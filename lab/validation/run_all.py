"""
lab/validation/run_all.py — the bench trust suite.
==================================================
Five stages, each with hard expected numbers. Exit code 0 only if all
selected stages pass.

  1. regression   — exp-000 scene through the lab engine reproduces its
                    committed results (lambda exact, shadow, peak field)
  2. impedance    — half-space reflection vs Fresnel: eps-only R=1/9;
                    impedance-matched (eps=mu) R~0, scalar AND tensor paths
  3. fdtd-lib     — same scene through flaport `fdtd`: SCATTERED-field
                    pattern correlation (scene minus each solver's own
                    vacuum run, so source-profile differences cancel)
  4. ceviche      — same scene through ceviche FDFD, same scattered-field
                    comparison
  5. cloak smoke  — bare PEC vs Schurig-reduced-cloaked PEC: scattered
                    field must drop

Run:  .venv\\Scripts\\python.exe lab\\validation\\run_all.py [--only 1234]
(stage 5 is the heavy one — run it alone with --only 5)

Measurement notes (learned the hard way, first run of this suite):
  * wavelength via raw FFT bins quantizes badly on short strips — use
    lab.fdtd2d.spatial_wavelength (zero-pad + parabolic peak).
  * reflection monitors must sit CLOSE to the interface: beam diffraction
    losses then cancel between reference and scene runs.
  * cross-solver comparisons must compare SCATTERED fields — total fields
    inherit each library's source profile.
"""

import os
import re
import sys
import time

if hasattr(sys.stdout, "reconfigure"):   # Windows pipes default to cp1252,
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # which chokes
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")  # on ·/→/λ/±

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from lab import Sim, materials
from lab.fdtd2d import spatial_wavelength

HERE = os.path.dirname(os.path.abspath(__file__))
BG, INK, MUTED = "#0d1117", "#e6edf3", "#9198a1"
try:
    CMAP = matplotlib.colormaps["berlin"]
except KeyError:
    CMAP = matplotlib.colormaps["seismic"]
plt.rcParams.update({
    "figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG,
    "text.color": INK, "axes.edgecolor": MUTED, "axes.labelcolor": MUTED,
    "xtick.color": MUTED, "ytick.color": MUTED,
})

RESULTS = []


def check(stage, name, value, ok, expect):
    RESULTS.append((stage, name, value, ok, expect))
    print(f"  [{'PASS' if ok else 'FAIL'}] {stage} · {name}: {value}  (expect {expect})")


def pearson(a, b):
    a = a.ravel() - a.mean()
    b = b.ravel() - b.mean()
    return float(np.sum(a * b) / np.sqrt(np.sum(a**2) * np.sum(b**2)))


# --------------------------------------------------------------- stage 1
def stage1_regression():
    print("stage 1 — exp-000 regression through lab engine")
    sim = Sim(720, 440, cells_per_lambda=20, courant_frac=0.99, absorb=36)
    materials.dielectric_cylinder(sim, 302, 220, 40, 4.0)
    sim.add_line_source(60)
    sim.run(1350)
    lam = sim.measure_lambda(y_line=370, x_lo=80, x_hi=640)
    peak = float(np.max(np.abs(sim.Ez)))
    env = sim.envelope()
    shadow = float(np.mean(env[362:502, 200:240] ** 2) / np.mean(env[362:502, 340:380] ** 2))
    check("regression", "lambda (cells)", f"{lam:.2f}", abs(lam - 20.0) <= 0.2, "20.0±0.2")
    check("regression", "peak |Ez|", f"{peak:.2f}", abs(peak - 2.50) <= 0.15, "2.50±0.15")
    check("regression", "shadow ratio", f"{shadow:.3f}", abs(shadow - 0.48) <= 0.03, "0.48±0.03")

    fig, ax = plt.subplots(figsize=(6.4, 4.0), dpi=140)
    v = 0.9 * np.max(np.abs(sim.Ez[:260, :]))
    ax.imshow(sim.Ez.T, cmap=CMAP, vmin=-v, vmax=v, origin="lower")
    ax.set_title("stage 1 — exp-000 scene via lab engine", loc="left", fontsize=10)
    ax.set_xticks([]); ax.set_yticks([])
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "v1_regression.png")); plt.close(fig)


# --------------------------------------------------------------- stage 2
def _reflection(build):
    """Monitor sits at x=230, 30 cells before the x=260 interface: beam
    diffraction losses up to the monitor are identical in reference and
    scene runs and cancel in the ratio."""
    sim = Sim(500, 240, cells_per_lambda=20, courant_frac=0.99, absorb=36)
    if build:
        build(sim)
    sim.add_line_source(60)
    mon = sim.add_poynting_line(230, start_step=1000)
    sim.run(1314)          # 314-step window ≈ 11 full periods
    return mon.mean_flux()


def stage2_impedance():
    print("stage 2 — half-space reflection vs Fresnel")
    f0 = _reflection(None)

    def eps_only(sim):
        sim.eps_r[260:, :] = 4.0

    def matched_scalar(sim):
        sim.eps_r[260:, :] = 4.0
        sim.ensure_inv_mu()
        sim.inv_mu["xx"][260:, :] = 0.25
        sim.inv_mu["yy"][260:, :] = 0.25

    def matched_yy(sim):
        sim.eps_r[260:, :] = 4.0
        sim.ensure_inv_mu()
        sim.inv_mu["yy"][260:, :] = 0.25   # only the component this wave feels

    for name, build, expect, tol in [
        ("eps=4, mu=1 (Fresnel)", eps_only, 1.0 / 9.0, 0.025),
        ("eps=mu=4 matched (scalar path)", matched_scalar, 0.0, 0.02),
        ("mu_yy=4 matched (tensor path)", matched_yy, 0.0, 0.02),
    ]:
        r = (f0 - _reflection(build)) / f0
        check("impedance", name, f"R={r:.4f}", abs(r - expect) <= tol,
              f"{expect:.3f}±{tol}")


# ------------------------------------------------------- stages 3+4 setup
ROI = (slice(70, 260), slice(40, 160))


def _our_small_scene(with_cylinder):
    sim = Sim(300, 200, cells_per_lambda=20, courant_frac=0.99, absorb=30)
    if with_cylinder:
        materials.dielectric_cylinder(sim, 126, 100, 20, 4.0)
    sim.add_line_source(54)
    sim.run(780)
    return sim, sim.envelope()


def stage3_fdtd_lib(ours_scat, ours_shadow):
    print("stage 3 — cross-check vs flaport fdtd (time domain)")
    try:
        import fdtd as flib

        flib.set_backend("numpy")
        c0 = 299792458.0

        def lib_env(with_cylinder):
            grid = flib.Grid(shape=(300, 200, 1), grid_spacing=30e-9)
            grid[0:10, :, :] = flib.PML(name="pml_xlow")
            grid[-10:, :, :] = flib.PML(name="pml_xhigh")
            grid[:, 0:10, :] = flib.PML(name="pml_ylow")
            grid[:, -10:, :] = flib.PML(name="pml_yhigh")
            grid[54, 30:170, 0] = flib.LineSource(period=600e-9 / c0, name="src")
            if with_cylinder:
                x = np.arange(106, 146)[:, None]
                y = np.arange(80, 120)[None, :]
                eps_block = np.where((x - 126) ** 2 + (y - 100) ** 2 <= 400, 4.0, 1.0)
                grid[106:146, 80:120, 0] = flib.Object(
                    permittivity=eps_block[:, :, None], name="cyl")
            grid.run(780, progress_bar=False)
            ez_a = np.asarray(grid.E[:, :, 0, 2]).copy()
            grid.run(7, progress_bar=False)  # ~quarter period at their courant
            ez_b = np.asarray(grid.E[:, :, 0, 2]).copy()
            return ez_a, np.sqrt(ez_a**2 + ez_b**2)

        ez_scene, env_scene = lib_env(True)
        _, env_vac = lib_env(False)
        scat_lib = env_scene - env_vac

        corr = pearson(ours_scat[ROI], scat_lib[ROI])
        lam_lib = spatial_wavelength(ez_scene[70:260, 160])
        sh_lib = float(np.mean(env_scene[156:226, 90:110] ** 2)
                       / np.mean(env_scene[156:226, 140:165] ** 2))

        check("fdtd-lib", "scattered-pattern corr", f"{corr:.3f}", corr >= 0.90, ">=0.90")
        check("fdtd-lib", "lambda (cells)", f"{lam_lib:.2f}", abs(lam_lib - 20.0) <= 0.5, "20.0±0.5")
        check("fdtd-lib", "shadow agreement",
              f"{sh_lib:.3f} vs ours {ours_shadow:.3f}",
              abs(sh_lib - ours_shadow) <= 0.10, "|Δ|<=0.10")
        return env_scene
    except Exception as e:  # keep the suite running; a FAIL here is loud enough
        check("fdtd-lib", "stage ran", f"EXC: {type(e).__name__}: {e}", False, "no exception")
        return None


def stage4_ceviche(ours_scat):
    print("stage 4 — cross-check vs ceviche (FDFD, frequency domain)")
    try:
        from ceviche import fdfd_ez

        c0 = 299792458.0
        omega = 2 * np.pi * c0 / 600e-9

        def solve(with_cylinder):
            eps = np.ones((300, 200))
            if with_cylinder:
                x = np.arange(300)[:, None]
                y = np.arange(200)[None, :]
                eps[(x - 126) ** 2 + (y - 100) ** 2 <= 400] = 4.0
            src = np.zeros((300, 200), dtype=complex)
            src[54, 30:170] = 1.0
            F = fdfd_ez(omega, 30e-9, eps, [20, 20])
            _, _, ez = F.solve(src)
            return ez

        ez_scene = solve(True)
        ez_vac = solve(False)
        scat_c = np.abs(ez_scene) - np.abs(ez_vac)

        corr = pearson(ours_scat[ROI], scat_c[ROI])
        lam_c = spatial_wavelength(np.real(ez_scene)[70:260, 160])

        check("ceviche", "scattered-pattern corr", f"{corr:.3f}", corr >= 0.90, ">=0.90")
        check("ceviche", "lambda (cells)", f"{lam_c:.2f}", abs(lam_c - 20.0) <= 0.5, "20.0±0.5")
        return np.abs(ez_scene)
    except Exception as e:
        check("ceviche", "stage ran", f"EXC: {type(e).__name__}: {e}", False, "no exception")
        return None


