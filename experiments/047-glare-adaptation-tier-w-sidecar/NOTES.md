# exp-047 — The Glare/Adaptation Tier-W Sidecar

**Panel Iteration 24.** Lead seat: VISION SCIENCE (Phase 1), per the
Iteration-23 hardened, unconditional rule — this item MUST run this cycle
or Checkpoint criterion 4 fires automatically. Full Phase 1–5 record:
`LOGBOOK.md` Iteration 24. Closes docket #7's second and final half;
THERMO's own half (the witness-photometry table) closed at Iteration 20
(exp-043).

## Hypothesis

The already-established, static `graded_black_shell` absorber — the same
object clearing constraints 1 and 2 to the camera floor since exp-001 —
clears the bench-scale glare-diluted SURROGATE of constraint 3's Tier-W
clause (never bare "Tier-W" — see below) once the flashlight holder's own
self-glare is priced into both the adapting-luminance threshold and the
measured contrast itself, under the "tracking" gaze regime. No new
mechanism, no switching, no new material: only the observer/adaptation
half of the scoring rule changes.

**Bench-scale surrogate, not a witness-scale verdict** (Red Team's central
mandatory fix, below): the C value composed here is a near-field bench
measurement; the program's own T8/T13/T14 threads show a real, unresolved
gap between bench-scale and witness-scale readings of this same object.
Every headline claim below is labeled accordingly.

## Panel record summary

**Phase 1 (VISION SCIENCE):** proposed composing two standard disability-
glare relations — Stiles–Holladay veiling luminance `L_v=10E/θ²`
(Holladay 1926; Stiles 1929) and the CIE-family veiling-contrast dilution
`C_eff=C/(1+L_v/L_B)` — onto the corrected, floor-cleaned bench contrast,
scored against the frozen `C_thr(L)` (T2). Self-flagged five conflicts,
including that E-at-eye and the glare angle were never actually sourced
despite PLAN.md's queue text implying they were.

**Phase 2 (five blind seats + Red Team):** all five seats returned
support-with-changes; Red Team ruled **proceed-with-mandatory-fixes**.
Two catches were load-bearing:

- **ELECTROMAGNETISM** (extended by Red Team into attack 1, the central
  finding of the cycle): the proposal's §5 idealizations state "bench-
  scale only, T8/T13 bridge untouched," but §4's headline language
  claims the absorber "clears Tier-W" — and PANEL.md's own Tier-W
  definition requires holding "in the reported scene's own regime," i.e.
  witness scale. A calculation scoped to bench-scale by its own admission
  cannot simultaneously claim to clear a tier defined at witness scale.
  Also caught a citation error: the cited "Iteration 4 close (exp-030)"
  is wrong — exp-030 is Iteration 7's close (Iteration 4 is exp-027, an
  unrelated diagnostic cycle). Both independently re-verified by Red Team
  directly against `LOGBOOK.md`.
- **Red Team's own catch, missed by all five blind seats** (attack 4):
  Tier-W's definition names the observer as "the flashlight holder" — the
  maximally *cued* case. The frozen threshold ladder's two bars are not
  interchangeable: lab=0.005 is the cued bar, field=0.02 is the *uncued*
  bar (`experiments/020-ambient-baseline/NOTES.md`). The proposal never
  stated which bar its headline verdicts used — load-bearing for exactly
  the fragile MARGINAL branch.

Other adopted fixes: MATERIALS' realizability gap (`graded_black_shell`
has never been formally scored by `REALIZABILITY_MEMO.md`; its own
Iteration-7 Phase-5 record carries an informal UNOBTANIUM call for a
witness-scale realization); THERMODYNAMICS' unaudited near-eye ocular
exposure at the ceiling estimate; QUANTUM OPTICS' threshold-transfer
caveat (narrowed to "unverified for localized/near-field glare
specifically," not "diffuse ambient only," per Red Team's correction);
PHOTONICS' chromatic/fringe uncertainty (demotes the FLOOR-estimate
branch out of the headline commitment).

