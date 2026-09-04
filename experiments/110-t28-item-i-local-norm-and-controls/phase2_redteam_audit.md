# PHASE 2 — RED TEAM FINAL AUDIT · Panel Iteration 87 (candidate exp-110)
## "Item i's Local-Magnitude Floor Gate, a Fault-Injection Control for
## `linear_fit_1_over_margin`, and `stage26`'s Truncation-Direction Control"

*Charter (PANEL.md, verbatim): attacks every proposal, speaks last and
hardest. Standard is NOT textbook-physics compliance — speculation is
permitted. Kills: internal inconsistency, unfalsifiable claims, mechanisms
that cannot be expressed as simulation parameters, and proposals that
quietly violate a target constraint — especially #3. Never leads a cycle;
no proposal of its own to protect. Sole seat receiving the Phase-1 proposal
AND all five Phase-2 critiques this cycle.*

Read in full: PANEL.md; LOGBOOK.md (RULED OUT R1–R26 in full; T28
Iterations 83–86, exp-106/107/108/109); `phase1_proposal.md`; all five
blind critiques (`phase2_critique_{photonics,materials,thermodynamics,
quantum,vision}.md`); `experiments/108-.../{run.py,analyze.py,
chunk_runner.py,NOTES.md,results.json}`; `lab/sections.py`
(`angular_scattered_pattern`, `widths`); `lab/validation/run_all.py`
lines 2698–2792 (`stage26_chunked_run_identity`).

---

## 0. Cycle framing

Governance/instrumentation cycle, T1 correctly N/A — confirmed
structurally, independent of the proposal's own claim: item 1 touches only
angular-pattern floor-gating arithmetic, item 2 a pure numpy curve-fit
diagnostic, item 3 a checkpoint/resume identity gate on a fixed empty-scene
bench. No σ(I)/σ(x,t)/angular-selectivity/sub-threshold machinery appears
anywhere; no constraint-1/2/3/4 verdict is scored or moved by any branch.
**Constraint 3 is not quietly dropped — it is correctly out of scope**,
matching every governance cycle since Iteration 84 (exp-107/108/109). All
five blind critiques land support-with-changes, zero opposition; each
found a genuinely different defect. No re-proposal of any R1–R26 idea
found anywhere in the proposal or the five critiques.

---

## 1. Independent re-verification from primitives (not trusted on the
##    critiques' own say-so)

### 1.1 PHOTONICS' common-mode-blindness claim — re-derived, CONFIRMED

Read `lab/sections.py::angular_scattered_pattern` (lines 200–263) directly.
`edges = linspace(-180, 180, 49)`, `centers[i] = -176.25 + 7.5*i`, so
`centers[47-i] = 176.25 - 7.5*i = -centers[i]` algebraically — exact index
reversal, matching the proposal's own claim and the committed
`bin_centers_deg` array at both r=156/312 (spot-checked by hand:
`i=0 → -176.25`, `i=47 → -176.25+352.5=176.25`, negatives exactly).

Physical premise (not just index bookkeeping), checked against
`experiments/108-.../run.py`'s `geom_fixedabs()`: `CY0=280`, `N0=560`, so
`CY0 = N0/2` exactly; both are scaled by the identical `k = r/78`, so
`CY = round(280k) = N/2` holds exactly at r=156 (`k=2`: CY=560=1120/2) and
r=312 (`k=4`: CY=1120=2240/2). The source (`add_line_source`, full-width
plane wave with symmetric edge taper both ends) and every box/circle
(`hypot(x-CX,y-CY)`, `CY±hw`) are manifestly even under `y → 2·CY−y`.
**Conclusion, independently reproduced: `pattern[i]=pattern[47-i]` is
forced by geometry+source+box in the noiseless/exact-grid limit** — the
premise the floor gate needs is genuinely true, not merely asserted.

