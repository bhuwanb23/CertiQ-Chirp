# Devpost submission — copy/paste text

> Replace only the bracketed team/link fields. Do not leave square brackets in the final submission. The short values are in code blocks for clean copying. The **About the project** section is raw Markdown, ready to paste directly into Devpost.

---

## General info

### Project name — 53/60 characters

```text
CertiQ-Chirp: Certified Quantum Campaign Intelligence
```

### Elevator pitch — 157/200 characters

```text
CertiQ-Chirp turns quantum components into an auditable banking decision: calibrated predictions, certified QAOA selection, and a six-qubit conversion check.
```

---

## Project Story

### About the project — paste everything from the next heading onward

## Inspiration

IBM’s decade of cloud-accessible quantum computing gave this hackathon its “Chi(r)ps” theme, but the challenge we found most compelling was quieter and more practical: **a bank has to make one decision well**. Contacting every customer is wasteful; choosing only the most likely subscribers ignores contact cost, operational capacity, and the uncertainty that flows from prediction into action.

We were inspired by the idea that quantum computing should be useful even when it is not magically faster. Instead of building three disconnected demos, we treated the problem as one auditable chain: a probability, a constrained decision, and a measurable outcome. That became **CertiQ-Chirp** — a hybrid system where the quantum methods have clear jobs, classical methods provide honest references, and every customer ID can be traced from the first prediction to the final campaign probability.

## What it does

CertiQ-Chirp answers the two questions the hackathon asks: **which six customers should the bank contact, and what is the probability that at least three of them subscribe?**

It does this in three connected stages:

1. **Predict.** We train on 300 labelled bank customers and produce a calibrated subscription probability $p_i$ for each of the 100 test customers. A Qiskit quantum kernel acts as a probability calibrator, while XGBoost supplies strong top-decile ranking. Their 60/40 fusion is selected only from out-of-fold training predictions.
2. **Select.** The ten highest-probability customers become candidates. For each candidate we compute expected net value
   $$w_i = p_i\,v_i - c_i,$$
   where $v_i$ is expected deposit value and $c_i$ is contact cost. We choose exactly six while satisfying
   $$\sum_i x_i = 6,\qquad \sum_i c_i x_i \le 25,\qquad \sum_i h_i x_i \le 22.$$
   A measured QAOA experiment explores this constrained space; hybrid repair and an exact brute-force certificate produce the final zero-gap decision.
3. **Simulate.** One qubit represents each selected customer. An $RY$ rotation with
   $$\theta_i = 2\arcsin\sqrt{p_i}$$
   prepares the correct subscription probability. Success is any measured bitstring with at least three ones, giving
   $$\Pr(K \ge 3).$$

The prototype’s concrete result is:

| Result | Value |
|---|---:|
| Six selected customers | `C0059, C0170, C0256, C0327, C0372, C0374` |
| Expected net value | `45.7874` |
| Budget used | `11 / 25` |
| Capacity used | `16 / 22` |
| Exact $\Pr(K\ge3)$ | `0.416413` |
| Qiskit Aer finite-shot estimate | `0.420380` |
| Expected conversions | `2.2870` |
| Expected net value per contact cost | `4.1625×` |

The same six probabilities are used in Stage 2 and Stage 3. Nothing is rounded, swapped, or manually repaired after ranking.

## How we built it

**Stage 1 — a ranker and a calibrator.** We ran repeated $3\times5$ stratified cross-validation on the training data only. All scaling, one-hot encoding, PCA, quantum feature angles, model fitting, and probability calibration were fitted inside each training fold. We benchmarked logistic regression, histogram gradient boosting, LightGBM, CatBoost, XGBoost, and a 4-qubit Qiskit `ZZFeatureMap` quantum-kernel SVC.

The results changed our design. The quantum kernel was a weak ranker, with ROC-AUC near 0.50, but it produced well-behaved probabilities. XGBoost had the best top-decile lift but was overconfident. A **40% XGBoost / 60% quantum-kernel fusion** preserved the useful ordering while improving Brier score, log loss, and expected calibration error. This is why we describe the quantum kernel as a *calibrator*, not as a superior classifier — and why we make no quantum-advantage claim.

**Stage 2 — measured quantum optimization with a certificate.** We built a 10-qubit warm-start, two-layer QAOA circuit with a diagonal cost Hamiltonian encoding the objective, the exact-six constraint, and one-sided budget/capacity penalties. The optimizer used 8,192 sampled bitstrings. We report the raw QAOA result transparently: it reached objective `40.7397`, a gap of `5.0477` to the exact optimum. Measured states then became warm starts for a one-swap hybrid repair, and all $\binom{10}{6}=210$ six-customer subsets were brute-force checked. The certified final objective is `45.7874`, with an optimality gap of exactly `0`.

