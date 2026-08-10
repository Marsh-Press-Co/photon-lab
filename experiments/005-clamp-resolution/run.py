"""
exp-005 -- Does the Clamp Jump Shrink With Resolution?: the runs.
===================================================================
Targeted follow-up to exp-004: same mu_r_floor sweep (0.05/0.10/0.18/
0.28/0.40), same physical geometry, same lambda=600nm, but cells-per-
lambda raised from exp-003/004's 20 to 30 (1.5x) -- to test whether the
600nm jump (floor=0.10->0.18, 0.662->0.545 at cpl=20) is a staircase
artifact of the clamp boundary's cell-alignment, which should shrink as
resolution increases.

Predictions were committed before this file first ran (see NOTES.md).

    .venv\\Scripts\\python.exe experiments\\005-clamp-resolution\\run.py
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

# --- exp-003/004 baseline (cpl=20) geometry, scaled by 1.5x to cpl=30 ---
CPL_BASE, CPL_NEW = 20, 30
SCALE = CPL_NEW / CPL_BASE                          # 1.5

N = int(round(680 * SCALE))                         # 1020
CX = CY = int(round(300 * SCALE))                   # 450
ABSORB = int(round(40 * SCALE))                      # 60
STEPS = int(round(3600 * SCALE))                     # 5400
FRAC = 0.32                                          # unchanged: eps_z is f-invariant
SRC_X = int(round(64 * SCALE))
REF_HALF_H = int(round(60 * SCALE))
MIN_MARGIN = int(round(60 * SCALE))

RADII_BASE = {"core": 30, "clk": 90}                 # cells, at cpl=20
BOX_BASE = {"a": 110, "b": 135}
LAM_NM = 600.0                                       # single lambda, the clearest exp-004 jump
FLOOR_SWEEP = [0.05, 0.10, 0.18, 0.28, 0.40]
EPS_Z = (RADII_BASE["clk"] / (RADII_BASE["clk"] - RADII_BASE["core"])) ** 2  # 2.25

# exp-004's cpl=20 baseline numbers, for direct comparison in this file's output
CPL20_QEXT = {0.05: 0.3859, 0.10: 0.6620, 0.18: 0.5449, 0.28: 1.3355, 0.40: 1.4612}


def geometry():
    r = {k: int(round(v * SCALE)) for k, v in RADII_BASE.items()}
    box_a = int(round(BOX_BASE["a"] * SCALE))
    box_b = int(round(BOX_BASE["b"] * SCALE))
    for half, name in ((box_a, "box_a"), (box_b, "box_b")):
        margin_x = min(CX - half, N - ABSORB - (CX + half)) - ABSORB
        margin_y = min(CY - half, N - ABSORB - (CY + half)) - ABSORB
        assert margin_x >= MIN_MARGIN and margin_y >= MIN_MARGIN, \
            f"{name} clearance too tight (margin={min(margin_x, margin_y)})"
        assert half > r["clk"], f"{name} does not clear the cloak"
    return r, (CX - box_a, CX + box_a, CY - box_a, CY + box_a), \
           (CX - box_b, CX + box_b, CY - box_b, CY + box_b)


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

    for f in FLOOR_SWEEP:
        cmax = math.sqrt(f * EPS_Z)
        assert FRAC < cmax, f"floor={f} unstable at courant_frac={FRAC}"
    print(f"eps_z={EPS_Z}, N={N}, CX=CY={CX}, ABSORB={ABSORB}, STEPS={STEPS}, "
          f"CPL={CPL_NEW}", flush=True)

    r, box_a, box_b = geometry()
    print(f"geometry: core={r['core']}, clk={r['clk']} cells (900/2700nm physical, "
          f"unchanged from exp-003/004)", flush=True)

    cap_e = run_scene(None)

    for floor in FLOOR_SWEEP:
        def build(sim, r=r, floor=floor):
            materials.pec_disk(sim, CX, CY, r["core"])
            materials.schurig_reduced_cloak_tm(sim, CX, CY, r["core"], r["clk"],
                                               mu_r_floor=floor)
        cap = run_scene(build)
        wa = sc.widths(cap, cap_e, box_a, (CX, CY, REF_HALF_H))
        wb = sc.widths(cap, cap_e, box_b, (CX, CY, REF_HALF_H))
        box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])
        cross_dev = abs(wa["sigma_ext"] - wa["sigma_ext_cross"]) / abs(wa["sigma_ext"])
        out = {k: wa[k] for k in ("sigma_scat", "sigma_abs", "sigma_ext",
                                   "sigma_ext_cross", "back_frac", "fwd_frac", "i_inc")}
        out["q_ext"] = wa["sigma_ext"] / (2.0 * r["clk"])
        out["box_dev"] = box_dev
        out["cross_dev"] = cross_dev
        out["mu_r_floor"] = floor
        out["cpl"] = CPL_NEW
        results[f"cloak-600-cpl30-floor{floor}"] = out
        cpl20 = CPL20_QEXT[floor]
        print(f"  floor={floor:.2f}: Q_ext={out['q_ext']:.4f}  "
              f"(cpl20 was {cpl20:.4f}, ratio={out['q_ext'] / cpl20:.3f})  "
              f"back={out['back_frac']:.4f}  boxdev={box_dev:.3f}  crossdev={cross_dev:.3f}",
              flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print(f"exp-005 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
