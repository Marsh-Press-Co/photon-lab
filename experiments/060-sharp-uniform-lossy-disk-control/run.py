"""
exp-060 -- Panel Iteration 37: the sharp-uniformly-lossy-disk FDTD control.
============================================================================
Lead: MATERIALS & METAMATERIALS. exp-059's own Iteration-36 Phase-5 top-
ranked queue item -- a rare six-way seat convergence, five of six seats
ranked it #1. Disentangles two mechanisms exp-059's PEC-reference
comparison conflated: does the flagship absorber's measured sub-PEC
Q_ext suppression (Q_ext=1.5385, 72.6% of the exact PEC reference
Q_ext_PEC(24.5044)=2.1177) come from its graded/adiabatic entry
specifically, or from any sufficiently lossy disk, sharp-edged or not?

Two articles, same PEC core (R_CORE=30) and outer radius (R_COAT=78,
identical to the real flagship construction), same total optical depth
(matched by equal radial line-integral of sigma across the shell -- see
Idealizations, NOTES.md, and materials.uniform_lossy_shell's own
docstring for the caveat this convention carries):
  - "graded": materials.graded_black_shell(R_CORE, R_COAT) -- reproduces
    experiments/002-cross-sections/results.json::absorber-600 EXACTLY, a
    regression anchor for this cycle's own harness before anything new
    is trusted.
  - "uniform": materials.uniform_lossy_shell(R_CORE, R_COAT, sigma_flat),
    sigma_flat = 0.5 * (181/462) ~= 0.19589 derived in NOTES.md.

Measured via lab.sections (Q_ext, back_frac, abs_frac, box_dev -- exp-002's
own idiom, unmodified) PLUS lab.sections.angular_scattered_pattern (new
instrumentation this cycle, PHOTONICS' Phase-2 mandatory fix: the
aggregate channels alone cannot attribute a difference to EDGE-specific
diffraction vs a magnitude-only diffuse effect) PLUS lab.thermo_sidecar's
established chain (THERMODYNAMICS' Phase-2 mandatory fix: route the new
measurement through the free energy sidecar before Phase-3 freeze).

Predictions committed to git BEFORE this script's official run (house
discipline, non-negotiable) -- see NOTES.md.

    python3 experiments/060-sharp-uniform-lossy-disk-control/run.py
"""

import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))

import numpy as np

from lab import Sim, materials
from lab import sections as sc
from lab import thermo_sidecar as ts

# --------------------------------------------------------- exp-002/020 geometry, verbatim
N, ABSORB, FRAC, STEPS = 560, 40, 0.32, 3200
CPL, NM = 20, 600
CX, CY = 252, 280
R_CORE, R_COAT = 30, 78
SRC_X = 64
BOX_A = (142, 362, 170, 390)
BOX_B = (117, 387, 145, 415)
REF = (CX, CY, 60)

# ------------------------------------------------------------- sigma_flat derivation
# graded_black_shell's profile: sigma(r) = sigma_max * s(d(r))^2, quintic
# smoothstep s(d) = 6d^5-15d^4+10d^3, d = clip((r_out-r)/(r_out-r_in),0,1).
# Matched-optical-depth convention (equal radial line-integral of sigma
# across the shell -- ONE disclosed convention among possible others, see
# NOTES.md Idealizations and materials.uniform_lossy_shell's own
# docstring; a peak-sigma-matched or transmission-matched convention
# would yield a different sigma_flat, and this convention does NOT match
# true field-attenuation depth once loss is order-unity -- a real,
# disclosed ~8.3% residual, trust-suite stage 22 gate 4):
#   integral_0^1 s(d)^2 dd = 181/462 exactly (term-by-term polynomial
#   integration of s(d)^2 = 36d^10-180d^9+345d^8-300d^7+100d^6)
#   sigma_flat = sigma_max * (181/462)
SIGMA_MAX = 0.5
SIGMA_FLAT = SIGMA_MAX * (181.0 / 462.0)   # 0.1958874458874459
TAU_MATCHED = SIGMA_FLAT * (R_COAT - R_CORE)   # 9.402597402597403 (line-integral units)

