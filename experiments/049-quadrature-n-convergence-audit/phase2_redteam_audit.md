# PHASE 2 — RED TEAM AUDIT · Panel Iteration 26 · exp-049

*Seventh seat, speaking last, with the Phase-1 proposal and all five blind
critiques. Standard: internal consistency, falsifiability, expressibility,
constraint violations — not textbook compliance. Every load-bearing claim
below was re-derived or re-run from source in this session, against the
unmodified `experiments/042-t21-magnitude-bridge/design_geometry.py` and
`experiments/046-.../run.py`/`results.json`. Where I checked a seat's number
I say so; where I sharpen or overturn a seat's framing I show the work.
Scripts used are summarized in the verification appendix.*

---

## 0. Headline

This is an instrument-fidelity cycle with no mechanism, no material, no T1
escape route — the five blind critiques agree it stays inside its own lane,
and I confirm that (§ Constraint check, below). All five load-bearing findings
handed to me check out against the actual code; two of them (MATERIALS',
QUANTUM's) I ran myself and found **understated, not overstated**. I also
found two defects none of the five blind seats caught, one of them squarely
in the item the proposal's own §4 calls "checked first" and gates every other
number in this audit on: **P-NCONV26-0's regression gate is not executable as
written** — it promises a 36-cell per-cell match against data
`experiments/046-.../results.json` never recorded at that granularity, and
half of it (the "corrected convention" coherent figure) requires a function
that exists only in `experiments/046-.../run.py`, not anywhere in this
proposal's own declared four-function scope. Separately, I ran QUANTUM's own
proposed fix formula and found it does not do what QUANTUM's prose says it
does — it still trips the exact hard-falsification clause it was written to
avoid.

**Ruling: PROCEED-WITH-MANDATORY-FIXES.** Nothing here is unfalsifiable,
inexpressible, or constraint-violating in a way that should stop the cycle —
every defect found is a same-day, zero-new-FDTD fix, most of them one-line
changes to formulas already in the proposal. But two defects (Attacks 5 and 7)
sit inside the machinery that gates trust in every other number this audit
will report, and must be fixed **before Phase 3 predictions are committed**,
not discovered after the run.

---

## ATTACK 1 — [inconsistency] MATERIALS' geometry-scope drift, affirmed

**Verified directly against code.** `experiments/048-evidentiary-chord-closure/
design_geometry.py:145-149`: `GEOM78 = dict(NY=1528, OBJ_Y=764, ABSORB=40, ...)`
⇒ `A = OBJ_Y - ABSORB = 724`, exactly as MATERIALS states, and exactly as
idealization 7 itself discloses (`A=724, NY=1528`). This is the geometry
exp-047/048's own near-boundary FALLBACK contamination check actually uses —
the one MATERIALS correctly identifies as "the geometry any future
near-boundary constraint-3 or realizability-adjacent citation would actually
use." MATERIALS' own framing is careful and correctly scoped: it does not
ask for a same-cycle re-run at A=724 (that would be scope creep the proposal
itself would be right to resist), only a **committed follow-up trigger** so
n\* results measured at A=752 are never silently cited as governing the
A=724 fallback geometry — the exact citation-scope failure this program
already paid six iterations to catch once for T21 itself (exp-042→exp-048).

**Affirmed as mandatory.** Cheap (one sentence + one LOGBOOK/PLAN.md queue
entry), does not touch this cycle's own arithmetic, and closes a real
citation-scope gap before it can recur.

---

## ATTACK 2 — [inconsistency] EM's grating-lobe/pooled-correlation masking — affirmed, and DEMONSTRATED, not just argued

EM's attack is that P-NCONV26-2's Spearman correlation is not stated as
scored per-function, so a strong incoherent fit could mask a weak coherent
one. **I did not take this on faith — I computed all three correlations from
the unmodified code**, using `Δrel(41)` = `Δrel(41→81)` from
`beam_divergence_incoherent` / `_corrected` / `_coherent` at the 9 FWHM=20°
cells, ranked against §2.1's own predicted difficulty order:

| function | Spearman ρ vs. predicted order | outcome under P-NCONV26-2's own bands |
|---|---|---|
| `incoherent` | **0.717** (p=0.030) | CONFIRMS (≥0.70) |
| `incoherent_corrected` | **0.600** (p=0.088) | neither confirms nor falsifies |
| `coherent` (the physically real grating-lobe mechanism this audit exists to characterize) | **0.450** (p=0.224) | neither confirms nor falsifies |
| naive pooled-by-raw-magnitude (27 points, predicted rank repeated ×3 — the reading an unspecified "measured Δrel(41) magnitudes" instruction most naturally invites) | **−0.343** | **hard-falsifies** (negative sign) |

This is not a hypothetical risk, it is a measured fact about the unmodified
functions: **the one function whose difficulty ordering P-NCONV26-2 exists to
test (`coherent`) does not clear its own ≥0.70 confirm bar**, while the two
noise-dominated incoherent readings sit closer to (or, for `incoherent`,
above) it — and the most natural literal reading of "the measured Δrel(41)
magnitudes" as one pooled statistic **inverts the sign entirely** and would
trip the hard-falsification clause outright. §5 idealization 4's claim that
the two mechanisms are "predicted to track FWHM/λ/θ₀ similarly" is
**demonstrably false as stated** — 0.717 and 0.450 are not "tracking
similarly," they straddle the confirm/no-decision boundary from opposite
sides.

**Affirmed as mandatory, and elevated above EM's own framing**: this is not
"could mask," it already does, on the unmodified code, at Phase 2. Adopt EM's
flip in full (three separate ≥0.70 bars, one per function) **and** add an
explicit operational definition of how the correlation is computed (per
EM's own text this is implied but never spelled out) — the −0.343 result
above shows the current wording is ambiguous enough to produce opposite
verdicts depending on an unstated implementation choice.

---

## ATTACK 3 — [cosmetic, non-load-bearing] THERMO's arithmetic slip — affirmed exactly

Recomputed: `0.005 / 0.004006497410421138 = 1.247972852046454`, headroom
`= 24.7973%` — THERMO's correction is exact to the last printed digit; the
proposal's `1.2483×`/`24.83%` is off by ~0.03pp. Non-load-bearing (P-NCONV26-5's
bands are 1%/5%, nowhere near this precision) but it is the exact species R4
was adopted to catch, one cycle after adoption, in the document most likely
to repeat it (THERMO's own framing, confirmed). **Affirmed, cosmetic fix
only — does not gate Phase 3.**

---

## ATTACK 4 — [program-integrity/methodology] THERMO's scope/delivery risk — affirmed and SHARPENED with a real measurement

THERMO flagged the cost estimate as "not yet profiled" and asked for a
machine-countable completeness ledger (972 expected records) plus profiled
wall-clock before any n\* claim is trusted. **I profiled it.** Benchmarking a
representative one-cell, three-function sweep across the full `N_SERIES`
(24 calls, all three `beam_divergence_*` functions × 8 doubling orders) took
**76.9s** on this box. Extrapolated linearly to the proposal's own accounting
(972 (cell, function, n) evaluations, same n-mix as the benchmark):
**≈3113s ≈ 52 minutes single-threaded** — **2.6×–3× above the proposal's own
stated ceiling of "~20 minutes."** This is before Attack 7's finding that a
fourth function (`beam_divergence_coherent_corrected`) is silently required
to satisfy the regression gate, which would add another ~25% to both the
evaluation count and the wall-clock.

**Affirmed as mandatory, strengthened from a risk to a measured fact**: the
cost estimate is not merely unprofiled, it is already demonstrably wrong by
a factor of ~3, before the run has even happened, at exactly the scale
(1.1M+ evaluations, no completeness instrumentation) where this program's
own fix-docket-delivery pattern (named 9+ times, three straight cycles
23–24–25) would be hardest to catch by inspection. THERMO's mandatory fix
(per-(cell,function,N_SERIES-entry) completeness ledger + profiled wall-clock,
committed alongside `results.json`) is adopted as stated, with the expected
record count revised upward to account for Attack 7's fourth function.

---

## ATTACK 5 — [constraint-integrity / metric-artifact] QUANTUM's ill-conditioned Δrel — affirmed, WORSENED, and QUANTUM's OWN proposed fix shown not to work

**Reproduced exactly, on unmodified code.** Computing `Δrel(41→81)` for all 9
FWHM=20° `beam_divergence_incoherent` cells:

```
450/36  drel=6680.19%   |C(81)|=5.24e-06
450/38  drel=9022.02%   |C(81)|=8.73e-06
450/40  drel= 152.25%   |C(81)|=5.73e-04
600/36  drel=  75.35%   |C(81)|=2.05e-04
600/38  drel= 661.41%   |C(81)|=6.00e-05
600/40  drel=  41.28%   |C(81)|=4.12e-04
750/36  drel=  54.02%   |C(81)|=3.07e-04
750/38  drel= 337.48%   |C(81)|=1.72e-04
750/40  drel=  14.51%   |C(81)|=3.03e-04
```

This matches QUANTUM's cited range (14.5%–9022%) exactly, and the |C| scale
(5e-6 to 8e-4) is if anything *more* extreme than QUANTUM's own "5e-5–8e-4"
citation. Running the full two-consecutive-pass test across the whole
`N_SERIES`: **9/9** of these cells read `n*>41` (none already converged),
against P-NCONV26-1b's own hard-falsification clause ("`>6/9` fail for
either incoherent function"). **This fires, exactly as QUANTUM predicts.**

**Worse than QUANTUM scoped it.** I extended the same check to the full
36-cell × 3-function grid, not just the 9 flagged cells, and found the
artifact is not confined to FWHM=20°: **4 additional cell-function
combinations at FWHM=10°** (`incoherent`/`incoherent_corrected` × 450nm ×
{36°,38°}) show the identical signature (|C|≈1–5×10⁻⁴, `Δrel`=70.7%–202.9%).
This directly contaminates **P-NCONV26-1c** (FWHM≤10° convergence-rate
prediction, ≥70% pooled bar) and **P-NCONV26-3** (which is explicitly
looking for FWHM=10° cells with intermediate `Δrel>1%` blowups as evidence
of *real*, non-monotonic Nyquist-margin aliasing) — a bookkeeping artifact
at exactly the same magnitude as the phenomenon P-NCONV26-3 is designed to
detect will be indistinguishable from it under the current criterion. **This
is the "worse compound failure" the task asked me to check for, and it is
real**: the ill-conditioning is not a FWHM=20°-only problem confined to
P-NCONV26-1b/2, it reaches into P-NCONV26-1c and P-NCONV26-3 as well.

**QUANTUM's own proposed fix does not solve this — I implemented and ran it.**
QUANTUM's formula, `Δrel(n) = 100·|C(2n)−C(n)| / max(|C(2n)|, C_THR)`: when
`|C(2n)| < C_THR`, the REL_TOL≤1% clause becomes `|C(2n)−C(n)| ≤
0.01×C_THR = 5×10⁻⁵` — **an order of magnitude *stricter* than ABS_TOL=5×10⁻⁴**,
the opposite of what QUANTUM's own prose says the fix should do ("below that,
Δabs≤5e-4 alone... is the physically meaningful bar"). Run against the same
9 FWHM=20° `incoherent` cells: **still 8/9 read `n*>41`** — the floor formula
barely moves the count (9/9→8/9) and **still trips the same `>6/9`
hard-falsification clause it exists to prevent.** The formula that actually
matches QUANTUM's stated intent — *exempt* the relative-error clause entirely
once `|C(2n)| < C_THR` and require only `Δabs≤ABS_TOL` — brings the count down
to **3/9**, matching the proposal's own central estimate (1–3/9) and clearing
the ≤4/9 confirm band.

**Ruling on this attack.** QUANTUM's diagnosis is correct and, on inspection,
understated (it reaches FWHM=10° too). QUANTUM's own remediation formula is
**wrong as written** and would not fix the problem it targets. **Mandatory
fix, corrected**: `Δrel(n) = 100·|C(2n)−C(n)|/|C(2n)|` **if** `|C(2n)|≥C_THR`,
**else the step is judged on `Δabs≤ABS_TOL` alone** (an exemption, not a
floored ratio) — apply this uniformly across the **full 36-cell×3-function
grid**, not only the 9 FWHM=20° cells, given the FWHM=10° contamination found
above. Re-score P-NCONV26-1b, 1c, 2, and 3 under the corrected criterion
before Phase 3 commits any of their bands.

---

## ATTACK 6 — [R4-adjacent disclosure gap] VISION's T24-cell caveat — affirmed; independently confirmed non-load-bearing to the actual outcome

**T24's figure verified directly against LOGBOOK.md** (Iteration 23 close /
live-thread table): `ABSORB 40→60` moved `C_empty` by **+0.0070** at
**750nm/38°/FWHM=2°** — the identical (λ,θ,FWHM) triple as P-NCONV26-5's
"sharpest stakes test" cell. VISION is right that this is a real, FDTD-
measured, comparable-magnitude, unaddressed systematic sitting on the exact
cell this prediction calls its own sharpest falsifier, and that idealization
5's disclaimer is not attached at the point of the claim.

**I also ran the actual n-sweep at that cell**, to check whether this caveat
has any chance of mattering to this cycle's own output: `beam_divergence_
incoherent_corrected(38, 2, 25, n=...)` across the full doubling series
(41→5121) moves from `−0.0040064974104211...` to `−0.0040064974415700...` —
a relative change of **≈7.7×10⁻⁹%**, nine orders of magnitude inside
P-NCONV26-5's own 1% confirm band. **This cell is essentially perfectly
converged already at n=41**; there is no scenario in which this audit's own
convergence finding is ambiguous or close to the T24 systematic's size. VISION's
fix is therefore correctly scoped as a **labeling** requirement, not a
substantive one — the caveat matters for how a future reader interprets
"does NOT flip" against a real, separate FDTD systematic, not for whether
this cycle's own arithmetic is trustworthy. **Affirmed as mandatory, cheap,
disclosure-only — attach VISION's proposed sentence to P-NCONV26-5's own
prediction text, not only idealization 5.**

---

## ATTACK 7 — [inconsistency] P-NCONV26-0's regression gate is not executable as written — new, not caught by any of the five blind seats, MANDATORY

All five blind critiques verified the *cited numbers* (4.472688822027389%,
3.1838964320070553%) reproduce exactly against `experiments/046-.../
results.json` — true, and I reconfirm it. **None of the five checked whether
the gate's *stated pass criterion* is even checkable against what that file
actually contains, or whether the functions needed to check it are in this
proposal's own declared scope. Neither holds.**

**7a. The "36/36 cells" claim references data that was never recorded at
that granularity.** I read `experiments/046-.../results.json`'s
`block_a_aperture_consistent_beam.angular_sampling_convergence` block in
full:

```json
{"statement": "...", "worst_cell_committed_convention": {...},
 "worst_rel_move_committed_convention_pct": 4.472688822027389,
 "worst_rel_move_corrected_convention_pct": 3.1838964320070553,
 "n_cells_above_1pct_committed": 2,
 "n_cells_above_0p16pct_committed": 3}
```

That is **the entire record**: one worst-cell figure per convention, plus
two integer threshold-counts. There is no per-cell table of all 36 `Δrel(41→
401)` values anywhere in `experiments/046-.../results.json` to check "≤0.1%
relative deviation... at 36/36 cells" against. P-NCONV26-0's stated pass
criterion cannot be executed as literally written — the comparison target
does not exist at that resolution. The genuinely checkable claims (matching
the two worst-cell figures and the two integer counts, which I independently
reproduced against unmodified code, see appendix) are a **strictly weaker**
regression test than "36/36 cells, ≤0.1% each," and the proposal should say
so rather than promising a check it cannot perform.

**7b. The "corrected convention" figure requires a function outside this
proposal's own declared scope.** Tracing `experiments/046-.../run.py:422-450`
(`angular_sampling_convergence`): the "committed" reading reimplements
`_G_for(lam,True)` inline (equivalent to `beam_divergence_coherent`'s own
logic, source `experiments/042-.../design_geometry.py`) — fine, in scope.
But the "corrected" reading calls `beam_divergence_coherent_corrected`
(`experiments/046-.../run.py:318-333`) — **a function that exists only in
exp-046's own `run.py`. It is not in `experiments/042-t21-magnitude-bridge/
design_geometry.py`, is not among the four functions §2.0's table lists as
"inherited VERBATIM, not rebuilt," and is not among the three functions
{`incoherent`, `incoherent_corrected`, `coherent`} §1 and §2.2 explicitly
define this audit's own scope over.** To reproduce the "corrected
convention" half of P-NCONV26-0's own committed band, this audit must
silently import or reimplement code from `experiments/046-.../run.py` that
it nowhere discloses as a dependency — directly contradicting §2.0's own
framing ("This audit imports `design_geometry`... exactly as exp-046 did" —
exp-046 *also* defined additional local functions beyond `design_geometry`,
and this proposal claims only the former).

**Why this is load-bearing, not cosmetic.** P-NCONV26-0 is explicitly "the
regression gate, checked first," and its own hard-falsification clause says
"no new number in this audit is trusted until the discrepancy is resolved."
A gate that cannot be executed as specified is worse than a gate that fails —
it will force an undisclosed implementation choice at Phase 4, silently,
in the one place this cycle has committed to zero ambiguity. **Mandatory
fix, before Phase 3 commits**: either (i) add `beam_divergence_coherent_
corrected`, sourced verbatim from `experiments/046-.../run.py:318-333`, to
§2.0's function table and the doubling-series scope (revising the
evaluation-count/cost estimate in Attack 4 upward accordingly), or (ii) drop
the "corrected convention" half of P-NCONV26-0 and restate the gate against
only what `results.json` actually contains: the two worst-cell figures and
the two integer counts, explicitly labeled as a weaker check than a full
36-cell table.

---

## ATTACK 8 — [minor, unfalsifiable sub-clause] P-NCONV26-4's "n\*∈{641,1281}" aside has no attached falsifier, and is measured wrong

Running the full two-consecutive-pass test on the actual hardest cell
(`beam_divergence_coherent`, 450nm/36°/FWHM=20°, the cell P-NCONV26-4 names
"specifically"): `41→81` fails (Δrel=4.47%, matching exp-046's own 4.4727%
figure almost exactly), but `81→161` and `161→321` both pass cleanly
(Δrel=0.0019%, 0.0011%) — **the measured n\* at this cell is 81**, not
`{641, 1281}` as P-NCONV26-4's own text predicts, a factor of 8–16× off. This
sub-claim sits inside P-NCONV26-4's committed-band text but is **not covered
by P-NCONV26-4's own stated hard-falsification condition** (which is only
about the aggregate `>25/108` count or a `NOT CONVERGED WITHIN RANGE`
outcome) — so it can be measured wrong, as it is, without moving the
prediction's CONFIRMED/REFUTED status. This reveals a real gap between §2.1's
physical "10 samples/period" ceiling-derivation heuristic (which motivated
extending `N_SERIES` all the way to 5121) and what §2.2's actual operational
convergence test reports (which converges far faster, because a
window-averaged Weber contrast smooths fringe ripple that a raw point value
would not). **Not mandatory** — it doesn't threaten any pass/fail outcome —
but the specific numeric aside should either get its own falsifier or be
demoted to descriptive-only language, and §2.1's ceiling-derivation heuristic
should be labeled as motivating *why the series goes as high as 5121*, not
as a predictor of where any specific cell's own n\* will land.

---

## Checked and cleared — items the Director's brief specifically asked me to re-examine

**"n=41→2n=81" doubling-series construction.** `N_SERIES` uses `2·(previous)
−1`, not literal doubling — verified this is a deliberate, sound
construction (it exactly halves the sample spacing `Δθ_sample=5·fwhm/(n−1)`
at each step, since `2n−1−1=2(n−1)`, and keeps every sample set centered
symmetrically on θ₀ per `linspace`'s endpoint-inclusive convention). §2.1
discloses this formula explicitly. **No defect.**

**n=401 excluded from the doubling series but present in the regression
gate.** Checked for inconsistency: none found. n=401 is used only as a fixed
threshold value compared against n\* (itself always an `N_SERIES` member),
which is a perfectly well-defined comparison (`n\*≤401` means `n\*∈{41,81,
161,321}`), and idealization 8 discloses the n=401 role correctly. The
regression-gate defect is Attack 7, which is about a different problem
(missing comparison data and an out-of-scope function), not about n=401's
dual role.

**"Two-consecutive-doublings + ill-conditioned Δrel ⇒ worse compound
failure?"** Yes — covered in full under Attack 5 (FWHM=10° contamination of
P-NCONV26-1c/3, not just P-NCONV26-1b/2 as QUANTUM scoped it).

**Idealization 4's "predicted to track similarly" claim vs. EM's attack.**
Checked and found **false as stated** — covered under Attack 2
(ρ=0.717 vs. 0.450, not "similar").

**Constraint-3/4 verdict, checked end-to-end, given P-NCONV26-5/6 touch a
cell exp-042 used in its own contamination-risk headline.** §3's "T1 escape
route: NONE" and "no constraint-3/4 verdict" claims are correct as far as
this cycle's own text goes — I grepped for constraint-3/4 language beyond
the two explicit disclaimers and found none. The substantive question is
whether the *result* could functionally reopen exp-042's own "0/36 cells
exceed C_THR" contamination-risk finding without the write-up treating that
as the constraint-3-adjacent event it would be. I ran the actual convergence
check at P-NCONV26-5's cell (Attack 6, above) and found it moves by
~7.7×10⁻⁹% across the whole doubling range — there is no live scenario in
which this cycle's own numbers reopen that finding. P-NCONV26-6 (the
"35/36 above 20×-incoherent" sub-clause) touches cells with `min|C|=0.03227`,
far outside the near-zero-crossing regime Attack 5 identifies — I spot-checked
several of those cells directly and confirmed none show the ill-conditioning
signature. **No constraint-3/4 violation, quiet or otherwise. VISION's
inline-caveat fix (Attack 6) is the correct and sufficient remedy — no
further escalation warranted.**

**REALIZABILITY_MEMO.md exposure.** Independently re-checked MATERIALS' own
verification (§3's claim that no memo tier is at stake): confirmed correct —
`gaussian_angle_weights`/`beam_divergence_*` feed only the T21
contamination-risk channel, never the σ(I) D_req tables or Entry 2's
`C=−0.7209` anchor (which is computed via `edge_diffraction_c_empty[_
corrected]` at a single fixed θ, a different code path entirely).

---

## Constraint check

No target constraint is violated or quietly dropped. §3's "T1 escape route:
NONE" is accurate (verified: no material law, no σ, no new source, no engine
change — this cycle re-evaluates an already-committed desk propagator at
different quadrature orders only). No constraint-3 or constraint-4 verdict is
issued anywhere in the proposal text (grep-confirmed), and the one place a
constraint-3-adjacent question could leak in through the back door
(P-NCONV26-5/6 touching exp-042's own contamination-risk headline cells) was
checked directly above and found clean. **Criterion 4 is NOT fired by this
audit.**

---

## OVERALL RULING

# PROCEED-WITH-MANDATORY-FIXES

**Why this proceeds.** Every defect found — including the two (Attacks 5 and
7) rated most serious — is a same-day, zero-new-FDTD fix: a corrected
tolerance formula already close to what QUANTUM proposed, a function added to
a table (or a gate re-scoped to what its own source data actually supports),
a Spearman correlation split three ways instead of pooled one way, one
sentence attached inline instead of buried in an idealization. This is
exactly the shape of cycle this program's own precedent (exp-046, T21's own
propagator-vs-envelope dispute) resolves with a mandatory-fix docket, not a
rejection. Nothing here is unfalsifiable in the structural sense Red Team
exists to strike (P-NCONV26-4's aside, Attack 8, is a narrow exception —
descriptive, not gating, and non-mandatory) and nothing is inexpressible —
every quantity is a `numpy` array computation over an already-committed
propagator.

**Why it does not proceed unchanged.** Two defects sit inside machinery this
cycle's own text says gates trust in everything else: P-NCONV26-0's
regression gate cannot be executed as written (Attack 7), and the criterion
meant to keep quadrature noise from being read as physics is broken in a way
that would already trip its own hard-falsification clauses on unmodified
code (Attack 5) — and QUANTUM's own proposed repair does not fix it (verified
by running it). Both must be resolved and re-verified **before** Phase 3
commits P-NCONV26-0/1b/1c/2/3's bands to git, not discovered at Phase 4 or
Phase 5.

---

## MANDATORY-FIX DOCKET (adoptable at Phase 3)

1. **[Attack 5, QUANTUM + Red Team]** Correct the Δrel formula to an
   **exemption**, not a floor: `Δrel(n) = 100·|C(2n)−C(n)|/|C(2n)|` when
   `|C(2n)|≥C_THR`; when `|C(2n)|<C_THR`, judge the step on `Δabs≤ABS_TOL`
   alone (no relative-error clause). QUANTUM's own `max(|C|,C_THR)` floor
   formula is verified NOT to work (still 8/9, not 1–3/9) and must not be
   adopted as written. Apply across the **full 36×3 grid**, not only the 9
   FWHM=20° cells — 4 FWHM=10° combinations show the identical artifact.
   Re-score P-NCONV26-1b, 1c, 2, and 3 under the corrected criterion.
2. **[Attack 7, Red Team, new]** Fix P-NCONV26-0 before it is trusted as
   "checked first": either add `beam_divergence_coherent_corrected`
   (sourced verbatim, `experiments/046-.../run.py:318-333`) to §2.0's
   function table and cost accounting, or restate the gate's pass criterion
   against what `experiments/046-.../results.json` actually contains (two
   worst-cell figures + two integer counts), not a fictional 36-cell table.
3. **[Attack 2, EM + Red Team, demonstrated]** Score P-NCONV26-2 as three
   separate per-function Spearman correlations (each its own ≥0.70 bar), and
   state the exact aggregation formula in the committed prediction text — the
   current wording's most natural pooled reading produces a
   hard-falsifying **negative** correlation (−0.343) on unmodified code, the
   opposite of what a correct per-function scoring shows for two of the
   three functions. Correct idealization 4's "track similarly" claim to
   report the measured 0.717 vs. 0.450 split rather than asserting similarity
   pre-run.
4. **[Attack 4, THERMO + Red Team, measured]** Emit the per-(cell, function,
   N_SERIES-entry) completeness ledger and profiled wall-clock THERMO
   requires, revised to the corrected combination count from fix 2. Budget
   wall-clock from the **measured** ≈52-minute single-threaded figure (not
   the proposal's own ~20-minute ceiling, now shown wrong by ~3×), plus the
   ~25% fix 2 may add.
5. **[Attack 1, MATERIALS]** Add a committed follow-up trigger (PLAN.md/
   LOGBOOK queue entry) to re-run this identical sweep at exp-048's A=724/
   NY=1528 geometry before any near-boundary constraint-3 or realizability
   citation is allowed to lean on an A=752-measured n\*.
6. **[Attack 6, VISION]** Attach VISION's inline caveat sentence to
   P-NCONV26-5's own prediction text (not only idealization 5): "FDTD-
   unvalidated at this cell; T24's ~0.0070 ABSORB systematic at this same
   (λ,θ,FWHM) point is untested here." Independently confirmed non-load-
   bearing to this cycle's own arithmetic (the cell is converged to
   ~7.7×10⁻⁹% already) — a disclosure fix, not a substantive one.
7. **[Attack 3, THERMO]** Correct P-NCONV26-5's margin figure to
   `1.247972852046454×` / `24.7973%`. Cosmetic; does not gate Phase 3.
8. **[Attack 8, Red Team, non-mandatory]** Either attach a falsifier to
   P-NCONV26-4's "n\*∈{641,1281} at the hardest cell specifically" aside or
   demote it to descriptive-only language; it is measured wrong (actual
   n\*=81) but currently cannot fail because nothing in P-NCONV26-4's hard-
   falsification clause covers it.

**No ask rejected.** Every one of the five blind seats' load-bearing findings
survives independent re-verification; none is downgraded to non-load-bearing
except THERMO's own arithmetic slip (Attack 3), which THERMO itself already
scoped as cosmetic.

---

## Verification appendix — what I actually ran

- Direct execution of `experiments/042-t21-magnitude-bridge/design_geometry.py`'s
  `gaussian_angle_weights`, `beam_divergence_incoherent`,
  `beam_divergence_incoherent_corrected`, `beam_divergence_coherent`, unmodified,
  at every `N_SERIES` order (41…5121) plus n=401, across the full 36-cell grid
  and, for the ill-conditioning check, all 108 cell-function combinations.
- Reproduced QUANTUM's cited Δrel(41→81) range (14.5%–9022%) and |C| scale
  exactly; extended the same check to the full grid and found 4 additional
  FWHM=10° combinations with the same signature.
- Implemented and ran both QUANTUM's proposed `max(|C|,C_THR)` floor formula
  (result: 8/9, does not fix the problem) and the exemption-based correction
  (result: 3/9, matches the proposal's own central estimate).
- Computed all three functions' Spearman correlations against §2.1's
  predicted difficulty order at the 9 FWHM=20° cells (per-function: 0.717 /
  0.600 / 0.450; naive pooled: −0.343), using `scipy.stats.spearmanr`.
- Read `experiments/046-.../results.json`'s
  `block_a_aperture_consistent_beam.angular_sampling_convergence` block in
  full and confirmed it contains no per-cell 36-row table.
- Traced `experiments/046-.../run.py:318-333,422-450` directly and confirmed
  `beam_divergence_coherent_corrected` is defined only there, not in
  `experiments/042-.../design_geometry.py`.
- Read `experiments/048-evidentiary-chord-closure/design_geometry.py:145-158`
  directly and confirmed `GEOM78`'s `A=724`, `NY=1528` against idealization 7's
  own citation.
- Benchmarked a representative 24-call sweep (1 cell × 3 functions × 8
  `N_SERIES` orders) at 76.9s wall-clock; extrapolated linearly to the
  proposal's own 972-evaluation accounting (≈52 minutes).
- Ran the full two-consecutive-pass convergence test at P-NCONV26-5's cited
  cell (750nm/38°/FWHM=2°, `incoherent_corrected`) across the whole doubling
  series: relative movement ≈7.7×10⁻⁹% end to end.
- Ran the full two-consecutive-pass test at P-NCONV26-4's named hardest cell
  (450nm/36°/FWHM=20°, `coherent`): measured n\*=81, not the predicted
  `{641,1281}`.
- Grepped `LOGBOOK.md` for the T24 `+0.0070` figure and confirmed it names
  the identical (λ,θ,FWHM) cell as P-NCONV26-5.
- Read `PANEL.md` in full and `LOGBOOK.md` in full (Iterations 1–25, with
  close attention to the T21/T24 threads, the fix-docket-delivery pattern's
  nine named recurrences, and Iterations 19/23/25's own precedent for how
  this program resolves propagator/convention disputes).
- Ruled-out check: nothing in this docket resurrects R1, R2, or R3 — this
  cycle proposes no mechanism, no cloaking, no shell-thickness law.