**Ruling: proceed-with-mandatory-fixes, all seven items adopted, none
overridden.** Full numbered attacks and ruling text: `LOGBOOK.md`
Iteration 24.

## Setup

`lab/glare_sidecar.py` (new module, trust-suite stage 17, 6 identity
gates, 17/17 green): implements `c_thr` (T2's frozen threshold function,
bar-explicit per mandatory fix 4), `stiles_holladay_veiling_luminance`,
`veiled_adapting_luminance`, `veiled_contrast` / `veiled_contrast_direct`
(EM's two algebraically-identical forms, cross-checked bit-exact),
`stray_light_ceiling_lux`, `corneal_irradiance_wcm2`, and `tier_w_verdict`
(the per-point PASS/MARGINAL/FAIL classifier, ratio thresholds ×0.5/×2 of
the bar).

`experiments/047-glare-adaptation-tier-w-sidecar/run.py`: scores a grid —
night-ambient `L_B` ∈ {10⁻⁵, 1.7×10⁻⁴, 10⁻³} cd/m² × `p` ∈ {0.4, 0.5} ×
`theta_hold` ∈ {5°, 10°, 15°} × the CEILING and FLOOR near-eye stray-light
bands, LAB (cued) bar as the Tier-W default, field bar computed only for
context. Also scores the "fixed-gaze" `L_v(θ)` sweep (informational, no
quantitative Crawford integration) and the new ocular-exposure
disposition (informational, single-pass only).

## Parameters (sourced, with corrected citations)

| Input | Value / band | Provenance |
|---|---|---|
| Measured absorber C | **−0.7209** | LOGBOOK **Iteration 7 close (exp-030)** — corrected citation (was mis-cited to Iteration 4 in Phase 1) |
| `C_thr(L)` | 0.005·max[1,(L/3)^−p], p∈[0.4,0.5]; field=lab×4 | T2 (exp-020, corrected exp-024); Blackwell 1946, Rose 1948, CIE 19/2, Adrian 1989 |
| Night-ambient `L_B` | {10⁻⁵, 1.7×10⁻⁴, 10⁻³} cd/m² | exp-020 NOTES.md (Roach & Gordon 1973) |
| Beam candela | [13827, 99310] cd | exp-043 NOTES.md |
| Luminous efficacy | 300 lm/W, uncited | exp-043 NOTES.md |
| Stray-light E, CEILING | [553.08, 55172.22] lx (corner identity, stage 17) | `f_spill·I/r_hold²`, f_spill∈[0.01,0.05], r_hold∈[0.3,0.5]m — NEW this cycle, uncited |
| Stray-light E, FLOOR | [0.01, 0.1] lx | Iteration-1 Phase-1 narrative, Red-Team-struck as unsourced; carried as sensitivity floor only |
| Glare angle θ_hold ("tracking") | {5°,10°,15°} | NEW this cycle, uncited anthropometric estimate |
| Witness-scale realizability of `graded_black_shell` | UNOBTANIUM (informal) | Iteration 7 (exp-030) Phase 5, MATERIALS, informal call — required shell thickness 0.31–0.92 m |

## Idealizations

- **Bench-scale surrogate, not witness-scale** — every headline PASS is
  labeled `gs.TIER_W_HEADLINE_LABEL`, never bare "Tier-W." The T8/T13/T14
  near-field→witness-scale bridge stays unresolved.
- No retinal/ocular PSF or pupil-constriction model.
- No quantitative Crawford `L_eq(t)` time-integration — qualitative
  ordering argument only (P-G24-4).
- Uniform-veiling assumption across object and flank windows.
- `C_thr(L)` applied at `L=L_eq` assumes adaptation-level alone governs
  threshold — glare-specific sensitivity loss beyond that is not modeled.
- θ_hold, f_spill, r_hold are new, uncited geometric estimates — the
  proposal's single largest evidentiary gap.
- Achromatic/V-weighted convention; static per-sweep-phase scoring, not a
  continuous percept model.
- Ocular exposure disposition (P-G24-5) is single-pass only;
  session-accumulated dose across a real multi-pass sweep session is an
  explicitly open question.
- `graded_black_shell`'s witness-scale realizability is carried as an
  informal call, not a formal `REALIZABILITY_MEMO.md` entry — a real gap,
  not resolved by this cycle.

## Predictions (committed before scoring — see `run.py`'s frozen
`PREDICTIONS` string, printed first, unmodified by the scoring loop)

