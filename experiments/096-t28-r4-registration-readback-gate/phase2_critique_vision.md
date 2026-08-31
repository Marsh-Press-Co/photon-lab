# Phase 2 Critique — VISION SCIENCE (blind)

*Panel Iteration 73, exp-096. T1 route N/A this cycle (pure
instrument-validation, matching every T28 desk cycle since exp-069), so
this seat's numeric-threshold-pinning duty is N/A. Applying this seat's
other established strength on this sub-thread: a completeness/legibility
check of the document itself.*

## Steel-man (≤150 words)

This is the right check, designed the right way. It closes the single
most-cited-but-never-run gap in 19 cycles (Gate 5 validates `sigma_e`,
never `angle_deg`/`sim.lam`/the phase array) at a genuine zero FDTD cost,
and it does not stop at building a check — §2b gives it a real positive
control with **three independently-constructed fault-injection scenarios**
(family/`cpl` swap, angle swap, sign flip), not one, specifically because
a single injected defect could only demonstrate one of three failure
axes. FI-C is the sharpest design choice in the document: it exists
precisely to defeat a magnitude-only comparison, which a lazier version
of this check would have used. §5a's no-lean framing is honest given the
sub-thread's own record, and the 8-point representative set's C/G-pair
coverage gap (checking one member per pair, not both) is explicitly
disclosed rather than smoothed over, with Phase 4 given the cheap option
to close it.

## Sharpest attack (≤150 words)

The document violates its own stated house rule. §6 closes with: "the
carried idealizations banner (mandatory at both this section and §5, per
the Iteration-65 CHECKPOINT's non-discretionary rule)" — but §5
("Predicted outcomes") never actually carries it. §5a/5b/5c cite
individual idealization numbers inline (32, 36, 37) but nowhere states
the governing-banner sentence itself (the "every prediction below is
governed by Idealizations X/Y/Z" line exp-095's own Predictions section
opened with, per this exact rule). This is not a nitpick: the
Iteration-65 CHECKPOINT text is explicit that "a banner scoped to one
section does not propagate to the other," and a recurrence of exactly
this shape — once caught, once not — is what the standing
forward-elevating clauses in this sub-thread (R15/R16/R17) exist to
escalate. Secondarily, §1's mechanism/instrument narrative runs 335
words against PANEL.md's own Phase-1 spec of "≤300 words."

## Verdict

**support-with-changes**

## Flip-to-plain-support change

Add the missing "every prediction in §5 is governed by Idealizations
1/7/17/31–37" banner sentence to the top of §5, and trim §1 to ≤300
words, before Phase 3 freezes anything — both are zero-cost text fixes
that do not touch the design, the 8-point set, the fault-injection
table, or the desk bound.
