"""exp-025 -- resolution check on exp-024's chromatic finding (Red Team's
Phase-5 audit of Iteration 2, R3 meta-rule). Reruns empty/absorber/pec at
the FALLBACK_ANGLES (+-35deg, N=9) set, at 450 and 750 nm ONLY, at 1.5x
cpl with geometry rescaled to hold physical size fixed (this lab's
established precedent: exp-005/010/015/023). 600nm is the unmoved control
already on record (exp-024's results_fallback.json / results.json).

54 runs (2 lambda x 9 angles x 3 articles). Predictions committed in
NOTES.md BEFORE this file's first run (house discipline).
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
from lab import Sim, materials, ambient as amb, sections as sc

STEPS = 1400
ARTICLES = ("empty", "absorber", "pec")


def build(article, sim, geo):
    cx, cy = geo["OBJ"]
    r_out = geo["R_OUT"]
    if article == "empty":
        return
    if article == "absorber":
        core = int(round(30 * geo["ratio"]))     # exp-024's core radius, scaled
        materials.pec_disk(sim, cx, cy, core)
        materials.graded_black_shell(sim, cx, cy, core, r_out)
    elif article == "pec":
        materials.pec_disk(sim, cx, cy, r_out)


def one_run(article, theta, geo):
    sim = Sim(geo["NX"], geo["NY"], cells_per_lambda=geo["cpl_new"],
              courant_frac=0.99, absorb=geo["ABSORB"])
    build(article, sim, geo)
    sim.add_line_source(geo["SRC_X"], angle_deg=theta, edge=geo["TAPER"],
                         amplitude=1.0)
    sim.run(STEPS)
    return sc.full_capture(sim)


def run_group(args):
    lam_nm, theta, geo = args
    t0 = time.time()
    out = {}
    cap_e = one_run("empty", theta, geo)
    ph_e = sc.phasors(cap_e)
    prof_e = amb.observer_profile(ph_e, geo["PLANE_X"], geo["ABSORB"],
                                   geo["NY"] - geo["ABSORB"])
    out["empty"] = {"profile": prof_e.tolist()}
    for art in ARTICLES:
        if art == "empty":
            continue
        cap = one_run(art, theta, geo)
        ph = sc.phasors(cap)
        prof = amb.observer_profile(ph, geo["PLANE_X"], geo["ABSORB"],
                                     geo["NY"] - geo["ABSORB"])
        out[art] = {"profile": prof.tolist()}
    return (lam_nm, theta, out, time.time() - t0)


def main():
    geos = {lam_nm: dg.scaled_geometry(lam_nm) for lam_nm in dg.TARGETS}
    for lam_nm, geo in geos.items():
        ok, _ = dg.verify_coverage(geo)
        assert ok, f"coverage failed at {lam_nm}nm"

    groups = [(lam_nm, float(th), geos[lam_nm])
              for lam_nm in dg.TARGETS for th in dg.FALLBACK_ANGLES]
    print(f"exp-025: {len(groups)} groups ({len(groups) * 3} runs), "
          f"{os.cpu_count()} cpus")
    t0 = time.time()
    results = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for lam_nm, theta, out, dt in ex.map(run_group, groups):
            results[(lam_nm, theta)] = out
            print(f"  [{len(results):2d}/{len(groups)}] lambda={lam_nm} "
                  f"theta={theta:+05.1f} ({dt:5.1f} s)", flush=True)
    print(f"done in {time.time() - t0:.0f} s")

    def contrast(article, lam_nm, geo):
        profs, e_profs = [], []
        for th in dg.FALLBACK_ANGLES:
            grp = results[(lam_nm, float(th))]
            profs.append(np.array(grp[article]["profile"]))
            e_profs.append(np.array(grp["empty"]["profile"]))
        weights = [1.0] * len(dg.FALLBACK_ANGLES)
        y0 = geo["OBJ"][1]
        return amb.contrast_from_runs(profs, e_profs, weights, geo["ABSORB"],
                                       y0, geo["W_OBJ"], geo["GUARD_OUT"],
                                       geo["W_FLANK"])

    table, floors = {}, {}
    for lam_nm, geo in geos.items():
        for art in ARTICLES:
            r = contrast(art, lam_nm, geo)
            table[f"{art}/{lam_nm}"] = {"C": r["C"], "C_empty": r["C_empty"]}
            if art == "empty":
                floors[str(lam_nm)] = abs(r["C_empty"])

    out = {"cpl_new": {k: v["cpl_new"] for k, v in geos.items()},
           "ratio": {k: v["ratio"] for k, v in geos.items()},
           "elapsed_s": time.time() - t0, "contrasts": table,
           "decision_floors": floors}
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1)

    print("\ndecision floors (fine resolution):")
    for k, v in floors.items():
        print(f"  {k}nm: {v:.6f}")
    print("\nWeber contrast C (fine resolution):")
    for lam_nm in dg.TARGETS:
        for art in ARTICLES:
            print(f"  {art:9s} {lam_nm}nm  {table[f'{art}/{lam_nm}']['C']:+.4f}")

    # comparison vs exp-024's coarse fallback numbers (hardcoded from its
    # results_fallback.json -- avoids a cross-experiment import dependency)
    coarse = {"absorber/450": -0.7170, "absorber/750": -0.7284,
              "pec/450": -0.8605, "pec/750": -0.8771}
    print("\nfine vs coarse (exp-024 fallback):")
    for k, cv in coarse.items():
        art, lam = k.split("/")
        fv = table[f"{art}/{lam}"]["C"]
        print(f"  {k}: coarse {cv:+.4f} -> fine {fv:+.4f}  "
              f"(delta {fv - cv:+.4f})")
    d_coarse_abs = coarse["absorber/750"] - coarse["absorber/450"]
    d_fine_abs = table["absorber/750"]["C"] - table["absorber/450"]["C"]
    d_coarse_pec = coarse["pec/750"] - coarse["pec/450"]
    d_fine_pec = table["pec/750"]["C"] - table["pec/450"]["C"]
    print(f"\nchromatic spread |C(750)-C(450)|:")
    print(f"  absorber: coarse {d_coarse_abs:+.4f} -> fine {d_fine_abs:+.4f}")
    print(f"  pec:      coarse {d_coarse_pec:+.4f} -> fine {d_fine_pec:+.4f}")

    print("\nresults.json written")


if __name__ == "__main__":
    main()
