"""exp-035 design constants -- Closing the R156/N17_156 Domain x Quadrature
Factorial (T16 priority 1), Rebuilding N17_NATIVE by the RATIO=1.5 Method
(T16 priority 2), and Reconciling T15 with a Zero-Cost Desk Correction
(priority 3, corrected).
=============================================================================
Panel Iteration 12 (lead: QUANTUM OPTICS, rotation). Phase-3 synthesis
incorporates Red Team's PROCEED-WITH-MANDATORY-FIXES verdict -- see NOTES.md
for the complete accepted/overridden record and LOGBOOK.md Iteration 12 for
the verbatim Phase 1/2/3 transcript.

THREE blocks, none gating another's execution:

  Block T16_CLOSE     -- the missing cell of a domain x quadrature 2x2 at
                         r=156: N17 (17 angles, +-40deg) on exp-034's own
                         Block R156 domain (GUARD_OUT=336, NY=2480),
                         VERBATIM -- not rebuilt, not widened. Combined
                         with exp-034's own three already-published cells
                         (R156dom x N9, N17_156dom x N9, N17_156dom x N17),
                         this closes the 2x2 and tests whether the
                         disclosed domain effect (3.552e-4) and quadrature
                         effect (4.2485e-4) are additive or interact.
                         34 new FDTD calls (17 angles x 2 scenes).

  Block N17_NATIVE_V2 -- Red Team's own Iteration-11 mandatory-fix-5
                         geometry (r=78-physical at cpl=30, exp-033's own
                         domain), rebuilt CORRECTLY this cycle: every
                         geometry constant below is copied VERBATIM from
                         experiments/033-g600-resolution-check/design_geometry.py
                         (GUARD_OUT=278, NY=2376, PLANE_DX=22), NOT
                         recomputed via exp-034's own generic
                         `_coverage_geometry()` formula, which the
                         Director's own Iteration-11 Phase-4 catch showed
                         gives a DIFFERENT, non-matching domain
                         (GUARD_OUT=295) at the same nominal parameters.
                         34 new FDTD calls (17 angles x 2 scenes).

  Block T15_RECONCILE -- ZERO new FDTD calls. Desk-only reconciliation of
                         live thread T15 (g0's chord-model deficit),
                         corrected per Red Team's Phase-2 audit: the
                         cpl=40 comparator in the ORIGINAL Phase-1 proposal
                         (g0/A = 0.687124) was a copy/paste of the r=117
                         chord-model value, not a real measurement --
                         caught independently by PHOTONICS (Phase 2) and
                         Red Team (Phase 2, re-derived from first
                         principles). The corrected comparison uses RAW
                         g = |C|/tau at all three resolutions this
                         program has ever measured the OFF-state
                         calibration at (already-published numbers, zero
                         new cost), each against `chord_model_g0()`
                         evaluated at that resolution's own geometry.
                         Extended per THERMODYNAMICS' mandatory fix to also
                         report chord_absorptance()'s pi/4 peak-chord
                         amplitude against the same three chord-model
                         values -- the SECOND unreconciled amplitude pair
                         T15's own LOGBOOK text names ("two extinction
                         amplitudes... unreconciled in one committed
                         record").

MANDATORY FIXES applied here (Red Team, Panel Iteration 12 Phase 2 --
verdict PROCEED-WITH-MANDATORY-FIXES; full numbered attack list in
LOGBOOK.md Iteration 12 / NOTES.md Phase 3):
  1. [Red Team attack 2/3, PHOTONICS' original catch] The Phase-1 proposal's
     cpl=40 "measured g0/A" cell (0.687124) does not exist anywhere in the
     codebase -- `block_cpl40()` (exp-034) never computes a g0/A ratio, and
     the stated number is, to 7 significant figures, a copy of the r=117
     chord-model value from the adjacent table column. CORRECTED here:
     Block T15_RECONCILE uses RAW g=|C|/tau at cpl=20/30/40 (all three
     already published, zero new cost) instead of a nonexistent
     floor-corrected cpl=40 fit-intercept. Verified independently by this
     module's own self-check, below, before being trusted.
  2. [Red Team attack 4, new finding] `block_cpl40()` discards its signed
     C_empty (only stores abs()) and never persists per-angle scene
     arrays -- so a "correctly-signed C_empty(cpl=40)" fix, as originally
     specified in Phase 2, would require ~9 NEW FDTD calls, silently
     breaking Block T15_RECONCILE's zero-cost claim. NOT done here -- the
     raw-g fix (mandatory fix 1) is genuinely zero-cost and internally
     consistent, per Red Team's own specific recipe.
  3. [Red Team attack 5, THERMODYNAMICS' catch] `chord_absorptance()`'s
     pi/4 peak-chord amplitude (0.785398...) sits ~14% above every
     `chord_model_g0()` value -- LOGBOOK's own T15 entry already names this
     unreconciled pair. Added to Block T15_RECONCILE's report, zero cost
     (chord_absorptance is a pure function of tau; r_out cancels via
     sigma=tau/(2*r_out), so no new sidecar computation is needed for the
     off_pass articles reused in Blocks T16_CLOSE/N17_NATIVE_V2 either --
     THERMO's sidecar constants for tau_center=0.0065 carry forward
     UNCHANGED from exp-034, cited not recomputed).
  4. [Red Team attack 6, EM's catch, elevated to mandatory] Block T16_CLOSE
     runs N17 (+-40deg) for the FIRST time on R156's domain, which was
     built for +-35deg (exp-030's own `geometry()`) and has never been
     coverage-tested past that span -- unlike N17_156's domain, which was
     purpose-widened. This program's own precedent (exp-024, T7) shows a
     +-40deg-specific artifact that survives margin-widening and is NOT
     visible in an aggregate empty-scene gate that pools 17 angles. A
     per-angle empty-scene check at theta=+-40deg specifically -- computed
     from data already captured inside `block_n17()`'s own `scenes` dict,
     zero additional FDTD cost -- is now MANDATORY before P-A1's
     interaction verdict is trusted. Advisory threshold |C_empty(single
     angle)| <= 0.04 -- this program's own established bound for a SINGLE
     oblique angle (stage 9's own +-15deg empty window balance gate,
     0.019-0.021), the loosest precedented analog for a single off-axis
     reading; NOT a previously-validated N=1/+-40deg-specific gate, and
     flagged as such, not silently promoted to a hard pass/fail.
  5. [Red Team attack 7, MATERIALS' catch -- accepted as hygiene, not as a
     violated requirement] PLAN.md's Iteration-12 priority (3) names a
     literature check as the condition for escalating the realizability
     memo toward Checkpoint-2 -- a condition this cycle does not trigger
     (D_req and the irradiance gap are algebraically orthogonal to the
     ambient-contrast reading this cycle refines). Disclosure sentence
     added to NOTES.md: this cycle's T15 work does not substitute for that
     still-open literature check.
  6. [Red Team attack 8, VISION's catch -- REJECTED as specified (wrong
     cost premise: N9 is a zero-marginal-cost byproduct of the N17 run, not
     a separate 17-call leg -- swapping it for a genuine N33 leg would grow
     this cycle's budget +47%, not swap for free), substance partially
     accepted] NOTES.md states explicitly that N17 is still only the SECOND
     point of an eventual three-point (N9->N17->N33) angular-convergence
     sequence, not a converged endpoint -- N33 queued as Iteration-13's
     top-ranked item, not deferred uncredited.

Total new FDTD calls: 68 (34 + 34 + 0), unchanged from the Phase-1 proposal
-- every mandatory fix above is a zero/near-zero-marginal-FDTD-cost code or
analysis addition, per Red Team's own budget discipline (mirroring its own
Iteration-11 precedent of cutting scope growth rather than absorbing it).
"""

