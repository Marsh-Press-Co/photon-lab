"""
exp-023 -- Does exp-022's r2=75 Box-Independence Gate Miss Survive
Resolution?: the runs.
============================================================================
exp-022 found 4 of 7 r2=75/floor=0.10 points miss the box_dev <=2% gate
(2.55%-3.36%), while every r2=120 point and every r2=75/floor=0.18 point
cleared it comfortably. This line's exp-004->005, exp-009->010 and
exp-014->015 precedent: don't discard or argue about a gate miss,
re-run at 1.5x resolution (cpl 20->30) with geometry scaled to hold
physical size fixed, and let refinement settle it.

Three of exp-022's r2=75 core points, not the full 7-point bracket:
r1=13 (worst gate miss, 3.36%), r1=15 (the shell=3lambda target itself,
2.55%), r1=18 (a clean flank, 1.89%, included as a control -- does
refinement leave an already-clean point clean, or was exp-022's own 2%
line drawn too finely to mean much at cpl=20?). Same minimal-but-decisive
three-point design as exp-015.

Predictions were committed before this file first ran (see NOTES.md).

    .venv/bin/python experiments/023-r2-75-resolution/run.py
"""

import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from lab import Sim, materials
from lab import sections as sc

HERE = os.path.dirname(os.path.abspath(__file__))

# --- exp-022's r2=75 geometry (cpl=20), scaled by 1.5x to cpl=30 ---
CPL_BASE, CPL_NEW = 20, 30
SCALE = CPL_NEW / CPL_BASE                          # 1.5

N = int(round(680 * SCALE))
CX = CY = int(round(300 * SCALE))
ABSORB = int(round(40 * SCALE))
STEPS = int(round(3600 * SCALE))
FRAC = 0.32                                          # unchanged: eps_z-based ceiling is f-invariant
SRC_X = int(round(64 * SCALE))
REF_HALF_H = int(round(60 * SCALE))
MIN_MARGIN = int(round(60 * SCALE))
R2_CELLS = int(round(75 * SCALE))                    # 112 (75 is not a multiple of 2 -- small
                                                       # sub-cell rounding, same as exp-015's r1=33)
BOX_A_HALF = int(round((75 + 20) * SCALE))            # matches exp-022's r2+20 convention
BOX_B_HALF = int(round((75 + 45) * SCALE))            # matches exp-022's r2+45 convention

CORE_BASE = [13, 15, 18]                              # worst gate miss / target / clean flank
FLOOR_SWEEP = [0.10, 0.18]

# exp-022's cpl=20 numbers at r2=75, for direct comparison in this file's output
CPL20 = {
    13: {0.10: 0.08385, 0.18: 0.19447, "jump": +131.87, "box_dev": (0.0336, 0.0178)},
    15: {0.10: 0.12025, 0.18: 0.32887, "jump": +173.46, "box_dev": (0.0255, 0.0115)},
    18: {0.10: 0.21472, 0.18: 0.53517, "jump": +149.30, "box_dev": (0.0189, 0.0010)},
}


def scaled_cores():
    return {base: int(round(base * SCALE)) for base in CORE_BASE}


def check_gates(cores):
    print(f"CFL + degeneracy check (courant_frac={FRAC}, r2={R2_CELLS}):", flush=True)
    for base, r1 in cores.items():
        eps_z = (R2_CELLS / (R2_CELLS - r1)) ** 2
        thresh = ((R2_CELLS - r1) / R2_CELLS) ** 2
        eps_z_base = (75 / (75 - base)) ** 2
        print(f"  base={base} -> r1={r1}: eps_z={eps_z:.4f} (cpl20 was {eps_z_base:.4f})  "
              f"degeneracy_threshold={thresh:.4f}", flush=True)
        for floor in FLOOR_SWEEP:
            cmax = math.sqrt(floor * eps_z)
            assert FRAC < cmax, f"base={base}, floor={floor} unstable (ceiling={cmax:.4f})"
            assert floor < thresh, f"base={base}, floor={floor} at/above degeneracy {thresh:.4f}"


