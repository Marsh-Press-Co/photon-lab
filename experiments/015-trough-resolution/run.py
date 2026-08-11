"""
exp-015 -- Does the eps_z Trough Survive Resolution?: the runs.
=================================================================
exp-014 found the exp-004/005/006 baseline's negative floor-jump
(core=30, eps_z=2.25) sits inside a real, contiguous 4-point trough in
eps_z (roughly 2.18-2.41) rather than being an isolated grid point -- but
that whole scan stepped r1 by exactly 1 cell at cpl=20, the finest
geometric step tested anywhere in this line, so a grid-quantization
origin (the clamp boundary's position relative to the fixed Cartesian
grid) hasn't been ruled out the way it was for the *floor* sweep
(exp-004->exp-005). This is that check: exp-004->exp-005 and
exp-009->exp-010's exact precedent -- same physical geometry, cpl raised
20->30 (1.5x), geometry scaled in cells to hold physical size fixed.

Three core points, not the full 6-point bracket: r1=28 (positive jump at
cpl=20, just outside the trough), r1=30 (deepest point in the trough,
reused baseline), r1=33 (positive jump at cpl=20, just outside on the
other side) -- enough to test whether the trough's *existence* (still
negative at center, still positive at both flanks) survives refinement,
the same minimal-but-decisive design exp-005 used (one core value, full
floor sweep) rather than re-running the whole 6-point map at 1.5x cost.

Predictions were committed before this file first ran (see NOTES.md).

    .venv\\Scripts\\python.exe experiments\\015-trough-resolution\\run.py
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

# --- exp-014 baseline (cpl=20) geometry, scaled by 1.5x to cpl=30 ---
CPL_BASE, CPL_NEW = 20, 30
SCALE = CPL_NEW / CPL_BASE                          # 1.5

N = int(round(680 * SCALE))                         # 1020
CX = CY = int(round(300 * SCALE))                   # 450
ABSORB = int(round(40 * SCALE))                      # 60
STEPS = int(round(3600 * SCALE))                     # 5400
FRAC = 0.32                                          # unchanged: eps_z-based ceiling is f-invariant
SRC_X = int(round(64 * SCALE))
REF_HALF_H = int(round(60 * SCALE))
MIN_MARGIN = int(round(60 * SCALE))
BOX_A_HALF = int(round(110 * SCALE))
BOX_B_HALF = int(round(135 * SCALE))
R2_CELLS = int(round(90 * SCALE))                    # 135

CORE_BASE = [28, 30, 33]                             # exp-014's cpl=20 core radii (flank/center/flank)
FLOOR_SWEEP = [0.10, 0.18]

# exp-014's cpl=20 numbers (r1=30 from exp-004/006), for direct comparison in this file's output
CPL20 = {
    28: {0.10: 0.5874, 0.18: 0.6227, "jump": +6.01},
    30: {0.10: 0.6620, 0.18: 0.5449, "jump": -17.69},
    33: {0.10: 0.6759, 0.18: 0.7585, "jump": +12.22},
}


def scaled_cores():
    return {base: int(round(base * SCALE)) for base in CORE_BASE}


def check_gates(cores):
    print(f"CFL + degeneracy check (courant_frac={FRAC}, r2={R2_CELLS}):", flush=True)
    for base, r1 in cores.items():
        eps_z = (R2_CELLS / (R2_CELLS - r1)) ** 2
        thresh = ((R2_CELLS - r1) / R2_CELLS) ** 2
        print(f"  base={base} -> r1={r1}: eps_z={eps_z:.4f} (cpl20 was "
              f"{(90 / (90 - base)) ** 2:.4f})  degeneracy_threshold={thresh:.4f}", flush=True)
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
    print(f"r2 (fixed) = {R2_CELLS} cells, lambda=600nm, cpl={CPL_NEW}", flush=True)

    box_a, box_b = box_coords()
    cap_e = run_scene(None)

    for base in CORE_BASE:
        r1 = cores[base]
        eps_z = (R2_CELLS / (R2_CELLS - r1)) ** 2
        qs = {}
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
            print(f"  base={base} (r1={r1}) floor={floor:.2f}: Q_ext={out['q_ext']:.4f}  "
                  f"boxdev={box_dev:.3f}  crossdev={cross_dev:.3f}", flush=True)
        jump = (qs[0.18] - qs[0.10]) / qs[0.10] * 100
        ref = CPL20[base]
        print(f"  base={base}: jump={jump:+.2f}%  (cpl20 was {ref['jump']:+.2f}%)", flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print(f"exp-015 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
