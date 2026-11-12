# Winning idea and 30-metric benchmark — The Atomiq Hackathon

**Concept name:** **CertiQ-Chirp** — *quantum-calibrated ranker fusion + certified QAOA + noise-aware six-qubit Bernoulli ledger*.

> **Honest scope:** Stage 1 numbers below are repeated out-of-fold estimates on the 300 labelled training rows. The 100 hidden test labels are unavailable, so these are not hidden-test scores. Stage 2 and Stage 3 are exact references computed from the prototype’s own final Stage 1 probabilities.

---

## 1. The best idea

The winning design is not “use a quantum model everywhere.” The benchmark showed a clearer division of labour:

- **XGBoost is the ranker:** best top-decile lift and Precision@10% among classical candidates.
- **A 4-qubit Qiskit `ZZFeatureMap` / SVC quantum kernel is the calibrator:** weak ranker (ROC-AUC ≈ 0.50) but strong probability quality (Brier ≈ 0.104, ECE ≈ 0.034).
- **A 40% XGBoost / 60% quantum-kernel fusion** preserves most ranking strength while cutting calibration error.
- **Certified QAOA:** a 10-qubit warm-start QAOA generates measured bitstrings; one-swap hybrid repair plus exact brute-force certificate closes the optimality gap.
- **Noise-aware Bernoulli ledger:** six independent `RY` qubits, ideal statevector, Aer finite-shot, noisy, and mitigated estimates, with exact 64-outcome and Monte Carlo references.

```text
300 labelled customers
  ├─ leakage-free 3x5 stratified OOF model selection
  ├─ XGBoost ranker  ───────────────┐
  └─ Qiskit quantum kernel calibrator ─┤ → calibrated p_i for 100 test customers
                                       ↓
                         deterministic top 10 by p_i, customer_id tie-break
                                       ↓
       10-qubit warm-start QAOA → measured bitstrings → hybrid repair → exact certificate
                                       ↓
       6 RY qubits → ideal / finite-shot / noisy / mitigated Pr(K≥3) → exact + Monte Carlo
```

### Why it is judge-aligned

| Rubric | Weight | How the idea attacks it |
|---|---:|---|
| Quantum Rigor & Technical Depth | 35% | Real Qiskit quantum kernel, 10-qubit QAOA, six-qubit circuit, transpilation/gate/noise reporting, classical baselines |
| Result Accuracy & Integration | 30% | Same continuous probabilities in all stages; exact Stage 2 certificate; exact Stage 3 Poisson-binomial; error propagation |
| Code Quality & Reproducibility | 20% | One runnable script, pinned versions, seed manifest, root-level result files, full measurement counts, license |
| Report & Communication | 15% | Clear quantum/classical boundary, honest raw QAOA gap, business interpretation, limitations |

### 90-second judge pitch

> “We do not claim quantum advantage. We use quantum components where they are technically defensible: a Qiskit `ZZFeatureMap` kernel acts as a calibrated probability prior, a warm-start QAOA explores the constrained selection space, and a six-qubit product circuit samples the campaign outcome. A classical XGBoost ranker supplies the top-decile ordering, while exact brute-force and Poisson-binomial references certify every result. All probabilities, IDs, seeds, circuits, counts, noise models, and errors are traceable from Stage 1 to Stage 3.”

The differentiator is **certified integration**: the same probability vector drives ranking, expected net value, selection, and the final quantum circuit—with a disclosed raw QAOA gap and a zero-gap hybrid certificate.

---

## 2. Headline evidence

| Metric | Winning fusion | Best classical | Quantum only | Interpretation |
|---|---:|---:|---:|---|
| PR-AUC (OOF) | 0.2347 | 0.2243 | 0.1226 | ~2.0× prevalence (0.1167) |
| Brier (OOF) | 0.1036 | 0.1164 | 0.1039 | Fusion is better calibrated than the classical ranker |
| Log loss (OOF) | 0.3609 | 0.4023 | 0.3639 | Reduces overconfident errors |
| ECE (OOF) | 0.0357 | 0.0877 | 0.0342 | Large calibration gain over classical ranker |
| Precision@10% (OOF) | 0.3000 | 0.2333 | 0.1333 | Proxy for hidden-test Precision@10 |
| Recall@10% (OOF) | 0.2571 | 0.2000 | 0.1143 | Proxy for hidden-test Recall@10 |
| Lift@10% | 2.5714× | 2× | 1.1429× | Top-decile business value |
| Judge-aligned composite | 0.4475 | 0.3638 | 0.3460 | Ranking + calibration + top-decile score |

**Selected winner:** `rank_calibrated_hybrid`; **best classical baseline:** `catboost`; **quantum-only baseline:** `quantum_kernel_svc`.

---

