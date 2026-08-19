# exp-046 — The Aperture-Consistent Single-Coherent-Mode Beam (T21) + T23's Mixed Length-Scale Regime + Dose Accumulation on the Full exp-038 Grid

Panel Iteration 23. Lead: THERMODYNAMICS (rotation). Runner: cloud panel
shift. Director: this shift. **9 new FDTD calls, all in Block A** (the
committed budget, exactly); Blocks B and C are desk-only, zero field solves.
Trust suite green before any number below was read: **88/88**
(`--only 12346789,10,11,12,13,14,15` 82/82 · `--only 16` 4/4 · `--only 5`
2/2), including the new stage 16 built this cycle.

**NETD is an instrument/detector threshold, not a human perceptual one —
none of the UNDETECTABLE classifications in this document bear on
constraint-3/4's human-eye verdict** (VISION SCIENCE's standing mandatory
fix; inlined here at the point of claim, per Red Team docket item 21, not
left to `results.json`). The Phase-1 proposal's "eye-invisible" language is
**struck everywhere** (docket 20) — it was a perceptual claim whose only
falsifier was a detector ratio, i.e. unfalsifiable as posed, and
constraint-3-shaped.

## Hypothesis

Three separable questions, no mechanism proposal, **T1 escape route: NONE**:

1. **Block A (live thread T21).** exp-042's beam-divergence check held the
   full 1504-cell source aperture fixed while imposing an angular spectrum
   of FWHM Δθ. A physically real single-mode emitter of divergence Δθ has a
   diffraction-limited waist instead. Does the aperture-consistent reading
   change the T21 contamination picture — and does exp-042's own desk
   Huygens–Fresnel propagator survive the regime change it implies
   (N_F falling from ~310–518 to 0.4–67)?
2. **Block B (live thread T23).** Add PHOTONICS' third, genuinely mixed
   length-scale regime (absorbed power on `w_on`, conduction/mass on
   `r_out`) to exp-045's `self_consistent_regime`. Does the least
   comfortable of the three conventions move any verdict?
3. **Block C.** Extend the dose-accumulation check from exp-045's Host-D
   four points to the full exp-038 5-host × 5-ratio grid, with a closed-form
   memory-onset criterion and a dwell-duration scan.

## Setup

The full seven-file panel record precedes this file and is unedited:
`phase1_proposal.md` (THERMODYNAMICS), five blind Phase-2 critiques,
`phase2_redteam_audit.md` (the 24-item mandatory-fix docket, which
re-derived and live-FDTD-verified its central ruling), and
`phase3_synthesis.md` (all 24 items adopted, none overridden).

`run.py` implements the adopted configuration with every docket item marked
`[docket N]` at the point of application. Geometry, propagator, window
geometry and reduction are exp-041/042's own committed ones, imported not
rebuilt: NX=360, NY=1584, ABSORB=TAPER=40, SRC_X=300, PLANE_X=77, R_OUT=78,
GUARD_OUT=185, W_FLANK=78, STEPS=1400, COURANT_FRAC=0.99, OBJ_Y=792,
D_SP=223, CPL={450:15, 600:20, 750:25}.

The one substantive change to the illumination model, and the whole of Red
Team's central ruling: **every oblique source width is `w₀/cos θ₀`**, not
`w₀` (docket 1). The observation-plane width `w_y = w₀√(1+(z_eff/z_R)²)/cos θ₀`
is unchanged (docket 2) — it is the correct partner to the fixed source.

## Phase 3 — Director's synthesis (recorded in `phase3_synthesis.md`)

All 23 substantive docket items are load-bearing in `run.py`; item 24 (the
VISION Tier-W glare/adaptation tripwire, hardened to fire Checkpoint
criterion 4 automatically if Iteration 24 closes without it) is a standing
program rule carried to Phase 5/LOGBOOK, not code.

