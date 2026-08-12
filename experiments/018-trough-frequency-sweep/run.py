"""
exp-018 -- The Trough Frequency Sweep: the runs.
==================================================
exp-016/017 both refuted their queued mechanisms for the eps_z~=2.25-2.4
trough (exp-014/015) -- neither the outer-boundary impedance mismatch nor
the angular scattering shape changes near the trough. exp-017's Next
section proposed a genuinely new candidate: is the trough a resonance-like
condition tied to the fixed lambda=600nm/cpl=20 grid (e.g. an internal
standing-wave condition set by the shell's radial extent in wavelengths),
or is it a pure eps_z effect that shows up regardless of the shell's
electrical size?

This is that mirror experiment: exp-003's own lambda-sweep machinery
(cells-per-lambda held FIXED at 20, geometry scaled in cells so physical
size in nm stays fixed as lambda varies -- same f(lambda) = 600nm/lambda
convention, same 6-point sweep), but anchored at the TROUGH's own
geometry (core=30, clk=90 cells at f=1, i.e. eps_z=2.25 exactly at
lambda=600) instead of exp-002's original core/coat/clk triple. Only the
cloak scene is built (no reflector/absorber -- this isn't a repeat of
exp-003's broadband question, it's a single-scene mechanism probe), at
the trough's own mu_r_floor pair (0.10, 0.18).

Because r1 and r2 scale by the SAME factor f(lambda), their ratio -- and
therefore eps_z = (r2/(r2-r1))^2 -- stays close to 2.25 at every lambda
(2.22-2.29 across the sweep after integer-cell rounding, comfortably
inside exp-014's characterized trough window of ~2.18-2.41). But the
shell's radial extent in WAVELENGTHS (r2-r1, in units of cpl=20 cells)
varies a lot across the same sweep: 2.4 lambda at 750nm up to 4.3 lambda
at 420nm. If the trough is a pure eps_z effect, the negative
floor-0.10->0.18 jump should persist at every lambda tested (eps_z stays
in-window throughout). If it's a resonance tied to a specific electrical
size / shell-radial-extent-in-wavelengths, the jump should weaken or flip
away from lambda=600nm (shell ~=3.0 lambda), where exp-014/015 pinned it.

Predictions were committed before this file first ran (see NOTES.md).

    .venv/bin/python experiments/018-trough-frequency-sweep/run.py
"""

import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from lab import Sim, materials
from lab import sections as sc

HERE = os.path.dirname(os.path.abspath(__file__))

# --- identical domain/scaling machinery to exp-003 (same fix for the
# domain-sizing bug caught there: N=680, CX=CY=300, STEPS=3600) ---
N, ABSORB, FRAC, STEPS = 680, 40, 0.32, 3600
CX, CY = 300, 300
SRC_X = 64
CPL = 20                                # FIXED across the whole sweep
REF_LAM_NM = 600.0                      # anchor: f(600) = 1
R1_BASE, R2_BASE = 30, 90               # cells at f=1 -- the trough's own core/clk geometry
BOX_BASE = {"a": 110, "b": 135}         # cells, at f=1 -- reused verbatim from exp-003
SWEEP_NM = [420, 480, 540, 600, 660, 750]
REF_HALF_H = 60
MIN_MARGIN = 60

FLOOR_SWEEP = [0.10, 0.18]               # the trough's own defining floor pair

# exp-014's reused core=30/eps_z=2.25 numbers, for the lambda=600 reproduction check
CORE30_QEXT = {0.10: 0.6620, 0.18: 0.5449}


def scale_factor(nm):
    return REF_LAM_NM / float(nm)


def geometry(nm):
    f = scale_factor(nm)
    r1 = int(round(R1_BASE * f))
    r2 = int(round(R2_BASE * f))
    box_a = int(round(BOX_BASE["a"] * f))
    box_b = int(round(BOX_BASE["b"] * f))
    for half, name in ((box_a, "box_a"), (box_b, "box_b")):
        margin_x = min(CX - half, N - ABSORB - (CX + half)) - ABSORB
        margin_y = min(CY - half, N - ABSORB - (CY + half)) - ABSORB
        assert margin_x >= MIN_MARGIN and margin_y >= MIN_MARGIN, \
            f"{name} clearance too tight at {nm}nm (margin={min(margin_x, margin_y)})"
        assert half > r2, f"{name} does not clear the cloak at {nm}nm"
    return r1, r2, (CX - box_a, CX + box_a, CY - box_a, CY + box_a), \
           (CX - box_b, CX + box_b, CY - box_b, CY + box_b)


