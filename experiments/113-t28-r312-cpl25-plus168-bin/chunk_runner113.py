"""Checkpoint/resume runner for exp-113's own r=312/cpl=25 leg (3 scenes:
empty, hollow, peccored) -- Panel Iteration 90. Extends
experiments/112-.../chunk_runner112.py's own checkpoint/resume idiom
(foreground Bash calls only -- backgrounded/nohup execution confirmed
pathologically slow for sustained FDTD numpy work, exp-107's own
A/B-tested finding, reused without re-testing) with a time-BUDGETED
sub-chunk loop (--budget-s) so one foreground invocation can cover
several thousand steps without guessing a fixed step count that might
overrun a single call's own wall-clock ceiling -- checkpointed every
SUBSTEP so a mid-budget interruption loses at most one substep.

Also hosts the R31 same-session control mode (--control): re-times
`control_steps` of the ALREADY-COMPLETED r=156/cpl=25 empty scene, fresh,
cold-build, no checkpoint reuse, at the START of this session, before the
cost gate is evaluated for real -- see run113.py::r31_control_ratio.

Phase 1 discipline: committed, ready-to-run, NOT executed this phase.
"""
import json
import os
import sys
import time
import pickle

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "experiments", "110-t28-item-i-local-norm-and-controls"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "112-t28-cpl25-floor-spot-check"))

import run as R110      # noqa: E402
import run112 as R112   # noqa: E402
import run113 as R      # noqa: E402
from lab import Sim, materials  # noqa: E402
from lab import sections as sc  # noqa: E402

# R29 (LOGBOOK.md, founding instance exp-112): executed identity assertions.
assert R is not R110 and R is not R112, "R29: run113 (R) must be distinct from run110/run112"
assert hasattr(R, "geom_fixedabs_cpl") and hasattr(R, "r31_control_ratio"), (
    "R29: R must be exp-113's own run113.py")
EXP110_DIR_NAME = "110-t28-item-i-local-norm-and-controls"
EXP112_DIR_NAME = "112-t28-cpl25-floor-spot-check"

SCRATCH = os.path.join(
    "/tmp/claude-0/-home-user-photon-lab/cf403016-9b91-56f9-84a5-8d5b9210dd7a/scratchpad",
    "exp113")
os.makedirs(SCRATCH, exist_ok=True)
SUBSTEP = 1000          # checkpoint granularity within one budgeted call
DEFAULT_BUDGET_S = 480  # stay well under the 600s foreground-call ceiling


def path_for(r, cpl, which):
    tag = f"r{r}_cpl{cpl}_{which}"
    return (os.path.join(SCRATCH, f"{tag}_ckpt.pkl"),
            os.path.join(SCRATCH, f"{tag}_done.pkl"))


def walltime_log_path(r, cpl, which):
    return os.path.join(SCRATCH, f"r{r}_cpl{cpl}_{which}_walltime.json")


def log_wall_time(r, cpl, which, dt):
    path = walltime_log_path(r, cpl, which)
    log = []
    if os.path.exists(path):
        with open(path) as f:
            log = json.load(f)
    log.append(dt)
    with open(path, "w") as f:
        json.dump(log, f)


def total_wall_time(r, cpl, which):
    path = walltime_log_path(r, cpl, which)
    if not os.path.exists(path):
        return 0.0
    with open(path) as f:
        return float(sum(json.load(f)))


def build_sim(g, which):
    """Byte-for-byte the same construction as experiments/110-.../112-.../
    chunk_runner*.py::build_sim."""
    sim = Sim(g["N"], g["N"], cells_per_lambda=g["cpl"],
              courant_frac=R110.COURANT_FRAC, absorb=g["absorb"])
    if which == "hollow":
        materials.graded_black_shell(sim, g["CX"], g["CY"], g["R_CORE"], g["R_COAT"],
                                      sigma_max=g["sigma_max"])
    elif which == "peccored":
        materials.pec_disk(sim, g["CX"], g["CY"], g["R_CORE"])
        materials.graded_black_shell(sim, g["CX"], g["CY"], g["R_CORE"], g["R_COAT"],
                                      sigma_max=g["sigma_max"])
    elif which == "empty":
        pass
    else:
        raise ValueError(which)
    sim.add_line_source(g["SRC_X"], angle_deg=0.0, profile="plane", edge=g["edge"])
    return sim


