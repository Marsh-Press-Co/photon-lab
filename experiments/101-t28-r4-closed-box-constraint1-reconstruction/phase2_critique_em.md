# Phase 2 Critique — ELECTROMAGNETISM seat
## exp-101 / Panel Iteration 78

All claims below independently re-derived from source: `lab/sections.py`
read in full (`_face_flux`, `widths`); `experiments/087-.../run.py:123-168`
(`widths_direction_corrected`, defining function of the chain re-exported
through exp-088/091/094) read in full; `experiments/100-.../run.py`'s
`plane_x_behind`/`observer_record_t28` read for the bench's own stated
face convention.

## 1. Steel-man (≤150 words)

Pure instrument fidelity, zero mechanism, zero `lab/` diff, reusing a
stage-8-gated primitive exactly as built. The face-labeling claim is also
*independently confirmable from the raw Sx convention*, not just by
analogy: `_face_flux`'s `sx(xf) = -0.5·Re{Ez·conj(Hy)}` is the physical
`<Sx>` density: `p_back = -Σsx(x0)` is exactly the box's outward flux
through its low-x face; `p_fwd = Σsx(x1)` is the outward flux through its
high-x face. This bench's own `plane_x_behind()` (exp-100) already calls
the low-x side "downstream" for this exact `src_x>obj_x>plane_x` geometry.
So `back_frac`'s low-x-built numerator genuinely does read the downstream
scattered fraction here — the proposal's bottom-line claim survives an
independent re-derivation, not merely trust in precedent. The box-
independence due-diligence check on the new derived scalar is appropriate
and proportionate.

## 2. Sharpest attack (≤150 words)

The proposal's own stated *warrant* for the relabeling is false, verified
against source. It claims `back_frac`/`fwd_frac`'s reinterpretation is
"the same reinterpretation already established for `sigma_scat/abs/ext`
(`widths_direction_corrected`)." Reading that function in full
(`experiments/087-.../run.py:123-168`) shows it does something unrelated:
it multiplies `sigma_scat`/`sigma_abs`/`sigma_ext`/`sigma_ext_cross` by
`sign(i_inc)` to fix a *normalization-magnitude* artifact (a signed
reference-strip flux), and its own `dict(w)` copy leaves `back_frac`/
`fwd_frac` untouched — they never depended on `i_inc`'s sign at all
(`back_frac`'s denominator is raw `p_scat`, not `sigma_scat`). Citing it
as precedent for a *face-direction* relabeling is a non-sequitur; the
actually-apt precedent (`observer_record_t28`'s scalar swap) sits right
next to it in the same sentence, uninterrogated. This is exactly the
"asserted by analogy" failure LOGBOOK has caught before (T20/T21) — it
happens to land on a correct conclusion here only because the geometric
fact (§1) independently holds, not because the cited precedent supports it.

## 3. Verdict

**support-with-changes.**

## 4. Parameter change that would flip to unconditional support

Replace the false citation with the actual warrant (the `_face_flux`
Sx-face correspondence + `plane_x_behind`'s own low-x="downstream"
convention, cross-checked against `observer_record_t28` alone — drop
`widths_direction_corrected` from that sentence), **and** add an explicit
per-cell floor/non-negativity gate on `p_scat` (the shared, unclamped
`back_frac`/`fwd_frac` denominator only floored at `1e-30`) before trusting
either fraction — `sigma_abs` has a stated non-negativity gate in §4;
`sigma_scat` does not, and nothing in the proposal establishes it stays
comfortably positive per angle/config rather than merely on the
aggregate `ratio_abs_ext_raw` average. Absent that gate, an unlucky
cell with small/negative raw `p_scat` produces an unbounded, silently
wrong `back_frac`/`fwd_frac` that the box-independence check (§2.5) would
not reliably catch, since both BOX_A and BOX_B would suffer the same
denominator pathology together.
