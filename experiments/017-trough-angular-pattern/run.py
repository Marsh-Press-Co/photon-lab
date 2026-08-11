"""
exp-017 -- Mechanism candidate 2: angular-pattern comparison, trough vs
flanks.
=============================================================================
exp-016 refuted outer-boundary impedance mismatch as the eps_z trough's
mechanism (smooth in eps_z, floor-independent where the trough lives --
structurally can't explain a floor-dependent sign flip). This file tests
the other candidate queued in exp-015's Next section: does the trough
(r1=30, eps_z=2.25) scatter into a qualitatively DIFFERENT angular shape
than its flanks (r1=27/33), or is it the same shape, just a different
magnitude?

New instrumentation: lab/sections.angular_scattered_pattern (added this
shift) bins the same per-cell scattered-outflow terms widths() already
sums, by angle around the box perimeter, instead of collapsing them to
one number. A self-consistency identity (sum(bins) == widths()'s own
sigma_scat) is checked before any pattern is trusted for shape work.

Same domain/geometry as exp-014/015/016's r1=27/30/33 bracket points,
floor=0.10 only (one of the trough's own defining pair, keeps this file
to 4 runs).

Predictions were committed before this file first ran (see NOTES.md).

    .venv\\Scripts\\python.exe experiments\\017-trough-angular-pattern\\run.py
"""

import json
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np

from lab import Sim, materials
from lab import sections as sc

HERE = os.path.dirname(os.path.abspath(__file__))

# --- identical to exp-014's cpl=20 baseline domain ---
N, ABSORB, FRAC, STEPS = 680, 40, 0.32, 3600
CX, CY = 300, 300
SRC_X = 64
CPL = 20
REF_HALF_H = 60
MIN_MARGIN = 60
BOX_A_HALF, BOX_B_HALF = 110, 135
R2_CELLS = 90

CORE_POINTS = [27, 30, 33]     # flank / trough center / flank
FLOOR = 0.10
N_BINS = 48

# exp-014's own reused core=30 number, for the reproduction check (P2)
CORE30_QEXT_FLOOR010 = 0.6620


def box_coords():
    for half, name in ((BOX_A_HALF, "box_a"), (BOX_B_HALF, "box_b")):
        margin_x = min(CX - half, N - ABSORB - (CX + half)) - ABSORB
        margin_y = min(CY - half, N - ABSORB - (CY + half)) - ABSORB
        assert margin_x >= MIN_MARGIN and margin_y >= MIN_MARGIN, \
            f"{name} clearance too tight (margin={min(margin_x, margin_y)})"
        assert half > R2_CELLS, f"{name} does not clear the cloak"
    return (CX - BOX_A_HALF, CX + BOX_A_HALF, CY - BOX_A_HALF, CY + BOX_A_HALF), \
           (CX - BOX_B_HALF, CX + BOX_B_HALF, CY - BOX_B_HALF, CY + BOX_B_HALF)


def run_scene(build):
    sim = Sim(N, N, cells_per_lambda=CPL, courant_frac=FRAC, absorb=ABSORB)
    if build is not None:
        build(sim)
    sim.add_line_source(SRC_X)
    sim.run(STEPS)
    return sc.full_capture(sim)


def normalized_corr(a, b):
    """Pearson correlation of two angular patterns (shape only -- each
    normalized to its own sum before comparing)."""
    an = a / np.sum(np.abs(a))
    bn = b / np.sum(np.abs(b))
    an = an - an.mean()
    bn = bn - bn.mean()
    denom = np.sqrt(np.sum(an ** 2) * np.sum(bn ** 2))
    return float(np.sum(an * bn) / denom) if denom > 0 else float("nan")


def main():
    t0 = time.time()
    results = {}

    box_a, box_b = box_coords()
    cap_e = run_scene(None)

    patterns = {}
    for r1 in CORE_POINTS:
        def build(sim, r1=r1):
            materials.pec_disk(sim, CX, CY, r1)
            materials.schurig_reduced_cloak_tm(sim, CX, CY, r1, R2_CELLS,
                                               mu_r_floor=FLOOR)
        cap = run_scene(build)
        wa = sc.widths(cap, cap_e, box_a, (CX, CY, REF_HALF_H))
        wb = sc.widths(cap, cap_e, box_b, (CX, CY, REF_HALF_H))
        box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])
        cross_dev = abs(wa["sigma_ext"] - wa["sigma_ext_cross"]) / abs(wa["sigma_ext"])
        q_ext = wa["sigma_ext"] / (2.0 * R2_CELLS)

        centers, pattern = sc.angular_scattered_pattern(cap, cap_e, box_a,
                                                         (CX, CY, REF_HALF_H), n_bins=N_BINS)
        self_consistency = abs(float(np.sum(pattern)) - wa["sigma_scat"]) / abs(wa["sigma_scat"])

        patterns[r1] = pattern
        results[f"core{r1}"] = {
            "eps_z": (R2_CELLS / (R2_CELLS - r1)) ** 2,
            "q_ext": q_ext,
            "box_dev": box_dev,
            "cross_dev": cross_dev,
            "sigma_scat": wa["sigma_scat"],
            "back_frac": wa["back_frac"],
            "fwd_frac": wa["fwd_frac"],
            "pattern_self_consistency_dev": self_consistency,
            "angle_centers_deg": centers.tolist(),
            "sigma_scat_per_bin": pattern.tolist(),
        }
        print(f"  r1={r1:2d}: Q_ext={q_ext:.4f}  box_dev={box_dev:.4f}  "
              f"cross_dev={cross_dev:.4f}  self_consistency_dev={self_consistency:.2e}", flush=True)

    corr_27_30 = normalized_corr(patterns[27], patterns[30])
    corr_33_30 = normalized_corr(patterns[33], patterns[30])
    corr_27_33 = normalized_corr(patterns[27], patterns[33])
    results["shape_correlations"] = {
        "corr_flank27_vs_trough30": corr_27_30,
        "corr_flank33_vs_trough30": corr_33_30,
        "corr_flank27_vs_flank33": corr_27_33,
    }
    print(f"  corr(flank27, trough30) = {corr_27_30:.4f}", flush=True)
    print(f"  corr(flank33, trough30) = {corr_33_30:.4f}", flush=True)
    print(f"  corr(flank27, flank33)  = {corr_27_33:.4f}", flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print(f"exp-017 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
