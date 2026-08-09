"""
lab.materials — material builders for the 2D TMz engine.
========================================================
Each function writes material arrays into a Sim. Everything here exists
because an experiment demanded it (lab convention: grown, never
speculative). exp-001's three objects:

  (a) reflector      -> pec_disk
  (b) ultra-absorber -> absorber_shell_stub  (STUB — see note below)
  (c) cloak          -> schurig_reduced_cloak_tm
"""

import numpy as np


def _grids(sim, cx, cy):
    """Radius/angle fields at the three staggered grid families.
    Ez points: (i, j) · Hx points: (i, j+1/2) · Hy points: (i+1/2, j)."""
    def ra(xoff, yoff, nx, ny):
        x = np.arange(nx)[:, None] + xoff - cx
        y = np.arange(ny)[None, :] + yoff - cy
        return np.hypot(x, y), np.arctan2(y, x)
    return {
        "ez": ra(0.0, 0.0, sim.nx, sim.ny),
        "hx": ra(0.0, 0.5, sim.nx, sim.ny - 1),
        "hy": ra(0.5, 0.0, sim.nx - 1, sim.ny),
    }


def dielectric_cylinder(sim, cx, cy, r, eps_r):
    rr, _ = _grids(sim, cx, cy)["ez"]
    sim.eps_r[rr <= r] = eps_r
    sim.objects.append({"type": "dielectric_cylinder",
                        "params": {"cx": cx, "cy": cy, "r": r, "eps_r": eps_r}})


def pec_disk(sim, cx, cy, r):
    """Perfect electric conductor: Ez forced to zero (an ideal mirror —
    exp-001's 'ordinary reflector' object)."""
    rr, _ = _grids(sim, cx, cy)["ez"]
    sim.pec |= rr <= r
    sim.objects.append({"type": "pec_disk", "params": {"cx": cx, "cy": cy, "r": r}})


def absorber_shell_stub(sim, cx, cy, r_in, r_out, sigma_max=0.15, eps_max=2.0):
    """STUB — placeholder absorber so the machinery can be exercised.

    The real exp-001 ultra-absorber (carbon-nanotube-black-style graded
    coating, near-zero backscatter) is an OPEN DESIGN LANE offered to
    Bonnie on co-lab #31. This stub is deliberately naive: a cubic
    conductivity ramp + gentle index grade over the shell. Do not tune it;
    replace it with the designed model."""
    rr, _ = _grids(sim, cx, cy)["ez"]
    shell = (rr >= r_in) & (rr <= r_out)
    d = np.zeros_like(rr)
    d[shell] = (rr[shell] - r_in) / max(r_out - r_in, 1)
    sim.sigma_e[shell] += sigma_max * d[shell] ** 3
    sim.eps_r[shell] = 1.0 + (eps_max - 1.0) * d[shell] ** 2
    sim.objects.append({"type": "absorber_shell_stub",
                        "params": {"cx": cx, "cy": cy, "r_in": r_in, "r_out": r_out,
                                   "sigma_max": sigma_max, "eps_max": eps_max}})


def _graded_black(d):
    """Normalized depth d in [0,1] -> (eps_r, sigma) for the graded-black
    profile. Quintic smoothstep (zero 1st AND 2nd derivative at both ends)
    so the wave meets no corner in the material properties — the adiabatic
    entry is what kills the reflection. Loss grows as smoothstep^2:
    absorption arrives *after* the wave is already inside."""
    s = d * d * d * (10.0 - 15.0 * d + 6.0 * d * d)
    return s, 0.5 * s * s          # (smoothstep, sigma profile)


