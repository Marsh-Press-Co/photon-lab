# PHASE 5 — REVIEW · Panel Iteration 28 · Seat: ELECTROMAGNETISM · exp-051

*Blind fresh-context review. No `phase5_review_*.md` or `phase5_redteam_audit.md`
was read before writing this. Charter: field/wave behavior, impedance
matching, energy coupling; reciprocity/passivity/causality bookkeeping. This
cycle issues no T1 mechanism and no constraint-3/4 verdict, so the charter
bites on one question: is the adopted crux quantity — QUANTUM OPTICS'
alias-lattice term, substituted at Phase 3 for this seat's own refuted
Phase-1 `phase_offset` design — actually sound electromagnetic/wave-optics
bookkeeping, and does the located `beam_divergence_coherent` breakdown hold
up as a coherence argument? Every load-bearing number below was produced by
running the actual committed code in this session, not read from NOTES.md's
prose. Scratch code: ad hoc, run inline via `python3 -c`, against
`experiments/051-.../design_geometry.py` and `results.json` unmodified;
nothing under `lab/` or any experiment directory was touched.*

---

## Verdict: PROMISING

## Steel-man (own seat's stake acknowledged first)

My own Phase-1 proposal is dead, correctly. Reviewing fresh, with no loyalty
to it, does not change that PHOTONICS/MATERIALS/QUANTUM/VISION's desk
refutation of `phase_offset` was right: I independently re-derived the fact
that kills it. The fringe's zero-crossing spacing is not `P(θ)=λ/(A·cosθ)`
at all — a two-edge Huygens sum is not a pure sinusoid, so nothing forces its
zeros onto one period. `phase_offset` measured a periodicity that does not
exist; no amount of Phase-4 tuning could have fixed a regressor built on the
wrong object. Red Team's ruling to replace it outright, not patch it, is the
correct call, both procedurally (flag, don't silently rewrite — the original
`phase1_proposal.md` stands unedited) and physically.

## Sharpest finding: the mechanism's soundness rests on an exact,
independently-reproducible algebraic identity — and the `coherent` failure
is not a residual, it is that identity's negation

I did not just re-run the scored predictions (all reproduce — see below). I
went one level under NOTES.md's own claim and checked the thing that makes
the whole aliasing framing *licensed as EM bookkeeping* rather than merely a
fitted-and-lucky curve.

**The identity.** `lab.ambient.incoherent_sum` normalizes each per-angle
profile by its own empty-run flank mean before summing, which forces the
summed profile's flank mean to exactly 1. Algebraically, that means the
FWHM-integrated Weber contrast for `incoherent`/`incoherent_corrected`
**is**, not merely resembles, the Gaussian-weighted average of the
single-angle fringe:

    beam_divergence_{incoherent,corrected}(θ₀,FWHM,λ,g,n)
        ≡ Σᵢ wᵢ · c(θᵢ) / Σᵢ wᵢ        (exact, for ALL n)

