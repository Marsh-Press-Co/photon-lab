"""exp-097 -- R18 Tier 0 Gate-Closure: Positional Check 6, Check-5 R3/R5
Extension, Check 7 (Taper), Documentation Bundle. Panel Iteration 74.
Lead seat (rotation): MATERIALS & METAMATERIALS. Frozen spec: NOTES.md
(Predictions committed to git strictly BEFORE this file's first run,
house discipline). Change rationale: phase2_redteam_audit.md (6 Red-
Team-mandatory fixes, all adopted, zero overridden -- see NOTES.md's own
"Changes from Phase 1" section for the item-by-item mapping).

0 FDTD calls. Every `Sim` construction below stops before `sim.run()` is
ever invoked. Extends exp-096's own run.py by IMPORT (the `_load()`
house pattern) -- never by editing that file, matching this program's
established immutable-past-experiments discipline. Checks 1-4 and the
new Check 7 are run against ONE SHARED Sim object per representative
point (construct_sim called once per point, not once per check) --
matching NOTES.md's own frozen 21-construction prediction; Checks 1-4's
own logic is replicated inline here (not called via
`exp096.run_checks_1234`, which builds and discards its own Sim
internally) specifically so the same object also feeds Check 7.

Executes exp-096's own Reconciled Iteration-74 queue, Tier 0 in full:
  1+2. Check 6 fixed to positional (index-for-index) comparison, with an
       independently-keyed `family_ok` sub-check (Red Team's own fix for
       the family-level tautology in Phase 1's draft) and the
       `cpl_intended` half.
  3. Check 5 extended to R3/R5, with a 3-leg fault-injection negative
     control (FI-G).
  4. New Check 7: independent recompute of the raised-cosine taper
     window against `sim.sources[-1]['profile']`, plus FI-D.
  5. Documentation bundle (see NOTES.md).

Fault-injection scenarios this cycle: FI-D (new Sim, wrong edge), FI-E
(index swap, zero-cost), FI-F (cpl corruption, zero-cost), FI-G (native
constant corruption x3 legs, zero-cost), FI-H (new: family mislabel,
zero-cost, the fix for Red Team's own found tautology). Plus a bit-exact
reproduction of exp-096's own positive control + FI-A/B/C triad (R18's
own compliance duty for Checks 1-4 was already discharged at exp-096;
this cycle reruns them, sharing the object with Check 7, per the shared-
construction design above).
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
    """House `_load()` pattern (exp-078..096's own idiom for cross-
    experiment-directory imports)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP096_DIR = os.path.join(ROOT, "experiments", "096-t28-r4-registration-readback-gate")
exp096 = _load(os.path.join(EXP096_DIR, "run.py"), "_exp097_exp096")

dg = exp096.dg
CONFIGS = exp096.CONFIGS
TAPER = exp096.TAPER
CPL = exp096.CPL
PAIR_KEYS = exp096.PAIR_KEYS
construct_sim = exp096.construct_sim
phase_expected = exp096.phase_expected
NOTES_MD_FROZEN_LINE_VALUES = exp096.NOTES_MD_FROZEN_LINE_VALUES

# ---------------------------------------------------------------- representative points
# REPRESENTATIVE reused by reference from exp-096, extended with `pair_index`
# (0/1, derived from each point's own `notes_label` suffix -- already implicit,
# made explicit here) for the new positional Check 6.
REPRESENTATIVE = []
for pt in exp096.REPRESENTATIVE:
    label = pt["notes_label"]
    pair_index = int(label[-2]) if label.endswith("]") and label[-2] in "01" else 0
    REPRESENTATIVE.append(dict(pt, pair_index=pair_index))

# Independently re-grepped this session from experiments/095-.../NOTES.md's
# own prose (NOT restated from NOTES_MD_FROZEN_LINE_VALUES's comment block):
#   line 265: "Rank 2 -- cpl=50 (R5) family"
#   line 291: "Rank 3 -- cpl=40 (R4) sigma-comparability"
#   line 304: "Rank 4 -- 38.4 deg at corrected sigma, R3/cpl=30 family"
NOTES_MD_FROZEN_CPL_BY_FAMILY = {"R3": (30, 304), "R4": (40, 291), "R5": (50, 265)}