Given that premise, the attack itself is a direct algebraic consequence,
re-derived here rather than trusted: `mirror_floor[i] =
|pattern[i]-pattern[47-i]|/2`. Decompose any per-bin measurement error
into an "odd" component `d_odd[i] = (e[i]-e[47-i])/2` and an "even"
component `d_even[i] = (e[i]+e[47-i])/2` about the pair's mean. Only
`d_odd` survives the difference; `d_even` — any bias, artifact, or
systematic offset that is IDENTICAL at bin `i` and its mirror bin `47-i`
— algebraically cancels to exactly zero in `mirror_floor`, regardless of
its magnitude. **CONFIRMED: this is a structural bias, not a sampling
issue — `mirror_floor` is provably a floor on the odd/antisymmetric noise
component only, and can never estimate common-mode/even noise, at any
sample size.** PHOTONICS' attack holds exactly as stated.

### 1.2 QUANTUM's correlated-statistic claim — re-derived, CONFIRMED

Read `angular_scattered_pattern` again with this question specifically:
does `pattern_peccored` and `pattern_hollow` share discretization? Both
are computed as `pt - pi` (article minus the SAME empty capture `cap_e`)
over the SAME box/perimeter geometry (`g["margin_boxes"][m]`, identical
`CX,CY` for both scenes at a given `r,m`) — confirmed directly from
`analyze.py::analyze_r()` (`pat_p = sc.angular_scattered_pattern(cap_p,
cap_e, box, g["ref"])`, `pat_h = sc.angular_scattered_pattern(cap_h,
cap_e, box, g["ref"])`, same `box`, same `cap_e`, only `cap_p`/`cap_h`
differ — and those two scenes differ ONLY in core fill, `pec_disk` vs.
none, per `chunk_runner.py::build_sim`; the shell/coating and the box
perimeter are identical). **CONFIRMED: peccored and hollow's per-bin
mirror-asymmetry draws are NOT independent samples — any registration or
Yee-staggering artifact tied to the shared box/grid/empty-reference
geometry (not the core) appears in both, correlated.** `max(mirror_floor
(peccored), mirror_floor(hollow))` is therefore not the two-independent-
draws robustness improvement its "AND-gate on both parents" framing
implies — it is closer to one draw counted twice. QUANTUM's attack holds
exactly as stated, and is a single-realization statistical-variance
concern, algebraically distinct from 1.1's structural bias.

### 1.3 VISION's R23-silence claim — re-derived, CONFIRMED

`grep -n "DISCLAIMER\|R23\|predictions_text\|result_text\|
build_predictions_text\|build_result_text" phase1_proposal.md` → zero
matches (independently re-run). Cross-checked VISION's own sharpest
claim — that exp-107's Phase 1 is the one other proposal in this family
that also never mentioned R23 — against
`experiments/107-t28-delta-scene-r5-census-decision/phase1_proposal.md`:
also zero matches. **CONFIRMED on both counts.** This is the exact
precondition of the regression LOGBOOK's own Iteration 84/85 record
(zero `DISCLAIMER` code shipped exp-107, caught only at Phase 5, closed
only as of exp-109/Iteration 86) — the parallel is real, not rhetorical.

### 1.4 MATERIALS' R14-mislabeling claim — re-derived from R14's own text

R14's own minimum discharge (LOGBOOK RULED OUT registry, R14(a)): "verify
the numerator's own parent quantities (A and B individually) are
smooth/monotonic, ruling out a sign-bookkeeping or registration artifact."
`classify_item_i_local`'s floor gate is a per-bin point check (does bin
`b` individually clear `K·floor`?) — it never evaluates
`pattern_peccored(θ)`/`pattern_hollow(θ)` as CURVES for smoothness or
monotonicity anywhere in the parameter table. **CONFIRMED: the proposal's
own "discharging R13 (denominator) and R14 (numerator-parent smoothness)
in one gate" (§1, Item 1) is false as stated** — only R13's discharge is
real; R14(a) is not performed. Separately worth noting (not raised by
MATERIALS, found independently here): R14(a)'s literal criterion — that
the parent curves be "smooth/monotonic" — does not even apply cleanly to
this channel. R14's founding case was a slowly-varying θ-sweep where
smoothness was a physically meaningful, achievable property; here
`pattern_peccored(θ)`/`pattern_hollow(θ)` are genuinely multi-lobed
diffraction patterns, non-monotonic and non-smooth BY PHYSICS, not by
artifact (PHOTONICS' own Phase-5 exp-108 finding: 62.5% of bins carry
<1% of peak power — a multi-lobed pattern, not a slow trend). So MATERIALS'
own remedy option (b) — "add the actual R14(a) verification" — cannot be
literally satisfied here; the only coherent fix is MATERIALS' option (a):
**drop the R14-discharge claim entirely**, not attempt a doomed literal
R14(a) smoothness check on curves that were never going to be smooth.

