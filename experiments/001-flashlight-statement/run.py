"""
exp-001 — The Flashlight Statement: the runs.
=============================================
One PEC core dressed three ways (bare / graded-black / reduced cloak) plus
the empty reference, swept across 450/600/750 nm. Emits a schema-0.2.0
artifact per scene per wavelength (observer record included, normalized
against that wavelength's empty run) and writes results.json with the three
metrics NOTES.md predicts against.

Predictions were committed before this file first ran — see NOTES.md and
the git history.

    .venv\\Scripts\\python.exe experiments\\001-flashlight-statement\\run.py
"""

import json
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import numpy as np

from lab import Sim, materials, artifacts
from lab import emit as em

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(HERE, "artifacts")

N, ABSORB, FRAC, STEPS = 560, 40, 0.32, 3200
CX, CY = 252, 280
R_CORE, R_COAT, R_CLK = 30, 78, 90          # 0.9 / 2.34 / 2.7 um at dx=30nm
SRC_X, OBS_X = 64, 78
SWEEP = [(15, 450), (20, 600), (25, 750)]    # cells/lambda <-> nm at dx=30nm
SUITE_STATUS = "24/24 (2026-08-09)"
PROV = [
    {"kind": "experiment", "id": "exp-001"},
    {"kind": "witness-statement",
     "id": "pursue-r1--western_us_event_slides_5.08.2026",
     "note": "the statement under test: beam 'stopped about 50 yards away on nothing in particular'"},
]


def build(scene, sim):
    if scene == "reflector":
        materials.pec_disk(sim, CX, CY, R_CORE)
    elif scene == "absorber":
        materials.pec_disk(sim, CX, CY, R_CORE)
        materials.graded_black_shell(sim, CX, CY, R_CORE, R_COAT)
    elif scene == "cloak":
        materials.pec_disk(sim, CX, CY, R_CORE)
        materials.schurig_reduced_cloak_tm(sim, CX, CY, R_CORE, R_CLK,
                                           mu_r_floor=0.05)


def run_scene(scene, cpl):
    sim = Sim(N, N, cells_per_lambda=cpl, courant_frac=FRAC, absorb=ABSORB)
    build(scene, sim)
    sim.add_line_source(SRC_X)
    sim.run(STEPS)
    cap = em.quarter_pair(sim)
    env = np.sqrt(cap[0] ** 2 + cap[2] ** 2)
    return sim, cap, env


# fixed measurement regions, identical for every scene (outside the largest
# dressing, inside the absorbing bands)
_x = np.arange(N)[:, None]
_y = np.arange(N)[None, :]
_rr = np.hypot(_x - CX, _y - CY)
ANNULUS = (_rr >= R_CLK + 10) & (_rr <= R_CLK + 70)
BEHIND = (slice(CX + R_CLK + 15, CX + R_CLK + 115), slice(CY - 20, CY + 20))


def main():
    t0 = time.time()
    results = {}
    for cpl, nm in SWEEP:
        print(f"--- lambda = {nm} nm (cells/lambda = {cpl}) ---", flush=True)
        sim_e, cap_e, env_e = run_scene("empty", cpl)
        _, _, aux_ref = em.observer_record(sim_e, cap_e, OBS_X)
        ref_dir = em.emit_run(
            sim_e, os.path.join(ART, f"empty-{nm}nm"), experiment="exp-001",
            scene="empty", lambda_nm=float(nm), suite_status=SUITE_STATUS,
            snapshot_step=STEPS, capture=cap_e, provenance=PROV)
        print(f"  empty: emitted {os.path.basename(ref_dir)}", flush=True)

        for scene in ("reflector", "absorber", "cloak"):
            sim, cap, env = run_scene(scene, cpl)
            ang, flux, _ = em.observer_record(sim, cap, OBS_X, reference=aux_ref)
            ret = float(np.sum(flux))
            behind = float(np.mean(env[BEHIND] ** 2) / np.mean(env_e[BEHIND] ** 2))
            scat = float(np.sqrt(np.mean((env - env_e)[ANNULUS] ** 2)))
            results[f"{scene}-{nm}"] = {
                "observer_return": ret, "beam_behind": behind,
                "scattered_rms": scat,
                "camera_floor": aux_ref["p_backward_total"] / aux_ref["p_forward_total"],
            }
            em.emit_run(
                sim, os.path.join(ART, f"{scene}-{nm}nm"), experiment="exp-001",
                scene=scene, lambda_nm=float(nm), suite_status=SUITE_STATUS,
                snapshot_step=STEPS, capture=cap, provenance=PROV,
                observer=dict(
                    plane_x=OBS_X, start_step=STEPS, normalization="vacuum_run",
                    reference_run=f"experiments/001-flashlight-statement/artifacts/empty-{nm}nm",
                    angles=ang, flux=flux))
            print(f"  {scene:9s}: return {ret:.4f} · beam-behind {behind:.3f} "
                  f"· scattered RMS {scat:.4f}", flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(results, f, indent=2, sort_keys=True)

    n_fail = artifacts.check(
        sorted(os.path.join(ART, d) for d in os.listdir(ART)))
    print(f"exp-001 runs complete in {(time.time() - t0) / 60:.1f} min; "
          f"artifact gate failures: {n_fail}", flush=True)
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
