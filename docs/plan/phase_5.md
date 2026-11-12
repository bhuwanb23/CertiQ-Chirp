# Phase 5 — End-to-end integration, 30-metric benchmark & validation

**File:** `docs/plan/phase_5.md`  
**Master:** [plan.md](plan.md)  
**Status:** ✅ Completed  
**Execution:** single-agent, end to end  
**Completed:** 2026-11-11 · IST  
**Last validated:** 2026-11-11 · IST  
**Completion report:** [phase_5_completion.md](phase_5_completion.md)

## 1. Goal

Bind the three stages into one traceable system, publish the 30-metric evidence table, and lock the reproducibility and honesty checks.

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

Phases 2, 3, and 4.

## 4. Sub-phases — work packages

| ID | Sub-phase | Workstream | Objective | Validation detail | Evidence | Parallelizable? |
|---|---|---|---|---|---|---|
| 5.1 | Continuous probability propagation | Integration | Keep one probability vector across stages. | Six Stage 3 probabilities equal the six selected Stage 1 probabilities. | `results/stage1_predictions.csv` | No |
| 5.2 | ID traceability | Integration | Prove end-to-end key continuity. | All six IDs appear in all three result files. | `results/stage2_selection.json, results/stage3_simulation.json` | Yes |
| 5.3 | Error propagation analysis | Integration | Quantify uncertainty transmission. | CI width 0.206885, CV std 0.016480, certified gap 0.0, finite-shot error 0.003966 recorded. | `results/benchmark_report.md` | Yes |
| 5.4 | 30-metric table | Validation | Publish the complete evidence table. | Exactly 30 rows; names match the locked metric list. | `results/benchmark_metrics.csv` | Yes |
| 5.5 | Reproducibility checks | Validation | Confirm the runnable package. | 10/10 checks true; score 100.0. | `results/benchmark_summary.json` | Yes |
| 5.6 | Readiness estimate | Validation | Record a conservative rubric-aligned planning figure. | 89/100 with per-criterion split 33/26/20/10. | `docs/04_TECHNICAL_REPORT.md` | Yes |
| 5.7 | Honest limitation register | Communication | Keep claims defensible. | All six constraints appear in the technical report. | `docs/04_TECHNICAL_REPORT.md` | Yes |

### Sub-phase actions

- **5.1 Continuous probability propagation** — Verify Stage 2 wᵢ and Stage 3 pᵢ come from the same Stage 1 rows. Output: `results/stage2_selection.json, results/stage3_simulation.json`.
- **5.2 ID traceability** — Trace top 10 → selected six → qubit mapping using customer_id. Output: `devpost_form_selected_ids, customer_to_qubit_mapping`.
- **5.3 Error propagation analysis** — Combine bootstrap CI, CV stability, Stage 2 gaps, and Stage 3 errors. Output: `benchmark_report.md`.
- **5.4 30-metric table** — Write 30 rows with winning idea, best classical, quantum-only, target, direction, and rationale. Output: `results/benchmark_metrics.csv`.
- **5.5 Reproducibility checks** — Check script, requirements, seeds, license, three result files, exact references, full counts/noise. Output: `reproducibility block`.
- **5.6 Readiness estimate** — Map evidence to 35/30/20/15 criteria and state it is not an official score. Output: `docs/04_TECHNICAL_REPORT.md`.
- **5.7 Honest limitation register** — Record hidden labels, wide CI, weak QSVC ranking, raw QAOA gap, synthetic noise, and no advantage claim. Output: `docs/04_TECHNICAL_REPORT.md`.

### Sub-phase checklist

- [x] **5.1** Continuous probability propagation — Six Stage 3 probabilities equal the six selected Stage 1 probabilities.
- [x] **5.2** ID traceability — All six IDs appear in all three result files.
- [x] **5.3** Error propagation analysis — CI width 0.206885, CV std 0.016480, certified gap 0.0, finite-shot error 0.003966 recorded.
- [x] **5.4** 30-metric table — Exactly 30 rows; names match the locked metric list.
- [x] **5.5** Reproducibility checks — 10/10 checks true; score 100.0.
- [x] **5.6** Readiness estimate — 89/100 with per-criterion split 33/26/20/10.
- [x] **5.7** Honest limitation register — All six constraints appear in the technical report.

