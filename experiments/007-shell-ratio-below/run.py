"""
exp-007 -- Chasing the Shell-Ratio Design Lead: the runs.
============================================================
Follow-up to exp-006's incidental finding (core=15/floor=0.10 gave the
best Q_ext in the lab's history). Traces the Q_ext(eps_z) curve below and
around core=15 at fixed lambda=600nm/floor=0.10 -- core in
{8, 10, 12, 20, 25} -- to test whether the shell-thickening law keeps
improving Q_ext or core=15 was near a floor of its own.

Predictions were committed before this file first ran (see NOTES.md).

    .venv\\Scripts\\python.exe experiments\\007-shell-ratio-below\\run.py
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

# --- identical to exp-003/004/006 baseline domain (cpl=20, lambda=600nm, f=1) ---
N, ABSORB, FRAC, STEPS = 680, 40, 0.32, 3600
CX, CY = 300, 300
SRC_X = 64
CPL = 20
REF_HALF_H = 60
MIN_MARGIN = 60
BOX_A_HALF, BOX_B_HALF = 110, 135
R2_CELLS = 90                                  # outer cloak radius -- FIXED, matches exp-006

# --- exp-007 free variable ---
CORE_SWEEP = [8, 10, 12, 20, 25]               # fills gaps around exp-006's core=15/30
FLOOR = 0.10                                    # the floor that produced exp-006's design lead

# exp-006's own core=15/30 numbers at floor=0.10, for context in this file's output
EXP006_QEXT = {15: 0.0934, 30: 0.6620}


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
    sim = Sim(N, N, cells_per_lambda=CPL, courant_frac=FRAC, absorb=ABSORB)
    if build is not None:
        build(sim)
    sim.add_line_source(SRC_X)
    sim.run(STEPS)
    return sc.full_capture(sim)


def main():
    t0 = time.time()
    results = {}

    print(f"r2 (fixed) = {R2_CELLS} cells, lambda=600nm, cpl={CPL}, floor={FLOOR}", flush=True)
    for r1 in CORE_SWEEP:
        eps_z = (R2_CELLS / (R2_CELLS - r1)) ** 2
        cmax = math.sqrt(FLOOR * eps_z)
        print(f"  core={r1}: eps_z={eps_z:.4f}  cfl_ceiling={cmax:.4f}  "
              f"margin={'OK' if FRAC < cmax else 'UNSTABLE!'}", flush=True)
        assert FRAC < cmax, f"core={r1} unstable at courant_frac={FRAC} (ceiling={cmax:.3f})"

    box_a, box_b = box_coords()
    cap_e = run_scene(None)

    for r1 in CORE_SWEEP:
        eps_z = (R2_CELLS / (R2_CELLS - r1)) ** 2

        def build(sim, r1=r1):
            materials.pec_disk(sim, CX, CY, r1)
            materials.schurig_reduced_cloak_tm(sim, CX, CY, r1, R2_CELLS,
                                               mu_r_floor=FLOOR)
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
        out["eps_z"] = eps_z
        out["mu_r_floor"] = FLOOR
        results[f"cloak-core{r1}-floor{FLOOR}"] = out
        print(f"  core={r1:2d}: Q_ext={out['q_ext']:.4f}  back={out['back_frac']:.4f}  "
              f"boxdev={box_dev:.3f}  crossdev={cross_dev:.3f}", flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print(f"exp-007 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