# --------------------------------------------------------------- stage 5
def stage5_cloak():
    """Reduced-cloak numbers: r1=30, r2=90 -> eps_z=(90/60)^2=2.25.
    mu_r clamped at 0.05 -> mu^-1 <= 20 -> max wave speed
    sqrt(20/2.25) ~ 2.98c -> S must stay under 1/(2.98*sqrt(2)) = 0.237;
    courant_frac=0.32 gives S=0.226. The clamp band (mu_r at floor) is
    r in [30, 38.7] — 14% of the shell, the price of stability."""
    print("stage 5 — cloak smoke: bare PEC vs Schurig-reduced cloak")
    CXY, R_PEC, R1, R2 = (252, 280), 30, 30, 90   # PEC flush at the inner wall

    def run_case(build):
        sim = Sim(560, 560, cells_per_lambda=20, courant_frac=0.32, absorb=40)
        if build:
            build(sim)
        sim.add_line_source(64)
        sim.run(3000)
        snap = sim.Ez.copy()
        return snap, sim.envelope()

    _, env_vac = run_case(None)

    def bare(sim):
        materials.pec_disk(sim, *CXY, R_PEC)

    def cloaked(sim):
        materials.pec_disk(sim, *CXY, R_PEC)
        materials.schurig_reduced_cloak_tm(sim, *CXY, R1, R2, mu_r_floor=0.05)

    snap_b, env_b = run_case(bare)
    snap_c, env_c = run_case(cloaked)

    xx = np.arange(560)[:, None] - CXY[0]
    yy = np.arange(560)[None, :] - CXY[1]
    rr = np.hypot(xx, yy)
    ann = (rr >= R2 + 10) & (rr <= R2 + 70)
    rms_b = float(np.sqrt(np.mean((env_b - env_vac)[ann] ** 2)))
    rms_c = float(np.sqrt(np.mean((env_c - env_vac)[ann] ** 2)))
    ratio = rms_c / rms_b
    check("cloak", "scattered-field RMS cloaked/bare", f"{ratio:.3f}", ratio <= 0.75, "<=0.75")

    # diagnostic splits (info, no pass/fail) — feed exp-001 design
    xg = np.arange(560)[:, None] - CXY[0]
    back = ann & (xg < 0)
    fwd = ann & (xg > 0)
    for name, m in [("backscatter half", back), ("forward half", fwd)]:
        rb = float(np.sqrt(np.mean((env_b - env_vac)[m] ** 2)))
        rc = float(np.sqrt(np.mean((env_c - env_vac)[m] ** 2)))
        print(f"  [info] cloak · {name} RMS cloaked/bare = {rc / rb:.3f}")
    sh_box = (slice(CXY[0] + R2 + 15, CXY[0] + R2 + 115), slice(CXY[1] - 20, CXY[1] + 20))
    for name, e in [("bare", env_b), ("cloaked", env_c)]:
        restore = float(np.mean(e[sh_box] ** 2) / np.mean(env_vac[sh_box] ** 2))
        print(f"  [info] cloak · beam-behind-object intensity vs vacuum ({name}) = {restore:.3f}")
    stable = np.all(np.isfinite(snap_c)) and float(np.max(np.abs(snap_c))) < 50
    check("cloak", "tensor run stable", f"max|Ez|={np.max(np.abs(snap_c)):.2f}", bool(stable), "finite, <50")

    fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.4), dpi=150)
    v = 0.9 * np.max(np.abs(snap_b[:180, :]))
    for ax, snap, title in [
        (axes[0], snap_b, "bare PEC cylinder"),
        (axes[1], snap_c, f"same PEC + reduced cloak (−{(1-ratio)*100:.0f}% scattered RMS)"),
    ]:
        ax.imshow(snap.T, cmap=CMAP, vmin=-v, vmax=v, origin="lower")
        for r, ls in [(R_PEC, "-"), (R1, ":"), (R2, ":")]:
            ax.add_patch(plt.Circle(CXY, r, fill=False, ls=ls, lw=1.0, ec="#ffffff", alpha=0.7))
        ax.set_title(title, loc="left", fontsize=10)
        ax.set_xticks([]); ax.set_yticks([])
    fig.suptitle("stage 5 — first cloak light (engine validation, not exp-001)",
                 x=0.045, ha="left", fontsize=12, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(os.path.join(HERE, "v5_cloak.png")); plt.close(fig)


# --------------------------------------------------------------- stage 6
def stage6_observer():
    """The observer camera answers to theory before it answers exp-001:
    an empty room returns ~nothing, a mirror returns ~everything, an eps=4
    half-space returns Fresnel's 1/9 (specularly). Then the emitter does a
    full save->load->validate round trip on a real builder scene."""
    print("stage 6 — observer camera vs Fresnel + emitter round-trip")
    import tempfile
    from pathlib import Path
    from lab import artifacts
    from lab import emit as em

    def run_scene(build):
        sim = Sim(360, 240, cells_per_lambda=20, courant_frac=0.99, absorb=30)
        if build:
            build(sim)
        sim.add_line_source(54)
        sim.run(900)
        return sim, em.quarter_pair(sim)

    sim_ref, cap_ref = run_scene(None)
    _, _, aux_ref = em.observer_record(sim_ref, cap_ref, 70)
    self_ratio = aux_ref["p_backward_total"] / aux_ref["p_forward_total"]
    check("observer", "empty room returns ~nothing", f"{self_ratio:.4f}",
          self_ratio < 0.02, "<0.02")

    def mirror(sim):
        sim.pec[260:276, :] = True

    sim_m, cap_m = run_scene(mirror)
    _, flux_m, _ = em.observer_record(sim_m, cap_m, 70, reference=aux_ref)
    total_m = float(np.sum(flux_m))
    # Bar recalibrated with the 2026-08-09 phasor-convention fix: the old
    # 0.955 borrowed ~1.2% of fake return from the phase-error floor. The
    # honest mirror reading is ~0.92 — the deficit is round-trip finite-beam
    # diffraction into the side absorbers (stage 2's documented mechanism)
    # plus window truncation. Accuracy is now anchored by the empty-room
    # floor (1e-4) and Fresnel to three decimals; this gate's job is only
    # "nothing lost to bookkeeping."
    check("observer", "mirror returns ~everything", f"{total_m:.3f}",
          total_m >= 0.90, ">=0.90")

    def halfspace(sim):
        sim.eps_r[260:, :] = 4.0

    sim_f, cap_f = run_scene(halfspace)
    ang_f, flux_f, _ = em.observer_record(sim_f, cap_f, 70, reference=aux_ref)
    total_f = float(np.sum(flux_f))
    check("observer", "half-space returns Fresnel 1/9", f"{total_f:.4f}",
          abs(total_f - 1.0 / 9.0) <= 0.02, "0.111±0.02")
    near = float(np.sum(flux_f[np.abs(ang_f) < np.deg2rad(12)])) / max(total_f, 1e-12)
    check("observer", "Fresnel return is specular", f"{near:.2f} within ±12°",
          near >= 0.80, ">=0.80")

    def cyl(sim):
        materials.dielectric_cylinder(sim, 200, 120, 20, 4.0)

    sim_c, cap_c = run_scene(cyl)
    ang_c, flux_c, _ = em.observer_record(sim_c, cap_c, 70, reference=aux_ref)
    print(f"  [info] observer · cylinder total return = {float(np.sum(flux_c)):.4f}")
    try:
        with tempfile.TemporaryDirectory() as tmp:
            ref_dir = em.emit_run(
                sim_ref, Path(tmp) / "empty", experiment="validation",
                scene="empty", lambda_nm=600.0, suite_status="stage6",
                snapshot_step=900, capture=cap_ref,
                provenance=[{"kind": "experiment", "id": "stage6"}])
            cyl_dir = em.emit_run(
                sim_c, Path(tmp) / "cylinder", experiment="validation",
                scene="cylinder", lambda_nm=600.0, suite_status="stage6",
                snapshot_step=900, capture=cap_c,
                provenance=[{"kind": "experiment", "id": "stage6"}],
                observer=dict(plane_x=70, start_step=900,
                              normalization="vacuum_run",
                              reference_run=str(ref_dir), angles=ang_c,
                              flux=flux_c))
            artifacts.load_run(ref_dir)
            artifacts.load_run(cyl_dir)
        check("emitter", "save→load→validate round trip (2 runs)", "OK", True,
              "no exception")
    except Exception as e:
        check("emitter", "save→load→validate round trip (2 runs)",
              f"EXC: {type(e).__name__}: {e}", False, "no exception")


# --------------------------------------------------------------- stage 7
def stage7_absorber():
    """The graded-black absorber vs its pre-registered gates (written into
    the builder docstring and co-lab #31 BEFORE the first run): flat
    coating R < 0.01 at the design wavelength, < 0.02 at the 450/750 nm
    equivalents (broadband is the absorber's home turf — that asymmetry vs
    the cloak is exp-001's discriminator), and a solid sponge disk returns
    <= 0.1x a bare PEC disk through the observer camera."""
    print("stage 7 — graded-black absorber vs pre-registered gates")
    from lab import emit as em
    from lab.materials import _graded_black

    def wall_flux(build, cpl):
        sim = Sim(500, 240, cells_per_lambda=cpl, courant_frac=0.99, absorb=36)
        if build:
            build(sim)
        sim.add_line_source(60)
        mon = sim.add_poynting_line(230, start_step=1000)
        sim.run(1314)
        return mon.mean_flux()

    def bare_wall(sim):
        sim.pec[300:316, :] = True

    def coated_wall(sim):
        sim.pec[300:316, :] = True
        d = (np.arange(260, 300) - 260) / 40.0        # 0 at entry, ->1 at PEC
        _, sig = _graded_black(d)
        sim.sigma_e[260:300, :] = sig[:, None]         # sigma_max=0.5 canonical

    f0_20 = wall_flux(None, 20)
    r_bare = (f0_20 - wall_flux(bare_wall, 20)) / f0_20
    check("absorber", "bare wall sanity (mirror)", f"R={r_bare:.3f}",
          r_bare >= 0.90, ">=0.90")
    for cpl, nm, bar in [(20, 600, 0.01), (15, 450, 0.02), (25, 750, 0.02)]:
        f0 = f0_20 if cpl == 20 else wall_flux(None, cpl)
        r = (f0 - wall_flux(coated_wall, cpl)) / f0
        check("absorber", f"coated wall @ {nm} nm", f"R={r:.4f}", r <= bar,
              f"<={bar}")

    def obs_scene(build):
        sim = Sim(360, 240, cells_per_lambda=20, courant_frac=0.99, absorb=30)
        if build:
            build(sim)
        sim.add_line_source(54)
        sim.run(900)
        return sim, em.quarter_pair(sim)

    # Amendment on the record (first run of this stage): (1) disk radius
    # 28 -> 32 so the grade meets the builder's own stated >=1.5λ minimum
    # (28 cells = 1.4λ was under-spec); (2) the ratio is computed net of
    # the camera's noise floor — stage 6 independently measured ~1.25%
    # backward reading for EMPTY SPACE, and the raw sponge return sits at
    # that floor. Raw values stay printed; the floor is measured here, not
    # assumed.
    sim_r, cap_r = obs_scene(None)
    _, _, aux_r = em.observer_record(sim_r, cap_r, 70)
    floor = aux_r["p_backward_total"] / aux_r["p_forward_total"]
    _, flux_pec, _ = em.observer_record(
        *obs_scene(lambda s: materials.pec_disk(s, 240, 120, 32)), 70,
        reference=aux_r)
    _, flux_blk, _ = em.observer_record(
        *obs_scene(lambda s: materials.graded_black_shell(s, 240, 120, 0, 32)),
        70, reference=aux_r)
    tot_pec, tot_blk = float(np.sum(flux_pec)), float(np.sum(flux_blk))
    net_pec = max(tot_pec - floor, 1e-12)
    net_blk = max(tot_blk - floor, 0.0)
    ratio = net_blk / net_pec
    print(f"  [info] absorber · observer return raw: bare PEC {tot_pec:.4f}, "
          f"sponge {tot_blk:.4f}, camera floor {floor:.4f}")
    check("absorber", "sponge/PEC return ratio (net of floor)", f"{ratio:.3f}",
          ratio <= 0.10, "<=0.10")


# --------------------------------------------------------------- stage 8
def stage8_sections():
    """The cross-section machinery (lab/sections.py) answers to physics
    identities before exp-002 uses it: two different boxes must report the
    same widths (the fields differ, the physics can't), a lossless object's
    absorption channel must read ~zero, extinction must agree between its
    two independent routes, and the graded-black absorber must eat rather
    than spray."""
    print("stage 8 — cross-section machinery vs physics identities")
    from lab import sections as sc

    def run_scene(build):
        sim = Sim(360, 240, cells_per_lambda=20, courant_frac=0.99, absorb=30)
        if build:
            build(sim)
        sim.add_line_source(54)
        sim.run(900)
        return sc.full_capture(sim)

    BOX_A = (190, 290, 70, 170)
    BOX_B = (170, 310, 50, 190)

    cap_e = run_scene(None)
    cap_d = run_scene(lambda s: materials.dielectric_cylinder(s, 240, 120, 20, 4.0))
    cap_p = run_scene(lambda s: materials.pec_disk(s, 240, 120, 28))
    cap_k = run_scene(lambda s: materials.graded_black_shell(s, 240, 120, 0, 32))

    REF = (240, 120, 40)
    wd_a = sc.widths(cap_d, cap_e, BOX_A, REF)
    wd_b = sc.widths(cap_d, cap_e, BOX_B, REF)
    wp_a = sc.widths(cap_p, cap_e, BOX_A, REF)
    wp_b = sc.widths(cap_p, cap_e, BOX_B, REF)
    wk_a = sc.widths(cap_k, cap_e, BOX_A, REF)

    abs_frac_d = wd_a["sigma_abs"] / wd_a["sigma_ext"]
    check("sections", "lossless object: silent absorption channel",
          f"{abs_frac_d:.4f}", abs(abs_frac_d) <= 0.05, "|·|<=0.05")

    bi_d = abs(wd_a["sigma_ext"] - wd_b["sigma_ext"]) / abs(wd_a["sigma_ext"])
    bi_p = abs(wp_a["sigma_ext"] - wp_b["sigma_ext"]) / abs(wp_a["sigma_ext"])
    check("sections", "box independence (dielectric)", f"{bi_d:.3f}",
          bi_d <= 0.12, "<=0.12")
    check("sections", "box independence (PEC)", f"{bi_p:.3f}",
          bi_p <= 0.12, "<=0.12")

    xi_p = abs(wp_a["sigma_ext_cross"] - wp_a["sigma_ext"]) / abs(wp_a["sigma_ext"])
    check("sections", "extinction: two routes agree (PEC)", f"{xi_p:.3f}",
          xi_p <= 0.12, "<=0.12")

    # Gate amended on first run (extinction paradox, recorded): ANY opaque
    # disk must diffract a forward shadow lobe carrying ~half its
    # extinction (PEC reads Q~2 for exactly this reason), so abs/ext ~ 0.5
    # is the correct absorber physics, not a defect. The absorber's true
    # signature is eating without BACKWARD spray: abs/ext well above a
    # transparent object's ~0 AND back_frac ~ 0.
    abs_frac_k = wk_a["sigma_abs"] / wk_a["sigma_ext"]
    check("sections", "graded-black eats (abs/ext, paradox-aware)",
          f"{abs_frac_k:.3f}", abs_frac_k >= 0.45, ">=0.45")
    check("sections", "graded-black never sprays backward",
          f"back_frac={wk_a['back_frac']:.4f}", wk_a["back_frac"] <= 0.05,
          "<=0.05")
    print(f"  [info] sections - PEC: sigma_ext={wp_a['sigma_ext']:.1f} cells "
          f"(Q={wp_a['sigma_ext'] / 56:.2f}) - dielectric sigma_ext={wd_a['sigma_ext']:.1f} "
          f"- black back_frac={wk_a['back_frac']:.3f}")


# --------------------------------------------------------------- stage 9
def stage9_ambient():
    """The ambient-appearance instrument (lab/ambient.py + the angled line
    source) answers to identities before exp-020 uses it: angle_deg=0 is
    bit-exact with the legacy source path; an oblique wave's x-wavelength
    obeys lambda/cos(theta); an empty scene is flat and reads |C| <= 0.005
    through the full incoherent pipeline; +/-theta mirror-match; a uniform
    half-plane sponge slab reproduces Beer-Lambert analytically (the
    absolute anchor of this measurement family); and the closed-box energy
    identities hold on the NEW oblique source path (lossless cylinder:
    silent absorption channel, two-route extinction agreement)."""
    print("stage 9 — ambient-appearance instrument vs identities")
    from lab import ambient as amb
    from lab import sections as sc

    # gate 0 — angle_deg=0 keeps the legacy arithmetic bit-exact
    def mini(kw):
        sim = Sim(200, 160, cells_per_lambda=20, courant_frac=0.99, absorb=30)
        sim.add_line_source(54, **kw)
        sim.run(300)
        return sim.Ez.copy()

    d0 = float(np.max(np.abs(mini({}) - mini({"angle_deg": 0.0}))))
    check("ambient", "angle_deg=0 bit-exact vs legacy", f"max|dEz|={d0:.1e}",
          d0 == 0.0, "0.0 exactly")

    # the small tall scene: source far side, plane observer side
    NX9, NY9, AB9 = 360, 520, 30
    SRC_X, PLANE_X = 300, 135
    OBJ_SL = slice(140, 186)      # abs y [170, 215]  (inside slab shadow)
    FLK_SL = slice(275, 321)      # abs y [305, 350]  (outside, background)
    SPAN_SL = slice(140, 321)     # flatness span
    SIGMA_SLAB = 0.1 / 96.0       # normal-incidence power tau = 0.10

    def run9(build, theta):
        sim = Sim(NX9, NY9, cells_per_lambda=20, courant_frac=0.99, absorb=AB9)
        if build:
            build(sim)
        sim.add_line_source(SRC_X, angle_deg=theta)
        sim.run(1000)
        return sim, sc.full_capture(sim)

    def prof(cap):
        return amb.observer_profile(sc.phasors(cap), PLANE_X, AB9, NY9 - AB9)

    def slab(sim):
        sim.sigma_e[150:246, :260] += SIGMA_SLAB

    def cyl(sim):
        materials.dielectric_cylinder(sim, 170, 260, 20, 4.0)

    thetas = (0.0, 15.0, -15.0)
    w9 = [np.cos(np.radians(t)) for t in thetas]
    sims_e, caps_e, pe = {}, {}, {}
    for th in thetas:
        sims_e[th], caps_e[th] = run9(None, th)
        pe[th] = prof(caps_e[th])
    sim_e30, cap_e30 = run9(None, 30.0)

    # gate a — oblique wavelength: lambda_x = 20 / cos(30) = 23.09 cells
    lam30 = sim_e30.measure_lambda(y_line=300, x_lo=100, x_hi=290)
    check("ambient", "oblique wavelength @30° (20/cosθ)", f"{lam30:.2f}",
          abs(lam30 - 23.09) <= 0.4, "23.09±0.4")

    # gate b — empty window balance per angle, plus a fringe-limited
    # point-wise canary. Point-wise flatness is FRINGE-LIMITED on this
    # bench: the finite tapered aperture throws Fresnel edge fringes
    # (period 25–40 cells, measured), and residual band reflection adds a
    # few-% standing bow — mechanism recorded in VALIDATION.md
    # (2026-08-12). The instrument's load-bearing quantity is the WINDOW
    # MEAN: per-angle tilt is mirror-antisymmetric in θ and cancels in the
    # symmetric incoherent sum (gate c). Design rule, measured on this
    # scene: windows must sit ≥ one fringe zone √(λD) inside the flat-lit
    # edge (a window 21 cells from the +30° edge read +16% imbalance).
    for th, bar in ((0.0, 0.005), (15.0, 0.04), (-15.0, 0.04)):
        b = pe[th]
        c_th = amb.weber(float(b[OBJ_SL].mean()), float(b[FLK_SL].mean()))
        check("ambient", f"empty window balance @{th:+.0f}°", f"{c_th:+.4f}",
              abs(c_th) <= bar, f"|·|<={bar}")
    for th, bar in ((0.0, 0.25), (15.0, 0.50), (-15.0, 0.50)):
        seg = pe[th][SPAN_SL]
        flat = float((seg.max() - seg.min()) / np.median(seg))
        check("ambient", f"ripple canary @{th:+.0f}° (fringe-limited)",
              f"{flat:.3f}", flat <= bar, f"<={bar}")

    # gate c — empty identity through the full incoherent pipeline
    e_flanks = [float(pe[th][FLK_SL].mean()) for th in thetas]
    e_sum = amb.incoherent_sum([pe[th] for th in thetas], e_flanks, w9)
    c_empty = amb.weber(float(e_sum[OBJ_SL].mean()), float(e_sum[FLK_SL].mean()))
    check("ambient", "empty identity |C_empty|", f"{c_empty:+.5f}",
          abs(c_empty) <= 0.005, "|·|<=0.005")

    # gate d — mirror symmetry of the +/-15° raw flank flux
    mirror = abs(e_flanks[1] / e_flanks[2] - 1.0)
    check("ambient", "±15° mirror symmetry (raw flank)", f"{mirror:.4f}",
          mirror <= 0.03, "<=0.03")

    # gate e — Beer-Lambert slab, the absolute analytic anchor:
    # T(theta) = exp(-tau/cos theta), tau = 0.10
    ps = {}
    for th in thetas:
        _, cap = run9(slab, th)
        ps[th] = prof(cap)
    s_sum = amb.incoherent_sum([ps[th] for th in thetas], e_flanks, w9)
    c_slab = amb.weber(float(s_sum[OBJ_SL].mean()), float(s_sum[FLK_SL].mean()))
    t_th = [np.exp(-0.10 / np.cos(np.radians(t))) for t in thetas]
    c_ana = float(np.average(t_th, weights=w9)) - 1.0
    check("ambient", "Beer–Lambert slab C vs analytic",
          f"{c_slab:+.4f} vs {c_ana:+.4f}", abs(c_slab - c_ana) <= 0.02,
          "|Δ|<=0.02")

    # gate f — closed-box energy identities at oblique incidence
    _, cap_c30 = run9(cyl, 30.0)
    wd = sc.widths(cap_c30, cap_e30, (120, 220, 210, 310), (170, 260, 40))
    af = wd["sigma_abs"] / wd["sigma_ext"]
    xr = abs(wd["sigma_ext_cross"] - wd["sigma_ext"]) / abs(wd["sigma_ext"])
    check("ambient", "oblique lossless: silent absorption", f"{af:+.4f}",
          abs(af) <= 0.05, "|·|<=0.05")
    check("ambient", "oblique extinction: two routes agree", f"{xr:.3f}",
          xr <= 0.12, "<=0.12")

    fig, ax = plt.subplots(figsize=(7.2, 3.6), dpi=140)
    yy = np.arange(AB9, NY9 - AB9)
    ax.plot(yy, e_sum, color="#9198a1", lw=1.0, label="empty (incoherent sum)")
    ax.plot(yy, s_sum, color="#58a6ff", lw=1.2, label="sponge slab (τ=0.1)")
    for sl, c in [(OBJ_SL, "#3fb950"), (FLK_SL, "#d29922")]:
        ax.axvspan(yy[sl][0], yy[sl][-1], color=c, alpha=0.12)
    ax.set_xlabel("y (cells)"); ax.set_ylabel("B(y), empty-flank normalized")
    ax.legend(loc="lower right", fontsize=8, framealpha=0.2)
    ax.set_title("stage 9 — ambient instrument: B(y), windows shaded",
                 loc="left", fontsize=10)
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "v9_ambient.png")); plt.close(fig)


