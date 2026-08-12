"""
exp-019 -- Shell Thickness at 2 Wavelengths: the runs.
========================================================
exp-018 found that the "eps_z trough" (exp-014/015/016/017) is not an
eps_z effect at all -- holding eps_z fixed in its established trough
window (2.22-2.29) while sweeping lambda made the negative floor-jump
vanish everywhere except lambda=600nm, the one point where the cloak
shell's radial extent (r2-r1) lands on an EXACT integer number of
wavelengths (60 cells = 3.00 x 20 cells/lambda). Sharpened hypothesis:
the trough is a shell-thickness standing-wave / Fabry-Perot condition,
not a property of eps_z.

This is the direct test exp-018's Next section queued: fix
lambda=600nm/cpl=20 (so 1 cell = lambda/20 exactly) and bracket a
DIFFERENT integer -- 2 lambda = 40 cells -- the same way exp-014
bracketed 3 lambda (60 cells) with a +/-3-cell scan around it. Same
"vary r1 at fixed r2=90" idiom this whole eps_z line has used since
exp-006 (core radius r1 and eps_z both move together; only outer radius
r2 stays fixed).

Predictions were committed before this file first ran (see NOTES.md).

    .venv/bin/python experiments/019-shell-thickness-2lambda/run.py
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

# --- identical to exp-006/.../018 baseline domain (cpl=20, lambda=600nm, f=1) ---
N, ABSORB, FRAC, STEPS = 680, 40, 0.32, 3600
CX, CY = 300, 300
SRC_X = 64
CPL = 20
REF_HALF_H = 60
MIN_MARGIN = 60
BOX_A_HALF, BOX_B_HALF = 110, 135
R2_CELLS = 90                                  # outer cloak radius -- fixed, matches exp-006+

# --- exp-019 free variables ---
CORE_SWEEP = [47, 48, 49, 50, 51, 52, 53]      # r1 -- brackets r1=50 (shell=40 cells=2.00 lambda)
FLOOR_SWEEP = [0.10, 0.18]                     # the trough's own defining floor pair, reused throughout

# exp-006/013's own core=48 numbers (r1=48 falls inside this sweep), for the reproduction check
CORE48_QEXT = {0.10: 1.20959, 0.18: 1.67510}


def degeneracy_threshold(r1_cells):
    return ((R2_CELLS - r1_cells) / R2_CELLS) ** 2


def check_gates():
    print(f"r2 (fixed) = {R2_CELLS} cells, lambda=600nm, cpl={CPL}, courant_frac={FRAC}", flush=True)
    excluded = set()
    for r1 in CORE_SWEEP:
        shell = R2_CELLS - r1
        eps_z = (R2_CELLS / shell) ** 2
        thresh = degeneracy_threshold(r1)
        print(f"  r1={r1}: shell={shell} cells ({shell / CPL:.2f} lambda)  eps_z={eps_z:.4f}  "
              f"degeneracy_thresh={thresh:.4f}", flush=True)
        for floor in FLOOR_SWEEP:
            cmax = math.sqrt(floor * eps_z)
            cfl_ok = FRAC < cmax
            graded_ok = floor < thresh
            status = "OK" if (cfl_ok and graded_ok) else "EXCLUDED"
            reason = "" if status == "OK" else (
                "degenerate (fully clamped)" if not graded_ok else "CFL unstable")
            print(f"    floor={floor}: cfl_ceiling={cmax:.4f} "
                  f"({'stable' if cfl_ok else 'UNSTABLE'})  graded={'yes' if graded_ok else 'no'}  "
                  f"{status} {reason}".rstrip(), flush=True)
            if status == "EXCLUDED":
                excluded.add((r1, floor))
            else:
                assert cfl_ok, f"r1={r1}, floor={floor} unstable (ceiling={cmax:.4f})"
    return excluded


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

    excluded = check_gates()
    box_a, box_b = box_coords()
    cap_e = run_scene(None)

    for r1 in CORE_SWEEP:
        shell = R2_CELLS - r1
        eps_z = (R2_CELLS / shell) ** 2
        for floor in FLOOR_SWEEP:
            if (r1, floor) in excluded:
                print(f"  r1={r1:2d} floor={floor:.2f}: SKIPPED (degenerate)", flush=True)
                continue

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
            out["shell_cells"] = shell
            out["shell_lambda"] = shell / float(CPL)
            out["eps_z"] = eps_z
            out["mu_r_floor"] = floor
            results[f"cloak-core{r1}-floor{floor}"] = out
            print(f"  r1={r1:2d} shell={shell}({shell / CPL:.2f}lam) eps_z={eps_z:.4f} "
                  f"floor={floor:.2f}: Q_ext={out['q_ext']:.4f}  back={out['back_frac']:.4f}  "
                  f"boxdev={box_dev:.3f}  crossdev={cross_dev:.3f}", flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print(f"exp-019 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