**Stage 3 — a six-qubit Bernoulli ledger.** We built a six-qubit product-state circuit, checked Qiskit’s little-endian bit ordering, and compared five views of the same quantity: ideal statevector, noiseless Aer sampling, an exact 64-outcome Poisson-binomial calculation, NumPy Monte Carlo, and a synthetic-noise Aer run with depolarizing and readout errors. We also applied noise-model-aware marginal mitigation and a full $64\times64$ response-matrix cross-check.

| Stage 3 view | $\Pr(K\ge3)$ |
|---|---:|
| Exact analytical / ideal statevector | `0.416413` |
| Noiseless Qiskit Aer, 32,768 shots | `0.420380` |
| Monte Carlo, 32,768 samples | `0.415131` |
| Noisy Aer, 32,768 shots | `0.431335` |
| Mitigated | `0.412398` |

The finite-shot error is `0.003966`, inside the reported 95% half-width of `0.005338`. Mitigation reduced synthetic-noise error by about **73%**.

**Reproducibility.** One runnable Python script regenerates the predictions, result files, measurement counts, benchmark metrics, and technical report. Seeds, package versions, circuit parameters, penalty weights, noise settings, and full count dictionaries are committed. The three root-level deliverables are provided in both CSV and JSON form.

## Challenges we ran into

- **A small, imbalanced dataset.** Only 35 of 300 training customers subscribed. Accuracy would have been misleading, so we concentrated on PR-AUC, Precision@10, Recall@10, Brier score, log loss, and calibration.
- **Hidden test labels.** We could not tune against the 100 test outcomes. Every model, fusion weight, and preprocessing step was selected with out-of-fold training predictions only; the test set was predicted once after the pipeline was frozen.
- **Ranking versus calibration.** The model that ranked customers best was not the model that produced the most trustworthy probabilities. The quantum kernel was nearly random as a ranker but unusually well calibrated. Solving that tension became the core idea.
- **QAOA constraints.** Large penalties guarantee feasibility but make optimization poorly conditioned. Our raw quantum sampler found feasible solutions often, but not the exact optimum. We chose to disclose that gap and add an explicit hybrid certificate rather than hide behind a post-selected best run.
- **Qiskit bit order and noise.** A reversed bit string can silently change customer-to-qubit traceability. We documented the `c5…c0` convention, verified the ideal statevector against the analytical tail, and reported unmitigated and mitigated results side by side.
- **Honest quantum positioning.** The most difficult communication challenge was resisting hype. Quantum components are genuinely used in all three stages, but the exact classical references are what make the result trustworthy.

## Accomplishments that we're proud of

- Built one integrated pipeline rather than three isolated notebooks.
- Achieved out-of-fold **PR-AUC 0.2347**, **Brier 0.1036**, **log loss 0.3609**, **Precision@10% 0.3000**, **Recall@10% 0.2571**, and **2.5714× top-decile lift** with the final hybrid model.
- Improved calibration dramatically over the best classical ranker: ECE fell from `0.0877` to `0.0357`.
- Produced a feasible, exactly certified six-customer selection with **zero optimality gap**.
- Verified Stage 3 against four independent references and reduced synthetic-noise error by about 73% through mitigation.
- Benchmarked the idea across **30 metrics**, passed **30/30 transparent prototype gates**, and retained a 100% reproducibility checklist covering seeds, versions, result files, license, exact references, and full measurement counts.
- Kept a clear quantum/classical boundary: Qiskit kernel, QAOA, and six-qubit sampling are quantum; XGBoost/CatBoost baselines, brute force, Poisson-binomial arithmetic, and Monte Carlo are classical.

## What we learned

The biggest lesson is that **calibration is part of the business decision**, not a cosmetic final step. Stage 1 probabilities determine the ranking, the expected net value, the selected IDs, and the final conversion probability. A small calibration improvement propagates through the entire pipeline.

We also learned that a “weaker” quantum model can still be valuable. The quantum kernel did not win the ranking contest, but its probability geometry made the hybrid system more reliable. That is a more defensible quantum contribution than claiming an advantage the data cannot support.

Finally, exact references made the project stronger, not weaker. Brute force over 210 subsets and a 64-outcome Poisson-binomial calculation are tiny classical computations, yet they turn quantum outputs into auditable results. We would rather show a raw QAOA gap and a certified correction than present a mysterious perfect number.

## What's next for CertiQ-Chirp

