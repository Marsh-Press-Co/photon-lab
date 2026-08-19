**SUPERSEDED — see `NOTES.md` (Phase 3 + Phase 5), `phase3_synthesis.md`,
`phase2_redteam_audit.md` and `phase5_redteam_audit.md`. This Phase-1 draft is
preserved UNEDITED below as the historical record of what Phase 1 actually
proposed and Phase 2 actually critiqued (T10's "flag, don't rewrite"
convention, extended to a Phase-1 draft at exp-045 `f48de18` and applied here
at the Iteration-23 Phase-5 close, Red Team docket item 3). What below is
superseded, and by what:**

- **"eye-invisible" (§1's seat sidecar; prediction P-TH23-B3 — lines 46 and
  342 of the un-bannered file `8950125`, now offset by this banner) —
  STRUCK.** A perceptual claim whose only falsifier was a detector
  ratio, i.e. unfalsifiable as posed, and constraint-3-shaped (Phase-2 docket
  item 20; VISION SCIENCE upheld in full). It appears in **no** live artifact,
  **no** scored prediction and **no** committed result of this cycle; it
  survives only in the two loci named above, in this preserved draft.
- **§2.1's geometry table — SUPERSEDED.** Every oblique source width is
  `w₀/cos θ₀`, not `w₀` (Phase-2 docket item 1); the table is re-issued in
  `run.py`/`results.json`. The `w_y(450 nm, FWHM 2°, θ₀=40°) = 199.33` entry
  is a θ₀=36° value pasted into a θ₀=40° column; corrected to **210.54**
  (docket item 2).
- **§1's N_F range (~310–518 → 0.32–40.7, and §2.1's 0.24–39.6) —
  SUPERSEDED** by the corrected width: the committed range is **0.38–67.5**
  (0.40–67.5 at θ₀=40°), and the aperture ratio is **2.15×–35.8×**, not
  2.80×–46.70× (docket item 3).
- **Idealization 2 (paraxial Gaussian relation) — SUPERSEDED TWICE.** The
  waist is **1.0737 λ at all three wavelengths, one value**, not "1.07–1.34 λ"
  (docket item 12). And its successor's "consequently the 3-λ sweep carries no
  material wavelength dependence" clause is itself **struck at Phase 5**
  (docket item 10): the medium is dispersionless and the emitter
  λ-scale-invariant, but `N_F ∝ λ_cells` and the reading is strongly
  chromatic — **4 of 36 cells read positive C**, a sign reversal across the
  visible band.
- **Idealization 4 (aperture truncation) — SUPERSEDED TWICE.** The unaimed rim
  residual is **9.99×10⁻³ in amplitude / 9.98×10⁻⁵ in intensity**, 25×/657×
  worse than the "≤3.90×10⁻⁴ / ≤1.52×10⁻⁷, four-plus orders below `C_THR`"
  claimed here (docket item 11). And its successor's "still below `C_THR`"
  clause is **also struck at Phase 5** (p5 docket item 11): the amplitude is
  *above* `C_THR` = 0.005, only the intensity is below — and comparing a
  source-plane field residual to a Weber contrast threshold is a category
  error in either direction.
