"""exp-048 design constants -- Closing exp-047's Evidentiary Chord: the
REALIZABILITY_MEMO.md entry (Block A), the T21 fringe bound at the actual
+-35deg fallback geometry (Block B), and the MARGINAL-band source check
(Block C).
=============================================================================
Panel Iteration 25 (lead: VISION SCIENCE, rotation). Executes LOGBOOK.md
Iteration 24 / exp-047 NOTES.md's own ranked queue, items 1-3. Zero new
FDTD calls -- desk arithmetic (Block A), a re-parameterized reuse of
exp-042's own committed analytic propagator (Block B), and a citation
trace (Block C).

MANDATORY FIXES applied here (Red Team, Panel Iteration 25 Phase 2 --
verdict PROCEED-WITH-MANDATORY-FIXES; full numbered attack list in
LOGBOOK.md Iteration 25 / NOTES.md Phase 3):

  1. [new, Red Team attack 1] Block A's core-radius figures do NOT come
     from a "verbatim" call to `experiments/030-scale-bridge/design_geometry
     .py::r_in_shell`, whose `round()` is a CELL-QUANTIZATION operation --
     called on meter-valued input it silently returns 0/0/1 m, not the
     cited 0.192/0.385/0.577 m. This module instead evaluates the
     CONTINUOUS ratio R_IN_BASE_FRAC * r_w directly, disclosed here as a
     deliberate, stated deviation from the cited function's own rounding
     behaviour (meaningless at continuous meter scale), not a silent
     "verbatim" reuse.
  2. [MATERIALS attack, Red-Team-hardened, LOAD-BEARING] Block A's
     sigma_max/e-folding-length figures (78.0/39.0/26.0 "m^-1"; 1.28/2.56/
     3.85 "cm") are ILLUSTRATIVE-ONLY -- a literal reuse of
     `sigma_max_shell`'s cell-normalized formula (SIGMA_MAX_BASE=0.5 and
     the base-78 denominator are FDTD grid-normalized constants, verified
     against `lab/fdtd2d.py`'s own "grid units (dx=1, c=1)" convention) fed
     meter-valued input with NO dx/unit bridge established anywhere in this
     program. NOT asserted as physically-grounded conductivities anywhere
     this cycle. See `physical_sigma_max_illustrative_only` below.
  3. [MATERIALS attack, adopted verbatim] Holding tau_shell constant under
     self-similar r-scaling is ORDINARY OPTICAL-DEPTH CONSERVATION --
     achievable via an independently-CHOSEN (different) conductivity/doping
     at each build size -- NOT evidence of "a conductivity that must shrink
     as the object grows, a property no real material has." The real
     realizability-relevant distinction: a self-similar construction needs
     a DIFFERENT recipe (re-engineered sigma) per target size; a
     fixed-absolute-thickness construction (item 4, still deferred) could
     in principle reuse ONE real material at any substrate size.
  4. [EM attack, Red-Team-hardened to a flat mandatory fix, LOAD-BEARING]
     Block B's headline-immunity argument is MULTIPLICATIVE, not additive.
     `veiled_contrast` is exactly linear in `C_measured`; scaling |C| from
     0.7209 to its physical ceiling 1.0 is a x1.3872 factor, giving
     8.14e-3 (PHOTONICS' own Iteration-24 closed-form figure, reproduced
     here) -- 61x/246x below MARGINAL/FAIL, NOT a "headroom of 0.28."
  5. [PHOTONICS attack, LOAD-BEARING] Block B's own deliverable is a
     PROPAGATOR RE-PARAMETERIZATION + MAGNITUDE CROSS-CHECK ONLY -- its
     findings are explicitly INCONCLUSIVE against live thread T24's own
     uncharacterized ABSORB=40 boundary systematic (0.002-0.007 absolute,
     same order of magnitude as this block's own predicted band), held
     fixed and uncorrected this cycle. No language anywhere in this
     experiment's Results claims this "closes" T21's contamination
     question.
  6. [QUANTUM attack, LOAD-BEARING] `_src_amp` (reused verbatim from
     exp-042) drives the FULL tapered aperture with a per-theta linear
     phase ramp -- the same "deliberately beamformed/focused synthetic
     array" construction exp-046/T21 already flagged as physically
     distinct from a naturally-divergent single-mode emitter. This block's
     numbers at the NEW geometry inherit that unresolved provenance
     question, not newly. Block C's own P-C2 regime-applicability check
     (below) is QUANTUM's own fold-in, not just a raw-number-proximity
     check.
  7. [new, Red Team attack 10] Block A's P-A2 is STRUCK as a "predicted
     outcome" -- MATERIALS' own charter tier call is solicited fresh at
     Phase 5, unprejudiced by this cycle's own (illustrative-only, per fix
     2) arithmetic. This memo entry carries forward Iteration 7's own
     INFORMAL UNOBTANIUM call as the cited prior tier, not a new tier
     derived here.

Non-mandatory, adopted anyway (THERMODYNAMICS' recommended addition, cheap
and correct): Block A's idealizations disclose that no existing THERMO
sidecar UNDETECTABLE verdict (exp-043/044/045) has been re-derived at these
newly-computed witness-scale PHYSICAL dimensions (cm-scale e-folding depth,
m-scale radius) -- `h_eff=k_air/L`'s quiescent-conduction-limit assumption
is unverified at that scale (real natural convection, not conduction-
limited, likely governs at meter scale).

See NOTES.md for the full Phase 1-5 accepted/overridden record and
LOGBOOK.md Iteration 25 for the verbatim panel transcript.
"""

