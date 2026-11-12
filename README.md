# CertiQ-Chirp — Certified Quantum Campaign Intelligence

> **Auditable banking campaign decisions with classical ranking, quantum experiments, and exact references.**

**Fintech** · **AI/ML + Quantum ML/Optimization** · The Atomiq Hackathon, Qiskit Fall Fest 2026 at IEM  
**Python 3.12+** · **Qiskit 2.6.2 / Aer 0.18.2** · **MIT License**

CertiQ-Chirp combines a leakage-safe customer-response benchmark, a quantum-kernel probability component, an experimentally evaluated QAOA selection stage, and a six-qubit conversion-probability circuit. Every stage is tied to exact or classical reference calculations. **No quantum advantage is claimed.**

## At a glance

| Evidence | Result |
|---|---:|
| Stage 1 winner | `rank_calibrated_hybrid` |
| Stage 1 ROC-AUC / PR-AUC (out-of-fold) | `0.6069003` / `0.2347176` |
| Stage 1 Brier / log loss / ECE (out-of-fold) | `0.1036442` / `0.3609301` / `0.0356714` |
| Stage 1 Precision@10% / Lift@10% (out-of-fold) | `0.3000` / `2.5714×` |
| Stage 2 selected customers | `C0059, C0170, C0256, C0327, C0372, C0374` |
| Stage 2 expected net value | `45.787439` · budget `11/25` · capacity `16/22` |
| Stage 2 exact certificate | `210/210` feasible subsets checked · certified gap `0.0` |
| Stage 3 exact `Pr(K ≥ 3)` / Aer finite-shot estimate | `0.4164131` / `0.4203796` (`0.420` to 3 d.p.) |
| Prototype engineering gates | **30/30 passed** |
| In-run reproducibility checks | **10/10 · 100%** |

Stage 1 is evaluated on the 300 labelled training rows using repeated out-of-fold predictions. The 100 test labels are not available; therefore its reported classification metrics are estimates, not hidden-test scores. Stage 2 and Stage 3 are computed from this prototype’s final Stage 1 probabilities and are not universal challenge answers.

## What the project does

The challenge is represented as one connected workflow rather than three disconnected quantum demonstrations:

1. **Predict:** rank 100 test customers from a 300-row labelled training set, using training-fold-only preprocessing and repeated stratified out-of-fold validation.
2. **Select:** choose exactly six customers from the top ten, maximizing expected net value subject to budget and capacity constraints. A 10-qubit warm-start QAOA experiment is evaluated alongside exhaustive classical search; the final choice is certified against that exact search.
3. **Simulate:** encode the six selected probabilities as independent Bernoulli qubits, estimate the probability of at least three conversions, and compare ideal, finite-shot, noisy, and mitigated results with an exact Poisson-binomial calculation.

### Rubric alignment

| Challenge criterion | Weight | Evidence in this repository |
|---|---:|---|
| Quantum Rigor & Technical Depth | 35% | Four-qubit Qiskit `ZZFeatureMap` kernel, 10-qubit QAOA experiment, six-qubit `RY` circuit, transpilation/resource reporting, classical comparisons |
| Result Accuracy & Integration | 30% | Same probability vector across stages, exhaustive Stage 2 certificate, exact Stage 3 probability, explicit errors and uncertainty |
| Code Quality & Reproducibility | 20% | Modular package, pinned dependencies, seed manifest, automated tests, compatibility scripts, retained result files |
| Report & Communication | 15% | Technical report, 30-metric table, result caveats, limitations, and auditable project plan |

## Results and methodology

### Stage 1 — leakage-safe hybrid prediction

The supplied workbook contains **300 training rows with 17 columns** (including ID and target) and **100 test rows with 16 columns** (including ID); the training set has **35 positive labels (11.67%)**. The 3×5 repeated stratified evaluation fits scaling, encoding, PCA, and quantum feature preprocessing within each training fold before transforming its held-out fold. The final models are then fit on all labelled rows to produce one prediction per test customer.

The selected `rank_calibrated_hybrid` uses a **60% quantum-kernel / 40% XGBoost probability blend**. The kernel is used as a probability-calibration component, not described as a stronger ranker. Headline out-of-fold estimates:

| Metric | Result | Context |
|---|---:|---|
| ROC-AUC | `0.6069003` | Out-of-fold ranking estimate |
| PR-AUC | `0.2347176` | Training prevalence `0.1166667`; bootstrap 95% CI width `0.2068854` |
| Brier score | `0.1036442` | Lower is better |
| Log loss | `0.3609301` | Lower is better |
| Expected calibration error | `0.0356714` | Ten-bin estimate |
| Precision@10% / Recall@10% | `0.3000` / `0.2571` | Out-of-fold top-decile estimates |
| Lift@10% | `2.5714×` | Relative to training prevalence |
| Winner repeated-CV PR-AUC standard deviation | `0.0164804` | Across the three repeated partitions |
| Quantum feature-map resources | `4` qubits · depth `17` | Qiskit `ZZFeatureMap`, one repetition |

