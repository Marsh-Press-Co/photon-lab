# PHASE 5 — REVIEW · Panel Iteration 28 · Seat: QUANTUM OPTICS

*Fresh-context instance, blind: no `phase5_review_*.md` or
`phase5_redteam_audit.md` existed in this directory at read time. I do not
assume my own seat's Phase-2 work (the alias-lattice mechanism this cycle
adopted) was right because I proposed it in a prior instance — I re-derived
and independently re-executed everything load-bearing below, against the
actual committed code, before trusting it. Charter: non-classical
absorption, coherent interactions; expressibility contract on effective
classical parameters. This cycle proposes no mechanism and touches no T1
escape route, so my charter engages on its coherence/interference-bookkeeping
axis, exactly as it did at Phase 2. Scratch code:
`/tmp/claude-0/-home-user-photon-lab/3f566c8d-1309-5c26-a429-8ae6c0875c6b/scratchpad/qreview/{probe1,probe2,probe3}.py`.
Nothing under `lab/`, or in experiments 042/048/049/050/051, was modified.*

---

## Verdict: **PROMISING**

The cycle's core deliverable holds up under fresh, independent re-execution.
I reran the regression anchor logic pattern, reproduced `beam_divergence_*`
values bit-exactly against the committed functions, and independently
re-derived the out-of-sample split. `P-ALIAS-3` (0 false positives on 81
well-sampled cells), `P-ALIAS-4` (clean transfer to the untouched A=752
geometry), and `P-ALIAS-5` (the asymmetry explanation, ρ=0.933, including
the correct reproduction of the 750nm/38° inversion) are real, falsifiable,
pre-registered wins, not favorable framing. `P-ALIAS-1`/`P-ALIAS-2` landing
PARTIAL is the honest result of a mechanism that is exactly right for the
family it was measured on (`incoherent`/`incoherent_corrected`: 126/126
correct, ρ=0.979) and inapplicable, in a specific and now-locatable way, to
`coherent`. The Phase-4 team disclosed this split themselves, unscored, in
`post_hoc_observations_unscored` rather than either hiding it or
re-scoring around it after the fact — that is the right discipline, and my
own duty this cycle is to check whether their located reason is the actual
reason.

---

## My specific duty: is the `coherent`-breakdown mechanism as located, correct?

**Finding: SHARPENED, not merely confirmed — and materially incomplete as
NOTES.md states it.**

### What NOTES.md's Reading says, and what is right about it

The E1 identity is real and I re-verified it from the actual committed
`lab/ambient.py` + `experiments/050-.../design_geometry.py` code, not from
the write-up's prose. `incoherent_sum` divides each per-angle profile by
**its own** flank mean before summing, so the flank mean of the sum is
identically 1 by construction; combined with `weber`'s algebraic form
`(bo−bf)/bf`, this makes `beam_divergence_incoherent(_corrected)` an EXACT
linear functional of the single-angle Weber contrasts:
`C = Σwᵢcᵢ/Σwᵢ`. I re-derived this from `window_means`+`incoherent_sum`+
`weber`'s source rather than accepting the Phase-2 assertion, and it is not
approximate — it is an identity of the reduction pipeline, independent of
the physics of `c(θ)`. `beam_divergence_coherent` has no per-angle
normalization and sums the complex field `E_tot = Σᵢ√wᵢ·(G@ampᵢ)` **before**
squaring, so `b(y) = |E_tot(y)|²` contains cross terms
`2√(wᵢwⱼ)·Re[Fᵢ(y)Fⱼ*(y)]` for every pair `i≠j` that have no counterpart in
the incoherent construction. This part of NOTES.md's Reading is correct and
I confirm it independently.

### What it is missing — verified by execution, not argument

