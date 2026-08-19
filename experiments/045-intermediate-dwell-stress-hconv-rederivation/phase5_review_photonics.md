# Phase 5 review — PHOTONICS (fresh context)

**Panel Iteration 22 · exp-045 · "The Intermediate-Dwell Coupled
Kinetics-Thermal Stress Sweep + h_conv/mass_kg Re-derivation"**

Charge (PANEL.md seat 1): is the proposal's optical response coherent as
stated, across wavelength and angle? This cycle is pure analytic/desk work
(zero FDTD calls) so "angle" does not apply — nothing in Block A/B/C touches
angular scattering. Wavelength does apply, because Block B newly promotes a
600nm-only optical measurement (`SIGMA_EXT_ON`) into a physical length scale
for heat conduction and thermal mass, for the first time in this program's
history. That is where I spent most of this review, after first
independently re-deriving the headline chain by hand.

## 1. Independent re-derivation (hand/script, not copied from NOTES.md)

I rebuilt the relevant formulas from `run.py` from scratch in a bare Python
script (no import of `lab.thermo_sidecar`/`lab.kinetics`) and compared
against `results.json` to displayed precision. Everything below matched
exactly — **I found zero arithmetic errors anywhere in this cycle's
committed numbers.**

- **The w_on-consistent h_eff/τ_thermal chain (Block B, primary regime).**
  `w_on = SIGMA_EXT_ON·dx = 235.96673494878587×30nm = 7.079002µm`;
  `h_eff = k_air/w_on = 0.026/7.079002µm = 3672.83 W/(m²K)`;
  `mass = ρ_Si·w_on³ = 2330×(7.079µm)³ = 8.2656×10⁻¹³ kg`;
  `dp/dT = w_on²(4·0.9·σ_SB·293.15³ + h_eff) = 1.8431×10⁻⁷ W/K`;
  `τ_thermal = mass·C_p/(dp/dT) = 3.1392 ms`; `dwell/τ_thermal =
  66.7ms/3.1392ms = 21.237×`. All five figures reproduce `results.json`'s
  `length_scale_regimes.w_on_consistent` block to the displayed digit.
- **The T22 area-ratio table.** `geometric_disk = π·(78×30nm)² =
  1.72021×10⁻¹¹ m²`; `iso_xsec_sq,ON = (235.967×30nm)² = 5.01123×10⁻¹¹ m²`
  → ratio **2.91315×**; `iso_xsec_sq,absorber = (240.007×30nm)² =
  5.18432×10⁻¹¹ m²` → ratio **3.01377×**. Both match `results.json` exactly
  and both sit inside T22's own established 2.9–3.0× band.
- **A sample sweep point (Block A, `coupled_kinetics_thermal_dT`).**
  Host D, r=1e-1, uncorrected regime, axis K, R=0.68129207: `k_f=1.0,
  k_r=10.0, τ_k=1/11=0.090909s, dwell=R·τ_k=0.061936s`. Using the module's
  own bracket identity by hand: `exact_dT = 1.74329×10⁻⁴ K`,
  `decoupled_dT = 1.77119×10⁻⁴ K`, `relative_difference = 1.6006%` — matches
  the committed point exactly.
- **The monotone-ceiling structural argument (P-EM45-A1/attack 12).** I
  swept the bracket function `1 − (τ_k/(τ_k−τ_th))e^{−t/τ_k} +
  (τ_th/(τ_k−τ_th))e^{−t/τ_th}` numerically over τ_th/τ_k ratios spanning
  10⁻⁶–10⁶ and dwell spanning 4 decades either side of both time constants
  (≈40,000 grid points); the maximum value found anywhere was 1.0 to
  floating precision, never exceeded. The "cascade of two real-pole,
  non-oscillatory first-order relaxations cannot overshoot its own final
  ceiling" claim is not just asserted — it holds numerically everywhere I
  probed it.
- **Block C (dose-accumulation) — all 8 points.** I re-implemented the
  segment walk (`[ON(dwell_central), OFF(dt_gap)]×5 + ON`) independently
  using only the closed-form exponential relaxation, without importing
  `lab.kinetics`. All 8 `n_first`/`n_periodic`/`ratio` values reproduce
  `results.json` to 5+ significant figures (e.g. r=1e-1/0.5τ:
  n_first=0.047245, n_periodic=0.067911, ratio=1.4374 — matches). The
  `max_dT_periodic_decoupled_K=7.385×10⁻⁷K` also reproduces exactly
  (`dt_ss_full(w_on)×0.067911`).

This is a genuinely clean cycle on the numbers — five blind Phase-2 seats
plus Red Team already found the *conceptual* bugs (mixed length scales,
wrong material); nothing I checked independently turned up a residual
arithmetic defect in the corrected code.

## 2. The P-IT22-A2 PARTIAL miss — adequately characterized, not hiding
   anything larger

