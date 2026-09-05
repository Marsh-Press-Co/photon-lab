# exp-114 — Panel Iteration 91

## Phase 1 — Propose (PHOTONICS)

See `phase1_proposal.md` in full. Executes the Reconciled Iteration-91
queue's Tier-1 item 3: a cheaper intermediate-`r` calibration point
(`r=234`, `fixedabs` family, `cpl=25`) for `KAPPA_COST_EXPONENT`, chosen
because it does not depend on the r=312 leg's own repeated cost-gate
deferrals (exp-111/112/113) and can proceed in parallel. Verified,
before proposing (R4/R9): `r=234` never previously used for this family
(two prior unexecuted Phase-5 proposals existed, for two DIFFERENT
quantities — disambiguated in Idealization 4); the estimated cost is
safely inside `COST_GATE_TOTAL_S` via the real committed cost-gate
formula (uncontrolled projection 2705.3s, 75.0% margin). Corrected a
real citation defect in MATERIALS' own Iteration-90 Phase-5 review (true
cost multiplier `3.668×`/`≈39.8%`, not the filed `≈2.98×`/`≈32%`). T1
escape route N/A throughout (instrument-calibration work, no
phenomenon-mechanism content).

## Phase 2 — Critique

Five blind critiques (`phase2_critique_materials.md`,
`phase2_critique_em.md`, `phase2_critique_thermodynamics.md`,
`phase2_critique_quantum.md`, `phase2_critique_vision.md`), all
**support-with-changes**, zero opposition. Red Team's audit
(`phase2_redteam_audit.md`) independently re-derived every cited figure
from primitives, confirmed all defects found, and found one additional
consequential defect underneath EM/VISION's convergent finding
(QUANTUM's own point that the exponent-space band's real-world
stringency is itself `kappa_ratio`-dependent). Verdict:
**PROCEED-WITH-MANDATORY-FIXES.**

## Phase 3 — Synthesis (Director)

