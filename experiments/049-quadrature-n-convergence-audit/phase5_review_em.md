# PHASE 5 — REVIEW · Panel Iteration 26 · exp-049 · Seat: ELECTROMAGNETISM

*Fresh context, blind to the other six Phase-5 reviews. Charter: field/wave
behaviour, impedance matching, energy coupling; owns the reciprocity /
passivity / causality bookkeeping. This is my own Phase-2 attack's cycle —
adjudicated below on what the committed code and data actually show, not on
authorship. Every number below was independently re-run against unmodified
`experiments/042-t21-magnitude-bridge/design_geometry.py`, not read off
`results.json` and trusted.*

---

## 0. Headline

This is the cleanest cycle I have reviewed in this program: every load-bearing
number I independently recomputed matches `results.json` to the printed digit,
the self-caught sign-convention erratum is a genuine, correctly-derived fix
(not a relabeling), and my own Phase-2 attack (P-NCONV26-2's pooled-correlation
masking) was not merely acknowledged but implemented, and Red Team's audit
caught a second, sharper defect in it (the ill-conditioned Δrel near |C|≈0)
that I had missed. The one place this cycle's own prose slightly overreaches
is the "Reading" section's framing of why the T21-period analogy under-predicts
per-cell difficulty — it reads as a generic failure of the heuristic, when the
actual numbers show something more specific and, I think, more interesting.

**Verdict: PROMISING.**

---

## 1. (a) The per-function Spearman split — verified correct, independently reproduced from raw code

I did not trust `results.json`'s `P_NCONV26_2` block on its own. I re-ran all
three `beam_divergence_*` functions directly against unmodified
`experiments/042-.../design_geometry.py` at n=41 and n=81 for all 9 FWHM=20°
cells, applying the Phase-3-corrected exemption formula (`Δrel` if
`|C(81)|≥C_THR`, else a `Δabs`-scaled proxy) and `run.py`'s own `rank_map`
(larger rank = predicted harder), and recomputed `scipy.stats.spearmanr`
myself, from scratch:

```
incoherent            rho = 0.48333333333333334  p = 0.187
incoherent_corrected  rho = 0.4666666666666666   p = 0.205
coherent              rho = 0.45                 p = 0.224
```

This is an **exact** match to `results.json`'s `predictions.P_NCONV26_2`
(0.483/0.467/0.450), computed independently, not copied. I also spot-checked
the underlying `Δrel(41→81)` values feeding this correlation at all 9 cells for
`incoherent` (e.g. 36°/450nm: C(41)=3.553e-4, C(81)=5.240e-6, dabs=3.500e-4 →
exempted, scaled magnitude 0.700; 40°/450nm: C(41)=−2.993e-4, C(81)=5.729e-4,
both below C_THR → exempted, magnitude 1.744) — the exemption logic fires
exactly where `|C(81)|<0.005`, consistent with the corrected criterion's own
text. Cross-checking against `per_cell_summary`'s stored `nstar` values for the
9 FWHM=20° `incoherent_corrected` cells: 5 read `nstar=81` (36°/450, 38°/450,
40°/450, 38°/600, 38°/750) and 4 read `nstar=41` — exactly the "5/9 fail"
`P_NCONV26_1b` reports. **This function is correctly implemented and its
headline ρ values are genuine, not an artifact of a scoring bug.**

**One quantitative check worth stating for the record, because it explains a
pattern nobody's prose calls out explicitly**: `coherent`'s ρ is numerically
**identical** between the Phase-2 informal citation (0.450, uncorrected Δrel
formula) and the Phase-4 corrected-criterion result (0.450). This is not a
coincidence — I confirmed none of the 9 FWHM=20° `coherent` cells ever trigger
the exemption (`|C(41..81)|` runs 0.91–0.99 throughout, two orders above
C_THR), so the ill-conditioning fix that moved `incoherent` from 0.717→0.483
and `incoherent_corrected` from 0.600→0.467 has **zero effect on `coherent`
by construction**. `coherent`'s own difficulty-ranking correlation was never
contaminated by the metric artifact my own attack and QUANTUM's independently
found — it was already the "clean" measurement, and it's still the weakest of
the three (though only marginally, see §3).

## 2. (b) The sign-convention erratum — genuinely fixed, re-derived from first principles

**My own derivation, before reading `run.py`'s inline comment.** P-NCONV26-2's
committed band is "Spearman ρ ≥ 0.70 to CONFIRM." A confirm-worthy result must
mean: cells the physical model predicts are *harder* actually show *larger*
measured aliasing error. For a Spearman correlation to register that as a
**positive** ρ, "predicted difficulty" and "measured magnitude" must be encoded
on the **same-direction** scale — both must increase together for a confirming
result. Since the measured-magnitude series is unambiguous (larger Δrel/Δabs
= more error, by definition), the predicted-rank series must assign its
**largest** value to the **hardest** cell for a confirmed hypothesis to read
positive. That is the only convention under which "ρ≥0.70 to CONFIRM" is a
coherent piece of pre-registered text — you would not design a confirm-bar of
+0.70 for a relationship you expect to be negative.

