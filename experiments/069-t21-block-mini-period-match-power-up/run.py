"""exp-069 -- Block MINI's Period-Match Test, Powered Up: measurement harness.
=============================================================================
Panel Iteration 46 (lead: THERMODYNAMICS, rotation; synthesis: Director,
post Red Team's PROCEED-WITH-MANDATORY-FIXES verdict -- see
`phase3_synthesis.md` for the full accepted/overridden record; ZERO
overridden, all 10 mandatory fixes applied).

Four blocks:
  Block DENSE:   31 theta x {C40,C80} @600nm, STEPS=2800           = 62 calls
  Block SETTLE:  {39,40}deg x C80 @600nm, STEPS=4200                =  2 calls
  Block R3:      {39,40}deg x {C40_R3,C80_R3} @600nm(cpl=30), 4200  =  4 calls
  Block LEG750:  16 theta x {C40,C80} @750nm, STEPS=2800            = 32 calls
  TOTAL: 100 new FDTD calls.

Predictions (P-069-G1, -1, -2, -3, -4, -5, -6) committed in NOTES.md BEFORE
this file's first run (house discipline, non-negotiable), and printed
structurally below before the first FDTD call (exp-046/065's own
structural-freeze precedent).

Mandatory fix 4 (Red Team's Phase-2 audit): the Combined Verdict is decided
by ONE fully-corroborated gate (P-069-1 AND P-069-2 AND P-069-3 AND P-069-4
AND P-069-5, ALL REFUTE/co-gate-pass) vs the additive-null gate (P-069-1 AND
P-069-2 both CONFIRM) vs a THIRD outcome that is NOT reported as PARTIAL-and-
deferred -- it is immediate formal retirement, stated reason recorded
verbatim. No `lab/` change.
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


# ============================================================= structural freeze
FROZEN_PREDICTIONS = """
P-069-G1  absolute identity gate: theta in {38,40} x {C40,C80} x 600nm x
          STEPS=2800 reproduce exp-065's own committed
          settled_sweep_steps2800_diagnostic.json exactly (4 values)
          CONFIRM dC == 0.0 (float64) for all 4 | REFUTE any nonzero -- halts
          the cycle before anything else is trusted

P-069-1   (HEADLINE, amplitude) ptp/|mean| of delta(theta)=C80-C40 over the
          31-point Block DENSE window @600nm, STEPS=2800
          CONFIRM ptp/|mean| <= 1.5 | REFUTE ptp/|mean| > 2.5
          (raw ptp and mean reported alongside the ratio -- mandatory fix 10)

P-069-2   (HEADLINE, period, PRIMARY) fixed-period fit delta(x) =
          c0 + a*cos(2*pi*x/T) + b*sin(2*pi*x/T), x=sin(theta), T=cpl/A=
          0.026595745 FIXED (zero free period parameters). R^2 vs flat null.
          CONFIRM R^2 <= 0.15 | REFUTE R^2 >= 0.50
          [mandatory fix 2: this tests CONSISTENCY with T21's established
          stationary-phase-limit model (R^2=0.7852->0.8271 at ITS OWN best
          fit, never 1.0) -- not an independently-verified exact period]

P-069-3   (co-gating, period, SECONDARY -- promoted from diagnostic-only,
          mandatory fix 3) free-period grid search over P* in [1.0,4.0]deg
          (Tc swept correspondingly in sin-theta units), report best-fit P*
          and its own R^2.
          WITHIN TOLERANCE: |P*-P(39deg)|/P(39deg) <= 20% AND R^2(P*) >= 0.30
          OUT OF TOLERANCE: |P*-P(39deg)|/P(39deg) >= 50%, OR no P* in
          [1.0,4.0]deg clears R^2>=0.30

P-069-4   (co-gating, settling) Block SETTLE-C80: |dC(4200-2800)| at
          theta in {39,40}deg, 600nm, relative to |dC(2800-1400)| at the
          same cells (1400 values reused from exp-065's own committed
          block_mini -- loaded programmatically, never re-typed)
          CONFIRM <= 1% relative at BOTH cells
          REFUTE  >= 5% relative at EITHER cell

