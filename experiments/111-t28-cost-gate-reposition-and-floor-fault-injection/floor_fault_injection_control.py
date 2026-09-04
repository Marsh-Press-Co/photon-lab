"""exp-111 -- Panel Iteration 88 (THERMODYNAMICS' rotation-lead cycle):
fault-injection control for mirror_pooled_floor/classify_item_i_local
(Reconciled Iteration-88 Tier-1 item 1). Zero Sim.run() calls anywhere in
this file -- all four synthetic cases plus the non-regression check are
deterministic numpy arithmetic or a direct read of exp-110's own already-
committed results.json.

Cases (phase1_proposal.md Sec 2.1, mandatory fixes 3/6 of
phase2_redteam_audit.md Sec 5):
  FI-A -- injected ASYMMETRIC/odd perturbation: floor should recover it.
  FI-B -- injected SYMMETRIC/common-mode perturbation, 2x FI-A's magnitude:
          floor should read exactly 0.0 (the disclosed blind spot).
  FI-C -- genuinely degenerate, fully mirror-symmetric input: floor==0.0
          exactly; post-fix, floor_degenerate=True, resolved=[False]*48,
          and (mandatory-fix 3, QUANTUM's own Phase-2 finding)
          local_snr_peccored/local_snr_hollow must NOT be inf in this case.
  FI-D -- PHOTONICS' own recommended addition (phase2_redteam_audit.md
          Sec 3/5 item 6): a swept-phase quasi-periodic perturbation at
          this bench's own established T28 period P*=2.8421 deg, aliased
          against this instrument's 7.5deg/bin pitch -- neither a clean
          odd nor even case. Narrows (not replaces) the "closes the last
          open R18 gap" claim: R18's own literal text requires only a
          positive/negative control (FI-A/FI-B satisfy it), so FI-D is
          informational, strengthening evidence, not a blocking gate.
  Non-regression -- the patched classify_item_i_local() re-run against all
          12 real (r, margin) cells already committed in exp-110's own
          results.json: floor_degenerate must be False everywhere (all 12
          real floors are strictly positive) and n_resolved must be
          bit-identical to the frozen dicts.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "experiments", "110-t28-item-i-local-norm-and-controls"))

import run as R  # noqa: E402  (exp-110's own, patched this cycle)

EXP110_DIR = os.path.join(ROOT, "experiments", "110-t28-item-i-local-norm-and-controls")
with open(os.path.join(EXP110_DIR, "results.json")) as f:
    EXP110_RESULTS = json.load(f)

N_BINS = 48
BIN_CENTERS_DEG = np.array([-180.0 + 3.75 + 7.5 * i for i in range(N_BINS)])  # matches analyze.py's own convention
P_STAR_DEG = 2.8421  # T28's own established boundary-echo period (LOGBOOK T28)


def fi_a():
    """Asymmetric/odd perturbation: recovers exactly."""
    baseline = 5.0e-3
    p = 5.0e-4
    arr = np.full(N_BINS, baseline)
    for k in range(N_BINS // 2):
        i, j = k, N_BINS - 1 - k
        arr[i] = baseline + p
        arr[j] = baseline - p
    floor = R.mirror_pooled_floor(arr)
    predicted = p
    ok = abs(floor - predicted) < 1e-12
    return dict(case="FI-A", floor=floor, predicted=predicted, pass_=bool(ok))


def fi_b():
    """Symmetric/common-mode perturbation, 2x FI-A's magnitude: floor reads 0."""
    baseline = 5.0e-3
    q = 1.0e-3  # 2x FI-A's p
    arr = np.full(N_BINS, baseline + q)
    floor = R.mirror_pooled_floor(arr)
    predicted = 0.0
    ok = abs(floor - predicted) < 1e-12
    return dict(case="FI-B", floor=floor, predicted=predicted, pass_=bool(ok), injected_magnitude=q)


def fi_c():
    """Genuinely degenerate, fully mirror-symmetric peccored+hollow pair.
    Both quadratic in (i-23.5)^2, exactly invariant under i<->47-i."""
    i_arr = np.arange(N_BINS, dtype=float)
    peccored = 3.0e-3 + 1.0e-6 * (i_arr - 23.5) ** 2
    hollow = 1.5e-3 + 4.0e-7 * (i_arr - 23.5) ** 2
    delta = peccored - hollow

    floor_p = R.mirror_pooled_floor(peccored)
    floor_h = R.mirror_pooled_floor(hollow)

    diag = R.classify_item_i_local(r=999, margin=999, pattern_peccored=peccored,
                                    pattern_hollow=hollow, pattern_delta=delta)

    all_unresolved = all(v is False for v in diag["resolved"])
    no_inf_snr = (not any(np.isinf(v) for v in diag["local_snr_peccored"])
                  and not any(np.isinf(v) for v in diag["local_snr_hollow"]))
    ok = (floor_p == 0.0 and floor_h == 0.0 and diag["floor_degenerate"] is True
          and all_unresolved and no_inf_snr)
    return dict(case="FI-C", floor_peccored_pooled=floor_p, floor_hollow_pooled=floor_h,
                floor_degenerate=diag["floor_degenerate"],
                resolved_all_false=all_unresolved,
                local_snr_peccored_sample=diag["local_snr_peccored"][:3],
                local_snr_hollow_sample=diag["local_snr_hollow"][:3],
                no_inf_snr=no_inf_snr, pass_=bool(ok))


