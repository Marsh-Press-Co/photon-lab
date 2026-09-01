# Panel Iteration 76 — Phase 2 RED TEAM Audit

*Speaks last, sees everything: Phase-1 proposal (THERMODYNAMICS, rotation
lead) + all five blind Phase-2 critiques (PHOTONICS, MATERIALS,
ELECTROMAGNETISM, QUANTUM OPTICS, VISION SCIENCE). Standard: not
textbook-physics compliance — speculation is permitted. Kills internal
inconsistency, unfalsifiable claims, mechanisms that cannot be expressed as
simulation parameters, and quiet constraint violations (especially #3, N/A
this cycle per Idealization 7). Every load-bearing claim below re-verified
against source this session — nothing taken on the critiques' word, and one
new defect (Attack 4) found independently, missed by all five blind seats.*

## 0. Source-of-truth confirmations (before any attack)

- **Null C θ₀, byte-exact**: `experiments/090-.../results.json::
  q8.crossings_deg[3] = 41.46090139413461` (re-read directly this session).
  The proposal's line 56 cites `41.460901139413461` — an extra "1" inserted
  after the sixth decimal digit. **VISION's finding confirmed exactly.**
- **The four "filed, reused" Null C `delta_scene` values** (proposal §2 item
  1 table) reproduce exactly from `experiments/098-.../results.json::
  item_i.C.report`: `{40.960901: +2.4718686763873787e-3, 41.294201:
  +1.5126843736852358e-3, 41.627601: +5.854146369200786e-4, 41.960901:
  +4.704113885973804e-4}`. Interval slopes: `Δ₁=−9.591843×10⁻⁴,
  Δ₂=−9.272697×10⁻⁴, Δ₃=−1.150032×10⁻⁴`, `r₂=0.9672`, `r₃=0.12402`
  (8.063× drop) — matches the proposal's cited `r₃=0.1240`/`~8.06×` and
  PHOTONICS'/QUANTUM's independent recomputations, to the digits stated.
