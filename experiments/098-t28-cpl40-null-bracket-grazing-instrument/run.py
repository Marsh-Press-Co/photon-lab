"""exp-098 -- cpl=40 Null Bracketing (Three Remaining Nulls), Re-Centered
theta0~=38.590230deg Recovery, and a Genuinely Theta-Dependent Grazing-
Incidence Instrument. Panel Iteration 75. Lead seat (rotation):
ELECTROMAGNETISM. Frozen spec: NOTES.md (Predictions committed to git
strictly BEFORE this file's first run, house discipline). Change
rationale: phase2_redteam_audit.md (9 numbered attacks; 5 mandatory
fixes, all adopted; 1 critique's precedent overridden, its recommendation
adopted anyway -- see NOTES.md's own "Changes from Phase 1" section).

32 real FDTD `sim.run()` calls (items i+ii), each preceded by a zero-cost
registration-readback pre-check (extends exp-097's own gate by IMPORT,
never by editing that file). Item (v)'s grazing-incidence instrument is
0 FDTD calls (a closed-form desk computation). Item (iv)'s FI-G' is 0 new
Sim constructions.

Executes exp-097's own Reconciled Iteration-75 queue: Tier 0 (zero-FDTD
fixes) runs ALONGSIDE Tier 1 (real FDTD spend), not gating it.
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
    """House `_load()` pattern (exp-078..097's own idiom for cross-
    experiment-directory imports)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP097_DIR = os.path.join(ROOT, "experiments", "097-t28-r18-tier0-gate-closure")
EXP095_DIR = os.path.join(ROOT, "experiments", "095-t28-r4-ground-truth-sign-control")
EXP090_DIR = os.path.join(ROOT, "experiments", "090-t28-floor-frac-threshold-fit")
EXP092_DIR = os.path.join(ROOT, "experiments", "092-t28-crossing-relocation-caution-zone-rebuild")
EXP085_DIR = os.path.join(ROOT, "experiments", "085-t28-leg-a-wide-window-period-pin")

# --- registration-readback gate (exp-097's own module) ---
exp097 = _load(os.path.join(EXP097_DIR, "run.py"), "_exp098_exp097")
CONFIGS = exp097.CONFIGS
CPL = exp097.CPL
run_checks_1234_and_7 = exp097.run_checks_1234_and_7
check5_recipe_spot_check_extended = exp097.check5_recipe_spot_check_extended

# --- R4-family real-FDTD machinery (exp-095's own module, independently
#     loaded -- a SEPARATE module instance from exp097's own transitive
#     chain, per this program's established `_load()` pattern; both
#     instances are deterministic reproductions of the same source and
#     agree on every value, but the actual FDTD calls below use ONLY
#     exp095's own objects, never mixed with exp097's, to stay internally
#     consistent with each function's own closure. ---
exp095 = _load(os.path.join(EXP095_DIR, "run.py"), "_exp098_exp095")
dg = exp095.dg
PAIR_KEYS_R4 = exp095.PAIR_KEYS_R4
cell_metrics_r4 = exp095.cell_metrics_r4
pair_metrics_full = exp095.pair_metrics_full
netd_row = exp095.netd_row
run_block_r4 = exp095.run_block_r4
compute_floor = exp095.compute_floor
XI_TOL = exp095.XI_TOL
SIGMA_R4_CORRECTED = exp095.SIGMA_R4_CORRECTED
assert abs(SIGMA_R4_CORRECTED - 0.25) < 1e-12
assert PAIR_KEYS_R4 == ("C40_R4", "G40_R4")

# --- grazing-incidence instrument machinery (exp-085's own module) ---
exp085 = _load(os.path.join(EXP085_DIR, "phase4_derivation.py"), "_exp098_exp085")
FastEval = exp085.FastEval
verify_fast_eval_bit_identical = exp085.verify_fast_eval_bit_identical
dg048 = exp085.dg048
dg065 = exp085.dg065
CFG_C40 = exp085.CFG_C40
LAM600 = exp085.LAM600
GEOM_C40 = dg065.propagator_geom(CFG_C40)  # uppercase-keyed geometry dict `_geom_derived` expects

