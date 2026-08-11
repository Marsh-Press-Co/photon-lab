"""
exp-010 -- Does the Below-Eight Bump Survive Resolution?: the runs.
============================================================
Resolution-convergence check on exp-009's two anomalies: the box_dev
gate failing at core=4/5 cells (cpl=20), and the non-monotonic bump in
cloaked Q_ext across core=4-7. Reruns the same 4 physical core sizes at
cpl=30 (1.5x), geometry scaled in cells to hold physical size fixed --
exp-004->exp-005's exact precedent.

Predictions were committed before this file first ran (see NOTES.md).

    .venv\\Scripts\\python.exe experiments\\010-ratio-resolution\\run.py
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

# --- exp-009 baseline (cpl=20) geometry, scaled by 1.5x to cpl=30 ---
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

CORE_BASE = [4, 5, 6, 7]                             # exp-009's cpl=20 core radii
FLOOR = 0.10

# exp-009's cpl=20 numbers, for direct comparison in this file's output
CPL20 = {
    4: {"bare": 0.1242, "cloak": 0.0351, "ratio": 0.2825, "box_dev_cloak": 0.035},
    5: {"bare": 0.1541, "cloak": 0.0424, "ratio": 0.2753, "box_dev_cloak": 0.023},
    6: {"bare": 0.1763, "cloak": 0.0413, "ratio": 0.2345, "box_dev_cloak": 0.020},
    7: {"bare": 0.1970, "cloak": 0.0365, "ratio": 0.1852, "box_dev_cloak": 0.018},
}


def scaled_cores():
    return {base: int(round(base * SCALE)) for base in CORE_BASE}


def check_cfl(cores):
    print(f"CFL margin check (floor={FLOOR}, courant_frac={FRAC}, r2={R2_CELLS}):", flush=True)
    for base, r1 in cores.items():
        eps_z = (R2_CELLS / (R2_CELLS - r1)) ** 2
        cmax = math.sqrt(FLOOR * eps_z)
        margin = cmax / FRAC - 1.0
        print(f"  base={base} -> r1={r1}: eps_z={eps_z:.4f}  cfl_ceiling={cmax:.4f}  "
              f"margin={margin * 100:.2f}%  {'OK' if FRAC < cmax else 'UNSTABLE!'}", flush=True)
        assert FRAC < cmax, f"r1={r1} unstable at courant_frac={FRAC} (ceiling={cmax:.4f})"


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


def measure(cap, cap_e, box_a, box_b, r1, extra):
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
    out.update(extra)
    return out


def main():
    t0 = time.time()
    results = {}

    cores = scaled_cores()
    check_cfl(cores)
    print(f"r2 (fixed) = {R2_CELLS} cells, lambda=600nm, cpl={CPL_NEW}, floor={FLOOR}", flush=True)
    print(f"core cells (cpl=30) for base 4/5/6/7: {cores}", flush=True)

    box_a, box_b = box_coords()
    cap_e = run_scene(None)

    for base in CORE_BASE:
        r1 = cores[base]
        eps_z = (R2_CELLS / (R2_CELLS - r1)) ** 2

        def build_bare(sim, r1=r1):
            materials.pec_disk(sim, CX, CY, r1)
        cap_bare = run_scene(build_bare)
        out_bare = measure(cap_bare, cap_e, box_a, box_b, r1, {"core_base_cpl20": base})
        results[f"bare-base{base}-r1_{r1}"] = out_bare

        def build_cloak(sim, r1=r1):
            materials.pec_disk(sim, CX, CY, r1)
            materials.schurig_reduced_cloak_tm(sim, CX, CY, r1, R2_CELLS,
                                               mu_r_floor=FLOOR)
        cap_cloak = run_scene(build_cloak)
        out_cloak = measure(cap_cloak, cap_e, box_a, box_b, r1,
                             {"eps_z": eps_z, "mu_r_floor": FLOOR, "core_base_cpl20": base})
        results[f"cloak-base{base}-r1_{r1}-floor{FLOOR}"] = out_cloak

        ratio = out_cloak["q_ext"] / out_bare["q_ext"]
        out_cloak["ratio_cloaked_over_bare"] = ratio
        out_bare["ratio_cloaked_over_bare"] = ratio

        ref = CPL20[base]
        print(f"  base={base} (r1={r1} cells): Q_ext(bare)={out_bare['q_ext']:.4f} "
              f"(cpl20 was {ref['bare']:.4f})  Q_ext(cloak)={out_cloak['q_ext']:.4f} "
              f"(cpl20 was {ref['cloak']:.4f})  ratio={ratio:.4f} (cpl20 was {ref['ratio']:.4f})  "
              f"boxdev(bare/cloak)={out_bare['box_dev']:.3f}/{out_cloak['box_dev']:.3f} "
              f"(cpl20 cloak was {ref['box_dev_cloak']:.3f})", flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print(f"exp-010 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