P-069-5   (co-gating, resolution/R3, mandatory fix 5) Block R3: does
          delta(theta)=C80-C40 at theta in {39,40}deg SURVIVE cpl 20->30
          (geometry rescaled x1.5, STEPS rescaled x1.5 to 4200, mirroring
          exp-033's own established R3 idiom)?
          CONFIRM: same sign at BOTH angles AND ratio delta_r3/delta_native
                   in [0.3, 3.0] at BOTH angles (survives refinement --
                   real physical feature, not a grid/staircase artifact)
          REFUTE:  sign flips at EITHER angle, OR ratio outside [0.1, 10]
                   at EITHER angle (consistent with grid-discretization
                   structure, not T21's own continuum mechanism)

P-069-6   (disclosed, NOT gating the Combined Verdict, mandatory fix 7)
          Block LEG750: same amplitude (ptp/|mean|) and period-search
          statistics as P-069-1/-3, computed at 750nm over 16 points
          spanning theta in [38,41]deg (~1.2 T21 periods at 750nm -- NOT
          powered the same as the 600nm leg; reported for generalization
          context, not scored pass/fail)

COMBINED VERDICT (mandatory fixes 1, 3, 4 -- computed in code, not prose):
  COHERENT-FRINGE, fully corroborated  <=> P-069-1 REFUTE AND P-069-2 REFUTE
    AND P-069-3 within tolerance AND P-069-4 CONFIRM AND P-069-5 CONFIRM.
  ADDITIVE-SYSTEMATIC, vindicated      <=> P-069-1 CONFIRM AND P-069-2 CONFIRM.
  ANYTHING ELSE => immediate FORMAL RETIREMENT of the period-match test,
    stated reason: "statistical power was raised to the mandate's own spec
    (31 points/0.2deg step/~3.0 periods, settled STEPS=2800, a resolution
    check, a settling-closure check, and a co-gating free-period
    cross-check) and the result is still non-decisive -- that is itself
    the finding." NOT reported as PARTIAL-and-deferred (mandatory fix 4).
"""


def assert_lab_clean():
    out = subprocess.run(["git", "diff", "--stat", "--", "lab/"],
                         cwd=os.path.abspath(os.path.join(HERE, "..", "..")),
                         capture_output=True, text=True).stdout.strip()
    assert out == "", f"lab/ is dirty -- the no-new-machinery position fails:\n{out}"
    return "clean"


# ===================================================== generic FDTD call
def _one_run(cfg, cpl, theta, steps):
    sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=cpl,
              courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
    sim.add_line_source(cfg["src_x"], y_lo=cfg["y_lo"], y_hi=cfg["y_hi"],
                        angle_deg=theta, amplitude=1.0,
                        profile="plane", edge=dg.TAPER)
    sim.run(steps)
    return sc.full_capture(sim)


def _one_run_r3(cfg, theta):
    """R3-rescaled call: cpl=30, R3-scaled TAPER (Block R3's own geometry
    carries its own TAPER -- see dg.R3_TAPER)."""
    sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=dg.R3_CPL[600],
              courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
    sim.add_line_source(cfg["src_x"], y_lo=cfg["y_lo"], y_hi=cfg["y_hi"],
                        angle_deg=theta, amplitude=1.0,
                        profile="plane", edge=dg.R3_TAPER)
    sim.run(dg.R3_STEPS)
    return sc.full_capture(sim)


def _profile(cap, cfg):
    ph = sc.phasors(cap)
    return amb.observer_profile(ph, cfg["plane_x"], cfg["y_lo"],
                                cfg["y_hi"]).tolist()


def _c_empty(profile, cfg):
    p = np.array(profile)
    r = amb.contrast_from_runs([p], [p], [1.0], cfg["y_lo"], cfg["obj_y"],
                               dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)
    return r["C_empty"]


def _c_empty_r3(profile, cfg):
    p = np.array(profile)
    r = amb.contrast_from_runs([p], [p], [1.0], cfg["y_lo"], cfg["obj_y"],
                               dg.R3_W_OBJ, dg.R3_GUARD_OUT, dg.R3_W_FLANK)
    return r["C_empty"]


# ===================================================== worker entry points
def _dense_one(args):
    key, theta = args
    cfg = dg.CONFIGS[key]
    t0 = time.time()
    cap = _one_run(cfg, dg.CPL[600], theta, dg.STEPS_SETTLED)
    return (key, theta, _profile(cap, cfg), time.time() - t0)


def _settle_one(args):
    key, theta = args
    cfg = dg.CONFIGS[key]
    t0 = time.time()
    cap = _one_run(cfg, dg.CPL[600], theta, dg.STEPS_STRESS)
    return (key, theta, _profile(cap, cfg), time.time() - t0)


def _r3_one(args):
    key, theta = args
    cfg = dg.R3_CONFIGS[key]
    t0 = time.time()
    cap = _one_run_r3(cfg, theta)
    return (key, theta, _profile(cap, cfg), time.time() - t0)


def _leg750_one(args):
    key, theta = args
    cfg = dg.CONFIGS[key]
    t0 = time.time()
    cap = _one_run(cfg, dg.CPL[750], theta, dg.STEPS_SETTLED)
    return (key, theta, _profile(cap, cfg), time.time() - t0)


# ===================================================== Block DENSE
def block_dense():
    jobs = [(k, th) for k in ("C40", "C80") for th in dg.DENSE_ANGLES]
    print(f"\n=== Block DENSE: {len(dg.DENSE_ANGLES)} theta x 2 configs "
          f"@600nm STEPS={dg.STEPS_SETTLED} = {len(jobs)} calls ===", flush=True)
    t0, n = time.time(), 0
    profiles = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, prof, dt in ex.map(_dense_one, jobs):
            profiles[(key, th)] = prof
            n += 1
            print(f"  [DENSE {n:3d}/{len(jobs)}] {key} theta={th:+06.2f} "
                  f"({dt:5.1f}s)", flush=True)
    assert n == len(jobs), f"DENSE run-count mismatch: {n} != {len(jobs)}"
    rows = []
    for th in dg.DENSE_ANGLES:
        c40 = _c_empty(profiles[("C40", th)], dg.CONFIGS["C40"])
        c80 = _c_empty(profiles[("C80", th)], dg.CONFIGS["C80"])
        rows.append({"theta": th, "C_empty_C40": c40, "C_empty_C80": c80,
                     "delta": c80 - c40})
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "rows": rows,
            "profiles": profiles}


# ===================================================== Block SETTLE-C80
def block_settle():
    jobs = [("C80", th) for th in dg.SETTLE_ANGLES]
    print(f"\n=== Block SETTLE-C80: {len(jobs)} theta x C80 @600nm "
          f"STEPS={dg.STEPS_STRESS} = {len(jobs)} calls ===", flush=True)
    t0, n = time.time(), 0
    profiles = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, prof, dt in ex.map(_settle_one, jobs):
            profiles[th] = prof
            n += 1
            print(f"  [SETTLE {n}/{len(jobs)}] theta={th:+05.1f} ({dt:5.1f}s)",
                  flush=True)
    assert n == len(jobs), f"SETTLE run-count mismatch: {n} != {len(jobs)}"
    rows = [{"theta": th, "C_empty_C80_4200": _c_empty(profiles[th], dg.CONFIGS["C80"])}
            for th in dg.SETTLE_ANGLES]
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "rows": rows}


# ===================================================== Block R3
def block_r3():
    jobs = [(k, th) for k in ("C40_R3", "C80_R3") for th in dg.SETTLE_ANGLES]
    print(f"\n=== Block R3: {len(dg.SETTLE_ANGLES)} theta x 2 configs "
          f"@600nm cpl={dg.R3_CPL[600]} STEPS={dg.R3_STEPS} = {len(jobs)} calls ===",
          flush=True)
    t0, n = time.time(), 0
    profiles = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, prof, dt in ex.map(_r3_one, jobs):
            profiles[(key, th)] = prof
            n += 1
            print(f"  [R3 {n}/{len(jobs)}] {key} theta={th:+05.1f} ({dt:5.1f}s)",
                  flush=True)
    assert n == len(jobs), f"R3 run-count mismatch: {n} != {len(jobs)}"
    rows = []
    for th in dg.SETTLE_ANGLES:
        c40 = _c_empty_r3(profiles[("C40_R3", th)], dg.R3_CONFIGS["C40_R3"])
        c80 = _c_empty_r3(profiles[("C80_R3", th)], dg.R3_CONFIGS["C80_R3"])
        rows.append({"theta": th, "C_empty_C40_r3": c40, "C_empty_C80_r3": c80,
                     "delta_r3": c80 - c40})
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "rows": rows}


# ===================================================== Block LEG750
def block_leg750():
    jobs = [(k, th) for k in ("C40", "C80") for th in dg.LEG750_ANGLES]
    print(f"\n=== Block LEG750: {len(dg.LEG750_ANGLES)} theta x 2 configs "
          f"@750nm STEPS={dg.STEPS_SETTLED} = {len(jobs)} calls ===", flush=True)
    t0, n = time.time(), 0
    profiles = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, prof, dt in ex.map(_leg750_one, jobs):
            profiles[(key, th)] = prof
            n += 1
            print(f"  [LEG750 {n:2d}/{len(jobs)}] {key} theta={th:+06.2f} "
                  f"({dt:5.1f}s)", flush=True)
    assert n == len(jobs), f"LEG750 run-count mismatch: {n} != {len(jobs)}"
    rows = []
    for th in dg.LEG750_ANGLES:
        c40 = _c_empty(profiles[("C40", th)], dg.CONFIGS["C40"])
        c80 = _c_empty(profiles[("C80", th)], dg.CONFIGS["C80"])
        rows.append({"theta": th, "C_empty_C40": c40, "C_empty_C80": c80,
                     "delta": c80 - c40})
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "rows": rows}


# ===================================================== gate
def gate_g1(dense_rows):
    ref_path = os.path.join(HERE, "..", "065-t24-absorb-boundary-sweep",
                            "settled_sweep_steps2800_diagnostic.json")
    ref = json.load(open(os.path.abspath(ref_path)))
    by_theta = {r["theta"]: r for r in dense_rows}
    checks = []
    for key in ("C40", "C80"):
        for th in (38.0, 40.0):
            ours = by_theta[th][f"C_empty_{key}"]
            k = f"{key}|{th}|600"
            ref_v = ref[k]
            d = ours - ref_v
            checks.append({"config": key, "theta": th, "ours": ours,
                           "ref": ref_v, "delta": d, "exact": d == 0.0})
    return {"n_checked": len(checks), "all_exact": all(c["exact"] for c in checks),
            "max_abs_delta": max((abs(c["delta"]) for c in checks), default=None),
            "checks": checks}


# ===================================================== period-match statistics
def _fixed_period_fit(x, y, T):
    """Linear least-squares fit y = c0 + a*cos(2*pi*x/T) + b*sin(2*pi*x/T),
    T FIXED. Returns (c0, a, b, r_squared)."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    w = 2 * math.pi / T
    X = np.column_stack([np.ones_like(x), np.cos(w * x), np.sin(w * x)])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    yhat = X @ coef
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return dict(c0=float(coef[0]), a=float(coef[1]), b=float(coef[2]), r_squared=r2)


def _free_period_search(theta_deg, delta, center_deg=39.0, lo_deg=1.0, hi_deg=4.0,
                        n_grid=400):
    """P-069-3: grid-search the best-fit period P* (degrees, evaluated at
    `center_deg`'s own cos-theta) over [lo_deg,hi_deg], fitting in sin(theta)
    space at each candidate. Returns best P* and its R^2."""
    x = np.sin(np.radians(np.asarray(theta_deg, dtype=float)))
    y = np.asarray(delta, dtype=float)
    cos_c = math.cos(math.radians(center_deg))
    best = None
    for p_star in np.linspace(lo_deg, hi_deg, n_grid):
        Tc = math.radians(p_star) * cos_c   # sin-theta period at this P*
        fit = _fixed_period_fit(x, y, Tc)
        if best is None or fit["r_squared"] > best["r_squared"]:
            best = dict(p_star_deg=float(p_star), r_squared=fit["r_squared"])
    return best


# ===================================================== scoring
def score(dense, settle, r3, leg750, g1):
    P39_600 = dg.P_deg(39.0, 600)
    by_theta = {r["theta"]: r for r in dense["rows"]}

    # P-069-1
    deltas = np.array([r["delta"] for r in dense["rows"]])
    thetas = np.array([r["theta"] for r in dense["rows"]])
    ptp = float(np.ptp(deltas))
    mean = float(np.mean(deltas))
    ratio = ptp / abs(mean) if mean != 0 else float("inf")
    p1 = dict(ptp=ptp, mean=mean, ratio=ratio,
             confirm=ratio <= 1.5, refute=ratio > 2.5)

    # P-069-2 (fixed period, primary)
    x_sin = np.sin(np.radians(thetas))
    fit_fixed = _fixed_period_fit(x_sin, deltas, dg.T_SINTHETA_600)
    p2 = dict(r_squared=fit_fixed["r_squared"], T_fixed=dg.T_SINTHETA_600,
             confirm=fit_fixed["r_squared"] <= 0.15,
             refute=fit_fixed["r_squared"] >= 0.50,
             coefficients=dict(c0=fit_fixed["c0"], a=fit_fixed["a"], b=fit_fixed["b"]))

    # P-069-3 (free period, co-gating)
    free = _free_period_search(thetas, deltas, center_deg=39.0)
    rel_dev = abs(free["p_star_deg"] - P39_600) / P39_600
    within_tol = (rel_dev <= 0.20) and (free["r_squared"] >= 0.30)
    out_of_tol = (rel_dev >= 0.50) or (free["r_squared"] < 0.30)
    p3 = dict(p_star_deg=free["p_star_deg"], r_squared=free["r_squared"],
             P39_600=P39_600, rel_dev=rel_dev,
             within_tolerance=bool(within_tol), out_of_tolerance=bool(out_of_tol))

    # P-069-4 (settling closure, C80)
    settle_by_theta = {r["theta"]: r["C_empty_C80_4200"] for r in settle["rows"]}
    # 1400 values: reused from exp-065's own committed block_mini
    exp065_results = json.load(open(os.path.abspath(os.path.join(
        HERE, "..", "065-t24-absorb-boundary-sweep", "results.json"))))
    mini_1400 = {r["theta"]: r["C_empty_C80"]
                for r in exp065_results["block_mini"]["rows"]}
    p4_cells = []
    for th in dg.SETTLE_ANGLES:
        c1400 = mini_1400[th]
        c2800 = by_theta[th]["C_empty_C80"]
        c4200 = settle_by_theta[th]
        d_28_14 = abs(c2800 - c1400)
        d_42_28 = abs(c4200 - c2800)
        rel = d_42_28 / d_28_14 if d_28_14 != 0 else float("inf")
        p4_cells.append(dict(theta=th, C_1400=c1400, C_2800=c2800, C_4200=c4200,
                             abs_delta_2800_1400=d_28_14,
                             abs_delta_4200_2800=d_42_28, rel=rel))
    p4 = dict(cells=p4_cells,
             confirm=all(c["rel"] <= 0.01 for c in p4_cells),
             refute=any(c["rel"] >= 0.05 for c in p4_cells))

    # P-069-5 (R3 resolution check)
    r3_by_theta = {r["theta"]: r["delta_r3"] for r in r3["rows"]}
    p5_cells = []
    for th in dg.SETTLE_ANGLES:
        d_native = by_theta[th]["delta"]
        d_r3 = r3_by_theta[th]
        same_sign = (d_native > 0) == (d_r3 > 0)
        ratio_r3 = d_r3 / d_native if d_native != 0 else float("inf")
        p5_cells.append(dict(theta=th, delta_native=d_native, delta_r3=d_r3,
                             same_sign=bool(same_sign), ratio=ratio_r3))
    p5 = dict(cells=p5_cells,
             confirm=all(c["same_sign"] and 0.3 <= c["ratio"] <= 3.0 for c in p5_cells),
             refute=any((not c["same_sign"]) or not (0.1 <= c["ratio"] <= 10.0)
                        for c in p5_cells))

    # P-069-6 (750nm, disclosed only)
    d750 = np.array([r["delta"] for r in leg750["rows"]])
    th750 = np.array([r["theta"] for r in leg750["rows"]])
    ptp750 = float(np.ptp(d750))
    mean750 = float(np.mean(d750))
    ratio750 = ptp750 / abs(mean750) if mean750 != 0 else float("inf")
    T_sin_750 = dg.CPL[750] / dg.A_HALF_APERTURE
    fit750 = _fixed_period_fit(np.sin(np.radians(th750)), d750, T_sin_750)
    p6 = dict(ptp=ptp750, mean=mean750, ratio=ratio750,
             r_squared_fixed=fit750["r_squared"], T_fixed=T_sin_750,
             P39_750=dg.P_deg(39.0, 750), n_periods=(dg.LEG750_HI - dg.LEG750_LO) / dg.P_deg(39.0, 750))

    # Combined verdict (mandatory fixes 1, 3, 4)
    coherent = p1["refute"] and p2["refute"] and p3["within_tolerance"] and p4["confirm"] and p5["confirm"]
    additive = p1["confirm"] and p2["confirm"]
    if coherent:
        combined = "COHERENT_FRINGE_FULLY_CORROBORATED"
        combined_reason = ("All five co-gates satisfied: amplitude REFUTE, "
                          "fixed-period REFUTE, free-period within tolerance, "
                          "settling CONFIRM, resolution CONFIRM.")
    elif additive:
        combined = "ADDITIVE_SYSTEMATIC_VINDICATED"
        combined_reason = "Both amplitude and fixed-period statistics CONFIRM the flat/null model."
    else:
        combined = "FORMAL_RETIREMENT_NON_DECISIVE"
        combined_reason = ("Statistical power was raised to the mandate's own "
                          "spec (31 points/0.2deg step/~3.0 periods, settled "
                          "STEPS=2800, a resolution check, a settling-closure "
                          "check, and a co-gating free-period cross-check) and "
                          "the result is still non-decisive -- that is itself "
                          "the finding. Per mandatory fix 4, this is NOT "
                          "reported as PARTIAL-and-deferred: the period-match "
                          "test (P-VIS42-10 lineage) is formally retired as of "
                          "this cycle's close.")

    return dict(g1=g1, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6,
               combined_verdict=combined, combined_reason=combined_reason)


# ===================================================== main
def main():
    t_start = time.time()
    print(FROZEN_PREDICTIONS, flush=True)
    print(assert_lab_clean(), flush=True)

    dense = block_dense()
    settle = block_settle()
    r3 = block_r3()
    leg750 = block_leg750()

    g1 = gate_g1(dense["rows"])
    assert g1["all_exact"], f"P-069-G1 FAILED: {g1}"
    print(f"\nP-069-G1 PASSED: {g1['n_checked']}/{g1['n_checked']} exact", flush=True)

    scored = score(dense, settle, r3, leg750, g1)

    total_calls = dense["n_new_runs"] + settle["n_new_runs"] + r3["n_new_runs"] + leg750["n_new_runs"]
    total_elapsed = time.time() - t_start

    out = {
        "experiment": "069-t21-block-mini-period-match-power-up",
        "panel_iteration": 46,
        "lead_seat": "THERMODYNAMICS",
        "t1_escape_route": "N/A (instrument/model-fidelity re-verification class)",
        "steps_settled": dg.STEPS_SETTLED, "steps_stress": dg.STEPS_STRESS,
        "r3_steps": dg.R3_STEPS, "r3_ratio": dg.R3_RATIO,
        "dense_angles": list(dg.DENSE_ANGLES), "leg750_angles": list(dg.LEG750_ANGLES),
        "block_dense": {"n_new_runs": dense["n_new_runs"], "elapsed_s": dense["elapsed_s"],
                        "rows": dense["rows"]},
        "block_settle": {"n_new_runs": settle["n_new_runs"], "elapsed_s": settle["elapsed_s"],
                         "rows": settle["rows"]},
        "block_r3": {"n_new_runs": r3["n_new_runs"], "elapsed_s": r3["elapsed_s"],
                    "rows": r3["rows"]},
        "block_leg750": {"n_new_runs": leg750["n_new_runs"], "elapsed_s": leg750["elapsed_s"],
                         "rows": leg750["rows"]},
        "scored": scored,
        "total_new_runs": total_calls,
        "total_elapsed_s": total_elapsed,
        "r_contact_disposition": ("UNTOUCHED this cycle -- PLAN.md's "
                                  "Iteration-46 queue item #2 remains blocked "
                                  "on WebSearch/WebFetch tooling; not picked "
                                  "up in parallel despite PLAN.md's explicit "
                                  "invitation to do so if capacity allows "
                                  "(mandatory fix 9, disclosed not silently "
                                  "dropped)."),
    }

    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)

    print(f"\n=== DONE: {total_calls} FDTD calls, {total_elapsed:.1f}s "
          f"({total_elapsed/60:.2f} min) ===", flush=True)
    print(f"P-069-1 (amplitude): ptp={scored['p1']['ptp']:.6f} "
          f"mean={scored['p1']['mean']:.6f} ratio={scored['p1']['ratio']:.4f} "
          f"confirm={scored['p1']['confirm']} refute={scored['p1']['refute']}", flush=True)
    print(f"P-069-2 (fixed period): R^2={scored['p2']['r_squared']:.4f} "
          f"confirm={scored['p2']['confirm']} refute={scored['p2']['refute']}", flush=True)
    print(f"P-069-3 (free period): P*={scored['p3']['p_star_deg']:.4f}deg "
          f"R^2={scored['p3']['r_squared']:.4f} rel_dev={scored['p3']['rel_dev']:.4f} "
          f"within_tol={scored['p3']['within_tolerance']}", flush=True)
    print(f"P-069-4 (settling): confirm={scored['p4']['confirm']} "
          f"refute={scored['p4']['refute']}", flush=True)
    print(f"P-069-5 (R3): confirm={scored['p5']['confirm']} "
          f"refute={scored['p5']['refute']}", flush=True)
    print(f"\nCOMBINED VERDICT: {scored['combined_verdict']}", flush=True)
    print(scored["combined_reason"], flush=True)

    return out


if __name__ == "__main__":
    main()
