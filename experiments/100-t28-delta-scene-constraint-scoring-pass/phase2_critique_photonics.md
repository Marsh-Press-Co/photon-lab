# Phase 2 Critique — PHOTONICS

## 1. Steel-man

This is the first T28 cycle to screen `delta_scene(θ)` against an actual
optical-detectability instrument (VISION's frozen `C_thr(L)`) rather than
run another zero-FDTD mechanism hunt — ten-plus prior cycles measured this
oscillation without ever scoring its magnitude against a perceptual bar.
Spending the 16 new calls on the four already-located `cpl=20` crossings
(exp-090) is efficient: it puts new FDTD exactly where sign, local slope,
and floor-margin are already characterized (R15/R17), rather than probing
blind. Scoping Leg A strictly to the already-tested 36°–43° window
(Idealization 64) is correct discipline, given T21's own established
grazing-incidence amplitude blow-up outside that band. Idealizations 62/63
correctly pre-empt an inflated-correlation misread by flagging that
`frac_p_abs` and `delta_scene` share the same four FDTD calls.

## 2. Sharpest attack

Tier 2 Leg A scores `|delta_scene(θ)|` against `C_thr(L)` using only the
λ=600nm dataset (Idealization 1), and its "weak-to-moderate lean: stays
below 0.005" verdict carries no wavelength caveat beyond the disclosed
angle-window scope (Idealizations 64/66). But this same bench already has
a directly analogous, structurally similar oscillatory confound in the
identical 36°–43° window: T21's own edge-diffraction fringe measured
0.0237 at 750nm/θ=40° — 4.7× `C_thr` — while reading comparatively benign
at 600nm, a wavelength T21's own Phase-5 record attributes partly to a
grid/Nyquist coincidence specific to 600nm. Nothing in this proposal tests
whether `delta_scene`'s own amplitude is similarly λ-dependent, so a
single-wavelength PASS lean cannot bound the white-light contamination
risk the actual phenomenon (a flashlight) requires. No idealization here
names this specific, on-file precedent as an open risk — an omission, not
a disclosed gap.

## 3. Verdict

**Support-with-changes.**

## 4. Parameter change that would flip to full support

Add an explicit idealization, alongside 64/66, scoping any Leg A PASS/lean
as λ=600nm-only and naming T21's 750nm/4.7×`C_thr` precedent as an
untested wavelength-generality risk specific to `delta_scene` — i.e.,
require that any Tier A/Tier W disposition drawn from Leg A state this
caveat inline, mirroring the discipline Idealization 64 already applies to
the angle-window scope.
