"""exp-110 item 2: R18 fault-injection control for linear_fit_1_over_margin's
own smooth/noise discriminator (never itself validated before this cycle).
Four deterministic synthetic 6-point sequences at the real MARGINS, zero
Sim.run() calls anywhere, isolating both arms of the is_monotonic OR
r_squared>=R2_SMOOTH_THRESHOLD gate. Panel Iteration 87.

P1 -- exact trend, zero noise (both arms True).
P2 -- monotonic, poor 1/margin fit (isolates the monotonic arm alone).
P3 -- non-monotonic, good fit (isolates the R^2 arm alone).
N1 -- non-monotonic, poor fit (negative control -- must read smooth=False).
"""
import json
import os

import numpy as np

import run as R

MARGINS = R.MARGINS  # (24, 32, 40, 48, 57, 65)


def p1_sequence():
    A, B = -1.5e-5, -4.0e-4
    return [A + B / m for m in MARGINS]


def p2_sequence():
    return [1e-9 * np.exp(m / 6.0) for m in MARGINS]


def p3_sequence():
    seq = p1_sequence()
    seq = list(seq)
    seq[2] = seq[2] + 3.0e-6  # perturb margin=40 (index 2)
    return seq


def n1_sequence():
    amp = 3.0e-6
    return [amp, -amp, amp, -amp, amp, -amp]


def run_case(name, y):
    fit = R.linear_fit_1_over_margin(MARGINS, y)
    return dict(name=name, y=y, is_monotonic=fit["is_monotonic"],
                r_squared=fit["r_squared"], residual_std=fit["residual_std"],
                smooth=fit["smooth"])


if __name__ == "__main__":
    cases = [
        run_case("P1", p1_sequence()),
        run_case("P2", p2_sequence()),
        run_case("P3", p3_sequence()),
        run_case("N1", n1_sequence()),
    ]
    for c in cases:
        print(f"{c['name']}: is_monotonic={c['is_monotonic']} r_squared={c['r_squared']:.4f} "
              f"residual_std={c['residual_std']:.4e} smooth={c['smooth']}")

    # ---- assertions: P1/P2/P3 must all read smooth=True (isolating each OR-arm);
    # N1 must read smooth=False (negative control -- the gate must discriminate)
    assert cases[0]["is_monotonic"] is True and cases[0]["smooth"] is True, "P1 (exact trend) must be smooth"
    assert cases[1]["is_monotonic"] is True and cases[1]["r_squared"] < R.R2_SMOOTH_THRESHOLD and cases[1]["smooth"] is True, \
        "P2 must isolate the monotonic arm (poor R^2, still smooth via monotonicity)"
    assert cases[2]["is_monotonic"] is False and cases[2]["r_squared"] >= R.R2_SMOOTH_THRESHOLD and cases[2]["smooth"] is True, \
        "P3 must isolate the R^2 arm (non-monotonic, still smooth via R^2>=0.90)"
    assert cases[3]["is_monotonic"] is False and cases[3]["smooth"] is False, \
        "N1 (negative control) must read smooth=False -- the gate must discriminate real noise"
    print("\nAll four fault-injection assertions PASSED.")

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "linear_fit_control_output.json")
    with open(out_path, "w") as f:
        json.dump(cases, f, indent=2)
    print(f"Written: {out_path}")
