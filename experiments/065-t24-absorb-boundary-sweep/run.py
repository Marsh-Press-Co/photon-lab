"""exp-065 -- The T24 `ABSORB` Boundary Sweep, on the Channel That Scores
Constraint 3: measurement harness.
=============================================================================
Panel Iteration 42 (lead: VISION SCIENCE, rotation; synthesis: Director,
post Red Team's PROCEED-WITH-MANDATORY-FIXES verdict -- see
`phase3_synthesis.md` for the full accepted/overridden record and the
11-item mandatory-fix docket, all applied, zero overrides).

Six blocks:
  Block SWEEP:   6 angles x 3 lambda, at C40/C60/C70/C80/N60  = 90 calls
  Block PAD:     G40 at 3 angles x 3 lambda                   =  9 calls
  Block ARTICLE: N9 FALLBACK @600nm, article + 7 new empty,
                 at C40 and C80                               = 32 calls
  Block BEAM:    T24's own 2 cells, at C40/C60/N60            =  6 calls
  Block MINI:    dense 0.5deg scan @600nm (38.5/39/39.5 new,
                 38/40 reused from SWEEP), at C40 and C80     =  6 calls
  Block SETTLE:  STEPS=2800 at C80/40deg/600nm                =  1 call
  TOTAL: 144 new FDTD calls.

Predictions (P-VIS42-1, -1b, -2, -2a, -3, -4, -5, -6, -7, -8, -9, -10, -11)
committed in NOTES.md BEFORE this file's first run (house discipline,
non-negotiable), and printed structurally below before the first FDTD call
(exp-046's own structural-freeze precedent). No `lab/` change -- asserted in
code before any result is read.
"""

import json
import math
import os
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, HERE)

import design_geometry as dg
from lab import Sim, ambient as amb, sections as sc

HARD_STOP_S = 90 * 60          # pre-registered wall-clock hard stop
C_COEF = 2.0 * math.sqrt(2.0 * math.log(2.0)) / (2.0 * math.pi)   # exp-046 verbatim


# ================================================== structural freeze print
FROZEN_PREDICTIONS = """
P-VIS42-1   anchor identity: 12 C40 rows reproduce exp-041 block_main exactly
            CONFIRM dC == 0.0 (float64) for all 12 | REFUTE any nonzero
P-VIS42-1b  static construction identity (REPLACES the voided causal gate)
            CONFIRM max_diff == 0.0 AND all_vacuum | REFUTE any nonzero
P-VIS42-2   HEADLINE dC_empty(C80-C40) over 24 SWEEP cells
            CONFIRM median <= 1.0e-3 AND max <= 3.0e-3  (relative transfer)
            REFUTE  median >= 2.0e-3 OR  max >= 7.0e-3  (absolute transfer)
P-VIS42-2a  aliasing discriminator: C70 (3.5 lambda) vs C60/C80 interpolant
            CONFIRM within +-40% at all 6 cells | REFUTE >2x at >=3 of 6
P-VIS42-3   Spearman rho(|dC_empty(C80-C40)|, |C_empty(C40)|)
            CONFIRM rho >= +0.50 | REFUTE rho <= 0.0
P-VIS42-4   naive protocol dominates: |dC(N60-C40)| vs |dC(C60-C40)|
            CONFIRM N60 exceeds at >=13/18 AND median in [1e-3, 2e-2]
            REFUTE  <=9/18 OR median outside [3e-4, 4e-2]
P-VIS42-5   pad-only null: |C_empty(G40)-C_empty(C40)| over 9 cells
            CONFIRM all 9 <= 5e-4 | REFUTE any cell >= 2e-3
P-VIS42-6   scored N9 floor @600nm: |C_empty,N9| at C40 and C80
            CONFIRM both <= GATE_HARD=1e-3 AND |delta| <= 5e-4
            REFUTE  either breaches GATE_HARD OR |delta| > 1e-3
P-VIS42-7   constraint-scored article row (tau=0.0065), N9/600nm, C40 vs C80
            CONFIRM |dC| <= 1.0e-3 AND identical PASS/MARGINAL/FAIL bucket
            REFUTE  bucket differs OR |dC| > 2.5e-3
P-VIS42-8   T24 beam provenance: C(A-v4,40)=+0.154376, C(A-v1,40)=-0.125698
            CONFIRM both to <=1% rel AND dC(40->60) within +-25% of
                    +0.00696 / -0.00220
            REFUTE  outside either (R4-class finding: rt_absorb.py was never
                    committed)
P-VIS42-9   cross-channel transfer ratio (plane median / beam median)
            CONFIRM in [0.02, 0.30] | REFUTE >= 0.6 or <= 0.005
P-VIS42-10  falsifies 'cancels to first order': dC_empty(theta) over
            {38,38.5,39,39.5,40} @600nm, >=1 full T21 period P(40)=1.989deg
            CONFIRM within +-30% of its own mean (flat, additive)
            REFUTE  peak-to-trough >2x mean at a period matching P(theta)
                    within 20% (coherent-fringe perturbation)
P-VIS42-11  settling: |C_empty(C80,2800) - C_empty(C80,1400)| @40deg/600nm
            CONFIRM <= 0.15% relative | REFUTE > 1% relative
"""