- **But the two INTERIOR angle labels attached to those values are wrong —
  a new, previously-uncaught defect, found independently this session (none
  of the five blind critiques caught it — see Attack 4).** `results.json`'s
  actual keys are `41.294201`/`41.627601`; the proposal's table (and its own
  downstream new-bracket arithmetic) states `41.294235`/`41.627568`.
  Traced to source: `experiments/098-.../run.py:416` builds Null C's test
  angles as `THETA0_C - 0.1667`/`THETA0_C + 0.1667` — a **literal 4-decimal
  constant**, not `1/6` exact. `41.46090139413461 − 0.1667 = 41.29420139…`
  (rounds to the true stored key, `41.294201`); `41.46090139413461 − 1/6 =
  41.29423473…` (rounds to the proposal's `41.294235`) — confirmed by direct
  computation (`abs(0.1667 − 1/6) = 3.333×10⁻⁵`, exactly the observed gap).
  The proposal recomputed the angle labels from the exact quartile fraction
  instead of reading the actual stored/run angle — the associated
  `delta_scene` VALUES are correct (they are the true 0.1667-offset points'
  values), only the LABEL is wrong.
- **Null B Richardson figures** (`shift_20_30=−0.1935812645°`,
  `shift_30_40=−0.1503190219°`, `observed_ratio=0.7765163757`,
  `naive_order2_ratio=0.5625`) reproduce exactly from `experiments/098-.../
  results.json::richardson_diagnostic.B`, matching the proposal and every
  critique that cited them.
- **exp-095's R5 spend, confirmed zero**: `experiments/095-.../
  results.json`: `rank2_calls=0`, `proceed_gate=False`,
  `rank2={"skipped": true, "reason": "Rank 1 combined go/no-go gate did not
  PROCEED"}`. The proposal's and MATERIALS'/PHOTONICS' citations are exact.
- **QUANTUM's fault-injection-coverage claim, confirmed at source.**
  `experiments/097-.../run.py:290-308`: `pc`/`fia`/`fib`/`fic`/`fid` all
  call `run_checks_1234_and_7("R4", 39.2, 40, "C40_R4", ...)` — hardcoded
  `family="R4"`. `run_fi_e()` (line 206-219) uses `family="R4"`; `run_fi_f()`
  (222-233) uses `REPRESENTATIVE[0]`, which is `family="R4"`
  (`experiments/096-.../run.py:85`); `run_fi_h()` (253-265) mislabels an R3
  point as `"R4"`. **Zero fault-injection scenario, anywhere in this
  program's history, has ever run with `family="R5"`.** The two R5 points in
  `REPRESENTATIVE` (`experiments/096-.../run.py:91-92`,
  `41.825°`/`41.850°`) are scored only via the plain
  `run_checks_1234_and_7(family, pt["theta"], cpl_intended, config_key)`
  call in `main()`'s representative loop (`experiments/097-.../
  run.py:272-278`) — no fault ever injected on that call. **Confirmed
  exactly.**
- **EM's hard-assert claim, confirmed at source.** `experiments/095-.../
  run.py`: Rank 2a's `assert xi_pass`/`assert nonneg_pass` sit at lines
  774-777; Rank 2b's sit at lines 851-854 (both re-read directly this
  session) — both fire *before* `settle_band`/the sign-check outcome is
  even computed, both un-predicted anywhere in the proposal's §4 table
  (independently re-checked: no row for `xi_ext`/`sigma_abs_nonneg`
  anywhere in §4). `XI_TOL` is confirmed carried unchanged from
  `experiments/093/094-...` (`exp094.XI_TOL`, re-read in `run.py:203`),
  never evaluated against real cpl=50 field data before this cycle.
  **Confirmed exactly.**
- **MATERIALS' R15-addendum citation, confirmed at source.**
  `experiments/095-.../NOTES.md:673-678`: *"Gate 5 has never, at any point
  in this 19-cycle sub-thread's history, independently verified
  geometric/angular registration (`cx`/`cy`/`angle_deg`/source
  placement) — only `sigma_e` magnitude."* Verbatim match. R15's addendum
  text (`LOGBOOK.md`, Iteration 71/exp-094) is independently re-read in
  full above (Required Reading §2) and does require a far-from-null,
  known-correct-sign recovery check before a new resolution family's
  third-point reading is trusted — R5 has never run one.
- **PHOTONICS' established-period claim, confirmed at source, with a
  caveat PHOTONICS' own critique does not fully carry.** `P_EDGE_A =
  2.8421052631578947` is asserted in `experiments/086-.../
  phase4_rescore.py:73`, and `LOGBOOK.md:3989-3990` independently states
  `delta_scene(θ)`'s own directly-fitted free period is `P*=2.9474°`
  (`R²=0.8582`), 3.7% off `P_edge_A`. R13's own founding text
  (`LOGBOOK.md`) gives the range `≈2.84–2.95°`. PHOTONICS' critique cites
  the tighter, single figure `2.8421°`; the more careful figure for
  `delta_scene` specifically is `2.9474°`, i.e., the new bracket's
  half-width (1.500°) is ~51% of the period either way — **the substance
  of the attack is unaffected by which figure in the established range is
  used**, but a Phase 3 write-up citing a period figure should use
  `2.9474°` (delta_scene's own fitted value), not `2.8421°` (a distinct,
  related quantity from a different config comparison), to avoid
  repeating the imprecision here.
- **Item 3's GP2′/exp-086 figures, confirmed exactly.** `results.json::
  item_v.gp2_curve`: peak `235.39611912782016×` at `θ=66.0°`; tail
  (`θ≥74°`, 32 points) minimum `12.22212934970524×` at `θ=89.5°`, zero
  VALID points. `phase4_rescore_results.json::method_c_rescore.sub_results`:
  `θc=69°→ptp=1.6959845846`, ratio-to-`θc=5°`-reference
  `6630.986931×`; `θc=75°→311.10×`; `θc=77°→621.44×`. All exact. **Minor,
  non-load-bearing imprecision**: the proposal's "78.5× (θ=74°)" is
  actually the value at `θ=74.5°` (`78.534×`); `θ=74.0°` itself reads
  `78.283×`, and the tail is not strictly monotonic between those two
  points (a ~0.3% uptick before the decline resumes) — the "monotonic-but-
  slow decline" framing overstates the tail's own smoothness by one data
  point. Immaterial to any classification or verdict.

## Numbered attacks

**1. [R8-class: unverified-robustness-argument-in-lieu-of-an-affordable-check]
Item 2's registration-readback gate has ZERO fault-injection coverage at
cpl=50 — confirmed at source (§0 above), not merely alleged by QUANTUM.**
The implicit argument for treating this as safe — "the checks are generic
in `cpl`, so a defect is unlikely" — is precisely the shape R8 (adopted
Iteration 52, already on the books, does NOT require a fresh founding
instance here) rules insufficient: an affordable named check exists
(re-run FI-A/B/C/D + FI-E/F/H with `family="R5"`, zero marginal FDTD cost,
all pre-`sim.run()`) and was not run. This is R5's first real spend ever —
if this cycle proceeds without it and the gap later proves
outcome-determining, this sub-thread would be shipping the exact
"known, named, ignored" pattern R6–R18's lineage exists to prevent, on a
rule that is not new this cycle. **ADOPT QUANTUM's fix as mandatory,
not merely as a flip-to-support courtesy.**

**2. [R15-addendum violation, rule already on the books] Item 2 spends all
24 new R5 calls inside a ≤0.5°-wide bracket hugging Null B itself, plus one
settling angle at the same location — zero far-from-null R5 points
anywhere, confirmed by direct read of §2 item 2's own angle table (Rank 2a:
39.854853°, inside the bracket; Rank 2b: 39.521519°–40.021519°, the
bracket itself).** R15's addendum (`LOGBOOK.md`, Iteration 71) requires,
**before** a third resolution point adjudicates genuine migration vs.
artifact, that the new family independently reproduce the
already-known-correct sign at a robust, far-from-null angle — because a
uniform-direction reading is indistinguishable from a systematic
registration defect baked into the new family's own construction. This
requirement predates R5's existence by one cycle (R15 addendum: Iteration
71/exp-094; R5 built: Iteration 72/exp-095) and has never once been
discharged for R5, at any angle, in this program's history — this is not
R5's founding-instance grace (R15 was already ratified and citable well
before R5 was ever built), it is a known rule the proposal's own item 2
does not honor. **ADOPT MATERIALS' fix as mandatory.**

**3. [inconsistency / unpriced-outcome] Item 2's own hard `assert`s
(`xi_ext`, `sigma_abs_nonneg`) can HALT Rank 2a or 2b before any
`delta_scene` reading exists, and §4's Predictions table has no row, band,
or lean for either — confirmed at source (§0 above): the asserts fire
literally before `settle_band` is computed.** This is not a hypothetical:
exp-098 (this sub-thread's immediately preceding cycle) crashed mid-run on
an unrelated arithmetic assert and had to re-execute from scratch. A
first-ever-resolution HALT here is a live, foreseeable, zero-cost-to-name
outcome this proposal's own frozen-before-any-run predictions discipline
(PANEL.md Phase 3) is supposed to price. **ADOPT EM's fix as mandatory**
(a predicted row, or at minimum an explicit "HALT is a live, undisclosed
outcome" caveat, before Phase 4 code is frozen).

**Ruling on Attacks 1–3 together — the three-way convergence is real, not
duplicated reasoning, and IS mandatory before Phase 3.** Independently
verified from source that MATERIALS, QUANTUM OPTICS, and ELECTROMAGNETISM
are each attacking a genuinely distinct mechanism, not restating one
finding three ways:
  - MATERIALS: whether the **physics reading itself** can be trusted (a
    ground-truth sign-recovery gap, R15-class).
  - QUANTUM: whether the **construction-time wiring** (Sim parameters:
    `cpl`/`theta`/placement/phase/taper) can be trusted at this resolution
    (a fault-injection-coverage gap, R18/R8-class).
  - ELECTROMAGNETISM: whether the **run itself completes** without an
    unpredicted crash (a runtime energy-bookkeeping assert, unpriced in
    §4).
None of the three critiques cites the other two's specific mechanism; each
is independently traceable to different lines of different files (R15's
own text vs. `run_checks_1234_and_7`'s hardcoded `family="R4"` calls vs.
`cell_metrics_r5`'s inline `assert`s). This is a genuine three-way
convergence on the theme "R5's first real spend rests on unvalidated
machinery," reached by three independent routes — not three seats making
the same unverified assumption. **Ruling: all three fixes are mandatory
before Phase 3 freezes item 2's `run.py`.** Two (Attacks 1–2) are
zero-marginal-FDTD-cost (fault-injection re-scoring, 4 extra `sim.run()`
calls respectively — Attack 2's far-from-null check is the only one that
spends real FDTD, at 4 calls) and can be added to item 2's existing budget
without materially changing its 24/8-call structure; Attack 3 costs
nothing (a documentation/prediction-table addition). None requires
re-scoping the cycle — this is PROCEED-WITH-MANDATORY-FIXES territory, not
RECOMMEND-REDESIGN, matching this sub-thread's own established pattern
when a defect is cheap to close (R16/R17/R18's own founding cycles).

**4. [R4-class: a "not hand-typed"/"reused not rebuilt" figure that does
not reproduce byte-exact from its own cited source — found independently
this session, missed by all five blind critiques] The proposal's Null C
"filed, reused" table mislabels its two interior angles by 3.33×10⁻⁵°,
traced to source in §0 above.** The proposal's own §1/§2 language leans
explicitly on "not hand-typed," "re-read this session, not assumed"
rhetoric to earn trust for its arithmetic (echoing VISION's own
Attack-6-class finding on line 56's θ₀) — and the same document commits
the identical error class one section later, on the very table it
describes as "filed, reused not rebuilt." The `delta_scene` VALUES are
correct (independently confirmed, §0); only the angle LABELS are
recomputed via exact-fraction arithmetic (`θ₀±1/6`) rather than pulled
from the literal 4-decimal offset (`θ₀±0.1667`) `experiments/098-.../
run.py` actually used to generate them. **Load-bearing risk, not merely
cosmetic**: if Phase 4's `run.py` "reuses, not rebuilds" these four points
by looking them up in `experiments/098-.../results.json::item_i.C.report`
using the WRONG hand-typed keys from this proposal's own table
(`"41.294235"`, `"41.627568"`), the lookup will `KeyError` (the true keys
are `"41.294201"`/`"41.627601"`) — a crash risk identical in shape to
exp-098's own arithmetic-assert crash one cycle ago, this time from a
mislabeled dict key rather than a miscounted total. **New mandatory fix,
this seat's own finding** (see §Mandatory Fixes below). Does not affect
the `r_i` ratios or the VANISHING-AMPLITUDE trichotomy itself (those use
only the `delta_scene` values, which are correct) — but does affect
whatever code path performs the "reuse" the proposal's own prose commits
to.

**5. [methodology: established-oscillation-vs-decay conflation, PHOTONICS'
finding] The bare `r_i<0.5`-at-3-points VANISHING-AMPLITUDE criterion
cannot distinguish true decay-to-zero from ordinary curvature approaching a
trough of `delta_scene`'s own established ~2.84–2.95° period — confirmed
at source (§0 above: the period is real, established, on the books; the
new bracket's 1.500° half-width is ~51–53% of it, not comfortably past a
full period).** The pre-registered trichotomy's own third branch
("reverses direction without crossing zero" → INCONCLUSIVE) would catch
this IF the tested span happens to include the reversal — but with a
half-width under one period, there is no guarantee it does, and a
still-decelerating, still-positive, still-monotonic 3-point tail ending
exactly where the proposal's own bracket ends is fully consistent with
"this is the flattening approach to a local trough, not an asymptote."
**ADOPT PHOTONICS' fix as mandatory**: require the tested half-width to
exceed roughly one full established period (`≥~2.84°–2.95°` — use
`2.9474°`, `delta_scene`'s own directly-fitted value, per §0's correction
above, not the more precise-looking but less-directly-applicable
`P_edge_A=2.8421°`) before VANISHING-AMPLITUDE, rather than
INCONCLUSIVE-consistent-with-same-lobe-oscillation, is reported.

**6. [R4-class: byte-exact citation, VISION's finding, confirmed exactly]
θ₀'s cited value has a hand-inserted extra digit** — see §0. Physically
negligible (`2.5×10⁻⁷°`), but the claim of exactness is false as written,
independent of magnitude, matching R4's own standard exactly. **ADOPT.**
Note for Phase 3: given Attack 4's finding that the SAME table's
downstream angle arithmetic already carries a larger, independent
labeling defect (`3.33×10⁻⁵°`, over 100× the θ₀ digit-insertion's own
magnitude), Phase 3 should not treat a spot-fix of line 56 alone as
closing this document's angle-arithmetic risk — both defects should be
corrected together, from source, in the same pass.

**7. [house-discipline: banner-placement regression, VISION's finding,
confirmed] §5's closing banner sentence names §4 ("every prediction in §4
is governed by...") but is not physically duplicated inside §4's own
body** — independently re-read: §4's table has no banner sentence in its
own text. This is the identical gap VISION found and got fixed at
Iteration 75 (exp-098's own Predictions section now carries the banner
duplicated in its own body); this proposal reverts to the pre-fix
pattern. **ADOPT.**

**8. [non-load-bearing, MATERIALS' secondary note] §3's T1 disposition
never uses the words "realizability" or "orthogonal," leaving exp-098's
own queue item 5 (state the cpl-is-orthogonal-to-realizability finding
explicitly) undischarged a second consecutive cycle.** Independently
confirmed: `L_GEOMETRIC_M_R4 == L_GEOMETRIC_M_R5` to `1e-12`
(`experiments/069-.../design_geometry.py`, re-checked this session,
matching exp-098's own Red Team Phase-2 confirmation of the R4/R3/native
identity, extended here to R5), so the underlying finding is true and the
fix is cheap. Not a flip-to-oppose issue by itself (MATERIALS' own
verdict agrees) — but two consecutive misses on the same named, cheap
governance ask is worth a plain instruction, not a repeated pass. Judged
**non-blocking, adopt as a Phase 3 wording addition, not a gate.**

**9. [non-load-bearing, this seat's own check] EM's judgment that the
`ptp`-vs-`ratio_to_ref` commensurability concern (R9-adjacent) is already
adequately disclosed, and EM's decision not to press it as an attack, is
correct — independently re-verified.** Idealization 56 (§5 of the
proposal) states explicitly that `ptp` and `ratio_to_ref` are "not
interchangeable measures of the same underlying phenomenon... a close
numeric match... would be informative but not a proof they measure the
identical thing; a mismatch is equally informative" — this is exactly the
disclosure R9 requires (both operands' incommensurability stated up front,
the comparison scoped to shape/trend rather than asserted numeric
equivalence), not a "confirmed comparison" of the kind R9 was written to
catch. **UPHOLD EM's judgment**; no fix needed here.

## Adopt/Override summary (Director-citable)

| Seat | Headline finding | Ruling |
|---|---|---|
| PHOTONICS | `delta_scene`'s own established ~2.84–2.95° period makes the bare `r_i<0.5` VANISHING-AMPLITUDE criterion unable to rule out ordinary oscillatory curvature | **ADOPT** (Attack 5) — period and half-width ratio confirmed exactly at source; corrected which period figure (`2.9474°`, not `2.8421°`) Phase 3 should actually cite |
| MATERIALS | Item 2 never reproduces the already-known-correct sign at a far-from-null R5 angle, violating R15's addendum (already on the books, not this cycle's founding instance) | **ADOPT** (Attack 2) — confirmed exactly at source, part of the mandatory three-way convergence |
| ELECTROMAGNETISM | Item 2's hard `xi_ext`/`sigma_abs_nonneg` asserts can HALT before `settle_band` even runs, and §4 has no predicted row for this outcome | **ADOPT** (Attack 3) — line numbers and assert placement confirmed exactly, part of the mandatory three-way convergence |
| QUANTUM OPTICS | Item 2's registration-readback gate has zero fault-injection coverage at cpl=50, an R8-class gap | **ADOPT, ESCALATE** (Attack 1) — confirmed exactly at source (every FI scenario hardcoded `family="R4"` or R3-mislabeled), ruled mandatory rather than a flip-to-outright-support courtesy, since R8 is an already-established rule, not a fresh finding this cycle gets founding-instance grace on |
| VISION SCIENCE | θ₀ citation has a hand-inserted digit; §5's banner is not duplicated in §4's own body | **ADOPT both** (Attacks 6–7) — both confirmed exactly; Attack 6 additionally connected to a larger, independently-found sibling defect in the same table (Attack 4) that VISION's own check did not reach |

No critique is overridden this cycle — all five verdicts (unanimous
support-with-changes) survive independent re-verification intact. This
seat adds two findings none of the five blind critiques caught (Attack 4,
load-bearing; the minor tail-monotonicity imprecision in §0, non-blocking)
and one calibration correction to an adopted critique (PHOTONICS' period
figure, Attack 5).

## Overall verdict: **PROCEED-WITH-MANDATORY-FIXES**

Items 1 and 3 are, on their own, disciplined, cheap, well-scoped
house-discipline work; item 2 (the first-ever real R5 FDTD spend) carries
the cycle's only genuinely load-bearing risk — the three-way convergent
validation gap (Attacks 1–3) — but every fix required to close it is
affordable, additive, and does not touch item 2's core design (Null B,
the asymmetric lower-θ-weighted bracket, the corrected Richardson
formula). Nothing here rises to RECOMMEND-REDESIGN: no fix requires
re-scoping which null or which family is targeted, and nothing requires
new, unvalidated machinery — every fix reuses code and figures already on
file. RECOMMEND-DEFER is not warranted either: R5 has sat fully built and
gate-verified but entirely unspent since Iteration 72 (four cycles), and
every fix below is priced at a handful of additional zero-or-low-cost
calls, not a multi-cycle build.

## Mandatory fixes for Phase 3 to adopt

1. **Item 2 — fault-injection ground-truth on the registration gate
   itself (QUANTUM's fix, Attack 1).** Before Rank 2b's 16-call spend
   (gated exactly as Rank 2a already gates on `settle_band`): re-run
   `run_checks_1234_and_7`'s positive-control + FI-A/B/C/D, plus Check 6's
   FI-E/F/H, with `family="R5"` at cpl=50 (zero marginal FDTD cost — all
   pre-`sim.run()`). Report CLEAN/DEFECT-FOUND alongside the existing
   R4-only figures in `results.json`. HALT Rank 2b if any scenario reads
   the wrong outcome (a real defect scored CLEAN, or a clean case scored
   DEFECT-FOUND).

2. **Item 2 — one far-from-null R5 ground-truth sign check (MATERIALS'
   fix, Attack 2).** Add one angle ≥1° from every established cpl=20 null
   (e.g. reuse Rank 1a's own `39.2°`/`39.4°` idiom, R5-scaled) at both legs
   (`C40_R5`/`G40_R5`) and both conditions — 4 additional `sim.run()`
   calls, run and required to reproduce the already-known R4/R3 sign
   BEFORE Rank 2b's interior points or the Richardson figure are reported
   as anything beyond "uninterpretable pending R5 ground-truth check."
   Updates the item-2 budget from 24/8 (PASS/HALT-path) to 28/12.

3. **Item 2 — price the Rank 2a/2b HALT outcome (EM's fix, Attack 3).**
   Add an explicit row (or at minimum a stated caveat) to §4's Predictions
   table for `xi_ext`/`sigma_abs_nonneg` at both Rank 2a and Rank 2b,
   naming HALT as a live, un-priced-until-now outcome, before Phase 4 code
   is frozen.

4. **Item 1 — correct the Null C "filed, reused" table's angle labels
   (this seat's own finding, Attack 4).** Replace `41.294235°`/
   `41.627568°` with the source-exact `41.294201°`/`41.627601°`
   throughout §2 item 1 (both the "filed" table and the derivation text
   that computes them as `θ₀−0.1667°`/`θ₀+0.1667°`). Phase 4's `run.py`
   must pull these four rows directly from `experiments/098-.../
   results.json::item_i.C.report` by the actual stored keys — never by
   hand-typed labels copied from this proposal's own table — and should
   assert the four expected keys are present before proceeding, so a
   mismatch fails loudly rather than silently mis-pairing a value with the
   wrong angle.

5. **Item 1 — widen the VANISHING-AMPLITUDE discharge condition
   (PHOTONICS' fix, Attack 5, with this seat's period-figure correction).**
   VANISHING-AMPLITUDE may be reported only if, in addition to the
   existing criteria (strictly positive, floor-clear, each new `r_i<0.5`),
   the tested half-width from θ₀ reaches at least one full established
   `delta_scene` period — use **2.9474°** (the directly-fitted value for
   `delta_scene` itself, `LOGBOOK.md`, not `P_edge_A=2.8421°`, a related
   but distinct figure). If the pre-registered 3-point extension (to
   42.960901°, half-width 1.500°) satisfies the amplitude criteria but not
   this widened span, report **INCONCLUSIVE-CONSISTENT-WITH-SAME-LOBE-
   OSCILLATION** explicitly (a fourth named outcome, not folded into the
   existing INCONCLUSIVE-AT-THIS-WIDTH bucket, since the diagnosis differs:
   this one has a specific, falsifiable alternative — the established
   period — rather than "neither pattern is clean").

6. **Item 1 — correct θ₀'s citation (VISION's fix, Attack 6, folded into
   the same corrective pass as Fix 4).** Correct line 56's θ₀ to the
   source-exact `41.46090139413461°`, and re-verify — by direct
   recomputation, not by inspection — that the three new-bracket angles
   (`42.294235°`, `42.627568°`, `42.960901°`) were computed from the
   corrected value, not the erroneous one, and are internally consistent
   with whichever offset convention (literal `0.1667`/`0.3333` vs. exact
   `1/6`/`1/3`) Phase 4's actual `run.py` code uses — Attack 4 shows these
   two conventions already disagree at the 3×10⁻⁵° level once in this same
   document; a second, undetected instance in the new-bracket angles
   themselves should be explicitly ruled out, not assumed absent.

7. **§4/§5 — duplicate the idealizations banner (VISION's fix, Attack 7).**
   Add the carried-idealizations banner sentence directly inside §4's own
   body (not only in §5's closing paragraph), matching exp-098's own
   established fix (Phase-5 correction 6, Iteration 75).

Non-blocking, recommended but not gating: state the
cpl-is-orthogonal-to-realizability finding explicitly in §3 using the
words "realizability"/"orthogonal" (MATERIALS' secondary note, Attack 8);
if item 3's Result-section prose describes the 74°–89.5° tail trend,
avoid "monotonic" and note the small non-monotonic uptick at θ=74.5°
relative to θ=74.0° (§0 above).
