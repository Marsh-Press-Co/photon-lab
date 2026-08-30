# PHASE 2 — CRITIQUE · Seat: THERMODYNAMICS · Panel Iteration 69 · exp-092

Fresh sub-agent, blind to any other seat's current-cycle critique. Read in
full: `PANEL.md`; `LOGBOOK.md` in full; `experiments/092-.../phase1_proposal.md`
(this cycle's frozen proposal); the complete exp-091 record, especially
`phase5_review_thermodynamics.md` (my own prior-cycle review) and
`results.json`'s `thermo`/`p_abs_w`/NETD fields; `lab/thermo_sidecar.py` in
full; exp-091's `run.py` for the `p_abs_w`/`frac_p_abs` wiring via
`ratio_abs_ext`/`sigma_ext`.

## Steel-man (≤150 words)

Rank 3 is this program's first attempt to test whether the `sigma_max`
confound — a real ~1.5× optical-depth inflation MATERIALS' own exp-091
self-review found (`τ_center` 78→117 at R3, unscaled `sigma_max=0.5`) —
contaminates the PRIMARY `delta_scene`/`frac_contrast`/`ratio_k` channel,
not only the already-checked bulk `p_abs_w`. The design correctly isolates
the variable: both legs sit at `cpl=30`, varying only `sigma_max`
(0.5→1/3), so nothing conflates resolution with the material change the
way exp-091's own native-vs-R3 comparison did. `sigma_max_R3=1/3` is
exactly, not approximately, derived from this program's own established
`τ_center=2σr_out(cells)` convention (the SIGMA_ON/T10 precedent), reuses
`absorbed_power_established_ratio`/`mixed_length_scale_regime` unmodified,
and closes the exact open question MATERIALS ranked #2 for this iteration.
Six calls, zero new machinery — a cheap, well-targeted closure of a named,
load-bearing gap.

## Sharpest attack (≤150 words)

§4b recomputes `p_abs_w`/`frac_p_abs` as a mere "byproduct," and §6 sets
**no CONFIRM/REFUTE band for either** — only `delta_scene`/`frac_contrast`
are scored. That is a real regression from exp-091's own (b2), which made
`frac_p_abs` a co-equal PRIMARY prediction precisely because it is R14's
own numerator hazard. Unlike exp-091's tangled confound, Rank 3 isolates a
genuine 33% reduction in the absorber's own conductivity at fixed `cpl` —
squarely THERMO's domain, and directionally predictable from this
program's own established anchor (T9's `ratio_abs_ext≈0.51` near-
saturation, which MATERIALS' own exp-091 review already used to argue the
effect should be modest, not the naive ~1.5×-in-σ swing). A falsifiable
band was cheap and available; none was pre-registered. Any energy-channel
surprise this cycle produces lands unscored — the "argued, not banded" gap
R4/R8 exist to prevent — and Idealization 3's banner, inherited verbatim
from a pure-resolution cycle, never discloses that Rank 3 is a real
material-parameter test, not a grid-refinement check.

## Verdict: **support-with-changes**

## Parameter change that would flip my verdict to full support

Add a pre-registered CONFIRM/REFUTE band for `p_abs_w` and `ratio_abs_ext`
under Rank 3 before Phase 4 runs — e.g. mirroring exp-091's own (b2):
`p_abs_w(sigma-corrected)/p_abs_w(as-filed exp-091)` ratio ∈ `[0.3,3.0]`
CONFIRM (sign/direction stated: a *decrease* toward the native-`cpl=20`
value is the directional lean, since T9's flat ~0.51 anchor argues the
effect should track resolution-only staircasing, not scale linearly with
the 33% σ cut), plus an explicit `ratio_abs_ext` stability band
(e.g. within ~2–3% of T9's established 0.51, matching R14's own
demonstrated flatness). Zero additional FDTD calls are needed — both
quantities are already computed as a byproduct of the same 6 calls.