### 1.5 THERMODYNAMICS' cost-gate-unwired claim — re-derived from source

`grep -rn "COST_GATE" experiments/108-t28-.../` → two hits, both the
definitions themselves (`run.py:63-64`,
`COST_GATE_PILOT_S = 90*60`, `COST_GATE_TOTAL_S = 180*60`); the only other
match is the compiled `.pyc`. Read `chunk_runner.py` and `analyze.py` in
full: neither imports, reads, nor branches on either name anywhere.
**CONFIRMED: the cost gate is asserted in a docstring/Idealizations
sentence and exists as two unused module-level constants — zero
enforcement code, exactly as THERMODYNAMICS states.**

---

## 2. PHOTONICS vs QUANTUM on the mirror floor: one root cause or two?

**Two distinct defects, not one — re-derived from the algebra above, not
assumed by analogy to exp-108's own Iteration-85 "two distinct root
causes" ruling.**

- **PHOTONICS' defect is a structural bias in what the estimator can see
  at all.** `mirror_floor` is, by construction, a measurement of only the
  odd/antisymmetric component of per-bin noise (§1.1). No amount of
  additional sampling, pooling, or averaging over more bins, more margins,
  or more realizations can make this construction see an even/common-mode
  component — it is projected to exactly zero by the differencing
  operation itself, identically, every time. This is a **bias**, not a
  variance problem.
- **QUANTUM's defect is a variance/correlation problem in the estimate of
  the part the construction CAN see.** Even restricted to genuinely odd
  noise, a single per-bin, per-margin, per-pattern draw is a noisy
  estimate of that noise's typical scale, and peccored/hollow's shared
  box/grid/empty-reference geometry (§1.2) means `max(...)` over the two
  is not two independent looks at that noise — it is one look, doubled.

