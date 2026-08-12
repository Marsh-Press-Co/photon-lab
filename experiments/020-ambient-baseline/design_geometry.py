"""exp-020 design calculation — oblique-source coverage + shadow ray trace.
=========================================================================
Red Team mandatory fix #4 (Iteration 1): the proposal's oblique geometry
failed twice — source walk-off left the analysis span unlit at large
angles, and the shadow lever arm is object-center-to-plane (93 cells),
not object-edge-to-plane (15). This script IS the published design
calculation: it pins the geometry, verifies full-span direct-beam
coverage at every committed angle, ray-traces the nine-angle shadow
union, and prints the geometric contrast ceilings the committed
prediction bands are derived from. Pure geometry — no FDTD, no
measurement. Run it; the numbers it prints are the ones committed in
NOTES.md. If you change any constant, re-run and re-commit BEFORE runs.
"""

import numpy as np

# ----------------------------------------------------------- pinned geometry
NX, NY = 360, 1200          # cells (x = propagation, y = transverse)
ABSORB = 40                 # graded damping bands
CPL_600 = 20                # cells per lambda at 600 nm (Δ = 30 nm)
SRC_X = 300                 # far-side line source (ambient back-light)
SRC_Y = (ABSORB, NY - ABSORB)   # y ∈ [40, 1160], length 1120
TAPER = 40                  # cosine taper cells at each source end
OBJ = (170, 600)            # object center (cx, cy)
R_OUT = 78                  # outer radius, all articles (2.34 µm at Δ=30nm)
PLANE_DX = 15               # measurement plane: 15 cells observer-side of edge
PLANE_X = OBJ[0] - R_OUT - PLANE_DX          # = 77
SENS_PLANES = (12, 15, 16)  # plane-distance sensitivity rows
ANGLES = (-40, -30, -20, -10, 0, 10, 20, 30, 40)   # committed N = 9
N17_EXTRA = (-35, -25, -15, -5, 5, 15, 25, 35)     # convergence set @600 nm

# windows (relative to object center y0) — re-registered by synthesis:
# max oblique shadow reach = 93·tan40° + 78/cos40° = 78 + 102 = 180 cells,
# so the proposal's flank inner edge (117) sat INSIDE the 40° penumbra;
# flanks move outward to [185, 263] so "background" is background at every
# committed angle. Guard = (78, 185).
W_OBJ = 78
GUARD_OUT = 185
W_FLANK = 78
FLANK = (GUARD_OUT, GUARD_OUT + W_FLANK)     # (185, 263)

# dilute-sponge calibration article (materials seat, adopted):
SPONGE_TAU_CENTER = 0.10    # center-chord power optical depth
SIGMA_SPONGE = SPONGE_TAU_CENTER / (2 * R_OUT)   # power decay e^{-sigma*L}

LEVER = OBJ[0] - PLANE_X    # object CENTER to plane = 93 cells (EM's number)
D_SP = SRC_X - PLANE_X      # source to plane = 223 cells (walk-off baseline)


def lit_interval(theta_deg):
    """Flat (untapered) part of the source, walked to the plane at theta."""
    walk = D_SP * np.tan(np.radians(theta_deg))
    lo = SRC_Y[0] + TAPER + walk
    hi = SRC_Y[1] - TAPER + walk
    return lo, hi


def shadow_interval(theta_deg, y0):
    """Geometric shadow footprint of the disk on the plane at theta."""
    off = LEVER * np.tan(np.radians(theta_deg))
    hw = R_OUT / np.cos(np.radians(theta_deg))
    return y0 + off - hw, y0 + off + hw


def window_means(theta_list, weights, y0, transmission=None):
    """Geometric B(y) per angle (0 in shadow, 1 lit; or e^{-tau} for the
    sponge), averaged over obj / flank windows with the given weights."""
    y = np.arange(NY, dtype=float)
    obj_w = (np.abs(y - y0) <= W_OBJ)
    flank_w = (np.abs(y - y0) >= FLANK[0]) & (np.abs(y - y0) <= FLANK[1])
    b_obj, b_flank, wsum = 0.0, 0.0, 0.0
    for th, w in zip(theta_list, weights):
        lo, hi = shadow_interval(th, y0)
        b = np.ones(NY)
        if transmission is None:
            b[(y >= lo) & (y <= hi)] = 0.0
        else:
            off = LEVER * np.tan(np.radians(th))
            yc = y - (y0 + off)
            sec = 1.0 / np.cos(np.radians(th))
            inside = np.abs(yc) < R_OUT / np.cos(np.radians(th))
            chord = np.zeros(NY)
            # chord length through the disk along k̂ for footprint coord yc:
            # perpendicular offset = yc·cosθ  →  L = 2·sqrt(r² − (yc cosθ)²)/1
            perp = yc * np.cos(np.radians(th))
            chord[inside] = 2.0 * np.sqrt(
                np.maximum(R_OUT**2 - perp[inside] ** 2, 0.0))
            b = np.exp(-SIGMA_SPONGE * chord) * sec ** 0  # path in disk, not plane
        b_obj += w * b[obj_w].mean()
        b_flank += w * b[flank_w].mean()
        wsum += w
    b_obj /= wsum
    b_flank /= wsum
    return b_obj, b_flank, (b_obj - b_flank) / b_flank


