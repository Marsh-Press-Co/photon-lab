# PHASE 2 — THERMODYNAMICS CRITIQUE · Panel Iteration 87 (candidate exp-110)

Fresh sub-agent, blind to every other seat's critique this cycle. Read
PANEL.md, LOGBOOK.md in full (including the R1-R26 RULED OUT registry and
the T28 live thread, Iterations 83-86), the Phase 1 proposal, and its
subject code (exp-108's `run.py`, `analyze.py`, `chunk_runner.py`,
`NOTES.md`, `results.json`, `analyze_output.json`) before critiquing.

## Steel-man

Item 1 carries zero energy-ledger risk — confirmed independently, not
assumed. `reproduction_precondition()` (exp-108's own code, reused
unmodified) checks only `sigma_abs`/`sigma_ext`/`abs_ext_ratio` against
exp-106's already-committed values as a REPRODUCTION gate, an established
discipline, not a new absorbed-power claim; the mirror-symmetry floor gate
and `classify_item_i_local` operate purely on σ_scat-per-bin angular-
pattern magnitudes (item 1b's own `raw_patterns` fields) and never touch
`ledger_check`, `closure`, or `core_frac` anywhere in the parameter table.
Item 1 is explicitly scoped INFORMATIONAL, not folded into item i's frozen
CONFIRM — correctly avoiding the exact R24 shape (a new instrument
silently reclassifying a verdict same-cycle). T1: N/A is correctly,
structurally true. Also encouraging: exp-109 already shipped
`build_result_text(..., wall_time_source=None)` for the precise purpose
this cycle needs — the tool to prevent historical-spend conflation is
already one line away from correct use.

## Sharpest attack

The cost gate is asserted, not wired. `COST_GATE_PILOT_S`/
`COST_GATE_TOTAL_S` (`run.py:63-64`) are defined once and referenced
NOWHERE else in exp-108's code — not in `chunk_runner.py` (item 1a's
literal, unmodified executor), not in `analyze.py`, no assert, no halt.
Iteration 83's own r=312 defer happened by a human reading printed
per-chunk wall times and manually stopping; nothing in the codebase would
stop a run that blew the budget. Idealizations claims "if the r=312 pilot
exceeds it, that leg defers... reported NOT-RUN, not silently skipped" — a
checkable consequence with zero code anywhere in this document's own
parameter table (items 1a-3) to enforce it, despite that same table
specifying exact function signatures elsewhere. This is precisely the
R23/R24/R25 "claimed-but-unwired consequence" shape this program's own
registry exists to catch — on the exact gate this critique cycle was
tasked with checking.

## Verdict

**support-with-changes**

## Flip condition (optional)

Wire the cost gate as a real, code-level check: after the r=156 pilot leg
completes, sum its measured wall time (already printed per-chunk by
`chunk_runner.py`; item 1b's `analyze.py` should capture and total it) and
compare against `COST_GATE_PILOT_S`/`COST_GATE_TOTAL_S` with an explicit
`if/assert` that either proceeds to the r=312 calls or halts and writes an
explicit `r312_deferred=True` field into `results.json` — turning the
prose promise into an executable, checkable gate, matching every other
item in this proposal's own parameter table.

## Additional finding (informational — does not change the verdict)

**Wall-time-attribution risk, same channel as Iteration 86's own finding.**
Item 1a is a genuine re-capture (6 new `Sim.run()` calls) — its own new
wall time is NOT exp-108's already-baked-in `total_wall_s=7712.0`/
`n_fdtd_calls=6` (`results.json:456-457`). But the proposal never states
how the new re-capture's wall time will be reported: no mention anywhere
of `build_result_text()`, its `wall_time_source` parameter (added
specifically by exp-109, at THERMODYNAMICS' own prior-cycle prompting, to
prevent old spend reading as new), `DISCLAIMER`, `R21`, or `R23`. If
exp-110's own forked `run.py`/`analyze.py` reuses exp-108's text-assembly
pattern without explicitly computing and labeling this cycle's own new
wall time — distinctly from exp-108's historical 7712.0s, and distinctly
from items 2/3's genuinely zero-new-FDTD cost — the exact gap
THERMODYNAMICS caught one cycle ago on this same document family recurs,
in the opposite direction (new spend silently absorbed/uncredited, rather
than old spend silently over-attributed). Recommend the Phase-3 synthesis
require an explicit sentence: "exp-110's own re-capture wall time: Xs,
measured fresh this cycle, distinct from exp-108's original 7712.0s."