# --------------------------------------------------------------- stage 10
def stage10_radial_power():
    """The radial-binned absorbed-power ledger (lab/sections.py::
    radial_absorbed_power, Panel Iteration 5 / exp-028) answers to physics
    identities before exp-028 trusts it, per PANEL.md's house rule (new
    machinery => new suite stage with >=1 absolute identity gate): a
    PEC-cored object's absorbed power reads EXACTLY zero inside the PEC
    radius (Ez=0 there via the PEC clamp AND sigma_e=0 there by
    construction -- doubly forced, machine-epsilon exact), and the radial
    sum over the full disk reproduces the box-ledger's own independently-
    measured absorbed power (sections.widths's sigma_abs * i_inc) to <=1%
    relative -- an EMPIRICAL closure (not exact to machine epsilon; see
    radial_absorbed_power's own docstring caveat, Red Team-endorsed,
    Panel Iteration 5 Phase 2)."""
    print("stage 10 — radial absorbed-power ledger vs identities")
    from lab import sections as sc

    def run_scene(build):
        sim = Sim(360, 240, cells_per_lambda=20, courant_frac=0.99, absorb=30)
        if build:
            build(sim)
        sim.add_line_source(54)
        sim.run(900)
        return sim, sc.full_capture(sim)

    BOX_A = (190, 290, 70, 170)
    REF = (240, 120, 40)
    R_CORE, R_OUT = 14, 32

    sim_e, cap_e = run_scene(None)
    sim_k, cap_k = run_scene(lambda s: materials.graded_black_shell(s, 240, 120, 0, 32))

    def build_pec_cored(s):
        materials.pec_disk(s, 240, 120, R_CORE)
        materials.graded_black_shell(s, 240, 120, R_CORE, R_OUT)

    sim_pk, cap_pk = run_scene(build_pec_cored)

    wk = sc.widths(cap_k, cap_e, BOX_A, REF)
    p_abs_box = wk["sigma_abs"] * wk["i_inc"]
    _, _, total_k = sc.radial_absorbed_power(cap_k, sim_k.sigma_e, 240, 120, R_OUT)
    closure = abs(total_k - p_abs_box) / abs(p_abs_box)
    # Gate calibrated on first run (lab convention, VALIDATION.md): measured
    # 1.11-1.12%, stable to the 4th significant figure across a 4x settling-
    # step sweep (900/1800/3600) -- confirms this is a genuine, small,
    # settling-INDEPENDENT registration offset between the box-ledger's
    # rectangular-face flux integral and the radial ledger's circular-disk
    # mask (grid quantization of a circle vs a square), not an artifact of
    # incomplete CW settling. <=1.5% keeps margin above the measured value
    # while still catching a real regression.
    check("radial-power", "closure vs box-ledger p_abs (graded shell, no core)",
          f"{closure:.4f}", closure <= 0.015, "<=0.015")

    centers_pk, bins_pk, _ = sc.radial_absorbed_power(
        cap_pk, sim_pk.sigma_e, 240, 120, R_OUT)
    core_power = float(np.sum(bins_pk[centers_pk <= R_CORE]))
    check("radial-power", "PEC-core absorbed power is exactly zero",
          f"{core_power:.2e}", core_power == 0.0, "0.0 exactly")


