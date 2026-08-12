# exp-020 — The Ambient-Appearance Baseline (panel Iteration 1)

**2026-08-12 · driver: Clyde as panel Director · status: predictions
committed, instrument not yet built, nothing run**

First experiment of the panel program (PANEL.md / LOGBOOK.md). Constraint 3
— "not a black silhouette under ambient light" — has never been a number on
this bench. Iteration 1's panel (LOGBOOK, Iteration 1 entry) proposed the
instrument (Vision Science, lead), critiqued it five ways, and Red Team
returned proceed-with-mandatory-fixes. This file is the **Phase-3
synthesis**: one testable configuration, the panel's criticisms resolved on
the record, predictions committed before the first run.

## Marsh's ruling (Checkpoint #0): constraint 3 scores as two tiers

- **Tier W — witness-reproduced:** the four constraints hold in the reported
  scene's own regime (night ambient; observer = the flashlight holder,
  adaptation state including self-glare once pinned). Checkpoint-worthy
  alone.
- **Tier A — invisible-to-anyone:** holds for any observer and adaptation,
  photopic included. The strict stretch goal.

Every run records the quantities both tiers need. **exp-020 scores Tier A
only** (photopic verdict + scotopic crossover bands); Tier W's verdict is
explicitly deferred until the witness-scenario parameter table exists
(docket #7) — the glare route stays hypothesis-not-result (docket #6).

## Synthesis — the panel's demands, resolved

Accepted in full (docket #1–#3, #5–#9): pinned oblique geometry with the
published design calculation (`design_geometry.py`, committed alongside this
file — run it, the numbers below are its output); re-derived threshold
crossovers spanning the exponent uncertainty; the gate-vs-PASS-bar collision
resolved via a committed decision floor; the dilute-sponge third article;
glare demoted to hypothesis; the σ(I) design window logged as bands with the
bar convention attached; the two-tier ruling above.

Accepted with amendments, reasons stated:

1. **Windows re-registered** (EM's lever-arm catch, extended): max oblique
   shadow reach = 93·tan40° + 78/cos40° = **180 cells**, so the proposal's
   flank inner edge (117) sat inside the 40° penumbra. Flanks move to
   [185, 263] relative; guard (78, 185]. Consequence: flanks are true
   background at every committed angle (design calc: max reach 179.9,
   inside 185 by 5 cells — tight, stated).
2. **Domain 360×1200** (not the proposal's 560×560): the walk-off arithmetic
   (D_source→plane = 223, walk at ±40° = 187 cells) plus the 526-cell
   analysis span forces transverse ny = 1200 for full flat-source coverage
   at all 17 angles (min margin 69.9 cells, design calc). The proposal's
   "exp-001 numerics unchanged" rationale is deleted as Red Team required —
   comparability lives in Δ = 30 nm, cpl, courant, and the article builders,
   not the domain shape.
3. **Energy + intensity ledger lands experiment-side** (thermo + quantum,
   docket #4, amended): every run records the closed-box σ_abs / σ_ext
   (both routes) via `sections.widths`, i_inc at the object position, and
   raw source amplitude (1.0, exp-001's unit) in `results.json`. The
   absolute anchors: empty-scene box net flux ≈ 0, and two-route σ_ext
   agreement on object runs. The formal artifact-schema bump this implies
   is **deferred to a counterparty-review PR** — `lab/ARTIFACTS.md` and
   `lab/artifacts.py` are the cross-lane contract (Bonnie's veto lane,
   AGENTS.md), and the panel does not amend contracts unilaterally. TODO
   recorded in PLAN.md.
4. **Suite stage 9 runs a small tall scene (360×520, angles {0, ±15, ±30})**
   rather than the full ±40° geometry: suite stages anchor physics
   identities on small scenes (stages 6–8 precedent); the ±40° coverage
   gate lives HERE, in the experiment harness, pre-registered as P1b and
   demonstrated on the real 360×1200 empty scenes. Rationale: CI runtime;
   the physics gates (phase-ramp wavelength, oblique energy identity,
   incoherent-sum bookkeeping) do not need 40° to catch bugs.
5. **Equal-flux weighting is primary** (proposal's own choice, kept; cosine
   Lambertian re-weight reported alongside — free post-processing of the
   same runs).

Overridden, with reasons: none. Every mandatory fix is implemented or
explicitly deferred-with-owner above.

## Setup (pinned by `design_geometry.py` — re-run it if any constant moves)

| Knob | Value |
|---|---|
| Grid | Δ = 30 nm · **360 × 1200** cells · courant 0.99 · absorb 40 |
| Wavelengths | 450 / 600 / 750 nm (cpl 15 / 20 / 25), per-λ reporting + V/V′ weighting |
| Ambient | far-side line source x = 300, y ∈ [40, 1160], taper 40; angles θ ∈ {0, ±10, ±20, ±30, ±40}°, one CW run per (θ, λ), intensities summed post-hoc; per-component normalization: empty flank mean → 1 |
| Articles (4) | empty · absorber = PEC core r=30 + `graded_black_shell` 30→78 (stage-7 config) · PEC disk r=78 · dilute sponge disk r=78, ε=1, uniform σ = 6.41×10⁻⁴ (center-chord τ = 0.10) |
| Object center | (170, 600) |
| Measurement plane | x = 77 (15 cells observer-side of the edge; lever to object center 93); sensitivity rows at 12 and 16 cells |
| Quantity | B(y) = observer-directed per-cell time-averaged flux (quadrature phasors, `sections` conventions) |
| Windows | object |y−600| ≤ 78 · guard (78, 185] · flanks [185, 263], both sides |
| Contrast | C = (B̄_obj − B̄_flank)/B̄_flank on the weighted incoherent sum; per λ + V/V′ |
| Convergence | N=5 subset {0,±20,±40} vs N=9 (free); N=17 adds ±5,±15,±25,±35 (empty + PEC @600 nm) |
| Ledger (every run) | σ_abs, σ_ext (both routes), i_inc, source amplitude, box net-flux residual |
| Runs | 4 × 9 × 3 = 108 + 16 convergence = **124** |

Geometric ceilings from the ray trace (committed inputs to the bands):
opaque articles C_geo = −0.799 (equal) / −0.809 (cos); per-angle object
coverage 65–100%; sponge C_geo = −0.063; Fresnel numbers 4.4 / 3.3 / 2.6 at
450/600/750 nm (diffraction fills shadows → measured |C| below |C_geo|,
more fill toward red).

## Frozen thresholds (corrected per Red Team #2 — the scoring table)

Committed function: C_thr(L) = 0.005 · max[1, (L / 3 cd·m⁻²)^(−p)], clipped
at 1, exponent band p ∈ [0.4, 0.5]; field factor ×4 (uncued observer).
Photopic bars: lab 0.005, field 0.02 (Blackwell 1946; CIE 19/2; Adrian
1989). Crossovers for a perfect absorber (|C| = 1), re-derived from the
function itself:

- **L\*_lab ∈ [5.3×10⁻⁶, 7.5×10⁻⁵] cd/m²** (p = 0.4 → 0.5)
- **L\*_field ∈ [1.7×10⁻⁴, 1.2×10⁻³] cd/m²**

Corrected committed reading (replaces the proposal's): the field-bar
crossover **spans and exceeds** the moonless rural sky reference
(1.7×10⁻⁴ cd/m²) — an *uncued* observer is at or past threshold on typical
moonless nights; a *cued, dark-adapted* observer still detects the
silhouette at every natural night ambient except the extreme dark floor.
Darkness alone hides this object only from the inattentive; the Tier-W
question (the glare-adapted flashlight holder) stays open pending docket #7.

## Predictions — committed before the instrument is built or any run

- **P1a (empty identity / decision floor):** |C_empty| ≤ 0.005 at every λ,
  both weightings. The measured max defines the decision floor δ_C; every C
  is reported ±δ_C; a PASS verdict at either bar is decidable only if
  δ_C < that bar. Empty B(y) flat to ±5% across the analysis span at θ = 0
  and ±40°.
- **P1b (coverage gate, the design calc's empirical half):** the ±40° empty
  runs light the full analysis span (no window mean below 0.8× the span
  median) — if this fails, the geometry pinning failed and no object number
  is interpreted.
- **P2 (absorber):** C ∈ [−0.82, −0.55] at every λ and both weightings,
  central ≈ −0.70. Falsifiable λ-ordering from the Fresnel numbers:
  |C(450)| ≥ |C(600)| ≥ |C(750)| (diffraction fill grows toward red).
  Tier-A verdict encoded: photopic constraint-3 **FAIL** by ≥ 27× the field
  bar (|C| ≥ 0.55 vs 0.02) and ≥ 110× the lab bar.
- **P3 (PEC control, material blindness):** C ∈ [−0.82, −0.55];
  |C_PEC − C_absorber| ≤ 0.15 per λ — a mirror and a black body read as the
  same dark hole in back-light (extinction, not albedo). Distinguishing
  them is the deferred front-lit channel's job.
- **P4 (dilute sponge, the mid-scale calibration):** C ∈ [−0.10, −0.03]
  (geometric −0.063); agreement with the committed Beer–Lambert window
  model within ±0.03 absolute. This is the instrument's first point in the
  regime every future sub-threshold mechanism occupies.
- **P5 (convergence + plane sensitivity):** |C(N9) − C(N5)| ≤ 0.05 on all
  articles; |C(N17) − C(N9)| ≤ 0.02 (empty + PEC @600); |ΔC| across planes
  12/15/16 ≤ 0.05.
- **P6 (ledger identities):** empty-scene box net flux within ±2% of zero
  (relative to the absorber run's σ_abs·i_inc scale); two-route σ_ext
  agreement ≤ 12% on every object run (stage-8 tolerance, now at oblique
  incidence); absorber σ_abs/σ_ext ≥ 0.45 at θ = 0 (stage-8 consistency).
- **P7 (scotopic crossover, derived — the falsifiable part is C):** the
  measured absorber C, pushed through the frozen threshold function, puts
  the Tier-A scotopic crossover inside L\*_lab ∈ [5×10⁻⁶, 8×10⁻⁵] cd/m²;
  the conclusion text above (uncued-at-threshold on moonless nights, cued
  observer sees it) survives contact with the measured value.

## Idealizations (lab convention)

2D TMz, one polarization; CW single-λ, 3-λ quadrature for white light;
ambient = 9 discrete incoherent plane waves over ±40° back-light only
(hemispheric and front-lit illumination not represented — |C| is an
upper bound in angle-span and a lower bound in object scale, both stated in
the proposal's limits (i)–(viii), adopted verbatim); linear media only —
per-component normalization and post-hoc summation are the linear-media
idiom (quantum seat), labeled here and in the code; graded damping bands,
not PML; window means on a near virtual plane, no imaging optics or eye
model — perception enters only through the frozen threshold table;
perceptual bars assume extended-target foveal detection (Blackwell
conditions), the hardest case for hiding.

## Run plan

1. Build instrument (`angle_deg` source + `sections.flux_profile_x` +
   `lab/ambient.py`) with trust-suite **stage 9** — green before any
   exp-020 run, alongside stages 1–8 (no regression).
2. 124 runs (~1 h at bench pace); results table + per-run ledger to
   `results.json`; B(y) profile PNGs per article.
3. Score P1–P7 in this file; ambient-appearance row into LOGBOOK
   (Iteration 1, Phase 4); panel Phase-5 review follows.

## Next (pre-registered)

Phase 5 owns the ranked directions, but two items are already on the
docket for it: the witness-scenario parameter table (docket #7 — unblocks
Tier-W scoring and the glare hypothesis test), and the front-lit
reflectance channel (the PEC-vs-absorber discriminator this back-lit
baseline deliberately cannot see).
