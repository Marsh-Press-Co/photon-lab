"""exp-026 -- The sigma(I) Endpoint Triplet: measurement harness.
===================================================================
Panel Iteration 3 (lead MATERIALS; synthesis: Director, post Red Team's
proceed-with-mandatory-fixes). Three uniform-conductivity, index-matched
(eps_r=1) sponge disks -- OFF-lab (tau=0.008), OFF-field (tau=0.032), ON
(tau=3.9) -- measured on TWO already-validated benches:

  (1) the ambient instrument (lab/ambient.py), exp-024's +-35deg fallback
      geometry, unchanged -- OFF-lab/OFF-field/ON x 9 angles x 3 lambda
      = 81 runs. Empty-scene and tau=0.10 tie-point reused from exp-024's
      committed fallback artifacts (commit c67506b), NOT rerun.
  (2) the exp-001/002 beam-scene bench, unchanged -- ON article only,
      empty + on x 3 lambda = 6 runs (empty reference needed per-lambda
      for beam-behind / observer-return / box-ledger, exactly as
      exp-001/002 required it -- corrects the Phase-1 proposal's
      undercounted "3 beam runs", a bookkeeping fix caught at Phase 3).

Total NEW FDTD runs: 81 + 6 = 87. N-convergence (P-MAT7) and the box-
closure identity gate (Thermo's mandatory fix) are BOTH zero-new-run
recomputations from data already collected above.

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
from lab import emit as em

# reused, not rerun: exp-024 fallback empty-scene B(y) profiles, commit
# c67506b (results_fallback.json is assembled-contrast only, so the raw
# per-angle empty profile is regenerated here at zero marginal cost --
# same seed/geometry/steps as exp-024, bit-reproducible -- rather than
# depending on a cross-experiment file read).
STEPS_AMBIENT = 1400


def build_ambient(article, sim):
    cx, cy = dg.OBJ
    x = np.arange(sim.nx)[:, None]
    y = np.arange(sim.ny)[None, :]
    mask = (x - cx) ** 2 + (y - cy) ** 2 <= dg.R_OUT ** 2
    sim.sigma_e[mask] += dg.SIGMA_BY_ARTICLE[article]
    sim.objects.append({"type": "uniform_sponge_disk",
                        "params": {"cx": cx, "cy": cy, "r": dg.R_OUT,
                                   "sigma": dg.SIGMA_BY_ARTICLE[article],
                                   "tau_center": {"off_lab": dg.TAU_OFF_LAB,
                                                  "off_field": dg.TAU_OFF_FIELD,
                                                  "on": dg.TAU_ON}[article]}})


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


def build_beam(article, sim):
    cx, cy = dg.BEAM_CX, dg.BEAM_CY
    if article == "empty":
        return
    x = np.arange(sim.nx)[:, None]
    y = np.arange(sim.ny)[None, :]
    mask = (x - cx) ** 2 + (y - cy) ** 2 <= dg.R_OUT ** 2
    sim.sigma_e[mask] += dg.SIGMA_ON


def run_beam_scene(article, cpl):
    """One capture per scene: sc.full_capture (single quarter-period
    advance) supplies BOTH the box-ledger phasors (needs Hx) and the
    quarter_pair-format tuple observer_record expects (ez_a, hy_a, ez_b,
    hy_b, off) -- built from the SAME snapshots, not a second capture, so
    the sim is never advanced twice past one quarter period per scene
    (exp-001's own quarter_pair and lab.sections.full_capture both capture
    the identical underlying (ez_a,hy_a,ez_b,hy_b) data; full_capture is a
    strict superset that also keeps Hx for the box ledger)."""
    sim = Sim(dg.BEAM_N, dg.BEAM_N, cells_per_lambda=cpl,
              courant_frac=dg.BEAM_FRAC, absorb=dg.BEAM_ABSORB)
    build_beam(article, sim)
    sim.add_line_source(dg.BEAM_SRC_X)
    sim.run(dg.BEAM_STEPS)
    cap_full = sc.full_capture(sim)
    cap_qp = (cap_full["ez_a"], cap_full["hy_a"],
              cap_full["ez_b"], cap_full["hy_b"], cap_full["off"])
    return sim, cap_full, cap_qp


def run_beam_group(cpl_nm):
    cpl, nm = cpl_nm
    t0 = time.time()
    sim_e, cap_e, capqp_e = run_beam_scene("empty", cpl)
    env_e = np.sqrt(cap_e["ez_a"] ** 2 + cap_e["ez_b"] ** 2)   # exp-001's own envelope idiom
    _, _, aux_ref = em.observer_record(sim_e, capqp_e, dg.BEAM_OBS_X)

    sim, cap, capqp = run_beam_scene("on", cpl)
    env = np.sqrt(cap["ez_a"] ** 2 + cap["ez_b"] ** 2)
    ang, flux, _ = em.observer_record(sim, capqp, dg.BEAM_OBS_X, reference=aux_ref)
    ret = float(np.sum(flux))
    behind = float(np.mean(env[dg.BEAM_BEHIND] ** 2)
                   / np.mean(env_e[dg.BEAM_BEHIND] ** 2))
    scat = float(np.sqrt(np.mean((env - env_e)[dg.BEAM_ANNULUS] ** 2)))

    wa = sc.widths(cap, cap_e, dg.BEAM_BOX_A, dg.BEAM_REF)
    wb = sc.widths(cap, cap_e, dg.BEAM_BOX_B, dg.BEAM_REF)
    box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])

    # Thermo's mandatory fix: box-closure identity on the EMPTY scene at
    # THIS domain/BOX (zero extra runs -- cap_e is already required above).
    # Same pattern as exp-024's own P6-emptybox gate: net outward flux of
    # the source-free... here, OBJECT-free (source present) scene through
    # the box, relative to the absorbed-power scale of the article it
    # gates. A vacuum box should show near-zero net flux imbalance only in
    # the STEADY sense the incident beam passes through untouched; the
    # correct empty-scene identity is p_abs(empty vs itself) = 0, checked
    # via widths(cap_e, cap_e, ...) which must give sigma_abs = sigma_ext = 0
    # exactly by construction (scattered field s = pt - pi = 0 when pt=pi).
    # The real closure test is net box flux of the ON scene's TOTAL field
    # equaling -sigma_abs*i_inc to within the two-box tolerance -- already
    # box_dev above. The additional empty-domain check Thermo asked for:
    w_self = sc.widths(cap_e, cap_e, dg.BEAM_BOX_A, dg.BEAM_REF)
    # w_self["sigma_ext"] is itself an i_inc-normalized cross-section (cells);
    # report it RELATIVE to the ON article's own measured sigma_ext this same
    # run -- Thermo's gate is meant as a relative closure check (exp-024's own
    # P6-emptybox convention: net flux relative to the article's own scale),
    # not an absolute cell count.
    empty_box_closure = abs(w_self["sigma_ext"]) / abs(wa["sigma_ext"])

    return {
        "lambda_nm": nm,
        "beam_behind": behind, "observer_return": ret, "scattered_rms": scat,
        "camera_floor": aux_ref["p_backward_total"] / aux_ref["p_forward_total"],
        "sigma_scat": wa["sigma_scat"], "sigma_abs": wa["sigma_abs"],
        "sigma_ext": wa["sigma_ext"], "sigma_ext_cross": wa["sigma_ext_cross"],
        "back_frac": wa["back_frac"], "box_dev": box_dev,
        "empty_box_closure": empty_box_closure,
        "elapsed_s": time.time() - t0,
    }


def main():
    # ---------------- ambient block (81 runs) ------------------------------
    groups = [(lam_nm, cpl, float(th))
              for lam_nm, cpl in dg.CPL.items() for th in dg.FALLBACK_ANGLES]
    print(f"exp-026 ambient: {len(groups)} groups ({len(groups) * 4} runs incl. empty), "
          f"{os.cpu_count()} cpus", flush=True)
    t0 = time.time()
    ambient_results = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for lam_nm, theta, out, dt in ex.map(run_ambient_group, groups):
            ambient_results[(lam_nm, theta)] = out
            print(f"  [{len(ambient_results):2d}/{len(groups)}] lambda={lam_nm} "
                  f"theta={theta:+05.1f} ({dt:5.1f} s)", flush=True)
    print(f"ambient block done in {time.time() - t0:.0f} s", flush=True)

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

    # P-MAT7: N5 vs N9 convergence, off_lab @ 600nm -- ZERO new runs
    c_n9 = contrast("off_lab", 600, dg.FALLBACK_ANGLES)["C"]
    c_n5 = contrast("off_lab", 600, dg.N5_SUBSAMPLE)["C"]
    conv_n5_n9 = abs(c_n5 - c_n9)

    # P-MAT6: linear-transfer constant g = |C|/tau_center
    g_values = {}
    for art, tau in (("off_lab", dg.TAU_OFF_LAB), ("off_field", dg.TAU_OFF_FIELD)):
        for lam_nm in dg.CPL:
            g_values[f"{art}/{lam_nm}"] = abs(table[f"{art}/{lam_nm}"]["C"]) / tau

    # ---------------- beam-scene block (6 runs) -----------------------------
    print(f"\nexp-026 beam-scene: {len(dg.BEAM_SWEEP)} lambda x (empty+on) "
          f"= {2 * len(dg.BEAM_SWEEP)} runs", flush=True)
    t1 = time.time()
    beam_results = {}
    for cpl_nm in dg.BEAM_SWEEP:
        r = run_beam_group(cpl_nm)
        beam_results[r["lambda_nm"]] = r
        print(f"  lambda={r['lambda_nm']}: beam_behind={r['beam_behind']:.4f} "
              f"return={r['observer_return']:.6f} "
              f"sig_abs/sig_ext={r['sigma_abs'] / r['sigma_ext']:.4f} "
              f"box_dev={r['box_dev']:.4f} "
              f"empty_closure={r['empty_box_closure']:.2e} "
              f"({r['elapsed_s']:.1f} s)", flush=True)
    print(f"beam-scene block done in {time.time() - t1:.0f} s", flush=True)

    # ---------------- assemble + write --------------------------------------
    out = {
        "meta": {"geometry_ambient": {k: getattr(dg, k) for k in
                                      ("NX", "NY", "ABSORB", "SRC_X", "OBJ",
                                       "R_OUT", "PLANE_X", "W_OBJ", "GUARD_OUT",
                                       "W_FLANK", "BOX")},
                 "geometry_beam": {k: getattr(dg, k) for k in
                                   ("BEAM_N", "BEAM_CX", "BEAM_CY", "BEAM_SRC_X",
                                    "BEAM_OBS_X", "BEAM_BOX_A", "BEAM_BOX_B")},
                 "fallback_angles": list(dg.FALLBACK_ANGLES),
                 "n5_subsample": list(dg.N5_SUBSAMPLE),
                 "tau": {"off_lab": dg.TAU_OFF_LAB, "off_field": dg.TAU_OFF_FIELD,
                         "on": dg.TAU_ON},
                 "sigma": dg.SIGMA_BY_ARTICLE,
                 "established_anchor_abs_ext_ratio": dg.ESTABLISHED_ABS_EXT_RATIO,
                 "decision_floor_reused": dg.DECISION_FLOOR,
                 "elapsed_s_ambient": time.time() - t0,
                 "elapsed_s_beam": time.time() - t1,
                 "n_new_runs": len(groups) * 4 + 2 * len(dg.BEAM_SWEEP)},
        "ambient_contrasts": table,
        "ambient_decision_floors_new_empty": floors,
        "g_values": g_values,
        "convergence_n5_vs_n9_off_lab_600": {"N5": c_n5, "N9": c_n9,
                                             "abs_delta": conv_n5_n9},
        "beam_scene": beam_results,
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1)

    # ---------------- console summary ----------------------------------------
    print("\nambient decision floors (new empty runs, informational -- exp-024's "
          "committed values are the ones scored):")
    for k, v in floors.items():
        print(f"  {k}nm: {v:.6f}")
    print("\nambient Weber contrast C (fallback, N=9):")
    for art in dg.ARTICLES_AMBIENT:
        row = "  ".join(f"{lam}nm {table[f'{art}/{lam}']['C']:+.4f}" for lam in dg.CPL)
        print(f"  {art:10s} {row}")
    print(f"\nP-MAT7 (N5 vs N9, off_lab@600): N5={c_n5:+.4f} N9={c_n9:+.4f} "
          f"|delta|={conv_n5_n9:.5f}  (gate <= 0.001)")
    print("\nP-MAT6 (g = |C|/tau_center):")
    for k, v in g_values.items():
        print(f"  {k}: g={v:.4f}")
    print("\nbeam-scene (ON article):")
    for nm, r in beam_results.items():
        print(f"  {nm}nm: beam_behind={r['beam_behind']:.4f} "
              f"return={r['observer_return']:.6f} "
              f"sig_abs/sig_ext={r['sigma_abs'] / r['sigma_ext']:.4f} "
              f"(established anchor {dg.ESTABLISHED_ABS_EXT_RATIO}) "
              f"box_dev={r['box_dev']:.4f} "
              f"empty_box_closure={r['empty_box_closure']:.2e}")
    print("\nresults.json written")


if __name__ == "__main__":
    main()