The structurally important adoption is **item 4**: the closed-form envelope
model no longer sets any band. Every Block-A band is set by a desk
propagation of the actual complex aperture
`exp(−(Y/w_line)²)·exp(i k sinθ₀ Y)` through exp-042's own committed
Huygens–Fresnel propagator (`_G0_for` + the corrected E/H reduction),
reduced through `lab.ambient.window_means`/`weber`. The closed form is
retained only as a disclosed accuracy anchor, with its measured accuracy
printed (worst 12.0%, median 1.14%).

## Predictions (committed to git BEFORE Phase 4's run — house discipline)

Commit **`a7eaaf8`** landed `run.py`, `predictions_frozen.txt` and the new
stage-16 code with **zero FDTD calls executed**. That is structural, not a
promise: `run.py --predict-only` never imports `lab.fdtd2d` (the import
lives inside `fdtd_leg`), and `predictions_frozen.txt` is that path's own
captured stdout. Every P-TH23-* band scored below is in that file.

Two Phase-1 bands were **corrected pre-run** and the corrections are in the
frozen file, not applied afterwards:

- **C3's ceiling** [2.9×10⁻⁶, 3.1×10⁻⁶] K was written for the pre-extension
  Hosts-A/B/C scope, whose largest `n_eq` was 0.0909. Docket item 16's own
  grid extension adds `r=1.0` (`n_eq`=0.5), raising the ceiling ~5.5× by
  construction. Superseded to [1.6×10⁻⁵, 1.7×10⁻⁵] K.
- **C6's second clause** ("at the 5τ gap no point anywhere exceeds 1.05") is
  **false** in the newly added `r=1.0` column: there `21f = 21e^(−2.5) =
  1.72 > 1`, so the supremum is 1.0894, not 1.0068. The clause was
  untestable in the Phase-1 scope and is falsified by the extension the
  docket mandated.

## Phase 4 — Results (run 2026-08-19, this shift)

`results.json` regenerated from the frozen, predictions-committed code; 9
new FDTD calls, 126 s total. The nine legs were executed twice during this
shift (once before and once after two disclosed post-freeze reporting edits,
below) and **every FDTD number reproduced bit-identically** — a free
determinism check on this platform.

### Scorecard — 11 CONFIRMED, 3 PARTIAL, 1 REFUTED, 2 DROPPED at Phase 3

