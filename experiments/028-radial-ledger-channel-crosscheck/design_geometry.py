"""exp-028 design constants -- The Radial Ledger and the Channel Cross-Check.
==============================================================================
Panel Iteration 5 (lead: THERMODYNAMICS, rotation). Phase-3 synthesis
incorporates Red Team's mandatory-fix docket (LOGBOOK.md Iteration 5,
Phase 2) in full:

  1. [MATERIALS/Red Team #1, LOAD-BEARING] Block A's SIGMA is rescaled PER
     LAMBDA so the ON article's optical depth is held at exactly the
     established tau_center=3.9 at every wavelength -- the Phase-1
     proposal's verbatim reuse of exp-027's `block2_one()` call pattern
     inherited a real bug: exp-027's own SIGMA_ON is a single module
     constant (3.9/(2*78), native R_OUT) applied unchanged to Block 2's
     PER-LAMBDA-RESCALED r_out (114/117/119 cells), silently drifting
     tau_center to 5.70/5.85/5.95 across the sweep -- NOT 3.9. This bug is
     already baked into exp-027's OWN PUBLISHED Block 2 numbers (the T10
     finding currently in LOGBOOK.md) -- see LOGBOOK.md's T10 erratum,
     added this shift, independent of whether this experiment runs.
  2. [PHOTONICS/Red Team #2] P-THERMO-B3's stated direction (Joule
     dissipation "skewing toward the outer boundary") is BACKWARDS --
     `graded_black_shell`'s own conductivity law peaks at the INNER
     boundary (r=r_in) and is zero at r=r_out. Corrected below.
  3. [EM/Red Team #3] "Absolute Poynting-theorem closure identity" language
     is corrected to "empirical closure gate (<=1.5%, calibrated stage 10)"
     -- reserved "absolute identity" strictly for Cell A's r<R_CORE=0 hard
     zero. A cpl x1.5 resolution companion is ADDED on Cell B (this
     program's own R3 meta-rule: any surprising first-run near-field
     spatial reading earns a resolution check before a mechanism debate).
  4. [QUANTUM/Red Team #4] The joint-injection diagnostic is NOT added this
     cycle (it would open its own gated suite stage, a real build cost,
     not "near-zero marginal cost" -- Red Team's ruling). Instead: honestly
     re-deferred as the bridge-gate package's FOURTH deferral (not framed
     as "not a repeated tautology"), committed as QUANTUM's own mandatory
     Iteration-6 lead-cycle build (next in rotation).
  5. [Red Team #5] The box-ledger channel's own missing decision-floor
     characterization is carried explicitly into Predictions (not just
     Idealizations): P-THERMO-A1/A2/A3 and P-THERMO-B1/B2 verdicts are
     informally suggestive, not floor-gated verdicts.
  6. [VISION/Red Team #6] r=156 scale-bridge check: NOT folded in as an
     unreviewed ad hoc Block C this cycle (the panel's independence
     mechanics -- blind Phase-2 critique before a design runs -- are the
     product; the Director designing a new instrument for VISION's own
     domain without a Phase-1/Phase-2 cycle would violate that). Instead:
     committed HARD as VISION's own mandatory Iteration-7 lead-cycle build
     (her next natural rotation slot), not a soft "should."
  7. [Red Team #7] The QUANTUM rider's language is corrected from "applied
     for the first time... not a third silent deferral" to an honest
     characterization: field names established, not yet exercised on a
     non-trivial value.

See NOTES.md for the full accepted/overridden record and LOGBOOK.md
Iteration 5 for the verbatim Phase 1/2/3 record.
"""

import numpy as np

# --------------------------------------------------- shared beam-scene bench (inherited verbatim)
# exp-001/002/026/027's exact native domain -- zero changes.
BEAM_N = 560
BEAM_ABSORB = 40
BEAM_FRAC = 0.32
BEAM_CX, BEAM_CY = 252, 280
BEAM_SRC_X, BEAM_OBS_X = 64, 78
R_OUT = 78
BEAM_STEPS_NATIVE = 3200
TAU_ON = 3.9  # established ON-article optical depth (exp-026)

BEAM_BOX_A = (142, 362, 170, 390)   # exp-002's box pair, unchanged
BEAM_BOX_B = (117, 387, 145, 415)
BEAM_REF = (BEAM_CX, BEAM_CY, 60)

# established anchors this experiment cross-checks against
ESTABLISHED_BEAM_BEHIND_3200 = {450: 0.0234, 600: 0.0297, 750: 0.0186}    # exp-026 @3200 steps
ESTABLISHED_BLOCK2_BEAM_BEHIND_BUGGY = {450: 0.010867, 600: 0.015956, 750: 0.003193}  # exp-027's
    # PUBLISHED Block-2 numbers -- computed with the UNRESCALED SIGMA_ON bug (see erratum,
    # LOGBOOK.md T10). Carried here as a labeled comparison point ONLY -- not an established
    # anchor this experiment's own (corrected) Block A is scored against.
ESTABLISHED_ABS_EXT = {"graded_black_shell_600nm": (0.512, 0.515),        # exp-002, PEC-cored
                       "coreless_on_disk_3lambda": (0.6056, 0.6083)}      # exp-026, no PEC


def _rr(x):
    return int(round(x))


