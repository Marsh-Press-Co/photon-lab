# Phase 2 — Red Team Audit (exp-097, Panel Iteration 74)

*Seat charter (PANEL.md, verbatim): attacks every proposal, speaks last and
hardest; standard is not textbook-physics compliance — speculation is
permitted; kills internal inconsistency, unfalsifiable claims, mechanisms
that cannot be expressed as simulation parameters, and proposals that
quietly violate a target constraint, especially #3. Never leads a cycle, has
no proposal of its own to protect. This cycle is zero-FDTD, zero-mechanism
code-verification work — no constraint-#N is in play (T1 route N/A,
`REALIZABILITY_MEMO.md` untouched, confirmed directly from `phase1_
proposal.md` §4). Standard applied instead, per this cycle's own brief:
internal consistency, unfalsifiable claims, and R4/R9/R18-house-discipline
compliance — whether a claimed "bit-exact," "independently verified," or
"matches" statement actually survives contact with source, and whether a
check's claimed coverage matches its actual code.*

Read in full, this session: PANEL.md, LOGBOOK.md (RULED OUT R1–R18 verbatim,
the T28 sub-thread Iterations 70–73), `experiments/096-t28-r4-registration-
readback-gate/NOTES.md`, `run.py`, `phase5_redteam_audit.md`,
`experiments/069-t21-block-mini-period-match-power-up/design_geometry.py`,
`lab/fdtd2d.py` (`add_line_source`, lines ~132–186), `experiments/097-.../
phase1_proposal.md`, and all five blind Phase-2 critiques
(photonics/em/thermodynamics/quantum/vision). Every factual/numeric claim
below — the proposal's own and all five critiques' own — was independently
re-derived from primary source this session, not taken on any document's
word.

## 1. Independent re-verification of the two convergent findings (EM +
## THERMODYNAMICS: the `y_hi`/`BASE_NY` desk-check defect)

