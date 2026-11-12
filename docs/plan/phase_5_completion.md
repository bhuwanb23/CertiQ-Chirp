# Phase 5 — End-to-End Completion Report

**Project:** CertiQ-Chirp: Certified Quantum Campaign Intelligence  
**Phase:** 5 — End-to-end integration, 30-metric benchmark & validation  
**Status:** ✅ Completed  
**Execution:** single-agent, end to end, without splitting Phase 5 across workstreams  
**Completed:** 2026-11-11 · IST  
**Dependency:** [Phase 2 completion](phase_2_completion.md) · [Phase 3 completion](phase_3_completion.md) · [Phase 4 completion](phase_4_completion.md)  
**Work package:** [`phase_5.md`](phase_5.md) · **Master:** [`plan.md`](plan.md)

> **Outcome:** Phase 5 is complete. Continuous Stage 1→Stage 2→Stage 3 probability propagation, end-to-end `customer_id` traceability, cross-stage error propagation, the complete 30-metric benchmark table and 30/30 engineering gates, the 10/10 reproducibility checklist (`100.0%`), the conservative rubric-aligned `89/100` planning estimate (`33/26/20/10`), and the 6-item honest limitation register were verified across `results/`, `docs/04_TECHNICAL_REPORT.md`, and `README.md`. An isolated fresh-clone full benchmark and report regeneration passed with 10 byte-identical result/metadata files; the canonical root results were unchanged.

---

## 1. What was executed

The workspace `phase_5.md` was read in full. All seven sub-phases were executed in one continuous single-agent pass from the retained source of truth: `src/run_benchmark.py`, `src/make_report.py`, `results/stage1_predictions.csv`, `results/stage2_selection.json`, `results/stage2_selection.csv`, `results/stage3_simulation.json`, `results/stage3_simulation.csv`, `results/benchmark_metrics.csv`, `results/benchmark_summary.json`, `results/benchmark_report.md`, `docs/04_TECHNICAL_REPORT.md`, `README.md`, `requirements.txt`, `seeds.json`, and `LICENSE`. No external submission or code links, and no placeholder team fields, were introduced.

| ID | Sub-phase | Action performed | Validation | Evidence | Result |
|---|---|---|---|---|---|
| 5.1 | Continuous probability propagation | Verified that all 10 Stage 2 `candidate_inputs` (`wᵢ = pᵢvᵢ − cᵢ`) and all 6 Stage 3 `input_probabilities` / `ry_angles` come unmodified from `results/stage1_predictions.csv`. | Max absolute Stage 1→Stage 2 diff `0.0`; Stage 1→Stage 3 diff `0.0`; angles match `2 arcsin √pᵢ` to `≤ 1e-12`. | `results/stage1_predictions.csv`, `results/stage2_selection.json`, `results/stage3_simulation.json` | PASS |
| 5.2 | ID traceability | Traced all 10 top-ranked IDs into the 6 certified Stage 2 IDs (`devpost_form_selected_ids`) and the 6 Stage 3 qubits (`customer_to_qubit_mapping`) across CSV and JSON views. | Same 6 IDs appear in `stage1_predictions.csv`, `stage2_selection.*`, `stage3_simulation.*`, `benchmark_summary.json`, `benchmark_report.md`, `04_TECHNICAL_REPORT.md`, and `README.md`. | `results/stage2_selection.json`, `results/stage3_simulation.json` | PASS |
| 5.3 | Error propagation analysis | Audited Stage 1 bootstrap CI width (`0.206885`), CV repeat PR-AUC std (`0.016480`), Stage 2 raw vs certified gaps (`5.047732 → 0.0`), and Stage 3 finite-shot/MC/noisy/mitigated/NNLS errors (`0.003966`, `0.001283`, `0.014922`, `0.004015`, `0.005302`). | All uncertainty and error terms present in `benchmark_summary.json`, `benchmark_metrics.csv`, and `benchmark_report.md`. | `results/benchmark_summary.json`, `results/benchmark_report.md` | PASS |
| 5.4 | 30-metric table | Verified all 30 rows, 7 columns, exact baseline comparisons, units, targets, rationales, and 30/30 engineering gate thresholds. | `30` rows exact; `30/30` pre-declared engineering gates passed. | `results/benchmark_metrics.csv`, `src/make_report.py` | PASS |
| 5.5 | Reproducibility checks | Verified all 10 boolean checks in `benchmark_summary.json["reproducibility"]`, pinned versions, seed manifest, MIT license, canonical runtime `145.9735211939999 s`, and isolated fresh-clone rerun. | `10/10` checks `true`; score `100.0%`; 10 files byte-identical in fresh clone. | `results/benchmark_summary.json`, `requirements.txt`, `seeds.json`, `LICENSE` | PASS |
| 5.6 | Readiness estimate | Verified the rubric-mapped planning table (`33/35`, `26/30`, `20/20`, `10/15` = `89/100`) and explicit non-official-score disclaimer. | Exact `89/100` (`33/26/20/10`) and planning disclaimer present in both generated and docs technical reports. | `docs/04_TECHNICAL_REPORT.md`, `results/benchmark_report.md` | PASS |
| 5.7 | Honest limitation register | Verified all 6 numbered limitations plus explicit no-quantum-advantage claim discipline across report and README. | All 6 constraints verbatim in Section 6 of `docs/04_TECHNICAL_REPORT.md`; byte-identical to `results/benchmark_report.md`. | `docs/04_TECHNICAL_REPORT.md`, `README.md` | PASS |

