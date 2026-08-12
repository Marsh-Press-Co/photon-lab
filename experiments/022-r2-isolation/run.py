"""
exp-022 -- R2 Isolation: is the shell=3lambda feature about r2=90, or about
shell thickness in general?
============================================================================
Every point in the eps_z/shell-thickness line since exp-006 has shared one
fixed outer cloak radius, r2=90 cells. exp-018 found the "eps_z trough"
(exp-014/015/016/017) is really a shell-thickness effect that appears at
exactly shell=3*lambda=60 cells (the r1=30/r2=90 point). exp-019 showed the
effect does NOT generalize to shell=2*lambda (40 cells) at that SAME r2=90.
Neither experiment has ever moved r2 -- so "shell=3lambda is special" and
"r2=90 is special" have never been told apart.

This experiment holds shell=3lambda=60 cells fixed (cpl=20, lambda=600nm)
and moves r2 itself: r2=75 (r1=15) and r2=120 (r1=60), bracketed +/-3 cells
each, mirroring exp-014/018/019's own bracket-around-the-target idiom.

Predictions were committed before this file first ran (see NOTES.md).

    .venv/bin/python experiments/022-r2-isolation/run.py
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

# --- identical domain/box machinery as exp-006/.../019, generalized over r2 ---
N, ABSORB, FRAC, STEPS = 680, 40, 0.32, 3600
CX, CY = 300, 300
SRC_X = 64
CPL = 20
REF_HALF_H = 60
MIN_MARGIN = 60
SHELL_TARGET = 3 * CPL                          # 60 cells = 3.00 lambda, the discriminator

# --- exp-022 free variable: r2 itself (fixed in every prior experiment in this line) ---
R2_SWEEP = [75, 120]                            # brackets exp-006..019's shared r2=90
FLOOR_SWEEP = [0.10, 0.18]                      # this line's defining pair, reused exactly

# box half-widths as an offset from r2, chosen to match r2=90's own convention
# EXACTLY: box_a=110=90+20, box_b=135=90+45 (exp-006 onward). Generalizing the
# offset (not the absolute size) is what keeps this comparison apples-to-apples.
BOX_A_OFFSET, BOX_B_OFFSET = 20, 45


def core_sweep(r2):
    target = r2 - SHELL_TARGET
    return list(range(target - 3, target + 4))


def degeneracy_threshold(r1, r2):
    return ((r2 - r1) / r2) ** 2


def check_gates():
    print(f"lambda=600nm, cpl={CPL} (shell target = {SHELL_TARGET} cells = "
          f"{SHELL_TARGET / CPL:.2f} lambda), courant_frac={FRAC}", flush=True)
    excluded = {}
    for r2 in R2_SWEEP:
        excluded[r2] = set()
        print(f" r2={r2} cells", flush=True)
        for r1 in core_sweep(r2):
            shell = r2 - r1
            eps_z = (r2 / shell) ** 2
            thresh = degeneracy_threshold(r1, r2)
            print(f"  r1={r1}: shell={shell} cells ({shell / CPL:.2f} lambda)  "
                  f"eps_z={eps_z:.4f}  degeneracy_thresh={thresh:.4f}", flush=True)
            for floor in FLOOR_SWEEP:
                cmax = math.sqrt(floor * eps_z)
                cfl_ok = FRAC < cmax
                graded_ok = floor < thresh
                status = "OK" if (cfl_ok and graded_ok) else "EXCLUDED"
                reason = "" if status == "OK" else (
                    "degenerate (fully clamped)" if not graded_ok else "CFL unstable")
                print(f"    floor={floor}: cfl_ceiling={cmax:.4f} "
                      f"({'stable' if cfl_ok else 'UNSTABLE'})  "
                      f"graded={'yes' if graded_ok else 'no'}  {status} {reason}".rstrip(),
                      flush=True)
                if status == "EXCLUDED":
                    excluded[r2].add((r1, floor))
                else:
                    assert cfl_ok, f"r2={r2} r1={r1} floor={floor} unstable (ceiling={cmax:.4f})"
    return excluded


def box_coords(r2):
    box_a_half, box_b_half = r2 + BOX_A_OFFSET, r2 + BOX_B_OFFSET
    for half, name in ((box_a_half, "box_a"), (box_b_half, "box_b")):
        margin_x = min(CX - half, N - ABSORB - (CX + half)) - ABSORB
        margin_y = min(CY - half, N - ABSORB - (CY + half)) - ABSORB
        assert margin_x >= MIN_MARGIN and margin_y >= MIN_MARGIN, \
            f"r2={r2} {name} clearance too tight (margin={min(margin_x, margin_y)})"
        assert half > r2, f"r2={r2} {name} does not clear the cloak"
    return (CX - box_a_half, CX + box_a_half, CY - box_a_half, CY + box_a_half), \
           (CX - box_b_half, CX + box_b_half, CY - box_b_half, CY + box_b_half)


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

    for r2 in R2_SWEEP:
        box_a, box_b = box_coords(r2)
        cap_e = run_scene(None)
        target = r2 - SHELL_TARGET

        for r1 in core_sweep(r2):
            shell = r2 - r1
            eps_z = (r2 / shell) ** 2
            for floor in FLOOR_SWEEP:
                if (r1, floor) in excluded[r2]:
                    print(f"  r2={r2:3d} r1={r1:2d} floor={floor:.2f}: SKIPPED (excluded)",
                          flush=True)
                    continue

                def build(sim, r1=r1, r2=r2, floor=floor):
                    materials.pec_disk(sim, CX, CY, r1)
                    materials.schurig_reduced_cloak_tm(sim, CX, CY, r1, r2,
                                                       mu_r_floor=floor)
                cap = run_scene(build)
                wa = sc.widths(cap, cap_e, box_a, (CX, CY, REF_HALF_H))
                wb = sc.widths(cap, cap_e, box_b, (CX, CY, REF_HALF_H))
                box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])
                cross_dev = abs(wa["sigma_ext"] - wa["sigma_ext_cross"]) / abs(wa["sigma_ext"])
                out = {k: wa[k] for k in ("sigma_scat", "sigma_abs", "sigma_ext",
                                           "sigma_ext_cross", "back_frac", "fwd_frac", "i_inc")}
                out["q_ext"] = wa["sigma_ext"] / (2.0 * r2)
                out["box_dev"] = box_dev
                out["cross_dev"] = cross_dev
                out["r2_cells"] = r2
                out["core_r1_cells"] = r1
                out["shell_cells"] = shell
                out["shell_lambda"] = shell / float(CPL)
                out["eps_z"] = eps_z
                out["mu_r_floor"] = floor
                out["is_target"] = (r1 == target)
                results[f"cloak-r2{r2}-core{r1}-floor{floor}"] = out
                tag = " <== 3.00 lambda TARGET" if r1 == target else ""
                print(f"  r2={r2:3d} r1={r1:2d} shell={shell}({shell / CPL:.2f}lam) "
                      f"eps_z={eps_z:.4f} floor={floor:.2f}: Q_ext={out['q_ext']:.4f}  "
                      f"boxdev={box_dev:.3f}  crossdev={cross_dev:.3f}{tag}", flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print(f"exp-022 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
