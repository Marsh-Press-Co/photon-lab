# Phase 5 Review — QUANTUM OPTICS (blind, independent)

*Panel Iteration 73, exp-096. Charter (verbatim): non-classical absorption,
state-dependent or coherent interactions; mechanisms enter the bench only
as effective classical parameters — σ(I), σ(x,t), dispersive ε(ω), gain —
or Red Team strikes them. T1 route N/A this cycle (pure instrument
validation, matching every T28 desk/instrument cycle since exp-069). This
review is written blind to every other seat's current Phase-5 output. Both
the Iteration-73 idea under test (the registration-readback gate) and its
own Phase-2 critique (the NOTES.md cross-check, Check 6, named by Red Team
"the single most load-bearing fix in this docket") are my own seat's prior
work — reviewed here with no more deference than any other seat's would
get, per this cycle's own explicit charge.*

## Verdict: **CONCUR-WITH-GAP(S)**

The registration-readback gate is real, correctly built, and its headline
CLEAN result is substantively trustworthy — independently re-verified from
raw source in every dimension I checked, including a full re-run that
reproduced `results.json` bit-exact. But two gaps survived every prior
phase's own review, both specifically on the two checks this seat itself
is most responsible for (Check 6, my own Phase-2 fix; the "logically
sufficient" framing of Check 4, which my own Phase-2 critique did not
catch): **Check 6, as actually coded, verifies only the angle component of
each job constant against NOTES.md — never the `cpl`/family pairing it is
documented, in NOTES.md's own Setup section and in Red Team's own
mandatory-fix wording, as checking** (§2); and **Check 4's own "logically
sufficient" claim is empirically falsified by this cycle's own
fault-injection data**, not merely a theoretical risk Red Team's attack #3
already named in the abstract (§3). Neither gap changes the substantive
CLEAN finding — I independently hand-verified every value the gaps leave
formally unchecked, and all are correct — but both are real,
previously-uncaught instances of "the write-up's claimed scope exceeds the
code's actual scope," the exact shape this program's own R4/R9 lineage
exists to police, now found on the fix this program's own Red Team
identified as this docket's most load-bearing.

## 1. Independent re-verification of Check 6's own line-value transcription

The task at hand, stated plainly: does `run.py`'s `NOTES_MD_FROZEN_LINE_
VALUES` dict — a third hand-typed copy of these numbers, after `run.py`'s
own job constants and NOTES.md's own prose — actually match what is
written at those five line numbers in `experiments/095-.../NOTES.md`? I
re-checked every line directly, twice, by two independent methods (a
`Read` of the file at the cited offset, and a fresh `sed -n` extraction in
a separate shell call, cross-compared against each other and against
`run.py`'s own dict):

| Line | `NOTES_MD_FROZEN_LINE_VALUES` (run.py) | Raw NOTES.md text at that line (this review's own extraction) | Match |
|---|---|---|---|
| 437 | `[39.2, 39.4]` | `` `delta_scene(R4, 39.2°) < 0` AND `delta_scene(R4, 39.4°) < 0`, both `` | ✅ |
| 445 | `[38.49, 38.69]` | `` `floor_pass=True` at both 38.49°/38.69° AND `delta_scene(R4)` signs `` | ✅ |
| 476 | `[41.825, 41.850]` | `` `cpl=50` readings at 41.825°/41.850° preserve Rank 2b's own `` | ✅ |
| 495 | `[41.6]` | `` `frac_contrast` ratio (corrected/native) at 41.6°, `cpl=40`, scored with `` | ✅ |
| 511 | `[38.4]` | `**(Rank 4, PRIMARY.)** 38.4° at corrected sigma (1/3), \`cpl=30\`.` | ✅ |

**All five, bit-exact.** No transcription defect exists in the specific
hand-typed dict this task asked me to police. This is a genuinely
independent check, not a restatement of the Director's or Red Team's own
claim: I did not trust `results.json`'s `check6_notes_md_cross_check`
output for this table — I read the raw NOTES.md bytes myself, at both
phases of this review, before looking at what the code concluded.

I also independently re-ran `run.py` in a scratch copy of the repository
state; the regenerated `results.json` is byte-identical to the committed
one except for the `wall_time_s` timing field (confirmed by structural
diff with that one key excluded) — the committed result is not a
hand-edited or stale artifact, it is what the committed code actually
produces.

## 2. Sharpest finding — Check 6, as coded, checks only the angle half of
## what it is documented to check, and nobody caught this across three
## phases

