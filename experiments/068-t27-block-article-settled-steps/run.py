"""exp-068 -- Block ARTICLE Settled-STEPS Re-Verification (T27 closure, part 2):
measurement harness.
=============================================================================
Panel Iteration 45 (lead: ELECTROMAGNETISM, rotation; synthesis: Director,
post Red Team's PROCEED-WITH-MANDATORY-FIXES verdict -- see
`phase3_synthesis.md` for the full accepted/overridden record and the
7-item mandatory-fix docket, zero overrides) -- PLUS two Director build-time
corrections, self-caught while implementing this file (disclosed here and
in NOTES.md, not silently fixed, per this program's own R4 discipline):

  BUILD-TIME CORRECTION 1: the Phase-3 synthesis (and every one of the six
  Phase-1/2 seats) assumed the +-35deg empty-scene companions needed for
  the N9 aggregate (P-068-1/2/3) could be CITED from exp-065's own
  `settled_sweep_steps2800_diagnostic.json` at zero marginal FDTD cost.
  That file stores only the REDUCED SCALAR C_empty = weber(obj_mean,
  flank_mean) for each cell -- `lab.ambient.contrast_from_runs`'s N9
  aggregate needs the RAW PROFILE for each of the 9 angles (the per-angle
  flank-mean normalization inside `incoherent_sum` does not reduce to a
  function of the scalar C_empty alone once >=2 angles with different
  flank levels are combined). A scalar citation cannot reconstruct a raw
  profile. New Tier0b block added: 4 calls (+-35deg x 600nm x {C40,C80},
  empty scene, STEPS=2800) -- the true marginal cost of this leg.

  BUILD-TIME CORRECTION 2: the Phase-1 proposal's P-068-4 ("750nm +-35deg
  bracket vs 600nm +-35deg bracket, predict 750nm shift LARGER") implicitly
  assumed a STEPS=1400 baseline exists for article-present readings at
  750nm. It does not: exp-065's own Block ARTICLE was 600nm-only (its own
  run.py docstring: "N9 FALLBACK @600nm"), and exp-065's results.json
  stores only the N9-AGGREGATE STEPS=1400 baseline (per_config C/C_empty),
  never a per-angle breakdown -- so no single-angle STEPS=1400 baseline
  exists at ANY wavelength for Block ARTICLE. P-068-4 is reformulated
  below to compare Tier2's own within-cycle STEPS=4200-vs-2800 convergence
  ratio between the two wavelengths (both computed this cycle, no external
  baseline needed) rather than a nonexistent cross-STEPS delta at 750nm.

Five FDTD blocks, 44 new calls total (ceiling 45), reusing exp-065's own
harness verbatim (no `lab/` engine change):

  Tier0  (mandatory floor, article): article-present, +-35deg x
         {600,750}nm x {C40,C80}, STEPS=2800                     =  8 calls
  Tier0b (mandatory floor, empty -- BUILD-TIME CORRECTION 1): empty
         scene, +-35deg x 600nm x {C40,C80}, STEPS=2800          =  4 calls
  Tier1a (N9 recert, article): article-present, 7 interior angles
         (0,+-5,+-15,+-25) x {C40,C80} x 600nm, STEPS=2800       = 14 calls
  Tier1b (N9 recert, empty):  empty scene, 7 interior angles x
         {C40,C80} x 600nm, STEPS=2800                           = 14 calls
  Tier2  (convergence-generalization stress): article-present,
         theta=-35deg x {600,750}nm x {C40,C80}, STEPS=4200
         (vs Tier0's own STEPS=2800 value at the same cell)      =  4 calls
  TOTAL: 44 new FDTD calls. Tier0+Tier0b+Tier2 together are the mandatory
  floor -- never de-scoped. If a hard-stop is approached, Tier1b is
  trimmed first, then Tier1a (both lower-stakes than the mandate's own
  named minimum scope).

Predictions (P-068-0 through P-068-6, plus the REALIZABILITY_MEMO
contingency check) committed in NOTES.md BEFORE this file's first run
(house discipline, non-negotiable), and printed structurally below before
the first FDTD call (exp-046/exp-065/exp-066's own structural-freeze
precedent).
"""

