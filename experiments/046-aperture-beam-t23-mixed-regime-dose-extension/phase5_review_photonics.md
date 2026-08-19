# PHASE 5 — REVIEW · PHOTONICS (fresh context, blind) · Panel Iteration 23 · exp-046

*Charter: surface interaction, absorption spectra, angular dependence, scattering
cross-sections. Owns: is the proposal's optical response coherent as stated,
across wavelength and angle?*

*Method, per this program's Phase-5 culture: every number below was re-derived
from `run.py`, `results.json`, `lab/`, and `experiments/042-.../design_geometry.py`
in this session — including one independent FDTD re-run and one independent
trust-suite stage execution. Nothing is taken from NOTES.md's prose. Scripts are
in this session's scratchpad; every check is a ≤40-line reproduction.*

---

## 1. Reading — what I verified, and how

### 1.1 What reproduces exactly (no change needed)

| Claim | My independent check | Result |
|---|---|---|
| S16-b FDTD leg | fresh `Sim(360,1584,cpl=20,courant 0.99)`, `profile="gauss"`, width 40, θ₀=40°, 1400 steps, `observer_profile` at `PLANE_X` | centre **992.092662**, half-width **90.988099** — bit-identical to `results.json` (14.5 s). The determinism claim holds against a *third* execution, in a fresh process. |
| Stage 16 | `python3 lab/validation/run_all.py --only 16` | **4/4 PASS, 76 s.** S16-a 1.06%, S16-c 6.96×10⁻¹⁵ relative, S16-d 1.25%. |
| `--only` selector fix (Learned #5) | re-implemented `_stage_selected` and ran all five historically-cited tokens | `12346789,10,11,12,13,14,15` → {1,2,3,4,6,7,8,9,10..15} (no 5, no false 12); `16` → {16}; `5` → {5}. **Fix is correct.** |
| A0 | recomputed `C = 2√(2ln2)/2π` and all 12 θ₀=40° geometry rows | 0.37478125; aperture ratio span **[2.1462, 35.769]** ✓ |
| A2 | recomputed envelope-vs-propagator deviations over 36 cells | worst **11.977%**, median **1.1426%**, 26/36 ≤5% ✓ |
| A3 identity | derived analytically *and* re-implemented `\|Σ√wᵢ e^{ik sinθᵢY}\|` from scratch | 1/e half-width = `w₀/cosθ₀` exactly in the paraxial limit (∫e^{−u²/4σ²}e^{ikcosθ₀uY}du ⇒ Y_e = 1/(k cosθ₀ σ) = 0.374781λ/(Δθ cosθ₀)); measured **0.0225–0.781%** (FWHM≤10°) and **2.605–3.252%** (FWHM=20°) — reproduces the committed numbers to 4 s.f. |
| `w_y` slip | recomputed both | 199.33 = `w_y(450nm, FWHM2, θ₀=**36°**)`; θ₀=40° value = **210.538**. PHOTONICS' Phase-2 catch and Red Team's Attack-1c ruling (keep the formula, fix the source width) are both correct: with `w_line = w₀/cosθ₀` the perpendicular waist is `w₀`, axial distance is `D_SP/cosθ₀`, and the y-projection restores the printed `/cosθ₀`. |
| Aperture truncation (idealization 4) | exp(−(752/350.395)²) at the widest cell | **9.9918×10⁻³** amplitude, 9.984×10⁻⁵ intensity; 25.6×/657× worse than Phase 1 ✓; 5 aimed cells flagged invalid ✓ |
| **Block B, every number** | recomputed from first principles (`h=k_air/L`, `A=L²`, `m=ρL³`, `dP/dT=A(4εσT³+h)`, `P=I·ratio·w_on²`) | `dt_ss_full` **3.293076054169134×10⁻⁵ K**, τ_th **3.4332969490950116×10⁻⁴ s**, `dwell/τ` **194.17681504141214**, (w_on/r_out)² **9.151923077316**, NETD_lo/ΔT **607.335**, Wien **9.8849 µm** — identical to 15+ digits. The "τ_thermal is independent of L_power" algebra is right and does settle T23's operative question. |
| **Block C** | recounted from the 42 point-runs | 21 new points / 42 runs; 12 with memory, 7 above 1.05, **all** at Host D r=1.0 or Host E; **0/12 PUBLISHED**, 7/18 UNOBTANIUM; max ΔT **1.64654×10⁻⁵ K**, margin **1214.7×** ✓ |

Blocks B and C are clean. I found nothing wrong with either. The rest of this
review is Block A, which is my charter.

### 1.2 The S16-b diagnosis is right in direction and wrong in its numbers — because it uses the wrong propagator AND the wrong observable

This is the finding I would defend hardest.

`run.py::exact_angular_spectrum_center` (and the identical `exact_center` now
shipped inside `lab/validation/run_all.py::stage16_oblique_gaussian_source`)
propagates `exp(−(y/w)²)·exp(ik sinθ₀y)` with `exp(i k_x z)` and reads `|E|²`.
That is the **fixed-field-screen** recipe — the same class of error this program
already caught once, at Iteration 19's own erratum (obliquity-on-E for a soft
additive current source). `lab/fdtd2d.py:231-237` adds to `Ez` each step: this is
an impressed **line-current sheet**, whose radiated field carries a **1/k_x**
factor in the angular spectrum, and whose measured profile is `observer_profile`
= a **flux** (`-flux_profile_x`), not `|E|²`. exp-042's own `_G0_for` propagator
— *the propagator this cycle exists to validate* — is the correct
current-source Green's function (`exp(i(kr−π/4))/√r`, the Hankel far-field
asymptotic) reduced as `Sx = −Re(E H*)`.

