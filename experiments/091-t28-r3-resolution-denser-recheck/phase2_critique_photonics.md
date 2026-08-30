# PHASE 2 — CRITIQUE · PHOTONICS · Panel Iteration 68 · exp-091

## Steel-man (≤150 words)

This is a well-targeted resolution check precisely because it probes optical
response where angular sensitivity is worst. `VALIDATION.md`'s own lesson is
that this bench's λ/20 grid staircases boundary structure as a matter of
course, and staircasing bites hardest exactly where a curve is steepest or
nearest a node — which is exactly where 40.2°/41.4° sit (0.065°/0.061° from a
real `delta_scene` zero-crossing). Testing there, rather than at a
comfortable mid-band angle, is the harder, more honest test, not a softer
one. The geometry rescale is done correctly for an optical check: physical
size is held fixed (`L_GEOMETRIC_M` identical at both `cpl`), so any drift in
`frac_contrast`/`delta_scene` under `cpl` 20→30 is cleanly attributable to
grid/dispersion effects rather than a smuggled geometry change — a legitimate
way to separate a real angular feature from a discretization artifact, R3's
own founding purpose.

## Sharpest attack (≤150 words)

The reused P-069-5 `[0.3,3.0]` band was derived from `C80−C40` — an
`ABSORB`-depth, graded-loss-boundary reflectance-magnitude delta. `G40−C40`
is a proven different animal (exp-076, independently re-derived from
`fdtd2d.py`'s source): `PAD` is lossless vacuum, so this whole signal is a
coherent propagation-phase/round-trip-timing effect, not a magnitude change.
A magnitude-ratio band built for a reflectance-depth quantity does not
transfer to a phase-round-trip quantity: numerical (Yee-grid) dispersion
error is angle-anisotropic and accumulates over the *longer* physical path
`PAD` itself creates, so `cpl` 20→30 can shift a phase-timing signal's
*location* (moving the true zero-crossing) rather than scaling its
magnitude — my own seat found exactly this failure shape at P-069-5's own
near-null cells (exp-069, phase5_review_photonics.md §4): a resolution-driven
phase shift near a node produces a large ratio under this same wide band
while telling you nothing about genuine feature stability. §4a tests only
magnitude ratio at 40.2°/41.4° — both chosen *because* they're near-node —
so it can CONFIRM while the crossing itself has silently moved, or REFUTE on
an ordinary dispersion artifact indistinguishable from a real effect.

## Verdict: support-with-changes

## Parameter that would flip my verdict

Add a location-sensitive companion test alongside §4a's magnitude ratio: at
minimum, report whether `delta_scene`'s locally-interpolated zero-crossing
angle (using the R3-leg's own three points) shifts by more than half the
0.2° grid step relative to the native-`cpl` crossing location — not just
whether the magnitude ratio at the fixed sampled angles stays in `[0.3,3.0]`.
Without that, a CONFIRM on §4a is compatible with exactly the phase-shift
failure mode my own seat already documented for this identical band at
P-069-5, and a REFUTE is not distinguishable from ordinary numerical
dispersion.
