# exp-046 — The Aperture-Consistent Single-Coherent-Mode Beam (T21) + T23's Mixed Length-Scale Regime + Dose Accumulation on the Full exp-038 Grid

Panel Iteration 23. Lead: THERMODYNAMICS (rotation). Runner: cloud panel
shift. Director: this shift. **9 new FDTD calls, all in Block A** (the
committed budget, exactly); Blocks B and C are desk-only, zero field solves.
Trust suite green before any number below was read: **88/88**
(`--only 12346789,10,11,12,13,14,15` 82/82 · `--only 16` 4/4 · `--only 5`
2/2), including the new stage 16 built this cycle. **After the Phase-5
mandatory-fix close (below): 89/89** — stage 16 is 5/5, its pointing gate
repointed to the physically correct comparator and re-barred at ≤1.5%
(measured **0.46%**), plus a new desk-only acceptance gate requiring an
independent second derivation of that comparator (measured 0.030 cells).

**NETD is an instrument/detector threshold, not a human perceptual one —
none of the UNDETECTABLE classifications in this document bear on
constraint-3/4's human-eye verdict** (VISION SCIENCE's standing mandatory
fix; inlined here at the point of claim, per Red Team docket item 21, not
left to `results.json`). The Phase-1 proposal's "eye-invisible" language is
**struck from every live artifact and every committed result; the Phase-1
draft is preserved unedited under a SUPERSEDED banner** (T10's
"flag, don't rewrite" convention) — docket 20, delivery claim corrected at
Phase 5 (p5 docket 3). It was a perceptual claim whose only falsifier was a
detector ratio, i.e. unfalsifiable as posed, and constraint-3-shaped. The
earlier wording here ("struck **everywhere**") and the `NETD_DISCLAIMER`
constant's "no 'eye-invisible' claim is made **anywhere in this cycle**"
were false as claims about this repository: the phrase was live and
unflagged at §1 and P-TH23-B3 of `phase1_proposal.md`, one cycle after this
program invented the SUPERSEDED-banner remedy for exactly that failure mode.
The substantive half of docket 20 *was* delivered; the delivery claim was
not, and both halves are now on the record.

## Phase 5 — the mandatory-fix close (same shift)

