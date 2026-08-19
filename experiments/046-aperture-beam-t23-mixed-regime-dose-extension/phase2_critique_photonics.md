# PHASE 2 — CRITIQUE · PHOTONICS (blind) · Panel Iteration 23 · exp-046

*Every number below was re-derived from the cited repo file in this session
(pure `math`; no numpy on this box). Nothing is taken on the proposal's word.*

## Steel-man (≤150 words)

Blocks B and C survive independent re-derivation exactly. From
`experiments/045-.../run.py:101-107,194-196,213-215` I reproduce the mixed
regime to every printed digit: h_eff 11111.111111, area 5.4756000e-12,
mass 2.9854066e-14, dP/dT 6.0868159e-08, P_abs 2.0044348e-12, dt_ss_full
3.2930761e-05 K, τ_th 3.4332969e-04 s, dwell/τ 194.176815, Bi 1.7567568e-04,
Kn 2.807692e-02, slip −5.3168%, NETD_lo/ΔT 607.3, Wien 9.885 µm, and
(w_on/r_out)² = 9.151923077316. The "τ_th is independent of L_power"
argument is algebraically right and genuinely settles T23's operative
question. Block C's closed form ratio_∞ = 1/(1−a·f) reproduces exp-045's
eight committed Host-D points (1.0034714 vs 1.0034714; 1.4522287 vs
1.4509044). `profile="gauss"` really is never exercised anywhere
(grep-confirmed), and stage 16's absolute anchor — exp-041's
−0.010964794540566314, `results.json:206` — is the right kind of gate.

## Sharpest attack (≤150 words)

§2.1's `w_y = w₀√(1+(z_eff/z_R)²)/cos θ₀` misplaces the obliquity.
`lab/fdtd2d.py:152-155` imposes `exp(−((yy−yc)/width)²)` **along y at the
source plane**; `:158-161` adds only a phase ramp. So `width` is the
y-extent; the waist perpendicular to the tilted axis is w₀·cos θ₀, and a
plane parallel to the source sees **w₀, unstretched**, at short range.
Exact angular-spectrum propagation of that exact aperture over `D_SP`=223
gives 1/e² half-width **162** cells at 450 nm/36°/FWHM 2° (table says
199.33) and **217** at 600 nm/40°/FWHM 2° (table says 280.54). The correct
stretch is 1/cos³θ₀. Reduced through `lab.ambient.window_means`/`weber`,
the exact profile departs from the proposal's envelope model by **>10% at
13 of 36 cells**, with sign flips at 750 nm/38° and 750 nm/40° — firing
P-TH23-A2's own falsification clause (">6 cells exceed 10%") before any run,
and A3's (">4 … exceed 3%") at 16 cells.

## Verdict

**Support-with-changes.** The FDTD legs, the stage-16 gates, and Blocks B
and C are worth running exactly as specified. Block A's *analytic* envelope
model — the sole basis of every committed Block-A band — is wrong and must
not be committed to git in its present form.

## Flip (single change)

Replace §2.1's obliquity bookkeeping with the tilted-angular-spectrum form
and re-derive P-TH23-A2/A3/A5/A7's bands from it:

> w_y(z) = w₀·√(1 + (`D_SP`/(z_R·cos³θ₀))²)  — propagation distance `D_SP`,
> not `D_SP`/cos θ₀, and cos³ not cos¹.

If the FWHM column headers are to mean the *emitted* single-mode divergence,
also correct the waist to **w₀ = 0.3747808·λ_cells/(Δθ_rad·cos θ₀)** (24–31%
larger at θ₀ = 36–40°), because an aperture of y-extent w₀ launched at θ₀
has perpendicular waist w₀cos θ₀ and therefore divergence Δθ/cos θ₀.

---

## Supporting arithmetic and verification ledger

### Verified correct (no change needed)

