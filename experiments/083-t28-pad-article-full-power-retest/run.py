"""exp-083 -- The full 31-point/0.2deg PAIR_PAD-with-article re-test at 600nm.
=============================================================================
Panel Iteration 60 (lead: VISION SCIENCE, by rotation). Executes PLAN.md's
Iteration-60 queue Tier 1 item 5 (experiments/082-.../phase5_redteam_audit.md
Sec 10) -- the near-unanimous single highest-value item on the board.

Runs exp-082's own PAIR_PAD-with-article harness (C40/G40, flagship
graded_black_shell+pec_disk absorber) at T28's own established FULL
statistical power: 31 angles / 0.2deg step / [36,42]deg (dg069.DENSE_ANGLES),
instead of exp-082's disclosed 7-point/1deg reduction. Red Team's own
Phase-2 and Phase-5 audits of exp-082 proved the mechanism-identity question
(same PAD-tied phase mechanism, observed through the article, vs a
qualitatively different article-mediated interaction) is UNRESOLVABLE at
7-point power; this is the test that removes the power deficiency.

Predictions (the three-branch period discriminator, PHOTONICS' own
two-branch-plus-null spec) committed in phase1_proposal.md Sec 4 BEFORE this
file's first run (house discipline, non-negotiable -- see the CRITICAL
git-provenance instruction in this cycle's own task brief: a THIRD
consecutive same-commit/late-freeze recurrence fires Checkpoint criterion 4
outright).

Bundles, at zero marginal FDTD cost, EM's own field-difference decomposition
(phase5_review_em.md Sec 3, adopted by Red Team's audit Sec 3): persists the
raw observer_profile arrays for both legs, both configs, all 31 angles, and
independently free-period-fits DeltaE_article(theta)'s own periodicity,
logged as complementary to -- not a substitute for -- the intensity-level
Weber-contrast fit.

Zero new `lab/` machinery -- every primitive reused is already gated (Sim;
materials.graded_black_shell/pec_disk, stage 7; ambient.observer_profile/
contrast_from_runs/window_means, stage 9; sections.full_capture/phasors).
_free_period_search/_fixed_period_fit (exp-069) and free_period_with_widening
(exp-077) are reused verbatim -- not modified, not reimplemented (R6 does
not apply, phase1_proposal.md Sec 3b).
"""