# Independent ground truth for `family`, keyed by `notes_line` -- NOT by
# `pt["family"]` (the fix for Red Team's own found tautology: the two
# sides of `family_ok` must not share an input).
NOTES_MD_FROZEN_FAMILY_BY_LINE = {437: "R4", 445: "R4", 476: "R5", 495: "R4", 511: "R3"}


def taper_expected(n, edge, amplitude=1.0):
    """Independent reproduction of `add_line_source`'s own raised-cosine
    window formula (`lab/fdtd2d.py:160-164`)."""
    p = np.ones(n)
    win = 0.5 * (1.0 - np.cos(np.pi * np.arange(edge) / edge))
    p[:edge] = win
    p[-edge:] = win[::-1]
    return amplitude * p


def run_checks_1234_and_7(family, theta_intended, cpl_intended, config_key,
                           cpl_actual=None, theta_actual=None, edge_actual=None):
    """One shared Sim construction feeding Checks 1-4 (replicated inline
    from exp-096's own `run_checks_1234`, unmodified logic) AND the new
    Check 7. `cpl_actual`/`theta_actual`/`edge_actual` default to the
    intended values; a fault-injection call passes a deliberately wrong
    value for exactly one."""
    cpl_actual = cpl_intended if cpl_actual is None else cpl_actual
    theta_actual = theta_intended if theta_actual is None else theta_actual
    edge_actual = TAPER[family] if edge_actual is None else edge_actual

    cfg = CONFIGS[family][config_key]
    from lab import Sim  # noqa: E402
    sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=cpl_actual,
              courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
    sim.add_line_source(cfg["src_x"], y_lo=cfg["y_lo"], y_hi=cfg["y_hi"],
                         angle_deg=theta_actual, amplitude=1.0,
                         profile="plane", edge=edge_actual)

    # Checks 1-4 (exp-096's own `run_checks_1234` logic, unmodified)
    check1 = (sim.lam == float(cpl_intended))
    check2 = (sim.source_specs[-1]["angle_deg"] == theta_intended)
    check3 = (sim.sources[-1]["x"] == cfg["src_x"]
              and sim.sources[-1]["sl"] == slice(cfg["y_lo"], cfg["y_hi"]))
    expected_phase = phase_expected(sim.lam, theta_intended, cfg["y_lo"], cfg["y_hi"])
    actual_phase = sim.sources[-1]["phase"]
    check4 = bool(actual_phase is not None
                  and np.allclose(actual_phase, expected_phase, atol=1e-9, rtol=0.0))

    # Check 7 (new): independent recompute of the taper window, using the
    # ALREADY-VERIFIED intended edge (matching Check 4's own pattern of
    # recomputing from the intended/upstream-verified value).
    n = cfg["y_hi"] - cfg["y_lo"]
    expected_taper = taper_expected(n, TAPER[family])
    actual_taper = sim.sources[-1]["profile"]
    check7 = bool(np.allclose(actual_taper, expected_taper, atol=1e-9, rtol=0.0))

    return dict(family=family, config_key=config_key,
                cpl_intended=cpl_intended, theta_intended=theta_intended,
                cpl_actual=cpl_actual, theta_actual=theta_actual, edge_actual=edge_actual,
                check1_resolution=check1, check2_angle_spec=check2,
                check3_placement=check3, check4_phase_ramp=check4,
                check7_taper=check7,
                clean_1234=bool(check1 and check2 and check3 and check4),
                clean_7=check7)


def check6_positional_and_cpl(pt):
    """Fix #1+#2+#5/6 (positional, cpl_intended, family_ok). Replaces
    set-membership. `family_ok` is looked up by `notes_line` alone --
    genuinely independent of `pt["family"]` -- closing Red Team's own
    found tautology in `cpl_ok` (which stays family-keyed on both sides,
    but is only meaningful once `family_ok` has independently confirmed
    the family label itself)."""
    line = pt["notes_line"]
    theta_frozen = NOTES_MD_FROZEN_LINE_VALUES[line][pt["pair_index"]]
    family_frozen = NOTES_MD_FROZEN_FAMILY_BY_LINE[line]
    cpl_frozen, _ = NOTES_MD_FROZEN_CPL_BY_FAMILY[family_frozen]
    theta_ok = bool(abs(pt["theta"] - theta_frozen) < 1e-9)
    family_ok = bool(pt["family"] == family_frozen)
    cpl_ok = bool(CPL[pt["family"]] == cpl_frozen)
    return dict(theta_ok=theta_ok, family_ok=family_ok, cpl_ok=cpl_ok,
                clean=bool(theta_ok and family_ok and cpl_ok))


