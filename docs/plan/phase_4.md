# Phase 4 — Stage 3 — six-qubit conversion simulation

**File:** `docs/plan/phase_4.md`  
**Master:** [plan.md](plan.md)  
**Status:** ✅ Completed  
**Execution:** single-agent, end to end  
**Completed:** 2026-11-11 · IST  
**Last validated:** 2026-11-11 · IST  
**Completion report:** [phase_4_completion.md](phase_4_completion.md)

## 1. Goal

Estimate Pr(K ≥ 3) with one qubit per selected customer and verify the result against exact, ideal, finite-shot, Monte Carlo, noisy, and mitigated references.

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

Phase 3 selected six and Phase 2 probabilities.

## 4. Sub-phases — work packages

| ID | Sub-phase | Workstream | Objective | Validation detail | Evidence | Parallelizable? |
|---|---|---|---|---|---|---|
| 4.1 | Customer-to-qubit mapping | Quantum | Remove bit-order ambiguity. | q0 is rightmost character; mapping exact. | `results/stage3_simulation.json` | No |
| 4.2 | RY state preparation | Quantum | Prepare independent Bernoulli qubits. | Six angles match the six Stage 1 probabilities. | `results/stage3_simulation.json` | Yes |
| 4.3 | Exact Poisson-binomial reference | Validation | Compute the 64-outcome ground truth. | 0.4164131424084104; ideal statevector agrees to 1e-16. | `results/stage3_simulation.json` | Yes |
| 4.4 | Aer noiseless finite-shot | Quantum | Run the ideal sampled simulation. | 0.420379638671875; error 0.003966496; within 95% half-width. | `results/stage3_simulation.json` | Yes |
| 4.5 | Monte Carlo cross-check | Validation | Independently validate the tail probability. | 0.415130615234375; error 0.001282527. | `results/stage3_simulation.json` | Yes |
| 4.6 | Synthetic noise model | Quantum | Quantify noise sensitivity. | 0.43133544921875; noisy error 0.014922307. | `results/stage3_simulation.json` | Yes |
| 4.7 | Mitigation and cross-check | Validation | Reduce known-channel bias. | Mitigated error 0.004014931 is below noisy error. | `results/stage3_simulation.json` | Yes |
| 4.8 | Circuit and shot ledger | Quantum | Lock reproducibility metadata. | All circuit fields match the technical report. | `results/stage3_simulation.json` | No |

### Sub-phase actions

- **4.1 Customer-to-qubit mapping** — Map six IDs to q0…q5 and state Qiskit c5…c0 printing convention. Output: `qubit_order, customer_to_qubit_mapping`.
- **4.2 RY state preparation** — Use θᵢ = 2 arcsin √pᵢ for the six probabilities. Output: `ry_angles`.
- **4.3 Exact Poisson-binomial reference** — Enumerate all outcomes and sum Hamming weight ≥ 3. Output: `exact_analytical_probability`.
- **4.4 Aer noiseless finite-shot** — Use AerSimulator with 32768 shots and record full counts. Output: `noiseless_finite_shot_probability, noiseless_counts`.
- **4.5 Monte Carlo cross-check** — Classical Monte Carlo with seeded sampling. Output: `monte_carlo_probability`.
- **4.6 Synthetic noise model** — Apply depolarizing 0.02 and readout 0.03; record noisy counts. Output: `noisy_probability, noisy_counts`.
- **4.7 Mitigation and cross-check** — Primary marginal inversion; 64×64 NNLS response-matrix cross-check. Output: `mitigated_probability, response_matrix_mitigated_probability`.
- **4.8 Circuit and shot ledger** — Record 6 qubits, depth 1, 6 one-qubit gates, 0 two-qubit/SWAP, shots, and CI. Output: `stage3 circuit fields`.

### Sub-phase checklist

- [x] **4.1** Customer-to-qubit mapping — q0 is rightmost character; mapping exact.
- [x] **4.2** RY state preparation — Six angles match the six Stage 1 probabilities.
- [x] **4.3** Exact Poisson-binomial reference — 0.4164131424084104; ideal statevector agrees to 1e-16.
- [x] **4.4** Aer noiseless finite-shot — 0.420379638671875; error 0.003966496; within 95% half-width.
- [x] **4.5** Monte Carlo cross-check — 0.415130615234375; error 0.001282527.
- [x] **4.6** Synthetic noise model — 0.43133544921875; noisy error 0.014922307.
- [x] **4.7** Mitigation and cross-check — Mitigated error 0.004014931 is below noisy error.
- [x] **4.8** Circuit and shot ledger — All circuit fields match the technical report.

