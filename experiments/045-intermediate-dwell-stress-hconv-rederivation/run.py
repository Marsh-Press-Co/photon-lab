"""exp-045 -- Panel Iteration 22: the intermediate-dwell coupled kinetics-
thermal stress sweep (Block A) + THERMODYNAMICS' h_conv/mass_kg
re-derivation bundled with ELECTROMAGNETISM's own T22 geometric-disk-vs-
`iso_xsec_sq` area table entry (Block B) + QUANTUM's dose-accumulation
sensitivity check (Block C, added at Phase 3 per Red Team's mandatory fix
5, overriding the Phase-1 draft's deferral). Lead: ELECTROMAGNETISM.

PHASE 3 REVISION NOTE (Director's synthesis, per Red Team's Phase-2 audit,
`phase2_redteam_audit.md` -- read that file for the full attack list): the
Phase-1 draft's Block B mixed two different characteristic lengths inside
what it called a single "first-principles" derivation (h_eff via the bench's
geometric r_out=2.34um; mass_kg/area via the extinction-width w_on=7.079um)
and named the wrong material (PMMA, with a citation that does not check out
-- grep-verified zero hits anywhere else in this repo) for the grid Block A
actually models (Hosts A-D are linearly-pumped FCA in doped silicon/
germanium, T17/exp-037/038). Both defects are corrected below, PRE-RUN --
per house discipline this is a Phase-3 fix to what gets committed and run,
not a post-hoc erratum (T10's "flag, don't rewrite" convention applies to
POST-run discoveries; nothing here has been run yet). The Phase-1 draft's
own text survives unedited in phase1_proposal.md as the historical record
of what Phase 1 proposed and Phase 2 critiqued -- see phase2_*.md for the
full seven-file critique/audit record.

Corrections applied (Red Team's 8 mandatory fixes, phase2_redteam_audit.md
Section 4):
  1. ONE consistent characteristic length per h_eff/mass/area chain, not two
     silently mixed. Two self-consistent regimes are computed and reported
     side by side (w_on-consistent -- the established-ratio branch's own
     already-adopted area convention -- and r_out-consistent -- the bench's
     real geometric radius), not the naive mixed pairing, which is dropped
     from the code entirely (it was never a legitimate reading).
  2. Material identity corrected: PMMA replaced with silicon (rho=2330
     kg/m^3, c_p=700 J/(kg*K), kappa=148 W/(m*K) -- all three ALREADY cited,
     sourced, and used in experiments/037-fca-combined-media-literature-
     check/NOTES.md line 828-829 for this identical Host A-D mechanism).
     The fabricated PMMA citation is deleted, not merely relabeled.
  3. TAU_TH_REGIMES now contains genuinely self-consistent Block-B entries
     (both length-scale readings), computed by the code, not asserted in
     prose after the fact -- Red Team's explicit concern (Attack 7:
     "unfalsifiable in practice" as originally coded).
  4. Biot number computed for the ADOPTED silicon identity (not left at
     THERMODYNAMICS' own PMMA-based Bi=0.137): Bi=k_air/k_solid is
     algebraically length-scale-invariant (Red Team Attack 6) but NOT
     material-invariant -- silicon's own high conductivity (148 W/(m*K)
     versus PMMA's ~0.19) drops Bi by ~3 orders of magnitude. This is a
     genuine Director-level refinement of Red Team's own "structural, all
     regimes" framing: the Biot concern was specific to the (now-superseded)
     PMMA identity, not a property of the h_eff=k_air/L formula alone.
     Disclosed explicitly below, not silently dropped.
  5. Block C -- QUANTUM's dose-accumulation/population-memory sensitivity
     check -- ADDED this shift (overriding the Phase-1 draft's deferral,
     per Red Team's override ruling, Attack 9). Reuses
     `lab.kinetics.pulse_train_segments`, targeting Host D at all 4 ratios,
     the 5*tau/0.5*tau inter-sweep-gap bounding pair from exp-038's own
     established convention. Implementation note: `pulse_train_segments`'s
     own parameter roles (an "ambient" rate the "pulse" multiplies by A) fit
     exp-038's ambient+enhancement picture, not exp-045's own single-ON-rate
     grid -- so roles are used INVERTED here: the "ambient" argument slot
     carries the ON/exposure rate (duration dwell_central) and the "pulse"
     slot (A=0.0) carries the OFF/inter-sweep relaxation gap (duration =
     the swept dt_gap). This reuses the function's actual segment-building
     logic unmodified; only which argument means what is remapped, disclosed
     here rather than silently done. Scope: reports the population-memory
     ratio (periodic/first-pulse peak n, exp-038's own established metric)
     and a DECOUPLED delta-T estimate (dt_ss_full * n) at both readings --
     NOT a new closed-form coupled-ODE solution for nonzero initial
     population, which is out of scope for a "bounded" check (disclosed
     idealization, not silently skipped).
  6. NETD disclaimer now stored per-point (the full `netd_disposition()`
     dict, not just its classification string) at every sweep/Block-C point,
     plus one console print and inline placement at the P-EM45-A1/A2/C
     prediction text in NOTES.md.
  7. One real cross-consistency assertion added (`h_eff` and `mass_kg`/area
     must be built from the SAME length variable in each self-consistent
     regime) so this exact bug class cannot silently recur.
  8. Knudsen-number correction disclosed as a stated sensitivity line for
     BOTH length-scale regimes (not just r_out's).

Zero FDTD calls throughout. Pure desk/analytic arithmetic reusing
already-verified machinery (`lab.kinetics`, stage-12-gated; `lab.
thermo_sidecar`, stage-15-gated) plus one already-verified, not-yet-promoted
closed form (`coupled_kinetics_thermal_dT`, Red Team's Iteration-21 Phase-2
derivation, reused VERBATIM from experiments/044/run.py).
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
EMISSIVITY, H_CONV_OLD, MASS_KG_OLD, C_P_OLD = 0.9, 5.0, 1.0e-15, 700.0
T_AMBIENT_K = 293.15
NETD_DISCLAIMER = (
    "NETD is an instrument/detector threshold, not a human perceptual one "
    "(VISION SCIENCE's standing mandatory fix, exp-043 Red Team attack 7, "
    "exp-044 mandatory fix 6, exp-045 Phase-2 mandatory fix 6). This "
    "classification does NOT bear on constraint-3/4's human-eye verdict.")


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
    one of that cycle's 16 grid points; re-verified independently a third
    time this cycle by Red Team, phase2_redteam_audit.md -- not re-derived,
    not modified). Assumes n(0)=0 -- Block C's population-memory readings
    are reported as a separate DECOUPLED estimate, not fed through this
    closed form (see module docstring, fix 5 scope note)."""
    tau_k = 1.0 / (k_f + k_r)
    n_ss = k_f / (k_f + k_r)
    if abs(tau_k - tau_thermal_s) < 1e-12 * max(tau_k, tau_thermal_s):
        raise ValueError("degenerate tau_k == tau_thermal_s, not expected on this grid")
    bracket = (1.0
               - (tau_k / (tau_k - tau_thermal_s)) * math.exp(-dwell_s / tau_k)
               + (tau_thermal_s / (tau_k - tau_thermal_s)) * math.exp(-dwell_s / tau_thermal_s))
    return dt_ss_full * n_ss * bracket


