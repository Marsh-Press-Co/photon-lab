# Photon Lab — PLAN

Standard co-lab shared-repo file (AGENTS.md convention): Vision is the
owner's words, durable; Current state and Next work stay fresh — the PR
that does the work updates this file, never a separate chore.

## Vision (Marsh, 2026-08-08, in-session — verbatim)

> the vision i see is that we can simulate reality with precise mathmatics
> that should leave probability that an actual design would work the same
> in the real world. [...] i want you and bonnie to keep discussing and
> trying new ideas and experiments in a collaborative effort to create this
> cloaking material or color or whatever. my belief is that two independent
> agents can work together to design the material needed and test their
> hypothesis and from the results work out a new design and test those
> results and the loop continues.

Operating mandate (Marsh + Preston, on the record at co-lab #31): **the
agents drive experiment design and discussion; the humans seed ideas.**
The honest frame binds every claim: amateur astronomy, not NASA —
idealizations stated, limits observed in our own data, no cloak shipping
promised. The arc from 2D mechanism-truth toward real-world-plausible
designs runs: single-λ → broadband → 3D → tolerance-to-imperfection.

## Current state (2026-08-26, panel Iteration 53 done (exp-076, PARTIAL,
`OUTCOME=PAD_TIED`, no Checkpoint criterion fires — QUANTUM OPTICS lead
by rotation, executing PLAN.md's own Iteration-53 queue item 1
(near-unanimous #1 across exp-075's six Phase-5 seats): the G40/`PAD`
decorrelation build, the only queued item that relieves rather than
discloses or prices the `ABSORB`-or-`PAD` confound running under every
T28 causal claim since Iteration 48. Full five-phase cycle: Phase 1
proposed a fresh 31-call build of `G40` (`ABSORB=40, PAD=40`, already
specified in `experiments/065-.../design_geometry.py` but never run at
T28's own dense window) scored against the confounded-series baseline
with exp-072's own phase-invariant amplitude channel → five blind
Phase-2 critiques (unanimous support-with-changes: PHOTONICS caught
every config this cycle runs sits at an exact integer-λ boundary
thickness at 600nm, the aliased condition `C70` was added to guard
against in this identical sub-thread's own precedent cycle; MATERIALS
caught a broken `ABSORB`/`PAD` symmetry in the proposal's own decision
language; ELECTROMAGNETISM + VISION SCIENCE independently converged
that `G40`'s own thin-boundary/large-domain combination had never been
settling-tested at `STEPS≥2800`; THERMODYNAMICS caught a silently-
dropped energy-sidecar N/A disposition) → Red Team's Phase-2 audit
(PROCEED-WITH-MANDATORY-FIXES, 8 items, zero overridden; found two NEW
load-bearing defects itself — the proposal's own outcome bands were
neither mutually exclusive nor exhaustive, and its `rho_pad_absorb`
"interaction" diagnostic contradicted its own cited exp-072 precedent,
never once evaluated on real data in this program's history) → Phase 3
adopted all 8 items, rebuilt an exhaustive/mutually-exclusive 9-cell/
5-outcome scheme, added a HALT-if-fails settling precondition and a
16-call 750nm advisory leg (budget 31→50 calls), FROZEN PREDICTIONS
committed before any run → Phase 4 (50 FDTD calls; two disclosed pure
engineering/serialization bugs, zero physics impact, bit-identical
results across crashed and clean runs; settling precondition PASSED
~500-666x inside its bar): **official result `x=amp_ratio(PAIR_PAD)=
0.119366` (HIGH) > `y=amp_ratio(PAIR_ABSORB40)=0.071616` (MED) →
`OUTCOME=PAD_TIED`** — the confound is NOT relieved in the reassuring
direction; a 750nm advisory leg shows the opposite ordering, non-
decisive → six blind Phase-5 reviews (unanimous PARTIAL, an unusually
clean crop) → Red Team's Phase-5 final audit: formalized ELECTROMAGNETISM's
load-bearing finding that `PAD` is provably lossless vacuum (independently
re-derived from `lab/fdtd2d.py`'s primitive source) — so `PAIR_PAD`'s
entire signal can only be a phase/interference effect, never absorbed
power — combined with MATERIALS' realizability reading into the
cleanest negative signal this six-cycle T28 sub-thread has produced (the
dominant axis has no witness-scene analog AND is structurally excluded
from an entire class of physical mechanisms); adjudicated three small
process/documentation gaps (VISION's dropped Phase-2 finding, QUANTUM's
`G0-e` promise-vs-implementation gap, PHOTONICS' discarded 750nm carrier
diagnostic), all independently verified inert or closable, none firing
Checkpoint criterion 4, all closed same-shift via a 6-item mandatory-fix
docket. **No Checkpoint criterion fires.** T28's own mechanism question
remains open, doubly narrowed. Full record: `experiments/076-t28-g40-
pad-decorrelation/`, LOGBOOK.md Iteration 53); panel Iteration 52 done (exp-075, PARTIAL,
Combined Verdict REFUTE for both a single-wall and a two-wall-cavity
boundary-reflectance-echo mechanism, **CHECKPOINT criterion 4 FIRES**
(notification, not a pause; 11th time this program) — THERMODYNAMICS lead
by rotation, executing PLAN.md's own Iteration-52 queue item 1
(PHOTONICS' own queued WKB/adiabatic boundary-reflectance analytic model
for the graded-loss `ABSORB` band): Phase 1 built an exact transfer-
matrix reflectance for the `-x`-wall graded band and self-scored REFUTE
against T28's real dense-sweep data (period ~4.3x too long, wrong-signed
shape match) → five blind Phase-2 critiques (unanimous support-with-
changes) found PHOTONICS' own two-wall-cavity variant (the OTHER PEC
wall, never priced) lands inside the proposal's own SUPPORT band on a
naive substitution → Red Team's Phase-2 audit confirmed this exactly plus
its own look-elsewhere risk (2/11 named constants also land in-band) and
ruled PROCEED-WITH-MANDATORY-FIXES, five items, zero overridden → Phase 3
adopted all five, pre-registered the actual (correctly-derived) two-wall
model BEFORE running it → Phase 4 CONFIRMED the frozen prediction: the
two-wall model REFUTEs identically (bit-identical `P_model=15.0000°`),
closing the look-elsewhere gap — PHOTONICS' match confirmed as the
artifact it was suspected of being → Phase 5's own load-bearing finding:
two independent blind seats (PHOTONICS, ELECTROMAGNETISM) found Test A's
REFUTE is convention-dependent (`r→conj(r)` collapses it to INCONCLUSIVE
for both mechanisms, undetected by the program's own G-PASSIVITY gate);
Red Team's final audit built a NEW, owned empirical FDTD tie-breaker
(reusing `lab.emit`'s own already-gated machinery) and RESOLVED it,
moderate-to-high confidence, in favor of the committed convention (2.8x-
6.7x margins) — **REFUTE STANDS for both mechanisms**. Checkpoint fires
on the verification-discipline shape (an unverified "robust to" argument,
not a false claim about a checked computation, filed a real gap as
informational-only until two blind Phase-5 seats caught it) — new
standing rule **R8** adopted, generalizing R7 to untested independence
arguments. T28's own mechanism question remains open. Full record:
`experiments/075-t28-absorb-boundary-wkb-reflectance/`, LOGBOOK.md
Iteration 52); panel Iteration 51 done (exp-074, PARTIAL,
Combined Verdict `HALT_NULL_MISCALIBRATED_9COL`, no Checkpoint criterion
fires — ELECTROMAGNETISM lead by rotation, executing PLAN.md's own
Iteration-51 queue item 1 (near-unanimous #1 across all six of exp-073's
Phase-5 seats): "price the window" — decide, zero FDTD, whether
θ∈[36°,42°] can ever support a carrier-conditioned discriminator for
T28's `C80−C40` periodicity. Full five-phase cycle: Phase 1 (EM priced
the 9-column two-tone design's Gram-matrix conditioning without fitting
it — `cond9=529`, `VIF_Rq=36.6`, reproducing two informal exp-072 Phase-5
figures exactly across all four `ABSORB` pairs for the first time — and
claimed CLOSURE-CONFIRM, a binding formal-retirement decision rule for
the sub-thread "independent of which null eventually gates it") → five
blind Phase-2 critiques (two of five — PHOTONICS, THERMODYNAMICS, by two
independent methods — showed CLOSURE-CONFIRM does not survive:
PHOTONICS found it non-monotonic across the contaminant-period space the
proposal's own `L(T)` function flags as dangerous; THERMODYNAMICS
actually fit the real 9-column design, never done by the pricing-only
script, and found the true joint-fit significance EXCEEDS the
"optimistic upper bound" at 3 of 4 pairs, by up to 9.3× — a collinear
design's realized residual variance is not bounded below by a VIF-only
rescaling, false as linear algebra, not merely unlucky; QUANTUM
independently found the widened-window "4/4 clear 2σ" recommendation
omits an already-established SE-inflation correction that, applied,
drops it to 0/4; MATERIALS found a ~4× FDTD-cost-citation understatement;
VISION found three of five falsifiable bars unsourced) → Red Team's
Phase-2 audit (PROCEED-WITH-MANDATORY-FIXES, ten items, **zero
overridden** — independently re-derived every load-bearing claim from
all five critiques computationally before adjudicating, and added a
sixth finding of its own: new standing rule **R7**, generalizing R6 one
level upstream — a conditioning/VIF-based pricing of an un-fit design is
necessary, not sufficient, evidence for a closure or detection claim; the
design must be fit and null-calibrated) → Phase 3 synthesis (all ten
docket items adopted, zero overrides; withdrew §5/§6 of the Phase-1
proposal; adopted R7; designed `fit_and_calibrate.py` — the actual
9-column fit of `R_q`, gated behind a two-leg null-calibration test:
i.i.d. Gaussian, plus a NEW genuinely order-preserving circular-shift leg
built from each config's own real per-config residual, closing the exact
gap exp-073's own Phase-5 erratum flagged as queued for this iteration;
frozen predictions committed before the run, including an analytic,
pre-computed reason — `lev9_Rq=0.586–0.596`, lower/worse than exp-073's
5-column `0.79–0.80` — to expect a WORSE null-calibration failure than
exp-073's own 5-column precedent; a written seventh-cycle decision rule
per queue item 5) → Phase 4 (official run: `HALT_NULL_MISCALIBRATED_9COL`,
both frozen predictions confirmed with margin — i.i.d. leg fails
8.7×–11.2× nominal at α=0.01, worse than exp-073's 5.4×; the
circular-shift leg fails far worse, 38.9×–46.1×; `z9=5.03` at C60–C70
remains genuinely unresolved, no valid null yet exists to test it) → six
blind Phase-5 reviews (PHOTONICS/MATERIALS/EM/QUANTUM PARTIAL;
THERMODYNAMICS/VISION PROMISING, scoped identically as instrument-level;
four of six independently found a genuinely new fact unavailable at
Phase 2 — the four `ABSORB` configs' own residuals are near-identical
(r=0.992–1.000) and strongly θ-autocorrelated (lag-1≈0.92–0.94), a
shared curvature misspecification, not `ABSORB`-differential noise; two
seats' candidate causal story for the circular-shift leg's extra
severity (an independent-shift amplitude artifact) was falsified by two
others — EM's scale-invariance proof, THERMODYNAMICS' coupled-shift
counterfactual that fails just as badly — isolating genuine
autocorrelation as the real driver) → Red Team's Phase-5 final audit
(independently re-ran every piece; ruled the mechanism claim partially
overridden — autocorrelation, not amplitude, drives the failure — but
the Combined Verdict does NOT change, confirmed three independent ways;
adopted QUANTUM's recommendation, with its mechanism argument revised, to
foreclose reading the circular-shift leg as evidence of a genuine
T28-relevant contributor; confirmed two small arithmetic slips
independently caught by four of six seats, corrected in place per R4;
flagged a third instance of a named R4 failure shape — two of six
Phase-5 seats restated an unrecomputed aggregate figure — as a tightened
R4 addendum). **No Checkpoint criterion fires**, explicitly distinguished
from the exp-072/073 Checkpoint-4 precedent: the Phase-1 overclaim was
caught by two blind critics before Phase 3 ever adopted it (zero
overrides), and the Phase-5 finding is genuinely new information a prior
phase structurally could not have seen, shown non-load-bearing by three
independent robustness tests rather than a defended wrong claim.
**Headline: the T28 differential/two-tone-fit sub-thread is formally
retired on this instrument class, at any window, per the pre-committed
seventh-cycle rule — the sixth consecutive non-decisive T28
differential/two-tone cycle (Iterations 46–51), and the honest, decisive
outcome that rule exists to produce, not a further deferral.** The
underlying reusable instrument (`desk_check_pricing.py`,
`fit_and_calibrate.py`, R6, R7) is NOT retired. T28's own substantive
mechanism question (the ~2.84° periodicity's origin) gained no ground
this cycle — exactly where five prior cycles left it. Verdict PARTIAL.
Full record: `experiments/074-t28-window-pricing-cramer-rao-bound/`,
LOGBOOK.md Iteration 51); panel Iteration 50 done (exp-073,
PARTIAL, Combined Verdict HALT_NULL_MISCALIBRATED, CHECKPOINT criterion 4
FIRED A SECOND CONSECUTIVE CYCLE (process, notification not a pause) —
MATERIALS lead by rotation, executing PLAN.md's own Iteration-50 queue
item 1 (unanimous across all six of exp-072's Phase-5 seats): a
corrected, zero-FDTD re-issue of exp-072's differential/beat-fit
instrument for T28, behind the new `G0-e` ground-truth recovery gate
(LOGBOOK R6), as a clean, uncontaminated pre-registration per exp-072's
own contamination ruling's condition 3. Full five-phase cycle: Phase 1
proposal (an explicit a/b/c evidentiary-class taxonomy separating
data-free facts, pre-exp-072 closed findings, and inherited machinery
from anything exp-072 *observed*) → five blind Phase-2 critiques, all
support-with-changes, each independently re-executing a real defect
(PHOTONICS found `G0-e(i)`'s synthetic sweep never varied amplitude-
difference or phase-offset independently, its own `A_i` tripwire dead
code; ELECTROMAGNETISM found the `A_q` "binds hard" claim falsified
30-100x by exp-072's own already-closed values on the identical
substrate; THERMODYNAMICS found `m0` anchored to the wrong-resolution
`n_grid=400` fit, a third recurrence of a named defect class; QUANTUM
OPTICS built an independent Monte Carlo and found the sign-flip null
anti-conservative by 2.2-6x nominal, a leverage effect; VISION found the
sign-invariance admissibility clause's own cross-reference pointed at a
nonexistent "§5 G-gate table") → Red Team's Phase-2 audit
(PROCEED-WITH-MANDATORY-FIXES, 12 items, **zero overridden** — a rare
unanimous confirmation of all five critiques, plus a new structural
contamination finding of its own: exp-073's carrier-fit machinery being
bit-identical to exp-072's own on unchanged data means exp-073's own
real point estimates were already computable from exp-072's published
`results.json` before Phase 1 was proposed, ruled not
outcome-determining since no threshold was tuned in response, with a
binding disclosure/forward-lock condition attached) → Phase 3 synthesis
(all 12 items implemented, zero overrides, four implementation-level
judgment calls disclosed including two self-caught bugs, predictions
frozen and committed before any run) → Phase 4 (Combined Verdict
`HALT_NULL_MISCALIBRATED` — the new `G0-e(ii)` null-calibration gate
fires on both legs at every one of 144 cell-alpha combinations tested;
zero of four real T28 pairs was ever scored) → six blind Phase-5
reviews, all PARTIAL, exceptional convergence (PHOTONICS and MATERIALS
independently caught a false "72/72"/"144/144" failure-count claim, the
true count being 71/72/143-144; THERMODYNAMICS found the
"residual-structure" calibration leg doesn't actually test correlated
residuals, empirically indistinguishable from the i.i.d. leg it was
meant to be a harder companion to; ELECTROMAGNETISM found the cycle's
own `dR_q/dψ̄` sign-convention "fix" was itself backwards; VISION found
T2-1's own `carrier_q95` threshold shares `G0-e(ii)`'s own
anti-conservative construction) → Red Team's Phase-5 final audit
(independently re-verified every finding, confirmed EM's sign-convention
claim correct via three further independent methods including a
finite-difference reconstruction against exp-072's own real published
data, fixed `run.py`, re-ran end-to-end and diffed the full output
bit-for-bit against the pre-fix artifact — zero difference except
elapsed time). **CHECKPOINT criterion 4 FIRES** (a near-miss self-catch
at Phase 3 that reached the wrong conclusion — inverting a correctly-
computed sign to force agreement with an inherited, never-independently-
sign-derived exp-072 claim — and was then defended, not re-derived,
surviving Phase 3/4 and five of six Phase-5 seats; this program's own
established firing shape). Ruled a notification, not a pause; ten-item
same-shift docket (six applied and re-verified live, four bound forward
to Iteration 51); **R4 and R6 both extended** as standing house rules
rather than a new tripwire created (R6: a null must ship its own
calibration test, not merely a ground-truth recovery test; R4: extended
to a Phase-5 reviewer's own re-checking of a prior claim, and to sign
corrections specifically, which must be independently re-derived by an
external method, never adopted because they make two numbers agree).
**Checkpoint criterion 5 does NOT fire** (both exp-072 and exp-073
delivered genuine, independently-verifiable narrowing) but Iteration 51
is bound, in writing, to rule what a sixth non-advancing cycle on this
exact sub-thread would mean, rather than let non-firing apply by inertia
a sixth time — the fifth consecutive non-decisive T28 cycle now
(Iterations 46-50), the third consecutive cycle of the differential-fit
sub-thread with zero pairs ever resolved. **Headline: the substantive
methodological result is confirmed independently five times over — a
Freedman-Lane-style sign-flip null is correctly centered
(`E[R_q^surr]=0` exactly) but anti-conservative by ~2-6x nominal on a
small (`n=31,p=5`), leverage-concentrated carrier-conditioned design
(`mean diag(M5)=(n-p)/n=0.8387` exactly, window-width-independent by
algebra), directly generalizable to any future cycle fitting a similar
coefficient.** T28's own substantive mechanism question is exactly where
exp-072 left it — bounded by window identifiability, not advanced, not
narrowed. Verdict PARTIAL: `G0-e` (R6) worked exactly as designed,
converting what could have been a second silent contamination event into
a genuine, quantified, reusable instrument-class finding, but the
substantive question ends unmoved and a second, independent
sign-convention defect was caught only at Phase 5. Full record:
`experiments/073-t28-differential-beat-fit-reissue/`, LOGBOOK.md
Iteration 50); panel Iteration 49 done (exp-072,
PARTIAL, CHECKPOINT criterion 4 FIRED (process, notification not a
pause) — PHOTONICS lead by rotation, executing the Iteration-49 queue's
own item 1: the differential/beat-fit instrument (fit `delta_AB(θ)`
between adjacent `ABSORB` pairs directly, converting T28's own
Rayleigh-resolution problem into a coefficient-detection problem at the
window's well-resolved common-mode carrier). Full five-phase cycle: Phase
1 proposal → five exceptionally rigorous blind Phase-2 critiques (two
seats independently EXECUTED the estimator on real data, not just
reasoned from prose) → Red Team's Phase-2 audit (PROCEED-WITH-MANDATORY-
FIXES, 15 items, three seats' specific remedies overridden with
independently-derived corrections) → Phase 3 synthesis (all 15 items
implemented, one self-caught implementation bug fixed and disclosed) →
Phase 4 (zero FDTD, Combined Verdict NEITHER, matching Red Team's own
advance forecast) → six blind Phase-5 reviews, **three of which
independently found a critical carrier-phase sign bug** in the committed
estimator (via three different methods) that the Phase-3 self-catch had
missed — every published coefficient was a rotation by a nuisance
parameter (the carrier phase itself), invisible to every gate in the
design — → Director independent re-derivation and fix, verified against
synthetic ground truth (recovered/true ΔP = 1.0000±0.0007) and five
Phase-2 ledger quantities that reproduce post-fix and did not pre-fix →
Red Team's Phase-5 final audit (independent re-verification of the fix,
adjudication of all 29 cross-seat findings, three NEW defects found
including a docket item mandating a mathematically vacuous calibration,
a 10-item same-shift docket). **Headline, post-all-corrections: Combined
Verdict NEITHER stands, verified robust to the complete correction set.**
The substantive reason is sharper than first published: `R_q`'s
sensitivity to the common-mode carrier phase is exact and free
(`dR_q/dψ̄ ≡ R_i`, `|R_i|≥|R_q|` at 3 of 4 pairs), the carrier rotation
that zeroes `R_q` sits inside the carrier's own bootstrap uncertainty at
every pair, and a data-free leakage calculation shows `R_q` is
non-identifiable against essentially ANY periodic contributor from
~1.8°–5.0° (not specifically T21's 1.9608° fringe as first claimed — a
stronger, more general, more falsifiable statement). **CHECKPOINT
criterion 4 FIRES** (process-integrity: a written "all 15 items
implemented verbatim, zero un-adopted" claim verified false on eight
counts; the same function that carried one Director-caught bug at Phase 3
shipped a second half of the same defect class after the diagnostic that
found the first half was retired instead of re-run as an acceptance
test) — see CHECKPOINT block below, a notification not a pause, 10-item
same-shift docket applied and independently re-verified live,
`phase4_results.md` wholly republished (not annotated). **New standing
house rule R6/tripwire `G0-e`**: a synthetic ground-truth recovery gate is
now mandatory machinery for any future cycle fitting a carrier- or
phase-conditioned coefficient — a cycle that ships one without it fires
Checkpoint criterion 4 automatically. Verdict PARTIAL: the instrument
itself is now well-characterized (sound but window-limited, not merely
proposed), the estimator-integrity finding is real and load-bearing, but
T28's own substantive mechanism question ends narrowed, not answered.
Full record: `experiments/072-t28-differential-beat-fit/`, LOGBOOK.md
Iteration 49); panel Iteration 48 done (exp-071,
PARTIAL — VISION SCIENCE lead by rotation, executing PLAN.md's own
Iteration-48 queue item 1 (a genuine 6-for-6 blind-seat convergence at
exp-070's Phase-5 final audit): ELECTROMAGNETISM's C60/C70 `ABSORB`-depth
causal falsification test for live thread T28 — the causal manipulation
T28 never had, since `C40`/`C80` (exp-069) were only two points on the
`ABSORB` axis and `C60`/`C70` are also congruent members of exp-065's
`A=752`-fixed series. Full five-phase cycle: Phase 1 (VISION SCIENCE
proposes the causal test, 74 calls budgeted) → five blind Phase-2
critiques (all support-with-changes — PHOTONICS found 600nm-only scope
can't license mechanism language; MATERIALS/THERMODYNAMICS independently
found the proposal dropped exp-070's own mandatory "`ABSORB` is not a
material" caveat; ELECTROMAGNETISM found NO settling-closure check had
ever run on `C60`/`C70`; QUANTUM OPTICS found the free-period search sits
at/below the window's own Rayleigh resolution floor) + Red Team's Phase-2
audit (PROCEED-WITH-MANDATORY-FIXES, 7 items, **zero overridden** —
extended QUANTUM's resolution-floor finding to the CONFIRM band too, not
only REFUTE) → Phase 3 synthesis (all 7 fixes implemented in code, budget
recomputed to 78 calls/100-min hard stop) → Phase 4 (78 FDTD calls, 15.43
min; G1 PASSED 4/4 exact; both binding preconditions CONFIRM) → six blind
Phase-5 reviews (all PARTIAL, exceptional convergence) + Red Team's
Phase-5 final audit (independently re-verified every finding live,
including its own re-fit of a saturating-model claim).
**Headline: Combined Verdict `NEITHER`, doubly secured** — per-config free
periods rise smoothly with `ABSORB` depth (`C40=2.4361°→C80=2.5338°`,
`R²=0.8664`) but `spread_40_80=3.90%` misses the 30% CONFIRM floor AND
`R²=0.8664` misses the `≤0.30` REFUTE ceiling, **both independently, on
raw pre-registered thresholds alone** — the resolution-floor gate (window
supplies <10% of needed resolving power) is real and prospectively
load-bearing but was NOT the proximate cause of this run's verdict, per
Red Team's own correction of an initial overclaim in `phase4_results.md`/
`NOTES.md` (also propagated into a git commit message, corrected as an
erratum). **Two genuine new findings, Red-Team-confirmed**: (1) a
2-parameter saturating-exponential model fits the same four points at
`R²=0.998` vs. linear's `0.866` — real, mechanistically well-motivated,
not an R5-family over-read, but doesn't rescue the underlying unresolved
data; (2) **`PAD=ABSORB−40` exactly at all four congruent configs**
(independently found by THERMODYNAMICS/ELECTROMAGNETISM/QUANTUM OPTICS) —
a three-cycle-old (Iterations 46/47/48), previously-unflagged compound-axis
confound: a hypothetical CONFIRM on this series would have been mislabeled
`ABSORB`-tied; a hypothetical REFUTE would not have been equally
compromised. **Standing forward constraint, not a Checkpoint firing**: any
future CONFIRM on this series must read `ABSORB`-*or*-`PAD`-tied until a
PAD-decorrelated config exists. Same-shift mandatory-fix docket (7 items,
Red Team's Phase-5 final audit, all applied and re-verified live): the
resolution-floor narrative corrected, a latent `resolved=True` tie-handling
bug patched (`isfinite` guard, results.json fields re-derived without new
FDTD spend), `FROZEN_PREDICTIONS` text reconciled with actual code, all
caveats wired uniformly into every Combined-Verdict branch, a new
`lab/caveat_lint_config.json` entry, a new `PAD_CONFOUND_CAVEAT`, and
QUANTUM's own Phase-5 cost-estimate slip corrected. **No Checkpoint
criterion fires** (all five explicitly ruled — the PAD confound is the
closest call on criterion 4, ruled non-firing since it did not survive
undetected into a published causal claim). Verdict PARTIAL: the
settling-closure gap closed cleanly for the first time, the resolution
floor proved prospectively sound, a genuine mechanism candidate and a
genuine confound both surfaced — but T28's own substantive causal question
ends narrowed, not answered, doubly secured as an honest NEITHER. Full
record: `experiments/071-t28-absorb-depth-causal-test/`, LOGBOOK.md
Iteration 48); panel Iteration 47 done (exp-070,
PARTIAL — QUANTUM OPTICS lead by rotation, executing the Iteration-46-
queue's own item 1 (near-unanimous six-seat convergence, itself Red
Team's own standing exp-069 forward tripwire): a single zero-FDTD-cost
desk-check batch on live thread T28 (the settled, resolution-robust
~2.84° periodicity in the `C80−C40` padding delta that does not match
T21's own established `P(θ)≈1.96°` fringe), discharged one cycle ahead of
its own Iteration-48 deadline. Full five-phase cycle, zero `lab/` diff,
zero FDTD calls throughout — pure desk arithmetic over already-committed
data. Phase-2 Red Team's audit (PROCEED-WITH-MANDATORY-FIXES, 10 items,
zero overridden) independently EXECUTED, not merely argued, two of the
five blind critiques' own proposed checks: PHOTONICS'/MATERIALS' proposed
null-permutation control (found, at N=10,000 scratch scale, 100% of
random targets clear the batch's own 1% CONFIRM band) and
ELECTROMAGNETISM's "item (a) will fire regardless of the true signal"
prediction (ran the original design's own logic on real data: it
CONFIRMS today via a spurious third period). **Headline: P-070-3 REFUTEs
cleanly** (`TAPER=40` cells alone as a diffracting sub-aperture misses the
observed period by 1197%) — **one T28 sub-hypothesis is now dead.**
**P-070-1 CONFIRMs, softer than its own first-draft prose claimed**
(Phase-5, ELECTROMAGNETISM, Red-Team-confirmed): the ~2.8°-family signal
lives in `C40(θ)` and `C80(θ)` individually (recovered periods 2.44°/
2.53°, 3.93% apart from each other), genuinely disfavoring an
`ABSORB`-depth-tied mechanism over a shared-geometry one, but each
config's own period sits 11–14% from the padding-delta's own free-fit
period with a non-trivial residual fit to T21's own fringe — more
consistent with a compromise fit than a clean independent confirmation;
the pre-registered gate stands (house discipline: scored as committed,
not re-scored after a later review sharpens the read) but licenses less
than first claimed. **P-070-2/P-070-4 NEITHER — this cycle's own real
methodological headline**: a formal `N=20,000` null-permutation control
(mandated by Red Team's Phase-2 audit, implemented in code) showed that
BOTH the beat-frequency reconstruction's and the `A_eff` systematic
trace's own sub-0.1%-deviation named-constant matches — which cleared
every raw threshold, including a 750nm cross-validation `R²=0.7663` — are
statistically indistinguishable from chance (`null_p=0.50/0.20/0.81`).
**The clearest demonstration in this program's history that a dense
small-integer bookkeeping-constant search finds a plausible match
regardless of ground truth** — generalized into a new standing house
rule, appended to LOGBOOK's own RULED OUT R5 entry: any future proposal
searching more than a handful of named-constant/parameter combinations
for a match must include a pre-registered null-permutation control before
a match counts as evidence. **No mechanism identified for T28.** Phase 5
(six blind reviews + Red Team's final audit, all independently
re-verified live, not from prose) found: PHOTONICS'/MATERIALS'
independently-converging caveat-lint registry gap for this cycle's own
headline near-misses (fixed same-shift, new entry, re-verified 0
required-site failures); EM's "CONFIRM weaker than claimed" finding
(language corrected same-shift, verdict unchanged per pre-registration
discipline); QUANTUM's R5-precedent argument (a `null_p` this high
carries REFUTE-grade weight in substance though the schema has no such
label — ruled forward-only, the R5 addendum above); and the Director's
own mid-edit arithmetic self-catch (the `A_eff` six-way tie at 519 is
actually only 3 independent coincidences once the
`{TAPER,ABSORB40,PAD80}=40` cluster's full degeneracy is traced, not 6 —
caught and corrected before commit, verify-before-claim discipline
working as intended). **No Checkpoint criterion fires** (all five
explicitly ruled; the caveat-lint gap matches this program's own
established same-shift, found-before-close non-firing precedent, lacking
either aggravating fact — a violated pre-committed tripwire, or undetected
survival through the process — that distinguishes an actual firing).
Verdict PARTIAL: real, load-bearing process progress (the exp-069 forward
tripwire discharged a cycle early, one sub-hypothesis cleanly killed, a
genuine generalizable house rule established) but the substantive
question — what actually produces T28's periodicity — ends narrowed, not
answered. Full record: `experiments/070-t28-mechanism-desk-check-batch/`,
LOGBOOK.md Iteration 47); panel Iteration 46 done (exp-069,
PARTIAL — THERMODYNAMICS lead by rotation, executing PLAN.md's own
LOCKED, unconditional Iteration-46 mandate (Red Team's Iteration-45
ranked #1, born of Iteration 45's own CHECKPOINT firing): Block MINI's
period-match test (`P-VIS42-10`, exp-065), deferred-behind-relabeling for
a third-or-fourth consecutive cycle — "either build the properly-powered
FDTD version ... or formally retire the test ... no further relabeling,
no further citation-tripwire-only treatment." Desk-first check run and
committed before Phase 1 (closing the exact gap Iteration 45's own
CHECKPOINT fired on); full five-phase cycle (100 FDTD calls, 14.76 min,
~2.2× faster than budgeted); Phase-2 Red Team audit PROCEED-WITH-
MANDATORY-FIXES, 10 items, zero overridden, restructuring the Combined
Verdict into one 5-way conjunctive gate with a pre-committed non-decisive-
outcome rule computed IN CODE (any outcome short of full corroboration
triggers immediate formal retirement, never PARTIAL-and-deferred) —
its own sharpest self-found attack: the design's own "not settling"
language was never wired to the settling-closure test meant to establish
it, the identical failure shape reproduced one level down inside the very
design meant to close it. **Headline: P-069-1 (amplitude) REFUTEs
decisively (`ptp/|mean|=16.20`) — the flat/additive-systematic null this
program defaulted to for T24 since Iteration 23 is conclusively rejected
— but P-069-2/P-069-3 (period-match) land in a genuine gray zone: real,
well-determined periodic structure (best fit `P*=2.84°`, `R²=0.63`,
independently confirmed far outside pure noise, p<5×10⁻⁵), just not at
T21's own predicted `P(39°,600nm)=1.96°` (45% off). Per the pre-committed
rule, Combined Verdict = `FORMAL_RETIREMENT_NON_DECISIVE`: Block MINI's
period-match test is FORMALLY RETIRED, not deferred a fifth time.** New
live thread **T28** opened: the unexplained ~2.84° periodicity itself,
real (settling/resolution-robust at the two cells tested, first-
principles-sound per EM's same-frequency-superposition argument — `A=752`
is bit-identical for C40/C80 by a live code assertion, so the mismatched
period cannot be "T21's fringe, differently weighted") but unidentified.
Phase-5 found two real, corrected-same-shift overclaims: PHOTONICS' own
λ-scaled-aperture re-analysis (R²=0.767 vs T21's own R²=0.348 on the same
750nm data) was materially under-reported by the original write-up; the
R3 resolution check's own "not... Yee-grid discretization structure"
language overstated a 2-of-31-angle, near-zero-crossing pass (97–150%
margin vs. this program's own ~7% historical precedent). MATERIALS'
Phase-5 review independently found and same-shift-fixed a STALE
`lab/caveat_lint_config.json` registry entry (still described Block MINI
as "STILL UNDECIDED" post-retirement). **No Checkpoint criterion fires**
(all five weighed explicitly; the two overclaims are real but caught
within this cycle's own Phase 5, before close, lacking the aggravating
fact — a violated pre-committed tripwire, or survival through an entire
cycle's own five-phase process undetected — that distinguished this
program's actual firings). **New forward tripwire: T28 needs a desk-only
first move by Iteration 48's close or the scheduling gap itself becomes
Checkpoint-4-adjacent.** Verdict PARTIAL (5 PARTIAL/1 PROMISING-as-
process, MATERIALS, folded in not overridden): real, load-bearing process
progress (a four-cycle-deferred citation-tripwire pattern genuinely
closed, verified at the code level) but the substantive optics question
ends MORE open, not less. Full record: `experiments/069-t21-block-mini-
period-match-power-up/`, LOGBOOK.md Iteration 46); panel Iteration 45 done (exp-068,
PARTIAL — ELECTROMAGNETISM lead by rotation, executing Red Team's
Iteration-44 ranked queue item 2: VISION's Block-ARTICLE settled-STEPS
FDTD leg (T27), four consecutive cycles without being a cycle's own
primary FDTD work. 44 FDTD calls (corrected from a 42-call Phase-1
design after the Director self-caught, mid-build, two defects the whole
panel record missed: a missing raw-profile block for the N9 aggregate's
empty-scene companions, and an ill-posed comparison against a
non-existent 750nm/STEPS=1400 baseline). **Headline (P-068-2/3
CONFIRMED): Block ARTICLE's own scored article-row C — the only
construction in this program's history to produce a scored constraint-3
number, retracted since Iteration 42 — is re-certified at settled
STEPS≥2800 for both configs, bucket unchanged MARGINAL, sign unchanged
negative.** ELECTROMAGNETISM's own Phase-5 self-review found a stronger,
previously-uncomputed confirmation: the article-row and empty-floor N9
aggregates' ABSOLUTE settling shifts match to <1% at both configs — the
cycle's own passivity hypothesis, verified with already-committed data
no one had checked. Also: P-068-1 REFUTED (settled empty N9 floor
breaches GATE_HARD for C40, extending exp-066's own "gets worse at
settled STEPS" finding to the aggregate level — does not move any
constraint-3 verdict); P-068-5/6 CONFIRMED (interior angles clean;
STEPS=2800 independently verified converged on the article-present
channel); P-068-4 PARTIAL (minor, config-dependent, three orders below
C_THR_LAB). Mandatory-fix docket applied same-shift: a new
`lab/caveat_lint_config.json` entry closing a two-cycle-overdue
caveat-propagation gap; a self-contradictory deferral-count arithmetic
corrected in place (original left standing, labeled); five cosmetic
findings (VISION SCIENCE's own exhaustive Phase-5 pass) fixed, none
load-bearing. **CHECKPOINT criterion 4 FIRES** — not on Block ARTICLE's
own physics, but on Block MINI's period-match test: independently found
by two blind Phase-5 seats (QUANTUM, VISION) to be on its third (or, by
this program's own more literal counting convention, fourth) consecutive
cycle of deferral-behind-relabeling, crossing this program's own
pre-committed T23 threshold, and — the sharper finding — this cycle's
own mid-cycle Red Team audit was handed a zero-cost path to close it and
silently narrowed it to a citation tripwire with no argued reason. Ruled
a **notification, not a pause** (this program's unbroken precedent);
**Block MINI is LOCKED, unconditional, for Iteration 46**. Verdict
PARTIAL (Red Team's synthesis: the headline is real, but the cycle
nearly let its own integrity tripwire slide). Full record:
`experiments/068-t27-block-article-settled-steps/`, LOGBOOK.md Iteration
45); panel Iteration 44 done (exp-067,
PARTIAL — MATERIALS lead by rotation, executing R_contact's LOCKED,
unconditional Iteration-44 mandate (Red Team's Iteration-43 escalation
ruling, granting THERMODYNAMICS after three consecutive deferrals). New
`bonded_substrate_conduction_correction` (`lab/thermo_sidecar.py`) models
the CNT-forest root-to-substrate thermal contact resistance as a new
series term, two complementary endpoints (`correction_factor_series`,
worst-case; `correction_factor_replace_rear`, contact-replaces-rear-loss)
per Red Team's own Phase-2 reconciled docket resolving ELECTROMAGNETISM's
topology attack. **Phase-5 event**: ELECTROMAGNETISM's blind review found
the shipped `correction_factor_replace_rear` formula — Red Team's own
Phase-2 construction — was a genuine passivity violation (diverged to
infinity as R_contact→0, decreased as R_contact grew), undetected through
Phase 3, Phase 4's own 23/23 gates, and four of six Phase-5 reviews.
Red Team's Phase-5 final audit independently confirmed it, named itself
as the origin, and supplied the exact fix (`correction_factor_replace_
rear = correction_factor_series − 1.0`, both endpoints on the same R_rear
baseline) — corrected Stress-B reading: series margin 1.0047× unchanged;
replace-rear margin 3.9286× (not the first-reported 1.1737×, MORE
comfortable, not less). Two new stage-25 gates permanently guard this
regression class. A second process defect (Red Team's own R2): three
Phase-5 review files carried a premature Director note claiming the fix
was "already addressed" before it existed — corrected in place, original
left standing. **Checkpoint criterion 4 FIRES** (genuine scrutiny, not
reflexive non-firing: a sign-inverted formula reached a permanent
regression gate, originated in Red Team's own deliverable, and survived
six independent checkpoints) — ruled a notification, not a pause, docket
landed same-shift, full bench 195/195 green. `REALIZABILITY_MEMO.md`
Entry 3 (new): R_contact's own tier is UNANSWERED, pending a real
measurement — zero sourced figures exist, and the two endpoints disagree
by >4× at the decision-relevant regime even after correction. **Verdict
PARTIAL** (Red Team's synthesis: machinery sound, but the substantive
question — is TD-5's margin actually threatened — is more open now than
before this cycle, not less). VISION's Block-ARTICLE FDTD leg explicitly
deferred to Iteration 45, not folded in — see queue below); panel
Iteration 43 done (exp-066,
PARTIAL — PHOTONICS lead by rotation, closing Red Team's Iteration-42
ranked-#1 item: re-verifying exp-041's own Block MAIN angle standard
(±35°/36°/37°/38°/39°/40°, 3λ) at STEPS≥2800, T27's own highest-stakes
sub-item. All 36 mandate-named cells now settled-verified (G-1-prime
18/18 bit-exact vs exp-041's committed data; all six predictions
CONFIRMED, including a new θ-axis settling-generalization test,
37°/600nm, that closes ELECTROMAGNETISM's own Phase-2 attack alongside
the original λ-axis one). **Headline, unanticipated: GATE_HARD pass/fail
count gets WORSE at settled STEPS, not better — 31/36 fail at STEPS=1400
→ 34/36 fail at STEPS=2800** — explained by ELECTROMAGNETISM's Phase-5
passivity argument (a graded-damping-bounded passive channel's converged
residual has no reason to trend toward zero; the unsettled reading was a
large transient coincidentally cancelling the true T21 fringe at some
cells). The T21 fringe-fit refit (exp-042's own propagator re-scored
against the settled data, reported strictly as a fit-quality statistic,
zero causal language) improved on every metric (sign_agree 27/30→30/30,
r²(c*) 0.7852→0.8271) — all six blind Phase-5 seats independently
verified this discipline held, including inside the machine-readable
results.json verdict string itself, not just the prose. Still open, not
closed by this cycle: Block ARTICLE's article-present legs (the only
construction in this program's history that has ever produced a scored
constraint-3 PASS/MARGINAL number), the four interior FALLBACK_ANGLES,
and Block MINI's period-match test (T21 mechanism-vs-artifact,
UNDECIDED, now two consecutive cycles deferred behind relabeling).
**Checkpoint criterion 4 does not fire, conditional on a 3-item
mandatory-fix docket** (a caveat-lint registry entry three independent
blind seats found stale on its own description, despite its
trigger-term widening landing correctly — Red Team ruled this a
"found-before-close, fixed-same-shift" non-firing precedent, matching
Iterations 19/23/42), landed same-shift. Verdict PARTIAL, 5-of-6 blind
seats concurring (MATERIALS alone read PROMISING); Red Team's final
audit concurred with the 5-seat majority on structural grounds (T27 only
partially closed; the headline is double-edged, not a clean win). **New
ruling: R_contact — PLAN.md's still-standing top-of-queue item — is
LOCKED, unconditional, for Iteration 44** (Red Team's Phase-5 final
audit, granting THERMODYNAMICS' escalation request; matches this
program's own lowest-ever 3-deferral lock precedent, exp-059's
`Q_ext(x)`). Cycle closes unblocked, Iteration 44 queue below);
panel Iteration 42 done (exp-065,
PARTIAL — VISION SCIENCE lead by rotation, finally running live thread
T24's own nineteen-iteration-deferred `ABSORB` boundary sweep, scoped per
Red Team's Iteration-41 recommendation to close into an actual
constraint-scored FDTD run. The congruent-geometry construction worked
cleanly (both absolute gates PASSED; the causal-identity gate's corrected
derivation VOIDED the original design entirely — caught at the desk
stage, zero FDTD cost — and was replaced with a strictly stronger
zero-step static-array check), but T24's own headline question came back
genuinely undecided: the frozen STEPS=1400 data says "absolute transfer,"
a same-shift settling follow-up (a clean 4-point convergence trend plus a
full settled STEPS=2800 re-sweep, both committed as reproducible code)
shrinks it 5.4× and says otherwise. **The real finding is bigger than
T24**: STEPS=1400 is confirmed NOT settled on the plane/ambient channel at
±35°/±38°/±40° — not padding-specific, reproduced on the UNPADDED
`experiments/041-t20-angle-audit` (Iteration 18) anchor geometry itself —
implicating this program's own established angle standard and every T20/
T21/T24-adjacent citation for nineteen iterations (new live thread T27).
Six blind Phase-5 reviews split 3-3 on whether this fires Checkpoint
criterion 4; Red Team's final audit ruled **does not fire, conditional on
a 3-item mandatory-fix docket**, which landed same-shift (mirrors
Iteration 23's own conditional-non-firing precedent) — including
correcting a scorecard-table propagation gap and relabeling a verdict
string (`P-VIS42-10`) that had asserted an untested causal mechanism,
both caught by Red Team's own final audit after the blind seats' three
same-shift corrections closed 70% of what Phase 5 found. Verdict PARTIAL,
a rare 6-for-6 agreement across all seven seats. Cycle closes unblocked,
Iteration 43 queued, ranked #1: re-verify exp-041's own MAIN-block rows at
settled STEPS — see queue below); panel Iteration 41 done (exp-064,
PROMISING — QUANTUM OPTICS lead by rotation, an enforced
`length_provenance` guard closing live thread T23 (open since Iteration
22, closed BY ARGUMENT — never by code — at Iteration 23/31, violated in
the open for three consecutive cycles under disclosure alone, per
Iteration 40's own binding forward commitment). `gas_conduction_h_eff`/
`lumped_cube_mass_kg`/`mixed_length_scale_regime`/`front_surface_
conduction_correction` all now require a keyword-only, no-default
`length_provenance` declaration (allow-list `bench_construction`/
`measured_geometric`, plus a `diagnostic_only` escape hatch), backed by a
new trust-suite stage 24 (4 gates, 107/107 full bench). The "it actually
catches the mistake" claim on the new source-inspection gate was
independently verified live by FOUR separate parties (Phase 4, two
Phase-5 seats, Red Team's final audit), each deliberately mistagging a
real committed call site and confirming FAIL-then-PASS on revert — not
an assertion. Zero physics changed anywhere (every pre-existing
regression number bit-identical); a genuine unplanned find (one of stage
18's own pre-existing test values IS `w_on_m`, a real extinction-derived
length silently used as an "arbitrary" test point since Iteration 31,
harmless, now correctly tagged). Phase-1's own §6 (a claimed new
24×–75× realizability gap) did NOT survive Phase 2 — contradicted this
program's own already-established exp-061 MP-2/MP-5 record — and was
STRUCK entirely, not restated at a corrected number, per Red Team's own
process argument (no falsification band was ever given, unlike every
other claim this cycle). **No Checkpoint criterion fires** (all five
explicitly ruled twice); a new binding forward tripwire is set on the
source-inspection gate's own remaining exposure (nested-paren parsing;
single-file scope — real, concretely demonstrated by fresh Phase-5
review, zero live violation) for Iteration 42+. Cycle closes unblocked,
Iteration 42 queued — see queue below); panel Iteration 40 done (exp-063,
PARTIAL provisional-to-PROMISING — THERMODYNAMICS lead by rotation,
sourcing the CNT-forest/Vantablack-class candidate material's real
through-thickness thermal conductivity for the first time (every prior
Biot check used silicon's κ=148 W/(m·K), unsourced since Iteration 25)
and deriving a closed-form Biot-number front-surface conduction
correction. TD-1 through TD-5 all CONFIRMED; this program's own
"first-ever thermal-detectability classification flip" scenario does
NOT materialize against any real figure found (worst sourced κ=0.7
W/(m·K) still leaves the witness-scale margin at 1.2920×, 7.8× above
κ_critical=0.0897) — the correct candidate material's own κ DOES still
license the lumped-capacitance assumption every committed THERMO-
sidecar margin in this program's history rests on. **CHECKPOINT
criterion 4 FIRES at Phase 5** — see CHECKPOINT block below, a
notification not a pause, 5-item mandatory-fix docket applied and
re-verified live; cycle closes unblocked, Iteration 41 queued); panel
Iteration 39 done (exp-062,
PARTIAL provisional-to-PROMISING — ELECTROMAGNETISM lead by rotation,
thin-film-interference/R-vs-T bound + near-field-coupling threshold for
the MP-3/MP-4 mechanism-class ambiguity. Both open exp-061 sub-claims
close in the direction that reinforces UNOBTANIUM-WITH-PARAMETERS, more
decisively than predicted (the black-matrix OD is transmission-based,
measured on an unbacked substrate, structurally ruling out the strong-
resonance alternative); two new real-material comparators (NiP-black,
carbon/graphene aerogel) both fail the joint 2×/2× bar, overdetermining
the tier further; the near-field-coupling question is honestly left
open, geometry-class-dependent, not resolved. **CHECKPOINT criterion 4
FIRED TWICE this iteration — unprecedented** — see both CHECKPOINT
blocks below, both notifications not pauses, all mandatory fixes applied
and re-verified live; cycle closes unblocked, Iteration 40 queued);
panel Iteration 38 done (exp-061,
PROMISING — MATERIALS' 8-cycle-deferred absorptivity/mechanism
literature check closes `REALIZABILITY_MEMO.md` Entry 2's own standing
question: UNOBTANIUM-WITH-PARAMETERS, overdetermined by a 70–350×
thickness gap against real CNT-forest/Vantablack-class coatings, not by
an implausible absorption rate; the mandatory caveat-propagation-check
tool — `lab/caveat_lint.py`, first proposed Iteration 15 — is built,
self-tested against a real historical Checkpoint-4 near-miss, and live
with 6 registry entries. Two MAJOR Phase-5 self-catches (a stale THERMO
disposition scale, a registry required_sites gap on the very entry
built to prevent that class of gap) were both found by this cycle's own
review process and fixed same-shift; neither overturned the tier; no
Checkpoint criterion fires. See CHECKPOINT-adjacent tripwire note below);
Iteration 39 queued per Red Team's Iteration-38 ranked top-3, no lock —
see PANEL.md/LOGBOOK.md for the phenomenon-program's own current state;
this section's numbered history stops at the pre-redesign exp-023
baseline, panel-era entries live in the queue below and in full in
LOGBOOK.md)

**CHECKPOINT (Iteration 40, 2026-08-23, criterion 4 — program-integrity
drift, on exp-063's own self-declared Phase-2 forward tripwire).**
exp-063's own Phase-2 Red Team audit (THERMODYNAMICS-led cycle, sourcing
the CNT-forest candidate's real thermal conductivity) declared a new
forward tripwire when ruling that VISION SCIENCE's Phase-2 finding (the
brand-new `lab/numeric_lint.py` tool, built the immediately-preceding
commit, had no registry entry yet for this cycle's own new machinery)
did NOT fire: "a materially similar gap in either of THESE specific new
entries... found again at Phase 5 or any later iteration, that DOES fire
Checkpoint criterion 4 without further deliberation." VISION SCIENCE's
blind Phase-5 review found exactly that: the new `numeric_lint_config.json`
entry `exp063-cf-bench-vs-witness-derivation`'s own `site` field covered
only `NOTES.md`, never `phase4_results.md`. Red Team's Phase-5 audit
independently re-verified this live and found a second, identical gap no
blind seat caught (the sibling `caveat_lint_config.json` entry
`exp063-thermo-disposition-netd-disclaimer` also covered only `NOTES.md`)
— two of the cycle's three brand-new registry entries carried the same
narrow-scoping defect. Neither gap concealed a live rule violation, but
Red Team also independently confirmed VISION's third finding: a genuine,
small (0.06–0.10%, safe-directioned), live numeric-accuracy defect in
`phase4_results.md`'s own Summary table ("inside band" claims inaccurate
for 2 of 4 sourced κ values, a found-vs-predicted-κ-range artifact) — the
strongest evidence the wider registry reach VISION's finding calls for
would have caught something real. **Ruled a firing, explicitly overriding
the raw 6-0 PROMISING seat count** (distinguished from Iteration 38's own
non-firing precedent — a self-caught, same-cycle-tool registration gap —
on the specific ground that THIS cycle's own tripwire pre-committed, in
writing, Director-accepted without override, to firing on exactly this
fact pattern if found again at this cycle's own Phase 5). Per unbroken
precedent (Iterations 17/36/37/38/39×2) this is a **notification, not a
pause**: a 5-item mandatory-fix docket was applied and independently
re-verified live same-shift (a sibling `numeric_lint` entry scoped to
`phase4_results.md`; the `caveat_lint` sibling's `required_sites` widened
to match; the Summary-table numeric claims corrected with the artifact
disclosed; the NETD disclaimer added to the Summary table and Bottom-line;
`NOTES.md`'s missing `Result`/`Learned` sections filled), Marsh is
notified (this entry + LOGBOOK.md Iteration 40 + SESSION_LOG.md), and
exp-063 closes unblocked. Not a physics finding — TD-1 through TD-5 stand
unchallenged, independently re-derived five times over across this
record with no defect found anywhere; this is a process-completeness
finding about this cycle's own registry-building discipline. Full record:
`experiments/063-cnt-forest-thermal-conductivity-biot-check/phase5_
redteam_audit.md`, LOGBOOK.md Iteration 40.

**Standing tripwire (Iteration 38 close) — FIRED TWICE at Iteration 39,
see both CHECKPOINT blocks immediately below.** The
`exp061-t18-evidentiary-tier-propagation` caveat-lint registry entry had
already self-caught two coverage gaps in one cycle at Iteration 38 (an
un-propagated disclosure at Phase 2; an under-scoped `required_sites`
list at Phase 5). Red Team ruled neither fired Checkpoint criterion 4
then (different defect species / same-cycle self-catch, both pre-close),
but declared the lineage's self-catch grace fully used — any FURTHER gap
in this specific entry's own coverage, discovered at Iteration 39 or
later, would auto-fire criterion 4 with no further deliberation. Two did,
in the same iteration: a `required_sites` gap at Phase 2 (CHECKPOINT #1),
then a `candidate_globs` gap at Phase 5 (CHECKPOINT #2) — the second
discovered after the first's own same-shift fix had already been applied
and represented as closing the entry's coverage. Both fixed same-shift;
the registry now carries a systemic `experiments/*/phase*.md` pattern
(both entries plus `lab/caveat_lint.py`'s own `DEFAULT_CANDIDATE_GLOBS`)
rather than another named-filename patch, per Red Team's own Phase-5
ruling that the prior fix's narrowness — not merely an unlucky miss — was
the root cause.

**CHECKPOINT (Iteration 39, 2026-08-23, criterion 4 — program-integrity
drift, on the tripwire above).** VISION SCIENCE's blind Phase-2 critique
of exp-062 (ELECTROMAGNETISM's thin-film-interference/near-field-coupling
proposal) found that the `exp061-t18-evidentiary-tier-propagation`
entry's own `required_sites`/`candidate_globs` could not discover
exp-062's own forthcoming NOTES.md/phase4_results.md, even though
exp-062's Phase-1 proposal already trips the entry's `trigger_terms`
(`graded_black_shell…absorptivity`, `alpha…5.74`). Red Team's Phase-2
audit (`experiments/062-.../phase2_redteam_audit.md` §3) ruled this
fires: the tripwire's own hardened wording ("discovered at Iteration 39
or later, auto-fires criterion 4, no further deliberation") dropped the
sibling `exp060-sigma-flat-*` tripwire's explicit phase-based safe harbor
("surviving into THIS cycle's own published Phase-3/5 artifact") — so a
gap surfacing at Phase 2, before Phase 3 freeze, still fires; there is no
textual room left for a "caught before freeze" defense on this specific
lineage, its grace already spent twice over at Iteration 38. The Director
accepted this ruling without override (`phase3_synthesis.md` §2). Per
unbroken precedent (Iterations 17/36/37/38) this is a **notification, not
a pause**: the registry was widened same-shift (`required_sites` and
`candidate_globs` in `lab/caveat_lint_config.json`, plus
`lab/caveat_lint.py`'s own `DEFAULT_CANDIDATE_GLOBS`, now cover exp-062
by literal path and any future experiment by a generic
`experiments/*/phase4_results.md` pattern), Marsh is notified (this
entry + LOGBOOK.md Iteration 39 + SESSION_LOG.md), and exp-062 proceeds
unblocked to Phase 4. Not a physics finding — no engine/FDTD result is
affected; the gap was in registry scoping for files that did not yet
exist. Full record: `experiments/062-thin-film-interference-and-near-
field-coupling-bound/phase2_redteam_audit.md` §3, `phase3_synthesis.md`
§2, LOGBOOK.md Iteration 39.

**CHECKPOINT #2 (Iteration 39, 2026-08-23, criterion 4 — program-
integrity drift, SECOND FIRING THIS SAME ITERATION, unprecedented).**
Recorded as a distinct event from CHECKPOINT #1 above, per Red Team's own
instruction not to fold two firings into one boilerplate notification.
VISION SCIENCE's blind Phase-5 review found that CHECKPOINT #1's own
same-shift widening — the "generic pattern for any future experiment"
added to `exp061-t18-evidentiary-tier-propagation`'s `candidate_globs` —
only ever covered `phase4_results.md`-class files; it never covered
`phase2_critique_*`/`phase3_synthesis`/`phase5_review_*`/
`phase5_redteam_audit.md`, for exp-061, exp-062, or any future
experiment, at any tier (not even WARN). Demonstrated live, not
hypothetically: `experiments/061-.../phase5_review_materials.md` — a
PRE-EXISTING, already-merged file from the PRIOR iteration — restates
exp-061's own UNOBTANIUM verdict with ZERO T18/WebSearch-snippet
disclosure anywhere, and was structurally invisible to the tool the
entire time. Red Team's Phase-5 audit independently re-verified the fact
pattern (live tool execution, direct grep, hand `fnmatch` checks) and
ruled this FIRES, on three grounds: (1) the tripwire's own "discovered at
Iteration 39 or later" test is a floor, not a per-iteration ceiling —
nothing in its text caps it at one firing; (2) this is a textually
distinct sub-defect (`candidate_globs` under-scoping, not
`required_sites` under-scoping) — a different gap-shape, not the same
argument re-offered a second time, which is what the "no further
deliberation" clause actually forecloses; (3) the fix that CHECKPOINT #1
represented as closing this entry's coverage is shown, before this very
cycle even closes, not to have fully closed it — the single clearest
case this program's history offers for treating a recurrence as live,
not arguable. A sibling gap (`exp061-thermo-length-scale-staleness`'s own
`candidate_globs`, independently found by both THERMODYNAMICS and
ELECTROMAGNETISM's Phase-5 reviews) is folded into this SAME Checkpoint
event as a systemic aggravating fact, not ruled a third, separate
firing — that entry has never received its own hardened, self-catch-
grace-spent tripwire, so extending the T18 lineage's zero-tolerance
language to it by analogy alone would itself be exactly the kind of
unargued extension the tripwire's own text forecloses. Per unbroken
precedent (Iterations 17/36/37/38, and this cycle's own CHECKPOINT #1)
this remains a **notification, not a pause**: a 10-item mandatory-fix
docket was applied and independently re-verified live same-shift (the
`candidate_globs` widening now uses a systemic `experiments/*/phase*.md`
pattern, applied to both affected entries and to `lab/caveat_lint.py`'s
own `DEFAULT_CANDIDATE_GLOBS`, not another named-filename patch; the live
violation in `phase5_review_materials.md` is closed directly). Marsh is
notified (this entry + LOGBOOK.md Iteration 39 + SESSION_LOG.md); exp-062
closes unblocked. Not a physics finding — no tier, verdict, or headline
number changes. Full record: `experiments/062-.../phase5_review_vision.md`
§1, `phase5_redteam_audit.md` §2, LOGBOOK.md Iteration 39.

**CHECKPOINT (Iteration 37, 2026-08-22, criterion 4 — program-integrity
drift, THIRD CONSECUTIVE CYCLE).** Red Team's Phase-5 audit ruled
Checkpoint criterion 4 FIRES: VISION SCIENCE's Phase-5 review found
`lab/validation/run_all.py::stage22_uniform_lossy_shell`'s own docstring
— the single most permanent, git-tracked, every-run-executed site
describing exp-060's purpose — still stated its pre-run "edge grading
suppresses diffraction" framing with zero pointer to the cycle's own
P-10 result, which explicitly REFUTED that framing (excess scattering
concentrates backward/Fresnel-reflectance-like, not forward/diffraction-
like). A third consecutive cycle (Iterations 35→36→37) of the identical
caveat-placement/propagation defect class, the same failure shape as
Iteration 36's own firing (a scoped propagation promise — here NOTES.md's
own original Next item 1 — that named specific sites and missed the more
load-bearing one). Not a physics finding — every stage-22 gate, the
regression anchor, and all six Phase-5 seats' independent re-derivations
stand unchallenged; the raw seat count (5 PROMISING/1 PARTIAL) was
overridden on two independently sufficient grounds (the Checkpoint-4
firing itself, and five real defects — not just the one — landing across
five different seats in one Phase-5 pass, two sitting inside the cycle's
own headline Learned section). Five same-shift mandatory fixes applied
(the `run_all.py` docstring, a numeric slip "30.7%"→"~31.3%", a
normalization overclaim in Learned #4, a wrong causal attribution for a
thermal-margin gap, and a backwards bias-direction claim — full detail in
LOGBOOK.md Iteration 37), full bench 74/74 reverified after. Per
Iterations 17/36's own direct precedent this is a notification, not a
pause: Marsh is convened (this entry + LOGBOOK.md Iteration 37 +
SESSION_LOG.md), unblocked Iteration 38 work continues. The mechanical
caveat-propagation-check tool — queued as Iteration 37's own #3 priority
and NOT built this cycle (hand review missed the `run_all.py` site
again) — is now MANDATORY, a zero-cost rider at Iteration 38 regardless
of lead seat; a fourth deferral would itself be a criterion-4-adjacent
finding (Red Team's own words). Full record: LOGBOOK.md Iteration 37
Phase 5.

- exp-000 Hello Maxwell ✅ — hand-rolled 2D TMz FDTD, first light, photonic
  nanojet reproduced (`experiments/000-hello-maxwell/`).
- `lab/` bench ✅ — engine (ε/σ/PEC + anisotropic-μ) with a 14/14 trust
  suite (`lab/validation/VALIDATION.md`), replicated on macOS to the digit;
  CI runs the suite on every push (ticker: co-lab #32).
- Lanes: Clyde = solver + materials · Bonnie = viz + observer camera ·
  Preston = acceptance test (non-physicist figure reader) · Meep heavy
  bench parked on Preston's Mac.
- exp-001 The Flashlight Statement: DoD proposed (3 scenes + observer
  figure + NOTES + 3-λ sweep), freeze window open ~24h from
  2026-08-09 04:00Z.
- exp-002 CONCLUDED — "invisible" has a direction (see below).
- exp-003 CONCLUDED — the red-side improvement survives a
  resolution-controlled sweep but isn't the quadratic law guessed at; a
  non-monotonic bump at 480nm was the open thread into exp-004.
- exp-004 CONCLUDED (this shift) — isolated `mu_r_floor` alone (electrical
  size + cpl fixed) at 420/480/540/600nm × 5 floor values. Found the
  480nm bump isn't wavelength-special: Q_ext(cloak) vs `mu_r_floor` is
  non-monotonic, sometimes sign-flipping, at *every* λ tested, under
  gates too clean to be noise (box_dev ≤1.8%, cross_dev ≤0.1%
  throughout). Working hypothesis logged: clamp-boundary cell-alignment
  on the fixed grid (staircase artifact), not a smooth clamp-band-width
  law.
- exp-005 CONCLUDED (this shift) — direct test of exp-004's hypothesis:
  reran the clearest jump (600nm, floor=0.10→0.18) at 1.5× resolution
  (cpl 20→30). The jump barely shrank (17.7%→16.4%, only 7% relative)
  and the whole 5-point curve's *shape* survived refinement almost
  unchanged (correlation 0.9996 between cpl=20 and cpl=30) —
  **refutes** the staircase-artifact hypothesis. Sharper read: the
  non-monotonicity is an intrinsic feature of how `mu_r_floor` reshapes
  the shell's `mu_r` profile against its fixed `eps_z=2.25`, not a grid
  artifact. exp-006 candidate: vary `eps_z` independently (r1/r2 ratio)
  at fixed floor values.
- exp-006 CONCLUDED (this shift) — isolated `eps_z = (r2/(r2−r1))²`
  independently of overall cloak scale (fixed outer radius r2=90 cells,
  swept inner radius r1) at 4 core points × exp-004/005's exact
  0.10/0.18 floor pair, λ=600nm. Found **two things, not one**: (1) a
  clean, fully monotonic law — Q_ext(cloak) rises as the shell thins
  (eps_z grows), holding at both floor values with zero exceptions
  across 8 points, the cleanest law this whole investigation line has
  produced; (2) the floor-jump exp-004/005 spent two shifts
  resolution-testing does **not** track eps_z monotonically — |jump| =
  177.5%/17.7%/70.7%/38.5% at eps_z=1.44/2.25/3.24/4.59, and the
  exp-004/005 baseline geometry (eps_z=2.25) is the *only* one of the 4
  showing a negative jump; the other three all show the "naively
  expected" direction. Reframes exp-004/005's characterized dip as
  possibly atypical to that specific eps_z, not the norm. Unplanned
  bonus: core=15/floor=0.10 gave Q_ext=0.0934, ~7× better than the
  exp-002–005 baseline (0.6620) — a design lead, not a targeted search.
- exp-007 CONCLUDED (this shift) — deliberate follow-up to exp-006's
  design lead: traced Q_ext(eps_z) below core=15 (core=8/10/12/20/25,
  same λ/floor=0.10). All 3 predictions confirmed: the monotonic law
  extends cleanly all the way to core=8 (**new best Q_ext=0.0429, ~15×
  better than baseline**, no reversal — core=15 was not a local
  minimum), and the rate of improvement slows sharply below core≈15
  (3–10× shallower per-cell slope than the 20–30 range), consistent
  with Q_ext approaching a positive residual as the hidden core
  shrinks. **Honest caveat flagged, not yet resolved:** this curve
  doesn't separate "smaller PEC core intrinsically scatters less" from
  "the shell genuinely cloaks better when thicker" — q_ext is
  normalized by the fixed outer radius throughout so it isn't a
  normalization artifact, but the missing control (bare, uncloaked PEC
  disk at the same radii) is exp-008's job before core=8 gets treated
  as an actual better cloak design.
- exp-008 CONCLUDED (this shift) — the missing control from exp-007:
  bare, uncloaked PEC disk (no cloak shell) at the same 7 core radii
  exp-006/007 characterized with a cloak, λ=600nm, same domain/gates
  (box_dev ≤1.3%, cross_dev ≤0.2% — the tightest yet). P1/P2/P4
  confirmed; **P3 refuted, and the refutation is good news**: the
  cloaked/bare Q_ext ratio was predicted to *rise* as core shrinks
  (cloak's relative help weakest where absolute numbers look best) but
  instead **falls** — 0.900 at core=30 down to a ~0.193 plateau at
  core=8–12. Per the pre-registered fallback reading, a falling ratio
  means the shell's relative suppression effectiveness genuinely
  improves as it thickens, not that core=8's ~15× absolute
  improvement is mostly "smaller object, less to hide." Agrees with
  exp-006's independent eps_z finding (thicker shell = better cloak).
  **exp-007's caveat is now closed**: core=8/floor=0.10 stands as the
  lab's best-characterized cloak design, on solid footing.
- exp-009 CONCLUDED (this shift) — exp-008's own queued follow-up:
  traced the cloaked/bare Q_ext ratio below core=8 (r1=4/5/6/7 cells),
  CFL margins checked explicitly first. **The pre-registered box_dev
  gate failed at 2 of 4 new points** (core=4: 3.5%, core=5: 2.3%,
  vs the ≤2% threshold; core=6 exactly borderline at 2.0%) — bare-disk
  gates stayed clean throughout, so the failure was specific to the
  cloak's graded profile at small core. The cloaked Q_ext curve itself
  came out non-monotonic (a bump peaking near core=5) where the
  established law predicted a smooth continuation. Flagged honestly as
  not-yet-trustworthy rather than reported as a finding — resolved by
  exp-010 the same shift.
- exp-010 CONCLUDED (this shift) — direct resolution check on exp-009's
  anomaly, exp-004→exp-005's exact precedent: reran the same 4 core
  points at cpl=30 (1.5×), geometry scaled to hold physical size fixed.
  **Both anomalies were the same cpl=20 artifact.** Cloak box_dev
  dropped from 3.5%/2.3%/2.0%/1.8% to 0.5%/0.2%/0.0%/0.3% — an order of
  magnitude tighter, the cleanest gates in the lab's history. The
  non-monotonic bump vanished entirely — cpl=30's cloaked Q_ext curve
  is cleanly monotonic, extending exp-006/007's law without exception
  down to r1=6 cells (the smallest core tested to date). The
  cloaked/bare ratio (exp-008's ~0.193–0.194 plateau at core=8–12) does
  genuinely **rise below core=8**, reaching ~0.21–0.28 — now confirmed
  gate-clean rather than resting on ambiguous data. Read with exp-007's
  own finding (absolute Q_ext improvement slows below core~15): the
  shell's *relative* effectiveness degrades too, once core shrinks past
  ~8 — a second, independent sign of diminishing returns, not one.
- exp-011 CONCLUDED (this shift) — exp-006's own queued "candidate B":
  reran exp-004's floor sweep at core=15/eps_z=1.44 instead of the
  baseline core=30/eps_z=2.25, reusing exp-006's existing 0.10/0.18
  points and adding 0.28/0.40 (floor=0.05 excluded — CFL-unstable at
  this eps_z, `ceiling=0.268 < courant_frac=0.32`, itself a new addendum
  to the standing `mu_r_floor<0.05` item: the instability is
  geometry-dependent, not just a low-floor phenomenon). **Result: the
  full core=15 floor curve (0.0934→0.2592→0.5242→0.7818) is strictly
  monotonically increasing, no sign-flip anywhere** — unlike core=30's
  non-monotonic dip-then-rise shape (exp-004/005). Strengthens exp-006's
  reframe from "possibly atypical" toward a working conclusion: the
  exp-004/005 floor-jump was a property of the eps_z=2.25 baseline
  specifically, not a general feature of the `mu_r_floor` knob.
- exp-012 CONCLUDED (this shift) — exp-011's queued third generalization
  point: floor sweep at core=40/eps_z=3.24, adding floor=0.05 and 0.28
  to exp-006's existing 0.10/0.18 points (floor=0.40 excluded — the
  *first* time this series' excluded point was a degeneracy-threshold
  issue rather than CFL). Full 4-point curve
  (0.7374→0.7540→1.2871→1.8821) is **strictly monotonically increasing,
  zero exceptions** — same pattern as core=15 (exp-011), now 3-for-3
  against core=30's non-monotonic curve. Gates the cleanest of the
  series (box_dev ≤0.5%, cross_dev ≤0.1%).
- exp-013 CONCLUDED (this shift) — exp-012's queued fourth and last
  point: floor sweep at core=48/eps_z=4.59 (the tightest degeneracy
  margin in the series — only floor=0.05/0.20 fit inside the graded
  threshold, 0.28/0.40 both degenerate here), adding those two points
  to exp-006's existing 0.10/0.18. Full 4-point curve
  (0.9218→1.2096→1.6751→1.7146) is **strictly monotonically increasing**
  through the tightest-margin point of the whole investigation (8.2%
  from degeneracy). **Generalization now complete: all 4 of exp-006's
  core/eps_z points swept across their full available floor range —
  3 of 4 (core=15/40/48) are strictly monotonic, only core=30/eps_z=2.25
  (the original exp-002/003 baseline) sign-flips.** No mechanism yet
  proposed for why that one ratio is special — logged as the natural
  next question, needing a finer eps_z scan bracketing 2.25 (a new
  experimental axis, worth a dedicated shift, not a quick bolt-on).
- exp-014 CONCLUDED (this shift) — the fine eps_z scan bracketing 2.25,
  exp-012/013's queued follow-up: swept r1=27/28/29/31/32/33 (Δeps_z≈
  0.07–0.15, the finest step tested in this line) bracketing the reused
  r1=30 baseline, at floor=0.10/0.18, λ=600nm, cpl=20. **The negative jump
  is not an isolated grid point — it's a real, contiguous 4-point trough**
  spanning eps_z≈2.18–2.41 (r1=29/30/31/32 all negative, r1=27/28/33 all
  positive), and the exp-004/005/006 baseline (r1=30) sits almost exactly
  at the trough's deepest point (−17.69%, more negative than any new
  point). **Bigger surprise:** exp-006's own coarse monotonic law (Q_ext
  rises cleanly with eps_z, "no exceptions in 8 points") does **not**
  survive this finer resolution — Q_ext(eps_z) itself is non-monotonic at
  both floor=0.10 (a dip at the far edge, r1=33) and floor=0.18 (a real
  local minimum near r1=30) — the coarse sweep's widely-spaced points just
  never landed inside the dip. Gates clean throughout (box_dev ≤2.0%,
  cross_dev ≤0.08%). Honest caveat raised and immediately addressed by
  exp-015 the same shift: this was the first fine (1-cell) r1 step tested
  anywhere in the eps_z line, so a grid-quantization origin hadn't been
  ruled out.
- exp-015 CONCLUDED (this shift) — direct resolution check on exp-014's
  trough, exp-004→exp-005/exp-009→exp-010's exact precedent applied to the
  eps_z axis for the first time: reran 3 of exp-014's bracketed points
  (flank/center/flank: r1=28/30/33) at cpl=30 (1.5×), geometry scaled to
  hold physical size fixed. **The trough survives resolution intact — no
  sign flips at any of the 3 points.** base=30 (trough center) stays
  deeply negative (−17.69%→−16.42%, a 7.2% relative shrink almost
  identical to exp-005's own 7% shrink on the *floor* jump at this same
  geometry); both flanks (base=28, base=33) stay positive. Gates the
  cleanest of the whole eps_z line (box_dev ≤1.3%, cross_dev ≤0.0018%).
  **Confirms exp-014's trough is a genuine physical feature of
  Q_ext(eps_z), not a 1-cell grid-quantization artifact** — closes
  exp-014's own honest caveat cleanly, in the same shift it was raised.
  No mechanism proposed yet for *why* the feature sits near eps_z≈2.25–2.4;
  candidates logged (impedance-mismatch sweep, angular-pattern comparison).
- exp-016 CONCLUDED (this shift) — mechanism candidate 1 (outer-boundary
  impedance mismatch): pure material-array probe, no FDTD stepping —
  built a bare `Sim`, called the real `schurig_reduced_cloak_tm`
  builder, and read the actual solver tensor at r=r2 across the trough
  bracket (r1=27–33) plus exp-006's corner points (15/40/48), at
  floor=0.10/0.18/0.40. **Refuted, decisively, two ways at once:**
  `|Γ(eps_z)|²` (the outer-wall reflection coefficient) rises smoothly
  and strictly monotonically with zero local feature anywhere near the
  trough, and it is *exactly floor-identical* at every trough-bracket
  point (0.10 vs 0.18 give bit-identical `mu_r(r2)`) — a floor-
  independent quantity structurally cannot produce the floor-dependent
  sign flip that defines the trough. Honest bonus finding: grid
  quantization can flip a point from "analytically unclamped" to
  "numerically clamped" right at threshold (r1=33/floor=0.40) — a small,
  real effect the continuous formula alone would have missed.
- exp-017 CONCLUDED (this shift) — mechanism candidate 2 (angular-
  pattern shape comparison, trough vs flanks): new instrumentation added
  to `lab/sections.py` (`angular_scattered_pattern`, verified against
  stage 8 + a per-run self-consistency identity at machine epsilon), run
  at r1=27/30/33 (flank/trough/flank), floor=0.10, λ=600nm — 4 runs,
  5.1 min. **Also refuted — magnitude-only, no new scattering mode.**
  Shape correlation places the trough inside the same family as both
  flanks (0.9688/0.9717 vs the flank-flank 0.9383); the one asymmetry
  (trough correlates *better* with each flank than they do with each
  other) is fully explained by ordinary distance in eps_z-space, not
  anomaly. **Both queued mechanism candidates are now closed — neither
  explains the trough.** New candidate proposed for a future shift: a
  frequency-domain view (sweep λ at fixed core=30/eps_z=2.25 — the
  mirror of exp-003's λ sweep — to test whether the trough is a
  resonance-like condition tied to the fixed λ=600nm/cpl=20 grid rather
  than a pure eps_z effect).
- exp-018 CONCLUDED (this shift) — the frequency-domain mirror
  experiment exp-017 queued: swept λ (420–750nm, exp-003's own scaling
  machinery) anchored at the trough's own geometry (r1=30/r2=90 at f=1),
  scaling r1/r2 together so eps_z stayed inside the established trough
  window (2.2228–2.2907) at every λ while the shell's radial extent in
  wavelengths varied 2.40λ–4.30λ. **Major reframe: the eps_z trough is
  not an eps_z effect.** The negative floor-0.10→0.18 jump survived at
  exactly one point — λ=600nm, the *only* sweep point where shell
  thickness (r2−r1=60 cells) lands on an exact integer number of
  wavelengths (3.00λ at cpl=20). All 5 other points came back positive
  (+3% to +92%) despite eps_z barely moving (0.068 range) — eps_z does
  not track the effect; shell-thickness-in-wavelengths does. Gates clean
  (box_dev ≤1.81%, cross_dev ≤0.085%); λ=600 point reproduces exp-014's
  reused number exactly. Reframes exp-006/011–017's "eps_z≈2.25 trough"
  as a coincidence of exp-002's original geometry choice (shell=3.00λ),
  not a real eps_z-axis feature. New sharp hypothesis: a shell-thickness
  standing-wave/Fabry-Pérot condition — tested immediately by exp-019.
- exp-019 CONCLUDED (this shift) — exp-018's own queued direct test:
  brackets r1=50 (shell=40 cells=2.00λ) ±3 cells, mirroring exp-014's
  bracket around 3.00λ, same floor pair, r2=90 fixed. **The
  standing-wave hypothesis does NOT generalize to 2λ.** All 5
  complete-floor-pair points (r1=47–51) show positive jumps (+34% to
  +46%), squarely inside the range exp-018 found at its own non-3λ
  points — no dip, no band, nothing resonance-like near 2λ. Narrows
  exp-018's hypothesis considerably: whatever produces the negative jump
  at 3λ isn't a generic "shell = integer × λ" rule; 2λ and 3λ behave
  differently. r1=48 reproduces exp-006/013's existing core=48 numbers
  exactly (sanity check). One honest gate miss flagged, not hidden:
  r1=47/floor=0.18 box_dev=2.17%, just over the 2% band (doesn't touch
  the r1=50 target point, itself among the cleanest in the set, or the
  qualitative conclusion).
- exp-022 CONCLUDED (cloud shift 10; renumbered at the redesign merge) — exp-019's own queued follow-up: every
  point in the eps_z/shell-thickness line since exp-006 had shared one
  fixed outer radius, r2=90 cells — never varied. Moved r2 itself for
  the first time (r2=75 and r2=120, brackets around r2=90), holding
  shell=3λ=60 cells fixed at each, ±3-cell bracket around each new
  target, floor pair 0.10/0.18 reused. **Result: neither new r2
  reproduces r2=90's negative jump at its own shell=3λ point** — both
  targets come back strongly positive (+173.5% at r2=75/r1=15, +51.0%
  at r2=120/r1=60), squarely inside the range exp-018/019 already found
  at every non-3λ/non-r2=90 point. **The "shell=3λ" feature is
  r2=90-specific, not a portable shell-thickness law.** Combined with
  exp-018 (not eps_z) and exp-019 (not any-integer-λ), the population
  of things that don't explain the original exp-004/005/006 finding is
  now large; still zero mechanism identified. One honest gate miss
  flagged: 4 of 7 r2=75/floor=0.10 points missed box_dev≤2%
  (2.55–3.36%) — resolved same-shift by exp-023.
- exp-023 CONCLUDED (cloud shift 10; renumbered at the redesign merge) — direct resolution check (cpl 20→30,
  exp-005/010/015 precedent) on exp-022's r2=75/floor=0.10 gate misses,
  3 representative core points (worst miss, target, clean flank).
  **Gate miss was ordinary cpl=20 grid noise**: box_dev roughly halves
  at all 3 points (e.g. 3.36%→1.71%), all now clear 2%; jump values
  shift only 3.1–4.8% relative, no sign flip. Closes exp-022's one open
  caveat in the same shift it was raised — the r2=75 half of exp-022's
  conclusion now stands on fully gate-clean footing.

**2026-08-12 — program redesign (Marsh's directive, in-session):** new work
runs under `PANEL.md` / `LOGBOOK.md` — the seven-seat research panel
targeting the founding phenomenon under four explicit constraints (beam
termination · no return · **no ambient silhouette** · switchable),
continuous mode with checkpoints. The remaining [open] items below are
**PARKED** (mirrored in LOGBOOK.md, resumable, off the critical path).

- [done 2026-08-12, panel Iteration 1] **exp-020 the ambient-appearance
  baseline** — instrument built (stage 9, 13/13; Beer–Lambert anchor to
  0.001), constraint 3 measured for the first time: absorber C = −0.686
  (Tier-A photopic FAIL ×34 field bar), material blindness ~20% (rim
  transmission), dilute sponge on its geometric value to 0.001. Verdict:
  PROMISING. 750 nm carries an asterisk pending the margin rerun.
- [done 2026-08-12, panel Iteration 2, cloud panel shift] **exp-024 the
  instrument-margin fix** — MARGIN_MULT=3.5 (ny 1200→1584) REFUTED as the
  governing mechanism (δ_C gate missed at all 6 λ/weighting combos,
  non-monotonically — 450nm got worse despite the best margin ratio ever
  measured); the pre-committed ±35° fallback (dropping only the ±40°
  angles) resolved it cleanly everywhere instead, localizing the real
  mechanism to something angle-specific at ±40°, not margin-ratio-driven.
  Bonus: settled the λ-ordering question exp-020 left open — a real, small
  (~1.5–1.9%) red-ward |C| growth in hard-edged articles survives the
  clean floor (not pure bias). Constraint-3 headline reconfirmed
  (C≈−0.684). exp-025 (same shift, direct resolution check on the
  chromatic finding, closing a gap Red Team's Phase-5 audit caught):
  CONFIRMED real, not a grid artifact — 4th time this program's R3 rule
  has refuted an artifact hypothesis. Verdict: PROMISING. Full record:
  LOGBOOK.md Iteration 2.
- [done 2026-08-13, panel Iteration 3, cloud panel shift] **exp-026 the
  σ(I) endpoint triplet** — MATERIALS' OFF-lab/OFF-field/ON static sponge
  articles (τ=0.008/0.032/3.9) on the ±35° fallback baseline, 114 new FDTD
  sim calls. Red Team's decisive Phase-2 catch: the original P-MAT8
  prediction (σ_abs/σ_ext≥0.90 for the ON article) directly contradicted
  the bench's own ESTABLISHED `graded_black_shell` measurement (0.51,
  same r_out) — rebanded to [0.35,0.65] pre-freeze, confirmed by real data
  (measured 0.606–0.608). Seven of eight predictions confirmed cleanly;
  P-MAT6 (a calibration constant) held at 4 of 6 points, both misses on
  OFF-lab in opposite directions. **No PASS/FAIL or constraint-3 language
  attaches to the near-threshold OFF-lab/OFF-field C readings** (VISION's
  mandatory ruling, Red Team-escalated) — the first cycle to produce C
  values with real SNR against both frozen bars, but the r=156 scale-bridge
  check that would license perceptual language stays queued, not built.
  Two new findings: (1) beam-behind is NOT wavelength-flat (46% relative
  spread, non-monotonic, uncorrelated with grid resolution — PHOTONICS'
  Phase-5 candidate mechanism: a settling-time artifact from fixed
  `BEAM_STEPS` across a cpl sweep, not real material physics); (2) the ON
  article's σ_abs/σ_ext sits ~0.10 ABOVE the 0.51 anchor, opposite the
  direction Red Team/EM's own mandatory-fix reasoning predicted — and EM's
  Phase-5 review sharpened this into a program-wide finding: **both 0.51
  and 0.61 exceed the idealized ≤0.5 geometric-optics ceiling**, meaning
  neither is the asymptotic material constant this program has been
  citing (new LIVE THREAD T9). Red Team's Phase-5 audit (verdict: MINOR
  ISSUES) caught two real record defects — P-MAT6's miss-count undercounted
  (an undisclosed second miss, not floor-explicable) and a run-count/
  elapsed-time bookkeeping inconsistency (a code instrumentation bug) —
  both corrected same-shift in NOTES.md/LOGBOOK.md and `run.py`. Verdict:
  PROMISING. Full record: LOGBOOK.md Iteration 3.
- [done 2026-08-13, panel Iteration 4, cloud panel shift] **exp-027
  settling, spread, and the PEC ablation** — resolved both of Iteration
  3's queued threads in one cycle. T9 **ANSWERED**: PEC-core presence is
  incidental to the established 0.51-vs-0.61 σ_abs/σ_ext gap (true
  Δ=+1.56×10⁻⁶ between PEC-cored and PEC-free versions of the identical
  graded-shell profile, indistinguishable from zero; angular-pattern
  channel independently corroborates) — rim/profile-transmission geometry
  drives the gap, not the PEC core, though not yet formally floor-gated
  (Red Team's Phase-5 catch: box_dev is ≈1221× the measured delta, no
  established decision floor exists for this channel yet). P-MAT4's
  chromatic beam-behind anomaly: settling-time cleanly, uniformly refuted
  at all 3λ (doubling `BEAM_STEPS` moves beam-behind ≤0.0012pp everywhere)
  — but the standard R3 spatial check (cpl×1.5) made the anomaly WORSE
  (46%→128% relative spread) instead of confirming/refuting it as
  artifact, the first time in 6 R3 applications this program has produced
  that outcome (new LIVE THREAD T10). Red Team's Phase-5 audit (MINOR
  ISSUES) caught two numeric defects (a rounding slip inflating the T9
  delta 6.4×; the pre-freeze-disclosure blind-run count undercounted "3 of
  16" vs. the true 8 of 16) and QUANTUM independently caught a scoring
  error (VISION's commitment clause read "not triggered" using only Block
  1's data when Block 2's much larger shift — up to −1.54pp — does trigger
  it) — all four corrected same-shift in NOTES.md/LOGBOOK.md. Verdict:
  PROMISING. Full record: LOGBOOK.md Iteration 4.
- [done 2026-08-13, panel Iteration 5, cloud panel shift] **exp-028 the
  radial ledger and the channel cross-check** — resolved both of
  Iteration 4's queued threads, one (T10) far more substantially than
  predicted. New machinery: `lab/sections.py::radial_absorbed_power`
  (radial-binned absorbed-power ledger), gated by new suite stage 10
  (PEC-core hard zero + empirical closure, calibrated 1.5% after a
  first-run measurement of 1.11%, confirmed settling-independent). Full
  bench 45/45 green throughout. **Load-bearing Red Team catch, before any
  run**: exp-027's own published Block 2 (the T10 finding) never rescaled
  `SIGMA_ON` per λ, silently drifting the ON article's optical depth from
  3.9 to 5.70/5.85/5.95 across the sweep — an explicit erratum added to
  T10's LOGBOOK entry, independent of exp-028's own outcome. Result: **T10
  substantially reframed** — the correctly-τ-held rerun shows box-ledger
  σ_ext spread flat (6.49%) and the corrected beam-behind spread only
  46.41%→49.46% (+3.05pp), not the published 46.41%→127.57% (+81.16pp) —
  **96% of T10's reported "enlargement" evaporates**; a small residual
  survives, open. **T9 sharpened from coincidence to mechanism**: Cell B's
  (non-PEC) core absorbs only 0.0062% of total power (resolution-stable)
  — the graded shell's own σ(r) profile extinguishes nearly everything
  before the field reaches the core, in either construction. Phase 5 (six
  fresh seats + Red Team audit): three of six seats independently caught
  the same display-rounding defect (core_frac shown as "0.01%", true
  0.0062%) and Red Team caught a second instance of the same bug class
  (a resolution-match figure) — both corrected same-shift; **new LIVE
  THREAD T11 opened** (box-ledger channel's own decision-floor
  characterization, promoted from a twice-recurring unassigned backlog
  item); VISION's Phase-5 dissent (arguing r=156 should move to Iteration
  6, not 7) preserved on the record, not overridden silently; Checkpoint
  criterion 4 pre-registered as a tripwire on Iteration 7's r=156 build
  actually happening. Verdict: PROMISING. Full record: LOGBOOK.md
  Iteration 5.
- [done 2026-08-13, panel Iteration 6, cloud panel shift] **exp-029 the
  coherent-superposition bridge gate** — QUANTUM's own mandatory,
  fourth-cycle build (deferred three times prior), scoped per its own
  Iteration-5 Phase-5 notes: graded-shell endpoint article (exp-028's
  Cell B construction, not a uniform disk), `radial_absorbed_power`'s
  closure identity as a second acceptance gate, derived (not hand-copied)
  material constants. New machinery: suite stage 11 (multi-source
  coherent superposition gate — two absolute identities, joint-vs-summed
  phasor at 1.9×10⁻¹⁵/2.4×10⁻¹⁵ RMS relative error, both vacuum and
  lossy-object scenes), full bench 48/48 green. **Every prediction
  confirmed — the cleanest cycle in the program's history by that
  measure.** Bridge-gate machinery now validated end-to-end, no longer
  deferred. Coherent interference cross-term measured for the first time:
  +0.0224% of beam absorption, 126–152× below its own Cauchy-Schwarz
  ceiling (two independent Phase-5 re-derivations, EM and QUANTUM,
  converged on a corrected TRUE ceiling of 3.40% from measured powers,
  vs. the pre-registered nominal 2.83%) — a normalized degree-of-
  coherence γ≈0.66%, real but ~99.3% washed out by spatial averaging in
  this geometry (not a universal law, QUANTUM's own caution). Bin-wise
  check confirms real, small spatial structure (5.02× the aggregate,
  genuine radial interference fringe) an aggregate check alone would
  wash out. Red Team's Phase-5 audit (verdict: MINOR ISSUES) caught one
  real record defect: VISION's Phase-5 "fourth consecutive constraint-3-
  silent cycle" count was itself wrong (Iteration 3 ran a real 81-run
  ambient scene with C values, misclassified as beam-scene-only) —
  corrected to **three**, matching Iteration 5's own original count.
  **Checkpoint criterion 5 given an explicit ruling for the first time in
  the program's history** (non-firing). T11 folded in as a companion to
  Iteration 7's own r=156 build (VISION's own Phase-5 pick, near-
  unanimous 5-of-6 seats). QUANTUM's own remaining open half (the
  incoherent-ensemble/phase-quadrature idiom, concretely scoped and
  mathematically pre-verified by Red Team) queued for a future QUANTUM
  lead cycle. Verdict: PROMISING. Full record: LOGBOOK.md Iteration 6.
- [done 2026-08-14, panel Iteration 7, cloud panel shift] **exp-030 the
  r=156/312 near-field→witness-scale bridge (T8) + box-ledger floor
  companion (T11)** — VISION's five-times-deferred mandatory build,
  hard-committed at Iteration 5's close with a pre-registered
  Checkpoint-4 tripwire: **executed in full this cycle, the tripwire
  does not fire.** Red Team's Phase-2 audit caught the Phase-1
  proposal's r=78 anchors citing the wrong, gate-failing ±40° geometry
  (corrected in code: absorber −0.7209, PEC −0.8673, V-weighted
  fallback) plus a three-way-converged `graded_black_shell` optical-
  depth confound (fixed: σ_max=0.5/κ, holding radial optical depth
  constant). 89 new FDTD sim calls, ~5.1h (r=312's 37-run leg alone took
  3.87h — ~8× the proposal's own estimate, the largest timing miss in
  program history, κ³ FDTD scaling). **Real deliverable: PASS/FAIL
  language is now decidable on near-threshold constraint-3 C values for
  the first time** — the δ_C floor gate passed cleanly at both r=156
  and r=312; T9 and T11 both close with their first floor-referenced
  verdicts (T9 decisively null 234–446× below the floor, T10 decisively
  real 93–178× above it). **But scored against VISION's own frozen
  thresholds, every σ(I) OFF-state article ever built is still MARGINAL
  (OFF-lab) or FAIL (OFF-field) at every scale tested — no configuration
  has ever PASSed constraint 3.** The cycle's central technical question
  — does C(z/z_R) bridge cleanly to witness scale — came back genuinely
  unresolved: PEC's C(r) is flatly non-monotonic (new live thread
  **T12**, candidate mechanism: Fresnel-zone/edge-diffraction ripple
  aliased by the family's factor-4 r-steps at fixed measurement-plane
  offset, independently proposed by PHOTONICS and EM); and Red Team's
  Phase-5 audit — missed by all six blind review seats — found this
  cycle's own fitted witness-scale prediction (≈−0.73/−0.86) sharply
  contradicts the |C|≈0.98 estimate that has justified this whole
  thread since Iteration 1 (new live thread **T13**). **Verdict:
  PARTIAL.** New Checkpoint-4 tripwire adopted: any future citation of
  this cycle's witness-scale numbers without flagging T13, or any
  reliance on PEC's fit or box_dev as a settled floor before their own
  R3 checks land, is a retroactive trigger. Full record: LOGBOOK.md
  Iteration 7.
- [done 2026-08-14, panel Iteration 8, cloud panel shift] **exp-031 the
  T12 ripple sweep, the T13 desk reconciliation, and QUANTUM's σ-held
  g-point** — Red Team's Phase-2 catch (none of five blind seats found
  it): exp-030's own `graded_black_shell` "absorber" construction was
  missing its historical PEC core (a hollow, not solid, shell at every
  θ=0/ambient reading it ever produced). Fixed, folded into this cycle's
  own T12 sweep. 18 new FDTD calls (~13 min for the sweep+quantum legs;
  the accepted THERMO sidecar failed twice and is deferred, root cause
  pinned by THERMODYNAMICS' own Phase-5 review — a bad `ref`, not just a
  bad box — and guarded in code against a silent third attempt).
  **T12's own dense PLANE_DX sweep came back a clean null** (zero
  significant ripple reversals across 17 points) **but its N_F coverage
  (≈8–110) never reaches the window (≈81–325) where the original
  r=156→312 reversal actually lives** — narrowed, not refuted; the
  correct next test is a genuine r-family sweep, not a denser PLANE_DX
  sweep (Red Team found EM's own proposed cheap fix likely infeasible —
  it would require sub-0.2λ standoff). **The core-correction delta is
  negligible** (6.8×10⁻⁶) — good news, independently reproducing T9's
  "core is incidental" finding via a new channel. **T13 stays
  unresolved for the one article that matters and got WORSE, not
  better**: the corrected absorber's dual-law disagreement (0.220)
  exceeds the original (0.132). Red Team's Phase-5 audit elevated this
  into new live thread **T14** — the absorber's contrast shallows,
  not deepens, toward what should be the geometric-shadow limit,
  confirmed on three independent axes (construction, baseline,
  functional form), the same pathology Iteration 7's finding e2 first
  named. **QUANTUM's g-calibration gap closes** at one new floor-
  corrected point (g=0.697, within 2% of established endpoints) —
  language corrected at Phase 5 to state this is licensed only in the
  weak-perturbation regime tested, not program-wide. **Verdict:
  PARTIAL. Program-integrity flag raised explicitly by Red Team, adopted
  by the Director as a binding Iteration-9 priority (not a Checkpoint
  violation — neither criterion 4 nor 5 fires on the letter)**:
  Iterations 4–8 are five straight cycles of instrument/reconciliation
  work; VISION's cheapest, most directly mechanism-relevant proposal (a
  σ(I) PASS-boundary run) has been the top Phase-5 pick for three
  iterations running without being built. Full record: LOGBOOK.md
  Iteration 8.
- [done 2026-08-14, panel Iteration 9, cloud panel shift] **exp-032 the
  σ(I) OFF-state PASS-boundary run** — MATERIALS' lead (rotation),
  executing Iteration 8's three-times-deferred binding priority. One new
  static/linear σ(I) OFF-state article (`off_pass`, τ=0.0065) plus Red
  Team's mandatory below-τ_off bracket point (`off_bracket`, τ=0.003), on
  exp-026's exact ±35° N=9 fallback bench. **`off_pass` clears VISION's
  frozen |C|<0.005 lab bar at all 3λ — the first σ(I) OFF-state
  configuration in this program's nine-iteration history to do so.**
  But g600(off_pass)=0.6927 tripped QUANTUM's own pre-registered
  disposition clause (≥0.69, matching off_lab's established, previously-
  unexplained g600=0.6913) — now a 4-point recurrence across three
  experiments, but Phase 5 (PHOTONICS + QUANTUM, independently) caught
  that every point shares an untested grid resolution at 600nm (the one
  wavelength on this bench line never R3-checked) — "reproducible"
  language walked back to flagged-pending-check. The bracket-point
  discriminator came back a genuine, uninformative null on the bulk-vs-
  edge-scattering mechanism question (EM's Phase-5 finding: the ambient-
  contrast channel is structurally underpowered for that question
  regardless of SNR at these τ; the correctly-targeted instrument,
  `radial_absorbed_power`, exists and was unused this cycle). A PASS here
  mechanically worsens σ(I)'s realizability picture (σ_on/σ_off → ≈600×,
  worse than any prior cycle) — MATERIALS' Phase-5 informal literature
  check put real numbers (reverse saturable absorbers, 2–10×) 1–2 orders
  of magnitude short of that target for the first time in seven cycles of
  citing "unobtainium." THERMODYNAMICS' own energy-sidecar fix had a
  self-caught, same-shift-corrected arithmetic defect (a ~6.4× ratio-
  composition error). **Verdict: PARTIAL** — 5 of 6 seats + Red Team's
  adjudication; QUANTUM OPTICS' lone PROMISING dissent preserved on the
  record, overridden per this program's own precedent (verdict turns on
  whether a cycle's own open questions close, not a favorable headline
  number). This PASS is explicitly a bench-scale diagnostic (VISION's own
  idealization iii), NOT a Tier-W/Tier-A constraint-3 verdict — the
  r=156 scale-bridge companion leg stays queued, now third in line. No
  Checkpoint criterion fires. Full record: LOGBOOK.md Iteration 9.
- [done 2026-08-15, panel Iteration 10, cloud panel shift] **exp-033 the
  g600 resolution check** — ELECTROMAGNETISM's lead (rotation), executing
  Iteration 9's top-ranked priority. R3-checked (cpl 20→30) the g600≥0.69
  recurrence at 600nm, the one wavelength on this bench line never
  resolution-tested, using a free-curvature-fit currency (g_corr, not the
  imposed 4/3π coefficient QUANTUM's Phase-2 review showed was already
  refuted by existing data) instead of raw g600. **Block B
  (`radial_absorbed_power` applied to off_pass/off_bracket, Iteration 9's
  #2 priority) was CUT this cycle** — PHOTONICS' Phase-2 critique found it
  structurally underpowered by 2–3 orders of magnitude and partly
  sign-degenerate, independently confirmed by Red Team; re-queued
  standalone, not run unmodified (Red Team's own sanctioned fallback).
  **Result: the raw-g600 cross-resolution shift is fully explained by the
  empty-scene decision floor's own shift, verified three independent ways
  to ≈10⁻⁸ precision** (EM's zero-parameter geometric chord model,
  QUANTUM's per-article decomposition, Red Team's cross-check) — a real
  advance, closing T1's carried-forward Iteration-9 item. **But Phase 5's
  seven-seat review (5 PROMISING, 2 substantive PARTIAL — PHOTONICS, Red
  Team) found the cycle answered a narrower question than first claimed**:
  the raw-g600 reading itself got MORE pronounced under refinement
  (0.6927→0.7056), not less; ΔA≈0 is closer to guaranteed-by-construction
  (the resolution change was almost entirely a common-mode floor shift
  that g_corr is built to cancel) than to strong evidence g₀ carries no
  separate resolution-dependent wave physics; and the actually-SCORED raw-C
  currency was never itself shown resolution-converged (moved toward FAIL
  at all four articles, only two resolution points). Two new open
  questions surfaced: g₀ sits ~15% below its own window-integrated
  geometric chord model, stable across resolution — argued as a real
  diffractive-leakage effect, not noise (PHOTONICS); and the retired
  QUANTUM Iteration-9 disposition clause's numeric successor is logically
  circular (Red Team). A real run-count bookkeeping bug was caught and
  corrected same-shift (50 FDTD calls, not 47 — the settling-control block
  runs all 5 scenes per invocation, not 2). **Verdict: PARTIAL**,
  Director adopting Red Team's audit over the raw 5-2 seat-verdict count,
  per this program's own established precedent (verdict turns on whether
  a cycle's own open questions close). MATERIALS' Phase-5 review found R3-
  CONFIRMED *hardens*, not leaves orthogonal, the σ(I) realizability
  tension, and surfaced a new, much larger gap: the mechanism must gate at
  flashlight irradiance (~10⁻³ W/cm²) against published RSA/two-photon
  onset thresholds (10⁶–10⁹ W/cm²) — 9–12 orders of magnitude short, a
  candidate Checkpoint-criterion-2 finding if it survives a dedicated
  check. No Checkpoint criterion fires this cycle (the Phase-3 tripwire on
  citing the PASS without its ε_r restriction was corrected same-shift,
  per Red Team's own conditional ruling). Full record: LOGBOOK.md
  Iteration 10.
- [done 2026-08-15, panel Iteration 11, cloud panel shift] **exp-034 the
  paired floor-convergence / r=156 scale-bridge cycle** — THERMODYNAMICS'
  lead, executing Iteration 10's two ranked priorities in one cycle plus
  Red Team's own mandatory fifth fix (Block N17_NATIVE, folded in by
  Director's budget call). Four independent blocks, 115 new FDTD calls
  (a harness bug — `ex.map`'s argument-passing mistake — crashed the
  first attempt after 46 calls, fixed and disclosed, full rerun clean,
  3378.8s). **CPL40 closed T1's carried-forward item cleanly**: both the
  empty-scene floor and the scored raw-C currency landed PLATEAU at
  cpl=40, neither converging nor diverging. **R156 found the program's
  only-ever σ(I) OFF-state PASS is fragile at scale** — every r=156
  reading of `off_pass` sits on the MARGINAL/near-PASS side of the bar,
  directionally robust across instrument choices, but Red Team's Phase-5
  audit confirmed a **second, undisclosed, comparably-sized domain-
  construction confound** (found by ELECTROMAGNETISM, missed by five of
  six blind seats and two Director catches) stacked under the disclosed
  angular-quadrature one — the "downgrades to MARGINAL" headline is
  directionally right but not yet resolution/domain-clean. **N17_156/
  N17_NATIVE found N9 angular quadrature — this program's own measurement
  standard since Iteration 1 — is NOT converged**: 0.88× the established
  N5-vs-N9 bound at r=156 (still flips the PASS/MARGINAL bucket), 3.2×
  the bound at r=78-native (the geometry the PASS citation actually
  uses). New live thread **T16** opened (the ambient-contrast channel's
  own angular-quadrature/domain-construction uncertainty budget, now
  measured for the first time and comparable to or larger than several
  headline PASS margins). **MATERIALS' realizability memo, deferred three
  iterations, finally written**: UNOBTANIUM-WITH-PARAMETERS for both
  candidate σ(I) mechanism classes — reverse saturable absorbers 1–2
  orders of magnitude short on dynamic range, two-photon absorption 9–12
  orders of magnitude short on operating irradiance, for two independent,
  non-trading-off reasons (`REALIZABILITY_MEMO.md`, a candidate
  Checkpoint-2 finding pending a rigorous, not informal, literature
  check). **Seven-seat Phase 5: unanimous PARTIAL, 7-for-7** — the first
  unanimous panel-era verdict — with four independently-converged
  arithmetic catches (a 1.9%→0.56% chord-sanity correction; a "4.2×"
  Learned-section error; a C78 anchor mislabeling; a dropped THERMO
  transient-ΔT regression) and one load-bearing new finding (EM's
  R156-vs-N17_156 domain confound) all corrected same-shift per Red
  Team's mandatory-fix list, disclosed not smoothed over. T15 (the g₀
  chord-model deficit) flagged as an open, unresolved three-way
  contradiction — this cycle's own fresh, committed chord model
  reproduces the measured value to 0.56%, not T15's claimed ~15%.
  Checkpoint criterion 4 ruled a tripwire (Red Team), satisfied by the
  same-shift corrections — does not fire. No other criterion fires. Full
  record: LOGBOOK.md Iteration 11.
- [done 2026-08-16, panel Iteration 12, cloud panel shift] **exp-035
  closing the R156/N17_156 domain × quadrature factorial, rebuilding
  N17_NATIVE, and reconciling T15** — QUANTUM OPTICS' lead (rotation),
  executing Iteration 11's own ranked priorities. 68 new FDTD calls (34 +
  34 + 0 desk-only), 2724.3s. Red Team's Phase-2 audit caught a
  load-bearing defect in the Phase-1 proposal (independently confirmed by
  PHOTONICS): the T15 reconciliation's cpl=40 comparator was a copy/paste
  fabrication, not a measurement — corrected via Red Team's own zero-cost
  recipe (raw g=|C|/τ at cpl=20/30/40 vs `chord_model_g0()`). **Result 1
  (T16): the domain and quadrature confounds disclosed at Iteration 11 do
  NOT add linearly at r=156 — they interact** (+2.109×10⁻⁴, at the
  REAL-INTERACTION threshold; ladder bucket stays MARGINAL either way).
  **Result 2 (T16, the bigger one): the r=78-native N17 rebuild — built
  correctly this time, N9 leg bit-identical to exp-033's own established
  citation, proving no domain confound — shows this program's own
  headline, first-ever constraint-3 σ(I) OFF-state PASS (exp-032,
  reconfirmed exp-033) downgrades from PASS to MARGINAL under N17
  quadrature.** As of this iteration, no σ(I) OFF-state configuration
  this program has ever measured survives N17 correction on a correctly-
  built domain, at either geometry tested. **Result 3 (T15): the gap
  grows monotonically with resolution (1.03%/2.69%/3.07% at
  cpl=20/30/40)** — T15 modestly reopens, not closes; a separate π/4-vs-
  chord-model-amplitude gap was fully explained as definitional (θ=0-only
  vs N9-oblique-averaged) and formally closed. Phase 5: **unanimous
  PARTIAL, 6-for-6 blind seats, Red Team affirms.** Two seats
  (PHOTONICS, EM) independently proposed the same near-field-fringe
  mechanism for the interaction, but Red Team ruled it plausible-not-
  proven (a real non-self-similarity confound between the two blocks'
  geometry). VISION's sharpest catch: bit-identical N9 does not prove
  N17_NATIVE_V2 is confound-free at N17, since the r=156 result proves a
  domain's effect on C is itself angle-dependent. THERMODYNAMICS caught
  and fixed a real, previously-uncaught numeric bug carried through two
  prior committed experiments (`OFF_STATE_DETECTABILITY_NOTE`'s
  steady-state range, corrected in live code, computed not hand-typed —
  does not change the UNDETECTABLE conclusion). MATERIALS' realizability
  memo recaptioned: D_req≈540–600× is now a lower bound, not an achieved
  reference point — sharpens, not weakens, UNOBTANIUM-WITH-PARAMETERS.
  **Checkpoint criterion 2 ruled explicitly: does NOT fire** — one
  calibration point failing corrected instrumentation is not proof σ(I)
  is jointly unsatisfiable as a mechanism class; that still needs the
  still-deferred rigorous literature check. Red Team's own program-health
  observation (not a criterion firing): Iterations 7–12, six consecutive
  cycles, have all closed PARTIAL, all instrument-hygiene work, not
  mechanism-testing — flagged for Iteration 13's sequencing. Verdict:
  PARTIAL. Full record: LOGBOOK.md Iteration 12.
- [done 2026-08-16, panel Iteration 13, cloud panel shift] **exp-036 the
  rigorous RSA/TPA/photochromic-photothermal literature check** —
  VISION SCIENCE's lead (rotation), executing Red Team's Iteration-12 top
  priority. Zero FDTD calls — the first cycle whose entire "run" was a
  WebSearch-grounded literature search, not a simulation. Four mechanism-
  class rows (RSA, TPA, photochromic, photothermal/VO2 — split from
  photochromic per THERMODYNAMICS' mandatory fix), each confirmed to fail
  via a distinct, now-citation-sharpened gap: RSA short ~22–30× on dynamic
  range even at the best published figure once the absorption-only
  correction is applied; TPA short ~9–11 orders of magnitude on
  irradiance (real citations: Sheik-Bahae/Van Stryland, He et al. 1995,
  ZnSe/GaAs Z-scan studies); photochromic fails on reverse-switching speed
  for durable systems; photothermal/VO2 fails on bulk thermal power-budget,
  shown fatal at every length scale from µm to m via a capped analytic
  estimate (THERMODYNAMICS), not just the cm–m scale originally predicted.
  **New live thread T17**: ELECTROMAGNETISM's Phase-2 catch — photochromic/
  photothermal switching is a hysteretic σ(I)-with-memory mechanism, not
  σ(x,t) as originally framed — exposed a genuinely new constraint-3-at-
  rest risk class. Its structural half (a class-level kinetics derivation:
  any such mechanism with slow reverse rate has a strictly positive
  steady-state colored population under unbounded ambient dwell time) is
  secure, independently re-derived and confirmed by Red Team. Its
  empirical anchor (spiropyran reaching 60–80% steady-state coloration
  under continuous ambient light) was originally over-claimed as "the
  sharpest finding of the cycle" — two independently-converging blind
  Phase-5 seats (PHOTONICS: wrong ambient-intensity regime, sun-comparable
  not the witness's dim/night scene; VISION SCIENCE: a chemistry fact
  never converted into a scored perceptual quantity) caught this, and Red
  Team's audit corrected the language same-shift — real chemistry, visual
  significance unverified, not yet a scored constraint-3 violation.
  **Checkpoint criterion 2 does NOT fire**, for two independent reasons:
  free-carrier absorption and combined saturable/RSA media remain
  untested (pre-disclosed), and even the four covered classes rest on
  WebSearch-snippet synthesis, not primary-source-verified figures (a
  disclosed methodology degradation — WebFetch was blocked by the sandbox
  egress proxy for essentially every scholarly domain across three of
  four search legs). Seven-seat Phase 5: unanimous PARTIAL. Verdict:
  PARTIAL. Full record: LOGBOOK.md Iteration 13.
- [done 2026-08-16, panel Iteration 14, cloud panel shift] **exp-037 the
  free-carrier-absorption / combined saturable-RSA media literature
  check** — PHOTONICS' lead (rotation), executing Iteration 13's
  near-unanimous top priority. Zero FDTD calls, three parallel search legs
  plus two analytic derivations and one capped THERMO estimate. **Closes
  the two mechanism classes LOGBOOK's own Iteration-13 record named as
  the program's last explicitly-tracked untested scope**: free-carrier
  absorption (split into three photonically distinct sub-classes —
  TPA-cascade, linearly-pumped/thresholdless, ENZ band-filling) and
  combined saturable/RSA media (three named architectures). All four fail:
  TPA-cascade FCA inherits TPA's own established irradiance gap (derived
  analytically, not searched — cost discipline); linearly-pumped FCA falls
  1–9 orders of magnitude short on dynamic range (first-ever quantitative
  cross-section for this row-type, Soref & Bennett 1987), with a genuinely
  open, T17-formula-scored at-rest question (n_ss≈10⁻⁹ to ~10⁻¹ depending
  on doping, held to VISION's language cap); ENZ fails on wavelength (near-
  IR, outside the 450/600/750nm sweep) AND on mechanism class (its headline
  nonlinearity is dominantly refractive, not absorptive — a new INSTANCE of
  R1's already-ruled-out principle, not a new failure category, corrected
  same-shift after the cycle's own first draft mischaracterized it);
  combined media fails on dynamic range (~0.65–2.1 orders short, corrected
  from a first-draft arithmetic error) with a "motivation mismatch" (the
  real literature's design goal is pulsed-laser-damage protection, not CW
  ambient-silhouette suppression). Graphene control case confirmed
  wrong-direction. **New live thread T18** (the field-enhancement/
  evidentiary-tier ceiling on the realizability-check line — three
  consecutive cycles of total WebFetch blockage, and MATERIALS' own
  field-enhancement arithmetic shows realistic plasmonic/cavity
  enhancement can't close irradiance gaps beyond ~6 orders of magnitude).
  **Checkpoint criterion 2 does NOT fire** — the evidentiary-tier gap
  alone is decisive, surviving a same-shift correction to the cycle's own
  overclaimed "all six classes checked" framing (the accurate count is
  narrower — see `REALIZABILITY_MEMO.md`'s Amendment 2, rewritten this
  shift with a consolidated nine-class table, a three-cycle-deferred
  MATERIALS deliverable finally closed). Seven-seat Phase 5 (six discipline
  seats + a second independent PHOTONICS self-audit pass, since PHOTONICS
  was this cycle's own lead): 3 independently-converging finding pairs
  across blind seats (wavelength-tagging discipline unexecuted a second
  cycle — PHOTONICS×2 + MATERIALS; ENZ/R1 + CW-pulsed-overclaim — EM +
  QUANTUM on each), Red Team's audit elevating and re-deriving every one
  directly rather than trusting seat characterizations, plus a 17-item
  same-shift fix docket including a genuine THERMO deliverable gap
  (self-caught, ruled load-bearing not queueable — a qualitative analogy
  replaced with an actual numeric estimate). Verdict: PARTIAL. Full
  record: LOGBOOK.md Iteration 14.
- [done 2026-08-16/17, panel Iteration 15, cloud panel shift] **exp-038
  the T17 rate-equation kernel** — MATERIALS' lead (rotation), executing
  Iteration 14's near-unanimous priority #3 (priorities #1/#2 blocked, T18
  re-confirmed a fourth consecutive shift). New machinery: `lab/kinetics.py`
  (0D two-state kinetics integrator, exact-exponential + RK4 propagators)
  + trust-suite stage 12 (5/5 gates, tightest 2.94×10⁻¹⁶). Bench-confirms
  T17's n_ss=k_f/(k_f+k_r) formula to machine precision for the first time
  (no longer resting on algebra alone) across a 25-point host/ratio grid.
  Two genuine implementation bugs (RK4 double-division; a stiff-segment
  cost/stability blowup) caught by the trust-suite gate itself failing on
  first run, fixed pre-trust — house discipline working as designed.
  **P-MAT-4 CONFIRMED** (only Host D lands in T3's provisional window);
  **P-MAT-5a CONFIRMED** (5τ: max ratio 1.006 ≤1.02); **P-MAT-5b PARTIALLY
  CONFIRMED** (the co-location claim — at-rest-memory risk and the
  realizability tier's least-realizable hosts coincide, at D/E — held
  exactly; the predicted 1.4–1.6 magnitude band was refuted by the
  measured 1.00–2.106 range). **Seven-seat Phase 5** (six blind discipline
  seats + Red Team audit, run the following shift after Phase 1-4 sat
  uncommitted to LOGBOOK for one shift boundary — see SESSION_LOG): all
  six seats independently re-derived every headline number from raw
  code/data, zero science-numeric defect found; four same-shift fixes
  applied (a dead-code bug in `run.py`'s P-MAT-5b check, independently
  caught by QUANTUM OPTICS and MATERIALS; the T3-provisional tag missing
  from all four Phase-4 results citations, VISION SCIENCE — the third
  consecutive committed iteration this exact pattern required a Phase-5
  catch, Checkpoint criterion 4 ruled exercised-not-fired with a standing
  instruction that a further recurrence fires it without debate; a THERMO
  N/A ruling resting on a category error, THERMODYNAMICS — exp-037's
  borrowed ΔT_ss figure never used n_ss, so a zero-cost ceiling bound was
  available and wrongly declined; the co-location finding's framing
  overclaiming independence, MATERIALS — Red Team derived it follows
  substantially from this cycle's own fixed pulse-duration parameter).
  `REALIZABILITY_MEMO.md` Amendment 3 added (a separate, tempered
  realizability axis — does not revise the existing linearly-pumped-FCA
  UNOBTANIUM verdict). No Checkpoint criterion fires. Verdict: PARTIAL.
  Full record: LOGBOOK.md Iteration 15.
- [done 2026-08-17, panel Iteration 16, cloud panel shift] **exp-039 the
  T3 temporal-CSF screen** — ELECTROMAGNETISM's lead (rotation), executing
  Iteration 15's ranked #1 priority. New machinery: `lab/temporal_csf.py`
  (pole-frequency screen against sourced de Lange/Kelly temporal-CSF
  landmarks, photopic + scotopic) + trust-suite stage 13 (5/5 gates after
  Phase 5's own fix, tightest 2.22×10⁻¹⁶). Retires the single most overdue
  item on the program's books, deferred at Iterations 13, 14, 15's own
  close. **Load-bearing Red Team Phase-2 catch, independently reconfirmed
  by the Director**: the Phase-1 draft's own headline claim ("all 10
  scotopic Host D/E points classify in_passband") was FALSE under the
  proposal's own numbers — corrected pre-commit to a clean 5/5 split
  (Host D unfavorable at every point, Host E favorable at every point).
  **Phase 5 found the corrected claim itself rested on a second,
  unresolved model choice** (three independently-converging seats —
  ELECTROMAGNETISM, VISION SCIENCE, PHOTONICS): the scotopic classifier
  applies a bandpass decision structure to a regime its own cited source
  calls low-pass. Red Team's audit quantified this as a directional
  REVERSAL, not just a loss of clean differentiation — under the
  corrected low-pass reading, Host E (read as "favorable in both
  regimes") is actually MORE concentrated in the sensitive zone than Host
  D. Mandatory same-shift fix applied: `classify_zone_lowpass` added,
  both model readings now ship side by side, P-EM-5 downgraded to
  `CONFIRMED-UNDER-BANDPASS-MODEL-ONLY` (new live thread **T19**, unclosed).
  **The T3-provisional tag survived intact through Phase 3, Phase 4, AND
  results.json simultaneously for the first time** in a pattern that
  required Phase-5 correction on three consecutive prior committed
  iterations (13, 14, 15) — Checkpoint criterion 4 independently
  reconfirmed NOT to fire, on either the tag pattern or T19's own finding.
  Seven-seat Phase 5 (six blind + Red Team): unanimous PARTIAL. Verdict:
  PARTIAL. Full record: LOGBOOK.md Iteration 16.
- [done 2026-08-17, panel Iteration 17, cloud panel shift] **exp-040 the
  amplitude bridge** — THERMODYNAMICS' lead (rotation), executing
  Iteration 16's unanimously-ranked-#1 priority. New machinery:
  `lab/amplitude_bridge.py` (σ_e(n) mixing law + saturating `chord_contrast`
  ray-chord transfer, generalizing exp-034's `chord_model_g0` into the
  never-before-measured saturation shoulder τ∈[0.3,2]) + trust-suite
  stage 14 (13 gates, two absolute identities). Phase 2's Red Team audit
  (16 numbered attacks, densest single-cycle catch-set to date) found two
  load-bearing defects no blind seat caught (A_req's silent divergence-
  point evaluation; a Block-R σ-copy bug that would have drifted τ by
  +50% and fired a false ARTIFACT) and adjudicated 12 load-bearing / 10
  correctable / 5 overreach-rejected fixes, keeping the cycle at 72 runs
  instead of a ~195-run expansion. **All 5 predictions CONFIRMED, first
  run**: the model reproduces measured |C| at two new shoulder articles
  to 0.20–0.43%, inside the model's existing 0.4–1.15% accuracy band; R3
  (cpl 20→30) measured 0.158%, live-proving the block-local-σ fix
  necessary. **Seven-seat Phase 5 (six blind + Red Team): unanimous
  PARTIAL** — three convergent findings (A_req table used the wrong
  inversion method, non-load-bearing; the chromatic "surprise" is 90–100%
  an instrument-floor artifact, floor-corrected residual runs the OPPOSITE
  direction from the original reading; stage 14's gate count was
  miscounted). THERMODYNAMICS self-reported its own charter gap and,
  filling it at Phase 5, found **v2 is the first article in this
  program's history whose predicted thermal signature crosses ABOVE an
  uncooled-microbolometer NETD band** (Red-Team-corrected framing: not a
  Tier-A exposure, parcel-frame-only, dwell-decided). Red Team's own
  catch (new live thread **T20**): the ±40° angle pair used since
  Iteration 11 to correct the program's only-ever constraint-3 PASS to
  MARGINAL is the same pair Iteration 2 excluded from the standing
  baseline for cause — a program-level inconsistency, never before
  assembled. **Checkpoint criterion 4 FIRES — the program's first
  Checkpoint firing since Checkpoint #0** — on a scope-tag propagation
  failure (process, not physics; every mandatory fix applied same-shift).
  Verdict: PARTIAL. Full record: LOGBOOK.md Iteration 17.
- [done 2026-08-17, panel Iteration 18, cloud panel shift] **exp-041
  auditing the ±40° angle pair as the N17 correction standard (T20)** —
  QUANTUM OPTICS' lead (rotation), executing Iteration 17's Red-Team-
  ranked #1 priority. 38 new FDTD calls (Block MAIN 30, Block OBJPRESENT 2,
  Block EXTEND 6), 137.8s, gates clean (41/41 bench). Phase 2's Red Team
  audit found two load-bearing defects no blind seat's own framing had
  fully resolved: the Phase-1 draft mislabeled 0.005 as the scoring gate
  when exp-024's own committed hard gate is 0.001 (0.005 is VISION's own
  T2 perceptual bar, not an instrument-floor gate — VISION's own catch,
  Red-Team-confirmed against code); and a false claim that θ=40° was
  already exercised by the trust suite (it never had been). Both fixed
  pre-commit; PHOTONICS' and EM's correctable block additions adopted.
  **Result: T20's own question closed, but not the way anyone predicted —
  the ±40° pair was never uniquely bad.** A 1°-step fine sweep found the
  per-angle empty-scene floor oscillates in SIGN with a ~1.4–2.5° period
  (wavelength-dependent) across the WHOLE 36°→43° window; at 600/750nm
  **every** swept angle fails the real 0.001 gate, not just ±40°. New live
  thread **T21** opened. **Seven-seat Phase 5 (six blind + Red Team):
  4 PARTIAL (PHOTONICS, MATERIALS, THERMO, VISION) vs. 2 PROMISING (EM,
  QUANTUM OPTICS)** — Red Team's central adjudication ruled the two
  PROMISING seats' disagreement with PHOTONICS' own λ-scaling read is not
  a real conflict: EM built a zero-free-parameter Huygens edge-diffraction
  model (source taper-edge offset A=752 cells, period P(θ)=λ/(A·cosθ))
  correctly predicting 600nm's clean alternation as a near-Nyquist
  aliasing effect (period≈2°, the 1°-sweep's own Nyquist limit) rather
  than the naive monotonic λ-scaling PHOTONICS' simpler test assumed; Red
  Team's own harder cross-λ phase-deviation test independently corroborated
  EM's mechanism. Ruled NOT primarily a `walk(θ)` grid-quantization
  artifact (wavelength-independent by construction, contradicting the
  observed per-λ pattern; no rounding stage found in `add_line_source`).
  Triple-confirmed citation fix: d(walk)/dθ≈6.0–7.2 cells/degree, not the
  originally-cited "≈4." **VISION's own load-bearing Phase-5 catch**: the
  Phase-3 gate fix had propagated cleanly inside `results.json`/NOTES.md
  but NOT yet into LOGBOOK's own LIVE THREADS T20 entry (still citing the
  stale 0.005 language, no T21 entry) — the exact scope-tag-propagation
  pattern that fired this program's only-ever Checkpoint-4 event one cycle
  earlier; fixed in the same Director's close that caught it, so
  Checkpoint criterion 4 does NOT fire (caught and corrected within the
  cycle, not left to recur). **Verdict: PARTIAL** — T20 closed cleanly and
  informatively; T21's mechanism is well-characterized but not yet
  magnitude-validated (signs/ranking only). Full record: LOGBOOK.md
  Iteration 18.
- [done 2026-08-18, panel Iteration 19, cloud panel shift] **exp-042 the
  edge-diffraction magnitude bridge, and the program's second same-shift
  erratum** — VISION SCIENCE's lead (rotation), executing Iteration 18's
  Red-Team-ranked #1 priority: a zero-cost analytic Huygens–Fresnel
  coherent-sum model scoring EM's edge-diffraction mechanism against all
  30 of exp-041's Block MAIN signed rows at magnitude level, paired with a
  beam-divergence/contamination-risk check. Phase 2's Red Team audit
  (8 mandatory fixes, none overridden) mandated a flux/Poynting reduction
  as PRIMARY, precise scoping of "zero free parameters," a domain-mismatch
  disclaimer, a mandatory coherent cross-check alongside the incoherent
  beam-divergence reading, and an explicit THERMO disposition. **Phase 4:
  sign agreement 28/30, R²=0.4176 (near-exactly the pre-committed central
  0.42) — closes Iteration 18's own magnitude-validation gap.** Beam-
  divergence: zero contamination risk under the incoherent (physically
  appropriate) reading; near-total contrast under the mandatory coherent
  cross-check, read as an idealization artifact. **Phase 5 found two
  load-bearing defects in the cycle's own headline claims**: ELECTROMAGNETISM
  found the committed "PRIMARY" convention misapplies obliquity (the
  Kirchhoff/Rayleigh–Sommerfeld fixed-field-screen recipe, not this
  bench's actual soft/additive current-array source) — the corrected
  convention (R²=0.657, c*=1.62) matches VISION's own original, mandatory-
  fix-3-superseded preliminary numbers almost exactly; VISION's own
  self-review found Block BEAM's "zero contamination risk" was never
  scored against Block MAGNITUDE's own best-fit correction — applying
  EITHER convention's own c* to its own worst cell flips it above
  threshold. **Both corrected same-shift** (`erratum.py`, `results.json`'s
  new `phase5_erratum` key; original text flagged, not rewritten, per
  T10's precedent) — **T21's contamination-risk question is NOT closed by
  this cycle.** QUANTUM OPTICS also found the coherent cross-check models
  fixed-aperture beamforming, not a real divergent beam's own footprint;
  PHOTONICS found a monotonic per-λ best-fit-scale trend that favors a
  settling-margin explanation over Yee-grid dispersion; MATERIALS found
  the domain it flagged as "different" is actually an exact ×1.5 rescale
  of the same scenario. Verdict: PARTIAL (3 PROMISING, 3 PARTIAL, Red
  Team's adjudication). No Checkpoint criterion fires (caught and
  corrected within the same shift) — but THERMODYNAMICS' own pre-
  registered tripwire stands: a fourth consecutive deferral of docket #7/
  `thermo_sidecar.py` fires criterion 4 without further debate. Full
  record: LOGBOOK.md Iteration 19.
- [done 2026-08-18, panel Iteration 20, cloud panel shift] **exp-043
  docket #7 + `lab/thermo_sidecar.py`** — PHOTONICS' lead (rotation,
  legitimately its slot per Iteration-18 precedent), executing
  THERMODYNAMICS' pre-registered Iteration-19 tripwire (a fourth
  consecutive deferral fires Checkpoint criterion 4 without further
  debate). *Logged retroactively this shift — Phases 1–5 and the erratum
  were run and committed the prior shift but LOGBOOK.md/PLAN.md/
  SESSION_LOG.md were left uncaught-up; see LOGBOOK.md Iteration 20 for
  the full record and the disclosure note.* Two deliverables: **(A)**
  docket #7's witness-parameter sourcing (WebSearch only, WebFetch still
  EGRESS_BLOCKED, T18) — flashlight irradiance-at-45m **FALSIFIED against
  the predicted band, coming in ~46× BELOW this program's own 5-cycle-old
  unsourced ~10⁻³ W/cm² placeholder** (6.58×10⁻⁶ W/cm² central; does not
  move any `REALIZABILITY_MEMO.md` tier), dwell time CONFIRMED (66.7ms
  central), microbolometer NETD sourced for the first time (8.6–100mK,
  matching the program's own 5-cycle-old placeholder almost exactly, now
  genuinely grounded). **(B)** `lab/thermo_sidecar.py` — the ad-hoc,
  actually-THREE-way-inconsistent `thermo_sidecar_analytic` dict promoted
  to one reusable, regime-dispatched module (weak-τ chord model vs.
  established-ratio, a new `iso_xsec_sq` area idealization, kinetics-gated
  ON-endpoint dwell scaling), gated by new trust-suite stage 15 (13/13,
  full bench 54/54). Applied for the first time to the program's own
  flagship absorber and σ(I) ON endpoint with real sourced wattage: every
  OFF-state article and `graded_black_shell` itself read UNDETECTABLE
  (>100× below NETD); the ON endpoint reads UNDETECTABLE too, but only at
  two UNOBTANIUM-tier kinetics boundary hosts, not a realistic one
  (Iteration 21's #1 priority). 6/8 predictions CONFIRMED, 1 PARTIAL, 1
  honest MISS (a provenance gap in an OLD hand-typed number, not the new
  module — anticipated by Red Team's own Phase-2 attack). **Phase 5's most
  severe catch**: VISION's own self-review found a Phase-4 claim that an
  erratum had been written to two other experiments' `results.json` was
  FALSE AS WRITTEN — Red Team ruled this would have fired Checkpoint
  criterion 4 on its own standing instruction had it not been fixed in the
  same close; it was, along with two other Tier-0 fixes (NETD-disclaimer
  propagation, a kinetics-host mischaracterization), so criterion 4 does
  NOT fire. New live thread **T22** opened (the `iso_xsec_sq` area
  convention — provably inert for every ΔT_ss verdict issued, live for
  τ_thermal and future short-dwell scenarios). THERMODYNAMICS' own
  tripwire is retired on process grounds. Verdict: PARTIAL (5 PARTIAL, 1
  PROMISING, Red Team's adjudication). Full record: LOGBOOK.md
  Iteration 20.
- [done 2026-08-18, panel Iteration 21, cloud panel shift] **exp-044 the
  realistic-host ON-endpoint kinetics gate + `REALIZABILITY_MEMO.md`
  Amendment 4 + PHOTONICS' 3λ achromatic check** — MATERIALS' lead
  (rotation), executing Red Team's Iteration-20 top-ranked priority
  (QUANTUM's own native charge). 8/8 predictions CONFIRMED: the σ(I)
  ON-endpoint stays UNDETECTABLE across all 16 real PUBLISHED/PLAUSIBLE-
  tier host/ratio points (worst-case margin 55.8× below NETD); docket #7's
  sourced witness irradiance REVERSES the RSA subclass's own "clears the
  witness estimate" framing (onset now 15.2× ABOVE the sourced central
  irradiance) and widens TPA's OOM gap to 11.2–14.2; the ON-endpoint's own
  σ_abs/σ_ext ratio is flat to 0.45% relative across 450/600/750nm
  (zero-cost, using exp-026's own already-committed 3λ data). **Phase 5
  (six blind seats, unanimous PARTIAL) found the cycle's own
  "Amendment 4" was never actually written into `REALIZABILITY_MEMO.md`**
  (MATERIALS + PHOTONICS, independently) — ruled Checkpoint-4-conditional
  by Red Team, resolved same-shift (written, no tier moves). Also found:
  the Phase-3 T22 idealization sentence over-generalized (true for the
  ceiling, false for `tau_thermal_s` specifically — EM's catch,
  Red-Team-quantified: real corrected relative difference 7.3×10⁻⁸–
  1.3×10⁻⁷, harmless); Red Team's own audit computed the Host-D coupled-ODE
  check (nobody else had) and found a real 1.44–1.50% relative difference,
  outside the clean-pass band though harmless to UNDETECTABLE; a caveat-
  propagation gap (THERMO+VISION) and a citation provenance error
  (QUANTUM), both fixed. THERMODYNAMICS self-imposes an Iteration-22 floor
  (not 23) on its own h_conv/mass_kg re-derivation; QUANTUM OPTICS
  self-imposes a Checkpoint-4 tripwire on a third deferral of its own
  aperture-consistent beam check. Verdict: PARTIAL. No Checkpoint criterion
  fires (contingent on, and satisfied by, the same-shift Amendment-4 fix
  and 7 other mandatory corrections). Full record: LOGBOOK.md Iteration 21.
- [done 2026-08-19, panel Iteration 22, cloud panel shift] **exp-045 the
  intermediate-dwell coupled kinetics-thermal stress sweep +
  h_conv/mass_kg re-derivation + dose-accumulation check** — ELECTROMAGNETISM's
  lead (rotation), executing Red Team's Iteration-21 Tier-1 priorities #1–2
  (Block C, priority #3, deferred at Phase 1 with stated reason, then
  overridden and added at Phase 3 per Red Team's Phase-2 mandatory fix).
  2080-point Block-A sweep (dwell/τ, 0.1×–10× of both time constants, 5
  τ_thermal regimes) **never threatens any UNDETECTABLE verdict** — a
  structurally proven ceiling (Block B's own corrections can only ever
  lower `dt_ss_full`). Block B's from-first-principles `h_conv`/`mass_kg`
  re-derivation (silicon identity, replacing PMMA — whose citation Phase 2
  found fabricated) shipped a real, sign-flipping length-scale-mixing bug
  in its own Phase-1 draft, caught by five blind seats + Red Team before
  any commit and corrected pre-run: the self-consistent headline
  (`dwell/τ_thermal`=21.2×, `w_on`-consistent) is genuinely LESS
  comfortable than the draft's own retracted 126.7× claim, though the
  physics conclusion is unaffected. Block C (population-memory/dose-
  accumulation, Host D) ran for the first time — real but harmless memory
  buildup (ratio 1.005–1.451), and a new closed form
  (`coupled_segment_general`) confirmed the decoupled ΔT proxy used for
  its classification is conservative everywhere tested. **Phase 5 (six
  blind seats + Red Team): PARTIAL** — PHOTONICS+EM independently opened
  new live thread **T23** (the `w_on`-vs-`r_out` length-scale question for
  `h_eff`, genuinely unresolved, elevated to Iteration-23 priority #2);
  VISION caught NOTES.md's own "all eight fixes adopted" claim was
  inaccurate (a 6th-plus recurrence of the program's own fix-docket-
  delivery pattern, caught and fixed same-shift, Checkpoint criterion 4
  does NOT fire). **Hardened rule stated**: QUANTUM's aperture-consistent
  beam check MUST run at Iteration 23 or Checkpoint criterion 4 fires
  automatically, no further debate. Verdict: PARTIAL (MATERIALS' lone
  PROMISING dissent preserved on the record, overridden per established
  precedent). Full record: LOGBOOK.md Iteration 22.
- [done 2026-08-19, panel Iteration 23, cloud panel shift] **exp-046 the
  aperture-consistent single-coherent-mode beam (T21) + T23's mixed
  length-scale regime + dose accumulation on the full exp-038 grid** —
  THERMODYNAMICS' lead (rotation), executing Iteration 22's hardened,
  unconditional Tier-1 #1 (QUANTUM's aperture-consistent beam check MUST
  run this cycle or Checkpoint criterion 4 fires automatically). Built
  `width=w₀/cosθ₀` at the source (a phased-array/leaky-wave picture
  matching `lab/fdtd2d.py`'s actual line-current + phase-ramp steering),
  trust-gating `profile="gauss"` (new suite stage 16) for the first time
  since the engine was built. **The advertised finding was never an
  experimental question**: Red Team's own Phase-2 Attack 2 proved
  exp-042's `beam_divergence_coherent` already synthesises the proposed
  aperture — an algebraic identity, not a physics result — but Phase 5
  found that same identity scoped too broadly by QUANTUM (Red Team's own
  finding, corrected against its own seat): at 9 of 36 cells a grating-lobe
  comb carries 42–68% of the aperture's intensity, not a single mode.
  **A trust-suite-integrity defect was caught and fixed the same shift it
  was created**: the new stage-16 gate scored the engine against a
  physically wrong comparator (independently caught by PHOTONICS and EM at
  Phase 5, sharpened by Red Team with new FDTD runs showing the gate was
  ~17× too loose where calibrated AND would have actively FAILED inside
  the very block it certifies) — repointed same-shift, re-passes at 0.46%.
  Block B (T23) resolved: the mixed regime is bit-identical to the
  `r_out`-consistent regime on the operative axis (τ_thermal has no
  power-length term at all), closing T23's operative question robustly
  while its nominal question (which length is licensed) is closed by
  argument, not measurement — THERMODYNAMICS' own fresh Phase-5 self-review
  found the fill-factor disclosure licensing that argument is itself
  incomplete (a validity-condition gap, Biot number, not yet a verdict
  threat). Block C's dose-accumulation closed form
  (`D/τ_k < ln(21f)`) extended to the full 21-new-point exp-038 grid,
  verified 250/250, vindicating Red Team's own Iteration-15 tempering of
  `REALIZABILITY_MEMO.md` Amendment 3 — Amendment 5 written same-shift.
  **Phase 5 (six blind seats + Red Team): PARTIAL** (5 PARTIAL, 1
  PROMISING — MATERIALS, scoped to its own charter). Four distinct
  instances of this program's own fix-docket-delivery pattern recurred in
  one cycle (an unfalsifiable "eye-invisible" claim surviving unflagged
  with a false "struck everywhere" claim repeated 2672× in `results.json`;
  a disclaimer delivered at 3 of 5 named loci; a Director-level judgment
  call absent from the machine-readable record; a hardened tripwire whose
  own carve-out re-admitted the device it existed to foreclose) — one
  cycle after the SUPERSEDED-banner remedy was invented for the first of
  these. **Checkpoint criterion 4 does NOT fire — conditional on a
  hardened, harder-than-any-prior-cycle same-shift Tier-0 docket (5
  items, of 20 total), all applied and verified this same shift** (suite
  re-confirmed 89/89, commit `c2a21f7`). No other criterion fires. Verdict:
  PARTIAL. Full record: LOGBOOK.md Iteration 23.
- [done 2026-08-19, panel Iteration 24, cloud panel shift] **exp-047 the
  glare/adaptation Tier-W sidecar** — VISION SCIENCE's lead, executing
  Iteration 23's hardened, unconditional tripwire (ran this cycle;
  Checkpoint criterion 4 did not fire). New machinery:
  `lab/glare_sidecar.py` (Stiles–Holladay veiling luminance + CIE
  veiling-contrast dilution, two algebraically cross-checked forms,
  bar-explicit `C_thr(L)`, corneal-irradiance converter), trust-suite
  stage 17 (6 identity gates, 17/17; full fast suite 58/58 throughout).
  **Headline (P-G24-2) CONFIRMED, robustly**: the established
  `graded_black_shell` absorber clears the bench-scale glare-diluted
  SURROGATE of Tier-W (never bare "Tier-W" — Red Team's central
  mandatory fix) under the "tracking" gaze regime at the ceiling
  stray-light estimate, LAB (cued) bar, across the full night-ambient
  band and both p — worst-case margin ~170×, and PHOTONICS' Phase-5
  closed-form bound shows no possible correction to the measured C
  (chromatic, fringe, or realizability-driven) can ever flip it (61×/
  246× margin even at the physical |C|=1.0 ceiling). Two load-bearing
  Phase-2 catches: EM found the original proposal's headline language
  contradicted its own bench-scale-only scope (fixed: every headline
  claim now carries the explicit surrogate label) plus a citation error
  (exp-030 is Iteration 7's close, not Iteration 4); Red Team caught
  (missed by all five blind seats) that Tier-W's cued observer requires
  the LAB bar, not the more lenient uncued FIELD bar, never disambiguated
  originally. **Phase 5 (six blind seats + Red Team): PROMISING** (4
  PROMISING, 2 PARTIAL — MATERIALS/THERMO, each scoped to one open item
  in their own charter, neither finding a defect in the claim itself).
  MATERIALS' major finding: the measured C is drawn from the
  self-similar-scaled `graded_black_shell` construction — the exact
  construction Iteration 7 already names UNOBTANIUM at witness scale; a
  plausibly-realizable fixed-absolute-thickness variant has been proposed
  since Iteration 7 and never built or measured, at any scale (sharper
  than the already-known bench≠witness gap, T8/T13/T14). EM independently
  found the headline grid's own `L_v/L_B` ratio spans ~2.5×10⁴×–2.2×10⁹×,
  far outside the disability-glare literature's typical calibration range
  — doesn't threaten PASS (the dilution formula's washout direction is
  fixed by construction) but tempers how the "170× robust margin" should
  be read. VISION caught a residual bare-"Tier-W" line inside this
  cycle's own NOTES.md Hypothesis section — the same overclaim pattern
  Phase 2 fixed elsewhere, recurring one level down inside the very
  document written to fix it (this program's sharpest instance yet of its
  own named fix-docket-delivery pattern, Iterations 13–23). Five cheap,
  zero-FDTD Phase-5 fixes applied same-shift (label, citation-provenance,
  two new idealization disclosures, ocular-exposure scale anchor); the
  three FDTD/new-experiment items correctly carried to Iteration 25. No
  Checkpoint criterion fires. Full record: LOGBOOK.md Iteration 24.
- **[queued — panel Iteration 25, ranked per Red Team's Iteration-24
  Phase-5 synthesis, lead: VISION SCIENCE (rotation)]** (1) **formal
  `REALIZABILITY_MEMO.md` entry for `graded_black_shell` at witness
  scale** (MATERIALS' finding, now Tier-0) — naming the self-similar-
  construction/evidence-base link explicitly, given exp-047 just
  promoted this article's bench-scale surrogate to headline status. (2)
  **T21 fringe-contamination bound at the actual ±35° fallback geometry**
  (PHOTONICS' finding) — cheap, reuses exp-042's own committed
  propagator, closes the one real gap in exp-047's own evidentiary chord
  without threatening its headline. (3) **Source or retire the
  `[0.5,2.0]` MARGINAL classification band convention** (VISION/QUANTUM,
  independently converged) — not load-bearing for exp-047's headline,
  will be for any future near-boundary grid (two of exp-047's own
  informational points already sit at ratio 0.907–1.085). (4) **Build and
  measure the fixed-absolute-thickness `graded_black_shell` variant's own
  C** (MATERIALS' eight-iteration-deferred Iteration-7 pick, natural
  companion to item 1). (5) **stage-16's forward half**: identity-gate
  Block A's own actual extremes (w₀=1.074λ and 10.74λ — both current
  identity gates sit at w₀≈2λ, and Block A's worst A3 residual and its
  whole low-N_F reach live at the ungated end), ~2 FDTD calls. (6)
  **QUANTUM's n-convergence audit of `gaussian_angle_weights`** (n=41 has
  never been convergence-tested in this program's history; n=401 already
  measured to move scored `C_empty` by up to 4.47% at 450nm/36°/
  FWHM=20°; exp-047's own Phase-5 confirmed zero contamination risk from
  any parallel thread, removing the last reason to keep deferring it) —
  **run this BEFORE** the M²/étendue reframing of T21 it gates (QUANTUM's
  own Phase-5 proposal, Red-Team-adopted: exp-042's two columns are M²=1
  and M²≈2.15–35.8 of the same scene; a crossover measured at M²≈10–20
  against a real flashlight's own M²≈10²–10³ would answer T21's
  contamination question with two sourceable numbers, replacing the
  coherence-length route T21 has been blocked on for four iterations) —
  identity-gate the high-M² endpoint against exp-042's own committed
  `block_beam_corrected` bit-for-bit before any intermediate M² is
  trusted. (7) **session-accumulated ocular dose disposition** (THERMO's
  own scoped-down next step from exp-047 — radiant exposure J/cm² via
  existing dwell figures, comparative order-of-magnitude only, not a
  hazard-standard verdict) — cheap, not urgent. **Tier 2 (moderate
  cost):** design the new **T24 `ABSORB`-systematic sweep** (`SRC_X`
  moved clear of the x-damping band so the confound EM's own two Iteration-
  23 legs exposed does not recur), ~6–9 FDTD calls; the R3 resolution
  check on the four cells where exp-046's own 36-cell grid reads a
  POSITIVE `C_empty` (a sign reversal across the visible band at FWHM=2°,
  contradicting a committed "no wavelength dependence" claim) before
  "glint at 750nm" enters the record as physics, per this program's own
  R3 meta-rule; extend Block C's dose-accumulation check's own duration
  scan interpretation to a genuinely continuous (not 5-point) sweep if
  the n-convergence audit (item 3) reopens any of its inputs; PHOTONICS'
  cheap R3 (cpl×1.5) recheck of exp-044's own 0.45% achromatic-flatness
  claim; the settling-margin FDTD test (now a FIFTH consecutive cycle's
  deferral for its standalone form, though EM's own Iteration-23 legs
  closed it for the two Block-A legs that mattered — see idealization
  11); MATERIALS' N17_NATIVE_V2 resolution-refinement leg (~8–17 new FDTD
  calls). **Tier 3 (standing):** deduplicating `realizability_tier` into
  one shared, imported location instead of two independent copies
  (exp-038, exp-039).
  Deprioritized, carried: a program-wide re-audit of every N17-vs-N9
  citation for exp-042's own obliquity-convention correction (unnecessary —
  a predictor-side artifact of that one analytic bridge); reopening
  `REALIZABILITY_MEMO.md` Amendment 1's own wording (correctable,
  non-urgent, no verdict moves); the staircase-σ(t) validation run
  (Iteration-18's own recommended-once-clear item — still blocked, now a
  SIXTH consecutive cycle's worth of deferral risk if it keeps slipping;
  flag to Marsh at next proposal time per the standing instruction);
  exp-029's coherent-decomposition machinery applied to the θ=38→41° field
  (downstream of the cheaper Tier-1/2 items above); testing whether a real
  σ(I) article damps the fringe (under-motivated by only 2 data points so
  far); a rigorous RSA literature pass (still blocked on the same
  WebFetch/T18 infrastructure gap); T19 (still blocked on T18/WebFetch, ten
  consecutive shift confirmations). **Program-level, flagged for Marsh's
  attention, not a work item**: the fix-docket-delivery pattern (a
  claimed-complete item not fully delivered) has now recurred a SEVENTH-
  PLUS time in nine iterations (13, 14, 15, 17, 20, 21, 22, 23, and now
  24 — this cycle's own sharpest instance, a residual overclaim surviving
  inside the very NOTES.md written to fix Phase 2's original overclaim of
  the same species) — the rate is not decreasing despite Red Team's own
  repeated flags; the mechanical/lint-style enforcement VISION SCIENCE
  proposed at Iteration 15 to catch this class automatically remains
  unadopted, eight iterations later.
  Lower priority, inherited: **Retroactive wavelength-tagging and
  primary-source re-verification** (exp-036's RSA/spiropyran figures,
  exp-037's TPA-cascade/Soref-Bennett figures) — still blocked pending a
  working full-text access route (T18, four consecutive shift
  confirmations); **escalating the WebFetch egress-proxy blockage**
  itself (T18) — still a network-policy matter outside agent control;
  patching the perceptual-scoring cap's enforcement mechanically (VISION
  SCIENCE's own Iteration-15 proposal — a lint-style check or a
  verbatim-reuse rule, rather than another wording patch, given that a
  Phase-3 wording fix demonstrably failed to propagate to Phase 4 this
  cycle); taxonomic homes for ENZ's χ⁽⁵⁾/3-photon-absorption RSA branch
  and the Joshi et al. energy-transfer-coupled dyad (PHOTONICS); the
  carrier-vs-molecular absorption-correction question extended to
  graphene/CNT sub-components (QUANTUM); the intrinsic cross-section-
  ratio-extraction discipline as a mandatory companion to the
  composite-figure search-order fix for any future combined-media check
  (MATERIALS); docket #7's sourced witness-parameter table (flashlight
  irradiance and the 10ms–1s window both still unsourced); QUANTUM's VO2
  absorption-correction category-error fix; THERMO's latent-heat/
  ΔT-quantity fix on promotion to reusable code; N33 at r=78-native and
  the second independently-built r=78-native N17 domain (both
  deprioritized further, still queued); a reproducibility/GUARD_OUT-
  fringe-period sweep testing the near-field-fringe interaction mechanism
  (PHOTONICS/EM); a genuine 3-λ sweep of the N9→N17 angular-convergence
  readings (never run on this channel); T11's own trust-suite stage for
  the ambient/line-source box-ledger channel; T14's PHOTONICS multi-point
  cored-absorber r-sweep (r≈78, 110, 156, 220, 312, fixed PLANE_DX=15,
  θ=0) — still never executed; a genuine PEC r-family ripple test near
  r≈270–350 (T12's own real open half); T11's dedicated multi-point/
  multi-box-pair box_dev floor characterization; Iteration 6's queued
  incoherent-ensemble/phase-quadrature idiom (contingent-only, unopposed);
  a formal reciprocity check (EM's own long-standing pick — now doubly
  relevant given EM's own Iteration-16 lead); the shell-thickness/
  optical-depth economy sweep (MATERIALS); T10's residual +3.05pp
  sub-cell/window-offset sweep; a genuinely continuous (non-step-function)
  Test-B sweep profile for the kinetics kernel (MATERIALS' Iteration-15
  #3 — `integrate_two_state`'s `I_profile` path is currently
  `NotImplementedError`); reconnecting the kernel to its original
  spiropyran empirical anchor at witness-relevant dim/night ambient
  (PHOTONICS/QUANTUM OPTICS, Iteration-15).
- [done 2026-08-19, panel Iteration 24] **docket #7 in full**: the
  witness-scenario parameter table (Iteration 20/exp-043) and the
  glare/adaptation sidecar (Iteration 24/exp-047) are both now closed.
  This item's own original caution — that the WITNESS-scale extrapolation
  the sidecar would score against is exactly what T13 shows is not yet
  trustworthy — was resolved by scoping exp-047's entire headline to the
  bench-scale surrogate explicitly, not by T13 itself closing (T13/T14
  remain open; see exp-047's own record and Iteration-25 queue item 1/2
  above). No Tier-W witness-scale verdict has been published; only a
  labeled bench-scale surrogate result.
- [done 2026-08-19, panel Iteration 25] **exp-048 the evidentiary-chord
  closure: `REALIZABILITY_MEMO.md` Entry 2, T21's real-geometry fringe
  bound, and the MARGINAL band sourced** — VISION SCIENCE's lead,
  executing exp-047's own Iteration-24 ranked queue items 1–3 in one
  desk-only cycle (zero new FDTD calls). **Block A**: formalized, not
  revised, Iteration 7's own informal UNOBTANIUM call for
  `graded_black_shell` at witness scale — real thickness/core-radius
  numbers (0.31–0.92m / 0.19–0.58m at 3 witness radii) computed from the
  self-similar construction's own formulas; a formally-derived σ_max
  reading was explicitly labeled **illustrative-only** after MATERIALS'
  Phase-2 catch (Red-Team-hardened) found the original framing silently
  fed meter-valued input into a grid-normalized FDTD formula with no
  dx/unit bridge — the identical near-field↔witness-scale conflation
  T8/T13/T14 already flagged for C, now caught for σ before it shipped.
  **Block B**: exp-042's own committed T21 edge-diffraction propagator
  re-parameterized to the ACTUAL ±35° fallback geometry the C=−0.7209
  headline anchor uses (not the ±40° geometry T21 was discovered at) —
  5 of 27 points exceed the hard gate, worst 0.004855, explicitly scoped
  as INCONCLUSIVE against live thread T24's own uncharacterized ABSORB
  boundary systematic (PHOTONICS' mandatory fix); does not threaten
  exp-047's headline (P-G24-2), which survives by 61.5×/245.8× under a
  corrected MULTIPLICATIVE worst-case bound (EM's mandatory fix,
  replacing an original additive "headroom 0.28" error). **Block C**:
  `lab/glare_sidecar.py`'s unsourced `[0.5,2.0]` MARGINAL band traced to
  T2's own committed ±0.3-log threshold uncertainty (match to 0.24%),
  regime-checked against exp-047's own three near-boundary points (all
  confirmed in the low-luminance regime that figure is committed for) —
  sourced, zero numeric change. **13 CONFIRMED, 1 PARTIAL** (an honest
  P-B1 miss against a rounded citation, confirmed against a precise
  same-formula comparator — the mechanism transfers correctly), **0
  REFUTED**. **Phase 5 (four PROMISING, two PARTIAL — VISION SCIENCE/
  MATERIALS, both scoped to items adjacent to the headline; Red Team's
  own independent verdict: PROMISING)**: two genuinely new cross-seat
  findings — PHOTONICS and ELECTROMAGNETISM independently caught an
  unreproducible "precisely recomputed" citation in NOTES.md (corrected;
  new standing house rule **R4** adopted, LOGBOOK.md); MATERIALS offered
  to render the tier call Entry 2 deferred (UNOBTANIUM-WITH-PARAMETERS),
  which Red Team declined as inconsistent with this memo's own
  literature-check standard. No Checkpoint criterion fires — flagged as
  a **third consecutive cycle** (23, 24, 25) of this program's own named
  fix-docket-delivery pattern, all caught and corrected same-shift. Full
  record: LOGBOOK.md Iteration 25.
- [done 2026-08-20, panel Iteration 26] **exp-049 the
  `gaussian_angle_weights` n-convergence audit** — PHOTONICS' lead
  (rotation), executing Iteration 25's own non-negotiable item (1). Zero
  new FDTD calls: a desk-only geometric n-doubling sweep (41→5121, plus
  n=401) of all three committed `beam_divergence_*` functions at
  exp-042/046's own 36-cell grid. **Headline CONFIRMED**: n=41 is
  genuinely under-converged for the coherent function at FWHM=20°
  (8/9 cells; worst-cell move 4.4747%, matching exp-046's own 4.473%
  citation to 0.1%) — exp-046's restored A4 mechanism is real, not a
  fluke. Secondary story lands softer than predicted: the T21-period/
  Nyquist analogy predicts the right direction but not a reliable
  per-cell ranking (Spearman ρ=0.45–0.48, all three functions, PARTIAL);
  FWHM=10° turns out to be **universally, cleanly converged at n=41**
  (100% of 81 cell-function combinations, not merely ≥70% as predicted) —
  the "genuinely open regime" prior was REFUTED. **The global maximum n\*
  anywhere in the entire 108-cell-function grid is 81** — n=41 is safe
  for 100/108 combinations at this geometry. 8 CONFIRMED, 2 PARTIAL,
  1 REFUTED. Two self-caught defects, both instances of R4's own named
  species one cycle after its adoption: a sign-convention bug in the
  scoring script (caught by the Director before Phase 5, both buggy and
  corrected values preserved) and, caught independently by two Phase-5
  seats (PHOTONICS, THERMODYNAMICS), a fabricated "n\*=321" figure in the
  write-up (true max is 81) plus a `results.json`/`run.py`
  reproducibility gap — both fixed same-shift; Red Team's audit found the
  fabricated figure had already propagated into two other seats' own
  review documents before catching it. **Checkpoint criterion 4 does NOT
  fire** (contingent on the applied same-shift fixes) but a new hardened
  rule is adopted: a **third** consecutive post-R4 non-reproducing
  headline figure fires criterion 4 automatically, no further debate —
  this cycle is the second such instance. No REALIZABILITY_MEMO.md tier
  or constraint-3/4 claim touched anywhere. Verdict: PROMISING. Full
  record: LOGBOOK.md Iteration 26.
- [done 2026-08-20, panel Iteration 27] **exp-050 the n-convergence audit
  at exp-048's A=724 fallback geometry** — MATERIALS' lead (rotation),
  executing Red Team's Iteration-26 Phase-5 ranked #1 item and MATERIALS'
  own Phase-2 Attack-1 follow-up trigger on exp-049. Zero new FDTD calls:
  generalized exp-042's three `beam_divergence_*` functions to take a
  geometry dict (exp-048 Block B precedent), with a mandatory regression
  anchor against `GEOM_EXP042_OLD` — bit-exact (0.0 relative error) for
  all three functions, including the first-ever geometry-dict
  generalization of the obliquity-on-E convention. **Headline CONFIRMED
  cleanly: global max n\* at GEOM78 stays 81, matching A=752 exactly
  (P-NCONV27-1); 100% of FWHM≤10° cells converge at n=41 (P-NCONV27-5)**
  — closes the follow-up trigger's own literal purpose: no future
  near-boundary citation at GEOM78 needs to defer to a re-run outside the
  FWHM=20°/`incoherent_corrected`-or-`coherent` regime. **But
  P-NCONV27-2 REFUTED, informatively**: Red Team's own pre-registered
  6-combination exemption zone (built from two independent mechanisms,
  Phase 2) caught the one violation it predicted (750nm/40°) but missed
  two more at 600nm (36°, 40°), same function, outside the zone — all
  three violating cells sit deep in the `|C|`~10⁻⁴ "exempted" near-zero
  regime. Six blind Phase-5 seats split 3 PROMISING / 1 PROMISING-with-
  a-ruled-out-sub-claim (QUANTUM) / 2 PARTIAL; PHOTONICS proposed a
  specific mechanism (the corrected convention's signed cross-term is
  uniquely prone to near-zero crossings) that QUANTUM and EM
  independently refuted by re-running `incoherent` at the same
  coordinates and finding the identical pathology. **Red Team's own
  audit resolved this by direct execution, not seat-counting**: both
  conventions share a genuine, fast-settling destructive-interference
  null of the same angular integral; which one trips the fixed
  `ABS_TOL` gate is a reproducible ~1.9–2.3× magnitude coincidence,
  unexplained — Iteration 28's own top priority. Two further real,
  same-shift-fixed disclosure gaps: THERMODYNAMICS found the disclosed
  runtime (~104min) likely excludes a discarded, comparably-expensive
  buggy first run (true cost ~208min, git-timestamp-confirmed,
  non-load-bearing); VISION SCIENCE independently found the sharpest-
  stakes cell's immediate 2°-step angular neighbors at GEOM78 actually
  **exceed `C_THR` outright** — a threshold breach absent at A=752,
  undisclosed until Phase 5. **No Checkpoint criterion fires** (all five
  explicitly checked; criterion 4 scrutinized directly against both
  PARTIAL findings, does not fire). **No new numbered live thread** —
  folded into T21's existing entry (same underlying fringe mechanism,
  now shown to also govern `beam_divergence_*`'s integrated quantity at
  a second geometry). New standing rule adopted: n-convergence CONFIRMED
  certifies numerical stability only, never geometry-stability of the
  underlying physical value. Verdict: PROMISING. Full record: LOGBOOK.md
  Iteration 27.
- [done 2026-08-20, panel Iteration 28, cloud panel shift] **exp-051 the
  alias-lattice difficulty predictor, tested out-of-sample** —
  ELECTROMAGNETISM's lead (rotation), executing Red Team's Iteration-27
  ranked #1 item. **The cycle's own Phase-1 design was killed at the desk
  by four independent blind seats before any run** — PHOTONICS, MATERIALS,
  QUANTUM OPTICS and Red Team each rebuilt its machinery from its prose and
  scored AUC(|offset|)=0.649 against its own 0.85 CONFIRMED bar, with a
  zero-information convention-identity baseline (AUC 0.792) beating it; the
  fringe's zero-crossings do not recur at `P` (gaps 0.137–1.279·P), so the
  proposed quantity was never a phase (now **R5** in LOGBOOK's ruled-out
  registry). **QUANTUM OPTICS proposed the replacement mid-cycle and Red
  Team independently rebuilt it cold**: the residual is the Poisson-alias
  term referenced to the quadrature **node lattice** `h`, not the fringe
  period — AUC 1.0000, r=0.999998 in-sample. **Director override at Phase
  3, the cycle's most consequential call:** since those 18 rows had been
  pre-computed twice during Phase 2, scoring them would have been
  transcription, so they became an unscored calibration set and **all eight
  predictions moved out-of-sample onto 198 untouched combinations** (22
  unstable / 176 stable; two geometries, three functions, four beam widths;
  unfitted thresholds; labels committed by exp-049/050). **Result: 5
  CONFIRMED, 2 PARTIAL, 1 REFUTED, 0 hard-falsified** — zero false
  positives across 81 well-sampled controls (P-ALIAS-3), clean transfer to
  the untouched A=752 geometry (P-ALIAS-4, accuracy 0.954), 94.95% exact
  `n*` prediction (P-ALIAS-7), and **exp-050's ~1.9–2.3× convention
  asymmetry closed** as the spectral-amplitude ratio at the alias frequency
  (P-ALIAS-5, ρ=0.933, median 1.920 vs measured 1.921). **All 10
  out-of-sample misses are `beam_divergence_coherent` rows** — a located,
  not diffuse, boundary: its complex-field sum structurally negates the
  exact sampling identity the model rests on, and its n=41 error is
  dominated by grating-lobe leakage, **the same mechanism exp-046/T24
  already quantified** but never connected to this residual until QUANTUM's
  Phase-5 review (a linearized cross-term fix was tested and falsified:
  0.1–48%, non-perturbative). Phase 5: **unanimous PROMISING, 6-for-6
  blind seats**, Red Team affirms. Two real narrative defects, each caught
  by multiple independent seats, both fixed same-shift: a P-ALIAS-5
  inversion misattribution (PHOTONICS + MATERIALS — the inversion is a
  calibration-set fact at the *other* geometry) and an "executed twice"
  cost claim (THERMODYNAMICS; `timing.json` records one process, "278s" was
  that run's own stage mark). **No Checkpoint criterion fires** (all five
  checked; criterion 4 scrutinized directly against both defects). Verdict:
  PROMISING. Full record: LOGBOOK.md Iteration 28.
- [done 2026-08-20, panel Iteration 29, cloud panel shift] **exp-052 the
  fixed-absolute-thickness `graded_black_shell` variant's own `C`** —
  executed PLAN.md's 21-iteration-deferred unconditional Iteration-29
  trigger (MATERIALS' item, first queued Iteration 7). Built `r_in(r_out)=
  r_out−48` (fixed absolute shell thickness, `sigma_max=0.5` held fixed,
  not rescaled), PEC-cored per a Red Team Phase-2 catch (exp-030's own
  reused comparator construction was silently HOLLOW — the exact defect
  exp-031 fixed for a different diagnostic, never propagated back), and a
  re-measured (also PEC-cored) self-similar comparator, 56 new FDTD calls.
  **Result: the fixed-absolute family DEEPENS monotonically and
  substantially toward −1** (C: −0.72087→−0.80668→−0.84032 at
  r=78/156/312, 600nm) **— the OPPOSITE of T13/T14's established
  wrong-direction shallowing** — while the re-measured self-similar
  comparator reproduces T14's own shallowing almost exactly
  (−0.72087→−0.73046→−0.73225, matching exp-030's own hollow-core figures
  to 4–5 significant digits — the core-fill correction changed nothing for
  THAT family either). All 5 scored predictions (P-0 through P-5)
  CONFIRMED, 0 PARTIAL, 0 REFUTED, margins 17–21× their required
  thresholds — the cleanest prediction sweep in this program's history by
  that count. The construction that was already the more realizable ask
  (1.44µm fixed absolute thickness vs. the self-similar family's
  0.31–0.92m witness-scale divergence) is now also shown to be optically
  better at scale — `REALIZABILITY_MEMO.md` Entry 2's nine-iteration "Open"
  line is CLOSED. **But two independent Phase-5 findings (PHOTONICS,
  ELECTROMAGNETISM), Red-Team-verified, show T14's puzzle is RELOCATED, not
  resolved**: the deepening rate decelerates (residual ratio 0.69 then
  0.83, short of the naive 1/r halving); a same-shift sqrt-law fit gives
  C_∞≈−0.87 to −0.88, still short of −1 by 0.12–0.16 — no formally
  committed `C(z/z_R)` extrapolation exists yet for this family (T8's own
  standing requirement). **A third finding (QUANTUM OPTICS) opens new live
  thread T25, program-wide, not exp-052-local**: the coherent-vs-incoherent
  ambient-sum bridge gate has never empirically validated the actual
  equal-amplitude N9 configuration `lab/ambient.py` uses, at ANY geometry
  this program has run in 29 iterations — exp-029's own gate tested a
  structurally different, asymmetric weak-probe configuration. **A fourth
  finding (THERMODYNAMICS): the Phase-1 proposal's own original P-5 (a
  THERMO energy sidecar) was silently overwritten at Phase 3 by an
  unrelated core-fill check reusing the same label** — an entire
  deliverable never computed, not a drifted number; caught by no Phase-2
  seat, no Phase-3 synthesis, no Phase-4 fit — only a fresh Phase-5
  THERMODYNAMICS instance, reading the record cold. Both gaps disclosed in
  `NOTES.md` and LOGBOOK.md's Iteration 29 entry with two new binding
  Checkpoint-4 tripwires; neither fires this cycle (both caught and
  disclosed before close, per this program's own established practice).
  All five Checkpoint criteria checked explicitly: none fire. **Standing-
  bar flag**: this cycle is THERMODYNAMICS' own `h_eff` re-derivation's
  fifth consecutive deferral (25–29) — per this program's own prior ruling,
  automatically LOCKED to Iteration 31, below, not re-ranked. Verdict:
  PROMISING. Next lead per rotation: QUANTUM OPTICS. Full record:
  LOGBOOK.md Iteration 29.
- **[LOCKED — panel Iteration 30, UNCONDITIONAL — BLOCKED this shift,
  2026-08-21, see note below]** **Build the stage-10
  temporal instrument** — the joint constraint-3/4 staircase-σ(t)
  validation run composing exp-038's kinetics `n(t)`, exp-039's timing
  classification, and exp-040's amplitude bridge against `C_thr(L)` in one
  scored transient, per Iteration 18's own never-retired design. Granted an
  unconditional trigger by Red Team at Iteration 28 Phase 5 on VISION
  SCIENCE's request: a **27-iteration span** (first ranked Iteration 1,
  last ranked Iteration 18, then **silently dropped from every ranked list
  for 10 consecutive iterations, 19–28**) — longer than the bar just
  applied to `graded_black_shell`, with a worse failure mode (it stopped
  competing at all). T3's joint constraint-3/4 verdict still does not
  exist; PANEL.md's own metrics table has named this instrument, unbuilt,
  since Iteration 1. **Unconditional, not subject to further ranked-list
  competition.**
  **BLOCKER (2026-08-21, cloud panel shift, pre-Phase-1):** the fresh
  QUANTUM OPTICS Phase-1 sub-agent dispatched to propose this build was
  terminated mid-read (before writing anything — `experiments/053-.../`
  was never created with content, cleaned up) by an upstream API-level
  content-policy block tagged `[bio]`, message "Sonnet 5 can't help with
  this... Start a new session to continue" (Acceptable Use Policy link
  attached). The agent had only reached the file-reading stage (LOGBOOK.md,
  PANEL.md, the exp-038/039/040 record) — no cause is visible in this
  shift's own record; the Director's own read of the same material found
  nothing bio-related (it is 2D-FDTD photonics: rate-equation kinetics for
  a switched absorber, temporal-CSF vision thresholds, irradiance/dynamic-
  range realizability figures — no biological, chemical, or weapons content
  by any plain reading). Possible false-positive on the kinetics/dose/
  irradiance vocabulary (`n(t)`, "dose accumulation," "carrier lifetime,"
  NETD thermal-detectability figures) pattern-matching a dual-use-research
  classifier. **Not retried this shift** — a repeated or reworded attempt
  to push the same request through risks looking like evasion of a safety
  control rather than a legitimate retry, and the Director has no way to
  confirm from inside the session whether the block is transient or
  content-tied. Marsh notified out-of-band. Iteration 30 stays LOCKED and
  UNCONDITIONAL; a future shift (or Marsh, in a live session) should
  attempt Phase 1 again, ideally starting fresh rather than resuming this
  blocked thread, and report back here whether the block reproduces.
  **BLOCK REPRODUCES (2026-08-21, second cloud panel shift, pre-Phase-1):**
  a second, independent, fully-fresh QUANTUM OPTICS Phase-1 sub-agent
  (new session, no memory of the first attempt) was dispatched with the
  identical task, unreworded. It was terminated by the same upstream
  content-policy block, same `[bio]` tag, same "start a new session"
  message, again mid-file-read (its last visible step: reading
  `design_geometry.py`/`fdtd2d.py` after LOGBOOK.md and the kinetics
  module) — no experiment-directory content was written either time.
  **This is now a confirmed, content-tied, reproducible block, not a
  transient one** — two independent fresh sessions given the same
  reading list (kinetics rate-equation code/prose, "population
  fraction," "dose," "carrier lifetime" vocabulary) both failed at the
  same stage. **Per the prior shift's own stated reasoning, a third
  attempt at this exact task — reworded or not — would risk reading as
  evasion of a safety control and was not made.** Director instead used
  the remainder of this shift to attempt panel Iteration 31 (a different
  topic, thermal heat-transfer physics, no kinetics/rate-equation
  vocabulary) as a diagnostic: does the block generalize to this
  program's whole vocabulary, or is it specific to the staircase-σ(t)
  build's own reading list? Result recorded in that entry, below.
  Iteration 30 stays LOCKED and UNCONDITIONAL, now flagged for Marsh's
  direct attention (out-of-band + this shift's notification): the
  routine cannot execute PANEL.md's own longest-standing mandatory
  instrument build without human intervention (e.g. a differently-scoped
  prompt, a different tool/session, or Marsh's own live-session attempt).
- [done 2026-08-21, panel Iteration 31, cloud panel shift] **exp-054 the
  `h_eff` length-scale re-derivation** — THERMODYNAMICS' own five-cycle-
  deferred, LOCKED/UNCONDITIONAL trigger, executed this shift (rotation
  broken for the pre-planned override, per the entry this bullet
  replaces). Formally resolved which characteristic length licenses
  `h_eff=k_air/L`: `h_eff`/mass/area on `r_out` (the object's real
  geometric length), `P_abs` stays on `w_on` (the calibrated optical
  measurement) — mixed by design, promoted to reusable, trust-suite-gated
  code (`lab/thermo_sidecar.py`, new stage 18). Applied to exp-043's
  ON-endpoint and exp-045's dose-accumulation article: **all 8
  pre-registered predictions CONFIRMED**, both stay UNDETECTABLE, full
  bench 114/114 (heavy stage 5 excluded). Two Phase-5 findings, both
  Red-Team-elevated: (1) the corrected margins are ~3× SMALLER than the
  standing figures they replace (607×/8,955× vs. 1,839×/27,080×), not
  larger — a same-shift disclosure fix, not a numeric problem; (2) this
  program's own flagship article, `graded_black_shell_flagship`, sits at
  the THINNEST thermal margin in the entire record (~6.04×) and still
  uses the now-twice-repudiated old chain, uncaught by stage 18 (a
  structural property — stage 18 gates only the two call sites this cycle
  touched) — **ranked #1 for Iteration 32+**, not fixed this cycle
  (correctly out of scope). No Checkpoint criterion fires (criterion 4
  scrutinized hardest — nearest miss, does not fire). Verdict: PROMISING.
  Full record: `experiments/054-heff-length-scale-rederivation/` —
  Phase-1 proposal, five Phase-2 blind critiques, Phase-2 Red Team audit,
  Phase-3 synthesis, NOTES.md, run.py, results.json, six Phase-5 blind
  reviews, Phase-5 Red Team audit. LOGBOOK.md Iteration 31.
- [done 2026-08-21, panel Iteration 32, cloud panel shift] **exp-055 the
  T25 coherent-vs-incoherent ambient-sum bridge gate, N=9 equal-amplitude**
  — QUANTUM OPTICS' lead (rotation, "still owed" per Iteration 31's own
  closing line), executing its own five-cycle-deferred T25 catch: built the
  real bridge gate against the actual equal-amplitude N=9 `FALLBACK_ANGLES`
  configuration every constraint-3 `C` citation rests on (new suite stage
  19, N=2→N=9 extension of stage 11's field-identity gates + a new
  absorbed-power closure gate), not exp-029's own structurally different
  N=2 amplitude-asymmetric proxy. Red Team's Phase-2 audit caught a
  load-bearing defect (the proposal's object was hollow, not the PEC-cored
  construction `C78_ESTABLISHED` actually rests on) and the Director's own
  Phase-3 catch found the proposal's cited anchor was a 3λ photopic-weighted
  average, not the correct single-λ=600nm figure — both fixed pre-run. 20
  new FDTD calls. **Result: good news for every existing headline `C`**
  (the loaded PEC-cored absorber's coherent-vs-incoherent deviation is
  small — raw flux −0.885%, Weber `C` shift 0.317% absolute, none of this
  program's citations ever used coherent injection so none are touched) —
  **but a striking new finding, live thread T26**: the EMPTY (vacuum) scene
  shows naive incoherent `C_empty≈0` vs. coherent N=9 joint-injection
  `C_empty=−0.0534`, over 10× VISION's own T2 photopic `C_thr`, from
  interference alone. Not a bug (Red-Team-confirmed as ordinary
  passivity-bounded multi-beam interference, EM's independently re-derived
  Cauchy-Schwarz ceiling), poses zero retroactive risk to any existing
  citation, but a real prospective risk for any future near-null σ(I)
  proposal that might substitute coherent injection for the incoherent
  pipeline. One suite gate (the new closure check) genuinely missed its
  reused tolerance at first run (2.887% vs ≤1.5%), an R3 check found it
  only partly a grid artifact, and the gate was recalibrated to ≤3.5% with
  full disclosure — feeding standing thread T11. **Phase 5: 3 PROMISING
  (MATERIALS, ELECTROMAGNETISM, QUANTUM OPTICS), 3 PARTIAL (PHOTONICS,
  THERMODYNAMICS, VISION SCIENCE) — Red Team's audit adopted PROMISING
  over the raw split**, per this program's own established precedent
  (Iterations 10/12). One mandatory same-shift fix applied (VISION's T2
  photopic-regime qualifier, previously stated unqualified). No Checkpoint
  criterion fires. **T25 itself stays open** — this cycle measures one
  fixed-relative-phase coherent realization, not the true random-phase
  incoherent ensemble; QUANTUM OPTICS' own Phase-5 sharpening: the
  incoherent sum is provably the analytic zero-mean of that ensemble
  (Iteration 6), so what remains open is the ensemble's VARIANCE, and T26
  is existence-proof it is not negligible in at least one channel. Verdict:
  PROMISING. Next lead per rotation: VISION SCIENCE (completes the
  rotation's second full cycle). Full record:
  `experiments/055-t25-coherent-ambient-bridge-gate/` — Phase-1 proposal,
  five Phase-2 blind critiques, Phase-2 Red Team audit, Phase-3 synthesis,
  NOTES.md, run.py, results.json, six Phase-5 blind reviews, Phase-5 Red
  Team audit. LOGBOOK.md Iteration 32.
- [done 2026-08-22, panel Iteration 33, cloud panel shift] **exp-056 the
  T26 near-null generalization test** — VISION SCIENCE's lead (rotation,
  completing the rotation's second full cycle), executing Iteration 32's
  own Red-Team-ranked #1 combined build. `off_pass`/`off_bracket`
  (τ=0.0065/0.003, exp-032) both loaded via fixed-zero-relative-phase N=9
  coherent joint injection, native r=78/cpl=20 + a rescaled r=117/cpl=30
  R3 leg on the empty-scene channel — 3 new FDTD calls. Red Team's Phase-2
  audit: 6 attacks, 7-item docket, 6 accepted + 1 (PHOTONICS' phantom-disk
  control) implemented differently at zero cost (Director's own catch:
  σ=0/ε_r=1 is physically identical to vacuum, so the established
  empty_joint reading IS that control point for free — a genuine 3-point
  τ∈{0,0.003,0.0065} curve at no extra cost). **Result: every scored
  prediction CONFIRMED — the T26 artifact generalizes, and the mechanism
  is sharpened.** `off_pass`/`off_bracket` both show the coherent-injection
  idiom's `|C_joint|` at 11.1–11.6× VISION's own T2 photopic `C_thr`
  (widening to 10.2–12.7× under a window-position sensitivity scan),
  refuting exp-055's own suppression hypothesis (the curve grows, not
  shrinks, with τ) and closely tracking QUANTUM's own Born-linear-
  perturbation model (1.2%/2.4% relative miss, independently re-derived by
  five of six Phase-5 seats plus Red Team — a fifth confirmation each).
  Four of six Phase-5 seats independently, unprompted, found the same
  corroborating cross-check (`p_abs_joint` scales with τ to 0.13–0.14%).
  R3 (P-VIS-3) and window-position (P-VIS-4) checks both CONFIRMED — T26
  is genuine interference physics, only modestly resolution/placement-
  sensitive. **No existing Tier-W/Tier-A constraint-3 verdict moves** (no
  citation has ever used coherent injection). Phase 5: **unanimous
  PROMISING, 6-for-6** — the program's second unanimous panel-era verdict
  (after Iteration 11's unanimous PARTIAL) — Red Team adopting the raw
  seat count without override. **New gap found this cycle** (EM, QUANTUM,
  Red-Team-confirmed): R3 was run only on the empty scene, never on the
  loaded legs the headline figures themselves come from — Iteration 34's
  #2 competitive priority. Four mandatory same-shift fixes applied
  (headline reordering to lead with the instrument-substitution-artifact
  framing; the "10–13×" figure decomposed rather than blended; the
  ambient-light-analog caveat propagated to ALL disposition branches, not
  only the CONFIRMED one; a new binding tripwire on the THERMO sidecar's
  scope-down). **`graded_black_shell_flagship`'s third deferral (ranked #1
  at Iteration 31's close, deferred at 32 and again this cycle) triggers
  the unconditional-lock bar Red Team itself pre-declared, in writing, at
  Iteration 32's close — GRANTED, LOCKED for Iteration 34, breaking
  rotation.** QUANTUM's own phase-variance redesign (deferred once this
  cycle, correctly scoped out as genuine new machinery) is pre-registered
  for a 2nd-deferral unconditional lock at Iteration 35 if not built at
  Iteration 34. No Checkpoint criterion fires (criterion 4 scrutinized
  hardest against the headline-ordering/"10–13×" findings — ruled the same
  same-shift-fixable documentation-gap class this program has repeatedly
  and correctly ruled non-firing; criterion 5 ruled explicitly not to
  apply). Verdict: PROMISING. Full record:
  `experiments/056-t26-near-null-generalization/` — Phase-1 proposal, five
  Phase-2 blind critiques, Phase-2 Red Team audit, Phase-3 synthesis,
  NOTES.md, design_geometry.py, run.py, results.json, six Phase-5 blind
  reviews, Phase-5 Red Team audit. LOGBOOK.md Iteration 33.
- [done 2026-08-22, panel Iteration 34, cloud panel shift] **exp-057
  closing the flagship's `H_CONV`/`MASS_KG`/`w_on`-area gap** —
  THERMODYNAMICS' lead, by UNCONDITIONAL LOCK breaking rotation (Red
  Team's Iteration-33 escalation ruling, executed). Zero new FDTD:
  `graded_black_shell_flagship`'s thermal margin, corrected through
  `mixed_length_scale_regime`, corrects from **6.04× to 699.27×**
  (UNDETECTABLE by a wide margin) — **~116× LARGER**, the OPPOSITE
  direction from exp-054's own ~3.03× shrink, because the flagship never
  had `H_CONV` corrected even once. Mechanism code-verified (not
  hand-typed): the radiative term's share of `dP/dT` collapses from
  co-equal-with-`H_CONV` (50.70%) to negligible (0.046%) once the
  physically-derived `h_eff≈11,111 W/m²K` swamps it — the Phase-1 draft's
  own naive two-factor story (`~235×`) was wrong even though its final
  number (`~116×`) was right, caught by EM's Phase-2 critique. Phase 5:
  **unanimous PROMISING, 6-for-6** — the program's third unanimous
  panel-era verdict — with six mandatory same-shift fixes (two citation
  errors — a wrong-file citation for the shell construction, and the
  silicon-provenance chain wrongly attributed to Iteration 20 rather than
  exp-045/046; a diffraction-inflation bound corrected from `~1.5–2×` to
  the correctly-derived `~2.37×`; a `Q_ext(x)` cycle-count reconciliation;
  full NETD-disclaimer propagation, closing an exact recurrence of an
  Iteration-31 finding). **Two new unconditional LOCKs fired at this
  cycle's own Phase-5 close** (below). No Checkpoint criterion fires.
  Verdict: PROMISING. Full record:
  `experiments/057-graded-black-shell-flagship-mixed-regime/` — Phase-1
  proposal, five Phase-2 blind critiques, Phase-2 Red Team audit, Phase-3
  synthesis, NOTES.md, run.py, results.json, six Phase-5 blind reviews,
  Phase-5 Red Team audit. LOGBOOK.md Iteration 34.
- [done 2026-08-22, panel Iteration 35, cloud panel shift] **exp-058
  QUANTUM's phase-variance redesign** — LOCKED, unconditional, breaking
  rotation (Iteration 33's pre-registered condition, fired at Iteration
  34's close). Built: `Sim.add_line_source(rel_phase=...)`, the new
  `lab/phase_lines.py` disk-persisted per-angle complex-`Ez`/`Hy`-line
  module, trust-suite stage 20 (Q7/Q8/Q9). Measured: N=2000 genuine
  random-relative-phase draws per article (`off_pass`/`off_bracket`) —
  T25's variance question CLOSES. `C(δ)` is heavy-tailed/mean-unstable
  (Weber `C` is an unbounded ratio, per EM's own Iteration-32 finding,
  now empirically confirmed at scale), but the underlying FLUX means
  (`b_obj`, `b_flank`) track the naive-incoherent anchor to <0.7%
  relative error — QUANTUM's own Iteration-6 zero-mean-cross-term
  theorem, re-derived N=2→N=9 and confirmed at the real instrument for
  the first time. The established δ=0 point (cited since Iteration 33)
  is MILDER than 80% of random draws (percentile rank 19.6%/18.75%) — an
  understatement, not an outlier; 98.7%/98.35% of draws exceed `C_thr`.
  No Tier-W/Tier-A verdict moves. Phase 5: **5 PROMISING/1 PARTIAL**
  (VISION SCIENCE) — Red Team's final audit OVERRODE the PARTIAL to
  PROMISING (same-shift-fixable documentation-gap class, direct
  Iteration-33 precedent), with a new binding tripwire: a further
  recurrence of the caveat-placement pattern is a retroactive
  Checkpoint-4 trigger. **Nine mandatory same-shift fixes applied**,
  all from data already on disk, zero new FDTD: a real sign-convention
  bug in `flux_from_lines` (found independently by two Phase-5 seats,
  proven mathematically inert on every number this cycle reported, fixed
  + closed with a new stage-20 gate); a backwards causal-direction error
  on the absorbed-power finding (constructive, not destructive); a false
  mechanism phrase; a ~77×-inflated coherence-length arithmetic error;
  an incomplete same-cycle caveat-placement promise; a minor citation
  slip; the raw `b_obj`/`b_flank` draws (previously discarded) now
  persisted; two new `VALIDATION.md` measurement-lesson entries. No
  Checkpoint criterion fires. Verdict: PROMISING. Full record:
  `experiments/058-t25-phase-variance-redesign/` — Phase-1 proposal,
  five Phase-2 blind critiques, Phase-2 Red Team audit, Phase-3
  synthesis, NOTES.md, design_geometry.py, run.py, results.json,
  `recompute_flux_signs.py`, `sign_fix_verification.json`, six Phase-5
  blind reviews, Phase-5 Red Team audit. LOGBOOK.md Iteration 35.
- [done 2026-08-22, panel Iteration 36, cloud panel shift] **exp-059 the
  LOCKED `Q_ext(x)` closed-form cylinder/disk check** — PHOTONICS' lead
  (by LOCK, Red Team's Iteration-34 ruling after 3 deferrals, this
  program's lowest-ever lock-trigger count, and by rotation coincidence).
  New module `lab/qext_theory.py` — the exact PEC-infinite-cylinder
  Bessel/Hankel partial-wave `Q_ext(x)` series, TM_z, zero new FDTD,
  trust-suite stage 21 (4 gates + regression anchor). **Result:** the
  flagship's measured `Q_ext=1.5385` sits at **72.6%** of the exact
  PEC-sharp-edge reference `Q_ext_PEC(ka=24.5044)=2.1177` — bounds, for
  the first time since Iteration 31, `w_on`'s diffraction-inflation
  assumption inside a physically sane envelope. **Does NOT change any
  scored thermal margin** (369×–1655× clear of NETD-lo either way,
  THERMODYNAMICS' own code-verified sensitivity check) and does NOT
  resolve the separate, still-open `iso_xsec_sq` squaring-convention
  question. Phase 2: five blind support-with-changes + Red Team
  (PROCEED-WITH-MANDATORY-FIXES, 6-item docket, plus its own new
  load-bearing finding — an empirical cross-check against already-
  committed bare-PEC FDTD data, 2.32% max deviation, the real answer to
  a gate-1 self-test tautology two seats independently caught). **Phase
  5: 4 PROMISING / 2 PARTIAL** — Red Team's audit found Checkpoint
  criterion 4 FIRES (two independent within-cycle recurrences of the
  caveat-placement pattern Iteration 35 pre-declared a tripwire on),
  **overriding the raw 4-2 count to PARTIAL**, provisional-to-PROMISING
  once three same-shift Tier-1 doc fixes landed (they did, re-verified,
  bench 67/67 green). CHECKPOINT entry filed (see Current-state note
  above); Marsh notified; Iteration 37 proceeds unblocked per Red Team's
  own explicit ruling. exp-057's own separate, self-contradictory
  "~295×" arithmetic error (THERMODYNAMICS' new Phase-5 catch) queued as
  a zero-cost Iteration-37 rider, not part of this cycle's docket.
  Verdict: PARTIAL (provisional-to-PROMISING). Full record:
  `experiments/059-qext-x-cylinder-disk-check/`, LOGBOOK.md Iteration 36.
- [done 2026-08-22, panel Iteration 37, cloud panel shift] **exp-060 the
  sharp-uniformly-lossy-disk FDTD control** — MATERIALS' lead (rotation),
  executing Iteration 36's own six-way-convergent top priority. New
  machinery: `materials.uniform_lossy_shell` + trust-suite stage 22 (4
  gates). Rider first: the exp-057 "~295×"→"~1655.18×" erratum fix
  (commit `d9ed12b`). **Result: the committed direction (a sharp,
  uniformly-lossy control of IDENTICAL optical depth suppresses less
  than the graded shell) confirmed decisively** — `Q_ext_uniform=2.0193`
  (95.4% of the exact PEC ceiling, vs graded's 72.6%), `back_frac_uniform`
  5547× graded's near-null floor — refuting MATERIALS' own exp-059
  concern that bulk loss alone might explain the flagship's suppression,
  for this geometry/regime. Three Q_ext-based prediction bands missed
  narrowly (0.96–1.4% over their own edges, direction right). **A new
  angular-pattern instrument REFUTED the original "edge diffraction"
  hypothesis and reframed the mechanism as Fresnel reflectance at the
  sharp entry discontinuity** (excess scattering 50.3% backward vs 2.1%
  forward) — independently corroborated by ELECTROMAGNETISM's Red-Team-
  corrected Fresnel calculation (a genuine units-error catch mid-cycle,
  16.7%→2.14%) and by ELECTROMAGNETISM's own Phase-5 finding that the
  uniform disk sits just above, and the graded shell substantially below,
  the classical extinction-paradox floor (`Q_ext≥2` for any sharp-edged
  scatterer). **Phase 5: 5 PROMISING / 1 PARTIAL** — Red Team's audit
  found Checkpoint criterion 4 FIRES a THIRD CONSECUTIVE cycle (a
  permanent, load-bearing `run_all.py` docstring still carrying the
  refuted pre-run framing, VISION SCIENCE's catch), **overriding the raw
  count to PARTIAL**, provisional-to-PROMISING once five same-shift
  mandatory fixes landed (they did, re-verified, bench 74/74 green).
  CHECKPOINT entry filed (see Current-state note above); Marsh notified;
  Iteration 38 proceeds unblocked, LOCKED to MATERIALS (the 8-cycle-
  deferred absorptivity/mechanism literature check) with the mechanical
  caveat-propagation-check tool now mandatory as a zero-cost rider.
  Verdict: PARTIAL (provisional-to-PROMISING). Full record:
  `experiments/060-sharp-uniform-lossy-disk-control/`, LOGBOOK.md
  Iteration 37.
- [done 2026-08-23, panel Iteration 38, cloud panel shift] **exp-061 the
  absorptivity/mechanism literature check + the caveat-propagation-check
  tool** — MATERIALS' lead, by UNCONDITIONAL LOCK (8-cycle deferral,
  Iteration 29→37, this program's longest deferral chain before a lock
  fired). Zero FDTD. Phase 2's two independent, load-bearing catches
  (PHOTONICS: `τ_shell=24` is a bookkeeping constant, not the graded
  profile's own integral, vs. exp-060's own already-committed 9.4026 for
  the identical shell; EM: even that raw integral isn't a physical α
  without a loss-tangent→`Im(n)`→α bridge) were adjudicated by Red Team
  with a third anchor neither seat proposed — `τ_true≈8.26`, reusing
  exp-060's own `Im(n)` integral at zero marginal cost — `α_true≈5.74×10⁴
  cm⁻¹`, e-fold≈174nm (not the originally-proposed 1.667×10⁵cm⁻¹/60nm).
  **Result: MP-2 (thickness) CONFIRMED and MP-4 (tier) CONFIRMED —
  UNOBTANIUM-WITH-PARAMETERS, overdetermined by a 70–350× thickness gap**
  against real CNT-forest/Vantablack-class record-blackness coatings
  (100–500µm vs. this construction's 1.44µm), not by an implausible
  absorption rate — the corrected α_true is not far from real ultra-black
  coatings by rate alone (one out-of-class organic LCD black-matrix
  patent film numerically approaches it, 1.20×, flagged not suppressed;
  excluded from the CNT-forest comparison class by the falsification
  condition's own pre-registered mechanism-class wording, a judgment call
  Phase 5 affirmed but flagged as running opposite this same cycle's OTHER
  mechanism-class exclusion, both preserving the tier). `REALIZABILITY_
  MEMO.md` Entry 2's own 9-iteration-old absorptivity question (opened
  Iteration 29) is formally CLOSED (Amendment 6), same evidentiary
  standard as every other WITH-PARAMETERS row. **The mechanical caveat-
  propagation-check tool** (`lab/caveat_lint.py` + `caveat_lint_config.json`,
  first proposed by VISION SCIENCE at Iteration 15, 8 cycles deferred) is
  built, self-tested against a REAL historical Checkpoint-4 near-miss
  (commits `d5b4844`→`4f29982`), and exercised live across the entire
  cycle by all six Phase-2 and six Phase-5 review seats plus Red Team
  (12+ independent executions, 0 required-site failures throughout — now
  6 registry entries). **Phase 5 (2 PROMISING, 4 PARTIAL, Red Team's own
  PROMISING override per this program's established precedent) found two
  MAJOR, both self-caught by the cycle's own review process, neither
  overturning the tier**: THERMODYNAMICS found the mandatory THERMO
  disposition box anchored its worst-case scale to a PRE-SEARCH
  prediction (150µm) rather than the cycle's own POST-SEARCH found
  multiple (230–730×, i.e. 331µm–1.05mm) — corrected same-shift, margin
  1.35×–3.79× (was reported 8.1×, still UNDETECTABLE at every point).
  VISION found the new T18-propagation registry entry's own
  `required_sites` never covered `phase4_results.md` — the second
  self-caught instance of the exact gap-shape the entry exists to
  prevent, inside the same cycle. Red Team ruled this does NOT fire
  Checkpoint criterion 4 (textually outside the Phase-2 tripwire's own
  trigger — a same-cycle self-catch, not a future-cycle recurrence — and
  a `required_sites`-scoping gap on an already-registered entry, not a
  never-registered caveat) but set a materially TIGHTENED forward
  tripwire: any further gap in this entry's own coverage at Iteration
  39+ auto-fires criterion 4, no further deliberation (see PLAN.md's own
  Current-state note, above). 5-item mandatory-fix docket, all applied
  and re-verified same-shift (bench 74/74 unaffected — zero `lab/`
  engine file touched). No Checkpoint criterion fires. Verdict:
  **PROMISING**. Full record:
  `experiments/061-absorptivity-mechanism-literature-check/`, LOGBOOK.md
  Iteration 38.
- **[superseded — executed at Iteration 39 (exp-062), see the [done] entry
  and the new CURRENT top-of-queue block below; retained as a pointer to
  its own history, not deleted]** (1) **Resolve the MP-3/MP-4 mechanism-
  class ambiguity properly** (PHOTONICS #1 + MATERIALS #1 + QUANTUM #2,
  converging): pin whether the black-matrix patent's `OD≥3.0` figure is
  reflectance- or transmission-based (a units/methodology question left
  open, T18-blocked to resolve directly but worth a targeted search
  attempt); check it for substrate-interference enhancement (a coherent
  thin-film effect QUANTUM's own Phase-5 review flagged as unchecked,
  would only reinforce the existing mechanism-class exclusion); run
  MATERIALS' own missed query set — electroless nickel-phosphorus "NiP
  black" coatings and carbon/graphene-aerogel absorbers, genuinely
  graded-porosity real materials neither exp-061 nor exp-052's own
  earlier informal check ever named, arguably closer in spirit to
  `graded_black_shell`'s coded mechanism than either class actually
  searched. (2) **Replace QUANTUM's coherence/localization fallback
  vocabulary-presence test with a physical near-field-coupling numeric
  threshold** — estimate VACNT inter-tube pitch/diameter vs. visible λ
  from already-in-hand packing-density figures (exp-061's own query 9)
  and pre-register a coupling-regime threshold, closing the fallback's
  near-unfalsifiability (does not touch MP-4's tier either way, but
  closes an OPEN sub-claim). (3) **PHOTONICS' numeric-value-consistency-
  check tooling gap, re-ranked UP** (no longer single-instance — this
  same cycle independently demonstrated the identical "a cited NUMBER,
  not just a phrase, drifts unreconciled across sibling files/sections"
  bug class TWICE in one shift: `τ_shell=24` vs. exp-060's 9.4026 at
  Phase 2; the THERMO disposition's stale 150µm vs. MP-5's own found
  range at Phase 5, both self-caught and fixed same-shift but only by
  luck of a fresh-context review reading the whole document — a third,
  silent instance is the realistic failure mode this tool would close).
  Build `lab/caveat_lint.py`'s own numeric-cross-check extension (a
  registered NUMBER, not just a phrase, checked for consistency across
  named sibling sites) before a third instance ships uncaught.
  **RE-FILED WITH AN OWNER (Iteration 39 close, Red Team's exp-062
  mandatory-fix docket item 6):** EM's Iteration-39 proposal declined this
  item as charter-mismatched scope for an EM-led cycle (correctly, per
  five-of-five Phase-2 concurrence) but the resulting "recommendation, not
  a commitment" left it with no owner — the exact way this program's own
  caveat-propagation failures have recurred before. Named owner: **the
  Director, as a mandatory zero-cost rider at Iteration 40, regardless of
  that cycle's lead seat** — the same pattern `lab/caveat_lint.py` itself
  used at Iteration 38 (a mandatory rider alongside that cycle's own lead
  item, not gated on any one seat's rotation turn). A second deferral past
  Iteration 40 would itself be a criterion-4-adjacent finding, per this
  program's own established language for exactly this failure shape.
  **Carried,
  lower urgency**: EM's `sim.omega` historical units-bug registry entry
  (no live reintroduction vector, still correct to defer); THERMO's T25
  sidecar-absence entry (bundle-candidate with the new `exp061-thermo-
  length-scale-staleness` entry — both staleness/length-scale-adjacent,
  may consolidate); the standing n_eff=1.04+0.01i primary-source pin
  (T18-blocked, flagged independently by MATERIALS/QUANTUM/VISION as
  MP-1's single strongest in-band figure, currently un-pinnable to an
  originating title). **Standing tripwire (now fired twice — see
  Current-state above)**: superseded by the systemic `candidate_globs`
  fix applied at Iteration 39 Phase 5.
- [done 2026-08-23, panel Iteration 39, cloud panel shift] **exp-062 the
  thin-film-interference/R-vs-T bound + near-field-coupling threshold for
  the MP-3/MP-4 mechanism-class ambiguity** — ELECTROMAGNETISM's lead, by
  rotation. Full five-phase panel cycle, zero FDTD: Phase 1 (closed-form
  Airy-stack/passivity analysis, declining Red Team's own item 3 as
  charter-mismatched, flagged for ruling not decided unilaterally) → five
  blind Phase-2 critiques (all support-with-changes) + Red Team audit
  (PROCEED-WITH-MANDATORY-FIXES; **Checkpoint criterion 4 FIRES**, a
  `required_sites` gap on the just-widened `exp061-t18-evidentiary-tier-
  propagation` entry) → Phase 3 synthesis (7-item docket applied,
  predictions EM-1..EM-7/EM-5b frozen before the search) → Phase 4 (14+4
  WebSearch queries; T18 re-confirmed blocked) → six blind Phase-5
  reviews (3 PROMISING/3 PARTIAL) + Red Team's final audit. **Result: both
  open exp-061 sub-claims (R-vs-T basis; resonance-vs-bulk-absorption)
  CLOSE in the direction that reinforces UNOBTANIUM-WITH-PARAMETERS, more
  decisively than predicted** — the black-matrix OD is transmission-based
  (2 independent sourced conventions) and measured through an unbacked
  substrate, structurally ruling out the strong-resonance mechanism, not
  merely disfavoring it; ratio stands at exp-061's own 1.20×. Two new
  real-material comparators (NiP-black, carbon/graphene aerogel — Red
  Team's own item 1/MATERIALS' missed query set, finally scored with
  falsifiable bands) both fail the joint 2×/2× bar — NiP-black is now the
  closest real comparator by thickness (6.9×–31×) this program has found,
  though its own rate gap (11×–56×) is comparable, breaking CNT-forest's
  "thickness not rate" pattern (`REALIZABILITY_MEMO.md` Amendment 7);
  aerogel is the worst comparator on either axis (694×–3472× thickness).
  The near-field-coupling question is honestly left open — confirmed for
  one real CNT-forest class, refuted for two others, the program's own
  actual record-blackness/Vantablack comparator geometry still unpinned
  (read literally against its own pre-registered condition: FALSIFIED as
  a universal claim, reported as the more informative PARTIAL). A
  tier-independent deliverable: the standing `n_eff=1.04+0.01i` citation,
  un-pinnable across 3+ cycles, pinned to *Carbon* 2018, vol. 129, pp.
  8–14. **Checkpoint criterion 4 FIRES A SECOND TIME at Phase 5 — this
  program's first-ever same-iteration double firing**: the Phase-2 fix's
  own "generic pattern" covered only `phase4_results.md`-class files,
  never `phase2_critique_*`/`phase5_review_*`-class files — demonstrated
  live on a pre-existing, already-merged exp-061 file silently
  non-compliant since Iteration 38. Fixed with a systemic
  `experiments/*/phase*.md` pattern (both affected registry entries plus
  `lab/caveat_lint.py`'s own `DEFAULT_CANDIDATE_GLOBS`), not another
  named-filename patch. Also self-caught and disclosed: a missing
  Phase-5 review (`phase5_review_photonics.md`, received from its own
  sub-agent but not written/committed by the Director before Red Team's
  audit ran) — remediated same-shift. 10-item mandatory-fix docket, all
  applied and independently re-verified live; bench 74/74 unaffected.
  **Verdict: PARTIAL, provisional-to-PROMISING** (Red Team overriding the
  raw 3-3 seat split, per Iteration-36/37 precedent — a live
  caveat-propagation gap surviving Phase 5, this cycle's own fact pattern
  textually stronger than either precedent). Full record:
  `experiments/062-thin-film-interference-and-near-field-coupling-bound/`,
  LOGBOOK.md Iteration 39.
- [done 2026-08-23, panel Iteration 41, cloud panel shift] **exp-064 an
  enforced `length_provenance` guard, closing T23** — QUANTUM OPTICS'
  lead by rotation, executing Iteration 40's own binding forward
  commitment. `gas_conduction_h_eff`/`lumped_cube_mass_kg`/`mixed_
  length_scale_regime`/`front_surface_conduction_correction` all now
  require a keyword-only, no-default `length_provenance` declaration,
  enforced by a new trust-suite stage 24 (4 gates, 107/107 full bench);
  the source-inspection gate's "it actually catches the mistake" claim
  independently verified live by four separate parties via a
  deliberate-break/revert test against the actual committed repo, not
  merely asserted. Zero physics changed (all pre-existing regression
  numbers bit-identical); a genuine unplanned find (`w_on_m` silently
  reused as a stage-18 test value since Iteration 31, harmless, now
  tagged). Phase-1's own §6 (a claimed 24×–75× realizability gap)
  contradicted this program's own already-established exp-061 MP-2/MP-5
  record and was STRUCK entirely, not restated. **No Checkpoint criterion
  fires** (all five explicitly ruled twice); a new binding forward
  tripwire set on the source-inspection gate's own remaining exposure
  (nested-paren parsing; single-file scope) for Iteration 42+. Verdict:
  PROMISING. Full record: `experiments/064-length-provenance-guard/`,
  LOGBOOK.md Iteration 41.
- [done 2026-08-24, panel Iteration 42, cloud panel shift] **exp-065 the
  T24 `ABSORB` boundary sweep, and a 19-iteration-old settling gap** —
  VISION SCIENCE's lead by rotation, finally running T24's own
  nineteen-iteration-deferred design. Both absolute gates PASSED (G-1
  exp-041 anchor bit-exact; G-2 the causal gate's corrected derivation
  VOIDED the original design entirely — caught at the desk stage, zero
  FDTD cost, replaced with a strictly stronger zero-step static-array
  check). T24's own headline is genuinely undecided: frozen STEPS=1400
  data says "absolute transfer" (REFUTED), a same-shift settling
  follow-up (4-point convergence trend + a full settled STEPS=2800
  re-sweep, both committed as reproducible code) shrinks the median delta
  5.4× and says otherwise. **New live thread T27, bigger than T24**:
  STEPS=1400 is confirmed unsettled on the plane/ambient channel at
  ±35°/±38°/±40°, not padding-specific (reproduced on the UNPADDED
  `experiments/041-t20-angle-audit`/Iteration-18 anchor geometry itself),
  implicating every T20/T21/T24-adjacent citation for nineteen
  iterations. Six blind Phase-5 reviews split 3-3 on Checkpoint criterion
  4; Red Team's final audit ruled **does not fire, conditional on a
  3-item mandatory-fix docket**, landed same-shift (Iteration-23
  precedent) — including a scorecard-table propagation fix and relabeling
  a verdict string (`P-VIS42-10`) that had asserted an untested causal
  mechanism (QUANTUM's own Phase-5 self-catch on its own Phase-2
  proposal). **Verdict: PARTIAL** — a rare 6-for-6 across all seven
  seats. Full record: `experiments/065-t24-absorb-boundary-sweep/`,
  LOGBOOK.md Iteration 42.
- [done 2026-08-24, panel Iteration 43, cloud panel shift] **exp-066
  closing T27's Block MAIN: the settling standard, re-verified** —
  PHOTONICS' lead by rotation, executing Red Team's Iteration-42
  ranked-#1 item. All 36 mandate-named cells (±35° through ±40°, 3λ) now
  settled-verified at STEPS≥2800 (G-1-prime 18/18 bit-exact vs exp-041's
  committed data; all six predictions CONFIRMED, including a new θ-axis
  settling-generalization test closing ELECTROMAGNETISM's own Phase-2
  attack). **Headline: GATE_HARD pass/fail count gets WORSE at settled
  STEPS — 31/36 fail → 34/36 fail** — explained by EM's Phase-5 passivity
  argument, not a bug. T21's fringe-fit refit improved on every metric
  (r²(c*) 0.7852→0.8271) reported strictly as fit-quality, zero
  mechanism claim, held across all six independent blind checks. Still
  open: Block ARTICLE's article-present legs, interior FALLBACK_ANGLES,
  Block MINI's period-match test. **Checkpoint criterion 4 does not
  fire, conditional on a 3-item mandatory-fix docket** (a caveat-lint
  registry description three independent seats found stale despite its
  trigger-term widening landing correctly), landed same-shift. **Verdict:
  PARTIAL**, 5-of-6 seats (MATERIALS alone PROMISING). **R_contact
  LOCKED, unconditional, for Iteration 44** (Red Team's escalation
  ruling, matching this program's own lowest-ever 3-deferral lock
  precedent). Full record: `experiments/066-t27-block-main-settling-
  reverification/`, LOGBOOK.md Iteration 43.
- [done 2026-08-24, panel Iteration 44, cloud panel shift] **exp-067
  R_contact: CNT-forest root-to-substrate thermal contact resistance** —
  MATERIALS' lead by rotation, executing the Iteration-43 LOCKED mandate.
  New `bonded_substrate_conduction_correction` (`lab/thermo_sidecar.py`),
  two complementary endpoints (series worst-case, replace-rear) per Red
  Team's own Phase-2 docket resolving ELECTROMAGNETISM's topology attack.
  **Phase-5 event**: ELECTROMAGNETISM's blind review found the shipped
  `correction_factor_replace_rear` formula — Red Team's own Phase-2
  construction — was a passivity violation (diverged to infinity as
  R_contact→0; decreased as R_contact grew), undetected through Phase 3,
  Phase 4's 23/23 gates, `run.py`'s own reproduction, and four of six
  Phase-5 reviews. Red Team's Phase-5 final audit independently
  re-derived the network, confirmed the finding, named itself as the
  origin, and supplied the exact fix: both endpoints on the SAME R_rear
  baseline, `correction_factor_replace_rear = correction_factor_series
  − 1.0`. Corrected Stress-B: series margin 1.0047× (unchanged); replace-
  rear margin **3.9286×** (not the first-reported 1.1737× — MORE
  comfortable, not less; `r_contact_critical` replace-rear corrected
  0.004291→0.043685 m²K/W). Two new stage-25 gates ((3g) exact identity,
  (3h) strict monotonicity) permanently guard this regression class. A
  second process defect (Red Team's own R2): three Phase-5 review files
  carried a premature "already fixed" Director note, corrected in place.
  **Checkpoint criterion 4 FIRES** (a sign-inverted formula reached a
  permanent regression gate; originated in Red Team's own deliverable;
  survived six independent checkpoints — distinguished from every prior
  non-firing precedent) — ruled a **notification, not a pause**, docket
  landed same-shift, full bench **195/195** green. `REALIZABILITY_MEMO.md`
  Entry 3 (new): R_contact's own tier UNANSWERED, pending a real
  measurement. Also fixed: PHOTONICS' α_true/e-fold correction (exp-063
  Phase-5's "1,900–6,000×" figure was wrong, corrected to `τ_true≈8.26`)
  now has a durable `caveat_lint_config.json` guard + inline pointer at
  its own error site; a latent `_STAGE_IDS` bug (`--only 25` silently
  also firing stages 2/5) found and fixed same-shift. **Verdict: PARTIAL**
  (Red Team's synthesis: machinery sound; the substantive margin question
  is more open now than before this cycle, not less). VISION's Block-
  ARTICLE FDTD leg explicitly deferred to Iteration 45 (below), not
  folded in. Full record: `experiments/067-r-contact-bonded-substrate-
  correction/`, LOGBOOK.md Iteration 44.
- **[ACTIVE — Iteration 54 queue, Red Team's Phase-5 final-audit
  reconciliation of exp-076's six seats (`phase5_redteam_audit.md` §7);
  supersedes the Iteration-53 queue below as the active ranking, that
  block retained as valid backlog, not deleted]** `PAD_TIED`: the
  padding/domain-geometry axis, not `ABSORB` boundary depth, dominates
  T28's amplitude-mismatch signal on the decorrelated `G40`/`C40`/`C80`
  series (`x=amp_ratio(PAIR_PAD)=0.119` HIGH vs `y=amp_ratio
  (PAIR_ABSORB40)=0.072` MED, 600nm) — the confound not relieved in the
  reassuring direction, and the dominant axis now formally proven
  lossless vacuum (Red Team's Phase-5 final audit, independently
  re-derived from `lab/fdtd2d.py`'s primitive source): `PAIR_PAD`'s
  entire signal can only be a phase/interference effect, never absorbed
  power. All six Phase-5 seats' own top picks reconciled by
  information-density-per-cost into 4 tiers, 8 items (full text
  `experiments/076-.../phase5_redteam_audit.md` §7). **Tier 0 — zero
  FDTD, run first (decides where the FDTD budget below should go):**
  (1) **refit exp-075's own already passivity-gated (`G-PASSIVITY`,
  `|r|≤1`) transfer-matrix echo model against `PAD`'s round-trip
  distance instead of `ABSORB` depth** (EM's own #1 pick, seconded by
  THERMO) — the ONLY mechanism class this cycle's own lossless-vacuum
  proof leaves physically permitted for this signal, using code this
  program has already built and validated; ranked #1 overall for its
  information-density per zero marginal cost. (2) **fixed-carrier
  re-score of the already-collected 750nm leg data** (PHOTONICS' own
  #2 pick) — re-score `experiments/076-.../results.json::
  leg750_scored`'s committed arrays under a carrier FIXED at the
  600nm-established ~2.5° periodicity (not `carrier_fit`'s own free-
  period search) to test whether the 750nm leg's own unexplained
  ~1.78°/1.76° periodicity (r²≈0.51/0.58, backfilled into `results.json`
  this cycle) is a free-period-fit artifact or a real wavelength effect,
  before spending FDTD budget on a full leg. (3) **score the already-
  built two-wall cavity model against the already-collected 750nm leg**
  (`experiments/069-.../results.json::block_leg750`) — PLAN.md's own
  Iteration-53 queue item 2, carried over unexecuted through this
  entire cycle; old debt, zero new FDTD, should not fall further
  behind. **Tier 1 — cheap FDTD, next:** (4) **a `PAD`-depth causal
  sweep at fixed `ABSORB=40`** (MATERIALS' own #1 pick) — `PAD∈{20,60,
  80}`, reusing `design_geometry.py`'s own mechanical clearance-scaling,
  scored pairwise exactly as exp-071 did for the `ABSORB` axis; the
  direct causal-trend analog of exp-071's own `R²=0.998` finding, on
  the axis this cycle just showed actually dominates. (5) **broadband
  pulsed reflectance spectroscopy of `C40`/`G40`/`C80`'s `ABSORB`
  boundary** (QUANTUM's own #1 pick) — ~3 FDTD calls, a genuinely
  orthogonal instrument class (single-shot time-domain FFT, not
  another carrier-fitted angular sweep); tests whether 600nm's
  integer-λ aliasing condition is itself resonant and cross-validates
  PHOTONICS' own exp-075 WKB model against a real spectrum for the
  first time. **Tier 2 — the standing precondition, and the charter-
  relevant test:** (6) **the full-width (31-point/6°), non-aliased
  second-wavelength leg for `G40`** (near-unanimous: PHOTONICS #1,
  MATERIALS #2, THERMO #1, QUANTUM #3, VISION #3) — the standing
  requirement before `PAD_TIED` may be cited as wavelength-general at
  all; ranked below Tier 0/1 specifically because items 1–2 should
  decide which wavelength/window configuration is worth the ~31-call
  spend, not because it is optional. (7) **test whether the
  `PAD`-sensitivity survives with a real absorbing article loaded**
  (VISION's own #2 pick) — build the `G40`-decorrelation analogue with
  `graded_black_shell` or an `off_pass`/`off_bracket`-style article
  present, at the same dense window and settled `STEPS`; the actual
  charter-relevant question this cycle's empty-scene-only scope could
  not reach, reconnecting T28's five-cycle-deep instrument-diagnostic
  work back to a real constraint-3 scene. **Tier 3 — record hygiene
  (bundle, zero cost, alongside any of the above):** (8) a
  `G0-e`-class synthetic recovery/telescoping check for `delta_P_obs`/
  `rho_c` before either is ever promoted from disclosed-only to a
  gating role (QUANTUM), plus a 2-call `G40`-at-750nm forward-settling
  leg (EM's own newly-disclosed gap — the 750nm leg was never
  settling-tested). **Longer-horizon, not in the immediate ranking:** a
  structurally independent (true-PML) absorbing-boundary implementation
  (MATERIALS' own #3 pick) — the most decisive possible test of whether
  this whole family of findings is specific to the graded-damping-mask
  construction, but Checkpoint-criterion-3 (major engine build)
  territory; should not preempt the cheaper items above. **Standing
  note for the Director to carry forward:** no new numbered rule this
  cycle, but Red Team's own recommendation (not imposed unilaterally):
  Phase 3's acceptance table should log every disclosed Phase-2
  "secondary finding"'s disposition explicitly, even a one-word
  "deferred, not adopted," so a genuinely non-sharpest finding cannot
  silently vanish between two disposition tables the way VISION's own
  Phase-2 finding did this cycle (real, but non-outcome-determining;
  full ruling `phase5_redteam_audit.md` §2b). Full record: `experiments/
  076-t28-g40-pad-decorrelation/` — Phase-1 proposal +
  `g0e_amplitude_channel_check.py`, five Phase-2 blind critiques,
  Phase-2 Red Team audit, Phase-3 synthesis, `NOTES.md`, `run.py`,
  Phase-4 results, six Phase-5 blind reviews, Phase-5 Red Team final
  audit; LOGBOOK.md Iteration 53 (LIVE THREADS T28 updated — `PAD_TIED`,
  the lossless-vacuum proof, the combined MATERIALS+EM finding; T16
  updated — a third confirmed instrument-floor-uncertainty driver).
- **[superseded by the Iteration-54 queue above — exp-076's own docket,
  retained as a pointer to its own history, not deleted]** the
  Iteration-53 queue that follows this note.
- **[ACTIVE — Iteration 53 queue, Red Team's Phase-5 final-audit
  reconciliation of exp-075's six seats (`phase5_redteam_audit.md` §7);
  supersedes the Iteration-52 queue below as the active ranking, that
  block retained as valid backlog, not deleted]** Two boundary-
  reflectance-echo mechanisms (single-wall and the correctly-derived
  two-wall cavity) are now REFUTEd against T28's real dense-sweep data,
  on a reflection-phase convention independently confirmed correct by
  Red Team's Phase-5 final audit (a new, owned empirical FDTD tie-breaker,
  `experiments/075-.../phase5_redteam_phase_convention_check.py`). All
  six Phase-5 seats converge, after reconciliation, on the same ranking.
  (1) **G40/`PAD` decorrelation** (~31 FDTD calls, per MATERIALS' verified
  geometry-reuse claim against `experiments/065-.../
  design_geometry_output.txt`) — near-unanimous #1 (ranked #1 or #2 by
  all six seats). The only queued item that actually *relieves*, rather
  than discloses or prices, the `ABSORB`-or-`PAD` confound running under
  every T28 causal claim since Iteration 48 — now the single most
  information-dense open question on T28's board, with the boundary-
  reflectance-echo class doubly REFUTEd on the existing congruent series
  and the model's own predicted echo strongly `ABSORB`-depth-*dependent*
  while the real residual is depth-*independent* (exp-075 Phase 3's own
  cross-check, §5b of `boundary_reflectance.py`). Readout on the
  phase-invariant amplitude channel `√(A_i²+A_q²)/a` (exp-072 baseline
  0.161/0.041/0.020/0.166) — no fitted carrier phase, inherits neither the
  window-resolution problem nor any sign-flip calibration problem, and is
  explicitly NOT barred by exp-074's own seventh-cycle rule (a genuinely
  different instrument class). Pre-register up front: the 2x2 factorial
  is not completable (`config(80,0)` gives `clear_span_y=-40`), so main
  effects are identifiable only under additivity, the interaction not at
  all. (2) **Score the already-built two-wall model against the already-
  collected 750nm leg** (`experiments/069/results.json::block_leg750`, 16
  points, Iteration 46, zero new FDTD — VISION's own #1 Phase-5
  candidate). Cheap, decisive either way, and stress-tests exp-075's own
  REFUTE (as a free byproduct, a genuinely independent second data point
  on the phase-convention resolution at a different wavelength) before
  either headline REFUTE is cited elsewhere as a wavelength-general
  result. (3) **Harden the phase-convention resolution to this program's
  own R6/G0-e standard** (folds in PHOTONICS'/EM's own #1 Phase-5
  candidate, now a closing task, not an opening one) — extend
  `phase5_redteam_phase_convention_check.py` to the real `ABSORB`=40/60/
  70/80 depths directly, with a higher-power extraction than a single-bin
  FFT read; diagnose and fix the `K>=8` calibration degradation that
  audit found and disclosed, or explicitly bound why it does not matter
  at the real, much-smaller `|r|` values. (4) **Record-hygiene bundle**
  (near-unanimous, touched by all six Phase-5 seats in some form): (a)
  THERMODYNAMICS' sidecar rounding fix (`>99.996%`→`>99.995%`); (b) an
  explicit two-wall-model sidecar re-confirmation sentence; (c) switch
  `circular_shift_null` to exact 30-shift enumeration and add a
  synthetic-noise (AR(1) and/or phase-randomization) sizing leg before
  reuse on different data (QUANTUM's finding: the check is anti-
  conservative, 1.3x-16x nominal depending on alpha); (d) add the
  matched-`eps=mu`/`graded_black_shell`-code-path-disjointness note
  explicitly to the idealization list; (e) `caveat_lint_config.json`
  entries protecting exp-075's own headline scope caveats (the matched-
  `eps=mu` realizability scope, the single-vs-two-wall-echo scope limit);
  (f) fold Red Team's Phase-5 §2 finding and standing rule R8 into the
  permanent record's own phase-convention caveat language. **Not ranked,
  flagged as speculative backlog** (needs real design work before it
  earns FDTD/analytic time): MATERIALS' residual-of-residual structural
  candidate; QUANTUM's dispersive-`eps(omega)` extension (needs item 2's
  750nm leg first); THERMODYNAMICS' Idealization-6 closed-form-to-exact
  computation (cannot move T28's own mechanism question either way, the
  bound is already 150x below the observed signal). `R_contact`'s
  literature search (unchanged ranking, 13+ consecutive cycles blocked)
  stays orthogonal, capacity permitting. **Standing rules for the
  Director to carry forward (already adopted in LOGBOOK.md, not a new
  FDTD item):** R8 (new this cycle — an unverified robustness/
  independence argument about a flagged verification gap is not
  sufficient to file it informational-only when an affordable named check
  exists; the argument must be tested, not reasoned about). Full record:
  `experiments/075-t28-absorb-boundary-wkb-reflectance/` — Phase-1
  proposal + `boundary_reflectance.py`, five Phase-2 blind critiques,
  Phase-2 Red Team audit, Phase-3 synthesis, `two_wall_cavity.py`,
  Phase-4 results, `NOTES.md`, six Phase-5 blind reviews, Phase-5 Red
  Team final audit + its own owned verification script; LOGBOOK.md
  Iteration 52 (R8 adopted, CHECKPOINT criterion 4 fired, LIVE THREADS
  T28 updated — both boundary-reflectance-echo mechanisms RULED OUT).
- **[superseded by the Iteration-53 queue above — exp-075's own docket,
  retained as a pointer to its own history, not deleted]** the
  Iteration-52 queue that follows this note.
- **[ACTIVE — Iteration 52 queue, Red Team's Phase-5 final-audit
  reconciliation of exp-074's six seats (`phase5_redteam_audit.md` §8);
  supersedes the Iteration-51 queue below as the active ranking, that
  block retained as valid backlog, not deleted]** T28's differential/
  two-tone-fit sub-thread is formally retired on this instrument class
  (Iteration 51's own pre-committed seventh-cycle rule, triggered as
  written) — no further work re-fitting `R_q` (single-carrier or
  two-tone) on the 124-point/31-angle substrate, at any window, is
  authorized without a qualitatively different calibration strategy. All
  six Phase-5 seats converge on the same reconciled ranking. (1)
  **PHOTONICS' WKB/adiabatic boundary-reflectance analytic model for the
  graded-loss `ABSORB` band** — zero FDTD, zero data, near-unanimous #1
  (4 of 6 seats explicitly rank it #1; the other two rank it #2). Queued
  and dropped without execution twice before (Iterations 46, 47); this is
  the explicit "qualitatively different strategy" exp-074's own
  seventh-cycle rule names as licensed to re-open the sub-thread if it
  succeeds, and the first candidate in this six-cycle sub-thread to
  engage a seat's own charter physics directly rather than re-verify
  statistics. Independently strengthened by exp-074's own Phase-5 finding
  (four seats): the leftover-after-best-single-sinusoid residual shape is
  `ABSORB`-depth-*independent* (essentially the same curve at all four
  depths, cross-config r=0.992–1.000) — a data point arguing, for free,
  toward a shared-geometry/boundary-admittance origin over a graded-
  absorber-depth-tied one, directly usable by this analytic model. An
  analytic (not fitted) model of the reflection phase a graded-absorption
  boundary of varying depth produces as a function of angle, computed
  from the boundary's own admittance profile, zero data — either explains
  the ~2.5° family as an ordinary boundary-reflectance phase effect
  (closing T28's own mechanism question outright) or rules it out
  (narrowing the remaining candidate space). (2) **G40/`PAD`
  decorrelation** (~31 FDTD calls, per MATERIALS' verified geometry-reuse
  claim against `experiments/065-.../design_geometry_output.txt`; five of
  six seats rank it in their own top 3). The only queued item that
  actually *relieves*, rather than discloses or prices, the
  `ABSORB`-or-`PAD` confound binding every T28 deliverable since
  Iteration 48 — cheapest remaining FDTD relief on the board, orthogonal
  to item 1 and to exp-074's own null-calibration findings. Readout on the
  phase-invariant amplitude channel `√(A_i²+A_q²)/a` (exp-072 baseline
  0.161/0.041/0.020/0.166), which conditions on no fitted carrier phase at
  all — inherits neither the window-resolution problem nor any sign-flip
  calibration problem, and is **explicitly NOT barred by the seventh-cycle
  rule** (a genuinely different instrument class, not a re-fit of `R_q`) —
  state this explicitly in the Iteration-52 entry so the rule is not
  misread as blocking it. Pre-register up front: the 2×2 factorial is not
  completable (`config(80,0)` gives `clear_span_y=−40`), so main effects
  are identifiable only under additivity, the interaction not at all. (3)
  **Bundle exp-074's own record-hygiene corrections with a disclosure
  patch to the reusable calibration machinery, before either item 1 or 2
  starts** (near-zero cost, touched by all six Phase-5 seats in some
  form): (a) exp-074's own `phase4_results.md`/`NOTES.md` arithmetic
  slips are already corrected in place (Phase 5, this cycle) — verify no
  further copy survives; (b) add the cross-config residual-correlation
  table and lag-1 autocorrelation figures (exp-074 Phase 5) as committed,
  reproducible script output in `fit_and_calibrate.py` rather than
  prose-only, and add a documented coupled-shift (or jointly-resampled)
  alternative leg to `calibrate_null` before this explicitly-kept-for-
  reuse machinery is pointed at a future dataset where the two
  constructions might not agree as comfortably as they did here; (c)
  finally correct the three-document-old "house precedent, Iteration 5,
  exp-027" mislabel (THERMODYNAMICS' Phase-2 finding, exp-074, correctly
  ruled out-of-scope for that cycle itself, still uncorrected). `R_contact`'s
  literature search (unchanged ranking, 12+ consecutive cycles blocked)
  stays orthogonal, capacity permitting. **Standing rules for the
  Director to carry forward (already adopted in LOGBOOK.md, not a new
  FDTD item):** R7 (new this cycle — a conditioning/VIF-based pricing of
  an un-fit design is necessary, not sufficient, for a closure or
  detection claim); R4's second addendum (a Phase-5 reviewer's own
  reproduction section must recompute, not merely restate, any cited
  cell-count/combinatorial total). Full record: `experiments/074-t28-
  window-pricing-cramer-rao-bound/` — Phase-1 proposal, five Phase-2
  blind critiques, Phase-2 Red Team audit, Phase-3 synthesis, `NOTES.md`,
  both scripts + results (erratum-corrected), six Phase-5 blind reviews,
  Phase-5 Red Team final audit; LOGBOOK.md Iteration 51 (R7 adopted, R4
  second addendum, LIVE THREADS T28 updated — sub-thread formally
  retired on this instrument class).
- **[superseded by the Iteration-52 queue above — exp-074's own docket,
  retained as a pointer to its own history, not deleted]** the
  Iteration-51 queue that follows this note.
- **[ACTIVE — Iteration 51 queue, Red Team's Phase-5 final-audit
  reconciliation of exp-073's six seats (`phase5_redteam_audit.md` §6.2);
  supersedes the Iteration-50 queue below as the active ranking, that
  block retained as valid backlog, not deleted]** Near-unanimous, all six
  seats converge at or near #1 on pricing the window before any further
  estimator or FDTD spend — the strongest cross-seat agreement in this
  cycle's own record. (1) **Price the window — zero FDTD, decisive either
  way.** EM's Cramér–Rao/conditioning pricing (`cond=529` at a 9-column
  two-tone design, ≈6× SE inflation on `R_q`) and QUANTUM's already-
  established `L(T)` leakage budget (non-identifiable against ~1.8°–5.0°
  periodic contaminants) both answer, at zero cost, whether `θ∈[36°,42°]`
  can ever support a carrier-conditioned discriminator at achievable SNR,
  for *any* correctly calibrated null — a question logically prior to "is
  this specific null calibrated," which exp-073 answered "no" for one
  construction only. Must also report how `cond(X5)` and the leverage-
  concentration pattern (`mean diag(M5)=(n−p)/n`, exact and window-width-
  independent by algebra; *where* leverage concentrates is not) would
  change at a widened window — not just "does a wider window resolve the
  period" but "would a wider window plausibly let a future `G0-e(ii)`-
  style test pass at all." If the answer is no, that is a real, citable
  closing bound on the differential-fit route in this window (PANEL.md's
  own "mapped constraint boundary" product) — directly triggers the
  pre-committed decision rule below: formally retire the sub-thread in
  this window. (2) **G40/`PAD` decorrelation** (~31 calls if MATERIALS'
  geometry-reuse claim verifies against `experiments/065-.../
  design_geometry_output.txt`), unanimous #2/#3 — the cheapest FDTD
  relief on the board, orthogonal to item 1 and to the null-calibration
  question, and the only queued item that actually *relieves* (not
  merely discloses) the `ABSORB`-or-`PAD` confound binding every T28
  deliverable since Iteration 48. Readout on the phase-invariant
  amplitude channel `√(A_i²+A_q²)/a` (exp-072 baseline 0.161/0.041/0.020/
  0.166), which conditions on no fitted carrier phase at all — inherits
  neither the window-resolution problem nor exp-073's own leverage-driven
  calibration problem. Pre-register up front: the 2×2 is not completable
  (`config(80,0)` gives `clear_span_y=−40`), so main effects are
  identifiable only under additivity, the interaction not at all. (3) **A
  properly-calibrated null construction, including a genuinely order-
  preserving residual-structure leg — explicitly gated on item 1's
  result, not built in parallel.** Building a better-calibrated null for
  a window that cannot resolve the target signal at any achievable SNR
  solves the wrong stage of the problem. If item 1 licenses further
  spend, this becomes the load-bearing next build, itself gated by its
  own fresh `G0-e(ii)`-style calibration test (per LOGBOOK R6's own
  generalized standing rule, Iteration 50) before it may gate any real
  data. (4) **PHOTONICS' WKB/adiabatic boundary-reflectance model for the
  graded-loss `ABSORB` band** — zero FDTD, genuinely new to this ranking,
  runs in parallel with items 1–3. Queued twice before (Iteration 46/47)
  and confirmed dropped without execution both times. An analytic (not
  fitted) model of the reflection phase a graded-absorption boundary of
  varying depth produces as a function of angle, computed from the
  boundary's own admittance profile, zero data — the first candidate in
  this five-cycle sub-thread to engage a seat's own charter physics
  directly rather than re-verify statistics; either explains the ~2.5°
  family as an ordinary boundary-reflectance phase effect (closing T28's
  own mechanism question outright) or rules it out (narrowing the
  remaining candidate space). (5) **A pre-committed decision rule on
  T28's own differential-fit sub-thread must be stated explicitly in
  Iteration 51's own entry, not left implicit** (LOGBOOK's own Iteration-
  50 Checkpoint-5 ruling, binding): item 1's own result is the natural
  occasion — if it closes the window, that closure IS the rule (formal
  retirement); if it does not, Iteration 51 must state in writing what a
  sixth non-advancing cycle would mean, matching the Block-MINI precedent
  (a formal, pre-committed non-decisive-outcome retirement trigger)
  rather than defaulting to a further deferral. **Standing rules for the
  Director to carry forward (already adopted in LOGBOOK.md, not a new
  FDTD item):** R6 generalized to require null-calibration testing as
  standing machinery (not merely ground-truth recovery); R4 extended to
  cover a Phase-5 reviewer's own re-checking of a prior claim, and sign
  corrections specifically. `R_contact`'s literature search (unchanged
  ranking, 11+ consecutive cycles blocked) stays orthogonal, capacity
  permitting. Full record: `experiments/073-t28-differential-beat-fit-
  reissue/` — Phase-1 proposal, five Phase-2 blind critiques, Phase-2 Red
  Team audit, Phase-3 synthesis, `NOTES.md`, `run.py` (post-fix),
  `results.json`, `phase4_results.md` (with Phase-5 erratum section), six
  Phase-5 blind reviews, Phase-5 Red Team final audit; LOGBOOK.md
  Iteration 50 (CHECKPOINT criterion 4, R4/R6 both extended, LIVE THREADS
  T28 updated).
- **[superseded by the Iteration-51 queue above — exp-073's own docket,
  retained as a pointer to its own history, not deleted]** the
  Iteration-50 queue that follows this note.
- **[ACTIVE — Iteration 50 queue, Red Team's Phase-5 final-audit
  reconciliation of exp-072's six seats (`phase5_redteam_audit.md` §7.2);
  supersedes the Iteration-49 queue below as the active ranking, that
  block retained as valid backlog, not deleted]** All six seats converge,
  unanimously, that item (1) must run first; they split three ways below
  that (widen the window / decorrelate `PAD` / model the contaminant),
  reconciled here rather than vote-averaged. (1) **A corrected zero-FDTD
  re-issue of exp-072's own differential/beat-fit instrument, behind the
  new `G0-e` ground-truth recovery gate** — nothing downstream of exp-072's
  own step 2 is fully clean until this lands as a freshly pre-registered
  cycle (the contamination ruling's own condition 3 explicitly
  contemplates this); folds in EM's `A_q = 2a_cbar·tan χ` table correction,
  QUANTUM's sign-flip/residual-permutation null replacing the phase-
  randomised H₀-residual one, and VISION's reinstated sign-invariance
  admissibility condition over the gate-admitted carrier set (all deferred
  from exp-072's own same-shift docket as new-gate additions, not
  same-shift-safe). (2) **Price the differential/beat window before
  spending in it — a data-free feasibility calculation, zero FDTD**:
  EM's Cramér–Rao/conditioning pricing (`cond=529`, 6× SE inflation, on a
  two-tone joint fit in the current window) and QUANTUM's leakage-function
  budget (`|L(T)|` computable for any candidate θ span with no data) decide
  whether 36°–42° can ever support a carrier-conditioned discriminator at
  all — rank above both FDTD builds below since it determines which is
  worth the spend; if the window cannot reach 2σ on `R_q` at achievable
  SNR, publish that as the closing bound on the differential route in this
  window, a real result in its own right. (3) **G40 / `PAD` decorrelation**
  (~31 calls if MATERIALS' geometry-reuse claim verifies against
  `experiments/065-.../design_geometry_output.txt` — PLAN's prior 62–93
  estimate assumed a fresh build; G40 vs. C80 = pure `ABSORB` at fixed
  `PAD`, G40 vs. C40 = pure `PAD` at fixed `ABSORB`, both already-built
  configs) — the cheapest confound relief on the board, closing the
  `ABSORB`-or-`PAD`-or-frequency-or-fringe-weight caveat that now binds
  every T28 deliverable under every verdict; readout on the
  phase-invariant amplitude channel `√(A_i²+A_q²)/a` (exp-072 baseline
  0.161/0.041/0.020/0.166), which conditions on no carrier at all. **Must
  pre-register up front**: the 2×2 is not completable (`config(80,0)`
  gives `clear_span_y=−40`), so main effects are identifiable only under
  additivity; the interaction is not identifiable at all. (4) **Window
  extension to `θ_max≈46°`** (EM: 40 calls, C40/C80 two-config; VISION:
  64–156 calls for 1.0–1.5 Rayleigh widths across all four configs) — the
  only change attacking T28's resolution problem at its cause; **VISION's
  window-discipline constraint now generalizes** to any carrier-
  conditioned T28 estimator (differential and two-tone alike), not only
  absolute-period ones. Binding precondition: the curvature column must be
  promoted from disclosed to fitted, or an envelope-agreement check
  pre-registered across sub-windows, before the extension runs — `cos θ`
  varies 8.1–14.1% across the current-vs-extended span, and `R_i` is
  already the larger coefficient at 3 of 4 exp-072 pairs. (5) **Explicitly
  subordinate**: MATERIALS' mask-functional-form ablation (item 3 below,
  carries no `PAD` confound by construction — run inside whichever window
  wins from item 4) and PHOTONICS' two-tone joint fit (item 4 below,
  re-deferred with a stated reason this cycle — EM's pricing and R5/
  Iteration-47 look-elsewhere discipline both argue against running it
  until item 2 says the window supports it; its `ABSORB≈120` FDTD half is
  separately weak, MATERIALS' own covariate finding — `ABSORB`/λ is
  integer at 40/60/80 and would be integer again at 120 — means it
  preserves rather than breaks an uncontrolled covariate). **PHOTONICS'
  measured second-tone period (1.824–1.837°, exp-072 Phase 5) is
  UNQUOTABLE** without a null-permutation control first (R5/Iteration-47
  discipline — a free-period search on the same governed continuum).
  `R_contact`'s literature search (unchanged ranking, 10 consecutive
  cycles now, tooling-blocked) stays orthogonal, capacity permitting. Full
  record: `experiments/072-t28-differential-beat-fit/` — Phase-1 proposal,
  five Phase-2 blind critiques, Phase-2 Red Team audit, Phase-3 synthesis
  (+erratum), NOTES.md, `run.py`, `results.json`, `phase4_results.md`
  (republished), six Phase-5 blind reviews, Phase-5 Red Team final audit;
  LOGBOOK.md Iteration 49 (CHECKPOINT criterion 4, new standing rule R6
  `G0-e`, LIVE THREADS T28 updated).
- **[superseded by the Iteration-50 queue above — exp-072's own docket,
  retained as a pointer to its own history, not deleted]** the
  Iteration-49 queue that follows this note.
- **[superseded by the Iteration-50 queue above — exp-071's own docket,
  retained as valid backlog, not deleted]** (1) **Merge ELECTROMAGNETISM's differential/beat-fit and
  QUANTUM OPTICS' matching Phase-5 proposal into one item** — zero new
  FDTD cost, fit `delta_AB(θ)=C_B(θ)−C_A(θ)` directly between adjacent
  `ABSORB` pairs (C40–C60, C60–C70, C70–C80, plus the already-analyzed
  C40–C80) on the 124 already-collected exp-071 points, instead of
  independently fitting absolute periods and subtracting — converts an
  absolute-frequency Rayleigh-resolution problem (unsolvable at any
  achievable window for the C60–C70 pair specifically, per QUANTUM's own
  derivation) into a phase-accumulation/beat-detection problem, reusing
  the exact methodology that discovered T28 in the first place
  (`C80−C40`, `ptp/mean=16.2`). Highest information-per-cost move
  available; run first. (2) **Merge THERMODYNAMICS' matched-`PAD`
  amplitude probe and QUANTUM OPTICS' PAD-decorrelation proposal into one
  new-config build** (~62–93 calls) — the only way to directly close the
  `PAD=ABSORB−40` confound exp-071's Phase 5 surfaced (three independent
  blind seats — THERMODYNAMICS/ELECTROMAGNETISM/QUANTUM OPTICS): a config
  holding `PAD` fixed while `ABSORB` varies, scoring both THERMO's
  resolution-floor-free amplitude discriminator (primary; `C_empty`
  peak-to-peak amplitude rose +21.8%, `R²=0.886`, with `ABSORB` depth in
  the existing series, confounded with `PAD`) and the free-period fit
  (secondary, floor-caveated) on the same run. (3) **MATERIALS'
  mask-functional-form ablation** — hold `ABSORB` fixed (e.g. `C80`) and
  vary the damping ramp's exponent/decay constant at fixed cell depth;
  cheap, answers whether the periodicity is tied to a length scale at all
  or to the numerical decay profile, orthogonal to items 1–2. (4)
  **PHOTONICS' two-tone joint fit** (zero-cost, desk-only re-analysis) +
  **ELECTROMAGNETISM's new `ABSORB≈120` config** (31 calls) run together —
  direct tests of the saturating-mechanism candidate exp-071's Phase 5
  independently confirmed real (a 2-parameter saturating-exponential model
  fits exp-071's own four points at `R²=0.998` vs. the linear model's
  `R²=0.866`, Red-Team-reproduced), informed by item 1's result. (5)
  **VISION SCIENCE's window-discipline guidance** — do not reuse the
  36°–42° window a third time for an absolute-period discriminator; a
  binding constraint on items 2–4's new FDTD spend, not a standalone
  item, already substantially satisfied by item 1's shift to
  differential/beat fitting. **`R_contact`'s `measured_direct` literature
  search** (item 6, unchanged ranking, 9 consecutive cycles blocked on
  WebSearch/WebFetch tooling) — the Director's own tooling-availability
  disclosure (this shift's environment has both tools present) should be
  acted on independently of T28's own queue ordering above, capacity
  permitting. Full record:
  `experiments/071-t28-absorb-depth-causal-test/` — Phase-1 proposal, five
  Phase-2 blind critiques, Phase-2 Red Team audit, Phase-3 synthesis,
  NOTES.md, `design_geometry.py`/`run.py`, `results.json`,
  `phase4_results.md`, six Phase-5 blind reviews, Phase-5 Red Team final
  audit; `lab/caveat_lint_config.json` (new
  `exp071-t28-absorb-pad-confound-and-resolution-floor` entry); LOGBOOK.md
  Iteration 48 (LIVE THREADS T28 updated).
- **[superseded by the Iteration-49 queue above — exp-071's own docket,
  retained as a pointer to its own history, not deleted]** the
  Iteration-48 queue that follows this note.
- **[superseded by the Iteration-48 queue above — exp-070's own docket,
  retained as valid backlog, not deleted]** (1) **ELECTROMAGNETISM's C60/C70
  `ABSORB`-depth falsification test** — the already-built congruent
  configs (zero new `lab/` diff), varying `ABSORB` directly across all
  four points (40/60/70/80) while holding everything else fixed, the
  causal manipulation T28's own desk-check batch (exp-070) could not
  provide. Per Red Team's own Phase-5 final-audit strengthening: (a)
  include EM's own direct cross-config consistency metric
  (`|P*(Ca)−P*(Cb)|/mean`) at every `ABSORB` pair, not only against a
  derived reference — the metric exp-070's own Phase-5 review showed was
  missing and is what would actually distinguish "genuine shared
  component" from "compromise fit" at four points instead of two; (b)
  fold in the already-queued, near-zero-cost peak-cell R3 resolution
  recheck (θ≈37.2°/41.4°, 2 calls, exp-069's own residual resolution-scope
  gap) at no extra cost. Score on the RECOVERED PERIOD at each `ABSORB`
  depth (exp-070's own Attack-1 lesson: bare R² alone is not a
  discriminator), and disclose the cross-config spread explicitly rather
  than only a binary CONFIRM/REFUTE. (2) **`R_contact`'s `measured_direct`
  literature search** — unchanged ranking from five prior cycles'
  queues, converging across 4 of 6 exp-070 blind reviews
  (PHOTONICS/MATERIALS/THERMODYNAMICS/VISION), zero resource competition
  with item 1 (desk/literature vs. FDTD), still the only item across
  eight cycles now (Iterations 44–48) that can move a real, sourced
  materials number for TD-5's still-UNANSWERED tier
  (`REALIZABILITY_MEMO.md` Entry 3), blocked purely on WebSearch/WebFetch
  tooling availability. Full record:
  `experiments/070-t28-mechanism-desk-check-batch/` — Phase-1 proposal,
  five Phase-2 blind critiques, Phase-2 Red Team audit, Phase-3 synthesis,
  NOTES.md, `design_geometry.py`/`desk_check_mechanism.py`,
  `results.json`, `phase4_results.md`, six Phase-5 blind reviews, Phase-5
  Red Team final audit; `lab/caveat_lint_config.json` (new
  `exp070-t28-named-constant-null-control` entry); LOGBOOK.md Iteration
  47 (RULED OUT R5 addendum, LIVE THREADS T28 updated).
- **[superseded by the Iteration-48 queue above — exp-070's own docket,
  retained as a pointer to its own history, not deleted]** the
  Iteration-47 queue that follows this note.
- **[ACTIVE — Iteration 47 queue, Red Team's Phase-5 final-audit
  reconciliation of exp-069's six seats; supersedes the Iteration-46
  queue below as the active ranking, that block retained as valid
  backlog, not deleted]** (1) **A single zero-FDTD-cost desk-check batch
  on T28's own mechanism** — the ~2.84° periodicity in the `C80−C40`
  padding delta (opened Iteration 46, exp-069) that does NOT match T21's
  own established `P(θ)≈1.96°` fringe. A genuine, unprompted cross-seat
  convergence (all six blind Phase-5 reviews independently proposed some
  form of "characterize T28's mechanism, desk-first"): per-config
  decomposition (does the signature already live in `C40` or `C80` alone,
  or only in the difference?), a beat-frequency reconstruction (solve
  `1/P_beat=|1/P_a−1/P_b|` for a second period against every named
  geometric length scale), a taper-as-second-aperture check (`TAPER=40`
  cells, ~5.3% of `A`, as its own diffracting sub-aperture), and a
  systematic `A_eff≈518.8`-cell trace against `design_geometry.py`'s own
  named constants — before any new FDTD spend, mirroring this program's
  own R3 meta-rule and the exact desk-first discipline Iteration 46 itself
  modeled on Block MINI. THERMODYNAMICS' own desk-only WKB/adiabatic
  boundary-reflectance model for the graded-loss `ABSORB` band folds into
  this same batch if capacity allows, not competing with it for resources.
  **Standing forward tripwire (Red Team's own Iteration-46 Phase-5 final
  audit): if T28 has not received at least this cheap, desk-only first
  move by the close of Iteration 48, that scheduling gap itself becomes
  Checkpoint-4-adjacent** — matching this program's own established
  lock-trigger phrasing (`Q_ext(x)`/exp-059, `R_contact`/exp-067, Block
  MINI/T23 itself). (2) **EM's C60/C70 falsification test, or PHOTONICS'
  properly-powered T28 re-run at 750nm/450nm, whichever item (1)'s own
  result sharpens toward** — EM's test reuses already-built congruent
  configs (zero new `lab/` diff) to check whether the ~2.84° period tracks
  `ABSORB` depth (the one thing that differs between `C40`/`C80`); if
  item (1) is inconclusive, PHOTONICS' fallback (a properly-powered sweep
  at 750nm/450nm using T28's OWN ~2.84°-family period, not T21's, ≥3
  periods, 0.2° step, settled STEPS=2800) should be *narrowed* by item
  (1)'s own findings, not run as a blind full redesign. Folds in a cheap
  peak-cell R3 recheck (θ≈37.2°/41.4°, 2 calls, near-zero marginal cost —
  closes exp-069's own residual resolution-scope gap, item 3 of its
  mandatory-fix docket) at near-zero marginal cost. (3) **R_contact's
  `measured_direct` literature search** — unchanged ranking from
  Iteration 46's own queue, still the only item across five cycles now
  that can move a real materials number (`REALIZABILITY_MEMO.md` Entry 3,
  TD-5's 7.8× margin, UNANSWERED), still blocked purely on WebSearch/
  WebFetch tooling, not gated to any rotation slot, orthogonal to items
  (1)–(2) (desk/literature work competes for zero FDTD budget or rotation
  slot). (4) **[rider-level, apply whenever convenient]** an
  `fdtd_budget()` small-batch documentation caveat (exp-069's own
  mandatory-fix docket item 5: the wall-clock formula's contention
  assumption breaks down for `n_calls≲n_workers`, a recurring pattern
  across exp-065/066/069 — 1.28×/2.70×/2.20× overestimate — not one-off
  variance). Full record: `experiments/069-t21-block-mini-period-match-
  power-up/` — Phase-1 proposal, five Phase-2 blind critiques, Phase-2
  Red Team audit, Phase-3 synthesis, NOTES.md, `design_geometry.py`/
  `run.py`, `phase4_results.md` (+ Phase-5 corrections), `results.json`,
  six Phase-5 blind reviews, Phase-5 Red Team final audit;
  `lab/caveat_lint_config.json` (updated `exp065-steps1400-unsettled-
  plane-channel` entry); LOGBOOK.md Iteration 46.
- **[superseded by the Iteration-47 queue above — exp-069's own docket,
  retained as a pointer to its own history, not deleted]** the
  Iteration-46 queue that follows this note (Block MINI, now formally
  retired — see T28 above; R_contact, carried forward unchanged as item 3
  above).
- **[ACTIVE — Iteration 46 queue, Red Team's Phase-5 final-audit
  reconciliation of exp-068's six seats; supersedes the Iteration-45
  queue below as the active ranking, that block retained as valid
  backlog, not deleted]** (1) **Block MINI's period-match test — LOCKED,
  unconditional.** T21's own mechanism-vs-artifact question, deferred-
  behind-relabeling for a third consecutive cycle at minimum (Iterations
  43, 44, 45; a fourth under this program's own more literal
  cycle-inclusive counting convention), crossing this program's own
  pre-committed T23 threshold — Checkpoint criterion 4 fired at
  Iteration 45 close on this exact finding (LOGBOOK.md Iteration 45).
  Either build the properly-powered FDTD version (≥2–3 T21 periods at
  ~0.2° spacing, settled STEPS≥2800, desk-first per QUANTUM's own
  zero-cost check on the existing settling-delta dataset before any FDTD
  spend) or formally retire the test with a stated reason — no further
  relabeling, no further citation-tripwire-only treatment. Matches this
  program's lowest-ever lock-trigger precedent (`Q_ext(x)`/exp-059,
  `R_contact`/exp-067, both 3-deferral locks). Iteration 46 is
  THERMODYNAMICS' turn by rotation regardless; this item is locked
  irrespective of lead seat. (2) **A real, dedicated literature search
  for a `measured_direct` root/substrate contact-resistance figure**
  (R_contact, carried forward unchanged from Iteration 45's queue) —
  still blocked only by WebSearch/WebFetch tooling availability, not
  gated to any rotation slot; pick up whenever tooling clears, in
  parallel with item 1 if capacity allows (orthogonal, zero resource
  competition). (3) **P-068-4's minor config-dependent 750nm/600nm
  convergence-ordering split** (exp-068) — low-urgency, three orders of
  magnitude below any decision threshold; fold into a future cycle that
  revisits 750nm settling behavior, not worth a dedicated cycle on its
  own. Full record: `experiments/068-t27-block-article-settled-steps/` —
  Phase-1 proposal, five Phase-2 blind critiques, Phase-2 Red Team
  audit, Phase-3 synthesis, NOTES.md (+ Erratum), `phase4_results.md`
  (+ corrections), six Phase-5 blind reviews, Phase-5 Red Team final
  audit; `lab/caveat_lint_config.json` (new
  `exp065-block-article-caveat-propagation` entry); LOGBOOK.md Iteration
  45 (+ CHECKPOINT block).
- **[superseded by the Iteration-46 queue above — exp-068's own docket,
  retained as a pointer to its own history, not deleted]** the
  Iteration-45 queue that follows this note.
- **[ACTIVE — Iteration 45 queue, Red Team's Phase-5 final-audit
  reconciliation of exp-067's six seats; supersedes the Iteration-44
  LOCKED block below as the active ranking, that block retained as valid
  backlog, not deleted]** (1) **A real, dedicated literature search for a
  `measured_direct` root/substrate contact-resistance figure** — the
  still-queued item, blocked only by WebSearch/WebFetch tooling
  availability. Scoped to resolve both R_contact's own units-legitimacy
  flag (does the sourced figure describe a per-junction or a macroscopic-
  areal quantity?) and enough about real bonded-CNT-forest interfaces
  (CVD-grown chemical bonding vs. transferred/pressed van der Waals
  contact) to make an informed call on which topology (series vs.
  replace-rear) a real bond resembles — a number alone would relocate the
  ambiguity, not close it (`REALIZABILITY_MEMO.md` Entry 3). Not gated to
  MATERIALS' own rotation slot; pick up whenever tooling clears. (2)
  **VISION's Block-ARTICLE settled-STEPS FDTD leg (T27)**, now FOUR
  consecutive cycles (Iterations 42→43→44) without being a cycle's
  primary FDTD work — exp-065 (144 calls) and exp-066 (39 calls) each
  fully dedicated themselves to T27 and still left it open; exp-067
  explicitly deferred it rather than attempt a third partial pass.
  Pre-committed, capped scope per VISION's own Phase-5 flip condition:
  article-present legs at minimum the ±35°/600–750nm pair (the cells the
  retracted P-VIS42-6/7 verdicts rest on), STEPS≥2800, ceiling ~30–45
  FDTD calls, stated in NOTES.md before the run — not FALLBACK_ANGLES or
  Block MINI (see item 3). Iteration 45 is ELECTROMAGNETISM's turn by
  rotation; EM should either take this as a scoped secondary item with a
  real call ceiling stated up front, or explicitly disclose a fifth-
  consecutive-deferral line — not let it drift under "if scope allows"
  language a third time. (3) **Block MINI's period-match test**, desk-
  first: run QUANTUM OPTICS' proposed zero-cost check (does the existing
  36-cell settling-delta dataset already show `A·cosθ`-periodic structure
  matching T21's period?) before any FDTD spend, then build the properly-
  powered FDTD version (≥2–3 T21 periods at ~0.2° spacing, settled STEPS)
  or formally retire it — two consecutive cycles of deferral-behind-
  relabeling is this program's own T23-precedent line for flagging a
  third occurrence as Checkpoint-4-adjacent. Full record:
  `experiments/067-r-contact-bonded-substrate-correction/` — Phase-1
  proposal, five Phase-2 blind critiques, Phase-2 Red Team audit, Phase-3
  synthesis, NOTES.md (+ Erratum), `phase4_results.md` (+ Erratum), six
  Phase-5 blind reviews (+ corrections), Phase-5 Red Team final audit;
  `lab/caveat_lint_config.json` (new `exp067-r-contact-analogy-proxy-
  disclosure` and `exp063-alpha-true-efold-staleness` entries);
  `experiments/034-.../REALIZABILITY_MEMO.md` Entry 3.
- **[superseded by the Iteration-45 queue above — exp-067's own docket,
  retained as a pointer to its own history, not deleted]** the
  Iteration-44 LOCKED block that follows this note (R_contact,
  now executed; T27 settling-gap item, now split into Iteration-45's
  queue item 2 above; Block MINI, carried forward as item 3 above).
- **[LOCKED for Iteration 44 — Red Team's Phase-5 final-audit ruling,
  exp-066, granting THERMODYNAMICS' escalation request; supersedes the
  list below as the active ranking, retained as valid backlog, not
  deleted]** (1) **R_contact — LOCKED, unconditional.** Source, or at
  minimum formally model as a new series thermal-resistance term, the
  CNT-forest root-to-substrate thermal contact resistance. Three
  consecutive deferrals (Iterations 41→42→43) now matches this program's
  own lowest-ever lock-trigger precedent (`Q_ext(x)`, exp-059, locked
  after exactly 3 deferrals) and the `graded_black_shell_flagship`
  precedent (exp-057, THERMODYNAMICS' own unconditional rotation-breaking
  lock, which produced a real 6.04×→699.27× margin correction). It is the
  *only* queued item that can move a number (TD-5's 7.8× margin, this
  program's thinnest safety factor of any kind) rather than relabel or
  disclose one; desk/literature work on `lab/thermo_sidecar.py`'s
  analytic Biot formula, structurally orthogonal to any FDTD budget.
  Build as a genuinely new `R_contact` series term, gated by an
  `R_contact→0` absolute-identity limit recovering the current bracket
  exactly. Iteration 44 is MATERIALS' turn by rotation regardless, so the
  lock costs nothing procedurally — it only removes the option to defer a
  4th time. (2) **Close T27's remaining settling gap in full**: interior
  `FALLBACK_ANGLES` (0°,±5°,±15°,±25°) at STEPS≥2800, Block ARTICLE's
  article-PRESENT legs at settled STEPS, Block EXTEND (41–43°) if budget
  allows — prioritize **39–40°/450nm** as the next convergence-check
  point (EM's Phase-5 finding: zero direct multi-STEPS convergence data
  exists at 450nm anywhere in this record, and it is both the coarsest
  grid, cpl=15, and the most grazing angle still untested). Reuse
  exp-065/066's own harness (`CONFIGS["C40"]`/`_settle_one`/`_c_empty`).
  Explicitly does NOT compete with R_contact for budget (desk vs. FDTD
  resource classes) — MATERIALS' own Phase-5 review recommends folding
  both into one Iteration-44 cycle if scope allows. (3) **Block MINI's
  period-match test**: run QUANTUM OPTICS' proposed zero-cost desk check
  first (does this cycle's own 36-cell settling-delta dataset already
  show `A·cosθ`-periodic structure matching T21's period?), then build
  the properly-powered FDTD version (≥2–3 T21 periods at ~0.2° spacing,
  at settled STEPS) or formally retire it — two consecutive cycles of
  deferral-behind-relabeling is enough; a third would be worth flagging
  as Checkpoint-4-adjacent, per this program's own T23 precedent. Full
  record: `experiments/066-t27-block-main-settling-reverification/` —
  Phase-1 proposal, five Phase-2 blind critiques, Phase-2 Red Team audit,
  Phase-3 synthesis, NOTES.md, `phase4_results.md`, six Phase-5 blind
  reviews, Phase-5 Red Team final audit; `lab/caveat_lint_config.json`
  widened twice (Phase-3 mandatory fix D, Phase-5 mandatory fix M1).
- **[superseded — the exp-065-era queue, retained only as a pointer to
  its own history; the binding record is the Iteration-43 [done] entry
  above and the CURRENT top-of-queue block immediately above this one]**
  (1) **Re-verify
  `experiments/041-t20-angle-audit`'s own MAIN-block ±35°/±38°/±40° rows
  at STEPS≥2800, and scope exactly how many downstream citations are
  affected** — the single highest-stakes, most-converged item across the
  entire packet; upstream of T21's fringe model, T16's quadrature deltas,
  T20/T24's own citations, and every near-threshold constraint-3
  τ-bucket call since Iteration 18. Reuse exp-065's own construction
  (`static_construction_identity`'s gate pattern,
  `settling_trend_diagnostic.py`). (2) **Close exp-065's own settling-
  characterization gap in full**: extend STEPS=2800 to the four untested
  interior `FALLBACK_ANGLES` (0°/±5°/±15°/±25°), re-run Block ARTICLE's
  article-PRESENT legs (not just the empty floor) at settled STEPS,
  complete the 750nm/C80 four-point convergence trend, and either
  implement or formally retire the period-match test for Block MINI
  (`P-VIS42-10`). Ranked #2, not tied with #1, because narrower in
  downstream stakes — though MATERIALS, VISION, and QUANTUM each rank
  pieces of it first from their own charters. (3) **Source, or formally
  model, the CNT-forest root-to-substrate thermal contact resistance
  (`R_contact`)** — this program's still-standing top-of-queue item since
  Iteration 40, untouched by exp-064 or exp-065, now deferred for a
  second consecutive cycle. The only queued item that can MOVE TD-5's own
  margin (this program's thinnest safety factor of any kind, 7.8× over
  κ_critical) rather than relabel or disclose one; a third consecutive
  deferral would itself be worth flagging at Iteration 44. Full record:
  `experiments/065-t24-absorb-boundary-sweep/` — Phase-1 proposal, five
  Phase-2 blind critiques, Phase-2 Red Team audit, Phase-3 synthesis,
  NOTES.md, `phase4_results.md`, six Phase-5 blind reviews, Phase-5 Red
  Team final audit; `lab/caveat_lint_config.json` widened (one new
  entry).
- **[superseded — the exp-064-era queue, retained only as a pointer to
  its own history; the binding record is the Iteration-42 [done] entry
  above and the CURRENT top-of-queue block immediately above this one]**
  (1) **Source, or at minimum formally
  model as a new series thermal-resistance term, the CNT-forest
  root-to-substrate thermal contact resistance** — named at or near #1 by
  five of six Iteration-41 Phase-5 seats; the ONLY carried item that can
  actually MOVE TD-5's own margin (this program's thinnest safety factor
  of any kind, 7.8× over κ_critical), not merely relabel it — exp-064 was
  a pure labeling cycle by construction and moved zero numbers. Build as
  a genuinely new `R_contact` series term, gated by an `R_contact→0`
  absolute-identity limit recovering the current bracket exactly — not a
  `κ_solid` reparameterization, which would conflate a bulk-material
  property with a boundary/interface property the current formula has no
  slot for. (2) **Harden and extend the `length_provenance` guard's own
  reach** — bundle three convergent Iteration-41 Phase-5 findings into one
  item: ELECTROMAGNETISM's own top-ranked remedy (replace stage-24 gate
  4's non-greedy regex with an `ast`-based call parser, eliminating the
  demonstrated nested-paren failure class by construction, and extend the
  source-scan to the four experiment `run.py` files it currently doesn't
  reach — this directly discharges Iteration 41's own new forward
  tripwire, the single highest-value fix of the three); VISION's
  `trigger_terms` widening to include headline numeric values
  (`correction_factor`, `1.015703`, `0.089731`), closing the name-vs-value
  blind spot both VISION and THERMODYNAMICS independently found in
  `caveat_lint_config.json`/`numeric_lint.py`; MATERIALS'
  `material_realizability_tier` field extending `geometric_realizability`
  to the licensed path (optional today, no live call site to retrofit,
  cheap to add before one exists). PHOTONICS' own broader ask — a
  codebase-wide sweep for other extinction-derived lengths silently
  feeding a geometric-length role — folds in if scope allows, else
  correctly defers one more cycle. (3) **Pin the record-blackness/
  Vantablack-class CNT forest's own pitch/diameter AND through-thickness
  thermal conductivity together, in one query set** — Iteration 39's
  still-open #1 item, now carrying a third sub-question (the
  thickness/realizability comparison exp-064's own struck §6 raised and
  declined to resolve). **Bundle MATERIALS' own recommended recovery of
  the struck §6 comparison into `REALIZABILITY_MEMO.md` as part of this
  same query cycle** — compute and commit the ≈0.66×–10.56× MP-2-vs-MP-5
  comparison once, explicitly captioned as a restatement of two
  already-scored exp-061 numbers (not a new exp-064 finding), carrying
  PHOTONICS' idealization caveat verbatim (forest-height ≠ single-pass
  Beer-Lambert path length; not corrected for oblique incidence or
  diffusive/scattering transport). **Carried, lower priority**: EM's
  provenance-ROLE structural gap and MATERIALS' material-identity-
  coherence gap on `measured_geometric` (both naturally fold into item 2
  once a real `measured_geometric` call site is sourced); PHOTONICS'
  diffusive-transport (Kubelka–Munk-class) correction to the Beer-Lambert
  `L=τ_true/α` back-calculation, a genuinely open, deeper question, real
  but gates no current verdict; QUANTUM's own low-urgency, one-sided-safe
  non-thermalized-energy re-emission flag. **Recommendation, not a
  ruling** (Red Team, Iteration 41 Phase-5 final audit §9): Iterations
  38–41 are four straight cycles with zero constraint-scored FDTD (three
  of the four forced by binding integrity commitments, not optional) —
  does not fire Checkpoint criterion 5 on the criterion's own text, but
  Iteration 42's own lead (VISION SCIENCE, next in rotation, constraint-3's
  own least-recently-exercised owner) should scope whichever item it
  selects to close into, or directly feed, an actual constraint-scored
  FDTD run. Full record: `experiments/064-length-provenance-guard/` —
  Phase-1 proposal, five Phase-2 blind critiques, Phase-2 Red Team audit,
  Phase-3 synthesis, NOTES.md, phase4_results.md, six Phase-5 blind
  reviews, Phase-5 Red Team final audit; `lab/thermo_sidecar.py`/`lab/
  validation/run_all.py` stage 24 (new, trust-suite-gated); `lab/
  caveat_lint_config.json` widened (one new entry).
- **[superseded — the exp-063-era queue, retained only as a pointer to
  its own history; the binding record is the Iteration-41 [done] entry
  above and the CURRENT top-of-queue block immediately above this one]**
  **(1, adopted as a BINDING FORWARD
  COMMITMENT, not merely a ranked pick)** resolve T23's witness-scale
  length-legitimacy question (`L=τ_true/α`, exp-063's own MP-5 figure,
  reused as a literal Fourier conduction-path length): deferred at
  Iteration 38 (THERMO), Iteration 39 (EM/Red Team), and again at
  Iteration 40 (mandatory fix 6, disclosure only) — three consecutive
  cycles against an already-decided rule (`gas_conduction_h_eff`'s own
  docstring, closed by argument at Iteration 23) and an
  already-identified violation. Source a real geometric length for the
  actual candidate class, or give `gas_conduction_h_eff`/
  `front_surface_conduction_correction` an enforced `length_provenance`
  code-level guard. **A fourth deferral past Iteration 41 is to be
  treated as a program-integrity finding for Red Team's own ruling at
  Iteration 42** — the same disposition this program gave the
  `exp061-t18-evidentiary-tier-propagation` lineage after its second
  self-catch. (2) Source, or at minimum formally model as a third
  disclosed scenario alongside exp-063's own front-colocated/rear-only
  bracket, the CNT-forest root-to-substrate thermal contact resistance
  (MATERIALS' Iteration-40 Phase-5 finding — query 10's own van der Waals
  contact-resistance result plausibly governs the root-substrate
  interface too, not just the inter-tube contacts already modeled);
  directly relevant given exp-063's own TD-5 has only 7.8× headroom on
  κ_solid, this program's thinnest safety factor of any kind on record.
  (3) Pin the record-blackness/Vantablack-class CNT forest's own
  pitch/diameter (Iteration 39's still-open #1 item) AND through-
  thickness thermal conductivity (PHOTONICS' Iteration-40 Phase-5
  finding: exp-063's TD-5 multiplies an optical constant and a thermal
  constant sourced from different, unconfirmed-common CNT-forest
  geometry classes) together, in one query set — closes both the
  standing near-field-coupling question and the optical/thermal
  material-provenance mismatch at once; exp-063's own query 8 already
  re-targeted the pinned *Carbon* 2018 paper and found geometry but no
  thermal figure, making this a natural single follow-up rather than two
  searches. **Carried, lower priority**: QUANTUM's own low-urgency flag
  (a non-thermalized-energy re-emission channel, confirmed one-sided-safe
  for the current candidate identity, exp-063 Phase 5); the disclaimer
  rule's own general `caveat_lint_config.json` registry entry (non-
  blocking, queued since Iteration 40); CNT-forest ρ/C_p sourcing
  (explicitly scoped out at exp-063). Full record: `experiments/063-cnt-
  forest-thermal-conductivity-biot-check/` — Phase-1 proposal, five
  Phase-2 blind critiques, Phase-2 Red Team audit, Phase-3 synthesis,
  NOTES.md, phase4_results.md, six Phase-5 blind reviews, Phase-5 Red
  Team audit; `lab/thermo_sidecar.py`/`lab/validation/run_all.py` stage
  23; `lab/caveat_lint_config.json`/`lab/numeric_lint_config.json`
  widened (four new/widened entries).
- **[superseded — the exp-062-era queue, retained only as a pointer to
  its own history; the binding record is the Iteration-40 [done] entry
  above and the CURRENT top-of-queue block immediately above this one]**
  **(0,
  process-mandatory, precedes the physics queue)** independently
  re-verify (not merely re-assert) exp-062's own 10-item mandatory-fix
  docket at pre-flight, and audit every remaining `caveat_lint_config.json`
  entry for the same `candidate_globs` blind-spot shape (a hand-curated
  named-filename list rather than a broad per-experiment glob), not just
  the two entries found this cycle. (1) **Pin the record-blackness/
  Vantablack-class CNT forest's own inter-tube pitch/diameter** — every
  one of the six Phase-5 reviews independently names this; query 13's own
  success (pinning the `n_eff=1.04+0.01i` citation to *Carbon* 2018, vol.
  129, pp. 8–14) makes a targeted follow-up search against that specific
  paper's own reported density/pitch figures the natural next step,
  closing (not merely sharpening) the standing `l_geometric_m`
  homogenization-validity question THERMODYNAMICS/QUANTUM/EM's own
  Phase-5 dispositions all trace back to. (2) **Resolve EM-5b's
  near-field-coupling direction with an actually dedicated query set** —
  QUANTUM's own Phase-5 review found none of exp-062's 18 queries ever
  targeted superradiant/subradiant/coupled-dipole terminology; "CONFIRMED
  UNDECIDABLE" is an honest null result, not yet a genuine search. (3)
  **Build the numeric/derivation-consistency-check tooling** — already
  re-filed with a named owner (the Director, mandatory zero-cost rider,
  regardless of that cycle's lead seat, per Red Team's Iteration-38
  mandatory-fix item 6) — widened per EM's own Phase-5 recommendation to
  catch not just a NUMBER drifting unreconciled across sibling files but
  the SAME derivation methodology applied two inconsistent ways within
  one document (exp-062's own EM-6/EM-7 R-vs-T drop, a ready regression
  test case). **Carried, lower urgency**: EM's `sim.omega` historical
  registry entry; THERMO's T25 sidecar-absence entry (bundle-candidate
  with the length-scale-staleness entries).
- **[superseded — the exp-060-era queue, retained only as a pointer to
  its own history; the binding record is the Iteration-38 [done] entry
  above and the CURRENT top-of-queue block immediately above this one]**
  (1) **The closed-form two-region (PEC core + uniform complex-ε
  annulus) Bessel/Hankel `Q_ext_uniform` series** — four-seat convergence
  (PHOTONICS/MATERIALS/VISION/QUANTUM), zero-FDTD, the same non-
  tautological external-validation role MF-6 played at exp-059. (2) **The
  partial-grading dose-response curve** — four-seat convergence
  (MATERIALS/EM/QUANTUM/VISION): sweep grading length within the fixed
  48-cell/τ-matched shell, turning exp-060's two-point comparison into a
  real interpolation. (3) **QUANTUM's own item**: a genuinely
  attenuation-matched third `uniform` article (`t'≈0.566`) as a measured
  FDTD check on exp-060's own corrected bias-direction claim. (4)
  PHOTONICS' 3-λ sweep / T26 λ-angle generalization, paired with
  `graded_black_shell_flagship`'s own 450/750nm sweep (PHOTONICS +
  MATERIALS). (5) EM's TE_z companion series for `qext_theory.py`. (6)
  Carried backlog, lower urgency, unblocked: shell-vs-solid thermal-mass
  parameterization (open since Iteration 22/T23, now a fourth-
  consecutive-cycle-plus item); R3-on-loaded-legs for
  `off_pass_joint`/`off_bracket_joint`; a Geary-Hinkley tail-shape model
  of `C(δ)`; P-VIS-5's angle-quantization sensitivity formula; QUANTUM's
  convergence-guard audit pass across `lab/`'s other closed-form modules;
  `coupled_segment_general`'s trust-suite promotion.
- **[queued — ranked for Iteration 37+, per Red Team's Iteration-36
  Phase-5 reconciliation of all six seats — a rare six-way convergence
  on item 1, exp-059 — CURRENT top-of-queue, supersedes the list below as
  the active ranking, retained as valid backlog, not deleted]** (1) **The
  sharp-uniformly-lossy-disk FDTD control run** — all six Phase-5 seats
  named this in their top-3, five as #1; disentangles "edge grading
  reduces diffraction" from "any bulk loss damps PEC's resonance
  ripple," directly resolving MATERIALS' own PARTIAL-driving concern
  (MF-5) — cheap, one new scene, reuses `materials.pec_disk` at
  `R_COAT` with uniform non-graded sigma matched to the shell's own
  optical depth. (2) **The exp-057 erratum fix** — three string edits
  (`NOTES.md`/`run.py`/`results.json`), zero new FDTD, corrects the
  self-contradictory "~295×" figure to the code-verified 1655.18×,
  execute as a zero-cost rider before Iteration 37's own proposal work.
  (3) **Build the mechanical caveat-propagation-check tool** Red Team
  authorized at Iteration 36's Checkpoint-4 ruling — grep every
  mandatory-fix caveat's own key phrase across every file touched by
  that fix's cited sites, not just the sites the fix draft names by
  hand; a sixth hand-applied wording patch would not distinguish this
  closure from the ones that already preceded and failed to hold. (4)
  **MATERIALS' absorptivity/mechanism literature check** — now SEVEN
  cycles deferred (Iteration 29→36), approaching this program's own
  escalation pattern; pin it to one checkable question before an eighth
  deferral forces an unconditional lock. (5) **EM's TE_z companion
  series** for `qext_theory.py` — mechanical, zero new FDTD, would let
  gate 1's polarization-agnostic tautology claim be numerically
  demonstrated rather than argued, and resolves the Hankel-choice
  (`H^(1)` vs `H^(2)`) documentation gap EM's own Phase-5 review flagged.
  (6) **PHOTONICS' T26 λ/angle generalization** (oblique-incidence
  `Q_ext` extension, still a closed-form Bessel/Hankel series, zero new
  FDTD), paired with **`graded_black_shell_flagship`'s own 450/750nm
  sweep** (both PHOTONICS and MATERIALS named this). (7) Carried
  backlog, unblocked, lower urgency: R3-on-loaded-legs for
  `off_pass_joint`/`off_bracket_joint`; the flank-denominator
  distribution upgrade; a Geary-Hinkley tail-shape model of `C(δ)`;
  P-VIS-5's angle-quantization sensitivity formula; shell-vs-solid
  thermal-mass parameterization (3rd consecutive cycle open); QUANTUM's
  convergence-guard audit pass across `lab/`'s other closed-form modules
  for the "exact-threshold-from-a-wide-bracket" pattern (QUANTUM's own
  new Phase-5 finding: the `Q_ext(x)` module's own "x=260 exact
  threshold" claim is itself imprecise, true NaN onset ≈x=259 — Tier-2,
  non-blocking); `coupled_segment_general`'s RK4-cross-checked
  trust-suite promotion.
- **[superseded — the original locked-item bullet, retained only as a
  pointer to the LOCK's own history; the binding record is the [done]
  entry above]** ~~The `Q_ext(x)` closed-form cylinder/disk check~~ —
  now closed by exp-059, see above.
- **[queued — ranked for Iteration 36+ (behind the LOCKED item above),
  per Red Team's Iteration-35 Phase-5 reconciliation of all six seats,
  exp-058 — CURRENT top-of-queue, supersedes the list below as the
  active ranking, retained as valid backlog, not deleted]** (1)
  **R3-on-loaded-legs** — resolution check (cpl 20→30, exp-056's own
  rescaled-geometry idiom) on `off_pass_joint`/`off_bracket_joint`
  themselves, still never run (independently found by EM and QUANTUM at
  Iteration 33, unaffected by Iteration 35's different phase-variance
  axis) — Iteration 34's own #2 competitive priority, carried forward
  two cycles now. (2) **Upgrade the flank-denominator diagnostic** from
  a binary `<0.20` flag to a reported distribution/correlation — EM's
  own Iteration-35 Phase-5 re-analysis found a real, moderate
  (`corr≈0.45–0.50`, R²≈0.20–0.25) but only partially-explanatory
  correlation the binary flag can't show; also re-derive the 0.20
  threshold for an N=2000-ensemble context rather than reusing the
  single-realization calibration unmodified. (3) **A Geary-Hinkley
  quantitative model of `C(δ)`'s own tail shape** — QUANTUM OPTICS'
  Iteration-35 Phase-5 proposal, near-zero-cost now that
  `b_obj_draws`/`b_flank_draws` are persisted (exp-058's own
  `recompute_flux_signs.py`). (4) **P-VIS-5's angle-quantization
  sensitivity formula** (derive, not measure, per Red Team's own
  Iteration-33 mandatory fix) — named by 3 of 6 Iteration-33 seats,
  still open. (5) **MATERIALS' absorptivity/mechanism literature check**
  (exp-052 queue item 5) — zero-FDTD, deferred since Iteration 29, now
  **SEVEN** cycles running — flagged explicitly by both MATERIALS and
  Red Team at Iteration 35 as approaching this program's own escalation
  pattern (half the count that triggered two prior unconditional locks).
  (6) **λ/angle generalization** (450nm/750nm) for the T26 near-null
  result — exp-056 tested one native geometry at one λ only. (7)
  **Shell-vs-solid thermal-mass parameterization** — third-consecutive-
  cycle open item (Iteration 20→31→34), confirmed non-load-bearing to
  date but "a live landmine" for a future transient prediction. (8)
  **`graded_black_shell_flagship`'s own 450/750nm sweep** through the
  corrected chain, zero new FDTD. (9) **`coupled_segment_general`'s
  promotion** to a real trust-suite stage with an RK4 cross-check —
  exp-054's own carried item, still unbuilt across five cycles now.
- **[queued — ranked for Iteration 33+, per Red Team's Iteration-32
  Phase-5 reconciliation of all six seats, exp-055 — superseded by the
  Iteration-33 list above, retained as historical backlog; both
  are retained as valid backlog, not deleted]** (1) **A combined T26
  build**: the generalization test on a near-null σ(I) article
  (`off_pass`/`off_bracket`, exp-032/033) — the regime where the empty-
  scene coherent-injection artifact could actually flip a live
  PASS/MARGINAL verdict (QUANTUM OPTICS' and VISION SCIENCE's own top
  pick) — folding in, as same-build riders at near-zero marginal FDTD
  cost: EM's own empty-scene-specific R3/resolution check at the ACTUAL
  r=78 geometry (never done at Iteration 32 — the only R3 check ran on the
  unrelated small canonical scene) and PHOTONICS' window-position/
  angle-quantization sensitivity scan on the T26 measurement itself. Any
  future `C_thr` citation from this build must carry VISION's own T2
  photopic-regime qualifier (Iteration 32's own mandatory-fix docket).
  (2) **THERMODYNAMICS' `graded_black_shell_flagship` re-run through the
  corrected `mixed_length_scale_regime`** (exp-054 queue item 1, below) —
  now genuinely twice-deferred (Iterations 31 and 32), zero new FDTD, this
  program's own thinnest thermal-detectability margin (~6.04×, itself
  shown to shrink ~3.03× under this exact bug class) — if deferred a third
  time, this item should be considered for the same unconditional-trigger
  bar this program has applied twice before (`h_eff`, r=156/`graded_
  black_shell`). (3) **MATERIALS' absorptivity/mechanism literature check**
  (exp-052 queue item 5, below) — zero-FDTD, deferred since Iteration 29,
  now four cycles running.
- **[queued — ranked for Iteration 32+ / alongside the LOCKED Iteration-31
  slot, per Red Team's Iteration-29 Phase-5 reconciliation of all six
  seats]** (1) **The coherent-vs-incoherent ambient-sum bridge-gate
  revalidation, built against the actual equal-amplitude N9 configuration**
  (not exp-029's own strong-beam/weak-probe idiom) — new live thread **T25**
  (LOGBOOK.md), ranked #1 or #2 by five of six exp-052 Phase-5 seats
  (PHOTONICS #3, EM #2, QUANTUM #1, THERMODYNAMICS #2, VISION #1). No
  geometry this program has run, in 29 iterations, has ever had its actual
  ambient-sum instrument empirically bridge-gated — QUANTUM's own
  concretely-scoped proposal (joint equal-amplitude injection, reusing
  suite stage 11's existing field-identity gates) is the cheapest correct
  next build. (2) **The λ-generalization run** (450nm + 750nm, r=156, both
  families) — ranked by three of six seats (PHOTONICS #1, VISION #3,
  MATERIALS #2), cheap, directly tests whether exp-052's own T14 reframe is
  general or a 600nm/2.4λ-specific coincidence (three on-the-record program
  precedents — R2, T21, the Iteration-19 c*(λ) finding — for treating
  single-λ near-field results with exactly this suspicion). (3) **A
  formally committed `C(z/z_R)` extrapolation fit for the fixed-absolute
  family**, pre-registered falsifiable bands on `C_∞` vs. −1, ideally a 4th
  r-point — executes T8's own long-standing requirement for the first time
  on a family whose slope is correctly signed (EM #1, PHOTONICS #2);
  resolves whether exp-052's own 0.12–0.16 C_∞ shortfall is real or a
  3-point-fit artifact. (4) **The genuine FDTD `ABSORB` sweep at GEOM78** —
  carried unrun across Iterations 26–29 (four straight cycles now), already
  flagged at Iteration 28 as "approaching unconditional-trigger territory
  if deferred again" — one more deferral from meeting the same bar just
  applied to `h_eff`. (5) **MATERIALS' absorptivity/mechanism literature
  check** (T18-dependent, zero-FDTD either way) — the one remaining
  unchecked axis between exp-052's own PLAUSIBLE tier and a tier change on
  this program's now-favored design lead. (6) **A targeted N9-vs-N17
  angular-quadrature check on the opaque-absorber article class** (VISION,
  new this cycle) — T16's entire angular-sampling uncertainty budget has
  only ever been measured on a near-null σ(I) article, never on the
  deep-shadow class most of this program's citations, including exp-052's
  own headline, actually are. (7) **Extend exp-052's own core-fill check to
  the full N9 sweep**, not just θ=0 (MATERIALS) — the θ=0 null is decisive
  at boresight but T9's own established mechanism is a grazing/tangential
  effect; the ±25°/±35° angles that actually feed the headline deepening
  have never been core-fill-tested at these ratios. (8) **QUANTUM's
  grating-lobe/array-factor n\* criterion for `beam_divergence_coherent`**
  (carried unchanged from Iteration 28's own queue, item 2 there) — scored
  against the 72 `coherent` rows exp-051 already computed and labeled,
  using exp-046's validated zero-free-parameter closed form. (9) Low
  priority: promote the `_geom_derived`/`_G_for_g` hoisting pattern to a
  shared utility at the next geometry-parameterized module. Carried
  forward, not re-ranked: VISION's sub-degree angular sweep across
  36°–40° at 750nm/FWHM=2°/GEOM78 (Iterations 27/28/29); T8/T13/T14's
  sensitivity-band minimum bar (dormant 20+ iterations); fresh c*(λ) refit
  at the new geometry; regime-stratify T2's ±0.3-log uncertainty near the
  absolute-threshold edge; ocular-dose disposition.
- **[queued — ranked for Iteration 32+, per Red Team's Iteration-31
  Phase-5 reconciliation of all six seats, exp-054]** (1) **Re-run
  `graded_black_shell_flagship` through the corrected
  `mixed_length_scale_regime`** — this program's flagship article, at the
  record's thinnest thermal margin (~6.04×), still on the old,
  now-twice-repudiated `H_CONV=5.0`/hardcoded-mass/`w_on`-area chain;
  cheapest same-pattern desk-analytic work available (THERMODYNAMICS #1,
  Red Team's own top priority). (2) **Promote `coupled_segment_general`
  into a real trust-suite stage** with a nonzero-initial-condition
  numerical-integrator (RK4) cross-check — EM's Phase-5 review already did
  the verification once outside the repo; commit it as a permanent gate
  (EM #1). (3) **Parameterize `mixed_length_scale_regime`'s fill-fraction
  and material-provenance strings** so a future caller with a different
  material doesn't silently inherit exp-054's own silicon/ASSUMED-T18
  citation (MATERIALS #1, THERMODYNAMICS #2). (4) **A desk closed-form
  `Q_ext(x)` cylinder/disk check** bounding `w_on`'s ~3.03× excess over
  `r_out` — diffraction vs. `iso_xsec_sq` convention artifact (PHOTONICS
  #1, EM #2, THERMODYNAMICS #3, QUANTUM #4 — four of six seats). (5) **Run
  the mixed chain across the standard 450/600/750nm sweep**, reusing
  already-committed exp-026/044 per-λ data, zero new FDTD (PHOTONICS #2).
  (6) **T8/T13/T14's near-field→witness-scale `h_eff` bridge** — the
  largest standing gap in this thread, again explicitly left open
  (P-054-6); named by every seat that discussed scope, ranked lowest only
  because it is the biggest build of the six, not because it matters
  least.
- **[SUPERSEDED — now LOCKED to Iteration 30, see above]** stage-10
  temporal instrument (VISION's Iteration-2 Phase-5 #2): TCSF bars pinned
  first (de Lange/Watson, sourced) — the last unmeasured perceptual axis
  (T3), gates constraint 4. *This bare line, sitting outside the numbered
  queue for 10 consecutive iterations, is exactly the mechanism by which
  the item silently stopped competing (Red Team's Iteration-28 finding).
  It is retained only as a pointer; the binding entry is the LOCKED
  Iteration-30 slot above.*
- **[housekeeping]** cloud shift 10 (old routine, fired 06:23Z mid-redesign)
  committed its r2-isolation experiment as a second "exp-020" on main —
  renumbered to exp-022/023 at the redesign merge, content untouched, noted in
  SESSION_LOG. Old `photonlab-shift` routine to be paused by Marsh
  (owner-created; agents cannot modify it) — replaced by the panel-shift
  routine.

- **[open, contract lane]** Artifact-schema formalization for the ambient
  instrument: the `angle_deg` source key + per-run energy/intensity ledger
  rows belong in `lab/ARTIFACTS.md` — that is the cross-lane contract
  (Bonnie's veto lane, AGENTS.md), so it needs the counterparty-review PR,
  not a unilateral panel edit. Until then the ledger lives experiment-side
  in `results.json` (exp-020 synthesis, docket #4).

- [done 2026-08-09] Artifact schema v0.1.0 — merged (`ba2cc7f`), verified
  on all three benches.
- [done 2026-08-09] Preston's cold read → house figure style **R1–R4**
  (shadows self-explain · orientation gizmo · panels work solo · witness
  view beside the map). His reads gate exp-001 figures.
- [done 2026-08-09, this PR] Artifact emitter (`lab/emit.py`): quadrature
  capture, angle-resolved observer camera (Fresnel-gated, suite stage 6),
  manifest from engine self-recorded scenes. First committed artifacts:
  `experiments/000-hello-maxwell/artifacts/{empty,cylinder}` — CI now runs
  the Evidence Gate on committed artifacts every push.
- [claimed: Bonnie] `lab/viz` extraction + observer camera rendering,
  carrying the Evidence Gate figure checker + R1–R4. Unblocked by this PR;
  exp-000 artifacts are her real data.
- [done 2026-08-09, this PR] **Graded-black absorber** — exp-001's object
  (b), designed and gated (suite stage 7, 5/5): R ≤ 0.2% across the
  450–750 sweep, observer return at the camera floor. Schema bumped 0.2.0
  (new builder row per the extension rule); exp-000 artifacts re-emitted.
- **exp-001 scope FROZEN 2026-08-09 (Marsh's word)**: three scenes
  (reflector / graded-black absorber / reduced cloak) + observer-at-source
  figure + NOTES + 3-λ sweep. Future freezes: agent consensus per
  AGENTS.md amendment (this PR).
- [done 2026-08-09] **exp-001 The Flashlight Statement** — verdict:
  absorber, 4.5/5 pre-registered (PR #5). Witness figure (Bonnie) + agent
  cold read close the presentation half.
- [done 2026-08-09] **exp-002 How Invisible Is Invisible** — cross-section
  machinery (stage 8) + 12-run sweep. Finding: "invisible" has a
  direction — cloak wins all-angle 4×, absorber wins source-observer by
  orders of magnitude; cloak monotonically better toward red.
- [done 2026-08-10, cloud shift] **exp-003 the broadband wall,
  redesigned** — cpl fixed at 20 across a 6-point λ sweep (420–750nm),
  geometry scaled in cells to hold physical (nm) defect size constant.
  First run caught its own domain-sizing bug (box independence blew up
  at the largest scale factor — a harness bug, not physics) before any
  result was trusted; full sweep rerun clean (box_dev ≤1.1%, cross_dev
  ≤0.2%) after fixing it. Findings: (1) the red-side improvement is real
  and NOT a resolution artifact (λ=600 point reproduces exp-002 to
  <1%, confirming the harness; net Q_ext(cloak) 0.460→0.318 across the
  sweep with cpl held fixed) — exp-001's flagged confound is resolved;
  (2) but it is NOT the (defect/λ)² law hypothesized — log-log slope
  ≈0.79 (R²=0.87), well below the predicted [1.5,3.0] band; (3) the
  trend is non-monotonic — a bump at 480nm exp-002's 3-point sweep
  couldn't have shown. Working hypothesis for exp-004: the mu_r clamp
  band's fixed *relative* extent (~0.29·r1) interacting with the fixed
  grid, not simple electrical-size scaling.
- [done 2026-08-10, cloud shift 2] **exp-004 candidate** (hold electrical
  size and cpl fixed, sweep `mu_r_floor` alone) — run; see Current state.
- [done 2026-08-10, cloud shift 2] exp-005 (resolution-convergence check
  on exp-004's clearest jump, cpl 20→30 at 600nm) — run; see Current
  state.
- [done 2026-08-10, cloud shift 3] exp-006 candidate (vary `eps_z`
  independently of overall cloak scale) — run; see Current state.
- [done 2026-08-10, cloud shift 3] exp-007 (chasing exp-006's design
  lead, core=8–25 at fixed floor=0.10) — run; see Current state.
- [done 2026-08-10, cloud shift 4] exp-008 candidate (bare-disk control,
  resolving exp-007's caveat) — run; see Current state.
- [done 2026-08-11, cloud shift 5] exp-009 candidate (ratio below core=8)
  — run; gate failed at 2 of 4 points, resolved by exp-010. See Current
  state.
- [done 2026-08-11, cloud shift 5] exp-010 (resolution check on exp-009's
  gate failure + non-monotonic bump, cpl 20→30) — run; both anomalies
  were the same artifact, resolved cleanly. See Current state.
- [done 2026-08-11, cloud shift 5] exp-006's candidate B (floor sweep at
  a non-baseline core, core=15) — run as exp-011; fully monotonic, no
  sign-flip, strengthens the eps_z=2.25-is-the-outlier reframe. See
  Current state.
- **[open]** exp-007's queued multi-λ check, now sharpened by exp-008
  and exp-010: does the core=8 design lead — and its *genuinely better
  relative cloaking effectiveness*, not just a smaller hidden object —
  survive across the exp-002/003 wavelength range, or is it a
  600nm-only result? Needs exp-003's cell-scaling machinery to hold
  physical geometry fixed across λ, not a quick bolt-on — worth a
  dedicated shift.
- [done 2026-08-11, cloud shift 6] exp-006's reframe, third and fourth
  points (core=40, core=48) — run as exp-012 and exp-013; both strictly
  monotonic, no sign-flip. Generalization complete: 3 of 4 core/eps_z
  points monotonic, only core=30/eps_z=2.25 sign-flips. See Current
  state.
- [done 2026-08-11, cloud shift 7] *Why* does eps_z≈2.25 specifically
  produce sign-flipping floor structure? — run as exp-014 (the fine
  bracketing scan) and exp-015 (resolution check on the finding). The
  negative jump is a real, contiguous 4-point trough in eps_z (≈2.18–
  2.41), confirmed grid-independent — not an isolated point. See Current
  state.
- [done 2026-08-11, cloud shift 8] *Mechanism* candidates for the
  eps_z≈2.25–2.4 trough — run as exp-016 (outer-boundary impedance
  mismatch) and exp-017 (angular-pattern shape comparison, new
  `lab.sections.angular_scattered_pattern` capability). **Both refuted.**
  See Current state.
- [done 2026-08-12, cloud shift 9] The frequency-domain mechanism check
  proposed by exp-017 — run as exp-018. **Major reframe: the "eps_z
  trough" is not an eps_z effect.** It's a shell-thickness standing-wave
  condition at exactly 3λ (exp-002's original geometry, a coincidence
  not a chosen eps_z). See Current state.
- [done 2026-08-12, cloud shift 9] Direct test of exp-018's standing-
  wave hypothesis at 2λ — run as exp-019. **Does not generalize**: no
  dip near 2λ, ruling out a generic "shell = integer × λ" rule. 3λ looks
  specific, not a member of a broader family (yet). See Current state.
- [done 2026-08-12, cloud shift 10] exp-019's own queued follow-up (is
  the 3λ feature reproducible at a different fixed r2?) — run as
  exp-022. **No**: neither r2=75 nor r2=120 reproduces the negative
  jump at their own shell=3λ point. The feature is r2=90-specific.
  Gate miss at r2=75/floor=0.10 resolved same-shift by exp-023. See
  Current state.
- **[open, parked — trough line]** exp-022's own queued follow-up (see its NOTES.md Next):
  the trough has now survived five mechanism/generality checks in a row
  (exp-016 impedance, exp-017 angular pattern, exp-018 eps_z, exp-019
  integer-λ, exp-022 r2) without one explaining or generalizing it.
  Two paths for a future dedicated shift: (a) declare
  r1=30/r2=90/λ=600nm/floor∈{0.10,0.18} an idiosyncratic anomaly and
  stop chasing it, returning fully to the design-lead line; or (b) one
  more targeted test — hold r1 AND r2 both fixed at exactly 30/90 and
  sweep λ finely (1–2nm steps) around 600nm to see whether the negative
  jump is itself narrow-band (a true resonance linewidth) — the mirror
  of exp-018's coarse λ sweep, which rescaled geometry to hold eps_z
  fixed rather than holding geometry fixed.
- [open, secondary, exp-017] A local-maxima count found 13 angular peaks
  at the trough vs 10 at each flank — unscored, not folded into the
  magnitude-only conclusion, but worth a finer-binned or bare-disk-
  referenced recheck if a future shift returns to this mechanism
  question. (Read now in light of exp-018/019: "the trough" in that
  observation is specifically the shell=3λ point, not an eps_z-axis
  location.)
- [open] The `mu_r_floor < 0.05` direction (toward the true r1
  singularity) remains untested — needs a paired `courant_frac`
  reduction for CFL stability (derivation in exp-004 NOTES.md
  Idealizations). **Sharpened by exp-011:** the instability is
  geometry-dependent, not purely a low-floor phenomenon — floor=0.05
  itself is already CFL-unstable at core=15/eps_z=1.44 (ceiling 0.268 <
  courant_frac 0.32), where it was stable at core=30/eps_z=2.25. Any
  future floor sweep at core values much below ~20 should check the
  CFL ceiling per-point rather than assume exp-004's core=30 margin
  carries over.
- [done 2026-08-10, cloud shift] exp-001 observer-table rerun post phasor
  fix — camera floor drops ~17× (bug removed), absorber return tracks the
  new floor at every λ, reflector/cloak shift a few % (same order, same
  ranking). Values shifted, verdict stands, exactly as queued.
- [open] Parking lot: black-lined cloak hybrid (eat the backward glint),
  Q vs incidence angle, near-to-far transform.
- Parking lot: TF/SF injector, true PML, finer-grid cloak, fourth panel
  (adjoint discovery), Disclosure physics-annex (humans' call), Blender/UE
  3D presentation when a design earns it.
