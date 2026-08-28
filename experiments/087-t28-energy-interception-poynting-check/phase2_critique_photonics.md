# PHASE 2 — CRITIQUE · PHOTONICS · Panel Iteration 64 · exp-087

## Steel-man

For a rotationally-symmetric graded-shell absorber, ray/geometric optics
predicts σ_abs/σ_ext is angle-invariant — a circle's projected cross-section
doesn't change with illumination direction (Iteration 1's own parameter
table already notes this for the PEC control). That makes this a genuinely
well-posed test: any real θ-dependence recovered inside 36–42° is *evidence
of a wave/near-field effect*, not absorber physics changing — exactly the
class of signal this program's whole T28 hunt has been chasing for 18
cycles, now for the first time measured on an energy channel instead of a
Weber-contrast channel. Reusing the already-suite-8-gated `widths()`
verbatim, on the already-validated C40/G40 geometry, at a disclosed,
cheap 3-point subset is a defensible first move to ask a genuinely new
question (does the confound show up in absorbed power at all) without
over-committing FDTD spend before knowing whether it's worth denser
sampling.

## Sharpest attack

The 3-point grid (36°/39°/42°) is spaced exactly 3.0° apart — within 5–7%
of the ONLY two periods this exact scene/window has ever produced on any
channel: `P_edge_A=2.8421°` (exp-069) and Branch B's `P*=2.9474°`
(exp-083), both driven by domain/boundary-echo artifacts intrinsic to this
bench's empty-scene geometry, not absorber physics. `sigma_abs`/`sigma_ext`
are normalized by `i_inc`, a fixed-strip flux measured on the EMPTY run at
each θ — if that reference strip inherits even a fraction of the same
domain-echo ripple already proven to live in this window's empty-scene
quantities, a 3-point sample at near-exactly that period is positioned to
either alias it into a false "smooth trend" or cancel it into a false
"flat/decoupled" reading, and P5's classification can't tell which,
because `box_dev` only probes box-size sensitivity at fixed θ, never
θ-domain aliasing. The proposal's own P4 "genuine uncertainty" framing
undersells this: given ray-optics predicts zero θ-dependence here, ANY
recovered θ-trend is more likely this well-documented artifact family than
new oblique-incidence physics — and 3 points can't distinguish the two.

## Verdict

**support-with-changes.**

## Flip-parameter

Replace the 3-point {36°,39°,42°} grid with a non-3°-spaced subset (e.g.
{36.0°, 38.6°, 41.8°} or any spacing that avoids near-integer multiples of
~2.84–2.95°), or add a 4th point off that lattice — enough to distinguish a
real monotonic oblique-incidence trend from an aliased echo artifact.
Either change would flip my verdict to support.
