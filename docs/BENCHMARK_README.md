# CertiQ-Chirp benchmark

CertiQ-Chirp: quantum-calibrated ranker fusion + certified QAOA + noise-aware six-qubit Bernoulli ledger

## Overview

A modular, reproducible benchmark for a three-stage banking campaign workflow: leakage-safe Stage 1 prediction, exact-certified Stage 2 selection with a QAOA experiment, and a noise-aware six-qubit Stage 3 Bernoulli simulation. Stage 1 values are out-of-fold estimates; hidden test labels are not available. No quantum advantage is claimed.

## Run from the repository root

```bash
python src/run_benchmark.py
python src/make_report.py
```

For tests, install `requirements-dev.txt` and run `python -m pytest -p no:cacheprovider`. The package can also be invoked with `python -m certiq_chirp` after installing the project or adding `src/` to `PYTHONPATH`.

## Main artifacts

- `results/benchmark_report.md` — full 30-metric report (mirrored at `docs/04_TECHNICAL_REPORT.md`)
- `results/benchmark_metrics.csv` — machine-readable benchmark metrics
- `results/benchmark_summary.json` — full metrics, diagnostics, seeds, and versions
- `results/stage1_predictions.csv` — ranked probabilities for the 100 test customers
- `results/stage2_selection.json` — candidates, QAOA experiment, and exact certificate
- `results/stage3_simulation.json` — exact, ideal, finite-shot, noisy, and mitigated results

The supplied workbook is `data/raw/bank_campaign_participant_release.xlsx`; pinned runtime dependencies are in `requirements.txt`, and random seeds are recorded in `seeds.json`. Repository architecture and the full reproduction guide are in the root `README.md`.