import importlib.util
import json
import math
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    """House `_load()` pattern (boundary_reflectance.py / y_wall_prescreen.py
    / y_wall_aperture_sum.py / validity_precheck.py / photonics_construction.py
    / exp-082's own run.py -- all reuse this exact idiom for cross-experiment-
    directory imports)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP069_DIR = os.path.join(ROOT, "experiments", "069-t21-block-mini-period-match-power-up")
EXP077_DIR = os.path.join(ROOT, "experiments", "077-t28-pad-round-trip-echo-model")
EXP076_RESULTS = os.path.join(ROOT, "experiments", "076-t28-g40-pad-decorrelation", "results.json")
EXP077_RESULTS = os.path.join(EXP077_DIR, "pad_round_trip_results.json")
EXP069_RESULTS = os.path.join(EXP069_DIR, "results.json")

# dg069 re-exports dg065.CONFIGS/CPL/GATE_HARD/... verbatim (design_geometry.py
# Sec "dg065 = _load_exp065()") AND adds DENSE_ANGLES (the 31-point/0.2deg
# window), P_deg, T_SINTHETA_600, STEPS_SETTLED=2800 -- one module, all of
# T28's established geometry+angle-grid constants, zero duplication.
dg = _load(os.path.join(EXP069_DIR, "design_geometry.py"), "_exp083_dg069")

# pad_round_trip_model.py (exp-077) internally loads exp-069's own run.py and
# re-exports `_fixed_period_fit`/`_free_period_search` verbatim, plus defines
# `free_period_with_widening` -- the staged-widening wrapper EM's own Phase-5
# review names explicitly ("apply the sub-thread's own free_period_with_
# widening machinery to DeltaE_article's own period").
prm = _load(os.path.join(EXP077_DIR, "pad_round_trip_model.py"), "_exp083_prm")

from lab import Sim, materials, ambient as amb, sections as sc  # noqa: E402
from lab import glare_sidecar as gs  # noqa: E402

THETAS = list(dg.DENSE_ANGLES)             # 31 points, 36.0..42.0, 0.2deg step
assert len(THETAS) == 31 and THETAS[0] == 36.0 and THETAS[-1] == 42.0
PAIR_KEYS = ("C40", "G40")
STEPS_MAIN = dg.STEPS_SETTLED               # 2800 -- T28's own established settled value
STEPS_SETTLE_CHECK = 1400
SETTLE_THETA = 39.0
SETTLE_CFG = "G40"
C_THR_LAB = gs.c_thr(3.0, 0.4, bar="lab")

# ---------------------------------------------------- pre-registered reference periods
# Never hand-typed -- copied directly from already-committed JSON fields
# (phase1_proposal.md Sec 4a cites the identical provenance).
with open(EXP077_RESULTS) as _f:
    _res77 = json.load(_f)
P_CONTINUITY = _res77["test_a_pair_pad"]["real"]["chosen"]["p_star_deg"]

with open(EXP069_RESULTS) as _f:
    _res69 = json.load(_f)
P_EDGE_A = _res69["scored"]["p3"]["p_star_deg"]      # T28's own original C80-C40 period
P_EDGE_B = _res69["scored"]["p3"]["P39_600"]          # T21's own established fringe at 39deg

REL_DEV_TOL = 0.20
R2_FLOOR = 0.30

FROZEN_PREDICTIONS = f"""
Reproduction precondition: this cycle's own freshly-run EMPTY leg at all 31
dg069.DENSE_ANGLES for C40/G40 must reproduce experiments/076-.../
results.json::headline's C40/G40 values at those same angles,
max|delta| < 1e-9 -- BEFORE the article-loaded leg (or any period fit) is
trusted.

PRIMARY (three-branch period discriminator, pre-registered BEFORE running):
free_period_with_widening(THETAS, delta_scene) recovers (P*, R2) for
delta_scene(theta) = C(G40;theta,article) - C(C40;theta,article) over all
31 angles.
  (A) MECHANISM CONTINUITY:      |P*-{P_CONTINUITY:.6f}|/{P_CONTINUITY:.6f} <= {REL_DEV_TOL}  AND R2 >= {R2_FLOOR}
  (B) ARTICLE-EDGE DIFFRACTION:  R2 >= {R2_FLOOR} AND (within {REL_DEV_TOL} of {P_EDGE_A:.6f} OR of {P_EDGE_B:.6f})
  (C) NEITHER ESTABLISHED FAMILY: R2 < {R2_FLOOR}, OR R2 >= {R2_FLOOR} but P* clears none of the three bands.

COMPANION (EM's field-difference decomposition, bundled at zero marginal
FDTD cost, disclosed/complementary -- NOT gating, no pre-registered band):
persist raw observer_profile(theta,y) for both legs, both configs, all 31
angles; DeltaE_article_k(theta,y) = profile_with(k,theta,y) -
profile_without(k,theta,y) for k in {{C40,G40}}; reduce via the object-window
mean (amb.window_means); free-period-fit DeltaE_obj_article_C40(theta),
DeltaE_obj_article_G40(theta), and their cross-config pair
DeltaDeltaE_obj_article_PAD(theta) = G40-C40, report against the same three
reference periods.

Secondary (disclosed, not gating): ratio=A_scene/A_empty (exp-082's own
[0.5,2.0]/<=0.2/other bands, recomputed at n=31 for direct comparability);
Pearson r(delta_scene,delta_empty) at n=31 with a 200,000-trial permutation
p-value (the diagnostic Red Team's own exp-082 audit showed was structurally
underpowered at n=7); A_scene/C_thr (C_thr={C_THR_LAB}).

