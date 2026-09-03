# Phase 2 Critique — ELECTROMAGNETISM

## Steel-man

T1 is genuinely N/A here — no absorbing/gain medium is varied, so there is
no live passivity or causality question this cycle creates. That makes
the census electromagnetically low-risk: `delta_scene≡c_g−c_c` differs
only in `PAD` (lossless vacuum, exp-076), so no run can produce a
non-passive or acausal artifact regardless of outcome. The cost law
(`cells∝ratio²`, `steps∝ratio` ⇒ `cost∝ratio³`) is exactly right for
CFL-limited explicit-timestep 2D FDTD held at fixed physical domain and
fixed simulated-time duration — a correctly-derived scaling argument,
notable given this program's own R4 history of hand-typed figures going
wrong. And the design honors "FAIL is a reported outcome": G0-FAIL routes
to escalation, not to quiet reinterpretation.

## Sharpest attack

G0 is billed as a "ground-truth-recovery gate" but tests no independent
ground truth. R6's own house rule requires injecting a KNOWN synthetic
effect and checking recovery; G0 instead checks whether R3, R4, and R5 —
three resolutions of the IDENTICAL ABSORB=40/PAD=40 boundary construction,
the very families whose mutual disagreement is the open question — happen
to agree in sign at one angle. With `delta_scene`'s own established
≈2.84–2.95° period, roughly half of any window already carries
sign-agreement between two independent phase-uncertain families by
construction; requiring a third to also agree, at a single pre-selected
point, is a weak filter dressed as a strong one. Worse: all three
families share the SAME systematic origin (finite-resolution PML/boundary
truncation of a lossless-vacuum-only signal) — agreement among
non-independent measurements of one converging (or non-converging)
artifact is not evidence the artifact is real diffraction rather than a
shared numerical residual. The `[0.5,2.0]` ratio band is this program's
established factor-of-2 convention (T9/exp-106 precedent) but has no
derivation here from FDTD discretization-error scaling — it is imported
by analogy, not re-justified for a 3-way, mutually-disputed comparison.

## Verdict: support-with-changes

## Flip condition

Replace G0's framing: drop "ground-truth-recovery," and require, in
addition to the existing sign/ratio test, that `delta_scene` at
`θ_anchor` also show the ratio-of-successive-resolution differences
consistent with a convergent (not merely agreeing) series — e.g.
Richardson-style `|Δ(R4,R3)|` vs `|Δ(R5,R4)|` shrinking with `cpl`,
not just three same-signed values — before the census's NEITHER-vs-
CORROBORATED branches are trusted as physics rather than as one more
data point in the shared-artifact hypothesis.