def _rescaled_geom(ratio, cpl):
    """Rescale every cell-based constant by `ratio`, rounding independently
    -- exp-027's own `_block2_geom` formula, reused verbatim (fix 1 keeps
    the geometry rescale; only SIGMA was missing it)."""
    n = _rr(BEAM_N * ratio)
    cx = _rr(BEAM_CX * ratio)
    cy = _rr(BEAM_CY * ratio)
    r_out = _rr(R_OUT * ratio)
    src_x = _rr(BEAM_SRC_X * ratio)
    obs_x = _rr(BEAM_OBS_X * ratio)
    absorb = _rr(BEAM_ABSORB * ratio)
    hw_a = _rr(r_out + 32 * ratio)
    hw_b = _rr(r_out + 57 * ratio)
    box_a = (cx - hw_a, cx + hw_a, cy - hw_a, cy + hw_a)
    box_b = (cx - hw_b, cx + hw_b, cy - hw_b, cy + hw_b)
    ann_lo = r_out + _rr(10 * ratio)
    ann_hi = r_out + _rr(70 * ratio)
    beh_x0 = cx + r_out + _rr(15 * ratio)
    beh_x1 = cx + r_out + _rr(115 * ratio)
    beh_yh = _rr(20 * ratio)
    ref_hh = _rr(60 * ratio)
    return dict(cpl=cpl, ratio=ratio, n=n, cx=cx, cy=cy, r_out=r_out,
               src_x=src_x, obs_x=obs_x, absorb=absorb,
               box_a=box_a, box_b=box_b, annulus=(ann_lo, ann_hi),
               behind=(beh_x0, beh_x1, cy - beh_yh, cy + beh_yh),
               ref=(cx, cy, ref_hh),
               # fix 1: SIGMA rescaled so tau_center = 2*sigma*r_out = TAU_ON exactly,
               # at THIS r_out (not the native R_OUT=78) -- the load-bearing correction.
               sigma_on=TAU_ON / (2.0 * r_out))


# --------------------------------------------------- Block A -- T10 box-ledger cross-check (FIXED)
# exp-027's own Block 2 rescaled-cpl geometries, reused verbatim (bit-for-bit identical
# N/CX,CY/R_OUT/SRC_X/ABSORB/BOX_A/BOX_B/ANNULUS/BEHIND to exp-027's own printed table) --
# ONLY sigma_on is now correctly rescaled per lambda (fix 1).
BLOCKA_RATIO = {450: 22 / 15, 600: 30 / 20, 750: 38 / 25}
BLOCKA_CPL = {450: 22, 600: 30, 750: 38}
BLOCKA_GEOM = {lam: _rescaled_geom(r, BLOCKA_CPL[lam]) for lam, r in BLOCKA_RATIO.items()}

# --------------------------------------------------- Block B -- radial-binned absorbed-power ledger
# Native geometry (exp-027's own Block-3 bench, unchanged): lambda=600nm, cpl=20.
BLOCKB_R_CORE = 30
BLOCKB_R_OUT = R_OUT   # 78
BLOCKB_SHELL_SIGMA_MAX = 0.5
BLOCKB_SHELL_EPS_MAX = 1.0
BLOCKB_N_BINS = 26

# fix 3: EM's cpl x1.5 resolution companion on Cell B, at lambda=600nm -- this is
# EXACTLY exp-027's own BLOCK2_GEOM[600] point (same ratio=1.5, same formula), reused.
BLOCKB_COMPANION_RATIO = 1.5
BLOCKB_COMPANION_CPL = 30
BLOCKB_COMPANION_GEOM = _rescaled_geom(BLOCKB_COMPANION_RATIO, BLOCKB_COMPANION_CPL)
BLOCKB_COMPANION_R_CORE = _rr(BLOCKB_R_CORE * BLOCKB_COMPANION_RATIO)   # 45


if __name__ == "__main__":
    print("exp-028 geometry -- Panel Iteration 5 (Radial Ledger + Channel Cross-Check)")
    print(f"\nBlock A (T10 cross-check, SIGMA rescaled per lambda -- fix 1):")
    for lam, g in BLOCKA_GEOM.items():
        tau_check = 2.0 * g["sigma_on"] * g["r_out"]
        print(f"  {lam}nm: cpl={g['cpl']} ratio={g['ratio']:.4f} N={g['n']} "
              f"CX,CY=({g['cx']},{g['cy']}) R_OUT={g['r_out']} SIGMA_ON={g['sigma_on']:.6f} "
              f"tau_center_check={tau_check:.4f} (target {TAU_ON})")
        assert abs(tau_check - TAU_ON) < 1e-9, "tau_center rescale failed"
    print(f"\nBlock B (radial ledger, native): R_CORE={BLOCKB_R_CORE} R_OUT={BLOCKB_R_OUT} "
          f"cpl=20 lambda=600nm shell sigma_max={BLOCKB_SHELL_SIGMA_MAX}")
    print(f"Block B companion (fix 3, cpl x1.5 on Cell B): cpl={BLOCKB_COMPANION_CPL} "
          f"N={BLOCKB_COMPANION_GEOM['n']} R_OUT={BLOCKB_COMPANION_GEOM['r_out']} "
          f"R_CORE={BLOCKB_COMPANION_R_CORE}")
    print(f"\n[labeled comparison only] exp-027's PUBLISHED (buggy-sigma) Block 2 beam-behind: "
          f"{ESTABLISHED_BLOCK2_BEAM_BEHIND_BUGGY}")
