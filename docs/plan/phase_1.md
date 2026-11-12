# Phase 1 — Data, environment & reproducibility baseline

**File:** `docs/plan/phase_1.md`  
**Master:** [plan.md](plan.md)  
**Status:** ✅ Completed  
**Execution:** single-agent, end to end  
**Completed:** 2026-11-11 · IST  
**Completion report:** [phase_1_completion.md](phase_1_completion.md)

## 1. Goal

Establish a clean, reproducible foundation from the official workbook, pinned dependencies, seed manifest, and lean repo layout.

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

Phase 0.

## 4. Sub-phases — work packages

| ID | Sub-phase | Workstream | Objective | Validation detail | Evidence | Parallelizable? |
|---|---|---|---|---|---|---|
| 1.1 | Workbook intake and schema audit | Data | Verify the released workbook structure. | 5 sheets, expected shapes, IDs C0001–C0400. | `data/raw/bank_campaign_participant_release.xlsx` | Yes |
| 1.2 | Data integrity controls | Data | Lock leakage and key rules. | No duplicate IDs; probabilities in [0,1]; one row per test customer. | `results/stage1_predictions.csv` | Yes |
| 1.3 | Environment pinning | Reproducibility | Freeze exact package versions. | 11 pinned packages match benchmark_summary.json versions. | `requirements.txt` | Yes |
| 1.4 | Seed manifest | Reproducibility | Record every stochastic seed. | All 8 seed fields match benchmark_summary.json. | `seeds.json` | Yes |
| 1.5 | Repo layout and run commands | Reproducibility | Make the lean repo runnable end to end. | py_compile passes; make_report regenerates benchmark_report.md and BENCHMARK_README.md. | `src/run_benchmark.py, src/make_report.py` | No |

### Sub-phase actions

- **1.1 Workbook intake and schema audit** — Load all 5 sheets, confirm shapes, column names, and ID coverage. Output: `data/raw/bank_campaign_participant_release.xlsx`.
- **1.2 Data integrity controls** — Confirm train/test disjointness, 35 positives, zero nulls, sentinel handling, and customer_id as universal key. Output: `results/stage1_predictions.csv`.
- **1.3 Environment pinning** — Write requirements.txt from the executed benchmark environment. Output: `requirements.txt`.
- **1.4 Seed manifest** — Write seeds.json with split, CV, QAOA, simulator, Monte Carlo, and bootstrap seeds. Output: `seeds.json`.
- **1.5 Repo layout and run commands** — Point src/run_benchmark.py to data/raw and results/; point src/make_report.py to results/ and docs/. Output: `src/, README.md`.

### Sub-phase checklist

- [x] **1.1** Workbook intake and schema audit — 5 sheets, expected shapes, IDs C0001–C0400.
- [x] **1.2** Data integrity controls — No duplicate IDs; probabilities in [0,1]; one row per test customer.
- [x] **1.3** Environment pinning — 11 pinned packages match benchmark_summary.json versions.
- [x] **1.4** Seed manifest — All 8 seed fields match benchmark_summary.json.
- [x] **1.5** Repo layout and run commands — py_compile passes; make_report regenerates benchmark_report.md and BENCHMARK_README.md.

## 5. Validation details

**Phase gate:** Workbook at data/raw with 5 sheets and zero nulls; train/test IDs disjoint; requirements.txt pinned; seeds.json exact; py_compile passed; make_report ran; reproducibility score 100%.

Every sub-phase above carries its own validation detail and evidence path. The phase is Verified only when all sub-phase checkboxes are checked and the phase gate matches the canonical result files.

## 6. Exact reference data

- Workbook sheets: README 20×2, Stage1_Train 300×17, Stage1_Test 100×16, Stage2_Data 400×5, Stage2_Constraints 6×4.
- IDs C0001–C0400; 35 train positives / 265 negatives; hidden test 11 positives / 89 negatives.
- Zero nulls; categorical unknown values are the literal `unknown`; pdays = −1 is a sentinel; duration removed.
- Pinned: Qiskit 2.6.2, Qiskit Aer 0.18.2, scikit-learn 1.6.1, XGBoost 3.4.1, CatBoost 1.2.10, LightGBM 4.7.0.
- Seeds: sampling 42, split 42, cv_repeats [42,142,242], meta_cv 999, qaoa 2026, simulator 31415, monte_carlo 27182, bootstrap 1618.
- Fresh-clone reproduction: full `src/run_benchmark.py` + `src/make_report.py` run verified; 10 result/metadata files byte-identical; canonical summary exact with timing fields normalized.

## 7. Deliverables and evidence

- Canonical results: `results/`
- Documentation: `docs/`, `README.md`
- Source: `src/`
- Plan artifacts: `docs/plan/plan.md`, `docs/plan/phase_1_completion.md`, `docs/plan/TRACKER.csv`, `docs/plan/status.json`
- Per-sub-phase evidence is listed in the work-package table above.

## 8. Split-work guidance

Data workstream owns 1.1–1.2; reproducibility workstream owns 1.3–1.5.

## 9. Risks and controls

Leakage from hidden test labels or environment drift; mitigated by training-only preprocessing, pinned versions, and seed manifest.

## 10. Definition of done

A fresh clone can install requirements, run `src/run_benchmark.py`, and reproduce `results/` from `data/raw`. Verified by an isolated fresh-clone full benchmark and report regeneration with 10 byte-identical result/metadata files.

## 11. End-to-end completion record

| Field | Value |
|---|---|
| Status | ✅ Completed |
| Execution | Single-agent, end to end, without splitting Phase 1 across workstreams |
| Completed | 2026-11-11 · IST |
| Sub-phases | 5 / 5 completed |
| Full report | [phase_1_completion.md](phase_1_completion.md) |
| Phase gate | PASS — workbook, data integrity, environment, seeds, layout, and fresh-clone reproduction all validated |
| Fresh-clone result | `src/run_benchmark.py` and `src/make_report.py` succeeded; 10 result/metadata files byte-identical; canonical summary exact with timing fields normalized |
| Downstream handoff | All Phases 2–6 are ✅ Completed on top of the locked workbook, pinned stack, seed manifest, Stage 1–3 outputs, 30/30 benchmark gates, and 100% reproducibility baseline |

The completion report records the workbook schema, data-integrity ledger, environment and seed tables, isolated fresh-clone reproduction, generator alignment, exact canonical values, validation matrix, and sign-off for every Phase 1 sub-phase.

---

Back to [master plan](plan.md) · [Plan README](README.md) · [Tracker](TRACKER.csv)
