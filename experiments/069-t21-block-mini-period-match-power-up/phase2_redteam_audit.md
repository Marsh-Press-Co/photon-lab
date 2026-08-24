# PHASE 2 — RED TEAM FINAL AUDIT · Panel Iteration 46 · exp-069 (Block MINI power-up)

*Fresh sub-agent, RED TEAM charter (PANEL.md seat 7). Receives the Phase-1
proposal AND all five blind Phase-2 critiques, per PANEL.md's independence
mechanics. Goes last. Standard: not textbook-physics compliance —
internal consistency, falsifiability, expressibility as simulation
parameters, and non-violation of a target constraint (N/A this cycle, T1
route = instrument/model-fidelity, no constraint-3 claim advanced).*

## 0. Framing — what is actually at stake this cycle

This is not a mechanism proposal. It is PLAN.md's Iteration-46 LOCKED,
unconditional mandate, itself born of a documented process failure:
LOGBOOK's own Iteration-45 CHECKPOINT found that a PRIOR Red Team Phase-2
audit was handed a zero-cost path to close Block MINI's period-match test
and silently kept only the citation-tripwire half, dropping the
substantive half with no argued reason anywhere in the record. This audit
treats that finding as a standing instruction to itself: every one of the
five blind critiques' load-bearing points is dispositioned explicitly
below — adopted, extended, or overridden, with a reason, in writing. None
is silently dropped.

The mandate's own text is the bar this design must clear: *"Either build
the properly-powered FDTD version (≥2–3 T21 periods at ~0.2° spacing,
settled STEPS≥2800, desk-first...) or formally retire the test with a
stated reason — no further relabeling, no further citation-tripwire-only
treatment."* The proposal delivers the FDTD-power half faithfully (31
points, 0.2° step, 3.03 periods, STEPS=2800, desk check run first and
committed). It does **not**, as written, deliver an enforceable version of
the "or formally retire" half — see Attack 4.

## 1. Numbered attacks

**Attack 1 — [inconsistency] The Combined Verdict's "not settling" claim
is not actually gated by the settling-closure test built to establish it.**
Not caught by any of the five blind critiques. §5's Combined-verdict row
computes its verdict as a pure function of P-069-1 and P-069-2:
"Both...REFUTE together ⇒ coherent-fringe perturbation, decisively
established at settled STEPS...**not settling**." P-069-4 (Block
SETTLE-C80, the 1400/2800/4200 convergence closure for `C80`) sits as an
independent row whose own REFUTE band explicitly instructs: *"P-069-1/2's
own 2800-STEPS data must then be reported as bounded by this uncertainty,
not trusted outright."* Nothing in §5's actual CONFIRM/REFUTE table wires
that instruction into the Combined Verdict. As literally specified, a
REFUTE+REFUTE outcome licenses the words "not settling" even in a universe
where P-069-4 itself REFUTEs (C80 is shown NOT settled at STEPS=2800).
This is exactly the shape of gap Iteration 45's CHECKPOINT fired on — a
conjunctive safeguard whose second half doesn't actually bind the
headline claim — reproduced one level down, inside the very design meant
to close that finding.

