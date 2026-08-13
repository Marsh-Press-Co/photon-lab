"""exp-027 design constants -- Settling, Spread, and the PEC Ablation.
=======================================================================
Panel Iteration 4 (lead: ELECTROMAGNETISM). Phase-3 synthesis incorporates
all seven of Red Team's mandatory fixes (LOGBOOK.md Iteration 4, Phase 2):

  1. Block 3 Cell B's interior fill uses a STRICT inequality (rr < r_in,
     not rr <= r_in) to avoid double-writing sigma at the 12 lattice
     points sitting exactly on the shell's own inclusive inner boundary
     (MATERIALS' verified catch, confirmed independently by Red Team).
  2. Block 1 (settling-time diagnostic) extended to ALL THREE wavelengths,
     not just the 450/750nm flanks -- lambda=600nm is P-MAT4's actual
     anomaly PEAK (2.97%, vs 2.34%/1.86% at the flanks); a pure
     settling-completeness bias predicts a MONOTONIC residual (post-ramp
     periods fall 45.3->33.2->26.0 across the sweep), so the flanks alone
     can't test the one point the mechanism narrative most needs to
     explain (PHOTONICS' catch, independently re-derived by Red Team).
  3. Block 2's outcome partition explicitly names T7/P-EST (the ambient
     channel's own established hard-edge chromatic finding, Delta=0.0114/
     0.0166) as a live alternative to settling -- see NOTES.md Predictions.
  4. Block 2's box/annulus/behind-window geometry is REDERIVED BY FORMULA
     here (not hand-typed) from the native beam-scene box definitions,
     so nothing goes stale at the new per-lambda cell counts -- the
     printed BLOCK2_GEOM table below is the pinned design calculation
     Red Team's attack #4 demanded.
  5. Block 3's P-EM4 outcome partition gets a fourth, exhaustive branch:
     "outside [0.46,0.68] -- unpredicted, no PEC/rim attribution claimed."
  6. Block 3 reports raw P_abs/I_inc per cell (free -- widths() already
     returns sigma_abs and i_inc) plus a one-line THERMO analytic caveat
     per cell; the full DeltaT/emission-band/detectability sidecar is
     explicitly (re-)deferred to docket #7, per exp-026's own precedent
     Iteration 4 had let lapse.
  7. QUANTUM's bridge-gate package (queue item d) and VISION's r=156
     scale-bridge check (queue item c) are explicitly named and
     re-deferred with stated reasons in NOTES.md Phase 3 -- not silently
     dropped a third/second time.

See NOTES.md for the full accepted/overridden record.
"""

import numpy as np

# --------------------------------------------------- beam-scene bench (inherited verbatim)
# exp-001/002/026's exact domain -- zero changes to the native geometry.
BEAM_N = 560
BEAM_ABSORB = 40
BEAM_FRAC = 0.32
BEAM_CX, BEAM_CY = 252, 280
BEAM_SRC_X, BEAM_OBS_X = 64, 78
R_OUT = 78
BEAM_SWEEP = ((15, 450), (20, 600), (25, 750))    # native cpl per lambda, exp-001/002 convention
BEAM_STEPS_NATIVE = 3200
BEAM_STEPS_EXTENDED = 6400                        # Block 1: doubled, all 3 lambda (fix 2)

BEAM_BOX_A = (142, 362, 170, 390)                 # exp-002's box pair, unchanged
BEAM_BOX_B = (117, 387, 145, 415)
BEAM_REF = (BEAM_CX, BEAM_CY, 60)
_bx = np.arange(BEAM_N)[:, None]
_by = np.arange(BEAM_N)[None, :]
_brr = np.hypot(_bx - BEAM_CX, _by - BEAM_CY)
BEAM_ANNULUS = (_brr >= R_OUT + 10) & (_brr <= R_OUT + 70)
BEAM_BEHIND = (slice(BEAM_CX + R_OUT + 15, BEAM_CX + R_OUT + 115),
              slice(BEAM_CY - 20, BEAM_CY + 20))

SIGMA_ON = 3.9 / (2 * R_OUT)                      # exp-026's exact ON article, tau_center=3.9