## 3. The 30-metric benchmark

Values are generated directly from `results/benchmark_metrics.csv`. “—” means the metric is not applicable to that baseline.

| # | Metric | Winning idea | Best classical | Quantum only | Unit | Reference / target | Why it matters |
|---:|---|---:|---:|---:|---|---|---|
| 1 | Stage 1 ROC-AUC (OOF) | 0.6069 | 0.6291 | 0.4992 | score | higher; 0.5 = random | Global ranking quality |
| 2 | Stage 1 PR-AUC (OOF) | 0.2347 | 0.2243 | 0.1226 | score | higher; prevalence=0.117 | Minority-class ranking, a named judge metric |
| 3 | Stage 1 Brier score (OOF) | 0.1036 | 0.1164 | 0.1039 | score | lower | Probability calibration, a named judge metric |
| 4 | Stage 1 log loss (OOF) | 0.3609 | 0.4023 | 0.3639 | nats | lower | Penalizes overconfident probabilities |
| 5 | Stage 1 expected calibration error | 0.0357 | 0.0877 | 0.0342 | score | lower | Calibration reliability |
| 6 | Stage 1 calibration slope | 0.6124 | 0.3102 | -0.1553 | ratio | near 1 | Whether probabilities are too extreme or too flat |
| 7 | Stage 1 Precision@10% (OOF) | 0.3000 | 0.2333 | 0.1333 | score | higher | Proxy for hidden-test Precision@10 |
| 8 | Stage 1 Recall@10% (OOF) | 0.2571 | 0.2000 | 0.1143 | score | higher | Proxy for hidden-test Recall@10 |
| 9 | Stage 1 lift@10% (OOF) | 2.5714 | 2 | 1.1429 | × | higher; 1 = random | Business value of the top decile |
| 10 | Stage 1 NDCG@10% (OOF) | 0.3628 | 0.2948 | 0.0985 | score | higher | Ranking quality with position weighting |
| 11 | Stage 1 PR-AUC bootstrap CI width | 0.2069 | not scored | not scored | score | narrower | Sampling stability of the minority-class metric |
| 12 | Stage 1 CV PR-AUC std | 0.0165 | 0.0184 | 0.0095 | score | lower | Robustness to CV partition |
| 13 | Stage 1 quantum feature-map qubits | 4 | — | 4 | qubits | 4-qubit ZZFeatureMap | Real Qiskit quantum contribution |
| 14 | Stage 1 feature-map transpiled depth | 17 | — | 17 | gates | u/cx basis | Circuit-resource transparency |
| 15 | Stage 2 exact objective | 45.7874 | 45.7874 | 45.7874 | expected net value | same submitted probabilities | Classical brute-force certificate |
| 16 | Stage 2 certified hybrid optimality gap | 0 | 0 | 0 | absolute | 0 = exact optimum | Feasibility/optimality judging credit |
| 17 | Stage 2 QAOA feasible sample rate | 0.6814 | — | — | fraction | higher | Quality of quantum constraint handling |
| 18 | Stage 2 raw QAOA gap to exact | 5.0477 | — | — | expected net value | 0 = QAOA sampled optimum | Honest raw quantum gap; hybrid repair closes it |
| 19 | Stage 2 budget utilization | 0.4400 | — | — | % of limit | ≤1 | Operational constraint compliance |
| 20 | Stage 2 capacity utilization | 0.7273 | — | — | % of limit | ≤1 | Operational constraint compliance |
| 21 | Stage 3 exact Pr(K≥3) | 0.4164 | — | — | probability | 64-outcome Poisson-binomial | Judge's exact reference |
| 22 | Stage 3 ideal statevector Pr(K≥3) | 0.4164 | — | — | probability | exact | Checks RY angles and Qiskit bit ordering |
| 23 | Stage 3 noiseless finite-shot error | 0.0040 | — | — | absolute | lower | Sampling accuracy |
| 24 | Stage 3 Monte Carlo error | 0.0013 | — | — | absolute | lower | Independent classical validation |
| 25 | Stage 3 noisy error | 0.0149 | — | — | absolute | lower | Noise/limitation analysis |
| 26 | Stage 3 mitigated error | 0.0040 | — | — | absolute | lower than noisy error | Unmitigated vs mitigation evidence |
| 27 | Stage 3 finite-shot 95% half-width | 0.0053 | — | — | probability | shots=32768 | Statistical uncertainty disclosure |
| 28 | Stage 3 two-qubit + SWAP gates | 0 | — | — | count | 0 expected | Correct independent product-state design |
| 29 | Expected net value / contact cost | 4.1625 | — | — | ratio | higher | Business recommendation quality |
| 30 | Prototype reproducibility checks passed | 100 | — | — | % | 100 | Seeds, versions, result files, exact references, license |

