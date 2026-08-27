"""exp-082 -- The PAD-loaded real-article check: measurement harness.
=============================================================================
Panel Iteration 59 (lead: QUANTUM OPTICS, by rotation). Executes PLAN.md's
Iteration-59 queue Tier 2 item 7 -- deferred SIX consecutive T28 cycles
(076-081) -- as this cycle's own primary build, per the standing tripwire
(a seventh deferral without an explicitly stated reason fires Checkpoint
criterion 4 outright).

Loads the established flagship absorber (materials.graded_black_shell,
PEC-cored, bit-identical to experiments/024-.../run.py::build("absorber"))
into dg065.CONFIGS' own C40/G40 pair (PAIR_PAD, the dominant empty-scene
PAD-tied confound, Iteration 53/exp-076) at the already-defined obj_x/obj_y
location, and asks: does the empty-scene PAD-sensitivity axis survive into
the REAL, article-loaded Weber-contrast channel (`C`, computed exactly the
way lab/ambient.py::contrast_from_runs computes it for every constraint-3
citation this program has ever issued), or does it cancel in the object-
minus-flank subtraction real scoring performs?

Predictions (pre-registered SUPPORT/INCONCLUSIVE/REFUTE-style SURVIVES/
CANCELS/INCONCLUSIVE bands) committed in phase1_proposal.md Sec 4 BEFORE
this file's first run (house discipline, non-negotiable).

Zero new `lab/` machinery -- every primitive reused is already gated
(Sim; materials.graded_black_shell/pec_disk, stage 7; ambient.observer_
profile/contrast_from_runs, stage 9; sections.full_capture/phasors).
"""

import importlib.util
import json
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
    -- all reuse this exact idiom for cross-experiment-directory imports)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP065_DIR = os.path.join(ROOT, "experiments", "065-t24-absorb-boundary-sweep")
EXP076_RESULTS = os.path.join(ROOT, "experiments", "076-t28-g40-pad-decorrelation", "results.json")

dg = _load(os.path.join(EXP065_DIR, "design_geometry.py"), "_exp082_dg065")

from lab import Sim, materials, ambient as amb, sections as sc  # noqa: E402
from lab import glare_sidecar as gs  # noqa: E402

THETAS = [36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0]
PAIR_KEYS = ("C40", "G40")
STEPS_MAIN = 2800
STEPS_SETTLE_CHECK = 1400
SETTLE_THETA = 39.0
SETTLE_CFG = "G40"
C_THR_LAB = gs.c_thr(3.0, 0.4, bar="lab")

FROZEN_PREDICTIONS = """
Reproduction precondition: this cycle's own freshly-run EMPTY leg at
theta in {36..42} (1deg step) for C40/G40 must reproduce
experiments/076-.../results.json::headline's C40/G40 values at those
same integer-degree points, max|delta| < 1e-9 -- BEFORE the article-
loaded leg is trusted.

Primary metric: A_scene = ptp(C(G40;theta,article) - C(C40;theta,article))
over theta in {36..42}; A_empty = ptp(C_empty(G40;theta) -
C_empty(C40;theta)) over the SAME 7 angles, this cycle's own fresh run;
ratio = A_scene / A_empty.
  SURVIVES:      ratio in [0.5, 2.0]
  CANCELS:       ratio <= 0.2
  INCONCLUSIVE:  0.2 < ratio < 0.5, OR ratio > 2.0

Secondary (disclosed, not gating): A_scene / C_thr (C_thr=0.005).

Settling precondition (disclosed, not gating): |C(G40,theta=39,article,
STEPS=2800) - C(G40,theta=39,article,STEPS=1400)| reported for context,
no pass/fail threshold (single directional check, not full R3).
"""


def assert_lab_clean():
    import subprocess
    out = subprocess.run(["git", "diff", "--stat", "--", "lab/"],
                          cwd=ROOT, capture_output=True, text=True).stdout.strip()
    assert out == "", f"lab/ is dirty -- the no-new-machinery position fails:\n{out}"
    return "clean"


def build_article(sim, cx, cy):
    """The established flagship absorber -- bit-identical to
    experiments/024-.../run.py::build("absorber"): PEC core to r=30,
    graded_black_shell shell 30->R_OUT. Not a new variant."""
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


