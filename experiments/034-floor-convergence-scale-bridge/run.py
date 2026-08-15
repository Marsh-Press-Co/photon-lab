"""exp-034 -- The Paired Floor-Convergence / r=156 Scale-Bridge Cycle:
measurement harness.
=============================================================================
Panel Iteration 11 (lead THERMODYNAMICS, rotation; synthesis: Director, post
Red Team's PROCEED-WITH-MANDATORY-FIXES verdict -- see design_geometry.py
module docstring and NOTES.md Phase 3 for the full accepted/overridden
record). Four independent blocks, run and analyzed separately (Red Team
mandatory fix 1 -- no shared cross-block article harness).

Run counts (each block's own scoped article list, printed/asserted below,
not just cited in the table):
  Block CPL40:     9 angles x 2 scenes (empty,off_pass) = 18, + 2 settling = 20
  Block R156:      9 angles x 3 scenes (empty,off_bracket,off_pass) = 27
  Block N17_156:   17 angles x 2 scenes (empty,off_pass) = 34
  Block N17_NATIVE: 17 angles x 2 scenes (empty,off_pass) = 34
  TOTAL: 115 new FDTD calls.

Predictions committed in NOTES.md BEFORE this file's first run (house
discipline, non-negotiable). No `lab/` change -- suite stays 46/46 fast-
stage green (re-verified before results are read).
"""

import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from functools import partial

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, HERE)

import design_geometry as dg
from lab import Sim, ambient as amb, sections as sc


# ===================================================== generic FDTD call
def _one_run(nx, ny, cpl, absorb, src_x, taper, obj, r_out, sigma, theta, steps):
    sim = Sim(nx, ny, cells_per_lambda=cpl, courant_frac=0.99, absorb=absorb)
    if sigma is not None:
        cx, cy = obj
        x = np.arange(sim.nx)[:, None]
        y = np.arange(sim.ny)[None, :]
        mask = (x - cx) ** 2 + (y - cy) ** 2 <= r_out ** 2
        sim.sigma_e[mask] += sigma
        sim.objects.append({"type": "uniform_sponge_disk",
                            "params": {"cx": cx, "cy": cy, "r": r_out, "sigma": sigma}})
    sim.add_line_source(src_x, angle_deg=theta, edge=taper, amplitude=1.0)
    sim.run(steps)
    return sc.full_capture(sim)


def _profile(cap, plane_x, y_lo, y_hi):
    ph = sc.phasors(cap)
    return amb.observer_profile(ph, plane_x, y_lo, y_hi).tolist()


def _contrast(scenes_by_theta, article, angles, y_lo, obj_y, w_obj, guard_out, w_flank):
    profs, e_profs = [], []
    for th in angles:
        grp = scenes_by_theta[th]
        profs.append(np.array(grp[article]))
        e_profs.append(np.array(grp["empty"]))
    weights = [1.0] * len(angles)
    return amb.contrast_from_runs(profs, e_profs, weights, y_lo, obj_y, w_obj, guard_out, w_flank)


def fit_free_line(taus, g_corrs):
    """Free two-parameter fit g_corr = A - B*tau (reused verbatim from
    exp-033 -- NEVER impose 4/(3pi), refuted by the free fit)."""
    taus = np.array(taus, dtype=float)
    g = np.array(g_corrs, dtype=float)
    coeffs = np.polyfit(taus, g, 1)
    B, A = -coeffs[0], coeffs[1]
    fit_vals = A - B * taus
    max_resid = float(np.max(np.abs(g - fit_vals)))
    return float(A), float(B), max_resid


# ===================================================== Block CPL40
def run_group_cpl40(args):
    theta, steps = args
    t0 = time.time()
    g = dg.CPL40
    cap_e = _one_run(g["NX"], g["NY"], g["CPL"], g["ABSORB"], g["SRC_X"], g["TAPER"],
                      g["OBJ"], g["R_OUT"], None, theta, steps)
    cap_p = _one_run(g["NX"], g["NY"], g["CPL"], g["ABSORB"], g["SRC_X"], g["TAPER"],
                      g["OBJ"], g["R_OUT"], g["SIGMA_OFF_PASS"], theta, steps)
    out = {"empty": _profile(cap_e, g["PLANE_X"], g["ABSORB"], g["NY"] - g["ABSORB"]),
           "off_pass": _profile(cap_p, g["PLANE_X"], g["ABSORB"], g["NY"] - g["ABSORB"])}
    return (theta, steps, out, time.time() - t0)


