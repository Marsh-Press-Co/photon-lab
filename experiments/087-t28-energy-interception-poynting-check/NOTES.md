# exp-087 — T28 Energy-Interception Cross-Check: a Purpose-Built Poynting-Box Measurement

Panel Iteration 64. Lead: THERMODYNAMICS (rotation). Discharges the
Iteration-63 forward tripwire (LOGBOOK.md, PLAN.md Tier 2 item 4): the
joint EM/THERMO energy-interception cross-check, named at Iteration 59
(exp-082), deferred/exempt four consecutive cycles (083–086) — a fifth
consecutive deferral without either a purpose-built article-loaded scene
or an explicit retirement of the deferral framing fires Checkpoint
criterion 4 automatically. Full phase record: `phase1_proposal.md` →
five blind Phase-2 critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM,
QUANTUM OPTICS, VISION SCIENCE, unanimous support-with-changes, zero
overlap) → `phase2_redteam_audit.md` (PROCEED-WITH-MANDATORY-FIXES,
10 items, zero overridden) → `phase3_synthesis.md` (this cycle's frozen
spec, all 10 fixes adopted).

## Hypothesis

The cross-check's originally-scoped shape (Iteration 59) was a zero-FDTD
sanity bound reusing T9's broadside `σ_abs/σ_ext=0.51` anchor —
never executed in any form across four subsequent cycles. This experiment
measures it instead: `lab/sections.py`'s already-stage-8-gated Poynting-box
ledger (`widths()`), never before applied to the T28 article-loaded scene,
runs on the same flagship-absorber-loaded C40/G40 (`PAIR_PAD`) geometry
exp-082/083 already built and validated, at a disclosed 3-angle subset of
the established 31-point window — fresh, scene-specific `σ_abs(θ)`/
`σ_ext(θ)` for both PAD configs, at real oblique incidence, for the first
time. Hypothesis: the article's real absorbed-power PAD-sensitivity
(`frac_p_abs`) is decoupled from (much smaller than) the already-measured
Weber-contrast PAD-sensitivity (`frac_contrast`, cited from exp-083) —
consistent with ten-plus cycles of convergent evidence that this
sub-thread's own confound is a phase/interference effect, not an
energy-budget one — but this is a genuine, falsifiable measurement, not a
foregone conclusion, and a CONSISTENT/ENERGY-DOMINANT/MIXED finding would
be a materially new, immediately actionable result.

## Setup

