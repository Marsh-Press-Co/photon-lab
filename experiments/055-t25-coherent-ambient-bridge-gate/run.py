"""exp-055 — The T25 Coherent-vs-Incoherent Ambient-Sum Bridge Gate (N=9
equal-amplitude): measurement harness.
============================================================================
Panel Iteration 32 (lead: QUANTUM OPTICS). Predictions committed in
NOTES.md BEFORE this file's first run (house discipline). Geometry from
design_geometry.py (exp-024's own r=78 fallback geometry, reused verbatim
— see that file's own header for why, not exp-030's `GEOM[78]`).

20 new FDTD calls at r=78: 9(empty)+9(absorber) individual single-source
legs + empty_joint + absorber_joint (9 simultaneous sources each).
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
from lab import Sim, materials, ambient as amb, sections as sc


def build_absorber(sim):
    materials.pec_disk(sim, dg.OBJ[0], dg.OBJ[1], dg.R_IN)
    materials.graded_black_shell(sim, dg.OBJ[0], dg.OBJ[1], dg.R_IN, dg.R_OUT,
                                  sigma_max=dg.SIGMA_MAX, eps_max=dg.EPS_MAX)


def run_one(article, sources):
    """article: 'empty' or 'absorber'. sources: list of (angle_deg, amp)."""
    sim = Sim(dg.NX, dg.NY, cells_per_lambda=dg.CPL, courant_frac=dg.COURANT_FRAC,
              absorb=dg.ABSORB)
    if article == "absorber":
        build_absorber(sim)
    for ang, amp in sources:
        sim.add_line_source(dg.SRC_X, angle_deg=ang, edge=dg.TAPER, amplitude=amp)
    sim.run(dg.STEPS)
    return sim, sc.full_capture(sim)


def profile_of(cap):
    ph = sc.phasors(cap)
    return amb.observer_profile(ph, dg.PLANE_X, dg.ABSORB, dg.NY - dg.ABSORB)


def main():
    t0 = time.time()
    n_calls = 0

    # ---------------------------------------------------- individual legs
    individual = {"empty": {}, "absorber": {}}
    for article in ("empty", "absorber"):
        for ang in dg.FALLBACK_ANGLES:
            _, cap = run_one(article, [(float(ang), 1.0)])
            n_calls += 1
            individual[article][ang] = profile_of(cap).tolist()
            print(f"  [{n_calls:2d}/20] individual {article} theta={ang:+05.1f}", flush=True)

    empty_profiles = [np.array(individual["empty"][a]) for a in dg.FALLBACK_ANGLES]
    absorber_profiles = [np.array(individual["absorber"][a]) for a in dg.FALLBACK_ANGLES]
    weights = [1.0] * len(dg.FALLBACK_ANGLES)

    naive = amb.contrast_from_runs(
        absorber_profiles, empty_profiles, weights,
        dg.ABSORB, dg.OBJ[1], dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)

    # ------------------------------------------------------------- joint
    sources_j = [(float(a), 1.0) for a in dg.FALLBACK_ANGLES]
    _, cap_empty_j = run_one("empty", sources_j)
    n_calls += 1
    print(f"  [{n_calls:2d}/20] joint empty (N=9)", flush=True)
    _, cap_absorber_j = run_one("absorber", sources_j)
    n_calls += 1
    print(f"  [{n_calls:2d}/20] joint absorber (N=9)", flush=True)

    b_empty_j = profile_of(cap_empty_j)
    b_absorber_j = profile_of(cap_absorber_j)

    eo_j, ef_j = amb.window_means(b_empty_j, dg.ABSORB, dg.OBJ[1], dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)
    so_j_raw, sf_j_raw = amb.window_means(b_absorber_j, dg.ABSORB, dg.OBJ[1], dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)

    # Weber contrast is scale-invariant (weber(a/k,b/k) == weber(a,b) for any
    # k != 0), so C_joint needs no explicit normalization step. For the raw-
    # flux deviation metric (P-055-1), which is NOT scale-invariant, both
    # legs are placed on the same footing as the naive pipeline's own scale
    # (each profile normalized by the MATCHING joint-empty-scene flank mean —
    # the direct N=9 analogue of `incoherent_sum`'s own per-component,
    # own-empty-flank normalization).
    b_obj_joint_normalized = so_j_raw / ef_j
    C_joint = amb.weber(so_j_raw, sf_j_raw)
    C_empty_joint = amb.weber(eo_j, ef_j)

    # -------------------------------------------------------------- output
    results = {
        "meta": {
            "experiment": "exp-055",
            "panel_iteration": 32,
            "lead": "QUANTUM OPTICS",
            "t1_escape_route": "NONE (instrument work)",
            "geometry": "exp-024's own r=78 fallback geometry (NY=1584, OBJ=(170,792)), "
                        "not exp-030's GEOM[78] — see design_geometry.py header",
            "n_fdtd_calls": n_calls,
            "elapsed_s": time.time() - t0,
        },
        "naive_incoherent": {
            "C": naive["C"], "C_empty": naive["C_empty"],
            "b_obj": naive["b_obj"], "b_flank": naive["b_flank"],
        },
        "joint_coherent": {
            "C_joint": C_joint, "C_empty_joint": C_empty_joint,
            "b_obj_joint_raw": so_j_raw, "b_flank_joint_raw": sf_j_raw,
            "b_obj_joint_normalized": b_obj_joint_normalized,
            "empty_joint_flank_raw": ef_j, "empty_joint_obj_raw": eo_j,
        },
        "established_anchor": {
            "C78_absorber_600_established": dg.C78_ABSORBER_600_ESTABLISHED,
        },
    }

    # ------------------------------------------------------- P-055 scoring
    p055 = {}
    p055["P-055-6_reproduction"] = {
        "naive_C": naive["C"],
        "established": dg.C78_ABSORBER_600_ESTABLISHED,
        "rel_dev": abs(naive["C"] - dg.C78_ABSORBER_600_ESTABLISHED)
                   / abs(dg.C78_ABSORBER_600_ESTABLISHED),
    }
    p055["P-055-1_raw_flux_deviation"] = {
        "b_obj_naive": naive["b_obj"],
        "b_obj_joint_normalized": b_obj_joint_normalized,
        "rel_dev": (b_obj_joint_normalized - naive["b_obj"]) / naive["b_obj"],
    }
    p055["P-055-2_weber_C_deviation"] = {
        "C_naive": naive["C"], "C_joint": C_joint,
        "abs_dev": abs(C_joint - naive["C"]),
    }
    p055["P-055-4_empty_scene_identity"] = {
        "C_empty_naive": naive["C_empty"], "C_empty_joint": C_empty_joint,
        "abs_dev": abs(C_empty_joint - naive["C_empty"]),
    }
    results["p055_scoring"] = p055

    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\ndone in {time.time() - t0:.0f} s, {n_calls} FDTD calls, "
          f"results -> {out_path}")
    print(f"P-055-6 (reproduction): naive_C={naive['C']:.6f} vs established "
          f"{dg.C78_ABSORBER_600_ESTABLISHED:.6f} "
          f"(rel_dev={p055['P-055-6_reproduction']['rel_dev']:.4%})")
    print(f"P-055-1 (raw flux dev): {p055['P-055-1_raw_flux_deviation']['rel_dev']:+.4%}")
    print(f"P-055-2 (Weber C dev): C_naive={naive['C']:.6f} C_joint={C_joint:.6f} "
          f"|dC|={p055['P-055-2_weber_C_deviation']['abs_dev']:.6f}")
    print(f"P-055-4 (empty identity): C_empty_naive={naive['C_empty']:.6f} "
          f"C_empty_joint={C_empty_joint:.6f} "
          f"|dC|={p055['P-055-4_empty_scene_identity']['abs_dev']:.6f}")


if __name__ == "__main__":
    main()
