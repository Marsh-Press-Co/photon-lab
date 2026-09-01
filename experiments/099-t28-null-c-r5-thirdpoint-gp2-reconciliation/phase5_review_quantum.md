# Panel Iteration 76 (exp-099) — Phase 5 Review (QUANTUM OPTICS)

*Fresh context. Read in full: PANEL.md, LOGBOOK.md (RULED OUT R1–R19,
LIVE THREADS T1–T28 including the complete T28 sub-thread history through
Iteration 75/exp-098), PLAN.md's current-state entry, and every exp-099
file (`phase1_proposal.md`, all five Phase-2 critiques, Red Team's Phase-2
audit, `NOTES.md`, `run.py`, `results.json`, `run_output.txt`). Blind to
every other seat's Phase-5 output, per PANEL.md independence mechanics.
Charter: non-classical absorption, state-dependent or coherent
interactions. Expressibility contract: mechanisms enter the bench only as
effective classical parameters (σ(I), σ(x,t), dispersive ε(ω), gain) or Red
Team strikes them.*

## 0. Scope note

This is the eighth consecutive T28 house-discipline/instrument-validation
cycle (exp-069 through exp-099, with the exceptions already logged). No new
mechanism is proposed — Checkpoint criterion 2 (T1 escape-route position) is
correctly N/A, and Idealization 7 discloses this honestly rather than
smuggling a claim past it. My charter's usual object of scrutiny (does a
proposed mechanism reduce honestly to an effective classical parameter) is
therefore not directly engaged by anything *executed* this cycle. Per this
sub-thread's own established practice for cycles in this shape (QUANTUM's
own critiques at exp-096–098), my duty this cycle is (a) independent
from-source re-verification, and (b) the forward-looking expressibility
question PANEL.md's own Phase-5 instructions pose explicitly: whether this
cycle's own *governance disposition* — not its FDTD physics — sets up a
future expressibility-contract violation. §3 below is that finding.

## 1. Independent spot-verification

I recomputed the following six load-bearing figures directly from
`results.json`/`run.py`/`run_output.txt`, and — for the fault-injection
scenarios — from the actual Check 1–7 function bodies in
`experiments/097-t28-r18-tier0-gate-closure/run.py` (not proposal prose,
not field names alone).

1. **Item 1's interval-slope-decay ratios (`r_ratios`).** Sequence from
   `NULL_C_FILED_KEYS[3]` (θ₀+0.500°, +4.704113885973804×10⁻⁴) through the
   three new points (+1.322250865020469×10⁻³, +2.4566233265059245×10⁻³,
   +2.7780786590187456×10⁻³): diffs = 8.518394764230886×10⁻⁴,
   1.1343724614854555×10⁻³, 3.214553325128211×10⁻⁴. `r₁=|diff₂|/|diff₁| =
   1.331674`, `r₂=|diff₃|/|diff₂| = 0.283377`. **Matches `results.json`'s
   `r_ratios: [1.3316739748300177, 0.28337723580831364]` exactly.** Since
   `r₁ > 0.5`, `amplitude_criteria_met` must be `False` — confirmed against
   the filed `"amplitude_criteria_met": false`, and against `run.py` lines
   364–368's own branch logic, which I traced line-by-line: the code
   correctly falls through to `INCONCLUSIVE-AT-THIS-WIDTH` (not the
   `VANISHING-AMPLITUDE`/`INCONCLUSIVE-CONSISTENT-WITH-SAME-LOBE-OSCILLATION`
   branches, both of which require `amplitude_criteria_met=True`). **Verdict
   logic reproduces correctly.**
