"""exp-027 -- Settling, Spread, and the PEC Ablation: measurement harness.
============================================================================
Panel Iteration 4 (lead ELECTROMAGNETISM; synthesis: Director, post Red
Team's proceed-with-mandatory-fixes -- all 7 items incorporated, see
NOTES.md Phase 3 and design_geometry.py's module docstring).

Three blocks, all on the already-validated exp-001/002/026 beam-scene bench,
zero new `lab/` engine code:

  Block 1 -- settling-time diagnostic (fix 2: ALL 3 lambda, not just the
             flanks). ON article, BEAM_STEPS 3200 (reused from exp-026's
             results.json, NOT rerun) vs 6400 (fresh). 3 x (empty+on) = 6
             new sim calls.
  Block 2 -- R3 spatial companion, cpl x1.5 per lambda, BEAM_STEPS held
             native (3200). Geometry from design_geometry.BLOCK2_GEOM (the
             pinned design calculation, fix 4). 3 x (empty+on) = 6 new sim
             calls.
  Block 3 -- PEC-ablation factorial (T9), lambda=600nm only, native
             cpl=20/BEAM_STEPS=3200. 4 cells (empty, A, B, C), all freshly
             captured (self-containment discipline, exp-026's own
             precedent). Cell B's interior fill uses STRICT inequality
             (fix 1). Reports raw P_abs/I_inc per cell (fix 6).

Total NEW FDTD sim calls: 6 + 6 + 4 = 16.

Predictions committed in NOTES.md BEFORE this file's first run (house
discipline, non-negotiable).
"""

import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, HERE)

import design_geometry as dg
from lab import Sim, materials as mat, sections as sc
from lab import emit as em

# exp-026's own BEAM_STEPS=3200 beam-behind numbers, reused not rerun (source:
# experiments/026-sigma-i-endpoints/results.json, beam_scene block).
EXP026_BEAM_BEHIND_3200 = dict(dg.ESTABLISHED_BEAM_BEHIND_3200)


# --------------------------------------------------------------- Block 1
def build_beam_on(sim, cx, cy, r_out):
    x = np.arange(sim.nx)[:, None]
    y = np.arange(sim.ny)[None, :]
    mask = (x - cx) ** 2 + (y - cy) ** 2 <= r_out ** 2
    sim.sigma_e[mask] += dg.SIGMA_ON


def run_beam_scene(article, cpl, n, cx, cy, r_out, src_x, absorb, steps, frac=dg.BEAM_FRAC):
    sim = Sim(n, n, cells_per_lambda=cpl, courant_frac=frac, absorb=absorb)
    if article == "on":
        build_beam_on(sim, cx, cy, r_out)
    sim.add_line_source(src_x)
    sim.run(steps)
    cap_full = sc.full_capture(sim)
    cap_qp = (cap_full["ez_a"], cap_full["hy_a"],
              cap_full["ez_b"], cap_full["hy_b"], cap_full["off"])
    return sim, cap_full, cap_qp


def block1_one(lam_nm, cpl):
    """Native geometry, BEAM_STEPS=6400 (extended). Returns beam-behind
    fraction at the extended step count, for comparison against exp-026's
    already-measured 3200-step number (dg.ESTABLISHED_BEAM_BEHIND_3200)."""
    t0 = time.time()
    sim_e, cap_e, capqp_e = run_beam_scene(
        "empty", cpl, dg.BEAM_N, dg.BEAM_CX, dg.BEAM_CY, dg.R_OUT,
        dg.BEAM_SRC_X, dg.BEAM_ABSORB, dg.BEAM_STEPS_EXTENDED)
    env_e = np.sqrt(cap_e["ez_a"] ** 2 + cap_e["ez_b"] ** 2)

    sim, cap, capqp = run_beam_scene(
        "on", cpl, dg.BEAM_N, dg.BEAM_CX, dg.BEAM_CY, dg.R_OUT,
        dg.BEAM_SRC_X, dg.BEAM_ABSORB, dg.BEAM_STEPS_EXTENDED)
    env = np.sqrt(cap["ez_a"] ** 2 + cap["ez_b"] ** 2)

    behind = float(np.mean(env[dg.BEAM_BEHIND] ** 2) / np.mean(env_e[dg.BEAM_BEHIND] ** 2))

    wa = sc.widths(cap, cap_e, dg.BEAM_BOX_A, dg.BEAM_REF)
    wb = sc.widths(cap, cap_e, dg.BEAM_BOX_B, dg.BEAM_REF)
    box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])

    return {"lambda_nm": lam_nm, "cpl": cpl, "steps": dg.BEAM_STEPS_EXTENDED,
           "beam_behind": behind, "beam_behind_3200_established": EXP026_BEAM_BEHIND_3200[lam_nm],
           "delta_vs_3200": behind - EXP026_BEAM_BEHIND_3200[lam_nm],
           "box_dev": box_dev, "elapsed_s": time.time() - t0}


