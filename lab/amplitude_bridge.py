"""
lab.amplitude_bridge — the n(t) -> sigma_e(t) -> C(t) amplitude bridge.
========================================================================
Panel Iteration 17 (exp-040), lead THERMODYNAMICS, synthesized after a
full seven-seat cycle whose Phase-2 packet (five blind critiques + Red
Team) is the densest catch-set this program has produced in one cycle --
see LOGBOOK.md Iteration 17 for the full transcript. Retires Iteration
16's #1-ranked priority: the missing amplitude half of any T3-provisional
timing classification (exp-039), letting a switching population n(t)
(`lab.kinetics`, stage-12-gated) become a scored Weber contrast against
T2's frozen C_thr(L) for the FIRST time in this program's history.

THE CHAIN, three composed maps:

  (a) n(t) -> sigma_e(t)   `sigma_e_of_n` -- bounded LINEAR interpolation
      between two REAL, already-FDTD-measured static articles (exp-026's
      off_lab/on). eps_r == 1 EXACTLY at every n (no Delta-eps_real term
      anywhere in this chain -- see IDEALIZATION 2 below, and QUANTUM
      OPTICS' Phase-2 catch: this is Kramers-Kronig-forbidden in the
      strict sense and creates a real, computed-not-ignored constraint-2
      exposure, carried as a disclosed correction, not a run).
  (b) sigma_e(t) -> tau(t) -> C(t)   `chord_contrast` -- a saturating
      ray-chord integral, generalizing exp-034's committed
      `chord_model_g0` (same geometry, same rays) to the FULL non-linear
      saturating regime instead of only chord_model_g0's own tau->0
      linear limit. Reproduces exp-026's MEASURED chord-model column to
      0.40-0.72% (independently re-verified this cycle -- Director,
      Phase 3). NOT treated as an independent cross-check of anything:
      Red Team's Phase-2 attack #3 found the weak-limit reduction
      (P-TH-2) would otherwise be a near-tautology against
      `chord_model_g0`, since both share the identical ray-chord code
      path -- stage 14 anchors against exp-026's MEASURED FDTD numbers
      instead (a genuine regression anchor, not a same-formula echo).
  (c) C(t) -> verdict   scored against T2's C_thr(L), BOTH tiers, with
      T2's own +-0.3-log VERTICAL threshold uncertainty carried as a
      mandatory second uncertainty term (Red Team attack #9 / VISION
      Phase-2 flip condition) -- the dominant term at every Tier-W row,
      never live before this cycle because every prior scored citation
      sat at photopic L>=3 where the max[1,.] clamp makes it inert.

CAUSALITY. sigma_e(t) depends on n(t) ONLY, same-instant, never
anticipatory; n(t) is itself `lab.kinetics`'s retarded single-pole
response to I(t'<=t). No inverse-time term exists anywhere in the chain.

PASSIVITY. n in [0,1] is exact by construction (`kinetics` stage-12 gate
2a), so sigma_e(t) in [sigma_off, sigma_on] with sigma_off > 0 --
Joule density (1/2)*sigma_e*|E|^2 >= 0 at every instant. eps_r is
time-INDEPENDENT throughout, so the Poynting energy theorem carries no
parametric-gain term: d u/dt + div S = -sigma(t)|E|^2 <= 0 pointwise,
an unconditional theorem for this sub-class (ELECTROMAGNETISM's Phase-2
steel-man, independently reconfirmed by Red Team from `lab/fdtd2d.py`'s
own update-coefficient structure -- ca/cb are computed ONCE, outside the
step loop, so a genuinely time-varying medium is correctly named
Checkpoint-3 territory and correctly NOT attempted this cycle).

QUASI-STATIC VALIDITY (Red Team attack #11, adopting ELECTROMAGNETISM's
Phase-2 fix over the Phase-1 proposal's own criterion). The governing
small parameter for a channel whose C(t) is read as a CW steady-state
phasor after a FIXED number of settling steps is t_settle/tau_local, NOT
1/(omega*tau_local) -- the two differ by a large, tau-independent
constant (2*pi*periods, periods = STEPS_AMBIENT/(cpl/S)) at this bench's
own settling convention. `settling_time_s` computes t_settle FROM THE
INSTRUMENT'S OWN PARAMETERS (cpl, courant_frac, step count, source
wavelength) -- never hand-typed, per Red Team's explicit mandatory fix.
`is_quasistatic` gates tau_local >= 100*t_settle (re-referenced from the
Phase-1 proposal's 100 optical periods, which Red Team's independent
enumeration showed under-counts the INVALID set 2 vs the correct 5, with
two more within 2% of the boundary).

Trust gates: suite stage 14 (`lab/validation/run_all.py::stage14_amplitude_bridge`)
-- green before any classification is believed.
"""

