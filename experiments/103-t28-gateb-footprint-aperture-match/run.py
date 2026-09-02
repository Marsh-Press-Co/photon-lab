"""exp-103 -- The Footprint- and Aperture-Matched Gate B Rebuild.
Panel Iteration 80. Lead seat (rotation): MATERIALS & METAMATERIALS. Frozen
spec: NOTES.md (Predictions committed to git strictly BEFORE this file's
first real run, house discipline). Change rationale: phase2_redteam_audit.md
(4 Red Team findings + rulings on 5 blind critiques, 8 mandatory fixes
adopted, 1 (QUANTUM's phase-resampling remedy) explicitly overridden as a
zero-information no-op).

Instrument-repair cycle, diagnostic only -- T1: N/A, zero `lab/` diff, no
mechanism proposed or varied.

DISCLAIMER (Phase-2 mandatory fix 8, VISION/Red Team, Checkpoint-4-adjacent
constraint-3 drift risk closed): kappa_window/kappa_region are raw physical
intensity ratios; no Weber-contrast or C_thr(L) perceptual scoring is
performed this cycle.

DISCLOSURE (Phase-2 mandatory fix 7, THERMODYNAMICS/Red Team): thermal
sidecar NOT invoked -- `thermo_sidecar.absorbed_power_established_ratio`'s
own `p_abs_w` derives from `sigma_ext_cells` (exp-059's Mie/qext-theory
extinction-width calculation) times an externally assumed
`i_incident_w_cm2` -- neither input reads this file's FDTD source
construction, amplitude, or `edge` parameter (verified directly against
`lab/thermo_sidecar.py:124-168`), so this cycle's aperture change cannot
silently stale the existing 699.27x thermal-UNDETECTABLE citation
(exp-057). This file imports nothing from `lab.thermo_sidecar`.

RESOLUTION NOTE (Phase-2 mandatory fix 1, Red Team's own top-ranked,
load-bearing finding -- corrects the Phase-1 proposal's original edge=80
choice): `R4_TAPER=80` (`experiments/069-.../design_geometry.py`) is
`round(TAPER * R4_RATIO)` = `round(40 * 2.0)`, deliberately rescaled UP
from the base `TAPER=40` (`experiments/065-.../design_geometry.py`)
specifically because the R4 family runs at DOUBLE this file's own
cells_per_lambda (R4_CPL[600]=40 vs this file's CPL_600=20) -- R4_TAPER=80
cells at cpl=40 represents the SAME 2-wavelength PHYSICAL taper width as
TAPER=40 cells at cpl=20. Reusing R4_TAPER=80 unchanged at this file's own
cpl=20 grid would give a 4-wavelength taper, TWICE the R4 family's actual
physical aperture -- reintroducing, one level down, exactly the kind of
unexamined cross-resolution-constant confound this whole cycle exists to
retire (the identical bug species this file's own D_STANDOFF/H_REGION
rescaling, inherited correctly from exp-102, already guards against).
Corrected: `EDGE = TAPER = 40` -- the value actually calibrated for this
file's own cpl=20 grid, giving genuine physical-aperture-width fidelity
with the R4 family's own edge=80-at-cpl=40 construction.

DISCLOSURE (Phase-2 mandatory fix 4, Red Team's own finding): `kappa_window`
(this file, `sc.phasors()`, a trig-corrected two-snapshot quadrature
phasor -- see `lab/emit.py::_phasor`) and the established `beam_behind`
figure (`experiments/001-.../run.py`, `Sim.envelope()`,
`sqrt(snap_a**2+snap_b**2)`, UNCORRECTED) are related but not identical
amplitude-reconstruction conventions. At this file's own grid numbers
(lam=20 cells, S=0.32/sqrt(2)~=0.2263, quarter=round(lam/S/4)=22,
omega~=0.07111 => phi=omega*22~=1.5644 rad vs exact pi/2=1.5708),
`envelope()`'s uncorrected Pythagorean sum carries a small
(cos(phi)~=0.0064, up to ~0.6% relative in the worst-case phase
relationship) quantization bias that `kappa_window` (phasor-corrected) does
not -- relevant context if kappa_window lands outside the predicted band on
the low side; does not by itself invalidate the comparison.

Fixes both real Gate-B defects exp-102 (Panel Iteration 79) diagnosed
honestly rather than force-fixing: (1) the point/region sample and the
established `beam_behind` figure's own wide-window average were taken at
different effective standoffs (near-field shadow fills in with distance --
not comparable); (2) Gate B's own source construction silently used
`edge=24` (the `add_line_source` code default) instead of a physically
matched aperture. ONE new field capture (empty + article, theta=0, native
flagship geometry) is reused for both the footprint-matched window
reproduction (`kappa_window`, scored against the literal established
`BEHIND` slice) and an 11-point standoff trend (`kappa_region`) from the
near-field gap identified last cycle out through the window itself. A
SECOND new field capture pair, at 2x STEPS, provides a genuine
settling-independence check on all 5 near-field points (Phase-2 mandatory
fix 6, EM/Red Team) at zero marginal FDTD cost beyond that one pair, since
`full_capture()` returns the whole field and every point reading is
post-processing arithmetic on it.
"""

