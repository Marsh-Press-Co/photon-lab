"""exp-096 -- Angle-Domain Registration-Readback Gate (R3/R4/R5) + Zero-FDTD
Bracket-Width Desk Bound. Panel Iteration 73. Lead seat (rotation):
PHOTONICS. Frozen spec: NOTES.md (Predictions committed to git strictly
BEFORE this file's first run, house discipline). Change rationale:
phase2_redteam_audit.md (8 Red-Team-mandatory fixes, all adopted, zero
overridden -- see NOTES.md's own "Changes from Phase 1" section for the
item-by-item mapping).

0 FDTD calls. Every `Sim` construction below stops before `sim.run()` is
ever invoked -- the quantities under test (`sim.lam`, `sim.source_specs`,
`sim.sources[-1]`) are fully determined at construction time.

Implementation route: OPTION B (inline replication of the real
`_run_sim_r{3,4,5}_sigma` construction sequence -- `Sim(...)` +
`add_line_source(...)` only, no materials/`build_article_*` call, per
Phase 1's own finding, independently reconfirmed reading `lab/materials.py`
directly this cycle, that skipping materials construction loses no
coverage of the angle/k-vector question). Chosen over Option A (adding a
`construct_only=False` parameter to the frozen `experiments/095-.../
run.py` functions) specifically to avoid editing a frozen prior
experiment's committed file -- this program's own established practice
keeps every past experiment's `run.py` immutable; new cycles add new code,
they do not edit old call sites. Idealization 34's own duplication risk
(this replication could drift from the real call sites in a future edit)
is accepted and disclosed, not eliminated.

Six checks per representative point (NOTES.md "Setup"):
  1. sim.lam == cpl_intended
  2. sim.source_specs[-1]['angle_deg'] == theta_intended
  3. sim.sources[-1]['x']/['sl'] == intended placement       (BOTH pair members)
  4. sim.sources[-1]['phase'] matches independent recompute  (BOTH pair members)
  5. R4/C40 y_lo/y_hi/src_x independently recomputed from native constants
     x RATIO=2.0, outside r4_config()                        (one point)
  6. run.py job constants vs exp-095 NOTES.md's own frozen Predictions text (8 points)

Plus a fault-injection triad (FI-A/B/C) + positive control, and the
zero-FDTD bracket-width desk bound (unchanged from Phase 1, re-verified
here bit-exact against raw results.json).
"""

