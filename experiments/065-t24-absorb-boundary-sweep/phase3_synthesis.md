# PHASE 3 — SYNTHESIS · Panel Iteration 42 · Director

Resolves the exp-065 debate (Phase 1 proposal, five blind Phase-2 critiques,
Red Team's Phase-2 audit) into ONE testable configuration. The Director does
not vote in Phase 2 and states here, explicitly, which criticisms are
accepted and which are overridden, and why.

## Ruling on Red Team's verdict

**Accepted in full: PROCEED-WITH-MANDATORY-FIXES, all 11 items, zero
overrides.** No seat's finding is disputed here. Every attack Red Team
sustained was independently re-verified by Red Team itself against a primary
artifact (direct script execution, direct code read, direct file read), not
merely relayed from a blind critique, and the Director re-checked the two
load-bearing ones independently again before accepting them (below). No
Checkpoint criterion fires — concurred, on the same ground Red Team gives:
this is Phase 2 catching defects before Phase 3 freeze, the designed
mechanism, not a violation of it.

## Independent Director re-check of the two load-bearing attacks

**Attack 1 (integer-λ aliasing).** Recomputed `ABSORB/cpl` at
`ABSORB=70, cpl∈{15,20,25}`: 4.667 / 3.5 / 2.8 — none an integer. Confirmed
`ABSORB=50` fails at 750nm (`50/25=2.0`) exactly as Red Team found. `70` is
the correct fourth point.

**Attack 2 (causal-step derivation).** Traced `lab/fdtd2d.py::Sim.run`
myself: the leapfrog H-then-E composition gives `Ez(new,i,j)` depending on
`Ez(old,i,j)` and its four nearest neighbors — a 5-point cross, domain of
dependence exactly 1 cell/step, independent of `courant_frac`. `S` bounds
the *physical* wavefront, not the *discrete stencil's* nonzero-support
boundary; these are different lines, and R2/T16/T21/R5's whole lesson is not
to conflate a modeled-physics bound with a numerical one. Confirmed: the
rigorous step is `floor(263/1) − 16 = 247`, not 359.

## Mandatory-fix docket — disposition (all 11 accepted, applied at Phase 3)

| # | Fix | Applied as |
|---|---|---|
| 1 | 4th `ABSORB` point, non-aliased at all 3λ | `ABSORB=70`, added to Block SWEEP, 18 more calls |
| 2 | Recompute `causal_identity_step` at 1-cell/step | `n=247` replaces `n=359` — **and this VOIDS the gate** (247 < 319 arrival). G-2 replaced by a strictly stronger zero-step static check; see the P-VIS42-1b entry below. Fired the proposal's own halt condition at the desk stage. |
| 3 | Dense angular mini-sweep, falsifies "cancels to first order" | `≤0.5°`-step scan over one T21 fringe period at 600nm, `C80−C40` |
| 4 | Cite `REALIZABILITY_MEMO.md`'s UNOBTANIUM + Amendment for τ=0.0065 | inline at P-VIS42-7 |
| 5 | `0.00449` figure: code-produce or strike | computed in `design_geometry.py`, T15 non-portability caveat inline |
| 6 | Cite T5/Iteration-20 UNDETECTABLE finding | one sentence at P-VIS42-7/§5 |
| 7 | Settling check at largest padded domain | `ABSORB=80`, `STEPS=2800` vs `1400`, 2 extra calls |
| 8 | Name the CNT `R_contact` trade-off explicitly | one sentence added to §0 |
| 9 | Soften §8.2: G-1/G-2 authorize, don't pre-validate | wording only |
| 10 | ±35° anchor: cite if exists, else disclose gap | checked — no prior ±35° committed figure at this geometry found; disclosed as a gap in idealization 4 |
| 11 | Clarify fringe-shift vs. fringe-period are distinct derivatives | one sentence, §2.4 |

**Revised FDTD budget** (computed by the amended `design_geometry.py`, not
estimated): **144 calls**, projected CPU 72.7 min, **projected wall 21.3
min** at the measured 4-worker cost basis, 3× safety envelope 64.0 min —
inside the 90-minute hard stop with room. Block totals: SWEEP 90 (C40/C60/
**C70**/C80/N60 × 18), PAD 9, ARTICLE 32, BEAM 6, **MINI 6** (only
38.5/39/39.5 are new; 38 and 40 are reused from SWEEP, not re-run),
**SETTLE 1 physical call** at 2× step cost. De-scope order (proposal §7.4)
stands unchanged, extended by a **`D0` ranked before D1**: drop the fix-7
settling call first (a robustness disclosure, not a scored prediction).
The fix-1 C70 legs are ranked **immediately after D1** in the de-scope
order — ahead of C60's flanking wavelengths — because C70 is the design's
only non-aliased point and dropping it would restore the exact defect
Red Team's attack 1 exists to close.

## Predictions — frozen before Phase 4

**P-VIS42-1 through P-VIS42-9 stand as written in `phase1_proposal.md`**,
with these amendments, frozen together as the complete pre-registered set
(verbatim text goes into `NOTES.md`, printed structurally by `run.py` before
any FDTD call, per house discipline):

- **P-VIS42-1b REPLACED — the cycle's first unplanned find, and it is a
  real one.** Applying Red Team's fix 2 did not merely tighten the number;
  it **voided the gate**. The corrected bound is `n=247`; the direct
  source→plane signal arrival is `ceil(D_SP/S) = ceil(223/0.700036) = 319`.
  **247 < 319** — there is no step at which real signal has reached the
  observation plane AND the boundary-difference region provably cannot
  have. The dynamic field-snapshot gate as written in `phase1_proposal.md`
  has **no valid window at this geometry**, and appeared valid only under
  the overstated `n=359` bound EM caught. This is precisely the halt
  condition the proposal pre-registered ("if (c) fails, the cycle stops")
  — fired at the **desk stage, before any FDTD call, at zero cost**.

  **Diagnosis: the dynamic argument was the wrong tool for the claim.**
  What G-2 existed to certify is that the padded region is a pure vacuum
  extension and the shared footprint's scored windows are unperturbed by
  the coordinate shift. That is a **static** fact about the damping
  arrays, not a transient one. `Sim.__init__` alone builds
  `damp_e`/`damp_hx`/`damp_hy` — zero `.run()` steps — so the claim can be
  checked directly and bit-for-bit.

  **G-2 is therefore replaced by `static_construction_identity()`**: build
  both `Sim` objects at zero steps, compare `damp_e` and `damp_hx` at the
  actual scored-window cells (object window, both flanks) on the
  observation plane, C40 vs G40 offset by `pad=40`. **Result, executed
  this shift: `max|diff| = 0.000e+00` at all six window×array
  combinations, and the scored window is confirmed pure vacuum
  (`damp_e == 1.0`).** This is *strictly stronger* than the gate it
  replaces on two counts: it holds at **every** time step rather than
  before some causal horizon, and it targets the static arrays where a
  construction bug (coordinate-shift error, off-by-one, asymmetric pad)
  actually lives, rather than inferring their correctness from wave
  propagation. It also, unlike its predecessor, has a valid domain.

  **P-VIS42-1b's new statement**: `static_construction_identity(C40, G40,
  pad=40)` returns `max_diff == 0.0` exactly and `all_vacuum == True`.
  CONFIRM: both hold. REFUTE: any nonzero diff, or a non-vacuum scored
  window ⇒ the padded domain is not a pure vacuum extension, §1's
  congruence argument fails, and the cycle halts before any sweep number
  is read. **Already executed and PASSED pre-freeze** — recorded here as
  a passed gate, not a pending one.
- **P-VIS42-2 amended**: scored over 18 original cells **plus** the 18 new
  `ABSORB=70` cells (6θ × 3λ); the three-`ABSORB`-point monotonicity read
  becomes a four-point read. Bands unchanged in value, widened in coverage.
  **New sub-clause P-VIS42-2a (the aliasing discriminator Red Team's attack
  1 demands):** at 600nm, C70 (`ABSORB/λ = 3.5`, non-integer) is compared
  against the interpolated midpoint of C60 (3λ) and C80 (4λ). CONFIRM
  (smooth, non-aliased boundary trend): C70's `ΔC_empty(C70−C40)` sits
  within ±40% of the C60/C80 linear interpolant at all 6 cells. REFUTE
  (aliasing real, the headline is contaminated): C70 departs from the
  interpolant by >2× at ≥3 of 6 cells, or falls outside the [C60, C80]
  bracket entirely — in which case P-VIS42-2's headline must be reported
  as aliasing-bounded, not clean, and the verdict capped at PARTIAL.
- **New P-VIS42-10 (fix 3)**: the dense angular mini-sweep. `ΔC_empty(θ) =
  C_empty(C80,θ) − C_empty(C40,θ)` over a ≤0.5°-step scan spanning ≥1 full
  T21 fringe period at 600nm (`P(40°)=1.989°` per §2.4 — span ≥2° centered
  near θ=38–40°, ~5 angles). CONFIRM (additive-systematic framing holds):
  the delta stays within ±30% of its own mean across the span (flat, no
  oscillation). REFUTE (coherent-fringe-perturbation framing): the delta's
  peak-to-trough range exceeds 2× its own mean, at a spatial period matching
  `P(θ)` to within 20%.
- **New P-VIS42-11 (fix 7)**: settling robustness. `|C_empty(ABSORB=80,
  STEPS=2800) − C_empty(ABSORB=80, STEPS=1400)|` at one representative cell
  (θ=40°, 600nm). CONFIRM: comparable to exp-046's own 0.083%/0.036%
  beam-channel settling figures (i.e. ≤0.15% relative). REFUTE: >1%
  relative — settling, not boundary reflectivity, would then be a live
  confound on P-VIS42-2's headline, and the headline must be reported as
  bounded by this uncertainty rather than clean.

No prediction is deleted; P-VIS42-1 through -9's original CONFIRM/REFUTE
bands are otherwise unchanged from `phase1_proposal.md`.

## Idealizations — unchanged from `phase1_proposal.md` §6, plus

11. (fix 10) No prior committed `±35°×3λ` `C_empty` figure exists anywhere
    in this program's record at a directly comparable geometry — checked
    against `experiments/041-.../results.json::block_main`
    (`FALLBACK_ANGLES`-family coverage is `{-40..-36, 36..40}` only, a 1°
    T21 fringe scan, no ±35°). P-VIS42-1's absolute-identity anchor is
    therefore silent on the ±35° legs that Block SWEEP's headline and Block
    ARTICLE's N9 aggregate both use. Not fatal — an implementation bug
    specific to only the ±35° angle codepath and no other would be an
    unusual failure mode — but disclosed as a real gap, not closed.

## Forward tripwire (Red Team's, adopted)

If Phase 3 had shipped without either fix 1 or fix 2 and a later cycle found
either omission load-bearing for a wrong conclusion already in LOGBOOK.md,
that would be a program-integrity finding. **Moot for this cycle — both are
applied below** — but the tripwire is recorded verbatim for the record, in
case a future re-derivation of this experiment's own numbers ever skips
them.

## Gates

Unchanged from `phase1_proposal.md` §8: full bench
(`--only 12346789,10,11,18,19,20,21,22,23,24`) green before and after; no
new trust-suite stage (position unchanged, fallback offer stands); house
discipline (predictions frozen before `run.py`'s first execution; Evidence
Gate on artifacts; R3/R4/R5 as amended above).

---

*Director's synthesis, Panel Iteration 42, Phase 3. Proceeding to build
`run.py` implementing Blocks SWEEP (4 `ABSORB` points × 6θ × 3λ + the
`ABSORB=70` extension), PAD, ARTICLE, BEAM, the fix-3 dense mini-sweep, and
the fix-7 settling check, then Phase 4 execution.*
