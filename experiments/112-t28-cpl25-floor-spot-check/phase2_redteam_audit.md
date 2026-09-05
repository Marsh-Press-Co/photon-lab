# Phase 2 Red Team Audit — exp-112 (Panel Iteration 89, candidate)

*Red Team receives everything this cycle: the Phase-1 proposal package
(`phase1_proposal.md`, `run.py`, `chunk_runner.py`, `analyze.py`) and all
five blind Phase-2 critiques. Charter: kill internal inconsistency,
unfalsifiable claims, mechanisms inexpressible as simulation parameters,
and quiet constraint violations — not textbook-physics purity. Every
consequential claim below was independently re-derived or re-executed
from primitives, not trusted on any critique's own say-so (this
sub-thread's own R4/R18 discipline).*

## 0. Scope confirmed before auditing content

T1 escape route: **N/A, confirmed structurally**, independent of the
document's own claim. `run.py`/`chunk_runner.py`/`analyze.py` touch only:
a congruent grid-resolution geometry generalization, a checkpoint/resume
capture driver, and a comparison of two already-frozen classification
functions across two `cpl` values. No σ(I)/σ(x,t)/angular-selectivity/
sub-threshold content is expressible in a grid-resolution parameter. No
constraint-1/2/3/4 verdict is scored or moved anywhere in this document.
Zero `lab/` diff this cycle (`git status --short lab/` clean) — the trust
suite is not implicated by this Phase-2 audit.

## 1. Independent re-verification (from primitives, not from the critiques' prose)

| Critique's claim | Re-verification performed | Result |
|---|---|---|
| THERMODYNAMICS: `chunk_runner.py`/`analyze.py` crash before any `Sim.run()` call, via a `run`/`run` module-name collision | Ran `python3 chunk_runner.py 156 25 empty` and `python3 analyze.py` myself, fresh, in this exp-112 directory | **CONFIRMED, both crash identically**: `chunk_runner.py` → `AttributeError: module 'run' has no attribute 'geom_fixedabs_cpl'` at `step_once()`'s first line (before `time.time()`, before any Sim construction); `analyze.py` → `AttributeError: module 'run' has no attribute 'verify_geometry_identity'` at its own first executable line. `python3 run.py --predictions-only` and `python3 run.py --verify-geometry` (exp-112's own `run.py`, run directly, not imported under a colliding alias) both work exactly as claimed — `verify_geometry_identity` returns `pass_=True` at both r, confirming the bug is specific to the TWO downstream files' own import pattern, not `run.py` itself. |
| MATERIALS: sponge accumulated log-attenuation `13.93` (cpl=20) → `17.24` (cpl=25), discrete cell-sum route | Reimplemented `_damping()`'s own ramp formula from `lab/fdtd2d.py` (`ramp=(arange(absorb,0,-1)/absorb)**3`, coefficient `0.30`) independently, computed `sum(0.30*ramp)/S` with `S=0.32/√2` | **CONFIRMED bit-exact**: `13.929451` / `17.242357` |
| ELECTROMAGNETISM: same finding via the closed-form continuum route, `-13.26`/`-16.57` | Computed `-(0.3/4/S)*absorb` for `absorb∈{40,50}` independently, `C=∫₀¹(1-ξ)³dξ=1/4` | **CONFIRMED bit-exact**: `-13.258252` / `-16.572815` — two structurally different derivations (discrete cell-sum vs. closed-form continuum integral), both independently reproducible, converge on the identical qualitative finding: a genuine `1.24×-1.25×` non-invariance, not an artifact of either method |
| VISION: "detection floor" appears in the mechanism narrative but not in the code-enforced `DISCLAIMER` string | `grep -n "detection floor" phase1_proposal.md run.py` | **CONFIRMED**: two hits in `phase1_proposal.md` §1 (lines 34/36), zero hits in `run.py` — the 251-word `DISCLAIMER` (lines 231-251) never uses the phrase |
| PHOTONICS: the full 48-bin arrays exist at both `cpl=20` and `cpl=25`, so a bin-neighborhood correlation check is zero-marginal-cost | Checked for `experiments/112-.../results.json` and any Phase-4 artifact | `cpl=20` arrays genuinely exist (`experiments/110-.../results.json`, committed). **`cpl=25` arrays do NOT yet exist** — no `results.json` in this directory (confirmed by directory listing and `git log`/`git status`, which show only the five Phase-2 critique commits). PHOTONICS' own present-tense "already exist... this cycle's own `analyze.py` output" is premature — Phase 4 has not run, and per the Thermodynamics finding above, currently *cannot* run. Non-fatal to PHOTONICS' own recommendation (the check remains genuinely zero-marginal-cost once Fix 1, below, lands and Phase 4 actually executes) but the critique's own tense is inaccurate as filed. |
| Numeric grounding facts in `phase1_proposal.md` §2.0 (named-bin baseline figures, `cost_gate_check` output, `cpl_cost_table.py` output, domain-clearance arithmetic) | Re-read `experiments/110-.../results.json` directly for the named bin (index 4, `-146.25°`); re-invoked `R.cost_gate_check(489.729, 1469.186)` directly; re-ran `cpl_cost_table.py` fresh; recomputed `box_a`/clearance by hand from `geom_fixedabs_cpl` | **All reproduce exactly**: `local_snr_peccored=0.0965212...`, `local_snr_hollow=0.1060574...`, `floor=0.0011261666...`, `resolved=False` (bit-exact); `local_rel=9.8798%` (matches claimed "9.88%"); `cost_gate_check` returns `proceed_to_r312=False` bit-exact to the proposal's own table; `cpl_cost_table.py` reproduces `1469.19s`/`15020.37s` bit-exact; `box_a` clearance = 305 cells, confirmed by hand. **No R4-class figure defect found anywhere in the proposal's own numeric claims** — every number that IS reported is genuinely, verifiably computed. |

