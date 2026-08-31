# Phase 2 — Red Team Audit (exp-095, Panel Iteration 72)

*Seat charter (PANEL.md, verbatim): attacks every proposal, speaks last and
hardest; standard is not textbook-physics compliance — speculation is
permitted; kills internal inconsistency, unfalsifiable claims, mechanisms
that cannot be expressed as simulation parameters, and proposals that
quietly violate a target constraint, especially #3. Never leads a cycle,
has no proposal of its own to protect.*

Read, in the order specified: PANEL.md; LOGBOOK.md in full (RULED OUT
R1–R16; ESTABLISHED; LIVE THREADS T1–T27 and T28's complete history,
Iterations 46–71); `experiments/095-.../phase1_proposal.md`; all five blind
Phase-2 critiques (photonics, materials, em, thermodynamics, quantum);
`experiments/092/093/094` (`NOTES.md`, `run.py`, `results.json`,
`phase5_redteam_audit.md` where present); `experiments/069-.../
design_geometry.py`. Every load-bearing number below was independently
re-derived from committed source this session — not taken on any critique's
or LOGBOOK's own word.

## 0. Scope note

This is instrument-validation work (exp-095's own §4: T1 route N/A,
Checkpoint criterion 2 N/A). **`constraint-#N-violation` essentially does
not apply to this cycle** — there is no phenomenon-mechanism claim to
quietly violate constraint 1/2/3/4 with, and I found nothing that smuggles
one in. **`inexpressible` also does not apply** — every quantity here
(angles, `cpl`, `sigma_max`, `STEPS`) is already a concrete FDTD parameter;
nothing in this proposal gestures at an untestable exotic mechanism. Both
tags are named here, not silently dropped, per the task's own instruction
to say so when a category genuinely doesn't fit rather than force it. The
attacks below are therefore tagged `[inconsistency]` almost throughout,
with one `[unfalsifiable]`-adjacent case discussed explicitly at #5.

## 1. Independent verification of the five blind critiques

All five are confirmed correct on independent re-derivation. Detail:

**PHOTONICS (39.8° is not far-from-null).** Recomputed directly from
`experiments/092-.../results.json::rank1.crossing_report.
lower_crossing_cpl30 = 40.07183833857387`: `|39.8 − 40.0718| = 0.2718°`,
`|39.2 − 40.0718| = 0.8718°` — both bit-exact to PHOTONICS' cited figures.
**Confirmed.**