- **P-G24-1** (baseline, informational): zero-glare LAB bar FAILS at
  L_B=1.7×10⁻⁴ both p; PASSES-or-MARGINAL at L_B=10⁻⁵.
- **P-G24-2** (PRIMARY HEADLINE — bench-scale surrogate): "tracking,"
  CEILING estimate, LAB bar — PASS at every grid point, including the
  worst case (E=553.08 lx, θ_hold=15°, L_B=10⁻³, p=0.4). Falsifier:
  any FAIL or MARGINAL anywhere in the grid refutes this headline.
- **P-G24-3** (informational, demoted out of the headline per Red Team
  fix 7): "tracking," FLOOR estimate, LAB bar — PASS at L_B≤1.7×10⁻⁴ and
  θ_hold≤10°; MARGINAL-or-FAIL at θ_hold=15°(p=0.4) and L_B=10⁻³(p=0.4).
- **P-G24-4** (informational, no scoring): L_v(θ) collapses 2+ orders of
  magnitude by θ=45°; argued (not computed) resolution via Crawford
  recovery ≫ sweep duration.
- **P-G24-5** (informational, no scoring): corneal irradiance reported at
  both E extremes; session-accumulated dose flagged open.
- **P-G24-6**: trust-suite stage 17, 17/17 green, gates every number
  above.

## Results

Trust suite: 58/58 (`--only 12346789,17`) before this experiment's own
run. `run.py` executed cleanly, zero exceptions (one pre-run bugfix: a
Python `.format()`/literal-brace collision in the predictions banner,
caught and fixed before any scoring output existed — the predicted TEXT
itself was not altered). Full per-point data: `results.json`.

**Scorecard: 4 CONFIRMED, 2 PARTIAL, 0 REFUTED.**

- **P-G24-1 (baseline) — PARTIAL.** L_B=1.7×10⁻⁴, LAB bar: p=0.4 FAILs as
  predicted (ratio 2.886×); p=0.5 lands **MARGINAL** (ratio 1.085×), not
  the predicted FAIL — close to the bar but not an exact match.
  L_B=1.0×10⁻⁵: p=0.5 PASSes (0.263×) and p=0.4 is MARGINAL (0.929×),
  both inside the predicted "PASS / MARGINAL-or-PASS" band. 5 of 6
  sub-points hit exactly; 1 landed one class softer than predicted.

- **P-G24-2 (PRIMARY HEADLINE) — CONFIRMED, robustly.** All 36 grid
  points (L_B × p × θ_hold × {E_ceiling_lo, E_ceiling_hi}) classify
  **PASS** at the LAB (cued) bar. Worst-case point: θ_hold=15°,
  E=553.08 lx (the ceiling band's *low* edge — correctly the hardest
  case, since larger E dilutes contrast further), L_B=10⁻³ (brightest
  night-ambient sub-class), p=0.4 — `|C_eff|/C_thr = 5.865×10⁻³`, i.e.
  **PASS by a margin of ~170×**, not a near-miss. The absorber **clears
  the bench-scale glare-diluted SURROGATE of Tier-W, pending the
  T8/T13/T14 near-field-to-witness-scale bridge — NOT a witness-scale
  constraint-3 verdict** (Red Team mandatory fix 1's exact required
  language) under the "tracking" gaze regime at the ceiling glare
  estimate, across the full committed night-ambient band and both p.
  Context only, never headline: the same grid at the FIELD (uncued) bar
  is also all-PASS, with an even larger margin (worst ratio 1.47×10⁻³)
  — unsurprising since field is 4× more lenient, and explicitly not the
  bar Tier-W's cued-observer definition licenses as primary.

