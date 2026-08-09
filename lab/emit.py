"""
lab.emit — the solver's half of the artifact contract (schema 0.1.0).
=====================================================================
Emits Evidence-Gated run artifacts per lab/ARTIFACTS.md: quadrature field
pair + materials + optional observer record, float32 stored, manifest
mirroring the scene the Sim actually ran (Sim self-records its sources and
objects; nothing here is hand-assembled).

THE OBSERVER CAMERA (angle-resolved return at the source plane)
---------------------------------------------------------------
exp-001's question is literally "what comes back to the person holding the
flashlight?" — so the measurement is: on a vertical plane between the
source and the scene, decompose the steady-state field into plane waves
and keep the ones traveling BACK toward the source (-x), power-resolved by
angle.

Method (angular spectrum, standard):
  1. Steady state is CW, so two snapshots a quarter period apart give the
     complex phasor of every field point: F = f_A + i*(f_B corrected for
     the integer-step quarter offset).
  2. FFT the Ez and Hy phasors along the plane -> per-k_y spectral
     amplitudes. Each propagating k_y belongs to a pair of plane waves
     with k_x = +/-sqrt(k^2 - k_y^2); Ez alone cannot split the pair, but
     Ez AND Hy together can:  Ez(k_y) = a+ + a-,  Hy(k_y) ~ (k_x/w)(a+ - a-).
  3. Backward power per k_y ~ (k_x/w)|a-|^2; map k_y -> angle
     theta = arcsin(k_y/k) measured from -x (0 = straight back, +CCW) and
     integrate into regular angle bins (schema: flux integrated per bin).
  4. Normalization "vacuum_run": divide by the total FORWARD power of the
     reference (empty) run through the same plane -> obs_return_flux sums
     to (returned power)/(incident power).

Sign conventions (H leapfrog half-step, Hy staggering) are pinned by the
validation gates in run_all.py stage 6, not by faith: the mirror must
return ~1.0, the empty room ~0, and an eps=4 half-space must return
Fresnel's 1/9. If those fail, this module is wrong, loudly.

Evanescent components (|k_y| >= k) carry no time-averaged power and are
excluded. Idealizations: rectangular window over the interior of the
plane (spectral leakage lands inside the gate tolerances), single-plane
measurement (no time-gating of multiple bounces).
"""

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from . import artifacts


# ------------------------------------------------------------- field capture
def quarter_pair(sim):
    """Capture (ez_snapshot, hy_snapshot, ez_quarter, hy_quarter, offset).
    Advances the sim by ~T/4. Call at steady state, before any emission."""
    ez_a = sim.Ez.copy()
    hy_a = sim.Hy.copy()
    quarter = max(1, int(round(sim.lam / sim.S / 4.0)))
    sim.run(quarter)
    return ez_a, hy_a, sim.Ez.copy(), sim.Hy.copy(), quarter


def _phasor(f_a, f_b, omega, offset_steps):
    """Complex phasor from two snapshots offset_steps apart. Convention
    f(n) = Re{F e^{-i omega n}}: f_a = Re{F}, f_b = Re{F e^{-i phi}} with
    phi = omega*offset  ->  Im{F} = (f_b - cos(phi) f_a) / sin(phi).

    History (stage-8 forensics, 2026-08-09): the first version negated
    Im{F} (conjugate convention), which silently fought the H half-step
    correction. Ratio-normalized gates couldn't see it — but it WAS the
    stage-6 'camera floor': the empty room read sin^2(omega/2) = 1.2%,
    exactly the phase-error prediction. Absolute power balances (stage 8)
    exposed it. Floors drop accordingly."""
    phi = omega * offset_steps
    return f_a + 1j * (f_b - np.cos(phi) * f_a) / np.sin(phi)


