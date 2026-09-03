"""exp-106 -- Floor-Gating, Settling, Risk-Propagation, and the
Fixed-Absolute-Thickness Control for `kappa_window`. Panel Iteration 83.
Lead seat (rotation): QUANTUM OPTICS. Frozen spec: NOTES.md (Predictions
committed to git strictly BEFORE this file's first real run, house
discipline). Change rationale: phase2_redteam_audit.md (7 mandatory
fixes, all five blind critiques' core findings independently re-verified
by Red Team from primitives; verdict PROCEED-WITH-MANDATORY-FIXES,
Checkpoint criterion 4 does NOT fire).

Instrument-extension cycle, diagnostic only -- T1: N/A, zero `lab/` diff,
no mechanism proposed or varied. Executes exp-105's own Reconciled
Iteration-83 queue, Tier 1 items 1-4 in full:

  1. Floor-gate `kappa_window`/`window_stats()`'s own output at r=156/312
     (self-similar), and stop discarding r=312's raw window/point-channel
     data.
  2. A settling-independence leg on `kappa_window` ITSELF (not merely
     `kappa_region_point`, already done at exp-105) at r=156 and r=312.
  3. `p3_trusted` -- a risk-propagation gate on P3's own scored verdict,
     symmetric to exp-105's `p4_156_trusted`.
  4. Re-run the `kappa_window`/P3 bridge on exp-052's fixed-absolute-
     thickness `graded_black_shell` variant at r=156/312 -- the
     discriminating control between the geometric-window (z/z_R)
     hypothesis and the growing-electrical-thickness materials
     hypothesis MATERIALS named at exp-105 Phase 5.

Director's synthesis decisions (Phase 3, full record in NOTES.md Panel
record):

  - All 7 of Red Team's mandatory fixes ADOPTED. One (fix 1's "zero
    marginal cost" framing) implemented as Red Team itself corrected it
    (Attack 8): `_run()` now also returns the article scene's `sigma_e`
    grid, a small code change, still zero new `Sim.run()` calls.
  - Director's own cost optimization, disclosed not hidden: an EMPTY
    scene never calls `materials.pec_disk`/`materials.graded_black_shell`
    -- it is therefore mathematically IDENTICAL between the self-similar
    and fixed-absolute-thickness families at a given (r, STEPS). Each
    empty-scene capture is run ONCE and reused for both families' P3/P4-
    style bridges, cutting the Phase-1 proposal's own disclosed 16-call
    budget to **12 real `Sim.run()` calls** (r=78 contributing 0 to
    both families, unchanged) -- a free, physically-justified reduction,
    not a scope cut (every Tier-1 item is still executed in full).
  - Red Team's mandatory fix 3 (a hard noise-floor gate on the near-zero
    shape_ratio denominator, R13/R14 discipline) is implemented with a
    UNITS CORRECTION: Red Team's own literal proposal compared a
    dimensionless kappa_window difference against a raw per-cell
    intensity RMS (mismatched units). Director's fix: the noise floor is
    expressed as `3 * FLOOR_FRAC * |kappa_156|` (a RELATIVE tolerance,
    dimensionally consistent with `floor_gate()`'s own `floor =
    floor_frac * rms` convention, applied in kappa's own units) --
    applied symmetrically to BOTH families' shape_ratio, closing Red
    Team's own Attack 7 (inconsistent rigor between p3_trusted and
    shape_ratio_fixedabs) for both, not just the fixed-abs family.
  - Mandatory fix 4 (MATERIALS' realizability sentence, Red Team's
    OVERRIDE + replacement text) implemented verbatim as Red Team wrote
    it in phase2_redteam_audit.md Sec 3.1 item 4.
  - Mandatory fixes 2, 5, 6, 7 implemented as specified.
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

from lab import Sim, materials                      # noqa: E402
from lab import sections as sc                       # noqa: E402
from lab import thermo_sidecar as ts                 # noqa: E402

EXP105_DIR = os.path.join(ROOT, "experiments", "105-t28-kappa-scale-bridge")

# ================================================================ T8's own formula chain (exp-030/exp-105, reused verbatim -- self-similar family)
DX_M = 30.0e-9
R_BASE = 78
N0, ABSORB, EDGE, TAPER = 560, 40, 40, 40
CX0, CY0, SRC_X0 = 252, 280, 64
R_CORE0 = 30
STEPS0 = 3200
SIGMA_MAX0 = 0.5
CPL_600 = 20
COURANT_FRAC = 0.32
LAMBDA_CELLS = 20.0
D_EFF = 77.0

DENSE_PITCH = 2
H_REGION_WIDE = 5
H_REGION_POINT = 0
FLOOR_FRAC = 0.10
STABILITY_TOL = 0.20        # kappa settling tolerance (exp-103's established value, reused)
PHASE_STABILITY_TOL = 0.20  # rad (unused this cycle -- window_stats() pools |Ez|^2 only, no
                            # complex mean, so there is no delta_phi_window to settle-check;
                            # kept as a named constant only for cross-file convention parity)

NETD_BAND_K = (0.020, 0.050)

# ---------------------------------------------- fixed-absolute-thickness family (exp-052)
ABS_THICKNESS = 48          # cells, HELD CONSTANT across r (exp-052's own established value)
SIGMA_MAX_FIXED = 0.5       # HELD CONSTANT across r (not rescaled by kappa)

# ---------------------------------------------- ledger box/ref convention (exp-028/030, reused verbatim)
BOX_A_MARGIN0 = 32
BOX_B_MARGIN0 = 57
REF_HH0 = 60

# ---------------------------------------------- shape_ratio classification bands (item 4, pre-registered)
SHAPE_RATIO_FIXEDABS_CONFIRM = 8.0    # <= this: CONFIRMS growing-electrical-thickness hypothesis
SHAPE_RATIO_FIXEDABS_REFUTE = 14.8    # >= this: REFUTES it (within 25% of self-similar's 19.79)
ABS_RATIO_BAND = 2.0                  # factor-of-2 band on the raw cross-family absolute ratio


def kappa_of(r):
    return r / R_BASE


def geom(r):
    """Self-similar family, T8's own formula chain -- BYTE-FOR-BYTE
    reused from exp-105's `geom()` for every domain/object field (Gate P0
    depends on exact reproduction), extended with the ledger box/ref
    fields (new this cycle, mandatory fix 1)."""
    k = kappa_of(r)
    N = round(N0 * k)
    CX = round(CX0 * k)
    CY = round(CY0 * k)
    SRC_X = round(SRC_X0 * k)
    STEPS = round(STEPS0 * k)
    R_CORE = round(R_CORE0 * k)
    R_COAT = r
    sigma_max = SIGMA_MAX0 / k
    tau_shell = sigma_max * (R_COAT - R_CORE)
    behind_x_lo = CX + R_COAT + 27
    behind_x_hi = CX + R_COAT + 127
    behind_y_lo = CY - 20
    behind_y_hi = CY + 20
    dense_x = list(range(CX + R_COAT + 22, CX + R_COAT + 127, DENSE_PITCH))
    z_over_zr = D_EFF * LAMBDA_CELLS / (r ** 2)
    predicted_period = LAMBDA_CELLS * D_EFF / r
    nyq_margin = predicted_period / (2.0 * DENSE_PITCH)
    # ledger box/ref (exp-028/030's own `_rescaled_geom` convention, reused verbatim,
    # margins scaled by kappa exactly as that module's own ratio-scaled hw_a/hw_b/ref_hh)
    box_a_hw = R_COAT + round(BOX_A_MARGIN0 * k)
    box_b_hw = R_COAT + round(BOX_B_MARGIN0 * k)
    box_a = (CX - box_a_hw, CX + box_a_hw, CY - box_a_hw, CY + box_a_hw)
    box_b = (CX - box_b_hw, CX + box_b_hw, CY - box_b_hw, CY + box_b_hw)
    ref = (CX, CY, round(REF_HH0 * k))
    return dict(r=r, k=k, N=N, CX=CX, CY=CY, SRC_X=SRC_X, STEPS=STEPS,
                R_CORE=R_CORE, R_COAT=R_COAT, sigma_max=sigma_max,
                tau_shell=tau_shell,
                behind=(behind_x_lo, behind_x_hi, behind_y_lo, behind_y_hi),
                dense_x=dense_x, n_dense=len(dense_x),
                z_over_zr=z_over_zr, predicted_ripple_period=predicted_period,
                nyquist_margin=nyq_margin, box_a=box_a, box_b=box_b, ref=ref,
                family="selfsim")


def geom_fixedabs(r):
    """Fixed-absolute-thickness family (exp-052's `design_geometry.py`
    formulas, r_in_fixedabs/sigma_max_fixedabs, generalized to r=156/312
    here for the first time). Domain construction (N/CX/CY/SRC_X/STEPS/
    behind/dense_x/box_a/box_b/ref/z_over_zr/nyquist_margin) is IDENTICAL
    to the self-similar family at the same r (only R_CORE/sigma_max/
    tau_shell differ, mandatory fix 3's own point -- confirmed identical
    domain by construction, not merely by assertion)."""
    g = dict(geom(r))
    r_core = r - ABS_THICKNESS
    sigma_max = SIGMA_MAX_FIXED
    g.update(R_CORE=r_core, sigma_max=sigma_max,
              tau_shell=sigma_max * (r - r_core), family="fixedabs")
    return g


# printed assertions (house discipline, exp-052's own pattern, reused)
assert geom(78)["R_CORE"] == geom_fixedabs(78)["R_CORE"] == 30, "families must coincide at r=78"
assert abs(geom(78)["sigma_max"] - geom_fixedabs(78)["sigma_max"]) < 1e-12, \
    "families must coincide at r=78 (sigma_max)"
for _r in (78, 156, 312):
    assert abs(geom_fixedabs(_r)["tau_shell"] - 24.0) < 1e-9, f"fixed-abs tau_shell drifted at r={_r}"
    assert abs(geom(_r)["tau_shell"] - 24.0) < 1e-9, f"self-similar tau_shell drifted at r={_r}"


def nyquist_trust_tier(margin):
    if margin >= 2.0:
        return "TRUSTED"
    if margin >= 1.0:
        return "MARGINAL-REDUCED-CONFIDENCE"
    return "UNRESOLVED-BY-CONSTRUCTION"


DISCLAIMER = ("Raw physical intensity ratios and an absorbed-power sanity "
              "ledger only -- no Weber-contrast or C_thr(L) perceptual scoring "
              "is performed this cycle; not a claim about human visibility. "
              "The Nyquist-margin trust tier is a reused DENSE_X point-sampling "
              "aliasing proxy, not an independently-derived box-integral aliasing "
              "bound for window_stats() (mandatory fix 7). " +
              ts.netd_disposition(0.0, NETD_BAND_K)["disclaimer"] + ".")


def _run(with_article, steps, g, capture_sigma_e=False):
    sim = Sim(g["N"], g["N"], cells_per_lambda=CPL_600, courant_frac=COURANT_FRAC, absorb=ABSORB)
    if with_article:
        materials.pec_disk(sim, g["CX"], g["CY"], g["R_CORE"])
        materials.graded_black_shell(sim, g["CX"], g["CY"], g["R_CORE"], g["R_COAT"],
                                      sigma_max=g["sigma_max"])
    sim.add_line_source(g["SRC_X"], angle_deg=0.0, profile="plane", edge=EDGE)
    sim.run(steps)
    cap = sc.full_capture(sim)
    sigma_e = sim.sigma_e.copy() if (with_article and capture_sigma_e) else None
    return cap, sigma_e


# ================================================================ point/region readout primitives (exp-102/103/104/105's own formulas, byte-for-byte)
def block_mean_intensity(ez, x, y, h):
    xs = slice(x - h, x + h + 1)
    ys = slice(y - h, y + h + 1)
    return float(np.mean(np.abs(ez[xs, ys]) ** 2))


def point_intensity(ez, x, y):
    return float(np.abs(ez[x, y]) ** 2)


def kappa_region_wide(ez_empty, ez_article, x, y, h=H_REGION_WIDE):
    i_e = block_mean_intensity(ez_empty, x, y, h)
    i_a = block_mean_intensity(ez_article, x, y, h)
    return (i_a / i_e if i_e != 0 else float("inf")), i_e, i_a


def kappa_region_point(ez_empty, ez_article, x, y):
    i_e = point_intensity(ez_empty, x, y)
    i_a = point_intensity(ez_article, x, y)
    return (i_a / i_e if i_e != 0 else float("inf")), i_e, i_a


def wrap_phase(phi):
    wrapped = (phi + math.pi) % (2 * math.pi) - math.pi
    if wrapped <= -math.pi:
        wrapped += 2 * math.pi
    return wrapped


def delta_phi_wide(ez_empty, ez_article, x, y, h=H_REGION_WIDE):
    xs = slice(x - h, x + h + 1)
    ys = slice(y - h, y + h + 1)
    mean_e = complex(np.mean(ez_empty[xs, ys]))
    mean_a = complex(np.mean(ez_article[xs, ys]))
    if mean_e == 0:
        return float("nan")
    return wrap_phase(float(np.angle(mean_a / mean_e)))


def delta_phi_point(ez_empty, ez_article, x, y):
    ez_e, ez_a = ez_empty[x, y], ez_article[x, y]
    if ez_e == 0:
        return float("nan")
    return wrap_phase(float(np.angle(ez_a / ez_e)))


def window_stats(ez, x_lo, x_hi, y_lo, y_hi):
    block = np.abs(ez[x_lo:x_hi, y_lo:y_hi]) ** 2
    return dict(mean=float(np.mean(block)), std=float(np.std(block)),
                min=float(np.min(block)), max=float(np.max(block)))


def floor_gate(pool_values, label, floor_frac=FLOOR_FRAC):
    """Byte-for-byte reused from exp-105's `floor_gate()`."""
    arr = np.asarray(pool_values, dtype=float)
    rms = float(np.sqrt(np.mean(np.square(arr))))
    floor = floor_frac * rms
    passes = [bool(v >= floor) for v in arr]
    n_unresolved = sum(1 for p in passes if not p)
    print(f"  [floor gate: {label}] n={len(arr)} rms={rms:.6e} floor={floor:.6e} "
          f"n_unresolved={n_unresolved}")
    return dict(rms=rms, floor=floor, n_unresolved=n_unresolved,
                frac_unresolved=n_unresolved / len(arr))


