"""exp-034 design constants -- The Paired Floor-Convergence / r=156
Scale-Bridge Cycle, with the off_pass/off_bracket Energy Sidecar Extended.
=============================================================================
Panel Iteration 11 (lead: THERMODYNAMICS, rotation). Phase-3 synthesis
incorporates Red Team's PROCEED-WITH-MANDATORY-FIXES verdict -- see NOTES.md
for the complete accepted/overridden record and LOGBOOK.md Iteration 11 for
the verbatim Phase 1/2/3 transcript.

FOUR blocks, none gating another's execution, reconciled only at Phase 5:

  Block CPL40    -- a third resolution point at native r=78 (physical size),
                    600nm, self-similar rescale RATIO=2.0 (cpl 20->40),
                    empty+off_pass only. Tests whether the empty-scene
                    decision floor and the actually-SCORED raw-C currency
                    are converging or diverging under refinement.

  Block R156     -- extends off_pass's PASS-boundary finding (exp-032) to
                    r=156 cells, exp-030's own r-family idiom (tau_center
                    held fixed, PLANE_DX fixed not self-similar). off_lab/
                    off_field REUSED verbatim from exp-030's own r=156
                    measurements; off_bracket/off_pass/empty are NEW.

  Block N17_156  -- a genuine 17-angle (5deg step, +-40deg span) angular-
                    quadrature convergence check on off_pass AT r=156, on
                    its own coverage-widened domain (NOT exp-030's +-35deg
                    domain -- rebuilt fresh to avoid a domain-size confound,
                    per this program's own T12 lesson).

  Block N17_NATIVE -- Red Team's own mandatory fix #5 (Panel Iteration 11
                    Phase 2): the SAME N9-vs-N17 quadrature check, but at
                    the geometry that actually backs the program's only-ever
                    constraint-3 PASS citation -- r=78 physical size at
                    cpl=30 (exp-033's own geometry), NOT r=156. VISION's
                    original Phase-2 attack found Block N17_156 (as
                    proposed) tests the wrong geometry; Red Team corrected
                    VISION's own cost estimate (~17-26 calls) upward to
                    ~34, matching Block N17_156's own domain-widening
                    discipline (rerun full N9 fresh on the re-derived
                    domain, do not mix old/new domain data).

DIRECTOR'S OWN CATCH (Phase 3, not raised by any Phase-2/Red-Team seat --
logged per house convention, flag don't silently fix): the N17 angle set
(ANGLES = (-40,-30,-20,-10,0,10,20,30,40), from
experiments/024-ambient-margin-adjudication/design_geometry.py) is EXACTLY
the "PRIMARY" +-40deg geometry that Panel Iteration 2 (exp-024) found failed
the delta_C<=0.001 gate at ALL SIX lambda/weighting combinations,
non-monotonically -- and margin-widening (MARGIN_MULT 2.0->3.5) was tested
and REFUTED as the fix; only DROPPING the +-40deg angles (the fallback,
+-35deg) resolved it. PLAN.md's own words: "localizing the real mechanism to
something angle-specific at +-40deg, not margin-ratio-driven." Neither N17
block in this cycle can assume that problem is margin-solved just because
this cycle's own coverage formula computes a wider NY than exp-024's
original failing geometry did -- exp-024's OWN MARGIN_MULT=3.5 test (a much
wider margin than the original failing geometry) ALSO failed. This is why
P-N17-1 (the empty-scene coverage/decision-floor gate) is load-bearing and
MUST be checked and reported honestly BEFORE any N9-vs-N17 comparison is
trusted, for BOTH N17 blocks -- a gate failure here is not a bug to route
around, it would be this program's second independent confirmation of a
real +-40deg-specific artifact, itself a finding worth having.

MANDATORY FIXES applied here (Red Team, Panel Iteration 11 Phase 2):
  1. [Red Team attack 1] Run-count bookkeeping guard: each block below
     defines its OWN scoped, block-local article tuple/sigma values --
     no shared module-wide ARTICLES tuple is imported across blocks. This
     forecloses the failure mode exp-033's own run.py exhibited (a shared
     multi-article harness silently running unused articles, corrected
     47->50 only at Phase-5 audit). n_new_runs per block is computed in
     run.py from the actual call sites, printed, and asserted against the
     table below before results are trusted.
  2. [Red Team attack 2, EM's flip parameter] Block R156's common-mode-vs-
     differential floor decomposition: ELECTROMAGNETISM's Phase-2 attack
     (g_corr's own construction subtracts C_empty per-geometry, so if the
     r=156-vs-r=78 shift in C_empty is common-mode across all four tau
     articles, the fit intercept A can land near-invariant almost
     regardless of whether real kappa-dependent wave physics exists -- the
     same trap as exp-033's own retired circular clause, laundered through
     a differently-shaped guarantee). Computed in run.py, reported BEFORE
     any SCALE-INVARIANT/DIVERGENT language is trusted.
  3. [Red Team attack 3, PHOTONICS/QUANTUM's flip parameter, corrected per
     Red Team attack 4's mechanism fix] A geometry-corrected chord-model
     null for P-R156-2's comparator -- PHOTONICS' Iteration-10 finding
     (T15) that g0 sits ~15% below its own window-integrated geometric
     chord model, stable across resolution, and is "specific to this
     bench's (PLANE_DX/lambda, W_OBJ/r_out) geometry, not a portable
     constant." Red Team's own correction to the Phase-2 attacks (this
     cycle's own attack 4): W_OBJ/r_out is an INVARIANT ratio (=1) across
     every geometry this program has ever built, including r=156 -- it
     cannot be the moving quantity; z/z_R is the correct, already-computed
     axis that genuinely differs (0.0123 at r=156 vs 0.0493 at r=78-native).
     The EXACT formula PHOTONICS/QUANTUM used at Iteration 10 to derive
     g0_geo=0.6981/0.814 is NOT preserved anywhere in this repo as
     reusable code (checked: absent from results.json, NOTES.md, and
     design_geometry.py of exp-033) -- it was a Phase-5 in-session
     derivation, never committed. Rather than guess at an unrecorded
     formula and risk misattributing a fabricated number to another seat,
     this cycle RE-DERIVES a geometric (ray-chord, zero-free-parameter)
     null from first principles, reusing the ALREADY-PRECEDENTED code path
     (experiments/024-ambient-margin-adjudication/design_geometry.py's own
     `window_means(..., transmission=True)`, the weak-absorption chord
     model already used for the original dilute-sponge calibration
     article) -- evaluated at each block's own actual (r_out, plane_dx,
     lever, d_sp) geometry via the tau->0 linear limit. This is flagged
     explicitly as a FRESH rederivation, not a reproduction of Iteration
     10's own unrecorded number -- cross-checked against the r=78/native
     citation (g0=0.6896) as a sanity bound, not asserted to match it
     exactly.
  4. [Red Team attack 2 elevated, MATERIALS' flip parameter] eps_r==1.0's
     restriction and its numeric consequence (a realizable condensed-phase
     host flips the ladder to FAIL and violates constraint 2) is restated
     inline at EVERY PASS/MARGINAL headline citation in NOTES.md, not just
     once in an idealizations section -- per Red Team's own elevation of
     this from "nice to have" to mandatory, flagging a FOURTH recurrence of
     this exact documentation gap across exp-031/032/033/034.
  5. [Red Team attack 5, mandatory fix 5 folded in as Block N17_NATIVE --
     see above] Director's budget call: fold in, not defer a 5th time.
  6. [Red Team attack 6/recommended] The lab/ build behind Block R156's
     fresh empty(156) is the SAME code as the one that produced exp-030's
     reused off_lab/off_field captures -- verified: `lab/` has had ZERO
     commits between exp-030 (Iteration 7) and this cycle (PLAN.md's own
     "No lab/ change" notes at exp-032/033 are unbroken; the trust suite
     is re-verified 46/46 green immediately before this cycle's own run,
     with no diff against exp-030's own suite state).
  7. [Red Team attack 7/recommended] P-CPL40-2's disposition bands closed
     (no unlabeled gap) -- see Predicted outcomes, NOTES.md.
"""