import numpy as np

# ============================================================ Block A
# ------------------------------------------------- self-similar construction
# Reproduced from experiments/030-scale-bridge/design_geometry.py -- NOT
# imported (that module is keyed to cell-valued r; this module works in
# meters throughout, disclosed per mandatory fix 1).
SIGMA_MAX_BASE = 0.5              # exp-030's own r=78-cell bench value (code units)
R_BASE_CELLS = 78                 # exp-030's own bench outer radius (cells)
R_IN_BASE_FRAC = 30 / 78          # self-similar r_in/r_out ratio (dimensionless, scale-free)
TAU_SHELL = 24.0                  # exp-030's own held optical depth (code units, dimensionless)

WITNESS_R_M = (0.5, 1.0, 1.5)     # exp-030's own committed witness radii


def shell_thickness_m(r_w_m):
    """Continuous, scale-free geometric fact -- no unit bridge needed
    (a pure ratio of two lengths in the SAME unit)."""
    return r_w_m * (1.0 - R_IN_BASE_FRAC)


def core_radius_m(r_w_m):
    """CONTINUOUS evaluation of the self-similar ratio (mandatory fix 1) --
    NOT a call to exp-030's `r_in_shell`, whose round() is a cell-
    quantization step meaningless for a continuous meter-valued radius."""
    return r_w_m * R_IN_BASE_FRAC


def physical_sigma_max_illustrative_only(r_w_m):
    """ILLUSTRATIVE ONLY (mandatory fix 2). Literal reuse of exp-030's
    `sigma_max_shell(r) = SIGMA_MAX_BASE / (r/R_BASE_CELLS)` formula with
    r_w_m (a length in METERS) substituted for r (a length in CELLS) --
    the SAME arithmetic operation, no dx/unit conversion applied, because
    none has ever been established in this program (this bench's own FDTD
    convention is grid units, dx=1 -- lab/fdtd2d.py's own docstring).
    The numeric OUTPUT is reported for completeness (it is what "holding
    tau=24 under this formula, fed meters" produces) but is NOT to be read
    as a physical conductivity in m^-1, and no downstream reasoning in this
    experiment treats it as one."""
    return SIGMA_MAX_BASE / (r_w_m / R_BASE_CELLS)


def tau_check(r_w_m):
    """The one thing that IS scale-free and physically meaningful: the
    optical depth identity itself, verified to hold under the continuous
    formula (mandatory fix 1's own disclosure) regardless of any unit
    question -- tau = sigma_illustrative * thickness must equal 24.0
    exactly, by algebraic construction."""
    return physical_sigma_max_illustrative_only(r_w_m) * shell_thickness_m(r_w_m)


C_ANCHOR = -0.7209
C_ANCHOR_CITATION = "Iteration 7 close (exp-030), V-weighted, r=78 cells, +-35deg fallback"
PRIOR_TIER_CALL = "UNOBTANIUM (informal call, Iteration 7/exp-030 Phase 5, MATERIALS)"

# ============================================================ Block B
# ------------------------------------------------- exp-030's real r=78 domain
# Values below are `experiments/030-scale-bridge/design_geometry.py::GEOM[78]`,
# reproduced verbatim (verified by direct execution, Red Team attack 9 --
# a clean check, no defect found):
GEOM78 = dict(
    NY=1528, OBJ_Y=764, D_SP=223, GUARD_OUT=186,
    R_OUT=78, W_FLANK=78, PLANE_X=77, SRC_X=300,
    ABSORB=40, TAPER=40,
)

# exp-042's own hardcoded (OLD) geometry -- reproduced verbatim, used ONLY
# as the regression-anchor domain (proving the generalization below
# introduces no bug), never as this cycle's own reported result:
GEOM_EXP042_OLD = dict(
    NY=1584, OBJ_Y=792, D_SP=223, GUARD_OUT=185,
    R_OUT=78, W_FLANK=78, PLANE_X=77, SRC_X=300,
    ABSORB=40, TAPER=40,
)

