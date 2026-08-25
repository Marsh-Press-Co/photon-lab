"""exp-071 -- ELECTROMAGNETISM's C60/C70 `ABSORB`-depth causal falsification
test for T28: measurement harness.
=============================================================================
Panel Iteration 48 (lead: VISION SCIENCE, rotation; synthesis: Director,
post Red Team's PROCEED-WITH-MANDATORY-FIXES verdict -- see
phase3_synthesis.md for the full accepted/overridden record; ZERO
overridden, all 7 mandatory fixes applied).

Four blocks:
  Block G1:            {39,40}deg x {C40,C80} @600nm, STEPS=2800    =  4 calls
  Block DENSE-CAUSAL:   31 theta x {C60,C70} @600nm, STEPS=2800      = 62 calls
  Block R3-PEAK:        {37.2,41.4}deg x {C40_R3,C60_R3,C70_R3,C80_R3}
                         @cpl=30, STEPS=4200                         =  8 calls
  Block SETTLE-C60C70:  {37.2,41.4}deg x {C60,C70} @600nm, STEPS=4200 = 4 calls
  TOTAL: 78 new FDTD calls.

Predictions (P-071-G1, -1, -2, -3, -4, -5, plus Block SETTLE-C60C70)
committed in NOTES.md BEFORE this file's first run (house discipline,
non-negotiable), and printed structurally below before the first FDTD call.

MANDATORY FIXES applied here (Red Team's Phase-2 audit, phase2_redteam_
audit.md; disposition table in phase3_synthesis.md; ZERO overridden):
  1. Block SETTLE-C60C70 added -- binding precondition on P-071-2 (EM).
  2. Rayleigh resolution-floor computed for every P-071-3 pair AND for the
     CONFIRM/REFUTE trend bands themselves (QUANTUM, extended by Red Team
     to both directions) -- comparisons/verdicts below the floor are
     reported UNRESOLVED, folded into NEITHER, never silently counted.
  3. CONFIRM branch relabeled "ABSORB-depth-tied numerical-boundary-
     construction effect (not a material/physical mechanism)" (MATERIALS) --
     ABSORB is lab/fdtd2d.py::Sim._damping's own domain-truncation device,
     a cubic-ramp PML-analog, not a witness-scene material.
  4. THERMO scope-inapplicability sentence added to the Combined Verdict
     text (THERMODYNAMICS): no energy sidecar applies -- no absorbing
     article is run this cycle and all four congruent configs are
     near-total absorbers at their boundary by construction regardless of
     ABSORB depth, so there is no absorbed-energy trend to characterize
     and no witness-scene material to re-radiate from.
  5. `_free_period_search`/`_fixed_period_fit` imported by reference from
     exp-069's run.py (design_geometry.py), defaults asserted in code.
  6. De-scope docket updated (design_geometry.py::fdtd_budget_minimum) --
     Block SETTLE-C60C70 and the resolution-floor computation never
     de-scoped.
  7. Hard stop restated 90->100 min (NOTES.md/phase3_synthesis.md).
No `lab/` change anywhere in this cycle.
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
ABSORB_NOT_MATERIAL_CAVEAT = (
    "ABSORB is lab/fdtd2d.py::Sim._damping's own numerical domain-truncation "
    "boundary depth (a cubic-ramp PML-analog, exp(-0.30*d), applied to all "
    "four box edges) -- NOT a material or physical-optics parameter, real or "
    "hypothetical. Any CONFIRM below describes a numerical-boundary-"
    "construction effect, never a physical absorbing mechanism (exp-070's "
    "own mandatory fix 5, MATERIALS' Phase-2 catch this cycle -- reinstated "
    "per the identical rule).")
THERMO_SCOPE_CAVEAT = (
    "THERMO energy-sidecar metric row does NOT apply this cycle: no "
    "absorbing article is run (Block ARTICLE not re-run, idealizations "
    "4/8), and all four congruent configs are near-total absorbers at "
    "their own boundary by construction (that is what makes them "
    "congruent) regardless of ABSORB depth -- there is no absorbed-energy "
    "TREND for a sidecar to characterize, and no witness-scene material "
    "for power to re-radiate from (THERMODYNAMICS' Phase-2 finding).")
WAVELENGTH_SCOPE_CAVEAT = (
    "600nm-only scope (idealization 2): the same ABSORB cell count is a "
    "different optical depth at other wavelengths (e.g. 80 cells = 4.0 "
    "lambda at 600nm/cpl20 but 3.2 lambda at 750nm/cpl25, PHOTONICS' "
    "Phase-2 finding) -- a CONFIRM at 600nm alone cannot distinguish a "
    "lambda-scaled physical coupling from a cell-count/discretization "
    "artifact; the CONFIRM label below is scoped to 600nm only, not to "
    "an optical mechanism generally. A confirmatory lambda leg is queued "
    "as a fast-follow (Iteration 49), not run this cycle (mandate scope).")
PAD_CONFOUND_CAVEAT = (
    "PAD = ABSORB - 40 EXACTLY at all four congruent configs (dg065."
    "CONFIGS) -- every absolute position (NX/NY/SRC_X/PLANE_X/OBJ_X/OBJ_Y) "
    "shifts in lockstep with ABSORB; only RELATIVE quantities (A=752, "
    "aperture_cells=1504, clearances) are genuinely held fixed. This ONE "
    "axis is therefore a COMPOUND axis: ABSORB (damping-ramp depth/"
    "strength) and PAD (round-trip path length to the boundary) move "
    "together by construction, with no config in this series holding one "
    "fixed while varying the other. A CONFIRM on this series describes an "
    "ABSORB-OR-PAD-tied effect, NOT specifically an ABSORB-tied one, until "
    "a PAD-decorrelated config exists (Red Team's Phase-5 final audit, "
    "independently confirmed by THERMODYNAMICS/ELECTROMAGNETISM/QUANTUM "
    "OPTICS' Phase-5 reviews -- a genuine gap in this congruent series' own "
    "causal-inference logic, unflagged across three consecutive T28 cycles "
    "using it, Iterations 46-48, until this cycle's Phase 5. A REFUTE is "
    "NOT equally compromised: a flat trend on the compound axis validly "
    "rules out sensitivity to both candidate quantities together.)")

FROZEN_PREDICTIONS = f"""
P-071-G1  absolute identity gate: theta in {{39,40}} x {{C40,C80}} x 600nm x
          STEPS=2800 reproduce exp-069's own committed block_dense rows
          exactly (4 values, loaded programmatically).
          CONFIRM dC == 0.0 (float64) for all 4 | REFUTE any nonzero -- halts
          the cycle before anything else is trusted.

