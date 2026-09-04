"""Checkpoint/resume runner for exp-108's Tier-1 batch: 3 scenes (empty,
hollow-article, PEC-cored-article) x 2 r (156, 312) = 6 new Sim.run()
calls. Panel Iteration 85. Extends exp-107's own chunk_runner.py pattern
(bit-exact A/B-validated at r=156, that cycle) to a third scene type.
Foreground Bash calls only -- this session's own backgrounded/nohup
execution mode is confirmed pathologically slow for sustained FDTD numpy
work (exp-107's own A/B-tested finding)."""
import os
import sys
import time
import pickle

sys.path.insert(0, "/home/user/photon-lab/experiments/108-t28-reclassification-angular-pattern-batch")
sys.path.insert(0, "/home/user/photon-lab")
import run as R  # noqa: E402
from lab import Sim, materials  # noqa: E402
from lab import sections as sc  # noqa: E402

SCRATCH = "/tmp/claude-0/-home-user-photon-lab/b3074561-e458-5939-8b7f-fe9684f9569f/scratchpad/exp108"
os.makedirs(SCRATCH, exist_ok=True)
CHUNK_STEPS = 2200


def path_for(r, which):
    return (os.path.join(SCRATCH, f"r{r}_{which}_ckpt.pkl"),
            os.path.join(SCRATCH, f"r{r}_{which}_done.pkl"))


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


def step_once(r, which):
    g = R.geom_fixedabs(r)
    ckpt_path, done_path = path_for(r, which)
    if os.path.exists(done_path):
        print(f"[{which} r={r}] already DONE ({done_path})")
        return True

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
    print(f"[{which} r={r}] ran {chunk} steps in {dt:.1f}s -> steps_done={steps_done}/{g['STEPS']}")

    if steps_done >= g["STEPS"]:
        cap = sc.full_capture(sim)
        with_article = which in ("hollow", "peccored")
        sigma_e = sim.sigma_e.copy() if with_article else None
        ez = sc.phasors(cap)["ez"]
        with open(done_path, "wb") as f:
            pickle.dump({"cap": cap, "sigma_e": sigma_e, "ez": ez, "g": g}, f)
        if os.path.exists(ckpt_path):
            os.remove(ckpt_path)
        print(f"[{which} r={r}] COMPLETE, saved {done_path}")
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