def box_coords():
    for half, name in ((BOX_A_HALF, "box_a"), (BOX_B_HALF, "box_b")):
        margin_x = min(CX - half, N - ABSORB - (CX + half)) - ABSORB
        margin_y = min(CY - half, N - ABSORB - (CY + half)) - ABSORB
        assert margin_x >= MIN_MARGIN and margin_y >= MIN_MARGIN, \
            f"{name} clearance too tight (margin={min(margin_x, margin_y)})"
        assert half > R2_CELLS, f"{name} does not clear the cloak"
    return (CX - BOX_A_HALF, CX + BOX_A_HALF, CY - BOX_A_HALF, CY + BOX_A_HALF), \
           (CX - BOX_B_HALF, CX + BOX_B_HALF, CY - BOX_B_HALF, CY + BOX_B_HALF)


def run_scene(build):
    sim = Sim(N, N, cells_per_lambda=CPL_NEW, courant_frac=FRAC, absorb=ABSORB)
    if build is not None:
        build(sim)
    sim.add_line_source(SRC_X)
    sim.run(STEPS)
    return sc.full_capture(sim)


def main():
    t0 = time.time()
    results = {}

    cores = scaled_cores()
    check_gates(cores)
    print(f"r2 (fixed) = {R2_CELLS} cells (base 75), lambda=600nm, cpl={CPL_NEW}", flush=True)

    box_a, box_b = box_coords()
    cap_e = run_scene(None)

    for base in CORE_BASE:
        r1 = cores[base]
        eps_z = (R2_CELLS / (R2_CELLS - r1)) ** 2
        qs = {}
        bds = {}
        for floor in FLOOR_SWEEP:
            def build(sim, r1=r1, floor=floor):
                materials.pec_disk(sim, CX, CY, r1)
                materials.schurig_reduced_cloak_tm(sim, CX, CY, r1, R2_CELLS,
                                                   mu_r_floor=floor)
            cap = run_scene(build)
            wa = sc.widths(cap, cap_e, box_a, (CX, CY, REF_HALF_H))
            wb = sc.widths(cap, cap_e, box_b, (CX, CY, REF_HALF_H))
            box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])
            cross_dev = abs(wa["sigma_ext"] - wa["sigma_ext_cross"]) / abs(wa["sigma_ext"])
            out = {k: wa[k] for k in ("sigma_scat", "sigma_abs", "sigma_ext",
                                       "sigma_ext_cross", "back_frac", "fwd_frac", "i_inc")}
            out["q_ext"] = wa["sigma_ext"] / (2.0 * R2_CELLS)
            out["box_dev"] = box_dev
            out["cross_dev"] = cross_dev
            out["core_r1_cells"] = r1
            out["core_base_cpl20"] = base
            out["eps_z"] = eps_z
            out["mu_r_floor"] = floor
            results[f"cloak-base{base}-r1_{r1}-floor{floor}"] = out
            qs[floor] = out["q_ext"]
            bds[floor] = box_dev
            print(f"  base={base} (r1={r1}) floor={floor:.2f}: Q_ext={out['q_ext']:.4f}  "
                  f"boxdev={box_dev:.4f}  crossdev={cross_dev:.4f}", flush=True)
        jump = (qs[0.18] - qs[0.10]) / qs[0.10] * 100
        ref = CPL20[base]
        print(f"  base={base}: jump={jump:+.2f}%  (cpl20 was {ref['jump']:+.2f}%)  "
              f"boxdev(0.10/0.18)={bds[0.10]:.4f}/{bds[0.18]:.4f}  "
              f"(cpl20 was {ref['box_dev'][0]:.4f}/{ref['box_dev'][1]:.4f})", flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print(f"exp-023 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
