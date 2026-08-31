# Phase 5 Review — QUANTUM OPTICS seat (exp-097, Panel Iteration 74)

*Blind review, fresh context. Charter: non-classical absorption, state-
dependent/coherent interactions; expressibility contract N/A this cycle (no
mechanism proposed, T1 N/A, `REALIZABILITY_MEMO.md` untouched — confirmed
directly from `phase1_proposal.md` §4 and `NOTES.md`'s own T1 section).
Applying this seat's discipline instead, per the assignment: precise
state-identification — does Check 6's three-sub-check design
(`theta_ok`/`family_ok`/`cpl_ok`) genuinely, independently discriminate the
state (family/cpl/angle registration) it claims to, in the actual committed
code, not merely in NOTES.md's prose? Note also this seat's own prior
proposal (exp-096's Check 6) is under review here, and this cycle's own
governance ruling (§6/Item 4) names the Phase-5 reviewer as the party
required to confirm the Result-section banner "by name" — discharged below,
§5.

**Method.** Read in full this session: `PANEL.md`; the RULED-OUT R1–R18
registry in `LOGBOOK.md`; the T28 sub-thread's Iteration 70–73 narrative;
`experiments/096-.../NOTES.md` and `run.py`; every file in
`experiments/097-t28-r18-tier0-gate-closure/` (`phase1_proposal.md`, all
five Phase-2 critiques, `phase2_redteam_audit.md`, `NOTES.md`, `run.py`,
`results.json`); `experiments/069-t21-.../design_geometry.py`; `lab/fdtd2d.py`
lines ~125–186. **Independently re-executed `run.py`** (not merely read) and
diffed the fresh output against the committed `results.json` — see §1.

## 1. Independent re-execution

```
$ python3 experiments/097-t28-r18-tier0-gate-closure/run.py
```

Re-ran to a scratch copy and diffed programmatically against the committed
`results.json` (excluding the non-deterministic `wall_time_s` field):
**bit-exact match on every other field.** `registration_gate_outcome=CLEAN`,
all fault-injection scenarios (positive control, FI-A/B/C/D/E/F/G/H)
reproduce exactly as tabled in NOTES.md's Predictions. Confirmed
`git status`/`git diff --stat` on `lab/` show zero changes — the "0 FDTD
calls, zero `lab/` diff" claim is real, not asserted.

## 2. Check 6's tautology fix — genuinely independent, verified by direct
## code trace and by re-running the fault-injection triad myself

This is the load-bearing question this seat was asked to answer. Traced
`check6_positional_and_cpl` (`run.py:156–171`) by hand against its inputs:

- **`theta_ok`**: `pt["theta"]` (sourced from `exp095.RANK*_ANGLES`, a live
  reference to job constants) vs. `NOTES_MD_FROZEN_LINE_VALUES[line][pair_index]`
  (hand-transcribed from NOTES.md prose). Independent — confirmed, unchanged
  from exp-096's own already-sound design for this half.
- **`family_ok`** (the actual fix): `pt["family"]` (hand-typed once, in
  exp-096 `run.py`'s `REPRESENTATIVE` list, `line 84–93` — verified this
  session that `family` and `notes_line` are two *separately* hand-typed
  literals on the same dict entry, not derived from one another) vs.
  `NOTES_MD_FROZEN_FAMILY_BY_LINE[pt["notes_line"]]` — keyed by `notes_line`,
  **never** by `pt["family"]`. This is a genuine, structurally independent
  cross-check: a `family` transcription slip in `REPRESENTATIVE` cannot
  corrupt both sides of this comparison, because the ground-truth side never
  reads the field under test. I confirmed this is not merely asserted but
  live in the production path — `check6_new` in `main()` runs
  `check6_positional_and_cpl` directly over `REPRESENTATIVE`, not only inside
  the synthetic FI-H harness — so a real mislabeling in the representative
  set would in fact be caught, not just a contrived one.
- **`cpl_ok`**: `CPL[pt["family"]]` vs. `cpl_frozen` — both sides ultimately
  keyed by `pt["family"]` once `family_frozen` resolves it, so `cpl_ok` is
  **not** independently meaningful in isolation (Idealization 40 says this
  explicitly, correctly). But the composite `clean = theta_ok and family_ok
  and cpl_ok` is an AND — if `family_ok` fails, `clean` is `False`
  regardless of `cpl_ok`'s own (possibly spurious) value. So the *tautology*
  Red Team found in Phase 1's draft (both sides of `cpl_ok` keyed by the same
  untrusted `family` field, unconditionally) is genuinely closed by
  `family_ok`'s gate — I re-verified this is not just true by construction
  argument but empirically: FI-H (`R3`→`R4` mislabel at line 511) reports
  `family_ok=False` **and** correctly flips the composite `clean` to `False`
  in my own re-run, matching `results.json`.
- **Old-vs-new comparison, executed, not merely claimed**: `check6_set_
  membership_OLD` is retained and run side-by-side on FI-E/F/H in my re-run —
  old reads CLEAN on all three (`old_clean=True`), new correctly flags all
  three. This is a real R12-idiom demonstration, not an assertion.

**Verdict on the core question: yes — Check 6, as coded, now genuinely and
independently discriminates all three states (angle, family, cpl) it claims
to, for the specific fault classes exercised (FI-E/F/H), confirmed against
source and by independent re-execution, not taken on NOTES.md's word.**

## 3. Red Team's own Phase-2 finding — my own scope-gap finding
## (FI-G/R3/R5) — both independently reconfirmed fixed

My own exp-096-cycle Phase-2 critique flagged FI-G's original R4-only scope
(Idealization 43 disclosed FI-D's R4-only scope but not FI-G's identical
one). Re-checked this cycle's `run_fi_g()` (`run.py:236–250`): now scores
`native_src_x=301` against all three of `R3_CONFIGS["C40_R3"]`,
`R4_CONFIGS["C40_R4"]`, `R5_CONFIGS["C40_R5"]` — confirmed in my own re-run,
`FI_G.all_caught=True`, all three legs individually `caught_as_defect=True`.
**Genuinely fixed, not merely disclosed.**

Red Team's own Phase-2 finding (the `cpl_ok` tautology, §2 above) is the
more consequential of the two — traced independently here and confirmed
fixed, matching §2's analysis. Both of the two governing-defect findings
this reading task asked me to verify (my own FI-G gap; Red Team's `cpl_ok`
tautology) **were actually fixed as claimed, in the actual committed code,
not only in prose.**

## 4. A gap none of the five blind Phase-2 critiques or Red Team's own audit
## named: Check 5's G-config scope limit is real, unchanged, and its
## disclosure has been quietly weakened relative to exp-096's own wording

`check5_recipe_spot_check_extended()` (`run.py:183–203`) reads only
`dg.R3_CONFIGS["C40_R3"]`, `dg.R4_CONFIGS["C40_R4"]`, `dg.R5_CONFIGS
["C40_R5"]` — confirmed directly against `design_geometry.py`'s own
`R{3,4,5}_CONFIGS` dicts. **The `G40_*` (padded) variant of all three
families remains completely unchecked by Check 5, exactly as before this
cycle's extension** — the extension added two new *families*, not the
missing *config* axis.

This limit is not new — exp-096's own Idealization 39 named it explicitly
for `R4`: *"A defect isolated to a different family (`R3`/`R5`) or the `G`
(padded) config specifically would not be caught by this single
spot-check."* But exp-097's `NOTES.md` restates Idealization 39, "carried
forward," as: *"Check 5, even extended, remains independent of the module
constants and the function call but not of the formula itself"* — the
family clause is correctly dropped (now genuinely covered), but **the `G`
(padded)-config clause is dropped too, silently, even though the gap it
named is still fully present in the code** (verified above). Idealization 42
(new this cycle) restates the formula-dependency point again but likewise
never mentions the G-config gap. Nothing in `NOTES.md` currently states, in
its own words, that Check 5 (any of its three families) has never checked a
padded config.

**This is not a code defect** — nothing incorrectly reports CLEAN; the
untested axis is simply untested, same as before. And it is not load-bearing
to this cycle's `CLEAN` verdict. But it is exactly the class of drift this
cycle's own R18 mandate exists to police: a previously-precise scope
disclosure, compressed across a "carried forward" restatement, in a way that
drops a still-true, still-relevant limitation rather than only dropping the
part that became stale. A future cycle citing "Check 5, extended to
R3/R4/R5" from this document alone, without re-reading exp-096's original
Idealization 39 text or the actual `run.py` source, could reasonably (and
wrongly) assume the padded-config axis is now covered for all three
families, when it never has been for any of them.

**Severity: minor, disclosure-only, non-blocking.** Recommend a one-line fix
before this enters the permanent record: restate Idealization 39/42 to name
the G-config gap explicitly for all three families (not just formula-sharing
across families), matching the precision of exp-096's own original text.

## 5. Governance-ruling verification duty (§6/Item 4), discharged as required

The Phase-2 fix docket (item 4, VISION's finding) requires this Phase-5
review to explicitly confirm, by name, that `NOTES.md`'s own Result section
carries the carried-idealizations banner sentence. **Confirmed by direct
inspection**: `NOTES.md`'s Result section opens with *"Carried idealizations
banner (per §6's own governance ruling ... ): every result below is
governed by Idealizations 1/7/17/38/39 plus this cycle's own 40–45."* —
present, correctly worded, matching the Predictions-section banner. **PASS.**
This is the first T28 cycle since the Iteration-65 rule's adoption to
satisfy its literal text (Predictions *and* Result) rather than the
Idealizations+Predictions pattern exp-095/exp-096 both drifted into.

## 6. What survives, independently re-checked and not attacked further

The phase-ramp (`phase_expected`) and taper (`taper_expected`) formulas
reproduce `lab/fdtd2d.py:132–186` bit-exact (re-derived by hand this
session, matching PHOTONICS'/EM's own Phase-2 findings). The
`y_hi`/`R{3,5}_BASE_NY` mis-citation (EM/THERMODYNAMICS' Phase-2 catch) is
correctly fixed in `NOTES.md`'s prose. The 21-construction accounting is
bit-exact in my own re-run. The standing-items ledger (grazing-incidence,
x-wall wavelength-generality) is restored, per PHOTONICS' Phase-2 catch.

## Verdict

**CONCUR-WITH-GAP(S).**

The cycle's central claim — that Check 6's three-sub-check design now
genuinely, independently discriminates angle/family/cpl registration state,
closing both the tautology Red Team found and the scope gap this seat found
at exp-096 — **is true, verified here by independent code trace and by
re-executing the script myself, not taken on the document's word.** No
undisclosed code-level defect was found in Checks 5, 6, or 7, or in the FI
triad. The one gap this review adds (§4: Check 5's G-config scope limit,
present since exp-096, whose disclosure was quietly weakened rather than
carried forward at the same precision by this cycle's own restatement) is
minor, non-load-bearing, and not a repeat of any already-fixed-and-reused
gap — it does not rise to a Checkpoint-criterion-4 matter, but should be
named and fixed same-shift, matching this program's own R4/R18 discipline
for scope claims.

## Ranked candidate directions for Iteration 75

1. **(Zero-cost, same-shift, this cycle's own fix docket)** Restate
   Idealization 39/42 to explicitly name the still-open G-config gap in
   Check 5's extension (§4 above) — the one finding this review adds. Cheap
   enough to fold into Phase 3/5 closeout rather than a standalone item.
2. **(Tier 1, item 6 of the Reconciled Iteration-74 queue — top rank)**
   Bracket the other three established `cpl=20` nulls at `cpl=40`
   (EM's proposal, ~24 calls). This is the decisive discriminator the whole
   two-cycle registration-gate detour (exp-096, exp-097) was built to
   unblock: with the gate now CLEAN under strictly more discriminating
   machinery (my own re-execution confirms this independently), a
   family-wide artifact vs. feature-dependent migration is exactly what this
   check resolves, and nothing about this cycle's own findings (§4 included)
   bears on that question's validity.
3. **(Tier 1, item 7)** The re-centered node-bracketing re-run at
   θ₀≈38.590°, sized to exp-096's own confirmed ≥0.5° half-width — the
   direct answer to the question the registration-gate detour exists to
   enable, sequenced after item 2 per the queue's own reasoning (a
   family-wide defect finding from item 2 would change how item 7's own
   result should be read).
4. **(Preventive, bundle with item 2 or 3)** Pre-wire `netd_row()`/
   `cell_metrics_r{3,4,5}` sidecar extraction into whichever run.py computes
   `delta_scene`/`frac_contrast` next, per R16 — cheap insurance against a
   third disclaimer-without-persistence occurrence (which would fire
   Checkpoint criterion 4 automatically per R16's own forward-elevating
   clause), and this seat's own rotation-lead cycle (exp-094) was the one
   that most recently tripped an adjacent version of this exact gap.
