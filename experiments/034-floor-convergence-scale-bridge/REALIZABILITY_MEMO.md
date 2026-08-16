# MATERIALS' realizability memo — the σ(I) switching mechanism vs published nonlinear-absorber physics

Panel Iteration 11 close-out, mandatory fix 7 (Red Team's Phase-5 audit).
Zero FDTD cost — a desk synthesis of this program's own established
numbers against published nonlinear-optics literature, informal (as
MATERIALS' own Iteration-9 check was self-flagged), not a rigorous survey.
Named as an open deliverable at the close of Iterations 9, 10, and 11 — a
three-cycle deferral this closes.

**AMENDMENT (Iteration 12, exp-035, MATERIALS' Phase-5 review + Red Team's
mandatory correction):** the "only σ(I) OFF-state configuration... to clear
that bar" (line 19, below) no longer clears the bar at EITHER geometry it
has ever been checked at (r=156: already MARGINAL at this memo's own
writing; r=78-native, THIS configuration's own home geometry: now shown
MARGINAL too, cleanly, without a domain-construction confound — exp-035,
LOGBOOK.md Iteration 12/T16). **D_req≈540–600× below should therefore be
read as a LOWER bound on the true dynamic range a real switch would need,
not an achieved reference point measured from a configuration that
actually cleared the bar** — if a genuinely constraint-3-clearing τ_off
exists at all, it must be smaller than 0.0065 (since 0.0065 no longer
clears under correctly-quadrature-instrumented measurement), which makes
the true D_req larger, not smaller, than the figure below. This
**sharpens, not weakens**, this memo's own UNOBTANIUM-WITH-PARAMETERS
verdict — it removes the one empirical foothold that made D_req read as
"the gap from a real starting point" rather than "the gap from a
hypothetical one." Does not change the TPA irradiance-gap finding (already
independent of any OFF-state ambient-contrast reading). This amendment
does not itself escalate this memo toward a Checkpoint-2 finding — that
still needs the rigorous (not informal) literature check this memo's own
"Idealizations and honest limits" section names as its missing rigor
(queued, Iteration 13's top-ranked priority per Red Team's Iteration-12
close).

**AMENDMENT 2 (Iteration 14, exp-037, MATERIALS' Phase-5 finding — a
three-cycle-deferred deliverable, named at the close of Iterations 12 and
13 and finally closed this shift, not deferred a fourth time).** This
memo's own scope, as originally written, evaluated only RSA and TPA and
named three further classes as not-yet-evaluated (free-carrier absorption,
photochromic switching, combined saturable/RSA media — see "Idealizations
and honest limits," below, unchanged as the historical record). Two
literature-check cycles since (exp-036, Iteration 13; exp-037, Iteration
14) have now checked all three of those named classes, plus split
photothermal/VO2 out of photochromic (exp-036's own mandatory fix) and
added two classes neither this memo nor any prior cycle had named (ENZ,
graphene — exp-037's own Phase-1 scoping). **Consolidated realizability
table, all classes checked to date, tier labels per this seat's charter
(published / plausible / unobtainium-with-parameters):**

| Class | D_req / dynamic-range finding | Irradiance finding | Tier | Source |
|---|---|---|---|---|
| RSA | ~2–7.2× typical, ~40× best single-outlier figure (porphyrin); ≥890–1180× corrected bar → ~22–30× short even at best figure | Clears, one subclass at ~10⁻⁴ W/cm², below witness estimate | UNOBTANIUM-WITH-PARAMETERS | exp-036 |
| TPA | n≈1 clears exponent bar comfortably | ~10⁷–10⁸ W/cm², 9–11 OOM above ceiling | UNOBTANIUM-WITH-PARAMETERS | exp-036 |
| Photochromic (photochemical) | Azobenzene ~3–6× short (1–2 orders); diarylethene/spiropyran genuinely open (no paired ε table recovered) | Clears easily | UNOBTANIUM-WITH-PARAMETERS (azobenzene); OPEN (diarylethene/spiropyran) | exp-036 |
| Photothermal (VO2) | Intrinsic ~10–30×, short before irradiance even binds | Every scale from µm–m fails heating+reset jointly within the window | UNOBTANIUM-WITH-PARAMETERS | exp-036 |
| TPA-cascade FCA (Si/GaAs/ZnSe/CdS) | Bounded by TPA's own gap, no independent channel | Inherits TPA's 9–11 OOM gap; residual 3–6 OOM even under generous field-enhancement | UNOBTANIUM-WITH-PARAMETERS | exp-037 |
| Linearly-pumped FCA (doped Si/Ge) | 1–9 OOM short depending on doping (Si, quantitative, Soref & Bennett 1987); Ge qualitative-only | Clears easily (no threshold) | UNOBTANIUM-WITH-PARAMETERS | exp-037 |
| ENZ (ITO/AZO) | Dominantly refractive (Δε_real) — does not reduce to a D_req/σ(I) comparison at all; separate Δε_imag branch found, magnitude unresolved | ~11–14 OOM above ceiling (GW/cm²-class pulsed only); residual 5–9 OOM even under generous field-enhancement | UNOBTANIUM-WITH-PARAMETERS (irradiance/wavelength) + MECHANISM-CLASS-DISQUALIFIED (dominant effect is not σ(I) at all — a new instance of R1's principle, LOGBOOK.md) | exp-037 |
| Graphene | Wrong direction (saturable, not reverse-saturable) — confirmed, not a candidate class | N/A | RULED OUT (wrong mechanism direction) | exp-037 |
| Combined SA+RSA media (tandem/dyad/composite) | Best composite figures ~10×–267×; ~0.65–2.1 orders short of the bound (corrected, exp-037 Red Team audit — not "2–4+" as first published) | No CW figure found for any architecture (pulsed-fluence literature only); no long-triplet-RSA-based architecture found in the literature | UNOBTANIUM-WITH-PARAMETERS, with a "motivation mismatch" caveat (the literature's own design goal is pulsed-laser-damage protection, not CW ambient-silhouette suppression) | exp-037 |

**Net: nine named classes/sub-classes now checked (RSA, TPA, photochromic,
VO2, TPA-cascade FCA, linearly-pumped FCA, ENZ, graphene, combined media);
every one fails, each via a distinct or partially-shared gap** —
predominantly dynamic range and/or irradiance, with ENZ additionally
failing on expressibility (not a σ(I) mechanism at all in its dominant
form) and graphene failing on wrong direction entirely. **This is NOT yet
a Checkpoint criterion 2 finding** — two independent reasons, both live:
(1) the evidentiary tier across every literature-check cycle to date
(exp-036, exp-037) remains WebSearch-snippet synthesis (39+ consecutive
WebFetch attempts blocked across three cycles), not primary-source-
verified, short of "gates clean"; (2) this table's own scope is bounded by
the specific named sub-classes and architectures each cycle chose to
search — a materials space this open-ended cannot be certified exhaustive
by any finite literature check, only bounded more and more tightly with
each cycle (this memo's own standing limit, unchanged since Iteration 11).
**Field-enhancement caveat (exp-037, MATERIALS' own arithmetic,
Red-Team-audited):** even generous published sub-wavelength plasmonic/
cavity field-enhancement factors (10²–10⁶×) leave residual irradiance
gaps of 3–9 orders of magnitude for the two rows checked (ENZ, TPA-cascade
FCA) — and such enhancement is inherently sub-wavelength-volume and
narrowband, incompatible with this program's macroscopic-beam/broadband-3λ
requirement, a third independent reason these specific rows stay
unobtainium even under generous assumptions.

## What the bench has established (this program's own numbers, cited)

The T1 escape route this program has instrumented — intensity-gated
absorption σ(I) — requires a real material whose absorption cross-section
switches between two states:

- **OFF state**: σ_off, weak enough that a swept beam's ambient silhouette
  stays below VISION's frozen photopic lab bar (|C| < 0.005). The
  best-characterized OFF article is τ_off = 0.0065 (exp-032's `off_pass`),
  the only σ(I) OFF-state configuration in this program's history to clear
  that bar at bench scale (r=78-native) — though Iteration 11 (this cycle)
  found that clearance downgrades to MARGINAL at r=156 and is not yet
  cleanly resolution/domain-established even at r=78 (see NOTES.md).
- **ON state**: τ_on ≈ 3.9 (exp-001's established beam-behind ≤ 2% bar).

**Dynamic range required, D_req = σ_on/σ_off:** algebraically
R_OUT-independent (τ is held fixed by construction across every geometry
this program has built — confirmed independently by both MATERIALS and
Red Team this cycle). Two published figures exist in this program's
record depending on which OFF-state article anchors the ratio:
τ_on/τ_off = 3.9/0.0065 = **600.0×** (off_pass, exp-032/034); a related
geometric-chord-model figure, D_req = g₀·τ_on/C̄ ≈ **537×**, was derived at
Iteration 9 using the bench's own g₀ calibration constant. Both sit in the
same 537–600× band; this memo treats **≈540–600×** as the working
dynamic-range target.

**Irradiance regime:** the mechanism must switch at the flashlight beam's
own intensity, order **~10⁻³ W/cm²** (witness arithmetic, established
Iteration 1: a household flashlight beam, several watts over a
few-cm² aperture, attenuated somewhat by throw distance — an order-of-
magnitude estimate, not a metered figure, and itself a candidate for a
future sourced witness-parameter table, docket #7).

## Candidate real material classes (informal desk synthesis)

**Reverse saturable absorbers (RSA)** — materials (metal phthalocyanines,
C₆₀ and other fullerenes, some porphyrins) whose absorption cross-section
*increases* with intensity via excited-state absorption exceeding
ground-state absorption. This is the correct-DIRECTION class: absorption
gates UP with intensity, matching σ(I) with σ_on > σ_off. MATERIALS' own
Iteration-9 informal check found published nonlinear-transmission
enhancement factors of **roughly 2–10×**, "occasionally a few tens of ×"
in favorable geometries (thick cells, resonant pump wavelengths) — this
memo does not improve on that figure with a fresh literature pull, but
notes it is **consistent with the general RSA literature's typical
reported dynamic range**, which rarely exceeds ~50–100× even in
specialized nonlinear-transmission demonstrations. **Against the 540–600×
target: 1–2 orders of magnitude short.**

**Two-photon absorption (TPA)** — σ(I) = σ₁ + σ₂·I, a genuinely
intensity-proportional (n=1) absorption channel, the mechanism class this
program's own T1 thread names as clearing the required exponent (n ≳
0.56–0.8, Tier-A; n ≳ 0.3, Tier-W) with the most margin. TPA's practical
switching range is bounded by two facts, not one: (a) the *linear*
background absorption σ₁ must itself be low enough to satisfy σ_off (TPA
media are typically chosen to be linearly transparent at the operating
wavelength, which is favorable — σ_off can in principle be made very
small); but (b) the *nonlinear* term σ₂·I only becomes comparable to a
useful σ_on at **irradiances where two-photon processes are
experimentally significant**, which for typical TPA cross-sections
(1–1000 GM, Göppert-Mayer units, 1 GM = 10⁻⁵⁰ cm⁴·s·photon⁻¹) and
realistic number densities sit at **~10⁶–10⁹ W/cm²** for meaningful
absorption depths — the figure this program's own LOGBOOK (T1, Iteration
10) already cites. **Against the flashlight's own ~10⁻³ W/cm²: a 9–12
order-of-magnitude gap.** This is not a dynamic-range problem (TPA's
intensity-proportional response is structurally well-suited to n≈1) —
it is an **absolute-threshold problem**: TPA-class media that respond
meaningfully at flashlight intensities are not a documented regime in the
nonlinear-optics literature this memo is aware of; the mechanism exists,
but not at this irradiance, by many orders of magnitude.

## Verdict (MATERIALS' own charter: published / plausible / unobtainium-with-parameters)

**UNOBTANIUM-WITH-PARAMETERS — for BOTH candidate classes, for two
independent reasons that do not trade off against each other:**

1. **RSA**: dynamic range 1–2 orders of magnitude short of the ≈540–600×
   target, independent of irradiance. A material with 10× *more*
   dynamic range than any RSA this memo is aware of would still need to
   clear 540–600×, not close the remaining gap partway.
2. **TPA**: dynamic range is not the binding constraint (n≈1 comfortably
   clears the exponent bars), but the operating irradiance is 9–12 orders
   of magnitude below where TPA-class materials show meaningful response
   in the literature. No incremental materials improvement plausibly
   closes a 9–12 OOM gap — this is the kind of gap that historically
   signals a wrong mechanism class, not an engineering target.

**Neither escape route has a named, published material sitting even
loosely near BOTH constraints simultaneously.** This does not rule out
σ(I) as a *formal* mechanism class (T1's own latitude rule: exotic
mechanisms are permitted if stated as concrete, testable parameters) —
but it substantially sharpens what "plausible" would require: either an
RSA-class material with an order-of-magnitude-better dynamic range than
anything in this informal survey, operating at an irradiance regime
9–12 orders of magnitude below where such nonlinearities are normally
observed — i.e., two separate, uncorrelated, order(s)-of-magnitude
advances in the same material, not incremental progress on either axis
alone.

## Candidate for PANEL.md Checkpoint criterion 2

Per Red Team's Phase-5 ruling (Iteration 11): this gap is a genuine
candidate for Checkpoint criterion 2 (**a proven boundary: a constraint
subset shown jointly unsatisfiable within a whole mechanism class, gates
clean**) — but does not yet fire it. What would fire it: a dedicated,
sourced check (not this desk memo) establishing that no published or
physically-plausible RSA/TPA-class material can simultaneously satisfy
D_req ≥ 540× and an operating irradiance ≤ 10⁻² W/cm² (two orders above
the flashlight's own estimate, a generous margin), across the full
published parameter space of both material classes — a genuine
literature review, not an informal synthesis, and ideally with a third,
independent material class considered (e.g. photochromic/photothermal
switching, considered and not yet evaluated by this memo).

## Idealizations and honest limits of this memo

Not a rigorous, citation-backed literature survey — a desk synthesis of
numbers already informally gathered by this program (MATERIALS'
Iteration-9 RSA check) plus general nonlinear-optics domain knowledge
about TPA cross-section magnitudes and typical operating irradiances,
explicitly flagged as such. No primary sources are cited with DOIs or
specific material names beyond broad classes. The witness irradiance
estimate (~10⁻³ W/cm²) is itself an order-of-magnitude estimate pending
docket #7's own sourced parameter table. **As originally written (Iteration
11), this memo considered only RSA and TPA; per Amendment 2 above
(Iteration 14), all classes it named as not-yet-evaluated have since been
checked (exp-036, exp-037), consolidated in Amendment 2's table.** The
open-endedness this paragraph originally flagged persists at a narrower
scope: exotic/engineered composite or metamaterial-hybrid media beyond the
specific architectures exp-037 named, and any mechanism class no cycle to
date has thought to name at all, remain unevaluated and could plausibly
change any single row's verdict — though the pattern across nine now-
checked classes (uniform failure via dynamic-range and/or irradiance
gaps of 1 to 14 orders of magnitude) makes a class clearing all bounds
simultaneously a narrowing, not widening, possibility with each cycle.
