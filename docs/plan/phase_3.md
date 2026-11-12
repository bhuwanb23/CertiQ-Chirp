# Phase 3 — Stage 2 — certified quantum-assisted selection

**File:** `docs/plan/phase_3.md`  
**Master:** [plan.md](plan.md)  
**Status:** ✅ Completed  
**Execution:** single-agent, end to end  
**Completed:** 2026-11-11 · IST  
**Completion report:** [phase_3_completion.md](phase_3_completion.md)  
**Last validated:** 2026-11-11 · IST

## 1. Goal

Choose exactly six of the top 10 customers maximizing expected net value under budget and capacity, with a disclosed QAOA run and an exact classical certificate.

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

Phase 2 probability vector.

## 4. Sub-phases — work packages

| ID | Sub-phase | Workstream | Objective | Validation detail | Evidence | Parallelizable? |
|---|---|---|---|---|---|---|
| 3.1 | Candidate input assembly | Optimization | Join Stage 1 probabilities to operational data. | 10 rows, all from Phase 2 top 10, w values exact. | `results/stage2_selection.json` | No |
| 3.2 | QUBO / Ising formulation | Optimization | Encode constraints for a quantum solver. | A=B=C=500; diagonal cost oracle recorded. | `results/stage2_selection.json` | Yes |
| 3.3 | Warm-start QAOA design | Quantum | Run the 10-qubit selection experiment. | 10 qubits, 2 layers, depth 5, 8192 shots, optimized parameters stored. | `results/stage2_selection.json` | Yes |
| 3.4 | Sampling and feasibility decoding | Quantum | Decode measured bitstrings honestly. | Feasible rate 0.681396484375; raw gap 5.047731581776915 disclosed. | `results/stage2_selection.json` | Yes |
| 3.5 | Hybrid repair and exact certificate | Validation | Certify the final six. | Certified gap 0.0; hybrid_hit_exact_optimum true; 210/210 feasible. | `results/stage2_selection.json` | No |
| 3.6 | Business interpretation | Business | Translate the optimization into campaign value. | Budget 11/25, capacity 16/22, net/cost 4.162494. | `results/benchmark_summary.json` | Yes |

### Sub-phase actions

- **3.1 Candidate input assembly** — Build top-10 table with p, deposit value v, cost c, capacity h, and w = pv − c. Output: `candidate_inputs`.
- **3.2 QUBO / Ising formulation** — Use −Σwᵢxᵢ + 500(Σxᵢ−6)² + one-sided budget/capacity penalties. Output: `qaoa.penalty_coefficients`.
- **3.3 Warm-start QAOA design** — Prepare Hamming-weight-6 warm start, 2 diagonal cost layers, RX mixers, 8192 shots. Output: `qaoa diagnostics`.
- **3.4 Sampling and feasibility decoding** — Record feasible rate, best feasible bitstring, raw objective, and raw gap. Output: `qaoa best-feasible fields`.
- **3.5 Hybrid repair and exact certificate** — Apply one-swap repair, enumerate all C(10,6)=210 subsets, lock exact optimum. Output: `certified_hybrid_selected_ids`.
- **3.6 Business interpretation** — Compute budget/capacity utilization, expected conversions, deposit value, cost, and ROI. Output: `business block`.

### Sub-phase checklist

- [x] **3.1** Candidate input assembly — 10 rows, all from Phase 2 top 10, w values exact.
- [x] **3.2** QUBO / Ising formulation — A=B=C=500; diagonal cost oracle recorded.
- [x] **3.3** Warm-start QAOA design — 10 qubits, 2 layers, depth 5, 8192 shots, optimized parameters stored.
- [x] **3.4** Sampling and feasibility decoding — Feasible rate 0.681396484375; raw gap 5.047731581776915 disclosed.
- [x] **3.5** Hybrid repair and exact certificate — Certified gap 0.0; hybrid_hit_exact_optimum true; 210/210 feasible.
- [x] **3.6** Business interpretation — Budget 11/25, capacity 16/22, net/cost 4.162494.

