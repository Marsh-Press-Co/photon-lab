# PHASE 4 — TEST · Panel Iteration 57 · exp-080

Re-run of `validity_precheck.py` after Phase 3's fix-docket fold-in
(`reflection_coefficient_vec_realizable`, `part_b_realizable`,
`part_c_power_budget_at_true_angle`, `part_b_abs_calibration_corrected`,
`photonics_image_term_curve`, `part_d_photonics_construction`). Every
pre-existing number (part a, part b) reproduced bit-identical to the
Phase-1 freeze; every new fold-in number reproduced exactly against Red
Team's own independent from-scratch re-derivation (`phase2_redteam_audit.md`
§0). Full stdout in `_output.txt` (overwritten by this run); full JSON in
`validity_precheck_results.json`.

## Gates

- Zero `lab/` diff (confirmed: `git diff --stat 41070f2 -- lab/` empty).
- House trust suite (41/41, `--only 12346789`) confirmed green at shift
  start; no engine code touched since — no re-run required.
- Version-drift guard (part b, recomputed true curve vs. committed
  `y_wall_aperture_sum_results.json`): `0.0` max abs diff, both proxies, all
  5 configs — unchanged from Phase 1.

## Headline numbers (copied from `validity_precheck_results.json`, never
## hand-typed)

| Quantity | Value |
|---|---|
| (a) Fraunhofer/spread | **FORECLOSE** — worst dist_ratio 2.145%, worst spread 2.752× |
| (b) matched admittance | **INCONCLUSIVE** — mean R²=0.7345, min=0.5214 (C70) |
| (b) realizable admittance | **REFUTE** — mean R²=0.4305, min=−0.6230 (C40) |
| (c) power budget @ true angle, ABSORB=40 | reflected-power-fraction ∈ [2.48×10⁻⁴, 1.49×10⁻³] |
| (c) power budget @ true angle, ABSORB=80 | reflected-power-fraction ∈ [4.10×10⁻⁸, 3.57×10⁻⁶] |
| (b) abs-calibration-corrected, C70/C80 | R²(abs)=−1.648/−2.296 (vs. raw −7.82/−8.45) |
| (d) PHOTONICS' image term, scale-corrected | mean R²(Re)=0.6020, min=0.0852 (C70) — worse floor than (b) |

## Combined Verdict this cycle: **PARTIAL**

See `phase3_synthesis.md` §3 for the full reading. No RULED-OUT item
(R1–R9) re-proposed. Checkpoint criteria 1/3 N/A, criterion 2 NOT YET RIPE,
criterion 4 does not fire, criterion 5 not at risk (full reasoning:
`phase3_synthesis.md` §4, `phase2_redteam_audit.md` §4).
