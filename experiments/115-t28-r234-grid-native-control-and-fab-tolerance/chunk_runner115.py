"""Block CG runner for exp-115 (Panel Iteration 92) -- the six control
readings that measure `G = per_step(r=234)/per_step(r=156)` directly, on
both grids, in one session, at matched step counts and matched scene mix.

Runner: bench panel shift (T5820) -- Director Clyde, live session.

Modelled on `experiments/114-.../chunk_runner114.py`. `build_sim` is
REUSED BYTE-FOR-BYTE (and the MF-12 identity gate proves it, by comparing
this file's own `build_sim` source segment against
`chunk_runner114.py`'s, parsed out of the committed source with `ast` --
no import, no side effects). `_time_control_blend` is the same recipe
with **the one minimal, disclosed change**: `r` becomes a parameter
instead of the hardcoded `156`. That single change is the whole reason
this cycle exists -- no control burst has ever been timed on any grid but
r=156 in this program's history.

NOT a checkpoint/resume runner: nothing here chunks, pickles, resumes or
captures. Six readings x three cold-built scenes = 18 `Sim.run()` calls
and 46,008 grid-steps, and that is the entire FDTD spend of this cycle.
No production leg, no `full_capture`, no `window_stats`, no
angular-pattern instrument, no named-bin classification.

Phase-3 fixes visible in THIS file:

  MF-6(a) The sustained pass is **ABBA** (U156, U234, U234b, U156b), not
          ABAB. Under ABAB both sustained pairs inherit the same-signed
          (a+b)/2 lag while `d_rep` reads ~0 -- an alarm structurally
          incapable of producing the reading that means "bad"
          (lab/ARTIFACTS.md's own named invariant).
  MF-6(b) Per-reading start/end ISO-UTC timestamps, per-scene wall times,
          and both pairwise `G` values are persisted, immediately, one
          reading at a time.
  MF-6(c) Same-grid drift is reported as a RATE PER UNIT ELAPSED TIME,
          because ABBA makes the two same-grid lags unequal (a+2b vs b).
  MF-6(e) Exclusive-use protocol, plus a machine-state block persisted
          with the run (lscpu/L3, THP, BLAS/OMP thread env, numpy config,
          loadavg before and after every reading).
  MF-12   An ABSOLUTE IDENTITY GATE on the new machinery, executed before
          any reading is trusted.
  R19     The `Sim.run()` call-count assert is CONDITIONAL on
          `repeat_skipped` (18 or 12) -- an invariant that fires
          spuriously on the designed-safe path is worse than none.
  R27/R28 `control_budget_gate()` reuses R110's own COST_GATE_TOTAL_S and
          COST_GATE_SAFETY_MARGIN unmodified and is evaluated BEFORE each
          next expensive stage, never after it. Graceful degradation at
          BOTH ends (Red Team's recommended-not-mandatory branch,
          ADOPTED and disclosed): a breach spends the REPEAT first; if
          even the primary sustained pass would breach,
          SUSTAINED_CONTROL_STEPS steps DOWN to the largest value that
          fits before the gate raises.

EXCLUSIVE-USE PROTOCOL (MF-6e, stated so it can be enforced rather than
hoped for). For the duration of `--run-cg`: no concurrent trust-suite
run, no second SSH session doing work, no `analyze115.py`, no editor
indexing the repo, nothing else on the T5820. The entire product of this
cycle is wall time; an uncontrolled concurrent process invalidates every
reading. `--post-ticker` exists precisely so the Director can follow the
run from the co-lab ticker instead of opening a second session to poll.
"""
import argparse
import ast
import json
import os
import platform
import socket
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
EXP114_DIR = os.path.join(ROOT, "experiments", "114-t28-kappa-exponent-r234-calibration")
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "experiments", "110-t28-item-i-local-norm-and-controls"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "112-t28-cpl25-floor-spot-check"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "113-t28-r312-cpl25-plus168-bin"))
sys.path.insert(0, EXP114_DIR)

import numpy as np           # noqa: E402
import run as R110           # noqa: E402
import run112 as R112        # noqa: E402
import run113 as R113        # noqa: E402
import run114 as R114        # noqa: E402
import run115 as R           # noqa: E402
from lab import Sim, materials  # noqa: E402

