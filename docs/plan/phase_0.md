# Phase 0 — Project charter, research lock & plan control

**File:** `docs/plan/phase_0.md`  
**Master:** [plan.md](plan.md)  
**Status:** ✅ Completed  
**Execution:** single-agent, end to end  
**Completed:** 2026-11-11 · IST  
**Completion report:** [phase_0_completion.md](phase_0_completion.md)

## 1. Goal

Lock the authoritative problem interpretation, success criteria, project identity, and planning conventions before any modeling work is split across workstreams.

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

None — this is the root phase.

## 4. Sub-phases — work packages

| ID | Sub-phase | Workstream | Objective | Validation detail | Evidence | Parallelizable? |
|---|---|---|---|---|---|---|
| 0.1 | Event and source hierarchy lock | Research | Confirm the authoritative source order and event facts. | Priority order and event metadata are explicit. | `docs/01_HACKATHON_ANALYSIS.md` | Yes |
| 0.2 | Authoritative challenge extraction | Research | Normalize the four-page problem statement into a working spec. | Stage 1/2/3 formulas, constraints, and 35/30/20/15 rubric match the PDF. | `docs/02_TECHNICAL_SPEC.md` | Yes |
| 0.3 | Project identity and domain lock | Research | Fix the name, pitch, and domain classification. | Name, pitch, and domain appear consistently in repo and handoffs. | `README.md` | Yes |
| 0.4 | Success metrics and validation philosophy | Validation | Define how the project will be judged and verified. | All acceptance gates reference exact files and numbers. | `results/benchmark_metrics.csv` | Yes |
| 0.5 | Plan structure and tracking conventions | Communication | Create the split-work planning layer. | Every phase has a file, goal, sub-phases, validation, and status. | `docs/plan/` | Yes |

### Sub-phase actions

- **0.1 Event and source hierarchy lock** — Review Devpost overview/rules/resources, QFF site, Drive PDF, workbook, and calendar; record contradictions. Output: `docs/01_HACKATHON_ANALYSIS.md`.
- **0.2 Authoritative challenge extraction** — Extract §§1–9: three linked stages, constraints, deliverables, reproducibility, and scoring. Output: `docs/02_TECHNICAL_SPEC.md`.
- **0.3 Project identity and domain lock** — Lock “CertiQ-Chirp”, the 157-character pitch, and Fintech primary classification. Output: `README.md`.
- **0.4 Success metrics and validation philosophy** — Lock hidden-label evaluation, exact classical references, leakage rules, and no quantum-advantage claim. Output: `plan.md global gates`.
- **0.5 Plan structure and tracking conventions** — Create docs/plan/plan.md, phase_0.md…phase_6.md, TRACKER.csv, status.json, and README.md. Output: `docs/plan/`.

### Sub-phase checklist

- [x] **0.1** Event and source hierarchy lock — Priority order and event metadata are explicit.
- [x] **0.2** Authoritative challenge extraction — Stage 1/2/3 formulas, constraints, and 35/30/20/15 rubric match the PDF.
- [x] **0.3** Project identity and domain lock — Name, pitch, and domain appear consistently in repo and handoffs.
- [x] **0.4** Success metrics and validation philosophy — All acceptance gates reference exact files and numbers.
- [x] **0.5** Plan structure and tracking conventions — Every phase has a file, goal, sub-phases, validation, and status.

## 5. Validation details

**Phase gate:** Source priority documented; normalized spec present; rubric weights locked; project identity/domain locked; plan.md, phase files, TRACKER.csv, and status.json cross-linked; all phases Verified.

Every sub-phase above carries its own validation detail and evidence path. The phase is Verified only when all sub-phase checkboxes are checked and the phase gate matches the canonical result files.

## 6. Exact reference data

- Event: The Atomiq Hackathon | Qiskit Fall Fest 2026 at IEM; theme “Chi(r)ps: A Decade of Harmony on the Cloud”.
- Deadline: 2026-11-11 22:00 IST / 16:30 UTC.
- Domain: Fintech primary; AI/ML + Quantum ML/Optimization secondary.
- Project: CertiQ-Chirp: Certified Quantum Campaign Intelligence.
- Final answers: six customer IDs and Pr(K ≥ 3).
- Rubric: Quantum Rigor 35 / Accuracy & Integration 30 / Reproducibility 20 / Communication 15.

## 7. Deliverables and evidence

- Canonical results: `results/`
- Documentation: `docs/`, `README.md`
- Source: `src/`
- Plan artifacts: `docs/plan/plan.md`, `docs/plan/phase_0_completion.md`, `docs/plan/TRACKER.csv`, `docs/plan/status.json`
- Per-sub-phase evidence is listed in the work-package table above.

