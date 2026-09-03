# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 84 (exp-107)

*Blind to all other Phase-5 seats, per PANEL.md's isolation discipline.
Charter: sub-wavelength structure realizability; owns the
published/plausible/unobtainium-with-parameters bound.*

## Item 1 — the Tier 0 retirement decision

### Steel-man

The Synthesis's own operative retirement clause is faithful to my memo.
`disposition_memo.md`'s ceiling claim is scoped, textually, to
**realizability**: *"Under NO branch of this memo's own per-outcome
conditional does a genuine new realizability question ever open."*
The Synthesis's actual retirement paragraph quotes and uses exactly that
scope — "a future proposal that identifies a **live realizability
question** genuinely depending on which family is correct would reopen
it" — and separately, correctly, carves out that this does **not**
foreclose T28's own larger mechanism question or any other standing T28
item. That is the right shape: narrow the closure to what the cited
authority actually proves, name the live thing it doesn't touch. Red
Team's own independent re-read of the memo (audit §0.5) reproduces my
exhaustive three-branch argument verbatim and correctly notes no branch
of the *census's own* outcome table (R3-CORROBORATED / R4-CORROBORATED /
NEITHER) escapes it. On its own terms, this is a clean, citable,
zero-cost retirement — exactly what I argued for in my own Phase-2
critique.

### Sharpest attack

The retirement text is faithful **at the Synthesis clause**, but NOTES.md
does not stay inside that scope throughout. Its own Hypothesis section
states: *"MATERIALS' own founding disposition memo (exp-100) already
proves no outcome of the question can ever change a realizability tier
or a constraint-1/2/3/4 verdict."* That second clause is not something my
memo proves, or discusses at all — `disposition_memo.md` never mentions
constraints 1–4; its entire content is the three-branch realizability
argument. The constraint-3 immunity claim comes from a *different*
seat's *different* argument (VISION's Phase-1 §1 sub-threshold framing),
and that argument was independently shown, same cycle, to be built on a
citation defect corrected from "0.08–0.12×" to **63.0%** of `C_thr_lab`
(Red Team §0.4, PHOTONICS' catch, exact reproduction:
`3.1495e-3/0.005=0.6299`). 63% is not saturated the way 8–12% is — it is
close enough to the bar that a future amplitude refinement, a different
θ, or a superposed-signal geometry could plausibly cross it, at which
point which family gives the correct `delta_scene` reading **would**
bear on a constraint-3 verdict. Attributing that live possibility's
closure to my memo, which never addresses it, overclaims my own seat's
authority to close a question outside my charter.

This surfaces the actual loophole in the stated reopening condition. The
single named trigger — "a live realizability question... depending on
which family is correct" — only covers **my** charter. It does not cover
a live *constraint-3/perceptual-scoring* dependency, which is the
concrete, non-hypothetical way this question could someday matter again
(63% is not a comfortable margin). The retirement's own careful
"does not foreclose the mechanism question" carve-out shows the authors
knew to scope this precisely for PHOTONICS' domain; the identical
discipline was not applied for VISION's. As written, a future cycle that
finds `delta_scene` amplitude pushing past `C_thr` under some
not-yet-tried configuration has no textually clean trigger to cite for
reopening — it would have to notice the gap and argue by analogy, not
invoke the stated condition directly.

### Verdict on Item 1: **CONFIRM-WITH-GAPS**

The retirement itself is sound and the right call — I would make the
identical call again with the same information, and the operative
Synthesis clause correctly represents my memo's own conditional, not
loosely. The gap is scope-creep in the surrounding prose (Hypothesis
section) attributing a constraint-1/2/3/4 closure to my memo that it
does not make, and a reopening condition narrower than the full set of
ways this question could legitimately resurface (realizability-only,
when constraint-3 dependency is the more plausible live trigger given a
63%-of-bar margin, not the 8–12% the proposal originally, wrongly,
believed). Neither gap changes the retirement decision; both should be
corrected in the permanent record so a future cycle does not cite "no
outcome ever changes a constraint-1/2/3/4 verdict" as if my memo said
that.

## Item 2 — the hollow-vs-PEC-cored delta at higher R_CORE/R_COAT

### Steel-man