import math

import numpy as np


# --------------------------------------------------------------- (a) n -> sigma_e

def sigma_e_of_n(n, sigma_off, sigma_on):
    """Bounded linear interpolation, sigma_off at n=0, sigma_on at n=1.
    Exact by construction: n in [0,1] (kinetics stage-12 gate 2a) implies
    sigma_e in [sigma_off, sigma_on] whenever sigma_on >= sigma_off > 0 --
    a convex-combination argument, the same style as `kinetics.relax_exact`'s
    own boundedness proof."""
    n = np.asarray(n, dtype=float)
    return sigma_off + n * (sigma_on - sigma_off)


def sigma_from_tau(tau, r_out):
    """The ONE canonical way to turn a target tau_center into a per-cell
    conductivity for a uniform disk of radius r_out: sigma = tau/(2*r_out)
    (exp-026's own established convention). Every article-building call
    site in this experiment MUST derive sigma this way, from THAT block's
    OWN r_out -- Red Team's attack #2 (Panel Iteration 17, load-bearing):
    a sigma pinned as a bare number and reused across a rescaled-geometry
    R3 block silently drifts tau by the geometry's own scale ratio (a
    50% drift measured at exp-040's own Block R geometry, R_OUT 78->117
    -- the same defect class as exp-027's published T10 SIGMA_ON erratum).
    Callers MUST additionally assert abs(2*sigma*r_out - tau) < 1e-9 at
    the point of use, per-block, per-article -- this function alone does
    not protect against a stale r_out at the CALL SITE."""
    return tau / (2.0 * r_out)


def tau_of_n(n, tau_off, tau_on):
    """tau_center(n) = tau_off + n*(tau_on - tau_off) -- linear in n because
    tau_center = 2*sigma_e*r_out is linear in sigma_e itself. Equivalent to
    2*r_out*sigma_e_of_n(n, sigma_off, sigma_on) but avoids a redundant r_out
    round-trip."""
    n = np.asarray(n, dtype=float)
    return tau_off + n * (tau_on - tau_off)


def n_of_tau(tau, tau_off, tau_on):
    """Inverse of `tau_of_n` -- the finite-D population fraction that
    produces a given tau_center. n_of_tau(tau_off,...) == 0 exactly;
    n_of_tau(tau_on,...) == 1 exactly."""
    tau = np.asarray(tau, dtype=float)
    return (tau - tau_off) / (tau_on - tau_off)


# ------------------------------------------------------------- (b) tau -> C(t)