def assert_lab_clean():
    """No `lab/` diff -- the whole 'no new machinery' position rests on it."""
    out = subprocess.run(["git", "diff", "--stat", "--", "lab/"],
                         cwd=os.path.abspath(os.path.join(HERE, "..", "..")),
                         capture_output=True, text=True).stdout.strip()
    assert out == "", f"lab/ is dirty -- the no-new-machinery position fails:\n{out}"
    return "clean"


# ===================================================== generic FDTD call
def _one_run(cfg, cpl, theta, sigma=None, steps=None, gauss_width=None):
    """One CW leg at configuration `cfg`. Source span is passed EXPLICITLY
    for every non-naive config (the fix T24's own design note demanded); the
    naive config deliberately lets `add_line_source` use its own
    [absorb, ny-absorb] default, which is what drags A 752 -> 732."""
    sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=cpl,
              courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
    if sigma is not None:
        cx, cy = cfg["obj_x"], cfg["obj_y"]
        x = np.arange(sim.nx)[:, None]
        y = np.arange(sim.ny)[None, :]
        mask = (x - cx) ** 2 + (y - cy) ** 2 <= dg.R_OUT ** 2
        sim.sigma_e[mask] += sigma
        sim.objects.append({"type": "uniform_sponge_disk",
                            "params": {"cx": cx, "cy": cy, "r": dg.R_OUT,
                                       "sigma": sigma}})
    kw = dict(angle_deg=theta, amplitude=1.0)
    if gauss_width is not None:
        kw.update(profile="gauss", width=gauss_width)
    else:
        kw.update(profile="plane", edge=dg.TAPER)
    if cfg["naive"]:
        sim.add_line_source(cfg["src_x"], **kw)          # default span (the point)
    else:
        sim.add_line_source(cfg["src_x"], y_lo=cfg["y_lo"], y_hi=cfg["y_hi"], **kw)
    sim.run(dg.STEPS if steps is None else steps)
    return sc.full_capture(sim)


def _profile(cap, cfg):
    ph = sc.phasors(cap)
    return amb.observer_profile(ph, cfg["plane_x"], cfg["y_lo"],
                                cfg["y_hi"]).tolist()


def _c_empty(profile, cfg):
    """Single-angle empty-scene Weber contrast -- exp-041's own `_c_empty`
    idiom verbatim in structure, with the configuration's own y_lo/obj_y
    (which is exactly what the congruent construction holds fixed in
    RELATIVE terms across the series)."""
    p = np.array(profile)
    r = amb.contrast_from_runs([p], [p], [1.0], cfg["y_lo"], cfg["obj_y"],
                               dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)
    return r["C_empty"]


def _c_article(article_profile, empty_profile, cfg):
    r = amb.contrast_from_runs([np.array(article_profile)],
                               [np.array(empty_profile)], [1.0],
                               cfg["y_lo"], cfg["obj_y"], dg.W_OBJ,
                               dg.GUARD_OUT, dg.W_FLANK)
    return r["C"], r["C_empty"]


def _c_n9(article_profiles, empty_profiles, cfg):
    """The aggregate N9 incoherent-sum reading (the scored currency for
    P-VIS42-6/7). Equal weights, `lab.ambient`'s own pipeline unmodified."""
    w = [1.0] * len(empty_profiles)
    r = amb.contrast_from_runs([np.array(p) for p in article_profiles],
                               [np.array(p) for p in empty_profiles], w,
                               cfg["y_lo"], cfg["obj_y"], dg.W_OBJ,
                               dg.GUARD_OUT, dg.W_FLANK)
    return r["C"], r["C_empty"]


# ===================================================== worker entry points
def _sweep_one(args):
    key, theta, lam = args
    cfg = dg.CONFIGS[key]
    t0 = time.time()
    cap = _one_run(cfg, dg.CPL[lam], theta)
    return (key, theta, lam, _profile(cap, cfg), time.time() - t0)


def _article_one(args):
    key, theta, sigma = args
    cfg = dg.CONFIGS[key]
    t0 = time.time()
    cap = _one_run(cfg, dg.CPL[600], theta, sigma=sigma)
    return (key, theta, sigma is not None, _profile(cap, cfg), time.time() - t0)


def _beam_one(args):
    key, cell, lam, theta0, fwhm = args
    cfg = dg.CONFIGS[key]
    lam_cells = dg.CPL[lam]
    width = (C_COEF * lam_cells / math.radians(fwhm)) / math.cos(math.radians(theta0))
    t0 = time.time()
    cap = _one_run(cfg, lam_cells, theta0, gauss_width=width)
    return (key, cell, lam, theta0, _profile(cap, cfg), width, time.time() - t0)


def _settle_one(args):
    key, theta, lam, steps = args
    cfg = dg.CONFIGS[key]
    t0 = time.time()
    cap = _one_run(cfg, dg.CPL[lam], theta, steps=steps)
    return (key, theta, lam, steps, _profile(cap, cfg), time.time() - t0)


