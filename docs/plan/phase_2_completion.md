# Phase 2 — End-to-End Completion Report

**Project:** CertiQ-Chirp: Certified Quantum Campaign Intelligence  
**Phase:** 2 — Stage 1 — calibrated hybrid prediction  
**Status:** ✅ Completed  
**Execution:** single-agent, end to end, without splitting Phase 2 across workstreams  
**Completed:** 2026-11-11 · IST  
**Dependency:** [Phase 1 completion](phase_1_completion.md)  
**Work package:** [`phase_2.md`](phase_2.md) · **Master:** [`plan.md`](plan.md)

> **Outcome:** Phase 2 is complete. The leakage-free 3×5 OOF benchmark, six-model suite, four-qubit quantum kernel, 0.6/0.4 fusion winner, single 100-row test-probability vector, top-10 ranking, and Stage 1 metric table were validated. A full benchmark and report regeneration were executed in an isolated fresh clone with 10 byte-identical result/metadata files.

---

## 1. What was executed

The workspace `phase_2.md` was read in full. All seven sub-phases were executed in one continuous pass from the retained source of truth. No external submission or code links, and no placeholder team fields, were introduced.

| ID | Sub-phase | Action performed | Validation | Evidence | Result |
|---|---|---|---|---|---|
| 2.1 | Fold-local preprocessing | Audited `build_preprocessor`, `run_stage1_cv`, and `quantum_preprocess`; verified scaler, one-hot encoder, PCA, and MinMaxScaler are fit only on training folds. | 14/14 source checks PASS; 3×5 stratified OOF CV only. | `src/run_benchmark.py`, `results/benchmark_summary.json` | PASS |
| 2.2 | Candidate model suite | Confirmed six OOF models: logistic, HistGradientBoosting, LightGBM, CatBoost, XGBoost, QSVC; all five core metric fields present. | 6/6 models have ROC-AUC, PR-AUC, Brier, log loss, ECE. | `results/benchmark_summary.json` | PASS |
| 2.3 | Quantum kernel specification | Confirmed `zz_feature_map(4, reps=1)`, statevector states, precomputed kernel SVC, and recorded transpiled resources. | 4 qubits, depth 17, 14 u / 12 CX, dimension 16. | `results/benchmark_summary.json` | PASS |
| 2.4 | Out-of-fold validation | Verified repeated CV, bootstrap PR-AUC interval, winner repeat stability, and training-only selection. | CI width 0.206885378; winner repeat PR-AUC std 0.016480408. | `results/benchmark_summary.json` | PASS |
| 2.5 | Fusion selection | Verified judge-aligned composite ranking and 0.6 QSVC + 0.4 XGBoost winner; best classical and quantum-only baselines retained. | `rank_calibrated_hybrid` composite 0.44751619741509907 is the maximum. | `results/benchmark_summary.json` | PASS |
| 2.6 | Single test prediction | Verified full-training fit, single test transform, deterministic rank with customer_id tie-break, and top-10 flag. | 100 rows; probabilities in [0,1]; ranks 1–100; 10 top-10 flags. | `results/stage1_predictions.csv` | PASS |
| 2.7 | Stage 1 metric lock | Cross-checked all 14 Stage 1 rows against canonical summary and technical report; full 30-row table retained. | 14 Stage 1 rows exact; 30 total metric rows. | `results/benchmark_metrics.csv`, `docs/04_TECHNICAL_REPORT.md` | PASS |

## 2. Source-level leakage and design audit — 2.1–2.3

**Source:** [`src/run_benchmark.py`](../../src/run_benchmark.py) · **Compile:** PASS

| Code-level check | Result |
|---|---|
| REPEATS = 3 | PASS |
| FOLDS = 5 | PASS |
| N_QK = 4 | PASS |
| P_QK = 1 | PASS |
| ColumnTransformer preprocessing | PASS |
| fold-local pre.fit_transform | PASS |
| fold-local pre.transform | PASS |
| fold-local PCA/MinMax | PASS |
| zz_feature_map(4, reps=1) | PASS |
| 0.6 QSVC + 0.4 XGB fusion | PASS |
| single final test transform | PASS |
| final winner formula | PASS |
| deterministic rank tie-break | PASS |
| top-10 flag | PASS |

- **CV design:** `REPEATS = 3`, `FOLDS = 5`, `StratifiedKFold(shuffle=True)` with seeds `[42, 142, 242]`.
- **Fold boundary:** `pre.fit_transform(X.iloc[tr])` followed by `pre.transform(X.iloc[va])`; quantum PCA and MinMaxScaler are also fit on the training fold only.
- **Final fit:** one full-training `fit_transform` and one test `transform`; the 100 test customers are predicted once.
- **Model suite:** `logistic`, `hist_gb`, `lightgbm`, `catboost`, `xgb`, `quantum_kernel_svc`.

