# exp-062 Phase 4 — Search Results, Scored Against Frozen Predictions

**Panel Iteration 39.** Scores EM-1 through EM-7 (plus EM-5b) as committed
in `NOTES.md` (commit `9e73b45`), frozen BEFORE this search ran. Nothing
in `NOTES.md` is edited by this file — per house discipline, this is a
separate, append-only Phase-4 record.

**Evidentiary tier for this entire document (T18): WebSearch-snippet
synthesis, not primary-source PDF/DOI-verified reading.** Every numeric
figure below is a WebSearch result-summary figure, cited by search-result
title, not a number read from the original paper/patent/datasheet PDF.
Restated at each verdict below per registry entry
`exp061-t18-evidentiary-tier-propagation`'s own propagation requirement
(widened at Phase 3 to cover this file).

---

## Step 1 — T18 (WebFetch block) re-confirmation

Two WebFetch attempts this shift:

1. `https://patents.google.com/patent/US20180346682A1/en` → `EGRESS_BLOCKED`.
2. `https://ntrs.nasa.gov/api/citations/20140011044/downloads/20140011044.pdf` → `EGRESS_BLOCKED`.

**T18 stands, as predicted.** 43+ consecutive blocked WebFetch attempts
since Iteration 13 (41+ carried forward from exp-061 + these 2). Phase 4
proceeds exactly as disclosed: **WebSearch-snippet synthesis only.** No
primary-source PDF was read for any figure in this file.

---

## Step 2 — the 14 committed queries (verbatim, run in order) + 4 supplementary