from lab import ambient as amb  # noqa: E402

NETD_ROW_KEYS = {
    "p_abs_w_c", "p_abs_w_g", "dt_ss_full_K_c", "dt_ss_full_K_g",
    "netd_classification_c", "netd_classification_g",
    "sigma_ext_cells_c", "sigma_ext_cells_g",
    "ratio_abs_ext_raw_c", "ratio_abs_ext_raw_g",
}

# ================================================================ established ground truth (re-pulled, not hand-typed)
j090 = json.load(open(os.path.join(EXP090_DIR, "results.json")))
CROSSINGS_CPL20 = j090["q8"]["crossings_deg"]
assert len(CROSSINGS_CPL20) == 4
THETA0_A, THETA0_38590, THETA0_B, THETA0_C = CROSSINGS_CPL20
for th, expect in [(THETA0_A, 37.127246), (THETA0_38590, 38.590230),
                    (THETA0_B, 40.265420), (THETA0_C, 41.460901)]:
    assert abs(th - expect) < 1e-5, f"crossing mismatch: {th} vs {expect}"

j092 = json.load(open(os.path.join(EXP092_DIR, "results.json")))
CR30 = j092["rank1"]["crossing_report"]
SHIFT_20_30_B = CR30["shift_vs_cpl20_lower"]                 # -0.193581...
SHIFT_20_30_C = CR30["shift_vs_cpl20_upper"]                  # +0.320166... (primary/lower of the two near-C crossings)
assert abs(SHIFT_20_30_B - (-0.1935812644838535)) < 1e-9
assert abs(SHIFT_20_30_C - 0.3201659178026546) < 1e-9

j095 = json.load(open(os.path.join(EXP095_DIR, "results.json")))
RANK1C_FILED = j095["rank1"]["rank1c"]["per_theta"]
assert set(RANK1C_FILED.keys()) == {"38.49", "38.69"}
for th_str, row in RANK1C_FILED.items():
    assert NETD_ROW_KEYS <= set(row.keys()), f"filed Rank1c row {th_str} missing netd_row keys"


# ================================================================ item (i)/(ii): registration pre-check + real FDTD batch
def registration_preflight(angles, config_keys=("C40_R4", "G40_R4")):
    """Zero-cost extension of exp-097's own registration-readback gate to
    every NEW (family, theta, cpl, config_key) point this cycle spends
    real FDTD on -- R18's own 'earn coverage, don't just claim it'
    discipline, applied to Tier-1 spend for the first time."""
    checks = []
    for th in angles:
        for key in config_keys:
            checks.append(run_checks_1234_and_7("R4", th, 40, key))
    all_clean = all(c["clean_1234"] and c["clean_7"] for c in checks)
    return dict(n_points=len(checks), all_clean=bool(all_clean), checks=checks)


def run_r4_batch(angles, floor):
    """One angle list -> registration preflight (must be CLEAN) -> real
    FDTD (both legs, cell_metrics_r4, pair_metrics_full, netd_row) ->
    per-angle report dict. Mirrors exp-095's own Rank 1c pattern exactly
    (same dg.R4_STEPS, same SIGMA_R4_CORRECTED, same PAIR_KEYS_R4,
    same xi_ext/sigma_abs_nonneg gates), extended with the mandatory
    netd_row()-coverage assert (Red Team Attack 5)."""
    preflight = registration_preflight(angles)
    assert preflight["all_clean"], f"REGISTRATION GATE FAILED for angles {angles}: HALT"

    jobs = []
    for th in angles:
        for key in PAIR_KEYS_R4:
            jobs.append((key, th, False, dg.R4_STEPS, None))
            jobs.append((key, th, True, dg.R4_STEPS, SIGMA_R4_CORRECTED))
    captures, wall = run_block_r4(jobs)

    xi_pass = True
    nonneg_pass = True
    cells = {}
    for th in angles:
        for key in PAIR_KEYS_R4:
            cap_empty = captures[(key, th, False, dg.R4_STEPS)]
            cap_article = captures[(key, th, True, dg.R4_STEPS)]
            cell = cell_metrics_r4(key, th, dg.R4_STEPS, cap_empty, cap_article)
            cells[(key, th)] = cell
            for xi in cell["xi_ext"].values():
                if xi > XI_TOL:
                    xi_pass = False
            if not cell["sigma_abs_nonneg"]:
                nonneg_pass = False
    assert xi_pass, "xi_ext gate FAILED -- extinction-routes disagreement; HALT"
    assert nonneg_pass, "sigma_abs>=0 gate FAILED; HALT"

    report = {}
    for th in angles:
        c_cell = cells[("C40_R4", th)]
        g_cell = cells[("G40_R4", th)]
        pm = pair_metrics_full(c_cell, g_cell, floor)
        row = dict(delta_scene=pm["delta_scene"], frac_contrast=pm["frac_contrast"],
                   ratio_k=pm["ratio_k"], floor_pass=pm["floor_pass"],
                   **netd_row(pm))
        assert NETD_ROW_KEYS <= set(row.keys()), (
            f"MANDATORY netd_row() COVERAGE ASSERT FAILED at theta={th} -- "
            f"missing keys {NETD_ROW_KEYS - set(row.keys())}; HALT before results.json")
        report[th] = row

    return dict(preflight=preflight, report=report, wall_s=wall,
                n_calls=len(jobs), xi_pass=xi_pass, nonneg_pass=nonneg_pass)