# established anchors this experiment is scored against
ESTABLISHED_BEAM_BEHIND_3200 = {450: 0.0234, 600: 0.0297, 750: 0.0186}   # exp-026 @3200 steps
ESTABLISHED_BEAM_BEHIND_FLAT_TARGET = float(np.exp(-3.9))                # = 0.02024 (Beer-Lambert)
ESTABLISHED_ABS_EXT = {"graded_black_shell_600nm": (0.512, 0.515),       # exp-002, PEC-cored
                       "coreless_on_disk_3lambda": (0.6056, 0.6083)}     # exp-026, no PEC
# T7's ambient-channel hard-edge chromatic silhouette drift (established, exp-024/025) --
# scale comparison for attack #3's T7-vs-settling disambiguation (NOT the same channel,
# used only as a magnitude yardstick per NOTES.md Predictions).
T7_AMBIENT_CHROMATIC_DELTA = {"absorber": 0.0114, "pec": 0.0166}

# --------------------------------------------------- Block 1 -- settling-time diagnostic
# ON article, geometry/cpl UNCHANGED at every lambda; only BEAM_STEPS doubles.
# 3 lambda x (empty + on) = 6 new sim calls.
BLOCK1_SWEEP = BEAM_SWEEP

# --------------------------------------------------- Block 2 -- R3 spatial companion
# cpl x1.5 per lambda (exp-025's own resolution-check precedent), BEAM_STEPS held at
# the NATIVE 3200 (unchanged) -- physical (nm) size held fixed by rescaling every
# cell-based constant by the same per-lambda ratio r and rounding.
BLOCK2_RATIO = {450: 22 / 15, 600: 30 / 20, 750: 38 / 25}
BLOCK2_CPL = {450: 22, 600: 30, 750: 38}

# Native BOX_A/BOX_B, ANNULUS and BEHIND expressed as offsets from (CX,CY)/R_OUT --
# derived once, here, from the hardcoded native tuples above (checked: BOX_A is a
# square of half-width R_OUT+32, BOX_B a square of half-width R_OUT+57, both centered
# on (BEAM_CX,BEAM_CY); ANNULUS is [R_OUT+10, R_OUT+70]; BEHIND is
# [R_OUT+15, R_OUT+115] x [-20,+20] from center).
assert BEAM_BOX_A == (BEAM_CX - (R_OUT + 32), BEAM_CX + (R_OUT + 32),
                      BEAM_CY - (R_OUT + 32), BEAM_CY + (R_OUT + 32))
assert BEAM_BOX_B == (BEAM_CX - (R_OUT + 57), BEAM_CX + (R_OUT + 57),
                      BEAM_CY - (R_OUT + 57), BEAM_CY + (R_OUT + 57))
_BOX_A_HW_OFFSET = 32     # BOX_A half-width = R_OUT + 32
_BOX_B_HW_OFFSET = 57     # BOX_B half-width = R_OUT + 57
_ANNULUS_LO_OFFSET = 10   # ANNULUS = [R_OUT+10, R_OUT+70]
_ANNULUS_HI_OFFSET = 70
_BEHIND_X_LO_OFFSET = 15  # BEHIND = [R_OUT+15, R_OUT+115] x [-20,+20]
_BEHIND_X_HI_OFFSET = 115
_BEHIND_Y_HALF = 20


def _rr(x):
    return int(round(x))


def _block2_geom(lam_nm, ratio):
    """Rescale every cell-based constant by `ratio`, rounding independently
    (the same per-constant-rounding discipline exp-025 used), holding
    physical (nm) size fixed. This is the pinned design calculation Red
    Team's attack #4 required -- run this module directly to print it."""
    n = _rr(BEAM_N * ratio)
    cx = _rr(BEAM_CX * ratio)
    cy = _rr(BEAM_CY * ratio)
    r_out = _rr(R_OUT * ratio)
    src_x = _rr(BEAM_SRC_X * ratio)
    obs_x = _rr(BEAM_OBS_X * ratio)
    absorb = _rr(BEAM_ABSORB * ratio)
    hw_a = _rr(r_out + _BOX_A_HW_OFFSET * ratio)
    hw_b = _rr(r_out + _BOX_B_HW_OFFSET * ratio)
    box_a = (cx - hw_a, cx + hw_a, cy - hw_a, cy + hw_a)
    box_b = (cx - hw_b, cx + hw_b, cy - hw_b, cy + hw_b)
    ann_lo = r_out + _rr(_ANNULUS_LO_OFFSET * ratio)
    ann_hi = r_out + _rr(_ANNULUS_HI_OFFSET * ratio)
    beh_x0 = cx + r_out + _rr(_BEHIND_X_LO_OFFSET * ratio)
    beh_x1 = cx + r_out + _rr(_BEHIND_X_HI_OFFSET * ratio)
    beh_yh = _rr(_BEHIND_Y_HALF * ratio)
    return dict(lambda_nm=lam_nm, cpl=BLOCK2_CPL[lam_nm], ratio=ratio,
               n=n, cx=cx, cy=cy, r_out=r_out, src_x=src_x, obs_x=obs_x,
               absorb=absorb, box_a=box_a, box_b=box_b,
               annulus=(ann_lo, ann_hi),
               behind=(beh_x0, beh_x1, cy - beh_yh, cy + beh_yh))