import importlib.util
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, REPO_ROOT)
sys.path.insert(0, HERE)

import design_geometry as dg           # exp-068's own thin wrapper

HARD_STOP_S = 30 * 60          # pre-registered wall-clock hard stop

# ---------------------------------------------------- load exp-065's own harness
# Same module-collision-avoidance pattern exp-066 established.
_EXP065_DIR = os.path.join(HERE, "..", "065-t24-absorb-boundary-sweep")
_saved_dg_module = sys.modules.get("design_geometry")
sys.modules["design_geometry"] = dg.dg065
_spec = importlib.util.spec_from_file_location(
    "_exp065_run", os.path.join(_EXP065_DIR, "run.py"))
R = importlib.util.module_from_spec(_spec)
sys.modules["_exp065_run"] = R
_spec.loader.exec_module(R)
if _saved_dg_module is not None:
    sys.modules["design_geometry"] = _saved_dg_module
else:
    sys.modules.pop("design_geometry", None)


# ================================================== structural freeze print
FROZEN_PREDICTIONS = """
P-068-0   harness-continuity gate: this cycle's new worker reproduces an
          already-settled empty cell (C40,-35,600,STEPS=2800) through
          R._one_run/_profile + this file's own _c_self, bit-exact vs
          settled_sweep_steps2800_diagnostic.json's committed scalar
          CONFIRM delta == 0.0 (float64) | REFUTE any nonzero -- HALTS
P-068-1   empty N9 floor, settled STEPS=2800, 600nm, both configs
          CONFIRM |C_empty,N9(2800)| <= GATE_HARD=0.001 both configs
          REFUTE  either breaches GATE_HARD
          (mandatory fix 5: does NOT by itself move any constraint-3
          verdict -- see GATE_HARD_M3_NOTE)
P-068-2   article row C, N9, 600nm, settled(2800) vs STEPS=1400 baseline
          (exp-065 results.json::block_article::per_config, loaded
          programmatically, never hand-typed -- R4)
          CONFIRM |dC| <= 1.5e-3 per config, bucket stays MARGINAL both,
                  sign stays negative
          REFUTE  |dC| > 4e-3 either config, OR bucket disagreement
                  reappears between C40/C80
          Pre-registered flip (MARGINAL band |C| in [0.0025,0.01]): flip
          to PASS requires C > -0.0025 (past MARGINAL_LO); flip to FAIL
          requires C < -0.01 (past MARGINAL_HI-equivalent on the negative
          side) -- see REALIZABILITY_MEMO_PASS_FLIP_NOTE if PASS fires.
P-068-3   sign persistence: C(article,N9,600nm) stays negative, both
          configs, at settled STEPS
          CONFIRM stays negative both | REFUTE sign flips either
P-068-4   [REFORMULATED, build-time correction 2 -- see module docstring]
          750nm vs 600nm relative convergence: |C(4200)-C(2800)| at
          theta=-35, article-present, using ONLY this cycle's own Tier0/
          Tier2 data (no external STEPS=1400 baseline needed, since none
          exists at 750nm article-present)
          CONFIRM 750nm's |dC(4200-2800)| exceeds 600nm's at BOTH configs
                  (consistent with the empty-channel's own established
                  pattern that 750nm carries more unconverged residual)
          REFUTE  750nm's is smaller than 600nm's at BOTH configs
P-068-5   GATE_HARD count, 14 new interior empty legs (Tier1b), 600nm,
          per-angle (NOT the N9 aggregate)
          CONFIRM >=12/14 pass GATE_HARD at 2800 | REFUTE <=7/14 pass
          NOTE: per mandatory fix 5, this does NOT by itself move any
          constraint-3 verdict -- see GATE_HARD_M3_NOTE.
P-068-6   convergence-generalization stress (Tier2), all 4 cells
          (theta=-35, {600,750}nm x {C40,C80}, STEPS=4200 vs 2800):
          CONFIRM |dC(4200-2800)| <= 0.01 x |C(2800)| at all 4 cells
                  (relative to the STEPS=2800 reading itself, since no
                  STEPS=1400 baseline exists to form the denominator
                  exp-066's own P-066-3a/3b used)
          REFUTE  ratio >= 0.05 at any of the 4 cells
"""


