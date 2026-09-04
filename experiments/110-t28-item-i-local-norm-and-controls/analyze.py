"""exp-110 Phase 4 analysis: gate_p0, reproduction_precondition, item 1a/1b/
1c/1d (re-capture fidelity, per-bin persistence, mirror pooled floor), the
R27 cost gate, and text/DISCLAIMER assembly (R23). Panel Iteration 87.
Zero new machinery beyond what run.py declares; this file only loads
chunk_runner.py's own pickles and calls run.py's functions.
"""
import json
import os
import pickle
import sys

import numpy as np

sys.path.insert(0, "/home/user/photon-lab/experiments/110-t28-item-i-local-norm-and-controls")
sys.path.insert(0, "/home/user/photon-lab")
import run as R  # noqa: E402
import chunk_runner as CR  # noqa: E402
from lab import sections as sc  # noqa: E402


def load(r, which):
    path = os.path.join(CR.SCRATCH, f"r{r}_{which}_done.pkl")
    with open(path, "rb") as f:
        return pickle.load(f)


def have(r, which):
    return os.path.exists(os.path.join(CR.SCRATCH, f"r{r}_{which}_done.pkl"))


def analyze_r(r):
    de = load(r, "empty")
    dh = load(r, "hollow")
    dp = load(r, "peccored")
    g = de["g"]
    cap_e = de["cap"]
    cap_h, sigma_e_h, ez_h = dh["cap"], dh["sigma_e"], dh["ez"]
    cap_p, sigma_e_p, ez_p = dp["cap"], dp["sigma_e"], dp["ez"]

    gate_p0 = R.gate_p0(g)
    repro = R.reproduction_precondition(cap_p, cap_e, g)
    repro_108 = R.reproduction_precondition_108(cap_p, cap_e, g)

    raw_patterns = {}
    local_diag = {}
    bin_centers_deg = None
    for m in R.MARGINS:
        box = g["margin_boxes"][m]
        centers_p, pat_p = sc.angular_scattered_pattern(cap_p, cap_e, box, g["ref"])
        centers_h, pat_h = sc.angular_scattered_pattern(cap_h, cap_e, box, g["ref"])
        if bin_centers_deg is None:
            bin_centers_deg = centers_p.tolist()
        pat_delta = pat_p - pat_h
        raw_patterns[m] = dict(peccored=pat_p.tolist(), hollow=pat_h.tolist(), delta=pat_delta.tolist())
        local_diag[m] = R.classify_item_i_local(r, m, pat_p, pat_h, pat_delta)

    # item i (existing, frozen classifier -- unchanged, reproduced for continuity)
    pattern_delta_by_m = {m: np.array(raw_patterns[m]["delta"]) for m in R.MARGINS}
    pattern_peccored_by_m = {m: np.array(raw_patterns[m]["peccored"]) for m in R.MARGINS}
    item_i = R.classify_item_i(pattern_delta_by_m, pattern_peccored_by_m, r)

    n_resolved = {m: local_diag[m]["n_resolved"] for m in R.MARGINS}
    n_total = {m: local_diag[m]["n_total"] for m in R.MARGINS}

    named_bins = {156: -146.25, 312: 168.75}
    named_deg = named_bins[r]
    named_idx = int(np.argmin(np.abs(np.array(bin_centers_deg) - named_deg)))
    named_bin_status = dict(
        margin32=dict(
            deg=bin_centers_deg[named_idx],
            resolved=local_diag[32]["resolved"][named_idx],
            local_rel=local_diag[32]["local_rel"][named_idx],
        )
    )

    return dict(r=r, gate_p0=gate_p0, reproduction_precondition=repro,
                reproduction_precondition_108=repro_108,
                item_i=item_i, raw_patterns=raw_patterns, local_diag=local_diag,
                n_resolved=n_resolved, n_total=n_total,
                bin_centers_deg=bin_centers_deg, named_bin_status=named_bin_status,
                total_wall_s=dict(empty=CR.total_wall_time(r, "empty"),
                                   hollow=CR.total_wall_time(r, "hollow"),
                                   peccored=CR.total_wall_time(r, "peccored")))


if __name__ == "__main__":
    results = {}
    n_fdtd_calls = 0
    total_wall_s = 0.0

    # r=156 always attempted first (the pilot leg)
    if have(156, "empty") and have(156, "hollow") and have(156, "peccored"):
        print(f"\n{'='*70}\nAnalyzing r=156\n{'='*70}")
        row156 = analyze_r(156)
        results["r156"] = row156
        n_fdtd_calls += 3
        total_wall_s += sum(row156["total_wall_s"].values())
        print(f"gate_p0 pass={row156['gate_p0']['pass_']}")
        print(f"reproduction_precondition pass={row156['reproduction_precondition']['pass_']}")
        print(f"item_i verdict={row156['item_i']['verdict']}")
        for m in R.MARGINS:
            print(f"  margin={m}: n_resolved={row156['n_resolved'][m]}/{row156['n_total'][m]}")

        pilot_empty = row156["total_wall_s"]["empty"]
        pilot_total = sum(row156["total_wall_s"].values())
        cost_gate = R.cost_gate_check(pilot_empty, pilot_total)
        print(f"\nR27 cost gate: {json.dumps(cost_gate, indent=2)}")
    else:
        cost_gate = None
        print("r=156 captures not yet complete; run chunk_runner.py for empty/hollow/peccored at r=156 first.")

    r312_deferred = None
    if cost_gate is not None and cost_gate["proceed_to_r312"]:
        if have(312, "empty") and have(312, "hollow") and have(312, "peccored"):
            print(f"\n{'='*70}\nAnalyzing r=312\n{'='*70}")
            row312 = analyze_r(312)
            results["r312"] = row312
            n_fdtd_calls += 3
            total_wall_s += sum(row312["total_wall_s"].values())
            print(f"gate_p0 pass={row312['gate_p0']['pass_']}")
            print(f"reproduction_precondition pass={row312['reproduction_precondition']['pass_']}")
            print(f"item_i verdict={row312['item_i']['verdict']}")
            for m in R.MARGINS:
                print(f"  margin={m}: n_resolved={row312['n_resolved'][m]}/{row312['n_total'][m]}")
            r312_deferred = False
        else:
            print("Cost gate cleared for r=312 but captures not yet complete; run chunk_runner.py for r=312.")
    elif cost_gate is not None:
        r312_deferred = True
        print("R27 cost gate did NOT clear for r=312 -- deferred, NOT-RUN (not silently skipped).")

    results["n_fdtd_calls"] = n_fdtd_calls
    results["total_wall_s"] = total_wall_s
    results["cost_gate"] = cost_gate
    results["r312_deferred"] = r312_deferred

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nWritten: {out_path}")
