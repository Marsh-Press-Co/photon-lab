# Phase 5 Review — VISION SCIENCE seat (Panel Iteration 79, exp-102)

Fresh sub-agent. Blind and parallel — no access to any other seat's Phase-5
review this cycle. Read `PANEL.md`, `LOGBOOK.md` in full (RULED OUT,
ESTABLISHED, LIVE THREADS, and the Iteration 76-78 narrative including the
R20 firing at exp-101/Iteration 78), `phase1_proposal.md`, all five
`phase2_critique_*.md`, `phase2_redteam_audit.md`, `NOTES.md`, and
`results.json` directly.

## 1. Did my own two Phase-2 mandatory fixes land correctly?

**Fix 5 (perceptual-overclaim wording, §4/Idealizations) — LANDED
CORRECTLY.** My Phase-2 attack targeted: *"κ(θ) alone answers 'is this
point dark relative to what would be there with nothing in the way,'
**which is constraint 1's witness question**."* `NOTES.md`'s Idealizations
now reads: *"No perceptual/Weber-contrast scoring this cycle... per fix 5,
this is constraint 1's **physical** transmission question only, a
necessary but not sufficient input to the witness's actual percept."*
(NOTES.md, Idealizations, ~line 267-270) — essentially my own proposed
replacement text verbatim. I re-scanned the rest of the document (Setup,
Result, Learned, Next) for any residual instance of the struck phrase: the
Hypothesis section does use "constraint 1's witness question" once, but in
a different, non-overclaiming sense — paraphrasing *exp-101's own* finding
that `sigma_scat_downstream` "is interpretable but structurally cannot
answer constraint 1's witness question," which is PANEL.md's own literal
constraint-1 wording ("does the background stay lit"), a physical
question by the phenomenon spec itself, not a claim that κ(θ) resolves the
percept. That usage is fine and does not need the fix. **Verdict: fix 5
landed correctly, everywhere it matters.**

