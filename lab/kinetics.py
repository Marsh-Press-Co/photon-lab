"""
lab.kinetics — the T17 rate-equation kernel.
=============================================
A standalone, 0D, kinetics-only numerical integrator for T17's hysteretic-
σ(I) equation (LOGBOOK.md live thread T17, Panel Iteration 15 / exp-038):

    dn/dt = k_f(I)*(1 - n) - k_r*n

n(t) in [0,1] is a generic two-state population fraction (excited/colored
state) -- applicable to photochromic isomerization or linearly-pumped FCA
carrier generation alike. Deliberately decoupled from the FDTD Maxwell
solver (`lab.fdtd2d.Sim`): no grid, no beam scene, no field coupling. See
exp-038/NOTES.md for the full panel record, idealizations, and predictions.

Two propagators, cross-checked against each other and against an exact
closed form:

  * `relax_exact` -- the closed-form solution for CONSTANT (k_f, k_r) over
    an interval. Exact, not an approximation, for genuinely piecewise-
    constant forcing -- which is exactly what every scene this module
    builds uses (Test A: one constant segment; Test B: alternating
    ambient/pulse segments).
  * `relax_rk4` -- classical 4th-order Runge-Kutta over the SAME constant-
    rate segment, stepped at a caller-supplied resolution. An independent
    numerical method exercising a different code path, used as a
    convergence cross-check (suite stage 12, gate 4) -- not the primary
    result.

`integrate_segments` walks a list of (k_f, k_r, duration) segments end to
end, so RK4's step grid is always pinned exactly to segment boundaries by
construction: it never has to cross a discontinuity mid-step (Panel
Iteration 15 Phase-2 fix, EM + Red Team attack #4). Per-segment RK4 step
size is `tau_local / steps_per_tau` where `tau_local = 1/(k_f+k_r)` for
THAT segment specifically -- never a single step size shared across the
whole sweep grid (Red Team attack #2's per-configuration resolution).
"""

import numpy as np


def n_eq_exact(k_f, k_r):
    """Steady-state population n_ss = k_f/(k_f+k_r) -- T17's own closed
    form (LOGBOOK.md T17, ELECTROMAGNETISM's structural derivation,
    Red-Team-confirmed). k_f=k_r=0 is undefined physically (no dynamics at
    all); callers should not pass that point."""
    k_f = np.asarray(k_f, dtype=float)
    k_r = np.asarray(k_r, dtype=float)
    return k_f / (k_f + k_r)


def tau_exact(k_f, k_r):
    """Relaxation time constant tau = 1/(k_f+k_r)."""
    k_f = np.asarray(k_f, dtype=float)
    k_r = np.asarray(k_r, dtype=float)
    return 1.0 / (k_f + k_r)


def relax_exact(n0, k_f, k_r, dt):
    """Exact closed-form update over a CONSTANT-(k_f,k_r) interval of
    length dt:  n(t0+dt) = n_eq + (n0 - n_eq)*exp(-dt/tau).

    This is provably bounded in [0,1] whenever n0 is: n_eq in [0,1] for any
    k_f,k_r >= 0 (not both zero), and n(t0+dt) is a convex combination of
    n0 and n_eq (weights exp(-dt/tau) in [0,1] and its complement) -- so it
    can never leave [0,1]. That is gate 2a (exact by construction), not an
    empirical tolerance."""
    n_eq = n_eq_exact(k_f, k_r)
    tau = tau_exact(k_f, k_r)
    return n_eq + (n0 - n_eq) * np.exp(-dt / tau)


def _deriv(n, k_f, k_r):
    return k_f * (1.0 - n) - k_r * n


def relax_rk4(n0, k_f, k_r, h, steps):
    """Classical 4th-order Runge-Kutta over a CONSTANT-(k_f,k_r) interval,
    `steps` fixed sub-steps of size `h` each (total integrated duration =
    h*steps). `h` is the PER-STEP size directly -- callers that have a
    total duration and a step count must divide before calling (this
    function does not divide again; an earlier version of this module did
    both, silently integrating 1/steps of the intended duration -- caught
    during exp-038's own Phase-4 run, see NOTES.md). An independent
    propagator (different code path, different truncation-error structure
    than the exact exponential update) used only as a convergence
    cross-check."""
    n = float(n0)
    for _ in range(steps):
        k1 = _deriv(n, k_f, k_r)
        k2 = _deriv(n + 0.5 * h * k1, k_f, k_r)
        k3 = _deriv(n + 0.5 * h * k2, k_f, k_r)
        k4 = _deriv(n + h * k3, k_f, k_r)
        n = n + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    return n


N_TRANSIENT_TAU = 25.0
"""Multiples of tau_local beyond which the RK4 branch of `integrate_segments`
finishes a segment via the exact closed form instead of further fixed-step
RK4. Discovered necessary during exp-038's own Phase-4 implementation (not
anticipated at Phase 1-3): for a segment whose duration spans an enormous
number of relaxation times relative to its own tau (e.g. a 100ms pulse
segment at a fast host with a large enhancement factor A, where
tau_pulse can be ~1e-15s), a fixed step dt=tau_local/steps_per_tau requires
an infeasible step count if held for the FULL duration (10^14+ steps at the
grid's worst corner) -- and forcibly capping the step count instead (using
a larger effective dt) drives dt/tau_local far outside classical RK4's
stability region (|h*lambda|<~2.78 for this real-negative-eigenvalue
decay), producing genuine numerical instability, not just imprecision.
Neither is acceptable. The fix exploits that after ~25 relaxation times
n has converged to n_eq to within exp(-25)~=1.4e-11 in EITHER method, so
finishing the "boring tail" (once the transient RK4 has already fully
resolved) with the same exact closed form the primary propagator uses
changes nothing about what gate 4's cross-check actually validates (RK4's
transient accuracy) while keeping both cost and stability bounded. Disclosed
explicitly here and in exp-038/NOTES.md's Phase-4 record, not a silent
shortcut."""