**Attack 2 — [inconsistency] §4 overclaims the epistemic status of
`Δ(sinθ)=cpl/A` against the proposal's own Idealization 5 hedge, and
against exp-042's own documented derivation.** Idealization 5 correctly
states the period-match statistic "treats T21's established
`P(θ)=λ/(A·cosθ)` mechanism as the null hypothesis being tested, not as
ground truth." §4 does not honor that hedge: it calls `Δ(sinθ)=cpl/A` "a
known constant, not fit" and "not a new idealization," and calls the
fixed-`T` statistic "a strictly more rigorous version of the same,
already-established quantity, not a different one." Independently
verified against `experiments/042-t21-magnitude-bridge/NOTES.md` lines
20-27: `P(θ)=λ/(A·cosθ)` is stated there to be "the [full Huygens–Fresnel
aperture integral] model's own **stationary-phase limit**" — a
leading-order asymptotic recovered FROM the full coherent model, not
independently re-derived — and that full model was fit to real FDTD data
at R²=0.7852 (Iteration 19) → 0.8271 (Iteration 43's settled refit), never
1.0: 17–23% of variance stays unexplained, origin never identified. The
source is a raised-cosine taper (`TAPER=40` cells, independently confirmed
in `experiments/065-.../design_geometry.py:123`, 5.32% of `A=752` — EM's
figure checks out exactly), not a sharp two-point edge. §4's own
"differentiating `P(θ)` confirms `d(sinθ)/dθ=cosθ`" argument is a
self-consistency check on the local formula, not independent verification
that the formula holds identically across the 36°–42° window. This
matters concretely: it licenses treating a modest R² miss (say 0.30–0.45)
as clean evidence against T21's mechanism, when it could equally be a
correctly-detected-but-slightly-mis-centered fringe.

**Attack 3 — [unfalsifiable as currently scoped] A REFUTE+REFUTE outcome
cannot, by this design alone, distinguish "T21's own coherent
edge-diffraction mechanism" from "Yee-grid discretization structure at the
identical characteristic scale," yet §5's prose claims the former
specifically.** Both derive from the same physical edge the grid
discretizes (QUANTUM's point, independently sound: a Cartesian staircase
realization of a continuous taper generically carries the same angular
periodicity as the continuum diffraction pattern it approximates). This
program's own standing meta-rule (LOGBOOK RULED OUT, R3: "any surprising
feature gets a resolution check before it gets a mechanism debate — and
'artifact' claims need the check too") is not applied anywhere in this
design — `cpl=20` throughout, zero resolution leg. Idealization 5's own
final sentence half-acknowledges this ("a different, unmodeled periodic
mechanism...would require separate investigation, disclosed not claimed
to be ruled out") but §5's actual verdict language — "decisively
established," "real physics" — does not carry that hedge forward. Same
species of gap as Attack 1: a disclosed limitation in the idealizations
section that the scored verdict language quietly ignores.

**Attack 4 — [inconsistency, the sharpest structural gap — VISION's catch,
independently confirmed] The Combined Verdict's third bucket reopens the
exact escape hatch the LOCKED mandate exists to close.** §1's narrative
claims "either outcome closes the item for good"; §5's actual logic has
three buckets, and the third ("any other combination...⇒ PARTIAL...not
forced into either mechanism claim") commits Phase 3/4/5 to nothing.
PLAN.md's mandate text requires "no further relabeling, no further
citation-tripwire-only treatment" — a PARTIAL landing with no stated
consequence is structurally identical to the citation-tripwire-only
pattern that just fired Checkpoint criterion 4 one cycle ago, on this
exact test. A design meant to retire the deferral pattern must not leave
its own most-likely-looking outcome bucket (given the desk-check evidence
already on hand — see Attack 7 — a noisy, partially-locked, ambiguous
result is a live possibility, not a tail case) without a committed next
action.

**Attack 5 — [inconsistency, R4-adjacent] §1's own motivating citation
misattributes findings — VISION's catch, independently re-verified
against both experiments' committed NOTES.md.** "exp-066 later proved
unsettled at this exact channel and these exact angles by 59.8–74.4%" is
wrong on both figures and on attribution. `experiments/066-.../NOTES.md`
Setup states plainly: *"Geometry | exp-041/exp-065's C40 config,
unchanged"* — exp-066 tested only `C40`, never `C80`, at any angle. 74.4%
is exp-065's own C40 four-point convergence trend (`40°/600nm`); 59.8% is
exp-065's own P-VIS42-11 (`C80/40°/600nm`, Block SETTLE precedent). Both
belong to exp-065, not exp-066. A proposal whose entire purpose is
enforcing the T27 citation-discipline standard should not itself ship a
wrong provenance for the fact that motivates it — this is precisely R4's
class of house-discipline violation (hand-attributed figures that don't
trace to their real source), even though the numbers themselves are
correct.

**Attack 6 — [process omission, unfalsifiable-adjacent] The proposal is
silent on R_contact — MATERIALS' catch, independently confirmed against
PLAN.md's Iteration-46 queue text.** PLAN.md item 2 states explicitly:
"not gated to any rotation slot; pick up whenever tooling clears, **in
parallel with item 1 if capacity allows** (orthogonal, zero resource
competition)." §6's eight-item idealizations list has no R_contact line.
Given this program just fired Checkpoint criterion 4 last cycle for
exactly this species of silent-deferral pattern, and R_contact is
desk/literature work that cannot compete with this cycle's FDTD budget,
silence here is an omission, not scope discipline — the same failure mode
this cycle exists to stop repeating, in miniature, on a second thread.

**Attack 7 — [inconsistency] Idealization #2's "600nm cleanest,
least-aliased" justification for single-λ scope is backward — PHOTONICS'
and QUANTUM's independently-converging catch, independently re-verified
against `desk_check_settling_delta_output.json`.** Read directly from the
committed file: `samples_per_period_at_1deg_step` = 0.5027 (600nm), 0.6703
(450nm), 0.4022 (750nm) — all three are sub-Nyquist at 1° sampling (< 1
sample/period), and 600nm sits closest to the classic 2-samples-per-period
aliasing-critical rate, not furthest. Its `flip_fraction=1.0` (perfect
1°-step alternation) is the textbook symptom of a signal sampled at its
own Nyquist edge — indistinguishable from an alias — not evidence of clean
resolution. This program said so itself, in writing, at Iteration 19
(LOGBOOK T21: 600nm's near-Nyquist period "should show the cleanest
sign-alternation...exactly what the data shows" — offered as an *aliasing*
explanation there, not a cleanliness merit here). The desk check's
`flip_fraction` metric, additionally, measures a *different* quantity
(the STEPS-settling delta `C_2800−C_1400` at fixed padding) than Block
MINI's own scored quantity (the padding delta `C_80−C_40`) — a plausible
transfer, per VISION's independent finding, never disclosed as an
assumption.

**Attack 8 — [minor, disclosure gap] P-069-1's `ptp/|mean|` amplitude
statistic is ill-conditioned exactly where the existing data suggests it
will land — EM's supporting note, independently plausible given the desk
check.** As `mean(delta)→0` the ratio diverges regardless of true physical
amplitude; the desk check's own 600nm `flip_fraction=1.0` shows the
*settling*-delta alternates sign at essentially every 1° sample there,
consistent with (though not proof of) a near-zero-mean oscillatory series
for the related padding-delta quantity too. §5's table reports only the
ratio, not the raw `ptp` and `mean` magnitudes that would let a reader
distinguish "REFUTE because the fringe is genuinely huge" from "REFUTE
because the mean happened to sit near zero in this particular 31-point
window." Not blocking, but a cheap, load-bearing disclosure gap on the
cycle's own HEADLINE prediction.

**No constraint-#N-violation applies this cycle.** T1 route is N/A
(instrument/model-fidelity re-verification class, explicitly and
correctly disclaimed in §2); no σ(I)/σ(x,t)/angular-selectivity/
sub-threshold claim is made or advanced anywhere in the design. Checked
and confirmed clean.

## 2. Reconciliation of the five blind critiques — explicit, per-seat

**PHOTONICS (support-with-changes).** Steel-man on the `sinθ`
reformulation and 0.2°-step Nyquist margin is correct and independently
reconfirmed (Attack 2's own numbers don't dispute the *sampling* is now
adequate — only that the *formula* itself carries unquantified residual
error). Sharpest attack (600nm-Nyquist-backward) **ADOPTED IN FULL** —
independently re-verified against the desk-check JSON (Attack 7). Its
proposed fix (add a 750nm confirmatory sub-sweep) is **ADOPTED**, scoped
down slightly from PHOTONICS' own suggestion for budget discipline — see
docket item 7.

**MATERIALS (support-with-changes).** Steel-man (correct T1
self-classification, no realizability-territory drift) confirmed by
independent read of §2 and §6 — accurate. Sharpest attack (silent
R_contact omission) **ADOPTED IN FULL** (Attack 6) — independently
verified against PLAN.md's own queue text. Proposed fix (one disclosure
sentence) **ADOPTED VERBATIM** — docket item 9.

**ELECTROMAGNETISM (support-with-changes).** Steel-man accurate — three
real defects fixed, G-1 gate discipline sound, P-069-4 correctly
identified as the right (if narrow) test of the transient-aperture
confound. Sharpest attack (the "exact global period" overclaim) **ADOPTED
AND SHARPENED** — independently re-verified against exp-042's own
NOTES.md text and the R²=0.7852→0.8271 figures (Attack 2). Proposed fix
(promote P-069-3 from diagnostic to co-gating with P-069-2) is **ADOPTED
AND EXTENDED, not applied as literally stated**: EM's own framing only
composes P-069-2+P-069-3; this audit's Attack 1 (P-069-4 not wired into
the Combined Verdict at all) and QUANTUM's Attack 3 (no resolution check
to rule out grid-discretization) are the same species of gap — a
sub-test that exists on paper but doesn't bind the headline claim. Docket
item 3 below folds all three (P-069-3, P-069-4, and the new R3 legs) into
one restructured, fully-corroborated Combined-verdict gate rather than a
simple pairwise co-gate, which is a strictly stronger fix than EM's own
literal ask and addresses EM's stated concern (a real, slightly-detuned
fringe reported as vindicating the null) more completely. EM's supporting
note on `ptp/|mean|` ill-conditioning **ADOPTED** as a minor disclosure
fix (Attack 8, docket item 10) — EM itself flagged this as non-blocking,
and this audit agrees it does not rise to a blocking objection, only a
cheap fix.