The test predictions and deterministic ranking are in [`results/stage1_predictions.csv`](results/stage1_predictions.csv). Equal scores are ordered by customer ID.

### Stage 2 — constrained selection with an exact certificate

The objective for each candidate is `predicted_probability × expected_deposit_value − contact_cost`. The solver selects exactly six of the ten highest-ranked customers, subject to a contact budget of 25 and a capacity limit of 22. In this candidate pool, **all 210 six-customer subsets are feasible**, so neither constraint binds.

- **Top ten:** `C0170, C0256, C0327, C0338, C0188, C0079, C0081, C0374, C0059, C0372`
- **Selected six:** `C0059, C0170, C0256, C0327, C0372, C0374`
- **Budget / capacity used:** `11/25` / `16/22`
- **Expected net value and exhaustive optimum:** `45.78743946915947`
- **QAOA:** 10 qubits, 2 layers, 8,192 samples; raw best feasible objective `40.73970788738256`, raw gap `5.047731581776915`
- **Certified hybrid result:** objective `45.78743946915947`, gap `0.0`

The raw QAOA gap is reported rather than hidden. The zero final gap follows from hybrid repair plus the explicit exact classical certificate; it is **not** evidence of quantum advantage. See [`results/stage2_selection.json`](results/stage2_selection.json) and its CSV companion.

### Stage 3 — six-qubit Bernoulli conversion ledger

Each selected probability `pᵢ` is encoded with an `RY(2 asin √pᵢ)` gate. The target is the probability of at least three conversions among the six independent Bernoulli outcomes.

| Estimator | `Pr(K ≥ 3)` |
|---|---:|
| Exact Poisson-binomial reference | `0.4164131424084104` |
| Ideal statevector | `0.4164131424084103` |
| Qiskit Aer, noiseless finite-shot (`32,768` shots) | `0.420379638671875` |
| Independent Monte Carlo | `0.415130615234375` |
| Synthetic noisy simulation | `0.43133544921875` |
| Primary marginal-inversion mitigation | `0.41239821154870004` |
| 64×64 NNLS response-matrix cross-check | `0.4111108154155694` |

The finite-shot 95% half-width is `0.0053376`; the primary mitigation reduces absolute error versus the noisy estimate by **73.0944%**. The circuit uses six qubits, logical/transpiled depth `1/1`, six one-qubit gates, and zero two-qubit or SWAP gates. The noise model is synthetic (single-qubit depolarizing probability `0.02`, symmetric readout error `0.03`) and is not a calibration of a real quantum backend.

Full counts, mapping, noise parameters, and errors are retained in [`results/stage3_simulation.json`](results/stage3_simulation.json).

### Engineering gates and reproducibility

The benchmark report evaluates **30 predeclared engineering gates; 30/30 pass**. These are project checks, not an official judging score. The benchmark also records 10 in-run integrity/reproducibility checks (10/10 pass). The project’s seed manifest is [`seeds.json`](seeds.json); package versions and raw diagnostics are in [`results/benchmark_summary.json`](results/benchmark_summary.json).

Random seeds and pinned libraries stabilize the model and simulation artifacts. Wall-clock measurements are hardware-dependent: `runtime_seconds` and `model_fit_seconds_mean` in the summary, plus the formatted report runtime line, may differ between runs. Prediction, selection, QAOA, simulation, and benchmark-metric artifacts are validated separately from those timing fields.

## Repository architecture

```text
CertiQ-Chirp/
├── .github/workflows/tests.yml       # GitHub Actions test job
├── data/
│   ├── raw/                           # supplied participant workbook
│   └── reference/                     # official problem-statement PDF
├── docs/
│   ├── 01_HACKATHON_ANALYSIS.md       # challenge and source audit
│   ├── 02_TECHNICAL_SPEC.md           # extracted technical specification
│   ├── 04_TECHNICAL_REPORT.md         # generated full benchmark narrative
│   └── plan/                          # master plan, work packages, evidence
├── results/                           # canonical CSV, JSON, and Markdown outputs
├── src/
│   ├── run_benchmark.py               # compatibility CLI
│   ├── make_report.py                 # compatibility report CLI
│   └── certiq_chirp/
│       ├── __init__.py                # package initialization and version
│       ├── __main__.py                # python -m entry point
│       ├── config.py                  # paths, seeds, experiment constants
│       ├── data.py                    # workbook loader
│       ├── metrics.py                 # metrics, calibration, bootstrap, meta-CV
│       ├── stage1_hybrid.py           # fold-local preprocessing and hybrid models
│       ├── stage2_qaoa.py             # exact selection and QAOA
│       ├── stage3_bernoulli.py        # six-qubit simulation and mitigation
│       ├── pipeline.py                # end-to-end orchestration
│       └── reporting.py               # benchmark report and engineering gates
├── tests/                             # pytest verification suite
├── pyproject.toml                     # package, CLI, and pytest configuration
├── requirements.txt                   # pinned runtime dependencies
├── requirements-dev.txt               # runtime plus test dependency
├── seeds.json                         # experiment seed manifest
├── MANIFEST.md                        # retained-file byte index
└── LICENSE                            # MIT
```

