"""exp-050 -- Panel Iteration 27: the n-convergence audit at exp-048's
GEOM78 (A=724/NY=1528) fallback geometry. Lead seat: MATERIALS &
METAMATERIALS (rotation). Director: this shift.

PHASE 4 IMPLEMENTATION NOTE. Implements the design frozen in `NOTES.md`
(Phase-3-synthesized, Red Team's mandatory-fix docket applied in full --
see `phase3_synthesis.md`). Predictions were committed to git in `NOTES.md`
BEFORE this file was written or executed (house discipline). Zero new FDTD
calls -- reuses `design_geometry.py`'s geometry-parameterized functions,
which in turn invoke exp-042's and exp-048's own already-committed
functions unmodified (via `importlib`, see that module's own docstring for
why -- both source files share a basename).
"""
import json
import sys
import time
from pathlib import Path

import numpy as np

_REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO_ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import design_geometry as dg  # noqa: E402

C_THR = 0.005
ABS_TOL = 5e-4
REL_TOL = 1.0  # percent

N_SERIES = (41, 81, 161, 321, 641, 1281, 2561, 5121)
N_REGRESSION = 401

THETA0S = (36, 38, 40)
FWHMS = (2, 5, 10, 20)
LAMBDAS = (450, 600, 750)
CPL = dg.CPL

FUNCS = {
    "incoherent": dg.beam_divergence_incoherent,
    "incoherent_corrected": dg.beam_divergence_incoherent_corrected,
    "coherent": dg.beam_divergence_coherent,
}

CELLS = [(th, fw, lam) for lam in LAMBDAS for th in THETA0S for fw in FWHMS]
assert len(CELLS) == 36

# P-NCONV27-2's own pre-registered exemption zone (Phase 3, Red Team
# Attacks 1+3+4): all three functions at these two (theta0,fwhm,lam)
# coordinates, named BEFORE this file ran, per NOTES.md.
EXEMPT_TRIPLES = {(38, 20, 750), (40, 20, 750)}

SHARPEST_STAKES_CELL = (38, 2, 750)  # theta0, fwhm, lam -- P-NCONV27-6/6b
SHARPEST_STAKES_FUNC = "incoherent_corrected"


def delta_step(c_n, c_2n):
    """Corrected Delta_rel: exemption, not floor (exp-049's own Phase-3
    fix, reused verbatim -- see NOTES.md Setup)."""
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
    return None, steps


def tier_index(nstar):
    """Position in N_SERIES; NOT-CONVERGED-WITHIN-RANGE is treated as
    strictly worse than every listed tier (P-NCONV27-2's own sign
    convention, NOTES.md idealization 10)."""
    if nstar is None:
        return len(N_SERIES)
    return N_SERIES.index(nstar)


def sweep(g, label, ledger):
    per_cell_func = {}
    for func_name, func in FUNCS.items():
        for (th, fw, lam) in CELLS:
            values = {}
            for n in N_SERIES:
                c = func(th, fw, CPL[lam], g, n=n)
                values[n] = c
                ledger.append(dict(geometry=label, func=func_name, theta0=th, fwhm=fw, lam=lam, n=n, C=c))
            c401 = func(th, fw, CPL[lam], g, n=N_REGRESSION)
            ledger.append(dict(geometry=label, func=func_name, theta0=th, fwhm=fw, lam=lam, n=N_REGRESSION, C=c401))
            nstar, steps = find_nstar(values)
            per_cell_func[(th, fw, lam, func_name)] = dict(
                values=values, n401=c401, nstar=nstar, steps=steps,
                converged_value=values[nstar] if nstar is not None else values[N_SERIES[-1]],
                not_converged_within_range=(nstar is None),
            )
    return per_cell_func


