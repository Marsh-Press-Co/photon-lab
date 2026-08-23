# exp-061 Phase 4 — Literature Search Results, Scored Against Frozen Predictions

**Panel Iteration 38.** Scores MP-1 through MP-5 as committed in `NOTES.md`
(commit `35f3179`), frozen BEFORE this search ran. Nothing in `NOTES.md`
is edited by this file — per house discipline, this is a separate,
append-only Phase-4 record.

**Evidentiary tier for this entire document (T18): WebSearch-snippet
synthesis, not primary-source PDF/DOI-verified reading.** Every numeric
figure below is a WebSearch result-summary figure, cited by search-result
title, not a number read from the original paper/datasheet/patent PDF.
This applies to every verdict rendered in this file — restated at each
verdict below per registry entry `exp061-t18-evidentiary-tier-propagation`'s
own propagation requirement.

---

## Step 1 — T18 (WebFetch block) re-confirmation

Two WebFetch attempts this shift, both on query-relevant URLs surfaced by
the WebSearch results below:

1. `https://www.pnas.org/doi/10.1073/pnas.0900155106` (the Yang et al.
   VA-SWCNT blackbody-absorber paper) → `EGRESS_BLOCKED` (network egress
   proxy).
2. `https://vantablack.co.jp/.../vantablack-s-vis-a4-data-sheet-space-v007.pdf`
   (Surrey NanoSystems S-VIS datasheet PDF) → `EGRESS_BLOCKED` (network
   egress proxy).

**T18 stands, as predicted.** This is now 41+ consecutive blocked WebFetch
attempts since Iteration 13 (39+ carried forward in `NOTES.md` + these 2).
Phase 4 proceeds exactly as disclosed: **WebSearch-snippet synthesis
only.** No primary-source PDF was read for any figure in this file.

---

## Step 2 — the 15 committed queries (verbatim, run in order)

All 15 queries from `NOTES.md`'s Setup section were run via WebSearch,
unreworded. Three supplementary queries beyond the 15 were also run
(labeled **[SUPPLEMENTARY]** below) to chase promising leads the core 15
turned up. Raw per-query snippets are not reproduced in full here (see
tool transcript); the figures extracted from each are cited by title in
the MP sections below.

1. `Vantablack absorption coefficient cm-1` — no direct α figure; only
   "99.965% absorption" percentage figures.
2. `carbon nanotube forest reflectance vs thickness optical density` —
   the 300–500µm/1–2%R vs 0.3–1µm/>80%R contrast (key MP-1/MP-2 pair).
3. `CNT forest ultra-black coating micron reflectance 0.035%` — VACNT
   0.012–0.045% R figures; CB-CNT automotive coating 0.05% R.
4. `Surrey NanoSystems Vantablack technical data sheet thickness` —
   VBx2 100–300µm; S-VIS "~250µm" (weakly sourced, see MP-2).
5. `NASA carbon nanotube black coating Hagopian absorptivity thickness` —
   99.5% UV/vis, 99.8% far-IR absorption; no thickness returned.
6. `vertically aligned carbon nanotube array effective refractive index imaginary part visible` —
   effective-medium/Bruggeman framing, no isolated n,k pair.
7. `super black carbon nanotube array reflectance forest height micron` —
   0.045% R figure; 200–650µm forest-height range.
8. `carbon nanotube forest absorption coefficient alpha cm-1 visible wavelength` —
   **n_eff = 1.04 + 0.01i "at visible wavelengths"** (key MP-1 figure).
9. `carbon nanotube forest packing density volume fraction optical properties` —
   Beer-Lambert-Bouguer attenuation methodology confirmed, no new α figure.
10. `NIST black coating characterization reflectance report` — NIST O2-
    plasma CNT-paint absorption-enhancement paper found; no thickness/α
    pair returned by the snippet.
11. `single wall carbon nanotube film extinction coefficient k optical constants` —
    k-peak at 450nm (exciton resonance) noted but not a scalar visible-band
    k; no usable α conversion.
12. `black silicon nanostructure reflectance absorption coefficient broadband` —
    secondary-class cross-check only (index-grading-dominant, per NOTES.md
    Idealization 4) — R<1–3%, no α/thickness pair for a homogeneous layer.
