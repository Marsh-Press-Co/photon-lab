# VISION SCIENCE — Phase 5 Review of exp-063 (Panel Iteration 40)

*Fresh sub-agent, blind to the other six seats' current-cycle Phase-5
reviews. Charter: human perceptual limits — contrast thresholds, luminance
edge detection, spectral sensitivity, adaptation, temporal (flicker/motion)
sensitivity, saccadic and attentional blindness. Central question: what
would make a human eye FAIL to register something physically present?
Standing duty this cycle: verify the two new `exp063-*` registry entries
live, check `phase4_results.md` directly (not just `NOTES.md`) for the
mandatory NETD/human-eye disclaimer at its own restated TD-3/4/5 verdicts,
and check the document's summary/"bottom line" language for constraint-3
conflation risk given how comfortably this cycle's own numbers came in.*

**Read in full**: `PANEL.md` (charter, Checkpoint criteria, metrics table);
`LOGBOOK.md` in full, ~12907 lines — the R1–R5 ruled-out registry, the
complete T1–T26 live-thread record (T22/T23's Biot-number/lumped-
capacitance lineage read closely, given this cycle's own continuation
claim), every prior Checkpoint-4 firing (Iterations 17, 20, 24, 36, 37, 38,
and both Iteration-39 firings) read in full, not summarized; `PLAN.md`'s
Current-state section, both Iteration-39 CHECKPOINT blocks in full; this
cycle's complete record (`phase1_proposal.md`, all five
`phase2_critique_*.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `phase4_results.md`); `lab/thermo_sidecar.py`,
`lab/caveat_lint.py`/`lab/caveat_lint_config.json`,
`lab/numeric_lint.py`/`lab/numeric_lint_config.json` (full source, and both
tools **executed live**, not trusted from the record's own claims — see
Section 1); `lab/validation/run_all.py` stage 23 (**executed live**, see
Section 1).

---

## 1. Mandatory duty — live tool verification, not taken on the record's word

### 1.1 Both linters and the trust-suite stage: run myself, exit clean

```
$ python3 lab/caveat_lint.py
...
8 caveat(s) checked, 0 required-site failure(s).
EXIT=0

$ python3 lab/numeric_lint.py
...
3 entry(ies) checked -- all PASS.
EXIT=0

$ python3 lab/validation/run_all.py --only 23
  [PASS] correction_factor(k_solid=1e30) == 1 (k_solid->infinity limit)
  [PASS] CF(kappa=2.0 W/mK, L=bench=2.34um) vs exp-063 Phase-1 script output
  [PASS] CF(kappa=2.0 W/mK, L=MP5-730x=1051.2um) vs exp-063 Phase-1 script output
  [PASS] kappa_critical (CF(MP5-730x)==1.35 bisection) vs exp-063 Phase-1 Section 4
