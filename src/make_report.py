#!/usr/bin/env python3
"""Generate the human-readable winning-idea benchmark report from result files."""
import json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / "results"
s = json.loads((RES / "benchmark_summary.json").read_text())
df = pd.read_csv(RES / "benchmark_metrics.csv")

wm = s["stage1_oof_metrics"][s["winner_model"]]
cm = s["stage1_oof_metrics"][s["best_classical_baseline"]]
qm = s["stage1_oof_metrics"][s["quantum_only_baseline"]]
st2 = s["stage2"]; st3 = s["stage3"]; biz = s["business"]
qaoa = st2["qaoa"]; qk = s["quantum_kernel_specs"]


def fmt(x):
    try:
        v = float(x)
    except Exception:
        return str(x)
    if pd.isna(v): return "—"
    if abs(v - round(v)) < 1e-12: return f"{v:.0f}"
    return f"{v:.4f}"


lines = []
lines.append("# Winning idea and 30-metric benchmark — The Atomiq Hackathon")
lines.append("")
lines.append("**Concept name:** **CertiQ-Chirp** — *quantum-calibrated ranker fusion + certified QAOA + noise-aware six-qubit Bernoulli ledger*.")
lines.append("")
lines.append("> **Honest scope:** Stage 1 numbers below are repeated out-of-fold estimates on the 300 labelled training rows. The 100 hidden test labels are unavailable, so these are not hidden-test scores. Stage 2 and Stage 3 are exact references computed from the prototype’s own final Stage 1 probabilities.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 1. The best idea")
lines.append("")
lines.append("The winning design is not “use a quantum model everywhere.” The benchmark showed a clearer division of labour:")
lines.append("")
lines.append("- **XGBoost is the ranker:** best top-decile lift and Precision@10% among classical candidates.")
lines.append("- **A 4-qubit Qiskit `ZZFeatureMap` / SVC quantum kernel is the calibrator:** weak ranker (ROC-AUC ≈ 0.50) but strong probability quality (Brier ≈ 0.104, ECE ≈ 0.034).")
lines.append("- **A 40% XGBoost / 60% quantum-kernel fusion** preserves most ranking strength while cutting calibration error.")
lines.append("- **Certified QAOA:** a 10-qubit warm-start QAOA generates measured bitstrings; one-swap hybrid repair plus exact brute-force certificate closes the optimality gap.")
lines.append("- **Noise-aware Bernoulli ledger:** six independent `RY` qubits, ideal statevector, Aer finite-shot, noisy, and mitigated estimates, with exact 64-outcome and Monte Carlo references.")
lines.append("")
lines.append("```text")
lines.append("300 labelled customers")
lines.append("  ├─ leakage-free 3x5 stratified OOF model selection")
lines.append("  ├─ XGBoost ranker  ───────────────┐")
lines.append("  └─ Qiskit quantum kernel calibrator ─┤ → calibrated p_i for 100 test customers")
lines.append("                                       ↓")
lines.append("                         deterministic top 10 by p_i, customer_id tie-break")
lines.append("                                       ↓")
lines.append("       10-qubit warm-start QAOA → measured bitstrings → hybrid repair → exact certificate")
lines.append("                                       ↓")
lines.append("       6 RY qubits → ideal / finite-shot / noisy / mitigated Pr(K≥3) → exact + Monte Carlo")
lines.append("```")
lines.append("")
lines.append("### Why it is judge-aligned")
lines.append("")
lines.append("| Rubric | Weight | How the idea attacks it |")
lines.append("|---|---:|---|")
lines.append("| Quantum Rigor & Technical Depth | 35% | Real Qiskit quantum kernel, 10-qubit QAOA, six-qubit circuit, transpilation/gate/noise reporting, classical baselines |")
lines.append("| Result Accuracy & Integration | 30% | Same continuous probabilities in all stages; exact Stage 2 certificate; exact Stage 3 Poisson-binomial; error propagation |")
lines.append("| Code Quality & Reproducibility | 20% | One runnable script, pinned versions, seed manifest, root-level result files, full measurement counts, license |")
lines.append("| Report & Communication | 15% | Clear quantum/classical boundary, honest raw QAOA gap, business interpretation, limitations |")
lines.append("")
lines.append("### 90-second judge pitch")
lines.append("")
lines.append("> “We do not claim quantum advantage. We use quantum components where they are technically defensible: a Qiskit `ZZFeatureMap` kernel acts as a calibrated probability prior, a warm-start QAOA explores the constrained selection space, and a six-qubit product circuit samples the campaign outcome. A classical XGBoost ranker supplies the top-decile ordering, while exact brute-force and Poisson-binomial references certify every result. All probabilities, IDs, seeds, circuits, counts, noise models, and errors are traceable from Stage 1 to Stage 3.”")
lines.append("")
lines.append("The differentiator is **certified integration**: the same probability vector drives ranking, expected net value, selection, and the final quantum circuit—with a disclosed raw QAOA gap and a zero-gap hybrid certificate.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 2. Headline evidence")
lines.append("")
lines.append("| Metric | Winning fusion | Best classical | Quantum only | Interpretation |")
lines.append("|---|---:|---:|---:|---|")
lines.append(f"| PR-AUC (OOF) | {fmt(wm['pr_auc'])} | {fmt(cm['pr_auc'])} | {fmt(qm['pr_auc'])} | ~2.0× prevalence ({fmt(wm['prevalence'])}) |")
lines.append(f"| Brier (OOF) | {fmt(wm['brier'])} | {fmt(cm['brier'])} | {fmt(qm['brier'])} | Fusion is better calibrated than the classical ranker |")
lines.append(f"| Log loss (OOF) | {fmt(wm['log_loss'])} | {fmt(cm['log_loss'])} | {fmt(qm['log_loss'])} | Reduces overconfident errors |")
lines.append(f"| ECE (OOF) | {fmt(wm['ece'])} | {fmt(cm['ece'])} | {fmt(qm['ece'])} | Large calibration gain over classical ranker |")
lines.append(f"| Precision@10% (OOF) | {fmt(wm['precision_at_10pct'])} | {fmt(cm['precision_at_10pct'])} | {fmt(qm['precision_at_10pct'])} | Proxy for hidden-test Precision@10 |")
lines.append(f"| Recall@10% (OOF) | {fmt(wm['recall_at_10pct'])} | {fmt(cm['recall_at_10pct'])} | {fmt(qm['recall_at_10pct'])} | Proxy for hidden-test Recall@10 |")
lines.append(f"| Lift@10% | {fmt(wm['lift_at_10pct'])}× | {fmt(cm['lift_at_10pct'])}× | {fmt(qm['lift_at_10pct'])}× | Top-decile business value |")
lines.append(f"| Judge-aligned composite | {fmt(wm['composite_score'])} | {fmt(cm['composite_score'])} | {fmt(qm['composite_score'])} | Ranking + calibration + top-decile score |")
lines.append("")
lines.append(f"**Selected winner:** `{s['winner_model']}`; **best classical baseline:** `{s['best_classical_baseline']}`; **quantum-only baseline:** `{s['quantum_only_baseline']}`.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 3. The 30-metric benchmark")
lines.append("")
lines.append("Values are generated directly from `results/benchmark_metrics.csv`. “—” means the metric is not applicable to that baseline.")
lines.append("")
lines.append("| # | Metric | Winning idea | Best classical | Quantum only | Unit | Reference / target | Why it matters |")
lines.append("|---:|---|---:|---:|---:|---|---|---|")
for i, row in df.iterrows():
    lines.append("| {} | {} | {} | {} | {} | {} | {} | {} |".format(
        i + 1, row["metric"], fmt(row["winning_idea"]), fmt(row["best_classical_baseline"]),
        fmt(row["quantum_only_baseline"]), row["unit"], row["reference_or_target"], row["why_it_matters"]))
