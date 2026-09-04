# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 86 (exp-109)

Fresh sub-agent, blind to every other seat's Phase-5 review this cycle. Read
PANEL.md, LOGBOOK.md in full (RULED OUT registry R1–R25, esp. R6, R13, R18,
R24, R25), PLAN.md lines 25–260, the full exp-109 record (`phase1_proposal.md`,
all five Phase-2 critiques including my own `phase2_critique_quantum.md`,
`phase2_redteam_audit.md`, `NOTES.md`, `results.json`, `run_output.txt`), and
the actual patched code (`experiments/108-.../run.py`, `.../analyze.py`,
`experiments/109-.../reclassify_108.py`). My charter this cycle: audit whether
the classification/gate construction is genuinely well-formed and correctly
calibrated (the R6/R13 lineage), and specifically whether my own prior-cycle
Phase-2 finding (the 1.729×/1.010× raw/residual ratio, mandatory fix 3) was
correctly, not just nominally, handled.

---

## 1. Independent re-derivation from primitives

**1.1 The ratio itself — re-derived three separate ways, not trusted from
any document's restatement.**

(a) By re-executing the actual shipped artifact: `python3
experiments/109-.../reclassify_108.py` was re-run live in this review (not
merely read) and reproduces `run_output.txt`/`results.json` exactly —
`raw_over_residual_ratio=1.7287` (r=156), `1.0104` (r=312); `git status
--short` on the experiment directory shows zero diff after the re-run, i.e.
the artifact is genuinely deterministic/idempotent, not merely committed
once and never reproducible.

(b) By a from-scratch, independent re-implementation in `numpy`, bypassing
the codebase's own `classify_item_ii`/`linear_fit_1_over_margin` entirely —
built directly from exp-108's own committed `delta_values` arrays
(`experiments/108-.../results.json`, `tier1.r{r}.item_ii.delta_values`):

| r | raw_std (independent) | residual_std (independent) | r² | ratio | CONFIRM bar (0.5·boxA) |
|---|---|---|---|---|---|
| 156 | 5.008327901×10⁻⁶ | 2.897162807×10⁻⁶ | 0.665374 | **1.728701×** | 1.4845×10⁻⁵ → raw_std clears, True |
| 312 | 2.124085729×10⁻⁶ | 2.102199273×10⁻⁶ | 0.020502 | **1.010411×** | 1.234×10⁻⁵ → raw_std clears, True |

Matches the Phase-1 proposal's, QUANTUM's own Phase-2 critique's, Red Team's
Phase-2 audit's, and `results.json`'s own figures to <1e-6 relative at both
r. **The 1.729×/1.010× ratio is exact, not an artifact of any one seat's
arithmetic — independently confirmed three times over (this review's own
two methods plus the already-cross-checked chain of Phase-1/Phase-2/Red-Team
figures it agrees with).**