def _lab_diff_excluding_registry():
    """No `lab/` ENGINE diff -- mandatory fix 7 (Red Team's own Attack 6)
    disclosed-ly widens exactly one entry in lab/caveat_lint_config.json,
    applied and verified live BEFORE this predict-commit (see
    phase3_synthesis.md), same precedent as exp-066's own mandatory fix D."""
    out = subprocess.run(
        ["git", "diff", "--stat", "--", "lab/", ":!lab/caveat_lint_config.json"],
        cwd=REPO_ROOT, capture_output=True, text=True).stdout.strip()
    assert out == "", f"lab/ engine code is dirty -- the no-new-machinery position fails:\n{out}"
    return "clean (lab/caveat_lint_config.json intentionally excluded, see above)"


# ===================================================== worker entry point
def _article_settle_one(args):
    """Composes exp-065's own _article_one (sigma-injection) with
    _settle_one (STEPS parameter) -- both existing patterns, no new
    physics: R._one_run already accepts both `sigma` and `steps` as
    independent keyword arguments (exp-065 run.py, `_one_run` signature),
    so this worker is a direct, unmodified call through exp-065's own
    harness. `article=False` runs the empty scene (sigma=None)."""
    key, theta, lam, steps, article = args
    cfg = R.dg.CONFIGS[key]
    t0 = time.time()
    sigma = dg.SIGMA_OFF_PASS if article else None
    cap = R._one_run(cfg, R.dg.CPL[lam], theta, sigma=sigma, steps=steps)
    return (key, theta, lam, steps, article, R._profile(cap, cfg), time.time() - t0)


def _c_self(profile, cfg):
    """weber(obj_mean, flank_mean) of ONE profile against itself -- exactly
    what exp-065's own `_c_empty` computes (the name refers to its usual
    calling context, an empty-scene profile, but the reduction is
    content-agnostic: `amb.contrast_from_runs`'s per-component flank
    normalization cancels exactly in the Weber ratio for a single-profile
    call, verified directly from `lab/ambient.py`'s own `incoherent_sum`/
    `weber` definitions before this file was written -- see NOTES.md
    Idealization 10). Applied to an ARTICLE profile, this yields that
    angle's own single-run article contrast; applied to an EMPTY profile,
    it yields the instrument-floor reading GATE_HARD scores."""
    return R._c_empty(profile, cfg)


# ===================================================== gate P-068-0
def gate_harness_continuity(tier0b_profiles):
    """Bit-exact reproduction, through this cycle's OWN new worker, of an
    already-settled EMPTY cell exp-065 already committed
    (settled_sweep_steps2800_diagnostic.json, C40|-35.0|600) -- consumes
    Tier0b's own C40/-35deg profile (zero extra FDTD calls)."""
    key, theta, lam = "C40", -35.0, 600
    prof = tier0b_profiles[(key, theta)]
    ours = _c_self(prof, R.dg.CONFIGS[key])
    settled = json.load(open(dg.EXP065_SETTLED_JSON))
    theirs = settled[f"{key}|{theta}|{lam}"]
    delta = ours - theirs
    return {"config": key, "theta": theta, "lambda_nm": lam, "steps": dg.STEPS_LONG,
            "ours": ours, "settled_sweep_2800": theirs, "delta": delta,
            "exact": delta == 0.0}