**QUANTUM OPTICS (support-with-changes).** Steel-man accurate — the desk
check's provenance and scope (real 36-row dataset, correctly excludes
cross-±35°-gap pairs) independently reconfirmed by direct read of
`desk_check_settling_delta.py`. Sharpest attack (no resolution check to
separate T21's coherent mechanism from grid-discretization structure at
the same scale) **ADOPTED IN FULL** (Attack 3) — this is this program's
own standing R3 meta-rule, not a discretionary ask, and QUANTUM is correct
that it has never been applied to this specific fringe-vs-artifact
question. QUANTUM's secondary point (the desk check's own "600nm
least-aliased" framing is backward) **independently confirmed** and
merged with PHOTONICS' identical finding (Attack 7). Proposed fix (a
minimal 2-cell `cpl=30` recheck at the 39.0°/40.0° cells already earmarked
for Block SETTLE-C80) **ADOPTED VERBATIM** — this is already the
minimal, budget-conscious version of an R3 check, matching this program's
own established idiom (exp-005/010/015/023/025 precedent: one to three
representative points, never a full grid sweep). Given the conjunctive
test's own scope and cost/budget realities, a full `cpl` sweep is **not**
required and would be disproportionate; QUANTUM's own minimal ask is the
right size and is adopted as such — docket item 5.