# ----------------------------------------------------- THERMO sidecar constants
# Reused verbatim from experiments/057-.../run.py (silicon rho=2330 kg/m^3,
# c_p=700 J/(kg*K) -- ASSUMED, provenance terminates unsourced, T18;
# REALIZABILITY_MEMO.md's standing downgrade -- not re-litigated here).
DX_M = 30.0e-9
R_OUT_M = R_COAT * DX_M
K_AIR = 0.026
DENSITY_SI_KG_M3, C_P_SI_J_KGK = 2330.0, 700.0
EMISSIVITY = 0.9
T_AMBIENT_K = 293.15
NETD_BAND_K = (0.020, 0.050)
# irr_central: back-derived from experiments/057's own reused
# P_ABS_W_FLAGSHIP_CENTRAL=1.7409069740390205e-12 W (itself exp-043's
# docket-7 witness-scenario irradiance, never re-derived by exp-057) via
# the exact inverse of absorbed_power_established_ratio's own formula, so
# this cycle's own irr_central reproduces exp-057's own established
# p_abs_w EXACTLY when fed the same SIGMA_EXT_CELLS/RATIO_ABS_EXT --
# verified below as a same-shift regression assertion before use.
IRR_CENTRAL_W_CM2 = 6.584362139917695e-06
_ESTABLISHED_SIGMA_EXT_CELLS = 240.0073740162445
_ESTABLISHED_RATIO_ABS_EXT = 0.51
_ESTABLISHED_P_ABS_W = 1.7409069740390205e-12


def build(scene, sim):
    if scene == "graded":
        materials.pec_disk(sim, CX, CY, R_CORE)
        materials.graded_black_shell(sim, CX, CY, R_CORE, R_COAT,
                                     sigma_max=SIGMA_MAX)
    elif scene == "uniform":
        materials.pec_disk(sim, CX, CY, R_CORE)
        materials.uniform_lossy_shell(sim, CX, CY, R_CORE, R_COAT, SIGMA_FLAT)
    elif scene != "empty":
        raise ValueError(scene)


def run_scene(scene):
    sim = Sim(N, N, cells_per_lambda=CPL, courant_frac=FRAC, absorb=ABSORB)
    build(scene, sim)
    sim.add_line_source(SRC_X)
    sim.run(STEPS)
    return sc.full_capture(sim)


def thermo_chain(sigma_ext_cells, ratio_abs_ext):
    """The established absorbed_power_established_ratio -> mixed_length_
    scale_regime -> netd_disposition chain, exp-057's own convention
    verbatim (THERMODYNAMICS' Iteration-37 Phase-2 mandatory fix)."""
    p = ts.absorbed_power_established_ratio(IRR_CENTRAL_W_CM2, sigma_ext_cells,
                                            DX_M, ratio_abs_ext)
    regime = ts.mixed_length_scale_regime(
        p["p_abs_w"], R_OUT_M, K_AIR, DENSITY_SI_KG_M3, C_P_SI_J_KGK, EMISSIVITY,
        T_AMBIENT_K)
    disp = ts.netd_disposition(regime["dt_ss_full_K"], NETD_BAND_K)
    margin = NETD_BAND_K[0] / regime["dt_ss_full_K"]
    return {"p_abs_w": p["p_abs_w"], "dt_ss_full_K": regime["dt_ss_full_K"],
            "margin": margin, "classification": disp["classification"],
            "netd_disclaimer": disp["disclaimer"]}