I derived this from `lab/ambient.py`'s own `weber`/`incoherent_sum` source
(not from QUANTUM's Phase-2 write-up) and confirmed it numerically against
the actual committed functions, independently of every seat that already
checked it:

```
incoherent: weighted avg of single-angle C = 0.0003318457747752804
            vs beam_divergence_incoherent  = 0.0003318457747751857
            rel diff = 2.85e-13
corrected:  weighted avg of single-angle C = 0.00044686642318621895
            vs beam_divergence_incoherent_corrected = 0.00044686642318647607
            rel diff = 5.75e-13
```

(matches QUANTUM's 5.2×10⁻¹⁴/4.6×10⁻¹³ and Red Team's independent figures to
the display digit — a third cold confirmation.)

**Why this licenses the aliasing analysis, not just motivates it.** Once the
observable is *exactly* a fixed-window, Gaussian-apodized, uniformly-spaced
quadrature of a scalar function c(θ), its refinement error under n-doubling
is a textbook sampling-theory object: the Poisson summation formula says a
uniform-lattice quadrature's error is dominated by the integrand's own
spectral content aliased down to the lattice's reciprocal frequencies
(1/h, 2/h, …). That c(θ) is a genuine, already magnitude-validated
(exp-042 Block MAGNITUDE) Huygens edge-diffraction fringe of the source
aperture's own taper edges — established EM physics, not a fitted curve —
is what makes "the quadrature error is an alias of a real diffraction
fringe" a physically meaningful sentence rather than a numerical-analysis
truism dressed up in optics language. QUANTUM's `alias_coeff`/`E_pred`
construction is the correct tool for exactly this object, and I confirm
Red Team's own from-scratch reproduction: r=0.999998 against measured
`C(41)−C(161)`, AUC 1.000 in-sample on the 18-row calibration set — I did
not re-derive `alias_coeff` from scratch myself (three independent
implementations already exist and agree to 4+ significant digits; a fourth
cold reimplementation would add confirmation density, not new information),
but I verified the one premise none of them stated explicitly: *why* a
scalar Poisson-alias model is the right class of model at all. It is right
because the observable is provably scalar-linear in c(θ), not merely
observed to correlate with it.

**The `coherent` failure is the same identity's negation, checked directly.**
I ran the same weighted-average test against `beam_divergence_coherent` at
the identical (θ₀,FWHM,λ,g)=(38°,20°,600nm,GEOM78):

```
coherent: weighted avg of single-angle C (incoherent convention) = 0.0003318457747752804
          vs beam_divergence_coherent                            = -0.9588431718691508
```

Three orders of magnitude apart, opposite character (a near-total silhouette
vs. a near-null fringe reading) — `coherent` is not "close but off," it is a
categorically different observable. The reason is visible directly in
exp-050's own committed code: `beam_divergence_coherent` builds
`E_tot = Σᵢ √wᵢ · E(θᵢ)` and only then computes `|E_tot|²`, whereas
`incoherent`/`corrected` compute each angle's own intensity (or intensity
cross-term) first and average those. Expanding the coherent square,
`|E_tot|² = Σᵢⱼ √(wᵢwⱼ)·E(θᵢ)E*(θⱼ)`, contains every off-diagonal (i≠j)
term — a discrete mutual-coherence object, Γ(θᵢ,θⱼ) — that has no
counterpart anywhere in the single-angle marginal c(θ) the alias predictor
is built from. `incoherent`/`corrected` retain only the diagonal (i=j)
terms by construction (each component normalized and summed independently,
the textbook mutually-incoherent-source idiom — physically the right model
for a real divergent flashlight beam with no fixed inter-angle phase
relationship, matching this program's own Iteration-22/T21 finding that
`beam_divergence_coherent` is a deliberately beamformed/focused synthetic
array, not a natural divergent emitter). A predictor built purely on the
diagonal cannot see the off-diagonal, **by construction**, for any n, at any
geometry — this is not a fixable gap in `alias_coeff`, it is the coherent/
incoherent distinction itself, restated as a sampling problem.

This also explains the *shape* of `coherent`'s failure, which I checked
against `results.json`'s own recorded mismatches: at all 10 out-of-sample
`coherent` false negatives, the measured quadrature step `|dabs|` exceeds
the model's `|E_pred|` — under-prediction, never over-prediction. That is
exactly what adding a genuine cross-term error source on top of (not instead
of) the diagonal alias term should look like: the diagonal model is not
wrong about the diagonal, it is silent about a real additional term.

## Independent re-verification of the scored record

I re-ran the Spearman split NOTES.md's Reading section reports, from
`results.json`'s own `per_combination` block, independently:

| Split | n | ρ(log\|E_pred\|, log\|dabs\|) | sensitivity |
|---|---|---|---|
| all out-of-sample | 198 | **0.73804** | 12/22 |
| non-`coherent` | 126 | **0.97881** | 8/8 |
| `coherent` only | 72 | **0.30250** | 4/14 |

Matches NOTES.md's cited figures (ρ=0.979 / 0.302, 8/8, 4/14) exactly. This
is not a hand-typed number reproducing a hand-typed number — I recomputed it
from the raw per-row JSON, independently of the prose that cites it. The
overall P-ALIAS-1 PARTIAL (ρ=0.738, band ≥0.85 CONFIRMED) is a genuine,
correctly-scored blend of a near-exact mechanism (non-coherent) and an
out-of-scope one (coherent), not a diffuse miss — the Reading section's own
diagnosis is right and I confirm it from source.

