# Phase 2 Critique — MATERIALS & METAMATERIALS

Seat charter note: this cycle is governance/instrumentation (no material or
mechanism proposed), so the realizability bound (published/plausible/
unobtainium-with-parameters) is N/A directly. Applying this seat's other
standing duty instead: independently re-deriving every checkable numeric
claim from primitives rather than trusting the proposal's own arithmetic.

## Independent verification performed

Ran Python directly against `experiments/110-t28-item-i-local-norm-and-
controls/results.json` (never hand-typed):

- `pilot_empty_wall_s=250.6266098022461`, `pilot_total_wall_s=
  752.2232966423035` (r=156, 3 calls) — **exact match** to §2.0/§2.2.
- `t312` (3-call sum) `=6938.207038640976`; ratio `=9.223600318696624`;
  `ln(ratio)/ln(2)=3.2053299988171697` — **exact match** to the proposal's
  re-derived `KAPPA_COST_EXPONENT`.
- §2.2's three formula cases (positive `10.145960350566288`, non-regression
  `7632.027742505074`, discriminating-negative old `10799.0`/new
  `13695.778228220666`) — **all reproduce exactly** from the stated formula
  and real committed inputs.
- §2.0's `n_resolved` dicts (r156 Σ203/288, r312 Σ222/288) and floor range
  (`2.3458e-4`–`2.0959e-3`) — **exact match** against `results.json`.
- The claimed-absent scratch path
  (`/tmp/.../99fb0d5c-.../scratchpad/exp110`) — **confirmed absent** in this
  session, corroborating §2.0's grounding-fact finding.

This is an unusually high hit rate for hand-checked figures in this
program's own history — every number I could check against a committed
source reproduced exactly. One number did not: the §3 cost table (below).

**§3 cost table, independently recomputed** (proposal's own disclosed
formula, `pilot_total(cpl=20) × cpl_ratio³`, against the exact `t156`/`t312`
above):

| cpl | ratio | r=156 | r=312 | Both r |
|---|---|---|---|---|
| 25 | 1.25 | 1469.2s (24.5 min) | 13551.2s (225.9 min) | 15020.4s (**4.17h**) |
| 30 | 1.50 | 2538.8s (42.3 min) | 23416.4s (390.3 min) | 25955.2s (**7.21h**) |

Every cell matches the proposal's table **except** the cpl=30 "Both r" hour
figure: the proposal states "~6.5h," but `25,956s` is `7.21h`, not `6.5h`.
`6.5h` (`23,400s`) is instead what the **r=312-alone** column converts to
(`23,416s`/`3600=6.50h`) — the r=312-only hour figure appears to have been
carried into the "Both r" cell instead of the true sum.

## Steel-man

The proposal is disciplined and unusually well-verified: every headline
figure I independently re-derived (the 3.2053 exponent, both pilot times,
the `n_resolved` sums, the floor range) reproduces exactly from exp-110's
own committed `results.json`, not hand-typed prose — genuine R4 discipline.
It closes R28's founding-instance gap correctly: the reposition moves
`cost_gate_check()` into `chunk_runner.py::step_once`, strictly before
`build_sim`, verified by a monkeypatched control that never touches `Sim`
across all four branch outcomes (favorable / budget-refused /
precondition-refused / r=156-path-untouched) — a genuine causal fix, not a
second downstream restatement. Item 1's three-case fault-injection battery
correctly demonstrates the disclosed common-mode blindness quantitatively
(FI-B recovers exactly 0.0 against a common-mode input 2× FI-A's detected
magnitude) rather than merely asserting it. The item-3 deferral is
explicit, reasoned, and honestly labeled a second (not hidden third)
instance, with a concrete, bounded recommendation for Iteration 89.

## Sharpest attack

The §3 cost table — the evidence grounding the item-3 deferral decision —
contains an arithmetic slip I can reproduce and name exactly: the cpl=30
"Both r (6 calls)" cell is labeled "~6.5h" when the table's own seconds
figure (`25,956s`, itself correct) converts to `7.21h`; `6.5h` is instead
the r=312-alone column's own conversion, apparently misplaced. This
understates, by ~45 minutes (~11%), the real wall-clock delta between the
cpl=25 and cpl=30 options Iteration 89 is asked to choose between — inside
the one part of this document that is disclosed prose, not code-invoked,
and therefore exactly the shape R4 exists to catch. It is non-load-bearing
for THIS cycle (item 3 isn't run here) and doesn't reverse the deferral
itself (sequencing/density reasons stand on their own), but it is a genuine,
checkable defect sitting inside a proposal whose own item 4 is specifically
about catching an underestimating projection formula — the same failure
shape recurring one section later, uncaught by its author.

## Verdict

**support-with-changes.**

## Parameter change that would flip verdict

None needed to flip to outright oppose — the defect is real but
non-outcome-reversing and cheaply fixed. The single change I require before
this document freezes: correct the §3 table's cpl=30 "Both r" entry from
"~6.5h" to "~7.2h" (or regenerate the whole table by invoking a script
rather than hand-typing conversions, per R4's own standing text) — with
that one fix applied, I move to full support.
