"""
exp-002 — How Invisible Is Invisible: the runs.
===============================================
Same scene family as exp-001 (one PEC core, three dressings, empty
reference) at 450/600/750 nm, measured in the proper currency: scattering
/ absorption / extinction widths via lab.sections (trust-suite stage 8),
two boxes each (independence reported), Q_ext per object's own silhouette.

Predictions were committed before the machinery existed (eda79c0).

    .venv\\Scripts\\python.exe experiments\\002-cross-sections\\run.py
"""

import json
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import numpy as np

from lab import Sim, materials
from lab import sections as sc

HERE = os.path.dirname(os.path.abspath(__file__))

N, ABSORB, FRAC, STEPS = 560, 40, 0.32, 3200
CX, CY = 252, 280
R_CORE, R_COAT, R_CLK = 30, 78, 90
SRC_X = 64
SWEEP = [(15, 450), (20, 600), (25, 750)]
BOX_A = (142, 362, 170, 390)
BOX_B = (117, 387, 145, 415)
REF = (CX, CY, 60)
OUTER = {"reflector": R_CORE, "absorber": R_COAT, "cloak": R_CLK}


def build(scene, sim):
    if scene == "reflector":
        materials.pec_disk(sim, CX, CY, R_CORE)
    elif scene == "absorber":
        materials.pec_disk(sim, CX, CY, R_CORE)
        materials.graded_black_shell(sim, CX, CY, R_CORE, R_COAT)
    elif scene == "cloak":
        materials.pec_disk(sim, CX, CY, R_CORE)
        materials.schurig_reduced_cloak_tm(sim, CX, CY, R_CORE, R_CLK,
                                           mu_r_floor=0.05)


def run_scene(scene, cpl):
    sim = Sim(N, N, cells_per_lambda=cpl, courant_frac=FRAC, absorb=ABSORB)
    build(scene, sim)
    sim.add_line_source(SRC_X)
    sim.run(STEPS)
    return sc.full_capture(sim)


def main():
    t0 = time.time()
    results = {}
    for cpl, nm in SWEEP:
        print(f"--- lambda = {nm} nm ---", flush=True)
        cap_e = run_scene("empty", cpl)
        for scene in ("reflector", "absorber", "cloak"):
            cap = run_scene(scene, cpl)
            wa = sc.widths(cap, cap_e, BOX_A, REF)
            wb = sc.widths(cap, cap_e, BOX_B, REF)
            box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])
            r = {k: wa[k] for k in ("sigma_scat", "sigma_abs", "sigma_ext",
                                    "sigma_ext_cross", "back_frac", "fwd_frac")}
            r["q_ext"] = wa["sigma_ext"] / (2.0 * OUTER[scene])
            r["box_dev"] = box_dev
            results[f"{scene}-{nm}"] = r
            print(f"  {scene:9s}: sig_ext={r['sigma_ext']:7.1f}  "
                  f"Q_ext={r['q_ext']:.3f}  abs/ext={r['sigma_abs'] / r['sigma_ext']:.3f}  "
                  f"back={r['back_frac']:.4f}  boxdev={box_dev:.3f}", flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(results, f, indent=2, sort_keys=True)
    print(f"exp-002 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
