"""exp-054 -- Panel Iteration 31: the h_eff length-scale re-derivation.

Phase 4 (TEST). Implements the design frozen in `NOTES.md`/
`phase3_synthesis.md` (Red Team's 7-item mandatory-fix docket, all
accepted). Zero new FDTD calls -- pure desk/analytic re-derivation from
already-committed bench measurements, matching the Iteration 20/22/25/27
sidecar-cycle precedent.

Two parts:
  (A) the ON-endpoint (tau=3.9) mixed-length-scale regime, via the NEW
      `lab.thermo_sidecar.mixed_length_scale_regime` (P-054-1/2).
  (B) exp-045's own Block C 8-point grid (Host D, 4 ratios x {5tau,0.5tau}),
      re-run through `coupled_segment_general` at the MIXED chain's own
      dt_ss_full/tau_thermal_s -- not the w_on-consistent pair Block C
      originally used (P-054-3a/3b/4).

`coupled_segment_general` and `coupled_kinetics_thermal_dT` are loaded via
`importlib.util` from `experiments/045-.../run.py` under a private module
name (exp-050's own precedent, `experiments/050-.../design_geometry.py:34-51`)
-- NOT re-derived, NOT copy-pasted. Only the two pure functions are used;
exp-045's own `main()` is never called (guarded by its own
`if __name__ == "__main__"`), so none of its heavy Block A/B/C computation
re-runs.
"""
import importlib.util
import json
import math
import os
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]