# ===================================================== Block SWEEP
def block_sweep():
    keys = ("C40", "C60", "C70", "C80", "N60")
    jobs = [(k, th, lam) for k in keys for lam in sorted(dg.CPL)
            for th in dg.SWEEP_ANGLES]
    print(f"\n=== Block SWEEP: {len(keys)} configs x {len(dg.SWEEP_ANGLES)} "
          f"angles x {len(dg.CPL)} lambda = {len(jobs)} calls ===", flush=True)
    t0 = time.time()
    profiles, n = {}, 0
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, lam, prof, dt in ex.map(_sweep_one, jobs):
            profiles[(key, th, lam)] = prof
            n += 1
            print(f"  [SWEEP {n:3d}/{len(jobs)}] {key} theta={th:+05.1f} "
                  f"lam={lam} ({dt:5.1f}s)", flush=True)
    assert n == len(jobs), f"SWEEP run-count mismatch: {n} != {len(jobs)}"
    rows = []
    for key in keys:
        cfg = dg.CONFIGS[key]
        for lam in sorted(dg.CPL):
            for th in dg.SWEEP_ANGLES:
                c = _c_empty(profiles[(key, th, lam)], cfg)
                rows.append({"config": key, "absorb": cfg["absorb"],
                             "theta": th, "lambda_nm": lam, "C_empty": c,
                             "abs_C_empty": abs(c),
                             "pass_gate_hard": abs(c) <= dg.GATE_HARD})
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "rows": rows,
            "profiles": profiles}


# ===================================================== Block PAD
def block_pad():
    angles = (-35.0, 35.0, 40.0)
    jobs = [("G40", th, lam) for lam in sorted(dg.CPL) for th in angles]
    print(f"\n=== Block PAD: G40 at {len(angles)} angles x {len(dg.CPL)} "
          f"lambda = {len(jobs)} calls ===", flush=True)
    t0 = time.time()
    profiles, n = {}, 0
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, lam, prof, dt in ex.map(_sweep_one, jobs):
            profiles[(key, th, lam)] = prof
            n += 1
            print(f"  [PAD {n:2d}/{len(jobs)}] theta={th:+05.1f} lam={lam} "
                  f"({dt:5.1f}s)", flush=True)
    assert n == len(jobs), f"PAD run-count mismatch: {n} != {len(jobs)}"
    cfg = dg.CONFIGS["G40"]
    rows = [{"config": "G40", "theta": th, "lambda_nm": lam,
             "C_empty": _c_empty(profiles[("G40", th, lam)], cfg)}
            for lam in sorted(dg.CPL) for th in angles]
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "rows": rows,
            "profiles": profiles, "angles": angles}


# ===================================================== Block ARTICLE
def block_article(sweep_profiles):
    """N9 FALLBACK @600nm at C40 and C80: 9 article legs + the empty legs.
    +-35 @600nm empties already exist in Block SWEEP -> reused, not re-run
    (7 new empty angles per config)."""
    keys = ("C40", "C80")
    existing = {35.0, -35.0}
    new_empty = [th for th in dg.FALLBACK_ANGLES if float(th) not in existing]
    jobs = ([(k, float(th), dg.SIGMA_OFF_PASS) for k in keys
             for th in dg.FALLBACK_ANGLES]
            + [(k, float(th), None) for k in keys for th in new_empty])
    print(f"\n=== Block ARTICLE: N9 @600nm, article + {len(new_empty)} new "
          f"empty, at {keys} = {len(jobs)} calls ===", flush=True)
    t0 = time.time()
    art, emp, n = {}, {}, 0
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, is_art, prof, dt in ex.map(_article_one, jobs):
            (art if is_art else emp)[(key, th)] = prof
            n += 1
            print(f"  [ARTICLE {n:2d}/{len(jobs)}] {key} theta={th:+05.1f} "
                  f"{'article' if is_art else 'empty  '} ({dt:5.1f}s)", flush=True)
    assert n == len(jobs), f"ARTICLE run-count mismatch: {n} != {len(jobs)}"
    for k in keys:                       # fold in the reused SWEEP empties
        for th in (35.0, -35.0):
            emp[(k, th)] = sweep_profiles[(k, th, 600)]
    out = {}
    for k in keys:
        cfg = dg.CONFIGS[k]
        order = [float(t) for t in dg.FALLBACK_ANGLES]
        c, c_emp = _c_n9([art[(k, t)] for t in order],
                         [emp[(k, t)] for t in order], cfg)
        out[k] = {"C": c, "C_empty": c_emp, "abs_C": abs(c)}
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "per_config": out,
            "n9_angles": [float(t) for t in dg.FALLBACK_ANGLES]}


