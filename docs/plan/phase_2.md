# Phase 2 — Stage 1 — calibrated hybrid prediction

**File:** `docs/plan/phase_2.md`  
**Master:** [plan.md](plan.md)  
**Status:** ✅ Completed  
**Execution:** single-agent, end to end  
**Completed:** 2026-11-11 · IST  
**Completion report:** [phase_2_completion.md](phase_2_completion.md)

## 1. Goal

Produce one continuous, leakage-free probability vector for all 100 test customers, rank the top 10, and lock the Stage 1 metric suite.

## 2. Master plan context

| Phase | File | Title | Status |
|---|---|---|---|
| Phase 0 | [phase_0.md](phase_0.md) | Project charter, research lock & plan control | ✅ Completed |
| Phase 1 | [phase_1.md](phase_1.md) | Data, environment & reproducibility baseline | ✅ Completed |
| Phase 2 | [phase_2.md](phase_2.md) | Stage 1 — calibrated hybrid prediction | ✅ Completed |
| Phase 3 | [phase_3.md](phase_3.md) | Stage 2 — certified quantum-assisted selection | ✅ Completed |
| Phase 4 | [phase_4.md](phase_4.md) | Stage 3 — six-qubit conversion simulation | ✅ Completed |
| Phase 5 | [phase_5.md](phase_5.md) | End-to-end integration, 30-metric benchmark & validation | ✅ Completed |
| Phase 6 | [phase_6.md](phase_6.md) | Technical communication, evidence pack & submission handoff | ✅ Completed |

## 3. Dependencies

Phase 1.

## 4. Sub-phases — work packages

| ID | Sub-phase | Workstream | Objective | Validation detail | Evidence | Parallelizable? |
|---|---|---|---|---|---|---|
| 2.1 | Fold-local preprocessing | ML | Prevent leakage. | No transform is fit on validation or test folds. | `results/benchmark_summary.json` | No |
| 2.2 | Candidate model suite | ML | Benchmark classical and quantum probabilistic models. | Six models have OOF ROC-AUC, PR-AUC, Brier, log loss, and ECE. | `results/benchmark_summary.json` | Yes |
| 2.3 | Quantum kernel specification | Quantum | Define the Qiskit feature map. | 4 qubits, depth 17, 14 u / 12 CX, dimension 16 recorded. | `results/benchmark_summary.json` | Yes |
| 2.4 | Out-of-fold validation | Validation | Select models on training data only. | CI width 0.206885 and repeat std 0.016480 recorded. | `results/benchmark_summary.json` | Yes |
| 2.5 | Fusion selection | Validation | Choose the judge-aligned probability source. | Composite 0.447516 is the maximum; best classical and quantum-only baselines retained. | `results/benchmark_summary.json` | Yes |
| 2.6 | Single test prediction | ML | Freeze and predict once. | 100 rows, probabilities in [0,1], rank 1–100, 10 true flags. | `results/stage1_predictions.csv` | No |
| 2.7 | Stage 1 metric lock | Validation | Lock the evidence table. | Rows match summary JSON and technical report. | `results/benchmark_metrics.csv` | Yes |

### Sub-phase actions

- **2.1 Fold-local preprocessing** — Fit scaler, one-hot encoder, and PCA inside each training fold only. Output: `OOF prediction arrays`.
- **2.2 Candidate model suite** — Train logistic, HistGradientBoosting, LightGBM, CatBoost, XGBoost, and QSVC across 3×5 CV. Output: `OOF metric dictionary`.
- **2.3 Quantum kernel specification** — Use zz_feature_map(4, reps=1); record depth, gates, and statevector dimension. Output: `quantum_kernel_specs`.
- **2.4 Out-of-fold validation** — Compute repeated stratified CV metrics and bootstrap PR-AUC interval. Output: `stage1_oof_metrics, stage1_bootstrap`.
- **2.5 Fusion selection** — Sweep QSVC/XGBoost weights; lock 0.6/0.4 rank_calibrated_hybrid. Output: `winner_model`.
- **2.6 Single test prediction** — Fit final pipeline on all training data, predict 100 test customers, rank, flag top 10. Output: `results/stage1_predictions.csv`.
- **2.7 Stage 1 metric lock** — Write the 10 core Stage 1 metric rows plus 4 supporting rows in `benchmark_metrics.csv` and confirm exact values. Output: `results/benchmark_metrics.csv`.

### Sub-phase checklist