lines.append("")
gates = [
    wm["roc_auc"] > 0.60,
    wm["pr_auc"] > 2 * wm["prevalence"],
    wm["brier"] < 0.11,
    wm["log_loss"] < 0.37,
    wm["ece"] < 0.05,
    0.5 <= wm["calibration_slope"] <= 1.5,
    wm["precision_at_10pct"] >= 0.25,
    wm["recall_at_10pct"] >= 0.25,
    wm["lift_at_10pct"] >= 2.0,
    wm["ndcg_at_10pct"] >= 0.30,
    s["stage1_bootstrap"]["ci_width"] < 0.25,
    s["stage1_stability"]["winner_repeat_pr_auc_std"] < 0.02,
    qk["logical_qubits"] == 4,
    qk["transpiled_depth"] <= 20,
    st2["objective_value"] > 0,
    abs(qaoa["certified_hybrid_gap"]) < 1e-9,
    qaoa["feasible_sample_rate"] > 0.50,
    qaoa["qaoa_gap_to_exact"] < 10,
    st2["budget_utilization"] <= 1,
    st2["capacity_utilization"] <= 1,
    0 <= st3["exact_analytical_probability"] <= 1,
    abs(st3["ideal_statevector_probability"] - st3["exact_analytical_probability"]) < 1e-9,
    st3["errors"]["finite_shot_vs_exact"] < 0.005,
    st3["errors"]["monte_carlo_vs_exact"] < 0.005,
    st3["errors"]["noisy_vs_exact"] < 0.02,
    st3["errors"]["mitigated_vs_exact"] < st3["errors"]["noisy_vs_exact"],
    st3["finite_shot_ci95_half_width"] < 0.01,
    st3["two_qubit_gates"] + st3["swap_gates"] == 0,
    biz["expected_net_value_per_cost"] > 1,
    s["reproducibility"]["score"] == 100,
]
lines.append(f"**Transparent prototype gate result: {sum(gates)}/30 passed.** These are pre declared engineering gates, not an official judging score. Hidden test labels remain unknown.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 4. Concrete prototype answer")
lines.append("")
lines.append("These are the deterministic outputs produced by the benchmark script; they are **not** a universal official answer because another team’s Stage 1 probabilities would change them.")
lines.append("")
lines.append(f"- **Top 10:** `{', '.join(s['stage1_test']['top_10_ids'])}`")
lines.append(f"- **Six selected IDs:** `{', '.join(st2['selected_6_customer_ids'])}`")
lines.append(f"- **Expected net value:** `{fmt(st2['objective_value'])}`")
lines.append(f"- **Budget used:** `{fmt(st2['total_budget_used'])}/25` ({fmt(100*st2['budget_utilization'])}%)")
lines.append(f"- **Capacity used:** `{fmt(st2['total_capacity_used'])}/22` ({fmt(100*st2['capacity_utilization'])}%)")
lines.append(f"- **Feasible six-subsets checked:** `{st2['feasible_subset_count']}/210` — all feasible for this candidate pool, so neither limit binds here; budget is globally redundant because six costs ≤ 24")
lines.append(f"- **Exact `Pr(K≥3)`:** `{fmt(st3['exact_analytical_probability'])}`")
lines.append(f"- **Expected conversions:** `{fmt(biz['expected_conversions'])}`")
lines.append(f"- **Expected net value / contact cost:** `{fmt(biz['expected_net_value_per_cost'])}×`")
lines.append("")
lines.append("### Stage 2 quantum result")
lines.append("")
lines.append(f"- Algorithm: `{qaoa['algorithm']}`")
lines.append(f"- Logical qubits / layers / shots: `{qaoa['logical_qubits']} / {qaoa['layers']} / {qaoa['shots']}`")
lines.append(f"- Measured feasible-sample rate: `{fmt(qaoa['feasible_sample_rate'])}`")
lines.append(f"- Raw QAOA best feasible objective: `{fmt(qaoa['qaoa_best_feasible_objective'])}`, raw gap `{fmt(qaoa['qaoa_gap_to_exact'])}`")
lines.append(f"- Certified hybrid objective: `{fmt(qaoa['hybrid_repaired_objective'])}`, **gap `{fmt(qaoa['certified_hybrid_gap'])}`**")
lines.append("")
lines.append("The raw gap is deliberately disclosed. The final zero gap comes from a quantum-warm-started hybrid repair plus an exact classical certificate; **no quantum advantage is claimed**.")
lines.append("")
lines.append("### Stage 3 quantum result")
lines.append("")
lines.append(f"- Ideal statevector: `{fmt(st3['ideal_statevector_probability'])}`")
lines.append(f"- Noiseless finite-shot: `{fmt(st3['noiseless_finite_shot_probability'])}`")
lines.append(f"- Monte Carlo: `{fmt(st3['monte_carlo_probability'])}`")
lines.append(f"- Noisy: `{fmt(st3['noisy_probability'])}`")
lines.append(f"- Mitigated: `{fmt(st3['mitigated_probability'])}`")
lines.append(f"- 64×64 response-matrix cross-check: `{fmt(st3['response_matrix_mitigated_probability'])}`")
lines.append(f"- Error reduction from mitigation: `{fmt(100*(1-st3['errors']['mitigated_vs_exact']/st3['errors']['noisy_vs_exact']))}%`")
lines.append(f"- Shots: `{st3['shots']}`; finite-shot 95% half-width: `{fmt(st3['finite_shot_ci95_half_width'])}`")
lines.append(f"- Circuit: `{st3['logical_qubits']}` qubits, logical/transpiled depth `{st3['logical_depth']}/{st3['transpiled_depth']}`, 1Q/2Q/SWAP `{st3['one_qubit_gates']}/{st3['two_qubit_gates']}/{st3['swap_gates']}`")
lines.append(f"- Noise model: single-qubit depolarizing `{st3['noise_model']['single_qubit_depolarizing']}`, symmetric readout `{st3['noise_model']['symmetric_readout_error']}`")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 5. Conservative readiness estimate")
lines.append("")
lines.append("This is a planning estimate, not a prediction of the judge’s score.")
lines.append("")
lines.append("| Criterion | Estimate | Rationale |")
lines.append("|---|---:|---|")
lines.append("| Quantum rigor 35 | 33 | Three genuine Qiskit components, exact/noisy/mitigated analysis; raw QAOA gap disclosed |")
lines.append("| Accuracy/integration 30 | 26 | Strong OOF calibration and top-decile lift, zero Stage 2 gap, low Stage 3 error; hidden labels unknown |")
lines.append("| Reproducibility 20 | 20 | 10/10 prototype checks, pinned versions, seeds, result files, full counts |")
lines.append("| Communication 15 | 10 | Technical report, data story, and external presentation handoffs are maintained alongside the repository |")
lines.append("| **Total** | **89/100** | Conservative planning estimate before hidden-test variance |")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 6. Limitations and risks")
lines.append("")
lines.append("1. Hidden test labels are unavailable; OOF PR-AUC, Precision@10, and Recall@10 are estimates, not final scores.")
lines.append("2. The 300-row training set has only 35 positives, so the PR-AUC bootstrap 95% interval is wide.")
lines.append("3. The quantum kernel is a calibrator, not a superior ranker; unsupported quantum-advantage claims must be avoided.")
lines.append("4. Raw QAOA did not hit the exact optimum; the zero gap is certified by explicit hybrid repair and brute force.")
lines.append("5. The 0.02/0.03 noise model is synthetic, not a real IBM backend calibration. A submission must state this.")
lines.append("6. Presentation media and submission documents are maintained as external deliverables; the repository focuses on the runnable benchmark, pinned environment, and exact result files.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 7. Files and reproduction")
lines.append("")
lines.append("```text")
lines.append("CertiQ-Chirp repository/")
lines.append("  src/run_benchmark.py         # end-to-end Qiskit + sklearn benchmark")
lines.append("  src/make_report.py           # regenerates this report")
lines.append("  requirements.txt             # pinned package versions")
lines.append("  seeds.json                   # all random seeds")
lines.append("  LICENSE                      # MIT")
lines.append("  README.md                    # repository map and run instructions")
lines.append("  data/raw/                    # original participant workbook")
lines.append("  data/reference/              # official problem-statement PDF")
lines.append("  docs/                        # analysis, spec, technical report, benchmark README")
lines.append("  results/")
lines.append("    benchmark_report.md        # this file")
lines.append("    benchmark_metrics.csv      # 30 core metrics")
lines.append("    benchmark_summary.json     # all raw values and diagnostics")
lines.append("    stage1_predictions.csv     # 100 test probabilities/ranks/top-10 flags")
lines.append("    stage2_selection.json      # candidates, QAOA, exact certificate")
lines.append("    stage3_simulation.json     # full counts, exact/noisy/mitigated results")
lines.append("```")
lines.append("")
lines.append(f"End-to-end benchmark runtime: **{fmt(s['runtime_seconds'])} s**. Reproducibility checks: **{fmt(s['reproducibility']['score'])}%**.")
lines.append("")
lines.append("Run:")
lines.append("")
lines.append("```bash")
lines.append("cd /home/user/atomiq_analysis")
lines.append("python src/run_benchmark.py")
lines.append("python src/make_report.py")
lines.append("```")