# --------------------------------------------------------------- Block 2
def block2_one(lam_nm):
    g = dg.BLOCK2_GEOM[lam_nm]
    t0 = time.time()
    sim_e, cap_e, capqp_e = run_beam_scene(
        "empty", g["cpl"], g["n"], g["cx"], g["cy"], g["r_out"],
        g["src_x"], g["absorb"], dg.BEAM_STEPS_NATIVE)
    env_e = np.sqrt(cap_e["ez_a"] ** 2 + cap_e["ez_b"] ** 2)

    sim, cap, capqp = run_beam_scene(
        "on", g["cpl"], g["n"], g["cx"], g["cy"], g["r_out"],
        g["src_x"], g["absorb"], dg.BEAM_STEPS_NATIVE)
    env = np.sqrt(cap["ez_a"] ** 2 + cap["ez_b"] ** 2)

    x0, x1, y0, y1 = g["behind"]
    behind_sl = (slice(x0, x1), slice(y0, y1))
    behind = float(np.mean(env[behind_sl] ** 2) / np.mean(env_e[behind_sl] ** 2))

    ref = (g["cx"], g["cy"], int(round(60 * g["ratio"])))
    wa = sc.widths(cap, cap_e, g["box_a"], ref)
    wb = sc.widths(cap, cap_e, g["box_b"], ref)
    box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])

    return {"lambda_nm": lam_nm, "cpl": g["cpl"], "steps": dg.BEAM_STEPS_NATIVE,
           "beam_behind": behind, "box_dev": box_dev, "elapsed_s": time.time() - t0}


# --------------------------------------------------------------- Block 3
def build_cell(cell, sim):
    cx, cy = dg.BEAM_CX, dg.BEAM_CY
    if cell == "empty":
        return
    if cell == "A":
        mat.pec_disk(sim, cx, cy, dg.BLOCK3_R_CORE)
        mat.graded_black_shell(sim, cx, cy, dg.BLOCK3_R_CORE, dg.BLOCK3_R_OUT,
                               sigma_max=dg.BLOCK3_SHELL_SIGMA_MAX,
                               eps_max=dg.BLOCK3_SHELL_EPS_MAX)
    elif cell == "B":
        mat.graded_black_shell(sim, cx, cy, dg.BLOCK3_R_CORE, dg.BLOCK3_R_OUT,
                               sigma_max=dg.BLOCK3_SHELL_SIGMA_MAX,
                               eps_max=dg.BLOCK3_SHELL_EPS_MAX)
        x = np.arange(sim.nx)[:, None]
        y = np.arange(sim.ny)[None, :]
        rr = np.hypot(x - cx, y - cy)
        # fix 1 (Red Team attack #1 / MATERIALS' verified catch): STRICT '<',
        # not '<=' -- the shell's own mask is (rr>=r_in)&(rr<=r_out), already
        # inclusive at r_in=30, so '<=' here would double-write sigma at the
        # 12 lattice points sitting exactly on r=30.
        sim.sigma_e[rr < dg.BLOCK3_R_CORE] += dg.BLOCK3_SHELL_SIGMA_MAX
    elif cell == "C":
        x = np.arange(sim.nx)[:, None]
        y = np.arange(sim.ny)[None, :]
        rr = np.hypot(x - cx, y - cy)
        sim.sigma_e[rr <= dg.BLOCK3_R_OUT] += dg.BLOCK3_ON_SIGMA
    else:
        raise ValueError(cell)
    sim.objects.append({"type": f"exp027_block3_cell_{cell}"})