### Module map

| Module | Responsibility |
|---|---|
| `__init__.py` / `__main__.py` | Initialize package configuration and expose `python -m certiq_chirp` |
| `config.py` | Sets `OMP_NUM_THREADS` before numerical imports; defines checkout paths, seeds, and stage constants |
| `data.py` | Loads the train, test, and Stage 2 workbook sheets |
| `metrics.py` | Probability clipping, calibration, ranking metrics, bootstrap CI, and meta-CV |
| `stage1_hybrid.py` | Classical baselines, quantum kernel, fold-local preprocessing, and repeated OOF evaluation |
| `stage2_qaoa.py` | Exact six-of-ten selection certificate, QAOA circuit and measured-sample repair |
| `stage3_bernoulli.py` | Poisson-binomial reference, six-qubit circuit, Aer noise, and mitigation |
| `pipeline.py` | Connects the stages and writes canonical benchmark result files |
| `reporting.py` | Regenerates the 30-metric report, concise benchmark README, and engineering-gate results |

The compatibility scripts preserve the existing `python src/run_benchmark.py` and `python src/make_report.py` commands. The package entry point is also available as `python -m certiq_chirp` when `src/` is on the import path or the project is installed.

## Quickstart

Use Python **3.12 or newer** to match the pinned numerical stack (including XGBoost 3.4.1). Run commands from the repository root so the workbook and generated files resolve correctly.

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Run the full benchmark and regenerate its reports:

```bash
python src/run_benchmark.py
python src/make_report.py
```

Run the automated test suite:

```bash
python -m pytest -p no:cacheprovider
```

To install package commands in the active environment, use `python -m pip install -e .` (or `python -m pip install -e ".[test]"` to include the pinned test extra). Then use `certiq-chirp` and `certiq-chirp-report`; run them from the repository checkout. Editable-install metadata and build/test caches are ignored by Git.

The complete rerun performs repeated cross-validation and Qiskit simulation; expect a few minutes depending on hardware. Report generation alone (`python src/make_report.py`) reads the retained results and is quick.

## Documentation index

- [Hackathon analysis](docs/01_HACKATHON_ANALYSIS.md) — challenge context, rubric, source priority, and submission requirements.
- [Technical specification](docs/02_TECHNICAL_SPEC.md) — problem stages, data, constraints, and scoring framework.
- [Full 30-metric technical report](docs/04_TECHNICAL_REPORT.md) — generated narrative and detailed limitations.
- [Concise benchmark README](docs/BENCHMARK_README.md) — results and reproduction overview.
- [Master project plan](docs/plan/plan.md) — seven phases and 44 sub-phases; [tracker](docs/plan/TRACKER.csv) and [status](docs/plan/status.json).
- [Phase 0–6 completion records](docs/plan/) — execution evidence, validation, and change-control history.
- [GitHub-readiness addendum](docs/plan/github_readiness_addendum.md) — modularization, automated tests, packaging, CI, and clean-clone verification.
- [Manifest](MANIFEST.md) and [cleanup report](CLEANUP_REPORT.md) — retained files and repository-footprint record.

## Scope, limitations, and interpretation

- Hidden test labels are unavailable; out-of-fold estimates are not hidden-test results.
- The training set is small and has 35 positive cases; the PR-AUC confidence interval is correspondingly broad.
- The quantum-kernel component is not a superior ranker. Classical XGBoost provides ranking information in the selected blend.
- The raw QAOA sample did not reach the exact optimum. The reported zero gap is a hybrid-repair result verified by exhaustive classical search.
- Stage 3’s noise channel is synthetic, and all circuits are run in simulation rather than on quantum hardware.
- Stage 2 and Stage 3 values depend on this model’s final Stage 1 probabilities and must not be represented as universal or official answers.

## License

Released under the [MIT License](LICENSE).
