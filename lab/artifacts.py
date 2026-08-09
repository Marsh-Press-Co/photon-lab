"""
lab.artifacts — run-artifact schema, I/O and loud validation (schema 0.1.0)
===========================================================================
The solver ↔ viz contract from co-lab #31; the human-readable spec lives in
lab/ARTIFACTS.md. One artifact directory = fields.npz + manifest.json.

Evidence Gate: `python -m lab.artifacts check <run_dir>...` validates every
run loudly (one line per check group — a silent gate and an absent gate
produce identical observations) and exits non-zero on any failure.
`python -m lab.artifacts selftest` proves the checker itself can fail.
"""

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

SCHEMA_VERSION = "0.1.0"

REQUIRED_ARRAYS = ("ez_snapshot", "ez_quarter", "eps_r", "sigma_e", "pec_mask")
TENSOR_ARRAYS = ("inv_mu_xx", "inv_mu_yy", "inv_mu_xy_hx", "inv_mu_xy_hy")
OBSERVER_ARRAYS = ("obs_angles_rad", "obs_return_flux")

REQUIRED_MANIFEST = (
    "schema_version", "experiment", "scene", "created_utc", "engine_commit",
    "suite_status", "lambda_nm", "grid", "run", "sources", "objects",
    "npz_sha256", "provenance",
)
GRID_KEYS = ("nx", "ny", "cells_per_lambda", "courant_frac", "absorb")
RUN_KEYS = ("steps", "snapshot_step", "quarter_offset_steps")
SOURCE_PROFILES = ("plane", "gauss")
OBSERVER_NORMS = ("vacuum_run", "incident_power")
PROVENANCE_KINDS = ("witness-statement", "document", "experiment", "paper", "url")

OBJECT_PARAMS = {
    "dielectric_cylinder": (("cx", "cy", "r", "eps_r"), ()),
    "pec_disk": (("cx", "cy", "r"), ()),
    "absorber_shell_stub": (("cx", "cy", "r_in", "r_out"), ("sigma_max", "eps_max")),
    "schurig_reduced_cloak_tm": (("cx", "cy", "r1", "r2"), ("mu_r_floor",)),
}


class ArtifactError(Exception):
    """Raised on save/load of an invalid artifact; carries every problem."""

    def __init__(self, problems):
        self.problems = list(problems)
        super().__init__("invalid artifact:\n  " + "\n  ".join(self.problems))


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _staggered_shape(name, nx, ny):
    return {
        "inv_mu_xx": (nx, ny - 1), "inv_mu_xy_hx": (nx, ny - 1),
        "inv_mu_yy": (nx - 1, ny), "inv_mu_xy_hy": (nx - 1, ny),
    }[name]


def validate(manifest, arrays, npz_path=None):
    """Return a list of problem strings (empty = valid). Grouped so `check`
    can report per-group liveness; see check() for the grouping."""
    return [p for _, ps in validate_groups(manifest, arrays, npz_path) for p in ps]