`phase5_redteam_audit.md` §8 issued a 20-item docket: **Tier 0 (items 1–5)**,
whose carry-over would fire Checkpoint criterion 4 automatically, and
**Tier 1 (items 6–20)**, mandatory the same shift by this program's own
established convention. **All 20 landed in this close.** Every numeric
correction below is computed by `run.py`, not hand-typed; every prose
correction is a flag or a restatement at the locus that was wrong, never a
silent rewrite of a committed record. `results.json` gains a top-level
`phase5_erratum` key (exp-042's own precedent) carrying the corrected
attributions, and `phase1_proposal.md` gains the SUPERSEDED banner.

**Two scope calls the docket does not fully resolve, disclosed rather than
smoothed over.** (1) Items 4, 19 and 20 each say "propagate to LOGBOOK's
Iteration-23 close"; that close is not yet written, so the canonical strings
live here and in `results.json` and are the text to carry at close — this
shift invents no partial LOGBOOK entry. (2) Item 1's mandatory acceptance
test must reproduce exp-042's `_G0_for`/`field_and_h`, but VALIDATION's own
rule is that the suite depends on no experiment directory; the propagator is
therefore **re-derived inside `run_all.py`** from the geometry constants —
which reproduces exp-042's numbers exactly (991.645 / 91.576) *and* doubles
as the independent second derivation item 20 requires.

### The item-24 hardened rule — ONE rendering (p5 docket 4)

It existed in three inconsistent renderings, and the fullest one had quietly
weakened the constraint it advertised as hardened. The carve-out ("or with an
explicit renewed-deferral reason that itself survives a Phase-2 Red Team
audit") is **struck** — Iteration 23's own deferral was exactly such a
reason, so the tripwire's own triggering event satisfied it. The dropped
clause is **restored**. The false claim of "mirroring the aperture-check
rule's own wording exactly" is **struck**. The canonical text, verbatim,
identical to `results.json`'s `phase5_erratum.item_24_hardened_rule`:

> If Iteration 24 closes without VISION SCIENCE's glare/adaptation Tier-W
> sidecar having been run (by any lead seat, sourced via
> WebSearch-snippet-tier per the standing T18 adaptation), Checkpoint
> criterion 4 fires automatically and immediately — no further debate, no
> seat vote, no Director discretion, and no further one-cycle extensions via
> prose. A Phase-2 Red Team audit blessing a renewed deferral does NOT
> satisfy this rule: Iteration 23's own deferral was Red-Team-blessed, and
> that is what tripped it.

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

The full seven-file panel record precedes this file and its **body text** is
unedited — `phase1_proposal.md` now carries a **SUPERSEDED banner** prepended
at the Phase-5 close (p5 docket 3, exp-045 `f48de18`'s own form), naming every
superseded claim; nothing below that banner is altered:
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
program rule carried to Phase 5/LOGBOOK, not code — **repaired at Phase 5 to
the single rendering quoted above (p5 docket 4); `phase3_synthesis.md`'s
version is superseded and is not the one to carry.**

**Docket item 21, stated as an OVERRIDE (p5 docket 13)**, per this program's
own rule that an overridden item is stated as overridden rather than silently
narrowed: item 21 asked for the NETD disclaimer at every point of claim. It
is applied per point in C2 and C5, and at **block scope** for C1 and C4 —
because C1 and C4 issue no detectability claim of their own (they count
memory point-runs and realizability tiers), and a per-point disclaimer on a
key that makes no detectability claim is noise, not disclosure. That was an
override, not a delivery, and Phase 4 did not say so.

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
new FDTD calls, 126 s total. The nine legs were executed **three times**
during this shift (before and after two disclosed post-freeze reporting
edits, and again at the Phase-5 mandatory-fix close) and **every FDTD number
reproduced bit-identically each time** — a free determinism check on this
platform, now with three independent executions.

### Scorecard — 11 CONFIRMED, 2 PARTIAL, 1 WITHHELD, 1 REFUTED, 2 DROPPED at Phase 3

*(Tally corrected at Phase 5, p5 docket 5: A1 is dropped from the PARTIAL
count. A reading the Director has withheld must not be counted in the cycle's
own success headline, and the Phase-4 cell "PARTIAL (computed in band;
withheld as gate-backed)" parses literally as the inverse of its intent —
which matters because LOGBOOK entries are built by copying scorecard rows.)*

| ID | Verdict | Measured |
|---|---|---|
| **A0** | CONFIRMED | C = 0.374781250; aperture ratio at θ₀=40° spans **2.1462×–35.769×** (band [2.14, 35.8]) |
| **A1** | **WITHHELD — not gate-backed (S16-b FAILED)** | 36/36 above `C_THR`, 35/36 at ≥20× the corrected incoherent reading, min\|C\| = 0.03227 — an estimator reading, not a validated measurement. **Post-fix (p5 docket 1–2, same close):** the repointed S16-b **passes at 0.46%** (0.418 cells on a 90.99-cell half-width), so the pointing chain *is* validated at 600 nm/40°, and A1 is restored as an explicitly-labelled **desk geometry reading, gate-backed at that configuration**. It stays out of the CONFIRMED column: it was never an experimental adjudication of coherence, and its own mechanism sentence ("C → −1 regardless of coherence") is contradicted at the 4 positive-C cells (p5 docket 10). |
| **A2** | CONFIRMED | envelope anchor vs propagated reading: ≤5% at 26/36, 0 cells above 15%, worst 11.98%, median 1.14% |
| **A3** | CONFIRMED, **scoped at Phase 5 (p5 docket 6/7)** | `beam_divergence_coherent`'s synthesised aperture has 1/e half-width `w₀/cos θ₀` to **≤0.78%** at all 27 FWHM≤10° cells, ≤3.25% at the 9 FWHM=20° cells. **The identity is about the CENTRAL LOBE.** At the 9 FWHM=20° cells the synthesised object is a **three-lobe comb** — replicas at ±412–722 cells, amplitude 0.440–0.472, carrying **48.1–68.0%** (41.7–67.1% tapered) of the aperture's intensity outside ±3·w_line — i.e. **not** a single transverse mode there. The residual is QUANTUM's closed form `w_meas/w_line = 1/√(1−4σ_θ²tan²θ₀)` (predicted 0.783%/3.246% vs measured 0.781%/3.252% at FWHM=10°/20°, θ₀=40°, zero free parameters), **not** taper truncation. |
| **A4** | DROPPED at Phase 3 (docket 7); **mechanism RESTORED as real at Phase 5 (p5 docket 8)** | The 5–20% magnitude band was correctly falsified. The 41-point angular-sampling aliasing it named is **real**: n=41→401 moves the scored `C_empty` by up to **4.473%** (450 nm/36°/FWHM=20°, committed convention; 3.18% corrected). `gaussian_angle_weights(n=41)` had **never** been convergence-checked in this program's history. New open item for Iteration 24. |
| **A5** | CONFIRMED 4/4 — **2 informative legs, 2 saturated (p5 docket 9)** | FDTD vs desk propagator in **C**: **1.91%** (N_F 53.98), **0.03%** (2.16), **0.11%** (0.54), **5.68%** (65.60); sign agreement 4/4. In the conditioned currency **1+C**: **0.268% / 8.405% / 8.373% / 0.799%**, with per-leg conditioning amplification **0.1× / 299× / 74× / 0.1×**. The cycle applied its own disqualifying criterion (the same conditioning factor) to drop A7 and not to the neighbouring A5 legs at identical `C_empty`. Nothing is refuted — 8.4% passes a 15% band — but "the cycle's genuine falsifiable Block-A content" overstates what 4/4 buys. |
| **A6** | **REFUTED** (3 of 4 gates pass) | S16-a 1.06% ✓ · S16-b **FAIL** (992.09 vs 979.12, Δ=12.97 cells) · S16-c **6.96×10⁻¹⁵ relative** ✓ · S16-d **1.25%** ✓ |
| **A7** | DROPPED at Phase 3 (docket 9) | ill-conditioned 77–300×; legs still run as EXPLORATORY-NON-SCORING |
| **B1** | CONFIRMED — **DESK-VERIFIABLE STRUCTURAL IDENTITY, not a measurement (p5 docket 17)** | mixed `dwell/τ_thermal` = **194.17681504141214**, identical to the `r_out` regime to **0.0** (not "within round-off" — bit-identical). Tagged the way A1/A3 are: τ_thermal contains no power term and "mixed" is *defined* as `r_out`-conduction, so bit-identity cannot fail. Same species Attack 2 struck one block over; `phase3_synthesis.md` already said "a reproduction, not a fresh finding" — one document upstream of the one that gets cited. |
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

> **PHASE-5 ERRATUM (p5 docket 2) — flag, don't rewrite (exp-042's own
> precedent). The paragraphs below are left exactly as committed at Phase 4;
> their *attribution numbers are wrong*, and here is the correction.** The
> post-run diagnostic's comparator was itself physically wrong: it propagated
> the aperture as a prescribed **field** and reduced it with **|E|²**, where
> `lab/fdtd2d.py:232-237` impresses a line **current** (so the radiated
> spectrum carries an extra `1/k_x`) and `lab/ambient.py`'s `observer_profile`
> reads a **flux** (obliquity `k_x/k` entering once, via H, not squared via
> E). Two missing obliquities, opposite directions, no cancellation — the
> fourth appearance of the species LOGBOOK T21 records from Iteration 19, and
> the first inside `lab/`. Corrected comparator: **991.675** (not 987.14),
> against FDTD 992.093 — cross-validated against exp-042's own committed
> `_G0_for`/`field_and_h` propagator (991.645) to **0.030 cells**.
>
> | term | committed here | **corrected** |
> |---|---|---|
> | target error (ray optics vs exact) | 8.03 cells (62%) | **12.556 cells (96.8%)** |
> | engine error (FDTD vs exact) | 4.95 cells (38%) | **0.418 cells (3.2%)** |
>
> **The engine is ~12× better than this document reports; the target is 56%
> worse.** 0.418 cells is **0.459% of the beam half-width**. And the further
> decomposition: under a *peak* estimator — which is what ray optics actually
> predicts, a stationary-phase ray — exact 976.54 / FDTD peak-cell 977.0 /
> ray optics 979.12, i.e. **2.58 cells**. So the 12.97 cells are ≈**9.97
> cells estimator/skew mismatch**, ≈**2.58 cells genuine non-paraxial target
> error**, ≈**0.42 cells engine**. Learned #2 and idealization 2 below name
> the right species and assign it ~4× too much of the effect, and none to the
> estimator pairing that dominates.
>
> **The shipped 8% bar would itself have FAILED.** At Block A's own extreme
> cell (FWHM=20°, θ₀=40°, 600 nm, `width` = w₀/cos θ₀ = 28.03) the shipped
> comparator reads 994.223 against an FDTD 1005.549 — **9.38% against its own
> 8% bar** — and would have blamed a solver whose true error there is
> **0.38%** (correct comparator 1005.090, reproduced by this shift's own
> corrected function to 1005.088). A gate that mis-fires inside the block it
> certifies is not a gate. The suite's stage-16 gate (b) is repointed and
> re-barred at **≤1.5%** (measured 0.46%), with a new desk-only acceptance
> gate (b2) requiring agreement with an independent second derivation
> (measured **0.030 cells**). `run.py` still scores the ORIGINAL,
> pre-registered gate and still records it as FAILED — nothing is
> retro-fitted.

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
forward-looking gate is repaired. **[SUPERSEDED at the Phase-5 close — that
first-light amendment's comparator was itself physically wrong and its 8%
bar would have mis-fired inside Block A; repointed to the line-current/flux
comparator and re-barred at ≤1.5% (measured 0.46%), with a new acceptance
gate 16b2. See the erratum block above (p5 docket 1–2). The half that still
stands: `run.py` still scores the original gate and still records it FAILED.]**

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

   **TEMPERED AT PHASE 5 (p5 docket 9).** In the conditioned currency `1+C`
   the same four legs read 0.268% / 8.405% / 8.373% / 0.799%, with per-leg
   conditioning amplification 0.1× / **299×** / **74×** / 0.1×. Two of the
   four are saturated by the cycle's *own* disqualifying criterion — the same
   factor that dropped A7. So this is **2 informative legs and 2 saturated
   ones**, not 4 equally-weighted ones. Nothing is refuted (8.4% passes a 15%
   band), and the finding survives: *the propagator reproduces FDTD to ≤0.80%
   at N_F ≈ 54–66*. What does not survive is the unqualified "4/4".
3. **The headline the proposal advertised was never an experimental
   question.** Red Team's Attack 2 proved, and this cycle measures, that
   `beam_divergence_coherent` already synthesises a Gaussian aperture of 1/e
   half-width `w₀/cos θ₀` (≤0.78% at 27 of 36 cells) — ~~QUANTUM's
   Iteration-20 conjecture is recorded as **mis-posed**, not refuted or
   confirmed.~~

   **SCOPED AND RE-RULED AT PHASE 5.** *(p5 docket 6)* The identity is a
   statement about the effective aperture's **central lobe**. Attack 2
   replaced the discrete sum by an integral — a Poisson-summation step, valid
   only if the comb's replicas fall outside the aperture, which Attack 2 never
   checked. At the 9 FWHM=20° cells they do not: replicas at ±412–722 cells,
   amplitude 0.440–0.472, carrying **48.1–68.0%** of the aperture's intensity
   outside ±3·w_line. The A3 *measurement* is not falsified; the
   *interpretation* — that the coherent column already **is** the
   diffraction-limited single transverse mode — is, at 9 of 36 cells. **This
   must not enter LOGBOOK unqualified.** *(Disclosed refinement of Red Team's
   own §2.1 table: its "≤0.06 amplitude / ≤0.1% outside" for the whole
   FWHM≤10° class holds at 24 of 27 cells, not all — at the three
   450 nm/FWHM=10° cells the first replica's shoulder reaches the aperture
   rim at amplitude 0.059/0.107/0.177 and 0.14%/0.51%/1.59% of intensity.
   Sharpens the scoping; does not change it.)*

   *(p5 docket 18)* **QUANTUM's Iteration-20 conjecture, recorded accurately,
   per Red Team's three-line Phase-5 ruling:** its **premise** (exp-042's
   coherent column holds the full ~75λ aperture fixed — beamforming, not
   natural divergence) is **REFUTED at the 27 FWHM≤10° cells** and
   **PARTIALLY VINDICATED at the 9 FWHM=20° cells**, where the replicas do
   substantially occupy the aperture, directionally what the premise claimed.
   Its **prediction** ("lands much closer to the incoherent reading") is
   **REFUTED at all 36 cells, at the desk**. **"Mis-posed" belongs to
   P-TH23-A1 as a scored metric** (Attack 7's pointing tautology) **and
   nowhere else** — "mis-posed" was both over-charitable and applied to the
   wrong object.
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

   **RESTATED AT PHASE 5 (p5 docket 9).** The propagator reproduces FDTD to
   **≤0.80%** at N_F ≈ 54–66 and to **≈8.4%** at N_F ≈ 0.5–2.2, *where the
   reduction is ill-conditioned by 74–299× and should not be quoted in C at
   all*. And PHOTONICS' narrower point is upheld: `_G0_for`'s validity
   parameter is **kr**, not N_F — the module asserts `kr > 50`, set by `D_SP`
   and the window span, not by aperture width. "Validated three orders of
   Fresnel number outside where it was built" is the wrong statement of what
   was earned; what was earned is a validation **across N_F at fixed,
   always-satisfied kr**.
2. **A gate can fail because its target is wrong.** ~~S16-b's ray-optics
   target is 8.0 cells off the exact non-paraxial answer at its own
   configuration's 14° divergence~~ — the band was falsified before any
   engine ran. Two lessons: pre-registered gates need their *targets*
   checked for validity in the configuration they will run in, not just
   their bars; and a failed gate's first job is attribution, which cost
   nothing here (one FFT) and would have cost a shift of suspicion
   otherwise.

   **FLAGGED AT PHASE 5 (p5 docket 2), not rewritten.** The lesson stands and
   the numbers do not: the correct figure is **12.556 cells** of target error
   (96.8%) against **0.418 cells** of engine error (3.2%), because the
   comparator that produced "8.0" was itself wrong — see the erratum block
   above. A third lesson, paid for the hard way: **a replacement target
   shipped inside a same-shift correction is itself an unreviewed physics
   change**, and this one was wrong in a species this program had already
   adjudicated three times. That is the standing rule in item 7 below.
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
   `--only 12346789,10,11` — ~~cited as 46/46 five times in SESSION_LOG~~ —
   selected only stages 10 and 11). Caught this time by executing the
   selector against every citation in this program's own history before
   wiring the new stage, which is the only method that has ever caught it.

   **CORRECTED AT PHASE 5, before it reached LOGBOOK (p5 docket 12).** The
   bug is real; its blast radius was **over-claimed**, which is the fix-docket
   pattern's mirror image and just as damaging to the record. The exact-match
   rule that caused the packed-token regression landed at commit **`6082e02`,
   2026-08-17**. Running the *pre*-`6082e02` `_stage_selected` against
   `--only 12346789,10,11` selects **{1,2,3,4,6,7,8,9,10,11}** — the intended
   ten stages. All five SESSION_LOG citations of that invocation (lines
   1026/1155/1253/1347/1455) sit under headers dated **2026-08-14/15**
   (Iterations 7–11, exp-030/031/032/033/034) and were **correct under the
   code in force**. The regression affects **post-2026-08-17 invocations only,
   none of which was ever cited: no published trust-suite citation in this
   program's history was damaged.** The `--only 16 → {1,6,16}` and
   `--only 12 → {1,2,12}` halves are correct and the fix itself is right.
   `VALIDATION.md` — the file CLAUDE.md instructs every agent to read before
   bench work — carried the over-claim and is corrected in the same commit.