# ===================================================== Tier0 -- article, +-35deg
def block_tier0():
    jobs = [(k, th, lam, dg.STEPS_LONG, True)
            for k in dg.CONFIGS for th in dg.TIER0_ANGLES for lam in dg.TIER0_LAMBDAS]
    print(f"\n=== Tier0 (mandatory floor, article-present): "
          f"{dg.TIER0_ANGLES} x {dg.TIER0_LAMBDAS} x {tuple(dg.CONFIGS)}, "
          f"STEPS={dg.STEPS_LONG} = {len(jobs)} calls ===", flush=True)
    t0 = time.time()
    profiles, n = {}, 0
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, lam, steps, art, prof, dt in ex.map(_article_settle_one, jobs):
            profiles[(key, th, lam)] = prof
            n += 1
            print(f"  [TIER0 {n}/{len(jobs)}] {key} theta={th:+05.1f} lam={lam} "
                  f"({dt:5.1f}s)", flush=True)
    assert n == len(jobs), f"Tier0 run-count mismatch: {n} != {len(jobs)}"
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "profiles": profiles}


# ===================================================== Tier0b -- empty, +-35deg
def block_tier0b():
    jobs = [(k, th, dg.TIER1_LAMBDA, dg.STEPS_LONG, False)
            for k in dg.CONFIGS for th in dg.TIER0_ANGLES]
    print(f"\n=== Tier0b (mandatory floor, empty scene -- build-time "
          f"correction 1): {dg.TIER0_ANGLES} x {dg.TIER1_LAMBDA}nm x "
          f"{tuple(dg.CONFIGS)}, STEPS={dg.STEPS_LONG} = {len(jobs)} calls ===",
          flush=True)
    t0 = time.time()
    profiles, n = {}, 0
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, lam, steps, art, prof, dt in ex.map(_article_settle_one, jobs):
            profiles[(key, th)] = prof
            n += 1
            print(f"  [TIER0b {n}/{len(jobs)}] {key} theta={th:+05.1f} "
                  f"({dt:5.1f}s)", flush=True)
    assert n == len(jobs), f"Tier0b run-count mismatch: {n} != {len(jobs)}"
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "profiles": profiles}


# ===================================================== Tier1a -- article, interior
def block_tier1a():
    jobs = [(k, th, dg.TIER1_LAMBDA, dg.STEPS_LONG, True)
            for k in dg.CONFIGS for th in dg.INTERIOR_ANGLES]
    print(f"\n=== Tier1a (N9 recert, article-present): "
          f"{len(dg.INTERIOR_ANGLES)} interior angles x {tuple(dg.CONFIGS)} "
          f"@ {dg.TIER1_LAMBDA}nm, STEPS={dg.STEPS_LONG} = {len(jobs)} calls ===",
          flush=True)
    t0 = time.time()
    profiles, n = {}, 0
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, lam, steps, art, prof, dt in ex.map(_article_settle_one, jobs):
            profiles[(key, th)] = prof
            n += 1
            print(f"  [TIER1a {n:2d}/{len(jobs)}] {key} theta={th:+05.1f} "
                  f"({dt:5.1f}s)", flush=True)
    assert n == len(jobs), f"Tier1a run-count mismatch: {n} != {len(jobs)}"
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "profiles": profiles}


# ===================================================== Tier1b -- empty, interior
def block_tier1b():
    jobs = [(k, th, dg.TIER1_LAMBDA, dg.STEPS_LONG, False)
            for k in dg.CONFIGS for th in dg.INTERIOR_ANGLES]
    print(f"\n=== Tier1b (N9 recert, empty floor): "
          f"{len(dg.INTERIOR_ANGLES)} interior angles x {tuple(dg.CONFIGS)} "
          f"@ {dg.TIER1_LAMBDA}nm, STEPS={dg.STEPS_LONG} = {len(jobs)} calls ===",
          flush=True)
    t0 = time.time()
    profiles, n = {}, 0
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, lam, steps, art, prof, dt in ex.map(_article_settle_one, jobs):
            profiles[(key, th)] = prof
            n += 1
            print(f"  [TIER1b {n:2d}/{len(jobs)}] {key} theta={th:+05.1f} "
                  f"({dt:5.1f}s)", flush=True)
    assert n == len(jobs), f"Tier1b run-count mismatch: {n} != {len(jobs)}"
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "profiles": profiles}


