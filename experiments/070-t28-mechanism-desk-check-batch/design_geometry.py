"""exp-070 design constants + desk arithmetic -- T28 mechanism desk-check
batch, zero FDTD cost. Panel Iteration 47 (lead: QUANTUM OPTICS, by
rotation). Phase 1 proposal (fresh sub-agent) + five blind Phase-2
critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, VISION
SCIENCE) + Red Team's Phase-2 audit (PROCEED-WITH-MANDATORY-FIXES, 10
items, ZERO overridden) -- full record in phase1_proposal.md,
phase2_critique_{photonics,materials,em,thermodynamics,vision}.md,
phase2_redteam_audit.md, phase3_synthesis.md.

WHAT THIS IMPLEMENTS (the 10-item mandatory-fix docket, applied here and
in NOTES.md -- every number quoted anywhere in this cycle's record is
produced by running this file / desk_check_mechanism.py, never hand-typed,
house rule R4):

  1. Item (a)'s pass/fail logic is redefined to score the RECOVERED PERIOD,
     not bare R^2 -- Red Team's own executed proof (Attack 1) showed the
     original bare-R^2 gate CONFIRMS today via a spurious third period
     (2.44/2.53deg) matching neither T21's 1.96deg nor T28's own 2.84deg.
  2. A permutation-null control is added to items (b)/(d)/(e): N=20,000,
     T~Uniform(100,1600) cells, identical search space, reporting the
     percentile `p` of the real target's own best match against 20,000
     random targets in the same space. No CONFIRM on (b)/(d)/(e) without
     `p<=0.05` disclosed alongside it.
  3. Tie-break well-definedness: ties (within 1e-9 relative) are ALL
     reported, not one arbitrary "best" pick; item (e) counts a match if
     ANY tied expression is shared between the two branches.
  4. Every P-070-N item has an explicit NEITHER catch-all (outside both
     CONFIRM and REFUTE bands) -- disclosed, does not narrow PLAN.md
     Iteration-47 queue item 2's scope.
  5. Mandatory disclosed caveat (both outcome-independent): every NAMED
     constant is this bench's own FDTD domain-construction bookkeeping
     (grid padding, graded-loss absorbing-boundary depth -- NOT PML, see
     VALIDATION.md -- taper length, window/guard clearances), not a
     material or physical-optics parameter; a match is at least as
     consistent with a numerical-boundary-construction artifact as with a
     physically real diffracting edge.
  6. One-line THERMODYNAMICS disclosure: the PLAN.md-named, capacity-
     permitting WKB/adiabatic boundary-reflectance fold-in is NOT picked
     up this cycle -- a scope choice, disclosed rather than silent.
  7. Disclosed up front (not buried): the disclosed Phase-1 recon values
     (A_alt~233.19, A_eff~518.81) already sit inside the ORIGINAL 1%/0.70
     bands -- the thresholds were set with full knowledge of these numbers
     (house-honest pre-registration caveat), which is exactly why fix 2's
     null control, not the raw threshold, is the actual gate.
  8. Search-space provenance sentences use the CORRECT per-target
     comparator (Red Team's own Attack 3 catch: PHOTONICS' critique
     conflated the A_eff/519 six-way tie with the A_alt/233 two-way tie).
  9. The null control (fix 2) runs BEFORE any P-070-2/4/5 result is
     narrated; a `p>0.05` result is reported as NEITHER (statistically
     indistinguishable from chance), never a soft/qualified CONFIRM.
  10. PLAN.md queue item 2 is narrowed ONLY by items that clear fix 9's
      corrected gate -- a NEITHER never narrows it.

Pure arithmetic over ALREADY-COMMITTED data -- NO FDTD in this file or in
desk_check_mechanism.py. Reuses exp-069's own `_fixed_period_fit`/
`_free_period_search`/`P_deg` verbatim (imported, never re-derived).
"""

import importlib.util
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load_module(rel_path, name):
    path = os.path.abspath(os.path.join(HERE, "..", rel_path))
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


dg065 = _load_module("065-t24-absorb-boundary-sweep/design_geometry.py",
                      "_exp065_design_geometry")
dg069 = _load_module("069-t21-block-mini-period-match-power-up/design_geometry.py",
                      "_exp069_design_geometry")
run069 = _load_module("069-t21-block-mini-period-match-power-up/run.py",
                       "_exp069_run")

CPL = dg065.CPL
CONFIGS = dg065.CONFIGS
P_deg = dg069.P_deg                       # T21's established period model
T_SINTHETA_600 = dg069.T_SINTHETA_600
_fixed_period_fit = run069._fixed_period_fit
_free_period_search = run069._free_period_search

