"""
exp-012 -- The Floor Sweep at core=40 (exp-006's Candidate C, third
generalization point): the runs.
============================================================
Adds floor=0.05 and floor=0.28 to exp-006's existing core=40/eps_z=3.24
data (which already covered floor=0.10/0.18) -- tests whether core=40's
floor curve stays monotonic across the whole tested range, the way
exp-011's core=15 curve did, or sign-flips the way exp-004/005's core=30
baseline did. floor=0.40 is excluded here on DEGENERACY grounds (shell
would clamp uniformly, not CFL grounds like exp-011's exclusion) -- see
NOTES.md.

Predictions were committed before this file first ran (see NOTES.md).

    .venv\\Scripts\\python.exe experiments\\012-floor-sweep-core40\\run.py
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

# --- identical to exp-006/.../011 baseline domain (cpl=20, lambda=600nm, f=1) ---
N, ABSORB, FRAC, STEPS = 680, 40, 0.32, 3600
CX, CY = 300, 300
SRC_X = 64
CPL = 20
REF_HALF_H = 60
MIN_MARGIN = 60
BOX_A_HALF, BOX_B_HALF = 110, 135
R2_CELLS = 90                                  # outer cloak radius -- fixed, matches exp-006

# --- exp-012 free variable ---
CORE = 40
EPS_Z = (R2_CELLS / (R2_CELLS - CORE)) ** 2    # 3.24
DEGENERACY_THRESHOLD = ((R2_CELLS - CORE) / R2_CELLS) ** 2   # 0.3086
FLOOR_SWEEP = [0.05, 0.28]                      # 0.10/0.18 reused from exp-006; 0.40 degenerate here

# exp-006's existing core=40 numbers, for context / the full 4-point comparison
EXP006_QEXT = {0.10: 0.75403, 0.18: 1.28709}


def check_gates():
    print(f"core={CORE}, eps_z={EPS_Z:.4f}, degeneracy_threshold={DEGENERACY_THRESHOLD:.4f}, "
          f"courant_frac={FRAC}:", flush=True)
    for floor in FLOOR_SWEEP + [0.40]:
        cmax = math.sqrt(floor * EPS_Z)
        cfl_ok = FRAC < cmax
        graded_ok = floor < DEGENERACY_THRESHOLD
        status = "OK" if (cfl_ok and graded_ok) else "EXCLUDED"
        reason = "" if status == "OK" else (
            "degenerate (fully clamped)" if not graded_ok else "CFL unstable")
        print(f"  floor={floor}: cfl_ceiling={cmax:.4f} ({'stable' if cfl_ok else 'UNSTABLE'})  "
              f"graded={'yes' if graded_ok else 'no'}  {status} {reason}".rstrip(), flush=True)
    for floor in FLOOR_SWEEP:
        cmax = math.sqrt(floor * EPS_Z)
        assert FRAC < cmax, f"floor={floor} unstable at courant_frac={FRAC} (ceiling={cmax:.4f})"
        assert floor < DEGENERACY_THRESHOLD, \
            f"floor={floor} at/above degeneracy threshold {DEGENERACY_THRESHOLD:.4f}"


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
    print(f"core={CORE}, r2={R2_CELLS}, eps_z={EPS_Z}, lambda=600nm, cpl={CPL}", flush=True)

    box_a, box_b = box_coords()
    cap_e = run_scene(None)

    for floor in FLOOR_SWEEP:
        def build(sim, floor=floor):
            materials.pec_disk(sim, CX, CY, CORE)
            materials.schurig_reduced_cloak_tm(sim, CX, CY, CORE, R2_CELLS,
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
        out["core_r1_cells"] = CORE
        out["eps_z"] = EPS_Z
        out["mu_r_floor"] = floor
        results[f"cloak-core{CORE}-floor{floor}"] = out
        print(f"  floor={floor:.2f}: Q_ext={out['q_ext']:.4f}  back={out['back_frac']:.4f}  "
              f"boxdev={box_dev:.3f}  crossdev={cross_dev:.3f}", flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print(f"exp-012 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
