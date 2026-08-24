"""exp-066 -- Settling Re-Verification of exp-041's Block MAIN (T27 closure):
measurement harness.
=============================================================================
Panel Iteration 43 (lead: PHOTONICS, rotation; synthesis: Director, post Red
Team's PROCEED-WITH-MANDATORY-FIXES verdict -- see phase3_synthesis.md for
the full accepted/overridden record and the 5-item (A-E) mandatory-fix
docket, all applied, zero overrides).

Three FDTD blocks (39 new calls total), plus desk-only citation of already-
committed data and a desk-only fringe-fit refit:

  Block G1EXT:     {36,37,39}x{+-}x{450,600,750}, STEPS=1400  = 18 calls
                    (extends exp-065's own G-1 anchor from 12/30 to 30/30
                    exp-041 Block MAIN cells)
  Block MAIN2800:  same 18 cells, STEPS=2800                  = 18 calls
                    (the core deliverable -- closes the gap no committed
                    data anywhere in this program covers beyond STEPS=1400)
  Block STRESS:    40deg/750nm @ STEPS=4200,5600              =  2 calls
                    37deg/600nm @ STEPS=4200 (mandatory fix B) =  1 call
  TOTAL: 39 new FDTD calls, all via exp-065's own CONFIGS["C40"]/_settle_one/
  _c_empty harness (design_geometry.py's `dg065`/`R` -- zero `lab/` engine
  change).

Desk-only (zero new FDTD calls, mandatory fix A): the mandate's own literal
"+-35/38/40deg" text is closed in full by citing exp-065's own already-
committed +-35deg x 3lambda values at BOTH STEPS=1400 (results.json Block
SWEEP) and STEPS=2800 (settled_sweep_steps2800_diagnostic.json), alongside
the already-settled +-38/+-40deg cells from the same two files.

Desk-only (zero new FDTD calls, mandatory fix C): P-066-4 refits exp-042's
own edge-diffraction propagator (`edge_diffraction_c_empty_corrected`)
against the FULL 30-row settled Block MAIN dataset this cycle produces,
STRICTLY as a fit-quality statistic -- no causal/mechanism language, per
the forward tripwire in design_geometry.py's FRINGE_FIT_STATISTICAL_ONLY_NOTE.

Predictions (P-066-G1, -1, -2, -3a, -3b, -4) committed in NOTES.md BEFORE
this file's first run (house discipline, non-negotiable), and printed
structurally below before the first FDTD call (exp-046/exp-065's own
structural-freeze precedent).
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

import design_geometry as dg           # exp-066's own thin wrapper

HARD_STOP_S = 30 * 60          # pre-registered wall-clock hard stop (39
                                # calls at exp-065's own measured C40 cost,
                                # ~25s/call single-process worst case, plus
                                # STRESS block's longer-STEPS calls -- see
                                # NOTES.md cost basis)

# ---------------------------------------------------- load exp-065's own harness
# exp-065's run.py does `import design_geometry as dg` internally (plain,
# unqualified) -- to avoid THAT resolving to THIS file's own design_geometry
# module (a name collision: both files are called design_geometry.py, and
# Python's import system caches sys.modules by plain name regardless of
# path), we temporarily point sys.modules["design_geometry"] at exp-065's
# OWN design_geometry module (already loaded, collision-safely, inside this
# file's own design_geometry.py as `dg.dg065`) before exec'ing exp-065's
# run.py, then restore it. Verified live before this file was written: the
# resulting R._settle_one(("C40", 40.0, 600, 1400)) reproduces exp-041's
# committed C_empty(40,600) bit-exact (-0.010964794540566314).
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
P-066-G1  G-1-prime extension: 18 new STEPS=1400 cells {36,37,39}x{+-}x3lam
          reproduce exp-041's committed block_main C_empty bit-exact
          CONFIRM dC == 0.0 (float64) for all 18 | REFUTE any nonzero -- HALTS
P-066-1   magnitude of settling correction, 18 new cells: median|dC(2800-1400)|
          CONFIRM in [0.001, 0.010] | REFUTE <0.0003 or >0.020
P-066-2   sign-flip prevalence, 18 new cells (1400 vs 2800)
          CONFIRM >=3 of 18 flip | REFUTE 0 of 18 flip
P-066-3a  lambda-coherence stress: 40deg/750nm |dC(4200-2800)| vs |dC(2800-1400)|
          CONFIRM <=1% | REFUTE >=5%
P-066-3b  theta-coherence stress (mandatory fix B): 37deg/600nm
          |dC(4200-2800)| vs |dC(2800-1400)| -- CONFIRM <=1% | REFUTE >=5%
P-066-4   T21 fringe-fit refit (desk-only, STRICTLY STATISTICAL -- mandatory
          fix C, no causal language): full 30-row settled Block MAIN R^2(c*)
          vs exp-042's own committed 0.7852421354715854
          CONFIRM within +-0.10 | REFUTE <0.4
"""