def run_block3_scene(cell, cpl=20, steps=dg.BEAM_STEPS_NATIVE):
    sim = Sim(dg.BEAM_N, dg.BEAM_N, cells_per_lambda=cpl,
             courant_frac=dg.BEAM_FRAC, absorb=dg.BEAM_ABSORB)
    build_cell(cell, sim)
    sim.add_line_source(dg.BEAM_SRC_X)
    sim.run(steps)
    return sim, sc.full_capture(sim)


def block3():
    t0 = time.time()
    sim_e, cap_e = run_block3_scene("empty")
    results = {}
    for cell in ("A", "B", "C"):
        sim, cap = run_block3_scene(cell)
        wa = sc.widths(cap, cap_e, dg.BEAM_BOX_A, dg.BEAM_REF)
        wb = sc.widths(cap, cap_e, dg.BEAM_BOX_B, dg.BEAM_REF)
        box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])
        w_self = sc.widths(cap_e, cap_e, dg.BEAM_BOX_A, dg.BEAM_REF)
        empty_box_closure = abs(w_self["sigma_ext"]) / abs(wa["sigma_ext"])

        centers, pattern = sc.angular_scattered_pattern(cap, cap_e, dg.BEAM_BOX_A, dg.BEAM_REF)
        # implementation self-consistency check (sections.py docstring): sum
        # of the per-bin pattern must equal widths()'s own sigma_scat
        pattern_sum_check = float(np.sum(pattern)) - wa["sigma_scat"]
        # wide-angle / side-lobe fraction: |angle| outside +-60deg of pure
        # forward(+-180)/backward(0) -- i.e. the "side" quadrant of the
        # square-path sample, informational (P-EM6, no numeric gate)
        side_mask = (np.abs(np.abs(centers) - 90.0) < 30.0)
        side_frac = float(np.sum(pattern[side_mask]) / wa["sigma_scat"]) if wa["sigma_scat"] else float("nan")

        # fix 6 (Thermo's mandatory sidecar, informational, zero extra runs):
        # raw absorbed power / incident intensity per cell.
        p_abs_raw = wa["sigma_abs"] * wa["i_inc"]

        obs_ang, obs_flux, obs_aux = em.observer_record(
            sim, (cap["ez_a"], cap["hy_a"], cap["ez_b"], cap["hy_b"], cap["off"]),
            dg.BEAM_OBS_X)
        _, _, ref_aux = em.observer_record(
            sim_e, (cap_e["ez_a"], cap_e["hy_a"], cap_e["ez_b"], cap_e["hy_b"], cap_e["off"]),
            dg.BEAM_OBS_X)
        observer_return = obs_aux["p_backward_total"] / ref_aux["p_forward_total"]

        results[cell] = {
            "sigma_scat": wa["sigma_scat"], "sigma_abs": wa["sigma_abs"],
            "sigma_ext": wa["sigma_ext"], "sigma_ext_cross": wa["sigma_ext_cross"],
            "abs_ext_ratio": wa["sigma_abs"] / wa["sigma_ext"],
            "i_inc": wa["i_inc"], "p_abs_raw": p_abs_raw,
            "back_frac": wa["back_frac"], "box_dev": box_dev,
            "empty_box_closure": empty_box_closure,
            "side_lobe_frac": side_frac, "pattern_self_consistency": pattern_sum_check,
            "observer_return": observer_return,
        }
    return results, time.time() - t0