Block SETTLE-C60C70  (mandatory fix 1, EM) |dC(4200-2800)| at theta in
          {{37.2,41.4}}deg, 600nm, C60/C70, relative to GATE_HARD (the
          instrument-floor scale -- idealization 10: 37.2/41.4deg are OFF
          exp-065's coarse STEPS=1400 angle grid, so there is no 1400-STEPS
          comparator at these exact cells; this is NOT a 1400-anchored
          relative percentage, corrected here per Red Team's Phase-5 final
          audit mandatory fix 3 -- score_settle_c60c70()'s own docstring
          and implementation always used this convention; this text
          originally described the wrong one). BINDING PRECONDITION on
          P-071-2:
          CONFIRM (settled) <= 1x GATE_HARD at ALL FOUR cells (2 theta x 2
          configs) | REFUTE (unsettled) >= 5x GATE_HARD at ANY cell.

P-071-1   (descriptive, feeds -2/-3) Free-period grid search -- IDENTICAL
          methodology to exp-069/070's `_free_period_search` (imported by
          reference, defaults asserted [1,4]deg/n_grid=400/center=39deg) --
          applied to C40(theta), C60(theta), C70(theta), C80(theta)
          INDIVIDUALLY over the 31-pt window. C40/C80 reused from
          exp-069's committed Block DENSE (0 new calls); C60/C70 newly
          computed from Block DENSE-CAUSAL.

P-071-2   (HEADLINE, causal trend test) Linear regression P*(ABSORB) =
          m*ABSORB + c over the four points ABSORB in {{40,60,70,80}}, GATED
          by the Rayleigh resolution floor (mandatory fix 2) on BOTH
          directions -- a trend statistic that falls below its own
          resolution floor is reported UNRESOLVED, not CONFIRM or REFUTE,
          regardless of its raw R^2/spread value.
          CONFIRM (ABSORB-depth-tied numerical-boundary-construction
          effect, mandatory fix 3 -- NOT a material/physical mechanism,
          see caveat below): |P*(80)_fit - P*(40)_fit|/mean(P*) >= 30% AND
          R^2(linear fit) >= 0.50 AND resolution_ratio(P*(40),P*(80)) >= 1.0
          REFUTE (shared-geometry, NOT ABSORB-tied): max pairwise
          |P*(Ca)-P*(Cb)|/mean <= 15% AND R^2(linear fit) <= 0.30 AND EVERY
          pairwise comparison used has resolution_ratio >= 1.0 (else that
          pair is UNRESOLVED, not evidence for flatness)
          NEITHER: anything else, including any precondition failure
          (G1/SETTLE-C60C70/P-071-4 not all CONFIRM) or resolution-floor
          failure on the trend test itself -- explicit, computed, disclosed
          with the full P-071-3 spread+resolution table and P-071-1
          per-config table attached. NOT a silent PARTIAL escape hatch.