**All four of Red Team's mandatory-fix-docket items accepted in full,
applied this shift, before any Phase-4 `Sim.run()` call — no criticism
overridden** (Red Team's own words: "None of the four rises to a
disclosed-override candidate").

1. **Fix 1 (EM/VISION/QUANTUM, consolidated by Red Team — 0.15/0.30
   band citation + second-order kappa_ratio-dependent-stringency
   defect)**: `run114.py::classify_kappa_exponent_check()` is rewritten
   to score in **ratio space**, not exponent space — Red Team's route
   (a). `measured_ratio = kappa_ratio ** exponent_234` (mathematically
   identical to the real measured `t234/t156`) is compared against
   `reference_ratio = kappa_ratio ** KAPPA_COST_EXPONENT`, both
   evaluated at THIS leg's own `kappa_ratio=1.5` — the same space and
   the same real founding figure (`2.0**3.2053.../2.0**3.0 - 1 =
   0.1530 ≈ R28's own cited "~15%"`) the 0.15/0.30 bands were always
   meant to reuse, and now `kappa_ratio`-invariant in real-world
   stringency by construction (closing QUANTUM's second-order finding,
   not just the citation). Verified by direct execution: an exact-match
   synthetic `exponent_234` scores `rel_dev=0.0` (CONFIRM); a synthetic
   ratio-doubling scores `rel_dev≈1.0` (REFUTE) — both `--predictions-
   only` and a standalone smoke test re-run clean post-edit.
2. **Fix 2 (QUANTUM's own finding, ratified by Red Team — LOGBOOK
   propagation)**: `LOGBOOK.md:24638`'s own frozen Iteration-90
   "Reconciled Iteration-91 queue" text ("~32%") is arithmetically
   wrong (true: `≈39.8%`) and this document's own R4 correction
   (`run114.py`'s `DISCLAIMER`) reaches only the originating
   `phase5_review_materials.md` citation, not the more permanent
   LOGBOOK record itself. Per this program's own established practice
   (never retroactively edit a frozen entry — disclose forward), **this
   NOTES.md is that forward disclosure**: Iteration-90's own "~32%"
   figure was arithmetically wrong; the correct figure, independently
   re-derived and confirmed by both `phase1_proposal.md` and Red Team's
   audit, is `1.5**3.2053299988171697 / 2.0**3.2053299988171697 ≈
   0.397677` (`≈39.8%`). Non-fatal to that review's own qualitative
   conclusion (r=234 remains comfortably the cheaper option). The
   Iteration-91 LOGBOOK entry (below, at this cycle's close) restates
   this correction in the permanent record.
3. **Fix 3 (THERMODYNAMICS' finding, broadened by Red Team — missing
   `analyze114.py`)**: authored `analyze114.py`, mirroring
   `analyze113.py`'s own structure: `sc.widths()` on the real
   hollow/peccored captures → `energy_ledger` (THERMODYNAMICS' own
   fix); `refit_kappa_exponent()`/`classify_kappa_exponent_check()`
   (Fix-1-corrected) on the real `(t156,t234)` pair, invoked for the
   first time by any committed script (Red Team's broader finding —
   these functions existed but were dead code through Phase 2);
   `R.DISCLAIMER in {predictions,result}_text` R23 asserts; a
   gate-refused branch (mirroring `analyze113.py`'s own, in case R31
   refuses this leg the way it refused r=312 last cycle) and a
   not-yet-complete branch. This leg does NOT invoke the angular-pattern/
   named-bin machinery (Idealization 3, unchanged) — `repro_ok` is
   reported `N/A`, stated explicitly in `result_text`, not silently
   dropped. Verified: `python3 analyze114.py` (no real r=234 data on
   file yet) prints the correct "not yet complete" message and exits
   cleanly; a standalone smoke test of the gate-refused and real-data
   text-builder paths (synthetic control/gate/kappa_exponent dicts) both
   produce `R.DISCLAIMER`-compliant text with no exception.
4. **Fix 4 (MATERIALS' own finding, ratified by Red Team — declined-
   items omission)**: `phase1_proposal.md` §3 now names MATERIALS' own
   fabrication-tolerance quantitative bound as a fifth declined,
   not-silently-dropped item (Phase-3 correction blockquote, matching
   this program's own established forward-disclosure convention) —
   restoring the three-cycle restatement chain exp-111/112/113 each
   maintained. No code or geometry change; Tier 2, unaffected by this
   leg's own question, carried forward to Iteration 92 unchanged.

**New standing rule?** Red Team considered and explicitly **declined**
to mint one this cycle (Fix 3's own risk-shape — "a falsifiable check's
scoring function must be invoked by committed code before real data can
be trusted against it" — generalizing the R16/R21 persisted-but-not-
narrated lineage) on the same zero-founding-instance ground this
program's registry has always required: nothing was actually mis-scored
(Phase 4 had not run; the gap was caught blind, at Phase 2, before any
freeze). **Named as a watched risk instead** (Red Team's own words,
`phase2_redteam_audit.md` §4): its founding-instance trigger is a future
T28 cycle that freezes a Result/NOTES.md verdict citing a classification
function never actually called by committed code. Director concurs —
no R33 minted this cycle.

**T1 escape route: N/A**, confirmed independently by every seat
(five blind critiques + Red Team, six routes) and by direct code
inspection at Phase 3 — no σ(I)/σ(x,t)/angular-selectivity/sub-threshold
content anywhere in this cycle; no constraint-1/2/3/4 verdict is scored
or moved.

**Verification of all four fixes, before any Phase-4 `Sim.run()` call**:
`python3 run114.py --verify-geometry` → `pass_=true` at r=156/234/312
(unchanged, re-run post-edit). `python3 run114.py --predictions-only` →
renders cleanly, Fix 1's ratio-space bands and Fix 2's own R4-corrected
figures both appear bit-exact to the values quoted above. Synthetic
zero-FDTD checks of `classify_kappa_exponent_check` (exact-match →
CONFIRM/`rel_dev=0`; doubled ratio → REFUTE/`rel_dev≈1.0`) and of
`analyze114.py`'s own text-builder paths (gate-refused branch;
real-data branch with a synthetic `kappa_exponent_result`) all behave
correctly. `python3 analyze114.py` (no real r=234 data) exits cleanly
with the correct "not yet complete" message. Trust suite green
throughout (41/41 — re-confirmed by the Director this shift, one clean
combined `--only 12346789` invocation once the Phase-2 seats' own
concurrent sessions had finished, resolving the partial-confirmation gap
VISION SCIENCE's and THERMODYNAMICS' own Phase-2 critiques disclosed
under shared-sandbox contention — see Phase 4/Result for the exact
figure), zero `lab/` diff throughout Phase 3.

## Setup

Congruent `cpl=20→25` (ratio 1.25×) grid-resolution refinement of the
`fixedabs` family (exp-106/108/110/112/113's own hollow-vs-PEC-cored
geometry) at **r=234** (kappa_of(234)=3.0, kappa_ratio=1.5 relative to
the r=156/cpl=25 pilot), targeting a fresh `(t156,t234)` wall-time pair
to check `KAPPA_COST_EXPONENT`'s own generalization across `kappa_ratio`
for the first time since its founding (a single `kappa_ratio=2.0` pair,
exp-110/111). Geometry reused unmodified from `run112.py::geom_
fixedabs_cpl`, extended to r=234 and verified byte-exact to
`R110.geom_fixedabs` at that r for the first time (`verify_geometry_
identity()`, above). 3 real FDTD calls this cycle (empty/hollow/
peccored, r=234, cpl=25), R31-gated by a same-session control point
measured at the start of Phase 4 (before the real spend, per house
discipline) — `chunk_runner114.py --control` then `--gate 25`,
reusing `run113.py`'s own control-timing machinery unmodified except
for the one disclosed `kappa_ratio`-parameterized line
(`cost_gate_check_r234`).

## Predictions (committed to git BEFORE any Phase-4 code is executed for
## real, house discipline, non-negotiable — verbatim quote of
## `run114.py::build_predictions_text()`'s own output, post-Fix-1/Fix-2,
## WITHOUT the control/gate figures, which do not exist until Phase 4's
## own R31 control point is measured)

```
PREDICTIONS (pre-registered, exp-114, Panel Iteration 91)

[DISCLAIMER — see run114.py::DISCLAIMER, quoted in full in
phase1_proposal.md and reproduced by `python3 run114.py
--predictions-only`; omitted here for length, unchanged since the last
`--predictions-only` re-run this document cites]

**Geometry identity (zero-FDTD, pre-Phase-4)**: verify_geometry_identity()
returns pass_=True at r=156, r=234 (new), AND r=312. Falsified by any
mismatch -- HALT before any Sim.run() call. (Already run, PASS.)

**Reproduction/self-consistency precondition**: N/A this cycle — the
angular-pattern instrument is not invoked (Idealization 3); no
sigma_scat_per_bin check is computed or scored.

**Cost gate (the genuinely uncertain question this leg exists to answer
cheaply)**: UNCONTROLLED reading = 2705.3s vs. the 10800s bound (75.0%
margin if this reading held) -- explicitly NOT the gating figure. R31
requires a fresh same-session control point (chunk_runner114.py
--control) before proceed_to_r234 governs any real spend --
proceed_to_r234 may read False even though the uncontrolled projection
looks comfortable, exactly as it did for the r=312 leg last cycle
(37% uncontrolled margin, REFUSED once R31-controlled for real).

**kappa_exponent generalization check (the falsifiable heart of this
cycle, Fix-1-corrected -- scored in RATIO space)**: once real t156
(already on file, 670.4778s) and a fresh real t234(cpl=25) both exist,
refit_kappa_exponent() computes exponent_234 = ln(t234/t156)/ln(1.5).
measured_ratio = 1.5**exponent_234 (== t234/t156 exactly) scored against
reference_ratio = 1.5**KAPPA_COST_EXPONENT = 3.668011 (the founding
exponent's own prediction at THIS leg's own kappa_ratio):
CONFIRM if relative deviation (ratio-space) <= 0.15;
AMBIGUOUS if 0.15 < relative deviation < 0.30;
REFUTE if relative deviation (ratio-space) >= 0.30.
The 0.15/0.30 bands are ratio-space bounds matching R28's own founding
miss (2.0**3.2053.../2.0**3.0 - 1 = 0.1530) in the SAME space, at ANY
kappa_ratio -- not an exponent-space bound whose real-world stringency
would otherwise vary with kappa_ratio. No advance position is taken on
which band this cycle's own real data will land in.

**Fix 1 (box_a clearance in wavelengths, zero-FDTD, computable now)**:
3.2 lambda at r=156, 4.8 lambda at r=234 (new, exactly the linear
midpoint), 6.4 lambda at r=312 -- a geometry fact, not a pass/fail band.

**Fix 2 (sponge-margin figures)**: the domain-edge sponge's own one-way
accumulated log-attenuation is IDENTICAL at r=234 to r=156/312
(17.242357, exp(-17.242357)=3.249e-08) -- the margin-against-signal/floor
split cannot be computed until Phase 4 produces a real r=234
measurement; not predicted here.

**Fix 3 (energy ledger, THERMODYNAMICS/Red Team)**: sigma_scat/sigma_abs/
sigma_ext/sigma_ext_cross for both hollow and peccored r=234 captures
will be persisted via analyze114.py's own sc.widths() call once real
data exists -- no advance position taken on their values; a real,
non-zero absorbed-power reading is expected (graded_black_shell,
tau_shell=24, genuinely absorptive), not itself a falsifiable claim this
cycle scores against a band.
```

Falsified/HALT conditions above are hard blockers — Phase 4 must not
proceed past a HALT to the kappa_exponent comparison.

## Phase 4 — Test

**R31 same-session control** (`chunk_runner114.py --control`): short
(1000 steps/scene, 198.5s, speed_ratio=0.4221) and sustained (3334
steps/scene, 712.2s, speed_ratio=0.3923) 3-scene-blend re-timings of the
r=156/cpl=25 pilot — `combine_control_readings()` correctly selected the
sustained (lower, more conservative) reading. **This session ran at
~0.392× the historical (Iteration-89-derived) session's own per-step
speed** — i.e. genuinely SLOWER, in the same direction as exp-113's own
finding (0.406×), reinforcing that "faster than historical" (Iteration
89's own +2.19× reading) is not the reliable default.

**Cost-gate re-check** (`chunk_runner114.py --gate 25`): R31-scaled
projection = **6895.7s** vs. the 10800s bound — **APPROVED** (36.2%
margin). Unlike the r=312 leg (refused three times running, exp-111/
112/113), this leg's own lower `kappa_ratio=1.5` keeps it comfortably
inside the bound even at this session's slow throughput — confirming the
proposal's own stated rationale for choosing r=234 (Tier-1 item 3,
"immune to a fourth session-speed-driven deferral").

**Real FDTD spend**: 3 real scenes (empty/hollow/peccored) at r=234,
cpl=25, run via time-budgeted, checkpointed `chunk_runner114.py` calls.
Total: empty=2355.9s, hollow=2326.2s, peccored=2356.1s —
**7038.3s total (117.3 min)**, ~2% ABOVE the R31-scaled projection
(6895.7s) but comfortably inside the 10800s hard bound (35% margin
remaining) — disclosed, not smoothed over: the projection is a
single-point extrapolation from one same-session control reading, not a
promise, and a small overrun is exactly the kind of residual variance
R31 itself does not claim to eliminate.

**Phase-4 correction (Director's own catch, R9 discipline — a real
defect, caught before any result was frozen, not by any Phase-2 seat
since `analyze114.py` did not exist until Phase 3)**: the first run of
`analyze114.py` fed the falsifiable-heart comparison
(`refit_kappa_exponent`) the raw cross-session historical `t156`
(670.4778s) directly against this session's own real `t234` (7038.3s) —
an operand-commensurability defect exactly of the class R9 exists to
catch ("verifying a ratio's arithmetic ≠ verifying its operands are
commensurable"): this session's own R31 control had ALREADY measured
that it runs at 0.392× historical throughput, so comparing a
cross-session historical figure against a same-session real measurement
conflates genuine `kappa_ratio` cost-scaling with an unrelated,
already-quantified session-speed difference. The naive, uncorrected
comparison gave `exponent_234=5.799`, `rel_dev=1.862` (186%) —
**REFUTE** — which would have been a materially wrong scientific
conclusion. Corrected `analyze114.py` to score against the historical
`t156` **rescaled by this session's own measured R31 `speed_ratio`**
(`t156_session_adjusted = 670.4778/0.3923 = 1709.045s`, exactly the
figure the cost gate's own `scaled.pilot_total_wall_s` already computed
for the cost projection — reused, not re-derived) — the session-
normalized, correctly-scored result is below. The naive/uncorrected
reading is retained in `results.json` under
`kappa_exponent_result_naive_uncorrected_DO_NOT_SCORE`, disclosed, not
deleted, so the size of the confound this correction removes stays
visible. **This is registered as a candidate standing rule (R33) at this
cycle's close** — see LOGBOOK.md.

## Result

Verbatim quote of `analyze114.py`'s own `result_text` (`results.json`):

```
RESULT (exp-114, Panel Iteration 91)

[DISCLAIMER -- unchanged, see above]

3 real FDTD calls, 7038.3s (117.30 min)
total wall time this cycle, zero `lab/` diff.
(exp-114's own genuinely new r=234/cpl=25 spend, R31-gated by a
same-session control. Reproduction/self-consistency precondition: N/A --
this leg does not invoke the angular-pattern instrument (declined by
scope, Idealization 3). Phase-4 correction (Director's own catch, R9):
kappa_exponent_result is scored against a same-session-normalized t156
(1709.0453s, the historical pilot rescaled by this session's own R31
speed_ratio=0.3923), NOT the raw cross-session historical t156
(670.4778s) directly -- the naive uncorrected comparison is disclosed,
not scored, in kappa_exponent_result_naive_uncorrected_DO_NOT_SCORE
(verdict=REFUTE (kappa_exponent is kappa_ratio-dependent, not a portable
constant), rel_dev=1.8619).)

**Geometry identity: PASS.**
**Reproduction/self-consistency precondition: N/A (not reached).**
**Cost gate:** {raw: proceed=true (2705.3s/10800s); scaled: proceed=true
(6895.7s/10800s, this session's own R31-controlled projection)}
**kappa_exponent generalization check:** exponent_234=3.490881,
measured_ratio=4.118258, reference_ratio=3.668011,
rel_dev(ratio-space)=0.1227, verdict=CONFIRM (kappa_exponent generalizes
across kappa_ratio)
```

**Energy ledger** (THERMODYNAMICS'/Red Team's Fix 3(a), zero marginal
FDTD cost): peccored `sigma_scat=551.585`, `sigma_abs=541.883`,
`sigma_ext=1093.468`; hollow `sigma_scat=551.645`, `sigma_abs=541.880`,
`sigma_ext=1093.525` — real, non-zero absorbed power confirmed, as
THERMODYNAMICS predicted (`graded_black_shell`, genuinely absorptive),
now persisted rather than silently discarded.

Trust suite green throughout (41/41, 98s, clean single combined run,
zero contention this check), zero `lab/` diff, confirmed both before and
after Phase 4.

## Phase 5 — Review

Six blind Phase-5 reviews (VISION, MATERIALS, EM, THERMODYNAMICS,
QUANTUM, PHOTONICS self-review): VISION/MATERIALS promising;
EM/PHOTONICS promising-with-a-named-caveat; THERMODYNAMICS/QUANTUM
partial. Every seat independently re-derived the R9 fix's own arithmetic
bit-exact — zero wrong numbers in the executed chain. But three seats
(EM, QUANTUM, PHOTONICS) each found a DIFFERENT, non-overlapping residual
confound underneath the correction: (1) EM — the R31 sustained control
(3334 steps/scene) is ~10× shorter than the real production run
(~2350s/scene) and measured once, before the spend, not bracketed after;
only ~2.4% further unfavorable drift would flip CONFIRM to AMBIGUOUS.
(2) QUANTUM — choosing the "short" control reading instead of
"sustained" (both same-session, both on file) flips the verdict to
AMBIGUOUS outright; the sustained/lower-of-two selection rule was
ratified (Iteration 90) for cost-gate safety-margin purposes, never
independently re-justified for this different, symmetric-risk scientific
use. (3) PHOTONICS — the deepest finding: the R31 control is measured
EXCLUSIVELY on the r=156 grid (N=1400) and applied to rescale a verdict
built from r=234-grid (N=2100, 2.25× cells) data — untested whether
session slowdown transfers uniformly across grid sizes, physically
plausible it doesn't (larger arrays more memory-bandwidth-bound).

The Director's own exploratory follow-up (using already-collected,
zero-marginal-cost cold-build r=234 timing data to construct an
alternative "v2" normalization via an N²-per-step-scaling assumption)
was handed to Red Team for independent assessment rather than added to
the record directly, given uncertainty whether it was a valid check.

## Phase 5 — Red Team final audit (`phase5_redteam_audit.md`)

Independently re-verified every headline figure across all six reviews
bit-exact; caught one non-outcome-reversing R4-class transcription slip
in an earlier revision of MATERIALS' own table, already self-corrected
in the committed record. **Extended the Director's "v2" check and found
something more consequential than the Director's own stated uncertainty
suggested: the two leading correction methods (sustained-control vs.
N²-scaling) place `measured_ratio` on OPPOSITE SIDES of `reference_ratio`
(4.118 vs. 3.217, a 28.0% spread between the two central estimates) — a
straddle, not a corroboration.** Ruled the v2 calculation should NOT
enter the record as supporting evidence, only as a further sensitivity
finding (recorded here for that reason, not as a scored result).

**Verdict-framing ruling: CONFIRM-WITH-NAMED-GAPS** — not plain CONFIRM
(would understate what three independent seats plus this audit's own
extension found); not a downgrade to AMBIGUOUS (would violate R7 — a
robustness argument alone, without a validated superior replacement
method, cannot override a correctly-executed pre-registered test; there
IS an independently-ratified physical argument favoring "sustained"
(Iteration 90); every alternative method tried stays nowhere near the
0.30 REFUTE line — the qualitative conclusion is robust, only the
precise tier boundary is fragile).

**Checkpoint criterion 4: does not fire** — a healthy Phase-5 catch
working as designed (Phase 2 caught the dead-code gap; the Director's
own Phase-4 R9 catch caught a more serious defect before any freeze;
Phase 5 found three further, mutually-independent, deeper layers of the
SAME question, not the same defect recurring unfixed) — conditioned on
promoting all three named confounds to explicit Iteration-92 Tier-1
queue lines (done; see LOGBOOK.md/PLAN.md for the full Reconciled
queue).

**R33 ratified**, core + both QUANTUM's and PHOTONICS' scoping addenda +
VISION's wording fixes — full text in `phase5_redteam_audit.md` §5,
reproduced in LOGBOOK.md's own registry at this cycle's close.

**Escalation**: Red Team's audit flags the Iteration-85 Checkpoint-4/R24
firing as now SEVEN cycles pending without Marsh's own convening —
escalated directly this shift (see SESSION_LOG.md).

## Combined Verdict (Director, final)

**CONFIRM-WITH-NAMED-GAPS** (Tier 1 falsifiable question) + a genuine,
self-caught R9 defect, now generalized into standing rule R33 (Tier 0
process finding) — both real, both disclosed, both now closed out.
`KAPPA_COST_EXPONENT` (fit from a single `kappa_ratio=2.0` pair,
exp-110/111) **generalizes to `kappa_ratio=1.5` under the pre-registered,
correctly ratio-space-scored rule** (`rel_dev=0.1227`, CONFIRM) — the
first real check of this exponent at any ratio other than its own
founding one — but the correction underlying that number rests on an
unverified cross-grid-transfer assumption that, under one equally
defensible alternative, would place the true ratio on the *other side*
of the reference value. Genuine, disclosed non-null progress on four
fronts: (1) the falsifiable heart resolves CONFIRM-WITH-NAMED-GAPS, not
AMBIGUOUS or REFUTE, under a rule the whole panel scrutinized and
believes robust in its qualitative conclusion; (2) this leg's own choice
of the lower-`kappa_ratio` r=234 (explicitly to avoid a fourth
r=312-style deferral) is vindicated — cost gate approved on the first
attempt, 36.2% margin; (3) a real, consequential R9-class defect was
caught and fixed by the Director before any result was frozen; (4) that
catch generalized into R33, a new standing rule with two independently-
sourced scoping addenda, closing exactly the kind of gap that produced
it. Zero Checkpoint criteria fire (Red Team's explicit ruling, §4 of its
audit) — no unfalsifiable claim, no dropped constraint (T1 route N/A
confirmed six ways at Phase 2 and again at Phase 5), and the R9 defect
and its own residual gaps were self-caught, disclosed, and queued for
Iteration 92 — not a program-integrity-drift finding against anyone.

## Idealizations — carried from `phase1_proposal.md` §6, as corrected at Phase 3

See `phase1_proposal.md` §6 for the full list (does/does-not establish,
Idealizations 1–5). Idealization 3 (no named-bin/angular-pattern
instrument invoked) is unchanged and now reflected directly in
`analyze114.py`'s own `repro_ok=None`/"N/A" handling, not merely
disclosed in prose. The R30/R32 "N/A, explicitly stated" position is
unchanged — this cycle produces no discriminating statistic of that
kind even after Fix 1's ratio-space rescoring (a CONFIRM/AMBIGUOUS/
REFUTE label against a fixed, disclosed, non-null-calibrated band is not
the kind of population-derived threshold/direction R30/R32 govern).
