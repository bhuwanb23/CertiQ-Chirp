# Phase 4 — End-to-End Completion Report

**Project:** CertiQ-Chirp: Certified Quantum Campaign Intelligence  
**Phase:** 4 — Stage 3 — six-qubit conversion simulation  
**Status:** ✅ Completed  
**Execution:** single-agent, end to end, without splitting Phase 4 across workstreams  
**Completed:** 2026-11-11 · IST  
**Dependency:** [Phase 3 completion](phase_3_completion.md) · [Phase 2 completion](phase_2_completion.md)  
**Work package:** [`phase_4.md`](phase_4.md) · **Master:** [`plan.md`](plan.md)

> **Outcome:** Phase 4 is complete. The six-customer qubit mapping, `RY` product-state preparation, 64-outcome exact Poisson-binomial reference, ideal statevector reference, 32,768-shot Qiskit Aer noiseless simulation, seeded Monte Carlo cross-check, synthetic depolarizing/readout noise simulation, noise-model-aware marginal inversion with 64×64 NNLS cross-check, circuit resource ledger, and CSV/JSON parity were validated. A full benchmark and report regeneration were executed in an isolated fresh clone with 10 byte-identical result/metadata files; the canonical root results were unchanged.

---

## 1. What was executed

The workspace `phase_4.md` was read in full. All eight sub-phases were executed in one continuous single-agent pass from the retained source of truth: `src/run_benchmark.py`, `results/stage1_predictions.csv`, `results/stage2_selection.json`, `results/stage3_simulation.json`, `results/stage3_simulation.csv`, `results/benchmark_summary.json`, `results/benchmark_metrics.csv`, `docs/04_TECHNICAL_REPORT.md`, `requirements.txt`, and `seeds.json`. No external submission or code links, and no placeholder team fields, were introduced.

| ID | Sub-phase | Action performed | Validation | Evidence | Result |
|---|---|---|---|---|---|
| 4.1 | Customer-to-qubit mapping | Verified circuit-order customer IDs `C0170, C0256, C0327, C0374, C0059, C0372` mapped to `q0…q5`, Qiskit `c5…c0` printing convention, `q0` rightmost character, and Stage 2 six-ID set equality. | `q0` is rightmost character; `customer_to_qubit_mapping` and `qubit_order` exact. | `results/stage3_simulation.json`, `results/stage3_simulation.csv` | PASS |
| 4.2 | `RY` state preparation | Recomputed `θᵢ = 2 arcsin √pᵢ` and `sin²(θᵢ/2)` from the six continuous Stage 1 probabilities. | Six `ry_angles` match `2 arcsin √pᵢ` to machine precision (`≤ 1e-12`). | `results/stage1_predictions.csv`, `results/stage3_simulation.json` | PASS |
| 4.3 | Exact Poisson-binomial reference | Enumerated all `2⁶ = 64` outcomes and dynamic-programming `Pr(K ≥ 3)` alongside the ideal 6-qubit `Statevector`. | Exact `0.4164131424084104`; ideal statevector `0.4164131424084103`; absolute difference `1e-16`. | `results/stage3_simulation.json` | PASS |
| 4.4 | Aer noiseless finite-shot | Verified seeded `AerSimulator` (`seed_simulator = 31415`) at `32768` shots and all 64 measurement bins. | Aer `0.420379638671875`; error `0.003966496263464625` ≤ 95% half-width `0.005337600548893514`; 64 bins sum to `32768`. | `results/stage3_simulation.json` | PASS |
| 4.5 | Monte Carlo cross-check | Re-ran classical Bernoulli Monte Carlo with `np.random.default_rng(27182)` at `32768 × 6` draws. | Monte Carlo `0.415130615234375`; error `0.001282527174035375`. | `results/stage3_simulation.json` | PASS |
| 4.6 | Synthetic noise model | Verified synthetic single-qubit depolarizing `0.02` on `ry`, symmetric readout `0.03`, `seed_simulator = 31416`, and all 64 noisy bins. | Noisy `0.43133544921875`; noisy error `0.014922306810339625`; 64 bins sum to `32768`. | `results/stage3_simulation.json` | PASS |
| 4.7 | Mitigation and cross-check | Recomputed six-qubit marginal channel inversion plus full `64×64` NNLS response-matrix unfolding. | Mitigated `0.41239821154870004` (error `0.004014930859710331` < noisy error `0.014922306810339625`, `73.0944%` reduction); NNLS `0.4111108154155694` (error `0.005302326992841`). | `results/stage3_simulation.json` | PASS |
| 4.8 | Circuit and shot ledger | Checked logical/transpiled circuit depth, gate counts, shot counts, standard error, 95% half-width, report tokens, and flattened CSV parity. | `6` qubits, logical/transpiled depth `1/1`, `6` one-qubit gates (`u: 6`), `0` two-qubit/SWAP gates, `32768` shots, CI half-width `0.005337600548893514`. | `results/stage3_simulation.json`, `docs/04_TECHNICAL_REPORT.md` | PASS |