## 2. Source-level integration audit and pinned environment

**Sources:** [`src/run_benchmark.py`](../../src/run_benchmark.py) and [`src/make_report.py`](../../src/make_report.py) · **Python compile:** PASS · **Source checks:** **22 / 22 PASS**

| Code-level check | Result |
|---|---|
| `Stage 1 probability map` | PASS |
| `Stage 2 merge from Stage 1 probabilities` | PASS |
| `Stage 2 expected_net_value formula` | PASS |
| `Stage 2 devpost_form_selected_ids` | PASS |
| `Stage 3 selected_order from exact_combo` | PASS |
| `Stage 3 ps from selected_order` | PASS |
| `Stage 3 customer_to_qubit_mapping` | PASS |
| `Reproducibility 10-check block` | PASS |
| `Summary stage2 filter` | PASS |
| `Summary stage3 filter` | PASS |
| `Summary bootstrap block` | PASS |
| `Summary stability block` | PASS |
| `Summary business block` | PASS |
| `30-metric writer to benchmark_metrics.csv` | PASS |
| `make_report reads benchmark_summary.json` | PASS |
| `make_report reads benchmark_metrics.csv` | PASS |
| `make_report 30 engineering gates` | PASS |
| `make_report readiness table 89/100` | PASS |
| `make_report 6 limitations` | PASS |
| `make_report runtime & reproducibility line` | PASS |
| `make_report writes benchmark_report.md` | PASS |
| `make_report writes docs/BENCHMARK_README.md` | PASS |

### Pinned runtime environment

| Package | `requirements.txt` | Installed / verified | Status |
|---|---|---|---|
| `numpy` | `2.3.5` | `2.3.5` | PASS |
| `pandas` | `2.2.3` | `2.2.3` | PASS |
| `scikit-learn` | `1.6.1` | `1.6.1` | PASS |
| `qiskit` | `2.6.2` | `2.6.2` | PASS |
| `qiskit-aer` | `0.18.2` | `0.18.2` | PASS |
| `qiskit-algorithms` | `0.4.0` | `0.4.0` | PASS |
| `qiskit-machine-learning` | `0.9.1` | `0.9.1` | PASS |
| `catboost` | `1.2.10` | `1.2.10` | PASS |
| `lightgbm` | `4.7.0` | `4.7.0` | PASS |
| `xgboost` | `3.4.1` | `3.4.1` | PASS |
| `scipy` | `1.17.1` | `1.17.1` | PASS |

## 3. Continuous probability propagation & end-to-end ID traceability — 5.1–5.2

### Single probability vector across all three stages

- **Stage 1 → Stage 2:** `top10` merges `stage1[["customer_id", "predicted_probability"]]` directly onto `Stage2_Data` and computes `wᵢ = pᵢvᵢ − cᵢ` with zero rounding or recalibration (`max |Δp| = 0.0`).
- **Stage 2 → Stage 3:** `selected_order = top10.iloc[exact_combo].sort_values(["predicted_probability", "customer_id"], ascending=[False, True])` feeds the exact 6 selected probabilities into `stage3_circuit(ps)` (`max |Δp| = 0.0`).
- **Ordering convention reconciled:** Stage 2 reports the submission-facing IDs sorted ascending (`devpost_form_selected_ids = "C0059, C0170, C0256, C0327, C0372, C0374"`), while Stage 3 orders those same 6 IDs by descending Stage 1 probability (`C0170, C0256, C0327, C0374, C0059, C0372` → `q0…q5`). Set equality is exact across all CSV and JSON artifacts.

