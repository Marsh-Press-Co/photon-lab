"""exp-029 -- The Coherent-Superposition Bridge Gate: measurement harness.
===========================================================================
Panel Iteration 6 (lead QUANTUM OPTICS; synthesis: Director, post Red
Team's proceed-with-mandatory-fixes -- see design_geometry.py's module
docstring and NOTES.md Phase 3 for the full accepted/overridden record).

Two sources injected SIMULTANEOUSLY in one Sim -- this program's first
multi-source run outside the suite: "beam" (angle 0 deg, amplitude 1.0)
and "off_axis" (angle 30 deg, amplitude sqrt(AMP_REL), AMP_REL=2e-4,
Iteration 1's own committed scenario default). Object: exp-028's exact
Cell B construction (graded_black_shell + core-fill), the non-PEC-cored
article T9 established as mechanistically clean.

6 new FDTD sim calls (empty+beam, empty+off_axis, empty+joint,
object+beam, object+off_axis, object+joint) at the native exp-001/026/
027/028 beam-scene bench, lambda=600nm, cpl=20, steps=3200.

Predictions committed in NOTES.md BEFORE this file's first run (house
discipline, non-negotiable). Suite stage 11 (lab/validation/run_all.py)
gates the underlying multi-source machinery and was run and green before
this file's first run.
"""

import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, HERE)

import design_geometry as dg
from lab import Sim, materials as mat, sections as sc


def build_object(sim):
    """exp-028's exact Cell B construction (fix 1, mandatory): graded shell
    PLUS the core-fill line -- NOT the shell alone, which leaves r<r_in an
    unfilled vacuum hole (an untested hollow-shell article)."""
    mat.graded_black_shell(sim, dg.BEAM_CX, dg.BEAM_CY, dg.R_IN, dg.R_OUT,
                           sigma_max=dg.SIGMA_MAX, eps_max=1.0)
    x = np.arange(sim.nx)[:, None]
    y = np.arange(sim.ny)[None, :]
    rr = np.hypot(x - dg.BEAM_CX, y - dg.BEAM_CY)
    sim.sigma_e[rr < dg.R_IN] += dg.SIGMA_MAX          # strict '<', exp-027/028's fix, reused
    sim.objects.append({"type": "exp029_object_cellB_style"})
    core_sigma = float(sim.sigma_e[dg.BEAM_CX, dg.BEAM_CY])
    assert core_sigma > 0.0, "core-fill assertion failed: r<r_in reads as vacuum"
    return core_sigma


def run_scene(article, sources):
    """sources: list of (x, angle_deg, amplitude) tuples, injected
    simultaneously in one Sim -- this program's first non-suite
    multi-source run (fix 3: no intensity_role/amp_rel kwargs -- those are
    manifest fields below, not add_line_source() arguments)."""
    sim = Sim(dg.BEAM_N, dg.BEAM_N, cells_per_lambda=20, courant_frac=dg.BEAM_FRAC,
              absorb=dg.BEAM_ABSORB)
    core_sigma = build_object(sim) if article == "object" else None
    for x, ang, amp in sources:
        sim.add_line_source(x, angle_deg=ang, amplitude=amp)
    sim.run(dg.BEAM_STEPS_NATIVE)
    return sim, sc.full_capture(sim), core_sigma


SRC_BEAM = (dg.BEAM_SRC_X, 0.0, dg.AMP_BEAM)
SRC_OFFAXIS = (dg.BEAM_SRC_X, dg.OFFAXIS_ANGLE_DEG, dg.AMP_OFFAXIS)


def rms(x):
    return float(np.sqrt(np.mean(np.abs(x) ** 2)))