## 2. Source-level audit and pinned environment — 4.1–4.8

**Source:** [`src/run_benchmark.py`](../../src/run_benchmark.py) (`poisson_binomial_at_least`, `bit_success`, `qiskit_counts_index`, `noise_response_matrix`, `stage3_circuit`, lines 293–545 and 699–838) · **Python compile:** PASS · **Source checks:** **32 / 32 PASS**

| Code-level check | Result |
|---|---|
| `SHOTS = 32768` | PASS |
| `simulator and Monte Carlo seeds` | PASS |
| `def stage3_circuit(ps, shots=SHOTS)` | PASS |
| `RY angles = 2 arcsin sqrt(p)` | PASS |
| `six RY gates on q0..q5` | PASS |
| `measure_all copy` | PASS |
| `ideal Statevector reference` | PASS |
| `Poisson-binomial exact reference` | PASS |
| `AerSimulator seeded noiseless` | PASS |
| `noiseless finite-shot seed` | PASS |
| `depolarizing 0.02` | PASS |
| `symmetric readout 0.03` | PASS |
| `noisy simulator seed` | PASS |
| `64x64 response matrix` | PASS |
| `NNLS unfolding` | PASS |
| `observed marginal extraction` | PASS |
| `primary marginal inversion` | PASS |
| `mitigated Poisson-binomial` | PASS |
| `seeded Monte Carlo RNG` | PASS |
| `Monte Carlo tail mean` | PASS |
| `q0 rightmost bit-order note` | PASS |
| `qubit_order field` | PASS |
| `finite-shot 95% half-width` | PASS |
| `noise model field` | PASS |
| `full noiseless counts field` | PASS |
| `full noisy counts field` | PASS |
| `Stage 3 Monte Carlo metric row` | PASS |
| `Stage 3 mitigated error metric row` | PASS |
| `summary filters Stage 3 submission-facing fields` | PASS |
| `quantum estimated probability field` | PASS |
| `devpost form value field` | PASS |
| `form probability basis field` | PASS |

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

## 3. Customer-to-qubit mapping and `RY` state preparation — 4.1–4.2

Stage 2’s submission-facing six-ID list is sorted ascending (`C0059, C0170, C0256, C0327, C0372, C0374`), whereas Stage 3 prepares qubits in the Stage 1 top-10 probability order of those same six customers (`C0170, C0256, C0327, C0374, C0059, C0372`). The two sets are identical, and Qiskit bitstrings are explicitly documented as `c5...c0` with `q0` as the rightmost character (`bit_order_note`: `"Qiskit printed keys are c5...c0; q0 is the rightmost character. Hamming weight is order-invariant."`).

Each independent customer conversion probability `pᵢ` is encoded on one qubit by `RY(θᵢ)|0⟩ = cos(θᵢ/2)|0⟩ + sin(θᵢ/2)|1⟩` with `θᵢ = 2 arcsin(√pᵢ)`, so `Pr(qᵢ = 1) = sin²(θᵢ/2) = pᵢ` without entangling gates.