# R29: executed identity assertions -- five genuinely distinct modules.
assert len({id(R110), id(R112), id(R113), id(R114), id(R)}) == 5, (
    "R29: run110/run112/run113/run114/run115 must be five distinct module objects")
assert hasattr(R, "classify_m5") and hasattr(R, "DISCLAIMER_115"), (
    "R29: R must be exp-115's own run115.py")
assert os.path.basename(os.path.dirname(os.path.abspath(R.__file__))) == os.path.basename(HERE)

SCRATCH = os.environ.get("EXP115_SCRATCH",
                         os.path.join(os.path.expanduser("~"), "routines", "scratch", "exp115"))
DATA_DIR = R.DATA_DIR
READINGS_PATH = os.path.join(DATA_DIR, "readings.json")
TICKER_ISSUE = "32"
TICKER_REPO = "Marsh-Press-Co/co-lab"

CONTROL_SCENES = R.CONTROL_SCENES
SHORT_CONTROL_STEPS = R.SHORT_CONTROL_STEPS
SUSTAINED_CONTROL_STEPS = R.SUSTAINED_CONTROL_STEPS
COST_GATE_TOTAL_S = R.COST_GATE_TOTAL_S
COST_GATE_SAFETY_MARGIN = R.COST_GATE_SAFETY_MARGIN

_SIM_RUN_CALLS = 0     # R19: the code-enforced call counter


def build_sim(g, which):
    """Byte-for-byte the same construction as experiments/110-.../112-.../
    113-.../chunk_runner*.py::build_sim."""
    sim = Sim(g["N"], g["N"], cells_per_lambda=g["cpl"],
              courant_frac=R110.COURANT_FRAC, absorb=g["absorb"])
    if which == "hollow":
        materials.graded_black_shell(sim, g["CX"], g["CY"], g["R_CORE"], g["R_COAT"],
                                      sigma_max=g["sigma_max"])
    elif which == "peccored":
        materials.pec_disk(sim, g["CX"], g["CY"], g["R_CORE"])
        materials.graded_black_shell(sim, g["CX"], g["CY"], g["R_CORE"], g["R_COAT"],
                                      sigma_max=g["sigma_max"])
    elif which == "empty":
        pass
    else:
        raise ValueError(which)
    sim.add_line_source(g["SRC_X"], angle_deg=0.0, profile="plane", edge=g["edge"])
    return sim


# ================================================================================
# MF-12 -- ABSOLUTE IDENTITY GATE ON THE NEW MACHINERY (PANEL.md's own
# Phase-4 house rule: new machinery ==> at least one absolute identity
# gate BEFORE results are trusted). Executed before any reading.
# ================================================================================
def _func_source(path, name):
    """Parse a committed source FILE and return one function's own source
    segment. Deliberately does NOT import the module: chunk_runner114.py
    calls os.makedirs() on a hardcoded, session-specific scratch path at
    import time, and an identity gate must not have side effects."""
    with open(path, encoding="utf-8") as f:
        src = f.read()
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return ast.get_source_segment(src, node)
    return None


def _module_literal(path, name):
    """Return a module-level literal assignment's value, without import."""
    with open(path, encoding="utf-8") as f:
        src = f.read()
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id == name:
                    return ast.literal_eval(node.value)
    return None


