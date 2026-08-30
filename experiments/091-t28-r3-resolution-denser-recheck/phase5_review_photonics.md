# PHASE 5 — REVIEW · PHOTONICS · exp-091 · Panel Iteration 68

*Fresh context, blind to any other seat's current-cycle Phase-5 output. Read
in full: `PANEL.md`; `LOGBOOK.md` start to end (R1–R14 in the RULED OUT
registry; the complete T28 live-thread arc, Iterations 46–67, both
CHECKPOINT entries at Iterations 61/65); the complete exp-091 record
(`phase1_proposal.md`, all five Phase-2 critiques, `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `NOTES.md`, `run.py`, `run_output.txt`,
`results.json`); exp-087–090's `NOTES.md`/`phase5_redteam_audit.md` for the
caution-zone/Firth-fit deliverable this cycle bears on; `experiments/069-.../
design_geometry.py` for the R3_RATIO scaling logic. No FDTD run; no other
file modified.*

## Verdict: **CONCUR-WITH-GAP**

The physics is sound and honestly reported where it exists in writing: I
independently re-derived every load-bearing number in `run_output.txt`/
`results.json` from raw primitives (§1) and found no R4-class slip, no
geometry-rescale bug, and no settling confound. The ten-item Phase-2
mandatory-fix docket is faithfully executed in `run.py` (§2). On my own
charter question — is a sign-flipping, moved zero-crossing under `cpl`
20→30 physically plausible for this channel, or does it smell like a
subtle R3-rescale defect — my answer is **plausible, not suspicious** (§3),
for reasons grounded in this program's own T10/T21/T28 record, not
assertion. The **gap** is that `NOTES.md` — the frozen document this whole
sub-thread's own house discipline treats as the permanent record — was
never updated with a Result/Learned section after the run: every number in
this review comes from `run_output.txt`/`results.json` directly, and at
least one of the ten frozen mandatory-fix items (item 10, the cross-
reference) resolves to an uninformative null (`None`) that is nowhere
written down or explained (§4). That is a real, fixable completeness
defect in the record, not a scientific one — hence CONCUR-WITH-GAP, not
plain CONCUR or PARTIAL.

## 1. Independent reproduction from raw primitives (not trust)

Pulled directly from `run_output.txt`/`results.json`, recomputed by hand:

- **The headline sign flip.** `delta_scene(40.2°, cpl=20, Leg1 fresh
  STEPS=4200) = −1.542677×10⁻⁴`; `delta_scene(40.2°, cpl=30, Leg2)
  = +4.369899×10⁻⁴`. Sign flips. The filed `STEPS=2800` comparator
  (`−1.540815×10⁻⁴`) agrees with the fresh `STEPS=4200` value to 0.12%
  relative — the flip is a `cpl` effect, not a settling artifact (confirms
  (c1)'s own clean CONFIRM independently, §3 below).
- **`ratio_k(41.4°, cpl=30) = frac_p_abs/frac_contrast = 9.588537×10⁻³ /
  1.040919×10⁻³ = 9.2116`** — matches `results.json`'s own
  `9.211608e+00` and the task brief's own cited figure to 4 s.f. This is
  below `RATIO_HIGH=10.0`, hence CONSISTENT — a genuine reclassification
  from the `cpl=20` reading (`ratio_k=28.85`, filed `28.8072`,
  ENERGY-DOMINANT).
- **`ratio_k(40.2°, cpl=30) = frac_p_abs/frac_contrast = 7.936113×10⁻³ /
  7.877482×10⁻⁴ = 10.07443`**. `(10.07443−10.0)/10.0 = 0.74%` above
  `RATIO_HIGH` — razor-thin, confirmed exactly as characterized.
- **`_label()`'s own threshold convention**, read directly from
  `experiments/087-.../run.py:193-194`: `ratio > RATIO_HIGH ⇒ "X"`
  (strict inequality) — `10.0744 > 10.0` is unambiguously ENERGY-DOMINANT
  by the code's own committed rule, not a rounding-adjacent judgment call.
- **The bracket-REFUTE claim.** At `cpl=30`: `delta_scene(40.2°)=
  +4.3699×10⁻⁴`, `delta_scene(40.4°)=+9.8564×10⁻⁴` — same sign, both
  positive and *growing*, so no crossing lies between them (the true
  crossing, if the local slope holds, sits *below* 40.2°, i.e. outside the
  bracketed window on the near side). At `41.4°/41.6°`: `+5.6255×10⁻⁴` /
  `+1.7838×10⁻⁴` — same sign, both positive and *shrinking* toward zero
  (the crossing, if the slope holds, sits *above* 41.6°, outside the
  window on the far side). Both bracket legs independently confirm: no
  sign change is found in either `[40.2°,40.4°]` or `[41.4°,41.6°]` at
  `cpl=30` — the known `cpl=20` crossings (`40.265°`/`41.461°`) are not
  reproduced inside either window. `find_zero_crossings` correctly returns
  empty and the code correctly scores this REFUTE (`a2_report`'s own
  "no sign change... cannot interpolate" branch), not a silent NEITHER.
- **`(b2)` numerator check**: `frac_p_abs_R3/frac_p_abs_cpl20` = `2.7756`
  (37.2°), `1.1178` (40.2°), `1.3270` (41.4°) — all inside `[0.3,3.0]`,
  all sign-matched ⇒ CONFIRM, exactly as filed. The entire instability is
  denominator-side, confirmed by direct recomputation, not merely restated.
- **`(c1)`/`(c2)` settling.** All six `(c1)` cells and all four `(c2)`
  cells (both angles, per the corrected fix-1/fix-2 scope) show relative
  deviations of `0.0001%`–`0.0138%`, six orders of magnitude inside the
  `≤1%` CONFIRM band. Settling is cleanly, unambiguously ruled out as an
  explanation for the sign flip at both resolutions — verified, not taken
  on faith.
- **The `R3_RATIO` article-geometry claim** (`results.json::
  r3_article_geometry_note`). Read `experiments/069-.../design_geometry.py`
  directly (not the note's paraphrase): `R3_RATIO=1.5` is a single module
  constant applied uniformly to `R3_BASE_NX/NY/ABSORB/SRC_X/PLANE_X/
  OBJ_X/TAPER`, and `R3_R_OUT=round(R_OUT*1.5)=117` is a **pre-existing**
  named constant (not new this cycle). `run.py`'s new
  `PEC_R_R3=round(30*1.5)=45` uses the identical rule. Both `30→45` and
  `78→117` are *exact* integer multiples (no `.5`-rounding ambiguity,
  unlike `R3_BASE_PLANE_X` (`77×1.5=115.5→116`) or `R3_GUARD_OUT`
  (`185×1.5=277.5→278`), two pre-existing, previously-used R3 constants
  that *do* carry a sub-cell (≤0.5-cell, ≤10–15 nm, ≤λ/40) rounding
  idealization). The claim that this is "the only value consistent with
  the single R3_RATIO scaling rule" is not merely asserted — it follows
  from the physical requirement `L_GEOMETRIC_M_R3 == L_GEOMETRIC_M`
  (asserted in code, line 174, and true only if *every* linear dimension
  of the article scales identically with the grid pitch). I find this
  claim **verified**, not merely trusted, and note that the one available
  alternative source of a rescale artifact (round-half-up idealizations
  elsewhere in the R3 machinery) is two orders of magnitude too small
  (≤λ/40) to explain a full-period sign flip.

No arithmetic, labeling, or geometry defect found anywhere I could
independently check.

## 2. Did the ten-item Phase-2 mandatory-fix docket actually land in `run.py`/`NOTES.md`?

Checked each against the committed code/document, not `phase3_synthesis.md`'s
own claim to have applied it:

| # | Fix | Where it landed | Applied? |
|---|---|---|---|
| 1 | Settling spot-check at 41.4° (or both) | `SETTLE_ANGLES=[40.2,41.4]`, both run at `STEPS=6300` (run.py:134,461; run_output rows 25-32) | **Yes — both angles** |
| 2 | Correct Idealization 10 | `NOTES.md` §Idealizations item 10, restated | **Yes** |
| 3 | PHOTONICS' location-sensitive companion test | `(a2)`, `find_zero_crossings` on bracket pairs (run.py:505-549) | **Yes** |
| 4 | EM's bracketing points | `BRACKET_ANGLES=[40.4,41.6]`, grid-aligned via `.index()`, not hand-typed (run.py:137-140) | **Yes**, and more careful than the minimum ask (asserted membership, not a hand computed index — the exact R4-avoidance discipline this program's own house rule demands) |
| 5 | THERMODYNAMICS' `frac_p_abs` co-equal check | `(b2)`, same `[0.3,3.0]`/`[0.1,10]` bands (run.py:577-594) | **Yes** |
| 6 | Banner citation fix | `NOTES.md` banner reads "Idealizations 3/6/7" (not the proposal's stale 3/7/8) | **Yes** |
| 7 | Absolute-Weber-contrast comparison | `NOTES.md`, disclosed-non-gating bullet under Predictions §(d) | **Yes**, text present (I did not find it re-verified against this cycle's *own* freshly-measured `delta_scene` — it still cites the `cpl=20` values used at Phase 2/3 freeze time, which is correct: it is a pre-registered disclosure about the *band*, not a post-hoc fact about the *measured* result) |
| 8 | Operationalize/drop "felt-lucky" claim | `(d)`, `margin_4200` printed and compared to the cited `STEPS=2800` figure (run.py:644-652; run_output line 107-108) | **Yes, operationalized** — see §4 for what the actual number says |
| 9 | Precision QUANTUM's wording | `NOTES.md` §(b), "a close, live possibility... not the expected case" | **Yes** |
| 10 | Cross-reference item 1 (settling) against item 4 (crossing shift) | `run.py`:689-703, computed and printed | **Executed, but resolves to an uninformative null** — see §4 |

Nine of ten land cleanly. Item 10 is where the gap driving my verdict
lives.

## 3. PHOTONICS' own charter question: is this physically plausible, or a red flag on the R3-rescale?

**Plausible, and for reasons this cycle's own honest two-sided framing
already anticipated — not evidence of a subtle rescale bug.** Four
independent lines of reasoning, none requiring new FDTD:

**One source-attribution correction first, per this program's own
verify-before-claim discipline.** The task brief's framing cites "T21's
own established ~2.84–2.95° period" — I checked this against `LOGBOOK.md`
directly and it is not quite right: `T21`'s own established period is
`P(θ)=λ/(A·cosθ)≈1.9608°` at 40°/600 nm (a source-aperture-edge Huygens
fringe, Iteration 18–19). The `~2.84–2.95°` period is `T28`'s **own**,
separate, still-unexplained periodicity (opened Iteration 46, exp-069),
explicitly established as **not matching** `T21`'s fringe (`45%` off) —
LOGBOOK's own text: T28's signal "does NOT match T21's own established
fringe period." Both periods are real and on the record; they are not the
same finding, and nine-plus T28 mechanism-search cycles have specifically
foreclosed reflection/echo explanations tying the two together. I use the
correct (T28) attribution throughout below.

**3a. This channel was already independently proven to be a coherent
propagation-*phase* signal, not an absorption-*magnitude* one — exactly
the class of quantity where location, not amplitude, is the fragile
observable.** exp-076's own Red-Team-confirmed proof (`_damping` in
`lab/fdtd2d.py` depends only on `absorb`, never `pad`) establishes that
`G40`/`C40` share bit-identical boundary reflectance — `delta_scene`'s
entire signal is a `PAD`-driven round-trip *timing* effect. Ordinary
Yee-grid numerical dispersion is a per-cell *phase* error that
**accumulates linearly with propagation distance**, not a per-cell
*amplitude* error. A timing/phase signal integrated over the near-field
aperture's own long path (`A`≈752–1128 cells, i.e. tens of wavelengths at
600 nm) is structurally the observable most exposed to a finer grid
shifting *where* a zero-crossing sits, as distinct from *how big* the
signal is elsewhere. This is precisely PHOTONICS' own Phase-2 attack
(upheld by Red Team) about why the reused `[0.3,3.0]` magnitude-ratio
band — built for `C80−C40`, a genuine `ABSORB`-*depth* (reflectance-
magnitude) delta — was never a clean fit for a `PAD`-timing delta in the
first place. The data now confirms the concern the design itself flagged
as live, not a surprise outside the design's own stated risk.

**3b. This program's own T10 precedent already put a comparable-magnitude
resolution sensitivity on the record for exactly this measurement
*class*.** T10 (exp-027, native cpl→cpl×1.5) found a near-field
point/field-probe channel's relative spread grow from 46%→128% (raw,
before an unrelated `SIGMA_ON` confound was found and removed, leaving a
smaller but real ~46%→49% residual). `frac_contrast`/`delta_scene` is
built on `lab/ambient.py`'s Weber-contrast field probe — the *same*
measurement family T10 characterized, not the closed-surface flux
integral (`sections.widths()`) that this program's own EM seat
(Phase-2, upheld) correctly notes has a much cleaner resolution-
convergence history (T9/T10/T11's own ~6.5% box-ledger spread). This
cycle's measured `frac_contrast` ratios — 5.21× (37.2°), 2.78× (40.2°),
4.16× (41.4°) — land in the *same order of magnitude* as T10's own
original, unconfounded 128%/46%=2.78× raw growth ratio (note the
near-exact numerical coincidence at 40.2° — almost certainly that, a
coincidence, not a mechanistic link, but a useful sanity check that this
cycle's numbers are not off-the-charts for this specific channel class).
A channel with an established ~2.8×-scale resolution-sensitivity history
producing a 2.8×–5.2× shift, including two sign flips at points chosen
*specifically* because they sit closest to a zero-crossing, is squarely
within — not beyond — this program's own prior experience with this
instrument family.

**3c. A back-of-envelope linear extrapolation of this cycle's own two
already-collected bracket points, at each crossing, puts the likely shift
at a modest fraction of the established period — not an implausibly large
one.** (This is my own informal estimate from already-committed numbers,
outside this cycle's own committed test — I flag it as such, not as an
adopted result.) At the `40.2°/40.4°` pair: `delta_scene` rises from
`+4.3699×10⁻⁴` to `+9.8564×10⁻⁴` over `0.2°` (slope `≈+2.74×10⁻³`/°);
extrapolating that slope backward to zero puts the `cpl=30` crossing near
`40.2°−4.3699×10⁻⁴/2.74×10⁻³ ≈ 40.04°` — a shift of `≈0.22°` from the
native `40.265°` crossing, about **8% of T28's own established
~2.84–2.95° period**. At `41.4°/41.6°`: `delta_scene` falls from
`+5.6255×10⁻⁴` to `+1.7838×10⁻⁴` (slope `≈−1.92×10⁻³`/°); extrapolating
forward to zero puts the crossing near `41.4°+5.6255×10⁻⁴/1.92×10⁻³ ≈
41.69°` — a shift of `≈0.23°` from `41.461°`, again `≈8%` of the period.
**Both back-of-envelope shifts are modest, single-digit-percent-of-period
corrections, not the multi-period jump a genuine rescale bug (e.g. a
mis-scaled aperture or a stray off-by-one in the article geometry) would
plausibly produce.** This is informal — the fringe is independently known
to be chirped/non-stationary (exp-084/085), so a two-point local slope is
not a rigorous crossing estimate — but it is a useful, cheap
plausibility check, and it points toward "ordinary accumulated
dispersion," not "something is broken."

**3d. What I did *not* find: any sign of a geometry-construction defect.**
I checked the two things most likely to hide a subtle bug — rounding
parity between the native and R3 article radii, and whether the R3 core/
shell scaling is genuinely forced by the design's own stated Idealization
4 rather than an arbitrary choice (§1, last bullet). Both check out clean.
A circular boundary's Yee-grid staircase pattern at `r=30`/`r=78` cells is
not a self-similar rescaling of the pattern at `r=45`/`r=117` cells (a
rasterized circle at a different radius does not preserve its own
staircase shape) — this is a real, always-present, deterministic
(non-noise) discretization difference between the two resolutions,
already a known lesson of this program (`VALIDATION.md`'s staircasing
caveat), and itself a *legitimate* contributor to a genuine
resolution-sensitive phase shift, not a sign of a coding error.

**Answer to the specific question posed:** no, I do not think the
magnitude of the shift is suspiciously large for a mere grid-resolution
effect, and I found no evidence pointing at a subtle rescale defect over
a genuine physical resolution-sensitivity reading. What I cannot do —
and what this cycle's own honest scope does not claim to do — is name
*why* T28's own ~2.84–2.95° periodicity exists in the first place (nine-
plus prior mechanism-search cycles have foreclosed every reflection/echo
class tested); without that, no seat can yet derive a first-principles
*quantitative* prediction for how far a crossing should move under
`cpl` 20→30. This cycle's own genuinely two-sided, no-lean framing (§4b
of `NOTES.md`) was the epistemically correct posture going in, and the
result validates that posture rather than surprising it.

## 4. What is under-disclosed: the missing Result section and item 10's null

**`NOTES.md` has no Result/Learned section at all** (confirmed: the
document's own section headers are `Hypothesis`/`Setup`/`Predictions`/
`Idealizations`, 221 lines, ending immediately after the idealizations
list — I grepped for `^##` and found no fifth heading). Every finding in
this review, and in the task brief handed to me, is reconstructed from
`run_output.txt`/`results.json` directly, not from a written Result
section in the frozen predictions document. This matters for three
concrete reasons, not merely as a formality:

1. **Mandatory-fix item 10 (the cross-reference between the crossing-shift
   finding and the settling-residual finding) resolves to an uninformative
   null, and nowhere is this stated in prose.** `run_output.txt`'s own
   line: `larger (a2) crossing shift at Nonedeg... directionally
   consistent=None` — because neither bracket produced a numeric shift
   (both REFUTEd on "no sign change found"), the cross-reference the
   mandatory-fix docket asked for cannot be computed as specified. The
   code degrades correctly (no crash, no silently-wrong number), but the
   *interpretation* — "this comparison could not be made because both
   crossings moved out of the sampled window entirely, which is itself
   informative" — exists nowhere in writing.
2. **Item 8's "felt-lucky" relief claim reports a genuinely marginal,
   possibly-null result that no prose discusses.** The 37.2° `resolved`-
   gate margin at `STEPS=4200` is `1.061940×`, against the cited
   `STEPS=2800` figure of `1.045659×` — a `1.5%` relative increase. This
   is technically "relief" in the predicted direction, but it is a
   two-decimal-place effect on a quantity this sub-thread's own record
   (exp-089 Learned #4) called "felt-lucky" at `1.046×` — a `1.6%` move
   does not obviously earn the word "relief" un-qualified, and the
   Phase-1 proposal's own §1 claim (flagged by Red Team as RT-1, an
   unfalsifiable narrative benefit) is discharged by a number that itself
   needs a sentence of interpretation nobody has written.
3. **The Iteration-65 CHECKPOINT's own escalated rule requires the
   carried-idealizations banner "at BOTH the Predictions section AND the
   Result section of any future T28 committed-predictions document."**
   With no Result section, that requirement cannot be met by construction
   — not because anyone dropped it, but because the section it is
   supposed to be carried into does not exist. I do not think this rises
   to a fifth disclaimer-erosion instance (the banner's *substance* is
   fully present and correctly cited at the one section that does exist,
   matching Red Team's own Phase-2 ruling on the milder miscitation
   defect, §1.5 of `phase2_redteam_audit.md`) — but an escalated rule
   that can be trivially satisfied by omitting the section it targets is
   a gap worth naming, distinct from the miscitation Red Team already
   caught.

None of this changes any scored verdict in `results.json` — the raw
numbers and classifications are correct and independently reproduce. It
is a completeness gap in the permanent written record this program's own
house discipline (verify-before-claim, same as the Disclosure culture;
every writeup states its idealizations) exists to prevent, and it should
be closed — with a short Result/Learned section stating items (a)/(a2)/
(b)/(b2)/(c1)/(c2)/(d) plainly, including item 10's own null and item 8's
own marginal number — before this cycle is cited elsewhere as complete.

## 5. What this means for exp-090's caution zone and Firth fit

**This result meaningfully undermines the specific numeric boundaries of
exp-090's deliverable — not the deliverable's methodological device in
principle.** I re-verified exp-090's own `NOTES.md` directly (not a
paraphrase): the n=7 sample underlying the caution zone `[1.4764,
2.1709]` and Firth's `m₅₀=2.071013` contains **exactly two** points
carrying the positive (`Y=1`, ENERGY-DOMINANT) label — `40.2°`
(margin `1.4764×`, literally the order statistic that sets the zone's own
lower edge) and `41.4°` (margin `1.3095×`, the sample's *other* positive
point, sitting below the zone). Firth's bias-reduced logistic fit exists
specifically because a naive MLE diverges on a perfectly-separated,
single-digit sample — its entire "positive class" support, at n=7, is
these two points.