def _lab_diff_excluding_registry():
    """No `lab/` ENGINE diff -- the whole 'no new machinery' position rests
    on it. `lab/caveat_lint_config.json` is deliberately EXCLUDED from this
    check: it is a hand-curated data registry, not engine code, and this
    cycle's own mandatory fix D (Red Team attack 5 / MATERIALS' catch)
    disclosed-ly widens exactly one entry in it -- applied and verified
    live BEFORE this predict-commit (see phase3_synthesis.md), same
    precedent as Iteration 42's own "only lab/caveat_lint_config.json (one
    new entry) among lab/ files touched" framing."""
    out = subprocess.run(
        ["git", "diff", "--stat", "--", "lab/", ":!lab/caveat_lint_config.json"],
        cwd=REPO_ROOT, capture_output=True, text=True).stdout.strip()
    assert out == "", f"lab/ engine code is dirty -- the no-new-machinery position fails:\n{out}"
    return "clean (lab/caveat_lint_config.json intentionally excluded, see above)"


# ===================================================== worker entry points
def _g1ext_one(args):
    theta, lam = args
    t0 = time.time()
    _, th, lm, steps, prof, dt = R._settle_one(("C40", theta, lam, dg.STEPS_BASE))
    c = R._c_empty(prof, dg.CFG)
    return (theta, lam, c, dt)


def _main2800_one(args):
    theta, lam = args
    t0 = time.time()
    _, th, lm, steps, prof, dt = R._settle_one(("C40", theta, lam, dg.STEPS_LONG))
    c = R._c_empty(prof, dg.CFG)
    return (theta, lam, c, dt)


def _stress_one(args):
    theta, lam, steps = args
    _, th, lm, st, prof, dt = R._settle_one(("C40", theta, lam, steps))
    c = R._c_empty(prof, dg.CFG)
    return (theta, lam, steps, c, dt)


# ===================================================== Block G1EXT
def block_g1ext():
    jobs = [(th, lam) for lam in sorted(dg.CPL) for s in dg.NEW_ANGLES
            for th in (s, -s)]
    print(f"\n=== Block G1EXT: {len(dg.NEW_ANGLES)*2} angles x {len(dg.CPL)} "
          f"lambda = {len(jobs)} calls @ STEPS={dg.STEPS_BASE} ===", flush=True)
    t0 = time.time()
    rows, n = [], 0
    with ProcessPoolExecutor(max_workers=4) as ex:
        for th, lam, c, dt in ex.map(_g1ext_one, jobs):
            rows.append({"theta": th, "lambda_nm": lam, "C_empty": c,
                         "abs_C_empty": abs(c),
                         "pass_gate_hard": abs(c) <= dg.GATE_HARD})
            n += 1
            print(f"  [G1EXT {n:2d}/{len(jobs)}] theta={th:+05.1f} lam={lam} "
                  f"C_empty={c:+.6f} ({dt:5.1f}s)", flush=True)
    assert n == len(jobs), f"G1EXT run-count mismatch: {n} != {len(jobs)}"
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "rows": rows}