def identity_gate(verbose=True):
    """Asserts that this cycle's parameterized machinery, evaluated at
    r=156, is the SAME ARTICLE exp-114's own hardcoded machinery built.
    Zero FDTD: no Sim is constructed and nothing is run."""
    cr114_path = os.path.join(EXP114_DIR, "chunk_runner114.py")
    checks = []

    def check(name, ok, detail=""):
        checks.append(dict(name=name, ok=bool(ok), detail=str(detail)))
        if verbose:
            print("  %-58s %s%s" % (name, "PASS" if ok else "FAIL",
                                    ("   (%s)" % detail) if detail else ""))
        return bool(ok)

    # 1. build_sim: byte-identical source segment.
    mine = _func_source(os.path.join(HERE, "chunk_runner115.py"), "build_sim")
    theirs = _func_source(cr114_path, "build_sim")
    check("build_sim source segment byte-identical to chunk_runner114",
          mine is not None and theirs is not None and mine == theirs,
          "%d chars" % (len(mine) if mine else -1))

    # 2. The scene set and the two step constants.
    their_scenes = _module_literal(cr114_path, "CONTROL_SCENES")
    check("CONTROL_SCENES identical (same three scenes, same order)",
          tuple(their_scenes) == tuple(CONTROL_SCENES), str(their_scenes))
    check("SHORT_CONTROL_STEPS identical",
          _module_literal(cr114_path, "SHORT_CONTROL_STEPS") == SHORT_CONTROL_STEPS,
          SHORT_CONTROL_STEPS)
    check("SUSTAINED_CONTROL_STEPS identical (nominal)",
          _module_literal(cr114_path, "SUSTAINED_CONTROL_STEPS") == SUSTAINED_CONTROL_STEPS,
          SUSTAINED_CONTROL_STEPS)

    # 3. The geometry dict at r=156, field-for-field. This is the article.
    theirs_geom = R114.geom_fixedabs_cpl(156, 25)
    mine_geom = R.geom_fixedabs_cpl(156, R.CPL_TARGET)
    same = (set(theirs_geom.keys()) == set(mine_geom.keys())
            and all(theirs_geom[k] == mine_geom[k] for k in theirs_geom))
    check("geom_fixedabs_cpl(156, 25) identical field-for-field", same,
          "%d fields" % len(mine_geom))

    # 4. exp-114's own _time_control_blend really did hardcode r=156.
    their_blend = _func_source(cr114_path, "_time_control_blend") or ""
    check("chunk_runner114._time_control_blend hardcodes geom_fixedabs_cpl(156, 25)",
          "geom_fixedabs_cpl(156, 25)" in their_blend)
    check("this cycle's _time_control_blend takes r as a parameter (the ONE disclosed change)",
          "def _time_control_blend(r," in (_func_source(
              os.path.join(HERE, "chunk_runner115.py"), "_time_control_blend") or ""))

    # 5. The r=234 geometry this cycle newly times is the same material law.
    g234 = R.geom_fixedabs_cpl(234, R.CPL_TARGET)
    check("tau_shell invariant across the two timed grids",
          mine_geom["tau_shell"] == g234["tau_shell"] == 24.0, g234["tau_shell"])
    check("absorb/edge invariant across the two timed grids",
          (mine_geom["absorb"], mine_geom["edge"]) == (g234["absorb"], g234["edge"]) == (50, 50))
    check("geometry identity (r=156/234/312, cpl=20 reduction)",
          R.verify_geometry_identity()["pass_"])

    ok = all(c["ok"] for c in checks)
    if verbose:
        print("\nMF-12 identity gate: %s (%d checks)" % ("PASS" if ok else "FAIL", len(checks)))
    return dict(pass_=ok, checks=checks)


# ================================================================================
# MACHINE STATE (MF-6e) -- persisted once per run and, in its cheap form
# (loadavg), before and after every reading.
# ================================================================================
def _cheap(cmd):
    try:
        out = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=20)
        return out.stdout.strip() or out.stderr.strip()
    except Exception as exc:          # noqa: BLE001 -- machine state must never break a run
        return "unavailable: %s" % exc


def _read_file(path, limit=400):
    try:
        with open(path) as f:
            return f.read()[:limit].strip()
    except Exception as exc:          # noqa: BLE001
        return "unavailable: %s" % exc


def loadavg():
    try:
        return list(os.getloadavg())
    except (AttributeError, OSError):
        return None


def machine_state():
    """Everything a future cycle needs to know whether this session's
    wall times are comparable to its own. THERMODYNAMICS' Sec 10(i)/Sec 11
    recommendation, adopted."""
    npcfg = ""
    try:
        import io
        buf = io.StringIO()
        old = sys.stdout
        sys.stdout = buf
        try:
            np.show_config()
        finally:
            sys.stdout = old
        npcfg = buf.getvalue()
    except Exception as exc:          # noqa: BLE001
        npcfg = "unavailable: %s" % exc
    thread_env = {k: os.environ.get(k) for k in
                  ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                   "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS")}
    return dict(
        hostname=socket.gethostname(),
        platform=platform.platform(),
        python_version=sys.version.replace("\n", " "),
        numpy_version=np.__version__,
        cpu_count=os.cpu_count(),
        lscpu=_cheap("lscpu | egrep 'Model name|Socket|Core|Thread|CPU\\(s\\)|MHz|L3|NUMA' "
                     "|| true")[:2000],
        cpuinfo_head=_read_file("/proc/cpuinfo", 800),
        meminfo_head=_read_file("/proc/meminfo", 300),
        transparent_hugepage=_read_file("/sys/kernel/mm/transparent_hugepage/enabled", 200),
        thread_env=thread_env,
        numpy_show_config=npcfg[:2000],
        loadavg=loadavg(),
        timestamp_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))


