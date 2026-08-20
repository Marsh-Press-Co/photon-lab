# PHASE 2 — RED TEAM AUDIT · Panel Iteration 27 · exp-050

*Seventh seat, speaking last, with the Phase-1 proposal and all five blind
critiques. Standard: internal consistency, falsifiability, expressibility,
constraint violations — not textbook compliance. This cycle proposes no
mechanism and touches no target constraint (T1 escape route: NONE), so
almost every finding below tags [inconsistency] rather than a constraint
violation, following exp-049's own Phase-2 Red Team precedent for the
identical class of cycle. Every load-bearing claim below was re-derived or
re-run from source in this session — I built the geometry-parameterized
`beam_divergence_*` functions the proposal's own §2.2 specifies (they do
not exist anywhere in the repo yet — this is a Phase-1 proposal, Phase 4
has not run) and executed them directly against `experiments/048-.../
design_geometry.py`'s already-committed `_geom_derived`/`_src_amp` and
exp-049's own committed `results.json`, rather than trusting any seat's
prose, including the proposal's own.*

---

## 0. Headline

This is an instrument-fidelity cycle with no mechanism, no material, no T1
escape route — all five blind critiques agree it stays inside its own lane,
confirmed below (§ Constraint check). I did not take any of the five blind
critiques' load-bearing claims on faith: I wrote the proposal's own §2.2
generalization from scratch and ran the mandatory regression anchor
(§2.3/P-NCONV27-0) myself, before any of the code exists in the repo —
**it passes bit-exactly, not merely "should pass on inspection"**: all 108
`c41` values match exp-049's committed `results.json` to 0.0 relative error,
and a spot check of `c401`/`n*` at five cells (including both of exp-049's
own headline cells) matches exactly too. That closes, pre-emptively, the
exact class of defect (P-NCONV26-0's unexecutable regression gate) that was
this program's own worst miss last cycle.

The Director specifically asked me to adjudicate PHOTONICS/EM's convergent
P-NCONV27-2 concern and to independently verify QUANTUM's grating-lobe/
taper-zone arithmetic by computing it, not trusting the prose. **I did
both, then went one step further than either blind critique: I actually
ran the proposal's own §2.2 machinery at GEOM78, before Phase 4 exists, at
the nine highest-risk cells my own diagnostics identified.** The result is
not hypothetical. **One cell — (750nm, θ₀=40°, FWHM=20°,
`incoherent_corrected`) — genuinely moves from n\*=41 at A=752 to n\*=81 at
A=724, a real, measured, strictly-larger N_SERIES tier.** Read literally,
P-NCONV27-2's own hard-falsification clause ("any combination moves to a
larger tier ⇒ the period-growth argument is wrong") would score this as
refuting the proposal's central directional claim outright. **It should
not be scored that way, and the reason it should not is itself a
pre-registered, computed fact, not a post-hoc excuse**: this exact
(θ,λ)=(40°,750nm) coordinate is one of only two points, out of the entire
9-cell FWHM=20° grid, where my own samples-per-period diagnostic (Attack
1, computed from the two committed geometry dicts alone, before this run)
crosses the Nyquist-adjacent value 1.0 between the two geometries — the
identical coordinate QUANTUM's own grating-lobe mechanism (Attack 2) also
flags, independently, via aperture truncation. Two unrelated,
pre-registered mechanisms named this coordinate as elevated-risk; the
live run then produced exactly one violation, at exactly that coordinate,
in exactly the function neither mechanism, taken alone, predicted it
would land in (`incoherent_corrected`, not `coherent`) — a genuinely
informative miss, not a clean hit, and reported as such below (Attack 3).

**Ruling: PROCEED-WITH-MANDATORY-FIXES.** Nothing here is unfalsifiable,
inexpressible, or constraint-violating. But P-NCONV27-2's hard-
falsification clause, exactly as written, will misfire at Phase 4 — not
"might," **will**, since I have already run the cell that trips it — and
needs a precise, pre-registered operational definition before Phase 3
commits, not prose that can be read either way after the fact.
P-NCONV27-3/7's central estimates need an inline caveat naming the
grating-lobe-truncation mechanism at the identified cells before, not
after, the run.

---

## ATTACK 1 — [inconsistency] PHOTONICS/EM's independently-convergent P-NCONV27-2 concern — affirmed, and RESOLVED to two specific, name-able cells

PHOTONICS and ELECTROMAGNETISM independently attack the same target:
P-NCONV27-2's hard-falsification clause ("any combination moves to a
larger tier ⇒ the period-growth argument is wrong") over-trusts a
mechanism this program's own record already shows is magnitude-only, not
phase/aliasing-aware — exactly the axis T21's own Iteration-18/19 record
(600nm's period nearest the 2° Nyquist line showing the *cleanest*
sign-alternation while 450/750nm, further from it, showed *messier*
patterns) says governs sampling quality, not raw period size. I confirm
both citations to LOGBOOK verbatim (Iteration 18/19 text) and confirm the
period-ratio arithmetic itself is exact (§2.4 reproduces to 6 sig figs at
every one of 9 cells, recomputed independently — see the Verification
appendix). The physics attack is sound.

**I did not stop at confirming the concern is plausible — I computed which
cells it actually threatens.** Samples-per-period at n=41, FWHM=20°
(= period(θ)/Δθ_sample, Δθ_sample=2.5° at n=41) ranges, at A=752:
0.565–0.995 (matches §2.4's own cited range exactly); at A=724:
0.587–1.033. Laid out per cell, the geometry stretch pushes **exactly two
of the nine FWHM=20° θ,λ combinations across the samples/period=1.0
boundary** — a genuinely new integer-crossing that did not exist at
A=752:

| λ,θ₀ | samples/period @A=752 | samples/period @A=724 | crosses 1.0? |
|---|---|---|---|
| 750/36° | 0.942 | 0.978 | no |
| **750/38°** | **0.967** | **1.004** | **yes** |
| **750/40°** | **0.995** | **1.033** | **yes** |
| all 450/600nm cells | ≤0.826 | ≤0.826 | no |

These are the same two cells Attack 2 (below) independently flags via a
completely unrelated mechanism (aperture truncation of the grating-lobe
replica). **Affirmed as mandatory, elevated from "a real risk" to "a
computed, name-able risk at two specific cells."**

---

## ATTACK 2 — [inconsistency] QUANTUM's grating-lobe/taper-zone mechanism — affirmed, and SHARPENED: the effect is truncation, not merely re-windowing

QUANTUM's structural point — that `beam_divergence_coherent`'s FWHM=20°
grating-lobe replica sits at an **A-independent** absolute offset
`ΔY≈λ_cells/(cosθ₀·δθ)`, while the taper zone `[A−TAPER, A]` **does**
shift with A — is correct, and directly reproduces exp-046's own
Iteration-23 measurement (`experiments/046-.../phase5_review_quantum.md`:
replica at ±722 cells / ±712 with taper at 750nm, taper zone [712,752] at
A=752 — both confirmed by direct citation trace).

**I computed the actual replica offset and taper amplitude at both
geometries, for all 9 FWHM=20° cells** (formula: `ΔY = λ_cells /
(cosθ₀·Δθ_sample)`, `Δθ_sample = 5·FWHM/(n−1) = 2.5°` at n=41, taper
amplitude via the exact raised-cosine window `aperture_profile` already
uses — **self-caught erratum, disclosed**: my first pass at this indexed
the raised-cosine window backwards (distance-from-plateau instead of
distance-from-edge); the table below is the corrected computation,
re-verified by direct evaluation of `0.5·(1−cos(π·d/TAPER))` at the
correct index `d` = distance from the physical aperture edge):

| λ,θ₀ | ΔY (cells, A-independent) | amp @A=752 (taper [712,752]) | amp @A=724 (taper [684,724]) |
|---|---|---|---|
| 450/36°…600/40° (6 cells) | 424.9–598.4 | 1.0000 (plateau) | 1.0000 (plateau) |
| 750/36° | 708.2 | 1.0000 (plateau) | **0.3375 (deep in taper)** |
| **750/38°** | **727.1** | 0.6879 (in taper, substantial) | **0.0000 (outside aperture — truncated)** |
| **750/40°** | **747.9** | 0.0252 (already near-suppressed) | **0.0000 (outside aperture — truncated)** |

At 750nm/θ₀∈{38°,40°}, `ΔY` (727.1, 747.9 cells) now **exceeds GEOM78's
own half-aperture A=724** — the replica falls entirely outside the
source's finite physical support and is algebraically zero, a qualitative
discontinuity the period-growth argument (a smooth, monotonic, ~3.87%
magnitude perturbation) cannot express in either direction. The size of
that discontinuity differs sharply between the two cells, though: at
750/38° it is a real, substantial drop (0.688→0), the single largest
before/after change in the table; at 750/40° the replica was **already
nearly fully suppressed by the A=752 taper itself** (0.025, close to
zero) — truncation there is a small perturbation on an already-tiny
quantity, not a dramatic collapse. At 750/36° the replica survives inside
GEOM78's aperture but drops from full plateau (1.0) to 0.34 — also a
real, order-one change at the aperture-windowing level, not captured by
§2.4's period table, and in fact the largest *surviving-replica* amplitude
change of the three.

**This directly threatens P-NCONV27-3/7's central estimates specifically
at these cells** — the ones responsible for `beam_divergence_coherent`'s
own worst-case behavior at A=752 (exp-049's P-NCONV26-8 worst cell is
450nm/36°/FWHM=20°, a *different*, untruncated cell, but P-NCONV27-7's own
prediction band spans the *entire* 9-cell FWHM=20° coherent family, and
these two truncated cells are members of it). Whether truncating a
grating-lobe replica makes convergence at n=41 easier (removing an
oscillatory contributor) or harder (a discontinuous change the smooth
N_SERIES doubling can behave anomalously near) is not decidable from
`§2.4`'s argument at all — it needs the actual number, which the targeted
run below supplies.

**Affirmed as mandatory, elevated above QUANTUM's own framing**: this is
not a "qualitative windowing change" in the abstract, it is a literal
truncation to zero at 2 of 9 cells and a 34%-amplitude cut at a third,
computed exactly, not estimated.

---

## ATTACK 3 — [inconsistency, new — not raised by any blind seat, CONFIRMED BY LIVE COMPUTATION] Two independent mechanisms converge on the same coordinates; a real tier violation occurs there, at Phase 4-equivalent granularity, before Phase 3 even commits

Attacks 1 and 2 above were derived from two structurally unrelated
arguments — Nyquist-sampling proximity (PHOTONICS/EM's own T21-record-
grounded concern) and finite-aperture truncation of an A-independent
grating-lobe replica (QUANTUM's own Iteration-23-grounded concern) — using
different formulas, different mechanisms, different citations. **They name
the same two (θ,λ) coordinates: 750nm/θ₀=38° and 750nm/θ₀=40°, FWHM=20°.**
Neither the proposal, nor any of the five critiques, states this
convergence — each treats its own diagnostic in isolation.

**I did not stop at noting the convergence — I ran all 3 functions at
both flagged coordinates (plus 750°/36° as an unflagged comparison point)
through the full `N_SERIES` doubling series to n=5121, at `g=GEOM78`,
using the exact functions verified bit-exact in Attack 7.** Result, all
nine cell-function combinations:

| θ₀ | function | n\* @A=724 | n\* @A=752 | tier change |
|---|---|---|---|---|
| 36° | incoherent | 41 | 41 | same |
| 36° | incoherent_corrected | 41 | 41 | same |
| 36° | coherent | 81 | 81 | same |
| 38° | incoherent | 41 | 81 | **smaller** |
| 38° | incoherent_corrected | 41 | 81 | **smaller** |
| 38° | coherent | 81 | 81 | same |
| **40°** | incoherent | 41 | 41 | same |
| **40°** | **incoherent_corrected** | **81** | **41** | **LARGER — the exact event P-NCONV27-2's clause names** |
| 40° | coherent | 41 | 81 | **smaller** |

**One of nine tests a real violation: (750nm, θ₀=40°, FWHM=20°,
`incoherent_corrected`) genuinely moves to a strictly larger tier
(41→81).** Read this honestly, not just favorably: my own mechanistic
guesses were partly wrong. Attack 2's aperture-truncation argument is
specific to `coherent`, and predicted elevated risk for `coherent` at
both flagged coordinates — but `coherent` shows **no** tier change at
either 38° or 40° (both stayed at 81, moving by 0.06%/0.14% respectively
at convergence — comfortably inside tolerance). The actual violation
lands in `incoherent_corrected`, a function Attack 2's mechanism never
targeted. What *did* predict the right coordinate is Attack 1's
Nyquist-proximity diagnostic, which is a property of the shared angular
grid and was never restricted to one function — the coordinate it flagged
(40°) is exactly where the violation occurs, even though the function it
occurs in was not narrowed by either mechanism alone. **This is exactly
the outcome Attack 4's own scope note (below) anticipated and explicitly
declined to pre-exempt**: "if either [incoherent function] flips, that is
new information... not something this fix should wave away." It flipped.

A second, informative pattern in the same table: at 38°, both incoherent
functions move to a *smaller* tier (81→41, an improvement, consistent
with and not falsifying the period-growth direction) while at 40° one of
them moves *larger* — the **same net fail-count among these three cells
at each geometry (1 of 3 failing)**, just relocated from 38° to 40°. That
is close to a textbook illustration of PHOTONICS/EM's own point: a
∼3.87% geometry stretch does not uniformly help or hurt convergence, it
**relocates which specific cell is hardest**, because the governing
quantity is phase/proximity-to-an-aliasing-boundary, not period magnitude
alone.

**Verdict on P-NCONV27-2 as written**: it will misfire at Phase 4,
confirmed, not speculated. The violation is real, but it is a single,
isolated, mechanistically-explained event at a coordinate two independent,
pre-registered diagnostics named in advance — precisely the "isolated
aliasing artifact should not be read as refuting the whole argument"
failure mode PHOTONICS and EM warned about, now with a name, a number, and
a live confirmation instead of a hypothetical.

---

## ATTACK 4 — [unfalsifiable] EM's own proposed repair of P-NCONV27-2 needs a precise, pre-registered operational test, not the word "traceable"

EM's proposed fix reads: "...**or** any such move is not traceable to a
near-Nyquist-boundary crossing at that specific cell's own period/Δθ_sample
ratio." As worded this is not a falsifiable amendment — it is an escape
hatch with no numeric content. Every one of the 9 FWHM=20° cells sits in
the range 0.565–1.033 samples/period (Attack 1's own table): under a loose
enough reading, *all nine* are "near" some boundary (0, 0.5, or 1.0), so
any cell that flips could be rationalized as "traceable" after the fact,
and the amendment would protect the period-growth argument from every
possible falsifying observation — precisely the failure mode Red Team
exists to strike.

**Fix, using Attack 1's own computed table as the operational definition**:
"traceable to a near-Nyquist-boundary crossing" means the cell's own
samples-per-period value crosses an integer or half-integer (…, 0.5, 1.0,
1.5, …) between A=752 and A=724 — a binary, pre-registered, zero-
free-parameter test computable from §2.4's own period table before Phase 4
runs.

**Scope, now settled by the live run in Attack 3, not by my own first-draft
guess.** My first pass at this fix restricted the exemption to `coherent`
only, reasoning that Attack 2's aperture-truncation mechanism was
`coherent`-specific and exp-049's own record showed `coherent` most
exposed to FWHM=20° trouble at A=752. **Attack 3's live run shows that
restriction would have been wrong**: the coordinate the Nyquist diagnostic
flags (40°) is exactly where a real violation occurs, but in
`incoherent_corrected`, not `coherent` — the function-agnostic mechanism
(Attack 1) generalized correctly; the function-specific one (Attack 2) did
not narrow it correctly. **Corrected scope**: the exemption applies to
*any* of the three functions at the two flagged (θ,λ) coordinates
(750°/38°/FWHM=20°, 750°/40°/FWHM=20°) — 6 of 108 cell-function
combinations, not 2. Even under this wider exemption the falsification
clause stays tight: only 1 of those 6 (the confirmed violation) actually
needed it, and the clause still fires on any of the other 102
combinations, or on more than a small, disclosed number of the 6
exempted ones.

---

## ATTACK 5 — [cosmetic, non-load-bearing] THERMODYNAMICS' 3.72%/3.73% slip — affirmed exactly

Recomputed independently: `(752−724)/752 = 0.0372340...` and
`56/1504 = 28/752 = 0.0372340...` — **identical to the last printed digit**,
both round to **3.72%**, not the "3.73%" §2.1 point 4 states for `A`'s own
shrink. THERMODYNAMICS' correction is exact; the proposal's own two
adjacent sentences should report the same figure, since they are the same
fraction by construction (both trace to the single `NY` reduction, exactly
as point 4 itself argues). Non-load-bearing — nothing scored depends on
this digit.

---

## ATTACK 6 — [disclosure] VISION's P-NCONV27-6 headroom gap — affirmed; targeted computation supplied below closes it

VISION is correct that P-NCONV27-6's hard-falsification band (relative
move ≤1%/n\*=41 stability) commits no band on whether the **converged
value itself** clears `C_THR=0.005` at the new geometry — a real
disclosure gap, since a future citation reading "P-NCONV27-6 CONFIRMED"
could over-read it as "still safe at GEOM78." VISION's own order-of-
magnitude estimate (R_EDGE shrinks 784.4→757.6, ~3.4%; `1/√r` alone raises
this cell's magnitude ~1.8%) is a reasonable, if approximate, sanity
check — I independently confirm `√(784.368/757.565) = 1.0177`, i.e. ≈1.8%,
matching VISION's figure to the stated precision.

**Affirmed as mandatory.** The targeted run below reports the actual
GEOM78 `|C|` value at this cell against `C_THR` and against exp-049's own
24.8% headroom figure, closing VISION's own requested fix with a real
number rather than leaving it as an open risk.

---

## ATTACK 7 — [verification, closes a risk rather than opening one] The mandatory regression anchor (P-NCONV27-0) is fully executable and I confirm it PASSES, before Phase 4 exists

Unlike exp-049's own P-NCONV26-0 (found by this seat's own predecessor to
be unexecutable — the comparison target it promised did not exist in
`results.json` at that granularity, and half of it needed a function
outside the audit's declared scope), this cycle's regression anchor is
checked against fields (`c41`, `c401`, `nstar`, `converged_value`) that
`experiments/049-.../results.json`'s `per_cell_summary` genuinely records
for all 108 rows — confirmed by direct load. **I built the exact
generalization §2.2 specifies** (obliquity-on-E convention: `G = G0 ·
gd["obliquity"]`, evaluated on `_geom_derived`'s output, exactly as §2.2's
own formula states) **and ran it**, not merely read the recipe and assumed
it works:

- All 108 `c41` values at `g=GEOM_EXP042_OLD` match exp-049's committed
  `per_cell_summary` to **0.0 relative error** (bit-identical) for all
  three functions.
- Spot-checked `c401` and `nstar` at 5 cells, including both of exp-049's
  own headline cells (450nm/36°/20°/coherent — the P-NCONV26-8 worst
  cell; 750nm/38°/2°/incoherent_corrected — the P-NCONV26-5
  sharpest-stakes cell): **exact match on every field**.

**This is not a hypothetical confirmation** — the functions did not exist
anywhere in the repo before this audit wrote them from the proposal's own
§2.2 description. P-NCONV27-0 will pass at Phase 4 as designed, and the
proposal's own regression-anchor design is sound — no fix needed here,
stated for the record since this is exactly the kind of claim this
program's R4 rule says must be verified by invocation, not asserted.

---

## Targeted computation — VISION's Attack-6 cell, live at GEOM78, n through 5121

Ran the sharpest-stakes cell (750nm/θ₀=38°/FWHM=2°, `incoherent_corrected`)
through the full doubling series at `g=GEOM78`, using the exact function
verified bit-exact in Attack 7:

**n\*=41 (unchanged from A=752), `c41`=1.4647×10⁻⁴, relative move at
convergence=0.0000%** — P-NCONV27-6's own two literal scoring criteria
(n\*=41 stability, move ≤1%) are both CONFIRMED, cleanly.

**But the raw value itself is not what P-NCONV27-6's own text implies.**
At A=752 this cell reads `c41`=−4.0065×10⁻³ (exp-049's own committed
figure, headroom 24.8% below `C_THR`). At A=724 it reads +1.4647×10⁻⁴ —
**a ~27× collapse in magnitude and a sign flip**, from
`C_THR`-headroom=24.8% to **headroom=3313.7%**. I checked this is not a
computational error by sweeping nearby angles at both geometries (36°–40°
in 1° steps): the T21 fringe genuinely oscillates between roughly
±2×10⁻³–7×10⁻³ across that 4° span at both geometries (consistent with
the ~2.4°-period fringe this program's own T21 record already
characterizes), and θ₀=38° at A=724 happens to sit almost exactly on a
zero-crossing while at A=752 it sits near a local extremum. **This is a
real, physical phase effect, not noise** — and it is a dramatically
stronger illustration of PHOTONICS/EM's own phase-sensitivity concern
(Attack 1) than the tier-count evidence in Attack 3: a purely
n-convergence-scored prediction (P-NCONV27-6) can read CONFIRMED, cleanly,
at both geometries, while the actual physical quantity underneath it
swings by more than an order of magnitude and changes sign. VISION's own
back-of-envelope estimate (§ Attack 6, ~1.8% from the `1/√r` term alone)
badly undersells the size of this effect — the dominant driver is not the
amplitude term VISION cited, it is the fringe phase, exactly as
PHOTONICS/EM's concern (Attack 1) would predict for a cell this close to
a zero-crossing. Favorable for contamination-risk purposes at this
specific cell (headroom went up, by a lot) — but the mechanism, not the
direction, is what future citations need disclosed.

---

## Constraint check

No target constraint is violated or quietly dropped. §3's "T1 escape
route: NONE" is accurate — verified: no material law, no σ, no new
source, no engine change, this cycle re-evaluates an already-committed
desk propagator at different quadrature orders and a different (already-
committed, exp-048's own) geometry only. No constraint-3 or constraint-4
verdict is issued anywhere in the proposal text (grep-confirmed). The one
place a constraint-3-adjacent question could leak in through the back door
— P-NCONV27-6 touching a cell from exp-042's own contamination-risk
headline — is exactly Attack 6/VISION's concern, closed with a real number
above, not a verdict shift. `REALIZABILITY_MEMO.md` exposure: confirmed
zero (grepped for `beam_divergence`/`gaussian_angle_weights`, zero hits).
**Criterion 4 is NOT fired by this audit.**

---

## OVERALL RULING

# PROCEED-WITH-MANDATORY-FIXES

**Why this proceeds.** The proposal's own regression-anchor design is
sound and I confirmed it passes by building and running it myself before
any of the underlying code exists in the repo. The geometry arithmetic
(§2.1), the fringe-period table (§2.4), and the cost accounting (§6) all
check out exactly against independent recomputation. Every defect found
is a same-shift, zero-new-FDTD fix — a numeric operational definition
added to one falsification clause, two cells named explicitly in a
prediction's own text, one rounding digit corrected, one headroom number
reported. Nothing here is unfalsifiable in the structural sense once
Attack 4's fix is applied, and nothing is inexpressible — every quantity
is a `numpy` array computation over an already-committed propagator and
an already-committed geometry dict.

**Why it does not proceed unchanged.** P-NCONV27-2's hard-falsification
clause, as stated in the Phase-1 text, **will** misfire at Phase 4 — this
is confirmed, not hypothetical (Attack 3): (750nm, θ₀=40°, FWHM=20°,
`incoherent_corrected`) genuinely moves to a strictly larger tier, and the
clause's own literal wording would score that single, isolated,
mechanistically-explained event as refuting the proposal's entire
directional argument. This is exactly the "isolated aliasing artifact
misread as mechanism refutation" failure mode PHOTONICS and EM
independently warned about, now with a confirmed instance rather than a
generic worry. EM's own proposed repair needs Attack 4's operational
definition or it is not a fix at all, only a differently-worded
unfalsifiable clause — and that definition's scope must cover all three
functions at the two flagged coordinates (6 of 108 combinations), not
`coherent` alone, per Attack 3's own live result. P-NCONV27-3/7's central
estimates need Attack 2's truncation finding disclosed inline, not left
implicit in the fringe-period argument alone. P-NCONV27-6 needs both its
n-convergence stability AND VISION's headroom number attached — the
targeted run shows the latter can move by an order of magnitude and flip
sign even while the former reads a clean, unqualified CONFIRMED.

---

## MANDATORY-FIX DOCKET (adoptable at Phase 3)

1. **[Attacks 1+3+4, PHOTONICS+EM+Red Team, CONFIRMED NECESSARY by a live
   run, not just recommended]** Amend P-NCONV27-2's hard-falsification
   clause to: "any of the 102 cell-function combinations NOT pre-
   identified below moves to a strictly larger N_SERIES tier, **or** more
   than 1 of the 6 pre-identified combinations moves to a strictly larger
   tier." Pre-register, by name, all three functions at the two
   coordinates Attack 1's own computed table identifies as crossing the
   samples-per-period=1.0 boundary — (750nm, θ₀=38°) and (750nm, θ₀=40°),
   FWHM=20°, × {`incoherent`, `incoherent_corrected`, `coherent`}. Without
   this fix, P-NCONV27-2 as literally written scores FALSIFIED at Phase 4
   on the (750°,40°,`incoherent_corrected`) result this audit already
   measured (Attack 3) — not a risk, an already-observed fact.
2. **[Attack 2, QUANTUM+Red Team]** Add an explicit idealization/
   prediction-table disclosure to P-NCONV27-3/7: at GEOM78, the n=41
   grating-lobe replica computed at 750nm/θ₀∈{38°,40°}/FWHM=20° falls
   entirely outside the source aperture's own finite support (truncated
   to zero, not merely re-windowed), and at 750nm/θ₀=36° its amplitude
   drops from 1.0 to 0.66 — a mechanism the fringe-period argument (§2.4)
   does not and cannot predict the direction of. Central estimates for
   these 3 of 9 FWHM=20° coherent cells should be flagged as governed by
   a different, untested mechanism, not the period-growth story.
3. **[Attack 5, THERMO]** Correct §2.1 point 4's "A shrinks 3.73%" to
   "3.72%," matching the Y-domain figure two lines above (both are
   28/752 exactly). Cosmetic.
4. **[Attack 6, VISION+Red Team, number now in hand]** Add a
   P-NCONV27-6b (or an inline addendum) reporting the actual GEOM78
   converged value at the 750nm/38°/FWHM=2°/`incoherent_corrected` cell:
   `c`=+1.465×10⁻⁴ (vs. A=752's −4.007×10⁻³ — a ~27× magnitude collapse
   and a sign flip, headroom improving from 24.8% to 3313.7%), disclosed
   as a genuine fringe-phase effect (verified against a 1°-step angle
   sweep at both geometries, not a computational artifact), not merely as
   a pass/fail number. Escalation trigger unchanged: a new live thread,
   not a new FDTD run, if any *future* near-boundary citation needs the
   magnitude (not just the sign of headroom) to be geometry-stable.
5. **[Carried, not new]** THERMO's request (Phase-2 critique) to report
   the regression anchor's pass/fail per function, distinguishing
   `..._corrected`'s confirmation of already-precedented machinery
   (exp-048 Block B) from `incoherent`/`coherent`'s first-ever check of
   the obliquity-on-E convention's geometry-dict generalization — cheap,
   adds real information, no cost to add given Attack 7's own findings
   already separate the two below.

**No ask rejected.** Every one of the five blind seats' load-bearing
findings survives independent re-verification; PHOTONICS' and EM's
converge into a single sharper finding (Attack 3) neither seat itself
made; QUANTUM's is confirmed and strengthened (Attack 2); THERMODYNAMICS'
and VISION's are both confirmed as stated (Attacks 5, 6).

---

## Verification appendix — what I actually ran

- Read `PANEL.md` in full; `LOGBOOK.md` in full (RULED OUT R1–R4,
  ESTABLISHED, all LIVE THREADS, PARKED, and the full Iteration 26 entry).
- Read `experiments/050-.../phase1_proposal.md` and all five
  `phase2_critique_*.md` in full.
- Read `experiments/042-t21-magnitude-bridge/design_geometry.py`,
  `experiments/048-evidentiary-chord-closure/design_geometry.py`,
  `experiments/049-.../run.py`, `results.json`, and both of exp-049's own
  Red Team audits (`phase2_redteam_audit.md`, `phase5_redteam_audit.md`)
  in full, for house-style precedent.
- **Built, from the Phase-1 proposal's own §2.2 description (not from any
  code that exists in the repo), the geometry-parameterized
  `beam_divergence_incoherent`/`_incoherent_corrected`/`_coherent`
  functions** and ran the mandatory regression anchor: all 108 `c41`
  values at `GEOM_EXP042_OLD` match exp-049's committed `results.json` to
  0.0 relative error; spot-checked `c401`/`nstar` at 5 cells (including
  both of exp-049's own headline cells) — exact match on every field.
- Independently recomputed §2.1's full geometry table (`A`, `R_EDGE`,
  `GUARD_OUT`, Y-domain length for both geometries) directly from the two
  committed geometry dicts — exact match to the proposal's own numbers.
- Independently recomputed §2.4's full 9-row fringe-period table and the
  752/724=1.038674 ratio at every cell — exact match.
- Independently computed the samples-per-period table (Attack 1) and the
  grating-lobe replica-offset/taper-amplitude table (Attack 2) from
  scratch, using the exact `aperture_profile` raised-cosine formula
  already committed in both `design_geometry.py` modules — found the two
  independent diagnostics converge on the identical two coordinates
  (Attack 3). **Self-caught and corrected an indexing bug in my own first
  pass at the taper-amplitude formula** (distance-from-plateau used where
  distance-from-edge was needed) before it reached this document — the
  qualitative truncation finding was unaffected, the specific amplitude
  numbers were not, and the corrected table is what appears in Attack 2.
- **Ran all three `beam_divergence_*` functions at `g=GEOM78`, full
  `N_SERIES` doubling through n=5121, at all nine (θ₀,fn) combinations
  spanning 750nm/FWHM=20°/θ₀∈{36°,38°,40°}** — the two coordinates Attacks
  1/2 flagged plus one unflagged comparison point — using the same
  geometry-parameterized functions verified bit-exact in Attack 7. Found
  one real tier violation, (750nm,40°,`incoherent_corrected`): n\*=41→81
  (Attack 3's table).
- Ran VISION's own Attack-6 cell (750nm/38°/FWHM=2°/`incoherent_corrected`)
  through the same full doubling series at `g=GEOM78`: n\*=41 (unchanged),
  but the raw value collapses from −4.007×10⁻³ to +1.465×10⁻⁴ — confirmed
  as a genuine fringe-phase effect, not an artifact, via a 1°-step angle
  sweep (36°–40°) at both geometries showing the expected ~2.4°-period
  oscillation at both A values (Targeted computation section above).
- Grepped `REALIZABILITY_MEMO.md` for `beam_divergence`/
  `gaussian_angle_weights`: zero hits, confirming no memo tier is touched.
- Grepped `PLAN.md` for the cited Iteration-27 queue entry: confirmed
  present, verbatim, as cited.
- Confirmed `experiments/048-.../run.py`'s own regression gate
  (`edge_diffraction_c_empty_corrected` at `GEOM_EXP042_OLD`, ≤1e-9
  relative, 3λ) exists and passed, per THERMODYNAMICS' own citation.
- Recomputed the cost arithmetic (10,609×108=1,145,772×2=2,291,544;
  doubling exp-049's measured 2743.235s≈45m43s gives ≈91.4min) — exact
  match to §6.
- Ruled-out check: nothing in this proposal or this audit resurrects R1,
  R2, or R3 — no mechanism, no cloaking, no shell-thickness claim
  anywhere in `phase1_proposal.md` or the five critiques.
