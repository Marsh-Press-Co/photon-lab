"""exp-102 -- The Coherent, Phase-Resolved Downstream Point-Intensity
Instrument. Panel Iteration 79. Lead seat (rotation): PHOTONICS. Frozen
spec: NOTES.md (Predictions committed to git strictly BEFORE this file's
first run, house discipline). Change rationale: phase2_redteam_audit.md
(9 numbered attacks, 7 mandatory fixes, all adopted, 0 overridden).

Instrument build, diagnostic only -- T1: N/A, zero `lab/` diff, no
mechanism proposed or varied. Thermal sidecar NOT invoked this cycle
(mandatory fix 1) -- this file does not import `netd_row`/`cell_metrics_r4`/
`pair_metrics_full`/`thermo_sidecar` from exp-101 or any other prior
experiment. It reuses only the pure geometry/config constants
(`R4_CONFIGS`, `PEC_R_R4`, `R4_R_OUT`, `SIGMA_R4_CORRECTED`, `R4_TAPER`,
`R4_STEPS`, `R4_CPL`, `COURANT_FRAC`) from
`experiments/069-.../design_geometry.py` (the actual source of those
constants -- see that file's own R4 block) and re-implements the short,
pure `box_for_r4`/`ref_for_r4`/article-construction helpers locally
(mirroring `experiments/094-.../run.py`'s own functions line-for-line,
which are themselves pure geometry/`lab.materials` calls, nothing thermal)
rather than loading the exp-094/exp-101 module chain, keeping this file
fully self-contained per NOTES.md's "lab/ diff: zero" / thermal-disposition
commitments.

DISCLOSED RESOLUTION NOTE 1 (Gate B's beam-aligned frame sign): NOTES.md's
`u(theta)=(-cos theta, sin theta)` is `add_line_source`'s own documented
launch convention (lab/fdtd2d.py docstring: "the -x-going wave... travels
along (-cos theta, sin theta)"), which is the physically downstream
direction ONLY for a scene where the source sits at LARGER x than the
object (true for every `R4_CONFIGS` config: src_x > obj_x, confirmed
below) -- the primary 24-call channel therefore uses this formula exactly
as given, unmodified. Gate B's own native-scale flagship geometry
(exp-001/002's "absorber" scene) has the OPPOSITE arrangement (SRC_X=64 <
CX=252 -- the source sits at SMALLER x than the object; exp-001's own
established downstream "BEHIND" window sits at x in [CX+R_CLK+15,
CX+R_CLK+115], i.e. +x of the object, confirmed by direct inspection of
`experiments/001-flashlight-statement/run.py`). Applying the literal
formula unmodified to Gate B's geometry would place P(0) at x=52 --
upstream of the source itself (SRC_X=64), nowhere near the object's
shadow, and would not exercise this instrument's own construction at all.
This file therefore derives the frame's sign generically and mechanically
from each config's own recorded `src_x`/`obj_x` (`downstream_sign()`
below: +1 iff src_x > obj_x, exactly NOTES.md's literal formula whenever
that holds), rather than hand-picking Gate B's sign -- verified to
reduce to sign=+1 (no change at all) for both `R4_CONFIGS` entries, and
sign=-1 (a mirror flip) only for Gate B's own distinct, disclosed
geometry. This is a geometry-fact-driven generalization of the same
one construction, not a second construction or a redesign of the
frozen formula.

DISCLOSED RESOLUTION NOTE 2 (Gate C's sign, found by an actual failed
first run, not assumed in advance): `sections.widths()`'s own established
`i_inc` is a RAW signed Poynting-x-component (`-0.5*Re{Ez*conj(Hy)}`,
positive meaning flow toward +x). For the R4 family the beam's real
propagation direction is -x (src_x>obj_x; u_x(theta)=-cos(theta)), so
`i_inc` genuinely comes out NEGATIVE there (confirmed empirically: e.g.
at 41.460901deg, i_inc=-0.343 while the unsigned magnitude
I0_corrected=0.453) -- this is not a bug in `i_inc`/`widths()` (unmodified,
already-gated code), it is what a correctly-oriented incident wave
produces. `I0_corrected=sqrt(mean_sx^2+mean_sy^2)` is by construction an
UNSIGNED magnitude (Setup's own words: "direction-agnostic
Poynting-magnitude reference"), so re-projecting it onto the signed `i_inc`
axis requires the SAME signed x-component this instrument already uses
for `P(theta)`/`P_off(theta)`, i.e. `u_x(theta)` (=-cos(theta) for the R4
family's sign=+1), not a bare, sign-blind `cos(theta)`. Using bare
`cos(theta)` (tried first; see the crash-and-fix history in the Phase-4
report) gives a spurious ~145-160% "deviation" at every single
(angle,config) cell -- a uniform, systematic sign flip, not per-cell
noise -- while `I0_corrected*u_x(theta)` against the SAME `i_inc` lands
under 1% at every cell tested. This is the same category of fix as
Resolution Note 1 (a sign made explicit and geometry-derived, not a
redesign of Gate C's own comparison or its 1% bar): NOTES.md's own u(theta)
IS this instrument's local-plane-wave direction convention, and Gate C's
whole purpose is checking that convention's own x-projection against the
raw measured flux it is supposed to describe.
"""

import importlib.util
import json
import math
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)

from lab import Sim, materials                      # noqa: E402
from lab import sections as sc                       # noqa: E402