def check6_set_membership_OLD(pt):
    """exp-096's own original (flawed) Check 6 -- kept, unmodified, for
    the direct old-vs-new fault-injection comparison (R12's idiom)."""
    line = pt["notes_line"]
    frozen_values = NOTES_MD_FROZEN_LINE_VALUES[line]
    found = any(abs(pt["theta"] - v) < 1e-9 for v in frozen_values)
    return dict(clean=bool(found))


def check5_recipe_spot_check_extended():
    """Fix #3: R4's own spot-check (exp-096, unchanged) plus new R3/R5
    legs, all hand-arithmetic outside `design_geometry.py`."""
    native_src_x, native_absorb, native_ny = 300, 40, 1584
    out = {}
    for family, ratio, target in [
        ("R3", 1.5, dg.R3_CONFIGS["C40_R3"]),
        ("R4", 2.0, dg.R4_CONFIGS["C40_R4"]),
        ("R5", 2.5, dg.R5_CONFIGS["C40_R5"]),
    ]:
        src_x = round(native_src_x * ratio) + 0
        absorb = round(native_absorb * ratio)
        ny = round(native_ny * ratio) + 0
        y_lo = absorb + 0
        y_hi = ny - y_lo
        ok = (src_x == target["src_x"] and y_lo == target["y_lo"] and y_hi == target["y_hi"])
        out[family] = dict(src_x_recomputed=src_x, y_lo_recomputed=y_lo, y_hi_recomputed=y_hi,
                            src_x_stored=target["src_x"], y_lo_stored=target["y_lo"],
                            y_hi_stored=target["y_hi"], clean=bool(ok))
    out["clean"] = all(out[f]["clean"] for f in ("R3", "R4", "R5"))
    return out


def run_fi_e():
    """FI-E: same-line index swap on line 437 (R4's Rank-1a pair).
    Zero new Sim constructions."""
    swapped = (39.4, 39.2)  # exp095.RANK1A_ANGLES reversed
    results = []
    for pair_index in (0, 1):
        pt = dict(family="R4", theta=swapped[pair_index], notes_line=437, pair_index=pair_index)
        new = check6_positional_and_cpl(pt)
        old = check6_set_membership_OLD(pt)
        results.append(dict(pair_index=pair_index, theta_scored=swapped[pair_index],
                             new_clean=new["clean"], old_clean=old["clean"]))
    caught_by_new = any(not r["new_clean"] for r in results)
    missed_by_old = all(r["old_clean"] for r in results)
    return dict(results=results, caught_by_new=bool(caught_by_new), missed_by_old=bool(missed_by_old))


def run_fi_f():
    """FI-F: CPL['R4'] corrupted to 30. Zero new Sim constructions."""
    pt = REPRESENTATIVE[0]  # family="R4", notes_line=437, pair_index=0
    cpl_saved = CPL["R4"]
    CPL["R4"] = 30
    try:
        new = check6_positional_and_cpl(pt)
        old = check6_set_membership_OLD(pt)
    finally:
        CPL["R4"] = cpl_saved
    return dict(new_clean=new["clean"], old_clean=old["clean"],
                caught_by_new=bool(not new["clean"]), missed_by_old=bool(old["clean"]))


def run_fi_g():
    """FI-G: native_src_x=301 (not 300), scored against all three
    families. Zero new Sim constructions."""
    native_src_x = 301  # corrupted (true value: 300)
    out = {}
    for family, ratio, target in [
        ("R3", 1.5, dg.R3_CONFIGS["C40_R3"]),
        ("R4", 2.0, dg.R4_CONFIGS["C40_R4"]),
        ("R5", 2.5, dg.R5_CONFIGS["C40_R5"]),
    ]:
        src_x = round(native_src_x * ratio) + 0
        out[family] = dict(src_x_recomputed=src_x, src_x_stored=target["src_x"],
                            caught_as_defect=bool(src_x != target["src_x"]))
    out["all_caught"] = all(out[f]["caught_as_defect"] for f in ("R3", "R4", "R5"))
    return out