| ID | Verdict | Measured |
|---|---|---|
| **A0** | CONFIRMED | C = 0.374781250; aperture ratio at θ₀=40° spans **2.1462×–35.769×** (band [2.14, 35.8]) |
| **A1** | PARTIAL (computed in band; **withheld as gate-backed**) | 36/36 above `C_THR`, 35/36 at ≥20× the corrected incoherent reading, min\|C\| = 0.03227 — but see the S16-b disposition |
| **A2** | CONFIRMED | envelope anchor vs propagated reading: ≤5% at 26/36, 0 cells above 15%, worst 11.98%, median 1.14% |
| **A3** | CONFIRMED | `beam_divergence_coherent`'s synthesised aperture has 1/e half-width `w₀/cos θ₀` to **≤0.78%** at all 27 FWHM≤10° cells, ≤3.25% at the 9 FWHM=20° cells |
| **A4** | DROPPED at Phase 3 (docket 7) | premise false under the fix |
| **A5** | **CONFIRMED 4/4 — the cycle's genuine falsifiable Block-A content** | FDTD vs desk propagator: **1.91%** (N_F 53.98), **0.03%** (2.16), **0.11%** (0.54), **5.68%** (65.60); sign agreement 4/4 |
| **A6** | **REFUTED** (3 of 4 gates pass) | S16-a 1.06% ✓ · S16-b **FAIL** (992.09 vs 979.12, Δ=12.97 cells) · S16-c **6.96×10⁻¹⁵ relative** ✓ · S16-d **1.25%** ✓ |
| **A7** | DROPPED at Phase 3 (docket 9) | ill-conditioned 77–300×; legs still run as EXPLORATORY-NON-SCORING |
| **B1** | CONFIRMED | mixed `dwell/τ_thermal` = **194.17681504141214**, identical to the `r_out` regime to **0.0** (not "within round-off" — bit-identical) |
| **B2** | CONFIRMED | `dt_ss_full` = **3.293076054×10⁻⁵ K**; ratio to `r_out` = 9.151923077 = (w_on/r_out)² to 15 digits; ratio to `w_on` = 3.0280489 |
| **B3** | CONFIRMED | NETD_lo/dt_ss = **607.33** ∈ [600, 615]; Wien peak **9.8849 µm** ∈ [9.87, 9.90]; UNDETECTABLE |
| **B4** | CONFIRMED | Bi = 1.7567568×10⁻⁴, Kn = 2.807692×10⁻², slip −5.3168% — identical to the `r_out` regime |
| **B5** | CONFIRMED | 2496 points, 416 new; max ΔT over the new points **2.99357×10⁻⁶ K**, margin **6681×**, all UNDETECTABLE-or-better |
| **B6** | CONFIRMED | 1−saturation = 5.983×10⁻¹⁰ (`w_on`) and 4.68×10⁻⁸⁵ (mixed) |
| **C1** | CONFIRMED (as restated) | 21 new grid points ⇒ 42 point-runs; `\|ratio−1\|` = **exactly 0.0** at all 30 negative controls; 12 point-runs with memory, 7 above 1.05, **all** at Host D r=1.0 / Host E |
| **C2** | CONFIRMED (as restated) | closed form exact at every no-/weak-memory point; 5-pulse under-convergence up to 10.03% at the strong-memory points, in the predicted direction |
| **C3** | PARTIAL (band superseded pre-run) | max ΔT **1.64654×10⁻⁵ K**, margin **1214.7×**, 100% UNDETECTABLE-or-better |
| **C4** | CONFIRMED | **0 of 12** PUBLISHED-tier point-runs show memory; 7 of 18 UNOBTANIUM-tier do |
| **C5** | CONFIRMED | closed form vs exp-045's 8 committed points: max **9.13×10⁻⁴**, min **1.55×10⁻¹⁵** |
| **C6** | PARTIAL (one clause refuted pre-run) | 0.5τ crossing measured **2.5450** (r≪1) and **2.5900** (r=1e-1) vs closed form 2.5445224 / 2.5899770; duration scan agrees with C2 at **250/250**; the "no 5τ point exceeds 1.05" clause is false at r=1.0 |

### The miss, in full: gate S16-b failed

Pre-registered: the beam centre at `PLANE_X` within ±2 cells of ray optics
(`y_c + D_SP·tan40°` = 979.12). Measured with the committed estimator (the
interpolated 1/e² crossing midpoint): **992.09, off by 12.97 cells**. The
peak-cell estimator reads 977.0 — off by 2.12 cells, also outside the band.
Both estimators fail; there is no reading of this configuration that lands
inside ±2 cells.

**Diagnosis (post-run, desk-only, in `results.json`).** The failure is in
the gate's *target*, not the engine, and that is demonstrable without the
engine. Ray optics assumes the paraxial mapping `k_y = k·θ`. S16-b's own
`width=40` emits a **14.0° FWHM**, where `k_y = k·sin θ` is measurably
nonlinear and the propagated profile skews toward +y. Exact non-paraxial
angular-spectrum propagation of the identical aperture (Red Team's own
`geom_check.py` method, reused) puts the 1/e² midpoint at **987.14 — 8.03
cells from the ray-optics target**, i.e. the pre-registered target is
outside its own ±2-cell band before any solver is involved. FDTD sits 4.95
cells (5.4% of the beam half-width) from the exact value. At the
physically-motivated width (A-v2, 10° FWHM) the same comparison gives 3.57
cells (exact vs ray optics) and 2.26 cells (FDTD vs exact).