### Top-10 → Selected-6 → Stage-3 qubit traceability table

| Stage 1 rank | `customer_id` | Continuous Stage 1 `pᵢ` | Cost `cᵢ` | Value `vᵢ` | Capacity `hᵢ` | Stage 2 `wᵢ = pᵢvᵢ − cᵢ` | Selected in Stage 2? | Stage 3 qubit |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | `C0170` | `0.451587809315112` | `1` | `22` | `1` | `8.934931804932459` | Yes | `q0` |
| 2 | `C0256` | `0.434955481805204` | `1` | `22` | `4` | `8.569020599714488` | Yes | `q1` |
| 3 | `C0327` | `0.418134568251759` | `1` | `25` | `4` | `9.453364206293971` | Yes | `q2` |
| 4 | `C0338` | `0.379853593971886` | `2` | `18` | `2` | `4.837364691493956` | No | — |
| 5 | `C0188` | `0.361197859231245` | `2` | `13` | `2` | `2.695572170006188` | No | — |
| 6 | `C0079` | `0.346319801895272` | `3` | `24` | `3` | `5.311675245486528` | No | — |
| 7 | `C0081` | `0.334811376538830` | `4` | `17` | `1` | `1.691793401160119` | No | — |
| 8 | `C0374` | `0.330473588552998` | `2` | `25` | `1` | `6.261839713824944` | Yes | `q3` |
| 9 | `C0059` | `0.328801432166969` | `3` | `27` | `3` | `5.877638668508174` | Yes | `q4` |
| 10 | `C0372` | `0.323021482529514` | `3` | `30` | `3` | `6.690644475885433` | Yes | `q5` |

## 4. Cross-stage error propagation ledger — 5.3

| Stage | Uncertainty / error diagnostic | Canonical exact value | Report rounded value | Role in end-to-end trustworthiness |
|---|---|---:|---:|---|
| Stage 1 | OOF PR-AUC 95% bootstrap CI (`[low, high]`) | `[0.14725000895182838, 0.354135387006292]` | width `0.2069` | Quantifies small-sample (`35/300` positive) minority-ranking uncertainty |
| Stage 1 | PR-AUC bootstrap CI width | `0.2068853780544636` | `0.2069` | Metric #11; gate `< 0.25` PASS |
| Stage 1 | Winner 3-repeat OOF PR-AUC std | `0.0164804083231497` | `0.0165` | Metric #12; partition stability gate `< 0.02` PASS |
| Stage 1 | Winner 3-repeat OOF log-loss std | `0.0043200071234994` | — | Confirms calibration stability across CV seeds `[42, 142, 242]` |
| Stage 2 | Raw 2-layer warm-start QAOA gap | `5.047731581776915` | `5.0477` | Metric #18; disclosed raw quantum suboptimality (`40.7397 vs 45.7874`) |
| Stage 2 | Certified hybrid + brute-force gap | `0.0` | `0` | Metric #16; one-swap repair + `210/210` enumeration removes optimization error |
| Stage 3 | Aer noiseless finite-shot error (`32,768` shots) | `0.0039664962634646` | `0.0040` | Metric #23; inside 95% sampling half-width `0.005337600548893514` |
| Stage 3 | Seeded classical Monte Carlo error (`32,768` trials) | `0.0012825271740354` | `0.0013` | Metric #24; independent classical simulation check |
| Stage 3 | Synthetic noisy Aer error (`depol=0.02`, `readout=0.03`) | `0.0149223068103396` | `0.0149` | Metric #25; quantifies upward bias under gate + readout noise |
| Stage 3 | Primary marginal-inversion mitigated error | `0.0040149308597103` | `0.0040` | Metric #26; cuts noisy error by `73.0944%` |
| Stage 3 | Secondary `64×64` NNLS response-matrix error | `0.0053023269928410` | (`0.4111` prob) | Cross-checks full-distribution unfolding vs marginal inversion |
| Stage 3 | Finite-shot 95% half-width | `0.0053376005488935` | `0.0053` | Metric #27; statistical sampling bound at `32,768` shots |

## 5. Complete 30-metric benchmark & 30/30 engineering gates — 5.4

### Row-count composition reconciliation