def main():
    y0 = OBJ[1]
    print(f"geometry: {NX}x{NY}, absorb {ABSORB}, source x={SRC_X} "
          f"y=[{SRC_Y[0]},{SRC_Y[1]}] taper {TAPER}, object {OBJ} r={R_OUT}, "
          f"plane x={PLANE_X} (lever {LEVER}), D_source→plane={D_SP}")
    span = (y0 - FLANK[1], y0 + FLANK[1])
    print(f"analysis span: y ∈ [{span[0]}, {span[1]}]  "
          f"(obj ±{W_OBJ}, guard →{GUARD_OUT}, flanks {FLANK})")

    # ---- coverage check (gate b's design-side half) --------------------
    ok = True
    print("\nsource coverage at the plane (flat part only):")
    for th in ANGLES + N17_EXTRA:
        lo, hi = lit_interval(th)
        covered = lo <= span[0] and hi >= span[1]
        margin = min(span[0] - lo, hi - span[1])
        ok &= covered
        print(f"  θ={th:+03d}°  lit=[{lo:7.1f},{hi:7.1f}]  "
              f"margin={margin:6.1f}  {'OK' if covered else 'FAIL'}")
    assert ok, "analysis span not fully lit at some committed angle"

    # damping-band clearance for every window
    assert span[0] > ABSORB + 20 and span[1] < NY - ABSORB - 20, \
        "windows too close to damping bands"

    # ---- opaque-article ray trace (PEC and absorber) --------------------
    w_eq = np.ones(len(ANGLES))
    w_cos = np.cos(np.radians(ANGLES))
    for name, w in [("equal", w_eq), ("cos", w_cos)]:
        bo, bf, c = window_means(ANGLES, w, y0)
        print(f"\nopaque article, {name} weights: "
              f"B_obj={bo:.4f} B_flank={bf:.4f}  C_geo={c:+.4f}")

    # per-angle object coverage table (for NOTES)
    print("\nper-angle geometric shadow vs windows:")
    y = np.arange(NY, dtype=float)
    obj_w = (np.abs(y - y0) <= W_OBJ)
    for th in ANGLES:
        lo, hi = shadow_interval(th, y0)
        cov = ((y >= lo) & (y <= hi) & obj_w).sum() / obj_w.sum()
        reach = max(abs(lo - y0), abs(hi - y0))
        print(f"  θ={th:+03d}°  shadow=[{lo - y0:+7.1f},{hi - y0:+7.1f}]rel "
              f"obj-coverage={cov * 100:5.1f}%  reach={reach:5.1f} "
              f"({'inside guard' if reach < GUARD_OUT else 'REACHES FLANK'})")

    # ---- dilute sponge --------------------------------------------------
    bo, bf, c = window_means(ANGLES, w_eq, y0, transmission=True)
    print(f"\ndilute sponge (σ={SIGMA_SPONGE:.2e}, center-chord τ="
          f"{SPONGE_TAU_CENTER}): B_obj={bo:.4f} B_flank={bf:.4f} "
          f"C_geo={c:+.4f}")

    # ---- Fresnel-number sanity (how much diffraction fill to expect) ----
    for lam_nm, cpl in [(450, 15), (600, 20), (750, 25)]:
        nf = R_OUT**2 / (cpl * LEVER)     # a²/(λ·d) in cells
        print(f"Fresnel number @ {lam_nm} nm: N_F = {nf:.1f}")

    print("\nrun-count: 4 scenes x 9 angles x 3 lambda = 108"
          f" + N17 extra (empty+PEC @600) = {2 * len(N17_EXTRA)}"
          " -> 124 runs")


if __name__ == "__main__":
    main()
