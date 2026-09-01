"""exp-098 Phase 5 same-shift fixes (Red Team's final audit, Iteration 75).

Applies the 8 mandated, zero-FDTD, zero-new-`sim.run()`-call corrections to
the already-filed `results.json` WITHOUT re-running the 64 real FDTD calls
(item i/ii's `delta_scene` values are unaffected by any of these fixes --
recomputing them would cost ~2.3 hours for zero information gain, the exact
waste this program's own "reuse, don't rebuild" discipline exists to avoid).

This script imports `run.py` (already patched with the corrected
`richardson_style_diagnostic()` pairing, the new `run_fi_g_double_prime()`,
and the `registration_preflight()` call for the reused Rank-1c points) as a
module WITHOUT calling its `main()` -- module-level execution already
recomputes every module-scope constant (THETA0_*, SHIFT_20_30_*,
CROSSINGS_CPL20, etc.) fresh from source, so nothing here is hand-typed.

Fixes applied (see phase5_redteam.md / NOTES.md Result for the full
rationale of each):
  1. Richardson diagnostic: corrected marginal-to-marginal pairing.
  2. GP2' Result overclaim: corrected in NOTES.md prose (this script adds
     the supporting exact VALID/MARGINAL counts as a results.json field).
  3. Row-count mislabeling: n_rows_new/n_rows_total_incl_reused added,
     netd_row_coverage_assert text corrected.
  4. GP1 framing: corrected disclosure text added.
  5. Idealization 47: the two missing registration-gate calls are now
     actually executed (reused_points_registration_check).
  6. Banner placement: fixed in NOTES.md directly (no results.json field).
  7. FI-G'': executed (fi_g_double_prime).
  8. GP2'/exp-086 "same formula" disclosure: added as a results.json field.
"""