# ===================================================== Block BEAM
def block_beam():
    """T24's own two published cells, reproduced from committed code for the
    first time (`rt_absorb.py` was never committed -- P-VIS42-8)."""
    jobs = []
    for cell, v in dg.T24_BEAM.items():
        for key in ("C40", "C60", "N60"):
            jobs.append((key, cell, v["lambda_nm"], v["theta0_deg"], v["fwhm_deg"]))
    print(f"\n=== Block BEAM: {len(dg.T24_BEAM)} T24 cells x 3 configs "
          f"= {len(jobs)} calls ===", flush=True)
    t0 = time.time()
    profiles, widths, n = {}, {}, 0
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, cell, lam, th0, prof, width, dt in ex.map(_beam_one, jobs):
            profiles[(key, cell)] = prof
            widths[(key, cell)] = width
            n += 1
            print(f"  [BEAM {n}/{len(jobs)}] {key} {cell} lam={lam} "
                  f"theta0={th0} w={width:.2f} ({dt:5.1f}s)", flush=True)
    assert n == len(jobs), f"BEAM run-count mismatch: {n} != {len(jobs)}"
    rows = []
    for cell, v in dg.T24_BEAM.items():
        r = {"cell": cell, "lambda_nm": v["lambda_nm"],
             "theta0_deg": v["theta0_deg"], "fwhm_deg": v["fwhm_deg"],
             "published_C_absorb40": v["fdtd_C_absorb40"],
             "published_C_absorb60": v["fdtd_C_absorb60"],
             "published_delta": v["delta"]}
        for key in ("C40", "C60", "N60"):
            r[f"C_{key}"] = _c_empty(profiles[(key, cell)], dg.CONFIGS[key])
            r[f"width_{key}"] = widths[(key, cell)]
        r["delta_congruent_C60_C40"] = r["C_C60"] - r["C_C40"]
        r["delta_naive_N60_C40"] = r["C_N60"] - r["C_C40"]
        rows.append(r)
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "rows": rows}


# ===================================================== Block MINI
def block_mini(sweep_profiles):
    """Dense 0.5deg angular scan @600nm over >=1 full T21 fringe period --
    P-VIS42-10, the direct falsifier for the 'matched-angle differencing
    cancels the quadrature phase error to first order' premise (Red Team
    attack 5 / QUANTUM's catch). 38 and 40 are reused from Block SWEEP."""
    keys = ("C40", "C80")
    new = [a for a in dg.MINI_SWEEP_ANGLES if a not in dg.SWEEP_ANGLES]
    jobs = [(k, a, 600) for k in keys for a in new]
    print(f"\n=== Block MINI: {len(new)} new angles x {len(keys)} configs "
          f"= {len(jobs)} calls (38/40 reused from SWEEP) ===", flush=True)
    t0 = time.time()
    profiles, n = {}, 0
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, lam, prof, dt in ex.map(_sweep_one, jobs):
            profiles[(key, th)] = prof
            n += 1
            print(f"  [MINI {n}/{len(jobs)}] {key} theta={th:+05.2f} "
                  f"({dt:5.1f}s)", flush=True)
    assert n == len(jobs), f"MINI run-count mismatch: {n} != {len(jobs)}"
    for k in keys:                       # fold in the reused SWEEP angles
        for a in dg.MINI_SWEEP_ANGLES:
            if a in dg.SWEEP_ANGLES:
                profiles[(k, a)] = sweep_profiles[(k, a, 600)]
    rows = []
    for a in dg.MINI_SWEEP_ANGLES:
        c40 = _c_empty(profiles[("C40", a)], dg.CONFIGS["C40"])
        c80 = _c_empty(profiles[("C80", a)], dg.CONFIGS["C80"])
        rows.append({"theta": a, "C_empty_C40": c40, "C_empty_C80": c80,
                     "delta": c80 - c40,
                     "reused_from_sweep": a in dg.SWEEP_ANGLES})
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "rows": rows}


# ===================================================== Block SETTLE
def block_settle(sweep_profiles):
    """One STEPS=2800 leg at the largest padded domain -- P-VIS42-11, closing
    the settling-time/domain-size confound (Red Team attack 7, T10's own
    precedent). The STEPS=1400 comparator is reused from Block SWEEP."""
    key, th, lam = "C80", 40.0, 600
    print(f"\n=== Block SETTLE: {key} theta={th} lam={lam} "
          f"STEPS={dg.STEPS_SETTLE} = 1 call ===", flush=True)
    t0 = time.time()
    _, _, _, _, prof, dt = _settle_one((key, th, lam, dg.STEPS_SETTLE))
    print(f"  [SETTLE 1/1] ({dt:5.1f}s)", flush=True)
    cfg = dg.CONFIGS[key]
    c_long = _c_empty(prof, cfg)
    c_base = _c_empty(sweep_profiles[(key, th, lam)], cfg)
    return {"n_new_runs": 1, "elapsed_s": time.time() - t0,
            "config": key, "theta": th, "lambda_nm": lam,
            "steps_base": dg.STEPS, "steps_long": dg.STEPS_SETTLE,
            "C_empty_1400": c_base, "C_empty_2800": c_long,
            "abs_delta": abs(c_long - c_base),
            "rel_delta": abs(c_long - c_base) / abs(c_base)}