### Six-model OOF metric coverage

| Model | ROC-AUC | PR-AUC | Brier | Log loss | ECE |
|---|---|---|---|---|---|
| logistic | 0.572183 | 0.185908 | 0.206288 | 0.602786 | 0.286460 |
| hist_gb | 0.564960 | 0.230767 | 0.120750 | 0.446714 | 0.119885 |
| lightgbm | 0.608194 | 0.230521 | 0.131082 | 0.449848 | 0.116167 |
| catboost | 0.629111 | 0.224278 | 0.116357 | 0.402256 | 0.087666 |
| xgb | 0.603127 | 0.242103 | 0.131140 | 0.438090 | 0.112946 |
| quantum_kernel_svc | 0.499191 | 0.122644 | 0.103939 | 0.363919 | 0.034161 |

### Quantum kernel specification

| Field | Value |
|---|---|
| logical_qubits | 4 |
| reps | 1 |
| logical_depth | 17 |
| transpiled_depth | 17 |
| transpiled_ops | {"u": 14, "cx": 12} |
| statevector_dimension | 16 |

## 3. Out-of-fold validation and fusion selection — 2.4–2.5

**Bootstrap:** 95% PR-AUC interval `[0.14725000895182838, 0.354135387006292]` · width **0.2068853780544636**  
**Winner repeat stability:** PR-AUC std **0.01648040832314972** · log-loss std **0.004320007123499389**

### Judge-aligned composite ranking

| Rank | Candidate | Composite |
|---|---|---|
| 1 | rank_calibrated_hybrid | 0.447516 |
| 2 | three_way_hybrid | 0.443989 |
| 3 | quantum_classical_blend | 0.438135 |
| 4 | oof_logistic_stack | 0.384932 |
| 5 | simple_average | 0.371248 |
| 6 | catboost | 0.363757 |
| 7 | xgb | 0.357286 |
| 8 | quantum_kernel_svc | 0.345957 |
| 9 | hist_gb | 0.341965 |
| 10 | lightgbm | 0.336956 |
| 11 | logistic | 0.269519 |

**Winner:** `rank_calibrated_hybrid` = **0.6 QSVC + 0.4 XGBoost**  
**Best classical baseline:** `catboost`  
**Quantum-only baseline:** `quantum_kernel_svc`

### Winner OOF metrics

| Metric | Exact value |
|---|---|
| roc_auc | 0.606900270 |
| pr_auc | 0.234717571 |
| brier | 0.103644171 |
| log_loss | 0.360930106 |
| ece | 0.035671404 |
| mce | 0.134273353 |
| calibration_slope | 0.612382480 |
| calibration_intercept | -0.947729306 |
| precision_at_10pct | 0.300000000 |
| recall_at_10pct | 0.257142857 |
| f1_at_10pct | 0.276923077 |
| lift_at_10pct | 2.571428571 |
| ndcg_at_10pct | 0.362780329 |
| ks | 0.231266846 |
| accuracy_0.5 | 0.883333333 |
| prevalence | 0.116666667 |
| k_top | 30.000000000 |
| composite_score | 0.447516197 |

## 4. Single test prediction — 2.6

**Canonical file:** [`results/stage1_predictions.csv`](../../results/stage1_predictions.csv)

| Check | Value |
|---|---|
| Rows | 100 |
| Unique customer IDs | 100 |
| Probability minimum | 0.0432623871278877 |
| Probability mean | 0.16247591836039937 |
| Probability maximum | 0.4515878093151118 |
| Rank range | 1–100 |
| Top-10 flags | 10 |
| Tie-break | `predicted_probability` descending, then `customer_id` ascending |
| Downstream use | same probability vector feeds Stage 2 expected net value and Stage 3 Bernoulli qubits |

### Locked top 10

| Rank | Customer ID | Predicted probability |
|---|---|---|
| 1 | C0170 | 0.451587809315112 |
| 2 | C0256 | 0.434955481805204 |
| 3 | C0327 | 0.418134568251759 |
| 4 | C0338 | 0.379853593971886 |
| 5 | C0188 | 0.361197859231245 |
| 6 | C0079 | 0.346319801895272 |
| 7 | C0081 | 0.334811376538831 |
| 8 | C0374 | 0.330473588552998 |
| 9 | C0059 | 0.328801432166969 |
| 10 | C0372 | 0.323021482529514 |

## 5. Stage 1 metric lock — 2.7

`benchmark_metrics.csv` contains **30 total rows**, of which **14 are Stage 1 rows**: 10 core judge-aligned metrics plus 4 supporting rows for bootstrap width, CV stability, feature-map qubits, and transpiled depth. The technical report carries the locked 4-decimal values.