def find_sign_change(angles_sorted, delta_scene_by_angle):
    """Simple linear-interpolation crossing finder over an ordered,
    already-sorted angle list. Returns (crossing_theta, bracket) or
    (None, None) if no sign change exists in the tested span."""
    for a, b in zip(angles_sorted[:-1], angles_sorted[1:]):
        da, db = delta_scene_by_angle[a], delta_scene_by_angle[b]
        if da == 0.0:
            return a, (a, b)
        if (da < 0) != (db < 0):
            frac = abs(da) / (abs(da) + abs(db))
            return a + frac * (b - a), (a, b)
    return None, None


def richardson_style_diagnostic(shift_20_30, shift_20_40, cpl20=20, cpl30=30, cpl40=40):
    """Explicitly DESCRIPTIVE (Idealization 49) -- not a formal Richardson
    extrapolation / convergence-order estimate: no continuum (converged)
    reference value exists anywhere in this program's record to anchor
    one. Reports the observed pairwise-shift ratio alongside the naive
    ratio a uniform 2nd-order-accurate (Yee-grid-typical) error scaling
    would predict, purely as a sanity comparison."""
    if shift_20_40 is None or shift_20_30 in (None, 0.0):
        return dict(available=False)
    observed_ratio = shift_20_40 / shift_20_30
    h20, h30, h40 = 1.0 / cpl20, 1.0 / cpl30, 1.0 / cpl40
    naive_order2_ratio = (h40 / h20) ** 2 / (h30 / h20) ** 2
    return dict(available=True, shift_20_30=shift_20_30, shift_20_40=shift_20_40,
                observed_ratio=observed_ratio, naive_order2_ratio=naive_order2_ratio,
                same_sign_as_20_30=bool((shift_20_30 < 0) == (shift_20_40 < 0)),
                note="descriptive only -- no continuum reference exists; not a formal order estimate (Idealization 49)")


# ================================================================ item (v): grazing-incidence instrument (0 FDTD calls)
def eval_raw(fe, theta_deg):
    """Independent, non-invasive extension of `FastEval` (exp-085's own
    frozen module, never edited): replicates `FastEval.one`'s own
    internal steps exactly, additionally returning the raw (unnormalized)
    window means `bo`/`bf` that its own `weber()` ratio call discards.
    Bit-identical to `fe.one(theta_deg)` by construction (same G0/G0_obl/
    amp/Sx/window_means call sequence) -- verified below before use."""
    amp = dg048._src_amp(theta_deg, fe.k, fe.gd)
    E = fe.G0 @ amp
    H = fe.G0_obl @ amp
    Sx = -np.real(E * np.conj(H))
    bo, bf = amb.window_means(Sx, fe.gd["y_lo"], fe.g["OBJ_Y"], fe.g["R_OUT"],
                               fe.g["GUARD_OUT"], fe.g["W_FLANK"])
    return bo, bf, amb.weber(bo, bf)