# ===================================================== Tier2 -- convergence stress
def block_tier2():
    jobs = [(k, dg.TIER2_THETA, lam, dg.STEPS_STRESS, True)
            for k in dg.CONFIGS for lam in dg.TIER0_LAMBDAS]
    print(f"\n=== Tier2 (convergence-generalization stress): "
          f"theta={dg.TIER2_THETA} x {dg.TIER0_LAMBDAS} x {tuple(dg.CONFIGS)}, "
          f"STEPS={dg.STEPS_STRESS} = {len(jobs)} calls ===", flush=True)
    t0 = time.time()
    profiles, n = {}, 0
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, lam, steps, art, prof, dt in ex.map(_article_settle_one, jobs):
            profiles[(key, lam)] = prof
            n += 1
            print(f"  [TIER2 {n}/{len(jobs)}] {key} lam={lam} steps={steps} "
                  f"({dt:5.1f}s)", flush=True)
    assert n == len(jobs), f"Tier2 run-count mismatch: {n} != {len(jobs)}"
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "profiles": profiles}


# ===================================================== N9 aggregate composition
def n9_aggregate(key, tier0, tier0b, tier1a, tier1b):
    """The full 9-angle N9 aggregate at 600nm for one config, via exp-065's
    own R._c_n9 unmodified -- article and empty profile lists, in
    FALLBACK_ANGLES order, matched angle-for-angle."""
    order = [float(t) for t in dg.FALLBACK_ANGLES]
    art_list, emp_list = [], []
    for th in order:
        if abs(th) == 35:
            art_list.append(tier0["profiles"][(key, th, 600)])
            emp_list.append(tier0b["profiles"][(key, th)])
        else:
            art_list.append(tier1a["profiles"][(key, th)])
            emp_list.append(tier1b["profiles"][(key, th)])
    c, c_empty = R._c_n9(art_list, emp_list, R.dg.CONFIGS[key])
    return c, c_empty


