"""
lab.sections — scattering / absorption / extinction widths (exp-002).
=====================================================================
The proper currency of invisibility. A closed four-face Poynting box
around the object, evaluated with complex phasors from quadrature
captures, yields three independent power channels:

  P_scat  = net OUTflow of scattered-field power   (sprayed light)
  P_abs   = net INflow  of total-field power        (eaten light)
  P_ext   = P_abs + P_scat                          (removed from the beam)

with the scattered field formed by exact phasor subtraction
(scene − empty reference, same source phase). Extinction is also computed
by an independent route — the incident×scattered cross-term integral
(−∮ S_cross · n, the near-field statement of the optical theorem) — and
the two routes must agree.

Normalization: divide by the incident intensity measured on the upstream
face of the same box in the empty run → widths in cells (2D analogue of
cross-sections). Q = width / (2 · outer radius) is the ranking metric.

Trust gates (suite stage 8) before any experiment uses this module:
box-independence (two boxes, same answer), a lossless object's absorption
channel reads ~zero, the graded-black absorber's absorption dominates.

TMz Poynting with phasors:  <Sx> = -1/2 Re{Ez conj(Hy)},
<Sy> = +1/2 Re{Ez conj(Hx)}.  Hx and Hy carry the leapfrog half-step
phase correction established (and gate-proven) in lab.emit.
"""

import numpy as np

from .emit import _phasor


def full_capture(sim):
    """Quadrature capture of Ez, Hx AND Hy (superset of emit.quarter_pair,
    which stays untouched for exp-001 reproducibility). Advances ~T/4."""
    ez_a, hx_a, hy_a = sim.Ez.copy(), sim.Hx.copy(), sim.Hy.copy()
    quarter = max(1, int(round(sim.lam / sim.S / 4.0)))
    sim.run(quarter)
    return {"ez_a": ez_a, "hx_a": hx_a, "hy_a": hy_a,
            "ez_b": sim.Ez.copy(), "hx_b": sim.Hx.copy(),
            "hy_b": sim.Hy.copy(), "off": quarter,
            "omega": sim.omega}


def phasors(cap):
    """Complex phasor fields on their native grids, H half-step-corrected."""
    w, off = cap["omega"], cap["off"]
    corr = np.exp(-0.5j * w)
    return {
        "ez": _phasor(cap["ez_a"], cap["ez_b"], w, off),
        "hx": _phasor(cap["hx_a"], cap["hx_b"], w, off) * corr,
        "hy": _phasor(cap["hy_a"], cap["hy_b"], w, off) * corr,
    }


def _face_flux(ez, hx, hy, box):
    """Outward time-averaged power flux through the four faces of
    box = (x0, x1, y0, y1) (Ez-grid indices, faces ON those lines).
    Returns the total outward power (grid units)."""
    x0, x1, y0, y1 = box
    ys = slice(y0, y1 + 1)
    xs = slice(x0, x1 + 1)

    def sx(xf):                       # <Sx> on vertical line x=xf
        hy_at = 0.5 * (hy[xf - 1, ys] + hy[xf, ys])
        return -0.5 * np.real(ez[xf, ys] * np.conj(hy_at))

    def sy(yf):                       # <Sy> on horizontal line y=yf
        hx_at = 0.5 * (hx[xs, yf - 1] + hx[xs, yf])
        return 0.5 * np.real(ez[xs, yf] * np.conj(hx_at))

    return (float(np.sum(sx(x1))) - float(np.sum(sx(x0)))
            + float(np.sum(sy(y1))) - float(np.sum(sy(y0))))


def flux_profile_x(ph, x_plane, y_lo, y_hi):
    """Per-cell time-averaged <Sx> along the Ez line x = x_plane,
    y in [y_lo, y_hi) — positive toward +x. Exactly the per-cell terms
    `_face_flux`'s sx() sums (same Hy interpolation, same gate-proven
    phasor conventions), kept as a profile instead of collapsed to one
    number. The ambient instrument's B(y) is the −x direction of this
    (lab/ambient.py)."""
    ys = slice(y_lo, y_hi)
    hy_at = 0.5 * (ph["hy"][x_plane - 1, ys] + ph["hy"][x_plane, ys])
    return -0.5 * np.real(ph["ez"][x_plane, ys] * np.conj(hy_at))


def _cross_flux(pi, ps, box):
    """Outward flux of the incident×scattered cross terms through the box:
    S_cross = 1/2 Re{Ei conj(Hs) + Es conj(Hi)} componentwise."""
    x0, x1, y0, y1 = box
    ys = slice(y0, y1 + 1)
    xs = slice(x0, x1 + 1)

    def sx(xf):
        hyi = 0.5 * (pi["hy"][xf - 1, ys] + pi["hy"][xf, ys])
        hys = 0.5 * (ps["hy"][xf - 1, ys] + ps["hy"][xf, ys])
        return -0.5 * np.real(pi["ez"][xf, ys] * np.conj(hys)
                              + ps["ez"][xf, ys] * np.conj(hyi))

    def sy(yf):
        hxi = 0.5 * (pi["hx"][xs, yf - 1] + pi["hx"][xs, yf])
        hxs = 0.5 * (ps["hx"][xs, yf - 1] + ps["hx"][xs, yf])
        return 0.5 * np.real(pi["ez"][xs, yf] * np.conj(hxs)
                             + ps["ez"][xs, yf] * np.conj(hxi))

    return (float(np.sum(sx(x1))) - float(np.sum(sx(x0)))
            + float(np.sum(sy(y1))) - float(np.sum(sy(y0))))