`experiments/087-.../run.py` reuses exp-083's `_load()` idiom to import
`dg069` (→`dg065.CONFIGS["C40"]`/`["G40"]`), `build_article`, `_run_sim`
**verbatim, unmodified** — zero geometry retyped. New code: `BOX_A`/`BOX_B`
Poynting boxes (exp-024's `BOX_CLEARANCE=12` convention, doubled for
`BOX_B`, translated per config's own PAD shift) and `REF` (exp-024's
`REF=(OBJ_X,OBJ_Y,80)` convention); `sc.widths()` calls at both boxes for
every (config, angle, leg); the `xi_ext` extinction-routes-agreement gate
(Phase 2 mandatory fix 1); `ts.absorbed_power_established_ratio` →
`ts.mixed_length_scale_regime` → `ts.netd_disposition` (reusing exp-043's
sourced witness irradiance and exp-057's thermal constants verbatim); a
synthetic classifier-recovery self-test (Phase 2 mandatory fix 4); a
non-negativity assertion (fix 7); and a settling spot-check
(STEPS=1400 vs 2800 at G40/38.6°, fix 5). 14 new FDTD calls total (12 main
+ 2 settling). Angle set: `{36.0°, 38.6°, 41.8°}`
(`dg069.DENSE_ANGLES[0,13,29]`) — non-uniformly spaced (2.6°, 3.2°) per
Phase-2 mandatory fix 2, replacing Phase 1's uniform 3.0° spacing after
Red Team confirmed it sat within 1.8% of exact aliasing against
`P*=2.9474°`, T28's own decisively-resolved dominant confound period.

## Idealizations

1. 3-angle subset (non-uniformly spaced, {36.0°,38.6°,41.8°}), not the
   full 31-point window.
2. Single λ=600nm, matching the rest of the T28 window.
3. `iso_xsec_sq` area convention (thermo_sidecar's own stated
   idealization): the object is treated as compact, not an infinite rod.
4. Silicon thermal constants (ρ, c_p) are ASSUMED, provenance unsourced
   (T18, `REALIZABILITY_MEMO.md`'s standing downgrade), reused verbatim
   from exp-057.
5. WitnessScenario irradiance/distance/candela are WebSearch snippet-tier
   (T18), reused verbatim from exp-043, not re-searched this cycle.
6. The `ratio_k` decade-scale tiers (0.1×/10×) are a deliberately wide,
   first-of-its-kind falsification band, not a rigorously derived
   confidence interval.
7. Settling of the `widths()`-derived channel is spot-checked once
   (one cell, STEPS=1400 vs 2800), not a full R3-grade convergence study —
   disclosed alongside the primary result, not gating it, matching
   exp-083's own precedent for the identical check on the Weber-contrast
   channel.
8. The 3× box-dev noise-floor multiplier is a house-style choice (mirrors
   R3's "survive a resolution change with margin" precedent); the
   synthetic recovery check (Idealization 12) validates the classifier's
   threshold LOGIC, not this specific numeric multiplier.
9. **NETD is an instrument/detector threshold, not a human-eye one** —
   any classification derived from this cycle's `dt_ss_full_K` does NOT
   bear on constraint-3/4's human-eye verdict.
10. **This cross-check bears only on T28's own confound-mechanism question
    and constraint-3's energy-ledger bookkeeping.** It does not test
    constraints 1/2/4, and does not re-open or re-score
    `REALIZABILITY_MEMO.md`'s verdict.
11. Not this cycle's mandate, named but not scored: the near-unanimous #1
    grazing-incidence validity check (`edge_diffraction_c_empty_corrected`,
    PHOTONICS' charter), the x-wall wavelength-generality leg (11 cycles
    deferred), the full-scale null-calibration re-run, and R12-into-
    standard-practice — real, overdue T28 board items for Iteration 65.
12. The synthetic classifier-recovery check (Phase-2 fix 4) validates the
    classification pipeline's own bucket logic at decade boundaries; it is
    NOT a null-permutation test against this run's own real data (R5's
    literal look-elsewhere machinery does not apply to a 3-point ratio
    comparison) and is not represented as one.

## Predictions (frozen, committed BEFORE any Phase-4 code runs — see
`phase3_synthesis.md` for full derivation, falsifiers, and the Phase-2
fix-by-fix mapping)

1. **P1 (vacuum-footprint precondition):** PASS at every `BOX_A`/`BOX_B`
   cell, both configs. HALT if it fails.
2. **P2 (reproduction precondition):** fresh `C_empty(cfg,θ)` at
   θ∈{36.0,38.6,41.8}° reproduces `experiments/083-.../results.json`
   exactly, max|Δ|<1e-9. HALT if it fails.
3. **P3 (box independence):** `box_dev_ext`/`box_dev_abs` reported at all
   6 (cfg,θ) cells, both legs — context, not gating.
4. **P4 (`xi_ext` verification gate, NEW):** predicted PASS (`≤0.12`) at
   every (cfg,θ,box,leg) cell, stated with only moderate confidence — a
   genuinely never-tested combination. HALT before P7 if violated anywhere.
5. **P5 (synthetic classifier-recovery check, NEW):** predicted PASS —
   the pipeline recovers the intended bucket at every decade-boundary
   synthetic test case.
6. **P6 (settling spot-check, NEW, disclosed not gating):** no
   pre-registered band; reported for context alongside P7.
7. **P7 (PRIMARY, pre-registered, falsifiable):** `ratio_k(θ) =
   frac_p_abs(θ)/frac_contrast(θ)` at each resolved angle, classified
   ENERGY-DECOUPLED (`<0.1` at every resolved angle) / CONSISTENT
   (`0.1–10` throughout) / ENERGY-DOMINANT (`>10` anywhere) / MIXED /
   DEGENERATE (<2 resolved angles). **Predicted: ENERGY-DECOUPLED at ≥2 of
   3 angles**, moderate confidence, corroborative not dispositive.
   Falsified by CONSISTENT, ENERGY-DOMINANT, MIXED, or DEGENERATE.
8. **P8 (scene-specific detectability):** `netd_disposition` predicted
   UNDETECTABLE at every (cfg,θ) cell. Pre-committed triage rule: any
   departure must be checked against this program's own already-measured
   material-identity swing magnitudes (~780× Biot, ~116× H_CONV) before
   being read as new physics.
9. **Non-negativity gate (hard assertion, not a scored prediction):**
   `sigma_abs≥0`, `p_abs_w≥0` everywhere. HALT if violated.

## Result

*(to be filled in after Phase 4 — not written before the run, per house
discipline)*

## Learned

*(to be filled in after Phase 5)*

## Next

*(to be filled in after Phase 5)*
