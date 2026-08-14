"""exp-030 -- The r=156/312 Near-Field->Witness-Scale Bridge (T8) + the
Box-Ledger Floor Companion (T11): measurement harness.
=======================================================================
Panel Iteration 7 (lead VISION SCIENCE; synthesis: Director, post Red
Team's proceed-with-mandatory-fixes -- see design_geometry.py's module
docstring and NOTES.md Phase 3 for the full accepted/overridden record).

Staged execution (cost-tiered, pre-authorized in the Phase-1 proposal and
kept in synthesis): run with `--stage NAME`. Stages, in commit order:

  rgate       -- flat-coating R re-check at each new sigma_max/thickness
                 (zero FDTD stepping through an object disk -- cheap wall
                 test, reused stage-7 idiom). No prior stage required.
  block1_156  -- 4 articles x 9 angles + empty x 9 @ r=156.        (45 runs)
  floor156    -- delta_C floor check @ r=156 (reuses block1_156's empty
                 captures -- zero marginal FDTD calls IF run in the same
                 process; else recomputed, still cheap vs the 45 above).
  settle156   -- doubled-STEPS settling diagnostic, absorber @ r=156.  (2 runs)
  t11         -- box_dev @ r=78 (1 run) + r=156 native+cpl*1.5 (4 runs). (5 runs)
  block1_312_pilot -- ONE timing pilot run @ r=312 before committing
                 to the full leg (empty, theta=0).                     (1 run)
  block1_312  -- PEC+absorber x 9 angles + off_lab+off_field x 5 angles
                 + empty x 9 (union of both angle sets) @ r=312.       (37 runs)
  fit         -- assemble results.json, fit C(z/zR)=C_inf+B*sqrt(z/zR),
                 score every P-VISION prediction. No FDTD.

Each stage appends to (does not overwrite) results.json.
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
LAM_NM, CPL = 600, 20   # single-lambda scope throughout, unchanged from proposal


def load_results():
    if os.path.exists(RESULTS_PATH):
        with open(RESULTS_PATH) as f:
            return json.load(f)
    return {"meta": {"experiment": "exp-030-scale-bridge"}}


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


def bare_wall_sanity_check(cpl=CPL):
    """Calibration-only check that this rig's flux-monitor methodology can
    reproduce stage7_absorber's own near-total-reflection reading for a
    bare PEC wall -- run ONCE, independent of r (sigma_max/thickness don't
    enter a bare-PEC test at all). Diagnostic note (found during Phase-4
    build, before any gate value was trusted): the SAME monitor-to-PEC
    standoff (70-100 cells, several wavelengths) that gives R_bare~0.98
    here collapses to R_bare~0.76-1.13 if the monitor sits close (<=30
    cells) OR far (>=118 cells) from the bare PEC face -- a real,
    unexplained sensitivity of this flux-monitor idiom to exact standoff
    distance for a hard reflector specifically (not reproduced for the
    graded coating, see R_coat below, which stays stable at every standoff
    tested). Recorded as an idealization/caveat, not chased further --
    R_bare is a sanity check, not a scored prediction; R_coat is the load-
    bearing gate and does not share this sensitivity."""
    src_x, mon_x, pec_x, nx = 60, 188, 258, 500

    def bare(sim):
        sim.pec[pec_x:pec_x + 16, :] = True

    f0 = _wall_flux(nx, src_x, mon_x, pec_x, None, cpl)
    fw = _wall_flux(nx, src_x, mon_x, pec_x, bare, cpl)
    return (f0 - fw) / f0


def coated_wall_r_gate(sigma_max, thickness_cells, cpl=CPL):
    """Fix 2 / Red Team #8: does the graded_black_shell profile stay a
    near-zero-reflectance broadband coating once sigma_max is rescaled and
    the taper is correspondingly longer (holding total optical depth
    const)? Reuses run_all.py::stage7_absorber's own flat-wall idiom (a
    graded coating in front of a PEC backing), generalized to a variable
    taper length. Monitor sits a fixed 90-cell standoff BEFORE the coating
    entry (not from the PEC backing, which is thickness_cells further
    back) -- calibrated directly (before freeze): unlike the bare-PEC
    case above, this reading is stable across a wide range of standoffs
    (60-120 cells tested, R_coat agreeing to within 5e-5 at every one),
    consistent with the coating absorbing the wave well before it reaches
    the PEC, leaving no significant standing-wave structure at the
    monitor to be standoff-sensitive to."""
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
    r_bare = bare_wall_sanity_check()
    print(f"  bare-wall sanity check (rig calibration, r-independent): "
          f"R_bare={r_bare:.4f}  (stage7's own established value: 0.988)")
    out = {"R_bare_sanity": r_bare}
    for r in dg.R_FAMILY:
        thickness = r - dg.r_in_shell(r)
        sm = dg.sigma_max_shell(r)
        t0 = time.time()
        r_coat = coated_wall_r_gate(sm, thickness)
        out[str(r)] = {"sigma_max": sm, "thickness_cells": thickness,
                        "R_coat": r_coat, "elapsed_s": time.time() - t0}
        print(f"  r={r:4d}  sigma_max={sm:.4f}  thickness={thickness:4d}  "
              f"R_coat={r_coat:.5f}  ({out[str(r)]['elapsed_s']:.1f}s)")
    res = load_results()
    res["rgate"] = out
    save_results(res)


# ---------------------------------------------------------- ambient stages
def build_ambient(article, sim, r, g):
    cx, cy = g["obj"]
    if article == "empty":
        return
    if article == "pec":
        mat.pec_disk(sim, cx, cy, r)
    elif article == "absorber":
        mat.graded_black_shell(sim, cx, cy, dg.r_in_shell(r), r,
                                sigma_max=dg.sigma_max_shell(r),
                                eps_max=dg.EPS_MAX)
    elif article in ("off_lab", "off_field"):
        sigma = dg.sigma_off_lab(r) if article == "off_lab" else dg.sigma_off_field(r)
        x = np.arange(sim.nx)[:, None]
        y = np.arange(sim.ny)[None, :]
        mask = (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2
        sim.sigma_e[mask] += sigma
        sim.objects.append({"type": "uniform_sponge_disk",
                             "params": {"cx": cx, "cy": cy, "r": r, "sigma": sigma}})


def one_ambient_run(article, theta, r, steps=None):
    g = dg.GEOM[r]
    sim = Sim(g["nx"], g["ny"], cells_per_lambda=CPL, courant_frac=dg.COURANT_FRAC,
              absorb=dg.ABSORB)
    build_ambient(article, sim, r, g)
    sim.add_line_source(g["src_x"], angle_deg=theta, edge=dg.TAPER, amplitude=1.0)
    sim.run(steps if steps is not None else g["steps_ambient"])
    return sc.full_capture(sim)


def _worker(args):
    article, theta, r, steps = args
    t0 = time.time()
    cap = one_ambient_run(article, theta, r, steps)
    ph = sc.phasors(cap)
    g = dg.GEOM[r]
    prof = amb.observer_profile(ph, g["plane_x"], dg.ABSORB, g["ny"] - dg.ABSORB)
    return (article, theta, prof.tolist(), time.time() - t0)


def run_block1(r, angle_articles, workers=4):
    """angle_articles: dict article -> tuple of angles to run (empty is
    auto-derived as the union of all article angle sets)."""
    all_angles = sorted(set().union(*angle_articles.values()))
    jobs = [("empty", th, r, None) for th in all_angles]
    for art, angles in angle_articles.items():
        jobs += [(art, th, r, None) for th in angles]
    print(f"  {len(jobs)} runs @ r={r} ({dg.GEOM[r]['nx']}x{dg.GEOM[r]['ny']}, "
          f"steps={dg.GEOM[r]['steps_ambient']})")
    t0 = time.time()
    out = {}
    with ProcessPoolExecutor(max_workers=workers) as ex:
        for article, theta, prof, dt in ex.map(_worker, jobs):
            out.setdefault(article, {})[str(theta)] = prof
            print(f"    {article:10s} theta={theta:+4.0f}  {dt:6.1f}s")
    print(f"  block1 r={r}: {len(jobs)} runs in {time.time()-t0:.1f}s total")
    return out, all_angles


def run_block1_156():
    angle_articles = {a: dg.FALLBACK_ANGLES for a in
                       ("pec", "absorber", "off_lab", "off_field")}
    out, angles = run_block1(156, angle_articles)
    res = load_results()
    res.setdefault("block1", {})["156"] = {"profiles": out, "angles": angles}
    save_results(res)


def run_block1_312_pilot():
    t0 = time.time()
    one_ambient_run("empty", 0.0, 312)
    dt = time.time() - t0
    print(f"  r=312 single run (empty, theta=0): {dt:.1f}s -> "
          f"est. full leg (37 runs, 4 workers): {dt*37/4/60:.1f} min")
    res = load_results()
    res["block1_312_pilot_s"] = dt
    save_results(res)
    return dt


def run_block1_312(workers=4):
    angle_articles = {"pec": dg.FALLBACK_ANGLES, "absorber": dg.FALLBACK_ANGLES,
                       "off_lab": dg.N5_SUBSAMPLE, "off_field": dg.N5_SUBSAMPLE}
    out, angles = run_block1(312, angle_articles, workers=workers)
    res = load_results()
    res.setdefault("block1", {})["312"] = {"profiles": out, "angles": angles}
    save_results(res)


# --------------------------------------------------------------- floor156
def run_floor156():
    """Red Team fix 5: delta_C empty-scene decision-floor check @ r=156,
    reusing block1_156's own empty captures (zero marginal FDTD calls)."""
    res = load_results()
    profiles = res["block1"]["156"]["profiles"]["empty"]
    g = dg.GEOM[156]
    weights = [1.0] * len(dg.FALLBACK_ANGLES)
    e_profiles = [np.array(profiles[str(th)]) for th in dg.FALLBACK_ANGLES]
    c = amb.contrast_from_runs(e_profiles, e_profiles, weights,
                                dg.ABSORB, g["obj"][1], g["w_obj"],
                                g["guard_out"], g["w_flank"])
    delta_c = c["C_empty"]
    res["floor156"] = {"delta_C": delta_c}
    save_results(res)
    print(f"  delta_C @ r=156 (empty-scene floor): {delta_c:+.5f}")
    return delta_c


