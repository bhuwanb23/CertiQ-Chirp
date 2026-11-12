# CertiQ-Chirp prototype

CertiQ-Chirp: quantum-calibrated ranker fusion + certified QAOA + noise-aware six-qubit Bernoulli ledger

## What it does

Runs a leakage-free 3×5 repeated-CV benchmark on `Stage1_Train`, fits all final models once, predicts the 100 `Stage1_Test` customers, solves Stage 2 with a certified quantum-assisted optimizer, and executes Stage 3 with Qiskit Aer under ideal and noisy conditions.

## Run

```bash
cd /home/user/atomiq_analysis
python src/run_benchmark.py
python src/make_report.py
```

The source workbook is at `data/raw/bank_campaign_participant_release.xlsx`. Dependencies are pinned in `requirements.txt`; all seeds are in `seeds.json`.

## Outputs

- `results/benchmark_report.md` — winning idea and 30-metric benchmark
- `results/benchmark_metrics.csv` — machine-readable 30 metrics
- `results/benchmark_summary.json` — every raw measurement
- `results/stage1_predictions.csv` — all 100 test probabilities
- `results/stage2_selection.json` — top 10, QAOA, exact classical certificate
- `results/stage3_simulation.json` — full measurement counts and exact/noisy/mitigated results

## Repository scope

This lean repository keeps the runnable benchmark, pinned environment, seed manifest, source data, and exact result files. Presentation media and submission documents are maintained as external deliverables.