**Confirmed, independently re-derived, bit-exact to both critiques.**
`design_geometry.py`'s own comments: `R3_BASE_NY = round(1584*1.5) = 2376`,
`R3_BASE_ABSORB = round(40*1.5) = 60`; `r3_config()`'s actual formula gives
`y_hi = ny − y_lo = 2376 − 60 = 2316`. The proposal's §2b desk pre-check
computes `y_hi=2316` (correct arithmetic) and then states it "matches...
`R3_BASE_NY` comments (450/60/**2376**) bit-exact" — comparing a computed
`2316` against a cited `2376`. These are not the same number and not the
same quantity: `NY` is the domain height, `y_hi` is the source's upper
placement edge, offset from `NY` by `y_lo`. Identical error for R5:
computed `y_hi=3860` vs. cited `R5_BASE_NY=3960`. Both critiques' claims
reproduce exactly.

**Extending both critiques' own scope check — this claim appears TWICE, not
once.** Both EM and THERMODYNAMICS locate the defect in §2b only. Re-reading
§0 (the "Standing-rule compliance header," the document's own
self-certification of R4/R9 compliance — the section a reviewer scans first
to confirm house-discipline adherence) independently found the identical
claim stated a second time, as an even more compressed, higher-confidence
assertion: *"The R3/R5 hand-arithmetic given in §3 below was independently
spot-checked against `design_geometry.py`'s own comments this session
(bit-exact)."* This is the SAME false comparison, asserted in the position
specifically designed to reassure a reviewer that R4 discipline was
followed — a more dangerous location for an unverified "bit-exact" claim to
sit uncorrected than the detailed §2b working-out underneath it, since a
reviewer who trusts the compliance header and skips §2b's arithmetic would
carry the false confidence forward unchallenged.

**Downstream-risk assessment (the specific question this audit's own brief
asked): is it really non-load-bearing, or could it mislead Phase 5?**
Non-load-bearing to Phase 4 execution — independently confirmed: the actual
Python in §2b (`assert (src_x, y_lo, y_hi) == (target["src_x"],
target["y_lo"], target["y_hi"])`) compares against `target = dg.R3_CONFIGS
["C40_R3"]` directly, i.e. the real, correct `y_hi` field (2316), never
against `R3_BASE_NY`. The eventual `run.py` will assert correctly regardless
of the prose. **But it is not risk-free for the reasons EM/THERMO both
stop short of naming: this is a Phase 1 document, and R4 discipline's own
text (LOGBOOK.md R4) governs "any falsifier or self-consistency figure cited
as 'precisely recomputed'" wherever it is COMMITTED, not only in `run.py`.**
If this exact sentence — "matches... bit-exact" against the wrong
constant — survives unedited into Phase 3's NOTES.md (a real risk: Phase 3
synthesis in this program's own established practice frequently carries
Phase-1 prose forward near-verbatim, see exp-096's own Setup section, which
is substantially exp-096 Phase 1's own text), it becomes a frozen,
committed, false "bit-exact" claim in the permanent record — a fresh R4
instance, not a hypothetical one, and one a future cycle citing this
document's own desk-check would inherit uncorrected, exactly the failure
shape R4's own second and third addenda (exp-073, exp-074) already named
twice. **This is why the fix must land in Phase 3's NOTES.md text directly,
not merely be noted as "cosmetic" and left for a future editor to remember.**

## 2. Independent verification of QUANTUM, PHOTONICS, and VISION's findings

**QUANTUM (FI-G R3/R5 scope gap).** Independently confirmed. §2b/§3: FI-G
corrupts `native_src_x=301` and checks the result ONLY against
`R4_CONFIGS["C40_R4"]` (`ratio=2.0` unchanged) — no `R3`(`ratio=1.5`)/
`R5`(`ratio=2.5`) leg of this same negative control exists anywhere in the
proposal. Re-read Idealizations 40–44 in full: Idealization 43 covers
FI-D/E/F/G generically ("single-point... one family, one axis... not an
exhaustive census") and names FI-D's own `R4`-only scope explicitly, but
never names FI-G's identical scope limit by name the way it names FI-D's —
an asymmetric disclosure, confirmed. §1's own claim ("every new check or fix
ships with its own fault-injection scenario this same cycle, per R18's own
text") is accurate for Check 5's pre-existing `R4` leg (which now gets
FI-G) but not for the two genuinely NEW `R3`/`R5` legs item 3 itself adds —
those ship with zero fault-injection control of their own this cycle,
inheriting the trust FI-G earns for a different leg. This is exactly R18's
own text ("a check joining an already-partially-fault-injection-verified
layered-check architecture... must receive its own fault-injection...
control in the SAME cycle it is added") applied to Check 5's own two new
sub-legs, not merely disclosure debt. **Confirmed real, ADOPT.**

**PHOTONICS (standing-items-line silent drop).** Independently confirmed by
direct grep of the full proposal text for "grazing," "wavelength-
generality," and "x-wall": zero hits, all three, reproduced above (§0 of
this audit). Cross-checked against `experiments/096-.../NOTES.md`'s own
"Standing, unranked, carried forward unchanged" line (present, naming both
items, 9 and 21 consecutive cycles respectively) and `phase5_redteam_
audit.md` §6's closing paragraph (present, same two items, 20 cycles).
exp-097's own §9 ("What this cycle does NOT do") restates only the Tier-1
FDTD-spend items (6–9), never the standing/unranked items. **Confirmed: the
first drop of this line in the entire cited span, inside a cycle whose own
mandate is auditing claimed-vs-actual coverage. Real, ADOPT.**

**VISION (banner-verification-mechanism gap).** Independently re-grepped
LOGBOOK.md's Iteration 65 CHECKPOINT text: *"the 'carried idealizations'
banner is now required at BOTH the Predictions section AND the Result
section of any future T28 committed-predictions document."* Matches the
proposal's §6 quotation verbatim. Independently spot-checked `experiments/
095-.../NOTES.md` and `experiments/096-.../NOTES.md`: both carry the banner
sentence at Idealizations (immediately pre-Predictions) and at Predictions,
neither carries it inside a section actually titled "Result" — confirmed,
the drift VISION names is real. The proposal's §6 ruling is textually
correct (independently confirmed against the ratified text) but is,
as VISION states, a stated intention with zero attached verification step —
§5 items and §9's scope boundary name no Phase-3/Phase-5 check that will
confirm the eventual NOTES.md's Result section actually carries the
sentence. **Confirmed real, ADOPT** — and note the irony VISION's own attack
names correctly: this is the SAME failure shape (a claimed compliance
target with no independent confirmation mechanism) the rest of this cycle
exists to eliminate from the CODE layer, recurring, undisclosed as such, in
this cycle's own DOCUMENTATION-layer fix.

## 3. Sixth defect — independently found, none of the five blind critiques
## caught it: Check 6's new `cpl_intended` half is tautological at the
## per-point level and cannot catch the fault class it is built to catch

**The defect.** `check6_positional_and_cpl`'s `cpl_ok` sub-check:

```python
cpl_frozen, cpl_line = NOTES_MD_FROZEN_CPL_BY_FAMILY[pt["family"]]
cpl_ok = (CPL[pt["family"]] == cpl_frozen)
```

Both operands are looked up by the SAME key: `pt["family"]` — a hand-typed
string literal, set once per entry in exp-096 `run.py`'s `REPRESENTATIVE`
list (e.g. `dict(family="R4", theta=exp095.RANK1A_ANGLES[0], notes_line=437,
...)`), independently re-read this session, character by character, from
`experiments/096-.../run.py` lines 84–93. `CPL["R4"]` is a fixed,
family-level module constant (`design_geometry.py`'s own `R4_CPL[600]=40`,
verified this session); `NOTES_MD_FROZEN_CPL_BY_FAMILY["R4"]=(40, 291)` is
likewise fixed and family-level, never per-point. **For any representative
point whose `family` field reads `"R4"`, `cpl_ok` evaluates `CPL["R4"] ==
NOTES_MD_FROZEN_CPL_BY_FAMILY["R4"][0]`, i.e. `40 == 40` — a comparison
between two GLOBAL constants that is true or false identically for all
points sharing that family label, independent of which specific `theta`/
`notes_line` the point actually carries.** This is not a per-point
verification at all, despite being executed once per representative point
in a loop; it is one family-level tautology (given the current, undisputed
values of `CPL` and `NOTES_MD_FROZEN_CPL_BY_FAMILY`, `cpl_ok` is
unconditionally `True` for every point in the entire representative set,
by construction, before any actual per-point data is consulted).

**Why this matters — the exact fault class it is meant to catch, and cannot.**
The stated purpose of this half of Check 6 (Idealization 40, this document's
own text) is closing the "documented-vs-actual scope gap" QUANTUM's own
exp-096 Phase-5 review named: a point's `family` assignment, as hand-typed
into `REPRESENTATIVE`, silently diverging from what NOTES.md's prose says
that point's Rank/line should carry — precisely a **family-mislabeling
transcription slip**, the exact failure class this program has an existing,
named precedent for: exp-096's own **FI-A is literally titled "family/`cpl`
swap"** and demonstrates the program already treats this as a real, live
threat model on the CONSTRUCTION side. If a representative point were
mislabeled — e.g. `family="R4"` typed where NOTES.md's line 511 text names
`R3`/`cpl=30` (the actual line-511 point today, correctly, IS `family="R3"`
— this is a structural argument about the check's discriminating power, not
a claim that today's data is wrong) — every downstream consequence of that
mislabeling (which `PAIR_KEYS[family]` selects the configs, what
`cpl_intended = CPL[family]` resolves to, what `construct_sim` builds) is
consistently derived from the SAME wrong `family` string. `cpl_ok`, keyed
by that identical string on both sides, reads CLEAN. So do Checks 1–4,
for the identical reason R18's own founding finding names for Check
4/FI-A: **"both sides of the comparison are functions of the same wrong
input and agree by construction."** No check anywhere in the seven-check,
now-21-construction architecture is keyed to an INDEPENDENT ground truth for
`family` itself (only `theta`, via the new positional `theta_ok`, achieves
this — it is looked up by `notes_line`, not by `family`, so it stays
genuinely independent). A family-mislabeling defect — the single most
plausible real-world instance of "documented scope diverges from actual
code," the exact class R18 exists to police, and the class this specific
item (Check 6, "the single most load-bearing fix in the docket" per
exp-096's own NOTES.md) is supposed to be the load-bearing defense
against — passes through the entire extended gate undetected.

**FI-F does not validate this axis.** FI-F corrupts the GLOBAL `CPL["R4"]`
dict value itself (`CPL["R4"]` set to 30), leaving every point's `family`
field untouched — a real, different, narrower fault mode (a
`design_geometry.py`-level constant edit) that the current `cpl_ok` design
does correctly catch. It supplies zero evidence about the per-point
family-mislabeling axis, because it never varies `pt["family"]` relative to
its own `notes_line`. The predicted-outcomes table (§5) accordingly never
poses a family-mislabel scenario at all — the coverage gap is invisible not
just in the code but in the document's own falsifiable-predictions table.

**The fix (cheap, zero-`Sim`, same shape as the theta half's own already-correct
design).** Re-key the ground truth by `notes_line` (independent of
`pt["family"]`), not by `family` itself:

```python
NOTES_MD_FROZEN_FAMILY_BY_LINE = {437: "R4", 445: "R4", 476: "R5",
                                   495: "R4", 511: "R3"}
family_ok = (pt["family"] == NOTES_MD_FROZEN_FAMILY_BY_LINE[pt["notes_line"]])
```

...combined with `cpl_ok` re-expressed as `CPL[pt["family"]] ==
NOTES_MD_FROZEN_CPL_BY_FAMILY[NOTES_MD_FROZEN_FAMILY_BY_LINE[pt["notes_line"]]][0]`
(or, more simply, `family_ok` alone already closes the gap, since a correct
`family_ok` plus the existing family-level `cpl_ok` together are no longer
both keyed by the untrusted field). This needs its own fault-injection
scenario distinct from FI-F: a genuine family mislabel (e.g., temporarily
score representative point 6 — the true `R3`/38.4°/line-511 point — with
`family` overridden to `"R4"`) and confirm the fixed check now reports
DEFECT-FOUND where the current design would read CLEAN. Zero new `Sim`
constructions, identical cost class to FI-E/F/G.

**Not yet a Checkpoint-criterion-4 matter.** This is caught here, at Phase 2,
before Phase 3 freeze and before any code is committed — earlier than every
prior R16/R17/R18 founding-instance catch (all caught blind at Phase 5).
Named, tagged, and put in the mandatory-fix docket below; does not rise to
"known, named, ignored," and no new standing rule is proposed for it — it is
a fresh instance of R18's own already-adopted discipline, not a new failure
shape.

## 4. Numbered, tagged attack list

1. **[inconsistency]** §0 and §2b both assert the R3/R5 desk pre-check
   "matches... bit-exact" against `R{n}_BASE_NY` (2376/3960); the true
   comparison target is `y_hi` (2316/3860), a different quantity offset by
   `y_lo`. Non-load-bearing to the actual `assert` code (which correctly
   targets `target["y_hi"]`), but stated TWICE, including in the document's
   own self-certifying compliance header, and must not be carried forward
   into Phase 3's NOTES.md unedited (§1 above).
2. **[incomplete-coverage]** The standing-items ledger line (grazing-
   incidence, 9 cycles; x-wall wavelength-generality, 21 cycles) — present
   in every T28 document since Iteration 64 — is silently absent from §9,
   the first such drop in that span, inside a cycle whose own mandate is
   "claimed coverage vs. actual coverage."
3. **[R18-violation]** Check 5's two genuinely new `R3`/`R5` legs (item 3's
   own extension) ship without their own fault-injection control this
   cycle; FI-G exercises only the pre-existing `R4` leg. §1's claim of
   complete R18 compliance overstates what is actually verified for these
   two legs.
4. **[unfalsifiable]** §6's governance ruling on the carried-idealizations-
   banner rule is textually correct but attaches no verification mechanism
   — a bare stated intention for Phase 3's eventual NOTES.md, in a program
   with two consecutive good-faith failures (exp-095, exp-096) to satisfy
   this exact rule despite believing, in real time, that they had.
5. **[R18-violation]** Check 6's new `cpl_intended` half (`cpl_ok`) is
   keyed on both sides by the same, hand-typed, unverified `pt["family"]`
   field, making it a family-level tautology rather than a per-point check
   — it cannot catch a family-mislabeling transcription slip, the single
   most plausible real-world defect this item exists to close, and the
   exact class exp-096's own FI-A already names as a live threat model on
   the construction side. FI-F validates a different, narrower fault mode
   (global `CPL` dict corruption) only. New finding, independently found
   this session, not raised by any of the five blind critiques.
6. **[incomplete-coverage]** A direct consequence of #5: §5's own
   predicted-outcomes table never poses a family-mislabel fault-injection
   scenario, so the gap is invisible in the document's falsifiable
   predictions, not only in the check's code.

## 5. Verdict and itemized fix docket

**PROCEED-WITH-MANDATORY-FIXES.** Six items, ruling on all six findings
(five blind critiques + this audit's own #5/#6, which are one underlying
defect with two facets) — **zero overridden, all six ADOPTED.** The
architecture is sound in its central design (positional theta-check,
formula-independent-in-name Check-5 extension, orthogonal-axis Check 7, a
genuine old-vs-new side-by-side comparison for Check 6) and every field-
theory/arithmetic recomputation not flagged above (the phase-ramp formula,
the taper formula, all NOTES.md line transcriptions, the 21-construction
count) independently reproduces exactly. None of the six findings is fatal;
every fix is zero-FDTD, same-shift, cheap.

| # | Finding | Source | Disposition | Required fix before Phase 3 freeze |
|---|---|---|---|---|
| 1 | `y_hi`/`BASE_NY` desk-check mis-citation, appears in §0 AND §2b | EM + THERMODYNAMICS (independently convergent) | **ADOPT** | Correct BOTH §0's compliance-header sentence and §2b's detailed prose to cite the correct comparison target (`R{3,5}_CONFIGS["C40_R{3,5}"]["y_hi"]` = 2316/3860), not `R{n}_BASE_NY`. This correction must land in Phase 3's NOTES.md text itself, not only in a Phase-2 fix note, or it becomes a fresh, committed R4 instance. |
| 2 | Standing-items ledger line (grazing-incidence, x-wall) silently dropped | PHOTONICS | **ADOPT** | Restore the line verbatim to §9, updated to 10/22 consecutive cycles. |
| 3 | Check 5's new `R3`/`R5` legs lack their own fault-injection control; asymmetric disclosure vs. FI-D's explicit scope note | QUANTUM OPTICS | **ADOPT** | Add FI-G legs at `R3` (ratio=1.5) and `R5` (ratio=2.5), same corrupted `native_src_x=301`, scored against `R3_CONFIGS["C40_R3"]`/`R5_CONFIGS["C40_R5"]` — zero new `Sim` constructions, same cost class as the existing FI-G. (Minimum acceptable alternative — an explicit Idealization naming the gap, matching FI-D's own precedent — is available but the actual fix is equally cheap and closes the gap rather than merely disclosing it; given this cycle's own stated purpose, prefer closing it.) |
| 4 | §6 governance ruling has no attached verification mechanism | VISION SCIENCE | **ADOPT** | Add one sentence to §6 or §9: this cycle's own Phase 3 NOTES.md is not complete until a Phase-5 (or this seat's own Phase-2 fix-verification pass) explicitly greps the Result section for the banner sentence and reports pass/fail by name. |
| 5 | Check 6's new `cpl_intended` half is a family-level tautology, keyed by the same untrusted field on both sides — cannot catch a family-mislabeling transcription slip | Red Team (this audit, independently found — no blind critique raised it) | **ADOPT, mandatory, highest priority of the docket** | Re-key `NOTES_MD_FROZEN_CPL_BY_FAMILY` lookups by `notes_line` via a new `NOTES_MD_FROZEN_FAMILY_BY_LINE` map (given in §3 above), add `family_ok` as an explicit third sub-check, and give it its own fault-injection scenario (a genuine family mislabel at one representative point, distinct from FI-F) proving the fixed check now catches what the current design cannot. |
| 6 | §5's predicted-outcomes table has no row exercising a family-mislabel scenario | Red Team (this audit, direct consequence of #5) | **ADOPT** | Add the new fault-injection scenario from item 5 as a table row (predicted DEFECT-FOUND under the fixed `family_ok`, CLEAN under every other check — a specificity claim, matching FI-D's own table shape) before Phase 3 freeze. |

**Reasoning for PROCEED-WITH-MANDATORY-FIXES over REJECT:** every finding
above is a scoping/coverage gap in a NEW check or a documentation citation
error, not a defect in the underlying, already-validated construction code
(`Sim`, `add_line_source`, `design_geometry.py`'s `r{3,4,5}_config()`) or in
Checks 1–4's own already-fault-injection-verified machinery, which this
cycle correctly leaves untouched. All six fixes are expressible as concrete
code/prose changes, all are zero-FDTD, and all are catchable and fixable
same-shift, before any Phase-4 script runs — matching this sub-thread's own
established PROCEED-WITH-MANDATORY-FIXES precedent (exp-093 through
exp-096, each 5–9 items, zero overridden, zero rejects). **Reasoning against
plain PROCEED:** finding #5, if it reached Phase 3 unfixed, would mean this
cycle — whose entire purpose is closing R18-class "claimed coverage exceeds
actual coverage" gaps in its own founding gate — ships a fix for exactly
that class of gap (Check 6's `cpl_intended` half) that itself has the exact
same defect shape, one cycle after R18 was adopted, inside R18's own first
discharge cycle. That is not disqualifying (it is caught here, at Phase 2,
the earliest possible point in the whole framework, well before Phase 3
freeze), but it is not a rubber-stamp PROCEED either — it requires an actual
code change to the check's own logic, not merely a documentation
correction, before Phase 3 can truthfully claim this item closes what
exp-096's Phase-5 audit asked for it to close.

## 6. What survives, unattacked

Independently re-verified and found sound, not merely accepted: the
phase-ramp (`phase_expected`) and raised-cosine taper (`taper_expected`)
formulas are bit-exact reproductions of `lab/fdtd2d.py:172–175` and
`:160–164` respectively; the old-vs-new side-by-side retention of
`check6_set_membership_OLD` (R12's own idiom) is a genuine, executed
comparison, not merely claimed; FI-D, FI-E are correctly designed and their
predicted specificity/catch results are logically sound by direct trace;
the 21-construction accounting (16 + 4 + 1) is arithmetically correct on the
actual-`Sim.__init__`-call basis exp-096's own Phase-5 audit established,
independently re-traced this session; every NOTES.md line citation
(265/291/304/437/445/476/495/511) reproduces exactly against
`experiments/095-.../NOTES.md`'s own text; the 212-word narrative count is
exact (independently recounted programmatically this session); Tier-0/
Tier-1 scope boundary (§9) correctly excludes all real FDTD spend, matching
the reconciled queue's own sequencing rationale.
