# Phase 2 Critique — ELECTROMAGNETISM (Panel Iteration 88, exp-111)

## Independent verification performed before writing this critique

- Read `run.py` and `chunk_runner.py` (exp-110) in full, current committed state.
- `grep -n "\.run(\|Sim(" experiments/110-.../*.py`: confirmed `chunk_runner.py`
  is the only file in the tree that constructs `Sim(...)` or calls `.run(`
  on it; `analyze.py` only loads pickles and calls `run.py` functions —
  the "sole caller" premise the proposal inherits from Iteration 87 is
  still true for this cycle's own tree.
- Independently recomputed two numeric claims directly from
  `experiments/110-.../results.json` (not hand-typed): `r312` per-scene
  wall times sum to `6938.207038640976s` (matches the proposal's cited
  `t312` exactly); `ln(9.223600318696624)/ln(2) = 3.2053299988171697`
  (matches `KAPPA_COST_EXPONENT` exactly); the unit-arithmetic
  (`10.145960350566288`), non-regression (`7632.027742505074s`), and
  discriminating-negative-control (`10799.0` vs `13695.778228220666`)
  cases all reproduce exactly by direct computation. Item 4's formula
  math has no sign or boundary defect.
- Confirmed all 12 real `local_diag` floors are strictly positive
  (`2.3458e-4`–`2.0959e-3`, min checked directly), so item 1's
  `floor_degenerate` guard is provably inert on every real cell, and —
  since `floor = K·max(floor_p, floor_h)` with both terms non-negative
  percentiles of `abs(·)` values and `K=3.0>0` — `floor≥0` always under
  real usage, so `floor<=0.0` ⟺ `floor==0.0` exactly: `floor_degenerate`
  is provably the *only* way `resolved` can differ from the old code: no
  unintended interaction with `K` or `percentile` under this cycle's
  actual parameters.

## Steel-man (≤150 words)

Item 2's causal claim is independently checkable, and I checked it:
`chunk_runner.py`'s `build_sim()` is the only `Sim()`/`.run(` call site in
the tree; `analyze.py` only reads pickles. The proposed
`check_cost_gate_for_312()` sits as the unconditional first statement of
`step_once()` when `r==312` — before `geom_fixedabs()`, before the
checkpoint/done-file branches, before `build_sim()`/`sim.run()` — so it
re-fires on *every* chunk, fresh-start and resumed alike, not only the
first. That is exactly R28's literal text, verified by tracing rather
than trusting the narrative. `gate_reposition_control`'s design (patch
only `build_sim`, run the real orchestration function, count calls) tests
causal *order* executably — a genuine upgrade over six prior review
layers' grep-level "exists and branches" standard. Items 1 and 4's math
independently reproduce exactly from committed source; no sign/boundary
defect in the `floor>0` guard under real `K=3.0`/`percentile=50` usage.

## Sharpest attack (≤150 words)

The causal claim is only as strong as one unstated commitment: that
`gate_reposition_control.py` monkeypatches `chunk_runner.build_sim` on
the *real imported module* and calls the *real* `chunk_runner.step_once(312,
"empty")` unmodified — not a hand-copied reimplementation of its control
flow. The proposal's text never says which. A parochial mock would prove
nothing about the actual production call chain — R28's exact failure
shape ("shown to branch," never traced against the real call site)
recurring one layer deeper, on the very rule this cycle exists to fix.
Separately: the guard is unconditional, placed *before* the existing `if
os.path.exists(done_path): return True` early-exit — so a status-check
call on an *already-completed* r=312 scene now also re-executes
`check_cost_gate_for_312()`. None of the four listed control cases test
this (all assume "not yet done"); a stale/rotated r=156 log at that point
raises instead of silently no-op'ing.

## Verdict: support-with-changes

## Parameter change that would flip to plain support

Add, in `gate_reposition_control.py`: (1) an explicit assertion that the
patch target and call are `chunk_runner.build_sim = stub` /
`chunk_runner.step_once(312, "empty")` — i.e. identity-bound to the
imported module's real symbols, not a local reimplementation; (2) a fifth
case — r=312 `done_path` already exists, r=156 logs absent/stale — and
pin its predicted behavior (no-op `True` vs. raise) before Phase 4 runs.