import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)

from lab import Sim, materials                      # noqa: E402
from lab import sections as sc                       # noqa: E402


# ================================================================ Gate B / native-scale flagship geometry (verbatim from exp-001/002)
N = 560
ABSORB = 40
COURANT_FRAC = 0.32
STEPS = 3200
STEPS_2X = 6400
SRC_X = 64
CX, CY = 252, 280
R_CORE, R_COAT, R_CLK = 30, 78, 90
CPL_600 = 20
EDGE = 40  # TAPER (experiments/065-.../design_geometry.py), the value
           # actually calibrated for a cpl=20 grid -- physically matches
           # the R4 family's own edge=80-at-cpl=40 (2-wavelength taper),
           # NOT a literal reuse of R4_TAPER=80 (Phase-2 mandatory fix 1).

# Established BEHIND window, byte-for-byte from experiments/001-.../run.py:
# BEHIND = (slice(CX+R_CLK+15, CX+R_CLK+115), slice(CY-20, CY+20))
BEHIND_X_LO = CX + R_CLK + 15   # 357
BEHIND_X_HI = CX + R_CLK + 115  # 457
BEHIND_Y_LO = CY - 20           # 260
BEHIND_Y_HI = CY + 20           # 300
assert (BEHIND_X_LO, BEHIND_X_HI, BEHIND_Y_LO, BEHIND_Y_HI) == (357, 457, 260, 300)

# exp-102's own Gate-B-corrected near-field reference point (rescaled
# D_STANDOFF=100 cells from center at GATEB_R_COAT=78 -> x=CX+100=352).
# This is a STANDOFF ratio, independent of the edge/aperture-width
# question fix 1 corrects -- unchanged from exp-102's own derivation.
GATEB_CORRECTED_X = CX + 100
assert GATEB_CORRECTED_X == 352

# Standoff sample x-values (Phase-2 mandatory fix 5, PHOTONICS/Red Team:
# <=10-cell / lambda/2 pitch on the window-spanning leg, the cheaper of
# the two ruled-sufficient options, taken alongside -- not instead of --
# reporting kappa_window's own internal spatial variance below).
NEAR_FIELD_X = [352, 353, 354, 355, 356]
WINDOW_SPAN_X = [357, 367, 377, 387, 397, 407, 417, 427, 437, 447, 456]
ALL_X = NEAR_FIELD_X + WINDOW_SPAN_X
assert len(ALL_X) == len(set(ALL_X)) == 16
assert max(np.diff(sorted(WINDOW_SPAN_X))) <= 10, "window-spanning pitch must be <=10 cells (Nyquist fix)"
assert BEHIND_X_LO <= min(WINDOW_SPAN_X) and max(WINDOW_SPAN_X) < BEHIND_X_HI