# --------------------------------------------------- NAMED constants (fix 8)
# Every value read PROGRAMMATICALLY from the imported modules -- none
# hand-typed (R4). 14 entries total: 11 invariant across the congruent
# C40/C80 construction (by design -- the congruent-construction discipline
# these experiments have used since exp-065), plus the 3 that legitimately
# differ (ABSORB at each config, and C80's own PAD).
C40, C80 = CONFIGS["C40"], CONFIGS["C80"]
assert C40["A"] == C80["A"], "congruent construction must hold A fixed"
assert C40["aperture_cells"] == C80["aperture_cells"]
assert C40["clear_plane"] == C80["clear_plane"]
assert C40["clear_src"] == C80["clear_src"]
assert C40["d_sp"] == C80["d_sp"] == dg065.D_SP
assert C40["lever"] == C80["lever"] == dg065.LEVER

NAMED = {
    "A": C40["A"],
    "TAPER": dg065.TAPER,
    "R_OUT": dg065.R_OUT,
    "W_OBJ": dg065.W_OBJ,
    "GUARD_OUT": dg065.GUARD_OUT,
    "W_FLANK": dg065.W_FLANK,
    "D_SP": C40["d_sp"],
    "LEVER": C40["lever"],
    "aperture_cells": C40["aperture_cells"],
    "clear_plane": C40["clear_plane"],
    "clear_src": C40["clear_src"],
    "ABSORB40": C40["absorb"],
    "ABSORB80": C80["absorb"],
    "PAD80": C80["pad"],
}
assert len(NAMED) == 14

_NAMED_NAMES = list(NAMED.keys())
_NAMED_VALS = np.array([NAMED[n] for n in _NAMED_NAMES], dtype=float)
_COEFFS = np.array([c for c in range(-10, 11) if c != 0], dtype=float)  # 20


def build_search_space():
    """All single-term (c*x, 14*20=280) and pair-term (c1*x1+c2*x2, over
    unordered distinct name-pairs, 91*20*20=36400) expressions -- 36,680
    total, matching PHOTONICS'/Red Team's independently-reproduced count.
    Returns (values: float array, labels: list[str])."""
    values = []
    labels = []
    # singles
    for n, v in zip(_NAMED_NAMES, _NAMED_VALS):
        for c in _COEFFS:
            values.append(c * v)
            labels.append(f"{int(c):+d}*{n}")
    # pairs (unordered distinct names, i<j)
    n_names = len(_NAMED_NAMES)
    for i in range(n_names):
        for j in range(i + 1, n_names):
            ni, nj = _NAMED_NAMES[i], _NAMED_NAMES[j]
            vi, vj = _NAMED_VALS[i], _NAMED_VALS[j]
            for c1 in _COEFFS:
                for c2 in _COEFFS:
                    values.append(c1 * vi + c2 * vj)
                    labels.append(f"{int(c1):+d}*{ni}{int(c2):+d}*{nj}")
    values = np.array(values, dtype=float)
    assert len(values) == 280 + 36400 == 36680
    return values, labels


SEARCH_VALUES, SEARCH_LABELS = build_search_space()
N_DISTINCT_VALUES = len(np.unique(np.round(SEARCH_VALUES, 6)))


def closest_matches(target, values=SEARCH_VALUES, labels=SEARCH_LABELS, tie_tol=1e-9):
    """Best relative deviation to `target` over the search space, and the
    FULL set of tied labels within `tie_tol` relative of the best deviation
    (fix 3 -- no arbitrary single 'best pick')."""
    rel = np.abs(values - target) / abs(target)
    best_rel = float(np.min(rel))
    tied_idx = np.where(rel <= best_rel * (1 + tie_tol) + 1e-15)[0]
    tied = sorted({(round(float(values[k]), 6), labels[k]) for k in tied_idx})
    return dict(best_rel=best_rel, n_ties=len(tied), tied=tied)


def null_percentile(target_best_rel, n_trials=20000, lo=100.0, hi=1600.0, seed=0):
    """Fix 2/9: fraction of `n_trials` random targets ~Uniform(lo,hi) whose
    OWN best-match relative deviation is <= `target_best_rel`. Uses a fixed
    seed so the check is exactly reproducible (Red Team's own N=10,000
    scratch check is NOT reused here -- re-run at the docket's specified
    N=20,000 through this committed code path, per mandatory fix 2 item 8)."""
    rng = np.random.default_rng(seed)
    targets = rng.uniform(lo, hi, size=n_trials)
    n_at_or_below = 0
    for t in targets:
        rel = np.abs(SEARCH_VALUES - t) / t
        if float(np.min(rel)) <= target_best_rel:
            n_at_or_below += 1
    p = n_at_or_below / n_trials
    return dict(n_trials=n_trials, lo=lo, hi=hi, seed=seed,
                p=p, n_at_or_below=n_at_or_below)


if __name__ == "__main__":
    print(f"NAMED ({len(NAMED)} constants): {NAMED}")
    print(f"Search space: {len(SEARCH_VALUES)} expressions, "
          f"{N_DISTINCT_VALUES} distinct values (rounded to 1e-6)")
    print(f"P(39,600) = {P_deg(39.0, 600):.4f} deg")