def _load(path, name):
    """House `_load()` pattern (exp-078..101's own idiom for cross-
    experiment-directory imports)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# design_geometry.py is the ACTUAL source of R4_CONFIGS/PEC_R_R4/R4_R_OUT/
# SIGMA_R4_CORRECTED/R4_TAPER/R4_STEPS/R4_CPL/COURANT_FRAC (confirmed by
# direct read) -- loaded directly, not via exp-094/exp-101's own run.py
# chain (which would additionally define cell_metrics_r4/netd_row/
# pair_metrics_full -- forbidden imports per NOTES.md Setup, even though
# unused, the cleanest way to guarantee they are never reachable from this
# file is to never load that chain at all).
DG_PATH = os.path.join(ROOT, "experiments", "069-t21-block-mini-period-match-power-up",
                        "design_geometry.py")
dg = _load(DG_PATH, "_exp102_design_geometry")

R4_CONFIGS = dg.R4_CONFIGS
PEC_R_R4 = dg.PEC_R_R4
R4_R_OUT = dg.R4_R_OUT
SIGMA_R4_CORRECTED = dg.SIGMA_R4_CORRECTED
R4_TAPER = dg.R4_TAPER
R4_STEPS = dg.R4_STEPS
R4_CPL = dg.R4_CPL
COURANT_FRAC = dg.COURANT_FRAC
BOX_CLEARANCE_A_R4 = dg.BOX_CLEARANCE_A_R4
REF_HALF_H_R4 = dg.REF_HALF_H_R4

PAIR_KEYS_R4 = ("C40_R4", "G40_R4")
assert set(R4_CONFIGS.keys()) == set(PAIR_KEYS_R4)
assert abs(SIGMA_R4_CORRECTED - 0.25) < 1e-12
assert R4_R_OUT == 156
assert PEC_R_R4 == 60

# The 6 established, pool-wide-largest-magnitude R4-family angles
# (exp-101's own committed LEG_B_ANGLES, restated literally here per
# NOTES.md Setup -- these were already independently re-derived and
# sorted in exp-101/run.py; re-deriving them again here would be the
# LEG_B_ANGLES computation copy-pasted, not an independent check, so the
# literal committed list is used directly).
ANGLES = [37.127246, 38.590230, 39.200000, 40.265420, 41.460901, 42.960901]
assert len(ANGLES) == 6 and len(set(ANGLES)) == 6

D_STANDOFF = 200
H_REGION = 10
DELTA_LAT = 450
FLOOR_FRAC = 0.10
THETA_GATE_D = 39.200000
assert THETA_GATE_D in ANGLES


# ================================================================ R4-family article/run construction
# Mirrors experiments/094-.../run.py's own box_for_r4/ref_for_r4/
# build_article_r4_sigma/_run_sim_r4_sigma exactly (pure geometry +
# lab.materials calls, nothing thermal) -- reimplemented locally per this
# file's own module docstring disclosure.
def box_for_r4(cfg, clearance):
    ox, oy = cfg["obj_x"], cfg["obj_y"]
    r = R4_R_OUT + clearance
    return (ox - r, ox + r, oy - r, oy + r)


def ref_for_r4(cfg):
    return (cfg["obj_x"], cfg["obj_y"], REF_HALF_H_R4)


def build_article_r4(sim, cx, cy, sigma_max):
    materials.pec_disk(sim, cx, cy, PEC_R_R4)
    materials.graded_black_shell(sim, cx, cy, PEC_R_R4, R4_R_OUT, sigma_max=sigma_max)


def _run_sim_r4(cfg, theta, steps, with_article, sigma_max):
    sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=R4_CPL[600],
              courant_frac=COURANT_FRAC, absorb=cfg["absorb"])
    if with_article:
        build_article_r4(sim, cfg["obj_x"], cfg["obj_y"], sigma_max)
        # due-diligence runtime check (mirrors exp-094's own Gate 5 in
        # spirit): the actual sigma_e landing in the shell must match what
        # was requested -- not a Python-constant tautology.
        rr, _ = materials._grids(sim, cfg["obj_x"], cfg["obj_y"])["ez"]
        shell_mask = (rr >= PEC_R_R4) & (rr <= R4_R_OUT)
        actual = float(sim.sigma_e[shell_mask].max())
        assert np.isclose(actual, sigma_max, atol=1e-9), (
            f"runtime sigma_e/sigma_max mismatch: {actual!r} vs {sigma_max!r}")
    # Both legs (with_article=False/True) launch with BIT-IDENTICAL
    # add_line_source params (same angle_deg, ramp_periods=default 3.0,
    # rel_phase=default 0.0) -- the coherent-comparison precondition.
    sim.add_line_source(cfg["src_x"], y_lo=cfg["y_lo"], y_hi=cfg["y_hi"],
                         angle_deg=theta, amplitude=1.0,
                         profile="plane", edge=R4_TAPER)
    sim.run(steps)
    return sc.full_capture(sim)


def _worker_r4(args):
    key, theta, with_article, steps, sigma_max = args
    cfg = R4_CONFIGS[key]
    cap = _run_sim_r4(cfg, theta, steps, with_article, sigma_max)
    return (key, theta, with_article, steps, cap)


def run_block_r4(jobs):
    t0 = time.time()
    captures = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for n, (key, th, art, steps, cap) in enumerate(ex.map(_worker_r4, jobs), 1):
            captures[(key, th, art)] = cap
            print(f"  [{n:2d}/{len(jobs)}] {key:8s} theta={th:+06.3f} "
                  f"article={art} steps={steps}", flush=True)
    wall = time.time() - t0
    return captures, wall


# ================================================================ R4-family cache
# The 24-call R4-family sweep is expensive (~53min wall) and its inputs
# (ANGLES/PAIR_KEYS_R4/R4_STEPS/SIGMA_R4_CORRECTED/geometry) are frozen by
# NOTES.md -- so its results are cached to disk (pickle, this experiment's
# own directory, zero lab/ diff) and reused whenever the cache is newer
# than this file. This only ever short-circuits the R4-family block; Gate
# B's own 2 calls always run fresh (cheap, and exercise the fix being
# tested this Phase-4 pass).
R4_CACHE_PATH = os.path.join(HERE, "r4_family_cache.pkl")
R4_CACHE_VERSION = 1  # bump if jobs/capture schema changes


def _load_r4_cache(jobs):
    if not os.path.exists(R4_CACHE_PATH):
        return None
    this_file = os.path.abspath(__file__)
    if os.path.getmtime(R4_CACHE_PATH) <= os.path.getmtime(this_file):
        print(f"[cache] {R4_CACHE_PATH} exists but is NOT newer than run.py -- ignoring "
              f"(stale, will recompute).")
        return None
    import pickle
    with open(R4_CACHE_PATH, "rb") as f:
        blob = pickle.load(f)
    if blob.get("version") != R4_CACHE_VERSION or blob.get("job_keys") != sorted(
            (k, t, a) for (k, t, a, _s, _sig) in jobs):
        print(f"[cache] {R4_CACHE_PATH} schema/job-set mismatch -- ignoring (will recompute).")
        return None
    return blob


def _save_r4_cache(captures, wall_r4, jobs):
    import pickle
    blob = dict(version=R4_CACHE_VERSION,
                job_keys=sorted((k, t, a) for (k, t, a, _s, _sig) in jobs),
                captures=captures, wall_r4=wall_r4)
    tmp = R4_CACHE_PATH + ".tmp"
    with open(tmp, "wb") as f:
        pickle.dump(blob, f, protocol=4)
    os.replace(tmp, R4_CACHE_PATH)
    print(f"[cache] R4-family sweep ({len(captures)} captures) saved to {R4_CACHE_PATH}")


def get_r4_captures(jobs):
    """Load the 24-call R4-family sweep from cache if a valid, fresh cache
    exists; otherwise run it for real and cache the result. Returns
    (captures, wall_r4, from_cache)."""
    cached = _load_r4_cache(jobs)
    if cached is not None:
        print(f"[cache] LOADED R4-family sweep ({len(cached['captures'])} captures) from "
              f"{R4_CACHE_PATH} -- skipping all 24 FDTD calls.")
        return cached["captures"], cached["wall_r4"], True
    captures, wall_r4 = run_block_r4(jobs)
    _save_r4_cache(captures, wall_r4, jobs)
    return captures, wall_r4, False


# ================================================================ Gate B native-scale flagship (exp-001/002's own "absorber" scene)
# Verbatim geometry/constants read directly from experiments/001-.../run.py
# and experiments/002-.../run.py -- both build "absorber" as
# pec_disk(r=R_CORE=30) + graded_black_shell(r_in=30, r_out=R_COAT=78,
# sigma_max=default 0.5), N=560, ABSORB=40, courant_frac=0.32, cpl=20
# (600nm), STEPS=3200, SRC_X=64, CX=252, CY=280.
GATEB_N = 560
GATEB_ABSORB = 40
GATEB_FRAC = 0.32
GATEB_CPL = 20
GATEB_STEPS = 3200
GATEB_SRC_X = 64
GATEB_CX, GATEB_CY = 252, 280
GATEB_R_CORE, GATEB_R_COAT = 30, 78
GATEB_Y_LO, GATEB_Y_HI = GATEB_ABSORB, GATEB_N - GATEB_ABSORB

# ---- Gate B's OWN D_STANDOFF/H_REGION (Phase-4 diagnostic fix) ----
# NOTES.md's D_STANDOFF=200/H_REGION=10 were derived (Phase-1) as multiples
# of the R4-family object's OWN scale (D_STANDOFF=200cells = 1.28*R4_R_OUT
# =156cells). This Gate's native-scale flagship uses a DIFFERENT
# cells_per_lambda than the R4 family -- confirmed by direct read of both
# grids' own constants: exp-001/002's 600nm leg uses GATEB_CPL=20 (their
# own SWEEP=[(15,450),(20,600),(25,750)]), while the R4 family always uses
# R4_CPL[600]=40 (design_geometry.py). Both articles share the SAME
# physical outer radius (78*30nm = 156*15nm = 2340nm, NOTES.md Setup), so
# reusing D_STANDOFF/H_REGION UNCHANGED IN CELL COUNT at this coarser grid
# does NOT hold the same physical-standoff-to-object-size ratio the
# R4-family value was designed around: 200 cells / GATEB_R_COAT(78 cells)
# = 2.564x r_out, not the 1.28x r_out that 200/R4_R_OUT(156) actually
# encodes for the R4 family. Fix: rescale D_STANDOFF/H_REGION by the
# article's own r_out ratio (a geometry fact, not a hand-picked constant)
# so both grids hold IDENTICAL standoff/r_out and region/r_out ratios by
# construction. RESULT (Phase-4 diagnostic, see Phase-4 report): even
# after this principled rescaling, Gate B still fails -- now BELOW the
# band (kappa_region~0.16%, band floor 0.5%) rather than above it. This is
# a genuine, honest finding, not a further bug: the rescaled standoff
# (~1.28x r_out, i.e. 100 native cells from center) sits just BEFORE
# exp-001's own established BEHIND window even starts (window: 105-205
# cells from center, x in [357,457)) -- comparing a near-object point
# (where the shadow is measurably darker) to a farther window average (of
# a shadow that fills in with distance) is not an apples-to-apples
# reproduction. Recorded as a genuine Gate B FAILURE below -- NOT forced
# to pass by further parameter search (that would be exactly the kind of
# named-constant search LOGBOOK's R5 already rules out).
_GATEB_R_OUT_RATIO = GATEB_R_COAT / R4_R_OUT          # 78/156 = 0.5 exactly
_gateb_d_standoff_f = D_STANDOFF * _GATEB_R_OUT_RATIO  # 200*0.5 = 100
_gateb_h_region_f = H_REGION * _GATEB_R_OUT_RATIO      # 10*0.5 = 5
assert _gateb_d_standoff_f == round(_gateb_d_standoff_f), (
    "GATEB_D_STANDOFF rescaling did not land on an integer cell count")
assert _gateb_h_region_f == round(_gateb_h_region_f), (
    "GATEB_H_REGION rescaling did not land on an integer cell count")
GATEB_D_STANDOFF = int(round(_gateb_d_standoff_f))     # 100
GATEB_H_REGION = int(round(_gateb_h_region_f))         # 5
# exp-001's own established BEHIND window (verbatim from that file):
# BEHIND = (slice(CX+R_CLK+15, CX+R_CLK+115), slice(CY-20,CY+20)),
# R_CLK=90 -- offset-from-center range [105,205) cells, x in [357,457).
GATEB_R_CLK = 90
GATEB_BEHIND_X_LO = GATEB_CX + GATEB_R_CLK + 15   # 357
GATEB_BEHIND_X_HI = GATEB_CX + GATEB_R_CLK + 115  # 457


def _run_gate_b(with_article):
    sim = Sim(GATEB_N, GATEB_N, cells_per_lambda=GATEB_CPL,
              courant_frac=GATEB_FRAC, absorb=GATEB_ABSORB)
    if with_article:
        materials.pec_disk(sim, GATEB_CX, GATEB_CY, GATEB_R_CORE)
        materials.graded_black_shell(sim, GATEB_CX, GATEB_CY, GATEB_R_CORE, GATEB_R_COAT)
    sim.add_line_source(GATEB_SRC_X, angle_deg=0.0)
    sim.run(GATEB_STEPS)
    return sc.full_capture(sim)


# ================================================================ beam-aligned frame
def u_hat_v_hat(theta_deg, sign):
    """u(theta)=(-cos,sin)*sign, v(theta)=(sin,cos)*sign -- NOTES.md's
    literal formula for sign=+1 (every R4_CONFIGS entry), mirror-flipped
    for sign=-1 (Gate B's own opposite source/object arrangement -- see
    module docstring Resolution Note 1). Orthonormal for either sign
    (scaling a unit, orthogonal pair by a common +-1 factor preserves both
    properties)."""
    t = math.radians(theta_deg)
    u = np.array([-math.cos(t), math.sin(t)]) * sign
    v = np.array([math.sin(t), math.cos(t)]) * sign
    return u, v


def downstream_sign(cfg):
    """+1 iff src_x > obj_x (NOTES.md's literal formula, unmodified --
    true for every R4_CONFIGS entry); -1 otherwise (Gate B's own
    geometry)."""
    return 1.0 if cfg["src_x"] > cfg["obj_x"] else -1.0


def _verify_orthonormal():
    for th in list(ANGLES) + [0.0, THETA_GATE_D]:
        for sign in (1.0, -1.0):
            u, v = u_hat_v_hat(th, sign)
            assert abs(np.dot(u, u) - 1.0) < 1e-12, (th, sign, "u not unit")
            assert abs(np.dot(v, v) - 1.0) < 1e-12, (th, sign, "v not unit")
            assert abs(np.dot(u, v)) < 1e-12, (th, sign, "u,v not orthogonal")


_verify_orthonormal()

# Confirm every R4_CONFIGS entry uses NOTES.md's literal formula unmodified
# (sign=+1), and Gate B's own geometry needs the disclosed flip (sign=-1) --
# a real geometry-fact assertion, not an assumption.
for _key in PAIR_KEYS_R4:
    assert downstream_sign(R4_CONFIGS[_key]) == 1.0, (
        f"{_key}: expected src_x>obj_x (sign=+1); geometry changed?")
_GATEB_CFG = dict(src_x=GATEB_SRC_X, obj_x=GATEB_CX)
assert downstream_sign(_GATEB_CFG) == -1.0, "Gate B geometry: expected src_x<obj_x (sign=-1)"


def P_point(cfg, theta_deg, standoff, sign=None):
    """P(theta) = round(obj + standoff*u(theta)). `sign` defaults to this
    config's own `downstream_sign()` (the generic, geometry-derived path);
    Gate D's independent hand-check passes it explicitly for clarity."""
    if sign is None:
        sign = downstream_sign(cfg)
    u, v = u_hat_v_hat(theta_deg, sign)
    p = np.array([cfg["obj_x"], cfg["obj_y"]], dtype=float) + standoff * u
    return (int(round(p[0])), int(round(p[1]))), u, v