H_REGION = 5    # Gate B/exp-102's own established small-block convention,
                # UNRESCALED (this cycle reuses Gate B's own r_out=78
                # object exactly -- the r_out-ratio rescale exp-102 needed
                # for other geometries is exactly 1 here, skipped as a
                # documented no-op rather than silently reapplied).
FLOOR_FRAC = 0.10
STABILITY_TOL = 0.20  # settling-independence tolerance (fix 6): relative
                       # change in kappa_region between STEPS and STEPS_2X
                       # at the 5 near-field points must stay below this.


def _run(with_article, steps):
    sim = Sim(N, N, cells_per_lambda=CPL_600, courant_frac=COURANT_FRAC, absorb=ABSORB)
    if with_article:
        materials.pec_disk(sim, CX, CY, R_CORE)
        materials.graded_black_shell(sim, CX, CY, R_CORE, R_COAT)  # sigma_max=0.5 default, unchanged
    sim.add_line_source(SRC_X, angle_deg=0.0, profile="plane", edge=EDGE)
    sim.run(steps)
    return sc.full_capture(sim)


def block_mean_intensity(ez, x, y, h):
    xs = slice(x - h, x + h + 1)
    ys = slice(y - h, y + h + 1)
    block = np.abs(ez[xs, ys]) ** 2
    return float(np.mean(block))


def kappa_region_at(ez_empty, ez_article, x, y, h):
    i_e = block_mean_intensity(ez_empty, x, y, h)
    i_a = block_mean_intensity(ez_article, x, y, h)
    return (i_a / i_e if i_e != 0 else float("inf")), i_e, i_a


def window_stats(ez, x_lo, x_hi, y_lo, y_hi):
    block = np.abs(ez[x_lo:x_hi, y_lo:y_hi]) ** 2
    return dict(mean=float(np.mean(block)), std=float(np.std(block)),
                min=float(np.min(block)), max=float(np.max(block)))


