"""exp-025 design calculation -- resolution check on exp-024's chromatic
finding (Red Team's Phase-5 audit of Iteration 2: the R3 meta-rule --
"any surprising feature gets a resolution check before it gets a mechanism
debate, and 'artifact' claims need the check too" -- was owed to the new
real-vs-floor-bias chromatic-C finding and not proactively applied before
it was scored CONFIRMED).

exp-024's fallback (+-35deg) geometry measured a real (delta_C-clear),
small (~1.5-1.9%) growth of |C| toward red in the two hard-edged articles
(absorber, PEC) but not the soft-edged sponge. EM's own Phase-5 review
flagged the leading candidate mechanism: numerical-dispersion anisotropy in
the Yee grid, worst at coarse cells-per-wavelength (cpl) and steep angles
-- and cpl varies by design across this bench's 3-lambda quadrature (15 at
450nm, 20 at 600nm, 25 at 750nm, all at a fixed Delta=30nm), with 450nm the
LEAST resolved. Per this lab's own established precedent (exp-005, -010,
-015, -023: cpl x1.5, geometry rescaled in cells to hold physical size
fixed), this script rescales the two suspect wavelengths (450, 750nm) to
1.5x their cpl and recomputes every cell-based constant to hold the
PHYSICAL (nm) geometry identical to exp-024's fallback configuration.
600nm is the unmoved control (already the wavelength showing the smallest
excursion in exp-024, per VISION's V-weighting point).

Pure geometry -- no FDTD. Run it; the numbers below are what run.py uses.
"""

import numpy as np

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "..", "024-ambient-margin-adjudication"))
import design_geometry as dg024   # the exp-024 baseline this check refines

# ------------------------------------------------------------- target set
TARGETS = {450: 15, 750: 25}          # lambda_nm -> exp-024's cpl
RES_MULT = 1.5                        # this lab's standing resolution-check factor

FALLBACK_ANGLES = dg024.FALLBACK_ANGLES     # (-35,...,35), N=9 -- unchanged
BOX_CLEARANCE = dg024.BOX_CLEARANCE          # 12 cells (at exp-024's Delta)


def scaled_geometry(lam_nm):
    """All exp-024 cell-based constants rescaled by cpl_new/cpl_old, holding
    physical (nm) geometry identical. Returns a dict of the scaled values."""
    cpl_old = TARGETS[lam_nm]
    cpl_new = int(round(cpl_old * RES_MULT))
    ratio = cpl_new / cpl_old

    def sc(v):
        return int(round(v * ratio))

    nx = sc(dg024.NX)
    ny = sc(dg024.NY)
    absorb = sc(dg024.ABSORB)
    src_x = sc(dg024.SRC_X)
    taper = sc(dg024.TAPER)
    r_out = sc(dg024.R_OUT)
    plane_dx = sc(dg024.PLANE_DX)
    obj_x = sc(dg024.OBJ_X)
    obj_y = ny // 2                      # recenter exactly, exp-024's own convention
    plane_x = obj_x - r_out - plane_dx
    w_obj = sc(dg024.W_OBJ)
    guard_out = sc(dg024.GUARD_OUT)
    w_flank = sc(dg024.W_FLANK)
    box_clear = sc(BOX_CLEARANCE)
    box = (obj_x - r_out - box_clear, obj_x + r_out + box_clear,
           obj_y - r_out - box_clear, obj_y + r_out + box_clear)
    src_y = (absorb, ny - absorb)
    return dict(lam_nm=lam_nm, cpl_old=cpl_old, cpl_new=cpl_new, ratio=ratio,
                NX=nx, NY=ny, ABSORB=absorb, SRC_X=src_x, TAPER=taper,
                R_OUT=r_out, OBJ=(obj_x, obj_y), PLANE_X=plane_x,
                W_OBJ=w_obj, GUARD_OUT=guard_out, W_FLANK=w_flank,
                FLANK=(guard_out, guard_out + w_flank), BOX=box, SRC_Y=src_y)


def verify_coverage(geo):
    """Same coverage check as exp-024's design_geometry.py, at the FALLBACK
    angle set, for the rescaled geometry."""
    D_SP = geo["SRC_X"] - geo["PLANE_X"]
    y0 = geo["OBJ"][1]
    span = (y0 - geo["FLANK"][1], y0 + geo["FLANK"][1])
    ok, margins = True, {}
    for th in FALLBACK_ANGLES:
        walk = D_SP * np.tan(np.radians(th))
        lo = geo["SRC_Y"][0] + geo["TAPER"] + walk
        hi = geo["SRC_Y"][1] - geo["TAPER"] + walk
        covered = lo <= span[0] and hi >= span[1]
        margins[th] = min(span[0] - lo, hi - span[1])
        ok &= covered
    return ok, margins


def main():
    for lam_nm in TARGETS:
        geo = scaled_geometry(lam_nm)
        ok, margins = verify_coverage(geo)
        print(f"--- {lam_nm} nm: cpl {geo['cpl_old']} -> {geo['cpl_new']} "
              f"(ratio {geo['ratio']:.4f}) ---")
        print(f"  NX,NY = {geo['NX']},{geo['NY']}  OBJ={geo['OBJ']} "
              f"R_OUT={geo['R_OUT']}  PLANE_X={geo['PLANE_X']}")
        print(f"  BOX={geo['BOX']}  coverage OK={ok}  "
              f"worst margin={min(margins.values()):.2f}")
        assert ok, f"fallback-angle coverage failed at {lam_nm}nm rescaled geometry"
    print("\nboth targets verified -- geometry ready for run.py")


if __name__ == "__main__":
    main()
