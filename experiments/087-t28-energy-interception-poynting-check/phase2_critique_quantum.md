# PHASE 2 — CRITIQUE · QUANTUM OPTICS · Panel Iteration 64 · exp-087

## Steel-man

This is a genuine measurement, not another desk exercise: it reuses the
already-validated `PAIR_PAD` article-loaded geometry and the already-gated
`sections.widths()` Poynting ledger, combined for the first time, at a
disclosed 12-call subset. It discharges the fifth-deferral tripwire the
honest way — building the instrument — rather than arguing around it.
The idealizations section is unusually forthcoming for this exact failure
class: #6 and #8 admit outright that the ratio_k decade bands and the 3×
box_dev multiplier are "house-style," not derived confidence intervals,
and P3's disclosed (non-gating) box-independence check gives real,
inspectable noise-floor context rather than asserting one. The UNRESOLVED
category means an angle that fails to clear noise is excluded, not
silently folded into a headline number — the correct instinct after R11.
Framing the P5 outcome as corroborative-not-dispositive is honest given
n=3.

## Sharpest attack

The classification is not falsifiable as specified at its own edge case.
With only 3 angles and an unvalidated 3×box_dev gate (Idealization 8: "not
a formally derived statistical significance threshold"), §4-P5 never
states what happens at 0 or 1 resolved angles. At exactly 0 resolved, the
universally-quantified definitions of ENERGY-DECOUPLED ("<0.1 at every
resolved angle") and CONSISTENT ("0.1–10 at every resolved angle") are
BOTH vacuously true simultaneously — an undefined, contradictory state the
document doesn't anticipate. Since §7 claims the tripwire discharges
"regardless of which classification... the data return," a degenerate
all-UNRESOLVED run — plausible if `box_dev` swamps the true G40−C40
absorbed-power delta — still gets credited as full discharge: the exact
silent/thin-deferral shape the tripwire exists to catch, relocated from
cycle-skipping to instrument-degeneracy. Nothing in this proposal — no
synthetic ground-truth injection (R6), no null-permutation control (R5) —
establishes that the 3× multiplier or the "≥2 of 3" majority rule actually
discriminates signal from noise at n=3, rather than passing or failing by
construction.

## Verdict

**Support-with-changes.**

## Flip-parameter

Add, before any FDTD call: (a) an explicit disposition stating that 0 or 1
resolved angles is NOT a valid tripwire discharge and must be reported as
such, not folded into "regardless of classification"; and (b) a minimal
synthetic check — inject a known `frac_p_abs`/`frac_contrast` pair at each
of the three decade-boundary values (0.1, 1, 10) into the same pipeline
and confirm the gate/classification recovers the correct bucket — before
`box_dev`'s 3× multiplier and the "≥2 of 3" rule are trusted to mean
anything at n=3. That single addition would move me to full support.
