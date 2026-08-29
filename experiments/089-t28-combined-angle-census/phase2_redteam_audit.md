# PHASE 2 — RED TEAM FINAL AUDIT · exp-089 · Panel Iteration 66

*Fresh context. Read: PANEL.md in full; LOGBOOK.md's RULED OUT (R1–R14) in
full, the ESTABLISHED section, and LIVE THREADS/T28 Iterations 58–65 (both
CHECKPOINT entries) in full through Iteration 65/exp-088; `phase1_proposal.md`
in full; all five blind Phase-2 critiques (photonics, materials, em,
thermodynamics, quantum); exp-088's `phase2_redteam_audit.md` for house-style
calibration. Independently re-derived every load-bearing number below from
raw primitives (`experiments/083-.../results.json`,
`experiments/088-.../results.json`), not trusted from any seat's own prose —
R4/R9 discipline.*

## 0. Independent verification performed

- **All three R13 desk margins reproduce exactly**, computed fresh from
  `experiments/083-.../results.json::per_theta` and the cited
  `FLOOR=1.91744×10⁻⁴`: `frac_contrast(37.2°)=4.162655×10⁻⁴` → **2.1709×**;
  `frac_contrast(40.2°)=2.830881×10⁻⁴` → **1.4764×**;
  `frac_contrast(41.4°)=2.510967×10⁻⁴` → **1.3095×**. Matches all five
  critiques and the proposal's own rounded 2.17×/1.48×/1.31×.
- **All three zero-crossings reproduce exactly** by linear interpolation of
  `delta_scene(θ)` across the real 31-point grid: 37.1273° (between
  37.0°/37.2°), 40.2654° (40.2°/40.4°), 41.4609° (41.4°/41.6°) — matching
  the cited 37.127°/40.265°/41.461°.
- **The "tightest-floor-margin grid neighbor" claim is verified, not just
  asserted.** For each crossing I computed the margin at BOTH flanking grid
  points, not just the one the proposal picked: 37.0° margin=3.790× vs
  37.2°'s 2.171× (37.2° correctly chosen); 40.4° margin=3.041× vs 40.2°'s
  1.476× (40.2° correctly chosen); 41.6° margin=3.015× vs 41.4°'s 1.310×
  (41.4° correctly chosen). The proposal's angle selection is honest, not
  cherry-picked toward a comfortable margin.
- **Q3/Q4's interpolation arithmetic reproduces exactly, independently
  reconstructed from `frac_p_abs` primitives** (`frac_p_abs(36.0°)` and
  `frac_p_abs(41.8°)` recovered as `ratio_k × frac_contrast` from
  exp-088's own `retroactive_exp087_reclassification`):
  `frac_p_abs`={36.0°: 1.9655×10⁻³, 38.4°: 1.3041×10⁻³, 38.8°: 5.9552×10⁻³,
  41.8°: 7.2142×10⁻³}. From these: local-trend(37.2°)=1.6348×10⁻³,
  wide-trend(37.2°)=3.0514×10⁻³, wide-trend-predicted(38.4°)=4.1373×10⁻³ vs
  actual 1.3041×10⁻³ → **3.1725×** miss (cited "3.17×"/"3.172×" — exact).
  Smooth-trend(40.2°)=6.5427×10⁻³, smooth-trend(41.4°)=7.0463×10⁻³ (both
  exact matches); naive `ratio_k`(40.2°)=23.11, (41.4°)=28.06 (matches the
  cited "20–28" range and PHOTONICS' "≈23.1"/"≈28.1").
- **`Δθ=3.0° / P*=2.9474° = 1.0178`, i.e. 1.78% over one full established
  period** — confirms EM's "within 1.8% of exact aliasing" exactly.
- **R14(c)'s half-period band and the 1.4° gap's clearance margin
  reproduce exactly**: `[2.84,2.95]/2 = [1.42,1.475]`; `1.42−1.4=0.02`,
  `1.475−1.4=0.075` — confirms the proposal's own "clears by 0.02–0.075°"
  is arithmetically correct (not an error; the concern raised by
  PHOTONICS/EM is about which quantity's period licenses that bound, not
  the arithmetic).
- **The self-contradicting superlative is genuine, independently
  confirmed**: `experiments/088-.../results.json::retroactive_
  exp087_reclassification["38.6"]` shows `floor_pass: false` at margin
  0.386× — 38.6° was sent to real FDTD twice (exp-087, exp-088) at a
  margin **thinner** than 41.4°'s 1.31×. §4's claim that 41.4° is "the
  thinnest margin of any angle this sub-thread has ever sent to FDTD" is
  false as written, two sentences after the same paragraph cites 38.6°'s
  own 0.39×.
- **A new computation this audit adds, not run by any of the five
  critiques**: applying the SAME 3.17× interpolation-bias factor
  QUANTUM's attack invokes (measured at the one point ground truth
  exists, 38.4°) to Q4's own "smooth trend" reference values gives
  bias-corrected null-continuation estimates of **≈2.06×10⁻³ at 40.2°**
  and **≈2.22×10⁻³ at 41.4°** — both of which fall INSIDE, not merely
  near, Q4's own currently-drafted CONFIRM zones (`<3.3×10⁻³`,
  `<3.0×10⁻³`). See §4 below; this sharpens QUANTUM's attack from
  "compatible with a false CONFIRM" to "a bias-corrected null-continuation
  scenario lands inside the CONFIRM band as currently drafted."