def _load(name, relpath):
    spec = importlib.util.spec_from_file_location(name, _REPO_ROOT / relpath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


exp045 = _load("_exp045_run", "experiments/045-intermediate-dwell-stress-hconv-rederivation/run.py")
coupled_segment_general = exp045.coupled_segment_general
coupled_kinetics_thermal_dT = exp045.coupled_kinetics_thermal_dT

from lab import thermo_sidecar as ts
from lab import kinetics as kin

HERE = os.path.dirname(os.path.abspath(__file__))

# ============================================================ shared inputs
# Reused VERBATIM, cited, not copy-pasted from local state (RATIOS/
# dwell_central are locals inside exp-045's main(), not importable; these
# exact values are exp-045's own established convention -- exp-045/run.py:
# 402 (RATIOS), :178 (dwell_central), :536 (k_r_d) -- and exp-043's own
# committed bench constants).
DX_M = 30.0e-9  # 600nm/cpl20 -- exp-043/run.py:167 equivalent
R_OUT_CELLS = 78  # exp-026/043's bench R_OUT -- exp-043/run.py:168 equivalent
R_OUT_M = R_OUT_CELLS * DX_M  # 2.34e-6 m
K_AIR = 0.026  # W/(m*K), textbook room-temp value -- exp-045/run.py:194
DENSITY_SI_KG_M3, C_P_SI_J_KGK = 2330.0, 700.0  # silicon -- ASSUMED, see below
EMISSIVITY = 0.9
T_AMBIENT_K = 293.15
NETD_BAND_K = (0.020, 0.050)  # exp-043/results.json::p_d7_4_netd
NETD_DISCLAIMER = (
    "NETD is an instrument/detector threshold, not a human perceptual one "
    "(VISION SCIENCE's standing mandatory fix, exp-043 Red Team attack 7, "
    "reaffirmed exp-054 Phase-2 mandatory fix 6). This classification does "
    "NOT bear on constraint-3/4's human-eye verdict.")
MATERIAL_PROVENANCE_NOTE = (
    "silicon rho=2330 kg/m^3, c_p=700 J/(kg*K), kappa=148 W/(m*K): "
    "ASSUMED -- provenance terminates unsourced (T18). REALIZABILITY_"
    "MEMO.md downgraded this identity from a plain sourced citation "
    "(exp-037/NOTES.md:828-829, which itself only says 'standard cited "
    "thermal constants' with no traceable DOI/handbook) at Iteration 25 "
    "(Red Team Attack 13 / MATERIALS M3). exp-054 restores that flag here "
    "per Phase-2 mandatory fix 3 (the Phase-1 draft had silently dropped "
    "it). mass_kg further assumes 100%-fill crystalline silicon at "
    "l_geometric_m, undisclosed in the Phase-1 draft, disclosed here.")

# exp-043 results.json::on_endpoint_tau_3p9 (ON-endpoint, tau=3.9, 600nm)
P_ABS_W_ON_CENTRAL = 2.0044347652689456e-12
P_ABS_W_ON_LO, P_ABS_W_ON_HI = 3.34e-13, 1.344e-11

# exp-045's own Block C grid (Host D, k_r_d=10.0, RATIOS, N_PULSES=5,
# dwell_central=10.0/150.0) -- reused verbatim, cited above.
RATIOS = [1e-9, 1e-5, 1e-3, 1e-1]
K_R_D = 10.0
DWELL_CENTRAL = 10.0 / 150.0
N_PULSES = 5


def main():
    # =================================================================
    # PART A -- the ON-endpoint mixed-length-scale regime (P-054-1/2)
    # =================================================================
    regime = ts.mixed_length_scale_regime(
        p_abs_w=P_ABS_W_ON_CENTRAL, l_geometric_m=R_OUT_M, k_air=K_AIR,
        density_kg_m3=DENSITY_SI_KG_M3, c_p_j_kgk=C_P_SI_J_KGK,
        emissivity=EMISSIVITY, t_ambient_k=T_AMBIENT_K)
    netd_on = ts.netd_disposition(regime["dt_ss_full_K"], NETD_BAND_K)
    margin_on = NETD_BAND_K[0] / regime["dt_ss_full_K"]

    p_054_1_band = (2.8e-5, 3.6e-5)
    p_054_1_pass = p_054_1_band[0] <= regime["dt_ss_full_K"] <= p_054_1_band[1]
    p_054_2_band = (500.0, 750.0)
    p_054_2_pass = p_054_2_band[0] <= margin_on <= p_054_2_band[1]

    part_a = {
        "regime": regime,
        "material_provenance_note": MATERIAL_PROVENANCE_NOTE,
        "netd_disposition": netd_on,
        "netd_lo_margin": margin_on,
        "netd_disclaimer": NETD_DISCLAIMER,
        "p_054_1_band": list(p_054_1_band), "p_054_1_pass": p_054_1_pass,
        "p_054_2_band": list(p_054_2_band), "p_054_2_pass": p_054_2_pass,
        "w_on_consistent_reference_dt_ss_full_K": 1.0875240683859519e-05,
        # exp-045 results.json::block_b...w_on_consistent.dt_ss_full_K
        "r_out_consistent_reference_dt_ss_full_K": 3.5982339737222747e-06,
        # exp-045 results.json::block_b...r_out_consistent.dt_ss_full_K --
        # NOT this cycle's number: r_out_consistent uses P_abs measured AT
        # r_out too (Q_ext=1 assumed), whereas the mixed chain keeps P_abs
        # on the real w_on measurement. Different physical quantities.
    }

    # =================================================================
    # PART B -- Block C genuine re-run at the mixed chain's own
    # dt_ss_full/tau_thermal_s (P-054-3a/3b/4)
    # =================================================================
    dt_ss = regime["dt_ss_full_K"]
    tau_th = regime["tau_thermal_s"]

    block_c_points = {}
    for r in RATIOS:
        k_f_on = r * K_R_D
        tau_k = 1.0 / (k_f_on + K_R_D)
        for gap_name, dt_gap in (("5tau", 5.0 * tau_k), ("0.5tau", 0.5 * tau_k)):
            segs = kin.pulse_train_segments(
                k_f_ambient=k_f_on, k_r=K_R_D, A=0.0,
                T_pulse=dt_gap, dt_sweep=DWELL_CENTRAL, n_pulses=N_PULSES)
            n_final, t_arr, n_arr = kin.integrate_segments(segs, n0=0.0, method="exp", record=True)
            on_end_idx = [1, 3, 5, 7, 9, 11]
            n_at_on_end = [float(n_arr[i]) for i in on_end_idx]
            n_first, n_periodic = n_at_on_end[0], n_at_on_end[-1]

            dT_first_decoupled = dt_ss * n_first
            dT_periodic_decoupled = dt_ss * n_periodic
            netd_first = ts.netd_disposition(dT_first_decoupled, NETD_BAND_K)
            netd_periodic = ts.netd_disposition(dT_periodic_decoupled, NETD_BAND_K)

            _n_walk, _dT_walk = 0.0, 0.0
            _dT_at_on_end = []
            for _seg_k_f, _seg_k_r, _seg_dur in segs:
                _n_walk, _dT_walk = coupled_segment_general(
                    _seg_k_f, _seg_k_r, dt_ss, tau_th, _seg_dur, _n_walk, _dT_walk)
                _dT_at_on_end.append(_dT_walk)
            _on_seg_idx = [0, 2, 4, 6, 8, 10]
            dT_exact_at_on_end = [_dT_at_on_end[i] for i in _on_seg_idx]
            dT_exact_first = dT_exact_at_on_end[0]
            dT_exact_periodic = dT_exact_at_on_end[-1]
            exact_vs_decoupled_ratio_first = (dT_exact_first / dT_first_decoupled
                                               if dT_first_decoupled > 0 else float("nan"))
            exact_vs_decoupled_ratio_periodic = (dT_exact_periodic / dT_periodic_decoupled
                                                  if dT_periodic_decoupled > 0 else float("nan"))

            # self-check, mirrors exp-045's own in-script assertion:
            # coupled_segment_general must reduce to coupled_kinetics_
            # thermal_dT exactly at n0=dT0=0.
            _n_check, _dT_check = coupled_segment_general(k_f_on, K_R_D, dt_ss, tau_th, DWELL_CENTRAL, 0.0, 0.0)
            _dT_ref = coupled_kinetics_thermal_dT(k_f_on, K_R_D, dt_ss, tau_th, DWELL_CENTRAL)
            assert abs(_dT_check - _dT_ref) < 1e-9 * max(abs(_dT_ref), 1e-30), \
                "coupled_segment_general must reduce to coupled_kinetics_thermal_dT at n0=dT0=0"

            block_c_points[f"r{r:.0e}_{gap_name}"] = {
                "r": r, "gap_name": gap_name,
                "k_f_on": k_f_on, "k_r": K_R_D, "tau_kinetics_s": tau_k,
                "dt_gap_s": dt_gap, "n_pulses": N_PULSES,
                "dwell_central_s": DWELL_CENTRAL,
                "n_first_pulse": n_first, "n_periodic": n_periodic,
                "dT_first_decoupled_K": dT_first_decoupled,
                "dT_periodic_decoupled_K": dT_periodic_decoupled,
                "netd_first": netd_first, "netd_periodic": netd_periodic,
                "dT_exact_first_K": dT_exact_first,
                "dT_exact_periodic_K": dT_exact_periodic,
                "exact_vs_decoupled_ratio_first": exact_vs_decoupled_ratio_first,
                "exact_vs_decoupled_ratio_periodic": exact_vs_decoupled_ratio_periodic,
                "decoupled_is_conservative_first": dT_exact_first <= dT_first_decoupled,
                "decoupled_is_conservative_periodic": dT_exact_periodic <= dT_periodic_decoupled,
            }

    ratios_periodic = [v["exact_vs_decoupled_ratio_periodic"] for v in block_c_points.values()]
    ratios_first = [v["exact_vs_decoupled_ratio_first"] for v in block_c_points.values()]
    all_ratios = ratios_periodic + ratios_first
    worst_ratio = max(all_ratios)  # closest to (or over) 1.0
    best_ratio = min(all_ratios)
    all_decoupled_conservative = all(
        v["decoupled_is_conservative_periodic"] and v["decoupled_is_conservative_first"]
        for v in block_c_points.values())
    max_dT_periodic_decoupled = max(v["dT_periodic_decoupled_K"] for v in block_c_points.values())
    max_dT_periodic_exact = max(v["dT_exact_periodic_K"] for v in block_c_points.values())
    margin_dose_decoupled = NETD_BAND_K[0] / max_dT_periodic_decoupled
    margin_dose_exact = NETD_BAND_K[0] / max_dT_periodic_exact
    all_c_undetectable = all(
        v["netd_periodic"]["classification"] != "DETECTABLE" for v in block_c_points.values())

    p_054_3a_band = (0.98, 1.000)
    p_054_3a_pass = p_054_3a_band[0] <= worst_ratio <= p_054_3a_band[1] and all_decoupled_conservative
    p_054_3b_band = (1.9e-6, 2.6e-6)
    p_054_3b_pass = p_054_3b_band[0] <= max_dT_periodic_decoupled <= p_054_3b_band[1]
    p_054_4_band_lo = 7000.0  # margin >= this (exact dT <= decoupled dT => margin_exact >= margin_decoupled)
    p_054_4_pass = margin_dose_exact >= p_054_4_band_lo

    part_b = {
        "block_c_points": block_c_points,
        "dt_ss_full_K_used": dt_ss, "tau_thermal_s_used": tau_th,
        "dwell_over_tau_thermal_mixed": DWELL_CENTRAL / tau_th,
        "worst_exact_vs_decoupled_ratio": worst_ratio,
        "best_exact_vs_decoupled_ratio": best_ratio,
        "all_decoupled_conservative": all_decoupled_conservative,
        "max_dT_periodic_decoupled_K": max_dT_periodic_decoupled,
        "max_dT_periodic_exact_K": max_dT_periodic_exact,
        "netd_lo_margin_decoupled": margin_dose_decoupled,
        "netd_lo_margin_exact": margin_dose_exact,
        "all_points_undetectable": all_c_undetectable,
        "netd_disclaimer": NETD_DISCLAIMER,
        "p_054_3a_band": list(p_054_3a_band), "p_054_3a_pass": p_054_3a_pass,
        "p_054_3b_band": list(p_054_3b_band), "p_054_3b_pass": p_054_3b_pass,
        "p_054_4_band_lo": p_054_4_band_lo, "p_054_4_pass": p_054_4_pass,
    }

    # =================================================================
    # P-054-5, P-054-6, P-054-8
    # =================================================================
    p_054_5_pass = (netd_on["classification"] == "UNDETECTABLE"
                     and all_c_undetectable)
    p_054_6_scope_statement = (
        "This cycle tests ONLY the bench-scale r_out-vs-w_on length-scale "
        "question and (via the mixed chain replacing the original h_conv="
        "5.0 W/(m^2K) placeholder) the gas-phase-conduction-vs-placeholder "
        "question. It does NOT test, confirm, or refute Iteration 25's "
        "separate, informal witness-scale (T8/T13/T14 near-field->witness-"
        "scale bridge) h_eff estimate (~5.1x->~2.6x / ~27,080x->~38-42x) -- "
        "that is a different physical question, explicitly out of scope "
        "(see NOTES.md idealizations, 'Bench-scale, not witness-scale'). "
        "T8/T13's witness-scale h_eff question REMAINS OPEN AND "
        "UNADDRESSED by exp-054.")

    results = {
        "meta": {
            "experiment": "054-heff-length-scale-rederivation",
            "panel_iteration": 31,
            "lead_seat": "THERMODYNAMICS",
            "t1_escape_route": "NONE",
            "new_fdtd_calls": 0,
        },
        "part_a_on_endpoint_mixed_regime": part_a,
        "part_b_block_c_rerun": part_b,
        "p_054_5_both_undetectable": p_054_5_pass,
        "p_054_6_scope_statement": p_054_6_scope_statement,
        "netd_disclaimer_ALL_CLAIMS": NETD_DISCLAIMER,
        "material_provenance_note_ALL_CLAIMS": MATERIAL_PROVENANCE_NOTE,
    }

    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(results, f, indent=2)

    print(f"P-054-1 dt_ss_full(ON, mixed)={regime['dt_ss_full_K']:.6e} K  "
          f"pass={p_054_1_pass}")
    print(f"P-054-2 NETD-lo margin(ON)={margin_on:.2f}x  pass={p_054_2_pass}")
    print(f"P-054-3a worst exact/decoupled ratio={worst_ratio:.6f}  "
          f"all_conservative={all_decoupled_conservative}  pass={p_054_3a_pass}")
    print(f"P-054-3b max dT_periodic_decoupled={max_dT_periodic_decoupled:.4e} K  "
          f"pass={p_054_3b_pass}")
    print(f"P-054-4 NETD-lo margin(dose, exact)={margin_dose_exact:.2f}x  "
          f"(decoupled={margin_dose_decoupled:.2f}x)  pass={p_054_4_pass}")
    print(f"P-054-5 both UNDETECTABLE={p_054_5_pass}")


if __name__ == "__main__":
    main()
