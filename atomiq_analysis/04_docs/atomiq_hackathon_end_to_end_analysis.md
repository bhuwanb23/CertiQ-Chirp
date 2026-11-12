# The Atomiq Hackathon — End-to-End Analysis

**Event:** The Atomiq Hackathon | Qiskit Fall Fest 2026 at IEM  
**Theme:** *Chi(r)ps: A Decade of Harmony on the Cloud*  
**Audit time:** 11 November 2026, about 14:03 UTC / 19:33 IST  
**Status at audit:** Devpost’s calendar confirms a hard deadline of **22:00 IST on 11 Nov 2026** (16:30 UTC / 11:30 AM EST), roughly **2 hours 26 minutes** after this audit.

---

## 1. Executive verdict

The public-facing language makes this look like a broad, creative quantum hackathon with QML, generative art, optimization, games, and open-source tooling. **The released problem statement is much narrower and more prescriptive:** it is one connected, three-stage fintech campaign problem.

Your final answers are:

1. **Six customer IDs** to contact; and
2. **Pr(K ≥ 3)** — the probability that at least three of those six subscribe.

The intended pipeline is:

```text
300 labelled customers
  → Stage 1: calibrated subscription probabilities for 100 hidden-label customers
  → rank by probability; top 10 candidates
  → Stage 2: quantum/hybrid constrained binary optimization; choose exactly 6
  → Stage 3: six-qubit product-state circuit; estimate probability of ≥3 successes
  → compare every quantum result with exact classical references
```

There is **no single official set of six IDs**. The correct selection and final probability depend on the Stage 1 probabilities your own pipeline produces. The judges recompute the exact Stage 2 optimum and exact Stage 3 probability *from your submitted probabilities*, while evaluating Stage 1 against hidden test labels.

The highest-value strategy is therefore not a flashy standalone quantum demo. It is a **leakage-free, calibrated, fully traceable pipeline** in which the same continuous probabilities flow through all three stages, with honest classical baselines and exact validation.

---

## 2. Sources checked and source priority

### Primary pages and files checked