This is the finding I did not expect, and it directly answers this
cycle's own charge ("could `run.py`'s own hand-transcription... have
silently introduced the exact defect class this whole gate exists to
catch?") — not by finding a wrong *number*, but by finding the check
narrower than every governing document says it is.

**What was asked for.** My own Phase-2 critique (`phase2_critique_quantum.
md`) asked: *"assert the `theta_intended`/`cpl_intended` values read from
run.py's job constants equal the values stated in exp-095's own NOTES.md
frozen Predictions section."* Red Team's Phase-2 audit adopted this
verbatim as fix #4: *"assert the `theta_intended`/`cpl_intended` values
pulled from `run.py` job constants equal the values stated in exp-095's
own NOTES.md frozen Predictions section."* NOTES.md's own "Setup" section
(§6, written at Phase 3, part of the frozen pre-run spec) restates the
same scope: *"`theta_intended`/`cpl_intended` (as read from `run.py`'s job
constants) compared against the values frozen in
`experiments/095-.../NOTES.md`'s own Predictions section."* Three
independent statements of the same requirement, all naming **both**
quantities.

**What was built.** `run.py::check6_notes_md_cross_check()` (lines
193–207):

```python
def check6_notes_md_cross_check():
    results = []
    for pt in REPRESENTATIVE:
        line = pt["notes_line"]
        frozen_values = NOTES_MD_FROZEN_LINE_VALUES[line]
        found = any(abs(pt["theta"] - v) < 1e-9 for v in frozen_values)
        results.append(dict(family=pt["family"], theta=pt["theta"], ...,
                             clean=bool(found)))
    return results
```

`cpl_intended` is never read inside this function, and
`NOTES_MD_FROZEN_LINE_VALUES` stores only θ values — `{437: [39.2, 39.4],
445: [38.49, 38.69], 476: [41.825, 41.850], 495: [41.6], 511: [38.4]}`,
never a `cpl`/family entry. The comparison performed is `theta` only.

**This is not a hypothetical gap — the source text it should have checked
against was sitting right there.** Every one of the five cited NOTES.md
lines explicitly states its own `cpl`/family alongside the angle: line 511
reads *"38.4° at corrected sigma (1/3), `cpl=30`"*; line 476 reads
*"`cpl=50` readings at 41.825°/41.850°"*; line 495 reads *"...at 41.6°,
`cpl=40`, scored with..."* — a `cpl_intended` cross-check was fully
computable from the same source text Check 6 already parses for its θ
values, and simply was not implemented, despite being named explicitly in
three separate governing documents.

**Why this survived three phases of review.** NOTES.md's own **Result**
section (written after the run) describes Check 6 accurately and
narrowly: *"every `run.py` job-constant **angle**... matches the value
hand-transcribed from exp-095's own NOTES.md Predictions section"* — note
"angle," not "angle and cpl." This sentence is not wrong, but it silently
narrows the claim made two sections earlier (Setup, §6) without flagging
that a narrowing occurred — the same shape this sub-thread's own R4/R9/R17
lineage exists to catch (a claimed scope that quietly does not match what
was actually verified), just not previously instantiated on a check's own
*coverage*, only on numeric figures and bracket widths. Because the Result
section's own restatement is individually true, and Red Team's own audit
did not re-read the committed `check6_notes_md_cross_check()` source
against its own fix-docket wording line-by-line, the gap passed clean
through Phase 2's fix and Phase 3's synthesis into a Result section
worded precisely enough to avoid contradicting itself, while still never
correcting the Setup section's over-scoped claim.

**Severity, stated precisely.** Non-load-bearing to the CLEAN verdict: I
independently re-checked, by hand, that every representative point's
actual `cpl_intended`/family pairing matches what NOTES.md's own text says
at the same cited line (R4 at 40 for lines 437/445/495; R3 at 30 for line
511, matching "`cpl=30`"; R5 at 50 for line 476, matching "`cpl=50`") —
there is no live defect of this kind in this cycle's own data. But the
*check itself*, as documented, currently cannot catch a family/`cpl`
mislabeling in `run.py`'s `REPRESENTATIVE` list (e.g., an R4 angle
accidentally scored against an R3 config) — and the `REPRESENTATIVE`
list's own `family="R3"/"R4"/"R5"` values are hand-typed literals in
`run.py`, not read from any of exp-095's own job constants, making this
exactly the kind of hand-transcribed field Check 6 was built to police,
left outside its own coverage.

## 3. Second finding — Check 4's "logically sufficient" claim is
## empirically falsified by this cycle's own FI-A data, not merely a
## theoretical risk