def block_cpl40():
    g = dg.CPL40
    n_expected = len(g["FALLBACK_ANGLES"]) * 2 + 2
    print(f"\n=== Block CPL40: {len(g['FALLBACK_ANGLES'])} angles x 2 scenes + 2 settling "
          f"= {n_expected} calls @ steps={g['STEPS_AMBIENT']} ===", flush=True)
    t0 = time.time()
    main_args = [(float(th), g["STEPS_AMBIENT"]) for th in g["FALLBACK_ANGLES"]]
    scenes = {}
    n_runs = 0
    with ProcessPoolExecutor(max_workers=4) as ex:
        for theta, steps, out, dt in ex.map(run_group_cpl40, main_args):
            scenes[theta] = out
            n_runs += 2
            print(f"  [cpl40 {len(scenes):1d}/{len(main_args)}] theta={theta:+05.1f} ({dt:5.1f}s)", flush=True)
    elapsed_main = time.time() - t0

    t1 = time.time()
    _, _, ctrl_out, ctrl_dt = run_group_cpl40((0.0, g["STEPS_SETTLING_CONTROL"]))
    n_runs += 2
    elapsed_settling = time.time() - t1
    print(f"  [cpl40 settling] theta=0.0 steps={g['STEPS_SETTLING_CONTROL']} ({ctrl_dt:5.1f}s)", flush=True)

    assert n_runs == n_expected, f"Block CPL40 run-count mismatch: {n_runs} != {n_expected}"

    r_empty = _contrast(scenes, "empty", g["FALLBACK_ANGLES"], g["ABSORB"], g["OBJ"][1], g["W_OBJ"], g["GUARD_OUT"], g["W_FLANK"])
    r_pass = _contrast(scenes, "off_pass", g["FALLBACK_ANGLES"], g["ABSORB"], g["OBJ"][1], g["W_OBJ"], g["GUARD_OUT"], g["W_FLANK"])
    fresh_floor = abs(r_empty["C_empty"])
    C_off_pass = r_pass["C"]

    r_e_ctrl = amb.contrast_from_runs([np.array(ctrl_out["empty"])], [np.array(ctrl_out["empty"])],
                                       [1.0], g["ABSORB"], g["OBJ"][1], g["W_OBJ"], g["GUARD_OUT"], g["W_FLANK"])
    r_p_ctrl = amb.contrast_from_runs([np.array(ctrl_out["off_pass"])], [np.array(ctrl_out["empty"])],
                                       [1.0], g["ABSORB"], g["OBJ"][1], g["W_OBJ"], g["GUARD_OUT"], g["W_FLANK"])
    r_p_main0 = amb.contrast_from_runs([np.array(scenes[0.0]["off_pass"])], [np.array(scenes[0.0]["empty"])],
                                        [1.0], g["ABSORB"], g["OBJ"][1], g["W_OBJ"], g["GUARD_OUT"], g["W_FLANK"])
    c_ctrl = r_p_ctrl["C"]
    c_main0 = r_p_main0["C"]
    settling_rel = abs(c_ctrl - c_main0) / abs(c_main0)

    def score(c):
        ac = abs(c)
        return "PASS" if ac < 0.005 else ("MARGINAL" if ac < 0.02 else "FAIL")

    return {
        "n_new_runs": n_runs, "elapsed_s": elapsed_main + elapsed_settling,
        "fresh_floor_cpl40": fresh_floor, "C_off_pass_cpl40": C_off_pass,
        "ladder": score(C_off_pass), "settling_relative_delta": settling_rel,
    }


