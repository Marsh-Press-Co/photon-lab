"""exp-058 -- QUANTUM OPTICS' phase-variance redesign: measurement harness.
============================================================================
Panel Iteration 35 (lead: QUANTUM OPTICS, LOCKED, breaking rotation).
Predictions committed in NOTES.md BEFORE this file's first run (house
discipline). Geometry/constants from design_geometry.py.

For each article (off_pass, off_bracket): 9 individual-angle legs
(native r=78, cpl=20, rel_phase=0) are captured, their observation-line
Ez/Hy phasors are PERSISTED TO DISK via lab.phase_lines (this cycle's own
new machinery), then reloaded and used to reconstruct: (a) the zero-phase
case, checked against exp-056's own established C_joint; (b) N_DRAWS
random-relative-phase realizations, purely post-hoc (zero marginal FDTD)
-- the first real characterization of T25's variance, not merely its
mean. One extra native FDTD call per article (a fixed, seeded nonzero-
phase joint run) empirically bounds the reconstruction's own settling-
limited noise floor on this near-null-tau geometry (Director's own Phase-3
catch -- see design_geometry.py's module docstring and NOTES.md).

18 (legs) + 2 (noise-floor validation) = 20 NEW native FDTD calls.
"""

import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, HERE)

import numpy as np

import design_geometry as dg
from lab import Sim, ambient as amb, sections as sc
from lab import phase_lines as pl

ARTIFACTS_DIR = os.path.join(HERE, "artifacts")
LEGS_DIR = os.path.join(ARTIFACTS_DIR, "legs")


def build_native(sim, article):
    cx, cy = dg.OBJ
    x = np.arange(sim.nx)[:, None]
    y = np.arange(sim.ny)[None, :]
    mask = (x - cx) ** 2 + (y - cy) ** 2 <= dg.R_OUT ** 2
    sim.sigma_e[mask] += dg.SIGMA_BY_ARTICLE[article]
    sim.objects.append({"type": "uniform_sponge_disk",
                        "params": {"cx": cx, "cy": cy, "r": dg.R_OUT,
                                   "sigma": dg.SIGMA_BY_ARTICLE[article],
                                   "tau_center": dg.TAU_BY_ARTICLE[article]}})


def run_leg(article, ang, rel_phase):
    sim = Sim(dg.NX, dg.NY, cells_per_lambda=dg.CPL, courant_frac=dg.COURANT_FRAC,
              absorb=dg.ABSORB)
    build_native(sim, article)
    sim.add_line_source(dg.SRC_X, angle_deg=float(ang), edge=dg.TAPER,
                        amplitude=1.0, rel_phase=float(rel_phase))
    sim.run(dg.STEPS)
    return sim, sc.full_capture(sim)


def run_joint(article, angle_rel_phases):
    sim = Sim(dg.NX, dg.NY, cells_per_lambda=dg.CPL, courant_frac=dg.COURANT_FRAC,
              absorb=dg.ABSORB)
    build_native(sim, article)
    for ang, rp in angle_rel_phases:
        sim.add_line_source(dg.SRC_X, angle_deg=float(ang), edge=dg.TAPER,
                            amplitude=1.0, rel_phase=float(rp))
    sim.run(dg.STEPS)
    return sim, sc.full_capture(sim)


def weber_c(ez_line, hy_line):
    b = pl.flux_from_lines(ez_line, hy_line)
    o, f = amb.window_means(b, dg.ABSORB, dg.OBJ[1], dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)
    return amb.weber(o, f), o, f