def main():
    t0 = time.time()
    ledger = []

    old = sweep(dg.GEOM_EXP042_OLD, "GEOM_EXP042_OLD", ledger)
    new = sweep(dg.GEOM78, "GEOM78", ledger)

    elapsed = time.time() - t0
    assert len(ledger) == 1944, f"completeness ledger has {len(ledger)} records, expected 1944"

    # ---- P-NCONV27-0: regression anchor vs exp-049's own committed results.json, per function ----
    exp049_path = _REPO_ROOT / "experiments" / "049-quadrature-n-convergence-audit" / "results.json"
    with open(exp049_path) as f:
        exp049 = json.load(f)
    exp049_lookup = {
        (row["theta0"], row["fwhm"], row["lam"], row["func"]): row
        for row in exp049["per_cell_summary"]
    }

    p_ncov0 = {}
    all_pass = True
    for fn in FUNCS:
        worst_rel = 0.0
        worst_cell = None
        n_mismatch_int = 0
        n_rows = 0
        for (th, fw, lam) in CELLS:
            row049 = exp049_lookup[(th, fw, lam, fn)]
            d = old[(th, fw, lam, fn)]
            n_rows += 1
            for field in ("n401", "converged_value"):
                a, b = d[field], row049[field]
                rel = abs(a - b) / abs(b) if b != 0 else abs(a - b)
                if rel > worst_rel:
                    worst_rel = rel
                    worst_cell = (th, fw, lam, field)
            c41_a, c41_b = d["values"][41], row049["c41"]
            rel41 = abs(c41_a - c41_b) / abs(c41_b) if c41_b != 0 else abs(c41_a - c41_b)
            if rel41 > worst_rel:
                worst_rel = rel41
                worst_cell = (th, fw, lam, "c41")
            if d["nstar"] != row049["nstar"]:
                n_mismatch_int += 1
        fn_pass = (worst_rel <= 1e-9) and (n_mismatch_int == 0)
        all_pass = all_pass and fn_pass
        p_ncov0[fn] = dict(
            worst_relative_error=worst_rel, worst_cell=worst_cell,
            n_nstar_mismatches=n_mismatch_int, n_rows_checked=n_rows,
            outcome="CONFIRMED" if fn_pass else "REFUTED",
        )
    p_ncov0["all_functions_pass"] = all_pass

    # ---- P-NCONV27-1: global max n* across all 108 GEOM78 combinations ----
    all_combos = [(th, fw, lam, fn) for (th, fw, lam) in CELLS for fn in FUNCS]
    max_nstar = 0
    n_not_converged = 0
    for combo in all_combos:
        d = new[combo]
        if d["not_converged_within_range"]:
            n_not_converged += 1
        elif d["nstar"] > max_nstar:
            max_nstar = d["nstar"]
    p_ncov1 = dict(
        max_nstar=max_nstar, n_not_converged_within_range=n_not_converged,
        outcome="CONFIRMED" if (max_nstar <= 81 and n_not_converged == 0) else "REFUTED",
    )

    # ---- P-NCONV27-2: tier-monotonicity, with the pre-registered exemption zone ----
    non_exempt_violations = []
    exempt_violations = []
    tier_table = []
    for (th, fw, lam) in CELLS:
        for fn in FUNCS:
            t_old = tier_index(old[(th, fw, lam, fn)]["nstar"])
            t_new = tier_index(new[(th, fw, lam, fn)]["nstar"])
            moved_larger = t_new > t_old
            is_exempt_eligible = (th, fw, lam) in EXEMPT_TRIPLES
            row = dict(theta0=th, fwhm=fw, lam=lam, func=fn,
                       tier_old=t_old, tier_new=t_new, moved_larger=moved_larger,
                       exempt_eligible=is_exempt_eligible)
            tier_table.append(row)
            if moved_larger:
                if is_exempt_eligible:
                    exempt_violations.append(row)
                else:
                    non_exempt_violations.append(row)
    p2_confirmed = (len(non_exempt_violations) == 0) and (len(exempt_violations) <= 1)
    p_ncov2 = dict(
        n_non_exempt_violations=len(non_exempt_violations),
        non_exempt_violations=non_exempt_violations,
        n_exempt_violations=len(exempt_violations),
        exempt_violations=exempt_violations,
        outcome="CONFIRMED" if p2_confirmed else "REFUTED",
    )

    # ---- P-NCONV27-3: coherent FWHM=20 tier failures ----
    fwhm20_cells = [(th, fw, lam) for (th, fw, lam) in CELLS if fw == 20]
    n_coherent_fail = sum(1 for c in fwhm20_cells if new[c + ("coherent",)]["nstar"] != 41)
    p_ncov3 = dict(
        n_fail_of_9=n_coherent_fail,
        outcome="CONFIRMED" if 6 <= n_coherent_fail <= 9 else
                ("REFUTED" if n_coherent_fail <= 2 else "PARTIAL"),
    )

    # ---- P-NCONV27-4: incoherent_corrected FWHM=20 tier failures ----
    n_ic_fail = sum(1 for c in fwhm20_cells if new[c + ("incoherent_corrected",)]["nstar"] != 41)
    p_ncov4 = dict(
        n_fail_of_9=n_ic_fail,
        outcome="CONFIRMED" if 3 <= n_ic_fail <= 7 else
                ("REFUTED" if n_ic_fail in (0, 9) else "PARTIAL"),
    )

    # ---- P-NCONV27-5: FWHM<=10 pooled convergence at n=41 ----
    fwhm_le10_cells = [(th, fw, lam) for (th, fw, lam) in CELLS if fw <= 10]
    pooled_total = len(fwhm_le10_cells) * len(FUNCS)
    pooled_converged = sum(1 for c in fwhm_le10_cells for fn in FUNCS if new[c + (fn,)]["nstar"] == 41)
    frac = pooled_converged / pooled_total
    p_ncov5 = dict(
        pooled_converged=pooled_converged, pooled_total=pooled_total, pooled_frac=frac,
        outcome="CONFIRMED" if frac >= 0.95 else ("REFUTED" if frac < 0.70 else "PARTIAL"),
    )

    # ---- P-NCONV27-6 / 6b: sharpest-stakes cell ----
    d6_new = new[SHARPEST_STAKES_CELL + (SHARPEST_STAKES_FUNC,)]
    d6_old = old[SHARPEST_STAKES_CELL + (SHARPEST_STAKES_FUNC,)]
    c41_new = d6_new["values"][41]
    conv_new = d6_new["converged_value"]
    move6 = 100.0 * abs(conv_new - c41_new) / abs(c41_new) if c41_new != 0 else float("inf")
    nstar6 = d6_new["nstar"]
    falsified6 = (nstar6 != 41) or (move6 > 5.0)
    p_ncov6 = dict(
        nstar=nstar6, c41=c41_new, converged_value=conv_new, relative_move_pct=move6,
        outcome="CONFIRMED" if (nstar6 == 41 and move6 <= 1.0) else
                ("REFUTED" if falsified6 else "PARTIAL"),
    )

    c41_old = d6_old["values"][41]
    redteam_precheck_old = -0.004006497410421138
    redteam_precheck_new = 1.465e-4  # Red Team's own rounded pre-check figure, phase2_redteam_audit.md
    old_match = abs(c41_old - redteam_precheck_old) / abs(redteam_precheck_old) if redteam_precheck_old != 0 else abs(c41_old)
    new_vs_precheck_rel = abs(conv_new - redteam_precheck_new) / abs(redteam_precheck_new) if redteam_precheck_new != 0 else abs(conv_new)
    headroom_old = (C_THR / abs(c41_old) - 1.0) * 100.0 if c41_old != 0 else float("inf")
    headroom_new = (C_THR / abs(conv_new) - 1.0) * 100.0 if conv_new != 0 else float("inf")
    p_ncov6b = dict(
        c_geom042old=c41_old, c_geom78_converged=conv_new,
        headroom_pct_geom042old=headroom_old, headroom_pct_geom78=headroom_new,
        ratio_geom042old_over_geom78=abs(c41_old) / abs(conv_new) if conv_new != 0 else float("inf"),
        sign_flip=bool((c41_old < 0) != (conv_new < 0)),
        redteam_precheck_old_relative_error=old_match,
        redteam_precheck_new_relative_error_to_2sf=new_vs_precheck_rel,
        outcome="CROSS-VALIDATED" if new_vs_precheck_rel <= 0.01 else "DISCREPANT-INVESTIGATE",
    )

    # ---- P-NCONV27-7: coherent worst-cell move at GEOM78, and whether it's a truncation cell ----
    worst_move7 = 0.0
    worst_cell7 = None
    for c in fwhm20_cells:
        d = new[c + ("coherent",)]
        c41c = d["values"][41]
        convc = d["converged_value"]
        move = 100.0 * abs(convc - c41c) / abs(convc) if convc != 0 else 0.0
        if move > worst_move7:
            worst_move7 = move
            worst_cell7 = c
    truncation_cells = {(36, 20, 750), (38, 20, 750), (40, 20, 750)}
    p_ncov7 = dict(
        worst_move_pct=worst_move7, worst_cell=worst_cell7,
        worst_cell_is_truncation_governed=(worst_cell7 in truncation_cells),
        outcome="CONFIRMED" if 3.0 <= worst_move7 <= 6.5 else
                ("REFUTED" if (worst_move7 < 1.5 or worst_move7 > 10.0) else "PARTIAL"),
    )

    results = dict(
        meta=dict(
            experiment="exp-050", panel_iteration=27, lead_seat="MATERIALS & METAMATERIALS",
            elapsed_s=elapsed, n_ledger_records=len(ledger),
            n_series=list(N_SERIES), n_regression=N_REGRESSION, abs_tol=ABS_TOL,
            rel_tol_pct=REL_TOL, c_thr=C_THR,
            exempt_triples=sorted(EXEMPT_TRIPLES),
        ),
        completeness_ledger_count=len(ledger),
        predictions=dict(
            P_NCONV27_0=p_ncov0,
            P_NCONV27_1=p_ncov1,
            P_NCONV27_2=p_ncov2,
            P_NCONV27_3=p_ncov3,
            P_NCONV27_4=p_ncov4,
            P_NCONV27_5=p_ncov5,
            P_NCONV27_6=p_ncov6,
            P_NCONV27_6b=p_ncov6b,
            P_NCONV27_7=p_ncov7,
        ),
        per_cell_summary_geom78=[
            dict(
                theta0=th, fwhm=fw, lam=lam, func=fn,
                nstar=new[(th, fw, lam, fn)]["nstar"],
                c41=new[(th, fw, lam, fn)]["values"][41],
                c401=new[(th, fw, lam, fn)]["n401"],
                converged_value=new[(th, fw, lam, fn)]["converged_value"],
                not_converged_within_range=new[(th, fw, lam, fn)]["not_converged_within_range"],
            )
            for (th, fw, lam) in CELLS for fn in FUNCS
        ],
        tier_table=tier_table,
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