Settling precondition (disclosed, not gating): |C(G40,theta=39,article,
STEPS=2800) - C(G40,theta=39,article,STEPS=1400)| reported for context,
repeats exp-082's own spot-check exactly, no new pass/fail threshold.
"""


def assert_lab_clean():
    import subprocess
    out = subprocess.run(["git", "diff", "--stat", "--", "lab/"],
                          cwd=ROOT, capture_output=True, text=True).stdout.strip()
    assert out == "", f"lab/ is dirty -- the no-new-machinery position fails:\n{out}"
    return "clean"


def build_article(sim, cx, cy):
    """The established flagship absorber -- bit-identical to
    experiments/024-.../run.py::build("absorber") and exp-082's own
    build_article(). Not a new variant."""
    materials.pec_disk(sim, cx, cy, 30)
    materials.graded_black_shell(sim, cx, cy, 30, dg.R_OUT)


def _run_sim(cfg, theta, steps, with_article):
    sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=dg.CPL[600],
              courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
    if with_article:
        build_article(sim, cfg["obj_x"], cfg["obj_y"])
    sim.add_line_source(cfg["src_x"], y_lo=cfg["y_lo"], y_hi=cfg["y_hi"],
                         angle_deg=theta, amplitude=1.0,
                         profile="plane", edge=dg.TAPER)
    sim.run(steps)
    return sc.full_capture(sim)


def _profile(cap, cfg):
    ph = sc.phasors(cap)
    return amb.observer_profile(ph, cfg["plane_x"], cfg["y_lo"], cfg["y_hi"])


def one_call(args):
    """(cfg_key, theta, with_article, steps) -> profile list. Run in a
    worker process; geometry re-derived from dg.CONFIGS by key (picklable)."""
    cfg_key, theta, with_article, steps = args
    cfg = dg.CONFIGS[cfg_key]
    t0 = time.time()
    cap = _run_sim(cfg, theta, steps, with_article)
    prof = _profile(cap, cfg).tolist()
    return (cfg_key, theta, with_article, steps, prof, time.time() - t0)


def pearson_r(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    xc = x - x.mean()
    yc = y - y.mean()
    denom = math.sqrt(float(np.sum(xc ** 2)) * float(np.sum(yc ** 2)))
    return float(np.sum(xc * yc) / denom) if denom > 0 else 0.0


def permutation_test_r(x, y, n_trials=200000, seed=7):
    rng = np.random.default_rng(seed)
    r_obs = pearson_r(x, y)
    y = np.asarray(y, dtype=float)
    count = 0
    for _ in range(n_trials):
        yp = rng.permutation(y)
        if abs(pearson_r(x, yp)) >= abs(r_obs):
            count += 1
    p = count / n_trials
    return dict(r_obs=r_obs, n_trials=n_trials, p_value=p)


def classify(p_star, r2):
    rel_c = abs(p_star - P_CONTINUITY) / P_CONTINUITY
    rel_a = abs(p_star - P_EDGE_A) / P_EDGE_A
    rel_b = abs(p_star - P_EDGE_B) / P_EDGE_B
    if r2 >= R2_FLOOR and rel_c <= REL_DEV_TOL:
        return "A_MECHANISM_CONTINUITY", dict(rel_dev_continuity=rel_c)
    if r2 >= R2_FLOOR and (rel_a <= REL_DEV_TOL or rel_b <= REL_DEV_TOL):
        return "B_ARTICLE_EDGE_DIFFRACTION", dict(rel_dev_edge_a=rel_a, rel_dev_edge_b=rel_b)
    return "C_NEITHER_ESTABLISHED_FAMILY", dict(
        rel_dev_continuity=rel_c, rel_dev_edge_a=rel_a, rel_dev_edge_b=rel_b, r2=r2)


def main():
    print("=" * 78)
    print("exp-083 -- the full 31-point/0.2deg PAIR_PAD-with-article re-test")
    print("=" * 78)
    print(FROZEN_PREDICTIONS)

    print(assert_lab_clean())

    jobs = []
    for key in PAIR_KEYS:
        for th in THETAS:
            jobs.append((key, th, False, STEPS_MAIN))   # empty
            jobs.append((key, th, True, STEPS_MAIN))    # scene (article)
    jobs.append((SETTLE_CFG, SETTLE_THETA, True, STEPS_SETTLE_CHECK))

    print(f"\n{len(jobs)} FDTD calls queued "
          f"(2 configs x 31 angles x 2 legs = 124, + 1 settling-precondition call)")
    t0 = time.time()
    results = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for n, (key, th, art, steps, prof, dt) in enumerate(ex.map(one_call, jobs), 1):
            results[(key, th, art, steps)] = prof
            print(f"  [{n:3d}/{len(jobs)}] {key} theta={th:+06.2f} "
                  f"article={art} steps={steps} ({dt:5.1f}s)", flush=True)
    total_wall = time.time() - t0
    print(f"\ntotal wall time: {total_wall:.1f}s")

    # ---------------------------------------------------------- assemble C/C_empty
    def contrast_pair(key, theta, steps=STEPS_MAIN):
        cfg = dg.CONFIGS[key]
        empty_p = np.array(results[(key, theta, False, steps)])
        scene_p = np.array(results[(key, theta, True, steps)])
        r = amb.contrast_from_runs([scene_p], [empty_p], [1.0],
                                    cfg["y_lo"], cfg["obj_y"],
                                    dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)
        return r["C"], r["C_empty"]

    per_theta = {}
    for th in THETAS:
        c40_C, c40_Ce = contrast_pair("C40", th)
        g40_C, g40_Ce = contrast_pair("G40", th)
        per_theta[th] = dict(C40_C=c40_C, C40_Ce=c40_Ce, G40_C=g40_C, G40_Ce=g40_Ce,
                              delta_scene=g40_C - c40_C, delta_empty=g40_Ce - c40_Ce)

    delta_scene = np.array([per_theta[th]["delta_scene"] for th in THETAS])
    delta_empty = np.array([per_theta[th]["delta_empty"] for th in THETAS])
    A_scene = float(np.ptp(delta_scene))
    A_empty = float(np.ptp(delta_empty))
    ratio = A_scene / A_empty if A_empty != 0 else float("inf")
    if 0.5 <= ratio <= 2.0:
        ratio_verdict = "SURVIVES"
    elif ratio <= 0.2:
        ratio_verdict = "CANCELS"
    else:
        ratio_verdict = "INCONCLUSIVE"

    print("\n[secondary: amplitude-ratio consistency check, n=31]")
    print(f"  A_scene (ptp) = {A_scene:.6e}   A_empty (ptp) = {A_empty:.6e}")
    print(f"  ratio = {ratio:.4f}   ratio_verdict = {ratio_verdict}")

    # ------------------------------------------------- reproduction precondition
    with open(EXP076_RESULTS) as f:
        res76 = json.load(f)
    ref_theta = res76["headline"]["theta"]
    ref_c40 = dict(zip(ref_theta, res76["headline"]["C40"]))
    ref_g40 = dict(zip(ref_theta, res76["headline"]["G40"]))

    repro = {}
    max_dev = 0.0
    for th in THETAS:
        c40_Ce = per_theta[th]["C40_Ce"]
        g40_Ce = per_theta[th]["G40_Ce"]
        ref_c40_th = next(v for k, v in ref_c40.items() if abs(k - th) < 1e-6)
        ref_g40_th = next(v for k, v in ref_g40.items() if abs(k - th) < 1e-6)
        d40 = abs(c40_Ce - ref_c40_th)
        d80 = abs(g40_Ce - ref_g40_th)
        repro[th] = dict(C40_dev=d40, G40_dev=d80)
        max_dev = max(max_dev, d40, d80)
    repro_pass = bool(max_dev < 1e-9)
    print("\n[reproduction precondition -- fresh 31-pt empty leg vs exp-076 committed]")
    print(f"  max_dev = {max_dev:.3e}  PASS(<1e-9) = {repro_pass}")
    assert repro_pass, "reproduction precondition FAILED -- do not trust the article-loaded leg"

    # ---------------------------------------------- PRIMARY: three-branch discriminator
    free_scene = prm.free_period_with_widening(THETAS, delta_scene.tolist(), "delta_scene")
    p_star = free_scene["chosen"]["p_star_deg"]
    r2 = free_scene["chosen"]["r_squared"]
    branch, branch_detail = classify(p_star, r2)
    print("\n[PRIMARY: three-branch period discriminator on delta_scene(theta), n=31]")
    print(f"  P* = {p_star:.4f}deg   R2 = {r2:.4f}")
    print(f"  P_continuity={P_CONTINUITY:.4f}  P_edge_A={P_EDGE_A:.4f}  P_edge_B={P_EDGE_B:.4f}")
    print(f"  BRANCH: {branch}  ({branch_detail})")

    # also free-period-fit delta_empty at full power, for direct comparison
    free_empty = prm.free_period_with_widening(THETAS, delta_empty.tolist(), "delta_empty")
    print(f"  [context] delta_empty free fit: P*={free_empty['chosen']['p_star_deg']:.4f}deg "
          f"R2={free_empty['chosen']['r_squared']:.4f}")

    # ---------------------------------------------- secondary: correlation @ n=31
    corr = permutation_test_r(delta_scene, delta_empty, n_trials=200000, seed=7)
    print("\n[secondary: Pearson r(delta_scene,delta_empty) @ n=31, 200000-trial permutation]")
    print(f"  r_obs = {corr['r_obs']:.4f}   p_value = {corr['p_value']:.5f}")

    a_scene_over_cthr = A_scene / C_THR_LAB
    print(f"\n[secondary] A_scene / C_thr = {a_scene_over_cthr:.4f}  (C_thr={C_THR_LAB})")

    # ------------------------------------------------- settling precondition
    cfg = dg.CONFIGS[SETTLE_CFG]
    empty_39 = np.array(results[(SETTLE_CFG, SETTLE_THETA, False, STEPS_MAIN)])
    scene_2800 = np.array(results[(SETTLE_CFG, SETTLE_THETA, True, STEPS_MAIN)])
    scene_1400 = np.array(results[(SETTLE_CFG, SETTLE_THETA, True, STEPS_SETTLE_CHECK)])
    r2800 = amb.contrast_from_runs([scene_2800], [empty_39], [1.0],
                                    cfg["y_lo"], cfg["obj_y"], dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)
    r1400 = amb.contrast_from_runs([scene_1400], [empty_39], [1.0],
                                    cfg["y_lo"], cfg["obj_y"], dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)
    settle_abs_dev = abs(r2800["C"] - r1400["C"])
    settle_rel_dev = settle_abs_dev / abs(r2800["C"]) if r2800["C"] != 0 else float("inf")
    print("\n[settling precondition, disclosed not gating]")
    print(f"  abs_dev = {settle_abs_dev:.3e}  rel_dev = {settle_rel_dev:.4f}")

    # ---------------------------------------------- COMPANION: EM's field-difference decomposition
    def obj_window_mean_profile(key, theta, with_article, steps=STEPS_MAIN):
        cfg = dg.CONFIGS[key]
        p = np.array(results[(key, theta, with_article, steps)])
        return p, cfg

    def delta_e_obj(key):
        vals = []
        for th in THETAS:
            p_with, cfg = obj_window_mean_profile(key, th, True)
            p_without, _ = obj_window_mean_profile(key, th, False)
            d_field = p_with - p_without
            obj_mean, _flank_mean = amb.window_means(
                d_field, cfg["y_lo"], cfg["obj_y"], dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)
            vals.append(obj_mean)
        return np.array(vals)

    dE_c40 = delta_e_obj("C40")
    dE_g40 = delta_e_obj("G40")
    dE_pair = dE_g40 - dE_c40

    def fit_and_classify(label, series):
        free = prm.free_period_with_widening(THETAS, series.tolist(), label)
        p = free["chosen"]["p_star_deg"]
        r = free["chosen"]["r_squared"]
        br, detail = classify(p, r)
        return dict(free=free, p_star_deg=p, r_squared=r, branch=br, branch_detail=detail)

    em_c40 = fit_and_classify("DeltaE_obj_article_C40", dE_c40)
    em_g40 = fit_and_classify("DeltaE_obj_article_G40", dE_g40)
    em_pair = fit_and_classify("DeltaDeltaE_obj_article_PAD", dE_pair)

    print("\n[COMPANION: EM's field-difference decomposition (disclosed, complementary, not gating)]")
    for label, d in (("DeltaE_obj_article_C40", em_c40),
                      ("DeltaE_obj_article_G40", em_g40),
                      ("DeltaDeltaE_obj_article_PAD (G40-C40)", em_pair)):
        print(f"  {label}: P*={d['p_star_deg']:.4f}deg  R2={d['r_squared']:.4f}  branch={d['branch']}")

    # ---------------------------------------------------------- persist raw profiles
    def profiles_block(key):
        return dict(
            empty={f"{th:.1f}": results[(key, th, False, STEPS_MAIN)] for th in THETAS},
            article={f"{th:.1f}": results[(key, th, True, STEPS_MAIN)] for th in THETAS},
        )

    out = dict(
        frozen_predictions=FROZEN_PREDICTIONS,
        thetas=THETAS, pair_keys=PAIR_KEYS, steps_main=STEPS_MAIN,
        total_new_fdtd_calls=len(jobs), total_wall_time_s=total_wall,
        p_continuity=P_CONTINUITY, p_edge_a=P_EDGE_A, p_edge_b=P_EDGE_B,
        rel_dev_tol=REL_DEV_TOL, r2_floor=R2_FLOOR,
        per_theta=per_theta,
        delta_scene=delta_scene.tolist(), delta_empty=delta_empty.tolist(),
        A_scene=A_scene, A_empty=A_empty, ratio=ratio, ratio_verdict=ratio_verdict,
        c_thr_lab=C_THR_LAB, a_scene_over_cthr=a_scene_over_cthr,
        reproduction_precondition=dict(per_theta=repro, max_dev=max_dev, passed=repro_pass),
        settling_precondition=dict(
            steps_main=STEPS_MAIN, steps_check=STEPS_SETTLE_CHECK,
            theta=SETTLE_THETA, cfg=SETTLE_CFG,
            C_steps2800=r2800["C"], C_steps1400=r1400["C"],
            abs_dev=settle_abs_dev, rel_dev=settle_rel_dev),
        primary_period_discriminator=dict(
            delta_scene_fit=free_scene, delta_empty_fit=free_empty,
            p_star_deg=p_star, r_squared=r2, branch=branch, branch_detail=branch_detail),
        secondary_correlation=corr,
        em_field_difference_decomposition=dict(
            delta_e_obj_article_c40=dE_c40.tolist(),
            delta_e_obj_article_g40=dE_g40.tolist(),
            delta_delta_e_obj_article_pad=dE_pair.tolist(),
            fit_c40=em_c40, fit_g40=em_g40, fit_pair=em_pair),
        raw_observer_profiles=dict(C40=profiles_block("C40"), G40=profiles_block("G40")),
    )
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
