"""exp-073 -- MATERIALS' corrected re-issue of exp-072's differential/beat fit
of `delta_AB(theta)` (T28), behind the new `G0-e` ground-truth recovery gate.
=============================================================================
Panel Iteration 50 (lead: MATERIALS, by rotation). Executes PLAN.md's
Iteration-50 queue item 1, unanimous across all six of exp-072's Phase-5
seats (`experiments/072-t28-differential-beat-fit/phase5_redteam_audit.md`
Sec 7.2). Phase-2 Red Team audit verdict: PROCEED-WITH-MANDATORY-FIXES,
12 items, ZERO items overridden -- every diagnosis and, where offered, remedy
from all five blind critiques was independently re-verified and adopted (the
one exception -- QUANTUM's own two candidate null-construction fixes -- is a
REFINEMENT of QUANTUM's own already-hedged position, not a reversal: neither
fix was independently found to reliably clear G0-e(ii)'s own calibration
bands, so the audit keeps G0-e(ii) as a binding, non-relaxable HALT rather
than mandating either). See `phase3_synthesis.md` for the Director's full
accept/override record and the two genuine implementation-level ambiguities
this file's own development surfaced (neither anticipated by the docket) --
`phase2_redteam_audit.md` Sec 5 is the single source of truth for every
gate/threshold; this docstring summarizes, it does not redefine.

THIS FILE STARTS FROM exp-072's OWN CORRECTED, POST-FIX `run.py` (the
already-published, already-Phase-5-verified version) AS ITS BASE, per the
Director's own scoping instruction -- `load_data`, `_amp_phase_at`,
`carrier_fit`, `design_matrix`, `holm_adjust`, and the design-respecting
bootstrap are REUSED VERBATIM (class (c), inherited machinery, independently
re-verified this cycle by ELECTROMAGNETISM from first principles -- see
`phase2_critique_em.md` Sec 1 -- not re-derived here). What changed, and why
each change is data-free-justified, is documented inline at each block
(search "docket item N").

PRE-REGISTRATION CONTAMINATION DISCLOSURE (Red Team's Phase-2 audit Sec 3,
binding, reproduced here per its own condition 1 -- docket items 9-11).
This extends, rather than repeats, exp-072's own Sec 4 ruling: it addresses a
NEW form of the same risk, arising specifically because this cycle's mandate
is a re-issue of UNCHANGED machinery on UNCHANGED data. Because exp-073's
carrier-fit and ramped-differential-OLS machinery is bit-identical to
exp-072's own already-committed, already-published `run.py`, applied to the
identical 124-point substrate, every real per-pair point estimate this
cycle's Phase 4 will produce -- T_mean, a_cbar, psi_bar, A_i, A_q, R_i, R_q,
Delta_f, |Delta_f|*X, and Delta_P (including its sign) -- is ALREADY
computable, bit-exact, from `experiments/072-.../results.json`, and was in
fact independently computed, for the A_q/chi0 channel, by this cycle's own
EM critique (see `phase2_critique_em.md`). Ruling (Red Team's audit Sec 3,
applying exp-072's own condition-1 test): NOT outcome-determining for the
Combined Verdict as specified -- none of exp-073's three new-machinery items
(T2-1's admissibility gate, T2-3's null, T2-4's coefficient-table relabeling)
were tuned in response to these now-known numbers; all three are justified
purely by data-free arguments (algebraic identities, leakage-minimization
over the search range, a trigonometric identity), independently re-verified
in `phase2_redteam_audit.md` Attacks 1-5. The one place a real, previously-
closed number enters this document's own argument (EM's chi0 correction,
docket item 5) touches an explicitly NON-GATING quantity (no Combined-Verdict
branch reads A_q or chi0). THREE BINDING CONDITIONS (docket items 9-11,
implemented here as code/data, not only prose):
  (9) This disclosure paragraph itself, extended beyond the A_q/chi0 channel
      EM's critique surfaced to cover every real per-pair point estimate --
      stated once, here, and echoed in NOTES.md/phase3_synthesis.md.
  (10) FORWARD LOCK: any change to a gate, band, or threshold made from
       Red Team's Phase-2 audit forward, for any reason traceable to
       exp-072's known real numbers, must be treated as a fresh Phase-1/2
       pre-registration decision, never folded into a same-cycle Phase-3
       correction. No such change was made anywhere in this file --
       `T_WRONG_DISPLACED`, `SAT_DECAY_L`, `N_GRID_CARRIER`, `HOLM_PAIRS`,
       the Holm alpha, the G0-e(i)/G0-e(ii) sweep ranges, and every
       Combined-Verdict threshold are all inherited unmodified from
       data-free derivations (exp-072's own, or this cycle's own window-
       geometry/leakage-minimization arithmetic).
  (11) If Phase 4 reaches a CONFIRM-shaped outcome on ANY pair, this
       disclosure must additionally travel into `phase4_results.md` --
       wired here as `results["contamination_disclosure"]`, computed
       automatically from the Combined Verdict so a future Phase-4 report
       generator cannot omit it by oversight. See `_contamination_block()`.

Zero FDTD calls. Zero `lab/` diff.
"""

import json
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)
EXP069 = os.path.join(ROOT, "experiments", "069-t21-block-mini-period-match-power-up")
EXP071 = os.path.join(ROOT, "experiments", "071-t28-absorb-depth-causal-test")
EXP072 = os.path.join(ROOT, "experiments", "072-t28-differential-beat-fit")
sys.path.insert(0, EXP069)

import run as exp069_run  # noqa: E402  (reuse _fixed_period_fit verbatim)

_fixed_period_fit = exp069_run._fixed_period_fit

# ===================================================== frozen constants
# All inherited unmodified from exp-072's own data-free derivations
# (phase2_redteam_audit.md Sec 5, "Unchanged, independently re-verified
# sound, no fix required") -- the forward-lock condition (10, above) means
# NONE of these may move for any reason traceable to exp-072's known real
# numbers.
CENTER_DEG = 39.0
SEED = 20490073                # distinct from exp-072's 20490072
SEED_CALIB = 20490173          # distinct from SEED (G0-e(ii)'s own text:
                                # "distinct from the real-data null's seed")
N_SURR = 20000                 # primary sign-flip gating null (T2-3)
N_SURR_Q95 = 2000              # carrier-consistency-gate calibration --
                                # a documented computational economy,
                                # inherited from exp-072 item 6: the q95
                                # calibration needs a smooth percentile, not
                                # a sharp p-value.
N_GRID_Q95 = 300               # ditto, per-surrogate free-period search
N_GRID_CARRIER = 3000          # step-1 common-mode carrier search
HOLM_PAIRS = ("C40-C60", "C60-C70", "C70-C80")  # 3 algebraically free
T_WRONG_DISPLACED = 1.2591     # deg -- unchanged from exp-072's own
                                # Phase-5-corrected value (>=2.36 Rayleigh
                                # widths, 36x-lower leakage than the
                                # original 3.60deg draft). Re-verified this
                                # cycle (phase2_redteam_audit.md, "Unchanged"
                                # list): data-free, no fix required.
T_WRONG_FRINGE = 1.9608        # deg, T21's established fringe -- disclosure
                                # only, 0.6452 Rayleigh widths, NOT a control
SAT_DECAY_L = 0.075            # 1/cell, engine-derived, FIXED not fitted

PAIRS = [
    ("C40", "C60", 20.0),
    ("C60", "C70", 10.0),
    ("C70", "C80", 10.0),
    ("C40", "C80", 40.0),   # derived (= sum of the other three, G0-b) --
                             # never called "independently measured"
]


