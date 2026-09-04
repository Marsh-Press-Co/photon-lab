# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 84 (exp-107)

*Fresh context. Charter: non-classical absorption, state-dependent or
coherent interactions. Expressibility contract: mechanisms enter the bench
only as effective classical parameters — σ(I), σ(x,t), dispersive ε(ω),
gain — or Red Team strikes them.*

## 0. Scope note

This cycle bundles two structurally independent pieces of work (Tier 0:
the `delta_scene` R3-vs-R4-vs-R5 retirement; Tier 1: three `kappa_window`
closeouts). My task brief asks me to (1) confirm T1 throughout everything
executed, including the checkpoint/resume mechanism specifically; (2)
re-derive my own Phase-2 anchor-impossibility finding one more time and
confirm it landed correctly in the retirement text; (3) run a statistical-
rigor check on Item 4. I address all three, then give a steel-man,
sharpest attack, verdict, and top ask for Iteration 85.

## 1. T1 confirmation

**Confirmed N/A throughout — retirement text, Item 1, Item 3, Item 4 —
with one genuine, disclosed-but-unverified methodological gap named
below, not load-bearing to this conclusion.**

- **Retirement text (Tier 0):** zero code, zero FDTD, a governance
  decision citing already-committed record. No mechanism of any kind is
  proposed, varied, or scored. Trivially N/A.