# ===================================================== Block MAIN2800
def block_main2800():
    jobs = [(th, lam) for lam in sorted(dg.CPL) for s in dg.NEW_ANGLES
            for th in (s, -s)]
    print(f"\n=== Block MAIN2800: {len(dg.NEW_ANGLES)*2} angles x {len(dg.CPL)} "
          f"lambda = {len(jobs)} calls @ STEPS={dg.STEPS_LONG} ===", flush=True)
    t0 = time.time()
    rows, n = [], 0
    with ProcessPoolExecutor(max_workers=4) as ex:
        for th, lam, c, dt in ex.map(_main2800_one, jobs):
            rows.append({"theta": th, "lambda_nm": lam, "C_empty": c,
                         "abs_C_empty": abs(c),
                         "pass_gate_hard": abs(c) <= dg.GATE_HARD})
            n += 1
            print(f"  [MAIN2800 {n:2d}/{len(jobs)}] theta={th:+05.1f} lam={lam} "
                  f"C_empty={c:+.6f} ({dt:5.1f}s)", flush=True)
    assert n == len(jobs), f"MAIN2800 run-count mismatch: {n} != {len(jobs)}"
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "rows": rows}


# ===================================================== Block STRESS
def block_stress():
    jobs = ([(dg.STRESS_CELL_LAMBDA[0], dg.STRESS_CELL_LAMBDA[1], s)
             for s in dg.STEPS_STRESS]
            + [(dg.STRESS_CELL_THETA[0], dg.STRESS_CELL_THETA[1], s)
               for s in dg.STEPS_STRESS_THETA])
    print(f"\n=== Block STRESS: {len(jobs)} calls "
          f"(lambda-coherence + theta-coherence, mandatory fix B) ===",
          flush=True)
    t0 = time.time()
    rows, n = [], 0
    with ProcessPoolExecutor(max_workers=3) as ex:
        for th, lam, steps, c, dt in ex.map(_stress_one, jobs):
            rows.append({"theta": th, "lambda_nm": lam, "steps": steps,
                         "C_empty": c})
            n += 1
            print(f"  [STRESS {n}/{len(jobs)}] theta={th:+05.1f} lam={lam} "
                  f"steps={steps} C_empty={c:+.6f} ({dt:5.1f}s)", flush=True)
    assert n == len(jobs), f"STRESS run-count mismatch: {n} != {len(jobs)}"
    return {"n_new_runs": n, "elapsed_s": time.time() - t0, "rows": rows}


# ===================================================== gates
def gate_g1ext(g1ext_rows):
    """P-066-G1: the 18 new STEPS=1400 cells must reproduce exp-041's
    committed block_main C_empty bit-exact -- extends exp-065's own G-1
    from 12/30 to 30/30 MAIN cells."""
    ref = json.load(open(dg.EXP041_RESULTS))["block_main"]["rows"]
    ref_map = {(r["theta"], r["lambda_nm"]): r["C_empty"] for r in ref}
    checks = []
    for row in g1ext_rows:
        k = (row["theta"], row["lambda_nm"])
        assert k in ref_map, f"no exp-041 anchor for {k} -- MAIN_ANGLES drift?"
        d = row["C_empty"] - ref_map[k]
        checks.append({"theta": k[0], "lambda_nm": k[1], "ours": row["C_empty"],
                       "exp041": ref_map[k], "delta": d, "exact": d == 0.0})
    return {"n_checked": len(checks), "all_exact": all(c["exact"] for c in checks),
            "max_abs_delta": max((abs(c["delta"]) for c in checks), default=None),
            "checks": checks}


