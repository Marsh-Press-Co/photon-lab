# Phase-5 Review — PHOTONICS seat, Panel Iteration 78 (exp-101)

Fresh sub-agent, independent pass over the FINISHED cycle (proposal, all
five Phase-2 critiques, Red Team's Phase-2 audit, NOTES.md, `run.py`,
`results.json`, `run_output.txt`). This is not a restatement of my own
Phase-2 critique (`phase2_critique_photonics.md`) — that document is read
here only as background; every numeric claim below was independently
recomputed against `results.json` and `lab/sections.py` this session.

## Verdict

**The Tier-0 deliverable is sound and should stand: the closed four-face
box genuinely fixes `beam_behind_t28`'s total-conservation problem, all six
Red-Team-mandated fixes were implemented in code (not just asserted), and
the trust/registration/margin gates are real, executed checks that
passed.** But this cycle's own headline "Result"/"Learned" claims about
`back_frac`'s angular trend, and its explanation of Prediction 3's
falsification, both stop one step short of the correct optical
diagnosis — and the missed step is squarely inside this seat's charter
(angular dependence of scattering). **No prior document in this cycle's
record (proposal, five critiques, Red Team audit) identified it.** Detail
below, per the three items requested.

---

## (a) The `back_frac` angular trend: does it have an optically sensible
## name, or is it unexplained?

**It is optically explainable, but NOT by anything specific to the
article's angular scattering response — it is very likely a box-face
registration artifact, and I can show this quantitatively from the
persisted data, not merely argue it qualitatively.**

`lab/sections.py::widths()` computes `sigma_scat` (`p_scat`) as the **net
outward flux summed over all four box faces** (`_face_flux`:
`sx(x1)-sx(x0)+sy(y1)-sy(y0)`), but `back_frac`'s numerator (`p_back`) and
`fwd_frac`'s numerator (`p_fwd`) only ever read the **two x-faces**
(`x0`/`x1`). The two y-faces (`y0`/`y1`, "lateral") contribute to the
`sigma_scat` denominator but to neither fraction's numerator — NOTES.md's
own Idealizations section discloses this as "a lateral/diffuse remainder
exits through the box's `y0`/`y1` faces," but only as a static disclosure,
not as something that could itself vary systematically with θ and drive
the very trend Predictions 2/3 are scored against.

I recomputed the lateral share directly from `results.json` (`lateral =
sigma_scat - sigma_scat_downstream - sigma_scat_sourceward`, `C40_R4`,
BOX_A, all six angles):

| θ (deg) | tan θ | `back_frac` | `sigma_scat` | lateral flux | lateral/`sigma_scat` |
|---|---|---|---|---|---|
| 37.1272 | 0.757 | 0.6536 | 294.01 | 101.84 | 0.3464 |
| 38.5902 | 0.798 | 0.6185 | 300.84 | 114.70 | 0.3813 |
| 39.2000 | 0.816 | 0.6076 | 303.16 | 118.91 | 0.3922 |
| 40.2654 | 0.847 | 0.5812 | 309.31 | 129.47 | 0.4186 |
| 41.4609 | 0.884 | 0.5619 | 312.55 | 136.89 | 0.4380 |
| 42.9609 | 0.931 | 0.5324 | 320.30 | 149.58 | 0.4670 |

(`G40_R4` reproduces this to within 0.002 at every angle — the two
configs "tracking each other to 3 decimal places" that NOTES.md notes is
exactly what a shared *geometric* (not article-specific) cause predicts.)

Over this 5.83° sweep, `sigma_scat` itself grows only ~9% (294→320, the
genuine extinction-cross-section growth with θ, unremarkable), while the
**lateral fraction grows ~35% in absolute terms (0.346→0.467) and the
lateral flux itself grows 47%** — several times faster than the total
scattered power. `back_frac`'s entire decline (0.6536→0.5324) is
arithmetically the mirror image of this lateral growth (sourceward stays
under 0.2/300 ≈ 0.06% throughout, negligible). Meanwhile `tan θ` itself
grows by 23% over the same sweep — same order of magnitude, same
direction, as the lateral-fraction growth.

