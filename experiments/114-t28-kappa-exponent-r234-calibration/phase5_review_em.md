# Phase 5 Review — ELECTROMAGNETISM — Panel Iteration 91 (exp-114)

*Charter: field/wave behavior, impedance matching, energy coupling; owns
reciprocity/passivity/causality bookkeeping and formalizes what T1
permits/forbids. Fresh context this phase, blind to the other six seats'
current Phase-5 reviews. I read `LOGBOOK.md` end to end (RULED OUT R1–R32,
with R9/R28/R31 read in full at their own primary text, not from summary);
`PANEL.md` in full; `PLAN.md`'s tail (Reconciled Iteration-91 queue);
every file in this cycle's own directory (`phase1_proposal.md`, `run114.py`,
`chunk_runner114.py`, `analyze114.py`, all five Phase-2 critiques —
including my own, `phase2_critique_em.md` — `phase2_redteam_audit.md`,
`NOTES.md`, `results.json`); and `experiments/113-.../` for R31's own
founding instance. Nothing below is taken on the Director's word — every
number is independently re-derived from primitives, most by direct Python
execution against the real committed constants and the real `results.json`
figures.*

## Verdict: **PROMISING** (Tier-1 falsifiable question CONFIRMs; the
governing R9 self-catch is sound; one residual, non-outcome-reversing
confound is named below, not yet closed)

This cycle is squarely in-scope for this seat by charter and delivers
real, non-null progress on exactly the kind of bookkeeping question this
seat owns: whether two wall-time quantities compared against each other
are actually commensurable. T1 route is correctly N/A throughout — no
σ(I)/σ(x,t)/angular-selectivity/sub-threshold content anywhere in this
cycle, confirmed by my own independent read of `run114.py` and
`chunk_runner114.py` end to end. My own Phase-2 critique (with VISION and
QUANTUM) found the original exponent-space CONFIRM/REFUTE bands mis-cited
R28's founding figure; Red Team's Fix 1 correctly moved the check into
ratio space. I re-verify below, from scratch, that (a) the Director's own
Phase-4 R9 catch is dimensionally sound and correctly signed, (b) Fix 1's
ratio-space rescoring is applied correctly to the real data this cycle
produced, and (c) the resulting CONFIRM verdict is real but sits closer
to the AMBIGUOUS boundary than the headline `rel_dev=0.1227` alone
suggests once the correction's own uncertainty is accounted for.

---

## 1. Independent, adversarial re-derivation of the Director's R9 catch

**Task: is `t156_session_adjusted = HISTORICAL_R156_CPL25_TOTAL_S /
control['used_speed_ratio']` the mathematically correct same-session
comparator for `refit_kappa_exponent(t156, t234)`?**

First, `speed_ratio`'s own definition, read directly from
`experiments/113-.../run113.py::r31_control_ratio` (not taken from any
prose summary):

```python
total_steps = control_steps_per_scene * n_scenes
this_session_per_step_s = total_control_wall_s / total_steps
speed_ratio = HISTORICAL_PER_STEP_S / this_session_per_step_s
```

So `speed_ratio = historical_per_step_s / this_session_per_step_s` —
confirmed exactly as the task brief states, by direct source read, not
inference. `speed_ratio < 1` means this session is *slower* (a bigger
`this_session_per_step_s` in the denominator); `speed_ratio > 1` means
faster. This cycle measured `used_speed_ratio = 0.3923` (the sustained
reading, correctly the lower/more conservative of the short/sustained
pair per `combine_control_readings`) — this session ran at ~39% of the
historical session's own throughput, i.e. genuinely slower, consistent
with `exp-113`'s own `0.406×` finding one cycle earlier.

**Dimensional derivation, from primitives, not from the code's own
comment.** `HISTORICAL_PER_STEP_S` is itself defined (read directly,
`run113.py` line 136) as
`HISTORICAL_R156_CPL25_TOTAL_S / (3 * HISTORICAL_R156_CPL25_STEPS)`, where
`HISTORICAL_R156_CPL25_STEPS = 8000` is the **per-scene** step count for
the r=156/cpl=25 pilot (`R112.geom_fixedabs_cpl(156,25)["STEPS"]`). So:

```
t156_session_adjusted = HIST_TOTAL / speed_ratio
                       = HIST_TOTAL / (historical_per_step_s / this_session_per_step_s)
                       = HIST_TOTAL * this_session_per_step_s / historical_per_step_s
                       = (3*8000*historical_per_step_s) * this_session_per_step_s / historical_per_step_s
                       = (3*8000) * this_session_per_step_s
                       = total_pilot_steps * this_session_per_step_s
```

