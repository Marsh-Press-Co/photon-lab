# Phase 5 Review — THERMODYNAMICS (exp-113, Panel Iteration 90)

**Fresh sub-agent, blind context.** Spawned fresh for this seat only. I have
NOT seen and did not seek out any other seat's Phase-5 output this cycle.
Read, in full: `PANEL.md`; `LOGBOOK.md`'s RULED OUT registry lines 1–1400
(all of R1–R31, including R27–R31 in full — my own seat founded R31,
Iteration 89); the T28 live-thread opening (`sed -n '3094,3200p'`); the full
Iteration 89 entry (`sed -n '24215,24415p'`); and, in
`experiments/113-t28-r312-cpl25-plus168-bin/`: `phase1_proposal.md`, all five
`phase2_critique_*.md` (including my own), `phase2_redteam_audit.md`,
`NOTES.md` in full, `run113.py`, `chunk_runner113.py`, `analyze113.py`, and
`results.json`. No `Sim.run()` call was made by me; every figure below is
independently re-derived by direct execution of the *committed* functions
(`r31_control_ratio`, `combine_control_readings`, `cost_gate_check_r31`,
`R110.cost_gate_check`) against the real numbers in `results.json`, or by
hand arithmetic cross-checked against those executions — never taken from
this document's own prose on faith. No real FDTD was run by me.

## Verdict: **CONFIRM**

Every arithmetic claim in the headline outcome re-derives bit-exact from
primitives. `combine_control_readings` correctly selects the lower
(more-conservative) of the two speed ratios; dividing the historical pilot
by that ratio correctly scales the effective pilot *up* (the gate becomes
*more* conservative when this session is slower); the resulting
`cost_gate_check_r31` scaled projection (`16737.44s`) correctly exceeds the
`10800s` bound while the raw/uncontrolled projection (`6802.64s`) would have
wrongly cleared it. R31's own mechanism — my own seat's rule — worked
exactly as designed, for real, for the first time, and correctly prevented
what would have been a genuine, unrecognized overspend. I find no arithmetic
defect and no direction error anywhere in the chain. I downgrade only one
half-step short of plain CONFIRM (to CONFIRM, not CONFIRM-WITH-GAPS,
because nothing here is disqualifying) but flag one genuine, previously
undisclosed residual gap below: the two-reading (short/sustained) control
that made this correct decision possible is itself an **N=1-per-duration**
measurement with no repeat, so "sustained reads lower than short" is
confirmed as a real, correctly-signed, physically well-motivated effect —
but its own reproducibility has never been tested.

## Findings

### 1. Re-derivation of `combine_control_readings` — CONFIRMED correct

From `results.json['r31_control']`: `short.speed_ratio = 0.439384...`,
`sustained.speed_ratio = 0.406433...`. The function's own logic
(`used = short if short["speed_ratio"] <= sustained["speed_ratio"] else
sustained`) takes the `else` branch here (0.439 is NOT ≤ 0.406), correctly
returning **sustained (0.406)** — the lower, more conservative value.
`results.json` confirms `used_label: "sustained"`, `used_speed_ratio:
0.40643257440437214`. Matches.

### 2. Re-derivation of the scaling division — CONFIRMED correct direction and bit-exact magnitude

Task's own arithmetic check, `670.4778/0.406`, gives **1651.42**, close to
but not identical to the reported `1649.665` — the ~0.1% gap is *entirely*
attributable to the task prompt's own 3-decimal rounding of the ratio.
Using the actual full-precision stored ratio:

```
670.4777698516846 / 0.40643257440437214 = 1649.6654354889522
```

— **bit-exact** to `results.json['cost_gate']['scaled']['pilot_total_wall_s']
= 1649.6654354889522`. Confirmed: dividing by a ratio **below 1** correctly
inflates the effective pilot, matching my own seat's Phase-2 hand-verified
direction (the concrete check I ran at Phase 2 — "session 2× slower,
speed_ratio=0.5, scaled=1340.96s" — used the identical formula; this is the
same code path, now exercised on real, not hypothetical, numbers). Carrying
the full projection through:

```
projected_312_total_s (scaled) = 1649.6654... * 2.0**3.2053299988171697 * 1.10
                                = 16737.440100170577
```

— bit-exact to `results.json`'s own figure, `>10800s` ⇒ REFUSED. The raw
(uncontrolled) path, `670.4777698516846 * 2.0**3.2053... * 1.10 =
6802.6408688513`, also reproduces exactly, `<10800s` ⇒ would have APPROVED.
Both directions independently confirmed against the real, committed
`R110.cost_gate_check()`, not a re-implementation.

### 3. The sustained-vs-short gap: genuinely validates my own Iteration-89-successor concern, and its direction is independently corroborated by ruling out the obvious alternative explanation

