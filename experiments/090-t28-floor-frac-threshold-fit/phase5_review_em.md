# PHASE 5 — REVIEW · ELECTROMAGNETISM (blind) · exp-090 · Panel Iteration 67

*Fresh context, no memory of Phase 2. Read in full: PANEL.md; LOGBOOK.md's
RULED OUT (R1–R14), ESTABLISHED, and LIVE THREADS sections (T1–T28 in
full, including every T28 sub-entry through Iteration 66/exp-089, both
CHECKPOINT entries in that sub-thread); `phase1_proposal.md`, all five
Phase-2 critiques (MATERIALS, ELECTROMAGNETISM — a different, now-finished
sub-agent from this one — THERMODYNAMICS, QUANTUM OPTICS, VISION SCIENCE),
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`,
`run_output.txt`, `results.json`; exp-087/088/089's NOTES.md and
`results.json` for context. All numbers below independently recomputed
from raw primitives with standalone scripts (Python/NumPy/SciPy), not
restated from NOTES.md's or run.py's own prose (R4/R9 discipline). I did
not read any other seat's Phase-5 output for this cycle.*

## Verdict

**CONCUR.** Every load-bearing number in this cycle reproduces bit-exact
under independent re-derivation, using methods deliberately different from
`run.py`'s own (a from-scratch penalized-likelihood optimization via three
different SciPy solvers for Q4, a hand re-derivation of Q8's zero-crossings
by linear interpolation on the raw `thetas`/`delta_scene` arrays, and a
from-primitives recomputation of Q7's noise-floor margin). The one thing
this cycle was specifically asked to get right — correctly demoting P2/P5
from "falsifiable evidence" to "diagnostic sanity check" after my own
prior-cycle Phase-2 self's exchangeability attack — was adopted in full
and is now essentially impossible to misread as independent evidence,
in both the printed output and the committed JSON. I found no arithmetic,
sign, or passivity defect anywhere. Two new, non-load-bearing findings
below (a physical explanation for *why* margin beats distance that
sharpens Q8's own conclusion, and a small ratio-language imprecision in
the same family R9 exists to catch) — neither reverses anything filed.

## 1. Independent recomputation

**Table 1 (7-point `frac_contrast`/`margin`/`ratio_k`) and `FLOOR`.**
Recomputed `frac_contrast(θ) = |delta_scene(θ)|/|C40_C(θ)|` directly from
`experiments/083-.../results.json::per_theta` at all 8 angles (7 fit +
the excluded 38.6°) and `RMS[frac_contrast]` over the full 31-point
window: **bit-exact** to `run.py`'s own values (`FLOOR=1.91744×10⁻⁴`,
`RMS=0.0019174375118374476`). Cross-checked `ratio_k`/`frac_contrast` at
each angle against the *citing* experiment's own committed field
(`exp-087::ratio_k['36.0'/'38.6'/'41.8']`,
`exp-088::ratio_k_new_angles['38.4'/'38.8']`,
`exp-089::ratio_k_new_angles['37.2'/'40.2'/'41.4']`) — all seven values
match to the full printed precision. This is now at least an eighth
independent reproduction of this table across Phase 1, five Phase-2
critiques, and Red Team's Phase-2 audit; I add a ninth from a from-scratch
script rather than trusting the seven-deep precedent alone.

**Q4, Firth's fit — reproduced via a genuinely different numerical route.**
`run.py`'s implementation is the modified-score Newton–Raphson recursion
(`β ← β + (XᵀWX)⁻¹Uᵀ(β)`, `U* = Xᵀ(y−p+h∘(0.5−p))`, `h` the hat-matrix
diagonal). I did not re-implement that recursion — instead I wrote the
Firth *penalized log-likelihood* directly (`ℓ*(β) = ℓ(β) + ½log det(XᵀWX)`)
and maximized it with three independent, derivative-free/quasi-Newton
optimizers (Nelder–Mead, BFGS, Powell), from a zero start, with no
knowledge of `run.py`'s own recursion:

| Method | β₀ | β₁ | m₅₀ |
|---|---|---|---|
| Nelder–Mead | 1.78058957 | −5.63151968 | 2.0710128 |
| BFGS | 1.78058980 | −5.63152256 | 2.0710129 |
| Powell | 1.77978992 | −5.62655164 | 2.0710129 |
| **`run.py` (Newton–Raphson on the modified score)** | **1.78058954** | **−5.63151961** | **2.071012796646712** |

All four agree to 6–7 significant figures — this is not a
same-recursion-twice check, it is confirmation from an entirely different
optimization principle that `run.py`'s Firth implementation is correctly
specified and correctly converged, not merely internally self-consistent.
The stated formula (modified score via the weighted hat matrix) is a
textbook-correct statement of Firth (1993)'s bias-reduction procedure.

**Q1, naive-MLE divergence.** Confirmed independently: a plain
unpenalized Newton–Raphson on the identical `(X,Y)` blows up (I capped at
5000 iterations rather than 200/2000; `|β|` was still climbing past
`10³` with no sign of a finite root) — the qualitative claim (no interior
MLE exists once `AUC=1.0` with no ties, a standard fact about
perfectly-separated logistic data, Albert & Anderson 1984) is correct, and
the exact numeric trajectory differing between `run.py`'s own run (2000
steps, blowup-threshold-terminated at `β≈(26.1,−103.0)`), the Director's
own throwaway script (`β→(65.0,−256.8)` at 2000 steps), and mine is
expected and immaterial — a diverging sequence's position at an arbitrary
stopping rule is implementation-detail noise, not a discrepancy in the
underlying claim.

**Q7, 37.2°'s own resolved-gate noise-floor margin.** Recomputed from
`experiments/089-.../results.json::thermo`/`box_dev` raw fields
(`p_abs_w(C40,37.2°)=2.8127043563514567×10⁻¹²`,
`p_abs_w(G40,37.2°)=2.808672836407139×10⁻¹²`,
`box_dev_max=4.5691305539087015×10⁻⁴`): `noise_floor = 3.0 × box_dev_max ×
p_C40 = 3.855484024115265×10⁻¹⁵`, `Δp_abs = 4.031519944317742×10⁻¹⁵`,
**margin = 1.0456585785601518** — bit-exact to `run.py`'s own figure, and
matching exp-089's own filed "1.046×" (Learned #4) to printed precision,
confirmed by hand from primitives it never re-derived to this precision
before (exp-089 stated it; this cycle and I both independently confirm
it).

**Q8, zero-crossings and distances — independently re-derived by hand
from the raw sign-change data, per this cycle's own assignment.** I loaded
`experiments/083-.../results.json::thetas`/`delta_scene` (31 points, 0.2°
step) directly and located sign changes myself:

- `36.8°→37.0°`: both negative, no crossing. `37.0°(−4.107×10⁻⁴)→37.2°
  (+2.348×10⁻⁴)`: crossing at `37.0+0.2×(4.107/(4.107+2.348))=`
  **37.1273°** (rounds to the filed 37.1272°).
- `38.4°(+8.083×10⁻⁴)→38.6°(−4.151×10⁻⁵)`: crossing at
  `38.4+0.2×(8.083/(8.083+0.415))=`**38.5902°** — exact match.
- `40.0°→40.2°`: both negative (**no** crossing here — I checked this
  explicitly since it is the pair immediately before the cited crossing
  and a careless implementation could mis-locate it one step early).
  `40.2°(−1.541×10⁻⁴)→40.4°(+3.170×10⁻⁴)`: crossing at
  `40.2+0.2×(1.541/(1.541+3.170))=`**40.2654°** — exact match.
- `41.2°→41.4°`: both positive, no crossing. `41.4°(+1.337×10⁻⁴)→41.6°
  (−3.055×10⁻⁴)`: crossing at `41.4+0.2×(1.337/(1.337+3.055))=`
  **41.4609°** — exact match.

All four crossings (`37.1272°, 38.5902°, 40.2654°, 41.4609°`) and all
seven nearest-crossing distances at the fitted angles reproduce
`run.py`'s own values to the printed digit, including the two counter-
intuitive non-monotonicities I checked by hand (40.2° is genuinely closest
to *its own* crossing at 40.2654°, not to the one at 38.5902°; 41.4° is
closest to 41.4609°, not 40.2654°). `AUC(distance)=1.0` and the distance
zone `[0.0654°,0.0728°]` both confirm exactly. **Q8's own core claim —
that both regressors achieve perfect separation but by measurably
different margins — is correctly computed, not merely asserted, and I
verify it from the rawest layer this cycle reaches (the sign-change
arithmetic itself), one level below where Phase 1/3/Red Team stopped.**

## 2. The exchangeability question (this seat's own prior-cycle Phase-2 attack)

A different, now-finished fresh-context EM sub-agent flagged at Phase 2
that the exact permutation test's null (reshuffle `Y` across fixed
margins) is not exchangeable with the actual generative mechanism, since
`margin` is one of `ratio_k`'s own two defining terms and exp-089's own
five-way decomposition already attributes ~90% of the 40.2°/41.4°
classification to the denominator alone. I re-verify the substance of
that attack independently rather than taking my prior self's word for
it: rearranging `Y=1 ⟺ ratio_k>10 ⟺ margin < frac_p_abs/(10·FLOOR)` and
computing the implied per-angle threshold from raw `results.json` fields
gives a 5.55× range (`0.6801`–`3.7724`) comparable to `margin`'s own
6.12× range — confirming, independently, that the label is not exogenous
to the regressor. Red Team's audit upheld this attack (§1.2 of
`phase2_redteam_audit.md`) and correctly compounded it with QUANTUM's
independent, purely order-theoretic attack on P5 (a tie-free `AUC=1.0`
set makes every leave-one-out outcome a deduction, not a discovery) — two
different routes converging on the same underlying fact, which the audit
correctly treats as strengthening, not merely repeating, the case for
demotion.

**Did Phase 3 correctly implement the reclassification, and does the
shipped record actually reflect it?** Yes, on both counts, checked
directly:

- `phase3_synthesis.md` item 6 explicitly reclassifies P2 and P5 from
  "falsifiable predictions" to "diagnostic sanity checks," names the two
  independent findings it rests on, and states P1/P3/P4 remain the
  load-bearing deliverables.
- `NOTES.md`'s own Predictions section labels Q2 "(diagnostic sanity
  check — reclassified from a falsifiable prediction...)" and Q5
  identically; the Result section repeats both labels verbatim next to
  the actual numbers.
- `run.py` itself — the artifact a future cycle would actually import or
  grep, not just the prose around it — prints, in capitals, immediately
  before each number: `"[Q2, DIAGNOSTIC SANITY CHECK ONLY -- not
  independent evidence, see NOTES.md]"` and `"[Q5, DIAGNOSTIC SANITY
  CHECK ONLY -- not a live falsification test, see NOTES.md]"`, and
  `results.json` carries the identical caveat in a `note` field inside
  `q2_diagnostic_only`/`q5_diagnostic_only` themselves — not only in a
  docstring or a comment a future importer might skip.

