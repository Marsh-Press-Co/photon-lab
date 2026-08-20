"""exp-051 -- Panel Iteration 28: the alias-lattice difficulty predictor,
tested OUT-OF-SAMPLE. Lead seat: ELECTROMAGNETISM (rotation).

PHASE 4 IMPLEMENTATION NOTE. Executes the design frozen in `NOTES.md`
(Phase-3-corrected -- the crux quantity is QUANTUM OPTICS' alias-lattice
term, not the Phase-1 `phase_offset`, which four blind seats refuted at the
desk). Predictions P-ALIAS-0..7 were committed to git in `NOTES.md` BEFORE
this file was written or executed. Zero new FDTD calls.

INDEPENDENCE (NOTES.md idealization 10). Written from the frozen NOTES.md
spec alone. No Phase-2 seat's scratch code was opened or copied; agreement
with QUANTUM's and Red Team's independent pre-checks on the CALIBRATION 18 is
reported as a three-way cross-validation, which is only meaningful because
the three implementations are independent.

SCORING DISCIPLINE (Phase-3 Director ruling, NOTES.md Scope):
  * the CALIBRATION 18 (GEOM78 x FWHM=20 x {incoherent, incoherent_corrected})
    are REPORTED AND SCORED AGAINST NOTHING -- two seats computed E_pred there
    during Phase 2 and committed the answers before the freeze.
  * every scored prediction lives on the 198 OUT-OF-SAMPLE combinations,
    except where a prediction names a sub-block (P-ALIAS-3: the 81 GEOM78
    FWHM<=10; P-ALIAS-4: the 108 A=752; P-ALIAS-5: the 9 A=752 FWHM=20 cells).
  * P-ALIAS-0 is checked FIRST and gates everything.

Red Team docket 9 is adopted in code here, not just in prose: process-start
timing is captured at MODULE IMPORT (below), and an `atexit` hook flushes a
timing record on every exit path including an uncaught exception -- Red Team
verified exp-050's `t0 = time.time()` still sat inside `main()`, so
THERMODYNAMICS' Iteration-27 recommendation had never actually been adopted.
"""

# ---- Red Team docket 9: process-start timing, captured at IMPORT ----------
import atexit
import json
import sys
import time
import traceback
from pathlib import Path

_PROC_T0 = time.time()
_PROC_T0_MONO = time.perf_counter()

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parents[1]
_TIMING_PATH = _HERE / "timing.json"

_RUN_STATE = dict(
    stage="import",
    completed=False,
    exception=None,
    proc_start_unix=_PROC_T0,
)


def _flush_timing():
    """Flushed on EVERY exit path -- clean return, sys.exit, or uncaught
    exception -- so a crashed run still records what it cost (Red Team
    docket 9). Never raises."""
    try:
        rec = dict(_RUN_STATE)
        rec["elapsed_s_from_import"] = time.perf_counter() - _PROC_T0_MONO
        rec["exit_unix"] = time.time()
        with open(_TIMING_PATH, "w") as f:
            json.dump(rec, f, indent=2)
    except Exception:                                    # pragma: no cover
        pass


atexit.register(_flush_timing)

import numpy as np  # noqa: E402

sys.path.insert(0, str(_HERE))
import design_geometry as dg  # noqa: E402

# ------------------------------------------------------------------ frozen
# Reused verbatim from exp-049/050 (NOTES.md Setup): "No tuning parameter is
# introduced or changed anywhere in this cycle."
C_THR = 0.005
ABS_TOL = 5e-4
REL_TOL = 1.0  # percent
N_SERIES = (41, 81, 161, 321, 641, 1281, 2561, 5121)

THETA0S = (36, 38, 40)
FWHMS = (2, 5, 10, 20)
LAMBDAS = (450, 600, 750)
CPL = dg.CPL

CELLS = [(th, fw, lam) for lam in LAMBDAS for th in THETA0S for fw in FWHMS]
assert len(CELLS) == 36

FUNCS = {
    "incoherent": dg.beam_divergence_incoherent,
    "incoherent_corrected": dg.beam_divergence_incoherent_corrected,
    "coherent": dg.beam_divergence_coherent,
}

GEOMS = (
    ("GEOM_EXP042_OLD", dg.GEOM_EXP042_OLD, 752,
     "experiments/049-quadrature-n-convergence-audit/results.json",
     "per_cell_summary"),
    ("GEOM78", dg.GEOM78, 724,
     "experiments/050-n-convergence-a724-geometry/results.json",
     "per_cell_summary_geom78"),
)

# NOTES.md idealization 3: the ABS_TOL-sensitivity ledger row, REPORTED, not
# re-tuned.
ABS_TOL_MULTIPLIERS = (0.05, 0.08, 0.10, 0.13, 0.20)

# NOTES.md idealization 7: the integration-step convergence spot-check.
STEP_SPOTCHECK_CELLS = [(38, fw, lam) for lam in (450, 750) for fw in (2, 20)]

# The pre-check figures quoted in NOTES.md / phase3_synthesis.md, transcribed
# here ONLY as the cross-validation target. They score nothing.
PRECHECK = dict(
    quantum=dict(auc=1.000, pearson_r=1.00000, max_rel_err_pct=1.4),
    redteam=dict(auc=1.0000, pearson_r=0.999998, max_rel_err_pct=1.445),
)


# ============================================================ statistics
def _rankdata(x):
    """Average ranks (ties shared) -- the Spearman/AUC primitive."""
    x = np.asarray(x, dtype=float)
    order = np.argsort(x, kind="mergesort")
    ranks = np.empty(x.size, dtype=float)
    sx = x[order]
    i = 0
    while i < x.size:
        j = i
        while j + 1 < x.size and sx[j + 1] == sx[i]:
            j += 1
        ranks[order[i:j + 1]] = 0.5 * (i + j) + 1.0
        i = j + 1
    return ranks


