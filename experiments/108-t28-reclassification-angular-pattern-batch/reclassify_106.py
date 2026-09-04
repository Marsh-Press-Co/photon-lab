"""exp-108 Tier-0 item 1 -- zero-FDTD reclassification of exp-106's own
`item4_fixedabs` verdict under the corrected `classify_shape_ratio_fixedabs()`
logic (Panel Iteration 85, R25's own founding tripwire discharged).

Imports the patched, extracted function directly from
`experiments/106-t28-kappa-window-floor-fixedabs-control/run.py` (Attack 1,
exp-108 phase2_redteam_audit.md: one function, one name, no duplicated
logic) via `importlib` (the source directory name is not a valid Python
package identifier). Loads exp-106's own committed `results.json`,
re-derives `classification` under the corrected rule using the four
already-persisted scalars, and reports it. Zero new `Sim.run()` calls --
pure post-processing, matching `finalize.py`'s own established idiom
(exp-107).
"""
import importlib.util
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
EXP106_DIR = os.path.join(ROOT, "experiments", "106-t28-kappa-window-floor-fixedabs-control")
EXP106_RUN_PY = os.path.join(EXP106_DIR, "run.py")
EXP106_RESULTS = os.path.join(EXP106_DIR, "results.json")


def load_exp106_module():
    spec = importlib.util.spec_from_file_location("exp106_run", EXP106_RUN_PY)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # runs module-level code only -- main() is
    # guarded behind `if __name__ == "__main__":` in exp-106's own run.py,
    # so this does NOT trigger any Sim.run() call.
    return mod


def main():
    exp106 = load_exp106_module()
    with open(EXP106_RESULTS) as f:
        results = json.load(f)

    item4 = results["item4_fixedabs"]
    ledger_r156 = results["ledger_r156"]
    ledger_r312 = results["ledger_r312"]

    sr_fa = item4["shape_ratio"]
    noise_dominated = item4["noise_flag"]["noise_dominated"]
    trusted = item4["trusted"]
    p_abs_frac_diff_156 = ledger_r156["p_abs_frac_diff"]
    p_abs_frac_diff_312 = ledger_r312["p_abs_frac_diff"] if ledger_r312 is not None else None

    old_classification = item4["classification"]
    new_classification = exp106.classify_shape_ratio_fixedabs(
        sr_fa, noise_dominated, trusted, p_abs_frac_diff_156, p_abs_frac_diff_312)

    print("exp-106 reclassification (Panel Iteration 85, exp-108 Tier-0 item 1)")
    print(f"  shape_ratio_fixedabs        = {sr_fa}")
    print(f"  noise_dominated             = {noise_dominated}")
    print(f"  trusted                     = {trusted}")
    print(f"  p_abs_frac_diff_156         = {p_abs_frac_diff_156}")
    print(f"  p_abs_frac_diff_312         = {p_abs_frac_diff_312}")
    print(f"  OLD classification (committed, exp-106 results.json):\n    {old_classification}")
    print(f"  NEW classification (patched, this cycle):\n    {new_classification}")

    contains_three_way = "THREE-WAY-AMBIGUOUS" in new_classification
    print(f"  Contains 'THREE-WAY-AMBIGUOUS': {contains_three_way}  "
          f"(predicted True, exp-108 NOTES.md Sec Predictions, Tier 0 item 1)")

    unchanged_fields = dict(
        shape_ratio_fixedabs=sr_fa,
        noise_dominated=noise_dominated,
        trusted=trusted,
    )
    print(f"  Unchanged fields (bit-identical to exp-106's own results.json, as predicted): "
          f"{unchanged_fields}")

    out = dict(
        shape_ratio_fixedabs=sr_fa,
        noise_dominated=noise_dominated,
        trusted=trusted,
        p_abs_frac_diff_156=p_abs_frac_diff_156,
        p_abs_frac_diff_312=p_abs_frac_diff_312,
        old_classification=old_classification,
        new_classification=new_classification,
        contains_three_way_ambiguous=contains_three_way,
    )
    out_path = os.path.join(HERE, "reclassify_106_output.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWritten: {out_path}")
    return out


if __name__ == "__main__":
    main()