The 30-row table in `results/benchmark_metrics.csv` comprises **14** `Stage 1 …` rows (10 core OOF/top-decile metrics + 4 supporting uncertainty/quantum-resource rows), **6** `Stage 2 …` rows (5 core feasibility/optimality/utilization metrics + the disclosed raw QAOA gap row), **8** `Stage 3 …` rows, **1** business ROI row (`Expected net value / contact cost = 4.162494497196316`), and **1** reproducibility row (`Prototype reproducibility checks passed = 100.0%`) — matching `phase_5.md`’s summary (“10 Stage 1, 5 Stage 2, 8 Stage 3, plus ROI, reproducibility, and supporting gates”) and totaling **30** exact rows.

### Canonical 30-metric table (`results/benchmark_metrics.csv`)

| # | Metric | Winning idea | Best classical (`catboost`) | Quantum-only (`quantum_kernel_svc`) | Unit | Reference / target | Why it matters |
|---:|---|---:|---:|---:|---|---|---|
| 1 | `Stage 1 ROC-AUC (OOF)` | `0.606900` | `0.6291105121293801` | `0.49919137466307273` | `score` | `higher; 0.5 = random` | Global ranking quality |
| 2 | `Stage 1 PR-AUC (OOF)` | `0.234718` | `0.22427803385763548` | `0.12264388117266026` | `score` | `higher; prevalence=0.117` | Minority-class ranking, a named judge metric |
| 3 | `Stage 1 Brier score (OOF)` | `0.103644` | `0.11635690947127046` | `0.10393886243329917` | `score` | `lower` | Probability calibration, a named judge metric |
| 4 | `Stage 1 log loss (OOF)` | `0.360930` | `0.4022557304844892` | `0.36391863520815265` | `nats` | `lower` | Penalizes overconfident probabilities |
| 5 | `Stage 1 expected calibration error` | `0.035671` | `0.08766574388820682` | `0.034161184226422205` | `score` | `lower` | Calibration reliability |
| 6 | `Stage 1 calibration slope` | `0.612382` | `0.3101817445901248` | `-0.15530313011805053` | `ratio` | `near 1` | Whether probabilities are too extreme or too flat |
| 7 | `Stage 1 Precision@10% (OOF)` | `0.300000` | `0.23333333333333334` | `0.13333333333333333` | `score` | `higher` | Proxy for hidden-test Precision@10 |
| 8 | `Stage 1 Recall@10% (OOF)` | `0.257143` | `0.2` | `0.11428571428571428` | `score` | `higher` | Proxy for hidden-test Recall@10 |
| 9 | `Stage 1 lift@10% (OOF)` | `2.571429` | `2.0` | `1.1428571428571428` | `×` | `higher; 1 = random` | Business value of the top decile |
| 10 | `Stage 1 NDCG@10% (OOF)` | `0.362780` | `0.29476975857714693` | `0.09845212737965606` | `score` | `higher` | Ranking quality with position weighting |
| 11 | `Stage 1 PR-AUC bootstrap CI width` | `0.206885` | `not scored` | `not scored` | `score` | `narrower` | Sampling stability of the minority-class metric |
| 12 | `Stage 1 CV PR-AUC std` | `0.016480` | `0.018430982797063546` | `0.009466225774401415` | `score` | `lower` | Robustness to CV partition |
| 13 | `Stage 1 quantum feature-map qubits` | `4` | `—` | `4` | `qubits` | `4-qubit ZZFeatureMap` | Real Qiskit quantum contribution |
| 14 | `Stage 1 feature-map transpiled depth` | `17` | `—` | `17` | `gates` | `u/cx basis` | Circuit-resource transparency |
| 15 | `Stage 2 exact objective` | `45.787439` | `45.78743946915947` | `45.78743946915947` | `expected net value` | `same submitted probabilities` | Classical brute-force certificate |
| 16 | `Stage 2 certified hybrid optimality gap` | `0` | `0.0` | `0.0` | `absolute` | `0 = exact optimum` | Feasibility/optimality judging credit |
| 17 | `Stage 2 QAOA feasible sample rate` | `0.681396` | `—` | `—` | `fraction` | `higher` | Quality of quantum constraint handling |
| 18 | `Stage 2 raw QAOA gap to exact` | `5.047732` | `—` | `—` | `expected net value` | `0 = QAOA sampled optimum` | Honest raw quantum gap; hybrid repair closes it |
| 19 | `Stage 2 budget utilization` | `0.440000` | `—` | `—` | `% of limit` | `≤1` | Operational constraint compliance |
| 20 | `Stage 2 capacity utilization` | `0.727273` | `—` | `—` | `% of limit` | `≤1` | Operational constraint compliance |
| 21 | `Stage 3 exact Pr(K≥3)` | `0.416413` | `—` | `—` | `probability` | `64-outcome Poisson-binomial` | Judge's exact reference |
| 22 | `Stage 3 ideal statevector Pr(K≥3)` | `0.416413` | `—` | `—` | `probability` | `exact` | Checks RY angles and Qiskit bit ordering |
| 23 | `Stage 3 noiseless finite-shot error` | `0.003966` | `—` | `—` | `absolute` | `lower` | Sampling accuracy |
| 24 | `Stage 3 Monte Carlo error` | `0.001283` | `—` | `—` | `absolute` | `lower` | Independent classical validation |
| 25 | `Stage 3 noisy error` | `0.014922` | `—` | `—` | `absolute` | `lower` | Noise/limitation analysis |
| 26 | `Stage 3 mitigated error` | `0.004015` | `—` | `—` | `absolute` | `lower than noisy error` | Unmitigated vs mitigation evidence |
| 27 | `Stage 3 finite-shot 95% half-width` | `0.005338` | `—` | `—` | `probability` | `shots=32768` | Statistical uncertainty disclosure |
| 28 | `Stage 3 two-qubit + SWAP gates` | `0` | `—` | `—` | `count` | `0 expected` | Correct independent product-state design |
| 29 | `Expected net value / contact cost` | `4.162494` | `—` | `—` | `ratio` | `higher` | Business recommendation quality |
| 30 | `Prototype reproducibility checks passed` | `100` | `—` | `—` | `%` | `100` | Seeds, versions, result files, exact references, license |