def graded_black_shell(sim, cx, cy, r_in, r_out, sigma_max=0.5, eps_max=1.0):
    """The designed ultra-absorber — exp-001's object (b), replacing the
    stub. Carbon-nanotube-black-style: a dilute conductive sponge whose
    permittivity stays ~1 (eps_max default 1.0 — NO index step, so there is
    no interface to glint off) while conductivity ramps in adiabatically
    over the shell. Light walks in and doesn't walk out; the object appears
    as darkness with no boundary — the witness's "stopped on nothing."

    r_in=0 gives a solid sponge disk. Thickness (r_out - r_in) >= ~1.5
    design wavelengths keeps the entry reflection broadband-small — this
    absorber should NOT crack across a wavelength sweep (unlike the cloak;
    that asymmetry is exp-001's discriminator working).

    Gates (trust suite stage 7, written before first run): flat-coating
    R < 0.01 at the design wavelength, < 0.02 at 450/750 nm equivalents;
    solid disk returns <= 0.1x a bare PEC disk's backscatter through the
    observer camera."""
    rr, _ = _grids(sim, cx, cy)["ez"]
    shell = (rr >= r_in) & (rr <= r_out)
    d = np.zeros_like(rr)
    d[shell] = np.clip((r_out - rr[shell]) / max(r_out - r_in, 1), 0.0, 1.0)
    s, sig = _graded_black(d[shell])
    sim.eps_r[shell] = 1.0 + (eps_max - 1.0) * s
    sim.sigma_e[shell] += sigma_max * sig / 0.5      # sig already carries 0.5
    sim.objects.append({"type": "graded_black_shell",
                        "params": {"cx": cx, "cy": cy, "r_in": r_in, "r_out": r_out,
                                   "sigma_max": sigma_max, "eps_max": eps_max}})


def schurig_reduced_cloak_tm(sim, cx, cy, r1, r2, mu_r_floor=0.10):
    """Cylindrical transformation-optics cloak, REDUCED parameter set for
    TMz (Ez) polarization — the set used in the field's founding papers:

        eps_z = (r2/(r2-r1))^2          (constant in the shell)
        mu_r  = ((r-r1)/r)^2            (radial, -> 0 at inner wall)
        mu_phi = 1

    Derivation sketch: Pendry/Schurig/Smith (Science 2006) map free space
    r' in [0, r2] onto the shell r in [r1, r2]; the transformed metric
    becomes material tensors. The reduced set (Cummer et al., PRE 2006)
    keeps the products eps_z*mu_r and eps_z*mu_phi — the ray trajectories —
    while flattening mu_phi to 1 for realizability. The price is an
    impedance mismatch at r = r2: a KNOWN residual reflection. We expect
    imperfection; that's published physics, not a bug.

    FDTD reality: mu_r -> 0 at r1 makes mu^-1 blow up, so we clamp
    mu_r >= mu_r_floor (default 0.10 -> mu^-1 <= 10). The clamp trades
    inner-wall fidelity for a stable timestep — run cloak scenes with
    courant_frac <= 0.4 (wave speed in the shell exceeds c; see
    VALIDATION.md stage 5 for the numbers).

    In Cartesian components (theta from the cloak center):
        mu^-1_xx = cos^2/mu_r + sin^2/mu_phi
        mu^-1_yy = sin^2/mu_r + cos^2/mu_phi
        mu^-1_xy = sin*cos*(1/mu_r - 1/mu_phi)
    evaluated at each staggered H location.
    """
    sim.ensure_inv_mu()
    g = _grids(sim, cx, cy)

    # eps_z on the Ez grid (constant in the shell)
    rr_ez, _ = g["ez"]
    shell_ez = (rr_ez >= r1) & (rr_ez <= r2)
    sim.eps_r[shell_ez] = (r2 / (r2 - r1)) ** 2

    def write_tensor(key, xx_or_yy):
        rr, th = g[key]
        shell = (rr >= r1) & (rr <= r2)
        mu_r = np.clip(((rr - r1) / np.maximum(rr, 1e-9)) ** 2, mu_r_floor, None)
        inv_r, inv_phi = 1.0 / mu_r, 1.0
        c, s = np.cos(th), np.sin(th)
        if xx_or_yy == "xx":
            diag = c**2 * inv_r + s**2 * inv_phi
            sim.inv_mu["xx"][shell] = diag[shell]
            sim.inv_mu["xy_hx"][shell] = (s * c * (inv_r - inv_phi))[shell]
        else:
            diag = s**2 * inv_r + c**2 * inv_phi
            sim.inv_mu["yy"][shell] = diag[shell]
            sim.inv_mu["xy_hy"][shell] = (s * c * (inv_r - inv_phi))[shell]

    write_tensor("hx", "xx")
    write_tensor("hy", "yy")
    sim.objects.append({"type": "schurig_reduced_cloak_tm",
                        "params": {"cx": cx, "cy": cy, "r1": r1, "r2": r2,
                                   "mu_r_floor": mu_r_floor}})