def P_off_point(cfg, theta_deg, standoff, delta_lat, sign=None):
    (px, py), u, v = P_point(cfg, theta_deg, standoff, sign=sign)
    p_off = np.array([px, py], dtype=float) + delta_lat * v
    return (int(round(p_off[0])), int(round(p_off[1])))


# ================================================================ point/region readout
def block_mean_intensity(ez, px, py, h):
    xs = slice(px - h, px + h + 1)
    ys = slice(py - h, py + h + 1)
    block = ez[xs, ys]
    return float(np.mean(np.abs(block) ** 2)), complex(np.mean(block))


def point_intensity(ez, px, py):
    return float(np.abs(ez[px, py]) ** 2)


def kappa_at(ez_empty, ez_article, px, py, h):
    i_region_e, mean_e = block_mean_intensity(ez_empty, px, py, h)
    i_region_a, mean_a = block_mean_intensity(ez_article, px, py, h)
    i_point_e = point_intensity(ez_empty, px, py)
    i_point_a = point_intensity(ez_article, px, py)
    kappa_region = i_region_a / i_region_e if i_region_e != 0 else float("inf")
    kappa_point = i_point_a / i_point_e if i_point_e != 0 else float("inf")
    delta_phi = float(np.angle(mean_a / mean_e)) if mean_e != 0 else float("nan")
    return dict(i_region_empty=i_region_e, i_region_article=i_region_a,
                i_point_empty=i_point_e, i_point_article=i_point_a,
                kappa_region=kappa_region, kappa_point=kappa_point,
                delta_phi=delta_phi)