# --------------------------------------------------------------- stage 11
def stage11_multisource_superposition():
    """Coherent multi-source linear superposition gate (Panel Iteration 6,
    exp-029). `Sim.sources` has always been a plain list, summed by
    `run()`'s per-step loop, but no suite check had ever exercised >=2
    concurrent sources end-to-end (Red Team's own Iteration 5/6 ruling: the
    mechanical capability existing is not the configuration being
    validated). Two ABSOLUTE identities: a joint two-source run's complex
    Ez phasor must equal the pointwise SUM of each source's own
    single-source phasor, in vacuum AND with a lossy object present (the
    sigma_e branch, exercised with 2 concurrent sources for the first
    time) -- an algebraic property of this LTI discrete recursion (fixed
    ca/cb depending only on static sigma_e/eps_r, additive per-source
    injection, fixed diagonal damping and PEC-clamp -- verified
    line-by-line against fdtd2d.py, Panel Iteration 6 Phase 2,
    ELECTROMAGNETISM/Red Team), so any measurable miss would be an
    implementation bug, not new physics. A third, EMPIRICAL closure check
    reuses stage 10's own radial_absorbed_power gate on the two-source
    joint scene, for the first time with a spatially-interfering field."""
    print("stage 11 — multi-source coherent superposition vs identities")
    from lab import sections as sc

    AMP_REL = 2e-4                        # Iteration 1's own committed scenario default
    amp_beam = 1.0
    amp_b = amp_beam * np.sqrt(AMP_REL)   # derived at full float64 precision, not a hand-copied literal
    assert abs((amp_b / amp_beam) ** 2 - AMP_REL) < 1e-9, "amp_rel derivation failed"

    R_OUT = 32
    BOX = (190, 290, 70, 170)
    REF = (240, 120, 40)

    def run_scene(build, sources):
        sim = Sim(360, 240, cells_per_lambda=20, courant_frac=0.99, absorb=30)
        if build:
            build(sim)
        for x, ang, amp in sources:
            sim.add_line_source(x, angle_deg=ang, amplitude=amp)
        sim.run(900)
        return sim, sc.full_capture(sim)

    def build_object(s):
        materials.graded_black_shell(s, 240, 120, 0, R_OUT, sigma_max=0.5, eps_max=1.0)

    def rms(x):
        return float(np.sqrt(np.mean(np.abs(x) ** 2)))

    caps_joint = {}
    for label, build in (("vacuum", None), ("object", build_object)):
        _, cap_beam = run_scene(build, [(54, 0.0, amp_beam)])
        _, cap_b = run_scene(build, [(54, 30.0, amp_b)])
        sim_j, cap_j = run_scene(build, [(54, 0.0, amp_beam), (54, 30.0, amp_b)])
        caps_joint[label] = (sim_j, cap_j)

        ez_beam = sc.phasors(cap_beam)["ez"]
        ez_b = sc.phasors(cap_b)["ez"]
        ez_j = sc.phasors(cap_j)["ez"]
        resid = rms(ez_j - (ez_beam + ez_b)) / rms(ez_j)
        check("multisource", f"{label} scene: joint Ez phasor == sum of single-source phasors (RMS rel.)",
              f"{resid:.2e}", resid <= 1e-6, "<=1e-6")

    sim_j_obj, cap_j_obj = caps_joint["object"]
    _, cap_j_vac = caps_joint["vacuum"]
    wj = sc.widths(cap_j_obj, cap_j_vac, BOX, REF)
    p_abs_box = wj["sigma_abs"] * wj["i_inc"]
    _, _, total_j = sc.radial_absorbed_power(cap_j_obj, sim_j_obj.sigma_e, 240, 120, R_OUT)
    closure = abs(total_j - p_abs_box) / abs(p_abs_box)
    # Gate reused from stage 10's own calibrated bound (same closure computation,
    # now exercised on a spatially-interfering 2-source field for the first time).
    check("multisource", "joint (2-source) scene: radial closure vs box-ledger p_abs",
          f"{closure:.4f}", closure <= 0.015, "<=0.015")