# ===================================================== desk-only citations (fix A)
def cite_fallback_35_and_settled_38_40():
    """Mandatory fix A: the mandate's own literal text ("+-35/38/40deg") is
    closed in full by citing exp-065's own already-committed data -- zero
    new FDTD calls. +-35 is a FALLBACK_ANGLES-only cell (not part of
    exp-041's own Block MAIN naming), but IS part of the Iteration-43
    mandate's own text (LOGBOOK.md T27 entry, "Ranked top-3", PLAN.md
    queue -- all three read "MAIN-block +-35/+-38/+-40deg rows"). +-38/+-40
    are exp-041's own Block MAIN cells, already settled by exp-065's G-1
    (bit-exact vs exp-041 at STEPS=1400) and settled_sweep_steps2800_
    diagnostic.json (at STEPS=2800)."""
    sweep = json.load(open(dg.EXP065_RESULTS))["block_sweep"]["rows"]
    sweep_c40 = {(r["theta"], r["lambda_nm"]): r["C_empty"]
                 for r in sweep if r["config"] == "C40"}
    settled = json.load(open(dg.EXP065_SETTLED_JSON))

    rows = []
    for th in (-dg.FALLBACK_ONLY_ANGLE, dg.FALLBACK_ONLY_ANGLE):
        for lam in sorted(dg.CPL):
            c1400 = sweep_c40[(th, lam)]
            c2800 = settled[f"C40|{th}|{lam}"]
            rows.append({"theta": th, "lambda_nm": lam, "family": "fallback_only",
                         "C_empty_1400": c1400, "C_empty_2800": c2800,
                         "delta": c2800 - c1400,
                         "sign_flip": (c1400 > 0) != (c2800 > 0)})
    for th in dg.ALREADY_SETTLED_ANGLES:
        for sign in (1, -1):
            t = sign * th
            for lam in sorted(dg.CPL):
                c1400 = sweep_c40[(t, lam)]
                c2800 = settled[f"C40|{t}|{lam}"]
                rows.append({"theta": t, "lambda_nm": lam, "family": "main_block",
                             "C_empty_1400": c1400, "C_empty_2800": c2800,
                             "delta": c2800 - c1400,
                             "sign_flip": (c1400 > 0) != (c2800 > 0)})
    return {"n_cited": len(rows), "rows": rows,
            "note": ("Cited directly from experiments/065-t24-absorb-boundary-"
                     "sweep/results.json (block_sweep, STEPS=1400) and "
                     "settled_sweep_steps2800_diagnostic.json (STEPS=2800) -- "
                     "zero new FDTD calls, per mandatory fix A.")}


# ===================================================== P-066-4: desk refit (fix C)
def refit_fringe_model(g1ext_rows, main2800_rows, cited):
    """Mandatory fix C: refit exp-042's own edge_diffraction_c_empty_corrected
    against the FULL 30-row settled Block MAIN dataset (12 already-settled
    +-38/+-40 cells cited from exp-065, 18 new cells from Block MAIN2800),
    reported STRICTLY as a fit-quality statistic -- see
    design_geometry.FRINGE_FIT_STATISTICAL_ONLY_NOTE. NOT run on the +-35
    cells (fix A's own citation): exp-042's original fit was scored against
    exactly exp-041's 30 Block MAIN rows (36-40deg only) -- adding +-35
    would compare against a DIFFERENT cell set than the +-0.10 CONFIRM band
    was calibrated on."""
    settled_main = {}
    for r in main2800_rows:
        settled_main[(r["theta"], r["lambda_nm"])] = r["C_empty"]
    for r in cited["rows"]:
        if r["family"] == "main_block":
            settled_main[(r["theta"], r["lambda_nm"])] = r["C_empty_2800"]
    assert len(settled_main) == 30, f"expected 30 settled MAIN cells, got {len(settled_main)}"

    preds, meas, per_row = [], [], []
    for (th, lam), c in sorted(settled_main.items()):
        pred = dg.dg042.edge_diffraction_c_empty_corrected(th, dg.CPL[lam])
        preds.append(pred)
        meas.append(c)
        per_row.append({"theta": th, "lambda_nm": lam, "measured_settled": c,
                        "predicted": pred,
                        "sign_match": bool(np.sign(pred) == np.sign(c))})
    preds, meas = np.array(preds), np.array(meas)
    sign_agree = int(np.sum(np.sign(preds) == np.sign(meas)))
    ss_tot = float(np.sum((meas - meas.mean()) ** 2))
    r2_c1 = 1.0 - float(np.sum((meas - preds) ** 2)) / ss_tot
    c_star = float(np.sum(meas * preds) / np.sum(preds ** 2))
    r2_cstar = 1.0 - float(np.sum((meas - c_star * preds) ** 2)) / ss_tot

    orig = {"sign_agree": 27, "n": 30, "r2_c1": 0.6569548291361436,
            "c_star": 1.6196430704378861, "r2_cstar": 0.7852421354715854}
    return {"n": 30, "sign_agree": sign_agree, "r2_c1": r2_c1, "c_star": c_star,
            "r2_cstar": r2_cstar, "rows": per_row, "original_steps1400_fit": orig,
            "statistical_only_note": dg.FRINGE_FIT_STATISTICAL_ONLY_NOTE}


