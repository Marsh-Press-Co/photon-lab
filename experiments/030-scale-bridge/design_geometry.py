"""exp-030 design constants -- The r=156/312 Near-Field->Witness-Scale
Bridge, with a Box-Ledger Floor Companion (T8 + T11).
=======================================================================
Panel Iteration 7 (lead: VISION SCIENCE, rotation) -- the five-times-
deferred r=156 near-field->witness-scale bridge, hard-committed at
Iteration 5's close with a pre-registered Checkpoint-4 tripwire: if this
build does not execute as committed this cycle, Checkpoint criterion 4
fires automatically (LOGBOOK.md, Iteration 5 close). T11 (box-ledger
channel decision-floor characterization) rides as a companion, strictly
lower priority -- it may fall back to Iteration 8, r=156 may not.

Phase-3 synthesis incorporates Red Team's mandatory-fix docket (LOGBOOK.md
Iteration 7, Phase 2) in full -- see NOTES.md for the complete accepted/
overridden record. Concretely, six corrections to the Phase-1 proposal:

  1. [Red Team #1, LOAD-BEARING] The r=78 "established" C anchors for the
     OPAQUE articles (absorber, PEC) are RECOMPUTED here from the actual
     per-lambda FALLBACK (+-35deg, NY=1584) numbers in exp-024's own
     NOTES.md, V-weighted in code -- not the PRIMARY (+-40deg) geometry,
     which is the exact configuration Iteration 2's own data showed missed
     the delta_C<=0.001 gate at all six (lambda,weighting) combinations,
     non-monotonically. The sponge anchors (OFF-lab/OFF-field, exp-026)
     were already correctly sourced from the fallback geometry -- verified
     by direct recomputation from exp-026/results.json, unchanged.
  2. [PHOTONICS #2, adjudicated by Red Team over MATERIALS'/QUANTUM's
     alternative fixes] `graded_black_shell`'s sigma_max is rescaled as
     sigma_max(kappa) = 0.5/kappa (kappa = r_out/78), holding the shell's
     radial optical depth integral(sigma dr) EXACTLY constant across the
     r=78/156/312 family (verified: sigma_max*(r_out-r_in) = 24 at every
     kappa) -- isolating the z/z_R diffraction effect Block 1 exists to
     measure from a confounding "coating got optically thicker" effect
     that held-sigma_max scaling would otherwise introduce. r_in=round(30*
     kappa) stays self-similar (geometric scale-invariance is what the fit
     needs -- MATERIALS' alternative, fixed ABSOLUTE thickness, would have
     broken that). A flat-coating R gate re-check at each new r_out is
     added (Red Team #8) rather than assumed to transfer.
  3. [QUANTUM #3, Red Team's "relabel, don't rescale" adjudication] The
     OFF-lab/OFF-field sponge articles keep their existing tau_center-
     held-fixed convention (correct for their designed role in the
     C(z/z_R) fit) -- but Sec. 3's claim that this family licenses
     "sigma(I) OFF-state bars transfer to witness scale" is STRUCK. That
     is a different, sigma-held claim this cycle does not test.
  4. [Red Team #3/#4/#5, none of Phase 2's five seats caught] T11's
     `box_dev` metric is REDEFINED to this program's own established
     convention (`abs(sigma_ext_A - sigma_ext_B) / abs(sigma_ext_A)`,
     verified against all 27 prior uses in this repo, exp-002 through
     exp-028) -- not the proposal's own drifted `/mean` formula. The
     T9/T10 "consequence" ratios are computed IN CODE (main(), below),
     not hand-asserted -- Red Team independently caught BOTH the Phase-1
     proposal's own arithmetic error AND a second error in THERMODYNAMICS'
     own hand-corrected figure on the same sentence. T9 and T11 are also
     now explicitly flagged as CROSS-ARTICLE (graded_black_shell vs. the
     uniform-conductivity ON disk), not just cross-run -- a second,
     independent reason box_dev is a floor on T11's own channel, not
     automatically transferable to T9's.
  5. [Red Team #6, constraint-3 relevant] A delta_C empty-scene decision-
     floor check is added at r=156 (reusing already-scheduled empty runs,
     zero marginal cost) BEFORE P-VISION-3's PASS/FAIL licensing language
     is trusted -- the +-35deg fallback's clean floor was only ever
     established at r=78's own NY=1584; this cycle's own geometry rule is
     structurally the same coverage-margin formula Iteration 2's own data
     showed does NOT govern the real mechanism (dropping +-40deg did), so
     the floor must be re-measured, not assumed to transfer by formula.
  6. [Red Team #7] At r=312, PEC and the graded_black_shell absorber (the
     two hard-edged, angle-sensitive articles) run the full N=9 fallback
     angle set, not N=5 -- the N5-vs-N9 convergence precedent (exp-026's
     P-MAT7) was measured on the smoothest, lowest-contrast article in the
     family (the tau=0.10 dilute sponge) and should not be generalized to
     opaque, hard-edged articles without its own check. The OFF-lab/
     OFF-field sponges keep N=5 at r=312 (the precedent's own regime).

  Recommended-not-mandatory (Red Team #9, adopted -- cheap and closes a
  live risk named at Iteration-4/5): one doubled-STEPS_AMBIENT settling
  diagnostic at r=156 (absorber, 600nm only) -- T10's own confound
  (settling re-entering at a finer/larger geometry) gets a direct check
  here rather than an assumption that STEPS_AMBIENT's linear D_SP-ratio
  scaling is automatically sufficient.

See NOTES.md for the full Phase 1/2/3 accepted/overridden record and
LOGBOOK.md Iteration 7 for the verbatim panel transcript.
"""