| Qubit | Customer ID | Stage 1 rank | Stage 1 `pᵢ` | `θᵢ = 2 arcsin √pᵢ` (rad) | `sin²(θᵢ/2)` | Aer noiseless marginal | Noisy marginal | Mitigated marginal | Qiskit key position (`c5…c0`) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `q0` | `C0170` | 1 | `0.451587809315112` | `1.473820016135568` | `0.451587809315112` | `0.448760986328` | `0.453521728516` | `0.449545949322` | rightmost character 6 (`c0`, LSB) |
| `q1` | `C0256` | 2 | `0.434955481805204` | `1.440337548143461` | `0.434955481805204` | `0.433135986328` | `0.437652587891` | `0.432319352899` | character 5 (`c1`) |
| `q2` | `C0327` | 3 | `0.418134568251759` | `1.406324950948975` | `0.418134568251759` | `0.422210693359` | `0.424957275391` | `0.418538075761` | character 4 (`c2`) |
| `q3` | `C0374` | 8 | `0.330473588552998` | `1.224886425509146` | `0.330473588552998` | `0.331939697266` | `0.342254638672` | `0.328761005940` | character 3 (`c3`) |
| `q4` | `C0059` | 9 | `0.328801432166969` | `1.221329260221279` | `0.328801432166969` | `0.330200195312` | `0.342193603516` | `0.328694749800` | character 2 (`c4`) |
| `q5` | `C0372` | 10 | `0.323021482529514` | `1.208997653721122` | `0.323021482529515` | `0.321594238281` | `0.331909179688` | `0.317530590195` | character 1 (`c5`) |

## 4. Probability reference hierarchy and K-distribution — 4.3–4.7

### Canonical probability and error ledger

| Quantity | Canonical value | Absolute error vs exact | Verification note |
|---|---:|---:|---|
| Exact analytical `Pr(K ≥ 3)` | `0.4164131424084104` | `0.0000000000000000` | 64-outcome Poisson-binomial ground truth (`Σ_{k=3}^6 Pr(K = k)`) |
| Ideal statevector `Pr(K ≥ 3)` | `0.4164131424084103` | `0.0000000000000001` | Qiskit `Statevector.from_instruction(qc)`; agrees with exact to `1e-16` |
| Aer noiseless finite-shot (`32768` shots) | `0.4203796386718750` | `0.0039664962634646` | `seed_simulator = 31415`; inside 95% half-width `0.0053376005488935` |
| Submission-facing `quantum_estimated_probability` | `0.4203796386718750` | `0.0039664962634646` | Equal to Aer noiseless finite-shot; `devpost_form_value = 0.42` (`0.420` in prose) |
| Seeded classical Monte Carlo (`32768` trials) | `0.4151306152343750` | `0.0012825271740354` | `np.random.default_rng(27182)` independent Bernoulli check |
| Synthetic noisy Aer (`depol=0.02`, `readout=0.03`) | `0.4313354492187500` | `0.0149223068103396` | `seed_simulator = 31416`; upward bias toward `0.5` per-qubit marginals |
| Primary mitigated (marginal channel inversion) | `0.4123982115487000` | `0.0040149308597103` | Reduces noisy error by `73.0944%` (`0.014922307 → 0.004014931`) |
| Secondary cross-check (`64×64` NNLS unfolding) | `0.4111108154155694` | `0.0053023269928410` | Full 64-state response matrix `R` with simplex weight `10.0`; retained as cross-check |

### Exact vs sampled Hamming-weight distribution (`K = 0…6`)

| Conversions `K` | Success event? | Exact Poisson-binomial `Pr(K)` | Noiseless Aer shots | Noiseless empirical | Noisy Aer shots | Noisy empirical |
|---|---|---|---|---:|---:|---:|
| `K = 0` | No | `0.0548537023062153` | 1831 | `0.055877685546875` | 1668 | `0.050903320312500` |
| `K = 1` | No | `0.2069325934180315` | 6737 | `0.205596923828125` | 6520 | `0.198974609375000` |
| `K = 2` | No | `0.3218005618673428` | 10425 | `0.318145751953125` | 10446 | `0.318786621093750` |
| `K = 3` | Yes (`K ≥ 3`) | `0.2640012161642373` | 8821 | `0.269195556640625` | 8776 | `0.267822265625000` |
| `K = 4` | Yes (`K ≥ 3`) | `0.1205053707944349` | 3948 | `0.120483398437500` | 4198 | `0.128112792968750` |
| `K = 5` | Yes (`K ≥ 3`) | `0.0290238189000416` | 910 | `0.027770996093750` | 1061 | `0.032379150390625` |
| `K = 6` | Yes (`K ≥ 3`) | `0.0028827365496966` | 96 | `0.002929687500000` | 99 | `0.003021240234375` |