| # | Metric | Winning idea | Best classical | Quantum-only |
|---|---|---|---|---|
| 1 | Stage 1 ROC-AUC (OOF) | 0.606900269 | 0.6291105121293801 | 0.49919137466307273 |
| 2 | Stage 1 PR-AUC (OOF) | 0.234717571 | 0.22427803385763548 | 0.12264388117266026 |
| 3 | Stage 1 Brier score (OOF) | 0.103644171 | 0.11635690947127046 | 0.10393886243329917 |
| 4 | Stage 1 log loss (OOF) | 0.360930106 | 0.4022557304844892 | 0.36391863520815265 |
| 5 | Stage 1 expected calibration error | 0.035671404 | 0.08766574388820682 | 0.034161184226422205 |
| 6 | Stage 1 calibration slope | 0.612382480 | 0.3101817445901248 | -0.15530313011805053 |
| 7 | Stage 1 Precision@10% (OOF) | 0.300000000 | 0.23333333333333334 | 0.13333333333333333 |
| 8 | Stage 1 Recall@10% (OOF) | 0.257142857 | 0.2 | 0.11428571428571428 |
| 9 | Stage 1 lift@10% (OOF) | 2.571428571 | 2.0 | 1.1428571428571428 |
| 10 | Stage 1 NDCG@10% (OOF) | 0.362780329 | 0.29476975857714693 | 0.09845212737965606 |
| 11 | Stage 1 PR-AUC bootstrap CI width | 0.206885378 | not scored | not scored |
| 12 | Stage 1 CV PR-AUC std | 0.016480408 | 0.018430982797063546 | 0.009466225774401415 |
| 13 | Stage 1 quantum feature-map qubits | 4.000000000 | — | 4 |
| 14 | Stage 1 feature-map transpiled depth | 17.000000000 | — | 17 |

## 6. Fresh-clone reproduction

**Commands verified**

```bash
python -m py_compile src/run_benchmark.py src/make_report.py
python src/run_benchmark.py
python src/make_report.py
```

The full benchmark and report-generation commands were run inside an isolated temporary clone, leaving the workspace canonical results untouched. The pinned stack from Phase 1 remained exact.

| Run | Return code | Timing | Output |
|---|---:|---:|---|
| `src/run_benchmark.py` | 0 | wall 93.757 s · runtime 91.18588580300002 s | Stage 1/2/3 results regenerated |
| `src/make_report.py` | 0 | — | `Wrote benchmark_report.md and docs/BENCHMARK_README.md` |

**Benchmark log tail**

```text
Top 10: ['C0170', 'C0256', 'C0327', 'C0338', 'C0188', 'C0079', 'C0081', 'C0374', 'C0059', 'C0372']
Selected 6: ['C0059', 'C0170', 'C0256', 'C0327', 'C0372', 'C0374'] objective 45.78743946915947
Exact P(K>=3): 0.4164131424084104
QAOA feasible rate: 0.681396484375 raw QAOA gap: 5.047731581776915 certified gap: 0.0
Runtime: 91.18588580300002
```

### Byte-identical result artifacts

| File | Canonical SHA-256 prefix | Comparison |
|---|---|---|
| `results/stage1_predictions.csv` | 71f3d313e35c4eaf | byte-identical |
| `results/stage2_selection.csv` | 2533f6e46c021f95 | byte-identical |
| `results/stage2_selection.json` | 74e12531a9ceb77c | byte-identical |
| `results/stage3_simulation.csv` | 856fc26fd39409be | byte-identical |
| `results/stage3_simulation.json` | c239d29e5c71f7ed | byte-identical |
| `results/benchmark_metrics.csv` | 3c6d0de6134ed242 | byte-identical |
| `requirements.txt` | 52d618446b03d4d8 | byte-identical |
| `seeds.json` | fb33d285adef2692 | byte-identical |
| `LICENSE` | 11767978e72b80fd | byte-identical |
| `docs/BENCHMARK_README.md` | 066bc9221cdef928 | byte-identical |

- `benchmark_summary.json`: every non-timing value is exact; only `runtime_seconds` and `model_fit_seconds_mean` are timing-dependent.
- `results/benchmark_report.md` and `docs/04_TECHNICAL_REPORT.md`: identical after normalizing the single runtime line.
- `docs/BENCHMARK_README.md`: byte-identical.
- Fresh reproducibility score: **100.0%**.
- Reproduction summary: **10 result/metadata files byte-identical**.

## 7. Validation results