def main():
    print("=" * 78)
    print("exp-082 -- PAD-loaded real-article check")
    print("=" * 78)
    print(FROZEN_PREDICTIONS)

    print(assert_lab_clean())

    jobs = []
    for key in PAIR_KEYS:
        for th in THETAS:
            jobs.append((key, th, False, STEPS_MAIN))   # empty
            jobs.append((key, th, True, STEPS_MAIN))    # scene (article)
    jobs.append((SETTLE_CFG, SETTLE_THETA, True, STEPS_SETTLE_CHECK))

    print(f"\n{len(jobs)} FDTD calls queued (2 configs x 7 angles x 2 legs "
          f"+ 1 settling-precondition call)")
    t0 = time.time()
    results = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for key, th, art, steps, prof, dt in ex.map(one_call, jobs):
            results[(key, th, art, steps)] = prof
            done = len(results)
            print(f"  [{done:2d}/{len(jobs)}] {key} theta={th:+05.1f} "
                  f"article={art} steps={steps} ({dt:5.1f}s)", flush=True)
    print(f"\ntotal wall time: {time.time() - t0:.1f}s")

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
        verdict = "SURVIVES"
    elif ratio <= 0.2:
        verdict = "CANCELS"
    else:
        verdict = "INCONCLUSIVE"

    print("\n[primary metric]")
    print(f"  delta_scene(theta) = {delta_scene.tolist()}")
    print(f"  delta_empty(theta) = {delta_empty.tolist()}")
    print(f"  A_scene (ptp) = {A_scene:.6e}   A_empty (ptp) = {A_empty:.6e}")
    print(f"  ratio = A_scene/A_empty = {ratio:.4f}")
    print(f"  VERDICT: {verdict}")

    print("\n[secondary metric, disclosed not gating]")
    a_scene_over_cthr = A_scene / C_THR_LAB
    print(f"  A_scene / C_thr = {a_scene_over_cthr:.4f}  (C_thr={C_THR_LAB})")

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
        # nearest committed theta (float key match at 1e-9)
        ref_c40_th = next(v for k, v in ref_c40.items() if abs(k - th) < 1e-6)
        ref_g40_th = next(v for k, v in ref_g40.items() if abs(k - th) < 1e-6)
        d40 = abs(c40_Ce - ref_c40_th)
        d80 = abs(g40_Ce - ref_g40_th)
        repro[th] = dict(C40_dev=d40, G40_dev=d80)
        max_dev = max(max_dev, d40, d80)
    repro_pass = bool(max_dev < 1e-9)
    print("\n[reproduction precondition -- fresh empty leg vs exp-076 committed]")
    for th, v in repro.items():
        print(f"  theta={th:+05.1f}  C40_dev={v['C40_dev']:.3e}  G40_dev={v['G40_dev']:.3e}")
    print(f"  max_dev = {max_dev:.3e}  PASS(<1e-9) = {repro_pass}")

    # ------------------------------------------------------- settling precondition
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
    print(f"  C(G40,39deg,article,STEPS=2800) = {r2800['C']:.6e}")
    print(f"  C(G40,39deg,article,STEPS=1400) = {r1400['C']:.6e}")
    print(f"  abs_dev = {settle_abs_dev:.3e}  rel_dev = {settle_rel_dev:.4f}")

    out = dict(
        frozen_predictions=FROZEN_PREDICTIONS,
        thetas=THETAS, pair_keys=PAIR_KEYS, steps_main=STEPS_MAIN,
        per_theta=per_theta,
        delta_scene=delta_scene.tolist(), delta_empty=delta_empty.tolist(),
        A_scene=A_scene, A_empty=A_empty, ratio=ratio, verdict=verdict,
        c_thr_lab=C_THR_LAB, a_scene_over_cthr=a_scene_over_cthr,
        reproduction_precondition=dict(per_theta=repro, max_dev=max_dev, passed=repro_pass),
        settling_precondition=dict(
            steps_main=STEPS_MAIN, steps_check=STEPS_SETTLE_CHECK,
            theta=SETTLE_THETA, cfg=SETTLE_CFG,
            C_steps2800=r2800["C"], C_steps1400=r1400["C"],
            abs_dev=settle_abs_dev, rel_dev=settle_rel_dev),
    )
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