# ===================================================== gates
def gate_g1_anchor(sweep_rows):
    """P-VIS42-1: 12 C40 rows must reproduce exp-041's committed block_main
    EXACTLY. Values loaded programmatically -- never re-typed (R4)."""
    ref_path = os.path.join(HERE, "..", "041-t20-angle-audit", "results.json")
    ref = json.load(open(os.path.abspath(ref_path)))["block_main"]["rows"]
    ref_map = {(r["theta"], r["lambda_nm"]): r["C_empty"] for r in ref}
    checks = []
    for row in sweep_rows:
        if row["config"] != "C40":
            continue
        k = (row["theta"], row["lambda_nm"])
        if k not in ref_map:
            continue                       # +-35 has no exp-041 anchor (fix 10)
        d = row["C_empty"] - ref_map[k]
        checks.append({"theta": k[0], "lambda_nm": k[1], "ours": row["C_empty"],
                       "exp041": ref_map[k], "delta": d, "exact": d == 0.0})
    return {"n_checked": len(checks), "all_exact": all(c["exact"] for c in checks),
            "max_abs_delta": max((abs(c["delta"]) for c in checks), default=None),
            "checks": checks,
            "note": ("+-35 legs have NO exp-041 anchor at this geometry "
                     "(Phase-3 fix 10, disclosed idealization 11)")}


def gate_g2_static():
    """P-VIS42-1b: the static construction identity that REPLACED the voided
    dynamic causal gate (Phase-3 fix 2 -- see phase3_synthesis.md)."""
    r = dg.static_construction_identity(dg.CONFIGS["C40"], dg.CONFIGS["G40"],
                                        pad=40)
    r["pass"] = (r["max_diff"] == 0.0) and r["all_vacuum"]
    return r


# ===================================================== scoring
def _spearman(a, b):
    def rank(v):
        order = np.argsort(np.argsort(np.asarray(v, dtype=float)))
        return order.astype(float)
    ra, rb = rank(a), rank(b)
    return float(np.corrcoef(ra, rb)[0, 1])