def floor_gate_window(ez_empty, x_lo, x_hi, y_lo, y_hi, label, floor_frac=FLOOR_FRAC):
    """Mandatory fix (item 1, proposal Sec 2c): floor-gates
    `window_stats()`'s own per-cell EMPTY-scene intensity block by reusing
    `floor_gate()` verbatim (R4) -- the load-bearing gap this cycle closes.
    Called on the empty-scene reference only, matching this file's own
    established convention (the question is whether kappa_window's
    DENOMINATOR sits above the solver's own numerical noise floor)."""
    block_e = np.abs(ez_empty[x_lo:x_hi, y_lo:y_hi]) ** 2
    return floor_gate(block_e.ravel().tolist(), label, floor_frac=floor_frac)


def settling_pass_window(kappa_1x, kappa_2x, tol=STABILITY_TOL):
    rel_change = abs(kappa_2x - kappa_1x) / abs(kappa_1x) if kappa_1x != 0 else float("inf")
    return bool(rel_change <= tol), rel_change


def ledger_check(cap_article, cap_empty, sigma_e_article, g, n_bins=26):
    """Mandatory fix 1 (EM/THERMODYNAMICS, converged; Red Team Attacks
    4/8/9): an absorbed/extinguished-power sanity ledger on the
    already-captured article/empty pair. `sections.widths()` gives
    sigma_abs/sigma_ext (the T9-comparable quantity, box-independence
    cross-checked via box_a/box_b); `sections.radial_absorbed_power()`
    gives the radially-binned Joule-dissipation density (spatial sanity:
    is absorption concentrated in the shell annulus, ~zero inside the PEC
    core). Zero new FDTD calls -- reuses the article/empty captures
    already scheduled for kappa_window's own floor-gate/settling work.
    Per Red Team Attack 9: this is NOT a re-run of exp-052's own
    hollow-vs-PEC-cored delta methodology (that needs a third, new
    capture, a real cost, not mandatory this cycle -- Tier 2)."""
    wa = sc.widths(cap_article, cap_empty, g["box_a"], g["ref"])
    wb = sc.widths(cap_article, cap_empty, g["box_b"], g["ref"])
    box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])
    centers, bins, total = sc.radial_absorbed_power(
        cap_article, sigma_e_article, g["CX"], g["CY"], g["R_COAT"], n_bins=n_bins)
    _, _, core_total = sc.radial_absorbed_power(
        cap_article, sigma_e_article, g["CX"], g["CY"], g["R_CORE"], n_bins=n_bins)
    core_frac = core_total / total if total else float("nan")
    p_abs_box = wa["sigma_abs"] * wa["i_inc"]
    closure = abs(total - p_abs_box) / abs(p_abs_box) if p_abs_box else float("nan")
    return dict(sigma_abs=wa["sigma_abs"], sigma_ext=wa["sigma_ext"],
                abs_ext_ratio=wa["sigma_abs"] / wa["sigma_ext"], box_dev=box_dev,
                radial_total=total, core_power=core_total, core_frac=core_frac,
                closure=closure, i_inc=wa["i_inc"], n_bins=n_bins,
                bins=bins.tolist(), bin_centers=centers.tolist())