def fi_d():
    """PHOTONICS' own recommended addition: swept-phase quasi-periodic
    perturbation at P*=2.8421 deg, aliased against this instrument's
    7.5deg/bin pitch. Informational -- demonstrates the floor's recovered
    magnitude is phase-DEPENDENT for this realistic, neither-clean-odd-
    nor-clean-even shape, unlike FI-A (always fully recovers) and FI-B
    (always exactly zero)."""
    amplitude = 5.0e-4  # same scale as FI-A's injected p
    baseline = 5.0e-3
    n_phases = 24
    phases_deg = np.linspace(0.0, 360.0, n_phases, endpoint=False)
    floors = []
    for phase_deg in phases_deg:
        arr = baseline + amplitude * np.cos(2 * np.pi * BIN_CENTERS_DEG / P_STAR_DEG
                                             + np.deg2rad(phase_deg))
        floors.append(R.mirror_pooled_floor(arr))
    floors = np.array(floors)
    floor_min, floor_max = float(np.min(floors)), float(np.max(floors))
    spread = floor_max - floor_min
    # Falsifiable prediction (phase1_proposal.md/Red Team addendum, informational):
    # the recovered floor is NOT constant across phase (unlike FI-A/FI-B's
    # clean extremes) -- i.e. spread must be non-negligible relative to
    # amplitude, and no swept phase drives the floor to exactly 0.0 or
    # exactly amplitude (P* is incommensurate with the 7.5deg pitch, so no
    # exact cancellation/alignment is expected at any tested phase).
    non_constant = bool(spread > 0.01 * amplitude)
    never_exactly_zero = bool(np.all(floors > 1e-12))
    never_exactly_full = bool(np.all(floors < amplitude - 1e-12))
    return dict(case="FI-D", amplitude=amplitude, n_phases=n_phases,
                floor_min=floor_min, floor_max=floor_max, spread=spread,
                floor_min_over_amplitude=floor_min / amplitude,
                floor_max_over_amplitude=floor_max / amplitude,
                non_constant=non_constant, never_exactly_zero=never_exactly_zero,
                never_exactly_full=never_exactly_full,
                pass_=bool(non_constant and never_exactly_zero and never_exactly_full))


def non_regression():
    """Re-run the PATCHED classify_item_i_local() against all 12 real
    (r, margin) cells already committed in exp-110's own results.json.
    floor_degenerate must be False everywhere; n_resolved must be
    bit-identical to the frozen dicts."""
    rows = []
    all_ok = True
    for r_key, r_val in (("r156", 156), ("r312", 312)):
        raw_patterns = EXP110_RESULTS[r_key]["raw_patterns"]
        frozen_n_resolved = EXP110_RESULTS[r_key]["n_resolved"]
        for margin_str, patt in raw_patterns.items():
            margin = int(margin_str)
            pat_p = np.array(patt["peccored"])
            pat_h = np.array(patt["hollow"])
            pat_d = np.array(patt["delta"])
            diag = R.classify_item_i_local(r=r_val, margin=margin,
                                            pattern_peccored=pat_p, pattern_hollow=pat_h,
                                            pattern_delta=pat_d)
            frozen_n = frozen_n_resolved[margin_str]
            match = (diag["n_resolved"] == frozen_n) and (diag["floor_degenerate"] is False)
            all_ok = all_ok and match
            rows.append(dict(r=r_val, margin=margin, floor=diag["floor"],
                              floor_degenerate=diag["floor_degenerate"],
                              n_resolved=diag["n_resolved"], frozen_n_resolved=frozen_n,
                              match=bool(match)))
    return dict(rows=rows, all_match=bool(all_ok), n_cells=len(rows))


if __name__ == "__main__":
    results = dict(fi_a=fi_a(), fi_b=fi_b(), fi_c=fi_c(), fi_d=fi_d(),
                    non_regression=non_regression())
    for k in ("fi_a", "fi_b", "fi_c", "fi_d"):
        print(f"{k}: {json.dumps(results[k], default=str)}")
    print(f"non_regression: all_match={results['non_regression']['all_match']} "
          f"n_cells={results['non_regression']['n_cells']}")
    out_path = os.path.join(HERE, "floor_fault_injection_control_output.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"Written: {out_path}")

    all_pass = (results["fi_a"]["pass_"] and results["fi_b"]["pass_"]
                and results["fi_c"]["pass_"] and results["fi_d"]["pass_"]
                and results["non_regression"]["all_match"])
    print(f"\nALL CASES PASS: {all_pass}")
    assert all_pass, "floor_fault_injection_control: at least one case failed"