# ===================================================== data loading (G0-a/b/c)
def load_data():
    """Reuses exp-072's own load_data() verbatim, PLUS docket item 6: also
    loads exp-072's own already-committed `saturating_vs_linear.linear.slope`
    (the n_grid=3000-resolved slope) as the primary rate reference, carrying
    exp-071's own n_grid=400 slope (`m0_native`) alongside only as the
    historical/Iteration-48-native anchor (never as the operative reference).
    Both are loaded at runtime -- neither is ever hand-typed (R4)."""
    with open(os.path.join(EXP069, "results.json")) as f:
        d069 = json.load(f)
    with open(os.path.join(EXP071, "results.json")) as f:
        d071 = json.load(f)
    with open(os.path.join(EXP072, "results.json")) as f:
        d072 = json.load(f)

    rows069 = {r["theta"]: r for r in d069["block_dense"]["rows"]}
    theta069 = sorted(rows069)
    c40 = np.array([rows069[t]["C_empty_C40"] for t in theta069])
    c80 = np.array([rows069[t]["C_empty_C80"] for t in theta069])
    delta_committed = np.array([rows069[t]["delta"] for t in theta069])

    theta_c60 = [r["theta"] for r in d071["dense_causal"]["rows"]["C60"]]
    theta_c70 = [r["theta"] for r in d071["dense_causal"]["rows"]["C70"]]
    c60 = np.array([r["C_empty"] for r in d071["dense_causal"]["rows"]["C60"]])
    c70 = np.array([r["C_empty"] for r in d071["dense_causal"]["rows"]["C70"]])

    theta = np.array(theta069, dtype=float)

    g0a = dict(
        n_checked=3,
        all_identical=bool(
            np.array_equal(theta, np.array(theta_c60))
            and np.array_equal(theta, np.array(theta_c70))
        ),
    )
    g0b_lhs = (c60 - c40) + (c70 - c60) + (c80 - c70)
    g0b_rhs = c80 - c40
    g0b = dict(max_abs_residual=float(np.max(np.abs(g0b_lhs - g0b_rhs))))
    g0c = dict(max_abs_delta=float(np.max(np.abs(delta_committed - (c80 - c40)))))

    m0_native = d071["trend"]["linear_fit"]["slope"]          # n_grid=400
    m0_resolved = d072["saturating_vs_linear"]["linear"]["slope"]  # n_grid=3000
    m0_resolved_r2 = d072["saturating_vs_linear"]["linear"]["r_squared"]
    per_config_free_native = d071["per_config_free_periods"]

    # class-(b) disclosure only (docket item 5): exp-072's own already-closed,
    # non-contaminating real chi0/A_q/amplitude values, loaded here so the
    # "binds hard" correction is programmatically sourced, never hand-typed
    # -- NEVER referenced by any gate or threshold below (contamination
    # ruling condition 3/forward lock, docket items 9-10).
    exp072_disclosure = {}
    for k, p in d072["scored"]["per_pair"].items():
        chi0 = math.atan2(p["A_q"], 2.0 * p["amplitude"]) if p["amplitude"] != 0 else float("nan")
        exp072_disclosure[k] = dict(
            A_q=p["A_q"], amplitude=p["amplitude"], chi0_real=chi0,
            tan_over_sin=(math.tan(chi0) / math.sin(chi0)) if math.sin(chi0) != 0 else float("nan"),
        )

    return dict(
        theta=theta, C40=c40, C60=c60, C70=c70, C80=c80,
        m0_native=float(m0_native),
        m0_resolved=float(m0_resolved), m0_resolved_r2=float(m0_resolved_r2),
        per_config_free_native=per_config_free_native,
        g0a=g0a, g0b=g0b, g0c=g0c,
        exp072_disclosure=exp072_disclosure,
    )


# ===================================================== step 1: carrier fit
# Inherited, class (c) -- verbatim from exp-072's post-fix `run.py`,
# independently re-derived from scratch this cycle (phase2_critique_em.md
# Sec 1) and confirmed exact. No code change.
def _amp_phase_at(theta_deg, series, T_x, xbar):
    """Fit series = c0 + a*cos(w*u) + b*sin(w*u), u = sin(theta)-xbar, T_x
    FIXED -- fit directly in u-space so the returned phase is usable as
    design_matrix()'s `psi` with no extra w*xbar correction (the exp-072
    Phase-3 self-catch: fitting in raw x and reusing atan2(b,a) as a
    u-domain phase needs a w*xbar shift first)."""
    x = np.sin(np.radians(theta_deg))
    u = x - xbar
    fit = _fixed_period_fit(u, series, T_x)
    amp = math.hypot(fit["a"], fit["b"])
    psi = -math.atan2(fit["b"], fit["a"])
    return amp, psi, fit["c0"]


def carrier_fit(theta_deg, series_a, series_b, n_grid=N_GRID_CARRIER):
    """Free-period search + fixed fit on the common-mode Cbar = (A+B)/2."""
    cbar = 0.5 * (series_a + series_b)
    free = exp069_run._free_period_search(theta_deg, cbar, center_deg=CENTER_DEG,
                                           n_grid=n_grid)
    T_mean_deg = free["p_star_deg"]
    cos_c = math.cos(math.radians(CENTER_DEG))
    T_x = math.radians(T_mean_deg) * cos_c
    xbar = float(np.mean(np.sin(np.radians(theta_deg))))
    amp, psi, _ = _amp_phase_at(theta_deg, cbar, T_x, xbar)
    return dict(T_mean_deg=T_mean_deg, T_x=T_x, amplitude=amp, psi=psi,
                r_squared=free["r_squared"])


def design_matrix(theta_deg, T_x, psi, xbar, curvature=False):
    """5-column ramped basis [1, cos(theta_c), -sin(theta_c), u*cos(theta_c),
    -u*sin(theta_c)] at a FIXED carrier (T_x, psi) -- the frozen basis,
    inherited unchanged (class c). `A_q` (coeff of -sin) reads, exactly,
    as `2*a_cbar*tan(chi0)` (docket item 5/T2-4, EM's exact re-derivation,
    phase2_critique_em.md Sec 1) -- a trigonometric identity, not a fitted
    correction, and requires NO code change here: the OLS-fitted A_q
    coefficient is the same number under either interpretation."""
    x = np.sin(np.radians(theta_deg))
    u = x - xbar
    w = 2 * math.pi / T_x
    theta_c = w * u + psi
    cols = [np.ones_like(x), np.cos(theta_c), -np.sin(theta_c),
            u * np.cos(theta_c), -u * np.sin(theta_c)]
    if curvature:
        cols.append(u * u * (-np.sin(theta_c)))
    return np.column_stack(cols)


def _sign(v):
    return 0 if v == 0 else (1 if v > 0 else -1)


def _sign_match(a, b):
    """Sign agreement, treating either operand being exactly zero as
    uninformative (neutral -- does not break agreement)."""
    return (a == 0) or (b == 0) or (_sign(a) == _sign(b))


def two_sided_p(obs, surr):
    return float((1 + np.sum(np.abs(surr) >= abs(obs))) / (len(surr) + 1))


def one_sided_p_ge(obs, surr):
    return float((1 + np.sum(surr >= obs)) / (len(surr) + 1))


# ===================================================== T2-3: sign-flip null
# Replaces exp-072's phase-randomized H0-residual null (QUANTUM's own
# exp-072 Phase-5 catch: that null cannot remove a component its own basis
# excludes, so phase-randomizing it leaves true ramp signal in the
# surrogate pool -- conservative, not correctly sized). Freedman-Lane-style:
# sign-flip the FULL 5-column residual (which, by construction, has the
# ramp component fit out regardless of its true size), add back the
# 4-column H0-fit prediction, refit. E[R_q^surr]=0 exactly (EM's algebraic
# proof, phase2_critique_em.md Sec 3, independently re-verified in
# phase2_redteam_audit.md Attack 4) -- but Attack 4 ALSO independently
# reproduced QUANTUM's finding that this construction's VARIANCE is
# anti-conservative (2-6x nominal), a leverage effect. Per Red Team's
# ruling (Attack 4): keep the literal construction, unmodified, and let
# G0-e(ii) -- a binding, non-relaxable HALT -- catch it if it fires.
def sign_flip_surrogates(y, X5, X4, n_surr, rng):
    pinv5 = np.linalg.pinv(X5)
    pinv4 = np.linalg.pinv(X4)
    coef5 = pinv5 @ y
    yhat0 = X4 @ (pinv4 @ y)
    resid5 = y - X5 @ coef5
    n = len(y)
    S = rng.choice(np.array([-1.0, 1.0]), size=(n, n_surr))
    surr = yhat0[:, None] + resid5[:, None] * S
    return surr, pinv5, resid5, yhat0


def residual_permutation_surrogates(y, X5, X4, n_surr, rng):
    """Disclosed cross-check only (T2-3, non-gating): permute resid5's
    order instead of sign-flipping it."""
    pinv5 = np.linalg.pinv(X5)
    pinv4 = np.linalg.pinv(X4)
    coef5 = pinv5 @ y
    yhat0 = X4 @ (pinv4 @ y)
    resid5 = y - X5 @ coef5
    n = len(y)
    surr = np.empty((n, n_surr))
    for j in range(n_surr):
        surr[:, j] = yhat0 + rng.permutation(resid5)
    return surr, pinv5


def holm_adjust(pvals, m=None):
    """Holm-Bonferroni step-down over the 3 algebraically-free pairs."""
    names = list(pvals)
    m = m or len(names)
    order = sorted(names, key=lambda k: pvals[k])
    adj = {}
    running_max = 0.0
    for i, name in enumerate(order):
        raw = pvals[name]
        val = min(1.0, (m - i) * raw)
        running_max = max(running_max, val)
        adj[name] = running_max
    return adj


