"""exp-047 -- The Glare/Adaptation Tier-W Sidecar, panel Iteration 24.

Zero FDTD calls (desk-analytic, `lab.glare_sidecar`). Executes VISION
SCIENCE's Phase-1 proposal with Red Team's seven mandatory fixes applied
(ruling: proceed-with-mandatory-fixes -- see LOGBOOK.md Iteration 24 for
the full Phase 1-5 record). Closes docket #7's second and final half;
THERMO's own half (the witness-photometry table) closed at Iteration 20
(exp-043).

PREDICTIONS ARE PRINTED BELOW, BEFORE ANY SCORING RUNS (house discipline,
non-negotiable) -- this file is committed to git in that state before the
scoring loop's own output is captured into results.json.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))

from lab import glare_sidecar as gs

# --------------------------------------------------------- fixed inputs
# All sourced per LOGBOOK.md / experiments/020, /043's committed tables;
# citations restated inline (Red Team fix 2: exp-030 is Iteration 7, not 4).
L_B_BAND = [1.0e-5, 1.7e-4, 1.0e-3]      # cd/m^2: darkest / moonless-rural-central / brightest
P_BAND = [0.4, 0.5]
THETA_HOLD_BAND = [5.0, 10.0, 15.0]      # deg, "tracking" gaze regime
E_CEILING_LO, E_CEILING_HI = 553.08, 55172.22   # lx (stray_light_ceiling_lux corners)
E_FLOOR_LO, E_FLOOR_HI = 0.01, 0.1              # lx (Iteration-1 Red-Team-struck floor)
EFFICACY_LM_W = 300.0                    # exp-043, uncited
THETA_FIXED_SWEEP = [0.5, 5.0, 10.0, 20.0, 45.0, 90.0, 150.0]  # deg, "fixed-gaze" regime

# --------------------------------------------------- PREDICTIONS (frozen)
PREDICTIONS = """
P-G24-1 (no-glare LAB-bar baseline, informational): at L_B=1.7e-4 (moonless-
  rural central), zero glare, LAB bar -- FAIL at both p in {0.4,0.5}
  (glare load-bearing at this ambient sub-class). At L_B=1.0e-5 (darkest),
  zero glare -- PASS at p=0.5, MARGINAL-or-PASS at p=0.4.

P-G24-2 (PRIMARY HEADLINE -- bench-scale surrogate, NOT witness-scale
  Tier-W): "tracking" gaze regime, CEILING glare estimate, LAB (cued) bar.
  Predicted: PASS at every point in the full grid L_B x {1e-5,1.7e-4,1e-3}
  x p x {0.4,0.5} x theta_hold x {5,10,15}deg, evaluated at BOTH ceiling
  corners (E=553.08 and E=55172.22 lx) -- including the single worst-case
  combination (E=553.08 lx, theta_hold=15deg, L_B=1e-3, p=0.4).
  Falsifier, stated in advance: if the worst-case combination above
  returns FAIL or even MARGINAL, this prediction is REFUTED and the
  ceiling-estimate headline route does not hold robustly.
  Label per Red Team mandatory fix 1: any PASS here is
  "@@LABEL@@", never bare "Tier-W".

