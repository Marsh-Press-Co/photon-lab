# LOGBOOK — the panel program's persistent memory

*Read this in full before proposing anything, every cycle. Never re-propose a
ruled-out idea — the reason it died is recorded here so it stays dead. New
entries append; the Ruled Out and Live Threads sections stay current at the
top. Protocol: PANEL.md.*

## RULED OUT (summary — the reason is the record)

- **R1 — Passive refractive / transformation-optics cloaking as the
  phenomenon's mechanism.** Ruled out by constraint 1 and by our own data:
  exp-001 — the cloak's entire function is that the beam *continues* into the
  distance (beam-behind 0.64 vs absorber 0.017), the opposite of the witness
  clause; it also glints (observer return ≈ bare metal at 450 nm) and its
  behavior swings ~2× across the visible band (exp-001/003) where the
  statement implies wavelength-flat white-light behavior. Do not revisit as a
  constraint-1 mechanism. (Angular-selectivity proposals are a different
  thread — they must terminate the beam, not route it around.)
- **R2 — "Shell = any integer × λ" standing-wave rule** (cloak line):
  exp-019 killed the generic-integer version — 2λ shows nothing where 3λ
  dips. Recorded so nobody resurrects "integer resonance" as a mechanism
  class without new evidence.
- **R3 — Grid/staircase artifacts as explanations for observed parameter
  structure**: refuted three separate times by resolution-convergence checks
  (exp-005, exp-010, exp-015). Meta-rule inherited by the panel: any
  surprising feature gets a resolution check before it gets a mechanism
  debate — and "artifact" claims need the check too.

## ESTABLISHED (what the bench has already proven — the absorption model
## assessment, 2026-08-12)

**The graded-black absorber (`materials.graded_black_shell`, suite stage 7)
already satisfies constraints 1 and 2, broadband:**

- Coated-wall reflection R ≤ 0.2% across the full 450–750 nm sweep
  (0.10% @ 600 nm) — designed to gates written before its first run.
- Observer return **equals the empty-room camera floor at every wavelength**
  (exp-001 post-phasor-fix: 0.00007–0.00014 absolute) — to measurement
  precision, nothing comes back. Backward spray ≤ 10⁻⁴ of extinction
  (exp-002).
- Beam-behind 1.5–1.8%: the beam stops. Wavelength-flat: white light changes
  nothing (the witness's flashlight was white light — exp-001's P2/P5).
- σ_abs/σ_ext = 0.51 — the extinction paradox, measured; "invisible" has a
  direction (exp-002): the absorber wins the source-observer geometry by
  orders of magnitude and *loses* all-angle visibility (largest shadow in
  the table).

**Bench trust:** 30/30 suite checks green; three independent solvers × two
OSes agree to the printed digit; CI runs the suite on every push.

**The gaps — why constraints 3 and 4 are open (no instrument has ever
measured them here):**

1. **No ambient-illumination scene exists.** Every experiment to date uses a
   single directed source. The absorber's silhouette under ambient light —
   the thing constraint 3 is about — has never been rendered as a number.
   (By construction it will be a deep silhouette photopically: a perfect
   absorber IS a black shape in daylight. Quantifying that failure, and the
   ambient level at which it stops being perceivable, is Iteration 1.)
2. **No time-varying materials** — the engine's update coefficients are
   static per run (constraint 4 unsupported).
3. **No intensity-dependent materials** — the leading escape route for the
   central tension (σ(I)) is unbuildable today.
4. **No angular-selectivity machinery** beyond source direction choice.
5. **No thermal accounting** — the energy ledger stops at "absorbed";
   nothing estimates re-radiation (THERMO's sidecar fills this per-proposal,
   analytically).

## LIVE THREADS (unresolved tensions between disciplines)

- **T1 — The central tension.** Linear time-invariant media cannot satisfy
  1+2+3 at photopic ambient: the extinction that stops the beam darkens the
  ambient view identically. EM seat to formalize per-proposal (reciprocity/
  passivity bookkeeping). Escape classes on the table: σ(I) intensity
  gating · σ(x,t) switching · angular selectivity · sub-threshold weak
  absorption + scotopic ambient. (σ(I) is the only class that natively
  serves constraints 3 AND 4 with one mechanism — flagged, not yet argued.)
- **T2 — Perceptual thresholds need pinning.** Photopic Weber-contrast
  detection sits near |C| ≈ 0.01–0.03 for well-adapted foveal viewing of
  extended targets; scotopic thresholds rise steeply as ambient falls, and
  the witness scene is scotopic. VISION SCIENCE pins the exact numbers, with
  sources, in Iteration 1 — before any run scores against them.
- **T3 — Switching must also hide.** The eye's temporal-contrast (flicker/
  motion) sensitivity beats its static-contrast sensitivity; a mechanism
  that switches ON mid-sweep creates a temporal edge. Constraint 4
  interacts with 3: the transition itself must stay sub-threshold. Metric
  exists in the table (switch transient at observer); instrument is stage-10
  work, not yet built.
- **T4 — Beam-trail realism.** One *sees* a flashlight beam in open air only
  via aerosol/dust scattering along the path; "the beam stopped" implies the
  visible trail terminates at the volume. Current scenes have no ambient
  scattering medium — a scene-realism upgrade candidate for a later
  iteration (weak volumetric scatterer along the beam path), not Iteration 1.
- **T5 — The thermo ledger.** A ~1 W-class flashlight beam absorbed in a
  ~m-scale volume: where does it go? ΔT, re-emission band (~10 µm — eye-
  invisible, IR-detectable), and steady-state budget must be logged per
  proposal (THERMO sidecar, analytic).
- **T6 — Cloak-line leftover, kept honest:** exp-017's unscored observation
  (13 angular peaks at the 3λ point vs 10 at flanks) — parked cloak-line
  curiosity; revisit only if a future thread returns to that mechanism space.

## PARKED (pre-panel threads, resumable — not on the program's critical path)