def carrier_q95(theta_deg, delta_ab, X5, X4, T_x, rng,
                n_surr=N_SURR_Q95, n_grid=N_GRID_Q95):
    """Docket item 7(a): the self-contained per-carrier admissibility
    statistic's own q95, computed in-run from the PAIR's own sign-flip
    surrogate ensemble (no forward reference to any undefined "G-gate
    table"). Generalizes exp-072's own clause-(iv) construction (there
    computed only for T_delta) so it can gate BOTH T_delta (clause iv)
    AND T_wrong=1.2591deg (clause vi) against the SAME calibrated
    percentile -- see phase3_synthesis.md for the documented judgment call
    this generalization required (there is no unique way to define a
    "per-candidate" q95 without either (a) re-anchoring the null at each
    candidate separately, at several times the compute cost, or (b) sharing
    one q95 calibrated at the pair's own fitted (T_mean, psi_bar), applied
    identically to every candidate's own admissibility test -- (b) is what
    Red Team's own Attack 5b used as its quantitative proxy and is adopted
    here, disclosed explicitly, not silently)."""
    surr, _, _, _ = sign_flip_surrogates(delta_ab, X5, X4, n_surr, rng)
    x = np.sin(np.radians(theta_deg))
    cos_c = math.cos(math.radians(CENTER_DEG))
    grid = np.linspace(1.0, 4.0, n_grid)
    Tx_grid = np.radians(grid) * cos_c
    w_grid = 2 * math.pi / Tx_grid
    n = len(theta_deg)
    best_r2 = np.full(surr.shape[1], -np.inf)
    best_Tx = np.full(surr.shape[1], np.nan)
    for gi in range(n_grid):
        Xg = np.column_stack([np.ones(n), np.cos(w_grid[gi] * x), np.sin(w_grid[gi] * x)])
        Hg = Xg @ np.linalg.pinv(Xg)
        yhat = Hg @ surr
        ss_res = np.sum((surr - yhat) ** 2, axis=0)
        ss_tot = np.sum((surr - surr.mean(axis=0, keepdims=True)) ** 2, axis=0)
        r2 = 1.0 - ss_res / np.where(ss_tot > 0, ss_tot, np.nan)
        better = r2 > best_r2
        best_r2 = np.where(better, r2, best_r2)
        best_Tx = np.where(better, Tx_grid[gi], best_Tx)
    stat = np.abs(best_Tx - T_x) / T_x
    return float(np.nanpercentile(stat, 95))


# ===================================================== one pair, full pipeline
def analyze_pair(data, key_a, key_b, d_absorb, rng):
    theta = data["theta"]
    series_a, series_b = data[key_a], data[key_b]
    delta_ab = series_b - series_a
    n = len(theta)

    # ---- step 1: common-mode carrier (inherited unchanged)
    carrier = carrier_fit(theta, series_a, series_b)
    T_x, psi = carrier["T_x"], carrier["psi"]
    x = np.sin(np.radians(theta))
    xbar = float(np.mean(x))
    u = x - xbar
    cos_c = math.cos(math.radians(CENTER_DEG))

    # ---- step 2: 5-column ramped fit + disclosed 6th curvature column
    X5 = design_matrix(theta, T_x, psi, xbar, curvature=False)
    X6 = design_matrix(theta, T_x, psi, xbar, curvature=True)
    pinv5 = np.linalg.pinv(X5)
    coef5 = pinv5 @ delta_ab
    cond5 = float(np.linalg.cond(X5))
    coef6 = np.linalg.pinv(X6) @ delta_ab
    cond6 = float(np.linalg.cond(X6))
    c0, A_i, A_q, R_i, R_q = (float(v) for v in coef5)

    amp = carrier["amplitude"]
    f_bar = 1.0 / T_x
    delta_f_obs = R_q / (2 * math.pi * amp) if amp != 0 else float("nan")
    delta_P_obs = -(delta_f_obs / f_bar) * carrier["T_mean_deg"]

    phase_channel = abs(A_q) / amp if amp != 0 else float("nan")   # = 2*tan(chi0)
    freq_channel = abs(R_q) * float(np.std(u)) / amp if amp != 0 else float("nan")
    strain_channel = abs(R_i) * float(np.std(u)) / amp if amp != 0 else float("nan")
    strain_flag = bool(strain_channel > freq_channel)

    # ---- G0-d: conditioning gate (per-pair exclusion, NOT a global HALT --
    # see phase3_synthesis.md for the disclosed reading of phase1_proposal's
    # own internally-inconsistent Combined-Verdict text, resolved here in
    # favor of G0-d's own row definition, "excluded from every downstream
    # gate," matching exp-072's own precedent)
    ill_conditioned = cond5 > 100.0

    # ---- docket item(s) T2-3: primary sign-flip null (N=20000, gates)
    X4 = X5[:, :4]
    rng_pair = np.random.default_rng(rng.integers(0, 2**63 - 1))
    surr_signflip, pinv5_chk, resid5_real, yhat0_real = sign_flip_surrogates(
        delta_ab, X5, X4, N_SURR, rng_pair)
    R_q_surr = (pinv5 @ surr_signflip)[4, :]
    R_i_surr = (pinv5 @ surr_signflip)[3, :]
    p_signflip = two_sided_p(R_q, R_q_surr)

    # ---- disclosed cross-check: residual-permutation null (non-gating)
    rng_perm = np.random.default_rng(rng.integers(0, 2**63 - 1))
    surr_perm, _ = residual_permutation_surrogates(delta_ab, X5, X4, N_SURR, rng_perm)
    R_q_perm_surr = (pinv5 @ surr_perm)[4, :]
    p_permutation = two_sided_p(R_q, R_q_perm_surr)

    # ---- T2-2: ||R|| = sqrt(R_i^2+R_q^2), THERMO's ψ-marginalized statistic
    # -- rotation-invariant, tests H0: R_i=R_q=0, a DIFFERENT hypothesis,
    # reported as disclosure only, never a substitute for or relaxation of
    # RESOLVED. Reuses the SAME N=20000 sign-flip surrogates, zero extra cost.
    norm_R = math.hypot(R_i, R_q)
    norm_R_surr = np.hypot(R_i_surr, R_q_surr)
    p_norm_R = one_sided_p_ge(norm_R, norm_R_surr)

    # ---- clause (iv) + docket item 7: shared q95, self-contained, in-run
    rng_q95 = np.random.default_rng(rng.integers(0, 2**63 - 1))
    q95 = carrier_q95(theta, delta_ab, X5, X4, T_x, rng_q95)

    T_delta = exp069_run._free_period_search(theta, delta_ab, center_deg=CENTER_DEG,
                                              n_grid=N_GRID_CARRIER)["p_star_deg"]
    T_delta_x = math.radians(T_delta) * cos_c
    carrier_stat_obs = abs(T_delta_x - T_x) / T_x
    carrier_gate_pass = carrier_stat_obs <= q95      # clause (iv)

    linearization_gate_pass = abs(delta_f_obs) * (float(np.ptp(x))) <= 0.25  # clause (iii)

    # ---- clause (v): wrong-carrier gate (displaced) + fringe disclosure
    def at_carrier(T_wrong_deg):
        Tx_w = math.radians(T_wrong_deg) * cos_c
        amp_w, psi_w, _ = _amp_phase_at(theta, 0.5 * (series_a + series_b), Tx_w, xbar)
        X5w = design_matrix(theta, Tx_w, psi_w, xbar)
        pinv5w = np.linalg.pinv(X5w)
        coefw = pinv5w @ delta_ab
        R_q_w = float(coefw[4])
        X4w = X5w[:, :4]
        rng_w = np.random.default_rng(rng.integers(0, 2**63 - 1))
        surr_w, _, _, _ = sign_flip_surrogates(delta_ab, X5w, X4w, N_SURR, rng_w)
        R_q_w_surr = (pinv5w @ surr_w)[4, :]
        p_w = two_sided_p(R_q_w, R_q_w_surr)
        return R_q_w, p_w, amp_w, psi_w, Tx_w

    R_q_wrong_disp, p_wrong_disp, amp_wrong_disp, psi_wrong_disp, Tx_wrong_disp = \
        at_carrier(T_WRONG_DISPLACED)
    R_q_fringe, p_fringe, amp_fringe, psi_fringe, Tx_fringe = at_carrier(T_WRONG_FRINGE)
    wrong_carrier_gate_pass_raw = (abs(R_q_wrong_disp) <= 0.5 * abs(R_q)) and (p_wrong_disp > 0.01)

    # ---- docket item 7(a): T_wrong's own admissibility statistic, using the
    # SAME shared q95 (see carrier_q95's own docstring for the disclosed
    # judgment call this generalization required)
    wrong_admissibility_stat = abs(Tx_wrong_disp - T_x) / T_x
    wrong_admissible = wrong_admissibility_stat <= q95

    # ---- ΔP at all four carriers
    amp_delta, psi_delta, _ = _amp_phase_at(theta, 0.5 * (series_a + series_b), T_delta_x, xbar)
    X5_delta = design_matrix(theta, T_delta_x, psi_delta, xbar)
    Rq_at_Tdelta = float((np.linalg.pinv(X5_delta) @ delta_ab)[4])

    def dP_from(Rq_val, amp_val, Tx_val, Tdeg_val):
        if amp_val == 0:
            return float("nan")
        df = Rq_val / (2 * math.pi * amp_val)
        fb = 1.0 / Tx_val
        return -(df / fb) * Tdeg_val

    dP_Tmean = delta_P_obs
    dP_Tdelta = dP_from(Rq_at_Tdelta, amp_delta, T_delta_x, T_delta)
    dP_wrong = dP_from(R_q_wrong_disp, amp_wrong_disp, Tx_wrong_disp, T_WRONG_DISPLACED)
    dP_fringe = dP_from(R_q_fringe, amp_fringe, Tx_fringe, T_WRONG_FRINGE)

    # ---- docket item 7: T2-1, clause (vi) -- self-contained admissibility
    # set + non-emptiness floor (Attack 5's own two-part remedy, adopted
    # verbatim). A carrier only enters the sign-invariance test if IT ITSELF
    # independently passes its own admissibility gate; if BOTH non-T_mean
    # candidates are excluded, the pair is NOT_EVALUABLE for T2-1 -- never
    # vacuously passed.
    admitted = []
    if carrier_gate_pass:
        admitted.append(("T_delta", dP_Tdelta))
    if wrong_admissible:
        admitted.append(("T_wrong_displaced", dP_wrong))
    t21_not_evaluable = len(admitted) == 0
    if t21_not_evaluable:
        clause_vi_pass = False
    else:
        clause_vi_pass = all(_sign_match(dP_Tmean, dp) for (_, dp) in admitted)

    # ---- design-respecting residual bootstrap for SE(ΔP) (inherited,
    # unchanged, class (c))
    rng_boot = np.random.default_rng(rng.integers(0, 2**63 - 1))
    n_boot = 300
    cbar = 0.5 * (series_a + series_b)
    cbar_fit0 = _fixed_period_fit(u, cbar, T_x)
    cbar_resid0 = cbar - (X5[:, :3] @ np.array([cbar_fit0["c0"], cbar_fit0["a"], cbar_fit0["b"]]))
    ramp_resid0 = delta_ab - X5 @ coef5
    Rq_boot = np.empty(n_boot)
    for bi in range(n_boot):
        cbar_star = (X5[:, :3] @ np.array([cbar_fit0["c0"], cbar_fit0["a"], cbar_fit0["b"]])
                     + cbar_resid0[rng_boot.permutation(n)])
        try:
            free_b = exp069_run._free_period_search(theta, cbar_star, center_deg=CENTER_DEG,
                                                      n_grid=400)
            Tx_b = math.radians(free_b["p_star_deg"]) * cos_c
            amp_b, psi_b, _ = _amp_phase_at(theta, cbar_star, Tx_b, xbar)
            Xb = design_matrix(theta, Tx_b, psi_b, xbar)
            y_star = delta_ab - ramp_resid0 + ramp_resid0[rng_boot.permutation(n)]
            coefb = np.linalg.pinv(Xb) @ y_star
            Rq_boot[bi] = coefb[4]
        except Exception:
            Rq_boot[bi] = np.nan
    SE_Rq_bootstrap = float(np.nanstd(Rq_boot))
    SE_Rq_ols = float(np.sqrt(np.sum((delta_ab - X5 @ coef5) ** 2) / (n - 5) *
                               np.linalg.inv(X5.T @ X5)[4, 4]))
    SE_deltaP_Tmean = abs(dP_Tmean / R_q) * SE_Rq_bootstrap if R_q != 0 else float("nan")
    dRq_dpsi = R_i        # exact algebraic identity of the OLS rotation
    R_i_over_Rq = abs(R_i / R_q) if R_q != 0 else float("nan")

    return dict(
        pair=f"{key_a}-{key_b}", d_absorb=d_absorb,
        T_mean_deg=carrier["T_mean_deg"], T_x=T_x, amplitude=amp, psi=psi,
        carrier_r_squared=carrier["r_squared"],
        c0=c0, A_i=A_i, A_q=A_q, R_i=R_i, R_q=R_q,
        dRq_dpsi=dRq_dpsi, R_i_over_Rq=R_i_over_Rq,
        norm_R=norm_R, p_norm_R=p_norm_R,
        cond5=cond5, cond6=cond6, curvature_coef=float(coef6[5]),
        ill_conditioned=ill_conditioned,
        delta_f_obs=delta_f_obs, delta_P_obs=delta_P_obs,
        SE_deltaP_Tmean=SE_deltaP_Tmean,
        phase_channel=phase_channel, freq_channel=freq_channel,
        strain_channel=strain_channel, strain_flag=strain_flag,
        p_signflip=p_signflip, p_permutation=p_permutation,
        T_delta_deg=T_delta, carrier_stat_obs=carrier_stat_obs,
        carrier_gate_q95=q95, carrier_gate_pass=bool(carrier_gate_pass),
        linearization_gate_pass=bool(linearization_gate_pass),
        R_q_wrong_displaced=R_q_wrong_disp, p_wrong_displaced=p_wrong_disp,
        wrong_carrier_gate_pass_raw=bool(wrong_carrier_gate_pass_raw),
        wrong_carrier_magnitude_pass=bool(abs(R_q_wrong_disp) <= 0.5 * abs(R_q)),
        wrong_admissibility_stat=wrong_admissibility_stat,
        wrong_admissible=bool(wrong_admissible),
        t21_admitted_carriers=[a for a, _ in admitted],
        t21_not_evaluable=bool(t21_not_evaluable),
        clause_vi_pass=bool(clause_vi_pass),
        R_q_fringe=R_q_fringe, p_fringe=p_fringe,
        deltaP_by_carrier=dict(T_mean=dP_Tmean, T_delta=dP_Tdelta,
                                T_wrong_displaced=dP_wrong, T_fringe=dP_fringe),
        SE_Rq_ols=SE_Rq_ols, SE_Rq_bootstrap=SE_Rq_bootstrap,
    )