def score(sweep, pad, article, beam, mini, settle, g1, g2):
    rows = sweep["rows"]

    def cell(key, th, lam):
        for r in rows:
            if r["config"] == key and r["theta"] == th and r["lambda_nm"] == lam:
                return r["C_empty"]
        raise KeyError((key, th, lam))

    cells = [(th, lam) for lam in sorted(dg.CPL) for th in dg.SWEEP_ANGLES]

    # ---- P-VIS42-2 (headline) + P-VIS42-3
    d80 = [cell("C80", th, lam) - cell("C40", th, lam) for th, lam in cells]
    d60 = [cell("C60", th, lam) - cell("C40", th, lam) for th, lam in cells]
    d70 = [cell("C70", th, lam) - cell("C40", th, lam) for th, lam in cells]
    dn60 = [cell("N60", th, lam) - cell("C40", th, lam) for th, lam in cells]
    a80 = [abs(v) for v in d80]
    base = [abs(cell("C40", th, lam)) for th, lam in cells]
    p2 = {"n_cells_C80": len(a80), "median": float(np.median(a80)),
          "max": float(max(a80)),
          "confirm": float(np.median(a80)) <= 1.0e-3 and float(max(a80)) <= 3.0e-3,
          "refute": float(np.median(a80)) >= 2.0e-3 or float(max(a80)) >= 7.0e-3}
    p2["verdict"] = ("CONFIRMED (relative transfer)" if p2["confirm"]
                     else "REFUTED (absolute transfer)" if p2["refute"]
                     else "PARTIAL (between bands)")
    p3 = {"rho": _spearman(a80, base)}
    p3["verdict"] = ("CONFIRMED (scales with reading -> relative)"
                     if p3["rho"] >= 0.50 else
                     "REFUTED (additive, reading-independent)"
                     if p3["rho"] <= 0.0 else "PARTIAL")

    # ---- P-VIS42-2a: aliasing discriminator at 600nm
    sub = [(th, 600) for th in dg.SWEEP_ANGLES]
    a2a = []
    for th, lam in sub:
        i = cells.index((th, lam))
        interp = 0.5 * (d60[i] + d80[i])          # C70 sits midway 60<->80
        dev = (abs(d70[i] - interp) / abs(interp)) if interp != 0 else float("inf")
        in_bracket = min(d60[i], d80[i]) <= d70[i] <= max(d60[i], d80[i])
        a2a.append({"theta": th, "d_C60": d60[i], "d_C70": d70[i],
                    "d_C80": d80[i], "interp": interp, "rel_dev": dev,
                    "within_40pct": dev <= 0.40, "in_bracket": in_bracket})
    n_bad = sum(1 for r in a2a if r["rel_dev"] > 2.0)
    p2a = {"cells": a2a, "n_all_within_40pct": sum(1 for r in a2a if r["within_40pct"]),
           "n_departing_2x": n_bad,
           "n_out_of_bracket": sum(1 for r in a2a if not r["in_bracket"])}
    p2a["confirm"] = all(r["within_40pct"] for r in a2a)
    p2a["refute"] = n_bad >= 3 or p2a["n_out_of_bracket"] == len(a2a)
    p2a["verdict"] = ("CONFIRMED (smooth, non-aliased)" if p2a["confirm"]
                      else "REFUTED (aliasing real -- headline is bounded)"
                      if p2a["refute"] else "PARTIAL")

    # ---- P-VIS42-4: naive dominates
    n_exceed = sum(1 for i in range(len(cells)) if abs(dn60[i]) > abs(d60[i]))
    med_n60 = float(np.median([abs(v) for v in dn60]))
    p4 = {"n_exceed": n_exceed, "n_cells": len(cells), "median_abs": med_n60,
          "confirm": n_exceed >= 13 and 1e-3 <= med_n60 <= 2e-2,
          "refute": n_exceed <= 9 or not (3e-4 <= med_n60 <= 4e-2)}
    p4["verdict"] = ("CONFIRMED" if p4["confirm"] else
                     "REFUTED" if p4["refute"] else "PARTIAL")

    # ---- P-VIS42-5: pad-only null
    pad_dev = []
    for r in pad["rows"]:
        c40 = cell("C40", r["theta"], r["lambda_nm"])
        pad_dev.append({"theta": r["theta"], "lambda_nm": r["lambda_nm"],
                        "abs_dev": abs(r["C_empty"] - c40)})
    p5 = {"cells": pad_dev, "max": max(d["abs_dev"] for d in pad_dev),
          "confirm": all(d["abs_dev"] <= 5e-4 for d in pad_dev),
          "refute": any(d["abs_dev"] >= 2e-3 for d in pad_dev)}
    p5["verdict"] = ("CONFIRMED (pad-only null)" if p5["confirm"] else
                     "REFUTED (instrument is padding-sensitive)"
                     if p5["refute"] else "PARTIAL")

    # ---- P-VIS42-6 / -7: the scored N9 rows
    a = article["per_config"]
    p6 = {"C_empty_C40": a["C40"]["C_empty"], "C_empty_C80": a["C80"]["C_empty"],
          "delta": a["C80"]["C_empty"] - a["C40"]["C_empty"]}
    p6["confirm"] = (abs(p6["C_empty_C40"]) <= dg.GATE_HARD
                     and abs(p6["C_empty_C80"]) <= dg.GATE_HARD
                     and abs(p6["delta"]) <= 5e-4)
    p6["refute"] = (abs(p6["C_empty_C40"]) > dg.GATE_HARD
                    or abs(p6["C_empty_C80"]) > dg.GATE_HARD
                    or abs(p6["delta"]) > 1e-3)
    p6["verdict"] = ("CONFIRMED" if p6["confirm"] else
                     "REFUTED" if p6["refute"] else "PARTIAL")

    def bucket(c):
        m = abs(c) / dg.C_THR_LAB
        return ("PASS" if m < dg.MARGINAL_LO else
                "MARGINAL" if m <= dg.MARGINAL_HI else "FAIL")

    p7 = {"C_C40": a["C40"]["C"], "C_C80": a["C80"]["C"],
          "delta": a["C80"]["C"] - a["C40"]["C"],
          "bucket_C40": bucket(a["C40"]["C"]), "bucket_C80": bucket(a["C80"]["C"]),
          "descriptive_central_estimate": dg.ARTICLE_CENTRAL_ESTIMATE,
          "caveats": [dg.REALIZABILITY_MEMO_CAVEAT, dg.G_TRANSFER_T15_CAVEAT,
                      dg.T5_THERMAL_CAVEAT],
          "tier_label": ("BENCH-SCALE SURROGATE ONLY -- no Tier-W/Tier-A "
                         "verdict is issued by this cycle, pending the "
                         "T8/T13/T14 witness-scale bridge (exp-047 "
                         "TIER_W_HEADLINE_LABEL discipline)")}
    p7["confirm"] = (abs(p7["delta"]) <= 1.0e-3
                     and p7["bucket_C40"] == p7["bucket_C80"])
    p7["refute"] = (p7["bucket_C40"] != p7["bucket_C80"]
                    or abs(p7["delta"]) > 2.5e-3)
    p7["verdict"] = ("CONFIRMED" if p7["confirm"] else
                     "REFUTED" if p7["refute"] else "PARTIAL")

    # ---- P-VIS42-8: T24 provenance
    p8rows = []
    for r in beam["rows"]:
        rel40 = abs(r["C_C40"] - r["published_C_absorb40"]) / abs(r["published_C_absorb40"])
        dpub = r["published_delta"]
        rel_d = abs(r["delta_congruent_C60_C40"] - dpub) / abs(dpub)
        p8rows.append({"cell": r["cell"], "ours_C40": r["C_C40"],
                       "published_C40": r["published_C_absorb40"],
                       "rel_dev_C40": rel40,
                       "ours_delta_congruent": r["delta_congruent_C60_C40"],
                       "ours_delta_naive": r["delta_naive_N60_C40"],
                       "published_delta": dpub, "rel_dev_delta": rel_d,
                       "within_1pct": rel40 <= 0.01, "within_25pct": rel_d <= 0.25})
    p8 = {"rows": p8rows,
          "confirm": all(r["within_1pct"] and r["within_25pct"] for r in p8rows),
          "refute": not all(r["within_1pct"] and r["within_25pct"] for r in p8rows)}
    p8["verdict"] = ("CONFIRMED (T24's figures reproduce from committed code)"
                     if p8["confirm"] else
                     "REFUTED (R4-class: published figures do not reproduce)")

    # ---- P-VIS42-9: cross-channel transfer
    med_plane = float(np.median([abs(v) for v in d60]))
    med_beam = float(np.median([abs(r["delta_congruent_C60_C40"])
                                for r in beam["rows"]]))
    ratio = med_plane / med_beam if med_beam else float("inf")
    p9 = {"median_plane": med_plane, "median_beam": med_beam, "ratio": ratio,
          "confirm": 0.02 <= ratio <= 0.30,
          "refute": ratio >= 0.6 or ratio <= 0.005}
    p9["verdict"] = ("CONFIRMED" if p9["confirm"] else
                     "REFUTED" if p9["refute"] else "PARTIAL")

    # ---- P-VIS42-10: the 'cancels to first order' falsifier
    #
    # PHASE-5 MANDATORY FIX (Red Team's final audit, attack 2 / QUANTUM's own
    # Phase-5 self-catch): the pre-registered REFUTE condition in NOTES.md/
    # phase3_synthesis.md is CONJUNCTIVE -- amplitude (ptp/mean>2x) AND a
    # period matching P(theta)=lambda/(A*cos theta) within 20%. The code
    # below previously computed and checked ONLY the amplitude clause, then
    # shipped a verdict string asserting "coherent-fringe perturbation" as an
    # established causal mechanism the second clause was supposed to test
    # for. Red Team's audit confirmed this live and required a fix before
    # close. Remedy taken (of the two Red Team offered): RELABEL, not force
    # a period-match fit -- MINI_SWEEP_ANGLES has only 5 points spanning
    # ~1.0 T21 period (2.0deg span vs P(40)=1.989deg); a period fit from 5
    # samples over one cycle cannot reliably distinguish "genuine coherent
    # oscillation at THIS period" from "five points that happen to differ"
    # (Nyquist-adjacent, same class of aliasing risk this cycle's own
    # ABSORB=70 fix was built to avoid). Fabricating a period-match verdict
    # from underpowered data would repeat, not fix, the defect. QUANTUM's own
    # Phase-5 alternative reading is independently plausible and unrefuted:
    # the settling artifact at one cell (0.0082 absolute) is comparable to
    # or larger than the measured peak-to-trough (0.00817), so an
    # UNSETTLED-TRANSIT reading is at least as consistent with these data as
    # a coherent-fringe one. The honest verdict is "large, oscillating,
    # mechanism undetermined, confounded by the settling defect" -- stated
    # as such, not as a specific mechanism this cycle did not establish.
    deltas = [r["delta"] for r in mini["rows"]]
    mean_d = float(np.mean(deltas))
    ptp = float(max(deltas) - min(deltas))
    within = [abs(d - mean_d) <= 0.30 * abs(mean_d) for d in deltas] if mean_d else []
    amplitude_refute = (ptp / abs(mean_d) > 2.0) if mean_d else False
    p10 = {"rows": mini["rows"], "mean_delta": mean_d, "peak_to_trough": ptp,
           "ptp_over_mean": ptp / abs(mean_d) if mean_d else float("inf"),
           "t21_period_deg": 1.989, "span_deg": max(dg.MINI_SWEEP_ANGLES)
                                                 - min(dg.MINI_SWEEP_ANGLES),
           "period_match_tested": False,
           "period_match_note": (
               "NOT TESTED -- 5 points over ~1.0 T21 period is insufficient "
               "to fit periodicity distinctly from noise/settling. The "
               "pre-registered REFUTE clause is conjunctive (amplitude AND "
               "period match); only the amplitude clause is evaluated. "
               "The verdict below is therefore deliberately NOT phrased as "
               "a mechanism claim -- see phase5_redteam_audit.md attack 2."),
           "confirm": bool(within) and all(within),
           "amplitude_clause_only_refute": amplitude_refute,
           "refute": False}   # the full conjunctive REFUTE is UNDECIDABLE, not False -- see verdict string
    if p10["confirm"]:
        p10["verdict"] = "CONFIRMED (flat -- additive-systematic framing holds)"
    elif amplitude_refute:
        p10["verdict"] = ("UNDECIDED (large amplitude oscillation, "
                          "ptp/mean={:.1f} -- mechanism undetermined: "
                          "period-match clause not tested (insufficient "
                          "points), and confounded by the settling defect "
                          "found elsewhere this cycle; NOT confirmed as "
                          "coherent-fringe perturbation)").format(
                              p10["ptp_over_mean"])
    else:
        p10["verdict"] = "PARTIAL"

    # ---- P-VIS42-11: settling
    p11 = dict(settle)
    p11["confirm"] = settle["rel_delta"] <= 0.0015
    p11["refute"] = settle["rel_delta"] > 0.01
    p11["verdict"] = ("CONFIRMED (settling closed)" if p11["confirm"] else
                      "REFUTED (settling is a live confound)" if p11["refute"]
                      else "PARTIAL")

    return {"P-VIS42-1": g1, "P-VIS42-1b": g2, "P-VIS42-2": p2,
            "P-VIS42-2a": p2a, "P-VIS42-3": p3, "P-VIS42-4": p4,
            "P-VIS42-5": p5, "P-VIS42-6": p6, "P-VIS42-7": p7,
            "P-VIS42-8": p8, "P-VIS42-9": p9, "P-VIS42-10": p10,
            "P-VIS42-11": p11}


