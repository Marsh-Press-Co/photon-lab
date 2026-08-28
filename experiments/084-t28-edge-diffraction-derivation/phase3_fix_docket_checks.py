"""
experiments/084-t28-edge-diffraction-derivation/phase3_fix_docket_checks.py
============================================================================
Panel Iteration 61 (exp-084), Phase 3. Director-run script committing to
code (R4 discipline: never hand-type a figure quoted in a permanent
record) the two numbers Red Team's Phase-2 audit (`phase2_redteam_audit.md`
Sec 2.1/2.2) independently derived and that Phase 3's synthesis now cites
as the basis for downgrading leg (a) from SUPPORT to INCONCLUSIVE and for
crediting the shape-correlation finding. Reuses `phase1_derivation.py`'s
own functions unchanged -- does not reimplement the diffraction physics.

[A] Shape-correlation finding (fix-docket item 5): corr(leg_a_curve,
    real FDTD C80(theta)), control-tested against three unrelated curves
    sampled at the identical 31-point grid.
[B] Circular-shift null-under-noise test (fix-docket item 1): the
    program's own established "harder companion" null (LOGBOOK Iteration
    60's own circular-shift precedent), run against the literal
    production fitting pipeline (`free_period_with_widening`), on the
    real committed leg (a) curve.

Zero new FDTD calls. Output written to
`phase3_fix_docket_results.json` and printed verbatim below.
"""

import importlib.util
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


deriv = _load(os.path.join(HERE, "phase1_derivation.py"), "_exp084_phase1_derivation")

EXP069_RESULTS = os.path.join(
    ROOT, "experiments", "069-t21-block-mini-period-match-power-up", "results.json"
)


def main():
    out = {}

    # ---------------------------------------------------------- [A]
    c_a = deriv.leg_a_curve()
    c_b_masked = deriv.leg_b_curve(mask_r_out=deriv.R_OUT)  # leg (b)'s OWN real output

    ref = json.load(open(EXP069_RESULTS))
    rows = ref["block_dense"]["rows"]
    thetas = np.array([r["theta"] for r in rows])
    assert np.allclose(thetas, deriv.DENSE_ANGLES)
    c80_real = np.array([r["C_empty_C80"] for r in rows])

    def corr(a, b):
        return float(np.corrcoef(a, b)[0, 1])

    x = deriv.DENSE_ANGLES
    linear_ramp = x - np.mean(x)
    quadratic = (x - np.mean(x)) ** 2
    quadratic = quadratic - np.mean(quadratic)

    controls = {
        "leg_a_vs_real_C80 (the finding)": corr(c_a, c80_real),
        "leg_b_own_masked_output_vs_real_C80 (control)": corr(c_b_masked, c80_real),
        "bare_linear_ramp_vs_real_C80 (control)": corr(linear_ramp, c80_real),
        "bare_quadratic_vs_real_C80 (control)": corr(quadratic, c80_real),
    }
    out["shape_correlation"] = controls
    print("[A] SHAPE CORRELATION vs the real FDTD C80(theta) empty-scene curve")
    for k, v in controls.items():
        print(f"    {k:46s} r = {v:+.6f}")

    # ---------------------------------------------------------- [B]
    _out_list = []
    fit0 = deriv.free_period_with_widening(deriv.DENSE_ANGLES, c_a, "leg_a_observed", _out_list)
    p_model, r2, window = fit0["p_star_deg"], fit0["r_squared"], fit0["window"]
    assert abs(p_model - 2.533834586466165) < 1e-9
    assert abs(r2 - 0.36965580905914364) < 1e-9

    n = len(c_a)
    shift_r2 = []
    for s in range(1, n):
        shifted = np.roll(c_a, s)
        fit_s = deriv.free_period_with_widening(deriv.DENSE_ANGLES, shifted, f"shift{s}", [])
        shift_r2.append(fit_s["r_squared"])
    shift_r2 = np.array(shift_r2)
    n_meet_or_exceed = int(np.sum(shift_r2 >= r2))
    frac = n_meet_or_exceed / len(shift_r2)

    out["circular_shift_null"] = dict(
        observed_r2=r2,
        observed_p_model_deg=p_model,
        window=window,
        n_shifts=len(shift_r2),
        n_meet_or_exceed=n_meet_or_exceed,
        fraction_meet_or_exceed=frac,
        mean_shift_r2=float(np.mean(shift_r2)),
        max_shift_r2=float(np.max(shift_r2)),
        min_shift_r2=float(np.min(shift_r2)),
    )
    print()
    print("[B] CIRCULAR-SHIFT NULL TEST (program's own 'harder companion',"
          " full production pipeline, free_period_with_widening)")
    print(f"    observed: P*={p_model:.4f}deg  R^2={r2:.6f}  window={window}")
    print(f"    {n_meet_or_exceed}/{len(shift_r2)} = {frac:.1%} of circular shifts"
          f" meet or exceed the observed R^2")
    print(f"    null distribution: mean={np.mean(shift_r2):.4f}"
          f" max={np.max(shift_r2):.4f} min={np.min(shift_r2):.4f}")
    print()
    print("    -> matches Red Team's phase2_redteam_audit.md Sec 2.2 exactly"
          " (15/30 = 50.0%)" if n_meet_or_exceed == 15 else
          "    -> DOES NOT MATCH Red Team's cited 15/30 -- investigate before citing")

    json.dump(out, open(os.path.join(HERE, "phase3_fix_docket_results.json"), "w"),
               indent=2)
    print()
    print("results written to phase3_fix_docket_results.json")


if __name__ == "__main__":
    main()