## 8. Split-work guidance

Research workstream owns 0.1–0.3; validation workstream owns 0.4; communication workstream owns 0.5.

## 9. Risks and controls

Conflicting public pages vs. released PDF; mitigated by source priority PDF+workbook > Devpost Rules > Overview > QFF site > registration form.

## 10. Definition of done

Every later phase references this charter, and no downstream result contradicts the locked spec or exact values.

## 11. All main phases at a glance

| Phase | File | Title | Goal | Validation gate | Status |
|---|---|---|---|---|---|
| Phase 0 | [phase_0.md](phase_0.md) | Project charter, research lock & plan control | Lock the authoritative problem interpretation, success criteria, project identity, and planning conventions before any modeling work is split across workstreams. | Source priority documented; normalized spec present; rubric weights locked; project identity/domain locked; plan.md, phase files, TRACKER.csv, and status.json cross-linked; all phases Verified. | ✅ Completed |
| Phase 1 | [phase_1.md](phase_1.md) | Data, environment & reproducibility baseline | Establish a clean, reproducible foundation from the official workbook, pinned dependencies, seed manifest, and lean repo layout. | Workbook at data/raw with 5 sheets and zero nulls; train/test IDs disjoint; requirements.txt pinned; seeds.json exact; py_compile passed; make_report ran; reproducibility score 100%. | ✅ Completed |
| Phase 2 | [phase_2.md](phase_2.md) | Stage 1 — calibrated hybrid prediction | Produce one continuous, leakage-free probability vector for all 100 test customers, rank the top 10, and lock the Stage 1 metric suite. | 3×5 stratified OOF CV only; 100 unique test IDs; deterministic rank with customer_id tie-break; top-10 flag exactly 10 rows; winner rank_calibrated_hybrid composite 0.447516; metrics match benchmark_metrics.csv. | ✅ Completed |
| Phase 3 | [phase_3.md](phase_3.md) | Stage 2 — certified quantum-assisted selection | Choose exactly six of the top 10 customers maximizing expected net value under budget and capacity, with a disclosed QAOA run and an exact classical certificate. | Six unique IDs from top 10; Σcost=11≤25; Σcapacity=16≤22; exact objective 45.78743946915947; 210/210 subsets checked; raw QAOA gap 5.047731581776915 disclosed; certified hybrid gap 0.0. | ✅ Completed |
| Phase 4 | [phase_4.md](phase_4.md) | Stage 3 — six-qubit conversion simulation | Estimate Pr(K ≥ 3) with one qubit per selected customer and verify the result against exact, ideal, finite-shot, Monte Carlo, noisy, and mitigated references. | Exact 0.4164131424084104; ideal 0.4164131424084103; Aer 0.420379638671875; mitigated error 0.004014931 < noisy error 0.014922307; 6 qubits, depth 1, 0 two-qubit/SWAP gates; bit order stated; full counts preserved. | ✅ Completed |
| Phase 5 | [phase_5.md](phase_5.md) | End-to-end integration, 30-metric benchmark & validation | Bind the three stages into one traceable system, publish the 30-metric evidence table, and lock the reproducibility and honesty checks. | 30/30 engineering gates passed; reproducibility 100%; exact Stage 2 gap 0.0; exact Stage 3 reference present; ID traceability intact; no unsupported quantum-advantage claim; runtime 145.9735 s recorded. | ✅ Completed |
| Phase 6 | [phase_6.md](phase_6.md) | Technical communication, evidence pack & submission handoff | Present the project as a coherent, professional, reproducible story with exact values, visual evidence, and external handoffs consistent with the lean repo. | Exact values consistent across README, docs, results, and external media; 21 diagram sources and branded gallery plates present in the external pack; no unsupported advantage claim; lean repo remains under budget; README points to docs/plan/. | ✅ Completed |

## 12. Complete master sub-phase register

This is the full 44-sub-phase register from `plan.md` Section 6, reproduced here so Phase 0 can be used as the project-control handoff. Individual `phase_1.md`…`phase_6.md` files expand their own rows with actions, risks, and split-work guidance.

### Phase 0 — Project charter, research lock & plan control