6. **T23's disposition, written somewhere durable (p5 docket 14).** The
   mixed convention is adopted: **absorbed power on `w_on`** (the length
   `RATIO_ON`'s own calibration is defined on — using `r_out` there
   double-counts beam geometry the ratio already contains) and **conduction
   and thermal mass on `r_out`** (the Nu=2 derivation `h_eff = k_air/L`
   requires the *body's* scale, and mass is the body's). And the honest
   split: the **operative** below-vs-above-`N_TRANSIENT_TAU`=25 question is
   decided **robustly** — 97×–19418× across every disclosed shape and fill
   variation, no endpoint anywhere near 25 — while the **nominal length**
   question is decided **by argument, not by measurement**; this cycle
   produced nothing that discriminates between the three conventions.
   *Caveat, and it is the sharpest charter-relevant open item this cycle
   leaves:* those τ_thermal numbers are lumped single-τ numbers, and Bi ≥ 0.25
   at every sub-unity fill factor, where that model is not licensed (item 7's
   sibling, idealization 7 below). **A τ_thermal that is not a well-defined
   single number is a worse problem for T23 than the length-scale ambiguity
   T23 was opened to settle.** Before this fix, `T23` appeared in
   `results.json` only inside two regime *labels*, and the argument for the
   mixed convention lived only in `phase1_proposal.md` §2.3 — a document with
   a dozen struck claims in it and, until this same close, no banner.