| Source | What it supplied |
|---|---|
| [Devpost overview](https://atomiq-hackathon-qff-26-iem.devpost.com/) | Narrative, prizes, judges, full submission list, video requirement, custom form fields |
| [Devpost rules](https://atomiq-hackathon-qff-26-iem.devpost.com/rules) | Dates, eligibility, required artifacts, scoring, integrity rules |
| [Devpost resources](https://atomiq-hackathon-qff-26-iem.devpost.com/resources) | Recommended SDKs, learning links, contacts |
| [Devpost schedule](https://atomiq-hackathon-qff-26-iem.devpost.com/details/dates) | Submission, judging, and winner windows |
| [Devpost calendar ICS](https://atomiq-hackathon-qff-26-iem.devpost.com/calendar) | Machine-readable confirmation of 22:00 IST deadline |
| [Devpost updates](https://atomiq-hackathon-qff-26-iem.devpost.com/updates) | No announcements posted |
| [Devpost discussions](https://atomiq-hackathon-qff-26-iem.devpost.com/forum_topics) | No discussion topics posted |
| [Devpost project gallery](https://atomiq-hackathon-qff-26-iem.devpost.com/project-gallery) | Gallery not yet published |
| [Official QFF website](https://qff-26-iem.vercel.app/) | Three-day fest, six tracks, full Day 1–3 programme, team/FAQ |
| [Google Drive resource folder](https://drive.google.com/drive/folders/1vjIM7mD7XjUjvfotAXF4uVfE2cYTS7Sp?usp=sharing) | Two files: the four-page technical PDF and the five-sheet XLSX dataset |
| [Registration form](https://forms.gle/LuS4ryGyBtPfTfBx5) | Form is currently closed |
| [IBM Quantum Learning](https://learning.quantum.ibm.com/) and [Qiskit docs](https://docs.quantum.ibm.com/) | Recommended learning resources |
| [Discord invite](https://discord.gg/2Z535c8UNv) | Mentorship/team-matching channel |

The two Drive files were downloaded into this workspace as:

- `PROBLEM_STATEMENT_THE_ATOMIQ_HACKTHON.pdf`
- `bank_campaign_participant_release.xlsx`

### Recommended hierarchy when pages disagree

1. **Technical problem statement PDF + workbook** for the actual task, formulas, data, and constraints.
2. **Devpost Rules** for dates, eligibility, submission requirements, and judging.
3. **Devpost Overview** for prizes, video demo, and custom form fields.
4. **Official QFF website** for the broader festival and context; some of it is stale pre-launch marketing.
5. **Google Form** for current registration status.

Where eligibility, registration, or a required artifact conflicts, email `qiskitfallfest26iem@gmail.com` and ask on Discord before relying on an interpretation.

---

## 3. Event identity, organizers, and theme

- **Host:** Centre of Excellence for Quantum Computing / QuantCom at Institute of Engineering & Management (IEM), Kolkata.
- **Collaboration/sponsor:** IBM Quantum.
- **Broader festival:** Qiskit Fall Fest 2026 at IEM, 9–11 November 2026.
- **Hackathon:** a 24-hour, public, online, free virtual sprint from 10:00 PM IST on 10 Nov to 10:00 PM IST on 11 Nov.
- **Devpost participant count:** 129 at the time of audit; names require login.
- **Team size:** 1–3 people; cross-university, cross-department, and mixed academic/industry teams are allowed by the detailed rules.
- **Mode:** external participants are virtual; on-site Day 1 workshops are reserved for IEM/UEM affiliates.
- **Prerequisites:** basic Python and a laptop; the website says prior quantum mechanics is not required.

### Theme

The “Chi(r)ps” name is a chip/chirp pun. According to the organizers, IBM quantum processors are named after birds and require precision tuning like acoustic chirps; 2026 marks ten years of cloud-accessible IBM quantum computing, 2016–2026. “Qreativity” frames superposition, interference, collapse, and NISQ noise as creative material rather than merely errors to suppress.

**Important:** the broad creative framing is not what the released rubric scores. The four advertised focus areas are:

1. Quantum Machine Learning
2. Qreative Quantum & Generative Algorithms
3. Algorithms & Optimization
4. Open Quantum Innovation

But the actual PDF specifies **one fintech/targeted-marketing pipeline**, and all 100 judging points are tied to its quantum rigor, accuracy, reproducibility, and communication. Creative presentation can help the narrative; it cannot replace the required three stages.

### Organizers and contacts

- Lead organizer: **Asmita Ghorai** — +91 83359 89812
- Co-organizers: **Arna Roy** — +91 91630 25296; **Tousif Aman Halder** — +91 82405 88201; **Sormista Pal** — +91 9064567630
- Faculty convenors: **Dr. Moutushi Singh**, **Dr. Prithwineel Paul**
- Email: `qiskitfallfest26iem@gmail.com`
- Community: official Discord, [LinkedIn](https://www.linkedin.com/company/qiskit-fall-fest-2026-iem), [Instagram](https://www.instagram.com/qiskitfallfestiem)

---

## 4. Complete timeline

All detailed rules use **IST (UTC+5:30)**. Devpost’s schedule displays the equivalent times in EST; they are consistent.

| Phase | IST | UTC | EST | Notes |
|---|---:|---:|---:|---|
| Registration opens | “Live now” | — | — | Exact opening date not stated |
| Registration closes | 8 Nov 2026, 23:59 | 18:29 | 13:29 | Google Form now says closed |
| Submissions open / sprint begins | 10 Nov, 22:00 | 16:30 | 11:30 AM | Problem statement was released shortly before this |
| **Hard submission deadline** | **11 Nov, 22:00** | **16:30** | **11:30 AM** | Single Devpost submission per team |
| Judging begins | 11 Nov, 22:30 | 17:00 | 12:00 PM | 30 minutes after submissions close |
| Judging ends | 14 Nov, 22:30 | 17:00 | 12:00 PM | Three-day evaluation window |
| Winners / Top 10 showcase | 15 Nov | — | — | Devpost calendar says 7:30 AM EST = 18:00 IST |

### Broader QFF programme

**Day 1 — 9 Nov, in person at IEM (IEM/UEM affiliates):**

- 10:00 reporting; 10:30–11:00 inauguration
- 11:00–13:00 Quantum Introduction + Qiskit 101 — Dr. Kavitha Yogaraj
- 13:00–14:00 networking lunch
- 14:00–15:00 Transpilation — Dr. Ritajit Majumdar
- 15:30–16:30 Quantum Machine Learning — Amitava Chakraborty
- 16:30–17:00 quiz/happy hour

**Day 2 — 10 Nov, virtual:**

- 19:00–21:00 Hardware–Software Interface — Dr. Subrata Chakraborty, covering transmon physics, noise, pulse control, heavy-hex topology, and hardware-aware transpilation
- 21:00–21:30 networking
- 21:30–22:00 hackathon kickoff and problem release
- 22:00 sprint begins

**Day 3 — 11 Nov, virtual:**

- Hackathon runs until 22:00
- 22:00–22:30 closing quiz
- Post-event: Top 3 announced and Top 10 leaderboard/spotlights on 15 Nov

The official website advertises **3 days, 6 tracks, 100+ attendees**. The six tracks are Workshops, QML, Hackathon, Expert Talks, Hardware, and Qiskit 1.0.

---

## 5. Eligibility and registration — the largest administrative risk

The sources materially disagree.

| Source | Eligibility statement |
|---|---|
| Devpost sidebar widget | Above legal age of majority; **students only**; companies/professional organizations excluded; specific countries/territories excluded. The tooltip appears to name the Democratic People’s Republic of Korea. |
| Devpost “At a Glance” | **Open to all**: UG/PG students, academic researchers, and industry professionals worldwide |
| Detailed Devpost Rules | Open globally to UG/graduate students, researchers, PhD scholars, faculty, independent developers, and industry professionals; subject to U.S. export/OFAC compliance; void where prohibited |
| Official website | “Open to all students and researchers”; Day 1 in person restricted to IEM/UEM; virtual Days 2–3 open to all |

The detailed rules are broader, but the structured Devpost eligibility widget may still be enforced by the platform. A professional participant should obtain written clarification. “Companies/professional organizations excluded” may mean an organization cannot enter as an entity, which is not necessarily the same as banning individual industry professionals.

### Mandatory Google Form

Both the detailed rules and the website say **Devpost handles submissions, but prior registration through the official Google Form is mandatory for team eligibility and awards**. At audit time that form says:

> “Registrations … are now officially closed.”

The rules give a registration deadline of 8 Nov 2026, 23:59 IST. If a team did not complete the form before closure, a technically excellent Devpost submission may still be ineligible for awards. This should be confirmed with the organizers immediately.

### Other eligibility facts

- 1–3 members; solo entrants use their full name as team name.
- Teams may span institutions and departments.
- Virtual participation is worldwide.
- Day 1 on-site activities are only for IEM/UEM affiliates.
- Free to enter.
- All submitted projects are publicly displayed in the Devpost gallery according to the rules, though the gallery was unpublished at audit time.

No official Updates post, discussion topic, or clarification resolving these conflicts exists.

---

## 6. Prizes, judge, and recognition

### Cash and non-cash prizes

| Place | Cash | Other recognition |
|---|---:|---|
| 1st — Atomiq Champion | ₹5,000 | IBM Quantum certificate, verifiable Certifier badge, digital sticker bundle, social/community spotlight |
| 2nd — Atomiq Supercharger | ₹3,000 | Same package |
| 3rd — Atomiq Entangler | ₹2,000 | Same package plus public leaderboard feature |
| Top 10 Global Finalists | — | IBM Quantum certificate, Certifier badge, spotlight, public leaderboard |

- Total displayed cash pool: **₹10,000+**, with notes that amounts may increase as sponsorships are finalized.
- One winner is listed for each of the top three places; ten winners for the finalist category, apparently including the top three.
- The overview mentions Credly and Certifier digital credentials; prize copy names Certifier specifically.
- The detailed rules say official completion/participation certificates are available for eligible submissions meeting baseline technical requirements; the website ties completion certificates to workshop/lab criteria and active participation. This scope is ambiguous.
- A public leaderboard with final Top 10 scores/rankings is promised.

### Judge

- **Aniruddha Biswas**, Quantum Computing Research Engineer, LTM Research; the rules call him “Dr. Aniruddha Biswas.”
- The PDF also says judges verify results using hidden test labels and exact classical references. Only one judge is publicly listed.

---

## 7. The actual technical challenge

### Overview

A bank wants to target a term-deposit campaign. Contacting everyone is wasteful; selecting only the highest-probability customers ignores costs and capacity. The challenge is to combine prediction, constrained optimization, and quantum outcome simulation.

The three stages are deliberately linked. **The same Stage 1 probabilities must be used in Stages 2 and 3**, and prediction errors are expected to propagate.

### Stage 1 — Predict

**Input:** `Stage1_Train` with 300 labelled customers; `Stage1_Test` with 100 unlabelled customers.  
**Task:** predict a continuous probability in `[0,1]` for each of the 100 test customers.

Requirements:

- At least one **quantum or hybrid probabilistic classifier** — e.g. VQC, quantum kernel, or QNN.
- At least one **classical probabilistic baseline**.
- Use training data only for development and validation, e.g. stratified cross-validation.
- Fit all preprocessing, encoders, scalers, imputers, feature selectors, and probability calibration on training data only.
- Predict the test set once after the pipeline is final.
- Rank by descending predicted probability; ties are broken by **ascending alphanumeric `customer_id`**.
- The top 10 become Stage 2 candidates.
- Keep continuous probabilities, not hard labels.

The PDF says Stage 1 is evaluated using **ROC-AUC, PR-AUC, Precision@10, Recall@10, Brier score, log loss, and calibration**. Devpost’s criterion 2 explicitly lists PR-AUC, Precision@10, Recall@10, and Brier. Accuracy is not a main metric because the positive class is small.

The workbook says the full 400-customer sample contains 46 `yes` and 354 `no`, while the 300 training rows contain 35 `yes` and 265 `no`. By subtraction, the hidden test set contains **11 `yes` and 89 `no`**. Therefore the theoretical maximum Precision@10 is 1.0 and maximum Recall@10 is 10/11 ≈ 0.909. The exact split method is not documented, but these counts are consistent with stratification. Do not try to recover the hidden labels from the original public `bank.csv`; that would be test leakage and is expressly penalized.

### Stage 2 — Select

From the ten candidates, choose exactly six. For candidate `i`:

```text
p_i = Stage 1 predicted probability
v_i = expected_deposit_value
c_i = contact_cost
h_i = capacity_units

w_i = p_i * v_i - c_i          (expected net value)
Z(x) = Σ w_i x_i               (maximize)
```

Subject to:

```text
x_i ∈ {0,1}
Σ x_i = 6
Σ c_i x_i ≤ 25
Σ h_i x_i ≤ 22
```

Use a quantum/hybrid binary optimizer such as QAOA or SamplingVQE, or another justified quantum method. Explain QUBO/Ising mapping, penalty weights, auxiliary/slack variables, optimized parameters, measured bitstrings, decoding, and comparison with an exact brute-force classical optimum.

There are only `C(10,6) = 210` six-customer subsets, so exact classical verification is trivial.

A valid selection must contain exactly six unique IDs, all from **your own** top 10, and satisfy both resource limits. An invalid selection receives no feasibility or objective credit.

### Stage 3 — Simulate

For the six selected customers, estimate:

```text
Pr(K ≥ 3), where K = number of the six who subscribe
```

Assume independent responses. Use **one qubit per customer** whose probability of measuring `1` equals that customer’s Stage 1 probability.

A minimal correct circuit is a six-qubit product state:

```text
RY(θ_i) on qubit i, with θ_i = 2 arcsin(sqrt(p_i))
then measure all six qubits
```

because `Pr(1) = sin²(θ_i/2) = p_i`.

A measured bitstring succeeds when its Hamming weight is at least 3. Qiskit’s bit ordering must be handled explicitly: `q0` generally appears at the right end of a printed classical bitstring, so state the customer-to-qubit mapping and whether bits were reversed.

The exact reference is the Poisson-binomial tail:

```text
P_exact = Σ over b ∈ {0,1}⁶ with popcount(b) ≥ 3
          ∏ p_i^{b_i} (1-p_i)^{1-b_i}
```

Only 64 bitstrings need to be enumerated; dynamic programming is an alternative. No entanglement or two-qubit gates are required for this ideal logical circuit because responses are independent.

The quantum estimate is:

```text
P_quantum = successful_shots / total_shots
```

Its finite-shot standard error is approximately `sqrt(P(1-P)/shots)`. For example, at 8,192 shots and P≈0.5, the 95% statistical interval is roughly ±0.011. Report a Monte Carlo benchmark, the exact analytical value, all bitstring counts, absolute errors, and confidence intervals.

The Devpost form’s “P ≥ 3” notation is malformed shorthand. It means **Pr(K ≥ 3)**, a decimal in `[0.000, 1.000]`, not a probability greater than three.

---

## 8. Workbook forensics and data findings

`bank_campaign_participant_release.xlsx` has five visible sheets, no hidden sheets, no formulas, no hidden columns/rows, and no solved answers.

| Sheet | Rows × columns | Contents |
|---|---:|---|
| `README` | 20 data rows × 2 | Field descriptions, formulas, constraints, seeds |
| `Stage1_Train` | 300 × 17 | 16 features plus `y` |
| `Stage1_Test` | 100 × 16 | Features only |
| `Stage2_Data` | 400 × 5 | Operational inputs for all 400 customers |
| `Stage2_Constraints` | 6 × 4 | N, K, budget, capacity, objective |

### Data quality and structure

- IDs are unique, zero-padded `C0001`–`C0400`.
- Train and test IDs are disjoint; their union equals all 400 Stage 2 IDs.
- No null cells and no duplicate IDs.
- `Stage1_Train`: 265 `no`, 35 `yes`; inferred test: 89 `no`, 11 `yes`.
- `duration` was removed from the source `bank.csv`, avoiding information that would only be known after contacting a customer.
- Sampling seed = 42; train/test split seed = 42.
- Categorical “missingness” is represented by the literal string `unknown`:
  - Train: `job` 1, `education` 14, `contact` 91, `poutcome` 254.
  - Test: `education` 7, `contact` 35, `poutcome` 76.
- `pdays = -1` is a sentinel, not an ordinary numeric value.
- Numeric ranges include negative balances, `campaign` up to 50 in train, `previous` up to 22 in test, and skewed `balance`; scaling or robust transformations are appropriate.
- `Stage2_Data` contains all 400 customers, not only the 100 test customers as the PDF’s brief wording suggests. Join to the ten selected test IDs by exact `customer_id`.
- `customer_segment` has values A–D but is **not** part of the stated objective or constraints. Do not silently introduce a segment constraint.

### Operational data ranges

| Field | Range | Observation |
|---|---:|---|
| `contact_cost` | 1–4 | Any six customers cost at most 24 |
| `expected_deposit_value` | 12–30 | Used only through `p_i*v_i - c_i` |
| `capacity_units` | 1–4 | Any six use at most 24 |
| `w_i` for `p_i∈[0,1]` | −4 to 29 | Derived from workbook ranges |

Two useful analytical consequences:

1. **The budget constraint is mathematically redundant for this dataset:** six selections × maximum cost 4 = 24 ≤ 25. Still compute, report, and enforce it to satisfy compliance, but it cannot bind.
2. **Capacity can bind:** six × maximum capacity 4 = 24 > 22. A feasible six-subset needs at least two units of capacity “slack” relative to six customers of capacity 4 — for example, one customer with capacity ≤2 or two with capacity ≤3. A pathological top 10 consisting only of capacity-4 customers, or nine capacity-4 plus one capacity-3, would have no feasible six-subset. The rules forbid manually altering the top 10, so this is an edge-case design flaw; ask organizers if it occurs. With the observed capacity distribution, a typical model-derived top 10 should be feasible.

### Derived QUBO guidance

A conventional quadratic formulation is:

```text
minimize F = −Σ w_i x_i
             + λ_K (Σ x_i − 6)²
             + λ_C (Σ c_i x_i + s_C − 25)²
             + λ_H (Σ h_i x_i + s_H − 22)²
```

where `s_C` and `s_H` are nonnegative integer slacks represented by auxiliary binary variables. Five binary slack bits per inequality are enough (`0…31`), giving 10 selection qubits + 10 slack qubits = 20 logical qubits in a straightforward QAOA QUBO. A constrained XY mixer can enforce `Σx=6` natively and remove `λ_K`; a custom inequality handling or the redundancy of the budget constraint can also reduce the formulation.

Penalty coefficients must be large enough that any one-unit constraint residual costs more than the largest possible objective swing. Across all ten candidates, `w_i∈[−4,29]`, so the total reward range is at most `10×29 − (−10×4) = 330`; λ around 400 or greater is a conservative starting point, after normalizing all coefficients consistently. Excessively large penalties hurt QAOA conditioning, so validate by enumerating the penalized objective and checking that the lowest-energy bitstrings are feasible. Document the chosen λ values rather than claiming a generic “large penalty.”

The “optimality gap” is not given a precise normalization. Report both:

```text
absolute gap = Z_exact − Z_quantum
relative gap = (Z_exact − Z_quantum) / |Z_exact|   (if Z_exact ≠ 0)
```

and state tie-breaking if several exact optima exist.

---

## 9. Required deliverables

### Public GitHub repository

- Clean end-to-end notebooks/scripts for preprocessing, classical baselines, quantum/hybrid classifier, probability generation, Stage 2 QUBO/quantum optimizer, classical brute force, Stage 3 circuit, exact result, and Monte Carlo validation.
- `requirements.txt` or `environment.yml` with exact package versions.
- All random seeds: data split, model initialization/weights, optimizer, transpiler, simulator shots, and Monte Carlo.
- Open-source license such as MIT or Apache 2.0.
- Step-by-step local/cloud execution instructions.
- Public repository and public/view-only links for every external asset.

### Root-level result files

| File | Required content |
|---|---|
| `stage1_predictions.csv` | All 100 test customers: `customer_id`, continuous `predicted_probability`, `rank`, `is_top_10` |
| `stage2_selection.csv` or `.json` | Ten candidate IDs and inputs; exact six selected IDs; budget/capacity totals; objective; measured best bitstrings; classical brute-force optimum; optimality gap |
| `stage3_simulation.csv` or `.json` | Six IDs; customer-to-qubit order; six input probabilities; circuit parameters; measurement counts; quantum estimate of Pr(K≥3); exact analytical result; Monte Carlo result; error calculations |

JSON is usually easier for Stage 2 and 3 because bitstring counts, parameter vectors, and nested mappings do not fit naturally in one CSV row.

### README / technical report

Must cover:

- End-to-end architecture and methodology
- Hybrid classifier and validation strategy
- QUBO/Ising mapping, penalties, auxiliary variables, and decoder
- Stage 3 circuit topology, gate synthesis, and bit ordering
- Logical vs physical qubit mapping, original/transpiled depth, 1Q/2Q/SWAP counts, backend/simulator
- Classical vs quantum contributions and honest benchmark comparisons
- Ideal, noiseless finite-shot, and noisy results where applicable; unmitigated alongside any mitigated results
- Error propagation across all stages, limitations, and noise analysis
- Exact setup/reproduction commands and environment details
- Business impact, operational feasibility, and data-driven campaign recommendations
- No unsupported quantum-advantage claims

### Presentation and video

- **Deck:** public view-only Google Slides, Canva, or hosted PDF; architecture, mathematical formulation, quantum/classical boundary, error analysis, and conclusions.
- **Video:** the full Devpost overview adds a **1–2 minute public YouTube/Loom/open-Drive video**. It must connect all three stages, visually walk through circuits and optimizer execution, and confirm key metrics. The Rules page and PDF omit this, but one duplicated section of the overview explicitly says “What to Submit” and includes it. **Make the video anyway**; it is the safe interpretation.

### Devpost custom form fields

- Team name; comma-separated full names, registered emails, and active Discord handles.
- Exact six Stage 2 customer IDs.
- Final Stage 3 estimated probability `Pr(K≥3)` as a decimal between 0.000 and 1.000.
- Quantum architecture: SDKs, backends/simulators, logical/physical qubit counts, circuit depth, gate counts, and shot count.
- Compliance checkboxes: no test leakage; preprocessing fit on train only; Stage 2/3 directly consume Stage 1 outputs; continuous probability propagation; root-level result files; documented seeds.
- Optional public view-only supplementary folder for large circuit diagrams or assets.

### Public visibility

The rules say every submission is displayed publicly in the Devpost gallery. Treat all code, deck, video, and result files as public; do not include secrets or private personal data beyond the requested team contact details.

---

## 10. Judging rubric and what it really rewards

| Criterion | Weight | What earns points |
|---|---:|---|
| Quantum Rigor & Technical Depth | 35% | Genuine quantum/hybrid classifier; technically valid QUBO and constraint handling; correct six-qubit circuit; real SDK execution/simulation; rigorous classical comparisons |
| Result Accuracy & End-to-End Integration | 30% | Hidden-label Stage 1 ranking/calibration; feasible Stage 2 with small optimality gap; Stage 3 close to exact probability; ID traceability; error propagation |
| Code Quality & Reproducibility | 20% | Organization, modularity, dependencies, error handling, seeds, environment, easy rerun |
| Report, Presentation & Communication | 15% | Clear technical report/deck, quantum vs classical boundary, business interpretation, noise/limitations/errors |

### Strategic interpretation

- **35 + 20 = 55 points** are largely under your control: correctness, genuine quantum components, clean code, seeds, dependencies, and reproducibility.
- **30 points** depend heavily on calibrated probabilities and exact integration. A sophisticated but poorly calibrated QML model can damage all three stages.
- The hidden test labels and exact classical references mean the judges can independently recompute your Stage 1 metrics, Stage 2 optimum, and Stage 3 Poisson-binomial tail.
- Error propagation is explicitly scored. A strong submission can use training-set bootstrapping or CV ensembles to estimate uncertainty in `p_i`, then report how often each customer enters the optimal six and how Pr(K≥3) varies.
- “Quantum advantage” is not required and unsupported claims are penalized. The goal is a quantum/hybrid implementation that is technically honest and benchmarked.

### Explicit penalties

- Using test information during development: major penalty or disqualification.
- Infeasible Stage 2 selection: no feasibility or objective credit.
- Quantum circuit unrelated to the stated task: no quantum credit.
- Manually altering the top 10 or using different probabilities across stages violates the pipeline rules.

---

## 11. Recommended implementation blueprint

### Stage 1

1. Build a single scikit-learn `Pipeline`/`ColumnTransformer`:
   - one-hot encode categorical features, treating `unknown` as its own category;
   - scale numeric features, with `pdays=-1` handled explicitly if desired;
   - fit everything inside stratified CV folds.
2. Classical baselines: regularized logistic regression and a gradient-boosted or random-forest classifier, both calibrated with training-only CV (`CalibratedClassifierCV` or equivalent out-of-fold Platt/isotonic calibration).
3. Quantum/hybrid model: a small PCA/feature-selected quantum kernel + calibrated SVC, or a 4–8 qubit VQC/QNN. Fit PCA/scaling on training folds only.
4. Choose any ensemble weight using **out-of-fold training predictions**, never test predictions.
5. Report out-of-fold ROC-AUC, PR-AUC, Precision@10, Recall@10, Brier, log loss, and calibration; then freeze the pipeline and predict the 100 test rows once.
6. Rank deterministically and save `stage1_predictions.csv`.

A hybrid ensemble that includes the quantum model is safer than leaving the quantum classifier as an unused side experiment, because the task asks to predict with a quantum/hybrid classifier while also requiring a classical baseline.

### Stage 2

1. Join the ten IDs to `Stage2_Data`.
2. Compute `w_i = p_i*v_i - c_i` from the **same** probabilities.
3. Build and document the QUBO; validate penalty weights by enumeration.
4. Run QAOA/SamplingVQE with recorded parameters, shots, backend, and seed; rank measured bitstrings by penalized energy, decode selection/slack bits, and reject infeasible strings.
5. Brute-force all 210 six-subsets; report exact optimum and both gap definitions.
6. Save candidate inputs, bitstrings, parameters, totals, and IDs in `stage2_selection.json`.

### Stage 3

1. Map the six IDs to `q0…q5` explicitly.
2. Apply `RY(2*arcsin(sqrt(p_i)))`, measure all qubits, and record full counts.
3. Estimate Pr(K≥3) from Hamming weight ≥3, with an explicitly stated bit-order convention.
4. Compute the 64-outcome exact result and a seeded NumPy Monte Carlo result.
5. Report ideal statevector/noiseless finite-shot/noisy outcomes where applicable, plus unmitigated and any mitigated values.
6. Report logical/physical qubits, original/transpiled depth, 1Q/2Q/SWAP counts, shots, backend/noise model, and finite-shot confidence interval.

With no entangling gates, the ideal Stage 3 logical circuit has six single-qubit rotations and six measurements. Quantum credit comes from correctly implementing and sampling the quantum circuit, not from claiming computational advantage for a probability that can be calculated exactly on 64 outcomes.

---

## 12. Contradictions, stale copy, and ambiguities

| Issue | Conflict | Safe action |
|---|---|---|
| Eligibility | Devpost widget says students only; detailed rules and overview include researchers, faculty, developers, and industry professionals | Follow detailed rules but get written confirmation if any member is not a student |
| Registration | Website says “Registration is open now”; Google Form says closed; rules say 8 Nov deadline | Confirm prior registration before investing; it is mandatory for awards |
| Scope | Website says “8+ domains”; Devpost lists four creative focus areas; PDF gives one prescribed fintech pipeline | Build the three-stage fintech pipeline; use creativity in presentation only |
| Video | Included in one duplicated Devpost “What to Submit” section, omitted from Rules and PDF | Submit a 1–2 minute public video |
| Packaging | PDF allows “single zipped folder or repository link”; Devpost requires a public GitHub repository | Use a public GitHub repo; optionally also provide a zip in a public supplementary folder |
| Gallery | Rules say projects are publicly displayed upon submission; gallery page says unpublished | Assume eventual public display; keep all assets public-ready |
| Stage 2 dataset | PDF says operational inputs for 100 test customers; sheet has all 400 | Join by exact ID and use only your top 10 |
| “Deadline: October 2, 2026” | Appears visually near the hackathon section on the website | It is the **call-for-mentors** deadline, not the hackathon deadline |
| Certificates | Rules say all eligible baseline-compliant submissions; overview says completion/participation certificates; website adds workshop/lab criteria | Do not assume automatic certification; ask organizers |
| `P ≥ 3` | Written like an impossible probability ≥3 | Interpret as `Pr(K ≥ 3)`, decimal 0–1 |
| Judge naming | “Aniruddha Biswas” on overview, “Dr. Aniruddha Biswas” in rules | Same person; Quantum Computing Research Engineer, LTM Research |
| Result gap | “Optimality gap” is not mathematically defined | Report absolute and relative gap and define both |
| Slack/auxiliary variables | Required in discussion, but no exact formulation mandated | State encoding, bit weights, penalty values, and validation |
| No official clarifications | Updates and Discussions are empty | Email/Discord for any unresolved conflict |

Most inconsistencies appear to be **pre-launch marketing text that was not updated after the 10 November problem release**. The PDF, workbook, and Devpost Rules are internally much more specific and should control the technical work.

---

## 13. Final submission checklist

- [ ] Google Form registration/eligibility confirmed.
- [ ] Devpost hackathon joined and one team submission created.
- [ ] Public GitHub repo with MIT/Apache-2.0/equivalent license.
- [ ] `requirements.txt` or `environment.yml` with exact versions.
- [ ] All seeds and environment details committed.
- [ ] No preprocessing, calibration, feature selection, or tuning on test data.
- [ ] No reconstruction of hidden labels from the original `bank.csv`.
- [ ] At least one quantum/hybrid probabilistic classifier and one classical baseline.
- [ ] Out-of-fold Stage 1 metrics and calibration reported.
- [ ] `stage1_predictions.csv` at repository root: 100 rows, continuous probabilities, rank, top-10 flag, documented tie-break.
- [ ] `stage2_selection.json` at root: top 10, six IDs, inputs, objective, totals, bitstrings, quantum parameters, classical optimum, gaps.
- [ ] Selection feasible: six unique IDs, all from own top 10, budget ≤25, capacity ≤22.
- [ ] Same probabilities used in Stage 2 and Stage 3.
- [ ] `stage3_simulation.json` at root: qubit order, probabilities, RY angles/circuit parameters, counts, Pr(K≥3), exact value, MC value, errors, backend/specs.
- [ ] Ideal, finite-shot, noisy/unmitigated/mitigated results reported where applicable.
- [ ] Logical/physical qubits, original/transpiled depth, 1Q/2Q/SWAP counts, shots, and noise model reported for each relevant circuit.
- [ ] Detailed README with architecture, math, quantum/classical split, error propagation, limitations, business recommendations, and exact run commands.
- [ ] Public view-only deck.
- [ ] Public 1–2 minute video.
- [ ] Optional public supplementary folder.
- [ ] Devpost form: names/emails/Discord handles, six IDs, Pr(K≥3), quantum specs, compliance checkboxes.
- [ ] Every external link tested while logged out.
- [ ] Submitted well before 22:00 IST; the deadline is described as hard.

### Minimum sensible repository shape

```text
README.md
LICENSE
requirements.txt
config/seeds.json
stage1_predictions.csv
stage2_selection.json
stage3_simulation.json
notebooks/
  stage1_modeling.ipynb
  stage2_optimization.ipynb
  stage3_circuit.ipynb
src/
  preprocess.py
  stage1_models.py
  stage2_qubo.py
  stage3_circuit.py
  validate_pipeline.py
results/
  figures/
  logs/
```

---

## 14. If participating with only a few hours left

1. **First 5 minutes:** confirm Google Form registration and professional/student eligibility.
2. **First 45 minutes:** build a leakage-free classical baseline plus a small quantum kernel or VQC; select/calibrate the final hybrid model using training-fold CV only.
3. **Next 20 minutes:** freeze predictions, rank, save Stage 1, join Stage 2 data, and brute-force all 210 subsets.
4. **Next 30 minutes:** implement a documented QUBO and run a modest QAOA/SamplingVQE experiment; compare its best feasible bitstring with the exact optimum.
5. **Next 20 minutes:** implement the six-`RY` circuit, exact 64-outcome calculation, Monte Carlo, and finite-shot/noise reporting.
6. **Final 45–60 minutes:** write README, make deck/video, verify public links and root files, fill the form, and submit at least 30 minutes early.

Do not spend the remaining time on generative-art extras or unsupported quantum-advantage claims. The scoring is dominated by pipeline correctness, calibration, quantum rigor, exact benchmarks, and reproducibility.

---

## 15. Bottom line

This is a **single integrated hybrid quantum-classical decision pipeline**, not a free-form quantum art contest. The released data and problem statement require a calibrated probabilistic classifier, a constrained QUBO-style selection, and a six-qubit independent-Bernoulli simulation. The six IDs and final probability are model-dependent; judges verify them against hidden labels and exact calculations derived from the probabilities you submit.

The biggest nontechnical risks are the **closed mandatory registration form** and the **conflicting eligibility language**. The biggest technical risks are **test leakage, uncalibrated probabilities, broken traceability between stages, infeasible Stage 2 output, bit-order errors, and missing reproducibility evidence**. Resolve those first, and the quantum components can remain small, exact, and defensible.