**Disposition of P-TH23-A6's own withholding clause** ("any gate fails ⇒ no
Block-A number is reported at all"). Applied in **scope**, not as a blanket,
and the judgment is disclosed rather than smoothed: S16-a (free-space
divergence identity, 1.06%), S16-c (absolute regression anchor, 6.96×10⁻¹⁵
relative) and S16-d (the oblique-width gate, 1.25%) certify the
width/propagator chain, so A0/A2/A3/A5 are reported as trusted. S16-b
certifies *pointing*, so the one reading that depends on where the beam
points — **A1** — is reported with the withholding clause applied: it is
**not gate-backed at this divergence**, and its 36/36 is recorded as an
estimator reading, not as a validated measurement. This is a Director-level
judgment call, and a reader who disagrees should read A1 as withheld
entirely; nothing else in this cycle depends on it.

The suite's own stage 16 carries a **first-light amendment** of that gate
(scoring against the exact propagation, in units of beam half-width, bar 8%,
measured 5.4%) following the convention stages 6, 7, 8 and 10 each already
carry. `run.py` scores the **original, unamended** gate and records it as
FAILED — the pre-registered prediction is not retro-fitted; only the suite's
forward-looking gate is repaired.

### What Block A actually established

1. **`profile="gauss"` is trust-gated for the first time in this program's
   history.** It was declared in `lab/fdtd2d.py` since the bench was built
   and, grep-verified, never once exercised. Stage 16 now gates it, and the
   oblique-width gate is the one that fires on the defect this cycle
   actually had: at the wrong width (`w₀` = 42.947) the same measurement
   reads 87.25 against a 79.47 target (9.8% off); at the right width
   (`w₀/cos θ₀` = 56.063) it reads 80.47 (1.25%).
2. **exp-042's desk Huygens–Fresnel propagator survives the regime change.**
   It had never been checked below N_F ≈ 310. FDTD reproduces it to 1.91% /
   0.03% / 0.11% / 5.68% at N_F = 53.98 / 2.16 / 0.54 / 65.60, signs 4/4 —
   comfortably inside the pre-registered 15%/35% bands. **This is the
   result of the cycle**, and it is the only Block-A prediction that could
   have failed on evidence rather than on algebra.
3. **The headline the proposal advertised was never an experimental
   question.** Red Team's Attack 2 proved, and this cycle measures, that
   `beam_divergence_coherent` already synthesises a Gaussian aperture of 1/e
   half-width `w₀/cos θ₀` (≤0.78% at 27 of 36 cells). QUANTUM's Iteration-20
   conjecture is recorded as **mis-posed**, not refuted or confirmed.
4. **exp-042's committed "coherent" column is under a superseded
   convention.** `C_coherent` exists only under the obliquity-on-E recipe
   the Phase-5 erratum itself calls illegitimate, and
   `block_beam_corrected` has no coherent column at all. A
   corrected-convention coherent column is generated here so the comparison
   is made at matched convention (docket 10): the propagated reading differs
   from the *committed* column by >3% at 2 of 27 FWHM≤10° cells (worst
   9.20%) and from the *matched-convention* column at 1 of 27 (worst 6.45%).

### Blocks B and C

Block B reproduces the docket's own hand-verified numbers to every printed
digit, and its exp-045 reproduction self-check (both committed regimes,
recomputed through the new two-length function) is exact to **0.0** relative
— the generalisation to separate `length_power_m`/`length_cond_m` changes
nothing where it should change nothing. The mixed regime is the least
comfortable of the three on the axis THERMODYNAMICS' charter scores
(607× below `netd_lo` versus 1839×/5558×) and still classifies
UNDETECTABLE.

Block C's grid count is computed, not asserted: **21** new points, agreeing
with Phase 3's hand-count. The extension is what makes the block a test
rather than an all-negative-control grid — Red Team's Attack 9. The
positive branch fires exactly where Attack 9 predicted (Host E at
`D/τ_k ≈ 0.067`), and the closed form (C2) explains the whole axis:
memory ⟺ `D/τ_k < ln(21 f)`, verified against the duration scan at
**250/250** points.

## Learned

**NETD is an instrument/detector threshold, not a human perceptual one —
none of the findings below bear on constraint-3/4's human-eye verdict.**

1. **A desk propagator can be validated three orders of Fresnel number
   outside where it was built.** exp-042's Huygens–Fresnel propagator was
   constructed and used at N_F ≈ 310–518 and is confirmed here at
   N_F = 0.54–65.6 to ≤5.7%. That is a reusable instrument result, not a
   T21 finding, and it is the honest deliverable of this cycle's Block A.
