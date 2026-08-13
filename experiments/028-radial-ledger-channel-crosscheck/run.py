"""exp-028 -- The Radial Ledger and the Channel Cross-Check: measurement harness.
=================================================================================
Panel Iteration 5 (lead THERMODYNAMICS; synthesis: Director, post Red Team's
proceed-with-mandatory-fixes -- see design_geometry.py's module docstring
and NOTES.md Phase 3 for the full accepted/overridden record).

Two blocks, all on the already-validated exp-001/002/026/027 beam-scene
bench, one new `lab/` function (`sections.radial_absorbed_power`, gated by
suite stage 10 before this file's first trusted run):

  Block A -- T10 box-ledger-vs-envelope-ratio cross-check, SIGMA FIXED to
             hold tau_center=3.9 at every lambda (Red Team's load-bearing
             catch). 3 x (empty+on) = 6 new sim calls.
  Block B -- radial-binned absorbed-power ledger (T9 spatial follow-up),
             native geometry, 4 cells (empty/A/B/C), PLUS a cpl x1.5
             resolution companion on Cell B (EM's mandatory fix). 4 + 2 = 6
             new sim calls.

Total NEW FDTD sim calls: 6 + 6 = 12.

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


# --------------------------------------------------------------- Block A
def build_beam_on(sim, cx, cy, r_out, sigma_on):
    x = np.arange(sim.nx)[:, None]
    y = np.arange(sim.ny)[None, :]
    mask = (x - cx) ** 2 + (y - cy) ** 2 <= r_out ** 2
    sim.sigma_e[mask] += sigma_on


def run_beam_scene(article, cpl, n, cx, cy, r_out, src_x, absorb, steps,
                   sigma_on=None, frac=dg.BEAM_FRAC):
    sim = Sim(n, n, cells_per_lambda=cpl, courant_frac=frac, absorb=absorb)
    if article == "on":
        build_beam_on(sim, cx, cy, r_out, sigma_on)
    sim.add_line_source(src_x)
    sim.run(steps)
    return sim, sc.full_capture(sim)


def blockA_one(lam_nm):
    g = dg.BLOCKA_GEOM[lam_nm]
    t0 = time.time()
    sim_e, cap_e = run_beam_scene(
        "empty", g["cpl"], g["n"], g["cx"], g["cy"], g["r_out"],
        g["src_x"], g["absorb"], dg.BEAM_STEPS_NATIVE)
    env_e = np.sqrt(cap_e["ez_a"] ** 2 + cap_e["ez_b"] ** 2)

    sim, cap = run_beam_scene(
        "on", g["cpl"], g["n"], g["cx"], g["cy"], g["r_out"],
        g["src_x"], g["absorb"], dg.BEAM_STEPS_NATIVE, sigma_on=g["sigma_on"])
    env = np.sqrt(cap["ez_a"] ** 2 + cap["ez_b"] ** 2)

    x0, x1, y0, y1 = g["behind"]
    behind_sl = (slice(x0, x1), slice(y0, y1))
    behind = float(np.mean(env[behind_sl] ** 2) / np.mean(env_e[behind_sl] ** 2))

    wa = sc.widths(cap, cap_e, g["box_a"], g["ref"])
    wb = sc.widths(cap, cap_e, g["box_b"], g["ref"])
    box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])
    tau_check = 2.0 * g["sigma_on"] * g["r_out"]

    return {"lambda_nm": lam_nm, "cpl": g["cpl"], "tau_center_check": tau_check,
           "beam_behind": behind, "sigma_ext": wa["sigma_ext"], "box_dev": box_dev,
           "elapsed_s": time.time() - t0}


# --------------------------------------------------------------- Block B
def build_cell(cell, sim, cx, cy, r_core, r_out):
    if cell == "empty":
        return
    if cell == "A":
        mat.pec_disk(sim, cx, cy, r_core)
        mat.graded_black_shell(sim, cx, cy, r_core, r_out,
                               sigma_max=dg.BLOCKB_SHELL_SIGMA_MAX,
                               eps_max=dg.BLOCKB_SHELL_EPS_MAX)
    elif cell == "B":
        mat.graded_black_shell(sim, cx, cy, r_core, r_out,
                               sigma_max=dg.BLOCKB_SHELL_SIGMA_MAX,
                               eps_max=dg.BLOCKB_SHELL_EPS_MAX)
        x = np.arange(sim.nx)[:, None]
        y = np.arange(sim.ny)[None, :]
        rr = np.hypot(x - cx, y - cy)
        sim.sigma_e[rr < r_core] += dg.BLOCKB_SHELL_SIGMA_MAX   # strict '<', exp-027's fix
    elif cell == "C":
        x = np.arange(sim.nx)[:, None]
        y = np.arange(sim.ny)[None, :]
        rr = np.hypot(x - cx, y - cy)
        sim.sigma_e[rr <= r_out] += dg.TAU_ON / (2.0 * r_out)
    else:
        raise ValueError(cell)
    sim.objects.append({"type": f"exp028_block_b_cell_{cell}"})


def run_cell(cell, n, cx, cy, r_core, r_out, cpl, absorb, src_x, steps):
    sim = Sim(n, n, cells_per_lambda=cpl, courant_frac=dg.BEAM_FRAC, absorb=absorb)
    build_cell(cell, sim, cx, cy, r_core, r_out)
    sim.add_line_source(src_x)
    sim.run(steps)
    return sim, sc.full_capture(sim)


def score_cell(cell, sim, cap, cap_e, box_a, box_b, ref, cx, cy, r_core, r_out):
    wa = sc.widths(cap, cap_e, box_a, ref)
    wb = sc.widths(cap, cap_e, box_b, ref)
    box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])
    p_abs_box = wa["sigma_abs"] * wa["i_inc"]

    centers, bins, total = sc.radial_absorbed_power(
        cap, sim.sigma_e, cx, cy, r_out, n_bins=dg.BLOCKB_N_BINS)
    _, _, core_total = sc.radial_absorbed_power(cap, sim.sigma_e, cx, cy, r_core)
    closure = abs(total - p_abs_box) / abs(p_abs_box) if p_abs_box else float("nan")
    core_frac = core_total / total if total else float("nan")
    peak_bin = float(centers[int(np.argmax(bins))])

    return {"abs_ext_ratio": wa["sigma_abs"] / wa["sigma_ext"], "box_dev": box_dev,
           "p_abs_box": p_abs_box, "radial_total": total, "closure": closure,
           "core_power": core_total, "core_frac": core_frac, "peak_bin_r": peak_bin,
           "bins": bins.tolist(), "bin_centers": centers.tolist()}


def block_b():
    t0 = time.time()
    cx, cy = dg.BEAM_CX, dg.BEAM_CY
    n, r_core, r_out = dg.BEAM_N, dg.BLOCKB_R_CORE, dg.BLOCKB_R_OUT

    sim_e, cap_e = run_cell("empty", n, cx, cy, r_core, r_out, 20,
                            dg.BEAM_ABSORB, dg.BEAM_SRC_X, dg.BEAM_STEPS_NATIVE)
    native = {}
    for cell in ("A", "B", "C"):
        sim, cap = run_cell(cell, n, cx, cy, r_core, r_out, 20,
                            dg.BEAM_ABSORB, dg.BEAM_SRC_X, dg.BEAM_STEPS_NATIVE)
        native[cell] = score_cell(cell, sim, cap, cap_e, dg.BEAM_BOX_A, dg.BEAM_BOX_B,
                                  dg.BEAM_REF, cx, cy, r_core, r_out)
    elapsed_native = time.time() - t0

    # companion (fix 3): cpl x1.5 on Cell B only, exp-027's own BLOCK2_GEOM[600] geometry
    t1 = time.time()
    g = dg.BLOCKB_COMPANION_GEOM
    sim_ec, cap_ec = run_cell("empty", g["n"], g["cx"], g["cy"],
                              dg.BLOCKB_COMPANION_R_CORE, g["r_out"], g["cpl"],
                              g["absorb"], g["src_x"], dg.BEAM_STEPS_NATIVE)
    sim_bc, cap_bc = run_cell("B", g["n"], g["cx"], g["cy"],
                              dg.BLOCKB_COMPANION_R_CORE, g["r_out"], g["cpl"],
                              g["absorb"], g["src_x"], dg.BEAM_STEPS_NATIVE)
    companion = score_cell("B", sim_bc, cap_bc, cap_ec, g["box_a"], g["box_b"], g["ref"],
                           g["cx"], g["cy"], dg.BLOCKB_COMPANION_R_CORE, g["r_out"])
    elapsed_companion = time.time() - t1

    return native, companion, elapsed_native, elapsed_companion


def main():
    print("exp-028: Block A (T10 box-ledger cross-check, SIGMA fixed per lambda)", flush=True)
    t0 = time.time()
    block_a = {}
    for lam_nm in dg.BLOCKA_GEOM:
        r = blockA_one(lam_nm)
        block_a[lam_nm] = r
        print(f"  {lam_nm}nm (cpl={r['cpl']}): tau_check={r['tau_center_check']:.4f} "
              f"beam_behind={r['beam_behind']:.5f} sigma_ext={r['sigma_ext']:.4f} "
              f"box_dev={r['box_dev']:.4f} ({r['elapsed_s']:.1f}s)", flush=True)
    elapsed_a = time.time() - t0

    sext_vals = [block_a[lam]["sigma_ext"] for lam in (450, 600, 750)]
    sext_spread_rel = (max(sext_vals) - min(sext_vals)) / (sum(sext_vals) / 3.0)

    print("\nexp-028: Block B (radial-binned absorbed-power ledger)", flush=True)
    t1 = time.time()
    native, companion, elapsed_native, elapsed_companion = block_b()
    for cell, r in native.items():
        print(f"  cell {cell} (native, cpl=20): abs/ext={r['abs_ext_ratio']:.4f} "
              f"closure={r['closure']:.4f} core_power={r['core_power']:.4e} "
              f"core_frac={r['core_frac']*100:.4f}% peak_bin_r={r['peak_bin_r']:.1f} "
              f"box_dev={r['box_dev']:.4f}", flush=True)
    print(f"  cell B (companion, cpl=30): closure={companion['closure']:.4f} "
          f"core_frac={companion['core_frac']*100:.4f}% peak_bin_r={companion['peak_bin_r']:.1f} "
          f"box_dev={companion['box_dev']:.4f}", flush=True)
    elapsed_b = time.time() - t1

    out = {
        "meta": {
            # QUANTUM rider (fix 7, honest framing per Red Team's Phase-2 correction):
            # field names established for a future shared-intensity-axis bridge gate,
            # NOT yet exercised on a non-trivial value -- every run in this experiment
            # is a single-source beam capture at amplitude 1.0, so amp_rel=1.0 is true
            # by construction, not a validated instrument step.
            "intensity_ledger": {"intensity_role": "beam", "amp_rel": 1.0,
                                 "convention_note": "field names established, not yet "
                                 "exercised on a non-trivial value (Panel Iteration 5)"},
            "block_a_geom": dg.BLOCKA_GEOM,
            "block_b_native": {"n": dg.BEAM_N, "cx": dg.BEAM_CX, "cy": dg.BEAM_CY,
                               "r_core": dg.BLOCKB_R_CORE, "r_out": dg.BLOCKB_R_OUT, "cpl": 20},
            "block_b_companion_geom": dg.BLOCKB_COMPANION_GEOM,
            "block_b_companion_r_core": dg.BLOCKB_COMPANION_R_CORE,
            "established_beam_behind_3200": dg.ESTABLISHED_BEAM_BEHIND_3200,
            "established_block2_beam_behind_buggy_labeled_only": dg.ESTABLISHED_BLOCK2_BEAM_BEHIND_BUGGY,
            "established_abs_ext": dg.ESTABLISHED_ABS_EXT,
            "elapsed_s_block_a": elapsed_a, "elapsed_s_block_b_native": elapsed_native,
            "elapsed_s_block_b_companion": elapsed_companion,
            "n_new_runs": 6 + 6,
        },
        "block_a": block_a,
        "block_a_sigma_ext_relative_spread": sext_spread_rel,
        "block_b_native": native,
        "block_b_companion": companion,
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1)

    print(f"\nBlock A sigma_ext relative spread: {sext_spread_rel:.4f}")
    print(f"Block B native Cell B core_frac: {native['B']['core_frac']*100:.4f}%  "
          f"(companion cpl x1.5: {companion['core_frac']*100:.4f}%)  "
          f"-- printed as a PERCENT directly (Red Team's Phase-5 fix), not a re-labeled "
          f"pre-rounded fraction (exp-028's own first-run bug: 6.199e-05 displayed as "
          f"'0.0001 (0.01%)' instead of the correct 0.0062%).")
    print("\nresults.json written")


if __name__ == "__main__":
    main()