import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def main():
    m = _load(os.path.join(HERE, "run.py"), "_exp098_fixes")

    with open(os.path.join(HERE, "results.json")) as f:
        results = json.load(f)

    # ---- Fix 1: Richardson diagnostic, corrected marginal-to-marginal pairing ----
    crossing_cpl40_B = results["item_i"]["B"]["crossing_cpl40"]
    crossing_cpl40_C = results["item_i"]["C"]["crossing_cpl40"]

    theta_cpl30_B = m.THETA0_B + m.SHIFT_20_30_B
    shift_30_40_B = (crossing_cpl40_B - theta_cpl30_B) if crossing_cpl40_B is not None else None
    richardson_B = m.richardson_style_diagnostic(m.SHIFT_20_30_B, shift_30_40_B)

    theta_cpl30_C = m.THETA0_C + m.SHIFT_20_30_C
    shift_30_40_C = (crossing_cpl40_C - theta_cpl30_C) if crossing_cpl40_C is not None else None
    richardson_C = m.richardson_style_diagnostic(m.SHIFT_20_30_C, shift_30_40_C)

    richardson_A = dict(available=False, note="no cpl=30 counterpart on file for null A (theta0=37.127246deg)")

    print(f"[Fix 1] Richardson B (corrected): {richardson_B}")
    assert abs(richardson_B["observed_ratio"] - 0.7765163757372424) < 1e-9, "Richardson fix did not reproduce Red Team's independently-verified figure"
    results["richardson_diagnostic"] = dict(A=richardson_A, B=richardson_B, C=richardson_C)

    # ---- Fix 7: FI-G'' (native_ny corruption), executed ----
    fi_g_double_prime = m.run_fi_g_double_prime()
    print(f"[Fix 7] FI-G'': all_caught={fi_g_double_prime['all_caught']}  "
          f"y_lo_independent_of_corruption={fi_g_double_prime['y_lo_independent_of_corruption']}")
    assert fi_g_double_prime["all_caught"]
    assert fi_g_double_prime["y_lo_independent_of_corruption"]
    results["item_iv"]["fi_g_double_prime"] = fi_g_double_prime

    # ---- Fix 5: Idealization 47, registration gate re-run against reused points ----
    reused_preflight = m.registration_preflight([38.49, 38.69])
    print(f"[Fix 5] reused-points registration gate: all_clean={reused_preflight['all_clean']}")
    assert reused_preflight["all_clean"]
    results["item_ii"]["reused_points_registration_check"] = reused_preflight

    # ---- Fix 3: row-count vs call-count, code-enforced (new standing rule) ----
    n_rows_new = (len(results["item_i"]["A"]["angles"]) + len(results["item_i"]["B"]["angles"])
                  + len(results["item_i"]["C"]["angles"]) + len(results["item_ii"]["new_angles"]))
    n_rows_total_incl_reused = n_rows_new + len(results["item_ii"]["reused_angles_from_exp095"])
    assert n_rows_new == 16 and n_rows_total_incl_reused == 18
    assert results["fdtd_calls"] == n_rows_new * 4, "call-count/row-count invariant failed"
    results["n_rows_new"] = n_rows_new
    results["n_rows_total_incl_reused"] = n_rows_total_incl_reused
    results["netd_row_coverage_assert"] = (
        f"PASS -- all {n_rows_total_incl_reused} distinct report rows ({n_rows_new} new, "
        f"backed by {results['fdtd_calls']} real FDTD calls, plus 2 reused from exp-095) carry all 10 keys"
    )
    print(f"[Fix 3] n_rows_new={n_rows_new}  n_rows_total_incl_reused={n_rows_total_incl_reused}  "
          f"fdtd_calls={results['fdtd_calls']}")

    # ---- Fix 2: GP2' exact VALID/MARGINAL/INVALID counts in the flagged band, for the record ----
    gp2_curve = results["item_v"]["gp2_curve"]
    band = [r for r in gp2_curve if 50.5 <= r["theta"] <= 89.5]
    valid_in_band = sorted(r["theta"] for r in band if r["classification"] == "VALID")
    marginal_in_band = sorted(r["theta"] for r in band if r["classification"] == "MARGINAL")
    tail = [r for r in gp2_curve if 74.0 <= r["theta"] <= 89.5]
    tail_valid = [r for r in tail if r["classification"] == "VALID"]
    print(f"[Fix 2] band [50.5,89.5]: {len(valid_in_band)} VALID {valid_in_band}, {len(marginal_in_band)} MARGINAL; "
          f"tail [74,89.5]: {len(tail)} points, {len(tail_valid)} VALID (0 = no recovery)")
    assert len(valid_in_band) == 9 and len(tail_valid) == 0, "GP2' band recount mismatch vs Phase-5 Red Team audit"
    results["item_v"]["gp2_band_exact_counts"] = dict(
        band="[50.5,89.5]deg", valid_thetas=valid_in_band, n_valid=len(valid_in_band),
        n_marginal=len(marginal_in_band), n_invalid=0,
        tail_band="[74.0,89.5]deg", tail_n_points=len(tail), tail_n_valid=len(tail_valid),
        correction_note=(
            "Result's original 'flags MARGINAL continuously... the ENTIRE upper half' overclaimed -- "
            f"{len(valid_in_band)} VALID points are interspersed (incl. theta=69.5deg, itself inside "
            "the exp-086 corroboration band), and the 74-89.5deg tail shows 0 recovery (0/{0} VALID), "
            "a shape divergence from exp-086's own trend never surfaced in the original Result text."
        ).format(len(tail)),
    )

    # ---- Fix 8: GP2'/exp-086 "same formula, not independent instruments" disclosure ----
    results["gp2_vs_exp086_disclosure"] = (
        "GP2' and exp-086's own ptp method are two post-processing statistics computed from the "
        "IDENTICAL closed-form formula (edge_diffraction_c_empty_corrected), not independent "
        "physical instruments -- their agreement corroborates the same underlying model behavior "
        "read two ways, not two separate measurements of reality (QUANTUM OPTICS, Phase-5 finding, "
        "adopted by Red Team)."
    )

    # ---- Fix 4: GP1 framing correction ----
    results["gp1_framing_correction"] = (
        "GP1 is a non-negativity check on a windowed Poynting-flux component, motivated by the "
        "absence of any gain mechanism in this source-driven construction -- not a direct corollary "
        "of Poynting's/passivity theorems applied to this specific window (those bound NET flux "
        "through a closed surface, not one windowed local vector component in an interference "
        "pattern, where local backflow is ordinary). The PASS result is correct; the original "
        "'hard passivity floor' language oversold its derivation (ELECTROMAGNETISM self-review, "
        "adopted by Red Team)."
    )

    results["phase5_same_shift_fixes_applied"] = [
        "1. Richardson diagnostic corrected: marginal-to-marginal pairing (was cumulative/marginal)",
        "2. GP2' Result overclaim corrected: exact VALID/MARGINAL counts added (gp2_band_exact_counts)",
        "3. Row-count vs call-count: n_rows_new/n_rows_total_incl_reused added, code-enforced invariant asserted",
        "4. GP1 framing corrected: gp1_framing_correction field added",
        "5. Idealization 47: reused-points registration gate actually executed (item_ii.reused_points_registration_check)",
        "6. Banner placement: fixed directly in NOTES.md (no results.json field)",
        "7. FI-G'' executed: item_iv.fi_g_double_prime",
        "8. GP2'/exp-086 disclosure added: gp2_vs_exp086_disclosure",
    ]

    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(results, f, indent=2, default=str)
    print("\nresults.json updated with Phase-5 same-shift fixes.")


if __name__ == "__main__":
    main()
