# Phase 2 Critique — ELECTROMAGNETISM (blind)

## 1. Steel-man (≤150 words)

Items 1 and 2 are genuinely well-formed EM design. Item 1's asymmetric Null C
bracket is justified from the null's *own* measured cpl20→cpl30 shift
(`shift_vs_cpl20_upper=+0.320°`/`+0.377°`), not borrowed by analogy the way
item (ii) at exp-098 had to be — the strongest available R17 basis — and it
pre-registers a genuine third outcome (VANISHING-AMPLITUDE) with a disclosed,
non-formal decay heuristic (`r_i<0.5`) rather than an open-ended "try wider"
loop. Item 2's Rank 2b bracket is weighted toward the *doubly*-confirmed
downward shift direction and stepped finer (0.1667°) than the largest
established marginal shift (0.194°), so a real crossing cannot hide between
same-sign samples — the identical design discipline that found the
38.590230° crossing at exp-098. Item 3 reuses `ptp` with zero new formula and
correctly carries forward exp-098's own Phase-5 disclosure
(`gp2_vs_exp086_disclosure`) that GP2′ and `ptp` are two statistics on one
model, not independent instruments (Idealization 57) — the right frame, not
a new claim.

## 2. Sharpest attack (≤150 words)

Item 2 reuses `cell_metrics_r5`, whose `xi_ext`/`sigma_abs_nonneg` outputs
gate *hard* `assert`s (`assert xi_pass, "...HALT"`) in exp-095's own
committed Rank 2a/2b code — verified at source, `run.py` lines 769–777 and
846–854 — that fire *before* `settle_band` is even computed. `XI_TOL` is not
an R5 quantity: it is `exp094.XI_TOL`, itself chained from `exp093.XI_TOL`,
carried unchanged across three grid-density generations (cpl 30→40→50) and
never once evaluated against real field data at cpl=50, since R5 "has spent
zero real FDTD calls anywhere" until this cycle. Yet §4's Predictions table
has no row, band, or lean for `xi_ext`/`sigma_abs_nonneg` at either Rank —
only `settle_band` is predicted for Rank 2a. A first-ever-resolution assert
crash (mid-Rank-2a-or-2b, pre-`results.json`, exp-098's own recent failure
shape) is a live, unpriced outcome this proposal's own frozen predictions
say nothing about.

## 3. Verdict

**support-with-changes**

## 4. Parameter change that would flip to oppose

None needed to flip to oppose — this is fixable without re-scoping the
cycle. If the Director declines to add a predicted `xi_ext`/`sigma_abs_nonneg`
row (or at minimum an explicit "HALT is a live, undisclosed outcome" caveat)
to §4 before Phase 4 code is frozen, and Rank 2a/2b then HALTs on this
un-pre-registered gate, this verdict should be read as retroactively
oppose — an EM-owned energy-bookkeeping gate firing for the first time,
unpredicted, on the cycle's own first real R5 spend.
