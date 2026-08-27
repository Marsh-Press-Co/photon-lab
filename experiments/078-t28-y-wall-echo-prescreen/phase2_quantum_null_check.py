"""
experiments/078-t28-y-wall-echo-prescreen/phase2_quantum_null_check.py
============================================================================
PHASE 2 -- QUANTUM OPTICS blind critique, Panel Iteration 55, exp-078.

Answers this cycle's own §7/§8-open-question-1 directly, by RUNNING the
check the proposal names as its own cheapest next move rather than only
arguing about it: does a null-permutation control (R5's own standing house
rule, generalized at its Iteration-47 addendum to exactly this kind of
"a period match, found without a look-elsewhere control, is not by itself
evidence" situation) show `rel_dev<=0.30` in 2 of 3 comparisons is
distinguishable from chance over this narrow window?

ZERO new FDTD calls. Imports, never reimplements (R4):
  - `y_wall_prescreen.py` (exp-078, this directory): `run69`
    (`_free_period_search`), the real `thetas` grid, and the already-
    computed `REFERENCE_PERIODS` / `primary_model_pair_deltas` results
    (read from the committed JSON, not hand-typed).
  - `pad_round_trip_model.py` (exp-077): the null-generation PATTERN this
    file is explicitly asked to reuse (i.i.d. Gaussian noise, scale-invariant
    for period/R^2 purposes, `seed=7`; this Phase-2 critique turn runs
    `n_trials=2,000` as a disclosed time-budget reduction from this
    program's own usual 20,000-trial standard -- see the runtime print
    below -- not the full house standard) -- the STAGED-
    WIDENING HARNESS (narrow[1,4]->wide[1,15]->widest[1,60]) is copied
    verbatim from `y_wall_prescreen.py`'s own `free_period_with_widening`
    (a data structure -- the stage list -- not a reimplementation of the
    underlying `_free_period_search` algorithm, which is imported).

WHAT THIS FILE DOES:
  [1] For EACH of the three primary-model comparisons (`c80_c40`,
      `pair_pad`, `pair_absorb40`), draw `n_trials` (2,000 this run;
      see the runtime print for the disclosed reduction from this
      program's usual 20,000) independent i.i.d. N(0,1) 31-point noise
      curves on the REAL angle grid, run them through
      the IDENTICAL staged free-period search y_wall_prescreen.py's own
      model curves went through, and compute P(rel_dev<=0.30) and
      P(R^2>=observed) against that comparison's own real reference period
      -- the single-comparison look-elsewhere rate.
  [2] A JOINT check: per null trial, draw THREE independent noise curves
      (matching the fact that the real analysis fits three independent
      model curves), score each against its own target, and report the
      distribution of "how many of 3 clear SUPPORT (rel_dev<=0.30)" -- to
      answer whether "2 of 3 SUPPORT" is itself an unremarkable rate under
      a null with NO relationship to reality.

Run: `python3 phase2_quantum_null_check.py` from this directory.
"""

import importlib.util
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# ---- import the proposal's own module (does NOT run main() -- guarded) ----
ywp = _load(os.path.join(HERE, "y_wall_prescreen.py"), "_exp078_phase2_ywp")
_free_period_search = ywp._free_period_search

# ---- real data + already-computed model results, read from committed JSON,
# never hand-typed (R4) ----
with open(os.path.join(HERE, "y_wall_prescreen_results.json")) as f:
    RESULTS = json.load(f)

with open(os.path.join(ROOT, "experiments", "076-t28-g40-pad-decorrelation", "results.json")) as f:
    res76 = json.load(f)
THETAS = np.array(res76["headline"]["theta"])
N = len(THETAS)

REFERENCE_PERIODS = RESULTS["reference_periods_deg"]
PRIMARY_SCORES = RESULTS["primary_model_scores"]