**MATERIALS (`cpl=50` is the least alias-breaking third point, not
neutral).** Read `experiments/065-.../design_geometry.py::R_OUT = 78`
directly. Gate-3 bit-exactness requires `round(78·RATIO) == 78·RATIO`
(no rounding). Since `RATIO = cpl/20` (this sub-thread's own `CPL[600]`
convention, `R3_CPL=30→RATIO=1.5`, `R4_CPL=40→RATIO=2.0`, `R5_CPL=50→
RATIO=2.5`), `78·RATIO = 78·cpl/20 = 39·cpl/10`; since `gcd(39,10)=1`, this
is an integer **iff `cpl` is a multiple of 10** — equivalently, iff `RATIO`
is a multiple of 0.5, exactly MATERIALS' "half-integer ratio steps" claim.
Verified `cpl=45` (`RATIO=2.25`) breaks this (`78·2.25=175.5`, matching the
proposal's own disclosed ~0.28% radius drift) and `cpl=50`/`60`/`70`
(`RATIO=2.5/3.0/3.5`) do not. `cpl=50` is indeed the *nearest* remaining
exact point, continuing the identical `1.5→2.0→2.5` arithmetic progression
the shared `r{n}_config()` recipe produces — i.e., of every Gate-3-exact
"third point" reachable from this one recipe, it is the least distinct from
`R3`/`R4`. **Confirmed**, and the underlying arithmetic is tighter than
"half-integer ratio" alone states (the true condition is `cpl` a multiple
of 10; I state it exactly here for the record).

**ELECTROMAGNETISM (Rank 2 has no native-sigma R5 comparator; exp-093's
own Item 3 already proved this exact contamination mode).** Read
`experiments/093-.../results.json::item3.per_theta`. At 42.0°:
`native_delta_scene = +8.0418×10⁻⁵`, `sigma_corrected_delta_scene =
−5.8102×10⁻⁵`, `delta_scene_ratio = −0.7225` — a genuine sign flip from the
sigma correction ALONE, one angle over from Rank 2b's own 41.75°–41.90°
sweep. Re-read `phase1_proposal.md` §3's angle table: Rank 2b lists only
`sigma_max=0.2 (corrected)` at all six interior angles, no native-sigma leg
anywhere in Rank 2. **Confirmed**, and the exp-093 precedent this attack
rests on is itself independently re-verified here, not merely cited.

**THERMODYNAMICS (no `cell_metrics_r5` named).** Full-text search of
`phase1_proposal.md`: `cell_metrics_r4` appears once (§3, Rank 1/3(b),
correctly — those ranks reuse the `R4` family verbatim); no occurrence of
`cell_metrics_r5` anywhere in the document, including §3's own `R5`
parameter table, which specifies `r5_config()` (geometry only) but never
names the metrics-computation analog. **Confirmed** — this is exactly
R16's own founding failure shape (a disclaimer/compliance line naming
functions that already exist, silent about the one that has to be
freshly written for the new family) recurring inside the very cycle
written in direct response to R16's adoption.

