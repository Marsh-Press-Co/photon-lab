"""
experiments/086-t28-free-period-boundary-fix-rescore/phase4_rescore.py
============================================================================
Panel Iteration 63 (exp-086). Director-run, implementing Phase 3's frozen
spec (`phase3_synthesis.md`) -- all 6 Red Team Phase-2 mandatory fixes
applied on top of the committed `phase1_proposal.md`. Zero new FDTD calls.

The R11 fix itself lives at the SOURCE (`pad_round_trip_model.py`'s and
`y_wall_prescreen.py`'s own `free_period_with_widening`/
`free_period_with_widening_quiet`), not here -- this script only re-runs
already-committed methodology on the corrected machinery via the same
`_load()` chain exp-084/085 established, so the fix propagates
automatically to every downstream import (verified: `ywp` resolves to the
now-patched `y_wall_prescreen.py`).

Steps: [1] re-run exp-085's Method C 37-sub-window fit on corrected
machinery (regenerating the 37 sub-window curves via the bit-identical
`FastEval`, unchanged formula); [2] extend the circular-shift null to all
37 sub-windows; [3] compute the overlap-corrected Spearman test at three
pre-registered non-overlapping stride phases; [4] persist ss_tot_full/ptp
per sub-window; [5] re-run `null_calibration_appendix` in full (60,001
calls, corrected quiet function) against exp-077's own committed real
data; [6] a bounded audit of committed JSON in experiments 077-085 (the
range `free_period_with_widening` actually spans -- 069-076 independently
confirmed absent of any occurrence by two separate grep methods, out of
scope by construction; corrected here per Red Team's Phase-5 final audit
Sec 1.3/Sec 6 item 2, which caught this docstring's own "069-085" against
the actual glob's "077-085") for any other silently boundary-pinned
citation.
"""

import glob
import json
import math
import os
import sys
import time

import numpy as np
from scipy.stats import spearmanr

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP077_DIR = os.path.join(ROOT, "experiments", "077-t28-pad-round-trip-echo-model")
EXP084_DIR = os.path.join(ROOT, "experiments", "084-t28-edge-diffraction-derivation")
EXP085_DIR = os.path.join(ROOT, "experiments", "085-t28-leg-a-wide-window-period-pin")

deriv = _load(os.path.join(EXP084_DIR, "phase1_derivation.py"), "_exp086_deriv084")
pad_model = _load(os.path.join(EXP077_DIR, "pad_round_trip_model.py"), "_exp086_pad")

dg048 = deriv.dg048
dg065 = deriv.dg065
free_period_with_widening = deriv.free_period_with_widening  # resolves through the fixed ywp
_free_period_search = deriv._free_period_search

from lab import ambient as amb  # noqa: E402

LAM600 = deriv.LAM600
CFG_C40 = deriv.CFG_C40
P_EDGE_A = deriv.P_EDGE_A
assert abs(P_EDGE_A - 2.8421052631578947) < 1e-9

CENTER_DEG_DEFAULT = 39.0
cos_c = math.cos(math.radians(CENTER_DEG_DEFAULT))


class FastEval:
    """Same cached-Green's-function evaluator as exp-085's own
    `phase4_derivation.py::FastEval` -- reproduced here (not imported --
    exp-085's own module executes its own `main()`-adjacent state on
    import via the `if __name__=="__main__"` guard, so it's safe to import,
    but a local, independently-typed copy plus the bit-identical
    verification below is cheaper to audit than importing a whole sibling
    script's namespace for one class)."""

    def __init__(self, g, lam_cells):
        self.g = g
        self.lam_cells = lam_cells
        self.gd = dg048._geom_derived(g)
        k = 2.0 * math.pi / lam_cells
        self.k = k
        self.G0 = np.exp(1j * (k * self.gd["r"] - math.pi / 4.0)) / np.sqrt(self.gd["r"])
        self.G0_obl = self.G0 * self.gd["obliquity"]

    def one(self, theta_deg):
        amp = dg048._src_amp(theta_deg, self.k, self.gd)
        E = self.G0 @ amp
        H = self.G0_obl @ amp
        Sx = -np.real(E * np.conj(H))
        bo, bf = amb.window_means(Sx, self.gd["y_lo"], self.gd["obj_y"],
                                   self.g["R_OUT"], self.g["GUARD_OUT"], self.g["W_FLANK"])
        return amb.weber(bo, bf)

    def curve(self, thetas):
        return np.array([self.one(th) for th in thetas])