# ===================================================== scoring
def score(g1ext, main2800, stress, g1, cited, refit):
    # ---- P-066-1 / P-066-2: 18 new cells only
    m2 = {(r["theta"], r["lambda_nm"]): r["C_empty"] for r in main2800["rows"]}
    g1r = {(r["theta"], r["lambda_nm"]): r["C_empty"] for r in g1ext["rows"]}
    deltas, flips = [], 0
    for k in g1r:
        d = m2[k] - g1r[k]
        deltas.append(abs(d))
        if (g1r[k] > 0) != (m2[k] > 0):
            flips += 1
    p1 = {"median": float(np.median(deltas)), "max": float(max(deltas)),
          "n_cells": len(deltas)}
    p1["confirm"] = 0.001 <= p1["median"] <= 0.010
    p1["refute"] = p1["median"] < 0.0003 or p1["median"] > 0.020
    p1["verdict"] = ("CONFIRMED" if p1["confirm"] else
                     "REFUTED" if p1["refute"] else "PARTIAL")

    p2 = {"n_flips": flips, "n_cells": len(deltas)}
    p2["confirm"] = flips >= 3
    p2["refute"] = flips == 0
    p2["verdict"] = ("CONFIRMED" if p2["confirm"] else
                     "REFUTED" if p2["refute"] else "PARTIAL")

    # ---- P-066-3a: 40deg/750nm lambda-coherence
    d041 = json.load(open(dg.EXP041_RESULTS))["block_main"]["rows"]
    d041_map = {(r["theta"], r["lambda_nm"]): r["C_empty"] for r in d041}
    settled = json.load(open(dg.EXP065_SETTLED_JSON))
    th_a, lam_a = dg.STRESS_CELL_LAMBDA
    c1400_a = d041_map[(th_a, lam_a)]
    c2800_a = settled[f"C40|{th_a}|{lam_a}"]
    stress_a = {r["steps"]: r["C_empty"] for r in stress["rows"]
                if r["theta"] == th_a and r["lambda_nm"] == lam_a}
    d_base_a = abs(c2800_a - c1400_a)
    d_next_a = abs(stress_a[4200] - c2800_a)
    ratio_a = d_next_a / d_base_a if d_base_a else float("inf")
    p3a = {"theta": th_a, "lambda_nm": lam_a, "C_1400": c1400_a,
           "C_2800": c2800_a, "C_4200": stress_a[4200], "C_5600": stress_a[5600],
           "delta_2800_1400": d_base_a, "delta_4200_2800": d_next_a,
           "ratio": ratio_a}
    p3a["confirm"] = ratio_a <= 0.01
    p3a["refute"] = ratio_a >= 0.05
    p3a["verdict"] = ("CONFIRMED (750nm settled by 2800)" if p3a["confirm"] else
                      "REFUTED (750nm needs STEPS>2800)" if p3a["refute"]
                      else "PARTIAL")

    # ---- P-066-3b: 37deg/600nm theta-coherence (mandatory fix B)
    th_b, lam_b = dg.STRESS_CELL_THETA
    c1400_b = g1r[(th_b, lam_b)]
    c2800_b = m2[(th_b, lam_b)]
    stress_b = {r["steps"]: r["C_empty"] for r in stress["rows"]
                if r["theta"] == th_b and r["lambda_nm"] == lam_b}
    d_base_b = abs(c2800_b - c1400_b)
    d_next_b = abs(stress_b[4200] - c2800_b)
    ratio_b = d_next_b / d_base_b if d_base_b else float("inf")
    p3b = {"theta": th_b, "lambda_nm": lam_b, "C_1400": c1400_b,
           "C_2800": c2800_b, "C_4200": stress_b[4200],
           "delta_2800_1400": d_base_b, "delta_4200_2800": d_next_b,
           "ratio": ratio_b}
    p3b["confirm"] = ratio_b <= 0.01
    p3b["refute"] = ratio_b >= 0.05
    p3b["verdict"] = ("CONFIRMED (37deg/600nm settled by 2800)" if p3b["confirm"]
                      else "REFUTED (settling does not generalize across theta)"
                      if p3b["refute"] else "PARTIAL")

    # ---- P-066-4: fringe-fit refit, strictly statistical (mandatory fix C)
    orig = refit["original_steps1400_fit"]
    d_r2 = refit["r2_cstar"] - orig["r2_cstar"]
    p4 = dict(refit)
    p4["delta_r2_cstar"] = d_r2
    p4["confirm"] = abs(d_r2) <= 0.10
    p4["refute"] = refit["r2_cstar"] < 0.4
    p4["verdict"] = ("CONFIRMED (fit quality recovered, no mechanism claim)"
                     if p4["confirm"] else
                     "REFUTED (fit quality degraded, no mechanism claim)"
                     if p4["refute"] else "PARTIAL")

    return {"P-066-G1": g1, "P-066-1": p1, "P-066-2": p2, "P-066-3a": p3a,
            "P-066-3b": p3b, "P-066-4": p4}