The gap is **7.50%** relative to the short reading (`(0.439384 −
0.406433)/0.439384`), matching the task's own "~7.5%" framing. This is
small in absolute percentage terms but it is the *entire margin* between
this cycle correctly REFUSING and wrongly APPROVING was already decided by
which of the two readings got used — had `combine_control_readings` used
the short reading instead, `scaled_total = 670.478/0.439384 = 1526.05s`,
projecting to `15,461s`, which *still* refuses (both readings independently
clear the refuse threshold here) — so in this specific instance the 7.5%
gap was not itself outcome-determining, but it is exactly the shape of gap
R31/Fix 4 exists to catch for a *future*, thinner-margin cycle.

I went one step further than the task's own framing and checked whether the
observed direction (sustained reads *slower* than short) is actually
consistent with a genuine sustained-load degradation mechanism (turbo-boost
clock decay, memory-bandwidth saturation — my own Phase-2 hypothesis) as
opposed to a measurement artifact pointing the same way by coincidence. The
obvious alternative artifact — fixed per-scene setup overhead (`Sim`
construction, array allocation) amortized over fewer steps — predicts the
**opposite** sign: a short control's per-step rate should read *slower* (not
faster) than a long one, because fixed overhead dominates more at low step
counts. What's actually observed is the reverse: `this_session_per_step_s`
short `= 0.063581s`, sustained `= 0.068736s` — the *sustained* reading is
the slower one. That rules out the fixed-overhead-dilution explanation and
is positive (not merely non-contradictory) evidence for a real sustained-load
degradation effect, exactly the mechanism my own Iteration-89-successor
critique named. **This validates the concern's existence and direction**,
for the first time with real data, not merely by engineering argument.

**It does not, however, establish that 3334 steps is long enough to reach
steady state**, and this is a genuine gap neither my own original critique
nor Fix 4's implementation closes: with exactly one reading at each of two
durations, there is no way to distinguish (a) a real, still-descending
trend that would drop further at, say, 10,000 steps/scene, from (b) a real
trend that has already substantially plateaued by 3334 steps, from (c)
ordinary run-to-run timing noise on a shared/virtualized host that happens
to have landed in the observed direction with only one sample per duration.
R15's own two-point-insufficiency discipline (already established in this
program for spatial-resolution convergence) applies with identical force
here for *temporal* convergence of a control measurement, and nothing in
`run113.py`/`chunk_runner113.py`/`NOTES.md` discloses this as an open
question — Idealization 2 (`phase1_proposal.md`) discusses only whether
*any* control exists and whether it's commensurable in scene-mix (Fix 3b),
not whether two single-shot readings are enough to call the trend real
versus noisy.

### 4. Would a third, even-longer control point change the picture? Diminishing returns for *this* decision, not for the underlying question

I solved for the breakeven `speed_ratio` at which the scaled gate would
flip back to APPROVE, holding everything else fixed:

```
breakeven_speed_ratio = raw_projection / COST_GATE_TOTAL_S
                       = 6802.6408688513 / 10800 = 0.629874...
```

The observed sustained ratio (0.406) sits **35.5% below** that breakeven
(equivalently, throughput would need to be `1.55×` higher than measured to
flip the decision), and the *short* reading (0.439) is also well below it
(30.2% short). Since the short→sustained trend moved *away* from approval,
not toward it, a third, even-longer reading could not plausibly reverse
this cycle's REFUSE outcome — it would have to reverse direction and then
overshoot by 55% relative to the current sustained figure, for which
nothing in the data gives any support. So: **diminishing returns for
gating this specific decision** — no further control spend is needed to
trust this cycle's REFUSE.

That is a different question from whether a third point is worth taking
for the *program's* sake. It is, but not the one the task's framing
implies (a longer duration) — given finding 3 above, the more informative
and cheaper next control is a **same-duration repeat** of the sustained
reading (3334 steps/scene again, ~687s, a cost this cycle already paid
once) to establish whether 0.406 is a reproducible reading of this
session's own sustained-load throughput or a single noisy sample, before
extending duration further. A repeat that reproduces ~0.406 would licence
real confidence in the number; a repeat that lands far from it (e.g.
0.35 or 0.46) would show the "sustained" reading itself still carries
run-to-run noise comparable to the signal it's trying to isolate, which no
amount of further duration alone would fix.

### 5. My own Phase-2 mandate (Fix 4) was implemented correctly, in full

My own Phase-2 critique asked for exactly two things: (a) a second,
sustained-duration control reading, comparable in duration to a real
production sub-chunk, and (b) gating on whichever `speed_ratio` is lower.
`chunk_runner113.py::run_control()` (`SHORT_CONTROL_STEPS=1000`,
`SUSTAINED_CONTROL_STEPS=3334`, ≈10,002 steps total across the 3-scene
blend, comparable to `DEFAULT_BUDGET_S`-scale production sub-chunks) and
`R.combine_control_readings()` (verified above, §1) implement both
faithfully. Nothing was softened or partially applied.