13. `ultra-black coating optical density per micron thickness` — **the
    "OD≥3.0 at ≤1µm" organic black-matrix patent figure** (key, and most
    consequential, single finding — see MP-3/MP-4 below).
14. `Acktar metal velvet black coating specular reflectance thickness` —
    Metal Velvet 3–8µm, <1% *specular* R (diffuse-dominated, caveated).
15. `ultra black coating ~1 micron thin film absorption coefficient visible` —
    cross-reference to bismuth sulfide α≈10⁴ cm⁻¹ as a general sanity
    anchor; TiAlC/SiO₂ and Cr/oxide interference-stack absorbers (excluded
    from MP-3 as resonant/interference-based, not non-resonant).

**[SUPPLEMENTARY]**
16. `"carbon nanotube forest" "absorption coefficient" per micron alpha` —
    randomly-modulated MWCNT forest, <20µm height, R<0.2% in mid-IR (key
    MP-1/MP-2/MP-5 data point, flagged mid-IR not visible).
17. `Vantablack S-VIS reflectance percent coating thickness micron space qualified` —
    S-VIS reflectance-vs-wavelength table (0.6%/0.3%/0.2%/0.2% at
    250/550/700/1400nm); no thickness in this pass either.
18. `vertically aligned multi-walled carbon nanotube effective index neff 1.04 0.01i reflectance visible near-infrared` —
    attempted to pin the n_eff=1.04+0.01i figure to one title; could not
    isolate the originating paper (see MP-1 caveat).

---

## MP-1 — literature CNT-forest effective α (OD-per-length)

**Predicted band:** 1×10³–3×10⁴ cm⁻¹.

**What was found**, with the R4-required explicit conversion for each
(OD = −log₁₀(R); τ = OD·ln(10); α = τ/thickness):

| Source (title) | Reported (R, thickness) | Conversion | α (cm⁻¹) |
|---|---|---|---|
| "(PDF) Optical reflection and absorption of carbon nanotube forest films on substrates" (ResearchGate) — query 2 | 300–500µm forests, R=1–2% | OD=1.70–2.00, τ=3.91–4.61 | **78–154 cm⁻¹** |
| WebSearch synthesized answer, query 8 (title not isolatable — see caveat below) | n_eff = 1.04+0.01i "at visible wavelengths" | α=4πk/λ, λ assumed 550nm (not stated by snippet — a chosen visible-band midpoint) | **≈2.28×10³ cm⁻¹** |
| Supplementary query 16 (randomly-modulated MWCNT forest paper) | height <20µm, hemispherical R<0.2%, **mid-IR** | OD>2.70, τ>6.22 | **>3.1×10³ cm⁻¹ (mid-IR, not visible)** |
| "S-VIS" reflectance table (query 17) paired with a separately-sourced "~250µm" thickness figure (query 4) — **two different search passes, not one paired report** | R=0.2% at 700nm; thickness ~250µm | OD=2.70, τ=6.22 | **≈249 cm⁻¹ (weak pairing — see caveat)** |
| VA-SWCNT R=0.045% (query 3/7) paired with the 300–500µm forest-height range (query 2) — **again a cross-query pairing, not one source's own paired figure** | R=0.045%; thickness assumed 400µm (band midpoint) | OD=3.35, τ=7.71 | **≈193 cm⁻¹ (weak pairing)** |

**Verdict: PARTIAL.** The single directly-comparable, single-source
figure (n_eff=1.04+0.01i, visible) lands **inside** the predicted band, at
its lower-middle (2.28×10³ vs. 1×10³–3×10⁴). The best cross-query-paired
figures (78–249 cm⁻¹) fall **below** the predicted band's own lower
bound — i.e., real CNT forests read as even MORE dilute/diffuse-dominated
than MP-1 predicted, not less — which is directionally consistent with
MP-1's own reasoning (light-trapping-dominated, not bulk Beer-Lambert) but
technically outside the numeric band as stated. The mid-IR outlier
(>3.1×10³ cm⁻¹) sits inside the band but is wavelength-mismatched to the
visible-band target. **None of the CNT-forest-class figures come within
an order of magnitude of the corrected target (5.74×10⁴ cm⁻¹).**