TARGETS = {
    "c80_c40": REFERENCE_PERIODS["c80_c40_deg"],
    "pair_pad": REFERENCE_PERIODS["pair_pad_deg"],
    "pair_absorb40": REFERENCE_PERIODS["pair_absorb40_deg"],
}
OBSERVED = {
    "c80_c40": (PRIMARY_SCORES["c80_c40_vs_2.8421"]["rel_dev"],
                PRIMARY_SCORES["c80_c40_vs_2.8421"]["p_model_deg"],
                RESULTS["primary_model_pair_deltas"]["c80_c40"]["r_squared"]),
    "pair_pad": (PRIMARY_SCORES["pair_pad_vs_4.6113"]["rel_dev"],
                 PRIMARY_SCORES["pair_pad_vs_4.6113"]["p_model_deg"],
                 RESULTS["primary_model_pair_deltas"]["pair_pad"]["r_squared"]),
    "pair_absorb40": (PRIMARY_SCORES["pair_absorb40_vs_4.1761"]["rel_dev"],
                       PRIMARY_SCORES["pair_absorb40_vs_4.1761"]["p_model_deg"],
                       RESULTS["primary_model_pair_deltas"]["pair_absorb40"]["r_squared"]),
}

# ---- staged-widening harness, STAGE LIST copied verbatim from
# y_wall_prescreen.py's own free_period_with_widening (the data, not the
# search algorithm -- _free_period_search is imported) ----
STAGES = [
    dict(name="narrow[1,4]", lo_deg=1.0, hi_deg=4.0, n_grid=400),
    dict(name="wide[1,15]", lo_deg=1.0, hi_deg=15.0, n_grid=2800),
    dict(name="widest[1,60]", lo_deg=1.0, hi_deg=60.0, n_grid=6000),
]


def staged_free_period_quiet(thetas, delta):
    """Same staged-widening idiom as y_wall_prescreen.py's own
    `free_period_with_widening` (and pad_round_trip_model.py's own
    `_quiet` variant of the same idiom for Monte Carlo use) -- silent,
    for 20,000-trial loops. Reuses the imported `_free_period_search`
    for every stage; only the stage-stepping loop is authored here,
    matching this program's own established pattern for null-generation
    harnesses."""
    chosen = None
    for st in STAGES:
        fit = _free_period_search(thetas, delta, center_deg=39.0,
                                   lo_deg=st["lo_deg"], hi_deg=st["hi_deg"],
                                   n_grid=st["n_grid"])
        p = fit["p_star_deg"]
        at_boundary = (p <= st["lo_deg"] * 1.005) or (p >= st["hi_deg"] * 0.995)
        rec = dict(p_star_deg=p, r_squared=fit["r_squared"], at_boundary=at_boundary,
                   window=st["name"])
        if chosen is None or (chosen["at_boundary"] and not at_boundary):
            chosen = rec
        if not at_boundary:
            break
    return chosen


def rel_dev(p_real, p_model):
    return abs(p_model - p_real) / p_real