2. **Item 2 Step 1's ground-truth sign match.** Filed `delta_scene(36.0°,
   R5) = −1.064305×10⁻³` (negative) against the established R4 reference
   `−8.776529×10⁻⁴` (also negative, `experiments/094-.../results.json`,
   `outcome="CONSISTENT"`) — `sign_match=True`, matching the code's
   `(ds_gt < 0) == GT_36_DEG_SIGN` boolean exactly.
3. **Item 2 Step 2's settling `rel_dev`.** `|5.243753061360268×10⁻⁴ −
   5.253136125293878×10⁻⁴| / 5.253136125293878×10⁻⁴ = 1.78618×10⁻³` =
   0.17862% — matches the filed `"rel_dev": 0.0017861832836256804` and
   the printed `0.1786%`, well inside the ≤1% PASS band.
4. **Item 2 Step 3's Richardson figure.** `shift_40_50 = crossing_cpl50 −
   theta_c40 = 39.77686992722644 − 39.921519316666235 = −0.144649389...°`
   — matches the filed `shift_30_40` field (the code's positional
   relabeling, per NOTES.md's own disclosure) exactly.
   `observed_ratio = −0.144649389 / −0.150319022 = 0.962283` — matches
   `"observed_ratio": 0.962282667915931` exactly. I also independently
   linear-interpolated the zero-crossing between the two flanking Step-3
   points (39.688519°, −5.951707×10⁻⁴) and (39.854519°, +5.230823×10⁻⁴):
   θ ≈ 39.68852 + 0.5322×0.16600 ≈ 39.7769°, matching the filed
   `crossing_cpl50=39.77686992722644` to 4 decimal places by hand.
5. **Item 3's extended `ptp` ratios.** At θc=79°: `0.21735385064978663 /
   0.00025576654006225 = 849.81×`, matching `"ratio_to_theta_c_5":
   849.8134689427543` exactly. At θc=87°: `0.07461436316975525 /
   0.00025576654006225 = 291.73×`, matching `291.7283986857513` exactly.
6. **Step 0's fault-injection classification logic — checked against the
   actual check-function source, not inferred.** I read
   `run_checks_1234_and_7` (`experiments/097-.../run.py:109–153`) and
   `check6_positional_and_cpl`/`check6_set_membership_OLD` directly. Each
   scenario's corruption and its predicted CLEAN/DEFECT-FOUND outcome
   reproduce exactly against the real logic:
   - **Positive control**: all actuals match intendeds → `check1`–`check4`,
     `check7` all `True` → CLEAN/CLEAN. **Matches.**
   - **FI-A** (`cpl_actual=dg.R4_CPL[600]=40≠50`): `check1 = (sim.lam ==
     cpl_intended)` — `sim.lam` reflects the actually-constructed `cpl=40`
     Sim, so `check1=False`; `check2`–`check4`/`check7` unaffected (angle,
     placement, phase, taper all still correct) → `clean_1234=False`,
     `clean_7=True` → DEFECT-FOUND/CLEAN. **Matches the filed
     `check1_resolution:false, clean_1234:false, clean_7:true`.**
   - **FI-B** (`theta_actual=41.85≠41.825`): `check2 = (actual angle_deg ==
     theta_intended)` fails directly; `check4` (`phase_ramp`) is computed
     as `expected_phase(theta_intended,...)` vs. the REAL constructed
     phase (which depends on `theta_actual`) — so a wrong angle corrupts
     the phase too, correctly cascading to `check4=False` as well. Filed:
     `check2_angle_spec:false, check4_phase_ramp:false, clean_1234:false,
     clean_7:true`. **Matches**, and the check2+check4 co-failure is
     physically correct (an angle-mislabel corrupts both the recorded
     angle metadata AND the actually-injected phase ramp).
   - **FI-C** (`theta_actual=−41.825`, sign flip): same mechanism as FI-B
     (both `check2` and `check4` fail, `check1`/`check3`/`check7`
     survive). **Matches filed values exactly.**
   - **FI-D** (`edge_actual=80≠100`, wrong taper): `check7 =
     allclose(actual_taper_profile, taper_expected(n, TAPER[family]))` —
     `TAPER[family]` is the CORRECT/intended edge value, independent of
     `edge_actual`, so only `check7` fails; `check1`–`check4` (resolution,
     angle, placement, phase) are untouched by a taper-edge corruption.
     Filed: `check7_taper:false` alone, `clean_1234:true, clean_7:false`.
     **Matches** — and this is the one scenario where CLEAN(1234)/
     DEFECT(7) is the *correct* prediction precisely because Checks 1–4
     and Check 7 are functionally independent probes (resolution/angle/
     placement/phase vs. taper shape), which I confirmed by reading both
     code paths, not merely trusting the docstring's claim of
     independence.
   - **FI-E/F/H (Check 6 idiom)**: `check6_positional_and_cpl` keys its
     `theta_ok`/`family_ok`/`cpl_ok` sub-checks against
     `NOTES_MD_FROZEN_LINE_VALUES`/`NOTES_MD_FROZEN_FAMILY_BY_LINE`/
     `NOTES_MD_FROZEN_CPL_BY_FAMILY` — genuinely external, hand-frozen
     ground truth, independent of whatever corrupted `pt` dict is passed
     in — while `check6_set_membership_OLD` only tests set membership of
     `theta` against the frozen list, which is exactly why an index swap
     (FI-E: both swapped angles are still members of the *same* two-
     element set) or a `cpl`/family mislabel (FI-F/H, which never touch
     `theta` at all) sail through the OLD check but are caught by the
     new one. Filed `caught_by_new=True, missed_by_old=True` at all three
     — **matches the mechanism exactly, traced to source, not merely to
     the summary booleans.**

   **All six load-bearing recomputations and the full fault-injection
   classification logic reproduce exactly. I found zero arithmetic,
   logic, or mislabeling defects anywhere in the executed code or its
   output — a materially cleaner spot-check than several recent T28
   cycles' own Phase-5 layers have found (cf. Iteration 66's affirmative
   false claim, Iteration 69's silent JSON truncation).**

## 2. Steel-man

This cycle earns its own "R5's first real spend" headline honestly. The
three-way convergent Phase-2 attack (MATERIALS: R15-addendum ground-truth
gap; QUANTUM: zero fault-injection coverage at `family="R5"`; ELECTROMAGNETISM:
unpriced hard-assert HALT risk) targeted three genuinely independent
mechanisms — physics trust, construction-time trust, and runtime
completion — and Red Team's audit verified each from source before ruling
mandatory, rather than taking any critique on its word. The Director's
Phase-3 synthesis adopted all seven mandatory fixes without dilution, and
the executed `run.py` visibly implements every one of them in the correct
order (Step 0 before Step 1 before Step 2/3, gated exactly as specified).
The cycle also self-corrected honestly in two places that could easily have
been smoothed over: (a) a mid-run `KeyError` crash (a second instance of
the "filed data reconstructed by fresh arithmetic instead of read back by
its stored key" failure class) is disclosed in full in the Result section,
with a diff proving no data was lost; (b) Item 1's own pre-registered
VANISHING-AMPLITUDE outcome, correctly barred in advance by Fix 5
(PHOTONICS' period-based discharge condition), turned out to be *exactly*
right to bar — the real data show a genuine trough-and-reversal (a "bounce"),
which a bare `r_i<0.5` criterion would have mis-scored as decay-to-zero.
Fix 5 is not a hypothetical improvement here; it is empirically vindicated
by this cycle's own result.

## 3. Sharpest finding — the Iteration-77 trigger risks scoring a domain
artifact as a material mechanism, an expressibility-contract violation
waiting to happen, not yet occurred

**This is my charter's own question, applied prospectively rather than
retrospectively: does anything this cycle sets in motion risk a future
mechanism that cannot be expressed as an effective classical parameter?**

NOTES.md's own §T1 disposition (item 5, THERMODYNAMICS' ruling, adopted
without Phase-2 attack beyond a non-blocking wording note) states the
Iteration-77 queue "should include...an actual constraint-1/2/3/4 scoring
pass that treats the now-more-fully-characterized `delta_scene(θ)` sign
structure as an angular-selectivity parameter and runs it through the
existing constraint-metric instruments" — and states explicitly that a
future cycle filing T1: N/A without addressing this trigger should be read
as *overriding* this seat's own disposition. This is a concrete, binding
governance instruction for next cycle, not idle language.

**`delta_scene(θ)` is not a candidate angular-selectivity mechanism as
currently characterized — it is an instrument-sensitivity diagnostic, and
this program's own record has never resolved whether it carries any
realizability content at all.** Tracing its own definition through this
sub-thread's history (independently re-confirmed this session against
`experiments/069-.../design_geometry.py` and the T28 LOGBOOK record):
`delta_scene` for the `PAIR_PAD`/Null-B/Null-C family is the Weber-contrast
difference between two scenes that are **identical in every physical
respect that matters to a witness** — same absorbing article
(`graded_black_shell`), same wavelength, same angle — differing *only* in
`PAD`, a pure simulation-domain-padding parameter, independently **proven
lossless vacuum** by exp-076 (`experiments/076-.../`, LOGBOOK Iteration 53:
the FDTD engine's own graded-loss damping array is a function of `absorb`
alone, with zero dependence on `nx`/`ny`/`pad`). A real witness coating has
no "PAD" parameter to tune; `PAD` cells do not correspond to anything a
material could embody. MATERIALS' own standing framing rule — adopted at
Iteration 59 ("this whole confound is a pure scene/domain-geometry fact, no
material implicated"), then explicitly and correctly **not** reinstated at
Iteration 60 ("genuine ambiguity remains between two opposite-realizability
readings") — has never been resolved in either direction across the nine
subsequent cycles (exp-084 through exp-099) I read in full. This is a
load-bearing, still-open ambiguity, not a settled question this proposal's
own item 5 is entitled to build on silently.

**Concretely, the risk**: if Iteration 77 takes item 5's trigger literally
and feeds `delta_scene(θ)`'s sign-structure directly into `emit.observer_
record`/`lab/ambient.py`/the beam-behind box as an "angular-selectivity
parameter," it would be scoring a domain-padding sensitivity curve as if it
were a coating's own angle-dependent absorption cross-section σ(θ) — a
mechanism that, on the record as it stands, **cannot be expressed as an
effective classical material parameter**, because no material parameter
drives it. That is precisely the class of claim Red Team's charter (and,
by extension, mine) exists to strike *before* it consumes real FDTD budget
scoring against PANEL.md's own constraint metrics, not after. This is not
a claim that `delta_scene` is *definitely* pure artifact — exp-087
(Iteration 64) found bulk-absorbed-power and localized Weber contrast are
"at minimum, comparable-order-of-magnitude coupled," so some genuine
material coupling may exist alongside the domain-geometry component; the
point is that this program has never separated the two, and item 5's own
trigger text does not ask Iteration 77 to separate them before scoring.

**What item 5 actually delivers instead (MATERIALS' non-blocking Attack 8,
correctly discharged) is a different, narrower claim**: `cpl` (grid
resolution) is orthogonal to realizability — true, verified, and useful,
but not the same question as whether `delta_scene`'s own *physical origin*
(PAD/aperture geometry vs. article response) is expressible at all. The
proposal conflates "we have shown resolution-indexing carries no
realizability content" with "the underlying signal is fit to be scored as
a mechanism" — these are different claims, and only the first was checked
this cycle.

**Recommended discharge, cheap and already-available**: before any
constraint-metric scoring pass runs on `delta_scene(θ)`, decompose it (or
a matched companion measurement) into a PAD-held-fixed/article-toggled leg
and a PAD-toggled/article-held-fixed leg, at the same angles — reusing
exactly the energy-interception machinery (`ratio_abs_ext`, `p_abs_w`)
this sub-thread's own `cell_metrics_r4`/`cell_metrics_r5` already compute
and this cycle's own `results.json` already carries at every new point
(e.g. `ratio_abs_ext_raw_c/g` sit at ≈0.512–0.514 uniformly across all 17
new cells this cycle produced, T9-flat as always) — to establish whether
any part of the oscillation tracks the article's own absorbed power
(expressible, real physics) as opposed to living entirely in the coherent
phase/timing channel `PAD`'s own lossless-vacuum proof already confines it
to. Zero new FDTD needed beyond what Iteration 77 would run anyway; this
is a re-labeling and re-partitioning of data already on file plus this
cycle's own new cells, not a new build.

## 4. Secondary findings

**4a. The Richardson ratio trend is moving the wrong way for a converging
sequence, and neither NOTES.md's Result nor Learned section names the
direction.** Two same-direction Richardson figures now exist on Null B:
20/30/40 gave `observed_ratio=0.7765` (exp-098); 30/40/50 gives
`observed_ratio=0.9623` (this cycle, independently re-derived in §1 above).
Both exceed the naive 2nd-order expectation (0.5625, 0.64 respectively) —
already flagged as "super-linear" by NOTES.md's own Learned #4 — but the
more consequential fact is that the ratio itself is *increasing toward 1*
as resolution refines (0.7765 → 0.9623), not decreasing toward any fixed
sub-1 constant. A geometrically converging sequence of marginal shifts
should show a roughly *stable* (or, under improving relative
discretization error, shrinking) ratio; a ratio climbing toward 1 means
the marginal shift is barely damping at all between cpl=40 and cpl=50 —
consistent with either (a) a genuinely slow (sub-linear) order of
convergence, or (b) exactly the R15-addendum concern this sub-thread's own
founding rule exists to name: "a persistent recipe-level artifact" shared
by the R3/R4/R5 construction (Idealization 17, carried forward unchanged
this cycle) that does not shrink under refinement because it isn't a
discretization error at all. NOTES.md's own Idealization 49 correctly
disclaims a formal convergence-order claim, but frames both figures as
merely "descriptive" without naming the *direction* of the trend across
the two data points now on file — a direction that, on its face, argues
against confident "genuine migration" readings, not for them. This should
be stated explicitly, not left implicit in two numbers a reader must
subtract.

**4b. The newly-discovered "bounce" (Learned #2) is asserted with more
confidence than a single, unresolution-checked cpl=40 measurement
supports.** Item 1's real new result — `delta_scene` reverses direction
between θ₀+0.5° and θ₀+0.83° without crossing zero — is stated as "a
genuine bounce, not a stall," and NOTES.md's own §Next item 1 proposes
centering a future, wider search on this location. This is new information
(correctly credited as such), but it is a single-cpl (cpl=40 only) reading
of a feature this sub-thread's own R15/T10 lineage has repeatedly shown can
relocate or invert entirely under resolution refinement (exp-090→exp-091's
own double-crossing collapsing to a single null; exp-093→exp-094's own
complete six-point sign reversal at cpl=40). The trough sits comfortably
clear of the R13 floor (minimum reading ≈4.7×10⁻⁴ vs. floor ≈1.92×10⁻⁴, a
healthy ≈2.45× margin — not a razor-thin R13/R14 hazard), so I am not
raising an R13-class floor concern; the concern is R15-class
resolution-sensitivity, which this cycle's own new feature has never been
checked against at any second `cpl`. Before §Next item 1's proposed wider
search is centered on this location, a cheap 1–2 point cpl=30 or cpl=50
spot-check at the trough's own approximate minimum (θ≈θ₀+0.65°) — mirroring
exactly the discipline this cycle's own item 2 just applied to Null B via
R15's far-from-null ground-truth check — would be a low-cost, high-value
precondition, not a delay.

**4c. Minor, non-blocking.** `run.py`'s own R19-style total-call assert
(`assert total_calls in (40, 24, 16, 20, 32)`) admits three values (16, 20,
32) that I traced are unreachable given the actual control flow: the
`xi_ext`/`sigma_abs_nonneg` gates are hard Python `assert`s that halt the
process before any `results.json` is written, so the only two live,
non-crashing totals are 40 (full PASS-path) and 24 (Step-1 GT-mismatch or
Step-2 HALT, both skip Step 3 identically). This is harmless dead-code
permissiveness — the actual run produced 40, correctly validated by the
second, tighter assert immediately below it — not a defect, but worth
tightening if this assert idiom is reused a further time.

## 5. Verdict

**CONCUR-WITH-GAP(S).**

Every load-bearing number I independently recomputed — including tracing
the fault-injection classification logic to the actual Check 1–7 source,
not merely its docstrings — reproduces exactly. The cycle correctly
executes exp-098's own queued items, honestly discloses a non-forced
INCONCLUSIVE-AT-THIS-WIDTH result for Item 1 and a genuine, cleanly-gated
SIGN-CHANGE-FOUND for Item 2, and Item 3's mixed non-resolution is treated
as the informative outcome it is rather than forced toward either
falsification branch. Nothing here rises to DISPUTE: no defect I found
touches an already-computed number, and my sharpest finding (§3) concerns
a *prospective* governance instruction for Iteration 77, not anything
executed or claimed as settled this cycle. The gap is real and, left
unaddressed, could let a domain-geometry artifact be scored as a physical
escape-route mechanism next cycle — worth a named precondition before
Iteration 77 spends real budget on it, per §3's discharge recommendation.

**On independently rebuilding this cycle's construction from primitives**
(this program's own precedent, invoked in my task brief): I judge it was
**not warranted this cycle**, and say so rather than perform a rebuild for
its own sake. Red Team's Phase-2 audit already re-verified essentially
every load-bearing claim from source — including finding one defect
(Attack 4, the mislabeled interior angle keys) that all five blind
critiques missed — a materially deeper adversarial pass than this
program's typical Phase-2 layer. My own from-primitives check (§1),
including reading the actual Check 1–7 functions rather than trusting
field names, found zero discrepancies anywhere. This differs from past
cycles where a QUANTUM rebuild was the *only* thing that caught a
load-bearing defect (exp-072's carrier-phase sign bug; exp-087's
zero-crossing denominator hazard) — here, the risk surface was already
covered more thoroughly than a solo rebuild would add, and my highest-value
contribution this cycle is the forward-looking category-error catch in §3,
not a redundant re-derivation of arithmetic already independently
confirmed three times over (Red Team, and now me, a fourth).

## 6. Ranked top-3 candidate next directions for Iteration 77

**#1 — Partition `delta_scene`'s own physical origin (article-response vs.
domain-artifact) before any constraint-metric scoring pass runs on it (§3
above).** This is a precondition, not a full alternative to NOTES.md's own
§Next item 2 trigger — it should gate that trigger, not replace it. Cheap:
reuses `ratio_abs_ext`/`p_abs_w`, already computed at every point this
sub-thread has ever run, including this cycle's own 17 new cells. I rank
this #1 because, unaddressed, it risks the single most consequential
category of error this program's charter (mine and Red Team's) exists to
prevent — an unfalsifiable/inexpressible mechanism entering a constraint
scoring pass — and because the ambiguity it resolves has sat open,
unaddressed, since Iteration 59/60, now nineteen-plus cycles ago.

**#2 — A cheap cross-resolution (`cpl=30` or `cpl=50`) spot-check of the
newly-found Null-C "bounce" trough (§4b) before centering a wider search on
it, folded into whatever bracket-widening test NOTES.md's own §Next item 1
proposes.** I agree with NOTES.md's own item 1 in substance (a bracket
reaching the full ≥2.9474° established period is the right next test for
Null C's own sign question) but would add this R15-class precondition
before trusting the trough's *location* as the search's own center — 1–2
extra calls, matching this cycle's own discipline exactly (Item 2's Step 1
did precisely this for Null B before trusting its interior sweep).

**#3 — Reframe the Richardson-pattern follow-up (NOTES.md's own §Next item
3) from lateral generalization (does it recur at Null A?) toward vertical
convergence-behavior characterization: does a further resolution point
continue the ratio's climb toward/above 1 (evidence against genuine
convergence, strengthening the R15-addendum "persistent recipe artifact"
reading) or does it fall back (evidence of a real, if slow, asymptote)?**
I partly disagree with NOTES.md's own draft ranking here: Null-A
generalization is informative but answers a different question (is this
pattern feature-specific) than the sharper, more decision-relevant one the
two Null-B data points already on file raise (is this sequence converging
at all). Both are legitimate; if only one is affordable next cycle, the
convergence-behavior question is the one I would fund first, since a
"genuinely non-convergent" finding would be directly load-bearing to every
future citation of any R3/R4/R5-family crossing location this sub-thread
has ever produced, while a Null-A replication would only be informative
about this one specific super-linear shape.

I do not re-propose any RULED-OUT idea (R1–R19) anywhere above.
