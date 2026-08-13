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
  dips. **Addendum (exp-022, cloud shift 10): the 3λ feature is also
  r2=90-specific — not a portable shell-thickness law at all.** Recorded
  so nobody resurrects "integer resonance" or "shell-thickness law" as a
  mechanism class without new evidence.
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
  ambient view identically. Escape classes: σ(I) intensity gating · σ(x,t)
  switching · angular selectivity · sub-threshold weak absorption +
  scotopic ambient. **Measured (exp-020): the wall is C = −0.686 raw**;
  bench transfer |C| ≈ 0.62–0.63·τ_center; tier-split design windows —
  photopic (Tier A): τ_on/τ_off ≳ 120–780, n ≳ 0.56–0.78 (EM's g-updated
  bands); Tier-W night bar at the scenario intensity ratio: τ_on/τ_off ≳
  13, n ≳ 0.3 (vision). Two-photon-class n = 1 clears every bar.
- **T2 — Perceptual thresholds.** PINNED and corrected in exp-020: frozen
  function C_thr(L) = 0.005·max[1,(L/3)^−p], p ∈ [0.4, 0.5], field ×4;
  crossovers re-derived from the function itself (Red Team #2's catch).
  Carried: re-fit p from Blackwell's large-target low-luminance data; the
  exponent, not the bench, now decides Tier-W margins (vision, Phase 5).
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
- **T7 — Instrument floor + estimator adjudication — CLOSED for practical
  purposes, mechanism still open (Iteration 2, exp-024).** The estimator
  question is retired: at the pre-committed ±35° fallback geometry, δ_C ≤
  0.00089 at every λ, so raw C needs no correction and none is applied
  going forward — the additive-vs-ratio debate dissolves because the floor
  it argued over is gone. **But the margin/fringe-ratio model that
  motivated the whole fix was itself refuted**: MARGIN_MULT=3.5 (ratio
  3.5–4.5×, 3–4× better than exp-020's best point) still MISSED the ≤0.001
  gate at all six (λ,weighting) combinations at the primary ±40° geometry,
  non-monotonically (450 nm got *worse* despite the best ratio). Only
  dropping the ±40° angle pair (the ±35° fallback) fixed it. **New open
  question, not T7's original one: something specific to the ±40° angle
  itself, not to margin/fringe-zone ratio, drives the residual floor** —
  candidate for a fine angle sweep near ±40° in a future iteration. 750 nm's
  asterisk is lifted (fallback δ_C = 0.00043–0.00045, clean). Bonus,
  resolved as a side effect: the λ-ordering reversal exp-020 flagged is
  **not** pure floor bias — a real, small (~1.5–1.9%) growth of |C| toward
  red survives in both opaque articles at the clean-floor fallback
  geometry (absorber Δ=0.0114, PEC Δ=0.0166; sponge Δ=0.0003, noise-level)
  — a new, small, unexplained chromatic-silhouette finding, opposite the
  originally-hypothesized diffraction-fill direction.
- **T8 — Near-field → witness-scale bridge.** The bench plane sits deep in
  the shadow's Rayleigh range (z/z_R ≈ 0.04–0.06); at witness scale
  (z/z_R ~ 10⁻⁴) an LTI beam-terminating volume reads |C| ≈ 0.98 (EM,
  Phase 5) — bench Tier-W leniency is partly scale. Bridge family
  r = 78/156/312 with a committed C(z/z_R) extrapolation model before any
  near-threshold verdict is believed at scenario scale.

## PARKED (pre-panel threads, resumable — not on the program's critical path)

- ~~Is the 3λ shell-thickness feature specific to r2=90?~~ **ANSWERED
  (2026-08-12, cloud shift 10, exp-022 — old-queue shift that fired
  mid-redesign): YES, r2=90-specific.** Neither r2=75 nor r2=120
  reproduces the negative jump at their own shell=3λ points (+173.5% /
  +51.0%). Five checks, zero mechanism (impedance, angular pattern,
  eps_z, integer-λ, r2). Its queued follow-up (fine 1–2 nm λ sweep at
  fixed 30/90 geometry, or park the thread for the design-lead line)
  stays PARKED here.
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

### Phase 3 — Synthesis (2026-08-12, post-Checkpoint #0)

Marsh's rulings at Checkpoint #0: **two-tier constraint-3 scoring** (Tier W
witness-reproduced / Tier A invisible-to-anyone — recorded in PANEL.md) and
**go**. Synthesis committed as `experiments/020-ambient-baseline/NOTES.md`
+ `design_geometry.py` (the published ray-trace design calculation). All
nine docket items accepted, none overridden: windows re-registered (flanks
→ [185, 263] relative — the 40° penumbra reaches 180); domain 360×1200
(full-span coverage verified at all 17 angles, min margin 69.9 cells);
geometric ceilings C_geo = −0.799/−0.809 → committed bands P2/P3 ∈
[−0.82, −0.55] with a falsifiable λ-ordering from the Fresnel numbers;
threshold crossovers re-derived with the exponent band (L*_lab ∈
[5.3×10⁻⁶, 7.5×10⁻⁵], L*_field ∈ [1.7×10⁻⁴, 1.2×10⁻³] cd/m² — the
corrected reading: uncued observers are at threshold on typical moonless
nights); decision-floor rule replaces the loose empty gate; energy +
intensity ledger lands experiment-side (the contract-file schema bump is
deferred to a counterparty PR — Bonnie's lane, not amended unilaterally);
dilute-sponge third article adopted; glare route held at
hypothesis-not-result; σ(I) window logged as bands (τ_on/τ_off ≳ 200–800,
n ≳ 0.62–0.78). exp-020 scores **Tier A only**; Tier W deferred pending
the witness-scenario parameter table (docket #7 → Phase 5). Predictions
P1–P7 committed before the instrument build.

### Phase 4 — Test (exp-020, 2026-08-12)

124 runs, 472 s, suite 43/43 before and after. Full detail:
`experiments/020-ambient-baseline/NOTES.md` (results + scored predictions).
Metric row (V-weighted, back-lit, plane 15): **absorber C = −0.686** (raw;
Tier-A photopic FAIL ×34 field bar) · PEC −0.826 · dilute sponge −0.0685
(floor-corrected on its geometric −0.0626 to 0.001) · δ_C floor 0.0009 /
0.0068 / 0.0183 at 450/600/750 nm · material blindness only to ~20%
(|ΔC| = 0.140, rim transmission) · ledger identities 17–200× inside gates.
Honest misses: P1a floor clause at 600/750, P1b 0.795 vs 0.8 at 750/±40°,
P2 λ-ordering reversed raw, P3 band edge by 0.02. **Per Red Team (below):
750 nm object numbers carry an asterisk, and "floor-corrected" values are
estimator-dependent, until Iteration 2's adjudication rerun.**

### Phase 5 — Review (seven fresh seats, blind, verbatim)

#### VISION SCIENCE

**Reading:** Constraint 3's cost is now measured, and the perceptual geometry shifted twice. First: |C| = 0.686 is 34× the uncued photopic bar — unmissable in any daylight adaptation state; Tier A stays closed to static absorbers. Second, the surprise: the REAL article's field crossover, [4.4×10⁻⁴, 2.6×10⁻³] cd/m², sits above moonless sky — darkness alone already hides it from uncued observers, and the cued dark-adapted margin at 1.7×10⁻⁴ is only 1.0–2.7×, inside the p ∈ [0.4, 0.5] band: the threshold exponent, not the bench, now decides Tier W. Floor-corrected λ-flatness makes the silhouette achromatic — V/V′ single-number scoring is complete. The δ_C floor is perceptually asymmetric: photopic verdicts ride 600 nm (0.0068 > lab bar — photopic-lab PASS undecidable), scotopic rides 450 nm (0.0009, decidable now); 750 nm is near-weightless in both systems. The 0.14 PEC–absorber split, photopically plain, is perceptually nil at night — night silhouettes carry no material identity.

**Argued next change:** Execute docket #7 as the one next change: the sourced witness-scenario parameter table plus the glare/adaptation sidecar, scoring Tier W's static-silhouette clause against the measured C = −0.686. Analytic, zero runs, sidecar-labeled. Committed parameters: distance 45 m [30–60]; flashlight 100–200 lm, beam 5×10³–2×10⁴ cd; stray-light-at-eye E ∈ [0.01, 0.1] lx; ambient classes 10⁻⁵–10⁻³ cd/m², moonless-sky anchor 1.7×10⁻⁴; glare angle θ(t) 0.5°→10° over a 1–3 s sweep; Stiles–Holladay veil L_v = 10E/θ²; adaptation persistence as a Crawford equivalent background L_eq(t) with sourced recovery constants (half-times ≥ 10 s at these exposures — Crawford 1946; Hecht et al. 1937; Pugh & Lamb 2000), answering Red Team #1's collapse objection: threshold elevation outlives the θ⁻² veil on sweep timescales. Verdict quantity: minimum over sweep phase of C_thr(L_bg+L_v+L_eq)/C_eff, with C_eff = 0.686·L_bg/(L_bg+L_v+L_eq); both exponents, both bars. My arithmetic says it closes 4–21× sub-threshold at E = 0.01–0.1 lx. If confirmed, glare goes hypothesis→result, Tier W's constraint-3 clause is banked for the existing article, and Tier W reduces to constraint 4, where the loosened night window applies.

**Ranked top-3:**
1. Complete docket #7 (witness-scenario table + glare/adaptation sidecar) and score Tier W's static-silhouette clause on the measured C — zero runs, converts the program's founding constraint-3 question from hypothesis to result.
2. Re-freeze the perceptual scaffolding before the next scoring run: tier-split the mechanism design windows (Tier-W night bar at the committed 5×10³ intensity ratio needs only τ_on/τ_off ≳ 13, n ≳ 0.3, vs 200–800 / 0.62–0.78 photopic), re-fit exponent p from Blackwell's large-target low-luminance data, and gate the ny+80 floor fix on δ_C(600 nm) < 0.005 — the perceptually binding wavelength.
3. Build the stage-10 temporal instrument with temporal-contrast bars pinned first (de Lange / Watson TCSF, sourced) — the phenomenon is a sweep, the eye's temporal channel beats its static one, and the switch transient (T3) is the last unmeasured perceptual axis.

#### PHOTONICS

**Reading:** The back-lit channel reads projected extinction, and exp-020 located exactly where that bends. The 0.140 absorber–PEC split is mostly rim transmission: Beer–Lambert chord integrals over the stage-7 σ(r)=0.5·s(d)² profile (recomputed this review) give T=0.5 at p≈62 cells — a ~16-cell, ~0.8λ semi-transparent annulus — predicting a 0.123 split; the ~0.017 remainder is differential edge physics: the hard PEC edge concentrates near-field extinction in-window (−0.818 vs the −0.799 ray ceiling; plane <λ from the rim, N_F≈3), while the adiabatic rim shows almost none (+0.004) and the sponge none (0.001). Ray traces are band centers, not ceilings, and the error scales with edge hardness. Diffraction fill is λ-flat at N_F 2.6–4.4 (article extinction is λ-flat by construction: per-cell conductivity), so the dataset's largest chromatic term is the instrument's own floor — δ_C=0.0183 at 750 nm, fringe zone 74.7 > 69.9-cell margin — making chromatic signatures below 0.02 unfalsifiable at red.

**Argued next change:** Build the front-lit reflectance channel — completing the constraint-3 instrument — with a wave-corrected design sidecar and the fringe-margin fix in one build. Parameters: mirror the angled line source to the observer side (x=40, +x propagation), θ∈{0,±10,±20,±30,±40}°, 450/600/750 nm, all four exp-020 articles (108 runs + gates). Observable: C_front on the existing x=77 plane and windows, reading observer-directed (−x) flux — direct transit is +x, so the quadrature-phasor direction split isolates returned light; normalize to the back-lit empty flank mean via the intensity ledger (source amplitude 1.0), making C_total = C_back + C_front one unit system (linear-media idiom, labeled). Absolute gates: flat-PEC-mirror return identity at 0°/30°; committed front-lit empty floor δ_front; reciprocity σ_abs(θ) front-vs-back ≤ 12%. Domain ny 1200→1280 (coverage margin ~110 > 74.7-cell fringe zone at 750 nm); gate: re-measured δ_C ≤ 0.005 at every λ, fallback trim to ±35°. Sidecar post-dictions committed before any new band: Beer–Lambert chord integral reproduces the 0.140 split (my check: 0.123 geometric, residual = edge term); Fresnel–Kirchhoff strip reproduces PEC's −0.019 excess ±0.01. Predictions: absorber C_front ∈ [0, +0.005]; PEC C_front ≥ +0.05, strongly θ-structured — material blindness broken.

**Ranked top-3:**
1. Front-lit ambient channel with the wave-corrected design sidecar and ny fringe-margin fix — completes constraint-3 instrumentation and breaks the back-lit channel's measured ~20%-ceiling material blindness.
2. Tier-W closure on the existing absorber: commit docket #7's witness photometry (beam candela, solid angle, stray-light illuminance at eye versus sweep angle) and score the measured C=−0.686 through the glare-elevated threshold, since constraints 1+2+3 may already hold witness-side.
3. First T1 mechanism article using existing engine physics: an angular-selective volume-Bragg notch deflecting only the beam cone into an internal absorbing sink (termination, not routing — R1-compliant), with the broadband-versus-angular-acceptance étendue tension pre-registered as its kill criterion.

#### MATERIALS & METAMATERIALS

**Reading:** For this seat the calibration is the result: the dilute sponge landed on its pre-committed geometric value to 0.001 after floor correction, so Beer–Lambert chord models are now predictive design tools — the weak-extinction regime every escape route's OFF state occupies is a design space, and articles can be placed at a target C rather than discovered there. The 0.14 absorber–PEC split is the channel's first material signature: back-lit C reads the radial extinction profile, not albedo — the graded coat's thin rim chords transmit, giving a silhouette-effective radius ~0.83x geometric. Rim grading designed for constraint 2 apodized the constraint-3 silhouette ~17% for free: the first measured coat-design lever. Cautions: PEC ran 0.02 deeper than the ray-trace ceiling (near-field excess — ray traces are not ceilings for hard reflectors), and the λ-dependent floor makes lab-bar certification 450-nm-only until ny grows. P7's corollary: blackness beyond beam-stopping is pure silhouette cost.

**Argued next change:** The σ(I)-endpoint static article pair on the calibrated sponge platform: measure both ends of the switching trajectory with zero new engine physics. Prerequisite (pre-registered in exp-020's Next): widen ny 1200 to 1280 so the 750 nm fringe zone (74.7 cells) sits inside the coverage margin; re-measure per-λ δ_C and gate δ_C ≤ 0.002 at every λ so both bars are decidable. Articles — r = 78, ε = 1, uniform σ, no PEC core: OFF-lab τ_center = 0.008 (σ = 5.1e-5, chord-model C = −0.005); OFF-field τ_center = 0.032 (σ = 2.05e-4, C = −0.020); ON τ_center = 3.9 (σ = 2.50e-2, chord-model C ≈ −0.73, band [−0.79, −0.65]); plus the τ = 0.10 sponge re-run as the cross-domain tie. Ambient channel on all; exp-001 beam-behind and observer-return on ON — a coreless distributed absorber must re-earn beam-behind ≤ 2% (chord model 2%, band 1.5–6%). Yield: the σ(I) window's endpoints become measured numbers, and disk chord asymmetry — beam takes the thick center chord, ambient averages thin rim chords — should relax the required switching ratio from ~195 to ~122 (field bar). Realizability: static endpoints are published-class (dilute absorbing aerosol); the CW-intensity gating between them is the open half this pair parameterizes.

**Ranked top-3:**
1. σ(I)-endpoint static pair — OFF sponges designed to the two frozen bars plus a coreless τ=3.9 ON article, after the ny+80 floor fix — measuring the switching window's endpoints on today's linear bench.
2. Front-lit reflectance channel, with the 0.14 rim transmission recast as a pre-registered absorber-vs-PEC front-lit split prediction — the albedo channel that realizability grading of any coat needs.
3. Graded-rim apodization curve — a grade-length family at fixed beam-stopping center depth, turning the 0.14 signature into a σ(r)-to-silhouette design rule that minimizes ON-state visibility for Tier-W margin.

#### ELECTROMAGNETISM

**Reading:** Anchors green at oblique incidence (empty-box 0.0012, two-route 0.0006, Beer–Lambert to 0.001): every C is trustworthy. The surprises are all near-zone geometry. Our plane sits deep inside the shadow's Rayleigh range r²/λ ≈ 243–406 cells (z/z_R ≈ 0.04–0.06), so far-zone diffraction fill is absent — explaining both PEC's 0.02 overshoot of the ray ceiling and the refuted λ-ordering (far-zone fill scaling misapplied to a near-zone plane). The 0.14 split is rim-chord transmission: ray optics, λ-flat. The δ_C floor is Fresnel edge-fringe leakage — margin/√(λD) crossed unity at 750 nm; cancellation degraded twentyfold. T1 math updates two ways: measured g = |C|/τ_center = 0.62 relaxes the σ(I) window to τ_on/τ_off ≳ 120–780, n ≳ 0.56–0.78 (conventions attached); but P7's leniency is partly bench-scale — a beam-terminating LTI volume at witness scale (z/z_R ~ 10⁻⁴) reads |C| ≈ 0.98, near the perfect-absorber crossovers.

**Argued next change:** Retire the λ-dependent decision floor at its source before any near-invisible article is scored. Concrete: widen the transverse domain ny 1200 → 1360 (+80 cells per side), object recentered at (170, 680), source line y ∈ [40, 1320] with taper 40, everything else frozen (Δ = 30 nm, D_source→plane = 223, θ ∈ {0, ±10, ±20, ±30, ±40}°, windows fixed relative to object center). Worst-corner flat-lit margin rises 69.9 → 150 cells at both signs of ±40°. Commit the design rule permanently — coverage margin m ≥ 2√(λ_max·D) = 149.3 cells, certified by re-running design_geometry.py at all 17 angles — as a stage-9/P1-class gate. Do NOT trim the angular span (buys margin by discarding fill-in light and the per-θ information the angular-selectivity class needs) and do NOT move the source (re-opens proven oblique gates; widening is strictly additive). Pre-registered outcomes: re-run the 27 empty scenes + convergence empties; δ_C(λ) collapses onto one curve in m/√(λD) with δ_C ≤ 0.002 at every λ (450 nm already reads 0.0009 at ratio 1.21); P1b coverage ≥ 0.8 at 750/±40°. Lab-bar PASS becomes decidable band-wide. Cost ≈ +13% cells, minutes. Floor subtraction stays a cross-check, not a crutch — at |C| ≈ 0.005 bias and signal are same-order.

**Ranked top-3:**
1. Fix the fringe-zone floor first: ny 1200→1360 plus the permanent coverage-margin gate m ≥ 2√(λ_max·D), pre-registering δ_C ≤ 0.002 at every λ — the prerequisite for any future lab-bar PASS verdict.
2. Then the first σ(I) mechanism iteration (checkpoint-3 engine build — nonlinearity is T1's formally clean escape: passive, causal, σ ≥ 0 throughout), gated by an EM bridge identity that the nonlinear engine at vanishing beam intensity reproduces exp-020's linear C within δ_C, scored against the updated window τ_on/τ_off ≳ 120–780, n ≳ 0.56–0.78.
3. A near-to-far-field scale bridge: PEC and fixed-τ sponge at r = 78/156/312 cells with a committed C(z/z_R) extrapolation model, separating scale-invariant rim-chord fill from decaying diffraction terms, so bench silhouettes convert to witness-scale claims before any near-threshold verdict is believed.

#### THERMODYNAMICS

**Reading:** The ledger is the quiet headline: every identity passed 17–200× inside gate (empty-box 0.0012 vs 0.02; two-route σ_ext 0.0006 vs 0.12), and σ_abs/σ_ext = 0.51 reproduced at oblique incidence — the absolute anchor now exists where objects exist, the phasor-bug lesson made standing machinery. Two results are energy stories. PEC at −0.818 corrected, 0.02 past the ray ceiling: extinction removes ~2× geometric blocking (the paradox) and the forward lobe has not refilled the shadow at 15 cells — near planes can undershoot ray ceilings. The 0.14 absorber–PEC split: where extinction goes is now visible even back-lit — the graded rim transmits low-τ chords; material-blindness holds only to ~20%. Kirchhoff confirmed: floor-corrected λ-flat C is pure elastic redistribution; visible self-emission stays Planck-suppressed (e^−87). The witness-scale sidecar remains blocked on docket #7's missing watts.

**Argued next change:** Build the time-resolved energy ledger now — the mandatory suite stage before any σ(t)/σ(I) engine work. Every existing energy identity is stationary: quadrature-phasor, cycle-averaged, CW. σ(t) breaks stationarity, σ(I) breaks superposition, so current gates go blind exactly where the flagged front-runner lives — the phasor-bug precondition recreated. Concrete: on the existing stage-8 box, record three per-step scalars — U(t) = Σ½(εEz² + μ|H|²)ΔV (B·μ⁻¹B on tensor articles), P_J(t) = ΣσEz²ΔV, P_box(t) = net instantaneous Poynting influx (half-step-centered). Gates: (i) discrete closure |ΔU − ∫(P_box − P_J)dt| ≤ 1% of absorbed energy (lossy) or peak stored energy (lossless); (ii) passivity canary min_t P_J(t) ≥ 0 — trivial now, load-bearing once σ varies; (iii) bridge: final-3-cycle mean P_J/i_inc reproduces phasor-route σ_abs within 2% on absorber and sponge (Beer–Lambert analytic), θ = 0 and 30°. Validate on all four exp-020 articles; empty and PEC test pure flux–storage closure (P_J ≡ 0). Cost: three scalars per timestep, a handful of runs, no new physics class, no checkpoint-3 trip; lands experiment-side per docket #4 precedent, schema bump stays in the counterparty PR. Payoff: T3's switch transient gets an energy budget (stored U at switch bounds the observable); gated absorbers get a passivity gate.

**Ranked top-3:**
1. Time-resolved energy ledger (per-step U, P_Joule, P_box with closure, passivity, and phasor-bridge gates, validated on the four exp-020 articles) as the suite stage that must precede any sigma(t)/sigma(I) build.
2. Witness-scenario parameter table (docket #7) extended with thermo columns — radiant watts from lumens, beam candela/solid angle, sweep dwell time, volume dimensions, absorbing-medium heat-capacity class — unblocking Tier-W scoring and the witness-scale sidecar (absorbed joules -> Delta-T -> 10 um re-emission -> detectability).
3. Front-lit reflectance channel with per-article energy-channel decomposition (absorbed/scattered/transmitted from the existing box ledger) to attribute the measured 0.14 rim-transmission split and price constraint 2's glint term.

#### QUANTUM OPTICS

**Reading:** The coherence model performed as it must, and the decisive number for my seat is the smallest one: the dilute sponge landed on its pre-committed geometric value to 0.001 (floor-corrected −0.062 vs −0.0626). The weak-extinction regime — where every σ(I) OFF state will be scored — is now calibrated: bench transfer |C| ≈ 0.63·τ_center, so the field bar needs τ_off ≲ 0.03, the lab bar ≲ 0.008; the committed τ_on/τ_off ≥ 200–800 window stands, and two-photon-class n = 1 (ratio = I_beam/I_ambient = 5×10³) clears both — its predicted OFF silhouette, |C| ≈ 5×10⁻⁴, would pass constraint 3 photopically. The surprise: that value sits below the decision floor everywhere except 450 nm (δ_C = 0.0068/0.0183 at 600/750) — the λ-dependent fringe floor, not physics, is now the σ(I) program's binding constraint. And the window's two ends still live in different units: ambient runs share no committed intensity axis with exp-001's beam.

**Argued next change:** One instrument commitment, no new material physics — make the bench σ(I)-ready before any gated article. (a) Shared intensity axis: every run's ledger gains intensity_role ∈ {ambient_component, beam, joint} and amp_rel = source amplitude in exp-001 beam units (beam ≡ 1.0); commit scenario default I_ambient/I_beam = 2×10⁻⁴ (per-component amplitude √(2.22×10⁻⁵) ≈ 4.7×10⁻³), banded [10⁻⁵, 10⁻³] until docket #7 pins it; ambient sources injected at physical amplitude, flank normalization moved to report side; experiment-side fields only — the contract bump stays in Bonnie's counterparty PR. (b) The linear-idiom bridge gate, new stage-9 checks: simultaneous nine-angle injection, random phases φᵢ ~ U[0, 2π), M = 12 draws, 600 nm — |⟨C_joint⟩ − C_posthoc| ≤ max(δ_C, 0.005) on empty AND sponge; plus one joint beam+ambient run on the linear sponge reproducing beam-behind and C simultaneously (superposition as the absolute identity). The ensemble spread doubles as the ambient speckle statistic any fast gate would false-fire on (I_gate ≳ 30×Ī_amb keeps exponential tails ~10⁻¹³). (c) Fold in the fringe fix: ny 1200 → 1280, margin ~110 > 74.7-cell fringe at 750; target δ_C ≤ 0.005 at all λ, else a two-photon OFF state is scorable only at 450 nm.

**Ranked top-3:**
1. σ(I)-readiness package (the change above): shared intensity units, coherent-superposition bridge gate proven on linear articles, 750 nm floor fix — one iteration, no new material physics.
2. First intensity-gated article: two-photon-class σ(I) = σ₂·⟨I⟩ with a committed averaging window, sponge-disk geometry, σ₂ set so τ_on = 3.9 at beam intensity (τ_off = 7.8×10⁻⁴ follows), scored against its two pre-measured linear endpoint articles — flagged Checkpoint-3 engine work, and its turn-on transient becomes stage-10/T3's first target.
3. Witness-scenario parameter table (docket #7) to pin I_beam/I_ambient with sources: the window's x-axis rests on an uncited 5-lx beam, and at the band's low end (~10³) n = 1's lab-bar margin thins to ~1.2×.

#### RED TEAM

**Reading:** Scoring discipline largely held: verdicts ran on raw numbers against committed bands; P2's ordering and P3's edge scored REFUTED, not excused; the headline −0.686 is raw and Tier-A-honest; no ruled-out idea resurfaces; tiers are not collapsing. Two integrity defects. First, P1b's pre-committed consequence — "no object number is interpreted" — was softened post-hoc to "doesn't touch any conclusion" after the 750 nm gate failed at 0.795 vs 0.8. Second, floor SUBTRACTION is an uncommitted estimator: the frozen rule was ±δ_C bands. Under the equally physical illumination-ratio model, (1+C)/(1+C_empty)−1, the absorber reads −0.676/−0.684/−0.690 — the reversed ordering survives; "wavelength-flat to ±0.003" and "entirely the empty-floor bias" are additive-model artifacts until adjudicated. Estimator-robust: the 34× Tier-A FAIL, sponge-to-geometric 0.001, the 0.140 material split. Also: PEC-below-ceiling got a mechanism story despite a monotone N-drift and no N17-angle-set ceiling recompute — R3's meta-rule, under-applied.

**Argued next change:** One instrument-integrity iteration before any future claim quotes "floor-corrected" numbers. (a) Adopt the results' own margin fix, pinned: ny 1200 → 1280, source line y ∈ [40, 1240], object center (170, 640), windows re-registered by re-running design_geometry.py; target coverage margin ≥ 110 cells > the 74.7-cell fringe zone at 750 nm. (b) Re-run empty + absorber + PEC + sponge at 600 and 750 nm, 9 angles each — 72 runs, ~5 min at exp-020 pace. Pre-commit three clauses: (i) δ_C ≤ 0.003 at both λ; (ii) estimator adjudication — with the floor collapsed, raw absorber C(750) ≈ −0.678 vindicates the additive subtraction, ≈ −0.690 vindicates the ratio model and forces restating every floor-corrected interpretive claim (λ-flatness first); (iii) P1b ≥ 0.8 at all committed angles — the violated stop rule returns to green rather than staying reinterpreted; until then 750 nm object numbers carry an explicit asterisk in LOGBOOK. (c) Zero-run rider: recompute C_geo for the N17 angle set and re-check the PEC N-series against it before "near-field extinction excess" or "rim transmission" becomes a front-lit design input (R3 meta-rule: check before mechanism story).

**Ranked top-3:**
1. Instrument-margin + estimator-adjudication rerun (the next_change): collapse the 750 nm fringe floor, adjudicate additive-vs-ratio floor correction, restore P1b to green — no floor-corrected claim feeds forward until this lands.
2. Witness-scenario parameter table (docket #7): sourced, uncertainty-banded distance/candela/glare-angle-vs-sweep-phase/adaptation-recovery numbers — converts the glare route from unfalsifiable sidecar to testable Tier-W arithmetic.
3. First sigma(I) mechanism test at the calibrated weak-extinction operating point (tau_off <= 0.02, tau_on/tau_off in [200, 800], n in [0.62, 0.78]) — keeps a Tier-A mechanism iteration committed so the program cannot drift into Tier-W-only work.

### Director's close of Iteration 1

**VERDICT: PROMISING.** The instrument exists with absolute anchors
(Beer–Lambert to 0.001, oblique energy identities to 0.0006); the wall is
measured (absorber C = −0.686 raw, Tier-A photopic FAIL ×34); the
weak-extinction regime every OFF-state lives in is calibrated to 0.001;
the channel's first material signature is in hand (0.140 rim
transmission); and Tier W cracked open twice — P7's sharpening (a real
imperfect black beats the perfect-absorber crossover arithmetic) and the
vision seat's glare/adaptation arithmetic (4–21× sub-threshold for the
flashlight holder, pending docket #7 sources).

**Red Team integrity items — ACCEPTED, both:** (1) P1b's pre-committed
stop rule ("no object number is interpreted") was softened post-hoc after
the 750 nm miss; the softening is retracted — 750 nm object numbers carry
an explicit asterisk until P1b returns to green. (2) Additive floor
subtraction is an uncommitted estimator (a ratio model preserves the raw
λ-ordering); every "floor-corrected" interpretive claim (λ-flatness
first) is provisional until Iteration 2's pre-committed estimator
adjudication. The frozen rule (raw C ± δ_C) remains the only committed
currency. R3 rider accepted too: the PEC near-field-excess mechanism
story gets its N17 ceiling recompute before feeding any design.

**Merged ranking (Iteration 2/3/4 queue):**
1. **Iteration 2 — instrument margin + adjudication rerun** (lead:
   PHOTONICS, per rotation): ny 1200→1360 with EM's permanent coverage
   rule m ≥ 2√(λ_max·D) ≈ 149 cells; design_geometry re-run at all 17
   angles; Red Team's three pre-committed clauses (δ_C ≤ 0.003 at
   600/750; estimator adjudication — collapsed-floor raw C(750) ≈ −0.678
   vindicates additive, ≈ −0.690 vindicates ratio; P1b ≥ 0.8 everywhere);
   N17 ceiling recompute rider. ~72–108 runs.
2. **Iteration 3 — docket #7, the witness-scenario table + glare/
   adaptation sidecar** (zero runs, analytic, sidecar-labeled): vision's
   parameter spec + thermo's watt columns + quantum's intensity-ratio
   pinning; scores Tier W's constraint-3 clause on measured C. If the
   4–21× closure holds, that is **checkpoint criterion 1 (Tier W,
   constraints 1+2+3)** — constraint 4 becomes Tier W's last open axis.
3. **Iteration 4 — σ(I) readiness, then the first gated article**:
   thermo's time-resolved energy ledger stage (the stationarity-breaking
   precondition), quantum's shared intensity axis + coherent-superposition
   bridge gate, materials' OFF/ON endpoint article pair — then the
   two-photon-class σ(I) article (checkpoint criterion 3: engine build).

Panel stats (Phase 5): 7 seats · consensus without collusion (blind seats
converged on the same three clusters from different arguments) · Red Team
audited the Director and scored two hits — the loop polices itself.
Carried questions: estimator adjudication; exponent p re-fit from
Blackwell low-luminance data; near-field→witness-scale bridge (EM: a
witness-scale LTI absorber reads |C| ≈ 0.98 — bench leniency is partly
scale); T3 temporal instrument with TCSF bars.

## Iteration 2 — Instrument Margin + Estimator Adjudication (exp-024) — 2026-08-12

Runner: cloud panel shift (background routine) · Lead: **PHOTONICS** (rotation)
· Phases run: **1–5, complete** · 7 fresh-context seats, Phase-2 critiques
written blind and in parallel; Red Team read everything and spoke last.

### Phase 1 — Proposal (PHOTONICS, verbatim)

# PHASE 1 — PROPOSAL · Panel Iteration 2 · Lead seat: PHOTONICS
## "Instrument Margin + Estimator Adjudication" — collapsing the λ-dependent fringe-zone floor, settling the additive-vs-ratio question, and clearing the P1b/N17 riders on exp-020's ambient instrument (candidate exp-024)

### 1. Narrative (≤300 words)

Iteration 1 built the ambient-appearance instrument and put a number on constraint 3 for the first time: absorber C = −0.686, a photopic Tier-A FAIL by 34× the field bar. But its own data flagged an instrument defect, not a material result. Past a coverage margin of ~60–70 cells, the flat-lit source's own edge-diffraction fringe zone (√(λD) = 58/67/75 cells at 450/600/750 nm) overruns the margin (69.9 cells) at 600 and 750 nm, leaking a λ-growing empty-scene floor (δ_C = 0.0009/0.0068/0.0183) into every window mean. That floor did two damaging things at once: it silently *reversed* my own seat's committed λ-ordering prediction (raw |C| grew with λ; diffraction-fill physics says it should shrink), and it left two floor-correction estimators — additive subtraction vs. the illumination-ratio model — disagreeing about whether the reversal was pure bias or partly real. No physics conclusion can be trusted while the floor itself is uncertified.

This iteration is an INSTRUMENT FIX, not a new mechanism test. Same four articles (empty / absorber / PEC / sponge), same object, same windows, same nine committed angles — only the transverse domain, source length, and object center move outward so the source's flat-lit region clears the fringe zone by ≥2× at every committed wavelength, everywhere the old margin fell short. With the floor pushed below ~0.001–0.002 at all three λ, raw C becomes trustworthy C without correction: the additive-vs-ratio question should mostly *dissolve* rather than get won by either side, and my seat's λ-ordering claim becomes decidable at a resolution an order of magnitude finer than Iteration 1 could support. A zero-run rider recomputes the ray-trace ceiling at 17 angles and checks the measured PEC near-field excess against it before that excess is trusted as a real effect. Nothing about T1's escape-route classes, the perceptual threshold table, or any material mechanism is touched.

### 2. Parameter table

**Design recomputation (shown work):**

```
D_source→plane  = SRC_X − PLANE_X = 300 − 77 = 223 cells       (frozen)
walk(40°) = 223 × tan(40°) = 187.12 cells
New SRC_Y = (40, 1320)  [was (40, 1160)]
margin(θ=±40°) = 149.88 cells  (was 69.88)
Coverage rule (EM, Phase 5): m ≥ 2·√(λ_max·D) = 149.32 cells → CLEARS by 0.56 cells (0.38%)
Fringe zones √(λ·D): 57.8 / 66.8 / 74.7 cells @ 450/600/750 nm
New margin/fringe ratio: 2.591 / 2.244 / 2.007  (old: 1.209 / 1.047 / 0.936)
N9 ceiling: C_geo −0.799(equal)/−0.809(cos); N17 ceiling (my recompute): −0.809/−0.818
PEC N-series excess: N9 −0.0271, N17 −0.0286 (essentially N-stable)
```

Full parameter table (key revisions): NY 1200→1360, source y∈[40,1320], object recentered (170,600)→(170,680), BOX (80,260,510,690)→(80,260,590,770), new permanent coverage-margin rule m ≥ 2√(λ_max·D), δ_C ≤0.003 gate at 600/750nm (Red Team clause i), P1b ≥0.8 everywhere (clause iii), additive floor-subtraction retired as ongoing procedure (clause ii), N17 ceiling recomputed and PEC excess checked against it (zero-run rider). Everything else (grid physics, source x-placement, window geometry relative to object, angle sets, weighting schemes, incoherent-sum machinery, suite stage 9) carried unchanged.

### 3. T1 escape-route statement

This iteration implements no escape mechanism and measures nothing new about escape routes — pure instrument hygiene, re-measuring the existing baseline (empty/absorber/PEC/sponge, materially unmodified) on a corrected instrument.

### 4. Falsifiable predicted outcomes (own optical reasoning)

P-PH1 (δ_C ≤0.003 gate): predicted δ_C(450/600/750) ∈ [0.0001,0.0010]/[0.0002,0.0018]/[0.0002,0.0025], extrapolated via two bracketing power laws (1/ratio, 1/ratio²) calibrated to the single 450nm anchor. P-PH2 (P1b ≥0.94 everywhere). P-PH3 (absorber C∈[−0.71,−0.66], λ-ordering |C(750)−C(450)|≤0.006, diffraction-fill argument). P-EST (estimator adjudication: raw C(750)∈[−0.695,−0.675], central −0.682 — predicted to land near the additive-corrected flat band, "estimator question mostly dissolves"). P-PH4 (PEC C∈[−0.85,−0.80], split 0.14±0.02). P-N17 (PEC N17 excess 0.025–0.035 over recomputed ceiling). P-PH5 (sponge C∈[−0.075,−0.055]). P-PH6/P-PH7 (convergence/ledger gates unchanged, predicted clean).

### 5. Idealizations

2D TMz; linear-media idiom unchanged; back-lit only; the coverage-margin rule extrapolated from a single anchor point via two untested bracketing models — flagged as the proposal's own acknowledged weak point, with a pre-committed ±35° fallback already on the table if it proves too thin.

### 6. Carried forward vs. revised — full accounting in the proposal (grid physics/window geometry/angle sets/incoherent-sum machinery carried; NY/source-extent/object-recenter/δ_C-gate/P1b-bar/estimator-retirement/N17-ceiling all revised, each with a stated reason).

*(Full proposal text: see PHOTONICS' Phase-1 sub-agent output, 2026-08-12 —
condensed here for LOGBOOK length; nothing material omitted from what Phase
2/3 acted on.)*

### Phase 2 — Critiques (five seats, blind, verbatim)

#### VISION SCIENCE — verdict: support-with-changes

**Steel-man:** Vision science's charter demands PASS be decidable, not just FAIL. Iteration 1's own retrospective (Materials, Phase 5) named the instrument's core defect precisely: it can certify FAIL but never PASS, because δ_C (0.0068/0.0183 at 600/750 nm) sat above or near the 0.005 lab bar. This proposal is the direct, targeted fix — extrapolated δ_C bands of 0.0002–0.0025 and a hard δ_C ≤ 0.003 gate at 600/750 nm, backed by a permanent, re-derivable coverage-margin design rule (m ≥ 2√(λ_max·D)) rather than an ad hoc patch. It touches none of my frozen machinery, and it is honest that this cycle re-measures known-FAIL articles rather than claiming a new perceptual result.

**Attack:** The proposal frames itself as unblocking "any σ(I) article," but its own gate is calibrated to the wrong signal. The logbook already pins the concrete near-threshold target this fix exists to serve: Materials' OFF-lab σ(I) article, τ_center=0.008, chord-model C = −0.005 — sitting exactly on the lab PASS bar. The proposal's hard gate is δ_C ≤ 0.003, giving SNR ≈ 1.7 — nowhere near the ≥3–5× separation ordinary detection-theory practice would require. "Unblocks the whole program's future C measurements including any σ(I) article" is asserted, not shown.

**Verdict:** support-with-changes. **Flip:** Tighten the decision-floor gate from δ_C ≤ 0.003 to δ_C ≤ 0.001 at every λ.

#### MATERIALS & METAMATERIALS — verdict: support-with-changes

**Steel-man:** The proposal correctly leaves my calibration article's physical design untouched. The sponge's signal (|C|≈0.062) already sat ≥3.4× Iteration 1's worst δ_C, so this was always the instrument's most trustworthy article, and the N17 ceiling recompute + PEC-excess stability check properly applies the R3 meta-rule.

**Attack:** P-EST's "estimator dissolves" claim and P-PH5 both lean on P-PH1's δ_C(750) band — extrapolated from a SINGLE validated anchor via two power laws that agree only because both are forced through that one point. The new margin/fringe ratios (2.01–2.59) sit near, not deep inside, the Fresnel regime, where fringe amplitude follows Cornu-spiral oscillation rather than monotone decay — the bracket could miss a secondary lobe and underpredict δ_C(750) by an order of magnitude.

**Verdict:** support-with-changes. **Flip:** Pre-commit that if δ_C(750) lands outside P-PH1's predicted band, the sponge C and g-value are automatically re-derived against whichever angle set was actually used.

#### ELECTROMAGNETISM — verdict: support-with-changes

**Steel-man:** The margin arithmetic checks out independently — D=223, walk(40°)=187.12, margin=149.88 vs rule=149.32, both reproduce to the printed digit. The N17 ceiling recompute rules out ceiling-coarseness for the PEC near-field excess without overclaiming resolution of the mechanism, correctly deferring to my T8 near-to-far bridge.

**Attack:** P-PH1's δ_C bands rest on an unsound extrapolation. Fitting a power law to Iteration 1's OWN three data points gives an effective exponent p≈11.8 between the 450 and 750nm points — nowhere near the proposal's bracketing p=1/p=2. That extreme steepness is my own Phase-5 finding restated: margin/√(λD) crossing unity at 750nm produced a "twentyfold" cancellation collapse — a near-threshold transition, not a smooth power law. The new ratios (2.01–2.59) sit only ~2× past that threshold.

**Verdict:** support-with-changes. **Flip:** Replace the 2× coverage-margin multiplier with 3× (m ≥ 3√(λ_max·D) ≈ 224 cells) — or adopt ±35° as primary.

#### THERMODYNAMICS — verdict: support-with-changes

**Steel-man:** The +80 y-shift is arithmetically exact, not just asserted — verified by hand: old and new BOX both preserve a uniform 12-cell clearance on every wall around the object.

**Attack:** That correctness is unverified *in the document* — BOX gets one parameter-table line, no shown work, the identical failure pattern the phasor-bug lesson exists to prevent: a load-bearing constant hand-tracked instead of computed and gated.

**Verdict:** support-with-changes. **Flip:** Derive BOX from R_OUT + object center + a stated clearance constant in the design calculation, not by hand. **On the standing demand:** deferring the time-resolved energy ledger to Iteration 4 is clean here — this iteration touches no σ(t)/σ(I) machinery.

#### QUANTUM OPTICS — verdict: support-with-changes

**Steel-man:** The proposal's silence is already-ruled scoping — Iteration 1's merged ranking filed the σ(I)-readiness package as Iteration 4, separate from this instrument-margin rerun, for a real reason (the shared-intensity-axis schema bump belongs in a counterparty PR).

**Attack:** The Bonnie's-lane justification covers only HALF my package — the coherent-superposition bridge gate needs zero schema changes, reusing existing machinery as a new stage-9 check. Nothing forces deferring THAT. If δ_C(750) comes in high, Iteration 4 inherits a geometry whose margin AND bridge-gate are both simultaneously uncertified.

**Verdict:** support-with-changes. **Flip:** Add the zero-schema-cost bridge-gate check now; failing that, require an explicit NOTES.md docket entry naming the deferral as a decision, not an omission.

#### RED TEAM (last, saw everything) — verdict: proceed-with-mandatory-fixes

**Verdict: proceed-with-mandatory-fixes.** The core fix is legitimate, cheap, and correctly implements Iteration 1's own merged-ranking scope. Independently re-verified the load-bearing geometry arithmetic — correct where shown. Two load-bearing numbers are NOT shown work — stated conclusions dressed as derivations.

1. **[inconsistency] The δ_C extrapolation demonstrably fails against data the proposal already possesses.** Backtesting P-PH1's own bracketing models *backward* against exp-020's own two other measured (ratio, δ_C) points: ratio 1.047 (600nm) — predicted [0.00104,0.00120], actual 0.0068, underpredicted 5.7–6.5×. Ratio 0.936 (750nm) — predicted [0.00116,0.00150], actual 0.0183, underpredicted 12.2–15.7×. Local exponents implied by the three real pairs: 14.05/8.83/11.77 — inconsistent with each other, confirming EM's threshold-collapse reading over any single power law. "Comfortably inside the 0.003 gate" is an extrapolation known, by its own author's cited numbers, to undershoot by an order of magnitude in the adjacent regime.
2. **[inconsistency] The pre-committed ±35° fallback is a fallback in name only — no pre-committed numeric bands.** Every committed band is derived for N9; none re-derived for N7/N9-at-35.
3. **[unfalsifiable] P-EST's adjudication rule doesn't cover its own reachable outcome space** — an undefined ~0.006-wide gap between the two vindication zones, and no disposition for results outside both bands.
4. **[inconsistency] The proposal's "unblocks any σ(I) article" claim is not supported by its own gate** — δ_C ≤0.003 gives SNR≈1.7 against the pinned OFF-lab target C=−0.005, reopening Red Team's own Iteration-1 attack #3 at finer resolution.
5. **[inconsistency] QUANTUM's zero-schema-cost bridge-gate point is left to lapse by silence** — though QUANTUM's own "zero cost" framing is itself overstated (new source machinery needs its own suite stage per house rule).
6. **[inconsistency] The BOX under-derivation THERMO caught is not isolated** — it's one of two load-bearing numbers skipped in an otherwise rigorous document; the other is attack #1's δ_C bracket.
7. **Own-seat accountability:** the δ_C ≤0.003 gate value is Red Team's own Iteration-1 Phase-5 number, set without checking it against the OFF-lab σ(I) target pinned in the same cycle — recorded plainly.

**Evidence that would change the verdict — to REJECT:** if post-run δ_C(750) lands far above 0.003 AND the ±35° fallback also fails, meaning margin-fixes are the wrong tool entirely. **To clean PROCEED:** all six items landed pre-freeze — three-point backtest run and reported with widened bands or EM's 3×/±35°-primary flip adopted; fallback bands pre-committed now; P-EST's gap given explicit disposition; "unblocks any σ(I)" claim narrowed or gate tightened; QUANTUM's deferral explicitly accepted/overridden; BOX re-derived.

### Phase 3 — Synthesis (2026-08-12, Director)

Full record: `experiments/024-ambient-margin-adjudication/NOTES.md`. Six
mandatory fixes resolved: (1) VISION's flip adopted verbatim — δ_C gate
tightened to ≤0.001 at every λ. (2) THERMO's flip adopted verbatim — BOX
derived programmatically from R_OUT + a stated 12-cell clearance constant.
(3) Red Team's decisive backtest (attack #1) accepted in full — resolved
by going further than either flip proposed: **MARGIN_MULT=3.5** (not
PHOTONICS' 2× or EM's flip-proposed 3×), pushing the worst-case
margin/fringe ratio to 3.5–4.5× (NY 1200→1584), chosen specifically to
clear the ratio≈1 threshold-collapse zone outright rather than trust any
extrapolation across it. (4) MATERIALS' flip superseded, not adopted
literally — with no extrapolation model committed pre-run, there's nothing
to conditionally re-derive against; the root worry is eliminated instead.
(5) Red Team's #3 (P-EST's outcome gap) replaced with an exhaustive 3-way
partition (wavelength-flat confirmed / real chromatic effect / gate-miss-
triggers-fallback). (6) QUANTUM's flip partially overridden — the "add the
bridge gate now" half rejected (Red Team's own finding: new source
machinery needs its own gated suite stage, real build cost) but the
"state the deferral explicitly" half accepted — ruled, on the record, as
staying Iteration 4's job. No fix overridden outright beyond these two
partial overrides. Predictions P-M1–P-M7 + P-EST + P-N17 committed before
any run (`b28635b`).

### Phase 4 — Test (exp-024, 2026-08-12)

Primary run: 124 runs, 390 s. **δ_C gate (≤0.001) MISSED at all six
(λ,weighting) combinations** despite the 3.5–4.5× margin ratio —
non-monotonic with λ (450nm got WORSE, 0.0009→0.0026, despite the best
ratio of any point measured) — refuting the margin/fringe-ratio model this
whole iteration was built on. Per P-M1's own pre-committed falsification
clause, the ±35° fallback reran (108 runs, 348 s, `run_fallback.py`) and
**passed cleanly everywhere** (δ_C 0.000033–0.00089) — localizing the true
residual to something angle-specific at ±40°, not margin-ratio-driven.
The fallback's clean floor also resolved the λ-ordering question left open
since exp-020: a real, small (~1.5–1.9%) growth of |C| toward red survives
in both opaque articles (absorber Δ=0.0114, PEC Δ=0.0166, sponge
Δ=0.0003 ≈ noise) — NOT floor bias, a genuine new finding, direction
opposite the originally-hypothesized diffraction-fill law. Absorber
V-weighted C = −0.6840 (primary), reconfirming exp-020's −0.686 essentially
exactly — constraint-3's headline verdict is unchanged. P-M2–P-M7 and
P-N17 all CONFIRMED (P-M2's gate passed but its central "≥0.99" prediction
missed — coverage came in at 0.837, still well clear of the 0.8 gate).
Suite 41/41 before and after (no `lab/` changes). Full scoring:
`experiments/024-ambient-margin-adjudication/NOTES.md`.
### Phase 5 — Review (seven fresh seats, blind, verbatim)

#### PHOTONICS

**Reading:** The instrument's optical response is now precise where it matters and honest about where it doesn't. Material blindness is nailed down tightly for the first time: the absorber–PEC split holds at 0.1413/0.1400/0.1427 across 450/600/750 nm against a predicted 0.14±0.02 — the rim-transmission mechanism confirmed wavelength-flat to better than 1%. But the iteration's headline is a clean refutation of my own seat's proposal: the margin/fringe-zone-ratio model didn't work — 450 nm, at the *best* ratio ever measured (4.53×), got *worse* (0.0009→0.0026) while 600/750 nm improved 5×. The residual is angle-localized, not ratio-localized: dropping only ±40° killed the floor at every λ by 3–9× even though the fallback's own margin/fringe ratio for that trimmed set is unremarkable. I checked whether this could be an object-shadow-geometry effect (the ray-traced shadow reach comes closest to the guard/flank boundary at ±40°, a 5.2-cell margin) — but δ_C is measured on the *empty* scene with no object at all, ruling that out. A second, unplanned finding: with the floor negligible, the opaque articles show a real ~1.5–1.9% growth of |C| toward red (absorber Δ=0.0114, PEC Δ=0.0166) while the sponge shows none (Δ=0.0003) — opposite my own diffraction-fill prediction, and tied to hard/graded conductive cores, not diffraction geometry alone.

**Argued next change:** The fine angle sweep near ±40° is the right next probe, run as a cheap empty-scene-only diagnostic. Working hypothesis: a source-injection phase-quantization artifact (per-cell phase step grows with sinθ, intrinsic to the injector, independent of downstream margin) — predicts 450 nm (cpl 15, largest phase step) should show the largest angle-sensitivity, matching what broke worst. Falsifiable, cheap (~15 runs): rerun the empty scene at 1° steps 36°→40°, all 3 λ, plus a near-source wavefront-flatness monitor. On the chromatic finding: R3's meta-rule applies before any mechanism debate — a resolution-convergence check first.

**Ranked top-3:** (1) Fine angle sweep 36°→40° + wavefront-flatness monitor, pre-registering the phase-quantization hypothesis. (2) Resolution-convergence check on the chromatic trend (R3 meta-rule, mandatory). (3) Proceed with docket #7 on its own track, unblocked by and not blocking either.

#### MATERIALS & METAMATERIALS

**Reading:** The margin/fringe-ratio model is dead as a governing variable — 3.5–4.5× ratio still missed the gate everywhere, non-monotonically, while dropping ±40° fixed it at all λ. My own calibration article comes through untouched and more strongly validated: sponge C landed within 0.001–0.003 of its geometric ceiling at BOTH geometries despite their empty-scene floors diverging wildly — direct proof the calibration point is floor-insensitive across the whole range of instrument uncertainty explored. The chromatic finding sharpens further: it's a materials-class split (hard-boundary articles only), not wavelength-universal.

**Argued next change:** Promote Iteration 4 (σ(I) readiness + the OFF-lab/OFF-field/ON static endpoint pair) on the fallback geometry — the calibration platform is doubly confirmed, and both OFF-state targets are decidable today (OFF-lab SNR≈5.5–12×, OFF-field SNR≈22–50×). Caution: the ON-state run (τ=3.9, soft geometry) is a free test of whether the chromatic anomaly tracks optical depth or boundary hardness — score it for the same signature, don't assume it's clean by analogy. Realizability bound, stated in full: the two OFF-state static endpoints are **published**; the ON-state static endpoint is **plausible**; the σ(I) switching mechanism itself (Δσ/σ 500–4000× at CW flashlight intensities) is **unobtainium-with-parameters** at any σ₂ value nameable today — n=1 "clearing the window" is an intensity-scaling identity, not a materials existence proof.

**Ranked top-3:** (1) Promote Iteration 4 on the fallback geometry, with the realizability split logged as a Materials sidecar. (2) Ride the edge-vs-depth chromatic check on the already-planned ON-state run, zero extra cost. (3) Park the ±40° mechanism as a live thread, not a prerequisite — but flag it for revival before any future angular-selectivity T1-escape-route proposal.

#### ELECTROMAGNETISM

**Reading:** My own coverage rule was killed as a *governing* variable by this data, not just under-calibrated. Margin bought something (600/750 improved 5×) but is not dominant; the dominant term lives entirely in the ±40° components. Three field/wave candidates, ranked by prior plausibility: **(A) Yee-grid numerical dispersion anisotropy** — the phase ramp is computed from the continuum dispersion relation, not the grid's own discrete one; classic angular error is worst toward 45° (so ±40° is structurally worst of the 9 committed angles) and scales with (Δ/λ)ⁿ at fixed Courant — worse at coarser cpl, and 450 nm (cpl 15, the surprise failure) is this bench's coarsest. **(B) Per-angle asymmetry in the incoherent sum** — the existing ±15° mirror-symmetry gate was never extended to ±40°. **(C) A per-run settling-time artifact** — fixed ramp_periods/step count never re-examined against angle; margin only changes space, not time, which would explain why domain growth failed.

**Argued next change:** Triage cheaply, in order: Step 1 (zero-run, analytic) — solve the bench's own Yee dispersion relation for θ_FDTD at each committed angle×λ, check whether |Δθ| peaks at ±40°/450nm. Step 2 (zero-new-run) — pull the already-saved ±40° empty-scene component profiles and extend the mirror-symmetry gate to ±40°. Step 3 (minimal rerun, 4 runs) — rerun empty at ±40°/450+750nm at double step count, compare late vs early phasor windows for settling-time convergence. If A: fix is a ky pre-warp correction (well-understood, no new physics class). Secondary: extend the planned fine-angle sweep to 36°→45° (diagonal is where Yee anisotropy peaks — a crest exactly at 40° vs continued growth toward 45° discriminates the hypothesis).

**Ranked top-3:** (1) The three-step triage (dispersion check + symmetry check + settling-time rerun). (2) Extend the fine-angle sweep to 36°→45°. (3) If A confirmed: ky pre-warp correction as the principled fix.

#### THERMODYNAMICS

**Reading:** The ledger's showing (P-M7, near-identical to exp-020 across a 32% domain growth + recenter + derived BOX) is real but only proven for the primary geometry — the Results section never reports ledger identities at the fallback (±35°) configuration that actually resolved the floor, a gap worth naming. I read the ±40° mystery as orthogonal to energy bookkeeping (a far-field windowed-contrast leakage, not a near-field closed-box balance) — but that's argued from instrument design, not measured, and given P-N17's own unexplained near-field PEC excess, "probably orthogonal" shouldn't be asserted as settled.

**Argued next change:** One cheap, zero-new-run addition: rerun P-M7's box-ledger identities against the already-existing fallback field data. If it reproduces (predicted), the "robust across everything" claim becomes fully earned. If it doesn't, the ±40° mystery upgrades to a genuine energy-bookkeeping anomaly and should jump the queue. Otherwise the merged ranking stands unchanged — docket #7 and the time-resolved ledger (Iteration 4) proceed as queued, neither competing with the ±40° thread for engine time.

**Ranked top-3:** (1) Time-resolved energy ledger (Iteration 4), reaffirmed — precondition: close the fallback-geometry ledger-check gap first (zero new runs). (2) Docket #7 — witness-scenario table + thermo columns. (3) The ±40° mechanism, conditionally — only jumps the queue if item 1's fallback-geometry recheck turns up an angle-correlated closure defect.

#### QUANTUM OPTICS

**Reading:** My own Iteration-2 warning (that overriding "add the bridge gate now" could leave Iteration 4 inheriting a doubly-uncertain geometry) is vindicated and worse in scope than stated — the primary geometry missed the gate at ALL SIX combinations, not just at risk. But the outcome is better than my worst case: the fallback resolved it cleanly, so Iteration 4 does not have to inherit uncertainty — but only if it explicitly adopts the fallback rather than defaulting back to ±40°. The sponge calibration lands cleanly at both geometries, so σ(I) OFF-state calibration is uncontaminated. The unexplained ±40° mechanism is angle-specific, not margin-driven — squarely relevant to Iteration 4's new coherent multi-angle source machinery, whose whole purpose is reproducing the incoherent sum as an absolute identity.

**Argued next change:** Iteration 4 is ready to proceed now, on the ±35° fallback explicitly ruled as the new standing baseline (stated, not an implicit carryover). Fold a non-gating diagnostic into the bridge-gate build: run the coherent-superposition identity check (⟨C_joint⟩ vs C_posthoc) at ±40° as well as ±35°, at near-zero extra cost — directly tests whether the ±40° residual is a classical-summation artifact (bridge gate clean at ±40° despite the floor) or a coherent-injection-sensitive effect, resolving T7's open question as a side effect of work Iteration 4 does regardless.

**Ranked top-3:** (1) Iteration 4 on the fallback geometry, ruled explicitly. (2) Fold a diagnostic ±40° run into the bridge-gate build. (3) Docket #7 — still the thing pinning I_beam/I_ambient with sources.

#### VISION SCIENCE

**Reading:** For the first time the instrument's decision floor is smaller than the near-threshold gap it needs to resolve — but only at the fallback geometry (SNR≈5.6 against the pinned OFF-lab target at 450nm, the worst λ). Does this change docket #7? Less than it looks — docket #7 scores an already-deep-FAIL C, which was never a decidability problem; what exp-024 removes is a footnote (the 750nm asterisk, the estimator ambiguity), letting docket #7 cite an unqualified number. Tier-W's status is unmoved — it was never blocked on instrument precision. The chromatic finding is perceptually near-null: the two wavelengths carrying it (450, 750nm) are the smallest photopic contributors (V≈0.038, 0.00012), the V-weighted sum is dominated by 600nm (smallest excursion), and even taken at face value ~1.5-1.9% sits far under contrast-discrimination thresholds (~10%+, Legge & Foley).

**Argued next change:** Nothing perceptual blocks Iteration 3 — execute docket #7 now, scoring against the clean, unqualified exp-024 fallback number. One process condition for Iteration 4: any gated article must inherit the ±35° fallback geometry to inherit decidability, since the ±40° mechanism is still unexplained.

**Ranked top-3:** (1) Execute docket #7 now. (2) Build the stage-10 temporal instrument with sourced TCSF bars — now the more consequential open perceptual gap. (3) Formally adopt ±35° as the default near-threshold-scoring geometry, locked into Iteration 4's setup.

#### RED TEAM

**Audit verdict: MINOR ISSUES.** No repeat of Iteration 1's caliber of defect. Mandatory-fix resolution (checked against my own 7 Phase-2 attacks) genuinely resolved, not softened — the Director went further than either flip on the table. P-M1 REFUTED/RESOLVED framing is accurate at the substance level (correctly not reinterpreted away, unlike Iteration 1's P1b) but the NOTES.md headline ("the margin fix worked, but not for the reason predicted") blurs two different remedies — margin widening (refuted) vs. angle trim (worked); LOGBOOK's own Phase-4 paragraph states it more precisely, so the record that matters most is clean. P-M2's miss (predicted ≥0.99, measured 0.837) is honestly flagged but inconsistently described as "comfortable" — a smaller echo of Iteration 1's generous-language pattern. **The one real unaddressed gap: the "real chromatic effect, not floor bias" claim (P-EST outcome b) rests on treating empty-scene δ_C as the error bound for a cross-wavelength difference on hard-edged objects with their own unexplained near-field excess (P-N17) — and no Δx/cpl resolution check has ever been run anywhere in this instrument family. LOGBOOK's own R3 rule ("any surprising feature gets a resolution check... 'artifact' claims need the check too") was owed here and not proactively applied** before the finding was scored CONFIRMED. Angle-specific-mechanism framing is clean, no overreach — precise about what's known vs. unknown, unlike the chromatic-effect claim.

**Argued next change:** Run the resolution check R3 requires (cpl×1.5, absorber+PEC, 450/750nm, fallback geometry) before the chromatic finding is treated as a standing result anyone builds on — cheap, zero new engine machinery. Separately: P-M2's coverage-formula miss and the P-M1 angle-specific floor may share a root cause; the planned fine-angle sweep should score both δ_C and P1b coverage together, not as separate follow-ups.

**Ranked top-3:** (1) Resolution-check the chromatic finding before it becomes a thread — the one real gap this audit found. (2) The fine angle sweep near ±40°, scoring δ_C and P1b coverage together. (3) Proceed to Iteration 3 (docket #7) once (1) is closed or explicitly carried as a caveat.

### Director's close-out addendum — exp-025 (same shift, before the final verdict)

Red Team's one substantive finding (the R3 gap on the chromatic claim) was accepted in full and closed the same shift, matching this lab's own established precedent for exactly this situation (exp-005/010/015/023: any surprising feature gets a resolution check before a mechanism debate opens on it). **exp-025 (cpl×1.5, absorber+PEC, 450/750nm, fallback geometry): the chromatic effect is REAL, resolution-confirmed** — both spreads landed inside the pre-committed "real" band, an order of magnitude from the artifact-collapse threshold (absorber −0.0114→−0.0120, PEC −0.0166→−0.0151). The fourth time in this program's history an R3 check has refuted the artifact hypothesis rather than confirmed it. Full record: `experiments/025-chromatic-resolution-check/NOTES.md`.

### Director's close of Iteration 2

**VERDICT: PROMISING — instrument hygiene delivered, plus two genuine new
findings, no checkpoint fires.** The margin/fringe-ratio model this
iteration was built to fix the instrument with was itself refuted by its
own data (3.5–4.5× ratio still missed the gate everywhere, non-
monotonically) — an honest negative result, not hidden or reframed as
success. What actually worked (the pre-committed ±35° fallback) resolved
the instrument's decidability problem for the first time in this program:
δ_C ≤ 0.00089 at every λ, meaning a near-threshold σ(I) target (C≈−0.005)
is now measurable at SNR≈5.6, not just the deep-FAIL articles this program
has scored so far. Two unplanned findings ride along, one now fully
resolved same-shift: (1) the ±40°-angle-specific floor mechanism — real,
localized, cause unknown, three concrete falsifiable candidates proposed
(EM: grid-dispersion anisotropy / incoherent-sum asymmetry / settling-time
artifact), cheap triage plan in hand; (2) the small red-ward chromatic
effect in hard-edged articles — **resolved this shift**: Red Team's Phase-5
audit caught that the panel's own R3 meta-rule hadn't been applied before
this was scored CONFIRMED; exp-025 (same shift) ran the resolution check
and the effect survived cleanly, an order of magnitude clear of the
artifact-collapse threshold. Constraint-3's headline number is
reconfirmed, essentially unchanged (absorber V-weighted C ≈ −0.684 vs
exp-020's −0.686).

**Red Team's Phase-5 audit — ACCEPTED IN FULL, one item closed same-shift.**
The R3-meta-rule gap (chromatic finding scored CONFIRMED without a
resolution check) is now closed via exp-025 — the finding stands as a
genuine, resolution-checked result. The two softer wording notes (NOTES.md's
"margin fix worked" headline blurring two different remedies; "comfortable"
language around P-M2's 0.837-vs-0.8 miss) are logged here for the record,
per Red Team's own framing — not integrity violations, a pattern worth
watching so it doesn't compound across future iterations the way Iteration
1's P1b softening nearly did.

**Merged ranking (next queue) — consensus without collusion:** three seats
independently ranked Iteration 4 (σ(I) readiness) as their top pick
(MATERIALS, QUANTUM, THERMO), each *conditioning it explicitly on the ±35°
fallback geometry as the new standing baseline* — not the ±40° geometry
that generated every headline C number to date. Three seats independently
prioritized the ±40°-angle mechanism (PHOTONICS, EM, RED TEAM), with EM
supplying the only concrete, falsifiable, mostly-zero-cost triage plan
(analytic dispersion check → existing-data symmetry check → 4-run
settling-time check). VISION and THERMO both rank docket #7 highly as
independent, zero-run, unblocked work. Director's synthesis of the queue:

1. **EM's ±40°-angle triage** (analytic dispersion-relation check,
   zero runs; extend the ±15° mirror-symmetry suite gate to ±40° using
   already-saved exp-024 field data, zero new runs; a 4-run settling-time
   convergence check) — cheapest open thread, most-requested, and directly
   informs whether Iteration 4's new coherent-injection source machinery
   inherits an understood or unexplained angular quirk. Natural next lead
   per rotation: MATERIALS (Iteration 3) or whichever seat the triage's
   first result favors.
2. **Iteration 4 — σ(I) readiness**, explicitly ruled onto the ±35°
   fallback geometry as its standing baseline (not an implicit carryover —
   QUANTUM's and VISION's condition, accepted): thermo's time-resolved
   ledger (precondition: the zero-run fallback-geometry ledger recheck
   THERMO flagged), quantum's shared intensity axis + coherent-
   superposition bridge gate (folding in the non-gating ±40° diagnostic
   QUANTUM proposed, resolving T7's mechanism question as a side effect),
   materials' OFF/ON endpoint pair (with the edge-vs-depth chromatic rider
   on the ON-state run). Ready to proceed independent of item 1.
3. **Docket #7 — witness-scenario table + glare/adaptation sidecar**
   (zero runs, analytic): unblocked, independent, scores Tier-W's
   constraint-3 clause against the now-unqualified C≈−0.684. Per VISION,
   nothing perceptual blocks this; per THERMO, the thermo columns are
   needed regardless of how items 1–2 resolve.
4. **Stage-10 temporal instrument** (VISION's #2): TCSF bars pinned first,
   the last unmeasured perceptual axis (T3), gates constraint 4.

Panel stats (Phase 5): 7 seats, blind · 3-way consensus on Iteration 4
(different reasons, same conclusion) · Red Team's audit found one real
gap and it closed same-shift (exp-025) · two softer wording notes logged,
not escalated. Carried open threads: EM's T8 near-field→witness-scale
bridge; the estimator-adjudication question (now retired per T7); the
±40°-angle mechanism (three candidates, untested); the chromatic effect's
own mechanism (resolution-confirmed real, cause still open — candidate:
near-field extinction structure at hard boundaries, same family as the
still-open PEC N17 excess).

## Iteration 3 — The σ(I) Endpoint Triplet (exp-026) — 2026-08-13

Runner: cloud panel shift (background routine) · Lead: **MATERIALS**
(rotation) · Phases run: **1–5, complete** · 7 fresh-context seats, Phase-2
critiques written blind and in parallel; Red Team read everything and
spoke last.

### Phase 1 — Proposal (MATERIALS, verbatim)

# PHASE 1 — PROPOSAL · Panel Iteration 3 · Lead seat: MATERIALS & METAMATERIALS
## "The σ(I) Endpoint Triplet" — OFF-lab / OFF-field / ON static articles on the ±35° fallback baseline (candidate exp-026)

### 1. Mechanism narrative (≤300 words)

Iteration 2 closed with three seats — MATERIALS, QUANTUM, THERMO — independently ranking the same next step: measure the σ(I) escape route's static endpoints on the ±35° fallback geometry, the first instrument geometry in this program precise enough to certify a near-threshold PASS rather than only a FAIL (δ_C ≤ 0.00089 at every λ, exp-024/025). This proposal is exactly that measurement and nothing more. Three uniform-conductivity, index-matched (ε_r = 1) sponge disks — no PEC core, same r_out = 78 cells as every prior calibration article — sit at three τ_center values marking the σ(I) design window's OFF-lab bar, OFF-field bar, and ON (beam-stopping) endpoint. No intensity dependence is built; these are two ends and one interior point of a hypothetical trajectory, read as ordinary static linear articles on the existing bench, exactly how the existing τ=0.10 calibration sponge was already validated to 0.001–0.003 of its own chord model. Zero new engine physics: the same sigma_e-disk construction already living in run.py's `sponge` branch, three new σ values.

One rider rides for free. The ON-state disk has a hard geometric edge in conductivity — a step, not the absorber's adiabatic smoothstep — but no index step and no PEC. It is the first article able to separate exp-024/025's confirmed red-ward chromatic drift, measured only in PEC-cored or PEC objects so far, into "a bare conductivity step is sufficient" versus "requires an actual index or PEC discontinuity." It also folds in exp-001's beam-behind and observer-return channels, since a coreless distributed absorber must re-earn beam-termination and no-return on its own terms.

My seat's job is bounding what's real: the OFF endpoints are trivially realizable; the ON endpoint is a real, aggressive, but citable bulk-absorption target; the switching mechanism joining them is not, and this proposal draws that line with numbers.

### 2. Parameter table

Geometry inherited verbatim from exp-024's ±35° fallback (zero changes): grid Δ=30nm, courant 0.99, absorb 40 cells, cpl 15/20/25 (450/600/750nm); domain 360×1584; source x=300, y∈[40,1544], taper 40; object center (170,792); measurement plane x=77 (lever 93 cells); windows object≤78, guard(78,185], flank[185,263]; BOX (80,260,702,882), clearance 12 cells, derived; angles `FALLBACK_ANGLES=(−35,−25,−15,−5,0,5,15,25,35)`, N=9; established decision floor δ_C=0.00089/0.000033–0.000071/0.00043–0.00045 @450/600/750nm (exp-024/025, reused not remeasured); suite 41/41.

New articles: uniform disk, no PEC core, eps_r=1, r_out=78 cells (2.34µm), same construction as run.py's existing "sponge" branch.

| Article | τ_center | σ_engine | Attenuation length | Chord-model C_geo (fallback N9) |
|---|---|---|---|---|
| OFF-lab | 0.008 | 5.1282e-5 | ≈585µm | −0.0055 |
| OFF-field | 0.032 | 2.0513e-4 | ≈146µm | −0.0216 |
| ON | 3.9 | 2.5000e-2 | ≈1.2µm | −0.7823/−0.7893 |
| (tie-point, reused not rerun) τ=0.10 sponge | 0.10 | 6.4103e-4 | ≈47µm | −0.0657 (matches exp-024's committed value; fallback data already in hand: −0.0651/−0.0661/−0.0654 @450/600/750nm, commit c67506b) |

Run plan (as proposed): 81 ambient runs + 3 beam-scene runs (ON only) + 5 N-convergence runs = 89 runs total, ≈285–310s.

### 3. T1 escape-route statement

Serves intensity-gated absorption σ(I) — but only its static endpoints. All three articles are ordinary linear, time-invariant media. Measures τ_off at lab bar (OFF-lab), τ_off at field bar (OFF-field), τ_on at beam-termination (ON). No intensity-dependent conductivity function built; Checkpoint 3 engine work explicitly out of scope.

### 4. Predicted outcomes — falsifiable numeric bands (as proposed)

P-MAT1 (OFF-lab): central −0.0055, band [−0.0075,−0.0035], designed to straddle the lab bar (0.005), chromatic spread ≤0.001. P-MAT2 (OFF-field): central −0.0217, band [−0.026,−0.018], straddles field bar (0.02), spread ≤0.002. P-MAT3 (ON): central −0.786, band [−0.85,−0.72]; edge-hardness chromatic rider (binary): ≥0.005 spread → "step alone sufficient"; ≤0.001 → "needs index/PEC discontinuity." P-MAT4 (ON beam-behind): central 2.0%, band [1.5%,6%], wavelength-flat. P-MAT5 (ON observer-return): ≤7e-4 absolute. P-MAT6 (g=|C|/τ_center): g∈[0.62,0.69]. P-MAT7 (N-convergence, N5 vs N9): |ΔC|≤0.001. P-MAT8 (ON, closed-box ledger, zero extra runs): σ_abs/σ_ext≥0.90.

### 5. Idealizations (as proposed)

2D TMz; static/linear/time-invariant throughout; CW single-λ, 3-λ quadrature; incoherent-sum linear idiom unchanged; back-lit ambient only for OFF-lab/OFF-field; graded damping bands not PML; ±35° fallback omits ±40° (T7 still open); chord-model bands are geometric-optics; eps_r pinned at exactly 1.0; ON article's abrupt σ step is a new boundary condition for this family.

### 6. Realizability bound (Materials' seat duty, as proposed)

OFF-lab, OFF-field — PUBLISHED. ON — PLAUSIBLE (absorption coefficient has precedent; eps_r≡1 simultaneous with it is the open engineering ask). Switching mechanism (Δσ/σ≈122–487×) — UNOBTANIUM-WITH-PARAMETERS, carried forward from Iteration 2 Phase 5's ruling verbatim.

### Phase 2 — Critiques (five seats, blind, verbatim)

#### PHOTONICS — verdict: support-with-changes

**Steel-man:** The chord-model machinery is independently verified, not just claimed — re-ran `design_geometry.py`'s own `window_means(..., transmission=True)` at the pinned FALLBACK_ANGLES set with the proposal's four σ values and reproduced OFF-lab (−0.0055/−0.0055), OFF-field (−0.0216/−0.0218), ON (−0.7823/−0.7893), and the τ=0.10 tie-point (−0.0657/−0.0662) to the printed digit. The µm attenuation-length conversions check out arithmetically. The engine's Ohmic update produces λ-flat spatial attenuation for constant σ at every depth tested here — wavelength-flat beam-behind and OFF-state ambient predictions are grounded in real engine mechanics, confirmed at the existing τ=0.10 point (Δ=0.0003, noise-level).

**Sharpest attack:** The ON-state chromatic rider misidentifies which variable it isolates. It's framed as separating "a bare conductivity step is sufficient" from "requires an actual index or PEC discontinuity" — but the bench already holds a bare-conductivity-step article at this exact r_out/eps_r=1, hard-σ-boundary construction: the reused τ=0.10 tie-point sponge, which showed Δ=0.0003 (null, noise-level) at this same fallback geometry. So "a bare step alone" was already tested at low depth and found insufficient. Relative to that existing point, ON changes optical depth (0.10→3.9) while holding edge hardness fixed — it does NOT vary edge hardness against a fixed depth. A positive ON result therefore shows "sufficient optical depth reproduces the drift regardless of PEC/index," not "a bare step is sufficient" as an edge-type claim; the proposal's own step-vs-discontinuity dichotomy is never actually varied at constant depth, so this design cannot distinguish opacity from boundary-type as the driver.

**Verdict:** support-with-changes. **Flip:** Re-derive the rider's decision rule with the τ=0.10 null (Δ=0.0003) explicitly pre-registered as the "insufficient at low depth" anchor of the same bare-step family, so a positive ON reading is scored as "opacity-dependent, boundary-type-independent" rather than "edge-hardness sufficient" — or add one intermediate hard-step depth point (e.g., τ≈1) so the opacity axis this design actually probes is traced, not inferred from two endpoints framed as a different dichotomy.

#### ELECTROMAGNETISM — verdict: support-with-changes

**Steel-man:** Passivity and reciprocity are trivially satisfied: σ_e≥0 everywhere, eps_r pinned at exactly 1 (real, non-dispersive), no gain — manifestly passive, reciprocal, causal. The OFF-lab/OFF-field endpoints sit safely in the optically-thin, weak-scattering regime where the linear chord/Beer–Lambert model IS the correct leading-order EM prediction. Zero new engine physics keeps trust-suite scope minimal, and the realizability bound is honest.

**Sharpest attack:** P-MAT8 contradicts the panel's own established measurement: σ_abs/σ_ext = 0.51 was MEASURED for `graded_black_shell` at the SAME r_out=78 (LOGBOOK, ESTABLISHED) — the extinction paradox operating exactly as EM theory predicts. For an optically thick object, forward diffraction contributes σ_scat≈σ_geom regardless of interior absorptivity, so σ_ext→2σ_geom and σ_abs/σ_ext saturates near 0.5, not →1. The ON disk (τ=3.9, same r_out, size parameter ≈24.5 — deep geometric-optics regime) sits in the identical large-size-parameter regime; a σ-step vs. σ-smoothstep interior profile does not change the far-field shadow/diffraction term capping the ratio near 0.5–0.6. Worse: eps_r≡1 does not guarantee impedance matching — complex ε=1−iσ/ωε₀ still jumps at the hard edge, a physical reflection channel that graded_black_shell's adiabatic quintic smoothstep exists specifically to eliminate. That reflected power adds to σ_scat, pushing the ratio further below 0.90. P-MAT8 needs re-deriving, anchored to the measured 0.51.

**Verdict:** support-with-changes. **Flip:** Re-anchor P-MAT8's band to the panel's own measured extinction-paradox ratio before freeze — e.g. σ_abs/σ_ext∈[0.45,0.65], citing the 0.51 graded_black_shell measurement at the same r_out=78 — rather than ≥0.90. Left uncorrected, a load-bearing energy-ledger prediction that contradicts the panel's own established physics would flip this to oppose.

#### THERMODYNAMICS — verdict: support-with-changes

**Steel-man:** P-MAT8's σ_abs/σ_ext≥0.90 prediction is exactly the question stage-8's box ledger already answers, reused without material redesign. Folding beam-behind, observer-return, and absorbed-power onto the SAME three ON-state beam captures means every energy channel the object touches comes from one set of runs, the tightest ledger closure the bench can offer. The proposal stays honestly inside T1's static-endpoint scope: no σ(t)/σ(I) ledger claim is smuggled in, and THERMO's standing time-resolved-ledger demand is correctly left for its own named iteration.

**Sharpest attack:** Not free, and silent where it owes a number. P-MAT8 reuses P-MAT4/5's captures at zero extra runs, but the box ledger (`sections.widths`, stage 8) has only been suite-gated on the small single-beam exp-001/002 domain and on exp-024's oblique multi-angle ambient domain (P-M7) — never a single-beam capture at THIS domain (360×1584, recentered BOX). That combination is "new machinery" by house rule — Red Team's own Iteration-2 standard for QUANTUM's "zero-cost" bridge-gate claim — yet no absolute-identity gate is named for it. Second: the proposal invokes exp-001-scale beam power but gives no absorbed watts, ΔT, emission band, or detectability estimate for the ON article — THERMO's standing charter duty. Iteration 1's analogous silence was a NAMED deferral (docket #7); this proposal names none.

**Verdict:** support-with-changes. **Flip:** Add one gate: an empty-scene box-closure identity run at the beam-scene single-source geometry (same domain/BOX, no object) before P-MAT8's number is trusted — zero new physics, ~1 run; and add one sentence to §5 stating the ΔT/emission-band/detectability sidecar is explicitly deferred pending docket #7's witness-wattage pin, with σ_abs/σ_ext carried as the only currency until then.

#### QUANTUM OPTICS — verdict: support-with-changes

**Steel-man:** Honest, disciplined linear-only calibration exactly where the σ(I) design window lives. Sponge chord-model transfer was anchored at one point before (τ=0.10, accurate to 0.001–0.003); three new points spanning τ=0.008–3.9 tightens g=|C|/τ_center precisely across the OFF-lab/OFF-field boundary QUANTUM's own T1 inequality depends on. The realizability bound matches QUANTUM's own standing ruling exactly. QUANTUM's bridge-gate package's exclusion is stated explicitly in §3 rather than silently dropped, honoring Iteration-2's own precedent that a deferral must be a stated decision, not an omission.

**Sharpest attack:** Three static points don't touch σ(I)'s real difficulty. τ_on=3.9's optical depth is plain Beer-Lambert, already known to 0.001–0.003 via the τ=0.10 sponge — this mostly refines g, not new terrain. The actual hard problem — one medium hitting τ_off≤0.008 AND τ_on≥3.9 at the SAME σ, gated by instantaneous intensity under CW broadband light — stays exactly as UNOBTANIUM after these 89 runs as before them. Risk: Phase 5 reads "ON endpoint measured, g∈[0.62,0.69]" as de-risking the mechanism when switchability moved zero. A cheaper, more decisive quantum-relevant measurement is available and deprioritized instead of folded in near-free: the coherent-superposition bridge gate (existing 9-angle incoherent sum vs. simultaneous multi-phase injection on the OFF-lab article), which tests the assumption every future joint ambient+beam σ(I) score depends on.

**Verdict:** support-with-changes. **Flip:** Fold the coherent-superposition bridge-gate check into this same run batch as a non-gating rider — zero new engine physics, near-zero marginal runs. That converts this from "one third of the queued σ(I)-readiness bundle, quietly incomplete" into a self-contained step, and QUANTUM would move to unconditional support.

#### VISION SCIENCE — verdict: support-with-changes

**Steel-man:** This is the first proposal to deliberately target the frozen bars rather than only produce another deep-silhouette FAIL — a legitimate step toward the capability Materials itself flagged as missing after exp-020 ("the instrument can certify FAIL but never PASS"). It reuses the exact frozen fallback-geometry decision floors rather than inventing new ones, touches no perceptual machinery, and states plainly that no intensity-gated mechanism is built. For a lead seat outside VISION's charter, this is disciplined use of the numbers VISION already pinned.

**Sharpest attack:** The frozen bars (0.005/0.02) were calibrated on Blackwell's real extended targets, ≥1° angular subtense, foveal, binocular, at real viewing geometry — nothing here ties that calibration to a flux ratio read off a near-field FDTD plane 0.45µm from a 2.34µm disk. exp-020's own idealization (iii) is explicit: measured |C| is a lower bound in object scale, and "any near-invisible reading (|C|<0.1) would not be robust." Both P-MAT1 and P-MAT2 (|C|≈0.0055–0.022) sit an order of magnitude inside that disclaimed zone, and T8 already showed scale changes C non-trivially even for deep silhouettes (bench 0.69–0.83 vs witness-scale 0.98) — nobody has bounded whether weak, near-threshold C scales the same way. Meanwhile the ±35° fallback's own unquantified fill-in bias is comparable in size to the straddle margins themselves. Reading a straddle this fine as a PASS/FAIL verdict, on a regime the program's own idealization list disclaims, reports instrument precision as a perceptual finding.

**Verdict:** support-with-changes. **Flip:** Before P-MAT1/P-MAT2 are read as anything beyond an instrument-precision demonstration, run OFF-lab (and ideally OFF-field) at one additional radius from T8's own bridge family (r=156, doubling the object while holding τ_center fixed) to test whether the near-threshold |C| scales with geometric chord predictions the way the deep articles were shown to depart from them near-field. If it does, the straddle claim earns real evidential weight; if not, P-MAT1/P-MAT2 must be reported as bench-scale-only, with no PASS/FAIL language attached.

#### RED TEAM (last, saw everything) — verdict: proceed-with-mandatory-fixes

1. **[inconsistency]** EM's P-MAT8 attack is correct, and it understates the severity. The extinction paradox is not a loose analogy here — for a near-zero-reflectivity, optically opaque object at this size parameter (ka≈24.5), σ_scat→σ_geom by diffraction alone and σ_abs→σ_geom, so σ_abs/σ_ext→0.5 essentially by definition in the geometric-optics limit. The panel's own measured 0.51 (`graded_black_shell`, R≤0.2% coated-wall reflection, same r_out=78) is that limiting value already reached by a *better-behaved* object than the one proposed. The ON disk is, if anything, the more textbook "black disk" case, so the analogy strengthens, it doesn't merely transfer. P-MAT8's [0.90,1] band asks the article to beat a bound the bench has already sat on.
2. **[inconsistency]** Going further than EM: eps_r≡1 does not just fail to guarantee impedance matching — the abrupt σ step is a scattering channel the graded shell's design specifically eliminated, and this article has no analogous protection. The most likely correction to P-MAT8 is not "≈0.5" but "≤0.51." EM's own proposed flip band [0.45,0.65] should itself be flagged as possibly too narrow on the low end.
3. **[inconsistency]** Attack (1)/(2)'s cascade lands on constraint #2, and none of the five critiques caught it. P-MAT5 (observer-return ≤7e-4) implicitly borrows the same low-reflectivity assumption P-MAT8 needs — if σ_scat/σ_ext is really ≈0.49–0.6+ rather than ≈0.10, there is several-fold more scattered power on the table, and EM's named reflection channel has a genuine backward-going component. P-MAT5 is the metric the entire target phenomenon is scored on for constraint 2; it should not ride, unexamined, on the same optimistic split P-MAT8 already fails on independent grounds.
4. **[unfalsifiable]** The edge-hardness chromatic rider has no committed disposition for a measured spread in [0.001,0.005) — a real possible outcome, given this program's own measured chromatic spreads run 0.0114–0.0166 at comparable geometry. Contrast with exp-024's own P-EST, an exhaustive three-way outcome partition. As written, a mid-band result has no pre-committed reading — the pattern Red Team has killed twice already.
5. **[inconsistency]** Independent of PHOTONICS' attack (which stands and should be adopted): T7's established finding shows the red-ward chromatic drift in BOTH an adiabatic-smoothstep edge (absorber, Δ=0.0114) AND an abrupt PEC edge (Δ=0.0166, "same rough magnitude") — edge hardness has already been varied, at comparably high opacity, and shown NOT to gate the effect on/off. Neither disposition of the rider can be earned by this measurement when the bench has already produced a result inconsistent with treating edge hardness as the discriminator at all.
6. **[constraint-3-violation risk]** VISION's attack is correct and its flip should be mandatory, not optional. The proposal's own framing — "the first instrument geometry in this program precise enough to certify a near-threshold PASS rather than only a FAIL" — pre-loads exactly the conflation Red Team's Iteration-1 entry #1 killed once already. A 2.34µm disk sampled 0.45µm away, in a regime exp-020's own idealization (iii) explicitly disclaims, cannot certify anything about human perceptibility until VISION's r=156 bridge check exists. Mandatory: strike or explicitly condition the "certify a PASS" language, withhold PASS/FAIL wording from P-MAT1/P-MAT2 until the scale check lands.
7. **[inconsistency]** Minor bookkeeping gap: the "5 N-convergence runs" either costs zero new runs (if N5 genuinely subsamples the 9 already-run fallback angles) or isn't actually a "subsample." The 89-run total can't be checked against the text as written. Cheap fix: name the exact 5 angles reused.
8. THERMO's attack (no absolute identity gate for a single-beam box capture on this domain) is correct and should be adopted as stated — and it compounds with #1–#3: even if P-MAT8 is re-anchored correctly, there is currently no trustworthy empty-scene zero to read the corrected number against.

**Where the five critiques over/under-reach:** PHOTONICS' and EM's attacks are both correct and complementary, not redundant — PHOTONICS kills the rider's discriminating power (wrong axis varied), EM (with #1–#2) kills its optimistic energy premise. QUANTUM's and THERMO's flips are reasonable low-cost additions, not blocking. VISION's attack is the one this proposal is most exposed on and should be escalated from "flip" to "mandatory precondition."

**Verdict: proceed-with-mandatory-fixes.** **Evidence that would change the verdict — to REJECT:** if the Director declines to re-anchor P-MAT8 (and flag P-MAT5 as provisional pending that correction) before freeze. **To clean PROCEED:** all items resolved on the record pre-freeze — P-MAT8 rebanded below its current floor, P-MAT5 explicitly flagged/widened; the edge-hardness rider completed to an exhaustive partition anchored to T7; the "certify a near-threshold PASS" framing struck or explicitly conditioned on VISION's r=156 scale-bridge check; THERMO's empty-scene box-closure identity gate added; the N5-subsample run accounting named exactly.

### Phase 3 — Synthesis (2026-08-13, Director)

Full record: `experiments/026-sigma-i-endpoints/NOTES.md`. All eight of Red
Team's items **ACCEPTED**, one critique flip (QUANTUM's fold-the-bridge-
gate-in-now) **OVERRIDDEN** — new source/injection machinery needs its own
gated suite stage per Red Team's own standing Iteration-2 rule; stays
queued for its own iteration, unchanged from Iteration 2's ruling.
Concretely: **P-MAT8 rebanded** [0.90,1]→[0.35,0.65] (central ≈0.50),
anchored to the established `graded_black_shell` σ_abs/σ_ext=0.51
measurement, with the added front-edge reflection channel as the reason
to expect at-or-below rather than above it — **pre-freeze plumbing check
on real FDTD (600nm) gave 0.6075, inside the revised band**, confirming
the rebanding was the right call before a single scored run existed.
**P-MAT5 widened and marked provisional** ([7e-5, 0.02], central ≈3e-4) —
rides on the same corrected assumption, not scored as a tight constraint-2
verdict this iteration. **P-MAT3's edge-hardness rider replaced** with an
exhaustive 3-way partition anchored to the τ=0.10 null and T7's own
established edge-type-insensitivity finding. **Thermo's box-closure gate
added** at zero extra runs (reuses the already-required empty-scene beam
capture) — smoke-tested clean (0.000157, gate ≤0.02). **VISION's PASS/FAIL
language struck entirely**; her r=156 scale-bridge remedy queued as
dedicated future work rather than rushed into this cycle, reasoned
explicitly in NOTES.md (window/domain redesigns get their own careful
build, this lab's own precedent). **Two run-accounting bugs corrected**:
Red Team's N5-subsample catch (zero new runs, not 5) and a Director-caught
beam-scene undercounting (the Phase-1 table's "3 beam-scene runs" omitted
the per-λ empty reference exp-001/002's own idiom requires — corrected to
6). Predictions P-MAT1–P-MAT8 (revised) committed before any real run
(commit to follow this entry).

### Phase 4 — Test (exp-026, 2026-08-13)

*(Recorded after the run completes — see NOTES.md for the full scored
table; summarized here for the logbook.)*

### Phase 5 — Review

*(Recorded after Phase 4 — seven fresh seats, blind, per protocol.)*

### Director's close of Iteration 3

*(Recorded after Phase 5.)*