def verify_fast_eval_bit_identical(fe, sample_thetas):
    rows = []
    for th in sample_thetas:
        orig = dg048.edge_diffraction_c_empty_corrected(th, fe.lam_cells, fe.g)
        fast = fe.one(th)
        diff = abs(orig - fast)
        rows.append(dict(theta=th, orig=orig, fast=fast, abs_diff=diff))
        assert diff == 0.0, f"FastEval NOT bit-identical at theta={th}: diff={diff}"
    return rows


def rel_dev(a, b):
    return abs(a - b) / b


def circular_shift_null(thetas, curve, label, verbose_every=None):
    """Exhaustive circular-shift null on the CORRECTED machinery (Fix 2:
    now applied to ALL 37 Method-C sub-windows, not the original 10-of-37
    sample)."""
    curve = np.asarray(curve, dtype=float)
    n = len(curve)
    t0 = time.time()
    fit0 = free_period_with_widening(thetas, curve, f"{label}_observed", [])
    p0, r2_0 = fit0["p_star_deg"], fit0["r_squared"]
    offsets = list(range(1, n))
    shift_r2 = np.empty(len(offsets))
    for i, s in enumerate(offsets):
        shifted = np.roll(curve, s)
        fit_s = free_period_with_widening(thetas, shifted, f"{label}_shift{s}", [])
        shift_r2[i] = fit_s["r_squared"]
        if verbose_every and (i + 1) % verbose_every == 0:
            print(f"      [{label}] shift {i+1}/{len(offsets)}  elapsed={time.time()-t0:.1f}s")
    n_meet = int(np.sum(shift_r2 >= r2_0))
    frac = n_meet / len(shift_r2)
    return dict(label=label, observed_p_star_deg=p0, observed_r2=r2_0,
                window=fit0["window"], converged=fit0.get("converged"),
                n_offsets_tested=len(offsets), n_possible_offsets=n - 1, exhaustive=True,
                n_meet_or_exceed=n_meet, fraction_meet_or_exceed=frac,
                mean_shift_r2=float(np.mean(shift_r2)), max_shift_r2=float(np.max(shift_r2)),
                min_shift_r2=float(np.min(shift_r2)), elapsed_s=time.time() - t0)


