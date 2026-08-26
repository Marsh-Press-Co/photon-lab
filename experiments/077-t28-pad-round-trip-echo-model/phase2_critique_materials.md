# PHASE 2 — CRITIQUE · MATERIALS & METAMATERIALS seat · Panel Iteration 54 (exp-077)

*Fresh sub-agent, blind to the other six seats' critiques this cycle. Charter
(PANEL.md, verbatim): "sub-wavelength structure; what could physically
realize the proposed optical behavior. Owns the realizability bound
(published / plausible / unobtainium-with-parameters)."*

---

## Steel-man (≤150 words)

This cycle earns its own realizability bookkeeping rather than inheriting it
blind. It correctly reuses exp-075's mandatory Phase-2 fix (Idealization 2:
`Z(x,θ)=n(x)/√(n(x)²−sin²θ)` is the admittance of a matched `eps=mu` medium,
`published/plausible only as microwave RAM, UNOBTAINIUM-WITH-PARAMETERS at
450–750nm`) by explicit reference (§6, "the matched-`eps=mu` friction-PDE
bridge and its realizability caveat... carry over UNCHANGED") rather than
silently dropping it — I checked and it was NOT dropped. It also independently
re-derives, not merely cites, `PAD`'s lossless-vacuum status by reading
`fdtd2d.py::Sim.__init__`'s missing `pad` argument directly (§2b), which is
the correct materials-adjacent fact this cycle's whole premise rests on: zero
material content changes between `C40`/`G40`, so nothing here can be, or is
claimed to be, a coating/absorption finding. Idealization 9 discloses rather
than hides the uncomputed far-wall contribution.

## Sharpest attack (≤150 words)

Idealization 9 frames the omitted `+x`-wall echo as a missing geometric term
("D_right 59→99... a second, uncomputed contribution"). It is not merely
that. I verified `lab/fdtd2d.py::_damping` (lines 122-128) applies the
*identical* `self.absorb`-parameterized cubic ramp to all four edges — so
the `+x` wall for `C40`/`G40` is built from the exact same unrealizable
matched-`eps=mu` admittance class as the `-x` wall this cycle already
scopes. The already-built, "zero new machinery" `two_wall_cavity.py` fix
this document offers as a hedge does not move the model one step closer to
anything physically buildable — it doubles the artifact's footprint. Neither
this REFUTE nor a hypothetical two-wall SUPPORT licenses any claim about a
real, `μ=1` graded-loss interface: the realizability bound for this entire
mechanism *class* stays fixed at unobtainium-with-parameters (exp-075), and
`PAIR_PAD`'s own mechanism (proven lossless-vacuum geometry) never engages a
materials question at all. §5's "narrows the remaining space" language
should say so explicitly — a future LOGBOOK reader could otherwise read a
two-wall SUPPORT as materials progress it structurally cannot be.

## Verdict: **support-with-changes**

The computation is R4-clean (I independently re-ran
`pad_round_trip_model.py`: `rel_dev_PAD=1.8798`, `r²_PAD=0.0444`, both
REFUTE, bit-identical to the document; `D_right=59/99/99` for `C40/G40/C80`
reproduces from `two_wall_cavity.py`'s own `d_right=(nx-1)-src_x` formula).
The realizability caveat this seat required at exp-075 is correctly
inherited, not silently lost. My objection is scope, not arithmetic: the
document should state, in one sentence next to the §6 Idealization-9 hedge,
that the `+x` wall's own boundary is built from the identical unrealizable
admittance class as the `-x` wall (verified above), so the offered two-wall
extension is available as an *instrument-fidelity* check only — it cannot
narrow, in either direction, what MATERIALS bounds as buildable at optical λ.

## Parameter/scope change that would flip verdict to support

Add one sentence to Idealization 9 (or a new Idealization 10) stating that
`fdtd2d.py::_damping`'s symmetric construction means the `+x` wall shares
`-x`'s matched-`eps=mu`/unobtainium status, and that any future two-wall
re-target of this model changes only which numerical artifact is being
fitted, never the realizability verdict on the mechanism class. No
recomputation needed — the REFUTE stands either way.
