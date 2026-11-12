# CertiQ-Chirp — Devpost Media Gallery

Every diagram is exported from its original SVG source. Text remains crisp, colours stay consistent, and each plate carries the project identity.

## Folder guide

| Folder | Contents |
|---|---|
| `diagrams_svg/` | 21 original vector diagrams |
| `diagrams_png/` | 21 high-resolution PNG exports at 2400 px width |
| `diagrams_png_web/` | 21 lighter PNG exports at 1600 px width |
| `gallery_png/` | 21 branded 1600×900 Devpost gallery plates |
| `thumbnails/` | 21 1200×630 thumbnail crops |
| `logos/` | 5 SVG logo files + 5 PNG exports |
| `hero/` | Hero banner and square social card, SVG + PNG |
| `icons/` | 6 SVG icons, 6 PNG exports, and a contact sheet |
| `data/` | `manifest.json` and `diagram_data.json` |

## Recommended upload order

1. `hero/hero_banner.png` — primary gallery image
2. `gallery_png/01_architecture_gallery.png`
3. `gallery_png/09_qaoa_circuit_gallery.png`
4. `gallery_png/11_stage3_circuit_gallery.png`
5. `gallery_png/18_business_dashboard_gallery.png`
6. `gallery_png/03_model_scores_gallery.png`
7. `gallery_png/05_calibration_gallery.png`
8. `gallery_png/13_stage3_estimates_gallery.png`
9. `gallery_png/17_rubric_gallery.png`
10. Remaining plates in figure order

## Figure catalog

| # | Title | Section | Caption |
|---:|---|---|---|
| 1 | Cover artwork | Cover | Abstract cloud-quantum network and circuit motif used on the submission cover. |
| 2 | End-to-end architecture | Architecture | Data, prediction, constrained selection, and quantum simulation form one traceable pipeline. |
| 3 | Stage 1 leakage controls | Stage 1 | All preprocessing, calibration, and fusion weights are learned from out-of-fold training predictions. |
| 4 | Model selection scoreboard | Stage 1 | The 40% XGBoost / 60% quantum-kernel fusion achieved the highest judge-aligned composite. |
| 5 | Discrimination curves | Stage 1 | Out-of-fold ROC and precision–recall behaviour on the 300 labelled training customers. |
| 6 | Probability calibration | Stage 1 | Reliability curve supports the low Brier score, log loss, and expected calibration error. |
| 7 | Fusion-weight sensitivity | Stage 1 | The selected 60% quantum / 40% XGBoost point balances calibration with top-decile ranking. |
| 8 | Top-10 candidate probabilities | Stage 1 | Continuous probabilities are preserved and ranked with customer_id tie-breaking. |
| 9 | Constraint and penalty design | Stage 2 | The exact-six and one-sided resource constraints are encoded in a diagonal QAOA cost oracle. |
| 10 | QAOA logical circuit | Stage 2 | Warm-start RY initialization, two diagonal cost layers, and RX mixers on ten selection qubits. |
| 11 | Stage 2 objective landscape | Stage 2 | All feasible six-customer subsets are enumerated; raw QAOA and certified optimum are shown. |
| 12 | Stage 3 product-state circuit | Stage 3 | One RY rotation per customer prepares the exact subscription probability on each qubit. |
| 13 | 64-outcome probability map | Stage 3 | Independent Bernoulli outcomes; the upper-right region corresponds to three or more successes. |
| 14 | Stage 3 estimate comparison | Stage 3 | Exact, ideal statevector, finite-shot, Monte Carlo, noisy, and mitigated results agree within reported errors. |
| 15 | Noise response matrix | Stage 3 | Tensor-product response of single-qubit depolarizing noise and symmetric readout error. |
| 16 | Measurement-count distribution | Stage 3 | The 32,768 noiseless shots populate all 64 outcomes according to the product-state distribution. |
| 17 | Error propagation | Integration | Probability uncertainty is carried into optimization and the final conversion estimate. |
| 18 | Judge rubric readiness | Judging | Rubric-aligned estimate based on quantum depth, exact references, reproducibility, and communication. |
| 19 | Business impact dashboard | Business | Operational and financial interpretation of the final Stage 2 and Stage 3 results. |
| 20 | Reproducibility map | Reproducibility | One runnable pipeline connects pinned inputs to every root-level deliverable and reference result. |
| 21 | Submission timeline | Submission | The final package consolidates code, result files, diagrams, and narrative into a judge-ready submission. |

## Alt-text pattern

`CertiQ-Chirp Figure NN: <title> — <caption>`

## Exact values used in the visual identity

- Submitted Pr(K ≥ 3): **0.420**
- Exact analytical Pr(K ≥ 3): **0.4164131424084104**
- Expected net value: **45.7874**
- Budget: **11 / 25** · Capacity: **16 / 22**
- Certified Stage 2 gap: **0.0000**
- Transparent engineering gates: **30 / 30**
- Net / cost: **4.1625×**

Total files in this gallery pack: **136**.
