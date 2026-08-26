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

**Combined Verdict: REFUTE, both mechanisms.** The frozen primary
prediction is CONFIRMED, with margin: the two-wall model's Test A REFUTEs
identically to the single-wall model's own boundary-search-artifact
result (`P_model=15.0000°`, `rel_dev=4.2778`, bit-identical). Test B's
raw `r²=0.3042` nominally clears the pre-registered SUPPORT band (unlike
the single-wall model's own `0.2586`), but the mandatory circular-shift
null-calibration check (`N=20,000`, R6-style order-preserving) shows this
is NOT statistically significant against the real data's own known
autocorrelation structure (`p=0.1953`) — real information, not evidence
for the mechanism. PHOTONICS' `nx`-substitution match is confirmed, as
predicted, to have been the look-elsewhere artifact Red Team's own audit
flagged it as being at risk of: the actual physically-derived two-wall
model does not reproduce it. Full detail: `phase4_results.md`.

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
mechanism classes are now ruled out on this instrument; the mechanism
itself remains open.

## Next

See PLAN.md's Iteration-53 queue (Phase 5's six blind reviews +
Red Team's final audit, this directory's `phase5_*.md` files) for the
next ranked candidates — completed and recorded after Phase 5 closes this
cycle.