### Pre-declared engineering gates (`30 / 30 PASS` in `src/make_report.py`)

| # | Gate condition | Measured value | Threshold | Result |
|---:|---|---:|---|---|
| 1 | Stage 1 ROC-AUC > 0.60 | `0.606900269542` | `> 0.60` | PASS |
| 2 | Stage 1 PR-AUC > 2× prevalence | `0.234717570686` | `> 0.233333` | PASS |
| 3 | Stage 1 Brier < 0.11 | `0.103644171059` | `< 0.11` | PASS |
| 4 | Stage 1 log loss < 0.37 | `0.36093010631` | `< 0.37` | PASS |
| 5 | Stage 1 ECE < 0.05 | `0.0356714043455` | `< 0.05` | PASS |
| 6 | Stage 1 calibration slope in [0.5, 1.5] | `0.612382479924` | `[0.5, 1.5]` | PASS |
| 7 | Stage 1 Precision@10% >= 0.25 | `0.3` | `>= 0.25` | PASS |
| 8 | Stage 1 Recall@10% >= 0.25 | `0.257142857143` | `>= 0.25` | PASS |
| 9 | Stage 1 lift@10% >= 2.0 | `2.57142857143` | `>= 2.0` | PASS |
| 10 | Stage 1 NDCG@10% >= 0.30 | `0.362780328689` | `>= 0.30` | PASS |
| 11 | Stage 1 PR-AUC bootstrap CI width < 0.25 | `0.206885378054` | `< 0.25` | PASS |
| 12 | Stage 1 winner repeat PR-AUC std < 0.02 | `0.0164804083231` | `< 0.02` | PASS |
| 13 | Stage 1 quantum feature-map qubits == 4 | `4` | `== 4` | PASS |
| 14 | Stage 1 transpiled depth <= 20 | `17` | `<= 20` | PASS |
| 15 | Stage 2 exact objective > 0 | `45.7874394692` | `> 0` | PASS |
| 16 | Stage 2 certified hybrid gap == 0 | `0` | `< 1e-9` | PASS |
| 17 | Stage 2 QAOA feasible sample rate > 0.50 | `0.681396484375` | `> 0.50` | PASS |
| 18 | Stage 2 raw QAOA gap < 10 | `5.04773158178` | `< 10` | PASS |
| 19 | Stage 2 budget utilization <= 1 | `0.44` | `<= 1` | PASS |
| 20 | Stage 2 capacity utilization <= 1 | `0.727272727273` | `<= 1` | PASS |
| 21 | Stage 3 exact Pr(K>=3) in [0, 1] | `0.416413142408` | `[0, 1]` | PASS |
| 22 | Stage 3 |ideal - exact| < 1e-9 | `5.55111512313e-17` | `< 1e-9` | PASS |
| 23 | Stage 3 finite-shot error < 0.005 | `0.00396649626346` | `< 0.005` | PASS |
| 24 | Stage 3 Monte Carlo error < 0.005 | `0.00128252717404` | `< 0.005` | PASS |
| 25 | Stage 3 noisy error < 0.02 | `0.0149223068103` | `< 0.02` | PASS |
| 26 | Stage 3 mitigated error < noisy error | `0.00401493085971` | `< 0.014922` | PASS |
| 27 | Stage 3 finite-shot 95% half-width < 0.01 | `0.00533760054889` | `< 0.01` | PASS |
| 28 | Stage 3 two-qubit + SWAP gates == 0 | `0` | `== 0` | PASS |
| 29 | Expected net value / contact cost > 1 | `4.1624944972` | `> 1` | PASS |
| 30 | Prototype reproducibility score == 100 | `100` | `== 100` | PASS |