**1. The two functions do not merely differ in combination rule — they live
in categorically different operating regimes, and this changes what
"instability" means.** I pulled `|C41|` for every row in the committed
`results.json`: `incoherent`'s median is `4.09×10⁻⁴` (min `3.85×10⁻⁵`, max
`5.10×10⁻³`) — the near-null destructive-interference regime the
alias-lattice mechanism was derived and calibration-validated on.
`coherent`'s median is **0.940** (min `0.027`, max `0.9997`) — **four orders
of magnitude larger**, a near-saturated, beamformed/synthesized-shadow
regime, not a small fringe near zero. This holds across TP, FN, *and* TN
`coherent` rows alike (TN median `|C41|=0.927`), so it is not a property of
the misses specifically — it is the entire function's operating point. This
matches, and gives new quantitative teeth to, this program's own prior
finding (LOGBOOK T21, Iteration 22 close, exp-046 Phase 5): the full-aperture
coherent sum is "a deliberately BEAMFORMED/FOCUSED synthetic array... several
near `|C|≈1`," a physically different object from natural angular
divergence. NOTES.md's Reading never states this regime gap; it should.

**2. The n=41 quadrature error for `coherent` is not a small correction on a
converged value — I tested this directly, and it fails a basic
small-perturbation check that the alias-lattice model's own derivation
requires.** For each of the 10 out-of-sample false negatives, I computed the
converged coherent field `E_∞(y)` (via `n=641`, then confirmed flat to 8
significant figures out to `n=5121` — genuinely converged, not merely
plateaued), the `n=41` field `E_41(y)`, and the exact **linearized**
cross-term estimate of the Weber-contrast step,
`ΔC_lin = 2Re[⟨E_∞*·δ⟩_obj]/bf_∞ − bo_∞·2Re[⟨E_∞*·δ⟩_flank]/bf_∞²`
(`δ = E_41 − E_∞`) — literally the first-order term NOTES.md's own framing
("account for cross-terms between angle samples") calls for:

| geometry | θ₀ | λ (nm) | actual ΔC (41→∞) | linear cross-term ΔC_lin | linear/actual |
|---|---|---|---|---|---|
| A=752 | 36° | 450 | −0.04133 | −0.000022 | **0.001** |
| A=752 | 36° | 600 | −0.00054 | −0.000245 | 0.454 |
| A=752 | 40° | 600 | +0.00123 | +0.000109 | 0.088 |
| A=752 | 36° | 750 | −0.00108 | −0.000440 | 0.407 |
| A=752 | 40° | 750 | +0.00153 | +0.000231 | 0.151 |
| A=724 | 36° | 450 | −0.04376 | +0.000078 | **−0.002** |
| A=724 | 40° | 450 | −0.00901 | −0.000093 | **0.010** |
| A=724 | 36° | 600 | +0.00123 | +0.000162 | 0.132 |
| A=724 | 36° | 750 | +0.00125 | +0.000160 | 0.128 |
| A=724 | 38° | 750 | −0.00062 | −0.000294 | 0.478 |

The linear cross-term explains at most **48%** of the actual step and, at
every 450nm cell (the three largest actual jumps, up to `4.4×10⁻²` — a
~4-percentage-point swing of the object's own extinction, not a fringe
residual), explains **0.1–1.0%** of it. I ran the identical check on the 4
true positives (cells the current predictor *does* flag correctly) and got
the same pathology: linear/actual ratios of 0.2–1.2%, 0.4%, and 12.1% —
meaning the "correct" classifications are not evidence the mechanism is
partially working on `coherent`; they are the same degenerate regressor
crossing a threshold coincidentally. I confirmed this degeneracy directly
from `results.json`: **`E_pred` for `coherent` is bit-identical to
`incoherent`'s at every one of the 18 shared `(θ₀,λ)` FWHM=20° coordinates**
(by construction — the single-angle building block is literally the same
function, `design_geometry.py`'s own documented "degenerate-x1 control").
`coherent`'s classifier is therefore not a weakened version of a working
model; it is the *same number*, from a different physical object, being
asked a question it contains zero information about.

**3. The correct mechanism class for this residual is already in this
program's own record, uncited by exp-051.** A 450nm-worst, ~4-percentage-
point, non-perturbative jump at `n=41→81` for a fixed FWHM=20° coherent sum
is exactly the signature of **discrete-aperture grating-lobe leakage**, not
Poisson-alias-of-a-smooth-fringe. LOGBOOK's own Iteration-22 entry (exp-046
Phase 5, QUANTUM's own prior-cycle finding) already measured this for the
identical construction: at the 9 FWHM=20° cells, the `n=41`-point angular
comb synthesizes "a three-lobe comb whose grating-lobe replicas... carry
41.7–68.0% of the total intensity outside ±3 aperture-widths." That is a
large-signal, discrete-array-factor phenomenon (shorter λ ⇒ more angular
oscillation cycles across the same physical aperture ⇒ worse under-resolution
by a fixed `n=41` ⇒ bigger leakage — exactly the λ-ordering the false
negatives show: the three biggest misses are all 450nm). It is a different
object in *kind* from the alias-lattice model's own derivation (a first-order
Poisson-summation correction, valid precisely when the quadrature is close to
converged already) — not a sharper version of the same idea that a bigger
`m` or a cross-term add-on would capture.

