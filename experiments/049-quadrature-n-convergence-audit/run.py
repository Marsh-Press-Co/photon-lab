"""exp-049 -- Panel Iteration 26: the `gaussian_angle_weights` n-convergence
audit. Lead seat: PHOTONICS (rotation), executing Red Team's Iteration-25
non-negotiable item (1). Director: this shift.

PHASE 4 IMPLEMENTATION NOTE. This file implements the corrected design from
`phase3_synthesis.md`, which adopted all 8 items of Red Team's mandatory-fix
docket (`phase2_redteam_audit.md`) with none overridden. Predictions are
frozen in `NOTES.md` (committed before this file was executed). The Phase-1
proposal's own text survives unedited in `phase1_proposal.md` as the
historical record, per this program's "flag, don't rewrite" convention.

Zero new FDTD calls. Imports `design_geometry` from exp-042 unmodified and
calls its three committed `beam_divergence_*` functions at different `n`
only.
"""
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from scipy.stats import spearmanr

_REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO_ROOT))
sys.path.insert(0, str(_REPO_ROOT / "experiments" / "042-t21-magnitude-bridge"))
import design_geometry as dg  # noqa: E402

C_THR = 0.005
ABS_TOL = 5e-4
REL_TOL = 1.0  # percent

N_SERIES = (41, 81, 161, 321, 641, 1281, 2561, 5121)
N_REGRESSION = 401

THETA0S = (36, 38, 40)
FWHMS = (2, 5, 10, 20)
LAMBDAS = (450, 600, 750)
CPL = {450: 15, 600: 20, 750: 25}

FUNCS = {
    "incoherent": dg.beam_divergence_incoherent,
    "incoherent_corrected": dg.beam_divergence_incoherent_corrected,
    "coherent": dg.beam_divergence_coherent,
}

CELLS = [(th, fw, lam) for lam in LAMBDAS for th in THETA0S for fw in FWHMS]
assert len(CELLS) == 36

# T21 fringe period, LOGBOOK's own model (Iteration 18), reused by analogy
# (idealization 3): P(theta) = lambda_cells / (A * cos(theta)) radians, A=752.
A_FRINGE = 752.0


def fringe_period_deg(theta0_deg, lam_cells):
    theta0_rad = math.radians(theta0_deg)
    p_rad = lam_cells / (A_FRINGE * math.cos(theta0_rad))
    return math.degrees(p_rad)


def predicted_difficulty_rank():
    """FWHM=20deg, 9 cells -- predicted hardest->easiest: 450>600>750 (lambda
    primary), 36>38>40 (theta0 secondary). Returns dict (th,lam)->rank,
    rank 1 = hardest."""
    order = []
    for lam in LAMBDAS:  # 450, 600, 750 -- primary, hardest first
        for th in THETA0S:  # 36, 38, 40 -- secondary, hardest first
            order.append((th, lam))
    return {cell: i + 1 for i, cell in enumerate(order)}


def delta_step(c_n, c_2n):
    """Corrected Delta_rel: exemption, not floor, per Red Team Attack 5."""
    dabs = abs(c_2n - c_n)
    if abs(c_2n) >= C_THR:
        drel = 100.0 * dabs / abs(c_2n)
        exempted = False
    else:
        drel = None
        exempted = True
    converged = (dabs <= ABS_TOL) and (exempted or drel <= REL_TOL)
    return dict(dabs=dabs, drel=drel, exempted=exempted, converged=bool(converged))


def find_nstar(values_by_n):
    """values_by_n: dict n -> C. Two-consecutive-doublings pass required."""
    steps = []
    for i in range(len(N_SERIES) - 1):
        n1, n2 = N_SERIES[i], N_SERIES[i + 1]
        step = delta_step(values_by_n[n1], values_by_n[n2])
        step["n_from"] = n1
        step["n_to"] = n2
        steps.append(step)
    for i in range(len(steps) - 1):
        if steps[i]["converged"] and steps[i + 1]["converged"]:
            return N_SERIES[i], steps
    return None, steps  # NOT CONVERGED WITHIN RANGE


