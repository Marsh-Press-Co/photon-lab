"""exp-093 -- T28 Upper-Window Crossing Resolution & NETD Threading: Panel
Iteration 70. Lead seat: THERMODYNAMICS. Frozen spec: NOTES.md (Predictions
committed to git strictly BEFORE this file's first run, house discipline).

Five items, run in this exact order (5 -> 3 -> 1 -> 2 -> 4):

  Item 5 (28 FDTD calls, FIRST) -- NETD/energy-sidecar backfill of exp-092's
    own Rank-1 seven angles ({39.2,39.4,39.6,39.8,40.0,41.8,42.0}), both
    configs, both legs, cpl=30, STEPS=4200, sigma_max=0.5 (native). New,
    additive `cell_metrics_full()`/`pair_metrics_full()` forward BOTH
    c_cell's and g_cell's own p_abs_w/dt_ss_full_K/netd_classification/
    sigma_ext_cells/ratio_abs_ext_raw -- exp-092's own pair_metrics() only
    ever forwarded c_cell's. Consistency gate: delta_scene/frac_contrast/
    ratio_k/floor_pass at all 7 angles must equal exp-092's own filed
    rank1.per_theta values to float equality (deterministic FDTD) -- a HARD
    assert, not a soft check.

  Item 3 (4 FDTD calls, SECOND) -- sigma_max=1/3 (corrected) check localized
    to the two NODE-UNRESOLVABLE angles (41.8/42.0), article leg only; empty
    legs reused in-memory from item 5. Gates item 1's own sigma_max choice.

  Item 1 (24 FDTD calls, THIRD) -- denser off-grid cpl=30 sweep, six new
    points {41.750,41.775,41.825,41.850,41.875,41.900}, both configs, both
    legs, sigma_max branch-gated on item 3's own verdict (CONFIRM->0.5,
    else->1/3). Scores the three-way TWO-NODE CONFIRMED / SINGLE-NULL /
    STILL AMBIGUOUS outcome.

  Item 2 (0 FDTD calls, FOURTH, desk-only) -- the n=8 cpl=30-only
    caution-zone re-fit, reusing exp-090's own find_zero_crossings/
    firth_logistic/naive_mle_diverges/auc VERBATIM, using exp-090's own
    auc(-pos_m,-neg_m) calling convention (NOT the plain auc(pos,neg) the
    pre-freeze draft mistakenly used -- phase3_synthesis.md's RT-1 fix).
    Gated (extension only, not the base table) on item 1's own outcome.

  Item 4 (0 FDTD calls, computed anywhere in this file, desk-only) -- the
    2D Yee-grid numerical-dispersion phase-accumulation integral at the
    actually-mandated aperture length scale (A_HALF_APERTURE=752/1128
    cells, Director's own independent third derivation, phase3_synthesis.md
    Sec.0 -- NOT the round-trip PAD distance the pre-freeze draft mistakenly
    used, retained below only as a relabeled secondary computation).

Reuses experiments/092-.../run.py's own `dg`/`box_for_r3`/`ref_for_r3`/
`_run_sim_r3`/`build_article_r3`/`build_article_r3_sigma`/`_run_sim_r3_sigma`/
`widths_direction_corrected`/`_label`/`compute_floor`/`_profile`/
`contrast_pair`/`ratio_sign_verdict`/`classification_word`/`PEC_R_R3`/
`R3_R_OUT_CELLS`/`cell_metrics`/`pair_metrics`/`one_call`/`run_block`/`FLOOR`/
`FLOOR_FRAC`/`RATIO_LOW`/`RATIO_HIGH`/`XI_TOL`/`NOISE_MULT` VERBATIM,
UNMODIFIED, by loading experiments/092-.../run.py as a module (which itself
already loads exp-091 and exp-090 by the same house `_load()` idiom) --
zero geometry retyped, zero `lab/` diff, zero diff to any frozen experiment
file. Reuses experiments/090-.../run.py's own `find_zero_crossings`/
`firth_logistic`/`naive_mle_diverges`/`auc` VERBATIM for item 2.

NEW code this cycle (all additive):
  * `cell_metrics_full()` -- thin, explicitly-named wrapper around
    exp-092's own `cell_metrics()`. Disclosed: `cell_metrics()` never
    stripped its own per-cell `thermo` dict (it already carries
    sigma_ext_cells/ratio_abs_ext_raw/p_abs_w/dt_ss_full_K/
    netd_classification in full) -- the truncation this cycle closes
    happens one level up, in `pair_metrics()`, which only ever forwarded
    `c_cell`'s own fields into the persisted record. Kept as its own named
    function per NOTES.md's own item-5 spec (not merely inlined), so a
    future cycle can find it by name.
  * `pair_metrics_full()` -- generalizes exp-092's own `pair_metrics()`:
    identical formula (calls it internally, no retyping), PLUS forwards
    `g_cell`'s own p_abs_w/dt_ss_full_K/netd_classification/
    sigma_ext_cells/ratio_abs_ext_raw (and, for symmetry, `c_cell`'s own
    sigma_ext_cells, not previously threaded either) alongside `c_cell`'s
    own fields the existing function already threads.
  * `compute_zone()` -- item 2's own n=8 caution-zone fit, mirroring
    exp-092's own Rank-2 `compute_zone()` (defined inside its `main()`,
    not importable) line-for-line, calling exp-090's own
    auc/firth_logistic/naive_mle_diverges through the loaded module,
    nothing re-derived.
  * `yee_dispersion_k()`/`delta_phi_deg()`/item-4 driver -- the desk-only
    2D Yee-grid dispersion solve (Brent's method via `scipy.optimize.
    brentq`), new this cycle (never coded before, only cited -- see
    NOTES.md Item 4 / phase3_synthesis.md Sec.0).
"""

import importlib.util
import json
import math
import os
import sys
import time

