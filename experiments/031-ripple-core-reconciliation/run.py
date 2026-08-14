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
    cx, cy = g["obj"]
    # NOTE (found during Phase-4 implementation, not assumed at Phase-1/3):
    # dg030.GEOM[r]['box'] is a computed-but-NEVER-ACTUALLY-USED field in
    # exp-030's own code (grepped -- zero references) -- clearance
    # round(12*kappa)=24 cells (~1.2 lambda at cpl=20) is too tight for a
    # closed-box Poynting ledger on this near-field-heavy geometry and
    # produced unphysical sigma_abs (large negative). Built fresh here at
    # clearance ~4 lambda (80 cells), matching this program's own
    # established beam-scene box-ledger convention order-of-magnitude
    # (BEAM_BOX_A0/B0, design_geometry.py L249-250, ~1.6 lambda at r=78
    # scaled) with extra margin since this is an untested configuration.
    clearance = 80
    box = (cx - r - clearance, cx + r + clearance,
           cy - r - clearance, cy + r + clearance)
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


# -------------------------------------------------------------- fit stage
def _C_at(res, r, article, dx):
    g = dg030.GEOM[r]
    y_lo = dg030.ABSORB
    b_scene = np.array(res["sweep"][str(r)][article]["profiles"][str(dx)])
    b_empty = np.array(res["sweep"][str(r)]["empty"]["profiles"][str(dx)])
    y0 = g["obj"][1]
    out = amb.contrast_from_runs([b_scene], [b_empty], [1.0], y_lo, y0,
                                  g["w_obj"], g["guard_out"], g["w_flank"])
    return out["C"]


def _count_significant_reversals(vals, floor):
    diffs = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
    signs = [(1 if d > 0 else -1) for d in diffs if abs(d) >= floor]
    return sum(1 for i in range(len(signs) - 1) if signs[i] != signs[i + 1]), diffs


def _fit_sqrt(c1, c2, x1, x2, x_t):
    B = (c1 - c2) / (x1 - x2)
    Cinf = c1 - B * x1
    return Cinf, B, Cinf + B * x_t


def _fit_ceiling(c1, c2, x1, x2, x_t):
    import math
    zzr1, zzr2 = x1 ** 2, x2 ** 2
    p = math.log((c1 + 1) / (c2 + 1)) / math.log(zzr1 / zzr2)
    B = (c1 + 1) / (zzr1 ** p)
    return B, p, -1 + B * (x_t ** 2) ** p


