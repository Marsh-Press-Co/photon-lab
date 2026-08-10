"""
exp-006 -- The Shell Ratio: the runs.
======================================
Holds the cloak's outer radius r2 (=90 cells, exp-002/003/004's own
electrical size) and lambda (=600nm) fixed, and sweeps the inner radius
r1 (core) instead -- changing eps_z = (r2/(r2-r1))^2 independently of
overall cloak scale. Two mu_r_floor values reused exactly from
exp-004/005 (0.10, 0.18) at each of 4 r1 points, to test whether that
already-characterized jump tracks eps_z.

Only the cloak scene has r1/mu_r_floor -- reflector/absorber are not run.
A single empty reference is captured once and reused across the whole
sweep (r2/domain never change, only the internal r1 boundary moves).

Predictions were committed before this file first ran (see NOTES.md).

    .venv\\Scripts\\python.exe experiments\\006-shell-ratio\\run.py
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

# --- identical to exp-003/004 baseline domain (cpl=20, lambda=600nm, f=1) ---
N, ABSORB, FRAC, STEPS = 680, 40, 0.32, 3600
CX, CY = 300, 300
SRC_X = 64
CPL = 20
REF_HALF_H = 60
MIN_MARGIN = 60
BOX_A_HALF, BOX_B_HALF = 110, 135
R2_CELLS = 90                                  # outer cloak radius -- FIXED throughout

# --- exp-006 free variables ---
CORE_SWEEP = [15, 30, 40, 48]                  # r1, cells -- 30 is the exp-004/005 baseline
FLOOR_SWEEP = [0.10, 0.18]                     # reused exactly from exp-004/005's cleanest jump

# exp-004/005's own cpl=20, lambda=600, core=30 (eps_z=2.25) numbers, for reproduction check
BASELINE_QEXT = {0.10: 0.6620, 0.18: 0.5449}


def clamp_geometry(r1_cells, floor):
    """clamp_width = r1 * sqrt(floor) / (1 - sqrt(floor)) [cells]; frac of shell it covers."""
    s = math.sqrt(floor)
    width = r1_cells * s / (1.0 - s)
    frac = width / (R2_CELLS - r1_cells)
    return width, frac


def degeneracy_threshold(r1_cells):
    """floor above this value clamps the ENTIRE shell to mu_r_floor uniformly --
    the natural (unclamped) mu_r at r=r2 is ((r2-r1)/r2)^2."""
    return ((R2_CELLS - r1_cells) / R2_CELLS) ** 2


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

    print(f"r2 (fixed) = {R2_CELLS} cells, lambda=600nm, cpl={CPL}", flush=True)
    for r1 in CORE_SWEEP:
        eps_z = (R2_CELLS / (R2_CELLS - r1)) ** 2
        thresh = degeneracy_threshold(r1)
        print(f"  core={r1}: eps_z={eps_z:.3f}  degeneracy_threshold={thresh:.3f}", flush=True)
        for floor in FLOOR_SWEEP:
            assert floor < thresh, \
                f"core={r1}, floor={floor} at/above degeneracy threshold {thresh:.3f} " \
                f"-- shell would be uniformly clamped, not graded"
            cmax = math.sqrt(floor * eps_z)
            assert FRAC < cmax, \
                f"core={r1}, floor={floor} unstable at courant_frac={FRAC} (ceiling={cmax:.3f})"

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
            width, frac = clamp_geometry(r1, floor)
            out["clamp_width_cells"] = width
            out["clamp_frac_of_shell"] = frac
            results[f"cloak-core{r1}-floor{floor}"] = out
            print(f"  core={r1:2d} floor={floor:.2f}: Q_ext={out['q_ext']:.4f}  "
                  f"back={out['back_frac']:.4f}  boxdev={box_dev:.3f}  crossdev={cross_dev:.3f}  "
                  f"clamp_frac={frac:.3f}", flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print(f"exp-006 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
