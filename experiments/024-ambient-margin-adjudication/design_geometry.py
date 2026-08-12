"""exp-024 design calculation — instrument-margin fix + estimator adjudication.
=============================================================================
Panel Iteration 2 (lead: PHOTONICS). Fixes exp-020's λ-dependent fringe-zone
floor (δ_C = 0.0009/0.0068/0.0183 @ 450/600/750nm, breaking P1a/P1b at
600/750nm) by widening the transverse domain so the flat-lit source clears
the Fresnel edge-fringe zone by a wide, SAFE margin at every committed angle
and wavelength — not the thin 0.38%-over-rule pad Phase-1 (PHOTONICS)
proposed and Red Team's Phase-2 backtest showed was unsafe.

Red Team's Phase-2 finding (verified independently below, in NOTES.md):
backtesting PHOTONICS' own bracketing δ_C(ratio) extrapolation models
against exp-020's OWN three measured (ratio, δ_C) points underpredicts
δ_C by 5.7-15.7x near ratio~1 — the true behavior there is EM's own
"twentyfold cancellation collapse" threshold, not a smooth power law.
Director's synthesis: don't trust any extrapolation near that threshold —
push the margin/fringe ratio well clear of it instead. MARGIN_MULT raised
from PHOTONICS' 2.0 (EM's original Phase-5 rule) to 3.5, chosen so the new
worst-case ratio (450nm, historically the SAFE end) still grows and the
750nm ratio — the historically dangerous end — clears 3x the point where
Iteration-1 data was already reliable (ratio 1.21 -> delta_C 0.0009).

Also derives BOX programmatically (Red Team #6 / Thermo's catch: exp-020's
harness hand-tracked this constant) and prints the N17-angle-set geometric
ceiling (Red Team's zero-run rider, reconfirmed at the new geometry --
depends only on R_OUT/LEVER/windows, not NY, so unchanged from exp-020).

Pure geometry -- no FDTD, no measurement. Run it; the numbers it prints are
the ones committed in NOTES.md.
"""

import numpy as np

# ----------------------------------------------------------- pinned geometry
MARGIN_MULT = 3.5           # coverage-margin safety factor (Director's Phase-3
                             # ruling; EM's original rule was 2.0, Red Team's
                             # flip suggested 3.0 -- widened further given the
                             # backtest showing the extrapolation near ratio~1
                             # cannot be trusted at any single exponent)
NX = 360                     # cells (x = propagation) -- unchanged from exp-020
ABSORB = 40                  # graded damping bands
CPL = {450: 15, 600: 20, 750: 25}   # cells per lambda by wavelength (nm)
SRC_X = 300                  # far-side line source (ambient back-light)
TAPER = 40                   # cosine taper cells at each source end
R_OUT = 78                   # outer radius, all articles (2.34 um at D=30nm)
PLANE_DX = 15                # measurement plane: 15 cells observer-side of edge
OBJ_X = 170                  # object center x (unchanged)
PLANE_X = OBJ_X - R_OUT - PLANE_DX          # = 77
SENS_PLANES = (12, 15, 16)   # plane-distance sensitivity rows
ANGLES = (-40, -30, -20, -10, 0, 10, 20, 30, 40)   # committed N = 9
N17_EXTRA = (-35, -25, -15, -5, 5, 15, 25, 35)     # convergence/rider set @600nm
FALLBACK_ANGLES = (-35, -25, -15, -5, 0, 5, 15, 25, 35)  # pre-committed ±35 fallback (N=9, kept odd for symmetry+0)

# windows (relative to object center y0) -- unchanged from exp-020 (a property
# of R_OUT/LEVER, not of NY):
W_OBJ = 78
GUARD_OUT = 185
W_FLANK = 78
FLANK = (GUARD_OUT, GUARD_OUT + W_FLANK)     # (185, 263)

# BOX ledger clearance -- Red Team #6 / Thermo: derive, don't hand-track.
# exp-020's BOX (80,260,510,690) around OBJ (170,600) reconstructs to exactly
# a 12-cell clearance past R_OUT on every wall; codified here.
BOX_CLEARANCE = 12

# dilute-sponge calibration article (materials seat, adopted, unchanged):
SPONGE_TAU_CENTER = 0.10
SIGMA_SPONGE = SPONGE_TAU_CENTER / (2 * R_OUT)

LEVER = OBJ_X - PLANE_X      # object CENTER to plane = 93 cells (EM's number)
D_SP = SRC_X - PLANE_X       # source to plane = 223 cells (walk-off baseline)


