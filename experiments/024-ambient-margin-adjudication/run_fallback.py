"""exp-024 fallback rerun -- triggered per P-M1's pre-committed falsification
clause (NOTES.md): the primary delta_C gate (<=0.001 at every lambda) MISSED
at all six (lambda, weighting) combinations (450/600/750 x equal/cos), a
real surprising instrument finding, not a bookkeeping miss. Per the
pre-registered response ("no further same-shift patch is attempted; the
pre-committed +-35deg fallback reruns instead"), this script runs the
FALLBACK_ANGLES set (9 angles, +-35deg span) fresh at all 3 lambda, self-
contained (results.json only persists assembled contrasts, not raw B(y)
profiles, so a genuinely new angle subset needs its own runs regardless of
overlap with the primary set) -- 27 groups x 4 articles = 108 runs.
"""

import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, HERE)

import design_geometry as dg
from lab import ambient as amb
import run as R   # reuse run_group, ARTICLES, LAMBDAS, DELTA_C_GATE


def main():
    groups = [(lam_nm, cpl, float(th), list(R.ARTICLES))
              for lam_nm, cpl in R.LAMBDAS for th in dg.FALLBACK_ANGLES]

    print(f"exp-024 fallback: {len(groups)} groups "
          f"({len(groups) * 4} runs), theta in {dg.FALLBACK_ANGLES}")
    t0 = time.time()
    results = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for lam_nm, theta, out, dt in ex.map(R.run_group, groups):
            results[(lam_nm, theta)] = out
            print(f"  [{len(results):3d}/{len(groups)}] lambda={lam_nm} "
                  f"theta={theta:+05.1f} ({dt:5.1f} s)", flush=True)
    print(f"done in {time.time() - t0:.0f} s")

    def contrast(article, lam_nm, angles, weights, plane=15):
        profs, e_profs = [], []
        for th in angles:
            grp = results[(lam_nm, float(th))]
            profs.append(np.array(grp[article]["profiles"][plane]))
            e_profs.append(np.array(grp["empty"]["profiles"][plane]))
        return amb.contrast_from_runs(
            profs, e_profs, weights, dg.ABSORB, dg.OBJ[1],
            dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)

    def wts(name, angles):
        return ([1.0] * len(angles) if name == "equal"
                else [float(np.cos(np.radians(t))) for t in angles])

    fb_table, fb_floors = {}, {}
    for art in R.ARTICLES:
        for lam_nm, _ in R.LAMBDAS:
            for wname in ("equal", "cos"):
                r = contrast(art, lam_nm, dg.FALLBACK_ANGLES,
                             wts(wname, dg.FALLBACK_ANGLES))
                fb_table[f"{art}/{lam_nm}/{wname}"] = {
                    "C": r["C"], "C_empty": r["C_empty"]}
                if art == "empty":
                    fb_floors[f"{lam_nm}/{wname}"] = abs(r["C_empty"])

    out = {"fallback_angles": list(dg.FALLBACK_ANGLES), "elapsed_s": time.time() - t0,
           "contrasts": fb_table, "decision_floors": fb_floors,
           "delta_c_pass": {k: v <= R.DELTA_C_GATE for k, v in fb_floors.items()}}
    with open(os.path.join(HERE, "results_fallback.json"), "w") as f:
        json.dump(out, f, indent=1)

    print("\nfallback (+-35deg, N=9) decision floors (gate <= "
          f"{R.DELTA_C_GATE}):")
    for k, v in fb_floors.items():
        print(f"  {k}: {v:.6f}  {'PASS' if v <= R.DELTA_C_GATE else 'FAIL'}")
    print("\nfallback Weber contrast C (equal weights):")
    for art in R.ARTICLES:
        row = "  ".join(f"{lam}nm {fb_table[f'{art}/{lam}/equal']['C']:+.4f}"
                        for lam, _ in R.LAMBDAS)
        print(f"  {art:9s} {row}")
    print("\nresults_fallback.json written")


if __name__ == "__main__":
    main()