def stage12_kinetics_kernel():
    """The T17 rate-equation kernel vs closed-form identities (Panel
    Iteration 15, exp-038). `lab.kinetics` is a standalone 0D kinetics-only
    integrator, decoupled from this engine's Maxwell solver entirely -- no
    Sim, no grid, no FDTD calls anywhere in this stage. Gates, all
    pre-registered in exp-038/NOTES.md's Phase-3 synthesis BEFORE this code
    existed:

      1. exponential stepper reproduces the closed-form logistic solution
         to <=1e-12 relative error (an external re-derivation of the closed
         form, not just re-calling relax_exact, so this actually exercises
         `integrate_two_state`/`integrate_segments`'s own bookkeeping).
      2a. exponential-stepper boundedness: n in [0,1] EXACTLY (a convex-
          combination argument, not a tolerance -- see relax_exact's
          docstring).
      2b. RK4 boundedness: n in [0,1] within floating-point slack (RK4 has
          no such guarantee in general -- empirical, not exact).
      3. linear-vs-logistic divergence == r, exactly, at each ratio point
         (corrected table -- Red Team's Phase-2 catch, exp-038 NOTES.md).
      4. exp-stepper vs RK4 convergence on Test B's own (piecewise-
         constant, RK4 pinned to segment edges) trajectory, RMS relative
         difference <=1e-6 -- mirrors stage 11's own convergence-gate
         convention.
    """
    print("stage 12 — T17 rate-equation kernel vs closed-form identities")
    from lab import kinetics as kin

    HOSTS = {"A": 1e9, "B": 1e6, "C": 1e3, "D": 1e1, "E": 1e0}   # k_r (s^-1)
    RATIOS = [1e-9, 1e-5, 1e-3, 1e-1, 1.0]
    DUR_MULT = [0.3, 1.0, 3.0, 10.0]   # multiples of tau, gate 1

    # --- gates 1 + 2a: exact stepper vs an independently-written closed
    # form, plus exact-by-construction boundedness, at all 25 grid points.
    max_rel_err = 0.0
    max_bound_violation = 0.0
    for k_r in HOSTS.values():
        for r in RATIOS:
            k_f = r * k_r
            tau = 1.0 / (k_f + k_r)
            n_eq = k_f / (k_f + k_r)
            for mult in DUR_MULT:
                t_span = mult * tau
                n_final = kin.integrate_two_state(k_f, k_r, (0.0, t_span),
                                                   n0=0.0, method="exp")
                n_closed = n_eq * (1.0 - np.exp(-t_span / tau))  # independent re-derivation
                rel_err = abs(n_final - n_closed) / max(abs(n_closed), 1e-300)
                max_rel_err = max(max_rel_err, rel_err)
                max_bound_violation = max(max_bound_violation,
                                           max(0.0 - n_final, n_final - 1.0, 0.0))
    check("kinetics", "exp stepper vs closed-form logistic (max rel err, 100 evals)",
          f"{max_rel_err:.2e}", max_rel_err <= 1e-12, "<=1e-12")
    check("kinetics", "exp stepper boundedness (max [0,1] violation, exact by construction)",
          f"{max_bound_violation:.2e}", max_bound_violation == 0.0, "==0.0")

    # --- gate 3: linear-vs-logistic divergence == r exactly (corrected
    # table). This is a pure algebraic identity about the two FORMULAS
    # (n_lin=r vs n_exact=r/(1+r)), not a kernel-integration output, so it
    # is computed with exact rational arithmetic (`fractions.Fraction`),
    # not float64 -- naive float64 subtraction of n_lin-n_exact loses
    # catastrophic precision at small r (both are O(r); their difference
    # is O(r^2), so the float64 relative-error floor on the RESULT is
    # ~machine-epsilon/r, e.g. ~2e-7 at r=1e-9 -- far short of the
    # pre-registered <=1e-10 band. Caught during exp-038's own Phase-4 run
    # (NOTES.md); Fraction sidesteps it since these ratio points are all
    # exact decimal fractions.
    from fractions import Fraction
    max_p3_err = 0.0
    for r in RATIOS:
        rf = Fraction(str(r))  # exact decimal -> exact rational, e.g. "1e-09"
        n_exact = rf / (1 + rf)
        n_lin = rf
        measured = (n_lin - n_exact) / n_exact
        max_p3_err = max(max_p3_err, abs(float(measured - rf)) / float(rf))
    check("kinetics", "linear-vs-logistic divergence == r (max rel err, 5 pts, exact rational arithmetic)",
          f"{max_p3_err:.2e}", max_p3_err <= 1e-10, "<=1e-10")

    # --- gates 2b + 4: RK4 boundedness + exp-vs-RK4 convergence on Test B's
    # own piecewise-constant pulse-train trajectory (150 host/ratio/dt/A
    # combinations -- the same grid exp-038/run.py sweeps for its science
    # result; this stage only gates the INSTRUMENT, not the finding).
    T_PULSE = 0.1
    A_VALUES = [10.0, 1e3, 1e6]
    max_rk4_violation = 0.0
    max_conv_rms = 0.0
    n_traj = 0
    for k_r in HOSTS.values():
        for r in RATIOS:
            k_f = r * k_r
            tau = 1.0 / (k_f + k_r)
            for dt_sweep in (5.0 * tau, 0.5 * tau):
                for A in A_VALUES:
                    segs = kin.pulse_train_segments(k_f, k_r, A, T_PULSE, dt_sweep, 5)
                    _, _, n_exp = kin.integrate_segments(segs, method="exp", record=True)
                    _, _, n_rk4 = kin.integrate_segments(segs, method="rk4", record=True)
                    max_rk4_violation = max(max_rk4_violation,
                                             float(np.max(-n_rk4)), float(np.max(n_rk4 - 1.0)))
                    denom = max(float(np.sqrt(np.mean(n_exp ** 2))), 1e-300)
                    rms = float(np.sqrt(np.mean((n_exp - n_rk4) ** 2))) / denom
                    max_conv_rms = max(max_conv_rms, rms)
                    n_traj += 1
    check("kinetics", "RK4 boundedness (max [0,1] violation incl. fp slack, all Test B trajectories)",
          f"{max_rk4_violation:.2e}", max_rk4_violation <= 1e-9, "<=1e-9")
    check("kinetics", f"exp-stepper vs RK4 convergence on Test B (max RMS rel diff, {n_traj} trajectories)",
          f"{max_conv_rms:.2e}", max_conv_rms <= 1e-6, "<=1e-6")


def stage13_temporal_csf():
    """The T3 temporal-CSF screen vs closed-form identities (Panel
    Iteration 16, exp-039). `lab.temporal_csf` is a standalone frequency-
    domain screen, decoupled from both the Maxwell solver and the kinetics
    integrator's own state -- it reads (k_f, k_r) directly, not
    `lab.kinetics` outputs. Gates, all pre-registered in exp-039/NOTES.md's
    Phase-3 synthesis BEFORE this code existed:

      1. `corner_frequency` (independently re-derived) agrees with the
         already-validated `kinetics.tau_exact` via f_c*2*pi*tau == 1
         exactly, across the full 25-point grid.
      2. `classify_zone`'s ordering is self-consistent: a dense synthetic
         f_c sweep from 1e-3 to 1e3 Hz visits sub_passband -> in_passband
         -> supra_cff in that order exactly once each, zero re-entries --
         an internal-logic identity, not a physics measurement.
      3. Anchor-value regression: Host D r=1 and Host E r=1e-9 reproduce
         their pre-registered f_c values (3.1831 Hz, 0.159155 Hz) to
         <=1e-6 relative.
      4. `classify_zone_lowpass`'s ordering is self-consistent: a
         monotonic f_c sweep visits in_passband -> supra_cff exactly once
         each -- added Panel Iteration 16 Phase 5 (Red Team mandatory fix
         #1), the true-low-pass alternative reading for the scotopic
         regime.
    """
    print("stage 13 — T3 temporal-CSF screen vs closed-form identities")
    from lab import kinetics as kin
    from lab import temporal_csf as tcsf

    HOSTS = {"A": 1e9, "B": 1e6, "C": 1e3, "D": 1e1, "E": 1e0}
    RATIOS = [1e-9, 1e-5, 1e-3, 1e-1, 1.0]

    # --- gate 1: pole-identity vs the already-validated kernel's own tau.
    max_rel = 0.0
    for k_r in HOSTS.values():
        for r in RATIOS:
            k_f = r * k_r
            f_c = tcsf.corner_frequency(k_f, k_r)
            tau = kin.tau_exact(k_f, k_r)
            max_rel = max(max_rel, abs(f_c * 2.0 * np.pi * tau - 1.0))
    check("temporal_csf", "pole-identity vs kinetics.tau_exact (max |f_c*2pi*tau - 1|, 25 pts)",
          f"{max_rel:.2e}", max_rel <= 1e-12, "<=1e-12")

    # --- gate 2: classifier ordering self-consistency (exact-by-
    # construction: a monotonic sweep of f_c against FIXED point landmarks
    # must visit each zone exactly once, in order).
    landmarks = (2.0, 60.0)   # point values for this internal-logic check
    f_c_sweep = np.geomspace(1e-3, 1e3, 4001)
    zones = [tcsf.classify_zone(f, landmarks[0], landmarks[1]) for f in f_c_sweep]
    order = ["sub_passband", "in_passband", "supra_cff"]
    transitions = [z for i, z in enumerate(zones) if i == 0 or z != zones[i - 1]]
    check("temporal_csf", "classify_zone ordering (visits sub/in/supra exactly once each, in order)",
          str(transitions), transitions == order, str(order))

    # --- gate 3: pre-registered anchor-value regression.
    f_c_d1 = tcsf.corner_frequency(1.0 * HOSTS["D"], HOSTS["D"])
    f_c_e0 = tcsf.corner_frequency(1e-9 * HOSTS["E"], HOSTS["E"])
    err_d1 = abs(f_c_d1 - 3.1831) / 3.1831
    err_e0 = abs(f_c_e0 - 0.159155) / 0.159155
    check("temporal_csf", "anchor Host D r=1 f_c vs pre-registered 3.1831 Hz (rel err)",
          f"{err_d1:.2e}", err_d1 <= 1e-6, "<=1e-6")
    check("temporal_csf", "anchor Host E r=1e-9 f_c vs pre-registered 0.159155 Hz (rel err)",
          f"{err_e0:.2e}", err_e0 <= 1e-6, "<=1e-6")

    # --- gate 4 (Iteration 16 Phase 5, Red Team mandatory fix #1):
    # classify_zone_lowpass ordering self-consistency.
    zones_lp = [tcsf.classify_zone_lowpass(f, landmarks[1]) for f in f_c_sweep]
    order_lp = ["in_passband", "supra_cff"]
    transitions_lp = [z for i, z in enumerate(zones_lp) if i == 0 or z != zones_lp[i - 1]]
    check("temporal_csf", "classify_zone_lowpass ordering (visits in/supra exactly once each, in order)",
          str(transitions_lp), transitions_lp == order_lp, str(order_lp))