# ===================================================== injection-recovery power test
def injection_recovery(data, key_a, key_b, m0, d_absorb, rng):
    """Docket item 6: m0 is now the caller-supplied, runtime-loaded
    n_grid=3000-resolved slope (m0_resolved), not the n_grid=400 m0_native.
    Null construction updated to T2-3's sign-flip null; H0-clean base
    construction (strip the pair's own fitted R_q first) unchanged,
    inherited from exp-072's own Phase-5 fix (T1-3)."""
    theta = data["theta"]
    series_a, series_b = data[key_a], data[key_b]
    delta_ab = series_b - series_a
    carrier = carrier_fit(theta, series_a, series_b)
    T_x, psi, amp = carrier["T_x"], carrier["psi"], carrier["amplitude"]
    x = np.sin(np.radians(theta))
    xbar = float(np.mean(x))
    cos_c = math.cos(math.radians(CENTER_DEG))
    f_bar = 1.0 / T_x

    dP_pred = m0 * d_absorb
    dT_x = math.radians(dP_pred) * cos_c
    df_pred = -dT_x / (T_x ** 2)
    Rq_pred = 2 * math.pi * amp * df_pred

    X5 = design_matrix(theta, T_x, psi, xbar)
    X4 = X5[:, :4]
    pinv5 = np.linalg.pinv(X5)

    coef_obs = pinv5 @ delta_ab
    Rq_obs = float(coef_obs[4])
    synthetic = delta_ab - Rq_obs * X5[:, 4] + Rq_pred * X5[:, 4]

    coef_syn = pinv5 @ synthetic
    Rq_syn = float(coef_syn[4])

    rng_inj = np.random.default_rng(rng.integers(0, 2**63 - 1))
    surr, _, _, _ = sign_flip_surrogates(synthetic, X5, X4, N_SURR, rng_inj)
    Rq_surr = (pinv5 @ surr)[4, :]
    p_syn = two_sided_p(Rq_syn, Rq_surr)
    return dict(pair=f"{key_a}-{key_b}", Rq_pred=Rq_pred, Rq_obs=Rq_obs,
                Rq_recovered=Rq_syn, p_recovered=p_syn)