I computed all four convention combinations at S16-b's exact configuration
(600 nm, θ₀=40°, width 40, z=`D_SP`=223, n_fft up to 2²², converged to ±0.01 cell):

| reference | 1/e² centre | half-width |
|---|---|---|
| field-aperture, \|E\|²  — **the one committed** | 987.14 | 89.10 |
| field-aperture, flux | 983.04 | 86.86 |
| current-source (1/k_x), \|E\|² | 996.74 | 94.62 |
| **current-source (1/k_x), flux — the physically correct one** | **991.670** | **91.573** |
| **exp-042's own `_G0_for` Huygens sum, same aperture** | **991.645** | **91.576** |
| **FDTD (my own re-run)** | **992.093** | **90.988** |
| ray-optics target the gate scores | 979.119 | — |

The two independent correct formulations agree with each other to **0.03 cells**
and with FDTD to **0.42 cells (0.46% of the beam half-width)**. The committed
comparator is the only one of the four that is wrong on *both* axes.

**Corrected attribution of the 12.97-cell gate failure:**

* target error (ray optics vs the correct exact answer): **12.55 cells — 96.8%**
* engine error (FDTD vs the correct exact answer): **0.42 cells — 3.2%**

versus NOTES.md's committed **8.03 / 4.95** (62% / 38%). The engine is **12×
better** than the cycle reports, and the target is **56% worse**.

**And the dominant cause is not non-paraxiality.** Under a *peak* estimator the
correct exact answer sits at **976.56** (FDTD peak-cell 977.0; `_G0_for` peak 977)
— only **2.56 cells** from ray optics. Ray optics predicts a stationary-phase
ray, i.e. the profile **peak**; the gate estimator is the 1/e²-crossing
**midpoint** of a profile that is strongly skewed toward +y. So the 12.97-cell
failure decomposes as ≈**10.4 cells estimator/skew mismatch**, ≈**2.6 cells
genuine non-paraxial target error**, ≈**0.4 cells engine**. NOTES.md's Learned #2
("S16-b's ray-optics target is 8.0 cells off the exact non-paraxial answer") and
idealization 2's "this idealization has now bitten" both name the right *species*
of cause but attribute ~4× too much of the effect to it, and none of it to the
estimator pairing that actually dominates.

**The consequence that matters more than the NOTES text.** The first-light
amendment is now *shipped in the trust suite*: stage 16 gate b permanently scores
the engine against 987.14, in units of half-width, with an **8% bar calibrated on
the 5.44% residual that the wrong comparator produces**. The engine's true
pointing accuracy at this configuration is **0.46%**. The gate as shipped is
~17× looser than the engine warrants and would not fire on a genuine pointing
regression of up to ~7 cells. A gate calibrated against a wrong reference is a
worse defect than a wrong sentence in NOTES.md, because it is forward-looking and
nobody re-derives a green gate.

### 1.3 A5 — the cycle's headline — is carried by 2 of its 4 legs

`P-TH23-A5` is scored on the Weber contrast `C_empty`, which is **bounded below
by −1**. At two of the four legs the reading is already saturated there:

| leg | N_F | C (desk) | max attainable deviation toward C=−1 | pre-registered band |
|---|---|---|---|---|
| A-v1 | 53.98 | −0.12334 | 710.7% | ±15% |
| **A-v2** | **2.16** | **−0.996664** | **0.335%** | **±15%** |
| **A-v3** | **0.54** | **−0.986618** | **1.356%** | **±35%** |
| A-v4 | 65.60 | +0.163673 | 711.0% | ±15% |

At A-v2 and A-v3 the band is *unreachable by construction* in the negative
direction. In the positive direction I scanned the propagator's own width
parameter through `prop_c_empty`:

| leg | width ×1.5 | ×2 | ×3 | ×5 | ×0.5 |
|---|---|---|---|---|---|
| A-v2 (band ±15%) | 1.42% | 6.51% | 29.5% ✗ | 87.6% ✗ | 1.01% |
| A-v3 (band ±35%) | 1.07% | 1.02% | 0.42% | 15.4% | 29.5% |

**A propagator that got the beam width wrong by a factor of 5 (A-v3) or 2
(A-v2) would still pass.** A realistic 10% propagator error moves C by
0.06–0.11% (A-v2) and 0.52–1.00% (A-v3), against 85–103% (A-v1) and 29–49%
(A-v4). So NOTES.md's "**This is the result of the cycle**, and it is the only
Block-A prediction that could have failed on evidence rather than on algebra" is
right about the other predictions and **half-right about A5**: two of its four
legs could not have failed either.

Two further problems with the framing:

* **N_F is not this propagator's controlling validity parameter.** `_G0_for` is a
  full cylindrical-wave Huygens sum; its only approximations are the Hankel
  far-field asymptotic (`design_geometry.py` asserts `kr > 50`, and `r` is set by
  `D_SP` and the window span, *not* by the aperture width), scalar 2-D, and
  one-way propagation. Narrowing the source aperture changes N_F by three orders
  and changes `kr` by nothing. "A desk propagator can be validated three orders of
  Fresnel number outside where it was built" (Learned #1) reads as if the
  propagator's trust region were Fresnel-number-bounded. It never was. The
  defensible statement is narrower: *the far-field-spreading limit is now
  exercised, and the two legs that could discriminate (N_F 53.98 and 65.60) agree
  to 1.91% and 5.68%.*
* **The band rule runs backwards.** `run.py:382` sets `35% if N_F < 1 else 15%` —
  looser bands where the propagator is least trusted, which is exactly where the
  observable is least sensitive. The two effects compound instead of cancelling.

### 1.4 Idealization 2's "consequently" is a non sequitur, and the λ data says so loudly

Committed (docket 12, adopted at Phase 3, restated in NOTES idealization 2 and in
`results.json`): *"w₀/λ = C/Δθ is LAMBDA-INDEPENDENT … **Consequently** Block A's
3-λ sweep carries NO material wavelength dependence beyond fixed cell geometry."*

`w₀/λ` is indeed λ-independent (1.0737 λ at FWHM=20°, one value — the Phase-1
"1.07–1.34 λ" was wrong and the correction is right). But the conclusion does not
follow, because `D_SP`, `R_OUT`, `GUARD_OUT`, `W_FLANK` and the aperture are fixed
in **cells**, not in λ. So `N_F ∝ λ_cells` exactly, and the reading is strongly
chromatic. From `results.json`'s own 36 cells:

| θ₀ | FWHM | C(450) | C(600) | C(750) | rel. spread |
|---|---|---|---|---|---|
| 36° | 2° | −0.24576 | **+0.07625** | **+0.24362** | 1981% (sign flip) |
| 38° | 2° | −0.37331 | −0.03227 | **+0.16367** | 666% (sign flip) |
| 40° | 2° | −0.47266 | −0.12334 | **+0.09368** | 338% (sign flip) |
| 40° | 5° | −0.98581 | −0.93181 | −0.83277 | 16.7% |
| 40° | 20° | −0.98995 | −0.98662 | −0.98195 | 0.8% |