(c) By reading the code directly (`experiments/108-.../run.py:187–231`):
`classify_item_ii()`'s patched body computes `ratio = raw_std /
fit["residual_std"]`, includes it in the returned dict as
`raw_over_residual_ratio`, and interpolates it into `stat_source` itself
(`f"...raw/residual ratio this point: {ratio:.3f}x)"`) — confirmed present
in the ACTUAL executed function body, not merely described in NOTES.md
prose.

**1.2 Persistence and narration — both genuinely present, not merely
computed and dropped (my mandatory task this cycle).**

- `results.json["item_ii_reclassified"]["r156"/"r312"]["raw_over_residual_ratio"]`:
  present, `1.72870088212608` / `1.010411218377062` — exact field name my
  own Phase-2 flip condition asked for.
- `stat_source` string (both the live-executed one and the one persisted in
  `results.json`): contains `"raw/residual ratio this point: 1.729x"` /
  `"...1.010x"` verbatim.
- `NOTES.md`'s own Result section, `result_text` field, AND the mandatory-fix
  summary (§3 of the "six mandatory fixes" list): all three narrate the
  ratio, not only the `stat_source` string in isolation — `**Item ii:**
  r=156: ... (stat_used=5.008328e-06, raw/residual ratio=1.729x); r=312: ...
  raw/residual ratio=1.010x)`.
- `analyze.py`'s companion call site (the only other caller of
  `classify_item_ii`) also threads `raw_over_residual_ratio` into its own
  `item_ii` dict — so the field is not orphaned to the reclassification
  script alone.

**Conclusion: my own prior-cycle Phase-2 finding was genuinely, not merely
nominally, discharged.** The ratio is computed once, in the one place that
matters (`classify_item_ii()`'s own executed body), and flows unchanged into
every downstream artifact (`results.json`, `stat_source`, `result_text`,
NOTES.md prose, `analyze.py`'s dict) — this is the correct shape, not the
R24/R21 failure shape (a value computed and left to die in one document
while the executed/frozen artifact never sees it).

**1.3 EM's correction (the two-sided conservative/liberal statement) — also
independently re-verified, since it lives in the same `stat_source` string
my own fix touches.** `stat ≥ boxA` fires REFUTE; since `raw_std ≥
residual_std` always (general OLS-with-intercept fact, re-derived
independently at §1.1(b): the constant model is a feasible point in the
same least-squares search space, so `ss_res(fit) ≤ ss_res(constant) =
ss_tot`, i.e. `r²≥0`, i.e. `residual_std ≤ raw_std` always), substituting
the larger raw statistic can only make `stat≥boxA` easier to satisfy, never
harder — i.e. conservative against a false CONFIRM, liberal/anti-
conservative against a false REFUTE. The shipped `stat_source` string states
exactly this two-sided form (`"...conservative against a false CONFIRM;
liberal/anti-conservative against a false REFUTE..."`), not the Phase-1
proposal's original, false "more conservative in every case" claim. Correct.

**1.4 Mandatory fix 4 (THERMODYNAMICS, the AND-reduction) — mostly
discharged, one small literal gap.** `reclassify_108.py:84–87` computes
`gate_p0_pass`/`repro_pass` as an explicit Python `and` of both r's `pass_`
fields — the reduction rule itself is correct and independently confirmed
`True`/`True` on re-execution. But the mandatory fix's own text asked this
be stated explicitly "in `reclassify_108.py`'s own code AND docstring" —
the code uses a literal `and` (self-evident to a reader, not truly
"undisclosed"), but there is no comment or docstring line at that call site
itself saying "this is the logical AND of both r's `pass_` fields." The
explicit prose statement instead lives in `NOTES.md`'s own Setup section
("Read `gate_p0_pass = ... and ...` (explicit AND, fix 4)"), not in the
script's own code/docstring as literally specified. **Low severity,
non-outcome-reversing** (the reduction is correct and the `and` operator is
unambiguous to any reader) — a minor, cosmetic shortfall against the
mandatory fix's own literal wording, not a substantive gap.

---

## 2. R25 disposition: was Red Team's override of my own critique reasonable?

My own Phase-2 sharpest attack named, but did not make my flip condition,
a deeper question: whether `R2_SMOOTH_THRESHOLD=0.90` — the cutoff that
decides which branch (detrended vs. raw) fires at all — is itself
calibrated for item ii's own question, rather than an unexamined round
number. Red Team's audit explicitly declined to extend this into a
mandatory re-derivation this cycle, for three stated reasons: (a)
non-outcome-reversing at both tested r; (b) out of this cycle's own
disclosed Tier-0-only scope; (c) "already correctly queued" as exp-108's
own Reconciled Iteration-86 queue, Tier 2 item 3.

**Re-checked (a) independently, from primitives.** True, and more strongly
true than stated: at r=156, even the LARGER of the two candidate statistics
(`raw_std=5.008e-6`) clears the CONFIRM bar (`1.4845e-5`) with a 2.96×
margin; at r=312 both statistics are within 1% of each other and both clear
their bar comfortably. Sweeping the threshold across any value in
`[0, 1.0)` cannot change either verdict — `r²=0.6654` (r=156) would need a
threshold `≤0.6654` to flip that branch, and even then the resulting
`residual_std=2.897e-6` still clears CONFIRM by 5.1×. **(a) holds and is not
overstated.**