# ===================================================== Block R156
def run_group_r156(args):
    theta, steps = args
    t0 = time.time()
    g = dg.R156
    cap_e = _one_run(g["NX"], g["NY"], g["CPL"], g["ABSORB"], g["SRC_X"], g["TAPER"],
                      g["OBJ"], g["R_OUT"], None, theta, steps)
    cap_br = _one_run(g["NX"], g["NY"], g["CPL"], g["ABSORB"], g["SRC_X"], g["TAPER"],
                       g["OBJ"], g["R_OUT"], g["SIGMA_OFF_BRACKET"], theta, steps)
    cap_ps = _one_run(g["NX"], g["NY"], g["CPL"], g["ABSORB"], g["SRC_X"], g["TAPER"],
                       g["OBJ"], g["R_OUT"], g["SIGMA_OFF_PASS"], theta, steps)
    out = {"empty": _profile(cap_e, g["PLANE_X"], g["ABSORB"], g["NY"] - g["ABSORB"]),
           "off_bracket": _profile(cap_br, g["PLANE_X"], g["ABSORB"], g["NY"] - g["ABSORB"]),
           "off_pass": _profile(cap_ps, g["PLANE_X"], g["ABSORB"], g["NY"] - g["ABSORB"])}
    return (theta, steps, out, time.time() - t0)