def run_grazing_incidence_instrument():
    fe = FastEval(GEOM_C40, LAM600)
    spot_thetas = [30.0, 39.0, 55.0, 65.0, 89.5]
    fast_eval_check = verify_fast_eval_bit_identical(fe, spot_thetas)

    thetas = list(np.arange(30.0, 89.5 + 1e-9, 0.5))
    thetas[-1] = 89.5

    curve = {}
    for th in thetas:
        bo, bf, c = eval_raw(fe, th)
        one_val = fe.one(th)
        assert c == one_val, f"eval_raw/FastEval.one MISMATCH at theta={th}: {c} vs {one_val}"
        curve[th] = dict(bo=bo, bf=bf, C=c)

    # GP1 -- passivity bound (unchanged from Phase 1)
    c_values = [row["C"] for row in curve.values()]
    gp1_min = min(c_values)
    gp1_pass = bool(gp1_min >= -1.0 - 1e-6)

    # GP2' -- grazing-incidence amplitude-blowup instrument (REDESIGNED,
    # genuinely theta-dependent: reuses the SAME C(theta) values GP1
    # already computed, viewed a second way -- magnitude vs. sign)
    ref_band = [th for th in thetas if 30.0 <= th <= 50.0]
    ref_abs = [abs(curve[th]["C"]) for th in ref_band]
    ref_median = float(np.median(ref_abs))
    gp2_rows = {}
    for th in thetas:
        ratio = abs(curve[th]["C"]) / ref_median if ref_median != 0 else float("inf")
        if ratio <= 10.0:
            cls = "VALID"
        elif ratio <= 1000.0:
            cls = "MARGINAL"
        else:
            cls = "INVALID"
        gp2_rows[th] = dict(abs_C=abs(curve[th]["C"]), ratio_to_ref=ratio, classification=cls)
    invalid_thetas = sorted(th for th, r in gp2_rows.items() if r["classification"] == "INVALID")
    marginal_thetas = sorted(th for th, r in gp2_rows.items() if r["classification"] == "MARGINAL")
    flagged_band = None
    if invalid_thetas or marginal_thetas:
        flagged = sorted(invalid_thetas + marginal_thetas)
        flagged_band = (min(flagged), max(flagged))
    overlaps_known_blowup = False
    if flagged_band is not None:
        overlaps_known_blowup = not (flagged_band[1] < 59.0 or flagged_band[0] > 73.0)

    # GP3 -- reciprocity code-read + assertion (QUANTUM OPTICS' degeneracy
    # finding, adopted verbatim)
    gd = fe.gd
    gp3_degenerate = bool(np.array_equal(gd["y_src"], gd["y_obs"]))
    assert gp3_degenerate, "GP3 assumption violated -- y_src/y_obs are no longer the same construction"

    return dict(
        fast_eval_bit_identical_check=fast_eval_check,
        n_evaluations=len(thetas),
        ref_band=[ref_band[0], ref_band[-1]], ref_median_abs_C=ref_median,
        gp1_min_C=gp1_min, gp1_pass=gp1_pass,
        gp2_reference_band_note="theta in [30,50] deg, comfortably inside the model's own narrow-window fit range",
        gp2_classification_bands=dict(VALID="<=10x", MARGINAL="10x-1000x", INVALID=">1000x"),
        gp2_invalid_thetas=invalid_thetas, gp2_marginal_thetas=marginal_thetas,
        gp2_flagged_band=flagged_band, gp2_overlaps_known_exp086_blowup_59_73=overlaps_known_blowup,
        gp2_curve=[dict(theta=th, abs_C=gp2_rows[th]["abs_C"], ratio_to_ref=gp2_rows[th]["ratio_to_ref"],
                         classification=gp2_rows[th]["classification"]) for th in thetas],
        gp3_y_src_equals_y_obs=gp3_degenerate,
        gp3_note="obliquity is symmetric purely because y_src/y_obs share one construction and one shared "
                 "d_sp -- there was never a second, independently-defined observer-side obliquity to "
                 "compare against in this geometry (QUANTUM OPTICS, adopted verbatim).",
    )