import numpy as np
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    """House `_load()` pattern (exp-078..092's own idiom for cross-
    experiment-directory imports)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP091_DIR = os.path.join(ROOT, "experiments", "091-t28-r3-resolution-denser-recheck")
EXP091_RESULTS = os.path.join(EXP091_DIR, "results.json")
EXP092_DIR = os.path.join(ROOT, "experiments", "092-t28-crossing-relocation-caution-zone-rebuild")
EXP092_RESULTS = os.path.join(EXP092_DIR, "results.json")

exp092 = _load(os.path.join(EXP092_DIR, "run.py"), "_exp093_exp092")
exp091 = exp092.exp091   # exp-092's own module already loaded exp-091 this way
exp090 = exp092.exp090   # ...and exp-090, same chain

dg = exp092.dg
PAIR_KEYS_R3 = exp092.PAIR_KEYS_R3
STEPS_R3 = exp092.STEPS_R3
assert STEPS_R3 == 4200
SIGMA_NATIVE = exp092.SIGMA_NATIVE
SIGMA_R3_CORRECTED = exp092.SIGMA_R3_CORRECTED
assert SIGMA_NATIVE == 0.5
assert abs(SIGMA_R3_CORRECTED - 1.0 / 3.0) < 1e-12

RANK1_ANGLES = exp092.RANK1_ANGLES        # {39.2,39.4,39.6,39.8,40.0,41.8,42.0}
RANK3_ANGLES = exp092.RANK3_ANGLES        # {37.2,40.2,41.4}
assert RANK1_ANGLES == [39.2, 39.4, 39.6, 39.8, 40.0, 41.8, 42.0]

cell_metrics = exp092.cell_metrics
pair_metrics = exp092.pair_metrics
one_call = exp092.one_call
run_block = exp092.run_block
ratio_sign_verdict = exp092.ratio_sign_verdict
classification_word = exp092.classification_word
compute_floor = exp092.compute_floor
XI_TOL = exp092.XI_TOL
NOISE_MULT = exp092.NOISE_MULT
RATIO_LOW, RATIO_HIGH = exp092.RATIO_LOW, exp092.RATIO_HIGH
NETD_BAND_K = exp092.NETD_BAND_K
find_zero_crossings = exp092.find_zero_crossings

from lab import Sim  # noqa: E402

# item 3 -- localized to the two NODE-UNRESOLVABLE Rank-1 angles
ITEM3_ANGLES = [41.8, 42.0]
for _a in ITEM3_ANGLES:
    assert _a in RANK1_ANGLES

# item 1 -- six new off-grid points, 0.025deg step, 41.75-41.90
ITEM1_ANGLES = [41.750, 41.775, 41.825, 41.850, 41.875, 41.900]
for _a in ITEM1_ANGLES:
    assert _a not in dg.DENSE_ANGLES, f"{_a} unexpectedly on the native DENSE_ANGLES grid"

VERDICT_RANK = {"REFUTE": 0, "NEITHER": 1, "CONFIRM": 2}


# ---------------------------------------------------------------- NEW code (item 5)
def cell_metrics_full(key, th, steps, cap_empty, cap_article):
    """Generalizes exp-092's own `cell_metrics()`. Disclosed: `cell_metrics`
    never stripped its own per-cell `thermo` dict -- it already returns
    sigma_ext_cells/ratio_abs_ext_raw/p_abs_w/dt_ss_full_K/
    netd_classification in full. Kept as its own named function per
    NOTES.md's own item-5 spec (calls the existing function verbatim, no
    formula retyped)."""
    return cell_metrics(key, th, steps, cap_empty, cap_article)


def pair_metrics_full(c_cell, g_cell, floor):
    """Generalizes exp-092's own `pair_metrics()`: identical formula
    (called internally, unmodified), PLUS forwards g_cell's own p_abs_w/
    dt_ss_full_K/netd_classification/sigma_ext_cells/ratio_abs_ext_raw
    alongside c_cell's own fields the existing function already threads
    (and, for symmetry/completeness, c_cell's own sigma_ext_cells, which
    was likewise never threaded)."""
    pm = pair_metrics(c_cell, g_cell, floor)
    pm = dict(pm)
    pm["sigma_ext_cells_c"] = c_cell["thermo"]["sigma_ext_cells"]
    pm["p_abs_w_g"] = g_cell["thermo"]["p_abs_w"]
    pm["dt_ss_full_K_g"] = g_cell["thermo"]["dt_ss_full_K"]
    pm["netd_classification_g"] = g_cell["thermo"]["netd_classification"]
    pm["sigma_ext_cells_g"] = g_cell["thermo"]["sigma_ext_cells"]
    pm["ratio_abs_ext_raw_g"] = g_cell["thermo"]["ratio_abs_ext_raw"]
    return pm


def netd_row(pm):
    """Full 14/2-cell NETD sidecar row (both configs), for persistence --
    matching Iteration-69 LOGBOOK's own named truncation defect (exp-092's
    own results.json dropped these fields), not repeating it here."""
    return dict(
        p_abs_w_c=pm["p_c"], p_abs_w_g=pm["p_abs_w_g"],
        dt_ss_full_K_c=pm["dt_ss_full_K_c"], dt_ss_full_K_g=pm["dt_ss_full_K_g"],
        netd_classification_c=pm["netd_classification_c"],
        netd_classification_g=pm["netd_classification_g"],
        sigma_ext_cells_c=pm["sigma_ext_cells_c"], sigma_ext_cells_g=pm["sigma_ext_cells_g"],
        ratio_abs_ext_raw_c=pm["ratio_abs_ext_raw_c"], ratio_abs_ext_raw_g=pm["ratio_abs_ext_raw_g"],
    )


# ---------------------------------------------------------------- NEW code (item 2)
def compute_zone(rows_subset):
    """Item 2's own n=8 caution-zone fit. Mirrors exp-092's own Rank-2
    `compute_zone()` (defined inside its own main(), not importable)
    line-for-line -- exp-090's own auc/firth_logistic/naive_mle_diverges,
    called through the loaded module, nothing re-derived. Uses exp-090's
    own auc(-pos_m,-neg_m) calling convention (RT-1 fix)."""
    margins = np.array([r["margin"] for r in rows_subset])
    Y = np.array([r["y"] for r in rows_subset])
    n = len(rows_subset)
    pos_m, neg_m = margins[Y == 1], margins[Y == 0]
    zone_lo = float(np.max(pos_m)) if len(pos_m) else None
    zone_hi = float(np.min(neg_m)) if len(neg_m) else None
    a = exp090.auc(-pos_m, -neg_m) if len(pos_m) and len(neg_m) else None
    x = np.log10(margins)
    X = np.column_stack([np.ones(n), x])
    beta, n_iter, converged = exp090.firth_logistic(X, Y)
    m50 = (10 ** (-beta[0] / beta[1])) if converged else float("nan")
    naive_beta, diverged = exp090.naive_mle_diverges(X, Y)
    return dict(n=n, pos=int(Y.sum()), auc=a, zone=[zone_lo, zone_hi],
                inverted=bool(zone_lo is not None and zone_hi is not None and zone_lo > zone_hi),
                firth_beta=beta.tolist(), firth_n_iter=n_iter, firth_converged=bool(converged),
                firth_m50=float(m50), naive_mle_diverges=bool(diverged),
                naive_mle_beta=naive_beta.tolist())


# ---------------------------------------------------------------- NEW code (item 4)
COURANT_FRAC = dg.COURANT_FRAC
assert abs(COURANT_FRAC - 0.99) < 1e-12
S_COURANT = COURANT_FRAC / math.sqrt(2.0)
A_HALF_APERTURE_NATIVE = dg.A_HALF_APERTURE                       # 752
A_HALF_APERTURE_R3 = round(dg.A_HALF_APERTURE * dg.R3_RATIO)      # 1128
assert A_HALF_APERTURE_NATIVE == 752 and A_HALF_APERTURE_R3 == 1128
PAD_NATIVE_ROUNDTRIP = 2 * 40    # exp-069's own native PAD=40, round-trip
PAD_R3_ROUNDTRIP = 2 * 60        # R3-scaled PAD=60, round-trip
P_STAR_DEG = 2.8421              # T28's own established macro-period


def yee_dispersion_k(theta_deg, cpl):
    """Solve (1/S^2) sin^2(pi*S/cpl) = sin^2(k cos(theta)/2) + sin^2(k
    sin(theta)/2) for the numerical wavenumber magnitude k(theta,cpl), via
    Brent's method, bracketing around the ideal k0=2*pi/cpl (NOTES.md Item
    4 / lab/fdtd2d.py::Sim.__init__'s own S=courant_frac/sqrt(2))."""
    th = math.radians(theta_deg)
    rhs = (1.0 / S_COURANT ** 2) * math.sin(math.pi * S_COURANT / cpl) ** 2

    def f(k):
        return math.sin(k * math.cos(th) / 2.0) ** 2 + math.sin(k * math.sin(th) / 2.0) ** 2 - rhs

    k0 = 2.0 * math.pi / cpl
    lo, hi = 0.5 * k0, 1.5 * k0
    return brentq(f, lo, hi), k0