### Answering the task's explicit test directly

*"Check whether a corrected alias formula for the coherent case (accounting
for cross-terms between angle samples) recovers the missing correlation."*
**No — tested directly above, and it does not, by 1–2 orders of magnitude at
exactly the cells that matter most.** The cross-term is real (E1's negation
is correct) but it is not the dominant term; a linear correction cannot
rescue a regime where the leading-order approximation itself is invalid.

*"...or whether the E1 identity itself is subtly wrong for `coherent` in a
way that's checkable."* **E1 is not wrong — I re-derived it independently
from `lab/ambient.py` source and it is an exact identity of the reduction
pipeline for `incoherent`/`incoherent_corrected`, and its negation for
`coherent` (no per-component normalization, field summed before squaring) is
also exactly right.** The imprecision is downstream of E1, not in it: stating
"a materially different combination rule" is true but underspecifies *how*
different — the practical answer is "different by an amount that puts the
n=41 error outside the small-perturbation regime the alias-lattice
derivation requires," which is a stronger, differently-actionable claim than
"needs a cross-term correction."

---

## Ranked Iteration-29+ priorities

Per PANEL.md, my seat does not vote — this is my ranked read, for the
Director to reconcile against the other six.

1. **(Unconditional, already bound — not re-litigated here.)** Red Team's
   Iteration-28 ruling that Iteration 29 builds the fixed-absolute-thickness
   `graded_black_shell` variant (MATERIALS' item, 21-iteration span since
   first proposal) is accepted as binding by this seat. Nothing in my review
   provides grounds to override it.

2. **Yes — closing the `coherent`-predictor gap deserves its own ranked
   slot, and it should be stated concretely, not as "investigate coherent
   more."** The task I was given already frames the right shape of test, and
   I have narrowed it further by execution: **build and score a
   grating-lobe/array-factor n\* criterion for `beam_divergence_coherent`
   specifically** — e.g., the angular-sampling comb's replica-leakage
   fraction outside the main synthesized lobe (LOGBOOK T21's own Iteration-22
   object, not a new one) as the regressor, scored against the same 72
   `coherent` out-of-sample rows exp-051 already computed and labeled (zero
   new FDTD, reuses committed `n*` labels, comparable cost to exp-051
   itself). Pre-registered falsifier: if a grating-lobe-leakage regressor
   does not clear a materially higher AUC/sensitivity bar than the current
   degenerate `E_pred` (chance-level ranking would itself be informative),
   the `coherent` residual is not a synthesis-undersampling story either, and
   that is worth knowing. This is a same-class, same-cost instrument-fidelity
   cycle to the ones already run (20/22/23/26/27/28) — I do not rank it above
   item 1's unconditional trigger, but it should not fall to a seventh
   consecutive re-ranking the way item 1 nearly did.

3. **A cheap, same-shift NOTES.md correction, not a new cycle**: the Reading
   section's `coherent`-breakdown paragraph should be amended to state the
   regime gap (four-orders-of-magnitude `|C|` difference) and cite the
   already-existing LOGBOOK T21/Iteration-22 grating-lobe finding as the
   located mechanism class, rather than leaving "a materially different...
   combination rule" as the terminal explanation. This does not change any
   scored prediction (all findings here are post-hoc/unscored, matching
   `post_hoc_observations_unscored`'s own status) but it is the difference
   between a correct-but-incomplete record and a precisely located one for
   whoever picks up item 2.

4. THERMODYNAMICS' overdue `h_eff` re-derivation (carried from Iteration
   26/27/28's own queue) — no new finding from this seat changes its
   standing; still worth its place in line.
