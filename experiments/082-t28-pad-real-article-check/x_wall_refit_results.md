# Tier 0 item 1 — x-wall realizable-admittance refit: RESULT

PLAN.md Iteration-59 queue Tier 0 item 1 (MATERIALS' restored item, exp-081
`phase5_redteam_audit.md` §0.8/§4/§6): "restore or explicitly retire the
x-wall realizable-admittance refit (reuse
`d80.reflection_coefficient_vec_realizable` against the already-built
exp-075/exp-077 x-wall models, or state why their already-wide REFUTE
margins make that unnecessary)."

**Disposition: RESTORED AND RUN, not retired.** Ran `x_wall_realizable_
refit.py` (zero new FDTD, reuses `experiments/077-.../pad_round_trip_
model.py`'s own `load_pair_geometries`/`predicted_c_empty`/`predicted_
c_empty_two_wall`/`free_period_with_widening` and `experiments/080-.../
validity_precheck.py`'s `reflection_coefficient_vec_realizable`
unmodified). Full output: `x_wall_output.txt`, `x_wall_realizable_
refit_results.json`.

## Result

Phase divergence `arg(r_matched)−arg(r_realizable)` over θ∈[36°,42°]:
`ABSORB=40`: 18.25°–24.66°; `ABSORB=80`: 0.47°–15.01°. Materially larger
than exp-081's own item-1 divergence at its `[48°,54°]` grazing range
(8.4°–10.6°) — this program's own established pattern (exp-080 part(b)):
the two admittance families diverge more sharply nearer normal incidence,
less at grazing.

| model | pair | matched `rel_dev` | matched `r²` | matched verdict | realizable `rel_dev` | realizable `r²` | realizable verdict |
|---|---|---|---|---|---|---|---|
| single-wall | PAIR_PAD | 1.8798 | 0.0444 | REFUTE | 0.6682 | 0.0011 | REFUTE |
| single-wall | PAIR_ABSORB40 | 0.9642 | 0.1997 | **INCONCLUSIVE** | 0.5893 | 0.0389 | **REFUTE** |
| two-wall (primary) | PAIR_PAD | 0.8797 | 0.0001 | **REFUTE** | 0.4653 | 0.0590 | **INCONCLUSIVE** |
| two-wall (primary) | PAIR_ABSORB40 | 0.6851 | 0.0418 | REFUTE | 0.4527 | 0.0089 | REFUTE |

**2 of 4 cells flip** — this differs from exp-081's own item-1 finding
(zero flips at its own grazing-incidence range) precisely because this
range sits closer to normal incidence, where the admittance families are
known to diverge more (table above). **Neither flip produces a SUPPORT.**
The x-wall single-wall and two-wall coherent-echo models remain REFUTE- or
INCONCLUSIVE-only under the realizable (`μ_r=1`, the only admittance family
that could ever describe a real material) admittance family, exactly as
under the matched family — the sub-thread's own REFUTE-leaning picture for
this mechanism class is **not overturned**, though it is no longer
uniformly this-clean in every cell (`rel_dev`s shrink toward the REFUTE/
INCONCLUSIVE boundary rather than growing away from it, in 3 of 4 cells).

**Self-scored disposition: the item is now closed for this cycle** — run,
not merely restored to the board. No further action queued unless a future
cycle wants the full 3-λ leg on this same refit (Tier 1 item 8's own
existing scope already covers wavelength generality for this model family).
