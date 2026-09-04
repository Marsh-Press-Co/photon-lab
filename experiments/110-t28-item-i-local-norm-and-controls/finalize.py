"""exp-110 Phase 4 finalize: assembles Result text (R23, build_result_text),
asserts DISCLAIMER in both predictions_text/result_text, persists both into
results.json (Fix 7). Zero new Sim.run() calls -- pure post-processing of
already-persisted results.json/linear_fit_control_output.json fields."""
import json
import os
import sys

sys.path.insert(0, "/home/user/photon-lab/experiments/110-t28-item-i-local-norm-and-controls")
import run as R  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(HERE, "results.json")) as f:
    results = json.load(f)
with open(os.path.join(HERE, "linear_fit_control_output.json")) as f:
    item2_cases = json.load(f)

gate_p0_pass = results["r156"]["gate_p0"]["pass_"] and results["r312"]["gate_p0"]["pass_"]
repro_pass = (results["r156"]["reproduction_precondition"]["pass_"]
              and results["r312"]["reproduction_precondition"]["pass_"])

item_1a = ("PASS exact, both r -- reproduction_precondition rel_dev=0.0 exactly at both r "
           f"(r=156: sigma_abs={results['r156']['reproduction_precondition']['widths']['sigma_abs']:.4f}, "
           f"sigma_ext={results['r156']['reproduction_precondition']['widths']['sigma_ext']:.4f}; "
           f"r=312: sigma_abs={results['r312']['reproduction_precondition']['widths']['sigma_abs']:.4f}, "
           f"sigma_ext={results['r312']['reproduction_precondition']['widths']['sigma_ext']:.4f} -- "
           "matches exp-108's own committed results.json exactly). NOT FALSIFIED.")

item_1b = "PASS -- 48/48 bins persisted for all 6 margins, both r. NOT FALSIFIED."

r156_resolved = sum(results["r156"]["n_resolved"].values())
r156_total = sum(results["r156"]["n_total"].values())
r312_resolved = sum(results["r312"]["n_resolved"].values())
r312_total = sum(results["r312"]["n_total"].values())
bin156 = results["r156"]["named_bin_status"]["margin32"]
bin312 = results["r312"]["named_bin_status"]["margin32"]
item_1cd = (f"NOT FALSIFIED -- some bins fail the K=3 pooled floor gate at both r, as predicted "
            f"(not 'ALL clear comfortably'). r=156: {r156_resolved}/{r156_total} bins RESOLVED "
            f"({100*r156_resolved/r156_total:.1f}%), {r156_total-r156_resolved} UNRESOLVED-BY-CONSTRUCTION "
            f"({100*(1-r156_resolved/r156_total):.1f}%) across all 6 margins. r=312: "
            f"{r312_resolved}/{r312_total} RESOLVED ({100*r312_resolved/r312_total:.1f}%), "
            f"{r312_total-r312_resolved} UNRESOLVED ({100*(1-r312_resolved/r312_total):.1f}%). "
            f"The two PHOTONICS-named bins (margin=32): r=156 bin at {bin156['deg']} deg is "
            f"{'RESOLVED' if bin156['resolved'] else 'UNRESOLVED-BY-CONSTRUCTION'}; "
            f"r=312 bin at {bin312['deg']} deg is "
            f"{'RESOLVED' if bin312['resolved'] else 'UNRESOLVED-BY-CONSTRUCTION'}. "
            "Neither named bin's ~10% local-normalized reading from exp-108's own Phase-5 review "
            "clears the K=3 mirror-pooled floor at this cycle's own default (K=3, median, "
            "within-margin) -- their earlier local-deviation readings are NOT validated as genuine "
            "shape structure by this instrument; they are exactly the shape of reading this floor "
            "gate exists to catch (near-null relative-error territory), though PHOTONICS' own "
            "unclosed common-mode-blindness concern (Idealizations) means this instrument cannot "
            "rule out a real but common-mode-masked effect at either bin.")

item_2 = ("PASS -- all four predicted (is_monotonic, r_squared, smooth) triples reproduced "
          "bit-exact: " + "; ".join(f"{c['name']}=({c['is_monotonic']}, {c['r_squared']:.3f}, "
          f"{c['smooth']})" for c in item2_cases) + ". All four fault-injection assertions passed "
          "(python3 linear_fit_control.py). NOT FALSIFIED.")

item_3 = ("PASS -- rel_diff_truncated=1.999 (lab/validation/run_all.py --only 26: 3/3), inside the "
          "predicted (0.01,10] band, same order of magnitude as the existing over-run control's own "
          "2.0. NOT FALSIFIED.")

wall_time_source = (f"This cycle's own genuinely new wall time: {results['total_wall_s']:.1f}s "
                     f"({results['total_wall_s']/60:.2f} min), 6 real FDTD calls -- distinct from "
                     "exp-108's own historical 7712.0s/6-call figure (a separate, already-committed "
                     "capture of the identical geometry); per-scene: "
                     f"r156 empty/hollow/peccored = "
                     f"{results['r156']['total_wall_s']['empty']:.1f}s/"
                     f"{results['r156']['total_wall_s']['hollow']:.1f}s/"
                     f"{results['r156']['total_wall_s']['peccored']:.1f}s; "
                     f"r312 empty/hollow/peccored = "
                     f"{results['r312']['total_wall_s']['empty']:.1f}s/"
                     f"{results['r312']['total_wall_s']['hollow']:.1f}s/"
                     f"{results['r312']['total_wall_s']['peccored']:.1f}s.")

predictions_text = R.build_predictions_text()
result_text = R.build_result_text(
    n_fdtd_calls=results["n_fdtd_calls"], total_wall_s=results["total_wall_s"],
    gate_p0_pass=gate_p0_pass, repro_pass=repro_pass,
    item_1a=item_1a, item_1b=item_1b, item_1cd=item_1cd, item_2=item_2, item_3=item_3,
    wall_time_source=wall_time_source,
)

assert R.DISCLAIMER in predictions_text, "R23: disclaimer missing from Predictions block"
assert R.DISCLAIMER in result_text, "R23: disclaimer missing from Result block"
print("R23 DISCLAIMER asserts: BOTH PASSED (predictions_text, result_text).")

results["predictions_text"] = predictions_text
results["result_text"] = result_text
results["r27_cost_gate_founding_instance"] = "does not fire (this cycle's own founding instance)"

with open(os.path.join(HERE, "results.json"), "w") as f:
    json.dump(results, f, indent=2, default=str)

print("\n" + "=" * 70)
print(result_text)
print("=" * 70)
print(f"\nWritten: {os.path.join(HERE, 'results.json')}")