def run_fi_h():
    """FI-H, new (Red Team's own fix for the family-level tautology):
    representative point 6 (true R3/38.4deg/line-511) scored with
    `family` overridden to "R4". Zero new Sim constructions."""
    true_pt = REPRESENTATIVE[5]  # family="R3", theta=38.4, notes_line=511, pair_index=0
    assert true_pt["family"] == "R3" and true_pt["notes_line"] == 511
    mislabeled = dict(true_pt, family="R4")
    new = check6_positional_and_cpl(mislabeled)
    old = check6_set_membership_OLD(mislabeled)
    return dict(true_family="R3", mislabeled_family="R4", notes_line=511,
                new_clean=new["clean"], old_clean=old["clean"],
                new_family_ok=new["family_ok"],
                caught_by_new=bool(not new["clean"]), missed_by_old=bool(old["clean"]))


def main():
    t0 = time.time()

    # --- Checks 1-4 + Check 7, representative set: ONE Sim per point (16) ---
    representative = []
    for pt in REPRESENTATIVE:
        family = pt["family"]
        cpl_intended = CPL[family]
        for config_key in PAIR_KEYS[family]:
            representative.append(
                run_checks_1234_and_7(family, pt["theta"], cpl_intended, config_key))

    # --- Check 6 (positional + cpl + family), both old and new, all 8 points ---
    check6_new = [check6_positional_and_cpl(pt) for pt in REPRESENTATIVE]
    check6_old = [check6_set_membership_OLD(pt) for pt in REPRESENTATIVE]

    # --- Check 5, extended to R3/R4/R5 ---
    check5 = check5_recipe_spot_check_extended()

    # --- Positive control + FI-A/B/C, one shared Sim each (4 new constructions),
    #     feeding Checks 1-4 AND Check 7 together, per the shared-construction
    #     design above. Bit-exact scenario reproduction of exp-096's own triad. ---
    pc = run_checks_1234_and_7("R4", 39.2, 40, "C40_R4")
    fia = run_checks_1234_and_7("R4", 39.2, 40, "C40_R4", cpl_actual=dg.R3_CPL[600])
    fib = run_checks_1234_and_7("R4", 39.2, 40, "C40_R4", theta_actual=38.69)
    fic = run_checks_1234_and_7("R4", 39.2, 40, "C40_R4", theta_actual=-39.2)
    fi_1234_7 = dict(
        positive_control=dict(**pc, must_be_1234="CLEAN", must_be_7="CLEAN"),
        FI_A_family_cpl_swap=dict(**fia, must_be_1234="DEFECT-FOUND", must_be_7="CLEAN"),
        FI_B_angle_mislabel=dict(**fib, must_be_1234="DEFECT-FOUND", must_be_7="CLEAN"),
        FI_C_sign_flip=dict(**fic, must_be_1234="DEFECT-FOUND", must_be_7="CLEAN"),
    )
    fi_1234_7["all_as_predicted"] = bool(
        pc["clean_1234"] and pc["clean_7"]
        and not fia["clean_1234"] and fia["clean_7"]
        and not fib["clean_1234"] and fib["clean_7"]
        and not fic["clean_1234"] and fic["clean_7"]
    )

    # --- FI-D (1 new Sim construction): wrong edge, R3's taper width where R4's is intended ---
    fid = run_checks_1234_and_7("R4", 39.2, 40, "C40_R4", edge_actual=TAPER["R3"])
    fid_result = dict(**fid, must_be_1234="CLEAN", must_be_7="DEFECT-FOUND",
                       as_predicted=bool(fid["clean_1234"] and not fid["clean_7"]))

    # --- FI-E/F/G/H (zero new Sim constructions) ---
    fi_e = run_fi_e()
    fi_f = run_fi_f()
    fi_g = run_fi_g()
    fi_h = run_fi_h()

    all_repr_1234_clean = all(r["clean_1234"] for r in representative)
    all_repr_7_clean = all(r["clean_7"] for r in representative)
    check6_new_all_clean = all(r["clean"] for r in check6_new)
    check6_old_all_clean = all(r["clean"] for r in check6_old)
    check5_clean = check5["clean"]

    gate_clean = bool(all_repr_1234_clean and all_repr_7_clean
                       and check6_new_all_clean and check5_clean)

    sim_construction_count = dict(
        representative=len(representative),          # 16
        fault_injection_new=4,                        # positive_control, FI-A, FI-B, FI-C
        fi_d_new=1,                                    # FI-D
        fi_e_f_g_h_new=0,
        total=len(representative) + 4 + 1,             # 21, matching NOTES.md's frozen prediction
    )

    results = dict(
        experiment="exp-097",
        panel_iteration=74,
        fdtd_calls=0,
        wall_time_s=None,
        representative=representative,
        representative_1234_all_clean=all_repr_1234_clean,
        representative_7_all_clean=all_repr_7_clean,
        check6_new=check6_new,
        check6_new_all_clean=check6_new_all_clean,
        check6_old=check6_old,
        check6_old_all_clean=check6_old_all_clean,
        check5_extended=check5,
        fault_injection_1234_7=fi_1234_7,
        FI_D=fid_result,
        FI_E=fi_e,
        FI_F=fi_f,
        FI_G=fi_g,
        FI_H=fi_h,
        registration_gate_outcome="CLEAN" if gate_clean else "DEFECT-FOUND",
        sim_construction_count=sim_construction_count,
    )
    results["wall_time_s"] = round(time.time() - t0, 3)
    return results