| Sub-phase | Workstream | Title | Objective | Validation detail | Evidence | Status |
|---|---|---|---|---|---|---|
| 0.1 | Research | Event and source hierarchy lock | Confirm the authoritative source order and event facts. | Priority order and event metadata are explicit. | `docs/01_HACKATHON_ANALYSIS.md` | ✅ Completed |
| 0.2 | Research | Authoritative challenge extraction | Normalize the four-page problem statement into a working spec. | Stage 1/2/3 formulas, constraints, and 35/30/20/15 rubric match the PDF. | `docs/02_TECHNICAL_SPEC.md` | ✅ Completed |
| 0.3 | Research | Project identity and domain lock | Fix the name, pitch, and domain classification. | Name, pitch, and domain appear consistently in repo and handoffs. | `README.md` | ✅ Completed |
| 0.4 | Validation | Success metrics and validation philosophy | Define how the project will be judged and verified. | All acceptance gates reference exact files and numbers. | `results/benchmark_metrics.csv` | ✅ Completed |
| 0.5 | Communication | Plan structure and tracking conventions | Create the split-work planning layer. | Every phase has a file, goal, sub-phases, validation, and status. | `docs/plan/` | ✅ Completed |

**Checklist**

- [x] **0.1** Event and source hierarchy lock — Priority order and event metadata are explicit.
- [x] **0.2** Authoritative challenge extraction — Stage 1/2/3 formulas, constraints, and 35/30/20/15 rubric match the PDF.
- [x] **0.3** Project identity and domain lock — Name, pitch, and domain appear consistently in repo and handoffs.
- [x] **0.4** Success metrics and validation philosophy — All acceptance gates reference exact files and numbers.
- [x] **0.5** Plan structure and tracking conventions — Every phase has a file, goal, sub-phases, validation, and status.


### Phase 1 — Data, environment & reproducibility baseline

| Sub-phase | Workstream | Title | Objective | Validation detail | Evidence | Status |
|---|---|---|---|---|---|---|
| 1.1 | Data | Workbook intake and schema audit | Verify the released workbook structure. | 5 sheets, expected shapes, IDs C0001–C0400. | `data/raw/bank_campaign_participant_release.xlsx` | ✅ Completed |
| 1.2 | Data | Data integrity controls | Lock leakage and key rules. | No duplicate IDs; probabilities in [0,1]; one row per test customer. | `results/stage1_predictions.csv` | ✅ Completed |
| 1.3 | Reproducibility | Environment pinning | Freeze exact package versions. | 11 pinned packages match benchmark_summary.json versions. | `requirements.txt` | ✅ Completed |
| 1.4 | Reproducibility | Seed manifest | Record every stochastic seed. | All 8 seed fields match benchmark_summary.json. | `seeds.json` | ✅ Completed |
| 1.5 | Reproducibility | Repo layout and run commands | Make the lean repo runnable end to end. | py_compile passes; make_report regenerates benchmark_report.md and BENCHMARK_README.md. | `src/run_benchmark.py, src/make_report.py` | ✅ Completed |

**Checklist**

- [x] **1.1** Workbook intake and schema audit — 5 sheets, expected shapes, IDs C0001–C0400.
- [x] **1.2** Data integrity controls — No duplicate IDs; probabilities in [0,1]; one row per test customer.
- [x] **1.3** Environment pinning — 11 pinned packages match benchmark_summary.json versions.
- [x] **1.4** Seed manifest — All 8 seed fields match benchmark_summary.json.
- [x] **1.5** Repo layout and run commands — py_compile passes; make_report regenerates benchmark_report.md and BENCHMARK_README.md.


### Phase 2 — Stage 1 — calibrated hybrid prediction

| Sub-phase | Workstream | Title | Objective | Validation detail | Evidence | Status |
|---|---|---|---|---|---|---|
| 2.1 | ML | Fold-local preprocessing | Prevent leakage. | No transform is fit on validation or test folds. | `results/benchmark_summary.json` | ✅ Completed |
| 2.2 | ML | Candidate model suite | Benchmark classical and quantum probabilistic models. | Six models have OOF ROC-AUC, PR-AUC, Brier, log loss, and ECE. | `results/benchmark_summary.json` | ✅ Completed |
| 2.3 | Quantum | Quantum kernel specification | Define the Qiskit feature map. | 4 qubits, depth 17, 14 u / 12 CX, dimension 16 recorded. | `results/benchmark_summary.json` | ✅ Completed |
| 2.4 | Validation | Out-of-fold validation | Select models on training data only. | CI width 0.206885 and repeat std 0.016480 recorded. | `results/benchmark_summary.json` | ✅ Completed |
| 2.5 | Validation | Fusion selection | Choose the judge-aligned probability source. | Composite 0.447516 is the maximum; best classical and quantum-only baselines retained. | `results/benchmark_summary.json` | ✅ Completed |
| 2.6 | ML | Single test prediction | Freeze and predict once. | 100 rows, probabilities in [0,1], rank 1–100, 10 true flags. | `results/stage1_predictions.csv` | ✅ Completed |
| 2.7 | Validation | Stage 1 metric lock | Lock the evidence table. | Rows match summary JSON and technical report. | `results/benchmark_metrics.csv` | ✅ Completed |

