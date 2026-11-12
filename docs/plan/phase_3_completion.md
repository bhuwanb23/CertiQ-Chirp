# Phase 3 — End-to-End Completion Report

**Project:** CertiQ-Chirp: Certified Quantum Campaign Intelligence  
**Phase:** 3 — Stage 2 — certified quantum-assisted selection  
**Status:** ✅ Completed  
**Execution:** single-agent, end to end, without splitting Phase 3 across workstreams  
**Completed:** 2026-11-11 · IST  
**Dependency:** [Phase 2 completion](phase_2_completion.md)  
**Work package:** [`phase_3.md`](phase_3.md) · **Master:** [`plan.md`](plan.md)

> **Outcome:** Phase 3 is complete. The top-10 candidate assembly, 10-qubit QUBO/Ising oracle, warm-start QAOA sampling, honest feasible decoding, one-swap repair, exact brute-force certificate, business interpretation, and Stage 3 handoff were validated. A full benchmark and report regeneration were executed in an isolated fresh clone with 10 byte-identical result/metadata files; the canonical root results were unchanged.

---

## 1. What was executed

The workspace `phase_3.md` was read in full. All six sub-phases were executed in one continuous pass from the retained source of truth: `src/run_benchmark.py`, `results/stage1_predictions.csv`, `results/stage2_selection.json`, `results/stage2_selection.csv`, `results/benchmark_summary.json`, `results/benchmark_metrics.csv`, `results/stage3_simulation.json`, `docs/04_TECHNICAL_REPORT.md`, the official workbook, `requirements.txt`, and `seeds.json`. No external submission or code links, and no placeholder team fields, were introduced.

| ID | Sub-phase | Action performed | Validation | Evidence | Result |
|---|---|---|---|---|---|
| 3.1 | Candidate input assembly | Joined the Phase 2 top-10 probabilities to `Stage2_Data` costs, deposit values, capacity units, and segments; recomputed `wᵢ = pᵢvᵢ − cᵢ` for all 10 rows. | 10/10 rows match `candidate_inputs`; order and tie rule match Phase 2. | `results/stage1_predictions.csv`, `results/stage2_selection.json` | PASS |
| 3.2 | QUBO / Ising formulation | Audited the 2¹⁰-state diagonal cost oracle with exact-six and one-sided budget/capacity penalties. | `A=B=C=500`; `D = −Σwx + 500(Σx−6)² + 500·max(0,Σc−25)² + 500·max(0,Σh−22)²`; normalized before `DiagonalGate`. | `src/run_benchmark.py` lines 337–353 | PASS |
| 3.3 | Warm-start QAOA design | Verified Hamming-weight-6 warm start, two diagonal cost layers, RX mixers, stored optimized parameters, and logical circuit resources. | 10 qubits · 2 layers · depth 5 · `rx=20 / ry=10 / diagonal=2` · 8192 shots · 4 optimized parameters. | `results/stage2_selection.json` | PASS |
| 3.4 | Sampling and feasibility decoding | Recomputed feasible rate from 8192 seeded samples and decoded the best feasible bitstring honestly. | Feasible rate `0.681396484375` (5582/8192); best feasible `1100101110`; raw objective `40.73970788738256`; raw gap `5.047731581776915`. | `results/stage2_selection.json` | PASS |
| 3.5 | Hybrid repair and exact certificate | Verified one-swap neighborhood repair, explicit inclusion of the exact classical certificate, full `C(10,6)=210` enumeration, and final six IDs. | `210/210` subsets feasible; exact certificate `1110000111`; certified gap `0.0`; `hybrid_hit_exact_optimum=true`. | `results/stage2_selection.json` | PASS |
| 3.6 | Business interpretation | Recomputed expected conversions, deposit value, cost, net value, ROI, utilizations, and Stage 3 probability/angle traceability. | Budget `11/25`; capacity `16/22`; conversions `2.286974`; deposit `56.787439`; cost `11`; net/cost `4.162494`. | `results/benchmark_summary.json`, `results/stage3_simulation.json` | PASS |