# ================================================================================
# PERSISTENCE -- one reading at a time, immediately (MF-6b). A run that
# dies at reading 5 must still leave readings 1-4 on disk.
# ================================================================================
def _load_readings():
    if os.path.exists(READINGS_PATH):
        with open(READINGS_PATH) as f:
            return json.load(f)
    return dict(cycle="exp-115", runner="bench panel shift (T5820) -- Director Clyde, live session",
                reading_order=list(R.READING_ORDER), readings={}, gates=[],
                repeat_skipped=False, repeat_skip_reason=None,
                sustained_steps_used=SUSTAINED_CONTROL_STEPS, sustained_stepped_down=False,
                machine_state=None, n_sim_run_calls=0)


def _save_readings(doc):
    os.makedirs(DATA_DIR, exist_ok=True)
    tmp = READINGS_PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(doc, f, indent=2, default=str)
    os.replace(tmp, READINGS_PATH)


def _ticker(line, enabled):
    """MF-6e: values only, no IPs, no host addresses -- so the Director
    can follow the run from the co-lab ticker instead of opening a second
    session on the bench and breaking exclusive use."""
    print("[ticker] %s" % line)
    if not enabled:
        return
    try:
        subprocess.run(["gh", "issue", "comment", TICKER_ISSUE, "-R", TICKER_REPO,
                        "-b", line], check=False, capture_output=True, text=True, timeout=60)
    except Exception as exc:          # noqa: BLE001 -- the ticker must never break a run
        print("[ticker] post failed (non-fatal): %s" % exc)


# ================================================================================
# THE READING -- the one disclosed change from chunk_runner114 is `r`
# ================================================================================
def _time_control_blend(r, control_steps_per_scene, scenes=CONTROL_SCENES):
    """Fresh, COLD builds of EACH scene in `scenes`, each timed for
    exactly `control_steps_per_scene` steps, summed -- byte-for-byte the
    same recipe as `chunk_runner114.py::_time_control_blend`, with the
    ONE minimal, disclosed change: `r` is a parameter instead of the
    hardcoded `156`. The 3-scene mix is mandatory, not stylistic
    (exp-113's own Fix 3b: re-timing `empty` alone against a blended
    comparator is a real, signed, anti-conservative commensurability
    defect -- though note MF-11: the profiled per-scene premium is
    +1.287% peccored/hollow and +0.009% peccored/empty, NOT the "~14%"
    the Phase-1 document repeated).

    Timing brackets `sim.run()` ONLY -- the cold build is outside the
    stopwatch, exactly as in chunk_runner114."""
    global _SIM_RUN_CALLS
    g = R.geom_fixedabs_cpl(r, R.CPL_TARGET)
    start = time.time()
    per_scene = {}
    total_wall_s = 0.0
    for which in scenes:
        sim = build_sim(g, which)
        t0 = time.time()
        sim.run(control_steps_per_scene)
        dt = time.time() - t0
        _SIM_RUN_CALLS += 1
        per_scene[which] = dt
        total_wall_s += dt
        del sim
    end = time.time()
    total_steps = control_steps_per_scene * len(scenes)
    return dict(r=r, cpl=R.CPL_TARGET, n_scenes=len(scenes),
                control_steps=control_steps_per_scene, total_steps=total_steps,
                per_scene_wall_s=per_scene, total_wall_s=total_wall_s,
                per_step_s=total_wall_s / total_steps,
                start_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(start)),
                end_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(end)),
                start_epoch_s=start, end_epoch_s=end,
                mid_epoch_s=0.5 * (start + end))