This cycle shows that at `cpl=30`, **one of those two points (`41.4°`)
flips to `Y=0`, and the other (`40.2°`) survives by `0.74%` of the
threshold's own value** (`10.0744` vs `10.0`) — both previously read
confidently ENERGY-DOMINANT (`ratio_k` 25–29) at `cpl=20`. In other
words: the *entire* labeled positive class the caution zone and Firth fit
were built on does not survive this program's own first resolution check
at either of its two members. `37.2°` (the point setting the zone's
*upper* edge and Firth's most load-bearing `Y=0` point) is independently
CONFIRMED stable (§1) — the CONSISTENT side of the sample holds up. The
ENERGY-DOMINANT side does not.

This does not mean the caution-zone *method* (a non-parametric order-
statistic gap plus a bias-reduced logistic fit, honestly scoped as
provisional at n=7 by exp-090's own text) was wrong to propose, and it
does not retroactively invalidate `37.2°`'s own CONSISTENT reading or
this cycle's own clean settling checks. But it does mean: **any future
citation of `[1.4764,2.1709]` or `m₅₀=2.071` as a resolution-verified
decision boundary would be a new instance of this program's own R3 meta-
rule violation** — the zone's defining data points have now been shown,
at the one location this program has actually resolution-checked them,
to be unstable at exactly the classification threshold that defines the
label they contribute. A re-fit of the caution-zone/Firth model with the
`41.4°` label corrected (or flagged as resolution-unstable, `Y`
undefined) — and a frank acknowledgment that the surviving positive
point (`40.2°`) is itself now shown to sit within `1%` of its own class
boundary — is the honest next step, not a footnote. I would not treat
`m₅₀=2.071` as load-bearing for any future decision until that re-fit
exists.

## 6. Ranked top-3 candidate directions for Iteration 69 (PHOTONICS' own lens, not coordinated with any other seat)

1. **Close the record-hygiene gap this review found before anything else
   builds on this cycle**: add a Result/Learned section to `NOTES.md`
   stating (a) REFUTE/(a2) REFUTE-both/(b) 37.2° preserved, 40.2°
   razor-thin-preserved, 41.4° flipped/(b2) CONFIRM/(c1)(c2) CONFIRM
   plainly, discharging item 10's own null and item 8's own marginal
   number in writing — cheap, zero FDTD, and this program's own R4/R9
   discipline treats an unwritten result as a standing debt, not a
   cosmetic one.
2. **Re-fit exp-090's caution zone/Firth model treating `41.4°`'s label
   as resolution-unstable** (either drop it, or refit with an explicit
   `Y`-uncertain third category), and re-run the n=7 sample's own
   permutation/AUC test on the reduced or re-labeled set — zero FDTD,
   directly answers whether the caution zone survives without its only
   other positive-class anchor. This is the single most consequential,
   cheapest next step this cycle's own result opens.
3. **A genuine crossing-localization leg at `cpl=30`**, densifying the
   bracket beyond the two REFUTEd windows (e.g. `39.6°–40.2°` and
   `41.6°–42.2°`, following my own §3c back-of-envelope estimate that the
   true crossings sit roughly `0.2–0.3°` outside the tested brackets) —
   this would convert my informal linear extrapolation into an actual
   measurement of where the `cpl=30` crossings live, closing (a2) properly
   rather than leaving it at "REFUTE, location unknown." Cheaper and more
   targeted than PHOTONICS' still-queued grazing-incidence validity check
   or the still-14-plus-cycle-deferred x-wall wavelength-generality leg,
   both of which remain open but are not sharpened by this cycle's own
   result the way the crossing-localization question is.