**QUANTUM OPTICS (sign check at antinodes has near-zero power against a
phase/registration defect).** This is a structural argument about
statistical power, not a numeric citation — verified by construction: `Re`
of two coherent contributions differenced is `A·cos(φ)`; near a node
(`φ→π/2`), sign is controlled by small perturbations to `φ`; far from a
node, sign is controlled by the amplitude term, comparatively insensitive
to phase perturbations of the size a coordinate/registration bug would
plausibly introduce. Cross-checked directly against exp-094's own
`results.json::rank1b` (all six flips at 41.75°–41.90°, R14's established
near-null band) and `rank3` (the 38.4° flip, itself R13/R14-flagged as
near-null-adjacent by exp-094's own Learned #... text) — every substantive
`R4`-family finding this sub-thread has produced to date lives in exactly
the band this gate does not test. **Confirmed.**

## 2. Numbered attacks

**#1 [inconsistency] — Rank 1's own "no ambiguity about the correct
answer" premise is falser than PHOTONICS' own fix credits, and PHOTONICS'
own proposed replacement (39.0° or 39.4°) is not uniformly safe.**
PHOTONICS checked each control angle's distance against exactly one known
null (exp-092's `cpl=30` lower crossing, 40.0718°). But this sub-thread's
own R13-founding record (`experiments/090-.../results.json::q8.
crossings_deg`) independently establishes FOUR `cpl=20` `delta_scene`
zero-crossings: `37.127°, 38.590°, 40.265°, 41.461°`. Checked against the
full six-crossing set (those four plus the two `cpl=30` crossings PHOTONICS
already used), the picture changes:

| θ | nearest known null | distance |
|---|---|---|
| 39.0° | 38.590° | **0.410°** |
| 39.2° | 38.590° | **0.610°** (not 0.872° — PHOTONICS' own cited comparator, `40.0718°`, is only the SECOND-nearest) |
| 39.4° | 40.0718° | **0.672°** |
| 39.8° | 40.0718° | 0.272° (PHOTONICS' own figure, confirmed) |

Two consequences neither PHOTONICS nor any other critique drew out: (a)
39.2° — the proposal's own "strong," unquestioned control point — is
itself only 21% of a period from a genuine, independently-established
null, materially closer than PHOTONICS' own critique credited it, which
*tightens* PHOTONICS' attack rather than softening it; (b) PHOTONICS' own
named fix — "replace 39.8° with 39.0° or 39.4°, same call count, zero added
cost" — is not fungible between the two options. 39.4° is the best of the
four candidates checked (0.672° from any known null). **39.0° is nearly as
compromised as the original 39.8°** (0.410° vs. 0.272°, both well under a
quarter-period) — a superficially plausible-looking substitution that would
not actually discharge PHOTONICS' own concern if the Director picks it
without re-running this same check. This also sharpens the practical risk
of hitting the proposal's own §2 AMBIGUOUS branch (`floor_pass=False` at
`cpl=40`) at 39.2° specifically, stalling the whole cascade before Rank
2/3 ever run.

**#2 [inconsistency] — the proposal's own confound-disentangling logic
(Rank 3b) does not extend to the item it exists to validate (Rank 2b),
though the identical fix EM names for Rank 2 would just as cheaply cover
it.** Rank 3b is explicitly built to answer "is the `cpl=40` reversal a
sigma-choice artifact or a genuine grid-refinement property" — exactly the
question EM's attack (#3 above) shows is equally open for Rank 2b's own
`cpl=50` reversal-or-no-reversal reading. As filed, a CONFIRM/REFUTE
verdict on Rank 3b tells you nothing about whether Rank 2b's own outcome
(TWO-NODE CONFIRMED / SINGLE-NULL / STILL AMBIGUOUS) is itself
sigma-driven. The proposal treats these as two separately-scoped items
(Rank 3b closes the `cpl=40` sigma question; Rank 2b is scored purely on
`cpl=50` vs `cpl=30`/`cpl=40` sign agreement) when they are the same
open question asked at two resolutions — Rank 2b inherits Rank 3's own
unresolved risk, unaddressed by Rank 3b's result no matter which way it
comes out.

**#3 [inconsistency] — §1's "minimum-discharge package" framing overclaims
what Rank 2 can structurally deliver, independent of how it runs
(MATERIALS' finding, restated at its strongest).** R15's own Iteration-71
addendum text (LOGBOOK, quoted in the founding record) requires, before a
third resolution point is trusted: "the new family must ... be shown to
reproduce the ALREADY-KNOWN-CORRECT sign at a robust, far-from-null angle"
(Rank 1's job) **and** enough independence from the prior families that a
"persistent recipe-level artifact" can be ruled out. Rank 2 supplies the
first half. It cannot supply the second, by MATERIALS' own proof (§1,
above): `R5` is not an independent discretization, it is the identical
`r{n}_config()` formula at a third ratio drawn from the same admissible
set `{1.5, 2.0, 2.5, ...}` `R3`/`R4` already came from. A recipe-level
systematic — by definition — reproduces at every ratio the recipe can
produce, so no outcome of Rank 2b (TWO-NODE, SINGLE-NULL, or AMBIGUOUS)
can, on its own, distinguish "genuine convergence" from "the same
artifact showing up a third time." Idealization 17 says this in one
sentence; §1 and §5's outcome taxonomy do not carry the caveat at the same
weight, and 71% of this cycle's own record 744-CPU-min budget is spent on
the item this applies to.

**#4 [inconsistency] — R16 compliance is asserted, not yet specified, for
the one Rank most likely to reproduce R16's own founding failure.**
Confirmed at §1: `cell_metrics_r4` is named and reused verbatim (low risk,
correctly disclosed); no `cell_metrics_r5` is named anywhere, though Rank 2
is a freshly-written code path in exactly the shape (`box_for_rN`/
`ref_for_rN`/`_run_sim_rN_sigma` hand-copied per family) that produced
R16's founding gap in exp-094. The proposal's R16-compliance header states
a *result* ("`netd_row()` merged... from the first draft") about a function
that does not yet have a name in this document.

**#5 [inconsistency, bordering unfalsifiable-in-practice] — the go/no-go
gate is powered against the wrong defect class, and this is not merely a
missing nice-to-have.** Restating QUANTUM's finding at full strength: Rank
1's entire reason for existing is R15's addendum's own demand — rule out
"a systematic registration/phase-reference defect in the new family's own
construction" before trusting Rank 1b's complete 41.75°–41.90° reversal.
A registration/phase defect is, almost by definition, a *small angular or
coordinate offset* — its signature is a shifted zero-crossing, not a
uniformly wrong-signed field far from any crossing. Testing only amplitude-
dominated points means a PASS is close to unfalsifiable *for the specific
hypothesis it exists to rule out* — a registration bug of exactly the size
that would explain the interior reversal could pass this gate with
certainty regardless of its presence. This does not make the gate useless
(it still catches a gross wiring/sign error, matching R4/R6's own
recompute-don't-hand-type lineage), but it does mean a PASS should not be
read, without QUANTUM's own proposed node-bracketing addition, as having
addressed R15's addendum's own registration-defect language at all.

**#6 [inconsistency, minor, disclosure-only] — the budget is 5–7× this
sub-thread's own established per-cycle band, and the proposal names this
without reconciling it.** `experiments/092-.../NOTES.md`'s own Phase-3
synthesis states its 134.6 CPU-min "sits at the top of, but inside, this
sub-thread's established ~100–150 CPU-min band." exp-095's own §7 estimates
≈744 CPU-min on the PASS path — roughly 5–7× that band, self-described as
"the largest single T28 cycle to date." This is disclosed, not hidden, and
I do not find it disqualifying on its own (the wall-time cost is modest,
≈3.1h at 4 workers, and the historical record shows every T28 wall-time
estimate has landed under budget) — but combined with #3 above, it means
the single largest CPU spend in this sub-thread's history is going to the
one item proven structurally unable to deliver, alone, the finding it is
funded to deliver. This is an efficiency argument for rescoping Rank 2, not
a correctness defect in its own right — folded into the mandatory-fix
docket below rather than counted as a seventh independent inconsistency.

## 3. Adjudication of the five blind critiques

All five: **ACCEPTED, no overrides.** Each independently reproduces
bit-exact against primary source (§1), none conflicts with another, and
none is answered by any existing idealization at adequate strength.

| # | Seat | Finding | Disposition | Fix |
|---|---|---|---|---|
| 1 | PHOTONICS | 39.8° is 0.272° from a known null, not a clean far-from-null control | **ACCEPTED**, sharpened by attack #1 above | Replace 39.8° with 39.4° specifically (not "39.0° or 39.4°" — 39.0° fails the same test); state both control angles' distance-to-nearest-of-the-FULL-six-crossing-set in §2's own table |
| 2 | MATERIALS | `cpl=50` is the least alias-breaking third point available, not neutral, given `R_OUT=78`'s even/half-integer-step structure | **ACCEPTED** | Reword §1/§5 so no Rank-2b outcome is described as discharging R15's addendum by itself; add MATERIALS' own remedy (b) — a companion desk bound on whether the `cpl=45`-scale (~0.28%) radius drift could plausibly explain an observed sign difference, quantifying rather than merely disclosing the shared-recipe risk |
| 3 | ELECTROMAGNETISM | Rank 2 has no native-sigma R5 comparator, unlike Rank 3; exp-093 Item 3 already proved sigma alone can sign-flip `delta_scene` at a neighboring fragile angle | **ACCEPTED** | Add a native-sigma `R5` leg at 2 of Rank 2b's six interior angles (the two nearest 41.8°/42.0°'s own already-demonstrated sigma-sensitivity — 41.825°/41.850° are the natural picks); until this leg exists, report Rank 2b's own classification as provisional-pending-sigma-check, matching EM's own fallback |
| 4 | THERMODYNAMICS | No `cell_metrics_r5` named anywhere; Rank 2 is fresh code in the exact shape that produced R16's founding gap | **ACCEPTED** | Name `cell_metrics_r5(key, th, steps, cap_empty, cap_article)` explicitly in §3 as a line-for-line mirror of `cell_metrics_r4`, with its `netd_row()` merge written in the same diff — matching THERMODYNAMICS' own suggested text verbatim |
| 5 | QUANTUM OPTICS | The sign-only, off-node gate has near-zero power against the registration/phase-defect class it exists to catch | **ACCEPTED** | Add QUANTUM's own proposed node-bracketing recovery check (verify `delta_scene(R4)` brackets zero near the established θ₀≈38.590° crossing within ±0.1°) as a THIRD, complementary Rank-1 test — additive to, not a replacement for, the sign check (the two are powered against different defect shapes: gross sign/wiring errors vs. subtle phase/registration errors) |

## 4. Verdict

**PROCEED-WITH-MANDATORY-FIXES.**

Not HALT-AND-REDESIGN. Reasoning, stated in full rather than defaulted:

The convergent severity here is real — four of five blind critiques attack
either Rank 1's control-point validity or Rank 2's ability to discharge
R15's addendum at all, and my own independent check (#1) shows the
control-point problem is *worse*, not better, than the mildest of those
five critiques stated. That is enough to take seriously the question this
task poses explicitly: does this need more than a fix docket?

I judge it does not, for three reasons specific to what "redesign" would
actually mean here. First, every defect found is a *scoping and evidentiary-
weight* problem, not a broken instrument: `r5_config()`/`R5_CONFIGS`, the
Gate-3/4/5 mandatory checks, the sequencing/go-no-go architecture, and
Ranks 3a/4 are all independently re-verified sound (§1, §3 of the MATERIALS
steel-man; my own arithmetic re-derivation above). Nothing here needs new
engine physics, a new instrument class, or abandoning the sequencing
Red Team itself specified last cycle — it needs different angles, one more
comparator leg, one more named function, and honest outcome labels. Second,
this program's own record for this exact sub-thread (exp-090 through
exp-094, all read in full above) treats findings of comparable or greater
severity — a caution zone that inverts under relabeling (exp-091), a
complete full-window sign reversal on R15's own founding channel
(exp-094) — as PROCEED-WITH-MANDATORY-FIXES material, reserving HALT-class
language for Phase-4 null-miscalibration findings (`HALT_NULL_MISCALIBRATED`,
exp-073), not Phase-2 critique convergence. Nothing here rises to that
bar: no run has occurred, no false verification claim has been made and
defended, and every gap was caught blind, before Phase 3, by design —
this program's own established non-firing shape for Checkpoint criterion 4,
which I rule does **not** fire this cycle (worked through below).
Third, and most important: the two most serious findings (#3, MATERIALS —
Rank 2 cannot discharge R15's addendum alone; #5, QUANTUM — Rank 1 is
underpowered against the registration-defect class) are not in tension
with running this cycle, they are reasons to run it *with a different
evidentiary label attached to what comes back*. A cheap node-bracketing
addition to Rank 1 and an honest "necessary-but-insufficient" framing for
Rank 2b cost nothing in FDTD calls and directly close both gaps. Redesigning
Rank 2 into a genuinely independent second discretization (MATERIALS' own
option (a) — not chosen here) would be the right call if this cycle's
entire point were to CLOSE R15 outright; it is not — the proposal's own §2
already states this cycle does not by itself close R15 — so the honest
fix is to make the proposal's own claimed scope match what MATERIALS
proved it can structurally deliver, not to rebuild the instrument.

**Checkpoint criteria, worked through explicitly (none fire):** Criterion
1 (candidate reproduction) N/A, no run yet. Criterion 2 (proven mechanism
boundary) N/A, T1 route explicitly not engaged. Criterion 3 (engine
physics beyond validated bench classes) N/A — every construction here is
the already-validated `r{n}_config()` recipe at a new ratio. Criterion 4
(program-integrity drift: unfalsifiable claims, a constraint quietly
dropped) — the closest candidate, given #3/#5 above, but does **not**
fire: every gap was caught at Phase 2, before Phase 3 froze anything,
matching this sub-thread's own repeated non-firing precedent (Iterations
53, 55, 56, 67, 69, 70 all ruled non-firing on an identical "caught blind,
same phase, before adoption" basis); nothing was defended against a named,
affordable check the way R8's firing precedent (exp-075) requires. Criterion
5 (two consecutive non-advancing iterations) N/A — exp-094 delivered a
genuine, independently-verified full-window reversal; this cycle has not
yet run.

## 5. Mandatory-fix docket (nine items, zero overridden)

1. Replace the Rank-1 control-angle pair. Drop 39.8° (0.272° from a known
   null) and 39.0° if considered (0.410° from a known null, comparably
   compromised). Use **39.2° and 39.4°** — recompute and state, in §2's own
   table, each candidate's distance to the nearest of the FULL six known
   `delta_scene` crossings (`37.127°, 38.590°, 40.265°, 41.461°` at
   `cpl=20`; `40.0718°, 41.7811°, 41.8377°` at `cpl=30`), not merely the
   nearest `cpl=30` crossing.
2. Add QUANTUM's node-bracketing recovery check as a third, additive Rank-1
   test: verify `delta_scene(R4)` brackets zero near θ₀≈38.590° within
   ±0.1° — complementary to, not a replacement for, the sign check (item
   1), since the two are powered against different defect shapes.
3. Add a native-sigma `R5` leg at two of Rank 2b's six interior angles
   (41.825°/41.850°, nearest the already-demonstrated 41.8°/42.0°
   sigma-sensitivity), mirroring Rank 3a's own native-vs-corrected design
   for `R4`. Until this leg exists and clears, report any Rank 2b
   classification as provisional-pending-sigma-check.
4. Reword §1 and §5's Rank-2b framing: no Rank-2b outcome (TWO-NODE
   CONFIRMED / SINGLE-NULL / STILL AMBIGUOUS) discharges R15's addendum
   on its own — a recipe-level systematic reproduces at every ratio drawn
   from the same `r{n}_config()` formula by construction. State this
   before the run, not as a Phase-5 correction.
5. Add MATERIALS' own companion desk bound: quantify whether the
   `cpl=45`-scale (~0.28%) radius drift could plausibly account for any
   observed Rank-2b sign difference, bounding (not merely disclosing) the
   shared-recipe risk item 4 names.
6. Extend Rank 3b's confound-disentangling logic explicitly to cover Rank
   2b (attack #2): state, before the run, how a Rank-3b CONFIRM/REFUTE at
   `cpl=40` is or is not read as informative about Rank 2b's own
   `cpl=50` sigma-sensitivity — they are the same open question at two
   resolutions, not two independently-scoped items.
7. Name `cell_metrics_r5(key, th, steps, cap_empty, cap_article)` explicitly
   in §3 as a line-for-line mirror of `cell_metrics_r4`, with its
   `netd_row()` merge written in the same diff that adds the function —
   matching THERMODYNAMICS' own text.
8. Add a `p_abs_w`-specific settling band for Rank 2a (currently only the
   generic cross-Rank 1–5% band applies; Rank 2a's own settling precondition
   names only `delta_scene`).
9. State explicitly, in §7, that the ≈744 CPU-min PASS-path budget is
   5–7× this sub-thread's own established ~100–150 CPU-min per-cycle band
   (exp-092's own Phase-3 language) — disclosed, reconciled against items
   4–6 above (Rank 2's rescoped evidentiary weight), not silently
   inherited as "the largest cycle to date" without comment on why that is
   an acceptable trade this cycle specifically.

No item requires new FDTD spend beyond what items 2, 3, and 8 add (≈2 + 8
calls) — the fix docket is materially cheaper than the cycle it corrects,
matching this program's own unbroken same-shift-fix precedent.