## 2. Source-level audit and environment — 3.2–3.3

**Source:** [`src/run_benchmark.py`](../../src/run_benchmark.py) · **Python compile:** PASS · **Source checks:** **27 / 27 PASS**

| Code-level check | Result |
|---|---|
| `def qaoa_stage2(top10, exact_obj, exact_ids):` | PASS |
| `A, B, C = 500.0, 500.0, 500.0` | PASS |
| `diagonal cost oracle with exact-6 and one-sided penalties` | PASS |
| `cost-oracle normalization` | PASS |
| `Hamming-weight-6 warm-start angle` | PASS |
| `warm-start RY layer` | PASS |
| `two diagonal cost layers` | PASS |
| `DiagonalGate phase application` | PASS |
| `RX mixer layer` | PASS |
| `8192 shots` | PASS |
| `seeded sampling` | PASS |
| `feasible sample rate` | PASS |
| `honest raw QAOA gap` | PASS |
| `one-swap neighborhood repair` | PASS |
| `exact certificate added to repair` | PASS |
| `hybrid gap` | PASS |
| `certified gap field` | PASS |
| `hybrid exact-hit field` | PASS |
| `exact certificate bitstring field` | PASS |
| `penalty coefficients field` | PASS |
| `logical depth/ops fields` | PASS |
| `brute-force C(10,6) enumeration` | PASS |
| `expected_net_value = p*v-c` | PASS |
| `feasible subset count` | PASS |
| `devpost form string` | PASS |
| `summary filters submission-facing stage2 field` | PASS |
| `Stage 2 raw QAOA gap metric row` | PASS |

### Key source landmarks

| Lines | Landmark |
|---:|---|
| 337–353 | `qaoa_stage2` diagonal cost oracle: `A, B, C = 500.0, 500.0, 500.0`; `D = np.zeros(2 ** n)`; exact-six and one-sided penalties; `Dn = D / scale` |
| 354–363 | Hamming-weight-6 warm start `theta0 = 2·arcsin(√0.6)`, 2 diagonal cost layers, and RX mixers |
| 379–405 | 8192 seeded shots, feasible-rate calculation, best-feasible decoding, and `qaoa_gap = exact_obj − qaoa_best_obj` |
| 415–425 | one-swap neighborhood, exact certificate insertion, hybrid objective, and `hybrid_gap` |
| 448–453 | certificate gap, exact bitstring, penalty coefficients, logical depth, and logical-operation counts |
| 654–690 | top-10 join, `w = p·v − c`, all `C(10,6)` combinations, `feasible_subset_count`, QAOA diagnostics, and `stage2_selection.json` writer |
| 708–788 | business block, reproducibility checks, filtered `stage2_summary`, and canonical summary writer |
| 825–828 | Stage 2 objective, certified gap, feasible-rate, raw-gap, and utilization metric rows |

### Pinned environment

| Package | Version | Package | Version |
|---|---:|---|---:|
| `numpy` | 2.3.5 | `pandas` | 2.2.3 |
| `scikit-learn` | 1.6.1 | `qiskit` | 2.6.2 |
| `qiskit-aer` | 0.18.2 | `qiskit-algorithms` | 0.4.0 |
| `qiskit-machine-learning` | 0.9.1 | `catboost` | 1.2.10 |
| `lightgbm` | 4.7.0 | `xgboost` | 3.4.1 |
| `scipy` | 1.17.1 |  |  |

**Canonical artifact roles.** `results/stage2_selection.json` is the live benchmark output. `results/stage2_selection.csv` is the retained one-row flattened canonical view of the same decision; both carry the same six IDs, objective, QAOA diagnostics, optimized parameters, measurement counts, and brute-force certificate. Both were byte-identical after the isolated reproduction. `benchmark_summary.json` intentionally filters only the submission-facing `devpost_form_selected_ids` field out of its `stage2` view; all other Stage 2 fields are exact.

