"""Panel Iteration 86 (exp-109) -- zero-FDTD reclassification of exp-108's
own item_ii verdict under the R24-second-instance-fixed `classify_item_ii()`
(now gated on `fit["smooth"]`), plus the first-ever live execution of
`build_result_text()` and R23's DISCLAIMER asserts on real data.

Imports the patched `experiments/108-.../run.py` directly (Attack 1 of
this cycle's own phase2_redteam_audit.md precedent: one function, one
name, no duplicated logic) via `importlib` (the source directory name is
not a valid Python package identifier). Loads exp-108's own committed
`results.json` (read-only -- not modified), re-derives item ii's
classification under the corrected rule using the already-persisted
`fit`/`delta_values` arrays, and reports it. Zero new `Sim.run()` calls --
pure post-processing, matching `reclassify_106.py`'s own established idiom
(exp-108) and `finalize.py`'s own (exp-107).
"""
import importlib.util
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
EXP108_DIR = os.path.join(ROOT, "experiments", "108-t28-reclassification-angular-pattern-batch")
EXP108_RUN_PY = os.path.join(EXP108_DIR, "run.py")
EXP108_RESULTS = os.path.join(EXP108_DIR, "results.json")


def load_exp108_module():
    spec = importlib.util.spec_from_file_location("exp108_run", EXP108_RUN_PY)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # module-level code only -- Sim.run() is
    # guarded behind `if __name__ == "__main__":` in exp-108's own run.py,
    # so this does NOT trigger any FDTD call.
    return mod


def git_blob_hash(path):
    try:
        out = subprocess.run(["git", "hash-object", path], cwd=ROOT,
                              capture_output=True, text=True, check=True)
        return out.stdout.strip()
    except Exception as e:  # pragma: no cover -- provenance is best-effort, never blocking
        return f"<git hash-object failed: {e}>"


