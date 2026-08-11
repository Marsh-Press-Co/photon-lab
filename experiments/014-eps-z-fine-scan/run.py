"""
exp-014 -- The Fine eps_z Scan Bracketing 2.25: the runs.
==========================================================
exp-006/011/012/013 found that of 4 core/eps_z points swept across the
mu_r_floor=0.10->0.18 pair, only core=30 (eps_z=2.25, the exp-002/003/004
baseline geometry) shows a *negative* jump -- the other three (eps_z=1.44,
3.24, 4.59) all show the "naive" positive direction. This experiment is
the queued follow-up: a FINE r1 scan bracketing r1=30 on both sides
(27,28,29,31,32,33 -> eps_z=2.04..2.49, step ~1 cell) at the same
floor=0.10/0.18 pair, to see whether the negative jump is an isolated,
sub-cell-narrow feature at exactly r1=30, or part of a smooth trough that
several nearby core values also sit inside.

core=30 itself is NOT rerun -- exp-004/006's own numbers (Q_ext=0.6620 at
floor=0.10, 0.5449 at floor=0.18) are reused directly, same convention as
exp-011/012/013 reusing exp-006's core=15/40/48 points.

Predictions were committed before this file first ran (see NOTES.md).

    .venv\\Scripts\\python.exe experiments\\014-eps-z-fine-scan\\run.py
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

# --- identical to exp-006/.../013 baseline domain (cpl=20, lambda=600nm, f=1) ---
N, ABSORB, FRAC, STEPS = 680, 40, 0.32, 3600
CX, CY = 300, 300
SRC_X = 64
CPL = 20
REF_HALF_H = 60
MIN_MARGIN = 60
BOX_A_HALF, BOX_B_HALF = 110, 135
R2_CELLS = 90                                  # outer cloak radius -- fixed, matches exp-006+

# --- exp-014 free variables ---
CORE_SWEEP = [27, 28, 29, 31, 32, 33]          # r1, cells -- brackets r1=30 (eps_z=2.25), not rerun
FLOOR_SWEEP = [0.10, 0.18]                     # reused exactly from exp-004/005/006/011/012/013

# exp-004/006's own core=30/eps_z=2.25 numbers, for the full bracketed comparison (not rerun here)
CORE30_QEXT = {0.10: 0.6620, 0.18: 0.5449}


def degeneracy_threshold(r1_cells):
    return ((R2_CELLS - r1_cells) / R2_CELLS) ** 2


def check_gates():
    print(f"r2 (fixed) = {R2_CELLS} cells, lambda=600nm, cpl={CPL}, courant_frac={FRAC}", flush=True)
    for r1 in CORE_SWEEP:
        eps_z = (R2_CELLS / (R2_CELLS - r1)) ** 2
        thresh = degeneracy_threshold(r1)
        print(f"  core={r1}: eps_z={eps_z:.4f}  degeneracy_threshold={thresh:.4f}", flush=True)
        for floor in FLOOR_SWEEP:
            cmax = math.sqrt(floor * eps_z)
            assert FRAC < cmax, \
                f"core={r1}, floor={floor} unstable at courant_frac={FRAC} (ceiling={cmax:.4f})"
            assert floor < thresh, \
                f"core={r1}, floor={floor} at/above degeneracy threshold {thresh:.4f}"


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

    check_gates()

    box_a, box_b = box_coords()
    cap_e = run_scene(None)

    for r1 in CORE_SWEEP:
        eps_z = (R2_CELLS / (R2_CELLS - r1)) ** 2
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
            out["eps_z"] = eps_z
            out["mu_r_floor"] = floor
            results[f"cloak-core{r1}-floor{floor}"] = out
            print(f"  core={r1:2d} eps_z={eps_z:.4f} floor={floor:.2f}: Q_ext={out['q_ext']:.4f}  "
                  f"back={out['back_frac']:.4f}  boxdev={box_dev:.3f}  crossdev={cross_dev:.3f}",
                  flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print(f"exp-014 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