BLOCK2_GEOM = {lam: _block2_geom(lam, r) for lam, r in BLOCK2_RATIO.items()}

# --------------------------------------------------- Block 3 -- PEC-ablation factorial
# Single lambda=600nm, native domain/cpl=20/BEAM_STEPS=3200, unchanged.
BLOCK3_R_CORE = 30       # exp-001/002's R_CORE
BLOCK3_R_OUT = R_OUT     # 78, exp-001/002's R_COAT
BLOCK3_SHELL_SIGMA_MAX = 0.5
BLOCK3_SHELL_EPS_MAX = 1.0
BLOCK3_ON_SIGMA = 0.025  # exp-026's exact ON-article construction (uniform, abrupt edge)

# Red Team attack #5: exhaustive 4-way outcome partition for P-EM4 (see NOTES.md) --
# bands stated there, not here; this module only carries geometry/material constants.


if __name__ == "__main__":
    print("exp-027 geometry -- Panel Iteration 4 (Settling, Spread, PEC Ablation)")
    print(f"\nBeam-scene bench (inherited verbatim): N={BEAM_N}, CX,CY=({BEAM_CX},{BEAM_CY}), "
          f"R_OUT={R_OUT}, SRC_X={BEAM_SRC_X}, OBS_X={BEAM_OBS_X}")
    print(f"established beam-behind @3200 steps: {ESTABLISHED_BEAM_BEHIND_3200} "
          f"(flat Beer-Lambert target: {ESTABLISHED_BEAM_BEHIND_FLAT_TARGET:.5f})")
    print(f"established sigma_abs/sigma_ext anchors: {ESTABLISHED_ABS_EXT}")
    print(f"T7 ambient chromatic deltas (yardstick only): {T7_AMBIENT_CHROMATIC_DELTA}")

    print("\nBlock 1 (settling-time diagnostic, ALL 3 lambda, fix 2):")
    for cpl, nm in BLOCK1_SWEEP:
        print(f"  {nm}nm cpl={cpl}: BEAM_STEPS {BEAM_STEPS_NATIVE} -> {BEAM_STEPS_EXTENDED}")

    print("\nBlock 2 (R3 spatial companion, cpl x1.5, pinned design calculation -- fix 4):")
    for lam_nm, g in BLOCK2_GEOM.items():
        print(f"  {lam_nm}nm: cpl={g['cpl']} ratio={g['ratio']:.4f} N={g['n']} "
              f"CX,CY=({g['cx']},{g['cy']}) R_OUT={g['r_out']} SRC_X={g['src_x']} "
              f"OBS_X={g['obs_x']} ABSORB={g['absorb']}")
        print(f"         BOX_A={g['box_a']} BOX_B={g['box_b']} "
              f"ANNULUS={g['annulus']} BEHIND={g['behind']}")

    print("\nBlock 3 (PEC-ablation factorial, lambda=600nm, native cpl=20):")
    print(f"  R_CORE={BLOCK3_R_CORE} R_OUT={BLOCK3_R_OUT} "
          f"shell sigma_max={BLOCK3_SHELL_SIGMA_MAX} eps_max={BLOCK3_SHELL_EPS_MAX} "
          f"ON sigma={BLOCK3_ON_SIGMA}")
    print("  Cell A: pec_disk(r=30) + graded_black_shell(30,78)  [PEC core]")
    print("  Cell B: graded_black_shell(30,78) + sigma_e[rr<30]+=0.5  [no PEC, fix 1: strict <]")
    print("  Cell C: uniform sigma_e[rr<=78]+=0.025  [no PEC, exp-026's exact ON article]")
