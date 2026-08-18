"""exp-042 design constants -- The Edge-Diffraction Magnitude Bridge (T21).
=============================================================================
Panel Iteration 19 (lead: VISION SCIENCE, rotation). Executes LOGBOOK.md
Iteration 18's Red-Team-ranked #1 priority: score ELECTROMAGNETISM's own
Iteration-18 Phase-5 edge-diffraction mechanism against all 30 of exp-041's
Block MAIN signed C_empty(theta,lambda) rows at MAGNITUDE level, not just
sign/ranking -- the single gap standing between live thread T21's PARTIAL
and a magnitude-confirmed mechanism. Paired with VISION's own zero-cost
beam-divergence/contamination-risk check (does the T21 fringe survive a
realistic flashlight beam's own angular spread).

Zero new FDTD calls. Every geometry constant below is copied VERBATIM from
experiments/041-t20-angle-audit/design_geometry.py -- this leg scores
against THAT experiment's own committed results.json, not a rescaled or
rebuilt geometry.

MANDATORY FIXES applied here (Red Team, Panel Iteration 19 Phase 2 --
verdict PROCEED-WITH-MANDATORY-FIXES; full numbered attack list in
LOGBOOK.md Iteration 19 / NOTES.md Phase 3):

  1. [PHOTONICS attack, Red-Team-confirmed to 3 sig figs by an independent
     reimplementation, LOAD-BEARING] The PRIMARY, headline-scoring model
     uses the flux/Poynting reduction (Rayleigh-Sommerfeld obliquity factor
     cos(psi) = D_SP/r applied to each Huygens wavelet BEFORE the coherent
     sum) -- because `lab.ambient.observer_profile` is verified by direct
     code read to return a Poynting FLUX (`-sections.flux_profile_x`), not
     bare |E|^2. The naive |E|^2 (no obliquity) reduction is reported
     ALONGSIDE as an explicitly labeled SECONDARY/context reading, never as
     "the" zero-free-parameter result.
  2. [Red Team, load-bearing] The "zero free parameters" language is scoped
     precisely: `lab.ambient.weber()` is homogeneous degree 0 in any UNIFORM
     rescale of the profile b(y) -> c*b(y) (re-derivable in one line, and
     re-verified against `lab/ambient.py:53-56` directly) -- that protects
     ONLY a uniform source-amplitude calibration constant. The intensity-
     vs-flux reduction choice is NOT a uniform rescale (cos(psi) ranges
     ~0.65-1.0 across the scored object/flank windows, verified below) --
     it is a separate, unprotected axis, and is NOT covered by the
     homogeneity argument.
  3. [Red Team, load-bearing] This module's own numbers supersede VISION's
     Phase-1 preliminary run -- reproduced independently three times now
     (VISION's own first pass, PHOTONICS' Phase-2 reimplementation, Red
     Team's Phase-2 reimplementation, and this committed module) but
     VISION's own original (R^2=0.656, c~1.6) matches NEITHER the naive NOR
     the flux convention exactly -- a fourth, undisclosed implementation
     choice. This module's own numbers are the ones NOTES.md predictions
     and Results are scored against, not VISION's preliminary figures.
  4. [Red Team, load-bearing] The best-fit scale c* is reported and labeled
     "of undetermined origin -- real residual vs. leftover convention
     artifact not yet distinguished" -- NOT asserted as "definitely real,
     non-cancelling physics" (EM's Phase-2 language) nor as a "benign
     calibration echo" (the implicit reading a bare "zero-free-parameter"
     claim invites). Distinguishing the two is future-cycle scope.
  5. [MATERIALS attack, Red-Team-confirmed directly against code,
     LOAD-BEARING] Domain-mismatch disclaimer: this leg's geometry
     (MARGIN_MULT=3.5, R_OUT=78 native -- exp-024/041's domain) is NOT the
     domain (RATIO=1.5, R_OUT=117, `experiments/035-t16-domain-quadrature-
     factorial/design_geometry.py`'s Block N17_NATIVE_V2) that produced the
     exp-032 PASS->MARGINAL delta (6.522e-4) `REALIZABILITY_MEMO.md`'s
     Amendment 1 cites. A clean fit here is real information about the
     edge-diffraction mechanism at EXP-041's OWN geometry; it is NOT
     evidence about that specific realizability citation, which lives at a
     structurally different domain. MATERIALS' own realizability-relevance
     cap (carried forward from exp-041, unchanged) also applies: this leg's
     result, in either direction, cannot move either UNOBTANIUM-WITH-
     PARAMETERS verdict.
  6. [QUANTUM OPTICS attack, independently reproduced by Red Team and found
     WORSE than first framed -- >2 orders of magnitude swing, not just
     "could go either direction" -- LOAD-BEARING] The beam-divergence check
     reports BOTH an incoherent angular power-sum (matching
     `lab.ambient.incoherent_sum`'s own convention, the physically
     appropriate model for a real, spatially-extended, low-coherence
     emitter) AND a coherent finite-angular-spread sum (each angular
     component's field coherently added, phase-referenced through the
     SAME shared aperture-center origin already used by every single-angle
     `field_profile` call -- an analytic realization of the same coherent-
     superposition PRINCIPLE QUANTUM's own Iteration-6 (exp-029) bench-
     validated, NOT a literal reuse of exp-029's own FDTD injection code,
     since this whole leg is desk-only by design; this substitution is
     disclosed here, not silently implied). ANY contamination-risk language
     in Results is gated on BOTH readings being reported side by side, and
     is not treated as settled until the sharp divergence between them
     (see Results) is itself explained.
  7. [THERMODYNAMICS attack, load-bearing] Explicit Phase-3 disposition on
     PLAN.md's two queued THERMO items (docket #7's sourced witness table;
     `lab/thermo_sidecar.py` re-scoping): DEFERRED to a future iteration,
     explicitly, not by silent default -- reason stated in NOTES.md Phase 3
     (this leg's own Phase-2 debate already produced 8 mandatory fixes
     spanning two independent physical conventions; docket #7 is a
     WebSearch-grounded literature-sourcing task and the sidecar re-scoping
     is a separate code deliverable -- bundling either into this leg risks
     under-resourcing both, the same scope-discipline concern exp-041's own
     Phase-3 raised for a genuinely budget-conflicted cycle. Ranked as the
     explicit #1 priority for the next iteration in Phase 5 below, not left
     to silently recur an eighth time.)
  8. [ELECTROMAGNETISM attack, independently re-derived and confirmed near-
     exactly by Red Team] Idealizations extended: the edge-to-observer
     causal transit margin is wavelength-dependent -- STEPS=1400,
     r_edge=sqrt(D_SP^2+A^2)=784.4 cells, S=courant_frac/sqrt(2)=0.700
     cells/step -> transit ~1120 steps, leaving 280 steps (13.0/9.8/7.8
     periods at 450/600/750nm) -- THINNEST at 750nm, the same wavelength
     whose P-M1 prediction exp-041's own Phase-4 record shows was refuted.
     A disclosed, untested candidate confound for 750nm's worse fit below
     (see Results) -- this leg's own continuum propagator cannot see it by
     construction (it has no FDTD settling dynamics at all).

Pure geometry + analytic propagation -- no FDTD, no new engine code. Run
this module directly; the self-checks below verify A=752, the aperture
taper's bit-identical reproduction of `lab.fdtd2d.Sim.add_line_source`'s
own array, and the kr>>1 far-field validity range, before anything here is
trusted.
"""