def validate_groups(manifest, arrays, npz_path=None):
    """[(group_name, [problems...]), ...] — every group always reported."""
    groups = []

    p = []
    for key in REQUIRED_MANIFEST:
        if key not in manifest:
            p.append(f"manifest missing key '{key}'")
    if manifest.get("schema_version") not in (SCHEMA_VERSION,):
        p.append(f"schema_version {manifest.get('schema_version')!r} != {SCHEMA_VERSION!r}")
    grid = manifest.get("grid", {})
    for key in GRID_KEYS:
        if key not in grid:
            p.append(f"grid missing '{key}'")
    run = manifest.get("run", {})
    for key in RUN_KEYS:
        if key not in run:
            p.append(f"run missing '{key}'")
    groups.append(("manifest", p))

    p = []
    for name in REQUIRED_ARRAYS:
        if name not in arrays:
            p.append(f"required array '{name}' missing")
    present_tensor = [n for n in TENSOR_ARRAYS if n in arrays]
    if present_tensor and len(present_tensor) != len(TENSOR_ARRAYS):
        p.append(f"tensor arrays are all-or-none, got only {present_tensor}")
    present_obs = [n for n in OBSERVER_ARRAYS if n in arrays]
    if len(present_obs) == 1:
        p.append(f"observer arrays are both-or-neither, got only {present_obs}")
    known = set(REQUIRED_ARRAYS) | set(TENSOR_ARRAYS) | set(OBSERVER_ARRAYS)
    for name, arr in arrays.items():
        if name not in known:
            p.append(f"unknown array '{name}' (schema {SCHEMA_VERSION} knows {sorted(known)})")
        elif name == "pec_mask":
            if arr.dtype != np.bool_:
                p.append(f"pec_mask dtype {arr.dtype}, want bool")
        elif not np.issubdtype(arr.dtype, np.floating):
            p.append(f"array '{name}' dtype {arr.dtype}, want float")
        elif not np.isfinite(arr).all():
            p.append(f"array '{name}' contains non-finite values")
    groups.append(("arrays", p))

    p = []
    nx, ny = grid.get("nx"), grid.get("ny")
    if isinstance(nx, int) and isinstance(ny, int):
        for name in REQUIRED_ARRAYS:
            if name in arrays and arrays[name].shape != (nx, ny):
                p.append(f"array '{name}' shape {arrays[name].shape}, want ({nx}, {ny})")
        for name in TENSOR_ARRAYS:
            want = _staggered_shape(name, nx, ny)
            if name in arrays and arrays[name].shape != want:
                p.append(f"array '{name}' shape {arrays[name].shape}, want {want}")
    if len(present_obs) == 2:
        ang, flux = arrays["obs_angles_rad"], arrays["obs_return_flux"]
        if ang.ndim != 1 or flux.ndim != 1 or ang.shape != flux.shape:
            p.append("observer arrays must be 1-D and same length")
        elif ang.size >= 2 and not (np.diff(ang) > 0).all():
            p.append("obs_angles_rad must be strictly increasing")
        obs = manifest.get("observer")
        if not isinstance(obs, dict):
            p.append("observer arrays present but manifest has no 'observer' block")
        else:
            for key in ("plane_x", "start_step", "normalization", "reference_run"):
                if key not in obs:
                    p.append(f"observer block missing '{key}'")
            if obs.get("normalization") not in OBSERVER_NORMS:
                p.append(f"observer.normalization {obs.get('normalization')!r} not in {OBSERVER_NORMS}")
            elif obs.get("normalization") == "vacuum_run" and not obs.get("reference_run"):
                p.append("normalization 'vacuum_run' requires a non-null reference_run "
                         "(the figure's normalization must be regenerable)")
            elif obs.get("normalization") == "incident_power" and obs.get("reference_run") is not None:
                p.append("normalization 'incident_power' requires reference_run null "
                         "(non-null iff vacuum_run)")
    elif "observer" in manifest:
        p.append("manifest 'observer' block present but observer arrays absent")
    groups.append(("shapes", p))

    p = []
    for i, src in enumerate(manifest.get("sources", [])):
        if src.get("profile") not in SOURCE_PROFILES:
            p.append(f"sources[{i}].profile {src.get('profile')!r} not in {SOURCE_PROFILES}")
        elif src["profile"] == "gauss" and "width" not in src:
            p.append(f"sources[{i}] gauss profile requires 'width'")
        for key in ("x", "y_lo", "y_hi", "ramp_periods", "amplitude"):
            if key not in src:
                p.append(f"sources[{i}] missing '{key}'")
    for i, obj in enumerate(manifest.get("objects", [])):
        typ = obj.get("type")
        if typ not in OBJECT_PARAMS:
            p.append(f"objects[{i}].type {typ!r} unknown (known: {sorted(OBJECT_PARAMS)})")
            continue
        required, optional = OBJECT_PARAMS[typ]
        params = obj.get("params", {})
        for key in required:
            if key not in params:
                p.append(f"objects[{i}] ({typ}) missing param '{key}'")
        for key in params:
            if key not in required + optional:
                p.append(f"objects[{i}] ({typ}) unknown param '{key}'")
    for i, ref in enumerate(manifest.get("provenance", [])):
        if ref.get("kind") not in PROVENANCE_KINDS:
            p.append(f"provenance[{i}].kind {ref.get('kind')!r} not in {PROVENANCE_KINDS}")
        if not ref.get("id"):
            p.append(f"provenance[{i}] missing 'id'")
    groups.append(("scene", p))

    p = []
    if npz_path is not None:
        actual = _sha256(npz_path)
        if manifest.get("npz_sha256") != actual:
            p.append(f"npz sha256 mismatch: manifest {manifest.get('npz_sha256')!r}, file {actual!r}")
    groups.append(("hash", p))

    return groups


def save_run(run_dir, manifest, arrays):
    """Write fields.npz + manifest.json (sha256 injected), validate, raise
    ArtifactError listing every problem if the result is invalid."""
    run_dir = Path(run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)
    npz_path = run_dir / "fields.npz"
    np.savez_compressed(npz_path, **arrays)
    manifest = dict(manifest, schema_version=SCHEMA_VERSION, npz_sha256=_sha256(npz_path))
    problems = validate(manifest, arrays, npz_path)
    if problems:
        raise ArtifactError(problems)
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True))
    return run_dir