## 3. Candidate input assembly — 3.1

**Workbook constraints:** `N=10`, `K=6`, `C=25`, `H=22`, `xᵢ∈{0,1}`, maximize `Z`.  
**Phase 2 top 10:** C0170, C0256, C0327, C0338, C0188, C0079, C0081, C0374, C0059, C0372.  
**Formula:** `wᵢ = pᵢvᵢ − cᵢ`; all values below were recomputed from `results/stage1_predictions.csv` and the workbook `Stage2_Data` sheet.

| Rank | ID | Segment | p | v | c | h | `w = p·v−c` | Certified six |
|---:|---|---|---:|---:|---:|---:|---:|:---:|
| 1 | `C0170` | C | 0.4515878093151118 | 22 | 1 | 1 | 8.934931804932459 | ✓ |
| 2 | `C0256` | A | 0.434955481805204 | 22 | 1 | 4 | 8.569020599714488 | ✓ |
| 3 | `C0327` | B | 0.4181345682517588 | 25 | 1 | 4 | 9.453364206293971 | ✓ |
| 4 | `C0338` | A | 0.37985359397188645 | 18 | 2 | 2 | 4.837364691493956 | — |
| 5 | `C0188` | B | 0.36119785923124526 | 13 | 2 | 2 | 2.695572170006188 | — |
| 6 | `C0079` | A | 0.346319801895272 | 24 | 3 | 3 | 5.311675245486528 | — |
| 7 | `C0081` | C | 0.33481137653883053 | 17 | 4 | 1 | 1.691793401160119 | — |
| 8 | `C0374` | D | 0.3304735885529978 | 25 | 2 | 1 | 6.261839713824944 | ✓ |
| 9 | `C0059` | C | 0.3288014321669694 | 27 | 3 | 3 | 5.877638668508174 | ✓ |
| 10 | `C0372` | B | 0.32302148252951446 | 30 | 3 | 3 | 6.690644475885433 | ✓ |

The selected six use budget `1+1+1+2+3+3 = 11 ≤ 25` and capacity `1+4+4+1+3+3 = 16 ≤ 22`. All 10 candidate IDs are unique and come from the locked Phase 2 top 10.

## 4. Certified cost oracle and QAOA — 3.2–3.4

| Field | Canonical value |
|---|---|
| Algorithm | `warm-start 2-layer QAOA + one-swap hybrid repair + exact brute-force certificate` |
| Penalty coefficients | `{"exact_K": 500.0, "budget": 500.0, "capacity": 500.0}` |
| Logical qubits / layers | `10 / 2` |
| Logical depth | `5` |
| Logical operations | `{"rx": 20, "ry": 10, "diagonal": 2}` |
| Shots | `8192` |
| Optimized parameters (`γ₀,β₀,γ₁,β₁`) | `[4.534176093391363, 2.917850865756762, 12.566370614359172, 3.0344960985260063]` |
| Optimizer energy, normalized | `0.007951606205251618` |
| Feasible sample rate | `0.681396484375` = `5582 / 8192` |
| Best feasible bitstring | `1100101110` |
| Best feasible IDs | `C0256`, `C0327`, `C0338`, `C0079`, `C0059`, `C0372` |
| Best feasible probability / count | `0.0032537994112026274` / `33` |
| Raw QAOA objective | `40.73970788738256` |
| Raw QAOA gap to exact | `5.047731581776915` |
| `qaoa_hit_exact_optimum` | `false` |

**Bit order.** Stage 2 bitstrings are emitted by `format(idx, "010b")`: bit 0 is the rightmost character and maps to the first top-10 candidate, `C0170`. The ID lists above were recomputed from each 10-character string and match the canonical JSON exactly. Stage 3 separately documents that Qiskit prints `c5…c0` with `q0` as the rightmost character.

### Top-20 measurement counts

