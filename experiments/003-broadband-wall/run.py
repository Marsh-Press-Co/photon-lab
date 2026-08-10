"""
exp-003 — The Broadband Wall, Redesigned: the runs.
====================================================
Same scene family as exp-002 (one PEC core, three dressings, empty
reference) at 6 wavelengths, but with cells-per-lambda held FIXED at 20
for every run (grid resolution constant) and the geometry scaled in cells
so its PHYSICAL size (nm) stays fixed as lambda changes -- a real
fixed-size defect viewed at different colors, with the resolution
confound from exp-002 removed.

f(lambda) = 600nm / lambda; radii/box halves scale by f from the
exp-002 lambda=600/cpl=20 baseline (R_core/coat/clk = 30/78/90 cells,
box halves 110/135 cells). f(600) = 1 exactly -> that sweep point
reproduces exp-002's lambda=600 geometry bit-for-bit (the harness
sanity check).

Predictions were committed before this file first ran (b25e84a).

    .venv\\Scripts\\python.exe experiments\\003-broadband-wall\\run.py
"""

import json
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from lab import Sim, materials
from lab import sections as sc

HERE = os.path.dirname(os.path.abspath(__file__))

N, ABSORB, FRAC, STEPS = 560, 40, 0.32, 3200
CX, CY = 252, 280
SRC_X = 64
CPL = 20                                # FIXED across the whole sweep
REF_LAM_NM = 600.0                      # anchor: f(600) = 1
RADII_BASE = {"core": 30, "coat": 78, "clk": 90}     # cells, at f=1
BOX_BASE = {"a": 110, "b": 135}                       # cells, at f=1
SWEEP_NM = [420, 480, 540, 600, 660, 750]
REF_HALF_H = 60


def scale_factor(nm):
    return REF_LAM_NM / float(nm)


def geometry(nm):
    f = scale_factor(nm)
    r = {k: int(round(v * f)) for k, v in RADII_BASE.items()}
    box_a = int(round(BOX_BASE["a"] * f))
    box_b = int(round(BOX_BASE["b"] * f))
    # sanity: every box must clear the absorbing layer on all sides
    for half, name in ((box_a, "box_a"), (box_b, "box_b")):
        assert CX - half >= ABSORB and CX + half <= N - ABSORB, \
            f"{name} escapes domain at {nm}nm (half={half})"
        assert CY - half >= ABSORB and CY + half <= N - ABSORB, \
            f"{name} escapes domain at {nm}nm (half={half})"
        assert half > r["clk"], f"{name} does not clear the cloak at {nm}nm"
    return r, (CX - box_a, CX + box_a, CY - box_a, CY + box_a), \
           (CX - box_b, CX + box_b, CY - box_b, CY + box_b)


def electrical_size(scene, nm):
    """2*R_outer(nm, FIXED physical size) / lambda(nm) -- varies only
    because lambda changes, resolution held constant throughout."""
    r_outer_nm = RADII_BASE[{"reflector": "core", "absorber": "coat",
                              "cloak": "clk"}[scene]] * (REF_LAM_NM / CPL)
    return 2.0 * r_outer_nm / nm


def build(scene, sim, r):
    if scene == "reflector":
        materials.pec_disk(sim, CX, CY, r["core"])
    elif scene == "absorber":
        materials.pec_disk(sim, CX, CY, r["core"])
        materials.graded_black_shell(sim, CX, CY, r["core"], r["coat"])
    elif scene == "cloak":
        materials.pec_disk(sim, CX, CY, r["core"])
        materials.schurig_reduced_cloak_tm(sim, CX, CY, r["core"], r["clk"],
                                           mu_r_floor=0.05)


def run_scene(scene, r):
    sim = Sim(N, N, cells_per_lambda=CPL, courant_frac=FRAC, absorb=ABSORB)
    if scene != "empty":
        build(scene, sim, r)
    sim.add_line_source(SRC_X)
    sim.run(STEPS)
    return sc.full_capture(sim)


def main():
    t0 = time.time()
    results = {}
    outer_key = {"reflector": "core", "absorber": "coat", "cloak": "clk"}
    for nm in SWEEP_NM:
        r, box_a, box_b = geometry(nm)
        print(f"--- lambda = {nm} nm  (f={scale_factor(nm):.4f}, "
              f"r_clk={r['clk']} cells) ---", flush=True)
        cap_e = run_scene("empty", r)
        for scene in ("reflector", "absorber", "cloak"):
            cap = run_scene(scene, r)
            wa = sc.widths(cap, cap_e, box_a, (CX, CY, REF_HALF_H))
            wb = sc.widths(cap, cap_e, box_b, (CX, CY, REF_HALF_H))
            box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])
            cross_dev = abs(wa["sigma_ext"] - wa["sigma_ext_cross"]) / abs(wa["sigma_ext"])
            out = {k: wa[k] for k in ("sigma_scat", "sigma_abs", "sigma_ext",
                                       "sigma_ext_cross", "back_frac", "fwd_frac")}
            out["q_ext"] = wa["sigma_ext"] / (2.0 * r[outer_key[scene]])
            out["box_dev"] = box_dev
            out["cross_dev"] = cross_dev
            out["electrical_size"] = electrical_size(scene, nm)
            out["r_outer_cells"] = r[outer_key[scene]]
            results[f"{scene}-{nm}"] = out
            print(f"  {scene:9s}: sig_ext={out['sigma_ext']:7.1f}  "
                  f"Q_ext={out['q_ext']:.3f}  abs/ext={out['sigma_abs'] / out['sigma_ext']:.3f}  "
                  f"back={out['back_frac']:.4f}  boxdev={box_dev:.3f}  "
                  f"crossdev={cross_dev:.3f}  elec={out['electrical_size']:.3f}", flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(results, f, indent=2, sort_keys=True)
    print(f"exp-003 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
