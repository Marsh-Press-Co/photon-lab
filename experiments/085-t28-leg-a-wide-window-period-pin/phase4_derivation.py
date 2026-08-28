"""
experiments/085-t28-leg-a-wide-window-period-pin/phase4_derivation.py
============================================================================
Panel Iteration 62 (exp-085). Director-run, implementing Phase 3's frozen,
corrected spec (`phase3_synthesis.md`) -- all 7 Red Team Phase-2 mandatory
fixes applied on top of the committed `phase1_proposal.md`. Zero new FDTD
calls; reuses, unchanged: `dg048.edge_diffraction_c_empty_corrected`'s own
formula (see performance note below), `dg065.propagator_geom`/`CONFIGS`,
`ywp.free_period_with_widening`/`_free_period_search`/
`SS_TOT_DEGENERATE_FLOOR`, `run69._fixed_period_fit`, `amb.window_means`/
`weber`. Loads `experiments/084-.../phase1_derivation.py` itself (same
`_load` idiom exp-084's own `phase3_fix_docket_checks.py` used) to inherit
its already-validated geometry constants and assertions rather than
re-deriving them.

PERFORMANCE NOTE (disclosed, not a physics change): `dg048.field_and_h`
(and therefore `edge_diffraction_c_empty_corrected`) recomputes its full
theta-INDEPENDENT G0/geometry matrix (`_geom_derived`, a 1504x1504 complex
array) on EVERY call. Benchmarked: ~130ms/call, ~510s for one 3901-point
curve. This cycle needs ~40,000+ evaluations (Method A's dense curve,
Method A's ~3900-shift circular-shift null needs only REFITS not
re-evals, Method C's 37 sub-curves). This script computes `gd`/`G0` ONCE
per geometry via a local `_FastEval` helper and reuses it across every
theta evaluation for that geometry -- **verified bit-identical (exactly
0.0 absolute difference) against the original per-call function at 5
spot-check angles, asserted below before any use.** The formula itself is
untouched, byte-for-byte; only the redundant matrix reconstruction is
skipped.
"""

import importlib.util
import json
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP084_DIR = os.path.join(ROOT, "experiments", "084-t28-edge-diffraction-derivation")
deriv = _load(os.path.join(EXP084_DIR, "phase1_derivation.py"), "_exp085_deriv084")

dg048 = deriv.dg048
dg065 = deriv.dg065
ywp = deriv.ywp
run69 = deriv.run69
free_period_with_widening = deriv.free_period_with_widening
_free_period_search = deriv._free_period_search
_fixed_period_fit = run69._fixed_period_fit
SS_TOT_DEGENERATE_FLOOR = deriv.SS_TOT_DEGENERATE_FLOOR

from lab import ambient as amb  # noqa: E402

LAM600 = deriv.LAM600
CFG_C40 = deriv.CFG_C40
P_EDGE_A = deriv.P_EDGE_A
assert abs(P_EDGE_A - 2.8421052631578947) < 1e-9

# narrow-window (exp-084) already-published numbers -- READ, never hand-typed
_prior = json.load(open(os.path.join(EXP084_DIR, "derivation_results.json")))
P_MODEL_A_NARROW = float(_prior["leg_a"]["p_model_deg"])
R2_NARROW = float(_prior["leg_a"]["r_squared"])
assert abs(P_MODEL_A_NARROW - 2.533834586466165) < 1e-9
assert abs(R2_NARROW - 0.36965580905914364) < 1e-9

CENTER_DEG_DEFAULT = 39.0  # Methods A/B convention, unchanged (Fix 3 note)


# ======================================================= fast evaluator
class FastEval:
    """Caches `_geom_derived`'s theta-independent G0/geometry matrix for one
    geometry `g`, so `curve(thetas)` costs O(len(thetas)) matvecs instead of
    O(len(thetas)) full matrix reconstructions. See module docstring."""

    def __init__(self, g, lam_cells):
        self.g = g
        self.lam_cells = lam_cells
        self.gd = dg048._geom_derived(g)
        k = 2.0 * math.pi / lam_cells
        self.k = k
        self.G0 = np.exp(1j * (k * self.gd["r"] - math.pi / 4.0)) / np.sqrt(self.gd["r"])
        self.G0_obl = self.G0 * self.gd["obliquity"]

    def one(self, theta_deg):
        amp = dg048._src_amp(theta_deg, self.k, self.gd)
        E = self.G0 @ amp
        H = self.G0_obl @ amp
        Sx = -np.real(E * np.conj(H))
        bo, bf = amb.window_means(Sx, self.gd["y_lo"], self.gd["obj_y"],
                                   self.g["R_OUT"], self.g["GUARD_OUT"], self.g["W_FLANK"])
        return amb.weber(bo, bf)

    def curve(self, thetas):
        return np.array([self.one(th) for th in thetas])