def block_r156():
    g = dg.R156
    n_expected = len(g["FALLBACK_ANGLES"]) * 3
    print(f"\n=== Block R156: {len(g['FALLBACK_ANGLES'])} angles x 3 scenes (empty,off_bracket,off_pass) "
          f"= {n_expected} calls @ steps={g['STEPS_AMBIENT']} (off_lab/off_field REUSED from exp-030) ===", flush=True)
    t0 = time.time()
    main_args = [(float(th), g["STEPS_AMBIENT"]) for th in g["FALLBACK_ANGLES"]]
    scenes = {}
    n_runs = 0
    with ProcessPoolExecutor(max_workers=4) as ex:
        for theta, steps, out, dt in ex.map(run_group_r156, main_args):
            scenes[theta] = out
            n_runs += 3
            print(f"  [r156 {len(scenes):1d}/{len(main_args)}] theta={theta:+05.1f} ({dt:5.1f}s)", flush=True)
    elapsed = time.time() - t0
    assert n_runs == n_expected, f"Block R156 run-count mismatch: {n_runs} != {n_expected}"

    r_empty = _contrast(scenes, "empty", g["FALLBACK_ANGLES"], g["ABSORB"], g["OBJ"][1], g["W_OBJ"], g["GUARD_OUT"], g["W_FLANK"])
    r_br = _contrast(scenes, "off_bracket", g["FALLBACK_ANGLES"], g["ABSORB"], g["OBJ"][1], g["W_OBJ"], g["GUARD_OUT"], g["W_FLANK"])
    r_ps = _contrast(scenes, "off_pass", g["FALLBACK_ANGLES"], g["ABSORB"], g["OBJ"][1], g["W_OBJ"], g["GUARD_OUT"], g["W_FLANK"])
    fresh_floor156 = r_empty["C_empty"]        # signed, per rider (b)

    C = {"off_bracket": r_br["C"], "off_pass": r_ps["C"],
         "off_lab": dg.R156_REUSED_C["off_lab"], "off_field": dg.R156_REUSED_C["off_field"]}
    tau = {"off_bracket": g["TAU_OFF_BRACKET"], "off_pass": g["TAU_OFF_PASS"],
           "off_lab": dg.R156_REUSED_TAU["off_lab"], "off_field": dg.R156_REUSED_TAU["off_field"]}

    # rider (b): determinism check -- fresh empty(156) vs exp-030's own reused value
    delta_empty_vs_exp030 = abs(fresh_floor156 - dg.R156_REUSED_C_EMPTY)

    # g_corr, using THIS cycle's own fresh empty(156) for ALL FOUR articles
    # (including the two reused scene profiles, per Phase-1 rider (b))
    g_corr = {a: abs(C[a] - fresh_floor156) / tau[a] for a in C}
    taus_sorted = [tau[a] for a in ("off_bracket", "off_pass", "off_lab", "off_field")]
    gcorr_sorted = [g_corr[a] for a in ("off_bracket", "off_pass", "off_lab", "off_field")]
    A156, B156, resid156 = fit_free_line(taus_sorted, gcorr_sorted)

    residual_gate_pass = resid156 <= dg.RESIDUAL_GATE_4ARTICLE
    delta_A_vs_78 = abs(A156 - dg.A78_ESTABLISHED)
    if not residual_gate_pass:
        disposition_naive = "INCONCLUSIVE (residual gate failed)"
    elif delta_A_vs_78 <= dg.A_CONFIRMED_BAND:
        disposition_naive = "SCALE-INVARIANT (naive, vs raw A78 -- see chord-corrected disposition)"
    elif delta_A_vs_78 >= dg.A_ARTIFACT_BAND:
        disposition_naive = "SCALE-DIVERGENT (naive, vs raw A78)"
    else:
        disposition_naive = "INCONCLUSIVE (delta_A between bands)"

    # mandatory fix 2 (EM): common-mode vs differential floor decomposition.
    # C78 established anchors -- r=78, native cpl=20, all four articles, all
    # sourced from exp-032/results.json's own committed `ambient_contrasts`
    # (off_lab/off_field: exact digits; off_pass: matches the 5-blind-seat-
    # and Red-Team-verified -0.00450 citation used throughout Phase 2;
    # off_bracket: -0.0020992636423987046, exp-032's own true native-cpl20
    # digit).
    # CORRECTED (Red Team Phase-5 audit, attack 3, mandatory fix 3): the
    # first-draft off_bracket value here (-0.00218) was transcribed from
    # exp-033's own ROUNDED cpl=30 reading, not exp-032's native cpl=20
    # figure every other entry in this dict actually is -- a mislabeled
    # anchor of the same transcription-risk class as the historical
    # SIGMA_ON/run-count bugs. The correction shifts the common-mode
    # decomposition below (spread/mean: 32.76%->26.18%, common_mode_fraction:
    # 67.24%->73.82%) -- corrected same-shift, disclosed not smoothed over.
    C78 = {"off_bracket": -0.0020992636423987046, "off_pass": -0.00450,
           "off_lab": -0.005530667330154762, "off_field": -0.02179302617779434}
    # ΔC(78->156) per article = C(156) - C(78). Note this cycle's own fresh
    # C_empty(156) and exp-032/033's native C_empty(78) are NOT differenced
    # here directly -- the native bench only ever published the empty
    # scene's MAGNITUDE (the decision floor), never a signed C_empty, so an
    # empty-anchored absolute delta isn't available on the historical
    # record. The honest common-mode test instead asks: do the four
    # per-article deltas cluster tightly (common-mode, EM's "guaranteed by
    # construction" risk) or spread widely relative to their own size
    # (differential, real tau-dependent curvature)?
    delta_C_per_article = {a: C[a] - C78[a] for a in C}
    spread = max(delta_C_per_article.values()) - min(delta_C_per_article.values())
    mean_abs = np.mean([abs(v) for v in delta_C_per_article.values()])
    common_mode_fraction = 1.0 - (spread / mean_abs if mean_abs else float("nan"))

    # mandatory fix 3: geometry-corrected chord-model null (fresh rederivation)
    g0_geo_156 = dg.chord_model_g0(g["R_OUT"], g["PLANE_DX"], g["OBJ_X"], g["SRC_X"],
                                    g["FALLBACK_ANGLES"], g["ABSORB"], g["TAPER"],
                                    g["GUARD_OUT"], g["W_FLANK"])
    g0_geo_78native = dg.chord_model_g0(78, 15, 170, 300, dg.FALLBACK_ANGLES, 40, 40, 185, 78)
    delta_A_vs_chord156 = abs(A156 - g0_geo_156)

    return {
        "n_new_runs": n_runs, "elapsed_s": elapsed,
        "fresh_C_empty_156": fresh_floor156,
        "delta_vs_exp030_reused_empty": delta_empty_vs_exp030,
        "C": C, "tau": tau, "g_corr": g_corr,
        "fit": {"A": A156, "B": B156, "max_residual": resid156,
                "residual_gate_pass": residual_gate_pass,
                "delta_A_vs_A78": delta_A_vs_78, "disposition_naive": disposition_naive},
        "common_mode_decomposition": {"delta_C_per_article": delta_C_per_article,
                                       "spread": spread, "mean_abs": mean_abs,
                                       "common_mode_fraction": common_mode_fraction},
        "chord_model_null": {"g0_geo_156": g0_geo_156, "g0_geo_78native_sanity": g0_geo_78native,
                              "delta_A_vs_chord156": delta_A_vs_chord156},
    }


