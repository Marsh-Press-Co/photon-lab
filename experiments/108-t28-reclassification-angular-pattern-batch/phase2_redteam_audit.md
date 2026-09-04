# PHASE 2 — RED TEAM AUDIT · Panel Iteration 85 (candidate exp-108)
## "The Two-Cycle-Old Reclassification Fix, R25/R23 Governance Rulings, and a Bundled `angular_scattered_pattern`/Absolute-Floor/Suite-Stage Batch"

Red Team seat, fresh context. Received: PANEL.md, LOGBOOK.md in full,
PLAN.md's Vision/Current-state, the Phase-1 proposal, and all five blind
Phase-2 critiques (MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM
OPTICS, VISION SCIENCE — PHOTONICS is this cycle's lead and does not
critique its own proposal). Every load-bearing figure below was
re-derived from primitives (`experiments/106-.../run.py`,
`experiments/106-.../results.json`, `experiments/107-.../results.json`,
`lab/sections.py`, `lab/validation/run_all.py`), not trusted from any
seat's restatement, including this document's own quotations.

---

## 0. Independent re-verification from primitives

**0.1 Tier-0 item 1's own source claims.** Read `experiments/106-.../
run.py` directly. The classification block runs **line 753**
(`sr_fa = p4_fa["shape_ratio"]`) through **line 765** (the `print(...)`
reporting it), confirming the proposal's own correction of the
"754–765" figure a prior source used. `grep -n "p_abs_frac_diff"
run.py` returns exactly four lines (593, 595–596, 672, 674–675) — two
definitions, two print statements, zero uses inside the classification
construction. Insertion point checked line-for-line: line 759 reads
`classification = "AMBIGUOUS"`, line 760 opens
`if p4_fa["noise_flag"]["noise_dominated"]:` — the patch's stated
insertion point ("immediately after 759, before the 760–761 wrap") is
exactly right.

**0.2 `results.json` headline numbers (exp-106).** Loaded and inspected
directly:

| Field | Proposal's claim | Verified value |
|---|---|---|
| `p_abs_frac_diff_156` | 0.1231 | 0.123057953... ✓ |
| `p_abs_frac_diff_312` | 0.1796 | 0.179622077... ✓ |
| `shape_ratio_fixedabs` | 18.2283 | 18.228333623... ✓ |
| `abs_ratio(156)`/`(312)` | 1.0852 / 1.8797 | 1.085174... / 1.879657... ✓ |
| Current classification string | no `THREE-WAY-AMBIGUOUS` | `"REFUTES-electrical-thickness-growth-hypothesis (NOT-TRUSTED -- r=312 MARGINAL/unsettled)"` ✓ (confirms the trigger fires and is currently unwired) |
| `shape_ratio_fixedabs_trusted` | — | `False` — confirmed the NOT-TRUSTED wrap is independently already firing; the new THREE-WAY-AMBIGUOUS wrap must compose with it exactly as §2a specifies (outer-wrap the existing string, not replace it) |

**0.3 exp-107's own `abs_ext_ratio_hollow`/`abs_ext_ratio_pec_cored_exp106`
deltas.** `item1_rows` gives `delta_abs_ext_ratio` = **−2.96857×10⁻⁵**
(r=156) and **−2.46843×10⁻⁵** (r=312) — matches the proposal's cited
2.97×10⁻⁵/2.47×10⁻⁵ to 3 significant figures. `floor_gate_article_
numerator.frac_unresolved` = 0.18275 (r=156) / 0.2675 (r=312), matching
item iii's own cited exp-107 hollow-reading bands exactly.

**0.4 THERMODYNAMICS' 30.9%/46.3% recomputation.** Independently
re-derived from exp-107's `item3_rows` (not trusted from the critique's
own restatement): `p_abs_w` fixedabs/selfsim at r=156 =
9.283886×10⁻¹²/7.093308×10⁻¹² → fractional divergence
**0.30895 (30.9%)**; at r=312, 4.151263×10⁻¹¹/2.837132×10⁻¹¹ →
**0.46318 (46.3%)**. Both exact. Minimum margin across all four
`item3_rows` cells is 117.46× (`fixedabs_312`), confirming "≥117×"
below the 0.020 K NETD floor. THERMODYNAMICS' critique is arithmetically
airtight.

**0.5 MATERIALS' T9-anchor correction.** LOGBOOK's own Iteration-84
entry (line ~8163, Red Team's own Phase-5 final audit) states
"PHOTONICS' 19.0×/15.8×" as an independently re-verified figure, and
PLAN.md's Current-state section restates it identically ("real gap
19.0x/15.8x, not '~10x'"). The Phase-1 proposal's own §1 narrative
(this cycle) still writes "the same order T9 found at r=78" — the
pre-correction framing. MATERIALS' attack is factually correct: this is
a live regression of an already-corrected figure back into the record,
one cycle after the correction was filed.

**0.6 EM's box-separation arithmetic.** Read `geom()` directly
(`experiments/106-.../run.py:121-158`): `box_a_hw = R_COAT +
round(32·k)`, `box_b_hw = R_COAT + round(57·k)`, `k = r/78`. At r=156
(`k=2`): margins 64/114 cells, separation 50 cells = 2.5λ at
`CPL_600=20`. At r=312 (`k=4`): margins 128/228 cells, separation 100
cells = 5λ. EM's "≈2.5λ at r=156, ≈5λ at r=312" is exact, not
approximate.

**0.7 Domain-clearance arithmetic (r=312, margin=65 box).** `N0=560`,
`CX0=252`, `ABSORB=40`. At r=312 (`k=4`): `N=round(560·4)=2240`,
`CX=round(252·4)=1008`, `R_COAT=312`, `box_hw = 312 + round(65·4) =
572`. `x ∈ [1008−572, 1008+572] = [436, 1580]`, comfortably inside the
valid `[40, 2200]` interior. Confirmed independently, matching both
the proposal's and MATERIALS' own figures.

**0.8 `_STAGE_IDS` state.** `lab/validation/run_all.py` currently
defines `stage23`…`stage25` as the highest-numbered stages, with
`_STAGE_IDS = frozenset(str(n) for n in range(1, 26))` (covers "1".."25").
No `stage26` exists yet. The proposal's claimed diff (`stage26_chunked_
run_identity`, `_STAGE_IDS` → `range(1,27)`) is consistent with the
current file — accurate, not a stale claim.

**0.9 The "zero marginal cost" bundling claims (item i/ii/iii),
checked against actual code, per §7's own named falsifier.**
`lab/sections.py::widths()` and `angular_scattered_pattern()` both take
`box` as a plain post-hoc tuple argument over already-captured phasor
fields (`cap_scene`, `cap_empty`) — no `Sim.run()` is involved in
varying the box. This confirms items ii and iii genuinely cost zero
additional FDTD calls once item i's three captures per r exist, exactly
as claimed. `ledger_check()` (`run.py:298`) requires `sigma_e_article`
to compute `closure`; `_run(..., capture_sigma_e=True)` supplies this on
the SAME call already scheduled, so EM's flip-condition ask (add
`closure`, "zero new FDTD if `sigma_e` is captured alongside the
PEC-cored fields item i already schedules") is also confirmed
cost-free, not merely plausible.

**0.10 R23/R24/R25 registry text, re-grepped directly, not quoted from
the proposal.** R25's entry (LOGBOOK.md ~997–1038) opens exactly:
*"(not a ruled-out idea; a standing house-discipline rule, proposed and
ratified by Red Team's own Phase-5 final audit, Iteration 84)"* —
confirms §2a item 2's quotation verbatim; R25 is already ratified, this
queue line is bookkeeping. R23's entry (LOGBOOK.md ~908–944) confirms
the Iteration-81 founding text and the three-cycle-old open scope
question exactly as §2a item 3 states it. R24's entry confirms the
distinguishing "same-cycle wiring gap" vs. R25's "cross-cycle
queue-survival gap" split the proposal draws in §2a item 2 is the
correct reading of both rules' own text.

**Constraint-3 structural check (not merely accepted from the
proposal's own claim).** Grepped the Phase-1 proposal, `run_all.py`'s
proposed new stage, and `run.py`'s `DISCLAIMER` text: zero occurrences
of `C_thr`, `ambient`, `Weber`, or any perceptual-scoring construction
anywhere in this cycle's own scope. The only `lab/` diff disclosed
(§6) is `stage26_chunked_run_identity()`, a pure FDTD-identity
regression test unrelated to constraint-3 machinery. **T1/constraint-3
is N/A throughout, confirmed structurally, independent of the
proposal's own self-report.**

---

## 1. Numbered attacks

**Attack 1 — [inconsistency] The exact `run.py` patch does not match
the execution method §2a item 1 claims for it.** §2a item 1's own prose
states `reclassify_106.py` achieves "zero new `Sim.run()` calls" by
"importing the corrected function from the patched `run.py`." But the
patch given is literal inline code inserted into the monolithic
procedural body of `run.py` (between lines 759 and 760, inside the same
scope that also drives real `Sim.run()` calls for r=312) — there is no
standalone, importable, pure function of the form `f(sr_fa,
noise_dominated, trusted, p_abs_frac_diff_156, p_abs_frac_diff_312) →
classification_string` anywhere in the patch as written. Phase 3 is left
to resolve this in one of (at least) two differently-shaped ways: (a)
actually extract such a function, used by both `run.py`'s own inline
flow and `reclassify_106.py` (satisfying the "one number, one name" R4
discipline the same patch already applies to the threshold constant),
or (b) let `reclassify_106.py` re-implement the classification logic as
its own duplicate inline block, reading the four already-persisted
scalars from `results.json` — a maintenance-drift risk (two independent
copies of the same decision rule) this program's own R4/R9 lineage
exists to catch. **This is exactly the shape of specification gap the
proposal's own §7 asks Red Team to check for ("fully specified enough
to apply without further interpretation") and it fails that bar as
written.** Verified this is not merely a hypothetical: `run.py` (read in
full structure) contains no function boundary anywhere near line
753–765 that could be imported without also importing the surrounding
Sim-driving code.

**Attack 2 — [unfalsifiable] Items i and ii each leave an unregistered
middle verdict zone between their own CONFIRM and REFUTE/Falsified-if
bands.** Item i: CONFIRM requires every floor-cleared bin ≤5% relative
deviation; REFUTE requires a ≥3-bin contiguous run at ≥15% AND
`box_b` reproduction. A result with, say, a single 8%-deviation bin, or
a 3-bin run at 10% that fails to reproduce at `box_b`, satisfies
neither named branch — no verdict string is pre-registered for this
region, unlike the `shape_ratio_fixedabs` classifier three lines away in
the same codebase, which explicitly names `AMBIGUOUS` as a third state
between its own CONFIRM/REFUTE bands (`SHAPE_RATIO_FIXEDABS_CONFIRM=8.0`
/ `_REFUTE=14.8`). Item ii has the identical shape: nothing is
pre-registered for `0.5×|Δ_boxA| < std < |Δ_boxA|`. **This program's own
house discipline (predictions committed to git BEFORE the run) exists
precisely to prevent an interpretive label being invented at Phase 4/5
on the spot; as currently drafted, a plausible, even likely, outcome
region for both items has no such label.** Minimum fix: add an explicit
`AMBIGUOUS`/`NODE-UNRESOLVED-BY-CONSTRUCTION`-style third band to each
table before Phase 3 freeze, mirroring the `shape_ratio_fixedabs`
convention already in the same file.

**Attack 3 — [unfalsifiable, minor] Item iv's negative control never
states its own pass/fail boundary precisely.** "Predicted": deviates
">1% relative." "Falsified if": "reproduces the true result anyway" —
this is not the logical negation of ">1%" (it does not say "≤1%," or
name any number at all), leaving a soft gap at exactly 1% and an
undefined "reproduces" threshold. Low-stakes (a code-only positive/
negative control on a canonical bench scene) but the same shape as
Attack 2, worth a one-line fix (state the falsified-if branch as
"`≤1%` relative" explicitly) before Phase 3 freeze.

**Attack 4 — [constraint-#3-violation check, structural, negative
result] Confirmed no item in this cycle risks constraint 3 even
indirectly.** Per §0's structural grep: no perceptual-scoring code path
exists anywhere in this cycle's scope; the only `lab/` diff is a pure
FDTD-identity regression stage. Recorded here explicitly, as the task
brief requires a structural (not proposal-trusting) confirmation, not
because any risk was found.

**Attack 5 — [inconsistency] The "belt-and-suspenders" premise behind
the R23 ratify-as-scoped ruling (§2a item 3(a)) overstates its own
redundancy, independent of VISION's critique (cross-checked, not merely
adopted — see §2).** Re-traced all three cited catches against LOGBOOK
directly: exp-104's founding scope gap (caught at Phase 5, three seats'
code re-read), exp-105's missing `PREDICTIONS_TEXT` assert (VISION,
Phase 5), exp-107's zero-`DISCLAIMER`-code gap (VISION's own Phase-5
self-review, independently re-confirmed by Red Team's own grep, also
Phase 5). All three trace to the SAME mechanism — a voluntary Phase-5
seat code-read — never to the Phase-2 Red Team scan the proposal cites
as the second independent layer. The Phase-2 scan cannot structurally
catch this class of gap: it fires against a scored constraint claim,
and every one of these three cycles scored none. This does not by
itself flip the R23 ratify-as-scoped OUTCOME (the cost argument in
premise (b) — inventing a "document family" taxonomy — stands
independently of premise (a)'s soundness), but the ruling's own stated
justification is partly false as written and must be corrected, not
merely caveated, before Phase 3 treats it as closed.

---

## 2. Disposition of the five blind Phase-2 critiques

**MATERIALS — ADOPT, in full, unconditionally.** §0.5 independently
reproduces the "same order" vs. 19.0×/15.8× regression exactly.
Steel-man and box-domain-arithmetic checks both independently
reconfirmed (§0.6/0.7 above land on identical figures). Folded into the
mandatory fix list: correct §1's own T9-anchor sentence to the
established 19.0×/15.8× gap before Phase 3 freeze — a narrative fix
only, changes no gate, no band, no FDTD call.

**ELECTROMAGNETISM — ADOPT the core finding in full; extend its remedy
rather than picking either offered option in isolation (see §3).** The
EM-precision distinction (total flux through a closed surface is
box-independent by Poynting conservation — what stage 8's own `≤0.12`
convention actually tests; the ANGULAR DISTRIBUTION of that flux at two
points 2.5–5λ apart is a different, near/mid-field-sensitive quantity
with no such guarantee) is independently re-verified from `lab/
sections.py` and `run.py`'s own `geom()` (§0.6). This is real and
load-bearing: as written, item i's REFUTE gate can (a) wrongly discard a
genuine angular anisotropy whose lobe structure migrates between
`box_a` and `box_b`'s differing radii, or (b) pass a spurious two-point
coincidence, and it does not test what §4/§7 claim it tests. ADOPT the
`closure`-narration ask outright (§0.9 confirms zero marginal cost).
Regarding EM's own two offered remedies (converge across ≥3 box radii,
or relabel a `box_a`-only feature `NEAR-FIELD-RADIUS-DEPENDENT`): I do
not pick either as stated — §3 below shows a stronger, unified fix that
reuses machinery this cycle already schedules at zero additional cost,
folding EM's own option (a) together with QUANTUM's finding.

**THERMODYNAMICS — ADOPT, in full, unconditionally.** §0.4
independently reproduces 30.9%/46.3% bit-for-bit from `item3_rows`, and
the ≥117× margin figure. The critique's own diagnosis (the "N/A
confirmed structurally" claim in §3/§6 was reached by never looking at
the one place THERMODYNAMICS' own charter collides with the headline
action, not by checking) is the correct R8-shaped framing — genuinely a
"never looked, not merely wrong" gap, not a mistake in either
direction's conclusion. Mandatory fix: add the flip-condition sentence
verbatim to §6 Idealizations before Phase 3 freeze.

**QUANTUM OPTICS — ADOPT the core finding in full; fold its remedy into
the same unified fix as EM's (§3).** Independently confirmed: the six
margins `{24,32,40,48,57,65}×k` sample the SAME deterministic field
snapshot at monotonically increasing radius, not exchangeable draws —
any smooth near-to-far-field convergence in `abs_ext_ratio` (a real,
physically expected effect independent of any genuine hollow-vs-
PEC-cored signal) inflates raw `std` exactly the way QUANTUM describes,
conflating bias with placement noise. This is the same underlying box-
radius-is-not-an-exchangeable-nuisance-parameter defect Attack 6 (§3)
identifies for item i. ADOPT the monotonicity-check-before-trusting-std
ask; superseded in form (not in substance) by the unified §3 fix, which
is stronger than a bare residual-from-fit because it also fixes item i's
box-independence bar using the SAME data.

**VISION SCIENCE — ADOPT, in full, unconditionally.** Independently
re-traced all three cited R23 catches (§0/Attack 5 above) and confirm
VISION's count is right: one mechanism, not two, 3/3. ADOPT the
mandatory Phase-4 live-fire check (`run.py --predictions-only`, grep for
`DISCLAIMER`, result reported in NOTES.md before the R23 ruling is
treated as closed) as a bound condition, matching exp-104's own
precedent VISION cites. This does not, on its own reasons, force
rejecting the ratify-as-scoped OUTCOME (see Attack 5) — but the ruling's
own text must be corrected, and the live-fire check is genuinely
load-bearing to trusting it, not optional polish.

No critique is overridden. All five are independently re-verified from
primitives and adopted; QUANTUM's and EM's remedies are not rejected but
combined into a stronger single fix (§3), which is the deeper structural
finding this audit's task brief specifically asked for.

---

## 3. The EM/QUANTUM combined defect: box radius is not an exchangeable
nuisance parameter, in either channel item i or item ii uses it in

**Do EM's and QUANTUM's attacks combine into one deeper defect?** Yes.
Both attacks are instances of the identical root-cause error, applied to
two different quantities built from the same box-family machinery:

- **Item i** (angular pattern): trusts a REFUTE only if a feature
  reproduces "same location, same sign" between `box_a` and `box_b` —
  treating the two box radii as if they should sample the SAME
  underlying angular distribution, when the angular distribution of
  scattered flux is a near/mid-field quantity known (by the function's
  own docstring, `VALIDATION.md`) to depend on observation radius.
- **Item ii** (absolute-floor family): treats `std` across six
  increasing box margins as a noise-floor proxy — an exchangeable-
  sample statistic — when the six margins are an ORDERED sequence
  around one deterministic field snapshot, where any real quantity
  (here, `abs_ext_ratio`) is physically expected to trend smoothly with
  box radius as the box converges from near-field toward the asymptotic
  cross-section.

In both cases, this cycle's own Tier-1 falsification logic implicitly
models "which box radius the measurement happened to use" as a
**random, iid nuisance dimension** (a noise-floor/placement-jitter
model — exactly stage 8's own `box_dev`/`box_a`-vs-`box_b` idiom,
which is legitimate there because stage 8 tests a scalar, Poynting-
conserved, genuinely box-independent quantity, `sigma_ext`). Item i and
item ii instead each build a NEW quantity — a per-bin angular reading,
and a between-family difference-of-ratios — that inherits none of that
conservation guarantee at a fixed pair of radii, and treats box radius
as if it still had it. This is a single defect wearing two costumes, not
two unrelated critiques that happen to land in the same cycle.

**The unified fix — reuses already-scheduled data, zero marginal
`Sim.run()` cost (verified, §0.9):** item ii's own six-margin family
`{24,32,40,48,57,65}×k` is not merely a floor characterization — it is
also the exact instrument EM's own option (a) asks for ("converge as a
function of box radius across ≥3 box sizes"), already scheduled, on the
same already-captured PEC-cored/hollow phasor fields item i uses.
Concretely, before Phase 3 freezes the predictions table:

1. **Item i's REFUTE gate**: replace "reproduces same location/sign at
   `box_b`" with — compute the candidate angular feature (or, more
   simply, `abs_ext_ratio`'s own per-bin analogue) at all 6 margins, not
   2; a genuine anisotropy signature should either (a) be stable in
   angular location across the full margin family, within a tolerance
   set from the SAME data, or (b) show smooth, small-parameter
   MIGRATION consistent with near-to-far-field lobe evolution (a
   physically real, not spurious, pattern) — distinguishable from noise
   by whether 6 points trace a smooth curve or scatter randomly. A
   2-point match/mismatch at `box_a`/`box_b` cannot make this
   distinction; 6 points can.
2. **Item ii's noise floor**: before reporting raw `std` across the 6
   margins as a placement-noise proxy, report whether the sequence is
   monotonic (or fits a smooth `1/margin`-type trend) in margin, at both
   r. If it is, report the residual-from-fit `std` (QUANTUM's own ask)
   as the genuine floor — the raw std conflates a real, expected
   near-field-convergence bias with placement jitter, and Tier-2 item
   1's own re-derived confirms band should NOT be built on the
   un-detrended number.

Both changes are **reporting/statistics fixes on data this cycle
already schedules to capture** — zero new `Sim.run()` calls, matching
this cycle's own established cost discipline. This is the deepest
finding of this audit and is folded into the mandatory fix list below
as a single combined item, not two.

---

## 4. R25's own status this cycle

**Ruling: R25 does NOT fire this cycle, and the founding instance
(exp-106→107) is being closed correctly on paper — CONDITIONAL on
Phase 3/4 actually executing the patch, not merely re-describing it a
third time.** Read against R25's own operative text: the rule targets a
fix "disclosed only in prose" that "fails to survive into the next
cycle's own authoritative cross-cycle-memory artifact" — specifically,
being left as "a parenthetical aside inside a different numbered item's
prose" rather than "its own explicit, numbered line item." This
cycle's Tier-0 item 1 is textually a clean, distinct, non-parenthetical
line item, fully specified down to insertion point and exact code
(modulo Attack 1's function-boundary gap) — this is precisely the shape
R25 exists to require, and on its face discharges the rule cleanly.

**But R25's own text is silent on a genuinely live risk this cycle
introduces: routine Phase 1→3 deferral (the proposal states "I do not
edit `run.py` myself... Phase 3's job") is NOT itself the R25 failure
mode (every PANEL.md cycle defers code execution from Phase 1 to Phase
3 by design) — but it becomes indistinguishable from a THIRD silent
drop if Phase 3/4 apply the SAME "flag, don't execute" pattern exp-106's
own audit used, and NOTES.md's Result section states the fix is
"specified" or "recommended" rather than confirming it was actually
run and its output checked against §4's own predicted band.** This is
not hypothetical: it is the literal mechanism that produced the
exp-106→107 gap in the first place (a fix fully described in prose,
never executed, and the description alone was mistaken for closure).
**Mandatory fix, folded below: NOTES.md's Phase 3 synthesis and Phase 4
Result MUST state explicitly, with the reclassified string quoted
inline (not merely referenced), that the patch was applied and
`reclassify_106.py`'s (or `run.py`'s own re-run) output was checked
against Tier-0 item 1's own predicted band. If a future cycle's audit
finds this cycle's own Tier-0 item 1 was, in fact, only described and
not executed, that is the literal second R25 instance and should fire
Checkpoint criterion 4 automatically per R25's own forward-elevating
clause — flagged here explicitly so no future audit has to rediscover
the mechanism from scratch.**

Items 2 (R25 ratification bookkeeping) and 3 (R23 scope ruling) are
correctly read against LOGBOOK's own text (§0.10); item 3's own stated
justification requires the Attack-5/VISION correction before being
treated as sound, but the ruling's outcome is not, on the evidence
available, wrong.

---

## 5. Overall verdict: **PROCEED-WITH-MANDATORY-FIXES**

The governance work (Tier 0) is sound in structure and largely sound in
execution; the physics batch (Tier 1) is honestly two-sided and
correctly gated in its reproduction/floor/box-independence disciplines
in the abstract, but item i's and item ii's own specific falsification
logic shares one real, previously-uncaught structural defect (§3) that
would, left unfixed, let a spurious box-radius artifact drive a REFUTE
or corrupt the noise-floor band Tier-2 item 1 leans on. None of the
seven mandatory fixes below requires additional `Sim.run()` calls beyond
what this cycle already schedules; none changes the T1/constraint
scoring (still correctly N/A throughout, confirmed structurally, §0).

**Mandatory fixes, before any Phase-4 FDTD call:**

1. **[Attack 1]** Resolve the run.py-patch/`reclassify_106.py`
   specification gap: either extract a standalone, importable
   classification function used by both `run.py` and
   `reclassify_106.py`, or explicitly disclose that
   `reclassify_106.py` duplicates the logic and accept the associated
   drift risk in writing.
2. **[MATERIALS, §0.5]** Correct §1's T9-anchor sentence to the
   established 19.0×/15.8× gap (not "same order").
3. **[THERMODYNAMICS, §0.4]** Add the one-sentence 30.9%/46.3%
   real-absorbed-watts-divergence confirmation (with margin ≥117×) to
   §6 Idealizations, sourced to exp-107's own `item3_rows`.
4. **[EM + QUANTUM combined, §3]** Replace item i's `box_a`/`box_b`
   two-point REFUTE bar and item ii's raw 6-box `std` with the unified
   multi-margin convergence/detrending check described in §3, using
   the already-scheduled 6-margin family for both.
5. **[EM, §0.9]** Add `ledger_check()`'s `closure` field to the
   predictions table as a named check (zero marginal FDTD cost,
   confirmed).
6. **[Attack 2]** Add an explicit named middle-verdict band (e.g.
   `AMBIGUOUS`) to items i and ii's predictions tables, matching the
   `shape_ratio_fixedabs` classifier's own three-way convention already
   in the same codebase.
7. **[VISION, §0/Attack 5]** Correct §2a item 3(a)'s "belt-and-
   suspenders" claim to state it traces to one mechanism (voluntary
   Phase-5 code-read), not two independent layers, and add VISION's
   mandatory Phase-4 live-fire check (`run.py --predictions-only`,
   grep for `DISCLAIMER`, reported in NOTES.md) as a bound condition of
   the R23 ratify-as-scoped ruling.

**Additionally, not a gate on Phase 4 but binding on Phase 3/4's own
Result-writing (§4):** NOTES.md must state explicitly, with the
reclassified string quoted inline, that Tier-0 item 1's patch was
actually applied and checked — not merely described — closing R25's
founding instance on the record, not only in intent.

---

## 6. Reconciled Iteration-86 queue (provisional — superseded by
Iteration 85's own Phase-5 Red Team final audit)

**Tier 0 — zero FDTD, governance/closeout:**
1. Confirm (or, if Phase 3/4 did not close it, execute) Tier-0 item 1's
   actual code application and the function-boundary fix (mandatory fix
   1); if this did not happen this cycle, that is R25's second instance
   and fires Checkpoint criterion 4 automatically per §4's own ruling.
2. Formally re-derive Tier-2 item 1's own `≤2×10⁻⁵` confirms band using
   the DETRENDED (not raw) 6-box residual std from mandatory fix 4, not
   the raw std the Phase-1 proposal's own §4 currently proposes to lean
   on.
3. Restore `Q_ext`-invariance/`closure` corroboration into exp-106's
   Result prose (deferred three consecutive cycles now — 106/107/108 —
   closed at least partially by mandatory fix 5 this cycle, but the
   narration into exp-106's own frozen Result text is still open).
4. Decide the constraint-3-immunity reopening condition (Iteration-85's
   own Tier-2 item 4) — a VISION/MATERIALS-charter question, still
   unclaimed; should be taken up by whichever seat next rotates to lead.

**Tier 1 — cheap/adjacent FDTD:**
1. If this cycle's r=312 leg is cost-gate-aborted, re-attempt with a
   fresh cost estimate (the pilot-and-abort structure is sound and
   reused verbatim; only the estimate itself would need updating).
2. Reframe Item 4's "worsens with r" claim with a genuine third r-point
   on the numerator channel specifically (still not discharged — this
   cycle's own item iii adds a same-r cross-check, not a new r-point,
   by its own §5 admission).
3. Extend `angular_scattered_pattern` to the oblique-incidence axis
   (θ≠0°) now that the instrument has its first-ever validated
   application to this shell family at r≠78 — promote from Tier 3 to
   Tier 1 once this cycle's own reproduction-precondition and §3's
   convergence check both clear.

**Tier 2:**
1. A fourth r-point (r=624) to empirically test THERMODYNAMICS'
   `r^-1.16` fixed-abs projection (≈52.6× margin, just above the 50×
   `box_dev` floor) — `box_dev`'s own margin has thinned from T9's
   founding ~1221× to ~9.0× at r=312; this is a live, not merely
   historical, risk to the whole family's trust basis.
2. Formalize the absolute-floor box family's 6 margins from a
   resolution/aliasing bound (this cycle's own §6 idealization names
   this as owed, not done).
3. Widen the R23 scope decision's own text with the corrected
   belt-and-suspenders framing (mandatory fix 7) as a standing note —
   documentation only, no new machinery.

**Tier 3 — long-standing, unchanged by this cycle:**
The 750/450nm wavelength-generality leg; the `G40` full-width leg; the
x-wall admittance refit; `PAD`-with-article survival; a genuinely
different bridge-family geometry; the near-null-exclusion refinement
(now 4+ cycles deferred). None of these compete with this cycle's own
disclosed budget and none is newly created or newly deferred by this
document.

Full record: `experiments/108-t28-reclassification-angular-pattern-batch/`
— Phase-1 proposal (PHOTONICS), five Phase-2 blind critiques
(`phase2_critique_{materials,em,thermodynamics,quantum,vision}.md`),
this Phase-2 Red Team audit.
