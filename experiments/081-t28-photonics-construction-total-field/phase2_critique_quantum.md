# PHASE 2 — CRITIQUE · QUANTUM OPTICS (fresh, blind to other Phase-2 seats) · Panel Iteration 58 · exp-081

*Fresh sub-agent, QUANTUM OPTICS charter (PANEL.md seat 5): non-classical
absorption, state-dependent or coherent interactions; expressibility
contract — mechanisms enter the bench only as effective classical
parameters, or Red Team strikes them. This is instrument/model-fidelity
work, T1 route N/A — no mechanism is being proposed for the phenomenon
program itself. I have no memory of the exp-080 Phase-2/Phase-5 QUANTUM
instances that flagged the two defects this cycle claims to fix; I read
the whole chain cold and independently verified it against the code.*

**No RULED-OUT item (R1–R9) is re-proposed or re-litigated here.**

---

## Independent verification performed

Read `experiments/080-.../phase5_review_quantum.md` and
`phase5_review_photonics.md` in full (the sources of both defects this
cycle claims to fix), traced the import chain
(`photonics_construction.py` → `y_wall_aperture_sum.py` →
`y_wall_prescreen.py` → `experiments/069-.../run.py::_free_period_search`/
`_fixed_period_fit`) confirming `_free_period_search`/
`free_period_with_widening`/`score_period`/`SS_TOT_DEGENERATE_FLOOR` are
imported verbatim at every hop, never reimplemented — no subtle-bug risk
here. Confirmed `dist_direct_cells` (`hypot(D_SP, OBJ_Y−y_s)`) matches
PHOTONICS' own exp-080 Phase-5 formula character-for-character, distinct
from `dist_image_cells` (`OBJ_Y+y_s`) only by the sign on `y_s`, and that
`e_direct_curve` reuses `aperture_amplitude`/`source_driven_phase` (generic
per-point aperture functions, independent of any wall) correctly. Recomputed
item 1c's own table from `phase1_results.json` and checked whether
"closer to T21 than T28" survives if measured in raw degrees instead of
`rel_dev`: it does (absolute gaps to T21 are 0.05–0.10° vs. 0.83–2.75° to
the real targets) — the finding is not an artifact of `rel_dev`'s two
different-magnitude denominators, and if anything T21's smaller denominator
should have worked against, not for, this conclusion.

---

## Steel-man (≤150 words)

This cycle delivers exactly what nine T28 cycles have been missing:
PHOTONICS' construction built and scored as originally specified.
`E_direct`'s PAD-invariance is re-verified bit-exact (item 1a), and the
correct free-period-search machinery replaces exp-080's mistaken
R²-against-a-candidate-curve methodology — both compounding defects I (as
QUANTUM) flagged at exp-080 Phase 5 are genuinely closed, not merely
relabeled; I independently confirmed both fixes against the code myself,
not by trusting the write-up. The self-falsification of the literal
"bit-identical" item-1b prediction (`~10⁻¹⁴`, not `0.0`) is disclosed
honestly and correctly traced to floating-point subtraction of two `O(100)`
values, not smoothed over. THERMODYNAMICS' energy-budget refinement
(116,000× tighter bound under the physically-correct angle convention) is a
genuine, independent, load-bearing finding. R4 provenance is clean
throughout — I recomputed several numbers myself and they match to the
printed digit.

---

## Sharpest attack (≤150 words)

Item 1c's `rel_dev` comparison is mathematically sound — verified above,
it is not an R9-style unit mismatch and is robust to which reference has
the larger magnitude. But it is missing the specific control THIS
sub-thread's own Red Team precedent (exp-079, cited by this cycle as
established discipline) ruled is the "mechanism-appropriate resolution"
for exactly this look-elsewhere shape: a reflectance-ablation control
(`r(90°−θ_beam)→1`, re-fit). Since item 1a proves `E_direct` cancels to
float noise, item 1c's recovered periods come entirely from `E_image` — but
nothing here tests whether `W(θ_beam)` alone, sharing the identical
driven-phase ramp that produces T21's fringe everywhere else in this
program, would ALSO land near T21 with zero wall physics. Without that
ablation, "closer to T21 than T28" cannot distinguish a genuine finding
about `r()` from geometry leaking through the unweighted sum — exactly the
trap exp-079's own ablation control was built to catch for a structurally
similar object. This gap feeds directly into the "REFUTE-leaning" language
this cycle's own Next section uses to inform Checkpoint-2/Iteration-59
framing, uncalibrated.

---

## Verdict: **support-with-changes**

The mechanically pre-registered Combined Verdict (NEITHER) and the primary
build (item 1: `E_direct`+`E_image`, correct methodology) are sound,
independently verified, and should stand unchanged. What should not yet
stand unchanged is the cycle's own "substantive REFUTE-leaning reading"
being carried into Iteration-59 framing/Checkpoint-2 deliberation as if it
were as load-bearing as the pre-registered result — it rests on a disclosed
but uncalibrated post-hoc diagnostic that this exact sub-thread's own prior
cycle showed needs a mechanism-appropriate ablation control, not a bare
distance-to-reference comparison, before it counts as more than a hint.

**Single parameter change that would flip my verdict to full support**: run
the reflectance-ablation control (`r(90°−θ_beam)→1` in `E_image`, re-fit
the same three pair-deltas via the same imported machinery) on this cycle's
own `E_total` construction before the "REFUTE-leaning" reading is used in
Iteration 59's ranking language. If the ablated periods are statistically
distinguishable from the `r`-weighted ones (i.e., the T21-proximity is
NOT wall-physics-independent), that sharpens rather than weakens this
cycle's own finding and I would support fully.