def main():
    t0 = time.time()
    # regression assertion: this cycle's own irr_central must reproduce
    # exp-057's established P_ABS_W_FLAGSHIP_CENTRAL exactly when fed the
    # same established sigma_ext/ratio (pins the back-derivation before
    # it's trusted for the new article).
    check = ts.absorbed_power_established_ratio(
        IRR_CENTRAL_W_CM2, _ESTABLISHED_SIGMA_EXT_CELLS, DX_M, _ESTABLISHED_RATIO_ABS_EXT)
    assert check["p_abs_w"] == _ESTABLISHED_P_ABS_W, (
        f"irr_central regression FAILED: {check['p_abs_w']!r} != {_ESTABLISHED_P_ABS_W!r}")

    print(f"sigma_flat={SIGMA_FLAT:.10f}  tau_matched={TAU_MATCHED:.10f}", flush=True)

    caps = {}
    for scene in ("empty", "graded", "uniform"):
        print(f"--- scene = {scene} ---", flush=True)
        caps[scene] = run_scene(scene)

    results = {}
    widths_by_scene = {}
    for scene in ("graded", "uniform"):
        wa = sc.widths(caps[scene], caps["empty"], BOX_A, REF)
        wb = sc.widths(caps[scene], caps["empty"], BOX_B, REF)
        box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])
        cross_dev = abs(wa["sigma_ext_cross"] - wa["sigma_ext"]) / abs(wa["sigma_ext"])
        r = {k: wa[k] for k in ("sigma_scat", "sigma_abs", "sigma_ext",
                                "sigma_ext_cross", "back_frac", "fwd_frac")}
        r["q_ext"] = wa["sigma_ext"] / (2.0 * R_COAT)
        r["abs_frac"] = wa["sigma_abs"] / wa["sigma_ext"]
        r["box_dev"] = box_dev
        r["cross_dev"] = cross_dev
        widths_by_scene[scene] = wa
        results[scene] = r
        print(f"  {scene:8s}: sig_ext={r['sigma_ext']:8.2f}  Q_ext={r['q_ext']:.4f}  "
              f"abs/ext={r['abs_frac']:.4f}  back={r['back_frac']:.3e}  "
              f"boxdev={box_dev:.4f}  crossdev={cross_dev:.4f}", flush=True)

    # regression anchor: "graded" must reproduce experiments/002's own
    # established absorber-600 numbers EXACTLY (same geometry/source/box/
    # ref, deterministic engine) -- this cycle's own harness sanity check
    # before anything NEW (the uniform article) is trusted.
    q_ext_graded_established = 1.5385088077964393
    back_frac_graded_established = 2.0834765227893057e-06
    abs_frac_graded_established = 0.5118033079980887
    q_ext_dev = abs(results["graded"]["q_ext"] - q_ext_graded_established)
    back_frac_dev = abs(results["graded"]["back_frac"] - back_frac_graded_established)
    abs_frac_dev = abs(results["graded"]["abs_frac"] - abs_frac_graded_established)
    print(f"[regression] graded vs exp-002/absorber-600: "
          f"dQ_ext={q_ext_dev:.3e}  dback_frac={back_frac_dev:.3e}  dabs_frac={abs_frac_dev:.3e}",
          flush=True)

    # angular scattered pattern (PHOTONICS' mandatory fix): shape, not
    # just magnitude -- does the uniform article's excess scattering
    # concentrate near the forward/grazing diffraction lobe (edge-driven)
    # or spread diffusely (bulk-loss-only)?
    centers, pat_graded = sc.angular_scattered_pattern(caps["graded"], caps["empty"], BOX_A, REF)
    _, pat_uniform = sc.angular_scattered_pattern(caps["uniform"], caps["empty"], BOX_A, REF)

    # self-consistency identity (per angular_scattered_pattern's own
    # docstring: sum(pattern) == sigma_scat is NOT an independent physics
    # check, an implementation identity -- verify before trusting shape)
    sum_dev_graded = abs(float(np.sum(pat_graded)) - widths_by_scene["graded"]["sigma_scat"]) / \
        abs(widths_by_scene["graded"]["sigma_scat"])
    sum_dev_uniform = abs(float(np.sum(pat_uniform)) - widths_by_scene["uniform"]["sigma_scat"]) / \
        abs(widths_by_scene["uniform"]["sigma_scat"])

    excess = pat_uniform - pat_graded
    forward_cone = np.abs(centers) > 150.0   # within 30 deg of the exact forward direction
    backward_cone = np.abs(centers) < 30.0   # within 30 deg of the exact backward direction
    total_abs_excess = float(np.sum(np.abs(excess)))
    frac_forward = float(np.sum(np.abs(excess[forward_cone]))) / total_abs_excess
    frac_backward = float(np.sum(np.abs(excess[backward_cone]))) / total_abs_excess

    print(f"[angular] sum-identity dev: graded={sum_dev_graded:.4f}  uniform={sum_dev_uniform:.4f}",
          flush=True)
    print(f"[angular] excess concentration: forward_cone(|theta|>150)={frac_forward:.4f}  "
          f"backward_cone(|theta|<30)={frac_backward:.4f}", flush=True)

    # THERMO sidecar (mandatory fix): route both articles through the
    # established chain, POST-RUN ANALYTIC, not an FDTD output.
    thermo_graded = thermo_chain(results["graded"]["sigma_ext"], results["graded"]["abs_frac"])
    thermo_uniform = thermo_chain(results["uniform"]["sigma_ext"], results["uniform"]["abs_frac"])
    print(f"[thermo] graded:  margin={thermo_graded['margin']:.2f}x  {thermo_graded['classification']}",
          flush=True)
    print(f"[thermo] uniform: margin={thermo_uniform['margin']:.2f}x  {thermo_uniform['classification']}",
          flush=True)

    out = {
        "sigma_flat": SIGMA_FLAT,
        "sigma_max": SIGMA_MAX,
        "tau_matched": TAU_MATCHED,
        "matched_optical_depth_caveat": (
            "sigma_flat derived by matching the RAW conductivity line-integral "
            "(equal integral_{r_in}^{r_out} sigma dr) -- ONE disclosed convention "
            "among possible others (a peak-sigma-matched or transmission-matched "
            "convention would yield a different sigma_flat). This convention does "
            "NOT match true field-attenuation depth once loss is order-unity: "
            "Im(n(sigma)) is concave in sigma at this bench's own grid "
            "normalization (t=sigma_e*cpl/(2*pi), the physical loss tangent), so "
            "by Jensen's inequality the graded profile's TRUE attenuation-weighted "
            "depth sits ~8.3% below the flat profile's uniform value despite "
            "identical raw line integrals by construction (QUANTUM OPTICS' "
            "Iteration-37 Phase-2 finding, independently reconfirmed by Red Team, "
            "pinned as trust-suite stage 22 gate 4's regression anchor). This "
            "caveat travels with sigma_flat/tau_matched everywhere they are cited "
            "in this results.json and NOTES.md (Iteration-37 Red Team mandatory "
            "fix, closing VISION SCIENCE's caveat-placement catch)."),
        "widths": results,
        "regression_check_graded_vs_exp002": {
            "q_ext_established": q_ext_graded_established,
            "q_ext_dev": q_ext_dev,
            "back_frac_established": back_frac_graded_established,
            "back_frac_dev": back_frac_dev,
            "abs_frac_established": abs_frac_graded_established,
            "abs_frac_dev": abs_frac_dev,
        },
        "angular_pattern": {
            "bin_centers_deg": centers.tolist(),
            "sigma_scat_per_bin_graded": pat_graded.tolist(),
            "sigma_scat_per_bin_uniform": pat_uniform.tolist(),
            "sum_identity_dev_graded": sum_dev_graded,
            "sum_identity_dev_uniform": sum_dev_uniform,
            "excess_frac_forward_cone_gt150deg": frac_forward,
            "excess_frac_backward_cone_lt30deg": frac_backward,
        },
        "thermo_sidecar": {
            "graded": thermo_graded,
            "uniform": thermo_uniform,
            "irr_central_w_cm2": IRR_CENTRAL_W_CM2,
            "irr_central_provenance": (
                "back-derived from experiments/057's own reused "
                "P_ABS_W_FLAGSHIP_CENTRAL via the exact inverse of "
                "absorbed_power_established_ratio's formula -- verified by a "
                "same-shift regression assertion (see run.py main()) before use, "
                "NOT independently re-sourced this cycle"),
            "expressibility_note": (
                "POST-RUN ANALYTIC calculation (PANEL.md's expressibility "
                "contract) -- not an FDTD output."),
        },
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=2, sort_keys=True)
    print(f"exp-060 run complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