# ---------------------------------------------------------- observer camera
def observer_record(sim, capture, plane_x, reference=None, n_bins=61,
                    theta_max_deg=78.0):
    """Angle-resolved backward flux at x = plane_x from a quarter_pair
    capture. Returns (obs_angles_rad, obs_flux, aux) where obs_flux is
    integrated per bin. If reference (another run's aux from the SAME
    geometry, empty scene) is given, flux is normalized to its total
    forward power ("vacuum_run" semantics); otherwise raw power units.
    aux carries (P_forward_total, P_backward_bins_raw) for reuse."""
    ez_a, hy_a, ez_b, hy_b, off = capture
    y_sl = slice(sim.absorb + 8, sim.ny - sim.absorb - 8)

    ez = _phasor(ez_a[plane_x, y_sl], ez_b[plane_x, y_sl], sim.omega, off)
    # Hy lives at (i+1/2, j) and half a time step behind Ez: interpolate to
    # the plane and correct the half-step phase.
    hy_at = lambda h: 0.5 * (h[plane_x - 1, y_sl] + h[plane_x, y_sl])
    hy = _phasor(hy_at(hy_a), hy_at(hy_b), sim.omega, off) * np.exp(-0.5j * sim.omega)

    n = ez.size
    k = 2.0 * np.pi / sim.lam
    ez_k = np.fft.fft(ez) / n
    hy_k = np.fft.fft(hy) / n
    ky = 2.0 * np.pi * np.fft.fftfreq(n)

    prop = np.abs(ky) < 0.985 * k          # propagating components only
    kx = np.sqrt(np.maximum(k**2 - ky[prop] ** 2, 1e-30))
    # Split the +x / -x pair. Engine convention (dHy/dn = S dEz/dx, plane
    # wave e^{i(kx x - w n)}): Hy = -(S kx / w)(a+ - a-) while
    # Ez = a+ + a-.  Hence with scale = w/(S kx):
    #   a+ = (Ez_k - scale*Hy_k)/2,   a- = (Ez_k + scale*Hy_k)/2.
    # The stage-6 gates (empty~0, mirror~1, Fresnel~1/9) prove the signs.
    scale = sim.omega / (sim.S * kx)        # ~ k/kx
    a_fwd = 0.5 * (ez_k[prop] - scale * hy_k[prop])
    a_bwd = 0.5 * (ez_k[prop] + scale * hy_k[prop])
    w = kx / k                              # obliquity: power ~ kx/k |a|^2
    p_fwd = w * np.abs(a_fwd) ** 2
    p_bwd = w * np.abs(a_bwd) ** 2

    theta = np.arcsin(np.clip(ky[prop] / k, -1, 1))   # from -x axis, +CCW
    theta_max = np.deg2rad(theta_max_deg)
    edges = np.linspace(-theta_max, theta_max, n_bins + 1)
    flux, _ = np.histogram(theta, bins=edges, weights=p_bwd)
    centers = 0.5 * (edges[:-1] + edges[1:])

    aux = {"p_forward_total": float(np.sum(p_fwd)),
           "p_backward_total": float(np.sum(p_bwd))}
    if reference is not None:
        flux = flux / reference["p_forward_total"]
    return centers, flux, aux


# ------------------------------------------------------------------ emitter
def _engine_commit():
    try:
        root = Path(__file__).resolve().parent.parent
        return subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            capture_output=True, text=True, timeout=10, check=True,
        ).stdout.strip()
    except Exception:
        return "unknown"


def emit_run(sim, run_dir, *, experiment, scene, lambda_nm, suite_status,
             snapshot_step, capture, provenance=(), observer=None):
    """Assemble arrays + manifest from a Sim and a quarter_pair capture,
    write via artifacts.save_run (which validates loudly). `observer`, if
    given: dict(plane_x, start_step, normalization, reference_run,
    angles, flux) — from observer_record().

    Stored fields are float32 by contract (rendering never needs float64;
    solver precision stays in memory); the sha256 anchors bytes."""
    ez_a, _, ez_b, _, off = capture
    f32 = lambda a: np.asarray(a, dtype=np.float32)
    arrays = {
        "ez_snapshot": f32(ez_a), "ez_quarter": f32(ez_b),
        "eps_r": f32(sim.eps_r), "sigma_e": f32(sim.sigma_e),
        "pec_mask": sim.pec.copy(),
    }
    if sim.inv_mu is not None:
        arrays["inv_mu_xx"] = f32(sim.inv_mu["xx"])
        arrays["inv_mu_yy"] = f32(sim.inv_mu["yy"])
        arrays["inv_mu_xy_hx"] = f32(sim.inv_mu["xy_hx"])
        arrays["inv_mu_xy_hy"] = f32(sim.inv_mu["xy_hy"])

    manifest = {
        "experiment": experiment,
        "scene": scene,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "engine_commit": _engine_commit(),
        "suite_status": suite_status,
        "lambda_nm": lambda_nm,
        "grid": {"nx": sim.nx, "ny": sim.ny,
                 "cells_per_lambda": sim.cells_per_lambda,
                 "courant_frac": sim.courant_frac, "absorb": sim.absorb},
        "run": {"steps": sim.step_count, "snapshot_step": snapshot_step,
                "quarter_offset_steps": off},
        "sources": list(sim.source_specs),
        "objects": list(sim.objects),
        "provenance": list(provenance),
    }
    if observer is not None:
        arrays["obs_angles_rad"] = np.asarray(observer["angles"], dtype=np.float64)
        arrays["obs_return_flux"] = np.asarray(observer["flux"], dtype=np.float64)
        manifest["observer"] = {
            "plane_x": observer["plane_x"],
            "start_step": observer["start_step"],
            "normalization": observer["normalization"],
            "reference_run": observer["reference_run"],
        }
    return artifacts.save_run(run_dir, manifest, arrays)
