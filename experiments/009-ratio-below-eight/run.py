"""
exp-009 -- The Ratio Below Eight: the runs.
============================================================
Traces the cloaked/bare Q_ext ratio (exp-008's headline number) below
exp-006/007/008's smallest tested core (r1=8), at r1 in {4, 5, 6, 7}
cells, lambda=600nm, mu_r_floor=0.10 fixed. Unlike exp-008 (which reused
already-gated exp-006/007 cloaked numbers), this file runs BOTH bare and
cloaked scenes at each new core -- new territory, paired, gated fresh.

CFL margin is checked explicitly and asserted stable before any run, per
the discipline exp-007 established and PLAN.md queued as this
experiment's precondition.

Predictions were committed before this file first ran (see NOTES.md).

    .venv\\Scripts\\python.exe experiments\\009-ratio-below-eight\\run.py
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

# --- identical to exp-003/004/006/007/008 baseline domain (cpl=20, lambda=600nm, f=1) ---
N, ABSORB, FRAC, STEPS = 680, 40, 0.32, 3600
CX, CY = 300, 300
SRC_X = 64
CPL = 20
REF_HALF_H = 60
MIN_MARGIN = 60
BOX_A_HALF, BOX_B_HALF = 110, 135
R2_CELLS = 90                                  # fixed outer cloak radius / footprint denominator
FLOOR = 0.10                                    # fixed throughout -- exp-006/007/008's value

# --- exp-009 free variable: four new core points below exp-006/007/008's floor of 8 ---
CORE_SWEEP = [4, 5, 6, 7]

# exp-008's plateau reference, for context in this file's printed output
EXP008_RATIO_PLATEAU = {8: 0.194, 10: 0.194, 12: 0.193}


def check_cfl():
    print(f"CFL margin check (floor={FLOOR}, courant_frac={FRAC}, r2={R2_CELLS}):", flush=True)
    for r1 in CORE_SWEEP:
        eps_z = (R2_CELLS / (R2_CELLS - r1)) ** 2
        cmax = math.sqrt(FLOOR * eps_z)
        margin = cmax / FRAC - 1.0
        print(f"  core={r1}: eps_z={eps_z:.4f}  cfl_ceiling={cmax:.4f}  "
              f"margin={margin * 100:.2f}%  {'OK' if FRAC < cmax else 'UNSTABLE!'}", flush=True)
        assert FRAC < cmax, f"core={r1} unstable at courant_frac={FRAC} (ceiling={cmax:.4f})"


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

    check_cfl()
    print(f"r2 (fixed) = {R2_CELLS} cells, lambda=600nm, cpl={CPL}, floor={FLOOR}", flush=True)

    box_a, box_b = box_coords()
    cap_e = run_scene(None)

    for r1 in CORE_SWEEP:
        eps_z = (R2_CELLS / (R2_CELLS - r1)) ** 2

        # bare
        def build_bare(sim, r1=r1):
            materials.pec_disk(sim, CX, CY, r1)
        cap_bare = run_scene(build_bare)
        out_bare = measure(cap_bare, cap_e, box_a, box_b, r1, {})
        results[f"bare-core{r1}"] = out_bare

        # cloaked
        def build_cloak(sim, r1=r1):
            materials.pec_disk(sim, CX, CY, r1)
            materials.schurig_reduced_cloak_tm(sim, CX, CY, r1, R2_CELLS,
                                               mu_r_floor=FLOOR)
        cap_cloak = run_scene(build_cloak)
        out_cloak = measure(cap_cloak, cap_e, box_a, box_b, r1,
                             {"eps_z": eps_z, "mu_r_floor": FLOOR})
        results[f"cloak-core{r1}-floor{FLOOR}"] = out_cloak

        ratio = out_cloak["q_ext"] / out_bare["q_ext"]
        out_cloak["ratio_cloaked_over_bare"] = ratio
        out_bare["ratio_cloaked_over_bare"] = ratio

        print(f"  core={r1}: Q_ext(bare)={out_bare['q_ext']:.4f}  "
              f"Q_ext(cloaked)={out_cloak['q_ext']:.4f}  ratio={ratio:.4f}  "
              f"boxdev(bare/cloak)={out_bare['box_dev']:.3f}/{out_cloak['box_dev']:.3f}  "
              f"crossdev(bare/cloak)={out_bare['cross_dev']:.3f}/{out_cloak['cross_dev']:.3f}",
              flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print(f"exp-009 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