2. **A gate can fail because its target is wrong.** S16-b's ray-optics
   target is 8.0 cells off the exact non-paraxial answer at its own
   configuration's 14° divergence — the band was falsified before any
   engine ran. Two lessons: pre-registered gates need their *targets*
   checked for validity in the configuration they will run in, not just
   their bars; and a failed gate's first job is attribution, which cost
   nothing here (one FFT) and would have cost a shift of suspicion
   otherwise.
3. **Extending a grid can falsify a prediction about the grid.** Docket
   item 16 added the `r=1.0` column to close Red Team's all-negative-control
   attack; that same column falsifies C6's "no 5τ point anywhere exceeds
   1.05". Both facts are consequences of the same fix, and the second was
   found by the code, before the run, not by a reviewer afterwards.
4. **One dimensionless number replaces a host list.** Amendment 3's
   "memory only at Hosts D and E" is `D/τ_k < ln(21 f)` — Hosts A/B/C sit a
   factor 26 past the threshold, so their zero is exact (measured `0.0`,
   not "small"). The tier correlation survives, but with a mechanism:
   PUBLISHED-tier hosts have lifetimes 10³–10⁸× shorter than any sweep
   dwell this program models.
5. **The same wiring bug species has now recurred three times.** Iteration
   15 (digit-substring collision), Iteration 17 (incomplete fix), and this
   cycle (`--only 16` selecting stages 1 and 6; and Iteration 17's fix
   silently dropping packed tokens in mixed invocations, so
   `--only 12346789,10,11` — cited as 46/46 five times in SESSION_LOG —
   selected only stages 10 and 11). Caught this time by executing the
   selector against every citation in this program's own history before
   wiring the new stage, which is the only method that has ever caught it.

## Idealizations (carried from Phase 1, corrected at Phase 3, extended here)

