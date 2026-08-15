# MATERIALS' realizability memo — the σ(I) switching mechanism vs published nonlinear-absorber physics

Panel Iteration 11 close-out, mandatory fix 7 (Red Team's Phase-5 audit).
Zero FDTD cost — a desk synthesis of this program's own established
numbers against published nonlinear-optics literature, informal (as
MATERIALS' own Iteration-9 check was self-flagged), not a rigorous survey.
Named as an open deliverable at the close of Iterations 9, 10, and 11 — a
three-cycle deferral this closes.

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
docket #7's own sourced parameter table. This memo considers only RSA and
TPA — the two classes this program's own record has already named; other
nonlinear-absorption mechanisms (free-carrier absorption in
semiconductors, photochromic switching, saturable-then-reverse-saturable
combined media) are not evaluated and could plausibly change this
verdict in either direction.