# ===================================================== saturating vs linear
# Regression-check only (permitted, per the contamination ruling: exp-072's
# own published results.json MAY be used to VALIDATE this cycle's code is
# correct, on the identical unchanged machinery -- this is exactly that
# check, disclosed as such). Not gating; used ONLY to confirm `m0_resolved`
# (loaded above) matches an independent re-derivation.
def saturating_vs_linear(theta, data):
    configs = ["C40", "C60", "C70", "C80"]
    absorb_vals = np.array([40.0, 60.0, 70.0, 80.0])
    periods = []
    for key in configs:
        free = exp069_run._free_period_search(theta, data[key], center_deg=CENTER_DEG,
                                               n_grid=N_GRID_CARRIER)
        periods.append(free["p_star_deg"])
    periods = np.array(periods)

    Xl = np.column_stack([np.ones(4), absorb_vals])
    coefl, *_ = np.linalg.lstsq(Xl, periods, rcond=None)
    yhat_l = Xl @ coefl
    r2_l = 1.0 - np.sum((periods - yhat_l) ** 2) / np.sum((periods - periods.mean()) ** 2)

    Xs = np.column_stack([np.ones(4), -np.exp(-SAT_DECAY_L * absorb_vals)])
    coefs, *_ = np.linalg.lstsq(Xs, periods, rcond=None)
    yhat_s = Xs @ coefs
    r2_s = 1.0 - np.sum((periods - yhat_s) ** 2) / np.sum((periods - periods.mean()) ** 2)

    return dict(absorb=absorb_vals.tolist(), periods_n_grid3000=periods.tolist(),
                linear=dict(intercept=float(coefl[0]), slope=float(coefl[1]), r_squared=float(r2_l)),
                saturating=dict(P_inf=float(coefs[0]), amplitude=float(-coefs[1]),
                                 decay_L=SAT_DECAY_L, r_squared=float(r2_s)),
                matches_exp072_slope=bool(abs(float(coefl[1]) - data["m0_resolved"]) < 1e-9))


# ===================================================== docket item 5: a-priori disclosure
def a_priori_disclosure(data):
    """docket item 5 (text-only per the audit, but the underlying numbers
    are computed here, loaded, never hand-typed): the naive a-priori
    chi0 estimate (using m0_resolved) vs. exp-072's own already-closed,
    non-contaminating real chi0 values -- disclosure only, never gating."""
    m0 = data["m0_resolved"]
    cos_c = math.cos(math.radians(CENTER_DEG))
    xbar_est = math.sin(math.radians(CENTER_DEG))  # x-bar approx, disclosure only
    out = {}
    for key_a, key_b, d_absorb in PAIRS:
        pair = f"{key_a}-{key_b}"
        dP_pred = m0 * d_absorb
        # representative T_x for the a-priori estimate: use the
        # window-centre nominal ~2.49deg carrier (data-free, matches G0-e's
        # own bracket choice) -- purely illustrative, non-gating.
        T_x_nom = math.radians(2.49) * cos_c
        dT_x = math.radians(dP_pred) * cos_c
        df_pred = -dT_x / (T_x_nom ** 2)
        chi0_naive = math.pi * df_pred * xbar_est
        real = data["exp072_disclosure"][pair]
        out[pair] = dict(
            d_absorb=d_absorb, dP_pred_naive=dP_pred,
            chi0_naive_a_priori=chi0_naive,
            chi0_real_exp072=real["chi0_real"],
            tan_over_sin_real=real["tan_over_sin"],
            note=("The naive a-priori chi0 estimate assumes the true effect "
                  "matches m0's predicted size; exp-072's own already-closed, "
                  "non-contaminating chi0 (class-b disclosure, never used to "
                  "set any threshold here) shows the realized value is "
                  "1-2 orders of magnitude smaller on this exact substrate "
                  "-- the tan-vs-sin correction (T2-4) is therefore expected "
                  "to remain numerically inert on real data, though it is "
                  "still the exact, non-approximate relation (docket item 5, "
                  "phase2_redteam_audit.md Attack 2)."),
        )
    return out


# ===================================================== residual pool (docket item 4)
def build_residual_pool(data):
    """Docket item 4: the empirical residual distribution from the four
    configs' own already-committed free-period fits (exp-069's C40/C80,
    exp-071's C60/C70, at each config's own native n_grid=400 p_star_deg) --
    used as G0-e(ii)'s harder, more realistic robustness leg (structured/
    non-Gaussian real FDTD residuals, not i.i.d. Gaussian)."""
    theta = data["theta"]
    x = np.sin(np.radians(theta))
    xbar = float(np.mean(x))
    u = x - xbar
    cos_c = math.cos(math.radians(CENTER_DEG))
    pool = []
    for key in ("C40", "C60", "C70", "C80"):
        p_star = data["per_config_free_native"][key]["p_star_deg"]
        Tx = math.radians(p_star) * cos_c
        fit = _fixed_period_fit(u, data[key], Tx)
        w = 2 * math.pi / Tx
        yhat = fit["c0"] + fit["a"] * np.cos(w * u) + fit["b"] * np.sin(w * u)
        pool.append(data[key] - yhat)
    pool = np.concatenate(pool)
    return pool