Red Team's attack #3 (`phase2_redteam_audit.md` §2) argued, correctly and
in the abstract, that Check 4 (the phase-array comparison, computed using
the *already-verified* `sim.lam` from Check 1 rather than `cpl_intended`
directly) inherits any corruption Check 1 fails to catch — but framed this
as a *source-of-truth-defect* scenario (`dg.R4_CPL[600]` itself wrong,
Check 1 falsely passing). I checked the cycle's own already-collected
fault-injection data directly and found a sharper, unconditional version
of the same fact, true independent of whether Check 1 passes or fails:

**FI-A** (`results.json::fault_injection.FI_A_family_cpl_swap`) —
`cpl_actual=30` injected where `cpl_intended=40`:

```
check1_resolution: False   (correctly caught)
check4_phase_ramp: True    (reports CLEAN — no defect detected)
check4_max_abs_diff: 0.0   (exact agreement)
```

Check 4 recomputes its comparator from `sim.lam` (the *actual*,
here-corrupted value, 30) — the identical value `add_line_source` itself
used to build the real phase array. Both sides of Check 4's comparison are
therefore functions of the same (possibly wrong) `sim.lam`, and agree
*by construction*, regardless of whether that `sim.lam` is correct. This
is not limited to the source-of-truth case Red Team's attack #3 discussed
— it holds for a bare caller-level `cpl` swap too, the simplest possible
defect shape, demonstrated directly by the gate's own mandatory positive-control
data. **Check 4, as designed, can only ever independently corroborate the
*angle* encoding of the phase array — it structurally cannot
independently corroborate the *resolution* encoding, in any scenario,**
contradicting Phase 1 §2a's claim (carried unchanged into NOTES.md's Setup)
that Check 4 alone is "logically sufficient to catch anything checks 1–3
catch."

**This directly contradicts this cycle's own frozen Prediction, and the
Result section quietly does not say so.** NOTES.md's Predictions section
states: *"FI-A by Check 1, transitively Check 4."* The actual data shows
Check 4 did **not** catch FI-A (`check4_phase_ramp=True`). The Result
section's own restatement — *"FI-A (family/`cpl` swap) caught by Check 1
as predicted"* — is true as far as it goes, but silently drops the
"transitively, Check 4" half of the same pre-registered sentence rather
than flagging that half as falsified. This is a small, non-load-bearing
instance of the identical shape as §2 above: a frozen claim narrower, on
reread, than what was actually predicted, corrected by omission rather
than by disclosure.

**Severity.** Zero practical consequence for this cycle's own CLEAN
verdict — Check 1 alone is a bit-exact, essentially unfalsifiable
comparison (`sim.lam` is a direct `float()` cast with no arithmetic
between assignment and read) and fully carries the resolution axis on its
own; the four-to-six-check architecture's redundancy claim is weaker than
advertised, not its correctness. Worth a one-line correction if NOTES.md
is ever revised, and worth naming for any future cycle that reuses this
gate's own "layered check" idiom and assumes Check 4 gives resolution
redundancy it does not.

## 4. Independent re-verification of the surrounding claims

Beyond §§1–3, I independently re-derived, from raw source, everything else
this cycle leans on:

- **Check 5's arithmetic.** Read `design_geometry.py` directly:
  `R4_BASE_SRC_X = round(300 × 2.0) = 600`, `R4_BASE_ABSORB = round(40 ×
  2.0) = 80`, `R4_BASE_NY = round(1584 × 2.0) = 3168`, and `r4_config`'s
  own `y_hi = ny − y_lo = 3088`. All four bit-exact against
  `check5_recipe_spot_check`'s own `_recomputed` fields and against
  `R4_CONFIGS["C40_R4"]`'s stored values. The "native" constants
  (300/40/1584) `run.py` hand-types for this check are themselves correct
  against the actual `R4_BASE_*` derivation, not merely internally
  self-consistent.
- **Attack #1's C/G-pair table.** Independently loaded `design_geometry.py`
  and printed `R4_CONFIGS["C40_R4"]`/`["G40_R4"]` directly: `nx`
  720/880, `ny` 3168/3328, `src_x` 600/680, `y_lo` 80/160, `y_hi`
  3088/3168, `A` 1504/1504 — bit-exact match to the Red Team table, and
  independent confirmation that fix #1's 8→16 expansion was a genuine,
  warranted correction, not overcaution.
