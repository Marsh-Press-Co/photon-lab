"""exp-065 -- the STEPS convergence trend diagnostic, committed as real code
(PHOTONICS' Phase-5 catch: the 1400/2800/4200/5600 series in
`phase4_results.md`'s "Diagnostic 2" existed only as prose, an R4-class gap
-- every other figure in this experiment is produced by committed code;
this one wasn't). Run directly: `python3 settling_trend_diagnostic.py`.

Reproduces the C40/40deg/600nm four-point series exactly as reported:
  STEPS=1400  C_empty=-0.010965
  STEPS=2800  C_empty=-0.002802
  STEPS=4200  C_empty=-0.002801
  STEPS=5600  C_empty=-0.002802
"""

import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, HERE)

import design_geometry as dg
import run as R


def diagnostic_2():
    """Runs 4 new FDTD calls."""
    print("exp-065 -- settling convergence trend (C40, theta=40, 600nm)")
    print("committed reproduction of phase4_results.md Diagnostic 2")
    print("-" * 60)
    for steps in (1400, 2800, 4200, 5600):
        key, th, lam, s, prof, dt = R._settle_one(("C40", 40.0, 600, steps))
        c = R._c_empty(prof, dg.CONFIGS[key])
        print(f"  STEPS={steps:5d}  C_empty={c:+.6f}  ({dt:.1f}s)", flush=True)


def diagnostic_3():
    """PHASE-5 MANDATORY FIX, RECOMMENDED (Red Team's final audit, attack 4):
    Diagnostic 3's summary statistics (median/max/cross-channel ratio) were
    reconstructable from committed data but not themselves produced by any
    committed script -- the same R4-adjacent gap class as Diagnostic 2's
    points, closed the same way. Zero new FDTD calls -- reads the already-
    committed settled-sweep JSON and results.json directly."""
    print("\nexp-065 -- Diagnostic 3 summary statistics (settled STEPS=2800 sweep)")
    print("committed reproduction of phase4_results.md Diagnostic 3")
    print("-" * 60)
    settled = json.load(open(os.path.join(HERE, "settled_sweep_steps2800_diagnostic.json")))
    results = json.load(open(os.path.join(HERE, "results.json")))

    def get(k, th, lam):
        return settled[f"{k}|{th}|{lam}"]

    cells = [(th, lam) for lam in sorted(dg.CPL) for th in dg.SWEEP_ANGLES]
    d80 = [get("C80", th, lam) - get("C40", th, lam) for th, lam in cells]
    a80 = [abs(v) for v in d80]
    median, mx = float(np.median(a80)), float(max(a80))
    print(f"  settled median|Delta(C80-C40)| = {median:.6f}  "
          f"(unsettled was {results['scored']['P-VIS42-2']['median']:.6f})")
    print(f"  settled max   |Delta(C80-C40)| = {mx:.6f}  "
          f"(unsettled was {results['scored']['P-VIS42-2']['max']:.6f})")

    beam_median = results["scored"]["P-VIS42-9"]["median_beam"]
    ratio = median / beam_median
    print(f"  cross-channel ratio (settled plane / beam) = {ratio:.4f}  "
          f"(unsettled ratio was {results['scored']['P-VIS42-9']['ratio']:.4f})")


if __name__ == "__main__":
    diagnostic_2()
    diagnostic_3()