- **P-G24-3 (informational, demoted per Red Team fix 7 — never part of
  the headline commitment) — PARTIAL.** Of the 16 points at L_B≤1.7×10⁻⁴
  and θ_hold≤10°, 15 PASS as predicted; one (L_B=1.7×10⁻⁴, p=0.4,
  θ_hold=10°, E=0.01 lx — the single hardest combination inside that
  sub-grid) lands MARGINAL (ratio 0.907×) rather than PASS. At
  L_B=10⁻³/p=0.4 (the branch predicted MARGINAL-or-FAIL): confirmed —
  every θ_hold from 5° to 15° at E=0.01 lx classifies FAIL (ratios
  2.23×–4.70×), softening to MARGINAL at E=0.1 lx. At θ_hold=15°/p=0.4
  specifically: the darkest ambient sub-class (L_B=10⁻⁵) still PASSes at
  both E — this cycle's own prediction wording did not clearly exclude
  that cell, an ambiguity in the prediction text itself, not a modeling
  surprise (see Learned). Net picture matches the proposal's own
  characterization: "genuinely sensitive, not robust" — correctly kept
  out of the headline.

- **P-G24-4 (fixed-gaze, informational) — CONFIRMED.** L_v collapses by
  **8100×** (≈3.9 orders of magnitude) between θ=0.5° and θ=45° at the
  ceiling-estimate E — comfortably past the predicted "2+ orders."
  Resolution argument (Crawford recovery ≫ single sweep-pass duration)
  remains argued, not computed — no quantitative L_eq(t) integration
  exists in this module, as disclosed.

- **P-G24-5 (ocular exposure, informational, new) — CONFIRMED /
  reported.** Single-pass corneal irradiance: floor 3.3×10⁻⁶–3.3×10⁻⁵
  mW/cm²; **ceiling 0.184–18.39 mW/cm²** — the upper figure matches
  THERMO's independent Phase-2 arithmetic (18.4 mW/cm²) to 4 significant
  figures, now also a trust-suite regression anchor (stage 17, gate 6).
  Session-accumulated dose over a real multi-pass sweep remains an open
  question, not computed here, exactly as flagged.

- **P-G24-6 (identity/regression) — CONFIRMED.** Trust-suite stage 17:
  17/17 green. Full fast suite with it: 58/58 green.

## Phase 5 (six fresh blind seats + Red Team audit)

**Six independent reviews, verdicts: 4 PROMISING (VISION, PHOTONICS, EM,
QUANTUM), 2 PARTIAL (MATERIALS, THERMO — each scoped to one open item in
their own charter, neither finding a defect in the claim itself). Red
Team's own independent verdict: PROMISING**, re-derived from source, not
inherited from the vote count — P-G24-2 CONFIRMED with a 170× margin,
17/17 gates, all 7 Phase-2 mandatory fixes verified actually shipped.

**Does anything found at Phase 5 threaten the headline (P-G24-2)? No —
independently re-confirmed by Red Team from source.** PHOTONICS proved a
hard closed-form bound: at the worst-case grid point, `c_thr` is pinned at
its photopic floor independent of `C`, so scaling `|C|` to its *physical
ceiling* of 1.0 only moves the worst ratio to 0.00814 — still 61× below
MARGINAL and 246× below FAIL. No possible correction to `C_measured`
(chromatic, fringe, or realizability-driven) can flip it.

**What Phase 5 found instead — all confined to the surrounding record,
now fixed same-shift where cheap:**

1. **VISION caught a real slip Phase 2's own fix didn't fully reach**:
   this NOTES.md's own Hypothesis section (line 14, before the fold) used
   bare "Tier-W" language — textually the exact overclaim Red Team's
   mandatory fix 1 exists to prevent, never propagated to code/
   `results.json` (confirmed clean there by both VISION and, separately,
   EM), but present in the single most-skimmed prose locus. **Fixed
   same-shift** (see Hypothesis section above). This revises the earlier
   "caught at Phase 2, not Phase 5" self-assessment in this file's first
   draft — it was NOT a clean instance; the failure class recurred one
   level down, inside the very NOTES.md written to fix it.