# ===================================================== closure summary
def closure_summary(g1ext, main2800, cited):
    """The full mandate-scope closure table: all 36 cells the Iteration-43
    mandate's own text names (+-35/36/37/38/39/40deg x 3lambda), at both
    STEPS=1400 and STEPS=2800, with GATE_HARD pass/fail at each STEPS --
    the concrete answer to 'scope exactly how many downstream citations
    are affected' at the level of this instrument's own bucket calls."""
    rows = []
    m2 = {(r["theta"], r["lambda_nm"]): r["C_empty"] for r in main2800["rows"]}
    g1r = {(r["theta"], r["lambda_nm"]): r["C_empty"] for r in g1ext["rows"]}
    for (th, lam), c1400 in g1r.items():
        c2800 = m2[(th, lam)]
        rows.append({"theta": th, "lambda_nm": lam,
                     "C_1400": c1400, "C_2800": c2800,
                     "pass_1400": abs(c1400) <= dg.GATE_HARD,
                     "pass_2800": abs(c2800) <= dg.GATE_HARD})
    for r in cited["rows"]:
        rows.append({"theta": r["theta"], "lambda_nm": r["lambda_nm"],
                     "C_1400": r["C_empty_1400"], "C_2800": r["C_empty_2800"],
                     "pass_1400": abs(r["C_empty_1400"]) <= dg.GATE_HARD,
                     "pass_2800": abs(r["C_empty_2800"]) <= dg.GATE_HARD})
    assert len(rows) == 36, f"closure summary should have 36 cells, got {len(rows)}"
    bucket_flips = sum(1 for r in rows if r["pass_1400"] != r["pass_2800"])
    return {"n_cells": 36, "rows": sorted(rows, key=lambda r: (r["lambda_nm"], r["theta"])),
            "n_bucket_flips_1400_vs_2800": bucket_flips,
            "n_fail_1400": sum(1 for r in rows if not r["pass_1400"]),
            "n_fail_2800": sum(1 for r in rows if not r["pass_2800"])}


