"""exp-058 -- Phase 5 same-shift fix script (Red Team docket items 1, 3, 8).
============================================================================
Reloads the already-persisted 18 legs from disk (zero new FDTD calls) and
recomputes everything through the FIXED lab.phase_lines.flux_from_lines
(Panel Iteration 35 Phase 5, PHOTONICS/ELECTROMAGNETISM/Red Team's own
sign-bug fix). Verifies the fix is provably inert on every C(delta)
number already in results.json (Weber C's own scale invariance under a
uniform sign flip), and -- newly -- persists b_obj_draws/b_flank_draws
(discarded by the original run.py, QUANTUM's own Phase-5 mandatory fix)
so this program's own Iteration-6 zero-mean-cross-term theorem can
finally be tested directly against the real N=9 instrument's raw flux,
not just its ratio.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, HERE)

import numpy as np

import design_geometry as dg
from lab import ambient as amb
from lab import phase_lines as pl

ARTIFACTS_DIR = os.path.join(HERE, "artifacts")
LEGS_DIR = os.path.join(ARTIFACTS_DIR, "legs")


def weber_c(ez_line, hy_line):
    b = pl.flux_from_lines(ez_line, hy_line)
    o, f = amb.window_means(b, dg.ABSORB, dg.OBJ[1], dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)
    return amb.weber(o, f), o, f


def main():
    with open(os.path.join(HERE, "results.json")) as fh:
        old_results = json.load(fh)

    report = {}
    for article in dg.ARTICLES:
        ez_lines, hy_lines = {}, {}
        for ang in dg.FALLBACK_ANGLES:
            leg_path = os.path.join(LEGS_DIR, f"{article}_{ang:+05.1f}.npz")
            ez_lines[ang], hy_lines[ang], _ = pl.load_leg(leg_path)

        # zero-phase reconstruction -- must be bit-identical to the
        # original (sign-invariant under Weber C)
        zero = {ang: 0.0 for ang in dg.FALLBACK_ANGLES}
        ez0, hy0 = pl.reconstruct_profile(ez_lines, hy_lines, zero)
        c0_fixed, b_obj0_fixed, b_flank0_fixed = weber_c(ez0, hy0)
        c0_old = old_results["per_article"][article]["c_zero_phase_reconstructed"]

        # N_DRAWS ensemble, WITH b_obj/b_flank retained this time
        rng = np.random.default_rng([dg.DRAW_SEED, dg.ARTICLE_SEED_OFFSET[article]])
        c_draws = np.empty(dg.N_DRAWS)
        b_obj_draws = np.empty(dg.N_DRAWS)
        b_flank_draws = np.empty(dg.N_DRAWS)
        for k in range(dg.N_DRAWS):
            deltas_k = rng.uniform(0.0, 2.0 * np.pi, len(dg.FALLBACK_ANGLES))
            phase_dict = dict(zip(dg.FALLBACK_ANGLES, deltas_k))
            ez_k, hy_k = pl.reconstruct_profile(ez_lines, hy_lines, phase_dict)
            c_k, b_obj_k, b_flank_k = weber_c(ez_k, hy_k)
            c_draws[k] = c_k
            b_obj_draws[k] = b_obj_k
            b_flank_draws[k] = b_flank_k

        c_mean_old = old_results["per_article"][article]["draws"]["mean"]
        c_std_old = old_results["per_article"][article]["draws"]["std"]
        max_c_drift = float(np.max(np.abs(
            c_draws - _redraw_old(article))))  # sanity: same RNG stream, must match c_draws exactly

        # THE theorem's target: E[B_joint(y;delta)] over independent
        # Uniform(0,2pi) relative phases equals Sum_i B_i(y) EXACTLY (not
        # approximately) -- derived directly: E_total*conj(H_total) =
        # Sum_i Sum_j e^{i(delta_i-delta_j)} E_i*conj(H_j), and
        # E[e^{i(delta_i-delta_j)}] is the Kronecker delta under
        # independent uniform phases, killing every cross (i!=j) term and
        # leaving exactly Sum_i E_i*conj(H_i) -- QUANTUM's own Iteration-6
        # cross-term-vanishes theorem, generalized N=2->N=9 (re-derived,
        # not merely cited, at Panel Iteration 35 Phase 5 by the QUANTUM
        # OPTICS review seat). This is the UNNORMALIZED per-leg flux sum,
        # a cleaner/more fundamental target than lab.ambient's own
        # per-component-empty-flank-normalized C_naive citation (which
        # adds a separate normalization step for its own ambient-light
        # modeling purpose, orthogonal to the pure superposition claim
        # tested here). window_means is itself linear, so it commutes
        # with the expectation: E[b_obj_joint]=window_mean(Sum_i B_i).
        b_per_leg = [pl.flux_from_lines(ez_lines[ang], hy_lines[ang]) for ang in dg.FALLBACK_ANGLES]
        b_naive_profile = sum(b_per_leg)  # equal-weight incoherent sum (amplitude=1 each, matches build_native)
        b_obj_naive, b_flank_naive = amb.window_means(
            b_naive_profile, dg.ABSORB, dg.OBJ[1], dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)

        mean_b_obj = float(np.mean(b_obj_draws))
        mean_b_flank = float(np.mean(b_flank_draws))

        report[article] = {
            "zero_phase_c_fixed": c0_fixed,
            "zero_phase_c_original": c0_old,
            "zero_phase_c_identical": bool(abs(c0_fixed - c0_old) < 1e-12),
            "draws_c_mean_fixed": float(np.mean(c_draws)),
            "draws_c_mean_original": c_mean_old,
            "draws_c_std_fixed": float(np.std(c_draws)),
            "draws_c_std_original": c_std_old,
            "draws_c_max_abs_diff_vs_original": max_c_drift,
            "b_obj_naive_incoherent": b_obj_naive,
            "b_flank_naive_incoherent": b_flank_naive,
            "mean_b_obj_over_draws": mean_b_obj,
            "mean_b_flank_over_draws": mean_b_flank,
            "b_obj_theorem_rel_err": abs(mean_b_obj - b_obj_naive) / abs(b_obj_naive),
            "b_flank_theorem_rel_err": abs(mean_b_flank - b_flank_naive) / abs(b_flank_naive),
        }

        # update the draws npz with the newly-retained raw flux arrays
        draws_path = os.path.join(ARTIFACTS_DIR, f"draws_{article}.npz")
        np.savez_compressed(draws_path, c_draws=c_draws,
                            flank_ratio_draws=(b_flank_draws / dg.EMPTY_JOINT_FLANK_RAW_NATIVE_ESTABLISHED),
                            b_obj_draws=b_obj_draws, b_flank_draws=b_flank_draws)

        print(f"{article}: C(0) fixed={c0_fixed:.9f} vs original={c0_old:.9f} "
              f"identical={report[article]['zero_phase_c_identical']}")
        print(f"  draws mean/std fixed=({report[article]['draws_c_mean_fixed']:.6f}, "
              f"{report[article]['draws_c_std_fixed']:.6f}) vs "
              f"original=({c_mean_old:.6f}, {c_std_old:.6f}), max|diff|={max_c_drift:.2e}")
        print(f"  Iteration-6 theorem test: mean(b_obj)={mean_b_obj:.6f} vs naive={b_obj_naive:.6f} "
              f"(rel err {report[article]['b_obj_theorem_rel_err']:.4%}); "
              f"mean(b_flank)={mean_b_flank:.6f} vs naive={b_flank_naive:.6f} "
              f"(rel err {report[article]['b_flank_theorem_rel_err']:.4%})", flush=True)

    with open(os.path.join(HERE, "sign_fix_verification.json"), "w") as fh:
        json.dump(report, fh, indent=2)
    print("\nwritten -> sign_fix_verification.json")


_redraw_cache = {}


def _redraw_old(article):
    """Reload the ORIGINAL (pre-fix) c_draws array straight from the
    existing draws_*.npz, before this script overwrites it, so the
    same-RNG-stream sanity check has something to compare against."""
    if article not in _redraw_cache:
        path = os.path.join(ARTIFACTS_DIR, f"draws_{article}.npz")
        with np.load(path) as z:
            _redraw_cache[article] = z["c_draws"].copy()
    return _redraw_cache[article]


if __name__ == "__main__":
    main()
