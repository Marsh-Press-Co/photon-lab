"""exp-052 -- measurement harness. See design_geometry.py for the full
Phase-3 synthesis record (accepted mandatory-fix docket) and NOTES.md for
predictions, committed before this file was ever run.

Stages (append-only to results.json, run with --stage NAME):
  rgate        -- flat-coating R re-check for the fixed-absolute shell's
                   own profile (sigma_max=0.5, thickness=48 cells) --
                   r-independent (same profile at every r_out), one check.
  block_156    -- empty (N9) + absorber_fixedabs (N9, PEC-cored) +
                   absorber_selfsim (N9, PEC-cored comparator) +
                   absorber_fixedabs_hollow (theta=0 only, core-fill
                   check) @ r=156.                              (28 runs)
  block_312_pilot -- ONE timing pilot run @ r=312 (empty, theta=0) before
                   committing to the full leg.
  block_312    -- same structure as block_156, @ r=312.          (28 runs)
  fit          -- assemble results.json, score every P-* prediction.
                   No FDTD.
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
from lab import Sim, materials as mat, ambient as amb, sections as sc

RESULTS_PATH = os.path.join(HERE, "results.json")
LAM_NM, CPL = dg.LAM_NM, dg.CPL


def load_results():
    if os.path.exists(RESULTS_PATH):
        with open(RESULTS_PATH) as f:
            return json.load(f)
    return {"meta": {"experiment": "exp-052-fixed-absolute-thickness-shell"}}


def save_results(d):
    with open(RESULTS_PATH, "w") as f:
        json.dump(d, f, indent=2)


# ------------------------------------------------------------- rgate stage
def _wall_flux(nx, src_x, mon_x, pec_x, build, cpl, courant=0.99, absorb=36):
    sim = Sim(nx, 240, cells_per_lambda=cpl, courant_frac=courant, absorb=absorb)
    if build:
        build(sim)
    sim.add_line_source(src_x)
    start_step = int(3.0 * (pec_x - src_x + pec_x - mon_x))
    steps = start_step + 20 * cpl
    mon = sim.add_poynting_line(mon_x, start_step=start_step)
    sim.run(steps)
    return mon.mean_flux()


def coated_wall_r_gate(sigma_max, thickness_cells, cpl=CPL):
    """Identical idiom to exp-030's own gate (reimplemented, not imported,
    to keep exp-052 self-contained) -- flat-wall reflectance for the
    fixed-absolute shell's own (sigma_max, thickness) pair. r-independent
    by construction (both are held fixed across the whole family), so ONE
    check covers r=156 and r=312 alike."""
    from lab.materials import _graded_black
    src_x, runway = 60, 150
    entry = src_x + runway
    pec_x = entry + thickness_cells
    mon_x = entry - 90
    nx = pec_x + 16 + 70

    def coated(sim):
        sim.pec[pec_x:pec_x + 16, :] = True
        d = (np.arange(entry, pec_x) - entry) / float(thickness_cells)
        _, sig = _graded_black(d)
        sim.sigma_e[entry:pec_x, :] = (sigma_max / 0.5) * sig[:, None]

    f0 = _wall_flux(nx, src_x, mon_x, pec_x, None, cpl)
    fc = _wall_flux(nx, src_x, mon_x, pec_x, coated, cpl)
    return (f0 - fc) / f0


def run_rgate():
    t0 = time.time()
    r_coat = coated_wall_r_gate(dg.SIGMA_MAX_FIXED, dg.ABS_THICKNESS)
    elapsed = time.time() - t0
    print(f"  fixed-absolute shell R-gate: sigma_max={dg.SIGMA_MAX_FIXED}  "
          f"thickness={dg.ABS_THICKNESS}  R_coat={r_coat:.5f}  ({elapsed:.1f}s)")
    print("  [disclosure, Fix 9] a clean pass bears on flat-wall normal-incidence "
          "reflectance ONLY -- no inference about core-fill/comparator questions.")
    res = load_results()
    res["rgate"] = {"sigma_max": dg.SIGMA_MAX_FIXED, "thickness_cells": dg.ABS_THICKNESS,
                     "R_coat": r_coat, "elapsed_s": elapsed}
    save_results(res)
    return r_coat


# ---------------------------------------------------------- ambient stages
def build_ambient(article, sim, r, g):
    cx, cy = g["obj"]
    if article == "empty":
        return
    if article == "absorber_fixedabs":
        # Fix 1: PEC-cored, not hollow.
        r_in = dg.r_in_fixedabs(r)
        mat.pec_disk(sim, cx, cy, r_in)
        mat.graded_black_shell(sim, cx, cy, r_in, r,
                                sigma_max=dg.sigma_max_fixedabs(r), eps_max=dg.EPS_MAX)
    elif article == "absorber_selfsim":
        # Fix 2: self-similar comparator, ALSO PEC-cored (re-measured, not inherited).
        r_in = dg.r_in_selfsim(r)
        mat.pec_disk(sim, cx, cy, r_in)
        mat.graded_black_shell(sim, cx, cy, r_in, r,
                                sigma_max=dg.sigma_max_selfsim(r), eps_max=dg.EPS_MAX)
    elif article == "absorber_fixedabs_hollow":
        # Fix 3 (Director's redesign, see NOTES.md): core-fill check, using
        # the SAME validated N9 ambient instrument at theta=0 rather than
        # the box/ref channel exp-031 found broken for this scene class
        # (NotImplementedError guard, experiments/031/run.py::run_thermo).
        # No PEC core -- vacuum interior, everything else identical.
        r_in = dg.r_in_fixedabs(r)
        mat.graded_black_shell(sim, cx, cy, r_in, r,
                                sigma_max=dg.sigma_max_fixedabs(r), eps_max=dg.EPS_MAX)
    else:
        raise ValueError(article)


def one_ambient_run(article, theta, r):
    g = dg.GEOM[r]
    sim = Sim(g["nx"], g["ny"], cells_per_lambda=CPL, courant_frac=dg.COURANT_FRAC,
              absorb=dg.ABSORB)
    build_ambient(article, sim, r, g)
    sim.add_line_source(g["src_x"], angle_deg=theta, edge=dg.TAPER, amplitude=1.0)
    sim.run(g["steps_ambient"])
    return sc.full_capture(sim)


def _worker(args):
    article, theta, r = args
    t0 = time.time()
    cap = one_ambient_run(article, theta, r)
    ph = sc.phasors(cap)
    g = dg.GEOM[r]
    prof = amb.observer_profile(ph, g["plane_x"], dg.ABSORB, g["ny"] - dg.ABSORB)
    return (article, theta, prof.tolist(), time.time() - t0)


def run_block(r, workers=4):
    angle_articles = {"absorber_fixedabs": dg.FALLBACK_ANGLES,
                       "absorber_selfsim": dg.FALLBACK_ANGLES,
                       "absorber_fixedabs_hollow": (0.0,)}
    all_angles = sorted(set().union(*[set(v) for v in angle_articles.values()]))
    jobs = [("empty", th, r) for th in all_angles]
    for art, angles in angle_articles.items():
        jobs += [(art, th, r) for th in angles]
    print(f"  {len(jobs)} runs @ r={r} ({dg.GEOM[r]['nx']}x{dg.GEOM[r]['ny']}, "
          f"steps={dg.GEOM[r]['steps_ambient']})")
    t0 = time.time()
    out = {}
    with ProcessPoolExecutor(max_workers=workers) as ex:
        for article, theta, prof, dt in ex.map(_worker, jobs):
            out.setdefault(article, {})[str(theta)] = prof
            print(f"    {article:26s} theta={theta:+4.0f}  {dt:6.1f}s")
    print(f"  block r={r}: {len(jobs)} runs in {time.time()-t0:.1f}s total")
    res = load_results()
    res.setdefault("block", {})[str(r)] = {"profiles": out, "angles": all_angles}
    save_results(res)
    return out


def run_block_156():
    run_block(156)


def run_block_312_pilot():
    t0 = time.time()
    one_ambient_run("empty", 0.0, 312)
    dt = time.time() - t0
    est_min = dt * 28 / 4 / 60
    print(f"  r=312 single run (empty, theta=0): {dt:.1f}s -> "
          f"est. full leg (28 runs, 4 workers): {est_min:.1f} min")
    res = load_results()
    res["block_312_pilot_s"] = dt
    res["block_312_pilot_est_min"] = est_min
    save_results(res)
    return dt


def run_block_312():
    run_block(312)


# --------------------------------------------------------------------- fit
def _C_full(res, r, article):
    g = dg.GEOM[r]
    data = res["block"][str(r)]["profiles"]
    angles = dg.FALLBACK_ANGLES
    e_profiles = [np.array(data["empty"][str(th)]) for th in angles]
    s_profiles = [np.array(data[article][str(th)]) for th in angles]
    weights = [1.0] * len(angles)
    c = amb.contrast_from_runs(s_profiles, e_profiles, weights, dg.ABSORB,
                                g["obj"][1], g["w_obj"], g["guard_out"], g["w_flank"])
    return c["C"], c["C_empty"]


def _C_theta0(res, r, article):
    g = dg.GEOM[r]
    data = res["block"][str(r)]["profiles"]
    b_scene = np.array(data[article]["0.0"])
    b_empty = np.array(data["empty"]["0.0"])
    c = amb.contrast_from_runs([b_scene], [b_empty], [1.0], dg.ABSORB,
                                g["obj"][1], g["w_obj"], g["guard_out"], g["w_flank"])
    return c["C"]


def run_fit():
    res = load_results()
    out = {}
    for r in (156, 312):
        if "block" not in res or str(r) not in res.get("block", {}):
            continue
        c_fixedabs, c_empty = _C_full(res, r, "absorber_fixedabs")
        c_selfsim, _ = _C_full(res, r, "absorber_selfsim")
        c_fixedabs_t0 = _C_theta0(res, r, "absorber_fixedabs")
        c_hollow_t0 = _C_theta0(res, r, "absorber_fixedabs_hollow")
        out[str(r)] = {
            "C_fixedabs": c_fixedabs,
            "C_selfsim": c_selfsim,
            "C_empty": c_empty,
            "C_fixedabs_theta0": c_fixedabs_t0,
            "C_fixedabs_hollow_theta0": c_hollow_t0,
            "core_fill_delta_theta0": c_hollow_t0 - c_fixedabs_t0,
        }
    out["C78_established"] = dg.C78_ABSORBER_ESTABLISHED

    # P-1/P-2 verdicts, computed in code (house discipline, not hand-asserted)
    if "156" in out:
        c156 = out["156"]["C_fixedabs"]
        cself156 = out["156"]["C_selfsim"]
        out["P1_verdict"] = ("CONFIRMED" if c156 <= -0.7350 else
                              "PARTIAL" if c156 <= -0.7305 else "REFUTED")
        out["P1_c_fixedabs_156"] = c156
        out["P1_c_selfsim_156_corrected"] = cself156
        out["P1_deepening_vs_c78"] = out["C78_established"] - c156
    if "312" in out:
        c156 = out["156"]["C_fixedabs"]
        c312 = out["312"]["C_fixedabs"]
        band = dg.P2_R312_BAND
        out["P2_verdict"] = "CONFIRMED" if (c156 - c312) >= band else \
                             ("REFUTED" if c312 >= c156 else "PARTIAL")
        out["P2_c_fixedabs_312"] = c312
        out["P2_delta_156_to_312"] = c156 - c312

    res["fit"] = out
    save_results(res)
    print(json.dumps(out, indent=2))
    return out


if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    dispatch = {
        "rgate": run_rgate,
        "block_156": run_block_156,
        "block_312_pilot": run_block_312_pilot,
        "block_312": run_block_312,
        "fit": run_fit,
    }
    if stage not in dispatch:
        print(f"unknown stage {stage!r}; choices: {list(dispatch)}")
        sys.exit(1)
    print(f"=== exp-052 stage: {stage} ===")
    dispatch[stage]()
