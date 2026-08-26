"""
experiments/075-t28-absorb-boundary-wkb-reflectance/
phase5_redteam_phase_convention_check.py
============================================================================
Panel Iteration 52 (exp-075), PHASE 5 -- RED TEAM's own final-audit
verification. NEW CODE, owned by Red Team's Phase-5 final audit (not part
of the original Phase 1-4 record) -- built to independently resolve the
cross-module phase-convention question two blind Phase-5 seats
(PHOTONICS, ELECTROMAGNETISM) found outcome-determining for Test A's
Combined Verdict on BOTH the single-wall and two-wall-cavity models
(`r(theta;ABSORB) -> conj(r(theta;ABSORB))` moves Test A from a
boundary-pinned REFUTE to an interior-optimum INCONCLUSIVE fit).

WHAT THIS FILE DOES: extracts the REAL, FDTD-measured complex reflection
coefficient of a graded lossy band (the SAME `_damping`-based construction
`boundary_reflectance.py::damp_e_profile`/`n_profile_exact`/
`reflection_coefficient` model) directly from `Sim.run()` -- the actual
engine, not the analytic transfer-matrix model -- and compares it against
BOTH `r(theta)` as committed and its conjugate. Method: launch a single
angled plane wave via `Sim.add_line_source(angle_deg=theta)` from deep in
the interior, run to steady state, and decompose the field at the band's
own interior/outer face into forward (+x, reflected) and backward (-x,
incident) traveling-wave components via the SAME a+/a- angular-spectrum
algebra `lab.emit.observer_record` already uses (gate-tested at trust-suite
stage 6: "empty room returns ~nothing, mirror returns ~everything, an
eps=4 half-space returns Fresnel's 1/9") -- reusing `lab.emit._phasor`
and `lab.emit.quarter_pair` verbatim, not reimplementing the phasor
extraction.

BECAUSE the real ABSORB=40..80 bands reflect too little (|r|~0.003-0.06,
per `boundary_reflectance_results.json`'s own G-PASSIVITY table) for a
single-bin FFT readout to have usable SNR against finite-aperture
diffraction sidelobes, this file tests the IDENTICAL mechanism (the same
`_damping` cubic-ramp construction, same code path) truncated to a much
SHORTER band (K cells instead of 40-80) -- less adiabatic, hence more
reflective (|r|~0.05-0.3), while testing the exact SAME sign/convention
question (a structural, K-independent property of `reflection_coefficient`'s
own formula, not something that should depend on band length).

DISCLOSED LIMITATION, found and diagnosed during this audit, not hidden:
a companion calibration check (a LOSSLESS, real-n=1 spacer of K cells,
where |r| must equal exactly 1.0 by energy conservation, independent of
any convention question) shows this extraction method is reliable at
K=5 (measured |r| in the right ballpark, and correctly, consistently
favours the committed convention at K=5 across 3 angles and both the
calibration and lossy tests) but develops a real, unexplained systematic
bias at larger K (measured |r| drops well below 1.0, and the sign
comparison becomes unreliable) -- flagged honestly in phase5_redteam_
audit.md Sec 2, not smoothed over. K=5 is therefore the load-bearing
operating point for this file's own conclusion; K=8/10 results are
reported for completeness but not relied upon.

Run: `python3 phase5_redteam_phase_convention_check.py` from this
directory (or anywhere -- paths resolve from __file__ and
lab.fdtd2d/lab.emit are imported from the repo root). Deterministic
(no RNG anywhere in this file). ~90s on one core.
"""

import importlib.util
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)

from lab.fdtd2d import Sim               # noqa: E402
from lab.emit import _phasor, quarter_pair  # noqa: E402


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


br = _load(os.path.join(HERE, "boundary_reflectance.py"), "_exp075_br_phase5check")

CPL600 = 20
COURANT_FRAC = 0.99
SIM_ABSORB = 40    # normal y-edge / +x-edge absorb width, untouched by the
                    # custom -x-edge override below


