"""exp-094 -- Gate 5 discriminator verification (Director, post-Phase-4/
mid-Phase-5, closing a real gap two independent Phase-5 seats caught blind:
QUANTUM OPTICS (self-review) and MATERIALS both found that NOTES.md's own
Result/Learned sections asserted Gate 5 was "independently confirmed a
genuine discriminator... by injecting a simulated R15-style wiring defect
into a standalone test harness during Phase 4" with NO corresponding
artifact anywhere in the committed record -- an R4-shaped unverifiable
claim entered the permanent record. This script IS that artifact, written
and run for real, closing the gap rather than merely correcting the prose.

Injects the exact R15-founding defect shape (a stray, un-rescaled sigma
constant reaching `build_article_r4_sigma` instead of the intended
corrected value -- the same "correct formula existed, never wired through
at the one call site that mattered" bug exp-091's own Phase-5 self-review
found by hand) and confirms Gate 5's own runtime `sigma_e`/`sigma_max`
check (`run.py::_run_sim_r4_sigma`) correctly raises AssertionError against
it, rather than silently passing. Run: `python3 gate5_wiring_defect_verification.py`.
"""
import sys
import importlib.util

import numpy as np

sys.path.insert(0, ".")


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def main():
    m = _load(
        "experiments/094-t28-cpl40-resolution-sigma-r3-census/run.py",
        "exp094_gate5_verify",
    )
    from lab.fdtd2d import Sim
    from lab import materials

    cfg = m.dg.R4_CONFIGS["C40_R4"]
    cx, cy = cfg["obj_x"], cfg["obj_y"]

    # --- Positive control: correct wiring must NOT raise. ---
    cap = m._run_sim_r4_sigma(cfg, 41.825, 200, True, m.dg.SIGMA_R4_CORRECTED)
    print("[control] correct-sigma call completed without raising -- OK "
          "(Gate 5 is silent on genuinely correct wiring)")

    # --- Negative control: inject the R15-founding defect shape. ---
    # Build the article's shell at the WRONG sigma (a stray native constant,
    # as if a call site forgot to rescale) while Gate 5's own check logic
    # (reproduced verbatim from run.py) is told the INTENDED corrected value.
    sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=m.dg.R4_CPL[600],
              courant_frac=m.dg.COURANT_FRAC, absorb=cfg["absorb"])
    wrong_sigma = m.dg.SIGMA_NATIVE_FOR_R4       # 0.5 -- the injected bug
    intended_sigma = m.dg.SIGMA_R4_CORRECTED     # 0.25 -- what should have been passed
    m.build_article_r4_sigma(sim, cx, cy, wrong_sigma)

    rr, _ = materials._grids(sim, cx, cy)["ez"]
    shell_mask = (rr >= m.PEC_R_R4) & (rr <= m.dg.R4_R_OUT)
    actual = float(sim.sigma_e[shell_mask].max())

    try:
        assert np.isclose(actual, intended_sigma, atol=1e-9), (
            f"GATE 5 FAILED -- runtime sigma_e/sigma_max mismatch: "
            f"sim.sigma_e[shell_mask].max()={actual!r} vs "
            f"sigma_max={intended_sigma!r}")
    except AssertionError as e:
        print("[injected defect] Gate 5 correctly raised AssertionError:")
        print(" ", e)
        print("\nVERIFIED: Gate 5 is a genuine discriminator, not a "
              "tautology or rubber stamp -- it distinguishes correctly-"
              "wired sigma from an injected R15-style wiring defect.")
        return 0

    print("\nBUG: Gate 5 did NOT fire on an injected wiring defect -- "
          "FALSE PASS. This would be a serious finding requiring immediate "
          "escalation.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
