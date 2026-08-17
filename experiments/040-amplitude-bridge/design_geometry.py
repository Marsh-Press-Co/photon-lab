"""exp-040 design constants -- The Amplitude Bridge (Panel Iteration 17).

Self-contained (lab convention: each experiment directory stands alone).
Block V's geometry is INHERITED VERBATIM from exp-026's own +-35deg fallback
(dx=30nm fixed across the 3-lambda sweep -- CPL varies, cell geometry does
not). Block R's geometry is INHERITED VERBATIM from exp-033's own x1.5
resolution-check rescale (R_OUT=117, cpl=30) -- copied, not cross-imported,
per this lab's own convention (exp-026/027/etc. all do the same).

sigma is NEVER copied as a bare number across a block boundary (Red Team's
Panel-Iteration-17 attack #2, load-bearing): every sigma below is derived
from ITS OWN block's r_out via `lab.amplitude_bridge.sigma_from_tau`, with
an explicit assert recovering the target tau_center to <1e-9.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from lab import amplitude_bridge as ab

# --------------------------------------------------- Block V geometry (exp-026 verbatim)
V_NX = 360
V_NY = 1584
V_ABSORB = 40
V_CPL = {450: 15, 600: 20}         # 450nm added this cycle (Red Team fix L12); 750nm deferred
V_SRC_X = 300
V_TAPER = 40
V_R_OUT = 78
V_OBJ_X = 170
V_PLANE_DX = 15
V_PLANE_X = V_OBJ_X - V_R_OUT - V_PLANE_DX      # 77
V_OBJ = (V_OBJ_X, V_NY // 2)                    # (170, 792)
V_ANGLES = (-35, -25, -15, -5, 0, 5, 15, 25, 35)  # N=9 fallback, unchanged
V_W_OBJ = 78
V_GUARD_OUT = 185
V_W_FLANK = 78
V_STEPS_AMBIENT = 1400

# T2's two Tier-W night-lab decision bars (moonless-anchor L=1.7e-4 cd/m^2),
# inverted through the SATURATING chord model (not the weak-tau linear g0
# approximation -- these sit well inside the never-before-measured shoulder,
# tau in [0.3,2]) -- the two articles Block V places AT the bars, per
# Phase-1's own design intent, preserved by Red Team.
C_THR_P04 = 0.005 * max(1.0, (1.7e-4 / 3.0) ** -0.4)   # 0.249827 -- Tier-W p=0.4 bar
C_THR_P05 = 0.005 * max(1.0, (1.7e-4 / 3.0) ** -0.5)   # 0.664211 -- Tier-W p=0.5 bar

TAU_V1 = ab.tau_thr_from_c_thr(C_THR_P04, V_R_OUT, V_PLANE_DX, V_ANGLES, V_GUARD_OUT, V_W_FLANK)
TAU_V2 = ab.tau_thr_from_c_thr(C_THR_P05, V_R_OUT, V_PLANE_DX, V_ANGLES, V_GUARD_OUT, V_W_FLANK)
assert TAU_V1 is not None and TAU_V2 is not None

SIGMA_V1 = ab.sigma_from_tau(TAU_V1, V_R_OUT)
SIGMA_V2 = ab.sigma_from_tau(TAU_V2, V_R_OUT)
assert abs(2.0 * SIGMA_V1 * V_R_OUT - TAU_V1) < 1e-9
assert abs(2.0 * SIGMA_V2 * V_R_OUT - TAU_V2) < 1e-9

ARTICLES_V = ("v1", "v2")
SIGMA_BY_ARTICLE_V = {"v1": SIGMA_V1, "v2": SIGMA_V2}
TAU_BY_ARTICLE_V = {"v1": TAU_V1, "v2": TAU_V2}

# --------------------------------------------------- Block R geometry (exp-033 verbatim, x1.5)
R_NX = 540
R_NY = 2376
R_ABSORB = 60
R_CPL = 30                          # the R3 check: cpl 20 -> 30, 600nm only
R_SRC_X = 450
R_TAPER = 60
R_R_OUT = 117                       # 78 * 1.5, independently rounded (exp-033's own choice)
R_OBJ_X = 255
R_PLANE_DX = 22
R_PLANE_X = R_OBJ_X - R_R_OUT - R_PLANE_DX   # 116
R_OBJ = (R_OBJ_X, 1188)              # NY//2
R_ANGLES = V_ANGLES
R_W_OBJ = 117
R_GUARD_OUT = 278
R_W_FLANK = 117
R_STEPS_AMBIENT = 2100               # 1400 * 1.5, exp-033's own settling fix

# Block R targets exp-040's OWN TAU_V2 (the p=0.5 bar article) -- the
# proposal's own R3 leg -- at Block R's OWN r_out. NOT a copy of SIGMA_V2.
SIGMA_V2_BLOCKR = ab.sigma_from_tau(TAU_V2, R_R_OUT)
assert abs(2.0 * SIGMA_V2_BLOCKR * R_R_OUT - TAU_V2) < 1e-9
# What the (now-avoided) bug would have produced, printed for the record:
_SIGMA_BUG_TAU_DRIFT = 2.0 * SIGMA_V2 * R_R_OUT
assert abs(_SIGMA_BUG_TAU_DRIFT - 1.5 * TAU_V2) < 1e-9   # confirms Red Team's +50% figure

ARTICLES_R = ("v2",)
SIGMA_BY_ARTICLE_R = {"v2": SIGMA_V2_BLOCKR}

# --------------------------------------------------- box-clearance (unused this cycle -- no beam block)

if __name__ == "__main__":
    print("exp-040 Block V (600/450nm, R_OUT=78):")
    print(f"  TAU_V1={TAU_V1:.6f} (C_thr p=0.4 bar={C_THR_P04:.6f})  SIGMA_V1={SIGMA_V1:.8e}")
    print(f"  TAU_V2={TAU_V2:.6f} (C_thr p=0.5 bar={C_THR_P05:.6f})  SIGMA_V2={SIGMA_V2:.8e}")
    print("exp-040 Block R (cpl=30, R_OUT=117):")
    print(f"  SIGMA_V2_BLOCKR={SIGMA_V2_BLOCKR:.8e}  "
          f"(bug would have given tau={_SIGMA_BUG_TAU_DRIFT:.6f}, +{_SIGMA_BUG_TAU_DRIFT/TAU_V2-1:.1%})")