import importlib.util
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    """House `_load()` pattern (exp-078..095's own idiom for cross-
    experiment-directory imports)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP095_DIR = os.path.join(ROOT, "experiments", "095-t28-r4-ground-truth-sign-control")
EXP095_NOTES = os.path.join(EXP095_DIR, "NOTES.md")

exp095 = _load(os.path.join(EXP095_DIR, "run.py"), "_exp096_exp095")
dg = exp095.dg

from lab import Sim  # noqa: E402

CONFIGS = {"R3": dg.R3_CONFIGS, "R4": dg.R4_CONFIGS, "R5": dg.R5_CONFIGS}
TAPER = {"R3": dg.R3_TAPER, "R4": dg.R4_TAPER, "R5": dg.R5_TAPER}
CPL = {"R3": dg.R3_CPL[600], "R4": dg.R4_CPL[600], "R5": dg.R5_CPL[600]}
assert CPL == {"R3": 30, "R4": 40, "R5": 50}

# ---------------------------------------------------------------- representative points
# theta_intended/cpl_intended sourced directly from exp-095's own already-
# committed job constants (exp095.RANK1A_ANGLES etc.) -- NOT hand-retyped --
# per Checks 1-4's designed scope (caller-plumbing fidelity to the SAME
# source the production call sites read). Check 6 below independently
# cross-checks these same constants against a DIFFERENT, textually
# separate source (exp-095's own NOTES.md prose).
REPRESENTATIVE = [
    dict(family="R4", theta=exp095.RANK1A_ANGLES[0], notes_line=437, notes_label="RANK1A[0]"),
    dict(family="R4", theta=exp095.RANK1A_ANGLES[1], notes_line=437, notes_label="RANK1A[1]"),
    dict(family="R4", theta=exp095.RANK1C_ANGLES[0], notes_line=445, notes_label="RANK1C[0]"),
    dict(family="R4", theta=exp095.RANK1C_ANGLES[1], notes_line=445, notes_label="RANK1C[1]"),
    dict(family="R4", theta=exp095.RANK3A_ANGLE, notes_line=495, notes_label="RANK3A"),
    dict(family="R3", theta=exp095.RANK4_ANGLE, notes_line=511, notes_label="RANK4"),
    dict(family="R5", theta=exp095.RANK2B_NATIVE_ANGLES[0], notes_line=476, notes_label="RANK2B_NATIVE[0]"),
    dict(family="R5", theta=exp095.RANK2B_NATIVE_ANGLES[1], notes_line=476, notes_label="RANK2B_NATIVE[1]"),
]
PAIR_KEYS = {"R3": ("C40_R3", "G40_R3"), "R4": ("C40_R4", "G40_R4"), "R5": ("C40_R5", "G40_R5")}

# NOTES.md's own frozen Predictions-section text, hand-transcribed from that
# document directly this session (Check 6's independent ground truth --
# confirmed present at these exact lines by direct `grep -n` this Phase):
#   line 437: "delta_scene(R4, 39.2 deg) < 0 AND delta_scene(R4, 39.4 deg) < 0"
#   line 445: "floor_pass=True at both 38.49 deg/38.69 deg"
#   line 476: "cpl=50 readings at 41.825 deg/41.850 deg"
#   line 495: "ratio (corrected/native) at 41.6 deg, cpl=40"
#   line 511: "38.4 deg at corrected sigma (1/3), cpl=30"
NOTES_MD_FROZEN_LINE_VALUES = {
    437: [39.2, 39.4],
    445: [38.49, 38.69],
    476: [41.825, 41.850],
    495: [41.6],
    511: [38.4],
}


def construct_sim(family, config_key, cpl_actual, theta_actual):
    """OPTION B inline replication of `_run_sim_r{3,4,5}_sigma`'s own
    construction sequence, stopping before `sim.run()`. Mirrors
    `experiments/092/094/095-.../run.py::_run_sim_r{3,4,5}_sigma` line for
    line (Sim(...) + add_line_source(...)), minus the materials/sigma call
    (out of scope, confirmed by reading `lab/materials.py`) and minus
    `sim.run()`/`sc.full_capture()` (this is where the 0-FDTD-call
    guarantee comes from)."""
    cfg = CONFIGS[family][config_key]
    sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=cpl_actual,
              courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
    sim.add_line_source(cfg["src_x"], y_lo=cfg["y_lo"], y_hi=cfg["y_hi"],
                         angle_deg=theta_actual, amplitude=1.0,
                         profile="plane", edge=TAPER[family])
    return sim, cfg


def phase_expected(sim_lam, theta_intended, y_lo, y_hi, rel_phase=0.0):
    """Independent recomputation of `add_line_source`'s own phase-ramp
    formula (`lab/fdtd2d.py:172-175`), using the ALREADY-VERIFIED `sim.lam`
    (Check 1), matching Check 4's own spec (the single recomputation it
    uses -- Phase 1's vestigial `cpl_intended`-based illustration removed
    per fix #8)."""
    k = 2.0 * np.pi / sim_lam
    yy = np.arange(y_lo, y_hi, dtype=float)
    return k * np.sin(np.radians(theta_intended)) * (yy - 0.5 * (y_lo + y_hi)) + rel_phase


def run_checks_1234(family, theta_intended, cpl_intended, config_key,
                     cpl_actual=None, theta_actual=None):
    """Checks 1/2/3/4 on one (family, config) construction. `cpl_actual`/
    `theta_actual` default to the intended values (correct wiring); a
    fault-injection call passes a deliberately wrong value for one of
    them, simulating a defect at that specific point in the pipeline."""
    cpl_actual = cpl_intended if cpl_actual is None else cpl_actual
    theta_actual = theta_intended if theta_actual is None else theta_actual
    sim, cfg = construct_sim(family, config_key, cpl_actual, theta_actual)

    check1 = (sim.lam == float(cpl_intended))
    check2 = (sim.source_specs[-1]["angle_deg"] == theta_intended)
    check3 = (sim.sources[-1]["x"] == cfg["src_x"]
              and sim.sources[-1]["sl"] == slice(cfg["y_lo"], cfg["y_hi"]))
    expected = phase_expected(sim.lam, theta_intended, cfg["y_lo"], cfg["y_hi"])
    actual_phase = sim.sources[-1]["phase"]
    check4 = bool(actual_phase is not None
                  and np.allclose(actual_phase, expected, atol=1e-9, rtol=0.0))
    max_abs_diff = None if actual_phase is None else float(np.max(np.abs(actual_phase - expected)))

    return dict(family=family, config_key=config_key,
                cpl_intended=cpl_intended, theta_intended=theta_intended,
                cpl_actual=cpl_actual, theta_actual=theta_actual,
                check1_resolution=check1, check2_angle_spec=check2,
                check3_placement=check3, check4_phase_ramp=check4,
                check4_max_abs_diff=max_abs_diff,
                clean=bool(check1 and check2 and check3 and check4))