**Checklist**

- [x] **2.1** Fold-local preprocessing — No transform is fit on validation or test folds.
- [x] **2.2** Candidate model suite — Six models have OOF ROC-AUC, PR-AUC, Brier, log loss, and ECE.
- [x] **2.3** Quantum kernel specification — 4 qubits, depth 17, 14 u / 12 CX, dimension 16 recorded.
- [x] **2.4** Out-of-fold validation — CI width 0.206885 and repeat std 0.016480 recorded.
- [x] **2.5** Fusion selection — Composite 0.447516 is the maximum; best classical and quantum-only baselines retained.
- [x] **2.6** Single test prediction — 100 rows, probabilities in [0,1], rank 1–100, 10 true flags.
- [x] **2.7** Stage 1 metric lock — Rows match summary JSON and technical report.


### Phase 3 — Stage 2 — certified quantum-assisted selection

| Sub-phase | Workstream | Title | Objective | Validation detail | Evidence | Status |
|---|---|---|---|---|---|---|
| 3.1 | Optimization | Candidate input assembly | Join Stage 1 probabilities to operational data. | 10 rows, all from Phase 2 top 10, w values exact. | `results/stage2_selection.json` | ✅ Completed |
| 3.2 | Optimization | QUBO / Ising formulation | Encode constraints for a quantum solver. | A=B=C=500; diagonal cost oracle recorded. | `results/stage2_selection.json` | ✅ Completed |
| 3.3 | Quantum | Warm-start QAOA design | Run the 10-qubit selection experiment. | 10 qubits, 2 layers, depth 5, 8192 shots, optimized parameters stored. | `results/stage2_selection.json` | ✅ Completed |
| 3.4 | Quantum | Sampling and feasibility decoding | Decode measured bitstrings honestly. | Feasible rate 0.681396484375; raw gap 5.047731581776915 disclosed. | `results/stage2_selection.json` | ✅ Completed |
| 3.5 | Validation | Hybrid repair and exact certificate | Certify the final six. | Certified gap 0.0; hybrid_hit_exact_optimum true; 210/210 feasible. | `results/stage2_selection.json` | ✅ Completed |
| 3.6 | Business | Business interpretation | Translate the optimization into campaign value. | Budget 11/25, capacity 16/22, net/cost 4.162494. | `results/benchmark_summary.json` | ✅ Completed |

**Checklist**

- [x] **3.1** Candidate input assembly — 10 rows, all from Phase 2 top 10, w values exact.
- [x] **3.2** QUBO / Ising formulation — A=B=C=500; diagonal cost oracle recorded.
- [x] **3.3** Warm-start QAOA design — 10 qubits, 2 layers, depth 5, 8192 shots, optimized parameters stored.
- [x] **3.4** Sampling and feasibility decoding — Feasible rate 0.681396484375; raw gap 5.047731581776915 disclosed.
- [x] **3.5** Hybrid repair and exact certificate — Certified gap 0.0; hybrid_hit_exact_optimum true; 210/210 feasible.
- [x] **3.6** Business interpretation — Budget 11/25, capacity 16/22, net/cost 4.162494.


### Phase 4 — Stage 3 — six-qubit conversion simulation

| Sub-phase | Workstream | Title | Objective | Validation detail | Evidence | Status |
|---|---|---|---|---|---|---|
| 4.1 | Quantum | Customer-to-qubit mapping | Remove bit-order ambiguity. | q0 is rightmost character; mapping exact. | `results/stage3_simulation.json` | ✅ Completed |
| 4.2 | Quantum | RY state preparation | Prepare independent Bernoulli qubits. | Six angles match the six Stage 1 probabilities. | `results/stage3_simulation.json` | ✅ Completed |
| 4.3 | Validation | Exact Poisson-binomial reference | Compute the 64-outcome ground truth. | 0.4164131424084104; ideal statevector agrees to 1e-16. | `results/stage3_simulation.json` | ✅ Completed |
| 4.4 | Quantum | Aer noiseless finite-shot | Run the ideal sampled simulation. | 0.420379638671875; error 0.003966496; within 95% half-width. | `results/stage3_simulation.json` | ✅ Completed |
| 4.5 | Validation | Monte Carlo cross-check | Independently validate the tail probability. | 0.415130615234375; error 0.001282527. | `results/stage3_simulation.json` | ✅ Completed |
| 4.6 | Quantum | Synthetic noise model | Quantify noise sensitivity. | 0.43133544921875; noisy error 0.014922307. | `results/stage3_simulation.json` | ✅ Completed |
| 4.7 | Validation | Mitigation and cross-check | Reduce known-channel bias. | Mitigated error 0.004014931 is below noisy error. | `results/stage3_simulation.json` | ✅ Completed |
| 4.8 | Quantum | Circuit and shot ledger | Lock reproducibility metadata. | All circuit fields match the technical report. | `results/stage3_simulation.json` | ✅ Completed |

