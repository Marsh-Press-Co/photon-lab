# PHASE 2 — CRITIQUE (ELECTROMAGNETISM) · Panel Iteration 64 · exp-087

## Steel-man

From reciprocity/passivity bookkeeping, this proposal is clean where it
counts. The scene is strictly linear, time-invariant, passive: σ_e≥0
everywhere in `graded_black_shell`, no dispersion, no gain medium
anywhere — T1's escape-route question is correctly N/A, not dodged. P1's
zero-FDTD vacuum-footprint check on `damp_e` at both new box windows is
exactly the right discipline: verify the boxes sit in true vacuum before
trusting any flux integral through them, extending exp-065's own
bit-exact precedent rather than assuming clearance. BOX_B doubling
BOX_A's clearance (R_OUT+24, still inside GUARD_OUT) gives a real, not
token, box-independence companion. Treating `frac_p_abs` vs
`frac_contrast` as a genuinely open, symmetric test (ENERGY-DECOUPLED /
CONSISTENT / ENERGY-DOMINANT / MIXED, no thumb on the scale) rather than
assuming either operand answers the other is the right epistemic posture
for a first-of-its-kind bulk-vs-local energy comparison.

## Sharpest attack

Box independence (BOX_A vs BOX_B) tests spatial-placement invariance of
`widths()`; it does NOT test the orthogonal identity `sections.py`'s own
docstring calls load-bearing — that `sigma_ext` and `sigma_ext_cross`
(the incident×scattered cross-term / near-field optical-theorem route)
agree. Passivity/reciprocity demand BOTH identities before a
Poynting-box number is trusted, and this proposal's Phase 4 plan (§6)
never computes or reports `sigma_ext_cross` at all. Worse: stage 8's own
suite gate for that identity ("extinction: two routes agree") has only
ever been exercised on a bare PEC disk at broadside incidence, in a
small generic scene — never on `graded_black_shell` (this program's
actual flagship absorber), and never obliquely. This cycle is
simultaneously the first oblique AND first PAD-shifted-box application
of `widths()` to an absorbing article — exactly the regime where a
route-specific near-field/phasor-extraction defect would most plausibly
surface, and exactly where no absolute identity gate currently exists to
catch it before P5's classification is trusted.

## Supporting detail (verified from source, not asserted)

- `lab/validation/run_all.py::stage8_sections()` computes
  `xi_p = |sigma_ext_cross − sigma_ext| / |sigma_ext|` **only** for
  `wp_a` — the bare PEC disk at BOX_A, broadside, in the suite's own
  360×240 test scene. There is no analogous `xi_d` (dielectric) or
  `xi_k` (the graded-black absorber) anywhere in that function, and the
  Results table in `VALIDATION.md` carries no stage-8 row at all listing
  a second extinction-route figure for an absorbing object. The
  "extinction must agree between its two independent routes" trust gate
  `sections.py`'s own module docstring advertises has, in this program's
  entire history, certified that identity for exactly one non-absorbing
  scatterer at one angle.
- This proposal's §6 Phase-4 plan step (e) reads: "from each pair,
  compute `sc.widths()` at `BOX_A` and `BOX_B`" — `widths()` returns
  `sigma_ext_cross` in its own dict (`lab/sections.py` line ~151), so
  capturing it costs nothing extra; the gap is that the plan never asks
  for it.
- On the R9 commensurability question specifically: `frac_p_abs` and
  `frac_contrast` are both dimensionless `|Δ|/baseline` fractional
  changes, so this is not the same shape of defect R9 caught (a fitted,
  differently-normalized ratio divided by a raw threshold and reported
  as if the division alone certified the comparison). The proposal's own
  P5 reasoning correctly names the real physical distinction — a
  bulk-integrated box-perimeter flux vs. a local, windowed contrast — as
  the stated HYPOTHESIS for why decoupling is plausible, not as an
  assumed equivalence, and Idealization 6 discloses the 0.1×/10× band as
  a deliberately wide, non-rigorous choice rather than a derived
  confidence interval. That is the right way to run a first-of-its-kind
  comparison between two different classes of observable — not an R9
  violation on its own. It does, however, make the `ratio_k` classification
  only as trustworthy as the two individual measurements feeding it, which
  is precisely why the missing `sigma_ext_cross` check (above) matters:
  an undetected route-disagreement in `sigma_ext(BOX_A)` would corrupt
  `frac_p_abs` silently, with nothing in the current plan positioned to
  catch it before P5.
- T1/passivity implication not currently stated anywhere in the
  document: for a linear, passive, σ_e≥0, gain-free medium, `sigma_abs`
  and `p_abs_w` must be non-negative at every (cfg, θ, box) cell, in both
  the empty and article legs. This is trivial by construction here, but
  "trivial by construction" is exactly the standard this program already
  applies elsewhere (e.g. `radial_absorbed_power`'s hard PEC-core p_J≡0
  gate) — it costs nothing to state and check explicitly (a one-line
  assertion over the already-computed `sigma_abs`/`p_abs_w` arrays) and
  gives a genuine, if low-probability, defect-catching floor: a negative
  reading anywhere would immediately flag a sign or phasor-convention
  bug in this cycle's own box translation, not a physics surprise.

## Verdict: support-with-changes

The measurement plan is sound in its passivity/reciprocity bookkeeping
and in treating the bulk-vs-local energy comparison as a genuine open
question rather than a foregone one. But it under-verifies its own
instrument at exactly the load-bearing step: the primary metric (P5)
depends entirely on `sigma_abs(BOX_A)`/`sigma_ext(BOX_A)` being correct
for an absorbing article at oblique incidence and PAD-shifted box
placement — a combination this program's trust suite has never
certified via the extinction-routes-agree identity, and this cycle's own
plan does not propose to certify it either. Box independence alone
answers "does moving the box change the answer," not "is the flux
computation itself internally consistent" — passivity/reciprocity
license both checks and this proposal only runs one.

## Flip-parameter

Add one mandatory, pre-registered gate to §4/§6, computed from data
already produced (zero marginal FDTD calls): for both configs, both legs
(empty/article), at `BOX_A`, report
`xi_ext(cfg,θ) = |sigma_ext_cross − sigma_ext| / |sigma_ext|`, and HALT
before any P5 classification is computed unless `xi_ext ≤ 0.12` at every
cell — reusing stage 8's own existing PEC tolerance rather than
inventing a new number. This single addition would flip my verdict to
full support: it closes the one reliability gap box-independence cannot
address, at no cost beyond reading a value `widths()` already computes.