def chord_contrast(tau, r_out, plane_dx, angles_deg, guard_out, w_flank):
    """The saturating ray-chord Weber contrast at conductivity tau_center =
    2*sigma*r_out, for a uniform disk illuminated by the `angles_deg` plane-
    wave set at this instrument's own (r_out, plane_dx, guard_out, w_flank)
    geometry. Generalizes exp-034's `chord_model_g0` (same rays, same
    windows) to the FULL saturating regime -- `chord_model_g0(...)` is
    recovered exactly as `chord_contrast(tau_probe, ...)/tau_probe` in the
    tau_probe->0 limit (Director, Phase 3: independently reproduced
    g0 = 0.68571636805 to 10 significant figures against exp-034's own
    committed number, matching P-TH-2's proposed value).

    NOT an independent cross-check of `chord_model_g0` -- it is the SAME
    ray-chord code path evaluated off the linear limit (Red Team Phase-2
    attack #3, PHOTONICS' Phase-2 observation). Suite stage 14 therefore
    anchors this function against exp-026's MEASURED FDTD column, not
    against `chord_model_g0`'s own output (a genuine regression anchor;
    see stage14_amplitude_bridge's own docstring)."""
    lever = r_out + plane_dx
    ny_rel = int(4 * (guard_out + w_flank))
    y = np.arange(-ny_rel // 2, ny_rel // 2, dtype=float)
    sigma = tau / (2.0 * r_out)
    b_obj, b_flank, wsum = 0.0, 0.0, 0.0
    for th in angles_deg:
        off = lever * math.tan(math.radians(th))
        yc = y - off
        inside = np.abs(yc) < r_out / math.cos(math.radians(th))
        chord = np.zeros_like(y)
        perp = yc * math.cos(math.radians(th))
        chord[inside] = 2.0 * np.sqrt(np.maximum(r_out ** 2 - perp[inside] ** 2, 0.0))
        b = np.exp(-sigma * chord)
        obj_w = np.abs(y) <= r_out
        flank_w = (np.abs(y) >= guard_out) & (np.abs(y) <= guard_out + w_flank)
        b_obj += b[obj_w].mean()
        b_flank += b[flank_w].mean()
        wsum += 1.0
    b_obj /= wsum
    b_flank /= wsum
    c_geo = (b_obj - b_flank) / b_flank
    return abs(float(c_geo))


def chord_contrast_asymptote(r_out, plane_dx, angles_deg, guard_out, w_flank):
    """|C(tau->infinity)| -- the chord model's own saturation ceiling
    (opaque-disk limit; every ray inside the disk fully extinguished).
    Evaluated at a large finite tau (1e6) rather than analytically, since
    the flank window can carry a nonzero residual at extreme angles for
    some geometries -- consistent with how `chord_contrast` itself is
    always evaluated."""
    return chord_contrast(1.0e6, r_out, plane_dx, angles_deg, guard_out, w_flank)


def tau_thr_from_c_thr(c_thr, r_out, plane_dx, angles_deg, guard_out, w_flank,
                        lo=1e-9, hi=1.0e4):
    """Invert `chord_contrast` for the tau_center at which the model first
    reaches |C| = c_thr (bisection -- the model is monotonic, gated by
    `check_monotonic`, so the inversion is well-posed). Returns None if
    c_thr exceeds the model's own saturation asymptote (no tau solves it --
    Red Team attack #9's own +0.3-log p=0.5 finding)."""
    asym = chord_contrast_asymptote(r_out, plane_dx, angles_deg, guard_out, w_flank)
    if c_thr >= asym:
        return None
    f = lambda t: chord_contrast(t, r_out, plane_dx, angles_deg, guard_out, w_flank) - c_thr
    a, b = lo, hi
    fa, fb = f(a), f(b)
    if fa > 0 or fb < 0:
        raise ValueError(f"tau_thr bracket does not contain a root: f({a})={fa}, f({b})={fb}")
    for _ in range(200):
        m = 0.5 * (a + b)
        fm = f(m)
        if fm > 0:
            b = m
        else:
            a = m
        if b - a < 1e-13 * max(1.0, m):
            break
    return 0.5 * (a + b)


def check_monotonic(r_out, plane_dx, angles_deg, guard_out, w_flank,
                     tau_lo=1e-4, tau_hi=10.0, n=10000):
    """|chord_contrast(tau)| strictly increasing over [tau_lo, tau_hi] --
    P-TH-3's monotonicity gate. Returns (n_violations, max_backstep)."""
    taus = np.geomspace(tau_lo, tau_hi, n)
    vals = np.array([chord_contrast(t, r_out, plane_dx, angles_deg, guard_out, w_flank)
                      for t in taus])
    diffs = np.diff(vals)
    n_violations = int(np.sum(diffs <= 0.0))
    max_backstep = float(np.min(diffs)) if diffs.size else 0.0
    return n_violations, max_backstep


# ------------------------------------------------------- n_ss ceilings, A_req

def n_ss_ceiling(tau_thr, tau_on, tau_off=0.0):
    """The at-rest population ceiling n_ss,max such that tau(n_ss,max) ==
    tau_thr, i.e. the largest at-rest switched population a material can
    carry without breaching a given constraint-3 bar tau_thr, GIVEN this
    article's own measured tau_on. tau_off=0.0 recovers the D->infinity
    idealization (n_ss,max = tau_thr/tau_on, the Phase-1 proposal's
    original headline table); tau_off > 0 gives the FINITE-D reading Red
    Team's attack #8 and MATERIALS/VISION's Phase-2 critiques required
    reported alongside it. Returns a negative value (EMPTY -- no feasible
    at-rest population clears this bar even at n=0) if tau_off itself
    already exceeds tau_thr."""
    return (tau_thr - tau_off) / (tau_on - tau_off)


def n_ss_ceiling_reciprocal_of_d_req(tau_thr, tau_on):
    """n_ss,max(D->infinity) == 1/D_req identically (Red Team attack #7,
    MATERIALS' Phase-2 catch, independently reconfirmed): D_req = tau_on/tau_thr
    (`REALIZABILITY_MEMO.md`'s own definition), so 1/D_req = tau_thr/tau_on
    = n_ss_ceiling(tau_thr, tau_on, tau_off=0.0) exactly. Provided as an
    explicit identity check, not a second computation."""
    d_req = tau_on / tau_thr
    return 1.0 / d_req


def a_req(f_peak, n_ss):
    """The pulse/ambient irradiance-enhancement ratio A required to reach a
    peak population n_peak = f_peak (f_peak = tau_peak/tau_on in the
    D->infinity idealization) GIVEN an at-rest population n_ss, under
    `lab.kinetics`'s own steady-state law n = A*r/(1+A*r) with ambient
    n_ss = r/(1+r):

        A_req = [n_peak/(1-n_peak)] / [n_ss/(1-n_ss)]

    Diverges as f_peak -> 1 (n_peak -> 1, tau_peak -> tau_on) -- Red Team
    attack #1, load-bearing: the Phase-1 proposal's own "cleared by 9.4x"
    claim silently evaluated this at f_peak=0.5 (tau_peak=1.95, 14.2%
    beam-behind), far short of the proposal's OWN stated constraint-1
    requirement tau_peak>=3.9 (f_peak=1.0, where A_req is infinite).
    Raises ValueError if n_ss<=0 or n_ss>=1 or f_peak>=1 (both odds ratios
    must be finite and positive)."""
    if not (0.0 < n_ss < 1.0):
        raise ValueError(f"n_ss must be in (0,1), got {n_ss}")
    if not (0.0 < f_peak < 1.0):
        raise ValueError(f"f_peak must be in (0,1) -- use a value < 1.0 to avoid the pole")
    odds_peak = f_peak / (1.0 - f_peak)
    odds_ss = n_ss / (1.0 - n_ss)
    return odds_peak / odds_ss


# ------------------------------------------------------------- quasi-static gate

C_LIGHT_M_S = 2.99792458e8


def settling_time_s(cpl, courant_frac, steps, lambda_nm):
    """Physical time (s) elapsed after `steps` leapfrog updates of this
    engine's own 2D TMz Courant convention (S = courant_frac/sqrt(2),
    `lab.fdtd2d`), for a source wavelength lambda_nm, at cells-per-lambda
    `cpl`. Computed from the instrument's own parameters -- Red Team's
    attack #11 mandatory fix: NEVER hand-typed, so a future cpl/courant/
    step-count change cannot silently desync this from the instrument it
    gates. Returns (t_settle_seconds, periods_elapsed)."""
    s_courant = courant_frac / math.sqrt(2.0)
    steps_per_period = cpl / s_courant
    periods = steps / steps_per_period
    period_s = (lambda_nm * 1e-9) / C_LIGHT_M_S
    return periods * period_s, periods


def is_quasistatic(tau_local_s, t_settle_s, margin=100.0):
    """True iff tau_local_s >= margin*t_settle_s -- the re-referenced
    adiabaticity criterion (Red Team attack #11, adopting ELECTROMAGNETISM's
    Phase-2 fix over the Phase-1 proposal's own 100-optical-period test).
    The governing small parameter for a CW phasor read after a FIXED
    settling-step budget is t_settle/tau_local, not 1/(omega*tau_local) --
    the two differ by omega*t_settle = 2*pi*periods, a large tau-INDEPENDENT
    constant at this bench's own settling convention (~308 at 600nm,
    exp-026's STEPS_AMBIENT=1400/cpl=20)."""
    return bool(tau_local_s >= margin * t_settle_s)


# ------------------------------------------------------- THERMO sidecar (exact)

def chord_absorptance_exact(tau, n=20001):
    """The exact, area-averaged, boresight (normal-incidence) chord
    absorptance A(tau) = <1 - exp(-sigma*chord(y))>_y over the disk's own
    impact-parameter range y in [-r_out, r_out] (chord(y) = 2*sqrt(r_out^2
    - y^2), sigma = tau/(2*r_out) -- r_out cancels exactly, so A depends
    only on tau, dimensionlessly). Replaces exp-034's committed
    `chord_absorptance(tau) = (pi/4)*tau*(1 - 4*tau/(3*pi))`, a weak-tau
    Taylor series that Red Team's Phase-2 audit found 65.2% LOW at
    tau=1.95 (not the Phase-1 proposal's stated "8% low") and UNPHYSICAL
    (negative, -2.007) at tau=3.9, the program's own established ON
    article -- crossing zero at tau=3*pi/4=2.35619, independently
    reconfirmed by two blind seats (PHOTONICS) and the Director (Phase 3).
    The series and this exact integral agree to 5 significant figures only
    at tau<=0.032 (exp-026's OFF-lab endpoint) -- THIS function, not the
    series, is the one used anywhere tau approaches the shoulder (tau>~0.3)
    or the ON endpoint (tau=3.9)."""
    r_out = 1.0   # cancels; kept as an explicit unit-radius disk for clarity
    sigma = tau / (2.0 * r_out)
    y = np.linspace(-r_out, r_out, n)
    chord = 2.0 * np.sqrt(np.maximum(r_out ** 2 - y ** 2, 0.0))
    absorptance = 1.0 - np.exp(-sigma * chord)
    return float(np.trapezoid(absorptance, y) / (2.0 * r_out))


def chord_absorptance_series_legacy(tau):
    """exp-034's original committed weak-tau series, kept ONLY for the
    stage-14 defect-regression gate (must stay negative at tau=3.9 and
    cross zero at 3*pi/4 -- proof the replacement was necessary, not a
    silent rewrite of history)."""
    return (math.pi / 4.0) * tau * (1.0 - (4.0 / (3.0 * math.pi)) * tau)