Checked against `run.py`'s committed `predicted_difficulty_rank()`
(lines 62–88): `order` is built hardest-first (`(36,450)` first,
`(40,750)` last), and the return is `{cell: n - i for i, cell in
enumerate(order)}` — so `(36,450)` (hardest) gets rank `9` (largest) and
`(40,750)` (easiest) gets rank `1` (smallest). **This matches my derivation
exactly**: largest rank ↔ hardest ↔ expected-largest-error, so a genuine
confirmation reads positive. The disclosed original bug — `rank 1` assigned to
the *hardest* cell (an ascending, hardest-first-numbered reading of "hardest→
easiest") — inverts this exactly, and a rank reversal produces an *exact* sign
flip of the Spearman statistic (Spearman ρ is antisymmetric under reversing
either input's rank order: `ρ(reverse(x), y) = −ρ(x, y)`), not an approximate
one. This predicts the disclosed buggy output should be the **exact negative**
of the corrected one, cell for cell.

**I verified this is exactly what `results.json` records.** The
`P_NCONV26_2_ERRATUM_ORIGINAL_BUGGY` block (present, not deleted, exactly as
NOTES.md claims) reads ρ = −0.48333333333333334 / −0.4666666666666666 / −0.45
— the bit-exact negatives of the corrected 0.483/0.467/0.450, with identical
p-values (0.187/0.205/0.224, as expected since |ρ| and its p-value are
sign-invariant). The `meta.phase4_erratum` field independently confirms the
same narrative in prose. **This is a genuine physics/statistics fix, correctly
re-derived, not a relabeling of the same number** — the corrected function
changes the actual rank assignment (`n-i` vs. the buggy `i+1`), and the
resulting sign flip is exactly the algebraic consequence that derivation
predicts, checked to the last digit, not merely "declared fixed."

## 3. (c) Does the "Reading" section's claim hold up against my own Phase-2 finding?

**Short answer: directionally yes, but the section's own framing is looser
than the data supports, in a way worth tightening before this feeds LOGBOOK.**

My Phase-2 attack argued `beam_divergence_coherent`'s error is a
finite-comb grating-lobe artifact governed by the angular-sample spacing
(`Δθ_sample`) against the *observation-window* geometry — a different natural
length scale than `A=752`, the *source*-aperture edge offset that governs the
`incoherent` functions' T21 edge-fringe mechanism (confirmed, in my own
Phase-2 critique, by an independent FFT of both `C_empty(θ)` and the raw
pointwise integrand peaking at the predicted 1.93° period). Red Team
demonstrated this at Phase 2 by computing the pooled-vs-per-function split
before Phase 3 froze anything (ρ = 0.717/0.600/0.450 under the then-uncorrected
formula) — a real gap, my attack's premise held up.

**But the Phase-4 result does not preserve that gap.** Under the
Attack-5-corrected criterion, the three ρ values compress to **0.483 /
0.467 / 0.450** — a spread of only 0.033, all three landing in the same
PARTIAL band, none anywhere near either the 0.70 confirm bar or the 0.30
falsify bar. §1's finding explains *why* `coherent` didn't move (it was never
exposed to the ill-conditioning fix) — but it does not explain why
`incoherent`/`incoherent_corrected`, once corrected, collapsed down to
essentially the same weak correlation as `coherent`, despite my own Phase-2
recomputation independently confirming the T21 fringe genuinely lives in
their integrand. **That is the more interesting finding this cycle actually
produced, and NOTES.md's "Reading" section states it too generically**: "the
T21-period analogy... is not itself a reliable predictor of per-cell
difficulty at this construction" reads as one uniform verdict across all
three functions, when the data supports a sharper one — **even the
mechanistically-confirmed case (`incoherent`, where the fringe is verifiably
present in the raw field) fails to predict per-cell rank order any better
than the mechanistically-distinct case (`coherent`) does.** That is evidence
against a narrower claim than "the analogy is unreliable" — it is evidence
that **period-vs-Nyquist-margin alone, without phase, is too crude a
predictor of per-cell severity even where the underlying periodic mechanism
is real and confirmed**, which is a materially different, more specific
finding than "wrong mechanism, wrong length scale" (my own Phase-2 attack)
or "unreliable analogy, full stop" (NOTES.md's Reading section). T21's own
record already contains the needed clue and this cycle doesn't reuse it: the
live-thread entry attributes the *messiness* of the 450nm/750nm fringe
pattern (vs. 600nm's clean one) to **phase**, not period-vs-sampling-margin —
600nm's period happens to sit nearest the 2° Nyquist-critical point of the
angle grid used there. A natural, cheap, zero-FDTD follow-up (§5.1) is to test
whether adding a phase term recovers predictive power for all three functions
uniformly, which would settle whether the gap is "wrong length scale for
coherent" (my prior) or "missing phase term for everyone" (the pattern the
Phase-4 numbers actually show).

**One further qualifier on all of P-NCONV26-2, not raised by any Phase-2
seat's text as far as I can tell from the record I was given**: at n=9 points,
none of the three Spearman p-values reach conventional significance
(0.187–0.224). The PARTIAL banding (0.30 ≤ ρ < 0.70) is being read as
"weak-but-real positive signal," but at this sample size a true ρ anywhere in
roughly [0, 0.6] would be statistically indistinguishable from the measured
values. This doesn't overturn anything scored (the pre-registered bands
don't require significance, just a magnitude threshold), but it means "all
three show the same direction" is a weaker statement than the "Reading"
section's prose suggests — it is also fully consistent with all three true
correlations being near zero and this cycle having gotten a same-signed
run by chance. Widening the cell grid (more θ₀/λ combinations at FWHM=20°,
zero new FDTD, same desk propagator) would give this specific question real
statistical power; the current 9-cell design cannot.

## 4. Reciprocity / passivity / causality (charter item d)

None applicable, and confirmed none manufactured. `git log` for this cycle's
commits touches only `experiments/049-.../` — zero lines in `lab/` or in
`experiments/042-.../design_geometry.py`. This audit re-evaluates an
already-committed, already-validated desk propagator at different quadrature
orders only; no material law, no new source, no engine change. There is
nothing here that could violate reciprocity, passivity, or causality, and §3's
"T1 escape route: NONE" is accurate — confirmed directly, not accepted on
assertion.

## 5. Ranked top-3 candidate directions

**1. Test a phase-corrected difficulty predictor against the same 9-cell grid
(zero new FDTD, desk-only, cheap).** Per §3: score `Δrel(41→81)` against a
predictor that includes each cell's phase offset within its own local T21
fringe period (`θ₀ mod P(θ₀)`, or equivalently the per-cell deviation from an
integer number of fringe periods across the sampled angular window), not just
`P(θ)` vs. Nyquist margin alone. If this recovers `ρ≥0.70` for `incoherent`
(where the mechanism is confirmed present) while `coherent` still does not
improve, that is the clean, falsifiable test that would finally distinguish
"wrong length scale for coherent" from "missing phase term for everyone" —
the ambiguity this cycle leaves open. Directly reuses this cycle's own
committed grid and functions.

**2. Execute MATERIALS' Attack-1 follow-up trigger: re-run this identical
sweep at exp-048's `A=724`/`NY=1528` fallback geometry.** Idealization 7
correctly scopes this cycle's findings to `A=752` only, and a committed
follow-up trigger was added to PLAN.md/LOGBOOK's queue per the adopted
mandatory fix — but it is not yet done. This is the geometry any actual
near-boundary constraint-3 or realizability-adjacent citation would use
(exp-047/048's own `±35°` fallback line), and the fringe period shortens by a
known, computable factor (752/724 ≈ 1.039×) at that geometry — cheap to check
whether any cell's `n*` crosses a reporting boundary (especially the
FWHM=10°/coherent-FWHM=20° cells nearest their own Nyquist margins).

**3. Widen the FWHM=20° cell grid before trusting P-NCONV26-2's "direction
but not magnitude" reading as settled.** Per §3's statistical-power note: 9
points cannot distinguish a real, weak (ρ≈0.45–0.48) predictive relationship
from chance agreement of an actually-null one. Adding more (θ₀, λ)
combinations at FWHM=20° — still desk-only, reusing the same three functions —
would either tighten the confidence interval around the current point
estimates or reveal they were noise, and is a natural, low-cost companion to
priority 1's phase-corrected predictor (same expanded grid serves both).

---

## Corrections this seat asks the Director to propagate to LOGBOOK at close

1. **T21 addendum**: this cycle (exp-049) formally n-converged
   `gaussian_angle_weights`/`beam_divergence_*` at `A=752`. `n=41` is safe for
   100/108 cell-function combinations there; the 8 coherent-FWHM=20° failures
   and the incoherent_corrected 5/9-FWHM=20° residual need `n*` up to 321
   (measured, not the Phase-1 heuristic's feared 641–1281). Scoped to
   `A=752` only (idealization 7) — not yet validated at exp-048's `A=724`
   fallback geometry (this review's priority 2, above).
2. **T21 addendum, sharper than NOTES.md's own Reading section states it**:
   the T21 fringe-period/Nyquist-margin heuristic does not merely fail to
   predict per-cell difficulty "at this construction" generically — it fails
   comparably (ρ≈0.45–0.48) for BOTH the mechanistically-confirmed
   `incoherent` case (T21 fringe verified present in the integrand, this
   seat's own Phase-2 recomputation) and the mechanistically-distinct
   `coherent` case (grating-lobe comb artifact) — evidence the missing
   ingredient is phase, not mechanism identity. Priority 1, above, is the
   concrete, cheap test that would resolve this.
3. No Checkpoint criterion fires from anything in this review. The one
   process point worth naming for the program's own pattern-tracking (not
   Checkpoint-4-shaped, fully disclosed same-shift, exactly the house
   discipline working as designed): the sign-convention erratum is this
   program's own R4-adjacent good case — a defect self-caught before Phase 5,
   both versions preserved in `results.json`, the fix independently
   re-derivable from the prediction band's own text. Worth citing as the
   positive counter-example the next fix-docket-pattern discussion should
   point to.
