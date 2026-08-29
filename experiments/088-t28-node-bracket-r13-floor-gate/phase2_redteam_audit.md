# PHASE 2 — RED TEAM FINAL AUDIT · exp-088 · Panel Iteration 65

*Fresh context. Read: PANEL.md in full; LOGBOOK.md's RULED OUT (R1–R13) in
full and LIVE THREADS/T28 in full through Iteration 64/exp-087;
`phase1_proposal.md`; all five blind Phase-2 critiques; exp-087's
`NOTES.md`/`run.py`; exp-083's `results.json::per_theta` (independently
re-derived from raw JSON throughout, not trusted from any seat's own
prose — R4/R9 discipline).*

## 0. Independent verification performed (before adjudicating anything)

All load-bearing numbers below were recomputed from primitives, not
restated from the proposal or any critique:

- Recomputed `RMS[frac_contrast(θ)]` over all 31 points of
  `experiments/083-.../results.json::per_theta`: **`1.9174375118374476×10⁻³`**
  — matches §4's cited `1.91744×10⁻³` exactly. `FLOOR=1.91744×10⁻⁴`
  reproduces. All five cited margins (3.879×/0.386×/6.589×/7.4946×/8.019×
  at 36.0°/38.6°/41.8°/38.4°/38.8°) reproduce to full precision — the
  displayed "7.50×" at 38.4° is confirmed a rounding artifact of the
  4-sig-fig table operands (true value 7.4946×), not an error, matching
  VISION's own independent finding.
- Recomputed `delta_scene(θ)`'s sign changes across the full 31-point
  window by linear interpolation between adjacent grid points: **exactly
  four zero-crossings in [36°,42°]: 37.127°, 38.590°, 40.265°, 41.461°**
  — reproduces PHOTONICS' claim exactly (their reported 38.590° matches
  the filed `θ₀` value bit-for-bit).
- Recomputed `frac_contrast(θ)/FLOOR` at the two other established-grid
  points nearest the extra crossings: **θ=40.2°: 1.4764×; θ=41.4°:
  1.3095×** — confirms PHOTONICS' claim that these margins are tighter
  than the two angles this cycle actually brackets (7.49×/8.02×).
- **Refinement PHOTONICS did not state**: applying `FLOOR_FRAC=0.10` to
  the FULL 31-point window, only **1 of 31** points fails the gate
  (38.6° itself, 0.386×) — 40.2°/41.4° both clear (>1×), just with less
  margin. So the floor *threshold* is not miscalibrated by this evidence;
  the real gap is that `ratio_k` (which needs a real FDTD `frac_p_abs`
  measurement, not just the desk-computable `frac_contrast`) has never
  been measured at 28 of these 31 angles, including all three of the
  other node-adjacent ones. This changes which of PHOTONICS' two possible
  remedies is correct — see §1.
- Recomputed exp-087's own linear-interpolation figures from
  `experiments/087-.../results.json::frac_p_abs`: interpolated
  `4.13734×10⁻³`/`4.49932×10⁻³` at 38.4°/38.8°, and the 38.6° interior
  check reads `+7.943%` high — reproduces §6/Q4 exactly.
- Recomputed THERMODYNAMICS' cited `p_abs_w`/`ratio_abs_ext_raw` smoothness
  claim from `experiments/087-.../results.json::thermo`: `p_abs_w` spans
  `2.749×10⁻¹²→3.258×10⁻¹² W` (≈18.5%) across 36.0°→41.8°,
  `ratio_abs_ext_raw` pinned to `0.5128–0.5138` — reproduces exactly.
- Recomputed `xi_ext` at 38.6° from the same file: max `3.484×10⁻⁴`
  (BOX_B, C40) — reproduces EM's cited "`≤3.5×10⁻⁴`" claim.