This is about as hard to misread as independent evidence as a committed
artifact can be made: the caveat travels with the number at every layer
(docstring, print statement, JSON field name, JSON note field, two
document sections). I find no residual path by which a future citation
could quote `p=1/21` or "AUC_LOO=1.0 in all 7 refits" as fresh evidence
without also seeing the demotion. This is a clean, complete discharge of
the attack — a real methodological correction landed, not a wording
softening.

## 3. Two new findings (EM lens), neither load-bearing

**(a) Q8's own conclusion is stronger than its own stated reason — a
physical mechanism the record states qualitatively but never quantifies.**
§5 of `phase1_proposal.md` argues `margin(θ)` is "to leading order near a
simple zero of `delta_scene`... locally linear in `(θ−θ₀)`" — correct,
since `frac_contrast(θ)=|delta_scene(θ)|/|C40_C(θ)|` and `C40_C(θ)` is
smooth and non-vanishing near every crossing. But this argument, as
stated, would predict `margin` and raw distance are *proportional* near
each crossing, which would make them equally good regressors up to a
single global rescaling — it does not, by itself, explain why margin's
zone is measurably *more* robust than distance's (Q8's own finding). The
missing piece is that the local proportionality constant —
`|delta_scene'(θ₀)|/|C40_C(θ₀)|`, i.e. how steeply `delta_scene` crosses
zero at each of the four crossings — is not the same at all four
crossings. I computed it directly from the raw 31-point data by central
finite difference at each crossing:

| Crossing θ₀ | slope `d(delta_scene)/dθ` (per °) | local `d(margin)/dθ` (per °) |
|---|---|---|
| 37.1272° | 3.228×10⁻³ | 5.711×10⁻³ |
| 38.5902° | −4.249×10⁻³ | 7.554×10⁻³ |
| 40.2654° | 2.355×10⁻³ | 4.327×10⁻³ |
| 41.4609° | −2.196×10⁻³ | 4.123×10⁻³ |

The steepest crossing (38.590°) and the shallowest (41.461°) differ by
**1.83×** in local slope. A *raw-distance* threshold is blind to this —
the same 0.06° from two different crossings maps to two different true
`margin` values depending on which crossing it is near, which is exactly
why a fixed-distance cutoff has a thinner effective safety margin than a
fixed-margin cutoff at this sample size: margin already performs the
crossing-specific rescaling a distance-only regressor would need a second,
un-modeled parameter to supply. This sharpens, rather than merely
restates, this cycle's own Learned #3 ("margin carries roughly Nx the
relative safety margin") into a stated physical reason, and it is
independently checkable that the two points setting the *margin* zone's
own edges (40.2°/41.4°) sit at the **two shallowest** of the four
crossings (4.33×10⁻³, 4.12×10⁻³ per degree) — the same two points
MATERIALS' Phase-2 attack (upheld, R3 gap) independently flags as the
most exposed to an unrun spatial-resolution check, for an unrelated but
compatible reason (a shallow local slope means a fixed absolute
grid-quantization perturbation converts into a *larger* relative
`margin` shift there than at a steep crossing). These are two independent
arguments landing on the identical two angles as this method's weakest
point — worth stating together in a future citation, since they compound.