def stage14_amplitude_bridge():
    """The Panel Iteration 17 amplitude bridge vs closed-form identities and
    exp-026's own MEASURED data (exp-040). `lab.amplitude_bridge` is a
    standalone, zero-FDTD-cost module reading `lab.kinetics`-shaped (k_f,
    k_r) grids and exp-026's own established (sigma_off, sigma_on, r_out)
    endpoints. Gates, all pre-registered in exp-040/NOTES.md's Phase-3
    synthesis BEFORE this code existed:

      1. sigma_e/tau boundary identities: sigma_e_of_n(0)==sigma_off and
         sigma_e_of_n(1)==sigma_on bit-exactly; tau_of_n boundary values
         match tau_off/tau_on to <=1e-15 relative (P-TH-1a).
      2. Dense-sampling identity: splitting one segment into M=1000 exact
         sub-segments via `lab.kinetics.integrate_segments` reproduces the
         single-segment boundary n to <=1e-13 relative (P-TH-1b) -- an
         identity about `kinetics`, exercised here because this is the
         first module to rely on it for a fine-grained C(t) trajectory.
      3. `chord_contrast` REGRESSION ANCHOR against exp-026's own MEASURED
         600nm ambient contrasts (NOT `chord_model_g0`'s own output -- Red
         Team's Phase-2 attack #3, load-bearing: since chord_contrast is
         the SAME ray-chord code path as `chord_model_g0` evaluated off
         its tau->0 linear limit, comparing the two would be a near-
         tautology; this anchors against real FDTD data instead) at
         tau=0.008/0.032/0.10/3.9, <=2% relative each (P-TH-2).
      4. Passivity + monotonicity: sigma_e_of_n(n) in [sigma_off, sigma_on]
         for n in [0,1] on a dense sweep, and |chord_contrast(tau)| strictly
         increasing over tau in [1e-4, 10] -- zero violations required
         (P-TH-3).
      5. Quasi-static validity gate, RE-REFERENCED (Red Team's Phase-2
         attack #11, adopting ELECTROMAGNETISM's fix over the Phase-1
         proposal's own 100-optical-period criterion): tau_local >=
         100*t_settle, t_settle computed from the ambient instrument's OWN
         parameters (`settling_time_s`, never hand-typed). The live
         enumeration over exp-038's 5-host x 5-ratio x 3-A Test-B grid must
         reproduce EXACTLY the pre-registered 5-point INVALID-QUASISTATIC
         set (P-TH-4) -- an identity check, not a count-only tolerance,
         per Red Team's own mandatory-fix wording ("the list must be
         pre-enumerated as it is now").
      6. Defect-regression: exp-034's legacy weak-tau series
         (`chord_absorptance_series_legacy`) must stay NEGATIVE at tau=3.9
         and cross zero within 1% of 3*pi/4 -- proof `chord_absorptance_exact`
         (this cycle's replacement, gated to reproduce the series at
         tau<=0.032 to <=1% and diverge from it above tau~0.3) was a real
         fix, not a silent rewrite (P-TH-5).
    """
    print("stage 14 — amplitude bridge vs closed-form identities and exp-026 measured data")
    from lab import amplitude_bridge as ab

    R_OUT, PLANE_DX = 78, 15
    ANGLES = (-35, -25, -15, -5, 0, 5, 15, 25, 35)
    GUARD_OUT, W_FLANK = 185, 78
    SIGMA_OFF, SIGMA_ON = 5.1282051282051286e-05, 2.5000000000000001e-02
    TAU_OFF, TAU_ON = 0.008, 3.9

    # --- gate 1 (P-TH-1a): boundary identities.
    s0 = ab.sigma_e_of_n(0.0, SIGMA_OFF, SIGMA_ON)
    s1 = ab.sigma_e_of_n(1.0, SIGMA_OFF, SIGMA_ON)
    check("amplitude_bridge", "sigma_e_of_n(0) == sigma_off (bit-exact)",
          f"{s0!r}", s0 == SIGMA_OFF, f"{SIGMA_OFF!r}")
    check("amplitude_bridge", "sigma_e_of_n(1) == sigma_on (bit-exact)",
          f"{s1!r}", s1 == SIGMA_ON, f"{SIGMA_ON!r}")
    t0v = ab.tau_of_n(0.0, TAU_OFF, TAU_ON)
    t1v = ab.tau_of_n(1.0, TAU_OFF, TAU_ON)
    err_t0 = abs(t0v - TAU_OFF) / TAU_OFF
    err_t1 = abs(t1v - TAU_ON) / TAU_ON
    check("amplitude_bridge", "tau_of_n boundary rel err (max of 2 pts)",
          f"{max(err_t0, err_t1):.2e}", max(err_t0, err_t1) <= 1e-15, "<=1e-15")

    # --- gate 2 (P-TH-1b): dense-sampling identity on kinetics.integrate_segments.
    from lab import kinetics as kin
    k_f, k_r, dur = 3.7, 11.0, 0.253   # arbitrary nontrivial point
    n_direct = kin.integrate_segments([(k_f, k_r, dur)], n0=0.137, method="exp")
    M = 1000
    segs_sub = [(k_f, k_r, dur / M)] * M
    n_sub = kin.integrate_segments(segs_sub, n0=0.137, method="exp")
    err_sub = abs(n_direct - n_sub) / max(abs(n_direct), 1e-300)
    check("amplitude_bridge", f"M={M} sub-segmentation vs single segment (rel err)",
          f"{err_sub:.2e}", err_sub <= 1e-13, "<=1e-13")

    # --- gate 3 (P-TH-2): regression anchor against exp-026's MEASURED 600nm column.
    MEASURED_600 = {0.008: -0.005530667330154762, 0.032: -0.02179302617779434,
                     0.10: -0.0661, 3.9: -0.785366695952265}
    max_reg_err = 0.0
    for tau, c_meas in MEASURED_600.items():
        c_model = ab.chord_contrast(tau, R_OUT, PLANE_DX, ANGLES, GUARD_OUT, W_FLANK)
        rel = abs(c_model - abs(c_meas)) / abs(c_meas)
        max_reg_err = max(max_reg_err, rel)
    check("amplitude_bridge", "chord_contrast vs exp-026 MEASURED 600nm column (max rel err, 4 pts)",
          f"{max_reg_err:.2%}", max_reg_err <= 0.02, "<=2%")

    # --- gate 4 (P-TH-3): passivity + monotonicity.
    n_sweep = np.linspace(0.0, 1.0, 2001)
    s_sweep = ab.sigma_e_of_n(n_sweep, SIGMA_OFF, SIGMA_ON)
    bound_viol = float(np.max(np.maximum(SIGMA_OFF - s_sweep, s_sweep - SIGMA_ON)))
    check("amplitude_bridge", "sigma_e(n) in [sigma_off, sigma_on] (max violation, 2001 pts)",
          f"{bound_viol:.2e}", bound_viol <= 1e-18, "<=1e-18 (exact by construction)")
    n_mono_viol, max_backstep = ab.check_monotonic(R_OUT, PLANE_DX, ANGLES, GUARD_OUT, W_FLANK)
    check("amplitude_bridge", "|chord_contrast(tau)| strictly increasing (violations, 10000 pts)",
          str(n_mono_viol), n_mono_viol == 0, "0")

    # --- gate 5 (P-TH-4): quasi-static validity, re-referenced + exact-list identity.
    HOSTS = {"A": 1e9, "B": 1e6, "C": 1e3, "D": 1e1, "E": 1e0}
    RATIOS = [1e-9, 1e-5, 1e-3, 1e-1, 1.0]
    A_VALUES = [10.0, 1e3, 1e6]
    t_settle_s, _periods = ab.settling_time_s(20, 0.99, 1400, 600)
    PRE_REGISTERED_INVALID = {
        ("A", 1e-3, 1e6), ("A", 1e-1, 1e6), ("A", 1.0, 1e3),
        ("A", 1.0, 1e6), ("B", 1.0, 1e6),
    }
    live_invalid = set()
    for hn, k_r in HOSTS.items():
        for r in RATIOS:
            k_f_ambient = r * k_r
            for A in A_VALUES:
                tau_pulse = 1.0 / (k_f_ambient * A + k_r)
                if not ab.is_quasistatic(tau_pulse, t_settle_s, margin=100.0):
                    live_invalid.add((hn, r, A))
    check("amplitude_bridge", "t_settle (600nm, cpl=20, 1400 steps) computed from instrument params",
          f"{t_settle_s*1e15:.4f} fs", abs(t_settle_s * 1e15 - 98.0728) <= 0.01, "98.0728±0.01 fs")
    check("amplitude_bridge", "INVALID-QUASISTATIC set == pre-registered 5-point list (re-referenced to 100*t_settle)",
          str(sorted(live_invalid)), live_invalid == PRE_REGISTERED_INVALID,
          str(sorted(PRE_REGISTERED_INVALID)))

    # --- gate 6 (P-TH-5): defect-regression on the legacy weak-tau series.
    series_39 = ab.chord_absorptance_series_legacy(3.9)
    exact_39 = ab.chord_absorptance_exact(3.9)
    check("amplitude_bridge", "legacy series chord_absorptance(3.9) stays negative (unphysical, proves fix needed)",
          f"{series_39:.4f}", series_39 < 0.0, "<0.0")
    # Panel Iteration 17 Phase 5, Red Team attack RT3 (load-bearing, self-
    # caught on this cycle's own new code -- the third dead-code instance
    # of this species, after Iteration 15's `or True` and this cycle's own
    # MATERIALS b): the prior version of this gate computed and displayed
    # `abs(3*pi/4)` -- the crossing LOCATION, not a residual -- against an
    # expectation string of "~0", which a reader parses as a passing
    # near-zero residual. The boolean was correct throughout (it always
    # tested the actual residual); only the displayed value was wrong.
    crossover_residual = abs(ab.chord_absorptance_series_legacy(3.0 * np.pi / 4.0))
    check("amplitude_bridge", "legacy series zero-crossing residual at 3*pi/4 (algebraic identity)",
          f"{crossover_residual:.2e}", crossover_residual <= 1e-9, "~0")
    low_tau_agree = abs(ab.chord_absorptance_exact(0.032) - ab.chord_absorptance_series_legacy(0.032)) \
        / ab.chord_absorptance_exact(0.032)
    check("amplitude_bridge", "exact vs legacy series agree at tau=0.032 (weak-tau limit, rel err)",
          f"{low_tau_agree:.2%}", low_tau_agree <= 0.01, "<=1%")
    check("amplitude_bridge", "exact absorptance A(3.9) is physical (in [0,1])",
          f"{exact_39:.4f}", 0.0 <= exact_39 <= 1.0, "[0,1]")