4/4 checks passed
```

Both new registry entries — `exp063-biot-correction-machinery` and
`exp063-thermo-disposition-netd-disclaimer` — PASS their `required_sites`
live: `NOTES.md` and `phase4_results.md` for the former, `NOTES.md` for the
latter. `phase3_synthesis.md`'s own claim ("Both re-run and confirmed
clean before this cycle closes") is verified correct, not merely asserted.
The `exp063-cf-bench-vs-witness-derivation` `numeric_lint` entry also PASSes
against its own registered site. No defect in what was checked.

### 1.2 Does `phase4_results.md` itself carry the disclaimer at its own restated TD-3/4/5 verdicts? Yes, at each section — but not at the document's two most quotable claim points

Direct grep confirms the disclaimer text ("NETD is an instrument
threshold... bears on no human-eye/constraint-3 verdict") appears
immediately above each of TD-3, TD-4, and TD-5's own `**Result:**` line in
`phase4_results.md` — the mandatory-fix docket's own "at TD-3/4/5's own
table rows/claim points" requirement is met at the section level, in both
`NOTES.md` and `phase4_results.md`, independently confirmed by both my own
read and the live tool run above. This is a real, correctly-applied fix,
not a partial one.

**But I find one gap, live, not hypothetical: the Summary table (lines
196–204) and the "Bottom line" paragraph immediately below it (lines
206–220) — the two places in this document a future reader is most likely
to skim, quote, or paste into LOGBOOK.md — carry the disclaimer NOWHERE.**
I read both sections end to end specifically hunting for it: zero
occurrence of "NETD," "human-eye," "constraint-3," or any paraphrase in
either the table or its prose summary. This is exactly the pattern class
Red Team's own attack 1 named as this cycle's own aggravating risk factor
("it matters more this cycle than any prior one... exactly the framing
under which an excited... write-up... is likeliest to conflate DETECTABLE
with eye-visible") — now recurring one section later than where the
mandatory-fix docket looked. The Summary table is a NEW claim point this
cycle's own docket did not name (it named "TD-3/TD-4/TD-5's own table
rows," meaning `NOTES.md`'s predictions table and the per-prediction
`phase4_results.md` sections) — not an already-registered site failing to
propagate.

**Does this cross into actual conflation, per the task's own sharpest
question?** No — checked directly, not assumed. I grepped the Summary
table and Bottom line for "eye," "visible," "silhouette," "perceiv,"
"Weber," "scotopic," "photopic," "witness" (beyond the established
"witness-*scale*" geometry idiom this program has used since exp-061 to
mean a physical length, never a perceptual claim), and "flicker": zero
hits beyond the geometry idiom. The language stays generic
("classification," "margin," "UNDETECTABLE... territory") — narrower than
a genuine human-eye conflation, but also narrower than the disclosure
standard this program set for itself one section earlier in the SAME
document. **Recommendation, not a Checkpoint-firing finding (see §3
below): add the disclaimer sentence once, inline, at the Summary table's
own header or the Bottom line's opening sentence** — cheap, mechanical,
and closes the gap between what the per-section fix achieved and what the
mandatory-fix docket's own stated purpose ("at the point of the claim")
actually required of the document's most-quotable location.

---

## 2. A second, independent finding: the new `numeric_lint` entry's own `site` field never reaches `phase4_results.md` — the identical gap-shape to both Iteration-39 firings, not yet exploited

Read `lab/numeric_lint_config.json` directly:

```
"id": "exp063-cf-bench-vs-witness-derivation",
"site": "experiments/063-cnt-forest-thermal-conductivity-biot-check/NOTES.md",
"window_patterns": ["^\\| \\*\\*TD-3\\*\\*", "^\\| \\*\\*TD-5\\*\\*"],
...
```

This entry checks exactly ONE file — `NOTES.md`, the pre-freeze document —
for the bench-vs-witness derivation-consistency pattern it was built to
guard. `phase4_results.md` now exists (written this same cycle, at Phase
4, after this entry was registered at Phase 3) and independently restates
the identical bracket structure — front-colocated/rear-only, both length
scales, the NETD disclaimer — with real found numbers, not the frozen
predicted band. **`site` was never widened to include it.** Running the
tool confirms this directly: all `PASS` lines for
`exp063-cf-bench-vs-witness-derivation` cite only `NOTES.md`; zero mention
of `phase4_results.md` anywhere in that entry's output.

This is structurally the SAME shape as both Iteration-39 Checkpoint-4
firings on `exp061-t18-evidentiary-tier-propagation` — a check registered
before a later-written results file existed, never widened once that file
was actually written — except caught here, live, at Phase 5, in the same
cycle the entry was built, before any later citation of it, with **no
live violation underneath it** (I independently verified `phase4_results.md`
DOES correctly carry both bracket endpoints and the disclaimer at both
length scales — Section 1.1 above; the content is right, only the
MECHANICAL CHECK's reach is short). This is the Iteration-38 shape
(self-caught, pre-any-later-citation, content already correct), not the
Iteration-39 shape (a hardened, grace-spent tripwire failing to discover
an already-merged, ALREADY-VIOLATING file). I state this distinction
explicitly because Red Team's own Phase-2 audit this cycle (§3) argued the
identical Iteration-38-vs-39 distinction for VISION's own Phase-2 catch,
and the same reasoning applies here without alteration.

**Recommendation**: widen `site` to a list covering both `NOTES.md` and
`phase4_results.md` (`lab/numeric_lint.py`'s own schema may need a
`sites`-plural or repeated-entry accommodation if it does not already
support a list — I did not find one in a quick read of the module; this
is itself worth a one-line note for whoever applies the fix). Cheap,
mechanical, no analysis required.

---

## 3. A third, independent finding: the Summary table's own "inside band" language is not numerically accurate for two of the four sourced κ values — verified by direct recomputation, not hand-typed (R4)

I recomputed `front_surface_conduction_correction` myself, invoking the
actual committed function, at all four sourced κ values plus the TD-1
predicted-band edges, for both the bench and MP-5/730× geometries:

```
>>> from lab import thermo_sidecar as ts
>>> # MP-5/730x, L=1051.2um, margin = 1.35 / correction_factor
kappa= 0.10  CF=1.314059  margin=1.0274x   <- TD-1 band floor
kappa=20.00  CF=1.001570  margin=1.3479x   <- TD-1 band ceiling; matches TD-5's own predicted upper edge exactly
kappa=40.00  CF=1.000785  margin=1.3489x   <- SOURCED (query 2, derived), ABOVE the predicted 1.3479x ceiling
kappa=50.00  CF=1.000628  margin=1.3492x   <- SOURCED (query 6), ABOVE the predicted 1.3479x ceiling