| Bitstring | Count | Bitstring | Count | Bitstring | Count | Bitstring | Count |
|---|---:|---|---:|---|---:|---|---:|
| `1001100111` | 43 | `0011111100` | 42 | `1111000011` | 42 | `0011011101` | 41 |
| `0100011111` | 40 | `1111001100` | 40 | `0110110011` | 37 | `1101100011` | 37 |
| `0111110010` | 36 | `1010110110` | 36 | `1010111100` | 36 | `1000011111` | 35 |
| `1110010110` | 35 | `0111010101` | 34 | `0111110100` | 34 | `1100010111` | 34 |
| `1100011011` | 34 | `1100101011` | 34 | `1101110100` | 34 | `1111001001` | 34 |

The raw quantum run is reported honestly: its best feasible sample does **not** hit the exact optimum, and the `5.047731581776915` gap is retained as a dedicated benchmark metric and technical-report row. This is not presented as a quantum-advantage claim.

## 5. Hybrid repair and exact certificate — 3.5

| Certificate field | Value |
|---|---|
| Six-customer subsets enumerated | `210` = `C(10,6)` |
| Feasible six-customer subsets | `210 / 210` |
| Maximum six-item cost / capacity | `17.0 ≤ 25` / `19.0 ≤ 22` |
| Exact objective | `45.78743946915947` |
| Budget used / capacity used | `11.0 / 25` · `16.0 / 22` |
| Exact certificate bitstring | `1110000111` |
| Exact certificate IDs | `C0170`, `C0256`, `C0327`, `C0374`, `C0059`, `C0372` |
| Hybrid repaired bitstring | `1110000111` |
| Hybrid repaired IDs | `C0170`, `C0256`, `C0327`, `C0374`, `C0059`, `C0372` |
| Hybrid repaired objective | `45.78743946915947` |
| Absolute / relative optimality gap | `0.0` / `0.0` |
| Certified hybrid gap | `0.0` |
| `hybrid_hit_exact_optimum` | `true` |
| Final six IDs | `C0059`, `C0170`, `C0256`, `C0327`, `C0372`, `C0374` |
| Form-ready ID string | `C0059, C0170, C0256, C0327, C0372, C0374` |

The independent recomputation returned `45.787439469159466`, within `1e−12` of the canonical `45.78743946915947` (floating-point summation order). The exact brute-force certificate is explicitly added to the one-swap neighborhood, so the final certified decision has zero optimality gap while the raw QAOA gap remains disclosed.

## 6. Business interpretation and Stage 3 traceability — 3.6

| Business field | Canonical value |
|---|---:|
| `expected_net_value` | 45.78743946915947 |
| `expected_conversions` | 2.286974362621556 |
| `expected_deposit_value` | 56.78743946915947 |
| `total_contact_cost` | 11.0 |
| `expected_net_value_per_cost` | 4.162494497196316 |
| `conversion_target_probability` | 0.4164131424084104 |
| `budget_utilization` | 0.44 |
| `capacity_utilization` | 0.7272727272727273 |

| Recomputed from the six selected candidate rows | Value |
|---|---:|
| `expected_conversions` | 2.286974362621556 |
| `expected_deposit_value` | 56.787439469159466 |
| `total_contact_cost` | 11.0 |
| `expected_net_value` | 45.787439469159466 |
| `expected_net_value_per_cost` | 4.162494497196315 |

Rounded business story: expected conversions `2.286974`, deposit value `56.787439`, contact cost `11`, expected net value `45.78743946915947`, net/cost `4.162494497196316` (`4.1625×`), budget utilization `0.44` (`11/25`), and capacity utilization `0.727273` (`16/22`).

### Stage 3 handoff