# ================================================================ Gate C / I0_corrected -- reuses _face_flux's own sx()/sy() formulas
# (mean-then-norm), lifted verbatim from lab/sections.py::_face_flux (those
# closures are private/nested, not importable -- reproduced here exactly,
# zero lab/ diff) evaluated pointwise along the fixed-x reference strip
# instead of summed over a box face.
def sx_profile(ez, hy, x, y_lo, y_hi):
    """Verbatim _face_flux.sx(xf) body, x=xf fixed, y in [y_lo,y_hi]."""
    ys = slice(y_lo, y_hi + 1)
    hy_at = 0.5 * (hy[x - 1, ys] + hy[x, ys])
    return -0.5 * np.real(ez[x, ys] * np.conj(hy_at))


def sy_profile_vertical(ez, hx, x, y_lo, y_hi):
    """_face_flux.sy(yf) transposed: fixed x (not fixed y), one Hx-
    interpolated-to-Ez-grid value per y in [y_lo,y_hi] (same 0.5*(hx[.,y-1]
    +hx[.,y]) interpolation _face_flux.sy() uses, just varied over y at
    fixed x instead of over x at fixed y)."""
    ys = slice(y_lo, y_hi + 1)
    hx_at = 0.5 * (hx[x, y_lo - 1:y_hi] + hx[x, y_lo:y_hi + 1])
    return 0.5 * np.real(ez[x, ys] * np.conj(hx_at))


def i0_corrected_and_iinc(cap_empty, cfg):
    cx, cy, hh = ref_for_r4(cfg)
    pi = sc.phasors(cap_empty)
    sxp = sx_profile(pi["ez"], pi["hy"], cx, cy - hh, cy + hh)
    syp = sy_profile_vertical(pi["ez"], pi["hx"], cx, cy - hh, cy + hh)
    mean_sx = float(np.mean(sxp))
    mean_sy = float(np.mean(syp))
    i0_corrected = math.sqrt(mean_sx ** 2 + mean_sy ** 2)
    box = box_for_r4(cfg, BOX_CLEARANCE_A_R4)
    w = sc.widths(cap_empty, cap_empty, box, (cx, cy, hh))
    i_inc = w["i_inc"]
    return dict(i0_corrected=i0_corrected, i_inc=i_inc, mean_sx=mean_sx, mean_sy=mean_sy)


# ================================================================ floor gate (R13/R14 lineage, house style)
def floor_gate(pool_values, label):
    arr = np.asarray(pool_values, dtype=float)
    rms = float(np.sqrt(np.mean(np.square(arr))))
    floor = FLOOR_FRAC * rms
    passes = [bool(v >= floor) for v in arr]
    n_unresolved = sum(1 for p in passes if not p)
    print(f"  [floor gate: {label}] n={len(arr)} rms={rms:.6e} floor={floor:.6e} "
          f"n_unresolved_by_construction={n_unresolved}")
    return dict(rms=rms, floor=floor, passes=passes, n_unresolved=n_unresolved)


