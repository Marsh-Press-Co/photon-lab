# Phase 2 Critique — MATERIALS & METAMATERIALS

*Blind review of Panel Iteration 75's Phase-1 proposal (ELECTROMAGNETISM,
lead). T28 house-discipline/validation cycle — no new mechanism or
material claim this cycle; critique applies discipline-lens scrutiny to
what the proposal's results could actually establish, per the assigned
charter note.*

## Steel-man (≤150 words)

Item (i)/(ii)'s design is disciplined: the ±0.500° half-width is the
*same* number exp-096's desk bound already Red-Team-ratified against the
three known cpl20→cpl30 migration shifts (−0.193582°/+0.320166°/
+0.376752°, `experiments/092-.../results.json::rank1.crossing_report`),
reapplied rather than re-derived (R4 discipline), and the 4-point quartile
spacing is finer than the largest known shift so a real crossing can't
hide between two same-sign samples the way exp-095's ±0.1°/2-point design
did. Idealization 17 is carried forward and stated plainly: a family-wide
`r{n}_config()` recipe defect isn't distinguishable from independent
per-family bugs by (i)/(ii) alone — the proposal doesn't hide this. Item
(v) finally schedules PHOTONICS' 10-cycle-overdue grazing check via
MATERIALS' own governance ask (exp-097), correctly scoped as zero-FDTD and
honestly self-limited (Idealization 49: cannot distinguish "model invalid"
from "mechanism vanishes").

## Sharpest attack (≤150 words)

The proposal frames (i)/(ii)'s outcome as "genuine node migration [vs] a
family-wide cpl=40 recipe defect" — a false dichotomy from MATERIALS'
lens. I verified in `experiments/069-.../design_geometry.py`: `cpl` is
cells-per-wavelength grid density (`CPL={450:15,600:20,750:25}`), and
R3/R4/R5 hold the *physical* geometry fixed while scaling cell counts by
`RATIO` (`L_GEOMETRIC_M_R5` "bit-identical to native/R3/R4," per exp-095's
own table). A fabricated shell has exactly one null angle — cpl is not a
manufacturing parameter, it's mesh density. So even the "genuine
migration" branch is not a materials finding: it's evidence the
discretization hasn't converged by cpl=40, not evidence about the
continuum angle a real device would exhibit. Nowhere in (i)/(ii)/(v) is a
convergence-order estimate computed from the now three-resolution shift
history, despite the shifts being non-monotonic in sign
(−0.194°/+0.320°/+0.377°). The whole exercise can PASS-family-clean and
still tell MATERIALS nothing about where the real null sits.

## Verdict

**Support-with-changes.**

Separately flagged, not verdict-determining: this is the fifth
consecutive Panel Iteration (71–75, exp-094 through this cycle) with T1
route N/A / Checkpoint criterion 2 N/A and zero FDTD evidence bearing on
a realizability parameter — the Iteration-7 UNOBTAINIUM shell-thickness
figure (0.31–0.92 m at witness scale, LOGBOOK.md:9826) is untouched since.
Worth a governance check at Phase 3/5, not grounds to oppose a cheap,
correctly-scoped instrument-hygiene cycle.

## Flip

Add, as a zero-marginal-cost addition to items (i)/(ii)'s report dict: for
each of the four nulls now measured at cpl=20/30/40 (three already exist
per null; item (i) supplies cpl=40), compute the pairwise shift ratio
(cpl20→30 shift ÷ cpl30→40 shift) as a local convergence-order proxy and
report whether it is consistent with the FDTD scheme's expected O(Δx) or
O(Δx²) decay. That turns "migration: genuine vs. defect" into an actual
(even if rough) Richardson-style estimate of the continuum null — the
number a realizability bound would need — rather than a binary that,
either way it resolves, stays silent on where a real device's null sits.