**Transparent prototype gate result: 30/30 passed.** These are pre declared engineering gates, not an official judging score. Hidden test labels remain unknown.

---

## 4. Concrete prototype answer

These are the deterministic outputs produced by the benchmark script; they are **not** a universal official answer because another team’s Stage 1 probabilities would change them.

- **Top 10:** `C0170, C0256, C0327, C0338, C0188, C0079, C0081, C0374, C0059, C0372`
- **Six selected IDs:** `C0059, C0170, C0256, C0327, C0372, C0374`
- **Expected net value:** `45.7874`
- **Budget used:** `11/25` (44%)
- **Capacity used:** `16/22` (72.7273%)
- **Feasible six-subsets checked:** `210/210` — all feasible for this candidate pool, so neither limit binds here; budget is globally redundant because six costs ≤ 24
- **Exact `Pr(K≥3)`:** `0.4164`
- **Expected conversions:** `2.2870`
- **Expected net value / contact cost:** `4.1625×`

### Stage 2 quantum result

- Algorithm: `warm-start 2-layer QAOA + one-swap hybrid repair + exact brute-force certificate`
- Logical qubits / layers / shots: `10 / 2 / 8192`
- Measured feasible-sample rate: `0.6814`
- Raw QAOA best feasible objective: `40.7397`, raw gap `5.0477`
- Certified hybrid objective: `45.7874`, **gap `0`**

The raw gap is deliberately disclosed. The final zero gap comes from a quantum-warm-started hybrid repair plus an exact classical certificate; **no quantum advantage is claimed**.

### Stage 3 quantum result

- Ideal statevector: `0.4164`
- Noiseless finite-shot: `0.4204`
- Monte Carlo: `0.4151`
- Noisy: `0.4313`
- Mitigated: `0.4124`
- 64×64 response-matrix cross-check: `0.4111`
- Error reduction from mitigation: `73.0944%`
- Shots: `32768`; finite-shot 95% half-width: `0.0053`
- Circuit: `6` qubits, logical/transpiled depth `1/1`, 1Q/2Q/SWAP `6/0/0`
- Noise model: single-qubit depolarizing `0.02`, symmetric readout `0.03`

---

## 5. Conservative readiness estimate

This is a planning estimate, not a prediction of the judge’s score.

| Criterion | Estimate | Rationale |
|---|---:|---|
| Quantum rigor 35 | 33 | Three genuine Qiskit components, exact/noisy/mitigated analysis; raw QAOA gap disclosed |
| Accuracy/integration 30 | 26 | Strong OOF calibration and top-decile lift, zero Stage 2 gap, low Stage 3 error; hidden labels unknown |
| Reproducibility 20 | 20 | 10/10 prototype checks, pinned versions, seeds, result files, full counts |
| Communication 15 | 10 | Technical report, data story, and external presentation handoffs are maintained alongside the repository |
| **Total** | **89/100** | Conservative planning estimate before hidden-test variance |

---

## 6. Limitations and risks

1. Hidden test labels are unavailable; OOF PR-AUC, Precision@10, and Recall@10 are estimates, not final scores.
2. The 300-row training set has only 35 positives, so the PR-AUC bootstrap 95% interval is wide.
3. The quantum kernel is a calibrator, not a superior ranker; unsupported quantum-advantage claims must be avoided.
4. Raw QAOA did not hit the exact optimum; the zero gap is certified by explicit hybrid repair and brute force.
5. The 0.02/0.03 noise model is synthetic, not a real IBM backend calibration. A submission must state this.
6. Presentation media and submission documents are maintained as external deliverables; the repository focuses on the runnable benchmark, pinned environment, and exact result files.

---

## 7. Files and reproduction

```text
CertiQ-Chirp repository/
  src/run_benchmark.py         # end-to-end Qiskit + sklearn benchmark
  src/make_report.py           # regenerates this report
  requirements.txt             # pinned package versions
  seeds.json                   # all random seeds
  LICENSE                      # MIT
  README.md                    # repository map and run instructions
  data/raw/                    # original participant workbook
  data/reference/              # official problem-statement PDF
  docs/                        # analysis, spec, technical report, benchmark README
  results/
    benchmark_report.md        # this file
    benchmark_metrics.csv      # 30 core metrics
    benchmark_summary.json     # all raw values and diagnostics
    stage1_predictions.csv     # 100 test probabilities/ranks/top-10 flags
    stage2_selection.json      # candidates, QAOA, exact certificate
    stage3_simulation.json     # full counts, exact/noisy/mitigated results
```

End-to-end benchmark runtime: **145.9735 s**. Reproducibility checks: **100%**.

Run:

```bash
cd /home/user/atomiq_analysis
python src/run_benchmark.py
python src/make_report.py
```