# ================================================================================
# BUDGET GATE (R27/R28) -- executable, upstream, with graceful
# degradation at BOTH ends.
# ================================================================================
def _project_total_s(per_step_r156, g, sustained_steps, include_repeat):
    """The Phase-1 projection formula, unchanged in form:
    per_step(r=156) x grid-steps-per-grid x (1 + G) x safety_margin,
    expressed in r=156-equivalent cost units. Deliberately projects the
    WHOLE cycle (including already-spent readings), which is the
    conservative direction."""
    n_per_grid = len(CONTROL_SCENES) * (SHORT_CONTROL_STEPS
                                        + (2 if include_repeat else 1) * sustained_steps)
    return per_step_r156 * n_per_grid * (1.0 + g) * COST_GATE_SAFETY_MARGIN


def _largest_sustained_that_fits(per_step_r156, g, include_repeat):
    """The ADOPTED step-down branch (Red Team's recommended-not-mandatory
    addition, THERMO Sec 12): the largest SUSTAINED_CONTROL_STEPS at or
    below the nominal 3334 whose projection fits under
    COST_GATE_TOTAL_S. Returns None if not even SHORT_CONTROL_STEPS fits."""
    k = 2 if include_repeat else 1
    denom = per_step_r156 * len(CONTROL_SCENES) * (1.0 + g) * COST_GATE_SAFETY_MARGIN * k
    if denom <= 0:
        return None
    n = int((COST_GATE_TOTAL_S / (per_step_r156 * len(CONTROL_SCENES) * (1.0 + g)
                                  * COST_GATE_SAFETY_MARGIN) - SHORT_CONTROL_STEPS) / k)
    n = min(n, SUSTAINED_CONTROL_STEPS)
    return n if n >= SHORT_CONTROL_STEPS else None