**Caveats, disclosed:** (a) most (R, thickness) pairs used above are
cross-query pairings — a reflectance figure from one search result matched
with a thickness figure from a *different* search result for a
*different*-named forest, not one source's own single paired
measurement; this is a real, disclosed weakness of snippet-synthesis
(the alternative — reporting no α figure at all — would be less useful,
but the pairing itself is not load-bearing-precise). (b) the n_eff figure
could not be pinned to one originating title (query 18 tried and failed);
WebSearch's summarizer stated it as if well-established, but this
document cannot certify which paper it traces to — reported here as
WebSearch-snippet synthesis, not primary-source PDF/DOI-verified reading
(T18), exactly the tier this file discloses throughout.

---

## MP-2 — published CNT-forest thickness at near-total blackness

**Predicted band:** 15–150µm, vs. this program's own 1.44µm.

**What was found:**

| Source | Thickness | Reflectance stated alongside |
|---|---|---|
| "(PDF) Optical reflection and absorption of carbon nanotube forest films on substrates" | 300–500µm | 1–2% (not "near-total," i.e. not the record-holder tier) |
| Surrey NanoSystems Vantablack VBx2 datasheet (spray-applied, ~2L/m²) | 100–300µm | not stated in this snippet |
| Surrey NanoSystems Vantablack S-VIS (space-qualified) | ~250µm (query 4; **not corroborated** by the dedicated query 17 re-search, which returned reflectance data only) | 0.2–0.6% across UV/vis/NIR (query 17) |
| Supplementary query 16 (randomly-modulated MWCNT forest) | <20µm | <0.2% hemispherical, **mid-IR** |
| Acktar Metal Velvet (query 14) | 3–8µm | <1% **specular** only — total/hemispherical R not given; this coating is explicitly marketed "Ultra Diffusive," i.e. optimized to scatter rather than absorb, so a low specular figure does not establish near-total absorptance (flagged per NOTES.md's own classical-parameter-scoping caveat) |

**Verdict: CONFIRMED**, with one wavelength-scoped exception. The best-
corroborated visible-wavelength CNT-forest figures (300–500µm, 100–300µm,
and the weakly-sourced ~250µm S-VIS figure) sit **within or above** the
predicted 15–150µm band — several samples are even thicker than the
upper bound, i.e. real record-blackness forests skew toward the high end
of, or past, the predicted range. The one figure below the band (<20µm)
is mid-IR, not visible, and its own reflectance (0.2%) is a full order of
magnitude short of the record-holder visible-band figures (0.035–0.045%),
so it is not a like-for-like near-total-blackness comparator. The Acktar
Metal Velvet figure (3–8µm) is the one candidate close to 1.44µm by
thickness alone, but its diffuse-scattering-dominant mechanism (explicit
in its own product name) means its low *specular* reflectance cannot be
read as evidence of near-total *absorptance* at that thickness — flagged,
not silently pooled into the CNT-forest thickness comparison.

**In every corroborated case: the gap from 1.44µm is large** (70–350×
for the well-sourced figures), confirming MP-2's own framing as the
dominant, anchor-invariant falsification axis.

---

## MP-3 — any primary-or-best-available source within ~2× of 5.74×10⁴ cm⁻¹, any visible wavelength, broadband non-resonant non-metallic coating

**Predicted: NOT FOUND.**

**For the CNT-forest/Vantablack class specifically: NOT FOUND**, confirmed.
The highest CNT-forest-class α figure recovered (mid-IR lower bound,
>3.1×10³ cm⁻¹) is still **>18× below** the 2× threshold (1.15×10⁵ cm⁻¹);
the best visible-band figure (n_eff-derived, 2.28×10³ cm⁻¹) is **>25×
below** it.

**One out-of-class candidate numerically clears the threshold** — flagged
prominently, not suppressed, per this cycle's own pre-registered
falsification discipline:

> **"High optical density ultra thin organic black matrix system"**
> (Brewer Science patent, query 13): reports **optical density ≥3.0 at
> coating thicknesses of 1 micron or less.** Conversion (R4, shown
> explicitly, taking the stated upper-bound thickness of exactly 1µm —
> a conservative choice, since a thinner actual film implied by "or
> less" would only raise α further): τ = 3.0·ln(10) = 6.908; α =
> 6.908/(1×10⁻⁴ cm) = **6.91×10⁴ cm⁻¹**, i.e. **1.20× the corrected
> target** — within the falsification band's own 2× threshold.

This is a **display-industry LCD black-matrix material** (carbon-black-
or graphite-pigment-loaded organic photoresist), not a CNT forest, not a
Vantablack-class manufacturer product, and not named in any of NOTES.md's
five ranked source classes — a sixth, unanticipated class. **It is
disclosed here as a genuine near-miss for MP-3's own literal wording**
("a genuinely broadband, non-resonant, non-metallic-interface coating" —
a carbon-black-pigment film arguably satisfies this literal description),
**but see MP-4 below for why it does not trigger the pre-registered MP-4
falsification condition specifically.**

**Verdict: PARTIAL.** NOT FOUND within the intended CNT-forest/Vantablack
comparison class (CONFIRMED as predicted for that scope); one weak,
patent-sourced, out-of-class candidate found for the broader literal
wording. Evidentiary tier for both the negative and the positive parts of
this finding: **WebSearch-snippet synthesis, not primary-source PDF/DOI-
verified reading (T18)** — the patent figure in particular is a claims-
language optical-density floor from a patent abstract/summary, not an
independently-verified laboratory measurement, and carries correspondingly
lower evidentiary weight than a peer-reviewed CNT-forest measurement would.

---

## MP-4 — the tier verdict

**Predicted: UNOBTANIUM-WITH-PARAMETERS** (driven by MP-2's thickness gap,
not by an implausible rate).

**Verdict: CONFIRMED — UNOBTANIUM-WITH-PARAMETERS.** Evidentiary tier for
this verdict: **WebSearch-snippet synthesis, not primary-source PDF/DOI-
verified reading (T18)** — stated here, adjacent to the verdict itself,
per registry entry `exp061-t18-evidentiary-tier-propagation`'s own
propagation requirement.

**Falsification check, explicit.** NOTES.md's own pre-registered
falsification condition requires a primary-or-best-available source
reporting **"CNT-forest (or comparable broadband graded near-ε=1
absorber)"** effective α within ~2× of target **AND** thickness within
~2× of 1.44µm, **both together**. The MP-3 near-miss candidate (the
organic black-matrix patent, α=6.91×10⁴ cm⁻¹ at ≤1µm) numerically clears
**both raw thresholds** (1.20× on α, 1.44× on thickness) — but it is
**not** a CNT forest and **not** a "graded near-ε=1 absorber": it is a
discrete-pigment-loaded Beer-Lambert dye/carbon-black film in a polymer
matrix, an entirely different `eps(r)` structure than `graded_black_shell`
codes (no radial index grading at all — the falsification condition's own
mechanism-class qualifier, not a goalpost this document is moving). **This
candidate is therefore excluded by the falsification condition's own
pre-registered wording, not by a post-hoc reinterpretation** — the
falsification condition does NOT trigger. This is the one finding this
document most needs Phase 5 to weigh independently, since the exclusion
turns on a mechanism-class judgment call (discrete-pigment vs.
index-graded), not on a numeric threshold.

**Coherence/localization scope-caveat fallback (also pre-registered):
does NOT trigger.** The sources found this cycle characterize CNT-forest
blackness via structural/diffuse multiple-scattering and effective-
medium-index language (Bruggeman model, n_eff=1.04+0.01i, Beer-Lambert-
Bouguer attenuation fits) — a homogenizable, reflectance-vs-thickness-
reducible framing, not predominantly coherence-length, Anderson-
localization, or near-field-coupling language. No source snippet this
cycle used those specific terms. MP-4 is therefore scoreable as a
scalar-α comparison, as MP-1/MP-2 above already did.

**Net: thickness, not rate, is confirmed as the harder ask**, exactly as
predicted — MP-1's α figures for CNT forests sit at-or-below the
predicted band (not dramatically above it), while MP-2's thickness gap is
70–350× for every well-corroborated visible-band figure.

---

## MP-5 — is τ_true≈8.26 achievable AT ALL, at some (greater) thickness?

**T1 escape route: NONE — this row scores zero constraint-1/2/3/4
metric**, per NOTES.md's own explicit instruction; nothing below is or
becomes a constraint-3 claim. Evidentiary tier: **WebSearch-snippet
synthesis, not primary-source PDF/DOI-verified reading (T18)**.

**Predicted: YES, PLAUSIBLE at ~15–100× the thickness.**

Conversion (R4, shown explicitly): for each α figure derived under MP-1,
the thickness needed to reach τ_true = 8.2588 is t = τ_true/α; the
multiple of the 1.44µm construction is t/1.44µm:

| α source | α (cm⁻¹) | thickness needed for τ=8.26 | × the 1.44µm construction |
|---|---|---|---|
| mid-IR <20µm forest (lower bound) | 3107 | 26.5µm | **18.4×** |
| n_eff visible (2285) | 2285 | 36.1µm | **25.1×** |
| S-VIS-paired estimate | 249 | 332µm | **231×** |
| 0.045%R/400µm-paired estimate | 193 | 429µm | **298×** |
| 300–500µm/1–2%R, high-α end | 154 | 538µm | **374×** |
| 300–500µm/1–2%R, low-α end | 78 | 1056µm | **733×** |

**Verdict: PARTIAL — qualitatively CONFIRMED, quantitatively an
undershoot.** Yes, real CNT-forest-class coatings appear able to supply
τ≈8.26 of optical depth — the darkest reported figures (R≈0.045%, τ≈7.7,
almost exactly τ_true) are not exotic. But at only ONE of six derived α
figures (the mid-IR, wavelength-mismatched one) does the required
multiple fall inside the predicted 15–100× band; the visible-band
figures — the more directly comparable ones — cluster at **~230–730×**,
one to two orders of magnitude higher than predicted. The qualitative
MP-5 conclusion (yes, plausible, just not at 1.44µm) is CONFIRMED; the
specific "~15–100×" quantitative claim is better restated as **"~20–700×,
most plausibly several hundred×, for visible-wavelength CNT-forest-class
coatings."** This is a genuine, disclosed sharpening, not a discovered
refutation — it does not change MP-4's tier and does not open any new
constraint-3/4 claim (T1 escape route: NONE, per above).

---

## Overall summary table

| Prediction | Predicted | Found | Verdict |
|---|---|---|---|
| MP-1 (CNT-forest effective α) | 1×10³–3×10⁴ cm⁻¹ | ≈78–3.1×10³ cm⁻¹ across sources (one figure inside the band, several below it); nothing near 5.74×10⁴ | **PARTIAL** — directionally right (well below target), band itself only partly matched |
| MP-2 (CNT-forest thickness at near-total blackness) | 15–150µm | 100–500µm (well-corroborated, visible); one 3–8µm diffuse-only outlier flagged, not pooled | **CONFIRMED** |
| MP-3 (any source within ~2× of 5.74×10⁴ cm⁻¹, any visible λ, broadband non-resonant) | NOT FOUND | NOT FOUND for CNT-forest class; one weak, patent-sourced, out-of-class (non-CNT, discrete-pigment) candidate numerically clears the raw threshold | **PARTIAL** |
| MP-4 (tier verdict) | UNOBTANIUM-WITH-PARAMETERS | Same — falsification condition's own mechanism-class qualifier excludes the one near-miss candidate (not a CNT-forest / graded near-ε=1 absorber); coherence/localization fallback did not trigger | **CONFIRMED** (T18: WebSearch-snippet synthesis, not primary-source PDF/DOI-verified reading) |
| MP-5 (achievable at all, some thickness) | YES, ~15–100× thickness | YES, but visible-band figures cluster at ~230–730×, not 15–100× (T1 escape route: NONE) | **PARTIAL** — direction confirmed, magnitude undershot |

**Bottom line:** the corrected construction's α (5.74×10⁴ cm⁻¹) is not
implausible relative to *some* real ultra-black coatings by rate alone —
one out-of-class organic pigment film numerically approaches it at
sub-micron thickness — but for the actual comparison class this
construction is meant to represent (CNT-forest/Vantablack-class, graded
near-ε=1 absorbers), thickness remains the dominant, unresolved gap: real
record-blackness CNT forests run 70–500× thicker than this construction's
1.44µm, and matching this construction's own required optical depth
(τ≈8.26) at CNT-forest-class α figures needs roughly 20–700× the
thickness, most plausibly several hundred×. **UNOBTANIUM-WITH-PARAMETERS
stands, confirmed** — every verdict in this file is sourced via
**WebSearch-snippet synthesis, not primary-source PDF/DOI-verified
reading (T18)**, disclosed here one final time at the file's own closing
verdict.