if __name__ == "__main__":
    results = main()
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"exp-097 -- R18 Tier 0 Gate Closure (0 FDTD calls, {results['wall_time_s']}s wall)")
    print(f"Representative Checks 1-4: all clean = {results['representative_1234_all_clean']}")
    print(f"Representative Check 7 (taper): all clean = {results['representative_7_all_clean']}")
    print(f"Check 5 extended (R3/R4/R5): clean = {results['check5_extended']['clean']}")
    print(f"Check 6-new (positional+cpl+family): all clean = {results['check6_new_all_clean']}")
    print(f"Check 6-old (set-membership, for comparison): all clean = {results['check6_old_all_clean']}")
    print(f"REGISTRATION-READBACK GATE OUTCOME: {results['registration_gate_outcome']}")
    print()
    print("Fault injection (Checks 1-4 + Check 7, shared construction):")
    for key in ("positive_control", "FI_A_family_cpl_swap", "FI_B_angle_mislabel", "FI_C_sign_flip"):
        r = results["fault_injection_1234_7"][key]
        print(f"  {key}: clean_1234={r['clean_1234']} (must be {r['must_be_1234']}), "
              f"clean_7={r['clean_7']} (must be {r['must_be_7']})")
    print(f"  ALL AS PREDICTED: {results['fault_injection_1234_7']['all_as_predicted']}")
    print()
    print(f"FI-D (wrong edge): clean_1234={results['FI_D']['clean_1234']} (must be True), "
          f"clean_7={results['FI_D']['clean_7']} (must be False), "
          f"as_predicted={results['FI_D']['as_predicted']}")
    print(f"FI-E (Check 6 theta, index swap): caught_by_new={results['FI_E']['caught_by_new']} "
          f"(must be True), missed_by_old={results['FI_E']['missed_by_old']} (must be True)")
    print(f"FI-F (Check 6 cpl, corruption): caught_by_new={results['FI_F']['caught_by_new']} "
          f"(must be True), missed_by_old={results['FI_F']['missed_by_old']} (must be True)")
    print(f"FI-G (Check 5, native constant corruption, 3 legs): all_caught={results['FI_G']['all_caught']} "
          f"(must be True)")
    print(f"FI-H (Check 6 family, mislabel): caught_by_new={results['FI_H']['caught_by_new']} "
          f"(must be True), missed_by_old={results['FI_H']['missed_by_old']} (must be True)")
    print()
    print(f"Sim construction count: {results['sim_construction_count']}")