def shape_ratio_fit(k78, k156, k312, z78, z156, z312):
    """Byte-for-byte the same 2-point-fit-vs-held-out-r=78 construction
    exp-105's own `run.py::main()` used, factored into a reusable function
    (R4 -- one formula, called for both families, not hand-duplicated)."""
    x78, x156, x312 = math.sqrt(z78), math.sqrt(z156), math.sqrt(z312)
    BA = (k156 - k312) / (x156 - x312)
    CA = k156 - BA * x156
    pred78_A = CA + BA * x78
    missA = abs(pred78_A - k78) / abs(k78)
    BB = (k156 - k312) / (x156 ** 2 - x312 ** 2)
    CB = k156 - BB * x156 ** 2
    pred78_B = CB + BB * x78 ** 2
    missB = abs(pred78_B - k78) / abs(k78)
    shape_ratio = (k78 - k156) / (k156 - k312) if (k156 - k312) != 0 else float("inf")
    return dict(x78=x78, x156=x156, x312=x312, model_A_B=BA, model_A_miss=missA,
                model_B_B=BB, model_B_miss=missB, shape_ratio=shape_ratio)


def noise_floor_flag(k156, k312, floor_frac=FLOOR_FRAC):
    """Red Team's mandatory fix 3 (Attack 7, R13/R14 discipline), UNITS-
    CORRECTED by the Director (see module docstring): Red Team's own
    literal proposal compared a dimensionless kappa difference against a
    raw per-cell intensity RMS (mismatched units). This version expresses
    the noise floor as a RELATIVE tolerance in kappa's own units --
    `3 * FLOOR_FRAC * |k156|` -- dimensionally consistent with
    `floor_gate()`'s own `floor = floor_frac * rms` convention, applied
    symmetrically to both families (closing Red Team's own inconsistent-
    rigor finding for both, not just the fixed-abs family)."""
    denom = k156 - k312
    noise_floor = 3.0 * floor_frac * abs(k156)
    return dict(denom=denom, noise_floor=noise_floor,
                noise_dominated=bool(abs(denom) < noise_floor))


