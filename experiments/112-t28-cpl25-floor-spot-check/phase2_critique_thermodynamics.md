# PHASE 2 — THERMODYNAMICS CRITIQUE · Panel Iteration 89 (candidate exp-112)

Fresh sub-agent, blind to every other seat's critique this cycle. Read
PANEL.md, LOGBOOK.md in full (R1-R28 RULED OUT registry; T28's opening,
Iteration 46; Iterations 85-88 in full, including the R27/R28
cost-gate-reposition history from my own prior lead cycle, exp-111), that
cycle's own `NOTES.md`, and this cycle's full Phase-1 package
(`phase1_proposal.md`, `run.py`, `chunk_runner.py`, `analyze.py`) before
critiquing. All code/number claims below were verified by actually
running the committed files, not by re-reading prose.

## Steel-man

The cost/wall-time accounting genuinely traces to real, executed code, not
assertion. I independently re-ran `cpl_cost_table.py` fresh and it
reproduces the proposal's own `1469.19s` (r=156) / `15020.37s` (both r)
figures bit-exact. I independently invoked `R.cost_gate_check()` with the
disclosed pilot split (`1469.186.../3`, `1469.186...`) and reproduced the
exact refusal dict verbatim — `pilot_pass=True`,
`projected_312_total_s=14906.304...`, `total_pass=False`,
`proceed_to_r312=False` — against the proposal's own §2.0 table. The
r=156-alone scope decision is therefore a genuine consequence of the real
gate's real output, not a preference dressed up as one, and the proposal
correctly discloses this is a "projection of a projection" until real
cpl=25 data exists. `verify_geometry_identity()` also passes exactly as
claimed. This is real R4 discipline, cleanly executed, on precisely the
question my charter exists to police.

## Sharpest attack

The Phase-4 pipeline cannot run at all, so the "1469.19s" figure that
justifies this cycle's entire scope has never been validated by the code
meant to produce it. `chunk_runner.py` and `analyze.py` each do
`import run as R110` (exp-110's `run.py`) then `import run as R`
(exp-112's own, identically-named `run.py`) — Python's `sys.modules`
cache silently binds BOTH aliases to whichever copy loads first
(exp-110's, since its directory lands first on `sys.path`). I ran
`python3 chunk_runner.py 156 25 empty` directly: it crashes with
`AttributeError: module 'run' has no attribute 'geom_fixedabs_cpl'` on
`step_once()`'s very first line, before any `Sim.run()` call — confirmed
by direct execution, not inspection alone. As shipped, this cycle cannot
generate a single second of the real timing or field data it exists to
gather; the disclosed cost remains a pure `cpl_cost_table.py`
extrapolation (a fixed `ratio**3` heuristic, not even the re-derived
`KAPPA_COST_EXPONENT`).

## Verdict

**support-with-changes**

## Flip condition (optional)

Fix the `run.py`/`run.py` module-name collision — e.g. load exp-112's own
`run.py` via `importlib.util.spec_from_file_location(...)` under a
distinct internal module name, or rename the file — so `chunk_runner.py`/
`analyze.py` can bind both modules' functions simultaneously. Verified
sufficient by re-running `python3 chunk_runner.py 156 25 empty` past
`step_once()`'s geometry line without the `AttributeError`. That single
fix flips this from support-with-changes to unqualified support; nothing
else in the physics, scope, or gate logic is in question.

## Additional finding (informational — does not change the verdict)

`sc.widths()` already computes `sigma_abs`/`sigma_ext` for both hollow and
peccored captures inside `analyze.py`'s own `w_p`/`w_h` dicts, but only
`sigma_scat` is ever extracted, compared, or persisted — the absorbed-power
ledger for the two configs is computed then discarded. This is the exact
energy-accounting question this "pure grid-resolution instrumentation"
cycle implicitly begs: holding `tau_shell` invariant under the cpl
refinement keeps the shell's continuum optical depth fixed, but says
nothing about whether the PEC-core-vs-hollow difference in absorbed power
(the PEC core cannot absorb; only the shell can, in both configs) tracks
the same angular signature as the −146.25° scattered-pattern deviation,
or whether `sigma_abs` itself is resolution-stable across cpl=20→25 the
same way the scattered pattern's own self-consistency identity is
checked. A future cycle attempting to give the named bin a genuine
physical (not merely statistical/noise-floor) interpretation will need
exactly this ledger. Recommend persisting `sigma_abs`/`sigma_ext` for both
configs, both cpl, into `results.json` even though this cycle draws no
verdict from them — the data is already computed in memory at zero
marginal FDTD cost.