def delta_phi_deg(theta_deg, cpl, ell_cells):
    """Delta_phi(theta,cpl,ell) = -degrees((k-k0)*ell) (NOTES.md's own
    sign convention -- negative at cpl=20, less-negative at cpl=30)."""
    k, k0 = yee_dispersion_k(theta_deg, cpl)
    return -math.degrees((k - k0) * ell_cells)


def item4_table(ell_native, ell_r3, angles):
    rows = {}
    for th in angles:
        dphi20 = delta_phi_deg(th, 20, ell_native)
        dphi30 = delta_phi_deg(th, 30, ell_r3)
        ddphi = dphi30 - dphi20
        predicted_dtheta = (ddphi / 360.0) * P_STAR_DEG
        rows[th] = dict(delta_phi_cpl20=dphi20, delta_phi_cpl30=dphi30,
                         delta_delta_phi=ddphi, predicted_dtheta=predicted_dtheta)
    return rows


def main():
    print("=" * 78)
    print("exp-093 -- T28 upper-window crossing resolution & NETD threading")
    print("=" * 78)

    t_start = time.time()

    # ---------------------------------------------------------------- R13 floor gate (desk, zero FDTD, unchanged)
    floor, rms, n83, per_theta_83_full = compute_floor()
    print(f"\n[R13 floor gate] RMS[frac_contrast], n={n83}: {rms:.6e}  "
          f"FLOOR={floor:.6e}  (unchanged, applied unrecomputed -- Idealization 6)")

    # ---------------------------------------------------------------- P1: vacuum footprint precondition
    BOX_CLEARANCE_A_R3 = exp092.BOX_CLEARANCE_A_R3
    BOX_CLEARANCE_B_R3 = exp092.BOX_CLEARANCE_B_R3
    box_for_r3 = exp092.box_for_r3
    vac_report = {}
    vac_pass = True
    for key in PAIR_KEYS_R3:
        cfg = dg.R3_CONFIGS[key]
        sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=dg.R3_CPL[600],
                  courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
        cell = {}
        for box_name, clearance in (("BOX_A", BOX_CLEARANCE_A_R3), ("BOX_B", BOX_CLEARANCE_B_R3)):
            x0, x1, y0, y1 = box_for_r3(cfg, clearance)
            footprint = sim.damp_e[x0:x1 + 1, y0:y1 + 1]
            ok = bool(np.all(footprint == 1.0))
            cell[box_name] = dict(box=[x0, x1, y0, y1], all_vacuum=ok)
            vac_pass = vac_pass and ok
        vac_report[key] = cell
    print(f"\n[P1] vacuum-footprint precondition: PASS={vac_pass}")
    assert vac_pass, "P1 FAILED -- a BOX_A/BOX_B footprint is not pure vacuum; HALT"

    xi_pass = True
    nonneg_pass = True

    # =================================================================
    # ITEM 5 -- NETD/energy-sidecar backfill (FIRST, 28 calls)
    # =================================================================
    print("\n" + "=" * 78)
    print("ITEM 5 -- NETD/energy-sidecar backfill of exp-092's own Rank-1 7 angles")
    print("=" * 78)

    jobs5 = []
    for key in PAIR_KEYS_R3:
        for th in RANK1_ANGLES:
            jobs5.append((key, th, False, STEPS_R3, None))
            jobs5.append((key, th, True, STEPS_R3, SIGMA_NATIVE))
    assert len(jobs5) == 28
    print(f"\n{len(jobs5)} FDTD calls queued (item 5)")
    captures5, wall5 = run_block(jobs5)
    print(f"item 5 wall time: {wall5:.1f}s ({wall5/60.0:.2f} min)")

    cells5 = {}
    for key in PAIR_KEYS_R3:
        for th in RANK1_ANGLES:
            cap_empty = captures5[(key, th, False, STEPS_R3)]
            cap_article = captures5[(key, th, True, STEPS_R3)]
            cell = cell_metrics_full(key, th, STEPS_R3, cap_empty, cap_article)
            cells5[(key, th)] = cell
            for xi in cell["xi_ext"].values():
                if xi > XI_TOL:
                    xi_pass = False
            if not cell["sigma_abs_nonneg"]:
                nonneg_pass = False
    print(f"\n[item 5] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
    assert xi_pass, "item 5 FAILED -- extinction-routes disagreement; HALT"
    print(f"[item 5] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
    assert nonneg_pass, "item 5 FAILED -- non-negativity gate; HALT"

    item5_report = {}
    for th in RANK1_ANGLES:
        c_cell = cells5[("C40_R3", th)]
        g_cell = cells5[("G40_R3", th)]
        pm = pair_metrics_full(c_cell, g_cell, floor)
        row = dict(
            delta_scene=pm["delta_scene"], frac_contrast=pm["frac_contrast"],
            ratio_k=pm["ratio_k"], floor_pass=pm["floor_pass"], resolved=pm["resolved"],
            frac_p_abs=pm["frac_p_abs"],
            classification=("NODE-UNRESOLVABLE" if not pm["floor_pass"] else classification_word(pm["ratio_k"])),
        )
        row.update(netd_row(pm))
        item5_report[th] = row
    print("\n[item 5] per-angle results:")
    for th, r in sorted(item5_report.items()):
        print(f"  theta={th}: delta_scene={r['delta_scene']:+.6e}  frac_contrast={r['frac_contrast']:.6e}  "
              f"ratio_k={r['ratio_k']:.4f}  class={r['classification']}  floor_pass={r['floor_pass']}  "
              f"dt_ss_full_K(C)={r['dt_ss_full_K_c']:.4e}  dt_ss_full_K(G)={r['dt_ss_full_K_g']:.4e}  "
              f"netd(C)={r['netd_classification_c']}  netd(G)={r['netd_classification_g']}")

    # ---- (Item 5) PRIMARY consistency gate vs exp-092's own filed rank1.per_theta
    with open(EXP092_RESULTS) as f:
        j092 = json.load(f)
    filed_rank1 = j092["rank1"]["per_theta"]
    consistency_check = {}
    consistency_all_match = True
    for th in RANK1_ANGLES:
        filed = filed_rank1[str(th)]
        fresh = item5_report[th]
        row = {}
        for field in ("delta_scene", "frac_contrast", "ratio_k", "floor_pass"):
            match = bool(fresh[field] == filed[field])
            row[field] = dict(fresh=fresh[field], filed=filed[field], bit_exact_match=match)
            if not match:
                consistency_all_match = False
        consistency_check[str(th)] = row
        flag = "" if all(v["bit_exact_match"] for v in row.values()) else "  <<< MISMATCH"
        print(f"  [item 5 consistency] theta={th}: "
              f"delta_scene match={row['delta_scene']['bit_exact_match']}  "
              f"frac_contrast match={row['frac_contrast']['bit_exact_match']}  "
              f"ratio_k match={row['ratio_k']['bit_exact_match']}  "
              f"floor_pass match={row['floor_pass']['bit_exact_match']}{flag}")
    print(f"\n[Item 5 PRIMARY] consistency gate vs exp-092's own filed rank1.per_theta, "
          f"ALL 7 ANGLES bit-exact: {consistency_all_match}")
    item5_verdict = "CONFIRM" if consistency_all_match else "REFUTE"
    assert consistency_all_match, (
        "Item 5 PRIMARY REFUTE -- deterministic-FDTD reproduction of exp-092's own filed "
        "rank1.per_theta values disagreed; STOPPING per NOTES.md's own hard-gate instruction "
        "rather than continuing to items 3/1/2/4 on an unverified base. See consistency_check above.")
    print(f"[Item 5 PRIMARY] VERDICT={item5_verdict}")

    # ---- (Item 5b) informational, non-gating -- NETD threading
    print("\n[Item 5b, informational, non-gating] NETD threading, 14 cells "
          "(NETD/instrument, not human-eye -- Idealization 3):")
    item5b_lo, item5b_hi = 1e-5, 5e-4
    item5b_surprises = []
    for key in PAIR_KEYS_R3:
        for th in RANK1_ANGLES:
            cell = cells5[(key, th)]
            dt = cell["thermo"]["dt_ss_full_K"]
            netd_c = cell["thermo"]["netd_classification"]
            in_range = item5b_lo <= dt <= item5b_hi
            surprise = (netd_c != "UNDETECTABLE") or (dt < item5b_lo / 3.0) or (dt > item5b_hi * 3.0)
            if surprise:
                item5b_surprises.append((key, th, dt, netd_c))
            print(f"  {key} theta={th}: dt_ss_full_K={dt:.4e}  class={netd_c}  "
                  f"in_predicted_range[{item5b_lo:.0e},{item5b_hi:.0e}]={in_range}")
    print(f"[Item 5b] genuine surprises (MARGINAL/DETECTABLE, or >3x outside predicted range): "
          f"{item5b_surprises if item5b_surprises else 'NONE'}")

    # =================================================================
    # ITEM 3 -- sigma_max check, near-null (SECOND, 4 calls)
    # =================================================================
    print("\n" + "=" * 78)
    print("ITEM 3 -- sigma_max PRIMARY-channel check, localized to the upper near-null")
    print("=" * 78)

    jobs3 = []
    for key in PAIR_KEYS_R3:
        for th in ITEM3_ANGLES:
            jobs3.append((key, th, True, STEPS_R3, SIGMA_R3_CORRECTED))
    assert len(jobs3) == 4
    print(f"\n{len(jobs3)} FDTD calls queued (item 3, article leg only; empty legs "
          f"reused in-memory from item 5)")
    captures3, wall3 = run_block(jobs3)
    print(f"item 3 wall time: {wall3:.1f}s ({wall3/60.0:.2f} min)")

    cells3 = {}
    for key in PAIR_KEYS_R3:
        for th in ITEM3_ANGLES:
            cap_empty = captures5[(key, th, False, STEPS_R3)]      # reused in-memory from item 5
            cap_article = captures3[(key, th, True, STEPS_R3)]
            cell = cell_metrics_full(key, th, STEPS_R3, cap_empty, cap_article)
            cells3[(key, th)] = cell
            for xi in cell["xi_ext"].values():
                if xi > XI_TOL:
                    xi_pass = False
            if not cell["sigma_abs_nonneg"]:
                nonneg_pass = False
    print(f"\n[item 3] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
    assert xi_pass, "item 3 FAILED -- extinction-routes disagreement; HALT"
    print(f"[item 3] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
    assert nonneg_pass, "item 3 FAILED -- non-negativity gate; HALT"

    item3_report = {}
    ds_cells, fc_cells, pabs_cells = [], [], []
    for th in ITEM3_ANGLES:
        c_cell = cells3[("C40_R3", th)]
        g_cell = cells3[("G40_R3", th)]
        pm = pair_metrics_full(c_cell, g_cell, floor)
        native = item5_report[th]

        ds_ratio = pm["delta_scene"] / native["delta_scene"] if native["delta_scene"] != 0 else float("inf")
        ds_sign_match = (pm["delta_scene"] > 0) == (native["delta_scene"] > 0)
        fc_ratio = pm["frac_contrast"] / native["frac_contrast"] if native["frac_contrast"] != 0 else float("inf")
        pabs_ratio = pm["p_c"] / native["p_abs_w_c"] if native["p_abs_w_c"] != 0 else float("inf")
        pabs_sign_match = (pm["p_abs_w_g"] - pm["p_c"] > 0) == (native["p_abs_w_g"] - native["p_abs_w_c"] > 0)

        ds_cells.append((ds_ratio, ds_sign_match))
        fc_cells.append((fc_ratio, True))
        pabs_cells.append((pabs_ratio, pabs_sign_match))

        item3_report[th] = dict(
            sigma_corrected_delta_scene=pm["delta_scene"], native_delta_scene=native["delta_scene"],
            delta_scene_ratio=ds_ratio, delta_scene_sign_match=ds_sign_match,
            sigma_corrected_frac_contrast=pm["frac_contrast"], native_frac_contrast=native["frac_contrast"],
            frac_contrast_ratio=fc_ratio,
            sigma_corrected_p_abs_w_c=pm["p_c"], native_p_abs_w_c=native["p_abs_w_c"],
            p_abs_w_ratio=pabs_ratio, p_abs_w_sign_match=pabs_sign_match,
            sigma_corrected_ratio_abs_ext_raw=pm["ratio_abs_ext_raw_c"],
            ratio_abs_ext_dev_from_anchor=abs(pm["ratio_abs_ext_raw_c"] - 0.51) / 0.51,
            ratio_k=pm["ratio_k"], floor_pass=pm["floor_pass"],
        )
        item3_report[th].update(netd_row(pm))
    print("\n[item 3] sigma-corrected (1/3) vs item-5's own native-sigma (0.5) comparison:")
    for th, r in sorted(item3_report.items()):
        print(f"  theta={th}: delta_scene ratio={r['delta_scene_ratio']:.4f} "
              f"sign_match={r['delta_scene_sign_match']}  "
              f"frac_contrast ratio={r['frac_contrast_ratio']:.4f}  "
              f"p_abs_w ratio={r['p_abs_w_ratio']:.4f} sign_match={r['p_abs_w_sign_match']}  "
              f"ratio_abs_ext={r['sigma_corrected_ratio_abs_ext_raw']:.4f} "
              f"(dev from 0.51 anchor: {r['ratio_abs_ext_dev_from_anchor']:.2%})")

    ds_verdict = ratio_sign_verdict(ds_cells)
    fc_verdict = ratio_sign_verdict(fc_cells)
    item3_verdict = min([ds_verdict, fc_verdict], key=lambda v: VERDICT_RANK[v])
    print(f"\n[Item 3 PRIMARY] delta_scene sub-verdict={ds_verdict}  frac_contrast sub-verdict={fc_verdict}  "
          f"OVERALL VERDICT={item3_verdict}")

    item3b_verdict = ratio_sign_verdict(pabs_cells)
    print(f"[Item 3b, informational, non-gating] p_abs_w verdict={item3b_verdict}")

    # ---- sigma_max branch rule for item 1 (pre-registered, NOTES.md)
    if item3_verdict == "CONFIRM":
        sigma_item1 = SIGMA_NATIVE
        branch_reason = "item 3 CONFIRM -> item 1 runs at sigma_max=0.5 (native, comparable to flanking anchors)"
    else:
        sigma_item1 = SIGMA_R3_CORRECTED
        branch_reason = (f"item 3 {item3_verdict} -> item 1 runs at sigma_max=1/3 (corrected"
                          f"{' -- REFUTE, material contamination confirmed' if item3_verdict == 'REFUTE' else ' -- NEITHER-triggered conservative default, disclosed as such, not a CONFIRM-level finding'}"
                          f"), disclosed as NOT directly comparable to the native-sigma flanking anchors "
                          f"(41.6/41.8/42.0) -- Idealization 11")
    print(f"\n[Sigma branch] {branch_reason}")

    # =================================================================
    # ITEM 1 -- denser off-grid sweep (THIRD, 24 calls)
    # =================================================================
    print("\n" + "=" * 78)
    print(f"ITEM 1 -- denser off-grid cpl=30 sweep, 41.75deg-41.90deg (sigma_max={sigma_item1:.6f})")
    print("=" * 78)

    jobs1 = []
    for key in PAIR_KEYS_R3:
        for th in ITEM1_ANGLES:
            jobs1.append((key, th, False, STEPS_R3, None))
            jobs1.append((key, th, True, STEPS_R3, sigma_item1))
    assert len(jobs1) == 24
    print(f"\n{len(jobs1)} FDTD calls queued (item 1)")
    captures1, wall1 = run_block(jobs1)
    print(f"item 1 wall time: {wall1:.1f}s ({wall1/60.0:.2f} min)")

    total_wall = wall5 + wall3 + wall1
    print(f"\ntotal FDTD wall time (items 5+3+1): {total_wall:.1f}s ({total_wall/60.0:.2f} min)")

    cells1 = {}
    for key in PAIR_KEYS_R3:
        for th in ITEM1_ANGLES:
            cap_empty = captures1[(key, th, False, STEPS_R3)]
            cap_article = captures1[(key, th, True, STEPS_R3)]
            cell = cell_metrics_full(key, th, STEPS_R3, cap_empty, cap_article)
            cells1[(key, th)] = cell
            for xi in cell["xi_ext"].values():
                if xi > XI_TOL:
                    xi_pass = False
            if not cell["sigma_abs_nonneg"]:
                nonneg_pass = False
    print(f"\n[item 1] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
    assert xi_pass, "item 1 FAILED -- extinction-routes disagreement; HALT"
    print(f"[item 1] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
    assert nonneg_pass, "item 1 FAILED -- non-negativity gate; HALT"

    item1_report = {}
    for th in ITEM1_ANGLES:
        c_cell = cells1[("C40_R3", th)]
        g_cell = cells1[("G40_R3", th)]
        pm = pair_metrics_full(c_cell, g_cell, floor)
        row = dict(
            delta_scene=pm["delta_scene"], frac_contrast=pm["frac_contrast"],
            ratio_k=pm["ratio_k"], floor_pass=pm["floor_pass"], resolved=pm["resolved"],
            frac_p_abs=pm["frac_p_abs"],
            classification=("NODE-UNRESOLVABLE" if not pm["floor_pass"] else classification_word(pm["ratio_k"])),
        )
        row.update(netd_row(pm))
        item1_report[th] = row
    print("\n[item 1] per-angle results:")
    for th, r in sorted(item1_report.items()):
        print(f"  theta={th}: delta_scene={r['delta_scene']:+.6e}  frac_contrast={r['frac_contrast']:.6e}  "
              f"ratio_k={r['ratio_k']:.4f}  class={r['classification']}  floor_pass={r['floor_pass']}")

    # ---- three-way outcome (NOTES.md's own falsifiable categories)
    any_confirmed = any(r["delta_scene"] > 0 and r["floor_pass"] for r in item1_report.values())
    all_nonpositive = all(r["delta_scene"] <= 0 for r in item1_report.values())
    all_floor_fail = all(not r["floor_pass"] for r in item1_report.values())
    if any_confirmed:
        item1_outcome = "TWO-NODE CONFIRMED"
    elif all_nonpositive:
        item1_outcome = "SINGLE-NULL"
    else:
        item1_outcome = "STILL AMBIGUOUS"
    print(f"\n[Item 1 PRIMARY] any interior point delta_scene>0 AND floor_pass: {any_confirmed}")
    print(f"[Item 1 PRIMARY] all interior points delta_scene<=0: {all_nonpositive}")
    print(f"[Item 1 PRIMARY] all interior points floor_pass=False (entire interior NODE-UNRESOLVABLE): "
          f"{all_floor_fail}")
    print(f"[Item 1 PRIMARY] THREE-WAY OUTCOME = {item1_outcome}")

    # combined ~0.025-0.05deg-step curve across 41.6-42.0deg, for context/printing
    with open(EXP091_RESULTS) as f:
        j091 = json.load(f)
    filed_r3_leg4 = j091["raw"]["r3_leg4_cpl30_steps4200_bracket"]   # includes 41.6
    # Red Team Phase-5 final audit, Fix 1 (exp-093): the interior points and
    # 41.6deg are always native sigma_max=0.5, but 41.8/42.0deg switch to
    # whatever sigma_item1 the branch rule picked (SIGMA_R3_CORRECTED here,
    # since item 3 fired REFUTE) -- tag each point's own sigma_max/
    # comparability explicitly, per-point, rather than one caption that
    # silently goes stale whenever the branch differs from native.
    combined_curve = {}
    for th in ITEM1_ANGLES:
        combined_curve[th] = dict(delta_scene=item1_report[th]["delta_scene"],
                                   sigma_max=sigma_item1, native=(sigma_item1 == SIGMA_NATIVE))
    combined_curve[41.8] = dict(
        delta_scene=item5_report[41.8]["delta_scene"] if sigma_item1 == SIGMA_NATIVE else item3_report[41.8]["sigma_corrected_delta_scene"],
        sigma_max=sigma_item1, native=(sigma_item1 == SIGMA_NATIVE))
    combined_curve[42.0] = dict(
        delta_scene=item5_report[42.0]["delta_scene"] if sigma_item1 == SIGMA_NATIVE else item3_report[42.0]["sigma_corrected_delta_scene"],
        sigma_max=sigma_item1, native=(sigma_item1 == SIGMA_NATIVE))
    if "41.6" in filed_r3_leg4:
        combined_curve[41.6] = dict(delta_scene=filed_r3_leg4["41.6"]["delta_scene"],
                                     sigma_max=SIGMA_NATIVE, native=True)
    print("\n[item 1, context] combined curve, 41.6-42.0deg "
          f"(41.6deg is always native sigma_max=0.5; 41.8/42.0deg follow item 3's own branch -- "
          f"here sigma_max={sigma_item1:.6f} -- "
          f"{'directly comparable to 41.6deg' if sigma_item1 == SIGMA_NATIVE else 'NOT directly comparable to 41.6deg, disclosed per Idealization 11'}; "
          f"interior points always at sigma_max={sigma_item1:.6f}; "
          f"per-point sigma_max/native tags carried in results.json, not asserted uniformly):")
    for th in sorted(combined_curve):
        c = combined_curve[th]
        print(f"  theta={th}: delta_scene={c['delta_scene']:+.6e}  sigma_max={c['sigma_max']:.6f}  native={c['native']}")

    # =================================================================
    # ITEM 2 -- caution-zone re-fit, gated on item 1 (FOURTH, 0 calls)
    # =================================================================
    print("\n" + "=" * 78)
    print("ITEM 2 -- zero-FDTD cpl=30-only caution-zone re-fit, gated on item 1")
    print("=" * 78)

    r3_leg2 = j091["raw"]["r3_leg2_cpl30_steps4200"]
    ITEM2_POINTS = [
        (37.2, "exp-091 Leg 2 (r3_leg2_cpl30_steps4200)"),
        (39.2, "item 5, this cycle (native sigma_max=0.5)"),
        (39.4, "item 5, this cycle (native sigma_max=0.5)"),
        (39.6, "item 5, this cycle (native sigma_max=0.5)"),
        (39.8, "item 5, this cycle (native sigma_max=0.5)"),
        (40.0, "item 5, this cycle (native sigma_max=0.5)"),
        (40.2, "exp-091 Leg 2 (r3_leg2_cpl30_steps4200)"),
        (41.4, "exp-091 Leg 2 (r3_leg2_cpl30_steps4200)"),
    ]
    assert len(ITEM2_POINTS) == 8
    EXP091_SOURCE_ANGLES = {37.2, 40.2, 41.4}

    rows2 = []
    for th, src in ITEM2_POINTS:
        if th in EXP091_SOURCE_ANGLES:
            row = r3_leg2[f"{th:.1f}"]
            fc, rk, fp = row["frac_contrast"], row["ratio_k"], row["floor_pass"]
        else:
            row = item5_report[th]
            fc, rk, fp = row["frac_contrast"], row["ratio_k"], row["floor_pass"]
        assert fp, f"item 2 dataset construction violated -- theta={th} does not floor_pass"
        m = fc / floor
        y = 1 if rk > RATIO_HIGH else 0
        rows2.append(dict(theta=th, source=src, frac_contrast=fc, ratio_k=rk, margin=m, y=y))
    rows2.sort(key=lambda r: r["margin"])

    print("\n[item 2] n=8 cpl=30-only table (sorted by margin):")
    for r in rows2:
        print(f"  theta={r['theta']:6.1f}  margin={r['margin']:8.4f}  ratio_k={r['ratio_k']:9.4f}  "
              f"Y={r['y']}  ({r['source']})")

    zone_base = compute_zone(rows2)
    print(f"\n[Item 2 PRIMARY, base table] n={zone_base['n']} pos={zone_base['pos']} "
          f"AUC(-pos,-neg)={zone_base['auc']:.4f}  zone={zone_base['zone']}  "
          f"inverted={zone_base['inverted']}  Firth beta={zone_base['firth_beta']}  "
          f"m50={zone_base['firth_m50']:.4f}  naive_MLE_diverges={zone_base['naive_mle_diverges']}")

    EXPECTED_ITEM2 = dict(auc=1.0000, zone=[4.1083, 5.4287],
                           firth_beta=[3.76504788, -5.60700572], firth_m50=4.6934)

    def sig4_match(a, b, tol=5e-4):
        return abs(a - b) <= tol

    item2_confirm = True
    item2_confirm &= sig4_match(zone_base["auc"], EXPECTED_ITEM2["auc"])
    item2_confirm &= sig4_match(zone_base["zone"][0], EXPECTED_ITEM2["zone"][0])
    item2_confirm &= sig4_match(zone_base["zone"][1], EXPECTED_ITEM2["zone"][1])
    item2_confirm &= sig4_match(zone_base["firth_beta"][0], EXPECTED_ITEM2["firth_beta"][0])
    item2_confirm &= sig4_match(zone_base["firth_beta"][1], EXPECTED_ITEM2["firth_beta"][1])
    item2_confirm &= sig4_match(zone_base["firth_m50"], EXPECTED_ITEM2["firth_m50"])
    item2_confirm &= (zone_base["inverted"] is False)
    item2_confirm &= (zone_base["naive_mle_diverges"] is True)
    item2_verdict = "CONFIRM" if item2_confirm else "REFUTE"
    print(f"\n[Item 2 PRIMARY] live recomputation vs frozen NOTES.md figures "
          f"(auc=1.0000, zone=[4.1083,5.4287], beta=[3.76504788,-5.60700572], m50=4.6934): "
          f"VERDICT={item2_verdict}")

    # ---- gate on item 1's own outcome (extension only, not the base table)
    item2_extension = dict(gate=item1_outcome)
    interior_floor_clearing = [(th, r) for th, r in item1_report.items() if r["floor_pass"]]
    if item1_outcome == "TWO-NODE CONFIRMED":
        new_rows = []
        for th, r in interior_floor_clearing:
            if r["delta_scene"] <= 0:
                continue   # only the confirming (positive) excursion point(s) extend the table
            m = r["frac_contrast"] / floor
            y = 1 if r["ratio_k"] > RATIO_HIGH else 0
            new_rows.append(dict(theta=th, source="item 1, this cycle (interior, floor-clearing)",
                                  frac_contrast=r["frac_contrast"], ratio_k=r["ratio_k"], margin=m, y=y))
        print(f"\n[Item 2 extension -- TWO-NODE CONFIRMED] new floor-clearing interior point(s): "
              f"{[r['theta'] for r in new_rows]}")
        if len(new_rows) == 1:
            extended_rows = sorted(rows2 + new_rows, key=lambda r: r["margin"])
            zone_extended = compute_zone(extended_rows)
            item2_extension.update(mode="single_point", rows=extended_rows, zone=zone_extended,
                                    provisional=True,
                                    provisional_note=("Idealization 16 -- angular-only, not itself an "
                                                       "R15-grade cross-resolution finding; provisional "
                                                       "pending a future cpl=40 check at the interior "
                                                       "near-null angles specifically."))
            print(f"  extended zone (n={zone_extended['n']}): {zone_extended['zone']}  "
                  f"PROVISIONAL pending cpl=40 check (Idealization 16)")
        elif len(new_rows) > 1:
            each_rows = sorted(rows2 + new_rows, key=lambda r: r["margin"])
            zone_each = compute_zone(each_rows)
            merged_row = dict(theta=[r["theta"] for r in new_rows],
                               source="item 1, this cycle (interior, merged as ONE excursion)",
                               frac_contrast=float(np.mean([r["frac_contrast"] for r in new_rows])),
                               margin=float(np.mean([r["margin"] for r in new_rows])),
                               ratio_k=float(np.mean([r["ratio_k"] for r in new_rows])),
                               y=1 if all(r["y"] == 1 for r in new_rows) else 0)
            pair_rows = sorted(rows2 + [merged_row], key=lambda r: r["margin"])
            zone_pair = compute_zone(pair_rows)
            item2_extension.update(mode="multi_point_side_by_side",
                                    each_independently=dict(rows=each_rows, zone=zone_each),
                                    treat_as_one_excursion=dict(rows=pair_rows, zone=zone_pair),
                                    provisional=True,
                                    provisional_note=("Idealization 16 -- angular-only, not itself an "
                                                       "R15-grade cross-resolution finding; provisional "
                                                       "pending a future cpl=40 check at the interior "
                                                       "near-null angles specifically."))
            print(f"  'each independently' zone (n={zone_each['n']}): {zone_each['zone']}")
            print(f"  'treat as one excursion' zone (n={zone_pair['n']}): {zone_pair['zone']}")
            print("  BOTH readings PROVISIONAL pending cpl=40 check (Idealization 16)")
        else:
            item2_extension.update(mode="no_positive_floor_clearing_point_found_after_all",
                                    note="any_confirmed was True but no positive floor-clearing row "
                                         "survived re-filtering -- internal inconsistency, investigate.")
    elif item1_outcome == "SINGLE-NULL":
        context_rows = [dict(theta=th, delta_scene=r["delta_scene"], floor_pass=r["floor_pass"],
                              y=(1 if r["ratio_k"] > RATIO_HIGH else None) if r["floor_pass"] else None)
                         for th, r in sorted(item1_report.items())]
        item2_extension.update(mode="table_stands_as_built", context_only_rows=context_rows,
                                note=("SINGLE-NULL: item 1's own new interior points, having failed to "
                                      "establish a genuine positive excursion, are reported as context "
                                      "only, not added as zone-defining members."))
        print("\n[Item 2 extension -- SINGLE-NULL] table stands as built; item 1's interior points "
              "reported as context only:")
        for r in context_rows:
            print(f"    theta={r['theta']}: delta_scene={r['delta_scene']:+.6e}  "
                  f"floor_pass={r['floor_pass']}  Y={r['y']}")
    else:
        item2_extension.update(mode="table_stands_as_built_provisional",
                                note=("STILL AMBIGUOUS: table stands as built; explicitly provisional "
                                      "pending item 1's own unresolved interior -- a future denser check "
                                      "could still add a member on either side of the boundary."))
        print("\n[Item 2 extension -- STILL AMBIGUOUS] table stands as built, explicitly flagged "
              "provisional pending item 1's own unresolved interior.")

    # =================================================================
    # ITEM 4 -- Yee-grid dispersion phase-accumulation integral (desk-only)
    # =================================================================
    print("\n" + "=" * 78)
    print("ITEM 4 -- Yee-grid dispersion phase-accumulation integral (mandatory, R8)")
    print("=" * 78)

    ITEM4_ANGLES = [37.2, 40.2, 40.0718, 41.4, 41.7811, 41.8377]
    OBSERVED_SHIFTS = {40.0718: -0.194, 41.7811: +0.320, 41.8377: +0.377}

    # symmetry check theta <-> 90-theta, formula-level property (Idealization 13)
    k_a, _ = yee_dispersion_k(41.4, 30)
    k_b, _ = yee_dispersion_k(90.0 - 41.4, 30)
    symmetry_dev = abs(k_a - k_b)
    print(f"\n[item 4] theta<->90-theta symmetry check: k(41.4)={k_a:.12f}  "
          f"k(48.6)={k_b:.12f}  |diff|={symmetry_dev:.3e}  (formula-level property, Idealization 13)")

    table_A = item4_table(A_HALF_APERTURE_NATIVE, A_HALF_APERTURE_R3, ITEM4_ANGLES)
    table_PAD = item4_table(PAD_NATIVE_ROUNDTRIP, PAD_R3_ROUNDTRIP, ITEM4_ANGLES)

    print(f"\n[item 4, PRIMARY, ell=A_HALF_APERTURE ({A_HALF_APERTURE_NATIVE}/{A_HALF_APERTURE_R3} cells)]:")
    item4_ratios = {}
    for th in ITEM4_ANGLES:
        row = table_A[th]
        line = (f"  theta={th}: Dphi(20)={row['delta_phi_cpl20']:+.4f}deg  "
                f"Dphi(30)={row['delta_phi_cpl30']:+.4f}deg  DDphi={row['delta_delta_phi']:+.4f}deg  "
                f"predicted_Dtheta={row['predicted_dtheta']:+.6f}deg")
        if th in OBSERVED_SHIFTS:
            obs = OBSERVED_SHIFTS[th]
            ratio = abs(obs / row["predicted_dtheta"])
            item4_ratios[th] = ratio
            line += f"  observed={obs:+.3f}deg  ratio={ratio:.1f}x"
        print(line)

    print(f"\n[item 4, secondary, relabeled, ell=2xPAD ({PAD_NATIVE_ROUNDTRIP}/{PAD_R3_ROUNDTRIP} cells)]:")
    item4_ratios_pad = {}
    for th in ITEM4_ANGLES:
        row = table_PAD[th]
        line = (f"  theta={th}: Dphi(20)={row['delta_phi_cpl20']:+.4f}deg  "
                f"Dphi(30)={row['delta_phi_cpl30']:+.4f}deg  DDphi={row['delta_delta_phi']:+.4f}deg  "
                f"predicted_Dtheta={row['predicted_dtheta']:+.6f}deg")
        if th in OBSERVED_SHIFTS:
            obs = OBSERVED_SHIFTS[th]
            ratio = abs(obs / row["predicted_dtheta"])
            item4_ratios_pad[th] = ratio
            line += f"  observed={obs:+.3f}deg  ratio={ratio:.1f}x"
        print(line)

    EXPECTED_RATIOS_A = {40.0718: 32.1, 41.7811: 80.2, 41.8377: 95.8}
    EXPECTED_RATIOS_PAD = {40.0718: 301.8, 41.7811: 754.0, 41.8377: 900.4}

    def pct_match(a, b, tol=0.01):
        return abs(a - b) / abs(b) <= tol

    item4_reproduces = all(pct_match(item4_ratios[th], EXPECTED_RATIOS_A[th]) for th in EXPECTED_RATIOS_A)
    item4_reproduces &= all(pct_match(item4_ratios_pad[th], EXPECTED_RATIOS_PAD[th]) for th in EXPECTED_RATIOS_PAD)
    item4_band_holds = all(10.0 <= item4_ratios[th] <= 200.0 for th in item4_ratios)
    item4_verdict = "CONFIRM" if (item4_reproduces and item4_band_holds) else "REFUTE of the 10x-200x band"
    print(f"\n[Item 4 PRIMARY] reproduces NOTES.md table to expected precision: {item4_reproduces}")
    print(f"[Item 4 PRIMARY] magnitude ratio stays in [10x,200x] at all 3 known-shift angles: "
          f"{item4_band_holds}  (ratios: {item4_ratios})")
    print(f"[Item 4 PRIMARY] VERDICT={item4_verdict}  -- REFUTEs the dispersion-alone mechanism by at "
          f"least one clear order of magnitude (not the pre-freeze draft's mistaken two-order claim)")

    total_wall_all = time.time() - t_start

    # ---------------------------------------------------------------- disclosures (printed AND persisted)
    netd_disclaimer = ("NETD is an instrument/detector threshold, not a human perceptual one -- "
                        "does NOT bear on constraint-3/4's human-eye verdict. (Idealization 3)")
    scope_note = ("This cycle is pure instrument recalibration and energy-sidecar instrumentation "
                   "(T1 route N/A, Checkpoint criterion 2 N/A) -- no phenomenon-mechanism claim, "
                   "REALIZABILITY_MEMO.md untouched. (Idealization 7)")
    sigma_branch_disclaimer = ("A Rank-3-style REFUTE/NEITHER-default (item 3's own verdict) reopens "
                                "item 1's own net-placement/sigma choice as provisional for a future "
                                "cycle -- resequencing fixes which article item 1's 24 calls measure; "
                                "it does not, by itself, revalidate whether the flanking anchor points "
                                "remain directly comparable if item 3 fires REFUTE/NEITHER. (Idealization 11)")
    r15_disclaimer = ("Items 1/2 are a further, cpl=30-verified STEP toward R15's founding mandate -- "
                       "NOT its completion. Two discharge conditions remain open: three of exp-090's "
                       "seven original points (36.0deg, 38.4deg, 38.8deg) still have no cpl=30 "
                       "measurement, and no cpl=40 comparator exists anywhere on this channel to confirm "
                       "cpl=30 itself is converged rather than merely a second, different, fixed "
                       "resolution.")
    print(f"\n[disclosure] netd_disclaimer: {netd_disclaimer}")
    print(f"[disclosure] scope_note: {scope_note}")
    print(f"[disclosure] sigma_branch_disclaimer: {sigma_branch_disclaimer}")
    print(f"[disclosure] r15_disclaimer: {r15_disclaimer}")

    # ---------------------------------------------------------------- persist
    def th_key(d):
        return {str(k): v for k, v in d.items()}

    out = dict(
        total_fdtd_calls=28 + 4 + 24, item5_calls=28, item3_calls=4, item1_calls=24,
        item2_calls=0, item4_calls=0,
        item5_wall_s=wall5, item3_wall_s=wall3, item1_wall_s=wall1,
        total_fdtd_wall_time_s=total_wall, total_wall_time_s=total_wall_all,
        sigma_native=SIGMA_NATIVE, sigma_r3_corrected=SIGMA_R3_CORRECTED,
        r13_floor_gate=dict(floor=floor, rms_frac_contrast=rms, n_window_points=n83),
        vacuum_footprint_check=vac_report, vac_pass=vac_pass,
        xi_pass=xi_pass, nonneg_pass=nonneg_pass,
        item5=dict(
            verdict=item5_verdict,
            angles=RANK1_ANGLES,
            per_theta=th_key(item5_report),
            consistency_check_vs_exp092_filed=consistency_check,
            consistency_all_match=consistency_all_match,
        ),
        item5b=dict(
            predicted_range_K=[item5b_lo, item5b_hi],
            surprises=item5b_surprises,
            note="dt_ss_full_K/netd_classification for all 14 (config,angle) cells are inside "
                 "item5.per_theta's own per-theta rows above (both _c and _g variants), not "
                 "truncated (Iteration-69 LOGBOOK defect, closed here).",
        ),
        item3=dict(
            angles=ITEM3_ANGLES,
            verdict=item3_verdict, delta_scene_sub_verdict=ds_verdict, frac_contrast_sub_verdict=fc_verdict,
            item3b_verdict=item3b_verdict,
            per_theta=th_key(item3_report),
        ),
        sigma_branch=dict(chosen_sigma_max=sigma_item1, reason=branch_reason),
        item1=dict(
            angles=ITEM1_ANGLES, sigma_max=sigma_item1,
            per_theta=th_key(item1_report),
            any_new_confirmed_excursion=any_confirmed, all_new_nonpositive=all_nonpositive,
            all_new_floor_fail=all_floor_fail,
            outcome=item1_outcome,
            combined_curve_41_6_to_42_0=th_key(combined_curve),
        ),
        item2=dict(
            base_table=rows2, base_zone=zone_base, base_verdict=item2_verdict,
            expected=EXPECTED_ITEM2,
            extension=item2_extension,
            r15_disclaimer=r15_disclaimer,
        ),
        item4=dict(
            courant_frac=COURANT_FRAC, S=S_COURANT,
            A_half_aperture_native=A_HALF_APERTURE_NATIVE, A_half_aperture_r3=A_HALF_APERTURE_R3,
            pad_roundtrip_native=PAD_NATIVE_ROUNDTRIP, pad_roundtrip_r3=PAD_R3_ROUNDTRIP,
            p_star_deg=P_STAR_DEG,
            symmetry_check=dict(theta=41.4, k_theta=k_a, k_90_minus_theta=k_b, abs_diff=symmetry_dev),
            table_ell_A=th_key(table_A), table_ell_pad=th_key(table_PAD),
            ratios_ell_A=item4_ratios, ratios_ell_pad=item4_ratios_pad,
            expected_ratios_ell_A=EXPECTED_RATIOS_A, expected_ratios_ell_pad=EXPECTED_RATIOS_PAD,
            band_10x_200x_holds=item4_band_holds, reproduces_notes_table=item4_reproduces,
            verdict=item4_verdict,
        ),
        netd_disclaimer=netd_disclaimer,
        scope_note=scope_note,
        sigma_branch_disclaimer=sigma_branch_disclaimer,
        r15_disclaimer=r15_disclaimer,
    )
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote {out_path}")

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"  Item 5 (NETD backfill, reproduction):  {item5_verdict}")
    print(f"  Item 3 (sigma_max, near-null):         {item3_verdict}  (item3b info: {item3b_verdict})")
    print(f"  Item 1 (three-way outcome):            {item1_outcome}")
    print(f"  Item 2 (n=8 zone base table):          {item2_verdict}  (extension gate: {item1_outcome})")
    print(f"  Item 4 (dispersion, 10x-200x band):    {item4_verdict}")
    print(f"  total FDTD calls: {out['total_fdtd_calls']}   total wall time: {total_wall_all:.1f}s "
          f"({total_wall_all/60.0:.2f} min)")

    return out


if __name__ == "__main__":
    main()
