"""exp-032 -- The sigma(I) OFF-State PASS-Boundary Run: measurement harness.
==============================================================================
Panel Iteration 9 (lead MATERIALS, rotation; synthesis: Director, post Red
Team's proceed-with-mandatory-fixes verdict). Two uniform-conductivity,
index-matched (eps_r=1) sponge disks -- off_pass (tau=0.0065, the headline
PASS-boundary probe) and off_bracket (tau=0.003, Red Team's mandatory
below-tau_off discriminator) -- measured on exp-026's own already-validated
ambient bench (lab/ambient.py), the +-35deg N=9 fallback geometry, unchanged.

2 articles x 9 angles x 3 lambda = 54 new object runs + 27 new empty runs
(empty reused across both articles, same (angle,lambda) grid) = 81 new FDTD
calls total. No beam-scene block -- explicitly out of scope this cycle (the
OFF-state endpoint is definitionally not beam-terminating; the ON/beam
channel was exp-026's job and is not re-measured here).

Predictions committed in NOTES.md BEFORE this file's first run (house
discipline, non-negotiable).
"""

import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, HERE)

import design_geometry as dg
from lab import Sim, ambient as amb, sections as sc

STEPS_AMBIENT = 1400   # exp-026's own value, unchanged (same geometry/domain)


def build_ambient(article, sim):
    cx, cy = dg.OBJ
    x = np.arange(sim.nx)[:, None]
    y = np.arange(sim.ny)[None, :]
    mask = (x - cx) ** 2 + (y - cy) ** 2 <= dg.R_OUT ** 2
    sim.sigma_e[mask] += dg.SIGMA_BY_ARTICLE[article]
    sim.objects.append({"type": "uniform_sponge_disk",
                        "params": {"cx": cx, "cy": cy, "r": dg.R_OUT,
                                   "sigma": dg.SIGMA_BY_ARTICLE[article],
                                   "tau_center": dg.TAU_BY_ARTICLE[article]}})


def one_ambient_run(article, theta, cpl):
    sim = Sim(dg.NX, dg.NY, cells_per_lambda=cpl, courant_frac=0.99,
              absorb=dg.ABSORB)
    if article != "empty":
        build_ambient(article, sim)
    sim.add_line_source(dg.SRC_X, angle_deg=theta, edge=dg.TAPER, amplitude=1.0)
    sim.run(STEPS_AMBIENT)
    return sc.full_capture(sim)


def run_ambient_group(args):
    lam_nm, cpl, theta = args
    t0 = time.time()
    out = {}
    cap_e = one_ambient_run("empty", theta, cpl)
    ph_e = sc.phasors(cap_e)
    prof_e = amb.observer_profile(ph_e, dg.PLANE_X, dg.ABSORB, dg.NY - dg.ABSORB)
    out["empty"] = {"profile": prof_e.tolist()}
    for art in dg.ARTICLES_AMBIENT:
        cap = one_ambient_run(art, theta, cpl)
        ph = sc.phasors(cap)
        prof = amb.observer_profile(ph, dg.PLANE_X, dg.ABSORB, dg.NY - dg.ABSORB)
        out[art] = {"profile": prof.tolist()}
    return (lam_nm, theta, out, time.time() - t0)