1. `Brewer Science black matrix organic photoresist optical density measurement method reflectance or transmission` — found spectrophotometric transmittance-AND-reflectance characterization methodology in general use; a pigmented-photoresist OD=3.8/µm figure.
2. `LCD black matrix optical density OD measurement convention reflection transmission display` — **key finding**: the standard LCD black-matrix OD definition is explicitly **transmission-based**: "transmission optical density (OD) of the substrate having a light-shielding film is measured at a wavelength of 555nm with a spectrophotometer... the value obtained by subtracting OD0 [bare substrate] from OD is taken as the transmission optical density." Also: "a black matrix should preferably be 2.3 or more in optical density per µm of thickness in the visible light wavelength range of 430–640nm" — a broadband (not single-λ) spec, with 555nm used only as the standard photometric reference point.
3. `high optical density ultra thin organic black matrix patent reflective backplane substrate metal layer` — confirms the Brewer Science patent (US5998090A) composition is Pigment Black 7 + organic dye on a polyimide vehicle — a discrete-pigment absorbing layer, not a reflective-metal-backed stack. A structurally DIFFERENT, genuinely interference-based black-matrix class exists in the literature (three-layer ZnO/Mo/ZnO antireflector, US5570212) — but this is a different patent family, not the one MP-3 cites.
4. `black matrix photoresist optical density visible spectrum wavelength range broadband narrowband` — "the technical goal is to keep the light transmission at or below 1%, across the entire spectrum of from ultraviolet to infrared" — broadband confirmed for this material class generally; no interference-stack/quarter-wave/antireflection language found for the pigment-loaded photoresist class specifically.
5. `black matrix coating interference stack quarter wave antireflection display panel` — confirms quarter-wave/interference antireflection IS a real, distinct black-matrix design strategy in the literature (used in some OLED-era circular-polarizer and metal-oxide-stack designs) — but again, a different design family from the pigment-loaded organic photoresist class MP-3 cites.
6. `carbon black pigment loaded photoresist absorption coefficient thin film optical density` — **key finding, generic definition**: "Optical density is the logarithm of the ratio of the intensity of light incident on a layer to the intensity of light **transmitted** through the layer" — confirms OD = −log₁₀(T) as this material class's standard convention, independently of query 2.
7. `electroless nickel phosphorus NiP black coating reflectance absorptance optical properties` — R≈0.5–5% across various NiP-black processing routes; solar-absorptance figures up to 99.9%.
8. `NiP black coating optical density thickness micron space stray light baffle` — general stray-light-baffle coating thickness context (black chrome 0.5–2.5µm; other vacuum-deposited coatings <1µm) — no direct (R, thickness) pair for NiP specifically in this query's snippets.
9. `graphene aerogel optical absorption coefficient broadband visible reflectance` — graphene monolayer α≈7×10⁵cm⁻¹ (a single 2D sheet, not a bulk/aerogel figure — flagged, not pooled); graphene-polymer composite R≈4–8% (VIS-NIR).
10. `carbon aerogel ultra-black coating reflectance thickness absorption coefficient` — R<0.24% (400–2000nm) for low-density (<70mg/cm³) carbon aerogels.
11. `vertically aligned carbon nanotube forest inter-tube spacing pitch diameter nanometer` — D=65±20 to 93±20nm (stainless-steel-grown VACNT forest characterization); a separate "0.34nm inter-tube distance" figure flagged as likely a MWCNT wall-to-wall (graphitic interlayer) spacing, NOT an areal forest pitch — a real unit/definition-confusion risk, disclosed not silently used.
12. `carbon nanotube forest areal packing density tube diameter gap nanometer volume fraction` — **key sourced figure**: "average radius of 60nm (coated), density of 10 nanotubes per µm², surface fraction 11%" (self-consistent with `f=(π/4)(D/p)²`); separately, "average distance between CNTs... about 47–64nm for spin-capable forests" (a directly-stated gap figure, different growth/application class).
13. `vertically aligned multi-walled carbon nanotube effective index n_eff 1.04 0.01i original paper title` — **PINS the standing citation**: "Modulation of the effective density and refractive index of carbon nanotube forests via nanoimprint lithography," *Carbon*, 2018, vol. 129, pp. 8–14 — resolving a 3+-cycle-flagged "currently un-pinnable to an originating title" gap (Iteration 38's carried backlog, flagged by MATERIALS/QUANTUM/VISION).
14. `black matrix optical density measurement specular near-normal vs diffuse integrating sphere hemispherical spectrophotometer` — found BOTH conventions in active industrial use depending on display technology: LCD-generation black matrix OD is defined via **transmission** through a transparent substrate (queries 2/6, above — no reflective backing at all in this measurement geometry, so the whole "resonant absorber via reflective backing" alternative is **structurally inapplicable** to how this specific patent's figure is measured, not merely disfavored by a broadband reading); separately, hemispherical/diffuse reflectance spectrophotometry IS standard for OLED-era black matrix characterization (a reflective-backplane display technology where a resonant/interference effect could in principle apply) — but the Brewer Science patent (1998–99, explicitly targeting "TFT or STN displays") predates OLED-era practice and is textually an LCD-class patent.

**[SUPPLEMENTARY, 4 beyond the 14]**
15. `"black nickel" OR "NiP black" coating micron thickness reflectance percent optical` — NiP thickness figures (10µm, 45±5µm, "tens to a hundred microns" typical) paired (cross-query, not one source's own pairing) with R≈0.5–1.0% (320–2140nm) chemically-treated electroless NiP-black figures.
16. `carbon aerogel monolith thickness millimeter total reflectance visible super black material` — "carbon aerogel monoliths can achieve effective absorption with thin thicknesses of 1.9mm," "adjusting thickness from 1–5mm" — paired (cross-query) with query 10's R<0.24% figure.
17–18. Two follow-up n_eff-pinning searches (query 13's own iteration) before landing the citation above.

---

## EM-1 — coherent multi-beam interference bound

**Predicted:** ≤0.2% relative (T-based, τ=6.91); ≤6.3% relative (R-based,
τ=3.45) — the passivity envelope `2e^{-τ}`.

**Result: not empirically tested this cycle** — this is a closed-form
derivation from `|r₁₂|,|r₂₃|≤1`, already verified by direct computation at
Phase 1 and independently re-derived by Red Team at Phase 2 (both to the
same printed digits). No search result bears on it either way; nothing
here changes the bound. **Verdict: CONFIRMED (unchanged, theoretical).**

## EM-2 — R-vs-T geometric correction

**Predicted:** transmission-based ⇒ 1.20× stands; reflectance-based ⇒
corrects to 0.60×.

**Result: CONFIRMED — transmission-based.** Two independent query results
(2, 6) both state the OD convention for this material class as
`OD = −log₁₀(T)`, defined via transmittance, not reflectance — query 2
even gives the exact measurement protocol (spectrophotometer, light
through the coated substrate vs. the bare substrate, reference wavelength
555nm). **α stands at 6.908×10⁴cm⁻¹, ratio 1.2034×** (recomputed by
direct invocation this shift, matching Phase 1/3's own figures exactly —
see script output in this document's commit). No ÷2 correction applies.

## EM-3 — spectral bandwidth as a resonance discriminator, conditioned on
measurement geometry

**Predicted:** broadband + no interference-stack mention (specular case);
uninformative if angle-integrated/undetermined.

**Result: CONFIRMED, more decisively than predicted.** (a) Broadband
confirmed: "keep light transmission at or below 1%, across the entire
spectrum from ultraviolet to infrared" (query 4); a 2.3 OD/µm floor stated
across 430–640nm (query 2) — no single-design-λ framing anywhere. (b) No
multilayer/quarter-wave/antireflection stack mentioned for this patent's
own composition (Pigment Black 7 + dye + polyimide, query 3) — a
genuinely different, interference-based black-matrix class exists in the
literature (query 5) but is a separate patent family. (c) **The
measurement-geometry conditioning added at Phase 3 (mandatory fix 2)
resolves cleanly, not merely "specular, so evidence stands":** query 14
establishes the LCD-era OD convention is measured in **transmission**
through a transparent, unbacked substrate — there is no reflective
backing in this measurement geometry at all, so the entire Salisbury-
screen/critically-coupled-resonance mechanism (which REQUIRES a reflective
backing to interfere against) is **structurally inapplicable**, not just
disfavored by a broadband reading. This is a stronger resolution than
Phase 1/3 anticipated: the falsification condition's own angle-
integration concern (mandatory fix 2) turns out not to bind, because the
measurement is transmission-mode on an unbacked substrate, not
reflectance-mode on a backed one.

## EM-4 — net effect on the numeric-proximity axis

**Predicted:** ratio lands in [0.60×,1.20×], reinforces not threatens the
mechanism-class exclusion.

**Result: CONFIRMED, at the upper (unmodified) end.** EM-2/EM-3 together
settle the R-vs-T question and the resonance-alternative question in the
SAME direction: transmission-based (no ÷2 correction) AND structurally
non-resonant (transmission through an unbacked substrate). The ratio
therefore stands at exactly exp-061's own original **1.20×** — this cycle
does not move the number, but converts an unchecked point estimate into a
checked one, closing both open questions MP-3/MP-4 flagged. The
mechanism-class exclusion (discrete-pigment vs. `graded_black_shell`'s
index-graded homogeneous medium) remains the operative reason this
candidate doesn't flip MP-4's tier — EM's own analysis this cycle
reinforces, not substitutes for, that exclusion.

## EM-5 — near-field-coupling existence

**Predicted:** `ratio≈0.68<1` (illustrative, D=20nm/f=5%); sourced figures
predicted to confirm ratio<1 at all three bench λ (450/600/750nm).

**Result: PARTIAL — falsified as stated; genuinely mixed across sourced
geometries.** Queries 11–12 surfaced THREE independent, non-overlapping
sourced geometries, computed by direct invocation:

| Source | D or gap | f (if derived) | ratio@450 | ratio@550 | ratio@600 | ratio@750 |
|---|---|---|---|---|---|---|
| Phase-1 placeholder (illustrative, not sourced this cycle) | D=20nm | 5% | 0.828 | 0.677 | 0.621 | 0.497 |
| Query 11 (stainless-steel VACNT characterization) | D=65nm | 5% (assumed, not co-sourced) | 2.689 | 2.200 | — | 1.614 |
| Query 11, upper D | D=93nm | 5% (assumed) | 3.848 | 3.148 | — | 2.309 |
| Query 12 (directly co-sourced: r=60nm, 10 tubes/µm², f=11%) | D=120nm | 11% (stated) | 2.740 | 2.242 | 2.055 | 1.644 |
| Query 12 (spin-capable forests, directly-stated gap) | gap=47nm | — | 0.656 | 0.537 | 0.492 | 0.394 |
| Query 12 (spin-capable forests, directly-stated gap) | gap=64nm | — | 0.894 | 0.731 | 0.670 | 0.536 |

**The near-field-coupling regime (`ratio<1`) is confirmed for the
spin-capable/yarn-precursor forest class (directly-stated gap, no
packing-fraction assumption needed) at every bench wavelength — but
REFUTED for the two other, independently-sourced dense-forest geometries**
(the stainless-steel-characterization diameter combined with any
reasonable packing fraction, and the directly co-sourced r=60nm/11%
figure) at every bench wavelength except a near-unity crossing at 750nm
for the most favorable dense-forest combination (D=65nm, f=10%,
ratio=0.982 — see Phase 1/3's own `NOTES.md` table, not reproduced here
since f=10% at D=65nm was not itself directly co-sourced this cycle).
**Neither this cycle's own searches, nor exp-061's own query 9, ever
pinned the specific pitch/diameter of a record-blackness/Vantablack-class
forest** (the comparison class this program's own α figures actually
cite) — the three sourced geometries above belong to different
CNT-forest application classes (general characterization, spin-capable
yarn precursors, and a density/refractive-index-modulation study),
none of them the ultra-black coating literature MP-1/MP-2 themselves
drew from. **This is a real, disclosed evidentiary gap, not resolved by
this cycle's search — the near-field classification is geometry-class-
dependent, not universal, and remains genuinely open for the specific
comparison class this program cares about.**

## EM-5b — near-field-coupling direction (enhance vs. suppress)

**Predicted:** UNDECIDABLE from available snippets.

**Result: CONFIRMED UNDECIDABLE.** None of queries 6–14 (or the four
supplementary queries) surfaced coupled-dipole/local-field-correction or
superradiant/subradiant-response literature discussing which direction
dense sub-λ CNT coupling biases ensemble absorption relative to an
independent-scatterer Beer–Lambert reading. QUANTUM OPTICS' own Phase-2
flip (mandatory fix 5) is therefore not resolved this cycle — flagged
explicitly for Phase 5, not silently dropped.

## EM-6 — NiP-black coating effective α / thickness

**Predicted band:** thickness 10–200µm, α 10²–10⁴cm⁻¹.

**Result: CONFIRMED (order-of-magnitude band match), falsification
condition NOT triggered.** Cross-query pairing (query 7/15's R≈0.5–1.0%
with query 8/15's typical thickness figures 10–45µm — not one source's
own paired measurement, a disclosed weakness matching exp-061's own MP-1
caveat pattern): **α≈1.0×10³–5.3×10³cm⁻¹** at 10–45µm, computed by direct
invocation:

```
R=1.00% (OD=2.000): t=10µm -> alpha=4605 cm^-1  (ratio to target 0.0802)   t=45µm -> alpha=1023 cm^-1  (ratio 0.0178)
R=0.50% (OD=2.301): t=10µm -> alpha=5298 cm^-1  (ratio to target 0.0923)   t=45µm -> alpha=1177 cm^-1  (ratio 0.0205)
```

Both α and thickness land inside the predicted band. **Thickness gap vs.
this construction's 1.44µm: 6.9×–31.25×** — genuinely smaller than
CNT-forest's own 70–350× gap, making NiP-black the CLOSEST real-material
secondary comparator this program has found for `graded_black_shell`'s
own construction, by thickness alone. **Falsification NOT triggered**:
neither α (11–56× below target) nor thickness (7–31× above) clears the
required "within ~2× of both, together" bar. **MATERIALS' own tier
interpretation is owed at Phase 5**, per `NOTES.md`'s explicit assignment
— this Phase-4 record reports the raw finding and its falsification
status only.

## EM-7 — carbon/graphene-aerogel effective α / thickness

**Predicted band:** thickness 5–500µm, α 10²–10⁴cm⁻¹.

**Result: PARTIAL — undershoot on BOTH axes, band miss.** Cross-query
pairing (query 10's R<0.24% with query 16's 1–5mm thickness figures —
disclosed cross-query weakness, as above): **α≈12–60cm⁻¹ at 1–5mm**,
computed by direct invocation:

```
t=1.0mm -> alpha=60.32 cm^-1  (ratio to target 0.00105)   thickness x 1.44um: 694.4x
t=1.9mm -> alpha=31.75 cm^-1  (ratio to target 0.00055)   thickness x 1.44um: 1319.4x
t=5.0mm -> alpha=12.06 cm^-1  (ratio to target 0.00021)   thickness x 1.44um: 3472.2x
```

**Both figures miss the predicted band**: α (12–60cm⁻¹) sits BELOW the
predicted 10²–10⁴cm⁻¹ floor; thickness (1–5mm) sits ABOVE the predicted
5–500µm ceiling — real ultra-black carbon aerogels are even more dilute
and even thicker than this proposal anticipated, the same direction of
surprise exp-061's own MP-1 found for CNT forests (real materials read
MORE dilute than predicted, not less). **Thickness gap vs. 1.44µm:
694×–3472×** — the LARGEST realizability gap found anywhere in this
program's history for this construction, exceeding even CNT-forest's own
70–350× figure. **Falsification NOT triggered** (nowhere close). Same
Phase-5 tier-interpretation assignment as EM-6.

---

## Overall summary table

| Prediction | Predicted | Found | Verdict |
|---|---|---|---|
| EM-1 (interference bound) | ≤0.2%/≤6.3% | Unchanged theoretical bound, re-verified twice (Phase 1, Phase 2) | **CONFIRMED** |
| EM-2 (R-vs-T basis) | Conditional on convention | Transmission-based, confirmed by 2 independent queries — 1.20× stands | **CONFIRMED** |
| EM-3 (bandwidth discriminator) | Broadband, no stack (specular case) | Broadband confirmed; no stack for this patent's class; measurement is transmission-mode on an UNBACKED substrate — resonance mechanism structurally inapplicable | **CONFIRMED**, more decisively than predicted |
| EM-4 (net numeric effect) | [0.60×,1.20×], reinforces exclusion | 1.20× stands exactly; exclusion reinforced by a checked, not assumed, R-vs-T/resonance analysis | **CONFIRMED** |
| EM-5 (near-field existence) | ratio<1 at all 3 bench λ | Confirmed for ONE sourced geometry class (spin-capable forests); refuted for TWO others (dense stainless-steel-class and directly co-sourced r=60nm/11% forests); the record-blackness-class forest's own pitch remains unpinned | **PARTIAL** — falsified as a universal claim; geometry-class-dependent |
| EM-5b (near-field direction) | UNDECIDABLE | UNDECIDABLE — no direction-bearing literature surfaced | **CONFIRMED UNDECIDABLE** |
| EM-6 (NiP-black) | 10–200µm, 10²–10⁴cm⁻¹ | 10–45µm, ~1.0–5.3×10³cm⁻¹ — inside predicted band; NOT within 2× of target on either axis | **CONFIRMED** (band), falsification NOT triggered |
| EM-7 (carbon/graphene aerogel) | 5–500µm, 10²–10⁴cm⁻¹ | 1–5mm, ~12–60cm⁻¹ — BOTH outside predicted band (thinner-band-miss on α, thicker-band-miss on thickness); largest realizability gap found this program's history | **PARTIAL** (band miss, same direction of surprise as exp-061's MP-1) |

**Bottom line: exp-061's UNOBTANIUM-WITH-PARAMETERS tier is untouched and,
if anything, further reinforced.** The two open numeric/mechanism
questions MP-3/MP-4 flagged (R-vs-T basis; resonance vs. bulk absorption)
are both CLOSED this cycle in the direction that reinforces, not
threatens, the existing mechanism-class exclusion — and more decisively
than predicted (a structural, not merely probabilistic, resolution of the
resonance question). The two new comparator classes (NiP-black,
carbon/graphene aerogel) both fail the "within 2× of both α and
thickness" bar; NiP-black is the closest real-material comparator this
program has ever found (6.9×–31× thickness gap, smaller than CNT-forest's
70–350×), while carbon/graphene aerogel is the WORST (694×–3472×). The
near-field-coupling question (EM-5) is the one genuine open result this
cycle produces — falsified as a universal claim, confirmed for one real
CNT-forest application class and refuted for two others, with the
program's own actual comparison class (record-blackness/Vantablack-type
forests) still unpinned on this specific geometric question. A genuine,
useful, non-tier-moving deliverable: the standing n_eff=1.04+0.01i
citation (flagged un-pinnable across Iterations 38 and earlier) is now
pinned to a specific title/journal/volume/year — *Carbon* 2018, vol. 129,
pp. 8–14 — closing a 3+-cycle-standing evidentiary gap, though the paper
itself remains unread (T18). Every verdict above is sourced via
**WebSearch-snippet synthesis, not primary-source PDF/DOI-verified
reading (T18)**, disclosed here one final time at the file's own closing
verdict, per registry entry `exp061-t18-evidentiary-tier-propagation`.