- Re-derived `dg069.DENSE_ANGLES` indexing from
  `experiments/069-.../design_geometry.py` (`DENSE_CENTER=39.0`,
  `DENSE_STEP=0.2`): index 0=36.0°, 12=38.4°, 13=38.6°, 14=38.8°, 29=41.8°
  — all four angle citations in the parameter table are correct; no
  indexing bug (a hygiene check none of the five critiques ran, since none
  found a defect to look for here — logged as a clean check, not an
  attack).
- Grepped LOGBOOK.md directly for every occurrence of "disclaimer-erosion"/
  "scope-erosion" to verify VISION's own recurrence count (§5) rather than
  trusting their prose.

No arithmetic or citation defect was found anywhere in the proposal's own
table. Every substantive gap below is a scoping/framing/completeness gap,
not a wrong number.

## 1. PHOTONICS — the 4+ zero-crossing finding

**Independently CONFIRMED, exactly**, per §0. This is the sharpest
finding among the five and is correct as far as it goes. **Refining it
one step further, per §0's own additional check**: the fix needed is
*not* "the floor gate itself needs a broader sweep" (the gate, as
specified, already excludes only the one point it should at
`FLOOR_FRAC=0.10` applied to the full window) — it is that **`ratio_k`
itself has never been measured by real FDTD at 28 of 31 angles**,
including all three of the other node-adjacent ones. A future cycle
could satisfy every letter of this cycle's own floor gate while still
resting a "CONSISTENT, channel-general" claim on a 5-point sample
deliberately clustered around exactly one of (at least) four known
near-zero features. **Adjudication: CONFIRM the arithmetic and the
substantive attack; the proposal's own remedy (PHOTONICS' flip-parameter:
disclose the tighter margins + narrow Q5's language) is necessary but,
per §6.2 below, not by itself sufficient to close the underlying
representativeness gap.**

## 2. MATERIALS — FLOOR is article/wavelength-specific, un-flagged for reuse

**Independently CONFIRMED.** `FLOOR=1.91744×10⁻⁴` is, by construction, the
RMS of `graded_black_shell`'s own `frac_contrast(θ)` curve at 600 nm —
verified from §0's own from-scratch recomputation, which used exactly
this one material's `C40_C`/`delta_scene` fields. The live-risk citation
(exp-087's own Next section queuing a "near-null σ(I) article" extension
under Tier 2) is accurate — I confirmed it by re-reading exp-087's `NOTES.md`
Next section directly, not merely trusting MATERIALS' quote. **Adjudication:
CONFIRM. The proposed Idealization-13 sentence is the right, minimal fix.**

## 3. ELECTROMAGNETISM — bracket width never justified against a physical linewidth

