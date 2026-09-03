# PHASE 2 — CRITIQUE · Panel Iteration 82 · Seat: ELECTROMAGNETISM
## exp-105 candidate — "The T8 r=78/156/312 Bridge, Extended to the Coherent Point/Region-Intensity Channel"

*Blind to other seats' current-cycle critiques, per PANEL.md. Verified
directly against `experiments/030-scale-bridge/design_geometry.py`,
`experiments/103-t28-gateb-footprint-aperture-match/run.py`,
`experiments/104-t28-subnyquist-standoff-recheck/run.py`,
`lab/sections.py`, `lab/materials.py`, and LOGBOOK.md Iterations 1, 7, 8
(T8/T9/T13/T14 full transcripts) before writing this.*

## T1 / passivity-reciprocity-causality bookkeeping — clean

No σ/ε/μ physics is touched. `graded_black_shell(sim, cx, cy, r_in, r_out,
sigma_max, eps_max=1.0)` (`lab/materials.py:74`) is a real, non-negative,
non-dispersive conductivity ramp on an ε≈1 host — confirmed directly in
code. `sigma_max(κ)=0.5/κ` stays strictly positive at every κ tested (1,
2, 4), so passivity (σ_e≥0, no gain) is preserved trivially; this is
exactly T8's own already-adopted, already-audited rescale (Red Team,
Iteration 7, mandatory fix 2), reused verbatim here, not a new material
claim. Reciprocity is not engaged either way — this is a single-source,
forward-transmission-only bench (no source/observer-swap test is run, at
T8's founding cycle or here) — moot, not satisfied, the same honest
framing I gave T8's own PEC non-monotonicity at Iteration 7 Phase 5.
Causality is likewise moot for a steady-state phasor instrument, not
"satisfied" — worth restating since this cycle inherits that same
instrument class unchanged. **My T8-founding finding holds again: a
measurement-geometry rescale of an already-passive lossy dielectric is
T1-inert.** N/A is the correct disposition.

## The z/z_R formula and forced 4:2:1 ratio — reproducible in shape, NOT in the stated numbers

The proposal's `z_over_zr(r) = 77·20/r²` formula, independently
re-executed: at r=78/156/312 this gives **0.2531 / 0.0633 / 0.0158** —
not the §5 Idealizations' own stated **0.0253/0.0063/0.0016**, a uniform
**10× error**, and that triple doesn't even self-consistently match §5's
own separately-stated range `[0.0026,0.041]` (neither its min nor its max
matches either the 10×-off triple or the correctly-computed one). This
number is absent from both Appendix scripts — unlike every other figure
in this document (which the proposal itself claims, correctly, is R4-
discipline "no hand-typed figure"), the z/z_R values are hand-typed and
unverified by the document's own stated verification process. **The
4:2:1 shape ratio itself IS a real, reproducible geometric necessity**
(verified: `x(r)∝1/r` regardless of the 77-cell constant, so P3/P3b's
2.00±0.3 / 4.00±0.5 discriminator bands are sound) — but the "narrower
and shallower than T8's original span" and "1.4–2.4 decades short of
witness" claims built on the wrong absolute numbers should be recomputed
before this document is cited again.

## Steel-man (150 words)

A genuinely disciplined re-derivation: every geometry/material constant
traces to T8's own printed formula chain, cross-checked bit-exact against
an independently-built family (R4, exp-069) at the one scale they share —
real, load-bearing corroboration, not coincidence. The `kappa_window`/
`kappa_region`/`delta_phi` machinery is reused byte-for-byte, isolating
exactly one variable (object/domain scale) the way T8's own Block 1
isolated z/z_R from optical-depth drift. Gate P0's κ=1 ground-truth
recovery and Gate P1's <1e-9 identity check are the right proactive
precondition discipline (R6/R15 lineage), not post-hoc rationalization.
Correctly declines to smuggle any constraint-3/4 perceptual claim from a
raw intensity ratio, and names T13/T14 engagement honestly as a
cross-channel replication test, not a resolution claim. The cost-gating
rule for r=312 (pilot-then-decide) is the right, disclosed response to
T8's own 8× timing miss.

## Sharpest attack (150 words)

The settling-adequacy argument (§5) borrows T8's P-VISION-S1 (STEPS
doubled, C unchanged to 5 decimals) from a *different bench, different
metric, κ=2 only* — disclosed, but the disclosure misses the sharper
problem: **this bench's own settling evidence exists and doesn't cover
the channel that matters.** exp-103's own settling leg (mandatory
EM/Red-Team fix, `STABILITY_TOL=0.20`) checked `kappa_region_wide`
only — never `kappa_region_point`/`delta_phi_point`, the zero-averaging,
single-cell phasor reading this cycle's own P4 (ripple generalization)
runs directly on at the new, unconditionally-committed r=156. A residual
settling transient in that literal single-cell channel is
indistinguishable, in P4's own sign-change test, from a genuine
sub-Nyquist ripple — an unverified settling assumption directly confounds
the metric it's being used to validate. No settling check on this channel
exists anywhere in this program's history, at any r.

## Verdict: **support-with-changes**

## Flip condition

Add one mandatory doubled-STEPS settling check on `kappa_region_point`/
`delta_phi_point` specifically (not `kappa_window`) at r=156, gating P4's
verdict before it is trusted — two more real FDTD calls at the cheapest
committed scale, symmetric with exp-103's own already-adopted settling
discipline for the wide channel. Absent that, P4's r=156 "P2 FALSIFIED
again" reading should be reported provisional.