- **§4(a)'s attribution re-checked directly against R14's own LOGBOOK
  text**: the parent-curve smoothness/monotonicity finding is credited
  there to "QUANTUM OPTICS' own Phase-5 self-review... re-derived...by Red
  Team's Phase-5 final audit," not to THERMODYNAMICS (whose own R14
  contribution was the `ratio_abs_ext` T9-flatness mechanistic-pathway
  argument — a different finding). exp-089's §4(a) claim that this "mirrors
  THERMODYNAMICS' exp-088 Phase-5 decomposition" misattributes it.

No arithmetic or citation defect was found anywhere in the proposal's own
tables. Every substantive gap below is a framing/calibration/completeness
gap, not a wrong desk number — with one exception (the self-contradicting
superlative, §1) that is a genuine internal inconsistency in the prose.

## 1. PHOTONICS — R14(c) borrows the wrong quantity's period; self-contradicting superlative

**Independently CONFIRMED, both parts.** The wrong-yardstick argument is
sound: `frac_p_abs`'s only directly-measured feature to date (exp-088's
38.4°→38.6° step) shows a 3.07× swing across 0.2° — R14's own founding
LOGBOOK text names this "the numerator hazard," a distinct construction
from `delta_scene`'s smooth ~2.84–2.95° interference fringe. Using the
latter's period as a safety margin for the former's own gaps is an
operand-mismatch in the R9 lineage (same units, wrong quantity), not a
raw arithmetic error — the "clears by 0.02–0.075°" statement is
computed correctly (§0) but licenses less confidence than its phrasing
implies. The "thinnest margin ever sent to FDTD" claim is independently
confirmed **false as written** (§0) — 38.6° at 0.39× predates it by two
cycles. **Adjudication: CONFIRM both. This is the single largest
divergence between what §4 claims and what the record actually
supports**, and I fold it together with EM's independently-derived
version of the same wrong-yardstick point (§3) — genuinely convergent,
not overlapping, findings, exactly as this sub-thread's briefing framed
it.

## 2. MATERIALS — the missing dual-section banner