**Checklist**

- [x] **4.1** Customer-to-qubit mapping — q0 is rightmost character; mapping exact.
- [x] **4.2** RY state preparation — Six angles match the six Stage 1 probabilities.
- [x] **4.3** Exact Poisson-binomial reference — 0.4164131424084104; ideal statevector agrees to 1e-16.
- [x] **4.4** Aer noiseless finite-shot — 0.420379638671875; error 0.003966496; within 95% half-width.
- [x] **4.5** Monte Carlo cross-check — 0.415130615234375; error 0.001282527.
- [x] **4.6** Synthetic noise model — 0.43133544921875; noisy error 0.014922307.
- [x] **4.7** Mitigation and cross-check — Mitigated error 0.004014931 is below noisy error.
- [x] **4.8** Circuit and shot ledger — All circuit fields match the technical report.


### Phase 5 — End-to-end integration, 30-metric benchmark & validation

| Sub-phase | Workstream | Title | Objective | Validation detail | Evidence | Status |
|---|---|---|---|---|---|---|
| 5.1 | Integration | Continuous probability propagation | Keep one probability vector across stages. | Six Stage 3 probabilities equal the six selected Stage 1 probabilities. | `results/stage1_predictions.csv` | ✅ Completed |
| 5.2 | Integration | ID traceability | Prove end-to-end key continuity. | All six IDs appear in all three result files. | `results/stage2_selection.json, results/stage3_simulation.json` | ✅ Completed |
| 5.3 | Integration | Error propagation analysis | Quantify uncertainty transmission. | CI width 0.206885, CV std 0.016480, certified gap 0.0, finite-shot error 0.003966 recorded. | `results/benchmark_report.md` | ✅ Completed |
| 5.4 | Validation | 30-metric table | Publish the complete evidence table. | Exactly 30 rows; names match the locked metric list. | `results/benchmark_metrics.csv` | ✅ Completed |
| 5.5 | Validation | Reproducibility checks | Confirm the runnable package. | 10/10 checks true; score 100.0. | `results/benchmark_summary.json` | ✅ Completed |
| 5.6 | Validation | Readiness estimate | Record a conservative rubric-aligned planning figure. | 89/100 with per-criterion split 33/26/20/10. | `docs/04_TECHNICAL_REPORT.md` | ✅ Completed |
| 5.7 | Communication | Honest limitation register | Keep claims defensible. | All six constraints appear in the technical report. | `docs/04_TECHNICAL_REPORT.md` | ✅ Completed |

**Checklist**

- [x] **5.1** Continuous probability propagation — Six Stage 3 probabilities equal the six selected Stage 1 probabilities.
- [x] **5.2** ID traceability — All six IDs appear in all three result files.
- [x] **5.3** Error propagation analysis — CI width 0.206885, CV std 0.016480, certified gap 0.0, finite-shot error 0.003966 recorded.
- [x] **5.4** 30-metric table — Exactly 30 rows; names match the locked metric list.
- [x] **5.5** Reproducibility checks — 10/10 checks true; score 100.0.
- [x] **5.6** Readiness estimate — 89/100 with per-criterion split 33/26/20/10.
- [x] **5.7** Honest limitation register — All six constraints appear in the technical report.


### Phase 6 — Technical communication, evidence pack & submission handoff

