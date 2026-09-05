"""Checkpoint/resume runner for exp-112's own cpl=25 resolution leg: 3
scenes (empty, hollow-article, PEC-cored-article) at r=156 ONLY this
cycle (r=312 is explicitly deferred -- see run.py's own cost-gate
projection, phase1_proposal.md Sec 2.0). Panel Iteration 89. Extends
experiments/110-.../chunk_runner.py's own checkpoint/resume idiom
(byte-for-byte the same pattern: foreground Bash calls only -- this
session's own backgrounded/nohup execution mode is confirmed
pathologically slow for sustained FDTD numpy work, exp-107's own
A/B-tested finding, reused without re-testing) to a new (r, cpl, which)
key space, since this cycle's own geometry is a NEW cpl value never
captured before in this family.

Phase 1 discipline: this file is committed, ready-to-run, but NOT
executed this phase -- no Sim.run() call happens until a future Phase 4
invokes it. It is imported by, not copy-pasted from,
experiments/110-.../chunk_runner.py's own build_sim/step_once shape.
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

import run as R110  # noqa: E402  (experiments/110-.../run.py -- cost_gate_check, constants)
import run112 as R  # noqa: E402  (this directory's own run112.py -- geom_fixedabs_cpl, etc.)
from lab import Sim, materials  # noqa: E402
from lab import sections as sc  # noqa: E402

# Phase-2 Red Team audit Docket Fix 1 (R29 candidate): the ORIGINAL
# same-basename "run.py"/"run.py" collision silently aliased R110 and R to
# the SAME sys.modules entry, crashing this file before any Sim.run() call
# (confirmed by direct execution, phase2_redteam_audit.md Attack 1). Renamed
# this directory's own module to run112.py; executed identity assertion so
# a future re-collision halts here, loudly, rather than silently aliasing.
assert R is not R110, "R29: run112 (R) must be a distinct module object from exp-110's run (R110)"
assert hasattr(R, "geom_fixedabs_cpl"), "R29: R must be exp-112's own run112.py, not exp-110's run.py"

SCRATCH = os.path.join(
    "/tmp/claude-0/-home-user-photon-lab/fbd87760-699f-5fb6-8cb5-6f52801ed2e5/scratchpad",
    "exp112")
os.makedirs(SCRATCH, exist_ok=True)
CHUNK_STEPS = 2200


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
    """Byte-for-byte the same construction as experiments/110-.../
    chunk_runner.py::build_sim, generalized to read absorb/edge/cpl from
    the geometry dict (geom_fixedabs_cpl's own new fields) instead of
    module constants, since both now vary with the cpl target."""
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


def check_cost_gate_for_r312_expansion(cpl):
    """A FUTURE-USE guard, mirroring experiments/110-.../chunk_runner.py::
    check_cost_gate_for_312()'s own genuinely-upstream position (R27/R28
    discipline) -- NOT exercised this cycle (this cycle's own CLI usage
    only ever passes r=156; see phase1_proposal.md Sec 3, scope decision).
    Included so a future cycle that DOES decide to expand this same cpl
    leg to r=312 inherits an upstream-positioned gate from day one,
    rather than repeating exp-110's own R28-founding gap (a gate that
    exists but sits downstream of the spend it purports to control)."""
    for which in ("empty", "hollow", "peccored"):
        _, done_path_156 = path_for(156, cpl, which)
        if not os.path.exists(done_path_156):
            raise RuntimeError(f"cost gate: r=156/cpl={cpl}/{which} not complete -- "
                                f"cannot evaluate cost_gate_check() before r=312.")
    pilot_empty = total_wall_time(156, cpl, "empty")
    pilot_total = sum(total_wall_time(156, cpl, w) for w in ("empty", "hollow", "peccored"))
    gate = R.cost_gate_check_for_r312_expansion(pilot_empty, pilot_total)
    with open(os.path.join(SCRATCH, f"r312_cpl{cpl}_costgate.json"), "w") as f:
        json.dump(gate, f, indent=2)
    if not gate["proceed_to_r312"]:
        raise RuntimeError(f"R27/R28 cost gate REFUSED r=312 (cpl={cpl}): {gate}")
    return gate


def step_once(r, cpl, which):
    g = R.geom_fixedabs_cpl(r, cpl)
    ckpt_path, done_path = path_for(r, cpl, which)
    if os.path.exists(done_path):
        print(f"[{which} r={r} cpl={cpl}] already DONE ({done_path}); total wall so far: "
              f"{total_wall_time(r, cpl, which):.1f}s")
        return True

    if r == 312:
        check_cost_gate_for_r312_expansion(cpl)   # genuinely upstream, not exercised this cycle

    t0 = time.time()
    if os.path.exists(ckpt_path):
        with open(ckpt_path, "rb") as f:
            state = pickle.load(f)
        sim = state["sim"]
        steps_done = state["steps_done"]
        print(f"[{which} r={r} cpl={cpl}] resumed at steps_done={steps_done}")
    else:
        sim = build_sim(g, which)
        steps_done = 0
        print(f"[{which} r={r} cpl={cpl}] fresh start, TOTAL_STEPS={g['STEPS']}")

    remaining = g["STEPS"] - steps_done
    chunk = min(CHUNK_STEPS, remaining)
    sim.run(chunk)
    steps_done += chunk
    dt = time.time() - t0
    log_wall_time(r, cpl, which, dt)
    print(f"[{which} r={r} cpl={cpl}] ran {chunk} steps in {dt:.1f}s -> "
          f"steps_done={steps_done}/{g['STEPS']} "
          f"(cumulative wall: {total_wall_time(r, cpl, which):.1f}s)")

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
        with open(ckpt_path, "wb") as f:
            pickle.dump({"sim": sim, "steps_done": steps_done}, f)
        print(f"[{which} r={r} cpl={cpl}] checkpoint saved, "
              f"{g['STEPS'] - steps_done} steps remaining")
        return False


if __name__ == "__main__":
    r_arg = int(sys.argv[1])       # 156 (this cycle) or 312 (future, gated)
    cpl_arg = int(sys.argv[2])     # 25 this cycle
    which_arg = sys.argv[3]        # "empty" | "hollow" | "peccored"
    step_once(r_arg, cpl_arg, which_arg)
