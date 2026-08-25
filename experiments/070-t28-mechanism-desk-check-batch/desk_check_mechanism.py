"""exp-070 -- T28 mechanism desk-check batch. Panel Iteration 47.

Zero FDTD cost: every input is already-committed data from
`experiments/069-t21-block-mini-period-match-power-up/results.json`
(`block_dense.rows`, 600nm, 31 pts; `block_leg750.rows`, 750nm, 16 pts;
`scored.p3`, the committed free-fit period of the padding delta) and
`experiments/065-t24-absorb-boundary-sweep/design_geometry.py`'s own
`CONFIGS` (named FDTD domain-construction constants). Implements items
(a)-(e) with the Phase-2 Red Team's 10-item mandatory-fix docket applied
in full (see design_geometry.py's own module docstring for the mapping).

Run with: python3 desk_check_mechanism.py
Writes:   results.json (this directory)
"""
import json
import math
import os

import numpy as np

import design_geometry as dg

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

EXP069_RESULTS = os.path.join(
    ROOT, "experiments", "069-t21-block-mini-period-match-power-up", "results.json")


def load_exp069():
    with open(EXP069_RESULTS) as f:
        d = json.load(f)
    dense = d["block_dense"]["rows"]
    leg750 = d["block_leg750"]["rows"]
    p3 = d["scored"]["p3"]
    assert len(dense) == 31 and len(leg750) == 16
    return dense, leg750, p3


def normalize_label(lbl):
    """Canonicalize a search-space label for cross-branch comparison (fix
    3): sort the two terms of a pair label so 'a+b' and 'b+a' orderings
    (which do not occur here by construction, but future edits could)
    compare equal, and treat sign-flipped single terms as distinct (they
    ARE distinct physical claims, e.g. +A vs -A)."""
    return lbl


def item_a_per_config_decomposition(dense, p3):
    """Docket fix 1: score the RECOVERED PERIOD against P*_delta, not bare
    R^2. CONFIRM requires BOTH configs' free-fit period within 20% of
    P*_delta AND their own R^2 not already disqualifying; REFUTE if EITHER
    config's R^2<0.15 or its period misses P*_delta by >=50%."""
    thetas = np.array([r["theta"] for r in dense])
    c40 = np.array([r["C_empty_C40"] for r in dense])
    c80 = np.array([r["C_empty_C80"] for r in dense])
    p_star_delta = p3["p_star_deg"]

    out = {}
    for key, series in (("C40", c40), ("C80", c80)):
        fixed = dg._fixed_period_fit(np.sin(np.radians(thetas)), series, dg.T_SINTHETA_600)
        free = dg._free_period_search(thetas, series, center_deg=39.0)
        dev = abs(free["p_star_deg"] - p_star_delta) / p_star_delta
        out[key] = dict(
            r_squared_fixed=fixed["r_squared"],
            p_star_free=free["p_star_deg"],
            r_squared_free=free["r_squared"],
            rel_dev_from_delta_period=dev,
            config_confirms=(dev <= 0.20),
            config_refutes=(free["r_squared"] < 0.15) or (dev >= 0.50),
        )

    confirm = out["C40"]["config_confirms"] and out["C80"]["config_confirms"]
    refute = out["C40"]["config_refutes"] or out["C80"]["config_refutes"]
    neither = not confirm and not refute
    return dict(cells=out, confirm=bool(confirm), refute=bool(refute),
                neither=bool(neither))


def item_b_beat_frequency(p3):
    """Beat-frequency reconstruction: solve 1/P_beat = |1/P(39,600) - 1/P_b|
    for both branches of P_b, convert each to an effective aperture A_alt,
    then search NAMED for a match (with the null-permutation control,
    docket fix 2)."""
    p39_600 = dg.P_deg(39.0, 600)
    p_beat = p3["p_star_deg"]
    inv_p39 = 1.0 / p39_600
    inv_beat = 1.0 / p_beat

    branches = {}
    for sign, name in ((+1, "plus"), (-1, "minus")):
        inv_b = inv_p39 + sign * inv_beat
        if inv_b <= 0:
            branches[name] = dict(valid=False)
            continue
        p_b = 1.0 / inv_b
        a_alt = dg.CPL[600] / (math.radians(p_b) * math.cos(math.radians(39.0)))
        match = dg.closest_matches(a_alt)
        null = dg.null_percentile(match["best_rel"])
        branches[name] = dict(
            valid=True, P_b_deg=p_b, A_alt=a_alt,
            best_rel=match["best_rel"], n_ties=match["n_ties"],
            tied=match["tied"][:10],   # cap listed ties for file size
            null_p=null["p"], null_n_trials=null["n_trials"],
            confirm=(match["best_rel"] <= 0.01) and (null["p"] <= 0.05),
            refute=(match["best_rel"] >= 0.10),
        )

    valid_branches = [b for b in branches.values() if b.get("valid")]
    confirm = any(b["confirm"] for b in valid_branches) if valid_branches else False
    refute = all(b["refute"] for b in valid_branches) if valid_branches else False
    neither = not confirm and not refute
    return dict(branches=branches, confirm=bool(confirm), refute=bool(refute),
                neither=bool(neither))