I traced the mechanism by hand rather than trusting NOTES.md's own
"artifact of the fixed R-grid" explanation. `host_d_witness_dwell_check`
(computed at the EXACT witness dwell, not the R-grid) gives r=1e-1 a true
relative difference of **1.4422%** — comfortably inside the predicted
[1.40%,1.55%] band. The R-grid's nearest point to r=1e-1's own
dwell/τ_kinetics ratio (0.7333) is R=0.68129 (Δ=0.052), which is
substantially further away than the same grid point is from the OTHER
three ratios' target ratio (≈0.6667, Δ=0.014) — because all four ratios
share one fixed, coarse 13-point log R-grid despite each having a slightly
different own dwell/τ_k. That asymmetry alone predicts exactly the observed
pattern: 3 of 4 ratios land inside the band, the fourth (whose true target
sits furthest from any grid point) overshoots by a small amount (1.60% vs
a 1.55% ceiling — a 3.2% relative overshoot of the band itself). I also
checked the neighboring grid point (R=1.0, rel_diff=0.90%) to make sure
there is no discontinuity or steepening being masked between them — there
isn't; the curve is smooth and monotonically decreasing through this
region exactly as the physics predicts. **Verdict: this PARTIAL is
honestly and correctly characterized. It does not hide a larger effect.**

## 3. Wavelength check — the cycle's one real, undisclosed gap (found here,
   confirmed harmless)

The task's own question: is reusing a single λ=600nm `SIGMA_EXT_ON`/
`RATIO_ON` pair throughout still licensed by exp-044's "achromatic
flatness" finding (P-IT21-C1, 0.45% relative spread), or does this cycle
quietly assume more than that finding covers?

**It assumes more, and nobody in this cycle's five-seat Phase-2 or the Red
Team audit caught it.** exp-044's Block C measured only the **ratio**
σ_abs/σ_ext (0.6056/0.6075/0.6083 at 450/600/750nm) for flatness — it never
checked `SIGMA_EXT_ON` itself, the absolute quantity. This cycle is the
*first* to use `SIGMA_EXT_ON` as a physical length (`w_on`), feeding
`h_eff`, `mass_kg`, and `τ_thermal` — a genuinely new dependency the
achromatic-ratio finding does not, by itself, license.

I pulled exp-026's own already-committed 3λ data (`beam_scene`, never
previously read this way): `sigma_ext` = 238.219 / 235.967 / 241.127 cells
at 450/600/750nm — a **2.16% relative spread**, about 5× larger than the
ratio's own 0.45%, and never checked against anything in this cycle.

I then ran Block B's own `self_consistent_regime()` formula by hand at all
three wavelengths (using each λ's own σ_ext and ratio):

| λ (nm) | w_on (µm) | h_eff (W/m²K) | τ_thermal (ms) | dwell/τ_thermal |
|---|---|---|---|---|
| 450 | 7.1466 | 3638.1 | 3.1994 | **20.84×** |
| 600 | 7.0790 | 3672.8 | 3.1392 | **21.24×** (the cycle's own headline) |
| 750 | 7.2338 | 3594.2 | 3.2779 | **20.34×** |

The spread across the full visible sweep is <5% (20.34–21.24×) — all three
land comfortably in the same "below `N_TRANSIENT_TAU=25`" bucket the cycle
reports, and 600nm is actually the *most* favorable of the three, not a
cherry-picked worst case. **The cycle's P-IT22-A6 headline (21.24×, below
25×) is robust to the single-λ idealization** — but this was never checked
or disclosed anywhere in the seven-file panel record, and the same gap
applies unexamined to the flagship absorber's own 3.014× T22 area ratio
(σ_ext=240.007 cells at 600nm only). Recommend this be committed as a
formal idealization-sentence addition (cheap, zero-FDTD, one paragraph) so
a future cycle doesn't have to re-derive it from scratch the way I just
did.

## 4. My top finding: the w_on-vs-r_out choice is an optical-cross-section-
   vs-real-geometry question, not just a bookkeeping convention

This is squarely a PHOTONICS-charter question and I don't think it has been
asked this way before. `w_on` is not the object's physical size — it is
`SIGMA_EXT_ON·dx`, an **extinction cross-section**, and this program's own
T9 finding already established that extinction-derived quantities on this
bench are diffraction-inflated well past the object's real geometric
footprint (σ_abs/σ_ext ratios of 0.51–0.61 exceed the ≤0.5 geometric-optics
ceiling; here, the area ratio is a much larger 2.9–3.0×). `w_on` measures
**how much power the object removes from the beam**, which is the right
quantity for computing absorbed power. It is not obviously the right
quantity for computing **heat conduction away from the object's surface**
or **the object's own thermal mass** — a real solid body conducts and
stores heat through its literal geometric boundary (`r_out`), not through
some diffraction-inflated "optical shadow." Red Team's fix 7 (one
`length_m` must feed both `h_eff` and `mass_kg`/area) is good, principled
defensive coding — it eliminates the Phase-1 draft's actual bug (silently
mixing two lengths inside one claimed-consistent chain) — but it also
forecloses, without discussion, a *third*, arguably more physically
motivated convention: **`w_on` for absorbed power (optical), `r_out` for
`h_eff`/mass (real geometry)** — deliberately mixed, not accidentally. That
convention was never computed this cycle. Its likely position: `p_abs_w`
stays at the w_on-based value (2.004×10⁻¹²W) but `dp/dT` uses `r_out`'s
much larger `h_eff` (11111 vs 3673 W/m²K) and `r_out`'s much smaller mass
— pushing `dt_ss_full` down and `τ_thermal` down together, landing
somewhere between the two reported endpoints (21.2× and 194.2×), not
identical to either. I did not compute it exactly (it needs a
`self_consistent_regime`-style function split across the power/conduction
boundary, a ~10-line, zero-FDTD change) — I flag it as the concrete,
falsifiable next test rather than asserting a number I haven't derived.

