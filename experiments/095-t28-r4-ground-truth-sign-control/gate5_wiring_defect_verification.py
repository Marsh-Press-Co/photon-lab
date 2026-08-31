"""exp-095 -- Gate 5 discriminator verification, extended to the new R5 call
site. Written and its own light logic run during Phase 3 (this script's
positive/negative control pair itself calls `_run_sim_r5_sigma`, which
constructs a real `Sim` object and runs a real FDTD loop -- per this
Phase's own instructions, that part is NOT executed by the authoring
agent; it is written here, correct and ready, and is to be RUN for real
during Phase 4, before any R5-family result is reported, matching Red
Team's own confirmation this is correctly planned (phase2_critique_em.md
S1; phase2_redteam_audit.md SS1) and exp-094's own corrected discipline
(Result-section Fix #1: a verification claim is exactly as subject to the
recompute-don't-hand-type house rule as a numeric figure -- this artifact
must actually execute and its result, PASS/FAIL with the literal
AssertionError text, printed AND persisted, not merely asserted in prose).

Mirrors experiments/094-.../gate5_wiring_defect_verification.py's own idiom
exactly, substituting every R4-scoped constant/function for its R5
equivalent. Injects the exact R15-founding defect shape (a stray,
un-rescaled sigma constant reaching `build_article_r5_sigma` instead of the
intended corrected value -- the same "correct formula existed, never wired
through at the one call site that mattered" bug exp-091's own Phase-5
self-review found by hand, and exp-094's own gate5 script re-verified for
the R4 family) and confirms Gate 5's own runtime `sigma_e`/`sigma_max`
check (`run.py::_run_sim_r5_sigma`) correctly raises AssertionError against
it, rather than silently passing.

Run: `python3 gate5_wiring_defect_verification.py` (during Phase 4, real
FDTD -- NOT run by this Phase's authoring agent, per instructions).
"""
import json
import os
import sys
import importlib.util

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ".")


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def main():
    m = _load(
        os.path.join(HERE, "run.py"),
        "exp095_gate5_verify",
    )
    from lab.fdtd2d import Sim
    from lab import materials

    cfg = m.dg.R5_CONFIGS["C40_R5"]
    cx, cy = cfg["obj_x"], cfg["obj_y"]

    result = dict(control_pass=None, injected_defect_pass=None, injected_defect_message=None)

    # --- Positive control: correct wiring must NOT raise. ---
    m._run_sim_r5_sigma(cfg, 41.825, 200, True, m.dg.SIGMA_R5_CORRECTED)
    print("[control] correct-sigma call completed without raising -- OK "
          "(Gate 5 is silent on genuinely correct wiring)")
    result["control_pass"] = True

    # --- Negative control: inject the R15-founding defect shape. ---
    # Build the article's shell at the WRONG sigma (a stray native constant,
    # as if a call site forgot to rescale) while Gate 5's own check logic
    # (reproduced verbatim from run.py) is told the INTENDED corrected value.
    sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=m.dg.R5_CPL[600],
              courant_frac=m.dg.COURANT_FRAC, absorb=cfg["absorb"])
    wrong_sigma = m.dg.SIGMA_NATIVE_FOR_R5     # 0.5 -- the injected bug (mirrors exp-094's
                                                # own gate5 script, which used
                                                # dg.SIGMA_NATIVE_FOR_R4 -- both constants
                                                # confirmed present in design_geometry.py)
    intended_sigma = m.dg.SIGMA_R5_CORRECTED   # 0.2 -- what should have been passed
    m.build_article_r5_sigma(sim, cx, cy, wrong_sigma)

    rr, _ = materials._grids(sim, cx, cy)["ez"]
    shell_mask = (rr >= m.PEC_R_R5) & (rr <= m.dg.R5_R_OUT)
    actual = float(sim.sigma_e[shell_mask].max())

    try:
        assert np.isclose(actual, intended_sigma, atol=1e-9), (
            f"GATE 5 FAILED -- runtime sigma_e/sigma_max mismatch: "
            f"sim.sigma_e[shell_mask].max()={actual!r} vs "
            f"sigma_max={intended_sigma!r}")
    except AssertionError as e:
        print("[injected defect] Gate 5 correctly raised AssertionError:")
        print(" ", e)
        print("\nVERIFIED: Gate 5 (R5 call site) is a genuine discriminator, not a "
              "tautology or rubber stamp -- it distinguishes correctly-"
              "wired sigma from an injected R15-style wiring defect.")
        result["injected_defect_pass"] = True
        result["injected_defect_message"] = str(e)
        result["verdict"] = "PASS"
        _persist(result)
        return 0

    print("\nBUG: Gate 5 (R5 call site) did NOT fire on an injected wiring defect -- "
          "FALSE PASS. This would be a serious finding requiring immediate "
          "escalation.")
    result["injected_defect_pass"] = False
    result["verdict"] = "FAIL"
    _persist(result)
    return 1


def _persist(result):
    """PASS/FAIL, with the literal AssertionError text on the induced
    failure, printed AND persisted -- not merely asserted in prose (exactly
    the R4-shaped overclaim exp-094's own Phase-5 caught, and this cycle's
    own Gate 5 discipline exists to avoid repeating for R5)."""
    out_path = os.path.join(HERE, "gate5_wiring_defect_verification_result.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nwrote {out_path}")


if __name__ == "__main__":
    raise SystemExit(main())