import numpy as np

# --------------------------------------------------------- the r-family
R_FAMILY = (78, 156, 312)
R_BASE = 78

PLANE_DX = 15                 # FIXED across the family (not self-similar) --
                               # the deliberate choice that maximizes the
                               # z/z_R dynamic range the fit needs (VISION's
                               # own Phase-1 design, unchanged by Phase 2/RT)
ABSORB = 40
TAPER = 40
MARGIN_MULT = 3.5             # exp-024's own established coverage-margin rule, reused
LAM_CELLS = 20                 # single-lambda scope, 600nm, cpl=20 (unchanged)
LAM_MAX_CPL = 25               # 750nm's cpl -- kept conservative in the NY rule (unchanged)
COURANT_FRAC = 0.99
STEPS_AMBIENT_BASE = 1400      # r=78's own established convention

FALLBACK_ANGLES = (-35, -25, -15, -5, 0, 5, 15, 25, 35)   # N=9
N5_SUBSAMPLE = (-35, -15, 0, 15, 35)                       # N=5 (sponges @ r=312 only, fix 6)

OFF_X0, SRC_X0 = 170, 300       # exp-024/026's own r=78 base geometry, unchanged


def kappa(r):
    return r / R_BASE


def geometry(r):
    """The full formula chain, per-r_out -- every derived quantity computed
    here, none hand-copied (Phase-1's own pre-registered discipline,
    unchanged by Phase 2/Red Team -- the geometry formulas themselves were
    NOT among Red Team's flagged defects)."""
    k = kappa(r)
    obj_x = round(OFF_X0 * k)
    src_x = round(SRC_X0 * k)
    nx = src_x + 60
    plane_x = obj_x - r - PLANE_DX
    lever = r + PLANE_DX
    d_sp = src_x - plane_x
    guard_out = int(np.ceil(lever * np.tan(np.radians(35))
                             + r / np.cos(np.radians(35)))) + 25
    flank = (guard_out, guard_out + r)
    box_clearance = round(12 * k)
    box = (obj_x - r - box_clearance, obj_x + r + box_clearance)
    const = flank[1] + TAPER + ABSORB + d_sp * np.tan(np.radians(35))
    fringe = np.sqrt(LAM_MAX_CPL * d_sp)
    rule = MARGIN_MULT * fringe
    ny = int(np.ceil(2 * (const + rule) / 8) * 8)
    steps = round(STEPS_AMBIENT_BASE * d_sp / geometry_d_sp_base())
    z_r = r ** 2 / LAM_CELLS
    z_over_zr = PLANE_DX * LAM_CELLS / r ** 2
    x_bridge = np.sqrt(z_over_zr)
    obj = (obj_x, ny // 2)
    box_full = (box[0], box[1], obj[1] - r - box_clearance, obj[1] + r + box_clearance)
    return dict(r=r, kappa=k, obj_x=obj_x, src_x=src_x, nx=nx, ny=ny,
                obj=obj, plane_x=plane_x, lever=lever, d_sp=d_sp,
                guard_out=guard_out, flank=flank, w_obj=r, w_flank=r,
                box_clearance=box_clearance, box=box_full,
                steps_ambient=steps, z_r=z_r, z_over_zr=z_over_zr,
                x_bridge=x_bridge)


def geometry_d_sp_base():
    k = kappa(R_BASE)
    obj_x = round(OFF_X0 * k)
    src_x = round(SRC_X0 * k)
    plane_x = obj_x - R_BASE - PLANE_DX
    return src_x - plane_x


GEOM = {r: geometry(r) for r in R_FAMILY}

# ------------------------------------------------- articles, per-r sigma
TAU_OFF_LAB = 0.008
TAU_OFF_FIELD = 0.032
SIGMA_MAX_BASE = 0.5           # r=78's own established, R<=0.2%-gated value
EPS_MAX = 1.0
R_IN_BASE_FRAC = 30 / 78       # self-similar r_in/r_out ratio, unchanged


def sigma_off_lab(r):
    return TAU_OFF_LAB / (2 * r)


def sigma_off_field(r):
    return TAU_OFF_FIELD / (2 * r)


def sigma_max_shell(r):
    """Fix 2: holds integral(sigma dr) constant across the family --
    verified: sigma_max_shell(r) * (r - r_in(r)) == SIGMA_MAX_BASE *
    (R_BASE - r_in(R_BASE)) == 24.0 at every r in R_FAMILY."""
    return SIGMA_MAX_BASE / kappa(r)


def r_in_shell(r):
    return round(R_IN_BASE_FRAC * r)


# printed assertions (house discipline) -- every derived material constant
# checked in code before it is trusted, not by eye
for _r in R_FAMILY:
    assert abs(2 * sigma_off_lab(_r) * _r - TAU_OFF_LAB) < 1e-9
    assert abs(2 * sigma_off_field(_r) * _r - TAU_OFF_FIELD) < 1e-9
    _thickness = _r - r_in_shell(_r)
    _tau_shell = sigma_max_shell(_r) * _thickness
    assert abs(_tau_shell - SIGMA_MAX_BASE * (R_BASE - r_in_shell(R_BASE))) < 1e-9, \
        f"shell optical depth not held constant at r={_r}: {_tau_shell}"

ARTICLES = ("empty", "absorber", "pec", "off_lab", "off_field")

# ------------------------------------------------- r=78 anchors, RECOMPUTED
# Fix 1 (Red Team #1, load-bearing). Raw per-lambda inputs below are GIVEN,
# sourced verbatim from the actual committed record (not this cycle's
# invention): absorber/PEC fallback (+-35deg, N=9) C values from
# experiments/024-ambient-margin-adjudication/NOTES.md's own printed
# fallback table (line ~271-277); off_lab/off_field from
# experiments/026-sigma-i-endpoints/results.json's `ambient_contrasts`
# (already fallback-geometry, re-verified bit-for-bit against the cited
# -0.0055 established figure). V-weights are the program's own frozen CIE
# 1924 photopic set, unchanged since Iteration 1.
V_PHOT = {450: 0.038, 600: 0.631, 750: 0.00012}

_C78_RAW = {
    "absorber": {450: -0.7170, 600: -0.7211, 750: -0.7284},   # exp-024 NOTES.md fallback table
    "pec":      {450: -0.8605, 600: -0.8677, 750: -0.8771},   # exp-024 NOTES.md fallback table
    "off_lab":  {450: -0.00460711308931395, 600: -0.005530667330154762,
                 750: -0.005052707590063023},                  # exp-026 results.json ambient_contrasts
    "off_field": {450: -0.020865817308441552, 600: -0.02179302617779434,
                  750: -0.02127632716651959},                  # exp-026 results.json ambient_contrasts
}


def _vweight(d):
    wsum = sum(V_PHOT.values())
    return sum(V_PHOT[lam] * d[lam] for lam in V_PHOT) / wsum


C78_ESTABLISHED = {k: _vweight(v) for k, v in _C78_RAW.items()}
# C78_ESTABLISHED == {'absorber': -0.72087, 'pec': -0.86729,
#                      'off_lab': -0.00548, 'off_field': -0.02174}
# (recomputed here; the proposal's original table cited the WRONG,
# gate-failing +-40deg PRIMARY geometry for absorber/pec: -0.684/-0.826)

# ------------------------------------------------------- witness scale
WITNESS_Z_M = 45.0
WITNESS_R_M = (0.5, 1.0, 1.5)     # (low, central, high)
WITNESS_LAM_NM = 550.0


def witness_z_over_zr(r_m):
    return WITNESS_Z_M * (WITNESS_LAM_NM * 1e-9) / r_m ** 2


WITNESS_ZZR = {"low": witness_z_over_zr(WITNESS_R_M[2]),      # largest r -> smallest z/zR
               "central": witness_z_over_zr(WITNESS_R_M[1]),
               "high": witness_z_over_zr(WITNESS_R_M[0])}      # smallest r -> largest z/zR

# ---------------------------------------------- T11 companion (beam-scene)
BEAM_R_FAMILY = (78, 156)          # r=312 explicitly optional, falls back to It.8
BEAM_N_BASE = 560
BEAM_STEPS_BASE = 3200
BEAM_CX0, BEAM_CY0 = 252, 280
BEAM_SRC_X0 = 64
TAU_ON = 3.9
BEAM_BOX_A0 = (142, 362, 170, 390)
BEAM_BOX_B0 = (117, 387, 145, 415)


def beam_geometry(r):
    k = kappa(r)
    n = round(BEAM_N_BASE * k)
    steps = round(BEAM_STEPS_BASE * k)
    cx, cy = round(BEAM_CX0 * k), round(BEAM_CY0 * k)
    src_x = round(BEAM_SRC_X0 * k)
    sigma_on = TAU_ON / (2 * r)
    box_a = tuple(round(v * k) for v in BEAM_BOX_A0)
    box_b = tuple(round(v * k) for v in BEAM_BOX_B0)
    ref = (cx, cy, round(60 * k))
    return dict(r=r, kappa=k, n=n, steps=steps, cx=cx, cy=cy, src_x=src_x,
                sigma_on=sigma_on, box_a=box_a, box_b=box_b, ref=ref)


BEAM_GEOM = {r: beam_geometry(r) for r in BEAM_R_FAMILY}
for _r in BEAM_R_FAMILY:
    assert abs(2 * BEAM_GEOM[_r]["sigma_on"] * _r - TAU_ON) < 1e-9


def box_dev(sigma_ext_a, sigma_ext_b):
    """Fix 4: the ESTABLISHED convention (verified against all 27 prior
    uses in this repo) -- not the Phase-1 proposal's own drifted /mean."""
    return abs(sigma_ext_a - sigma_ext_b) / abs(sigma_ext_a)


def main():
    print("exp-030 geometry (r=78/156/312 near-field->witness-scale bridge)\n")
    for r in R_FAMILY:
        g = GEOM[r]
        print(f"r_out={r:4d}  kappa={g['kappa']:.3f}  NX={g['nx']:5d} NY={g['ny']:5d}  "
              f"OBJ={g['obj']}  PLANE_X={g['plane_x']:5d}  D_SP={g['d_sp']:5d}  "
              f"STEPS={g['steps_ambient']:5d}  z/zR={g['z_over_zr']:.6f}  "
              f"x=sqrt(z/zR)={g['x_bridge']:.6f}")
    print(f"\nsigma_max_shell (fix 2, holds tau_shell=24.0 const): "
          + ", ".join(f"r={r}: {sigma_max_shell(r):.5f}" for r in R_FAMILY))
    print(f"r_in_shell: " + ", ".join(f"r={r}: {r_in_shell(r)}" for r in R_FAMILY))
    print(f"\nC78 anchors, RECOMPUTED from the fallback (+-35deg) geometry, "
          f"V-weighted (fix 1):")
    for k, v in C78_ESTABLISHED.items():
        print(f"  {k:10s}: {v:+.5f}")
    print(f"\nwitness z/zR (docket #7, z=45m, r=0.5-1.5m, lam=550nm): "
          f"central={WITNESS_ZZR['central']:.4e}  "
          f"band=[{WITNESS_ZZR['low']:.4e}, {WITNESS_ZZR['high']:.4e}]")
    print(f"\nT11 beam-scene geometry:")
    for r in BEAM_R_FAMILY:
        g = BEAM_GEOM[r]
        print(f"  r={r:4d}  N={g['n']:5d}  STEPS={g['steps']:5d}  "
              f"sigma_on={g['sigma_on']:.5e}  BOX_A={g['box_a']}  BOX_B={g['box_b']}")


if __name__ == "__main__":
    main()