def control_budget_gate(stage, per_step_r156, g, sustained_steps, doc,
                        measured_elapsed_s=None, per_step_r234=None):
    """R27/R28: evaluated BEFORE the next Sim.run(), never after it, and
    it RAISES rather than proceeds.

    stage == "after_S156"  -- G_prior = G_E (exp-114's own disclosed prior)
    stage == "after_S234"  -- re-projected with the MEASURED G_short
    stage == "after_U234"  -- the repeat pass, projected from MEASURED
                              elapsed time rather than from any prior

    Degradation order (a budget breach should cost this cycle its REPEAT,
    not its primary measurement): drop the repeat first; only if the
    PRIMARY sustained pass would itself breach does SUSTAINED_CONTROL_STEPS
    step down; only if no value at or above SHORT_CONTROL_STEPS fits does
    the gate raise."""
    rec = dict(stage=stage, per_step_r156=per_step_r156, g_used=g,
               sustained_steps_in=sustained_steps, bound_s=COST_GATE_TOTAL_S,
               safety_margin=COST_GATE_SAFETY_MARGIN,
               timestamp_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))

    if stage == "after_U234":
        # Project the repeat pass from what the primary pass actually cost.
        repeat_cost_s = len(CONTROL_SCENES) * sustained_steps * (per_step_r156 + per_step_r234)
        projected = (measured_elapsed_s + repeat_cost_s) * COST_GATE_SAFETY_MARGIN
        rec.update(measured_elapsed_s=measured_elapsed_s, repeat_cost_s=repeat_cost_s,
                   projected_total_s=projected, pass_=bool(projected < COST_GATE_TOTAL_S))
        if not rec["pass_"]:
            doc["repeat_skipped"] = True
            doc["repeat_skip_reason"] = (
                "R27/R28 budget gate at stage after_U234: measured elapsed %.1fs + projected "
                "repeat %.1fs, x%.2f safety margin = %.1fs, which breaches "
                "COST_GATE_TOTAL_S = %ds. Readings U234b/U156b SKIPPED so the breach costs "
                "this cycle its repeat, not its primary measurement. M4 reports UNMEASURED, "
                "m3_scored is False, and the R19 call-count assert expects %d calls."
                % (measured_elapsed_s, repeat_cost_s, COST_GATE_SAFETY_MARGIN, projected,
                   COST_GATE_TOTAL_S, R.N_SIM_RUN_CALLS_REPEAT_SKIPPED))
            rec["action"] = "SKIP-REPEAT"
        else:
            rec["action"] = "PROCEED"
        doc["gates"].append(rec)
        _save_readings(doc)
        return doc["sustained_steps_used"], rec

    include_repeat = not doc["repeat_skipped"]
    projected_full = _project_total_s(per_step_r156, g, sustained_steps, include_repeat)
    projected_primary = _project_total_s(per_step_r156, g, sustained_steps, False)
    rec.update(projected_total_s=projected_full, projected_primary_only_s=projected_primary)

    if projected_full < COST_GATE_TOTAL_S:
        rec.update(pass_=True, action="PROCEED")
        doc["gates"].append(rec)
        _save_readings(doc)
        return sustained_steps, rec

    # (i) spend the repeat first
    if include_repeat and projected_primary < COST_GATE_TOTAL_S:
        doc["repeat_skipped"] = True
        doc["repeat_skip_reason"] = (
            "R27/R28 budget gate at stage %s: the full six-reading plan projects %.1fs against "
            "COST_GATE_TOTAL_S = %ds, but the four-reading primary plan projects %.1fs and "
            "fits. Readings U234b/U156b SKIPPED -- the breach costs this cycle its repeat, not "
            "its primary measurement."
            % (stage, projected_full, COST_GATE_TOTAL_S, projected_primary))
        rec.update(pass_=True, action="SKIP-REPEAT")
        doc["gates"].append(rec)
        _save_readings(doc)
        return sustained_steps, rec

    # (ii) step SUSTAINED_CONTROL_STEPS down (ADOPTED branch, disclosed)
    n = _largest_sustained_that_fits(per_step_r156, g, False)
    if n is not None:
        doc["repeat_skipped"] = True
        doc["repeat_skip_reason"] = doc["repeat_skip_reason"] or (
            "R27/R28 budget gate at stage %s: repeat dropped before the step-down." % stage)
        doc["sustained_steps_used"] = n
        doc["sustained_stepped_down"] = True
        rec.update(pass_=True, action="STEP-DOWN", sustained_steps_out=n,
                   projected_after_step_down_s=_project_total_s(per_step_r156, g, n, False))
        doc["gates"].append(rec)
        _save_readings(doc)
        print("[gate] SUSTAINED_CONTROL_STEPS stepped down %d -> %d (graceful degradation "
              "branch, adopted and disclosed)" % (sustained_steps, n))
        return n, rec

    rec.update(pass_=False, action="RAISE")
    doc["gates"].append(rec)
    _save_readings(doc)
    raise RuntimeError(
        "R27/R28 budget gate REFUSED Block CG at stage %s: projected %.1fs (primary-only "
        "%.1fs) against COST_GATE_TOTAL_S = %ds, and no SUSTAINED_CONTROL_STEPS at or above "
        "%d fits. Nothing further is run."
        % (stage, projected_full, projected_primary, COST_GATE_TOTAL_S, SHORT_CONTROL_STEPS))


