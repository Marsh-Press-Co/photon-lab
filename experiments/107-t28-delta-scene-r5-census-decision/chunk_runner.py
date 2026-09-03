"""Checkpoint/resume runner for exp-107's item-1/4 FDTD captures. Panel
Iteration 84. Diagnosed this shift: long-running processes launched via
this session's backgrounded/nohup execution mode run this FDTD workload
pathologically slowly (an isolated A/B test found foreground execution
reproduces exp-106's own historical per-step rate, ~0.047-0.22s/step,
while the identical code launched in the background accrued CPU time at
roughly 1/10-1/20 that rate over a >90-minute wall-clock window with zero
completed output -- a pure CPU-bound Python loop was NOT similarly
slowed in the background, isolating this to the sustained large-array
numpy FDTD workload specifically. An environment/tooling characteristic
of this remote session, not a `lab/` engine defect -- the trust suite,
run directly foreground, was green in 104s at this shift's start).

This script chunks a single Sim.run() into pieces that fit comfortably
under the foreground Bash tool's ~10-min timeout, pickling the whole Sim
object between chunks (confirmed picklable/resumable this shift). Used
for BOTH r=156 (completes in 1 chunk, STEPS=6400 < CHUNK_STEPS is not
true here so it still chunks correctly -- see CHUNK_STEPS below) and
r=312 (needs 6 chunks per scene at CHUNK_STEPS=2200, ~500s each)."""
import os
import sys
import time
import pickle

sys.path.insert(0, "/home/user/photon-lab/experiments/107-t28-delta-scene-r5-census-decision")
sys.path.insert(0, "/home/user/photon-lab")
import run as R  # noqa: E402
from lab import Sim, materials  # noqa: E402
from lab import sections as sc  # noqa: E402

SCRATCH = "/tmp/claude-0/-home-user-photon-lab/6cf0c183-8ce9-5c5c-af14-ff173a23cef4/scratchpad/exp107"
CHUNK_STEPS = 2200


def path_for(r, with_article):
    tag = "article" if with_article else "empty"
    return (os.path.join(SCRATCH, f"r{r}_{tag}_ckpt.pkl"),
            os.path.join(SCRATCH, f"r{r}_{tag}_done.pkl"))


def step_once(r, with_article):
    g = R.geom_fixedabs(r)
    ckpt_path, done_path = path_for(r, with_article)
    if os.path.exists(done_path):
        print(f"[{'article' if with_article else 'empty'}] already DONE ({done_path})")
        return True

    t0 = time.time()
    if os.path.exists(ckpt_path):
        with open(ckpt_path, "rb") as f:
            state = pickle.load(f)
        sim = state["sim"]
        steps_done = state["steps_done"]
        print(f"[{'article' if with_article else 'empty'}] resumed at steps_done={steps_done}")
    else:
        sim = Sim(g["N"], g["N"], cells_per_lambda=R.CPL_600, courant_frac=R.COURANT_FRAC, absorb=R.ABSORB)
        if with_article:
            materials.graded_black_shell(sim, g["CX"], g["CY"], g["R_CORE"], g["R_COAT"],
                                          sigma_max=g["sigma_max"])
        sim.add_line_source(g["SRC_X"], angle_deg=0.0, profile="plane", edge=R.EDGE)
        steps_done = 0
        print(f"[{'article' if with_article else 'empty'}] fresh start, TOTAL_STEPS={g['STEPS']}")

    remaining = g["STEPS"] - steps_done
    chunk = min(CHUNK_STEPS, remaining)
    sim.run(chunk)
    steps_done += chunk
    dt = time.time() - t0
    print(f"[{'article' if with_article else 'empty'}] ran {chunk} steps in {dt:.1f}s "
          f"-> steps_done={steps_done}/{g['STEPS']}")

    if steps_done >= g["STEPS"]:
        # final capture (full_capture's own extra `quarter` steps happen inside sc.full_capture)
        cap = sc.full_capture(sim)
        sigma_e = sim.sigma_e.copy() if with_article else None
        ez = sc.phasors(cap)["ez"]
        with open(done_path, "wb") as f:
            pickle.dump({"cap": cap, "sigma_e": sigma_e, "ez": ez, "g": g}, f)
        if os.path.exists(ckpt_path):
            os.remove(ckpt_path)
        print(f"[{'article' if with_article else 'empty'}] COMPLETE, saved {done_path}")
        return True
    else:
        with open(ckpt_path, "wb") as f:
            pickle.dump({"sim": sim, "steps_done": steps_done}, f)
        print(f"[{'article' if with_article else 'empty'}] checkpoint saved, "
              f"{g['STEPS'] - steps_done} steps remaining")
        return False


if __name__ == "__main__":
    r_arg = int(sys.argv[1])         # 156 or 312
    which = sys.argv[2]              # "empty" or "article"
    step_once(r_arg, with_article=(which == "article"))