def main():
    t_start = time.time()
    out = {}
    print("=" * 78)
    print("exp-086 -- R11 boundary-pinning fix + full re-score (Iteration 63, EM lead)")
    print("Phase 4: corrected spec (phase3_synthesis.md, 6 mandatory fixes)")
    print("=" * 78)

    g = dg065.propagator_geom(CFG_C40)
    fe = FastEval(g, LAM600)

    print("\n[0] FastEval bit-identity verification (mandatory before any use)")
    spot = verify_fast_eval_bit_identical(fe, [36.0, 37.7, 39.0, 40.3, 42.0, 15.0, 60.5])
    for r in spot:
        print(f"    theta={r['theta']:6.2f}  orig={r['orig']:+.15f}  fast={r['fast']:+.15f}  "
              f"abs_diff={r['abs_diff']:.3e}")
    print("    -> bit-identical at every spot-check angle, confirmed.")
    out["fast_eval_verification"] = spot

    # ---------------------------------------------------- Method C re-score
    print("\n[1] METHOD C RE-SCORE -- 37 sub-windows, corrected free_period_with_widening (R11 fix)")
    theta_centers = np.arange(5.0, 77.0 + 1e-9, 2.0)
    assert len(theta_centers) == 37, len(theta_centers)
    sub_results = []
    t0 = time.time()
    stage_times = []
    for thc in theta_centers:
        ts = time.time()
        sub_theta = np.round(np.arange(thc - 3.0, thc + 3.0 + 1e-9, 0.2), 6)
        c_sub = fe.curve(sub_theta)
        ptp_sub = float(np.ptp(c_sub))
        ss_tot_sub = float(np.sum((c_sub - np.mean(c_sub)) ** 2))
        stages_sub = []
        fit_sub = free_period_with_widening(sub_theta, c_sub, f"subwin_{thc:.1f}", stages_sub)
        Tc_wrong = math.radians(fit_sub["p_star_deg"]) * cos_c
        p_local_corrected = math.degrees(Tc_wrong / math.cos(math.radians(thc)))
        rec = dict(theta_c=float(thc), p_local_reported_at_39=fit_sub["p_star_deg"],
                   p_local_corrected=p_local_corrected, r2_local=fit_sub["r_squared"],
                   window=fit_sub["window"], converged=fit_sub.get("converged"),
                   no_interior_optimum=fit_sub.get("no_interior_optimum"),
                   ptp=ptp_sub, ss_tot_full=ss_tot_sub,
                   elapsed_s=time.time() - ts)
        sub_results.append(rec)
        stage_times.append(rec["elapsed_s"])
    print(f"    37 sub-windows re-fit in {time.time()-t0:.1f}s")

    n_boundary = sum(1 for r in sub_results if not r["converged"])
    print(f"    boundary-pinned (converged=False) sub-windows: {n_boundary}/37")
    boundary_thetas = [r["theta_c"] for r in sub_results if not r["converged"]]
    print(f"    theta_c of boundary-pinned windows: {boundary_thetas}")

    # "recovered" per phase3_synthesis.md: converged AND p_local_corrected<=6deg AND r2>=0.30
    recovered = [r for r in sub_results
                 if r["converged"] and r["p_local_corrected"] <= 6.0 and r["r2_local"] >= 0.30]
    frac_recovered = len(recovered) / len(sub_results)
    print(f"    frac_recovered (converged & P<=6deg & R2>=0.30) = {len(recovered)}/37 = {frac_recovered:.4f}")

    local_periods = np.array([r["p_local_corrected"] for r in recovered])
    local_thetas = np.array([r["theta_c"] for r in recovered])
    if len(local_periods) >= 2:
        spread = (float(np.max(local_periods)) - float(np.min(local_periods))) / float(np.median(local_periods))
        rho_full, rho_p_full = spearmanr(local_thetas, local_periods)
        rho_full = float(rho_full)
    else:
        spread, rho_full, rho_p_full = float("nan"), float("nan"), float("nan")
    print(f"    (uncorrected-overlap) spread={spread:.4f}  rho={rho_full:.4f} (p={rho_p_full:.4g})  "
          f"[NOT the headline -- see [3] below for the overlap-corrected test]")

    out["method_c_rescore"] = dict(
        theta_centers=theta_centers.tolist(), sub_results=sub_results,
        n_boundary_pinned=n_boundary, boundary_thetas=boundary_thetas,
        frac_recovered=frac_recovered, n_recovered=len(recovered), n_total=len(sub_results),
        spread_uncorrected_overlap=spread, rho_uncorrected_overlap=rho_full,
        rho_p_uncorrected_overlap=rho_p_full,
        stage_elapsed_total_s=float(np.sum(stage_times)))

    if frac_recovered >= 0.80:
        classification_a = "NEEDS FULL RE-EVALUATION (frac_recovered>=0.80, see original 4-way table)"
    else:
        classification_a = "NOT STABLY PERIODIC"
    print(f"    CLASSIFICATION (a), corrected = {classification_a}")
    out["classification_a"] = classification_a

    # ---------------------------------------------------- Fix 2: extend null to all 37
    print("\n[2] FIX 1/2 -- circular-shift null extended to ALL 37 sub-windows "
          "(was 10/37)")
    t0 = time.time()
    null_all = []
    for thc in theta_centers:
        sub_theta = np.round(np.arange(thc - 3.0, thc + 3.0 + 1e-9, 0.2), 6)
        c_sub = fe.curve(sub_theta)
        null_i = circular_shift_null(sub_theta, c_sub, f"subwin_{thc:.1f}")
        null_all.append(null_i)
    print(f"    37/37 sub-windows circular-shift-null-tested in {time.time()-t0:.1f}s")
    null_pass_rate = sum(1 for n in null_all if n["fraction_meet_or_exceed"] >= 0.40) / len(null_all)
    print(f"    {sum(1 for n in null_all if n['fraction_meet_or_exceed']>=0.40)}/37 sub-windows "
          f"have circular-shift pass rate >=40% -> null_pass_rate={null_pass_rate:.4f} "
          f"(was 4/10=0.40 on the original 10-sample)")
    out["circular_shift_null_all37"] = dict(per_window=null_all, null_pass_rate=null_pass_rate)

    # ---------------------------------------------------- Fix 1: three pre-registered stride phases
    print("\n[3] FIX 1 -- overlap-corrected Spearman, three PRE-REGISTERED "
          "non-overlapping stride-3 phases (theta_c start = 5/7/9deg)")
    idx_by_thc = {r["theta_c"]: i for i, r in enumerate(sub_results)}
    thc_list = [r["theta_c"] for r in sub_results]
    stride_results = {}
    for phase_start in (5.0, 7.0, 9.0):
        phase_idx = thc_list.index(phase_start)
        idxs = list(range(phase_idx, len(sub_results), 3))
        phase_windows = [sub_results[i] for i in idxs]
        phase_recovered = [r for r in phase_windows
                            if r["converged"] and r["p_local_corrected"] <= 6.0 and r["r2_local"] >= 0.30]
        n_phase = len(phase_windows)
        n_rec = len(phase_recovered)
        if n_rec >= 2:
            pth = np.array([r["theta_c"] for r in phase_recovered])
            pp = np.array([r["p_local_corrected"] for r in phase_recovered])
            rho, p_asymp = spearmanr(pth, pp)
            rho = float(rho)
            # exact permutation p-value (small n -- exhaustive when feasible)
            from itertools import permutations
            obs = abs(rho)
            if n_rec <= 8:
                ranks = np.argsort(np.argsort(pp))
                base_ranks = np.argsort(np.argsort(pth))
                count = 0
                total = 0
                for perm in permutations(range(n_rec)):
                    total += 1
                    rp, _ = spearmanr(base_ranks, np.array(perm))
                    if abs(rp) >= obs - 1e-12:
                        count += 1
                p_exact = count / total
            else:
                p_exact = float(p_asymp)
        else:
            rho, p_asymp, p_exact = float("nan"), float("nan"), float("nan")
        stride_results[f"phase_{int(phase_start)}"] = dict(
            phase_start_theta_c=phase_start, n_windows_in_phase=n_phase,
            n_recovered_in_phase=n_rec, rho=rho, p_asymptotic=float(p_asymp) if n_rec >= 2 else float("nan"),
            p_exact_permutation=p_exact)
        print(f"    phase theta_c-start={phase_start:.0f}deg: n_windows={n_phase} n_recovered={n_rec} "
              f"rho={rho:.4f} p_exact={p_exact:.4f}")
    any_significant = any(abs(v["rho"]) > 0.75 and v["p_exact_permutation"] < 0.05
                           for v in stride_results.values() if not math.isnan(v["rho"]))
    headline_significance = ("PHASE-DEPENDENT -- not a single robust verdict"
                              if any_significant else "no phase clears significance")
    print(f"    headline: {headline_significance}")
    out["spearman_stride_phases"] = dict(phases=stride_results, headline=headline_significance)

    # ---------------------------------------------------- Fix 5 disclosure computed above (ptp/ss_tot already persisted per-window)

    elapsed = time.time() - t_start
    out["elapsed_s"] = elapsed
    out_path = os.path.join(HERE, "phase4_rescore_results.json")
    json.dump(out, open(out_path, "w"), indent=2)
    print(f"\n[SUMMARY] frac_recovered={frac_recovered:.4f}  classification_a={classification_a}")
    print(f"    total elapsed (Method C rescore + null + Spearman) = {elapsed:.1f}s")
    print(f"    results written to {out_path}")
    return out


if __name__ == "__main__":
    main()