Wavelength is the **largest single lever in the entire Block-A grid**, larger
than θ₀ and larger than FWHM at FWHM=2°, and it flips the sign of the observable
at three of nine (θ₀,FWHM=2°) cells. The medium is genuinely dispersionless
(σ≡0, ε_r≡1) and the emitter is λ-scale-invariant — that part is true and worth
saying — but "no material wavelength dependence beyond fixed cell geometry, and
should not be read as a wavelength result" is precisely the kind of achromatic
blanket that T7's chromatic-silhouette finding and PHOTONICS' still-outstanding
R3 recheck of exp-044's 0.45% achromatic claim exist to guard against. The
qualifier "beyond fixed cell geometry" carries the entire sentence, and a future
reader quoting the headline clause will be quoting something false about the
reading.

**Related, same data:** A1's own committed statement is *"the object window sits
in the beam's exponential wing while the +flank window sits under the beam, so
C → −1 regardless of coherence."* Four of the 36 cells read **positive** C (a
glint: the object window is *brighter* than the flanks), all at FWHM=2° and
600/750 nm. The `|C| > C_THR` band is blind to this because it takes an absolute
value. The stated mechanism is contradicted by its own grid at those cells.

### 1.5 A3's FWHM=20° residual is mis-attributed

`results.json`'s A3 band reads *"≤4% at all 9 FWHM=20° cells **(taper
truncation)**"*. It cannot be taper truncation: at FWHM=20° the synthesised
aperture is 19.9–35.0 cells wide, sitting deep inside a 1504-cell aperture whose
raised-cosine taper occupies the outer 40 cells at |Y|≈752. I re-ran the same
41-point sum with `sinθᵢ` replaced by the paraxial mapping
`sinθ₀ + cosθ₀·(θᵢ−θ₀)`:

| λ/θ₀ | deviation, sin mapping | deviation, paraxial mapping |
|---|---|---|
| 450/40° | 3.252% | **0.000%** |
| 600/40° | 3.231% | −0.000% |
| 750/36° | 2.605% | 0.004% |

The residual is **entirely** the sinθ-vs-θ nonlinearity over the ±2.5·FWHM = ±50°
angular span (which reaches θ = 90° at θ₀=40°), not truncation. That is the *same*
physics the cycle correctly identifies for S16-b — mis-attributed two keys away
in the same `results.json`.

### 1.6 Smaller, verified

* **S16-d has S16-b's disease in miniature.** Its target is the closed form
  `w_y = 79.4747`; the correct exact propagation gives **81.05** and FDTD gives
  80.47. So the gate's measured "1.25% engine error" is mostly the *target's* own
  ~2.0% paraxial error — the engine is 0.72% from exact. The gate passes for the
  wrong reason, and its 5% bar is measuring the closed form, not the solver.
* **Idealization 4's C_THR sentence.** "Unaimed rim residual is 9.99×10⁻³ in
  amplitude / 9.98×10⁻⁵ in intensity … still below `C_THR`=0.005" — the
  *amplitude* is **above** 0.005; only the intensity is below. And comparing a
  source-plane field residual against a Weber contrast threshold is a category
  error in either direction: the right figure of merit is the ΔC the truncation
  rim induces at the scored windows (which I estimate at ~10⁻⁴, two orders below
  the T21 fringe amplitudes this thread is about — the conclusion survives, by two
  orders, not four).
* **The A5 residuals, normalised for sensitivity, single out 750 nm.** Converting
  each leg's C residual through its own measured dC/dw: A-v1's 1.91% ≈ **0.20%**
  width-equivalent; A-v4's 5.68% ≈ **1.47%** width-equivalent — **7.3× worse at
  750 nm**. Since 750 nm runs the *finer* grid (cpl 25 vs 20), Yee numerical
  dispersion runs the wrong way and is disfavoured; the λ-dependent causal
  settling margin (7.8 vs 9.8 post-transit periods) is the leading candidate.
  That is idealization 11's own disclosed confound, now with a number attached —
  and the fifth consecutive cycle in which the test is not run.

### 1.7 The A1 "withheld as gate-backed" disposition

**Defensible, conservative, and it hides nothing** — but it is the wrong shape of
answer, in both directions.

It hides nothing: A1 is a pure desk computation over 36 cells, and its content
is a geometric near-certainty. The beam walks 162–187 cells while the object
window is ±78 cells; the pointing error would have to be ~100 cells, not 13, to
move `n_above_C_THR` off 36/36. min|C| = 0.03227 is 6.5× `C_THR`. The Director
states the judgment explicitly and offers the reader the stricter reading — that
is the honest form, and it is a better disposition than the "reinterpreted after
the fact" pattern LOGBOOK records at Iteration 1's P1b.

