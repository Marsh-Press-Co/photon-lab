"""exp-101 -- Closed-Box (4-Face Poynting) Reconstruction of Constraint-1's
`beam_behind_t28`. Panel Iteration 78. Lead seat (rotation): VISION SCIENCE.
Tier-0 mandate ONLY (Red Team's Phase-5 final audit, exp-100, "Reconciled
Iteration-78 queue"): Tiers 1-3 explicitly out of scope this cycle.

Frozen spec: NOTES.md (Predictions committed to git strictly BEFORE this
file's first run, house discipline). Change rationale: phase2_redteam_
audit.md (7 numbered attacks, 6 mandatory fixes, all adopted, 0 overridden
-- see NOTES.md's own "Changes from Phase 1" section).

WHAT THIS FIXES: exp-100's `beam_behind_t28` measured net -x flux through a
FIXED [obj_y-160,obj_y+160] line window at a plane 10 cells past the
object's far side -- at this cycle's oblique angles (37-43 deg) the
object's own shadow walks 125.7-154.6 cells laterally between the object
and that plane (79-97% of the window's own half-width), diluting the
reading to an uninterpretable 0.42-0.46. THE FIX: `lab/sections.py::
widths()` (trust-suite stage 8, already gated) sums flux over the FULL
four-face box perimeter -- no lateral-centering assumption at all, so it
cannot miss the shadow regardless of which way it walks. `beam_behind_t28`
is REPLACED (zero lab/ diff; the fix lives entirely in this file) by
`sigma_scat_downstream = back_frac * sigma_scat`, computed on the
already-gated BOX_A (`box_for_r4`/`ref_for_r4`, exp-094) -- reusing this
bench's own established low-x="downstream" convention
(`plane_x_behind`/`observer_record_t28`, exp-100), independently
re-derived from `_face_flux`'s raw Sx sign convention this cycle (Phase-2
EM critique + Red Team audit attack #1), NOT by analogy to
`widths_direction_corrected` (whose citation as precedent was FALSE --
that function never touches `back_frac`/`fwd_frac` at all; Phase-3 fix 2).

`cell_metrics_r4`/`pair_metrics_full`/`netd_row`/`observer_record_t28`
(constraint-2, constraint-3-sidecar, delta_scene/frac_contrast channel)
are reused COMPLETELY UNMODIFIED -- none of that is broken; only
`beam_behind_t28` was. 24 real `sim.run()` calls (6 corrected angles x 2
configs x 2 conditions), same budget as exp-100's own Leg B.
"""