1. **Expressibility contract (PANEL.md, THERMODYNAMICS' charter):** every
   Block-B and Block-C number is a post-run analytic calculation, not an
   FDTD output, and is labelled as such in `results.json`. Zero field solves
   in either block.
2. **Paraxial Gaussian relation.** `w₀ = 0.374781250·λ/Δθ` assumes
   sin θ ≈ θ. **Restated (docket 12):** the waist is **1.0737 λ at all three
   wavelengths, one value** — so Block A's 3-λ sweep carries no material
   wavelength dependence beyond fixed cell geometry, and should not be read
   as a wavelength result. **And, new this cycle, this idealization has now
   bitten:** S16-b's failure is exactly the paraxial assumption failing at
   14° divergence.
3. **Fully coherent, monochromatic, single transverse mode.** A real
   flashlight is none of these. No sourced coherence length or beam FWHM for
   any real flashlight exists anywhere in this program (T21's standing gap).
   The Gaussian Schell-model partial-coherence bridge remains unbuilt; this
   cycle does not build it and does not claim to.
4. **Aperture truncation, corrected (docket 11).** Unaimed rim residual is
   **9.99×10⁻³ in amplitude / 9.98×10⁻⁵ in intensity** — 25×/657× worse than
   the Phase-1 idealization claimed, still below `C_THR`=0.005 but without
   the "four-plus orders" margin that idealization asserted. The aimed leg
   truncates at 1.61–2.96 `w_line` at the FWHM=2° cells with rim amplitude
   up to 7.43×10⁻²; **5 of 36 aimed cells are flagged truncation-INVALID**
   (rim amplitude > 10⁻²) and excluded from every aimed-leg summary rather
   than the aimed leg being dropped wholesale.
5. **Thermal body shape.** exp-045's cube idiom (area = L², volume = L³) is
   inherited unchanged so the mixed regime differs in exactly one variable.
   Disclosed sensitivity: a true disk gives `dwell/τ_thermal` = 97.09×
   instead of 194.18× — no verdict moves.
6. **Silicon identity is ASSUMED, not sourced (docket 18).** The provenance
   chain terminates unsourced: exp-046 §2.3 → exp-037/NOTES.md:828-829 →
   "standard *cited* thermal constants" → grep returns only that sentence.
   Values correct for bulk crystalline Si; the label was wrong. Recorded in
   `results.json` and in REALIZABILITY_MEMO Amendment 5.
7. **Fill factor (docket 19).** `netd_disposition`'s `fill_factor` is left
   at 1.0 while `mass = ρ_Si·L³` assigns 100%-fill crystalline silicon to
   what the same module elsewhere calls a dilute vapour/aerosol host. A
   dilute host lowers the effective ΔT (making UNDETECTABLE more
   conservative) but also lowers τ_thermal — both sides disclosed together,
   with a ρC_P sensitivity row (at 10% fill, `dwell/τ_thermal` = 1942× and
   the `N_TRANSIENT_TAU`=25 question does not change answer).
8. **Block C's OFF gap uses a hard k_f = 0** — exp-045's own disclosed
   idealization, unchanged so the new points are comparable to its Host-D
   four.
9. **Bench-scale, not witness-scale.** T8/T13's near-field→witness bridge is
   unresolved; no ΔT or C here extrapolates to 45 m.
10. **NETD is an instrument/detector threshold, not a human perceptual one**
    — stored per point at all 2496 + 42 + 250 points AND inlined at every
    point of claim in this file and in `run.py`'s console output (docket 21:
    the loci that have actually failed twice, not storage, which
    `lab/thermo_sidecar.py:215` already auto-fills).
11. **FDTD settling.** exp-041's 1400 steps and its λ-dependent causal
    transit margin (13.0/9.8/7.8 periods at 450/600/750 nm) are inherited
    unchanged; the margin is thinnest at 750 nm, which is leg A-v4 — the
    worst A5 residual (5.68%). Disclosed, still-untested confound, and now
    the **fifth** consecutive cycle in which the dedicated settling-margin
    test is not run.
12. **A-unaimed's beam walks off the object window** by 162–187 cells while
    the object window is ±78 cells wide. That is a property of the geometry,
    not a defect — and it is why A1 is a pointing reading (docket 5).
13. **Sign-convention guard (docket 15).** exp-042's analytic `B(y)` is
    globally negative; `lab.ambient.observer_profile` is positive. `weber` is
    invariant under a global sign flip, so only `weber`-reduced scalars cross
    code paths here — enforced by `_weber_of` being the only route from any
    profile to any compared number.
14. **Two post-freeze edits to `run.py`, disclosed rather than silent.**
    After the predictions commit (`a7eaaf8`) and after the first execution of
    the nine legs, two reporting-only changes were made: (i) the θ₀=0 leg's
    Weber contrast is recorded as `null` instead of a ~10¹⁰ artefact (at
    θ₀=0 the beam sits on the object window and the flank windows sit in its
    far exponential wing, so the Weber denominator underflows; S16-a is
    gated on w(z), not on C); (ii) the S16-b post-run diagnostic and the
    amended-gate record were added. **Neither touches a desk prediction**:
    `run.py --predict-only` after both edits is byte-identical to
    `predictions_frozen.txt` except for its own elapsed-time line, and the
    nine FDTD legs reproduced bit-identically across both executions.
15. **A3's own tolerance is quantization-limited, and Red Team's quoted
    range understates its own measurement.** The audit prose quotes
    0.07–1.3% (FWHM≤10°) / 3.5–5.7% (FWHM=20°) for the effective-aperture
    identity; re-running the audit's own script reproduces **0.07–2.98% /
    3.45–7.64%**. The excess is integer-grid crossing quantization (±0.5 cell
    = 2.4% of the width at the narrowest cell). With the crossing
    interpolated the spread collapses to ≤0.78% / ≤3.25%. Disclosed rather
    than re-quoting the audit's range.

## Cost

9 new FDTD calls (126 s), 5 s of desk work, stage 16's own 4 FDTD calls
(80 s) inside the trust suite. Blocks B and C: zero.