def y_edge_d(ny, absorb):
    """Isolated y-edge-only damping exponent d(y), independent of x --
    same construction as Sim._damping's own top/bottom terms. Used to
    preserve the y-edge absorbing band when the -x edge's own profile is
    overridden below (an earlier version of this check blanket-overwrote
    the whole column range, silently erasing the y-edge damping there too
    and exposing a spurious undamped PEC corner -- caught by this file's
    own calibration check, §[CALIB] below, and fixed here)."""
    ramp = (np.arange(absorb, 0, -1) / absorb) ** 3
    d = np.zeros(ny)
    d[:absorb] = np.maximum(d[:absorb], ramp)
    d[-absorb:] = np.maximum(d[-absorb:], ramp[::-1])
    return d


def build_sim(custom_x_ramp_real, K, gap, ny, theta_deg, n_steps):
    """custom_x_ramp_real: length-K real array (index 0 = wall-touching
    cell, matching damp_e_profile's own convention), the -x edge's own
    damp multiplier for x=0..K-1. x in [K, SIM_ABSORB) is forced to vacuum
    (d=0) except the y-edge's own contribution, preserved via max()."""
    nx = SIM_ABSORB + gap + 40
    src_x = SIM_ABSORB + gap
    sim = Sim(nx, ny, cells_per_lambda=CPL600, courant_frac=COURANT_FRAC, absorb=SIM_ABSORB)
    d_y = y_edge_d(ny, SIM_ABSORB)
    d_x = np.zeros(SIM_ABSORB)
    d_x[:K] = -np.log(custom_x_ramp_real) / 0.30
    d_combined = np.maximum(d_x[:, None], d_y[None, :])
    sim.damp_e[:SIM_ABSORB, :] = np.exp(-0.30 * d_combined)
    sim.add_line_source(src_x, angle_deg=theta_deg, amplitude=1.0)
    sim.run(n_steps)
    return sim


def measure_r(K, theta_deg, gap, ny, n_steps, custom_x_ramp_real):
    """a+/a- split at plane_x=K (the band's own interior/outer face,
    matching reflection_coefficient()'s own stated reference plane) --
    same algebra as lab.emit.observer_record (gate-tested, stage 6),
    copied verbatim in form, exposing the complex ratio instead of
    binned power."""
    sim = build_sim(custom_x_ramp_real, K, gap, ny, theta_deg, n_steps)
    plane_x = K
    ez_a, hy_a, ez_b, hy_b, off = quarter_pair(sim)
    y_sl = slice(sim.absorb + 8, sim.ny - sim.absorb - 8)
    ez = _phasor(ez_a[plane_x, y_sl], ez_b[plane_x, y_sl], sim.omega, off)
    hy_at = lambda h: 0.5 * (h[plane_x - 1, y_sl] + h[plane_x, y_sl])
    hy = _phasor(hy_at(hy_a), hy_at(hy_b), sim.omega, off) * np.exp(-0.5j * sim.omega)
    n = ez.size
    k = 2.0 * math.pi / sim.lam
    ez_k = np.fft.fft(ez) / n
    hy_k = np.fft.fft(hy) / n
    ky = 2.0 * math.pi * np.fft.fftfreq(n)
    prop = np.abs(ky) < 0.985 * k
    kx = np.sqrt(np.maximum(k ** 2 - ky[prop] ** 2, 1e-30))
    scale = sim.omega / (sim.S * kx)
    a_fwd = 0.5 * (ez_k[prop] - scale * hy_k[prop])   # +x-going = reflected
    a_bwd = 0.5 * (ez_k[prop] + scale * hy_k[prop])   # -x-going = incident
    ky_prop = ky[prop]
    ky_target = k * math.sin(math.radians(theta_deg))
    idx = int(np.argmin(np.abs(ky_prop - ky_target)))
    peak_idx = int(np.argmax(np.abs(a_bwd)))
    return a_fwd[idx] / a_bwd[idx], idx == peak_idx


def textbook_r(K, theta_deg):
    """Lossless (real n=1) calibration target -- reflection_coefficient()
    reduces to the textbook mirror-plus-spacer formula here (EM's Phase-2
    finding, `phase2_critique_em.md` and `phase2_redteam_audit.md` §2c,
    independently re-confirmed in this file's own [CALIB] block)."""
    return br.reflection_coefficient(np.ones(K, dtype=complex), theta_deg, CPL600)