P-071-3   (required disclosure) Pairwise cross-config consistency
          |P*(Ca)-P*(Cb)|/mean at ALL 6 pairs among {{C40,C60,C70,C80}},
          EACH annotated with its own Rayleigh resolution_ratio and a
          RESOLVED/UNRESOLVED flag (mandatory fix 2) -- reported in full,
          every pair, regardless of P-071-2's outcome.

P-071-4   (co-gating, peak-cell R3 -- BINDING PRECONDITION) Mirrors
          P-069-5's exact construction, at the PEAK angles: does
          delta(theta)=C80(theta)-C40(theta) survive cpl 20->30
          (R3_STEPS=4200) at theta in {{37.2,41.4}}deg?
          CONFIRM: same sign at both angles AND ratio delta_r3/delta_native
          in [0.3,3.0] at both | REFUTE: sign flip at either, OR ratio
          outside [0.1,10] at either.

P-071-5   (disclosed, non-gating extension) Same peak-cell R3 check,
          additionally on delta(theta)=C70(theta)-C60(theta) -- extends
          resolution-robustness evidence into the interior of the ABSORB
          series.

CAVEATS (mandatory fixes 3, 4, plus Phase-5 mandatory fix 4/6; disclosed
regardless of outcome, appended UNIFORMLY to every Combined-Verdict branch):
  {ABSORB_NOT_MATERIAL_CAVEAT}
  {THERMO_SCOPE_CAVEAT}
  {WAVELENGTH_SCOPE_CAVEAT}
  {PAD_CONFOUND_CAVEAT}

COMBINED VERDICT (computed in code, not prose):
  HALT <=> P-071-G1 fails. No other item is scored.
  CONFIRMED <=> G1 PASSED AND Block-SETTLE-C60C70 CONFIRM AND P-071-4
    CONFIRM AND P-071-2 CONFIRM (resolution-floor-gated, both directions).
  REFUTED <=> G1 PASSED AND Block-SETTLE-C60C70 CONFIRM AND P-071-4
    CONFIRM AND P-071-2 REFUTE (resolution-floor-gated, both directions).
  NEITHER <=> G1 PASSED AND anything else -- an explicit, computed branch,
    reported with full P-071-1/-3 tables, never a silent default.
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
              courant_frac=dg.dg065.COURANT_FRAC, absorb=cfg["absorb"])
    sim.add_line_source(cfg["src_x"], y_lo=cfg["y_lo"], y_hi=cfg["y_hi"],
                        angle_deg=theta, amplitude=1.0,
                        profile="plane", edge=dg.dg065.TAPER)
    sim.run(steps)
    return sc.full_capture(sim)


def _one_run_r3(cfg, theta):
    sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=dg.R3_CPL[600],
              courant_frac=dg.dg065.COURANT_FRAC, absorb=cfg["absorb"])
    sim.add_line_source(cfg["src_x"], y_lo=cfg["y_lo"], y_hi=cfg["y_hi"],
                        angle_deg=theta, amplitude=1.0,
                        profile="plane", edge=dg.dg069.R3_TAPER)
    sim.run(dg.R3_STEPS)
    return sc.full_capture(sim)


def _profile(cap, cfg):
    ph = sc.phasors(cap)
    return amb.observer_profile(ph, cfg["plane_x"], cfg["y_lo"],
                                cfg["y_hi"]).tolist()


def _c_empty(profile, cfg):
    p = np.array(profile)
    r = amb.contrast_from_runs([p], [p], [1.0], cfg["y_lo"], cfg["obj_y"],
                               dg.dg065.W_OBJ, dg.dg065.GUARD_OUT, dg.dg065.W_FLANK)
    return r["C_empty"]


def _c_empty_r3(profile, cfg):
    p = np.array(profile)
    r = amb.contrast_from_runs([p], [p], [1.0], cfg["y_lo"], cfg["obj_y"],
                               dg.dg069.R3_W_OBJ, dg.dg069.R3_GUARD_OUT,
                               dg.dg069.R3_W_FLANK)
    return r["C_empty"]