This matters because the whole point of Block B was to relieve or worsen
T22's own "is `dwell/τ_thermal` still ≥25×" concern, and the two reported
answers (21.2× "genuinely less comfortable," 194.2× "comfortably above")
disagree by 9× depending on a choice this cycle reports side-by-side rather
than argues for. Neither choice is shown to be the more physically correct
one; a third possible convention that plausibly IS the physically motivated
one was never tried.

One secondary, smaller note in the same territory: the `r_out`-consistent
regime's own `p_abs_w` is computed as `irr × r_out²_geometric × RATIO_ON`
(disclosed in the code comment, not hidden) — but `RATIO_ON` was measured
and calibrated specifically against the `w_on`-cross-section's own incident
power, not the bare geometric footprint's. Applying that same calibrated
fraction to a smaller incident-power base is a further, undiscussed
idealization (assumes the same *fractional* absorption efficiency
regardless of which aperture defines "incident power") — worth a one-line
disclosure, not a blocking issue.

## 5. Verdict for the cycle

**PARTIAL.** The load-bearing physics conclusion (every UNDETECTABLE
verdict this program has issued survives the newly-swept intermediate-dwell
regime, 2080 points, 5 regimes, a genuine population-memory check) is
robust, and I could not find a single arithmetic defect anywhere in the
corrected, post-audit code — an unusually clean cycle by this program's own
running standard (Red Team's own "fifth occurrence in seven iterations of
an undelivered fix-docket item" pattern did not recur here; all eight
mandatory fixes actually landed). What keeps this from PROMISING: (1) a
new, real σ_ext-as-physical-length idealization was introduced this cycle
and never checked for wavelength-flatness by anyone, including the five
Phase-2 seats and Red Team — I closed that gap in this review and found it
harmless, but it should not have needed a Phase-5 seat to catch it after
the fact; (2) the cycle's own headline "relief vs. worsening" question for
T22 is reported as two disclosed-but-unargued endpoints (21.2×/194.2×) with
a plausible third, more physically motivated convention never computed —
a genuinely open question this cycle's own framing ("both reported,
neither preferred") does not resolve, it just states.

## 6. Ranked top-3 candidate directions for Iteration 23

1. **QUANTUM's aperture-consistent single-coherent-mode beam check** — not
   my own charge's finding, but I'm ranking it first anyway: it is a
   self-imposed Checkpoint-4 tripwire on its THIRD deferral (Iterations
   19→20→21, and Iteration 22/exp-045 did not touch it either). PANEL.md's
   own checkpoint criterion 4 language ("Red Team flags program-integrity
   drift... a constraint quietly dropped") is squarely aimed at exactly
   this pattern. Nothing in exp-045 should be read as displacing it —
   QUANTUM leads Iteration 24, but this item cannot wait that long without
   risking a real checkpoint firing.
2. **Compute the third, power-on-w_on/conduction-on-r_out mixed thermal
   regime** (§4 above) — zero-FDTD, ~10 lines reusing `self_consistent_
   regime`'s own structure split across the power/conduction boundary,
   directly closes the 9× w_on-vs-r_out ambiguity this cycle left as two
   disclosed endpoints rather than an argued answer. PHOTONICS/THERMO
   joint, cheap, and the single most concrete unfinished thread this
   review surfaced.
3. **Commit the σ_ext λ-flatness check formally** (§3 above) — extend it
   to the flagship absorber's own 3.014× T22 area ratio (only the ON
   endpoint was checked here), and add the resulting idealization sentence
   to `NOTES.md`/`results.json` so a future cycle isn't left to re-derive
   it from scratch the way this review just did. Zero-FDTD, already
   computed in this review, essentially free to commit.

Secondary carryovers not displaced by anything above: T21's still-open
contamination-risk verdict; VISION's Iteration-23 glare/adaptation
tripwire (both already standing LOGBOOK priorities, neither touched by
this cycle or this review).
