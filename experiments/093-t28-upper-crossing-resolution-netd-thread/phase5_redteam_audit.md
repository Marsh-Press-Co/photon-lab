# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 70 · exp-093

*Fresh sub-agent, RED TEAM charter (PANEL.md verbatim): attacks every
proposal, speaks last and hardest. Standard is not textbook-physics
compliance — speculation is permitted. Kills internal inconsistency,
unfalsifiable claims, mechanisms inexpressible as simulation parameters,
and quiet constraint violations, especially #3. Read in full: PANEL.md;
LOGBOOK.md (RULED OUT R1–R15, LIVE THREADS, the Iteration-65 CHECKPOINT
disclaimer-erosion text, and the surrounding Iteration-53/63/64
citations it names); the complete exp-093 record — `phase1_proposal.md`,
all five Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`run.py`, `results.json`, `run_output.txt`, `NOTES.md` **as currently
committed** (post both mid-Phase-5 Director fixes), and all six Phase-5
reviews. No party's word trusted on its own — every disputed figure below
was independently re-pulled from `results.json`/`run.py` primitives in
this session.*

## 0. Scope check

This cycle takes T1 route N/A, makes no phenomenon-mechanism claim, and
does not touch `REALIZABILITY_MEMO.md` — independently re-verified against
LOGBOOK.md's own chronological record (entries run through Iteration 57;
RULED OUT/CHECKPOINT summaries at the top are current through R15/
Iteration 68) and against every T28 sub-thread entry since Iteration 46:
all state T1 route N/A. Checkpoint criterion 2 is correctly N/A. Nothing
in the five items (NETD backfill, sigma check, denser angular sweep,
caution-zone re-fit, dispersion integral) constructs a gain medium, a
non-causal update, or a constraint-3/4 claim of any kind. No hidden
mechanism claim found anywhere in `run.py` or `NOTES.md`.

## 1. Finding 1 (MATERIALS + PHOTONICS convergent) — UPHELD, confirmed independently, not load-bearing, needs a same-shift fix

Re-derived from `run.py` and `results.json` directly, not trusted from
either review:

```python
# run.py:584-585
combined_curve[41.8] = item5_report[41.8]["delta_scene"] if sigma_item1 == SIGMA_NATIVE else item3_report[41.8]["sigma_corrected_delta_scene"]
combined_curve[42.0] = item5_report[42.0]["delta_scene"] if sigma_item1 == SIGMA_NATIVE else item3_report[42.0]["sigma_corrected_delta_scene"]
# run.py:589 (unconditional string, not branch-aware)
print(f"... 41.6/41.8/42.0 are always native sigma_max=0.5 ...")
```

Item 3 fired REFUTE, so `sigma_item1 = SIGMA_R3_CORRECTED = 1/3`.
`results.json::item1.combined_curve_41_6_to_42_0["41.8"] = -8.790556777193981e-05`
— bit-exact to `item3.per_theta["41.8"].sigma_corrected_delta_scene`, not
to `item5.per_theta["41.8"].delta_scene = -1.865e-05` (native). Same for
`42.0`: `-5.8101656300157956e-05` matches the sigma-corrected value, not
native `+8.041787e-05`. `run_output.txt` lines 155–164 print these exact
corrected numbers under the false "always native" caption. **The code's
data selection is correct; the printed label is false for the branch that
actually ran.** Confirmed independently against both reviews — no
discrepancy found in either's arithmetic.

**Scope-checked against the task's own framing**: this field carries no
per-point comparability annotation in `results.json`, so a future cycle
reading `results.json::item1.combined_curve_41_6_to_42_0` alone, without
`run.py`'s source, has no way to know 41.8°/42.0° are corrected-sigma
values while 41.6° is native — exactly the "persisted uncorrected"
concern the task names. **Not load-bearing**: independently re-verified
against `run.py:561–570` (§4 below) that the SINGLE-NULL three-way outcome
reads only `item1_report`'s six interior points, never `combined_curve`.

**Verdict: UPHELD as a real, currently-uncorrected defect. Mandatory
same-shift fix required (see §7, Fix 1) — this is the one finding in this
audit that is NOT yet closed.**

## 2. Finding 2 (MATERIALS + THERMODYNAMICS convergent) — the NOTES.md gap: fix verified adequate, non-firing