def verify_fast_eval_bit_identical(fe, sample_thetas):
    """Mandatory pre-use check: FastEval must reproduce
    `dg048.edge_diffraction_c_empty_corrected` EXACTLY (0.0 absolute
    difference) at every sample angle, or this script aborts rather than
    trusting an unverified optimization."""
    rows = []
    for th in sample_thetas:
        orig = dg048.edge_diffraction_c_empty_corrected(th, fe.lam_cells, fe.g)
        fast = fe.one(th)
        diff = abs(orig - fast)
        rows.append(dict(theta=th, orig=orig, fast=fast, abs_diff=diff))
        assert diff == 0.0, f"FastEval NOT bit-identical at theta={th}: diff={diff}"
    return rows


# ======================================================= circular-shift null
def circular_shift_null(thetas, curve, label, n_shifts=None, verbose_every=None):
    """The program's own established 'harder companion' null (LOGBOOK
    Iteration 60 precedent, reused verbatim as exp-084's own
    `phase3_fix_docket_checks.py` implemented it): for every non-trivial
    integer roll offset of `curve`, refit via `free_period_with_widening`
    (same production pipeline, same `thetas`), and report what fraction of
    shifts meet or exceed the UN-shifted fit's own R^2. `n_shifts=None`
    means exhaustive (len(curve)-1); an integer subsamples evenly-strided
    offsets (cost discipline for large curves), disclosed via the returned
    dict's own `exhaustive` flag."""
    curve = np.asarray(curve, dtype=float)
    n = len(curve)
    fit0 = free_period_with_widening(thetas, curve, f"{label}_observed", [])
    p0, r2_0 = fit0["p_star_deg"], fit0["r_squared"]

    if n_shifts is None:
        offsets = list(range(1, n))
        exhaustive = True
    else:
        offsets = sorted(set(int(round(s)) for s in
                              np.linspace(1, n - 1, min(n_shifts, n - 1))))
        exhaustive = False

    shift_r2 = []
    t0 = time.time()
    for i, s in enumerate(offsets):
        shifted = np.roll(curve, s)
        fit_s = free_period_with_widening(thetas, shifted, f"{label}_shift{s}", [])
        shift_r2.append(fit_s["r_squared"])
        if verbose_every and (i + 1) % verbose_every == 0:
            print(f"      [{label}] shift {i+1}/{len(offsets)}  "
                  f"elapsed={time.time()-t0:.1f}s")
    shift_r2 = np.array(shift_r2)
    n_meet = int(np.sum(shift_r2 >= r2_0))
    frac = n_meet / len(shift_r2)
    return dict(label=label, observed_p_star_deg=p0, observed_r2=r2_0,
                window=fit0["window"], n_offsets_tested=len(offsets),
                n_possible_offsets=n - 1, exhaustive=exhaustive,
                n_meet_or_exceed=n_meet, fraction_meet_or_exceed=frac,
                mean_shift_r2=float(np.mean(shift_r2)),
                max_shift_r2=float(np.max(shift_r2)),
                min_shift_r2=float(np.min(shift_r2)),
                elapsed_s=time.time() - t0)


# ======================================================= R5 specificity (reused convention)
def specificity_sweep(p_model, r2, target_grid_lo=1.0, target_grid_hi=15.0,
                       n_targets=60, rel_dev_bar=0.20):
    targets = np.linspace(target_grid_lo, target_grid_hi, n_targets)
    n_clear = sum(1 for t in targets if r2 >= 0.30 and abs(p_model - t) / t <= rel_dev_bar)
    return dict(p_model_deg=p_model, r_squared=r2, n_targets=n_targets,
                n_clear=n_clear, frac_clear=n_clear / n_targets)


