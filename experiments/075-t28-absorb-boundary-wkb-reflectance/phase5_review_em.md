# PHASE 5 — REVIEW · ELECTROMAGNETISM · Panel Iteration 52 (exp-075)

*Fresh sub-agent, ELECTROMAGNETISM charter (PANEL.md seat 3, verbatim):
"field/wave behavior, impedance matching, energy coupling. Owns the
reciprocity / passivity / causality bookkeeping — formalizes what T1
permits and forbids for each proposal." T1 is N/A this cycle
(instrument-fidelity work, constraint 3 not engaged, confirmed against
`phase1_proposal.md` §4 and `phase2_redteam_audit.md` §0). Blind to the
other five Phase-5 reviewers and to Red Team's own Phase-5 final audit.
Read PANEL.md, LOGBOOK.md in full, this cycle's complete record
(`phase1_proposal.md` with its `[PHASE-3 FIX]` corrections,
`boundary_reflectance.py`/results, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`,
`two_wall_cavity.py`/results, `phase4_results.md`, `NOTES.md`) and
`lab/fdtd2d.py` before writing anything below.*

---

## 0. Verdict: **PARTIAL** (not PROMISING, not RULED OUT)

This cycle's overall finding — "both boundary-reflectance-echo
mechanisms (single-wall and the correctly-derived two-wall cavity) are
REFUTEd" — is **not earned as robustly as `NOTES.md`'s Learned section
and `phase4_results.md`'s headline claim.** The transfer-matrix
derivation, the passivity-adjudicated branch resolution, the two-wall
geometry correction, VISION's ABSORB-depth cross-check, and the
look-elsewhere discipline on PHOTONICS' `nx`-substitution match are all
genuinely well-executed EM/optics physics — I would not overturn any of
those individually. But my own independent re-verification (§2, below)
shows that **Test A's own "boundary-pinned, no-completed-oscillation"
REFUTE — the test that alone determines the Combined Verdict via the
pre-registered `REFUTE if EITHER test REFUTEs` rule, for BOTH mechanisms
— is not robust to the cross-module phase-convention gap my own Phase-2
critique flagged, contrary to what my own critique argued and what Red
Team's audit and Phase 3 both, without independently testing it, treated
as settled.** This is the exact scenario the task's own framing warns of:
the gap I found at Phase 2 is now MORE load-bearing than Phase 3
characterized it — not merely "load-bearing the moment a second echo term
is built" (Phase 3 §3.4's framing, about the two-wall model specifically)
but load-bearing for the ALREADY-SCORED single-wall model too, which
Phase 3 treated as settled and did not re-open.

Not RULED OUT: nothing here revives either mechanism as an explanation for
T28, and under neither tested convention does either mechanism reach
SUPPORT. Not PROMISING: this cycle's own physics does not advance T28's
substantive mechanism question, and my finding is a *negative* result
about the cycle's own methodology, not a positive lead. PARTIAL is the
honest bucket: real, verified narrowing on several fronts, sitting next to
a genuine, outcome-determining, unresolved measurement-convention gap on
the test that carries the headline conclusion.

---

## 1. What I independently re-derived, and why (R4)

My own Phase-2 critique (`phase2_critique_em.md`, this cycle) found and
confirmed numerically that (a) the two candidate `n(x)` branches are exact
pointwise complex conjugates, yet feed into `reflection_coefficient()`
with a ~5-order-of-magnitude `|r|` gap because the `Zin` recursion's own
`1j` factors are not conjugation-covariant — a real, load-bearing
convention artifact, not a physical fact; and (b) testing the obvious
candidate fix (`r → conj(r)`) on Test B does NOT flip its sign
(`r: −0.508 → −0.542`). I stopped there at Phase 2, correctly scoped to
what my own critique could support in the time available, and rated the
gap **informational-only for that cycle** — matching Red Team's own
adjudication (`phase2_redteam_audit.md` §2c: "PARTIALLY CONFIRMED /
NARROWED... Combined Verdict REFUTE does not depend on it... bind forward
for any future cycle that builds a second wall-echo/cavity variant").

Phase 3 (`phase3_synthesis.md` §3.4) then built exactly that second echo
term (the two-wall cavity) and re-examined my gap — but its own
mitigation only addressed **whether the mismatch enters the two echo
terms differentially** ("whatever convention relationship exists...
enters both echo contributions the same way rather than differentially —
the two-wall model does not introduce a NEW convention-mismatch risk
beyond what the already-tested single-wall model already carries"). That
argument is correct as far as it goes, but it answers a *different*
question than the one that matters for the headline verdict: it says the
mismatch is symmetric between the two new terms, not that the mismatch —
present in EITHER model — leaves the REFUTE conclusion unchanged. Nobody
in this cycle's record actually re-ran Test A (the test that alone
determines Combined Verdict here) under the alternate convention, for
either model. EM's own Phase-2 critique only checked the alternate
convention against Test B's correlation, and only for the single-wall
model.

**I built and ran that check myself** — the "fourth, convention-agnostic
gate" my own Phase-2 critique named as the change that would flip my
verdict to unqualified support, run here in its cheapest, most direct
form (recompute the actual coherently-summed model under `r → conj(r)`,
re-run the SAME `_free_period_search`/Pearson-r machinery this cycle's own
committed scripts use, unmodified) rather than the full independent
finite-difference re-derivation I originally proposed, which is a larger
Iteration-53 item (§4 below).

## 2. Independent re-verification: results

**Method.** Loaded `boundary_reflectance.py` and `two_wall_cavity.py` as
committed, unmodified. Recomputed the predicted `delta(theta)` curve for
both the single-wall and two-wall models under four conventions for the
complex weight applied to each image term: `committed` (as shipped),
`conj` (r → conj(r), the specific candidate my own Phase-2 critique
tested against Test B only), `neg` (r → −r, a pure sign flip — not a
time/phase-convention question, included as a discriminating control),
and `neg_conj` (both). Re-ran the exact imported `_free_period_search`
(from `experiments/069/run.py`, the same function `boundary_reflectance.py`
and `two_wall_cavity.py` already import) and the same Pearson-r² shape
test, on the real `block_dense.rows` data, unchanged.

**Cross-validation of my own script, before trusting any new number**: my
`conj` run reproduces the single-wall model's already-published Test B
figures (`phase2_critique_em.md`, `phase2_redteam_audit.md` §2c) to 4
significant figures — `r=−0.5422` here vs. `−0.5422`/`−0.542` in the
record — confirming my re-implementation is computing the same quantity
the record already vetted, not a divergent script.

**Single-wall model (`boundary_reflectance.py`, `c_empty_with_wall`):**

| convention | `P_model` | `R²` | at search boundary? | `rel_dev` | Test A verdict |
|---|---|---|---|---|---|
| committed | 15.0000° | 0.8587 | **yes** | 4.2778 | REFUTE |
| conj | **3.9260°** | 0.5825 | **no — interior optimum** | **0.3814** | **INCONCLUSIVE** |

**Two-wall-cavity model (`two_wall_cavity.py`, `c_empty_two_wall`):**

| convention | `P_model` | `R²` | at boundary? | `rel_dev` | Test A verdict | shape `r²` | Pearson `r` |
|---|---|---|---|---|---|---|---|
| committed | 15.0000° | 0.9062 | **yes** | 4.2778 | REFUTE | 0.3042 | −0.5516 |
| conj | **4.1211°** | 0.5823 | **no** | **0.4500** | **INCONCLUSIVE** | 0.2919 | −0.5403 |
| neg | 15.0000° | 0.9068 | yes | 4.2778 | REFUTE | 0.3034 | **+0.5508** |
| neg_conj | 4.1211° | 0.5858 | no | 0.4500 | INCONCLUSIVE | 0.2911 | +0.5395 |

**Reading.** Across every combination tested, the qualitative Test A
outcome bifurcates cleanly on ONE bit: whether `r` is conjugated, not
whether it is negated. `neg` alone (a pure sign flip, not a genuine
convention question) changes nothing material — REFUTE survives, exactly
as EM's own Phase-2 critique implicitly assumed a "phase issue" would have
to look like. But `conj` — the specific, physically-motivated candidate
for a genuine time/phase-convention mismatch between this cycle's
transmission-line-formula module and exp-048's independently-authored
Huygens-Fresnel propagator, and the ONE alternate this program's own
history (T21's own "fourth, undisclosed implementation choice," Iteration
19, LOGBOOK.md, a real bug of exactly this class in this exact propagator
family) says is a live risk, not a hypothetical one — turns Test A's
"never completes an oscillation, pinned to the search boundary" REFUTE
into a genuine interior-optimum fit landing squarely in the
**pre-registered INCONCLUSIVE band** (`0.30 < rel_dev ≤ 1.00`), for BOTH
models. Under `conj`, neither test REFUTEs and neither SUPPORTs for the
two-wall model (`period rel_dev=0.45`, `shape r²=0.29`, both short of
their own bars) — so the pre-registered combining rule (`REFUTE if EITHER
REFUTEs; SUPPORT iff BOTH SUPPORT; else INCONCLUSIVE`) would score the
two-wall model's **Combined Verdict as INCONCLUSIVE, not REFUTE**, under
this equally-plausible, gate-untested convention. The same is true of the
single-wall model, whose committed REFUTE rests on Test A alone
(`rel_dev=4.28`) exactly as much as the two-wall model's does.

**Why the G-PASSIVITY gate cannot catch this.** `|conj(r)| = |r|`
identically — the passivity gate (`|r|≤1`) is a pure magnitude test and is
mathematically blind to conjugation by construction. It correctly kills
the OTHER branch ambiguity in this cycle's derivation (`n=1+iν/ω`, which
fails passivity by orders of magnitude, §2b of `phase1_proposal.md`) —
that resolution is sound EM physics and I do not question it. But it
provides zero discriminating power on the SEPARATE ambiguity my own
Phase-2 critique raised (cross-module phase referencing), because that
ambiguity, by its nature, cannot violate a magnitude-only conservation law
in either direction. **Passivity constrains |r|; it says nothing about
arg(r)'s reference convention relative to a second, independently-built
module — these are different EM bookkeeping questions, and only the first
was actually settled here** (see §5, seat-specific finding, for why this
distinction is exactly this seat's charter business).

**A precise correction to my own Phase-2 reasoning, found only by running
this.** My own critique's §3 argued Test A's REFUTE "is not premature on
the period axis" because "idealization 4 (vacuum-Snell oblique
substitution)... perturbs the reflection phase/magnitude at a given
angle, not the interferometer baseline `2·PLANE_X` that sets the period
scale itself" — true of the CLOSED-FORM period estimate in §2e/§8 (which
literally drops `arg(r(θ))`'s θ-dependence, `P_wall(θ)=(180/π)λ/(2·PLANE_X·
sinθ)`, a zero-order approximation stated as such), but **not true of the
actual numerically-fit `P_model` Test A is scored on**, which uses the
full coherent sum including `r(θ)`'s own θ-varying phase. Over the tested
36°–42° window, `arg(r(θ;40))` swings roughly 77° (§2d of
`phase1_proposal.md`: −78.1° at 36° to −1.2° at 42°) against a geometric
phase excursion of order 180° over the same window (back-solved from
`P_wall(39°)≈11.8°` at ABSORB=40) — a ~40% contribution, not negligible.
I conflated the closed-form diagnostic with the scored numeric quantity in
my own Phase-2 critique; this review corrects that in place, per this
program's own R4 discipline applied to my own prior output, not just to
others'.

## 3. Does this change what T28 is? No. Does it change what this cycle
## proved? Yes.

Nothing here revives the single-wall or two-wall echo mechanism as an
actual explanation for T28's ~2.84° family — under EVERY convention
tested, including the untested `conj` alternate, neither model reaches
SUPPORT (best shape `r²` obtained, 0.294, still under the 0.30 bar; best
period `rel_dev`, 0.38, still outside the 0.30 SUPPORT band). T28's
substantive mechanism question is exactly as open after this review as
before it. **What changes is the epistemic status of "REFUTE."** As
committed, both models REFUTE cleanly and (per Red Team's own audit) the
REFUTE was independently reconfirmed six ways and judged robust to every
other flagged gap. My finding adds a seventh check Red Team's own audit
did not run (§2c explicitly deferred it: "does not resolve EM's actual
concern... narrows where a bug, if any, could live... without finding or
ruling one out in the composition step") and it is NOT robust: under a
specific, well-motivated, gate-untested alternate convention, Combined
Verdict for BOTH models drops to INCONCLUSIVE. The correct standing
claim, until the phase convention is independently pinned (§4, item 1), is
**"REFUTE under the as-implemented convention; genuinely unresolved
(neither REFUTE nor SUPPORT) under an equally-plausible untested
alternate this program's own gates cannot distinguish"** — not the flat
"REFUTE, both mechanisms" `NOTES.md`'s Learned section currently states.

## 4. Ranked top-3 Iteration-53 candidates

**(1) [NEW, this review] Pin the cross-module phase convention with an
independently-derived, convention-agnostic gate — promoted from
"informational, bind forward" to a MANDATORY, blocking fix, per §2's
finding that it is outcome-determining for the Combined Verdict of BOTH
models already scored this cycle, not merely a risk for future work.**
Concretely: (a) my own Phase-2 critique's originally-proposed check —
re-derive `r(θ;ABSORB)` by directly time-stepping the STATED continuous
ODEs (`dE/dt=cdH/dx−νE`, `dH/dt=cdE/dx−νH`) to steady state on the same
per-cell profile, rather than via a second closed-form instance of the
same transmission-line formula, and compare PHASE, not just magnitude,
against the committed `r(θ)`; (b) separately and more directly: validate
`r(θ)`'s phase convention against `lab/fdtd2d.py`'s own actual, documented
convention — `add_line_source`'s docstring names `emit._phasor`'s
`f(n)=Re{F e^{-iωn}}` as this engine's real steady-state phasor
convention (Iteration 35's phase-variance machinery, LOGBOOK.md) — the
one ground truth this whole analytic exercise is trying to approximate,
never checked against here. This is zero-to-near-zero FDTD cost (reuses
`Sim.__init__`-only machinery already imported this cycle) and directly
closes the exact gap class this program has already been burned by once
(T21's "fourth, undisclosed implementation choice," Iteration 19). Until
it lands, any LOGBOOK citation of this cycle's REFUTE should carry the
caveat this review documents.

**(2) G40/`PAD` decorrelation (PLAN.md's own already-queued Iteration-52
item 2, ~31 FDTD calls) — still the right next FDTD spend, unaffected by
my finding.** This is a genuinely different (causal, real-FDTD)
instrument class from the desk analytic propagator my finding concerns —
it does not touch `reflection_coefficient()` or exp-048's propagator at
all, so it is not vulnerable to the phase-convention gap either way. Given
this cycle's REFUTE is now shown less settled than claimed, the case for
pursuing an orthogonal, causal-manipulation route to T28's actual
mechanism (rather than resting on the analytic model's unresolved
verdict) is, if anything, slightly strengthened, not weakened.

**(3) Record-hygiene bundling (PLAN.md's own already-queued Iteration-52
item 3), extended to capture this finding specifically.** Beyond the
already-scoped items, add: the phase-convention robustness table above
(or a re-run, committed version of it) as a disclosed caveat on
`NOTES.md`'s Learned section and `phase4_results.md`'s headline, per this
program's own erratum-in-place convention (T10's precedent) — flag, don't
silently rewrite, matching how this cycle itself already handled the
Test-A-boundary-artifact and Test-B-sign-significance corrections at
Phase 3.

I do not rank PHOTONICS'/MATERIALS'/QUANTUM's/VISION's own Phase-2
follow-up items (the multiple-internal-bounce bound, further
realizability scoping, etc.) above these three from my own seat's
charter — they are real but lower-stakes than an unresolved,
outcome-determining convention gap on the test that carries this cycle's
headline number.

## 5. Seat-specific finding: passivity bounds magnitude, not phase — and
## this cycle's own text quietly leans on it for more than it gives

This is the one place a general-purpose read would miss what an EM
charter should catch. `phase1_proposal.md`'s Idealization 2b resolves a
genuine sign/branch ambiguity by an "unambiguous physical requirement"
(passivity, `|r|≤1`) and is explicit, correctly, that this is a magnitude
statement. But the disposition of the SEPARATE cross-module phase
question — in my own Phase-2 critique, in Red Team's audit (§2c: "not in
the proposal or any of the five critiques... does not resolve EM's actual
concern"), and in Phase 3's mitigation (§3.4, "does not introduce a NEW
convention-mismatch risk... beyond what the already-tested single-wall
model already carries") — implicitly treats the passivity-adjudicated
derivation as having earned more confidence in the OVERALL reflectance
`r(θ)` than a magnitude-only energy-conservation argument can supply. This
is a first-principles EM distinction, not a stylistic quibble: passivity
(`|S|≤1` for a scattering quantity) and a phase/causality reference
convention (which branch of a time-harmonic ansatz two independently-coded
modules agree to use) are orthogonal constraints — Kramers-Kronig-style
causality relations bound how `arg(r(ω))` may vary WITH frequency at fixed
convention; they say nothing about which convention two separately-derived
complex quantities were computed under before being coherently summed.
Nothing in this cycle's three sanity/passivity gates (`G-LOSSLESS`, `G-N1`,
`G-PASSIVITY`) tests convention-matching, by design — they were built
(correctly, for their own stated purpose) to catch bugs in the
transfer-matrix code's own internal consistency, not to certify its phase
against an external module. Reading "we resolved this by an unambiguous
physical principle" as closing the ambiguity generally, rather than
closing exactly the one branch question it was built for, is the specific
misreading a general-purpose review would not be positioned to catch, and
is what let the cross-module gap ride as "informational" through two
further phases of work on data it demonstrably determines.

**Secondary, lower-priority note, not run this cycle**: this cycle's
charter language also names reciprocity. The derived `r(θ;ABSORB)`
comes from an ordinary (non-gyrotropic, non-magnetized) matched-`ε=μ`
stratified medium backed by a PEC short — such a structure is reciprocal
by construction (no time-reversal-symmetry-breaking element anywhere in
the model), so I see no reciprocity violation to report, and did not find
the two-wall composition (§3.3 of `phase3_synthesis.md`, same `r(θ)` for
both walls, justified by the scene's own mirror symmetry) introducing one.
Flagged as checked-by-inspection, not by a dedicated computed test — a
much smaller open item than §2's phase-convention finding, not competing
with it for Iteration-53 priority.

---

## Reproduction

The two verification tables in §2 were produced by two standalone scripts
(not committed to this directory, per the task's own scope — this is a
Phase-5 review, not a new experiment cycle) that import
`boundary_reflectance.py`/`two_wall_cavity.py` unmodified and recompute
`c_empty_with_wall`/`c_empty_two_wall` under `r → conj(r)` (and, for the
two-wall model, `r → −r`/`−conj(r)`) in place of the committed `r`,
re-running the SAME imported `_free_period_search`/Pearson-r code the
committed scripts already use, on the same real `block_dense.rows` data.
Bit-exact match to the `committed` row in both tables against
`boundary_reflectance_results.json`/`two_wall_cavity_results.json`
confirms correct reuse of the existing machinery; bit-exact match of the
single-wall `conj` row's shape statistics against `phase2_critique_em.md`
and `phase2_redteam_audit.md` §2c's already-published `−0.542`/`−0.5422`
confirms the script is computing the quantity the record already vetted,
not a divergent one.