# ================================================================================
# BLOCK CG
# ================================================================================
def run_cg(post_ticker=False):
    global _SIM_RUN_CALLS
    gate = identity_gate(verbose=True)
    if not gate["pass_"]:
        raise RuntimeError("MF-12 identity gate FAILED -- no reading is trusted. %s"
                           % json.dumps(gate, indent=2))

    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(SCRATCH, exist_ok=True)
    doc = _load_readings()
    doc["identity_gate"] = gate
    doc["machine_state"] = machine_state()
    doc["scratch_dir"] = SCRATCH
    _save_readings(doc)
    _ticker("exp-115 Block CG: identity gate PASS, exclusive-use protocol in force, starting "
            "S156 (6 readings, 18 Sim.run calls, 46008 grid-steps).", post_ticker)

    t_run_start = time.time()

    def take(label, r, steps):
        load_before = loadavg()
        rd = _time_control_blend(r, steps)
        rd["label"] = label
        rd["loadavg_before"] = load_before
        rd["loadavg_after"] = loadavg()
        rd["n_sim_run_calls_cumulative"] = _SIM_RUN_CALLS
        doc["readings"][label] = rd
        doc["n_sim_run_calls"] = _SIM_RUN_CALLS
        _save_readings(doc)
        _ticker("exp-115 %s: r=%d, %d steps/scene, total %.1fs, per-step %.6fs (cumulative "
                "Sim.run calls %d)." % (label, r, steps, rd["total_wall_s"],
                                        rd["per_step_s"], _SIM_RUN_CALLS), post_ticker)
        return rd

    sustained = doc["sustained_steps_used"]

    # ---- 1. S156 -----------------------------------------------------------
    s156 = take("S156", 156, SHORT_CONTROL_STEPS)
    sustained, _ = control_budget_gate("after_S156", s156["per_step_s"], R.G_E, sustained, doc)

    # ---- 2. S234 (the FIRST r=234-grid control in this program's history) --
    s234 = take("S234", 234, SHORT_CONTROL_STEPS)
    g_short = s234["per_step_s"] / s156["per_step_s"]
    doc["G_short"] = g_short
    _save_readings(doc)
    sustained, _ = control_budget_gate("after_S234", s156["per_step_s"], g_short, sustained, doc)

    # ---- 3/4. the sustained pass, ABBA: U156, U234, U234b, U156b -----------
    u156 = take("U156", 156, sustained)
    u234 = take("U234", 234, sustained)
    doc["G_pair1"] = u234["per_step_s"] / u156["per_step_s"]
    _save_readings(doc)

    sustained_after, _ = control_budget_gate(
        "after_U234", u156["per_step_s"], doc["G_pair1"], sustained, doc,
        measured_elapsed_s=time.time() - t_run_start, per_step_r234=u234["per_step_s"])

    if not doc["repeat_skipped"]:
        u234b = take("U234b", 234, sustained)
        u156b = take("U156b", 156, sustained)
        doc["G_pair2"] = u234b["per_step_s"] / u156b["per_step_s"]
    else:
        doc["G_pair2"] = None
    _save_readings(doc)

    # ---- R19: the call-count invariant, CONDITIONAL on repeat_skipped -----
    expected = (R.N_SIM_RUN_CALLS_REPEAT_SKIPPED if doc["repeat_skipped"]
                else R.N_SIM_RUN_CALLS_FULL)
    assert _SIM_RUN_CALLS == expected, (
        "R19: expected %d Sim.run() calls (repeat_skipped=%s), counted %d"
        % (expected, doc["repeat_skipped"], _SIM_RUN_CALLS))
    doc["n_sim_run_calls"] = _SIM_RUN_CALLS
    doc["n_sim_run_calls_expected"] = expected
    doc["total_wall_s"] = time.time() - t_run_start
    doc["machine_state_end"] = dict(loadavg=loadavg(),
                                    timestamp_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                                                time.gmtime()))
    _save_readings(doc)
    _ticker("exp-115 Block CG COMPLETE: %d Sim.run calls (expected %d), %.1fs total, "
            "G_short=%.5f, G_pair1=%s, G_pair2=%s, repeat_skipped=%s. Run analyze115.py."
            % (_SIM_RUN_CALLS, expected, doc["total_wall_s"], doc.get("G_short", float("nan")),
               doc.get("G_pair1"), doc.get("G_pair2"), doc["repeat_skipped"]), post_ticker)
    print("\nWritten: %s" % READINGS_PATH)
    return doc


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="exp-115 Block CG runner (six control readings).")
    ap.add_argument("--identity-gate", action="store_true",
                    help="MF-12: run the absolute identity gate only. Zero FDTD.")
    ap.add_argument("--machine-state", action="store_true",
                    help="MF-6e: print/persist the machine-state block. Zero FDTD.")
    ap.add_argument("--run-cg", action="store_true",
                    help="Take the six readings. EXCLUSIVE USE OF THE BENCH REQUIRED.")
    ap.add_argument("--post-ticker", action="store_true",
                    help="After each reading, post a one-line values-only update to the "
                         "co-lab ticker (issue #%s) so the Director can follow without "
                         "opening a second session on the bench." % TICKER_ISSUE)
    args = ap.parse_args()

    if args.identity_gate:
        res = identity_gate(verbose=True)
        raise SystemExit(0 if res["pass_"] else 1)
    if args.machine_state:
        ms = machine_state()
        print(json.dumps(ms, indent=2, default=str))
        os.makedirs(DATA_DIR, exist_ok=True)
        d = _load_readings()
        d["machine_state"] = ms
        _save_readings(d)
        print("\nWritten: %s" % READINGS_PATH)
        raise SystemExit(0)
    if args.run_cg:
        run_cg(post_ticker=args.post_ticker)
        raise SystemExit(0)
    ap.print_help()