**VISION SCIENCE (support-with-changes).** Steel-man accurate — correctly
credits this cycle with actually running the desk check first, unlike
Iteration 45. Sharpest attack (the PARTIAL escape hatch) **ADOPTED,
ESSENTIALLY VERBATIM** (Attack 4) — this is the single most important
finding among all five blind critiques, given the program's own
freshly-fired Checkpoint on exactly this failure mode. Misattribution
catch **ADOPTED, INDEPENDENTLY RE-VERIFIED** word-for-word against both
experiments' committed NOTES.md files (Attack 5) — VISION's citation of
exp-066's own Setup line ("exp-041/exp-065's C40 config, unchanged") is
exact. Line-by-line arithmetic audit **independently spot-checked and
confirmed correct** (wall formula, 3× envelope, 31-point grid
construction, `T=cpl/A` rounding all reproduce). VISION's own open
question (the desk check measures a different quantity than Block MINI
scores) folded into Attack 7 above, not treated as a separate finding.

**No override of any of the five critiques' core, load-bearing points.**
Every sharpest-attack is adopted in full or adopted-and-extended with a
stated reason; the only place this audit goes beyond "adopt as literally
proposed" is EM's co-gating ask, which is strengthened rather than
weakened, and QUANTUM's R3 ask, which was already minimally scoped by
QUANTUM itself. The one place this audit overrides is the *proposal's
own* Idealization #2 stance (scope-discipline against a "3× cost
redesign") — narrowed, not eliminated: a full 3λ duplicate of the 31-point
sweep is correctly out of scope, but a bounded, single-window 750nm
generalization leg is not the thing that idealization was written to
prevent, and the LOCKED mandate's "close it for good" bar justifies the
marginal cost.

## 3. Decisive rulings on the five posed questions

**EM's fixed-period-vs-asymptotic attack — does P-069-2 alone risk a false
CONFIRM, and should P-069-3 be promoted to co-gating?** Precisely stated,
the sharper risk is not quite "false CONFIRM of the additive-systematic
null" in isolation (that bucket requires P-069-1 to ALSO CONFIRM — low
`ptp/|mean|` — which Attack 8's own analysis suggests is unlikely given
the desk-check's near-zero-mean oscillatory pattern on the related
quantity). The real risk is twofold and both parts are real: (a) a
genuine, slightly-detuned coherent fringe landing in the R² 0.15–0.50
gray zone, producing an uninformative PARTIAL on a test meant to be
decisive (compounds with Attack 4); (b) a fixed-`T` fit crossing R²≥0.50
for a periodic structure that is real but is NOT specifically T21's
mechanism (Attack 3 — grid-discretization at the same scale would fit
just as well). **Yes — promote P-069-3, but not as a simple pairwise
co-gate. Fold P-069-2, P-069-3, P-069-4, and the new R3 legs (docket item
5) into one fully-corroborated gate (docket item 3) before "coherent-fringe
perturbation, decisively established" language is licensed.**