### 6. Energy sidecar: correctly, legitimately N/A this cycle — re-confirmed after the real run, not merely as predicted

At Phase 2 I predicted the sidecar should be silent this cycle since no new
absorptive mechanism is proposed. That holds even more strongly now that
Phase 4 has actually executed: zero r=312 scoring `Sim.run()` calls
occurred (gate-refused upstream), and the 6 real FDTD calls that *did*
run were all r=156/cpl=25 **timing-control** bursts (`_time_control_blend`)
— each builds a `Sim`, runs it for a fixed step count, and discards it
without ever invoking `lab/sections.py`'s flux/energy-ledger machinery. No
new absorbed-power number of any kind exists anywhere in this cycle's
output for my charter to sidecar. `analyze113.py`'s persisted output
(`results.json`) contains no `energy_ledger` key this cycle — confirmed by
inspection — consistent with "nothing new absorbs anything, so there is
nothing to sidecar," not an oversight.

### 7. Minor: my own Phase-2 "one-line disclosure gap" (no document states the sidecar as N/A) was correctly left unfixed

I flagged this at Phase 2 as explicitly "not load-bearing," and Red Team's
mandatory-fix docket (five items, none mine) correctly did not include it.
Still true and still non-blocking after the real run — noted for
completeness, not as a finding against this cycle.

## Ranked top-3 candidate directions for Panel Iteration 91

**1. (Highest value, lowest cost) Re-attempt the SAME r=312/cpl=25 gate check at the start of a future session, paired with a same-duration control repeat — no code or geometry change needed.**
Nothing about this cycle's REFUSE is a property of the physics or the
geometry; it is a property of *this session's own measured throughput*
(0.406×, the slowest of the two sessions on record for this exact pilot —
Iteration 89's own session read 2.19× *faster* than exp-110's baseline, a
combined ~5.4× peak-to-peak spread already visible across just two data
points). `chunk_runner113.py --control` + `--gate 25` is a complete,
self-contained, zero-marginal-FDTD-cost re-check that can simply be run
again at the start of any future session; if that session's throughput
clears the independently-derived breakeven ratio (0.630, §4 above), the
named `+168.75°` bin's real r=312 leg can proceed with the SAME instrument,
zero code changes, and zero wasted prior spend (nothing was spent on the
r=312 leg itself this cycle). Pair this with a repeat sustained-control
measurement (finding 4) before trusting whichever session's gate reading
ends up favorable, so a lucky-fast single sample doesn't substitute for a
reproducible one.

**2. Flag `COST_GATE_TOTAL_S`'s own semantics to Marsh — a real, not hypothetical, ambiguity this cycle exposes.** `COST_GATE_TOTAL_S = 10800s` (3 wall-clock hours) is a hardcoded constant from exp-110, chosen before this program had any evidence that session-to-session compute throughput varies at all. Two consecutive cycles now show it varying substantially in *opposite* directions relative to the exp-110 baseline (Iteration 89: this session ~2.19× faster; this cycle: ~2.46× slower, i.e. 1/0.406). If the bound is meant to cap **real elapsed waiting time** (a scheduling/practical constraint — "no session should sit running FDTD for more than 3 real hours"), R31's own session-relative scaling is *already* the objectively correct fix, and nothing about the constant itself needs to change. If instead the bound is meant to cap **actual compute/resource cost** (CPU-seconds, energy, cloud spend), a fixed wall-clock bound is the *wrong* invariant to hold constant across sessions of different speed: a session running at 0.406× throughput that clears a wall-clock bound is, at the same time, burning proportionally *more* real compute-seconds (and, plausibly, more energy) to answer the identical physics question than a 2.19×-fast session would for the same bound — the wall-clock gate and a compute-cost gate diverge precisely when speed varies this much. This is a genuine governance ambiguity in the gate's own stated purpose, now empirically live rather than academic, and belongs on the Tier-0 queue alongside the other pending Director/Marsh rulings (0a–0c) rather than being silently assumed one way or the other in a future cycle's code.

**3. Add a reproducibility check to the R31 control machinery before the next real r=312 gate decision.** Per finding 3–4: the short→sustained drop (0.439→0.406) is real and correctly signed, but is a single sample at each duration — nothing distinguishes "a stable, reproducible sustained-load effect" from "ordinary timing noise that happened to land in the throttling-consistent direction once." The cheapest, most decision-relevant next step is a same-duration **repeat** of the sustained (3334-step/scene) reading — not a longer one — the next time this gate is evaluated. This is not blocking (§4: the current 55%-over-bound margin means no plausible third reading reverses this cycle's REFUSE), so it should land as a cheap addition to whichever future session next runs `chunk_runner113.py --control`, not as a reason to defer that attempt.