def widths(cap_scene, cap_empty, box, ref):
    """All widths (cells) for one scene/reference pair through one box.
    ref = (cx, cy, half_h): incident intensity is measured in the EMPTY run
    at the object's own x-position over the central beam strip — one fixed
    normalization independent of box geometry. (First-run lesson: per-face
    normalization made widths drift with box size because the finite beam's
    intensity varies between faces; the object doesn't care where our box
    is, so neither may sigma.)
    Returns dict with sigma_scat / sigma_abs / sigma_ext (both routes),
    the backward/forward split of the scattered outflow, and I_inc."""
    pt = phasors(cap_scene)
    pi = phasors(cap_empty)
    ps = {k: pt[k] - pi[k] for k in pt}

    x0, x1, y0, y1 = box
    ys = slice(y0, y1 + 1)

    p_scat = _face_flux(ps["ez"], ps["hx"], ps["hy"], box)
    p_abs = -_face_flux(pt["ez"], pt["hx"], pt["hy"], box)
    p_ext_cross = -_cross_flux(pi, ps, box)

    # backward vs forward share of the scattered OUTflow
    hy_b = 0.5 * (ps["hy"][x0 - 1, ys] + ps["hy"][x0, ys])
    p_back = -float(np.sum(-0.5 * np.real(ps["ez"][x0, ys] * np.conj(hy_b))))
    hy_f = 0.5 * (ps["hy"][x1 - 1, ys] + ps["hy"][x1, ys])
    p_fwd = float(np.sum(-0.5 * np.real(ps["ez"][x1, ys] * np.conj(hy_f))))

    # incident intensity: fixed central strip at the object's x, empty run
    cx, cy, hh = ref
    rs = slice(cy - hh, cy + hh + 1)
    hy_i = 0.5 * (pi["hy"][cx - 1, rs] + pi["hy"][cx, rs])
    i_inc = float(np.mean(-0.5 * np.real(pi["ez"][cx, rs] * np.conj(hy_i))))

    return {
        "sigma_scat": p_scat / i_inc,
        "sigma_abs": p_abs / i_inc,
        "sigma_ext": (p_scat + p_abs) / i_inc,
        "sigma_ext_cross": p_ext_cross / i_inc,
        "back_frac": max(p_back, 0.0) / max(p_scat, 1e-30),
        "fwd_frac": max(p_fwd, 0.0) / max(p_scat, 1e-30),
        "i_inc": i_inc,
    }


def angular_scattered_pattern(cap_scene, cap_empty, box, ref, n_bins=48):
    """Angle-resolved scattered-power distribution around the box
    perimeter (exp-016/017's mechanism line: does a trough/flank pair
    differ in SHAPE, not just magnitude?).

    Reuses `widths()`'s exact per-cell outward-flux terms (same box, same
    scattered-phasor construction) but keeps them per-cell instead of
    summing to a single sigma_scat or the two-way back/fwd split — each
    perimeter cell is tagged with its angle from the box's own center
    (atan2, source direction = 0 deg = "backward toward the source",
    180/-180 deg = "forward, downstream") and binned.

    Idealization: this is a square-path angular sample, not a true
    circular far-field pattern — consistent with sigma_scat's own
    near-to-mid-field box convention (VALIDATION.md), not a new
    approximation. Because binning is a re-partition of the exact same
    per-cell terms `widths()` already sums in full, `sum(pattern) ==
    sigma_scat` is not an independent physical check -- it's an
    implementation self-consistency identity, verified by the caller
    against widths()'s own number before the pattern is trusted for
    shape comparisons.

    Returns (bin_centers_deg, sigma_scat_per_bin) as two 1-D arrays of
    length n_bins, angle convention: 0 deg = -x (toward the source,
    "backward"), +-180 deg = +x (downstream, "forward")."""
    pt = phasors(cap_scene)
    pi = phasors(cap_empty)
    ps = {k: pt[k] - pi[k] for k in pt}

    x0, x1, y0, y1 = box
    bcx, bcy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    ys = slice(y0, y1 + 1)
    xs = slice(x0, x1 + 1)

    def sx(xf):
        hy_at = 0.5 * (ps["hy"][xf - 1, ys] + ps["hy"][xf, ys])
        return -0.5 * np.real(ps["ez"][xf, ys] * np.conj(hy_at))

    def sy(yf):
        hx_at = 0.5 * (ps["hx"][xs, yf - 1] + ps["hx"][xs, yf])
        return 0.5 * np.real(ps["ez"][xs, yf] * np.conj(hx_at))

    yy = np.arange(y0, y1 + 1, dtype=float)
    xx = np.arange(x0, x1 + 1, dtype=float)

    angs = np.concatenate([
        np.degrees(np.arctan2(yy - bcy, x1 - bcx)),   # x1 face (mostly forward)
        np.degrees(np.arctan2(yy - bcy, x0 - bcx)),   # x0 face (mostly backward)
        np.degrees(np.arctan2(y1 - bcy, xx - bcx)),   # y1 face
        np.degrees(np.arctan2(y0 - bcy, xx - bcx)),   # y0 face
    ])
    flux = np.concatenate([sx(x1), -sx(x0), sy(y1), -sy(y0)])

    cx, cy, hh = ref
    rs = slice(cy - hh, cy + hh + 1)
    hy_i = 0.5 * (pi["hy"][cx - 1, rs] + pi["hy"][cx, rs])
    i_inc = float(np.mean(-0.5 * np.real(pi["ez"][cx, rs] * np.conj(hy_i))))

    edges = np.linspace(-180.0, 180.0, n_bins + 1)
    idx = np.clip(np.digitize(angs, edges) - 1, 0, n_bins - 1)
    sigma_per_bin = np.zeros(n_bins)
    np.add.at(sigma_per_bin, idx, flux / i_inc)
    centers = 0.5 * (edges[:-1] + edges[1:])
    return centers, sigma_per_bin