**PHOTONICS' 600nm-Nyquist-aliasing point — does the justification need
correcting, and should a 750nm leg be added?** **Yes to both, decisively.**
The justification is factually backward (Attack 7, independently
re-verified from the committed JSON) and must be corrected regardless of
any other change. Given the LOCKED item's "close for good" bar and the
proposal's own measured 17.6-minute headroom under its stated hard stop
(before any recompute), a bounded 750nm leg is affordable and directly
closes the one-wavelength generalization gap PHOTONICS correctly
identifies (750nm carries the largest established fringe amplitude,
`c*=3.23` vs 600nm's 2.74, per exp-042's own committed figures) — see
docket item 7.

**VISION's "PARTIAL escape hatch" point — does the Combined Verdict need a
concrete no-further-deferral rule, and is the misattribution fixed?**
**Yes, unconditionally, and yes.** This is the single highest-priority
fix in this docket — the LOCKED mandate's own text ("no further
relabeling, no further citation-tripwire-only treatment") has no teeth
without it, and this program fired Checkpoint criterion 4 exactly one
cycle ago on the same underlying failure shape. Docket item 4. The
misattribution is factual and independently confirmed — docket item 8.

**QUANTUM's R3-resolution-sweep demand — genuinely required this cycle, or
a disclosed follow-up?** **Genuinely required, in QUANTUM's own
minimally-scoped form.** This is not a discretionary nice-to-have folded
in for completeness — it is this program's own standing, named
house-discipline rule (LOGBOOK RULED OUT R3), directly on point for a
LOCKED, final-attempt instrument test whose entire purpose is separating
mechanism from artifact. Given the conjunctive test's own narrow scope
(two configs, one λ primarily) and real cost/budget realities, the
correct answer is QUANTUM's own proposed minimal 2-cell reuse of the
already-budgeted Block SETTLE-C80 cells at `cpl=30` — not a full grid
sweep, which would be disproportionate and is not what R3's own
precedent (exp-005/010/015/023/025) ever required. Docket item 5.

**MATERIALS' R_contact-disclosure point — does this cycle need an explicit
one-line deferral disclosure?** **Yes, unconditionally, cheap, and
consistent with this program's own established per-cycle practice** since
Iteration 41 (every cycle since has carried an explicit R_contact
disposition line, in prose or in `results.json`, whether deferred or
locked). Docket item 9.

## 4. Overall verdict

**PROCEED-WITH-MANDATORY-FIXES.**

The core design is sound and represents genuine, disciplined engineering
progress on a four-cycle-deferred instrument: it correctly identifies and
fixes all three real defects in `P-VIS42-10` (sparse sampling, unsettled
STEPS, and the never-coded period-match half of its own conjunctive
REFUTE clause), reuses proven machinery with zero `lab/` diff, and gates
every new number behind a bit-exact absolute-identity check before
trusting anything. No seat opposed; every seat's sharpest attack survives
independent re-verification and is addressed below. The gaps found —
principally the unbound Combined-verdict logic (Attacks 1, 3, 4) and the
backward 600nm justification (Attack 7) — are real but fixable at the
design stage, before any FDTD spend, at low marginal cost. None of them
implicates existing `lab/` code, any already-committed number, or any
constraint-3 verdict.

### Mandatory-fix docket (10 items — apply at Phase 3, before predictions are committed to git)

1. **Wire P-069-4 into the Combined Verdict as a binding precondition.**
   If P-069-4 REFUTEs (C80 not settled at STEPS=2800), the Combined
   Verdict must report the P-069-1/P-069-2 result as "bounded by unclosed
   settling uncertainty," never as "not settling," regardless of the
   P-069-1/P-069-2 outcome. (Attack 1 — this audit's own catch.)

2. **Correct §4's epistemic framing.** Remove "not a new idealization" and
   "exact global period" language describing `Δ(sinθ)=cpl/A`. Replace with
   language matching Idealization 5's own correct hedge and exp-042's own
   documented characterization: the fixed-`T` statistic tests consistency
   with T21's established stationary-phase-limit model (fit to real data
   at R²=0.7852→0.8271, never 1.0), not an independently-verified exact
   period. (Attack 2 — ADOPT + sharpen EM.)