# ===================================================== main
def main():
    t_start = time.time()
    print("=" * 78)
    print("exp-066 -- T27 Block MAIN settling re-verification | Panel Iteration 43")
    print("Lead: PHOTONICS (rotation). Director's Phase-3 synthesis applied in full.")
    print("=" * 78)
    print("\nFROZEN PREDICTIONS (committed to git in NOTES.md BEFORE this "
          "file's first run):")
    print(FROZEN_PREDICTIONS)
    print(f"lab/ engine diff check: {_lab_diff_excluding_registry()}")

    g1ext = block_g1ext()
    print("\n--- GATE P-066-G1: exp-041 Block MAIN anchor, extended to 30/30 ---")
    g1 = gate_g1ext(g1ext["rows"])
    for c in g1["checks"]:
        print(f"    theta={c['theta']:+05.1f} lam={c['lambda_nm']}  "
              f"ours={c['ours']:+.17g}  exp041={c['exp041']:+.17g}  "
              f"delta={c['delta']:+.3e}  exact={c['exact']}")
    print(f"    {g1['n_checked']} checked, all_exact={g1['all_exact']}")
    assert g1["all_exact"], "P-066-G1 FAILED -- halting before STEPS=2800 is trusted"

    main2800 = block_main2800()
    stress = block_stress()

    total_runs = g1ext["n_new_runs"] + main2800["n_new_runs"] + stress["n_new_runs"]
    elapsed = time.time() - t_start
    print(f"\n=== {total_runs} new FDTD calls in {elapsed / 60:.1f} min "
          f"(hard stop {HARD_STOP_S / 60:.0f} min) ===")
    assert total_runs == 39, f"run-count mismatch vs frozen budget: {total_runs} != 39"

    print("\n--- Desk citation (mandatory fix A): +-35/38/40deg already-committed data ---")
    cited = cite_fallback_35_and_settled_38_40()
    print(f"    {cited['n_cited']} cells cited (6 fallback-only +-35, "
          f"12 already-settled main-block +-38/+-40), zero new FDTD calls")

    print("\n--- Desk refit (mandatory fix C): T21 fringe model vs full settled MAIN ---")
    refit = refit_fringe_model(g1ext["rows"], main2800["rows"], cited)
    print(f"    sign_agree={refit['sign_agree']}/30  r2_c1={refit['r2_c1']:.4f}  "
          f"c_star={refit['c_star']:.4f}  r2_cstar={refit['r2_cstar']:.4f}")
    print(f"    original (STEPS=1400) r2_cstar={refit['original_steps1400_fit']['r2_cstar']:.4f}")

    sc_ = score(g1ext, main2800, stress, g1, cited, refit)
    summary = closure_summary(g1ext, main2800, cited)

    print("\n" + "=" * 78)
    print("SCORED PREDICTIONS")
    print("=" * 78)
    for pid in ("P-066-G1", "P-066-1", "P-066-2", "P-066-3a", "P-066-3b", "P-066-4"):
        v = sc_[pid].get("verdict")
        if v is None:
            v = "PASSED" if sc_[pid].get("all_exact") else "FAILED"
        print(f"  {pid:<10} {v}")

    print(f"\nCLOSURE SUMMARY: 36/36 mandate-scope cells covered "
          f"(+-35/36/37/38/39/40deg x 3lambda). "
          f"GATE_HARD fails: {summary['n_fail_1400']}/36 @1400 -> "
          f"{summary['n_fail_2800']}/36 @2800. "
          f"Bucket flips: {summary['n_bucket_flips_1400_vs_2800']}/36.")

    out = {
        "experiment": "exp-066-t27-block-main-settling-reverification",
        "panel_iteration": 43, "lead_seat": "PHOTONICS",
        "t1_escape_route": "N/A -- instrument/model-fidelity class",
        "steps_base": dg.STEPS_BASE, "steps_long": dg.STEPS_LONG,
        "gates": {"GATE_HARD": dg.GATE_HARD, "C_THR_LAB": dg.C_THR_LAB,
                  "C_THR_FIELD": dg.C_THR_FIELD,
                  "MARGINAL_BAND": [dg.MARGINAL_LO, dg.MARGINAL_HI]},
        "r_contact_disposition": dg.R_CONTACT_DISPOSITION,
        "settling_mechanism_note": dg.SETTLING_MECHANISM_NOTE,
        "block_g1ext": g1ext, "block_main2800": main2800, "block_stress": stress,
        "gate_g1": g1, "cited_fallback_and_settled": cited,
        "fringe_fit_refit": refit,
        "scored": sc_, "closure_summary": summary,
        "total_new_runs": total_runs, "total_elapsed_s": elapsed,
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote results.json ({total_runs} runs, {elapsed / 60:.1f} min)")


if __name__ == "__main__":
    main()