## 5. Validation details

**Phase gate:** Six unique IDs from top 10; Σcost=11≤25; Σcapacity=16≤22; exact objective 45.78743946915947; 210/210 subsets checked; raw QAOA gap 5.047731581776915 disclosed; certified hybrid gap 0.0.

Every sub-phase above carries its own validation detail and evidence path. The phase gate remains ✅ Verified when all sub-phase checkboxes are checked and the phase gate matches the canonical result files.

## 6. Exact reference data

- Objective: wᵢ = pᵢvᵢ − cᵢ; maximize Σwᵢxᵢ subject to Σxᵢ = 6, Σcᵢxᵢ ≤ 25, Σhᵢxᵢ ≤ 22.
- Penalties: exact_K = budget = capacity = 500, normalized before phase application.
- QAOA: 10 qubits, 2 layers, logical depth 5, ops rx=20 / ry=10 / diagonal=2, 8192 shots.
- QAOA feasible rate 0.681396484375; best feasible bitstring 1100101110; raw objective 40.73970788738256.
- Exact certificate bitstring 1110000111; selected C0059, C0170, C0256, C0327, C0372, C0374.
- Business: expected conversions 2.286974, deposit value 56.787439, cost 11, net/cost 4.162494.
- Fresh-clone reproduction: full `src/run_benchmark.py` + `src/make_report.py` run verified; 10 result/metadata files byte-identical; canonical summary exact with timing fields normalized.
- CSV/JSON parity: same six IDs, exact objective, QAOA diagnostics, optimized parameters, measurement counts, and brute-force certificate.

## 7. Deliverables and evidence

- Canonical results: `results/`
- Documentation: `docs/`, `README.md`
- Source: `src/`
- Plan artifacts: `docs/plan/plan.md`, `docs/plan/phase_3_completion.md`, `docs/plan/TRACKER.csv`, `docs/plan/status.json`
- Per-sub-phase evidence is listed in the work-package table above.

## 8. Split-work guidance

Optimization workstream owns 3.1–3.2; quantum workstream owns 3.3–3.4; validation workstream owns 3.5; business workstream owns 3.6.

## 9. Risks and controls

Infeasible bitstrings or unsupported advantage claims; mitigated by penalty design, one-swap repair, brute force, and honest disclosure.

## 10. Definition of done

`results/stage2_selection.json` and `results/stage2_selection.csv` carry the same six IDs, objective, QAOA diagnostics, and brute-force certificate. Verified by isolated fresh-clone full benchmark and report regeneration with 10 byte-identical result/metadata files.

## 11. End-to-end completion record

| Field | Value |
|---|---|
| Status | ✅ Completed |
| Execution | Single-agent, end to end, without splitting Phase 3 across workstreams |
| Completed | 2026-11-11 · IST |
| Sub-phases | 6 / 6 completed |
| Full report | [phase_3_completion.md](phase_3_completion.md) |
| Phase gate | PASS · ✅ Verified — top-10 assembly, QUBO/Ising oracle, warm-start QAOA, honest decoding, one-swap repair, exact certificate, and business interpretation all validated |
| Fresh-clone result | `src/run_benchmark.py` and `src/make_report.py` succeeded; 10 result/metadata files byte-identical; canonical summary exact with timing fields normalized |
| Downstream handoff | All Phases 4–6 are ✅ Completed from the six selected IDs and probabilities |

The completion report records the 27-check source audit, pinned environment, 10-row candidate table, 2¹⁰-state cost oracle, QAOA diagnostics and measurement counts, exact 210-subset certificate, CSV/JSON parity, six Stage 2 metric rows, business recomputation, Stage 3 traceability, isolated fresh-clone reproduction, validation matrix, and sign-off for every Phase 3 sub-phase.

---

Back to [master plan](plan.md) · [Plan README](README.md) · [Tracker](TRACKER.csv)