## 5. Validation details

**Phase gate:** Exact 0.4164131424084104; ideal 0.4164131424084103; Aer 0.420379638671875; mitigated error 0.004014931 < noisy error 0.014922307; 6 qubits, depth 1, 0 two-qubit/SWAP gates; bit order stated; full counts preserved.

Every sub-phase above carries its own validation detail and evidence path. The phase gate remains ✅ Verified; Phase 4 itself is ✅ Completed end to end in a single-agent pass.

## 6. Exact reference data

- Mapping: q0 C0170, q1 C0256, q2 C0327, q3 C0374, q4 C0059, q5 C0372.
- RY angles: 1.473820, 1.440338, 1.406325, 1.224886, 1.221330, 1.208998.
- Exact 0.4164131424084104; ideal statevector 0.4164131424084103; Aer finite-shot 0.420379638671875.
- Monte Carlo 0.415130615234375; noisy 0.43133544921875; mitigated 0.41239821154870004; NNLS 0.4111108154155694.
- Noise: depolarizing 0.02, symmetric readout 0.03; mitigation = noise-model-aware marginal inversion with 64×64 NNLS cross-check.
- Shots: 32768 noiseless + 32768 noisy; 95% half-width 0.005337600548893514.
- Fresh-clone reproduction: full `src/run_benchmark.py` + `src/make_report.py` run verified; 10 result/metadata files byte-identical; canonical summary exact with timing fields normalized.
- CSV/JSON parity: same qubit mapping, RY angles, probabilities, errors, noise model, and 64-bin count dictionaries.

## 7. Deliverables and evidence

- Canonical results: `results/`
- Documentation: `docs/`, `README.md`
- Source: `src/`
- Plan artifacts: `docs/plan/plan.md`, `docs/plan/phase_4_completion.md`, `docs/plan/TRACKER.csv`, `docs/plan/status.json`
- Per-sub-phase evidence is listed in the work-package table above.

## 8. Split-work guidance

Quantum workstream owns 4.1–4.4 and 4.6–4.8; validation workstream owns 4.3, 4.5, and 4.7.

## 9. Risks and controls

Bit-order mistakes or overclaiming mitigation; mitigated by explicit q0 rightmost note, product-state design, and NNLS cross-check.

## 10. Definition of done

`results/stage3_simulation.json` and `results/stage3_simulation.csv` carry the qubit mapping, `RY` angles, all probability views, errors, noise model, and 64-bin count dictionaries. Verified by isolated fresh-clone full benchmark and report regeneration with 10 byte-identical result/metadata files.

## 11. End-to-end completion record

| Field | Value |
|---|---|
| Status | ✅ Completed |
| Execution | Single-agent, end to end, without splitting Phase 4 across workstreams |
| Completed | 2026-11-11 · IST |
| Sub-phases | 8 / 8 completed |
| Full report | [phase_4_completion.md](phase_4_completion.md) |
| Phase gate | PASS · ✅ Verified — qubit mapping, `RY` angles, exact Poisson-binomial, ideal statevector, Aer finite-shot, Monte Carlo, synthetic noise, marginal/NNLS mitigation, and circuit/count ledger all validated |
| Fresh-clone result | `src/run_benchmark.py` and `src/make_report.py` succeeded; 10 result/metadata files byte-identical; canonical summary exact with timing fields normalized |
| Downstream handoff | Phases 5–6 are ✅ Completed across Stage 1/2/3 integration, 30/30 benchmark gates, reproducibility, narrative consistency, and external handoff governance |

The completion report records the 32-check source audit, pinned environment, six-qubit mapping and `RY` table, full `K = 0…6` Poisson-binomial distribution, noise/mitigation derivations, 64-bin count ledgers, CSV/JSON parity, eight Stage 3 metric rows, isolated fresh-clone reproduction, validation matrix, and sign-off for every Phase 4 sub-phase.

---

Back to [master plan](plan.md) · [Plan README](README.md) · [Tracker](TRACKER.csv)
