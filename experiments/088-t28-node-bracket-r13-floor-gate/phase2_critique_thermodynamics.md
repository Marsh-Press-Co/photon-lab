# PHASE 2 — CRITIQUE (THERMODYNAMICS) · Panel Iteration 65 · exp-088

*Fresh context, blind to all other seats' current-cycle critiques. Read
PANEL.md, LOGBOOK.md (RULED OUT R1–R13 in full, LIVE THREADS T28 in full
through Iteration 64/exp-087), `experiments/088-.../phase1_proposal.md`
(this cycle's proposal, in full), `experiments/087-.../NOTES.md` +
`run.py`, and `lab/thermo_sidecar.py` source. Independently re-derived
every load-bearing numeric claim below from committed JSON and source —
not restated from the proposal's own prose (R4/R9 discipline).*

## Independent verification performed

- **§4's floor-gate arithmetic reproduces exactly.** Recomputed RMS of
  `frac_contrast(θ)` over all 31 angles in `experiments/083-.../
  results.json::per_theta` from primitives: `1.9174375118374476e-3`,
  matching the proposal's cited `1.91744×10⁻³` to displayed precision;
  `FLOOR=1.917×10⁻⁴` reproduces; every cited `frac_contrast` value
  (36.0°, 38.4°, 38.6°, 38.8°, 41.8°) reproduces exactly against the
  underlying `delta_scene`/`C40_C` fields, and all five clear/fail margins
  in §4 (3.88×, 0.39×, 6.59×, 7.50×, 8.02×) reproduce exactly. No defect
  found here.
- **The P8/NETD "would not plausibly move" claim's physical premise is
  independently checkable — and turns out to be true, but not because the
  proposal shows it.** Pulled `experiments/087-.../results.json::thermo`
  directly: `p_abs_w` varies smoothly, only ~18% across the whole
  36.0°→41.8° span (2.749×10⁻¹²→3.235×10⁻¹² W, C40; 2.754×10⁻¹²→3.258×10⁻¹²
  W, G40), and `ratio_abs_ext_raw` is pinned to 0.5128–0.5138 throughout —
  smooth enough that a margin already ≈374×–442× plausibly cannot flip
  from an interpolated point. But this arithmetic appears nowhere in the
  proposal; Idealization 9 asserts the conclusion, not the check.
- **The iso_xsec_sq convention-sensitivity direction, re-derived**:
  exp-087's own THERMODYNAMICS Phase-5 review (§8) found the *linear*
  (infinite-rod) convention gives LOWER `ratio_k` than the iso_xsec_sq
  convention currently in use (36.0°/38.6°/41.8°: 1.71/30.95/2.75 vs.
  actual 2.64/53.99/5.71) — confirmed by re-reading that file directly.
  So the disclosed ~1.5–2× convention sensitivity pulls AWAY from
  `RATIO_HIGH=10`, not toward it; it is not a classification-flip risk
  for this cycle's predicted bands, contrary to what I initially
  suspected before checking.

## Steel-man (≤150 words)

The R13 floor gate is implemented exactly as R13's text requires: a
pre-filter on `resolved_ratios` (an angle failing it is excluded and
reported as `NODE-UNRESOLVABLE`, never silently scored), leaving
`classify_resolved()`'s own bucket logic — and its already-validated
synthetic-recovery check — untouched. Every number behind it is
desk-computable from already-committed exp-083/exp-087 JSON, and I
independently reproduced all of it exactly, including the arithmetic
that resolves θ=38.6°'s reclassification. The 8-call bracketing design is
genuinely the cheapest, most decisive test of the node-artifact question
on the board, reuses exp-087's gated pipeline verbatim, and pre-commits
falsifiable bands (Q4) wide enough to be honest about a linear-trend
method's own known ~7% bias, not narrowed to manufacture a clean result.

## Sharpest attack (≤150 words)

Idealization 9 skips P8/NETD at the two new angles on an *argument*
("would not plausibly move a margin already ≈374×–442×") rather than a
computation — the exact shape R8 exists to forbid, and here the affordable
check is not merely affordable, it is free: §1 states the cycle reuses
exp-087's "thermo-chain pipeline, verbatim," and `frac_p_abs` (this
cycle's own PRIMARY input) already requires computing `p_abs_w` for both
configs at both new angles via `absorbed_power_established_ratio`. P8 is
two more already-gated (stage 15) function calls on numbers already in
hand — cheaper than the R13 floor gate this proposal *does* include. I
independently confirmed the underlying physical premise holds (§ above),
but that confirmation isn't in the document, and a desk check on
exp-087's old data cannot certify the new angles specifically — the whole
reason 8 fresh FDTD calls are being spent.

## Verdict: support-with-changes

## Flip-to-support parameter

Add `mixed_length_scale_regime`→`netd_disposition` calls at θ=38.4°/38.8°
(both configs) in Phase 4, reusing the `p_abs_w` values already computed
for `frac_p_abs`, and report `dt_ss_full_K`/margin/classification
alongside P7 in `results.json` — zero new FDTD, marginal cost near zero.
Secondary, non-blocking: also extend the `ratio_abs_ext`-vs-T9-anchor
(0.51) cross-check to the two new angles (free from the same
`widths_by_cell` data) — exp-087's own Phase-5 called this "worth logging
against T9," and it generalizes the check the last cycle only established
at 3 points.