## 5. Validation details

**Phase gate:** 30/30 engineering gates passed; reproducibility 100%; exact Stage 2 gap 0.0; exact Stage 3 reference present; ID traceability intact; no unsupported quantum-advantage claim; runtime 145.9735 s recorded.

Every sub-phase above carries its own validation detail and evidence path. The phase gate remains ✅ Verified; Phase 5 itself is ✅ Completed end to end in a single-agent pass.

## 6. Exact reference data

- 30 metric rows: 10 Stage 1, 5 Stage 2, 8 Stage 3, plus ROI, reproducibility, and supporting gates.
- Reproducibility checks: 10/10, score 100.0.
- Runtime: 145.9735211939999 s.
- Conservative readiness estimate: 89/100 (quantum 33/35, accuracy 26/30, reproducibility 20/20, communication 10/15); planning figure, not an official judge score.
- Known constraints: hidden labels unknown, wide PR-AUC CI, QSVC weak ranker, nonzero raw QAOA gap, synthetic noise, no quantum-advantage claim.
- Metric composition reconciled: 14 `Stage 1 …` rows (10 core OOF/decile + 4 supporting), 6 `Stage 2 …` rows (5 core + raw QAOA gap), 8 `Stage 3 …` rows, 1 ROI row, and 1 reproducibility row = 30 rows; 30/30 engineering gates passed.
- Fresh-clone reproduction: full `src/run_benchmark.py` + `src/make_report.py` run verified; 10 result/metadata files byte-identical; canonical summary exact with timing fields normalized.

## 7. Deliverables and evidence

- Canonical results: `results/`
- Documentation: `docs/`, `README.md`
- Source: `src/`
- Plan artifacts: `docs/plan/plan.md`, `docs/plan/phase_5_completion.md`, `docs/plan/TRACKER.csv`, `docs/plan/status.json`
- Per-sub-phase evidence is listed in the work-package table above.

## 8. Split-work guidance

Integration workstream owns 5.1–5.3; validation workstream owns 5.4–5.5; communication workstream owns 5.6–5.7.

## 9. Risks and controls

Silent drift between narrative and result files; mitigated by exact-value consistency checks and a single canonical summary JSON.

## 10. Definition of done

`results/benchmark_metrics.csv`, `results/benchmark_summary.json`, and `results/benchmark_report.md` agree with `docs/04_TECHNICAL_REPORT.md` and `README.md`. Verified by isolated fresh-clone full benchmark and report regeneration with 10 byte-identical result/metadata files.

## 11. End-to-end completion record

| Field | Value |
|---|---|
| Status | ✅ Completed |
| Execution | Single-agent, end to end, without splitting Phase 5 across workstreams |
| Completed | 2026-11-11 · IST |
| Sub-phases | 7 / 7 completed |
| Full report | [phase_5_completion.md](phase_5_completion.md) |
| Phase gate | PASS · ✅ Verified — continuous probability propagation, ID traceability, error propagation, 30-metric benchmark & 30/30 engineering gates, 10/10 reproducibility (`100.0%`), `89/100` planning estimate, and 6-item limitation register all validated |
| Fresh-clone result | `src/run_benchmark.py` and `src/make_report.py` succeeded; 10 result/metadata files byte-identical; canonical summary exact with timing fields normalized |
| Downstream handoff | Phase 6 is ✅ Completed from the locked 30/30-gated evidence base across `results/`, `docs/04_TECHNICAL_REPORT.md`, and `README.md` |

The completion report records the 22-check integration source audit, pinned environment, Stage 1→2→3 probability and ID continuity table, error-propagation ledger, full 30-metric table and 30/30 gate verification, 10/10 reproducibility checklist, rubric-mapped `89/100` planning estimate, 6-item limitation register, isolated fresh-clone reproduction, validation matrix, and sign-off for every Phase 5 sub-phase.

---

Back to [master plan](plan.md) · [Plan README](README.md) · [Tracker](TRACKER.csv)
