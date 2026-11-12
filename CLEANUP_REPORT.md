# Repository Cleanup & GitHub Readiness Report

**Current footprint:** `60` retained files · `1.33 MB` · `1,398,366` bytes · **0 hard-linked entries**. Counts and totals include this report and the self-indexed `MANIFEST.md`; transient caches and build/install output are excluded and ignored.

## Historical cleanup record

| Snapshot | Indexed files | Apparent size | Notes |
|---|---:|---:|---|
| Before cleanup | 657 | 212.4 MB | Included generated decks, PDFs, media, archives, working copies, and staging trees |
| Lean repository after cleanup | 23 | 1.0 MB | Retained source data, core docs, scripts, and benchmark results |
| After project-plan governance | 41 | 1.30 MB | Added the self-indexed `docs/plan/` control layer |
| Current GitHub-ready repository | `60` | `1.33 MB` | Added modular package, tests, packaging metadata, CI, and readiness evidence |

## Current retained structure

| Folder | Files | Bytes | Size |
|---|---:|---:|---:|
| `(root)` | `9` | `26,954` | `26.3 KB` |
| `.github` | `1` | `596` | `0.6 KB` |
| `data` | `2` | `851,897` | `831.9 KB` |
| `docs` | `23` | `351,836` | `343.6 KB` |
| `results` | `8` | `86,869` | `84.8 KB` |
| `src` | `12` | `67,510` | `65.9 KB` |
| `tests` | `5` | `12,704` | `12.4 KB` |

The project plan remains the original seven main phases and 44 tracked sub-phases, all completed. `docs/plan/` now also contains a separate GitHub-readiness addendum; it does not change the phase numbering or tracker. The source package is split into focused modules, while the original script paths remain runnable compatibility entry points.

## Intentional repository scope

- Retained: the participant workbook, official problem-statement PDF, runnable source, pinned dependencies, seed manifest, canonical CSV/JSON/Markdown results, technical documents, project plan, tests, and license.
- Intentionally external: presentation decks, generated PDF dossiers, media galleries, diagram exports, ZIP archives, and delivery wrappers. They are not restored to the repository; `.gitignore` keeps those generated handoffs out while explicitly retaining the official source PDF under `data/reference/`.
- The benchmark no longer rewrites `requirements.txt`, `seeds.json`, or `LICENSE` when it runs. Python bytecode, pytest caches, editable-install metadata, coverage output, and build directories are ignored.

## GitHub-ready project files

- `src/certiq_chirp/` contains the configuration, data, metrics, Stage 1, Stage 2/QAOA, Stage 3, pipeline, and reporting modules.
- `tests/` verifies workbook integrity, fold-local preprocessing, probability metrics, quantum circuits, exact certificates, Stage 3 simulation, all 30 engineering gates, CLI entry points, package configuration, and narrative/result parity.
- `pyproject.toml`, `requirements.txt`, and `requirements-dev.txt` define the package, compatible Python range, pinned runtime/test stack, and CLI entry points. `openpyxl` is explicitly pinned for Excel input.
- `.github/workflows/tests.yml` runs the pytest suite on pushes and pull requests.
- The root `README.md` is the publication-facing guide; `MANIFEST.md` indexes every retained file, including itself and this report.

## Verification

- `PYTHONPATH=src pytest -p no:cacheprovider`: **15/15 tests passed**.
- Editable installation from an isolated checkout succeeded; `certiq-chirp --help` and `certiq-chirp-report --help` both passed.
- `python src/run_benchmark.py` and `python src/make_report.py` both completed successfully in an isolated fresh clone.
- Six deterministic result files (`stage1_predictions.csv`, Stage 2 CSV/JSON, Stage 3 CSV/JSON, and `benchmark_metrics.csv`) matched the retained canonical files byte-for-byte. The summary also matched after excluding timing-only `runtime_seconds` and `model_fit_seconds_mean`; the full report matched after normalizing its formatted runtime line. `results/benchmark_report.md` and `docs/04_TECHNICAL_REPORT.md` are byte-identical.
- Reproduced Stage 2 objective: `45.78743946915947`, certified gap `0.0`; Stage 3 exact probability: `0.4164131424084104`, Aer finite-shot estimate: `0.420379638671875`.
- Benchmark report: **30/30** predeclared engineering gates passed. In-run reproducibility checks: **10/10 (100%)**.
- Final retained tree contains no Python/pytest/build caches and has **0 hard-linked entries**. The root canonical results were not overwritten by the isolated full run.

Wall-clock runtime and model-fit timings are expected to vary by machine and run. They remain explicitly represented as timing diagnostics rather than being described as byte-stable scientific results. See [`docs/plan/github_readiness_addendum.md`](docs/plan/github_readiness_addendum.md) for the detailed change and verification record.