Summing `K ∈ {3, 4, 5, 6}` gives `13,775 / 32,768 = 0.420379638671875` for noiseless Aer and `14,134 / 32,768 = 0.43133544921875` for synthetic noisy Aer, matching `results/stage3_simulation.json` exactly.

## 5. Noise model, mitigation design, and 64-bin count ledger — 4.6–4.8

### Noise and mitigation specification

- **Synthetic noise disclosure:** single-qubit depolarizing error `0.02` attached to every `ry` gate plus symmetric all-qubit readout error `0.03` (`[[0.97, 0.03], [0.03, 0.97]]`), explicitly documented as a synthetic sensitivity model rather than live IBM hardware calibration.
- **Primary mitigation (`mitigated_probability = 0.41239821154870004`):** extracts the six observed marginal excitation rates from the 64 noisy counts using `qiskit_counts_index` (`q0` as LSB), inverts symmetric readout via `(m − r) / (1 − 2r)` and single-qubit depolarizing via `(p_pre − d/2) / (1 − d)` clipped to `[0, 1]`, then evaluates the exact 6-variable Poisson-binomial tail. Because six marginals are estimated with `32,768` shots each rather than unfolding 64 bins simultaneously, its error (`0.004014930859710331`) beats full `64×64` NNLS unfolding (`0.005302326992841`) while cutting unmitigated noisy error (`0.014922306810339625`) by `73.0944%`.
- **Secondary cross-check (`response_matrix_mitigated_probability = 0.4111108154155694`):** builds the exact `64×64` channel matrix `M[m, z] = P(measured m | ideal z)` and solves constrained non-negative least squares (`nnls`) before summing weight-`≥3` probabilities. No unsupported quantum-advantage or hardware-calibration claim is made.

### Circuit and shot ledger

| Field | Canonical value | Check |
|---|---|---|
| `logical_qubits` | `6` | One qubit per selected customer |
| `logical_depth` / `transpiled_depth` | `1` / `1` | Product state; depth 1 before and after transpilation |
| `one_qubit_gates` / `transpiled_ops` | `6` / `{"u": 6}` | Six independent single-qubit rotations |
| `two_qubit_gates` / `swap_gates` | `0` / `0` | Zero entangling and zero SWAP gates |
| `shots` | `32768` noiseless + `32768` noisy | Full 64-bin histograms preserved for both runs |
| `finite_shot_standard_error` | `0.0027232655861702` | `√(p(1−p)/32768)` at exact `p = 0.4164131424084104` |
| `finite_shot_ci95_half_width` | `0.0053376005488935` | `1.96 × SE`; finite-shot error `0.003966496` lies well inside |
| `noiseless_counts` integrity | `64` bins · `32768` shots · SHA-256 prefix `c4a569eb97e63321` | Complete 64-key dictionary |
| `noisy_counts` integrity | `64` bins · `32768` shots · SHA-256 prefix `0a562ef42f157ba5` | Complete 64-key dictionary |

### Top 10 noiseless Aer bitstrings (`c5…c0`, `32,768` shots)

| Bitstring | Hamming weight | Counts toward `K ≥ 3`? | Count | Empirical frequency |
|---|---:|---|---:|---:|
| `000000` | 0 | No | 1831 | `0.055877685547` |
| `000001` | 1 | No | 1463 | `0.044647216797` |
| `000010` | 1 | No | 1394 | `0.042541503906` |
| `000100` | 1 | No | 1268 | `0.038696289062` |
| `000011` | 2 | No | 1106 | `0.033752441406` |
| `000101` | 2 | No | 1040 | `0.031738281250` |
| `000110` | 2 | No | 1024 | `0.031250000000` |
| `010000` | 1 | No | 884 | `0.026977539062` |
| `001000` | 1 | No | 873 | `0.026641845703` |
| `100000` | 1 | No | 855 | `0.026092529297` |