import math

import numpy as np

# =====================================================================
# shared angle sets -- copied VERBATIM from exp-034's own
# design_geometry.py (itself sourced from exp-024's ANGLES/N17_EXTRA)
# =====================================================================
FALLBACK_ANGLES = (-35, -25, -15, -5, 0, 5, 15, 25, 35)          # N=9
N17_PRIMARY = (-40, -30, -20, -10, 0, 10, 20, 30, 40)            # exp-024's own ANGLES
N17_EXTRA = (-35, -25, -15, -5, 5, 15, 25, 35)                   # exp-024's own N17_EXTRA
N17_ANGLES = tuple(sorted(set(N17_PRIMARY) | set(N17_EXTRA)))    # 17 angles, +-40deg, 5deg step
assert len(N17_ANGLES) == 17 and N17_ANGLES[0] == -40 and N17_ANGLES[-1] == 40
assert set(FALLBACK_ANGLES).issubset(set(N17_ANGLES))            # N9 is a strict subset of N17


# =====================================================================
# chord_model_g0 -- copied VERBATIM from experiments/034-floor-convergence-
# scale-bridge/design_geometry.py (itself a fresh rederivation of the
# precedented weak-absorption chord idiom in
# experiments/024-ambient-margin-adjudication/design_geometry.py's own
# `window_means(..., transmission=True)`). Reused, not modified.
# =====================================================================
def chord_model_g0(r_out, plane_dx, obj_x, src_x, angles_deg, absorb, taper,
                    guard_out, w_flank, tau_probe=1.0e-4):
    """Zero-free-parameter geometric (ray-chord) prediction of the linear
    ambient-contrast coefficient g0_geo = |C_geo(tau)|/tau in the tau->0
    limit. No FDTD, no fit -- pure ray optics through the disk at this
    geometry's own (r_out, plane_dx, lever, angle set)."""
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