def required_ny(margin_mult, lam_max_cpl=25):
    """Smallest NY (object centered at NY/2) whose ±40 deg margin clears
    margin_mult * sqrt(lam_max_cpl * D_SP), given the fixed span half-width
    (FLANK[1] = 263) and fixed walk-off geometry."""
    walk40 = D_SP * np.tan(np.radians(40.0))
    rule = margin_mult * np.sqrt(lam_max_cpl * D_SP)
    # margin(NY) = NY/2 - (FLANK[1] + TAPER + ABSORB + walk40)   [see lit_interval/
    # shadow span algebra below -- this is the closed form of that expression]
    const = FLANK[1] + TAPER + ABSORB + walk40
    ny_min = 2 * (const + rule)
    return ny_min, rule, walk40


# ---- module-level geometry (computed at import time, so run.py can just
# `import design_geometry as dg` and use dg.NY / dg.OBJ / dg.SRC_Y / dg.BOX
# directly, exp-020's pattern) ------------------------------------------
_ny_min, _rule750, _walk40 = required_ny(MARGIN_MULT)
NY = int(np.ceil(_ny_min / 8.0) * 8)        # round up to a multiple of 8
OBJ = (OBJ_X, NY // 2)
SRC_Y = (ABSORB, NY - ABSORB)
BOX = (OBJ_X - R_OUT - BOX_CLEARANCE, OBJ_X + R_OUT + BOX_CLEARANCE,
       OBJ[1] - R_OUT - BOX_CLEARANCE, OBJ[1] + R_OUT + BOX_CLEARANCE)


def lit_interval(theta_deg, ny, srcy):
    walk = D_SP * np.tan(np.radians(theta_deg))
    lo = srcy[0] + TAPER + walk
    hi = srcy[1] - TAPER + walk
    return lo, hi


def shadow_interval(theta_deg, y0):
    off = LEVER * np.tan(np.radians(theta_deg))
    hw = R_OUT / np.cos(np.radians(theta_deg))
    return y0 + off - hw, y0 + off + hw


def window_means(theta_list, weights, y0, ny, transmission=None):
    y = np.arange(ny, dtype=float)
    obj_w = (np.abs(y - y0) <= W_OBJ)
    flank_w = (np.abs(y - y0) >= FLANK[0]) & (np.abs(y - y0) <= FLANK[1])
    b_obj, b_flank, wsum = 0.0, 0.0, 0.0
    for th, w in zip(theta_list, weights):
        lo, hi = shadow_interval(th, y0)
        b = np.ones(ny)
        if transmission is None:
            b[(y >= lo) & (y <= hi)] = 0.0
        else:
            off = LEVER * np.tan(np.radians(th))
            yc = y - (y0 + off)
            inside = np.abs(yc) < R_OUT / np.cos(np.radians(th))
            chord = np.zeros(ny)
            perp = yc * np.cos(np.radians(th))
            chord[inside] = 2.0 * np.sqrt(np.maximum(R_OUT**2 - perp[inside]**2, 0.0))
            b = np.exp(-SIGMA_SPONGE * chord)
        b_obj += w * b[obj_w].mean()
        b_flank += w * b[flank_w].mean()
        wsum += w
    b_obj /= wsum
    b_flank /= wsum
    return b_obj, b_flank, (b_obj - b_flank) / b_flank


def main():
    print(f"MARGIN_MULT = {MARGIN_MULT}  (coverage rule: m >= {MARGIN_MULT} * "
          f"sqrt(lam_max_cpl * D_source_to_plane))")
    print(f"D_source->plane = {D_SP}, walk(40deg) = {_walk40:.2f}, "
          f"rule (750nm) = {_rule750:.2f} cells")
    print(f"required NY (exact) = {_ny_min:.2f} -> rounding up")
    print(f"NY (chosen, rounded up to x8) = {NY}  [module-level constant]")

    y0 = OBJ[1]
    span = (y0 - FLANK[1], y0 + FLANK[1])
    print(f"\ngeometry: {NX}x{NY}, absorb {ABSORB}, source x={SRC_X} "
          f"y=[{SRC_Y[0]},{SRC_Y[1]}] taper {TAPER}, object {OBJ} r={R_OUT}, "
          f"plane x={PLANE_X} (lever {LEVER}), D_source->plane={D_SP}")
    print(f"analysis span: y in [{span[0]}, {span[1]}]  "
          f"(obj +-{W_OBJ}, guard ->{GUARD_OUT}, flanks {FLANK})")

    # ---- coverage check at all 17 angles + the fallback set -------------
    ok = True
    print("\nsource coverage at the plane (flat part only), N17 angle set:")
    margins = {}
    for th in sorted(set(ANGLES) | set(N17_EXTRA)):
        lo, hi = lit_interval(th, NY, SRC_Y)
        covered = lo <= span[0] and hi >= span[1]
        margin = min(span[0] - lo, hi - span[1])
        margins[th] = margin
        ok &= covered
        print(f"  theta={th:+03d}deg  lit=[{lo:7.1f},{hi:7.1f}]  "
              f"margin={margin:7.2f}  {'OK' if covered else 'FAIL'}")
    assert ok, "analysis span not fully lit at some committed angle"

    worst_margin = min(margins.values())
    for lam_nm, cpl in CPL.items():
        fringe = np.sqrt(cpl * D_SP)
        ratio = worst_margin / fringe
        print(f"  fringe zone @ {lam_nm}nm: sqrt({cpl}*{D_SP}) = {fringe:.2f} "
              f"cells; worst-margin/fringe ratio = {ratio:.3f}  "
              f"(exp-020 had {69.9/fringe*(20/cpl)**0 :.2f}... see NOTES for exp-020 comparison)")

    assert span[0] > ABSORB + 20 and span[1] < NY - ABSORB - 20, \
        "windows too close to damping bands"

    # ---- opaque-article ray trace (ceilings unaffected by NY) -----------
    w_eq9 = np.ones(len(ANGLES))
    w_cos9 = np.cos(np.radians(ANGLES))
    a17 = sorted(list(ANGLES) + list(N17_EXTRA))
    w_eq17 = np.ones(len(a17))
    w_cos17 = np.cos(np.radians(a17))
    for label, angs, w in [("N9 equal", ANGLES, w_eq9), ("N9 cos", ANGLES, w_cos9),
                            ("N17 equal", a17, w_eq17), ("N17 cos", a17, w_cos17)]:
        bo, bf, c = window_means(angs, w, y0, NY)
        print(f"\nopaque article, {label}: B_obj={bo:.4f} B_flank={bf:.4f}  "
              f"C_geo={c:+.4f}")

    # ---- fallback (+-35, N=9) geometry + ceiling, pre-committed ----------
    print("\n--- pre-committed fallback (+-35deg, N=9) ---")
    ok_fb = True
    fb_margins = {}
    for th in FALLBACK_ANGLES:
        lo, hi = lit_interval(th, NY, SRC_Y)
        covered = lo <= span[0] and hi >= span[1]
        m = min(span[0] - lo, hi - span[1])
        fb_margins[th] = m
        ok_fb &= covered
    print(f"  fallback coverage all angles OK: {ok_fb}, worst margin "
          f"{min(fb_margins.values()):.2f}")
    w_eq_fb = np.ones(len(FALLBACK_ANGLES))
    w_cos_fb = np.cos(np.radians(FALLBACK_ANGLES))
    bo, bf, c = window_means(FALLBACK_ANGLES, w_eq_fb, y0, NY)
    print(f"  fallback opaque ceiling (equal): C_geo={c:+.4f}")
    bo, bf, c = window_means(FALLBACK_ANGLES, w_cos_fb, y0, NY)
    print(f"  fallback opaque ceiling (cos):   C_geo={c:+.4f}")
    bo, bf, c = window_means(FALLBACK_ANGLES, w_eq_fb, y0, NY, transmission=True)
    print(f"  fallback sponge ceiling (equal): C_geo={c:+.4f}")

    # ---- dilute sponge (N9, primary) -------------------------------------
    bo, bf, c = window_means(ANGLES, w_eq9, y0, NY, transmission=True)
    print(f"\ndilute sponge (sigma={SIGMA_SPONGE:.4e}, center-chord tau="
          f"{SPONGE_TAU_CENTER}): B_obj={bo:.4f} B_flank={bf:.4f} C_geo={c:+.4f}")

    # ---- per-angle object coverage table (N9) ----------------------------
    print("\nper-angle geometric shadow vs windows (N9):")
    y = np.arange(NY, dtype=float)
    obj_w = (np.abs(y - y0) <= W_OBJ)
    for th in ANGLES:
        lo, hi = shadow_interval(th, y0)
        cov = ((y >= lo) & (y <= hi) & obj_w).sum() / obj_w.sum()
        reach = max(abs(lo - y0), abs(hi - y0))
        print(f"  theta={th:+03d}deg  shadow=[{lo - y0:+7.1f},{hi - y0:+7.1f}]rel "
              f"obj-coverage={cov * 100:5.1f}%  reach={reach:5.1f} "
              f"({'inside guard' if reach < GUARD_OUT else 'REACHES FLANK'})")

    # ---- BOX, derived (Red Team #6) — module-level constant, printed here
    print(f"\nBOX (derived, clearance={BOX_CLEARANCE}): {BOX}")
    print(f"  BOX vs damping bands: x-clear=[{BOX[0]-ABSORB}, {NX-ABSORB-BOX[1]}]"
          f"  y-clear=[{BOX[2]-ABSORB}, {NY-ABSORB-BOX[3]}]")

    print(f"\nrun-count: 4 scenes x 9 angles x 3 lambda = 108"
          f" + N17 extra (empty+PEC @600) = {2 * len(N17_EXTRA)}"
          " -> 124 runs (primary); fallback only triggers on a gate miss")


if __name__ == "__main__":
    main()