| Check | Result detail | Outcome |
|---|---|---|
| Source audit | 14 code-level checks PASS; Python compile PASS | PASS |
| Leakage boundary | Fold-local preprocessing; test set transformed once after full-training fit | PASS |
| Quantum kernel | 4 qubits · reps 1 · depth 17 · 14 u / 12 CX · dimension 16 | PASS |
| Fusion winner | rank_calibrated_hybrid composite 0.44751619741509907 | PASS |
| Baselines | Best classical catboost · quantum-only quantum_kernel_svc | PASS |
| Bootstrap / stability | CI width 0.2068853780544636 · winner repeat PR-AUC std 0.01648040832314972 | PASS |
| Prediction vector | 100 rows · 100 unique IDs · probability 0.0432623871278877–0.4515878093151118 · mean 0.16247591836039937 | PASS |
| Top 10 | C0170, C0256, C0327, C0338, C0188, C0079, C0081, C0374, C0059, C0372 | PASS |
| Metric table | 14 Stage 1 rows · 30 total rows · technical-report tokens exact | PASS |
| Fresh-clone benchmark | RC 0 · wall 93.757 s · runtime 91.18588580300002 s | PASS |
| Fresh-clone report generation | RC 0 · `Wrote benchmark_report.md and docs/BENCHMARK_README.md` | PASS |
| Exact reproduction | 10 files byte-identical; summary non-timing exact; reports exact after runtime normalization | PASS |
| Downstream traceability | Stage 2/3 results regenerated exactly from the same Stage 1 probability vector | PASS |

## 8. Plan and tracking updates

| Artifact | Update |
|---|---|
| [`phase_2.md`](phase_2.md) | Status → ✅ Completed; single-agent execution head; Section 11 completion record |
| [`phase_3_completion.md`](phase_3_completion.md) | Stage 2 certified quantum-assisted selection execution record |
| [`phase_4_completion.md`](phase_4_completion.md) | Stage 3 six-qubit conversion simulation execution record |
| [`phase_5_completion.md`](phase_5_completion.md) | End-to-end integration, 30-metric benchmark, and validation execution record |
| [`phase_6_completion.md`](phase_6_completion.md) | Technical communication, evidence pack, and submission handoff execution record |
| [`plan.md`](plan.md) | Phase 2 status → ✅ Completed; Phase 2 subphase register → Completed; completion-report links and Stage 1 digest updated |
| [`README.md`](README.md) | Plan-folder index now lists Phase 0–6 completion records |
| [`TRACKER.csv`](TRACKER.csv) | Phase 2 rows → Completed with single-agent completion evidence |
| [`status.json`](status.json) | Top-level status → Phases 0–6 Completed · All phases Verified; Phase 2–6 completion objects recorded |
| [`phase_0.md`](phase_0.md) / [`phase_1.md`](phase_1.md) | Downstream status and plan-layer counts refreshed |
| [`phase_3.md`](phase_3.md) … [`phase_6.md`](phase_6.md) | Master-plan context reflects Phases 0–6 as Completed |
| [`../../README.md`](../../README.md) | Repository entry point links the Phase 0–6 completion records |
| [`../../MANIFEST.md`](../../MANIFEST.md) / [`../../CLEANUP_REPORT.md`](../../CLEANUP_REPORT.md) | Re-indexed to the final lean repo |

## 9. Downstream handoff and change control

1. All Phases 3–6 are ✅ Completed from the locked top 10 and six selected probabilities.
2. A change to Stage 1 probabilities re-opens Phases 2–6 and refreshes all downstream completion records.
3. A change to the model suite, kernel, or fusion weights updates this report and re-runs `src/run_benchmark.py` plus `src/make_report.py`.
4. Bulky presentation, PDF, media, and archive handoffs remain outside the lean repository; `.gitignore` keeps them from returning.

## 10. Sign-off

| Field | Value |
|---|---|
| Phase gate | **PASS** |
| Sub-phases | **7 / 7 Completed** |
| Leakage boundary | **3×5 stratified OOF CV · fold-local preprocessing · one test prediction** |
| Quantum kernel | **4 qubits · depth 17 · 14 u / 12 CX · dimension 16** |
| Fusion winner | **`rank_calibrated_hybrid` · composite 0.44751619741509907** |
| Probability vector | **100 rows · ranks 1–100 · 10 top-10 flags** |
| Metric table | **14 Stage 1 rows · 30 total rows** |
| Fresh-clone reproduction | **PASS — 10 files byte-identical** |
| Reproducibility score | **100%** |
| Status | **✅ Completed** |
| Execution mode | **Single-agent, end to end** |
| Timestamp | **2026-11-11 · IST** |

Back to [`phase_2.md`](phase_2.md) · [`plan.md`](plan.md) · [`TRACKER.csv`](TRACKER.csv) · [`status.json`](status.json)