import math

import numpy as np

# =====================================================================
# shared helpers
# =====================================================================


def chord_model_g0(r_out, plane_dx, obj_x, src_x, angles_deg, absorb, taper,
                    guard_out, w_flank, tau_probe=1.0e-4):
    """Zero-free-parameter geometric (ray-chord) prediction of the linear
    ambient-contrast coefficient g0_geo = |C_geo(tau)|/tau in the tau->0
    limit, reusing the EXACT precedented weak-absorption chord idiom from
    experiments/024-ambient-margin-adjudication/design_geometry.py's own
    `window_means(..., transmission=True)` (originally built to predict
    the dilute-sponge calibration article's C to 0.001-0.003 of itself).
    No FDTD, no fit -- pure ray optics through the disk at this geometry's
    own (r_out, plane_dx, lever, angle set). Mandatory fix 3 (Red Team
    attack 3, corrected mechanism per attack 4) -- a FRESH rederivation,
    not a reproduction of Iteration 10's own unrecorded number."""
    lever = obj_x - (obj_x - r_out - plane_dx)   # = r_out + plane_dx
    y0 = 0.0  # relative coordinates; absolute y0 cancels in the Weber ratio
    ny_rel = int(4 * (guard_out + w_flank))       # generous relative span
    y = np.arange(-ny_rel // 2, ny_rel // 2, dtype=float)
    sigma_probe = tau_probe / (2.0 * r_out)
    b_obj, b_flank, wsum = 0.0, 0.0, 0.0
    for th in angles_deg:
        off = lever * math.tan(math.radians(th))
        yc = y - off
        inside = np.abs(yc) < r_out / math.cos(math.radians(th))
        chord = np.zeros_like(y)
        perp = yc * math.cos(math.radians(th))
        chord[inside] = 2.0 * np.sqrt(np.maximum(r_out ** 2 - perp[inside] ** 2, 0.0))
        b = np.exp(-sigma_probe * chord)
        obj_w = np.abs(y) <= r_out
        flank_w = (np.abs(y) >= guard_out) & (np.abs(y) <= guard_out + w_flank)
        b_obj += b[obj_w].mean()
        b_flank += b[flank_w].mean()
        wsum += 1.0
    b_obj /= wsum
    b_flank /= wsum
    c_geo = (b_obj - b_flank) / b_flank
    return abs(c_geo) / tau_probe


def _coverage_geometry(r_out, plane_dx, obj_x, src_x, absorb, taper,
                        span_deg, margin_mult=3.5, lam_max_cpl=25):
    """General +-span_deg coverage-margin geometry, generalizing
    experiments/030-scale-bridge/design_geometry.py::geometry()'s own
    tan(35deg)-embedded formula (there hardcoded to the fallback family) to
    an explicit span_deg parameter -- verified at import time (below) to
    reproduce exp-030's own r=156/+-35deg numbers EXACTLY (GUARD_OUT=336,
    FLANK=(336,492), NY=2480) before being trusted at +-40deg."""
    plane_x = obj_x - r_out - plane_dx
    d_sp = src_x - plane_x
    lever = r_out + plane_dx
    guard_out = int(np.ceil(lever * np.tan(np.radians(span_deg))
                             + r_out / np.cos(np.radians(span_deg)))) + 25
    flank = (guard_out, guard_out + r_out)
    const = flank[1] + taper + absorb + d_sp * np.tan(np.radians(span_deg))
    fringe = np.sqrt(lam_max_cpl * d_sp)
    rule = margin_mult * fringe
    ny = int(np.ceil(2 * (const + rule) / 8) * 8)
    return dict(plane_x=plane_x, d_sp=d_sp, lever=lever, guard_out=guard_out,
                flank=flank, ny=ny)


# self-check: reproduce exp-030's own established r=156/+-35deg geometry
# exactly, before this module's +-40deg formula is trusted for anything.
_check35 = _coverage_geometry(156, 15, 340, 600, 40, 40, 35.0)
assert _check35["guard_out"] == 336 and _check35["flank"] == (336, 492) and _check35["ny"] == 2480, \
    f"coverage-geometry formula does not reproduce exp-030's own r=156/+-35deg geometry: {_check35}"

FALLBACK_ANGLES = (-35, -25, -15, -5, 0, 5, 15, 25, 35)          # N=9
N17_PRIMARY = (-40, -30, -20, -10, 0, 10, 20, 30, 40)            # exp-024's own ANGLES
N17_EXTRA = (-35, -25, -15, -5, 5, 15, 25, 35)                   # exp-024's own N17_EXTRA
N17_ANGLES = tuple(sorted(set(N17_PRIMARY) | set(N17_EXTRA)))    # 17 angles, +-40deg, 5deg step
assert len(N17_ANGLES) == 17 and N17_ANGLES[0] == -40 and N17_ANGLES[-1] == 40
assert set(FALLBACK_ANGLES).issubset(set(N17_ANGLES))            # N9 is a strict subset of N17

# ===================================================== eps_r idealization
# Mandatory fix 4 (Red Team attack 2 elevated, MATERIALS): restated INLINE
# at every PASS/MARGINAL headline in NOTES.md, not just here.
EPS_R_IDEALIZATION_NOTE = (
    "g0 and every PASS/MARGINAL in this line are properties of an "
    "index-matched (eps_r == 1.0, n-1 <~ 1e-5) article -- a gas/aerosol "
    "host only. At a realizable condensed-phase index (n=1.33-1.5): "
    "two-surface ambient contrast C = -0.040 to -0.078 (VISION-ladder "
    "FAIL, independent of tau), specular return 143-571x the established "
    "camera floor (constraint-2 violation). NOT a material transfer "
    "function. (Fourth recurrence of this exact documentation gap across "
    "exp-031/032/033/034 -- Red Team elevated this to mandatory.)"
)

# =====================================================================
# Block CPL40 -- r=78 physical, self-similar RATIO=2.0 (cpl 20 -> 40)
# =====================================================================
CPL40 = {}
CPL40["RATIO"] = 2.0
CPL40["CPL"] = 40
CPL40["CPL_NATIVE"] = 20
CPL40["NX"] = 720
CPL40["NY"] = 3168
CPL40["ABSORB"] = 80
CPL40["SRC_X"] = 600
CPL40["TAPER"] = 80
CPL40["R_OUT"] = 156                       # 78 * 2.0, EXACT integer (no rounding)
CPL40["OBJ_X"] = 340
CPL40["PLANE_DX"] = 30                     # 15 * 2.0, EXACT (unlike exp-033's 22.5->22 drift)
CPL40["PLANE_X"] = CPL40["OBJ_X"] - CPL40["R_OUT"] - CPL40["PLANE_DX"]   # = 154
CPL40["OBJ"] = (CPL40["OBJ_X"], CPL40["NY"] // 2)                        # (340, 1584)
CPL40["GUARD_OUT"] = 370
CPL40["W_FLANK"] = CPL40["R_OUT"]
CPL40["FLANK"] = (CPL40["GUARD_OUT"], CPL40["GUARD_OUT"] + CPL40["W_FLANK"])  # (370, 526)
CPL40["W_OBJ"] = CPL40["R_OUT"]
CPL40["BOX_CLEARANCE"] = 24
CPL40["BOX"] = (CPL40["OBJ_X"] - CPL40["R_OUT"] - CPL40["BOX_CLEARANCE"],
                CPL40["OBJ_X"] + CPL40["R_OUT"] + CPL40["BOX_CLEARANCE"],
                CPL40["OBJ"][1] - CPL40["R_OUT"] - CPL40["BOX_CLEARANCE"],
                CPL40["OBJ"][1] + CPL40["R_OUT"] + CPL40["BOX_CLEARANCE"])
CPL40["FALLBACK_ANGLES"] = FALLBACK_ANGLES
CPL40["STEPS_AMBIENT"] = 2800               # 1400 * 2.0
CPL40["STEPS_SETTLING_CONTROL"] = 1400      # native, unchanged
CPL40["TAU_OFF_PASS"] = 0.0065
CPL40["SIGMA_OFF_PASS"] = CPL40["TAU_OFF_PASS"] / (2 * CPL40["R_OUT"])   # 2.08333e-5
CPL40["ARTICLES"] = ("off_pass",)
assert abs(2.0 * CPL40["SIGMA_OFF_PASS"] * CPL40["R_OUT"] - CPL40["TAU_OFF_PASS"]) < 1e-9

# self-similarity check (z/z_R match to r=78/cpl=20 native, exact per proposal)
_ZZR_NATIVE = CPL40["PLANE_DX"] / CPL40["CPL"] * CPL40["CPL_NATIVE"] / (2 * 78) \
    if False else None  # (not used -- z/z_R defined identically to exp-030's own convention below)


def z_over_zr(r_out, plane_dx, lam_cells):
    return plane_dx * lam_cells / (r_out ** 2)


CPL40["Z_OVER_ZR"] = z_over_zr(CPL40["R_OUT"], CPL40["PLANE_DX"], CPL40["CPL"])
_ZZR_78_NATIVE = z_over_zr(78, 15, 20)
assert abs(CPL40["Z_OVER_ZR"] - _ZZR_78_NATIVE) < 1e-9, \
    f"Block CPL40 self-similarity broken: {CPL40['Z_OVER_ZR']} vs native {_ZZR_78_NATIVE}"

# established anchors this block tests against (exp-032 native cpl=20, exp-033 cpl=30)
CPL40_ESTABLISHED = {
    "floor_cpl20": 3.3166e-5, "floor_cpl30": 1.165e-4,
    "C_off_pass_cpl20": -0.00450, "C_off_pass_cpl30": -0.0045865,
}

# =====================================================================
# Block R156 -- exp-030's own r-family idiom, tau_center held fixed
# =====================================================================
R156 = {}
R156["R_OUT"] = 156
R156["PLANE_DX"] = 15                       # FIXED, not self-similar (exp-030's own choice)
R156["OBJ_X"] = 340
R156["SRC_X"] = 600
R156["NX"] = 660
R156["ABSORB"] = 40
R156["TAPER"] = 40
R156["PLANE_X"] = R156["OBJ_X"] - R156["R_OUT"] - R156["PLANE_DX"]   # 169
R156["LEVER"] = R156["R_OUT"] + R156["PLANE_DX"]                    # 171
R156["D_SP"] = R156["SRC_X"] - R156["PLANE_X"]                      # 431
R156["GUARD_OUT"] = 336
R156["W_FLANK"] = R156["R_OUT"]
R156["FLANK"] = (336, 492)
R156["W_OBJ"] = R156["R_OUT"]
R156["NY"] = 2480
R156["OBJ"] = (R156["OBJ_X"], R156["NY"] // 2)                      # (340, 1240)
R156["BOX_CLEARANCE"] = 24
R156["BOX"] = (R156["OBJ_X"] - R156["R_OUT"] - R156["BOX_CLEARANCE"],
               R156["OBJ_X"] + R156["R_OUT"] + R156["BOX_CLEARANCE"],
               R156["OBJ"][1] - R156["R_OUT"] - R156["BOX_CLEARANCE"],
               R156["OBJ"][1] + R156["R_OUT"] + R156["BOX_CLEARANCE"])
R156["STEPS_AMBIENT"] = 2706
R156["FALLBACK_ANGLES"] = FALLBACK_ANGLES
R156["CPL"] = 20
R156["Z_OVER_ZR"] = z_over_zr(R156["R_OUT"], R156["PLANE_DX"], R156["CPL"])   # 0.012327

TAU_OFF_BRACKET = 0.003
TAU_OFF_PASS = 0.0065
TAU_OFF_LAB = 0.008
TAU_OFF_FIELD = 0.032

R156["TAU_OFF_BRACKET"] = TAU_OFF_BRACKET
R156["TAU_OFF_PASS"] = TAU_OFF_PASS
R156["SIGMA_OFF_BRACKET"] = TAU_OFF_BRACKET / (2 * R156["R_OUT"])   # 9.61538e-6
R156["SIGMA_OFF_PASS"] = TAU_OFF_PASS / (2 * R156["R_OUT"])         # 2.08333e-5
R156["NEW_ARTICLES"] = ("off_bracket", "off_pass")     # NEW this cycle
for _a, _t, _s in (("off_bracket", R156["TAU_OFF_BRACKET"], R156["SIGMA_OFF_BRACKET"]),
                    ("off_pass", R156["TAU_OFF_PASS"], R156["SIGMA_OFF_PASS"])):
    assert abs(2.0 * _s * R156["R_OUT"] - _t) < 1e-9

# off_lab/off_field REUSED VERBATIM from exp-030's own results.json
# (block1/156/profiles), zero marginal FDTD cost this cycle.
R156_REUSED_C = {
    "off_lab": -0.006805763564640212,
    "off_field": -0.023355358832853428,
}
R156_REUSED_C_EMPTY = -0.0012113954918918646     # exp-030's own fresh empty(156)
R156_REUSED_TAU = {"off_lab": TAU_OFF_LAB, "off_field": TAU_OFF_FIELD}

# established r=78/cpl=20 fit this block's dual-currency comparison uses
A78_ESTABLISHED = 0.689593
B78_ESTABLISHED = 0.299943
RESIDUAL_GATE_4ARTICLE = 3.0e-3          # reused verbatim from exp-033, same tau-grid
A_CONFIRMED_BAND = 0.015
A_ARTIFACT_BAND = 0.035

# =====================================================================
# Block N17_156 -- off_pass only, r=156, +-40deg (17 angles), fresh domain
# =====================================================================
N17_156 = {}
N17_156["R_OUT"] = 156
N17_156["PLANE_DX"] = 15
N17_156["OBJ_X"] = 340
N17_156["SRC_X"] = 600
N17_156["NX"] = 660
N17_156["ABSORB"] = 40
N17_156["TAPER"] = 40
_g156 = _coverage_geometry(156, 15, 340, 600, 40, 40, 40.0)
N17_156["PLANE_X"] = _g156["plane_x"]
N17_156["LEVER"] = _g156["lever"]
N17_156["D_SP"] = _g156["d_sp"]
N17_156["GUARD_OUT"] = _g156["guard_out"]          # 373
N17_156["FLANK"] = _g156["flank"]                  # (373, 529)
N17_156["W_FLANK"] = N17_156["R_OUT"]
N17_156["W_OBJ"] = N17_156["R_OUT"]
N17_156["NY"] = _g156["ny"]                        # 2672
N17_156["OBJ"] = (N17_156["OBJ_X"], N17_156["NY"] // 2)
N17_156["BOX_CLEARANCE"] = 24
N17_156["BOX"] = (N17_156["OBJ_X"] - N17_156["R_OUT"] - N17_156["BOX_CLEARANCE"],
                  N17_156["OBJ_X"] + N17_156["R_OUT"] + N17_156["BOX_CLEARANCE"],
                  N17_156["OBJ"][1] - N17_156["R_OUT"] - N17_156["BOX_CLEARANCE"],
                  N17_156["OBJ"][1] + N17_156["R_OUT"] + N17_156["BOX_CLEARANCE"])
N17_156["STEPS_AMBIENT"] = 2706          # unchanged -- depends on D_SP, not NY
N17_156["N17_ANGLES"] = N17_ANGLES
N17_156["TAU_OFF_PASS"] = TAU_OFF_PASS
N17_156["SIGMA_OFF_PASS"] = TAU_OFF_PASS / (2 * N17_156["R_OUT"])
assert abs(2.0 * N17_156["SIGMA_OFF_PASS"] * N17_156["R_OUT"] - N17_156["TAU_OFF_PASS"]) < 1e-9
assert N17_156["GUARD_OUT"] == 373 and N17_156["FLANK"] == (373, 529) and N17_156["NY"] == 2672

# =====================================================================
# Block N17_NATIVE -- Director's fold-in (Red Team mandatory fix 5):
# off_pass only, r=78-physical AT cpl=30 (exp-033's own geometry), +-40deg
# =====================================================================
N17_NATIVE = {}
N17_NATIVE["R_OUT"] = 117                  # exp-033's own R_OUT (78 * 1.5), cpl=30
N17_NATIVE["CPL"] = 30
N17_NATIVE["PLANE_DX"] = 22                # inherited from exp-033 UNCHANGED (not re-derived)
N17_NATIVE["OBJ_X"] = 255
N17_NATIVE["SRC_X"] = 450
N17_NATIVE["NX"] = 540
N17_NATIVE["ABSORB"] = 60
N17_NATIVE["TAPER"] = 60
_gnat = _coverage_geometry(117, 22, 255, 450, 60, 60, 40.0)
N17_NATIVE["PLANE_X"] = _gnat["plane_x"]           # 116, matches exp-033 exactly
N17_NATIVE["LEVER"] = _gnat["lever"]
N17_NATIVE["D_SP"] = _gnat["d_sp"]                 # 334, matches exp-033 exactly
N17_NATIVE["GUARD_OUT"] = _gnat["guard_out"]       # 295
N17_NATIVE["FLANK"] = _gnat["flank"]                # (295, 412)
N17_NATIVE["W_FLANK"] = N17_NATIVE["R_OUT"]
N17_NATIVE["W_OBJ"] = N17_NATIVE["R_OUT"]
N17_NATIVE["NY"] = _gnat["ny"]                      # 2272
N17_NATIVE["OBJ"] = (N17_NATIVE["OBJ_X"], N17_NATIVE["NY"] // 2)
N17_NATIVE["BOX_CLEARANCE"] = 18
N17_NATIVE["BOX"] = (N17_NATIVE["OBJ_X"] - N17_NATIVE["R_OUT"] - N17_NATIVE["BOX_CLEARANCE"],
                     N17_NATIVE["OBJ_X"] + N17_NATIVE["R_OUT"] + N17_NATIVE["BOX_CLEARANCE"],
                     N17_NATIVE["OBJ"][1] - N17_NATIVE["R_OUT"] - N17_NATIVE["BOX_CLEARANCE"],
                     N17_NATIVE["OBJ"][1] + N17_NATIVE["R_OUT"] + N17_NATIVE["BOX_CLEARANCE"])
N17_NATIVE["STEPS_AMBIENT"] = 2100         # unchanged from exp-033 -- D_SP unchanged
N17_NATIVE["N17_ANGLES"] = N17_ANGLES
N17_NATIVE["TAU_OFF_PASS"] = TAU_OFF_PASS
N17_NATIVE["SIGMA_OFF_PASS"] = TAU_OFF_PASS / (2 * N17_NATIVE["R_OUT"])   # matches exp-033's own value
assert abs(2.0 * N17_NATIVE["SIGMA_OFF_PASS"] * N17_NATIVE["R_OUT"] - N17_NATIVE["TAU_OFF_PASS"]) < 1e-9
assert N17_NATIVE["GUARD_OUT"] == 295 and N17_NATIVE["FLANK"] == (295, 412) and N17_NATIVE["NY"] == 2272

# established comparators for N17_NATIVE (exp-033's own N9/cpl=30 reading)
N17_NATIVE_ESTABLISHED_C = -0.0045865        # exp-033's off_pass C @cpl=30, N9 fallback
N17_NATIVE_MARGIN = 0.005 - abs(N17_NATIVE_ESTABLISHED_C)     # 4.135e-4
N5N9_INCREMENT_ESTABLISHED = 4.824e-4        # exp-032's own N5-vs-N9 increment, cpl=20

# =====================================================================
# empty-scene coverage / decision-floor gate threshold (Director's own
# catch, above) -- both N17 blocks must clear this BEFORE any N9-vs-N17
# comparison is trusted. Reused from this program's own suite-level
# absolute-identity bound (|C_empty| <= 0.005, stage 9), the tightest
# established bar for this exact quantity anywhere in this program.
# =====================================================================
N17_COVERAGE_GATE = 0.005

# =====================================================================
# THERMO sidecar (post-run analytic, expressibility contract) -- extended
# to off_lab/off_field this cycle (previously informal Phase-5 estimates).
# =====================================================================
NETD_BAND_K = (0.020, 0.050)   # exp-033's own implied microbolometer range


def chord_absorptance(tau):
    return (math.pi / 4.0) * tau * (1.0 - (4.0 / (3.0 * math.pi)) * tau)


THERMO_ABSORBED_FRACTION = {a: chord_absorptance(t) for a, t in
                            (("off_bracket", TAU_OFF_BRACKET), ("off_pass", TAU_OFF_PASS),
                             ("off_lab", TAU_OFF_LAB), ("off_field", TAU_OFF_FIELD))}
# scale the sidecar's off_pass steady-state dT (exp-033's own established
# 8.17e-4 K) linearly by absorbed-fraction ratio to get off_lab/off_field
_REF_ABS_FRAC_OFF_PASS = THERMO_ABSORBED_FRACTION["off_pass"]
_REF_DT_OFF_PASS_K = 8.17e-4
THERMO_DT_STEADY_K = {a: _REF_DT_OFF_PASS_K * (THERMO_ABSORBED_FRACTION[a] / _REF_ABS_FRAC_OFF_PASS)
                       for a in THERMO_ABSORBED_FRACTION}

# ------------------------------------------------------------- mandatory
# fix 6 (Red Team, Phase-5 audit, attack 7): restore the transient dwell-
# limited DeltaT machinery exp-033 built and this cycle's own first draft
# silently dropped (a real regression, caught by no Phase-1-4 seat). exp-
# 033's own published off_pass_transient_dT_K_by_dwell_s = {0.1: 6.9e-5,
# 0.5: 3.46e-4, 1.0: 6.92e-4} is EXACTLY linear in dwell time (rate =
# 6.92e-4 K/s to 3 sig figs at every point) -- a separate, simpler linear-
# heating model from the steady-state (radiative-equilibrium) estimate,
# not its short-time limit. Extended here to off_bracket/off_lab/off_field
# by the SAME absorbed-fraction-ratio scaling already used for
# THERMO_DT_STEADY_K, verified below to reproduce exp-033's own off_pass
# numbers to their own printed precision before being trusted for the
# other three articles.
# =====================================================================
_REF_TRANSIENT_RATE_OFF_PASS_K_PER_S = 6.92e-4    # exp-033's own established rate
THERMO_TRANSIENT_RATE_K_PER_S = {
    a: _REF_TRANSIENT_RATE_OFF_PASS_K_PER_S * (THERMO_ABSORBED_FRACTION[a] / _REF_ABS_FRAC_OFF_PASS)
    for a in THERMO_ABSORBED_FRACTION}
DWELL_TIMES_S = (0.1, 0.5, 1.0)
THERMO_TRANSIENT_DT_K_BY_DWELL = {
    a: {str(t): THERMO_TRANSIENT_RATE_K_PER_S[a] * t for t in DWELL_TIMES_S}
    for a in THERMO_ABSORBED_FRACTION}
_check_off_pass_transient = THERMO_TRANSIENT_DT_K_BY_DWELL["off_pass"]
assert abs(_check_off_pass_transient["0.1"] - 6.9e-5) < 1e-6, _check_off_pass_transient
assert abs(_check_off_pass_transient["0.5"] - 3.46e-4) < 1e-6, _check_off_pass_transient
assert abs(_check_off_pass_transient["1.0"] - 6.92e-4) < 1e-6, _check_off_pass_transient

# ---------------------------------------------------------------- erratum
# (Panel Iteration 12, exp-035 Phase 5, THERMODYNAMICS' catch + Red Team's
# independent confirmation and mandatory fix): the note below was
# originally HAND-TYPED ("5.9-49.8x" steady-state) and wrong -- the true
# steady-state range, recomputed directly from THERMO_DT_STEADY_K and
# NETD_BAND_K, is ~5.0-132.4x (off_bracket's true high end, 132.4x, was
# silently dropped from the stated range; the stated "5.9" actually matched
# the TRANSIENT off_field low end, not any steady-state ratio -- apparent
# cross-contamination between the two clauses at authoring time). Does NOT
# change the UNDETECTABLE conclusion (the true minimum, ~5.0x steady /
# ~5.9x transient, is still comfortably sub-threshold). Per house
# convention this experiment's own NOTES.md/results.json prose from its
# original run is left uncorrected as the historical record; this LIVE
# CODE fix (computed from source values, not hand-typed, so it cannot
# drift silently again) is what every future cycle actually imports and
# cites -- including exp-035 itself, which carried this note forward by
# citation before the bug was caught.
_steady_ratios = [netd / dt for dt in THERMO_DT_STEADY_K.values() for netd in NETD_BAND_K]
_transient_1s_ratios = [netd / THERMO_TRANSIENT_DT_K_BY_DWELL[a]["1.0"]
                         for a in THERMO_TRANSIENT_DT_K_BY_DWELL for netd in NETD_BAND_K]

OFF_STATE_DETECTABILITY_NOTE = (
    "UNDETECTABLE at every dwell tested, every article -- steady-state DeltaT "
    "is {:.1f}-{:.1f}x below the {:.3f}-{:.3f}K NETD band (off_field the "
    "closest, off_bracket furthest); transient (dwell-limited, 1.0s) DeltaT is "
    "SMALLER still at every article (linear-heating regime, has not caught up "
    "to steady state) -- {:.1f}-{:.1f}x below NETD at 1.0s. The phenomenon is a "
    "SWEPT beam (constraint 4): transient dwell-limited DeltaT is the "
    "physically apt number, not steady-state. (Computed from source values, "
    "not hand-typed -- corrected Iteration 12 per THERMODYNAMICS'/Red Team's "
    "Phase-5 catch of a hand-typed transcription error in the original range; "
    "see this module's erratum comment, above.)"
).format(min(_steady_ratios), max(_steady_ratios), NETD_BAND_K[0], NETD_BAND_K[1],
         min(_transient_1s_ratios), max(_transient_1s_ratios))


if __name__ == "__main__":
    print("exp-034 geometry (four independent blocks):\n")
    print(f"Block CPL40: NX={CPL40['NX']} NY={CPL40['NY']} R_OUT={CPL40['R_OUT']} "
          f"PLANE_DX={CPL40['PLANE_DX']} OBJ={CPL40['OBJ']} STEPS={CPL40['STEPS_AMBIENT']} "
          f"z/zR={CPL40['Z_OVER_ZR']:.6f} (native check: {_ZZR_78_NATIVE:.6f})")
    print(f"Block R156:  NX={R156['NX']} NY={R156['NY']} R_OUT={R156['R_OUT']} "
          f"PLANE_DX={R156['PLANE_DX']} OBJ={R156['OBJ']} STEPS={R156['STEPS_AMBIENT']} "
          f"z/zR={R156['Z_OVER_ZR']:.6f}")
    print(f"Block N17_156:   NX={N17_156['NX']} NY={N17_156['NY']} GUARD_OUT={N17_156['GUARD_OUT']} "
          f"FLANK={N17_156['FLANK']} STEPS={N17_156['STEPS_AMBIENT']}")
    print(f"Block N17_NATIVE: NX={N17_NATIVE['NX']} NY={N17_NATIVE['NY']} GUARD_OUT={N17_NATIVE['GUARD_OUT']} "
          f"FLANK={N17_NATIVE['FLANK']} STEPS={N17_NATIVE['STEPS_AMBIENT']}")
    print(f"\nrun counts: CPL40=9*2+2=20  R156=9*3=27  N17_156=17*2=34  N17_NATIVE=17*2=34  "
          f"TOTAL=115")
    print(f"\nsigma pins: CPL40 off_pass={CPL40['SIGMA_OFF_PASS']:.6e}  "
          f"R156 off_pass={R156['SIGMA_OFF_PASS']:.6e}  off_bracket={R156['SIGMA_OFF_BRACKET']:.6e}  "
          f"N17_156 off_pass={N17_156['SIGMA_OFF_PASS']:.6e}  N17_NATIVE off_pass={N17_NATIVE['SIGMA_OFF_PASS']:.6e}")
    print(f"\nTHERMO sidecar absorbed fractions: {THERMO_ABSORBED_FRACTION}")
    print(f"THERMO sidecar steady dT (K): {THERMO_DT_STEADY_K}")