# ================================================================ predictions text (R23: single source of truth, generated BEFORE any FDTD call)
def build_predictions_text(g78, g156, g312, g156_fa, g312_fa):
    return f"""PREDICTIONS (pre-registered, exp-106, Panel Iteration 83)

{DISCLAIMER}

**Gate P0** (ground-truth recovery, zero cost). geom(78/156/312)
reproduces exp-105's own committed geometry EXACTLY on every shared field
(N, CX, CY, SRC_X, STEPS, R_CORE, sigma_max, behind window, dense_x).
Falsified by ANY mismatch -> halt, do not trust anything downstream.

**Reproduction check** (Gate-P1-equivalent for kappa_window, zero new
information but load-bearing). Fresh r=156/312 self-similar captures'
kappa_window must reproduce exp-105's own committed values
({EXP105_DIR}/results.json) to <1e-6 relative. Falsified -> halt before
trusting this cycle's own floor-gate/settling diagnostics built on the
same fields.

**Item 1 (floor-gate window_stats()'s own output, self-similar family,
r=156/312).** Predicted PASS (frac_unresolved < 2%) at r=156, by direct
analogy to the clean dense_x floor gates exp-105 already found at r=78/156
(n_unresolved=0 both). At r=312: BORDERLINE predicted (frac_unresolved
possibly >10%) -- the empty-scene window-box mean intensity itself falls
steeply with r, consistent with kappa_window's own ~1,100x collapse being
partly a shrinking-signal, not shrinking-noise, story. Falsified (i.e.
the floor concern unwarranted) if frac_unresolved stays <2% at r=312 too.
Because floor_gate_window() only ever touches the EMPTY-scene capture, and
an empty scene never depends on family, this result is SHARED between the
self-similar and fixed-abs families at a given r (computed once, reused).
r=312's own wide_channel/point_channel/delta_phi (self-similar only,
DENSE_X machinery) are persisted in full this cycle -- the specific
"stop discarding" gap exp-105's own Phase 5 named.

**Item 2 (settling-independence leg on kappa_window itself, both
families, r=156 and r=312).** r=156: predicted PASS (rel_change<=0.20),
by direct analogy to exp-105's own landslide point-channel settling pass
at this r (0/53 failures). r=312: genuinely uncertain -- no settling leg
has ever been run there for ANY channel; this is the most urgent leg in
the whole cycle. Falsifiable band: rel_change<=0.20 -> PASS; >0.20 -> FAIL
(kappa_window_312 itself, not just P4's dense_x readings, may be
settling-artifact-contaminated).

**Item 3 (p3_trusted, self-similar; shape_ratio_fixedabs_trusted,
fixed-abs -- risk-propagation gates symmetric in KIND, not just name, to
exp-105's own p4_156_trusted).**
p3_trusted = settling_pass_window_312_selfsim AND (nyquist_tier(312)=="TRUSTED").
shape_ratio_fixedabs_trusted = settling_pass_window_312_fixedabs AND (nyquist_tier(312)=="TRUSTED").
**Both predicted FALSE at r=312 by construction** -- nyquist_margin(312)=
{g312['nyquist_margin']:.3f} (MARGINAL-REDUCED-CONFIDENCE) is a fixed
property of the domain geometry (identical between families, mandatory
fix 3/Red-Team-verified), not something either family's new capture can
move. This is a structural, disclosed prediction, not a coin flip.
Additionally, per Red Team's mandatory fix 3 (units-corrected, see
module docstring): a `noise_floor_flag` is scored on BOTH families'
shape_ratio denominator (kappa_156 - kappa_312), flagging
NOISE-DOMINATED-UNRELIABLE if |denom| < 3*FLOOR_FRAC*|kappa_156|,
independent of the hard nyquist/settling gate above.

**Item 4 (fixed-absolute-thickness control's own shape_ratio -- the
falsifiable heart of this cycle).** The self-similar and fixed-abs
families share IDENTICAL domain/z_over_zr geometry at each r (only
R_CORE/sigma_max differ) -- so a pure geometric-window diffraction effect
predicts shape_ratio_fixedabs approx EQUAL to self-similar's own 19.79
(PHOTONICS' own sharper absolute-ratio test, mandatory fix 2, scores this
directly: abs_ratio(r) = kappa_window_fixedabs(r)/kappa_window_selfsim(r)
at r=156/312, band: within a factor of {ABS_RATIO_BAND:.1f} of 1.0 ->
geometric dominance corroborated at the absolute-magnitude level).
Pre-registered classification on shape_ratio_fixedabs itself:
<= {SHAPE_RATIO_FIXEDABS_CONFIRM:.1f} -> CONFIRMS the growing-electrical-
thickness hypothesis as a material driver;
>= {SHAPE_RATIO_FIXEDABS_REFUTE:.1f} -> REFUTES it (geometric z/z_R window
effect dominates regardless of coating thickness law); between -> AMBIGUOUS,
disclosed as such. Per mandatory fix 6 (PHOTONICS/Red Team): even the
CONFIRM band (shape_ratio<=8.0, implied exponent n<=3.0 via the forced
shape_ratio===2^n identity exp-105 derived) sits ABOVE this program's own
cited edge-diffraction theory range (n~=1-2) -- neither pre-registered
outcome reconciles this cycle's own two-hypothesis discriminator with
known diffraction physics; it can only arbitrate between two
program-internal hypotheses. Per mandatory fix 1 (EM/THERMODYNAMICS,
Red-Team-corrected cost characterization): a `radial_absorbed_power`/
`widths()` sanity ledger is run on BOTH families at r=156/312 -- the
fixed-abs family reaches R_CORE/R_COAT={geom_fixedabs(156)['R_CORE']}/156=
{geom_fixedabs(156)['R_CORE']/156:.3f} and
{geom_fixedabs(312)['R_CORE']}/312={geom_fixedabs(312)['R_CORE']/312:.3f},
both past T9's only-validated core-energetically-incidental anchor of
0.385 -- this ledger checks (not re-validates from scratch) that absorbed
power stays physically concentrated in the shell annulus (near-zero
inside the PEC core) and that box-independence (box_dev) holds, before
shape_ratio_fixedabs is trusted as a clean two-hypothesis discriminator.
Not a re-run of exp-052's own hollow-vs-PEC-cored delta test (a real,
new-FDTD-call cost, Tier 2, not mandatory this cycle -- Red Team Attack 9).

**Realizability note (mandatory fix 4, Red Team's own replacement text,
verbatim, correcting a stale claim in the Phase-1 proposal's own Sec 5):**
Both families' r=78 anchor sits at the same 1.44um absolute shell
thickness whose realizability tier is already CLOSED at
experiments/034-floor-convergence-scale-bridge/REALIZABILITY_MEMO.md
AMENDMENT 6/7 (Iteration 38/39): UNOBTANIUM-WITH-PARAMETERS, overdetermined
by the THICKNESS axis (real CNT-forest/Vantablack coatings run 100-500um,
a 70-350x gap) -- not the absorption-rate axis, which was also re-derived
there (alpha~=1/174nm, not the ~1/60nm bookkeeping artifact this program
once cited) and found comparably unhealthy. Fixed-abs holds this same
69-347x thickness gap at every r; self-similar's absolute thickness grows
with r (2.88um/5.76um at r=156/312) and is therefore marginally, not
substantially, closer to the real range at larger r -- the opposite of a
naive "fixed-abs is more realistic" reading. Neither family's realizability
tier changes this cycle.

Mandatory Idealizations: 2D TMz, single lambda=600nm/cpl=20 scope,
theta=0 deg only, no witness-scale extrapolation attempted, P5/thermal
sidecar not re-invoked (varying R_CORE/sigma_max at fixed r_out does not
change the thermal chain's own l_geometric_m argument). The delta_scene
R3-vs-R4 split (T28, now SIX consecutive deferrals) is explicitly
re-justified for a seventh deferral in NOTES.md's own Idealizations
section, citing the Iteration-51 no-seventh-cycle precedent -- Iteration
84 must execute it or formally retire it.
"""


