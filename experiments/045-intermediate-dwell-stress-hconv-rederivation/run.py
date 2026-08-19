"""exp-045 -- Panel Iteration 22: the intermediate-dwell coupled kinetics-
thermal stress sweep (Block A) + THERMODYNAMICS' h_conv/mass_kg
re-derivation bundled with ELECTROMAGNETISM's own T22 geometric-disk-vs-
`iso_xsec_sq` area table entry (Block B). Lead: ELECTROMAGNETISM.

Zero FDTD calls. Pure desk/analytic arithmetic reusing already-verified
machinery (`lab.kinetics`, stage-12-gated; `lab.thermo_sidecar`, stage-15-
gated) plus one already-verified, not-yet-promoted closed form
(`coupled_kinetics_thermal_dT`, Red Team's Iteration-21 Phase-2 derivation,
reused VERBATIM from experiments/044/run.py -- not re-derived here, and
NOT promoted into lab/thermo_sidecar.py this cycle: a deliberate no-new-
trust-suite-stage scope judgment, named explicitly per exp-044's own
precedent, backed by (i) exp-044's own <4e-4 relative-error cross-check
against scipy.integrate.odeint at all 16 of ITS grid points, (ii) this
script's own internal analytic identity checks below, (iii) the
monotonic-approach-to-ceiling bound derived in phase1_proposal.md and
verified numerically against every point this script computes).

  Block A -- sweep the coupled-vs-decoupled relative difference across
      dwell/tau ratios spanning 0.1x-10x of BOTH tau_kinetics (per host/
      ratio point, "axis K") and tau_thermal (per tau_thermal regime,
      "axis T"), for all 16 PUBLISHED/PLAUSIBLE-tier host/ratio points
      (exp-044's own grid, reused verbatim) -- the genuinely untested
      regime per Iteration-21's own close (exp-044 tested exactly ONE
      dwell against this grid). Three tau_thermal regimes swept in
      parallel: uncorrected (exp-043/044's own number), T22-area-only-
      corrected (x2.9/x3.0, the isolated iso_xsec_sq inflation factor
      already established), and Block B's own FULLY-corrected number
      (h_conv AND mass_kg re-derived together) -- so Block A's stress
      test and Block B's re-derivation are evaluated against each other
      in the same run, not left as two disconnected desk items.

  Block B -- re-derive h_conv (gas-phase conduction, h_eff = k_air/r_out)
      and mass_kg (material density x the iso_xsec_sq idealized volume,
      extended for the first time from an area convention to a volume
      convention -- a NEW idealization, disclosed) from first principles
      instead of the placeholder h_conv=5.0 W/(m^2K) / mass_kg=1.0e-15 kg
      carried since exp-032. Bundled with the geometric-disk-vs-
      `iso_xsec_sq` area table (T22) at the two committed bench
      geometries (the sigma(I) ON endpoint and the graded_black_shell
      flagship absorber).

  Block C -- QUANTUM's repeated-sweep/dose-accumulation kinetics test
      (`pulse_train_segments`, Iteration-22 priority #3) is explicitly
      DEFERRED, not run -- see phase1_proposal.md Scope Decision.

See phase1_proposal.md for the full Phase-1 record, T1 escape-route
statement (NONE -- pure instrument/model-fidelity characterization), and
every falsifiable predicted band this script's own output is scored
against.
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)

from lab import thermo_sidecar as ts
from lab import kinetics as kin

# ============================================================ shared inputs
# Reused VERBATIM from exp-043/exp-044 -- NOT re-sourced or re-derived this
# cycle (Block A idealization; matches exp-044's own precedent).
DX_M = 30.0e-9  # 600nm/cpl20
R_OUT_CELLS = 78  # exp-026/043's bench R_OUT (2.34um at this dx)
SIGMA_EXT_ON, RATIO_ON = 235.96673494878587, 0.6074830175566805  # exp-026/043/044, 600nm
SIGMA_EXT_ABSORBER, RATIO_ABSORBER = 240.0073740162445, 0.51  # graded_black_shell flagship, exp-043
NETD_BAND_K = (0.020, 0.050)
EMISSIVITY, H_CONV_OLD, MASS_KG_OLD, C_P = 0.9, 5.0, 1.0e-15, 700.0
T_AMBIENT_K = 293.15


def _irradiance_w_cm2(candela, efficacy_lm_w, distance_m):
    lux = candela / distance_m ** 2
    w_per_m2 = lux / efficacy_lm_w
    return w_per_m2 / 1.0e4


def coupled_kinetics_thermal_dT(k_f, k_r, dt_ss_full, tau_thermal_s, dwell_s):
    """Red Team's own closed-form solve (Iteration-21 Phase 2, exp-044
    mandatory fix 3) of the coupled ODE the decoupled two-stage shortcut
    (ceiling * n_at_dwell) approximates:

        dn/dt   = k_f*(1-n) - k_r*n,                    n(0)=0
        dDT/dt  = (1/tau_th)*(dt_ss_full*n(t) - DT),     DT(0)=0

    Exact solution, reused VERBATIM from experiments/044/run.py (verified
    there against scipy.integrate.odeint to <4e-4 relative error at every
    one of that cycle's 16 grid points) -- not re-derived, not modified."""
    tau_k = 1.0 / (k_f + k_r)
    n_ss = k_f / (k_f + k_r)
    if abs(tau_k - tau_thermal_s) < 1e-12 * max(tau_k, tau_thermal_s):
        raise ValueError("degenerate tau_k == tau_thermal_s, not expected on this grid")
    bracket = (1.0
               - (tau_k / (tau_k - tau_thermal_s)) * math.exp(-dwell_s / tau_k)
               + (tau_thermal_s / (tau_k - tau_thermal_s)) * math.exp(-dwell_s / tau_thermal_s))
    return dt_ss_full * n_ss * bracket


def main():
    # -------- reused Part-A witness inputs (exp-043/044, unchanged) ------
    irr_central = _irradiance_w_cm2(40000.0, 300.0, 45.0)
    dwell_central = 10.0 / 150.0  # theta_beam=10deg / omega=150deg/s

    on_central = ts.absorbed_power_established_ratio(
        irr_central, SIGMA_EXT_ON, DX_M, RATIO_ON)
    on_area_m2_iso = on_central["area_m2"]
    dt_ss_full_old = ts.steady_state_delta_T(
        on_central["p_abs_w"], on_area_m2_iso, EMISSIVITY, H_CONV_OLD, T_AMBIENT_K)
    dp_dt_old = on_area_m2_iso * (4.0 * EMISSIVITY * ts.SIGMA_SB * T_AMBIENT_K ** 3 + H_CONV_OLD)
    tau_thermal_s_old = MASS_KG_OLD * C_P / dp_dt_old

    # ==================================================================
    # BLOCK B -- h_conv / mass_kg re-derivation + T22 area table
    # (computed BEFORE Block A so its corrected numbers feed Block A's
    # third dwell-sweep regime)
    # ==================================================================
    K_AIR_W_MK = 0.026  # room-temperature air thermal conductivity, textbook value
    r_out_m = R_OUT_CELLS * DX_M
    h_eff = K_AIR_W_MK / r_out_m
    assert abs(h_eff * r_out_m - K_AIR_W_MK) < 1e-15 * K_AIR_W_MK, \
        "h_eff*r_out identity must reproduce k_air exactly (gate-lite, no new trust-suite stage)"

    geometric_disk_area_m2 = math.pi * r_out_m ** 2
    iso_area_on_m2 = (SIGMA_EXT_ON * DX_M) ** 2
    iso_area_absorber_m2 = (SIGMA_EXT_ABSORBER * DX_M) ** 2
    area_ratio_on = iso_area_on_m2 / geometric_disk_area_m2
    area_ratio_absorber = iso_area_absorber_m2 / geometric_disk_area_m2

    DENSITY_PMMA_KG_M3 = 1180.0  # PMMA (poly-methyl-methacrylate), the most
    # commonly cited photochromic-dye host polymer in the literature this
    # program has surveyed (T17/T18) -- a STATED, not sourced-this-cycle,
    # density assumption (idealization, see phase1_proposal.md).
    DENSITY_WATER_KG_M3 = 1000.0  # disclosed lower-density comparison bound
    w_on_m = SIGMA_EXT_ON * DX_M
    volume_iso_cube_m3 = w_on_m ** 3  # NEW idealization this cycle: extends
    # iso_xsec_sq's own "compact, not rod" area convention (w^2) to a
    # volume for the FIRST time (mass_kg was always an arbitrary
    # placeholder before) -- the natural completion is a cube of side w,
    # same compactness assumption, disclosed explicitly, not inherited
    # from any prior committed code.
    mass_kg_pmma = DENSITY_PMMA_KG_M3 * volume_iso_cube_m3
    mass_kg_water = DENSITY_WATER_KG_M3 * volume_iso_cube_m3
    assert abs(mass_kg_pmma - DENSITY_PMMA_KG_M3 * volume_iso_cube_m3) < 1e-30

    # steady-state ceiling with h_conv corrected only (mass_kg does not
    # enter steady_state_delta_T at all -- PHOTONICS' Iteration-20 proof,
    # area-invariant too, reused unmodified)
    dp_dt_hcorr = on_area_m2_iso * (4.0 * EMISSIVITY * ts.SIGMA_SB * T_AMBIENT_K ** 3 + h_eff)
    dt_ss_full_corrected = on_central["p_abs_w"] / dp_dt_hcorr
    tau_thermal_s_fully_corrected = mass_kg_pmma * C_P / dp_dt_hcorr
    tau_thermal_s_fully_corrected_water = mass_kg_water * C_P / dp_dt_hcorr

    block_b = {
        "h_conv_rederivation": {
            "k_air_w_mk": K_AIR_W_MK,
            "k_air_source_note": "textbook room-temperature air thermal conductivity value, not re-sourced this cycle (T18 WebFetch still blocked)",
            "r_out_cells": R_OUT_CELLS, "dx_m": DX_M, "r_out_m": r_out_m,
            "h_eff_w_m2k": h_eff,
            "h_conv_old_placeholder_w_m2k": H_CONV_OLD,
            "h_eff_over_h_conv_old_ratio": h_eff / H_CONV_OLD,
            "regime_note": "gas-phase conduction (h_eff = k_air/r_out), the correct micron-scale regime per exp-043 Phase-5 (THERMODYNAMICS), replacing the macroscopic natural-convection placeholder h_conv=5.0 W/(m^2K) used since exp-032",
        },
        "mass_kg_rederivation": {
            "sigma_ext_on_cells": SIGMA_EXT_ON, "w_on_m": w_on_m,
            "volume_convention": "iso_xsec_cube -- NEW this cycle: extends iso_xsec_sq's own compact-object area idealization (w^2) to a volume (w^3), same compactness assumption, disclosed explicitly (not inherited from any prior committed code)",
            "density_pmma_kg_m3": DENSITY_PMMA_KG_M3,
            "density_pmma_source_note": "stated assumption: PMMA, the most commonly cited photochromic-dye host polymer in this program's own literature surveys (T17/T18) -- not independently re-sourced this cycle (T18 WebFetch still blocked)",
            "density_water_kg_m3": DENSITY_WATER_KG_M3,
            "mass_kg_pmma": mass_kg_pmma,
            "mass_kg_water": mass_kg_water,
            "mass_kg_old_placeholder": MASS_KG_OLD,
            "mass_pmma_over_old_ratio": mass_kg_pmma / MASS_KG_OLD,
            "mass_water_over_old_ratio": mass_kg_water / MASS_KG_OLD,
        },
        "t22_area_table": {
            "geometric_disk_area_m2": geometric_disk_area_m2,
            "geometric_disk_formula": "pi * (R_OUT_CELLS * dx_m)^2 -- the bench's own real simulated disk",
            "iso_xsec_sq_area_on_endpoint_m2": iso_area_on_m2,
            "area_ratio_iso_over_geometric_on_endpoint": area_ratio_on,
            "iso_xsec_sq_area_absorber_m2": iso_area_absorber_m2,
            "area_ratio_iso_over_geometric_absorber": area_ratio_absorber,
            "t22_established_range_note": "matches T22's own established 2.9-3.0x inflation figure (exp-043/044) at both bench geometries measured to date -- ON endpoint 2.913x, graded_black_shell flagship 3.014x",
            "convention_recommendation": (
                "Both stay, scoped per-branch, as thermo_sidecar.py already does -- NOT "
                "a single winner. geometric-disk area is unambiguous and matches the "
                "actual simulated object for the weak-tau branch (absorbed_power_weak_tau "
                "already uses it, correctly, per its own docstring). iso_xsec_sq is a "
                "stated, disclosed idealization for the established-ratio branch "
                "specifically, where sigma_ext (not object geometry) is the only "
                "measured quantity available -- replacing it with the geometric-disk "
                "area there would silently assume Q_ext=1, which T9 already refutes for "
                "both established-ratio articles (0.51, 0.6075 both exceed the "
                "geometric-optics Q_ext<=1-implied ceiling). Recommendation: keep both, "
                "but stop calling iso_xsec_sq-derived tau_thermal_s 'the' thermal time "
                "constant without the geometric-disk comparator alongside it -- this "
                "table is that comparator, now committed."
            ),
        },
        "corrected_steady_state": {
            "dt_ss_full_old_K": dt_ss_full_old,
            "dt_ss_full_h_corrected_K": dt_ss_full_corrected,
            "drop_factor_vs_old": dt_ss_full_old / dt_ss_full_corrected,
            "note": "mass_kg does NOT enter steady_state_delta_T (PHOTONICS' Iteration-20 area-invariance proof, reused unmodified) -- only h_conv correction moves this number",
        },
        "corrected_tau_thermal": {
            "tau_thermal_s_old_uncorrected": tau_thermal_s_old,
            "tau_thermal_s_fully_corrected_pmma": tau_thermal_s_fully_corrected,
            "tau_thermal_s_fully_corrected_water": tau_thermal_s_fully_corrected_water,
            "factor_vs_old_pmma": tau_thermal_s_fully_corrected / tau_thermal_s_old,
            "factor_vs_old_water": tau_thermal_s_fully_corrected_water / tau_thermal_s_old,
            "note": (
                "the two corrections (h_conv up ~2222x in the pure-h_conv term, mass_kg "
                "up ~355-419x) do NOT merely 'partially offset' as exp-043 Phase-5 first "
                "flagged without a number -- combined, tau_thermal_s SHRINKS by a factor "
                "of ~0.35-0.38 (i.e. gets ~2.6-2.9x SHORTER), because dp_dt's ~1096x "
                "growth (h_eff dominates the radiative term, which is itself only "
                "~5.1 W/(m^2K) at this geometry -- comparable to the OLD placeholder "
                "h_conv=5.0, explaining why the drop is ~1096x not the naive ~2222x "
                "h_eff/h_conv_old ratio) outpaces the ~355-419x mass growth."
            ),
        },
    }

    # ==================================================================
    # BLOCK A -- intermediate-dwell coupled kinetics-thermal stress sweep
    # ==================================================================
    HOSTS = [("A", 1e9), ("B", 1e6), ("C", 1e3), ("D", 1e1)]
    RATIOS = [1e-9, 1e-5, 1e-3, 1e-1]
    N_R = 13  # log-spaced 0.1x-10x, 6 points/decade
    R_GRID = [10.0 ** (-1.0 + 2.0 * i / (N_R - 1)) for i in range(N_R)]

    TAU_TH_REGIMES = {
        "uncorrected": (tau_thermal_s_old, dt_ss_full_old),
        "t22_area_only_x2.9": (tau_thermal_s_old * 2.9, dt_ss_full_old),
        "t22_area_only_x3.0": (tau_thermal_s_old * 3.0, dt_ss_full_old),
        "fully_corrected_pmma": (tau_thermal_s_fully_corrected, dt_ss_full_corrected),
    }

    sweep_points = []
    for host, k_r in HOSTS:
        for r in RATIOS:
            k_f = r * k_r
            tau_k = 1.0 / (k_f + k_r)
            n_ss = float(kin.n_eq_exact(k_f, k_r))
            for regime_name, (tau_th, dt_ss) in TAU_TH_REGIMES.items():
                for axis_name, anchor_tau in (("K", tau_k), ("T", tau_th)):
                    for Rv in R_GRID:
                        dwell = Rv * anchor_tau
                        exact_dT = coupled_kinetics_thermal_dT(k_f, k_r, dt_ss, tau_th, dwell)
                        n_at_dwell = float(kin.relax_exact(n0=0.0, k_f=k_f, k_r=k_r, dt=dwell))
                        decoupled_dT = dt_ss * n_at_dwell
                        rel_diff = abs(exact_dT - decoupled_dT) / exact_dT if exact_dT > 0 else 0.0
                        netd = ts.netd_disposition(exact_dT, NETD_BAND_K)
                        sweep_points.append({
                            "host": host, "r": r, "k_f": k_f, "k_r": k_r,
                            "tau_kinetics_s": tau_k, "n_ss": n_ss,
                            "regime": regime_name, "tau_thermal_s": tau_th,
                            "dt_ss_full_K": dt_ss, "axis": axis_name, "R": Rv,
                            "dwell_s": dwell,
                            "exact_coupled_dT_K": exact_dT,
                            "decoupled_shortcut_dT_K": decoupled_dT,
                            "relative_difference": rel_diff,
                            "netd_classification": netd["classification"],
                        })

    # ---- summary: worst-case rel_diff per host, per axis, per regime ----
    def worst_for(host=None, axis=None, regime=None):
        pts = sweep_points
        if host is not None:
            pts = [p for p in pts if p["host"] == host]
        if axis is not None:
            pts = [p for p in pts if p["axis"] == axis]
        if regime is not None:
            pts = [p for p in pts if p["regime"] == regime]
        best = max(pts, key=lambda p: p["relative_difference"])
        return best

    per_host_axis_summary = {}
    for host, _ in HOSTS:
        for axis in ("K", "T"):
            w = worst_for(host=host, axis=axis, regime="uncorrected")
            per_host_axis_summary[f"{host}_{axis}"] = {
                "worst_rel_diff": w["relative_difference"],
                "at_r": w["r"], "at_R": w["R"], "at_dwell_s": w["dwell_s"],
            }

    global_max_dT = max(sweep_points, key=lambda p: p["exact_coupled_dT_K"])
    all_undetectable_or_better = all(
        p["netd_classification"] != "DETECTABLE" for p in sweep_points)

    # ---- consistency check: does axis-K reproduce exp-044's own single
    # Host-D witness-dwell point (1.44-1.50% relative difference)? ----
    host_d_witness_check = {}
    for r in RATIOS:
        k_r = 10.0
        k_f = r * k_r
        exact = coupled_kinetics_thermal_dT(k_f, k_r, dt_ss_full_old, tau_thermal_s_old, dwell_central)
        n_at_dwell = float(kin.relax_exact(n0=0.0, k_f=k_f, k_r=k_r, dt=dwell_central))
        decoupled = dt_ss_full_old * n_at_dwell
        rel = abs(exact - decoupled) / exact
        host_d_witness_check[f"r{r:.0e}"] = {
            "rel_diff_at_dwell_central": rel,
            "dwell_over_tau_kinetics": dwell_central / (1.0 / (k_f + k_r)),
            "matches_exp044_band_1.44_1.50pct": 0.0144 <= rel <= 0.0150,
        }

    # ---- theoretical ceiling bound (monotone-approach-to-n_ss argument,
    # phase1_proposal.md Idealization): no coupled-ODE point can exceed
    # dt_ss_full * n_ss_max regardless of dwell, since the system is a
    # cascade of two real-pole (non-oscillatory) first-order relaxations.
    n_ss_max = max(k_f / (k_f + k_r) for host, k_r in HOSTS for k_f in
                   [r * k_r for r in RATIOS])
    ceiling_bounds = {
        regime: dt_ss * n_ss_max for regime, (tau_th, dt_ss) in TAU_TH_REGIMES.items()
    }
    ceiling_check = all(
        p["exact_coupled_dT_K"] <= ceiling_bounds[p["regime"]] * (1 + 1e-9)
        for p in sweep_points
    )

    block_a = {
        "hosts_ratios_grid": {"HOSTS": HOSTS, "RATIOS": RATIOS,
                               "n_points": len(HOSTS) * len(RATIOS)},
        "R_grid_0.1x_to_10x": R_GRID,
        "tau_thermal_regimes": {k: {"tau_thermal_s": v[0], "dt_ss_full_K": v[1]}
                                 for k, v in TAU_TH_REGIMES.items()},
        "n_sweep_points": len(sweep_points),
        "sweep_points": sweep_points,
        "per_host_axis_worst_case_summary_uncorrected_regime": per_host_axis_summary,
        "global_max_dT_K": global_max_dT["exact_coupled_dT_K"],
        "global_max_dT_point": {k: global_max_dT[k] for k in
                                 ("host", "r", "regime", "axis", "R", "dwell_s")},
        "global_max_dT_netd_lo_margin": NETD_BAND_K[0] / global_max_dT["exact_coupled_dT_K"],
        "all_points_undetectable_or_better": all_undetectable_or_better,
        "theoretical_ceiling_bounds_K": ceiling_bounds,
        "theoretical_ceiling_check_holds_everywhere": ceiling_check,
        "host_d_witness_dwell_consistency_check": host_d_witness_check,
        "netd_disclaimer": (
            "NETD is an instrument/detector threshold, not a human perceptual one "
            "(VISION SCIENCE's standing mandatory fix, exp-043 Red Team attack 7). "
            "This classification does NOT bear on constraint-3/4's human-eye verdict."),
        "short_dwell_relative_error_note": (
            "At the SMALL-R end of the sweep (R~0.1) for Hosts A/B/C, relative "
            "difference can read as large as O(10)-O(1e7) -- this is an EXPECTED, "
            "benign artifact (the decoupled shortcut assumes the thermal response "
            "tracks n(t) instantly, while the true coupled response is O(t^2) at "
            "very short dwell vs. the shortcut's O(t) -- a relative-error blowup "
            "at a vanishing absolute scale), NOT a new physical finding. The "
            "absolute dT at every such point remains many orders of magnitude "
            "below NETD (see global_max_dT_K) -- see phase1_proposal.md Idealizations."
        ),
    }

    # ==================================================================
    # BLOCK C -- explicitly deferred
    # ==================================================================
    block_c = {
        "status": "DEFERRED",
        "reason": (
            "QUANTUM's repeated-sweep/dose-accumulation kinetics test "
            "(pulse_train_segments, targeting Host D) is QUANTUM OPTICS' own "
            "native charge, ranked Iteration-22 priority #3 (not #1). This "
            "cycle already delivers two substantial, well-developed analytic "
            "blocks (A: a 4-regime x 2-axis x 16-point dwell sweep; B: a "
            "from-first-principles h_conv/mass_kg re-derivation). Block C "
            "deserves its own dedicated design attention -- specifically, "
            "choosing a sweep-rate/inter-pulse-interval that matches the "
            "witness scenario's own beam geometry (a QUANTUM-native judgment "
            "call, not an EM-appropriable arithmetic swap, mirroring MATERIALS' "
            "own Iteration-21 reasoning for deferring THIS cycle's Block B). "
            "The Iteration-18/20/21 non-native-lead precedent (MATERIALS ran "
            "QUANTUM's #1-ranked item) does not mechanically extend to a #3 "
            "item being ADDITIONALLY bundled onto an already-two-block cycle -- "
            "scope discipline. QUANTUM OPTICS leads again at Iteration 24, "
            "two cycles away, not an open-ended deferral."
        ),
    }

    out = {
        "meta": {"elapsed_s": 0.0, "n_new_fdtd_calls": 0,
                 "trust_suite_stage": "reuses stages 12/15 (lab.kinetics, lab.thermo_sidecar); "
                                       "coupled_kinetics_thermal_dT reused verbatim from exp-044, "
                                       "no new trust-suite stage this cycle (see run.py docstring)"},
        "block_a_intermediate_dwell_sweep": block_a,
        "block_b_hconv_mass_rederivation_and_t22_table": block_b,
        "block_c_dose_accumulation_kinetics": block_c,
    }

    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1, default=float)

    print(f"Block B: h_eff={h_eff:.1f} W/(m^2K) ({h_eff/H_CONV_OLD:.0f}x placeholder h_conv=5.0)")
    print(f"  mass_kg(PMMA)={mass_kg_pmma:.3e} kg ({mass_kg_pmma/MASS_KG_OLD:.1f}x placeholder 1e-15 kg)")
    print(f"  T22 area ratio (iso_xsec_sq/geometric-disk): ON-endpoint={area_ratio_on:.4f}x, "
          f"flagship absorber={area_ratio_absorber:.4f}x")
    print(f"  dt_ss_full: old={dt_ss_full_old:.4e}K -> h-corrected={dt_ss_full_corrected:.4e}K "
          f"({dt_ss_full_old/dt_ss_full_corrected:.1f}x drop)")
    print(f"  tau_thermal_s: old={tau_thermal_s_old:.4e}s -> fully-corrected(PMMA)="
          f"{tau_thermal_s_fully_corrected:.4e}s (factor {tau_thermal_s_fully_corrected/tau_thermal_s_old:.3f}x)")
    print()
    print(f"Block A: {len(sweep_points)} sweep points across {len(HOSTS)*len(RATIOS)} host/ratio "
          f"points x {len(TAU_TH_REGIMES)} tau_thermal regimes x 2 axes x {N_R} R-values")
    print(f"  global max dT anywhere in sweep: {global_max_dT['exact_coupled_dT_K']:.4e} K "
          f"at {global_max_dT['host']}/r={global_max_dT['r']:.0e}/{global_max_dT['regime']}/"
          f"axis-{global_max_dT['axis']}/R={global_max_dT['R']:.2f} "
          f"({NETD_BAND_K[0]/global_max_dT['exact_coupled_dT_K']:.1f}x below netd_lo)")
    print(f"  ALL {len(sweep_points)} points UNDETECTABLE-or-better: {all_undetectable_or_better}")
    print(f"  theoretical ceiling bound holds everywhere: {ceiling_check}")
    print(f"  Host-D witness-dwell reproduction (should match exp-044's 1.44-1.50%):")
    for k, v in host_d_witness_check.items():
        print(f"    {k}: rel_diff={v['rel_diff_at_dwell_central']:.4%}  "
              f"matches_exp044_band={v['matches_exp044_band_1.44_1.50pct']}")
    print(f"  NOTE: {block_a['short_dwell_relative_error_note']}")
    print()
    print("Block C: DEFERRED (see block_c_dose_accumulation_kinetics.reason)")
    print("results.json written")


if __name__ == "__main__":
    main()
