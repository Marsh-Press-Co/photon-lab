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

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, HERE)

import design_geometry as dg
import run as R


def main():
    print("exp-065 -- settling convergence trend (C40, theta=40, 600nm)")
    print("committed reproduction of phase4_results.md Diagnostic 2")
    print("-" * 60)
    for steps in (1400, 2800, 4200, 5600):
        key, th, lam, s, prof, dt = R._settle_one(("C40", 40.0, 600, steps))
        c = R._c_empty(prof, dg.CONFIGS[key])
        print(f"  STEPS={steps:5d}  C_empty={c:+.6f}  ({dt:.1f}s)", flush=True)


if __name__ == "__main__":
    main()