def main():
    n_trials = 2000
    seed = 7
    rng = np.random.default_rng(seed)

    print("=" * 78)
    print("exp-078 Phase 2 (QUANTUM OPTICS) -- null-permutation control on the")
    print("proposal's own three primary Test-A period comparisons")
    print("=" * 78)
    print(f"n_trials={n_trials}, seed={seed}, N={N} points (real theta grid, "
          f"36-42deg, 0.2deg step) -- i.i.d. N(0,1) noise, scale-invariant for "
          f"P*/R^2 (fit is linear-least-squares in a fixed cos/sin basis). "
          f"NOTE: n_trials=2,000 not this program's usual 20,000 (R5/exp-070/"
          f"exp-077 precedent) -- disclosed time-budget reduction for a single "
          f"Phase-2 critique turn (the staged search's Python-loop grid "
          f"evaluation, imported unmodified per R4, costs ~30-40ms/trial); "
          f"SE of an estimated proportion near p=0.3 at n=2,000 is ~1.0pp, "
          f"sufficient to resolve the questions asked here (is the observed "
          f"rate order-of-magnitude consistent with chance, not a precision "
          f"estimate of a small tail probability).")

    out = {"n_trials": n_trials, "seed": seed, "n_points": int(N), "per_target": {},
           "observed": {}}

    # ---- [1] per-target single-comparison null ----
    print(f"\n[1] PER-COMPARISON NULL (independent {n_trials}-trial noise draw per target)")
    single_hits = {}  # trial-indexed boolean arrays, for the joint check below
    for key, p_real in TARGETS.items():
        obs_rel_dev, obs_p_model, obs_r2 = OBSERVED[key]
        rel_dev_le_030 = np.empty(n_trials, dtype=bool)
        r2_ge_obs = np.empty(n_trials, dtype=bool)
        window_counts = {"narrow[1,4]": 0, "wide[1,15]": 0, "widest[1,60]": 0}
        for i in range(n_trials):
            noise = rng.normal(0.0, 1.0, size=N)
            fit = staged_free_period_quiet(THETAS, noise)
            window_counts[fit["window"]] += 1
            rd = rel_dev(p_real, fit["p_star_deg"])
            rel_dev_le_030[i] = rd <= 0.30
            r2_ge_obs[i] = fit["r_squared"] >= obs_r2
        p_support = float(np.mean(rel_dev_le_030))
        p_r2 = float(np.mean(r2_ge_obs))
        single_hits[key] = rel_dev_le_030
        print(f"    {key:>15} (target P*={p_real:.4f}deg, observed rel_dev={obs_rel_dev:.4f}, "
              f"observed R^2={obs_r2:.4f}):")
        print(f"        P(null rel_dev<=0.30) = {p_support:.4f}   "
              f"P(null R^2>={obs_r2:.4f}) = {p_r2:.4f}")
        print(f"        window distribution under null: {window_counts}")
        out["per_target"][key] = dict(p_real_deg=p_real, p_null_rel_dev_le_030=p_support,
                                       p_null_r2_ge_observed=p_r2,
                                       window_counts=window_counts)
        out["observed"][key] = dict(rel_dev=obs_rel_dev, p_model_deg=obs_p_model, r_squared=obs_r2)

    # ---- [2] joint check: 3 independent noise curves per trial, how many of 3
    # clear SUPPORT (rel_dev<=0.30) against their OWN target, matching the
    # real analysis's structure (three independently-fit model curves) ----
    print("\n[2] JOINT NULL -- 3 independent noise curves per trial (one per target), "
          "count of SUPPORTs (rel_dev<=0.30) out of 3, vs the OBSERVED count (2 of 3)")
    joint_counts = np.zeros(n_trials, dtype=int)
    targets_list = list(TARGETS.items())
    for i in range(n_trials):
        c = 0
        for key, p_real in targets_list:
            noise = rng.normal(0.0, 1.0, size=N)
            fit = staged_free_period_quiet(THETAS, noise)
            if rel_dev(p_real, fit["p_star_deg"]) <= 0.30:
                c += 1
        joint_counts[i] = c

    dist = {k: int(np.sum(joint_counts == k)) / n_trials for k in range(4)}
    p_ge2 = float(np.mean(joint_counts >= 2))
    observed_n_support = sum(1 for k in TARGETS if OBSERVED[k][0] <= 0.30)
    print(f"    distribution of #SUPPORT-out-of-3 under null: {dist}")
    print(f"    P(>=2 of 3 SUPPORT under null, independent noise, no relationship "
          f"to reality) = {p_ge2:.4f}")
    print(f"    OBSERVED: {observed_n_support} of 3 comparisons SUPPORT "
          f"(c80_c40={OBSERVED['c80_c40'][0]:.4f}, pair_pad={OBSERVED['pair_pad'][0]:.4f}, "
          f"pair_absorb40={OBSERVED['pair_absorb40'][0]:.4f})")
    out["joint"] = dict(distribution_k_of_3=dist, p_ge2_of_3=p_ge2,
                         observed_n_support=observed_n_support)

    out_path = os.path.join(HERE, "phase2_quantum_null_check_results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