| Claim | Check |
|---|---|
| `NX/NY/ABSORB/TAPER/SRC_X/PLANE_X/R_OUT/GUARD_OUT/W_FLANK/CPL/STEPS/COURANT_FRAC/OBJ_Y/D_SP/Y_LO/Y_HI` at `042-.../design_geometry.py:119-136` | all 16 line cites exact |
| `C_THR`=0.005 at `042-.../run.py:41`; grid at `:89-91` | exact |
| windows \|y−792\|≤78, 185≤\|y−792\|≤263 (`lab/ambient.py:42-50`) | exact |
| `SIGMA_SPONGE` = 0.10/(2·78) = 6.41025641025641e-4, `041-.../design_geometry.py:140-141` | exact |
| C = 2√(2 ln 2)/(2π) = 0.37478125…; w₀ = C·λ_c/Δθ; FWHM/(1/e² half-angle)=√(2 ln 2) | derivation correct |
| all 12 w₀, 2w₀, 1504/(2w₀), z_R, z_eff/z_R, N_F values | reproduce exactly |
| full-aperture N_F at 40° = 518.03/388.52/310.82 | exact |
| walk = 223·tan(36/38/40°) = 162.02/174.23/187.12; y_c,aim = 629.98/617.77/604.88 | exact |
| unaimed rim residual exp(−(752/268.42)²) = 3.892e-4 → 1.51e-7 intensity | exact |
| exp-042 worst incoherent cell −0.004006497 (750/38°/2°) | exact |
| exp-041 C_empty(+40°,600) = −0.010964794540566314; C_sponge = −0.05815337265493213 | exact |
| cost: 91.607 s / 30 runs = 3.05 s per run | exact |
| Block B: all three regime columns (see steel-man) | exact |
| Block C tiers: 6 PUBLISHED + 6 PLAUSIBLE per `038-.../run.py:31-45` | exact |
| Block C τ_k, dwell/τ_k, 2496 = 4·4·6·2·13, 416 new points | exact |
| C3 max decoupled ΔT = 3.2930761e-5 × (0.1/1.1) = 2.99371e-6 K, margin 6680.5× | exact |
| B6 saturation 1 − 5.982999e-10 at 21.24×; e^−194.18 ≈ 10^−84.3 | exact |
| A4 replica spacing λ/δθ = 343.8/458.4/573.0 (δθ = FWHM/8), 687–5730 at FWHM≤10; 526-cell span | exact |
| `N_TRANSIENT_TAU`=25.0 `lab/kinetics.py:97`; `:131-133`, `:156`; `pulse_train_segments` `:201-219` | exact |
| Amendment 3 quote, `034-.../REALIZABILITY_MEMO.md:101-108` | exact (path elided in proposal) |
| stage 16 is the next free stage number (`run_all.py` has 1–15); 41/41 fast stages matches exp-045 NOTES:223 | exact |

### The envelope-model defect, in numbers

Exact scalar angular-spectrum propagation of `E(y)=exp(−y²/w₀²)·exp(i k sinθ₀ y)`
over Δx = `D_SP` = 223 (non-paraxial k_x = √(k²−k_y²), evanescent clipped),
reduced through the same object/flank windows and Weber formula:

| λ/θ₀/FWHM | C, exact propagation | C, proposal's envelope | C_coherent (exp-042) |
|---|---|---|---|
| 450/36/2 | −0.4775 | −0.2430 | −0.2432 |
| 450/40/2 | −0.7380 | −0.4705 | −0.4709 |
| 600/38/2 | −0.3133 | −0.0299 | −0.0296 |
| 600/40/2 | −0.4465 | −0.1210 | −0.1208 |
| 750/38/2 | **−0.0485** | **+0.1656** | +0.1662 |
| 750/40/2 | **−0.1741** | **+0.0956** | +0.0961 |
| 750/36/5 | −0.7874 | −0.6416 | −0.6476 |
| 750/38/5 | −0.8834 | −0.7534 | −0.7588 |
| 600/40/10 | −0.9966 | −0.9937 | −0.9980 |

All nine FWHM=2° cells and four FWHM=5° cells exceed the 10% band; two flip
sign. Peak position is fine (exact propagation puts the peak at
`OBJ_Y`+`D_SP`tan θ₀ to ≤1 cell) — it is only the **width** that is wrong,
and it is wrong in *both* limits: 23–30% too large where z ≪ z_R (FWHM 2°,
5°) and ~1/cos θ₀ too small where z ≫ z_R (FWHM 20°, where the saturated
\|C\|→1 hides it). A θ₀=0 control reproduces w(z)=w₀√(1+(z/z_R)²) to 1%,
confirming the propagator, not the check, is sound.