# ===================================================== G0-e(i): ground-truth recovery
def ground_truth_recovery_check(theta_deg):
    """docket items 1-2 (PHOTONICS' remedy, adopted verbatim): widened
    coverage PLUS independent amplitude (delta_a/a) and independent phase
    (Delta_psi) axes, decoupled from the primary T_A/a/DeltaP/psi_bar grid.

    Generator redesigned this cycle (disclosed judgment call, see
    phase3_synthesis.md) to use EM's own exact symmetric two-tone
    parameterization (phase2_critique_em.md Sec 1: C_A=a_A*cos(Theta-phi),
    C_B=a_B*cos(Theta+phi), phi=chi0+pi*Delta_f*u) rather than literally
    bolting delta_a/Delta_psi onto exp-072's original independently-tuned
    cos(w*u-psi0) form -- the symmetric form gives an EXACT (to the same
    leading-order-in-u the whole 5-column model already assumes), testable
    ground-truth target for A_i (= delta_a * cos(chi0)), closing PHOTONICS'
    own "A_i tripwire is dead code" attack with a live, non-vacuous check
    (docket item 2, option (a): kept purely synthetic, class (c)).

    Leg A (primary, widened): T_A in {2.40,2.49,2.55}, a0 in
    {0.002,0.005,0.01}, DeltaP in the 12 signed values of
    {0.005,0.01,0.02,0.04,0.08,0.10} (BOTH signs -- phase1_proposal.md's own
    "3x3x6x32=1728" arithmetic undercounts by exactly 2x relative to its own
    ΔP definition (six magnitudes, each signed = 12 values, not 6); this is
    disclosed in phase3_synthesis.md as a self-caught issue, not a docket
    item, and resolved here by using the full signed list, since bracketing
    both signs is the stated requirement), psi_bar over 32 phases, delta_a=0,
    Delta_psi=0 -- 3*3*12*32 = 3456 cells.
    Leg B (independent amplitude): T_A=2.49, a0=0.005 (representative,
    "alongside" not fully crossed), DeltaP (12) x psi_bar (32) x
    delta_a/a in {0.03,0.10} -- 768 cells.
    Leg C (independent phase): same representative T_A/a0, DeltaP (12) x
    psi_bar (32) x Delta_psi in {+-0.3,+-0.8} rad -- 1536 cells.
    Total 5760 cells.

    Two tripwires, both formula-derived (class c): dR_q/dpsi_bar == R_i to
    within 1e-6 (central finite difference, eps=1e-4 rad) at EVERY cell; A_i
    must match delta_a*cos(chi0_true) within 1% at every cell where
    |delta_a*cos(chi0_true)| >= 1e-4 (now genuinely live once delta_a != 0,
    docket item 1)."""
    x = np.sin(np.radians(theta_deg))
    xbar = float(np.mean(x))
    u = x - xbar
    cos_c = math.cos(math.radians(CENTER_DEG))

    dP_magnitudes = (0.005, 0.01, 0.02, 0.04, 0.08, 0.10)
    dP_values = tuple(s * m for m in dP_magnitudes for s in (1.0, -1.0))  # 12 signed values

    def one_cell(P_A_deg, a0, dP_true, psi_bar, delta_a_frac, delta_psi):
        T_A = math.radians(P_A_deg) * cos_c
        P_B_deg = P_A_deg + dP_true
        T_B = math.radians(P_B_deg) * cos_c
        T_mean_x = 0.5 * (T_A + T_B)
        P_mean_deg = 0.5 * (P_A_deg + P_B_deg)
        w_bar = 2 * math.pi / T_mean_x
        delta_f = 1.0 / T_B - 1.0 / T_A
        # NOTE (disclosed judgment call, phase3_synthesis.md): chi0 here is
        # the u=0 (window-CENTRE, not raw-x=0) phase gap, swept directly as
        # delta_psi/2 -- NOT phase1_proposal's own real-data convention
        # chi0=pi*Delta_f*xbar+Delta_psi/2 (an x=0-EXTRAPOLATED quantity,
        # explicitly "may not be quoted" per Sec 2b.3). Using the real-data
        # convention here would make even delta_psi=0 carry a nonzero
        # chi0=pi*Delta_f*xbar baked in by construction, which is NOT what
        # exp-072's own already-validated generator produces (there, both
        # tones share one psi0 exactly, so the u=0 phase gap is exactly
        # zero) -- verified directly: the un-shifted (window-centre) form
        # below reduces EXACTLY to exp-072's own generator's accuracy
        # (worst-cell 0.17% vs exp-072's own 0.15%) at delta_a=Delta_psi=0,
        # while the x=0-extrapolated form does NOT (worst-cell 78%, an
        # implementation bug caught during this cycle's own development --
        # see phase3_synthesis.md). This file's synthetic generator is a
        # deliberately self-contained recovery test, not a literal
        # reproduction of the real-data chi0 bookkeeping; the REAL analysis
        # pipeline (analyze_pair, above) is untouched by this choice.
        chi0 = delta_psi / 2.0

        def build(psi_val):
            Theta = w_bar * u + psi_val
            phi = chi0 + math.pi * delta_f * u
            a_A = a0
            a_B = a0 * (1.0 + delta_a_frac)
            C_A = a_A * np.cos(Theta - phi)
            C_B = a_B * np.cos(Theta + phi)
            return C_B - C_A, 0.5 * (C_A + C_B), a_A, a_B

        delta_true, Cbar_true, a_A, a_B = build(psi_bar)
        amp, psi, _ = _amp_phase_at(theta_deg, Cbar_true, T_mean_x, xbar)
        f_bar = 1.0 / T_mean_x
        X5 = design_matrix(theta_deg, T_mean_x, psi, xbar)
        coef = np.linalg.lstsq(X5, delta_true, rcond=None)[0]
        A_i_est, R_i_est, R_q_est = float(coef[1]), float(coef[3]), float(coef[4])
        delta_f_est = R_q_est / (2 * math.pi * amp) if amp != 0 else float("nan")
        dP_est = -(delta_f_est / f_bar) * P_mean_deg
        err = abs(dP_est / dP_true - 1.0) if dP_true != 0 else abs(dP_est)

        # tripwire 1: dR_q/dpsi_bar == R_i -- an identity of the FITTED
        # design matrix's own psi argument, holding the DATA fixed (this is
        # what exp-072's own Phase-5 verification actually checked, "5
        # decimals," item K/C19 in phase5_redteam_audit.md -- NOT a
        # perturbation of this synthetic generator's own psi_bar, which
        # conflates the derivative with _amp_phase_at's own re-estimation
        # noise on a genuinely two-tone Cbar and gives only ~1e-4-level
        # agreement, not 1e-6; verified independently during this cycle's
        # own development, see phase3_synthesis.md). Sign convention:
        # design_matrix()'s own `psi` argument is `_amp_phase_at`'s
        # `-atan2(b,a)`, i.e. the NEGATIVE of the symbol "psi_bar" used in
        # the write-up's own formulas -- so dR_q/d(psi_bar_symbol) =
        # -dR_q/d(design_matrix psi), independently re-verified this cycle
        # against exp-072's own real, published per-pair R_i/psi/T_x values
        # (ratio -1.0000000000 to 10 decimals at all four pairs before this
        # sign correction; +1.0000000000 after it).
        eps = 1e-6
        X5p = design_matrix(theta_deg, T_mean_x, psi + eps, xbar)
        X5m = design_matrix(theta_deg, T_mean_x, psi - eps, xbar)
        Rqp = np.linalg.lstsq(X5p, delta_true, rcond=None)[0][4]
        Rqm = np.linalg.lstsq(X5m, delta_true, rcond=None)[0][4]
        dRq_dpsi_num = -(float(Rqp) - float(Rqm)) / (2 * eps)
        identity_err = abs(dRq_dpsi_num - R_i_est)

        # tripwire 2: A_i vs delta_a*cos(chi0_true), live whenever non-tiny
        target_Ai = (a_B - a_A) * math.cos(chi0)
        if abs(target_Ai) >= 1e-4:
            ai_rel_err = abs(A_i_est - target_Ai) / abs(target_Ai)
            ai_checked = True
        else:
            ai_rel_err = None
            ai_checked = False

        return err, identity_err, ai_checked, ai_rel_err

    def run_leg(cells):
        worst_recovery = 0.0
        worst_identity = 0.0
        worst_ai = 0.0
        n_ai_checked = 0
        n_ai_fail = 0
        n = 0
        for (P_A, a0, dP, psib, da, dpsi) in cells:
            err, ident_err, ai_checked, ai_rel = one_cell(P_A, a0, dP, psib, da, dpsi)
            worst_recovery = max(worst_recovery, err)
            worst_identity = max(worst_identity, ident_err)
            if ai_checked:
                n_ai_checked += 1
                worst_ai = max(worst_ai, ai_rel)
                if ai_rel > 0.01:
                    n_ai_fail += 1
            n += 1
        return dict(n_cells=n, worst_recovery_ratio_error=worst_recovery,
                    worst_identity_error=worst_identity,
                    n_ai_checked=n_ai_checked, n_ai_fail=n_ai_fail,
                    worst_ai_rel_error=worst_ai)

    psi_bar_full = list(np.linspace(0, 2 * math.pi, 32, endpoint=False))

    leg_primary = [(P_A, a0, dP, psib, 0.0, 0.0)
                   for P_A in (2.40, 2.49, 2.55)
                   for a0 in (0.002, 0.005, 0.01)
                   for dP in dP_values
                   for psib in psi_bar_full]
    leg_delta_a = [(2.49, 0.005, dP, psib, da, 0.0)
                   for dP in dP_values
                   for psib in psi_bar_full
                   for da in (0.03, 0.10)]
    leg_delta_psi = [(2.49, 0.005, dP, psib, 0.0, dpsi)
                      for dP in dP_values
                      for psib in psi_bar_full
                      for dpsi in (0.3, -0.3, 0.8, -0.8)]

    res_primary = run_leg(leg_primary)
    res_delta_a = run_leg(leg_delta_a)
    res_delta_psi = run_leg(leg_delta_psi)

    worst = max(res_primary["worst_recovery_ratio_error"],
                res_delta_a["worst_recovery_ratio_error"],
                res_delta_psi["worst_recovery_ratio_error"])
    worst_identity = max(res_primary["worst_identity_error"],
                          res_delta_a["worst_identity_error"],
                          res_delta_psi["worst_identity_error"])
    n_ai_checked = (res_primary["n_ai_checked"] + res_delta_a["n_ai_checked"]
                    + res_delta_psi["n_ai_checked"])
    n_ai_fail = res_primary["n_ai_fail"] + res_delta_a["n_ai_fail"] + res_delta_psi["n_ai_fail"]
    n_cells_total = res_primary["n_cells"] + res_delta_a["n_cells"] + res_delta_psi["n_cells"]

    identity_pass = worst_identity <= 1e-6
    ai_tripwire_pass = (n_ai_checked > 0) and (n_ai_fail == 0)
    recovery_pass = worst <= 0.02

    return dict(
        pass_=bool(recovery_pass and identity_pass and ai_tripwire_pass),
        worst_abs_ratio_error=float(worst),
        n_cells=n_cells_total,
        legs=dict(primary=res_primary, delta_a=res_delta_a, delta_psi=res_delta_psi),
        identity_tripwire=dict(pass_=bool(identity_pass), worst_error=float(worst_identity)),
        ai_tripwire=dict(pass_=bool(ai_tripwire_pass), n_checked=n_ai_checked,
                          n_fail=n_ai_fail,
                          note=("Vacuous under exp-072's original delta_a=Delta_psi=0 "
                                "generator (0 cells ever qualified); now live via the "
                                "delta_a/Delta_psi legs (docket item 1) -- n_checked>0 "
                                "confirms the tripwire is no longer dead code (docket "
                                "item 2, PHOTONICS' Attack 1, phase2_redteam_audit.md).")),
    )