This is exactly "the number of FDTD steps the r=156/cpl=25 pilot actually
took (24000, historical, fixed), multiplied by THIS session's own
measured per-step rate" — a legitimate same-session projection, not an
extrapolation across geometries, **because the control blend that
supplies `this_session_per_step_s` was measured on the literal r=156/
cpl=25 geometry** (`chunk_runner114.py::_time_control_blend` calls
`R.geom_fixedabs_cpl(156, 25)` explicitly), the same geometry the
historical `670.4778s` figure itself describes. I confirmed this
algebraic identity by direct computation, not just derivation on paper:

```
historical_per_step_s = 670.4778 / 24000        = 0.027937 s/step
sustained this_session_per_step_s = 712.2446/(3334*3) = 0.071210 s/step
speed_ratio = 0.027937/0.071210                 = 0.392311   (bit-exact to results.json)
t156_session_adjusted = 670.4778/0.392311       = 1709.0453 s
     == 24000 * 0.071210                        = 1709.0453 s  (identical, confirming the algebra)
```

**Sign/direction check.** This session is slower (`speed_ratio<1`), so
the projected same-session cost of the r=156 pilot must come out LARGER
than the historical `670.4778s` figure — and it does (`1709.05s`, a
2.549× inflation), in the correct direction. Had the arithmetic
inverted the ratio (multiplying instead of dividing, or vice versa), a
slower session would have produced a *smaller* projected pilot cost,
which would be nonsensical and immediately visible as wrong — it is not
what happens here.

**Units/commensurability with `t234_cpl25`.** `t234_cpl25=7038.29s` is a
real wall-clock measurement taken entirely in this session, at r=234.
`t156_session_adjusted=1709.05s` is not measured directly at the full
step count, but is dimensionally the same quantity: seconds this session
would spend completing the fixed, historically-known 24000-step r=156
workload, at this session's own measured throughput. Both numerators of
`refit_kappa_exponent(t156, t234)` are now expressed in the same units
(this-session seconds), removing exactly the R9-class defect the naive
version committed (comparing a cross-session t156 directly against a
same-session t234). **I independently confirm this is the correct fix,
not merely a plausible-looking one** — the derivation above is exact, not
approximate, given the stated inputs.