**(b) A ratio-language imprecision in Q8's own "roughly a third"/"roughly
3×" characterization — small, non-load-bearing, but in the family R9 was
adopted to prevent.** `NOTES.md`, `phase1_proposal.md`, and
`phase3_synthesis.md` all describe the distance-zone's gap ratio (`1.1121`)
as "roughly a third of" margin's own gap ratio (`1.4704`), and Learned #3
separately states margin "carries roughly 3× the relative safety margin."
I checked both readings against the actual numbers directly:

- **Literal ratio of the two `gap_ratio` values** (`1.1121/1.4704`):
  distance's is **75.6%** of margin's — margin's is about **1.32×**
  distance's, not 3×, and distance is not "a third of" margin on this
  reading at all.
- **Ratio of each zone's own excess-over-1.0** (i.e. `(hi−lo)/lo`, the
  same "% of lower edge" quantity Q3 itself already reports for the
  margin zone — `0.6946/1.4764=47.0%`): margin's excess is `47.04%`,
  distance's is `11.21%`, a ratio of **4.20×**, not 3×.

Neither of the two natural ways to compare "gap ratio" supports "roughly
a third"/"roughly 3×" precisely — the true multiplicative relationship is
either `≈1.32×` (comparing the raw ratios as printed) or `≈4.20×`
(comparing each zone's relative width to its own lower edge, the more
physically meaningful "safety margin" reading, and the one Q3's own
`width/lo` convention already uses elsewhere in this same document). This
does not change Q8's qualitative conclusion — margin is more robust than
distance under either precise reading, and no classification or verdict
depends on which multiplicative factor is quoted — but a document this
careful about R4/R9 discipline everywhere else (LOGBOOK's own T16 "24×"
saga is the standing cautionary instance for exactly this shape of error)
should state the actual computed factor rather than a round-number
approximation that doesn't match either natural computation of it.
**Recommended fix, cheap, zero-FDTD:** replace "roughly a third"/"roughly
3×" with the precise figure(s) above, or simply cite both raw numbers
(`1.11` vs `1.47`) without an approximate ratio, which is what `run.py`'s
own printed output already does correctly.