**Fix 6 ("T3" mislabel strike) — LANDED CORRECTLY.** My Phase-2 flag: the
Phase-1 draft's Idealizations re-cited "the T3 build" for the still-unbuilt
Tier-2 conversion, reintroducing a label exp-101's own Phase-5 correction
had explicitly dropped. `NOTES.md`'s Idealizations now reads: *"That
conversion (constraint 1's own missing conversion, exp-101's Next item —
**no thread number assigned; NOT T3, per fix 6**) is future work, out of
scope here"* — and Next item 4 repeats the same clean framing: *"The
Tier-2 perceptual conversion (constraint 1's own missing conversion from
this cycle's raw κ(θ)/I_abs(θ) to a witness-perceived C_thr(L) judgment) —
still unbuilt, per fix 5/6's corrected scoping."* I grepped the full
document for "T3" and found it only in the "Changes from Phase 1" section
narrating the fix itself (correctly, as history) — zero live recurrences
in Setup/Result/Learned/Next. **Verdict: fix 6 landed correctly, and does
not recur anywhere in the new Result/Learned/Next material.**

Both fixes: **confirmed landed, no residual mislabeled thread reference
anywhere in the document.**

## 2. New perceptual overclaim scan (Result/Learned/Next — unseen material)

No new overclaim found. Specifically:

- Result's κ(θ) description: *"a genuine, spatially-localized on-axis
  darkening"* — physical language throughout, correctly paired with the
  realizability caveat (fix 7) inline. No adaptation state, ambient level,
  or C_thr(L) comparison is invoked.
- Learned item 1: *"a genuine, spatially-localized on-axis darkening of
  κ~0.4–0.7%... This closes exp-101's own Next item 1 as a working
  instrument, not merely a proposal"* — scoped as an instrument-capability
  claim, not a visibility claim. Correct.
- κ_off(θ) > 1 (1.041-1.077, "mildly BRIGHTER than the empty scene") is
  explained as *"light scattered/diffracted away from the shadow's own
  axis"* — a physical, not perceptual, reading. No implication that a
  witness would "see" this brightening (it would not clear any C_thr(L) on
  its own, and the text does not claim it would).
- Next item 4 explicitly scopes the still-unbuilt Tier-2 conversion as the
  place any such claim would eventually be earned.

**Clean.** Neither Result nor Learned nor Next smuggles a visibility or
perceptibility conclusion this cycle.

## 3. Independent numeric verification against `results.json` — a genuine
## finding

I recomputed the on-axis κ(θ) range directly from `results.json`'s
`predictions.p1_on_axis_kappa.cells` (the actual scored 12-cell pool):

```
min = 0.003479968184461652   (C40_R4@41.460901)
max = 0.007289772019643874   (C40_R4@42.960901)
```

**`NOTES.md`'s Result section states the range as `3.68×10⁻³`–`7.29×10⁻³`.
The maximum is correct; the stated minimum (3.68×10⁻³) is NOT the true
minimum.** The true minimum is `3.48×10⁻³` (C40_R4@41.460901) — the value
`3.68×10⁻³` is a real data point (C40_R4@38.59023) but the *second*-smallest
of the twelve, not the floor of the range. I checked whether some
plausible subsetting (C40_R4-only, G40_R4-only) legitimately produces
3.68×10⁻³ as a floor — it does not: C40_R4's own minimum is the same
3.48×10⁻³ point, and G40_R4's minimum is a third, different value
(3.82×10⁻³). This is a genuine, independently-reproducible restatement
error, not a rounding artifact or a defensible alternate reading.

**This propagates into Learned item 1's rounded headline, "κ~0.4–0.7%."**
The true minimum, 0.348%, rounds to ~0.3% under the same one-decimal
convention the "0.7%" ceiling already uses (0.729%→0.7%) — the stated
floor should read "~0.3–0.7%." The Learned figure was evidently derived
from the Result section's own (incorrect) 3.68×10⁻³ floor, not
independently re-checked against the raw 12-cell pool — one root cause
manifesting in two places, not two independent errors.

**Materiality**: does not change any scored verdict — Prediction 1's
falsification band was `[0, 0.10]` and both the true and the stated
minimum sit far inside it; this is a range-citation defect, not a
pass/fail error. But it is squarely the **R4/R20-shaped defect class**
this cycle's own predecessor (exp-101) fired Checkpoint criterion 4 on
one cycle ago: a range figure in Result that does not reproduce from the
underlying data, caught only at Phase 5, in the exact document that
otherwise disclosed its own defects (Gate B's failure, the Gate-C sign
bug) with unusual rigor. I found no other Result/Learned numeric claim
that fails to reproduce (κ_off range 1.041-1.077 ✓, point-vs-region ratio
range 1.23-1.56× ✓, Δφ range +0.21 to +0.59 rad — recomputed as
+0.2092 to +0.5871 rad ✓, Gate D's 48.95%/8.24% perturbation deltas ✓, all
against `results.json` directly). **This is one isolated instance found
so far from my seat's own check** — whether it combines with defects other
seats may independently find to approach R20's "three or more" bar is a
question for Red Team's Phase-5 audit, which has cross-seat visibility I
do not.

## 4. Citation/restatement defect flag (R4/R20 lineage) — summary for Red
## Team

- **New defect (§3 above)**: on-axis κ(θ) range floor misstated in Result
  (3.68×10⁻³ cited vs. true 3.48×10⁻³), propagating into Learned's rounded
  "0.4-0.7%" headline. Non-load-bearing (verdict unaffected), but a
  genuine restatement error in Result/Learned — the section R20 is scoped
  to.
- **"T3" mislabel**: does NOT recur anywhere in Result/Learned/Next this
  cycle (§1 above) — the Phase-2 catch held through Phase 3/4 cleanly.
- No other citation of a prior experiment's figure (exp-001's 1.5-1.8%,
  exp-101's `Q_ext`≈1.54-1.56, `REALIZABILITY_MEMO.md` Amendments 6-7) was
  found altered or drifted from its source in this document.

## 5. Verdict on the cycle's Combined Verdict candidate

**CONFIRM-WITH-GAPS.** The instrument build is real, honestly self-audited,
and substantively advances my seat's own future work (Tier 2 needs exactly
this κ(θ)/I_abs(θ) physical-transmission quantity as its input, and it now
exists, correctly scoped as non-perceptual). Both of my Phase-2 mandatory
fixes landed cleanly and do not recur. Set against that: (a) Gate B — the
one gate meant to independently cross-validate this new channel against
already-trusted physics — genuinely FAILED and is disclosed as such, so the
primary channel currently rests on an internal identity gate (A) and a
fault-injection control (D) alone, not an independent old-instrument
cross-check; (b) I independently found one new, real, R4/R20-shaped
range-citation defect in Result/Learned (§3) that this cycle's own
five-critique-plus-Red-Team Phase-2 layer could not have caught (it
postdates the run) and that the document's own Phase-4/5 self-audit did
not catch either. Neither gap changes a scored verdict, and the instrument
itself is sound — but "CONFIRM" outright would understate that this cycle
produced its own next-cycle homework (Gate B's proper fix, already
correctly deferred to Next item 1) and its own fresh citation-hygiene
instance, on the heels of a cycle that fired Checkpoint criterion 4 for
exactly this defect class.