def main():
    print("=" * 78)
    print("exp-106 -- floor-gating, settling, risk-propagation, and the")
    print("fixed-absolute-thickness control for kappa_window")
    print("=" * 78)

    t_start = time.time()
    n_fdtd_calls = 0

    g78, g156, g312 = geom(78), geom(156), geom(312)
    g78_fa, g156_fa, g312_fa = geom_fixedabs(78), geom_fixedabs(156), geom_fixedabs(312)

    # ---------------------------------------------------------- Gate P0
    with open(os.path.join(EXP105_DIR, "results.json")) as f:
        exp105 = json.load(f)
    shared_keys = ("N", "CX", "CY", "SRC_X", "STEPS", "R_CORE", "sigma_max", "behind", "dense_x")

    def _p0(g, ref):
        return all(g[k] == tuple(ref[k]) if isinstance(g[k], tuple) else g[k] == ref[k]
                   for k in shared_keys)

    p0_pass = (_p0(g78, exp105["geom_78"]) and _p0(g156, exp105["geom_156"])
               and _p0(g312, exp105["geom_312"]))
    print(f"\n[Gate P0] geom(78/156/312) reproduces exp-105's own committed geometry: PASS={p0_pass}")
    if not p0_pass:
        raise SystemExit("GATE P0 FAILED -- halting before any FDTD call.")

    predictions_text_ = build_predictions_text(g78, g156, g312, g156_fa, g312_fa)
    assert DISCLAIMER in predictions_text_, "R23: disclaimer missing from Predictions block"
    print(f"\n{predictions_text_}")

    # ============================================================ r=78: REUSE (0 new calls, both families -- object is identical)
    kappa_window_78 = exp105["kappa_windows"]["r78"]
    z78 = g78["z_over_zr"]
    print(f"\n[r=78, REUSED both families] kappa_window={kappa_window_78:.6e}")

    # ============================================================ r=156: 2 distinct empty captures + 2 self-similar + 2 fixed-abs article captures
    # (empty scene is family-independent -- Director's own cost optimization, disclosed)
    print("\n" + "=" * 78)
    print(f"r=156 -- empty (shared) + self-similar article + fixed-abs article, STEPS={g156['STEPS']}")
    print("=" * 78)
    t0 = time.time()
    cap_e156, _ = _run(False, g156["STEPS"], g156)
    n_fdtd_calls += 1
    cap_a156_ss, sig_a156_ss = _run(True, g156["STEPS"], g156, capture_sigma_e=True)
    n_fdtd_calls += 1
    cap_a156_fa, sig_a156_fa = _run(True, g156["STEPS"], g156_fa, capture_sigma_e=True)
    n_fdtd_calls += 1
    wall_156_primary = time.time() - t0
    print(f"r=156 primary triple (1 empty + 2 article) wall time: {wall_156_primary:.1f}s")

    ez_e156 = sc.phasors(cap_e156)["ez"]
    ez_a156_ss = sc.phasors(cap_a156_ss)["ez"]
    ez_a156_fa = sc.phasors(cap_a156_fa)["ez"]

    win_e156 = window_stats(ez_e156, *g156["behind"])
    win_a156_ss = window_stats(ez_a156_ss, *g156["behind"])
    win_a156_fa = window_stats(ez_a156_fa, *g156["behind"])
    kappa_window_156_ss = win_a156_ss["mean"] / win_e156["mean"]
    kappa_window_156_fa = win_a156_fa["mean"] / win_e156["mean"]

    repro_156 = abs(kappa_window_156_ss - exp105["kappa_windows"]["r156"]) / abs(exp105["kappa_windows"]["r156"])
    repro_156_pass = repro_156 < 1e-6
    print(f"[reproduction check, r=156] fresh kappa_window_selfsim={kappa_window_156_ss:.6e} "
          f"vs exp-105's committed {exp105['kappa_windows']['r156']:.6e}  "
          f"rel_dev={repro_156:.3e}  PASS={repro_156_pass}")
    if not repro_156_pass:
        raise SystemExit("REPRODUCTION CHECK (r=156) FAILED -- halting.")

    fg_win_e156 = floor_gate_window(ez_e156, *g156["behind"], "r=156 window (empty, shared)")

    # r=156 dense_x machinery (self-similar only -- already persisted at exp-105, reused here
    # only as a free byte-exact reproduction spot-check, not re-scored)
    wide156_repro = {x: kappa_region_wide(ez_e156, ez_a156_ss, x, g156["CY"])[0] for x in g156["dense_x"][:3]}

    # ------------------------------------------------------ item 2: settling leg on kappa_window, r=156, both families
    print("\n" + "=" * 78)
    print(f"r=156 SETTLING LEG on kappa_window (both families) -- STEPS={2*g156['STEPS']}")
    print("=" * 78)
    t0 = time.time()
    cap_e156_2x, _ = _run(False, 2 * g156["STEPS"], g156)
    n_fdtd_calls += 1
    cap_a156_ss_2x, sig_a156_ss_2x = _run(True, 2 * g156["STEPS"], g156, capture_sigma_e=True)
    n_fdtd_calls += 1
    cap_a156_fa_2x, sig_a156_fa_2x = _run(True, 2 * g156["STEPS"], g156_fa, capture_sigma_e=True)
    n_fdtd_calls += 1
    wall_156_settling = time.time() - t0
    print(f"r=156 settling triple wall time: {wall_156_settling:.1f}s")

    ez_e156_2x = sc.phasors(cap_e156_2x)["ez"]
    ez_a156_ss_2x = sc.phasors(cap_a156_ss_2x)["ez"]
    ez_a156_fa_2x = sc.phasors(cap_a156_fa_2x)["ez"]
    win_e156_2x = window_stats(ez_e156_2x, *g156["behind"])
    win_a156_ss_2x = window_stats(ez_a156_ss_2x, *g156["behind"])
    win_a156_fa_2x = window_stats(ez_a156_fa_2x, *g156["behind"])
    kappa_window_156_ss_2x = win_a156_ss_2x["mean"] / win_e156_2x["mean"]
    kappa_window_156_fa_2x = win_a156_fa_2x["mean"] / win_e156_2x["mean"]

    settle_156_ss_pass, settle_156_ss_rel = settling_pass_window(kappa_window_156_ss, kappa_window_156_ss_2x)
    settle_156_fa_pass, settle_156_fa_rel = settling_pass_window(kappa_window_156_fa, kappa_window_156_fa_2x)
    print(f"[settling, r=156, self-similar] rel_change={settle_156_ss_rel:.4f}  PASS={settle_156_ss_pass}")
    print(f"[settling, r=156, fixed-abs]    rel_change={settle_156_fa_rel:.4f}  PASS={settle_156_fa_pass}")

    nyq156 = nyquist_trust_tier(g156["nyquist_margin"])

    # ------------------------------------------------------ item 1 (ledger, mandatory fix 1): r=156, both families
    ledger_156_ss = ledger_check(cap_a156_ss, cap_e156, sig_a156_ss, g156)
    ledger_156_fa = ledger_check(cap_a156_fa, cap_e156, sig_a156_fa, g156_fa)
    print(f"[ledger, r=156, self-similar] sigma_abs/sigma_ext={ledger_156_ss['abs_ext_ratio']:.4f}  "
          f"core_frac={ledger_156_ss['core_frac']:.3e}  box_dev={ledger_156_ss['box_dev']:.4f}")
    print(f"[ledger, r=156, fixed-abs]    sigma_abs/sigma_ext={ledger_156_fa['abs_ext_ratio']:.4f}  "
          f"core_frac={ledger_156_fa['core_frac']:.3e}  box_dev={ledger_156_fa['box_dev']:.4f}")
    p_abs_frac_diff_156 = (abs(ledger_156_fa["sigma_abs"] - ledger_156_ss["sigma_abs"])
                            / abs(ledger_156_ss["sigma_abs"]))
    print(f"[ledger cross-family, r=156] |p_abs_fa - p_abs_ss|/p_abs_ss = {p_abs_frac_diff_156:.4f} "
          f"({'within ~10%' if p_abs_frac_diff_156 <= 0.10 else 'EXCEEDS ~10%'})")

    # ============================================================ r=312: cost-gated, per-leg pilot (empty scene shared)
    print("\n" + "=" * 78)
    print(f"r=312 COST-GATED PILOT -- empty scene (shared, primary STEPS={g312['STEPS']})")
    print("=" * 78)
    t0 = time.time()
    cap_e312, _ = _run(False, g312["STEPS"], g312)
    n_fdtd_calls += 1
    wall_312_empty_pilot = time.time() - t0
    projected_primary_min = (wall_312_empty_pilot + 2 * wall_312_empty_pilot) / 60.0  # empty + 2 articles, naive equal-cost estimate
    print(f"r=312 empty (primary) wall time: {wall_312_empty_pilot:.1f}s "
          f"({wall_312_empty_pilot/60.0:.2f} min). Projected 3-call primary total: "
          f"{projected_primary_min:.2f} min.")
    r312_primary_committed = (wall_312_empty_pilot / 60.0) < 90.0 and projected_primary_min < 180.0
    print(f"[r=312 primary cost gate] committed={r312_primary_committed} "
          f"(rule: pilot<90min AND projected-3call-total<180min)")

    kappa_window_312_ss = kappa_window_312_fa = None
    p3_trusted = shape_ratio_fixedabs_trusted = False
    ledger_312_ss = ledger_312_fa = None
    fg_win_e312 = None
    settle_312_ss_pass = settle_312_fa_pass = False
    settle_312_ss_rel = settle_312_fa_rel = None
    wall_312_article = wall_312_settling = None
    r312_settling_committed = False

    if r312_primary_committed:
        t0 = time.time()
        cap_a312_ss, sig_a312_ss = _run(True, g312["STEPS"], g312, capture_sigma_e=True)
        n_fdtd_calls += 1
        cap_a312_fa, sig_a312_fa = _run(True, g312["STEPS"], g312_fa, capture_sigma_e=True)
        n_fdtd_calls += 1
        wall_312_article = time.time() - t0
        print(f"r=312 primary article pair (self-similar + fixed-abs) wall time: {wall_312_article:.1f}s")

        ez_e312 = sc.phasors(cap_e312)["ez"]
        ez_a312_ss = sc.phasors(cap_a312_ss)["ez"]
        ez_a312_fa = sc.phasors(cap_a312_fa)["ez"]
        win_e312 = window_stats(ez_e312, *g312["behind"])
        win_a312_ss = window_stats(ez_a312_ss, *g312["behind"])
        win_a312_fa = window_stats(ez_a312_fa, *g312["behind"])
        kappa_window_312_ss = win_a312_ss["mean"] / win_e312["mean"]
        kappa_window_312_fa = win_a312_fa["mean"] / win_e312["mean"]

        repro_312 = abs(kappa_window_312_ss - exp105["kappa_windows"]["r312"]) / abs(exp105["kappa_windows"]["r312"])
        repro_312_pass = repro_312 < 1e-6
        print(f"[reproduction check, r=312] fresh kappa_window_selfsim={kappa_window_312_ss:.6e} "
              f"vs exp-105's committed {exp105['kappa_windows']['r312']:.6e}  "
              f"rel_dev={repro_312:.3e}  PASS={repro_312_pass}")
        if not repro_312_pass:
            raise SystemExit("REPRODUCTION CHECK (r=312) FAILED -- halting.")

        fg_win_e312 = floor_gate_window(ez_e312, *g312["behind"], "r=312 window (empty, shared)")

        # item 1: persist r=312's own wide/point/delta_phi (self-similar, dense_x) -- the
        # specific "stop discarding" gap this cycle closes
        wide312 = {}
        point312 = {}
        dphi_w312 = {}
        dphi_p312 = {}
        i_e_wide312 = {}
        for x in g312["dense_x"]:
            k_w, i_e_w, i_a_w = kappa_region_wide(ez_e312, ez_a312_ss, x, g312["CY"])
            k_p, _, _ = kappa_region_point(ez_e312, ez_a312_ss, x, g312["CY"])
            wide312[x], i_e_wide312[x], point312[x] = k_w, i_e_w, k_p
            dphi_w312[x] = delta_phi_wide(ez_e312, ez_a312_ss, x, g312["CY"])
            dphi_p312[x] = delta_phi_point(ez_e312, ez_a312_ss, x, g312["CY"])
        fg_wide312 = floor_gate([i_e_wide312[x] for x in g312["dense_x"]], "r=312 wide channel (dense_x, empty)")

        ledger_312_ss = ledger_check(cap_a312_ss, cap_e312, sig_a312_ss, g312)
        ledger_312_fa = ledger_check(cap_a312_fa, cap_e312, sig_a312_fa, g312_fa)
        print(f"[ledger, r=312, self-similar] sigma_abs/sigma_ext={ledger_312_ss['abs_ext_ratio']:.4f}  "
              f"core_frac={ledger_312_ss['core_frac']:.3e}  box_dev={ledger_312_ss['box_dev']:.4f}")
        print(f"[ledger, r=312, fixed-abs]    sigma_abs/sigma_ext={ledger_312_fa['abs_ext_ratio']:.4f}  "
              f"core_frac={ledger_312_fa['core_frac']:.3e}  box_dev={ledger_312_fa['box_dev']:.4f}")
        p_abs_frac_diff_312 = (abs(ledger_312_fa["sigma_abs"] - ledger_312_ss["sigma_abs"])
                                / abs(ledger_312_ss["sigma_abs"]))
        print(f"[ledger cross-family, r=312] |p_abs_fa - p_abs_ss|/p_abs_ss = {p_abs_frac_diff_312:.4f} "
              f"({'within ~10%' if p_abs_frac_diff_312 <= 0.10 else 'EXCEEDS ~10%'})")

        # ------------------------------------------------------ item 2: settling leg on kappa_window, r=312, both families -- per-leg cost gate
        print("\n" + "=" * 78)
        print(f"r=312 SETTLING LEG cost gate -- empty pilot, STEPS={2*g312['STEPS']}")
        print("=" * 78)
        t0 = time.time()
        cap_e312_2x, _ = _run(False, 2 * g312["STEPS"], g312)
        n_fdtd_calls += 1
        wall_312_empty_settling_pilot = time.time() - t0
        projected_settling_min = (wall_312_empty_settling_pilot + 2 * wall_312_empty_settling_pilot) / 60.0
        print(f"r=312 settling-leg empty wall time: {wall_312_empty_settling_pilot:.1f}s "
              f"({wall_312_empty_settling_pilot/60.0:.2f} min). Projected 3-call total: "
              f"{projected_settling_min:.2f} min.")
        r312_settling_committed = ((wall_312_empty_settling_pilot / 60.0) < 90.0
                                    and projected_settling_min < 180.0)
        print(f"[r=312 settling cost gate] committed={r312_settling_committed} "
              f"(rule: pilot<90min AND projected-3call-total<180min)")

        if r312_settling_committed:
            t0 = time.time()
            cap_a312_ss_2x, _ = _run(True, 2 * g312["STEPS"], g312)
            n_fdtd_calls += 1
            cap_a312_fa_2x, _ = _run(True, 2 * g312["STEPS"], g312_fa)
            n_fdtd_calls += 1
            wall_312_settling = time.time() - t0
            print(f"r=312 settling article pair wall time: {wall_312_settling:.1f}s")

            ez_e312_2x = sc.phasors(cap_e312_2x)["ez"]
            ez_a312_ss_2x = sc.phasors(cap_a312_ss_2x)["ez"]
            ez_a312_fa_2x = sc.phasors(cap_a312_fa_2x)["ez"]
            win_e312_2x = window_stats(ez_e312_2x, *g312["behind"])
            win_a312_ss_2x = window_stats(ez_a312_ss_2x, *g312["behind"])
            win_a312_fa_2x = window_stats(ez_a312_fa_2x, *g312["behind"])
            kappa_window_312_ss_2x = win_a312_ss_2x["mean"] / win_e312_2x["mean"]
            kappa_window_312_fa_2x = win_a312_fa_2x["mean"] / win_e312_2x["mean"]

            settle_312_ss_pass, settle_312_ss_rel = settling_pass_window(kappa_window_312_ss, kappa_window_312_ss_2x)
            settle_312_fa_pass, settle_312_fa_rel = settling_pass_window(kappa_window_312_fa, kappa_window_312_fa_2x)
            print(f"[settling, r=312, self-similar] rel_change={settle_312_ss_rel:.4f}  PASS={settle_312_ss_pass}")
            print(f"[settling, r=312, fixed-abs]    rel_change={settle_312_fa_rel:.4f}  PASS={settle_312_fa_pass}")
        else:
            print("[r=312 settling leg] COST-DEFERRED beyond the empty pilot -- queued for a future cycle.")
    else:
        print("[r=312 primary leg] COST-DEFERRED, not attempted beyond the empty-scene pilot.")

    nyq312 = nyquist_trust_tier(g312["nyquist_margin"])
    p3_trusted = bool(settle_312_ss_pass and (nyq312 == "TRUSTED"))
    shape_ratio_fixedabs_trusted = bool(settle_312_fa_pass and (nyq312 == "TRUSTED"))
    print(f"\n[item 3] p3_trusted (self-similar) = {p3_trusted}  "
          f"(nyquist_tier(312)={nyq312}, structurally forced False whenever not TRUSTED)")
    print(f"[item 3] shape_ratio_fixedabs_trusted = {shape_ratio_fixedabs_trusted}")

    total_wall = time.time() - t_start

    # ============================================================ P2 (monotonicity), self-similar (unchanged formula, fresh data)
    if kappa_window_312_ss is not None:
        p2_monotonic = kappa_window_78 > kappa_window_156_ss > kappa_window_312_ss
        p2_verdict = "CONFIRMED" if p2_monotonic else "FALSIFIED"
    else:
        p2_monotonic = kappa_window_78 > kappa_window_156_ss
        p2_verdict = "CONFIRMED-PARTIAL(78->156 only)" if p2_monotonic else "FALSIFIED-PARTIAL(78->156 only)"

    # ============================================================ P3 (self-similar) and item 4 (fixed-abs), shape_ratio
    p3 = {}
    p4_fa = {}
    abs_ratio = {}
    if kappa_window_312_ss is not None:
        z156v, z312v = g156["z_over_zr"], g312["z_over_zr"]
        p3 = shape_ratio_fit(kappa_window_78, kappa_window_156_ss, kappa_window_312_ss, z78, z156v, z312v)
        p3["noise_flag"] = noise_floor_flag(kappa_window_156_ss, kappa_window_312_ss)
        p3["trusted"] = p3_trusted
        print(f"\n[P3, self-similar] shape_ratio={p3['shape_ratio']:.4f}  trusted={p3_trusted}  "
              f"noise_dominated={p3['noise_flag']['noise_dominated']}")

        p4_fa = shape_ratio_fit(kappa_window_78, kappa_window_156_fa, kappa_window_312_fa, z78, z156v, z312v)
        p4_fa["noise_flag"] = noise_floor_flag(kappa_window_156_fa, kappa_window_312_fa)
        p4_fa["trusted"] = shape_ratio_fixedabs_trusted
        sr_fa = p4_fa["shape_ratio"]
        if sr_fa <= SHAPE_RATIO_FIXEDABS_CONFIRM:
            classification = "CONFIRMS-electrical-thickness-growth-hypothesis"
        elif sr_fa >= SHAPE_RATIO_FIXEDABS_REFUTE:
            classification = "REFUTES-electrical-thickness-growth-hypothesis"
        else:
            classification = "AMBIGUOUS"
        if p4_fa["noise_flag"]["noise_dominated"]:
            classification = f"NOISE-DOMINATED-UNRELIABLE ({classification} nominally)"
        if not shape_ratio_fixedabs_trusted:
            classification = f"{classification} (NOT-TRUSTED -- r=312 MARGINAL/unsettled)"
        p4_fa["classification"] = classification
        print(f"[item 4, fixed-abs] shape_ratio={sr_fa:.4f}  classification={classification}")

        abs_ratio["r156"] = kappa_window_156_fa / kappa_window_156_ss
        abs_ratio["r312"] = kappa_window_312_fa / kappa_window_312_ss
        for rk, rv in abs_ratio.items():
            band_pass = (1.0 / ABS_RATIO_BAND) <= rv <= ABS_RATIO_BAND
            print(f"[item 4, abs_ratio {rk}] kappa_fixedabs/kappa_selfsim = {rv:.4f}  "
                  f"within factor-of-{ABS_RATIO_BAND:.0f} of 1.0 = {band_pass}")
    else:
        print("\n[P3/item4] NOT SCORED -- r=312 primary leg cost-deferred this shift.")

    # ============================================================ RESULT_TEXT (R23 pattern)
    result_text = f"""RESULT (exp-106, Panel Iteration 83)

{DISCLAIMER}

{n_fdtd_calls} real FDTD calls, {total_wall:.1f}s ({total_wall/60.0:.2f} min)
total wall time, zero `lab/` diff throughout. (Director's own cost
optimization: empty-scene captures reused across families -- 12 real
calls scheduled vs. the Phase-1 proposal's own naive 16-call budget,
if every leg commits.)

**Gate P0: {'PASS' if p0_pass else 'FAIL'}.**
**Reproduction checks (r=156/312, self-similar):** r=156 rel_dev=
{repro_156:.3e} PASS={repro_156_pass}. r=312 {'rel_dev=' + format(repro_312, '.3e') + ' PASS=' + str(repro_312_pass) if kappa_window_312_ss is not None else 'not run (r=312 cost-deferred).'}

**Item 1 (floor-gate window_stats(), r=156/312):** r=156 (shared both
families) frac_unresolved={fg_win_e156['frac_unresolved']:.4f}. r=312
{'(shared) frac_unresolved=' + format(fg_win_e312['frac_unresolved'], '.4f') if fg_win_e312 else 'not run (cost-deferred).'}
r=312 self-similar wide_channel/point_channel/delta_phi persisted in full
this cycle (the "stop discarding" gap closed) -- see results.json r312_selfsim.

**Item 2 (settling leg on kappa_window):** r=156 self-similar
rel_change={settle_156_ss_rel:.4f} PASS={settle_156_ss_pass}; fixed-abs
rel_change={settle_156_fa_rel:.4f} PASS={settle_156_fa_pass}.
r=312 {'self-similar rel_change=' + format(settle_312_ss_rel, '.4f') + ' PASS=' + str(settle_312_ss_pass) + '; fixed-abs rel_change=' + format(settle_312_fa_rel, '.4f') + ' PASS=' + str(settle_312_fa_pass) if settle_312_ss_rel is not None else 'not run (cost-deferred).'}

**Item 3 (risk-propagation gates):** p3_trusted={p3_trusted};
shape_ratio_fixedabs_trusted={shape_ratio_fixedabs_trusted}. Both
structurally forced False whenever nyquist_tier(312) != TRUSTED
(nyquist_tier(312)={nyq312}), per this cycle's own pre-registered,
disclosed prediction.

**Item 4 (fixed-abs control):** {"shape_ratio_fixedabs=" + format(p4_fa.get('shape_ratio', 0), '.4f') + ', classification=' + p4_fa.get('classification', 'N/A') + ', abs_ratio(156)=' + format(abs_ratio.get('r156', 0), '.4f') + ', abs_ratio(312)=' + format(abs_ratio.get('r312', 0), '.4f') if p4_fa else 'NOT SCORED -- r=312 cost-deferred.'}
Self-similar P3 (recomputed fresh this cycle): {"shape_ratio=" + format(p3.get('shape_ratio', 0), '.4f') + ' (exp-105 committed 19.79 for reference)' if p3 else 'NOT SCORED -- r=312 cost-deferred.'}

**Ledger sanity check (mandatory fix 1):** r=156 |p_abs_fa-p_abs_ss|/p_abs_ss=
{p_abs_frac_diff_156:.4f}. r=312 {'|p_abs_fa-p_abs_ss|/p_abs_ss=' + format(p_abs_frac_diff_312, '.4f') if ledger_312_ss else 'not run (cost-deferred).'}
core_frac (fraction of absorbed power landing inside the PEC core, should
be ~0): self-similar r=156={ledger_156_ss['core_frac']:.3e}, fixed-abs
r=156={ledger_156_fa['core_frac']:.3e}{', self-similar r=312=' + format(ledger_312_ss['core_frac'], '.3e') + ', fixed-abs r=312=' + format(ledger_312_fa['core_frac'], '.3e') if ledger_312_ss else ''}.
box_dev (two-box independence, established <=0.12 convention): self-similar
r=156={ledger_156_ss['box_dev']:.4f}, fixed-abs r=156={ledger_156_fa['box_dev']:.4f}
{', self-similar r=312=' + format(ledger_312_ss['box_dev'], '.4f') + ', fixed-abs r=312=' + format(ledger_312_fa['box_dev'], '.4f') if ledger_312_ss else ''}.

**Realizability note (mandatory fix 4, verbatim):** Both families' r=78
anchor sits at the same 1.44um absolute shell thickness whose
realizability tier is already CLOSED at REALIZABILITY_MEMO.md AMENDMENT
6/7 (Iteration 38/39): UNOBTANIUM-WITH-PARAMETERS, overdetermined by the
THICKNESS axis (100-500um real vs 1.44um here, 70-350x gap), not the rate
axis (alpha~=1/174nm, also unhealthy). Fixed-abs holds this same gap at
every r; self-similar's absolute thickness grows with r and is marginally
(not substantially) closer to the real range at larger r -- the opposite
of a naive "fixed-abs is more realistic" reading. Neither tier changes
this cycle.
"""
    assert DISCLAIMER in result_text, "R23: disclaimer missing from Result block"
    print("\n" + result_text)

    result = dict(
        experiment="exp-106", panel_iteration=83,
        n_fdtd_calls=n_fdtd_calls, total_wall_s=total_wall,
        wall_156_primary_s=wall_156_primary, wall_156_settling_s=wall_156_settling,
        wall_312_empty_pilot_s=wall_312_empty_pilot, wall_312_article_s=wall_312_article,
        wall_312_settling_s=wall_312_settling,
        r312_primary_committed=r312_primary_committed, r312_settling_committed=r312_settling_committed,
        geom_78=g78, geom_156=g156, geom_312=g312,
        geom_78_fixedabs=g78_fa, geom_156_fixedabs=g156_fa, geom_312_fixedabs=g312_fa,
        gate_p0=dict(pass_=p0_pass),
        reproduction_r156=dict(rel_dev=repro_156, pass_=repro_156_pass),
        reproduction_r312=(dict(rel_dev=repro_312, pass_=repro_312_pass) if kappa_window_312_ss is not None else None),
        kappa_windows_selfsim=dict(r78=kappa_window_78, r156=kappa_window_156_ss, r312=kappa_window_312_ss),
        kappa_windows_fixedabs=dict(r78=kappa_window_78, r156=kappa_window_156_fa, r312=kappa_window_312_fa),
        floor_gate_window_r156=fg_win_e156,
        floor_gate_window_r312=fg_win_e312,
        settling_r156=dict(selfsim=dict(pass_=settle_156_ss_pass, rel_change=settle_156_ss_rel),
                            fixedabs=dict(pass_=settle_156_fa_pass, rel_change=settle_156_fa_rel)),
        settling_r312=dict(selfsim=dict(pass_=settle_312_ss_pass, rel_change=settle_312_ss_rel),
                            fixedabs=dict(pass_=settle_312_fa_pass, rel_change=settle_312_fa_rel)),
        p3_trusted=p3_trusted, shape_ratio_fixedabs_trusted=shape_ratio_fixedabs_trusted,
        p2_verdict=p2_verdict,
        p3_selfsim=p3, item4_fixedabs=p4_fa, abs_ratio=abs_ratio,
        ledger_r156=dict(selfsim=ledger_156_ss, fixedabs=ledger_156_fa, p_abs_frac_diff=p_abs_frac_diff_156),
        ledger_r312=(dict(selfsim=ledger_312_ss, fixedabs=ledger_312_fa, p_abs_frac_diff=p_abs_frac_diff_312)
                      if ledger_312_ss is not None else None),
        r312_selfsim=(dict(wide_channel=wide312, point_channel=point312,
                            delta_phi_wide=dphi_w312, delta_phi_point=dphi_p312,
                            floor_gate_wide=fg_wide312)
                      if kappa_window_312_ss is not None else None),
        wide156_reproduction_spotcheck=wide156_repro,
        predictions_text=predictions_text_,
        result_text=result_text,
    )
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(result, f, indent=2, default=str)
    print("\nresults.json written.")
    return result


if __name__ == "__main__":
    if "--predictions-only" in sys.argv:
        g78, g156, g312 = geom(78), geom(156), geom(312)
        g156_fa, g312_fa = geom_fixedabs(156), geom_fixedabs(312)
        print(build_predictions_text(g78, g156, g312, g156_fa, g312_fa))
    else:
        main()