## 6. Reproducibility checklist, readiness estimate, and limitation register — 5.5–5.7

### 10/10 prototype reproducibility checks (`results/benchmark_summary.json["reproducibility"]`)

| Check key | Value | Status |
|---|---|---|
| `runnable_script` | `True` | PASS |
| `pinned_requirements` | `True` | PASS |
| `seed_manifest` | `True` | PASS |
| `open_source_license` | `True` | PASS |
| `stage1_root_result` | `True` | PASS |
| `stage2_root_result` | `True` | PASS |
| `stage3_root_result` | `True` | PASS |
| `exact_stage2_reference` | `True` | PASS |
| `exact_stage3_reference` | `True` | PASS |
| `full_counts_and_noise_model` | `True` | PASS |

- **Reproducibility score:** `100.0%` (`10 / 10` checks `true`).
- **Canonical benchmark runtime:** `145.9735211939999 s` (`145.9735 s` in `results/benchmark_report.md` and `docs/04_TECHNICAL_REPORT.md`, which are byte-for-byte identical at `13,072` bytes).

### Conservative rubric-aligned readiness estimate (planning figure only — 5.6)

`docs/04_TECHNICAL_REPORT.md` Section 5 explicitly states: *“This is a planning estimate, not a prediction of the judge’s score.”*

| Rubric criterion | Weight | Planning estimate | Evidence locked in repository |
|---|---:|---:|---|
| Quantum Rigor & Technical Depth | 35 | **33** | Real 4-qubit `ZZFeatureMap` kernel, 10-qubit warm-start QAOA, 6-qubit `RY` circuit, transpilation/gate/noise/mitigation reporting, raw QAOA gap disclosed |
| Result Accuracy & Integration | 30 | **26** | Continuous Stage 1→2→3 probability propagation, `0.0` certified Stage 2 gap (`210/210`), `1e-16` Stage 3 statevector agreement, low sampling/mitigated error; hidden test labels unknown |
| Code Quality & Reproducibility | 20 | **20** | `10/10` reproducibility checks (`100%`), pinned `requirements.txt`, `seeds.json`, MIT `LICENSE`, root-level `results/`, full 64-bin counts |
| Report & Communication | 15 | **10** | Technical report, data/method story, honest limitations, and external presentation handoffs maintained alongside the lean repo |
| **Total** | **100** | **89 / 100** | Conservative planning estimate before hidden-test variance |

### Six-item honest limitation register (5.7)

All six required constraints appear verbatim in Section 6 of `docs/04_TECHNICAL_REPORT.md` and `results/benchmark_report.md`:

1. **Hidden test labels unavailable** — OOF PR-AUC, Precision@10%, and Recall@10% are training-set estimates, not hidden-test scores.
2. **Wide PR-AUC bootstrap interval** — `300` training rows with `35` positives yield 95% CI `[0.147250, 0.354135]` (width `0.206885`).
3. **Quantum kernel role & claim discipline** — QSVC is a probability calibrator (ROC-AUC `0.4992`, ECE `0.0342`), not a superior standalone ranker; no unsupported quantum-advantage claim is made.
4. **Nonzero raw QAOA gap** — raw 2-layer warm-start QAOA reached `40.7397` (gap `5.0477`); zero final gap comes from explicit one-swap hybrid repair + `210/210` classical brute force.
5. **Synthetic noise model** — single-qubit depolarizing `0.02` and symmetric readout `0.03` are synthetic sensitivity channels, not live IBM hardware calibration.
6. **Lean repository boundary** — bulky PDFs, PNG/SVG media packs, and ZIP bundles live outside the lean code/data/results repo as external handoffs.

## 7. Isolated fresh-clone reproduction