**Independently CONFIRMED.** Full-text search of `phase1_proposal.md`
finds T28's own established `~2.84–2.95°` period cited only as context for
the aliasing-risk log (§ elsewhere in the sub-thread's history) — nowhere
in §4 or §6 of *this* proposal is it invoked to bound what "broader than
0.4°" would mean physically, or to argue the bracket is wide enough to
rule out a genuine, narrower critical-coupling-type resonance on the
absorbed-power channel specifically (a channel EM correctly notes need
not share the ambient-contrast channel's own linewidth). **Adjudication:
CONFIRM. This is a distinct axis from PHOTONICS' attack** — PHOTONICS
concerns *multiplicity* of nodes across the swept window; EM concerns
*width* of feature around the one node actually bracketed. Both are valid
and compound rather than overlap (§7 confirms no conflict between them).

## 4. THERMODYNAMICS — is the P8/NETD skip an R8 violation?

**Ruled: NOT an R8 violation as filed. THERMODYNAMICS' own critique
correctly identifies a real gap but mis-frames its severity; Idealization
9's argument clears a lower bar R8 explicitly leaves open.**

R8's text (LOGBOOK RULED OUT) requires independent verification of an
argument used to justify skipping an affordable check, "before the gap is
filed as non-blocking" — and its escalation clause fires "when the gap
later proves outcome-determining." Two facts distinguish this from R8's
founding instance (exp-075, where an unverified convention argument
gated a REFUTE headline that later flipped):

1. **P8/NETD is not wired into any of this cycle's own scored predictions.**
   Re-reading §6 in full: Q1–Q5 are the entirety of the pre-registered,
   falsifiable predictions; none of them reference `netd_disposition` or
   `dt_ss_full_K`. Idealization 9 states this explicitly ("not load-bearing
   to this cycle's own scored predictions"), and I confirm it by
   construction — there is no downstream verdict for a wrong P8 argument
   to corrupt. R8's firing clause requires the gap to "later prove
   outcome-determining"; there is no outcome here for it to determine.
2. **The argument WAS independently verified — by THERMODYNAMICS' own
   Phase-2 critique, before Phase 3 exists.** Their "Independent
   verification performed" section pulls `experiments/087-.../
   results.json::thermo` directly and confirms the physical premise
   (smooth ~18% variation, `ratio_abs_ext_raw` pinned to
   0.5128–0.5138) — I independently reproduced this exactly in §0. This
   is precisely "actually computing the alternate case," performed by
   the review layer *before* any Phase-3 adoption, matching this
   program's own established **non-firing** pattern (R6/R7/R8/R9/R10's
   own text: caught blind by Phase-2 critics before a defended claim
   reaches Phase 3), not the firing one (a defended, unverified claim
   surviving to Phase 5/LOGBOOK).

**However**, since the check itself costs nothing (`p_abs_w` for both
configs at both new angles is already computed as `frac_p_abs`'s own input;
`mixed_length_scale_regime`→`netd_disposition` are two more calls on
numbers already in hand), there is no reason to leave the *appearance* of
an R8-shaped gap in the record even though it does not meet R8's firing
bar. **Recommend, not mandate on R8 grounds: adopt THERMODYNAMICS' own
flip-parameter (compute P8/NETD at 38.4°/38.8°, report alongside P7) as a
zero-cost precautionary fix — closing the gap outright is cheaper than
continuing to argue about whether it was ever really open.**

## 5. VISION — the disclaimer-erosion finding: 3rd/4th recurrence, and is the fix sufficient?

**Independently CONFIRMED as filed, and treated as the single highest-
stakes item in this audit.** I grepped LOGBOOK.md directly for
"disclaimer-erosion"/"scope-erosion" rather than trusting VISION's own
count: the shape is named three times before this cycle — Iteration 53
(T16, `amp_ratio` normalizer-proximity flagged then never adjudicated),
Iteration 63/exp-086 (VISION's own Phase-5 finding: `NOTES.md`'s Learned
section silently widened a `pair_pad`-only null-calibration finding to an
unqualified "the real oscillation," explicitly logged in LOGBOOK as "the
T16/R9 scope-erosion shape"), and Iteration 64/exp-087 (VISION's own
Phase-5 finding, explicitly logged as "a THIRD instance of the
disclaimer-erosion shape... a fourth instance fires Checkpoint criterion
4 automatically" — LOGBOOK's own pre-committed standing tripwire, not
VISION's invention). Re-reading `phase1_proposal.md`'s own §6 confirms
VISION's factual claim: Idealizations 9 and 10 appear exactly once, in
§5, and Q1/Q4/Q5 each restate the CONSISTENT/ENERGY-DOMINANT/
NODE-UNRESOLVABLE classification language without either disclaimer
riding along. **This is the identical shape, confirmed, and this
document — as currently drafted — is what would become the fourth
instance if it reaches Phase 3/NOTES.md unfixed.**

**Is VISION's fix (carry Idealizations 9/10 inline at every Q1/Q4/Q5
restatement) sufficient?** For *this* instance, yes — it directly closes
the letter of the recurring defect. But three independent occurrences of
the identical shape, each individually caught and individually "fixed"
in its own cycle, is itself evidence that a manual per-cycle copy-paste
discipline is not a stable fix — it has now failed to prevent recurrence
three times running in the same lineage, with this cycle's own first
draft making a fourth attempt at the same mistake before any critique
even touched it. **Going further than VISION's own fix: recommend Phase
3 adopt a structural, not merely textual, remedy** — e.g., require any
future T28 write-up's committed-predictions section to open with a
one-line "carried idealizations" banner naming every corroborative-only
disclaimer (by number) that governs the classification language below it,
so omission becomes a visibly missing banner rather than a silently
dropped clause. This is named here as a strong recommendation for Phase
3 to adopt or explicitly formalize as a new standing rule; it is not
made a blocking condition of this cycle's own PROCEED ruling, since
VISION's narrower fix already discharges the immediate tripwire risk.

## 6. New attacks, not raised by any of the five critiques

### 6.1 — Q5's "replacing exp-087's own filed... headline" language risks contradicting exp-087's own Phase-5 ruling **[inconsistency]**

exp-087's `NOTES.md` (`Learned`, re-read directly, §0 above) states: *"Red
Team's audit explicitly declined to retroactively relabel [the filed
ENERGY-DOMINANT classification] against a gate that did not exist in the
frozen Phase-3 spec, the same house discipline that governs every other
post-hoc-rationalization risk this program guards against."* This
cycle's own Q5 (§6) states: *"...replacing exp-087's own filed
ENERGY-DOMINANT headline with a corrected, gate-respecting CONSISTENT
reading."* "Replacing... headline" is not, on the most careful reading,
actually inconsistent with the prior ruling — a fresh, disclosed
document (exp-088) computing a new, forward-citable reading is different
from silently editing exp-087's own committed record — but the word
"replacing" is exactly the kind of loose language a future LOGBOOK/
PLAN.md citation could misread as license to overwrite or supersede
exp-087's own filed classification outright, precisely the risk R9's
whole lineage (T16 in particular — a *labels*, not numbers, version of
the same commensurability problem) exists to prevent. **Recommend,
mandatory**: Phase 3/NOTES.md must state explicitly that exp-087's own
`results.json`/`NOTES.md` remain the unedited historical record of what
the frozen Iteration-64 pipeline computed; exp-088 supplies a separate,
disclosed, R13-corrected reading for forward citation purposes only —
and any future citation of "T28's energy-interception classification"
must specify which of the two it means.

### 6.2 — The un-sampled node census is a genuine, quantified board item, not just a language-narrowing fix **[unfalsifiable-adjacent]**

Extending PHOTONICS' own finding (§1): of the four known `delta_scene`
zero-crossings in the swept window, only one (38.590°) has ever had
`ratio_k` measured near it by real FDTD, across this channel's entire
5-point history (36.0°, 38.4°, 38.6°, 38.8°, 41.8°). The other three
(≈37.13°, ≈40.27°, ≈41.46°) have *never* been FDTD-sampled for
`frac_p_abs` at all — only their desk-computable `frac_contrast` values
are known, which is necessary but not sufficient to say anything about
`ratio_k` there. A "CONSISTENT" verdict resting on this sample is
therefore a claim about behavior *near one specific node*, not a
claim about the channel's behavior near near-zero-crossing regions in
general — and nothing in this cycle's own predictions (Q1–Q5) currently
distinguishes those two claims for a future reader. This is not quite
"unfalsifiable" in the classical sense (every Q1–Q5 prediction here is
individually falsifiable) but the *broader* claim implicit in Q5's own
framing ("the first fully R13-compliant classification... across the
node's immediate neighborhood") is not actually testable by this cycle's
own 8 calls — it asserts more generality than the data can support,
functionally unfalsifiable at the scope claimed even though every
individual number behind it is sound. **Recommend, mandatory**: name a
concrete forward-tripwire queue item (Tier 1 or 2) for a future T28
cycle — measure `ratio_k` by real FDTD at the three other node-adjacent
angles (≈37.1°/37.2°, 40.2°, 41.4°) — before any LOGBOOK/PLAN.md entry
asserts the energy-interception channel is CONSISTENT in a
channel-general, not merely point-sampled, sense.

### 6.3 — Hygiene checks that came back clean (logged for completeness, R4 discipline)

`dg069.DENSE_ANGLES` indexing (§0) and the 8-call cost accounting
(2 configs × 2 angles × 2 legs = 8, matching §2's table exactly) both
independently re-verify with no defect. Idealization 7 (settling not
independently re-checked at the two new angles) is adequately disclosed
and low-risk given the ±0.2°/±0.4° proximity to exp-087's own G40/38.6°
spot-check (`rel_dev(sigma_abs)=7.9×10⁻⁵`) — flagged as a plausible
Phase-2 candidate by the proposal itself, correctly not elevated to
mandatory by any of the five critiques or by this audit.

## 7. Do any two critiques conflict?

**No.** All five are unanimous support-with-changes, zero opposition, and
attack five genuinely disjoint axes: PHOTONICS (multiplicity of
near-node features across the window), MATERIALS (portability of the
FLOOR constant across articles/wavelengths), ELECTROMAGNETISM (width of
the tested feature around the one node bracketed), THERMODYNAMICS
(completeness of the corroborative NETD check), VISION (disclaimer
carry-forward discipline). None restates a claim another critique makes,
and none of their independently-recomputed numbers disagree with each
other or with §0's own from-scratch recomputation.

## 8. Checkpoint criterion 4 — explicit ruling

**Does not currently fire** — nothing in this cycle has yet reached a
defended, Phase-3-adopted state; every gap identified above (by the five
critiques and by this audit) was caught blind, at Phase 2, before any
Phase-3 synthesis exists — this program's own established non-firing
shape.

**At material, immediate risk of firing automatically if Phase 3 fails to
adopt Fix 1 (§5) specifically.** This is not a discretionary judgment
call for the Director to weigh — Iteration 64's own close pre-committed,
in writing, that "a fourth instance fires Checkpoint criterion 4
automatically" of the disclaimer-erosion shape, and this cycle's own
first draft already exhibits the identical shape a fourth time. Adopting
Fix 1 (carry Idealizations 9/10 inline at every Q1/Q4/Q5 restatement,
before Phase 3 is treated as frozen) is the only action that keeps this
criterion from firing on this cycle; every other fix in this docket is
important but not itself Checkpoint-4-adjacent under any currently-filed
standing rule.

No other Checkpoint criterion (1/2/3/5) is implicated: this is T28
instrument work (criterion 2 explicitly N/A, matching every T28 desk/
instrument cycle since exp-069); no constraint metric is passed or
approached (criterion 1 N/A); no engine-physics build is needed
(criterion 3 N/A); this is not a non-advancing cycle in the criterion-5
sense — it is a cheap, decisive, well-targeted follow-up to a cycle that
itself discharged a live forward tripwire.

## 9. Ruling: PROCEED-WITH-MANDATORY-FIXES

Fix docket for Phase 3 to adopt or explicitly override with reasons
(10 items; items 1–6 are blocking, 7–8 are recommended zero-cost
closures, 9 is blocking, 10 is optional):

1. **[BLOCKING]** Carry Idealization 9 (NETD disclaimer) and Idealization
   10 ("does not test constraint 3 — only its energy-ledger bookkeeping")
   verbatim, inline, at every restatement of the P7/Q1/Q4/Q5
   classification language in Phase 3's synthesis and the eventual
   `NOTES.md` — including this proposal's own §6 before it is treated as
   frozen. (VISION's own fix, §5.) Failure here is the specific,
   pre-committed condition under which Checkpoint criterion 4 fires
   automatically (§8).
2. **[Recommended, forward standing-practice]** Beyond item 1: adopt a
   structural "carried idealizations" banner convention for any future
   T28 committed-predictions section, so a dropped disclaimer becomes a
   visibly missing banner rather than a silent omission (§5).
3. **[BLOCKING]** Narrow Q5's "first fully R13-compliant classification...
   across the node's immediate neighborhood" to explicit scoping: "at the
   5 sampled angles only." Disclose, alongside §4's margin table, that
   θ≈40.2°/41.4° clear the same floor by only 1.31×–1.48× (tighter than
   the two angles actually bracketed) against the same 4-zero-crossing
   structure (PHOTONICS' fix, §1).
4. **[BLOCKING]** Name a concrete forward-tripwire queue item: measure
   `ratio_k` at the three other node-adjacent established-grid angles
   (≈37.1°/37.2°, 40.2°, 41.4°) before any future LOGBOOK/PLAN.md entry
   describes the energy-interception channel as CONSISTENT in a
   channel-general sense (§6.2).
5. **[BLOCKING]** Add one sentence bounding the bracketing test's claim:
   it rules out only a feature ≳0.4° wide, citing T28's own established
   ~2.84–2.95° periodicity as the physical basis for that bound; strike
   "decisive" from the §1 framing (EM's fix, §3).
6. **[BLOCKING]** Add Idealization 13: *"FLOOR and RMS are specific to
   `graded_black_shell`/600 nm and must be independently recomputed, not
   reused numerically, for any other absorber article or wavelength this
   gate is later applied to"* (MATERIALS' fix, §2).
7. **[Recommended, zero marginal cost]** Compute
   `mixed_length_scale_regime`→`netd_disposition` at θ=38.4°/38.8° (both
   configs) in Phase 4, reusing the already-computed `p_abs_w` values;
   report alongside P7 in `results.json` (THERMODYNAMICS' fix, §4 — not
   mandated on R8 grounds, recommended because it is free).
8. **[Recommended, zero marginal cost]** Extend the `ratio_abs_ext`-vs-T9
   (0.51) cross-check to the two new angles from the same
   `widths_by_cell` data (THERMODYNAMICS' secondary finding).
9. **[BLOCKING]** State explicitly that exp-087's own `results.json`/
   `NOTES.md` remain the unedited historical record of the frozen
   Iteration-64 pipeline's output; exp-088's Q1 "CONSISTENT" reading is a
   separate, disclosed, R13-corrected reading for forward citation only —
   not a retroactive edit — and any future citation must specify which
   (§6.1).
10. **[Optional, minor]** One-line gloss on `NODE-UNRESOLVABLE`/
    "R13-compliant" language: clarify it refers to denominator-
    resolvability of one internal ratio, not a scene-visibility verdict
    (VISION's secondary finding).

Zero items are overridden. Nothing in this docket requires new `lab/`
machinery or changes the frozen 8-call FDTD budget.

## 10. Summary

**Ruling: PROCEED-WITH-MANDATORY-FIXES.** All five blind Phase-2 critiques
are substantively correct on their sharpest attacks (four independently
CONFIRMED as filed; THERMODYNAMICS' R8 framing is confirmed as a real,
worth-closing gap but ruled not an actual R8 violation, since nothing in
this cycle's own scored predictions depends on the skipped check and the
critique itself already performed the independent verification R8
requires). No two critiques conflict. One materially new finding beyond
the five (§6.1): the "replacing... headline" language in Q5 risks a
future citation conflating exp-087's own frozen record with exp-088's
forward-superseding reading — the same class of risk R9's lineage exists
to prevent, applied here to a classification label rather than a numeric
ratio. A second (§6.2): PHOTONICS' own zero-crossing finding, extended
one step, shows the real gap is sampling completeness (only 1 of 4 known
near-zero features has ever had `ratio_k` measured near it), not a
miscalibrated floor threshold — the floor gate itself needs no change,
but Q5's implicit channel-general framing does, and a concrete
forward-tripwire measurement item should be named.

**Checkpoint criterion 4 is not currently firing but is at material,
immediate, pre-committed risk of firing automatically** if Phase 3 does
not adopt fix docket item 1 — carrying Idealizations 9/10 inline at every
restatement of the classification language this cycle computes. That is
the single highest-priority item in this docket; every other item
matters but none carries an automatic-fire consequence under any
currently-filed standing rule.