**Independently CONFIRMED.** Full-text search of `phase1_proposal.md`
finds Idealization 8 (NETD) and the FLOOR/RMS specificity caveat
(exp-088's own Idealization 13, never restated here under any number)
appearing exactly once, in §5 — zero inline occurrence in §6, which is
itself a "committed... predictions" section by the proposal's own §6
header. This is precisely the shape Iteration 65's CHECKPOINT escalated
to a **mandatory** dual-section requirement one cycle ago, for the
express reason that a banner scoped to one section does not propagate to
the other. **Adjudication: CONFIRM. Ruled the single highest-priority
item in this docket — full reasoning in §6.**

## 3. ELECTROMAGNETISM — Nyquist-style bound misapplied; Q4 pairs near-exact aliasing

**Independently CONFIRMED, both parts.** The Nyquist-framing critique is
the same substantive finding as PHOTONICS' §1 (a "half of the
established period" safety bound presumes the guarded quantity is
well-approximated by that period's own fundamental tone — the opposite
of what R14's founding evidence shows for `frac_p_abs`), reached by
independent reasoning; I treat these as one finding, doubly confirmed,
not two. **The aliasing claim is a separate, Q4-specific defect**,
independently verified exactly at §0: `Δθ=3.0°` is 1.78% off one full
`P*=2.9474°` period — close enough that ANY curve carrying meaningful
fundamental-tone power will show apparent "recurrence" at this spacing
regardless of whether the underlying mechanism is genuine
periodicity-inheritance or the still-causally-unattributed domain
artifact this sub-thread has chased for 14+ cycles (LOGBOOK Iteration
64's own T28 record). **Adjudication: CONFIRM both. The aliasing finding
is Q4-specific and compounds, rather than duplicates, QUANTUM's §4
finding below** — one attacks the pair-*spacing*, the other the
threshold *calibration*; a fix to one does not fix the other.

## 4. THERMODYNAMICS — the dropped NETD/T9-anchor extension; the banner gap

**Independently CONFIRMED, both parts.** §7's machinery inventory names
`_load()`/`dg`/`build_article`/`_run_sim`, `box_for`/`ref_for`,
`widths_direction_corrected`, `_label`/`classify_resolved`,
`frac_contrast_of`/`compute_floor` — `thermo_sidecar` appears nowhere,
and §6 (Q1–Q6) has no Q6/Q7-equivalent NETD prediction, even though
`p_abs_w(C40,θ)`/`p_abs_w(G40,θ)` — the exact inputs `netd_disposition`
needs — are already mandatory Phase-4 outputs for `frac_p_abs` itself.
This is a genuine, zero-marginal-cost regression from exp-088's own
established practice. The banner-gap half of this attack is the same
finding as MATERIALS' §2, reached independently — doubly confirmed, one
item in the docket, not two. **Adjudication: CONFIRM both.**

**One correction to THERMODYNAMICS' own "Independent verification
performed" section, not the sharpest attack**: its claim that R14(a)'s
parent-smoothness check is credited to THERMODYNAMICS' own exp-088
Phase-5 decomposition is itself a misattribution — confirmed at §0. The
real R14(a) credit belongs to QUANTUM OPTICS' Phase-5 self-review;
THERMODYNAMICS' own R14 contribution was the `ratio_abs_ext` T9-flatness
mechanistic-pathway argument. Non-blocking (this is a citation-accuracy
slip in the critique document itself, not a claim this cycle's
predictions depend on), but logged per this program's own R4/R9
discipline that a reviewer's own citations get checked, not trusted.

## 5. QUANTUM OPTICS — Q4's REFUTE threshold is calibrated with a proven-biased comparator

**Independently CONFIRMED and STRENGTHENED with new arithmetic (§0).**
QUANTUM's own framing ("the genuinely smooth-continuation case could
still read comfortably below both REFUTE thresholds — a false CONFIRM")
is correct as a qualitative claim. I went one step further: applying the
SAME 3.17× bias factor QUANTUM's own critique measures at 38.4° to the
Q4 reference values (`6.5427×10⁻³`→`≈2.06×10⁻³` at 40.2°;
`7.0463×10⁻³`→`≈2.22×10⁻³` at 41.4°) puts BOTH bias-corrected
null-continuation estimates **inside** Q4's currently-drafted CONFIRM
zones (`<3.3×10⁻³`, `<3.0×10⁻³`), not merely in the ambiguous
"neither-CONFIRM-nor-REFUTE" gap between the two thresholds. This is not
proof the true value WILL land there (the actual FDTD measurement at
Phase 4 could differ from a naive bias-corrected desk estimate for
reasons neither this proposal nor this audit can rule out from the desk)
— but it is proof the CURRENT threshold specification cannot distinguish
"genuine periodicity inheritance" from "ordinary smooth continuation,
corrected for the comparator's own known bias" at either angle, which is
exactly the R5/R10 look-elsewhere failure shape QUANTUM names.
**Adjudication: CONFIRM, and elevate from "recommend a fix before Phase
4" (QUANTUM's own framing) to a mandatory Phase-3 fix (§9) given the
quantified severity.**

## 6. The CHECKPOINT-4-adjacent question — is the missing banner mandatory, and does it fire now?

**Ruling: does NOT currently fire. Mandatory fix for Phase 3, at
material and immediate risk of firing automatically as this sub-thread's
FIFTH disclaimer-erosion instance if unaddressed.**

This is not a novel question — exp-088's own Red Team audit (this
document's own house-calibration reference) faced the structurally
identical situation one cycle ago: a disclaimer-carry gap caught blind,
at Phase 2, before any Phase-3 synthesis existed. That audit ruled
(verbatim): *"Does not currently fire — nothing in this cycle has yet
reached a defended, Phase-3-adopted state; every gap identified... was
caught blind, at Phase 2, before any Phase-3 synthesis exists — this
program's own established non-firing shape."* Every one of R6 through
R14's own adoption texts, and both prior CHECKPOINT entries this
sub-thread has fired (Iterations 61, 65), fire on a defect that reached
Phase 3 (a defended, adopted claim) or Phase 5/NOTES.md (the frozen
record) — never on a Phase-1-draft gap caught by blind Phase-2 review
before Phase 3 exists. Applying that same, already-established
distinction here: exp-089's `phase1_proposal.md` is a Phase-1 document,
now under Phase-2 review; nothing has reached Phase 3 yet.

**But the stakes are higher than exp-088's own precedent instance,
for two compounding reasons, and I rule the fix mandatory rather than
merely recommended:**

1. Iteration 65's own CHECKPOINT escalated the banner from a Phase-2
   recommendation (exp-088's own audit, §5, explicitly declined to make
   it blocking) to a **mandatory** dual-section requirement, precisely
   because three individually-fixed instances had already demonstrated
   that per-cycle manual vigilance does not reliably prevent recurrence.
   exp-089 is the very next cycle this mandatory rule applies to, and its
   own first draft already violates it — direct, immediate evidence the
   mandatory rule alone (without a Phase-3 gate actually enforcing it)
   is not self-executing.
2. Iteration 65's own CHECKPOINT text used unconditional language for
   the fourth instance ("fires... automatically... no discharge clause
   attached") specifically because a defect "fixed just in time" three
   cycles running was ruled not reliably preventable by per-cycle
   vigilance. A fifth occurrence — even one caught blind at Phase 2,
   which would ordinarily discharge it under the R6–R13 pattern — sits
   uncomfortably close to the same "known, named, ignored" territory
   R6–R13's own lineage exists to escalate against, one cycle after the
   rule was made mandatory specifically to stop it.

**Ruling, precisely stated**: Checkpoint criterion 4 does not fire on
this cycle *as currently drafted at Phase 2* — matching exp-088's own
precedent for an identical-shape gap at an identical stage. It is
**mandatory, not optional, that Phase 3 add the dual-section banner
before `phase1_proposal.md`/its Phase-3 synthesis is treated as frozen**
(fix docket item 1, §9). If this cycle reaches Phase 3 or NOTES.md
without it, that would be the fifth instance of the shape, reaching
Phase 3 with the fix available and named in writing beforehand by three
independent parties (MATERIALS, THERMODYNAMICS, this audit) — a
materially worse case than any of the first four instances, none of
which had a *mandatory*, previously-adopted, cycle-specific rule already
on the books naming the exact fix. I would expect a Director who lets
that happen to find no room for a "caught blind, same cycle" discharge
argument, and no basis to treat it as a discretionary weighing call.

## 7. New attack, not raised by any of the five critiques

### 7.1 — Q4's false-CONFIRM risk compounds specifically at the cycle's own named highest-stakes outcome **[inconsistency-risk]**

§6 states plainly that a miss at 40.2°/41.4° (`ratio_k>10`) is "the
single most consequential possible outcome of this cycle." Q4 is offered
as an "independent, cheaper discriminator" whose CONFIRM is predicted to
"correlate with the Q3 CONSISTENT lean holding." §5's own arithmetic
(strengthened at §0) shows Q4's CONFIRM zone can be reached by a
bias-corrected null with no real periodicity. If Phase 4 produces a real
`ratio_k(40.2°)` or `ratio_k(41.4°)` reading near or above 10 (the
consequential, ENERGY-DOMINANT-leaning outcome) at the SAME angle where
Q4 also reads CONFIRM (plausible precisely because Q4's CONFIRM zone is
under-discriminating), a future NOTES.md drafted under the normal
pressure to narrate a coherent story could read Q4's spurious CONFIRM as
reassuring corroborating context beside a genuinely alarming Q3 finding —
manufacturing exactly the kind of muddled, disclaimer-adjacent narrative
this sub-thread's four prior erosion instances all share the shape of.
**Recommend, mandatory**: whichever Q4 fix Phase 3 adopts (§9 item 4),
state explicitly, in the same paragraph as any future Q3 ENERGY-DOMINANT
finding, that Q4's own CONFIRM/REFUTE reading (however computed) is not
evidence bearing on whether Q3's finding itself is a real physical
effect or an artifact — the two questions are logically independent and
must not be allowed to read as mutually corroborating in prose.

## 8. Do any two critiques conflict?

**No.** All five attack disjoint, complementary axes: PHOTONICS
(R14(c)'s wrong-yardstick + a false superlative), MATERIALS (the banner
gap, FLOOR/RMS half), ELECTROMAGNETISM (the same wrong-yardstick
argument by independent reasoning + Q4's aliasing), THERMODYNAMICS (the
dropped NETD/T9-anchor extension + the banner gap, NETD half),
QUANTUM OPTICS (Q4's biased threshold calibration). PHOTONICS/EM converge
on one finding (§1/§3) and MATERIALS/THERMODYNAMICS converge on another
(§2/§4) — genuine convergence, not restatement, since each pair reaches
its shared conclusion from a different discipline's own reasoning, and I
confirm none of the five numeric claims disagrees with any other or with
§0's own from-scratch recomputation.

## 9. Checkpoint criterion 4 — explicit ruling

**Does not currently fire.** See §6 for full reasoning. Nothing in this
cycle has reached a defended, Phase-3-adopted state; the banner gap was
caught blind, at Phase 2, before any Phase-3 synthesis exists — this
program's own established non-firing shape, applied here identically to
exp-088's own precedent one cycle ago.

**At material, immediate, and elevated risk of firing automatically** —
more elevated than exp-088's own precedent instance, because the rule
this cycle violates is the mandatory dual-section banner Iteration 65
itself adopted specifically to stop this exact recurrence, one cycle
after it was adopted. Adopting fix docket item 1 (§10) before Phase 3 is
treated as frozen is the only action that keeps this from becoming the
fifth instance of a shape this sub-thread's own record shows is not
reliably prevented by per-cycle vigilance alone.

No other Checkpoint criterion (1/2/3/5) is implicated: T28 instrument
work, criterion 2 explicitly N/A matching every T28 desk/instrument cycle
since exp-069; no constraint metric is passed or approached (criterion 1
N/A); no engine-physics build needed (criterion 3 N/A); this is a cheap,
well-targeted, logbook-advancing follow-up, not a stalled cycle
(criterion 5 N/A). Constraint-#N-violation tags do not apply to any
attack in this audit for the same reason — this is instrument-fidelity
work on T28's own energy-interception channel, not a phenomenon-mechanism
proposal.

## 10. Ruling: PROCEED-WITH-MANDATORY-FIXES

**Q4 verdict, stated explicitly per the task's own question**: Q4 is
**not salvageable as specified** for any CONFIRM/REFUTE labeled verdict —
its reference thresholds are calibrated with a comparator this same
document's own Q3 section proves biased by 3.17× in exactly the direction
that manufactures a false CONFIRM (§5), and its recurrence-pair spacing
sits within 1.8% of exact aliasing against the established period (§3),
an independent defect that would remain even if the threshold
calibration were fixed. It does **not** need a structural redesign — the
underlying idea (compare a new angle's `frac_p_abs` against a
same-period-offset partner, at zero additional machinery) is sound and
cheap. It needs its **calibration** fixed before Phase 4 computes it:
either rebase both CONFIRM and REFUTE references against the measured
3.17× bias correction (giving `≈2.06×10⁻³`/`≈2.22×10⁻³` as the true
null-continuation estimates, §5) and add a non-aliased control angle
(EM's fix, in-budget at 16 total calls, still inside Red Team's own
Iteration-65 authorized "~8–16" range... at the top of it), or — cheaper
and more conservative — drop the CONFIRM/REFUTE verdict language
entirely and report `frac_p_abs(40.2°)`/`frac_p_abs(41.4°)` as raw
numbers only, explicitly not a periodicity-inheritance finding, pending
the still-queued formal fit (Idealization 12/R14(b)). Phase 3 must choose
one of these two paths — leaving Q4 as currently drafted is not an
option.

Fix docket for Phase 3 to adopt or explicitly override with reasons
(9 items; 1, 2, 4 are blocking; the rest are recommended, mostly
zero-marginal-cost, closures):

1. **[BLOCKING]** Add an explicit "carried idealizations" banner inline
   at the top of §6, before any Phase-3 synthesis or the eventual
   NOTES.md treats this cycle's predictions as frozen — per the mandatory
   dual-section rule Iteration 65's CHECKPOINT adopted. Name explicitly,
   by number: Idealization 2 (λ unchanged), Idealization 7 (`FLOOR_FRAC`
   house-style), Idealization 8 (NETD — restated inline, not merely
   cross-referenced, at every Q1/Q3/Q4/Q5/Q6 restatement of a
   classification), Idealization 11 (R14(c)'s residual open span — see
   item 3), and a restated exp-088 Idealization-13-equivalent (FLOOR/RMS
   material-and-wavelength specificity). The same banner must also open
   the eventual Result section once Phase 4 runs, matching the exact
   standard exp-088 was held to (§6/§9).
2. **[BLOCKING]** Correct §4's "41.4° (1.31×) is the thinnest margin of
   any angle this sub-thread has ever sent to FDTD" — false as written;
   38.6° (0.39×, sent twice) is thinner. Restate scoped to
   floor-*clearing* angles specifically, or drop the superlative (§0, §1).
3. **[BLOCKING]** Do not let Q6 or any future prose treat the 1.4° gap
   (38.8°→40.2°) as adequately protected by R14(c)'s bound. State
   explicitly, alongside Q6, that this gap is not protected against a
   feature at `frac_p_abs`'s own demonstrated (sub-0.4°) native scale —
   the only directly-measured evidence of that quantity's own periodicity
   to date argues the reverse of what the borrowed `delta_scene` yardstick
   implies (§1, §3).
4. **[BLOCKING]** Fix Q4's calibration before its output is treated as
   any kind of directional signal: either rebase the CONFIRM/REFUTE
   reference values against the 3.17× bias correction AND disclose the
   Δθ=3.0° aliasing risk explicitly, or drop the CONFIRM/REFUTE labels
   entirely and report raw numbers only (§5, §10). Whichever is chosen,
   add the §7.1 disclaimer decoupling Q4's own reading from any Q3
   ENERGY-DOMINANT finding at the same angle.
5. **[Recommended, zero marginal FDTD cost]** Add the NETD/T9-anchor
   extension (`p_abs_w`→`mixed_length_scale_regime`→`netd_disposition`,
   `ratio_abs_ext` vs the 0.51 T9 anchor) at all three new angles,
   mirroring exp-088's own Q6/Q7 (§4).
6. **[Recommended, minor]** Correct §4(a)'s attribution — the
   parent-curve smoothness finding is QUANTUM OPTICS' Phase-5
   self-review, not THERMODYNAMICS' own decomposition (§0, §4).
7. **[Recommended, in-budget]** If path (a) of item 4 is chosen, add one
   Q4 control angle at a non-period-aliased offset (Δθ≈1.5° from 37.2° or
   38.4°) — 4 more calls, 16 total, still inside the authorized "~8–16"
   range (§10).
8. **[Recommended, zero cost]** Give R14(a)'s "individually smooth/
   monotonic" check a concrete, code-executable criterion and a stated
   owner (Phase 4/`run.py` vs Phase-5 prose) (THERMODYNAMICS' secondary
   finding).
9. **[Recommended, house discipline]** Re-verify Idealization 13's
   `back_frac`/`fwd_frac` "not read anywhere" claim by grep against the
   actual committed `run.py` once it exists, rather than carrying it
   forward as an inherited assumption about not-yet-written code
   (QUANTUM's secondary note).

Zero items are overridden.

## 11. Summary

**Ruling: PROCEED-WITH-MANDATORY-FIXES.** All five blind Phase-2
critiques are substantively correct on their sharpest attacks, all
independently re-derived from primitives and confirmed exact (§0). No
two conflict; two genuine convergent pairs (§1/§3, §2/§4) strengthen
rather than duplicate each other. The FDTD plan itself (12 calls, reused
validated machinery, correct grid indices, honestly-disclosed thin
margins) is sound and cheap — nothing here blocks running it once the
fix docket lands. The missing dual-section banner (§2/§4/§6) does **not**
currently fire Checkpoint criterion 4, on the same non-firing precedent
exp-088's own audit established one cycle ago for an identical-shape,
identical-stage gap — but it is now a **mandatory**, not merely
recommended, Phase-3 fix, and the single highest-priority item in this
docket, because the rule it violates is the very rule adopted to stop
this shape recurring a fifth time. Q4 (§5, §10) is not salvageable as
currently specified for a labeled CONFIRM/REFUTE verdict — its
comparator is proven biased in the false-CONFIRM direction by this same
document's own Q3 arithmetic, and its pair-spacing sits within 1.8% of
exact aliasing — but the underlying measurement is cheap and sound, and
either of two named fixes (bias-correct the thresholds, or drop the
labels) closes the gap at Phase 3 without touching the frozen 12-call
FDTD budget.