def rel_dev(a, b):
    return abs(a - b) / b


# ======================================================= main
def main():
    t_start = time.time()
    out = {}
    print("=" * 78)
    print("exp-085 -- leg (a) wide-window/dense period pin (Iteration 62, "
          "MATERIALS lead)")
    print("Phase 4: corrected spec (phase3_synthesis.md, 7 mandatory fixes)")
    print("=" * 78)

    g = dg065.propagator_geom(CFG_C40)
    fe = FastEval(g, LAM600)

    print("\n[0] FastEval bit-identity verification (mandatory before any use)")
    spot = verify_fast_eval_bit_identical(fe, [36.0, 37.7, 39.0, 40.3, 42.0, 15.0, 60.5])
    for r in spot:
        print(f"    theta={r['theta']:6.2f}  orig={r['orig']:+.15f}  "
              f"fast={r['fast']:+.15f}  abs_diff={r['abs_diff']:.3e}")
    print("    -> bit-identical at every spot-check angle, confirmed.")
    out["fast_eval_verification"] = spot

    # ---------------------------------------------------- Method A
    print("\n[1] METHOD A -- wide/dense fit, existing free_period_with_widening "
          "machinery")
    theta_wide = np.round(np.arange(2.0, 80.0 + 1e-9, 0.02), 6)
    print(f"    domain=[{theta_wide[0]},{theta_wide[-1]}]deg step=0.02deg "
          f"N={len(theta_wide)}")
    t0 = time.time()
    c_wide = fe.curve(theta_wide)
    print(f"    curve evaluated in {time.time()-t0:.1f}s "
          f"(cached-G0 FastEval; see module docstring)")
    ptp_w, mean_w = float(np.ptp(c_wide)), float(np.mean(c_wide))
    print(f"    c_wide: ptp={ptp_w:.6e}  mean={mean_w:.6e}")

    stages_a = []
    fit_wide = free_period_with_widening(theta_wide, c_wide, "method_a", stages_a)
    P_wide, R2_wide = fit_wide["p_star_deg"], fit_wide["r_squared"]
    print(f"    fit (center_deg={CENTER_DEG_DEFAULT}): P_wide={P_wide:.4f}deg  "
          f"R^2_wide={R2_wide:.4f}  window={fit_wide['window']}")

    # Fix 1: mandatory circular-shift null on the full wide curve
    print("\n[1b] FIX 1 -- mandatory circular-shift null on c_wide "
          "(exhaustive, N-1 offsets)")
    null_a = circular_shift_null(theta_wide, c_wide, "method_a",
                                  n_shifts=None, verbose_every=500)
    print(f"    {null_a['n_meet_or_exceed']}/{null_a['n_offsets_tested']} = "
          f"{null_a['fraction_meet_or_exceed']:.1%} of circular shifts meet/exceed "
          f"observed R^2={null_a['observed_r2']:.4f}  "
          f"(elapsed {null_a['elapsed_s']:.1f}s)")
    print("    Interpreted per R10's own deterministic-curve clause: a "
          "self-similarity/specificity")
    print("    reading (what fraction of this curve's own reorderings fit this "
          "well), NOT a")
    print("    measurement-noise significance test -- stated explicitly, not "
          "silently assumed.")
    out["method_a"] = dict(theta_domain=[2.0, 80.0], step=0.02, n_points=len(theta_wide),
                            curve=c_wide.tolist(), ptp=ptp_w, mean=mean_w,
                            stages=stages_a, p_wide_deg=P_wide, r2_wide=R2_wide,
                            window=fit_wide["window"], circular_shift_null=null_a)

    # ---------------------------------------------------- Method B
    print("\n[2] METHOD B -- independent dense FFT in sin(theta), Hann-tapered "
          "(Fix 6)")
    u_lo, u_hi = math.sin(math.radians(2.0)), math.sin(math.radians(80.0))
    N_FFT = 32768
    u_grid = np.linspace(u_lo, u_hi, N_FFT)
    theta_u = np.degrees(np.arcsin(u_grid))
    t0 = time.time()
    c_u = fe.curve(theta_u)
    print(f"    curve evaluated on sin(theta)-uniform grid, N={N_FFT}, "
          f"in {time.time()-t0:.1f}s")
    window = np.hanning(N_FFT)
    c_u_tapered = (c_u - np.mean(c_u)) * window
    du = (u_hi - u_lo) / (N_FFT - 1)
    N_PAD = 131072
    spec = np.fft.rfft(c_u_tapered, n=N_PAD)
    freqs = np.fft.rfftfreq(N_PAD, d=du)  # cycles per unit sin(theta)
    power = np.abs(spec) ** 2

    # primary peak search restricted to periods in [1,15]deg (this
    # sub-thread's own established scoring range), converted via the
    # SAME Tc=radians(P)*cos(center_deg) convention _free_period_search uses
    cos_c = math.cos(math.radians(CENTER_DEG_DEFAULT))

    def freq_to_period_deg(f):
        if f <= 0:
            return float("inf")
        T_sintheta = 1.0 / f
        return math.degrees(T_sintheta / cos_c)

    period_of_freq = np.array([freq_to_period_deg(f) for f in freqs[1:]]) # skip DC
    mask_primary = (period_of_freq >= 1.0) & (period_of_freq <= 15.0)
    power_primary = power[1:][mask_primary]
    freqs_primary = freqs[1:][mask_primary]
    if len(power_primary) == 0:
        raise RuntimeError("no FFT bins fall in the primary [1,15]deg period range")
    i_peak = int(np.argmax(power_primary))
    f_peak = freqs_primary[i_peak]
    P_fft = freq_to_period_deg(f_peak)
    P1 = float(power_primary[i_peak])

    # full-spectrum disclosure: largest peak anywhere (not discarded)
    i_peak_full = int(np.argmax(power[1:])) + 1
    f_peak_full = freqs[i_peak_full]
    P_fft_full = freq_to_period_deg(f_peak_full)

    # second-highest local max within primary range, excluding a small
    # neighborhood of the primary peak (peak-sharpness diagnostic)
    guard = max(1, int(0.02 * len(power_primary)))
    masked_for_p2 = power_primary.copy()
    lo_ex = max(0, i_peak - guard)
    hi_ex = min(len(masked_for_p2), i_peak + guard + 1)
    masked_for_p2[lo_ex:hi_ex] = -1.0
    P2 = float(np.max(masked_for_p2)) if np.any(masked_for_p2 >= 0) else 0.0
    P2_over_P1 = P2 / P1 if P1 > 0 else float("inf")

    half = P1 / 2.0
    above = power_primary >= half
    idx_above = np.where(above)[0]
    if len(idx_above) > 0:
        fwhm_bins = idx_above[-1] - idx_above[0] + 1
        fwhm_frac = fwhm_bins / len(power_primary)
    else:
        fwhm_frac = 0.0

    print(f"    primary-range peak: P_fft={P_fft:.4f}deg  (bin power={P1:.3e})")
    print(f"    full-spectrum peak (disclosed, not discarded): "
          f"P_fft_full={P_fft_full:.4f}deg" +
          ("  [SAME as primary]" if abs(P_fft_full - P_fft) < 1e-9 else
           "  [DIFFERENT -- largest peak overall is OUTSIDE [1,15]deg]"))
    print(f"    peak sharpness: P2/P1={P2_over_P1:.4f}   "
          f"FWHM/(primary-range span)={fwhm_frac:.4f}")
    out["method_b"] = dict(n_fft=N_FFT, n_pad=N_PAD, tapered="hann",
                            p_fft_deg=P_fft, p_fft_full_deg=P_fft_full,
                            p1_power=P1, p2_power=P2, p2_over_p1=P2_over_P1,
                            fwhm_frac_of_primary_range=fwhm_frac)

    # ---------------------------------------------------- Method C
    print("\n[3] METHOD C -- 37 sliding sub-windows, center_deg=theta_c fix "
          "(Fix 3), primary instrument (Fix 7)")
    theta_centers = np.arange(5.0, 77.0 + 1e-9, 2.0)
    assert len(theta_centers) == 37, len(theta_centers)
    sub_results = []
    t0 = time.time()
    null_sample_idx = set(range(0, 37, 4))  # 10 of 37, evenly spaced (Fix 2)
    null_samples = []
    for i, thc in enumerate(theta_centers):
        sub_theta = np.round(np.arange(thc - 3.0, thc + 3.0 + 1e-9, 0.2), 6)
        c_sub = fe.curve(sub_theta)
        stages_sub = []
        fit_sub = free_period_with_widening(sub_theta, c_sub, f"subwin_{thc:.1f}",
                                             stages_sub)
        # -------- Fix 3: correct center_deg=39.0 hardcode to theta_c --------
        Tc_wrong = math.radians(fit_sub["p_star_deg"]) * cos_c
        p_local_corrected = math.degrees(Tc_wrong / math.cos(math.radians(thc)))
        rec = dict(theta_c=float(thc), p_local_reported_at_39=fit_sub["p_star_deg"],
                   p_local_corrected=p_local_corrected, r2_local=fit_sub["r_squared"],
                   window=fit_sub["window"])
        if i in null_sample_idx:
            null_i = circular_shift_null(sub_theta, c_sub, f"subwin_{thc:.1f}",
                                          n_shifts=None)
            rec["circular_shift_null"] = null_i
            null_samples.append(null_i)
        sub_results.append(rec)
    print(f"    37 sub-windows fit in {time.time()-t0:.1f}s "
          f"({len(null_samples)}/37 also circular-shift-null-tested, Fix 2)")

    frac_recovered = sum(1 for r in sub_results if r["r2_local"] >= 0.30) / len(sub_results)
    local_periods = np.array([r["p_local_corrected"] for r in sub_results
                               if r["r2_local"] >= 0.30])
    local_thetas = np.array([r["theta_c"] for r in sub_results if r["r2_local"] >= 0.30])
    if len(local_periods) >= 2:
        spread = (float(np.max(local_periods)) - float(np.min(local_periods))) / float(np.median(local_periods))
        from scipy.stats import spearmanr
        rho, rho_p = spearmanr(local_thetas, local_periods)
        rho = float(rho)
    else:
        spread = float("nan")
        rho = float("nan")
        rho_p = float("nan")

    null_pass_rate = (sum(1 for n in null_samples if n["fraction_meet_or_exceed"] >= 0.40)
                       / len(null_samples)) if null_samples else float("nan")
    print(f"    frac_recovered={frac_recovered:.3f}  spread={spread:.4f}  "
          f"rho={rho:.4f} (p={rho_p:.4f})")
    print(f"    Fix 2: {sum(1 for n in null_samples if n['fraction_meet_or_exceed']>=0.40)}/"
          f"{len(null_samples)} sampled sub-windows have circular-shift pass "
          f"rate >=40% (self-similarity-comparable-to-exp-084-precedent)")

    out["method_c"] = dict(theta_centers=theta_centers.tolist(), sub_results=sub_results,
                            frac_recovered=frac_recovered, spread=spread, rho=rho,
                            rho_pvalue=rho_p, null_sample_pass_rate=null_pass_rate,
                            n_null_sampled=len(null_samples))

    # ---------------------------------------------------- Fix 5: classification
    print("\n[4] CLASSIFICATION (a) -- Fix 5's 4-way Method C decision table")
    reliability_note = ""
    if not math.isnan(null_pass_rate) and null_pass_rate >= 0.40:
        reliability_note = ("UNRELIABLE per Fix 2 (sampled sub-window "
                             "circular-shift pass rate >=40%) -- ")
    if frac_recovered >= 0.80 and spread <= 0.15:
        classification_a = "STABLE"
    elif frac_recovered >= 0.80 and spread > 0.50 and abs(rho) >= 0.5:
        classification_a = "STRONG COHERENT CHIRP"
    elif frac_recovered >= 0.80 and 0.15 < spread <= 0.50 and abs(rho) >= 0.5:
        classification_a = "DRIFTING"
    elif frac_recovered < 0.80 or (spread > 0.50 and abs(rho) < 0.5):
        classification_a = "NOT STABLY PERIODIC"
    else:
        classification_a = "UNCLASSIFIED (residual gap -- report raw numbers)"
    if reliability_note and classification_a == "STABLE":
        classification_a = "DRIFTING (downgraded from STABLE per Fix 2)"
    print(f"    {reliability_note}CLASSIFICATION (a) = {classification_a}")

    fft_corroborates = (P2_over_P1 <= 0.5) and (fwhm_frac <= 0.15)
    print(f"    Method B corroboration (soft signal, Fix 7 -- does not veto "
          f"Method C): P2/P1<=0.5 AND FWHM<=0.15 -> {fft_corroborates}")

    print("\n[5] CLASSIFICATION (b) -- Fix 4's 4-band precedence "
          "(only meaningful if (a) is STABLE or a chirp with a well-defined "
          "asymptote)")
    rd_wide_fft = rel_dev(P_wide, P_fft) if P_wide else float("inf")
    mean_wf = (P_wide + P_fft) / 2.0
    disagreement = abs(P_wide - P_fft) / mean_wf > 0.10
    if disagreement:
        classification_b = "METHOD DISAGREEMENT"
    elif (rel_dev(P_wide, P_EDGE_A) <= 0.10 and rel_dev(P_fft, P_EDGE_A) <= 0.10
          and null_a["fraction_meet_or_exceed"] < 0.15 and R2_wide >= 0.55):
        classification_b = "NARROW WINDOW UNDERSHOT -- WIDE FIT MOVES TOWARD P_EDGE_A"
    elif (rel_dev(P_wide, P_MODEL_A_NARROW) <= 0.05 and rel_dev(P_fft, P_MODEL_A_NARROW) <= 0.05
          and rel_dev(P_wide, P_EDGE_A) > 0.20 and rel_dev(P_fft, P_EDGE_A) > 0.20):
        classification_b = "WIDE FIT CONFIRMS 2.5338, P_EDGE_A EXCLUDED"
    else:
        classification_b = "NEITHER -- THIRD VALUE / CATCH-ALL"
    print(f"    P_wide={P_wide:.4f}  P_fft={P_fft:.4f}  "
          f"rel_dev(P_wide,P_fft vs mean)={rd_wide_fft:.4f}")
    print(f"    rel_dev(P_wide,P_edge_A)={rel_dev(P_wide, P_EDGE_A):.4f}  "
          f"rel_dev(P_fft,P_edge_A)={rel_dev(P_fft, P_EDGE_A):.4f}")
    print(f"    rel_dev(P_wide,P_model_a_narrow)={rel_dev(P_wide, P_MODEL_A_NARROW):.4f}  "
          f"rel_dev(P_fft,P_model_a_narrow)={rel_dev(P_fft, P_MODEL_A_NARROW):.4f}")
    print(f"    CLASSIFICATION (b) = {classification_b}")

    # ---------------------------------------------------- R5 control
    spec_wide = specificity_sweep(P_wide, R2_wide)
    print(f"\n[6] R5 specificity control on (P_wide,R2_wide): "
          f"{spec_wide['n_clear']}/{spec_wide['n_targets']} targets "
          f"({spec_wide['frac_clear']:.1%})")
    out["specificity_control_wide"] = spec_wide

    elapsed = time.time() - t_start
    print(f"\n[7] SUMMARY")
    print(f"    (a) Method-C-primary classification: {classification_a}")
    print(f"        frac_recovered={frac_recovered:.3f}  spread={spread:.4f}  "
          f"rho={rho:.4f}  FFT-corroborates={fft_corroborates}")
    print(f"    (b) period-value classification: {classification_b}")
    print(f"        P_wide={P_wide:.4f}deg (R^2={R2_wide:.4f}, circular-shift "
          f"{null_a['fraction_meet_or_exceed']:.1%})  P_fft={P_fft:.4f}deg")
    print(f"    total elapsed = {elapsed:.1f}s")

    out["classification_a"] = classification_a
    out["classification_b"] = classification_b
    out["fft_corroborates"] = fft_corroborates
    out["p_edge_a"] = P_EDGE_A
    out["p_model_a_narrow"] = P_MODEL_A_NARROW
    out["r2_narrow"] = R2_NARROW
    out["elapsed_s"] = elapsed

    out_path = os.path.join(HERE, "derivation_results.json")
    json.dump(out, open(out_path, "w"), indent=2)
    print(f"\n    results written to {out_path}")
    return out


if __name__ == "__main__":
    main()