def main():
    t0 = time.time()
    n_calls = 0
    os.makedirs(LEGS_DIR, exist_ok=True)
    results = {"meta": {"experiment": "exp-058", "panel_iteration": 35,
                        "lead": "QUANTUM OPTICS", "t1_escape_route": "NONE (instrument work)",
                        "n_draws": dg.N_DRAWS, "draw_seed": dg.DRAW_SEED,
                        "noise_floor_seed": dg.NOISE_FLOOR_SEED}}

    per_article = {}
    for article in dg.ARTICLES:
        # ---------------------------------------------- 9 individual legs
        ez_lines, hy_lines, p_abs_legs = {}, {}, {}
        for ang in dg.FALLBACK_ANGLES:
            sim, cap = run_leg(article, ang, 0.0)
            n_calls += 1
            ph = sc.phasors(cap)
            ez_i, hy_i = pl.line_phasor(ph, dg.PLANE_X, dg.ABSORB, dg.NY - dg.ABSORB)

            # persist to disk -- this cycle's own new machinery, genuinely
            # round-tripped (save then immediately reload), not merely
            # held in memory.
            leg_path = os.path.join(LEGS_DIR, f"{article}_{ang:+05.1f}.npz")
            pl.save_leg(leg_path, ez_i, hy_i, angle_deg=ang, plane_x=dg.PLANE_X,
                        article=article, lam_nm=dg.LAM_NM, cpl=dg.CPL,
                        rel_phase=0.0)
            ez_lines[ang], hy_lines[ang], _ = pl.load_leg(leg_path)

            # THERMODYNAMICS' mandatory fix (Iteration 35 Phase 2): the
            # naive-incoherent absorbed-power anchor, zero marginal FDTD
            # cost -- same capture, same call already used at exp-056 for
            # p_abs_joint_measured.
            _, _, p_abs_legs[ang] = sc.radial_absorbed_power(
                cap, sim.sigma_e, dg.OBJ[0], dg.OBJ[1], dg.R_OUT)

            print(f"  [{n_calls}] {article} leg angle={ang:+.1f} deg captured+persisted", flush=True)

        p_abs_naive = float(sum(p_abs_legs.values()))

        # -------------------------------------------- zero-phase reconstruction
        zero = {ang: 0.0 for ang in dg.FALLBACK_ANGLES}
        ez0, hy0 = pl.reconstruct_profile(ez_lines, hy_lines, zero)
        c0, b_obj0, b_flank0 = weber_c(ez0, hy0)
        c_established = dg.C_JOINT_ESTABLISHED[article]
        zero_phase_rel_err = abs(c0 - c_established) / abs(c_established)

        # -------------------------------- noise-floor validation leg (Director's
        # own Phase-3 catch): ONE extra native FDTD call, a fixed nonzero
        # relative-phase draw, direct joint Sim vs post-hoc reconstruction
        # from the already-captured legs.
        nf_rng = np.random.default_rng([dg.NOISE_FLOOR_SEED, dg.ARTICLE_SEED_OFFSET[article]])
        nf_deltas = {ang: float(d) for ang, d in
                     zip(dg.FALLBACK_ANGLES, nf_rng.uniform(0.0, 2.0 * np.pi, len(dg.FALLBACK_ANGLES)))}
        ez_nf_recon, hy_nf_recon = pl.reconstruct_profile(ez_lines, hy_lines, nf_deltas)
        c_nf_recon, _, _ = weber_c(ez_nf_recon, hy_nf_recon)
        sim_nf, cap_nf = run_joint(article, [(ang, nf_deltas[ang]) for ang in dg.FALLBACK_ANGLES])
        n_calls += 1
        ez_nf_direct, hy_nf_direct = pl.line_phasor(sc.phasors(cap_nf), dg.PLANE_X,
                                                      dg.ABSORB, dg.NY - dg.ABSORB)
        c_nf_direct, _, _ = weber_c(ez_nf_direct, hy_nf_direct)
        noise_floor_abs_c_error = abs(c_nf_recon - c_nf_direct)
        print(f"  [{n_calls}] {article} noise-floor validation leg: "
              f"|C_recon-C_direct|={noise_floor_abs_c_error:.6e}", flush=True)

        # ----------------------------------------------------- N_DRAWS ensemble
        rng = np.random.default_rng([dg.DRAW_SEED, dg.ARTICLE_SEED_OFFSET[article]])
        c_draws = np.empty(dg.N_DRAWS)
        flank_ratio_draws = np.empty(dg.N_DRAWS)
        for k in range(dg.N_DRAWS):
            deltas_k = rng.uniform(0.0, 2.0 * np.pi, len(dg.FALLBACK_ANGLES))
            phase_dict = dict(zip(dg.FALLBACK_ANGLES, deltas_k))
            ez_k, hy_k = pl.reconstruct_profile(ez_lines, hy_lines, phase_dict)
            c_k, b_obj_k, b_flank_k = weber_c(ez_k, hy_k)
            c_draws[k] = c_k
            # EM's mandatory fix (Iteration 35 Phase 2): per-draw flank-
            # denominator diagnostic, SAME construction/threshold as
            # exp-056's own flank_denominator_flag, reused UNMODIFIED
            # (Red Team docket item 3: disclosed, not re-derived).
            flank_ratio_draws[k] = b_flank_k / dg.EMPTY_JOINT_FLANK_RAW_NATIVE_ESTABLISHED

        abs_c = np.abs(c_draws)
        frac_over_thr = float(np.mean(abs_c > dg.C_THR_PHOTOPIC))
        flagged = np.abs(flank_ratio_draws) < dg.FLANK_DENOMINATOR_THRESHOLD
        frac_flagged = float(np.mean(flagged))
        # PHOTONICS' mandatory fix: percentile rank of |C(delta=0)| within
        # the empirical |C(delta)| distribution.
        percentile_rank_c0 = float(np.mean(abs_c <= abs(c0)) * 100.0)

        draws_path = os.path.join(ARTIFACTS_DIR, f"draws_{article}.npz")
        np.savez_compressed(draws_path, c_draws=c_draws, flank_ratio_draws=flank_ratio_draws)

        per_article[article] = {
            "c_established_native_joint": c_established,
            "c_zero_phase_reconstructed": c0,
            "zero_phase_relative_error": zero_phase_rel_err,
            "p_abs_naive": p_abs_naive,
            "p_abs_joint_established": dg.P_ABS_JOINT_ESTABLISHED[article],
            "p_abs_naive_over_joint_ratio": p_abs_naive / dg.P_ABS_JOINT_ESTABLISHED[article],
            "noise_floor_abs_c_error": noise_floor_abs_c_error,
            "noise_floor_over_c_thr": noise_floor_abs_c_error / dg.C_THR_PHOTOPIC,
            "draws": {
                "n": dg.N_DRAWS,
                "mean": float(np.mean(c_draws)),
                "std": float(np.std(c_draws)),
                "median": float(np.median(c_draws)),
                "min": float(np.min(c_draws)),
                "max": float(np.max(c_draws)),
                "c_naive_established": dg.C_NAIVE_ESTABLISHED[article],
                "mean_minus_c_naive_abs": abs(float(np.mean(c_draws)) - dg.C_NAIVE_ESTABLISHED[article]),
                "fraction_over_c_thr": frac_over_thr,
                "fraction_flank_denominator_flagged": frac_flagged,
                "percentile_rank_of_delta0_within_abs_c": percentile_rank_c0,
                "draws_file": os.path.relpath(draws_path, HERE),
            },
        }
        print(f"  {article}: C(0)={c0:.6f} (established {c_established}), "
              f"mean(C)={np.mean(c_draws):.6f}, std(C)={np.std(c_draws):.6f}, "
              f"frac>C_thr={frac_over_thr:.3f}, frac_flagged={frac_flagged:.3f}, "
              f"pct_rank(delta0)={percentile_rank_c0:.1f}", flush=True)

    results["per_article"] = per_article
    results["meta"]["n_fdtd_calls"] = n_calls
    results["meta"]["elapsed_s"] = time.time() - t0

    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\ndone in {time.time() - t0:.0f} s, {n_calls} FDTD calls, results -> {out_path}")


if __name__ == "__main__":
    main()
