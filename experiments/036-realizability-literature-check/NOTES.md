# exp-036 — The Rigorous RSA/TPA/Photochromic-Photothermal Literature Check

Panel Iteration 13 · Runner: cloud panel shift · Lead: VISION SCIENCE (rotation)

Full seven-seat cycle: Phase 1 proposal (VISION SCIENCE) → 5 blind parallel
critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM
OPTICS) → Red Team last with everything (verdict:
**proceed-with-mandatory-fixes**, 7 numbered attacks, all 7 fix-docket
items accepted by the Director, none overridden) → Phase 3 synthesis
(this file) → predictions committed here, before any search runs → Phase 4
literature search. Verbatim panel transcript: `LOGBOOK.md` Iteration 13.

## Hypothesis

Iteration 12 (exp-035) closed with Red Team's explicit re-ranking of
Iteration 13's priorities: the rigorous RSA/TPA/third-mechanism-class
literature check outranks every further FDTD refinement of the
ambient-contrast channel, because that channel's own Phase-5 record calls
it "algebraically orthogonal" to the realizability question. This is the
first zero-FDTD-cost cycle in the panel's history whose entire "run" is a
literature search rather than a simulation. The pre-registered hypothesis:
no published, real material class (reverse saturable absorption, two-photon
absorption, or photochromic/photothermal switching) simultaneously clears
the dynamic-range (D_req ≥ 540–600×, now a *lower* bound per Iteration 12),
irradiance (≤10⁻² W/cm², a generous two-order margin over the ~10⁻³ W/cm²
witness estimate), and switching-speed (10ms–1s, both directions,
unsourced) bounds this program has established — but each class is
predicted to fail via a **different, non-overlapping physical gap**, which
if confirmed is a genuine boundary-mapping result even though it does not,
by itself, fire Checkpoint criterion 2 (a fourth named class, free-carrier
absorption, and a fifth, combined saturable/RSA media, remain untested).

## Phase 1 — Proposal (VISION SCIENCE, abridged)

Full verbatim proposal: LOGBOOK.md Iteration 13 / this repo's
`/tmp` scratch history is not committed — the text below is the
as-committed version, folding in all Phase-2 mandatory fixes (see Parameter
tables). Original framing: three mechanism classes (RSA, TPA, photochromic/
photothermal), searched via review-level sources (≥2 independent per class),
extracting ON/OFF ratio or ΔOD, operating intensity (unit-normalized to
W/cm², CW-vs-pulsed flagged), and forward/reverse switching time constants —
the last axis new to this program, addressing constraint 4 directly.
Photochromic/photothermal named families: diarylethenes, spiropyrans/
spirooxazines, fulgides, azobenzenes (T-type vs P-type reversibility
distinguished), VO2/phase-change. RSA families: metal phthalocyanines,
C60/C70 fullerenes, porphyrins, Pt/Ir-acetylide organometallics, carbon
nanotubes. TPA families: TPA-active organic chromophores, direct-gap
semiconductor TPA coefficients (ZnSe, GaAs).

## Phase 2 — Critique (five blind, then Red Team) — summary

Full verbatim critiques: LOGBOOK.md Iteration 13. All five blind seats
independently returned **support-with-changes** — no verdict conflict, but
five non-overlapping substantive fixes:

- **PHOTONICS** caught a real unit/quantity error before it happened: the
  proposal's own photochromic dynamic-range comparison would have scored a
  film ΔOD figure (sample-specific, Δτ) directly against D_req (a
  sample-independent cross-section ratio, σ_on/σ_off) — apples to oranges,
  and in the wrong direction to boot (a small literature-sample τ_off could
  make the same ΔOD imply a MUCH larger true ratio than the flat "10–100×"
  read suggested). Mandatory: extract intrinsic ε_colored/ε_bleached, not
  film ΔOD, before scoring; tag every figure's wavelength against this
  program's 450/600/750nm sweep.
