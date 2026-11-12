# CertiQ-Chirp — Development Repository

**CertiQ-Chirp: Certified Quantum Campaign Intelligence**  
The Atomiq Hackathon | Qiskit Fall Fest 2026 at IEM · **Fintech** primary · AI/ML, Quantum ML, Optimization secondary.

This is the lean development source of truth. Presentation media, PDF dossiers, and upload archives are external handoffs; this repository keeps the runnable benchmark, pinned environment, source data, exact results, and core documentation.

## Headline results

- Selected six: **C0059, C0170, C0256, C0327, C0372, C0374**
- Submitted `Pr(K ≥ 3)`: **0.420** · exact analytical: **0.4164131424084104**
- Expected net value: **45.7874** · budget **11/25** · capacity **16/22**
- Certified Stage 2 gap: **0.0000** · engineering gates **30/30**
- Framework: **Qiskit 2.6.2 / Qiskit Aer 0.18.2**, statevector and Aer simulation only
- No unsupported quantum-advantage claim is made.

## Repository layout

| Path | Purpose |
|---|---|
| `README.md` | Repository entry point |
| `MANIFEST.md` | Every retained file with exact byte size |
| `CLEANUP_REPORT.md` | Before/after cleanup record |
| `.gitignore` | Keeps bulky generated deliverables out of the repo |
| `requirements.txt` | Pinned runtime versions |
| `seeds.json` | Reproducibility seed manifest |
| `LICENSE` | MIT license |
| `data/raw/` | Original participant workbook |
| `data/reference/` | Official problem-statement PDF |
| `docs/` | Hackathon analysis, technical spec, technical report, generated benchmark README |
| `results/` | Stage 1/2/3 CSV + JSON deliverables, 30-metric table, full summary, benchmark report |
| `src/run_benchmark.py` | End-to-end benchmark and exact-reference generator |
| `src/make_report.py` | Human-readable report generator from result files |

## Reproduce

```bash
pip install -r requirements.txt
python src/run_benchmark.py
python src/make_report.py
```

`run_benchmark.py` reads `data/raw/bank_campaign_participant_release.xlsx` and writes the `results/` files. `make_report.py` refreshes `results/benchmark_report.md` and `docs/BENCHMARK_README.md`.

## Design principle

Quantum components have defined jobs: a four-qubit kernel for calibrated probabilities, a ten-qubit QAOA selection experiment with an exact classical certificate, and a six-qubit product-state conversion simulation. Exact classical references and pinned seeds keep every headline number auditable.
