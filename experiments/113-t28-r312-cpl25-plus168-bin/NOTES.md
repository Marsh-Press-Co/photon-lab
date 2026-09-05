# exp-113 — Panel Iteration 90

## Phase 1 — Propose (VISION SCIENCE)

See `phase1_proposal.md` in full. Executes the Reconciled Iteration-90
queue's Tier-1 items 1–4: the `+168.75°`/r=312/bin-46 companion of
exp-112's own `−146.25°`/r=156 bin, R31-gated by a same-session control,
Check C recalibrated per R30, Check B normalized per the `CPL_RATIO`
finding. T1 escape route N/A throughout (instrument-fidelity work).

## Phase 2 — Critique

Five blind critiques (`phase2_critique_photonics.md`,
`phase2_critique_materials.md`, `phase2_critique_em.md`,
`phase2_critique_thermodynamics.md`, `phase2_critique_quantum.md`), all
**support-with-changes**, zero opposition. Red Team's audit
(`phase2_redteam_audit.md`) independently re-derived every cited figure
from primitives and confirmed all five findings exactly. Verdict:
**PROCEED-WITH-MANDATORY-FIXES**.

## Phase 3 — Synthesis (Director)

**All five mandatory-fix-docket items accepted in full, applied this
shift, before any Phase-4 `Sim.run()` call — no criticism overridden**
(Red Team's own words: "None of the five rises only to a disclosed
override... I decline to soften any of them").

1. **Fix 1 (PHOTONICS — box_a near-field-depth confound)**: `run113.py`'s
   `DISCLAIMER` now discloses, as computed constants (not hand-typed),
   `box_a`'s clearance past the coat surface in wavelengths —
   **3.2λ at r=156** (exp-112) vs. **6.4λ at r=312** (this cycle), exactly
   `kappa_ratio=2.0`, present already at `cpl=20` — with an explicit
   caution that Phase 5 must not read this leg and exp-112's own
   `−146.25°` leg as probing the same physical near-field depth
   "companion" question, only the same proportional-margin construction
   at two different depths. Non-blocking for this leg's own
   self-referential falsification.
2. **Fix 2 (MATERIALS — wrong sponge-margin comparator)**: the single
   `_SPONGE_MARGIN_ORDERS` figure (`~4.02` orders, computed against
   `BASELINE_FLOOR`, the K=1 instrument-floor scale) is replaced by
   THREE explicitly labeled figures: `~4.02` orders vs. the floor scale,
   `~3.43` orders vs. the named bin's own signal magnitude
   (`min(|peccored|,|hollow|)`), and `~2.47` orders vs. `|delta|` (the
   quantity Check B actually scores) — all three non-fatal, all three
   independently re-derived by Red Team bit-exact to MATERIALS' own
   figures.
3. **Fix 3 (ELECTROMAGNETISM — false engine-invariance claim + R31
   control commensurability)**: (a) corrected the false "per-step FDTD
   cost is materials-invariant... regardless of contents" claim —
   `lab/fdtd2d.py::Sim.run()`'s own PEC-zeroing masked write is a real,
   independently op-counted `~14%` extra per-step cost `peccored` alone
   pays; `run113.py`'s own comment above `HISTORICAL_PER_STEP_S` is
   corrected in place, and `phase1_proposal.md`'s Idealization 1 carries
   a Phase-3 correction blockquote. (b) `chunk_runner113.py::run_control()`
   now re-times the SAME 3-scene blend (`empty`+`hollow`+`peccored`)
   `HISTORICAL_PER_STEP_S` itself blends, removing the anti-conservative
   mismatch a single-scene (`empty`-only) control introduced.
4. **Fix 4 (THERMODYNAMICS — unrepresentative control duration)**:
   `run_control()` now takes TWO commensurable 3-scene-blend readings —
   a short burst (`SHORT_CONTROL_STEPS=1000`/scene) and a sustained
   reading (`SUSTAINED_CONTROL_STEPS=3334`/scene, ≈10002 steps total) —
   combined by the new `combine_control_readings()`, which gates on the
   LOWER (more conservative) of the two `speed_ratio` values.
5. **Fix 5 (QUANTUM OPTICS — Check-C direction inversion, the most
   consequential finding, ratifying R32)**: `classify_resolution_check`'s
   single directional `supports_real_structure = percentile<=10.0` field
   — which silently inverted the ORIGINAL `neighbor_correlation_check`
   docstring premise (HIGH correlation across `cpl` = real structure) —
   is replaced by two symmetric, undirected fields
   (`low_percentile_outlier`, `high_percentile_outlier`) plus a
   `direction_validated` flag that starts `False`. Check A's own
   "candidate real structure" upgrade language is removed entirely
   pending validation. `analyze113.py` now computes, post-Phase-4, a
   resolved-vs-unresolved windowed-correlation cross-tabulation
   (`R.resolved_unresolved_crosstab`, zero marginal FDTD cost, both
   input arrays already computed) on r=312's OWN real data, and sets
   `direction_validated=True` only if it independently confirms the SAME
   (low) direction the code currently treats as the candidate reading —
   a "high" or degenerate crosstab result means the premise is NOT
   validated at r=312 either, and Phase 5 must report the percentile as
   an undirected, disclosed-only reading in that case.

**R32 ratified** (LOGBOOK.md RULED OUT registry, this shift) — a freshly
recalibrated discriminating statistic's DIRECTION, not just its
threshold, must be independently validated — via a stated mechanistic
argument or a same-geometry cross-tabulation — before an evidentiary
reading in either direction; extends R30 one level deeper. Founding
instance exp-113, caught cleanly at Phase 2 (before any freeze); does not
fire; forward-firing on a future cycle that cites a directional
statistic's reading without this validation, matching R16/R21–R31's own
precedent.

**T1 escape route: N/A**, confirmed independently by every seat and by
Red Team's own audit — no σ(I)/σ(x,t)/angular-selectivity/sub-threshold
content anywhere in this cycle; no constraint-1/2/3/4 verdict is scored
or moved.

**Verification of all five fixes, before any Phase-4 `Sim.run()` call**:
`python3 run113.py --verify-geometry` → `pass_=true` both r (unchanged).
`python3 run113.py --predictions-only` → renders cleanly, all five fixes'
own computed figures appear bit-exact to Red Team's independently
re-derived values (`4.0175`/`3.4298`/`2.4664` orders; `3.2`/`6.4`
wavelengths). Synthetic zero-FDTD unit tests of
`combine_control_readings`/`cost_gate_check_r31`/
`resolved_unresolved_crosstab` all behave correctly (gate correctly picks
the more conservative reading; crosstab correctly recovers the injected
direction on synthetic data). Trust suite green throughout (41/41),
zero `lab/` diff.

## Setup

Congruent `cpl=20→25` (ratio 1.25×) grid-resolution refinement of the
`fixedabs` family (exp-106/108/110's own hollow-vs-PEC-cored geometry) at
**r=312** (companion of exp-112's own r=156 leg), targeting the
`+168.75°` bin (index 46 of 48, margin=32/`box_a`) — flagged by
PHOTONICS' Iteration-85 self-review at a 10.88% local fractional
deviation while sitting below even the K=1 mirror-pooled floor at
`cpl=20` (`local_snr_peccored=0.2584`, `local_snr_hollow=0.2865`).
Geometry reused unmodified from `run112.py::geom_fixedabs_cpl`, already
verified byte-exact to `R110.geom_fixedabs` at `cpl==20` for both r=156
and r=312. ~~3 real FDTD calls this cycle (empty/hollow/peccored, r=312,
cpl=25), R31-gated by a same-session control point measured at the start
of Phase 4 (before the real spend, per house discipline).~~

> **Phase-5 correction (Red Team's final audit, Iteration 90, PHOTONICS'
> own Phase-5 finding F3):** the struck sentence above was written at
> Phase 3, before Phase 4 ran, per house discipline — but was never
> retroactively annotated once Phase 4's actual outcome (below) was known,
> so it reads as an accomplished fact to any reader who stops at "Setup."
> **Zero r=312 `Sim.run()` calls occurred this cycle.** The R31 same-
> session control (correctly gated *before* the real spend, per house
> discipline) measured this session's own throughput at 0.406× historical
> and REFUSED the projected r=312 leg (16737.4s vs. the 10800s bound) —
> see Phase 4/Result, below. The 6 real FDTD calls this cycle actually
> made were all at r=156/`cpl=25` (the R31 control's own short+sustained
> 3-scene blends), not the 3 calls (empty/hollow/peccored, r=312) this
> Setup section describes as the plan. Non-blocking (the Phase 4/Result/
> Combined-Verdict sections below always correctly stated what actually
> happened; only this Setup paragraph lagged) — matching this program's
> own R23/citation-shortening discipline: a reader must not stop at
> "Setup" and conclude real r=312 data exists.

## Predictions (committed to git BEFORE any Phase-4 code is executed for
## real, house discipline, non-negotiable — verbatim quote of
## `run113.py::build_predictions_text()`'s own output, post-fix, WITHOUT
## the control/gate figures, which do not exist until Phase 4's own R31
## control point is measured)

```
PREDICTIONS (pre-registered, exp-113, Panel Iteration 90)

[DISCLAIMER — see run113.py::DISCLAIMER, quoted in full in
phase1_proposal.md and reproduced by `python3 run113.py
--predictions-only`; omitted here for length, unchanged since the last
`--predictions-only` re-run this document cites]

**Geometry identity (zero-FDTD, pre-Phase-4)**: verify_geometry_identity()
returns pass_=True at both r=156 and r=312 (already re-run above).
Falsified by any mismatch -- HALT before any Sim.run() call.

**Reproduction/self-consistency precondition**: sum(sigma_scat_per_bin) ==
sigma_scat (angular_scattered_pattern's own docstring identity) to <1e-9
relative, at margin=32, both peccored and hollow captures, r=312, cpl=25.
Falsified by any larger deviation -- HALT before the named-bin comparison
is trusted.

**Named bin (168.75deg, r=312, margin=32, bin index 46) --
the genuinely uncertain question this leg exists to answer**:
Check A (mirror-pooled-floor instrument, reused unmodified, at cpl=25):
SURVIVES if local_snr_peccored AND local_snr_hollow both clear 1.0
(cpl=20 values: 0.2584/0.2865);
COLLAPSES if neither local_snr improves over cpl=20; else AMBIGUOUS.
Check B-normalized (this cycle's own scored reading, CPL_RATIO-divided):
SURVIVES if delta[idx]/CPL_RATIO keeps the same sign as cpl=20
(-9.510156e-06) and stays within one order of magnitude of it;
COLLAPSES on a sign flip or a >=10x drop; else AMBIGUOUS. Check B-raw
(uncorrected, exp-112-comparable, disclosed but NOT scored) reported
alongside. Check C (R30 null-calibrated, R32/Fix 5 UNDIRECTED): reports
whether the named bin's own +/-2-bin correlation is a
low_percentile_outlier (<=10th percentile) and/or a high_percentile_outlier
(>=90th percentile) of this cycle's own 48-window null population -- NEITHER
tail is asserted as "candidate real structure" this cycle (direction_validated
stays False) regardless of Check A's own reading, pending the
resolved-vs-unresolved cross-tabulation (Fix 5b, computed post-Phase-4 on
r=312's own real data, zero marginal FDTD cost). No advance position taken
on which outcome any of the three checks, or either Check-C tail, will
report.
```

Falsified/HALT conditions above are hard blockers — Phase 4 must not
proceed past a HALT to the named-bin comparison.

## Phase 4 — Test

**R31 same-session control (Fix 3b/Fix 4), before any r=312 spend**: two
commensurable 3-scene-blend re-timings of the r=156/cpl=25 scenes — short
(1000 steps/scene, 190.7s, speed_ratio=0.439) and sustained (3334
steps/scene, 687.5s, speed_ratio=0.406) — `combine_control_readings()`
correctly selected the sustained reading (the LOWER, more conservative
speed_ratio). **This session ran at ~0.41× the historical (Iteration 89)
session's own per-step speed — i.e. genuinely SLOWER, the OPPOSITE
direction from that session's own ~2.19×-faster finding.** 6 real FDTD
calls, 878.2s (14.64 min) total, all at r=156 (cheap grid) — zero r=312
Sim.run() calls at this stage.

**Cost-gate re-check (`chunk_runner113.py --gate 25`)**: the R31-scaled
projection is `16737.4s` against the `10800s` bound — **REFUSED**. The
naive, uncontrolled cross-session projection this cycle's own Reconciled-
Iteration-90 queue cited (`6802.6s`, reproducing Iteration 89's own
briefed figure bit-exact) would have wrongly **APPROVED** the real spend.
`chunk_runner113.py`'s own `check_cost_gate_for_r312` (R28: independently
confirmed genuinely upstream of every r=312 `Sim.run()` call by
ELECTROMAGNETISM's own Phase-2 critique and Red Team's audit) raised
`RuntimeError` before any real r=312 scoring call was attempted — **zero
r=312 `Sim.run()` calls occurred this cycle.**

**This is R31's own mechanism working exactly as designed — the first
time it has actually prevented a real overspend**, unlike its own
founding instance (exp-112, Iteration 89), where the miss was
conservative (over-, not under-, estimating cost) and no unsafe spend
would have occurred either way. Here, without R31's same-session control,
this cycle would have proceeded to attempt a real r=312/cpl=25 leg
projected (by the naive cross-session figure) to cost ~6802s but actually
requiring, by this session's own real per-step throughput, ~4.6 hours —
a genuine near-miss the gate correctly caught.

## Result

Verbatim quote of `analyze113.py`'s own committed `result_text`
(`results.json`, this cycle's own gate-refused branch):

```
RESULT (exp-113, Panel Iteration 90)

[DISCLAIMER -- unchanged, see above]

6 real FDTD calls, 878.2s (14.64 min)
total wall time this cycle, zero `lab/` diff.
(6 real FDTD calls this cycle, ALL at r=156/cpl=25 (R31 same-session
control, short+sustained 3-scene blends) -- ZERO real r=312 scoring
Sim.run() calls were made; the gate refused upstream of all of them.)

**Geometry identity: PASS.**
**Reproduction/self-consistency precondition: N/A (not reached).**
**Named bin (168.75deg, r=312, margin=32):** NOT REACHED -- R27/R28/R31
cost gate REFUSED the real r=312 leg before any scoring Sim.run() call
was attempted (upstream, per R28). Same-session control (Fix 3b/Fix 4):
this session ran at 0.406x the historical (Iteration 89) session's own
speed (sustained reading used, the more conservative of the two) -- i.e.
THIS session is slower, the OPPOSITE direction from Iteration 89's own
~2.19x-faster finding. R31-scaled projection: 16737.4s vs. the 10800s
bound -- REFUSED (the naive, uncontrolled cross-session projection this
cycle's own Reconciled-Iteration-90 queue cited, 6802.6s, would have
wrongly APPROVED). This is R31's own mechanism working as designed,
catching a real would-have-been-unsafe spend this time -- unlike its own
founding (conservative-miss) instance.
```

Both R23 `DISCLAIMER` asserts (predictions-side, result-side) fired on
real, live re-execution. Trust suite green throughout (41/41), zero
`lab/` diff, confirmed both before and after Phase 4.

## Combined Verdict (Director, pending Phase 5)

**PARTIAL — BLOCKED BY COST GATE, not RULED OUT, not the intended
data-producing PROMISING/AMBIGUOUS/etc. outcome.** The named-bin question
(the `+168.75°` bin at r=312) remains untested — deferred for a THIRD
time, but this time for a verified, real, this-session cost-gate
refusal, not a sequencing/density choice (exp-111: sequencing; exp-112:
cost/density risk; exp-113: genuine R31-scaled REFUSAL). All five
Phase-3 mandatory fixes are real, verified, and now exercise real code
paths for the first time (the R31 control/gate machinery ran for real
and produced the single most consequential finding of this cycle: R31
prevented a real overspend). Genuine, disclosed, non-null progress
nonetheless: (1) R31/Fix-3b/Fix-4's own necessity is now empirically
demonstrated, not merely reasoned about — a materially different outcome
from simply re-confirming the prior session's own projection; (2) all
five Phase-2 findings (box_a depth confound, sponge-margin comparator,
PEC-zeroing cost asymmetry, control representativeness, Check-C
direction inversion) are now permanently fixed in code, available to
every future cycle in this family; (3) the new standing rule R32 is
ratified. Zero Checkpoint criteria fire this cycle on their own account —
this is a real, gated, disclosed cost-based deferral, not an
unfalsifiable claim, a dropped constraint, or program-integrity drift.

## Idealizations — carried from `phase1_proposal.md` §6, as corrected at Phase 3

See `phase1_proposal.md` §6 for the full list; Idealization 1 carries a
Phase-3 correction blockquote (Fix 3a). Idealizations 3/4 (Check C's null
population includes the named bin itself; the original `≤10th
percentile` bar was a disclosed, not independently re-derived, choice)
are superseded by Fix 5's own undirected reporting — the bar itself is
no longer scored evidentially in isolation, only alongside the
`direction_validated` crosstab.