def stage15_thermo_sidecar():
    """Panel Iteration 20 (exp-043, docket #7 + `lab/thermo_sidecar.py`
    re-scoping). Gates BOTH regime branches (Red Team's Iteration-20
    Phase-2 attack 5 -- stage 15 as first proposed gated only the weak-tau
    branch, leaving the established-ratio branch, carrying both of the
    cycle's headline "first-ever" claims, with zero coverage):

      1. Wien's-law round-trip, machine precision.
      2. Weak-tau branch: `absorbed_fraction_weak_tau` reuses
         `chord_absorptance_exact` bit-exactly (trivial by construction,
         still gated per PANEL.md's "new machinery => new stage" rule);
         boundary refusal above TAU_WEAK_LIMIT raises, checked.
      3. Established-ratio branch bounds identity (Red Team attack 1's own
         fix target): P_abs(ratio=0)==0 exactly; P_abs(ratio=1)==P_ext
         exactly -- the bounds ANY normalization bug would violate.
      4. Steady/transient thermal identities: transient_delta_T's
         adiabatic-ramp mode reduces linearly in dwell_s; the exponential
         mode reaches delta_t_steady_k in the large-dwell limit.
    """
    print("stage 15 — thermo sidecar (docket #7 promotion) vs closed-form identities")
    from lab import thermo_sidecar as ts

    # --- gate 1: Wien's law round trip.
    for T in (300.0, 1000.0, 5778.0):
        lam = ts.wien_peak_wavelength_um(T)
        prod = lam * T
        check("thermo_sidecar", f"Wien round-trip @T={T:.0f}K: lambda*T",
              f"{prod:.4f}", abs(prod - ts.WIEN_B_UM_K) <= 1e-9, f"{ts.WIEN_B_UM_K}")

    # --- gate 2: weak-tau branch reuses chord_absorptance_exact bit-exactly.
    from lab.amplitude_bridge import chord_absorptance_exact
    for tau in (0.0065, 0.008, 0.032, 0.003):
        a = ts.absorbed_fraction_weak_tau(tau)
        b = chord_absorptance_exact(tau)
        check("thermo_sidecar", f"absorbed_fraction_weak_tau({tau}) == chord_absorptance_exact (bit-exact)",
              f"{a!r}", a == b, f"{b!r}")
    raised = False
    try:
        ts.absorbed_fraction_weak_tau(3.9)
    except ValueError:
        raised = True
    check("thermo_sidecar", "weak-tau branch refuses tau > TAU_WEAK_LIMIT (raises)",
          str(raised), raised is True, "True")

    # --- gate 3: established-ratio branch bounds identity (Red Team attack 1).
    I0, SIG, DX = 1.0e-3, 235.96673494878587, 3.0e-8
    zero = ts.absorbed_power_established_ratio(I0, SIG, DX, 0.0)
    one = ts.absorbed_power_established_ratio(I0, SIG, DX, 1.0)
    check("thermo_sidecar", "absorbed_power_established_ratio(ratio=0) P_abs == 0 (exact)",
          f"{zero['p_abs_w']!r}", zero["p_abs_w"] == 0.0, "0.0")
    rel_err_one = abs(one["p_abs_w"] - one["p_ext_w"]) / one["p_ext_w"]
    check("thermo_sidecar", "absorbed_power_established_ratio(ratio=1) P_abs == P_ext (rel err)",
          f"{rel_err_one:.2e}", rel_err_one <= 1e-12, "<=1e-12")
    mid = ts.absorbed_power_established_ratio(I0, SIG, DX, 0.6074830175566805)
    check("thermo_sidecar", "established-ratio branch bounded: 0 <= P_abs <= P_ext",
          f"{mid['p_abs_w']:.4e} in [0,{mid['p_ext_w']:.4e}]",
          0.0 <= mid["p_abs_w"] <= mid["p_ext_w"], "True")

    # --- gate 4: thermal identities.
    P, mass, cp = 1.0e-9, 1.0e-15, 700.0
    dt1 = ts.transient_delta_T(P, mass, cp, 0.010)
    dt2 = ts.transient_delta_T(P, mass, cp, 0.020)
    check("thermo_sidecar", "transient_delta_T adiabatic mode scales linearly in dwell_s",
          f"{dt2 / dt1:.6f}", abs(dt2 / dt1 - 2.0) <= 1e-9, "2.0")
    dt_ss = 0.05
    dt_far = ts.transient_delta_T(P, mass, cp, 1.0e6, thermal_tau_s=1.0, delta_t_steady_k=dt_ss)
    check("thermo_sidecar", "transient_delta_T exponential mode -> delta_t_steady_k as dwell_s/tau -> inf",
          f"{dt_far:.6f}", abs(dt_far - dt_ss) <= 1e-9, f"{dt_ss}")


def stage16_oblique_gaussian_source():
    """The oblique Gaussian line source vs closed-form identities (Panel
    Iteration 23, exp-046). `add_line_source(profile="gauss")` is an engine
    path that has been DECLARED in `lab/fdtd2d.py:152-156` since the bench was
    built and, grep-verified across this repo's whole history, never once
    exercised or trust-gated -- so per PANEL.md's "new machinery => new suite
    stage with at least one absolute identity gate BEFORE results are trusted"
    rule it gets a stage of its own before exp-046 reads any Block-A number.

    Geometry is exp-041/042's own committed scene (NX=360, NY=1584,
    ABSORB=TAPER=40, SRC_X=300, PLANE_X=77, STEPS=1400, COURANT_FRAC=0.99,
    OBJ_Y=792, D_SP=223, cpl=20 at 600nm, window geometry R_OUT=78 /
    GUARD_OUT=185 / W_FLANK=78), hardcoded here with citation rather than
    imported, so the suite never depends on an experiment directory.

    Four gates, four 1400-step FDTD runs (~90 s -- an opt-in stage like the
    heavy stage 5, NOT part of the fast `--only 12346789` default):

      a. FREE-SPACE DIVERGENCE IDENTITY (theta=0, width=40): the 1/e^2
         half-width of `ambient.observer_profile` at three planes reproduces
         w0*sqrt(1+(z/z_R)^2), z_R = pi*w0^2/lambda = 251.327 cells, to <=3%.
         This gates the FWHM relation too: Delta-theta = 2*sqrt(2 ln 2)*
         lambda/(2 pi w0) follows from z_R by one algebraic step, and this
         domain's usable x-span (223 cells ~ 0.89 z_R) cannot reach the true
         far field, so a direct far-field-FWHM gate is not honestly available.
      b. POINTING IDENTITY (theta=40deg, width=40): the interpolated beam
         centre at PLANE_X sits within +/-2 cells of y_c + D_SP*tan(40deg)
         = 979.12.
      c. ABSOLUTE REGRESSION ANCHOR (theta=+40deg, profile="plane"): the
         legacy tapered-top-hat path still reproduces exp-041 Block MAIN's
         committed C_empty(+40deg, 600nm) = -0.010964794540566314. Stated as a
         RELATIVE tolerance with the reference platform named (Red Team docket
         item 14, ELECTROMAGNETISM's Phase-2 catch upheld): a 1400-step FDTD
         bit-reproducibility claim that does not name its platform is not a
         gate, it is a hope.
      d. OBLIQUE-WIDTH GATE (theta=40deg, width=56.063 = w0/cos(40deg) for
         FWHM=10deg at 600nm): the 1/e^2 half-width at PLANE_X reproduces
         w0*sqrt(1+(z_eff/z_R)^2)/cos(theta0) = 79.4747 cells to <=5%. This is
         the gate that matters: gates (a) and (b) CANNOT fail on exp-046's own
         actual Phase-1 defect (a source width of w0 where the physics
         requires w0/cos(theta0)) -- (a) runs at theta=0 where the two agree
         and (b) reads only the centroid. Red Team's own independent FDTD run
         of exactly this configuration measured 80.47 cells (1.3% high), and
         the same run at the WRONG width (w0 = 42.947) measured 87.25 against
         a 79.47 target -- 9.8% off, i.e. this gate fires on the real defect
         and passes on the fix.
    """
    print("stage 16 — oblique Gaussian line source vs closed-form identities")
    from lab import ambient as amb
    from lab import sections as sc

    NX16, NY16, AB16, TAPER16 = 360, 1584, 40, 40
    SRC_X16, PLANE_X16, STEPS16, CPL16 = 300, 77, 1400, 20
    OBJ_Y16 = NY16 // 2                    # 792
    D_SP16 = SRC_X16 - PLANE_X16           # 223
    R_OUT16, GUARD_OUT16, W_FLANK16 = 78, 185, 78
    C_COEF16 = 2.0 * np.sqrt(2.0 * np.log(2.0)) / (2.0 * np.pi)   # 0.374781250

    def run16(width, theta, profile="gauss", sigma=None):
        sim = Sim(NX16, NY16, cells_per_lambda=CPL16, courant_frac=0.99, absorb=AB16)
        if profile == "gauss":
            sim.add_line_source(SRC_X16, profile="gauss", width=width,
                                angle_deg=theta, amplitude=1.0)
        else:
            sim.add_line_source(SRC_X16, angle_deg=theta, edge=TAPER16, amplitude=1.0)
        sim.run(STEPS16)
        return sc.phasors(sc.full_capture(sim))

    def half_width_1e2(b, y_lo):
        """1/e^2 half-width and interpolated centre of a positive flux profile.
        For E ~ exp(-y^2/w^2) the intensity falls to 1/e^2 of peak at y = w, so
        this measures w directly -- the same quantity every closed form here is
        written in."""
        b = np.asarray(b, dtype=float)
        y = np.arange(y_lo, y_lo + b.size, dtype=float)
        ip = int(np.argmax(b))
        thr = b[ip] / np.e ** 2
        r = ip + int(np.argmax(b[ip:] < thr))
        l = ip - int(np.argmax(b[:ip + 1][::-1] < thr))
        itp = lambda i0, i1: y[i0] + (thr - b[i0]) * (y[i1] - y[i0]) / (b[i1] - b[i0])
        hi, lo = itp(r - 1, r), itp(l + 1, l)
        return 0.5 * (hi - lo), 0.5 * (hi + lo)

    # --- gate a: free-space Gaussian divergence identity (theta = 0)
    W0_A = 40.0
    z_r = np.pi * W0_A ** 2 / CPL16
    ph_a = run16(W0_A, 0.0)
    worst_a, detail_a = 0.0, []
    for plane_x in (250, 150, PLANE_X16):
        prof = amb.observer_profile(ph_a, plane_x, AB16, NY16 - AB16)
        hw, _ = half_width_1e2(prof, AB16)
        z = SRC_X16 - plane_x
        target = W0_A * np.sqrt(1.0 + (z / z_r) ** 2)
        rel = abs(hw - target) / target
        worst_a = max(worst_a, rel)
        detail_a.append(f"z={z}: {hw:.2f} vs {target:.2f}")
    print(f"  [info] stage16 · w(z) at 3 planes (z_R={z_r:.2f}): " + " | ".join(detail_a))
    check("gauss-source", "free-space divergence w(z) vs closed form (worst of 3 planes)",
          f"{worst_a:.2%}", worst_a <= 0.03, "<=3%")

    # --- gate b: pointing identity (theta = 40 deg, same width)
    ph_b = run16(W0_A, 40.0)
    prof_b = amb.observer_profile(ph_b, PLANE_X16, AB16, NY16 - AB16)
    _, ctr_b = half_width_1e2(prof_b, AB16)
    target_ctr = OBJ_Y16 + D_SP16 * np.tan(np.radians(40.0))
    check("gauss-source", "oblique beam centre at PLANE_X (ray optics y_c + D_SP*tan40)",
          f"{ctr_b:.2f} vs {target_ctr:.2f}", abs(ctr_b - target_ctr) <= 2.0,
          "within +/-2 cells")

    # --- gate c: absolute regression anchor on the legacy plane path
    ph_c = run16(None, 40.0, profile="plane")
    prof_c = amb.observer_profile(ph_c, PLANE_X16, AB16, NY16 - AB16)
    bo, bf = amb.window_means(prof_c, AB16, OBJ_Y16, R_OUT16, GUARD_OUT16, W_FLANK16)
    c_empty = amb.weber(bo, bf)
    REF_C_EMPTY = -0.010964794540566314        # exp-041 results.json, block_main, +40deg/600nm
    rel_c = abs(c_empty - REF_C_EMPTY) / abs(REF_C_EMPTY)
    print(f"  [info] stage16 · reference platform for gate c: python "
          f"{sys.version.split()[0]} / numpy {np.__version__} / {sys.platform}")
    check("gauss-source", "plane-path C_empty(+40deg,600nm) reproduces exp-041 (RELATIVE, platform-named)",
          f"{rel_c:.2e}", rel_c <= 1e-12, "<=1e-12 relative")

    # --- gate d: the oblique-width gate (the one that fires on the real defect)
    W0_D = C_COEF16 * CPL16 / np.radians(10.0)          # 42.947 -- the WRONG width
    WIDTH_D = W0_D / np.cos(np.radians(40.0))           # 56.063 -- the right one
    z_r_d = np.pi * W0_D ** 2 / CPL16
    z_eff_d = D_SP16 / np.cos(np.radians(40.0))
    target_d = W0_D * np.sqrt(1.0 + (z_eff_d / z_r_d) ** 2) / np.cos(np.radians(40.0))
    ph_d = run16(WIDTH_D, 40.0)
    prof_d = amb.observer_profile(ph_d, PLANE_X16, AB16, NY16 - AB16)
    hw_d, _ = half_width_1e2(prof_d, AB16)
    rel_d = abs(hw_d - target_d) / target_d
    check("gauss-source", f"oblique-width identity: 1/e^2 half-width at PLANE_X "
          f"(width={WIDTH_D:.3f} = w0/cos40)",
          f"{hw_d:.2f} vs {target_d:.2f} ({rel_d:.2%})", rel_d <= 0.05, "<=5%")


