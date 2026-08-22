"""exp-056 -- The T26 Near-Null Generalization Test: measurement harness.
============================================================================
Panel Iteration 33 (lead: VISION SCIENCE). Predictions committed in
NOTES.md BEFORE this file's first run (house discipline). Geometry from
design_geometry.py.

3 NEW FDTD calls: off_pass_joint, off_bracket_joint (native r=78, cpl=20,
N=9 simultaneous coherent) + empty_joint_cpl30 (rescaled r=117, cpl=30,
N=9 simultaneous coherent, R3 check on T26's own empty-scene artifact).
Window-position sensitivity (P-VIS-4) and the thermo sidecar (mandatory
fix 4) are extracted from the SAME three captures, zero marginal cost:
`sections.phasors` retains the FULL 2D field, so `observer_profile` can be
evaluated at multiple x-planes post-hoc from one run, and
`sections.radial_absorbed_power` reads absorbed power directly off the
held capture.
"""

import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, HERE)

import numpy as np

import design_geometry as dg
from lab import Sim, ambient as amb, sections as sc


def build_native(sim, article):
    if article in dg.ARTICLES:
        cx, cy = dg.OBJ
        x = np.arange(sim.nx)[:, None]
        y = np.arange(sim.ny)[None, :]
        mask = (x - cx) ** 2 + (y - cy) ** 2 <= dg.R_OUT ** 2
        sim.sigma_e[mask] += dg.SIGMA_BY_ARTICLE[article]
        sim.objects.append({"type": "uniform_sponge_disk",
                            "params": {"cx": cx, "cy": cy, "r": dg.R_OUT,
                                       "sigma": dg.SIGMA_BY_ARTICLE[article],
                                       "tau_center": dg.TAU_BY_ARTICLE[article]}})


def run_native_joint(article):
    """article: 'off_pass' or 'off_bracket'. N=9 simultaneous sources,
    fixed zero relative phase, amplitude=1.0 each."""
    sim = Sim(dg.NX, dg.NY, cells_per_lambda=dg.CPL, courant_frac=dg.COURANT_FRAC,
              absorb=dg.ABSORB)
    build_native(sim, article)
    for ang in dg.FALLBACK_ANGLES:
        sim.add_line_source(dg.SRC_X, angle_deg=float(ang), edge=dg.TAPER, amplitude=1.0)
    sim.run(dg.STEPS)
    cap = sc.full_capture(sim)
    return sim, cap


def run_rescaled_empty_joint():
    sim = Sim(dg.NX_R, dg.NY_R, cells_per_lambda=dg.CPL_R, courant_frac=dg.COURANT_FRAC_R,
              absorb=dg.ABSORB_R)
    for ang in dg.FALLBACK_ANGLES:
        sim.add_line_source(dg.SRC_X_R, angle_deg=float(ang), edge=dg.TAPER_R, amplitude=1.0)
    sim.run(dg.STEPS_R)
    cap = sc.full_capture(sim)
    return sim, cap


def profile_at(ph, plane_x, y_lo, y_hi):
    return amb.observer_profile(ph, plane_x, y_lo, y_hi)


def window_scan(ph, obj_x, r_out, dx_list, y_lo, y_hi, y0, w_obj, guard_out, w_flank):
    """Post-hoc window-position sensitivity: re-evaluate the profile at
    several x-planes (dx offsets from the object edge) from ONE capture."""
    out = {}
    for dx in dx_list:
        plane_x = obj_x - r_out - dx
        b = profile_at(ph, plane_x, y_lo, y_hi)
        o, f = amb.window_means(b, y_lo, y0, w_obj, guard_out, w_flank)
        out[int(dx)] = {"plane_x": plane_x, "b_obj": o, "b_flank": f, "C": amb.weber(o, f)}
    return out


