# Panel Iteration 78 (exp-101) — Phase 2 Critique: MATERIALS & METAMATERIALS

*Fresh-context seat. Blind to all other seats' current-cycle critiques, per
PANEL.md independence mechanics. Speaking only from this discipline's
charter: sub-wavelength structure / what could physically realize the
proposed optical behavior; owns the realizability bound (published /
plausible / unobtainium-with-parameters). No RULED-OUT idea (LOGBOOK.md
registry, read in full) is re-proposed below.*

**Charter-fit note, stated up front rather than manufactured around:** this
cycle proposes zero new material or mechanism — `graded_black_shell` +
`pec_disk`, same `sigma_max` (`SIGMA_R4_CORRECTED=0.25`, re-verified this
session at `experiments/069-.../design_geometry.py:300`, gate-checked
`==0.25` at every downstream site from exp-094 through exp-100), same
geometry. That article already carries a locked realizability verdict
(**UNOBTANIUM-WITH-PARAMETERS**, `experiments/034-.../REALIZABILITY_MEMO.md`
Amendments 6–7, exp-061/062, "more robustly overdetermined than at any prior
point in this program's history" — four independent real-material
comparator classes checked, none clearing the joint rate/thickness bar).
This proposal touches none of that. My charter's realizability bound
genuinely has almost nothing new to bite on here; I verified `lab/materials.py`,
`lab/sections.py`, and the `R4_CONFIGS`/`SIGMA_R4_CORRECTED` chain directly
rather than assume this, and confirm it.

## 1. Steel-man (charter perspective)

Instrument fidelity IS a realizability-adjacent duty: my charter's tier
calls (RSA/TPA/CNT-forest/NiP-black/aerogel, `REALIZABILITY_MEMO.md`) all
rest on this bench's own measured optical quantities being trustworthy. A
broken `beam_behind_t28` reading (0.42–0.46, established uninterpretable)
sitting next to a locked UNOBTANIUM verdict would eventually invite someone
to cite the wrong instrument's number against a materials question it was
never fit to answer. This fix touches zero material parameters — I
independently confirmed `lab/sections.py::widths()` is unmodified and
`graded_black_shell`'s `sigma_max`/`eps_max` defaults are untouched — so it
carries zero realizability risk of its own while protecting the integrity
of data that future MATERIALS charter work will eventually have to use.
Reusing already-gated `box_for_r4`/`ref_for_r4`/`widths_direction_corrected`
verbatim, rather than inventing new geometry, is the correct discipline for
a cycle with no material change to justify one.

## 2. Sharpest attack

Falsifiable Prediction 1 sets the confirmatory band `sigma_abs/sigma_ext ∈
[0.505, 0.520]` — **entirely above 0.5** — citing it as consistent with "the
T9 anchor (0.51)." I read T9 in full (LOGBOOK.md line 1161): it explicitly
states this exact figure **EXCEEDS the idealized geometric-optics ceiling
(σ_abs/σ_ext ≤ 0.5, a Babinet/shadow-formation bound for any perfectly-black
object, independent of interior structure)**, is **"not an asymptotic
material constant,"** and is attributed to the box sitting deep in the
near/Rayleigh zone (T8), not to any real absorptivity a material could
have. Prediction 1 cites "the T9 anchor" as a bare numeric precedent without
once restating T9's own disclaimer — a number that structurally cannot
describe any real perfectly-black material's far-field absorption ratio is
about to be re-confirmed, again, as an unremarkable expected outcome. If
this band lands in NOTES.md's Result prose bare (as R16/R21 discipline
would otherwise commit it), a future realizability check citing "0.51"
without T9's caveat would be citing a near-field artifact as if it were a
material property — exactly my seat's charter to prevent.

## 3. Verdict

**Support-with-changes.**

## 4. Parameter change to flip to full support

Not a numeric parameter — a one-line addition to §5 (Idealizations) and to
the eventual NOTES.md Result prose, co-located with Prediction 1's
[0.505, 0.520] band wherever it is reported: restate T9's own disclaimer
verbatim (this figure exceeds the Babinet/shadow-formation ceiling for a
perfectly-black object and is a near-field box-geometry artifact, T8, not
an asymptotic material absorptivity constant). With that one sentence
carried forward, I have no remaining charter objection — this cycle would
be full **support**.