**(b) is a reasonable scope discipline** — re-deriving a shared threshold
mid-cycle in a document whose own §5 explicitly rejects "manufacturing a
third rule the fix never specified" as overreach would have been
inconsistent with the same document's own stated restraint elsewhere.

**(c) is the one that does not fully survive contact with `NOTES.md`'s own
text — a real, newly-discovered gap, structurally the R25 failure shape,
though not a literal R25 firing.** R25's own standard: a deferred
item "must be added as its own explicit, numbered line item in that
audit's own Reconciled Iteration-N+1 queue — never left only as a
parenthetical aside inside a different numbered item's prose, or folded
into a... line about a textually-adjacent but distinct action." Checked
directly against `NOTES.md`'s own "Next" section, Tier 2 (the section a
future cycle is entitled to read literally, per R25's own text):

> "...formalize the absolute-floor six-margin family from a
> resolution/aliasing bound, **now including** a re-derivation of
> `R2_SMOOTH_THRESHOLD=0.90` for item ii's own question specifically
> (QUANTUM's named-but-not-mandatory concern this cycle,
> Red-Team-deferred here, not dropped)."

This program's own Tier convention (visible throughout `PLAN.md`'s
Iteration-84/85 queue text) treats each semicolon-delimited clause within a
Tier as one discrete, trackable item. Tier 2 here still contains exactly
**three** semicolon-delimited items — the r=624 point, the fabrication-
tolerance framing, and "formalize the absolute-floor six-margin family from
a resolution/aliasing bound." The `R2_SMOOTH_THRESHOLD` re-derivation was
**not** given its own semicolon-delimited slot; it is grafted onto the third
item via a comma ("now including..."), as a parenthetical qualifier on a
**textually-adjacent but genuinely distinct action**: "formalize the
absolute floor from a resolution/aliasing bound" is a bottom-up physical
derivation of what the floor *should* be, and does not entail, and could
easily be completed without ever producing, a re-calibrated value for the
specific `R²` cutoff `classify_item_ii()` uses to decide detrended-vs-raw.
A future cycle inheriting this queue "as literally written" (R25's own
entitlement) could discharge the six-margin-family item in full while never
separately touching the threshold — reproducing exactly the mechanism R25
was written to prevent, one level tighter than R25's founding case (there
the drop crossed a cycle boundary; here the same document that names the
override is the one that mis-files its own follow-up).

**Not a literal R25 firing** — R25's own text is scoped to "a code-level
fix," and a threshold re-calibration is a calibration/statistics task, not
a code fix; also this is the founding instance of this specific concern
(exp-108's own Phase-5 QUANTUM review, re-read this cycle, applied the 0.90
bar faithfully without ever questioning its calibration — the calibration
question itself is new to exp-109, not a second silent drop of an
already-once-dropped item). **But the shape and the risk are the same
family as R25's**, and Red Team's own reason (c) for the override rests on
a queuing claim that is not, on inspection, accurate to the letter its own
citation (R25) sets. `NOTES.md`'s own Idealizations section states this is
"correctly queued as Tier 2 item 3, not dropped" — true that it is not
*silently* dropped (it is named, in prose, with attribution), but not true
that it received its own line item as R25's own standard requires.

**Recommendation, forward (not blocking this cycle, since (a)/(b) hold and
nothing here is outcome-reversing):** the next cycle to touch Tier 2 should
split "formalize the absolute-floor six-margin family from a
resolution/aliasing bound" and "re-derive `R2_SMOOTH_THRESHOLD=0.90` for
item ii's own question" into two separate, independently-checkable queue
items before either is worked, so neither can be silently satisfied by
completing only the other.

---

## 3. A second, smaller newly-discovered defect: a broken internal
cross-reference in `NOTES.md`

