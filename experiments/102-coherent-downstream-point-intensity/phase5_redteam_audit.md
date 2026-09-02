# Phase 5 — RED TEAM Final Audit, Panel Iteration 79 (exp-102)

Fresh sub-agent, RED TEAM seat. Read PANEL.md in full; LOGBOOK.md's RULED
OUT registry R1–R21 (in full, verbatim text — not a summary), ESTABLISHED,
and the Iteration 76–78 R20/R21 narrative (exp-099's R20 founding,
exp-100's R21 founding, exp-101's R20 first-ever firing); the complete
exp-102 record (`phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `NOTES.md` in full, `run.py`, `run_output.txt`,
`results.json`); and all six `phase5_review_*.md` files. Every numeric
claim below is independently recomputed from `results.json` directly by me
(Python, this session) or independently re-derived from source/first
principles — nothing is taken on any reviewer's word, including my own
prior reads of other documents.

---

## 1. Independent primitive re-verification (before adjudicating anyone)

I loaded `results.json` myself and recomputed, cell-by-cell, from
`primary_rows` (12 entries) and `gates`:

- **κ_region(θ) true range**: sorted all 12 `kappa_region` values myself.
  `min = 3.479968×10⁻³` (`C40_R4@41.460901`), `max = 7.289772×10⁻³`
  (`C40_R4@42.960901`). **`NOTES.md`'s Result states "3.68×10⁻³–7.29×10⁻³".
  The floor is wrong.** `3.68×10⁻³` (`0.0036815...`) is real data
  (`C40_R4@38.59023`) but is the **second-smallest** of 12, not the
  minimum. The ceiling is correct. This exactly matches all six Phase-5
  reviews' independent findings (PHOTONICS, MATERIALS, EM, THERMODYNAMICS,
  QUANTUM, VISION) — six independent recomputations, mine now a seventh,
  all converging on the identical true minimum. **One fact, seven
  confirmations.**
- **κ_off_region range**: recomputed min/max myself — `1.0405807`–
  `1.0766458`, matching "1.041–1.077" exactly.
- **Gate C**: recomputed `|i0_corrected·u_x − i_inc|/i0_corrected` for all
  12 cells from raw `i0_corrected`/`u_x`/`i_inc` fields — max
  `0.0091979...` (0.92%), matching exactly. Original-erroneous bare-`cosθ`
  comparator: recomputed max `1.597792...` (159.78%), matching exactly.
- **Gate D**: recomputed `rel_dev_region` from raw perturbed/correct
  `kappa_region` pairs — 48.9511% (C40_R4), 8.2417% (G40_R4), matching
  exactly.
- **Gate B**: `kappa_region(θ=0°)=1.6268958...×10⁻³`, `P=[352,280]`;
  established window `x∈[357,457)` ⇒ `P.x=352` sits before the window.
  Confirmed exactly.
- **Point-vs-region ratios**: recomputed all 12 — range `1.2301`–`1.5591`,
  matching exactly.
- **Predictions/verdicts**: re-read `results.json['predictions']` directly
  — `p1`/`p2`/`p3`/`p4` all `"verdict": "CONFIRMED"`, `n_violations: 0`
  throughout; `run_output.txt`'s own printed Prediction-5 line reads
  `VERDICT=CONFIRMED`. All five predictions are CONFIRMED as filed
  (Prediction 2 confirmed on the corrected formula, disclosed).
- **`lab/` diff, independently checked via git, not taken on NOTES.md's
  word**: `git log --oneline -- lab/` shows the most recent commit
  touching `lab/` is Iteration 76 (`d9f1006`, exp-099) — no commit since
  then touches `lab/`, and `git status --short lab/` is clean. **The
  "zero `lab/` diff" claim is independently confirmed from the actual git
  record, not merely disclosed prose.**
- **The Gate C sign correction — my own third-from-scratch, sixth-overall
  independent re-derivation.** From `add_line_source`'s own docstring
  (`lab/fdtd2d.py`, read directly): "The −x-going wave then travels along
  (−cosθ, +sinθ)" — this is the applicable convention for the R4 family
  (`src_x > obj_x`, asserted at runtime by `downstream_sign()`). For a
  locally plane wave the time-averaged Poynting vector is parallel to the
  propagation direction, `⟨S⟩ = I₀·u(θ)`, `I₀=|⟨S⟩|≥0` by definition. So
  `Sx = I₀·u_x(θ) = I₀·(−cosθ)`, **not** `+I₀·cosθ`. `i_inc` is confirmed
  directly from `lab/sections.py` to be `mean_y(Sx)` — a signed quantity —
  so `i_inc ≈ I0_corrected·(−cosθ)` is the correct identity; the frozen
  Phase-3 formula's bare `+cosθ` was wrong by a sign. This derivation uses
  only (a) the source docstring and (b) the textbook plane-wave Poynting
  identity — it does not depend on NOTES.md's own Resolution Note, EM's
  Phase-5 derivation, QUANTUM's Phase-5 Maxwell's-equations derivation, or
  PHOTONICS' `2cosθ`-shape check. **Independently confirmed correct: this
  is now the sixth independent derivation (NOTES.md's own Resolution Note
  2; EM's Phase-2 critique establishing `u(θ)` for an unrelated purpose;
  PHOTONICS' Phase-5 `2cosθ`-shape cross-check; EM's Phase-5 from-scratch
  Poynting-vector re-derivation; QUANTUM's Phase-5 Maxwell's-equations
  re-derivation; mine, here) — the most heavily cross-verified single
  formula correction in this program's history.** All six independent
  checks agree on both the sign and the quantitative `2cosθ`-shaped
  magnitude of the original error (145.4%–159.8%, matching `2cosθ` at the
  six R4 angles to the plane-wave-approximation residual). This is R4's
  own addendum discipline ("never adopt a sign correction merely because
  it makes two numbers agree — re-derive it independently by an external
  method") executed about as thoroughly as this program has ever executed
  it.

---

## 2. Defect count and ruling: how many DISTINCT R4-class defects survive
## Phase-3-freeze into Result/Learned, caught only at Phase 5?

**Ruling: ONE.**

**Instance 1 — the κ_region(θ) range floor.** All six Phase-5 seats
independently recomputed the same true minimum (`3.48×10⁻³`) against the
same stated, incorrect floor (`3.68×10⁻³`) in Result. This is a single
fact (one number, in one sentence, in one section, wrong in one specific
way), independently corroborated by six different reviewers using
materially the same method (sort the 12-cell array, compare to the stated
range). Per this program's own direct precedent — exp-101's Red Team
audit ruling that VISION's and EM's independent findings of the
`observer_article_norm` range error were "the SAME single defect, ruled to
count ONCE, not twice, since it is one fact corroborated by two
independent methods, not two independently-arising defects" — six-way
corroboration of the identical fact counts once here for exactly the same
reason, only more so. **Count: 1.**

VISION additionally traced this instance's *propagation*: Learned item
1's rounded headline (`κ~0.4–0.7%`) inherits the same wrong floor
(`0.348%` rounds to `~0.3%`, not `~0.4%`), and VISION's own text rules
this "one root cause manifesting in two places, not two independent
errors." I independently re-checked this and concur: Learned #1's number
was not separately, independently miscomputed — it is a straight
propagation of Result's own (wrong) floor under the same one-decimal
rounding convention already used for the ceiling. **This does not add a
second count.**

**Candidate instance 2 — MATERIALS' finding: Learned #1 restates the
headline figure with no realizability caveat, though fix 7 required the
caveat "beside Prediction 1's κ(θ) confirmation text" and Result complies
literally.** I independently re-verified this by direct quote (§1 of
MATERIALS' review, cross-checked against `NOTES.md`'s own Result and
Learned sections, both read in full above): Result's κ(θ) sentence is
immediately followed by the fix-7 caveat, in bold, inline. Learned item
1's restatement of the same headline carries no caveat at all. This is a
**real, genuine, distinct textual gap** — but it is a different failure
*shape* than R20's own definitional text ("a claimed-exact figure,
citation, label, or coincidence that does not reproduce from its own
cited source"). MATERIALS' complaint is not that Learned #1's figure
fails to reproduce from `results.json` on its own numeric merits in a way
independent of Instance 1 — it is that a *required qualifying caveat*
did not travel to a second citation of the same figure. That is
structurally the R1/Iteration-14-lineage failure shape (a caveat that
must travel with a figure wherever it is restated) and the R21-lineage
failure shape (a finding persisted/stated in one place but not narrated
completely at every citation) — not the R4/R20 shape (a number,
independently checked, that turns out not to match its source). Applying
the same non-vote-driven, classify-by-actual-shape discipline Red Team
used at exp-101 to exclude QUANTUM's genuine `Q_ext`/`cosθ` finding from
the R20 tally (ruled "R9-shaped, not R4/R20-shaped," despite being a real
defect) — I rule MATERIALS' finding real, genuine, and mandatory to fix,
but **not R4/R20-shaped, and excluded from the R20 tally on that
classification ground, not because it is unimportant.**

**Total R4-class instances surviving Phase-3-freeze into Result/Learned,
caught only at Phase 5: 1.**

---

## 3. Explicit R20 ruling

R20's text: "three or more independent R4-class defects... surviving a
document's own Phase-3 prediction-freeze into its Result/Learned
sections, each caught only at Phase 5... constitutes a Checkpoint-4-grade
recurrence pattern."

**Arithmetic: 1 < 3. R20 does NOT fire — and this is not a close call.**
Unlike exp-101 (Iteration 78), where three genuinely distinct facts
(a mislabeled range subset, a false "3-decimal" coincidence claim, and a
false "same trend" claim across three different quantities/sections) met
the bar at the minimum sufficient count, this cycle has exactly one
distinct fact, independently confirmed by seven recomputations (six
reviewers plus this audit) using the same method, appearing in two
locations by direct propagation, not by independent re-arising. Even
under the most generous counting available — treating MATERIALS' caveat
gap as a second R20-shaped instance despite the classification argument
in §2 — the count would be 2, still one short of "three or more." R20's
bar is not met under any defensible counting this cycle produces.

This lands squarely in the pattern R20 exists to distinguish: exp-101
(the cycle immediately prior) demonstrated that this program's citation
hygiene *can* degrade to a systemic density worth a Checkpoint flag;
exp-102 demonstrates the opposite — a single, well-isolated, thoroughly
disclosed citation slip in a document that otherwise disclosed two real
findings (Gate B's honest failure, the Gate C sign bug) with unusual
rigor and cross-checked its own sign correction six ways. **R20 does not
fire.**

---

## 4. Explicit Checkpoint criterion 4 ruling (program-integrity drift,
## separate from R20's mechanical bar)

Checkpoint criterion 4: "Red Team flags program-integrity drift
(unfalsifiable claims, a constraint quietly dropped — especially #3)."

Evaluated against every candidate raised this cycle:

- **The Phase-4 process erratum (two execution agents racing).**
  Disclosed in full in NOTES.md's own dedicated section, not discovered
  by a reviewer. Independently confirmed via git: zero `lab/` diff at any
  point (§1), one final consolidated 26-call run, both real defects
  (Gate C's sign, Gate B's rescaling) discovered independently by the two
  racing agents and correctly reconciled rather than either being
  silently dropped. This is a disclosed, resolved operational hiccup —
  not an unfalsifiable claim, not a dropped constraint. **No drift.**
- **Gate B's honest FAIL.** The diagnosis (near-field Fresnel fill-in,
  point sample vs. window average at different effective standoffs) is
  physically sound, and — per EM's own Phase-5 review, which I
  independently re-checked against the three numbers in `run_output.txt`
  myself (Gate B's rescaled point 0.163% at 1.28×r_out; the established
  `BEHIND` window 1.5–1.8% at 1.35–2.63×r_out; Gate B's original
  unrescaled point 5.47% at 2.56×r_out) — the three-point ordering is
  genuinely monotonic with the correct sign, consistent with the stated
  mechanism. EM's own caveat (the specific 0.163% figure is not yet shown
  immune to near-field fringe structure at this sub-wavelength standoff)
  is a **live, correctly-scoped open question**, not a defect masquerading
  as a finding — NOTES.md's own Result text states this is "a real, open
  limitation, not a formality" and defers the fix to Next item 1 rather
  than claiming the number is settled. An honestly-flagged instrument
  limitation, with a concrete and already-identified next check (EM's
  own §7 item 1: a cheap, zero-new-FDTD 4–5-point standoff sweep on the
  already-captured field), is the correct scientific posture, not drift.
  **No drift** — and I decline to treat "not yet fully characterized" as
  equivalent to "unfalsifiable": Prediction 1's `[0,0.10]` band is wide
  enough that even a substantially fringe-shifted true value would not
  move the scored verdict, and nothing in NOTES.md claims otherwise.
- **Constraint 3 (the hard one).** Untouched this cycle by explicit,
  correct design (fix 5/6, Idealizations, Next item 4 all correctly scope
  this instrument as answering constraint 1's *physical* question only).
  No perceptual or visibility claim is smuggled anywhere in Result,
  Learned, or Next (independently re-scanned by VISION's own Phase-5
  review, which I independently spot-checked against the same three
  sections — clean). **No constraint quietly dropped.**
- **T1 escape-route.** Correctly, honestly N/A — no mechanism, material,
  or parameter is proposed or varied; independently confirmed by my own
  read of `run.py` (byte-identical R4-family constants, one `_load()` of
  a pure-constants module, no `σ(I)`/`σ(x,t)`/dispersive-`ε`/gain symbol
  anywhere).

**Ruling: Checkpoint criterion 4 does NOT fire on any ground this cycle.**
No unfalsifiable claim, no quietly-dropped constraint, no drift beyond
the single, below-bar citation instance already adjudicated under R20 in
§3.

---

## 5. Adjudication of each of the six Phase-5 reviews — adopt or override,
## with my own independent verification standing behind each call

**PHOTONICS — ADOPTED IN FULL.** Both numeric findings (§3 items 1–7 of
its review) independently reproduce against my own recomputation of
`results.json` (§1, above). Its Gate-C `2cosθ`-shape cross-check is a
genuinely independent, valid verification method, distinct from mine and
from EM's/QUANTUM's. Its aperture/profile-mismatch observation (R4
family's `edge=80`-tapered source vs. Gate B's unspecified default
profile as a confound orthogonal to standoff) is a real, previously
unflagged methodological point — checked directly against `run.py`'s own
Gate-B source construction, which indeed passes no `edge=` argument,
confirming the observation. Adopted as a genuine, non-load-bearing gap to
carry into any future Gate-B redesign. Its angular-pattern observation on
`κ_off(θ)` is correctly hedged against R5/R10 (six unevenly-spaced points,
explicitly not claimed as periodicity) — adopted as a candidate direction,
not a finding, matching its own framing.

**MATERIALS — ADOPTED IN FULL**, including the fix-7-scope finding, with
the classification refinement in §2 above (real, mandatory, but excluded
from the R20 tally as a differently-shaped defect, not because it is
unimportant). Its own recomputation set (§2 of its review) independently
reproduces against mine. Its realizability classification
(UNOBTANIUM-WITH-PARAMETERS, unchanged, correctly unaffected by this
cycle's own instrument build) is independently confirmed: I re-verified
the physical-unit identity myself (`96·15nm=48·30nm=1440nm`,
`156·15nm=78·30nm=2340nm`) and find no rescaling anywhere in `run.py`'s
Phase-4 code.

**ELECTROMAGNETISM — ADOPTED IN FULL.** Its from-scratch Gate-C
re-derivation and its code-level/hand-geometry confirmation of the
`P_off(θ)` construction both independently reproduce against my own
checks (§1). Its three-point Gate-B ordering argument (near point / old
window / far unrescaled point, monotonic and correctly signed) is a
genuine, valuable piece of corroborating evidence not present in
`NOTES.md` itself — I re-verified all three x-coordinates and κ values
directly against `run_output.txt` and confirm the ordering. Its own §4
citation-defect finding matches the single instance adjudicated in §2/§3
above exactly (same cell, same true/stated values). Its recommended
zero-new-FDTD standoff-sweep-on-the-already-captured-field diagnostic
(§7 item 1) is the correctly minimal next step, ranked appropriately.

**THERMODYNAMICS — ADOPTED IN FULL.** Its R21 third-strike-risk
discharge is independently re-confirmed by me: I grepped `run.py` myself
for `netd_row`, `cell_metrics_r4`, `pair_metrics_full` — zero executable
call sites, comment/docstring mentions only, and the one cross-experiment
`_load()` targets a pure-constants module with no thermal symbols. This
is a clean, code-level discharge, not merely NOTES.md's own assertion.
Its citation-defect finding matches the adjudicated instance exactly. Its
disclosure note on `i_abs`/`I0_corrected` remaining dimensionless (no
witness-wattage pin) is correct and non-alarmist — it explicitly states
this is not itself a defect, which I confirm: nothing in Result or
Learned treats `i_abs` as a physical irradiance.

**QUANTUM OPTICS — ADOPTED IN FULL.** Its averaging-order-fix
verification (quoting `run.py` lines 446–457 directly) is independently
confirmed by my own read of the same function. Its from-scratch
Maxwell's-equations re-derivation of the `Sx=-0.5Re{Ez·conj(Hy)}`
sign convention is a genuinely independent method from mine (source
docstring + textbook Poynting-parallel-to-propagation identity) and from
EM's (also from-scratch, but via the docstring+Poynting route without an
explicit Maxwell's-equations cross-derivation of the field-component
formulas themselves) — a third distinct derivation path reaching the
identical conclusion, which I count in my own §1 sixth-derivation tally.
Its non-classical-absorption charter check (no σ(I)/σ(x,t)/dispersive-ε/
gain anywhere) is independently confirmed by my own `run.py` read. Its
citation-defect finding matches the adjudicated instance exactly.

**VISION SCIENCE — ADOPTED IN FULL.** Its fix-5/fix-6 landing checks
(both re-scanned against Setup/Result/Learned/Next myself, confirmed
clean) and its own overclaim scan (no adaptation state, ambient level, or
`C_thr(L)` comparison invoked anywhere) are independently confirmed by my
own re-read of the same sections. Its tracing of the citation defect's
propagation into Learned #1's rounded headline (and the correct
"one root cause, two places" ruling that keeps this at one instance, not
two — adopted directly in §2 above) is the single most careful piece of
reasoning on the exact question this audit had to resolve, and I adopt
its logic explicitly rather than merely its conclusion. Its Iteration-80
priority argument — that feeding today's raw near-field κ(θ) directly
into `C_thr(L)` without first routing through the T8 bridge-family
extension would score a perceptibility verdict at the wrong physical
distance — is a substantive, correct methodological point that materially
reshapes how I sequence the reconciled queue in §7, below.

**Zero overrides. All six reviews' substantive findings adopted; the one
classification refinement (§2, MATERIALS' fix-7 finding) is a scoping
clarification of how to count it for R20 purposes, not a rejection of
the finding itself — MATERIALS' finding is adopted as a mandatory fix
(§6) in full.**

---

## 6. New finding of my own, independent of the six reviews

**The "zero `lab/` diff" claim is independently confirmed from the actual
git history, not merely from NOTES.md's own disclosure** (§1, above): the
most recent commit touching `lab/` predates this cycle by three
iterations (Iteration 76/exp-099), and the working tree shows no
uncommitted `lab/` changes. No Phase-5 review checked this against git
directly — all six correctly took the "zero `lab/` diff" claim as read
from `run_output.txt`/`NOTES.md`'s own text. This is a small,
non-load-bearing addition (nothing suggested the claim was false), but it
closes the loop with an independent source outside the document under
audit itself, which no reviewer including me should skip when git history
is available and free to check.

No additional citation/restatement defect, sign error, or gate-scope gap
was found beyond what the six reviews already surfaced.

---

## 7. Mandatory same-shift documentation fixes (zero re-run, zero verdict
## change — fixable now, per this program's own precedent)

1. **Result section**: correct the on-axis `κ(θ)` region range floor from
   `3.68×10⁻³` to `3.48×10⁻³` (true minimum, `C40_R4@41.460901°`,
   `results.json['primary_rows']['C40_R4@41.460901']['kappa_region']`).
2. **Learned item 1**: correct the rounded range from `κ~0.4–0.7%` to
   `κ~0.3–0.7%` (the true `0.348%` floor rounds to `~0.3%` under the same
   convention already used for the `0.729%→0.7%` ceiling).
3. **Learned item 1**: append the fix-7 realizability caveat (or an
   explicit forward reference to Result's own inline caveat) beside the
   restated κ(θ) headline, so a reader citing Learned #1 in isolation does
   not get an unqualified UNOBTANIUM-WITH-PARAMETERS figure. (MATERIALS'
   finding, §2/§5 above — adopted as mandatory, not merely recommended.)
4. **Process note for future fix-drafting (not a numbered rule; a stated
   convention, per MATERIALS' own recommendation)**: any future fix in
   this caveat-travel lineage should bind explicitly to the FIGURE
   wherever it is restated (Result, Learned, or Next), not only to the
   first sentence the fix's own text names — record this as house
   practice in this document's own Next section or the fix's own
   language at the next touch.

No other Result/Learned figure requires correction — every other cited
range, deviation, or ratio in this document independently reproduces
exactly (§1, and all six reviews' own §-level recomputations).

---

## 8. A new standing-rule candidate — adopted now (Red Team's own
## prerogative, per R17–R21 precedent of direct adoption at Phase 5)

Three independent Phase-5 seats (EM, THERMODYNAMICS, QUANTUM) recommend
formal ratification of NOTES.md's own Learned item 4 self-critique: a
sign relating two vector-valued quantities in a frozen self-consistency
identity was checked for magnitude and averaging-order by three
independent review passes (two Phase-2 critiques, EM and QUANTUM, plus
Red Team's own Phase-2 audit) without any of them independently
re-deriving the SIGN from the same governing convention (`u(θ)`) already
in use two lines away for an unrelated purpose (`P(θ)`'s construction) in
the same document. This is the second on-the-books instance of this
specific shape (the first: exp-073's R4 addendum, Iteration 50, catching
a sign inversion that a magnitude-only check could not distinguish) —
but a genuinely distinct rule surface from that addendum: exp-073's
addendum requires independent re-derivation of a sign correction ONCE A
DISCREPANCY IS ALREADY SUSPECTED; this cycle's gap is upstream — three
independent PRE-RUN reviewers each verified magnitude/averaging-order on
a FROZEN Phase-3 formula and none flagged the sign as unverified before
Phase 4 spent real FDTD calls against it.

**New standing rule R22 — a self-consistency identity between two
vector-valued quantities, frozen at Phase 3, must have its SIGN (not only
its magnitude or averaging order) independently re-derived from whatever
convention already governs that vector elsewhere in the same document,
before any Phase-4 FDTD call is scored against it.** Founding case:
exp-102's own Gate C, where the frozen `I0_corrected(θ)·cosθ` comparator
omitted the leading minus sign `u(θ)=(-cosθ,sinθ)` already required two
lines away — caught only after Phase 4 produced a uniform,
suspiciously-shaped ~150% "deviation" across every cell, not before. A
future cycle that ships a frozen vector self-consistency identity whose
sign is later found wrong, when three or more independent reviewers
checked its magnitude but none checked its sign before the run, fires
Checkpoint criterion 4 automatically — matching R6–R21's own "known,
named, ignored" standard, once this rule's text is on the books. **Does
not fire on its own founding instance** (exp-102), matching every prior
rule's own precedent: this cycle's own diagnostic heuristic (a
suspiciously *uniform* per-cell deviation is more likely a
formula/convention bug than a real effect — Learned item 3) caught it at
Phase 4 before any verdict was scored on the wrong formula, and both the
original error and the correction are fully disclosed in `results.json`
and `NOTES.md`.

---

## 9. Combined Verdict for Iteration 79 / exp-102: **PROMISING**

Weighing the substance: this cycle delivers a genuinely new, working
instrument that directly answers exp-101's own top-ranked Iteration-79
queue item — a phase-resolved, same-point coherent-field measurement of
constraint 1's physical transmission question, immune by construction to
both defects exp-101's Phase-5 layer found in the box-flux family
(`i_inc`/cosθ and fixed-lab-frame registration). Two of four trust-suite
gates (A, D) independently validate the primary channel by construction;
Gate D is a genuine, hand-verified fault-injection positive control, not
a self-comparison. Gate C, after a real formula-bug catch, is now the
most heavily cross-verified sign correction in this program's history —
six independent derivations, all agreeing on both sign and quantitative
shape. Gate B's FAIL is a real, honestly-diagnosed, non-fatal limitation
with a cheap, already-identified next check (EM's zero-FDTD standoff
sweep), not a defended error or a hidden gap. All five pre-registered
predictions are CONFIRMED (Prediction 2 after a disclosed correction).
R21's thermal-sidecar risk is discharged cleanly at the code level,
independently confirmed by two seats and by me. The one real defect this
document carries (the κ_region range floor) is a single, non-load-bearing
instance — well below R20's firing bar, immediately following the cycle
that first fired it, demonstrating the density pattern was an isolated
recurrence, not a systemic regression. No constraint is quietly dropped;
no unfalsifiable claim is made; the process erratum is disclosed,
resolved, and independently confirmed to have touched zero `lab/` code.

This nets out clearly above PARTIAL: every scored verdict stands, the
core new capability is real and correctly gated, and the citation-hygiene
finding is a single, well-isolated slip in a document that otherwise
disclosed its own two genuine findings (Gate B, Gate C) with unusual
rigor. **Combined Verdict: PROMISING.**

---

## 10. Reconciled Iteration-80 queue (Red Team's own ranking, resolving
## the six seats' partially-overlapping top-3 lists)

Five of six seats (PHOTONICS, MATERIALS, EM, THERMODYNAMICS, QUANTUM)
independently rank a Gate-B fix at or near their own #1; VISION's own #1
(the Tier-2 perceptual conversion) explicitly names the T8 bridge-family
extension as its own precondition, not a competing priority — the same
extension MATERIALS ranks #2. These are not six independent priorities;
they cluster into three real workstreams plus one governance item already
discharged in §8. Sequencing, not choosing, resolves the apparent
disagreement — matching this program's own established resolution pattern
(exp-100/101's own Reconciled-queue precedent).

**Tier 1 — cheap, zero-new-FDTD, unlocks everything else:**
1. **EM's zero-additional-FDTD standoff diagnostic**: 4–5 point/region
   readings between Gate B's corrected point (x=352) and the established
   `BEHIND` window's near edge (x=357), read off the field array Gate B's
   own run already captured. Disambiguates "smooth Fresnel fill-in" from
   "fringe-limited near-field null" before any gate redesign — the
   single cheapest, highest-information next step, and a precondition for
   trusting item 2's own redesign choices.
2. **A properly footprint- AND aperture-matched Gate B** (NOTES.md's own
   Next item 1, sharpened by PHOTONICS' aperture-taper control): rebuild
   the cross-scale reproduction check against the literal `BEHIND` window
   footprint, using the SAME `profile="plane", edge=80` source
   construction as the R4 family, not Gate B's own unspecified default
   profile — so a future PASS/FAIL genuinely isolates standoff from
   aperture shape. This is the single highest-priority substantive fix:
   until it exists, every κ(θ) citation rests on internal self-consistency
   (Gates A/D) alone, with no independent old-instrument cross-check.
3. **Extend the coherent point/region instrument across the T8 bridge
   family (r=78/156/312)** (MATERIALS' #2, VISION's own stated
   precondition for Tier 2) — cheap, same code, no new machinery. This is
   the single item both MATERIALS' quantitative realizability claim
   ("shallower, not deeper" as a number, not merely a direction) and
   VISION's Tier-2 conversion need before either can proceed soundly;
   sequencing it here, alongside items 1–2, avoids doing it twice.

**Tier 2 — gated on Tier 1's outputs:**
4. **The Tier-2 perceptual conversion** (constraint 1's own missing
   conversion, QUANTUM's #2, VISION's #1) — explicitly gated on item 3's
   bridge-family extrapolation to witness scale, per VISION's own
   correctly-argued warning against scoring `C_thr(L)` at today's raw
   near-field standoff.
5. **Pin the witness-scale absolute source wattage** (THERMODYNAMICS'
   #1, T5's long-open precondition) — parallel-track with items 1–4, not
   blocking them; needed before `i_abs(θ)` can be cited as a physical
   irradiance for any future thermal/detectability claim.

**Tier 3 — standing, correctly deferred, but now flagged for scheduling:**
6. **Tier 1's own R3-vs-R4 `delta_scene` split** (PHOTONICS' zero-FDTD
   physical-hypothesis check, still first in queue) — now deferred three
   consecutive cycles (exp-100→101→102), each time correctly out of scope
   for an instrument-building cycle, but the program's own precedent (the
   T1:N/A eight-cycle flag at Iteration 77/78) counsels naming a
   deferral count explicitly once it reaches three; Iteration 80 should
   either execute PHOTONICS' own committed zero-FDTD check or explicitly
   re-justify a fourth deferral in writing.
7. **PHOTONICS' dense angular resweep of `κ_off(θ)`**, pre-registered
   against a null-permutation/circular-shift control before any
   periodicity is fit (R5/R10 discipline) — a genuine, cheap, independent-
   instrument-class opportunity to corroborate or rule out the recurring
   T21/T28-adjacent angular structure, ranked last only because it is
   exploratory and blocks nothing else.

**Governance — adopted now, not queued:** R22 (§8, above).