## 4. Reciprocity / passivity / causality bookkeeping (this seat's charter)

**N/A for new physics this cycle, correctly and consistently disclosed
throughout** (T1: N/A; Checkpoint criterion 2: N/A) — this is a zero-FDTD
re-analysis of already-committed numbers, not a new field simulation, so
there is no new energy-conservation, reciprocity, or passivity identity
for this cycle to violate or confirm on its own account. I checked for
the only way such a defect could still enter here — silent re-derivation
of a physically-meaningful quantity from raw fields in a way that could
smuggle in a sign or normalization error — and found none: Q7's
`noise_floor`/`Δp_abs` recomputation pulls `p_abs_w` and `box_dev` fields
verbatim from exp-089's own already-gated (`xi_ext`, `nonneg_pass`, T9
`ratio_abs_ext` anchor) record without re-deriving them from field
primitives, so it inherits, rather than re-risks, that cycle's own
passivity bookkeeping (already independently checked by a different EM
sub-agent's Phase-5 review of exp-089, and by that cycle's own five Phase-2
critiques and Red Team audit — not re-litigated here, correctly, since
nothing in this cycle touches the underlying fields). No sign flip,
no non-physical negative quantity, and no unit/normalization mismatch of
the R9 kind (I checked `margin`, `frac_contrast`, `ratio_k`, and the two
`gap_ratio`s are each used as dimensionless ratios of like-normalized
quantities throughout — unlike T16's own historical `amp_ratio`-vs-`C_thr`
error, nothing here divides two operands drawn from different
normalization conventions).

## Ranked top-3 for Iteration 68

1. **The still-overdue R3 spatial (`cpl` 20→30) resolution check on the
   `frac_contrast`/`ratio_k` channel — now doubly motivated, not merely
   overdue.** MATERIALS' Phase-2 attack (upheld) already names 40.2°/41.4°
   as the load-bearing, most-exposed points because they sit nearest a
   real zero-crossing; §3(a) above adds an independent, quantitative
   reason those exact two points are the *shallowest*-slope crossings of
   the four on record (4.12–4.33×10⁻³/° vs. 5.71–7.55×10⁻³/° at the other
   two), meaning a fixed grid-quantization perturbation converts into a
   proportionally larger `margin` shift there than anywhere else this
   method touches. This is the single check most likely to actually move
   the caution zone's own lower edge, not merely narrate an
   already-known gap.
2. **A repeat or denser FDTD measurement at/near 37.2° specifically**
   (NOTES.md's own Next item 5, RT-1's own disclosure gate) — it
   simultaneously sets the caution zone's upper edge, anchors Firth's
   `m₅₀` at its shallow end, and already carries a pre-existing,
   independently-reconfirmed 1.046× resolved-gate margin ("a felt-lucky
   pass"). This is the single most information-dense next FDTD call on
   the whole T28 board by this cycle's own accounting, and nothing in
   this desk cycle's own machinery can resolve it.
3. **The still-queued R14(b) formal, null-controlled period fit against
   the raw signed `p_abs(G40,θ)−p_abs(C40,θ)` difference**, informed now
   by both exp-089's own 4-fold sign-alternation finding and §3(a)'s own
   per-crossing slope table above (a genuine single-tone model should, if
   it holds, predict the *relative* size of the sign-alternation gaps
   near each crossing to scale with these same local slopes — a concrete,
   cheap, zero-FDTD cross-check this fit's own by-product data now makes
   possible for the first time, tying two previously separate T28
   instruments together).