| Sub-phase | Workstream | Title | Objective | Validation detail | Evidence | Status |
|---|---|---|---|---|---|---|
| 6.1 | Communication | Technical report and README | Provide the written source of truth. | Commands, paths, and exact values match src/ and results/. | `README.md, docs/04_TECHNICAL_REPORT.md` | ✅ Completed |
| 6.2 | Communication | Project story and pitch | Lock the narrative identity. | Name and pitch are consistent everywhere. | `README.md` | ✅ Completed |
| 6.3 | Visual | Visual evidence and media | Supply judge-friendly diagrams. | 21 diagram sources and 21 gallery plates; exact typography; no garbled text. | `External media pack` | ✅ Completed |
| 6.4 | Visual | PDF dossier and deck | Provide presentation-ready documents. | Page counts 24 / 22 / 12 / 1 / 5; stale text absent. | `External PDF pack` | ✅ Completed |
| 6.5 | Validation | Exact-value consistency | Prevent narrative drift. | All narrative values equal the canonical JSON. | `results/benchmark_summary.json` | ✅ Completed |
| 6.6 | Communication | External handoff package | Keep delivery assets outside the lean repo. | Repo stays small; generated PDFs/PNGs/SVGs/ZIPs are ignored. | `.gitignore` | ✅ Completed |

**Checklist**

- [x] **6.1** Technical report and README — Commands, paths, and exact values match src/ and results/.
- [x] **6.2** Project story and pitch — Name and pitch are consistent everywhere.
- [x] **6.3** Visual evidence and media — 21 diagram sources and 21 gallery plates; exact typography; no garbled text.
- [x] **6.4** PDF dossier and deck — Page counts 24 / 22 / 12 / 1 / 5; stale text absent.
- [x] **6.5** Exact-value consistency — All narrative values equal the canonical JSON.
- [x] **6.6** External handoff package — Repo stays small; generated PDFs/PNGs/SVGs/ZIPs are ignored.


## 13. Split-work map

| Phase | Workstreams | Handoff scope |
|---|---|---|
| Phase 0 | Research / Validation / Communication | Charter, spec, identity, success criteria, plan structure |
| Phase 1 | Data / Reproducibility | Workbook, environment, seeds, repo layout |
| Phase 2 | ML / Quantum / Validation | Leakage-free prediction, quantum kernel, fusion, top 10 |
| Phase 3 | Optimization / Quantum / Validation / Business | QUBO, QAOA, repair, certificate, business value |
| Phase 4 | Quantum / Validation | Six-qubit circuit, exact reference, noise, mitigation |
| Phase 5 | Integration / Validation / Communication | Traceability, 30 metrics, reproducibility, limitations |
| Phase 6 | Communication / Visual / Validation | Report, pitch, evidence pack, exact-value consistency |

## 14. Master identity and research base


| Field | Value |
|---|---|
| Project | CertiQ-Chirp: Certified Quantum Campaign Intelligence |
| Primary domain | Fintech / targeted term-deposit marketing |
| Secondary domains | AI/ML, quantum machine learning, constrained optimization |
| Event | The Atomiq Hackathon \| Qiskit Fall Fest 2026 at IEM |
| Theme | Chi(r)ps: A Decade of Harmony on the Cloud |
| Final answers | Six customer IDs and Pr(K ≥ 3) |
| Core SDKs | Qiskit 2.6.2, Qiskit Aer 0.18.2, scikit-learn, XGBoost, CatBoost, LightGBM |
| Claim policy | Quantum components have defined jobs; exact classical references; no unsupported quantum-advantage claim |


| Area | Exact decision |
|---|---|
| Source priority | Problem PDF + workbook > Devpost Rules > Devpost Overview > official QFF site > registration form |
| Stage 1 | 300 train → 100 test probabilities; training-only CV/calibration; rank descending, ascending customer_id ties |
| Stage 2 | Maximize Σ(pᵢvᵢ − cᵢ)xᵢ; Σxᵢ = 6; Σcᵢxᵢ ≤ 25; Σhᵢxᵢ ≤ 22; exact brute-force reference |
| Stage 3 | One RY qubit per customer; θᵢ = 2 arcsin √pᵢ; success = Hamming weight ≥ 3; exact 64-outcome Poisson-binomial |
| Rubric | Quantum Rigor 35 / Accuracy & Integration 30 / Reproducibility 20 / Communication 15 |
| Workbook | 5 sheets; 300×17 train, 100×16 test, 400×5 Stage 2 data, 6×4 constraints; zero nulls; IDs C0001–C0400 |
| Positives | 35 train / 265 negative; 11 hidden-test positives / 89 negative |
| Winner | rank_calibrated_hybrid = 0.6 QSVC + 0.4 XGBoost; best classical CatBoost; quantum-only QSVC |
| Selected six | C0059, C0170, C0256, C0327, C0372, C0374 |
| Stage 2 | Objective 45.78743946915947; budget 11/25; capacity 16/22; 210/210 feasible; certified gap 0.0 |
| Stage 3 | Exact 0.4164131424084104; Aer 0.420379638671875; submitted form value 0.420 |
| Business | Expected net 45.78743946915947; conversions 2.286974; deposit 56.787439; cost 11; net/cost 4.162494 |
| Benchmark | 30/30 gates; reproducibility 100%; runtime 145.9735211939999 s; planning estimate 89/100 |
| Environment | numpy 2.3.5, pandas 2.2.3, scikit-learn 1.6.1, qiskit 2.6.2, qiskit-aer 0.18.2, xgboost 3.4.1, catboost 1.2.10, lightgbm 4.7.0, scipy 1.17.1 |
| Seeds | sampling 42, split 42, cv_repeats [42,142,242], meta_cv 999, qaoa 2026, simulator 31415, monte_carlo 27182, bootstrap 1618 |

