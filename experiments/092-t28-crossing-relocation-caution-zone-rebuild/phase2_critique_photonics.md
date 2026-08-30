# PHASE 2 — CRITIQUE · PHOTONICS · Panel Iteration 69 · exp-092

## Steel-man (≤150 words)

The §2a framing is optically sound at its core: `PAD` is independently proven
lossless vacuum (exp-076), so `delta_scene` is a coherent phase/round-trip-
timing signal, and Yee-grid numerical dispersion is exactly the kind of
`O((Δx/λ)²)` phase-velocity error that relocates an interference null without
touching passivity or reciprocity — a sign flip under `cpl` refinement is the
expected signature of that class of error, not a red flag. The net itself is
cheap and well-disciplined: every new angle is an exact `DENSE_ANGLES` member
(verified: 39.6°/39.8°/40.0°/41.8°/42.0° are all exact grid points, giving a
free `cpl=20` comparator at each), the arithmetic checks out (the naive
40.04°/41.69° extrapolations reproduce exactly from `results.json::a2.per_pair`;
`sigma_max_R3=78/(2·117)=1/3` is correct), and the design honestly carries a
REFUTE/NEITHER outcome path rather than forcing a CONFIRM narrative.

## Sharpest attack (≤150 words)

§2a's justification for an *asymmetric, outward-biased* net conflates two
independent measurements. A zero-crossing of `f(θ)` is invariant under a pure
amplitude rescaling `f→kf` — vertical amplitude growth carries zero
information about whether a null moves outward, inward, or stays put. So
citing EM's `2.8×–5.2×` `frac_contrast` inflation (a magnitude finding, at
three angles none of which are the crossings themselves) as corroborating a
"widening lobe" (a horizontal, shape-side claim) is a non sequitur — it
borrows plausibility from an unrelated measurement. The evidence that
actually bears on shape — exp-091's own ordering-check failure ("genuinely
reshaped... not merely phase-shifted") — is equally compatible with a rigid
shift *larger* than the naive 2-point secant predicts, a new node appearing,
or asymmetric distortion, none of which "widening" privileges. Because the
net's width is derived from this narrative, and the upper window is already
pinned against the hard `DENSE_ANGLES` edge (42.0°, no off-grid extension in
scope), a wrong shape-model risks an undersized net exactly where recovery
this cycle is impossible.

## Verdict: support-with-changes

## Parameter that would flip my verdict

Extend the lower net two more (already-on-grid, ~4-call) points to 39.2°/39.4°.
The lower crossing has *direct* evidence of a shift larger than the naive
estimate (40.2° itself already flipped sign, from −1.54×10⁻⁴ to +4.37×10⁻⁴ —
a jump comparable in size to the entire 40.0°→40.2° approach at `cpl=20`),
unlike the upper crossing, which rests only on extrapolation from a bracket
that never itself showed a sign change. Hedging the side with stronger,
measured (not extrapolated) evidence of a large relocation is cheap and
directly addresses the attack above; without it, a REFUTE on the lower window
cannot distinguish "the net was correctly sized but wrong-shaped" from "the
net was simply too narrow."