| Qubit | Customer | Stage 1 probability | RY angle `2·arcsin(√p)` |
|---|---|---:|---:|
| `q0` | `C0170` | 0.4515878093151118 | 1.4738200161355677 |
| `q1` | `C0256` | 0.434955481805204 | 1.4403375481434615 |
| `q2` | `C0327` | 0.4181345682517588 | 1.4063249509489748 |
| `q3` | `C0374` | 0.3304735885529978 | 1.2248864255091458 |
| `q4` | `C0059` | 0.3288014321669694 | 1.221329260221279 |
| `q5` | `C0372` | 0.3230214825295144 | 1.2089976537211216 |

Exact `Pr(K ≥ 3)` is `0.4164131424084104`; the noiseless finite-shot estimate is `0.420379638671875`, the form value is `0.42`, and `results/stage3_simulation.json` records `Qiskit printed keys are c5...c0; q0 is the rightmost character. Hamming weight is order-invariant.` The six probabilities and RY angles are the same six selected Stage 1 probabilities, preserving the continuous probability chain.

## 7. Canonical reports, metric rows, and CSV/JSON parity

### Technical report tokens

`docs/04_TECHNICAL_REPORT.md` intentionally presents rounded, reader-facing Stage 2 values. All report tokens below are present; exact full-precision values live in the JSON/CSV result files.

| Token | Result |
|---|---|
| `45.7874` | PASS |
| `5.0477` | PASS |
| `0.6814` | PASS |
| `4.1625×` | PASS |
| `2.2870` | PASS |
| `210/210` | PASS |
| `11/25` | PASS |
| `16/22` | PASS |
| `warm-start 2-layer QAOA` | PASS |
| `no quantum advantage is claimed` | PASS |
| `C0059, C0170, C0256, C0327, C0372, C0374` | PASS |

### Phase 3 work-package reference tokens

| Token | Result |
|---|---|
| `45.78743946915947` | PASS |
| `5.047731581776915` | PASS |
| `0.681396484375` | PASS |
| `1100101110` | PASS |
| `1110000111` | PASS |
| `4.162494` | PASS |
| `2.286974` | PASS |
| `56.787439` | PASS |
| `A=B=C=500` | PASS |
| `10 qubits, 2 layers, logical depth 5, ops rx=20 / ry=10 / diagonal=2, 8192 shots` | PASS |
| `Budget 11/25, capacity 16/22` | PASS |
| `210/210 subsets checked` | PASS |

### Six Stage 2 rows inside the 30-row benchmark table

| Metric | Winning idea | Best classical | Quantum-only | Unit | Reference | Why it matters |
|---|---:|---|---|---|---|---|
| Stage 2 exact objective | 45.7874394692 | 45.78743946915947 | 45.78743946915947 | expected net value | same submitted probabilities | Classical brute-force certificate |
| Stage 2 certified hybrid optimality gap | 0.0 | 0.0 | 0.0 | absolute | 0 = exact optimum | Feasibility/optimality judging credit |
| Stage 2 QAOA feasible sample rate | 0.6813964844 | — | — | fraction | higher | Quality of quantum constraint handling |
| Stage 2 raw QAOA gap to exact | 5.0477315818 | — | — | expected net value | 0 = QAOA sampled optimum | Honest raw quantum gap; hybrid repair closes it |
| Stage 2 budget utilization | 0.44 | — | — | % of limit | ≤1 | Operational constraint compliance |
| Stage 2 capacity utilization | 0.7272727273 | — | — | % of limit | ≤1 | Operational constraint compliance |

### Stage 2 CSV ↔ JSON parity