But it is over-conservative in one direction and over-generous in the other.
Over-conservative: once the gate's target is corrected (§1.2), the pointing chain
is validated to **0.42 cells** and A1 is fully backed. Over-generous: labelling
it *"PARTIAL (computed in band; withheld as gate-backed)"* presents an algebraic
near-certainty as a measurement awaiting a gate. A1 was the proposal's advertised
headline; it was re-scoped at Phase 3 from a coherence adjudication to a pointing
reading (docket 5) and then withheld at Phase 4. Each step is individually
justified and NOTES discloses the arc ("The headline the proposal advertised was
never an experimental question"). The clean resolution is to restore it as an
explicitly-labelled **desk geometry reading**, not to leave it in limbo.

---

## 2. Physical meaning for the program

1. **The illumination model is now correct where it matters, and better than the
   cycle claims.** `width = w₀/cosθ₀` is right, `w_y` is its right partner, and
   the engine reproduces a genuinely non-paraxial 40°-tilted Gaussian to <0.5% in
   both centroid and width. That is real instrument progress for T21, and it is
   understated, not overstated, in the record.
2. **The propagator's trust region is set by `kr`, not by N_F.** For every future
   T21/T15-family desk calculation this matters: `_G0_for` may be used at any
   aperture width at this standoff, and may **not** be assumed valid at a
   *shorter* standoff, no matter how large the aperture. This cycle's evidence
   licenses the first and says nothing about the second — the opposite of what
   "validated three orders of Fresnel number outside where it was built" suggests.
3. **T21's contamination-risk question is chromatic, and this grid says so.** The
   illumination model's own reading flips sign with λ at FWHM=2°, with 750 nm
   reading a **positive** contrast (a glint at the object window) where 450 nm
   reads a silhouette. T21's worst cell has been 750 nm since Iteration 19. Any
   future contamination re-score that inherits idealization 2's "no wavelength
   dependence" framing will be wrong at exactly the wavelength that has been the
   problem all along.
4. **The `sinθ` nonlinearity is now this bench's recurring angular hazard.** It
   broke S16-b's target, it sets A3's FWHM=20° residual, and it is why `±2.5·FWHM`
   angle sets reach θ=90° at FWHM=20°. Any future angular-spectrum construction on
   this bench (N33 quadrature, the Gaussian Schell-model partial-coherence bridge
   T21 has pre-registered) needs the paraxial-vs-`sinθ` distinction stated up
   front, or it will re-inherit both errors.
5. **Blocks B and C stand.** T23's operative question is settled correctly: the
   conduction length alone decides `dwell/τ_thermal`; the mixed regime is the least
   comfortable of the three (607× below NETD_lo) and still UNDETECTABLE. Block C's
   `D/τ_k < ln(21f)` criterion is a genuine one-number replacement for Amendment
   3's host list, and its PUBLISHED-tier zero is exact, not small. Neither block
   touches T1.

---

## 3. Argued next change (one concrete item)

**Replace stage-16 gate b's reference propagation, re-band it against the engine's
actual accuracy, and file a flag-don't-rewrite erratum on the S16-b diagnosis —
before any further Block-A number or T21 propagator claim is cited.** Zero new
FDTD cost beyond stage 16's existing four calls.

Four changes, each verified here:

1. **`lab/validation/run_all.py::stage16_oblique_gaussian_source::exact_center`
   and `run.py::exact_angular_spectrum_center`** — two lines: divide the
   propagated angular spectrum by `k_x` (line-current Green's function, matching
   `lab/fdtd2d.py:231-237`'s additive-`Ez` source), and reduce with
   `Sx = Re(E·conj(H))`, `H = F⁻¹[(k_x/k)·Ê]` (matching
   `ambient.observer_profile`, which is a flux). Acceptance test, free: the
   corrected function must reproduce exp-042's own `_G0_for` Huygens sum for the
   identical aperture — measured here at **991.670 vs 991.645 (0.03 cells)** and
   **91.573 vs 91.576 half-width**.
2. **Re-band gate b at ≤1.5% of the beam half-width** (measured 0.46%; 3× margin,
   stage 10's own calibration convention), replacing the shipped 8% bar which was
   calibrated on the wrong comparator's own error.
3. **Add a peak-estimator `[info]` line** so the ray-optics comparison is made
   against the estimator ray optics actually predicts (exact peak 976.56 vs
   ray-optics 979.12 = 2.56 cells; the estimator pairing, not non-paraxiality,
   is ~80% of the original failure).
4. **Erratum, not rewrite** (T10/Iteration-19 precedent): NOTES.md's 8.03/4.95
   split, Learned #2's "8.0 cells", and idealization 2's "this idealization has
   now bitten" get a flag pointing to the corrected 12.55/0.42 split and the
   estimator-mismatch attribution. `results.json` gains a `phase5_erratum` key
   the way exp-042's did.

**Companion, same change-set, also zero FDTD:** re-score A5's two low-N_F legs on
a non-saturating observable. The 1/e² **half-width and centroid** at `PLANE_X`
stay linear in propagator error where Weber `C` saturates; A-v2's are already in
`results.json` (80.471 / 984.951 vs propagator 81.051 / 984.688 — 0.72% and 0.26
cells, a *real* agreement), and A-v3's come free from the stored profile. That
converts two structurally-unfalsifiable legs into two informative ones and lets
the "validated at N_F = 0.54–65.6" claim be stated at a strength the data
supports.

---

## 4. Ranked top-3 candidate directions for Iteration 24

*(All three are zero-to-low FDTD cost and none competes with VISION's
glare/adaptation Tier-W sidecar, which by the Director's own hardened item-24
rule fires Checkpoint criterion 4 automatically if Iteration 24 closes without
it. That item outranks all three of mine on program-integrity grounds; these are
what I argue for on top of it.)*

1. **Stage-16 gate-b reference fix + re-band + A5 low-N_F re-score on a
   non-saturating observable** (§3). This is a live defect in a *shipped trust
   gate*, and it is the only item on this list whose cost is essentially zero and
   whose absence silently degrades every future measurement on this bench. It also
   converts the cycle's own headline from half-supported to fully supported, and
   restores A1 from limbo.
2. **The λ-audit of Block A's grid, and an R3 check on the positive-C cells.**
   Restate idealization 2 to what the data supports (dispersionless medium and
   λ-invariant emitter; strongly chromatic *reading*, N_F ∝ λ_cells, sign flip at
   FWHM=2°), and run this program's own mandatory R3 resolution check
   (cpl×1.5 at all 3λ) on the four positive-C cells **before** "glint at 750 nm"
   is allowed to enter the record as physics rather than as a window-geometry
   artifact. R3's meta-rule is explicit that a surprising feature gets the check
   before the mechanism debate — and a sign reversal across the visible band, on
   the exact axis T21's worst cell lives on, is a surprising feature. Zero new
   engine code; ~6 desk propagations plus 6 FDTD legs if the check is run in the
   solver too.
3. **The settling-margin FDTD test — fifth deferral, now with a quantitative
   hook.** Re-run A-v1 (600 nm) and A-v4 (750 nm) at `STEPS` = 2800 and re-score
   against the same desk propagator. Falsifiable: if settling drives it, A-v4's
   5.68% should fall toward A-v1's sensitivity-normalised ~0.2% level while A-v1
   moves ≤0.3pp; if both are unchanged, settling is refuted and the 7.3×
   sensitivity-normalised asymmetry becomes a real, unexplained λ-dependent
   propagator/engine discrepancy that PHOTONICS should own. Two FDTD calls, ~30 s.

---

## 5. Verdict

**PARTIAL.**

Blocks B and C are clean, fully reproducible, and settle what they set out to
settle. Block A delivered real instrument progress — `profile="gauss"` is
trust-gated for the first time, the oblique source-width convention is fixed and
gated, and the engine's non-paraxial behaviour is in fact *better* than the cycle
records. Against that: the cycle's genuinely falsifiable content is two FDTD legs,
not four, because the scored observable saturates at C = −1 at exactly the two low
Fresnel numbers the headline advertises; the one gate that failed is diagnosed
with a comparator that uses the wrong Green's function and the wrong observable,
splitting the blame 62/38 between target and engine where the correct split is
97/3; that wrong comparator is now shipped as a standing trust-suite gate with a
bar ~17× looser than the engine warrants; and the adopted "no material wavelength
dependence" idealization is contradicted by the cycle's own grid, which flips the
sign of the observable across the visible band.

Not RULED OUT: nothing here is a dead mechanism, the direction is right, and
every defect I found is fixable at essentially zero cost with code that already
exists in this repo. Not PROMISING: a green gate calibrated against a wrong
reference is exactly the class of defect this program's Phase-5 culture exists to
catch, and it would have propagated silently into every future run of stage 16.
