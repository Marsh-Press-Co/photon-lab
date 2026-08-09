# Run artifacts — the solver ↔ viz contract (schema 0.1.0)

The boundary agreed on co-lab #31: anything with physics-correctness stakes
is computed solver-side in `lab/` where the trust suite can validate it;
everything from **artifact → pixels** is the viz lane. This file pins what
crosses the boundary. The emitter (solver lane) and the consumer (viz lane)
both hold veto over changes here; changes bump `schema_version`.

Evidence Gate (#28/#29): every published figure regenerates deterministically
from a committed artifact. The manifest carries a sha256 of the field file so
the gate anchors on content, and `python -m lab.artifacts check` validates
loudly — it reports every check it ran, because a silent gate and an absent
gate produce identical observations.

## Layout

One artifact = one directory (one scene of one experiment):

    experiments/NNN-slug/artifacts/<scene>/
        fields.npz       arrays (compressed)
        manifest.json    everything else + sha256 of fields.npz

## fields.npz

| Array | Shape | Dtype | Presence |
|---|---|---|---|
| `ez_snapshot` | (nx, ny) | float32/64 | required |
| `ez_quarter` | (nx, ny) | float32/64 | required |
| `eps_r` | (nx, ny) | float32/64 | required |
| `sigma_e` | (nx, ny) | float32/64 | required |
| `pec_mask` | (nx, ny) | bool | required |
| `inv_mu_xx` | (nx, ny−1) | float32/64 | tensor scenes only |
| `inv_mu_yy` | (nx−1, ny) | float32/64 | tensor scenes only |
| `inv_mu_xy_hx` | (nx, ny−1) | float32/64 | tensor scenes only |
| `inv_mu_xy_hy` | (nx−1, ny) | float32/64 | tensor scenes only |
| `obs_angles_rad` | (n,) | float | observer scenes only |
| `obs_return_flux` | (n,) | float | observer scenes only |

- `ez_snapshot` / `ez_quarter` are the steady-state pair a quarter period
  apart, exactly what `Sim.envelope()` combines; the |E| envelope is a
  viz-side derivation (`sqrt(a² + b²)`), never stored.
- The four `inv_mu_*` arrays mirror `Sim.inv_mu` at the staggered H
  locations. All four or none.
- **Observer record (pinned):** `obs_angles_rad` are bin centers in radians
  measured at the observer plane (0 = straight back toward the source along
  −x, +CCW), strictly increasing; `obs_return_flux` is time-averaged
  Poynting flux **integrated within each bin** — the sum over bins equals
  the total returned flux under `manifest.observer.normalization` — *not* a
  per-radian density. Both or neither, same length. The flux *semantics*
  (extraction plane, windowing, normalization physics) are solver-lane and
  validated by the trust suite; this schema only fixes the container.

## manifest.json

| Key | Type | Notes |
|---|---|---|
| `schema_version` | str | this document: `"0.1.0"` |
| `experiment` | str | e.g. `"exp-001"` |
| `scene` | str | e.g. `"cloaked"`, `"bare-pec"`, `"empty"` |
| `created_utc` | str | ISO 8601 |
| `engine_commit` | str | git SHA of `lab/` that produced the run |
| `suite_status` | str | trust-suite state at emit time, e.g. `"14/14"` |
| `lambda_nm` | number | physical wavelength the scene represents |
| `grid` | obj | `nx, ny, cells_per_lambda, courant_frac, absorb` |
| `run` | obj | `steps, snapshot_step, quarter_offset_steps` |
| `sources` | list | per source: `profile` (`"plane"`/`"gauss"`), `x`, `y_lo`, `y_hi`, `ramp_periods`, `amplitude`, `width` (gauss), `edge` (plane) — mirrors `add_line_source` |
| `objects` | list | `{type, params}`; `type` is the `lab.materials` builder name, `params` mirror its exact signature (see table below) |
| `observer` | obj | only with observer arrays: `plane_x`, `start_step`, `normalization` (`"vacuum_run"`/`"incident_power"`), `reference_run` — non-null (the vacuum run's artifact path) **iff** normalization is `"vacuum_run"`, else null: a vacuum-normalized figure must be regenerable deterministically |
| `npz_sha256` | str | sha256 hex of `fields.npz` — the Evidence Gate anchor |
| `provenance` | list | typed refs, may be empty — see below |

### objects[].params by type

| type | required | optional |
|---|---|---|
| `dielectric_cylinder` | cx, cy, r, eps_r | — |
| `pec_disk` | cx, cy, r | — |
| `absorber_shell_stub` | cx, cy, r_in, r_out | sigma_max, eps_max |
| `schurig_reduced_cloak_tm` | cx, cy, r1, r2 | mu_r_floor |

New material builders add a row here (schema bump: minor).

### provenance[] — typed refs, not free-form

    { "kind": "witness-statement" | "document" | "experiment" | "paper" | "url",
      "id": "...", "page": 12, "url": "...", "note": "..." }

`kind` + `id` required, rest optional. This is the Disclosure-annex door:
e.g. `{"kind": "witness-statement",
"id": "pursue-r1--western_us_event_slides_5.08.2026", "page": N}` lets an
incident page cite the experiment mechanically, and the figure cite back.

## Storage dtype (decided in PR #1 review)

**float32 for stored fields.** Rendering never needs float64; solver
precision stays in-memory solver-side; `npz_sha256` anchors the gate on
bytes either way. The validator accepts float32/float64 so old artifacts
never rot; the emitter writes float32.

## Checking

    python -m lab.artifacts check experiments/*/artifacts/*
    python -m lab.artifacts selftest

`check` exits non-zero on any failure and prints one line per check group
per run — liveness by construction.
