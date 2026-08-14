"""exp-031 -- measurement harness. See design_geometry.py for the full
Phase-3 synthesis record and NOTES.md for predictions (committed before
this file was ever run).

Stages (append-only to results.json, run with --stage NAME):
  sweep    -- 6 new FDTD runs (empty/pec/absorber x r in {78,156}, theta=0),
              each full-domain-captured once, then re-sliced at every
              PLANE_DX in the r's own grid (post-processing, zero extra
              FDTD stepping). Absorber uses the CORRECTED PEC-cored
              construction (Fix 1).
  quantum  -- 9 new FDTD runs (sigma-held sponge, r=156, N=9 angles),
              reusing exp-030's own saved r=156 empty profiles.
  thermo   -- zero new FDTD (post-run analytic on the sweep stage's own
              r=156/PLANE_DX=15 absorber+pec captures).
  fit      -- assemble everything, run every P-PHOTONICS/P-QUANTUM/P-DIR
              prediction check. No FDTD.
"""

import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
EXP030 = os.path.abspath(os.path.join(HERE, "..", "030-scale-bridge"))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, EXP030)

import design_geometry as dg030   # exp-030's module, resolved via EXP030 on sys.path

import importlib.util
_spec = importlib.util.spec_from_file_location("dg031", os.path.join(HERE, "design_geometry.py"))
dg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dg)       # exp-031's own module, loaded by explicit path
                                    # (avoids the sys.modules name collision --
                                    # both files are named design_geometry.py)

from lab import Sim, materials as mat, ambient as amb, sections as sc

RESULTS_PATH = os.path.join(HERE, "results.json")
EXP030_RESULTS = os.path.join(EXP030, "results.json")


def load_results():
    if os.path.exists(RESULTS_PATH):
        with open(RESULTS_PATH) as f:
            return json.load(f)
    return {"meta": {"experiment": "exp-031-ripple-core-reconciliation"}}


def save_results(d):
    with open(RESULTS_PATH, "w") as f:
        json.dump(d, f, indent=2)


def load_exp030_results():
    with open(EXP030_RESULTS) as f:
        return json.load(f)


# --------------------------------------------------------------- builders
def build_scene(article, sim, r, g):
    cx, cy = g["obj"]
    if article == "empty":
        return
    if article == "pec":
        mat.pec_disk(sim, cx, cy, r)
        return
    if article == "absorber":
        # Fix 1 (Red Team #1, load-bearing): the historically-correct
        # PEC-cored construction, matching exp-001/020/024/025/027 --
        # NOT exp-030's own hollow-core convention.
        r_in = dg.r_in_shell(r)
        mat.pec_disk(sim, cx, cy, r_in)
        mat.graded_black_shell(sim, cx, cy, r_in, r,
                                sigma_max=dg.sigma_max_shell(r), eps_max=dg.EPS_MAX)
        return
    if article == "sigma_held":
        sigma = dg.SIGMA_HELD
        x = np.arange(sim.nx)[:, None]
        y = np.arange(sim.ny)[None, :]
        mask = (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2
        sim.sigma_e[mask] += sigma
        sim.objects.append({"type": "uniform_sponge_disk",
                             "params": {"cx": cx, "cy": cy, "r": r, "sigma": sigma}})
        return
    raise ValueError(article)


def one_run(article, theta, r):
    g = dg030.GEOM[r]
    sim = Sim(g["nx"], g["ny"], cells_per_lambda=dg.CPL, courant_frac=dg030.COURANT_FRAC,
              absorb=dg030.ABSORB)
    build_scene(article, sim, r, g)
    sim.add_line_source(g["src_x"], angle_deg=theta, edge=dg030.TAPER, amplitude=1.0)
    sim.run(g["steps_ambient"])
    return sc.full_capture(sim)


# ------------------------------------------------------------ sweep stage
def run_sweep():
    out = {}
    for r in dg.R_SWEEP:
        g = dg030.GEOM[r]
        out[str(r)] = {}
        for article in ("empty", "pec", "absorber"):
            t0 = time.time()
            cap = one_run(article, 0.0, r)
            elapsed = time.time() - t0
            ph = sc.phasors(cap)
            profiles = {}
            for dx in dg.PLANE_DX_GRID[r]:
                plane_x = dg.plane_x_at(r, dx)
                b = amb.observer_profile(ph, plane_x, dg030.ABSORB, g["ny"] - dg030.ABSORB)
                profiles[str(dx)] = b.tolist()
            out[str(r)][article] = {"elapsed_s": elapsed, "profiles": profiles}
            print(f"  r={r:4d} {article:9s} theta=0  {elapsed:6.1f}s  "
                  f"({len(dg.PLANE_DX_GRID[r])} PLANE_DX offsets extracted, zero extra FDTD)")
    res = load_results()
    res["sweep"] = out
    save_results(res)


# ---------------------------------------------------------- quantum stage
def run_quantum():
    r = dg.R_SIGMA_HELD
    g = dg030.GEOM[r]
    out = {"angles": {}}
    for theta in dg.FALLBACK_ANGLES:
        t0 = time.time()
        cap = one_run("sigma_held", float(theta), r)
        elapsed = time.time() - t0
        ph = sc.phasors(cap)
        b = amb.observer_profile(ph, g["plane_x"], dg030.ABSORB, g["ny"] - dg030.ABSORB)
        out["angles"][str(theta)] = {"profile": b.tolist(), "elapsed_s": elapsed}
        print(f"  sigma_held r={r} theta={theta:+4.0f}  {elapsed:6.1f}s")
    res = load_results()
    res["quantum"] = out
    save_results(res)


# ------------------------------------------------------------ thermo stage
def run_thermo():
    """Post-run ANALYTIC sidecar (Fix 5) -- zero new FDTD. Reuses the
    sweep stage's own r=156/PLANE_DX=15 (canonical anchor) full captures.
    Reports absorbed fraction of the object-footprint incident power via
    the established sections.widths() box-ledger idiom. The DeltaT/
    emission-band step stays blocked on docket #7's still-missing
    witness-scenario watts (Iteration 1's own recorded limit)."""
    r = 156
    g = dg030.GEOM[r]
    box = g["box"]
    cx, cy = g["obj"]
    ref = (cx, cy, r)

    def recap(article):
        return one_run(article, 0.0, r)

    print("  re-running r=156/theta=0 empty+pec+absorber for thermo sidecar "
        "(full captures aren't persisted between stages; cheap, same rate as sweep stage)")
    cap_empty = recap("empty")
    out = {}
    for article in ("pec", "absorber"):
        cap = recap(article)
        w = sc.widths(cap, cap_empty, box, ref)
        out[article] = w
        print(f"  thermo r=156 {article:9s}  sigma_abs={w['sigma_abs']:.3f}  "
              f"P_abs/P_inc(footprint)={w['sigma_abs']/(2*r):.5f}")
    res = load_results()
    res["thermo"] = out
    save_results(res)


if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 else "sweep"
    {"sweep": run_sweep, "quantum": run_quantum, "thermo": run_thermo}[stage]()