CPL = {450: 15, 600: 20, 750: 25}
FALLBACK_ANGLES = (-35, -25, -15, -5, 0, 5, 15, 25, 35)     # exp-030/047's own N=9 set

GATE_HARD = 0.001                    # exp-024/041's own committed hard gate
GATE_PERCEPTUAL_CONTEXT = 0.005      # VISION's own T2 photopic C_thr bar (lab)


def aperture_profile(edge, y_lo, y_hi):
    """Bit-identical reproduction of `Sim.add_line_source`'s tapered
    top-hat array -- same formula as exp-042's own `aperture_profile`,
    parameterized instead of module-global."""
    n = y_hi - y_lo
    p = np.ones(n)
    win = 0.5 * (1.0 - np.cos(np.pi * np.arange(edge) / edge))
    p[:edge] = win
    p[-edge:] = win[::-1]
    return p


def _geom_derived(g):
    """Every quantity `field_and_h` needs, derived from one geometry dict --
    the generalization exp-042's own module never needed (single fixed
    geometry) but this cycle does (two geometries: OLD regression anchor,
    NEW exp-030 domain)."""
    y_lo = g["ABSORB"]
    y_hi = g["NY"] - g["ABSORB"]
    obj_y = g["OBJ_Y"]
    a = obj_y - y_lo
    d_sp = g["D_SP"]
    r_edge = float(np.hypot(d_sp, a))
    y_src = np.arange(y_lo, y_hi, dtype=float)
    y_obs = np.arange(y_lo, y_hi, dtype=float)
    dy = y_obs[:, None] - y_src[None, :]
    r = np.sqrt(d_sp ** 2 + dy ** 2)
    obliquity = d_sp / r
    p = aperture_profile(g["TAPER"], y_lo, y_hi)
    return dict(y_lo=y_lo, y_hi=y_hi, obj_y=obj_y, a=a, d_sp=d_sp, r_edge=r_edge,
                y_src=y_src, y_obs=y_obs, r=r, obliquity=obliquity, p=p)


def _src_amp(theta_deg, k, gd):
    """Exact reproduction of exp-042's own `_src_amp` -- taper amplitude x
    phase ramp, phase referenced to the aperture/object-window centre."""
    phase = k * np.sin(np.radians(theta_deg)) * (gd["y_src"] - gd["obj_y"])
    return gd["p"] * np.exp(1j * phase)


def field_and_h(theta_deg, lam_cells, g):
    """CORRECTED convention (exp-042 Phase-5 erratum, reused verbatim): E
    from the bare coherent sum, H from the obliquity-weighted coherent sum
    -- Faraday's law for this bench's actual line-current soft source.
    Parameterized on geometry dict `g` (mandatory-fix-1-disclosed
    generalization of exp-042's own module-global implementation)."""
    gd = _geom_derived(g)
    k = 2.0 * np.pi / lam_cells
    G0 = np.exp(1j * (k * gd["r"] - np.pi / 4)) / np.sqrt(gd["r"])
    amp = _src_amp(theta_deg, k, gd)
    E = G0 @ amp
    H = (G0 * gd["obliquity"]) @ amp
    return E, H, gd


def edge_diffraction_c_empty_corrected(theta_deg, lam_cells, g):
    """Predicted C_empty(theta,lambda) at geometry `g` -- reduced through
    `lab.ambient.window_means`/`weber` directly, same as exp-042."""
    from lab import ambient as amb
    E, H, gd = field_and_h(theta_deg, lam_cells, g)
    Sx = -np.real(E * np.conj(H))
    bo, bf = amb.window_means(Sx, gd["y_lo"], gd["obj_y"], g["R_OUT"],
                               g["GUARD_OUT"], g["W_FLANK"])
    return amb.weber(bo, bf)


def ripple_period_deg(a_cells, lam_cells, theta_deg=40.0):
    """EM's own Iteration-18/19-established fringe period,
    P(theta) = lambda / (A * cos(theta)) -- reused for Block B's own P-B1
    consistency check (predicted period at the NEW geometry's own A)."""
    return float(np.degrees(lam_cells / (a_cells * np.cos(np.radians(theta_deg)))))


# ============================================================ Block C
MARGINAL_LO, MARGINAL_HI = 0.5, 2.0          # lab/glare_sidecar.py::tier_w_verdict
T2_VERTICAL_LOG_UNCERTAINTY = 0.3            # LOGBOOK.md line ~1408 ("Scotopic scaling")
L_REF_CDM2 = 3.0                             # lab/glare_sidecar.py::C_THR_L_REF_CDM2 (photopic floor)


def log_band_ratio(log10_delta):
    return 10.0 ** log10_delta, 10.0 ** (-log10_delta)