| Field | `stage2_selection.json` | `stage2_selection.csv` | Result |
|---|---|---|---|
| Top 10 | `C0170;C0256;C0327;C0338;C0188;C0079;C0081;C0374;C0059;C0372` | `C0170;C0256;C0327;C0338;C0188;C0079;C0081;C0374;C0059;C0372` | PASS |
| Selected six | `C0059;C0170;C0256;C0327;C0372;C0374` | `C0059;C0170;C0256;C0327;C0372;C0374` | PASS |
| Objective | `45.78743946915947` | `45.78743946915947` | PASS |
| Classical optimum | `45.78743946915947` | `45.78743946915947` | PASS |
| Budget / capacity | `11.0 / 16.0` | `11.0 / 16.0` | PASS |
| Feasible subset count | `210` | `210` | PASS |
| QAOA qubits / layers / shots | `10 / 2 / 8192` | `10 / 2 / 8192` | PASS |
| Feasible rate | `0.681396484375` | `0.681396484375` | PASS |
| Best feasible bitstring | `1100101110` | `1100101110` | PASS |
| Raw QAOA objective / gap | `40.73970788738256 / 5.047731581776915` | `40.73970788738256 / 5.047731581776915` | PASS |
| Hybrid objective / certified gap | `45.78743946915947 / 0.0` | `45.78743946915947 / 0.0` | PASS |
| Exact certificate bitstring | `1110000111` | `1110000111` | PASS |
| Algorithm | `warm-start 2-layer QAOA + one-swap hybrid repair + exact brute-force certificate` | `warm-start 2-layer QAOA + one-swap hybrid repair + exact brute-force certificate` | PASS |
| Optimized parameters | `[4.534176093391363, 2.917850865756762, 12.566370614359172, 3.0344960985260063]` | `[4.534176093391363, 2.917850865756762, 12.566370614359172, 3.0344960985260063]` | PASS |

The flattened CSV also preserves `candidate_inputs_json`, `measurement_counts_top20_json`, penalty/depth metadata, and the submission-facing ID string. Its bitstring columns are stored as 10-digit numeric tokens; because both bitstrings begin with `1`, the exact 10-character values are retained. The canonical summary `stage2` view equals the JSON after filtering only `devpost_form_selected_ids`.

## 8. Fresh-clone reproduction

**Commands verified**

```bash
python -m py_compile src/run_benchmark.py src/make_report.py
python src/run_benchmark.py
python src/make_report.py
```

The full benchmark and report-generation commands were run inside `/tmp/atomiq_phase3_repro/atomiq_analysis` after installing the exact pinned stack. The workspace canonical `results/` files were left untouched; a SHA-256 snapshot before and after the isolated run was identical.

| Run | Return code | Timing | Output |
|---|---:|---:|---|
| `src/run_benchmark.py` | 0 | wall 96.264 s · runtime 92.21294843499999 s | Stage 1/2/3 results regenerated |
| `src/make_report.py` | 0 | — | `Wrote benchmark_report.md and docs/BENCHMARK_README.md` |

**Benchmark log tail**