def step_budgeted(r, cpl, which, budget_s=DEFAULT_BUDGET_S):
    """Runs SUBSTEP-sized chunks of (r, cpl, which) until g['STEPS'] is
    reached or `budget_s` of THIS call's own wall time is used, whichever
    comes first -- checkpointing after every substep. Returns True iff
    the scene reached STEPS (done)."""
    g = R.geom_fixedabs_cpl(r, cpl)
    ckpt_path, done_path = path_for(r, cpl, which)
    if os.path.exists(done_path):
        print(f"[{which} r={r} cpl={cpl}] already DONE; total wall so far: "
              f"{total_wall_time(r, cpl, which):.1f}s")
        return True

    call_start = time.time()
    if os.path.exists(ckpt_path):
        with open(ckpt_path, "rb") as f:
            state = pickle.load(f)
        sim = state["sim"]
        steps_done = state["steps_done"]
        print(f"[{which} r={r} cpl={cpl}] resumed at steps_done={steps_done}/{g['STEPS']}")
    else:
        sim = build_sim(g, which)
        steps_done = 0
        print(f"[{which} r={r} cpl={cpl}] fresh start, TOTAL_STEPS={g['STEPS']}")

    while steps_done < g["STEPS"] and (time.time() - call_start) < budget_s:
        remaining = g["STEPS"] - steps_done
        chunk = min(SUBSTEP, remaining)
        t0 = time.time()
        sim.run(chunk)
        steps_done += chunk
        dt = time.time() - t0
        log_wall_time(r, cpl, which, dt)
        with open(ckpt_path, "wb") as f:
            pickle.dump({"sim": sim, "steps_done": steps_done}, f)
        print(f"[{which} r={r} cpl={cpl}] +{chunk} steps in {dt:.1f}s -> "
              f"{steps_done}/{g['STEPS']} (cumulative wall: "
              f"{total_wall_time(r, cpl, which):.1f}s, call elapsed "
              f"{time.time()-call_start:.1f}s/{budget_s}s budget)")

    if steps_done >= g["STEPS"]:
        cap = sc.full_capture(sim)
        with_article = which in ("hollow", "peccored")
        sigma_e = sim.sigma_e.copy() if with_article else None
        ez = sc.phasors(cap)["ez"]
        with open(done_path, "wb") as f:
            pickle.dump({"cap": cap, "sigma_e": sigma_e, "ez": ez, "g": g,
                         "total_wall_s": total_wall_time(r, cpl, which)}, f)
        if os.path.exists(ckpt_path):
            os.remove(ckpt_path)
        print(f"[{which} r={r} cpl={cpl}] COMPLETE, saved {done_path}, total wall "
              f"{total_wall_time(r, cpl, which):.1f}s")
        return True
    else:
        print(f"[{which} r={r} cpl={cpl}] budget exhausted, checkpoint saved, "
              f"{g['STEPS'] - steps_done} steps remaining")
        return False


SHORT_CONTROL_STEPS = 1000     # per scene
SUSTAINED_CONTROL_STEPS = 3334  # per scene, ~10002 steps total -- Fix 4's own
                                # "comparable duration to a real production
                                # sub-chunk" sustained-load reading
CONTROL_SCENES = ("empty", "hollow", "peccored")   # Fix 3b: same 3-scene mix
                                                     # HISTORICAL_PER_STEP_S blends


def _time_control_blend(control_steps_per_scene, scenes=CONTROL_SCENES):
    """Fresh, cold builds (NOT resumed, NOT reusing any r=156/cpl=25
    checkpoint from a prior session -- this session has none) of EACH
    scene in `scenes`, each timed for exactly `control_steps_per_scene`
    steps, summed. Fix 3b (Red Team's Phase-2 audit, EM's own finding):
    re-timing 'empty' alone against a HISTORICAL_PER_STEP_S that blends
    in peccored's own ~14%-costlier PEC-zeroing step was a real,
    anti-conservative mismatch -- this control re-times the SAME 3-scene
    mix, so both sides of the R31 ratio are commensurable."""
    g = R.geom_fixedabs_cpl(156, 25)
    total_wall_s = 0.0
    for which in scenes:
        sim = build_sim(g, which)
        t0 = time.time()
        sim.run(control_steps_per_scene)
        total_wall_s += time.time() - t0
    return R.r31_control_ratio(control_steps_per_scene, total_wall_s, n_scenes=len(scenes))


def run_control():
    """R31 same-session control, repaired per Fix 3b/Fix 4: a short
    (SHORT_CONTROL_STEPS/scene) 3-scene-blend reading and a sustained
    (SUSTAINED_CONTROL_STEPS/scene) 3-scene-blend reading, combined by
    R.combine_control_readings() (gates on the LOWER, more conservative
    speed_ratio of the two -- Fix 4, THERMODYNAMICS' own finding: a short
    burst on r=156's small grid cannot see sustained-load effects a
    multi-hour r=312 job would). Written to its own control-tagged path
    so it never collides with (and never gets mistaken for) the real
    r=312 done files."""
    short = _time_control_blend(SHORT_CONTROL_STEPS)
    sustained = _time_control_blend(SUSTAINED_CONTROL_STEPS)
    result = R.combine_control_readings(short, sustained)
    out_path = os.path.join(SCRATCH, "r31_control.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps(result, indent=2))
    print(f"\nWritten: {out_path}")
    return result


def check_cost_gate_for_r312(cpl):
    control_path = os.path.join(SCRATCH, "r31_control.json")
    if not os.path.exists(control_path):
        raise RuntimeError("R31: run --control before evaluating the cost gate "
                            "(no same-session control point on file).")
    with open(control_path) as f:
        control = json.load(f)
    _, done_path_156 = path_for(156, cpl, "empty")
    pilot_empty = R.HISTORICAL_R156_CPL25_TOTAL_S / 3.0  # avg per-scene, historical
    pilot_total = R.HISTORICAL_R156_CPL25_TOTAL_S
    gate = R.cost_gate_check_r31(pilot_empty, pilot_total, control)
    with open(os.path.join(SCRATCH, f"r312_cpl{cpl}_costgate.json"), "w") as f:
        json.dump(gate, f, indent=2)
    print(json.dumps(gate, indent=2))
    if not gate["proceed_to_r312"]:
        raise RuntimeError(f"R27/R28/R31 cost gate REFUSED r=312 (cpl={cpl}): {gate}")
    return gate


if __name__ == "__main__":
    if sys.argv[1] == "--control":
        run_control()
    elif sys.argv[1] == "--gate":
        cpl_arg = int(sys.argv[2])
        check_cost_gate_for_r312(cpl_arg)
    else:
        r_arg = int(sys.argv[1])
        cpl_arg = int(sys.argv[2])
        which_arg = sys.argv[3]
        budget_arg = int(sys.argv[4]) if len(sys.argv) > 4 else DEFAULT_BUDGET_S
        if r_arg == 312:
            check_cost_gate_for_r312(cpl_arg)   # genuinely upstream (R28), re-verified every call
        step_budgeted(r_arg, cpl_arg, which_arg, budget_arg)