`NOTES.md`'s own "Phase 1 → Phase 2 → Phase 3" section (mandatory fix 1,
line 62) states the PHOTONICS+Red-Team correction of the misdescribed
`classify_item_i` analogy is "**Corrected below (§ "Why raw std, not forced
AMBIGUOUS")**." No section with that title, or any title resembling it,
exists anywhere in the frozen `NOTES.md` (checked via a full heading grep:
`Hypothesis`, `Setup`, `Predictions`, `Idealizations`, `T1 escape-route`,
`Result`, `Same-shift note`, `Combined Verdict`, `Next` — eighteen headings
total, none matching). The corrected reasoning itself IS genuinely present
— compactly in the mandatory-fix-1 paragraph itself (lines 56–67) and in
full in `classify_item_ii()`'s own docstring (quoted verbatim in `NOTES.md`
§Setup) — so **mandatory fix 1's substance is discharged**; only the
self-reference is broken. Low severity, non-outcome-reversing, but exactly
the kind of "claimed pointer must survive contact with the document's own
actual structure" gap this program's own R4/R9/R18 lineage exists to catch
one level removed from a numeric figure. Worth a same-shift correction
(delete or retarget the dangling `§` reference) the next time this document
is touched; does not by itself warrant reopening Phase 3.

---

## 4. Incidental observation (outside this seat's charter, flagged not
pursued)

`git status --short lab/` currently shows `M lab/validation/v1_regression.png`
— a tracked binary regenerated (mtime after `NOTES.md`'s own freeze) but not
committed, in a document whose own Result section asserts "zero `lab/` diff
(`git diff --stat lab/` empty)." Most likely a benign trust-suite plotting
byproduct (visual/metadata non-determinism on re-run, not a code change) and
not attributable with confidence to this cycle's own actions from the
evidence available to this review — noted for completeness, not asserted as
a defect of exp-109, and outside my charter's substantive scope (T1 is
correctly N/A throughout this cycle; nothing here touches a
mechanism/absorption parameter).

---

## 5. Verdict

**CONFIRM-WITH-GAPS.**

The core, substantive question this cycle exists to answer — did my own
prior-cycle mandatory fix (persist and narrate the 1.729×/1.010× raw/
residual ratio) get wired into the executed path, not merely computed once
and dropped — is **independently re-derived and CONFIRMED, exactly, three
separate ways** (live re-execution, from-scratch re-implementation, direct
source read). EM's two-sided conservative/liberal correction is likewise
independently re-verified correct. The R24 second-instance fix itself
(`classify_item_ii()` now genuinely gated on `fit["smooth"]`) is real,
executed, and reproduces exactly at both r — CONFIRM/CONFIRM, non-
outcome-reversing, as predicted.

Red Team's own override of my sharpest Phase-2 attack (declining to make
`R2_SMOOTH_THRESHOLD=0.90`'s re-derivation mandatory this cycle) is
**substantively reasonable** — reasons (a) and (b) hold up under
independent re-derivation — but its **third stated ground, that the
concern was "already correctly queued," does not fully survive a literal
check against `NOTES.md`'s own Tier 2 text against R25's own "own explicit
line item" standard**: the threshold re-derivation is folded as a
subordinate clause into a different, textually-adjacent Tier-2 item rather
than given its own line, the precise shape R25 exists to forbid, though not
a literal R25 firing (founding instance of this specific concern; scoped to
a calibration task, not "a code-level fix"). A second, independent, minor
defect (a dangling `§` cross-reference in `NOTES.md`) is newly found and
disclosed here; mandatory fix 1's substance is unaffected by it.

**Most important finding:** the 1.729×/1.010× ratio my own prior-cycle
critique demanded is genuinely persisted and narrated, not merely computed
and dropped — but the override that declined to escalate my *deeper*
concern (the uncalibrated `R2_SMOOTH_THRESHOLD=0.90` itself) rests partly
on a "correctly queued" claim that, checked literally against R25's own
line-item standard, is not quite true: the re-derivation is named in
`NOTES.md`'s Tier 2 prose but not given its own queue line, leaving real
risk that a future cycle discharges the item it's folded into without ever
touching the threshold itself.