**Does QUANTUM's own proposed remedy (pool the mirror-asymmetry statistic
across bin-pairs/margins) also close PHOTONICS' concern? No — checked
directly against the algebra in §1.1.** Pooling `|pattern[i]-pattern[47-i]|`
over more bin-pairs or margins improves the estimate of the TYPICAL SCALE
of the odd noise component (addressing §1.2's variance concern), because
that scale genuinely varies bin-to-bin and margin-to-margin and more
samples narrow the estimate. It does nothing whatsoever for an even/
common-mode bias, because that bias is annihilated inside EVERY single
`|pattern[i]-pattern[47-i]|` term being pooled — pooling a set of numbers
that are all individually blind to a quantity cannot recover that
quantity. **Both remedies are independently needed; neither substitutes
for the other**, matching this program's own Iteration-85 precedent that
convergent-looking Phase-2 attacks on the same instrument can be genuinely
separate root causes (there ruled Defect A/Defect B; here, a bias vs. a
variance/correlation defect).

**One asymmetry worth flagging for Phase 3: the two remedies do not cost
the same.** QUANTUM's own fix — pooling the mirror-asymmetry statistic
across the 24 within-margin bin-pairs (or the 6 margins) for a given
pattern — requires **zero new FDTD and zero new persistence**: every
number it needs (the full 48-bin arrays, all 6 margins, both r) is already
what item 1b commits to persisting. This is a same-cycle, zero-marginal-
cost fix, not a deferred one (QUANTUM's own closing line: "closing the
single-point-estimate gap without expanding this cycle's scope" — QUANTUM
itself frames it this way). PHOTONICS' fix — an independent, non-
differencing floor estimate (a `cpl`-refinement spot check at the two
named bins) — genuinely requires new FDTD work and is correctly deferred.
**Recommendation below (§6) treats these two fixes asymmetrically for
this reason: QUANTUM's pooling becomes a same-cycle mandatory fix;
PHOTONICS' independent-estimate check stays an explicit Iteration-88
queue line, as the proposal itself already proposes.**

Within-margin pooling (across the 24 bin-pairs of a single, already-
captured 48-bin array) requires no additional statistical assumption
(same box, same capture). Cross-margin pooling (QUANTUM's alternative,
"or across the 6 margins for that bin") additionally assumes the noise
floor's scale is comparable across margins of different box radii — a
real assumption, not free, and should be disclosed as such if used
(R17's own "a tolerance must be justified" spirit, applied here to a
pooling assumption rather than a bracket width). **Recommend within-margin
pooling as the default; cross-margin pooling only with an explicit
justifying sentence if adopted.**

---

## 3. Is MATERIALS' R14-mislabeling finding a fresh R18 instance?

**No — checked element-by-element against R18's own operative text, not
assumed from the "R18-shaped" resemblance alone.**

R18's rule: "a check's own documented/claimed scope... must be
independently confirmed against the check's own actual source code,
line-by-line, before it is **relied upon, cited as closing a defect
class, or described as load-bearing**." The false "discharges R13 and
R14" claim lives in a **Phase-1 proposal** — a document that has not yet
been relied upon, cited as closing anything in a frozen record, or
described as load-bearing anywhere; no NOTES.md exists yet for this
cycle. MATERIALS caught it by exactly the line-by-line source check R18
prescribes, **at Phase 2, before any freeze** — this is R18's discipline
functioning as designed, not a violation of it. Compare against R14's
own founding precedent (exp-088): a Phase-1-adjacent overclaim caught and
corrected before it reached a frozen citation does not count as a fresh
instance of the rule it resembles; the rule fires only when the overclaim
SURVIVES into a relied-upon, frozen document. **Ruling: not a fresh R18
instance. Does not fire, does not tally toward R18's or R20's own
density bars.** It is, however, exactly the failure MODE R18 exists to
prevent, and Phase 3 must not let it survive into NOTES.md unchanged —
if the false discharge claim is repeated in the frozen synthesis without
correction, THAT would be the point a genuine R18-shaped citation defect
enters this program's permanent record. This makes the fix in §6 below
a hard Tier-0 requirement, not a stylistic nicety.

---

## 4. Is THERMODYNAMICS' cost-gate finding a fresh R23/R24/R25 instance?

**No — checked element-by-element against each rule's own operative text;
none of the three literally fires, and this appears to be a genuinely new
failure shape, not a recurrence of any named one.**

- **R23** ("a disclaimer required in multiple document sections must be
  enforced by a code-level assert on a single source-of-truth string, not
  manual prose-carrying-forward"): the cost gate is not a disclaimer
  string repeated across sections; R23's own text is scoped to that
  specific artifact class. Does not apply.
- **R24** ("a Phase-2 mandatory fix's own specified consequence, once a
  Phase-3 synthesis states it was 'adopted in full,' must be implemented...
  not merely computed and left as an unscored, disclosed observation"):
  R24 requires a **specific chain** — a Phase-2 mandatory fix, a Phase-3
  "adopted in full" claim, then a silent non-implementation. `COST_GATE_
  PILOT_S`/`TOTAL_S` were not introduced as a mandatory fix of any single
  prior cycle's Phase-2 critique — they are long-standing, inherited
  convention ("reused verbatim, exp-106's own r312_primary_committed
  rule," per the proposal's own item-3 note in its idealizations), never
  before subjected to a "Phase-3 adopted in full" claim about THEIR OWN
  enforcement specifically. There is no prior "adopted in full" statement
  this finding falsifies. **R24's literal trigger is not met — this is
  not the shape R24 names**, even though the flavor (a promised
  consequence with no code behind it) rhymes.
- **R25** ("a code-level fix an audit determines is necessary, but
  defers... must be added as its own explicit, numbered line item... never
  left only as a parenthetical"): no prior audit disclosed this exact gap
  and then deferred it under a scope excuse — THERMODYNAMICS is the FIRST
  seat, across this entire sub-thread's history back through exp-105/106,
  to name that the cost gate has never been code-enforced. There is no
  prior "named but dropped" instance for R25 to be a second occurrence of.
  Does not apply.

**Ruling: this is a genuinely new failure shape** — a long-lived,
repeatedly-invoked-in-prose numeric gate that has never once been
code-enforced across at least four cycles (exp-105→108) that each relied
on a human reading printed wall times and manually stopping. It shares
the family's general theme ("claimed governance behavior with no
executable teeth") but matches no single rule's specific operative
text. Per this program's own precedent (R26 was adopted for exactly this
situation — a genuinely new shape adjacent to, but not an instance of,
R4 or R18), **this is at most a candidate FOUNDING instance of a new
rule, not a firing of any existing one — and per every prior founding
instance in this registry (R5/R6/R9/R10/.../R26), a founding instance
does not fire Checkpoint criterion 4 on its own.** Reasoned through, not
assumed: given the cost gate is now independently attacked in this same
document by a blind Phase-2 critique naming the specific fix (wire it as
a real `if`/`assert`), that fix belongs on Phase 3's mandatory-fix list;
whether to name a fresh standing rule for "prose-promised numeric gates
with no enforcing code" is a judgment call left to the Director at
synthesis, not mandated here — the underlying gap is real either way and
must be fixed. **Does not fire Checkpoint criterion 4.**

---

## 5. Numbered attacks

**RT-1 [statistical-hazard]** — Mirror floor is structurally blind to
common-mode/even noise (PHOTONICS' finding; re-derived from primitives,
§1.1). A bin cleared RESOLVED under this floor could still be
contaminated by a systematic, mirror-symmetric bias the construction can
never detect at any sample size.

**RT-2 [statistical-hazard]** — Mirror floor is a single-realization,
correlated (peccored/hollow share discretization) point estimate of even
the noise component it CAN see (QUANTUM's finding; re-derived, §1.2).
`max(mirror_floor(peccored), mirror_floor(hollow))` does not buy the
two-independent-draws robustness its AND-gate framing implies.

**RT-3 [inconsistency]** — "Discharging R13 (denominator) AND R14
(numerator-parent smoothness) in one gate" is false as stated; only R13
is discharged (MATERIALS' finding; re-derived from R14's own text, §1.4).
Not a fresh R18 instance (§3) because it has not yet reached a frozen,
relied-upon document — but it must not survive into NOTES.md unchanged,
or it becomes one.

**RT-4 [code-not-wired]** — `COST_GATE_PILOT_S`/`COST_GATE_TOTAL_S` are
defined and referenced in prose but enforced nowhere in code
(THERMODYNAMICS' finding; re-derived, §1.5). Neither R23, R24, nor R25
literally fires (§4) — a genuinely new "prose-promised, code-toothless
gate" shape, four-plus cycles old, first named this cycle.

**RT-5 [documentation-gap]** — The proposal states zero position on how
item 1a's genuinely NEW wall time (distinct from exp-108's baked-in
7712.0s) will be reported, despite `build_result_text()`'s
`wall_time_source` parameter existing for exactly this purpose since
exp-109 (THERMODYNAMICS' additional finding, non-verdict-flipping but
real — the opposite-direction sibling of the gap THERMODYNAMICS itself
caught one cycle ago).

**RT-6 [documentation-gap]** — Zero occurrences of `DISCLAIMER`/`R23`/
`predictions_text`/`result_text`/`build_predictions_text`/
`build_result_text` anywhere in the proposal (VISION's finding; re-derived
by direct grep, §1.3), despite extending the exact six-margin family the
existing `DISCLAIMER` string covers. Independently confirmed: exp-107's
own Phase 1 is the ONE other proposal in this family with the identical
silence, and that is the cycle that shipped with genuinely zero
`DISCLAIMER` code, caught only at Phase 5. The precondition is reproduced
exactly; this is the single highest-priority item on this list precisely
because the precedent is not analogical, it is the same pattern recurring
one rotation later.

**RT-7 [documentation-gap]** — Minor, non-load-bearing: §0.5 point 2 names
nonexistent identifiers (`pattern_by_margin_delta[m]`,
`sigma_scat_by_margin_peccored[m]`/`_hollow[m]`) where the real committed
names are `pattern_delta[m]`/`pattern_peccored[m]`/`pattern_hollow[m]`,
with per-margin `sigma_scat` actually nested inside
`sum_check[m]["peccored"/"hollow"]["sigma_scat"]` (VISION's own
self-caught item, independently confirmed here by direct read of
`analyze_r()` lines 50–68). The substance of the claim is correct; the
cited identifiers are not verbatim. R4/R9/R20-lineage-adjacent, too
minor and non-recurring (single instance, self-caught, non-outcome-
reversing) to tag as anything beyond documentation-gap — flagged for the
record, not a mandatory-fix item on its own (folded into Phase 3's
routine copy-edit).

**RT-8 [documentation-gap]** (Red Team's own addition, not raised by any
Phase-2 critique) — Nothing in the proposal commits item 1c/1d's findings
to be **narrated** in Result prose, only "reported as an informational
diagnostic." R21's own standard ("a persisted field's own headline
finding must be stated inline in Result, not merely left in Setup/
persisted") is not literally engaged (item 1's diagnostic is not a
required verdict field), but the SAME failure shape — a real finding that
ends up in `results.json` and nowhere in the prose a future citation
would actually read — is exactly what R21 exists to prevent on adjacent
channels. Cheap to close: whatever `mirror_floor`/`classify_item_i_local`
finds (how many of the 30/48 low-power bins clear vs. fail K=3, and the
fate of the two PHOTONICS-named bins specifically) should be stated in
Result prose, not left implicit in the persisted JSON.

No `[unfalsifiable]` findings: every predicted outcome in the proposal
(items 1a/1b/1c/1d/2/3) states an explicit falsification condition,
independently checked here — none found wanting. No `[inexpressible]`
findings: no exotic mechanism is proposed; every instrument (mirror
differencing, OLS curve fit, checkpoint corruption) is concrete,
already-committed code or numpy arithmetic. No `[constraint-#N-
violation]` findings: constraint 3 (and 1/2/4) are correctly, structurally
out of scope this cycle, confirmed independently in §0, not merely
asserted by the proposal.

---

## 6. Unified mandatory fixes (combining overlapping critiques)

Following exp-108's own EM+QUANTUM-unified-fix precedent: fixes are
grouped by the underlying defect they close, not listed one-per-critique.

**Fix 1 (closes RT-2, same-cycle, zero marginal cost).** Replace the
single-point-estimate floor, `K * max(mirror_floor(pattern_peccored)[bin],
mirror_floor(pattern_hollow)[bin])`, with a floor built from a pooled
statistic of the per-bin mirror-asymmetry array — default: the median (or
a stated percentile) of `|pattern[i]-pattern[47-i]|/2` over the 24
within-margin bin-pairs, computed once per pattern per margin, not
re-drawn per bin. Uses only data item 1b already persists — no new FDTD,
no scope expansion. If cross-margin pooling is used instead of (or in
addition to) within-margin pooling, disclose the added assumption (noise
scale comparable across box radii) explicitly in Idealizations.

**Fix 2 (names RT-1, defers the remedy, mandatory disclosure now).** Add
an explicit Idealizations sentence stating the mirror floor (even after
Fix 1's pooling) remains structurally blind to common-mode/even noise
components — a bias, not merely unresolved variance — and cannot be
closed by pooling. Per R25's own discipline, promote the already-queued
Iteration-88 fault-injection control to name BOTH cases as separate,
explicitly numbered sub-items, not one parenthetical: (a) an injected
ASYMMETRIC synthetic perturbation (already planned), AND (b) an injected
SYMMETRIC/common-mode synthetic perturbation, confirming the floor
correctly does NOT flag it and does NOT inflate `local_snr` — PHOTONICS'
own named remedy, unaddressable by Fix 1, requiring new instrumentation
and therefore correctly deferred, not attempted this cycle.

**Fix 3 (closes RT-3).** Correct the "discharging R13 (denominator) and
R14 (numerator-parent smoothness) in one gate" language: drop the R14
half of the claim. Per §1.4, a genuine R14(a) smoothness check cannot be
meaningfully performed on multi-lobed diffraction-pattern curves that are
non-monotonic and non-smooth by physics, not by artifact — MATERIALS' own
option (b) is not achievable here. State plainly: item 1c/1d discharges
R13 only; R14 is not in scope for this construction.

**Fix 4 (closes RT-3's companion, MATERIALS' first item, not separately
numbered by MATERIALS but required alongside Fix 3).** Add the
discretization-vs-fabrication-tolerance disclaimer to Idealizations:
`mirror_floor` characterizes grid-discretization/floating-point noise for
the IDEALIZED simulated geometry only; a bin clearing it licenses no
inference about a physically realized coated-disk's own achievable
angular-pattern symmetry (real deposition/machining tolerances sit orders
of magnitude above this floor's ~1e-9–1e-4 scale).

**Fix 5 (closes RT-4).** Wire the cost gate as executable code, not prose:
after the r=156 pilot leg's empty-scene capture completes, sum its
measured wall time (already printed per-chunk by `chunk_runner.py`;
`analyze.py` should capture and total it) and compare against
`COST_GATE_PILOT_S`; halt the r=312 leg and write an explicit
`r312_deferred=True` field into `results.json` if exceeded, rather than
relying on a human reading printed times. Matches every other item in
this proposal's own parameter table, which specifies exact function
signatures elsewhere.

**Fix 6 (closes RT-5, bundled with Fix 5 as the same "cost/wall-time
accounting" concern).** State explicitly, in the eventual Result text,
that item 1a's own new wall time is measured fresh this cycle and is
distinct from exp-108's historical 7712.0s/6-call figure — use
`build_result_text()`'s existing `wall_time_source` parameter
(exp-109's own tool, one call site away from correct use here) rather
than reusing exp-108's text-assembly pattern unmodified.

**Fix 7 (closes RT-6 — highest priority on this list).** Bind Phase 3/4
to call `build_predictions_text()`/`build_result_text()` (imported from
the patched `experiments/108-.../run.py`, matching `reclassify_108.py`'s
own idiom) for this cycle's own predictions/result text; assert
`DISCLAIMER in` both; persist both into exp-110's own `results.json`;
NOTES.md quotes `result_text` verbatim. Report pass/fail on both asserts
before the Combined Verdict is written. Given §1.3's confirmed exp-107
parallel, this is not optional polish — it is the exact precondition of
this sub-thread's one and only prior regression, recurring on schedule
one rotation later if not closed here.

**Fix 8 (closes RT-8, cheap, folds into the Result section Fix 7 already
requires).** State in Result prose (not merely in the persisted JSON) how
many of the 48 bins clear vs. fail the `K=3` floor gate at each r, and the
disposition of the two PHOTONICS-named bins specifically (−146.25° at
r=156, +168.75° at r=312) — RESOLVED-with-genuine-structure or
UNRESOLVED-by-construction, whichever the run produces, with no
pre-committed direction (matching the proposal's own stated neutrality).

Fix 9 (RT-7, minor) folds into ordinary Phase-3 copy-editing — not
listed as its own numbered mandatory item; correct the identifier names
in §0.5 when NOTES.md is written.

---

## 7. Verdict

# PROCEED-WITH-MANDATORY-FIXES

No `HALT`-grade or `RETIRE`-grade defect found: no internal inconsistency
survives unaddressed once Fixes 3/4 are applied, no unfalsifiable claim
exists anywhere in the document, no mechanism is inexpressible (none is
proposed), and constraint 3 (nor 1/2/4) is not quietly touched, let alone
violated — this is a correctly-scoped governance cycle. The two
statistically genuine hazards on the mirror floor (RT-1/RT-2) are real
and independently re-derived from primitives here, but do not rise to
HALT because the instrument is, and stays, explicitly informational —
no scored verdict this cycle depends on `classify_item_i_local`'s output,
so neither hazard can corrupt this cycle's own deliverable, only mislead
a future cycle that promotes it without first applying Fix 1 (mandatory
now) and Fix 2's deferred remedy (mandatory before any such promotion).

**Zero overrides of any Phase-2 critique's core finding.** One partial
override, reasoned above: MATERIALS' own remedy option (b) for RT-3 (add
a genuine R14(a) check) is DECLINED as unachievable on physically
multi-lobed curves — option (a) (drop the claim) is adopted instead
(Fix 3). Both THERMODYNAMICS' and PHOTONICS'/QUANTUM's/VISION's
recommendations are adopted in full, elaborated into Fixes 1/2/5/6/7/8.

**Mandatory fixes for Phase-3 synthesis (numbered, as required — no
parenthetical folding, per this program's own R25 discipline):**

1. Replace item 1c/1d's floor with a pooled (median/percentile,
   within-margin-by-default) statistic in place of the raw
   `max(mirror_floor(peccored), mirror_floor(hollow))` point estimate —
   zero new FDTD, uses already-planned item-1b data.
2. Add an Idealizations sentence naming the mirror floor's structural
   blindness to common-mode/even noise (a bias, not variance, unclosed by
   fix 1) and split the already-queued Iteration-88 fault-injection
   control into two explicit, separately-numbered sub-items: (a)
   asymmetric perturbation (as planned), (b) symmetric/common-mode
   perturbation (new).
3. Correct the proposal's "discharges R13 and R14" language to "discharges
   R13 only" — a literal R14(a) smoothness check does not apply to
   multi-lobed diffraction-pattern curves.
4. Add the discretization-noise-vs-fabrication-tolerance disclaimer to
   Idealizations for the mirror floor.
5. Wire `COST_GATE_PILOT_S`/`COST_GATE_TOTAL_S` as an executable
   halt/defer check (not a prose promise) after the r=156 pilot leg,
   writing `r312_deferred=True` if exceeded.
6. State explicitly, using `build_result_text()`'s `wall_time_source`
   parameter, that item 1a's wall time is newly measured this cycle,
   distinct from exp-108's historical 7712.0s.
7. Bind Phase 3/4 to call `build_predictions_text()`/`build_result_text()`,
   assert `DISCLAIMER in` both, persist both to `results.json`, and quote
   `result_text` verbatim in NOTES.md — report pass/fail before the
   Combined Verdict.
8. State in Result prose (not only in `results.json`) the count of bins
   clearing vs. failing the K=3 floor gate at each r, and the disposition
   of the two PHOTONICS-named bins specifically.

**Checkpoint status: no criterion fires this cycle.** RT-3 is not a fresh
R18 instance (§3 — caught pre-freeze, exactly as R18's discipline
intends). RT-4 is not a fresh R23/R24/R25 instance (§4 — none of the
three rules' literal operative text is met; at most a candidate founding
instance of an as-yet-unnamed rule, which the Director may choose to
name at synthesis but which cannot fire on its own founding occurrence
either way, matching every prior rule in this registry). The
Iteration-85 Checkpoint-4 firing (R24, `classify_item_ii`) remains open,
unchanged, still pending Marsh's own ruling — correctly out of scope for
this Panel proposal (Tier-0 item 0), not attempted here, not resolved by
anything in this document.

**Recommended Iteration-88 queue additions (beyond this cycle's own
Fixes 1–8, for the Director's Reconciled-queue line items, each its own
entry per R25):** (i) PHOTONICS' independent, non-differencing floor
check at the two named bins (a `cpl`-refinement spot check) — genuinely
new instrumentation, correctly deferred; (ii) the split symmetric/
asymmetric fault-injection control (Fix 2 above); (iii) a judgment call,
not mandated here, on whether "a prose-promised numeric gate with no
enforcing code" (§4) merits a new standing rule alongside R23/R24/R25,
given this is (to this audit's knowledge) the first time this specific
shape has been named in four-plus cycles of reuse.