Item 1 is legitimately scoped and correctly executed. My own Phase-2
critique already established that the rising `R_CORE/R_COAT` ratio
(0.692/0.846) is a pure consequence of the fixed-abs family's core
*growing* while the coating holds a fixed 48-cell/1.44µm absolute
thickness — it is not a claim about a thinner or differently-realizable
coating, so it cannot, on its own, extrapolate past
`REALIZABILITY_MEMO.md` AMENDMENT 6/7's thickness bound (a real
metamaterial graded-absorptive coating can in principle be wrapped
around a core of any size). Gate P0 passed exactly; the instrument
(`sections.radial_absorbed_power`/`widths()`) is already suite-gated
(stage 10); `core_frac` (8.65×10⁻⁷ at r=156, 2.88×10⁻⁷ at r=312) is
exactly the near-zero reading the graded shell's own r<R_CORE-untouched
construction predicts, since σ(r)=0 inside the hollow core by
construction regardless of what test is run. Both deltas
(2.97×10⁻⁵/2.47×10⁻⁵) clear the 10× falsification margin comfortably —
Red Team's founding Attack 9 concern (core-reflection leakage) is
discharged at the order-of-magnitude level the falsification band was
built to test. Nothing here should move my realizability bound: that
bound concerns whether the graded-absorptive *coating structure itself*
is fabricable at the required thickness, which this test does not touch
either way.

### Sharpest attack

Three things, from my own discipline, that NOTES.md's "roughly an order
of magnitude above the original T9 anchors" framing smooths over.

**(a) The delta does not grow with ratio in the data actually collected —
it is flat-to-mildly-declining.** `|Δ|=2.969×10⁻⁵` at ratio 0.692 (r=156)
vs. `|Δ|=2.468×10⁻⁵` at ratio 0.846 (r=312) — both negative-signed
(`delta_abs_ext_ratio` is negative at both r, i.e. hollow's
`abs_ext_ratio` sits consistently *below* the PEC-cored comparator), and
the *magnitude* is smaller at the higher ratio, not larger. A genuine
near-field/cavity-resonance-scaling-with-core-size story would predict
monotonic growth with ratio (a bigger vacuum cavity has more room to
support internal modes); what two points show instead is a step-like
jump between T9's original anchor ratio (0.385, `Δ`≈1.56×10⁻⁶–6.8×10⁻⁶)
and this cycle's much higher ratios (0.692/0.846, `Δ`≈2.5–3.0×10⁻⁵),
then something closer to flat (or a small counter-trend) between the two
new points. Two points cannot distinguish "flat once past some
threshold ratio," "genuinely non-monotonic," or "the step itself is
noise, not physics" — the question the task poses ("does a delta
*growing with* R_CORE/R_COAT change your reasoning") is not quite what
the data shows, and NOTES.md's own text does not flag this directly
(it reports both numbers correctly but never states the direction of
change between them).