```text
Fitting final models and generating Stage 1 test predictions...
Winner: rank_calibrated_hybrid best classical: catboost
Composite scores: {'logistic': 0.2695, 'hist_gb': 0.342, 'lightgbm': 0.337, 'catboost': 0.3638, 'xgb': 0.3573, 'quantum_kernel_svc': 0.346, 'simple_average': 0.3712, 'quantum_classical_blend': 0.4381, 'rank_calibrated_hybrid': 0.4475, 'three_way_hybrid': 0.444, 'oof_logistic_stack': 0.3849}
Top 10: ['C0170', 'C0256', 'C0327', 'C0338', 'C0188', 'C0079', 'C0081', 'C0374', 'C0059', 'C0372']
Selected 6: ['C0059', 'C0170', 'C0256', 'C0327', 'C0372', 'C0374'] objective 45.78743946915947
Exact P(K>=3): 0.4164131424084104
QAOA feasible rate: 0.681396484375 raw QAOA gap: 5.047731581776915 certified gap: 0.0
Runtime: 92.21294843499999
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
- `results/stage2_selection.csv` and `results/stage3_simulation.csv`: retained canonical flattened views, byte-identical in the isolated clone.
- Canonical runtime: `145.9735211939999` s; fresh runtime: `92.21294843499999` s.
- Fresh reproducibility score: **100.0%**.
- Reproduction summary: **10 result/metadata files byte-identical**.
- Canonical root snapshot before/after the isolated run: **unchanged**.

## 9. Validation results

| Check | Result detail | Outcome |
|---|---|---|
| Phase 3 work package | `phase_3.md` read in full; 6/6 checkboxes checked; phase gate exact. | PASS |
| Source audit | 27/27 code-level checks PASS; Python compile PASS. | PASS |
| Pinned environment | 11/11 package versions match `requirements.txt`. | PASS |
| Workbook constraints | `N=10`, `K=6`, `C=25`, `H=22`; `Stage2_Data` 400×5; `Stage2_Constraints` 6×4. | PASS |
| Candidate assembly | 10/10 candidate inputs recomputed from Stage 1 + workbook; `w=p·v−c` exact. | PASS |
| QUBO / Ising | `A=B=C=500`; exact-six, one-sided budget/capacity diagonal penalties; normalized oracle. | PASS |
| QAOA circuit | 10 qubits · 2 layers · depth 5 · `rx=20 / ry=10 / diagonal=2` · 8192 shots · parameters stored. | PASS |
| Honest decoding | feasible rate `0.681396484375`; best feasible `1100101110`; raw gap `5.047731581776915` disclosed. | PASS |
| Exact certificate | `210/210` subsets feasible; exact bitstring `1110000111`; objective `45.78743946915947`. | PASS |
| Final six | C0059, C0170, C0256, C0327, C0372, C0374; budget `11/25`; capacity `16/22`; certified gap `0.0`. | PASS |
| CSV/JSON parity | same six IDs, objective, QAOA diagnostics, parameters, measurement counts, and certificate. | PASS |
| Stage 2 metric table | 6 Stage 2 rows inside 30 total rows; rounded technical-report tokens present. | PASS |
| Business block | recomputed conversions, deposit, cost, net, ROI, and utilizations match canonical summary. | PASS |
| Stage 3 traceability | six probabilities, RY angles, qubit mapping, exact `0.4164131424084104`, and form `0.42` match. | PASS |
| Fresh-clone benchmark | RC 0 · wall 96.264 s · runtime 92.21294843499999 s. | PASS |
| Fresh-clone report generation | RC 0 · `Wrote benchmark_report.md and docs/BENCHMARK_README.md`. | PASS |
| Exact reproduction | 10 files byte-identical; summary non-timing exact; reports exact after runtime normalization. | PASS |
| Canonical root integrity | SHA-256 snapshot unchanged; no canonical result file modified. | PASS |
| Claim discipline | raw quantum gap disclosed; exact classical certificate explicit; no unsupported quantum-advantage claim. | PASS |
| Plan-layer strict validation | 18 plan-layer files; 44 tracker rows; status, links, manifests, and completion record cross-linked; **ISSUES NONE**. | PASS |

Key evidence was written to `/tmp/phase3_validation.json` during validation and copied into this workspace report. The canonical result files themselves remain the source of truth.

## 10. Plan and tracking updates

| Artifact | Update |
|---|---|
| [`phase_3.md`](phase_3.md) | Status → ✅ Completed; single-agent execution head; Section 11 completion record; completion-report link |
| [`phase_3_completion.md`](phase_3_completion.md) | This end-to-end execution and validation record |
| [`phase_4_completion.md`](phase_4_completion.md) | Stage 3 six-qubit conversion simulation execution record |
| [`phase_5_completion.md`](phase_5_completion.md) | End-to-end integration, 30-metric benchmark, and validation execution record |
| [`phase_6_completion.md`](phase_6_completion.md) | Technical communication, evidence pack, and submission handoff execution record |
| [`plan.md`](plan.md) | Phase 3 status → ✅ Completed; Phase 3 subphase register → Completed; four completion-report links; Phase 3 digest and change control refreshed |
| [`README.md`](README.md) | Plan-folder index now lists Phase 0–6 completion records; 44 completed sub-phases |
| [`TRACKER.csv`](TRACKER.csv) | Six `phase_3` rows → Completed / single-agent with per-subphase completion evidence |
| [`status.json`](status.json) | Top-level status → Phases 0–6 Completed · All phases Verified; Phase 3–6 completion objects recorded |
| [`phase_0.md`](phase_0.md) / [`phase_1.md`](phase_1.md) / [`phase_2.md`](phase_2.md) | Master-plan contexts and downstream handoffs refreshed |
| [`phase_0_completion.md`](phase_0_completion.md) / [`phase_1_completion.md`](phase_1_completion.md) / [`phase_2_completion.md`](phase_2_completion.md) | Context, artifact tables, and downstream status refreshed |
| [`phase_4.md`](phase_4.md) … [`phase_6.md`](phase_6.md) | Master-plan context reflects Phases 0–6 as Completed |
| [`../../README.md`](../../README.md) | Repository entry point links the Phase 0–6 completion records |
| [`../../MANIFEST.md`](../../MANIFEST.md) / [`../../CLEANUP_REPORT.md`](../../CLEANUP_REPORT.md) | Re-indexed to the final lean repo, including the new completion report |

**Tracking convention:** `✅ Verified` remains the locked, evidence-backed phase gate. `✅ Completed` denotes a phase executed end to end. All seven phases (Phases 0–6) now carry both properties. All seven phase gates remain Verified. The plan layer contains 18 files and the tracker retains 44 rows.

## 11. Downstream handoff and change control

1. All Phases 4–6 are ✅ Completed from the six selected IDs and their continuous Stage 1 probabilities.
2. A change to Stage 1 probabilities re-opens Phases 2–6 and refreshes `phase_2_completion.md` through `phase_6_completion.md`.
3. A change to Stage 2 inputs, QAOA parameters, or the certificate re-opens Phase 3 and refreshes `results/stage2_selection.json`, `results/stage2_selection.csv`, `results/benchmark_summary.json`, the six Stage 2 metric rows, and the report tokens.
4. Both the JSON and the retained flattened CSV view must continue to carry the same six IDs, objective, QAOA diagnostics, optimized parameters, measurement counts, and brute-force certificate.
5. The raw QAOA gap must remain disclosed separately from the certified hybrid gap; no unsupported quantum-advantage claim is added.
6. Bulky presentation, PDF, media, and archive handoffs remain outside the lean repository; `.gitignore` keeps them from returning. No external links or placeholder team fields were introduced.

## 12. Sign-off

| Field | Value |
|---|---|
| Phase gate | **PASS · ✅ Verified** |
| Sub-phases | **6 / 6 Completed** |
| Candidate table | **10 / 10 exact · `w=p·v−c`** |
| Cost oracle | **A=B=C=500 · 2¹⁰ diagonal states · normalized** |
| QAOA | **10 qubits · 2 layers · depth 5 · 8192 shots** |
| Raw quantum result | **`1100101110` · objective `40.73970788738256` · gap `5.047731581776915` disclosed** |
| Exact certificate | **`1110000111` · `210/210` subsets · objective `45.78743946915947`** |
| Certified six | **C0059, C0170, C0256, C0327, C0372, C0374** |
| Constraints | **budget `11/25` · capacity `16/22` · certified gap `0.0`** |
| Business | **conversions `2.286974` · deposit `56.787439` · cost `11` · net/cost `4.162494`** |
| CSV/JSON parity | **PASS — same IDs, objective, diagnostics, and certificate** |
| Fresh-clone reproduction | **PASS — 10 files byte-identical** |
| Reproducibility score | **100%** |
| Strict final validation | **ISSUES NONE** |
| Status | **✅ Completed** |
| Execution mode | **Single-agent, end to end** |
| Timestamp | **2026-11-11 · IST** |

Back to [`phase_3.md`](phase_3.md) · [`plan.md`](plan.md) · [`TRACKER.csv`](TRACKER.csv) · [`status.json`](status.json)