import numpy as np

# ----------------------------------------------------------- pinned geometry
# Every constant below is copied VERBATIM from
# experiments/041-t20-angle-audit/design_geometry.py -- this leg scores
# against THAT experiment's own committed results.json.
NX = 360
NY = 1584
ABSORB = 40
TAPER = 40
SRC_X = 300
PLANE_X = 77
OBJ_X = 170
R_OUT = 78
GUARD_OUT = 185
W_FLANK = 78
CPL = {450: 15, 600: 20, 750: 25}
STEPS = 1400
COURANT_FRAC = 0.99

OBJ_Y = NY // 2                      # 792 -- window/aperture center
D_SP = SRC_X - PLANE_X               # 223 -- source -> observation-plane distance
Y_LO = ABSORB                        # 40  -- aperture hard rim (add_line_source default y_lo)
Y_HI = NY - ABSORB                   # 1544 -- aperture hard rim (add_line_source default y_hi)
A = OBJ_Y - Y_LO                     # 752 -- edge-to-window-center offset (EM's own A)

assert A == 752 and (Y_HI - OBJ_Y) == 752, \
    f"A drift from Iteration-18's own citation: {A}, {Y_HI - OBJ_Y}"

# bonus cross-check (EM's Phase-5 citation, Iteration 18): straight-line
# rim-to-observer distance should be ~784 cells
R_EDGE = float(np.hypot(D_SP, A))
assert abs(R_EDGE - 784.4) < 0.1, f"r_edge drift: {R_EDGE}"

# ------------------------------------------------------- source aperture
def aperture_profile(edge=TAPER, y_lo=Y_LO, y_hi=Y_HI):
    """Bit-identical reproduction of `Sim.add_line_source`'s own tapered
    top-hat array (`lab/fdtd2d.py:132-172`, profile='plane' path) -- same
    raised-cosine formula, same edge width. Self-checked below."""
    n = y_hi - y_lo
    p = np.ones(n)
    win = 0.5 * (1.0 - np.cos(np.pi * np.arange(edge) / edge))
    p[:edge] = win
    p[-edge:] = win[::-1]
    return p