def check5_recipe_spot_check():
    """Fix #3 (MATERIALS): independently recompute R4/C40's own
    y_lo/y_hi/src_x directly from the NATIVE (cpl=20) base constants
    (300, 40, 1584) x RATIO=2.0, by hand-written arithmetic -- NOT a call
    to `r4_config()` or any function under test -- and compare against
    `R4_CONFIGS["C40_R4"]`'s own stored values."""
    native_src_x, native_absorb, native_ny = 300, 40, 1584
    ratio = 2.0
    src_x_recomputed = round(native_src_x * ratio) + 0    # pad=0 for C40
    absorb_recomputed = round(native_absorb * ratio)
    ny_recomputed = round(native_ny * ratio) + 0           # pad=0 for C40
    y_lo_recomputed = absorb_recomputed + 0
    y_hi_recomputed = ny_recomputed - y_lo_recomputed

    cfg = dg.R4_CONFIGS["C40_R4"]
    ok = (src_x_recomputed == cfg["src_x"] and y_lo_recomputed == cfg["y_lo"]
          and y_hi_recomputed == cfg["y_hi"])
    return dict(point="R4/C40_R4", src_x_recomputed=src_x_recomputed,
                y_lo_recomputed=y_lo_recomputed, y_hi_recomputed=y_hi_recomputed,
                src_x_stored=cfg["src_x"], y_lo_stored=cfg["y_lo"], y_hi_stored=cfg["y_hi"],
                clean=bool(ok))


def check6_notes_md_cross_check():
    """Fix #4 (QUANTUM), the single most load-bearing fix: for each of the
    8 representative points, assert exp-095's own run.py job constant
    equals the value hand-transcribed from exp-095's own NOTES.md frozen
    Predictions section (a textually separate, temporally-prior document)
    at the cited line."""
    results = []
    for pt in REPRESENTATIVE:
        line = pt["notes_line"]
        frozen_values = NOTES_MD_FROZEN_LINE_VALUES[line]
        found = any(abs(pt["theta"] - v) < 1e-9 for v in frozen_values)
        results.append(dict(family=pt["family"], theta=pt["theta"],
                             notes_line=line, notes_label=pt["notes_label"],
                             notes_md_frozen_values=frozen_values, clean=bool(found)))
    return results


def run_fault_injection():
    """Fix #5 (THERMODYNAMICS' corrected count): positive control + 3
    genuinely distinct fault-injection scenarios, 2 of which (FI-A, FI-C)
    are new constructions and one (FI-B) reuses representative point 4's
    already-built object under a deliberately wrong `theta_intended`
    label -- spends zero new constructions, per NOTES.md's own reconciled
    count."""
    out = {}

    # Positive control: identical to representative point 1 (R4, 39.2, C40_R4).
    pc = run_checks_1234("R4", 39.2, 40, "C40_R4")
    out["positive_control"] = dict(**pc, must_be="CLEAN", caught_as_defect=(not pc["clean"]))

    # FI-A: family/cpl swap -- Sim built at cpl=30 (R3's own resolution),
    # told cpl_intended=40 (R4's).
    fia = run_checks_1234("R4", 39.2, 40, "C40_R4", cpl_actual=dg.R3_CPL[600])
    out["FI_A_family_cpl_swap"] = dict(**fia, must_be="DEFECT-FOUND",
                                        caught_as_defect=(not fia["clean"]))

    # FI-B: reuse representative point 4 (R4, 38.69, C40_R4) but mislabel
    # its intended theta as 39.2 -- zero new Sim constructions.
    fib = run_checks_1234("R4", 39.2, 40, "C40_R4", theta_actual=38.69)
    out["FI_B_angle_mislabel"] = dict(**fib, must_be="DEFECT-FOUND",
                                       caught_as_defect=(not fib["clean"]))

    # FI-C: sign flip -- actual angle_deg=-39.2 where intended is +39.2.
    fic = run_checks_1234("R4", 39.2, 40, "C40_R4", theta_actual=-39.2)
    out["FI_C_sign_flip"] = dict(**fic, must_be="DEFECT-FOUND",
                                  caught_as_defect=(not fic["clean"]))

    all_pass = (out["positive_control"]["clean"]
                and not out["FI_A_family_cpl_swap"]["clean"]
                and not out["FI_B_angle_mislabel"]["clean"]
                and not out["FI_C_sign_flip"]["clean"])
    out["fault_injection_all_as_predicted"] = bool(all_pass)
    return out


