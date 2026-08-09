"""
exp-000 artifact emission — the repo's first Evidence-Gated run artifacts.
Re-runs the exp-000 scene (and its empty-domain reference) through the lab
engine and emits schema-0.1.0 artifacts with an observer record, giving
the viz lane real committed data to build against.

    .venv\\Scripts\\python.exe experiments\\000-hello-maxwell\\make_artifacts.py

Scenes:
    artifacts/empty/     reference run (no object, no observer block)
    artifacts/cylinder/  the exp-000 cylinder + observer record normalized
                         against the empty reference (vacuum_run)

reference_run is stored repo-relative so the artifact travels.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import numpy as np

from lab import Sim, materials, artifacts
from lab import emit as em

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(HERE, "artifacts")
SUITE_STATUS = "19/19 (2026-08-09, incl. observer gates)"
PROV = [
    {"kind": "experiment", "id": "exp-000"},
    {"kind": "witness-statement",
     "id": "pursue-r1--western_us_event_slides_5.08.2026",
     "note": "the founding statement; exp-001 tests it — exp-000 is the bench it stands on"},
    {"kind": "paper", "id": "Chen-Taflove-Backman-2004-OptExpress",
     "note": "photonic nanojet, reproduced unprompted in this scene"},
]


def run_scene(with_cylinder):
    sim = Sim(720, 440, cells_per_lambda=20, courant_frac=0.99, absorb=36)
    if with_cylinder:
        materials.dielectric_cylinder(sim, 302, 220, 40, 4.0)
    sim.add_line_source(60)
    sim.run(1350)
    return sim, em.quarter_pair(sim)


def main():
    print("running empty reference ...")
    sim_ref, cap_ref = run_scene(False)
    _, _, aux_ref = em.observer_record(sim_ref, cap_ref, plane_x=84)
    ref_dir = em.emit_run(
        sim_ref, os.path.join(ART, "empty"), experiment="exp-000",
        scene="empty", lambda_nm=600.0, suite_status=SUITE_STATUS,
        snapshot_step=1350, capture=cap_ref, provenance=PROV[:1])
    print(f"  wrote {ref_dir}")

    print("running cylinder scene ...")
    sim_c, cap_c = run_scene(True)
    ang, flux, _ = em.observer_record(sim_c, cap_c, plane_x=84, reference=aux_ref)
    cyl_dir = em.emit_run(
        sim_c, os.path.join(ART, "cylinder"), experiment="exp-000",
        scene="cylinder", lambda_nm=600.0, suite_status=SUITE_STATUS,
        snapshot_step=1350, capture=cap_c, provenance=PROV,
        observer=dict(plane_x=84, start_step=1350, normalization="vacuum_run",
                      reference_run="experiments/000-hello-maxwell/artifacts/empty",
                      angles=ang, flux=flux))
    print(f"  wrote {cyl_dir}")
    print(f"  observer: total return fraction = {float(np.sum(flux)):.4f}")

    n_fail = artifacts.check([os.path.join(ART, "empty"), os.path.join(ART, "cylinder")])
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