def main():
    t0 = time.time()
    ledger = []
    per_cell_func = {}  # (th,fw,lam,func) -> {values, nstar, steps, n401}

    for func_name, func in FUNCS.items():
        for (th, fw, lam) in CELLS:
            values = {}
            for n in N_SERIES:
                c = func(th, fw, CPL[lam], n=n)
                values[n] = c
                ledger.append(dict(func=func_name, theta0=th, fwhm=fw, lam=lam, n=n, C=c))
            c401 = func(th, fw, CPL[lam], n=N_REGRESSION)
            ledger.append(dict(func=func_name, theta0=th, fwhm=fw, lam=lam, n=N_REGRESSION, C=c401))

            nstar, steps = find_nstar(values)
            per_cell_func[(th, fw, lam, func_name)] = dict(
                values=values, n401=c401, nstar=nstar, steps=steps,
                converged_value=values[nstar] if nstar is not None else values[N_SERIES[-1]],
                not_converged_within_range=(nstar is None),
            )

    elapsed = time.time() - t0
    assert len(ledger) == 972, f"completeness ledger has {len(ledger)} records, expected 972"

    # ---- P-NCONV26-0: regression gate (restated scope, Attack 7) ----
    worst_cell = None
    worst_move = -1.0
    n_above_1pct = 0
    n_above_0p16pct = 0
    for (th, fw, lam) in CELLS:
        d = per_cell_func[(th, fw, lam, "coherent")]
        c41, c401 = d["values"][41], d["n401"]
        move = 100.0 * abs(c401 - c41) / abs(c401) if c401 != 0 else float("inf")
        if move > worst_move:
            worst_move = move
            worst_cell = (th, fw, lam)
        if move > 1.0:
            n_above_1pct += 1
        if move > 0.16:
            n_above_0p16pct += 1

    p0_expected_worst = 4.472688822027389
    p0_expected_n1 = 2
    p0_expected_n016 = 3
    p0_pass = (
        abs(worst_move - p0_expected_worst) / p0_expected_worst <= 1e-6
        and n_above_1pct == p0_expected_n1
        and n_above_0p16pct == p0_expected_n016
    )
    p_ncov0 = dict(
        measured_worst_move_pct=worst_move, measured_worst_cell=worst_cell,
        expected_worst_move_pct=p0_expected_worst,
        measured_n_above_1pct=n_above_1pct, expected_n_above_1pct=p0_expected_n1,
        measured_n_above_0p16pct=n_above_0p16pct, expected_n_above_0p16pct=p0_expected_n016,
        outcome="CONFIRMED" if p0_pass else "REFUTED",
    )

    # ---- P-NCONV26-1a/1b/1c: n* at 41 across the grid ----
    fwhm20_cells = [(th, fw, lam) for (th, fw, lam) in CELLS if fw == 20]
    fwhm10_cells = [(th, fw, lam) for (th, fw, lam) in CELLS if fw == 10]
    fwhm_le10_cells = [(th, fw, lam) for (th, fw, lam) in CELLS if fw <= 10]
    fwhm2_cells = [(th, fw, lam) for (th, fw, lam) in CELLS if fw == 2]

    def n41_converged(cell, func_name):
        d = per_cell_func[cell + (func_name,)]
        return d["nstar"] == 41

    p1a_fail = sum(1 for c in fwhm20_cells if not n41_converged(c, "coherent"))
    p_ncov1a = dict(
        n_fail_of_9=p1a_fail,
        outcome="CONFIRMED" if p1a_fail >= 6 else ("REFUTED" if p1a_fail <= 2 else "PARTIAL"),
    )

    p1b = {}
    for fn in ("incoherent", "incoherent_corrected"):
        fail = sum(1 for c in fwhm20_cells if not n41_converged(c, fn))
        p1b[fn] = dict(
            n_fail_of_9=fail,
            outcome="CONFIRMED" if fail <= 4 else ("REFUTED" if fail > 6 else "PARTIAL"),
        )

    pooled_le10 = sum(
        1 for c in fwhm_le10_cells for fn in FUNCS if n41_converged(c, fn)
    )
    pooled_le10_total = len(fwhm_le10_cells) * len(FUNCS)
    pooled_fwhm2 = sum(1 for c in fwhm2_cells for fn in FUNCS if n41_converged(c, fn))
    pooled_fwhm2_total = len(fwhm2_cells) * len(FUNCS)
    p1c_frac = pooled_le10 / pooled_le10_total
    p1c_fwhm2_frac = pooled_fwhm2 / pooled_fwhm2_total
    p_ncov1c = dict(
        pooled_converged=pooled_le10, pooled_total=pooled_le10_total, pooled_frac=p1c_frac,
        fwhm2_converged=pooled_fwhm2, fwhm2_total=pooled_fwhm2_total, fwhm2_frac=p1c_fwhm2_frac,
        outcome="CONFIRMED" if (p1c_frac >= 0.70 and p1c_fwhm2_frac >= 0.90) else
                ("REFUTED" if (p1c_frac < 0.50 or p1c_fwhm2_frac < 0.70) else "PARTIAL"),
    )

    # ---- P-NCONV26-2: three independent per-function Spearman correlations ----
    rank_map = predicted_difficulty_rank()
    p_ncov2 = {}
    for fn in FUNCS:
        predicted = []
        measured = []
        for (th, fw, lam) in fwhm20_cells:
            d = per_cell_func[(th, fw, lam, fn)]
            step0 = d["steps"][0]  # 41->81
            dabs = step0["dabs"]
            drel = step0["drel"]
            magnitude = drel if drel is not None else (dabs / ABS_TOL) * REL_TOL  # exempted cells ranked by Delta_abs, scaled onto the same axis
            predicted.append(rank_map[(th, lam)])
            measured.append(magnitude)
        rho, pval = spearmanr(predicted, measured)
        p_ncov2[fn] = dict(
            spearman_rho=float(rho), pvalue=float(pval),
            outcome="CONFIRMED" if rho >= 0.70 else ("REFUTED" if (rho < 0.30 or rho < 0) else "PARTIAL"),
        )

    # ---- P-NCONV26-3: FWHM=10deg genuine intermediate movement, net<1%, not exempted ----
    p3_qualifying = []
    for c in fwhm10_cells:
        for fn in FUNCS:
            d = per_cell_func[c + (fn,)]
            net_move = 100.0 * abs(d["n401"] - d["values"][41]) / abs(d["n401"]) if abs(d["n401"]) >= C_THR else None
            hit = False
            for step in d["steps"]:
                if not step["exempted"] and step["drel"] is not None and step["drel"] > 1.0:
                    hit = True
                    break
            if hit and (net_move is not None) and net_move < 1.0:
                p3_qualifying.append(dict(cell=c, func=fn, net_move_pct=net_move))
    p_ncov3 = dict(
        n_qualifying=len(p3_qualifying), qualifying=p3_qualifying,
        outcome="CONFIRMED" if len(p3_qualifying) >= 1 else "REFUTED",
    )

    # ---- P-NCONV26-4: n* <=401 at >=85/108, no NOT-CONVERGED-WITHIN-RANGE ----
    all_combos = [(th, fw, lam, fn) for (th, fw, lam) in CELLS for fn in FUNCS]
    n_le401 = sum(1 for combo in all_combos if per_cell_func[combo]["nstar"] is not None and per_cell_func[combo]["nstar"] <= 401)
    n_not_converged = sum(1 for combo in all_combos if per_cell_func[combo]["nstar"] is None)
    p_ncov4 = dict(
        n_le401_of_108=n_le401, n_not_converged_within_range=n_not_converged,
        outcome="CONFIRMED" if (n_le401 >= 85 and n_not_converged == 0) else "REFUTED",
    )

    # ---- P-NCONV26-5: sharpest stakes cell, incoherent_corrected, 750/38/2 ----
    cell5 = (38, 2, 750)
    d5 = per_cell_func[cell5 + ("incoherent_corrected",)]
    c41_5 = d5["values"][41]
    conv5 = d5["converged_value"]
    move5 = 100.0 * abs(conv5 - c41_5) / abs(c41_5) if c41_5 != 0 else float("inf")
    flips5 = abs(conv5) > C_THR
    p_ncov5 = dict(
        c41=c41_5, converged_value=conv5, nstar=d5["nstar"], relative_move_pct=move5,
        flips_C_THR=bool(flips5),
        margin_ratio=0.005 / abs(c41_5), margin_headroom_pct=100.0 * (0.005 / abs(c41_5) - 1.0),
        outcome="CONFIRMED" if (not flips5 and move5 <= 1.0) else ("REFUTED" if (flips5 or move5 > 5.0) else "PARTIAL"),
    )

    # ---- P-NCONV26-6: 36/36 above C_THR, 20x-incoherent sub-clause ----
    n_above_thr = 0
    n_at_least_20x = 0
    committed_min_abs_c = float("inf")
    for (th, fw, lam) in CELLS:
        coh = per_cell_func[(th, fw, lam, "coherent")]["converged_value"]
        incoh_corr = per_cell_func[(th, fw, lam, "incoherent_corrected")]["converged_value"]
        committed_min_abs_c = min(committed_min_abs_c, abs(coh))
        if abs(coh) > C_THR:
            n_above_thr += 1
        if abs(incoh_corr) > 0 and abs(coh) >= 20 * abs(incoh_corr):
            n_at_least_20x += 1
    n_below_20x = 36 - n_at_least_20x
    p_ncov6 = dict(
        n_above_thr=n_above_thr, n_at_least_20x=n_at_least_20x, n_below_20x=n_below_20x,
        min_abs_c=committed_min_abs_c,
        outcome="CONFIRMED" if (n_above_thr == 36 and 1 <= n_below_20x <= 3) else "PARTIAL",
    )

    # ---- P-NCONV26-7: A3 central-lobe identity residual shift, informational ----
    # (A3's own bands live in exp-046's own record; here we report the shift in
    # the coherent function's converged vs n=41 value at the 27 FWHM<=10 cells
    # as a proxy for "does the central-lobe-shape identity move materially".)
    max_shift_pp = 0.0
    for c in fwhm_le10_cells:
        d = per_cell_func[c + ("coherent",)]
        c41c = d["values"][41]
        convc = d["converged_value"]
        shift_pp = 100.0 * abs(convc - c41c) / abs(convc) if convc != 0 else 0.0
        max_shift_pp = max(max_shift_pp, shift_pp)
    p_ncov7 = dict(
        max_shift_pp=max_shift_pp,
        outcome="CONFIRMED" if max_shift_pp <= 0.5 else ("REFUTED" if max_shift_pp > 2.0 else "PARTIAL"),
    )

    # ---- P-NCONV26-8: coherent worst-cell relative move within 2x of 4.473% ----
    worst_coherent_move = 0.0
    worst_coherent_cell = None
    for c in fwhm20_cells:
        d = per_cell_func[c + ("coherent",)]
        c41c = d["values"][41]
        convc = d["converged_value"]
        move = 100.0 * abs(convc - c41c) / abs(convc) if convc != 0 else 0.0
        if move > worst_coherent_move:
            worst_coherent_move = move
            worst_coherent_cell = c
    p_ncov8 = dict(
        worst_coherent_move_pct=worst_coherent_move, worst_coherent_cell=worst_coherent_cell,
        outcome="CONFIRMED" if 2.2 <= worst_coherent_move <= 8.9 else
                ("REFUTED" if (worst_coherent_move < 0.5 or worst_coherent_move > 15.0) else "PARTIAL"),
    )

    # ---- Descriptive-only, Attack 8: the P-NCONV26-4 hardest-cell aside ----
    hardest_cell_named = (36, 20, 450)
    d_hardest = per_cell_func[hardest_cell_named + ("coherent",)]
    p_ncov4_aside = dict(
        note="Descriptive only, not scored (Attack 8, Red Team) -- the Phase-1 heuristic predicted n*∈{641,1281} at this cell specifically; measured below.",
        measured_nstar=d_hardest["nstar"],
    )

    results = dict(
        meta=dict(
            experiment="exp-049", panel_iteration=26, lead_seat="PHOTONICS",
            elapsed_s=elapsed, n_ledger_records=len(ledger),
            n_series=list(N_SERIES), n_regression=N_REGRESSION, abs_tol=ABS_TOL,
            rel_tol_pct=REL_TOL, c_thr=C_THR,
        ),
        completeness_ledger_count=len(ledger),
        predictions=dict(
            P_NCONV26_0=p_ncov0,
            P_NCONV26_1a=p_ncov1a,
            P_NCONV26_1b=p1b,
            P_NCONV26_1c=p_ncov1c,
            P_NCONV26_2=p_ncov2,
            P_NCONV26_3=p_ncov3,
            P_NCONV26_4=p_ncov4,
            P_NCONV26_4_aside=p_ncov4_aside,
            P_NCONV26_5=p_ncov5,
            P_NCONV26_6=p_ncov6,
            P_NCONV26_7=p_ncov7,
            P_NCONV26_8=p_ncov8,
        ),
        per_cell_summary=[
            dict(
                theta0=th, fwhm=fw, lam=lam, func=fn,
                nstar=per_cell_func[(th, fw, lam, fn)]["nstar"],
                c41=per_cell_func[(th, fw, lam, fn)]["values"][41],
                c401=per_cell_func[(th, fw, lam, fn)]["n401"],
                converged_value=per_cell_func[(th, fw, lam, fn)]["converged_value"],
                not_converged_within_range=per_cell_func[(th, fw, lam, fn)]["not_converged_within_range"],
            )
            for (th, fw, lam) in CELLS for fn in FUNCS
        ],
    )

    out_path = Path(__file__).resolve().parent / "results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)

    print(f"elapsed_s={elapsed:.1f} ledger_records={len(ledger)}")
    for pid, val in results["predictions"].items():
        if isinstance(val, dict) and "outcome" in val:
            print(f"{pid}: {val['outcome']}")
        elif isinstance(val, dict):
            for k, v in val.items():
                if isinstance(v, dict) and "outcome" in v:
                    print(f"{pid}[{k}]: {v['outcome']}")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