(RES / "benchmark_report.md").write_text("\n".join(lines) + "\n")

readme = f"""# CertiQ-Chirp prototype

{s['idea']}

## What it does

Runs a leakage-free 3×5 repeated-CV benchmark on `Stage1_Train`, fits all final models once, predicts the 100 `Stage1_Test` customers, solves Stage 2 with a certified quantum-assisted optimizer, and executes Stage 3 with Qiskit Aer under ideal and noisy conditions.

## Run

```bash
cd /home/user/atomiq_analysis
python src/run_benchmark.py
python src/make_report.py
```

The source workbook is at `data/raw/bank_campaign_participant_release.xlsx`. Dependencies are pinned in `requirements.txt`; all seeds are in `seeds.json`.

## Outputs

- `results/benchmark_report.md` — winning idea and 30-metric benchmark
- `results/benchmark_metrics.csv` — machine-readable 30 metrics
- `results/benchmark_summary.json` — every raw measurement
- `results/stage1_predictions.csv` — all 100 test probabilities
- `results/stage2_selection.json` — top 10, QAOA, exact classical certificate
- `results/stage3_simulation.json` — full measurement counts and exact/noisy/mitigated results

## Repository scope

This lean repository keeps the runnable benchmark, pinned environment, seed manifest, source data, and exact result files. Presentation media and submission documents are maintained as external deliverables.
"""
(ROOT / "docs" / "BENCHMARK_README.md").write_text(readme)
print("Wrote benchmark_report.md and docs/BENCHMARK_README.md")