Git history confirms the sequence precisely:
`46ff3cc` (16:24:58, MATERIALS review, catches missing Result section) →
`72060ae` (16:25:41, Director adds Result/Learned/Next) → the remaining
four Phase-5 reviews (PHOTONICS 16:25:51 through QUANTUM 16:27:53) run
against a NOTES.md that already carries the fix, and VISION's own review
explicitly notes "superseded by the Director's own mid-Phase-5 fix
(already landed)."

**Is the fix itself adequate?** Read the current NOTES.md in full: it now
has `## Result` (Items 5/5b/3/1/2/4, all five verdicts stated with
figures), `## Learned` (3 items), and `## Next` (3 ranked items, correctly
flagged provisional pending this audit). Cross-checked every headline
figure quoted in the Result section against `results.json` and
`run_output.txt` (§1, §3, §4, §5 below) — all reproduce bit-exact. **The
fix is substantively complete, not a stub.**

**Does it need re-review by the four seats that reviewed the pre-fix
document?** No. PHOTONICS, EM, VISION, and THERMODYNAMICS's own reviews
each independently re-derive every headline figure from `results.json`/
`run_output.txt` primitives directly (not from NOTES.md's prose) — their
verdicts do not rest on NOTES.md's Result section existing, only on the
underlying data, which was unchanged before and after the fix. The one
review that DOES cite NOTES.md prose for a claim it makes (MATERIALS, on
the R15-disclaimer wording) verified that wording against `phase3_
synthesis.md`'s pre-frozen text, `results.json`, and `run_output.txt` —
three surfaces the fix did not touch. No seat's verdict is stale relative
to the current NOTES.md.

**Checkpoint framing**: this is the third occurrence of this exact defect
shape on this sub-thread (exp-080/Iteration-56, exp-091/Iteration-68,
now exp-093), each time caught and fixed same-shift, each time ruled
non-firing. VISION's own review states the expectation explicitly and
correctly. I concur: **non-firing**, matching established precedent
exactly — see §6 for the general Checkpoint-4 reasoning.

## 3. Finding 3 (THERMODYNAMICS' own self-review) — fix independently re-verified bit-exact, adequate, non-firing

Pulled `results.json::item1.per_theta[*].dt_ss_full_K_c/g` and
`netd_classification_c/g` directly and checked every cell in NOTES.md's
added table against it:

| θ | NOTES.md `dt_c` | `results.json` `dt_ss_full_K_c` | match | NOTES.md `dt_g` | `results.json` `dt_ss_full_K_g` | match |
|---|---|---|---|---|---|---|
| 41.750° | 5.2914e-05 | 5.291399241145361e-05 | ✓ | 5.3278e-05 | 5.327789292396884e-05 | ✓ |
| 41.775° | 5.3000e-05 | 5.299953075021056e-05 | ✓ | 5.3346e-05 | 5.334577897819887e-05 | ✓ |
| 41.825° | 5.3169e-05 | 5.316932724560572e-05 | ✓ | 5.3477e-05 | 5.347723456116063e-05 | ✓ |
| 41.850° | 5.3253e-05 | 5.325317441129739e-05 | ✓ | 5.3541e-05 | 5.3540523760758376e-05 | ✓ |
| 41.875° | 5.3336e-05 | 5.333604703066974e-05 | ✓ | 5.3602e-05 | 5.3602005744538606e-05 | ✓ |
| 41.900° | 5.3418e-05 | 5.341774141699699e-05 | ✓ | 5.3662e-05 | 5.366154959672013e-05 | ✓ |

All 12 values bit-exact, all `netd_classification` fields UNDETECTABLE
(also matches). The sequence is monotonically increasing in both `_c` and
`_g` across all six interior points — the "smooth, no swing coincident
with the disputed node" claim is arithmetically correct. §1's own
self-test is genuinely discharged, and correctly rules **no surprise** at
the SINGLE-NULL result's own node.

**One imprecision in the added text, independent finding, non-firing but
worth naming for a future citation.** NOTES.md's added paragraph states
the interior sequence is "fully consistent with the flanking item-5
values (5.5×10⁻⁵ K at 41.8°/42.0°), with no discontinuity." Checking this
literally, in angular order (41.775° → 41.8° → 41.825°): the interior
point at 41.775° reads `5.30e-05`, but 41.8° — which sits between it and
41.825° — reads `5.518e-05` (item 5's native-sigma value, not the
corrected-sigma value the interior sweep uses), before dropping back to
`5.317e-05` at 41.825°. That IS a discontinuity in the raw θ-ordered
sequence, and THERMODYNAMICS' own Phase-5 review already named it
correctly one document earlier: *"the one local bump (41.8°/42.0°...) is
fully explained by the disclosed sigma_max mismatch."* The added NOTES.md
text's "no discontinuity" phrasing reads as stronger than what the
reviewer's own analysis supports — a discontinuity exists and is
explained (not physical), which is a different, weaker claim than "no
discontinuity." This is the same *shape* of comparability imprecision as
Finding 1/Finding 4 (a native/corrected-sigma boundary described more
smoothly than it actually is) — not a new defect, but the identical
hazard resurfacing in the very paragraph written to close a different gap.
**Non-load-bearing** (the self-test's actual claim — no swing in the
corrected-sigma channel itself — is unaffected and correctly discharged);
recommend a one-clause wording fix alongside Fix 1 (§7).

**Checkpoint framing**: self-caught by the lead seat's own mandated
Phase-5 self-review, fixed same-shift, before any external citation and
before this audit — the exact "caught blind, same cycle" pattern R12's
own Iteration-63 precedent ruled non-firing under near-identical
circumstances (a lead-seat gap self-caught and closed with independently
re-verified figures, before LOGBOOK). **Non-firing.** See §6 for why I
weigh this one more carefully than Finding 2 before reaching that
conclusion.

## 4. Finding 4 (EM's own finding) — confirmed correct, NOT load-bearing to SINGLE-NULL, a real disclosed limitation

Read `run.py`'s outcome logic directly (lines ~561–570, independently
re-confirmed, matching QUANTUM's own quotation exactly):

```python
any_confirmed  = any(r["delta_scene"] > 0 and r["floor_pass"] for r in item1_report.values())
all_nonpositive = all(r["delta_scene"] <= 0 for r in item1_report.values())
if any_confirmed:      item1_outcome = "TWO-NODE CONFIRMED"
elif all_nonpositive:  item1_outcome = "SINGLE-NULL"
else:                  item1_outcome = "STILL AMBIGUOUS"
```

`item1_report` is built only from item 1's own six interior FDTD calls
(41.750°–41.900°, all at corrected `σ_max=1/3`). **41.6°/41.8°/42.0° never
enter this function at all** — they exist only in the separately-computed,
non-gating `combined_curve` context dict. SINGLE-NULL is therefore
entirely independent of the native/corrected-sigma mixing Finding 1/4
describe. **Confirmed: not load-bearing to the verdict itself.**

Is it a real limitation for a future cycle? Yes, and EM's own
demonstration is the strongest evidence in the whole record for this:
`item3.per_theta["42.0"]` shows `delta_scene` genuinely flips sign between
native (`+8.04e-5`) and corrected (`-5.81e-5`) `σ_max` — a controlled,
single-variable swap (same empty-scene capture, only the article leg's
`σ_max` differs), not a bookkeeping artifact. Independently re-derived:
`ratio = -5.8101656300157956e-05 / 8.041787461443572e-05 = -0.72250`,
matches `delta_scene_ratio` field exactly. `41.6°` (exp-091's own anchor)
has never been measured at corrected `σ_max=1/3` at all — its
comparability to the now-corrected-sigma interior window is asserted
(Idealization 11), not checked, and the 42.0° result is direct proof that
"asserted" and "checked" can disagree by a full sign in exactly this
window. **Rule: real, disclosed (Idealization 11 exists precisely for
this), non-load-bearing this cycle, and the cheapest possible unclosed
loose end for Iteration 71 (2 FDTD calls: article leg only, empty leg
reusable).**

## 5. Finding 5 (QUANTUM's own finding) — REJECTED as scoped; a footnote worth naming

The task's own scoped test: does the conflated "20–84×" range for item
1's floor-clearing `ratio_k` values appear, uncorrected, in NOTES.md or
`results.json`? Checked both directly:

- `results.json::item1.per_theta`: each θ's own `ratio_k` is stated
  individually (83.89/50.66/29.58/25.11/22.26/20.48) — no aggregated range
  string anywhere in the file.
- `NOTES.md`'s Result section, Item 1 paragraph: *"four
  (41.825°/41.850°/41.875°/41.900°) clear R13's floor gate, all
  classifying ENERGY-DOMINANT (`ratio_k` **20.5–29.6×**)"* — correctly
  scoped to the four floor-clearing points only, matching
  `results.json` exactly (20.477–29.577, rounds to 20.5–29.6).

**Neither document contains the conflated 20–84× framing. Per the task's
own discharge condition ("if this conflation does NOT actually appear in
the committed record... rule it non-firing/moot"): REJECTED as scoped —
non-firing, moot.**

Independently checked one level further, since the task brief's own
"20–84×" language had to originate somewhere: it traces to
`phase5_review_photonics.md`'s own §0 verdict-recap sentence — *"four of
six interior points clear R13's floor gate, all classifying
ENERGY-DOMINANT, `ratio_k` 20.5×–83.9×; all six interior points read
`delta_scene≤0`"* — a genuinely ambiguous parenthetical (83.9× belongs to
41.75°, one of the two floor-**failing**, NODE-UNRESOLVABLE points, not
one of the four ENERGY-DOMINANT ones) that a careless read could conflate
exactly the way QUANTUM's own review flags. **This is not NOTES.md or
results.json**, so it is outside Finding 5's own stated scope and does
not require a fix under this task's own terms — flagged here only because
it is the closest thing in the committed record to the shape QUANTUM
warns against, and PHOTONICS' own independent §0 recomputation table
(lines 11–19 of that document) already correctly separates the two
groups, so the ambiguity is confined to one summary sentence, not a
computational error.

## 6. Checkpoint criteria — explicit ruling, all five

**Criterion 1 (a configuration passes ALL constraint metrics).** N/A —
this cycle takes T1 route N/A and scores no constraint metric.

**Criterion 2 (a proven mechanism-class boundary, gates clean).** N/A,
independently re-verified per §0.

**Criterion 3 (synthesis requires engine physics beyond the validated
bench classes).** N/A — zero `lab/` diff this cycle (`item2_calls=0`,
`item4_calls=0`, both desk-only; all 56 FDTD calls reuse
`experiments/069-.../design_geometry.py` and existing `_run_sim_r3`-family
machinery verbatim, independently confirmed by the "zero new `lab/` diff"
claim in NOTES.md's Setup section, which I did not take on trust — `git
diff --stat` scoped to `lab/` for this cycle's commits shows no `lab/`
changes).

**Criterion 4 (program-integrity drift — unfalsifiable claims, a
constraint quietly dropped, especially #3).** **Does NOT fire.** Worked
through each candidate trigger explicitly, not by inertia:

- *The specific NETD/human-eye disclaimer-erosion shape (Iterations
  53/63/64/65 lineage) — checked directly, does not recur.* VISION's own
  review traced both originally-flagged bare "detectability" occurrences,
  confirmed the inline `(NETD/instrument, not human-eye)` qualifier is
  present at both, confirmed `netd_disclaimer`/`scope_note` are printed
  AND persisted from the same source strings in `run.py` (a structural
  fix, not a manual transcription this time), and confirmed the
  Iteration-68/69-established "third occurrence" tripwire on the
  JSON-not-printed variant passed clean. I independently spot-checked one
  of these myself: `results.json`'s top-level `netd_disclaimer` string is
  byte-identical to `run_output.txt`'s printed line. **No recurrence of
  the named lineage this cycle — the strongest possible outcome, an
  actual structural fix rather than a fourth near-miss.**
- *Is fixing something mid-Phase-5, after Phase-4 results already exist,
  a materially different, less-protected situation than catching
  something at Phase 2 before any run?* I considered this directly rather
  than defaulting to precedent. The distinction that matters is not
  "before vs. after the run" — it is "before vs. after THIS phase's own
  freeze/citation point." R6–R15's own adoption texts uniformly use
  "caught blind, same cycle" (not "same phase," not "before any run") as
  the discharge test, and Iteration 63/R12's own precedent explicitly
  applied non-firing to a defect caught by a Phase-5 review AFTER a Phase-4
  run, closed with independently-verified multi-seed evidence, before
  LOGBOOK — the closest prior case to Findings 2 and 3 in this cycle, and
  it was ruled non-firing on exactly this reasoning. Both of this cycle's
  fixes were made and independently re-verifiable (by me, above) before
  this Red Team final audit — this cycle's own actual freeze/citation
  point — closes. I therefore rule the "mid-Phase-5" timing does NOT by
  itself demote these catches to a less-protected category; what would
  demote them is if either fix reached a future citation unverified,
  which did not happen here (both are independently re-derived bit-exact
  in §2/§3 above, by me, not merely re-asserted).
- *A sharper concern, named but not firing.* Finding 3's own defect —
  a pre-registered falsifiable self-test, computed correctly, silently
  dropped between computation and the written record — is the third
  instance of "a confident claim, unverified in the delivered record"
  found WITHIN THIS SAME DOCUMENT (after items 2 and 4's Phase-2-caught
  defects, both self-identified by THERMODYNAMICS' own Phase-5
  self-review as the same shape). Three instances of an identical failure
  mode inside one cycle, even though each was individually caught before
  it reached LOGBOOK, is a *density* signal the R4-addendum lineage
  treats as significant across cycles (three consecutive cycles,
  Iterations 23/24/25, triggered a rule tightening) — I do not think it
  is dispositive within a single cycle the way it was across three, but
  it is real evidence the lead seat's own Phase-1 draft-to-freeze
  discipline needs a stronger structural check before Phase 4, not only a
  self-review after it. I recommend this as a process item (§8), not a
  firing.
- *Constraint 3 "quietly dropped"?* No — the T1-N/A / criterion-2-N/A
  status is stated loudly, verified twice (proposing seat + Red Team's
  Phase-2 audit) against LOGBOOK's own record every single cycle, and
  VISION's own review raises the 24-cycle streak as an explicit governance
  question for the board, not a hidden fact. Loud, disclosed, and
  independently reverified is the opposite of "quiet."

**Criterion 4: does not fire.**

**Criterion 5 (two consecutive iterations with no logbook-advancing
result).** Does not fire — this cycle produced a real result (SINGLE-NULL,
correctly derived and independently reproduced by four of six seats plus
this audit; item 4's CONFIRM at the corrected length scale, independently
reproduced FOUR times over — Red Team's Phase-2 audit, the Director's own
Phase-3 §0, EM's Phase-5 review, QUANTUM's Phase-5 review, and now this
audit's own spot-check, all bit-exact). Not two consecutive non-advancing
cycles by any reading.

## 7. Mandatory same-shift fixes still needed before this cycle can close

1. **The `run.py`/`results.json` caption defect (Finding 1, §1).**
   Branch-condition the print string at `run.py:589` (mirror the
   "directly comparable"/"NOT directly comparable" phrase two lines later,
   which is already correctly branch-aware), and add an explicit
   per-point `sigma_max`/comparability tag to the persisted
   `combined_curve_41_6_to_42_0` field in `results.json` so a future
   cycle reading the JSON alone cannot inherit the wrong assumption. Zero
   FDTD, string/serialization-only.
2. **NOTES.md's added self-test paragraph, one-clause wording fix
   (§3).** Replace "with no discontinuity at the near-total-null region"
   with wording that matches what THERMODYNAMICS' own Phase-5 review
   already established — a real, explained (sigma_max-driven, not
   physical) discontinuity exists at 41.8°/42.0° in raw θ-order; the
   corrected-sigma interior sequence itself (the actual self-test claim)
   is smooth. Zero FDTD, wording-only.

Both are cheap, disclosed-in-spirit-already, non-outcome-determining
fixes — not blocking findings, but real and currently uncorrected. No
other finding in this audit requires a same-shift fix; Findings 2 and 3
are already adequately fixed and independently re-verified above.

## 8. Combined Verdict

**PARTIAL — the correct call, not a reflexive default.** Reasoning,
stated explicitly:

- **Not RULED OUT**: no mechanism class is foreclosed this cycle (T1 N/A
  throughout — this is instrument work, not a mechanism test).
- **Not PROMISING**: no constraint-metric progress is claimed or scored.
- **Real, useful, gated progress exists**: item 5's NETD backfill closes a
  genuine LOGBOOK-named data gap (Iteration-69's own defect, 14 cells
  now on record); item 4's dispersion-integral REFUTE is now independently
  reproduced FIVE times over at the actually-mandated length scale (Red
  Team Phase-2, Director Phase-3, EM Phase-5, QUANTUM Phase-5, this
  audit), correcting a two-order-of-magnitude overclaim in the pre-freeze
  draft to a one-order-of-magnitude finding — a real, if milder, result;
  item 1's SINGLE-NULL is arithmetically sound, correctly derived under a
  pre-registered rule I independently re-confirmed does not even touch
  the sigma-mixing question (§4), and is the more physically expected
  reading of a near-total-cancellation feature (PHOTONICS' §1, unopposed).
- **Disclosed limits, correctly named, none swept under the rug**: the
  cycle's own Idealization 16 states up front that SINGLE-NULL is
  angular-only, not R15-grade; item 3's own sign-flip is disclosed
  (Idealization 11) and — per Finding 4 — now demonstrated, not merely
  hypothesized, as a real gap at the window's edge; R15's two founding
  discharge conditions remain explicitly open, stated in the same words
  in `results.json`, `run_output.txt`, and NOTES.md (I checked all three
  — identical text).
- **Zero DISPUTE across six independent blind reviews, one small,
  fixable, non-load-bearing defect surviving to this audit (Finding 1),
  everything else independently re-verified and closed.** This is
  exactly the PARTIAL shape this program's own precedent (Iteration 65,
  a structurally similar cluster of small caught gaps around a sound
  headline result) already defines — not weaker (nothing here is wrong or
  unresolved at the level of the actual physics/arithmetic), not stronger
  (no constraint metric moved, no mechanism boundary proven).

## 9. Ranked top-3 candidate directions for Iteration 71

Reconciled across all six seats' own ranked lists — not my own
preference alone. Two genuine convergence clusters emerged independently
across disciplines; a third comes from the single most-repeated board
item plus this cycle's own governance findings.

**Rank 1 — A targeted `cpl=40` spatial-resolution check at
41.75°–41.90° specifically.** Convergent: MATERIALS' Rank 1, PHOTONICS'
Rank 1, and directly motivated by THERMODYNAMICS' own parallel
cross-`cpl` energy-channel question (Rank 3). This is the cheapest,
single most decisive test of whether SINGLE-NULL is a genuine
resolution-stable feature or itself a `cpl=30`-specific artifact —
exactly R15's second remaining discharge condition, targeted at the
feature this cycle's own item 3 already showed to be fragile on a
different axis (~6 FDTD calls, same budget class as this cycle's item 1).

**Rank 2 — Close the sigma_max comparability gap the corrected-sigma
window actually has, at both its edges.** Convergent: EM's Rank 1
(measure 41.6° at corrected `σ_max=1/3` — 2 calls, article leg only), and
QUANTUM's Rank 1 (a native-`σ_max=0.5` cross-check at 2–4 of item 1's own
interior points, e.g. 41.75°/41.825°, testing whether SINGLE-NULL
survives under the SAME sigma convention that located the original
double-crossing), reinforced by PHOTONICS' Rank 2 (map `σ_max` sensitivity
across the broader near-null neighborhood) and QUANTUM's Rank 3 (sample
41.6°–41.75° densely under corrected sigma, the one genuinely unsampled
sub-interval). Combine into one omnibus item, ~8–12 FDTD calls total —
the direct, cheap answer to Finding 4's own open loose end, and the one
test that would let SINGLE-NULL be cited going forward as resolving,
rather than merely bounding-under-one-convention, the original
double-crossing question.

**Rank 3 — R15's first remaining discharge condition: R3-verify
(`cpl=30`) the three still-unmeasured original caution-zone points
(36.0°, 38.4°, 38.8°).** MATERIALS' Rank 2, and — by MATERIALS' own count
— the single most-repeated deferred item on the whole T28 board. I rank
it third, not first, because Rank 1 targets a feature THIS cycle newly
showed to be fragile, while this item extends an already-settled zone
construction to points not currently in dispute; but it is cheap,
well-specified, and closing both R15 conditions together (Ranks 1 and 3)
would let R15 be cited as genuinely closed for the first time since its
own founding.

**Not in my own top 3, but flagged for the Director's attention because
two seats independently raised it from different angles**: MATERIALS'
own closing caution (after five consecutive desk/instrument cycles on
this exact upper-crossing sub-question, do not open a *sixth* narrow
near-null zoom-in regardless of how Ranks 1–2 land — pivot to PHOTONICS'
long-deferred grazing-incidence check or the x-wall wavelength-generality
leg) and VISION's own scoping question (does this 24-cycle-and-counting
T1-N/A streak still connect to constraint-3 at all, or has it become a
self-contained numerical-methods exercise that should be named as such).
Neither is a Checkpoint-4 violation — both are disclosed, not hidden —
but both are legitimate "what should the program actually be spending its
next several cycles on" questions the Director should weigh explicitly
once Ranks 1–2 above close, not decide by momentum.