- **Fix #1's actual implementation.** Confirmed `results.json`'s 16
  `representative_results` entries genuinely alternate `C40_R{n}`/
  `G40_R{n}` for all 8 points, all `clean=True` — the fix was implemented,
  not merely documented.
- **The desk bound.** Independently recomputed the three migration
  figures from `experiments/090/results.json::q8.crossings_deg` and
  `experiments/092/results.json::rank1.crossing_report` — `0.1936°`,
  `0.3202°`, `0.3768°`, matching `desk_bound`'s own filed figures to the
  digit; the containment-ratio table reproduces on recomputation.
- **Fault injection, otherwise.** FI-B (`check4_max_abs_diff=1.6355`) and
  FI-C (`298.6310`) both independently reproduce from the stated formula
  and both correctly trigger `clean=False`; the sign-flip magnitude being
  ~180× the angle-swap magnitude is consistent with a full-array
  negation vs. a modest angle shift, as claimed.

No other defect found. The R17 boundary-drawing question (whether
`atol=1e-9` should have been R17-governed) is correctly reasoned in the
audit and I have nothing to add — it is a floating-point-noise tolerance,
not a physical bracket.

## 5. Does this change my own exp-095 assessment of the "2:1 to 3:1,
## impressionistic" balance?

**Yes, modestly, in the direction NOTES.md itself states — and my
findings in §§2–3 do not undercut that, once accounted for.** My own
exp-095 Phase-5 review argued the registration-vs-migration question was
genuinely open and that Rank 1c's own ±0.1° bracket was too narrow to be
informative either way. This cycle removes one of Red Team's own two named
candidates (caller-level wiring/transcription defect) at every point
actually checked — and, per §§1 and 4 above, the checks that matter most
for my own seat's angle (the angle-registration axis itself, Checks 2/4,
and the NOTES.md-transcription axis, Check 6's angle half) are genuinely
clean, independently re-verified by me from raw source, not merely
inherited from the write-up's own say-so. The two gaps I found (§2: Check
6's undocumented narrowing to angle-only; §3: Check 4's non-independence
on the resolution axis) are real but do not reopen either of Red Team's
two named candidates — I hand-verified the specific values both gaps
leave formally unchecked and found no defect in them. Net effect: the
"2:1 to 3:1, impressionistic" reading should move modestly further toward
migration — call it "3:1, still impressionistic, still not a computed
posterior" — bounded from moving further still by Idealization 17/38/39's
own honestly-stated residual: Check 5's recipe-internal spot-check covers
only `R4`/`C40`, one point of three families, so a defect specific to the
`R3` or `R5` recipe branches, or to the `G` (padded) recipe branch's own
placement arithmetic beyond what Checks 3/4 already cover, remains
genuinely untested by this cycle.

## Ranked candidate directions for Iteration 74

**1 (highest value — the actual physics test this cycle's own CLEAN result
now licenses).** Run the reconciled node-bracketing re-run at θ₀≈38.590° in
the `R4` family, using the desk-bound-informed window (≥0.5° single-sided
half-width, or the already-committed asymmetric 0.3°–0.7° design) that
exp-095's queue and this cycle's own item 2 both converge on. With
registration credibly cleared, this is now the direct test of whether the
node genuinely migrates — the question this whole two-cycle detour exists
to eventually answer.

**2.** EM's own queue item 3 — bracket the other three established
`cpl=20` nulls (37.1°/40.2°/41.4°-family crossings) at `cpl=40`, ~24 calls.
The decisive discriminator between "the `R4` family migrates its nodes
uniformly, feature-independent" and "38.590° behaves differently from the
sub-thread's other established crossings" — currently indistinguishable
from a single tested node.

**3 (cheap, code-only, closes this review's own two findings before either
is cited forward as a completed check).** (a) Implement the `cpl_intended`
half of Check 6 that NOTES.md's own Setup section already claims exists —
a same-shape addition to `NOTES_MD_FROZEN_LINE_VALUES`/
`check6_notes_md_cross_check()`, near-zero cost; (b) extend Check 5's
recipe-internal spot-check from `R4`/`C40` to at least one point each in
`R3` and `R5` (Idealization 39's own named-but-undischarged gap) — the
minimum needed before this cycle's "one spot-check against the shared
recipe" claim can honestly be read as covering all three families rather
than one.

Also still open, standing, unaffected by this review: the x-wall
wavelength-generality leg (now twenty-one consecutive cycles deferred);
PHOTONICS' own grazing-incidence validity check; the unbiased
margin-vs-distance rebuild; the ritualization governance question
(Iteration 61).