**(b) The box-ledger channel's own absolute-noise-floor gap — flagged
once at this program's founding instance (T9, Iteration 4, exp-027) and
never closed — is *more* exposed here than it has ever been.** T9's
original caveat: `box_dev≈0.0019` was `≈1221×` larger than the measured
delta, "informally decisive" but never formally floor-gated. Here:
`box_dev(156)=0.000708` vs. `|Δ|=2.969×10⁻⁵` → ratio **23.8×**;
`box_dev(312)=0.000222` vs. `|Δ|=2.468×10⁻⁵` → ratio **9.0×**. At r=312
specifically, the historical 1221× margin has shrunk to under one order
of magnitude. `box_dev` itself is only a box-to-box *self-consistency*
check (same run, two collection boxes) — it is not an absolute noise
floor, and `delta_abs_ext_ratio` additionally combines two
*independently-run* simulations (this cycle's hollow capture and
exp-106's own separately-executed PEC-cored capture), so the true
uncertainty budget on the delta itself is unmeasured and plausibly
larger than `box_dev` alone suggests once independent-run noise is
included. With the margin this thin at r=312, I cannot distinguish "the
delta shrank because of ratio-dependent physics" from "the delta moved
within an uncharacterized noise floor" — and NOTES.md's own "PASS at the
loose band, not a tight reproduction" language does not surface that the
margin against the *relevant* self-consistency check has itself
degraded by two orders of magnitude relative to the founding instance.
This is the correct next instrument, not a re-derived confirms band
alone (see Iteration-85 recommendation, below).

**(c) `core_frac`≈10⁻⁷ answers a narrower question than "does core
presence matter physically."** It measures local Joule dissipation
*inside* r<R_CORE — which is trivially ≈0 for a hollow core regardless
of any interior electromagnetic behavior, because `σ(r)=0` there by
construction; it cannot register energy *stored* rather than
*dissipated* (a resonant or whispering-gallery-type field buildup in the
vacuum cavity would show zero local heating while still perturbing the
far-field-derived `sigma_ext`/`sigma_abs` split this test actually relies
on to detect anything at all). The real physical question a
sub-wavelength-structure perspective raises is not "does the core
absorb power" (already answered, trivially, by construction) but
"does the vacuum-vs-PEC interior boundary condition set up a standing-
wave/interference pattern with the shell's own graded σ(r) profile — which
peaks immediately at r=R_CORE, not at r=R_COAT — that shows up in the
*angular* distribution of scattered power rather than the aggregate
radial ledger?" `sections.radial_absorbed_power`/`widths()` is a bulk,
angle-integrated instrument; it cannot see this even in principle. The
already-built, already-validated `lab/sections.py::
angular_scattered_pattern` (used for exactly this purpose at exp-059/060,
Iteration 37, to separate shape/edge-diffraction effects from bulk-loss
effects) is the correctly-targeted instrument for this specific
question, and it was not run here — a real gap, not a hypothetical one,
given this program has already built and validated the tool this
question calls for on a structurally analogous PEC-core-vs-uniform-disk
question two years of program-time ago.

None of (a)–(c) moves my realizability bound: the coating's absolute
thickness is unaffected by any of this, so `REALIZABILITY_MEMO.md`
AMENDMENT 6/7 stands exactly as before. What (a)–(c) *do* affect is
confidence in `sections.radial_absorbed_power`/`widths()` as a clean
precondition-validation instrument for OTHER seats' P3/shape-ratio work
at these higher ratios — an instrument-trust finding, not a
materials-realizability one, and I flag it as such rather than
overreach my own charter the way I found NOTES.md's Hypothesis section
doing above.

### Verdict on Item 2: **CONFIRM-WITH-GAPS**

`item1_pass=True` at both r is correct on its own falsification-band
terms, and Attack 9 is genuinely discharged at the order-of-magnitude
level the band was built to test. But "roughly an order of magnitude
above the original T9 anchors, same qualitative conclusion" reads as a
settled generalization when the actual two-point record shows a
step-then-flat(or-declining) pattern with a shrinking, uncharacterized
self-consistency margin at the larger r — a genuinely different, more
fragile evidentiary shape than the PASS band alone conveys, and one
this document does not name.

## Overall verdict: **CONFIRM-WITH-GAPS**

Both scored decisions (the Tier 0 retirement itself; Item 1's PASS
classification) are correct calls that I would not reverse. The gaps are
in the surrounding prose overclaiming what my own memo settles
(Hypothesis section, Item 1) and in a falsification-band framing that
reports the right numbers but not the right shape of the evidence
(flat/declining-not-growing delta; a shrinking self-consistency margin;
a bulk instrument standing in for a question about angular/near-field
structure) (Item 2).

## The single most important thing for Iteration 85, from this discipline

Run `lab/sections.py::angular_scattered_pattern` on the hollow-vs-
PEC-cored fixed-abs pair at r=156 and r=312 (the same two captures this
cycle already has, or cheap re-captures if raw fields were not
persisted) — the correctly-targeted instrument for "does the interior
boundary condition imprint a distinguishable signature," reusing this
program's own exp-059/060 precedent rather than inferring an absence of
near-field coupling from a bulk ledger that cannot see it by
construction. Pair this with a genuine absolute (not merely box-to-box)
noise-floor characterization for the `sections.widths()` box-ledger
channel — T9's own Iteration-4 caveat, open for over eighty cycles, and
now more exposed than at its founding (9× margin at r=312 vs. the
historical 1221×) — before either the "confirms" band is re-derived
(NOTES.md's own Next item 2) or any future cycle treats a small
cross-family `abs_ext_ratio` delta at these ratios as decisively small
again.