# ===================================================== worker entry points
def _g1_one(args):
    key, theta = args
    cfg = dg.CONFIGS[key]
    t0 = time.time()
    cap = _one_run(cfg, dg.CPL[600], theta, dg.STEPS_SETTLED)
    return (key, theta, _c_empty(_profile(cap, cfg), cfg), time.time() - t0)


def _dense_causal_one(args):
    key, theta = args
    cfg = dg.CONFIGS[key]
    t0 = time.time()
    cap = _one_run(cfg, dg.CPL[600], theta, dg.STEPS_SETTLED)
    return (key, theta, _c_empty(_profile(cap, cfg), cfg), time.time() - t0)


def _r3_peak_one(args):
    key, theta = args
    cfg = dg.R3_CONFIGS[key]
    t0 = time.time()
    cap = _one_run_r3(cfg, theta)
    return (key, theta, _c_empty_r3(_profile(cap, cfg), cfg), time.time() - t0)


def _settle_one(args):
    key, theta = args
    cfg = dg.CONFIGS[key]
    t0 = time.time()
    cap = _one_run(cfg, dg.CPL[600], theta, dg.STEPS_STRESS)
    return (key, theta, _c_empty(_profile(cap, cfg), cfg), time.time() - t0)


# ===================================================== Block G1
def block_g1():
    jobs = [(k, th) for k in ("C40", "C80") for th in dg.G1_ANGLES]
    print(f"\n=== Block G1: {len(jobs)} calls (identity gate) ===", flush=True)
    t0, n = time.time(), 0
    out = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, c, dt in ex.map(_g1_one, jobs):
            out[(key, th)] = c
            n += 1
            print(f"  [G1 {n}/{len(jobs)}] {key} theta={th:+05.1f} ({dt:5.1f}s)",
                  flush=True)
    assert n == len(jobs)
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "values": out}


# ===================================================== Block DENSE-CAUSAL
def block_dense_causal():
    jobs = [(k, th) for k in dg.DENSE_CAUSAL_CONFIGS for th in dg.DENSE_ANGLES]
    print(f"\n=== Block DENSE-CAUSAL: {len(jobs)} calls "
          f"({dg.DENSE_CAUSAL_CONFIGS} x {len(dg.DENSE_ANGLES)} theta) ===",
          flush=True)
    t0, n = time.time(), 0
    out = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, c, dt in ex.map(_dense_causal_one, jobs):
            out[(key, th)] = c
            n += 1
            print(f"  [DENSE-CAUSAL {n:3d}/{len(jobs)}] {key} theta={th:+06.2f} "
                  f"({dt:5.1f}s)", flush=True)
    assert n == len(jobs)
    rows = {k: [{"theta": th, "C_empty": out[(k, th)]} for th in dg.DENSE_ANGLES]
            for k in dg.DENSE_CAUSAL_CONFIGS}
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "rows": rows}


# ===================================================== Block R3-PEAK
def block_r3_peak():
    jobs = [(k, th) for k in dg.R3_CONFIGS for th in dg.PEAK_ANGLES]
    print(f"\n=== Block R3-PEAK: {len(jobs)} calls "
          f"({list(dg.R3_CONFIGS)} x {dg.PEAK_ANGLES}) ===", flush=True)
    t0, n = time.time(), 0
    out = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, c, dt in ex.map(_r3_peak_one, jobs):
            out[(key, th)] = c
            n += 1
            print(f"  [R3-PEAK {n}/{len(jobs)}] {key} theta={th:+05.1f} ({dt:5.1f}s)",
                  flush=True)
    assert n == len(jobs)
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "values": out}


# ===================================================== Block SETTLE-C60C70
def block_settle_c60c70():
    jobs = [(k, th) for k in dg.SETTLE_C60C70_CONFIGS for th in dg.SETTLE_C60C70_ANGLES]
    print(f"\n=== Block SETTLE-C60C70: {len(jobs)} calls "
          f"({dg.SETTLE_C60C70_CONFIGS} x {dg.SETTLE_C60C70_ANGLES}, "
          f"STEPS={dg.STEPS_STRESS}) ===", flush=True)
    t0, n = time.time(), 0
    out = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, c, dt in ex.map(_settle_one, jobs):
            out[(key, th)] = c
            n += 1
            print(f"  [SETTLE {n}/{len(jobs)}] {key} theta={th:+05.1f} ({dt:5.1f}s)",
                  flush=True)
    assert n == len(jobs)
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "values": out}


