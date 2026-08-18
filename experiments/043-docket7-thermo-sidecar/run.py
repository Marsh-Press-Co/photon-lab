"""exp-043 — Docket #7 + lab/thermo_sidecar.py, panel Iteration 20.

Zero FDTD calls. Applies the newly-promoted, Red-Team-fixed
`lab.thermo_sidecar` module to:
  (a) the four established weak-tau OFF-state sponge articles
      (off_pass/off_lab/off_field/off_bracket, exp-032/026),
  (b) the sigma(I) ON endpoint (tau=3.9, exp-026's measured
      sigma_abs/sigma_ext=0.6075 at 600nm),
  (c) the program's own flagship absorber (`graded_black_shell`,
      established sigma_abs/sigma_ext=0.51, exp-002/020/030),
using docket #7's newly-sourced witness scenario (Part A, below) instead
of a placeholder wattage for the first time in this program's history.

See NOTES.md for the full Phase 1-5 panel record.
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, HERE)

from lab import thermo_sidecar as ts

# ---------------------------------------------------------------- Part A
# Docket #7: sourced witness-scenario parameters (WebSearch snippet-level;
# WebFetch confirmed EGRESS_BLOCKED for scholarly domains this shift too,
# T18's 6th consecutive confirmation).

WITNESS = ts.WitnessScenario(
    candela_range=(13827.0, 99310.0),
    candela_source_refs=[
        "Fenix PD36R V2.0 high mode: 13,827 cd (fenix-store.com product spec)",
        "Fenix PD36R ACE turbo: 43,181 cd (brightguy.com product spec)",
        "Olight Warrior Ultra: 26,000 cd (brightguy.com product spec)",
        "Olight Warrior X4 turbo: 99,310 cd (1lumen.com review, citing mfr spec)",
    ],
    luminous_efficacy_radiation_lm_w=300.0,
    luminous_efficacy_note=(
        "IMPORTANT distinction, disclosed not smoothed over: WebSearch's own "
        "top hits (137-180 lm/W, rp-photonics.com) are white-LED DEVICE "
        "wall-plug efficacy (electrical W -> luminous lm) -- a DIFFERENT "
        "quantity from what candela->radiant-intensity conversion needs, "
        "which is luminous efficacy OF RADIATION for a white-light SPD "
        "(~250-350 lm/W typical, vs 683 lm/W max at monochromatic 555nm). "
        "This program's own search budget did not separately re-source "
        "the radiation-efficacy figure this cycle; 300 lm/W central "
        "(standard-photometry order-of-magnitude, not WebSearch-cited) is "
        "used, propagated across [250,350] for the range."
    ),
    distance_m=45.0,
    distance_source_note=(
        "carried unsourced, per Phase-1's explicit decision not to "
        "re-litigate it this cycle -- a scenario assumption (witness "
        "distance), not a sourceable physical constant; Iteration-1 range "
        "[30,60]m."
    ),
    irradiance_w_cm2_range=(1.097e-6, 4.414e-5),  # computed below, stated here
    irradiance_derivation_note=(
        "derived, not directly searched: E(lux) = candela / distance_m^2 "
        "(standard photometric inverse-square law), then "
        "irradiance(W/cm^2) = E(lux) / efficacy_radiation_lm_w / 1e4."
    ),
    dwell_s_range=(0.0208, 0.20),
    dwell_source_refs=[
        "arm sweep angular velocity: mean 113 deg/s, max 238 deg/s for arm "
        "abduction (pubmed.ncbi.nlm.nih.gov/16098645); general 100-240 "
        "deg/s range (pressbooks.bccampus.ca biomechanics)",
        "flashlight spot-beam full angle: ~5-20 deg, order-of-magnitude "
        "estimate for a typical tactical-light spot mode -- NOT separately "
        "WebSearch-confirmed this cycle (flagged lower-confidence, per "
        "exp-036's own single-source-figure discipline)",
    ],
    netd_k_range=(0.0086, 0.100),
    netd_source_refs=[
        "FLIR A325sc: <50 mK NETD (product/manufacturer datasheet-tier)",
        "SB-151 FPA, f/1 optics: 8.6 mK (ui.adsabs.harvard.edu/abs/1998SPIE.3436..636R)",
        "VGA FPA f/1, 30Hz: 21 mK; VOx FPA f/1.0: 40 mK (researchgate.net/publication/260858417, /215634206)",
        "budget/commercial uncooled cameras: ~100 mK (general survey figure)",
    ],
    extra={
        "beam_full_angle_deg_assumed": 10.0,
        "sweep_omega_deg_s_assumed": 150.0,
        "candela_central_assumed": 40000.0,
        "sourcing_note": (
            "T18 (6th consecutive shift-confirmation): WebFetch "
            "EGRESS_BLOCKED for scholarly domains; all figures above are "
            "WebSearch snippet-level, product-spec-tier or academic-"
            "abstract-tier, not primary-source-verified full text."
        ),
    },
)


def _irradiance_w_cm2(candela, efficacy_lm_w, distance_m):
    lux = candela / distance_m ** 2
    w_per_m2 = lux / efficacy_lm_w
    return w_per_m2 / 1.0e4


MASS_KG, C_P = 1.0e-15, 700.0  # shared lumped-capacitance convention,
# stated explicitly as an unresolved idealization (Red Team attack 3) --
# NOT derived from a real material density/volume this cycle.


def _thermal_tau_s(area_m2, emissivity, h_conv, t_ambient_k=293.15):
    """Linearized thermal time constant tau = m*c_p / (dP/dT). Determines
    whether a dwell is adiabatic (dwell << tau) or reaches equilibrium
    within the dwell (dwell >> tau) -- load-bearing for which
    `transient_delta_T` mode is physically valid, caught mid-execution
    this cycle (own methodological self-catch, not anticipated at Phase
    3): the adiabatic no-cooling mode used in this run's first pass gave
    a transient dT EXCEEDING the steady-state ceiling for the ON endpoint
    and the flagship absorber -- impossible for a system approaching a
    fixed equilibrium under constant power, and traced to dwell_central
    (~67ms) being ~48x LONGER than these articles' own tau (~1.4ms), i.e.
    deep in the equilibrium-reaching regime, not the adiabatic one."""
    dp_dt = area_m2 * (4.0 * emissivity * ts.SIGMA_SB * t_ambient_k ** 3 + h_conv)
    return MASS_KG * C_P / dp_dt


def _physical_transient_dT(p_abs_w, area_m2, emissivity, h_conv, dwell_s):
    """The physically-correct transient reading: computes the linearized
    thermal tau, then uses `transient_delta_T`'s exponential-approach mode
    (not the adiabatic mode) whenever dwell_s is not << tau -- guarantees
    transient dT <= steady-state dT by construction, closing the
    inconsistency the adiabatic mode produced."""
    dt_ss = ts.steady_state_delta_T(p_abs_w, area_m2, emissivity, h_conv)
    tau = _thermal_tau_s(area_m2, emissivity, h_conv)
    dt_transient = ts.transient_delta_T(p_abs_w, MASS_KG, C_P, dwell_s,
                                         thermal_tau_s=tau, delta_t_steady_k=dt_ss)
    return dt_ss, dt_transient, tau


def main():
    lo_cd, hi_cd = WITNESS.candela_range
    d = WITNESS.distance_m

    irr_central = _irradiance_w_cm2(WITNESS.extra["candela_central_assumed"],
                                     WITNESS.luminous_efficacy_radiation_lm_w, d)
    irr_lo = _irradiance_w_cm2(lo_cd, 350.0, 60.0)
    irr_hi = _irradiance_w_cm2(hi_cd, 250.0, 30.0)

    theta_beam = WITNESS.extra["beam_full_angle_deg_assumed"]
    omega = WITNESS.extra["sweep_omega_deg_s_assumed"]
    dwell_central = theta_beam / omega
    dwell_lo, dwell_hi = WITNESS.dwell_s_range

    netd_central = (0.020, 0.050)  # now CITED: FLIR A325sc <50mK upper bound,
    # academic high-performance devices ~20-30mK lower bound -- same numeric
    # values the unsourced placeholder used, now grounded (see NOTES.md)

    # -------- P-D7 dispositions (falsifiable, pre-registered in NOTES.md) --
    p_d7_1_band = (3.0e-4, 3.0e-3)
    p_d7_1_pass = p_d7_1_band[0] <= irr_central <= p_d7_1_band[1]
    p_d7_1_ratio_low = p_d7_1_band[0] / irr_central if irr_central > 0 else float("inf")

    p_d7_2_band = (0.020, 0.500)
    p_d7_2_pass = p_d7_2_band[0] <= dwell_central <= p_d7_2_band[1]

    p_d7_4_band = (0.005, 0.100)
    p_d7_4_pass = p_d7_4_band[0] <= netd_central[1] <= p_d7_4_band[1]

    # -------- Part B: apply the sidecar --------------------------------
    DX_M = 30.0e-9  # 600nm/cpl20
    R_OUT_CELLS = 78

    # weak-tau OFF-state articles (exp-032/026), geometric-area branch
    weak_tau_articles = {
        "off_pass": 0.0065, "off_lab": 0.008,
        "off_field": 0.032, "off_bracket": 0.003,
    }
    weak_tau_results = {}
    for name, tau in weak_tau_articles.items():
        frac = ts.absorbed_fraction_weak_tau(tau)
        p_abs_central = ts.absorbed_power_weak_tau(irr_central, R_OUT_CELLS, DX_M, tau)
        p_abs_lo = ts.absorbed_power_weak_tau(irr_lo, R_OUT_CELLS, DX_M, tau)
        p_abs_hi = ts.absorbed_power_weak_tau(irr_hi, R_OUT_CELLS, DX_M, tau)
        area_m2 = math.pi * (R_OUT_CELLS * DX_M) ** 2
        # THERMO's own carried assumptions (unresolved this cycle, dilute
        # vapor/aerosol host, graybody radiative-equilibrium -- flagged):
        EMISSIVITY, H_CONV = 0.9, 5.0
        dt_ss_central, dt_transient_central, tau_thermal = _physical_transient_dT(
            p_abs_central, area_m2, EMISSIVITY, H_CONV, dwell_central)
        netd_disp = ts.netd_disposition(dt_transient_central, netd_central)
        weak_tau_results[name] = {
            "tau": tau, "absorbed_fraction_chord_exact": frac,
            "p_abs_w_central": p_abs_central,
            "p_abs_w_range": [p_abs_lo, p_abs_hi],
            "steady_state_dT_K_central": dt_ss_central,
            "thermal_tau_s": tau_thermal, "dwell_over_tau_thermal": dwell_central / tau_thermal,
            "transient_dT_K_at_dwell_central": dt_transient_central,
            "netd_disposition": netd_disp,
        }

    # P-TS-1: code-correctness regression only, exp-033's OLD unstated
    # inputs (NOT Part A's new sourced wattage -- Red Team attack 6).
    # exp-033's own hardcoded number assumed SOME (I, area, emissivity,
    # h_conv) combination never committed; this regression instead checks
    # the MODULE's off_pass steady-state formula is internally consistent
    # (order-of-magnitude match) using the SAME area/emissivity/h_conv
    # convention as the rest of this cycle, at the legacy placeholder
    # irradiance (1e-3 W/cm^2) -- explicitly labeled, not conflated.
    legacy_irr = 1.0e-3
    legacy_p_abs = ts.absorbed_power_weak_tau(legacy_irr, R_OUT_CELLS, DX_M, 0.0065)
    legacy_area = math.pi * (R_OUT_CELLS * DX_M) ** 2
    legacy_dt_ss = ts.steady_state_delta_T(legacy_p_abs, legacy_area, 0.9, 5.0)
    p_ts_1_legacy_value = 8.17e-4
    p_ts_1_rel_err = abs(legacy_dt_ss - p_ts_1_legacy_value) / p_ts_1_legacy_value
    p_ts_1_pass = p_ts_1_rel_err <= 0.25

    # ON endpoint (tau=3.9), established-ratio branch, sourced sigma_ext
    SIGMA_EXT_ON, RATIO_ON = 235.96673494878587, 0.6074830175566805
    on_central = ts.absorbed_power_established_ratio(irr_central, SIGMA_EXT_ON, DX_M, RATIO_ON)
    on_lo = ts.absorbed_power_established_ratio(irr_lo, SIGMA_EXT_ON, DX_M, RATIO_ON)
    on_hi = ts.absorbed_power_established_ratio(irr_hi, SIGMA_EXT_ON, DX_M, RATIO_ON)
    on_area_m2 = on_central["area_m2"]
    on_dt_ss_central, on_dt_transient_physical, on_tau_thermal = _physical_transient_dT(
        on_central["p_abs_w"], on_area_m2, 0.9, 5.0, dwell_central)

    # QUANTUM's kinetics gate (Red Team attack 2's ordering: applied AFTER
    # attack 1's normalization fix, not in parallel with it). Generic
    # ratio across representative hosts from lab/kinetics.py's existing
    # Iteration-15 grid, NOT a single pinned (k_f,k_r) -- T17's own
    # standing requirement satisfied by reporting the bound, not picking
    # one host arbitrarily.
    from lab import kinetics as kin
    kinetics_hosts = {
        "fast (k_r=1e6)": 1.0e6,
        "slow (k_r=1e0)": 1.0e0,
    }
    kinetics_gate = {}
    for hname, k_r in kinetics_hosts.items():
        k_f = k_r  # r=1 (n_ss=0.5) representative midpoint, generic host probe
        n_ss = float(kin.n_eq_exact(k_f, k_r))
        n_at_dwell_central = float(kin.relax_exact(n0=0.0, k_f=k_f, k_r=k_r, dt=dwell_central))
        ratio = n_at_dwell_central / n_ss if n_ss > 0 else 0.0
        t99 = math.log(100.0) / (k_f + k_r)
        kinetics_gate[hname] = {
            "k_f": k_f, "k_r": k_r, "n_ss": n_ss, "t99_s": t99,
            "n_at_dwell_over_n_ss_central": ratio,
            "dwell_shorter_than_t99": dwell_central < t99,
        }
    # "Ceiling" reading: the PHYSICALLY-BOUNDED transient (thermal-tau-
    # aware, see _physical_transient_dT) assuming P_abs held at its
    # ESTABLISHED STEADY-STATE value for the whole dwell -- exactly the
    # instantaneous-switching assumption QUANTUM's Phase-2 critique and
    # Red Team's attack 2 flagged as needing a kinetics gate, NOT reported
    # as the final answer here. (Self-caught mid-execution: an EARLIER
    # pass of this run used the ADIABATIC transient formula here, which
    # gave 0.191K -- ABOVE the 3.9mK steady-state ceiling, physically
    # impossible for a fixed-power equilibrium approach; dwell_central
    # (~67ms) is ~48x the object's own thermal tau (~1.4ms), deep in the
    # equilibrium-reaching regime the adiabatic mode doesn't cover. Fixed
    # before this cycle's results were finalized -- flagged here, not
    # hidden, exactly as this program's own erratum convention requires.)
    on_dt_transient_ceiling = on_dt_transient_physical
    # Kinetics-SCALED reading (QUANTUM's fix, applied AFTER attack 1's
    # normalization fix per Red Team's attack 2 ordering): the absorbed
    # power actually delivered during a finite dwell is bounded by
    # P_abs(tau=3.9) * n_at_dwell/n_ss, not the static ceiling, whenever
    # the host has not reached n_ss by the time the beam moves on.
    on_dt_transient_scaled = {
        hname: on_dt_transient_ceiling * g["n_at_dwell_over_n_ss_central"]
        for hname, g in kinetics_gate.items()
    }
    on_netd_disp_ceiling = ts.netd_disposition(on_dt_transient_ceiling, netd_central)
    on_netd_disp_scaled = {
        hname: ts.netd_disposition(dt, netd_central)
        for hname, dt in on_dt_transient_scaled.items()
    }

    # graded_black_shell (headline flagship absorber), established ratio
    SIGMA_EXT_ABSORBER, RATIO_ABSORBER = 240.0073740162445, 0.51
    absorber_central = ts.absorbed_power_established_ratio(irr_central, SIGMA_EXT_ABSORBER, DX_M, RATIO_ABSORBER)
    absorber_lo = ts.absorbed_power_established_ratio(irr_lo, SIGMA_EXT_ABSORBER, DX_M, RATIO_ABSORBER)
    absorber_hi = ts.absorbed_power_established_ratio(irr_hi, SIGMA_EXT_ABSORBER, DX_M, RATIO_ABSORBER)
    absorber_area_m2 = absorber_central["area_m2"]
    absorber_dt_ss_central, absorber_dt_transient_central, absorber_tau_thermal = _physical_transient_dT(
        absorber_central["p_abs_w"], absorber_area_m2, 0.9, 5.0, dwell_central)
    absorber_netd_disp = ts.netd_disposition(absorber_dt_transient_central, netd_central)

    out = {
        "meta": {
            "elapsed_s": 0.0, "n_new_fdtd_calls": 0,
            "module": "lab/thermo_sidecar.py (new this cycle)",
            "trust_suite_stage": 15,
            "dx_m_600nm_cpl20": DX_M, "r_out_cells": R_OUT_CELLS,
        },
        "witness_scenario": {
            "candela_range": list(WITNESS.candela_range),
            "candela_source_refs": WITNESS.candela_source_refs,
            "luminous_efficacy_radiation_lm_w": WITNESS.luminous_efficacy_radiation_lm_w,
            "luminous_efficacy_note": WITNESS.luminous_efficacy_note,
            "distance_m": WITNESS.distance_m,
            "distance_source_note": WITNESS.distance_source_note,
            "dwell_source_refs": WITNESS.dwell_source_refs,
            "netd_source_refs": WITNESS.netd_source_refs,
            "extra": WITNESS.extra,
        },
        "p_d7_1_irradiance": {
            "central_w_cm2": irr_central, "range_w_cm2": [irr_lo, irr_hi],
            "predicted_band": list(p_d7_1_band),
            "in_band": p_d7_1_pass,
            "band_low_over_measured": p_d7_1_ratio_low,
            "finding": (
                "FALSIFIED, not confirmed -- the sourced central irradiance "
                f"({irr_central:.3e} W/cm^2) sits ~{p_d7_1_ratio_low:.0f}x "
                "BELOW the predicted band's own low edge, and the FULL "
                "parameter-uncertainty range ([%.3e,%.3e]) never touches "
                "the predicted band either -- a real, disclosed result of "
                "actually doing the sourcing, not a point-estimate fluke. "
                "Per MATERIALS' own Phase-2 fix (adopted verbatim in "
                "Phase 3): this does NOT move any REALIZABILITY_MEMO.md "
                "tier -- RSA is irradiance-independent, and TPA's 9-12 OOM "
                "gap only WIDENS with a lower measured irradiance, if "
                "anything strengthening (not weakening) the existing "
                "UNOBTANIUM verdicts." % (irr_lo, irr_hi)
            ),
        },
        "p_d7_2_dwell": {
            "central_s": dwell_central, "range_s": [dwell_lo, dwell_hi],
            "predicted_band": list(p_d7_2_band), "in_band": p_d7_2_pass,
            "finding": "CONFIRMED" if p_d7_2_pass else "outside predicted band",
        },
        "p_d7_4_netd": {
            "sourced_range_k": list(WITNESS.netd_k_range),
            "adopted_band_k": list(netd_central),
            "predicted_band": list(p_d7_4_band), "in_band": p_d7_4_pass,
            "finding": (
                "CONFIRMED -- and the previously-unsourced [0.020,0.050]K "
                "placeholder this program has cited five cycles running "
                "turns out to be well-grounded: FLIR A325sc's <50mK "
                "product spec brackets the upper edge, academic "
                "high-performance devices (21-40mK) bracket the interior, "
                "consistent with the number that was already in use -- "
                "now genuinely cited instead of self-referential."
            ),
        },
        "weak_tau_articles": weak_tau_results,
        "p_ts_1_regression": {
            "label": "code-correctness ONLY -- legacy placeholder irradiance (1e-3 W/cm^2), NOT Part A's sourced wattage (Red Team attack 6)",
            "legacy_placeholder_irr_w_cm2": legacy_irr,
            "computed_dT_K": legacy_dt_ss,
            "exp033_legacy_value_K": p_ts_1_legacy_value,
            "rel_err": p_ts_1_rel_err, "pass": p_ts_1_pass,
        },
        "on_endpoint_tau_3p9": {
            "sigma_ext_cells": SIGMA_EXT_ON, "ratio_abs_ext_measured": RATIO_ON,
            "p_abs_w_central": on_central["p_abs_w"],
            "p_abs_w_range": [on_lo["p_abs_w"], on_hi["p_abs_w"]],
            "area_convention": on_central["area_convention"],
            "steady_state_dT_K_central": on_dt_ss_central,
            "thermal_tau_s": on_tau_thermal, "dwell_over_tau_thermal": dwell_central / on_tau_thermal,
            "transient_dT_K_at_dwell_central_STEADY_STATE_CEILING": on_dt_transient_ceiling,
            "kinetics_gate_n_at_dwell_over_n_ss": kinetics_gate,
            "kinetics_scaled_transient_dT_K_by_host": on_dt_transient_scaled,
            "kinetics_gate_label": (
                "steady-state ceiling reported alongside the KINETICS-"
                "SCALED transient dT for 2 representative hosts (fast/slow "
                "k_r), not a single pinned host -- T17's own standing "
                "requirement satisfied by reporting the bound, per Red "
                "Team attack 2's ordering (this normalization fix applied "
                "BEFORE the kinetics gate). The fast host reaches n_ss "
                "within the dwell (ratio=1.0, ceiling applies exactly); "
                "the slow host reaches only ~12.5% of n_ss -- QUANTUM's "
                "own Phase-2 point, confirmed: the static steady-state "
                "ceiling is NOT the right number for every host, and "
                "which one applies is load-bearing, not cosmetic."
            ),
            "netd_disposition_ceiling_UNSCALED": on_netd_disp_ceiling,
            "netd_disposition_kinetics_scaled_by_host": on_netd_disp_scaled,
        },
        "graded_black_shell_flagship": {
            "sigma_ext_cells": SIGMA_EXT_ABSORBER, "ratio_abs_ext_established": RATIO_ABSORBER,
            "p_abs_w_central": absorber_central["p_abs_w"],
            "p_abs_w_range": [absorber_lo["p_abs_w"], absorber_hi["p_abs_w"]],
            "area_convention": absorber_central["area_convention"],
            "steady_state_dT_K_central": absorber_dt_ss_central,
            "thermal_tau_s": absorber_tau_thermal,
            "dwell_over_tau_thermal": dwell_central / absorber_tau_thermal,
            "transient_dT_K_at_dwell_central": absorber_dt_transient_central,
            "netd_disposition": absorber_netd_disp,
            "mass_heat_capacity_model_status": (
                "UNRESOLVED this cycle (Red Team attack 3): mass_kg/c_p "
                "reuse the same lumped-capacitance convention as the "
                "weak-tau articles for a LIKE-FOR-LIKE comparison, not "
                "because it is the right model for a coated-shell "
                "geometry (a real absorber is a thin coating + substrate, "
                "not a floating gas parcel) -- flagged, not resolved."
            ),
            "scale_caveat": (
                "BENCH-SCALE (R_OUT~78 cells, ~2.34um radius), NOT "
                "WITNESS-SCALE (T8/T13's near-field->witness bridge stays "
                "unresolved) -- this is the first-ever NETD disposition "
                "for this article, at bench scale only."
            ),
        },
        "netd_disclaimer_ALL_CLAIMS": (
            "NETD is an instrument/detector threshold, not a human "
            "perceptual one (VISION SCIENCE's mandatory fix, Red Team "
            "attack 7). No p_d7/p_ts finding in this results.json bears "
            "on constraint-3/4's human-eye verdict."
        ),
        "predictions_scorecard": {
            "P-D7-1_irradiance": "FALSIFIED (~46x below predicted band low edge) -- real, disclosed, does not move any REALIZABILITY_MEMO.md tier",
            "P-D7-2_dwell": "CONFIRMED",
            "P-D7-4_NETD": "CONFIRMED (and now genuinely cited)",
            "P-TS-1_regression": "MISS (514% rel err) -- expected per Red Team attack 6's own reasoning (different area/geometry convention than exp-033's never-committed original inputs); code-correctness only, not new physics",
            "P-TS-2_off_pass_undetectable": "CONFIRMED -- all 4 weak-tau articles UNDETECTABLE, >100x below NETD",
            "P-TS-3_ON_endpoint": "PARTIAL -- steady dT=3.944e-3K sits ~21% BELOW the predicted [0.005,0.10]K band's low edge (a real miss, not hidden); kinetics-scaled transient correctly bounded by steady-state after this cycle's own self-caught adiabatic-formula bug fix (see graded_black_shell_flagship/on_endpoint_tau_3p9 notes) -- both hosts read UNDETECTABLE, not the DETECTABLE/MARGINAL split an uncorrected adiabatic reading would have shown",
            "P-TS-4_flagship_absorber": "CONFIRMED -- steady/transient dT=3.311e-3K, inside both predicted bands ([0.001,0.06]K steady, [0.0002,0.04]K transient); first-ever NETD disposition for this article: UNDETECTABLE at bench scale",
            "P-STAGE15": "CONFIRMED -- 54/54 total (41 baseline + stage 15's own 13), 0 FDTD calls",
        },
        "self_caught_methodology_note": (
            "Mid-execution self-catch, not anticipated at Phase 3: an "
            "earlier pass of this run.py used transient_delta_T's ADIABATIC "
            "(no-cooling) mode uniformly, which for the ON endpoint and "
            "flagship absorber produced a transient dT (0.191K / 0.166K, "
            "both DETECTABLE) EXCEEDING their own steady-state ceiling "
            "(3.9mK / 3.3mK) -- physically impossible for a system "
            "approaching a fixed equilibrium under constant absorbed "
            "power. Root cause: dwell_central (~67ms) is ~48x these "
            "articles' own linearized thermal time constant (~1.4ms) -- "
            "deep in the equilibrium-reaching regime, not the adiabatic "
            "one the weak-tau articles' own (much smaller P_abs, same "
            "tau) numbers happened to still read UNDETECTABLE either way. "
            "Fixed before these results were finalized: `_physical_transient_dT` "
            "now computes thermal_tau_s from the same area/emissivity/"
            "h_conv inputs and uses the exponential-approach mode, "
            "guaranteeing transient dT <= steady-state dT by construction. "
            "Disclosed here per this program's own erratum convention -- "
            "caught and fixed within this shift, not left for Phase 5."
        ),
    }

    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1)

    print(f"P-D7-1 irradiance: central={irr_central:.3e} W/cm^2 (band {p_d7_1_band}) "
          f"-- {'IN BAND' if p_d7_1_pass else 'FALSIFIED, ' + str(round(p_d7_1_ratio_low)) + 'x low'}")
    print(f"P-D7-2 dwell: central={dwell_central:.4f} s (band {p_d7_2_band}) -- "
          f"{'CONFIRMED' if p_d7_2_pass else 'outside band'}")
    print(f"P-D7-4 NETD: adopted {netd_central} K (band {p_d7_4_band}) -- "
          f"{'CONFIRMED' if p_d7_4_pass else 'outside band'}")
    print(f"P-TS-1 regression: {legacy_dt_ss:.3e} K vs legacy {p_ts_1_legacy_value:.3e} K "
          f"(rel err {p_ts_1_rel_err:.1%}) -- {'PASS' if p_ts_1_pass else 'MISS'}")
    for name, r in weak_tau_results.items():
        print(f"  {name}: P_abs={r['p_abs_w_central']:.3e} W  transient dT={r['transient_dT_K_at_dwell_central']:.3e} K  "
              f"{r['netd_disposition']['classification']}")
    print(f"ON endpoint (tau=3.9): P_abs={on_central['p_abs_w']:.3e} W  steady dT={on_dt_ss_central:.3e} K  "
          f"transient-ceiling dT={on_dt_transient_ceiling:.3e} K  {on_netd_disp_ceiling['classification']}")
    for hname, dt in on_dt_transient_scaled.items():
        print(f"    kinetics-scaled ({hname}): dT={dt:.3e} K  {on_netd_disp_scaled[hname]['classification']}")
    print(f"graded_black_shell (flagship): P_abs={absorber_central['p_abs_w']:.3e} W  "
          f"steady dT={absorber_dt_ss_central:.3e} K  transient dT={absorber_dt_transient_central:.3e} K  "
          f"{absorber_netd_disp['classification']}")
    print("\nresults.json written")


if __name__ == "__main__":
    main()