def integrate_segments(segments, n0=0.0, method="exp", steps_per_tau=20,
                        record=False):
    """Walk a list of (k_f, k_r, duration) segments end to end.

    method="exp": each segment uses `relax_exact` once (no sub-stepping --
      it's exact for a constant-rate segment regardless of duration).
    method="rk4": each segment uses `relax_rk4` with its OWN per-segment
      step size dt = tau_local/steps_per_tau (tau_local from THAT
      segment's own k_f,k_r) -- resolves the global-vs-per-configuration
      Delta-t ambiguity (Red Team attack #2) by construction: there is no
      shared step size across segments or across grid points at all -- for
      at most the first `N_TRANSIENT_TAU*tau_local` of the segment; any
      remainder is finished via the exact closed form (see
      `N_TRANSIENT_TAU`'s docstring).

    If record=True, also returns (t_arr, n_arr): the cumulative time and
    population at every segment BOUNDARY (not every RK4 sub-step) -- enough
    to compute Test A's t99 and Test B's per-pulse peaks without carrying
    a huge sample array.

    Returns n_final, or (n_final, t_arr, n_arr) if record=True.
    """
    n = float(n0)
    t = 0.0
    t_list = [0.0]
    n_list = [n]
    for k_f, k_r, duration in segments:
        if duration < 0:
            raise ValueError("segment duration must be >= 0")
        if duration == 0:
            pass
        elif method == "exp":
            n = float(relax_exact(n, k_f, k_r, duration))
        elif method == "rk4":
            tau_local = float(tau_exact(k_f, k_r))
            dt = tau_local / steps_per_tau
            transient_dur = min(duration, N_TRANSIENT_TAU * tau_local)
            steps = max(1, int(np.ceil(transient_dur / dt)))
            n = relax_rk4(n, k_f, k_r, transient_dur / steps, steps)
            remainder = duration - transient_dur
            if remainder > 0:
                n = float(relax_exact(n, k_f, k_r, remainder))
        else:
            raise ValueError(f"unknown method {method!r}")
        t += duration
        t_list.append(t)
        n_list.append(n)
    if record:
        return n, np.array(t_list), np.array(n_list)
    return n


def integrate_two_state(k_f, k_r, t_span, n0=0.0, I_profile=None,
                         method="exp", steps_per_tau=20, record=False):
    """Convenience wrapper for the simple constant-(k_f,k_r) case (Test A):
    integrate from t_span[0] to t_span[1] at fixed k_f, k_r. `I_profile` is
    accepted for API-shape compatibility with a future time-varying-I
    caller but is NOT used this cycle (Phase-1 idealization: k_f is taken
    as given, not re-derived from a time-varying I(t) via microphysics) --
    passing a non-None I_profile raises, so a future cycle can't silently
    rely on an unimplemented path."""
    if I_profile is not None:
        raise NotImplementedError(
            "I_profile is not implemented this cycle (exp-038 Idealizations: "
            "k_f is taken as a given constant, not re-derived from I(t)). "
            "Use integrate_segments with an explicit segment list instead.")
    t0, t1 = t_span
    duration = t1 - t0
    return integrate_segments([(k_f, k_r, duration)], n0=n0, method=method,
                               steps_per_tau=steps_per_tau, record=record)


def t99(k_f, k_r):
    """Exact time to reach 99% of n_ss from n0=0, constant (k_f,k_r):
    t99 = tau * ln(1/(1-0.99)) = tau * ln(100) ~= 4.60517*tau. Closed form
    (not simulated) -- used both as the Test A prediction and, cheaply, as
    an internal cross-check on `integrate_segments`' own exact propagator."""
    tau = tau_exact(k_f, k_r)
    return tau * np.log(100.0)


def pulse_train_segments(k_f_ambient, k_r, A, T_pulse, dt_sweep, n_pulses):
    """Build the Test-B segment list: ambient dwell (duration dt_sweep),
    pulse (k_f = k_f_ambient*A, duration T_pulse), repeated n_pulses times,
    ending on a final ambient dwell so the last pulse's relaxation is also
    observable. All segments carry the SAME k_r (a k_r that changes with a
    generation pulse would be a different, unmodeled physical picture --
    not scoped this cycle).

    Piecewise-CONSTANT throughout, by construction (Panel Iteration 15
    Phase-3 fix: Test B is not "smoothly time-varying" -- it is a step
    function, and RK4's step grid is pinned to these exact segment
    boundaries by `integrate_segments`)."""
    k_f_pulse = k_f_ambient * A
    segs = []
    for _ in range(n_pulses):
        segs.append((k_f_ambient, k_r, dt_sweep))
        segs.append((k_f_pulse, k_r, T_pulse))
    segs.append((k_f_ambient, k_r, dt_sweep))
    return segs