### Top 10 synthetic noisy Aer bitstrings (`c5…c0`, `32,768` shots)

| Bitstring | Hamming weight | Counts toward `K ≥ 3`? | Count | Empirical frequency |
|---|---:|---|---:|---:|
| `000000` | 0 | No | 1668 | `0.050903320312` |
| `000001` | 1 | No | 1393 | `0.042510986328` |
| `000010` | 1 | No | 1297 | `0.039581298828` |
| `000100` | 1 | No | 1269 | `0.038726806641` |
| `000011` | 2 | No | 1085 | `0.033111572266` |
| `000101` | 2 | No | 1037 | `0.031646728516` |
| `000110` | 2 | No | 941 | `0.028717041016` |
| `001000` | 1 | No | 896 | `0.027343750000` |
| `010000` | 1 | No | 857 | `0.026153564453` |
| `100000` | 1 | No | 808 | `0.024658203125` |

## 6. Benchmark metric lock and CSV/JSON parity — 4.8 & Definition of Done

### Eight Stage 3 rows in `results/benchmark_metrics.csv` (rows 21–28 of 30)

| Metric | `winning_idea` | Unit | Reference / target | Role |
|---|---:|---|---|---|
| `Stage 3 exact Pr(K≥3)` | `0.416413142400` | `probability` | `64-outcome Poisson-binomial` | Judge's exact reference |
| `Stage 3 ideal statevector Pr(K≥3)` | `0.416413142400` | `probability` | `exact` | Checks RY angles and Qiskit bit ordering |
| `Stage 3 noiseless finite-shot error` | `0.003966496300` | `absolute` | `lower` | Sampling accuracy |
| `Stage 3 Monte Carlo error` | `0.001282527200` | `absolute` | `lower` | Independent classical validation |
| `Stage 3 noisy error` | `0.014922306800` | `absolute` | `lower` | Noise/limitation analysis |
| `Stage 3 mitigated error` | `0.004014930900` | `absolute` | `lower than noisy error` | Unmitigated vs mitigation evidence |
| `Stage 3 finite-shot 95% half-width` | `0.005337600500` | `probability` | `shots=32768` | Statistical uncertainty disclosure |
| `Stage 3 two-qubit + SWAP gates` | `0.000000000000` | `count` | `0 expected` | Correct independent product-state design |

### Canonical `stage3_simulation.json` vs `stage3_simulation.csv` parity

- `results/stage3_simulation.json` contains **31** keys: the 28 core `stage3_circuit` / mapping fields mirrored into `results/benchmark_summary.json["stage3"]` plus the 3 submission-facing fields (`quantum_estimated_probability = 0.420379638671875`, `devpost_form_value = 0.42`, `form_probability_basis`).
- `results/stage3_simulation.csv` is the retained 1-row × **27**-column flattened companion view: semicolon-joined `selected_customer_ids`, `input_probabilities` (12-decimal formatting, matching JSON within `≤ 5e-13`), and `ry_angles` (12-decimal formatting, matching JSON within `≤ 5e-13`), exact scalar probabilities/errors/circuit counts, `bit_order_note`, `noise_model_json`, and full 64-bin `noiseless_counts_json` and `noisy_counts_json` dictionaries that parse to the exact JSON dictionaries.
- As documented in Phases 1–3, `src/run_benchmark.py` writes `results/stage3_simulation.json` directly while `results/stage3_simulation.csv` is retained as a canonical flattened companion artifact; `response_matrix_mitigated_probability` (`0.4111108154155694`) and `response_matrix_mitigated_vs_exact` (`0.005302326992841`) live in `stage3_simulation.json`, `benchmark_summary.json`, and `docs/04_TECHNICAL_REPORT.md` (`0.4111`).

## 7. Isolated fresh-clone reproduction

The repository was copied into `/tmp/atomiq_phase4_repro/atomiq_analysis` excluding bytecode caches. `py_compile`, `python src/run_benchmark.py`, and `python src/make_report.py` were executed inside the isolated clone, then compared byte-for-byte against the untouched canonical root.

