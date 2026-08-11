"""
exp-016 -- Mechanism candidate 1: outer-boundary impedance mismatch.
======================================================================
exp-014/015 confirmed a grid-independent trough in Q_ext(eps_z) near
eps_z~2.25-2.4 (core=30's floor=0.10->0.18 jump sign-flips; the other
core/eps_z points from exp-006/011/012/013 don't). Two mechanism
candidates were logged in exp-015's Next section. This file tests the
first: the shell's local impedance mismatch at the OUTER boundary r=r2,
already invoked (at a different location -- the floor/inner-wall clamp)
and refuted for magnitude trend in exp-006's P3.

No FDTD time-stepping needed -- this is a pure material-array probe:
build a bare Sim, call the production schurig_reduced_cloak_tm builder,
and read the actual inv_mu tensor the solver would use, at theta~0 near
r=r2. Near-zero compute (no run() calls at all).

    .venv\\Scripts\\python.exe experiments\\016-impedance-mismatch-mechanism\\run.py
"""

import json
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np

from lab import Sim, materials

HERE = os.path.dirname(os.path.abspath(__file__))

N = 300
CX = CY = 150
R2 = 90

# trough bracket (exp-014/015) + exp-006/011/012/013's corner points
CORE_POINTS = [15, 27, 28, 29, 30, 31, 32, 33, 40, 48]
PROBE_FLOORS = [0.10, 0.18, 0.40]   # 0.10/0.18 = the trough's own floor pair;
                                    # 0.40 = deliberately high, to expose clamping at r2


def mu_r_at_r2(r1, floor):
    """Read the production tensor array directly -- no re-derivation of the
    formula, so this can't diverge from what the solver actually uses."""
    sim = Sim(N, N, cells_per_lambda=20, courant_frac=0.32, absorb=10)
    materials.schurig_reduced_cloak_tm(sim, CX, CY, r1, R2, mu_r_floor=floor)
    xx = sim.inv_mu["xx"]              # hx grid: x-offset 0, y-offset 0.5 -> theta~0 at j=CY
    j = CY
    row = xx[:, j]
    xs = np.arange(N) - CX
    rr = np.hypot(xs, 0.5)
    mask = rr <= R2 + 1e-9
    idx = np.where(mask)[0]
    i_last = idx[np.argmax(rr[idx])]
    r_last = float(rr[i_last])
    mu_r_last = float(1.0 / row[i_last])
    return r_last, mu_r_last


def main():
    t0 = time.time()
    results = {}
    print(f"R2={R2} cells (fixed, matches exp-006+)", flush=True)
    for r1 in CORE_POINTS:
        eps_z = (R2 / (R2 - r1)) ** 2
        analytic_mu_r_r2 = ((R2 - r1) / R2) ** 2   # == 1/eps_z exactly
        row = {"r1": r1, "eps_z": eps_z, "analytic_mu_r_r2": analytic_mu_r_r2,
               "eta_shell_over_eta0": (1.0 / eps_z) ** 0.5, "probe": {}}
        for floor in PROBE_FLOORS:
            r_last, mu_r_last = mu_r_at_r2(r1, floor)
            clamped = abs(mu_r_last - floor) < 1e-6 and floor > analytic_mu_r_r2
            row["probe"][f"floor{floor}"] = {
                "r_last_cells": r_last, "mu_r_at_r2_numeric": mu_r_last,
                "clamped_at_r2": bool(clamped),
            }
        gamma = (row["eta_shell_over_eta0"] - 1.0) / (row["eta_shell_over_eta0"] + 1.0)
        row["gamma_power_reflection"] = gamma ** 2
        results[f"core{r1}"] = row
        p10 = row["probe"]["floor0.10"]["mu_r_at_r2_numeric"]
        p18 = row["probe"]["floor0.18"]["mu_r_at_r2_numeric"]
        p40 = row["probe"]["floor0.40"]["mu_r_at_r2_numeric"]
        print(f"  r1={r1:2d} eps_z={eps_z:.4f} analytic_mu_r(r2)={analytic_mu_r_r2:.4f} "
              f"numeric[0.10]={p10:.4f} numeric[0.18]={p18:.4f} numeric[0.40]={p40:.4f} "
              f"|Gamma|^2={row['gamma_power_reflection']:.5f}", flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print(f"exp-016 probe complete in {time.time() - t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