def main():
    groups = [(lam_nm, cpl, float(th))
              for lam_nm, cpl in dg.CPL.items() for th in dg.FALLBACK_ANGLES]
    n_calls = len(groups) * (1 + len(dg.ARTICLES_AMBIENT))
    print(f"exp-032 ambient: {len(groups)} groups ({n_calls} FDTD calls incl. empty), "
          f"{os.cpu_count()} cpus", flush=True)
    t0 = time.time()
    ambient_results = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for lam_nm, theta, out, dt in ex.map(run_ambient_group, groups):
            ambient_results[(lam_nm, theta)] = out
            print(f"  [{len(ambient_results):2d}/{len(groups)}] lambda={lam_nm} "
                  f"theta={theta:+05.1f} ({dt:5.1f} s)", flush=True)
    elapsed = time.time() - t0
    print(f"ambient block done in {elapsed:.0f} s", flush=True)

    def contrast(article, lam_nm, angles=dg.FALLBACK_ANGLES):
        profs, e_profs = [], []
        for th in angles:
            grp = ambient_results[(lam_nm, float(th))]
            profs.append(np.array(grp[article]["profile"]))
            e_profs.append(np.array(grp["empty"]["profile"]))
        weights = [1.0] * len(angles)
        return amb.contrast_from_runs(profs, e_profs, weights, dg.ABSORB,
                                      dg.OBJ[1], dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)

    table, floors = {}, {}
    for art in ("empty",) + dg.ARTICLES_AMBIENT:
        for lam_nm in dg.CPL:
            r = contrast(art, lam_nm)
            table[f"{art}/{lam_nm}"] = {"C": r["C"], "C_empty": r["C_empty"]}
            if art == "empty":
                floors[str(lam_nm)] = abs(r["C_empty"])

    # N-convergence: N5 vs N9, off_pass @ 600nm -- ZERO new runs, exp-026's
    # own P-MAT7 idiom, inherited (not re-derived as a fresh prediction --
    # this geometry's convergence is already established at a comparable
    # magnitude by off_lab's own N5-vs-N9 check, exp-026).
    c_n9 = contrast("off_pass", 600, dg.FALLBACK_ANGLES)["C"]
    c_n5 = contrast("off_pass", 600, dg.N5_SUBSAMPLE)["C"]
    conv_n5_n9 = abs(c_n5 - c_n9)

    # g = |C|/tau_center, per article per lambda
    g_values = {}
    for art in dg.ARTICLES_AMBIENT:
        tau = dg.TAU_BY_ARTICLE[art]
        for lam_nm in dg.CPL:
            g_values[f"{art}/{lam_nm}"] = abs(table[f"{art}/{lam_nm}"]["C"]) / tau

    # VISION ladder scoring: PASS |C|<0.005, MARGINAL [0.005,0.02), FAIL >=0.02
    def score(c):
        ac = abs(c)
        if ac < 0.005:
            return "PASS"
        elif ac < 0.02:
            return "MARGINAL"
        return "FAIL"

    ladder = {}
    for art in dg.ARTICLES_AMBIENT:
        for lam_nm in dg.CPL:
            ladder[f"{art}/{lam_nm}"] = score(table[f"{art}/{lam_nm}"]["C"])

    # QUANTUM's mandatory disposition clause (Red Team fix #2, zero cost):
    # flag whether g600 continues off_lab's own unexplained-high miss
    # (established off_lab g600 = 0.6913, itself already a documented,
    # unexplained overshoot). If off_pass's own g600 is ALSO >= 0.69, the
    # 600nm reading is anomaly-consistent and must not be folded silently
    # into an unqualified clean-PASS headline even if it numerically PASSes.
    g600_off_pass = g_values["off_pass/600"]
    g600_anomaly_consistent = g600_off_pass >= 0.69

    # THERMODYNAMICS' mandatory energy sidecar (Red Team fix #3): must show
    # its arithmetic, not just assert "negligible". POST-RUN ANALYTIC ONLY,
    # not an FDTD output (expressibility contract).
    tau_off_pass = dg.TAU_OFF_PASS
    abs_ext_lo, abs_ext_hi = dg.ESTABLISHED_ABS_EXT_RATIO_ON
    # optically-thin absorptance approx (tau << 1): absorbed fraction of
    # intercepted (geometric-cross-section) flux ~ tau_off_pass.
    thermo_absorbed_fraction_of_intercepted = tau_off_pass
    # relative to the ON article's own established sigma_abs/sigma_ext
    # (tau=3.9, deep-shadow regime) -- purely a scale comparison, not a
    # claim the two regimes share a mechanism.
    thermo_ratio_vs_on = tau_off_pass / dg.TAU_ON_ESTABLISHED

    out = {
        "meta": {"geometry_ambient": {k: getattr(dg, k) for k in
                                      ("NX", "NY", "ABSORB", "SRC_X", "OBJ",
                                       "R_OUT", "PLANE_X", "W_OBJ", "GUARD_OUT",
                                       "W_FLANK", "BOX")},
                 "fallback_angles": list(dg.FALLBACK_ANGLES),
                 "n5_subsample": list(dg.N5_SUBSAMPLE),
                 "tau": dg.TAU_BY_ARTICLE,
                 "sigma": dg.SIGMA_BY_ARTICLE,
                 "g_band_harmonized": list(dg.G_BAND),
                 "decision_floor_reused": dg.DECISION_FLOOR,
                 "off_lab_established_anchor": {"C": dg.OFF_LAB_C_ESTABLISHED,
                                                 "g": dg.OFF_LAB_G_ESTABLISHED,
                                                 "tau": dg.TAU_OFF_LAB_ESTABLISHED},
                 "elapsed_s": elapsed,
                 "n_new_runs": n_calls},
        "ambient_contrasts": table,
        "ambient_decision_floors_new_empty": floors,
        "g_values": g_values,
        "convergence_n5_vs_n9_off_pass_600": {"N5": c_n5, "N9": c_n9,
                                              "abs_delta": conv_n5_n9},
        "vision_ladder": ladder,
        "quantum_disposition_g600": {
            "g600_off_pass": g600_off_pass,
            "off_lab_established_g600": dg.OFF_LAB_G_ESTABLISHED[600],
            "anomaly_consistent_threshold": 0.69,
            "flag_anomaly_consistent": g600_anomaly_consistent,
        },
        "thermo_sidecar_analytic": {
            "label": "POST-RUN ANALYTIC, NOT AN FDTD OUTPUT (expressibility contract)",
            "tau_off_pass": tau_off_pass,
            "absorbed_fraction_of_intercepted_flux_optically_thin_approx": thermo_absorbed_fraction_of_intercepted,
            "on_article_established_sigma_abs_over_sigma_ext_range": [abs_ext_lo, abs_ext_hi],
            "ratio_tau_off_pass_over_tau_on_established": thermo_ratio_vs_on,
        },
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1)

    print("\nambient decision floors (new empty runs, informational -- exp-024/025/026's "
          "committed values are the ones scored):")
    for k, v in floors.items():
        print(f"  {k}nm: {v:.6f}")
    print("\nambient Weber contrast C (fallback, N=9):")
    for art in dg.ARTICLES_AMBIENT:
        row = "  ".join(f"{lam}nm {table[f'{art}/{lam}']['C']:+.5f} [{ladder[f'{art}/{lam}']}]"
                        for lam in dg.CPL)
        print(f"  {art:12s} {row}")
    print(f"\nN-convergence (N5 vs N9, off_pass@600): N5={c_n5:+.5f} N9={c_n9:+.5f} "
          f"|delta|={conv_n5_n9:.5f}")
    print("\ng = |C|/tau_center:")
    for k, v in g_values.items():
        print(f"  {k}: g={v:.4f}")
    print(f"\nQUANTUM disposition (Red Team mandatory fix): g600(off_pass)={g600_off_pass:.4f} "
          f"vs off_lab established g600={dg.OFF_LAB_G_ESTABLISHED[600]:.4f} -> "
          f"{'ANOMALY-CONSISTENT (flag, do not read PASS as unqualified)' if g600_anomaly_consistent else 'no anomaly signal'}")
    print(f"\nTHERMODYNAMICS sidecar (post-run analytic, not FDTD output): "
          f"absorbed fraction of intercepted flux (optically-thin approx) "
          f"~{thermo_absorbed_fraction_of_intercepted:.4%}; "
          f"tau_off_pass/tau_on_established = {thermo_ratio_vs_on:.5f} "
          f"({thermo_ratio_vs_on*100:.3f}% of the ON article's own established "
          f"sigma_abs/sigma_ext={abs_ext_lo}-{abs_ext_hi} scale)")
    print("\nresults.json written")


if __name__ == "__main__":
    main()
