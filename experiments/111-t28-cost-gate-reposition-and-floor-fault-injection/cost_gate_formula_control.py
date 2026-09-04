"""exp-111 -- Panel Iteration 88: formula-level fault-injection control for
cost_gate_check()'s recalibrated projection formula (Reconciled Iteration-88
Tier-1 item 4). Pure arithmetic, zero FDTD, zero mocking needed.

Three cases (phase1_proposal.md Sec 2.2, all mandatory-fix-4 verified):
  Positive       -- formula-arithmetic sanity on a unit input.
  Non-regression -- exp-110's own real committed r=156 pilot data still
                    PASSes under the new, stricter formula (an OVERestimate
                    of the real measured r=312 total, the opposite
                    direction from the old formula's UNDERestimate --
                    the fix's whole point).
  Discriminating -- a constructed near-boundary pilot_total_wall_s where
                    the old formula (exponent 3.0, no margin) PASSes and
                    the new formula (exponent 3.2053, x1.10 margin) FAILs.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "experiments", "110-t28-item-i-local-norm-and-controls"))

import run as R  # noqa: E402  (exp-110's own, patched this cycle)


def positive_case():
    gate = R.cost_gate_check(pilot_empty_wall_s=0.0, pilot_total_wall_s=1.0)
    predicted = 2.0 ** 3.2053299988171697 * 1.10
    ok = abs(gate["projected_312_total_s"] - predicted) < 1e-9
    return dict(case="positive", projected=gate["projected_312_total_s"], predicted=predicted, pass_=bool(ok))


def non_regression_case():
    pilot_empty = 250.6266098022461
    pilot_total = 752.2232966423035  # exp-110's own committed r=156 figures
    gate = R.cost_gate_check(pilot_empty_wall_s=pilot_empty, pilot_total_wall_s=pilot_total)
    predicted = 7632.027742505074
    ok = (abs(gate["projected_312_total_s"] - predicted) < 1e-6) and gate["total_pass"] and gate["pilot_pass"]
    real_measured_r312_total = 6938.207038640976  # exp-110's own real, already-captured figure
    overestimate = gate["projected_312_total_s"] - real_measured_r312_total
    old_formula_projection = pilot_total * (2.0 ** 3.0)  # exp-110's own old, unfixed formula
    old_underestimate = real_measured_r312_total - old_formula_projection
    return dict(case="non_regression", projected=gate["projected_312_total_s"], predicted=predicted,
                total_pass=gate["total_pass"], pass_=bool(ok),
                real_measured_r312_total=real_measured_r312_total,
                new_formula_overestimate_s=overestimate,
                old_formula_projection_s=old_formula_projection,
                old_formula_underestimate_s=old_underestimate)


def discriminating_case():
    pilot_total = 1349.875
    old_gate_equiv_projection = pilot_total * (2.0 ** 3.0)  # old formula, no margin
    old_pass = old_gate_equiv_projection < R.COST_GATE_TOTAL_S
    new_gate = R.cost_gate_check(pilot_empty_wall_s=0.0, pilot_total_wall_s=pilot_total)
    predicted_old = 10799.0
    predicted_new = 13695.778220666
    ok = (abs(old_gate_equiv_projection - predicted_old) < 1e-3
          and abs(new_gate["projected_312_total_s"] - predicted_new) < 1e-3
          and old_pass and not new_gate["total_pass"])
    return dict(case="discriminating", old_formula_projection_s=old_gate_equiv_projection,
                old_formula_pass=old_pass, new_formula_projection_s=new_gate["projected_312_total_s"],
                new_formula_pass=new_gate["total_pass"], pass_=bool(ok))


if __name__ == "__main__":
    results = dict(positive=positive_case(), non_regression=non_regression_case(),
                    discriminating=discriminating_case())
    for k, v in results.items():
        print(f"{k}: {json.dumps(v, default=str)}")
    out_path = os.path.join(HERE, "cost_gate_formula_control_output.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"Written: {out_path}")

    all_pass = all(v["pass_"] for v in results.values())
    print(f"\nALL CASES PASS: {all_pass}")
    assert all_pass, "cost_gate_formula_control: at least one case failed"