# --------------------------------------------------------------- settle156
def run_settle156():
    """Red Team fix 9 (recommended): doubled-STEPS_AMBIENT settling
    diagnostic, absorber @ r=156, theta=0 only."""
    g = dg.GEOM[156]
    native = g["steps_ambient"]
    doubled = native * 2
    out = {}
    for label, steps in (("native", native), ("doubled", doubled)):
        t0 = time.time()
        cap_e = one_ambient_run("empty", 0.0, 156, steps)
        cap_a = one_ambient_run("absorber", 0.0, 156, steps)
        ph_e, ph_a = sc.phasors(cap_e), sc.phasors(cap_a)
        prof_e = amb.observer_profile(ph_e, g["plane_x"], dg.ABSORB, g["ny"] - dg.ABSORB)
        prof_a = amb.observer_profile(ph_a, g["plane_x"], dg.ABSORB, g["ny"] - dg.ABSORB)
        c = amb.contrast_from_runs([prof_a], [prof_e], [1.0], dg.ABSORB,
                                    g["obj"][1], g["w_obj"], g["guard_out"], g["w_flank"])
        out[label] = {"steps": steps, "C": c["C"], "elapsed_s": time.time() - t0}
        print(f"  settle156 {label} (steps={steps}): C={c['C']:+.5f}  "
              f"({out[label]['elapsed_s']:.1f}s)")
    res = load_results()
    res["settle156"] = out
    save_results(res)


