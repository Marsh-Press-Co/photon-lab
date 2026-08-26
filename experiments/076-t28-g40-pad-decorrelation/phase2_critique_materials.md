# Phase 2 Critique — MATERIALS & METAMATERIALS

**Cycle: exp-076 (Panel Iteration 53), G40/`PAD` decorrelation.** Reviewed
independently (blind to other seats' critiques), against the committed
`phase1_proposal.md`, `g0e_amplitude_channel_check.py`/`_output.json`,
`experiments/065-.../design_geometry.py`/`_output.txt`,
`experiments/069-.../design_geometry.py`/`results.json`, and
`experiments/072-.../run.py`/`results.json`. All load-bearing numbers below
were independently re-derived by me, not taken from the proposal's prose.

## Steel-man (≤150 words)

This is a cleanly-scoped instrument build. I re-ran
`experiments/065-.../design_geometry.py` from scratch: §2a's table (`G40`:
`NX=440, NY=1664, SRC_X=340, PLANE_X=117, OBJ_Y=832, y_lo=80, y_hi=1584,
A=752, aper=1504, D_SP=223`) reproduces bit-exact, and the `clrPl`/`clrSrc`/
`clrSpan` deltas versus `C80` are correctly attributed to `ABSORB` thickness
alone (clearances are measured *from* the band edge, so a thinner band at
identical domain size mechanically opens more clearance) — not a
construction defect. I re-ran `g0e_amplitude_channel_check.py`: identical
`1.0255e-4`/`8.346e-3` worst-case recovery errors, `PASS`. Both baseline
`amp_ratio` figures (0.161/0.041/0.020/0.166) reproduce exactly from
`exp-072/results.json`. Most relevant to my charter: the 31-call budget
faithfully executes my own exp-072 claim's actual basis — one fresh `G40`
build on exp-069's already-committed `C40`/`C80` grid at T27's settled
`STEPS=2800`, explicitly declining to reuse exp-065's own stale
`STEPS=1400` `G40` legs (Idealization 4).

## Sharpest attack (≤150 words)

The document never once states that `ABSORB` and `PAD` are the same
representational class — both pure `Sim(absorb=...)`/domain-padding
numerical constructs of a matched-`eps=mu` boundary, "not a statement about
realizable coatings" (my own Phase-2 finding, exp-075, standing this exact
sub-thread). I grepped all 427 lines: zero occurrences of "material" or
"realiz" anywhere. Yet §4's decision language breaks that symmetry: a
"reassuring" outcome makes prior readings "substantively `ABSORB`-depth-tied,
not an artifact of the padding construction" (§4a), while the alternative is
framed as failing to be "physically tied to the graded boundary's absorption
depth" (§4b) — language that implies `ABSORB`-tied carries physical standing
`PAD`-tied lacks. It does not; both are boundary-condition knobs of identical
status. This is the exact unlabeled-physicality creep my charter exists to
catch, and it is missing precisely the caveat exp-071's own mandatory-fix
docket item 4 required on *every* Combined-Verdict branch of this sub-thread.

## Verdict: **support-with-changes**

The instrument, budget, and geometry are sound and independently
re-verified; the gap is textual, not numerical, and cheap to close before
Phase 3 freezes §4's branch language.

## Single parameter change that would flip my verdict to unqualified support

Add one explicit sentence to §4, applied uniformly to both branches (a) and
(b) — e.g. "`ABSORB` and `PAD` are both pure numerical FDTD boundary-
condition parameters (`Sim`'s graded damping-mask thickness and domain
padding, respectively); neither reading in this section is a realizability
or material claim, and `ABSORB`-tied carries no more physical standing than
`PAD`-tied" — mirroring exp-071's own precedent of appending this caveat
uniformly across every Combined-Verdict branch, not just the top-level §1
narrative.