| Check | Result |
|---|---|
| `python -m py_compile src/run_benchmark.py src/make_report.py` | RC `0` · PASS |
| `python src/run_benchmark.py` | RC `0` · wall `150.166 s` · fresh runtime `147.671025 s` (canonical `145.973521 s`) |
| `python src/make_report.py` | RC `0` · `Wrote benchmark_report.md and docs/BENCHMARK_README.md` |
| Fresh reproducibility score | `100.0%` (`10/10` reproducibility checks true) |
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
| Phase 4 work package read | `docs/plan/phase_4.md` read in full before edits | PASS |
| 4.1 Customer-to-qubit mapping | `q0…q5` ↔ `C0170, C0256, C0327, C0374, C0059, C0372`; `c5…c0` with `q0` rightmost | PASS |
| 4.2 `RY` state preparation | Six `ry_angles` equal `2 arcsin √pᵢ` from `stage1_predictions.csv` | PASS |
| 4.3 Exact & statevector references | Exact `0.4164131424084104`; ideal `0.4164131424084103`; difference `1e-16` | PASS |
| 4.4 Aer noiseless finite-shot | `0.420379638671875` at `32768` shots; error `0.003966496` ≤ CI half-width `0.005337601` | PASS |
| 4.5 Monte Carlo cross-check | `0.415130615234375` at seed `27182`; error `0.001282527` | PASS |
| 4.6 Synthetic noise model | Depolarizing `0.02`, symmetric readout `0.03`; noisy `0.43133544921875`; error `0.014922307` | PASS |
| 4.7 Mitigation & NNLS cross-check | Marginal inversion `0.41239821154870004` (error `0.004014931` < noisy error, `73.0944%` reduction); NNLS `0.4111108154155694` | PASS |
| 4.8 Circuit & shot ledger | `6` qubits, depth `1/1`, `6` 1Q gates, `0` 2Q/SWAP, `32768` noiseless + `32768` noisy shots, 64+64 counts | PASS |
| Technical report consistency | All Stage 3 rounded values, circuit resources, shots, CI half-width, noise parameters, and claim discipline present | PASS |
| CSV/JSON parity | `stage3_simulation.csv` and `stage3_simulation.json` agree across mapping, angles, probabilities, errors, noise model, and 64-bin counts | PASS |
| Isolated fresh-clone rerun | 10 byte-identical result/metadata files; non-timing summary exact; canonical root untouched | PASS |
| Plan-layer strict validation | 18 plan-layer files; 44 tracker rows; status, links, manifests, and completion record cross-linked; **ISSUES NONE** | PASS |

Key validation evidence was written to `/tmp/phase4_validation.json` during execution and summarized directly in this workspace report; the canonical files under `results/` remain the source of truth.

## 9. Plan and tracking updates

| Artifact | Update |
|---|---|
| [`phase_4.md`](phase_4.md) | Status → ✅ Completed; single-agent execution header; completion-report link; Definition of Done reproduction note; Section 11 completion record |
| [`phase_4_completion.md`](phase_4_completion.md) | This end-to-end Phase 4 execution and validation record |
| [`phase_5_completion.md`](phase_5_completion.md) | End-to-end integration, 30-metric benchmark, and validation execution record |
| [`phase_6_completion.md`](phase_6_completion.md) | Technical communication, evidence pack, and submission handoff execution record |
| [`plan.md`](plan.md) | Phase 4 status → ✅ Completed; Phase 4 subphase register → Completed; five completion-report links; Phase 4 digest and change control refreshed |
| [`README.md`](README.md) | Plan-folder index now lists Phase 0–6 completion records; 44 completed sub-phases across 18 plan-layer files |
| [`TRACKER.csv`](TRACKER.csv) | Eight `phase_4` rows → Completed / single-agent with per-subphase completion evidence |
| [`status.json`](status.json) | Top-level status → `Phases 0–6 Completed · All phases Verified`; `phase_4` through `phase_6` marked Completed; completion objects recorded |
| [`phase_0.md`](phase_0.md) … [`phase_3.md`](phase_3.md) | Master-plan contexts, Phase 0 subphase register, Phase 4 technical digest, and downstream handoffs refreshed |
| [`phase_0_completion.md`](phase_0_completion.md) … [`phase_3_completion.md`](phase_3_completion.md) | Plan-control tables, global status references, and downstream handoffs refreshed to Phases 0–6 |
| [`phase_5.md`](phase_5.md), [`phase_6.md`](phase_6.md) | Master-plan context reflects Phases 0–6 as Completed |
| [`../../README.md`](../../README.md) | Repository entry point links the Phase 0–6 completion records |
| [`../../MANIFEST.md`](../../MANIFEST.md) / [`../../CLEANUP_REPORT.md`](../../CLEANUP_REPORT.md) | Self-indexed to the 41-file lean repository state with 0 hard links |

