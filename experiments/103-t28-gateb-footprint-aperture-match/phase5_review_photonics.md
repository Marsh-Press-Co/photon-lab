#### PHOTONICS — verdict: **CONFIRM-WITH-GAPS**

## Independent recomputation (from `results.json` primitives)

All headline numbers recomputed directly from raw fields; all matched the reported values to full float precision.

1. **kappa_window** = article.mean/empty.mean = 0.09149678174941363 / 4.989746982701996 = **0.018336958179764707** — exact match.
2. **Pointwise std/mean** = 0.015864562708848298 / 0.01868984554416697 = **0.8488** — matches "0.849" (rounds correctly).
3. **Monotonicity**, checked myself in x-sorted order (all 16 keys): strictly increasing at every step, zero reversals even at zero tolerance. Confirmed, not just restated.
4. **Settling relative-change**, recomputed at all 5 near-field points: 0.10990%, 0.08358%, 0.05221%, 0.02328%, 0.00314% — exact match, all ≪20% tolerance.
5. **Floor-gate RMS/floor/n_unresolved** and **span_mean/ratio_to_window** independently recomputed — both match exactly.

No arithmetic discrepancy found anywhere I checked. `run.py` code inspection confirms the reported figures are computed exactly as described, `EDGE=40` is hard-coded with the stated derivation, and the `BEHIND` window bounds are asserted in `run.py` to equal exp-001's own slice — independently confirmed against `experiments/001-flashlight-statement/run.py` line 72, byte-identical.

## Findings

**F1 [non-load-bearing, CONFIRMED plausible]** — `kappa_window` std/mean≈0.849 is not alarming on its own. The window spans x=357→457, exactly the range over which the trend itself rises ~14× (0.58%→6.41%). A window mean averaging over a region whose local intensity varies by more than an order of magnitude will trivially show std/mean of order unity; consistent with a smooth diffraction-shadow gradient.

**F2 [load-bearing]** — The Phase-2 "Nyquist fix" (≤10-cell pitch, described as "λ/2 pitch") does **not** actually satisfy the sampling theorem for the λ/2=10-cell standing-wave period it was adopted to guard against. Nyquist requires sample spacing strictly less than half the period being resolved — here that is <5 cells, not ≤10. A 10-cell pitch equals *one full period* of the suspected ripple: the textbook degenerate aliasing case, not a fix. The reduction from the Phase-1 proposal's original ~18–20-cell pitch (worse: ~2× the period, doubly aliased) to 10 cells is a real improvement in degree but not a correction in kind — it moved the sampling from clearly-aliased to exactly-at-the-degenerate-limit, not to resolved.

**F3 [load-bearing, partially mitigating F2]** — However, `H_REGION=5` in `run.py` gives an 11×11-cell box average (`block_mean_intensity`), not a point sample. A boxcar of width W=11 cells filters a spatial-period-P=10-cell sinusoid by a factor |sinc(W/P)| = |sinc(1.1)| ≈ **0.089** — each single sample already suppresses ~91% of any λ/2-period ripple amplitude internally, independent of the inter-sample pitch. So the smooth appearance of the trend partly reflects genuine per-sample low-pass filtering built into the H_REGION averaging convention (inherited from exp-102, not new to this cycle).

**F4 [load-bearing]** — F2 and F3 together mean NOTES.md's own causal claim — "the tightened … sampling pitch … shows no sign of the aliased ripple that risk would have produced; the trend is smooth at this resolution" — overstates what this data can show. A smooth trend at H_REGION=5, 10-cell pitch is close to what you'd see **whether or not** a λ/2-scale coherent ripple is present, because the measurement is constructed to be intrinsically close-to-blind to that specific spatial frequency. The zero-reversal result is real and correctly computed, and is good evidence for the *broad* Fresnel-fill-in envelope shape, but it is weak evidence specifically against the finer λ/2 standing-wave alternative Prediction 2 explicitly claims to have distinguished from.

**F5 [non-load-bearing, corroborating]** — VALIDATION.md's own recorded lesson (25–40-cell Fresnel edge-fringe period) is directly on point for this geometry class. At 10-cell pitch, this coarser fringe mechanism *is* adequately Nyquist-sampled (2.5–4 samples/period), so the smooth trend is credible evidence against large-amplitude source-aperture edge-diffraction fringes specifically — just not against the finer λ/2 back-reflection-driven standing-wave mechanism. NOTES.md and the Red Team audit conflate these two distinct fringe mechanisms under one "Nyquist fix," when they operate at different spatial scales.

**F6 [non-load-bearing, CONFIRMED]** — The EDGE=40 vs EDGE=80 correction is physically the right fix on independent optical-taper reasoning, re-derived from `lab/fdtd2d.py::add_line_source` and the design_geometry.py constants directly.

**F7 [non-load-bearing]** — kappa_window=1.8337% lands essentially at the *top edge* of, not comfortably inside, the established 1.5–1.8% `beam_behind` range — a genuine numeric proximity, not a strong central match, though self-consistent with the disclosed quantization-bias direction (independently re-derived and confirmed correct).

## Argued next change (PHOTONICS seat, for Iteration 81)

Before extending this instrument to the r=156/312 bridge family, Iteration 81 should close the sampling-scale gap this review surfaces: re-run or re-analyze the standoff leg with either (a) a genuinely sub-Nyquist pitch for the λ/2=10-cell period specifically — ≤4 cells, not ≤10 — over at least one contiguous stretch, or (b) a smaller `H_REGION` (1–2 cells instead of 5) at a handful of points so the per-sample boxcar stops pre-filtering the frequency being tested, and compare against the current trend to see whether the two converge (real confirmation) or diverge (a λ/2 standing wave was there all along). Cheap relative to the bridge-family extension — better to find out now, at native scale, than after Tier 1 item 3 has propagated the same convention across three more radii.