# ===================================================== G0-e(ii): null calibration
def null_calibration_check(theta_deg, residual_pool):
    """docket items 3-4: G0-e(ii) as a binding, non-relaxable HALT,
    UNMODIFIED in construction (per Red Team's own Attack 4 ruling -- do
    not adopt either candidate fix as a same-cycle patch), PLUS a
    residual-structure robustness leg (Attack 7/docket item 4) using the
    real per-config free-period-fit residual pool instead of i.i.d.
    Gaussian noise. BOTH legs' full calibration tables are persisted
    regardless of outcome (docket item 3a); EITHER leg failing its own
    band at any (cell, alpha) HALTs the cycle as HALT_NULL_MISCALIBRATED
    (docket item 3b) -- the i.i.d. leg is the harder-to-satisfy floor per
    Red Team's own independently-reproduced finding (Attack 4: anti-
    conservative 2-6x nominal, a leverage effect, uniform across the swept
    carrier phase/noise level), and Attack 7 argues the residual-structure
    leg can only be as bad or worse, so requiring both to pass is the
    correct reading of "genuinely trustworthy before any real data is
    scored," not a redundant check."""
    x = np.sin(np.radians(theta_deg))
    xbar = float(np.mean(x))
    u = x - xbar
    cos_c = math.cos(math.radians(CENTER_DEG))
    T_A_x = math.radians(2.49) * cos_c   # carrier fixed at T_A=2.49deg
    n = len(theta_deg)

    sigmas = (0.0005, 0.002, 0.008)
    psi0_vals = list(np.linspace(0, 2 * math.pi, 8, endpoint=False))
    alphas = (0.01, 0.05, 0.10)
    K = 500
    N_CALIB = N_SURR   # "identical construction to the real gating null" (N=20000)

    pool_std = float(np.std(residual_pool))

    def run_grid(rng, use_pool):
        rows = []
        for sigma in sigmas:
            for psi0 in psi0_vals:
                X5 = design_matrix(theta_deg, T_A_x, psi0, xbar)
                X4 = X5[:, :4]
                pinv5 = np.linalg.pinv(X5)
                pinv4 = np.linalg.pinv(X4)
                row5 = pinv5[4, :]
                reject_counts = {a: 0 for a in alphas}
                for _ in range(K):
                    if use_pool:
                        y = rng.choice(residual_pool, size=n, replace=True)
                        y = y * (sigma / pool_std) if pool_std > 0 else y
                    else:
                        y = rng.normal(0.0, sigma, size=n)
                    coef5 = pinv5 @ y
                    Rq_obs = float(coef5[4])
                    yhat0 = X4 @ (pinv4 @ y)
                    resid5 = y - X5 @ coef5
                    w = row5 * resid5
                    S = rng.choice(np.array([-1.0, 1.0]), size=(n, N_CALIB))
                    Rq_surr = w @ S
                    p = (1 + np.sum(np.abs(Rq_surr) >= abs(Rq_obs))) / (N_CALIB + 1)
                    for a in alphas:
                        if p <= a:
                            reject_counts[a] += 1
                for a in alphas:
                    rate = reject_counts[a] / K
                    band = 3.0 * math.sqrt(a * (1 - a) / K)
                    lo, hi = a - band, a + band
                    rows.append(dict(sigma=sigma, psi0=psi0, alpha=a,
                                      rejection_rate=rate, nominal=a,
                                      deviation=rate - a, band_lo=lo, band_hi=hi,
                                      pass_=bool(lo <= rate <= hi)))
        return rows

    rng_iid = np.random.default_rng(SEED_CALIB)
    rng_pool = np.random.default_rng(SEED_CALIB + 1)  # distinct stream
    table_iid = run_grid(rng_iid, use_pool=False)
    table_pool = run_grid(rng_pool, use_pool=True)

    iid_pass = all(r["pass_"] for r in table_iid)
    pool_pass = all(r["pass_"] for r in table_pool)

    return dict(
        pass_=bool(iid_pass and pool_pass),
        iid_leg=dict(pass_=bool(iid_pass), table=table_iid),
        residual_structure_leg=dict(pass_=bool(pool_pass), table=table_pool,
                                     pool_std=pool_std, pool_n=len(residual_pool)),
        K=K, N=N_CALIB, n_cells_per_leg=len(sigmas) * len(psi0_vals),
    )


# ===================================================== contamination disclosure wiring
_CONTAMINATION_TEXT = (
    "CONTAMINATION DISCLOSURE (phase2_redteam_audit.md Sec 3, docket item 11): "
    "exp-073's carrier-fit and ramped-differential-OLS machinery is bit-"
    "identical to exp-072's own already-committed, already-published "
    "run.py, applied to the identical 124-point substrate. Every real "
    "per-pair point estimate this cycle's Phase 4 produced -- T_mean, "
    "a_cbar, psi_bar, A_i, A_q, R_i, R_q, Delta_f, |Delta_f|*X, and "
    "Delta_P including its sign -- was ALREADY computable, bit-exact, from "
    "experiments/072-t28-differential-beat-fit/results.json before this "
    "cycle's Phase 1 was even proposed, and was in fact independently "
    "computed, for the A_q/chi0 channel, by this cycle's own EM critique. "
    "This CONFIRM-shaped outcome must be read with that fact in mind: no "
    "gate, band, or threshold was set or moved with reference to any of "
    "exp-072's known real numbers (verified item-by-item, "
    "phase2_redteam_audit.md Sec 3), but a reader must be able to discount "
    "the 'clean re-issue' framing without reconstructing that document's "
    "own reasoning."
)


def _contamination_block(combined_verdict, p073_2, per_pair):
    confirm_shaped = (combined_verdict == "CONFIRMED") or (p073_2 == "CONFIRM") or \
        any(p.get("resolved") for p in per_pair.values())
    return dict(
        pre_registration_paragraph=(
            "During Phase 2, EM's critique independently computed exp-072's "
            "own real chi0/A_q/amplitude values for all four pairs (a real, "
            "previously-closed, non-contaminating number, per Red Team's "
            "audit Sec 3) while diagnosing the chi0-regime a-priori claim. "
            "Red Team's audit generalized this: because exp-073's machinery "
            "is bit-identical to exp-072's own on unchanged data, ALL of "
            "this cycle's real point estimates were already computable from "
            "exp-072's own results.json before Phase 1. Ruled NOT outcome-"
            "determining for the Combined Verdict as specified: none of the "
            "three new-machinery items (T2-1, T2-3, T2-4) were tuned in "
            "response to these numbers; every threshold traces to a data-"
            "free argument (algebraic identity, leakage-minimization, "
            "window geometry). See phase2_redteam_audit.md Sec 3 for the "
            "full ruling this cycle operates under."),
        forward_lock_statement=(
            "Any change to a gate, band, or threshold made from Red Team's "
            "Phase-2 audit forward, for any reason traceable to exp-072's "
            "known real numbers, must be treated as a fresh Phase-1/2 "
            "pre-registration decision -- never folded into a same-cycle "
            "Phase-3 correction. No such change was made in this file."),
        confirm_disclosure_required=bool(confirm_shaped),
        confirm_disclosure_text=(_CONTAMINATION_TEXT if confirm_shaped else None),
    )