3. **Restructure the Combined Verdict into one fully-corroborated gate.**
   "Coherent-fringe perturbation, decisively established, attributable to
   T21's own mechanism specifically" requires ALL of: P-069-1 REFUTE, AND
   P-069-2 REFUTE, AND P-069-3 lands within a disclosed tolerance of
   `T=cpl/A`, AND P-069-4 CONFIRM, AND the new R3 legs (item 5) show the
   fringe's location/amplitude survives resolution refinement. Any other
   combination is reported with precise, per-subtest hedged language (no
   forced mechanism claim) — matching this program's own P-066-4
   strictly-statistical precedent. (Attacks 1+2+3 — ADOPT+EXTEND EM,
   ADOPT QUANTUM.)

4. **Add a pre-committed, concrete non-decisive-outcome rule.** Before the
   run: "Any outcome short of full corroboration on item 3's combined gate
   is not reported as PARTIAL-and-deferred; it triggers immediate formal
   retirement of the period-match test at this cycle's own close, stated
   reason: statistical power was raised to the mandate's own spec and the
   result is still non-decisive — that is itself the finding." This
   satisfies PLAN.md's LOCKED "no further relabeling, no further
   citation-tripwire-only treatment" text directly. (Attack 4 — ADOPT
   VISION, essentially verbatim.)

5. **Add a minimal R3 (resolution) check.** Rerun the two Block
   SETTLE-C80 cells (39.0°, 40.0°, C80, 600nm) at `cpl=30` (both configs
   if budget allows, C80 alone at minimum), mirroring exp-025's
   established minimal-R3 idiom. Feeds gate item 3. (Attack 3 — ADOPT
   QUANTUM verbatim.)

6. **Correct Idealization #2's "600nm least-aliased" justification.**
   State the true fact: all three λ sample below Nyquist for their own
   fringe period at 1° step (`samples_per_period` 0.50/0.67/0.40 at
   600/450/750nm); 600nm's `flip_fraction=1.0` is the signature of
   near-Nyquist aliasing, not clean resolution. Also disclose that the
   desk check measures the STEPS-settling delta, not Block MINI's own
   padding delta — a plausible, not demonstrated, transfer. (Attack 7 —
   ADOPT PHOTONICS + QUANTUM.)

7. **Add a bounded 750nm confirmatory sub-sweep.** θ∈[38.0°,41.0°], 0.2°
   step (~16 points), both configs (C40/C80), STEPS=2800, same discipline
   as the 600nm leg. Phase 3 must recompute the full cost table with this
   leg AND item 5's R3 legs included, restate the hard stop explicitly,
   and apply the proposal's own pre-declared de-scope order if the
   recomputed 3× envelope breaches it — trimming this leg's size before
   cutting item 5 (resolution) or item 1/3's settling-closure legs, since
   generalization-breadth is lower-priority than the integrity checks that
   gate the headline claim. (Attack 7 — ADOPT PHOTONICS.)

8. **Correct the §1 misattribution.** "exp-066 later proved unsettled...
   by 59.8–74.4%" → reattribute both figures to exp-065 (its own C40
   four-point convergence trend, 74.4%; its own P-VIS42-11 C80 point,
   59.8%). exp-066 never tested C80. (Attack 5 — ADOPT VISION, verbatim.)

9. **Add a one-line R_contact disclosure.** State plainly: "R_contact
   (PLAN.md's Iteration-46 queue item #2) remains untouched this cycle;
   still blocked on WebSearch/WebFetch tooling, not picked up in parallel
   despite PLAN.md's explicit invitation to do so if capacity allows."
   (Attack 6 — ADOPT MATERIALS, verbatim.)

10. **Report raw `ptp` and `mean` alongside P-069-1's ratio.** Cheap,
    non-blocking, closes a real interpretability gap on the cycle's own
    headline statistic. (Attack 8 — ADOPT EM's supporting note.)

None of these fixes require new `lab/` engine code, change the design's
core construction, or threaten its budget by more than the cost of items
5 and 7 (both bounded and de-scopable). All ten are actionable before
predictions are committed to git, per house discipline.
