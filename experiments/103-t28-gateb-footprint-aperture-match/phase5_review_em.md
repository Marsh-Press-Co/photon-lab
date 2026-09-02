#### ELECTROMAGNETISM — verdict: **CONFIRM-WITH-GAPS**

**Scope note (charter):** T1 is N/A this cycle (zero `lab/` diff, no mechanism, no gain/nonreciprocal element introduced) — reciprocity is not engaged and I find nothing to check there. My bookkeeping this phase is (1) passivity (kappa bounded by 1), and (2) causality/settling (transient-vs-steady-state validity of the STEPS=3200 convention).

### Independent recomputation (raw fields, shown)

**1. Settling-check `rel_change`, hand-recomputed for two of the five points:**
- x=352: `|0.004575402764189365 - 0.004580436735147808| / 0.004580436735147808 = 1.09902e-3` → matches reported exactly.
- x=356: `|0.005579531994004347 - 0.0055797070057914296| / 0.0055797070057914296 = 3.1366e-5` → matches reported exactly.

**2. `kappa_window` ratio-of-means, recomputed from raw window stats:** matches reported `0.018336958179764707`. Also cross-checked `span_mean` (0.0329313300) and `ratio_to_window` (1.7959) — both match exactly.

**3. `envelope()`-vs-`phasors()` quantization-bias arithmetic, recomputed independently from the stated formula at N=560, cpl=20 (λ=20 cells), courant_frac=0.32:**
- `S = 0.32/√2 = 0.22627417`
- `λ/S/4 = 22.097` → `quarter = round(22.097) = 22` — matches NOTES.
- `ω = 2π·S/λ = 0.0710861` — NOTES states `ω≈0.07111`; my recomputation gives `0.071086`, a small (~0.03%) discrepancy.
- `φ = ω·22 = 1.563895 rad` — NOTES states `φ≈1.5644`; my value is `1.5639`, ~0.0005 rad off.
- `cos(φ) ≈ 0.0069014` — NOTES states `cos(φ)≈0.0064`. My recomputation from the exact stated formula gives ~8% higher than the disclosed figure (using NOTES' own rounded ω=0.07111 reproduces their 0.0064, so the discrepancy traces to ω's own rounding, not a different formula).

**Verdict on this disclosure:** the qualitative conclusion (small, sub-1% bound) survives — 0.69% vs. the claimed 0.64% is the same order and doesn't change any decision — but the arithmetic as literally specified does not reproduce the document's own headline number; the true worst-case bound is closer to ~0.69%, not ~0.6%. More importantly: the disclosure cannot mechanistically predict *which direction* beam_behind and kappa_window should diverge, and `kappa_window` landed **above** the 1.5–1.8% anchor, not below — so this disclosure was pre-registered against a scenario that didn't occur and, correctly, is not invoked to explain anything in Result.

### Findings

**[load-bearing] NOTES.md's Result/Learned-#2 comparison to VALIDATION.md's stage-20 baseline is numerically backwards — the observed settling residuals are LARGER than the cited baseline, not smaller.**
NOTES.md states the 0.003%–0.11% settling residuals are "two to three orders of magnitude **smaller** than VALIDATION.md's own stage-20 canonical figure … (~1.5×10⁻⁵ field-relative RMS by 900 steps)." Recomputing: `1.5e-5` = 0.0015%. The five observed relative changes (`3.14e-5, 8.36e-4, 5.22e-4, 2.33e-4, 1.10e-3` as fractions) are **every one larger than 1.5e-5**, ranging from ~2× (x=356) to **~73×** (x=352: `1.099e-3/1.5e-5=73.3`). That's roughly two orders of magnitude in the *opposite* direction from what's claimed. This does **not** flip any of the four Prediction verdicts — Prediction 4's actual falsification criterion (20% tolerance) is independently verified correct and clears by 2–4 orders of magnitude regardless — but it is a load-bearing error in the interpretive narrative that future cycles will inherit from LOGBOOK/NOTES as an anchor claim.

**[non-load-bearing, methodological]** Passing the 3200-vs-6400 settling check is necessary, not sufficient, for genuine convergence to the correct CW steady state — it cannot by construction distinguish "settled correctly" from "settled to a shared, step-count-independent artifact" (e.g. numerical dispersion from `cells_per_lambda=20`, which is fixed by spatial resolution, not step count). Two observations keep this from being a live concern: (1) relative-change decreases monotonically with standoff (0.110% at x=352 down to 0.003% at x=356) — the correct qualitative signature of a decaying near-field transient, not a flat artifact floor; (2) this matches my own Phase-2 critique's directional logic. But the check as built genuinely cannot rule out a slowly-decaying leakage mode with a longer time constant than the 3200-step gap tested — a true convergence bench (3rd step count, or an independent analytic reference) would close this gap. Not claimed closed by NOTES.md, so not a false claim, just an underdisclosed limit on Prediction 4's "CONFIRMED, decisively" language.

**[non-load-bearing, confirms a charter sanity-check was implicitly satisfied]** No kappa value — window or region, mean, pointwise, min, or max — approaches or exceeds 1 anywhere in `results.json`. All comfortably ≪1. This is exactly the passivity bound my charter is responsible for, implicitly satisfied everywhere, worth stating explicitly (currently absent from NOTES.md/results.json).

**[non-load-bearing]** Two internally-consistent but distinct window-level statistics differ by ~1.9% — `kappa_window` (ratio of means, 0.018337) vs. `pointwise_mean` (mean of pointwise ratios, 0.018690) — a Jensen's-inequality-type divergence expected whenever a ratio's numerator and denominator both carry spatial structure, which the window's own std/mean=0.849 confirms they do. Neither figure is wrong; worth one explicit sentence.

### Argued next change

Before this NOTES.md is trusted as a LOGBOOK anchor for future settling-independence claims, correct the "two to three orders of magnitude smaller" sentence in Result/Learned-#2 to state the arithmetic actually found — larger, not smaller, by up to ~73× at the closest-sampled point — while being explicit this does not flip Prediction 4's verdict and that the two figures measure different things (a phase-rotation-identity noise floor vs. a two-step-count κ comparison), so the comparison was probably never apples-to-apples and should either be dropped or reframed as illustrative. Separately, for the next cycle leaning on near-field settling at even smaller standoffs, a genuine convergence bench (a third step count, or a direct comparison to an analytically known reference) would close the "settled to the wrong value" gap this check cannot address by construction.