# ------------------------------------------------------------------- T11
def run_t11():
    out = {}
    for r in dg.BEAM_R_FAMILY:
        g = dg.BEAM_GEOM[r]
        cpls = (CPL,) if r == 78 else (CPL, round(CPL * 1.5))
        for cpl in cpls:
            steps = round(g["steps"] * (cpl / CPL))
            t0 = time.time()
            sim_e = Sim(g["n"], g["n"], cells_per_lambda=cpl, courant_frac=0.32,
                        absorb=40)
            sim_e.add_line_source(g["src_x"])
            sim_e.run(steps)
            cap_e = sc.full_capture(sim_e)

            sim_on = Sim(g["n"], g["n"], cells_per_lambda=cpl, courant_frac=0.32, absorb=40)
            x = np.arange(sim_on.nx)[:, None]
            y = np.arange(sim_on.ny)[None, :]
            mask = (x - g["cx"]) ** 2 + (y - g["cy"]) ** 2 <= r ** 2
            sim_on.sigma_e[mask] += g["sigma_on"]
            sim_on.add_line_source(g["src_x"])
            sim_on.run(steps)
            cap_on = sc.full_capture(sim_on)

            wa = sc.widths(cap_on, cap_e, g["box_a"], g["ref"])
            wb = sc.widths(cap_on, cap_e, g["box_b"], g["ref"])
            bd = dg.box_dev(wa["sigma_ext"], wb["sigma_ext"])
            key = f"{r}_{cpl}"
            out[key] = {"r": r, "cpl": cpl, "steps": steps,
                        "sigma_ext_a": wa["sigma_ext"], "sigma_ext_b": wb["sigma_ext"],
                        "box_dev": bd, "elapsed_s": time.time() - t0}
            print(f"  T11 r={r:4d} cpl={cpl:2d}: box_dev={bd*100:.4f}%  "
                  f"({out[key]['elapsed_s']:.1f}s)")
    res = load_results()
    res["t11"] = out
    save_results(res)


