"""exp-035 -- Closing the R156/N17_156 Domain x Quadrature Factorial,
Rebuilding N17_NATIVE by RATIO=1.5, and Reconciling T15: measurement harness.
=============================================================================
Panel Iteration 12 (lead QUANTUM OPTICS, rotation; synthesis: Director, post
Red Team's PROCEED-WITH-MANDATORY-FIXES verdict -- see design_geometry.py
module docstring and NOTES.md Phase 3 for the full accepted/overridden
record). Three independent blocks (Red Team's own mandatory-fix-1 discipline,
inherited from exp-034: block-local article lists, no shared cross-block
harness).

Run counts (each block's own scoped article list, printed/asserted below):
  Block T16_CLOSE:     17 angles x 2 scenes (empty,off_pass) = 34
  Block N17_NATIVE_V2:  17 angles x 2 scenes (empty,off_pass) = 34
  Block T15_RECONCILE: 0 (desk-only, corrected per mandatory fixes 1-3)
  TOTAL: 68 new FDTD calls.

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


def block_n17(geom, label, established_C=None):
    """Reused verbatim in structure from exp-034's own block_n17(), extended
    per Red Team's mandatory fix 4 (EM's catch): a per-angle empty-scene
    check at theta=+-40deg specifically, computed from the SAME `scenes`
    dict already captured for the aggregate result -- zero additional FDTD
    cost. Advisory only (see design_geometry.PER_ANGLE_EMPTY_ADVISORY_BOUND
    docstring) -- not a previously-validated N=1/+-40deg-specific gate."""
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

    # mandatory fix 4 (Red Team attack 6, EM's catch): per-angle empty check at +-40deg
    c_empty_plus40 = _contrast(scenes, "empty", (40.0,), geom["ABSORB"], geom["OBJ"][1],
                                geom["W_OBJ"], geom["GUARD_OUT"], geom["W_FLANK"])["C_empty"]
    c_empty_minus40 = _contrast(scenes, "empty", (-40.0,), geom["ABSORB"], geom["OBJ"][1],
                                 geom["W_OBJ"], geom["GUARD_OUT"], geom["W_FLANK"])["C_empty"]
    per_angle_40_advisory_pass = (abs(c_empty_plus40) <= dg.PER_ANGLE_EMPTY_ADVISORY_BOUND
                                   and abs(c_empty_minus40) <= dg.PER_ANGLE_EMPTY_ADVISORY_BOUND)

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
        "per_angle_empty_check": {
            "C_empty_plus40": c_empty_plus40, "C_empty_minus40": c_empty_minus40,
            "advisory_bound": dg.PER_ANGLE_EMPTY_ADVISORY_BOUND,
            "advisory_pass": per_angle_40_advisory_pass,
            "note": ("Advisory only (mandatory fix 4, EM's catch) -- NOT a previously-"
                     "validated N=1/+-40deg-specific gate; a fail here means P-A1/P-B2's "
                     "interaction/margin verdicts should be read with reduced confidence, "
                     "not silently trusted, even if the aggregate coverage_gate_pass above "
                     "is clean."),
        },
    }


# ===================================================== Block T15_RECONCILE (zero FDTD cost)
def block_t15_reconcile():
    """Corrected per mandatory fixes 1-3 (Red Team Phase-2 audit, PHOTONICS'
    original catch): the Phase-1 proposal's cpl=40 comparator was a
    copy/paste bug, not a measurement. This block uses RAW g=|C|/tau at
    cpl=20/30/40 (all already published) against chord_model_g0() at each
    resolution's own geometry, plus THERMODYNAMICS' pi/4-amplitude
    extension."""
    rows = {}
    for cpl in (20, 30, 40):
        g0 = dg.chord_model_g0(**dg.T15_GEOM[cpl], angles_deg=dg.FALLBACK_ANGLES)
        g_raw = dg.T15_G_RAW[cpl]
        gap = g_raw - g0
        gap_pct = gap / g0
        rows[cpl] = {"g_raw": g_raw, "chord_model_g0": g0, "gap": gap, "gap_pct": gap_pct}

    gap20, gap40 = rows[20]["gap_pct"], rows[40]["gap_pct"]
    if abs(gap40) <= abs(gap20) * 1.1:
        disposition = "STABLE-OR-SHRINKING (T15 CLOSES as a discretization artifact)"
    elif abs(gap40) > abs(gap20) * 1.5:
        disposition = "GROWING (T15 modestly REOPENS -- a real, resolution-persistent effect survives)"
    else:
        disposition = "INCONCLUSIVE"

    # THERMO's mandatory extension: pi/4 peak-chord amplitude vs chord_model_g0
    pi4_rows = {}
    for cpl in (20, 30, 40):
        g0 = rows[cpl]["chord_model_g0"]
        pi4_gap_pct = (dg.PI4_PEAK_CHORD_AMPLITUDE - g0) / g0
        pi4_rows[cpl] = {"pi4_amplitude": dg.PI4_PEAK_CHORD_AMPLITUDE, "chord_model_g0": g0,
                          "gap_pct": pi4_gap_pct}

    return {
        "n_new_runs": 0, "elapsed_s": 0.0,
        "raw_g_vs_chord_model": rows,
        "disposition": disposition,
        "disposition_bands": {"stable_or_shrinking": "gap(40) <= gap(20)*1.1",
                               "growing": "gap(40) > gap(20)*1.5", "else": "inconclusive"},
        "pi4_amplitude_vs_chord_model": pi4_rows,
        "note": ("Corrected per Red Team Phase-2 mandatory fixes 1-3: the original Phase-1 "
                 "proposal's cpl=40 comparator (0.687124) was a copy/paste of the r=117 "
                 "chord-model value, not a measurement (PHOTONICS' catch, independently "
                 "confirmed by Red Team). This table uses raw g=|C|/tau at all three "
                 "resolutions, all zero-new-cost, and adds THERMO's pi/4-vs-chord-model "
                 "comparison (mandatory fix 3)."),
    }


def main():
    t_start = time.time()
    print(f"exp-035: 3 blocks, 68 new FDTD calls total, {os.cpu_count()} cpus", flush=True)

    res_t16 = block_n17(dg.T16_CLOSE, "T16_CLOSE", established_C=None)
    res_n17native = block_n17(dg.N17_NATIVE_V2, "N17_NATIVE_V2",
                               established_C=dg.N17_NATIVE_V2_ESTABLISHED_C)
    res_t15 = block_t15_reconcile()

    total_runs = res_t16["n_new_runs"] + res_n17native["n_new_runs"] + res_t15["n_new_runs"]
    assert total_runs == 68, f"TOTAL run-count mismatch: {total_runs} != 68"
    elapsed = time.time() - t_start

    # ---- Block T16_CLOSE: interaction decomposition ----
    C_N17_R156dom_new = res_t16["C_N17"]
    interaction = (C_N17_R156dom_new - dg.T16_C_N9_R156DOM) - dg.T16_QUADRATURE_EFFECT_ON_N17_156DOM
    if abs(interaction) <= 1.0e-4:
        interaction_verdict = "CONFIRMED-ADDITIVE"
    elif abs(interaction) >= 2.0e-4:
        interaction_verdict = "REAL INTERACTION (domain choice and angular convergence are not independent)"
    else:
        interaction_verdict = "INCONCLUSIVE"

    def score(c):
        ac = abs(c)
        return "PASS" if ac < 0.005 else ("MARGINAL" if ac < 0.02 else "FAIL")

    out = {
        "meta": {"n_new_runs_total": total_runs, "elapsed_s_total": elapsed,
                 "eps_r_idealization_note": (
                     "g0/g_corr/raw-C in this line are properties of an index-matched "
                     "(eps_r == 1.0, n-1 <~ 1e-5) article -- a gas/aerosol host only. At a "
                     "realizable condensed-phase index (n=1.33-1.5): two-surface ambient "
                     "contrast C = -0.040 to -0.078 (VISION-ladder FAIL, independent of tau), "
                     "specular return 143-571x the established camera floor (constraint-2 "
                     "violation). NOT a material transfer function. (Fifth recurrence of this "
                     "exact documentation gap across exp-031/032/033/034/035.)"),
                 "materials_realizability_scope_note": (
                     "This cycle's T15 reconciliation (Block T15_RECONCILE) does NOT address, "
                     "and is not a substitute for, REALIZABILITY_MEMO.md's still-open literature "
                     "check -- D_req and the TPA irradiance gap are algebraically orthogonal to "
                     "the ambient-contrast reading refined here (Red Team's ruling on MATERIALS' "
                     "Phase-2 attack, mandatory fix 5)."),
                 "n9_n17_n33_convergence_note": (
                     "N17 (this cycle) is still only the SECOND point of an eventual three-point "
                     "(N9->N17->N33) angular-convergence sequence, not a converged endpoint -- "
                     "N33 is queued as Iteration-13's top-ranked item (Red Team's ruling on "
                     "VISION's Phase-2 attack, mandatory fix 6: substance accepted, but folding "
                     "N33 into THIS cycle was rejected on cost grounds -- N9 is a zero-marginal-"
                     "cost byproduct of the N17 run, not a separate 17-call leg, so there was no "
                     "free substitution available)."),
                 },
        "block_t16_close": {**res_t16,
                             "existing_cells_reused": {
                                 "C_N9_R156dom": dg.T16_C_N9_R156DOM,
                                 "C_N9_N17_156dom": dg.T16_C_N9_N17_156DOM,
                                 "C_N17_N17_156dom": dg.T16_C_N17_N17_156DOM,
                             },
                             "domain_effect_at_N9": dg.T16_DOMAIN_EFFECT_AT_N9,
                             "quadrature_effect_on_N17_156dom": dg.T16_QUADRATURE_EFFECT_ON_N17_156DOM,
                             "additive_prediction_C_N17_R156dom": dg.T16_ADDITIVE_PREDICTION_C_N17_R156DOM,
                             "interaction": interaction,
                             "interaction_verdict": interaction_verdict,
                             "ladder_N17_R156dom": score(C_N17_R156dom_new)},
        "block_n17_native_v2": res_n17native,
        "block_t15_reconcile": res_t15,
        "thermo_sidecar_analytic": {
            "label": "POST-RUN ANALYTIC, NOT AN FDTD OUTPUT (expressibility contract); "
                     "off_pass tau_center=0.0065 unchanged from exp-034 -- sidecar constants "
                     "carried forward, not recomputed (mandatory fix 3 scope note)",
            "tau_off_pass": dg.TAU_OFF_PASS,
        },
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1)

    print(f"\nexp-035 done in {elapsed:.0f}s, {total_runs} new FDTD calls", flush=True)
    print(f"\n--- Block T16_CLOSE ---")
    print(f"  C_empty(N17)={res_t16['C_empty_N17']:.6e}  coverage_gate_pass={res_t16['coverage_gate_pass']}")
    print(f"  per-angle empty +-40deg: {res_t16['per_angle_empty_check']}")
    print(f"  C(N9,thisdomain)={res_t16['C_N9_from_this_domain']:+.6f}  C(N17)={res_t16['C_N17']:+.6f}")
    print(f"  additive prediction={dg.T16_ADDITIVE_PREDICTION_C_N17_R156DOM:+.6f}  "
          f"interaction={interaction:+.6e}  verdict={interaction_verdict}")
    print(f"\n--- Block N17_NATIVE_V2 ---")
    print(f"  C_empty(N17)={res_n17native['C_empty_N17']:.6e}  coverage_gate_pass={res_n17native['coverage_gate_pass']}")
    print(f"  per-angle empty +-40deg: {res_n17native['per_angle_empty_check']}")
    print(f"  C(N9,thisdomain)={res_n17native['C_N9_from_this_domain']:+.6f}  C(N17)={res_n17native['C_N17']:+.6f}  "
          f"delta={res_n17native['delta_N9_vs_N17_same_domain']:.4e}  "
          f"vs established={res_n17native['C_established_reference']:+.6f} "
          f"(delta={res_n17native['delta_vs_established']:.4e})  margin={dg.N17_NATIVE_V2_MARGIN:.4e}")
    print(f"\n--- Block T15_RECONCILE ---")
    for cpl, row in res_t15["raw_g_vs_chord_model"].items():
        print(f"  cpl={cpl}: g_raw={row['g_raw']:.6f}  chord_model_g0={row['chord_model_g0']:.6f}  "
              f"gap={row['gap_pct']*100:+.3f}%")
    print(f"  disposition={res_t15['disposition']}")
    print("\nresults.json written")


if __name__ == "__main__":
    main()
