"""
experiments/078-t28-y-wall-echo-prescreen/phase4_null_calibration_corrected.py
============================================================================
PHASE 4, Panel Iteration 55, exp-078. Mandatory-fix docket item 6
(`phase2_redteam_audit.md`): a fresh null-calibration control against the
CORRECTED primary model (post Phase-3's angle-convention fix), at this
program's own house 20,000-trial standard (R5/exp-070/exp-077 precedent) --
not the 2,000-trial, disclosed time-budget reduction QUANTUM's own Phase-2
critique (`phase2_quantum_null_check.py`) ran against the WRONG (as-filed,
angle-uncorrected) model. Red Team's audit was explicit that the Phase-2
control could not and did not answer whether the CORRECTED 0/3-SUPPORT
picture is itself informative or merely what a structurally different
(but still noise-indistinguishable) model produces -- this file answers
that, new information not available before Phase 4.

ZERO new FDTD calls. Imports, never reimplements (R4): identical pattern to
`phase2_quantum_null_check.py` (`y_wall_prescreen.py`'s own
`_free_period_search` and staged-widening stage list), reading `TARGETS`/
`OBSERVED` from the now-CORRECTED `y_wall_prescreen_results.json` (Phase 3
folded the angle fix into `y_wall_prescreen.py` itself and Phase 4 already
re-ran it -- this file reads that committed corrected JSON, not the
as-filed one).

WHAT CHANGED vs `phase2_quantum_null_check.py`, and why this is a
DIFFERENT file rather than a mutated re-run of that one: QUANTUM's own
Phase-2 critique is a historical, already-cited artifact (Red Team's audit
cross-checked its committed output/JSON line by line) -- it is not
retargeted or overwritten here. This file is Phase 4's own, separate,
fresh instrument, at `n_trials=20,000` (not 2,000), reading the corrected
results.

Run: `python3 phase4_null_calibration_corrected.py` from this directory.
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


# ---- import the (now-corrected) proposal's own module (does NOT run
# main() -- guarded) ----
ywp = _load(os.path.join(HERE, "y_wall_prescreen.py"), "_exp078_phase4_ywp")
_free_period_search = ywp._free_period_search

# ---- real data + already-computed CORRECTED model results, read from the
# committed JSON (post Phase-3/4 angle fix), never hand-typed (R4) ----
with open(os.path.join(HERE, "y_wall_prescreen_results.json")) as f:
    RESULTS = json.load(f)

with open(os.path.join(ROOT, "experiments", "076-t28-g40-pad-decorrelation", "results.json")) as f:
    res76 = json.load(f)
THETAS = np.array(res76["headline"]["theta"])
N = len(THETAS)

REFERENCE_PERIODS = RESULTS["reference_periods_deg"]
PRIMARY_SCORES = RESULTS["primary_model_scores"]  # CORRECTED, post Phase-3 fix

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
    `free_period_with_widening` -- silent, for 20,000-trial loops. Reuses
    the imported `_free_period_search` for every stage; only the
    stage-stepping loop is authored here."""
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
    n_trials = 20000  # house standard (R5/exp-070/exp-077), not QUANTUM's own
    # Phase-2 2,000-trial disclosed reduction -- this IS the full-scale check.
    seed = 7
    N_LOCAL = N
    rng = np.random.default_rng(seed)

    print("=" * 78)
    print("exp-078 Phase 4 -- fresh 20,000-trial null-calibration against the")
    print("CORRECTED primary model (mandatory-fix docket item 6)")
    print("=" * 78)
    print(f"n_trials={n_trials}, seed={seed}, N={N_LOCAL} points (real theta grid, "
          f"36-42deg, 0.2deg step) -- i.i.d. N(0,1) noise, scale-invariant for "
          f"P*/R^2. Targets read from the CORRECTED y_wall_prescreen_results.json "
          f"(post Phase-3 angle-convention fix), not the as-filed (wrong-angle) "
          f"numbers QUANTUM's own Phase-2 control (n_trials=2,000) targeted.")
    observed_n_support = sum(1 for k in TARGETS if OBSERVED[k][0] <= 0.30)
    print(f"OBSERVED (corrected primary model): {observed_n_support} of 3 comparisons "
          f"SUPPORT (c80_c40 rel_dev={OBSERVED['c80_c40'][0]:.4f}, "
          f"pair_pad rel_dev={OBSERVED['pair_pad'][0]:.4f}, "
          f"pair_absorb40 rel_dev={OBSERVED['pair_absorb40'][0]:.4f}) -- note this is "
          f"0/3 under the corrected model (down from the as-filed 2/3), so the "
          f"per-target 'how close to real is this, relative to noise' questions below "
          f"are the informative ones; the joint 'P(>=2 of 3 SUPPORT)' framing QUANTUM's "
          f"Phase-2 control used no longer applies to an observed count of 0.")

    out = {"n_trials": n_trials, "seed": seed, "n_points": int(N_LOCAL),
           "targets_corrected_model": True, "per_target": {}, "observed": {}}

    # ---- [1] per-target single-comparison null ----
    print(f"\n[1] PER-COMPARISON NULL (independent {n_trials}-trial noise draw per target)")
    for key, p_real in TARGETS.items():
        obs_rel_dev, obs_p_model, obs_r2 = OBSERVED[key]
        rel_dev_le_030 = np.empty(n_trials, dtype=bool)
        r2_ge_obs = np.empty(n_trials, dtype=bool)
        rel_dev_le_obs = np.empty(n_trials, dtype=bool)
        window_counts = {"narrow[1,4]": 0, "wide[1,15]": 0, "widest[1,60]": 0}
        for i in range(n_trials):
            noise = rng.normal(0.0, 1.0, size=N_LOCAL)
            fit = staged_free_period_quiet(THETAS, noise)
            window_counts[fit["window"]] += 1
            rd = rel_dev(p_real, fit["p_star_deg"])
            rel_dev_le_030[i] = rd <= 0.30
            rel_dev_le_obs[i] = rd <= obs_rel_dev
            r2_ge_obs[i] = fit["r_squared"] >= obs_r2
        p_support = float(np.mean(rel_dev_le_030))
        p_close_as_obs = float(np.mean(rel_dev_le_obs))
        p_r2 = float(np.mean(r2_ge_obs))
        print(f"    {key:>15} (target P*={p_real:.4f}deg, observed rel_dev={obs_rel_dev:.4f}, "
              f"observed R^2={obs_r2:.4f}):")
        print(f"        P(null rel_dev<=0.30) = {p_support:.4f}   "
              f"P(null rel_dev<=observed={obs_rel_dev:.4f}) = {p_close_as_obs:.4f}   "
              f"P(null R^2>={obs_r2:.4f}) = {p_r2:.4f}")
        print(f"        window distribution under null: {window_counts}")
        out["per_target"][key] = dict(p_real_deg=p_real, p_null_rel_dev_le_030=p_support,
                                       p_null_rel_dev_le_observed=p_close_as_obs,
                                       p_null_r2_ge_observed=p_r2,
                                       window_counts=window_counts)
        out["observed"][key] = dict(rel_dev=obs_rel_dev, p_model_deg=obs_p_model, r_squared=obs_r2)

    # ---- [2] joint check, retained for direct comparability with QUANTUM's
    # own Phase-2 metric, though OBSERVED is now 0-of-3 under the corrected
    # model (the joint metric's own interpretation shifts accordingly -- see
    # print note above and phase4_results.md) ----
    print("\n[2] JOINT NULL -- 3 independent noise curves per trial (one per target), "
          "count of SUPPORTs (rel_dev<=0.30) out of 3, vs the OBSERVED count "
          f"({observed_n_support} of 3, corrected model)")
    joint_counts = np.zeros(n_trials, dtype=int)
    targets_list = list(TARGETS.items())
    for i in range(n_trials):
        c = 0
        for key, p_real in targets_list:
            noise = rng.normal(0.0, 1.0, size=N_LOCAL)
            fit = staged_free_period_quiet(THETAS, noise)
            if rel_dev(p_real, fit["p_star_deg"]) <= 0.30:
                c += 1
        joint_counts[i] = c

    dist = {k: int(np.sum(joint_counts == k)) / n_trials for k in range(4)}
    p_le_observed = float(np.mean(joint_counts <= observed_n_support))
    print(f"    distribution of #SUPPORT-out-of-3 under null: {dist}")
    print(f"    P(<= observed count of {observed_n_support} of 3 SUPPORT under null) = "
          f"{p_le_observed:.4f}  (a LOW value here would mean the corrected model "
          f"clears SUPPORT unusually RARELY vs noise -- not evidence for the mechanism "
          f"either way; this metric mainly documents that {observed_n_support}-of-3 is, "
          f"as expected, an unremarkable outcome under a null with no relationship to "
          f"reality)")
    out["joint"] = dict(distribution_k_of_3=dist, p_le_observed_count=p_le_observed,
                         observed_n_support=observed_n_support)

    out_path = os.path.join(HERE, "phase4_null_calibration_corrected_results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
