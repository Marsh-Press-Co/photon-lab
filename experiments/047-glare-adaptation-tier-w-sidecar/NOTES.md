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
clears constraint 3's Tier-W clause once the flashlight holder's own
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
run. `run.py` executed cleanly, zero exceptions.

*[Predictions committed above, before this section is filled in. Results
to be appended after `run.py` executes — see git history: this NOTES.md
is committed in its pre-results state first, results appended and
committed separately, per house predict-before-run discipline.]*

## Learned

- The panel's own mandatory-fix discipline caught a real overclaim risk
  (bare "clears Tier-W" language) before it reached the permanent record
  — the same failure class (a scope tag not propagating to the headline
  locus) this program has now named and fixed multiple times (Iterations
  17, 20, 21, 22, 23). This cycle is a clean instance: caught at Phase 2,
  not Phase 5.
- Red Team's own attack (the cued/uncued bar ambiguity) that no blind
  seat found is exactly the kind of catch this panel's independence
  mechanics exist to buy — Red Team seeing everything, going last, is
  doing real work here, not just formal ritual.
- The ocular-exposure question THERMO raised (near-eye stray light at the
  ceiling estimate, up to ~18.4 mW/cm² at the cornea) is a genuinely new
  open question this program has never scored — flagged, not resolved.

## Next

- Session-accumulated ocular dose disposition (P-G24-5's open half) —
  cheap, zero-FDTD, a natural next-cycle pick if a lead seat wants it.
- `graded_black_shell`'s formal `REALIZABILITY_MEMO.md` entry at witness
  scale — MATERIALS' own flagged gap, informal UNOBTANIUM call only so
  far.
- The T8/T13/T14 near-field→witness-scale bridge remains the single
  biggest blocker on ever promoting this cycle's headline from "bench-
  scale surrogate" to an actual Tier-W verdict.