def pearson(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    xc = x - x.mean()
    yc = y - y.mean()
    d = np.sqrt((xc ** 2).sum() * (yc ** 2).sum())
    return float((xc * yc).sum() / d) if d > 0 else float("nan")


def spearman(x, y):
    return pearson(_rankdata(x), _rankdata(y))


def auc(scores, labels):
    """Mann-Whitney AUC; ties contribute 0.5 (rank-based, exact)."""
    scores = np.asarray(scores, dtype=float)
    labels = np.asarray(labels, dtype=bool)
    npos = int(labels.sum())
    nneg = int((~labels).sum())
    if npos == 0 or nneg == 0:
        return float("nan")
    r = _rankdata(scores)
    return float((r[labels].sum() - npos * (npos + 1) / 2.0) / (npos * nneg))


def confusion(pred, truth):
    pred = np.asarray(pred, dtype=bool)
    truth = np.asarray(truth, dtype=bool)
    tp = int((pred & truth).sum())
    fp = int((pred & ~truth).sum())
    fn = int((~pred & truth).sum())
    tn = int((~pred & ~truth).sum())
    n = tp + fp + fn + tn
    return dict(
        tp=tp, fp=fp, fn=fn, tn=tn, n_scored=n,
        accuracy=(tp + tn) / n if n else float("nan"),
        sensitivity=tp / (tp + fn) if (tp + fn) else float("nan"),
        specificity=tn / (tn + fp) if (tn + fp) else float("nan"),
    )


# ============================================================ n* machinery
def find_nstar_from_steps(converged_flags):
    """exp-049/050's committed rule, reused: n* is the first N_SERIES entry
    whose step AND the following step both converge (two consecutive
    doublings)."""
    for i in range(len(converged_flags) - 1):
        if converged_flags[i] and converged_flags[i + 1]:
            return N_SERIES[i]
    return None


def predicted_nstar(theta0, fwhm, lam_cells, g, convention, step=dg.STEP_DEG):
    """P-ALIAS-7: predict n* by evaluating |E_pred(h(n))| against the same
    unfitted ABS_TOL down the same N_SERIES with the same two-consecutive-
    doublings rule. `h(n) = 2*half_width_factor*FWHM/(n-1)` shrinks with n, so
    the same alias integral -- same dense c(theta) grid, same Gaussian weight,
    same support -- is simply re-transformed at each lattice frequency. No
    fitted parameter."""
    per_n = {}
    flags = []
    for i in range(len(N_SERIES) - 1):
        n = N_SERIES[i]
        e = dg.E_pred(theta0, fwhm, lam_cells, g, convention, n=n, step=step)
        per_n[n] = e["E_pred"]
        flags.append(abs(e["E_pred"]) <= ABS_TOL)
    return find_nstar_from_steps(flags), per_n, flags


# ============================================================ labels
def load_committed_labels():
    """exp-049's and exp-050's committed `n*` + `c41`, taken as ground truth
    (NOTES.md idealization 8). Already-committed public data from two prior
    experiments; this cycle does not re-derive them."""
    out = {}
    for label, g, a, relpath, key in GEOMS:
        with open(_REPO_ROOT / relpath) as f:
            doc = json.load(f)
        for row in doc[key]:
            out[(label, row["theta0"], row["fwhm"], row["lam"], row["func"])] = dict(
                nstar=row["nstar"], c41=row["c41"],
                converged_value=row["converged_value"],
                not_converged_within_range=row["not_converged_within_range"],
            )
    assert len(out) == 216, f"expected 216 committed label rows, got {len(out)}"
    return out


def split_of(geom_label, fwhm, func):
    """The Phase-3 Director ruling's calibration/out-of-sample split, fixed in
    NOTES.md Setup before any code ran."""
    if geom_label == "GEOM78" and fwhm == 20 and func in (
            "incoherent", "incoherent_corrected"):
        return "CALIBRATION"
    return "OUT_OF_SAMPLE"


# ============================================================ main
def main():
    t_wall0 = time.perf_counter()
    stage_times = {}

    def mark(name):
        stage_times[name] = time.perf_counter() - t_wall0
        _RUN_STATE["stage"] = name
        _RUN_STATE["stage_times"] = dict(stage_times)
        print(f"[{stage_times[name]:7.1f}s] {name}")

    committed = load_committed_labels()
    mark("labels_loaded")

    combos = [(gl, th, fw, lam, fn)
              for (gl, g, a, _p, _k) in GEOMS
              for (th, fw, lam) in CELLS
              for fn in FUNCS]
    assert len(combos) == 216, f"expected 216 combinations, got {len(combos)}"
    GBY = {gl: g for (gl, g, a, _p, _k) in GEOMS}
    ABY = {gl: a for (gl, g, a, _p, _k) in GEOMS}

    # -------------------------------------------------- C(41), C(81) sweep
    # The committed `beam_divergence_*` functions, invoked -- NOT a
    # reimplementation. P-ALIAS-0b scores c41 against exp-049/050 at 1e-9,
    # which is what certifies the same machinery is being driven.
    meas = {}
    for i, (gl, th, fw, lam, fn) in enumerate(combos):
        f = FUNCS[fn]
        g = GBY[gl]
        c41 = f(th, fw, CPL[lam], g, n=41)
        c81 = f(th, fw, CPL[lam], g, n=81)
        meas[(gl, th, fw, lam, fn)] = dict(C41=c41, C81=c81, dabs=abs(c81 - c41))
    mark("C41_C81_sweep")

    # ======================================================== P-ALIAS-0
    # Checked FIRST and gates everything: if it fails, no other number in this
    # cycle is trusted.
    # ---- (a) 18 spot points: geometry-parameterized single-angle functions
    #          vs exp-042's committed module-globals, at g=GEOM_EXP042_OLD
    anchor_rows = []
    worst_a = 0.0
    worst_a_where = None
    for lam in LAMBDAS:
        for th in THETA0S:
            for conv, ref in (("incoherent", dg.edge_diffraction_c_empty_042),
                              ("corrected", dg.edge_diffraction_c_empty_corrected_042)):
                mine = dg.edge_diffraction_c_empty_g(
                    float(th), CPL[lam], dg.GEOM_EXP042_OLD, conv)
                theirs = ref(float(th), CPL[lam])
                rel = abs(mine - theirs) / abs(theirs) if theirs != 0 else abs(mine - theirs)
                anchor_rows.append(dict(theta=th, lam=lam, convention=conv,
                                        mine=mine, exp042=theirs, rel=rel))
                if rel > worst_a:
                    worst_a, worst_a_where = rel, (th, lam, conv)
    assert len(anchor_rows) == 18, f"P-ALIAS-0a needs 18 spot points, got {len(anchor_rows)}"

    # ---- (b) beam_divergence_* at n=41 vs exp-049's and exp-050's c41,
    #          all 216 rows
    worst_b = 0.0
    worst_b_where = None
    for key in combos:
        mine = meas[key]["C41"]
        theirs = committed[key]["c41"]
        rel = abs(mine - theirs) / abs(theirs) if theirs != 0 else abs(mine - theirs)
        if rel > worst_b:
            worst_b, worst_b_where = rel, key

    # ---- master dense scans, one per (geometry, lambda) (Red Team docket 2).
    #      Every in-scope alias window (theta0 +- 2.5*FWHM, theta0 in
    #      {36,38,40}, FWHM in {2,5,10,20}) is a sub-interval of
    #      [36-50, 40+50] = [-14, 90] on the same 0.01-deg integer lattice, so
    #      ONE scan per (geometry, lambda) serves all 108 combinations there.
    I_LO = int(round((min(THETA0S) - dg.HALF_WIDTH_FACTOR * max(FWHMS)) / dg.STEP_DEG))
    I_HI = int(round((max(THETA0S) + dg.HALF_WIDTH_FACTOR * max(FWHMS)) / dg.STEP_DEG))
    for gl, g, a, _p, _k in GEOMS:
        for lam in LAMBDAS:
            dg.scan_c_empty(g, CPL[lam], I_LO, I_HI)
    mark("master_scans")

    # ---- implementation self-check (added by Phase 4, NOT a frozen clause,
    #      but GATING): the batched `_src_amp_batch`/matmul path used for the
    #      dense alias scan must reproduce the scalar `edge_diffraction_c_empty_g`
    #      path. Without this, a batching bug would corrupt every E_pred while
    #      leaving P-ALIAS-0a (a scalar-path check) green. Test angles are
    #      taken AS lattice values so the two paths see bit-identical theta.
    worst_batch = 0.0
    worst_batch_where = None
    for gl, g, a, _p, _k in GEOMS:
        for lam in LAMBDAS:
            for i in (I_LO, 3600, 3713, 4000, I_HI):
                th_ = i * dg.STEP_DEG
                sc = dg.scan_c_empty(g, CPL[lam], i, i)
                for conv in dg.CONVENTIONS:
                    batched = float(sc[conv][i - sc["i_lo"]])
                    scalar = dg.edge_diffraction_c_empty_g(th_, CPL[lam], g, conv)
                    rel = abs(batched - scalar) / abs(scalar) if scalar != 0 else abs(batched - scalar)
                    if rel > worst_batch:
                        worst_batch, worst_batch_where = rel, (gl, lam, th_, conv)

    a_pass = worst_a <= 1e-9
    b_pass = worst_b <= 1e-9
    batch_pass = worst_batch <= 1e-9
    p0 = dict(
        a_spot_points=18,
        a_worst_relative_error=worst_a,
        a_worst_at=worst_a_where,
        a_outcome="CONFIRMED" if a_pass else "REFUTED",
        b_rows_checked=len(combos),
        b_worst_relative_error=worst_b,
        b_worst_at=worst_b_where,
        b_outcome="CONFIRMED" if b_pass else "REFUTED",
        batched_vs_scalar_worst_relative_error=worst_batch,
        batched_vs_scalar_worst_at=worst_batch_where,
        batched_vs_scalar_note=(
            "Phase-4 implementation self-check, not a frozen P-ALIAS-0 clause; "
            "gates the run because the batched matmul path produces every "
            "E_pred while P-ALIAS-0a only exercises the scalar path."),
        outcome="CONFIRMED" if (a_pass and b_pass and batch_pass) else "REFUTED",
        gate="PASS" if (a_pass and b_pass and batch_pass) else "FAIL",
        anchor_rows=anchor_rows,
    )
    mark("P_ALIAS_0")
    print(f"    P-ALIAS-0: {p0['outcome']}  (a: {worst_a:.3e}, b: {worst_b:.3e}, "
          f"batch: {worst_batch:.3e}; bar 1e-9)")

    if p0["gate"] == "FAIL":
        # NOTES.md: "any mismatch beyond float noise => no number in this cycle
        # is trusted until resolved." Stop here; produce no science number.
        out = dict(
            meta=_meta(stage_times, aborted=True),
            gate="P-ALIAS-0 FAILED -- run aborted before any science number",
            predictions=dict(P_ALIAS_0=p0),
        )
        _write(out)
        _RUN_STATE["stage"] = "aborted_at_P_ALIAS_0"
        print("P-ALIAS-0 FAILED -- aborted. No other number in this cycle is trusted.")
        return 1

    # ==================================================== E_pred, all 216
    ledger = []
    rows = []
    for (gl, th, fw, lam, fn) in combos:
        g = GBY[gl]
        conv = dg.FUNC_TO_CONVENTION[fn]
        e = dg.E_pred(th, fw, CPL[lam], g, conv, n=41)
        nstar_pred, e_by_n, flags = predicted_nstar(th, fw, CPL[lam], g, conv)
        m = meas[(gl, th, fw, lam, fn)]
        c = committed[(gl, th, fw, lam, fn)]
        row = dict(
            geometry=gl, A=ABY[gl], theta0=th, fwhm=fw, lam=lam, func=fn,
            convention=conv,
            split=split_of(gl, fw, fn),
            E_pred_m1=e["E_pred_m1"], E_pred_m2=e["E_pred_m2"],
            E_pred=e["E_pred"], abs_E_pred=abs(e["E_pred"]),
            abs_ghat1=e["abs_ghat1"], abs_ghat2=e["abs_ghat2"],
            h_deg=e["h_deg"],
            samples_per_period=dg.samples_per_period(th, fw, CPL[lam], g, 41),
            local_period_deg=dg.local_period_deg(th, CPL[lam], g),
            C41=m["C41"], C81=m["C81"], dabs=m["dabs"],
            nstar_committed=c["nstar"],
            nstar_pred=nstar_pred,
            E_pred_by_n={str(k): v for k, v in e_by_n.items()},
            label_unstable=bool(c["nstar"] != 41),
            pred_unstable=bool(abs(e["E_pred"]) >= ABS_TOL),
        )
        rows.append(row)
        # ---- completeness ledger: one record per (combination, quantity) ----
        base = dict(geometry=gl, theta0=th, fwhm=fw, lam=lam, func=fn)
        for qname, qval in (("E_pred(m=1)", e["E_pred_m1"]),
                            ("E_pred(m=2)", e["E_pred_m2"]),
                            ("C(41)", m["C41"]),
                            ("C(81)", m["C81"]),
                            ("nstar_pred", nstar_pred)):
            ledger.append(dict(base, quantity=qname, value=qval))
    mark("E_pred_sweep")

    # ---- executable completeness assertion (Red Team docket 9) ----
    n_expected = 216 * 5
    assert len(ledger) == n_expected, \
        f"completeness ledger has {len(ledger)} records, expected {n_expected}"
    assert n_expected == 1080

    by_key = {(r["geometry"], r["theta0"], r["fwhm"], r["lam"], r["func"]): r
              for r in rows}
    oos = [r for r in rows if r["split"] == "OUT_OF_SAMPLE"]
    cal = [r for r in rows if r["split"] == "CALIBRATION"]
    assert len(oos) == 198 and len(cal) == 18, (len(oos), len(cal))
    assert sum(r["label_unstable"] for r in oos) == 22, "out-of-sample positives != 22"
    assert sum(r["label_unstable"] for r in cal) == 7, "calibration positives != 7"

    def arr(rs, k):
        return np.array([r[k] for r in rs], dtype=float)

    def lab(rs):
        return np.array([r["label_unstable"] for r in rs], dtype=bool)

    # ==================================================== P-ALIAS-1
    _FLOOR = 1e-300     # guards log10 only; Spearman is rank-invariant anyway
    n_zero = int((arr(oos, "abs_E_pred") == 0).sum() + (arr(oos, "dabs") == 0).sum())
    x1 = np.log10(np.maximum(arr(oos, "abs_E_pred"), _FLOOR))
    y1 = np.log10(np.maximum(arr(oos, "dabs"), _FLOOR))
    rho1 = spearman(x1, y1)
    p1 = dict(
        n=len(oos), n_exact_zero_values_floored=n_zero,
        spearman_rho=rho1, pearson_r_log10=pearson(x1, y1),
        outcome=("CONFIRMED" if rho1 >= 0.85 else
                 "PARTIAL" if rho1 >= 0.60 else "REFUTED"),
        hard_falsified=bool(rho1 < 0.40),
    )

    # ==================================================== P-ALIAS-2
    pred2 = np.array([r["pred_unstable"] for r in oos], dtype=bool)
    truth2 = lab(oos)
    cm2 = confusion(pred2, truth2)
    auc2 = auc(arr(oos, "abs_E_pred"), truth2)
    null_score = np.array([1.0 if r["func"] == "incoherent_corrected" else 0.0
                           for r in oos])
    auc_null = auc(null_score, truth2)
    cm_null = confusion(null_score > 0.5, truth2)
    beats_null = bool(auc2 > auc_null)
    conf2 = (cm2["accuracy"] >= 0.90 and cm2["sensitivity"] >= 0.75)
    part2 = ((0.75 <= cm2["accuracy"] < 0.90) or (0.50 <= cm2["sensitivity"] < 0.75)
             or (conf2 and not beats_null))
    p2 = dict(
        n=len(oos), positives=int(truth2.sum()), threshold_unfitted=ABS_TOL,
        **cm2,
        auc_E_pred=auc2,
        null_baseline_convention_identity=dict(auc=auc_null, **cm_null),
        beats_null_baseline=beats_null,
        outcome=("CONFIRMED" if (conf2 and beats_null) else
                 "PARTIAL" if part2 else "REFUTED"),
        hard_falsified=bool(cm2["accuracy"] < 0.70 or cm2["sensitivity"] < 0.35),
    )

    # ==================================================== P-ALIAS-3
    blk3 = [r for r in oos if r["geometry"] == "GEOM78" and r["fwhm"] <= 10]
    assert len(blk3) == 81, len(blk3)
    assert not any(r["label_unstable"] for r in blk3), "block 3 not all committed-stable"
    fp3 = sum(1 for r in blk3 if r["pred_unstable"])
    frac_stable3 = 1.0 - fp3 / len(blk3)
    p3 = dict(
        n=len(blk3), false_positives=fp3, fraction_predicted_stable=frac_stable3,
        max_samples_per_period=float(arr(blk3, "samples_per_period").max()),
        min_samples_per_period=float(arr(blk3, "samples_per_period").min()),
        max_abs_E_pred=float(arr(blk3, "abs_E_pred").max()),
        outcome=("CONFIRMED" if fp3 <= 4 else
                 "REFUTED" if fp3 > 12 else "PARTIAL"),
        hard_falsified=bool(fp3 > 12),
    )

    # ==================================================== P-ALIAS-4
    blk4 = [r for r in oos if r["geometry"] == "GEOM_EXP042_OLD"]
    assert len(blk4) == 108, len(blk4)
    cm4 = confusion([r["pred_unstable"] for r in blk4], lab(blk4))
    assert cm4["tp"] + cm4["fn"] == 16, "A=752 block positives != 16"
    p4 = dict(
        n=len(blk4), positives=16, **cm4,
        auc_E_pred=auc(arr(blk4, "abs_E_pred"), lab(blk4)),
        outcome=("CONFIRMED" if (cm4["accuracy"] >= 0.85 and cm4["sensitivity"] >= 0.60)
                 else "REFUTED" if cm4["accuracy"] < 0.70 else "PARTIAL"),
        hard_falsified=bool(cm4["accuracy"] < 0.70),
    )

    # ==================================================== P-ALIAS-5
    cells5 = [(th, lam) for lam in LAMBDAS for th in THETA0S]
    assert len(cells5) == 9
    rows5 = []
    for (th, lam) in cells5:
        r_inc = by_key[("GEOM_EXP042_OLD", th, 20, lam, "incoherent")]
        r_cor = by_key[("GEOM_EXP042_OLD", th, 20, lam, "incoherent_corrected")]
        spec = r_cor["abs_ghat1"] / r_inc["abs_ghat1"]
        measured = r_cor["dabs"] / r_inc["dabs"]
        rows5.append(dict(theta0=th, lam=lam, spectral_ratio=spec,
                          measured_dabs_ratio=measured,
                          abs_ghat1_corrected=r_cor["abs_ghat1"],
                          abs_ghat1_incoherent=r_inc["abs_ghat1"],
                          dabs_corrected=r_cor["dabs"],
                          dabs_incoherent=r_inc["dabs"]))
    sr = np.array([r["spectral_ratio"] for r in rows5])
    mr = np.array([r["measured_dabs_ratio"] for r in rows5])
    rho5 = spearman(sr, mr)
    med5 = float(np.median(sr))
    conf5 = (rho5 >= 0.70 and 1.4 <= med5 <= 2.6)
    hard5 = bool(rho5 < 0.30 or med5 < 1.1 or med5 > 3.5)
    p5 = dict(
        n=9, spearman_rho=rho5,
        median_spectral_ratio=med5,
        spectral_ratio_range=[float(sr.min()), float(sr.max())],
        median_measured_dabs_ratio=float(np.median(mr)),
        measured_dabs_ratio_range=[float(mr.min()), float(mr.max())],
        scored_median_is="spectral_ratio |ghat_corrected(1/h)|/|ghat_incoherent(1/h)|",
        outcome=("CONFIRMED" if conf5 else "REFUTED" if hard5 else "PARTIAL"),
        hard_falsified=hard5,
        per_cell=rows5,
    )

    # ==================================================== P-ALIAS-6
    x6 = np.log10(np.maximum(np.abs(arr(oos, "E_pred_m1")), _FLOOR))
    rho6_m1 = spearman(x6, y1)
    drop = rho1 - rho6_m1
    rel_change = np.abs(arr(oos, "E_pred_m2")) / np.abs(arr(oos, "E_pred_m1"))
    med_by_lam = {}
    for lamv in LAMBDAS:
        sel = np.array([r["lam"] == lamv for r in oos])
        med_by_lam[lamv] = float(np.median(rel_change[sel]))
    lam_ordered = med_by_lam[450] > med_by_lam[750]
    all_below_1pct = all(v < 0.01 for v in med_by_lam.values())
    conf6 = (drop >= 0.03) and lam_ordered
    p6 = dict(
        rho_m1_plus_m2=rho1, rho_m1_only=rho6_m1, degradation=drop,
        median_relative_change_by_lam={str(k): v for k, v in med_by_lam.items()},
        degradation_concentrated_at_450nm=bool(lam_ordered),
        outcome=("CONFIRMED" if conf6 else
                 "REFUTED" if all_below_1pct else
                 "PARTIAL" if (drop >= 0.03 or lam_ordered) else "REFUTED"),
        hard_falsified=bool(all_below_1pct),
    )

    # ==================================================== P-ALIAS-7
    exact7 = sum(1 for r in oos if r["nstar_pred"] == r["nstar_committed"])
    frac7 = exact7 / len(oos)
    mism7 = [dict(geometry=r["geometry"], theta0=r["theta0"], fwhm=r["fwhm"],
                  lam=r["lam"], func=r["func"],
                  nstar_committed=r["nstar_committed"], nstar_pred=r["nstar_pred"],
                  abs_E_pred=r["abs_E_pred"], dabs=r["dabs"])
             for r in oos if r["nstar_pred"] != r["nstar_committed"]]
    p7 = dict(
        n=len(oos), exact_matches=exact7, fraction_exact=frac7,
        outcome=("CONFIRMED" if frac7 >= 0.85 else
                 "REFUTED" if frac7 < 0.60 else "PARTIAL"),
        hard_falsified=bool(frac7 < 0.60),
        n_mismatches=len(mism7), mismatches=mism7,
    )
    mark("predictions_scored")

    # ============================================ CALIBRATION 18 (UNSCORED)
    # Reported in full, scored against nothing (Phase-3 Director ruling).
    # C(161) is computed HERE ONLY, for the 18 calibration rows, because
    # QUANTUM's and Red Team's quoted pre-check figures compare E_pred against
    # measured C(41)-C(161). It is informational, outside the 1080-record
    # ledger (which the frozen spec defines over C(41)/C(81)).
    cal_rows = []
    for r in sorted(cal, key=lambda r: (r["lam"], r["theta0"], r["func"])):
        g = GBY[r["geometry"]]
        c161 = FUNCS[r["func"]](r["theta0"], r["fwhm"], CPL[r["lam"]], g, n=161)
        d41_161 = r["C41"] - c161
        cal_rows.append(dict(
            theta0=r["theta0"], lam=r["lam"], func=r["func"],
            E_pred=r["E_pred"], E_pred_m1=r["E_pred_m1"], E_pred_m2=r["E_pred_m2"],
            C41=r["C41"], C81=r["C81"], C161=c161,
            measured_C41_minus_C161=d41_161,
            ratio_Epred_over_measured=r["E_pred"] / d41_161 if d41_161 else float("nan"),
            rel_err_pct=100.0 * abs(r["E_pred"] - d41_161) / abs(d41_161) if d41_161 else float("nan"),
            nstar_committed=r["nstar_committed"], nstar_pred=r["nstar_pred"],
            label_unstable=r["label_unstable"], pred_unstable=r["pred_unstable"],
        ))
    cal_meas = np.array([r["measured_C41_minus_C161"] for r in cal_rows])
    cal_pred = np.array([r["E_pred"] for r in cal_rows])
    cal_lab = np.array([r["label_unstable"] for r in cal_rows], dtype=bool)
    cal_cm = confusion([r["pred_unstable"] for r in cal_rows], cal_lab)
    cal_auc = auc(np.abs(cal_pred), cal_lab)
    cal_r = pearson(cal_meas, cal_pred)
    cal_maxrel = float(max(r["rel_err_pct"] for r in cal_rows))
    calibration = dict(
        status="REPORTED, SCORED AGAINST NOTHING (Phase-3 Director ruling)",
        n=18, positives=int(cal_lab.sum()), negatives=int((~cal_lab).sum()),
        auc_E_pred=cal_auc,
        pearson_r_measured_vs_predicted=cal_r,
        max_rel_err_pct=cal_maxrel,
        median_rel_err_pct=float(np.median([r["rel_err_pct"] for r in cal_rows])),
        confusion_at_unfitted_ABS_TOL=cal_cm,
        min_abs_E_pred_among_unstable=float(np.abs(cal_pred[cal_lab]).min()),
        max_abs_E_pred_among_stable=float(np.abs(cal_pred[~cal_lab]).max()),
        precheck_targets=PRECHECK,
        cross_validation=dict(
            vs_quantum=dict(
                auc_delta=cal_auc - PRECHECK["quantum"]["auc"],
                pearson_r_delta=cal_r - PRECHECK["quantum"]["pearson_r"],
                max_rel_err_pct_theirs=PRECHECK["quantum"]["max_rel_err_pct"],
                max_rel_err_pct_mine=cal_maxrel),
            vs_redteam=dict(
                auc_delta=cal_auc - PRECHECK["redteam"]["auc"],
                pearson_r_delta=cal_r - PRECHECK["redteam"]["pearson_r"],
                max_rel_err_pct_theirs=PRECHECK["redteam"]["max_rel_err_pct"],
                max_rel_err_pct_mine=cal_maxrel),
            note=("Three-way cross-validation of three independently written "
                  "implementations (QUANTUM Phase 2, Red Team Phase 2, this "
                  "Phase-4 module). Informational only -- it scores nothing."),
        ),
        rows=cal_rows,
    )
    mark("calibration_18")

    # ============================ ABS_TOL sensitivity ledger (idealization 3)
    # VISION SCIENCE's Phase-2 finding: at ABS_TOL = 0.1*C_THR every in-scope
    # tier label reduces to the single continuum cut `Delta_abs > 0.1*C_THR`,
    # because the |C(2n)| >= C_THR clause never fires anywhere in scope.
    # That reduction is VERIFIED here before the ledger uses it. REPORTED,
    # NOT RE-TUNED (idealization 2 still governs).
    cut_agree = sum(1 for r in rows
                    if (r["dabs"] > ABS_TOL) == r["label_unstable"])
    n_rel_clause_live = int((np.abs(arr(rows, "C81")) >= C_THR).sum())
    cut_check = dict(
        n=len(rows), agreements=cut_agree,
        n_rows_with_absC81_ge_C_THR=n_rel_clause_live,
        n_rows_absC81_in_C_THR_to_10x=int((
            (np.abs(arr(rows, "C81")) >= C_THR)
            & (np.abs(arr(rows, "C81")) < 10 * C_THR)).sum()),
        premise_finding=(
            "NOTES.md idealization 3 states the |C(2n)|>=C_THR clause 'never "
            "fires anywhere in scope' (VISION SCIENCE's Phase-2 finding, made "
            "on the 18 calibration rows). Across the full 216-combination "
            "scope the clause DOES fire, at the row count above -- almost all "
            "of them `coherent`, whose Weber contrast is order-unity rather "
            "than order-1e-3. The idealization's CONCLUSION nevertheless holds "
            "on all 216 (agreements == n below): where |C(2n)| is large, "
            "drel = 100*dabs/|C(2n)| <= 100*ABS_TOL/|C(2n)| is automatically "
            "under REL_TOL, so the rel clause is non-binding. Disclosed here "
            "rather than smoothed over: the conclusion is verified "
            "executably, the stated premise is not true in this wider scope."),
        disagreements=[dict(geometry=r["geometry"], theta0=r["theta0"],
                            fwhm=r["fwhm"], lam=r["lam"], func=r["func"],
                            dabs=r["dabs"], nstar_committed=r["nstar_committed"])
                       for r in rows
                       if (r["dabs"] > ABS_TOL) != r["label_unstable"]],
        max_abs_C81_in_scope=float(np.abs(arr(rows, "C81")).max()),
        c_thr=C_THR,
        rel_clause_can_fire=bool(np.abs(arr(rows, "C81")).max() >= C_THR),
        note=("Verifies VISION's single-continuum-cut reduction on all 216 "
              "before the sensitivity ledger below relies on it."),
    )
    sens_ledger = []
    for mult in ABS_TOL_MULTIPLIERS:
        tol = mult * C_THR
        relabel = np.array([r["dabs"] > tol for r in oos], dtype=bool)
        pred = np.array([r["abs_E_pred"] >= tol for r in oos], dtype=bool)
        cm = confusion(pred, relabel)
        cm_vs_frozen = confusion(pred, truth2)
        sens_ledger.append(dict(
            multiplier=mult, abs_tol=tol,
            is_frozen_value=bool(abs(tol - ABS_TOL) < 1e-15),
            label_positives=int(relabel.sum()), label_negatives=int((~relabel).sum()),
            pred_positives=int(pred.sum()), pred_negatives=int((~pred).sum()),
            vs_relabelled=cm,
            vs_frozen_labels=cm_vs_frozen,
        ))
    mark("abs_tol_sensitivity")

    # ==================== integration-step convergence (idealization 7)
    step_rows = []
    _sc_th = sorted({c[0] for c in STEP_SPOTCHECK_CELLS})
    _sc_fw = max(c[1] for c in STEP_SPOTCHECK_CELLS)
    _sc_lam = sorted({c[2] for c in STEP_SPOTCHECK_CELLS})
    fi_lo = int(round((min(_sc_th) - dg.HALF_WIDTH_FACTOR * _sc_fw) / dg.STEP_DEG_FINE))
    fi_hi = int(round((max(_sc_th) + dg.HALF_WIDTH_FACTOR * _sc_fw) / dg.STEP_DEG_FINE))
    for (gl, g, a, _p, _k) in GEOMS:
        for lam in _sc_lam:
            dg.scan_c_empty(g, CPL[lam], fi_lo, fi_hi, step=dg.STEP_DEG_FINE)
    for (gl, g, a, _p, _k) in GEOMS:
        for (th, fw, lam) in STEP_SPOTCHECK_CELLS:
            for conv in dg.CONVENTIONS:
                e_c = dg.E_pred(th, fw, CPL[lam], g, conv, n=41, step=dg.STEP_DEG)
                e_f = dg.E_pred(th, fw, CPL[lam], g, conv, n=41, step=dg.STEP_DEG_FINE)
                d = e_f["E_pred"] - e_c["E_pred"]
                step_rows.append(dict(
                    geometry=gl, theta0=th, fwhm=fw, lam=lam, convention=conv,
                    E_pred_step_0p01=e_c["E_pred"], E_pred_step_0p005=e_f["E_pred"],
                    abs_change=abs(d),
                    rel_change_pct=100.0 * abs(d) / abs(e_c["E_pred"]) if e_c["E_pred"] else float("nan"),
                    change_over_ABS_TOL=abs(d) / ABS_TOL,
                    crosses_ABS_TOL=bool((abs(e_c["E_pred"]) >= ABS_TOL) !=
                                         (abs(e_f["E_pred"]) >= ABS_TOL)),
                ))
    step_check = dict(
        n=len(step_rows), step_coarse=dg.STEP_DEG, step_fine=dg.STEP_DEG_FINE,
        max_rel_change_pct=float(max(r["rel_change_pct"] for r in step_rows)),
        max_abs_change=float(max(r["abs_change"] for r in step_rows)),
        max_change_over_ABS_TOL=float(max(r["change_over_ABS_TOL"] for r in step_rows)),
        n_classification_flips=sum(1 for r in step_rows if r["crosses_ABS_TOL"]),
        rows=step_rows,
    )
    mark("step_convergence_spotcheck")

    # ================ POST-HOC diagnostics -- UNSCORED, NOTHING RE-SCORED
    # Every number in this block was computed AFTER the frozen predictions
    # above were scored, and no band, threshold or disposition anywhere above
    # depends on it. It exists because "22 positives, 10 missed" is not a
    # finding until you say WHERE they were missed. No frozen prediction is
    # re-run, re-cut or re-interpreted here.
    def _blk(rs):
        if not rs:
            return None
        t = lab(rs)
        cm = confusion([r["pred_unstable"] for r in rs], t)
        x = np.log10(np.maximum(arr(rs, "abs_E_pred"), _FLOOR))
        y = np.log10(np.maximum(arr(rs, "dabs"), _FLOOR))
        return dict(n=len(rs), positives=int(t.sum()), spearman_rho=spearman(x, y),
                    auc_E_pred=auc(arr(rs, "abs_E_pred"), t), **cm)

    by_func = {fn: _blk([r for r in oos if r["func"] == fn]) for fn in FUNCS}
    non_coh = _blk([r for r in oos if r["func"] != "coherent"])
    coh = _blk([r for r in oos if r["func"] == "coherent"])
    m2_grid = {}
    for lamv in LAMBDAS:
        for fwv in FWHMS:
            sel = [r for r in oos if r["lam"] == lamv and r["fwhm"] == fwv]
            if sel:
                m2_grid[f"{lamv}nm_FWHM{fwv}"] = float(np.median(
                    np.abs(arr(sel, "E_pred_m2")) / np.abs(arr(sel, "E_pred_m1"))))
    m2_fwhm20 = {}
    for lamv in LAMBDAS:
        sel = [r for r in oos if r["lam"] == lamv and r["fwhm"] == 20]
        m2_fwhm20[str(lamv)] = float(np.median(
            np.abs(arr(sel, "E_pred_m2")) / np.abs(arr(sel, "E_pred_m1"))))
    observations = dict(
        status="POST-HOC, UNSCORED. No frozen prediction above depends on any "
               "number in this block.",
        where_the_out_of_sample_misses_are=dict(
            note=("All out-of-sample false negatives (and therefore all "
                  "P-ALIAS-7 n* mismatches) fall in one block: `coherent`. "
                  "That is the one function for which the alias model's own "
                  "premise does not hold -- QUANTUM's E1 identity "
                  "(C = sum w_i c_i / sum w_i, which makes the quadrature a "
                  "literal sampling of c(theta)) is a property of "
                  "`lab.ambient.incoherent_sum`'s per-component flank "
                  "normalization. `beam_divergence_coherent` sums FIELDS "
                  "before squaring, so its n-error is not the Poisson alias of "
                  "the single-angle contrast, and E_pred is being applied "
                  "there as the degenerate-x1 control phase3_synthesis.md S3 "
                  "item 3 designed it to be. Reported as an observation, not "
                  "as a re-scoring: the frozen predictions were scored on all "
                  "198, and they stay scored on all 198."),
            by_function=by_func,
            excluding_coherent=non_coh,
            coherent_only=coh,
        ),
        m2_term_size=dict(
            note=("P-ALIAS-6's lambda clause was drawn from QUANTUM's E5, "
                  "measured at FWHM=20 on GEOM78. Restricted to FWHM=20 the "
                  "450nm>750nm ordering does hold out-of-sample; pooled over "
                  "all four FWHM -- which is what the frozen band scores -- it "
                  "inverts, because at FWHM=2 the m=2 term is ~25% of the m=1 "
                  "term at every lambda. The frozen band is scored as frozen."),
            median_abs_Em2_over_Em1_by_lam_and_fwhm=m2_grid,
            median_abs_Em2_over_Em1_fwhm20_only=m2_fwhm20,
        ),
    )

    # ==================================================== assemble
    predictions = dict(
        P_ALIAS_0=p0, P_ALIAS_1=p1, P_ALIAS_2=p2, P_ALIAS_3=p3,
        P_ALIAS_4=p4, P_ALIAS_5=p5, P_ALIAS_6=p6, P_ALIAS_7=p7,
    )
    results = dict(
        meta=_meta(stage_times, aborted=False),
        gate="P-ALIAS-0 PASSED",
        completeness_ledger_count=len(ledger),
        completeness_ledger_expected=n_expected,
        scope=dict(
            combinations=216, calibration=18, out_of_sample=198,
            out_of_sample_positives=int(lab(oos).sum()),
            calibration_positives=int(lab(cal).sum()),
            blocks={
                "GEOM78 coherent FWHM=20": dict(
                    n=9, positives=sum(1 for r in oos if r["geometry"] == "GEOM78"
                                       and r["fwhm"] == 20 and r["label_unstable"])),
                "GEOM78 all funcs FWHM<=10": dict(n=81, positives=0),
                "A=752 all funcs all FWHM": dict(n=108, positives=16),
            },
        ),
        predictions=predictions,
        calibration_18_unscored=calibration,
        abs_tol_sensitivity=dict(
            note=("NOTES.md idealization 3: REPORTED, NOT RE-TUNED. The frozen "
                  "ABS_TOL = 0.1*C_THR governs every scored number above."),
            single_cut_reduction_check=cut_check,
            ledger=sens_ledger,
        ),
        integration_step_convergence=step_check,
        alias_integration_resolution=dict(
            note=("Disclosed limitation of the P-ALIAS-7 n*-prediction: the "
                  "alias integrand oscillates at 1/h, and h shrinks with n, so "
                  "the fixed 0.01-deg grid resolves the m=2 replica with "
                  "h/(2*step) points per period. Below ~4 points/period the "
                  "trapezoid under-resolves the integrand. Every committed n* "
                  "in scope is 41 or 81, so only the n=41/81/161 rows below "
                  "can affect a scored n* match; those are all well resolved "
                  "except FWHM=2 at n=161 (3.1 pts/period for m=2)."),
            points_per_period_m2_by_fwhm_and_n={
                str(fw): {str(n): dg.node_spacing_deg(fw, n) / (2.0 * dg.STEP_DEG)
                          for n in N_SERIES[:-1]}
                for fw in FWHMS},
        ),
        post_hoc_observations_unscored=observations,
        memoization=dict(dg.MEMO_STATS),
        per_combination=rows,
        completeness_ledger=ledger,
    )
    _write(results)

    print("\n---- dispositions (out-of-sample unless the row says otherwise) ----")
    for pid in ("P_ALIAS_0", "P_ALIAS_1", "P_ALIAS_2", "P_ALIAS_3",
                "P_ALIAS_4", "P_ALIAS_5", "P_ALIAS_6", "P_ALIAS_7"):
        print(f"  {pid}: {predictions[pid]['outcome']}")
    print(f"  CALIBRATION 18: UNSCORED -- AUC={cal_auc:.4f} r={cal_r:.6f} "
          f"max_rel_err={cal_maxrel:.3f}%")
    _RUN_STATE["completed"] = True
    _RUN_STATE["stage"] = "done"
    return 0


def _meta(stage_times, aborted):
    return dict(
        experiment="exp-051", panel_iteration=28,
        lead_seat="ELECTROMAGNETISM",
        title="The Alias-Lattice Difficulty Predictor, Tested Out-of-Sample",
        new_fdtd_calls=0,
        bench_before_run="lab/validation/run_all.py --only 12346789 -> 41/41",
        elapsed_s_from_import=time.perf_counter() - _PROC_T0_MONO,
        proc_start_unix=_PROC_T0,
        stage_times_s=dict(stage_times),
        aborted=aborted,
        n_series=list(N_SERIES), abs_tol=ABS_TOL, rel_tol_pct=REL_TOL,
        c_thr=C_THR,
        half_width_factor=dg.HALF_WIDTH_FACTOR,
        integration_step_deg=dg.STEP_DEG,
        timing_note=("Process-start timing captured at module IMPORT and "
                     "flushed by an atexit hook to timing.json on every exit "
                     "path including crash -- Red Team docket 9."),
    )


def _jsonable(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    return str(o)


def _write(results):
    out_path = _HERE / "results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=_jsonable)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    try:
        rc = main()
    except BaseException as exc:                      # noqa: BLE001
        _RUN_STATE["exception"] = "".join(
            traceback.format_exception_only(type(exc), exc)).strip()
        _RUN_STATE["traceback"] = traceback.format_exc()
        raise
    sys.exit(rc)
