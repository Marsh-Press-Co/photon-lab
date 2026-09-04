"""Checkpoint/resume runner for exp-110's item-1a re-capture: 3 scenes
(empty, hollow-article, PEC-cored-article) x 2 r (156, 312) = 6 FDTD
Sim.run() calls -- byte-for-byte the identical geometry exp-108 already
captured (Panel Iteration 85). Panel Iteration 87. Extends exp-107/108's
own chunk_runner.py pattern (bit-exact A/B-validated at r=156, exp-107;
extended to a third scene type, exp-108). Foreground Bash calls only --
this session's own backgrounded/nohup execution mode is confirmed
pathologically slow for sustained FDTD numpy work (exp-107's own
A/B-tested finding, reused without re-testing).

Environment-path correction (disclosed, non-substantive): exp-108's own
chunk_runner.py hardcoded a SCRATCH path belonging to that session's own
ephemeral scratchpad, which does not exist in this session -- this is the
exact gap item 1b exists to close for good. SCRATCH below points to THIS
session's own scratchpad instead; every other constant is unchanged.

Also implements the R27 cost-gate wall-time log (Fix 5/6): every chunk's
own wall time is appended to a per-(r,which) log file, so cost_gate_check()
(run.py) and build_result_text()'s wall_time_source can sum genuinely-new
wall time without conflating it with exp-108's own historical 7712.0s
figure (Fix 6).
"""
import json
import os
import sys
import time
import pickle

sys.path.insert(0, "/home/user/photon-lab/experiments/110-t28-item-i-local-norm-and-controls")
sys.path.insert(0, "/home/user/photon-lab")
import run as R  # noqa: E402
from lab import Sim, materials  # noqa: E402
from lab import sections as sc  # noqa: E402

SCRATCH = "/tmp/claude-0/-home-user-photon-lab/99fb0d5c-aa12-5461-9307-ebac1add313f/scratchpad/exp110"
os.makedirs(SCRATCH, exist_ok=True)
CHUNK_STEPS = 2200


def path_for(r, which):
    return (os.path.join(SCRATCH, f"r{r}_{which}_ckpt.pkl"),
            os.path.join(SCRATCH, f"r{r}_{which}_done.pkl"))


def walltime_log_path(r, which):
    return os.path.join(SCRATCH, f"r{r}_{which}_walltime.json")


def log_wall_time(r, which, dt):
    path = walltime_log_path(r, which)
    log = []
    if os.path.exists(path):
        with open(path) as f:
            log = json.load(f)
    log.append(dt)
    with open(path, "w") as f:
        json.dump(log, f)


def total_wall_time(r, which):
    path = walltime_log_path(r, which)
    if not os.path.exists(path):
        return 0.0
    with open(path) as f:
        return float(sum(json.load(f)))


def build_sim(g, which):
    sim = Sim(g["N"], g["N"], cells_per_lambda=R.CPL_600, courant_frac=R.COURANT_FRAC, absorb=R.ABSORB)
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
    sim.add_line_source(g["SRC_X"], angle_deg=0.0, profile="plane", edge=R.EDGE)
    return sim


def check_cost_gate_for_312():
    """Panel Iteration 88 (exp-111), mandatory-fixes 1/2 of
    experiments/111-.../phase2_redteam_audit.md Sec 5 (THERMODYNAMICS' own
    Phase-1 proposal; R28's own founding remedy). Genuinely upstream of
    every real r=312 Sim.run() call: refuses to proceed unless r=156's
    three scenes are DONE and R.cost_gate_check() clears, using THIS
    session's own log_wall_time()/total_wall_time() records (grounding-fact
    correction, phase1_proposal.md Sec 2.0: a prior session's own historical
    wall-time logs are not assumed present). Called from step_once() AFTER
    the existing already-DONE early-return (mandatory-fix 2: the guard must
    not re-evaluate the gate on an idempotent status-check of an
    already-completed r=312 scene, where r=156's own logs may be absent or
    stale in a fresh session -- see gate_reposition_control.py Case 5)."""
    for which in ("empty", "hollow", "peccored"):
        _, done_path_156 = path_for(156, which)
        if not os.path.exists(done_path_156):
            raise RuntimeError(f"cost gate: r=156/{which} not complete -- "
                                f"cannot evaluate cost_gate_check() before r=312.")
    pilot_empty = total_wall_time(156, "empty")
    pilot_total = sum(total_wall_time(156, w) for w in ("empty", "hollow", "peccored"))
    gate = R.cost_gate_check(pilot_empty, pilot_total)
    with open(os.path.join(SCRATCH, "r312_costgate.json"), "w") as f:
        json.dump(gate, f, indent=2)
    if not gate["proceed_to_r312"]:
        raise RuntimeError(f"R27/R28 cost gate REFUSED r=312: {gate}")
    return gate


def step_once(r, which):
    g = R.geom_fixedabs(r)
    ckpt_path, done_path = path_for(r, which)
    if os.path.exists(done_path):
        print(f"[{which} r={r}] already DONE ({done_path}); total wall so far: "
              f"{total_wall_time(r, which):.1f}s")
        return True

    if r == 312:
        check_cost_gate_for_312()          # genuinely upstream of build_sim/Sim.run below

    t0 = time.time()
    if os.path.exists(ckpt_path):
        with open(ckpt_path, "rb") as f:
            state = pickle.load(f)
        sim = state["sim"]
        steps_done = state["steps_done"]
        print(f"[{which} r={r}] resumed at steps_done={steps_done}")
    else:
        sim = build_sim(g, which)
        steps_done = 0
        print(f"[{which} r={r}] fresh start, TOTAL_STEPS={g['STEPS']}")

    remaining = g["STEPS"] - steps_done
    chunk = min(CHUNK_STEPS, remaining)
    sim.run(chunk)
    steps_done += chunk
    dt = time.time() - t0
    log_wall_time(r, which, dt)
    print(f"[{which} r={r}] ran {chunk} steps in {dt:.1f}s -> steps_done={steps_done}/{g['STEPS']} "
          f"(cumulative wall: {total_wall_time(r, which):.1f}s)")

    if steps_done >= g["STEPS"]:
        cap = sc.full_capture(sim)
        with_article = which in ("hollow", "peccored")
        sigma_e = sim.sigma_e.copy() if with_article else None
        ez = sc.phasors(cap)["ez"]
        with open(done_path, "wb") as f:
            pickle.dump({"cap": cap, "sigma_e": sigma_e, "ez": ez, "g": g,
                         "total_wall_s": total_wall_time(r, which)}, f)
        if os.path.exists(ckpt_path):
            os.remove(ckpt_path)
        print(f"[{which} r={r}] COMPLETE, saved {done_path}, total wall "
              f"{total_wall_time(r, which):.1f}s")
        return True
    else:
        with open(ckpt_path, "wb") as f:
            pickle.dump({"sim": sim, "steps_done": steps_done}, f)
        print(f"[{which} r={r}] checkpoint saved, {g['STEPS'] - steps_done} steps remaining")
        return False


if __name__ == "__main__":
    r_arg = int(sys.argv[1])       # 156 or 312
    which_arg = sys.argv[2]        # "empty" | "hollow" | "peccored"
    step_once(r_arg, which_arg)