## 15. Exact reference data by phase

### Phase 0 — Project charter, research lock & plan control

- Event: The Atomiq Hackathon | Qiskit Fall Fest 2026 at IEM; theme “Chi(r)ps: A Decade of Harmony on the Cloud”.
- Deadline: 2026-11-11 22:00 IST / 16:30 UTC.
- Domain: Fintech primary; AI/ML + Quantum ML/Optimization secondary.
- Project: CertiQ-Chirp: Certified Quantum Campaign Intelligence.
- Final answers: six customer IDs and Pr(K ≥ 3).
- Rubric: Quantum Rigor 35 / Accuracy & Integration 30 / Reproducibility 20 / Communication 15.

### Phase 1 — Data, environment & reproducibility baseline

- Workbook sheets: README 20×2, Stage1_Train 300×17, Stage1_Test 100×16, Stage2_Data 400×5, Stage2_Constraints 6×4.
- IDs C0001–C0400; 35 train positives / 265 negatives; hidden test 11 positives / 89 negatives.
- Zero nulls; categorical unknown values are the literal `unknown`; pdays = −1 is a sentinel; duration removed.
- Pinned: Qiskit 2.6.2, Qiskit Aer 0.18.2, scikit-learn 1.6.1, XGBoost 3.4.1, CatBoost 1.2.10, LightGBM 4.7.0.
- Seeds: sampling 42, split 42, cv_repeats [42,142,242], meta_cv 999, qaoa 2026, simulator 31415, monte_carlo 27182, bootstrap 1618.
- Fresh-clone reproduction: full `src/run_benchmark.py` + `src/make_report.py` run verified; 10 result/metadata files byte-identical; canonical summary exact with timing fields normalized.

### Phase 2 — Stage 1 — calibrated hybrid prediction

- Quantum kernel: 4 qubits, reps=1, logical/transpiled depth 17, 14 u, 12 CX, statevector dimension 16.
- Winner: 0.6 QSVC + 0.4 XGBoost = rank_calibrated_hybrid; best classical CatBoost; quantum-only QSVC.
- Winner OOF: ROC-AUC 0.6069, PR-AUC 0.234718, Brier 0.103644, log loss 0.360930, ECE 0.035671, slope 0.612382.
- Top-decile: P@10 0.300000, R@10 0.257143, lift 2.571429×, NDCG@10 0.362780, KS 0.231267.
- Bootstrap PR-AUC 95% CI [0.147250, 0.354135], width 0.206885; winner repeat PR-AUC std 0.016480.
- Top 10: C0170, C0256, C0327, C0338, C0188, C0079, C0081, C0374, C0059, C0372.
- Stage 1 metric table: 14 Stage 1 rows (10 core metrics plus 4 supporting rows) inside the 30-row benchmark table.
- Fresh-clone reproduction: 3×5 OOF CV, quantum kernel, fusion, and 100-row probability vector regenerated; 10 result/metadata files byte-identical.

### Phase 3 — Stage 2 — certified quantum-assisted selection

- Objective: wᵢ = pᵢvᵢ − cᵢ; maximize Σwᵢxᵢ subject to Σxᵢ = 6, Σcᵢxᵢ ≤ 25, Σhᵢxᵢ ≤ 22.
- Penalties: exact_K = budget = capacity = 500, normalized before phase application.
- QAOA: 10 qubits, 2 layers, logical depth 5, ops rx=20 / ry=10 / diagonal=2, 8192 shots.
- QAOA feasible rate 0.681396484375; best feasible bitstring 1100101110; raw objective 40.73970788738256.
- Exact certificate bitstring 1110000111; selected C0059, C0170, C0256, C0327, C0372, C0374.
- Business: expected conversions 2.286974, deposit value 56.787439, cost 11, net/cost 4.162494.
- Fresh-clone reproduction: full `src/run_benchmark.py` + `src/make_report.py` run verified; 10 result/metadata files byte-identical; canonical summary exact with timing fields normalized.
- CSV/JSON parity: same six IDs, exact objective, QAOA diagnostics, optimized parameters, measurement counts, and brute-force certificate.

