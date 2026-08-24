"""exp-069 -- zero-cost desk check on the EXISTING 36-cell settling-delta
dataset (exp-066's `closure_summary`), per QUANTUM's own Iteration-45 Phase-2
proposal (never executed -- Red Team's own Iteration-45 Phase-5 final audit,
`phase5_redteam_audit.md` Attack 1c). Reads ONLY already-committed data --
zero new FDTD calls. Run this BEFORE any new FDTD spend, per PLAN.md's
Iteration-46 mandate.

Question: does delta(theta) = C_empty(STEPS=2800, theta) - C_empty(STEPS=1400,
theta), read off exp-066's own committed `closure_summary` (all 36 Block MAIN
cells, +-35..40 deg x 3 lambda), show sign/phase structure locked to T21's own
established fringe period P(theta) = lambda/(A*cos theta), A=752 cells (the
`degrees(cpl/(A*cos theta))` form verified against exp-065's own committed
`P(40deg)=1.989deg` design constant)?

This is NOT Block MINI's own scored quantity (P-VIS42-10's dC_empty(C80-C40)
padding-delta) -- it is a DIFFERENT delta (a STEPS-settling delta, fixed
padding) that PLAN.md's own Iteration-45 queue named as a cheap precursor
diagnostic. A positive finding here does not itself re-open or close
P-VIS42-10; it only informs whether building the properly-powered padding-
delta sweep this cycle is worth doing densely enough to resolve, and gives an
independent, zero-cost cross-check on whether *some* T21-locked periodic
structure survives into the settling-correction channel at 1 deg sampling
(right at Nyquist for this period -- expected to alias, not cleanly resolve).
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

A = 752                      # exp-042/065's own established half-aperture, cells
CPL = {450: 15, 600: 20, 750: 25}


def P_deg(theta_deg, lambda_nm):
    """T21's established fringe period, degrees. Verified against exp-065's
    own committed constant: P_deg(40, 600) == 1.989 (design_geometry_output.txt)."""
    cpl = CPL[lambda_nm]
    return math.degrees(cpl / (A * math.cos(math.radians(theta_deg))))


def load_closure_summary():
    path = os.path.join(ROOT, "experiments",
                         "066-t27-block-main-settling-reverification",
                         "results.json")
    with open(path) as f:
        d = json.load(f)
    return d["closure_summary"]["rows"]


def main():
    rows = load_closure_summary()
    assert len(rows) == 36, f"expected 36 Block MAIN cells, got {len(rows)}"

    by_lam = {}
    for r in rows:
        delta = r["C_2800"] - r["C_1400"]
        by_lam.setdefault(r["lambda_nm"], []).append((r["theta"], delta))

    out = {"A_cells": A, "source": "experiments/066-.../results.json::closure_summary",
           "n_cells": len(rows), "by_lambda": {}}

    for lam in (450, 600, 750):
        pts = sorted(by_lam[lam])
        p40 = P_deg(40.0, lam)
        # sign-alternation score: fraction of adjacent SAME-side-of-axis
        # pairs (theta, theta+1) with opposite sign, within each 6-point
        # contiguous window (35..40 and -35..-40 do NOT abut -- do not
        # score across the +-35 gap).
        pos = [th for th, _ in pts if th > 0]
        neg = [th for th, _ in pts if th < 0]

        def flips(window_thetas, d):
            xs = sorted(window_thetas)
            n_flip, n_pair = 0, 0
            for a, b in zip(xs, xs[1:]):
                if abs(b - a) - 1.0 < 1e-9:  # adjacent 1deg step only
                    n_pair += 1
                    if d[a] * d[b] < 0:
                        n_flip += 1
            return n_flip, n_pair

        d = dict(pts)
        nf_pos, np_pos = flips(pos, d)
        nf_neg, np_neg = flips(neg, d)
        n_flip = nf_pos + nf_neg
        n_pair = np_pos + np_neg

        out["by_lambda"][lam] = {
            "P_deg_at_40": round(p40, 4),
            "samples_per_period_at_1deg_step": round(1.0 / p40, 4),
            "points": [{"theta": th, "delta": d_} for th, d_ in pts],
            "adjacent_sign_flips": n_flip,
            "adjacent_pairs_scored": n_pair,
            "flip_fraction": round(n_flip / n_pair, 4) if n_pair else None,
        }

    out_path = os.path.join(HERE, "desk_check_settling_delta_output.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)

    for lam in (450, 600, 750):
        b = out["by_lambda"][lam]
        print(f"{lam}nm: P(40)={b['P_deg_at_40']}deg "
              f"({b['samples_per_period_at_1deg_step']} samples/period @1deg step)  "
              f"adjacent sign-flip fraction = {b['flip_fraction']} "
              f"({b['adjacent_sign_flips']}/{b['adjacent_pairs_scored']})")
    print(f"\nWritten: {out_path}")


if __name__ == "__main__":
    main()