- **The "sourced" silicon label (§2.3's parameter table) — DOWNGRADED** to `ASSUMED — provenance terminates unsourced (T18)`. The chain
  reads exp-046 §2.3 → exp-037 `NOTES.md:828-829` → "standard *cited* thermal
  constants" → grep returns only that sentence. The values are correct for
  bulk crystalline Si; the **label** was wrong (docket item 18).
- **Prediction P-TH23-A3 — RE-SCOPED.** Not an experimental result but an
  algebraic identity of `beam_divergence_coherent` (Phase-2 Attack 2), and its
  "5–20% divergence at FWHM=20°" clause hard-falsifies pre-run under the
  corrected width. Its residual is QUANTUM's closed form
  `w_meas/w_line = 1/√(1−4σ_θ² tan²θ₀)`, **not** taper truncation (p5 docket
  item 7). And the identity is a statement about the effective aperture's
  **central lobe only**: at the 9 FWHM=20° cells the synthesised object is a
  three-lobe comb carrying 41.7–68.0% of its intensity outside ±3·w_line
  (p5 docket item 6).
- **Prediction P-TH23-A4 — DROPPED** at Phase 3 on its 5–20% magnitude band
  (docket item 7). Its stated **mechanism** — 41-point angular-sampling
  aliasing — is **restored as real** at Phase 5 (p5 docket item 8): n=41→401
  moves the scored `C_empty` by up to 4.473%.
- **Prediction P-TH23-A7 — DROPPED** at Phase 3 (docket item 9): the ratio
  estimator is ill-conditioned by 77–300× at these `C_empty` values. Its two
  object-present FDTD legs still run, as EXPLORATORY-NON-SCORING.
- **§2.3's "decided by the conduction length alone" — CORRECTED** to the full
  `ρ C_P L²/(4εσT³L + k_air)` dependence (docket item 19), and T23's own
  disposition now lives in `results.json`'s `t23_disposition` key rather than
  only in this document (p5 docket item 14).
- **The Tier-2 escalation's soft form — HARDENED** (docket item 24), and the
  hardened rule itself **repaired** at Phase 5 (p5 docket item 4): see
  `NOTES.md` for the one canonical rendering.

---

# PHASE 1 — PROPOSAL · Panel Iteration 23 · Lead seat: THERMODYNAMICS

## "The Aperture-Consistent Single-Mode Beam, T23's Mixed Length-Scale Regime, and the Dose-Accumulation Extension" (candidate exp-046)

*Runner: cloud panel shift · rotation: VISION→PHOTONICS→MATERIALS→ELECTROMAGNETISM→**THERMODYNAMICS**→QUANTUM.
Protocol: PANEL.md. Memory: LOGBOOK.md (RULED OUT R1/R2/R3 checked — nothing here
resurrects a ruled-out idea; this cycle proposes no mechanism at all).*

---

## 1. Mechanism / test narrative (≤300 words)

**This is NOT a T1 mechanism proposal** (unlike exp-041/042/043/044/045's own
mechanism-adjacent legs). It is instrument- and model-fidelity characterization,
in the Iteration-20/22 precedent. No new material law, no new escape route, no
constraint-3 verdict. **T1 escape route: NONE.**

**Block A — the aperture-consistent single-coherent-mode beam** (Iteration-22's
hardened unconditional rule; live thread T21). exp-042's beam-divergence check
held the full 1504-cell (60.2–100.3 λ) source aperture fixed while imposing an
angular spectrum of FWHM Δθ. A physically real single-mode emitter of divergence
Δθ has a diffraction-limited waist w₀ = 2√(2 ln 2)·λ/(2π·Δθ) — **2.80×–46.69×
narrower** than this bench's aperture. Block A replaces the taper with that
Gaussian waist and injects **one** angle, on exp-042's own geometry, propagator
and reduction. A small FDTD leg validates the propagator at the new Fresnel
numbers (N_F falls from ~310–518 to 0.32–40.7) and gates
`add_line_source(profile="gauss")` — an engine path declared in `lab/fdtd2d.py`
but, grep-verified, **never once exercised or trust-gated** in this program's
history. Committed prediction, *opposite to QUANTUM's own*: the aperture-
consistent reading lands on the **coherent** column, not near the incoherent
one — because a coherent Gaussian angular spectrum over a wide aperture already
*is* the diffraction-limited single mode.

**Block B — resolve T23.** Add PHOTONICS' third, genuinely mixed regime (power
on `w_on` per its own calibration; conduction/mass on `r_out` per the Nu=2
conduction-limit formula's own derivation requirement) to exp-045's
`self_consistent_regime`. Desk-only.

**Block C — dose accumulation beyond Host D.** Extend `coupled_segment_general`
over the remaining 12 host/ratio points on exp-045's exact convention, scored
against `REALIZABILITY_MEMO.md`'s tiers, plus a closed-form memory-onset
criterion and a 5-decade pulse-duration scan testing Amendment 3's own Red-Team
tempering. Desk-only.

**Seat sidecar (charter):** the mixed regime raises the ON-endpoint steady-state
ΔT ceiling to 3.293×10⁻⁵ K — 607× below NETD, Wien peak 9.885 µm, eye-invisible.

*(295 words)*

---

## 2. Parameter tables

Every number below is either copied from a cited repo line or computed from cited
repo constants by a formula stated in full. Nothing is asserted from memory.

### 2.0 Geometry — inherited VERBATIM, not rebuilt

| Constant | Value | Source |
|---|---|---|
| `NX`, `NY` | 360, 1584 | `experiments/042-t21-magnitude-bridge/design_geometry.py:119-120` |
| `ABSORB`, `TAPER` | 40, 40 | ibid. `:121-122` |
| `SRC_X`, `PLANE_X` | 300, 77 | ibid. `:123-124` |
| `R_OUT`, `GUARD_OUT`, `W_FLANK` | 78, 185, 78 | ibid. `:126-128` |
| `CPL` (λ_cells) | {450:15, 600:20, 750:25} | ibid. `:129` |
| `STEPS`, `COURANT_FRAC` | 1400, 0.99 | ibid. `:130-131` |
| `OBJ_Y` | 792 | ibid. `:133` |
| `D_SP` = `SRC_X`−`PLANE_X` | 223 | ibid. `:134` |
| `Y_LO`, `Y_HI` | 40, 1544 | ibid. `:135-136` |
| full aperture `Y_HI`−`Y_LO` | **1504 cells** = 100.3/75.2/60.2 λ at 450/600/750 nm | computed from `:135-136`, `:129` |
| `C_THR` | 0.005 (VISION's T2 photopic bar) | `experiments/042-t21-magnitude-bridge/run.py:41` |
| object window / flank windows | \|y−792\| ≤ 78 / 185 ≤ \|y−792\| ≤ 263 | `lab/ambient.py:42-50` with the constants above |
| `SIGMA_SPONGE` | 6.41025641025641×10⁻⁴ (τ_center = 0.10) | `experiments/041-t20-angle-audit/design_geometry.py:140-141` |

The exp-042 grid this block corrects: λ ∈ {450,600,750}, θ₀ ∈ {36,38,40}°,
FWHM ∈ {2,5,10,20}° — 36 cells (`experiments/042-t21-magnitude-bridge/run.py:89-91`).
Angular sum machinery being replaced: `gaussian_angle_weights` (n=41, ±2.5·FWHM,
σ = FWHM/2.3548), `beam_divergence_incoherent` (`design_geometry.py:310-334`),
`beam_divergence_coherent` (`:337-355`).

### 2.1 Block A — the diffraction-limited aperture width

**Relation chosen: the Gaussian-beam (fundamental-transverse-mode) relation, not
the single-slit relation.** Reasons, stated because Red Team will ask:

1. The check's own name is *single-coherent-mode*. The fundamental Gaussian is
   the exact single transverse eigenmode of free-space paraxial propagation; a
   uniformly-illuminated slit is a *superposition* of modes and is exactly the
   hard-edged object whose two rim discontinuities generate the T21 fringe
   (period P(θ)=λ/(A·cosθ), A=752, `design_geometry.py:137`) this cycle is trying
   to remove from the illumination model.
2. `lab/fdtd2d.py:152-156` already implements a Gaussian aperture
   (`profile="gauss"`, `p = exp(−((y−y_c)/width)²)`), so `width` maps to the
   Gaussian waist **w₀ exactly** — amplitude 1/e radius = intensity 1/e² radius —
   with no new engine code. A slit convention would need a new profile.
3. A Gaussian aperture has no edges, so the far-field FWHM relation is exact and
   side-lobe-free; a slit's sinc² FWHM (Δθ = 0.886 λ/a) is a first-null-adjacent
   half-max whose "aperture width" is ambiguous once a taper is applied.

**Derivation (2-D / one transverse dimension).** E(y) = exp(−y²/w₀²) ⇒ angular
amplitude spectrum ∝ exp(−k_y²w₀²/4) ⇒ far-field intensity ∝ exp(−k²θ²w₀²/2).
Half-max at k θ w₀ = √(2 ln 2); **full-angle intensity FWHM
Δθ = 2√(2 ln 2)/(k w₀) = [2√(2 ln 2)/2π]·λ/w₀**, hence

> **w₀ = C·λ_cells / Δθ_rad ,  C = 2√(2 ln 2)/(2π) = 0.3747808…**

(Sanity anchor: the 1/e² half-angle is λ/(π w₀), the textbook Gaussian-beam
divergence; FWHM/(1/e² half-angle) = √(2 ln 2) = 1.17741.)

| λ (nm) | λ_cells | FWHM (°) | **w₀ (cells)** | 2w₀ (cells) | 1504/(2w₀) | z_R = πw₀²/λ (cells) | z_eff/z_R at θ₀=40° | w_y(z) at θ₀=40° (cells) | N_F = (2w₀)²/(λ z_eff) |
|---|---|---|---|---|---|---|---|---|---|
| 450 | 15 | 2 | **161.05** | 322.10 | 4.67× | 5432.3 | 0.0536 | 199.33 | 23.76 |
| 450 | 15 | 5 | **64.42** | 128.84 | 11.67× | 869.2 | 0.3349 | 88.69 | 3.80 |
| 450 | 15 | 10 | **32.21** | 64.42 | 23.35× | 217.3 | 1.3397 | 70.29 | 0.95 |
| 450 | 15 | 20 | **16.11** | 32.21 | 46.69× | 54.3 | 5.3588 | 114.61 | 0.24 |
| 600 | 20 | 2 | **214.73** | 429.47 | 3.50× | 7243.0 | 0.0402 | 280.54 | 31.68 |
| 600 | 20 | 5 | **85.89** | 171.79 | 8.76× | 1158.9 | 0.2512 | 115.61 | 5.07 |
| 600 | 20 | 10 | **42.95** | 85.89 | 17.51× | 289.7 | 1.0048 | 79.47 | 1.27 |
| 600 | 20 | 20 | **21.47** | 42.95 | 35.02× | 72.4 | 4.0191 | 116.10 | 0.32 |
| 750 | 25 | 2 | **268.42** | 536.83 | 2.80× | 9053.8 | 0.0322 | 350.57 | 39.60 |
| 750 | 25 | 5 | **107.37** | 214.73 | 7.00× | 1448.6 | 0.2010 | 142.96 | 6.34 |
| 750 | 25 | 10 | **53.68** | 107.37 | 14.01× | 362.2 | 0.8038 | 89.91 | 1.58 |
| 750 | 25 | 20 | **26.84** | 53.68 | 28.02× | 90.5 | 3.2153 | 117.98 | 0.40 |

z_eff = `D_SP`/cos θ₀ = 291.1 cells at θ₀=40°; w_y(z) = w₀√(1+(z_eff/z_R)²)/cos θ₀
(the 1/cos θ₀ factor is the oblique-incidence stretch of the transverse profile
onto the y-axis of the observation plane). **Full-aperture reference N_F at
θ₀=40°: 518.0 / 388.5 / 310.8 at 450/600/750 nm** — i.e. this block moves the
propagator from N_F ≈ 310–518 down to 0.24–39.6, a regime change the exp-042
propagator has never been validated in. That is the entire reason the FDTD leg
exists.

The 1504/(2w₀) column **spans 2.80×–46.69×**, bracketing the "3–30× smaller"
figure LOGBOOK's T21 entry cites — the citation is right in central tendency and
slightly narrow at both ends; corrected here with the exact numbers.

**Geometric pointing.** walk = `D_SP`·tan θ₀ = **162.02 / 174.23 / 187.12 cells**
at θ₀ = 36/38/40°. Two pointing conventions are reported side by side, disclosed,
never merged:

* **A-unaimed (PRIMARY — QUANTUM's literal spec).** Source span left at the
  `add_line_source` defaults, so y_c = ½(40+1544) = 792 = `OBJ_Y` exactly
  (`lab/fdtd2d.py:144-145,153`). Beam axis lands at 792 + walk.
* **A-aimed (SECONDARY control, analytic only).** Symmetric span about
  y_c,aim = 792 − walk = **629.98 / 617.77 / 604.88** → integer 630/618/605, so
  the beam axis lands on `OBJ_Y`. Analytic-only because the symmetric span
  truncates the widest waists at 2.10–2.75 w₀ (see idealization 4), and because
  it is a pointing diagnostic, not a contamination reading. (Truncation at the
  widest waists: 2.10–2.75 w₀.)

### 2.2 Block A — new FDTD calls (the ONLY FDTD in this cycle)

| # | Leg | λ | θ₀ | source | purpose / gate |
|---|---|---|---|---|---|
| 1 | S16-a | 600 | 0° | `profile="gauss"`, `width`=40 | Gaussian free-space divergence identity: w(z) at ≥3 planes vs w₀√(1+(z/z_R)²), z_R = π·40²/20 = 251.3 cells; ≤3% |
| 2 | S16-b | 600 | 40° | `profile="gauss"`, `width`=40 | pointing identity: beam centroid at `PLANE_X` = y_c + `D_SP`·tan 40° ± 2 cells |
| 3 | S16-c | 600 | +40° | `profile="plane"`, `edge`=40 | **absolute regression anchor**: must reproduce exp-041 Block MAIN's committed `C_empty(+40°,600nm) = −0.010964794540566314` (`experiments/041-t20-angle-audit/results.json`) to ≤1×10⁻¹² |
| 4 | A-v1 | 600 | 40° | gauss, `width` = 214.73 | propagator validation, N_F = 31.7 |
| 5 | A-v2 | 600 | 40° | gauss, `width` = 42.95 | propagator validation, N_F = 1.27 |
| 6 | A-v3 | 600 | 40° | gauss, `width` = 21.47 | propagator validation, N_F = 0.32 (far-field transition) |
| 7 | A-v4 | 750 | 38° | gauss, `width` = 268.42 | exp-042's own worst incoherent cell (C = −0.004006, `results.json` `phase5_erratum.block_beam_corrected.worst_cell`), N_F = 40.7 |
| 8 | A-o1 | 600 | 40° | gauss, `width` = 42.95, `sigma`=`SIGMA_SPONGE` | object-present pair for run 5 |
| 9 | A-o2 | 600 | 40° | gauss, `width` = 21.47, `sigma`=`SIGMA_SPONGE` | object-present pair for run 6 |

Runs 1–3 constitute proposed **trust-suite stage 16** (`lab/validation/run_all.py`
gains one function; **no `lab/` engine file is touched**). Per PANEL.md's Phase-4
gate and CLAUDE.md's standing rule, the full suite (41 fast stages + stage 16) is
re-run and green **before any Block-A number is read**. Note that gating w(z)
against the closed form *is* gating the FWHM relation, since Δθ = 2√(2 ln 2)λ/(2πw₀)
follows from z_R = πw₀²/λ by one algebraic step — stated explicitly because the
domain's usable x-span (260 cells ≈ 1.03 z_R at w₀=40) cannot reach the true far
field, so a direct far-field-FWHM gate is not honestly available here.

### 2.3 Block B — T23's third, mixed regime (desk)

Inputs, all reused verbatim from `experiments/045-.../run.py`:

| Symbol | Value | Line |
|---|---|---|
| `DX_M` | 3.0×10⁻⁸ m | `:101` |
| `R_OUT_CELLS` → r_out | 78 → 2.34×10⁻⁶ m | `:102`, `:195` |
| `SIGMA_EXT_ON` → w_on | 235.96673494878587 → 7.079002048463575×10⁻⁶ m | `:103`, `:196` |
| `RATIO_ON` | 0.6074830175566805 | `:103` |
| `K_AIR_W_MK` | 0.026 | `:194` |
| ρ_Si, C_P,Si, κ_Si | 2330 kg/m³, 700 J/(kg·K), 148 W/(m·K) | `:213-215` (sourced: `experiments/037-.../NOTES.md:828-829`) |
| `EMISSIVITY`, `T_AMBIENT_K` | 0.9, 293.15 K | `:106-107` |
| `NETD_BAND_K` | (0.020, 0.050) K | `:105` |
| irradiance | 6.584362×10⁻⁶ W/cm² (= (40000/45²)/300/10⁴) | `:115-118`, `:177` |
| dwell | 0.06666667 s (= 10°/150° s⁻¹) | `:178` |

The change to `self_consistent_regime` (`:269-339`) is exactly this: give it two
lengths instead of one — `length_power_m` and `length_cond_m` — with the existing
two regimes recovered by passing the same value twice, and a third call
`self_consistent_regime(w_on_m, r_out_m, "mixed_w_power_r_cond")`. Fix 7's
cross-consistency assertion (`:297-300`) is *strengthened*, not weakened: it must
now assert `h_eff·length_cond == k_air` **and** `mass_kg == ρ·length_cond³`
**and** `p_abs` is built from `length_power` alone.

**Computed here (pure `math`, no FDTD, no numpy — reproduced the two committed
regimes exactly first, as a self-check):**

| Quantity | `w_on`-consistent (exp-045 primary) | `r_out`-consistent (exp-045 alternate) | **MIXED (this proposal)** |
|---|---|---|---|
| L_power | w_on | r_out | **w_on** |
| L_cond | w_on | r_out | **r_out** |
| h_eff (W/m²K) | 3672.8340834 | 11111.111111 | **11111.111111** |
| area (m²) | 5.0112270×10⁻¹¹ | 5.4756000×10⁻¹² | **5.4756000×10⁻¹²** |
| mass (kg) | 8.2655553×10⁻¹³ | 2.9854066×10⁻¹⁴ | **2.9854066×10⁻¹⁴** |
| dP/dT (W/K) | 1.8431176×10⁻⁷ | 6.0868159×10⁻⁸ | **6.0868159×10⁻⁸** |
| P_abs (W) | 2.0044348×10⁻¹² | 2.1901788×10⁻¹³ | **2.0044348×10⁻¹²** |
| **dt_ss_full (K)** | 1.0875241×10⁻⁵ | 3.5982340×10⁻⁶ | **3.2930761×10⁻⁵** |
| **τ_thermal (s)** | 3.1391858×10⁻³ | 3.4332969×10⁻⁴ | **3.4332969×10⁻⁴** |
| **dwell/τ_thermal** | **21.236929** | **194.176815** | **194.176815** |
| Biot | 1.7567568×10⁻⁴ | 1.7567568×10⁻⁴ | **1.7567568×10⁻⁴** |
| Knudsen (λ_air=65.7 nm) | 9.280969×10⁻³ | 2.807692×10⁻² | **2.807692×10⁻²** |
| h_eff slip-corrected | 3605.9016 | 10520.3528 | **10520.3528** |
| NETD_lo / dt_ss_full | 1839× | 5558× | **607×** |

The first two columns reproduce `experiments/045-.../results.json`
(`block_b_...length_scale_regimes`) to every printed digit — that reproduction is
the desk self-check gating the third column.

**The structural point T23 never stated.** τ_thermal = mass·C_P/(dP/dT) =
ρ C_P L³ / [L²(4εσT³ + k_air/L)] = **ρ C_P L² / (4εσT³ L + k_air)** — algebraically
independent of the absorbed power, hence of L_power. So *any* convention that
puts conduction/mass on `r_out` gives 194.176815× identically, and T23's operative
"below vs above 25" question is decided by the conduction length **alone**.

**And the stake itself is smaller than T23's framing implies.** `N_TRANSIENT_TAU
= 25.0` is defined at `lab/kinetics.py:97` as the RK4-branch switchover for
`integrate_segments` (`:131-133`, `:156`) — a *numerical-integration* constant for
the **kinetics** solver. Nothing in the thermal chain is numerically integrated at
all: `coupled_kinetics_thermal_dT` (`experiments/045-.../run.py:121-143`),
`coupled_segment_general` (`:146-172`), `steady_state_delta_T` and
`transient_delta_T` (`lab/thermo_sidecar.py:146-177`) are all exact closed forms.
Physically, the saturation fraction 1−e^(−dwell/τ_th) is **1 − 5.98×10⁻¹⁰** at
21.24× and 1 − O(10⁻⁸⁵) at 194.18×: indistinguishable. The consequential
difference between conventions is **dt_ss_full** (3.028× vs `w_on`, 9.1519× vs
`r_out`; the latter equals (w_on/r_out)² = (235.96673494878587/78)² exactly), and
the mixed regime is the **least comfortable of the three on that axis** — the one
this seat's charter actually scores.

Propagation: the mixed regime is added as a 6th entry in `TAU_TH_REGIMES`
(`:406-412`), taking Block A's sweep from 4 hosts × 4 ratios × 5 regimes × 2 axes
× 13 R-points = **2080** to **2496** points.

### 2.4 Block C — dose accumulation beyond Host D (desk)

Convention held **identical** to exp-045 Block C (`:528-620`): `n_pulses` = 5,
gaps 5τ_k and 0.5τ_k, `pulse_train_segments(k_f_ambient=k_f_on, k_r=k_r, A=0.0,
T_pulse=dt_gap, dt_sweep=dwell_central, n_pulses=5)` with the same disclosed role
inversion (`lab/kinetics.py:201-219`), ON-segment duration = dwell_central =
0.06666667 s, hard k_f=0 in the OFF gap.

**C1 — the 12 remaining host/ratio points** (Hosts A/B/C × r ∈ {1e-9,1e-5,1e-3,1e-1};
Host D's 4 were done in exp-045), 2 gaps each = **24 new points**. Tier labels per
`experiments/038-t17-rate-equation-kernel/run.py:31-45`:

| Host | k_r (s⁻¹) | τ_k at r≤1e-3 (s) | dwell/τ_k | r ≤ 1e-3 tier | r = 1e-1 tier |
|---|---|---|---|---|---|
| A | 1×10⁹ | 1.0×10⁻⁹ | 6.67×10⁷ | PUBLISHED | PLAUSIBLE |
| B | 1×10⁶ | 1.0×10⁻⁶ | 6.67×10⁴ | PUBLISHED | PLAUSIBLE |
| C | 1×10³ | 1.0×10⁻³ | 66.7 | PLAUSIBLE | PLAUSIBLE |
| D (done, exp-045) | 1×10¹ | 1.0×10⁻¹ | 0.667 | PLAUSIBLE | PLAUSIBLE |

⇒ **6 PUBLISHED-tier + 6 PLAUSIBLE-tier** among the 12 new points.

**C2 — the closed-form memory-onset criterion** (new this cycle, zero cost). For
the 11-segment train, the end-of-ON population obeys the affine map
n_(k+1) = n_eq(1−a) + a·f·n_k with a = e^(−D/τ_k) and f = e^(−k_r·G) = e^(−m/(1+r))
for a gap G = m·τ_k. Its fixed point gives

> **ratio_∞ = n_ON,∞ / n_ON,1 = 1 / (1 − a·f)**

⇒ ratio_∞ > 1.05 ⟺ a·f > 1/21 ⟺ **D/τ_k < ln(21 f)**. For m = 0.5, r ≪ 1:
f = e^(−0.5) = 0.6065307, threshold **D/τ_k = 2.5443**. For m = 5: f = e⁻⁵ =
0.0067379, 21f = 0.1415 < 1 ⇒ **no dwell whatever can exceed 1.05**, and the
supremum is 1/(1−f) = **1.006784**.

Desk validation against exp-045's own committed 8 Host-D points (`results.json`
`block_c_...points`): closed form 1.005125 / 1.438574 / 1.452229 vs committed
1.0051247 / 1.437419 / 1.450904 — agreement **2.6×10⁻⁷ to 9.1×10⁻⁴** relative
(the 10⁻⁴-level residual is the finite-5-pulse offset from the exact periodic
fixed point, in the expected direction: 5 pulses under-converge).

**C3 — the pulse-duration scan** Red Team's own Amendment-3 tempering demands
(`REALIZABILITY_MEMO.md`, AMENDMENT 3: "substantially a near-mechanical
consequence of exp-038's own fixed pulse-duration parameter (0.1 s)"). All 16
host/ratio points × T_pulse ∈ {1 ms, 10 ms, 66.7 ms, 100 ms, 1 s} × 2 gaps =
**160 points**, testing whether "memory only at Hosts D/E" is a host property or
a duration artifact.

ΔT classification uses the **mixed regime as primary** (dt_ss_full =
3.2930761×10⁻⁵ K, τ_th = 3.4332969×10⁻⁴ s), with `w_on`- and `r_out`-consistent
reported alongside — so Blocks B and C are one coherent chain, not two.

---

## 3. T1 escape-route statement

**NONE.** This cycle proposes no material law, no σ(I), no σ(x,t), no angular
selectivity, no sub-threshold operation, and no new mechanism class. It changes
nothing about which escape routes T1 permits. It characterizes (a) an
illumination model used by the ambient-contrast instrument, (b) a length-scale
convention inside the THERMODYNAMICS sidecar, and (c) the coverage of an existing
kinetics closed form. Per PANEL.md's Latitude rule there is nothing exotic to
bound; per the Iteration-20/22 precedent an instrument cycle states NONE rather
than manufacturing an escape-route claim. No constraint-3 or constraint-4 verdict
is issued, at either tier, and no result here can move either
`REALIZABILITY_MEMO.md` UNOBTANIUM-WITH-PARAMETERS verdict.

---

## 4. Falsifiable predicted outcomes — committed BEFORE any run

Numeric bands. Nothing in Block A's Huygens–Fresnel or FDTD output has been
computed; the Block A predictions come from an independent closed-form
Gaussian-envelope model derived at Phase 1 (shown below), deliberately kept as a
*prediction* rather than pre-computing the answer. Blocks B and C are desk items
whose numbers are computed here in full, per the Director's brief and exp-045's
own Block-B precedent; their falsifiable content is exact-identity reproduction,
which a coding error breaks.

**The zero-free-parameter envelope model used to set Block A's bands** (paraxial
tilted Gaussian, no diffraction integral, no taper, no obliquity):
b(y) = exp(−2(y−y_peak)²/w_y(z)²), y_peak = y_c + `D_SP` tan θ₀, w_y(z) per §2.1,
reduced through `lab.ambient.window_means`/`weber` unchanged. Its 36-cell output
(unaimed) spans |C| = 2.99×10⁻² … 9.98×10⁻¹.

| ID | Prediction | Committed band | Hard falsification |
|---|---|---|---|
| **P-TH23-A0** | Aperture arithmetic gate: w₀ = 0.3747808·λ_cells/Δθ_rad reproduces §2.1's 12 values | exact to 6 s.f.; 1504/(2w₀) ∈ [2.80, 46.70] | any mismatch |
| **P-TH23-A1** | **Headline, contradicting QUANTUM's own Iteration-20 prediction:** the aperture-consistent single-mode reading does **NOT** land near the incoherent sum | \|C_empty\| > `C_THR`=0.005 at **≥34 of 36** cells (central expectation 36/36); \|C_empty\| ≥ 20× the corrected-convention incoherent value at **≥30/36** | ≥18/36 cells land within a factor 3 of the incoherent reading (⇒ QUANTUM right, this seat wrong) |
| **P-TH23-A2** | The reading is set by the beam's own transverse envelope, not by the T21 edge fringe: it tracks the envelope model | ≤5% relative at **≥30/36** cells, ≤10% at **36/36** | >6 cells exceed 10% |
| **P-TH23-A3** | **Reinterpretation of exp-042's "beamformed" column:** the aperture-consistent reading reproduces exp-042's committed `C_coherent` (`results.json` `block_beam.rows`) | ≤3% relative at the **24 cells with FWHM ≤ 10°**; **5–20%** divergence at the 12 FWHM=20° cells | >4 of the FWHM≤10 cells exceed 3%, **or** the FWHM=20 divergence is <2% (⇒ the angular-replica explanation is wrong) |
| **P-TH23-A4** | The FWHM=20° divergence in A3 is the 41-point angular sampling aliasing: replica spacing λ/δθ = 343.8/458.4/573.0 cells at 450/600/750 nm, comparable to the 526-cell object+flank span, vs 687–5730 cells at FWHM ≤ 10 | monotone degradation with FWHM at all 3 λ | non-monotone in FWHM at any λ |
| **P-TH23-A5** | FDTD validates the propagator at the new Fresnel numbers | analytic vs FDTD `C_empty` ≤**15%** relative at runs 4/5/7 (N_F = 31.7/1.27/40.7), ≤**35%** at run 6 (N_F = 0.32); sign agreement 4/4 | any cell >50%, or any sign disagreement |
| **P-TH23-A6** | Stage-16 gates pass | S16-a ≤3%; S16-b ≤2 cells; **S16-c reproduces −0.010964794540566314 to ≤1×10⁻¹²** | any gate fails ⇒ **no Block-A number is reported at all** |
| **P-TH23-A7** | *(EXPLORATORY, wide band, may be dropped at Phase 3)* Under aperture-consistent illumination the envelope largely cancels in the ratio estimator T7 retired: C_corr = (1+C_scene)/(1+C_empty) − 1 recovers exp-041's full-aperture sponge reading (−0.05815337265493213) | C_corr **negative** at both cells, \|C_corr\| ∈ [0.019, 0.18] (within 3× of 0.0582) | \|C_corr\| outside [0.006, 0.6], or positive sign at either cell |
| **P-TH23-B1** | Mixed regime's dwell/τ_thermal **equals** the `r_out`-consistent value identically (τ_thermal is independent of L_power) | **194.176815** ± 1 in the 12th s.f. | any difference beyond float round-off |
| **P-TH23-B2** | Mixed dt_ss_full | **3.2930761×10⁻⁵ K**; ratio to `r_out` = (w_on/r_out)² = **9.151923** exactly; ratio to `w_on` = **3.02805** | ±0.01% on any of the three |
| **P-TH23-B3** | Mixed regime is still UNDETECTABLE and eye-invisible (seat sidecar) | NETD_lo/dt_ss_full = **607×** ∈ [600, 615]; Wien peak **9.885 µm** ∈ [9.87, 9.90] | classification ≠ UNDETECTABLE |
| **P-TH23-B4** | Biot / Knudsen at the mixed regime match the `r_out` regime exactly (length-invariance of Bi = k_air/k_solid, Red Team's Attack 6) | Bi = **1.7567568×10⁻⁴**, Kn = **2.807692×10⁻²**, slip correction **−5.3168%** | any mismatch |
| **P-TH23-B5** | Block A regrows to 6 regimes; new-regime max exact-coupled ΔT | **2496** points; max ΔT over the 416 new points ∈ [2.95×10⁻⁶, 3.05×10⁻⁶] K, NETD_lo margin ≥ **6500×**; all 2496 UNDETECTABLE-or-better | any point DETECTABLE, or max outside the band |
| **P-TH23-B6** | The `N_TRANSIENT_TAU=25` stake is void: thermal saturation at both endpoints | 1−e^(−dwell/τ_th) ≥ **1 − 1×10⁻⁹** at *both* 21.24× and 194.18× (computed: 1 − 5.98×10⁻¹⁰ and 1 − O(10⁻⁸⁵)) | saturation < 1 − 1×10⁻⁹ at either |
| **P-TH23-C1** | Zero dose accumulation at all 24 new Host-A/B/C points (D/τ_k ≥ 66.7 ⇒ every ON segment re-equilibrates: residual ~e⁻⁶⁶·⁷ ≈ 10⁻²⁹) | \|ratio − 1\| ≤ **1×10⁻¹²** at 24/24 | any point > 1×10⁻⁶ |
| **P-TH23-C2** | The decoupled ΔT proxy stays conservative on the extended grid | exact/decoupled ∈ [1−1×10⁻⁸, 1] at 24/24, all three regimes; conservatism 24/24 | any point > 1, or < 1−1×10⁻⁶ |
| **P-TH23-C3** | ΔT at the extended grid (mixed regime primary) | max decoupled ΔT = **2.99371×10⁻⁶ K** ∈ [2.9×10⁻⁶, 3.1×10⁻⁶]; NETD_lo margin **6681×** ≥ 6000×; 24/24 UNDETECTABLE | outside band or any DETECTABLE |
| **P-TH23-C4** | Tier scoring: zero memory at **all 6 PUBLISHED-tier** new points — corroborating `REALIZABILITY_MEMO.md` Amendment 3 at a *different* pulse duration (66.7 ms vs exp-038's 100 ms) | 6/6 PUBLISHED and 6/6 PLAUSIBLE at ratio = 1.000000 | any PUBLISHED point > 1.05 |
| **P-TH23-C5** | The closed form reproduces exp-045's own committed Host-D points | ≤**0.2%** relative at 8/8 (computed: 2.6×10⁻⁷ – 9.1×10⁻⁴) | any point > 0.2% |
| **P-TH23-C6** | **Amendment 3's host-list finding is a dimensionless-dwell finding.** Across the 160-point duration scan, ratio > 1.05 at the 0.5τ gap **iff D/τ_k < 2.54 ± 0.05**, at ≥95% of points; at the 5τ gap **no point anywhere exceeds 1.05**, sup = 1.006784 | as stated | a 5τ point exceeds 1.05, or the 0.5τ threshold sits outside [2.4, 2.7] |

**What would make this cycle a failure, stated plainly:** if P-TH23-A1 falls the
way QUANTUM predicted, this seat's whole reading of exp-042's coherent column is
wrong and T21's contamination risk reverts to the incoherent reading — that is a
real, pre-registered way for this proposal to lose.

---

## 5. Idealizations (lab convention — stated, not buried)

1. **Expressibility contract (PANEL.md, this seat's charter):** every Block-B and
   Block-C number is a **post-run analytic calculation, not an FDTD output**, and
   is labelled as such in `results.json`. Blocks B and C run zero field solves.
2. **Paraxial Gaussian relation.** w₀ = 0.3747808 λ/Δθ assumes sin θ ≈ θ. Error
   ≤**1.5%** at FWHM=20° (1/e² half-angle 16.99°), ≤0.02% at FWHM=2°. At FWHM=20°
   the waist is only 1.07–1.34 λ, at the edge of paraxial validity — disclosed,
   and it is precisely where P-TH23-A5's loosest band sits.
3. **Fully coherent, monochromatic, single transverse mode.** A real flashlight is
   none of these. **No sourced coherence length or beam FWHM for any real
   flashlight exists anywhere in this program** (T21's own standing gap, LOGBOOK
   Iteration 19). The Gaussian Schell-model partial-coherence bridge T21
   pre-registered remains unbuilt; this cycle does not build it and does not
   claim to.
4. **Aperture truncation.** Unaimed leg: the Gaussian is untruncated over the
   default span, residual amplitude at the hard rim ≤**3.90×10⁻⁴** (worst cell
   750 nm/FWHM=2°, w₀=268.42), i.e. ≤1.52×10⁻⁷ in intensity — four-plus orders
   below anything `C_THR` can see, so no new hard-edge fringe is smuggled in.
   Aimed leg truncates at **2.10–2.75 w₀** (residual amplitude ≤**1.19×10⁻²**,
   worst at 750 nm/θ₀=40°/FWHM=2°) for the FWHM=2° cells only; that is why the
   aimed leg is analytic-only and diagnostic.
5. **Thermal body shape.** exp-045's cube idiom (area = L², volume = L³,
   `run.py:277-279`) is inherited **unchanged**, so the mixed regime differs from
   the existing two in exactly one variable. Disclosed sensitivity: a true disk
   (π r² area, 2r thickness) gives dwell/τ_thermal = **97.09×** instead of
   194.18× and dt_ss_full = 1.048×10⁻⁵ K — still ≫ any saturation concern, still
   UNDETECTABLE, no verdict moves.
6. **Material identity** reused from `experiments/037-.../NOTES.md:828-829`, not
   re-sourced (T18 WebFetch still EGRESS_BLOCKED — 11th consecutive shift
   confirmation). Following Iteration 22's fabricated-PMMA lesson: no citation in
   this document is offered that is not a live path in this repo.
7. **Block C's OFF gap uses hard k_f = 0** (exp-045's own disclosed idealization,
   QUANTUM's Phase-5 catch) — unchanged, so C1 is comparable to exp-045's Host-D
   points.
8. **Bench-scale, not witness-scale.** T8/T13's near-field→witness bridge is
   unresolved; no ΔT or C here extrapolates to 45 m.
9. **NETD is an instrument/detector threshold, not a human perceptual one**
   (`lab/thermo_sidecar.py:193-199`, standing mandatory disclaimer). Stored
   per-point at all 2496 + 24 + 160 points, not block-scope-only — the exact
   regression Iterations 21 and 22 both had to fix.
10. **FDTD settling.** exp-041's 1400 steps and its λ-dependent causal transit
    margin (13.0/9.8/7.8 periods at 450/600/750 nm,
    `experiments/042-.../design_geometry.py:96-104,187-192`) are inherited
    unchanged; the margin is thinnest at 750 nm, which is run 7. Disclosed,
    untested confound — and still the *fourth* consecutive cycle in which
    PHOTONICS'/EM's dedicated settling-margin test is not run.
11. **A-unaimed's beam walks off the object window** by 162–187 cells while the
    object window is only ±78 cells wide. That is a real property of the geometry,
    not a defect, and it is exactly why A-aimed is reported beside it.

---

## 6. Cost note

**New FDTD calls: 9.** All in Block A (§2.2): 3 stage-16 gates + 4 propagator
validations + 2 object-present pairs. Estimated wall clock ≈**30 s parallel /
≈90 s sequential**, from exp-041's own measured 91.6 s for 30 identical-domain
runs (`experiments/041-t20-angle-audit/results.json`,
`block_main.elapsed_s`/`n_new_runs` = 3.05 s per run). Blocks B and C add **zero**.

**Desk-only items:** Block A's 36-cell analytic grid × 2 pointing conventions ×
2 obliquity conventions (corrected E/H primary per exp-042's Phase-5 erratum,
committed obliquity-on-E secondary) = 144 propagator evaluations, a few seconds;
Block B's three regimes plus Block A's regrown 2496-point sweep; Block C's 24 + 160
points. Total desk runtime comparable to exp-045's 0.27 s.

**Code footprint:** `experiments/046-.../run.py` (new); `lab/validation/run_all.py`
gains one stage-16 function. **No `lab/` engine file is modified** — `fdtd2d.py`,
`ambient.py`, `kinetics.py`, `thermo_sidecar.py` all untouched. The full suite is
re-run green (41 fast stages + stage 16) before any result is read (CLAUDE.md).

### Tier-2 disposition — stated explicitly, not by silent default

**VISION's glare/adaptation Tier-W sidecar is DEFERRED.** Reasons, specific rather
than generic:

1. It is Tier 2 in Red Team's own Iteration-22 ranking; all three Tier-1 items are
   delivered here, and Iteration 22's own lesson was that a Phase-1 deferral with
   a *weak* reason gets overridden at Phase 3 (Block C) while scope creep gets
   punished at Phase 2.
2. It is a **sourcing** deliverable — disability-glare veiling luminance and
   adaptation-state thresholds, "with sources," per PANEL.md's VISION duty — and
   the sourcing channel it needs (T18/WebFetch for scholarly domains) has been
   EGRESS_BLOCKED for **eleven consecutive shift confirmations**. Producing
   numeric perceptual thresholds from seat memory is exactly the failure mode
   that produced Iteration 22's fabricated PMMA citation, the single worst defect
   of the last cycle. THERMODYNAMICS declines to repeat it.
3. PANEL.md assigns threshold-pinning to VISION SCIENCE, not to this seat, and
   requires it *before* any run scored against those thresholds — nothing in
   exp-046 is scored against a glare threshold, so the tripwire is not load-bearing
   for this cycle's own claims.

**Escalation attached to the deferral, so it does not silently recur a third
time:** the rotation puts VISION's lead turn at Iteration **25**, which is too
late. This proposal recommends it as Iteration **24's Tier-1 #1**, run by
QUANTUM as lead under the same "any lead seat" wording Iteration 22 used for the
aperture check, with a WebSearch-snippet-level sourcing convention (the same
T18-adapted standard `WitnessScenario` already uses,
`lab/thermo_sidecar.py:224-243`). If it slips past Iteration 24 it should be
treated as a Red Team program-integrity item, not a queue item.

**Tier-2 "extend Block C's dose-accumulation check to the remaining 12 host/ratio
points" is NOT deferred** — it is Block C above, folded in as the Director's brief
directs, and extended beyond the ask with the closed-form onset criterion (C2) and
the duration scan (C3) that Red Team's own Amendment-3 tempering has been asking
for since Iteration 15.

**Also not addressed this cycle, disclosed:** T21's contamination-risk re-score
(Block A partially answers it — see P-TH23-A1/A7 — but a full re-score needs the
partial-coherence bridge, blocked on idealization 3's missing sourced figures);
PHOTONICS' R3 recheck of exp-044's 0.45% achromatic claim; the settling-margin
FDTD test (fourth consecutive deferral, idealization 10); `realizability_tier`
de-duplication (Tier 3 housekeeping — Block C imports exp-038's copy rather than
making a third).