def main():
    print("=" * 78)
    print("exp-103 -- Footprint- and aperture-matched Gate B rebuild")
    print("=" * 78)
    print("\nDISCLAIMER (Phase-2 mandatory fix 8): kappa_window/kappa_region are raw "
          "physical intensity ratios; no Weber-contrast or C_thr(L) perceptual "
          "scoring is performed this cycle.")
    print("\nDISCLOSURE (Phase-2 mandatory fix 7): thermal sidecar NOT invoked -- "
          "p_abs_w (thermo_sidecar.absorbed_power_established_ratio) derives from "
          "sigma_ext_cells (exp-059 Mie/qext theory) x an assumed i_incident_w_cm2, "
          "independent of this file's FDTD source `edge` parameter; this file "
          "imports nothing from lab.thermo_sidecar.")
    print(f"\nEDGE={EDGE} (Phase-2 mandatory fix 1: TAPER=40, the cpl=20-calibrated "
          f"value, physically matches the R4 family's own edge=80-at-cpl=40 "
          f"2-wavelength taper -- NOT a literal reuse of R4_TAPER=80).")

    t_start = time.time()
    n_fdtd_calls = 0

    # ---------------------------------------------------------- margin check (R17-style, direct geometry)
    for x in ALL_X:
        lo_x, hi_x = x - H_REGION, x + H_REGION
        assert lo_x > ABSORB and hi_x < N - ABSORB, f"x={x} block too close to absorb/boundary"
    lo_y, hi_y = CY - H_REGION, CY + H_REGION
    assert lo_y > ABSORB and hi_y < N - ABSORB
    print(f"\n[margin gate] {len(ALL_X)} standoff points, all clear of absorb/boundary: PASS")

    # ============================================================
    # Primary pair -- STEPS=3200, edge=40 (2 real FDTD calls)
    # ============================================================
    print(f"\n-- Primary pair: empty + article, theta=0, STEPS={STEPS}, edge={EDGE} --")
    t0 = time.time()
    cap_empty = _run(with_article=False, steps=STEPS)
    cap_article = _run(with_article=True, steps=STEPS)
    n_fdtd_calls += 2
    wall_primary = time.time() - t0
    print(f"Primary pair wall time: {wall_primary:.1f}s")

    ez_empty = sc.phasors(cap_empty)["ez"]
    ez_article = sc.phasors(cap_article)["ez"]

    # ============================================================
    # kappa_window -- literal established BEHIND footprint (Tier 1 item 2)
    # ============================================================
    print("\n" + "=" * 78)
    print("KAPPA_WINDOW -- literal established BEHIND footprint")
    print("=" * 78)
    win_empty = window_stats(ez_empty, BEHIND_X_LO, BEHIND_X_HI, BEHIND_Y_LO, BEHIND_Y_HI)
    win_article = window_stats(ez_article, BEHIND_X_LO, BEHIND_X_HI, BEHIND_Y_LO, BEHIND_Y_HI)
    kappa_window = win_article["mean"] / win_empty["mean"]
    print(f"window empty:   mean={win_empty['mean']:.6e}  std={win_empty['std']:.6e}  "
          f"min={win_empty['min']:.6e}  max={win_empty['max']:.6e}")
    print(f"window article: mean={win_article['mean']:.6e}  std={win_article['std']:.6e}  "
          f"min={win_article['min']:.6e}  max={win_article['max']:.6e}")
    print(f"kappa_window = {kappa_window:.6e}  ({kappa_window*100:.4f}%)")
    # internal spatial-variance report (Phase-2 mandatory fix 5, cheaper option)
    kappa_window_pointwise = (np.abs(ez_article[BEHIND_X_LO:BEHIND_X_HI, BEHIND_Y_LO:BEHIND_Y_HI]) ** 2
                               / np.abs(ez_empty[BEHIND_X_LO:BEHIND_X_HI, BEHIND_Y_LO:BEHIND_Y_HI]) ** 2)
    kw_pw_mean = float(np.mean(kappa_window_pointwise))
    kw_pw_std = float(np.std(kappa_window_pointwise))
    kw_pw_min = float(np.min(kappa_window_pointwise))
    kw_pw_max = float(np.max(kappa_window_pointwise))
    print(f"kappa_window pointwise ratio (internal spread): mean={kw_pw_mean:.6e} "
          f"std={kw_pw_std:.6e} min={kw_pw_min:.6e} max={kw_pw_max:.6e} "
          f"(std/mean={kw_pw_std/abs(kw_pw_mean):.4f})")

    # ============================================================
    # kappa_region -- 16-point standoff trend (Tier 1 item 1)
    # ============================================================
    print("\n" + "=" * 78)
    print("KAPPA_REGION -- 16-point standoff trend (STEPS=3200)")
    print("=" * 78)
    trend = {}
    for x in ALL_X:
        k, i_e, i_a = kappa_region_at(ez_empty, ez_article, x, CY, H_REGION)
        trend[x] = dict(kappa_region=k, i_region_empty=i_e, i_region_article=i_a)
        print(f"  x={x:4d}  kappa_region={k:.6e}  i_empty={i_e:.4e}  i_article={i_a:.4e}")

    # ============================================================
    # Floor gate (R13/R14 lineage, house style -- exp-102's own
    # floor_gate() convention exactly: RMS across the pool of the
    # points' own local i_region_empty readings, Phase-2 mandatory fix 3)
    # ============================================================
    print("\n" + "=" * 78)
    print("FLOOR GATE (RMS across the 16-point pool's own local i_region_empty readings)")
    print("=" * 78)
    empty_vals = np.array([trend[x]["i_region_empty"] for x in ALL_X])
    rms = float(np.sqrt(np.mean(empty_vals ** 2)))
    floor = FLOOR_FRAC * rms
    for x in ALL_X:
        passed = trend[x]["i_region_empty"] >= floor
        trend[x]["floor_pass"] = bool(passed)
        trend[x]["outcome"] = "resolved" if passed else "UNRESOLVED-BY-CONSTRUCTION"
    n_unresolved = sum(1 for x in ALL_X if not trend[x]["floor_pass"])
    print(f"rms={rms:.6e}  floor={floor:.6e}  n_unresolved={n_unresolved}/{len(ALL_X)}")

    # ============================================================
    # Settling-independence leg (Phase-2 mandatory fix 6, EM/Red Team)
    # -- 2 MORE real FDTD calls at STEPS_2X=6400, ALL 5 near-field points
    # checked at zero marginal FDTD cost (whole-field capture reused).
    # ============================================================
    print("\n" + "=" * 78)
    print(f"SETTLING-INDEPENDENCE LEG -- all 5 near-field points re-read at STEPS={STEPS_2X}")
    print("=" * 78)
    t0 = time.time()
    cap_empty_2x = _run(with_article=False, steps=STEPS_2X)
    cap_article_2x = _run(with_article=True, steps=STEPS_2X)
    n_fdtd_calls += 2
    wall_2x = time.time() - t0
    print(f"2x-STEPS pair wall time: {wall_2x:.1f}s")
    ez_empty_2x = sc.phasors(cap_empty_2x)["ez"]
    ez_article_2x = sc.phasors(cap_article_2x)["ez"]

    settling = {}
    settling_pass = True
    for x in NEAR_FIELD_X:
        k1 = trend[x]["kappa_region"]
        k2, i_e2, i_a2 = kappa_region_at(ez_empty_2x, ez_article_2x, x, CY, H_REGION)
        rel_change = abs(k2 - k1) / abs(k1) if k1 != 0 else float("inf")
        cell_pass = rel_change <= STABILITY_TOL
        settling_pass = settling_pass and cell_pass
        settling[x] = dict(kappa_region_1x=k1, kappa_region_2x=k2,
                            rel_change=rel_change, cell_pass=cell_pass)
        print(f"  x={x:4d}  kappa@1x={k1:.6e}  kappa@2x={k2:.6e}  "
              f"rel_change={rel_change:.4%}  PASS(<={STABILITY_TOL:.0%})={cell_pass}")
    print(f"[settling gate] OVERALL PASS = {settling_pass}")

    # ============================================================
    # Predictions
    # ============================================================
    print("\n" + "=" * 78)
    print("PREDICTIONS")
    print("=" * 78)

    # Prediction (i): kappa_window in [0.005, 0.04]
    p1_lo, p1_hi = 0.005, 0.04
    p1_verdict = "CONFIRMED" if p1_lo <= kappa_window <= p1_hi else "FALSIFIED"
    print(f"\n[Prediction i] kappa_window in [{p1_lo},{p1_hi}]: {kappa_window:.6e}  "
          f"VERDICT={p1_verdict}")

    # Prediction (ii): monotonic rise, at most one local reversal (floor-gated points only, in x order)
    resolved_x = [x for x in ALL_X if trend[x]["floor_pass"]]
    resolved_x_sorted = sorted(resolved_x)
    vals = [trend[x]["kappa_region"] for x in resolved_x_sorted]
    reversals = 0
    for i in range(1, len(vals)):
        # a "reversal" is a decrease exceeding the floor-scale noise tolerance
        if vals[i] < vals[i - 1] * (1 - FLOOR_FRAC):
            reversals += 1
    p2_verdict = "CONFIRMED" if reversals <= 1 else "FALSIFIED"
    print(f"\n[Prediction ii] monotonic rise, <=1 reversal: reversals={reversals}  "
          f"VERDICT={p2_verdict}")
    for x in resolved_x_sorted:
        print(f"    x={x}: kappa_region={trend[x]['kappa_region']:.6e}")

    # Prediction (iii): floor gate at all points + window-spanning mean within ~2x of kappa_window
    p3a_pass = n_unresolved == 0
    span_vals = [trend[x]["kappa_region"] for x in WINDOW_SPAN_X]
    span_mean = float(np.mean(span_vals))
    ratio = max(span_mean, kappa_window) / min(span_mean, kappa_window) if kappa_window != 0 else float("inf")
    p3b_pass = ratio <= 2.0
    p3_verdict = "CONFIRMED" if (p3a_pass and p3b_pass) else "FALSIFIED"
    print(f"\n[Prediction iii] floor gate all-clear={p3a_pass}, window-span mean "
          f"{span_mean:.6e} vs kappa_window {kappa_window:.6e} ratio={ratio:.3f} "
          f"(<=2.0)={p3b_pass}  VERDICT={p3_verdict}")

    # Prediction (iv): settling-independence gate (all 5 near-field points)
    p4_verdict = "CONFIRMED" if settling_pass else "FALSIFIED"
    print(f"\n[Prediction iv] settling-independence (STEPS 3200 vs 6400, all 5 "
          f"near-field points, <={STABILITY_TOL:.0%} tolerance): VERDICT={p4_verdict}")

    total_wall = time.time() - t_start
    print(f"\nTotal wall time: {total_wall:.1f}s ({total_wall/60.0:.2f} min)")
    print(f"Real FDTD calls: {n_fdtd_calls} (expected 4 = 2 primary + 2 settling-check)")
    print(f"Reported kappa_region readings: {len(ALL_X)} (11 standoff points; the "
          f"settling-independence leg additionally re-reads all 5 near-field points "
          f"from the SAME 2 settling-check calls, zero marginal FDTD cost) "
          f"[Phase-2 mandatory fix 2, R19]")
    assert n_fdtd_calls == 4, f"R19 call-count assert: expected 4, got {n_fdtd_calls}"
    assert len(ALL_X) == 16, f"R19 row-count assert: expected 16 kappa_region readings, got {len(ALL_X)}"
    assert len(NEAR_FIELD_X) == 5, "R19 row-count assert: expected 5 settling-check readings"

    result = dict(
        experiment="exp-103", panel_iteration=80,
        n_fdtd_calls=n_fdtd_calls, wall_primary_s=wall_primary, wall_2x_s=wall_2x,
        total_wall_s=total_wall,
        geometry=dict(N=N, absorb=ABSORB, courant_frac=COURANT_FRAC, steps=STEPS,
                      steps_2x=STEPS_2X, src_x=SRC_X, cx=CX, cy=CY, r_core=R_CORE,
                      r_coat=R_COAT, cpl=CPL_600, edge=EDGE, h_region=H_REGION,
                      floor_frac=FLOOR_FRAC, stability_tol=STABILITY_TOL),
        behind_window=dict(x_lo=BEHIND_X_LO, x_hi=BEHIND_X_HI, y_lo=BEHIND_Y_LO, y_hi=BEHIND_Y_HI),
        kappa_window=dict(value=kappa_window, empty=win_empty, article=win_article,
                          pointwise_mean=kw_pw_mean, pointwise_std=kw_pw_std,
                          pointwise_min=kw_pw_min, pointwise_max=kw_pw_max),
        kappa_region_trend={str(x): trend[x] for x in ALL_X},
        floor_gate=dict(rms=rms, floor=floor, n_unresolved=n_unresolved),
        settling_check={str(x): settling[x] for x in NEAR_FIELD_X},
        predictions=dict(
            p1_kappa_window=dict(verdict=p1_verdict, value=kappa_window, band=[p1_lo, p1_hi]),
            p2_monotonic_trend=dict(verdict=p2_verdict, reversals=reversals),
            p3_floor_and_span_consistency=dict(verdict=p3_verdict, floor_all_clear=p3a_pass,
                                                span_mean=span_mean, ratio_to_window=ratio),
            p4_settling_independence=dict(verdict=p4_verdict, overall_pass=settling_pass),
        ),
    )
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(result, f, indent=2, default=str)
    print("\nresults.json written.")
    return result


if __name__ == "__main__":
    main()