2. **MATERIALS' major finding, independently confirmed by Red Team from
   source**: `C_MEASURED` is drawn from the SELF-SIMILAR-SCALED
   `graded_black_shell` construction — the exact construction this
   program's own Iteration-7 record already names UNOBTANIUM at witness
   scale. A fixed-absolute-thickness variant (the physically plausible
   alternative) has been proposed since Iteration 7 and never built or
   measured, at any scale. Sharper than "bench≠witness" (already known,
   T8/T13/T14): the specific evidence is the signature of the already-
   unrealizable construction. Elevated by Red Team to Tier-0 for
   Iteration 25.
3. **A citation-provenance drift, caught by MATERIALS, confirmed by Red
   Team**: `WITNESS_SCALE_REALIZABILITY`'s figure (0.31–0.92m) was
   attributed to "MATERIALS seat, informal call" when it was actually a
   correction of MATERIALS' OWN unit error, made by Red Team at Iteration
   7. **Fixed same-shift** (`lab/glare_sidecar.py`).
4. **EM's extrapolation-range finding, independently re-derived by Red
   Team to 5+ significant figures**: the headline grid's `L_v/L_B` ratio
   spans ~2.5×10⁴×–2.2×10⁹× — far outside the road-lighting/automotive
   glare literature's typical calibration range (small integers to low
   hundreds). Doesn't threaten PASS (the formula's washout direction is
   fixed by construction, cannot reverse), but the "170× robust margin"
   partly reflects extrapolating the model far past empirical support,
   not fresh physical confirmation. **Disclosed same-shift** (docstring).
5. **PHOTONICS found T21's fringe contamination has never been bounded at
   the ACTUAL ±35° fallback geometry `C_MEASURED` uses** (only at ±40°,
   where T21 was discovered) — doesn't threaten the headline (per the
   closed-form bound above) but threatens any non-headline use of this
   constant (P-G24-1/P-G24-3). Queued for Iteration 25, not same-shift
   (requires a real FDTD resweep).
6. **THERMO found the ocular-exposure disclosure (P-G24-5) had zero
   magnitude context** — no comparison anchor, no source-geometry
   caveat. **Fixed same-shift** (`corneal_irradiance_wcm2` docstring: the
   ~100 mW/cm² solar-irradiance anchor and the "not a hazard assessment"
   caveat).
7. **PHOTONICS and Red Team independently found a second, uncredited
   achromaticity assumption**: `stiles_holladay_veiling_luminance`
   treats near-eye illuminance as spectrally flat — distinct from
   `C_MEASURED`'s own V-weighting, and this program has caught this exact
   "achromatic by construction" overclaim pattern before (Iteration 20).
   **Fixed same-shift** (docstring).
8. **Red Team's own catch, missed by all six blind seats**: P-G24-4's own
   informational sweep evaluates θ=0.5°, below the module's own stated
   1.0° validity floor for the Stiles–Holladay formula — physically the
   more dangerous direction (L_v diverges as θ→0). Non-load-bearing
   (informational only). **Disclosed same-shift** (docstring).
9. **VISION and QUANTUM independently converged** on the `[0.5,2.0]`
   MARGINAL classification band being an unsourced, round convention that
   quietly absorbs real uncertainty exactly where it matters most (near-
   boundary points, e.g. ratio=1.085). Not load-bearing this cycle;
   queued for Iteration 25.

