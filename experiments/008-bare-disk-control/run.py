"""
exp-008 -- The Bare-Disk Control: the runs.
============================================================
Isolates exp-007's flagged caveat: strips the cloak shell entirely and
measures the *bare* PEC disk's own Q_ext across the same 7 core radii
exp-006/007 already characterized with a cloak (r1 in
{8, 10, 12, 15, 20, 25, 30}, lambda=600nm). Divide exp-006/007's cloaked
Q_ext by this experiment's bare Q_ext at matched r1 to separate "smaller
hidden object trivially scatters less" from "the shell genuinely cloaks
better."

Predictions were committed before this file first ran (see NOTES.md).

    .venv\\Scripts\\python.exe experiments\\008-bare-disk-control\\run.py
"""

import json
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from lab import Sim, materials
from lab import sections as sc

HERE = os.path.dirname(os.path.abspath(__file__))

# --- identical to exp-003/004/006/007 baseline domain (cpl=20, lambda=600nm, f=1) ---
N, ABSORB, FRAC, STEPS = 680, 40, 0.32, 3600
CX, CY = 300, 300
SRC_X = 64
CPL = 20
REF_HALF_H = 60
MIN_MARGIN = 60
BOX_A_HALF, BOX_B_HALF = 110, 135
R2_CELLS = 90                                  # fixed footprint denominator -- matches exp-006/007

# --- exp-008 free variable: the full 7-point core set exp-006/007 already ran with a cloak ---
CORE_SWEEP = [8, 10, 12, 15, 20, 25, 30]

# exp-006/007's cloaked Q_ext at these exact 7 points, floor=0.10, for the ratio this
# experiment exists to compute (reused, not rerun -- already-gated data)
EXP006_007_QEXT_CLOAKED = {
    8: 0.0429, 10: 0.0520, 12: 0.0591, 15: 0.0934,
    20: 0.2592, 25: 0.4913, 30: 0.6620,
}


def box_coords():
    for half, name in ((BOX_A_HALF, "box_a"), (BOX_B_HALF, "box_b")):
        margin_x = min(CX - half, N - ABSORB - (CX + half)) - ABSORB
        margin_y = min(CY - half, N - ABSORB - (CY + half)) - ABSORB
        assert margin_x >= MIN_MARGIN and margin_y >= MIN_MARGIN, \
            f"{name} clearance too tight (margin={min(margin_x, margin_y)})"
        assert half > R2_CELLS, f"{name} does not clear the largest core"
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

    print(f"bare PEC disk control, r2_footprint (fixed denom) = {R2_CELLS} cells, "
          f"lambda=600nm, cpl={CPL}", flush=True)

    box_a, box_b = box_coords()
    cap_e = run_scene(None)

    for r1 in CORE_SWEEP:
        def build(sim, r1=r1):
            materials.pec_disk(sim, CX, CY, r1)
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
        q_cloaked = EXP006_007_QEXT_CLOAKED[r1]
        out["q_ext_cloaked_exp006_007"] = q_cloaked
        out["ratio_cloaked_over_bare"] = q_cloaked / out["q_ext"]
        results[f"bare-core{r1}"] = out
        print(f"  core={r1:2d}: Q_ext(bare)={out['q_ext']:.4f}  "
              f"Q_ext(cloaked)={q_cloaked:.4f}  ratio={out['ratio_cloaked_over_bare']:.4f}  "
              f"boxdev={box_dev:.3f}  crossdev={cross_dev:.3f}", flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print(f"exp-008 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