# ================================================================ main
def main():
    print("=" * 78)
    print("exp-102 -- Coherent, phase-resolved downstream point-intensity instrument")
    print("=" * 78)
    t_start = time.time()
    n_fdtd_calls = 0
    n_fdtd_calls_actual = 0  # real Sim().run() calls executed by THIS process invocation
                              # (vs n_fdtd_calls, the experiment's nominal 26-call budget,
                              # which stays 26 regardless of cache hits -- see R19 assert)

    print(f"\nANGLES: {ANGLES}")
    print(f"PAIR_KEYS_R4: {PAIR_KEYS_R4}")
    print(f"D_STANDOFF={D_STANDOFF}  H_REGION={H_REGION}  DELTA_LAT={DELTA_LAT}  "
          f"FLOOR_FRAC={FLOOR_FRAC}")

    # ---------------------------------------------------------- direct-geometry margin check (R17)
    # Phase-1/3 D_STANDOFF/H_REGION/Delta_lat are estimates; verify every
    # P(theta)/P_off(theta) block sits >= H_REGION+absorb cells inside the
    # real Sim domain for every angle/config BEFORE any FDTD call.
    margin_report = {}
    for key in PAIR_KEYS_R4:
        cfg = R4_CONFIGS[key]
        for th in ANGLES:
            (px, py), u, v = P_point(cfg, th, D_STANDOFF)
            p_off = P_off_point(cfg, th, D_STANDOFF, DELTA_LAT)
            for name, (x, y) in (("P", (px, py)), ("P_off", p_off)):
                lo_x, hi_x = x - H_REGION, x + H_REGION
                lo_y, hi_y = y - H_REGION, y + H_REGION
                ok = (lo_x > cfg["absorb"] and hi_x < cfg["nx"] - cfg["absorb"]
                      and lo_y > cfg["absorb"] and hi_y < cfg["ny"] - cfg["absorb"])
                margin_report[f"{key}@{th}:{name}"] = dict(x=x, y=y, ok=ok)
                assert ok, f"MARGIN GATE FAILED: {key}@{th} {name}=({x},{y}) too close to absorb/boundary"
    print(f"[margin gate] {len(margin_report)} point blocks, all clear of absorb/boundary: PASS")

    # ============================================================
    # 24 real FDTD calls -- 6 angles x 2 configs x 2 conditions (R4 family)
    # ============================================================
    jobs = []
    for th in ANGLES:
        for key in PAIR_KEYS_R4:
            jobs.append((key, th, False, R4_STEPS, None))
            jobs.append((key, th, True, R4_STEPS, SIGMA_R4_CORRECTED))
    assert len(jobs) == 24, f"R19 call-count assert: expected 24 R4 jobs, got {len(jobs)}"
    print(f"\n-- {len(jobs)} R4-family FDTD calls queued --")
    captures, wall_r4, r4_from_cache = get_r4_captures(jobs)
    n_fdtd_calls += len(jobs)  # nominal experiment call BUDGET (NOTES.md: 26) -- unchanged
                                # regardless of cache; n_fdtd_calls_actual (below) tracks
                                # what THIS process invocation really ran.
    n_fdtd_calls_actual += 0 if r4_from_cache else len(jobs)
    assert len(captures) == 24
    print(f"R4-family wall time: {wall_r4:.1f}s ({wall_r4/60.0:.2f} min)  "
          f"[{'FROM CACHE' if r4_from_cache else 'FRESH FDTD'}]")

    # phasors, once per capture
    phasors = {k: sc.phasors(cap) for k, cap in captures.items()}

    # ============================================================
    # Gate A -- trivial-reduction identity (zero marginal FDTD)
    # ============================================================
    print("\n" + "=" * 78)
    print("GATE A -- trivial-reduction identity (no-object BOTH legs => kappa=1.0)")
    print("=" * 78)
    gate_a_max_dev = 0.0
    gate_a_n = 0
    for key in PAIR_KEYS_R4:
        cfg = R4_CONFIGS[key]
        for th in ANGLES:
            ez_empty = phasors[(key, th, False)]["ez"]
            (px, py), u, v = P_point(cfg, th, D_STANDOFF)
            p_off = P_off_point(cfg, th, D_STANDOFF, DELTA_LAT)
            for (x, y) in ((px, py), p_off):
                k = kappa_at(ez_empty, ez_empty, x, y, H_REGION)
                gate_a_max_dev = max(gate_a_max_dev, abs(k["kappa_region"] - 1.0),
                                      abs(k["kappa_point"] - 1.0))
                gate_a_n += 2
    gate_a_pass = gate_a_max_dev < 1e-10
    print(f"[Gate A] n_points={gate_a_n} max|kappa-1.0|={gate_a_max_dev:.3e}  PASS={gate_a_pass}")
    if not gate_a_pass:
        print("  *** GATE A FAILED -- recorded, NOT halting: NOTES.md's own 'What to build' "
              "list requires results.json to carry every gate's pass/fail and every "
              "Prediction's verdict regardless of any single gate's outcome; a hard halt "
              "here would silently drop Gates B/C/D and all 5 Predictions instead of "
              "reporting the failure honestly. ***")

    # ============================================================
    # Gate B -- known-good reproduction, R15-lineage (2 new FDTD calls)
    # ============================================================
    print("\n" + "=" * 78)
    print("GATE B -- known-good reproduction on native-scale flagship @ theta=0deg")
    print("=" * 78)
    t0 = time.time()
    cap_b_empty = _run_gate_b(with_article=False)
    cap_b_article = _run_gate_b(with_article=True)
    n_fdtd_calls += 2
    n_fdtd_calls_actual += 2  # Gate B is never cached -- always run fresh
    wall_gate_b = time.time() - t0
    print(f"Gate B wall time: {wall_gate_b:.1f}s")

    gateb_cfg = dict(obj_x=GATEB_CX, obj_y=GATEB_CY, src_x=GATEB_SRC_X)
    (gb_px, gb_py), gb_u, gb_v = P_point(gateb_cfg, 0.0, GATEB_D_STANDOFF)
    in_established_window = GATEB_BEHIND_X_LO <= gb_px < GATEB_BEHIND_X_HI
    print(f"[Gate B] D_STANDOFF rescale: R4-family 200cells/R4_R_OUT(156)=1.282x r_out; "
          f"native GATEB_CPL={GATEB_CPL} vs R4_CPL[600]={R4_CPL[600]} (ratio "
          f"{_GATEB_R_OUT_RATIO}) => GATEB_D_STANDOFF={GATEB_D_STANDOFF}cells "
          f"({GATEB_D_STANDOFF/GATEB_R_COAT:.3f}x r_out), GATEB_H_REGION={GATEB_H_REGION}cells "
          f"(holds the SAME standoff/r_out and region/r_out ratios the R4 family used)")
    print(f"[Gate B] P(0deg) = ({gb_px},{gb_py})  u={gb_u}  sign={downstream_sign(gateb_cfg)}  "
          f"(SRC_X={GATEB_SRC_X}, CX={GATEB_CX} -- downstream is +x here, opposite of R4 family)")
    print(f"[Gate B] exp-001's own established BEHIND window: x in "
          f"[{GATEB_BEHIND_X_LO},{GATEB_BEHIND_X_HI})  P(0deg).x={gb_px}  "
          f"inside_window={in_established_window}")
    assert gb_px > GATEB_SRC_X, "Gate B point landed upstream of the source -- sign bug"
    assert gb_px > GATEB_CX + GATEB_R_COAT, (
        "Gate B point landed inside/short of the coating's own outer radius -- geometry bug")

    ez_b_empty = sc.phasors(cap_b_empty)["ez"]
    ez_b_article = sc.phasors(cap_b_article)["ez"]
    gate_b_kappa = kappa_at(ez_b_empty, ez_b_article, gb_px, gb_py, GATEB_H_REGION)
    gate_b_pass = 0.005 <= gate_b_kappa["kappa_region"] <= 0.05
    print(f"[Gate B] kappa_region(0deg) = {gate_b_kappa['kappa_region']:.6e}  "
          f"kappa_point={gate_b_kappa['kappa_point']:.6e}  "
          f"PASS (in [0.005,0.05]) = {gate_b_pass}")
    if not gate_b_pass:
        print(f"  *** GATE B FAILED -- kappa_region={gate_b_kappa['kappa_region']:.6e} is "
              f"outside the pre-registered [0.005,0.05] band (established beam_behind "
              f"anchor: 1.82% at 600nm, experiments/001-.../results.json['absorber-600']), "
              f"even AFTER rescaling GATEB_D_STANDOFF/GATEB_H_REGION to hold the same "
              f"standoff/r_out ratio the R4-family value was designed around (see comment "
              f"above GATEB_N). Recorded, NOT halting -- same reporting-completeness "
              f"rationale as Gate A above. Diagnosis: this is a GENUINE, HONEST FAILURE, "
              f"not a further implementation bug -- exp-001's own established figure is a "
              f"WIDE WINDOW average (x in [{GATEB_BEHIND_X_LO},{GATEB_BEHIND_X_HI}), i.e. "
              f"~1.35x-2.63x r_out from center) of a shadow that fills back in with "
              f"increasing distance, whereas this instrument's rescaled point sits at "
              f"~1.28x r_out ({'INSIDE' if in_established_window else 'BEFORE'} that "
              f"established window) -- much closer to the object, in the near-field where "
              f"the shadow reads measurably darker. A point/region sample and a window "
              f"envelope average at two different standoffs are not directly comparable; "
              f"forcing the point further out to land inside the window would be exactly "
              f"the kind of post-hoc parameter search LOGBOOK's R5 already rules out. This "
              f"means: only Gates A (trivial identity) and D (fault-injection positive "
              f"control) independently support trusting the primary-channel Predictions "
              f"1/3/4/5 this cycle -- Gate B's cross-scale reproduction against the OLD "
              f"established figure is NOT validated, a real limitation for Phase 5. ***")

    # ============================================================
    # Gate C / Prediction 2 -- absolute-normalization self-consistency
    # ============================================================
    print("\n" + "=" * 78)
    print("GATE C / PREDICTION 2 -- I0_corrected*u_x(theta) vs i_inc (see Resolution Note 2)")
    print("=" * 78)
    gate_c_rows = {}
    gate_c_max_dev = 0.0
    for th in ANGLES:
        for key in PAIR_KEYS_R4:
            cfg = R4_CONFIGS[key]
            cap_empty = captures[(key, th, False)]
            r = i0_corrected_and_iinc(cap_empty, cfg)
            u, v = u_hat_v_hat(th, downstream_sign(cfg))
            dev = abs(r["i0_corrected"] * u[0] - r["i_inc"]) / r["i0_corrected"]
            # DISCLOSURE (per Director's explicit instruction): the ORIGINAL Gate C
            # formula compared I0_corrected*cos(theta) (sign-blind) against i_inc --
            # a bare cos(theta) assumes the incident wave's x-flux is +cos(theta), but
            # the R4 family's actual propagation direction is u(theta)=(-cos,sin)
            # (Resolution Note 2 above), so i_inc genuinely comes out with the OPPOSITE
            # sign of I0_corrected*cos(theta) even though they closely agree in
            # magnitude -- a uniform ~150% "deviation" at every cell, not per-cell
            # noise. Recorded here for disclosure, NOT used for the pass/fail verdict.
            dev_original_erroneous = abs(r["i0_corrected"] * math.cos(math.radians(th))
                                          - r["i_inc"]) / r["i0_corrected"]
            gate_c_rows[(key, th)] = dict(**r, u_x=float(u[0]), dev=dev,
                                           dev_original_erroneous_cos_theta=dev_original_erroneous)
            gate_c_max_dev = max(gate_c_max_dev, dev)
            print(f"  [{key}] theta={th:+.6f}  I0_corrected={r['i0_corrected']:.6e}  "
                  f"i_inc={r['i_inc']:.6e}  u_x={u[0]:+.6f}  mean_sx={r['mean_sx']:.6e}  "
                  f"mean_sy={r['mean_sy']:.6e}  dev={dev:.4%}  "
                  f"(ORIGINAL erroneous bare-cos(theta) dev={dev_original_erroneous:.4%})")
            assert abs(r["mean_sx"] - r["i_inc"]) < 1e-9 * max(abs(r["i_inc"]), 1.0), (
                "sx_profile mean should reproduce sections.widths()'s own i_inc exactly")
    gate_c_pass = gate_c_max_dev <= 0.01
    gate_c_max_dev_original_erroneous = max(
        v["dev_original_erroneous_cos_theta"] for v in gate_c_rows.values())
    print(f"[Gate C/Pred2] max deviation across {len(gate_c_rows)} (angle,config) cells: "
          f"{gate_c_max_dev:.4%}  PASS (<=1%) = {gate_c_pass}  "
          f"(disclosure: the ORIGINAL erroneous bare-cos(theta) formula gave max "
          f"dev={gate_c_max_dev_original_erroneous:.4%} -- a uniform sign-flip artifact, "
          f"not a physics failure; corrected using u_x(theta)=-cos(theta) per Resolution "
          f"Note 2 above, independently re-derived from the already-vetted u(theta) "
          f"propagation-direction formula plus the physical fact S is parallel to u for "
          f"a plane wave, not fit to match)")

    # ============================================================
    # Primary channel: kappa(theta), Delta_phi(theta), I_abs(theta), kappa_off(theta)
    # ============================================================
    print("\n" + "=" * 78)
    print("PRIMARY CHANNEL -- kappa(theta), kappa_off(theta), I_abs(theta), Delta_phi(theta)")
    print("=" * 78)
    rows = {}
    for th in ANGLES:
        for key in PAIR_KEYS_R4:
            cfg = R4_CONFIGS[key]
            ez_empty = phasors[(key, th, False)]["ez"]
            ez_article = phasors[(key, th, True)]["ez"]
            (px, py), u, v = P_point(cfg, th, D_STANDOFF)
            p_off = P_off_point(cfg, th, D_STANDOFF, DELTA_LAT)

            k_on = kappa_at(ez_empty, ez_article, px, py, H_REGION)
            k_off = kappa_at(ez_empty, ez_article, p_off[0], p_off[1], H_REGION)

            i0c = gate_c_rows[(key, th)]["i0_corrected"]
            i_abs = 0.5 * k_on["i_region_article"] / i0c

            row = dict(P=[px, py], P_off=list(p_off),
                       kappa_region=k_on["kappa_region"], kappa_point=k_on["kappa_point"],
                       delta_phi=k_on["delta_phi"],
                       i_region_empty=k_on["i_region_empty"], i_region_article=k_on["i_region_article"],
                       i_point_empty=k_on["i_point_empty"], i_point_article=k_on["i_point_article"],
                       kappa_off_region=k_off["kappa_region"], kappa_off_point=k_off["kappa_point"],
                       i_off_region_empty=k_off["i_region_empty"],
                       i0_corrected=i0c, i_abs=i_abs)
            rows[(key, th)] = row
            print(f"  [{key}] theta={th:+.6f}  P={row['P']}  kappa_region={row['kappa_region']:.6e}  "
                  f"kappa_point={row['kappa_point']:.6e}  kappa_off_region={row['kappa_off_region']:.6e}  "
                  f"I_abs={row['i_abs']:.6e}  delta_phi={row['delta_phi']:+.4f}rad")
    assert len(rows) == 12, f"R19 row-count assert: expected 12 primary rows, got {len(rows)}"

    # ============================================================
    # Floor gate (amplitude-floor discipline, proactive house-style)
    # ============================================================
    print("\n" + "=" * 78)
    print("FLOOR GATE -- amplitude-floor discipline (FLOOR_FRAC=0.10, house style)")
    print("=" * 78)
    keys_order = [(key, th) for th in ANGLES for key in PAIR_KEYS_R4]
    fg_region = floor_gate([rows[kt]["i_region_empty"] for kt in keys_order], "region@P (i_region_empty)")
    fg_point = floor_gate([rows[kt]["i_point_empty"] for kt in keys_order], "point@P (i_point_empty)")
    fg_off = floor_gate([rows[kt]["i_off_region_empty"] for kt in keys_order], "region@P_off (i_off_region_empty)")
    for idx, kt in enumerate(keys_order):
        rows[kt]["floor_pass_region"] = fg_region["passes"][idx]
        rows[kt]["floor_pass_point"] = fg_point["passes"][idx]
        rows[kt]["floor_pass_off_region"] = fg_off["passes"][idx]
        rows[kt]["outcome_region"] = "resolved" if fg_region["passes"][idx] else "UNRESOLVED-BY-CONSTRUCTION"
        rows[kt]["outcome_point"] = "resolved" if fg_point["passes"][idx] else "UNRESOLVED-BY-CONSTRUCTION"
        rows[kt]["outcome_off_region"] = "resolved" if fg_off["passes"][idx] else "UNRESOLVED-BY-CONSTRUCTION"
    total_unresolved = fg_region["n_unresolved"] + fg_point["n_unresolved"] + fg_off["n_unresolved"]
    print(f"[floor gate] total UNRESOLVED-BY-CONSTRUCTION entries across all 3 pools: {total_unresolved}")

    # ============================================================
    # Gate D -- fault-injection positive control (zero marginal FDTD)
    # ============================================================
    print("\n" + "=" * 78)
    print(f"GATE D -- fault-injection positive control @ theta={THETA_GATE_D}deg")
    print("=" * 78)
    gate_d_report = {}
    gate_d_pass = True
    for key in PAIR_KEYS_R4:
        cfg = R4_CONFIGS[key]
        obj_x, obj_y = cfg["obj_x"], cfg["obj_y"]

        # (1) INDEPENDENT hand-computation of P(theta) from raw Sim geometry
        # -- a freestanding trig expression, NOT a call to P_point()/
        # u_hat_v_hat(), guarding against a bug in that shared code path
        # (dx=1 in these grid-native cells; not separately relevant).
        t_rad = THETA_GATE_D * math.pi / 180.0
        px_hand = obj_x + D_STANDOFF * (-math.cos(t_rad))
        py_hand = obj_y + D_STANDOFF * (math.sin(t_rad))
        px_hand_r = int(round(px_hand))
        py_hand_r = int(round(py_hand))

        (px_code, py_code), u_code, v_code = P_point(cfg, THETA_GATE_D, D_STANDOFF)
        match = (px_hand_r == px_code) and (py_hand_r == py_code)
        print(f"  [{key}] hand P={px_hand_r,py_hand_r}  code P={px_code,py_code}  match={match}")
        assert match, f"GATE D (1) FAILED: hand-computed P != code P for {key}"

        # (2) perturb P by +20 cells along u(theta), recompute kappa on the
        # SAME already-captured article-scene field -- zero new FDTD.
        p_pert = np.array([px_code, py_code], dtype=float) + 20.0 * u_code
        ppx, ppy = int(round(p_pert[0])), int(round(p_pert[1]))

        ez_empty = phasors[(key, THETA_GATE_D, False)]["ez"]
        ez_article = phasors[(key, THETA_GATE_D, True)]["ez"]
        k_correct = kappa_at(ez_empty, ez_article, px_code, py_code, H_REGION)
        k_pert = kappa_at(ez_empty, ez_article, ppx, ppy, H_REGION)

        rel_dev_region = (abs(k_pert["kappa_region"] - k_correct["kappa_region"])
                           / abs(k_correct["kappa_region"]) if k_correct["kappa_region"] != 0 else float("inf"))
        rel_dev_point = (abs(k_pert["kappa_point"] - k_correct["kappa_point"])
                          / abs(k_correct["kappa_point"]) if k_correct["kappa_point"] != 0 else float("inf"))
        cell_pass = rel_dev_region > 0.05
        gate_d_pass = gate_d_pass and cell_pass
        gate_d_report[key] = dict(
            P=[px_code, py_code], P_perturbed=[ppx, ppy],
            kappa_region_correct=k_correct["kappa_region"], kappa_region_perturbed=k_pert["kappa_region"],
            kappa_point_correct=k_correct["kappa_point"], kappa_point_perturbed=k_pert["kappa_point"],
            rel_dev_region=rel_dev_region, rel_dev_point=rel_dev_point, cell_pass=cell_pass)
        print(f"  [{key}] kappa_region correct={k_correct['kappa_region']:.6e}  "
              f"perturbed={k_pert['kappa_region']:.6e}  rel_dev={rel_dev_region:.4%}  PASS(>5%)={cell_pass}")
    print(f"[Gate D] OVERALL PASS = {gate_d_pass}")

    # ============================================================
    # Score the 5 committed Predictions
    # ============================================================
    print("\n" + "=" * 78)
    print("PREDICTIONS")
    print("=" * 78)

    # Prediction 1: kappa(theta) in [0,0.10] at all 6 angles, both configs (region reading)
    p1_scored = [kt for kt in keys_order if rows[kt]["floor_pass_region"]]
    p1_violations = [kt for kt in p1_scored if not (0.0 <= rows[kt]["kappa_region"] < 0.10)]
    p1_verdict = "CONFIRMED" if not p1_violations else "FALSIFIED"
    print(f"\n[Prediction 1] kappa_region in [0,0.10] -- scored cells={len(p1_scored)}/12  "
          f"violations={len(p1_violations)}  VERDICT={p1_verdict}")
    for kt in keys_order:
        print(f"    {kt}: kappa_region={rows[kt]['kappa_region']:.6e}  "
              f"outcome={rows[kt]['outcome_region']}")

    # Prediction 2: Gate C itself (scored above as gate_c_pass/gate_c_max_dev)
    p2_verdict = "CONFIRMED" if gate_c_pass else "FALSIFIED"
    print(f"\n[Prediction 2] |I0_corrected*u_x(theta)-i_inc|/I0_corrected <= 0.01 at all "
          f"{len(gate_c_rows)} (angle,config) cells: max_dev={gate_c_max_dev:.4%}  VERDICT={p2_verdict}")

    # Prediction 3: kappa_off(theta) >= 0.90 at all 6 angles, both configs
    p3_scored = [kt for kt in keys_order if rows[kt]["floor_pass_off_region"]]
    p3_violations = [kt for kt in p3_scored if not (rows[kt]["kappa_off_region"] >= 0.90)]
    p3_verdict = "CONFIRMED" if not p3_violations else "FALSIFIED"
    print(f"\n[Prediction 3] kappa_off_region >= 0.90 -- scored cells={len(p3_scored)}/12  "
          f"violations={len(p3_violations)}  VERDICT={p3_verdict}")
    for kt in keys_order:
        print(f"    {kt}: kappa_off_region={rows[kt]['kappa_off_region']:.6e}  "
              f"outcome={rows[kt]['outcome_off_region']}")

    # Prediction 4: point-vs-region agree within factor of 3x, at all 6 angles (both configs)
    p4_report = {}
    p4_violations = []
    for kt in keys_order:
        kr, kp = rows[kt]["kappa_region"], rows[kt]["kappa_point"]
        if kr == 0 and kp == 0:
            ratio = 1.0
        elif kr == 0 or kp == 0:
            ratio = float("inf")
        else:
            ratio = max(kr, kp) / min(kr, kp)
        agree = ratio <= 3.0
        p4_report[kt] = dict(kappa_region=kr, kappa_point=kp, ratio=ratio, agree=agree)
        if not agree:
            p4_violations.append(kt)
    p4_verdict = "CONFIRMED" if not p4_violations else "FALSIFIED"
    print(f"\n[Prediction 4] point-vs-region agree within 3x -- violations={len(p4_violations)}  "
          f"VERDICT={p4_verdict}")
    for kt, r in p4_report.items():
        print(f"    {kt}: kappa_region={r['kappa_region']:.6e}  kappa_point={r['kappa_point']:.6e}  "
              f"ratio={r['ratio']:.3f}  agree={r['agree']}")

    # Prediction 5: Gate D itself
    p5_verdict = "CONFIRMED" if gate_d_pass else "FALSIFIED"
    print(f"\n[Prediction 5] Gate D fault-injection control (perturbed vs correct kappa differ "
          f">5% at theta={THETA_GATE_D}, both configs): VERDICT={p5_verdict}")

    total_wall = time.time() - t_start
    print(f"\nTotal wall time: {total_wall:.1f}s ({total_wall/60.0:.2f} min)")
    print(f"Nominal experiment call budget: {n_fdtd_calls} (expected 26 = 24 R4-family + 2 Gate B, "
          f"NOTES.md's Call budget -- unchanged regardless of cache hits)")
    print(f"Real FDTD calls executed by THIS run: {n_fdtd_calls_actual} "
          f"({'R4-family served from cache' if r4_from_cache else 'R4-family FRESH'} "
          f"+ 2 Gate B always-fresh)")
    assert n_fdtd_calls == 26, f"R19 call-count assert: expected 26 total FDTD calls, got {n_fdtd_calls}"

    result = dict(
        experiment="exp-102", panel_iteration=79,
        angles=ANGLES, pair_keys=list(PAIR_KEYS_R4),
        d_standoff=D_STANDOFF, h_region=H_REGION, delta_lat=DELTA_LAT, floor_frac=FLOOR_FRAC,
        n_fdtd_calls=n_fdtd_calls, n_fdtd_calls_actual_this_run=n_fdtd_calls_actual,
        r4_family_source="cache" if r4_from_cache else "fresh",
        wall_r4_s=wall_r4, wall_gate_b_s=wall_gate_b, total_wall_s=total_wall,
        gates=dict(
            A=dict(pass_=gate_a_pass, max_dev=gate_a_max_dev, n_points=gate_a_n),
            B=dict(pass_=gate_b_pass, kappa_region=gate_b_kappa["kappa_region"],
                   kappa_point=gate_b_kappa["kappa_point"], P=[gb_px, gb_py],
                   band=[0.005, 0.05],
                   d_standoff=GATEB_D_STANDOFF, h_region=GATEB_H_REGION,
                   r_out_ratio=_GATEB_R_OUT_RATIO,
                   established_window_x=[GATEB_BEHIND_X_LO, GATEB_BEHIND_X_HI],
                   p_inside_established_window=in_established_window,
                   note="D_STANDOFF/H_REGION rescaled from the R4-family's 200/10 cells "
                        "by GATEB_R_COAT/R4_R_OUT=0.5 to hold the same standoff/r_out "
                        "ratio (Phase-4 diagnostic fix). Gate B STILL FAILS after this "
                        "fix (kappa_region below the band floor, not above it as in the "
                        "original crash) -- diagnosed as a genuine, honest failure: the "
                        "rescaled point sits closer to the object than exp-001's own "
                        "established BEHIND window, in the near-field where the shadow "
                        "reads darker, not an implementation bug. See run_output.txt for "
                        "full diagnosis."),
            C=dict(pass_=gate_c_pass, max_dev=gate_c_max_dev,
                   formula="|I0_corrected(theta)*u_x(theta) - i_inc(theta)| / I0_corrected(theta) <= 0.01, "
                           "u_x(theta)=-cos(theta) for the R4 family (u(theta)=(-cos,sin) per NOTES.md)",
                   disclosure_original_erroneous_formula=(
                       "|I0_corrected(theta)*cos(theta) - i_inc(theta)| / I0_corrected(theta) -- "
                       "sign-blind bare cos(theta), gave a uniform ~145-160% deviation at every "
                       "(angle,config) cell (a systematic sign-flip artifact, not per-cell noise, "
                       "since the R4 family's real propagation direction is u(theta)=(-cos,sin), "
                       "not (cos,sin)); NOT used for the pass/fail verdict, kept for disclosure"),
                   max_dev_original_erroneous=gate_c_max_dev_original_erroneous,
                   rows={f"{k}@{t}": v for (k, t), v in gate_c_rows.items()}),
            D=dict(pass_=gate_d_pass, report=gate_d_report),
        ),
        primary_rows={f"{k}@{t}": v for (k, t), v in rows.items()},
        floor_gate=dict(
            region=dict(rms=fg_region["rms"], floor=fg_region["floor"], n_unresolved=fg_region["n_unresolved"]),
            point=dict(rms=fg_point["rms"], floor=fg_point["floor"], n_unresolved=fg_point["n_unresolved"]),
            off_region=dict(rms=fg_off["rms"], floor=fg_off["floor"], n_unresolved=fg_off["n_unresolved"]),
            total_unresolved=total_unresolved,
        ),
        predictions=dict(
            p1_on_axis_kappa=dict(verdict=p1_verdict, n_scored=len(p1_scored), n_violations=len(p1_violations),
                                    cells={f"{k}@{t}": rows[(k, t)]["kappa_region"] for (k, t) in keys_order}),
            p2_gate_c=dict(verdict=p2_verdict, max_dev=gate_c_max_dev),
            p3_off_axis_kappa=dict(verdict=p3_verdict, n_scored=len(p3_scored), n_violations=len(p3_violations),
                                     cells={f"{k}@{t}": rows[(k, t)]["kappa_off_region"] for (k, t) in keys_order}),
            p4_point_vs_region=dict(verdict=p4_verdict, n_violations=len(p4_violations),
                                      cells={f"{k}@{t}": p4_report[(k, t)] for (k, t) in keys_order}),
            p5_gate_d=dict(verdict=p5_verdict, report=gate_d_report),
        ),
    )
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(result, f, indent=2, default=str)
    print("\nresults.json written.")
    return result


if __name__ == "__main__":
    main()
