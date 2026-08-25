"""exp-071 design constants -- ELECTROMAGNETISM's C60/C70 `ABSORB`-depth
causal falsification test for live thread T28 (LOGBOOK.md).

Panel Iteration 48, PHASE 1 (lead: VISION SCIENCE, by rotation). Executes
PLAN.md's Iteration-48 queue item 1, LOCKED by a genuine 6-for-6 blind-seat
convergence at exp-070's Phase-5 final audit: does the ~2.84 deg-family
periodicity in the `C80-C40` padding delta (T28, opened exp-069) track
`ABSORB` depth (a genuine causal, ABSORB-tied mechanism) or stay ~constant
across all four already-built congruent depths (a shared-geometry origin,
NOT ABSORB-tied)?

THE CAUSAL MANIPULATION exp-070's own desk-check batch could not provide:
C40/C80 (already run, exp-069) are only TWO points on the ABSORB axis.
C60 (ABSORB=60,PAD=20) and C70 (ABSORB=70,PAD=30) are ALSO congruent
members of the SAME series (exp-065's design_geometry.py, `A=752` cells
fixed for all four -- CONGRUENT_KEYS). Running the identical period-recovery
analysis exp-069/070 ran on C40/C80 (dense 31-point/0.2deg sweep, free-period
grid search) on C60/C70 too gives FOUR points on the ABSORB-depth axis
instead of two.

WHAT THIS FILE DOES: pure geometry + desk arithmetic + config reuse
(house convention, mirrors experiments/069-.../design_geometry.py's own
structure). Imports exp-065's design_geometry.py (`CONFIGS`,
`CONGRUENT_KEYS`, `CPU_S_PER_CALL`, `CPL`) and exp-069's design_geometry.py
(`DENSE_ANGLES`, `P_deg`, `r3_config`, `R3_RATIO`, `R3_STEPS`, `R3_CPL`,
`STEPS_SETTLED`, `STEPS_NATIVE`) UNCHANGED -- zero new `lab/` diff, zero
redefinition of geometry already established elsewhere (house rule).
NO FDTD stepping happens in this file.

Red Team's Iteration-47 Phase-5 final-audit strengthening requirements,
each addressed by a specific block/metric below (see phase1_proposal.md
for the full falsifiable-bands table):
  (a) a direct cross-config consistency metric |P*(Ca)-P*(Cb)|/mean at
      EVERY ABSORB pair (all 6 pairs among {C40,C60,C70,C80}), not only
      against a derived reference -- Block DENSE-CAUSAL supplies the
      per-config series this is computed from at run.py/Phase 4.
  (b) fold in the already-queued, near-zero-cost peak-cell R3 resolution
      recheck (theta~=37.2/41.4 deg, exp-069's own residual resolution-
      scope gap -- only 2 of 31 angles were ever resolution-checked, both
      near a zero-crossing, not a peak) -- Block R3-PEAK, EXTENDED here
      to all four configs (C40_R3/C60_R3/C70_R3/C80_R3), not only the
      originally-queued C40/C80 pair, since this cycle's own causal claim
      needs resolution-robustness established across the whole ABSORB
      axis, not just the two legacy points. De-scope order (below) can
      retract this extension back to the literal C40/C80-only minimum if
      budget is breached.
  (c) score on the RECOVERED PERIOD at each ABSORB depth, not bare R^2
      alone -- Block DENSE-CAUSAL is sized (31 pts/0.2deg step, same
      window as exp-069's own Block DENSE) so the SAME free-period grid
      search (`_free_period_search`, exp-069's run.py, reused verbatim at
      Phase 4) can run on C60/C70 exactly as it already ran on C40/C80.
  (d) disclose the cross-config spread explicitly, not only a binary
      CONFIRM/REFUTE -- the full 6-pair table from (a) is a required,
      non-optional output row (see phase1_proposal.md Predictions table).

Pure geometry + desk arithmetic -- NO FDTD in this file.

=============================================================================
PHASE 3 SYNTHESIS (Director) -- Red Team's Phase-2 audit verdict:
PROCEED-WITH-MANDATORY-FIXES, 7 items, ZERO overridden (see
phase3_synthesis.md for the full accepted/overridden record; full audit in
phase2_redteam_audit.md). Mandatory fixes implemented in THIS file:
  1. Block SETTLE-C60C70 added (EM's finding) -- C60/C70 at the PEAK angles
     (37.2/41.4deg, not the original P-069-4 zero-crossing angles -- a
     stronger test), STEPS=4200 vs the already-planned STEPS=2800 reading,
     native geometry. Binding precondition on P-071-2, exactly as P-071-4
     already is. +4 calls.
  2. Rayleigh/Fourier resolution-floor computation added (QUANTUM's finding,
     EXTENDED by Red Team to gate BOTH the CONFIRM and REFUTE branches, not
     only REFUTE as originally proposed -- Red Team's own unprompted finding,
     phase2_redteam_audit.md Sec 1: the CONFIRM band's 30% threshold sits at
     only 75% of full Rayleigh resolving power, i.e. UNDER the floor too).
     Zero FDTD cost -- desk arithmetic on already-planned data.
  5. `_free_period_search`/`_fixed_period_fit` now imported BY REFERENCE from
     exp-069's run.py (not re-derived), with an explicit assertion that its
     default grid `(lo_deg, hi_deg, n_grid) == (1.0, 4.0, 400)` matches
     exp-069/070's own values -- closes QUANTUM's "prose promise, not a code
     fact" finding.
  6. De-scope docket (fdtd_budget_minimum) updated to name Block
     SETTLE-C60C70 and the resolution-floor computation as never-de-scoped,
     alongside Block G1 and Block DENSE-CAUSAL (Red Team's own attack 7).
  7. Hard stop restated 90->100 min in NOTES.md/phase3_synthesis.md (text
     only, no code here) -- preserves this program's "a few minutes past the
     3x envelope" convention under the revised (78-call) budget.
Fixes 3/4 (MATERIALS'/THERMODYNAMICS' language-only findings -- reinstating
the "ABSORB is not a material" caveat, renaming the CONFIRM branch's
parenthetical, and adding the THERMO scope-inapplicability sentence) are
implemented in run.py's Combined Verdict text and NOTES.md, not here (no
code artifact backs a pure-language fix).
=============================================================================
"""