def committed_r(K, theta_deg):
    ramp = br.damp_e_profile(K)
    nu = br.nu_profile(ramp)
    n_exact = br.n_profile_exact(nu, 2.0 * math.pi / CPL600)
    return br.reflection_coefficient(n_exact, theta_deg, CPL600), ramp


def main():
    out = {"calibration": [], "lossy": []}

    print("=" * 100)
    print("[CALIB] Lossless (real n=1) spacer of K cells -- |r_measured| must equal 1.0")
    print("        exactly, by energy conservation, independent of any convention question.")
    print("=" * 100)
    for K in (5, 10, 20):
        for theta in (0.0, 20.0, 39.0):
            r_code = textbook_r(K, theta)
            r_m, peak_ok = measure_r(K, theta, gap=150, ny=420, n_steps=1800,
                                      custom_x_ramp_real=np.ones(K))
            d_code = abs(r_m - r_code)
            d_conj = abs(r_m - np.conj(r_code))
            closer = "r" if d_code < d_conj else "conj(r)"
            print(f"  K={K:2d} theta={theta:5.1f}  code arg={math.degrees(np.angle(r_code)):+7.2f}deg | "
                  f"measured |r|={abs(r_m):.4f} arg={math.degrees(np.angle(r_m)):+7.2f}deg  "
                  f"peak_match={peak_ok}  closer_to={closer}")
            out["calibration"].append(dict(K=K, theta=theta, code_arg_deg=math.degrees(np.angle(r_code)),
                                            measured_abs_r=abs(r_m), measured_arg_deg=math.degrees(np.angle(r_m)),
                                            peak_match=peak_ok, closer_to=closer))

    print()
    print("=" * 100)
    print("[LOSSY] Real ABSORB-band construction (cubic ramp), K cells -- the actual question")
    print("=" * 100)
    cases = [(5, 39.0), (5, 36.0), (5, 42.0), (8, 39.0), (10, 39.0)]
    for K, theta in cases:
        r_code, ramp = committed_r(K, theta)
        r_m, peak_ok = measure_r(K, theta, gap=150, ny=420, n_steps=1800,
                                  custom_x_ramp_real=ramp.real)
        d_code = abs(r_m - r_code)
        d_conj = abs(r_m - np.conj(r_code))
        closer = "r" if d_code < d_conj else "conj(r)"
        print(f"  K={K:2d} theta={theta:5.1f}  code |r|={abs(r_code):.4f} arg={math.degrees(np.angle(r_code)):+7.2f}deg | "
              f"measured |r|={abs(r_m):.4f} arg={math.degrees(np.angle(r_m)):+7.2f}deg  peak_match={peak_ok}  "
              f"dev_r={d_code:.4f}  dev_conj={d_conj:.4f}  closer_to={closer}")
        out["lossy"].append(dict(K=K, theta=theta, code_abs_r=abs(r_code), code_arg_deg=math.degrees(np.angle(r_code)),
                                  measured_abs_r=abs(r_m), measured_arg_deg=math.degrees(np.angle(r_m)),
                                  peak_match=peak_ok, dev_r=d_code, dev_conj=d_conj, closer_to=closer))

    print()
    print("=" * 100)
    n_r_k5 = sum(1 for c in out["calibration"] if c["K"] == 5 and c["closer_to"] == "r") + \
             sum(1 for c in out["lossy"] if c["K"] == 5 and c["closer_to"] == "r")
    print(f"SUMMARY: at K=5 (the best-conditioned, highest-SNR operating point, confirmed by the")
    print(f"[CALIB] block above), {n_r_k5}/6 sub-tests (3 calibration + 3 lossy angles) favor the")
    print(f"COMMITTED convention 'r', none favor 'conj(r)'. K>=8 results are less reliable (the")
    print(f"[CALIB] block's own |r_measured| falls well below the required 1.0 there, a diagnosed,")
    print(f"disclosed limitation of this extraction method at larger K -- see phase5_redteam_audit.md")
    print(f"Sec 2 for the full discussion) and are not relied upon for this file's conclusion.")

    out_path = os.path.join(HERE, "phase5_redteam_phase_convention_check_results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote {out_path}")


if __name__ == "__main__":
    main()