# ===================================================== scoring
def score_all(tier0, tier0b, tier1a, tier1b, tier2):
    baseline = json.load(open(dg.EXP065_RESULTS))["block_article"]["per_config"]

    n9 = {key: n9_aggregate(key, tier0, tier0b, tier1a, tier1b) for key in dg.CONFIGS}

    # ---- P-068-1: empty N9 floor
    p1_rows = {}
    for key in dg.CONFIGS:
        c_empty = n9[key][1]
        p1_rows[key] = {"C_empty_N9": c_empty, "abs": abs(c_empty),
                         "pass_gate_hard": abs(c_empty) <= dg.GATE_HARD}
    p1 = {"rows": p1_rows, "note": dg.GATE_HARD_M3_NOTE}
    p1["confirm"] = all(r["pass_gate_hard"] for r in p1_rows.values())
    p1["refute"] = not p1["confirm"]
    p1["verdict"] = "CONFIRMED" if p1["confirm"] else "REFUTED"

    # ---- P-068-2/3: article row C, N9, settled vs 1400 baseline
    # MARGINAL_LO/MARGINAL_HI are MULTIPLIERS on C_THR_LAB (0.5x/2.0x), per
    # lab/glare_sidecar.py::tier_w_verdict -- the absolute band is
    # [0.0025, 0.01], NOT [MARGINAL_LO, MARGINAL_HI] taken literally.
    marginal_lo_abs = dg.MARGINAL_LO * dg.C_THR_LAB   # 0.0025
    marginal_hi_abs = dg.MARGINAL_HI * dg.C_THR_LAB   # 0.01
    p2_rows, realizability_flip = {}, {}
    for key in dg.CONFIGS:
        c = n9[key][0]
        c1400 = baseline[key]["C"]
        d = c - c1400
        bucket = ("PASS" if abs(c) < marginal_lo_abs
                  else "FAIL" if abs(c) > marginal_hi_abs else "MARGINAL")
        p2_rows[key] = {"C_2800": c, "C_1400": c1400, "delta": d,
                         "abs_delta": abs(d), "sign_negative": c < 0,
                         "bucket": bucket}
        if bucket == "PASS":
            realizability_flip[key] = dg.REALIZABILITY_MEMO_PASS_FLIP_NOTE
    p2 = {"rows": p2_rows,
          "caveats": [dg.REALIZABILITY_MEMO_CAVEAT, dg.G_TRANSFER_T15_CAVEAT,
                      dg.T5_THERMAL_CAVEAT],   # mandatory fix 4, exp-065's own
                                                # P-VIS42-7 precedent, verbatim
          "tier_label": ("BENCH-SCALE SURROGATE ONLY -- no Tier-W/Tier-A "
                         "verdict is issued by this cycle, pending the "
                         "T8/T13/T14 witness-scale bridge (exp-047/exp-065's "
                         "own TIER_W_HEADLINE_LABEL discipline)")}
    p2["confirm"] = (all(r["abs_delta"] <= 1.5e-3 for r in p2_rows.values())
                     and all(r["bucket"] == "MARGINAL" for r in p2_rows.values())
                     and all(r["sign_negative"] for r in p2_rows.values()))
    p2["refute"] = (any(r["abs_delta"] > 4e-3 for r in p2_rows.values())
                    or len({r["bucket"] for r in p2_rows.values()}) > 1)
    p2["verdict"] = ("CONFIRMED" if p2["confirm"] else
                     "REFUTED" if p2["refute"] else "PARTIAL")
    p2["realizability_memo_amendment_needed"] = bool(realizability_flip)
    p2["realizability_flip_detail"] = realizability_flip

    p3 = {"rows": {k: p2_rows[k]["sign_negative"] for k in dg.CONFIGS}}
    p3["confirm"] = all(p2_rows[k]["sign_negative"] for k in dg.CONFIGS)
    p3["refute"] = not p3["confirm"]
    p3["verdict"] = "CONFIRMED" if p3["confirm"] else "REFUTED"

    # ---- P-068-5: GATE_HARD count, 14 interior empty legs, per-angle
    p5_rows = []
    n_pass = 0
    for key in dg.CONFIGS:
        for th in dg.INTERIOR_ANGLES:
            c = _c_self(tier1b["profiles"][(key, th)], R.dg.CONFIGS[key])
            ok = abs(c) <= dg.GATE_HARD
            n_pass += int(ok)
            p5_rows.append({"config": key, "theta": th, "C_empty": c,
                            "pass_gate_hard": ok})
    p5 = {"rows": p5_rows, "n_pass": n_pass, "n_total": len(p5_rows),
          "note": dg.GATE_HARD_M3_NOTE}
    p5["confirm"] = n_pass >= 12
    p5["refute"] = n_pass <= 7
    p5["verdict"] = ("CONFIRMED" if p5["confirm"] else
                     "REFUTED" if p5["refute"] else "PARTIAL")

    # ---- P-068-6 (+ P-068-4, reformulated): Tier2 convergence, per cell
    p6_rows = {}
    for key in dg.CONFIGS:
        for lam in dg.TIER0_LAMBDAS:
            c2800 = _c_self(tier0["profiles"][(key, dg.TIER2_THETA, lam)],
                            R.dg.CONFIGS[key])
            c4200 = _c_self(tier2["profiles"][(key, lam)], R.dg.CONFIGS[key])
            d = abs(c4200 - c2800)
            ratio = d / abs(c2800) if c2800 else float("inf")
            p6_rows[(key, lam)] = {"config": key, "lambda_nm": lam,
                                   "C_2800": c2800, "C_4200": c4200,
                                   "abs_delta": d, "ratio": ratio}
    p6 = {"rows": {f"{k}_{l}": v for (k, l), v in p6_rows.items()}}
    p6["confirm"] = all(r["ratio"] <= 0.01 for r in p6_rows.values())
    p6["refute"] = any(r["ratio"] >= 0.05 for r in p6_rows.values())
    p6["verdict"] = ("CONFIRMED" if p6["confirm"] else
                     "REFUTED" if p6["refute"] else "PARTIAL")

    p4_rows = {}
    for key in dg.CONFIGS:
        d600 = p6_rows[(key, 600)]["abs_delta"]
        d750 = p6_rows[(key, 750)]["abs_delta"]
        p4_rows[key] = {"abs_delta_600": d600, "abs_delta_750": d750,
                        "750_exceeds_600": d750 > d600}
    p4 = {"rows": p4_rows,
          "note": ("Reformulated per build-time correction 2 -- see module "
                   "docstring: compares Tier0/Tier2's own within-cycle "
                   "STEPS=4200-vs-2800 deltas between wavelengths, NOT a "
                   "cross-STEPS delta at 750nm (no STEPS=1400 article-"
                   "present baseline exists at 750nm anywhere in this "
                   "program's history).")}
    p4["confirm"] = all(r["750_exceeds_600"] for r in p4_rows.values())
    p4["refute"] = not any(r["750_exceeds_600"] for r in p4_rows.values())
    p4["verdict"] = ("CONFIRMED" if p4["confirm"] else
                     "REFUTED" if p4["refute"] else "PARTIAL")

    return {"P-068-1": p1, "P-068-2": p2, "P-068-3": p3, "P-068-4": p4,
            "P-068-5": p5, "P-068-6": p6, "n9": {k: {"C": v[0], "C_empty": v[1]}
                                                  for k, v in n9.items()}}