# ===================================================== Block N17 (shared harness, block-local geometry)
def run_group_n17(geom, args):
    theta, steps = args
    t0 = time.time()
    cap_e = _one_run(geom["NX"], geom["NY"], geom.get("CPL", 20), geom["ABSORB"], geom["SRC_X"],
                      geom["TAPER"], geom["OBJ"], geom["R_OUT"], None, theta, steps)
    cap_p = _one_run(geom["NX"], geom["NY"], geom.get("CPL", 20), geom["ABSORB"], geom["SRC_X"],
                      geom["TAPER"], geom["OBJ"], geom["R_OUT"], geom["SIGMA_OFF_PASS"], theta, steps)
    out = {"empty": _profile(cap_e, geom["PLANE_X"], geom["ABSORB"], geom["NY"] - geom["ABSORB"]),
           "off_pass": _profile(cap_p, geom["PLANE_X"], geom["ABSORB"], geom["NY"] - geom["ABSORB"])}
    return (theta, steps, out, time.time() - t0)


def block_n17(geom, label, established_C, established_margin_bar=0.005):
    n_expected = len(geom["N17_ANGLES"]) * 2
    print(f"\n=== Block {label}: {len(geom['N17_ANGLES'])} angles x 2 scenes "
          f"= {n_expected} calls @ steps={geom['STEPS_AMBIENT']} (NX={geom['NX']} NY={geom['NY']}) ===", flush=True)
    t0 = time.time()
    main_args = [(float(th), geom["STEPS_AMBIENT"]) for th in geom["N17_ANGLES"]]
    scenes = {}
    n_runs = 0
    with ProcessPoolExecutor(max_workers=4) as ex:
        for theta, steps, out, dt in ex.map(partial(run_group_n17, geom), main_args):
            scenes[theta] = out
            n_runs += 2
            print(f"  [{label} {len(scenes):2d}/{len(main_args)}] theta={theta:+05.1f} ({dt:5.1f}s)", flush=True)
    elapsed = time.time() - t0
    assert n_runs == n_expected, f"Block {label} run-count mismatch: {n_runs} != {n_expected}"

    r_empty17 = _contrast(scenes, "empty", geom["N17_ANGLES"], geom["ABSORB"], geom["OBJ"][1],
                           geom["W_OBJ"], geom["GUARD_OUT"], geom["W_FLANK"])
    r_pass17 = _contrast(scenes, "off_pass", geom["N17_ANGLES"], geom["ABSORB"], geom["OBJ"][1],
                          geom["W_OBJ"], geom["GUARD_OUT"], geom["W_FLANK"])
    C_empty_N17 = abs(r_empty17["C_empty"])
    C_N9_fromN17domain = _contrast(scenes, "off_pass", dg.FALLBACK_ANGLES, geom["ABSORB"], geom["OBJ"][1],
                                    geom["W_OBJ"], geom["GUARD_OUT"], geom["W_FLANK"])["C"]
    C_N17 = r_pass17["C"]

    coverage_gate_pass = C_empty_N17 <= dg.N17_COVERAGE_GATE

    delta_N9_N17 = abs(C_N17 - C_N9_fromN17domain)

    def score(c):
        ac = abs(c)
        return "PASS" if ac < 0.005 else ("MARGINAL" if ac < 0.02 else "FAIL")

    return {
        "n_new_runs": n_runs, "elapsed_s": elapsed,
        "C_empty_N17": C_empty_N17, "coverage_gate_pass": coverage_gate_pass,
        "coverage_gate_threshold": dg.N17_COVERAGE_GATE,
        "C_N9_from_this_domain": C_N9_fromN17domain, "C_N17": C_N17,
        "delta_N9_vs_N17_same_domain": delta_N9_N17,
        "C_established_reference": established_C,
        "delta_vs_established": abs(C_N9_fromN17domain - established_C) if established_C is not None else None,
        "ladder_N17": score(C_N17), "ladder_N9_this_domain": score(C_N9_fromN17domain),
    }


