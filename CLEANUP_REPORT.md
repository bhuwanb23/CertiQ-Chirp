# Workspace Cleanup Report

**Result:** the repository is now a lean, root-level development tree. The downloaded PDF dossiers, presentation deck, media gallery, diagram exports, ZIP archives, wrapper project tree, staged bundles, source-working duplicates, root quick copies, and one-off asset/PDF/organization generators were removed.

| Measure | Before cleanup | Post-cleanup | Current with `docs/plan/` |
|---|---:|---:|---:|
| Indexed files | 657 | 23 | 41 |
| Apparent indexed size | 212.4 MB | 1.0 MB | 1.30 MB |
| `du -sb` actual size | — | 1.0 MB | 1.30 MB |
| Hard-linked file entries | 621 | 0 | 0 |
| Workspace budget | 128.0 MB | comfortably within limit | comfortably within limit |

## What remains

| Folder | Files | Size |
|---|---:|---:|
| `data` | 2 | 831.9 KB |
| `docs` | 22 | 339.3 KB |
| `results` | 8 | 84.6 KB |
| `src` | 2 | 60.2 KB |
| `(root)` | 7 | 11.2 KB |

The 18 additional files are the `docs/plan/` tracking layer: `plan.md`, `phase_0.md`…`phase_6.md`, `phase_0_completion.md`, `phase_1_completion.md`, `phase_2_completion.md`, `phase_3_completion.md`, `phase_4_completion.md`, `phase_5_completion.md`, `phase_6_completion.md`, `README.md`, `TRACKER.csv`, and `status.json`.

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
- Phase 1 fresh-clone reproduction: pinned stack installed; `src/run_benchmark.py` and `src/make_report.py` succeeded in an isolated clone; 10 result/metadata files byte-identical.
- Phase 2 fresh-clone reproduction: 3×5 OOF CV, quantum kernel, fusion, and 100-row probability vector regenerated; 10 result/metadata files byte-identical.
- Phase 3 fresh-clone reproduction: QUBO/QAOA, exact brute-force certificate, business block, and Stage 3 handoff regenerated; 10 result/metadata files byte-identical.
- Phase 4 fresh-clone reproduction: six-qubit `RY` product circuit, exact/ideal/Aer/Monte Carlo/noisy/mitigated probabilities, and 64-bin count histograms regenerated; 10 result/metadata files byte-identical.
- Phase 5 fresh-clone reproduction: Stage 1–3 probability/ID integration, 30-metric benchmark (`30/30` gates), `10/10` reproducibility checks (`100.0%`), readiness table, and limitation register verified; 10 result/metadata files byte-identical.
- Phase 6 communication & handoff validation: 22/22 narrative-to-JSON consistency checks PASS, `make_report.py` byte-exact, 19/19 `.gitignore` patterns active, and 0 bulky generated deliverables in the lean repo.
- Post-cleanup apparent size: **1.0 MB** across **23 files**.
- Current apparent size with the plan layer: **1.30 MB** across **41 files**.
- Current hard-linked file count: **0**.
