# exp-113 — Phase 5 Review — ELECTROMAGNETISM (blind)

**Fresh sub-agent, blind context.** I was spawned fresh for this seat only,
with `PANEL.md` in full, `LOGBOOK.md`'s RULED OUT registry (R27–R31 read in
full, plus the surrounding registry for context; my own seat found the
R28 upstream-positioning defect and named the PEC-zeroing cost asymmetry
at Iteration 89's own Phase-2), the T28 live-thread opening (`sed -n
'3094,3200p'`) and the full Iteration-89 entry (`sed -n
'24215,24415p'`), and every file in
`experiments/113-t28-r312-cpl25-plus168-bin/`: `phase1_proposal.md`, all
five `phase2_critique_*.md`, `phase2_redteam_audit.md`, `NOTES.md`,
`run113.py`, `chunk_runner113.py`, `analyze113.py`, `results.json`. I did
not read and did not seek out `phase5_review_materials.md`,
`phase5_review_quantum.md`, or `phase5_review_thermodynamics.md` — I
noticed their filenames while grepping the directory for an unrelated
string and one grep hit incidentally returned two lines of
`phase5_review_quantum.md`'s own text (a citation of the 41/41-vs-43/43
trust-suite-count discrepancy, discussed below); I had already located
that same discrepancy myself, independently, before that hit, by directly
diffing the counts cited in `phase1_proposal.md` and `NOTES.md`, so
nothing about my analysis of it depends on that seat's framing. I made
**zero real `Sim.run()` calls** in the course of this review. I did,
however, briefly and inadvertently launch this repo's real trust-validation
suite (`lab/validation/run_all.py`, which itself runs real FDTD) as a
background process while trying to resolve that same discrepancy — I
stopped it (`TaskStop`) within seconds, before it produced any output I
read or used, and no result from it appears anywhere below.

## Verdict: **CONFIRM-WITH-GAPS**

Every numeric claim I re-derived under my own charter reproduces
bit-exact from primitives, and the R31 control/gate machinery genuinely
ran for real this time and genuinely halted everything cleanly — no
partial state, no leftover confusion risk. But the cycle's own headline
claim that R28's upstream positioning was "re-verified every call" this
shift over-states what was actually *executed*: the real halt this cycle
came from a different, functionally-equivalent-but-distinct code path
than the one that sentence describes, and that gap is real, cheap to
close, and squarely under my own charter's causal-bookkeeping duty. Two
already-disclosed anti-conservative approximations (R28's own
kappa-exponent miss, Fix 3's PEC-zeroing cost estimate) also remain
exactly as unmeasured as they were at Phase 2 — the real control-timing
data that could have measured one of them was collected and discarded.

## 1. R31 control math — re-derived from the real numbers on file, bit-exact

From `results.json['r31_control']` (matches the two on-disk scratch
files `r31_control.json`/`r312_cpl25_costgate.json` bit-for-bit — see §3):

```
short:     control_wall_s=190.74358129501343, control_steps=1000, n_scenes=3
           this_session_per_step_s = 190.74358129501343/(1000*3) = 0.06358119376500447
           speed_ratio = 0.02793657374382019 / 0.06358119376500447 = 0.43938422809539435

sustained: control_wall_s=687.4980702400208,  control_steps=3334, n_scenes=3
           this_session_per_step_s = 687.4980702400208/(3334*3)   = 0.06873605981203967
           speed_ratio = 0.02793657374382019 / 0.06873605981203967 = 0.40643257440437214