### Four further verified defects (each smaller, all concrete)

1. **A wrong-row transcription in §2.1.** The "w_y at θ₀=40°" column reads
   **199.33** for 450 nm/FWHM 2°. 199.33 is that formula's **θ₀=36°** value;
   the θ₀=40° value is **210.54**. Every other cell in the column is the
   correct θ₀=40° value, so this is a paste error, not a convention.
2. **P-TH23-A3's cell counts are wrong.** The grid is 3λ × 3θ₀ × 4 FWHM
   (`042-.../run.py:89-91`), so FWHM≤10° is **27** cells and FWHM=20° is
   **9** — not the "24" and "12" the prediction commits to. The counts are
   the denominators of a pre-registered pass/fail band, so this is
   load-bearing, not cosmetic. (24+12 sums to 36 only because the FWHM axis
   was treated as having three values, not four.)
3. **P-TH23-A1 is decided by geometry, not by coherence.** With the beam
   unaimed, the axis lands at 792 + 162…187, while the object window is only
   ±78 wide — the object window is simply not illuminated, at all 36 cells.
   I get 36/36 above `C_THR` and 35/36 above the 20× clause straight out of
   the proposal's *own already-computed* envelope model, whose span
   (\|C\| = 2.99e-2 … 9.98e-1) I reproduce to four figures. So §4's claim
   that Block A's bands were "deliberately kept as a prediction rather than
   pre-computing the answer" does not hold for A1 or A3: A3's committed
   bands (≤3% at FWHM≤10, 5–20% at FWHM=20) are exactly the residuals of an
   envelope-vs-`C_coherent` comparison that the proposal already had in hand
   (I get 0.1–2.8% and 5.3–14.2%). Retrodiction labelled as prediction.
   Separately, exp-042's incoherent column is not merely "incoherent" — it
   divides each angular component by *its own* flank mean
   (`lab/ambient.py:58-70`), a normalization a single-angle reading cannot
   have. The coherent/incoherent split A1 claims to adjudicate is therefore
   partly a reduction artifact, and a one-angle beam lands on the "coherent"
   side by construction of the estimator.
4. **Two small internal inconsistencies.** §1 quotes the new Fresnel range
   as "0.32–40.7" while §2.1's own table gives 0.24–39.6 (0.32/40.7 are the
   FDTD-leg values only). Idealization 2's "at FWHM=20° the waist is only
   1.07–1.34 λ" cannot be right: w₀/λ_cells = C/Δθ_rad is λ-independent by
   construction — it is **1.074 λ at all three wavelengths**. (Relatedly:
   because w₀/λ is fixed by Δθ alone, Block A's 3-λ sweep carries no
   material wavelength dependence beyond the fixed cell geometry — worth
   stating rather than presenting it as a λ-sweep result.) Idealization 2's
   "≤1.5%" paraxial error is conservative; I get 0.52% at FWHM=20°.
   C5's quoted agreement floor "2.6e-7" is also off — the 5τ points agree
   with the closed form to ~2e-15, not 3e-7; the ≤0.2% band still holds.
   C6's stated 5τ supremum 1.006784 is the r≪1 value; at r=1e-1,
   f = e^(−5/1.1) gives sup **1.010711**, and the 0.5τ threshold there is
   ln(21·e^(−0.4545)) = **2.590**, at the very edge of the committed
   2.54±0.05.

### What I am *not* attacking

The choice of the Gaussian relation over the single-slit relation is right,
and reason 2 in §2.1 is correct as stated: `p = exp(−((y−yc)/width)²)` on
the field with a \|E\|²-based observable does make `width` the waist w₀
under the standard amplitude-1/e = intensity-1/e² convention. The
truncation numbers are right. The T23 structural argument is right. My
attack is entirely about what happens to that waist when the source is
tilted by 36–40°, which is exactly the axis this seat owns.