P-G24-3 (informational only, demoted per Red Team mandatory fix 7 --
  T7's un-error-banded ~1.5-1.9% chromatic red-growth and T21's
  un-error-banded angular fringe both sit inside this branch's margin):
  "tracking", FLOOR glare estimate, LAB bar. Predicted PASS at L_B<=1.7e-4
  AND theta_hold<=10deg (both p); MARGINAL-or-FAIL at theta_hold=15deg
  (p=0.4) and at L_B=1e-3 (p=0.4). NOT part of the headline commitment
  (P-G24-2) regardless of outcome.

P-G24-4 ("fixed-gaze" qualitative check, informational, no PASS/FAIL
  scoring -- no quantitative Crawford L_eq(t) time-integration exists in
  this module, per idealizations): L_v(theta) computed across
  theta in [0.5,150]deg at both E extremes. Predicted: L_v collapses by
  2+ orders of magnitude between theta=0.5deg and theta=45deg at every E.
  Argued (not computed) resolution: because a single witnessed sweep-pass
  duration (order 1-10s) is short relative to Crawford-class cone/mesopic
  recovery time constants (order several-to-tens of seconds, NOT
  independently re-verified via WebFetch this cycle -- T18 blocked), the
  PHYSIOLOGICAL L_eq(t) does not track this instantaneous geometric
  collapse -- an argued, not demonstrated, resolution of Red Team's
  original Iteration-1 sweep-phase objection.

P-G24-5 (ocular exposure disposition, NEW this cycle per Red Team
  mandatory fix 5, no prior scoring convention exists for this quantity):
  single-pass corneal irradiance at both E floor and ceiling extremes,
  informational, NOT scored against any constraint. Session-accumulated
  dose over multiple sweep passes explicitly flagged as an OPEN QUESTION,
  not computed here.

P-G24-6 (identity/regression, code self-consistency): trust-suite stage
  17, 17/17 gates, must be green before any number above is trusted.
""".replace("@@LABEL@@", gs.TIER_W_HEADLINE_LABEL)

print(PREDICTIONS)

# ------------------------------------------------------------- scoring


def score_grid(theta_band, e_values, bar="lab"):
    rows = []
    for L_B in L_B_BAND:
        for p in P_BAND:
            for theta in theta_band:
                for E in e_values:
                    l_v = gs.stiles_holladay_veiling_luminance(E, theta)
                    verdict = gs.tier_w_verdict(gs.C_MEASURED, l_v, L_B, p, bar=bar)
                    verdict.update({"theta_hold_deg": theta, "e_lux": E})
                    rows.append(verdict)
    return rows


def summarize(rows):
    classes = {r["classification"] for r in rows}
    worst = max(rows, key=lambda r: r["abs_c_eff_over_thr"])
    return {
        "n_points": len(rows),
        "classes_seen": sorted(classes),
        "all_pass": classes == {"PASS"},
        "worst_case": worst,
    }


results = {
    "citation": gs.C_MEASURED_CITATION,
    "c_measured": gs.C_MEASURED,
    "witness_scale_realizability": gs.WITNESS_SCALE_REALIZABILITY,
    "headline_label": gs.TIER_W_HEADLINE_LABEL,
}

# P-G24-1: no-glare baseline, LAB bar.
baseline_rows = []
for L_B in L_B_BAND:
    for p in P_BAND:
        v = gs.tier_w_verdict(gs.C_MEASURED, 0.0, L_B, p, bar="lab")
        baseline_rows.append(v)
results["p_g24_1_baseline"] = baseline_rows

# P-G24-2: tracking, ceiling estimate, LAB bar (headline).
ceiling_rows_lab = score_grid(THETA_HOLD_BAND, [E_CEILING_LO, E_CEILING_HI], bar="lab")
results["p_g24_2_tracking_ceiling_lab"] = ceiling_rows_lab
results["p_g24_2_summary"] = summarize(ceiling_rows_lab)

# Context only (never headline): same grid, field bar.
ceiling_rows_field = score_grid(THETA_HOLD_BAND, [E_CEILING_LO, E_CEILING_HI], bar="field")
results["context_tracking_ceiling_field"] = summarize(ceiling_rows_field)

# P-G24-3: tracking, floor estimate, LAB bar (informational, demoted).
floor_rows_lab = score_grid(THETA_HOLD_BAND, [E_FLOOR_LO, E_FLOOR_HI], bar="lab")
results["p_g24_3_tracking_floor_lab"] = floor_rows_lab
results["p_g24_3_summary"] = summarize(floor_rows_lab)

# P-G24-4: fixed-gaze L_v(theta) sweep, informational.
fixed_gaze = []
for E in (E_CEILING_LO, E_FLOOR_LO):
    for theta in THETA_FIXED_SWEEP:
        l_v = gs.stiles_holladay_veiling_luminance(E, theta)
        fixed_gaze.append({"e_lux": E, "theta_deg": theta, "l_v_cdm2": l_v})
results["p_g24_4_fixed_gaze_sweep"] = fixed_gaze
lv_at_05 = next(r["l_v_cdm2"] for r in fixed_gaze if r["e_lux"] == E_CEILING_LO and r["theta_deg"] == 0.5)
lv_at_45 = next(r["l_v_cdm2"] for r in fixed_gaze if r["e_lux"] == E_CEILING_LO and r["theta_deg"] == 45.0)
results["p_g24_4_collapse_orders_of_magnitude"] = (lv_at_05 / lv_at_45)

# P-G24-5: ocular exposure disposition, informational.
results["p_g24_5_corneal_irradiance_mwcm2"] = {
    "floor_lo": gs.corneal_irradiance_wcm2(E_FLOOR_LO, EFFICACY_LM_W) * 1000.0,
    "floor_hi": gs.corneal_irradiance_wcm2(E_FLOOR_HI, EFFICACY_LM_W) * 1000.0,
    "ceiling_lo": gs.corneal_irradiance_wcm2(E_CEILING_LO, EFFICACY_LM_W) * 1000.0,
    "ceiling_hi": gs.corneal_irradiance_wcm2(E_CEILING_HI, EFFICACY_LM_W) * 1000.0,
    "note": ("single-pass instantaneous only; session-accumulated dose over "
             "multiple sweep passes is an OPEN QUESTION, not computed here "
             "(Red Team mandatory fix 5)"),
}

# ---- scored predictions
worst_ceiling = results["p_g24_2_summary"]["worst_case"]
p_g24_2_confirmed = results["p_g24_2_summary"]["all_pass"]
print(f"\nP-G24-2 worst-case point: theta_hold={worst_ceiling['theta_hold_deg']}deg, "
      f"E={worst_ceiling['e_lux']:.2f}lx, L_B={worst_ceiling['l_b_cdm2']:.2e}, p={worst_ceiling['p']}, "
      f"|C_eff|/C_thr={worst_ceiling['abs_c_eff_over_thr']:.3e}, class={worst_ceiling['classification']}")
print(f"P-G24-2 (headline): {'CONFIRMED' if p_g24_2_confirmed else 'REFUTED'} "
      f"({results['p_g24_2_summary']['classes_seen']} seen across "
      f"{results['p_g24_2_summary']['n_points']} points)")

results["p_g24_2_scored"] = "CONFIRMED" if p_g24_2_confirmed else "REFUTED"

out_path = os.path.join(HERE, "results.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2, default=str)
print(f"\nwrote {out_path}")