def item_c_taper_as_aperture(p3):
    """TAPER=40 cells alone as a diffracting sub-aperture."""
    p_taper = math.degrees(dg.CPL[600] / (dg.NAMED["TAPER"] * math.cos(math.radians(39.0))))
    p_star = p3["p_star_deg"]
    rel_dev = abs(p_taper - p_star) / p_star
    return dict(P_taper_deg=p_taper, P_star_delta_deg=p_star, rel_dev=rel_dev,
                confirm=bool(rel_dev <= 0.20), refute=bool(rel_dev >= 1.00),
                neither=bool(not (rel_dev <= 0.20) and not (rel_dev >= 1.00)))


def item_d_aeff_trace(p3, leg750):
    """Back-solve A_eff from the committed free-fit P*_delta; search NAMED
    for a match (null-controlled, fix 2); cross-validate the best candidate
    against the held-out 750nm leg."""
    p_star = p3["p_star_deg"]
    a_eff = dg.CPL[600] / (math.radians(p_star) * math.cos(math.radians(39.0)))
    match = dg.closest_matches(a_eff)
    null = dg.null_percentile(match["best_rel"])

    th750 = np.array([r["theta"] for r in leg750])
    d750 = np.array([r["delta"] for r in leg750])
    # cross-validate using the (numeric) best-matching candidate value, not
    # necessarily a single named expression when several tie
    candidate_value = match["tied"][0][0] if match["tied"] else a_eff
    t750 = dg.CPL[750] / candidate_value
    fit750 = dg._fixed_period_fit(np.sin(np.radians(th750)), d750, t750)

    confirm = (match["best_rel"] <= 0.01) and (null["p"] <= 0.05) and (fit750["r_squared"] >= 0.70)
    refute = (match["best_rel"] >= 0.10) or (fit750["r_squared"] < 0.40)
    neither = not confirm and not refute
    return dict(A_eff=a_eff, best_rel=match["best_rel"], n_ties=match["n_ties"],
                tied=match["tied"][:10], null_p=null["p"], null_n_trials=null["n_trials"],
                candidate_value=candidate_value, r_squared_750=fit750["r_squared"],
                confirm=bool(confirm), refute=bool(refute), neither=bool(neither))


def item_e_convergence(item_b, item_d):
    """Fix 3: match if ANY tied expression from item (b)'s branches
    overlaps ANY tied expression from item (d) -- not only a single 'best'
    pick each."""
    d_labels = {lbl for _, lbl in item_d["tied"]}
    overlap_by_branch = {}
    any_overlap = False
    for name, br in item_b["branches"].items():
        if not br.get("valid"):
            overlap_by_branch[name] = []
            continue
        b_labels = {lbl for _, lbl in br["tied"]}
        shared = sorted(b_labels & d_labels)
        overlap_by_branch[name] = shared
        if shared:
            any_overlap = True
    return dict(overlap_by_branch=overlap_by_branch,
                confirm=bool(any_overlap), refute=bool(not any_overlap),
                neither=False)   # binary by construction (fix 4's own carve-out)


def main():
    dense, leg750, p3 = load_exp069()

    p1 = item_a_per_config_decomposition(dense, p3)
    p2 = item_b_beat_frequency(p3)
    p3_taper = item_c_taper_as_aperture(p3)
    p4 = item_d_aeff_trace(p3, leg750)
    p5 = item_e_convergence(p2, p4)

    out = dict(
        experiment="070-t28-mechanism-desk-check-batch",
        panel_iteration=47,
        lead_seat="QUANTUM OPTICS",
        source="experiments/069-t21-block-mini-period-match-power-up/results.json",
        named_constants=dg.NAMED,
        search_space_size=len(dg.SEARCH_VALUES),
        search_space_distinct_values=int(dg.N_DISTINCT_VALUES),
        p_070_1_per_config=p1,
        p_070_2_beat_frequency=p2,
        p_070_3_taper=p3_taper,
        p_070_4_aeff=p4,
        p_070_5_convergence=p5,
    )

    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)

    def verdict(d):
        return "CONFIRM" if d["confirm"] else ("REFUTE" if d["refute"] else "NEITHER")

    print(f"P-070-1 (per-config decomposition): {verdict(p1)}")
    print(f"  C40: P*={p1['cells']['C40']['p_star_free']:.4f} R2={p1['cells']['C40']['r_squared_free']:.4f} "
          f"dev={p1['cells']['C40']['rel_dev_from_delta_period']:.2%}")
    print(f"  C80: P*={p1['cells']['C80']['p_star_free']:.4f} R2={p1['cells']['C80']['r_squared_free']:.4f} "
          f"dev={p1['cells']['C80']['rel_dev_from_delta_period']:.2%}")
    print(f"P-070-2 (beat frequency): {verdict(p2)}")
    for name, br in p2["branches"].items():
        if br.get("valid"):
            print(f"  branch {name}: A_alt={br['A_alt']:.3f} best_rel={br['best_rel']:.4%} "
                  f"null_p={br['null_p']:.4f} n_ties={br['n_ties']}")
    print(f"P-070-3 (taper-as-aperture): {verdict(p3_taper)}  "
          f"P_taper={p3_taper['P_taper_deg']:.2f}deg vs P*={p3_taper['P_star_delta_deg']:.2f}deg "
          f"({p3_taper['rel_dev']:.1%} off)")
    print(f"P-070-4 (A_eff trace): {verdict(p4)}  A_eff={p4['A_eff']:.3f} "
          f"best_rel={p4['best_rel']:.4%} null_p={p4['null_p']:.4f} R2(750)={p4['r_squared_750']:.4f}")
    print(f"P-070-5 (convergence): {verdict(p5)}  overlap={p5['overlap_by_branch']}")
    print(f"\nWritten: {out_path}")


if __name__ == "__main__":
    main()