## 2. Numbered attacks

**Attack 1 — `[inconsistency]`.** The Phase-4 execution pipeline as
committed cannot run at all, and this is not a hypothetical: I executed
it and it crashes. `chunk_runner.py` and `analyze.py` both do `import run
as R110` (intending exp-110's `run.py`) immediately followed by `import
run as R` (intending *this directory's own, differently-located*
`run.py`). Python's `sys.modules` cache keys purely on the string `"run"`
— the second `import run as R` does not re-search `sys.path`; it silently
rebinds `R` to whatever module object `sys.modules["run"]` already holds
(exp-110's, since that directory is inserted onto `sys.path` last, i.e.
first-priority, in both files). `R` and `R110` end up being the *same*
object in both files — exp-112's own `run.py` (which defines
`geom_fixedabs_cpl`, `CPL_TARGET`, `classify_resolution_check`,
`verify_geometry_identity`, `NAMED_BIN_DEG`, `MARGIN`, the `BASELINE_*`
constants, and this cycle's own `build_predictions_text`/
`build_result_text`) is *never actually bound to `R` anywhere in either
file*. Every one of those names is unreachable through `R` in
`chunk_runner.py`/`analyze.py`. This is not narrowly scoped to the one
attribute access that happens to crash first (`geom_fixedabs_cpl` in
`chunk_runner.py`, `verify_geometry_identity` in `analyze.py`) — it is
total: `chunk_runner.py`'s own future-use guard
(`check_cost_gate_for_r312_expansion`, line 109, calling
`R.cost_gate_check_for_r312_expansion`) and every one of `analyze.py`'s
eight-plus exp-112-specific attribute reads on `R` would fail identically
if reached. The consequence stated plainly: the headline "1469.19s" cost
figure that scopes this entire cycle to r=156-alone was never produced,
and cannot currently be produced, by the pipeline the document describes
as producing it — it comes from `cpl_cost_table.py` (a separate,
independently-verified, already-correct extrapolation script, confirmed
bit-exact above), not from a single second of genuine `cpl=25` FDTD data.
As shipped, Phase 3 cannot honestly freeze Predictions against this
pipeline, because the pipeline cannot execute past its own first
geometry call.

**Attack 2 — `[inconsistency]`.** §2.1's own framing — "`ABSORB`/`EDGE`...
following the T21/Block-MINI family's own established convention," folded
into the same table and the same "congruent-refinement" language as
`tau_shell`/`sigma_max` — asserts a resolution-invariance guarantee for
the sponge boundary that the code does not actually provide, and that I
independently confirm is false by direct construction. `tau_shell`'s
invariance is a genuine, provable fact about `lab/fdtd2d.py`'s Yee update
coefficients (`alpha=sigma_e·S/(2·eps_r)`, where the Courant factor `S`
cancels exactly against the compensating `1/ratio` scaling of
`sigma_max`) — MATERIALS' and EM's own steel-men each re-derive this
correctly and I confirm it independently: it holds at both `cpl`, exactly.
The domain-edge sponge (`self.Ez *= self.damp_e`, `_damping()`) is a
structurally different mechanism — a bare per-timestep multiplicative
mask with no `S`/`dt` normalization anywhere in its own formula — and its
accumulated one-way log-attenuation genuinely scales with `ABSORB`'s
*absolute cell count*, which the congruent-refinement recipe explicitly
inflates by the same `ratio=1.25` used for signal-preserving quantities.
Two independent derivations (a discrete cell-sum route and a closed-form
continuum-integral route), both reproduced bit-exact above from the raw
`lab/fdtd2d.py` source, agree that the log-attenuation rises by exactly
the geometry-scaling ratio (`16.573/13.258=1.25` exact in the continuum
form) — a real, quantifiable, disclosed-nowhere non-invariance. Non-fatal
(the boundary only strengthens with `cpl`, which cannot manufacture the
near-field signal under test, and no r=312 leg exists this cycle to
compound it) — but "same convention" is false as stated, and the
Idealizations section's actual text ("not independently re-derived from a
... bound") describes an *unverified* parameter, when the true state,
once checked, is a *verified non-invariant* one — a materially different
disclosure, on exactly the axis R8 (LOGBOOK RULED OUT registry) exists to
close: an affordable, named check was skipped, and a vaguer disclosure
substituted for a computed number.

**Attack 3 — `[inconsistency]`.** The mechanism narrative (§1) stakes its
own claim on "genuine, deterministic sub-wavelength field structure,"
which by construction should imprint *spatially correlated* structure
across several adjacent angular bins (physical correlation length ~
λ/box-scale) — while `classify_resolution_check`'s Check A scores the
named bin in complete angular isolation, comparing only its own single
`local_snr` reading against its own past self at `cpl=20`. Nothing in
`run.py`/`analyze.py` computes or reports any neighbor-bin structure. This
is a real gap between what the mechanism narrative claims would
distinguish "real structure" from "isolated noise spike" and what the
actual, committed classifier tests — confirmed absent by direct source
read (no correlation, covariance, or neighbor-window computation exists
anywhere in either file). The gap is currently low-stakes only because the
document's own Idealizations section already declines to claim more than
"rule out sign-flip/order-of-magnitude collapse" — but the check is
genuinely zero-marginal-cost (both 48-bin arrays will exist once Fix 1
lands) and directly strengthens exactly the discriminating power a
"SURVIVES" reading would need before any future citation could honestly
call it "candidate real structure" rather than "not yet ruled out."

**Attack 4 — `[inconsistency]`.** "Detection floor" — used twice in §1's
mechanism narrative to describe this cycle's own grid-discretization SNR
instrument — sits one section away from the single code-enforced
`DISCLAIMER` string that R23 (LOGBOOK RULED OUT registry) exists to make
authoritative, and is never folded into it; confirmed by direct grep, zero
hits in the asserted text. Constraint-3's own governing vocabulary
("what would make a human eye FAIL to register something physically
present") uses the identical word "detection" for a completely different
quantity (a human perceptual/observer threshold). This is the exact shape
of the R9/T16 (Iteration 53-54) unit-conflation this program has already
paid for once: an ambiguous, un-asserted phrase, positioned exactly where
a future citation-shortening reviewer would lift it out of context,
sitting adjacent to — but outside — the one mechanism (a single-source
string plus a code-level assert) this program built specifically to
prevent that. The document's own T1/constraint-3-N/A claim is correct
today; the risk is entirely in how cheaply this ambiguity could survive
into a future citation that inherits this cycle's own numbers without its
own full context.

**Attack 5 — `[inconsistency]` (Red Team's own, not sourced from any
single blind critique).** VISION's own steel-man credits `analyze.py`'s
result-side `assert DISCLAIMER in ...` (line 141) as "genuine" and states
this closes "exactly the predictions/result asymmetry that recurred
twice on this same T28 sub-thread" (R23's founding instance at exp-108;
the R23 First Addendum at exp-111). That characterization is not false as
a statement about source code — the assert genuinely exists, in text, at
that line — but it is unverified as a statement about the *program's
actual behavior*: per Attack 1, `analyze.py` crashes 37 lines before
reaching it, so as of this Phase-2 audit that assert has executed
successfully **zero times**. This is precisely the lesson the R23 First
Addendum (LOGBOOK, Iteration 88, exp-111) was ratified to teach: a
predictions/result assert pair must be confirmed to *actually fire on
real invocation*, not merely confirmed present in source, before Phase 3
credits the "both assert" claim as closed — that cycle's own
`finalize_88.py` exists for exactly this reason. This is a distinct
finding from R23's own registered failure shape (this is not a case of
one side of the pair being *absent* — both sides are textually present,
unlike exp-108/exp-111) — it is a new, adjacent risk: a code-level check
whose own file cannot currently execute at all. Filing this as "closed"
in a Phase-3 synthesis before Fix 1 lands and is verified by actual
end-to-end execution would repeat, in substance, the exact "claimed
closed, never actually invoked" pattern this sub-thread has now named
twice.

## 3. Mandatory-fix docket

| # | Fix | Owner-critique(s) | Attack | Cost |
|---|---|---|---|---|
| 1 | Resolve the `run`/`run` module-name collision in `chunk_runner.py` and `analyze.py`. Minimum sufficient repair: give the two colliding files genuinely distinct basenames (simplest — e.g. rename exp-112's own `run.py` → `run112.py`, update both downstream files' imports accordingly) *or* load the second one via `importlib.util.spec_from_file_location(...)` under a distinct `sys.modules` key. Either way, add an executed identity/attribute assertion (e.g. `assert R is not R110`, or `assert hasattr(R, "geom_fixedabs_cpl")`) in both files, run before any function relying on the distinction is trusted. Verify sufficiency by ACTUALLY re-running `python3 chunk_runner.py 156 25 empty` end-to-end past the geometry line, and `python3 analyze.py` (once all 3 captures exist) through to `results.json` — not by re-reading the diff. | THERMODYNAMICS | 1, 5 | Zero FDTD, code-only |
| 2 | Correct §2.1/Idealizations: state plainly that `ABSORB`/`EDGE` scaling does NOT carry the same resolution-invariance proof `tau_shell`/`sigma_max` does. Compute and disclose, in committed text (not merely in a critique), the sponge's one-way accumulated log-attenuation at both `cpl=20`/`absorb=40` and `cpl=25`/`absorb=50` (either the closed-form continuum route, `-13.26`→`-16.57`, or the discrete cell-sum route, `13.93`→`17.24` — state which convention and cite the formula), and disclose explicitly that both sit orders of magnitude below the `~1e-4`-`1e-3` measurement-floor scale — non-fatal, now an actual number rather than a vague "not independently re-derived." | MATERIALS, ELECTROMAGNETISM (independently convergent) | 2 | Zero FDTD, pure arithmetic |
| 3 | Add a zero-marginal-FDTD-cost bin-neighborhood cross-correlation (or ±2-bin-window ratio) check on the `peccored`/`hollow` delta pattern around `NAMED_BIN_IDX`, computed at both `cpl=20` (already-committed) and `cpl=25` (once Fix 1 lands and Phase 4 runs); require a stated bar (e.g. correlation ≥0.5) before any future document may cite a Check-A SURVIVES reading as "candidate real structure" rather than "not yet ruled out." | PHOTONICS | 3 | Zero FDTD |
| 4 | Append one disambiguating clause to `DISCLAIMER` itself: *"'detection floor' throughout this document means the K=3/K=1 mirror-pooled-floor instrument's own grid-discretization SNR threshold — not a human perceptual or observer-detection threshold; no constraint-2/3 claim is made or implied by this term."* | VISION | 4 | Zero FDTD, one sentence |
| 5 | Before Phase 3 credits Fix 1 or R23 compliance as closed, re-verify BOTH `assert DISCLAIMER in ...` calls (predictions-side and result-side) by actually executing `analyze.py` end-to-end post-Fix-1, confirming `results.json`'s `predictions_text`/`result_text` fields both contain the (Fix-4-updated) `DISCLAIMER` verbatim — matching this program's own `finalize_88.py`-style verification discipline (LOGBOOK, R23 First Addendum). Do not carry forward VISION's own "closes... the asymmetry" language as settled until this executes for real. | Red Team (own finding) | 5 | Zero FDTD, one script run |
| 6 | *(Recommended, not mandatory — THERMODYNAMICS' own explicit framing: "does not change the verdict.")* Persist `sigma_abs`/`sigma_ext` for both hollow and peccored captures, both `cpl`, into `results.json` (already computed in-memory inside `analyze.py`'s own `w_p`/`w_h` dicts). Not load-bearing for this cycle's own scored checks; needed by any future cycle attempting a genuinely physical, not merely statistical, interpretation of the named bin. | THERMODYNAMICS | — | Zero FDTD |

## 4. Disclosed overrides

**No opposition overrides.** All five blind Phase-2 critiques land
support-with-changes; I independently confirm all five underlying
findings are real, and none is fatal to this cycle's own stated,
deliberately modest purpose (a single-resolution-point noise-floor spot
check, explicitly not claiming continuum convergence). No finding here
rises to outright reject.

**One disclosed upgrade, not a downgrade, of a critique's own framing.**
PHOTONICS' own text ties escalation to opposition only to a *future*
misuse ("if... that reading is then carried into any future document's
prose as evidence of genuine physics") and states its own verdict stands
support-with-changes without the fix, scoped as disclosed. Red Team
elevates PHOTONICS' own recommended check to a **mandatory** fix now
(Docket #3) rather than a contingent future one — it is genuinely
zero-marginal-cost once Fix 1 lands, and this sub-thread's own R13/R14/R17
lineage consistently favors building an affordable discriminating
instrument immediately over deferring it pending a hypothetical future
misuse. This is a disclosed strengthening, not an override of substance.

**No override of THERMODYNAMICS', MATERIALS', ELECTROMAGNETISM's, or
VISION's own primary findings** — all four adopted in full, each
independently re-derived from primitives above and confirmed exactly as
each critique stated. THERMODYNAMICS' own secondary/informational
finding (Docket #6) is adopted at the severity THERMODYNAMICS itself
assigned it (recommended, non-blocking) — a disclosed non-elevation, not
a suppression, matching THERMODYNAMICS' own explicit words.

## 5. New standing rule candidate — recommended R29 (proposed by Red Team's Phase-2 audit; ratification is the Director's Phase-3 act, per this registry's own R23/R27 precedent for Red-Team-originated rules)

**R29 (candidate) — when two different files sharing an identical base
module name are both imported via bare `import <name>` statements inside
the same process, Python's `sys.modules` cache silently binds EVERY
subsequent `import <name> as <alias>` to whichever file resolved first on
`sys.path`, regardless of how many distinct aliases the source code uses
to try to tell them apart. A cycle that imports a same-basename module
from more than one directory must either (a) give the colliding files
genuinely distinct basenames, or (b) load the second one via
`importlib.util.spec_from_file_location(...)` under a distinct
`sys.modules` key — and in either case must verify, by an EXECUTED
identity or attribute check run before any function relying on the
distinction is trusted, that the intended distinct module object is
actually bound.** This is a genuinely new failure shape, not a
recurrence of any rule currently on file (checked element-by-element
against R1-R28's own operative text — closest analogues, R18's
"documented scope vs. actual source" and R6's "ground-truth-recovery
before trust," neither literally covers an import-cache collision).
Recurrence risk is concrete, not hypothetical: this exact "import a prior
cycle's `run.py` as `R<iteration>`, this cycle's own `run.py` as `R`"
idiom is now an established convention across at least two consecutive
T28 cycles (exp-110→exp-111's `import run as R` pattern; exp-111→exp-112
repeats the identical two-file naming shape that collided here) — a
future cycle reusing this idiom a third time is likely absent this rule.
**Founding instance: exp-112 (this cycle) — caught cleanly at Phase 2,
before any `Sim.run()` call, by direct execution (THERMODYNAMICS' own
critique, independently confirmed here). Does not fire on its own
founding instance**, matching every prior rule in this registry. **Rule,
forward: a second instance of this exact collision shape, on this or any
channel, after this rule is on the books, fires Checkpoint criterion 4
automatically** — a single-instance-ratified, forward-firing model,
matching R16/R21-R28's own precedent.

## 6. Checkpoint criteria — checked element-by-element against PANEL.md's own text

**Criterion 1 (a configuration passes ALL constraint metrics):** does not
fire. No constraint metric is scored this cycle; T1 is structurally N/A.

**Criterion 2 (a proven mechanism-class boundary):** does not fire. This
is pure grid-resolution instrumentation on a noise-floor question; no
mechanism class is bounded or ruled out.

**Criterion 3 (synthesis requires engine physics beyond validated bench
classes):** does not fire. Zero `lab/` diff; `geom_fixedabs_cpl` is a
pure-Python geometry-scaling generalization of an already-validated
family, verified byte-exact to the existing `geom_fixedabs` at `cpl=20`.

**Criterion 4 (Red Team flags program-integrity drift — unfalsifiable
claims, a constraint quietly dropped, especially #3):** **does NOT fire
this cycle**, ruled explicitly, checked against each of the five
findings individually and against R1-R28's own registry:

- The module-collision bug (Attack 1/5) is serious — it currently makes
  the cycle's own headline execution pipeline non-functional — but it was
  caught cleanly at Phase 2, before Phase 3 synthesis, before any
  `Sim.run()` call, before any results.json existed, by a blind critique
  that actually executed the code. This is Phase 2 review functioning
  exactly as PANEL.md designs it to, not drift. It also fails to match
  any existing R-rule's "known, named, ignored" recurrence bar (there is
  no prior instance of THIS collision shape on file) — it is a genuinely
  new failure category, addressed above as a recommended new standing
  rule (R29) precisely so that a *second* instance would fire. A single,
  cleanly-caught, same-shift-fixable founding instance does not, by this
  registry's own unbroken and repeatedly-applied precedent (R5 through
  R28 all "do not fire on their own founding instance").
- The ABSORB/EDGE non-invariance (Attack 2), the missing
  cross-correlation check (Attack 3), and the "detection floor" ambiguity
  (Attack 4) are each real but non-fatal, disclosed-and-being-corrected
  gaps, not claims that reached a frozen record undisclosed. No
  constraint is "quietly" dropped by any of them — constraint-3 is not
  engaged by this document at all (T1 N/A, confirmed structurally), so
  there is no constraint-3 claim in play to quietly drop; VISION's own
  finding is precisely the kind of vigilance that PREVENTS a future
  quiet drop, not evidence that one occurred.
- None of the five findings constitutes an "unfalsifiable claim" as
  filed — every prediction in `phase1_proposal.md` remains falsifiable
  in principle; Attack 1's bug makes the pipeline *currently unable to
  run*, which is a different defect (a blocked test, not an untestable
  one) and is fully remediable by Docket Fix 1 before any Predictions
  freeze.

**Criterion 5 (two consecutive iterations with no logbook-advancing
result):** not evaluable at Phase 2 (this is a Phase-5/LOGBOOK-entry
determination). Flagged for the Director's attention: Iteration 88
(exp-111) was a zero-new-FDTD governance/instrumentation cycle; if
Docket Fix 1 is NOT applied before Phase 4 and this cycle also produces
zero new FDTD data, Iteration 89 would be the second consecutive cycle
without a genuinely new physical result — a real, avoidable risk this
audit's own mandatory Fix 1 exists specifically to prevent, since the
underlying bug is small, already fully diagnosed, and fixable within the
same shift. This is a reason Fix 1 must land before Phase 3 freezes
Predictions, not merely a code-quality nicety.

**Ruling: zero Checkpoint criteria fire this cycle**, contingent on the
mandatory-fix docket (§3) being applied before Phase 4 executes for real.

## 7. Overall verdict

**PROCEED-WITH-MANDATORY-FIXES.**

The underlying instrumentation design is sound and, where checkable
independently of the module-collision bug, genuinely verified: geometry
identity to the frozen `cpl=20` baseline is byte-exact (confirmed by
direct execution, both r); the cost gate correctly and conservatively
scopes this cycle to r=156-alone (confirmed by direct invocation of the
real, unmodified `R.cost_gate_check`); `tau_shell`/`sigma_max`'s
resolution-invariance is provably correct; every numeric grounding claim
in `phase1_proposal.md` §2.0 reproduces exactly from primitives — this is
not a cycle riddled with fabricated or hand-typed figures. But Fix 1 is a
**hard blocker**: as committed, `chunk_runner.py` and `analyze.py` cannot
execute a single line of real FDTD work, confirmed by direct execution,
and Phase 3 must not freeze Predictions against a pipeline that cannot
run. All six items in the mandatory-fix docket are cheap (zero or
near-zero marginal FDTD cost), independently owned by name, and
same-shift-fixable — none requires new engine physics, none touches
`lab/`, and none moves any constraint verdict. Once Fix 1 lands and is
verified by actual re-execution (not by re-reading the diff), this cycle
is fully able to deliver the genuine new `cpl=25` data it exists to
gather.

**Verdict summary for the Director:** 6 mandatory fixes (5 required
before Phase 4 executes for real, 1 recommended/non-blocking), 1 new
standing rule recommended for ratification (R29), zero Checkpoint
criteria fire, zero opposition overrides, one disclosed upgrade
(PHOTONICS' own conditional fix elevated to mandatory).