The repository was copied into `/tmp/atomiq_phase5_repro/atomiq_analysis` excluding bytecode caches. `py_compile`, `python src/run_benchmark.py`, and `python src/make_report.py` were executed inside the isolated clone and compared against the untouched canonical workspace.

| Check | Result |
|---|---|
| `python -m py_compile src/run_benchmark.py src/make_report.py` | RC `0` · PASS |
| `python src/run_benchmark.py` | RC `0` · wall `149.764 s` · fresh runtime `147.021854 s` (canonical `145.973521 s`) |
| `python src/make_report.py` | RC `0` · `Wrote benchmark_report.md and docs/BENCHMARK_README.md` |
| Fresh reproducibility score | `100.0%` (`10/10` checks true) |
| Non-timing `benchmark_summary.json` comparison | Exact match (`runtime_seconds` and `model_fit_seconds_mean` normalized) |
| Normalized report comparison | `results/benchmark_report.md` and `docs/04_TECHNICAL_REPORT.md` exact after runtime-line normalization |
| Canonical root SHA-256 snapshot | Unchanged before vs after isolated reproduction (`True`) |

### Ten byte-identical result and metadata files

| File | SHA-256 prefix | Comparison vs fresh clone |
|---|---|---|
| `results/stage1_predictions.csv` | `71f3d313e35c4eaf` | Byte-identical |
| `results/stage2_selection.csv` | `2533f6e46c021f95` | Byte-identical |
| `results/stage2_selection.json` | `74e12531a9ceb77c` | Byte-identical |
| `results/stage3_simulation.csv` | `856fc26fd39409be` | Byte-identical |
| `results/stage3_simulation.json` | `c239d29e5c71f7ed` | Byte-identical |
| `results/benchmark_metrics.csv` | `3c6d0de6134ed242` | Byte-identical |
| `requirements.txt` | `52d618446b03d4d8` | Byte-identical |
| `seeds.json` | `fb33d285adef2692` | Byte-identical |
| `LICENSE` | `11767978e72b80fd` | Byte-identical |
| `docs/BENCHMARK_README.md` | `066bc9221cdef928` | Byte-identical |

## 8. Validation matrix

| Gate / check | Acceptance detail | Outcome |
|---|---|---|
| Phase 5 work package read | `docs/plan/phase_5.md` read in full before edits | PASS |
| 5.1 Continuous probability propagation | 10 Stage 2 `wᵢ` inputs and 6 Stage 3 `pᵢ` inputs equal `stage1_predictions.csv` (`max |Δ| = 0.0`) | PASS |
| 5.2 End-to-end ID traceability | Top 10 → selected 6 (`C0059, C0170, C0256, C0327, C0372, C0374`) → `q0…q5` (`C0170…C0372`) intact across CSV, JSON, report, and README | PASS |
| 5.3 Error propagation analysis | CI width `0.206885`, CV std `0.016480`, raw/certified Stage 2 gaps `5.047732 / 0.0`, Stage 3 finite-shot/MC/noisy/mitigated errors recorded | PASS |
| 5.4 30-metric benchmark & gates | `30` exact rows in `benchmark_metrics.csv`; `30/30` engineering gates passed | PASS |
| 5.5 Reproducibility checks | `10/10` checks `true`; score `100.0%`; canonical runtime `145.9735211939999 s` (`145.9735 s`) | PASS |
| 5.6 Readiness estimate | `89/100` (`33/26/20/10`) with explicit planning-estimate disclaimer | PASS |
| 5.7 Honest limitation register | All 6 constraints + no-quantum-advantage claim discipline present verbatim | PASS |
| Cross-file parity (`Definition of done`) | `benchmark_metrics.csv`, `benchmark_summary.json`, `benchmark_report.md`, `docs/04_TECHNICAL_REPORT.md`, and `README.md` agree | PASS |
| Isolated fresh-clone rerun | 10 byte-identical result/metadata files; non-timing summary exact; canonical root untouched | PASS |
| Plan-layer strict validation | 18 plan-layer files; 44 tracker rows; status, links, manifests, and completion record cross-linked; **ISSUES NONE** | PASS |

Key validation evidence was written to `/tmp/phase5_validation.json` during execution and summarized directly in this workspace report; the canonical files under `results/` remain the source of truth.

## 9. Plan and tracking updates