def run_fit():
    res = load_results()
    res030 = load_exp030_results()
    out = {}

    # --- T12 ripple detection, magnitude-floored, + safety diagnostic
    sweep = {}
    for r in dg.R_SWEEP:
        g = dg030.GEOM[r]
        y_lo, y0 = dg030.ABSORB, g["obj"][1]
        ref_dx = str(dg.ANCHOR_PLANE_DX)
        _, ref_flank = amb.window_means(
            np.array(res["sweep"][str(r)]["empty"]["profiles"][ref_dx]),
            y_lo, y0, g["w_obj"], g["guard_out"], g["w_flank"])
        flank_devs = {}
        for dx in dg.PLANE_DX_GRID[r]:
            _, fl = amb.window_means(
                np.array(res["sweep"][str(r)]["empty"]["profiles"][str(dx)]),
                y_lo, y0, g["w_obj"], g["guard_out"], g["w_flank"])
            flank_devs[str(dx)] = (fl - ref_flank) / ref_flank
        sweep[str(r)] = {"flank_dev": flank_devs, "any_excluded_gt5pct":
                          any(abs(v) > 0.05 for v in flank_devs.values())}
        for art in ("pec", "absorber"):
            vals = [_C_at(res, r, art, dx) for dx in dg.PLANE_DX_GRID[r]]
            revs, diffs = _count_significant_reversals(vals, dg.RIPPLE_NOISE_FLOOR)
            sweep[str(r)][art] = {"C_by_plane_dx":
                                   dict(zip((str(d) for d in dg.PLANE_DX_GRID[r]), vals)),
                                   "significant_reversals": revs,
                                   "max_abs_diff": max(abs(d) for d in diffs)}
    out["sweep_analysis"] = sweep

    # --- P-PHOTONICS-3: kappa^2-matched cross-check
    c78_15 = _C_at(res, 78, "pec", 15)
    c156_60 = _C_at(res, 156, "pec", 60)
    out["p_photonics_3"] = {"C_78_dx15": c78_15, "C_156_dx60": c156_60,
                             "abs_diff": abs(c78_15 - c156_60)}

    # --- P-DIR-1: core-correction delta
    c156_cored = _C_at(res, 156, "absorber", 15)
    c156_uncored_established = -0.83412   # exp-030's own theta=0 reading, Iter-8 Phase-1 Step 3
    out["p_dir_1_core_correction"] = {
        "C_156_absorber_cored": c156_cored,
        "C_156_absorber_uncored_established": c156_uncored_established,
        "abs_delta": abs(c156_cored - c156_uncored_established)}

    # --- P-DIR-2: dual-law theta=0 fit, PEC and absorber(cored)
    x78, x156 = dg030.GEOM[78]["x_bridge"], dg030.GEOM[156]["x_bridge"]
    x_witness = dg030.WITNESS_ZZR["central"] ** 0.5
    dual = {}
    for art in ("pec", "absorber"):
        c78 = _C_at(res, 78, art, 15)
        c156 = _C_at(res, 156, art, 15)
        cinf, b, c_sqrt = _fit_sqrt(c78, c156, x78, x156, x_witness)
        b_ceil, p_ceil, c_ceil = _fit_ceiling(c78, c156, x78, x156, x_witness)
        dual[art] = {"C78": c78, "C156": c156,
                     "sqrt_law": {"C_inf": cinf, "B": b, "C_pred_witness": c_sqrt},
                     "ceiling_law": {"p": p_ceil, "B": b_ceil, "C_pred_witness": c_ceil},
                     "law_disagreement": abs(c_sqrt - c_ceil)}
    out["p_dir_2_dual_law"] = dual

    # --- QUANTUM: sigma-held r=156, N=9 ambient sum, scored against ladder
    g156 = dg030.GEOM[156]
    angles = dg.FALLBACK_ANGLES
    scene_profiles = [np.array(res["quantum"]["angles"][str(a)]["profile"]) for a in angles]
    empty_profiles = [np.array(res030["block1"]["156"]["profiles"]["empty"][str(a)]) for a in angles]
    q = amb.contrast_from_runs(scene_profiles, empty_profiles, [1.0] * len(angles),
                                dg030.ABSORB, g156["obj"][1], g156["w_obj"],
                                g156["guard_out"], g156["w_flank"])
    C_q = q["C"]
    tau156 = dg.TAU_SIGMA_HELD_156
    g_raw = abs(C_q) / tau156
    g_floor_corrected = abs(C_q - q["C_empty"]) / tau156
    g78 = abs(res030["fit"]["off_lab"]["C78_established"]) / 0.008
    g312 = abs(res030["fit"]["off_field"]["C312"]) / 0.032
    ladder = "PASS" if abs(C_q) < 0.005 else ("MARGINAL" if abs(C_q) <= 0.02 else "FAIL")
    out["quantum_sigma_held"] = {
        "C_156": C_q, "C_empty_156_this_run": q["C_empty"],
        "tau_156": tau156, "g_raw": g_raw, "g_floor_corrected": g_floor_corrected,
        "g_78_established": g78, "g_312_established": g312,
        "ladder_verdict": ladder}

    res["fit"] = out
    save_results(res)
    print(json.dumps(out, indent=2, default=str))


if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 else "sweep"
    {"sweep": run_sweep, "quantum": run_quantum, "thermo": run_thermo,
     "fit": run_fit}[stage]()
