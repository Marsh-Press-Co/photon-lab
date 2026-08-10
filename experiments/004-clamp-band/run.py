"""
exp-004 -- The Clamp Band: the runs.
=====================================
Isolates mu_r_floor as the single free variable in the reduced cloak's
schurig_reduced_cloak_tm material: same geometry/cpl as exp-003 at four
wavelengths (420/480/540/600), sweeping mu_r_floor in
{0.05, 0.10, 0.18, 0.28, 0.40} to test whether the clamp band's relative
width explains exp-003's 480nm bump and sub-quadratic exponent.

Only the cloak scene has mu_r_floor -- reflector/absorber are not rerun.
Empty reference captured once per lambda, reused across the floor sweep.

Predictions were committed before this file first ran (see NOTES.md).

    .venv\\Scripts\\python.exe experiments\\004-clamp-band\\run.py
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

# --- identical to exp-003 (reused, not re-derived) ---
N, ABSORB, FRAC, STEPS = 680, 40, 0.32, 3600
CX, CY = 300, 300
SRC_X = 64
CPL = 20
REF_LAM_NM = 600.0
RADII_BASE = {"core": 30, "coat": 78, "clk": 90}   # cells, at f=1
BOX_BASE = {"a": 110, "b": 135}
REF_HALF_H = 60
MIN_MARGIN = 60

# --- exp-004 free variables ---
SWEEP_NM = [420, 480, 540, 600]
FLOOR_SWEEP = [0.05, 0.10, 0.18, 0.28, 0.40]
EPS_Z = (RADII_BASE["clk"] / (RADII_BASE["clk"] - RADII_BASE["core"])) ** 2  # 2.25, f-invariant


def scale_factor(nm):
    return REF_LAM_NM / float(nm)


def geometry(nm):
    """Identical to exp-003's geometry(): same domain, same margin assert,
    so this sweep inherits its box-independence fix for free."""
    f = scale_factor(nm)
    r = {k: int(round(v * f)) for k, v in RADII_BASE.items()}
    box_a = int(round(BOX_BASE["a"] * f))
    box_b = int(round(BOX_BASE["b"] * f))
    for half, name in ((box_a, "box_a"), (box_b, "box_b")):
        margin_x = min(CX - half, N - ABSORB - (CX + half)) - ABSORB
        margin_y = min(CY - half, N - ABSORB - (CY + half)) - ABSORB
        assert margin_x >= MIN_MARGIN and margin_y >= MIN_MARGIN, \
            f"{name} clearance too tight at {nm}nm (margin={min(margin_x, margin_y)})"
        assert half > r["clk"], f"{name} does not clear the cloak at {nm}nm"
    return r, (CX - box_a, CX + box_a, CY - box_a, CY + box_a), \
           (CX - box_b, CX + box_b, CY - box_b, CY + box_b)


def electrical_size(nm):
    r_outer_nm = RADII_BASE["clk"] * (REF_LAM_NM / CPL)
    return 2.0 * r_outer_nm / nm


def clamp_geometry(r1_cells, floor):
    """clamp_width = r1 * sqrt(floor) / (1 - sqrt(floor)) [cells]."""
    s = math.sqrt(floor)
    width = r1_cells * s / (1.0 - s)
    return width


def run_scene(build, sim_kwargs):
    sim = Sim(N, N, cells_per_lambda=CPL, courant_frac=FRAC, absorb=ABSORB)
    if build is not None:
        build(sim)
    sim.add_line_source(SRC_X)
    sim.run(STEPS)
    return sc.full_capture(sim)


def main():
    t0 = time.time()
    results = {}
    max_stable_courant = {f: math.sqrt(f * EPS_Z) for f in FLOOR_SWEEP}
    print(f"eps_z (f-invariant) = {EPS_Z}", flush=True)
    for f, cmax in max_stable_courant.items():
        print(f"  floor={f}: courant_frac ceiling={cmax:.3f} "
              f"(using {FRAC}, margin={'OK' if FRAC < cmax else 'UNSTABLE!'})", flush=True)
        assert FRAC < cmax, f"floor={f} unstable at courant_frac={FRAC}"

    for nm in SWEEP_NM:
        r, box_a, box_b = geometry(nm)
        print(f"--- lambda = {nm} nm  (r_core={r['core']}, r_clk={r['clk']} cells) ---",
              flush=True)
        cap_e = run_scene(None, {})
        wa_e = None
        for floor in FLOOR_SWEEP:
            def build(sim, r=r, floor=floor):
                materials.pec_disk(sim, CX, CY, r["core"])
                materials.schurig_reduced_cloak_tm(sim, CX, CY, r["core"], r["clk"],
                                                   mu_r_floor=floor)
            cap = run_scene(build, {})
            wa = sc.widths(cap, cap_e, box_a, (CX, CY, REF_HALF_H))
            wb = sc.widths(cap, cap_e, box_b, (CX, CY, REF_HALF_H))
            box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])
            cross_dev = abs(wa["sigma_ext"] - wa["sigma_ext_cross"]) / abs(wa["sigma_ext"])
            out = {k: wa[k] for k in ("sigma_scat", "sigma_abs", "sigma_ext",
                                       "sigma_ext_cross", "back_frac", "fwd_frac", "i_inc")}
            out["q_ext"] = wa["sigma_ext"] / (2.0 * r["clk"])
            out["box_dev"] = box_dev
            out["cross_dev"] = cross_dev
            out["electrical_size"] = electrical_size(nm)
            out["r_outer_cells"] = r["clk"]
            out["mu_r_floor"] = floor
            width = clamp_geometry(r["core"], floor)
            out["clamp_width_cells"] = width
            out["clamp_frac_of_shell"] = width / (r["clk"] - r["core"])
            results[f"cloak-{nm}-floor{floor}"] = out
            print(f"  floor={floor:.2f}: sig_ext={out['sigma_ext']:7.1f}  "
                  f"Q_ext={out['q_ext']:.4f}  back={out['back_frac']:.4f}  "
                  f"boxdev={box_dev:.3f}  crossdev={cross_dev:.3f}  "
                  f"clamp_frac={out['clamp_frac_of_shell']:.3f}", flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print(f"exp-004 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