# ===================================================== full scoring + Combined Verdict
def score_all(data):
    rng = np.random.default_rng(SEED)
    theta = data["theta"]

    # ---- G0-a/b/c: data-integrity gates (unchanged, inherited)
    g0a_pass = data["g0a"]["all_identical"]
    g0b_pass = data["g0b"]["max_abs_residual"] <= 1e-12
    g0c_pass = data["g0c"]["max_abs_delta"] <= 1e-12

    combined = None
    per_pair = {}
    injection = {}
    power_demonstrated = None
    p073_2 = p073_3 = p073_4 = None
    rho_c = None
    rho_c_common_carrier_residual = None
    n_resolved_holm10 = None
    g0e_i = None
    g0e_ii = None

    if not g0a_pass:
        combined = "HALT_GRID_MISMATCH"
    elif not g0b_pass:
        combined = "HALT_TELESCOPE_MISMATCH"
    elif not g0c_pass:
        combined = "HALT_PROVENANCE_MISMATCH"
    else:
        # ---- G0-e(i): ground-truth recovery, BEFORE any real pair is scored
        g0e_i = ground_truth_recovery_check(theta)
        if not g0e_i["pass_"]:
            combined = "HALT_RECOVERY_FAILED"
        else:
            # ---- G0-e(ii): null calibration, BEFORE any real pair is scored
            residual_pool = build_residual_pool(data)
            g0e_ii = null_calibration_check(theta, residual_pool)
            if not g0e_ii["pass_"]:
                combined = "HALT_NULL_MISCALIBRATED"

    if combined is None:
        # ---- gates all clear: proceed to real-pair analysis
        for key_a, key_b, d_absorb in PAIRS:
            per_pair[f"{key_a}-{key_b}"] = analyze_pair(data, key_a, key_b, d_absorb, rng)

        # Holm over the 3 algebraically-free adjacent pairs (item 14-lineage,
        # inherited unchanged); C40-C80 reported unadjusted/derived (G0-b).
        p_signflip_free = {k: per_pair[k]["p_signflip"] for k in HOLM_PAIRS}
        holm_signflip = holm_adjust(p_signflip_free, m=3)
        for k in HOLM_PAIRS:
            per_pair[k]["p_signflip_holm"] = holm_signflip[k]
        per_pair["C40-C80"]["p_signflip_holm"] = per_pair["C40-C80"]["p_signflip"]
        per_pair["C40-C80"]["p_derived_unadjusted"] = True

        p_wrong_free = {k: per_pair[k]["p_wrong_displaced"] for k in HOLM_PAIRS}
        holm_wrong = holm_adjust(p_wrong_free, m=3)
        for k in HOLM_PAIRS:
            per_pair[k]["p_wrong_displaced_holm"] = holm_wrong[k]
        per_pair["C40-C80"]["p_wrong_displaced_holm"] = per_pair["C40-C80"]["p_wrong_displaced"]
        for k, p in per_pair.items():
            p["wrong_carrier_gate_pass"] = bool(
                p["wrong_carrier_magnitude_pass"] and p["p_wrong_displaced_holm"] > 0.01)

        # RESOLVED: 6-clause conjunction (P-073-2 (i)-(vi))
        for k, p in per_pair.items():
            p["resolved"] = bool(
                (not p["ill_conditioned"])                        # (i)
                and (p["p_signflip_holm"] <= 0.01)                 # (ii)
                and p["linearization_gate_pass"]                   # (iii)
                and p["carrier_gate_pass"]                         # (iv)
                and p["wrong_carrier_gate_pass"]                   # (v)
                and p["clause_vi_pass"]                            # (vi), T2-1
            )

        # ---- injection-recovery power test (3 adjacent pairs), m0_resolved
        for key_a, key_b, d_absorb in PAIRS[:3]:
            injection[f"{key_a}-{key_b}"] = injection_recovery(
                data, key_a, key_b, data["m0_resolved"], d_absorb, rng)
        p_injection = {k: injection[k]["p_recovered"] for k in injection}
        holm_injection = holm_adjust(p_injection, m=3)
        for k in injection:
            injection[k]["p_recovered_holm"] = holm_injection[k]
        power_demonstrated = all(v <= 0.01 for v in holm_injection.values())

        n_resolved_holm10 = sum(
            1 for k in HOLM_PAIRS if per_pair[k]["p_signflip_holm"] <= 0.10
        )

        c4080 = per_pair["C40-C80"]["resolved"]
        c4060 = per_pair["C40-C60"]["resolved"]
        c6070 = per_pair["C60-C70"]["resolved"]
        c7080 = per_pair["C70-C80"]["resolved"]

        if c4080 and c4060 and (c6070 or c7080):
            p073_2 = "CONFIRM"
        elif n_resolved_holm10 == 0:
            p073_2 = "REFUTE" if power_demonstrated else "UNDERPOWERED_NOT_EVALUABLE"
        else:
            p073_2 = "NEITHER"

        # ---- P-073-3: rho_c, carrier-sensitivity closure (relabelled per
        # Red Team's RT-1 finding, inherited -- disclosed common-carrier
        # sanity check, NEVER scored)
        _common_Tx, _common_psi = per_pair["C40-C80"]["T_x"], per_pair["C40-C80"]["psi"]
        _common_xbar = float(np.mean(np.sin(np.radians(theta))))
        _Rq_common = {}
        for key_a, key_b, _ in PAIRS:
            _Xc = design_matrix(theta, _common_Tx, _common_psi, _common_xbar)
            _delta_c = data[key_b] - data[key_a]
            _Rq_common[f"{key_a}-{key_b}"] = float((np.linalg.pinv(_Xc) @ _delta_c)[4])
        rho_c_common_carrier_residual = abs(
            sum(_Rq_common[k] for k in HOLM_PAIRS) - _Rq_common["C40-C80"]
        ) / max(abs(_Rq_common["C40-C80"]), 1e-12)

        adj_resolved = [per_pair[k]["resolved"] for k in HOLM_PAIRS]
        if not all(adj_resolved):
            p073_3 = "NOT_EVALUABLE"
        else:
            S = sum(per_pair[k]["delta_P_obs"] for k in HOLM_PAIRS)
            D = per_pair["C40-C80"]["delta_P_obs"]
            rho_c = abs(S - D) / max(abs(D), 0.005)
            if rho_c <= 0.05 and _sign_match(S, D):
                p073_3 = "CONFIRM"
            elif rho_c >= 1.00 or (not _sign_match(S, D) and abs(S) >= 0.010 and abs(D) >= 0.010):
                p073_3 = "REFUTE"
            else:
                p073_3 = "NEITHER"

        # ---- P-073-4: ABSORB-depth-trend consistency (sign-reversal is the
        # ONLY gating rate clause; the [m0/3,3m0] band is disclosed, non-gating)
        resolved_pairs = [k for k in per_pair if per_pair[k]["resolved"]]
        sign_reversal = any(
            per_pair[k]["delta_P_obs"] < 0 and abs(per_pair[k]["delta_P_obs"]) >= 0.010
            for k in resolved_pairs
        )
        m0_ref = data["m0_resolved"]
        rate_band_lo, rate_band_hi = m0_ref / 3.0, 3.0 * m0_ref
        rate_disclosure = {}
        for k in resolved_pairs:
            p = per_pair[k]
            r = p["delta_P_obs"] / p["d_absorb"] if p["d_absorb"] != 0 else float("nan")
            sat_pred = m0_ref  # SAT_DECAY_L-based rate: disclosed via saturating_vs_linear()
            rate_disclosure[k] = dict(rate=r, in_linear_band=bool(rate_band_lo <= r <= rate_band_hi))

        if sign_reversal:
            p073_4 = "REFUTE"
        elif len(resolved_pairs) >= 2 and all(per_pair[k]["delta_P_obs"] > 0 for k in resolved_pairs):
            all_in_band = all(rate_disclosure[k]["in_linear_band"] for k in resolved_pairs)
            p073_4 = "CONFIRM" if all_in_band else "NEITHER"
        else:
            p073_4 = "NEITHER"

        # ---- Combined Verdict (gates already clear at this point)
        if p073_2 == "REFUTE" or p073_3 == "REFUTE":
            combined = "REFUTED"
        elif p073_2 == "CONFIRM" and p073_3 == "CONFIRM" and p073_4 == "CONFIRM":
            combined = "CONFIRMED"
        else:
            combined = "NEITHER"

    contamination = _contamination_block(combined, p073_2, per_pair)

    return dict(
        per_pair=per_pair, injection=injection, power_demonstrated=power_demonstrated,
        p073_2=p073_2, p073_3=p073_3, rho_c=rho_c,
        rho_c_common_carrier_residual=rho_c_common_carrier_residual,
        p073_4=p073_4,
        combined_verdict=combined,
        g0a_pass=bool(g0a_pass), g0b_pass=bool(g0b_pass), g0c_pass=bool(g0c_pass),
        g0e_i=g0e_i, g0e_ii=g0e_ii,
        n_resolved_holm10=n_resolved_holm10,
        contamination=contamination,
    )


def main():
    t0 = time.time()
    data = load_data()
    scored = score_all(data)
    sat = saturating_vs_linear(data["theta"], data)
    a_priori = a_priori_disclosure(data)

    results = dict(
        experiment="073-t28-differential-beat-fit-reissue",
        panel_iteration=50,
        lead_seat="MATERIALS",
        t1_escape_route=None,
        m0_native=data["m0_native"],
        m0_resolved=data["m0_resolved"], m0_resolved_r2=data["m0_resolved_r2"],
        exp072_disclosure=data["exp072_disclosure"],
        a_priori_disclosure=a_priori,
        g0=dict(a=data["g0a"], b=data["g0b"], c=data["g0c"]),
        saturating_vs_linear=sat,
        scored=scored,
        elapsed_s=time.time() - t0,
    )

    out_path = os.path.join(HERE, "dev_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=float)
    print(f"[DEV RUN -- not the official Phase-4 deliverable; see task instructions]")
    print(f"Combined Verdict: {scored['combined_verdict']}")
    if scored["combined_verdict"] not in (
            "HALT_GRID_MISMATCH", "HALT_TELESCOPE_MISMATCH",
            "HALT_PROVENANCE_MISMATCH", "HALT_RECOVERY_FAILED", "HALT_NULL_MISCALIBRATED"):
        print(f"P-073-2: {scored['p073_2']}  P-073-3: {scored['p073_3']} (rho_c={scored['rho_c']})  "
              f"P-073-4: {scored['p073_4']}")
        for k, p in scored["per_pair"].items():
            print(f"  {k}: resolved={p['resolved']}  p_signflip_holm={p.get('p_signflip_holm'):.4f}  "
                  f"dP(Tmean)={p['delta_P_obs']:+.4f}deg  cond={p['cond5']:.1f}  "
                  f"t21_not_evaluable={p['t21_not_evaluable']}")
    elif scored["combined_verdict"] == "HALT_NULL_MISCALIBRATED":
        iid = scored["g0e_ii"]["iid_leg"]
        n_fail = sum(1 for r in iid["table"] if not r["pass_"])
        print(f"G0-e(ii) HALT: iid leg {n_fail}/{len(iid['table'])} cell-alpha combos "
              f"outside calibration band (pass={iid['pass_']})")
    print(f"elapsed: {results['elapsed_s']:.1f}s")


if __name__ == "__main__":
    main()
