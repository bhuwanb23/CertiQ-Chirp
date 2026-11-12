# Workspace Cleanup Report

**Result:** the repository is now a lean, root-level development tree. The downloaded PDF dossiers, presentation deck, media gallery, diagram exports, ZIP archives, wrapper project tree, staged bundles, source-working duplicates, root quick copies, and one-off asset/PDF/organization generators were removed.

| Measure | Before | After |
|---|---:|---:|
| Indexed files | 657 | 23 |
| Apparent indexed size | 212.4 MB | 1.0 MB |
| `du -sb` actual size | — | 1.0 MB |
| Hard-linked file entries | 621 | 0 |
| Workspace budget | 128.0 MB | comfortably within limit |

## What remains

| Folder | Files | Size |
|---|---:|---:|
| `(root)` | 7 | 6.5 KB |
| `data` | 2 | 831.9 KB |
| `docs` | 4 | 59.0 KB |
| `results` | 8 | 84.6 KB |
| `src` | 2 | 59.4 KB |

## Structural fix

- Code moved to `src/`, results to `results/`, data to `data/`, and documentation to `docs/`.
- `src/run_benchmark.py` and `src/make_report.py` were repointed to the new root-level paths.
- `.gitignore` prevents bulky generated deliverables from returning to the repository.
- The duplicate `docs/05_BENCHMARK_REPORT.md` was removed; `results/benchmark_report.md` is the canonical generated report.
- All retained files are regular single-link files; no duplicate hard-link trees remain.

## Verification

- `python -m py_compile src/run_benchmark.py src/make_report.py` passed.
- `python src/make_report.py` regenerated `results/benchmark_report.md` and `docs/BENCHMARK_README.md`.
- `data/raw/bank_campaign_participant_release.xlsx` is present at the benchmark's expected path.
- Final apparent size: **1.0 MB** across **23 files**.
