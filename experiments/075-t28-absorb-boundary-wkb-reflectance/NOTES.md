# exp-075 — the `ABSORB` boundary band's own reflectance: single-wall and two-wall-cavity echo mechanisms, both REFUTEd

**Panel Iteration 52.** Lead: THERMODYNAMICS (by rotation). Director
synthesis post Phase 2 (five blind critiques + Red Team's audit, verdict
PROCEED-WITH-MANDATORY-FIXES, five-item docket, **zero items overridden** —
full record in `phase1_proposal.md`, `phase2_critique_{photonics,
materials,em,quantum,vision}.md`, `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `phase4_results.md`).

## Mandate

PLAN.md's Iteration-52 queue, item 1 (near-unanimous #1 across all six of
exp-074's Phase-5 seats): PHOTONICS' analytic WKB/adiabatic boundary-
reflectance model for the graded-loss `ABSORB` band — zero new FDTD, the
explicit "qualitatively different strategy" exp-074's own seventh-cycle
rule requires before any further work on live thread T28 (the real,
unresolved ~2.84° `C80−C40` periodicity, opened Iteration 46). Either
explain T28 as an ordinary boundary-reflectance phase effect or rule it
out, narrowing the remaining space.

## Setup

**Phase 1** (THERMODYNAMICS, by rotation — the queue item's substantive
content is EM/PHOTONICS physics, executed per house precedent for a
cross-domain rotation lead): derived an effective complex index from
`lab/fdtd2d.py::Sim._damping`'s own per-cell arrays, resolved a genuine
sign/branch ambiguity via a passivity requirement, built an EXACT
recursive transfer-matrix reflectance `r(theta;ABSORB)` (not a truncated
WKB/Born integral — the band is only 2-4λ thick), and predicted a
coherent single-echo interference term via an extension of exp-048's own
committed Huygens-Fresnel propagator. Tested zero-cost against
experiments/069's real dense-sweep data. Self-scored Combined Verdict:
**REFUTE** (period ~4.3× too long; wrong-signed, inconclusive shape
match).

**Phase 2** (five blind critiques + Red Team): unanimous support-with-
changes (zero oppose). PHOTONICS found a same-cost, same-machinery
two-wall-cavity variant (the domain's OTHER PEC wall, never priced)
landing inside the proposal's own SUPPORT band on a naive closed-form
substitution. MATERIALS confirmed the model describes a matched-`ε=μ`
medium — a statement about the engine's own numerical construct, not
realizable optical coatings. ELECTROMAGNETISM found no gate tests
cross-module phase-convention consistency. QUANTUM found Test A's headline
number is a boundary-search artifact and Test B's wrong-signed `r²` is a
statistically significant anti-correlation. VISION flagged an un-run
`ABSORB`-depth residual cross-check against exp-074's own established
finding. Red Team's audit independently re-derived every claim
computationally, confirmed all five (sharpening two), ran its own
look-elsewhere check (2 of 11 named geometric constants also land in-band
under the same naive substitution — suggestive, not decisive), and ruled
PROCEED-WITH-MANDATORY-FIXES, five items, zero overridden.

**Phase 3** (this Director): adopted all five items. Executed mandatory
fixes 2-4 as in-place edits/new committed code; designed and pre-
registered the actual two-wall-cavity model (mandatory fix 1) — the
physically correct wall distances, not PHOTONICS' `nx` substitution —
BEFORE running it, with a frozen primary prediction (Test A REFUTEs
again) and a new circular-shift null-calibration robustness check per
Red Team's own instruction.

**Phase 5** (six blind reviews + Red Team's final audit): all six PARTIAL.
Two independent blind seats (PHOTONICS, ELECTROMAGNETISM), neither aware
of the other, found and confirmed the SAME load-bearing defect: under an
untested alternate phase convention (`r→conj(r)`, indistinguishable by
the program's own G-PASSIVITY gate), Test A's REFUTE collapses to
INCONCLUSIVE for BOTH models. Red Team's final audit independently
reproduced this from scratch, then RESOLVED it — a disclosed static
analysis that did not cleanly settle the question, followed by a new,
owned, empirical FDTD tie-breaker (reusing `lab.emit`'s own already-gated
machinery) that, at its one calibration-confirmed reliable operating
point (three angles, lossless + lossy), favors the committed convention
by 2.8×-6.7× margins. **Combined Verdict REFUTE STANDS for both
mechanisms.** Other findings adopted: VISION's independent 4/6
re-confirmation, QUANTUM's finding that `circular_shift_null` is
anti-conservative against synthetic AR(1)/phase-randomized data (does not
change the verdict — Test A alone REFUTEs), THERMODYNAMICS' minor sidecar
percentage fix, MATERIALS' `graded_black_shell` code-path-disjointness
confirmation, VISION's 750nm-leg suggestion.

## FROZEN PREDICTIONS (committed before Phase 4's official run)

Full specification: `phase3_synthesis.md` §3 — single source of truth,
not re-transcribed here (R4).

**Primary prediction:** the two-wall-cavity model's Test A REFUTEs again
— both walls' own correctly-derived closed-form periods (7.8°-15.4°) sit
far from `P*=2.8421°`, and no physical mechanism turns a beat of two such
components into a clean ~2.84° period.

**Falsification criterion:** Test A SUPPORTs AND the circular-shift
null-calibration p-value on Test B is ≤0.05 — stated as a
Checkpoint-2-adjacent finding if it occurred.

## Idealizations

See `phase1_proposal.md` §6 (nine items, two amended in place per
mandatory fixes 3-4) plus `phase3_synthesis.md` §3.3 (same-`r`-for-both-
walls justification, single-bounce-only bound, `|r|²≤4.1×10⁻⁵`).

## Result

**Combined Verdict: REFUTE, both mechanisms — confirmed robust by Phase 5.**
The frozen primary prediction is CONFIRMED, with margin: the two-wall
model's Test A REFUTEs identically to the single-wall model's own
boundary-search-artifact result (`P_model=15.0000°`, `rel_dev=4.2778`,
bit-identical). Test B's raw `r²=0.3042` nominally clears the
pre-registered SUPPORT band (unlike the single-wall model's own
`0.2586`), but the mandatory circular-shift null-calibration check
(`N=20,000`, R6-style order-preserving) shows this is NOT statistically
significant against the real data's own known autocorrelation structure
(`p=0.1953`) — real information, not evidence for the mechanism.
PHOTONICS' `nx`-substitution match is confirmed, as predicted, to have
been the look-elsewhere artifact Red Team's own Phase-2 audit flagged it
as being at risk of: the actual physically-derived two-wall model does
not reproduce it.

**A load-bearing question surfaced and resolved at Phase 5**: two
independent blind seats (PHOTONICS, ELECTROMAGNETISM) found that Test A's
REFUTE is convention-dependent — an untested alternate reflection-phase
convention (`r→conj(r)`, algebraically indistinguishable by the
program's own G-PASSIVITY gate) collapses REFUTE to INCONCLUSIVE for
BOTH mechanisms. Red Team's final audit built a new, owned empirical FDTD
measurement of the real reflected wave (reusing `lab.emit`'s own
already-gated machinery) and resolved the question, moderate-to-high
confidence: the committed convention is correct, by 2.8×-6.7× margins at
its one calibration-confirmed reliable operating point. **REFUTE stands.**
Full detail: `phase4_results.md`, `phase5_redteam_audit.md`.

## Learned

Two independently well-motivated, zero-free-parameter boundary-
reflectance-echo mechanisms — a single echo off the near wall, and the
correctly-derived two-wall cavity using both PEC boundaries — are now
REFUTEd against the same real dense-sweep data, closing the specific gap
Red Team's Phase-2 audit found open (an untested, same-cost variant that
looked promising on a first-pass estimate). The look-elsewhere risk Red
Team's own supplementary check raised is resolved in the direction that
check anticipated as plausible, not dismissed by assertion: the actual
model, run honestly against a frozen prediction that could have gone
either way, does not support the naive substitution's apparent match.

House-discipline notes: mandatory fix 2 (committing VISION's ABSORB-depth
residual cross-check as code, not audit prose) caught a same-cycle
arithmetic slip in Red Team's OWN write-up (its prose said "3 of 6 pairs
negative"; the correct count, verified by running the committed code, is
4 of 6) — R4 applied one level further than usual, to a Red Team audit's
own restated figure, exactly the class of gap R4's own addenda exist to
close. The circular-shift robustness check did genuine, load-bearing work
this cycle: without it, Test B's nominal `r²=0.3042` SUPPORT reading for
the two-wall model would have stood uncontextualized as an apparent
partial positive signal; the check showed it is not distinguishable from
the real data's own autocorrelation-driven chance level.

T28's own substantive mechanism question — the ~2.84° periodicity's
origin — is not answered by this cycle. Two boundary-reflectance-echo
mechanism classes are now ruled out on this instrument, on a convention
now independently confirmed correct; the mechanism itself remains open.

**CHECKPOINT criterion 4 fires** (11th time this program, unbroken
notification-not-pause precedent) — on a narrower basis than the
Iterations 49/50 precedent this exact criterion also fired on: the
published REFUTE conclusion is actually correct (nothing needs
correcting), but an UNVERIFIED robustness argument (EM's own Phase-2
claim that Test A was "robust to" the phase-convention gap) was adopted
verbatim by Red Team's Phase-2 audit and by Phase 3, in place of running
the exact check EM itself had already named — that argument was false,
and it took two independent blind Phase-5 seats to catch, one cycle after
R7 was adopted for the structurally analogous "pricing substituting for
fitting" failure. **New standing rule R8 adopted**: an unverified
robustness/independence argument about a flagged verification gap is not
sufficient to file it informational-only when an affordable named check
exists — the argument must be tested, not merely reasoned about. Ruled a
notification, not a pause (full ruling, all five Checkpoint criteria:
`phase5_redteam_audit.md` §5).

House-discipline notes, in addition to R8 and the mandatory-fix-2
arithmetic correction already logged above: QUANTUM's Phase-5 finding
that the new `circular_shift_null` robustness check is itself
anti-conservative against synthetic autocorrelated null data (does not
change the Combined Verdict — Test A alone REFUTEs regardless of Test B's
robustness reading) is a genuine, disclosed gap bound forward to
Iteration 53, not a defect corrected in place this cycle.

## Next

See PLAN.md's Iteration-53 queue (Red Team's Phase-5 final-audit
reconciliation of all six seats, `phase5_redteam_audit.md` §7):
(1) **G40/`PAD` decorrelation** (~31 FDTD calls) — near-unanimous #1,
the only queued item that relieves rather than discloses the standing
`ABSORB`-or-`PAD` confound, now the single most information-dense open
question on T28's board with the boundary-reflectance-echo class doubly
REFUTEd; (2) **score the already-built two-wall model against the
already-collected 750nm leg** (`block_leg750`, zero new FDTD) — cheap,
decisive, stress-tests this cycle's own REFUTE before it is cited
elsewhere as wavelength-general; (3) **harden the phase-convention
resolution to this program's own R6/G0-e standard** — extend
`phase5_redteam_phase_convention_check.py` to the real `ABSORB` depths
directly, diagnose the `K≥8` reliability degradation this audit disclosed
but did not fully resolve; (4) **record-hygiene bundle** (six items,
`phase5_redteam_audit.md` §7 item 4), including `caveat_lint_config.json`
entries for this cycle's own headline scope caveats and folding R8's
phase-convention caveat language into the permanent record.