def main():
    print("exp-027: Block 1 (settling, 3 lambda x 6400 steps)", flush=True)
    t0 = time.time()
    block1 = {}
    for cpl, nm in dg.BLOCK1_SWEEP:
        r = block1_one(nm, cpl)
        block1[nm] = r
        print(f"  {nm}nm: beam_behind@6400={r['beam_behind']:.4f} "
              f"(@3200 established={r['beam_behind_3200_established']:.4f}, "
              f"delta={r['delta_vs_3200']:+.4f}) box_dev={r['box_dev']:.4f} "
              f"({r['elapsed_s']:.1f}s)", flush=True)
    elapsed_block1 = time.time() - t0

    print("\nexp-027: Block 2 (R3 spatial companion, cpl x1.5, 3 lambda)", flush=True)
    t1 = time.time()
    block2 = {}
    for lam_nm in dg.BLOCK2_GEOM:
        r = block2_one(lam_nm)
        block2[lam_nm] = r
        print(f"  {lam_nm}nm (cpl={r['cpl']}): beam_behind={r['beam_behind']:.4f} "
              f"box_dev={r['box_dev']:.4f} ({r['elapsed_s']:.1f}s)", flush=True)
    elapsed_block2 = time.time() - t1

    print("\nexp-027: Block 3 (PEC-ablation factorial, lambda=600nm)", flush=True)
    t2 = time.time()
    block3_results, elapsed_block3 = block3()
    for cell, r in block3_results.items():
        print(f"  cell {cell}: abs/ext={r['abs_ext_ratio']:.4f} "
              f"p_abs_raw={r['p_abs_raw']:.4f} box_dev={r['box_dev']:.4f} "
              f"empty_closure={r['empty_box_closure']:.2e} "
              f"side_lobe_frac={r['side_lobe_frac']:.4f} "
              f"pattern_check={r['pattern_self_consistency']:.2e} "
              f"observer_return={r['observer_return']:.6f}", flush=True)

    spread_450, spread_600, spread_750 = (block1[450]["beam_behind"],
                                          block1[600]["beam_behind"],
                                          block1[750]["beam_behind"])
    b1_vals = [spread_450, spread_600, spread_750]
    b1_spread_rel = (max(b1_vals) - min(b1_vals)) / (sum(b1_vals) / 3.0)

    b2_vals = [block2[450]["beam_behind"], block2[600]["beam_behind"], block2[750]["beam_behind"]]
    b2_spread_rel = (max(b2_vals) - min(b2_vals)) / (sum(b2_vals) / 3.0)

    out = {
        "meta": {
            "geometry_beam_native": {k: getattr(dg, k) for k in
                                     ("BEAM_N", "BEAM_CX", "BEAM_CY", "BEAM_SRC_X",
                                      "BEAM_OBS_X", "R_OUT", "BEAM_BOX_A", "BEAM_BOX_B")},
            "block2_geom": dg.BLOCK2_GEOM,
            "established_beam_behind_3200": dg.ESTABLISHED_BEAM_BEHIND_3200,
            "established_abs_ext": dg.ESTABLISHED_ABS_EXT,
            "t7_ambient_chromatic_delta": dg.T7_AMBIENT_CHROMATIC_DELTA,
            "elapsed_s_block1": elapsed_block1, "elapsed_s_block2": elapsed_block2,
            "elapsed_s_block3": elapsed_block3,
            "n_new_runs": 6 + 6 + 4,
        },
        "block1_settling": block1,
        "block1_relative_spread_6400": b1_spread_rel,
        "block2_spatial": block2,
        "block2_relative_spread": b2_spread_rel,
        "block3_pec_ablation": block3_results,
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1)

    print(f"\nBlock 1 relative spread @6400: {b1_spread_rel:.4f} "
          f"(established @3200: {(max(EXP026_BEAM_BEHIND_3200.values()) - min(EXP026_BEAM_BEHIND_3200.values())) / (sum(EXP026_BEAM_BEHIND_3200.values()) / 3.0):.4f})")
    print(f"Block 2 relative spread: {b2_spread_rel:.4f}")
    print("\nresults.json written")


if __name__ == "__main__":
    main()
