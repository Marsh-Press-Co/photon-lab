# PHASE 2 — CRITIQUE (ELECTROMAGNETISM) · Panel Iteration 68 · exp-091

## Steel-man (≤150 words)

The G40_R3 congruence argument is genuinely EM-sound, not merely
cell-count bookkeeping. Every physical length this cycle touches —
`BOX_CLEARANCE_A/B` (12/24→18/36 cells), `REF_HALF_H` (80→120),
`R_OUT`, `A` — scales by exactly `R3_RATIO=1.5` while `DX_M` shrinks by
2/3 (30nm→20nm at cpl 20→30), so physical distance is held *exactly*
fixed: `12×30nm = 18×20nm = 360nm = 0.6λ` in both resolutions, confirmed
independently by the proposal's own `L_GEOMETRIC_M` identity (§2a). This
is the textbook grid-refinement design — isolate discretization error by
holding physical geometry constant, not by holding cell counts constant —
and it correctly reuses `sections.py::widths()` unmodified. The
Poynting-box channel (`p_abs_w`, feeding `ratio_k`'s numerator) is also
the *more* trustworthy half of this check: VALIDATION.md's own lesson
and T10's resolved history establish that closed-surface flux integrals
are far less resolution-fragile than point/field-probe channels — this
cycle's box-ledger leg is measuring exactly the kind of quantity R3
checks have historically confirmed cleanly (exp-005/010/015/023/025), not
the kind that surprised (T10's near-field envelope channel).

## Sharpest attack (≤150 words)

`frac_contrast`/`delta_scene` is not the resolution-robust flux-box
channel — it is `lab/ambient.py`'s point/field-based Weber-contrast
fringe, independently proven by T21 to be a genuine Huygens
edge-diffraction interference pattern whose period sits near this
program's own Nyquist regime, and by T10 to be a class of near-field
measurement that resolution refinement can *enlarge*, not just confirm
or null (T10's headline: 46%→128% spread under cpl×1.5, before the
SIGMA_ON confound reduced but did not zero a residual). `FLOOR=
1.91744×10⁻⁴` is the RMS of that fringe *at cpl=20*, which implicitly
encodes cpl=20's own zero-crossing locations. 40.2°/41.4° were chosen
*because* they sit 0.065°/0.061° from a crossing at cpl=20 — so testing
whether `ratio_k`'s classification survives cpl=30 with the *old* FLOOR
tests whether the crossing has moved using a threshold whose own
validity presumes it hasn't. That is circular, not the "disclosed
mixed-resolution comparison" Idealization 6 frames it as: a genuine
resolution-driven node shift at these two specific points would present
indistinguishably from a `ratio_k` classification flip, and the design
has no way to tell the two apart.

## Verdict

**support-with-changes**

## Parameter change that would flip verdict

Add 2–4 cheap `cpl=30` `PAIR_PAD` points bracketing 40.2°/41.4° at
±0.1–0.2° (mirroring exp-088's own bracketing idiom), sufficient to
directly locate the cpl=30 `delta_scene` zero-crossings near those two
angles from data rather than inferring crossing-stability indirectly
through the old FLOOR. That converts §4b's classification question from
"does an old-resolution threshold still fire" into a direct, resolution-
native measurement of whether the crossing itself moved — cheap (4–8
more calls) against this cycle's own 78.5 CPU-min budget, and it would
let (a)'s CONFIRM/REFUTE band and (b)'s classification question be read
as independent tests of the same physics rather than one masking the
other.