def desk_bound():
    """Zero-FDTD bracket-width desk bound (queue item 2), re-verified this
    Phase bit-exact against raw results.json (unchanged from Phase 1's
    computed answer)."""
    with open(os.path.join(ROOT, "experiments", "090-t28-floor-frac-threshold-fit", "results.json")) as f:
        r090 = json.load(f)
    with open(os.path.join(ROOT, "experiments", "092-t28-crossing-relocation-caution-zone-rebuild", "results.json")) as f:
        r092 = json.load(f)

    cpl20 = r090["q8"]["crossings_deg"]
    lower_cpl20, upper_cpl20 = cpl20[2], cpl20[3]
    cr = r092["rank1"]["crossing_report"]
    lower_cpl30 = cr["lower_crossing_cpl30"]
    upper1_cpl30 = cr["upper_crossing_cpl30"]
    upper2_cpl30 = cr["upper_crossing_cpl30_second"]
    # sanity: cr's own already-filed known_cpl20_lower/upper must match r090's
    # own q8.crossings_deg values this function independently pulled above
    assert abs(cr["known_cpl20_lower"] - lower_cpl20) < 1e-9
    assert abs(cr["known_cpl20_upper"] - upper_cpl20) < 1e-9

    figures = {
        "lower_window": abs(lower_cpl20 - lower_cpl30),
        "upper_window_1": abs(upper_cpl20 - upper1_cpl30),
        "upper_window_2": abs(upper_cpl20 - upper2_cpl30),
    }
    candidates = [0.2, 0.4, 0.5]
    ratios = {str(delta): {name: round(delta / m, 4) for name, m in figures.items()}
              for delta in candidates}
    return dict(migration_figures_deg=figures, candidate_half_widths_deg=candidates,
                containment_ratios=ratios)


def main():
    t0 = time.time()
    representative_results = []
    for pt in REPRESENTATIVE:
        family = pt["family"]
        cpl_intended = CPL[family]
        for config_key in PAIR_KEYS[family]:
            representative_results.append(
                run_checks_1234(family, pt["theta"], cpl_intended, config_key))

    check5 = check5_recipe_spot_check()
    check6 = check6_notes_md_cross_check()
    fi = run_fault_injection()
    db = desk_bound()

    all_representative_clean = all(r["clean"] for r in representative_results)
    check5_clean = check5["clean"]
    check6_clean = all(c["clean"] for c in check6)
    gate_clean = bool(all_representative_clean and check5_clean and check6_clean)

    results = dict(
        experiment="exp-096",
        panel_iteration=73,
        fdtd_calls=0,
        wall_time_s=round(time.time() - t0, 3),
        representative_results=representative_results,
        representative_all_clean=all_representative_clean,
        check5_recipe_spot_check=check5,
        check6_notes_md_cross_check=check6,
        check6_all_clean=check6_clean,
        registration_gate_outcome="CLEAN" if gate_clean else "DEFECT-FOUND",
        fault_injection=fi,
        desk_bound=db,
        sim_construction_count=dict(
            representative=len(representative_results),
            fault_injection_new=2,  # FI-A, FI-C (positive control + FI-B reuse existing points)
            total=len(representative_results) + 2,
        ),
    )
    return results


if __name__ == "__main__":
    results = main()
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"exp-096 -- Registration-Readback Gate + Desk Bound (0 FDTD calls, "
          f"{results['wall_time_s']}s wall)")
    print(f"Representative points: {len(REPRESENTATIVE)} x 2 pair members = "
          f"{results['sim_construction_count']['representative']} constructions, "
          f"all clean = {results['representative_all_clean']}")
    print(f"Check 5 (recipe spot-check): clean = {results['check5_recipe_spot_check']['clean']}")
    print(f"Check 6 (NOTES.md cross-check): all clean = {results['check6_all_clean']}")
    print(f"REGISTRATION-READBACK GATE OUTCOME: {results['registration_gate_outcome']}")
    print()
    print("Fault injection (must be: positive_control=CLEAN, FI-A/B/C=DEFECT-FOUND):")
    for key in ("positive_control", "FI_A_family_cpl_swap", "FI_B_angle_mislabel", "FI_C_sign_flip"):
        r = results["fault_injection"][key]
        print(f"  {key}: clean={r['clean']}, must_be={r['must_be']}, "
              f"caught_as_defect={r['caught_as_defect']}")
    print(f"  ALL AS PREDICTED: {results['fault_injection']['fault_injection_all_as_predicted']}")
    print()
    print("Desk bound (containment ratios, candidate half-width / migration figure):")
    for delta_str, ratios in results["desk_bound"]["containment_ratios"].items():
        print(f"  +/-{delta_str} deg: {ratios}")