**A second, independent confirmation available in the record itself,
which I checked**: `t156_session_adjusted` (`1709.0453443658805`) is
bit-identical to `cost_gate['scaled']['pilot_total_wall_s']` in
`results.json` — the same object was already being computed for the R31
cost-gate purpose (`cost_gate_check_r31_r234`'s own `scaled_total =
pilot_total_wall_s / speed_ratio`) and is simply reused, not re-derived,
for the kappa-exponent comparator. This is good practice (one code path,
two consumers, verified consistent) and a useful cross-check: anyone
doubting the kappa-exponent correction can instead audit the
independently-motivated, already-reviewed cost-gate arithmetic and get
the identical number.

**Conclusion on Task item 1: the R9 catch is dimensionally sound, correctly
signed, and its central number is independently corroborated by a second,
differently-motivated code path already in the record. I find no defect
in the correction itself.**

---

## 2. Residual confound the correction does NOT address

The task asks specifically whether the R31 control's own short/sustained
blend measures *pure* per-step throughput, or whether scene-construction/
warmup overhead could pollute the ratio in a way that does not cancel
cleanly. I checked this by reading `chunk_runner114.py::_time_control_blend`
directly:

```python
sim = build_sim(g, which)          # scene construction happens HERE
t0 = time.time()                   # timer starts AFTER construction
sim.run(control_steps_per_scene)
total_wall_s += time.time() - t0
```

**Scene-construction overhead (materials placement, `materials.
graded_black_shell`/`pec_disk`) is excluded from the timed interval** —
the clock starts after `build_sim` returns. So construction overhead does
not pollute `speed_ratio`; that specific worry is cleanly closed by the
code as written.

**A different, real residual confound does survive, and I name it
explicitly, as the task instructs.** Two related timing-window issues:

1. **Duration mismatch.** The "sustained" control reading is 3334
   steps/scene (~237s/scene, `712.2/3=237.4s`) — the reading
   `combine_control_readings` actually used. The real r=234 production
   scenes each ran ~2350s (`empty=2355.9s, hollow=2326.2s,
   peccored=2356.1s`) — **roughly 10× longer** than the sustained
   control sample. If throughput continues to degrade with duration
   beyond 3334 steps (e.g. progressive thermal throttling, or
   contention from other panel seats' own concurrent sessions building
   up over the ~40-minute-per-scene production window — Red Team's own
   Phase-2 audit for THIS SAME cycle independently observed `6–10`
   concurrent copies of a shared command and `/proc/loadavg` readings
   of `10–22` under a `nproc=4` sandbox), the sustained control may
   still understate the true degradation a full-length run experiences.

2. **Point-in-time vs. continuously-varying contention.** The control is
   measured once, "at the start of this session" (`chunk_runner114.py`'s
   own docstring), *before* the ~2-hour real spend, not interleaved with
   it or re-measured after. If the shared-container contention Red
   Team's audit documented for this exact cycle got *worse* over the
   session (plausible, given multiple concurrent panel seats' own
   sessions sharing the same box across a multi-hour cycle), the true
   production-window throughput was slower than the control captured —
   which would mean `t156_session_adjusted` is an *underestimate* of the
   true same-session-equivalent pilot cost, and the true `rel_dev` is
   smaller than reported (the CONFIRM verdict would be *more* secure,
   not less). If contention instead *eased* over the session, the
   opposite holds and the true `rel_dev` is larger than reported.

**I do not have the data to sign this confound** — it requires either a
second control reading taken after the real spend (a before/after
bracket) or a continuous throughput log across the production run's own
sub-chunks, neither of which this cycle collected. I flag it as an open,
plausible, currently *unsigned* residual — not as a reason to distrust
the reported CONFIRM, but as a genuine gap the R9 fix, as applied, does
not close. This is exactly the "known, named, not yet closed" shape this
program's own registry (R6 lineage) asks reviewers to state explicitly
rather than silently accept as fully resolved.

**Quantifying how much room there is before this matters** (my own
addition, independent of anything in the record): I computed how much the
true production-window throughput would have to differ from the
control's own reading before the verdict itself moves. Currently
`rel_dev=0.12275` against a `0.15` CONFIRM ceiling. Solving for the
`measured_ratio` that would just reach `0.15`:

```
boundary measured_ratio = reference_ratio * 1.15 = 3.668011*1.15 = 4.218213
current measured_ratio                            = 4.118258
relative headroom                                 = 4.218213/4.118258 - 1 = 2.43%
```

**A same-session throughput swing of only ~2.4% beyond what the control
measured — in the unfavorable direction (production running faster,
relative to history, than the control implies) — would push this cycle's
own falsifiable heart from CONFIRM into AMBIGUOUS.** Given the short vs.
sustained control readings themselves already differ by
`(0.4221-0.3923)/0.3923 = 7.6%` in `speed_ratio` from a mere 1000-vs-3334
step duration change, a further several-percent drift over a 10×-longer
production run is not a remote possibility. **This does not overturn the
CONFIRM verdict** — the gap between the naive (REFUTE, `rel_dev=1.86`)
and corrected (`rel_dev=0.123`) readings is enormous, and no plausible
throughput-drift magnitude closes THAT gap — but the margin inside the
corrected verdict itself is thinner than the headline number alone
conveys, and I record that explicitly rather than letting "CONFIRM with
room to spare" stand unqualified.

---

## 3. Independent recomputation of Fix 1's ratio-space rescoring against the real data

I recomputed every quantity in `classify_kappa_exponent_check` myself,
from the real `results.json` figures, by direct execution (not by
re-reading the document's own prose):

```
t234        = 2355.936572790146 + 2326.2050988674164 + 2356.1488120555878
            = 7038.29048371315 s          (sums exactly to the persisted t234_cpl25)
t156_adj    = 1709.0453443658805 s        (re-derived independently in §1, matches exactly)

exponent_234   = ln(t234/t156_adj) / ln(1.5)               = 3.490880835092507
measured_ratio = 1.5 ** exponent_234  (== t234/t156_adj exactly, by construction) = 4.11825848092089
reference_ratio = 1.5 ** KAPPA_COST_EXPONENT (3.2053299988171697)                 = 3.6680107109370383
rel_dev        = |measured_ratio - reference_ratio| / reference_ratio            = 0.12274985147707763
```

All four bit-exact to `results.json`'s own persisted
`kappa_exponent_result`. Against the Fix-1-corrected bands
(`CONFIRM ≤ 0.15`, `AMBIGUOUS` in `(0.15, 0.30)`, `REFUTE ≥ 0.30`):
`0.1227 ≤ 0.15` → **CONFIRM is the correct, bit-exact-verified verdict**
at the stated bands. I also independently recomputed the naive
(uncorrected) comparison for contrast:

```
naive t156 = 670.4777698516846 s (raw historical, no session adjustment)
naive exponent = 5.798600165690798; naive measured_ratio = 10.497425567547275
naive rel_dev  = 1.8618852001295216  → REFUTE
```

Both bit-exact to `results.json`'s
`kappa_exponent_result_naive_uncorrected_DO_NOT_SCORE`. The correction
moves `rel_dev` from `1.86` to `0.123` — essentially entirely driven by
the `2.549×` (`=1/0.3923`) session-throughput correction, since
`10.497/4.118 = 2.549` exactly. This is the single largest lever in the
whole calculation, which is precisely why §1/§2's scrutiny of that one
factor is where this seat's review effort belongs.

**Consistency check against the cost gate** (my own addition): the
scaled cost-gate projection is `t156_adj * 1.5^K * 1.10 = 1709.0453 *
3.6680107 * 1.10 = 6895.676s`, bit-exact to the persisted
`cost_gate.scaled.projected_234_total_s`, giving a margin of
`1 - 6895.676/10800 = 36.15%` (rounds to the stated "36.2%"), and the
real `t234=7038.29s` sits `2.07%` above that same projection — both
figures I independently confirm match the task's own briefed numbers.

**Conclusion on Task item 3: Fix 1's rescoring machinery is applied
correctly to the real data; CONFIRM is the mathematically correct verdict
at the stated, correctly-derived bands. No arithmetic defect found.**

---

## 4. This seat's own ranked candidates for Iteration 92

1. **Close the R9-correction's own residual timing-window confound named
   in §2** — the cheapest possible version: repeat the sustained
   (3334-step/scene) control reading a second time, immediately *after*
   a future cycle's real FDTD spend completes (not just before it), and
   report the two speed_ratio readings side by side. If they agree
   closely, the point-in-time concern is empirically closed for this
   family going forward; if they diverge by more than a few percent, that
   is itself a new, useful finding about how much this program's shared-
   sandbox contention drifts within a single multi-hour cycle — and
   would bear directly on how much confidence the *already-filed*
   exp-114 CONFIRM deserves, given the ~2.4% headroom computed in §2.
   Zero new FDTD cost beyond one extra control-blend call; this is squarely
   this seat's own energy/rate-bookkeeping charter.
2. **Register the candidate R33 standing rule this cycle proposes**
   (NOTES.md's own Phase-4 section: "an operand-commensurability check
   comparing a cross-session baseline against a same-session measurement
   must apply the session's own already-measured R31 speed_ratio before
   scoring"), generalizing R9 explicitly to R31-adjacent wall-time
   comparisons. I support ratification: this cycle is a genuine,
   real-data founding instance (not the zero-instance/prospective shape
   Red Team correctly declined to ratify at Phase 2) — a naive comparison
   was actually computed, actually would have shipped a materially wrong
   REFUTE verdict, and was caught and corrected before freeze. This
   matches the pattern (a live, would-have-shipped defect, not a
   hypothetical) every prior single-instance-ratified rule (R16, R21–R32)
   in this registry has required.
3. **A third `kappa_ratio` point, this time above 2.0**, per the
   proposal's own honestly-stated Idealization 2: this cycle's CONFIRM
   at `kappa_ratio=1.5` (below the founding `2.0`) does not license
   extrapolating `KAPPA_COST_EXPONENT` above `2.0` — a REFUTE at, say,
   `kappa_ratio=1.5` sits *below* the founding point in the same
   direction the exponent was fit from and is a genuinely different
   generalization question than testing above it. If the still-blocked
   r=312 leg (`kappa_ratio=2.0`, the founding point itself, not a new
   ratio) ever executes, a genuinely new above-2.0 point (e.g. a
   hypothetical r≈470–624 leg, named but never executed since exp-108/110)
   would be the natural next calibration point for this exponent's own
   portability question, using the exact same Fix-1 ratio-space
   machinery this cycle validated.

---

## Trust suite

A single combined `python3 lab/validation/run_all.py --only 12346789`
was attempted from repo root and killed at its own wall-clock ceiling
partway through stage 4 (`ceviche` FDFD cross-check) — `ps aux` during
the attempt showed multiple concurrent copies of this exact command and
of `--only 4` alone under heavy shared-sandbox contention, matching (and,
by direct observation this session, reproducing) the exact contention
this cycle's own `phase2_redteam_audit.md` §0 already disclosed. Falling
back to the individually-run stages (the disclosed acceptable fallback):
stages 1, 2, 3, 6, 7, 8, 9 each completed cleanly on the first attempt
(3+3+4+5+5+6+13 = 39 checks, all `[PASS]`); stage 4 alone needed a second
attempt (the first was killed, exit code 137, under the same contention;
the second completed cleanly in 8s: `ceviche · scattered-pattern corr:
0.956 [PASS]`, `ceviche · lambda (cells): 19.80 [PASS]`, `[PASS]` ×3 —
bit-exact to this cycle's own Phase-2 Red Team audit figures). Naive sum
across all 8 standalone stages = 42, but stages 2 and 3 both separately
recompute and print the shared `ours-small · lambda (cells): 19.96`
prerequisite when run standalone; deduplicating (this program's own R19
discipline — call-count is not distinct-check-count) gives the true
unique-check total: **41/41 green, zero `lab/` diff, no regression** —
matching this program's own long-established combined-run figure exactly,
independently reconstructed from its own parts under real, directly-observed
contention this session, not merely asserted.