- **`run.py`, `chunk_runner.py`, `finalize.py` (direct source read, not
  taken on NOTES.md's word):** the only material construct anywhere in
  the three files is `materials.graded_black_shell(sim, CX, CY, R_CORE,
  R_COAT, sigma_max=...)` — a static, position-only `σ(x)` assignment,
  identical in kind to every prior T28-bridge cycle. `chunk_runner.py`'s
  `_run_hollow`-equivalent (`step_once()`) never calls `materials.
  pec_disk()` — by design (Item 1's hollow-vs-PEC-cored construction) —
  and never introduces any intensity-, time-, or state-dependent
  coefficient. `finalize.py` is pure post-hoc arithmetic on already-
  captured fields. `item3_thermal_row()` is explicitly the seat's own
  post-run analytic sidecar (`thermo_sidecar.mixed_length_scale_regime`),
  honoring THERMODYNAMICS' expressibility contract, operating on already-
  persisted classical `sigma_ext`/`abs_ext_ratio` scalars — no FDTD, no
  mechanism. I additionally grepped `lab/fdtd2d.py` for
  `random|seed|threading` — zero matches; the engine has no stochastic or
  state-dependent element for any mechanism to hide inside, and the
  `ca`/`cb` update coefficients (`Sim.run()`, lines 213–217) are computed
  once from `sigma_e`/`eps_r` and held fixed for the entire run, matching
  LOGBOOK's own ESTABLISHED gap #2 ("no time-varying materials... static
  per run"). T1:N/A is earned, not merely asserted, across all three files.

- **The checkpoint/resume mechanism, examined specifically as instructed.**
  `lab/fdtd2d.py::Sim.run()` (lines 208–264) is a strict, single-step
  Markov update: every quantity the next step needs (`Ez`, `Hx`, `Hy`,
  `Bx`/`By` if anisotropic, `sigma_e`, `damp_e`/`damp_hx`/`damp_hy`, and
  critically `self.step_count`, which drives the source phase term
  `sin(self.omega * n)` at `n = self.step_count`) lives as an instance
  attribute of `sim`. `chunk_runner.py::step_once()` pickles the *entire*
  `sim` object between chunks and unpickles it to resume — nothing the
  next chunk needs is reconstructed from a separate, possibly-inconsistent
  external counter. Since (a) numpy `float64` arrays pickle to their exact
  bit pattern (no precision loss), (b) every per-step operation is
  elementwise (no threaded reduction/summation whose order could vary
  between a continuous run and a chunked one), and (c) there is no RNG
  anywhere in the engine, resuming from a pickle **should**, on this
  architecture, reproduce a run bit-identical to an uninterrupted
  `sim.run(STEPS)` call. This is a real, correct piece of reasoning — but
  it was never actually *tested* this cycle. The only verification
  performed (`run.py`'s own module docstring: "independently re-run at
  Phase 3.5 to confirm bit-exact reproduction of the numbers in
  `results.json`") re-ran the *same* chunked method against itself — a
  self-consistency check, not a cross-validation against a genuinely
  uninterrupted run. Concretely: `run_output.txt` shows r=156's own 6400
  steps ran as **a single uninterrupted foreground call, no chunking at
  all** ("ran 6400 steps (single foreground call)") — its numbers carry
  zero checkpoint/resume exposure. Only r=312 (12,800 steps, both empty
  and article scenes) was split into 6 pickled chunks each — the first
  time this program's history has used mid-run `Sim`-object pickling as
  load-bearing measurement machinery, not merely a documented workaround.
  Per this program's own R18 precedent (new machinery joining an analysis
  pipeline earns its own validation *in the cycle it is introduced*, not
  merely the trust its architecture "should" deserve by inspection), a
  cheap toy-scale A/B (a few hundred steps, run continuously vs. via a
  2-chunk pickle-resume, diffed to machine precision) would have closed
  this for the cost of seconds. Its absence is an R8-shaped gap (an
  argued-not-verified equivalence claim) — genuinely new, not previously
  named anywhere in LOGBOOK's checkpoint/resume history because this is
  the first cycle to use this mechanism at all. **I judge this unlikely to
  be materially wrong** (no non-determinism source exists anywhere in the
  reasoning above), and it does not change my T1 conclusion — nothing
  non-classical could be smuggled in via a resume mechanism that only ever
  restores a classical field/coefficient state — but it is a real,
  disclosed-but-unverified gap specific to r=312's numbers that the record
  should not treat as fully closed. See §4.

## 2. Anchor-impossibility re-derivation (Phase-2 finding, re-checked)

Re-deriving independently, from the same four cited crossings
(`experiments/083-.../results.json`, LOGBOOK, exp-107 `phase1_proposal.md`
§2), not copying my own prior write-up:

```
crossings = 37.127°, 38.590°, 40.265°, 41.461°
buffer    = 1.4° (half the established 2.84–2.95° period)

consecutive gaps:
  38.590 − 37.127 = 1.463°
  40.265 − 38.590 = 1.675°
  41.461 − 40.265 = 1.196°
all three gaps < 2×buffer = 2.8°  →  every pair of exclusion zones overlaps

exclusion zone per crossing (±1.4°):
  37.127 → [35.727, 38.527]
  38.590 → [37.190, 39.990]   overlaps zone 1 (37.190 < 38.527)  → merge → [35.727, 39.990]
  40.265 → [38.865, 41.665]   overlaps merged (38.865 < 39.990)  → merge → [35.727, 41.665]
  41.461 → [40.061, 42.861]   overlaps merged (40.061 < 41.665)  → merge → [35.727, 42.861]

merged forbidden band: [35.727°, 42.861°],  width 7.134°
proposed census grid:  [36.000°, 42.000°]  ⊂  [35.727°, 42.861°]  entirely
```

**Confirmed exactly, a third independent time**, matching my own Phase-2
critique digit-for-digit and Red Team's own §0.1 re-derivation. Zero of
the 31 proposed grid points can serve as `θ_anchor`; Gate G0 has no
candidate to evaluate. **Checking NOTES.md's Synthesis section (item 1 of
the five-point retirement case): it states the identical merged band
`[35.727°, 42.861°]`, the identical "zero of 31 candidate points clear the
buffer" conclusion, and correctly attributes it to QUANTUM as ADOPTED in
full.** My finding landed correctly — not merely trusted from my own
earlier critique, independently re-verified here from the source numbers
a third time (mine, Red Team's, and now this one).

I also re-checked Red Team's own extension of my finding (§0.2/§0.3,
generalizing to the buffer-vs-period structural argument and testing my
own proposed rescue against exp-095's record) against the retirement
text's own item 2/3 — both are stated accurately and are, on their merits,
the more consequential findings of the two (my own local-domain finding
would have been patchable by re-windowing; Red Team's generalization
correctly shows it would not have been). I have no correction to offer
here — this is as clean a reflection of a Phase-2 finding into a
retirement text as this program has produced.

## 3. Statistical rigor check — Item 4

**`frac_unresolved` = 0.18275 (731/4000, r=156) / 0.2675 (1070/4000,
r=312), `FLOOR_FRAC=0.10`.**

**(a) The "worsens with r" framing overstates what two points and 4000
correlated pixels can establish, though the direction is plausible.**
Two independent statistical concerns, neither disclosed in NOTES.md:

1. The 4000 "cells" in each pool are **not independent samples** — they
   are neighboring pixels of one coherent near-field `|Ez|²` map inside a
   single fixed window box. A naive two-proportion comparison treating
   them as i.i.d. Bernoulli trials (`p̂₁=0.18275`, `p̂₂=0.2675`, pooled
   `p̄=0.225125`) gives `z ≈ (0.2675−0.18275)/√(0.225125·0.774875·(2/4000))
   ≈ 9.1` — a wildly overstated significance for a coherent EM field whose
   true spatial correlation length spans many cells (this program's own
   FDTD windows run at `cells_per_lambda=20–50`; adjacent pixels within a
   fraction of a wavelength are strongly correlated). The genuine number
   of independent spatial degrees of freedom inside this window is far
   smaller than 4000, so the true uncertainty on `frac_unresolved` is
   correspondingly larger than a raw pixel count implies. NOTES.md
   presents `0.18275`/`0.2675` as two bare point estimates with no
   acknowledgment of this — a category error this program has flagged
   before in different guises (autocorrelated residuals misread as
   independent evidence, exp-074's own Iteration-51 finding).
2. This is exactly **two r-points** (156, 312) for this specific
   numerator channel — r=78 was never tested (exp-106's own Item 1 tested
   only the empty-scene denominator). This program has a standing,
   on-the-books rule for precisely this shape of claim: R15's own
   Iteration-71 addendum states that two cross-resolution/cross-condition
   points "cannot, on their own, distinguish genuine continuum convergence
   from a persistent recipe-level artifact or a genuinely non-convergent
   oscillation... a third, differently-ratioed [point] is the minimum
   required." NOTES.md's Result section states flatly that "contamination
   is real and WORSENS with r (18.3%→26.8%)" — asserting a trend from
   exactly the two-point sample size this program's own rule already
   named as insufficient to call a trend established, elsewhere on this
   identical `kappa_window` r-family. The direction is mechanistically
   plausible and not merely a coincidence of two points — PHOTONICS' own
   exp-106 Phase-5 finding of a `~200,000×` article-scene field collapse
   at r=312 gives a genuine physical reason to expect more cells falling
   below a fixed-fraction-of-RMS floor at the larger r — but the write-up
   should say "consistent with a genuine worsening, on 2 points, not yet
   an established trend by this program's own R15 standard," not state
   the trend as settled fact. This is not outcome-determining (the
   qualitative finding — the numerator carries real, previously-
   undetected contamination the denominator-only check missed — survives
   regardless), but the specific "worsens with r" language is thinner
   evidence than it reads.

**(b) `FLOOR_FRAC=0.10` is a borrowed round convention, not independently
derived for this use — the same species of defect this cycle's own Red
Team audit caught elsewhere.** `FLOOR_FRAC=0.10` traces to R13 (Iteration
64), always disclosed there as "a house-style convention," and LOGBOOK's
own record already contains a direct, on-point precedent for scrutinizing
it: Iteration 66 (exp-089's own Phase-5 Red Team final audit) ruled "R13's
`FLOOR_FRAC=0.10` empirically demonstrated inadequate" in the closely
related `ratio_k`/`frac_contrast` classifier context — misclassifications
occurred at margins as low as 1.48× the floor, correct classifications
only from 2.17× up — and recommended a proper zero-FDTD logistic/threshold
refit rather than continuing to cite the bare `0.10` figure (exp-090
executed that refit for the `ratio_k` channel specifically; I find no
record of an equivalent refit ever being done for `window_stats()`'s own
raw-intensity floor gate, the channel Item 4 uses). That specific numeric
critique does not mechanically transfer here (a different quantity: raw
`|Ez|²` intensity vs. a fitted ratio), so I do not claim Item 4's PASS/
FALSIFIED calls are wrong — `0.18275` clears `0.10` by a comfortable
1.8×, not a razor-thin margin the way R13's own founding cases were — but
the underlying principle is identical, and this cycle's own Red Team audit
already caught exactly this shape of defect elsewhere in the SAME
document: Attack 5 ruled the census's `[0.5,2.0]` G0 amplitude-ratio band
"imported by exact numerical analogy... reused here... without
re-justification... exactly the failure R17... was adopted to prevent."
`FLOOR_FRAC=0.10`, reused a second time this cycle on a genuinely
different physical quantity with no independent re-derivation, is the
same failure shape, missed by the same audit that caught it once already
in this document. Not load-bearing to either verdict at r=156 or r=312
this cycle, but worth naming for consistency and for whoever next reuses
this constant on a channel where the margin is thinner.

## 4. Steel-man (150 words)

This cycle does exactly what a governance cycle should: it treats
"execute vs. retire" as an empirical question, builds the cheapest gate
that could have settled it, and — when five independent lines of
adversarial review (mine among them) show that gate cannot even run —
retires the question by written argument rather than either forcing a
scientifically hollow census through or deferring an eighth time. The
retirement text is precise, not sweeping (it closes only the resolution-
family-attribution question, names its own reopening condition, and
leaves T28's larger mechanism question and every other standing deferred
item untouched). Item 4's own honest disclosure — a real, unanticipated
finding neither the Phase-1 proposal nor any Phase-2 critique predicted,
scoped explicitly as measured on the hollow substitute rather than the
PEC-cored primary article — is this program's own R8/R16 discipline
working exactly as intended: report the surprise, don't smooth it over.

## 5. Sharpest attack (150 words)

The single most consequential number this cycle produced from real new
FDTD — r=312's `frac_unresolved=0.2675`, the reading that turns "the
solver's own noise floor may explain P3's collapse" from a flagged worry
into a real, actionable finding — rests entirely on this program's
*first-ever* use of mid-run `Sim`-object checkpoint/resume pickling
(§1), introduced this shift as an environment workaround and never
cross-validated against an uninterrupted run, only against itself. r=156's
own numbers carry no such exposure (a single foreground call, confirmed
from `run_output.txt`); r=312's do. I judge the mechanism architecturally
sound by direct inspection of `lab/fdtd2d.py::Sim.run()` — but "sound by
inspection" is exactly the standard R18 exists to say is not enough for
new load-bearing machinery, and this document treats the two r-points as
equally trustworthy without flagging that one ran through genuinely
unverified new code and the other did not.

## Verdict: **CONFIRM-WITH-GAPS**

T1 is correctly, repeatedly N/A everywhere in this cycle, and my own
Phase-2 anchor-impossibility finding is reflected in the retirement text
exactly, re-derived independently a third time with the identical result.
Nothing I found reverses the retirement decision, Item 3's CONFIRM, or
Item 1's PASS-at-the-loose-band verdict. The gaps are real but non-firing
by this program's own standard: an unverified (though probably sound)
new-machinery equivalence claim behind r=312's numbers, and a "worsens
with r" / raw-pixel-count framing in Item 4 that overstates what two
correlated-pixel data points can establish — both disclosure gaps, not
computational errors, both consistent in kind with defects this program
has named and non-fired on before (R8, the R15 two-point caution).

## Single most important thing for Iteration 85, from this seat

**Before `chunk_runner.py`'s checkpoint/resume mechanism is reused again
on any load-bearing measurement, run a cheap toy-scale validation: a small
`Sim` (a few hundred steps) executed once continuously and once via a
2-chunk pickle-save/reload cycle, diffed to machine precision.** This
costs seconds, not minutes, and closes the one genuine "argued, not
verified" gap this cycle leaves open on its own most consequential new
number (r=312's `frac_unresolved=0.2675`) — squarely this seat's own
standing duty (confirming strict classical determinism holds end-to-end,
including through whatever execution machinery a cycle invents under
time pressure) and squarely this program's own R18 precedent (new
machinery earns its own control in the cycle it is introduced, not
merely the trust its architecture appears to deserve).