# --------------------------------------------------------------------- fit
def assemble_contrasts(r):
    res = load_results()
    g = dg.GEOM[r]
    data = res["block1"][str(r)]["profiles"] if r != 78 else None
    contrasts = {}
    if r == 78:
        return dg.C78_ESTABLISHED
    angle_articles = {"pec": dg.FALLBACK_ANGLES, "absorber": dg.FALLBACK_ANGLES,
                       "off_lab": dg.N5_SUBSAMPLE if r == 312 else dg.FALLBACK_ANGLES,
                       "off_field": dg.N5_SUBSAMPLE if r == 312 else dg.FALLBACK_ANGLES}
    for art, angles in angle_articles.items():
        e_profiles = [np.array(data["empty"][str(th)]) for th in angles]
        s_profiles = [np.array(data[art][str(th)]) for th in angles]
        weights = [1.0] * len(angles)
        c = amb.contrast_from_runs(s_profiles, e_profiles, weights, dg.ABSORB,
                                    g["obj"][1], g["w_obj"], g["guard_out"], g["w_flank"])
        contrasts[art] = c["C"]
    return contrasts


def fit_sqrt_law(x156, c156, x312, c312):
    """Exact 2-point solve of C = C_inf + B*sqrt(x): x already = sqrt(z/zR)."""
    b = (c156 - c312) / (x156 - x312)
    c_inf = c156 - b * x156
    return c_inf, b


def run_fit():
    res = load_results()
    c78 = dg.C78_ESTABLISHED
    c156 = assemble_contrasts(156)
    c312 = assemble_contrasts(312)
    x78, x156, x312 = (dg.GEOM[r]["x_bridge"] for r in (78, 156, 312))
    x_wit = np.sqrt(dg.WITNESS_ZZR["central"])

    out = {}
    for art in ("absorber", "pec"):
        c_inf, b = fit_sqrt_law(x156, c156[art], x312, c312[art])
        c_pred_78 = c_inf + b * x78
        c_pred_wit = c_inf + b * x_wit
        miss = abs(c_pred_78 - c78[art])
        ratio_actual = (c78[art] - c156[art]) / (c156[art] - c312[art])
        out[art] = {"C78_established": c78[art], "C156": c156[art], "C312": c312[art],
                    "C_inf": c_inf, "B": b, "C_pred_78": c_pred_78,
                    "miss_vs_established": miss, "C_pred_witness": c_pred_wit,
                    "shape_ratio": ratio_actual}
    for art in ("off_lab", "off_field"):
        out[art] = {"C78_established": c78[art], "C156": c156[art], "C312": c312[art],
                    "delta_78_to_312": c312[art] - c78[art]}

    res["fit"] = out
    save_results(res)
    print(json.dumps(out, indent=2))
    return out


if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    dispatch = {
        "rgate": run_rgate,
        "block1_156": run_block1_156,
        "floor156": run_floor156,
        "settle156": run_settle156,
        "t11": run_t11,
        "block1_312_pilot": run_block1_312_pilot,
        "block1_312": run_block1_312,
        "fit": run_fit,
    }
    if stage not in dispatch:
        print(f"unknown stage {stage!r}; choices: {list(dispatch)}")
        sys.exit(1)
    print(f"=== exp-030 stage: {stage} ===")
    dispatch[stage]()