**Optical reading:** `BOX_A`'s four faces are fixed in the lab (object)
frame, at the same `(x0,x1,y0,y1)` for every angle — they do not rotate
with the incident beam. The object is a circular PEC+graded-shell
cylinder (`ka = 2π·R4_R_OUT/λ = 2π·156/40 ≈ 24.5`, comfortably in the
large-size-parameter/geometric-optics regime), so by rotational symmetry
the *shape* of its forward-diffraction lobe, expressed in the beam's own
frame, should not itself change much over a 6° sweep. What changes is
purely geometric: as θ grows, the beam's own propagation axis (and hence
its forward-diffracted cone, which by Keller/GTD-type reasoning stays
collinear with the incident ray) tilts further away from the box's fixed
x-axis, so a growing share of the *same* forward-diffracted power crosses
the box's y-faces instead of its x0 ("downstream") face — exactly what the
lateral-fraction numbers above show. I could not find, and NOTES.md/the
Phase-1/Phase-2 record does not cite, any established Mie-phase-function
or GTD relation that predicts a genuine *change in the article's own*
forward/backward scattering split over a bare 6° incidence-angle range for
a rotationally symmetric absorber this large — the far more parsimonious
explanation is box-frame vs. beam-frame misalignment, not new physics.

**This matters for exactly the reason this cycle exists.** The whole
premise of the closed-box fix is that a box "cannot miss the shadow
regardless of which way it walks" (Phase-1 §1) — true for the *aggregate*
`sigma_scat`/`sigma_abs`/`sigma_ext` (rigorous energy conservation,
independent of angle or box orientation). But the **face-wise split**
(`back_frac`/`fwd_frac`, and hence `sigma_scat_downstream` — Tier-0's own
actual deliverable, the intended replacement for `beam_behind_t28`) is
NOT immune to an angle-dependent registration artifact, and this cycle's
own due-diligence check (`box_dev_scat_downstream`, BOX_A vs. BOX_CROSS)
cannot catch it: both boxes share the *same* fixed orientation, so
agreeing with each other only rules out *size* sensitivity, never
*orientation-vs-beam-obliquity* sensitivity. A future instrument (T3, or
any successor built on `sigma_scat_downstream`) that wants a genuinely
angle-robust forward-power reading needs either a box that rotates with θ
or an explicit beam-axis-aligned coordinate frame — not the current
object-centered, lab-axis-aligned box. Nobody in this cycle's five
critiques or the Red Team audit raised this (their box concerns were about
absorb-boundary clearance and box *size*, a different geometric axis of
the same machinery).

---

## (b) Is NOTES.md's extinction-paradox/Babinet explanation for
## Prediction 3's falsification correct and complete?

**Correct as far as it goes; incomplete on two charter-relevant points.**