def check_gates():
    print(f"lambda=600nm anchor, cpl={CPL}, courant_frac={FRAC}", flush=True)
    for nm in SWEEP_NM:
        r1, r2, _, _ = geometry(nm)
        eps_z = (r2 / (r2 - r1)) ** 2
        shell_lam = (r2 - r1) / float(CPL)
        thresh = ((r2 - r1) / r2) ** 2
        print(f"  nm={nm:4d}: r1={r1:3d} r2={r2:3d} shell={r2 - r1:3d} cells "
              f"({shell_lam:.2f} lambda)  eps_z={eps_z:.4f}  degeneracy_thresh={thresh:.4f}",
              flush=True)
        for floor in FLOOR_SWEEP:
            cmax = math.sqrt(floor * eps_z)
            assert FRAC < cmax, \
                f"nm={nm}, floor={floor} unstable at courant_frac={FRAC} (ceiling={cmax:.4f})"
            assert floor < thresh, \
                f"nm={nm}, floor={floor} at/above degeneracy threshold {thresh:.4f}"


def run_scene(build):
    sim = Sim(N, N, cells_per_lambda=CPL, courant_frac=FRAC, absorb=ABSORB)
    if build is not None:
        build(sim)
    sim.add_line_source(SRC_X)
    sim.run(STEPS)
    return sc.full_capture(sim)


def main():
    t0 = time.time()
    results = {}

    check_gates()

    for nm in SWEEP_NM:
        r1, r2, box_a, box_b = geometry(nm)
        eps_z = (r2 / (r2 - r1)) ** 2
        print(f"--- lambda = {nm} nm  (r1={r1}, r2={r2}, eps_z={eps_z:.4f}) ---", flush=True)
        cap_e = run_scene(None)
        for floor in FLOOR_SWEEP:
            def build(sim, r1=r1, r2=r2, floor=floor):
                materials.pec_disk(sim, CX, CY, r1)
                materials.schurig_reduced_cloak_tm(sim, CX, CY, r1, r2, mu_r_floor=floor)
            cap = run_scene(build)
            wa = sc.widths(cap, cap_e, box_a, (CX, CY, REF_HALF_H))
            wb = sc.widths(cap, cap_e, box_b, (CX, CY, REF_HALF_H))
            box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])
            cross_dev = abs(wa["sigma_ext"] - wa["sigma_ext_cross"]) / abs(wa["sigma_ext"])
            out = {k: wa[k] for k in ("sigma_scat", "sigma_abs", "sigma_ext",
                                       "sigma_ext_cross", "back_frac", "fwd_frac", "i_inc")}
            out["q_ext"] = wa["sigma_ext"] / (2.0 * r2)
            out["box_dev"] = box_dev
            out["cross_dev"] = cross_dev
            out["r1_cells"] = r1
            out["r2_cells"] = r2
            out["eps_z"] = eps_z
            out["shell_lambda"] = (r2 - r1) / float(CPL)
            out["mu_r_floor"] = floor
            results[f"cloak-{nm}-floor{floor}"] = out
            print(f"  floor={floor:.2f}: Q_ext={out['q_ext']:.4f}  back={out['back_frac']:.4f}  "
                  f"boxdev={box_dev:.3f}  crossdev={cross_dev:.3f}", flush=True)
        j = (results[f"cloak-{nm}-floor0.18"]["q_ext"] - results[f"cloak-{nm}-floor0.1"]["q_ext"]) \
            / results[f"cloak-{nm}-floor0.1"]["q_ext"]
        print(f"  jump(0.10->0.18) = {j * 100:+.2f}%", flush=True)

    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    print(f"exp-018 runs complete in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