>>> # bench, L=2.34um, margin = 699.27 / correction_factor
kappa=20.00  CF=1.001301  margin=698.3617x  <- TD-1 band ceiling; matches TD-4's own predicted upper edge exactly
kappa=40.00  CF=1.000650  margin=698.8156x  <- SOURCED, ABOVE the predicted 698.36x ceiling
kappa=50.00  CF=1.000520  margin=698.9064x  <- SOURCED, ABOVE the predicted 698.36x ceiling
```

**The mechanism, and why it is real, not an error on my part:** TD-3/4/5's
own predicted numeric bands were computed by propagating TD-1's own
PREDICTED κ range, [0.1, 20] W/(m·K), through the correction formula —
correctly, since that is all Phase 3 had before Phase 4 ran. But TD-1's
own Phase-4 search FOUND real figures (40 and 50 W/(m·K), the derived
query-2 estimate and the drawn-sheet query-6 figure) that sit ABOVE its
own predicted band's ceiling of 20 — a fact `phase4_results.md`'s own TD-1
section discloses honestly and explicitly ("the derived ≈40 W/(m·K)
estimate sits just above the band's own upper edge"). That disclosed
overshoot was never carried forward into TD-3/TD-4/TD-5: propagating
κ=40/50 through the SAME formula pushes their corrected margins slightly
past the predicted bands those three sections quote, in the safe/good
direction (LESS correction needed at the bench scale, MORE margin at the
witness scale) — never toward DETECTABLE, and nowhere close to any actual
pre-registered falsification condition (TD-3's ">2×," TD-4's "<100×," and
TD-5's own binding test, "<0.0897 W/(m·K)," are the only tests that
actually govern the verdict, and none is remotely approached). **No
verdict is wrong.** But the Summary table's own literal claims —
"1.2920×–1.3492×, inside band" (predicted ceiling: 1.3479×) and
"674.22×–698.91×, inside band" (predicted ceiling: 698.36×) — are not
accurate as written, by margins of 0.09–0.10%. TD-3's own reported range
(1.00052–1.03716 "inside predicted band [1.001,1.26]") has the SAME
defect at its other edge: 1.00052 and 1.00065 (κ=50, 40) sit slightly
BELOW the predicted floor of 1.001.

This is small, cosmetic, and directionally harmless — but it is a further,
independently-found instance of this program's own repeatedly-named bug
class ("a cited NUMBER, not just a phrase, drifts unreconciled across
sibling sections of one document" — Iteration 38's `τ_shell=24` vs.
9.4026, the stale-150µm THERMO disposition; Iteration 39's EM-6/EM-7
R-vs-T drop), this time within a single Phase-4 document rather than
across files, and the third-plus instance this program has now
self-documented. It reinforces, from a fresh angle, the already-queued
numeric-consistency-tooling item (§5 below) rather than opening a new
concern.

---

## 4. Does either new finding (§2, §3) or the summary-table gap (§1.2) fire Checkpoint criterion 4?

**My own reading: no, on all three, for the same reason Red Team's own
Phase-2 audit this cycle gave for the Iteration-38-vs-39 distinction — but
I lay out the reasoning rather than assert it, consistent with this
seat's role (I find and pin gaps; Red Team's Phase-5 audit rules).**

All three findings share the same shape: found live, at Phase 5, in the
same iteration the underlying machinery was built; no prior "grace already
spent" tripwire exists for any of `exp063-biot-correction-machinery`,
`exp063-thermo-disposition-netd-disclaimer`, or
`exp063-cf-bench-vs-witness-derivation` (all three were registered THIS
cycle, at this cycle's own Phase 3, with zero opportunity for a prior
firing); none rests on an already-hardened, self-catch-grace-spent
lineage the way `exp061-t18-evidentiary-tier-propagation` did at both
Iteration-39 firings; and critically, none is a live VIOLATION of an
existing rule's letter — the mandatory-fix docket's own text named
"TD-3/TD-4/TD-5's own table rows," which both `NOTES.md` and
`phase4_results.md` satisfy exactly as written. The Summary table and the
`numeric_lint` site gap are both places the docket's INTENT plausibly
reaches but its LETTER did not yet name — the Iteration-38 shape (ordinary
Phase-5 feedback the review loop exists to catch), not the Iteration-39
shape (a promise already made, in writing, and shown broken).

**A forward-tripwire recommendation, matching this program's own standing
pattern (Iterations 23, 37, 38, and this cycle's own Phase-3 ruling)**: if
either the Summary-table disclaimer or the `numeric_lint` site-widening is
not applied before this cycle's own LOGBOOK entry closes, or if a
materially similar gap recurs in either of these three entries at
Iteration 41 or later, that should fire criterion 4 without further
deliberation.

---

## 5. From my own charter's lens: does anything in exp-063 touch perceptual thresholds, contrast, or detection?

**No — confirmed by a full second read of `NOTES.md` and
`phase4_results.md`, specifically hunting for smuggled perceptual claims**
(the standing risk pattern this charter exists to catch, per the
T17-spiropyran precedent and my own seat's repeated Iteration-38/39
findings). None found. Every TD-1 through TD-5 prediction is a
conduction-physics/instrument-detectability quantity (a thermal
conductivity, a Biot number, a correction factor, a microbolometer-NETD
margin) — never a contrast, luminance, adaptation, or temporal-sensitivity
claim. §2's own "zero constraint-1/2/3/4 metric scored" self-declaration
is honestly true on inspection, independently confirmed alongside Red
Team's own identical finding (`phase2_redteam_audit.md` §5, criterion 1).
This charter's own duty — "pin numeric thresholds, with sources, BEFORE
any run that scores against them" — has nothing to attach to this cycle,
which is the correct outcome for an instrument/model-fidelity continuation
with no phenomenon-constraint metric in scope, not an absence to be
filled.

One item worth naming for completeness, not a defect: this cycle's own
Idealization 3 (κ_solid sourced from "general VACNT/CNT-forest
thermal-interface literature, not necessarily the SAME specific
record-blackness/Vantablack-class geometry") and `phase4_results.md`'s own
"flagged geometry-class distinction" (drawn-sheet vs. as-grown forest) are
a thermal-conductivity-domain recurrence of the identical
evidentiary-caution discipline my own charter has repeatedly required for
optical claims (n_eff, α_true) — correctly self-applied here without my
needing to raise it as a critique.

---

## 6. Verdict

**PROMISING.**

The core physics is sound and now independently re-verified FOUR times
(EM's Phase-2 critique, Red Team's Phase-2 audit, my own recomputation
above, and the live trust-suite stage), to the printed digit throughout.
The Phase-2 triangulation (PHOTONICS/MATERIALS/EM each attacking a
different variable in the same Section-4 model, Red Team's own audit
confirming they compose rather than duplicate) is a genuinely good piece
of process; the two disclosed-not-resolved brackets (substrate-interface
boundary condition, witness-scale length legitimacy) are honestly flagged
as open rather than silently resolved either direction, and neither
threatens any classification even at its own worst disclosed reading. The
mandatory-fix docket from my own Phase-2 critique was applied correctly
and completely at the level it was written to reach (TD-3/4/5's own
`NOTES.md` and `phase4_results.md` sections, both linters PASS live, the
new trust-suite stage is 4/4 green). Every sourced κ this cycle found —
even the single worst real figure, 0.7 W/(m·K), the bulk-aggregate
measurement — leaves both the bench-scale and witness-scale UNDETECTABLE
classifications comfortably intact, 8×–560× above the falsification
boundary at the fragile end.

I do **not** downgrade to PARTIAL the way this seat's own Iteration-36/37
and Iteration-39 precedent did, because the three findings above are
categorically lighter than those precedents: no disclosure is fully
ABSENT anywhere a rule's own letter required it (unlike Iteration
36/37/39's live violations), no hardened tripwire's grace is spent, and
none of the three findings moves, or comes close to moving, any scored
number past its actual falsification condition. They are real, and should
be fixed before this cycle's LOGBOOK entry closes (§4's tripwire), but
they are the ordinary texture of a healthy Phase-5 review catching what
Phase 3's own necessarily-incomplete docket could not yet see (the Summary
table and `phase4_results.md` did not exist when the docket was written),
not evidence of drift.

---

## 7. Top-3 ranked candidate directions for Iteration 41+

1. **Resolve exp-063's own two disclosed-not-resolved brackets before
   citing TD-5's headline number as settled anywhere outside this
   document.** The substrate-interface boundary condition (is a real
   CNT-forest coating's dominant loss channel front-colocated with
   absorption, as MATERIALS argues from the program's own established
   "coating" deployment language, or genuinely rear-only, as Section 4's
   worst-case model assumes?) and the witness-scale length legitimacy
   (does `L=τ_true/α`, an optical-extinction-derived thickness, pass
   `gas_conduction_h_eff`'s own licensing test for a real geometric
   conduction length — flagged and deferred at Iterations 38, 39, AND now
   40 on the identical `l_geometric_m` lineage) are both cheap, analytic,
   zero-FDTD continuations this program has already built the vocabulary
   for (T22/T23). A third deferral in a row on the length question in
   particular should be named explicitly as such if it happens again.
2. **Pin the record-blackness/Vantablack-class CNT forest's OWN
   through-thickness thermal-conductivity figure** — not the generic
   VACNT/thermal-interface-material literature this cycle correctly
   sourced but explicitly flagged as an adjacent application class
   (Idealization 3). This is the thermal-domain sibling of Iteration 39's
   own still-unaddressed #1-ranked item (the same geometry's inter-tube
   pitch/diameter for near-field coupling) — `phase4_results.md` names
   this gap itself ("still the program's #1 ranked Iteration-40+ queue
   item, unaddressed by this cycle, a different physical quantity") and
   this cycle's own query 8 (targeting the newly-pinned *Carbon* 2018
   citation for a thermal figure) came back an honest null. One
   dedicated, narrowly-targeted query set could close both the pitch/
   diameter and thermal-conductivity gaps for the actual candidate
   geometry at once, replacing two cycles of adjacent-class inference with
   one direct citation.
3. **Close this review's own three findings, same-shift if possible, and
   fold the pattern into the standing numeric-consistency-tooling item**
   (already re-filed with the Director as owner at Iteration 38/39/40):
   add the NETD disclaimer to `phase4_results.md`'s Summary table/Bottom
   line; widen `exp063-cf-bench-vs-witness-derivation`'s `site` to include
   `phase4_results.md`; correct the Summary table's "inside band" language
   for TD-3/TD-4/TD-5 (§3 above) to disclose that 2 of 4 sourced κ values
   sit slightly outside the pre-registered predicted bands (harmlessly, in
   the safe direction) rather than stating all four are "inside band."
   None of these three changes any verdict; all three are exactly the
   class of defect `lab/numeric_lint.py` exists to eventually catch
   mechanically rather than by a seventh independent human/agent read.

---

## 8. Ruled-out registry check (R1–R5, T1–T26)

No re-proposal found, on direct read of the complete registry against this
cycle's actual content:

- **R1–R5**: none apply. exp-063 makes no refractive-cloaking claim (R1),
  no integer-λ shell-thickness claim (R2), no grid-artifact explanation
  for a measured feature (R3), no hand-typed "precisely recomputed"
  figure passed off as verified (R4 — every number in Section 4 and every
  scored result in `phase4_results.md` is computed by direct invocation of
  `lab/thermo_sidecar.py`, independently re-run by EM, Red Team, and by me
  above, all matching to the printed digit), and no `P`-normalized
  phase-offset regressor (R5).
- **T1–T26**: `phase1_proposal.md` correctly declares "T1 escape route:
  N/A" — this cycle scores no constraint-1/2/3/4 metric and proposes no
  mechanism. It is an honest, correctly-scoped continuation of **T23**
  (Iteration 22/23's own informal Biot-number/Maxwell-Garnett findings),
  promoting T23's own arithmetic to committed, trust-suite-gated code for
  the first time with the actual candidate material's own κ, rather than
  re-arguing T23's already-closed nominal question (which length is
  licensed for `h_eff` at the ORIGINAL bench geometry — a different
  question from this cycle's NEW one, whether that same licensing logic
  extends to a Fourier-conduction-path role at witness scale, which
  remains genuinely open, not re-closed). No T18/NETD/sigma_flat/
  thermo-length-scale-staleness registry entry is mis-triggered by this
  cycle's own text. I did not find grounds to add a new entry to the
  Ruled Out registry from this cycle's content — the two open brackets are
  live, disclosed threads, not refuted claims.
