# Phase 2 Critique — MATERIALS & METAMATERIALS

**Panel Iteration 79, exp-102 ("The Coherent, Phase-Resolved Downstream
Point-Intensity Instrument"). Blind, parallel critique — no other seat's
Phase-2 output was read.**

## Steel-man

This proposal earns something specifically MATERIALS-relevant that most
instrument-build cycles get wrong by accident: it treats the R4 family
(`r_in=60/r_out=156`, cpl=40, `DX_M_R4=15nm`) as the IDENTICAL physical
object to the native r=78 flagship (`r_in=30/r_out=78`, cpl=20, dx=30nm),
not a differently-sized construction. Independently recomputed: shell
thickness = 96 cells × 15nm = 48 cells × 30nm = 1440nm in both cases; outer
radius = 156×15nm = 78×30nm = 2.34µm in both cases. Same physical article,
double grid resolution. That means Gate B's "known-good reproduction"
check validates the new instrument against a genuinely
realizability-identical article, not a rescaled geometry that would need
fresh `REALIZABILITY_MEMO.md` scoring — exactly the resolution-vs-rebuild
conflation this program's own R9/R15 lineage exists to catch, avoided here
without being told to.

## Sharpest attack

The one place this diagnostic touches my lane, it under-enforces its own
correct instinct. Idealizations states the caveat correctly — "a buildable
coating at this thickness would show a shallower, not deeper, on-axis
darkening" — but nowhere requires it to travel into the Result-section
prose that will narrate Prediction 1's κ(θ) confirmation, the way exp-101's
own mandatory fix 6 explicitly required T9's disclaimer to "travel...
everywhere it is cited below." R21 already establishes that
disclosure/persistence is necessary but not sufficient: a headline
finding's caveat must be stated where a future citation will actually
read it, not left one section away. A confirmed "κ≈0, genuine shadow"
headline, read without cross-referencing Idealizations, invites exactly
the R1-family error (treating a locked-unrealizable article's optical
response as informative about real-coating darkness) this program has
already been burned by once (ENZ, Iteration 14).

## Verdict: support-with-changes

The instrument build itself is outside my charter to score (that is
PHOTONICS'/ELECTROMAGNETISM's territory — the phasor bookkeeping, the
`i_inc`/cosθ fix, the beam-aligned frame). My charter is realizability, and
on that axis this proposal is careful, correctly sourced, and does not
imply anything about buildability it hasn't earned. The one gap is
procedural, not physical: require that Prediction 1's Result narration
inline-restates the UNOBTANIUM-WITH-PARAMETERS / "shallower-not-deeper"
caveat, not merely reference it via Idealizations — the same discipline
exp-101 itself imposed on the T9 disclaimer one cycle ago. This is a
one-sentence fix to the reporting template, not to the experiment design.

**Single change that would flip me to unconditional support:** add one
line to the Result-writing instructions: "State the REALIZABILITY_MEMO.md
UNOBTANIUM-WITH-PARAMETERS verdict and its shallower-not-deeper
consequence inline, immediately beside Prediction 1's κ(θ) confirmation
text, not only in Idealizations." Not a numeric/design parameter — there
is none in my lane worth gating on here.

## RULED OUT / Live Thread check (explicit, per Director's request)

No re-tread found.

- **R1** (refractive/real-Δε cloaking, and its Iteration-14 addendum on
  mischaracterized nonlinearities): not applicable — no mechanism or
  material parameter is proposed, varied, or claimed novel; the article is
  unmodified and explicitly named as already-locked unbuildable.
- **T8** (near-field/z_R caveat) and **T9** (Babinet-ceiling
  σ_abs/σ_ext≈0.51 disclaimer): both correctly restated as open/applicable
  caveats, not re-litigated or claimed resolved.
- **`REALIZABILITY_MEMO.md` Amendments 6–7** (`graded_black_shell`'s
  1.44µm shell locked UNOBTANIUM-WITH-PARAMETERS, overdetermined by
  thickness): correctly cited and, per my independent recomputation above,
  correctly identified as the SAME physical construction the R4 family
  discretizes at finer resolution — not weakened, not silently
  re-opened, not used to imply the article is any more buildable than
  already locked.
- No named-constant search (R5/R5-addendum), no ratio-classifier
  denominator with a known zero-crossing (R13/R14), no cross-resolution
  boundary claim (R15), no uncalibrated bracket (R17) — none of these
  apply; this is a diagnostic instrument build on an already-fixed
  article, matching the proposal's own "why nothing here re-treads"
  section, which I independently verified rather than took on faith.
