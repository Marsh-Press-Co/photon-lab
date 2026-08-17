"""exp-041 -- Auditing the +-40deg Angle Pair as the N17 Correction
Standard (T20): measurement harness.
=============================================================================
Panel Iteration 18 (lead: QUANTUM OPTICS, rotation; synthesis: Director,
post Red Team's PROCEED-WITH-MANDATORY-FIXES verdict -- see
design_geometry.py module docstring and NOTES.md Phase 3 for the full
accepted/overridden record).

Three blocks (block-local scope, no shared harness beyond design_geometry.py):
  Block MAIN:       10 angles x 3 lambda = 30 calls (empty-scene-only)
  Block OBJPRESENT: 2 calls (sponge @ +-40deg, 600nm; reuses MAIN's own
                     empty(+-40,600nm) profiles for the contrast pairing)
  Block EXTEND:     6 calls (empty-scene-only, +-41/42/43deg, 600nm only)
  TOTAL: 38 new FDTD calls.

Predictions committed in NOTES.md BEFORE this file's first run (house
discipline, non-negotiable). No `lab/` change -- suite stays fast-stage
green (re-verified before results are read).
"""

import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from functools import partial

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, HERE)

import design_geometry as dg
from lab import Sim, ambient as amb, sections as sc


# ===================================================== generic FDTD call
def _one_run(cpl, theta, sigma=None):
    sim = Sim(dg.NX, dg.NY, cells_per_lambda=cpl, courant_frac=0.99, absorb=dg.ABSORB)
    if sigma is not None:
        cx, cy = dg.OBJ
        x = np.arange(sim.nx)[:, None]
        y = np.arange(sim.ny)[None, :]
        mask = (x - cx) ** 2 + (y - cy) ** 2 <= dg.R_OUT ** 2
        sim.sigma_e[mask] += sigma
        sim.objects.append({"type": "uniform_sponge_disk",
                            "params": {"cx": cx, "cy": cy, "r": dg.R_OUT, "sigma": sigma}})
    sim.add_line_source(dg.SRC_X, angle_deg=theta, edge=dg.TAPER, amplitude=1.0)
    sim.run(dg.STEPS)
    return sc.full_capture(sim)


def _profile(cap):
    ph = sc.phasors(cap)
    return amb.observer_profile(ph, dg.PLANE_X, dg.ABSORB, dg.NY - dg.ABSORB).tolist()


def _c_empty(profile):
    """Single-angle empty-scene Weber contrast: the per-(theta,lambda)
    diffraction/edge-leakage floor. Reuses amb.contrast_from_runs with a
    one-element angle list -- exp-035's own `_contrast(...,"empty",(theta,))`
    idiom, verbatim in structure. Weber-ratio-invariant to the empty run's
    own flank-normalization (algebraically identical to a direct
    window_means ratio; kept via contrast_from_runs for exact precedent
    consistency)."""
    r = amb.contrast_from_runs([np.array(profile)], [np.array(profile)], [1.0],
                                dg.ABSORB, dg.OBJ[1], dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)
    return r["C_empty"]


def _c_article(article_profile, empty_profile):
    r = amb.contrast_from_runs([np.array(article_profile)], [np.array(empty_profile)], [1.0],
                                dg.ABSORB, dg.OBJ[1], dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)
    return r["C"], r["C_empty"]


# ===================================================== Block MAIN
def _main_one(args):
    theta, lam, cpl = args
    t0 = time.time()
    cap = _one_run(cpl, theta, sigma=None)
    prof = _profile(cap)
    return (theta, lam, prof, time.time() - t0)


def block_main():
    jobs = [(theta, lam, cpl) for lam, cpl in dg.CPL.items() for theta in dg.MAIN_ANGLES]
    print(f"\n=== Block MAIN: {len(dg.MAIN_ANGLES)} angles x {len(dg.CPL)} lambda "
          f"= {len(jobs)} calls (empty-scene-only) ===", flush=True)
    t0 = time.time()
    profiles = {}   # (theta, lam) -> profile
    n_runs = 0
    with ProcessPoolExecutor(max_workers=4) as ex:
        for theta, lam, prof, dt in ex.map(_main_one, jobs):
            profiles[(theta, lam)] = prof
            n_runs += 1
            print(f"  [MAIN {n_runs:2d}/{len(jobs)}] theta={theta:+05.1f} lam={lam} ({dt:5.1f}s)", flush=True)
    elapsed = time.time() - t0
    assert n_runs == len(jobs), f"Block MAIN run-count mismatch: {n_runs} != {len(jobs)}"

    rows = []
    for lam in sorted(dg.CPL):
        for theta in dg.MAIN_ANGLES:
            c_emp = _c_empty(profiles[(theta, lam)])
            rows.append({
                "theta": theta, "lambda_nm": lam,
                "C_empty": c_emp, "abs_C_empty": abs(c_emp),
                "pass_gate_hard": abs(c_emp) <= dg.GATE_HARD,
                "pass_gate_perceptual_context": abs(c_emp) <= dg.GATE_PERCEPTUAL_CONTEXT,
                "pass_advisory_040": abs(c_emp) <= dg.ADVISORY_BOUND_040,
            })
    return {"n_new_runs": n_runs, "elapsed_s": elapsed, "rows": rows, "profiles": profiles}


# ===================================================== Block OBJPRESENT
def _objpresent_one(theta):
    t0 = time.time()
    cap = _one_run(dg.CPL[600], theta, sigma=dg.SIGMA_SPONGE)
    prof = _profile(cap)
    return (theta, prof, time.time() - t0)