import importlib.util
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load_module(rel_path, mod_name):
    """Load another experiment's design_geometry.py under a distinct module
    name -- a plain `import design_geometry` would collide with THIS file
    (mirrors exp-069's own `_load_exp065` idiom exactly)."""
    path = os.path.abspath(os.path.join(HERE, "..", rel_path))
    spec = importlib.util.spec_from_file_location(mod_name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[mod_name] = mod
    spec.loader.exec_module(mod)
    return mod


dg065 = _load_module("065-t24-absorb-boundary-sweep/design_geometry.py",
                      "_exp065_design_geometry")
dg069 = _load_module("069-t21-block-mini-period-match-power-up/design_geometry.py",
                      "_exp069_design_geometry")
run069 = _load_module("069-t21-block-mini-period-match-power-up/run.py",
                       "_exp069_run")

# Mandatory fix 5 (QUANTUM/Red Team): import the period-recovery methodology
# BY REFERENCE, never re-derived, and assert its defaults match exp-069/070's
# own values -- "identical methodology" is now a code fact, not prose.
_fixed_period_fit = run069._fixed_period_fit
_free_period_search = run069._free_period_search
import inspect as _inspect
_fps_defaults = dict(zip(
    ("center_deg", "lo_deg", "hi_deg", "n_grid"),
    (p.default for p in list(_inspect.signature(_free_period_search).parameters.values())[2:])))
assert _fps_defaults == dict(center_deg=39.0, lo_deg=1.0, hi_deg=4.0, n_grid=400), \
    f"_free_period_search defaults drifted from exp-069/070's own values: {_fps_defaults}"

# ------------------------------------------------------- reused verbatim
CONFIGS = dg065.CONFIGS                 # C40, C60, C70, C80, G40, N60
CONGRUENT_KEYS = dg065.CONGRUENT_KEYS   # ("C40","C60","C70","C80")
CPL = dg065.CPL                         # {450:15, 600:20, 750:25}
CPU_S_PER_CALL_1400 = dg065.CPU_S_PER_CALL   # measured, exp-065

P_deg = dg069.P_deg                     # T21's established fringe period model
DENSE_ANGLES = dg069.DENSE_ANGLES       # 31 pts, 36.0-42.0deg, 0.2deg step, 600nm
STEPS_NATIVE = dg069.STEPS_NATIVE       # 1400
STEPS_SETTLED = dg069.STEPS_SETTLED     # 2800 -- this program's settled floor
R3_RATIO = dg069.R3_RATIO               # 1.5
R3_CPL = dg069.R3_CPL                   # {600: 30}
R3_STEPS = dg069.R3_STEPS               # 4200 -- settled-equivalent at cpl=30
r3_config = dg069.r3_config             # generic R3-rescaled congruent-config builder

A_HALF_APERTURE = dg069.A_HALF_APERTURE  # 752
assert CONFIGS["C40"]["A"] == CONFIGS["C60"]["A"] == CONFIGS["C70"]["A"] \
    == CONFIGS["C80"]["A"] == A_HALF_APERTURE, \
    "congruent construction: A must be held fixed across all four ABSORB depths"

ABSORB_DEPTHS = {"C40": 40, "C60": 60, "C70": 70, "C80": 80}

# ---------------------------------------------------- already-committed data
EXP069_RESULTS = os.path.join(
    ROOT, "experiments", "069-t21-block-mini-period-match-power-up", "results.json")


def load_exp069_dense():
    """C40(theta)/C80(theta) at the 31-pt Block DENSE window are ALREADY
    committed (exp-069, Block DENSE, 62 calls) -- reused, not re-run.
    Zero-cost desk read; used both for the G1 identity gate (below) and as
    two of the four per-config series scored at Phase 4."""
    import json
    with open(EXP069_RESULTS) as f:
        d = json.load(f)
    rows = d["block_dense"]["rows"]
    assert len(rows) == 31
    return rows


# -------------------------------------------------- Block G1 (identity gate)
# Mirrors P-069-G1's own construction exactly: a near-zero-cost re-run of
# already-committed cells, checked bit-exact BEFORE any reused data is
# trusted (house rule, exp-069 precedent). 39.0/40.0deg are dense-grid
# points already present in DENSE_ANGLES (step 0.2deg from 36.0) -- reruns
# them at C40/C80 (600nm, STEPS=2800) and diffs against exp-069's own
# committed block_dense rows.
G1_ANGLES = (39.0, 40.0)
assert all(a in DENSE_ANGLES for a in G1_ANGLES)

# ------------------------------------------------- Block DENSE-CAUSAL (new)
# THE causal manipulation: run the IDENTICAL 31-point/0.2deg/600nm/
# STEPS=2800 sweep exp-069 ran on C40/C80, now on C60/C70 -- the two
# congruent, already-built, never-densely-swept points on the ABSORB axis.
DENSE_CAUSAL_CONFIGS = ("C60", "C70")
N_DENSE = len(DENSE_ANGLES)
assert N_DENSE == 31

# ------------------------------------------------------- Block R3-PEAK (new)
# Mandatory-fix (b): the peak-cell R3 recheck exp-069's own resolution leg
# never ran (it tested only 2 of 31 angles, both near delta(theta)'s own
# zero-crossing -- see LOGBOOK T28 entry). Verified below, from exp-069's
# own committed data, that 37.2/41.4deg sit near local extrema of
# delta(theta)=C80(theta)-C40(theta), NOT near a zero-crossing (the
# defect this recheck exists to close).
PEAK_ANGLES = (37.2, 41.4)


def verify_peak_angles_are_extrema():
    rows = load_exp069_dense()
    by_theta = {round(r["theta"], 4): r["delta"] for r in rows}
    deltas = np.array([r["delta"] for r in rows])
    ptp = float(np.ptp(deltas))
    out = {}
    for a in PEAK_ANGLES:
        assert a in by_theta, f"{a} not in committed dense grid"
        out[a] = dict(delta=by_theta[a], frac_of_ptp=abs(by_theta[a]) / (ptp / 2))
    zero_cross_deltas = [by_theta[39.0], by_theta[40.0]]
    return dict(peak=out, window_ptp=ptp,
                zero_crossing_deltas=zero_cross_deltas)


# --------------------------------------------- Block SETTLE-C60C70 (new,
# mandatory fix 1 -- EM's Phase-2 finding). STEPS=2800 was certified
# "settled" only for C40 (exp-065's own 4-point asymptotic series) and C80
# (exp-069's Block SETTLE-C80) -- NEVER for C60/C70, which change
# NX/NY/the damping profile (the geometry) relative to both. Scored at the
# PEAK angles (37.2/41.4deg), a stronger test than P-069-4's original
# zero-crossing angles (39/40deg), mirroring Block SETTLE-C80's own
# construction exactly (STEPS_STRESS=4200 vs STEPS_SETTLED=2800, native
# geometry, cell_ratio=1.0).
STEPS_STRESS = dg069.STEPS_STRESS   # 4200 -- native-geometry stress step
SETTLE_C60C70_CONFIGS = ("C60", "C70")
SETTLE_C60C70_ANGLES = PEAK_ANGLES   # (37.2, 41.4) -- reuse, not re-pick

# R3-rescaled configs for ALL FOUR congruent depths (extends the
# originally-queued C40/C80-only R3 pair -- mandatory-fix (b), extended
# per this file's own docstring rationale). Reuses dg069.r3_config()
# UNCHANGED -- only new (absorb, pad) arguments, zero new machinery.
R3_CONFIGS = {
    "C40_R3": dg069.R3_CONFIGS["C40_R3"],     # already built, exp-069
    "C60_R3": r3_config(round(60 * R3_RATIO), round(20 * R3_RATIO)),   # 90, 30
    "C70_R3": r3_config(round(70 * R3_RATIO), round(30 * R3_RATIO)),   # 105, 45
    "C80_R3": dg069.R3_CONFIGS["C80_R3"],     # already built, exp-069
}
for k, cfg in R3_CONFIGS.items():
    assert cfg["A"] == round(A_HALF_APERTURE * R3_RATIO), \
        f"{k}: R3 congruent construction must hold A fixed"

# --------------------------------------------------------- decision bars
# Cross-config consistency / ABSORB-depth-trend bands (P-071-2, HEADLINE)
# -- see phase1_proposal.md for the full pre-committed table and rationale.
TREND_CONFIRM_MIN_SPREAD = 0.30    # |ΔP* over ABSORB 40->80| / mean(P*) >= 30%
TREND_CONFIRM_MIN_R2 = 0.50        # linear fit P*(ABSORB), R^2 >= 0.50
TREND_REFUTE_MAX_PAIR_SPREAD = 0.15   # max pairwise |P*(Ca)-P*(Cb)|/mean <=15%
TREND_REFUTE_MAX_R2 = 0.30            # linear fit P*(ABSORB), R^2 <= 0.30

# Peak-cell R3 bands (P-071-4) -- IDENTICAL convention to P-069-5 (exp-069),
# now scored at peak angles instead of zero-crossing angles.
R3_CONFIRM_RATIO_BAND = (0.3, 3.0)
R3_REFUTE_RATIO_BAND = (0.1, 10.0)

# --------------------------------------------------- Rayleigh resolution floor
# Mandatory fix 2 (QUANTUM's Phase-2 finding, EXTENDED by Red Team to gate
# BOTH the CONFIRM and REFUTE branches -- phase2_redteam_audit.md Sec 1: the
# CONFIRM band's own 30% threshold sits at only 75% of full Rayleigh
# resolving power at this window/period scale, i.e. UNDER the floor, not
# over it). The 31-point Block DENSE window (36.0-42.0deg) supplies a fixed
# frequency resolution in sin(theta) space; two periods closer together than
# that resolution cannot be reliably distinguished by ANY fit over this
# window, however good its R^2 looks.
DENSE_WINDOW_LO, DENSE_WINDOW_HI = float(DENSE_ANGLES[0]), float(DENSE_ANGLES[-1])
DENSE_WINDOW_DSIN = (math.sin(math.radians(DENSE_WINDOW_HI))
                      - math.sin(math.radians(DENSE_WINDOW_LO)))   # 0.081345...
RESOLUTION_CENTER_DEG = 39.0   # matches _free_period_search's own default


def _T_sin(period_deg, center_deg=RESOLUTION_CENTER_DEG):
    """Convert a period in theta-degrees to a period in sin(theta) units at
    the window's own reference angle -- exactly `_free_period_search`'s own
    internal convention (Tc = radians(P*) * cos(center_deg))."""
    return math.radians(period_deg) * math.cos(math.radians(center_deg))


def rayleigh_resolution_ratio(p_a_deg, p_b_deg, center_deg=RESOLUTION_CENTER_DEG,
                               window_dsin=DENSE_WINDOW_DSIN):
    """Ratio of (window's available frequency resolution) to (frequency
    separation needed to resolve two periods p_a/p_b). >=1.0 means the
    window CAN resolve the pair; <1.0 means it cannot -- any comparison
    built from p_a/p_b (a pairwise spread, or a CONFIRM/REFUTE trend
    verdict) is UNRESOLVED at that scale, regardless of how clean the raw
    statistic looks. Two periods identical returns +inf (trivially
    unresolvable AND uninformative -- treated as unresolved by the caller,
    never as a false REFUTE)."""
    if p_a_deg == p_b_deg:
        return float("inf")
    inv_diff = abs(1.0 / _T_sin(p_a_deg, center_deg) - 1.0 / _T_sin(p_b_deg, center_deg))
    required_dsin = 1.0 / inv_diff
    return window_dsin / required_dsin


RESOLUTION_FLOOR_RATIO_THRESHOLD = 1.0   # ratio >= 1.0 => resolved; < 1.0 => UNRESOLVED

# ------------------------------------------------------------- cost basis
# CPU_S_PER_CALL reused verbatim from dg065 (measured, this container,
# 4-worker ProcessPoolExecutor contention included). C70's own entry is
# disclosed in dg065 as a LINEAR INTERPOLATION between measured C60/C80
# figures, not itself measured -- inherited unchanged, not re-measured
# (task instruction: reuse exp-065's CPU_S_PER_CALL table, do not
# re-measure).
CPU_S_PER_CALL = CPU_S_PER_CALL_1400


def _cost(cfg_key, steps, cell_ratio=1.0):
    base = CPU_S_PER_CALL[cfg_key]
    return base * (steps / STEPS_NATIVE) * cell_ratio


def fdtd_budget():
    """Call counts and wall-clock, block by block. No leg double-counted;
    C40(theta)/C80(theta) at the 31-pt dense window are REUSED from
    exp-069's own committed results.json (0 new calls) -- only C60/C70
    are new FDTD spend for Block DENSE-CAUSAL. Includes mandatory fix 1
    (Block SETTLE-C60C70, Red Team's Phase-2 docket item 1)."""
    n_g1 = len(G1_ANGLES)
    n_causal_cfgs = len(DENSE_CAUSAL_CONFIGS)
    n_peak = len(PEAK_ANGLES)
    n_r3_cfgs = len(R3_CONFIGS)
    n_settle_cfgs = len(SETTLE_C60C70_CONFIGS)
    n_settle_ang = len(SETTLE_C60C70_ANGLES)

    # Block G1: 2 theta x {C40,C80} x 600nm x STEPS=2800 -- identity gate,
    # reruns already-committed cells to certify reuse of exp-069's data.
    g1_calls = n_g1 * 2
    g1_cpu = n_g1 * (_cost("C40", STEPS_SETTLED) + _cost("C80", STEPS_SETTLED))

    # Block DENSE-CAUSAL: 31 theta x {C60,C70} x 600nm x STEPS=2800 --
    # THE causal manipulation. C40/C80 at these same 31 angles are reused
    # from exp-069, zero new cost.
    dense_calls = N_DENSE * n_causal_cfgs
    dense_cpu = N_DENSE * sum(_cost(k, STEPS_SETTLED) for k in DENSE_CAUSAL_CONFIGS)

    # Block R3-PEAK: 2 theta x {C40_R3,C60_R3,C70_R3,C80_R3} x cpl=30 x
    # STEPS=4200(r3). cell_ratio = R3_RATIO^2 (both nx,ny scale by RATIO).
    r3_calls = n_peak * n_r3_cfgs
    r3_cell_ratio = R3_RATIO ** 2
    r3_cpu = n_peak * sum(_cost(k[:3], R3_STEPS, r3_cell_ratio) for k in R3_CONFIGS)

    # Block SETTLE-C60C70 (mandatory fix 1, EM): 2 theta(peak) x {C60,C70} x
    # 600nm x STEPS=4200(stress), native geometry -- closes the settling-
    # closure gap EM's Phase-2 critique found (only C40/C80 ever certified).
    settle_calls = n_settle_ang * n_settle_cfgs
    settle_cpu = n_settle_ang * sum(_cost(k, STEPS_STRESS) for k in SETTLE_C60C70_CONFIGS)

    total_calls = g1_calls + dense_calls + r3_calls + settle_calls
    total_cpu = g1_cpu + dense_cpu + r3_cpu + settle_cpu

    overhead_factor = 1.15
    n_workers = 4
    parallel_efficiency = 0.98
    wall_s = overhead_factor * total_cpu / (n_workers * parallel_efficiency)

    return dict(
        g1=dict(calls=g1_calls, cpu_s=g1_cpu),
        dense_causal=dict(calls=dense_calls, cpu_s=dense_cpu),
        r3_peak=dict(calls=r3_calls, cpu_s=r3_cpu),
        settle_c60c70=dict(calls=settle_calls, cpu_s=settle_cpu),
        total_calls=total_calls, total_cpu_s=total_cpu, wall_s=wall_s,
        wall_min=wall_s / 60.0, envelope3x_min=3 * wall_s / 60.0,
    )


def fdtd_budget_minimum():
    """De-scope floor (mandatory fix 6, Red Team attack 7): R3-PEAK
    retracted to the LITERALLY-queued C40/C80-only pair, dropping C60_R3/
    C70_R3 (this file's own extension). Block DENSE-CAUSAL, Block G1, Block
    SETTLE-C60C70, and the resolution-floor computation are NEVER
    de-scoped -- they gate the headline causal claim's interpretation
    directly (settling-closure and resolution-floor are the two mandatory
    fixes Red Team's Phase-2 audit found load-bearing; a future
    budget-pressured shift must not silently drop them under the pre-
    existing 'retract R3-PEAK first' logic, which predates these fixes)."""
    n_peak = len(PEAK_ANGLES)
    r3_min_calls = n_peak * 2   # C40_R3, C80_R3 only
    r3_min_cpu = n_peak * sum(_cost(k[:3], R3_STEPS, R3_RATIO ** 2)
                               for k in ("C40_R3", "C80_R3"))
    full = fdtd_budget()
    total_calls = (full["g1"]["calls"] + full["dense_causal"]["calls"]
                   + r3_min_calls + full["settle_c60c70"]["calls"])
    total_cpu = (full["g1"]["cpu_s"] + full["dense_causal"]["cpu_s"]
                 + r3_min_cpu + full["settle_c60c70"]["cpu_s"])
    wall_s = 1.15 * total_cpu / (4 * 0.98)
    return dict(total_calls=total_calls, total_cpu_s=total_cpu,
                wall_min=wall_s / 60.0)


if __name__ == "__main__":
    print(f"A_HALF_APERTURE = {A_HALF_APERTURE}")
    print(f"CONGRUENT_KEYS = {CONGRUENT_KEYS}")
    print("\n[1] Congruent-series geometry (dg065.CONFIGS, verified congruent)")
    hdr = ("cfg", "ABSORB", "PAD", "NX", "NY", "A", "aperture_cells")
    print("  " + " ".join(f"{h:>9}" for h in hdr))
    for k in CONGRUENT_KEYS:
        c = CONFIGS[k]
        row = (k, c["absorb"], c["pad"], c["nx"], c["ny"], c["A"], c["aperture_cells"])
        print("  " + " ".join(f"{v:>9}" for v in row))

    print(f"\n[2] P(39deg, 600nm) = {P_deg(39.0, 600):.4f} deg  "
          f"(T21's established model, cited context)")
    print(f"    DENSE_ANGLES ({len(DENSE_ANGLES)} pts): "
          f"{DENSE_ANGLES[0]}..{DENSE_ANGLES[-1]} step 0.2deg (reused verbatim, exp-069)")

    print("\n[3] Peak-angle verification (against exp-069's committed data)")
    pv = verify_peak_angles_are_extrema()
    print(f"    window ptp(delta) = {pv['window_ptp']:.6e}")
    for a, v in pv["peak"].items():
        print(f"    theta={a}: delta={v['delta']:+.6e}  "
              f"|delta|/(ptp/2) = {v['frac_of_ptp']:.3f}  (near 1.0 = near extremum)")
    print(f"    zero-crossing angles (39.0,40.0) delta values = "
          f"{pv['zero_crossing_deltas']}  (near 0 -- the ORIGINAL R3 leg's cells)")

    print("\n[4] R3-rescaled configs (all four ABSORB depths)")
    for k, cfg in R3_CONFIGS.items():
        print(f"    {k}: absorb={cfg['absorb']} pad={cfg['pad']} "
              f"A={cfg['A']} nx={cfg['nx']} ny={cfg['ny']}")

    print("\n[5] FDTD BUDGET (full design, mandatory fixes applied)")
    b = fdtd_budget()
    for name in ("g1", "dense_causal", "r3_peak", "settle_c60c70"):
        print(f"    Block {name.upper():<14} calls={b[name]['calls']:3d}  "
              f"cpu_s={b[name]['cpu_s']:.1f}")
    print(f"    TOTAL calls = {b['total_calls']}")
    print(f"    TOTAL cpu_s = {b['total_cpu_s']:.1f}")
    print(f"    wall = {b['wall_min']:.2f} min")
    print(f"    3x envelope = {b['envelope3x_min']:.2f} min")

    print("\n[6] FDTD BUDGET (de-scoped floor: R3-PEAK retracted to C40/C80 only)")
    bm = fdtd_budget_minimum()
    print(f"    TOTAL calls = {bm['total_calls']}  "
          f"TOTAL cpu_s = {bm['total_cpu_s']:.1f}  wall = {bm['wall_min']:.2f} min")

    print("\n[7] Rayleigh resolution floor (mandatory fix 2, Red Team-extended "
          "to both CONFIRM and REFUTE)")
    print(f"    window Delta(sin theta) = {DENSE_WINDOW_DSIN:.6f} "
          f"({DENSE_WINDOW_LO}-{DENSE_WINDOW_HI}deg)")
    pairs = [
        ("T21 vs P*_delta(exp-069)", 1.9608, 2.8421),
        ("T21 vs C40-free(exp-070)", 1.9608, 2.4361),
        ("C40-free vs C80-free (exp-070)", 2.4361, 2.5338),
    ]
    for label, pa, pb in pairs:
        r = rayleigh_resolution_ratio(pa, pb)
        print(f"    {label:<32} P_a={pa} P_b={pb}  ratio={r:.4f}  "
              f"{'RESOLVED' if r >= RESOLUTION_FLOOR_RATIO_THRESHOLD else 'UNRESOLVED'}")
    print("    CONFIRM band break-even (Red Team Sec 1): spread=30.0% -> "
          f"ratio={rayleigh_resolution_ratio(2.45*(1-0.15), 2.45*(1+0.15)):.4f}  "
          f"(< 1.0 = under the floor); spread=39.3% -> ratio="
          f"{rayleigh_resolution_ratio(2.45*(1-0.1965), 2.45*(1+0.1965)):.4f} (break-even)")