- Run the Stage 2 and Stage 3 circuits on a real IBM Quantum backend and replace the synthetic noise model with calibrated device noise.
- Compare a standard slack-variable QUBO against our diagonal-oracle QAOA, including logical/physical qubit counts and transpilation overhead.
- Add amplitude estimation or a tailored constrained mixer to reduce shot noise and improve the raw quantum optimizer gap.
- Quantify probability uncertainty with bootstrapped models, then report how often each customer enters the optimal six and how $\Pr(K\ge3)$ varies.
- Build a small campaign dashboard where a bank can change budget, capacity, and contact cost and immediately see the certified decision change.
- Validate calibration drift over time before any production use; this prototype is a decision-support experiment, not a deployed banking model.

---

## Built with

Add as separate tags:

```text
Python, Qiskit, Qiskit Aer, ZZFeatureMap, Quantum Kernel, Support Vector Machines, Hybrid Quantum-Classical, QAOA, QUBO, Quantum Optimization, Statevector Simulator, Noise Model, Error Mitigation, Monte Carlo Simulation, XGBoost, CatBoost, LightGBM, scikit-learn, pandas, NumPy, SciPy, Model Calibration, Fintech, Targeted Marketing, Reproducible Research
```

---

## Additional info

### Upload a File

Upload the generated **`atomiq_submission_upload.zip`** from the workspace. It contains the runnable code, pinned dependencies, seeds, license, technical report, three root-level result files, full JSON diagnostics, and the source workbook.

### Team Name

```text
[YOUR OFFICIAL TEAM NAME OR FULL NAME IF SOLO]
```

### Full Names of All Team Members

```text
[Full Name 1, Full Name 2, Full Name 3]
```

### Team Member Emails

```text
[registered-email-1, registered-email-2, registered-email-3]
```

### Team Member Discord Usernames

```text
[discord-handle-1, discord-handle-2, discord-handle-3]
```

### PROJECT DELIVERABLE — Stage 2: Six Selected Customer IDs

```text
C0059, C0170, C0256, C0327, C0372, C0374
```

### PROJECT DELIVERABLE — Stage 3: Estimated Conversion Probability

```text
0.420
```

This is the Qiskit Aer noiseless finite-shot estimate, full precision `0.420379638671875`. The exact analytical and ideal statevector reference is `0.4164131424084104`; the absolute finite-shot difference is `0.003966`.

### Quantum Framework & Backend Used

```text
Qiskit 2.6.2 and Qiskit Aer 0.18.2; qiskit.quantum_info.Statevector for the 4-qubit ZZFeatureMap quantum kernel, 10-qubit QAOA optimization, and ideal Stage 3; custom DiagonalGate cost oracle for QAOA; AerSimulator for noiseless and synthetic-noise six-qubit measurements. All results are reproducible statevector/Aer simulations; no physical QPU was used.
```

### Circuit & Transpilation Metrics (Stage 2 & 3)

```text
Stage 1 kernel: 4 logical qubits, 1 ZZFeatureMap repetition, transpiled depth 17, 14 single-qubit u gates, 12 CX gates, 0 SWAPs, shot-free statevector kernel.
Stage 2 QAOA: 10 simulated logical/physical qubits, 2 layers, logical depth 5 (10 RY + 20 RX + 2 diagonal cost layers), u/cx-transpiled depth 4006, 2072 single-qubit u gates, 2044 CX gates, 0 SWAPs, 8192 sampled bitstrings.
Stage 3: 6 simulated logical/physical qubits, logical/transpiled depth 1/1, 6 single-qubit RY/u gates, 0 two-qubit gates, 0 SWAPs, 32768 noiseless shots plus 32768 noisy shots.
Total sampled shots: 73728. Ideal statevector and quantum-kernel calculations are shot-free.
```

### Presentation Slides URL

```text
[PASTE VIEW-ONLY DECK URL — ANYONE WITH THE LINK CAN VIEW]
```

### GitHub Repository URL

```text
[PASTE PUBLIC GITHUB REPOSITORY URL]
```

### Supplementary Materials & Large Files (Optional Drive / Cloud Link)

```text
[OPTIONAL PUBLIC VIEW-ONLY DRIVE/CLOUD FOLDER URL]
```

---

## Final warning before clicking Submit

- Replace every bracketed placeholder.
- Make the GitHub repository **Public**.
- Make the deck and supplementary links **Anyone with the link can view**.
- Ensure the repository contains `stage1_predictions.csv`, `stage2_selection.csv`, and `stage3_simulation.csv` at the root.
- Confirm the six IDs and `0.420` match the result files.
- Submit before the hard deadline: **11 November 2026, 10:00 PM IST**.