7. **STANDING RULE — post-freeze changes to a gate's TARGET (p5 docket 20,
   ELECTROMAGNETISM's, adopted and hardened by Red Team).** *A post-freeze
   change to a trust-suite gate's **target** — as opposed to its bar or its
   reporting — is a physics change and requires an **independent second
   derivation, from a different route**, before it is committed. Shipping one
   without that derivation fires Checkpoint criterion 4 automatically at the
   next Phase 5 that finds it.* Recorded alongside Iteration 19's own warning
   that same-shift correction "should not be read as establishing same-shift
   correction is generally safe from criterion 4." Iteration 23 shipped
   exactly such a change without a second derivation, and it was wrong; this
   close's repoint carries one, **wired into the suite as gate 16b2** so it
   cannot silently rot. To carry to LOGBOOK at close.
8. **NEW LIVE THREAD — the `C_empty` channel's absorbing-boundary systematic
   (p5 docket 19).** Red Team's four new FDTD runs move `ABSORB` 40→60 at two
   legs: A-v4 by **+0.0070** in C (**1.39× VISION's own C_thr**, closing the
   desk gap 5.68%→1.43%) and A-v1 by **−0.0022** (widening it 1.91%→3.69%,
   i.e. *away* from the desk value). Real at both legs, **not** a monotone
   convergence — so EM's "the residual is mostly a boundary artefact" is
   **confirmed at one leg and NOT established as a general explanation**, and
   is recorded as narrowed, not as "explained". What *is* established is a
   **0.002–0.007 absolute systematic** — 0.4–1.4× the perceptual threshold the
   whole T21 contamination question is scored against — on an `ABSORB = 40`
   (with `SRC_X`=300, `PLANE_X`=77) inherited unexamined by every T21/T16
   reading since exp-041, including all 30 Block MAIN rows T21's fringe
   mechanism was fitted to. Structurally the same debt T11 tracks for the
   box-ledger channel. Iteration 24 design: sweep `ABSORB` with `SRC_X` moved
   clear of the x-damping band so EM's ABSORB=80 confound does not recur,
   source span fixed, all 3 λ, ~6–9 FDTD runs. *Not re-measured this shift —
   the numbers are Red Team's, cited as its measurement; this close carries no
   new FDTD budget.* To carry to LOGBOOK at close as a new live thread.