P-ALIAS-0's gate (bit-exact regression anchor, both clauses) reproduces;
P-ALIAS-3 (0/81 false positives on the well-sampled FWHM≤10° block) and
P-ALIAS-4 (clean transfer to the untouched A=752 geometry, 0.954 accuracy)
both check out against `results.json` directly. I did not find any
arithmetic, sign, or scope error anywhere in the committed record — a
different situation than several recent cycles this program's own LOGBOOK
records (exp-048/049's non-reproducing headline figures).

## A genuine, if minor, EM-charter observation not previously flagged

**Every label this cycle validates against, and every `c(θ)` it validates
with, comes from the same unvalidated-at-GEOM78 analytic propagator.**
Idealization 6 discloses this plainly ("no FDTD cross-check exists at GEOM78
at any n"), so nothing is hidden — but it is worth stating in EM terms,
since it bears on my charter's causality/passivity concern: a diffraction
propagator's magnitude was validated against FDTD only at A=752 (exp-042
Block MAGNITUDE, exp-046's A5 desk-vs-FDTD check). Everything in this cycle
— the fringe c(θ), the `nstar` ground-truth labels it is scored against, and
the alias prediction itself — lives entirely inside that one analytic model
at GEOM78. A perfect score here is strong evidence the *quadrature machinery*
behaves as sampling theory says it should; it is not independent evidence
that the *underlying analytic propagator* itself is the physically correct
description of GEOM78's edge-diffraction field at the level T24's own
~0.002–0.007-absolute ABSORB-boundary systematic could matter. This doesn't
threaten anything scored in this cycle (idealization 6 says so and I agree),
but it sharpens, rather than replaces, the standing Iteration-27/28 queue
item for a genuine FDTD `ABSORB` sweep at the T21-vs-T24 geometry — see
priorities below.

## What I did not find

No inconsistency, no unfalsifiable claim, no constraint quietly dropped, no
`REALIZABILITY_MEMO.md` exposure (grep-confirmed: no
`beam_divergence`/`alias_coeff`/`edge_diffraction` citation there). The
Phase-3 Director's override of Red Team's own docket item 7 (moving every
scored prediction off the 18 pre-checked rows onto 198 untouched
combinations) is, from this seat, the single best procedural decision in
this cycle's record — it converted a result that would otherwise have been
transcription (QUANTUM and Red Team had already computed the 18-row answer
at Phase 2) into a real out-of-sample test, and that test is what located
the `coherent` boundary cleanly rather than burying it in an AUC=1.000
headline.

---

## Ranked priorities for Iteration 29+

*Iteration 29's substantive slot is already committed, per Red Team's
Phase-2 ruling in this cycle, to MATERIALS' fixed-absolute-thickness
`graded_black_shell` variant, unconditionally. Ranking what runs alongside
or immediately after.*

1. **The genuine FDTD `ABSORB` sweep at the T21-vs-T24 geometry** — carried
   forward from Iteration 27/28's own queue, now further motivated: this
   cycle's own idealization 6 disclosure means the entire alias-lattice
   result, however clean, is a statement about the analytic propagator's
   internal consistency at GEOM78, not yet cross-checked against FDTD there
   at any n. This is the last uncharacterized uncertainty source on the
   program's own sharpest near-boundary cell family (LOGBOOK T24) and now
   also, incidentally, the thing that would upgrade this cycle's own
   labels from "committed" to "FDTD-verified."
2. **THERMODYNAMICS' own overdue `h_eff` re-derivation** for the program's
   two thinnest surviving detectability margins (exp-043 ON-endpoint,
   exp-045 dose-accumulation) — outside my charter to assess the physics,
   but it is the oldest item on every recent queue (overdue since Iteration
   25) and carries no dependency on anything this cycle touched, so it can
   run alongside Iteration 29 at zero opportunity cost.
3. **A scoped, cheap extension of this cycle's own located mechanism to
   `beam_divergence_coherent`**: build the off-diagonal generalization of
   `alias_coeff` — the discrete mutual-coherence sum
   `Σᵢⱼ√(wᵢwⱼ)E(θᵢ)E*(θⱼ)` restricted to the same alias-frequency structure
   — rather than the diagonal-only single-angle fringe. This is not urgent
   (no constraint-3/4 verdict depends on `coherent`'s tier stability, and
   `coherent` remains, per Iteration 22's own finding, a beamformed
   synthetic-array construction rather than a natural-beam model), but it
   is now a well-posed, low-cost desk question with a stated first-principles
   target (this review's own cross-term argument) rather than an open
   mystery — exactly the shape of problem this program's queue discipline
   says should be named, not left implicit. Explicitly the thing NOTES.md's
   own "Unresolved, concretely scoped for a future cycle" sentence points at.
4. **VISION SCIENCE's sub-degree (0.25–0.5°) angular sweep across 36°–40°
   at 750nm/FWHM=2°/GEOM78** — carried from Iteration 27's queue, motivated
   by exp-050's own adjacent-cell threshold-breach finding, independent of
   this cycle's own predictor thread.
5. **Low priority, general engineering debt, largely discharged by this
   cycle's own scope**: the `_geom_derived`/`_G_for_g` hoisting Red Team
   ranked #6 at Iteration 27 is now implemented as the mandatory pattern
   inside exp-051's own `design_geometry.py` (Red Team docket item 2 here);
   worth promoting to a shared utility the next time any cycle builds a
   fourth geometry-parameterized module, but not worth a dedicated slot on
   its own.