**Red Team's ranked priorities for Iteration 25** (adopted in full by the
Director): (1) formal `REALIZABILITY_MEMO.md` entry for `graded_black_shell`
at witness scale, naming the construction/evidence-base link. (2) T21
fringe-contamination bound at the actual ±35° geometry. (3) [done
same-shift, see above — the three cheap prose/citation/disclosure fixes].
(4) Source or retire the MARGINAL band convention. (5) Build and measure
the fixed-absolute-thickness `graded_black_shell` variant (MATERIALS'
eight-iteration-deferred pick). (6) Resume standing queue: QUANTUM's
n-convergence audit, stage-16 forward half, T24 ABSORB sweep.

## Learned

- The panel's own mandatory-fix discipline caught a real overclaim risk
  (bare "clears Tier-W" language) at Phase 2 — but a residual instance of
  the SAME failure class survived into this very NOTES.md's own prose
  until Phase 5 caught it (see above). The failure class (a corrected
  scope tag not propagating to every locus) is now confirmed recurrent
  even inside the document written to fix it — the sharpest instance yet
  of this program's own repeated lesson (Iterations 17, 20, 21, 22, 23).
- Red Team's own attack (the cued/uncued bar ambiguity, Phase 2) and its
  own Phase-5 catch (the small-θ validity gap, missed by all six blind
  seats) both landed on things no blind seat found — the panel's
  independence mechanics doing real work, not formal ritual.
- MATERIALS' Phase-5 finding — the headline's own evidence base is drawn
  from a construction already named unrealizable — is the single most
  consequential result of this cycle's review, sharper than the already-
  known bench/witness scale gap, and does not threaten the (correctly
  narrowly-scoped) headline itself.
- The headline (P-G24-2) came back far more robust than its own
  pre-registered worst case demanded (~170× margin, not a near-miss),
  and PHOTONICS proved a hard closed-form bound (61×/246× margin even at
  the physical |C| ceiling) — the informational FLOOR branch (P-G24-3) is
  where the real fragility lives, exactly as predicted and correctly kept
  out of the headline. EM's extrapolation-range finding tempers HOW that
  robustness should be read (it's partly an artifact of scoring far past
  the underlying literature's calibration range) without overturning it.
- Minor process note: P-G24-1 and P-G24-3's own prediction text used
  informal set-notation ("MARGINAL-or-FAIL at theta_hold=15deg (p=0.4)
  and at L_B=1e-3 (p=0.4)") that reads ambiguously as either an AND or an
  OR across the full grid — a real instance of the imprecise-prediction-
  wording pattern this program has flagged before (informational-only
  here, so non-load-bearing, but worth tightening in any future
  cycle's prediction text: state set-membership as an explicit grid
  subset, not natural-language shorthand).

## Next

Red Team's Phase-5 ranked priorities for Iteration 25 (adopted in full):

1. **`REALIZABILITY_MEMO.md` formal entry for `graded_black_shell` at
   witness scale**, naming the self-similar-construction/evidence-base
   link explicitly — now Tier-0, MATERIALS' finding.
2. **T21 fringe-contamination bound at the actual ±35° fallback
   geometry** — PHOTONICS' finding, cheap (reuses exp-042's own committed
   propagator), closes the one open gap in the headline's own evidentiary
   chord (does not threaten the headline itself).
3. Source or retire the `[0.5,2.0]` MARGINAL classification band
   convention (VISION/QUANTUM) — not load-bearing this cycle, will be for
   any future near-boundary grid.
4. Build and measure the fixed-absolute-thickness `graded_black_shell`
   variant's own C — MATERIALS' eight-iteration-deferred Iteration-7
   pick, natural companion to item 1.
5. Session-accumulated ocular dose disposition (P-G24-5's open half,
   THERMO's own scoped-down next step) — cheap, zero-FDTD, not urgent.
6. Resume standing queue: QUANTUM's `gaussian_angle_weights`
   n-convergence audit (overdue, now confirmed zero contamination risk),
   stage-16's forward half, the T24 ABSORB sweep.

The T8/T13/T14 near-field→witness-scale bridge remains the single
biggest blocker on ever promoting this cycle's headline from "bench-scale
surrogate" to an actual Tier-W verdict — items 1, 2, and 4 above all
bear on it without requiring it to close first.