- **MATERIALS** (this thread's own prior author) found the proposal
  silently narrowed its own memo's four named-unevaluated classes to
  three — free-carrier absorption dropped on cost grounds, not physics, and
  a "combined saturable/RSA media" class vanished with no disclosure at
  all. Real risk: a clean three-class UNOBTANIUM sweep could be read as
  firing Checkpoint criterion 2 when it hasn't earned that yet.
- **ELECTROMAGNETISM** found the single most consequential catch of the
  cycle: photochromic/photothermal absorption is not T1's σ(x,t)
  (externally time-switched) escape route at all — it's a **hysteretic
  σ(I) with memory**, still driven by the same light field integrated over
  a rate-equation kernel. That reclassification matters because it exposes
  a genuinely new constraint-3 risk this program's LOGBOOK has never named
  in eleven prior iterations: **continuous ambient light alone, with no
  flashlight present, could drive a photochromic to a non-trivial
  steady-state colored population** — a silhouette-at-rest failure mode,
  independent of anything the flashlight does.
- **THERMODYNAMICS** found the photothermal (VO2) row was being scored
  with the same "irradiance clears easily" verdict as molecular
  photochromics, on the strength of an irrelevant precedent (photochromic
  eyewear responds to ambient UV, VO2 needs bulk heating through a
  ~40–70K phase-transition span). Mandatory: split the VO2 row out, and
  check — analytically, using this program's own established T5 power
  budget, capped at one back-of-envelope estimate — whether flashlight-
  level absorbed power density can plausibly drive AND passively cool a
  VO2 transition inside the proposal's own dwell/reset windows.
- **QUANTUM OPTICS** found the proposal never converts its dynamic-range
  RATIO into an absolute cross-section a real material must supply, and
  flagged that this program's own established σ_abs/σ_ext ≈ 0.51–0.61
  (the bench's extinction is only partly pure absorption; RSA/TPA/
  photochromic mechanisms are absorption-only, with no engineered
  scattering assist) means a real material's σ_on must be ~1.6–2× the
  bench's nominal figure — tightening every D_req comparison further.

**Red Team (PROCEED-WITH-MANDATORY-FIXES).** All five critiques accepted
in substance; none in conflict. Confirmed EM's constraint-3-at-rest catch
as genuinely novel (grep-verified: "photochromic" and "hysteretic" appear
nowhere in LOGBOOK.md before this cycle) and load-bearing — PANEL.md names
constraint 3 "the hard one, do not let it slip," and a class that quietly
fails at rest under ordinary ambient light, with no flashlight involved at
all, is exactly that failure mode. Ruled MATERIALS' FCA gap real but not
worth expanding this cycle's scope to a fourth full search — instead
required the write-up to explicitly disclose that Checkpoint criterion 2
does NOT fire regardless of outcome, naming both untested classes (FCA and
combined media) by name, not by omission. Capped THERMODYNAMICS' power-
budget check at one analytic estimate, explicitly barring a THERMO-sidecar-
style rebuild. Sequenced PHOTONICS' and QUANTUM's fixes (extract intrinsic
ε first, THEN apply the absorption-only correction — applying the
correction to a raw film ΔOD compounds one error on another). Added one
new attack of its own: any "switching speed clears" finding is checked
against an unsourced 10ms–1s band, not the eye — the actual gating
instrument (T3's flicker/temporal-contrast threshold) is still unbuilt
(stage-10) — so any such finding must carry that caveat explicitly, not as
a settled perceptual result.

**Director's synthesis: all seven mandatory-fix items accepted in full, none
overridden.** Red Team's docket was itself already an adjudication of five
non-conflicting seat critiques with sound reasoning throughout (cost
discipline on THERMO's and MATERIALS' items; correct sequencing on
PHOTONICS'/QUANTUM's; a genuinely new, load-bearing catch on EM's) — there
was nothing in it that warranted a Director override.

## Parameter tables

**Quantitative bounds under test:**

| Bound | Value | Source |
|---|---|---|
| D_req (dynamic range σ_on/σ_off) | **≥ 540–600×**, a LOWER bound (Iteration 12 amendment) | REALIZABILITY_MEMO.md; LOGBOOK T1 |
| Irradiance ceiling (witness estimate) | ~10⁻³ W/cm² | LOGBOOK T1, Iteration 1 |
| Irradiance ceiling (Checkpoint-2 firing margin) | ≤ 10⁻² W/cm² | REALIZABILITY_MEMO.md |
| Switching-speed requirement (unsourced, this cycle's own addition) | ~10ms–1s, both directions — **flag every verdict against this band as provisional pending T3** (stage-10 instrument, unbuilt) | derived this cycle; Red Team fix 7 |
| Absorption-only correction factor | σ_on(real, absorption-only) ≈ σ_on(bench, extinction) / 0.51–0.61 | LOGBOOK ESTABLISHED (σ_abs/σ_ext); QUANTUM fix 6 |

**Mechanism classes in scope (four rows, VO2 split from photochromic per
THERMO's mandatory fix):**

1. **RSA** (metal phthalocyanines, C60/C70, porphyrins, Pt/Ir-acetylide
   organometallics, carbon nanotubes).
2. **TPA** (organic chromophores, ZnSe/GaAs-class direct-gap
   semiconductors).
3. **Photochromic (photochemical)** — diarylethenes, spiropyrans/
   spirooxazines, fulgides, azobenzenes; T-type vs P-type reversibility
   distinguished explicitly.
4. **Photothermal (VO2 / phase-change)** — scored separately from (3);
   requires the T5-power-budget sub-check (PHOTONICS'/THERMO's fixes).

**Explicitly out of scope, named not silently dropped (MATERIALS' fix,
Red-Team-capped):** free-carrier absorption (FCA) and combined saturable/
RSA media — both remain untested. **Checkpoint criterion 2 does NOT fire
this cycle regardless of outcome**, precisely because these two classes
are undone.

**Search methodology, unchanged from Phase 1, now with mandatory
extraction discipline:**

- Prioritize review-level sources over single primary papers; ≥2
  independent sources per class before a figure counts as "the literature
  says," not "one paper reports."
- Extract, per class: (i) intrinsic ε_colored/ε_bleached or σ_on/σ_off —
  **not** film-specific ΔOD (PHOTONICS' fix) — converted where possible to
  the absolute, absorption-only-corrected figure (QUANTUM's fix, sequenced
  after extraction); (ii) operating intensity/fluence, unit-normalized to
  W/cm², CW-vs-pulsed flagged explicitly; (iii) forward AND reverse
  response time constants.
- **New, mandatory (EM's fix):** for the photochromic/photothermal rows,
  additionally extract published photostationary-state population or
  coloration fraction under continuous, ambient-comparable illumination
  (no pulsed/flashlight-level excitation) — the constraint-3-at-rest check.
- **New, mandatory (THERMO's fix, capped):** for the photothermal (VO2)
  row only, one back-of-envelope lumped thermal-mass/diffusion-time
  estimate — using this program's own T5 power budget (~1W diffused over a
  ~m-scale volume, ~10⁻³ W/cm²) and published VO2 thermal diffusivity —
  testing whether flashlight-level absorbed power density can plausibly
  drive AND passively cool a transition inside the proposal's dwell/reset
  windows. Explicitly capped: no new FDTD thread, no THERMO-sidecar
  rebuild.

## T1 escape-route statement

Bears directly on **σ(I)** (RSA, TPA — genuinely intensity-self-gating).
**Corrected per EM's mandatory fix**: photochromic/photothermal switching
is **not** T1's σ(x,t) (externally time-switched) escape route — it is a
**hysteretic σ(I) with memory** (a rate-equation kernel integrating dose or
heat over time), a mechanism sub-class this program has never previously
named or checked. This produces the first literature-grounded data point
for that hysteretic sub-class, and — per EM's own catch — the first
explicit test of whether such a mechanism can violate constraint 3 *at
rest*, independent of the flashlight.

## Predicted outcomes (falsifiable bands, committed BEFORE any search)

| Class | (a) D_req ≥ 540–600×? | (b) irradiance ≤ 10⁻² W/cm²? | (c) switching speed 10ms–1s both directions? [provisional vs T3] | (d) constraint-3-at-rest: detectable steady-state colored fraction under continuous ambient light, no flashlight? | **Predicted verdict** |
|---|---|---|---|---|---|
| **RSA** | Predict NO — published enhancement factors cluster 2–10×, rarely "tens of ×"; a rigorous search finds at most a handful of outlier papers above 100×, none credibly above 500×. The absorption-only correction (÷0.51–0.61) makes this gap look larger still once applied, not smaller. | Predict YES, clears easily | Predict YES, clears easily (ns–µs excited-state lifetimes) | N/A — RSA has no ground state persistently populated by ambient light the way a photochromic isomer is; predict no detectable at-rest signature | **published-partial**: dynamic range is the sole, unclosed gap |
| **TPA** | Predict YES, clears comfortably (n≈1 structurally suited) | Predict NO — published TPA onset thresholds cluster 10⁶–10⁹ W/cm², 8–12 orders above the ceiling even with the generous margin | Predict YES, clears trivially (sub-ps virtual-state process) | N/A — same reasoning as RSA | **unobtainium**: irradiance gap dominates, expected un-shrunk by a rigorous search |
| **Photochromic (photochemical)** | Predict NO once intrinsic ε_colored/ε_bleached is correctly extracted — most durable, thermally-reversible (T-type) systems read as ΔOD~1–2 in typical films, translating to an intrinsic ratio still 1–2 orders of magnitude short of 540–600×, though PHOTONICS' own attack means this could in principle come back higher for a low-τ_off sample — genuinely open, not assumed | Predict YES, clears easily (ambient/sunlight-level UV-visible operation is these materials' whole commercial premise) | **Predict NO for the reverse (OFF) leg specifically** — T-type thermal bleaching commonly reported seconds-to-minutes; P-type systems that switch fast don't reverse passively at all | **Predict YES — detectable steady-state coloration under continuous ambient light is expected for at least one commonly-cited T-type system** (the same slow-reset kinetics that fails (c) predict a non-trivial photostationary population under any sustained illumination, ambient included) — this is the cycle's sharpest, most novel falsifiable claim | **published-partial, with a NEW binding failure**: reverse-switching speed AND a possible constraint-3-at-rest failure, not dynamic range, are predicted to be decisive |
| **Photothermal (VO2)** | Not the binding constraint if (b) fails | Predict NO — published VO2 switching is almost universally measured under concentrated pulsed/resistive heating (MW–GW/cm²-class), not diffuse flashlight-level CW fluence; predict the T5-power-budget estimate shows the flashlight cannot raise the absorbing volume through the ~40–70K transition span within any practical dwell time, AND that passive cooling/reset via thermal diffusion at cm–m scale is order seconds-to-minutes, outside the 10ms–1s window regardless of heating feasibility | Predicted moot given (b)'s failure, but for completeness: predict reset fails independently on diffusion-time grounds even in a hypothetical high-power variant | Predict NO detectable at-rest signature — VO2's transition requires sustained bulk heating past a sharp threshold; ambient-level flux alone is not expected to sustain the transition temperature | **unobtainium**: a second, independent irradiance/power-budget failure, mechanistically distinct from TPA's quantum-threshold failure (bulk thermal vs. quantum nonlinear) |

**Program-level pre-registered prediction:** no class clears all bounds
simultaneously; the four classes are predicted to fail via **three or four
structurally distinct primary gaps** — RSA (dynamic range), TPA (quantum
irradiance threshold), photochromic (reverse-switch speed, possibly
compounded by an at-rest constraint-3 failure), VO2 (thermal power-budget/
diffusion-time, a mechanistically distinct irradiance failure from TPA's).
If confirmed, this is a genuine boundary-mapping result — but **does NOT
fire Checkpoint criterion 2**, since free-carrier absorption and combined
saturable/RSA media remain untested (Red Team's mandatory disclosure,
accepted in full). Any switching-speed verdict is provisional against the
unsourced 10ms–1s band, not a settled perceptual finding, pending T3's
still-unbuilt instrument.

## Idealizations

- **Proprietary/unpublished materials are invisible to this check by
  construction.** Classified, patent-only, or trade-secret optical-
  limiting work could sit anywhere relative to these bounds.
- **Exotic/engineered composite or metamaterial-hybrid nonlinear media are
  out of scope** — a materials-engineering-roadmap question, not a
  literature-survey one.
- **The switching-speed band (10ms–1s) is an unsourced witness estimate**,
  the same evidentiary status as the ~10⁻³ W/cm² irradiance figure —
  pending docket #7's still-unbuilt sourced witness-parameter table.
- **This is a search, not a lab measurement or formal meta-analysis.** No
  extracted number is independently re-verified; a review article's own
  reported range is trusted as reported. Publication bias could bias any
  single class's apparent ceiling upward.
- **Free-carrier absorption and combined saturable/RSA media are
  explicitly untested this cycle** — Checkpoint criterion 2 cannot fire
  regardless of this cycle's outcome (Red Team's mandatory disclosure).
- **The VO2 thermal estimate is a single back-of-envelope calculation**,
  not a rigorous heat-transfer model — order-of-magnitude only, explicitly
  capped against scope creep into a THERMO-sidecar rebuild.
- **Does not evaluate materials-engineering roadmaps** — "could a future
  material close this gap" is out of scope; this reports what is published
  now.
- **English-language, freely-accessible-source bias** — WebSearch/WebFetch
  access does not guarantee coverage of paywalled specialist journals.
- **Switching-speed and at-rest verdicts are checked against an unsourced
  perceptual band and an unbuilt instrument (T3, stage-10)** — flagged
  provisional throughout, per Red Team's fix 7.

## Cost note

Zero FDTD calls. No `lab/` engine changes; no trust-suite re-run required.
Expected effort: a bounded WebSearch/WebFetch pass (order 20–30 queries
across four mechanism-class rows × five data axes, including the two new
mandatory checks) plus one capped analytic thermal estimate. The cheapest
cycle this program has run, and per Red Team's own ranking, the most
overdue.

## Phase 4 — Results (exp-036, 2026-08-16)

Four independent search legs, one per mechanism-class row, run in
parallel by fresh sub-agents against the pre-registered predictions above.

**⚠ Methodology degradation, disclosed up front (verify-before-claim):**
WebFetch was blocked by this session's network egress proxy for
essentially every scholarly domain attempted (ScienceDirect, Nature,
PMC/NCBI, arXiv, RSC, MDPI, AIP, ResearchGate, even Wikipedia) — three of
the four legs (RSA, photochromic, photothermal) hit this independently and
reported it explicitly; the TPA leg did not flag it, but also did not
report opening full-text sources beyond what WebSearch's own snippets
supplied. **Every figure below comes from WebSearch result/snippet
synthesis, not independently-opened, directly-read primary-source
tables.** Where 2+ distinct search hits from different papers/groups
converged on the same order of magnitude, this is reported as meeting the
≥2-independent-source bar in the weaker "corroborating search snippets"
sense, not the stronger "read the actual tables" sense the Phase-1
proposal and Red Team's "rigorous, not informal" framing intended. This is
a real, honest shortfall against this cycle's own stated bar — flagged
for Phase 5 to weigh, not smoothed over.

### RSA — **published-partial, CONFIRMED, dynamic range remains the sole decisive gap, now measured wider**

Real dynamic-range figures found across every named family: 2.8–7.2×
(Ir-acac complexes, systematic 5-compound series), ~2× (heavy-atom
phthalocyanines, the field's most-cited paper), ~40× (single-source
porphyrin outlier, explicitly self-described in its own text as "among the
best values found in the literature"). Repeated targeted searches for
>100×/>500× RSA dynamic-range claims across every named family returned
**nothing** — a genuine negative result. Applying QUANTUM's mandatory
absorption-only correction (÷0.51–0.61) sharpens the effective bar from
≥540–600× to **≥~890–1,180×** — against the best literature figure found
(~40×), the shortfall widens to **~22–30×**, not the naive ~13–15×.
Irradiance **confirmed clearing even more strongly than predicted**: a
distinct RSA subclass (long-lived-triplet accumulation, Hirata et al.,
*Nature Materials* 13, 938 (2014)) operates at **10⁻⁴ W/cm² — below the
~10⁻³ W/cm² witness estimate itself**, not just the generous ceiling.
Switching speed confirmed **ns–µs, clears trivially** for classic RSA
materials — but a genuinely new, unanticipated finding: the same
low-irradiance-capable subclass achieves its sensitivity via triplet
lifetimes reaching **1–21+ seconds**, plausibly **failing the reverse/
reset leg** of the 10ms–1s window — an internal RSA-class irradiance-vs-
speed tradeoff this program had not previously considered, and a possible
new constraint-3-at-rest risk for that specific subclass (moderate
confidence, flagged not scored).

### TPA — **unobtainium, CONFIRMED, irradiance gap sharpened not shrunk**

Dynamic-range/exponent (n≈1, structurally intensity-proportional)
confirmed as textbook-standard across every source — the least
contestable finding of the cycle. Irradiance: real, cited visible-
wavelength thresholds (Sheik-Bahae/Van Stryland foundational
semiconductor-TPA database; He et al. *Opt. Lett.* 20, 435 (1995), visible
602nm demonstration; ZnSe/GaAs-nanocrystal Z-scan studies) cluster
**~10⁷–10⁸ W/cm²** — landing at the lower-middle of the prior 10⁶–10⁹
estimate, i.e. **~9–11 orders of magnitude above the ≤10⁻²/~10⁻³ W/cm²
ceilings**, squarely inside (not below, not above) the pre-registered
8–12 OOM band. Switching speed confirmed sub-ps/instantaneous both
directions (virtual-state process, no real-state bottleneck), with a
minor caveat: applied TPA optical limiters often pair the instantaneous
TPA event with a secondary, genuinely slower excited-state/free-carrier
process (~ns) — irrelevant to the ms–s window either way.

### Photochromic (photochemical) — **published-partial, CONFIRMED, with the at-rest failure now the strongest single finding of the cycle**

Dynamic range sharpened rather than uniformly confirmed: azobenzene
cleanly confirms "1–2 orders short" (~3–6× after absorption-only
correction, 2 independent sources on both ε values); diarylethene and
spiropyran are **genuinely open, not closed** — both show near-zero
bleached-state baseline absorption at the colored band, meaning the
intrinsic on/off ratio could in principle be large, but no paired
ε_colored/ε_bleached table was recoverable given the WebFetch blockage;
fulgide dynamic range is an **outright data gap** (no figure found).
Irradiance confirmed clearing easily (2.4×10⁻³ W/cm², near the witness
estimate itself). Reverse-switching speed confirmed as the dominant
failure mode for the commonly-cited, durable systems (spiropyran thermal
half-lives sec–hours–effectively-permanent depending on matrix; P-type
diarylethene/fulgide have no thermal reverse path at all, structurally
failing constraint 4 regardless of speed) — **but real, published fast
exceptions exist** (fast T-type diarylethenes, µs–ms; amino-/push-pull
azobenzenes, ms–s), just not the durable systems the pre-registration had
in mind. **Constraint-3-at-rest — EM's mandatory catch — strongly
confirmed, the sharpest result of this experiment**: spiropyran reaches
**60–80% steady-state colored (merocyanine) population under continuous,
sun-comparable ambient illumination**, two independent sources, no
flashlight involved at all; P-type systems (fulgide, most diarylethenes)
are structurally worse (dose-ratcheting toward their photostationary
ceiling with no thermal escape channel); a newly-surfaced **all-visible-
light-activated diarylethene subclass** would fail this check
unconditionally, needing no UV at all. Caveat carried honestly: robust for
outdoor/daylight-spectrum ambient; the magnitude at dim indoor ambient
specifically is kinetically expected non-zero but not directly sourced at
that intensity.

### Photothermal (VO2) — **unobtainium, CONFIRMED, and sharper than predicted**

Intrinsic dynamic range (distinguishing bare-material figures from
metasurface/resonant-cavity device figures, per PHOTONICS' film-vs-
intrinsic discipline applied here too) is order 10–30×, likely 1–2 orders
short even before irradiance is considered — moot, since irradiance fails
independently and more severely. Irradiance/pump-regime confirmed
decisively: every pulsed demonstration found sits 6–9 OOM above the
witness estimate; every CW demonstration, even the most favorably
plasmonically-enhanced case (0.28–0.4 W/cm²), sits 2–5+ OOM above it — VO2
photoswitching is essentially never demonstrated at diffuse, unconcentrated
CW flux. THERMODYNAMICS' mandatory capped analytic estimate, worked
through with cited VO2 thermal properties (ρ=4340 kg/m³, c_p≈690 J/kg·K,
κ≈3.5 W/m·K, α≈1.17×10⁻⁶ m²/s) against this program's own T5 power budget:
heating time at flashlight-level absorbed power ranges from **~15–45s**
(idealized 1µm film, zero-loss, latent-heat-corrected) to **~1.7 days**
(1cm scale); passive reset time ranges from **~0.85µs** (1µm) to **~11.5
days** (1m), crossing the 1s mark near L≈1mm. **Sharper than
pre-registered: no length scale from µm to m clears BOTH legs
simultaneously** — the heating leg alone is fatal across the *entire*
tested size range, not only at the cm–m scale the pre-registration named.
Constraint-3-at-rest confirmed no signature under ordinary ambient — VO2
"smart window" self-activation is real but requires direct, sustained,
hours-long solar irradiance (~0.1 W/cm², two orders above flashlight
level) heating the object's entire bulk, mechanistically distinct from
this program's ordinary-ambient framing.

## Learned

**Program-level pre-registered prediction CONFIRMED**: no mechanism class
clears all bounds simultaneously, and the four classes fail via four
structurally distinct, non-overlapping primary gaps, now literature-
grounded rather than informally estimated — RSA (dynamic range, ~22–30×
short of the absorption-corrected bar even at the best published figure),
TPA (quantum-nonlinear irradiance threshold, ~9–11 OOM), photochromic
(reverse-switching speed AND/OR a strongly-confirmed constraint-3-at-rest
failure — the single sharpest finding of this cycle), photothermal/VO2
(bulk thermal power-budget/diffusion, now shown fatal at every length
scale tested, not just cm–m). This is the genuine boundary-mapping result
PANEL.md's "honest alternative product" names — four now-cited mechanism
classes, four distinct failure modes, each independently sufficient.

**Checkpoint criterion 2 does NOT fire**, exactly as pre-committed: this
cycle deliberately left free-carrier absorption and combined saturable/RSA
media untested (Red Team's own mandatory disclosure). A clean four-class
sweep, however decisive, is not "a whole mechanism class" ruled out.

**Constraint-3-at-rest is a genuinely new, load-bearing finding this
program had never checked before this cycle** (ELECTROMAGNETISM's Phase-2
catch): σ(x,t)-adjacent hysteretic mechanisms can fail PANEL.md's hardest
clause — "not a black silhouette at rest under ambient light" — via
ordinary daylight alone, independent of the flashlight entirely.
**Correction, Phase 5 (Red Team, adjudicating two independent blind
attacks from PHOTONICS and VISION SCIENCE — accepted in full, language
walked back same-shift):** the originally-committed framing here
("strongly confirmed," "the sharpest single number this cycle produced")
overclaimed what was actually shown. Two open gaps, neither closed by
this cycle: (a) the spiropyran 60–80% figure was measured under
sun-comparable/photopic continuous illumination, not the dim/night ambient
regime the witness scenario (Tier-W) actually specifies — nobody notices
a swept flashlight beam in daylight-level light, so the sourced figure sits
in the wrong intensity regime for the phenomenon this program studies; (b)
a photostationary *population fraction* is chemistry, not a scored
perceptual quantity — it has not been carried through ε_colored/
ε_bleached, path length, and object geometry into an actual scene contrast
(luminance or chromatic), nor checked against any sourced detection
threshold analogous to T2's. **Correct standing as of this cycle: a real,
sourced chemistry finding whose visual significance is unverified — not
yet a scored constraint-3 violation.** What DOES survive this correction
intact, and is arguably the more secure result: ELECTROMAGNETISM's
structural derivation (Phase 5, independently re-derived by Red Team) that
ANY hysteretic-σ(I) mechanism with reverse rate k_r slow relative to
ambient dwell time has a strictly positive steady-state colored population
n_ss = k_f(I_ambient)/(k_f(I_ambient)+k_r) for any nonzero k_f(I_ambient) —
a class-level kinetic necessity, independent of any single material's
measured coloration fraction, and not undone by discounting the spiropyran
number specifically. Logged as new LIVE THREAD **T17** in LOGBOOK.md.

**Two new, unanticipated findings, neither closing cleanly this cycle:**
(1) a low-irradiance-capable RSA subclass (long-triplet-lifetime
materials) appears to trade its irradiance advantage for a probable
reverse-switching-speed failure — an internal tradeoff within the RSA
class itself, structurally echoing the photochromic row's own failure
mode, previously unconsidered; (2) diarylethene/spiropyran intrinsic
dynamic range is genuinely open, not closed NO, pending a source that
supplies a directly paired ε_colored/ε_bleached table — the WebFetch
blockage is the specific reason this could not be resolved this cycle.

**The rigor bar was only partially met (Phase 5 ruling: PARTIAL, not
full).** This cycle set out to upgrade MATERIALS' self-flagged "informal"
desk synthesis into something citation-backed; it did produce real paper/
review titles, authors, and years for nearly every figure above, a
substantial improvement — but WebFetch's total blockage across three of
four legs means no primary-source table was independently read and
verified end-to-end; every number rests on WebSearch's own snippet
synthesis. Phase 5 (PHOTONICS and MATERIALS, independently) rules this a
real middle tier — "sourced-but-unverified" — above the prior informal
synthesis but short of the "rigorous... gates clean" standard Checkpoint
criterion 2 requires.

**PHOTONICS' own Phase-2 mandatory fix (tag every extracted figure's
wavelength against this program's 450/600/750nm sweep) was NOT carried out
in the Results above** — a confirmed mandatory-fix miss (Red Team's Phase
5 audit, checked directly against the text). Moderate severity: does not
change RSA/TPA/VO2's verdicts (all fail by wide margins regardless of
wavelength), but is directly load-bearing for the photochromic row —
photochromic *coloration* is typically UV-driven (~350–380nm), outside
both this program's sweep and a white flashlight's dominant spectrum, and
whether the witness's actual flashlight even triggers the write step at
all was never checked despite being explicitly committed to. Queued for
Iteration 14, not resolved this cycle.

**Checkpoint criterion 2 does not fire, for TWO independent reasons, not
one.** NOTES.md's own pre-registration named the first (free-carrier
absorption and combined saturable/RSA media remain untested). Red Team's
Phase-5 audit adds a second, independently sufficient reason: even the
four classes that WERE covered rest on WebSearch-snippet synthesis, not
primary-source-verified figures — "gates clean" requires rigor this cycle
admits it did not fully reach. Either gap alone would keep criterion 2
from firing; both are open simultaneously.

## Phase 5 — Review (six fresh seats, blind, verbatim) — summary

Full verbatim reviews: LOGBOOK.md Iteration 13. All six seats reviewed the
committed Results independently; two pairs of findings converged
unprompted across blind seats — a rare and load-bearing signal:

- **PHOTONICS and VISION SCIENCE independently attacked the same flagship
  finding** (spiropyran's at-rest coloration) from different angles —
  PHOTONICS on the wrong ambient-intensity regime (sun-comparable vs. the
  witness's actual dim/night scene), VISION SCIENCE on the missing
  chemistry-to-perception conversion. Both correct; both accepted; the
  Learned section above is corrected accordingly.
- **MATERIALS, ELECTROMAGNETISM, and QUANTUM OPTICS independently ranked
  closing free-carrier absorption + combined saturable/RSA media as
  Iteration 14's top priority** — near-unanimous, for compatible but
  distinct reasons (MATERIALS: the last gap blocking Checkpoint-2;
  ELECTROMAGNETISM: directly testable via this cycle's own kinetics
  framework; QUANTUM: expressible in existing bench machinery).
- **PHOTONICS** additionally caught its own Phase-2 fix (wavelength-tagging)
  going unexecuted, and flagged that σ_abs/σ_ext≈0.51–0.61 (T9, this
  program's own established figure) is being reused outside the near-field
  box-scale regime it was validated in — an extrapolation risk, not
  verdict-overturning.
- **ELECTROMAGNETISM** derived the class-level leaky-integrator argument
  described above, and found LOGBOOK.md's T1 entry has not yet absorbed
  the hysteretic-σ(I)-with-memory distinction this cycle established
  (grep-confirmed zero prior occurrences of "hysteretic"/"at-rest"/
  "photochromic").
- **THERMODYNAMICS** independently re-derived its own capped VO2 thermal
  estimate from cited primitives and found the conclusion MORE robust than
  originally stated (heating alone is fatal at the smallest length scale
  tested, not only at cm–m scale) — with two flagged, non-verdict-
  overturning inconsistencies (latent-heat handling; a possible ΔT
  rise-vs-hysteresis-width ambiguity) queued for correction on promotion
  to reusable code.
- **QUANTUM OPTICS** found the absorption-only correction (its own Phase-2
  mandatory fix) was applied correctly for RSA and photochromic, correctly
  withheld for TPA (dimension doesn't apply), but is absent with no hard
  number for VO2 — a real category error (molecular vs. Drude/plasma
  physics), ruled non-load-bearing this cycle (VO2 already fails
  independently by wide margins) but queued for correction before any
  future standalone VO2 citation.

**Red Team (audit, verdict: PARTIAL).** Independently re-derived EM's
kinetics argument and THERMO's thermal estimate, confirming both sound.
Confirmed PHOTONICS' wavelength-tagging miss directly against the text.
Ruled the spiropyran overclaim a genuine constraint-3-language risk
(Checkpoint criterion 4, narrow/self-correcting form — not a program
pause, but a same-shift correction, completed above) precisely because
EM's underlying catch is real and useful; the risk was in how the specific
empirical number got described, not in raising the question. Ruled
Checkpoint criterion 2 does not fire for two independent reasons (the
pre-disclosed FCA/combined-media gap, plus the WebFetch-evidentiary-tier
gap). Affirmed the near-unanimous FCA-next ranking with no dissenting
consideration strong enough to displace it.

**Director's synthesis: all four same-shift corrections in Red Team's
docket accepted in full, applied above; none overridden.** This was
itself an adjudication of two independently-converging blind critiques
(PHOTONICS + VISION SCIENCE on the same finding) plus a confirmed textual
miss (PHOTONICS' own wavelength-tagging fix) and a bookkeeping gap
(LOGBOOK.md's T1 not yet reflecting this cycle's finding) — every one
checked directly against the record, not asserted. Nothing in the docket
warranted a Director override. **Verdict: PARTIAL** — a genuine,
citation-sharpened four-class boundary-mapping result (Checkpoint criterion
2 does not fire, disclosed on two independent grounds), a real new
class-level finding (T17, secured on EM's structural derivation rather
than the discounted empirical headline number), and a program-integrity
catch resolved within the same cycle it was raised, per this program's own
established precedent for what PARTIAL means (a cycle's own open questions
close or don't — this one closed cleanly, with corrections disclosed, not
smoothed over).

## Next

Ranked per Red Team's Phase-5 adjudication across all six seats:

1. **Free-carrier absorption + combined saturable/RSA media literature
   check** (near-unanimous: MATERIALS, ELECTROMAGNETISM, QUANTUM OPTICS),
   same zero-FDTD-cost methodology — the last named-but-untested class
   standing between this program and any legitimate future Checkpoint-2
   attempt, on top of also needing the evidentiary-tier gap closed.
2. **Targeted primary-source re-verification of this cycle's two fragile
   numbers** (RSA's single-outlier ~40× porphyrin figure; the spiropyran
   at-rest figure, specifically re-sourced at witness-relevant dim/night
   ambient) via a working full-text access route, paired with the still-
   outstanding wavelength-tagging check and the ε/path-length/geometry
   perceptual conversion VISION SCIENCE named — before the spiropyran
   figure is cited anywhere as a scored constraint-3 violation.
3. **Formalize T17 (hysteretic-σ(I)-with-memory / constraint-3-at-rest) as
   a persistent LOGBOOK thread** (done, this record) **and build the
   rate-equation kernel in-engine** (QUANTUM's proposal) to bench-test the
   at-rest population directly — converting this cycle's sourced-but-
   unverified chemistry claim into a bench-confirmed, expressible
   simulation result.

Lower priority, inherited/queued: stage-10 T3 (temporal-contrast/flicker
instrument) — VISION SCIENCE's and ELECTROMAGNETISM's own top-3 pick,
independently, now flagged more urgent (second consecutive cycle producing
a switching-speed verdict gated on it); docket #7's sourced witness-
parameter table (flashlight irradiance AND the 10ms–1s window both remain
unsourced, and every kinetic/thermal verdict this cycle issued depends on
them); QUANTUM's VO2 absorption-correction category-error fix; THERMO's
latent-heat/ΔT-quantity fix on promotion to reusable code; REALIZABILITY_
MEMO.md amendment with this cycle's sharper cited figures (MATERIALS).