def main():
    t0 = time.time()
    print("exp-029: 6 runs (empty/object x beam/off_axis/joint)", flush=True)

    caps = {}
    core_sigma_seen = None
    for article in ("empty", "object"):
        for label, sources in (("beam", [SRC_BEAM]), ("off_axis", [SRC_OFFAXIS]),
                               ("joint", [SRC_BEAM, SRC_OFFAXIS])):
            sim, cap, core_sigma = run_scene(article, sources)
            caps[(article, label)] = (sim, cap)
            if core_sigma is not None:
                core_sigma_seen = core_sigma
            print(f"  {article}/{label}: done ({time.time()-t0:.1f}s elapsed)", flush=True)

    print(f"\ncore-fill assertion: sigma_e(r<r_in) = {core_sigma_seen} (non-vacuum, PASS)", flush=True)

    # ---- Gate P-QUANTUM-4/5: field superposition (vacuum reconfirm + object primary claim) ----
    ez_beam_e = sc.phasors(caps[("empty", "beam")][1])["ez"]
    ez_off_e = sc.phasors(caps[("empty", "off_axis")][1])["ez"]
    ez_joint_e = sc.phasors(caps[("empty", "joint")][1])["ez"]
    resid_empty = rms(ez_joint_e - (ez_beam_e + ez_off_e)) / rms(ez_joint_e)

    ez_beam = sc.phasors(caps[("object", "beam")][1])["ez"]
    ez_off = sc.phasors(caps[("object", "off_axis")][1])["ez"]
    ez_joint = sc.phasors(caps[("object", "joint")][1])["ez"]
    resid_object = rms(ez_joint - (ez_beam + ez_off)) / rms(ez_joint)

    # ---- Gate P-QUANTUM-6: empirical radial-ledger closure, joint scene ----
    sim_j, cap_j = caps[("object", "joint")]
    _, cap_j_e = caps[("empty", "joint")]
    wj = sc.widths(cap_j, cap_j_e, dg.BEAM_BOX_A, dg.BEAM_REF)
    p_abs_box = wj["sigma_abs"] * wj["i_inc"]
    centers, bins_j, total_j = sc.radial_absorbed_power(
        cap_j, sim_j.sigma_e, dg.BEAM_CX, dg.BEAM_CY, dg.R_OUT, n_bins=dg.RADIAL_N_BINS)
    closure = abs(total_j - p_abs_box) / abs(p_abs_box)

    # ---- P-QUANTUM-7/9: coherent interference cross-term (informational, renormalized -- fix 2) ----
    sim_beam, cap_beam = caps[("object", "beam")]
    sim_off, cap_off = caps[("object", "off_axis")]
    _, cap_beam_e = caps[("empty", "beam")]
    _, cap_off_e = caps[("empty", "off_axis")]

    w_beam = sc.widths(cap_beam, cap_beam_e, dg.BEAM_BOX_A, dg.BEAM_REF)
    w_off = sc.widths(cap_off, cap_off_e, dg.BEAM_BOX_A, dg.BEAM_REF)
    p_abs_beam = w_beam["sigma_abs"] * w_beam["i_inc"]
    p_abs_off = w_off["sigma_abs"] * w_off["i_inc"]
    p_int = p_abs_box - (p_abs_beam + p_abs_off)
    p_int_frac_of_beam = p_int / p_abs_beam            # fix 2: renormalized denominator

    _, bins_beam, total_beam = sc.radial_absorbed_power(
        cap_beam, sim_beam.sigma_e, dg.BEAM_CX, dg.BEAM_CY, dg.R_OUT, n_bins=dg.RADIAL_N_BINS)
    _, bins_off, total_off = sc.radial_absorbed_power(
        cap_off, sim_off.sigma_e, dg.BEAM_CX, dg.BEAM_CY, dg.R_OUT, n_bins=dg.RADIAL_N_BINS)
    bins_naive = bins_beam + bins_off
    bin_delta = bins_j - bins_naive
    # P-QUANTUM-9 (fix 6, recommended by Red Team, folded in): bin-wise closure the
    # aggregate check alone can't see -- Ez-level equality (Gate Q2) does NOT imply
    # p_J=0.5*sigma*|Ez|^2 is bin-wise additive, since p_J is quadratic in Ez.
    nonzero = bins_naive > 0
    peak_bin_idx = int(np.argmax(np.abs(bin_delta[nonzero]))) if nonzero.any() else -1
    peak_bin_idx_full = int(np.arange(len(bins_naive))[nonzero][peak_bin_idx]) if nonzero.any() else -1
    peak_local_frac = (float(bin_delta[peak_bin_idx_full] / bins_naive[peak_bin_idx_full])
                       if peak_bin_idx_full >= 0 else float("nan"))
    aggregate_frac = p_int_frac_of_beam

    out = {
        "meta": {
            "amp_rel": dg.AMP_REL, "amp_beam": dg.AMP_BEAM, "amp_offaxis": dg.AMP_OFFAXIS,
            "offaxis_angle_deg": dg.OFFAXIS_ANGLE_DEG,
            "p_int_ceiling_frac_of_beam": dg.P_INT_CEILING_FRAC_OF_BEAM,
            "note_naming": ("second source role is 'off_axis', NOT 'ambient' (fix 5) -- this "
                           "experiment does not touch lab/ambient.py, computes no Weber contrast, "
                           "and does not reproduce C. It DEFERS the beam+ambient-C-reproduction "
                           "half of Iteration 1's own committed bridge-gate design (LOGBOOK.md "
                           "docket #4/(b)); not built this cycle."),
            "core_fill_sigma_at_center": core_sigma_seen,
            "elapsed_s": time.time() - t0, "n_new_runs": 6,
        },
        "gate_Q4_vacuum_superposition_rms_rel": resid_empty,
        "gate_Q5_object_superposition_rms_rel": resid_object,
        "gate_Q6_radial_closure_joint_scene": closure,
        "p_abs_box_joint": p_abs_box, "p_abs_beam": p_abs_beam, "p_abs_offaxis": p_abs_off,
        "p_int": p_int, "p_int_frac_of_beam": p_int_frac_of_beam,
        "bins_joint": bins_j.tolist(), "bins_naive_sum": bins_naive.tolist(),
        "bin_centers": centers.tolist(), "peak_bin_idx": peak_bin_idx_full,
        "peak_local_frac_of_naive": peak_local_frac,
        "aggregate_frac_of_beam": aggregate_frac,
        "abs_ext_ratio_object_beam": w_beam["sigma_abs"] / w_beam["sigma_ext"],
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1)

    print(f"\nGate Q4 (vacuum superposition, reconfirm):  {resid_empty:.3e}")
    print(f"Gate Q5 (object superposition, primary):     {resid_object:.3e}")
    print(f"Gate Q6 (radial closure, joint scene):        {closure:.4f}")
    print(f"P-QUANTUM-7 (interference, /P_abs(beam)):     {p_int_frac_of_beam*100:.4f}%  "
          f"(ceiling {dg.P_INT_CEILING_FRAC_OF_BEAM*100:.4f}%)")
    print(f"P-QUANTUM-9 (peak local bin /naive bin sum):  {peak_local_frac*100:.4f}%  "
          f"(bin r={centers[peak_bin_idx_full]:.2f})")
    print(f"abs_ext_ratio (object+beam only):             {out['abs_ext_ratio_object_beam']:.4f}")
    print("\nresults.json written")


if __name__ == "__main__":
    main()