# ================================================================ item (iv): Tier-0 doc/code bundle -- FI-G'
def run_fi_g_prime():
    """FI-G' (new, item iv-c): native_absorb corrupted to 41 (true: 40),
    scored against all three families' y_lo/y_hi recomputation -- closes
    the gap that the original FI-G (native src_x corruption only) left
    the y_lo/y_hi branch of Check 5 with zero fault-injection coverage.
    Zero new Sim constructions."""
    native_src_x, native_absorb, native_ny = 300, 41, 1584  # native_absorb corrupted: 41, not 40
    dg097 = exp097.dg
    out = {}
    for family, ratio, target in [
        ("R3", 1.5, dg097.R3_CONFIGS["C40_R3"]),
        ("R4", 2.0, dg097.R4_CONFIGS["C40_R4"]),
        ("R5", 2.5, dg097.R5_CONFIGS["C40_R5"]),
    ]:
        src_x = round(native_src_x * ratio) + 0
        absorb = round(native_absorb * ratio)
        ny = round(native_ny * ratio) + 0
        y_lo = absorb + 0
        y_hi = ny - y_lo
        y_lo_ok = (y_lo == target["y_lo"])
        y_hi_ok = (y_hi == target["y_hi"])
        caught = bool(not y_lo_ok or not y_hi_ok)
        out[family] = dict(y_lo_recomputed=y_lo, y_hi_recomputed=y_hi,
                            y_lo_stored=target["y_lo"], y_hi_stored=target["y_hi"],
                            caught_as_defect=caught)
    out["all_caught"] = all(out[f]["caught_as_defect"] for f in ("R3", "R4", "R5"))
    return out