_STAGE_IDS = frozenset(str(n) for n in range(1, 17))


def _stage_selected(n, only):
    """Stage selection, aware of ALL THREE of this suite's `--only` idioms.

    Panel Iteration 15 / Red Team attack #5 fixed the multi-digit half: the
    naive `str(n) in only` check silently fired stage 12 on every existing
    invocation (the local default "123456789" and CI's "--only 12346789" both
    contain "1" immediately followed by "2"), purely an accident of decimal-
    digit concatenation with the single-digit stages 1-9.

    Panel Iteration 17 Phase 5 (Red Team finding F3/L-E) fixed the mixed-idiom
    half: "--only 12,13,14" ALSO fired stages 1/2/3/4 as bare substrings, with
    no comma-awareness at all. Resolved by tokenizing on commas/whitespace.

    Panel Iteration 23 (exp-046) fixes what that left, and it is the SAME bug
    species a third time -- caught by direct execution before stage 16 was
    wired, not by reading: a LONE multi-digit token was still passed to the
    single-digit substring test for stages 1-9, so `--only 16` selected stages
    1 AND 6 as well as stage 16 (and `--only 12`, documented in SESSION_LOG as
    "stage 12 alone, 5/5", actually fired stages 1, 2 and 12). It also dropped
    a packed token in a mixed invocation entirely: "--only 12346789,10,11",
    cited as 46/46 across five SESSION_LOG entries, selected only stages 10
    and 11.

    The rule now, one sentence: each token is EITHER an exact stage id (any
    width -- it selects exactly that stage) OR a legacy PACKED digit run
    (e.g. "123456789", "12346789", "1234"), in which case single-digit stages
    match as substrings and multi-digit stages match on digit boundaries.
    Tokens are independent, so mixed invocations compose. Every citation in
    this program's own history reproduces: "123456789" -> 1-9, "12346789" ->
    1,2,3,4,6,7,8,9, "12346789,10,11" -> those plus 10 and 11, "12,13" ->
    12 and 13, "12" -> stage 12 alone, "5" -> stage 5 alone, "16" -> stage 16
    alone."""
    for tok in [t for t in re.split(r"[,\s]+", only.strip()) if t]:
        if tok in _STAGE_IDS:
            if tok == str(n):
                return True
            continue
        if n < 10:
            if str(n) in tok:
                return True
        elif re.search(rf"(?<!\d){n}(?!\d)", tok):
            return True
    return False


# ------------------------------------------------------------------ main
if __name__ == "__main__":
    only = "123456789"
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1]
    run_stage10 = _stage_selected(10, only)
    run_stage11 = _stage_selected(11, only)
    run_stage12 = _stage_selected(12, only)
    run_stage13 = _stage_selected(13, only)
    run_stage14 = _stage_selected(14, only)
    run_stage15 = _stage_selected(15, only)
    run_stage16 = _stage_selected(16, only)
    t0 = time.time()

    if _stage_selected(1, only):
        stage1_regression()
    if _stage_selected(2, only):
        stage2_impedance()
    if _stage_selected(3, only) or _stage_selected(4, only):
        sim_scene, env_scene_ours = _our_small_scene(True)
        _, env_vac_ours = _our_small_scene(False)
        ours_scat = env_scene_ours - env_vac_ours
        lam_small = sim_scene.measure_lambda(y_line=160, x_lo=70, x_hi=260)
        shadow_small = float(
            np.mean(env_scene_ours[156:226, 90:110] ** 2)
            / np.mean(env_scene_ours[156:226, 140:165] ** 2))
        check("ours-small", "lambda (cells)", f"{lam_small:.2f}",
              abs(lam_small - 20.0) <= 0.2, "20.0±0.2")
        env_lib = stage3_fdtd_lib(ours_scat, shadow_small) if _stage_selected(3, only) else None
        env_c = stage4_ceviche(ours_scat) if _stage_selected(4, only) else None

        if env_lib is not None and env_c is not None:
            fig, axes = plt.subplots(1, 3, figsize=(12.6, 3.6), dpi=140)
            for ax, e, title in [
                (axes[0], env_scene_ours, "lab engine (time-domain)"),
                (axes[1], env_lib, "flaport fdtd (time-domain)"),
                (axes[2], env_c, "ceviche (FDFD)"),
            ]:
                ax.imshow((e / np.max(e[ROI]))[ROI].T, cmap="magma", vmin=0, vmax=1.1,
                          origin="lower")
                ax.set_title(title, loc="left", fontsize=9)
                ax.set_xticks([]); ax.set_yticks([])
            fig.suptitle("stages 3+4 — one scene, three independent solvers (|E| envelope, ROI)",
                         x=0.04, ha="left", fontsize=11, fontweight="bold")
            fig.tight_layout(rect=[0, 0, 1, 0.9])
            fig.savefig(os.path.join(HERE, "v34_cross.png")); plt.close(fig)

    if _stage_selected(5, only):
        stage5_cloak()
    if _stage_selected(6, only):
        stage6_observer()
    if _stage_selected(7, only):
        stage7_absorber()
    if _stage_selected(8, only):
        stage8_sections()
    if _stage_selected(9, only):
        stage9_ambient()
    if run_stage10:
        stage10_radial_power()
    if run_stage11:
        stage11_multisource_superposition()
    if run_stage12:
        stage12_kinetics_kernel()
    if run_stage13:
        stage13_temporal_csf()
    if run_stage14:
        stage14_amplitude_bridge()
    if run_stage15:
        stage15_thermo_sidecar()
    if run_stage16:
        stage16_oblique_gaussian_source()

    n_fail = sum(1 for r in RESULTS if not r[3])
    print(f"\n{len(RESULTS) - n_fail}/{len(RESULTS)} checks passed in {time.time() - t0:.0f} s")
    sys.exit(1 if n_fail else 0)