# ===================================================== gate G1
def gate_g1(g1_values):
    exp069 = dg.load_exp069_dense()
    by_theta = {r["theta"]: r for r in exp069}
    checks = []
    for key in ("C40", "C80"):
        for th in dg.G1_ANGLES:
            ours = g1_values[(key, th)]
            ref = by_theta[th][f"C_empty_{key}"]
            d = ours - ref
            checks.append({"config": key, "theta": th, "ours": ours,
                           "ref": ref, "delta": d, "exact": d == 0.0})
    return {"n_checked": len(checks), "all_exact": all(c["exact"] for c in checks),
            "max_abs_delta": max((abs(c["delta"]) for c in checks), default=None),
            "checks": checks}


# ===================================================== per-config free period
def per_config_free_periods(dense_causal_rows):
    """P-071-1: free-period search on EACH config's own C_empty(theta)
    series -- identical call signature to exp-070's item_a_per_config_
    decomposition (imported dg._free_period_search, center_deg=39.0
    default)."""
    exp069 = dg.load_exp069_dense()
    thetas069 = np.array([r["theta"] for r in exp069])
    out = {}
    for key in ("C40", "C80"):
        series = np.array([r[f"C_empty_{key}"] for r in exp069])
        free = dg._free_period_search(thetas069, series)
        out[key] = dict(p_star_deg=free["p_star_deg"], r_squared=free["r_squared"])
    for key in dg.DENSE_CAUSAL_CONFIGS:
        rows = dense_causal_rows[key]
        thetas = np.array([r["theta"] for r in rows])
        series = np.array([r["C_empty"] for r in rows])
        free = dg._free_period_search(thetas, series)
        out[key] = dict(p_star_deg=free["p_star_deg"], r_squared=free["r_squared"])
    return out


# ===================================================== P-071-2/3: trend + pairwise
def score_trend_and_pairs(per_config):
    keys = ("C40", "C60", "C70", "C80")
    absorb = np.array([dg.ABSORB_DEPTHS[k] for k in keys], dtype=float)
    p_star = np.array([per_config[k]["p_star_deg"] for k in keys])

    # linear fit P*(ABSORB)
    X = np.column_stack([np.ones_like(absorb), absorb])
    coef, *_ = np.linalg.lstsq(X, p_star, rcond=None)
    yhat = X @ coef
    ss_res = float(np.sum((p_star - yhat) ** 2))
    ss_tot = float(np.sum((p_star - np.mean(p_star)) ** 2))
    r2_trend = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0

    spread_40_80 = abs(p_star[keys.index("C80")] - p_star[keys.index("C40")]) / np.mean(p_star)
    trend_resolution_ratio = dg.rayleigh_resolution_ratio(
        p_star[keys.index("C40")], p_star[keys.index("C80")])
    # Mandatory fix 2 (Red Team's Phase-5 final audit): rayleigh_resolution_
    # ratio()'s own docstring promises an exact-tie pair (+inf) is "treated
    # as unresolved by the caller, never as a false REFUTE" -- the original
    # `ratio >= THRESHOLD` comparison did not special-case infinity
    # (`float("inf") >= 1.0` is True in Python), the documented-opposite
    # value. isfinite() guard applied here and below, matching the contract.
    trend_resolved = math.isfinite(trend_resolution_ratio) and \
        trend_resolution_ratio >= dg.RESOLUTION_FLOOR_RATIO_THRESHOLD

    # pairwise table, all 6 pairs, each with its own resolution ratio
    pairs = []
    for i in range(4):
        for j in range(i + 1, 4):
            ka, kb = keys[i], keys[j]
            pa, pb = per_config[ka]["p_star_deg"], per_config[kb]["p_star_deg"]
            spread = abs(pa - pb) / ((pa + pb) / 2.0)
            ratio = dg.rayleigh_resolution_ratio(pa, pb)
            pairs.append(dict(pair=f"{ka}-{kb}", p_a=pa, p_b=pb, spread=spread,
                              resolution_ratio=ratio,
                              resolved=bool(math.isfinite(ratio)
                                           and ratio >= dg.RESOLUTION_FLOOR_RATIO_THRESHOLD)))
    max_pair_spread = max(p["spread"] for p in pairs)
    all_pairs_resolved = all(p["resolved"] for p in pairs)

    raw_confirm = (spread_40_80 >= dg.TREND_CONFIRM_MIN_SPREAD
                   and r2_trend >= dg.TREND_CONFIRM_MIN_R2)
    raw_refute = (max_pair_spread <= dg.TREND_REFUTE_MAX_PAIR_SPREAD
                  and r2_trend <= dg.TREND_REFUTE_MAX_R2)

    # mandatory fix 2: gate BOTH directions by the resolution floor
    confirm = bool(raw_confirm and trend_resolved)
    refute = bool(raw_refute and all_pairs_resolved)
    unresolved_only = bool((raw_confirm and not trend_resolved)
                           or (raw_refute and not all_pairs_resolved))

    return dict(
        per_config=per_config, absorb=absorb.tolist(), p_star=p_star.tolist(),
        linear_fit=dict(intercept=float(coef[0]), slope=float(coef[1]), r_squared=r2_trend),
        spread_40_80=float(spread_40_80),
        trend_resolution_ratio=float(trend_resolution_ratio),
        trend_resolved=bool(trend_resolved),
        max_pair_spread=float(max_pair_spread),
        all_pairs_resolved=bool(all_pairs_resolved),
        pairs=pairs,
        raw_confirm=bool(raw_confirm), raw_refute=bool(raw_refute),
        confirm=confirm, refute=refute, unresolved_only=unresolved_only,
    )