def main():
    t0 = time.time()
    n_calls = 0
    results = {"meta": {"experiment": "exp-056", "panel_iteration": 33,
                        "lead": "VISION SCIENCE", "t1_escape_route": "NONE (instrument work)"}}

    # ------------------------------------------------ native joint legs
    native = {}
    for article in ("off_pass", "off_bracket"):
        sim, cap = run_native_joint(article)
        n_calls += 1
        ph = sc.phasors(cap)
        print(f"  [{n_calls}/3] native joint {article} (N=9, r=78, cpl=20)", flush=True)

        b_primary = profile_at(ph, dg.PLANE_X, dg.ABSORB, dg.NY - dg.ABSORB)
        b_obj, b_flank = amb.window_means(b_primary, dg.ABSORB, dg.OBJ[1], dg.W_OBJ,
                                           dg.GUARD_OUT, dg.W_FLANK)
        c_joint = amb.weber(b_obj, b_flank)
        c_naive = dg.C_NAIVE_ESTABLISHED[article]

        # Red Team mandatory fix 1 (EM): flag whether the object's presence
        # has collapsed the flank-window denominator toward a near-null,
        # which would make a large |C_joint| a Weber-ratio artifact rather
        # than a genuine unsuppressed-interference finding (EM's attack:
        # Cauchy-Schwarz bounds raw flux, NOT the C ratio, which has no
        # finite passivity ceiling). Comparator: the SAME injection
        # modality's own flank reading on the empty scene at this geometry
        # (exp-055, established, apples-to-apples -- more direct than a
        # cross-modality naive/incoherent comparator, which isn't on record
        # for off_pass/off_bracket in the first place).
        flank_ratio_vs_empty_joint = b_flank / dg.EMPTY_JOINT_FLANK_RAW_NATIVE_ESTABLISHED
        flank_denominator_flag = flank_ratio_vs_empty_joint < 0.20

        # window-position sensitivity, zero marginal cost (same capture)
        sens = window_scan(ph, dg.OBJ_X, dg.R_OUT, dg.PLANE_DX_SENS_NATIVE,
                           dg.ABSORB, dg.NY - dg.ABSORB, dg.OBJ[1], dg.W_OBJ,
                           dg.GUARD_OUT, dg.W_FLANK)

        # thermo sidecar: FDTD-measured absorbed power off the SAME capture
        # (zero marginal cost) -- mandatory fix 4, Director-scoped (see
        # NOTES.md: no naive-incoherent absorbed-power anchor exists in
        # this program's record to compare against; that would need the
        # 18 individual legs re-run with full captures retained, which
        # neither exp-032 nor this cycle does -- named as follow-on, not
        # built here, same structural reason Red Team deferred QUANTUM's
        # fuller redesign).
        _, _, p_abs_joint = sc.radial_absorbed_power(cap, sim.sigma_e, dg.OBJ[0], dg.OBJ[1], dg.R_OUT)

        native[article] = {
            "C_joint": c_joint, "b_obj_joint": b_obj, "b_flank_joint": b_flank,
            "C_naive_established": c_naive,
            "flank_ratio_vs_empty_joint": flank_ratio_vs_empty_joint,
            "flank_denominator_flag": flank_denominator_flag,
            "window_position_sensitivity": sens,
            "p_abs_joint_measured": p_abs_joint,
        }
        print(f"      C_joint={c_joint:.6f} (naive={c_naive:.6f})  "
              f"flank_ratio={flank_ratio_vs_empty_joint:.4f} flag={flank_denominator_flag}  "
              f"p_abs_joint={p_abs_joint:.6e}", flush=True)

    # -------------------------------------------- rescaled empty R3 leg
    sim_r, cap_r = run_rescaled_empty_joint()
    n_calls += 1
    ph_r = sc.phasors(cap_r)
    print(f"  [{n_calls}/3] rescaled empty joint (N=9, r=117, cpl=30, R3 check)", flush=True)

    b_primary_r = profile_at(ph_r, dg.PLANE_X_R, dg.ABSORB_R, dg.NY_R - dg.ABSORB_R)
    eo_r, ef_r = amb.window_means(b_primary_r, dg.ABSORB_R, dg.OBJ_R[1], dg.W_OBJ_R,
                                   dg.GUARD_OUT_R, dg.W_FLANK_R)
    c_empty_joint_r3 = amb.weber(eo_r, ef_r)

    sens_r = window_scan(ph_r, dg.OBJ_X_R, dg.R_OUT_R, dg.PLANE_DX_SENS_R,
                         dg.ABSORB_R, dg.NY_R - dg.ABSORB_R, dg.OBJ_R[1], dg.W_OBJ_R,
                         dg.GUARD_OUT_R, dg.W_FLANK_R)

    print(f"      C_empty_joint(cpl30)={c_empty_joint_r3:.6f} "
          f"(cpl20 established={dg.C_EMPTY_JOINT_NATIVE_ESTABLISHED:.6f})", flush=True)

    # ---------------------------------------------------------- scoring
    results["native_joint"] = native
    results["rescaled_r3"] = {
        "C_empty_joint_cpl30": c_empty_joint_r3,
        "C_empty_joint_cpl20_established": dg.C_EMPTY_JOINT_NATIVE_ESTABLISHED,
        "C_empty_naive_cpl30_established": dg.C_EMPTY_NAIVE_RESCALED_ESTABLISHED,
        "window_position_sensitivity": sens_r,
    }
    results["phantom_control_zero_cost"] = {
        "note": "sigma=0/eps_r=1 'phantom' disk is physically identical to "
                "vacuum -- the established native empty_joint value below "
                "IS that control point (tau=0), reused at zero cost "
                "(Director's Phase-3 override of Red Team docket item 3).",
        "tau_0_C_joint": dg.C_EMPTY_JOINT_NATIVE_ESTABLISHED,
        "tau_0_C_naive": dg.C_EMPTY_NAIVE_NATIVE_ESTABLISHED,
    }
    results["meta"]["n_fdtd_calls"] = n_calls
    results["meta"]["elapsed_s"] = time.time() - t0

    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\ndone in {time.time() - t0:.0f} s, {n_calls} FDTD calls, results -> {out_path}")


if __name__ == "__main__":
    main()
