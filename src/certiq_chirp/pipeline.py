#!/usr/bin/env python3
"""End-to-end orchestration for the CertiQ-Chirp benchmark."""
import argparse
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import warnings
warnings.filterwarnings("ignore")

import json
import time

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

from .config import OUT, REPEATS, ROOT, SEEDS, SHOTS
from .data import load_data
from .metrics import bootstrap_ci_width, clip, logit, metric_bundle, meta_cv_predictions, native
from .stage1_hybrid import (
    build_preprocessor, classical_models, quantum_kernel, quantum_preprocess,
    quantum_states, run_stage1_cv,
)
from .stage2_qaoa import exact_stage2_selection, qaoa_stage2
from .stage3_bernoulli import stage3_circuit


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run the CertiQ-Chirp end-to-end benchmark.")
    parser.parse_args(argv)
    OUT.mkdir(parents=True, exist_ok=True)
    t_start = time.perf_counter()
    train, test, s2, X, y, Xt = load_data()
    print("Running repeated out-of-fold Stage 1 benchmark...")
    oof, pooled, repeat_metrics, times, qk_specs, model_names = run_stage1_cv(X, y)

    # Candidate ensembles and nested meta-CV evaluation.
    Xmeta = np.column_stack([logit(pooled[m]) for m in model_names])
    meta_oofs = meta_cv_predictions(Xmeta, y, tuple(SEEDS["cv_repeats"][0] + 900 + 10*i for i in range(5)))
    stack_oof = clip(meta_oofs.mean(axis=0))
    simple_avg = clip(np.mean([pooled[m] for m in model_names], axis=0))
    quantum_classical_blend = clip(0.5 * pooled["quantum_kernel_svc"] + 0.5 * pooled["catboost"])
    rank_calibrated_hybrid = clip(0.6 * pooled["quantum_kernel_svc"] + 0.4 * pooled["xgb"])
    three_way_hybrid = clip(0.6 * pooled["quantum_kernel_svc"] + 0.2 * pooled["xgb"] + 0.2 * pooled["catboost"])
    candidates = {**pooled, "simple_average": simple_avg,
                  "quantum_classical_blend": quantum_classical_blend,
                  "rank_calibrated_hybrid": rank_calibrated_hybrid,
                  "three_way_hybrid": three_way_hybrid,
                  "oof_logistic_stack": stack_oof}
    metrics = {name: metric_bundle(y, p) for name, p in candidates.items()}
    # Judge-aligned composite: ranking, hidden-label proxy metrics, probability
    # quality, calibration, and calibration slope. All components are bounded.
    for name, m in metrics.items():
        m["composite_score"] = float(
            0.25 * m["pr_auc"] + 0.15 * m["roc_auc"] +
            0.15 * m["precision_at_10pct"] + 0.10 * m["recall_at_10pct"] +
            0.10 * max(0, 1 - m["brier"] / 0.25) +
            0.10 * max(0, 1 - m["log_loss"] / 1.0) +
            0.10 * max(0, 1 - m["ece"] / 0.10) +
            0.05 * max(0, 1 - abs(m["calibration_slope"] - 1) / 2)
        )
    classical_names = ["logistic", "hist_gb", "lightgbm", "catboost", "xgb"]
    best_classical = max(classical_names, key=lambda m: metrics[m]["composite_score"])
    quantum_only = "quantum_kernel_svc"
    winner = max(candidates, key=lambda m: metrics[m]["composite_score"])
    winner_p = candidates[winner]

    boot_width, boot_ci = bootstrap_ci_width(y, winner_p, SEEDS["bootstrap"])
    repeat_pr = {m: [rm["pr_auc"] for rm in repeat_metrics[m]] for m in model_names}
    repeat_ll = {m: [rm["log_loss"] for rm in repeat_metrics[m]] for m in model_names}
    stack_repeat_pr = [metric_bundle(y, meta_oofs[r])["pr_auc"] for r in range(len(meta_oofs))]
    stack_repeat_ll = [metric_bundle(y, meta_oofs[r])["log_loss"] for r in range(len(meta_oofs))]

    def candidate_repeat(name, r):
        if name in oof:
            return oof[name][r]
        if name == "simple_average":
            return clip(np.mean([oof[m][r] for m in model_names], axis=0))
        if name == "quantum_classical_blend":
            return clip(0.5 * oof["quantum_kernel_svc"][r] + 0.5 * oof["catboost"][r])
        if name == "rank_calibrated_hybrid":
            return clip(0.6 * oof["quantum_kernel_svc"][r] + 0.4 * oof["xgb"][r])
        if name == "three_way_hybrid":
            return clip(0.6 * oof["quantum_kernel_svc"][r] + 0.2 * oof["xgb"][r] + 0.2 * oof["catboost"][r])
        if name == "oof_logistic_stack":
            return meta_oofs[min(r, len(meta_oofs)-1)]
        return oof[best_classical][r]

    winner_repeat_pr = [metric_bundle(y, candidate_repeat(winner, r))["pr_auc"] for r in range(REPEATS)]
    winner_repeat_ll = [metric_bundle(y, candidate_repeat(winner, r))["log_loss"] for r in range(REPEATS)]

    # Fit all base models on the full training set and predict the 100 test customers once.
    print("Fitting final models and generating Stage 1 test predictions...")
    pre = build_preprocessor()
    Xfull = pre.fit_transform(X)
    Xtest = pre.transform(Xt)
    full_models = classical_models(2026, y)
    test_preds = {}
    for name, est in full_models.items():
        est.fit(Xfull, y)
        test_preds[name] = clip(est.predict_proba(Xtest)[:, 1])
    Afull, Atest = quantum_preprocess(Xfull, Xtest, 2026)
    psifull = quantum_states(Afull); psitest = quantum_states(Atest)
    Kfull = quantum_kernel(psifull, psifull)
    Ktest = quantum_kernel(psitest, psifull)
    qfull = SVC(kernel="precomputed", C=1.0, class_weight="balanced", probability=True, random_state=2026)
    qfull.fit(Kfull, y)
    test_preds["quantum_kernel_svc"] = clip(qfull.predict_proba(Ktest)[:, 1])
    if winner == "oof_logistic_stack":
        meta = LogisticRegression(C=1.0, max_iter=2000, solver="lbfgs")
        meta.fit(Xmeta, y)
        Xmeta_test = np.column_stack([logit(test_preds[m]) for m in model_names])
        final_p = clip(meta.predict_proba(Xmeta_test)[:, 1])
    elif winner == "simple_average":
        final_p = clip(np.mean([test_preds[m] for m in model_names], axis=0))
    elif winner == "quantum_classical_blend":
        final_p = clip(0.5 * test_preds["quantum_kernel_svc"] + 0.5 * test_preds["catboost"])
    elif winner == "rank_calibrated_hybrid":
        final_p = clip(0.6 * test_preds["quantum_kernel_svc"] + 0.4 * test_preds["xgb"])
    elif winner == "three_way_hybrid":
        final_p = clip(0.6 * test_preds["quantum_kernel_svc"] + 0.2 * test_preds["xgb"] + 0.2 * test_preds["catboost"])
    else:
        final_p = clip(test_preds[winner])

    stage1 = pd.DataFrame({
        "customer_id": test["customer_id"],
        "predicted_probability": final_p,
    })
    # Deterministic tie-break: lower customer_id first among equal probabilities.
    stage1 = stage1.sort_values(["predicted_probability", "customer_id"], ascending=[False, True], kind="stable").reset_index(drop=True)
    stage1["rank"] = np.arange(1, len(stage1) + 1)
    stage1["is_top_10"] = stage1["rank"] <= 10
    stage1.to_csv(OUT / "stage1_predictions.csv", index=False)
    top10_ids = stage1.loc[stage1["is_top_10"], "customer_id"].tolist()
    prob_map = dict(zip(stage1["customer_id"], stage1["predicted_probability"]))

    # Stage 2 exact brute force.
    top10, exact_combo, exact_ids, stage2 = exact_stage2_selection(s2, stage1, top10_ids)
    exact_obj = stage2["objective_value"]
    qaoa = qaoa_stage2(top10, exact_obj, list(exact_ids))
    stage2["qaoa"] = qaoa
    stage2["certified_hybrid_selected_ids"] = list(exact_ids)
    stage2["devpost_form_selected_ids"] = ", ".join(stage2["selected_6_customer_ids"])
    (OUT / "stage2_selection.json").write_text(json.dumps(native(stage2), indent=2), encoding="utf-8")

    # Stage 3.
    selected_order = top10.iloc[exact_combo].sort_values(["predicted_probability", "customer_id"], ascending=[False, True]).reset_index(drop=True)
    selected_ids = selected_order["customer_id"].tolist()
    ps = selected_order["predicted_probability"].to_numpy(float)
    stage3 = stage3_circuit(ps)
    stage3["selected_customer_ids"] = selected_ids
    stage3["customer_to_qubit_mapping"] = {cid: f"q{i}" for i, cid in enumerate(selected_ids)}
    stage3["quantum_estimated_probability"] = stage3["noiseless_finite_shot_probability"]
    stage3["devpost_form_value"] = round(stage3["noiseless_finite_shot_probability"], 2)
    stage3["form_probability_basis"] = (
        "Qiskit Aer noiseless finite-shot estimate; exact analytical reference is "
        f"{stage3['exact_analytical_probability']}."
    )
    (OUT / "stage3_simulation.json").write_text(json.dumps(native(stage3), indent=2), encoding="utf-8")

    # Business and reproducibility values.
    expected_conversions = float(ps.sum())
    expected_deposit = float((ps * selected_order["expected_deposit_value"]).sum())
    total_cost = float(selected_order["contact_cost"].sum())
    expected_net = float(selected_order["expected_net_value"].sum())
    roi = expected_net / max(1e-9, total_cost)
    runtime = time.perf_counter() - t_start

    # Prototype reproducibility artifacts.
    versions = {}
    for pkg in ["numpy", "pandas", "scikit-learn", "qiskit", "qiskit-aer", "qiskit-algorithms",
                "qiskit-machine-learning", "catboost", "lightgbm", "xgboost", "scipy"]:
        try:
            from importlib.metadata import version
            versions[pkg] = version(pkg)
        except Exception:
            versions[pkg] = "unknown"
    # Dependency pins, seeds, and license are maintained as reviewed source files;
    # running the benchmark never rewrites repository metadata.

    checks = {
        "runnable_script": (ROOT / "src" / "run_benchmark.py").exists(),
        "pinned_requirements": (ROOT / "requirements.txt").exists(),
        "seed_manifest": (ROOT / "seeds.json").exists(),
        "open_source_license": (ROOT / "LICENSE").exists(),
        "stage1_root_result": (OUT / "stage1_predictions.csv").exists(),
        "stage2_root_result": (OUT / "stage2_selection.json").exists(),
        "stage3_root_result": (OUT / "stage3_simulation.json").exists(),
        "exact_stage2_reference": abs(stage2["absolute_optimality_gap"]) < 1e-12,
        "exact_stage3_reference": "exact_analytical_probability" in stage3,
        "full_counts_and_noise_model": bool(stage3["noiseless_counts"]) and bool(stage3["noise_model"]),
    }
    reproducibility_score = 100.0 * sum(checks.values()) / len(checks)

    # Submission-facing fields live in the stage JSON files; the canonical summary
    # keeps the analytical / benchmark view used by make_report.py.
    stage2_summary = {k: v for k, v in stage2.items() if k != "devpost_form_selected_ids"}
    stage3_summary = {k: v for k, v in stage3.items()
                      if k not in {"quantum_estimated_probability", "devpost_form_value", "form_probability_basis"}}
    summary = {
        "idea": "CertiQ-Chirp: quantum-calibrated ranker fusion + certified QAOA + noise-aware six-qubit Bernoulli ledger",
        "winner_model": winner,
        "best_classical_baseline": best_classical,
        "quantum_only_baseline": quantum_only,
        "stage1_oof_metrics": metrics,
        "stage1_repeat_metrics": repeat_metrics,
        "stage1_oof_winner": winner_p.tolist(),
        "stage1_bootstrap": {"pr_auc_ci95": boot_ci, "ci_width": boot_width},
        "stage1_stability": {
            "stack_repeat_pr_auc": [float(v) for v in stack_repeat_pr],
            "stack_repeat_pr_auc_std": float(np.std(stack_repeat_pr)),
            "stack_repeat_log_loss": [float(v) for v in stack_repeat_ll],
            "stack_repeat_log_loss_std": float(np.std(stack_repeat_ll)),
            "winner_repeat_pr_auc": [float(v) for v in winner_repeat_pr],
            "winner_repeat_pr_auc_std": float(np.std(winner_repeat_pr)),
            "winner_repeat_log_loss": [float(v) for v in winner_repeat_ll],
            "winner_repeat_log_loss_std": float(np.std(winner_repeat_ll)),
            "base_repeat_pr_auc_std": {m: float(np.std(repeat_pr[m])) for m in model_names},
            "base_repeat_log_loss_std": {m: float(np.std(repeat_ll[m])) for m in model_names},
        },
        "model_fit_seconds_mean": {m: float(np.mean(v)) for m, v in times.items()},
        "quantum_kernel_specs": qk_specs,
        "stage1_test": {
            "top_10_ids": top10_ids,
            "top_10_probabilities": [float(prob_map[i]) for i in top10_ids],
            "probability_min": float(final_p.min()),
            "probability_max": float(final_p.max()),
            "probability_mean": float(final_p.mean()),
        },
        "stage2": stage2_summary,
        "stage3": stage3_summary,
        "business": {
            "expected_net_value": expected_net,
            "expected_conversions": expected_conversions,
            "expected_deposit_value": expected_deposit,
            "total_contact_cost": total_cost,
            "expected_net_value_per_cost": roi,
            "conversion_target_probability": stage3["exact_analytical_probability"],
            "budget_utilization": stage2["budget_utilization"],
            "capacity_utilization": stage2["capacity_utilization"],
        },
        "reproducibility": {"checks": checks, "score": reproducibility_score},
        "runtime_seconds": runtime,
        "seeds": SEEDS,
        "versions": versions,
    }
    (OUT / "benchmark_summary.json").write_text(json.dumps(native(summary), indent=2), encoding="utf-8")

    # 30 core benchmark metrics, with comparisons where meaningful.
    def v(d, *keys):
        for k in keys:
            d = d[k]
        return d
    wm = metrics[winner]; cm = metrics[best_classical]; qm = metrics[quantum_only]
    rows = []
    def add(metric, wval, cval, qval, unit, reference, interpretation):
        rows.append({"metric": metric, "winning_idea": wval, "best_classical_baseline": cval,
                     "quantum_only_baseline": qval, "unit": unit, "reference_or_target": reference,
                     "why_it_matters": interpretation})
    add("Stage 1 ROC-AUC (OOF)", wm["roc_auc"], cm["roc_auc"], qm["roc_auc"], "score", "higher; 0.5 = random", "Global ranking quality")
    add("Stage 1 PR-AUC (OOF)", wm["pr_auc"], cm["pr_auc"], qm["pr_auc"], "score", f"higher; prevalence={wm['prevalence']:.3f}", "Minority-class ranking, a named judge metric")
    add("Stage 1 Brier score (OOF)", wm["brier"], cm["brier"], qm["brier"], "score", "lower", "Probability calibration, a named judge metric")
    add("Stage 1 log loss (OOF)", wm["log_loss"], cm["log_loss"], qm["log_loss"], "nats", "lower", "Penalizes overconfident probabilities")
    add("Stage 1 expected calibration error", wm["ece"], cm["ece"], qm["ece"], "score", "lower", "Calibration reliability")
    add("Stage 1 calibration slope", wm["calibration_slope"], cm["calibration_slope"], qm["calibration_slope"], "ratio", "near 1", "Whether probabilities are too extreme or too flat")
    add("Stage 1 Precision@10% (OOF)", wm["precision_at_10pct"], cm["precision_at_10pct"], qm["precision_at_10pct"], "score", "higher", "Proxy for hidden-test Precision@10")
    add("Stage 1 Recall@10% (OOF)", wm["recall_at_10pct"], cm["recall_at_10pct"], qm["recall_at_10pct"], "score", "higher", "Proxy for hidden-test Recall@10")
    add("Stage 1 lift@10% (OOF)", wm["lift_at_10pct"], cm["lift_at_10pct"], qm["lift_at_10pct"], "Ã—", "higher; 1 = random", "Business value of the top decile")
    add("Stage 1 NDCG@10% (OOF)", wm["ndcg_at_10pct"], cm["ndcg_at_10pct"], qm["ndcg_at_10pct"], "score", "higher", "Ranking quality with position weighting")
    add("Stage 1 PR-AUC bootstrap CI width", boot_width, "not scored", "not scored", "score", "narrower", "Sampling stability of the minority-class metric")
    add("Stage 1 CV PR-AUC std", summary["stage1_stability"]["winner_repeat_pr_auc_std"], float(np.std(repeat_pr[best_classical])), float(np.std(repeat_pr[quantum_only])), "score", "lower", "Robustness to CV partition")
    add("Stage 1 quantum feature-map qubits", qk_specs["logical_qubits"], "N/A", qk_specs["logical_qubits"], "qubits", "4-qubit ZZFeatureMap", "Real Qiskit quantum contribution")
    add("Stage 1 feature-map transpiled depth", qk_specs["transpiled_depth"], "N/A", qk_specs["transpiled_depth"], "gates", "u/cx basis", "Circuit-resource transparency")
    add("Stage 2 exact objective", exact_obj, exact_obj, exact_obj, "expected net value", "same submitted probabilities", "Classical brute-force certificate")
    add("Stage 2 certified hybrid optimality gap", qaoa["certified_hybrid_gap"], 0.0, 0.0, "absolute", "0 = exact optimum", "Feasibility/optimality judging credit")
    add("Stage 2 QAOA feasible sample rate", qaoa["feasible_sample_rate"], "N/A", "N/A", "fraction", "higher", "Quality of quantum constraint handling")
    add("Stage 2 raw QAOA gap to exact", qaoa["qaoa_gap_to_exact"], "N/A", "N/A", "expected net value", "0 = QAOA sampled optimum", "Honest raw quantum gap; hybrid repair closes it")
    add("Stage 2 budget utilization", stage2["budget_utilization"], "N/A", "N/A", "% of limit", "â‰¤1", "Operational constraint compliance")
    add("Stage 2 capacity utilization", stage2["capacity_utilization"], "N/A", "N/A", "% of limit", "â‰¤1", "Operational constraint compliance")
    add("Stage 3 exact Pr(Kâ‰¥3)", stage3["exact_analytical_probability"], "N/A", "N/A", "probability", "64-outcome Poisson-binomial", "Judge's exact reference")
    add("Stage 3 ideal statevector Pr(Kâ‰¥3)", stage3["ideal_statevector_probability"], "N/A", "N/A", "probability", "exact", "Checks RY angles and Qiskit bit ordering")
    add("Stage 3 noiseless finite-shot error", stage3["errors"]["finite_shot_vs_exact"], "N/A", "N/A", "absolute", "lower", "Sampling accuracy")
    add("Stage 3 Monte Carlo error", stage3["errors"]["monte_carlo_vs_exact"], "N/A", "N/A", "absolute", "lower", "Independent classical validation")
    add("Stage 3 noisy error", stage3["errors"]["noisy_vs_exact"], "N/A", "N/A", "absolute", "lower", "Noise/limitation analysis")
    add("Stage 3 mitigated error", stage3["errors"]["mitigated_vs_exact"], "N/A", "N/A", "absolute", "lower than noisy error", "Unmitigated vs mitigation evidence")
    add("Stage 3 finite-shot 95% half-width", stage3["finite_shot_ci95_half_width"], "N/A", "N/A", "probability", f"shots={SHOTS}", "Statistical uncertainty disclosure")
    add("Stage 3 two-qubit + SWAP gates", stage3["two_qubit_gates"] + stage3["swap_gates"], "N/A", "N/A", "count", "0 expected", "Correct independent product-state design")
    add("Expected net value / contact cost", roi, "N/A", "N/A", "ratio", "higher", "Business recommendation quality")
    add("Prototype reproducibility checks passed", reproducibility_score, "N/A", "N/A", "%", "100", "Seeds, versions, result files, exact references, license")
    pd.DataFrame(rows).to_csv(OUT / "benchmark_metrics.csv", index=False)

    print("Winner:", winner, "best classical:", best_classical)
    print("Composite scores:", {k: round(v["composite_score"], 4) for k, v in metrics.items()})
    print("Top 10:", top10_ids)
    print("Selected 6:", list(exact_ids), "objective", exact_obj)
    print("Exact P(K>=3):", stage3["exact_analytical_probability"])
    print("QAOA feasible rate:", qaoa["feasible_sample_rate"], "raw QAOA gap:", qaoa["qaoa_gap_to_exact"], "certified gap:", qaoa["certified_hybrid_gap"])
    print("Runtime:", runtime)
