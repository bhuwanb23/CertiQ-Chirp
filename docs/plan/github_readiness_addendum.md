# GitHub Readiness Addendum — Modular Package, Tests & Publication

**Status:** ✅ Completed  
**Scope:** Post-Phase-6 repository engineering hardening; this addendum does not alter the numbered Phase 0–6 plan or its 44/44 sub-phase tracker.

## Objective

Prepare the lean CertiQ-Chirp repository for direct publication and reproduction from a clean checkout, while retaining the existing command-line paths and scientific outputs.

## Completed work

- Split the benchmark into `src/certiq_chirp/` modules for configuration, data loading, metrics, Stage 1, exact Stage 2/QAOA, Stage 3, orchestration, and reporting.
- Retained `python src/run_benchmark.py` and `python src/make_report.py`; added `python -m certiq_chirp` and package console entry points.
- Preserved fold-local preprocessing and placed `OMP_NUM_THREADS=1` before numerical imports.
- Added `pyproject.toml`, pinned runtime and test requirements, the Excel engine dependency, cache/build ignore rules, and a GitHub Actions pytest workflow.
- Added tests for workbook integrity, fold-local preprocessing, probability metrics, the four-, ten-, and six-qubit circuits, exact Stage 2 selection/certificates, Stage 3 references/noise, all 30 engineering gates, CLI smoke checks, and README/report value parity.
- Upgraded the root README and regenerated the benchmark report/concise documentation for the modular architecture. The technical report and `results/benchmark_report.md` are kept byte-identical.
- Replaced the abbreviated license text with the standard MIT grant and warranty disclaimer; benchmark runs no longer rewrite requirements, seed, or license source files.

## Verification evidence

- `PYTHONPATH=src pytest -p no:cacheprovider`: **15 tests passed**.
- Editable package installation from an isolated checkout succeeded; both `certiq-chirp --help` and `certiq-chirp-report --help` returned successfully.
- Full end-to-end run from an isolated fresh clone using `python src/run_benchmark.py`, followed by `python src/make_report.py`: **exit code 0**.
- The fresh clone reproduced the retained `stage1_predictions.csv`, Stage 2 CSV/JSON, Stage 3 CSV/JSON, and `benchmark_metrics.csv` byte-for-byte.
- The fresh-clone `benchmark_summary.json` matched after excluding timing-only fields (`runtime_seconds` and `model_fit_seconds_mean`). The generated benchmark report matched after normalizing its formatted runtime line; the generated `results/benchmark_report.md` and `docs/04_TECHNICAL_REPORT.md` were byte-identical.
- Reproduced headline values: Stage 2 objective `45.78743946915947`, certified gap `0.0`; Stage 3 exact probability `0.4164131424084104`, Aer finite-shot estimate `0.420379638671875`; engineering gates `30/30`.

## Reproducibility note

Wall-clock runtime and per-model fit-time diagnostics are intentionally measured values and can vary by machine and run. The benchmark’s prediction, selection, QAOA, simulation, and metric artifacts were verified against the retained canonical files; the root repository’s canonical results remain the source of truth. The runtime-dependent fields are disclosed rather than represented as byte-stable scientific outputs.

## Maintenance

Run tests with `python -m pytest -p no:cacheprovider`. Run the full benchmark from the repository root with `python src/run_benchmark.py`, and regenerate the synchronized report files with `python src/make_report.py`. Review result and narrative parity whenever benchmark behavior or the pinned environment changes.