def load_run(run_dir):
    """Read + validate an artifact directory; returns (manifest, arrays)."""
    run_dir = Path(run_dir)
    npz_path = run_dir / "fields.npz"
    manifest = json.loads((run_dir / "manifest.json").read_text())
    with np.load(npz_path) as z:
        arrays = {name: z[name] for name in z.files}
    problems = validate(manifest, arrays, npz_path)
    if problems:
        raise ArtifactError(problems)
    return manifest, arrays


def check(run_dirs, out=print):
    """Loud validation of artifact dirs. Reports every group per run
    (liveness), returns the number of failing groups."""
    failures = 0
    n_runs = 0
    for run_dir in run_dirs:
        n_runs += 1
        run_dir = Path(run_dir)
        out(f"run {run_dir}")
        try:
            manifest = json.loads((run_dir / "manifest.json").read_text())
            with np.load(run_dir / "fields.npz") as z:
                arrays = {name: z[name] for name in z.files}
        except Exception as exc:
            out(f"  [FAIL] load · {exc}")
            failures += 1
            continue
        for group, problems in validate_groups(manifest, arrays, run_dir / "fields.npz"):
            if problems:
                failures += 1
                for problem in problems:
                    out(f"  [FAIL] {group} · {problem}")
            else:
                out(f"  [PASS] {group}")
    out(f"artifact check: {n_runs} run(s), {failures} failing group(s)")
    return failures


def _selftest_manifest(nx, ny):
    return {
        "schema_version": SCHEMA_VERSION,
        "experiment": "selftest", "scene": "tiny", "created_utc": "1970-01-01T00:00:00+00:00",
        "engine_commit": "0" * 40, "suite_status": "selftest", "lambda_nm": 600.0,
        "grid": {"nx": nx, "ny": ny, "cells_per_lambda": 20, "courant_frac": 0.7, "absorb": 2},
        "run": {"steps": 10, "snapshot_step": 10, "quarter_offset_steps": 7},
        "sources": [{"profile": "plane", "x": 2, "y_lo": 2, "y_hi": ny - 2,
                     "ramp_periods": 3.0, "amplitude": 1.0, "edge": 2}],
        "objects": [{"type": "pec_disk", "params": {"cx": nx // 2, "cy": ny // 2, "r": 3}}],
        "provenance": [{"kind": "experiment", "id": "exp-000"}],
        "npz_sha256": "",
    }


def selftest(out=print):
    """Round-trip a tiny synthetic run, then prove the checker can fail:
    a checker that cannot fail is indistinguishable from no checker."""
    import tempfile

    nx, ny = 24, 16
    rng_free = np.linspace(0.0, 1.0, nx * ny, dtype=np.float32).reshape(nx, ny)
    arrays = {
        "ez_snapshot": rng_free, "ez_quarter": rng_free[::-1].copy(),
        "eps_r": np.ones((nx, ny), np.float32), "sigma_e": np.zeros((nx, ny), np.float32),
        "pec_mask": np.zeros((nx, ny), bool),
        "obs_angles_rad": np.linspace(-1.5, 1.5, 9), "obs_return_flux": np.ones(9),
    }
    manifest = _selftest_manifest(nx, ny)
    manifest["observer"] = {"plane_x": 2, "start_step": 5,
                            "normalization": "vacuum_run",
                            "reference_run": "experiments/selftest/artifacts/empty"}
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        run_dir = save_run(Path(tmp) / "tiny", manifest, arrays)
        load_run(run_dir)
        out("[PASS] selftest · round-trip save/load/validate")

        tampered = dict(arrays, ez_snapshot=arrays["ez_snapshot"] + 1.0)
        np.savez_compressed(run_dir / "fields.npz", **tampered)
        try:
            load_run(run_dir)
            ok = False
            out("[FAIL] selftest · tampered npz was accepted")
        except ArtifactError as exc:
            if any("sha256" in problem for problem in exc.problems):
                out("[PASS] selftest · tampered npz caught by the sha256 anchor")
            else:
                ok = False
                out(f"[FAIL] selftest · tamper rejected, but not by the hash: {exc.problems}")

        bad = {k: v for k, v in arrays.items() if k != "ez_quarter"}
        problems = validate(manifest, bad)
        if any("ez_quarter" in problem for problem in problems):
            out("[PASS] selftest · missing required array rejected")
        else:
            ok = False
            out("[FAIL] selftest · missing required array was accepted")

        unref = dict(manifest, observer=dict(manifest["observer"], reference_run=None))
        problems = validate(unref, arrays)
        if any("reference_run" in problem for problem in problems):
            out("[PASS] selftest · vacuum_run without reference_run rejected")
        else:
            ok = False
            out("[FAIL] selftest · vacuum_run without reference_run was accepted")
    return ok


def main(argv):
    if len(argv) >= 2 and argv[0] == "check":
        return 1 if check(argv[1:]) else 0
    if argv[:1] == ["selftest"]:
        return 0 if selftest() else 1
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