| Artifact | Update |
|---|---|
| [`phase_5.md`](phase_5.md) | Status → ✅ Completed; single-agent execution header; completion-report link; metric-composition & reproduction notes; Section 11 completion record |
| [`phase_5_completion.md`](phase_5_completion.md) | This end-to-end Phase 5 execution and validation record |
| [`phase_6_completion.md`](phase_6_completion.md) | Technical communication, evidence pack, and submission handoff execution record |
| [`plan.md`](plan.md) | Phase 5 status → ✅ Completed; Phase 5 subphase register → Completed; six completion-report links; Phase 5 digest and change control refreshed |
| [`README.md`](README.md) | Plan-folder index now lists Phase 0–6 completion records; 44 completed sub-phases across 18 plan-layer files |
| [`TRACKER.csv`](TRACKER.csv) | Seven `phase_5` rows → Completed / single-agent with per-subphase completion evidence |
| [`status.json`](status.json) | Top-level status → `Phases 0–6 Completed · All phases Verified`; `phase_5` and `phase_6` marked Completed; completion objects recorded |
| [`phase_0.md`](phase_0.md) … [`phase_4.md`](phase_4.md) | Master-plan contexts, Phase 0 subphase register, Phase 5 technical digest, and downstream handoffs refreshed |
| [`phase_0_completion.md`](phase_0_completion.md) … [`phase_4_completion.md`](phase_4_completion.md) | Plan-control tables, global status references, and downstream handoffs refreshed to Phases 0–6 |
| [`phase_6.md`](phase_6.md) | Master-plan context reflects Phases 0–6 as Completed |
| [`../../README.md`](../../README.md) | Repository entry point links the Phase 0–6 completion records |
| [`../../MANIFEST.md`](../../MANIFEST.md) / [`../../CLEANUP_REPORT.md`](../../CLEANUP_REPORT.md) | Self-indexed to the 41-file lean repository state with 0 hard links |

**Tracking convention:** `✅ Verified` remains the locked, evidence-backed phase gate. `✅ Completed` denotes a phase executed end to end. All seven phases (Phases 0–6) now carry both properties (44 of 44 sub-phases Completed), and all seven phase gates remain Verified.

## 10. Downstream handoff and change control

1. Phase 6 is ✅ Completed from the fully integrated, 30/30-gated, 100%-reproducible evidence base across `results/`, `docs/04_TECHNICAL_REPORT.md`, and `README.md`.
2. Any change to Stage 1 probabilities re-opens Phases 2–6 and refreshes `phase_2_completion.md` through `phase_6_completion.md`.
3. Any change to `src/make_report.py` or `results/benchmark_summary.json` requires refreshing both `results/benchmark_report.md` and `docs/04_TECHNICAL_REPORT.md` so byte-for-byte report parity is preserved.
4. The `89/100` readiness table must remain labeled as a conservative planning estimate rather than an official judge score, and all six limitations plus no-quantum-advantage claim discipline must remain explicit.
5. Bulky PDFs, PNG/SVG media assets, and ZIP bundles remain outside the lean repository; `.gitignore` keeps them from returning. No external links or placeholder team fields were introduced.

## 11. Sign-off

| Field | Value |
|---|---|
| Phase gate | **PASS · ✅ Verified** |
| Sub-phases | **7 / 7 Completed** |
| Probability continuity | **Exact (`max |Δ| = 0.0` across Stage 1 → Stage 2 → Stage 3)** |
| ID traceability | **Top 10 → `C0059, C0170, C0256, C0327, C0372, C0374` → `q0…q5` (`C0170…C0372`)** |
| Error propagation | **CI width `0.206885` · CV std `0.016480` · gaps `5.047732 → 0.0` · finite-shot error `0.003966`** |
| Benchmark & gates | **`30` metric rows · `30 / 30` engineering gates passed** |
| Reproducibility & runtime | **`10 / 10` checks (`100.0%`) · canonical runtime `145.9735211939999 s` (`145.9735 s`)** |
| Readiness estimate | **`89 / 100` (`33 / 26 / 20 / 10`) — planning figure, not official judge score** |
| Honest limitations | **`6 / 6` constraints verbatim · no unsupported quantum-advantage claim** |
| Report & README parity | **`results/benchmark_report.md` == `docs/04_TECHNICAL_REPORT.md` (`13,072` B); `README.md` aligned** |
| Fresh-clone reproduction | **PASS — 10 files byte-identical** |
| Strict final validation | **ISSUES NONE** |
| Status | **✅ Completed** |
| Execution mode | **Single-agent, end to end** |
| Timestamp | **2026-11-11 · IST** |

Back to [`phase_5.md`](phase_5.md) · [`plan.md`](plan.md) · [`TRACKER.csv`](TRACKER.csv) · [`status.json`](status.json)