# ===================================================== main
def main():
    t_start = time.time()
    print("=" * 78)
    print("exp-065 -- T24 ABSORB boundary sweep  |  Panel Iteration 42")
    print("Lead: VISION SCIENCE (rotation).  Director's Phase-3 synthesis "
          "applied in full.")
    print("=" * 78)
    print("\nFROZEN PREDICTIONS (committed to git in NOTES.md BEFORE this "
          "file's first run):")
    print(FROZEN_PREDICTIONS)
    print(f"lab/ diff check: {assert_lab_clean()}")

    print("\n--- GATE G-2 (P-VIS42-1b): static construction identity ---")
    g2 = gate_g2_static()
    for k, v in sorted(g2["by_window"].items()):
        print(f"    {k:<20} max|diff| = {v:.3e}")
    print(f"    max over all = {g2['max_diff']:.3e}   all_vacuum="
          f"{g2['all_vacuum']}   PASS={g2['pass']}")
    assert g2["pass"], "G-2 FAILED -- halting before any FDTD call (halt condition)"

    sweep = block_sweep()
    print(f"\n--- GATE G-1 (P-VIS42-1): exp-041 anchor identity ---")
    g1 = gate_g1_anchor(sweep["rows"])
    for c in g1["checks"]:
        print(f"    theta={c['theta']:+05.1f} lam={c['lambda_nm']}  "
              f"ours={c['ours']:+.17g}  exp041={c['exp041']:+.17g}  "
              f"delta={c['delta']:+.3e}  exact={c['exact']}")
    print(f"    {g1['n_checked']} checked, all_exact={g1['all_exact']}")
    print(f"    note: {g1['note']}")
    assert g1["all_exact"], "G-1 FAILED -- nothing else is read until this passes"

    pad = block_pad()
    article = block_article(sweep["profiles"])
    beam = block_beam()
    mini = block_mini(sweep["profiles"])
    settle = block_settle(sweep["profiles"])

    total_runs = (sweep["n_new_runs"] + pad["n_new_runs"] + article["n_new_runs"]
                  + beam["n_new_runs"] + mini["n_new_runs"] + settle["n_new_runs"])
    elapsed = time.time() - t_start
    print(f"\n=== {total_runs} new FDTD calls in {elapsed / 60:.1f} min "
          f"(hard stop {HARD_STOP_S / 60:.0f} min) ===")
    assert total_runs == 144, f"run-count mismatch vs frozen budget: {total_runs} != 144"

    sc_ = score(sweep, pad, article, beam, mini, settle, g1, g2)

    print("\n" + "=" * 78)
    print("SCORED PREDICTIONS")
    print("=" * 78)
    for pid in ("P-VIS42-1", "P-VIS42-1b", "P-VIS42-2", "P-VIS42-2a",
                "P-VIS42-3", "P-VIS42-4", "P-VIS42-5", "P-VIS42-6",
                "P-VIS42-7", "P-VIS42-8", "P-VIS42-9", "P-VIS42-10",
                "P-VIS42-11"):
        v = sc_[pid].get("verdict")
        if v is None:
            v = ("PASSED" if sc_[pid].get("all_exact", sc_[pid].get("pass"))
                 else "FAILED")
        print(f"  {pid:<12} {v}")

    out = {
        "experiment": "exp-065-t24-absorb-boundary-sweep",
        "panel_iteration": 42, "lead_seat": "VISION SCIENCE",
        "t1_escape_route": "N/A -- instrument/model-fidelity class",
        "configs": {k: {kk: vv for kk, vv in c.items()}
                    for k, c in dg.CONFIGS.items()},
        "steps": dg.STEPS, "steps_settle": dg.STEPS_SETTLE,
        "sweep_angles": list(dg.SWEEP_ANGLES),
        "mini_sweep_angles": list(dg.MINI_SWEEP_ANGLES),
        "fallback_angles": [float(t) for t in dg.FALLBACK_ANGLES],
        "gates": {"GATE_HARD": dg.GATE_HARD, "C_THR_LAB": dg.C_THR_LAB,
                  "C_THR_FIELD": dg.C_THR_FIELD,
                  "MARGINAL_BAND": [dg.MARGINAL_LO, dg.MARGINAL_HI]},
        "article": {"tau_center": dg.TAU_OFF_PASS, "sigma_e": dg.SIGMA_OFF_PASS,
                    "r_out": dg.R_OUT},
        "caveats": {"realizability_memo": dg.REALIZABILITY_MEMO_CAVEAT,
                    "g_transfer_t15": dg.G_TRANSFER_T15_CAVEAT,
                    "t5_thermal": dg.T5_THERMAL_CAVEAT},
        "block_sweep": {k: v for k, v in sweep.items() if k != "profiles"},
        "block_pad": {k: v for k, v in pad.items() if k != "profiles"},
        "block_article": article, "block_beam": beam, "block_mini": mini,
        "block_settle": settle,
        "scored": sc_,
        "total_new_runs": total_runs, "total_elapsed_s": elapsed,
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote results.json ({total_runs} runs, {elapsed / 60:.1f} min)")


if __name__ == "__main__":
    main()