def coupled_segment_general(k_f, k_r, dt_ss_full, tau_thermal_s, dt, n0, dT0):
    """Fix 9 (Phase-5 Red Team audit): a GENERALIZED closed-form solve of
    the same coupled ODE as `coupled_kinetics_thermal_dT`, but for an
    arbitrary segment starting population n0 and temperature dT0, not just
    n0=0/dT0=0 -- derived this shift (Director, Phase 5 close) to commit
    EM's own Phase-5 finding (the decoupled shortcut is conservative --
    an OVER-estimate -- at every Block-C point tested) into the permanent
    record as actual computed data, not only a Phase-5 review file's prose.

    Standard linear-ODE solve (integrating factor e^{t/tau_th}) of
        dn/dt  = k_f*(1-n) - k_r*n,                          n(0)=n0
        dDT/dt = (1/tau_th)*(dt_ss_full*n(t) - DT),           DT(0)=dT0
    Reduces EXACTLY to `coupled_kinetics_thermal_dT`'s own formula at
    n0=0/dT0=0 (verified symbolically and re-confirmed numerically below,
    at import time is overkill -- see the assertion in main()).

    Returns (n_final, dT_final) at t=dt."""
    n_eq = k_f / (k_f + k_r)
    tau_k = 1.0 / (k_f + k_r)
    n_final = n_eq + (n0 - n_eq) * math.exp(-dt / tau_k)
    if abs(tau_k - tau_thermal_s) < 1e-12 * max(tau_k, tau_thermal_s):
        raise ValueError("degenerate tau_k == tau_thermal_s, not expected on this grid")
    dT_final = (dT0 * math.exp(-dt / tau_thermal_s)
                + dt_ss_full * n_eq * (1.0 - math.exp(-dt / tau_thermal_s))
                + dt_ss_full * (n0 - n_eq) * (tau_k / (tau_k - tau_thermal_s))
                  * (math.exp(-dt / tau_k) - math.exp(-dt / tau_thermal_s)))
    return n_final, dT_final


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
    tau_thermal_s_old = MASS_KG_OLD * C_P_OLD / dp_dt_old

    # ==================================================================
    # BLOCK B -- h_conv / mass_kg re-derivation + T22 area table
    # (computed BEFORE Block A so its corrected numbers feed Block A's
    # dwell-sweep regimes). FIX 1+2: one consistent length per regime;
    # silicon identity, not PMMA.
    # ==================================================================
    K_AIR_W_MK = 0.026  # room-temperature air thermal conductivity, textbook value
    r_out_m = R_OUT_CELLS * DX_M
    w_on_m = SIGMA_EXT_ON * DX_M  # iso_xsec_sq width -- the established-ratio
    # branch's OWN already-adopted length convention for area/absorbed power
    # (ts.absorbed_power_established_ratio itself uses this, not r_out)

    geometric_disk_area_m2 = math.pi * r_out_m ** 2
    iso_area_on_m2 = w_on_m ** 2
    iso_area_absorber_m2 = (SIGMA_EXT_ABSORBER * DX_M) ** 2
    area_ratio_on = iso_area_on_m2 / geometric_disk_area_m2
    area_ratio_absorber = iso_area_absorber_m2 / geometric_disk_area_m2

    # Silicon, fix 2 -- all three constants already sourced and used in
    # experiments/037-fca-combined-media-literature-check/NOTES.md line
    # 828-829 for this identical Host A-D (linearly-pumped FCA) mechanism.
    # NOT independently re-sourced this cycle (T18 WebFetch still blocked) --
    # reused from this program's own prior, already-cited literature figure.
    # (Moved earlier this shift, Phase-5 fix 6, so the sigma_ext-flatness
    # sensitivity check below can use it too.)
    DENSITY_SI_KG_M3 = 2330.0
    C_P_SI = 700.0
    K_SI_W_MK = 148.0

    # Fix 6 (Phase-5 Red Team audit, PHOTONICS' catch): w_on was promoted
    # this cycle into a physical LENGTH SCALE feeding h_eff/mass/area --
    # exp-044's own achromatic-flatness finding (0.45% relative) checked
    # ONLY sigma_abs/sigma_ext, never sigma_ext itself. Computed here from
    # exp-026's own already-committed 3-lambda beam_scene data (zero new
    # cost) -- the ON-endpoint's own sigma_ext varies MORE than its ratio.
    _exp026_path = os.path.join(ROOT, "experiments", "026-sigma-i-endpoints", "results.json")
    with open(_exp026_path) as _f:
        _exp026 = json.load(_f)
    _sigma_ext_by_lambda = {lam: _exp026["beam_scene"][lam]["sigma_ext"] for lam in ("450", "600", "750")}
    _sext_vals = list(_sigma_ext_by_lambda.values())
    _sext_spread_rel_pct = (max(_sext_vals) - min(_sext_vals)) / _sigma_ext_by_lambda["600"] * 100.0
    # Sensitivity: recompute w_on-consistent dwell/tau_thermal at each
    # lambda's own sigma_ext (holding silicon identity + RATIO_ON fixed --
    # only the length scale itself varies) to confirm the headline P-IT22-A6
    # conclusion (below N_TRANSIENT_TAU=25) survives across the sweep.
    _sensitivity_by_lambda = {}
    for _lam, _sext in _sigma_ext_by_lambda.items():
        _w = _sext * DX_M
        _h = K_AIR_W_MK / _w
        _area = _w ** 2
        _mass = DENSITY_SI_KG_M3 * _w ** 3
        _dpdt = _area * (4.0 * EMISSIVITY * ts.SIGMA_SB * T_AMBIENT_K ** 3 + _h)
        _p_abs = irr_central * _area * 1.0e4 * RATIO_ON
        _tau_th = _mass * C_P_SI / _dpdt
        _sensitivity_by_lambda[_lam] = {"sigma_ext_cells": _sext, "dwell_over_tau_thermal": dwell_central / _tau_th}
    sigma_ext_flatness = {
        "sigma_ext_by_lambda_cells": _sigma_ext_by_lambda,
        "spread_relative_percent": _sext_spread_rel_pct,
        "comparison_note": (
            f"sigma_ext itself varies {_sext_spread_rel_pct:.2f}% relative across "
            "450/600/750nm -- roughly 5x exp-044's own sigma_abs/sigma_ext RATIO "
            "flatness (0.45%). This is the quantity w_on (=sigma_ext*dx) is built "
            "from, so it was an UNCHECKED assumption, not a verified one, that "
            "using it as a physical length scale for h_eff/mass is achromatic -- "
            "caught at Phase 5 (PHOTONICS), not disclosed at Phase 1/3."),
        "dwell_over_tau_thermal_sensitivity_by_lambda": _sensitivity_by_lambda,
        "headline_survives_note": (
            "Confirmed harmless: dwell/tau_thermal(w_on-consistent, silicon) "
            "stays in [20.3x,21.3x] across all 3 swept wavelengths -- the "
            "P-IT22-A6 headline (below N_TRANSIENT_TAU=25) is robust to this "
            "gap, though the gap itself was real and undisclosed until Phase 5."),
        "flagship_absorber_gap_note": (
            "The SAME check for graded_black_shell (the flagship absorber, "
            "T22's OTHER area-ratio entry, 3.014x) could not be extended this "
            "shift: no 3-lambda sigma_ext series for that article exists "
            "anywhere in this repo (grep-confirmed) -- only the single 600nm "
            "value (240.007 cells, exp-043) has ever been measured. Disclosed "
            "as a real, standing gap, not silently skipped -- a candidate "
            "companion 3-lambda run for a future cycle, not scoped this shift."),
    }

    def self_consistent_regime(length_m, length_name):
        """FIX 7: the one cross-consistency assertion -- h_eff and
        mass_kg/area are built from the SAME length variable by
        construction (the function only takes one `length_m`), not
        asserted after the fact. A future edit that re-introduces two
        different lengths in this chain would have to do so explicitly,
        not silently."""
        h_eff = K_AIR_W_MK / length_m
        area_m2 = length_m ** 2
        volume_m3 = length_m ** 3
        mass_kg = DENSITY_SI_KG_M3 * volume_m3
        dp_dt = area_m2 * (4.0 * EMISSIVITY * ts.SIGMA_SB * T_AMBIENT_K ** 3 + h_eff)
        dt_ss_full = on_central["p_abs_w"] / dp_dt if length_name == "w_on" else \
            (irr_central * area_m2 * 1.0e4 * RATIO_ON) / dp_dt
        # both branches physically equivalent for area=w_on^2 (established-
        # ratio convention); the r_out branch recomputes p_abs_w against the
        # GEOMETRIC area explicitly rather than reusing on_central's own
        # w_on-based p_abs_w, since p_abs_w and area must share one length
        # too (fix 7's own logic applied consistently to power, not just
        # thermal mass).
        tau_thermal_s = mass_kg * C_P_SI / dp_dt
        bi = h_eff * length_m / K_SI_W_MK  # Biot number, fix 4
        # Knudsen number + first-order thermal-slip correction, fix 8
        # (THERMODYNAMICS' own derivation, re-applied at this length scale):
        # lambda_air ~= 65.7nm at 293K/1atm (kinetic-theory mean free path)
        lambda_air_m = 65.7e-9
        kn = lambda_air_m / length_m
        h_eff_slip_corrected = h_eff / (1.0 + 2.0 * kn)
        assert abs(h_eff * length_m - K_AIR_W_MK) < 1e-15 * K_AIR_W_MK, \
            "h_eff*L must reproduce k_air exactly (fix 7 cross-consistency)"
        assert abs(mass_kg - DENSITY_SI_KG_M3 * length_m ** 3) < 1e-30, \
            "mass_kg must be built from the SAME length_m as h_eff (fix 7)"
        return {
            "length_convention": length_name, "length_m": length_m,
            "h_eff_w_m2k": h_eff, "area_m2": area_m2, "mass_kg": mass_kg,
            "dp_dt_w_k": dp_dt, "dt_ss_full_K": dt_ss_full,
            "tau_thermal_s": tau_thermal_s,
            "dwell_over_tau_thermal": dwell_central / tau_thermal_s,
            "biot_number": bi,
            "biot_disclaimer": (
                "Bi=h_eff*L/k_solid is algebraically length-scale-invariant "
                "(cancels L; Red Team Attack 6) but NOT material-invariant -- "
                "this value uses silicon's own kappa=148 W/(m*K). Under the "
                "Phase-1 draft's PMMA identity (kappa~=0.19 W/(m*K)), Bi "
                "would be ~0.137, marginal for the lumped-capacitance "
                "assumption; under the adopted silicon identity it is "
                "negligible (~1.8e-4) -- deeply lumped-valid. The Biot "
                "concern was specific to the superseded PMMA identity, not "
                "structural across every possible material choice."),
            "note_vs_redteam_audit_table": (
                "phase2_redteam_audit.md's own Attack-3 table includes a "
                "'MATERIALS' fix alone' row (r_out h_eff, Si density, w_on "
                "mass) reading 64.2x -- that row was NOT fully "
                "length-scale-self-consistent (it kept mass on w_on while "
                "changing only h_eff/density), an intermediate diagnostic "
                "step in Red Team's own investigation, not a final "
                "candidate. This regime (r_out used for BOTH h_eff AND "
                "mass/area, fix 7's own cross-consistency requirement) is a "
                "different, genuinely self-consistent reading the audit "
                "table did not compute -- expect a different number "
                "(194.2x, not 64.2x) for that reason, not because of a "
                "discrepancy with the audit."),
            "knudsen_number": kn,
            "h_eff_slip_corrected_w_m2k": h_eff_slip_corrected,
            "slip_correction_relative": (h_eff_slip_corrected - h_eff) / h_eff,
            "slip_correction_note": (
                "First-order thermal-slip correction (THERMODYNAMICS, "
                "Phase-2, re-applied here at this length scale), disclosed "
                "as a sensitivity bound -- not applied to the headline "
                "h_eff above."),
        }

    regime_w = self_consistent_regime(w_on_m, "w_on")
    regime_r = self_consistent_regime(r_out_m, "r_out")

    block_b = {
        "length_scale_regimes": {"w_on_consistent": regime_w, "r_out_consistent": regime_r},
        "primary_headline_regime": "w_on_consistent",
        "primary_regime_rationale": (
            "w_on is the established-ratio branch's OWN already-adopted "
            "length convention for area/absorbed power "
            "(ts.absorbed_power_established_ratio uses it, not r_out) -- "
            "using it for h_eff/mass too keeps the WHOLE established-ratio "
            "energy chain on one consistent length, per Red Team's own "
            "recommendation (phase2_redteam_audit.md fix 1). The r_out "
            "regime is reported alongside as a genuine, equally-legitimate "
            "alternate convention (T22's own committed purpose is exactly "
            "to compare these two conventions), not as a discredited "
            "'mixed' reading -- the Phase-1 draft's actual bug (mixing "
            "BOTH lengths inside one regime) does not appear in either "
            "regime here."),
        "material_identity": {
            "material": "silicon (doped Si/Ge FCA host, matching Block A's own grid)",
            "density_kg_m3": DENSITY_SI_KG_M3, "c_p_j_kgk": C_P_SI, "k_solid_w_mk": K_SI_W_MK,
            "source": "experiments/037-fca-combined-media-literature-check/NOTES.md line 828-829 (already-cited, already-sourced for this identical Host A-D mechanism)",
            "superseded_material": "PMMA (Phase-1 draft) -- deleted: the material was wrong for Block A's own grid (Hosts A-D are doped-Si/Ge FCA, not a photochromic dye-in-polymer host) AND its citation was fabricated (grep -rl PMMA across this repo returns zero hits outside exp-045's own files) -- see phase2_redteam_audit.md Attack 4.",
        },
        "t22_area_table": {
            "geometric_disk_area_m2": geometric_disk_area_m2,
            "geometric_disk_formula": "pi * (R_OUT_CELLS * dx_m)^2 -- the bench's own real simulated disk",
            "iso_xsec_sq_area_on_endpoint_m2": iso_area_on_m2,
            "area_ratio_iso_over_geometric_on_endpoint": area_ratio_on,
            "iso_xsec_sq_area_absorber_m2": iso_area_absorber_m2,
            "area_ratio_iso_over_geometric_absorber": area_ratio_absorber,
            "t22_established_range_note": "matches T22's own established 2.9-3.0x inflation figure (exp-043/044) at both bench geometries measured to date -- ON endpoint 2.913x, graded_black_shell flagship 3.014x",
        },
        "sigma_ext_wavelength_flatness_check": sigma_ext_flatness,  # fix 6 (Phase-5 Red
        # Team audit, PHOTONICS' catch): w_on was promoted this cycle into a
        # physical LENGTH SCALE (not just a ratio input) -- exp-044's own
        # achromatic-flatness finding (0.45% relative) checked ONLY
        # sigma_abs/sigma_ext, never sigma_ext itself. Computed here from
        # exp-026's own already-committed 3-lambda data (zero new cost).
        "old_uncorrected_reference": {
            "dt_ss_full_K": dt_ss_full_old, "tau_thermal_s": tau_thermal_s_old,
            "h_conv_w_m2k": H_CONV_OLD, "mass_kg": MASS_KG_OLD, "c_p": C_P_OLD,
            "note": "the ORIGINAL placeholder carried since exp-032 -- h_conv=5.0 (macroscopic natural convection), mass_kg=1e-15 (arbitrary), c_p=700 (never attributed to a material). Kept as the sweep's own baseline regime, not because it is believed correct.",
        },
        "phase1_defect_note": (
            "The Phase-1 draft's own 'fully_corrected_pmma' regime (h_eff via "
            "r_out=2.34um, mass_kg via w_on=7.079um, PMMA density+unmatched "
            "C_P=700) mixed both length conventions inside one claimed-"
            "consistent chain -- Red Team's Attack 1/2 (phase2_redteam_"
            "audit.md). That regime is NOT reproduced here; it was never a "
            "legitimate physical reading, only a bug. The two regimes above "
            "(w_on_consistent, r_out_consistent) are the Phase-3-corrected "
            "replacement, each internally self-consistent."
        ),
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
        "fully_corrected_si_w_consistent": (regime_w["tau_thermal_s"], regime_w["dt_ss_full_K"]),
        "fully_corrected_si_r_out_consistent": (regime_r["tau_thermal_s"], regime_r["dt_ss_full_K"]),
    }

    # Phase-5 mandatory fix 5 (Red Team's final audit, phase5_redteam_audit.md):
    # the Biot-number caveat was originally stored only twice (once per
    # Block-B regime dict) -- the identical block-scope-only pattern
    # Iteration 21 flagged for h_conv, recurring for Biot (THERMODYNAMICS'
    # Phase-5 catch). Propagated here to every sweep point whose regime
    # actually uses an h_eff-derived tau_thermal (the two silicon-corrected
    # regimes); the three h_conv=5.0-placeholder regimes never touch h_eff,
    # so Biot is not applicable there (None, not a fabricated number).
    BIOT_BY_REGIME = {
        "fully_corrected_si_w_consistent": (regime_w["biot_number"], regime_w["biot_disclaimer"]),
        "fully_corrected_si_r_out_consistent": (regime_r["biot_number"], regime_r["biot_disclaimer"]),
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
                        biot_number, biot_disclaimer = BIOT_BY_REGIME.get(regime_name, (None, None))
                        sweep_points.append({
                            "host": host, "r": r, "k_f": k_f, "k_r": k_r,
                            "tau_kinetics_s": tau_k, "n_ss": n_ss,
                            "regime": regime_name, "tau_thermal_s": tau_th,
                            "dt_ss_full_K": dt_ss, "axis": axis_name, "R": Rv,
                            "dwell_s": dwell,
                            "exact_coupled_dT_K": exact_dT,
                            "decoupled_shortcut_dT_K": decoupled_dT,
                            "relative_difference": rel_diff,
                            "netd": netd,  # FIX 6: full dict (incl. disclaimer), not just classification
                            "biot_number": biot_number,  # fix 5: per-point, not block-scope-only;
                            "biot_disclaimer": biot_disclaimer,  # None for the 3 h_conv-placeholder
                            # regimes, which never touch h_eff -- not a fabricated number.
                        })

    def worst_for(host=None, axis=None, regime=None):
        pts = sweep_points
        if host is not None:
            pts = [p for p in pts if p["host"] == host]
        if axis is not None:
            pts = [p for p in pts if p["axis"] == axis]
        if regime is not None:
            pts = [p for p in pts if p["regime"] == regime]
        return max(pts, key=lambda p: p["relative_difference"])

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
        p["netd"]["classification"] != "DETECTABLE" for p in sweep_points)

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

    n_ss_max = max(k_f / (k_f + k_r) for host, k_r in HOSTS for k_f in
                   [r * k_r for r in RATIOS])
    ceiling_bounds = {regime: dt_ss * n_ss_max for regime, (tau_th, dt_ss) in TAU_TH_REGIMES.items()}
    ceiling_check = all(
        p["exact_coupled_dT_K"] <= ceiling_bounds[p["regime"]] * (1 + 1e-9)
        for p in sweep_points
    )

    block_a = {
        "hosts_ratios_grid": {"HOSTS": HOSTS, "RATIOS": RATIOS, "n_points": len(HOSTS) * len(RATIOS)},
        "R_grid_0.1x_to_10x": R_GRID,
        "tau_thermal_regimes": {k: {"tau_thermal_s": v[0], "dt_ss_full_K": v[1]}
                                 for k, v in TAU_TH_REGIMES.items()},
        "n_sweep_points": len(sweep_points),
        "sweep_points": sweep_points,
        "per_host_axis_worst_case_summary_uncorrected_regime": per_host_axis_summary,
        "global_max_dT_K": global_max_dT["exact_coupled_dT_K"],
        "global_max_dT_point": {k: global_max_dT[k] for k in ("host", "r", "regime", "axis", "R", "dwell_s")},
        "global_max_dT_netd_lo_margin": NETD_BAND_K[0] / global_max_dT["exact_coupled_dT_K"],
        "all_points_undetectable_or_better": all_undetectable_or_better,
        "theoretical_ceiling_bounds_K": ceiling_bounds,
        "theoretical_ceiling_check_holds_everywhere": ceiling_check,
        "host_d_witness_dwell_consistency_check": host_d_witness_check,
        "netd_disclaimer": NETD_DISCLAIMER,
        "short_dwell_relative_error_note": (
            "At the SMALL-R end of the sweep (R~0.1) for Hosts A/B/C, relative "
            "difference can read as large as O(10)-O(1e7) -- this is an EXPECTED, "
            "benign artifact (relative-error blowup at a vanishing absolute scale), "
            "NOT a new physical finding. The absolute dT at every such point "
            "remains many orders of magnitude below NETD -- see global_max_dT_K."
        ),
    }

    # ==================================================================
    # BLOCK C -- QUANTUM's dose-accumulation / population-memory
    # sensitivity check (ADDED at Phase 3, overriding the Phase-1 draft's
    # deferral -- Red Team mandatory fix 5). Host D, all 4 ratios, the
    # 5*tau/0.5*tau inter-sweep-gap bounding pair (exp-038's own
    # established convention), n_pulses=5 (exp-038's own N_PULSES).
    # See module docstring for the pulse_train_segments role-inversion note.
    # ==================================================================
    k_r_d = 10.0
    block_c_points = {}
    for r in RATIOS:
        k_f_on = r * k_r_d
        tau_k = 1.0 / (k_f_on + k_r_d)
        for gap_name, dt_gap in (("5tau", 5.0 * tau_k), ("0.5tau", 0.5 * tau_k)):
            # role inversion (see docstring): "ambient" slot = ON rate,
            # duration dwell_central; "pulse" slot (A=0.0) = OFF/relaxation
            # gap, duration dt_gap.
            segs = kin.pulse_train_segments(
                k_f_ambient=k_f_on, k_r=k_r_d, A=0.0,
                T_pulse=dt_gap, dt_sweep=dwell_central, n_pulses=5)
            n_final, t_arr, n_arr = kin.integrate_segments(segs, n0=0.0, method="exp", record=True)
            # segment list: [ON, OFF] * 5 + [ON]. Boundaries after each ON
            # segment are at indices 1, 3, 5, 7, 9, 11 (0-indexed t_arr/n_arr
            # boundary list starts at t=0=index 0).
            on_end_idx = [1, 3, 5, 7, 9, 11]
            n_at_on_end = [float(n_arr[i]) for i in on_end_idx]
            n_first, n_periodic = n_at_on_end[0], n_at_on_end[-1]
            ratio = n_periodic / n_first if n_first > 0 else float("inf")

            dt_ss = regime_w["dt_ss_full_K"]  # primary regime, per Block B
            tau_th = regime_w["tau_thermal_s"]
            dT_first_decoupled = dt_ss * n_first
            dT_periodic_decoupled = dt_ss * n_periodic
            netd_first = ts.netd_disposition(dT_first_decoupled, NETD_BAND_K)
            netd_periodic = ts.netd_disposition(dT_periodic_decoupled, NETD_BAND_K)

            # Fix 9: walk the SAME 11-segment sequence through the exact
            # coupled ODE (n AND DT together), committing EM's own Phase-5
            # closure (the decoupled shortcut is conservative) as actual
            # computed data.
            _n_walk, _dT_walk = 0.0, 0.0
            _dT_at_on_end = []
            for _seg_k_f, _seg_k_r, _seg_dur in segs:
                _n_walk, _dT_walk = coupled_segment_general(
                    _seg_k_f, _seg_k_r, dt_ss, tau_th, _seg_dur, _n_walk, _dT_walk)
                _dT_at_on_end.append(_dT_walk)
            # _dT_at_on_end has one entry per segment (ON,OFF,ON,OFF,...,ON);
            # ON-segment endpoints are at the same 0-indexed positions as
            # on_end_idx minus 1 (segs is 0-indexed per-segment, not per-
            # boundary-including-t=0 like t_arr/n_arr).
            _on_seg_idx = [0, 2, 4, 6, 8, 10]
            dT_exact_at_on_end = [_dT_at_on_end[i] for i in _on_seg_idx]
            dT_exact_first = dT_exact_at_on_end[0]
            dT_exact_periodic = dT_exact_at_on_end[-1]
            exact_vs_decoupled_ratio_first = dT_exact_first / dT_first_decoupled if dT_first_decoupled > 0 else float("nan")
            exact_vs_decoupled_ratio_periodic = dT_exact_periodic / dT_periodic_decoupled if dT_periodic_decoupled > 0 else float("nan")
            # self-check: coupled_segment_general must reduce to
            # coupled_kinetics_thermal_dT exactly at n0=0/dT0=0 (the first
            # ON segment starts cold by construction).
            _n_check, _dT_check = coupled_segment_general(k_f_on, k_r_d, dt_ss, tau_th, dwell_central, 0.0, 0.0)
            _dT_ref = coupled_kinetics_thermal_dT(k_f_on, k_r_d, dt_ss, tau_th, dwell_central)
            assert abs(_dT_check - _dT_ref) < 1e-9 * max(abs(_dT_ref), 1e-30), \
                "coupled_segment_general must reduce to coupled_kinetics_thermal_dT at n0=dT0=0"

            block_c_points[f"r{r:.0e}_{gap_name}"] = {
                "r": r, "gap_name": gap_name,  # stored explicitly -- do NOT
                # filter on the dict key string: "0.5tau" ends with the
                # substring "5tau", so a naive key.endswith("5tau") check
                # silently matches BOTH gap settings (a real bug caught and
                # fixed during this script's own Phase-3 dry run, before
                # any commit -- see NOTES.md).
                "k_f_on": k_f_on, "k_r": k_r_d, "tau_kinetics_s": tau_k,
                "dt_gap_s": dt_gap, "n_pulses": 5, "dwell_central_s": dwell_central,
                "n_at_each_on_end": n_at_on_end,
                "n_first_pulse": n_first, "n_periodic": n_periodic,
                "periodic_over_first_ratio": ratio,
                "dT_first_decoupled_K": dT_first_decoupled,
                "dT_periodic_decoupled_K": dT_periodic_decoupled,
                "netd_first": netd_first, "netd_periodic": netd_periodic,
                # fix 9: the exact coupled-ODE trajectory through the SAME
                # segment sequence (not just population, but temperature
                # too), committing EM's own Phase-5 closure as data.
                "dT_exact_first_K": dT_exact_first,
                "dT_exact_periodic_K": dT_exact_periodic,
                "exact_vs_decoupled_ratio_first": exact_vs_decoupled_ratio_first,
                "exact_vs_decoupled_ratio_periodic": exact_vs_decoupled_ratio_periodic,
                "decoupled_is_conservative_first": dT_exact_first <= dT_first_decoupled,
                "decoupled_is_conservative_periodic": dT_exact_periodic <= dT_periodic_decoupled,
            }

    max_ratio_5tau = max(v["periodic_over_first_ratio"] for v in block_c_points.values() if v["gap_name"] == "5tau")
    max_ratio_05tau = max(v["periodic_over_first_ratio"] for v in block_c_points.values() if v["gap_name"] == "0.5tau")
    max_dT_periodic = max(v["dT_periodic_decoupled_K"] for v in block_c_points.values())
    max_dT_exact_periodic = max(v["dT_exact_periodic_K"] for v in block_c_points.values())
    all_c_undetectable = all(v["netd_periodic"]["classification"] != "DETECTABLE" for v in block_c_points.values())
    all_decoupled_conservative = all(v["decoupled_is_conservative_periodic"] and v["decoupled_is_conservative_first"]
                                      for v in block_c_points.values())
    worst_exact_vs_decoupled = min(v["exact_vs_decoupled_ratio_periodic"] for v in block_c_points.values())

    block_c = {
        "status": "RUN (Phase 3 override of the Phase-1 draft's deferral, per Red Team mandatory fix 5)",
        "scope_note": (
            "Reports the population-memory ratio (periodic/first-pulse peak "
            "n, exp-038's own established metric), a DECOUPLED delta-T "
            "estimate (dt_ss_full * n) at both readings, AND (fix 9, Phase-5 "
            "close) the EXACT coupled-ODE delta-T through the same segment "
            "sequence via `coupled_segment_general` -- a from-scratch "
            "generalization of `coupled_kinetics_thermal_dT` to nonzero "
            "segment-start population/temperature, derived and self-checked "
            "against the original formula at n0=dT0=0 (see the in-script "
            "assertion). Commits EM's own Phase-5 finding (the decoupled "
            "proxy is conservative at every point tested) as permanent, "
            "independently re-runnable data, not only a Phase-5 review "
            "file's prose. T_pulse(=dwell_central)=66.7ms here, vs "
            "exp-038's own T_pulse=100ms -- a DIFFERENT pulse duration, not "
            "a reproduction of exp-038's own numbers, though the same Host "
            "D / 5tau-0.5tau convention. The OFF gap uses a hard k_f=0 "
            "(disclosed idealization, QUANTUM's Phase-5 catch) -- unlike "
            "exp-038's own 'ambient' segments, which are never a true dark "
            "state; this is why exp-045's own 0.5tau ratio (1.4509) reads "
            "~13% above exp-038's own Host-D-specific 0.5tau maximum "
            "(1.2865, not the looser programwide 1.4-1.6 band)."
        ),
        "points": block_c_points,
        "max_periodic_over_first_ratio_5tau": max_ratio_5tau,
        "max_periodic_over_first_ratio_0.5tau": max_ratio_05tau,
        "max_dT_periodic_decoupled_K": max_dT_periodic,
        "max_dT_periodic_exact_K": max_dT_exact_periodic,
        "max_dT_periodic_netd_lo_margin": NETD_BAND_K[0] / max_dT_periodic if max_dT_periodic > 0 else float("inf"),
        "all_points_undetectable_or_better": all_c_undetectable,
        "decoupled_proxy_conservative_at_every_point": all_decoupled_conservative,
        "worst_case_exact_vs_decoupled_ratio": worst_exact_vs_decoupled,
        "conservative_bound_note": (
            f"exact/decoupled ratio ranges down to {worst_exact_vs_decoupled:.4f} "
            "across all 8 points (i.e. the exact coupled solution sits up to "
            f"{(1.0-worst_exact_vs_decoupled)*100:.1f}% BELOW the decoupled "
            "estimate) -- the decoupled proxy used for classification is an "
            "OVER-estimate, never an under-estimate, at every point this "
            "cycle tested (EM's Phase-5 finding, independently spot-checked "
            "sound by Red Team's own audit). Not a general proof for "
            "arbitrary future host/gap choices -- see NOTES.md."
        ),
        "netd_disclaimer": NETD_DISCLAIMER,
    }

    out = {
        "meta": {"elapsed_s": 0.0, "n_new_fdtd_calls": 0,
                 "trust_suite_stage": "reuses stages 12/15 (lab.kinetics, lab.thermo_sidecar); "
                                       "coupled_kinetics_thermal_dT reused verbatim from exp-044, "
                                       "no new formal trust-suite stage this cycle -- backed by "
                                       "exp-044's own scipy cross-check (Block A) PLUS this "
                                       "script's own cross-consistency assertions (Block B, fix 7), "
                                       "which specifically close the gap Red Team's Attack 10 found "
                                       "in the Phase-1 draft's own (inadequate) justification"},
        "block_a_intermediate_dwell_sweep": block_a,
        "block_b_hconv_mass_rederivation_and_t22_table": block_b,
        "block_c_dose_accumulation_kinetics": block_c,
        "netd_disclaimer_ALL_CLAIMS": NETD_DISCLAIMER,
    }

    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1, default=float)

    print("=" * 70)
    print("BLOCK B -- h_conv/mass_kg re-derivation (silicon identity, two self-consistent length regimes)")
    print(f"  w_on-consistent (PRIMARY): h_eff={regime_w['h_eff_w_m2k']:.1f} W/(m^2K), "
          f"tau_thermal={regime_w['tau_thermal_s']*1e3:.4f}ms, "
          f"dwell/tau_thermal={regime_w['dwell_over_tau_thermal']:.1f}x, Bi={regime_w['biot_number']:.2e}")
    print(f"  r_out-consistent (alternate): h_eff={regime_r['h_eff_w_m2k']:.1f} W/(m^2K), "
          f"tau_thermal={regime_r['tau_thermal_s']*1e3:.4f}ms, "
          f"dwell/tau_thermal={regime_r['dwell_over_tau_thermal']:.1f}x, Bi={regime_r['biot_number']:.2e}")
    print(f"  T22 area ratio (iso_xsec_sq/geometric-disk): ON-endpoint={area_ratio_on:.4f}x, "
          f"flagship absorber={area_ratio_absorber:.4f}x")
    print(f"  NOTE: {NETD_DISCLAIMER}")
    print()
    print(f"BLOCK A: {len(sweep_points)} sweep points across {len(HOSTS)*len(RATIOS)} host/ratio "
          f"points x {len(TAU_TH_REGIMES)} tau_thermal regimes x 2 axes x {N_R} R-values")
    print(f"  global max dT anywhere in sweep: {global_max_dT['exact_coupled_dT_K']:.4e} K "
          f"at {global_max_dT['host']}/r={global_max_dT['r']:.0e}/{global_max_dT['regime']}/"
          f"axis-{global_max_dT['axis']}/R={global_max_dT['R']:.2f} "
          f"({NETD_BAND_K[0]/global_max_dT['exact_coupled_dT_K']:.1f}x below netd_lo) -- {NETD_DISCLAIMER}")
    print(f"  ALL {len(sweep_points)} points UNDETECTABLE-or-better: {all_undetectable_or_better} -- {NETD_DISCLAIMER}")
    print(f"  theoretical ceiling bound holds everywhere: {ceiling_check}")
    print(f"  Host-D witness-dwell reproduction (should match exp-044's 1.44-1.50%):")
    for k, v in host_d_witness_check.items():
        print(f"    {k}: rel_diff={v['rel_diff_at_dwell_central']:.4%}  "
              f"matches_exp044_band={v['matches_exp044_band_1.44_1.50pct']}")
    print()
    print(f"BLOCK C: dose-accumulation check, Host D, {len(block_c_points)} points")
    print(f"  max periodic/first ratio: 5tau={max_ratio_5tau:.4f}, 0.5tau={max_ratio_05tau:.4f}")
    print(f"  max periodic dT (decoupled estimate): {max_dT_periodic:.4e} K "
          f"({NETD_BAND_K[0]/max_dT_periodic:.1f}x below netd_lo) -- {NETD_DISCLAIMER}")
    print(f"  ALL Block-C points UNDETECTABLE-or-better: {all_c_undetectable} -- {NETD_DISCLAIMER}")
    print("results.json written")


if __name__ == "__main__":
    main()