def main():
    t_start = time.time()
    print(f"exp-034: 4 blocks, 115 new FDTD calls total, {os.cpu_count()} cpus", flush=True)

    res_cpl40 = block_cpl40()
    res_r156 = block_r156()
    res_n17_156 = block_n17(dg.N17_156, "N17_156", established_C=None)
    res_n17_native = block_n17(dg.N17_NATIVE, "N17_NATIVE",
                                established_C=dg.N17_NATIVE_ESTABLISHED_C)

    total_runs = res_cpl40["n_new_runs"] + res_r156["n_new_runs"] + \
        res_n17_156["n_new_runs"] + res_n17_native["n_new_runs"]
    assert total_runs == 115, f"TOTAL run-count mismatch: {total_runs} != 115"
    elapsed = time.time() - t_start

    out = {
        "meta": {"n_new_runs_total": total_runs, "elapsed_s_total": elapsed,
                 "eps_r_idealization_note": dg.EPS_R_IDEALIZATION_NOTE},
        "block_cpl40": res_cpl40,
        "block_r156": res_r156,
        "block_n17_156": res_n17_156,
        "block_n17_native": res_n17_native,
        "thermo_sidecar_analytic": {
            "label": "POST-RUN ANALYTIC, NOT AN FDTD OUTPUT (expressibility contract)",
            "absorbed_fraction_chord_model": dg.THERMO_ABSORBED_FRACTION,
            "dT_steady_K": dg.THERMO_DT_STEADY_K,
            "NETD_band_K": dg.NETD_BAND_K,
        },
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1)

    print(f"\nexp-034 done in {elapsed:.0f}s, {total_runs} new FDTD calls", flush=True)
    print(f"\n--- Block CPL40 ---")
    print(f"  fresh floor(cpl=40)={res_cpl40['fresh_floor_cpl40']:.6e} "
          f"(cpl20={dg.CPL40_ESTABLISHED['floor_cpl20']:.4e}, cpl30={dg.CPL40_ESTABLISHED['floor_cpl30']:.4e})")
    print(f"  C(off_pass,cpl=40)={res_cpl40['C_off_pass_cpl40']:+.6f}  ladder={res_cpl40['ladder']}  "
          f"(cpl20={dg.CPL40_ESTABLISHED['C_off_pass_cpl20']:+.5f}, cpl30={dg.CPL40_ESTABLISHED['C_off_pass_cpl30']:+.5f})")
    print(f"  settling relative delta={res_cpl40['settling_relative_delta']:.4f} (band <=0.03)")
    print(f"\n--- Block R156 ---")
    print(f"  fresh C_empty(156)={res_r156['fresh_C_empty_156']:+.6e}  "
          f"(exp-030 reused: {dg.R156_REUSED_C_EMPTY:+.6e}, delta={res_r156['delta_vs_exp030_reused_empty']:.2e})")
    for a, c in res_r156["C"].items():
        print(f"  C({a},156)={c:+.6f}  g_corr={res_r156['g_corr'][a]:.4f}")
    print(f"  fit: A156={res_r156['fit']['A']:.6f} B156={res_r156['fit']['B']:.6f} "
          f"max_resid={res_r156['fit']['max_residual']:.6e} gate_pass={res_r156['fit']['residual_gate_pass']}")
    print(f"  delta_A vs A78={res_r156['fit']['delta_A_vs_A78']:.6f}  disposition(naive)={res_r156['fit']['disposition_naive']}")
    print(f"  common-mode fraction={res_r156['common_mode_decomposition']['common_mode_fraction']:.4f}")
    print(f"  chord-model null: g0_geo(156)={res_r156['chord_model_null']['g0_geo_156']:.6f}  "
          f"delta_A_vs_chord156={res_r156['chord_model_null']['delta_A_vs_chord156']:.6f}")
    print(f"\n--- Block N17_156 ---")
    print(f"  C_empty(N17)={res_n17_156['C_empty_N17']:.6e}  coverage_gate_pass={res_n17_156['coverage_gate_pass']}")
    print(f"  C(N9,thisdomain)={res_n17_156['C_N9_from_this_domain']:+.6f}  C(N17)={res_n17_156['C_N17']:+.6f}  "
          f"delta={res_n17_156['delta_N9_vs_N17_same_domain']:.4e}")
    print(f"\n--- Block N17_NATIVE ---")
    print(f"  C_empty(N17)={res_n17_native['C_empty_N17']:.6e}  coverage_gate_pass={res_n17_native['coverage_gate_pass']}")
    print(f"  C(N9,thisdomain)={res_n17_native['C_N9_from_this_domain']:+.6f}  C(N17)={res_n17_native['C_N17']:+.6f}  "
          f"delta={res_n17_native['delta_N9_vs_N17_same_domain']:.4e}  "
          f"vs exp-033 established={res_n17_native['C_established_reference']:+.6f} "
          f"(delta={res_n17_native['delta_vs_established']:.4e})")
    print("\nresults.json written")


if __name__ == "__main__":
    main()