# ===================================================== main
def main():
    t_start = time.time()
    print("=" * 78)
    print("exp-068 -- T27 Block ARTICLE settled-STEPS re-verification | "
          "Panel Iteration 45")
    print("Lead: ELECTROMAGNETISM (rotation). Director's Phase-3 synthesis "
          "applied in full, plus 2 build-time corrections (see module "
          "docstring).")
    print("=" * 78)
    print("\nFROZEN PREDICTIONS (committed to git in NOTES.md BEFORE this "
          "file's first run):")
    print(FROZEN_PREDICTIONS)
    print(f"\nDEFERRAL DISCLOSURE: {dg.DEFERRAL_DISCLOSURE}")
    print(f"\nT5 THERMAL CAVEAT (mandatory fix 4): {dg.T5_THERMAL_CAVEAT}")
    print(f"\nREALIZABILITY_MEMO CAVEAT (mandatory fix 4): "
          f"{dg.REALIZABILITY_MEMO_CAVEAT}")
    print(f"\nBLOCK MINI TRIPWIRE (nice-to-have fix 8): "
          f"{dg.BLOCK_MINI_TRIPWIRE_NOTE}")
    print(f"\nlab/ engine diff check: {_lab_diff_excluding_registry()}")

    tier0 = block_tier0()
    tier0b = block_tier0b()

    print("\n--- GATE P-068-0: harness-continuity check ---")
    g0 = gate_harness_continuity(tier0b["profiles"])
    print(f"    {g0}")
    assert g0["exact"], "P-068-0 FAILED -- halting before any new number is trusted"

    tier1a = block_tier1a()
    tier1b = block_tier1b()
    tier2 = block_tier2()

    total_runs = (tier0["n_new_runs"] + tier0b["n_new_runs"] + tier1a["n_new_runs"]
                  + tier1b["n_new_runs"] + tier2["n_new_runs"])
    elapsed = time.time() - t_start
    print(f"\n=== {total_runs} new FDTD calls in {elapsed / 60:.1f} min "
          f"(hard stop {HARD_STOP_S / 60:.0f} min) ===")
    assert total_runs == 44, f"run-count mismatch vs frozen budget: {total_runs} != 44"

    sc_ = score_all(tier0, tier0b, tier1a, tier1b, tier2)

    print("\n" + "=" * 78)
    print("SCORED PREDICTIONS")
    print("=" * 78)
    for pid in ("P-068-0", "P-068-1", "P-068-2", "P-068-3", "P-068-4",
                "P-068-5", "P-068-6"):
        if pid == "P-068-0":
            print(f"  {pid:<10} {'PASSED' if g0['exact'] else 'FAILED'}")
            continue
        print(f"  {pid:<10} {sc_[pid]['verdict']}")

    print(f"\nGATE_HARD_M3_NOTE: {dg.GATE_HARD_M3_NOTE}")
    if sc_["P-068-2"]["realizability_memo_amendment_needed"]:
        print("\n*** REALIZABILITY_MEMO.md AMENDMENT NEEDED ***")
        print(sc_["P-068-2"]["realizability_flip_detail"])

    out = {
        "experiment": "exp-068-t27-block-article-settled-steps",
        "panel_iteration": 45, "lead_seat": "ELECTROMAGNETISM",
        "t1_escape_route": "N/A -- instrument/model-fidelity class",
        "steps_base": dg.STEPS_BASE, "steps_long": dg.STEPS_LONG,
        "steps_stress": dg.STEPS_STRESS,
        "gates": {"GATE_HARD": dg.GATE_HARD, "C_THR_LAB": dg.C_THR_LAB,
                  "C_THR_FIELD": dg.C_THR_FIELD,
                  "MARGINAL_BAND": [dg.MARGINAL_LO, dg.MARGINAL_HI]},
        "deferral_disclosure": dg.DEFERRAL_DISCLOSURE,
        "t5_thermal_caveat": dg.T5_THERMAL_CAVEAT,
        "realizability_memo_caveat": dg.REALIZABILITY_MEMO_CAVEAT,
        "g_transfer_t15_caveat": dg.G_TRANSFER_T15_CAVEAT,
        "gate_hard_m3_note": dg.GATE_HARD_M3_NOTE,
        "block_mini_tripwire_note": dg.BLOCK_MINI_TRIPWIRE_NOTE,
        "gate_p068_0_harness_continuity": g0,
        "block_tier0": {k: v for k, v in tier0.items() if k != "profiles"},
        "block_tier0b": {k: v for k, v in tier0b.items() if k != "profiles"},
        "block_tier1a": {k: v for k, v in tier1a.items() if k != "profiles"},
        "block_tier1b": {k: v for k, v in tier1b.items() if k != "profiles"},
        "block_tier2": {k: v for k, v in tier2.items() if k != "profiles"},
        "scored": sc_,
        "total_new_runs": total_runs, "total_elapsed_s": elapsed,
        "build_time_corrections": [
            "1: Tier0b (4 calls) added -- N9 aggregate needs raw empty "
            "profiles, not the cited scalar C_empty; a scalar citation "
            "cannot reconstruct a raw profile for incoherent_sum's "
            "per-component flank normalization.",
            "2: P-068-4 reformulated -- no STEPS=1400 article-present "
            "baseline exists at 750nm (or at any single angle, at any "
            "wavelength) anywhere in this program's history; exp-065's "
            "own results.json stores only the N9-aggregate baseline.",
        ],
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote results.json ({total_runs} runs, {elapsed / 60:.1f} min)")


if __name__ == "__main__":
    main()