### Phase 4 — Stage 3 — six-qubit conversion simulation

- Mapping: q0 C0170, q1 C0256, q2 C0327, q3 C0374, q4 C0059, q5 C0372 (`c5…c0`, `q0` rightmost).
- RY angles: 1.473820, 1.440338, 1.406325, 1.224886, 1.221330, 1.208998.
- Exact 0.4164131424084104; ideal statevector 0.4164131424084103; Aer finite-shot 0.420379638671875.
- Monte Carlo 0.415130615234375; noisy 0.43133544921875; mitigated 0.41239821154870004; NNLS 0.4111108154155694.
- Noise: depolarizing 0.02, symmetric readout 0.03; mitigation = noise-model-aware marginal inversion with 64×64 NNLS cross-check (73.0944% error reduction).
- Shots: 32768 noiseless + 32768 noisy; 95% half-width 0.005337600548893514.
- Fresh-clone reproduction: full `src/run_benchmark.py` + `src/make_report.py` run verified; 10 result/metadata files byte-identical; canonical summary exact with timing fields normalized.
- CSV/JSON parity: same qubit mapping, RY angles, probabilities, errors, noise model, and 64-bin count dictionaries.

### Phase 5 — End-to-end integration, 30-metric benchmark & validation

- 30 metric rows: 14 `Stage 1 …` rows (10 core OOF/decile + 4 supporting), 6 `Stage 2 …` rows (5 core + raw QAOA gap), 8 `Stage 3 …` rows, 1 ROI row, and 1 reproducibility row = 30 rows; 30/30 engineering gates passed.
- Reproducibility checks: 10/10, score 100.0.
- Runtime: 145.9735211939999 s (`145.9735 s` in `results/benchmark_report.md` and byte-identical `docs/04_TECHNICAL_REPORT.md`).
- Conservative readiness estimate: 89/100 (quantum 33/35, accuracy 26/30, reproducibility 20/20, communication 10/15); planning figure, not an official judge score.
- Known constraints: hidden labels unknown, wide PR-AUC CI, QSVC weak ranker, nonzero raw QAOA gap, synthetic noise, no quantum-advantage claim.
- Fresh-clone reproduction: full `src/run_benchmark.py` + `src/make_report.py` run verified; 10 result/metadata files byte-identical; canonical summary exact with timing fields normalized.

### Phase 6 — Technical communication, evidence pack & submission handoff

- Project name: CertiQ-Chirp: Certified Quantum Campaign Intelligence (53 chars).
- Pitch: “CertiQ-Chirp turns quantum components into an auditable banking decision: calibrated predictions, certified QAOA selection, and a six-qubit conversion check.” (157 chars).
- Submitted Pr(K ≥ 3): 0.420; exact analytical: 0.4164131424084104.
- Expected net value 45.7874; budget 11/25; capacity 16/22; net/cost 4.1625×; 22/22 exact-value narrative checks PASS.
- External evidence set: 21 SVG diagrams, 2400 px / 1600 px PNG exports, 21 branded 1600×900 gallery plates, thumbnails, logos, hero, social card, icons (excluded from lean repo by `.gitignore`).
- External PDF set: 24-page dossier, 22-page diagram atlas, 12-slide deck, 1-page judge one-pager, 5-page media catalog (`data/reference/PROBLEM_STATEMENT_THE_ATOMIQ_HACKTHON.pdf` preserved).
- Report regeneration: `python src/make_report.py` byte-identical across `results/benchmark_report.md`, `docs/04_TECHNICAL_REPORT.md`, and `docs/BENCHMARK_README.md`.

## 16. End-to-end completion record

| Field | Value |
|---|---|
| Status | ✅ Completed |
| Execution | Single-agent, end to end, without splitting Phase 0 across workstreams |
| Completed | 2026-11-11 · IST |
| Sub-phases | 5 / 5 completed |
| Full report | [phase_0_completion.md](phase_0_completion.md) |
| Phase gate | PASS — source hierarchy, normalized spec, identity/domain, success philosophy, and plan control all validated |
| Downstream handoff | All Phases 1–6 are ✅ Completed against the locked charter across `plan.md`, `docs/`, and `results/` |

The completion report records the actions, exact validation checks, source hierarchy, challenge digest, locked identity, global gates, and sign-off for every Phase 0 sub-phase.

---

Back to [master plan](plan.md) · [Plan README](README.md) · [Tracker](TRACKER.csv)