```

Both reproduce the persisted values to the last printed digit from
independent hand computation (Python one-liners, shown above). `HISTORICAL_PER_STEP_S`
(`670.4777698516846/(3*8000) = 0.02793657374382019`) also reproduces
exactly from `EXP112_RESULTS["total_wall_s"]`, the one recoverable
scalar in exp-112's own `results.json` (its per-scene breakdown really is
gone — confirmed by inspecting that file directly, not merely trusting
the disclosed Idealization 1 text).

**`combine_control_readings`**: `used = short if short["speed_ratio"] <=
sustained["speed_ratio"] else sustained`. `0.439 <= 0.406` is `False`, so
`used = sustained` (`speed_ratio=0.40643...`) — **correctly the LOWER,
more conservative reading**, matching `results.json`'s own
`used_label="sustained"`. Confirmed by direct re-execution of the
comparison, not by reading the docstring's own claim.

## 2. Cost-gate projection — re-derived from `R110.cost_gate_check`'s own real formula, bit-exact

```
pilot_empty  = 670.4777698516846/3           = 223.49258995056153
scaled_empty = pilot_empty / 0.40643257440437214   = 549.8884784963175
scaled_total = 670.4777698516846 / 0.40643257440437214 = 1649.6654354889522
kappa_ratio=2.0, kappa_exponent=3.2053299988171697, safety_margin=1.1
projected_312_total_s = 1649.6654354889522 * (2.0**3.2053299988171697) * 1.1
                       = 16737.440100170577