# ===================================================== P-071-4/5: peak R3
def _peak_r3_check(delta_native_by_theta, r3_values, key_a_r3, key_b_r3):
    """Generic peak-cell R3 check: does delta(theta) survive cpl 20->30 at
    the PEAK angles? key_a_r3/key_b_r3 are the two R3-config keys whose
    difference reproduces delta_native's own (a-b) convention."""
    cells = []
    for th in dg.PEAK_ANGLES:
        d_native = delta_native_by_theta[th]
        d_r3 = r3_values[(key_a_r3, th)] - r3_values[(key_b_r3, th)]
        same_sign = (d_native > 0) == (d_r3 > 0)
        ratio_r3 = d_r3 / d_native if d_native != 0 else float("inf")
        cells.append(dict(theta=th, delta_native=d_native, delta_r3=d_r3,
                          same_sign=bool(same_sign), ratio=ratio_r3))
    confirm = all(c["same_sign"] and dg.R3_CONFIRM_RATIO_BAND[0] <= c["ratio"] <= dg.R3_CONFIRM_RATIO_BAND[1]
                  for c in cells)
    refute = any((not c["same_sign"])
                 or not (dg.R3_REFUTE_RATIO_BAND[0] <= c["ratio"] <= dg.R3_REFUTE_RATIO_BAND[1])
                 for c in cells)
    return dict(cells=cells, confirm=bool(confirm), refute=bool(refute))


# ===================================================== Block SETTLE-C60C70 scoring
def score_settle_c60c70(dense_causal_rows, settle_values):
    """37.2/41.4deg are off the coarse angle grid exp-065's own committed
    STEPS=1400 data covers -- there is no 1400-STEPS comparator at these
    exact cells, so this cycle's own new settling check is scored on the
    ABSOLUTE 2800-vs-4200 shift relative to GATE_HARD (the program's own
    instrument-floor scale), not a 1400-anchored relative percentage. This
    is a genuinely new construction (Block SETTLE-C60C70 has no precedent
    cell to inherit a 1400 value from), disclosed explicitly here rather
    than silently substituted -- CONFIRM requires the shift to sit at or
    below the instrument floor itself (a settled channel should not move
    by more than the floor when STEPS is pushed 50% further)."""
    cells = []
    for key in dg.SETTLE_C60C70_CONFIGS:
        rows_by_theta = {r["theta"]: r["C_empty"] for r in dense_causal_rows[key]}
        for th in dg.SETTLE_C60C70_ANGLES:
            c2800 = rows_by_theta[th]
            c4200 = settle_values[(key, th)]
            d_42_28 = abs(c4200 - c2800)
            # 1400-basis reference: use the 2800-vs-4200 SHIFT's own scale
            # if a 1400 value is not available at this exact off-grid
            # theta (37.2/41.4 are NOT on exp-065's coarse angle grid) --
            # report the absolute shift and, where a 1400 comparator
            # exists, the relative figure; else relative is N/A and the
            # cell is scored on the absolute shift against GATE_HARD-scale
            # only (disclosed, not silently defaulted).
            cells.append(dict(config=key, theta=th, C_2800=c2800, C_4200=c4200,
                              abs_delta_4200_2800=d_42_28))
    # Relative scoring vs GATE_HARD (the program's own instrument-floor
    # scale) since 37.2/41.4deg have no committed 1400-STEPS comparator on
    # this off-grid angle pair -- disclosed explicitly, not a silent
    # substitution (this cycle's own new construction, stated as such).
    gate_hard = dg.dg065.GATE_HARD
    for c in cells:
        c["rel_to_gate_hard"] = c["abs_delta_4200_2800"] / gate_hard
    confirm = all(c["rel_to_gate_hard"] <= 1.0 for c in cells)   # shift <= 1x instrument floor
    refute = any(c["rel_to_gate_hard"] >= 5.0 for c in cells)    # shift >= 5x instrument floor
    return dict(cells=cells, gate_hard=gate_hard, confirm=bool(confirm), refute=bool(refute))