P = aperture_profile()
Y_SRC = np.arange(Y_LO, Y_HI, dtype=float)
Y_OBS = np.arange(Y_LO, Y_HI, dtype=float)          # same span the FDTD capture's
                                                      # observer_profile(...,Y_LO,Y_HI) reads

# self-check: taper shape sane (endpoints ~0, plateau ~1, monotonic ramp)
assert P[0] < 1e-6 and P[-1] < 1e-6 and abs(P[len(P) // 2] - 1.0) < 1e-9
assert np.all(np.diff(P[:TAPER]) >= -1e-12)          # monotonically rising into the plateau

# ----------------------------------------------- geometry for the propagator
_DY = Y_OBS[:, None] - Y_SRC[None, :]
_R = np.sqrt(D_SP ** 2 + _DY ** 2)
_OBLIQUITY = D_SP / _R                                # cos(psi), Rayleigh-Sommerfeld obliquity

# self-check: obliquity range across the SCORED windows (object + flank) --
# demonstrates it is NOT a uniform factor (mandatory fix 2)
_obj_rows = np.abs(Y_OBS - OBJ_Y) <= R_OUT
_flank_rows = (np.abs(Y_OBS - OBJ_Y) >= GUARD_OUT) & (np.abs(Y_OBS - OBJ_Y) <= GUARD_OUT + W_FLANK)
OBLIQUITY_RANGE_OBJ = (float(_OBLIQUITY[_obj_rows].min()), float(_OBLIQUITY[_obj_rows].max()))
OBLIQUITY_RANGE_FLANK = (float(_OBLIQUITY[_flank_rows].min()), float(_OBLIQUITY[_flank_rows].max()))

# self-check: kr >> 1 far-field validity, every source cell, every lambda
_KR_MIN = {lam: float(2 * np.pi / cpl * _R.min()) for lam, cpl in CPL.items()}
_KR_MAX = {lam: float(2 * np.pi / cpl * _R.max()) for lam, cpl in CPL.items()}
for _lam in CPL:
    assert _KR_MIN[_lam] > 50, f"kr validity marginal at {_lam}nm: {_KR_MIN[_lam]}"

# --------------------------------------------------- causal transit margin
# (Idealization, mandatory fix 8 -- EM's own finding, Red-Team-confirmed)
_S = COURANT_FRAC / np.sqrt(2.0)
TRANSIT_STEPS = R_EDGE / _S
MARGIN_STEPS = STEPS - TRANSIT_STEPS
MARGIN_PERIODS = {lam: MARGIN_STEPS * _S / cpl for lam, cpl in CPL.items()}

_Gcache = {}


def _G_for(lam_cells, obliquity):
    """Propagator matrix G[i,j] = exp(i(k*r-pi/4))/sqrt(r) [* cos(psi)],
    r = distance from source cell j (x=SRC_X) to observation cell i
    (x=PLANE_X). Depends only on lambda and the obliquity flag -- cached
    per (lambda, obliquity), reused across every theta (the coherent
    beam-divergence sum needs many theta at fixed lambda; rebuilding this
    NX_obs x NX_src matrix per theta would be wasteful and was the
    original prototype's own performance bug, fixed here)."""
    key = (lam_cells, obliquity)
    if key not in _Gcache:
        k = 2.0 * np.pi / lam_cells
        G = np.exp(1j * (k * _R - np.pi / 4)) / np.sqrt(_R)
        if obliquity:
            G = G * _OBLIQUITY
        _Gcache[key] = (k, G)
    return _Gcache[key]


def _src_amp(theta_deg, k):
    """Complex per-cell source weight: taper amplitude x phase ramp,
    exactly `add_line_source`'s own `phase = k*sin(theta)*(y-yc)` with
    yc = 0.5*(y_lo+y_hi) = OBJ_Y (verified: the source aperture is centered
    on the SAME NY as the object window, by construction)."""
    phase = k * np.sin(np.radians(theta_deg)) * (Y_SRC - OBJ_Y)
    return P * np.exp(1j * phase)


def field_profile(theta_deg, lam_cells, obliquity=True):
    """Coherent Huygens-Fresnel flux profile B(y) at the observation plane
    for ONE injection angle theta and wavelength lambda. obliquity=True is
    the PRIMARY (flux/Poynting-consistent) reduction; obliquity=False is
    the SECONDARY (naive |E|^2) reduction, reported as context only."""
    k, G = _G_for(lam_cells, obliquity)
    E = G @ _src_amp(theta_deg, k)
    return np.abs(E) ** 2


def edge_diffraction_c_empty(theta_deg, lam_cells, obliquity=True):
    """Predicted C_empty(theta,lambda) -- the single number scored against
    exp-041's results.json rows. Reduced through `lab.ambient.window_means`
    / `weber` DIRECTLY (imported, not reimplemented) -- the same functions
    that produced every measured row, so this is an apples-to-apples
    comparison, not a parallel metric."""
    from lab import ambient as amb
    b = field_profile(theta_deg, lam_cells, obliquity)
    bo, bf = amb.window_means(b, Y_LO, OBJ_Y, R_OUT, GUARD_OUT, W_FLANK)
    return amb.weber(bo, bf)


def gaussian_angle_weights(theta0_deg, fwhm_deg, n=41, half_width_factor=2.5):
    """n angular samples of a Gaussian(theta0, FWHM) kernel, +-2.5 FWHM
    (>99.9% of the Gaussian mass), weights normalized to sum 1."""
    sigma = fwhm_deg / 2.3548
    thetas = np.linspace(theta0_deg - half_width_factor * fwhm_deg,
                          theta0_deg + half_width_factor * fwhm_deg, n)
    w = np.exp(-0.5 * ((thetas - theta0_deg) / sigma) ** 2)
    w /= w.sum()
    return thetas, w


def beam_divergence_incoherent(theta0_deg, fwhm_deg, lam_cells, n=41):
    """VISION's own check, PRIMARY reading: n angular components, each an
    independent `field_profile` (flux/obliquity-consistent), combined via
    `lab.ambient.incoherent_sum` -- REUSES the actual production function,
    the same one this program's real N9/N17/fallback angular-quadrature
    measurements use for genuinely separate illumination directions."""
    from lab import ambient as amb
    thetas, w = gaussian_angle_weights(theta0_deg, fwhm_deg, n)
    k, G = _G_for(lam_cells, True)
    profiles = [np.abs(G @ _src_amp(th, k)) ** 2 for th in thetas]
    flanks = [amb.window_means(b, Y_LO, OBJ_Y, R_OUT, GUARD_OUT, W_FLANK)[1] for b in profiles]
    s = amb.incoherent_sum(profiles, flanks, list(w))
    bo, bf = amb.window_means(s, Y_LO, OBJ_Y, R_OUT, GUARD_OUT, W_FLANK)
    return amb.weber(bo, bf)


def beam_divergence_coherent(theta0_deg, fwhm_deg, lam_cells, n=41):
    """QUANTUM's mandatory cross-check (mandatory fix 6): n angular field
    components summed COHERENTLY (sqrt(weight)-scaled complex field, shared
    aperture-center phase reference already built into `_src_amp`) BEFORE
    taking |E|^2 -- an analytic realization of the coherent-superposition
    PRINCIPLE exp-029 bench-validated, not a literal reuse of its FDTD
    injection code. One specific, simple, disclosed phase convention among
    possible coherent models (Red Team's own caveat) -- NOT asserted as the
    physically correct answer for a real (finite-coherence-length)
    flashlight, only as the mandated upper-bound cross-check."""
    from lab import ambient as amb
    thetas, w = gaussian_angle_weights(theta0_deg, fwhm_deg, n)
    k, G = _G_for(lam_cells, True)
    E_tot = np.zeros(Y_OBS.size, dtype=complex)
    for th, wt in zip(thetas, w):
        E_tot = E_tot + np.sqrt(wt) * (G @ _src_amp(th, k))
    b = np.abs(E_tot) ** 2
    bo, bf = amb.window_means(b, Y_LO, OBJ_Y, R_OUT, GUARD_OUT, W_FLANK)
    return amb.weber(bo, bf)


def main():
    print(f"exp-042 geometry -- scoring against exp-041's own committed geometry")
    print(f"NY={NY} ABSORB={ABSORB} SRC_X={SRC_X} PLANE_X={PLANE_X} D_SP={D_SP} "
          f"OBJ_Y={OBJ_Y} A={A} R_EDGE={R_EDGE:.1f}")
    print(f"obliquity range -- object window: {OBLIQUITY_RANGE_OBJ}, "
          f"flank window: {OBLIQUITY_RANGE_FLANK} (NOT uniform -- mandatory fix 2)")
    print(f"kr validity (min,max) by lambda: "
          + ", ".join(f"{lam}nm=({_KR_MIN[lam]:.1f},{_KR_MAX[lam]:.1f})" for lam in CPL))
    print(f"causal transit margin (periods) by lambda: "
          + ", ".join(f"{lam}nm={MARGIN_PERIODS[lam]:.1f}" for lam in CPL))


if __name__ == "__main__":
    main()
