# Technical Challenge Specification (extracted text)

Source: `PROBLEM_STATEMENT_THE_ATOMIQ_HACKTHON.pdf` in the official [Google Drive resource folder](https://drive.google.com/drive/folders/1vjIM7mD7XjUjvfotAXF4uVfE2cYTS7Sp?usp=sharing). Extracted from the four-page PDF. Formatting normalized to Markdown.

---

## Hybrid Quantum-Classical Term Deposit Campaign Pipeline

### 1. Overview

A bank wants to run a targeted term-deposit campaign. Contacting every customer is wasteful, and simply picking the most likely customers ignores costs and limits. Your team will build a hybrid quantum-classical pipeline that predicts who is likely to subscribe, chooses which customers to contact within set limits, and estimates the chance that the campaign reaches its conversion target.

Your final answer: six customers to contact, and the probability that at least three of them subscribe.

### 2. Challenge at a Glance

**Stage 1 – Predict.** Train on 300 labeled customers and predict a subscription probability for each of 100 test customers. The 10 highest-probability customers move on.

**Stage 2 – Select.** From those 10, choose exactly six that maximize expected net value within the budget and capacity limits, using a quantum or hybrid optimizer.

**Stage 3 – Simulate.** For your six customers, build a quantum circuit that estimates the probability that at least three subscribe.

The stages are linked. Stages 2 and 3 use your own Stage 1 probabilities, so prediction errors carry forward. This is intentional: judges reward teams that treat the work as one connected system.

### 3. Data Provided

- README: field descriptions, constraints, and file formats.
- Stage1_Train: 300 customers with features and the subscription outcome (`y`).
- Stage1_Test: 100 customers with features only. Outcomes are hidden.
- Stage2_Data: operational inputs for the 100 test customers, such as expected deposit value, contact cost, and capacity requirement.
- Stage2_Constraints: candidate pool size (10), exact number to select (6), budget limit, and capacity limit.

### 4. Stage 1: Subscription Prediction

Task: predict the probability that each test customer subscribes, then keep the 10 customers with the highest probabilities.

Build at least one quantum or hybrid probabilistic classifier (for example, a variational quantum classifier, a quantum kernel classifier, or a quantum neural network) and one classical probabilistic baseline.

Develop and validate using the training data only, for example with stratified cross-validation. Fit all preprocessing and any probability calibration on training data only.

Predict the 100 test customers once, after your pipeline is final. Keep continuous probabilities, not just yes/no labels.

Rank test customers from highest to lowest probability. Break ties by placing the lower customer_id first. The top 10 are your Stage 2 candidates.

How it is judged: ROC-AUC, PR-AUC, Precision@10, Recall@10, and probability quality (Brier score, log loss, calibration). Accuracy is not a main metric because only a small share of customers subscribe.

### 5. Stage 2: Constrained Customer Selection

Task: from your 10 candidates, select exactly six customers to contact. Maximize the total expected net value (based on each customer's subscription probability, expected deposit value, and contact cost) while staying within the budget and capacity limits.

Formulate the selection as a binary optimization problem that a quantum or hybrid solver can run (for example QAOA, SamplingVQE, or another justified method).

Explain how you enforced the constraints, including any penalty design and auxiliary variables. Report the optimized parameters, measured bitstrings, and how you decoded them into a selection.

Compare your result with an exact classical solution. The problem is small enough to check by brute force.

A valid selection has exactly six unique customer IDs, all from your own top 10, and meets both the budget and capacity limits. Invalid selections receive no feasibility or objective credit.

### 6. Stage 3: Campaign Outcome Simulation

Task: using your six selected customers, estimate the probability that at least three of them subscribe.

Use one qubit per selected customer, prepared so that the chance of measuring 1 matches that customer's Stage 1 probability. Assume customers respond independently.

Count a measured outcome as a success when at least three qubits read 1. State your customer-to-qubit order and handle bit-ordering conventions correctly.

How Stage 3 is judged: against an exact calculation from the probabilities you submit.

### 7. Rules

- Do not use the test set to select features, tune thresholds, calibrate probabilities, or choose hyperparameters.
- Fit all preprocessing (encoders, scalers, imputers, feature selectors) on training data only.
- Use the same Stage 1 probabilities in Stages 2 and 3. Do not manually alter your top 10.
- Clearly separate your quantum contribution from the classical reference methods. Do not make unsupported quantum-advantage claims.
- Penalties: using test information during development carries a major penalty or disqualification. An infeasible Stage 2 selection earns no feasibility or objective points. A quantum circuit unrelated to the stated task earns no quantum credit.

### 8. Submission Guidelines

#### 8.1 What to submit

- Code and notebooks: runnable end to end, covering preprocessing, models, probability generation, the Stage 2 formulation and quantum optimizer, the classical benchmark, and the Stage 3 circuit with its exact and Monte Carlo validation.
- Stage 1 result file: for all 100 test customers, the customer_id, predicted probability, rank, and a top-10 flag.
- Stage 2 result file: the top 10 IDs with their inputs, your six selected IDs, budget and capacity totals, objective value, best bitstrings, the classical optimum, and the gap to it.
- Stage 3 result file: selected IDs, qubit order, the six probabilities, circuit parameters, measurement counts, your quantum estimate, the exact result, the Monte Carlo result, and the errors.
- Short technical report (README): approach, validation, constraint handling, results, error analysis, limitations, and a business recommendation.
- Presentation: a concise story that connects all three stages and shows what is quantum and what is classical.

Package everything as a single zipped folder or repository link, with the three result files at the top level and the README explaining how to run your code. Submit once per team before the deadline announced by the organizers. Send any questions during the event to the organizers through the channel announced at the start.

#### 8.2 Format and reproducibility

- Use customer_id exactly as given as the key in every file. Provide one row per customer, with probabilities between 0 and 1.
- Record all seeds (data split, model, optimizer, simulator, transpiler, Monte Carlo) and package versions.
- State the backend or simulator used, its configuration, and the shot count.
- Report logical and physical qubit counts, original and transpiled circuit depth, one-qubit and two-qubit gate counts, and SWAP count.
- Show ideal, noiseless finite-shot, and noisy results where applicable. Report unmitigated results alongside any mitigated ones.
- Include clear instructions in the README so the judges can rerun your work locally or in the cloud.

### 9. Scoring Framework

Submissions are scored out of 100 across four criteria. Judges verify results using hidden test labels and exact classical references.

#### Criterion 1: Quantum Rigor & Technical Depth — 35%

Evaluates technical soundness of the quantum or hybrid classifier, the binary optimization formulation and constraint handling in Stage 2, and the circuit design in Stage 3. Assesses valid execution or simulation with quantum SDKs and tools, and the quality of comparison with classical baselines.

#### Criterion 2: Result Accuracy & End-to-End Integration — 30%

Evaluates Stage 1 ranking and probability quality (PR-AUC, Precision@10, Recall@10, Brier score), Stage 2 feasibility and gap to the exact optimum, and Stage 3 closeness to the exact probability. Also assesses customer ID traceability across stages and how well the team analyzes error propagation.

#### Criterion 3: Code Quality & Reproducibility — 20%

Evaluates code organization, modular structure, dependencies, error handling, recorded seeds and environment details, and ease of local or cloud reproducibility.

#### Criterion 4: Report, Presentation & Communication — 15%

Assesses clarity, depth, and structure of the technical report and presentation, including business interpretation, a clear split between quantum and classical contributions, and discussion of noise, limitations, and error sources.