# ===================================================== main
def main():
    t_start = time.time()
    print(FROZEN_PREDICTIONS, flush=True)
    print(assert_lab_clean(), flush=True)

    g1 = block_g1()
    g1_gate = gate_g1(g1["values"])
    assert g1_gate["all_exact"], f"P-071-G1 FAILED: {g1_gate}"
    print(f"\nP-071-G1 PASSED: {g1_gate['n_checked']}/{g1_gate['n_checked']} exact",
          flush=True)

    dense_causal = block_dense_causal()
    r3_peak = block_r3_peak()
    settle = block_settle_c60c70()

    per_config = per_config_free_periods(dense_causal["rows"])
    trend = score_trend_and_pairs(per_config)

    exp069_dense_by_theta = {r["theta"]: r for r in dg.load_exp069_dense()}
    delta_c80_c40_native = {th: exp069_dense_by_theta[th]["delta"] for th in dg.PEAK_ANGLES}
    p071_4 = _peak_r3_check(delta_c80_c40_native, r3_peak["values"], "C80_R3", "C40_R3")

    dense_causal_by_theta = {k: {r["theta"]: r["C_empty"] for r in dense_causal["rows"][k]}
                             for k in dg.DENSE_CAUSAL_CONFIGS}
    delta_c70_c60_native = {th: dense_causal_by_theta["C70"][th] - dense_causal_by_theta["C60"][th]
                            for th in dg.PEAK_ANGLES}
    p071_5 = _peak_r3_check(delta_c70_c60_native, r3_peak["values"], "C70_R3", "C60_R3")

    settle_scored = score_settle_c60c70(dense_causal["rows"], settle["values"])

    preconditions_pass = (g1_gate["all_exact"] and settle_scored["confirm"]
                          and p071_4["confirm"])
    # Mandatory fix 4 (Red Team's Phase-5 final audit): all three caveats
    # are appended UNIFORMLY to every branch's combined_reason, not just a
    # partial subset per branch (the original wiring gave CONFIRMED 1-of-3,
    # REFUTED 0-of-3, NEITHER 1-of-3 -- non-load-bearing for what actually
    # printed this run, since it landed NEITHER, but a real gap for any
    # future CONFIRMED/REFUTED outcome reusing this file).
    ALL_CAVEATS = " ".join((ABSORB_NOT_MATERIAL_CAVEAT, THERMO_SCOPE_CAVEAT,
                            WAVELENGTH_SCOPE_CAVEAT, PAD_CONFOUND_CAVEAT))
    if trend["confirm"] and preconditions_pass:
        combined = "CONFIRMED_ABSORB_TIED_NUMERICAL_BOUNDARY_EFFECT"
        combined_reason = (
            "All binding preconditions hold (G1 identity gate, Block "
            "SETTLE-C60C70 settled, P-071-4 resolution-robust) AND the "
            "P*(ABSORB) trend clears the CONFIRM band above its own "
            "Rayleigh resolution floor. " + ALL_CAVEATS)
    elif trend["refute"] and preconditions_pass:
        combined = "REFUTED_SHARED_GEOMETRY_NOT_ABSORB_TIED"
        combined_reason = (
            "All binding preconditions hold AND the pairwise spread "
            "clears the REFUTE band with every pair independently above "
            "its own Rayleigh resolution floor -- genuine evidence the "
            "compound ABSORB/PAD axis (PAD=ABSORB-40 exactly across this "
            "congruent series -- see the PAD-confound caveat) is flat, "
            "not floor-limited indistinguishability. " + ALL_CAVEATS)
    else:
        combined = "NEITHER"
        reasons = []
        if not g1_gate["all_exact"]:
            reasons.append("G1 identity gate failed")
        if not settle_scored["confirm"]:
            reasons.append("Block SETTLE-C60C70 did not confirm settling")
        if not p071_4["confirm"]:
            reasons.append("P-071-4 peak-cell R3 check did not confirm resolution-robustness")
        if trend["unresolved_only"]:
            reasons.append("trend statistic sits below its own Rayleigh resolution floor "
                          f"(trend_resolved={trend['trend_resolved']}, "
                          f"all_pairs_resolved={trend['all_pairs_resolved']})")
        if not reasons:
            reasons.append("raw trend statistic (spread/R^2) landed in the gray zone "
                          "between the CONFIRM and REFUTE bands, on the pre-registered "
                          "thresholds ALONE -- independent of the resolution-floor gate "
                          "below, which was correctly computed but was NOT the proximate "
                          "cause of this branch firing (Red Team's Phase-5 final audit, "
                          "mandatory fix 1: raw_confirm/raw_refute both already False)")
        combined_reason = ("Explicit NEITHER branch (not a silent PARTIAL escape "
                          "hatch): " + "; ".join(reasons) + ". " + ALL_CAVEATS)

    total_calls = (g1["n_new_runs"] + dense_causal["n_new_runs"]
                  + r3_peak["n_new_runs"] + settle["n_new_runs"])
    total_elapsed = time.time() - t_start

    out = {
        "experiment": "071-t28-absorb-depth-causal-test",
        "panel_iteration": 48,
        "lead_seat": "VISION SCIENCE",
        "t1_escape_route": "N/A (instrument/mechanism-identification class)",
        "steps_settled": dg.STEPS_SETTLED, "steps_stress": dg.STEPS_STRESS,
        "r3_steps": dg.R3_STEPS, "r3_ratio": dg.R3_RATIO,
        "dense_angles": list(dg.DENSE_ANGLES), "peak_angles": list(dg.PEAK_ANGLES),
        "g1": {"n_new_runs": g1["n_new_runs"], "elapsed_s": g1["elapsed_s"],
              "gate": g1_gate},
        "dense_causal": {"n_new_runs": dense_causal["n_new_runs"],
                         "elapsed_s": dense_causal["elapsed_s"],
                         "rows": dense_causal["rows"]},
        "r3_peak": {"n_new_runs": r3_peak["n_new_runs"], "elapsed_s": r3_peak["elapsed_s"],
                   "values": {f"{k}|{th}": v for (k, th), v in r3_peak["values"].items()}},
        "settle_c60c70": {"n_new_runs": settle["n_new_runs"], "elapsed_s": settle["elapsed_s"],
                          "scored": settle_scored},
        "per_config_free_periods": per_config,
        "trend": trend,
        "p071_4_peak_r3": p071_4,
        "p071_5_peak_r3_interior": p071_5,
        "combined_verdict": combined,
        "combined_reason": combined_reason,
        "caveats": {"absorb_not_material": ABSORB_NOT_MATERIAL_CAVEAT,
                   "thermo_scope": THERMO_SCOPE_CAVEAT,
                   "wavelength_scope": WAVELENGTH_SCOPE_CAVEAT,
                   "pad_confound": PAD_CONFOUND_CAVEAT},
        "total_new_runs": total_calls,
        "total_elapsed_s": total_elapsed,
        "r_contact_disposition": ("UNTOUCHED this cycle -- PLAN.md's Iteration-48 "
                                  "queue item #2 remains blocked on WebSearch/"
                                  "WebFetch tooling per this cycle's own scope "
                                  "(item 1 is the locked mandate); Phase 1's "
                                  "tooling-availability disclosure is carried "
                                  "forward to phase3_synthesis.md for the "
                                  "Director to act on, not acted on here."),
    }

    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=float)

    print(f"\n=== DONE: {total_calls} FDTD calls, {total_elapsed:.1f}s "
          f"({total_elapsed/60:.2f} min) ===", flush=True)
    print(f"Per-config P*: " +
          "  ".join(f"{k}={per_config[k]['p_star_deg']:.4f}deg(R2={per_config[k]['r_squared']:.3f})"
                    for k in ("C40", "C60", "C70", "C80")), flush=True)
    print(f"Trend: slope={trend['linear_fit']['slope']:.6f} "
          f"R2={trend['linear_fit']['r_squared']:.4f} "
          f"spread_40_80={trend['spread_40_80']:.4f} "
          f"trend_resolved={trend['trend_resolved']} "
          f"max_pair_spread={trend['max_pair_spread']:.4f} "
          f"all_pairs_resolved={trend['all_pairs_resolved']}", flush=True)
    print(f"Block SETTLE-C60C70: confirm={settle_scored['confirm']} "
          f"refute={settle_scored['refute']}", flush=True)
    print(f"P-071-4 (peak R3, C80-C40): confirm={p071_4['confirm']} "
          f"refute={p071_4['refute']}", flush=True)
    print(f"P-071-5 (peak R3, C70-C60, disclosed): confirm={p071_5['confirm']} "
          f"refute={p071_5['refute']}", flush=True)
    print(f"\nCOMBINED VERDICT: {combined}", flush=True)
    print(combined_reason, flush=True)

    return out


if __name__ == "__main__":
    main()