def chord_absorptance(tau):
    """Copied verbatim from exp-034's own THERMO sidecar -- the pi/4
    peak-chord (theta=0) linear-absorption amplitude, a pure function of
    tau (r_out cancels via sigma=tau/(2*r_out))."""
    return (math.pi / 4.0) * tau * (1.0 - (4.0 / (3.0 * math.pi)) * tau)


TAU_OFF_PASS = 0.0065

# =====================================================================
# Block T16_CLOSE -- exp-034's own Block R156 domain, VERBATIM, N17 angles
# =====================================================================
T16_CLOSE = {}
T16_CLOSE["R_OUT"] = 156
T16_CLOSE["PLANE_DX"] = 15
T16_CLOSE["OBJ_X"] = 340
T16_CLOSE["SRC_X"] = 600
T16_CLOSE["NX"] = 660
T16_CLOSE["ABSORB"] = 40
T16_CLOSE["TAPER"] = 40
T16_CLOSE["PLANE_X"] = T16_CLOSE["OBJ_X"] - T16_CLOSE["R_OUT"] - T16_CLOSE["PLANE_DX"]   # 169
T16_CLOSE["GUARD_OUT"] = 336
T16_CLOSE["W_FLANK"] = T16_CLOSE["R_OUT"]
T16_CLOSE["FLANK"] = (336, 492)
T16_CLOSE["W_OBJ"] = T16_CLOSE["R_OUT"]
T16_CLOSE["NY"] = 2480
T16_CLOSE["OBJ"] = (T16_CLOSE["OBJ_X"], T16_CLOSE["NY"] // 2)          # (340, 1240)
T16_CLOSE["CPL"] = 20
T16_CLOSE["STEPS_AMBIENT"] = 2706          # reused verbatim from exp-034 Block R156
T16_CLOSE["N17_ANGLES"] = N17_ANGLES
T16_CLOSE["TAU_OFF_PASS"] = TAU_OFF_PASS
T16_CLOSE["SIGMA_OFF_PASS"] = TAU_OFF_PASS / (2 * T16_CLOSE["R_OUT"])   # 2.083333e-5
assert abs(2.0 * T16_CLOSE["SIGMA_OFF_PASS"] * T16_CLOSE["R_OUT"] - T16_CLOSE["TAU_OFF_PASS"]) < 1e-9
# self-check: reproduces exp-034's own R156 block geometry exactly
assert T16_CLOSE["GUARD_OUT"] == 336 and T16_CLOSE["FLANK"] == (336, 492) and T16_CLOSE["NY"] == 2480
assert T16_CLOSE["PLANE_X"] == 169

# established comparators (exp-034's own committed results.json, full precision)
T16_C_N9_R156DOM = -0.005759806872194646            # block_r156.C.off_pass
T16_C_N9_N17_156DOM = -0.005404596414491869          # block_n17_156.C_N9_from_this_domain
T16_C_N17_N17_156DOM = -0.00497974499443827          # block_n17_156.C_N17
T16_C_EMPTY_N17_156DOM = 0.0005496127931839956        # block_n17_156.C_empty_N17
T16_DOMAIN_EFFECT_AT_N9 = T16_C_N9_R156DOM - T16_C_N9_N17_156DOM        # -3.5521e-4
T16_QUADRATURE_EFFECT_ON_N17_156DOM = T16_C_N17_N17_156DOM - T16_C_N9_N17_156DOM  # +4.2485e-4
T16_ADDITIVE_PREDICTION_C_N17_R156DOM = T16_C_N9_R156DOM + T16_QUADRATURE_EFFECT_ON_N17_156DOM

# =====================================================================
# Block N17_NATIVE_V2 -- exp-033's own domain, VERBATIM (RATIO=1.5 method,
# NOT exp-034's ad-hoc `_coverage_geometry()`), N17 angles
# =====================================================================
N17_NATIVE_V2 = {}
N17_NATIVE_V2["RATIO"] = 1.5              # exp-033's own rescale of exp-032's native +-35 fallback
N17_NATIVE_V2["CPL_NATIVE"] = 20
N17_NATIVE_V2["CPL"] = 30
N17_NATIVE_V2["NX"] = 540
N17_NATIVE_V2["NY"] = 2376
N17_NATIVE_V2["ABSORB"] = 60
N17_NATIVE_V2["SRC_X"] = 450
N17_NATIVE_V2["TAPER"] = 60
N17_NATIVE_V2["R_OUT"] = 117               # 78 * 1.5, independently rounded (exp-033)
N17_NATIVE_V2["OBJ_X"] = 255
N17_NATIVE_V2["PLANE_DX"] = 22             # 15*1.5=22.5 -> 22, exp-033's own rounding
N17_NATIVE_V2["PLANE_X"] = N17_NATIVE_V2["OBJ_X"] - N17_NATIVE_V2["R_OUT"] - N17_NATIVE_V2["PLANE_DX"]  # 116
N17_NATIVE_V2["OBJ"] = (N17_NATIVE_V2["OBJ_X"], N17_NATIVE_V2["NY"] // 2)   # (255, 1188)
N17_NATIVE_V2["W_OBJ"] = 117
N17_NATIVE_V2["GUARD_OUT"] = 278           # 185*1.5=277.5 -> 278, exp-033's own rounding
N17_NATIVE_V2["W_FLANK"] = 117
N17_NATIVE_V2["FLANK"] = (278, 395)
N17_NATIVE_V2["STEPS_AMBIENT"] = 2100      # reused verbatim from exp-033 (settling-validated there)
N17_NATIVE_V2["N17_ANGLES"] = N17_ANGLES
N17_NATIVE_V2["TAU_OFF_PASS"] = TAU_OFF_PASS
N17_NATIVE_V2["SIGMA_OFF_PASS"] = TAU_OFF_PASS / (2 * N17_NATIVE_V2["R_OUT"])   # 2.777778e-5
assert abs(2.0 * N17_NATIVE_V2["SIGMA_OFF_PASS"] * N17_NATIVE_V2["R_OUT"] - N17_NATIVE_V2["TAU_OFF_PASS"]) < 1e-9
# self-check: reproduces exp-033's own committed domain exactly (NOT exp-034's ad-hoc 295/2272)
assert N17_NATIVE_V2["GUARD_OUT"] == 278 and N17_NATIVE_V2["FLANK"] == (278, 395) and N17_NATIVE_V2["NY"] == 2376
assert N17_NATIVE_V2["PLANE_X"] == 116

# established comparator (exp-033's own committed results.json, full precision)
N17_NATIVE_V2_ESTABLISHED_C = -0.004586460833023719     # exp-033 ambient_contrasts.off_pass.C
N17_NATIVE_V2_MARGIN = 0.005 - abs(N17_NATIVE_V2_ESTABLISHED_C)   # 4.1354e-4

# =====================================================================
# empty-scene coverage / decision-floor gate (aggregate, N17) -- reused
# verbatim from exp-034's own N17_COVERAGE_GATE. The PER-ANGLE +-40deg
# check (mandatory fix 4, EM) is a NEW, advisory-only bound -- see module
# docstring; not previously validated as an N=1/+-40deg-specific gate.
# =====================================================================
N17_COVERAGE_GATE = 0.005
PER_ANGLE_EMPTY_ADVISORY_BOUND = 0.04      # this program's own +-15deg single-angle
                                            # empty-window-balance precedent (stage 9),
                                            # the loosest established analog available

# =====================================================================
# Block T15_RECONCILE -- zero FDTD cost, corrected per mandatory fixes 1-3
# =====================================================================
# raw g = |C_off_pass|/tau at every resolution this program has ever
# measured the OFF-state calibration at (already-published, zero new cost)
T15_G_RAW = {
    20: 0.692743113607875,          # exp-032 results.json::g_values["off_pass/600"]
    30: 0.705609358926726,          # exp-033 results.json::g_raw["off_pass"]
    40: abs(-0.004601531803829529) / TAU_OFF_PASS,   # exp-034 results.json::block_cpl40.C_off_pass_cpl40
}

# chord-model geometries at each resolution (self-similar r=78/117/156 family)
T15_GEOM = {
    20: dict(r_out=78, plane_dx=15, obj_x=170, src_x=300, absorb=40, taper=40, guard_out=185, w_flank=78),
    30: dict(r_out=117, plane_dx=22, obj_x=255, src_x=450, absorb=60, taper=60, guard_out=278, w_flank=117),
    40: dict(r_out=156, plane_dx=30, obj_x=340, src_x=600, absorb=80, taper=80, guard_out=370, w_flank=156),
}

PI4_PEAK_CHORD_AMPLITUDE = math.pi / 4.0    # 0.7853981634 -- THERMO's chord_absorptance() leading coefficient

if __name__ == "__main__":
    print("exp-035 geometry (three blocks, 68 new FDTD calls total):\n")
    print(f"Block T16_CLOSE: NX={T16_CLOSE['NX']} NY={T16_CLOSE['NY']} R_OUT={T16_CLOSE['R_OUT']} "
          f"GUARD_OUT={T16_CLOSE['GUARD_OUT']} FLANK={T16_CLOSE['FLANK']} STEPS={T16_CLOSE['STEPS_AMBIENT']}")
    print(f"  existing cells: C(N9,R156dom)={T16_C_N9_R156DOM:+.6f}  C(N9,N17_156dom)={T16_C_N9_N17_156DOM:+.6f}  "
          f"C(N17,N17_156dom)={T16_C_N17_N17_156DOM:+.6f}")
    print(f"  domain effect (at N9) = {T16_DOMAIN_EFFECT_AT_N9:+.6e}  "
          f"quadrature effect (on N17_156dom) = {T16_QUADRATURE_EFFECT_ON_N17_156DOM:+.6e}")
    print(f"  additive prediction C(N17,R156dom) = {T16_ADDITIVE_PREDICTION_C_N17_R156DOM:+.6f}")
    print(f"\nBlock N17_NATIVE_V2: NX={N17_NATIVE_V2['NX']} NY={N17_NATIVE_V2['NY']} R_OUT={N17_NATIVE_V2['R_OUT']} "
          f"GUARD_OUT={N17_NATIVE_V2['GUARD_OUT']} FLANK={N17_NATIVE_V2['FLANK']} STEPS={N17_NATIVE_V2['STEPS_AMBIENT']}")
    print(f"  established C(N9)={N17_NATIVE_V2_ESTABLISHED_C:+.6f}  margin={N17_NATIVE_V2_MARGIN:.6e}")
    print(f"\nBlock T15_RECONCILE (0 new calls):")
    for cpl in (20, 30, 40):
        g0 = chord_model_g0(**T15_GEOM[cpl], angles_deg=FALLBACK_ANGLES)
        gap = (T15_G_RAW[cpl] - g0) / g0
        print(f"  cpl={cpl:2d}: g_raw={T15_G_RAW[cpl]:.6f}  chord_model_g0={g0:.6f}  gap={gap*100:+.3f}%")
    print(f"  pi/4 peak-chord amplitude = {PI4_PEAK_CHORD_AMPLITUDE:.6f}")
    print(f"\nrun counts: T16_CLOSE=17*2=34  N17_NATIVE_V2=17*2=34  T15_RECONCILE=0  TOTAL=68")
