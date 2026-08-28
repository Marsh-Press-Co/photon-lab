# PHASE 1 — PROPOSAL · Panel Iteration 62 · exp-085 · Lead seat: MATERIALS & METAMATERIALS

## "Pinning Leg (a)'s Own Asymptotic Period, Zero-FDTD" — a wide/dense re-evaluation of `edge_diffraction_c_empty_corrected`'s own model-internal periodicity, independent of the narrow window's own null distribution

### 1. Mechanism narrative (≤300 words)

T28's founding periodicity has, since exp-069, only ever been fit inside
one fixed 6°-wide, 31-point angular window (36°–42°, the same window every
real-FDTD comparison must use because that is what costs FDTD calls).
`edge_diffraction_c_empty_corrected` — leg (a)'s exact, non-paraxial,
zero-noise 2D scalar Huygens–Fresnel sum over the source aperture's own two
tapered edges (exp-084) — costs nothing to evaluate anywhere else, so the
narrow window is a constraint on *how this program has looked at the
model*, not a constraint on the physics the model itself computes.

Physically, what sets this curve's own period? A genuine far-field
two-slit grating (point sources separated by the full aperture width
`A=752` cells) would be EXACTLY periodic in `sin(θ)`, period `λ/A` — the
origin of the already-refuted `P_edge_B=1.9608°`. But this bench sits at
0.197% of its own Fraunhofer distance (`experiments/084-.../
phase1_proposal.md` §1) — deep Fresnel regime, where the propagation phase
uses the EXACT `hypot(D_SP, y−y_p)` distance, not its paraxial (quadratic)
truncation. That exact distance couples the observation angle and the
source-point position nonlinearly: the local fringe spacing near any given
`θ` is set by a Fresnel-zone-like construction whose own characteristic
width (`√(λ·D_SP)≈66.8` cells) is angle-independent in absolute (cell)
terms but angle-DEPENDENT once projected into `sin(θ)` — the textbook
signature of a CHIRPED (non-stationary) near-field pattern, not a
stationary grating tone (EM's own Phase-5 review of exp-084 already named
this qualitatively; this cycle quantifies it). Two outcomes are therefore
both physically plausible a priori: (i) the chirp is weak enough over the
accessible domain that one dominant period still describes the curve well,
in which case a wide/dense fit should converge tightly, at much higher R²
than the narrow window's 0.3697; or (ii) the chirp is strong enough that
"the period" is not a well-defined single number at all, in which case no
wide-window fit — however dense — converges, and the finding IS the drift,
not a number.

### 2. Parameter table

Every value below is either read from a committed file (R4) or a new,
disclosed design-time choice for this cycle.