**Tracking convention:** `✅ Verified` remains the locked, evidence-backed phase gate. `✅ Completed` denotes a phase executed end to end. All seven phases (Phases 0–6) now carry both properties (44 of 44 sub-phases Completed), and all seven phase gates remain Verified.

## 10. Downstream handoff and change control

1. Phases 5–6 are ✅ Completed across Stage 1–3 integration, the 30-metric benchmark table (`30/30` gates), `10/10` reproducibility (`100%`), `22/22` narrative consistency checks, and external handoff governance.
2. A change to Stage 1 probabilities re-opens Phases 2–6 and refreshes `phase_2_completion.md` through `phase_6_completion.md`.
3. A change to Stage 2’s selected six customers re-opens Phases 3–6 and refreshes `results/stage2_selection.*`, `results/stage3_simulation.*`, `results/benchmark_summary.json`, `results/benchmark_metrics.csv`, and both technical reports.
4. A change to Stage 3 shots, seeds, noise parameters, or mitigation equations re-opens Phase 4 and requires checking both `results/stage3_simulation.json` and the retained flattened companion `results/stage3_simulation.csv`.
5. The synthetic `0.02 / 0.03` noise disclosure, explicit `q0` rightmost bit-order note, and claim discipline (no unsupported quantum-advantage claim) remain mandatory.
6. Bulky PDFs, PNG/SVG media packs, and ZIP bundles remain outside the lean repository; `.gitignore` keeps them from returning. No external links or placeholder team fields were introduced.

## 11. Sign-off

| Field | Value |
|---|---|
| Phase gate | **PASS · ✅ Verified** |
| Sub-phases | **8 / 8 Completed** |
| Qubit mapping | **`q0 C0170, q1 C0256, q2 C0327, q3 C0374, q4 C0059, q5 C0372` (`c5…c0`, `q0` rightmost)** |
| `RY` angles | **`1.473820, 1.440338, 1.406325, 1.224886, 1.221330, 1.208998` rad** |
| Exact / ideal `Pr(K ≥ 3)` | **`0.4164131424084104` / `0.4164131424084103` (`|Δ| = 1e-16`)** |
| Aer noiseless (`32768` shots) | **`0.420379638671875` · error `0.003966496` ≤ 95% half-width `0.005337601` · form `0.420`** |
| Monte Carlo (`32768` trials) | **`0.415130615234375` · error `0.001282527`** |
| Synthetic noisy (`0.02 / 0.03`) | **`0.43133544921875` · error `0.014922307`** |
| Mitigated / NNLS cross-check | **`0.41239821154870004` (error `0.004014931`, `-73.0944%`) / `0.4111108154155694` (error `0.005302327`)** |
| Circuit & histograms | **`6` qubits · depth `1/1` · `6/0/0` gates · `64 + 64` count bins (`32768` shots each)** |
| CSV/JSON parity | **PASS — mapping, angles, probabilities, errors, noise model, and 64-bin counts aligned** |
| Fresh-clone reproduction | **PASS — 10 files byte-identical** |
| Reproducibility score | **100%** |
| Strict final validation | **ISSUES NONE** |
| Status | **✅ Completed** |
| Execution mode | **Single-agent, end to end** |
| Timestamp | **2026-11-11 · IST** |

Back to [`phase_4.md`](phase_4.md) · [`plan.md`](plan.md) · [`TRACKER.csv`](TRACKER.csv) · [`status.json`](status.json)