## 6. Ranked top-3 candidate directions for Iteration 80 (Vision Science
## lens)

1. **The Tier-2 perceptual conversion (Next item 4) — ripe to START, but
   NOT ripe to score against C_thr(L) without first routing through T8.**
   A working κ(θ)/I_abs(θ) instrument is a genuine, necessary precondition
   my charter has been waiting for — but it measures at `D_STANDOFF`=200
   cells, deep in the shadow's near/Rayleigh zone (T8: z/z_R≈0.04-0.06),
   and this cycle's own Gate B failure is direct, fresh evidence that the
   shadow's measured depth is standoff-dependent even within the near
   zone (Fresnel fill-in, Learned item 2). Feeding today's near-field κ
   directly into T2's frozen `C_thr(L) = 0.005·max[1,(L/3)^-p]` bar without
   first passing it through T8's own r=78/156/312 standoff-bridge family
   would score a witness-perceptibility verdict at the wrong physical
   distance — precisely the kind of premature threshold-scoring my
   charter exists to block. Rank #1 as: build the bridge-family
   application of THIS instrument first (cheap — no new machinery, same
   `κ(θ)` code at r=78/156/312), THEN attach `C_thr(L)`/adaptation state
   to the resulting extrapolated-to-witness-scale figure, not to today's
   raw bench number.
2. **A properly-scoped Gate B (Next item 1)**, matched to the established
   `beam_behind` window's own spatial footprint. Until this exists, the
   new channel's only cross-validation against known-good physics is
   negative (a documented failure), which matters directly to my seat:
   any future perceptual scoring inherits whatever trust level this
   instrument carries, and right now that trust rests on self-consistency
   (Gates A/D) rather than an independent old-instrument agreement.
3. **Tier 1's own R3-vs-R4 `delta_scene` split** (PHOTONICS' zero-FDTD
   check first) — the standing, unchanged queue item from exp-100/101,
   outside my domain's direct stake but still the program's other
   committed thread; no vision-specific objection to its continued
   deferral.

## RULED OUT / Live Thread re-tread check (own domain)

No RULED OUT item (R1-R21) is re-litigated from a vision-science angle in
`NOTES.md`. T2 (perceptual thresholds) is correctly left untouched/
un-invoked this cycle (no C_thr(L) scoring occurs, matching the
Idealizations' own explicit scope). T3 (temporal-contrast/switching, still
unclosed per T19) is correctly never touched by this static, single-
snapshot instrument, and is not conflated with the Tier-2 conversion
anywhere in the final document (§1 above). T8's near-field caveat is
disclosed, not resolved, and this cycle's own Gate-B failure is fresh,
concrete evidence of exactly the effect T8 warns about — good, load-bearing
consistency, not a re-tread.