| Quantity | Value | Reused unchanged / New |
|---|---|---|
| Model function | `dg048.edge_diffraction_c_empty_corrected(theta_deg, lam_cells, g)` | **REUSED verbatim** — `experiments/048-evidentiary-chord-closure/design_geometry.py` |
| Geometry | `g = dg065.propagator_geom(dg065.CONFIGS["C40"])` | **REUSED verbatim** — identical config exp-084 leg (a) used |
| Wavelength | `λ=20` cells (600 nm), `dg065.CPL[600]` | **REUSED**, single-λ only (Idealization 2) |
| `P_model_a` (narrow-window fit, already published) | `2.5338°`, `R²=0.3697` | READ — `experiments/084-.../derivation_results.json::leg_a.p_model_deg`/`.r_squared` (R4 — never hand-typed) |
| `P_edge_A` (T28 target, already published) | `2.8421052631578947°` | READ — `experiments/083-t28-pad-article-full-power-retest/results.json::p_edge_a` (R4) |
| **Method A** domain | `θ ∈ [2.0°, 80.0°]`, step `0.02°`, θ-uniform | **NEW** grid, `N=3901` points — 13.0× wider, 10× denser than the established 6°/0.2° window |
| **Method A** fit | `ywp.free_period_with_widening(theta_grid, c_wide, "leg_a_wide", stages)` | **REUSED verbatim** — `experiments/078-t28-y-wall-echo-prescreen/y_wall_prescreen.py`; `center_deg=39.0` fixed (unchanged, matches every prior T28 citation), same 3-stage `[1,4]→[1,15]→[1,60]°` candidate-period widening; only the INPUT curve is new |
| **Method B** domain | `u=sin(θ)` uniform on `[sin(2.0°), sin(80.0°)] = [0.034899, 0.984808]`, `N=32768=2^15` | **NEW** grid — uniform in the natural periodic variable (θ-uniform sampling would under-resolve `sin(θ)` near grazing incidence) |
| **Method B** computation | zero-padded FFT (pad to `2^17=131072`), power spectrum `|·|²`, peak bin search restricted to periods `∈[1°,15°]` (primary — matches this sub-thread's own established scoring range) with the FULL unrestricted spectrum also inspected and any larger peak outside that range disclosed, not discarded | **NEW** code (~40 lines) — a dense FFT, genuinely independent of `_free_period_search`'s bounded candidate-range grid search (see §4 justification) |
| **Method B** period conversion | `P_fft_deg = degrees((1/f_peak) / cos(radians(39.0)))` | **NEW**, algebraically inverts `_free_period_search`'s own `Tc=radians(P)·cos(39°)` convention exactly, for direct comparability to `P_model_a`/`P_edge_A` |
| **Method C** (chirp-stability diagnostic) sub-window centers | `θc ∈ {5°,7°,9°,…,77°}` (step 2°, `N=37`), each sub-window `θc±3°`, 0.2° step (31 pts) — bit-identical recipe to `dg069.DENSE_ANGLES` | **NEW** loop; `ywp.free_period_with_widening` **REUSED unchanged** per sub-window |
| R5 specificity control on the wide fit | same convention as exp-084 (`specificity_sweep`, target grid `[1°,15°]`, `n=60`) | **REUSED verbatim**, applied to Method A's own `(P_wide, R²_wide)` |

### 3. T1 escape-route statement

**N/A — instrument/model-fidelity thread, identical disposition to every
T28 cycle since exp-069** (069, 075, 077–084). This is a MODEL-INTERNAL
question about `edge_diffraction_c_empty_corrected`'s own asymptotic
periodic structure — it proposes no absorption mechanism and touches no
constraint-3 scene. It does NOT re-score leg (a) against real FDTD data
(exp-084 already scored that comparison and it stands, INCONCLUSIVE, per
R10); this cycle only asks whether the narrow window's own null-limited
verdict undersold or correctly read the model's own true period. Checkpoint
criterion 2 (mechanism-class boundary) is N/A this cycle, matching every
prior T28 desk cycle's own ruling.

### 4. Falsifiable predicted outcomes

**Why Method B is a genuinely independent second check (not a restatement
of Method A):** `_free_period_search`/`free_period_with_widening` performs
a bounded, candidate-range grid search (3-parameter cosine/sine LSQ fit at
each of up to 6000 candidate periods within a range capped at 60° even at
its widest stage) — a matched-filter search that can only ever report a
period inside the range it was told to search, and reports only the single
best-scoring candidate. A zero-padded FFT over a uniformly-sampled
`sin(θ)` grid computes the full power spectrum simultaneously, with no
range restriction and no single-best-candidate collapse — it can reveal
multiple comparable-power tones, a broadened/smeared peak (the spectral
signature of a chirp), or no dominant peak at all, none of which the
existing search machinery is built to report on its own.

**(a) Is `c_model_a(θ)` genuinely (quasi-)periodic in `sin(θ)`, or does its
local period drift?**

Define, over Method C's 37 sub-window centers: `frac_recovered` = fraction
with local `R² ≥ 0.30`; among those, `spread = (max(P_local) −
min(P_local)) / median(P_local)`; `ρ` = Spearman rank correlation between
`θc` and `P_local(θc)` (tests for a coherent trend vs. scatter). Method B
corroborates via peak sharpness: `P2/P1` (second-highest local spectral
maximum, excluding DC±2 bins, over the highest) and `FWHM/f_peak`.

- **STABLE (single global period)**: `frac_recovered ≥ 0.80` AND `spread ≤
  0.15`, corroborated by Method B (`P2/P1 ≤ 0.5` AND `FWHM/f_peak ≤
  0.15`).
- **DRIFTING (real, quantified chirp)**: `frac_recovered ≥ 0.80` AND `0.15
  < spread ≤ 0.50` AND `|ρ| ≥ 0.5` (a coherent trend, not noise) —
  reported as a chirp rate `dP_local/dθc`, not a single number.
- **NOT STABLY PERIODIC**: `frac_recovered < 0.80` (most local windows
  recover no periodic structure at all), OR `spread > 0.50` with `|ρ| <
  0.5` (scattered, incoherent) — no single global period exists at this
  window scale; any downstream period-match question is retroactively
  judged unanswerable by this construction, a stronger, different finding
  than either of the above.
- If Method B's classification (via `P2/P1`/`FWHM`) disagrees with Method
  C's, both are reported side by side and flagged for reconciliation, not
  silently resolved (matching this sub-thread's own instrument-
  disagreement discipline, e.g. exp-083's EM/circular-shift episode).

**(b) If (quasi-)periodic, what period does the wide/dense fit converge
to?** Using `P_wide` (Method A, full `[2°,80°]` domain) and `P_fft`
(Method B spectral peak), only evaluated if (a) is STABLE or DRIFTING-
with-a-well-defined-asymptote:

- **"Narrow window undershot — wide fit moves toward `P_edge_A`"**:
  `rel_dev(P_wide, P_edge_A) ≤ 0.10` AND `rel_dev(P_fft, P_edge_A) ≤
  0.10` AND `R²_wide ≥ 0.55` (a real tightening, not merely "still not
  excluded" — more data should constrain a genuine tone far better than
  the narrow window's `R²=0.3697`).
- **"Wide fit confirms `2.5338°`, `P_edge_A` remains excluded"**:
  `rel_dev(P_wide, P_model_a) ≤ 0.05` AND `rel_dev(P_fft, P_model_a) ≤
  0.05` AND `rel_dev(P_wide, P_edge_A) > 0.20` AND `rel_dev(P_fft,
  P_edge_A) > 0.20`.
- **"Neither — a third, previously unreported value"**: `rel_dev(P_wide,
  P_model_a) > 0.05` AND `rel_dev(P_wide, P_edge_A) > 0.10` (both
  excluded) — reported as its own finding, opening a fresh question rather
  than resolving the existing one.
- **"Method disagreement"**: `rel_dev(P_wide, P_fft)` relative to their
  mean `> 0.10` — neither number is trusted as "the" wide-window period
  until reconciled.

`rel_dev` throughout matches this sub-thread's own established convention:
`|P_model − P_target| / P_target`.

**R5 specificity control** (mandatory, RULED OUT registry): before any of
the above STABLE/period-match outcomes is reported as evidence, re-score
`(P_wide, R²_wide)` against the same 60-point `[1°,15°]` target grid
exp-084 used; if `frac_clear ≥ 0.15` (comparable to the band's own ~20%
width), downgrade the period-match reading one tier, exactly as exp-084's
own convention specifies. **No circular-shift null is run on the wide
curve** — per R10's own explicit carve-out (RULED OUT registry): this
curve is deterministic and zero-noise by construction, so a
null-under-noise question does not apply; the entire point of this cycle
is that width and density, not a significance test, are what let a
noise-free curve answer the period question with certainty. This is
stated explicitly, not silently assumed.

### 5. Idealizations

1. **2D scalar Huygens–Fresnel model only** — identical scope to exp-084
   leg (a); no new physics, only a wider/denser evaluation of the same
   already-validated function.
2. **Single wavelength, 600 nm only** — no 750/450 nm generality claim;
   the x-wall wavelength-generality leg (nine cycles deferred) is untouched.
3. **Model-internal question, not a new real-FDTD comparison.** This
   cycle does not re-score leg (a) against real FDTD `C80(θ)−C40(θ)` data
   — that comparison is exp-084's own, and stands (INCONCLUSIVE, per R10).
   A "wide fit confirms `P_edge_A`" outcome here would motivate, not
   itself constitute, a future real-data re-test at a wider/denser
   FDTD-sampled window (a materially more expensive follow-up, out of
   this cycle's zero-FDTD scope).
4. **Domain restricted to `θ∈[2°,80°]`**, excluding near-normal (`<2°`,
   where `sin(θ)≈0` is a degenerate reference for a sin(θ)-periodicity
   question) and grazing incidence (`>80°`, where this scalar,
   non-vector, non-polarization-resolved approximation of the true FDTD
   vector fields is least trustworthy, and where a physically swept
   flashlight beam would not plausibly operate relative to this bench's
   own source-aperture axis).
5. **Method C's sub-window width (`±3°`, matching the original real-data
   window) is a comparability choice, not a claim of first-principles
   optimality** — a different sub-window width could in principle recover
   a different local-stability verdict; this is disclosed, not defended
   as the only valid diagnostic scale.
6. **FFT peak-sharpness (Method B) is a corroborating signal for
   determination (a), not the sole one** — a slowly-chirping tone over a
   short-enough domain could in principle still present a deceptively
   sharp spectral peak; Method C's direct local-fit trend is the primary
   test, Method B the independent cross-check.

### 6. Realizability / cost note

Zero new FDTD calls. Zero realizability content — MATERIALS' own seat duty
(the realizability bound) does not engage this cycle, matching every prior
T28 empty-scene/geometry-fact desk cycle's own standing framing rule
(established Iteration 59/60). Total new function evaluations: Method A
(3,901) + Method B (32,768) + Method C (37×31=1,147) ≈ 37,800 evaluations
of an already-validated closed-form function, each O(aperture length,
~1,504 points) — trivially fast (sub-minute aggregate), well inside a
single desk cycle's budget. New code: a grid generator + FFT/peak-finder
(~40 lines) and a sub-window loop (~20 lines), both thin wrappers around
already-committed, unchanged machinery (`edge_diffraction_c_empty_
corrected`, `free_period_with_widening`). No `lab/` engine change, no
trust-suite implication.