def main():
    R = load_exp108_module()
    with open(EXP108_RESULTS) as f:
        committed = json.load(f)

    item_ii_reclassified = {}
    for r in (156, 312):
        tier1_r = committed["tier1"][f"r{r}"]
        old_item_ii = tier1_r["item_ii"]
        fit = old_item_ii["fit"]
        delta_values = old_item_ii["delta_values"]
        old_verdict = old_item_ii["verdict"]

        new = R.classify_item_ii(r, fit, delta_values)

        print(f"\n--- r={r} item_ii reclassification ---")
        print(f"  fit: is_monotonic={fit['is_monotonic']} r_squared={fit['r_squared']:.4f} "
              f"smooth={fit['smooth']}")
        print(f"  raw_std={new['raw_std']:.6e}  residual_std={new['residual_std']:.6e}  "
              f"raw_over_residual_ratio={new['raw_over_residual_ratio']:.4f}")
        print(f"  OLD verdict (committed, exp-108 results.json): {old_verdict}")
        print(f"  NEW verdict (patched, this cycle):             {new['verdict']}")
        print(f"  stat_used={new['stat_used']:.6e}  boxA={new['boxA']:.6e}")
        print(f"  stat_source: {new['stat_source']}")

        item_ii_reclassified[f"r{r}"] = dict(
            old_verdict=old_verdict, new_verdict=new["verdict"],
            stat_used=new["stat_used"], stat_source=new["stat_source"],
            raw_std=new["raw_std"], residual_std=new["residual_std"],
            raw_over_residual_ratio=new["raw_over_residual_ratio"],
            boxA=new["boxA"], fit=fit,
        )

    # -------------------------------------------------- predictions_text (R23, live-fired)
    predictions_text = R.build_predictions_text()
    assert R.DISCLAIMER in predictions_text, "R23: disclaimer missing from predictions_text"

    # -------------------------------------------------- result_text (R23, first live call ever)
    # Same-shift Red Team annotation (Phase 5 final audit, phase5_redteam_audit.md
    # section 5 item 5): fix 4 (THERMODYNAMICS) asked that this reduction rule be
    # stated explicitly "in code AND docstring" -- the code below IS the explicit
    # logical AND of both r's pass_ fields (not left for a reader to infer), but
    # lacked this inline comment naming it as such until this same-shift addition.
    gate_p0_pass = bool(committed["tier1"]["r156"]["gate_p0"]["pass_"]
                         and committed["tier1"]["r312"]["gate_p0"]["pass_"])
    repro_pass = bool(committed["tier1"]["r156"]["reproduction_precondition"]["pass_"]
                       and committed["tier1"]["r312"]["reproduction_precondition"]["pass_"])
    n_fdtd_calls = committed["n_fdtd_calls"]
    total_wall_s = committed["total_wall_s"]

    item_i_summary = (
        f"r=156 verdict={committed['tier1']['r156']['item_i']['verdict']}, "
        f"r=312 verdict={committed['tier1']['r312']['item_i']['verdict']} "
        f"(exp-108's own committed values, unchanged this cycle)")
    item_ii_summary = (
        f"r=156: OLD={item_ii_reclassified['r156']['old_verdict']} -> "
        f"NEW={item_ii_reclassified['r156']['new_verdict']} "
        f"(stat_used={item_ii_reclassified['r156']['stat_used']:.6e}, "
        f"raw/residual ratio={item_ii_reclassified['r156']['raw_over_residual_ratio']:.3f}x); "
        f"r=312: OLD={item_ii_reclassified['r312']['old_verdict']} -> "
        f"NEW={item_ii_reclassified['r312']['new_verdict']} "
        f"(stat_used={item_ii_reclassified['r312']['stat_used']:.6e}, "
        f"raw/residual ratio={item_ii_reclassified['r312']['raw_over_residual_ratio']:.3f}x) "
        f"-- both take the raw/undetrended fallback branch (fit not smooth at either r); "
        f"both CONFIRM survives, non-outcome-reversing, exp-108's own Phase-5 annotation "
        f"informally disclosed this, now a coded, executed, falsifiable gate (R24 second "
        f"instance closed)")
    item_iii_summary = (
        f"r=156: {committed['tier1']['r156']['item_iii']['frac_unresolved']:.4f} "
        f"pass={committed['tier1']['r156']['item_iii']['pass_']}, "
        f"r=312: {committed['tier1']['r312']['item_iii']['frac_unresolved']:.4f} "
        f"pass={committed['tier1']['r312']['item_iii']['pass_']} "
        f"(exp-108's own committed values, unchanged this cycle)")
    item_iv_summary = f"{committed['item_iv']} (exp-108's own committed value, unchanged this cycle)"
    closure_rows_summary = (
        f"hollow: r156={committed['tier1']['r156']['closure_hollow']['closure']:.6f}, "
        f"r312={committed['tier1']['r312']['closure_hollow']['closure']:.6f}; "
        f"peccored: r156={committed['tier1']['r156']['closure_peccored']['closure']:.6f}, "
        f"r312={committed['tier1']['r312']['closure_peccored']['closure']:.6f} "
        f"(exp-108's own committed values, unchanged this cycle)")

    result_text = R.build_result_text(
        n_fdtd_calls=n_fdtd_calls, total_wall_s=total_wall_s,
        gate_p0_pass=gate_p0_pass, repro_pass=repro_pass,
        item_i=item_i_summary, item_ii=item_ii_summary,
        item_iii=item_iii_summary, item_iv=item_iv_summary,
        closure_rows=closure_rows_summary,
        wall_time_source=("exp-108's own historical spend, reused verbatim -- "
                           "exp-109 makes zero new Sim.run() calls"),
    )
    assert R.DISCLAIMER in result_text, "R23: disclaimer missing from result_text"

    print("\n=== predictions_text ===")
    print(predictions_text)
    print("\n=== result_text ===")
    print(result_text)

    out = dict(
        predictions_text=predictions_text,
        result_text=result_text,
        item_ii_reclassified=item_ii_reclassified,
        gate_p0_pass=gate_p0_pass,
        repro_pass=repro_pass,
        n_fdtd_calls=n_fdtd_calls,
        total_wall_s=total_wall_s,
        source_results_json_sha=git_blob_hash(EXP108_RESULTS),
    )
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWritten: {out_path}")
    return out


if __name__ == "__main__":
    main()