The core physics is right and is standard: for an optically large
(`ka≈24.5`), near-zero-reflectance absorber, the extinction paradox
(`Q_ext→2` in the geometric-optics limit) is a real, established result —
half the extinction is genuine absorption of intercepted rays, half is a
forward-diffracted wave of comparable cross-section that destructively
interferes with the unperturbed beam to *create* the geometric shadow
(Babinet's principle). A large `sigma_scat_downstream` being the
*companion* of a real shadow, not evidence against one, is the right
qualitative conclusion, and heading off a future cycle's naive
misreading is a genuinely useful, disclosed finding.

Two gaps, both inside this seat's angular/spectral-coherence charter:

1. **The asymptotic Q_ext→2/Babinet argument is a far-field (Fraunhofer)
   statement, and this cycle's box sits deep in the near field** —
   `BOX_A`'s faces are only 24–48 cells beyond the object's own
   `R4_R_OUT=156`-cell radius, i.e. z/z_R≈0.04–0.06 (T8, already logged on
   this bench and cited elsewhere in this very NOTES.md for Prediction 2).
   NOTES.md invokes T8's near-field caveat when *hedging* Prediction 2's
   confirmation ("genuinely untested... T8's open caveat"), but does **not**
   re-invoke it when asserting Prediction 3's falsification is fully
   explained ("this prediction band was wrong about the physics, not
   merely mis-calibrated"). The qualitative direction of the argument
   (large forward lobe) is genuinely far-field-independent (it follows
   from `σ_ext=σ_abs+σ_scat` energy bookkeeping alone), but the specific
   claim that this measurement's `sigma_scat_downstream` value should
   match the geometric-optics asymptote in *magnitude* is exactly the kind
   of far-field-derived expectation T8 warns cannot yet be assumed to hold
   at this box distance. The same disclaimer discipline change 6 already
   applies to the `sigma_abs/sigma_ext` ratio should have been applied
   here too, for consistency.
2. **NOTES.md treats Prediction 3's falsification (an extinction-paradox
   magnitude story) and the back_frac angular trend (filed separately, in
   "Learned," as a possible genuine article finding "worth a future
   cycle's attention") as two unrelated observations.** Per (a) above,
   they are very likely the *same* underlying box-registration effect
   viewed two ways: the large, angle-dependent `sigma_scat_downstream`
   values Prediction 3 measured are partly an accounting artifact of how
   much of the (genuinely large, extinction-paradox-consistent) total
   diffracted power happens to cross the box's x0 face vs. its y-faces at
   each θ — not a clean, angle-independent measure of "the true
   forward-diffraction cross section" that a future T3-style instrument
   could reuse as-is. NOTES.md's own "Next" item 1 (build a coherent,
   phase-resolved successor) correctly flags the incoherent-power vs.
   coherent-field distinction as a limitation of this cycle's own
   quantity, but does not flag this *second*, purely-geometric limitation
   (lab-frame box axes vs. beam axis) that afflicts even the *incoherent*
   power partition once θ is oblique enough — a future cycle building
   directly on `sigma_scat_downstream`'s numbers, rather than starting the
   successor instrument from scratch, would inherit this.

---

## (c) Was my own Phase-2 concern (the two re-selected extremal angles
## carrying no established `delta_scene`/`frac_p_abs` correlation)
## adequately addressed?

**Yes, for what it actually applies to — and the final data make clear
it was never load-bearing to begin with.** NOTES.md's Prediction 3 carries
my Phase-2 disclosure sentence forward essentially verbatim (the R4-family
`r=0.1103, p=0.5249` correlation, framed as "instrument-behavior data...
not evidence of angle-dependent optical engagement, pending Tier 1"), and
Red Team's own audit (attack #3, adopted as change 5) went further and
found the R3 comparator I leaned on for contrast is itself fragile
(duplicate rows; `r=0.486,p=0.0042`→`r=0.360,p=0.107` deduplicated) —
NOTES.md correctly declines to carry that comparator forward as settled.
Both fixes are real and correctly scoped.

But the finished results make the underlying worry moot in a way nobody
states explicitly: **Prediction 3's falsification is uniform across all
six angles** (range `[0.5457, 0.6159]`, no discontinuity at
`39.200000°`/`42.960901°` relative to the four cpl20-crossing angles), and
**`back_frac`'s decline is smooth and monotonic across the full 37–43°
sweep**, tracking `tan θ` continuously rather than spiking at the two
`delta_scene`-extremal points. If either finding were actually driven by
whatever mechanism makes `delta_scene` peak at those two angles (an
oscillatory, cpl-tied confound per the T28 thread), a discontinuity or
non-monotonic wiggle right at 39.2°/42.96° would be the signature to
expect; instead the data are smooth in θ across angles selected for two
entirely different reasons (cpl20 zero-crossings vs. pool-magnitude
extrema). That is itself a small piece of positive evidence *for* my (a)
finding above (a continuous function of incidence angle, i.e. geometric
registration) and *against* reading either result as tied to the
angle-selection criterion my Phase-2 critique was worried about. NOTES.md
does not make this observation, but it does not need to — my original
concern was about mislabeling a *result at those two specific angles* as
an article finding, and no such angle-specific result exists in the
Result section to mislabel.

---

## Summary for the Director

1. Tier-0's core deliverable stands: total-flux conservation via the
   closed box, all six mandatory Red-Team fixes correctly implemented,
   trust gates genuinely green.
2. **New finding (this review, not caught by the proposal, any Phase-2
   critique, or Red Team's audit):** `back_frac`/`sigma_scat_downstream`'s
   decline with θ is best explained by box-face registration against a
   rotating beam axis, not by any established or article-specific angular
   scattering law — demonstrated quantitatively via the lateral
   (y-face) flux share, which grows 47% (vs. `sigma_scat`'s own 9%) over
   the same sweep that grows `tan θ` by 23%. `box_dev_scat_downstream`
   (same-orientation, different-size box pair) structurally cannot detect
   this, since it never varies box orientation relative to the beam.
3. Recommend, for whichever future cycle takes up "Next" item 1 (coherent
   downstream instrument) or item 2 (investigate the `back_frac` trend):
   do not treat this cycle's `back_frac`/`sigma_scat_downstream` numbers as
   an angle-clean baseline without first testing box-orientation
   sensitivity (e.g. a beam-aligned or rotated box) — the current
   `BOX_A`/`BOX_CROSS` pair only tests size-independence at fixed
   orientation.
4. NOTES.md's Prediction-3 physical explanation (extinction paradox /
   Babinet) is directionally correct but should carry the same T8
   near-field disclaimer it already applies to Prediction 2, for internal
   consistency, and should be read as connected to (not separate from) the
   back_frac angular-trend observation in "Learned."
5. My own Phase-2 concern about the two re-selected extremal angles is
   correctly discharged in NOTES.md and, per the finished data, was never
   actually load-bearing — both scored phenomena are smooth, continuous
   functions of θ across all six angles, not artifacts localized to the
   two `delta_scene`-extremal points.