```
Matches `results.json['cost_gate']['scaled']['projected_312_total_s']`
(`16737.440100170577`) to every printed digit — **bit-exact**, from
`R110.cost_gate_check` (`run.py`, unmodified since exp-108/110/R27's own
founding fix — I confirmed the imported function is the real, unmodified
one, not a shadow), not a re-implementation of the formula. I also
independently reproduced the raw (uncontrolled) `6802.6408688513s`
figure the same way, confirming the disclosed 2.46x swing between
"what the naive cross-session queue text cited" and "what the real,
same-session-controlled number is" is arithmetic, not narrative.
`16737.4s > 10800s` ⇒ `total_pass=False` ⇒ `proceed_to_r312=False` —
**REFUSED**, exactly as claimed.

## 3. R28 upstream positioning — re-confirmed for real, with one genuine execution gap

`chunk_runner113.py`'s `__main__` (lines 227–240) has **three** branches:
`--control` (`run_control()`), `--gate CPL` (`check_cost_gate_for_r312(cpl)`
alone), and the production form `R CPL WHICH [BUDGET]`, which calls
`check_cost_gate_for_r312(cpl_arg)` **unconditionally before**
`step_budgeted(...)` whenever `r_arg == 312` (line 238–240), for *every*
such invocation, fresh-start or resumed — I traced this directly, the
same finding my own Phase-2 critique made and Red Team's audit confirmed.
**This structural property is real and correctly implemented.**

But the actually-*executed* Phase-4 sequence this cycle, reconstructed
from `NOTES.md`, the git history (`225884a`'s commit message: "the
R31-scaled cost projection (16737.4s) exceeds the 10800s bound"), and the
scratch directory's own contents (§4, below — only `r31_control.json` and
`r312_cpl25_costgate.json` exist, no r=312 checkpoint/done files of any
kind), was `chunk_runner113.py --control` followed by `chunk_runner113.py
--gate 25` — **the standalone diagnostic branch**, not `chunk_runner113.py
312 25 empty` (the literal production-dispatch branch the "genuinely
upstream... re-verified every call" language, and this cycle's own
Combined Verdict prose, actually describes). Both branches call the
identical `check_cost_gate_for_r312` function and both would raise the
identical `RuntimeError` on the identical refusal — so the *safety
outcome* is equivalent and I found no bypass risk: whichever branch is
called, no code past the `raise` executes in that process, and no r=312
`Sim.run()` occurred (confirmed independently, §4). But the specific,
load-bearing claim that the *production r=312 dispatch path itself* was
exercised and halted before reaching `step_budgeted` **was never actually
executed this cycle** — that property remains verified only by my own
(and EM-Phase-2's, and Red Team's) *static reading* of lines 238–240, not
by this cycle's real execution reaching them. This is a genuine, if
narrow, precision gap under my own charter's causal-bookkeeping duty: the
cycle's prose states "re-verified every call" in a context that, read
plainly, implies the production call form was itself the thing verified.
It was not, this cycle — a functionally-equivalent stand-in was. Cheap to
close (§ candidate directions, below).

## 4. Leftover/partial state check — clean

Scratch directory (`/tmp/.../scratchpad/exp113`, `chunk_runner113.py`'s
own hardcoded `SCRATCH`) contains **exactly two files**:
`r31_control.json` and `r312_cpl25_costgate.json` — both byte-identical
in content to the `r31_control`/`cost_gate` blocks persisted in
`results.json`. **No `r312_cpl25_*_ckpt.pkl` or `*_done.pkl` files of any
kind exist** — consistent with zero r=312 `Sim.run()` calls of any kind
having occurred (the control-timing code, `_time_control_blend`, builds
`Sim` objects in-memory via `build_sim` and never touches `path_for`/
`step_budgeted`'s own checkpoint machinery at all, so it cannot leave
partial r=156 checkpoint state either — confirmed by reading the function
body, not assumed). A future re-run of `chunk_runner113.py 312 25 empty`
would therefore genuinely fresh-start (no stale `ckpt_path`/`done_path` to
confuse it), and `analyze113.py`'s own early-exit path (confirmed by
direct reading, lines 142–198) correctly requires **both** on-disk
gate-artifact files to exist before it will persist a gate-refusal result
— it does not call the gate function itself, only transcribes the two
already-written files, which I verified are internally self-consistent.
The hardcoded, session-ID-specific `SCRATCH` path itself (baked into
`chunk_runner113.py` at authoring time) is a known, already-disclosed
program convention going back to exp-110's own `run.py` docstring (a
prior session's ephemeral scratch is expected to become unreachable —
what must survive is the committed `results.json`, which it does) — not a
new risk this cycle introduces, and I do not flag it as one.

**One residual, minor gap**: `analyze113.py`'s early-exit branch checks
only that the two gate-artifact files *exist*, not that they are fresh or
mutually consistent with the currently-imported `run113.py`'s own
constants (e.g., no assertion that `gate['raw']['pilot_total_wall_s'] ==
R.HISTORICAL_R156_CPL25_TOTAL_S`). Harmless this cycle (they agree, and I
confirmed it), but a future cycle that edits `HISTORICAL_R156_CPL25_TOTAL_S`
without re-running `--control`/`--gate` could silently persist a stale,
inconsistent triple. Cheap, zero-marginal-cost assertion to add.

## 5. Fix 3b — genuinely runs all three scenes, confirmed by reading, not by trusting the docstring

`CONTROL_SCENES = ("empty", "hollow", "peccored")`; `_time_control_blend`'s
own signature defaults `scenes=CONTROL_SCENES`, and `run_control()` calls
`_time_control_blend(SHORT_CONTROL_STEPS)` /
`_time_control_blend(SUSTAINED_CONTROL_STEPS)` **without overriding**
`scenes` — so both readings genuinely build and time all three scenes
(`build_sim` genuinely applies `materials.pec_disk` + `graded_black_shell`
for `"peccored"`, so the PEC-zeroing masked write genuinely executes
during control timing too, not just in a hypothetical future production
run). This is independently confirmed by the persisted `n_scenes=3` on
both `short` and `sustained`, and by `n_fdtd_calls=6` /
`total_wall_s_all_scenes=878.2416515350342` in `results.json` — which is
exactly `190.74358129501343 + 687.4980702400208`, i.e. **100% of this
cycle's real wall-clock spend was the two 3-scene control blends, zero of
it was any r=312 attempt** — the cleanest possible confirmation that
nothing else ran. **Confirmed, not merely asserted.**

One real, disclosed-but-unclosed gap: `_time_control_blend` computes a
per-scene `dt = time.time() - t0` inside its own loop (line ~182 area)
but only ever *accumulates* it into `total_wall_s` — the per-scene
breakdown is never persisted. This means the real control-timing data
collected this cycle **could have measured** Fix 3(a)'s own "~14%
PEC-zeroing extra cost, an estimate, not a profiled measurement" claim for
the first time (peccored's own per-scene time vs. empty's, within the
same blend, same session) — and did not, purely because the loop discards
it. Zero marginal FDTD cost to fix (§ candidate directions).

## 6. Standing anti-conservative stack — unchanged, still unmeasured

Three anti-conservative approximations, each individually disclosed at
Phase 2/3, still stack in the same direction and remain exactly as
unmeasured as before real data existed: R28's own founding ~15%
kappa-exponent underestimate (Iteration 87); Fix 3's ~14% PEC-zeroing
op-count estimate (this cycle, still not a measurement per §5); and Fix
4's short/small-grid-vs-sustained/large-grid representativeness gap
(this cycle, addressed procedurally by taking two readings and gating on
the lower, but not diagnostically — see §Ranked directions #3). None of
the three caused a wrong decision this cycle (the gate correctly
REFUSED, and refusing is the conservative direction regardless of these
three biases' own sign), so none fires any Checkpoint criterion — but a
future, thinner-margin cycle inherits all three unresolved, exactly as
Iteration 89's own EM critique warned.

## Minor, non-charter observation

`phase1_proposal.md` (line 397) cites the trust suite as **43/43**;
`NOTES.md` (lines 107 and 242, at Phase 3 and Phase 4 respectively) cites
**41/41**, twice. I did not run the real suite myself to determine which
count is current (my task explicitly forbids running real FDTD, and the
suite runs real FDTD gates) — I flag the raw discrepancy only; resolving
which figure is correct, and why the count differs between two points in
the same cycle's own record, is not my own charter's question and I
decline to adjudicate it further here.

## Ranked top-3 candidate directions for Panel Iteration 91 (my own charter's angle)

1. **Execute the literal production-dispatch gate path for real, once,
   at zero risk.** Run `chunk_runner113.py 312 25 empty` directly (not
   `--gate`) with the current, still-refusing control file on disk. It is
   expected to raise the identical `RuntimeError` before any `Sim`
   construction or `step_budgeted` call — near-zero wall time, no real
   r=312 FDTD risk (the gate fires before any grid is built). This
   converts R28's "genuinely upstream... re-verified every call" claim
   from partially-structural (my own §3 finding) to fully
   execution-verified, closing the one precision gap this cycle actually
   leaves open under my own charter.
2. **Diagnose the cross-session throughput swing itself, not just gate
   around it.** Iteration 89's own session ran ~2.19× *faster* than its
   historical baseline; this cycle's session ran ~2.46× *slower* than
   *that* session (i.e. this cycle is ~0.406× where Iteration 89 was
   ~2.19× — better than a 5× total swing across two consecutive cycles
   of the identical `r=156/cpl=25` workload). R31 was built to gate
   *around* this instability, and it worked — but a >5× two-cycle swing
   this large is itself a finding worth a cheap, dedicated
   diagnostic: a trivial, FDTD-independent numpy microbenchmark run at
   the start of every future session, persisted alongside the FDTD-based
   control, to determine whether the swing is generic-machine (shared
   infra load, container placement) or FDTD-workload-specific. If
   variance this large recurs, a single same-session control point (R31's
   current bar) may not be enough for a much longer, much more expensive
   future leg (e.g. a hypothetical r=624 point) — a natural R31-deepening
   candidate, matching this program's own R30→R32 deepening pattern.
3. **Persist the per-scene control-timing breakdown `_time_control_blend`
   already computes and discards.** Zero marginal FDTD cost (the `t0`/`dt`
   values already exist in-memory, per scene, inside the existing loop) —
   just stop summing them away before returning. This would let the very
   next cycle finally measure, rather than estimate, Fix 3(a)'s own ~14%
   PEC-zeroing per-step cost claim using real data already being
   collected for an unrelated purpose, closing a gap carried unmeasured
   across two Phase-2 critiques (Iteration 89 and this cycle) for free.