# ================================================================ main
def main():
    t0 = time.time()
    print("=" * 78)
    print("exp-098 -- T28 cpl=40 null bracketing + grazing-incidence instrument")
    print("Panel Iteration 75, ELECTROMAGNETISM rotation lead")
    print("=" * 78)

    floor, rms, n83, per_theta_83_full = compute_floor()
    print(f"\n[R13 floor gate] RMS[frac_contrast], n={n83}: {rms:.6e}  FLOOR={floor:.6e}  "
          "(unchanged, applied unrecomputed -- Idealization 6)")

    # ---- item (iv): Tier-0 doc/code bundle ----
    print("\n" + "=" * 78)
    print("ITEM (iv): Tier-0 documentation/code-correction bundle -- FI-G'")
    print("=" * 78)
    check5_extended = check5_recipe_spot_check_extended()
    fi_g_prime = run_fi_g_prime()
    print(f"[Check 5, R3/R4/R5, reused from exp-097] clean={check5_extended['clean']}")
    print(f"[FI-G', new] all_caught={fi_g_prime['all_caught']}")
    assert fi_g_prime["all_caught"], "FI-G' FAILED to catch native_absorb corruption -- HALT"

    # ---- item (i): bracket the other three established cpl=20 nulls at cpl=40 ----
    print("\n" + "=" * 78)
    print("ITEM (i): bracket nulls A/B/C (cpl=20) at cpl=40, +/-0.500deg quartile-spaced")
    print("=" * 78)
    NULLS = {
        "A": dict(theta0=THETA0_A, angles=[THETA0_A - 0.500, THETA0_A - 0.1667, THETA0_A + 0.1667, THETA0_A + 0.500]),
        "B": dict(theta0=THETA0_B, angles=[THETA0_B - 0.500, THETA0_B - 0.1667, THETA0_B + 0.1667, THETA0_B + 0.500]),
        "C": dict(theta0=THETA0_C, angles=[THETA0_C - 0.500, THETA0_C - 0.1667, THETA0_C + 0.1667, THETA0_C + 0.500]),
    }
    item_i = {}
    for label, spec in NULLS.items():
        angles_sorted = sorted(spec["angles"])
        print(f"\n[Null {label}] theta0(cpl20)={spec['theta0']:.6f}deg  angles={[round(a, 6) for a in angles_sorted]}")
        batch = run_r4_batch(angles_sorted, floor)
        print(f"  wall={batch['wall_s']:.1f}s ({batch['wall_s'] / 60.0:.2f} min)  "
              f"calls={batch['n_calls']}  preflight_clean={batch['preflight']['all_clean']}")
        delta_by_angle = {a: r["delta_scene"] for a, r in batch["report"].items()}
        for a in angles_sorted:
            print(f"    theta={a:.6f}: delta_scene={delta_by_angle[a]:+.6e}  "
                  f"floor_pass={batch['report'][a]['floor_pass']}")
        all_floor_pass = all(r["floor_pass"] for r in batch["report"].values())
        crossing, bracket = find_sign_change(angles_sorted, delta_by_angle)
        verdict = "SIGN-CHANGE-FOUND" if crossing is not None else "NO-SIGN-CHANGE"
        if not all_floor_pass:
            verdict = "INCONCLUSIVE-FLOOR"
        print(f"  [Null {label}] verdict={verdict}  crossing={crossing}")
        item_i[label] = dict(theta0_cpl20=spec["theta0"], angles=angles_sorted,
                              report={f"{a:.6f}": batch["report"][a] for a in angles_sorted},
                              all_floor_pass=all_floor_pass, crossing_cpl40=crossing,
                              crossing_bracket=bracket, verdict=verdict,
                              wall_s=batch["wall_s"], n_calls=batch["n_calls"],
                              preflight=batch["preflight"])

    item_i_all_sign_change = all(item_i[l]["verdict"] == "SIGN-CHANGE-FOUND" for l in NULLS)
    item_i_all_no_sign_change = all(item_i[l]["verdict"] == "NO-SIGN-CHANGE" for l in NULLS)
    if item_i_all_sign_change:
        item_i_family_verdict = "PASS-family-clean"
    elif item_i_all_no_sign_change:
        item_i_family_verdict = "FAIL-family-wide"
    else:
        item_i_family_verdict = "MIXED"
    print(f"\n[Item (i) SUMMARY] family verdict={item_i_family_verdict}")

    # MATERIALS' Richardson-style diagnostic (descriptive only, Idealization 49)
    richardson_B = richardson_style_diagnostic(SHIFT_20_30_B, item_i["B"]["crossing_cpl40"] and
                                                (item_i["B"]["crossing_cpl40"] - THETA0_B))
    richardson_C = richardson_style_diagnostic(SHIFT_20_30_C, item_i["C"]["crossing_cpl40"] and
                                                (item_i["C"]["crossing_cpl40"] - THETA0_C))
    richardson_A = dict(available=False, note="no cpl=30 counterpart on file for null A (theta0=37.127246deg)")
    print(f"[Richardson-style diagnostic, descriptive only] B={richardson_B}  C={richardson_C}  A={richardson_A}")

    # ---- item (ii): re-centered node-bracketing re-run at theta0~=38.590230deg ----
    print("\n" + "=" * 78)
    print("ITEM (ii): re-centered node-bracketing re-run at theta0~=38.590230deg")
    print("=" * 78)
    NEW_ANGLES_II = [38.09, 38.19, 38.29, 38.39]
    batch_ii = run_r4_batch(NEW_ANGLES_II, floor)
    print(f"  wall={batch_ii['wall_s']:.1f}s ({batch_ii['wall_s'] / 60.0:.2f} min)  calls={batch_ii['n_calls']}")
    combined_angles = sorted(NEW_ANGLES_II + [38.49, 38.69])
    combined_delta = {}
    combined_report = {}
    for a in NEW_ANGLES_II:
        combined_delta[a] = batch_ii["report"][a]["delta_scene"]
        combined_report[f"{a:.6f}"] = batch_ii["report"][a]
    for a_str, row in RANK1C_FILED.items():
        a = float(a_str)
        combined_delta[a] = row["delta_scene"]
        combined_report[f"{a:.6f}"] = row
    for a in combined_angles:
        print(f"    theta={a:.6f}: delta_scene={combined_delta[a]:+.6e}")
    combined_all_floor_pass = all(combined_report[f"{a:.6f}"]["floor_pass"] for a in combined_angles)
    crossing_ii, bracket_ii = find_sign_change(combined_angles, combined_delta)
    if not combined_all_floor_pass:
        item_ii_verdict = "INCONCLUSIVE-FLOOR"
    elif crossing_ii is not None:
        item_ii_verdict = "CONFIRM-migration-down" if crossing_ii < 38.49 else "SIGN-CHANGE-FOUND-not-below-38.49"
    else:
        item_ii_verdict = "REFUTE-down-CONFIRM-neither"
    print(f"[Item (ii) SUMMARY] verdict={item_ii_verdict}  crossing={crossing_ii}  span=38.09-38.69deg")
    item_ii = dict(theta0_cpl20=THETA0_38590, new_angles=NEW_ANGLES_II,
                   reused_angles_from_exp095=[38.49, 38.69], combined_angles=combined_angles,
                   combined_report=combined_report, all_floor_pass=combined_all_floor_pass,
                   crossing_cpl40=crossing_ii, crossing_bracket=bracket_ii, verdict=item_ii_verdict,
                   wall_s=batch_ii["wall_s"], n_calls=batch_ii["n_calls"], preflight=batch_ii["preflight"])

    # ---- item (v): grazing-incidence instrument ----
    print("\n" + "=" * 78)
    print("ITEM (v): grazing-incidence instrument (GP1/GP2'/GP3), 0 FDTD calls")
    print("=" * 78)
    item_v = run_grazing_incidence_instrument()
    print(f"[GP1] min(C(theta))={item_v['gp1_min_C']:+.6e}  pass={item_v['gp1_pass']}")
    print(f"[GP2'] flagged_band={item_v['gp2_flagged_band']}  "
          f"overlaps_known_exp086_blowup(59-73deg)={item_v['gp2_overlaps_known_exp086_blowup_59_73']}")
    print(f"[GP3] y_src==y_obs (degenerate)={item_v['gp3_y_src_equals_y_obs']}")

    # ---- item (iii): netd_row() coverage, enforced (already asserted inline above) ----
    total_calls = item_i["A"]["n_calls"] + item_i["B"]["n_calls"] + item_i["C"]["n_calls"] + item_ii["n_calls"]
    assert total_calls == 32, f"expected 32 real FDTD calls, got {total_calls}"
    all_netd_rows = []
    for l in NULLS:
        all_netd_rows.extend(item_i[l]["report"].values())
    all_netd_rows.extend({k: v for k, v in item_ii["combined_report"].items() if k not in
                           (f"{a:.6f}" for a in [38.49, 38.69])}.values())
    for row in all_netd_rows:
        assert NETD_ROW_KEYS <= set(row.keys()), "MANDATORY netd_row() coverage assert failed at final aggregation"

    total_wall = time.time() - t0
    print(f"\n{'=' * 78}\nTOTAL: {total_calls} real FDTD calls, {total_wall:.1f}s "
          f"({total_wall / 60.0:.2f} min) wall time\n{'=' * 78}")

    results = dict(
        experiment="exp-098", panel_iteration=75,
        fdtd_calls=total_calls, wall_time_s=total_wall,
        r13_floor_gate=dict(floor=floor, rms=rms, n83=n83),
        item_iv=dict(check5_extended=check5_extended, fi_g_prime=fi_g_prime),
        item_i=item_i, item_i_family_verdict=item_i_family_verdict,
        richardson_diagnostic=dict(A=richardson_A, B=richardson_B, C=richardson_C),
        item_ii=item_ii,
        item_v=item_v,
        netd_row_coverage_assert="PASS -- all rows carry all 10 keys",
        idealization_40_correction=(
            "cpl_ok alone already discriminates every currently-possible family mislabel among "
            "R3/R4/R5, since CPL={R3:30,R4:40,R5:50} is injective -- independently re-confirmed by "
            "QUANTUM OPTICS this cycle -- not merely 'safe because gated behind family_ok' as "
            "exp-097's own text claimed."
        ),
        quantum_echo_logged=(
            "QUANTUM OPTICS' own exp-097 Phase-5 self-review independently repeated this exact "
            "Idealization-40 mischaracterization -- the first instance of an R18-class scope error "
            "occurring inside a review document itself, not a proposal."
        ),
    )
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(results, f, indent=2, default=str)
    print("\nresults.json written.")


if __name__ == "__main__":
    main()