- Is the 3λ shell-thickness feature specific to r2=90? (exp-019's queued
  follow-up; every point in that line shared one outer radius.)
- Multi-λ check of the core=8 cloak design lead (exp-007/008/010).
- `mu_r_floor < 0.05` with paired courant reduction; CFL ceiling is
  geometry-dependent (exp-011's addendum).
- Original parking lot: TF/SF injector, true PML, near-to-far transform,
  black-lined cloak hybrid, Q vs incidence angle, adjoint fourth panel,
  Disclosure physics-annex (humans' call), Blender/UE presentation.

## ITERATION TEMPLATE

    ## Iteration N — <title> (exp-0NN) — <date>
    Runner: <session/shift> · Lead: <seat>
    PHASE 1 (proposal): mechanism, parameter table, T1 escape route,
      predictions with falsifiable bands, idealizations
    PHASE 2 (critiques): per seat — steel-man · attack · verdict;
      Red Team last — tagged attack list
    PHASE 3 (synthesis): the ONE configuration; criticisms accepted /
      overridden, with reasons; NOTES.md committed before run
    PHASE 4 (test): metric row + gates
    PHASE 5 (review): VERDICT promising / partial / ruled out (+reason);
      ranked top-3 next directions; logbook sections updated
    Open questions carried forward: …

---

# Iterations

## Iteration 1 — The Ambient-Appearance Instrument — 2026-08-12

Runner: interactive cloud session (Marsh present) · Lead: **VISION SCIENCE**
· Phases run: **1–2 only** · Status: **HALTED AT CHECKPOINT #0** — awaiting
Marsh's go-ahead before Phase 3 (synthesis), any engine code, or any run.
Experiment number reserved: exp-020 (directory created at synthesis).
Panel: 7 fresh-context seats, Phase-2 critiques written blind and in
parallel; Red Team read everything and spoke last.

### Phase 1 — Proposal (VISION SCIENCE, verbatim)

# PHASE 1 — PROPOSAL · Iteration 1 · Lead seat: VISION SCIENCE
## "The Ambient-Appearance Instrument" — first measurement of constraint 3 (`lab/ambient.py`, suite stage 9)

### 1. Narrative (≤300 words)

Constraint 3 has never been a number on this bench: no ambient scene has ever been rendered, for any object. Iteration 1 builds that instrument and takes the baseline the entire T1 debate needs. We back-light the two best-characterized objects we own — the stage-7 graded-black absorber (already proven on constraints 1 and 2) and a PEC disk matched to its outer radius — with a nine-angle incoherent plane-wave ambient spanning ±40°, and read the observer-directed flux profile B(y) on a pre-registered plane 15 cells from the object. Weber contrast C over pre-registered object and flank windows is the silhouette number, reported per wavelength and luminance-weighted (photopic V, scotopic V′). The instrument ships with its own trust-suite stage — empty-scene identity, absolute flux balance against the analytic angle sum, angled-source wavelength gate, N-convergence — before any object number is believed.

Vision science leads because the output is perceptual: a contrast means nothing without a threshold. So the photopic and scotopic detection bars are pinned below, with sources, before any run, and the crossover question is committed: how dark must the world be before a perfect absorber's hole in the background falls below human detectability? The committed answer — lab-observer crossover near 5×10⁻⁶ cd/m², one to two log units darker than typical moonless rural scenes — reframes the sub-threshold escape route: darkness alone cannot hide this object from a dark-adapted observer; darkness plus the observer's own flashlight-ruined adaptation plausibly can, and that glare arithmetic is delivered as a labeled analytic sidecar, not an FDTD claim.

The expected headline, stated in advance: the absorber fails constraint 3 photopically by more than thirty times the conservative field threshold — quantified for the first time, as the number every future mechanism must beat. Deferred by design: front-lit reflectance channel, temporal transients (T3), aerosol realism (T4).

### 2. Parameter table

| Knob | Value | Note |
|---|---|---|
| Grid / domain | Δ = 30 nm; 560×560 cells (16.8 µm)²; courant 0.32; 3200 steps; CW | exp-001 numerics unchanged (comparability) |
| Wavelengths | 450 / 600 / 750 nm (cpl 15 / 20 / 25) | equal-energy 3-λ white quadrature |
| Ambient geometry | line source, FAR side (back-lighting); angles θ ∈ {0, ±10, ±20, ±30, ±40}°, N = 9 | span capped at ±40°, inside the honest ±45° boundary limit |
| New engine change | `angle_deg` on the line source | small change; gated by its own suite stage before use |
| Coherence model | one CW run per (θ, λ); intensities summed post-hoc | incoherent-ambient approximation |
| Component normalization | post-hoc scale so each (θ,λ) empty-scene flank mean = 1 | kills source-profile ambiguity |
| Angular weights | primary wᵢ = 1/9 (equal observer-directed flux); secondary wᵢ ∝ cos θᵢ (Lambertian) | secondary is a free re-weight of the same runs |
| Source taper | outermost 40 cells of the line only | flatness gated below |
| Scenes (3) | empty (identity + reference) · `graded_black_shell` stage-7 config verbatim (PEC core r = 0.9 µm, coat → r_out = 2.34 µm) · bare PEC disk r = 2.34 µm | PEC is outer-radius-matched: isolates material from geometry; a circle's projected width is angle-invariant |
| Measurement plane | observer side, fixed absolute row, 15 cells from object outer edge (primary); rows at 12 and 16 cells recorded as sensitivity | close plane per Director's brief and the VALIDATION close-monitor lesson |
| Quantity | time-averaged observer-directed Poynting flux per y-cell via quadrature phasors (stage-6 idiom) → B(y) | total-field observable, deliberately (a shadow is a total-field object) |
| Windows | object: \|y−y₀\| ≤ 78 cells (= r_out); guard: 78–117; flanks: 117–195 cells, both sides averaged; all windows ≥ 20 cells clear of damping bands | oblique shadow shift ≤ 15·tan 40° ≈ 13 cells ≪ 78 — why the close plane works |
| Contrast | C = (B̄_obj − B̄_flank)/B̄_flank on the weighted incoherent sum (Director's formula verbatim); reported per λ, plus V- and V′-weighted | V = {0.038, 0.631, 0.00012}; V′ = {0.455, 0.033, ≈10⁻⁶} at {450, 600, 750} nm (CIE 1924 / CIE 1951) |
| Run count | 3 scenes × 9 angles × 3 λ = 81; +16 (empty + PEC @600 nm at ±5, ±15, ±25, ±35°) for N = 17 convergence; ≈ 97 runs ≈ 1 h at exp-001 pace | artifacts via `save_run` + Evidence Gate, house rule |
| Suite stage 9 gates (green before any object number is read) | (a) angled-source wavelength along k̂: 20.0 ± 0.5 cells @600 nm, θ = 30°; (b) empty-scene flatness ±5% over the analysis span at θ = 0, ±40°; (c) empty identity \|C_empty\| ≤ 0.01, every λ, both weightings; (d) absolute balance: raw empty flank flux = Σᵢ cos θᵢ analytic sum ±5%; (e) convergence \|C(N9) − C(N5)\| ≤ 0.05 and \|C(N17) − C(N9)\| ≤ 0.02 (PEC @600 nm) | (c) and (d) are this family's absolute-identity gates, per the phasor-bug lesson |
| Meta-rule | any surprising B(y) feature gets a resolution check before a mechanism debate | R3, inherited |
| Deferred | front-lit (observer-side) reflectance channel; sweep/temporal transient (T3, stage 10); aerosol beam-trail (T4) | stated, not smuggled |

### 3. Pinned perceptual thresholds (committed before any run; frozen at Phase-3 commit — post-run revision voids the scoring)

**Photopic bar, extended dark target (≥ 1° angular subtense — witness volume ~1–3 m at ~45 m ≈ 1.3–3.8°).** Laboratory threshold |C|_thr = 0.005 (50% detection, binocular, known location, unlimited time): Blackwell 1946 (JOSA 36:624), 121-arcmin-target asymptote 0.003–0.005 at ≥ ~3 cd/m²; corroborated by peak contrast sensitivity ≈ 1/300 (van Nes & Bouman 1967, JOSA 57:401; Campbell & Robson 1968, J. Physiol. 197:551). Field bar |C|_thr = 0.02 for an uncued observer (field factor ≈ 4: CIE Pub. 19/2 1981; Adrian 1989, Light. Res. Technol. 21:181). **Scoring rule: |C| < 0.005 → constraint 3 PASS; 0.005–0.02 → MARGINAL; > 0.02 → FAIL.**

**Scotopic scaling.** Committed threshold function for extended dark targets, single power law bridging Weber → Rose–de Vries (∝ L^−0.5; Rose 1948, JOSA 38:196) → absolute regimes: **C_thr(L) = 0.005 · max[1, (L/3 cd·m⁻²)^−0.4], clipped at 1**; vertical uncertainty ±0.3 log. Anchors: Blackwell's large-target family (low-L end rises steeply); absolute rod limit for extended fields ~10⁻⁶ cd/m² (Hecht, Shlaer & Pirenne 1942, J. Gen. Physiol. 25:819; Pirenne 1962 in Davson, *The Eye* v.2). Committed table (lab bar): 100 cd/m² → 0.005 · 1 → 0.008 · 10⁻² → 0.05 · 10⁻³ → 0.13 · 10⁻⁴ → 0.31 · 10⁻⁵ → 0.78 · ~5×10⁻⁶ → 1.0.

**The crossover question, explicit.** For a perfect absorber (C = −1), invisibility requires C_thr(L_B) ≥ 1: **L*_lab ≈ 5×10⁻⁶ cd/m² (band 10⁻⁶–10⁻⁵); with the ×4 field factor, L*_field ≈ 4×10⁻⁵ (band 10⁻⁵–10⁻⁴).** Reference luminances: clear moonless rural sky ≈ 1.7×10⁻⁴ cd/m² (22 mag/arcsec²; Roach & Gordon 1973); starlit terrain ~10⁻⁴–10⁻³; heavily overcast light-pollution-free terrain ~10⁻⁵–10⁻⁴. Reading, committed in advance: a cued dark-adapted observer sees the silhouette at every natural ambient except extreme overcast; an uncued casual observer straddles threshold on the darkest nights; **and the witness himself is neither** — a hand-held ~100–200 lm flashlight puts ~0.01–0.1 lx of stray light at the holder's eye, a Stiles–Holladay veiling luminance L_v = 10·E/θ² ≈ 0.01–0.25 cd/m² (Holladay 1926; Stiles 1929; CIE disability-glare), elevating his effective adaptation 2.5–3.5 log units above night sky and pushing C_thr for the dark background above 1. The static silhouette is then sub-threshold for the flashlight holder while the beam interaction stays high-contrast — which is precisely constraint 3's phenomenology. This glare term is an **analytic sidecar, labeled as such** (THERMO-sidecar convention), not an FDTD output.

**How 2D flux contrast maps onto the perceptual quantity — and its limits.** The transferable quantity is the window-mean level contrast of an extended uniform patch scored against extended-target thresholds; nothing else transfers. Limits, all stated: (i) *spectral* — 3-λ equal-energy quadrature of a white band, V/V′-weighted post-hoc; no photon-noise floor is simulated (noise enters only through the threshold curves); (ii) *spatial frequency* — the simulated µm-scale edge diffraction does not model the retinal edge; a meter-scale edge at 45 m is acuity-sharp, so we score area contrast, not edge-profile detectability, and near-plane profile shape is instrument detail, not percept; (iii) *scale bias* — a 10⁶λ object's geometric shadow is cleaner than our ~10λ object's, so measured |C| is a lower bound on real-scale |C|: "visible" conclusions are robust to this bias, any near-invisible reading (|C| < 0.1) would not be; (iv) *2D vs 3D* — cylinder shadows are not sphere shadows; trust is O(1) for deep silhouettes only — near-threshold verdicts from this bench require a 3D or analytic cross-check before belief; (v) *polarization* — TMz only; rods and cones are polarization-blind and PEC scattering is polarization-dependent, so the PEC C is polarization-conditional; (vi) *adaptation state* — bars assume steady adaptation at L_B, free fixation, known location, unlimited time, binocular (Blackwell's conditions): the hardest case for hiding; monocular viewing relaxes thresholds ×~1.4 (Campbell & Green 1965, Nature 208:191); decrement thresholds are, if anything, slightly lower than increment thresholds, so the bars are not lenient; (vii) *back-lit only* — the deferred front-lit channel means C understates PEC-type visibility (no glint term) and is near-exact for the R ≤ 0.2% absorber; (viii) *no temporal term* — static scene; motion/flicker sensitivity (T3) is a later instrument.

### 4. Falsifiable predicted outcomes (numeric bands, per metric)

- **P-V1 — empty-scene identity:** |C_empty| ≤ 0.01 at every λ and both weightings; empty B(y) flat to ±5% across the analysis span at θ = 0 and ±40°. Failure = instrument defect; no object number is interpreted until fixed.
- **P-V2 — graded-black absorber, photopic:** C_V ∈ [−1.00, −0.75], central −0.90; per-λ spread ≤ 0.05 (wavelength-flat, per its stage-7 pedigree). Encoded verdict: constraint-3 FAIL photopically by ≥ 37× the field bar (|C| ≥ 0.75 vs 0.02) and ≥ 150× the lab bar.
- **P-V3 — PEC control:** C_V ∈ [−1.00, −0.70], central −0.85; **material-blindness of the back-lit channel: |C_PEC − C_absorber| ≤ 0.15** — a mirror and a black body read as the same dark hole against a bright background; distinguishing them is the front-lit channel's job. PEC per-λ spread ≥ the absorber's and ≤ 0.2 (edge-fringe dispersion).
- **P-V4 — convergence:** |C(N=9) − C(N=5)| ≤ 0.05 and |C(N=17) − C(N=9)| ≤ 0.02 (PEC and empty @600 nm); plane-distance sensitivity across 12/15/16 cells ≤ 0.05 in |C|.
- **P-V5 — scotopic crossover (derived from measured C via the frozen threshold table; the falsifiable simulation quantity is C itself):** for the measured C band, L*_lab = 5×10⁻⁶ cd/m² [10⁻⁶–10⁻⁵], L*_field ≈ 4×10⁻⁵ [10⁻⁵–10⁻⁴]; committed conclusion that L*_lab sits ≥ 1 log unit below typical moonless rural scene luminance — darkness alone does not reach sub-threshold for a dark-adapted observer; the sub-threshold route survives only jointly with adaptation/glare elevation (sidecar numbers above).

### 5. Idealizations (lab convention)

2D TMz, one polarization; CW single-λ runs, 3-λ quadrature standing in for white light; diffuse ambient = 9 discrete incoherent plane waves over ±40° only — hemispheric illumination not represented (bias direction: fuller span raises flank light and shadow fill-in, so true C is slightly less negative; our |C| is an upper bound in angle-span and a lower bound in object scale, both stated); equal-flux slab sky primary, Lambertian as re-weight; post-hoc intensity summation ignores inter-component coherence; back-lit channel only, front-lit reflectance deferred; static scene — no sweep, no switching, no aerosol medium (T4 parked); graded damping bands, not PML; window means on a near virtual plane stand in for a retinal image — no imaging optics, no eye model in the loop; perception enters only through the frozen threshold table.

### 6. T1 escape-route statement

**This proposal implements no escape mechanism in simulation — it is the baseline, and says so.** It instruments constraint 3 for the first time, quantifies the LTI failure photopically with committed bands (the absorber's C is predicted ≥ 37× the field detection bar — T1's cost made numeric), and locates the sub-threshold route's operating window analytically: darkness alone fails for any natural night ambient under dark-adapted viewing; darkness plus observer glare/adaptation (the flashlight holder's own veiling luminance) plausibly succeeds, with the Stiles–Holladay parameters now on the table for a later iteration to formalize. Every future escape-route proposal — σ(I), σ(x,t), angular selectivity, sub-threshold — will be scored against the C bars and threshold table pinned here.

### Phase 2 — Critiques (five seats, blind, verbatim)

#### PHOTONICS — verdict: **support-with-changes**

**Steel-man:** Back-lit-first is the optically correct ordering, not a shortcut: for the stage-7 absorber (R ≤ 0.2% broadband) the omitted observer-side reflectance channel contributes O(0.002) to C, so the back-lit silhouette is near-exact for the one object T1 needs quantified — the deferral costs nothing where the headline lives. The coherence model is right physics: skylight has femtosecond coherence times, so per-(θ,λ) runs summed in intensity is the correct incoherent-ambient limit. Per-λ reporting with post-hoc V/V′ weighting keeps the absorber's proven wavelength-flatness as a live cross-check instead of burying it in one white number. The close plane follows the paid-for close-monitor lesson; window means refuse to over-read near-field fringes; the outer-radius-matched PEC exploits the circle's angle-invariant projected width to isolate material from geometry. Gates (c)/(d) give this new measurement family the absolute-identity anchor the phasor bug taught us to demand.

**Attack:** The illumination geometry cannot deliver the committed angular span. A far-side phased line source lights, at angle θ, only the parallelogram swept along k̂; with source-to-measurement-plane distance D ≈ 320 cells, the lit interval walks off by D·tanθ ≈ 271 cells at 40°. Against the pre-registered span y ∈ [85, 475]: at θ = +40° everything below y ≈ 271 is geometrically unlit — the entire lower flank, the guard, and 44% of the object window itself (≈70% counting the 40-cell taper) — softened only by an ~80-cell Fresnel edge (√(λD)). At ±30° a whole flank is dark; only ±10° covers the span cleanly. Six of nine angles fail gate (b) by construction, and per-(θ,λ) flank normalization then rescales a half-dark empty profile into the incoherent sum. The proposal's sole walk-off check (shadow shift ≤ 13 cells) used the 15-cell object→plane baseline, not the ~320-cell source→plane baseline.

**Flip:** Guarantee full-span direct-beam coverage at |θ|max before any run: widen the domain laterally to ≥1100 cells (or adopt the parked TF/SF injector) so the source parallelogram covers the entire analysis span at ±40°, keeping gate (b)'s ±5% empty-scene flatness at ±40° as the arbiter — and extend gate (a) to the worst-dispersion corner (450 nm, cpl 15, θ = 40°). Run cost ≈2×, still ~2 h.

#### MATERIALS & METAMATERIALS — verdict: **support-with-changes**

**Steel-man:** From the materials bench, the article choice is exactly right as far as it goes: these are the only two material-pedigreed objects we own. The graded shell carries pre-registered broadband gates (R ≤ 0.2%, 450–750 nm) and exp-001's return-equals-floor record; PEC is the one material FDTD represents exactly — no dispersion model, no parameter fitting, geometry-only staircase already covered by the R3 meta-rule. Outer-radius matching isolates material response from projected aperture. And P-V3's material-blindness prediction encodes a materials truth the bench already paid for: exp-002's σ_abs/σ_ext = 0.51 — a back-lit silhouette is set by extinction cross-section, not albedo, so mirror and black body must read as the same dark hole. That makes C the correct class invariant for T1: a baseline every material, published or exotic, inherits — measured with zero new material machinery.

**Attack:** The C axis gets calibrated only at its endpoints. Both articles are optically thick — predicted C ∈ [−1.0, −0.70] — and empty pins 0. Nothing validates the instrument anywhere in (−0.7, 0), yet every escape route this baseline exists to score — sub-threshold weak absorption, σ(I) below gate, partial switching — operates at |C| ≲ 0.1, straddling the 0.005/0.02 bars. Diffractive shadow fill-in and angular-span sensitivity are strongest precisely for weak extinction, so N-convergence proven on a deep PEC silhouette does not transfer; the proposal itself concedes near-invisible readings (|C| < 0.1) are not robust (limit iii). As scoped, the instrument can certify FAIL but never PASS — it cannot score the sub-threshold route its own P-V5 motivates. The charter question — what third article sharpens the baseline — has a concrete answer, and it is missing.

**Flip:** Add a third article: a solid dilute sponge disk, r = 2.34 µm, no PEC core, ε ≈ 1 with uniform σ scaled to center-chord optical depth ≈ 0.1 (target C ≈ −0.05 to −0.10). ε ≈ 1 keeps scattering negligible, so extinction ≈ absorption and a Beer–Lambert expectation band is pre-registerable; run the N = 9/17 convergence gate on it, not only on PEC. Cost: 27–35 runs (~20 min). Zero new engine physics — σ_e and the stage-7 solid-sponge-disk precedent already exist; a calibration article, not an absorber redesign, so Bonnie's lane is untouched. It also doubles as the first measured point of T1's sub-threshold class.

#### ELECTROMAGNETISM — verdict: **support-with-changes**

**Steel-man:** The EM bookkeeping is right where it is hardest to get right. For LTI media the ambient response is exactly the weighted sum of independent plane-wave components, and summing per-(θ,λ) intensities post-hoc is exact for mutually incoherent illumination — no coherent cross terms are ever formed, so the classic incoherent-approximation artifact cannot arise. The observable is extinction's shadow — precisely what T1 forbids hiding — and the radius-matched PEC control turns the optical theorem's shadow-side material-blindness (back-lit C reads projected extinction, not absorption) into falsifiable P-V3. Gates honor the paid-for lessons: an absolute raw-flux balance against the analytic Σcosθ sum (the class of check that caught the phasor bug), empty-scene identity, and N-convergence bounding single-run Fresnel-fringe ripple that window means alone don't kill. At Fresnel number ~20 with a ~2λ guard band, rim near-fields stay out of both windows.

**Attack:** Every oblique number in the table uses a 15-cell lever arm; the real arms are 93 and ~340 cells. (i) A disk's blocking chord passes through its center, 93 cells from the plane: at 40° the shadow centerline lands at 93·tan40° ≈ 78 cells off-axis, in-plane width 2r/cosθ ≈ 204 — vacating a third of the object window and shading 63 cells of the pre-registered flank. Ray-summing nine equal-weight angles: object coverage 0.80, flank deficit 0.13 — geometric ceiling C ≈ −0.77 before diffraction fill. The committed centrals (−0.90/−0.85) are unreachable; "shift ≤ 13 cells" is wrong by ×6 and propagated into P-V2/P-V3. (ii) A phased 400-cell-flat line (absorb=40, edge=40) walks Δx·tanθ ≈ 180–285 cells at 40° for any far-side placement; coverage cannot span the 390-cell window set — gate (b) fails by ±10° already, and at +40° the object window sits unlit in the empty scene.

**Flip:** Fix the oblique geometry end-to-end before Phase-3 freeze: grow the transverse domain to ≥~840 cells (390-cell span + 283-cell walk at 40° + tapers + damping) or adopt the parked TF/SF injector, and re-register windows and P-V2/P-V3 bands from a center-lever ray trace of the nine-angle shadow union — demonstrated by gate (b) passing at ±40° in the empty scene.

#### THERMODYNAMICS — verdict: **support-with-changes**

**Steel-man:** From thermodynamics, the back-lit instrument is not merely convenient — it is complete for the photopic question. Kirchhoff plus Planck close the one channel the proposal omits: self-emission. A room-temperature absorber's visible-band radiance carries a Planck suppression of e^(−hc/λkT) ≈ e^(−87) ≈ 10⁻³⁸ at 550 nm/300 K; to fill its own silhouette thermally the object needs ~800 K (Draper point) and then visibly glows — violating constraint 3 in the opposite direction. So elastic redistribution of ambient flux — exactly what B(y) measures — is the only channel an eye can score, and "no emission modeled" is exact, not approximate. Gate (d) honors the paid-for lesson: an absolute flux balance against the analytic angle sum at the instrument's birth, where ratio-normalized gates hid the phasor bug. And the glare arithmetic ships under the analytic-sidecar labeling convention, keeping the FDTD/analytic boundary clean.

**Attack:** The ledger row is missing — in the iteration whose whole point is building missing instruments. PANEL.md requires "absorbed energy budget + predicted re-radiation" recorded EVERY run; this spec commits ~97 runs and not one absorbed-power number. Every committed output is a ratio: per-component normalization (empty flank mean → 1) plus contrast C — the exact failure family the phasor-bug lesson names — and gate (d) anchors only the empty scene; absorption is not derivable from one observer-side plane at all. Concrete cost: the σ(I) gate, T1's flagged front-runner, must sit between ambient intensity at the object and beam intensity, in the same bench units as exp-001's beam runs. This bath is where the ambient-side denominator gets measured nearly free — one closed Poynting box per run (stage-8 machinery, σ_abs/σ_ext = 0.51 already demonstrated), summed with the same incoherent weights. Omit it and Iteration 2 re-runs the bath or trusts a reconstruction.

**Flip:** Add to the per-run recorded quantities a closed-box net absorbed-power monitor around the object — raw engine units (tied to gate (d)'s analytic anchor) plus bath-normalized — summed over (θ, λ) with the same incoherent weights, so the absolute ambient absorbed-power budget lands in the artifacts; the THERMO sidecar (absorbed power → ΔT → ~10 µm emission band → detectability) then follows analytically from that number, labeled as such.

#### QUANTUM OPTICS — verdict: **support-with-changes**

**Steel-man:** The incoherent-sum architecture is not an apology — for ambient (thermal) light it is the correct coherence model: mutually incoherent angular components add in intensity exactly, and both baseline objects are linear, so the nine-run sum is exact within the model, not approximate. More important for my seat: this baseline converts directly into the σ(I) design window T1 needs. Back-lit silhouette contrast of a weak distributed absorber is |C| ≈ τ_off, so the frozen lab bar pins the OFF state at τ_off ≤ 0.005; exp-001's beam-behind ≤ 2% pins the ON state at τ_on ≥ 3.9; any intensity-gated mechanism must therefore deliver τ_on/τ_off ≳ 800. Witness arithmetic gives I_beam/I_ambient ≈ 5×10³ at the volume, so an effective σ ∝ I^n needs n ≳ 0.8 — two-photon-class n = 1 clears it with margin. The baseline turns the leading escape route into one committed inequality.

**Attack:** Both core idioms are linear-only and the proposal never says so. Per-(θ,λ) normalization to empty-flank mean = 1 erases absolute intensity, but σ(I) lives on an absolute intensity axis; and post-hoc summation assumes superposition, which any gated object violates — the medium responds to the instantaneous total of all components plus the beam, so ambient-while-beam-on (the actual joint 1+3 test, and T3's transition observable) cannot be assembled from these runs even in principle. Dynamic range is not the obstacle: I_beam/I_ambient ≈ 5×10³ is an amplitude ratio ~70, representable in one float64 run with orders of headroom. The obstacle is architectural — no committed scale ties ambient runs to exp-001's beam units (gate (d) checks raw flux only against an analytic angle sum). As written, stage 9's baseline C cannot be re-scored against the first σ(I) object without rebuilding the instrument.

**Flip:** Commit an intensity ledger to the stage-9 artifact schema: every run's raw source amplitude recorded in exp-001 beam-source units, with a committed default I_ambient/I_beam ≈ 2×10⁻⁴ (≈5 lx beam at 45 m vs ~10⁻³ lx starlit ambient), and label the post-hoc sum as the linear-media idiom whose nonlinear replacement (simultaneous multi-angle injection, random relative phases, ensemble-averaged) must reproduce the linear sum as its future bridge gate.

#### RED TEAM (last, saw everything) — verdict: **proceed-with-mandatory-fixes**

1. **[constraint-3-violation]** The glare sidecar quietly re-scopes the hard constraint, and its committed mechanism contradicts its committed conclusion. P-V5 plus the Stiles–Holladay paragraph promote 'sub-threshold for the glare-ruined holder' to 'precisely constraint 3's phenomenology' — narrowing constraint 3 from PANEL.md's observer-generic standard (photopic is the committed hard design target) to one observer in one adaptation state at one sweep phase. That may even be the right reading of a single-witness night event, but it is a spec ruling for Director/Marsh at Checkpoint #0, not a threshold-table footnote. Worse, the cited mechanism fails its own scenario: L_v = 10E/θ² falls ~2 log units as the swept beam moves from ~1° to ~10° off the volume, so the claimed 2.5–3.5-log elevation collapses mid-sweep and the silhouette re-crosses its own committed threshold — a flickering percept, the temporal edge T3 says the eye detects best. The rescue is persistent adaptation (bleach recovery over seconds–minutes, plausibly favorable), which is uncommitted and unnumbered. Mandatory: strike 'plausibly succeeds'; log the route as hypothesis-not-result until E-at-eye, θ(t) over a sweep, and recovery time constants are pinned with sources.

2. **[inconsistency]** The frozen threshold table's field crossover cannot be derived from its own committed function. Solving 0.02·(L/3 cd·m⁻²)^−0.4 = 1 gives L*_field = 1.7×10⁻⁴ cd/m² — 4.2× the committed 4×10⁻⁵, outside the committed band [10⁻⁵–10⁻⁴], and numerically equal to the section's own moonless-rural-sky reference (1.7×10⁻⁴). Corrected, the committed clause flips: the uncued observer is at threshold on typical moonless nights, not only 'the darkest.' (I verified L*_lab = 5.3×10⁻⁶ and the lab table values 0.78/0.31/etc. — correct; the dark-adapted headline survives.) Second fragility in the same section: it cites Rose ∝ L^−0.5 but commits −0.4; under −0.5 the lab crossover is 7.5×10⁻⁵, outside the committed lab band, and the committed 'L*_lab ≥ 1 log below moonless rural' clause fails (0.35 log). Mandatory before Phase-3 freeze: re-derive both crossovers from the committed function and widen the L* bands to span the exponent uncertainty the section's own citations imply. A scoring table the whole program will freeze must be reproducible from itself. Five seats let this pass.

3. **[inconsistency]** The PASS band is undecidable under the instrument's own gate. Gate (c) accepts |C_empty| ≤ 0.01 — twice the lab PASS bar (0.005) the scoring rule commits to. An instrument allowed a 0.01 systematic in the scored quantity cannot certify |C| < 0.005, so PASS and the PASS/MARGINAL boundary are decorative for exactly the regime every future escape route occupies (|C| ≲ 0.1, which limit iii already concedes is non-robust here). Materials' dilute-sponge article (τ ≈ 0.1, Beer–Lambert band pre-registerable, convergence gate moved onto it since deep-PEC convergence does not transfer to weak extinction) is right and cheap — adopt it — but it fixes mid-scale calibration, not the floor: the collision is between gate tolerance and bar, which materials did not see. Mandatory: tighten gate (c) to ≤ 0.002 if achievable, else commit a decision floor δ_C = max measured |C_empty|, report every C ± δ_C, and mark PASS decidable only when δ_C < the bar. FAIL at |C| ≥ 0.75 is untouched; the instrument's advertised range is not.

4. **[inconsistency]** Independently verified: the oblique geometry is broken twice and both committed bands inherit it. (a) Source coverage — over the ~300+-cell source-to-plane run, walk-off D·tan40° ≈ 250–285 cells leaves a flank, the guard, and ~44% of the object window unlit in the EMPTY scene; gate (b) fails by construction at large angles, and per-(θ,λ) flank normalization then inflates half-dark components ~2× into the sum. Gate (b) samples only 0/±40°, so ±20/±30° enter the sum ungated even under a narrowed-span salvage. (b) Shadow lever — the blocking chord sits 93 cells from the plane, not 15: at 40° the shadow center lands 78 cells off-axis with a ~204-cell footprint; my nine-angle ray sum gives a geometric ceiling C ≈ −0.8 before diffraction fill, so the committed centrals (−0.90/−0.85) are unreachable and P-V2 would likely score refuted for geometry, not physics — a wasted cycle. The proposal's '≤13 cells' check used the wrong baseline. Where the critiques are soft: photonics caught only (a); photonics and EM disagree on onset (±20° vs ±10°) and fix size (≥1100 vs ≥840 cells) precisely because the proposal never pins source position or usable length — neither prescription is adoptable as written. Mandatory: pin source geometry; publish the parallelogram plus center-lever ray trace as a design calculation in NOTES.md; size the domain (or the parked TF/SF injector, honestly costed with its own suite stage) to pass gate (b) at ±40°; extend gate (a) to the 450 nm/cpl-15/40° worst corner; re-derive and re-commit P-V2/P-V3 pre-freeze, on the record; and delete the now-false 'exp-001 numerics unchanged (comparability)' rationale rather than carry a dead justification.

5. **[inconsistency]** A mandated ledger row is dropped, and the new family's only absolute anchor covers the scene with nothing in it. PANEL.md's metric table records the absorbed-energy budget EVERY run; ~97 committed runs record none. Every object-run output is a normalized ratio (per-component flank normalization, then contrast), and gate (d)'s absolute balance anchors the empty scene only — the exact failure family VALIDATION.md's phasor-bug lesson names ('ratio gates can't see convention bugs — absolute balances can'). Thermo's closed-box fix is correct and nearly free (stage-8 machinery, σ_abs/σ_ext = 0.51 already demonstrated); quantum's intensity ledger is the same schema change seen from the other side, and the synthesis should land them as ONE commitment, not two bolt-ons: per-run raw source amplitude in exp-001 beam units, closed-box absorbed power in raw and bath-normalized units, incoherent-weighted sums, plus an object-run absolute identity — energy closure (absorbed + net box flux vs incident) to a committed tolerance — so stage 9 carries an absolute gate where objects exist, not only where they don't.

6. **[unfalsifiable]** Scenario numbers are entering the permanent record without sources or pinned inputs. The sidecar's '100–200 lm → 0.01–0.1 lx at the holder's eye' hides the load-bearing glare angle — 10E/θ² spans 25× across the implied but unstated θ ≈ 0.6–3°. Quantum's committed default I_ambient/I_beam ≈ 2×10⁻⁴ rests on an uncited 5-lx-at-45-m beam (that is a ~10⁴ cd thrower — plausible for a duty light, but nowhere pinned), and the two seats' flashlight numbers are not visibly the same flashlight. None of these claims is falsifiable as stated because the scenario parameters they derive from are committed nowhere. Mandatory: one witness-scenario parameter table — distance, luminous flux, beam solid angle/candela, ambient luminance class, stray-light-at-eye, glare angle vs sweep phase — with sources and uncertainty bands, committed once in the iteration entry and cited by every seat's arithmetic. The proposal applied exactly this discipline to detection thresholds; the scenario gets no exemption.

7. **[inconsistency]** Quantum's forward inequality — the cycle's best forward product — silently hardens a convention: τ_on/τ_off ≳ 800 and n ≳ 0.8 use the LAB bar; under the committed FIELD bar (0.02) they are ≳ 195 and n ≳ 0.62 (verified: τ_on ≥ 3.9 from beam-behind ≤ 2%; (5×10³)^n thresholds). If the synthesis logs the σ(I) design window, log it as bands — τ ratio [200, 800], n [0.62, 0.78] — with the bar convention attached, or the program inherits a point estimate nobody committed. For the record, the panel's blind spot this cycle: all five critiques attacked the FDTD half and let the lead seat's own lane — the frozen perceptual table and the sidecar's internal dynamics (attacks 1–2 above) — pass unaudited, though that table is what every future iteration scores against. And for balance, two critique claims I verified and endorse on my own arithmetic: photonics' O(0.002) front-lit bound makes the back-lit C near-exact for the absorber, and materials' extinction-not-albedo argument makes P-V3's material-blindness prediction well-posed; both are worth keeping verbatim.

**Evidence that would change the verdict:** To REJECT: the pinned-geometry ray trace shows gate (b) at ±40° cannot be met within roughly the ~2× cost envelope both critiques estimate (that is Checkpoint-condition-3 major-build territory, not an Iteration-1 instrument); or the re-derived bands put the absorber's back-lit |C| within ~2× of the demonstrated empty-scene floor (the instrument cannot separate its flagship object from nothing); or vision cannot produce a self-consistent re-derivation of the L* crossover table from a single committed threshold function. To clean PROCEED: all mandatory fixes demonstrated pre-freeze in NOTES.md and the iteration entry — pinned source geometry with the published ray-trace design calculation and re-committed P-V2/P-V3 bands; a self-consistent L* table with exponent-spanning bands; gate (c) tightened below the PASS bar or an explicit committed decision floor; the glare route demoted to hypothesis with pinned E-at-eye, θ(t), and adaptation-recovery numbers; the unified energy-plus-intensity artifact schema with an object-run absolute closure gate; and the sourced witness-scenario parameter table. Note for the record: under Checkpoint #0, 'proceed' means proceed to Phase-3 synthesis and the mandated halt for Marsh's go-ahead — not to engine code or runs.

### Director's note — mandatory-fix docket carried into Phase 3 (recorded, not yet synthesized)

The synthesis happens after Marsh's go-ahead; this docket lists the panel's
demands so nothing is lost or quietly softened:

1. **Pin the oblique-source geometry end-to-end** (photonics + EM + Red Team
   #4): source position/length committed; domain widened (or the parked
   TF/SF injector adopted, honestly costed with its own suite stage) so the
   empty-scene flatness gate (b) passes at ±40°; the parallelogram +
   center-lever ray trace published as a design calculation in NOTES.md;
   P-V2/P-V3 bands re-derived and re-committed BEFORE the freeze (EM's
   geometric ceiling: C ≈ −0.8, so the proposed −0.90/−0.85 centrals are
   unreachable as written); gate (a) extended to the 450 nm / cpl-15 / 40°
   worst corner; the "exp-001 numerics unchanged" rationale deleted if the
   domain grows.
2. **Threshold-table self-consistency** (Red Team #2, arithmetic verified by
   the Director): L*_field re-derives from the committed function to
   1.7×10⁻⁴ cd/m², not the committed 4×10⁻⁵ — corrected consequence: the
   uncued observer is at threshold on TYPICAL moonless nights, not only the
   darkest. Re-derive both crossovers from the single committed function and
   widen L* bands to span the exponent uncertainty (−0.4 vs Rose's −0.5).
3. **Gate (c) vs PASS bar collision** (Red Team #3): empty-scene tolerance
   0.01 cannot certify a 0.005 PASS. Tighten to ≤ 0.002 if achievable, else
   commit a decision floor δ_C = max measured |C_empty|, report every C ±
   δ_C, PASS decidable only when δ_C < the bar.
4. **One unified energy + intensity ledger** (thermo + quantum, one schema
   commitment): per-run closed-box absorbed power (raw engine units +
   bath-normalized, stage-8 machinery), raw source amplitude recorded in
   exp-001 beam units with committed default I_ambient/I_beam, incoherent-
   weighted sums, and an object-run absolute energy-closure gate — so stage
   9 carries an absolute anchor where objects exist, not only where they
   don't (the phasor-bug lesson, again).
5. **Third calibration article** (materials): dilute sponge disk, ε ≈ 1,
   uniform σ, center-chord optical depth ≈ 0.1 (target C ≈ −0.05…−0.10),
   Beer–Lambert band pre-registered; N-convergence gate moved onto it (deep-
   PEC convergence does not transfer to weak extinction). Doubles as the
   first measured point of T1's sub-threshold class. Bonnie's absorber lane
   untouched (calibration article, not an absorber design).
6. **Glare route demoted to hypothesis-not-result** (Red Team #1): strike
   "plausibly succeeds" until E-at-eye, θ(t) across a sweep, and adaptation-
   recovery time constants are pinned with sources. Mid-sweep, L_v falls ~2
   log units as the beam moves off-axis — the static-silhouette percept
   would flicker exactly where T3 says the eye is sharpest; the rescue
   (bleach-recovery persistence) is real but currently unnumbered.
7. **Witness-scenario parameter table** (Red Team #6): distance, luminous
   flux, beam candela/solid angle, ambient luminance class, stray-light-at-
   eye, glare angle vs sweep phase — sourced, uncertainty-banded, committed
   once in this logbook, cited by every seat's arithmetic thereafter.
8. **σ(I) design window logged as BANDS with the bar convention attached**
   (quantum, corrected by Red Team #7): for I_beam/I_ambient ≈ 5×10³ —
   τ_on/τ_off ≳ 200 (field bar) … ≳ 800 (lab bar); effective exponent
   n ≳ 0.62 … 0.78. Two-photon-class n = 1 clears both with margin. This is
   the program's first quantitative mechanism specification.
9. **SPEC RULING FOR MARSH at Checkpoint #0** (Red Team #1, promoted): does
   constraint 3 bind **observer-generic** (photopic hard target — the
   standing PANEL.md reading) or **witness-specific** (the glare-adapted
   flashlight holder)? Both regimes stay measured every run regardless; the
   ruling decides what "PASS" means for the program.

Panel stats: 7 seats · 5× support-with-changes · Red Team
proceed-with-mandatory-fixes · no seat deferred · the five blind seats all
attacked the FDTD half; Red Team alone audited the lead's own lane and
found the threshold-table inconsistency — the diversity the panel exists
to buy, working on cycle one.