import importlib.util
import json
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    """House `_load()` pattern (exp-078..100's own idiom for cross-
    experiment-directory imports). Per exp-100's own documented Phase-4
    hazard (a `PicklingError` from two independent `_load()` chains of the
    same underlying file clobbering one `sys.modules` registration), this
    file loads exp-100's own chain EXACTLY ONCE and takes every downstream
    name (exp099/exp098/exp095/exp094/dg/run_block_r4/PAIR_KEYS_R4/etc.)
    from THAT single instance -- never a second, independent `_load()` of
    any file already reachable through it."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP100_DIR = os.path.join(ROOT, "experiments", "100-t28-delta-scene-constraint-scoring-pass")
exp100 = _load(os.path.join(EXP100_DIR, "run.py"), "_exp101_exp100")

# -- everything below is exp-100's OWN single instance, not a fresh load --
exp098 = exp100.exp098
exp095 = exp100.exp095
dg = exp100.dg
registration_preflight = exp100.registration_preflight
run_block_r4 = exp100.run_block_r4
cell_metrics_r4 = exp095.cell_metrics_r4
pair_metrics_full = exp095.pair_metrics_full
netd_row = exp095.netd_row
NETD_ROW_KEYS = exp100.NETD_ROW_KEYS
PAIR_KEYS_R4 = exp100.PAIR_KEYS_R4
SIGMA_R4_CORRECTED = exp100.SIGMA_R4_CORRECTED
XI_TOL = exp100.XI_TOL
compute_floor = exp100.compute_floor
box_for_r4 = exp095.box_for_r4          # == exp094.box_for_r4, chained
ref_for_r4 = exp095.ref_for_r4
widths_direction_corrected = exp095.widths_direction_corrected
BOX_CLEARANCE_A_R4 = exp095.BOX_CLEARANCE_A_R4
BOX_CLEARANCE_B_R4 = exp095.BOX_CLEARANCE_B_R4
observer_record_t28 = exp100.observer_record_t28   # UNCHANGED -- constraint 2, already passed cleanly
plane_x_obs = exp100.plane_x_obs
_fresh_sim_scaffold = exp100._fresh_sim_scaffold
pool_rows = exp100.pool_rows

assert abs(SIGMA_R4_CORRECTED - 0.25) < 1e-12
assert PAIR_KEYS_R4 == ("C40_R4", "G40_R4")
assert abs(XI_TOL - 0.12) < 1e-12

# ================================================================ corrected LEG_B_ANGLES (Phase-1 sec 2.3, Red Team attack #3 disclosure)
THETA0_A, THETA0_38590, THETA0_B, THETA0_C = exp100.THETA0_A, exp100.THETA0_38590, exp100.THETA0_B, exp100.THETA0_C
POOL_LARGEST_1 = 39.200000     # exp-095, R4 family -- pool-wide largest |delta_scene|, re-verified this cycle
POOL_LARGEST_2 = 42.960901     # exp-099, R4 family -- pool-wide 2nd-largest (unchanged from exp-100's own pick)
LEG_B_ANGLES = sorted([THETA0_A, THETA0_38590, THETA0_B, THETA0_C, POOL_LARGEST_1, POOL_LARGEST_2])
assert len(LEG_B_ANGLES) == 6 and len(set(LEG_B_ANGLES)) == 6, LEG_B_ANGLES

FLOOR, _FLOOR_RMS, _FLOOR_N, _ = compute_floor()

# ================================================================ Fix 4 (R17): per-config BOX_CROSS clearance
# C40_R4's own domain (nx=720, pad=0) leaves only 104 cells between obj_x
# and the absorb-boundary interior edge at BOX_CLEARANCE_A_R4=24 clearance
# (margin_left=80). The UNIFORM BOX_CLEARANCE_B_R4=48 exp-100's own
# cell_metrics_r4 already uses for its established xi_ext/box_dev/thermo
# channel (UNCHANGED here) gives C40_R4 only a 56-cell margin -- below
# exp-003's own established >=60-cell threshold (ABSORB=40 there; this
# bench's ABSORB=80 makes 60 cells a floor, not a target -- Red Team attack
# #5). For THIS CYCLE'S OWN NEW due-diligence check on `sigma_scat_
# downstream` only (never for the existing thermo/xi_ext/box_dev channel,
# which is out of scope and unmodified), use a smaller, per-config-safe
# clearance for C40_R4: clearance=14 -> margin_left=90 cells (verified
# below by direct computation, not by re-deriving the formula by hand).
BOX_CROSS_CLEARANCE = {"C40_R4": 14, "G40_R4": BOX_CLEARANCE_B_R4}


def _verify_box_margins():
    """Recompute every box's absorb-boundary margin directly from the real
    Sim geometry (never hand-derived) -- both the unmodified BOX_A/BOX_B
    pair (cell_metrics_r4's own channel, untouched) and this cycle's new
    BOX_CROSS pair, for both configs. HALTs before any FDTD call if any
    margin used by THIS cycle's own new check falls below 90 cells (Fix 4's
    own bar) -- a pre-registered gate, not a post-hoc reassurance."""
    report = {}
    for key in PAIR_KEYS_R4:
        cfg = dg.R4_CONFIGS[key]
        box_a = box_for_r4(cfg, BOX_CLEARANCE_A_R4)
        box_cross = box_for_r4(cfg, BOX_CROSS_CLEARANCE[key])
        margin_a = box_a[0] - cfg["absorb"]
        margin_cross = box_cross[0] - cfg["absorb"]
        margin_a_right = cfg["nx"] - cfg["absorb"] - box_a[1]
        margin_cross_right = cfg["nx"] - cfg["absorb"] - box_cross[1]
        report[key] = dict(box_a=box_a, box_cross=box_cross,
                            margin_a_left=margin_a, margin_cross_left=margin_cross,
                            margin_a_right=margin_a_right, margin_cross_right=margin_cross_right)
        assert margin_a >= 60, f"{key}: BOX_A margin {margin_a} < exp-003 established floor 60"
        assert margin_cross >= 90, f"{key}: BOX_CROSS margin {margin_cross} < Fix-4 bar 90"
        assert margin_a_right >= 60 and margin_cross_right >= 90, f"{key}: right-side margin gate failed: {report[key]}"
    return report


BOX_MARGIN_REPORT = _verify_box_margins()

# ================================================================ Fix 1 (R13): p_scat noise/amplitude floor gate
# House-style constant (exp-088's own R13-founding FLOOR_FRAC=0.10,
# reused for the SAME kind of amplitude-normalized-magnitude floor,
# applied here to a different quantity -- sigma_scat has no larger
# established cross-cycle dataset to draw a floor from yet, since this is
# this bench's first use of `back_frac`/`fwd_frac` on the R4 family, so
# the floor is drawn from THIS cycle's own 12-cell dataset -- disclosed as
# an idealization in NOTES.md, not claimed as an externally-anchored bound
# the way exp-088's own FLOOR was).
FLOOR_FRAC_SCAT = 0.10


def sigma_scat_partition(cap_empty, cap_article, cfg, key):
    """THE FIX: closed-box reconstruction of constraint 1, replacing
    `beam_behind_t28`. Returns the primary (BOX_A) reading and the
    per-config BOX_CROSS independence check -- zero new `sim.run()` calls,
    both derived from the SAME already-captured field arrays `cell_metrics_
    r4` uses for its own (unmodified) BOX_A/BOX_B pair."""
    ref = ref_for_r4(cfg)
    box_a = box_for_r4(cfg, BOX_CLEARANCE_A_R4)
    box_cross = box_for_r4(cfg, BOX_CROSS_CLEARANCE[key])

    w_a = widths_direction_corrected(cap_article, cap_empty, box_a, ref)
    w_x = widths_direction_corrected(cap_article, cap_empty, box_cross, ref)

    # Sourced from `_face_flux`'s raw Sx convention, independently re-derived
    # (Phase-2 EM critique + Red Team audit attack #1) -- NOT by analogy to
    # `widths_direction_corrected` (which never touches back_frac/fwd_frac):
    # this bench's own `plane_x_behind()` (exp-100) already calls the box's
    # low-x face "downstream" for this geometry (src_x>obj_x>plane_x); that
    # is exactly the face `_face_flux`'s `p_back` (hence `back_frac`) reads.
    scat_downstream_a = w_a["back_frac"] * w_a["sigma_scat"]
    scat_downstream_x = w_x["back_frac"] * w_x["sigma_scat"]
    scat_sourceward_a = w_a["fwd_frac"] * w_a["sigma_scat"]

    box_dev_scat_downstream = (abs(scat_downstream_a - scat_downstream_x) / abs(scat_downstream_a)
                                if scat_downstream_a != 0 else float("inf"))

    return dict(
        sigma_scat=w_a["sigma_scat"], sigma_abs=w_a["sigma_abs"], sigma_ext=w_a["sigma_ext"],
        sigma_ext_cross=w_a["sigma_ext_cross"],
        xi_ext=abs(w_a["sigma_ext_cross"] - w_a["sigma_ext"]) / abs(w_a["sigma_ext"]),
        back_frac=w_a["back_frac"], fwd_frac=w_a["fwd_frac"],
        sigma_scat_downstream=scat_downstream_a, sigma_scat_sourceward=scat_sourceward_a,
        box_dev_scat_downstream=box_dev_scat_downstream,
        sigma_scat_downstream_cross=scat_downstream_x,
    )


def run_leg_b_fixed():
    preflight = registration_preflight(LEG_B_ANGLES, config_keys=PAIR_KEYS_R4)
    assert preflight["all_clean"], f"REGISTRATION GATE FAILED for {LEG_B_ANGLES}: HALT"

    jobs = []
    for th in LEG_B_ANGLES:
        for key in PAIR_KEYS_R4:
            jobs.append((key, th, False, dg.R4_STEPS, None))
            jobs.append((key, th, True, dg.R4_STEPS, SIGMA_R4_CORRECTED))
    assert len(jobs) == 24, f"R19 call-count assert: expected 24 jobs, got {len(jobs)}"
    t0 = time.time()
    captures, wall = run_block_r4(jobs)
    assert len(captures) == 24, f"R19: expected 24 captures, got {len(captures)}"

    scaffolds = {key: _fresh_sim_scaffold(dg.R4_CONFIGS[key]) for key in PAIR_KEYS_R4}

    xi_pass, nonneg_pass = True, True
    cells = {}
    partitions = {}
    for th in LEG_B_ANGLES:
        for key in PAIR_KEYS_R4:
            cap_empty = captures[(key, th, False, dg.R4_STEPS)]
            cap_article = captures[(key, th, True, dg.R4_STEPS)]
            cell = cell_metrics_r4(key, th, dg.R4_STEPS, cap_empty, cap_article)   # UNCHANGED, existing channel
            cells[(key, th)] = cell
            for xi in cell["xi_ext"].values():
                if xi > XI_TOL:
                    xi_pass = False
            if not cell["sigma_abs_nonneg"]:
                nonneg_pass = False

            cfg = dg.R4_CONFIGS[key]
            part = sigma_scat_partition(cap_empty, cap_article, cfg, key)
            if part["xi_ext"] > XI_TOL:
                xi_pass = False
            partitions[(key, th)] = part
    assert xi_pass, "xi_ext gate FAILED -- extinction-routes disagreement; HALT"
    assert nonneg_pass, "sigma_abs>=0 gate FAILED; HALT"

    # Fix 1 (R13): pool this cycle's own 12 sigma_scat readings (BOX_A) into
    # a self-referential amplitude floor -- disclosed idealization, this
    # bench's first use of back_frac/fwd_frac on the R4 family means no
    # larger established cross-cycle dataset exists yet to draw one from.
    all_sigma_scat = [partitions[(key, th)]["sigma_scat"] for th in LEG_B_ANGLES for key in PAIR_KEYS_R4]
    floor_scat_rms = float(np.sqrt(np.mean(np.square(all_sigma_scat))))
    floor_scat = FLOOR_FRAC_SCAT * floor_scat_rms

    report = {}
    empty_self_ratios = {}
    for th in LEG_B_ANGLES:
        c_cell = cells[("C40_R4", th)]
        g_cell = cells[("G40_R4", th)]
        pm = pair_metrics_full(c_cell, g_cell, floor=FLOOR)
        nrow = netd_row(pm)   # Fix 3 (R21): persisted here, narrated in NOTES.md Result -- see NOTES.md
        assert set(nrow.keys()) >= NETD_ROW_KEYS, (
            f"MANDATORY netd_row() COVERAGE ASSERT FAILED at theta={th} -- "
            f"missing keys; HALT before results.json")

        row = dict(delta_scene=pm["delta_scene"], frac_contrast=pm["frac_contrast"],
                   ratio_k=pm["ratio_k"], floor_pass=pm["floor_pass"], **nrow)

        for key in PAIR_KEYS_R4:
            cfg = dg.R4_CONFIGS[key]
            cap_empty = captures[(key, th, False, dg.R4_STEPS)]
            cap_article = captures[(key, th, True, dg.R4_STEPS)]
            part = partitions[(key, th)]

            # Fix 1 (R13): floor-gate -- a cell whose |sigma_scat| does not
            # clear the amplitude floor is reported UNRESOLVED-BY-
            # CONSTRUCTION, never silently scored in Predictions #2/#3.
            scat_floor_pass = bool(abs(part["sigma_scat"]) >= floor_scat)
            outcome = "resolved" if scat_floor_pass else "UNRESOLVED-BY-CONSTRUCTION"

            obs_empty = observer_record_t28(scaffolds[key], cap_empty, cfg)
            obs_article = observer_record_t28(scaffolds[key], cap_article, cfg)
            self_ratio = (obs_empty["p_observer_raw"] / obs_empty["p_incident_raw"]
                          if obs_empty["p_incident_raw"] != 0 else float("inf"))
            empty_self_ratios[(key, th)] = self_ratio

            prefix = f"partition_{key}"
            row[f"{prefix}_sigma_abs"] = part["sigma_abs"]
            row[f"{prefix}_sigma_scat"] = part["sigma_scat"]
            row[f"{prefix}_sigma_ext"] = part["sigma_ext"]
            row[f"{prefix}_sigma_ext_cross"] = part["sigma_ext_cross"]
            row[f"{prefix}_xi_ext"] = part["xi_ext"]
            row[f"{prefix}_sigma_scat_downstream"] = part["sigma_scat_downstream"]
            row[f"{prefix}_sigma_scat_sourceward"] = part["sigma_scat_sourceward"]
            row[f"{prefix}_box_dev_scat_downstream"] = part["box_dev_scat_downstream"]
            row[f"{prefix}_scat_floor_pass"] = scat_floor_pass
            row[f"{prefix}_outcome"] = outcome
            row[f"{prefix}_observer_empty_self_ratio"] = self_ratio
            row[f"{prefix}_observer_article_norm"] = (
                obs_article["p_observer_raw"] / obs_empty["p_incident_raw"]
                if obs_empty["p_incident_raw"] != 0 else float("inf"))
            # Three-way energy-partition table (Phase-1 sec 2.5): absorbed /
            # observer-direction return / forward-continuing. NOT a claimed
            # exact algebraic sum (Idealization, Phase-1 sec 2.5) -- the
            # shortfall is lateral/diffuse exit through the box's y0/y1 faces.
            row[f"{prefix}_partition_absorbed"] = part["sigma_abs"]
            row[f"{prefix}_partition_observer_return"] = row[f"{prefix}_observer_article_norm"]
            row[f"{prefix}_partition_forward_continuing"] = (
                part["sigma_scat_downstream"] if scat_floor_pass else None)
        report[th] = row

    validation_gate_pass = all(v < 0.02 for v in empty_self_ratios.values())

    return dict(preflight=preflight, report=report, wall_s=wall, n_calls=len(jobs),
                xi_pass=xi_pass, nonneg_pass=nonneg_pass,
                floor_scat=floor_scat, floor_scat_rms=floor_scat_rms,
                box_margin_report=BOX_MARGIN_REPORT,
                empty_self_ratios={f"{k[0]}@{k[1]}": v for k, v in empty_self_ratios.items()},
                validation_gate_pass=bool(validation_gate_pass))


# ================================================================ main
def main():
    print("=" * 78)
    print("exp-101 -- Closed-box (4-face Poynting) reconstruction of beam_behind_t28")
    print("=" * 78)
    t_start = time.time()

    print(f"\nCorrected LEG_B_ANGLES: {LEG_B_ANGLES}")
    print(f"BOX_MARGIN_REPORT: {json.dumps(BOX_MARGIN_REPORT, indent=2, default=str)}")

    print(f"\n-- Leg B (fixed): {len(LEG_B_ANGLES)} angles x 2 keys x 2 conditions = "
          f"{len(LEG_B_ANGLES) * 4} sim.run() calls --")
    leg_b = run_leg_b_fixed()
    print(f"  wall_s={leg_b['wall_s']:.1f}  n_calls={leg_b['n_calls']}  "
          f"xi_pass={leg_b['xi_pass']}  nonneg_pass={leg_b['nonneg_pass']}")
    print(f"  floor_scat={leg_b['floor_scat']:.6e} (10% of RMS over this cycle's own 12 cells)")
    print(f"  R18 validation gate (empty-scene observer self-ratio < 0.02): "
          f"{leg_b['validation_gate_pass']}")

    for th, row in sorted(leg_b["report"].items()):
        print(f"\n  theta={th:+.6f}  delta_scene={row['delta_scene']:+.6e}")
        for key in PAIR_KEYS_R4:
            p = f"partition_{key}"
            print(f"    [{key}] outcome={row[p+'_outcome']}  "
                  f"absorbed={row[p+'_partition_absorbed']:.6f}  "
                  f"observer_return={row[p+'_partition_observer_return']:.6e}  "
                  f"forward_continuing={row[p+'_partition_forward_continuing']}  "
                  f"box_dev_scat_downstream={row[p+'_box_dev_scat_downstream']:.4f}")

    n_unresolved = sum(1 for th in LEG_B_ANGLES for key in PAIR_KEYS_R4
                        if leg_b["report"][th][f"partition_{key}_outcome"] == "UNRESOLVED-BY-CONSTRUCTION")
    n_box_dev_fail = sum(1 for th in LEG_B_ANGLES for key in PAIR_KEYS_R4
                          if leg_b["report"][th][f"partition_{key}_box_dev_scat_downstream"] > XI_TOL)
    print(f"\n  n_cells=12  n_unresolved_by_construction={n_unresolved}  "
          f"n_box_dev_scat_downstream_fail(>{XI_TOL})={n_box_dev_fail}")

    result = dict(
        experiment="exp-101", panel_iteration=78,
        leg_b_angles=LEG_B_ANGLES,
        box_margin_report=BOX_MARGIN_REPORT,
        leg_b=leg_b,
        n_unresolved_by_construction=n_unresolved,
        n_box_dev_scat_downstream_fail=n_box_dev_fail,
        total_wall_s=time.time() - t_start,
    )
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(result, f, indent=2, default=str)
    print(f"\nTotal wall time: {result['total_wall_s']:.1f}s. results.json written.")
    return result


if __name__ == "__main__":
    main()