## Idealizations (carried from Phase 1, corrected at Phase 3, extended here)

1. **Expressibility contract (PANEL.md, THERMODYNAMICS' charter):** every
   Block-B and Block-C number is a post-run analytic calculation, not an
   FDTD output, and is labelled as such in `results.json`. Zero field solves
   in either block.
2. **Paraxial Gaussian relation.** `w₀ = 0.374781250·λ/Δθ` assumes
   sin θ ≈ θ. **Restated (docket 12):** the waist is **1.0737 λ at all three
   wavelengths, one value** — ~~so Block A's 3-λ sweep carries no material
   wavelength dependence beyond fixed cell geometry, and should not be read
   as a wavelength result.~~ **And, new this cycle, this idealization has now
   bitten:** S16-b's failure is exactly the paraxial assumption failing at
   14° divergence.

   **CORRECTED AT PHASE 5 (p5 docket 10):** the "consequently … NO material
   wavelength dependence" clause is **struck**. The medium *is* dispersionless
   and the emitter *is* λ-scale-invariant — that half is true — but
   `N_F ∝ λ_cells` and **the reading is strongly chromatic**: **4 of 36 cells
   read positive C** (a glint at the object window), all at FWHM=2° and
   600/750 nm, with a **sign reversal across the visible band at all three
   θ₀**:

   | θ₀ | C(450) | C(600) | C(750) |
   |---|---|---|---|
   | 36° | −0.24576 | **+0.07625** | **+0.24362** |
   | 38° | −0.37331 | −0.03227 | **+0.16367** |
   | 40° | −0.47266 | −0.12334 | **+0.09368** |

   The `|C| > C_THR` band is blind to this because it takes an absolute
   value. **A1's own committed mechanism sentence ("C → −1 regardless of
   coherence") is contradicted at exactly those cells** — flagged in A1's
   prediction record, not rewritten. Given T7's chromatic-silhouette finding
   and T21's worst cell having been 750 nm since Iteration 19, this is not a
   cosmetic wording issue. **R3's own meta-rule applies:** the resolution
   check on these four cells is queued for Iteration 24 *before* "glint at
   750 nm" is allowed into the record as physics.

   **And the paraxial correction has a second half (p5 docket 2):** S16-b's
   failure is *not* mostly the paraxial assumption. Of the 12.97 cells, only
   ≈2.58 are genuine non-paraxial target error; ≈9.97 are estimator/skew
   mismatch (1/e² midpoint scored against a stationary-phase ray) and ≈0.42
   are the engine. This idealization names the right species and was assigned
   ~4× too much of the effect.
3. **Fully coherent, monochromatic, single transverse mode.** A real
   flashlight is none of these. No sourced coherence length or beam FWHM for
   any real flashlight exists anywhere in this program (T21's standing gap).
   The Gaussian Schell-model partial-coherence bridge remains unbuilt; this
   cycle does not build it and does not claim to.
4. **Aperture truncation, corrected (docket 11).** Unaimed rim residual is
   **9.99×10⁻³ in amplitude / 9.98×10⁻⁵ in intensity** — 25×/657× worse than
   the Phase-1 idealization claimed, ~~still below `C_THR`=0.005~~ but without
   the "four-plus orders" margin that idealization asserted.

   **CORRECTED AT PHASE 5 (p5 docket 11), and VISION's V4 upheld:** the
   "still below `C_THR` = 0.005" clause is **wrong twice over**. The rim
   **amplitude** (9.99×10⁻³) is *above* `C_THR`, not below; only the
   **intensity** (9.98×10⁻⁵) is below. And comparing a *source-plane field
   residual* to a *Weber contrast threshold* is a **category error in either
   direction** — they are not the same kind of quantity, so neither comparison
   licenses a conclusion. The truncation numbers stand; the `C_THR`
   comparison is **withdrawn**. That the Phase-2 docket's own re-authored
   sentence recreated here exactly the defect the same docket fixed at A1 is
   the finding, and `C_THR`'s own source comment is carried verbatim at this
   locus as it is at A1: *"VISION's T2 photopic C_thr — context only, this leg
   scores no perceptual pass/fail"*.

   The aimed leg
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

   **VALIDITY CONDITIONS ATTACHED AT PHASE 5 (p5 docket 15), THERMODYNAMICS
   upheld.** A fill factor below unity *also* lowers κ_eff, raising
   **Bi = k_air/κ_eff toward unity — 0.25 / 0.75 / 0.97 at φ = 0.5 / 0.1 /
   0.01** under the Maxwell–Garnett mixing rule κ_eff = k_air(1+2φ)/(1−φ) —
   and **invalidating the lumped single-τ model the sensitivity row's own
   numbers come from**. THERMO's framing, adopted verbatim: *the sensitivity
   table offered as reassurance is evaluated at fill fractions where the model
   that produced its numbers is no longer licensed, and the reassurance is
   largest precisely where the model is most invalid.* The ΔT **classification
   is unaffected** — internal gradients make the radiating surface cooler, not
   warmer, so detectability gets more conservative — the **τ_thermal numbers
   are** what is affected, which is why this is a T23 finding (Learned #6) and
   not a ΔT finding. `biot_number` and `knudsen_number` are now stored per row
   under the stated mixing rule, and the same sentence is carried to
   `REALIZABILITY_MEMO.md` Amendment 5(b) and `fill_factor_disclosure`.

   **Emissivity, with the computed magnitude (p5 docket 16), MATERIALS
   partly upheld.** At the mixed regime the radiative channel is
   **4εσT³ = 5.1426 W/(m²K)** against **h_eff = 11111.11 W/(m²K)** — a
   **0.0463%** share of dP/dT. So the absurd bound **ε → 0 inflates `dt_ss`
   by 1.000463× and moves the mixed-regime NETD margin 607.33× → 607.05×.**
   MATERIALS' review states ε_corr = 0.1 "only inflates `dt_ss_full` by up to
   ~4×"; the true figure is **1.0004×** — wrong by ~4 orders of magnitude, in
   the safe direction, so its *conclusion* holds a fortiori. **The computed
   number is recorded, not the estimate.** Its actual finding stands:
   idealization 7's "dilution is uniformly conservative" framing omits a
   third, opposite-signed consequence already flagged in
   `lab/thermo_sidecar.py:151-153` since exp-033. Note also that
   `netd_disposition`'s own `emissivity_correction` is a multiplier **on** ΔT
   (`lab/thermo_sidecar.py:205`), so on the *detector* side lower emissivity
   is strictly conservative — the two sides push opposite ways and both are
   negligible here. **No UNDETECTABLE classification anywhere across the
   2496 + 42 + 250 points is threatened by either concern**, with four orders
   of margin to spare. Fill factor cannot touch `dt_ss` at all: mass and ρC_P
   do not appear in it.
8. **Block C's OFF gap uses a hard k_f = 0** — exp-045's own disclosed
   idealization, unchanged so the new points are comparable to its Host-D
   four.
9. **Bench-scale, not witness-scale.** T8/T13's near-field→witness bridge is
   unresolved; no ΔT or C here extrapolates to 45 m.
10. **NETD is an instrument/detector threshold, not a human perceptual one**
    — stored per point at ~~all 2496 + 42 + 250 points~~ AND inlined at every
    point of claim in this file and in `run.py`'s console output (docket 21:
    the loci that have actually failed twice, not storage, which
    `lab/thermo_sidecar.py:215` already auto-fills).

    **COUNT CORRECTED AT PHASE 5 (p5 docket 13):** the true figure is
    **2672 `netd_disclaimer` keys**, computed on the serialized document
    rather than asserted (`phase5_erratum.netd_disclaimer_coverage_corrected`).
    The **250 duration-scan points carry no NETD classification and need
    none** — they scan a memory ratio, not a temperature. 2496 (Block-B
    regrowth) + 42 (Block-C point runs) do.
11. **FDTD settling.** exp-041's 1400 steps and its λ-dependent causal
    transit margin (13.0/9.8/7.8 periods at 450/600/750 nm) are inherited
    unchanged; the margin is thinnest at 750 nm, which is leg A-v4 — the
    worst A5 residual (5.68%). Disclosed, ~~still-untested confound, and now
    the **fifth** consecutive cycle in which the dedicated settling-margin
    test is not run~~.

    **CREDITED AT PHASE 5, not deferred a sixth time** (Red Team §7,
    "Settling", adopted here alongside the numbered docket and disclosed as
    an extra): ELECTROMAGNETISM *ran* it. STEPS 1400→2800→4200 moves A-v4 by
    **0.083%** and A-v1 by **0.036%**; source-aperture extension 0.06%/0.01%;
    exact Hankel vs asymptotic 0.031%. **Settling is ruled out as the A-v4
    confound for the two informative legs**, and this idealization is closed
    for them rather than repeated as a deferral count. *(Cited as EM's
    measurement, not re-run this shift — this close carries no new FDTD
    budget.)* What replaces it as the live A-v4 question is the `ABSORB`
    systematic in Learned #8.
12. **A-unaimed's beam walks off the object window** by 162–187 cells while
    the object window is ±78 cells wide. That is a property of the geometry,
    not a defect — and it is why A1 is a pointing reading (docket 5).
13. **Sign-convention guard (docket 15).** exp-042's analytic `B(y)` is
    globally negative; `lab.ambient.observer_profile` is positive. `weber` is
    invariant under a global sign flip, so only `weber`-reduced scalars cross
    code paths here — enforced by `_weber_of` being the only route from any
    profile to any compared number.
14. **Post-freeze edits to `run.py`, disclosed rather than silent.**

    **THIRD CLASS ADDED AT THE PHASE-5 CLOSE, and the byte-identity claim
    below is now FALSE and is corrected here rather than left standing.**
    Applying the Phase-5 docket changed `run.py` in ways `--predict-only`
    prints, so its stdout is **no longer byte-identical to
    `predictions_frozen.txt`**. What is unchanged, and what is not:

    - **No pre-registered band's numeric content moved, and no measured desk
      quantity moved.** Verified by diffing `--predict-only`'s output against
      `predictions_frozen.txt` line by line: **not one number differs.**
      Exactly one of the 18 band strings changed at all, and only in its
      parenthetical attribution — A3's `"…≤4% at all 9 FWHM=20° cells (taper
      truncation)"` → `"…(residual explained by QUANTUM's closed form
      1/√(1−4σ_θ²tan²θ₀) … NOT taper truncation, which is refuted)"`, which
      *is* p5 docket item 7. Everything else in the diff is **additions**
      (`gate_backing`, `phase5_flag`, `residual_attribution`, the A4 mechanism
      keys, B1's identity tag, and the lobe-census / n-convergence /
      chromatic / emissivity / Biot–Knudsen / T23 / item-24 records plus the
      Phase-5 console sections) together with the corrected
      `NETD_DISCLAIMER` wording and the corrected `exact_angular_spectrum_
      center` **post-run diagnostic** — which was never a prediction.
    - **All nine FDTD legs reproduce bit-identically** for the third
      execution of this shift — the determinism check is unaffected.
    - `predictions_frozen.txt` itself is **left exactly as committed at
      `a7eaaf8`**: it is the frozen record, and freezing means it does not get
      regenerated. The correct statement of the freeze is the **commit
      order** (`a7eaaf8` contains `run.py`, `predictions_frozen.txt` and stage
      16 with **no** `results.json`), which is structural and still holds.

    *(Original entry, as committed at Phase 4:)* **Two post-freeze edits to
    `run.py`, disclosed rather than silent.**
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

**Phase-5 mandatory-fix close: zero new FDTD calls.** `results.json` is
regenerated from the corrected code and **all nine FDTD legs reproduce
bit-identically for the third execution of this shift** — a further free
determinism check. Desk work rises from 5 s to ~38 s, entirely the new
36-cell n=41 vs n=401 angular-sampling convergence audit (p5 docket 8) and
the 36-cell effective-aperture lobe census (p5 docket 6). The suite's own
stage 16 gains a fifth, desk-only gate at zero FDTD cost. Every FDTD number
Red Team cites but this close does not re-run (`rt_extreme.py`'s 28.03-cell
gate mis-fire, `rt_absorb.py`'s four ABSORB legs, EM's settling sweep) is
attributed to its measurer and labelled as not re-measured here.
