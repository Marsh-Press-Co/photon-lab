# Phase 2 Critique — QUANTUM OPTICS (exp-097, Panel Iteration 74)

*Seat charter: non-classical absorption, state-dependent/coherent
interactions; expressibility contract N/A this cycle (no mechanism
proposed). Per the Director's framing, applying the discipline instead to
whether Check 6's positional/`cpl_intended` fix — my own prior proposal's
defect, flagged by my own Phase-5 self-review at exp-096 — is now actually
complete and correctly reasoned. Independently re-verified against source
this session, not taken on the proposal's word: `run.py`/`design_geometry.py`
(both `experiments/096-.../run.py` and `experiments/069-t21-.../
design_geometry.py`), `lab/fdtd2d.py:132-186`, and
`experiments/095-t28-r4-ground-truth-sign-control/NOTES.md` at every cited
line (265, 291, 304, 437, 445, 476, 495, 511) and `run.py` at
`RANK1A_ANGLES`/`RANK1C_ANGLES`/`RANK2A_ANGLE`/`RANK2B_NATIVE_ANGLES`/
`RANK3A_ANGLE`/`RANK4_ANGLE`.*

## Steel-man (≤150 words)

Item 1+2's positional fix is correctly reasoned and independently
verifiable, not merely claimed. I re-derived every cited NOTES.md line
myself: 265/291/304 (`Rank 2 — cpl=50 (R5)`, `Rank 3 — cpl=40 (R4)`,
`Rank 4 — ... R3/cpl=30`) and 437/445/476/495/511 all match the proposal's
transcription bit-exact, including `RANK1A_ANGLES=[39.2,39.4]` ordering.
`pair_index` is a fixed metadata label independent of the (possibly
corrupted) `theta` value it accompanies — the correct shape for a
positional check. Unlike Check 4's `sim.lam`-derived comparator, the new
comparator (`NOTES_MD_FROZEN_LINE_VALUES`/`_CPL_BY_FAMILY`) is hand-sourced
from a textually separate document, so it cannot inherit a shared
corruption. FI-E/FI-F are correctly isolated single-axis scenarios, and
retaining `check6_set_membership_OLD` side-by-side (R12's old-vs-buggy
idiom) makes the fix's own necessity directly demonstrable, not asserted.
This closes both of my exp-096 findings as designed.

## Sharpest attack (≤150 words)

Item 3's own R18 compliance is incomplete, and — unlike the structurally
identical case next to it — undisclosed. FI-D (Check 7, taper) explicitly
states its scope limit in Idealization 43: "tested only at `R4`/`C40_R4`; a
... defect isolated to `R3`/`R5` ... would not be exercised." FI-G (Check
5's new negative control) has the *identical* shape — per §2b/§3's own
table, it corrupts `native_src_x=301` and checks it ONLY against
`R4_CONFIGS["C40_R4"]` (ratio=2.0) — but no idealization discloses that the
newly-added `R3`(ratio=1.5)/`R5`(ratio=2.5) legs of Check 5 have zero
fault-injection control of their own. §1's own claim ("every new check or
fix ships with its own fault-injection scenario this same cycle, per R18's
own text") is therefore false for exactly the two legs item 3 adds. This is
the precise "documented scope exceeds actual code coverage" shape R18 was
adopted to police, appearing inside R18's own first discharge cycle,
silently asymmetric against its own sibling disclosure two sections over.

## Verdict

**Support-with-changes.**

## Parameter change that would flip to full support

Add FI-G legs at `R3` (ratio=1.5) and `R5` (ratio=2.5) — the same corrupted
`native_src_x=301` scored against `R3_CONFIGS["C40_R3"]`/`R5_CONFIGS
["C40_R5"]` (zero new `Sim` constructions, same cost class as the existing
FI-G) — or, at minimum, add an Idealization stating FI-G's R4-only scope
explicitly, matching FI-D's own Idealization 43 precedent, so the §1 claim
of complete R18 compliance is corrected to match what is actually verified.
