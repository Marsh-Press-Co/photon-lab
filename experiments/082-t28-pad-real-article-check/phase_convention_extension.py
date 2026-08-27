"""exp-082 -- Tier 1 item 4: extend the empirical FDTD phase-convention
tie-breaker to 2-3 angles inside [47.5,54.5]deg.
=============================================================================
PLAN.md Iteration-59 queue, Tier 1 item 4 (near-unanimous top pick: EM #1,
QUANTUM #1, PHOTONICS #2, VISION #2, exp-081 phase5_redteam_audit.md Sec 6).
Mirrors experiments/075-.../phase5_redteam_phase_convention_check.py's own
[0,20,39]deg precedent EXACTLY -- same K=5-only reliable operating point
(the [CALIB] block there showed K>=8 develops an unexplained systematic
bias and is not relied upon), same construction, same algebra. This file
does not reimplement any of that machinery; it imports
phase5_redteam_phase_convention_check.py and calls its own measure_r/
committed_r/textbook_r functions at NEW theta values inside item 1's own
[47.5,54.5]deg construction range (exp-081), which the original check
never covered (its own range was [0,20,39]deg).

Genuinely new FDTD calls: 3 lossy cases (K=5, theta in {48,51,54}) + 3
calibration cases (K=5, same thetas) = 6 calls, ~90s total per the
original file's own docstring (K=5 only, not the full K in {5,8,10,20}
sweep the original ran for completeness).
"""

import importlib.util
import json
import math
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


EXP075_DIR = os.path.join(ROOT, "experiments", "075-t28-absorb-boundary-wkb-reflectance")
pcc = _load(os.path.join(EXP075_DIR, "phase5_redteam_phase_convention_check.py"), "_exp082_pcc")

NEW_THETAS = (48.0, 51.0, 54.0)   # inside [47.5,54.5]deg, item 1's own range
K_RELIABLE = 5


def main():
    out = {"calibration": [], "lossy": []}

    print("=" * 100)
    print("exp-082 Tier-1 item 4 -- phase-convention tie-breaker extended to "
          f"theta in {NEW_THETAS} (inside [47.5,54.5]deg), K={K_RELIABLE} only")
    print("=" * 100)

    print("\n[CALIB] Lossless (real n=1) spacer, K=5 -- |r_measured| must equal 1.0")
    for theta in NEW_THETAS:
        r_code = pcc.textbook_r(K_RELIABLE, theta)
        r_m, peak_ok = pcc.measure_r(K_RELIABLE, theta, gap=150, ny=420, n_steps=1800,
                                      custom_x_ramp_real=np.ones(K_RELIABLE))
        d_code = abs(r_m - r_code)
        d_conj = abs(r_m - np.conj(r_code))
        closer = "r" if d_code < d_conj else "conj(r)"
        print(f"  K={K_RELIABLE} theta={theta:5.1f}  code arg={math.degrees(np.angle(r_code)):+7.2f}deg | "
              f"measured |r|={abs(r_m):.4f} arg={math.degrees(np.angle(r_m)):+7.2f}deg  "
              f"peak_match={peak_ok}  closer_to={closer}")
        out["calibration"].append(dict(K=K_RELIABLE, theta=theta,
                                        code_arg_deg=math.degrees(np.angle(r_code)),
                                        measured_abs_r=abs(r_m), measured_arg_deg=math.degrees(np.angle(r_m)),
                                        peak_match=peak_ok, closer_to=closer))

    print("\n[LOSSY] Real ABSORB-band construction (cubic ramp), K=5 -- the actual question")
    for theta in NEW_THETAS:
        r_code, ramp = pcc.committed_r(K_RELIABLE, theta)
        r_m, peak_ok = pcc.measure_r(K_RELIABLE, theta, gap=150, ny=420, n_steps=1800,
                                      custom_x_ramp_real=ramp.real)
        d_code = abs(r_m - r_code)
        d_conj = abs(r_m - np.conj(r_code))
        closer = "r" if d_code < d_conj else "conj(r)"
        print(f"  K={K_RELIABLE} theta={theta:5.1f}  code |r|={abs(r_code):.4f} "
              f"arg={math.degrees(np.angle(r_code)):+7.2f}deg | measured |r|={abs(r_m):.4f} "
              f"arg={math.degrees(np.angle(r_m)):+7.2f}deg  peak_match={peak_ok}  "
              f"dev_r={d_code:.4f}  dev_conj={d_conj:.4f}  closer_to={closer}")
        out["lossy"].append(dict(K=K_RELIABLE, theta=theta, code_abs_r=abs(r_code),
                                  code_arg_deg=math.degrees(np.angle(r_code)),
                                  measured_abs_r=abs(r_m), measured_arg_deg=math.degrees(np.angle(r_m)),
                                  peak_match=peak_ok, dev_r=d_code, dev_conj=d_conj, closer_to=closer))

    n_r = sum(1 for c in out["calibration"] if c["closer_to"] == "r") + \
        sum(1 for c in out["lossy"] if c["closer_to"] == "r")
    calib_ok = all(abs(c["measured_abs_r"] - 1.0) < 0.15 for c in out["calibration"])
    print(f"\nSUMMARY: at K=5 inside [47.5,54.5]deg, {n_r}/6 sub-tests (3 calibration + 3 lossy) "
          f"favor the COMMITTED convention 'r'.")
    print(f"[CALIB] reliability check (|r_measured| close to 1.0, matching the original file's "
          f"own K=5 reliability finding): {calib_ok}")

    out["summary"] = dict(n_favor_r=n_r, n_total=6, calibration_reliable=calib_ok,
                           theta_range_deg=[47.5, 54.5])
    out_path = os.path.join(HERE, "phase_convention_extension_results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