- [x] **2.1** Fold-local preprocessing — No transform is fit on validation or test folds.
- [x] **2.2** Candidate model suite — Six models have OOF ROC-AUC, PR-AUC, Brier, log loss, and ECE.
- [x] **2.3** Quantum kernel specification — 4 qubits, depth 17, 14 u / 12 CX, dimension 16 recorded.
- [x] **2.4** Out-of-fold validation — CI width 0.206885 and repeat std 0.016480 recorded.
- [x] **2.5** Fusion selection — Composite 0.447516 is the maximum; best classical and quantum-only baselines retained.
- [x] **2.6** Single test prediction — 100 rows, probabilities in [0,1], rank 1–100, 10 true flags.
- [x] **2.7** Stage 1 metric lock — Rows match summary JSON and technical report.

## 5. Validation details

**Phase gate:** 3×5 stratified OOF CV only; 100 unique test IDs; deterministic rank with customer_id tie-break; top-10 flag exactly 10 rows; winner rank_calibrated_hybrid composite 0.447516; metrics match benchmark_metrics.csv.

Every sub-phase above carries its own validation detail and evidence path. The phase is Verified only when all sub-phase checkboxes are checked and the phase gate matches the canonical result files.

## 6. Exact reference data

- Quantum kernel: 4 qubits, reps=1, logical/transpiled depth 17, 14 u, 12 CX, statevector dimension 16.
- Winner: 0.6 QSVC + 0.4 XGBoost = rank_calibrated_hybrid; best classical CatBoost; quantum-only QSVC.
- Winner OOF: ROC-AUC 0.6069, PR-AUC 0.234718, Brier 0.103644, log loss 0.360930, ECE 0.035671, slope 0.612382.
- Top-decile: P@10 0.300000, R@10 0.257143, lift 2.571429×, NDCG@10 0.362780, KS 0.231267.
- Bootstrap PR-AUC 95% CI [0.147250, 0.354135], width 0.206885; winner repeat PR-AUC std 0.016480.
- Top 10: C0170, C0256, C0327, C0338, C0188, C0079, C0081, C0374, C0059, C0372.
- Stage 1 metric table: 14 Stage 1 rows (10 core metrics plus 4 supporting rows) inside the 30-row benchmark table.
- Fresh-clone reproduction: 3×5 OOF CV, quantum kernel, fusion, and 100-row probability vector regenerated; 10 result/metadata files byte-identical.

## 7. Deliverables and evidence

- Canonical results: `results/`
- Documentation: `docs/`, `README.md`
- Source: `src/`
- Plan artifacts: `docs/plan/plan.md`, `docs/plan/phase_2_completion.md`, `docs/plan/TRACKER.csv`, `docs/plan/status.json`
- Per-sub-phase evidence is listed in the work-package table above.

## 8. Split-work guidance

ML workstream owns 2.1–2.2 and 2.6; quantum workstream owns 2.3; validation workstream owns 2.4–2.5 and 2.7.

## 9. Risks and controls

Test-set leakage or overconfident probabilities; mitigated by fold-local preprocessing, OOF fusion selection, and calibration metrics.

## 10. Definition of done

`results/stage1_predictions.csv` is the single probability source consumed by Phases 3 and 4. Verified by isolated fresh-clone full benchmark and report regeneration with 10 byte-identical result/metadata files.

## 11. End-to-end completion record

| Field | Value |
|---|---|
| Status | ✅ Completed |
| Execution | Single-agent, end to end, without splitting Phase 2 across workstreams |
| Completed | 2026-11-11 · IST |
| Sub-phases | 7 / 7 completed |
| Full report | [phase_2_completion.md](phase_2_completion.md) |
| Phase gate | PASS — leakage boundary, six-model suite, quantum kernel, OOF validation, fusion winner, single test prediction, and metric lock all validated |
| Fresh-clone result | `src/run_benchmark.py` and `src/make_report.py` succeeded; 10 result/metadata files byte-identical; canonical summary exact with timing fields normalized |
| Downstream handoff | All Phases 3–6 are ✅ Completed from the locked Stage 1 probability vector |

The completion report records the source-level audit, six-model OOF metrics, quantum kernel specification, composite ranking, winner metrics, top-10 probability table, 14 Stage 1 metric rows, isolated fresh-clone reproduction, validation matrix, and sign-off for every Phase 2 sub-phase.

---

Back to [master plan](plan.md) · [Plan README](README.md) · [Tracker](TRACKER.csv)
