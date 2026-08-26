# PHASE 2 — CRITIQUE · QUANTUM OPTICS seat · Panel Iteration 52 (exp-075)

*Fresh sub-agent, QUANTUM OPTICS charter (PANEL.md seat 5: non-classical
absorption, state-dependent/coherent interactions; expressibility contract —
mechanisms enter the bench only as effective classical parameters or Red
Team strikes them). Blind to the other five seats' Phase-2 critiques.
Re-ran `boundary_reflectance.py` myself before writing anything below;
every number cited here that isn't in the committed
`boundary_reflectance_results.json` was produced by a script run in this
review (permutation test, R² vs. candidate-period sweep, polynomial-fit
comparison) — none hand-typed (R4).*

## Reproduction

`python3 experiments/075-t28-absorb-boundary-wkb-reflectance/boundary_reflectance.py`
reproduces every headline number bit-for-bit: `P_model=15.0000°`,
`R²=0.8587` (widened search `P*=60.0000°`, `R²=0.8785`), `rel_dev=4.2778`,
shape `r²=0.2586` with `r=-0.5085`, `COMBINED VERDICT: REFUTE`. All three
sanity/passivity gates (G-LOSSLESS 2.2e-16, G-N1 1.4e-15, G-PASSIVITY worst
`|r|=0.0064` over 124 pairs) pass as claimed.

## Steel-man (145 words)

The transfer-matrix derivation is genuinely rigorous by this program's own
R4 standard: `nu(x)` is read programmatically from `Sim.damp_e`, never
retyped; the exact (not linearized) branch of `n(x)` is selected by an
unambiguous physical requirement (passivity, `|r|<=1`) rather than
convenience, with the failing branch's own catastrophic numbers disclosed,
not hidden; three independently-checkable sanity gates all pass before any
`r(theta;ABSORB)` is trusted. The pre-registered SUPPORT/REFUTE bands were
fixed and disclosed *before* the real-data comparison, and the write-up is
honest that its own closed-form estimate (7.8–11.8°) was known in advance.
Choosing the exact recursive impedance transform over a single-pass
WKB/Born integral is the right call given the explicitly-computed marginal
adiabaticity (`Q=0.09–0.18` at 600nm) — a proposal correctly declining the
tool its own title advertises, and saying so, is rarer than it should be.

## Sharpest attack (149 words)

Test B's sign-blind band (SUPPORT≥0.30, REFUTE≤0.05) mis-scores its own
result. I ran a 200,000-trial permutation null (shuffling the real
`delta(theta)` against the fixed model curve): `r²=0.2586` sits at the
99.66th percentile of chance (`p=0.0035`, `t=-3.18`, `n=31`) — not an
ambiguous number. But it's **negative** (`r=-0.508`): a statistically
significant *anti*-correlation, not weak support. For a zero-free-parameter
model with a definite predicted phase, that is real evidence the mechanism
is backwards, yet the band files it as "close to, but under, the SUPPORT
bar" — the opposite of the correct read. Separately: `P_model=15.0000°` is
not a period estimate. I swept candidate periods and confirmed R²(model)
rises *monotonically* to whatever grid boundary is set, asymptoting exactly
to the pure-quadratic-trend R² (0.8796) — no interior optimum exists at any
window width, so `rel_dev=4.28` is a boundary-search artifact, not a
measured deviation, though the qualitative REFUTE it feeds is not wrong.

## Supporting detail (not part of either 150-word block, for the record)

- **Test A degeneracy, quantified**: `R²(P*)` for the model curve is
  0.0131/0.4387/0.7542/0.8587/0.8785/0.8796 at `P*`=1°/4°/7.8°/15°/60°/1000°
  — a smooth, monotone approach to the ceiling, matching a degree-2
  polynomial fit to the same curve in `sin(theta)` (`R²=0.8796` exactly).
  This is the textbook signature of a fixed-period sinusoid basis
  degenerating to a low-order polynomial trend once the candidate period
  exceeds the data window (here `sin(42°)-sin(36°)=0.0813` in x, vs. the
  candidate periods `Tc` of 0.20–13.6+ at `P*`=15°–1000°): under one-third
  of a cycle never resolves a period, it resolves curvature. This matches
  this exact sub-thread's own precedent — my seat's Iteration-48 finding
  that `_free_period_search` can sit below the window's Rayleigh floor for
  the periods a given test needs to separate (LOGBOOK.md, exp-071) — now
  recurring in a *different* instrument (a single free-fit against a
  fixed, zero-parameter model curve, not two configs' periods compared
  against each other), a genuinely new failure shape, not a repeat of the
  old one. **The real data's own R²(P*) curve, by contrast, has a genuine
  local maximum at P*=2.8421° (R²=0.6272) well above its own large-P
  asymptote (R²≈0.41)** — confirming the real signal is a completed
  oscillation and the model's curve is not, which is itself a clean,
  independent argument for REFUTE that doesn't depend on `rel_dev` at all.
- **On power (task item c)**: widening the search window (1–60°, `n_grid`
  6000) does not change the qualitative picture — it still runs to
  boundary — so this is not a resolution/power problem fixable by a wider
  or finer grid; it's structural (the model's own predicted curve simply
  doesn't complete a cycle in any window tested). The `n=31`/124-pair
  sample size is not the binding constraint on Test A; it is on Test B,
  where it is nonetheless enough to reject "no relationship" at `p=0.0035`.
- **On idealization 6 (task item d)**: the model's `omega`-dependence enters
  only through `nu/omega` at a fixed, frequency-flat `nu(x)` — i.e. this is
  a lossy-conductor-like effective medium, not a resonant/dispersive one. A
  genuinely dispersive `epsilon(omega)` band (relaxation- or Lorentz-type,
  `nu` itself a function of `omega`) would change `arg(r(theta;ABSORB))`'s
  frequency scaling and could shift the predicted period independent of
  `PLANE_X` — a real follow-up direction, staying inside this seat's
  expressibility contract, but out of scope for this fully-classical cycle
  and correctly not attempted here.

## Verdict: **support-with-changes**

The substantive REFUTE conclusion is not undermined by anything above — if
anything both findings tighten it: the real oscillation genuinely resolves
where the model's does not, and the "close call" on shape is actually a
significant miss in the wrong direction. But the document should not carry
forward `P_model=15.0000°`/`rel_dev=4.28` as if they were calibrated
period-mismatch numbers, and should not describe `r²=0.2586` as sitting in
an ambiguous zone.

**Flip**: Re-score Test B as a signed test fixed *before* comparison would
have required disclosing sign as physically meaningful for a
zero-free-parameter model with a definite predicted phase (e.g. SUPPORT
iff `r>=+sqrt(0.30)`; REFUTE iff `r<=0`) — under that band, Test B alone is
REFUTE at `p=0.0035`, and Test A's boundary-pinned fit should be reported
as "no completed oscillation within any tested window," not as a period
number. Neither change moves the combined verdict off REFUTE; both would
make the document's own stated reasoning match what actually happened.
