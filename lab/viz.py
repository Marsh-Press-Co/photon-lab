"""Viz lane: artifact -> pixels. Never physics-correctness-bearing (lab/ARTIFACTS.md).

Renders the exp-001 witness figure per house style R1-R4 (PLAN.md, ratified
2026-08-09): shadows self-explain, orientation gizmo, panels work solo,
witness view beside the map.
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrow, Rectangle

SCENE_COLORS = {"reflector": "#4C78A8", "absorber": "#222222", "cloak": "#E45756"}
SCENE_LABELS = {"reflector": "reflector (bare metal)", "absorber": "absorber (designed sponge)", "cloak": "cloak (reduced shell)"}


def load_artifact(exp_dir: Path, scene: str, lam_nm: int) -> tuple[dict, dict]:
    art_dir = exp_dir / "artifacts" / f"{scene}-{lam_nm}nm"
    fields = np.load(art_dir / "fields.npz")
    manifest = json.loads((art_dir / "manifest.json").read_text())
    return dict(fields), manifest


def envelope(fields: dict) -> np.ndarray:
    """|E| envelope from the quadrature pair (viz-side derivation, ARTIFACTS.md)."""
    return np.sqrt(fields["ez_snapshot"] ** 2 + fields["ez_quarter"] ** 2)


def _draw_map_panel(ax, fields: dict, manifest: dict, scene: str, beam_behind: float, lam_nm: int) -> None:
    """One field map. Must work solo (R3): own title, own colorbar, own gizmo, own annotation."""
    env = envelope(fields)
    nx, ny = env.shape
    im = ax.imshow(
        env.T, origin="lower", cmap="inferno", extent=[0, nx, 0, ny],
        vmin=0, vmax=np.percentile(env, 99.5),
    )
    cb = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.03)
    cb.set_label("|E| envelope (arb.)", fontsize=8)
    cb.ax.tick_params(labelsize=7)

    # Geometry outline -- R1 shadows self-explain: label what's making the dark region,
    # don't leave it to be inferred.
    for obj in manifest["objects"]:
        p = obj["params"]
        if obj["type"] == "pec_disk":
            ax.add_patch(Circle((p["cx"], p["cy"]), p["r"], fill=False, edgecolor="cyan", lw=1.2))
            ax.annotate("PEC core", (p["cx"], p["cy"] - p["r"] - 6), color="cyan",
                        fontsize=7, ha="center", va="top")
        elif "r_out" in p:
            ax.add_patch(Circle((p["cx"], p["cy"]), p["r_out"], fill=False,
                                 edgecolor="white", lw=1.0, linestyle="--"))
            label = "absorber shell" if obj["type"] == "graded_black_shell" else "cloak shell"
            ax.annotate(label, (p["cx"], p["cy"] + p["r_out"] + 6), color="white",
                        fontsize=7, ha="center", va="bottom")

    # Orientation gizmo (R2): beam direction + where the witness/camera stands.
    src = manifest["sources"][0]
    obs_x = manifest["observer"]["plane_x"]
    ax.add_patch(FancyArrow(6, ny - 20, 34, 0, width=2, head_width=8, head_length=10,
                             color="#4C78A8", length_includes_head=True))
    ax.annotate("beam", (24, ny - 32), color="#4C78A8", fontsize=7, ha="center")
    ax.axvline(obs_x, color="#4C78A8", lw=0.8, linestyle=":")
    ax.annotate("witness /\ncamera", (obs_x, 8), color="#4C78A8", fontsize=6.5, ha="center", va="bottom")

    # Beam-behind measurement box: fixed downstream region, past every dressing,
    # value pulled from the committed, Evidence-Gated results (not recomputed here).
    obj_max_x = max(p["params"].get("r_out", p["params"].get("r", 0)) + p["params"]["cx"]
                     for p in manifest["objects"])
    box_x0 = min(obj_max_x + 20, nx - 60)
    ax.add_patch(Rectangle((box_x0, ny * 0.42), 40, ny * 0.16, fill=False,
                            edgecolor="lime", lw=1.2))
    ax.annotate(f"beam-behind\n{beam_behind:.3f}", (box_x0 + 20, ny * 0.42 - 10),
                color="lime", fontsize=7.5, ha="center", va="top", weight="bold")

    ax.set_title(f"{SCENE_LABELS[scene]} @ {lam_nm}nm", fontsize=9.5)
    ax.set_xticks([]); ax.set_yticks([])


def _draw_sweep_panel(ax, results: dict, metric: str, ylabel: str, title: str) -> None:
    """One measurement vs wavelength, all three scenes. Works solo (R3): legend in-panel."""
    lambdas = [450, 600, 750]
    for scene in ("reflector", "absorber", "cloak"):
        ys = [results[f"{scene}-{lam}"][metric] for lam in lambdas]
        ax.plot(lambdas, ys, marker="o", color=SCENE_COLORS[scene], label=scene, lw=1.8)
    ax.set_xlabel("wavelength (nm)", fontsize=8)
    ax.set_ylabel(ylabel, fontsize=8)
    ax.set_title(title, fontsize=9.5)
    ax.tick_params(labelsize=7)
    ax.legend(fontsize=7, loc="best", framealpha=0.9)
    ax.grid(alpha=0.25)


def render_witness_figure(exp_dir: Path, out_path: Path) -> Path:
    results = json.loads((exp_dir / "results.json").read_text())
    fig, axes = plt.subplots(2, 3, figsize=(13, 8))

    for col, scene in enumerate(("reflector", "absorber", "cloak")):
        fields, manifest = load_artifact(exp_dir, scene, 600)
        _draw_map_panel(axes[0, col], fields, manifest, scene, results[f"{scene}-600"]["beam_behind"], 600)

    _draw_sweep_panel(axes[1, 0], results, "observer_return", "observer return (backward flux)",
                       "Does light come back to the witness?")
    _draw_sweep_panel(axes[1, 1], results, "beam_behind", "beam-behind (intensity ratio)",
                       "Does the beam continue past the object?")
    _draw_sweep_panel(axes[1, 2], results, "scattered_rms", "scattered RMS (annulus)",
                       "How loudly does the object announce itself?")

    fig.suptitle(
        "exp-001 — The Flashlight Statement: which object matches \"stopped about 50 yards "
        "away on nothing in particular\"?", fontsize=11.5, y=0.995,
    )
    fig.text(
        0.5, 0.005,
        "Note: \"scattered RMS\" conflates shadow-casting with glint — the absorber scores highest here by\n"
        "casting an enormous shadow, not by radiating light. It does not distinguish \"invisible because dark\"\n"
        "from \"invisible because loud in every direction\" (NOTES.md); exp-002 separates the two.",
        ha="center", va="bottom", fontsize=8, style="italic", color="#444444",
    )
    fig.tight_layout(rect=[0, 0.045, 1, 0.97])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=160)
    plt.close(fig)
    return out_path


if __name__ == "__main__":
    exp = Path(__file__).resolve().parent.parent / "experiments" / "001-flashlight-statement"
    out = exp / "figures" / "witness-figure.png"
    render_witness_figure(exp, out)
    print(f"wrote {out}")