def block_objpresent(main_profiles):
    print(f"\n=== Block OBJPRESENT: {len(dg.OBJPRESENT_ANGLES)} calls "
          f"(sponge @ 600nm, +-40deg; reuses MAIN's empty(+-40,600nm)) ===", flush=True)
    t0 = time.time()
    n_runs = 0
    rows = []
    with ProcessPoolExecutor(max_workers=2) as ex:
        for theta, prof, dt in ex.map(_objpresent_one, dg.OBJPRESENT_ANGLES):
            n_runs += 1
            empty_prof = main_profiles[(theta, 600)]
            c, c_emp_check = _c_article(prof, empty_prof)
            c_emp_main = _c_empty(empty_prof)
            rows.append({
                "theta": theta, "lambda_nm": 600,
                "C_sponge": c, "abs_C_sponge": abs(c),
                "C_empty_paired": c_emp_check,
                "C_empty_from_MAIN": c_emp_main,
                "self_consistency_delta": abs(c_emp_check - c_emp_main),
            })
            print(f"  [OBJPRESENT {n_runs}/{len(dg.OBJPRESENT_ANGLES)}] theta={theta:+05.1f} ({dt:5.1f}s)", flush=True)
    elapsed = time.time() - t0
    assert n_runs == len(dg.OBJPRESENT_ANGLES)
    return {"n_new_runs": n_runs, "elapsed_s": elapsed, "rows": rows}


# ===================================================== Block EXTEND
def _extend_one(theta):
    t0 = time.time()
    cap = _one_run(dg.CPL[600], theta, sigma=None)
    prof = _profile(cap)
    return (theta, prof, time.time() - t0)


def block_extend():
    print(f"\n=== Block EXTEND: {len(dg.EXTEND_ANGLES)} calls "
          f"(empty-scene-only, 600nm, 41-43deg both signs) ===", flush=True)
    t0 = time.time()
    n_runs = 0
    rows = []
    with ProcessPoolExecutor(max_workers=4) as ex:
        for theta, prof, dt in ex.map(_extend_one, dg.EXTEND_ANGLES):
            n_runs += 1
            c_emp = _c_empty(prof)
            rows.append({
                "theta": theta, "lambda_nm": 600,
                "C_empty": c_emp, "abs_C_empty": abs(c_emp),
                "pass_gate_hard": abs(c_emp) <= dg.GATE_HARD,
            })
            print(f"  [EXTEND {n_runs}/{len(dg.EXTEND_ANGLES)}] theta={theta:+05.1f} ({dt:5.1f}s)", flush=True)
    elapsed = time.time() - t0
    assert n_runs == len(dg.EXTEND_ANGLES)
    rows.sort(key=lambda r: r["theta"])
    return {"n_new_runs": n_runs, "elapsed_s": elapsed, "rows": rows}


# ===================================================== main
def main():
    t_start = time.time()
    res_main = block_main()
    res_obj = block_objpresent(res_main["profiles"])
    res_ext = block_extend()
    total_runs = res_main["n_new_runs"] + res_obj["n_new_runs"] + res_ext["n_new_runs"]
    total_elapsed = time.time() - t_start
    assert total_runs == 38, f"expected 38 new FDTD calls, got {total_runs}"

    # ---- MAIN summary: crossing-point read per lambda ---------------------
    print("\n=== MAIN: per-lambda gate crossing (GATE_HARD=0.001) ===")
    crossing = {}
    for lam in sorted(dg.CPL):
        lam_rows = sorted([r for r in res_main["rows"] if r["lambda_nm"] == lam],
                           key=lambda r: r["theta"])
        pos = [r for r in lam_rows if r["theta"] > 0]
        breach_thetas = [r["theta"] for r in pos if not r["pass_gate_hard"]]
        first_breach = min(breach_thetas) if breach_thetas else None
        crossing[lam] = first_breach
        print(f"  {lam}nm: first breach (positive side) at theta={first_breach}, "
              f"row abs|C_empty|: " +
              ", ".join(f"{r['theta']:+.0f}:{r['abs_C_empty']:.5f}" for r in pos))

    results = {
        "experiment": "exp-041-t20-angle-audit",
        "panel_iteration": 18,
        "lead_seat": "QUANTUM OPTICS",
        "director_synthesis": "PROCEED-WITH-MANDATORY-FIXES per Red Team Phase 2",
        "geometry": {k: getattr(dg, k) for k in
                     ("NX", "NY", "ABSORB", "SRC_X", "TAPER", "R_OUT", "PLANE_X",
                      "OBJ", "MARGIN_MULT", "SIGMA_SPONGE")},
        "gates": {"GATE_HARD": dg.GATE_HARD,
                  "GATE_PERCEPTUAL_CONTEXT": dg.GATE_PERCEPTUAL_CONTEXT,
                  "ADVISORY_BOUND_040": dg.ADVISORY_BOUND_040,
                  "STAGE9_EMPTY_GATE": dg.STAGE9_EMPTY_GATE},
        "steps": dg.STEPS,
        "block_main": {"n_new_runs": res_main["n_new_runs"], "elapsed_s": res_main["elapsed_s"],
                       "rows": res_main["rows"]},
        "block_objpresent": res_obj,
        "block_extend": res_ext,
        "first_breach_positive_side_by_lambda": crossing,
        "total_new_runs": total_runs,
        "total_elapsed_s": total_elapsed,
    }
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nTOTAL: {total_runs} new FDTD calls, {total_elapsed:.1f}s. "
          f"Written to {out_path}")


if __name__ == "__main__":
    main()
