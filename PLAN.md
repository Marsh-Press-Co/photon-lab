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

## Current state (2026-09-05, panel Iteration 90 done (exp-113, PARTIAL --
BLOCKED BY COST GATE, VISION SCIENCE's rotation-lead cycle: executed the
Reconciled Iteration-90 queue's Tier-1 items 1-4 -- the +168.75deg bin
(r=312/cpl=25, mirror companion of exp-112's own -146.25deg/r=156 bin,
10.88% local deviation, local_snr 0.2584/0.2865 at cpl=20), R31-gated by
a fresh same-session control, Check C recalibrated per R30, Check B
normalized per the CPL_RATIO finding. Five blind Phase-2 critiques
(PHOTONICS, MATERIALS, EM, THERMODYNAMICS, QUANTUM), all
support-with-changes, zero opposition, each finding a distinct defect --
PHOTONICS: box_a clearance in wavelengths is 3.2lambda at r=156 but
6.4lambda at r=312, undisclosed; MATERIALS: the sponge-margin figure
compared against the wrong operand (floor scale, not signal/|delta|);
EM: the PEC-zeroing masked write makes peccored scenes ~14% costlier per
step, biasing the R31 control anti-conservatively; THERMODYNAMICS: a
1000-step burst on r=156's small grid may not represent sustained r=312
throughput; QUANTUM OPTICS (most consequential): an earlier draft's
Check-C direction silently inverted the ORIGINAL neighbor_correlation_
check premise (HIGH correlation = real structure), never validated at
the new geometry. Red Team's Phase-2 audit combined all five into a
5-item mandatory-fix docket, verdict PROCEED-WITH-MANDATORY-FIXES, ruled
Check C should ship undirected pending a same-geometry cross-tabulation,
proposed new standing rule R32 (a recalibrated statistic's direction, not
just its threshold, needs independent validation at the geometry under
test). Phase 3: all five fixes applied (box_a wavelength disclosure;
three-figure sponge-margin comparators; corrected false
materials-invariant-cost claim + commensurable 3-scene-blend control;
short+sustained control gated on the lower speed_ratio; undirected Check
C with a post-Phase-4 resolved-vs-unresolved cross-tabulation), R32
ratified, predictions committed before Phase 4. **Phase 4: the R31
control fired for real, for the first time, and correctly REFUSED the
r=312 spend** -- this session ran at ~0.406x the historical (Iteration
89) session's own speed (genuinely SLOWER, opposite direction from that
session's own ~2.19x-faster finding); the R31-scaled cost projection
(16737.4s) exceeds the 10800s bound, where the naive cross-session
projection (6802.6s, matching Iteration 89's own briefed figure) would
have wrongly APPROVED. Zero r=312 Sim.run() calls occurred; the
named-bin question remains untested, deferred a third time (exp-111:
sequencing; exp-112: cost/density choice; exp-113: a real, R31-scaled
refusal). Persisted as a genuine result (not a silent no-op) via
analyze113.py's own gate-refused branch. Six blind Phase-5 reviews, all
CONFIRM or CONFIRM-WITH-GAPS, zero substantive disagreement, every
headline figure re-verified from primitives: PHOTONICS (re-ran the FULL
trust suite, 43/43) found NOTES.md's own Setup section still described
"3 real FDTD calls this cycle...r=312" as accomplished fact (Director's
own oversight) but incorrectly claimed the 41/41 figure was stale
relative to 43/43 (VISION's own review had already correctly reconciled
these as two legitimately different invocations -- Red Team confirmed
VISION, not PHOTONICS). MATERIALS confirmed Fix 2 landed correctly,
proposed a cheaper intermediate-r (r=234) calibration point. EM confirmed
all R31 arithmetic bit-exact, found the literal production-dispatch path
was never actually executed this cycle (a commit-message-vs-review-body
discrepancy, not an experiment defect) -- closed by Red Team itself,
same-shift. THERMODYNAMICS ruled out fixed per-scene overhead as an
alternative explanation for the sustained-vs-short gap -- positive
evidence for genuine sustained-load degradation; flagged whether
COST_GATE_TOTAL_S should be a fixed wall-clock bound given ~5x
session-to-session throughput swings now demonstrated across two
consecutive cycles. QUANTUM OPTICS tested Fix 5b with eight synthetic
constructions (core logic correct) and found a new composition gap:
direction_validated conflates three distinct future states into one
False; check_a's own text goes stale the moment a future crosstab runs.
VISION SCIENCE (self-review) confirmed R23 discipline holds in the
gate-refused branch; found Fix 3b/4 closes only the control's duration
half, not its grid-size half. Red Team's Phase-5 final audit independently
re-derived every figure, corrected PHOTONICS' own 41-vs-43 finding as
wrong (vindicating VISION), closed the production-dispatch-path gap
itself, applied two same-shift fixes (NOTES.md's stale Setup claim
corrected; QUANTUM's direction_validated/check_a composition gap
completed in code -- a new high_direction_validated field, an explicit
named_bin_evidentiary_reading conjunction field, a non-stale check_a
text, a length assertion), verified against 13 synthetic constructions
and byte-identical results.json reproduction. Ruled zero Checkpoint
criteria fire -- criterion 5 does not fire and should not be conflated
with "two consecutive PARTIAL labels": this cycle produced a fourth new
standing rule (R32), five permanently-fixed Phase-2 defects, and the
first real-data confirmation that R31 can actually prevent an overspend.
Declined to mint new standing rules for the COST_GATE_TOTAL_S policy
question (queued as new Tier-0 item 0d) or VISION's R23-forward-risk
(named as a watched risk, zero founding instance). Combined Verdict:
PARTIAL -- BLOCKED BY COST GATE (Red Team confirmed) -- not RULED OUT (T1
correctly N/A throughout), real progress nonetheless: R31's own necessity
now empirically demonstrated, not merely reasoned about; all five
Phase-2 findings permanently fixed in code; R32 ratified with its own
composition gap closed rather than merely disclosed. Zero Checkpoint
criteria fire. Reconciled Iteration-91 queue: Tier 1 -- re-attempt the
+168.75deg/r=312/cpl=25 leg with an upgraded R31 control (repeat the
sustained reading once for reproducibility; add a same-session timing
point genuinely on the r=312 grid itself, closing the grid-size
confound); execute the crosstab immediately the moment real data lands;
a cheaper intermediate-r (r=234) calibration point pursued in parallel,
immune to a fourth session-speed-driven deferral. Tier 0 -- rule on the
Iteration-85 Checkpoint-4/R24 firing (unchanged, still pending -- SIX
cycles now); ratify or reject the R23 First Addendum; ratify or reject
R30/R31/R32; (0d, new) should COST_GATE_TOTAL_S cap wall-clock time or
actual compute/energy cost -- a genuine policy fork, not a discovered
defect. Tier 2/3 -- unchanged (see LOGBOOK.md Iteration 89 for full
text). Full record: `experiments/113-t28-r312-cpl25-plus168-bin/`,
LOGBOOK.md Iteration 90. Next: panel Iteration 89 done (exp-112, PARTIAL,
QUANTUM OPTICS' rotation-lead cycle: executed the Reconciled Iteration-89
queue's headline Tier-1 item -- PHOTONICS' own cpl-refinement floor
spot-check, deferred twice, executed for the first time: cpl=20->25
(1.25x) congruent grid-resolution refinement of the fixedabs family,
r=156 alone, targeting bin index 4 (-146.25deg, margin=32),
UNRESOLVED-BY-CONSTRUCTION at cpl=20 despite a 9.88% local deviation.
Five blind Phase-2 critiques (PHOTONICS, MATERIALS, EM, THERMODYNAMICS,
VISION), all support-with-changes, zero opposition, each finding a
distinct defect -- PHOTONICS: no bin-neighborhood correlation check;
MATERIALS/EM (independently convergent): the ABSORB/EDGE sponge scaling
is NOT resolution-invariant the way tau_shell/sigma_max is;
THERMODYNAMICS: the Phase-4 pipeline as shipped could not run at all (a
run/run module-import-cache collision, confirmed by direct execution,
crashing before any Sim.run() call); VISION: "detection floor" never
disambiguated from a human perceptual threshold. Red Team's Phase-2
audit combined all five into a 6-item mandatory-fix docket, verdict
PROCEED-WITH-MANDATORY-FIXES, recommended new standing rule R29
(same-basename-module import-cache collisions). Phase 3: all six fixes
applied (module renamed run112.py with executed identity assertions;
ABSORB/EDGE non-invariance disclosed with computed numbers; new Check C
neighbor-correlation gate added; DISCLAIMER clause disambiguating
"detection floor"; sigma_abs/sigma_ext persistence), R29 ratified,
predictions committed before Phase 4. Phase 4: 3 real FDTD calls, 670.5s
total (well under the 1469.19s projection). A SECOND, previously-
undiscoverable instance of the identical R29 collision surfaced here
(analyze.py's own chunk_runner import), fixed identically, flagged for
Phase 5 to adjudicate. Result: Check A (mirror-pooled floor) AMBIGUOUS
(local_snr improved but stayed well below the K=1 bar); Check B (T28's
founding R3 standard) SURVIVES; Check C corr=0.9994, clears its own bar
-- but since Check A never reached SURVIVES, "candidate real structure"
was correctly NOT claimed per the pre-registered DISCLAIMER. Both R23
asserts confirmed firing on real execution. Six blind Phase-5 reviews
independently re-verified every figure and surfaced two new, convergent
findings: PHOTONICS and QUANTUM (self-review), by different methods,
found Check C has ZERO discriminating power (48/48 bins clear its own
bar; the UNRESOLVED population's own mean correlation exceeds the
RESOLVED population's) -- PHOTONICS traced the mechanism to an
un-normalized 1.25x raw-magnitude artifact in lab/sections.py's own
_face_flux(). MATERIALS found the DISCLAIMER's own "6-8 orders of
magnitude below the floor" claim does not survive re-derivation (true
margin ~1.8-4.5 orders, a ~100-1000x overstatement, non-outcome-
reversing). ELECTROMAGNETISM found the sigma_ext~=sigma_abs+sigma_scat
cross-check is a code-level tautology; the genuinely independent
sigma_ext_cross had been silently dropped from the persisted ledger.
THERMODYNAMICS' own headline finding: real wall time (670.5s) came in at
less than half the ratio^3 projection (1469.19s) -- re-invoking the real
cost gate with the actual pilot FLIPS the r=312-expansion decision from
REFUSED to APPROVED (37% margin), traced to a ~2.19x cross-session
compute-speed confound. Four of six seats explicitly ruled the second
R29 instance does NOT fire Checkpoint 4. Red Team's Phase-5 final audit
independently re-derived all three tasked findings bit-exact, no
correction needed to their substance; ruled definitively the second R29
instance does NOT fire (six-of-six unanimous), ratified a textual
addendum scoping R29's forward clause to a future cycle's own reuse;
ratified two new standing rules (R30 -- an adopted, uncalibrated
discriminating-instrument threshold must be checked against its own
computable null population before evidentiary language is used; R31 --
a cross-session wall-time cost projection needs a same-session control
point), neither firing on its founding instance. Zero Checkpoint
criteria fire; R20's density tally sits at 1-2, a fifth consecutive
cycle at this near-miss level, named as a standing observation. Same-
shift fixes applied and verified by re-execution (sigma_ext_cross
restored; corrective DISCLAIMER comment; three attributed NOTES.md
corrections). Trust suite green throughout (43/43), zero lab/ diff.
Combined Verdict: PARTIAL -- continues this exact T28 sub-thread's own
unbroken pattern since Iteration 82 -- but real progress: the first
genuinely new FDTD data this long-deferred spot-check has ever produced,
tau_shell-invariance independently confirmed to hold in real data
(<0.01%), both module-collision defects genuinely fixed, R23 compliance
genuinely clean, and the cost-gate re-invocation hands Iteration 90 a
concretely unblocked, affordable next step (the +168.75deg bin at
r=312) that did not exist before this cycle ran. Reconciled Iteration-90
queue: Tier 0 -- rule on the Iteration-85 Checkpoint-4/R24 firing
(unchanged, still Marsh's own call, still pending -- FIVE cycles now);
ratify or reject the R23 First Addendum; ratify or reject R30/R31. Tier
1 -- execute the +168.75deg bin at r=312/cpl=25 (the cost gate now
clears it, needing its own fresh same-session pilot per R31); recalibrate
Check C's own bar per R30; diagnose/normalize the CPL_RATIO raw-
magnitude confound in lab/sections.py::_face_flux(). Tier 2/3 --
unchanged (see LOGBOOK.md Iteration 89 for full text). Full record:
`experiments/112-t28-cpl25-floor-spot-check/`, LOGBOOK.md Iteration 89.
Next: panel Iteration 88 done (exp-111, PARTIAL,
THERMODYNAMICS' rotation-lead cycle: executed Reconciled Iteration-88
Tier-1 items 1/2/4 (fault-injection control for mirror_pooled_floor/
classify_item_i_local; repositioning the R27/R28 cost gate genuinely
upstream into chunk_runner.py; recalibrating cost_gate_check()'s
projection formula with an empirically re-derived exponent, 3.2053, plus
a 10% safety margin), all zero new FDTD, and explicitly deferred item 3
(PHOTONICS' cpl-refinement floor spot-check, genuine new FDTD) a second
time, reasoned (sequencing + predicted cost + density risk). Five blind
Phase-2 critiques (PHOTONICS, MATERIALS, EM, QUANTUM, VISION), all
support-with-changes, zero opposition, each finding a distinct defect --
PHOTONICS: the fault-injection triad tests only idealized mirror-parity
extremes; MATERIALS: an R4-shaped hand-typed arithmetic slip in the
item-3 deferral cost table; EM: the gate-reposition control's probative
value depended on binding to the REAL chunk_runner module (R28's own
founding shape recurring one layer deeper if unbound), plus a guard-
ordering gap; QUANTUM: local_snr_peccored/hollow would still leak inf at
the floor==0 case even post-fix; VISION: zero R23/DISCLAIMER machinery
referenced despite three new claims this cycle introduces. Red Team's
Phase-2 audit adopted all five into 7 mandatory fixes, verdict PROCEED-
WITH-MANDATORY-FIXES. Predictions committed to git in the same commit as
all 7 fixes' code (nothing executed for real before that commit). Phase
4: zero new FDTD, zero lab/ diff, trust suite green throughout (41/41).
Item 1: FI-A/B/C PASS exactly, non-regression against all 12 real
committed cells PASS. FI-D (informational, added per Red Team's own
mandatory fix 6) FAILED its own "never exactly zero" sub-claim at swept
phases 0/180deg -- disclosed and explained (BIN_CENTERS_DEG's own mirror-
antisymmetry collapses the perturbation to common-mode at those two
phases, the same mechanism FI-B already demonstrates, not a new
pathology). Item 2: all 5 gate-reposition cases PASS. Item 4: all 3
formula-recalibration cases PASS exactly. Item 3: deferred, cost table
regenerated confirming MATERIALS' found slip (7.21h, not 6.5h). All six
blind Phase-5 reviews (PHOTONICS, MATERIALS, EM, QUANTUM, VISION,
THERMODYNAMICS self-review) independently landed CONFIRM-WITH-GAPS --
four of six (MATERIALS, PHOTONICS, VISION, THERMODYNAMICS) converged,
blind, on the same root defect: NOTES.md's own disposition table falsely
claimed BOTH R23 text-builder functions carried a working assert
DISCLAIMER_88, when only the predictions half did. VISION additionally
found the Result section's own "verbatim quote" claim was false (a hand-
edited rewrite). EM independently found gate_reposition_control.py tests
only the fresh-build branch, never the checkpoint-resume branch where 5
of 6 real Sim.run() calls per r=312 scene actually occur -- and itself
constructed/executed the missing case, confirming the underlying causal
property genuinely holds there too. QUANTUM found the floor<=0.0 guard
is not floating-point-robust (adversarial construction: floor~5.85e-18,
floor_degenerate=False, local_snr~1e14), and that NOTES.md's own
"exactly 0.0 at 180deg" claim is itself false (~1.95e-18). THERMODYNAMICS'
own self-review derived the closed form governing FI-D's collapse and
showed it is P*-independent, a generic property of any cosine on this
mirror-symmetric grid, not the T28-specific regime NOTES.md's own framing
implied. Red Team's Phase-5 final audit independently re-verified all
five findings from primitives (two understated by their own finders),
ratified a new standing rule (R23 First Addendum -- a disclaimer string's
own assert-symmetry does not transfer to a later cycle's successor
string; does not fire on this consolidating instance, third instance
auto-fires Checkpoint 4), classified the remaining findings as fresh
instances of R4 (x2, R20 tally 2 of 3, does not fire, a fourth
consecutive cycle at this exact tally), R13, and R18 (none firing,
matching established non-escalating precedent for each). Ten same-shift
fixes applied directly (predictions_result_88.py's builders now assert
internally; new finalize_88.py makes results.json's text fields
genuinely reproducible from committed code alone, verified passing;
NOTES.md annotated throughout). Trust suite reconfirmed green (41/41).
Combined Verdict: PARTIAL -- not RULED OUT (T1 correctly N/A throughout),
not PROMISING (a real, disclosed, seven-ways-confirmed gap cluster
survives freeze, matching this exact T28 sub-thread's own established
pattern since Iteration 82). Zero Checkpoint criteria fire this cycle --
the Iteration-85 Checkpoint-4/R24 firing remains open, unchanged, still
pending Marsh's own ruling. Reconciled Iteration-89 queue: Tier 0 --
rule on the Iteration-85 Checkpoint-4 firing (unchanged); ratify or
reject the new R23 First Addendum. Tier 1 -- a sixth gate_reposition_
control.py case exercising the checkpoint-resume branch directly; harden
classify_item_i_local's own floor<=0.0 test to an amplitude/epsilon-scaled
magnitude floor gate (R13 discipline); a genuinely non-sinusoidal/multi-
harmonic FI-D successor; execute item 3 (PHOTONICS' cpl-refinement floor
check), cpl=25/r=156-alone-first, deferred twice now, not a third time
without new reasoning; the R2_SMOOTH_THRESHOLD=0.90 re-derivation (fifth
consecutive cycle); MATERIALS' own fabrication-tolerance bound (fourth
consecutive cycle). Tier 2/3 -- unchanged (see LOGBOOK.md Iteration 88
for full text). Full record: `experiments/111-t28-cost-gate-reposition-
and-floor-fault-injection/`, LOGBOOK.md Iteration 88. Next: panel
Iteration 87 done (exp-110, PARTIAL,
ELECTROMAGNETISM's rotation-lead cycle: independently proved the
Iteration-86 queue's own "zero new FDTD, all data already committed"
premise for item i's local-magnitude renormalization false -- the
per-bin angular-pattern arrays lived only in a now-defunct prior
session's ephemeral scratchpad, never persisted -- and corrected it
with a minimal, bit-identical 6-call re-capture (empty/hollow/peccored
x r=156/312) whose sole new purpose is permanent per-bin persistence
(36 arrays, 1728 floats, now committed to git). Bundled with the two
genuinely zero-FDTD Tier-1 items: a synthetic fault-injection control
for linear_fit_1_over_margin's own smooth/noise discriminator (R18),
and stage26's symmetric truncation-direction negative control. Five
blind Phase-2 critiques (PHOTONICS, MATERIALS, THERMODYNAMICS, QUANTUM,
VISION), all support-with-changes, zero opposition: PHOTONICS and
QUANTUM independently attacked the proposed mirror-symmetry noise
floor from two angles (common-mode blindness; correlated-not-
independent variance) -- Red Team ruled these two distinct root
causes, adopted both remedies; MATERIALS found the "discharges R13 and
R14" claim false (multi-lobed curves can't clear a literal R14
smoothness check); THERMODYNAMICS found COST_GATE_PILOT_S/
COST_GATE_TOTAL_S defined but never enforced in code; VISION found
zero R23/DISCLAIMER machinery anywhere in the proposal, naming
exp-107's own identical silence as this sub-thread's one prior R23
regression precedent. Red Team's Phase-2 audit combined all five into
8 mandatory fixes, one partial override, verdict PROCEED-WITH-
MANDATORY-FIXES. Predictions committed to git before any Phase-4
Sim.run() call, all 8 fixes already implemented in that same commit.
Phase 4: 6 real FDTD calls, 7690.4s (128.17 min) wall -- the r=312 leg
cleared the newly-code-enforced R27 cost gate (pilot 752.2s vs 5400s
bound; projected total 6017.8s vs 10800s bound) and executed in full.
Gate P0/reproduction_precondition PASS exact both r (rel_dev=0.0).
classify_item_i verdict CONFIRM both r, unchanged. Item 1c/1d
(informational): neither of the two low-power bins PHOTONICS' own
Iteration-85 self-review flagged (~10% local deviation under the old
global-blind computation) clears the new K=3 mirror-pooled floor --
both UNRESOLVED-BY-CONSTRUCTION. Item 2: all four synthetic triples
reproduced bit-exact. Item 3: rel_diff_truncated=1.999, inside the
predicted band. R23 fully honored: both DISCLAIMER asserts passed,
both text fields persisted and quoted verbatim. Trust suite green
throughout (41/41). All six blind Phase-5 reviews (PHOTONICS,
MATERIALS, EM self-review, THERMODYNAMICS, QUANTUM, VISION)
independently landed CONFIRM-WITH-GAPS -- unanimous six-of-six
departure from the Director's own initial PROMISING, zero factual/
arithmetic defect found anywhere, but five distinct NEW gaps
surfaced, none raised at Phase 2 including by Red Team's own Phase-2
audit: QUANTUM found classify_item_i_local's resolved mask lacks a
floor==0 guard (non-firing on real data); PHOTONICS found the Result
section understates how decisively both named bins sit below even a
K=1 floor across all six margins; THERMODYNAMICS found the R27 cost
gate sits downstream of 90.2% of this cycle's own wall-clock spend --
structurally incapable of aborting the leg its own comment claims it
guards, missed by six review layers; EM's own self-review found
cost_gate_check()'s kappa_ratio**3 formula underestimates the real
r=312/r=156 wall-time ratio by ~15%; MATERIALS found R27's own
founding-instance narrative false -- exp-105/106/107 all had real,
executing, upstream cost-gate conditionals, only exp-108 actually left
it unenforced, not "exp-105 through exp-108 (four-plus cycles)" as
THERMODYNAMICS' own Phase-2 critique and Red Team's own Phase-2 audit
(twice) claimed without opening those files' own source. Red Team's
Phase-5 final audit independently re-verified the two most
consequential findings from primitives (traced the actual call chain
itself for THERMODYNAMICS' finding, confirming 90.2% exactly; read
exp-105/106/107's own run.py itself for MATERIALS' finding, confirming
it exactly), adopted all six reviews in full, ruled VISION's logic-
direction finding correct (the Interpretation prose applied the mirror
floor's common-mode-blindness mechanism backward -- an underestimated
floor risks false RESOLVED, not false UNRESOLVED), checked all five
findings element-by-element against R1-R27 -- none fires -- and
ratified two new standing rules: R28 (a cost gate satisfying R27 must
also sit causally upstream of the spend it controls, independently
traced; founding instance exp-110's own cost_gate_check(), does not
fire) and the R4 Third Addendum (a Phase-2 Red Team audit's own multi-
cycle claims must be independently verified per-named-cycle before
being trusted forward; second instance of the pattern Iteration 82
flagged as "a pattern to watch," discharged into a rule; does not fire
on its own consolidating instance). Nine same-shift annotations
applied directly to NOTES.md and the frozen Phase-2 documents
(blockquoted/struck-and-corrected, zero re-run, zero verdict-
arithmetic change): R27's founding-instance narrative corrected to
exp-108 alone; R27's forward clause and label brought into line with
registry convention; the Interpretation paragraph's backward hedge
corrected; the causal-positioning and formula-bias gaps disclosed; the
floor==0 gap disclosed; the margin-independence/bimodal finding stated
explicitly; Combined Verdict corrected PROMISING -> PARTIAL;
phase2_critique_thermodynamics.md and phase2_redteam_audit.md flagged
with a pointer to the correction. Combined Verdict (LOGBOOK-level):
PARTIAL -- not RULED OUT (T1 correctly N/A throughout), not PROMISING
(a real, disclosed gap cluster survives freeze, none individually
fatal, matching this exact sub-thread's own established pattern since
Iteration 82); real, disclosed, seven-ways-reproduced progress
nonetheless -- the data-persistence gap genuinely, permanently closed;
R23 honored byte-exact; all 8 mandatory fixes genuinely implemented.
Zero Checkpoint criteria fire this cycle -- the Iteration-85
Checkpoint-4/R24 firing remains open, unchanged, still pending Marsh's
own ruling. Reconciled Iteration-88 queue: Tier 0 -- rule on the
Iteration-85 Checkpoint-4 firing at the next convened checkpoint
(unchanged); the R27/R28/R4-Third-Addendum corrections are already
applied, this shift. Tier 1 (named in every one of six Phase-5
reviews' own top-3) -- execute the queued fault-injection control for
mirror_pooled_floor/classify_item_i_local, both sub-cases (asymmetric
+ symmetric/common-mode, including QUANTUM's own floor==0 degenerate
case), zero new FDTD; reposition the R27/R28 cost gate genuinely
upstream (chunk_runner.py itself calls cost_gate_check() before
r=312's first Sim.run(), using r=156's already-logged wall times),
zero new FDTD; PHOTONICS' own independent non-differencing floor check
(cpl-refinement) at the two named bins, genuine new FDTD; apply an
empirical safety margin (or the measured ~3.2 exponent) to the cost
gate's own projection formula. Tier 2 -- the long-outstanding
R2_SMOOTH_THRESHOLD=0.90 re-derivation; MATERIALS' own fabrication-
tolerance quantitative bound, now a third consecutive cycle naming it
undone; a full per-margin Result-section table for item 1c/1d;
CLOSURE_CONFIRM/CLOSURE_FALSIFY dead-code cleanup; a fourth r-point
(r=624). Tier 3 -- unchanged: the oblique-angle extension; the
750/450nm leg; the G40 full-width leg; the x-wall admittance refit;
PAD-with-article survival; box_dev's own thinning margin (~9.0x at
r=312, still unresolved). Full record: `experiments/110-t28-item-i-
local-norm-and-controls/`, LOGBOOK.md Iteration 87. Next: panel
Iteration 86 done (exp-109, PARTIAL,
MATERIALS' rotation-lead cycle: executed exactly the four Tier-0
UNBLOCKED items from exp-108's own Reconciled Iteration-86 queue -- gate
classify_item_ii() on fit["smooth"] (the R24 second-instance fix that
fired Iteration 85's own Checkpoint criterion 4); wire build_result_text()
into an executed path; restore both founding assert DISCLAIMER calls;
persist predictions_text/result_text into a new results.json. Tier-0
item 0 (ruling on the Iteration-85 Checkpoint-4 firing itself) is Marsh's
call, explicitly out of scope, still pending -- unblocked-threads-continue
per PANEL.md's own continuous-mode protocol. Five blind Phase-2 critiques
(PHOTONICS, EM, THERMODYNAMICS, QUANTUM, VISION), all support-with-changes,
zero opposition: PHOTONICS found the proposal's own rejection of a
forced-AMBIGUOUS alternative rested on a misdescribed sibling-code analogy
(classify_item_i's CONFIRM branch never reaches the fit/smoothness code
path at all); EM found "raw std is more conservative in every case" false
as stated (conservative against false CONFIRM, liberal against false
REFUTE); THERMODYNAMICS found an undisclosed AND-reduction rule and a
wall-time-attribution gap; QUANTUM found the raw/residual ratio
(1.729x/1.010x) should be persisted and narrated; VISION found R23's own
human-readable-citation half left unbound. Red Team's Phase-2 audit
independently re-derived every figure from primitives and adopted all
five into six mandatory fixes (one explicit, disclosed override: declined
to mandate an R2_SMOOTH_THRESHOLD re-derivation this cycle). Verdict
PROCEED-WITH-MANDATORY-FIXES. Predictions committed to git five minutes
before Phase 4's code was patched or run (git-blame-verified). Phase 4:
zero new Sim.run() calls, zero lab/ diff, trust suite green before and
after (41/41). classify_item_ii() patched to (r, fit, delta_values):
detrended residual_std when smooth, raw undetrended np.std otherwise (true
at both r=156/312, unchanged from exp-108). Every predicted outcome
reproduced exactly: CONFIRM/CONFIRM at both r, ratios matching to <1e-3
relative, both DISCLAIMER asserts live-fired for the first time on real
data and passed silently. All six blind Phase-5 reviews (PHOTONICS,
MATERIALS self-review, EM, THERMODYNAMICS, QUANTUM, VISION) independently
re-derived the core numeric chain -- unanimous on the fix's correctness --
but three of six (PHOTONICS, MATERIALS, QUANTUM), independently and blind
to each other, found NOTES.md's own mandatory-fix-1 disposition promised a
correction "below (Sec 'Why raw std, not forced AMBIGUOUS')" that did not
exist anywhere in the frozen document; three of six (MATERIALS,
THERMODYNAMICS, EM) independently found the trust-suite citation
("41/41, 100s/102s") unevidenced by its own cited console record
(run_output.txt); EM independently found a cosmetic double-braced
f-string quotation slip in NOTES.md not matching the real single-braced
source; QUANTUM found a subtler R25-shaped gap (a declined re-derivation
folded into a different item's subordinate clause rather than its own
queue line). VISION alone returned clean CONFIRM: byte-for-byte diff of
results.json's two text fields against NOTES.md's own quoted blocks --
exact match, DISCLAIMER confirmed present verbatim, twice -- genuinely
closing VISION's own three-cycle-old exp-108 finding for the first time.
Red Team's Phase-5 final audit independently re-verified every finding
from primitives, adopted all six reviews, and overrode one factual error
(PHOTONICS' claim that NOTES.md was committed only once, bundled with
Phase 4's results -- git blame/log show its Predictions content was
committed five minutes before Phase 4's execution, at a separate commit,
byte-exact diff boundary at the Result placeholder -- house discipline
was honored). Ruled the missing-section defect a genuinely new failure
shape and adopted a new standing rule, R26 (a Phase-3 document's own
named forward cross-reference must resolve to real content before
freeze) -- founding instance, does not fire. The trust-suite-citation gap
ruled R4-lineage, non-firing (R20 tally 2, short of three, the second
consecutive cycle in this lineage to land exactly one short). QUANTUM's
R25-shaped concern ruled non-firing (a calibration task, not a code-level
fix; founding instance of this sub-concern). Six same-shift annotations
applied directly to NOTES.md (blockquoted, zero re-run, zero
verdict-arithmetic change): the missing section written in, the brace
quotation corrected, the trust-suite citation gap disclosed, the Combined
Verdict corrected CONFIRM -> CONFIRM-WITH-GAPS, a docstring comment added
to reclassify_108.py, the folded Tier-2 item queued for a future split.
Combined Verdict (LOGBOOK-level): PARTIAL -- not RULED OUT, not
PROMISING (real, disclosed, non-outcome-reversing completeness gaps
remain); the substantive result stands unreversed, seven-ways
independently verified. Zero Checkpoint criteria fire this cycle -- the
Iteration-85 Checkpoint-4 firing whose root cause this cycle was built to
close remains open, unchanged, still pending Marsh's own ruling. Reconciled
Iteration-87 queue: Tier 0 -- rule on the Iteration-85 Checkpoint-4 firing
at the next convened checkpoint (unchanged). Tier 1 -- re-normalize (or
floor-gate) item i's per-bin comparison against each bin's own LOCAL
magnitude (still the single highest-value item); a synthetic
positive/negative control for linear_fit_1_over_margin's own smooth/noise
discriminator, now doubly motivated (discharges the R18 gap on both
classify_item_ii()'s new branch and analyze.py's companion call site);
extend stage26's negative control to the symmetric truncation direction.
Tier 2 -- split into two lines: formalize the absolute-floor six-margin
family from a resolution/aliasing bound; re-derive R2_SMOOTH_THRESHOLD=
0.90 for item ii's own question specifically, now its own line; a fourth
r-point (r=624), checked against BOTH bars per this cycle's own fix-2
finding; MATERIALS' own fabrication-tolerance framing for item i's
CONFIRM. Tier 3 -- unchanged: the oblique-angle extension; the 750/450nm
leg; the G40 full-width leg; the x-wall admittance refit; PAD-with-article
survival; box_dev's own thinning margin (~9.0x at r=312, still
unresolved). Full record: `experiments/109-t28-item-ii-smooth-gate-r23-
completion/`, LOGBOOK.md Iteration 86. Next: panel Iteration 85 done
(exp-108, PARTIAL --
revised by Red Team's own Phase-5 final audit from the Director's initial
PROMISING, CHECKPOINT CRITERION 4 FIRES (notification, not a pause; Marsh
notified), PHOTONICS' rotation-lead cycle: executed exp-107's own
Reconciled Iteration-85 queue in full -- all three Tier-0 governance items
(execute exp-106's own two-cycle-old run.py reclassification code fix,
R25's own load-bearing tripwire; ratify R25 itself, bookkeeping; force the
three-cycle-stale R23 scope decision) and all four Tier-1 items, bundled
at the cost of one FDTD spend: angular_scattered_pattern on the
hollow-vs-PEC-cored fixed-abs pair (first application to this family at
r!=78); an absolute box-ledger noise-floor characterization (T11's
80-cycle-old open question); the numerator floor-gate check on the actual
PEC-cored PRIMARY article (closing exp-107's own hollow-substitute
disclosure); promoting chunk_runner.py's checkpoint/resume mechanism to a
named, suite-gated trust-suite stage (stage26_chunked_run_identity). Five
blind Phase-2 critiques (MATERIALS, EM, THERMODYNAMICS, QUANTUM, VISION),
all support-with-changes: EM and QUANTUM independently found the same
root-cause defect from two angles (box radius treated as an exchangeable
nuisance parameter for two quantities that do not carry the scalar-flux
conservation guarantee stage 8's own box_a/box_b convention relies on);
Red Team's Phase-2 audit combined their remedies into one unified
multi-margin convergence/detrending fix, plus 5 more mandatory fixes.
Verdict PROCEED-WITH-MANDATORY-FIXES, 7 mandatory fixes, zero overrides.
Predictions committed to git BEFORE any Phase-4 call. Phase 4: 6 real new
FDTD captures (empty+hollow-article+PEC-cored-article, r=156/312), 128.5
min combined wall via chunk_runner.py's checkpoint/resume (extended to a
third scene type), zero lab/ diff beyond the disclosed stage26 addition,
trust suite green throughout (41/41 standard set, 2/2 on --only 26).
Tier-0 item 1: classify_shape_ratio_fixedabs() extracted as a standalone
function in exp-106's own run.py, wired into both the inline call site
and a new reclassify_106.py; corrected classification reads
THREE-WAY-AMBIGUOUS(...) exactly as predicted -- git-tracked,
independently-diffable evidence the fix was executed, not merely
described a third time. Gate P0 and the item-i reproduction precondition:
PASS exact both r. Item i (angular_scattered_pattern, unified fix):
CONFIRM at both r -- null generalizes to the angular domain, no
floor-cleared bin exceeds 5% relative deviation at any of 6 margins. Item
ii (absolute noise floor, detrended): CONFIRM at both r -- residual_std
sits 5.1x/5.9x inside the CONFIRM bar. Item iii (numerator floor-gate,
PEC-cored PRIMARY): PASS both r (0.1827/0.2525, within +/-0.05 of
exp-107's own hollow-article reading). Item iv (stage26): both controls
PASS. closure: CONFIRM all four cells. All six blind Phase-5 reviews
(PHOTONICS self-review, MATERIALS, EM, THERMODYNAMICS, QUANTUM, VISION)
independently reproduced every headline number from primitives -- a clean
six-of-six, zero overrides by Red Team's own final audit. THERMODYNAMICS:
clean CONFIRM. MATERIALS: CONFIRM-WITH-GAPS -- item i's CONFIRM is a
genuine fabrication-tolerance finding never translated into MATERIALS'
own charter language. EM and QUANTUM, independently and blind to one
another: classify_item_ii() never checks its own fit["smooth"]/r_squared
diagnostic before applying the detrended residual_std as "the genuine
floor" -- at r=312 the fit explains 2% of the variance (smooth=False at
BOTH r), the IDENTICAL diagnostic that DOES correctly gate item i's own
REFUTE branch, applied to one sibling classifier and not the other, in
code built together in the same Phase-3 synthesis. QUANTUM additionally
found item i's own "floor-cleared bin" filtering was never implemented.
PHOTONICS' own self-review found the deepest single defect: item i
normalizes each of 48 angular bins against the GLOBAL peak bin, not local
magnitude -- in a strongly forward-peaked pattern (62.5% of bins carry
<1% of peak power), this is structurally blind to real shape differences
in low-cross-section sectors, where locally-normalized deviations reach
9.88%/10.88% against a reported global-normalized max of 0.015%. VISION:
build_result_text() -- R23's own founding "RESULT_TEXT" half -- is
defined but never called anywhere, zero assert statements exist anywhere
in the cycle's code -- a regression below even exp-105's own single
missing assert -- while NOTES.md claims "genuinely R23-compliant,
live-fire-verified," true only for the predictions half. Red Team's
Phase-5 final audit independently re-verified every finding from
primitives (including a from-scratch re-derivation of PHOTONICS' own
62.5%/9.88%/10.88% figures, and a from-scratch re-implementation of the
A+B/margin fit by normal equations) and adopted all six reviews in full,
zero overrides. Ruled the EM/QUANTUM/PHOTONICS convergence as TWO
distinct root-cause defects: Defect A (item i's global-vs-local
normalization) is a spec-level design choice, correctly implemented
exactly as specified, closer to R17's own shape than R20/R24 -- does not
fire either tally. Defect B (item ii's ungated smoothness diagnostic) is
ruled a clean SECOND INSTANCE of R24 -- a Phase-2 mandatory fix's if/then
consequence, Phase-3-claimed "adopted in full," never wired into the
classification logic it was written to gate, its own trigger condition
met by the data at both r. R24's own forward-elevating clause fires
CHECKPOINT CRITERION 4 automatically -- the first Checkpoint-4 firing
since Iteration 68. R20 tally: 2 (short of "three or more," does not fire
independently). R21: declined to independently fire alongside R24 on the
identical code defect (this program's own "ruled once, not twice"
counting discipline). R23: VISION's finding is a genuinely new sub-shape,
correctly adopted, but R23 carries no forward-elevating clause. R25:
genuinely, robustly discharged -- git show confirms a real, git-tracked,
33-line-net diff extracting the function exactly as specified; a cold
re-run of reclassify_106.py reproduces the exact string NOTES.md quotes
inline; does not fire, unrelated to and undiminished by the R24 firing on
a different channel. Six same-shift annotations applied directly to
NOTES.md (blockquoted, attributed, zero re-run, zero verdict-arithmetic
change): Combined Verdict corrected PROMISING -> PARTIAL; item ii's
Result table annotated with the r_squared/smooth values; item i's Result
re-scoped explicitly to the dominant forward-scattering lobe; the R23
"live-fire-verified" claims annotated true for predictions only; the
"annotated, not overwritten" sentence corrected; PHOTONICS' own citation
corrected (exp-016/017, not exp-059/060). Combined Verdict: PARTIAL --
not RULED OUT (T1 correctly N/A throughout); not PROMISING (Checkpoint
criterion 4 fires, inside the very document built to demonstrate clean
post-R25 governance, on a different rule, on a different channel, in code
built the same cycle); real, disclosed progress nonetheless: R25's
founding instance is genuinely, verifiably discharged; items iii, iv, and
closure are clean, independently reproduced, with no gaps found by any of
seven reviewing layers; item i's CONFIRM for the dominant, power-carrying
part of the scattering pattern is genuine, not merely salvaged.
CHECKPOINT ruled a notification, not a pause (this program's unbroken
precedent) -- no engine physics implicated, zero lab/ diff beyond the
disclosed stage26 addition, physically-scored verdicts unaffected in
outcome; unblocked threads continue. Reconciled Iteration-86 queue (Red
Team's own tiered ranking): Tier 0 -- rule on this Checkpoint-4 firing at
the next convened checkpoint; wire build_result_text() into the executed
path, restore both founding assert DISCLAIMER calls, persist
predictions_text/result_text into results.json; gate classify_item_ii()
on fit["smooth"] (the R24 second-instance fix itself, zero new FDTD).
Tier 1 -- re-normalize (or floor-gate) item i's per-bin comparison
against each bin's own LOCAL magnitude, not the global peak (zero new
FDTD, all data already committed -- the single highest-value item on this
queue); a synthetic positive/negative control for linear_fit_1_over_
margin's own smooth/noise discriminator; extend stage26's negative
control to the symmetric truncation direction. Tier 2 -- a fourth
r-point (r=624) to test THERMODYNAMICS' own r^-1.16 fixed-abs projection
(~52.6x margin, just above the 50x box_dev floor); MATERIALS' own
recommended fabrication-tolerance framing for item i's CONFIRM, with Red
Team's own observer-angle caveat folded in; formalize the absolute-floor
six-margin family from a resolution/aliasing bound. Tier 3 -- the
oblique-angle extension (now doubly motivated); the 750/450nm leg; the
G40 full-width leg; the x-wall admittance refit; PAD-with-article
survival; box_dev's own thinning margin (~9.0x at r=312, still
unresolved). Full record: `experiments/108-t28-reclassification-angular-
pattern-batch/`, LOGBOOK.md Iteration 85, CHECKPOINT (Iteration 85,
2026-09-04, criterion 4). Next: panel Iteration 84 done (exp-107, PARTIAL,
VISION SCIENCE's rotation-lead cycle: executed exp-106's own Reconciled
Iteration-84 queue -- Tier 0 (delta_scene R3-vs-R4-vs-R5 governance
decision, eight consecutive deferrals) and Tier 1 items 1/3/4 (kappa_
window closeouts). VISION's own Phase-1 proposal designed a properly-
powered R5 census gated on a mandatory ground-truth-recovery check --
does NOT survive Phase 2. Five blind critiques (all support-with-
changes): QUANTUM found the census's own theta_anchor selection rule has
an EMPTY DOMAIN over the proposed grid (the four zero-crossings' own
exclusion zones merge into one continuous forbidden band); PHOTONICS
found the proposal's own central safety claim cites the wrong statistic
(5.25x-7.87x off); EM found the "ground-truth-recovery" gate is partly
self-fulfilling and not genuine ground truth; MATERIALS argued the
census isn't worth running regardless, citing its own exp-100
disposition memo's unconditional realizability ceiling. Red Team's
Phase-2 audit generalized QUANTUM's finding (the 1.4deg buffer is close
to half the signal's own period, tiling the entire angular axis with
exclusion zones) and recommended formal retirement over redesign,
adopted in full by the Director. Tier 0 discharged by written retirement
(Iteration-51 no-further-cycle precedent), scoped precisely (closes only
the resolution-family-attribution question, not T28's larger open
periodicity-origin question). Two Director cost corrections to the
Tier-1 bundle (Item 1 needed 4 new FDTD calls not 2; Item 4 folded into
Item 1 at zero additional cost). Predictions committed to git BEFORE any
Phase-4 call. Phase 4 included a genuine same-shift environment
diagnosis: this session's backgrounded/nohup process execution runs
sustained FDTD numpy work pathologically slowly (isolated A/B test
confirmed, not a lab/ engine defect -- trust suite green foreground in
104s); items 1/4 executed via sequential foreground Bash calls with
Sim-object checkpoint/resume pickling (chunk_runner.py) and finalize.py.
Gate P0: PASS exact both r. Item 3 (real ledger-measured P5 thermal row,
not placeholder): CONFIRMED, all four cells reproduce the pre-registered
table exactly; (fixedabs, r=312) at 117.5x margin clears the tightened
50x floor. Item 1: PASSES the falsification band at both r but not the
tighter T9-anchor band (~15-20x above the historical anchors, honest
partial); core_frac~1e-7 discharges Red Team's founding Attack 9 concern
at these higher R_CORE/R_COAT ratios. Item 4: FALSIFIED at r=156
(frac_unresolved=0.183, predicted clean) and worsens at r=312 (0.268) --
a genuinely new finding: kappa_window's ARTICLE-scene numerator (not
just the empty-scene denominator exp-106 tested) carries real
noise-floor contamination, increasing with r, disclosed as measured on
the hollow variant not the PEC-cored primary article. Same-shift
addendum: the checkpoint/resume mechanism EM/QUANTUM flagged as
unverified was empirically A/B-tested (r=156 replayed through the
chunked path vs. the original single-shot captures) -- bit-exact,
max|diff|=0.000e+00 on every field. 4 real FDTD calls, ~109.3 min wall,
trust suite green throughout, zero lab/ diff. Six blind Phase-5 reviews,
all CONFIRM-WITH-GAPS, zero disagreement on any load-bearing point:
PHOTONICS found the Result section blends two non-commensurable T9
anchors (real gap 19.0x/15.8x, not "~10x"); MATERIALS found box_dev's
own margin over the delta has thinned from T9's founding ~1221x to just
~9.0x at r=312, and named angular_scattered_pattern as the correctly-
targeted unused instrument; EM/QUANTUM independently flagged the
checkpoint/resume mechanism as unverified (closed same-shift, above);
THERMODYNAMICS found margin ~ r^-1.16 for fixed-abs (vs self-similar's
exact r^-1), projecting a hypothetical r=624 point at ~52.6x, just above
the 50x floor; VISION's own self-review owned its Phase-1 defects and
found, unprompted, zero DISCLAIMER code despite NOTES.md's own
Idealizations claiming R23 code-enforcement. Red Team's Phase-5 final
audit independently re-verified every flagged claim from primitives and
adopted all six reviews in full. New finding, traced to root cause: the
exp-106-code-fix carryover (wiring the reclassification trigger into
run.py, named "Iteration 84's job") was SILENTLY DROPPED -- but the root
cause is one cycle upstream: exp-106's own audit disclosed the fix only
in prose, never promoted it to its own numbered Reconciled-queue line
item, so exp-107 worked faithfully from an incomplete queue. New
standing rule R25 adopted (queue-item completeness): a code fix an audit
defers by "may not touch [file]" must become its own explicit queue line
item; founding instance, does not fire; a second instance fires
Checkpoint criterion 4 automatically. R20 tally=1 (short of 3+, does not
fire). R21: genuinely discharged. R23: a live, verified but non-load-
bearing compliance gap (zero DISCLAIMER code, but this cycle's document
family never invokes the pipeline R23 presupposes) -- founding instance
of a new scope question, does not fire; the standing Iteration-82 R23
scope decision must be forced at Iteration 85 (three cycles unresolved).
Checkpoint criterion 4 does NOT fire -- the closest non-firing call in
the R16/R21/R23/R24 silent-drop lineage's history, only because R25 is
being named for the first time. Combined Verdict: PARTIAL -- not RULED
OUT (T1 correctly N/A throughout), not PROMISING (pure governance/
instrumentation cycle by design), real disclosed progress on both
structurally independent halves weighed against a real governance-
process cost (a named code fix surviving an entire cycle untouched
because this program's own cross-cycle-memory mechanism failed to carry
it forward in trackable form). Reconciled Iteration-85 queue (Red Team's
own tiered ranking): Tier 0 -- execute exp-106's own two-cycle-old
run.py reclassification code fix (do not let it reach a third cycle
unexecuted); ratify or reject R25; force the three-cycle-stale R23 scope
decision. Tier 1 -- run angular_scattered_pattern on the hollow-vs-
PEC-cored fixed-abs pair at r=156/312; a genuine absolute noise-floor
characterization for sections.widths()'s own box-ledger channel (T9's
80-cycle-old caveat, now at 9.0x margin); check Item 4's numerator
finding on the actual PEC-cored PRIMARY article, not the hollow
substitute; promote chunk_runner.py's checkpoint/resume mechanism to a
named, suite-gated trust-suite stage. Tier 2 -- re-derive Item 1's own
confirms band for these specific ratios; restore Item 3's Q_ext-
invariance corroboration and the ledger closure identity into Result
prose; re-frame or re-test Item 4's "worsens with r" claim; decide
whether the constraint-3-immunity claim needs its own reopening
condition. Tier 3 -- the oblique-angle extension; the near-null-
exclusion refinement (three cycles deferred); standing T28 items
untouched (a fourth r-point; a different bridge-family geometry; the
750/450nm leg; the G40 full-width leg; the x-wall admittance refit;
PAD-with-article survival at other wavelengths). Full record:
`experiments/107-t28-delta-scene-r5-census-decision/`, LOGBOOK.md
Iteration 84). Next: panel Iteration 83 done (exp-106, PARTIAL,
QUANTUM OPTICS' rotation-lead cycle: executed exp-105's own Reconciled
Iteration-83 queue Tier 1 items 1-4 in full (Red Team's own final-audit
tiered ranking) -- floor-gated window_stats()'s own output and stopped
discarding r=312's raw channel data; ran a settling-independence leg on
kappa_window itself (not merely its sibling kappa_region_point) at
r=156/312; built p3_trusted/shape_ratio_fixedabs_trusted, risk-
propagation gates symmetric in kind to exp-105's own p4_156_trusted; and,
for the first time on this channel, re-ran the bridge on exp-052's
fixed-absolute-thickness graded_black_shell control at r=156/312 --
MATERIALS' own newly-identified discriminator between the geometric z/z_R
window hypothesis and a growing-electrical-thickness alternative. Five
blind Phase-2 critiques, all support-with-changes; Red Team's Phase-2
audit adopted all five in full, one MAJOR partial override of MATERIALS'
own stale realizability claim, verdict PROCEED-WITH-MANDATORY-FIXES.
Predictions committed to git BEFORE any Phase-4 call; 10 real FDTD calls
(of 12 scheduled if every leg committed), 18398.4s (306.64 min) wall,
zero lab/ diff, trust suite green throughout (41/41). Gate P0/
reproduction checks: exact PASS. Item 1 (floor-gate): clean at BOTH r
(frac_unresolved=0.0000 everywhere) -- falsifies the Phase-1 proposal's
own "possibly >10% unresolved at r=312" worry, in the reassuring
direction. Item 2 (settling on kappa_window itself): landslide PASS at
r=156 for both families; r=312 genuinely NOT RUN -- its own empty-scene
settling pilot alone (103.28 min) correctly exceeded the 90-min cost
gate, deferring the article calls. Item 3 (risk-propagation gates): both
FALSE exactly as predicted, structurally forced by nyquist_tier(312)=
MARGINAL -- confirmed (QUANTUM's Phase-5 finding, Red-Team-reverified)
that p3_trusted/shape_ratio_fixedabs_trusted can NEVER reach True at
r=312 under this bridge geometry, a structural ceiling, not a coin flip.
Item 4 (fixed-abs control, the cycle's own stated centerpiece):
shape_ratio_fixedabs=18.2283, REFUTE-band direction, explicitly
NOT-TRUSTED; PHOTONICS' own ungated abs_ratio cross-check clears its
factor-of-2 band at both r. Ledger sanity check: core_frac=0/box_dev
clean at every point, but the cross-family absorbed-power divergence
(12.31%/17.96%) exceeds mandatory fix 1's own pre-registered ~10%
reclassification trigger at both r. Five of six blind Phase-5 seats (EM,
MATERIALS, PHOTONICS, QUANTUM, THERMODYNAMICS), independently and blind
to one another, converged on the identical finding: that reclassification
rule was never wired into run.py's classification logic despite NOTES.md
claiming all 7 mandatory fixes "adopted in full." Red Team's Phase-5
final audit independently re-verified this from primitives, ruled R20
tally=0 (at most 1 under the most generous reading -- a
specification-vs-implementation gap is a different failure shape than
R20's own citation/figure-reproduction instances), ruled the Iteration-82
pre-freeze shield does NOT apply (this gap IS the frozen Result text
itself) yet Checkpoint criterion 4 still does NOT fire (the tally falls
short of "three or more," not a timing technicality; caught blind, same
cycle, before LOGBOOK). Same-shift fix applied directly to NOTES.md:
Item 4 reclassified THREE-WAY AMBIGUOUS (pure post-processing of
already-persisted results.json fields, zero re-run); run.py's own code
fix left for Iteration 84. New standing rule R24 ratified (a Phase-2
mandatory fix's own specified consequence, once claimed "adopted in
full," must be implemented as a binding classification/verdict element,
not left computed-but-unwired -- does not fire on its own founding
instance, fires Checkpoint 4 automatically on a second instance).
Combined Verdict: PARTIAL -- not RULED OUT (T1 correctly N/A throughout),
not PROMISING (the cycle's own stated hypothesis, that closing all four
exp-105 gaps would let P3's collapse finally be TRUSTED or REFUTED as
physics, is not achieved), but real self-correction: the risk-propagation
symmetry fix genuinely works, the floor gate genuinely falsifies its own
r=312 worry, and the fixed-abs control genuinely executes for the first
time on this channel. Reconciled Iteration-84 queue (Red Team's own
tiered ranking): Tier 0 -- execute or formally retire the delta_scene
R3-vs-R4 split (now SEVEN consecutive deferrals, no eighth silent
deferral permitted); Tier 1 -- exp-052's literal hollow-vs-PEC-cored
radial_absorbed_power delta test on the fixed-abs family (the only
instrument that can discharge Red Team's own founding Attack 9 concern);
complete the r=312 settling leg (still diagnostically valuable despite
the structural p3_trusted ceiling); a real non-placeholder P5 thermal row
for both families (zero marginal FDTD cost); an absolute noise-floor
check on kappa_window's own numerator, not merely the empty-scene
denominator PHOTONICS found is all item 1 currently tests. Tier 2 -- a
genuinely different bridge-family geometry (engineered so nyquist_margin
crosses 2.0, since no re-run of the CURRENT geometry can ever produce a
fully-TRUSTED r=312 reading); a fourth r-point; widen the R23 scope
decision; correct exp-105's own stale Tier-2 realizability-tag queue item
before it is executed. Full record: `experiments/106-t28-kappa-window-
floor-fixedabs-control/`, LOGBOOK.md Iteration 83). Next: panel Iteration
82 done (exp-105, PARTIAL,
THERMODYNAMICS' rotation-lead cycle: executed exp-104's own Reconciled
Iteration-82 queue Tier 1 item 1 (Red Team's consensus top pick) --
extended T8's r=78/156/312 near-field-to-witness-scale bridge
methodology (exp-030, Iteration 7) to the coherent point/region-
intensity channel (kappa_window/kappa_region_wide/kappa_region_point/
delta_phi, built exp-102, hardened exp-103/104) for the first time --
T8's own bridge had only ever been applied to the ambient Weber-contrast
instrument. r=78 fully reused (0 new FDTD calls); r=156 unconditionally
committed; r=312 cost-gated behind a timing pilot per T8's own
Iteration-7 cost-blowup precedent, came in well under threshold (31.13
min) so the full leg executed. THERMODYNAMICS sidecar invoked this cycle
(departure from exp-102/103/104's own N/A precedent). Five blind Phase-2
critiques, all support-with-changes -- three independently caught the
identical 10x arithmetic error in the Phase-1 proposal's own hand-typed
z_over_zr figures; Red Team's Phase-2 audit adopted all five in full,
raised 3 new attacks of its own, verdict PROCEED-WITH-MANDATORY-FIXES.
Predictions committed to git BEFORE any FDTD call (b8dc2d5); exactly 6
real FDTD calls, 64.72 min wall, zero lab/ diff, trust suite green
throughout (41/41). Gate P0/P1: PASS exact. Fresnel/Nyquist pre-check
landed exactly in its own predicted trust tiers before any r=312 call
ran. P2 (monotonicity): CONFIRMED. P3 (functional-form + shape
discriminator): SCORED -- the headline finding: shape_ratio=19.79 (vs
sqrt-law 2.00+/-0.3 and linear-law 4.00+/-0.5 bands), kappa_window
collapses ~20.7x then ~185x across r=78->156->312 -- accelerating, far
more extreme than T8's own already-REFUTED absorber finding (ratio
5.33) on the ambient channel. P4 (ripple generalization, gated):
FALSIFIED at all three r, TRUSTED at r=78/156 (a new point-channel
settling leg passed cleanly, this program's first-ever settling test on
that channel at any r); r=312 reduced-confidence (no settling leg
there). P5 (thermal sidecar): CONFIRMED -- UNDETECTABLE at all three r
(699.27x/349.80x/175.06x, monotonically declining as predicted). Six
blind Phase-5 reviews, all CONFIRM-WITH-GAPS (denser cluster than either
exp-102 or exp-104's own Phase-5 layer): PHOTONICS proved the bridge's
own forced geometry makes shape_ratio=2^n exactly, implying exponent
n~=4.31 -- roughly double the steepest diffraction-theory candidate,
the wrong direction for an apodized shell -- and found kappa_window
never floor-gated, r=312's raw data discarded, and a pre-registered
prediction (P3b) silently dropped before freeze. MATERIALS named a
genuine unconsidered alternative mechanism (growing electrical shell
thickness) with an already-built, unused discriminating control
(exp-052). ELECTROMAGNETISM found this cycle's single most consequential
code-level gap: P3 has no risk-propagation gate symmetric to P4's,
despite depending on the identical MARGINAL-tier r=312 capture. QUANTUM
independently reproduced every headline number and confirmed zero
non-classical content (T1 correctly N/A). VISION found a second,
code-level R23 disclaimer-erosion data point and proved P3's dramatic
collapse carries ~zero constraint-3 information (saturated, ΔC~=0.018).
THERMODYNAMICS' own self-review found a genuine defect in its own
Phase-1 proposal (a dominance-ratio citation that does not reproduce
from its own stated constants) AND that Red Team's own Phase-2 audit
repeated the identical wrong figures while claiming to have
independently re-checked them. Red Team's Phase-5 final audit adopted
all six reviews in full, zero overrides, found one new defect (Gate P1
never touches kappa_window_78, the actual anchor P2/P3 score against).
R20 tally: 0 (the dominance-ratio error is one root-cause defect in two
PRE-FREEZE documents, confirmed absent from NOTES.md's own frozen
Result/Learned by direct grep -- does not survive freeze, does not
count). Checkpoint criterion 4 does NOT fire (R20 unmet, T1 correctly
N/A, constraint-3 proactively scoped out with numbers, no unfalsifiable
claim standing unflagged). Eight mandatory same-shift fixes applied
(zero re-run, zero verdict change): dominance-ratio citation annotated
in both historical documents; P3b scored explicitly; shape_ratio=2^n/
n~=4.31 characterization added; r=312 confidence caveat added to P3
symmetric to P4's; Gate-P1-scope note added; constraint-3 scope-boundary
note added; R23's missing predictions_text assert restored in run.py.
Combined Verdict: PARTIAL -- real, logbook-advancing science (four of
five scored verdicts reproduce clean with wide margins), but the
cycle's own declared headline finding rests on zero floor-gating, no
symmetric risk-propagation gate, an unverified Gate-P1 anchor, and an
unconsidered alternative mechanism with an unused discriminating
control -- denser than either exp-102's or exp-104's own gap clusters.
Reconciled Iteration-83 queue (Red Team's own tiered ranking, real
4-of-6-seat convergence on Tier 1): Tier 1 -- floor-gate kappa_window
and stop discarding r=312 raw data (the load-bearing precondition for
trusting or refuting P3 as physics vs artifact); a settling-independence
leg on kappa_window itself, especially at r=312; a symmetric Nyquist/
settling gate on P3's own scored verdict; re-run the bridge on exp-052's
existing fixed-absolute-thickness control. Tier 2 -- a fourth r-point to
break the two-point fit degeneracy; a real measured sigma_ext(r) trend
replacing the Q_ext-invariance placeholder; splitting the blanket
UNOBTANIUM tag; pinning the kappa-to-C scope-boundary note as a standing
T13/T14 cross-reference. Tier 3 -- the oblique-angle extension; the
standing delta_scene R3-vs-R4 split, now SIX consecutive deferrals
(Iteration 83 is the point requiring explicit written re-justification
or execution, not a silent seventh deferral); the other two Reconciled
Iteration-82 Tier-1 items (R23's own scope decision, now sharpened by
this cycle's own second erosion data point; the near-null-exclusion
raw-bin-identity refinement); a narrower r=312 settling spot-check.
Full record: `experiments/105-t28-kappa-scale-bridge/`, LOGBOOK.md
Iteration 82). Next: panel Iteration 81 done (exp-104, PARTIAL,
ELECTROMAGNETISM's rotation-lead cycle: a prior same-numbered shift
BLOCKED before Phase 1 (tooling gap, no sub-agent-spawning primitive,
logged and pushed as commit 2ad0c6e, zero science attempted) before a
later shift with working tooling executed the full cycle. Executed
exp-103's own Reconciled Iteration-81 queue Tier 1 (Red Team's own top
ranking): a genuinely sub-Nyquist (2-cell pitch) standoff recheck of
exp-103's own degenerate-aliasing sampling defect -- samples that landed
at exactly the lambda/2=10-cell coherent-intensity fringe period, not
resolved against it. Byte-identical article/geometry to exp-103's
primary pair; a new zero-averaging point_intensity channel (ported from
exp-102) alongside the unchanged 11-cell box-average kappa_region_wide
channel, at 53 DENSE_X points split into 5 per-quintile FFT period
estimates with a signed sinc-based suppression-ratio cross-check and a
delta_phi co-variation proxy. Five blind Phase-2 critiques, all
support-with-changes, five distinct flip conditions; Red Team's Phase-2
audit adopted all five, raised 2 more attacks of its own (a P3
grid-quantization fix via per-quintile FFT; a P6 missing numeric
threshold), and ratified new standing house rule R23 (a disclaimer
required in multiple sections must be code-enforced via a single
source-of-truth string constant + assert -- the disclaimer-erosion
pattern's 8th recurrence, caught and fixed at Phase 1 itself).
Predictions committed to git BEFORE any FDTD call (db57beb); exactly 2
real FDTD calls, 58.7s wall, zero lab/ diff, trust suite green
throughout (41/41). Gate P1 (reproducibility): PASS, exact
(0.000e+00 deviation). P2 (ripple existence): FALSIFIED -- the headline
finding: at genuinely sub-Nyquist pitch, with a zero-averaging channel
built to surface any ripple the box average would suppress, NO
qualifying ripple was found anywhere across the full 104-cell span --
residual_point is strictly monotonic with zero sign changes in 4 of 5
quintiles. P3/P4 FALSIFIED (three quintiles locked onto the identical
FFT bin, confirmed spectral leakage of a monotonic trend, not a real
oscillation; the one genuine in-band candidate, Q4, was decisively
disproved by P4's digit-exact sinc mismatch -- wrong sign, 22.12x off in
magnitude). P5 CONFIRMED (2/2, on evidentiarily-weak ground). P6:
NARROWS (ripple_fraction <=0.138 in all 5 quintiles). Six blind Phase-5
reviews (PHOTONICS, QUANTUM, VISION: CONFIRM-WITH-GAPS; MATERIALS,
THERMODYNAMICS: CONFIRM; ELECTROMAGNETISM self-review: CONFIRM) found
P2's sign-change test is structurally blind to the one real in-band
wiggle (P4's sinc mismatch is the actual disproof, not P2); Q0-Q3 share
the identical raw FFT bin (QUANTUM's sharpest finding, independently
confirmed by Red Team from results.json's own diagnostic fields); three
of six seats independently found R23's assert covers only the one
perceptual disclaimer it was built for; VISION executed
run.py --predictions-only live to confirm the asserts fire and raised
the round's deepest critique -- R23 proves transcription-fidelity, not
content-adequacy/placement/generality. Red Team's final audit
independently re-derived eleven findings from primitives, adopted all
six reviews with zero overrides. R20 tally: 0 (this round's findings are
evidentiary-strength/framing critiques, not false citations -- a cleaner
citation record than either prior T28 cycle). Checkpoint criterion 4
does NOT fire on either live sub-issue (the R23-coverage gap is its
founding-cycle scope question, not a recurrence; VISION's legibility
critique names a designed-in ceiling with no live defect to remedy) --
both caught blind, pre-LOGBOOK, non-load-bearing. Six mandatory
same-shift fixes applied to NOTES.md (zero re-run, zero verdict change):
the P2/P4 headline reframed; the Q3-shared-FFT-bin finding added; "beat"
corrected to "spectral leakage"; an explicit R23 scope-limitation
statement added; three Iteration-82 queue items added to Next; a Phase 5
outcome section appended. Combined Verdict: PARTIAL. Reconciled
Iteration-82 queue (Red Team's own tiered ranking): Tier 1 -- the T8
r=78/156/312 bridge extension (now unblocked by this cycle's clean
null); the R23 scope decision (genericize or formally ratify
single-disclaimer scope); the near-null-exclusion raw-bin-identity
refinement. Tier 2 -- VISION's fresh-context cold-read trial; a
multi-step-count settling convergence bench across the full dense span.
Tier 3 -- the standing delta_scene R3-vs-R4 split, now FIVE consecutive
deferrals (a sixth must be re-justified in writing or executed);
standing lower-priority items unchanged from exp-103's own Tier 4. Full
record: `experiments/104-t28-subnyquist-standoff-recheck/`, LOGBOOK.md
Iteration 81). Next: panel
Iteration 80 done (exp-103, PARTIAL,
MATERIALS' rotation-lead cycle: executed exp-102's own Reconciled
Iteration-80 queue Tier 1 items 1+2 combined (Red Team's own top
ranking) -- the footprint- and aperture-matched Gate B rebuild. One new
native-flagship FDTD pair (empty+article, theta=0) reused for a genuine
window-averaged kappa_window over the literal established BEHIND
footprint and an 11-point standoff trend (kappa_region) from the
near-field gap out through the window. Red Team's own Phase-2 audit
caught a load-bearing defect before any FDTD call ran: the Phase-1
draft's edge=80 (a literal reuse of R4_TAPER) was the wrong constant
for this file's own cpl=20 grid -- R4_TAPER=80 is rescaled for the R4
family's DOUBLE cells_per_lambda; corrected to EDGE=TAPER=40, giving
genuine physical-aperture-width fidelity. Five blind Phase-2 critiques
(four support-with-changes, one support) plus Red Team's Phase-2 audit
(8 of 9 fixes adopted, QUANTUM's own proposed phase-resampling remedy
explicitly overridden as a zero-information no-op -- sc.phasors()'s
magnitude is provably rel_phase-invariant for this linear engine,
independently re-confirmed three separate times). 4 real FDTD calls (2
primary + 2 settling-check, checking all 5 near-field points at zero
marginal cost, stronger than Red Team's own single-point fallback),
226.7s wall, trust suite green (41/41), zero lab/ diff. All four
predictions CONFIRMED: kappa_window=1.8337% (inside [0.5%,4.0%], close
to the established 1.5-1.8% beam_behind anchor -- Gate B genuinely
reproduced, not force-fixed); the 16-point standoff trend rises
monotonically with zero reversals; floor gate clean; settling residuals
2-4 orders of magnitude inside the 20% bar. Six blind Phase-5 reviews,
five of six CONFIRM-WITH-GAPS (THERMODYNAMICS alone CONFIRM):
PHOTONICS+QUANTUM independently found the adopted <=10-cell "Nyquist
fix" pitch does NOT actually satisfy Nyquist for the lambda/2=10-cell
coherent-intensity fringe at risk (needs <5 cells -- the fix samples at
exactly one full period, the degenerate-aliasing case), partially
mitigated by H_REGION=5's own box-average low-pass filtering; MATERIALS'
own self-review found its Realizability Bound reasoning was silently
dropped between Phase 1 and NOTES.md's own Phase-3 freeze; EM found the
Result section's settling-residual comparison to VALIDATION.md's
baseline ran numerically backwards (larger not smaller, by 2x-73x,
verdict unaffected); VISION found the mandatory perceptual disclaimer
missing from Predictions/Result (the third post-escalation instance of
an Iteration-65-named recurring gap, first to survive to Phase 5). Red
Team's Phase-5 final audit independently re-verified every finding from
primitives (8 re-derivations) and adopted all of them, zero overrides.
R20 tally=1 (far below 3+), does not fire. Checkpoint criterion 4 ruled
on both live sub-issues (disclaimer-erosion; Nyquist-overclaim) and does
NOT fire on either, per unbroken discharge-test precedent -- both
flagged, both mandatory same-shift fixes applied to NOTES.md (backwards
citation corrected; disclaimer added to both sections; Realizability
Bound restored; Prediction-2 Result paragraph rescoped as weak not
clean disconfirmation of the lambda/2-scale alternative specifically;
passivity statement added; quantization arithmetic corrected). Zero
verdict changes. Combined Verdict: PARTIAL. Reconciled Iteration-81
queue: Tier 1 (a genuinely sub-Nyquist standoff recheck, one fresh
~2-call FDTD pair, plus restoring Delta_phi and per-point spread
reporting at zero further marginal cost); Tier 2 (the T8 r=78/156/312
bridge extension, sequenced after Tier 1); Tier 3 (a multi-step-count
settling convergence bench; thermal-sidecar cross-resolution scrutiny
pre-registered for its next invocation; the disclaimer-erosion
standing-rule question); Tier 4 (Tier-2 perceptual conversion,
witness-scale wattage, the delta_scene R3-vs-R4 split -- now FOUR
consecutive deferrals, a fifth must be explicitly re-justified in
writing -- dense-standoff-trend functional fit). Full record:
`experiments/103-t28-gateb-footprint-aperture-match/`, LOGBOOK.md
Iteration 80); panel Iteration 79 done (exp-102, PROMISING,
PHOTONICS' rotation-lead cycle: executed exp-101's own Reconciled
Iteration-79 queue item 1 -- built the coherent, phase-resolved
downstream point-intensity instrument (reads already-gated Ez/Hx/Hy
phasors, lab/sections.py::full_capture/phasors, stage 8, zero lab/ diff,
at a small region on the beam's own rotating downstream axis, comparing
empty/article captures coherently at the identical point), closing
exp-101's own top-ranked Next item and NOT touching T28/delta_scene at
all (Tier 1's own R3-vs-R4 split now three cycles deferred). Diagnostic
only, T1: N/A. Five blind Phase-2 critiques (unanimous support-with-
changes) plus Red Team's Phase-2 audit (9 attacks, 7 mandatory fixes
adopted, 0 overridden, 1 new defect Red Team itself found -- Gate A's
self-comparison can't catch a P(theta) placement bug, closed by adding
Gate D). A Director orchestration error (two Phase-4 agents raced on the
same run.py) was disclosed in full and cleanly consolidated -- zero lab/
diff throughout, trust suite green before/during/after, independently
confirmed via git at Phase 5. 26 real FDTD calls, 3278.5s (54.6 min)
wall. Gate A: PASS (exact). Gate B: FAIL, genuine and honestly diagnosed
-- a real cpl-rescaling bug was found and fixed first, but the corrected
point still sits closer to the object than the established beam_behind
figure's own wide-window footprint, in the near-field where a shadow
reads darker before Fresnel fill-in -- not force-fixed (would be the R5
post-hoc-search pattern); only Gates A+D validate this cycle's primary
readings. Gate C/a frozen self-consistency formula: FAILED as originally
specified (uniform ~150% deviation, a sign-flip signature), PASSED after
a sign correction independently re-derived SIX separate ways -- the most
heavily cross-verified single formula fix in this program's history, both
error and correction fully disclosed. Gate D: PASS. All five predictions
CONFIRMED. kappa(theta): 3.48e-3-7.29e-3 across all 12 cells, genuinely
dark (realizability caveat carried -- article is locked UNOBTAINIUM-WITH-
PARAMETERS); kappa_off(theta): 1.04-1.08, confirming localized darkening.
Thermal sidecar N/A, code-confirmed not invoked. Six blind Phase-5
reviews (all CONFIRM-WITH-GAPS) converged, all six, on one real citation
defect (Result's kappa range floor 3.68e-3 was the second-smallest of 12
cells, not the true minimum 3.48e-3); MATERIALS additionally found the
same headline recurring in Learned #1 without the caveat. Red Team's
Phase-5 final audit independently re-verified every number (a seventh
recomputation of the range-floor defect, a sixth Gate-C re-derivation)
and ruled ONE distinct R4-class defect survives Phase-3-freeze into
Result/Learned (one root cause, two places, not two defects) --
R20 requires 3+, does NOT fire (the cycle immediately after Iteration
78's own first-ever R20 firing). Checkpoint criterion 4 does not fire on
any ground. New standing rule R22 adopted (a frozen vector self-
consistency identity's SIGN must be independently re-derived from the
same governing convention already in use elsewhere in the document,
before any Phase-4 FDTD call is scored against it) -- founding instance,
does not fire. Three same-shift documentation fixes applied (zero re-run,
zero verdict change). LOGBOOK.md Iteration 79 entry written; Marsh
notified per PANEL.md's continuous-mode protocol (no checkpoint pause).
Reconciled Iteration-80 queue (Red Team's own ranking): Tier 1 (EM's
zero-FDTD standoff diagnostic on Gate B's own captured field; a
footprint+aperture-matched Gate B rebuild; extending this instrument
across the T8 r=78/156/312 bridge family); Tier 2 (the Tier-2 perceptual
conversion, gated on Tier 1; pinning the witness-scale source wattage);
Tier 3 (the standing delta_scene split, now 3 cycles deferred; a
pre-registered kappa_off angular resweep). Full record:
`experiments/102-coherent-downstream-point-intensity/`, LOGBOOK.md
Iteration 79); panel Iteration 78 done (exp-101, PROMISING
substantively with CHECKPOINT CRITERION 4 FIRED as a process flag --
VISION SCIENCE's rotation-lead cycle: executed exp-100's own Reconciled
Iteration-78 queue, Tier 0 only -- replaced beam_behind_t28 (Iteration
77's uninterpretable fixed-line-window instrument) with a closed
four-face Poynting-box reconstruction on already-gated sc.widths()/
box_for_r4/ref_for_r4 (trust-suite stage 8), zero lab/ diff, T1 N/A.
Re-selected the true pool-wide-largest-magnitude delta_scene angle
(39.200000deg, exp-095, the single largest of 75 pooled values) in
place of exp-100's own locally-scoped 40.960901deg. Five blind Phase-2
critiques (unanimous support-with-changes) plus Red Team's Phase-2
audit (7 attacks, 6 mandatory fixes adopted, 0 overridden, 1 new
defect found -- undisclosed duplicate rows in the delta_scene pool,
12/33 R3 + 6/35 R4, flipping R3's "significant coupling" to
non-significant on dedup). 24 real FDTD calls, 1961.6s (32.7 min)
wall, trust suite green throughout (41/41), zero lab/ diff, all 12
cells cleared the amplitude floor. Three of four predictions
CONFIRMED (sigma_abs/sigma_ext in [0.5129,0.5145]; back_frac>0.5 at
every cell with a real, un-pre-registered monotonic decline
0.65->0.53; box_dev_scat_downstream<=0.0454); Prediction 3 FALSIFIED
by a wide margin (measured 0.55-0.62 vs predicted <0.15) --
self-diagnosed as the necessary extinction-paradox companion of a real
shadow, the clearest demonstration yet that this energy-partition
instrument cannot itself answer constraint 1's witness question
(needs coherent field PHASE, which a Poynting-flux integral
discards). Constraint 2 stays clean (>=173x inside the R18 gate).
Thermal sidecar: all 12 cells UNDETECTABLE (368x margin), narrated per
R21. Six blind Phase-5 reviews (all CONFIRM/CONFIRM-WITH-GAPS) found
two genuinely new physics results (QUANTUM: an R9 i_inc/cos(theta)
commensurability artifact inflating every ABSOLUTE sc.widths() output
at oblique incidence, corrected values matching the bench's own
locked Q_ext=1.5385 anchor to ~1%; PHOTONICS: the back_frac decline is
very likely a fixed-lab-frame-box registration artifact, not article
physics, tracking tan(theta)) plus MATERIALS' Q_abs>1 finding and its
connection to the article's own locked UNOBTAINIUM-WITH-PARAMETERS
verdict -- and, independently, THREE R4-class citation/restatement
defects in NOTES.md's own Result prose (an observer_article_norm
range that was actually a subset mislabeled as the whole; a
back_frac "tracking to 3 decimal places" claim that fails at 5 of 6
angles; a thermal-sidecar "same trend as sigma_abs" claim that
diverges 2.09x), each caught only at Phase 5. Red Team's Phase-5 final
audit independently re-verified every finding from primitives and
ruled: standing rule R20 (adopted Iteration 76) FIRES for the first
time in this program's history -- three valid R4-class instances meet
its "three or more" bar under the most conservative counting (a
fourth candidate ruled R9-shaped not R20-shaped; a fifth excluded on
textual scope grounds, living in Idealizations/Next not
Result/Learned) -- and CHECKPOINT CRITERION 4 FIRES automatically as
R20's own textually-mandated consequence. None of the three defects
changes any of the four scored verdicts; every number in results.json
was independently reproduced unchanged. Ruled a notification, not a
pause, per this program's unbroken precedent (15 for 15). 13
same-shift, documentation-only NOTES.md fixes applied (zero re-run,
zero verdict change). LOGBOOK.md CHECKPOINT entry + Iteration 78
entry written; Marsh notified per PANEL.md's continuous-mode protocol.
Reconciled Iteration-79 queue (Red Team's own ranking): (1) the
coherent, phase-resolved downstream point-intensity instrument
(constraint 1's own missing conversion -- corrected from a mislabeled
"T3" reference this cycle caught), bound to two new preconditions
(correct the i_inc/cos(theta) artifact; use a beam-aligned or
beam-rotating frame, not a fixed lab-frame box); (2) Tier 1's own
R3-vs-R4 delta_scene split (PHOTONICS' zero-FDTD physical-hypothesis
check first), now doubly informed by this cycle's own pool-duplication
finding; (3) standing deferred items unchanged. Full record:
`experiments/101-t28-r4-closed-box-constraint1-reconstruction/`,
LOGBOOK.md Iteration 78); panel Iteration 77 done (exp-100, PARTIAL,
QUANTUM OPTICS' rotation-lead cycle: executed exp-099's own Reconciled
Iteration-77 queue -- Tier 1 (PAD-vs-article partition, MATERIALS'
disposition memo, 4-point Richardson characterization at Null B) gating
Tier 2 (the constraint-1/2/3/4 scoring pass on delta_scene(theta),
deferred seven prior cycles). Five blind Phase-2 critiques (unanimous
support-with-changes) plus Red Team's Phase-2 audit (9 attacks, 0
overridden, 3 new defects Red Team itself found: RT-1 -- Leg B's
original 4 angles are delta_scene's own zero-crossings, the worst
possible sampling; RT-2 -- no pre-registered correlation threshold;
RT-3 -- Tier 2 not actually gated on Tier 1's outputs as commissioned,
a live risk of an eighth T1:N/A deferral dressed as progress). Phase 3
adopted all 9 fixes, expanding Leg B to 6 angles and pre-registering
the cycle's own T1-label per Tier-1 outcome before any run. Phase 4:
run.py's first execution crashed before any sim.run() call (0 FDTD
calls spent) with a PicklingError from two independent _load() chains
clobbering the same sys.modules registration; fixed by sourcing every
R4-family name through a single internal chain, re-executed from
scratch. 24 real FDTD calls, 3095.8s (51.6 min) wall, trust suite
green, zero lab/ diff. Tier 1 item 1 (PAD-vs-article partition):
AMBIGUOUS -- pooled r=0.2065/p=0.0758 misses the joint rule, but R3
alone shows a significant correlation (r=0.486, p=0.0042, n=33)
contradicting R4 (r=0.110, p=0.525, n=35) and R5 (n=4, underpowered) --
routed to AMBIGUOUS per the pre-registered fold-in rule, not a post-hoc
choice. Item 3: raw-magnitude monotonicity CONFIRMED at full precision,
implied local order drops sharply (0.879->0.172). Tier 2 Leg A: PASS
at both C_thr bars (static-contrast bound only, pending T3). Tier 2 Leg
B -- split result: observer_record_t28 (constraint 2) PASSES cleanly
at all 6 angles, this bench's first-ever trustworthy direct specular-
return measurement; beam_behind_t28 (constraint 1) is UNINTERPRETABLE
-- a real, quantified window-centering defect (the object's own shadow
walks 125.7-154.6 cells laterally at these oblique angles, 79-97% of
the window's own half-width), independently confirmed four ways
(NOTES.md, PHOTONICS, EM, Red Team). Six blind Phase-5 reviews (all
CONCUR-WITH-GAPS): PHOTONICS corroborated the beam_behind_t28 diagnosis
quantitatively; MATERIALS found the R3-vs-R4 split is a named instance
of R15's own Iteration-71 addendum (remedy: a properly-powered,
ground-truth-gated R5 census, not more R3 data); ELECTROMAGNETISM
independently re-confirmed both new-instrument diagnoses from
primitives; THERMODYNAMICS found fix 7's netd_row() persistence landed
code-enforced but its own headline finding was never narrated in
Result/Learned, the identical shape THERMODYNAMICS' own Iteration-76
self-review found in itself; VISION found the ambiguous-Tier-1 caveat
missing from Leg A's own Result paragraph; QUANTUM OPTICS' own
self-review traced RT-1/RT-2/RT-3 to reduced adversarial scrutiny from
a motivated rotation lead. Red Team's Phase-5 final audit ADOPTED all
six (0 overridden except QUANTUM's own governance request, ruled
already covered by PANEL.md's existing charter) plus one new defect of
its own (fix 1's "two largest" claim searched only a local subset,
missing a larger full-pool value at theta=39.2 -- non-load-bearing,
disclosed same-shift). New standing rule R21 adopted: a persisted
sidecar field's own headline finding must be narrated in Result, not
merely persisted -- distinguishes from R16 (persistence alone),
founding basis two instances (exp-099, exp-100), neither fires.
Checkpoint criterion 4: closest call yet, does NOT fire -- RT-3's risk
verified structurally discharged, R21 only its second instance, every
defect caught blind within-cycle. The now-eight-consecutive-cycle
T1:N/A streak (Iterations 70-77) is named explicitly and bound forward:
Iteration 78/79 must either complete the R15-prescribed diagnostic or
explicitly retire the delta_scene-realizability question. Combined
Verdict: PARTIAL. Reconciled Iteration-78 queue: Tier 0 (fix
beam_behind_t28 via closed-box reconstruction, re-select angles from
the full pool, an energy-partition table); Tier 1 (a physical-
hypothesis check, then targeted R3 replication, then the R15-prescribed
properly-powered ground-truth-gated R5 census, then the 750/450nm leg);
Tier 2 (T3 build, scope future sigma(I)/sigma(x,t) claims); Tier 3
(standing deferred items). Full record:
`experiments/100-t28-delta-scene-constraint-scoring-pass/`, LOGBOOK.md
Iteration 77); panel Iteration 76 done (exp-099, PROMISING,
THERMODYNAMICS' rotation-lead cycle: executed exp-098's own Reconciled
Iteration-76 queue items 1-3 (item 4, ratifying R19, already done; item 5
given a reasoned disposition). Five blind Phase-2 critiques (unanimous
support-with-changes) plus Red Team's Phase-2 audit (9 attacks, 7
mandatory fixes adopted, 1 new defect Red Team itself found). Phase 4:
run.py's first execution crashed mid-item-1 with a KeyError (a
freshly-computed float failing to bit-match a filed dict key) after 12
real calls had already completed correctly; fixed (pull the actual
stored key) and re-executed from scratch. 40 real FDTD calls (full
PASS-path), 148.32 min wall, trust suite green throughout, zero lab/
diff. Item 1 (Null C wider bracket): INCONCLUSIVE-AT-THIS-WIDTH -- a
genuine reversal/bounce near theta0+0.5-0.83deg, no zero-crossing across
the +-1.5deg span. Item 2 (cpl=50/R5's first-ever real FDTD spend in
this program's history, ground-truth-gated): every gate cleared, full
28/28-call PASS-path, SIGN-CHANGE-FOUND at theta_c50~=39.776870deg,
Richardson (30/40/50): observed 0.9623 vs naive 0.64. Item 3 (GP2'/ptp
tail): genuine non-resolution honestly disclosed. Six blind Phase-5
reviews (all CONCUR-WITH-GAP(S)): PHOTONICS found Learned #4 cited
exp-098's own RETRACTED Richardson figure (1.777) instead of the
corrected 0.7765163757372424, inverting growing into shrinking;
THERMODYNAMICS' own self-review found a mislabeled ratio and its own
energy sidecar silently omitted from Result/Learned; ELECTROMAGNETISM
found a false settling-angle "coincidence" claim (actual gap
3.3368e-4deg); QUANTUM+MATERIALS independently converged on
delta_scene's own unresolved realizability ambiguity (Iteration 59-60,
never reaffirmed) risking the T1 trigger scoring a domain artifact as a
material mechanism; VISION found a Phase-2 word-cap recurrence and an
unauditable verification claim. Red Team's Phase-5 final audit ADOPTED
all six in full (independently re-verified from primitives), named the
aggregate pattern (FIVE total R4-class citation/label defects across
this document's lifecycle) and adopted new standing rule R20 (3+
R4-class defects surviving Phase-3 freeze into Result/Learned, each
caught only at Phase 5, is a Checkpoint-4-grade pattern going forward --
does not fire on its own founding instance). Checkpoint criterion 4:
does NOT fire (closest call in the R4 lineage, but every defect caught
blind within-cycle, matching R16-R19 precedent). All six mandatory
documentation-only fixes applied same-shift to NOTES.md. Reconciled
Iteration-77 queue (resolves a genuine 5-vs-1 seat disagreement on
sequencing): Tier 1 (mandatory preconditions before any
constraint-1/2/3/4 scoring pass touches delta_scene(theta)) -- QUANTUM's
PAD-vs-article partition elevated to mandatory, MATERIALS' disposition
memo, a 4-point Richardson convergence characterization at Null B; Tier
2 -- the constraint-1/2/3/4 scoring pass itself (rotation lead: QUANTUM
OPTICS), gated on Tier 1 but not deferred an eighth cycle (seven
consecutive T1:N/A cycles); Tier 3 -- Null C's trough at full period,
VISION's pre-flight note, EM/THERMODYNAMICS persistence-gap backfills,
Richardson generalization to Null A, item 3's GP2'-vs-exp-086 recompute,
standing 5-8-cycle-deferred items. Full record:
`experiments/099-t28-null-c-r5-thirdpoint-gp2-reconciliation/`,
LOGBOOK.md Iteration 76); panel Iteration 75 done (exp-098, PROMISING,
ELECTROMAGNETISM's rotation-lead cycle: executed exp-097's own Reconciled
Iteration-75 queue, Tier 0 alongside Tier 1, plus the 11-cycle-old
grazing-incidence governance ask, scheduled and genuinely discharged
rather than deferred a 12th time. Five blind Phase-2 critiques
(unanimous support-with-changes): PHOTONICS found the proposed
grazing-incidence check was analytically theta-independent by
construction, unable to ever detect the already-known exp-086 blow-up;
MATERIALS found "migration vs. recipe defect" a false dichotomy absent
a convergence-order estimate; THERMODYNAMICS found netd_row() wiring
was prose-only, citing a since-overridden precedent (recommendation
adopted anyway); QUANTUM confirmed the Idealization-40 fix and found
GP3's reciprocity check degenerate; VISION found word-count/banner
gaps. Red Team's Phase-2 audit (PROCEED-WITH-MANDATORY-FIXES, 9 items,
1 overridden) ruled the grazing-incidence check must be redesigned, not
shipped as a blind discharge -- Director chose a genuinely
theta-dependent redesign (GP2', reusing the same already-verified
closed-form machinery) over deferral. Phase 4: 64 real FDTD calls
(corrected mid-cycle from an initially-miscounted 32, an arithmetic
error that survived every review layer, caught only by the code's own
assert), 134.6 min wall, trust suite green, zero lab/ diff. Item (i)
(bracket the other three cpl=20 nulls at cpl=40): MIXED -- nulls A/B
show genuine cpl=40 sign changes, null C does not. Item (ii)
(re-centered node search at theta0~=38.590230deg): CONFIRM-migration-
down, crossing found at ~38.252deg below exp-095's own original
bracket -- R17 working exactly as designed one cycle after its own
founding defect. Item (v): GP1 passivity PASS; GP2' (redesigned) flags
MARGINAL amplitude departure theta=50.5-89.5deg, peaking at theta=66.0
deg (235.4x) squarely inside the known exp-086 blow-up band --
genuinely discharging the governance ask for the first time. Six blind
Phase-5 reviews (all CONCUR-WITH-GAP(S)): QUANTUM found a new
fault-injection scenario (FI-G'') was named by exp-097's own queue and
silently dropped this cycle; PHOTONICS+THERMODYNAMICS independently
found a GP2' Result overclaim ("continuously... entire upper half" --
actually 9 VALID points interspersed); MATERIALS found the Richardson
diagnostic compared a cumulative shift against a marginal one, a
category mismatch reversing the reported direction (corrected: 0.777
shrinking, not 1.777 growing); THERMODYNAMICS+ELECTROMAGNETISM
independently found a THIRD instance of this cycle's own call-count
arithmetic error class ("64 report rows" was the call count, not the
16/18 row count); VISION found a banner-placement gap; ELECTROMAGNETISM's
own self-review found GP1's "passivity floor" framing oversold its
derivation. Red Team's Phase-5 final audit adopted all six plus a
seventh bonus defect, adopted new standing rule R19 NOW (an explicit
exception to the usual cross-cycle cadence: call-count vs. row-count
must be a code-enforced assert), ruled Checkpoint criterion 4 the
closest call this program has had but does NOT fire (caught blind,
same cycle, matching R16/R17/R18 precedent) -- explicit warning that a
fourth recurrence fires it without further warning. All 8 mandated
same-shift fixes applied (zero FDTD, none load-bearing). Combined
Verdict: PROMISING -- both stated goals substantively achieved.
Reconciled Iteration-76 queue: Null C re-test at a wider, asymmetric,
R17-compliant bracket (unanimous #1); the cpl=50/R5 third resolution
point at Null B against the corrected Richardson formula; reconcile
GP2' against exp-086's own method through the 74-89.5deg tail; ratify
R19 (done); state the cpl-is-orthogonal-to-realizability finding and
revisit the six-consecutive-cycle T1-route-N/A flag. Full record:
`experiments/098-t28-cpl40-null-bracket-grazing-instrument/`, LOGBOOK.md
Iteration 75); panel Iteration 74 done (exp-097, PARTIAL,
MATERIALS' rotation-lead cycle: executed exp-096's own Reconciled
Iteration-74 queue, Tier 0 in full, as one combined zero-FDTD build --
Check 6 fixed to positional comparison plus its own cpl_intended half;
Check 5 extended to R3/R5 with a negative control; a new Check 7
(amplitude-taper registration) plus FI-D; a zero-cost documentation
bundle. Five blind Phase-2 critiques (unanimous support-with-changes,
EM+THERMODYNAMICS independently converged on a false "bit-exact"
desk-check claim; QUANTUM found FI-G's R4-only scope; PHOTONICS found
the standing-items ledger silently dropped; VISION found the governance
ruling had no attached verification mechanism). Red Team's Phase-2
audit (PROCEED-WITH-MANDATORY-FIXES, 6 items, zero overridden)
independently found the most load-bearing defect: Check 6's new
cpl_intended sub-check was a family-level tautology, keyed by the same
untrusted field on both sides -- fixed via a notes_line-keyed family_ok
sub-check plus its own fault-injection scenario (FI-H). Phase 4: 0 FDTD
calls, 2.305s wall, 21 Sim constructions bit-exact against the frozen
prediction, trust suite green, zero lab/ diff. Registration-readback
gate: CLEAN (representative set, Check 5 3/3 families, Check 6-new 8/8
points). All nine fault-injection scenarios resolved exactly as
predicted. Six blind Phase-5 reviews (all CONCUR-WITH-GAP(S), zero
DISPUTE): PHOTONICS/MATERIALS/ELECTROMAGNETISM independently found
Idealization 40 mischaracterizes cpl_ok's own independence (the code is
STRONGER than documented, the mirror-image, non-dangerous direction of
every prior R18 instance); PHOTONICS additionally found FI-G validates
only src_x, never y_lo/y_hi; QUANTUM found Check 5 never tests G40_*
padded configs; THERMODYNAMICS found a wording imprecision;
VISION found four of five Phase-2 sections exceeded the word cap. Red
Team's Phase-5 final audit ADOPTED all six reviews, one partial
override -- QUANTUM's own review independently repeated the
Idealization-40 error, the first instance of an R18-class error inside
a review document itself. All five Checkpoint criteria ruled: none
fire. No new standing rule proposed. Combined Verdict: PARTIAL -- the
core claim survives, R18's own Tier-0 discipline closes all four
claimed-vs-actual coverage gaps plus the mid-cycle tautology without
finding a genuine registration defect. Tier 1 (real FDTD spend) is
genuinely, fully unblocked -- unanimous across all six Phase-5 reviews
and Red Team. Reconciled Iteration-75 queue: Tier 0 fixes now run
ALONGSIDE Tier 1 (correct Idealization 40, log QUANTUM's echo, add
FI-G' to Check 5, restate the G40_* disclosure); Tier 1: bracket the
other three established cpl=20 nulls at cpl=40 (unanimous #1), the
re-centered node-bracketing re-run at 38.590deg, pre-wire netd_row()
sidecar per R16, cpl=50/R5 sweep stays deferred. New governance ask:
PHOTONICS' own grazing-incidence check (10-11 cycles undischarged)
should be scheduled within two cycles or formally deprioritized. Full
record: `experiments/097-t28-r18-tier0-gate-closure/`, LOGBOOK.md
Iteration 74); panel Iteration 73 done (exp-096, PARTIAL,
PHOTONICS' rotation-lead cycle: executed exp-095's own Reconciled
Iteration-73 queue items 1+2 -- the angle-domain registration-readback
gate (QUANTUM's proposal, run first per the queue) and the zero-FDTD
bracket-width desk bound. Five blind Phase-2 critiques (unanimous
support-with-changes, MATERIALS/ELECTROMAGNETISM/QUANTUM OPTICS
independently converged, by three different routes, that the gate
validated job constants against themselves, never a ground truth outside
the code path it audits; VISION found the mandatory Idealizations banner
missing from Predictions plus a 300-word Phase-1 cap overrun;
THERMODYNAMICS found a 12-vs-10 construction-count arithmetic error).
Red Team's Phase-2 audit (PROCEED-WITH-MANDATORY-FIXES, 8 items, zero
overridden) independently found the proposal's own C/G-pair congruence
claim factually wrong (only the aperture A is held identical, misattributed
to the wrong gate) -- expanded the representative set 8->16 points for the
placement/phase-array checks. Ruled the three-way convergent finding
fixable: adopted QUANTUM's NOTES.md cross-check (Check 6, "the single most
load-bearing fix") plus MATERIALS' recipe-internal spot-check (Check 5).
Phase 4: 0 FDTD calls, 2.175s wall, 18 Sim constructions, trust suite
green throughout, zero lab/ diff. **Registration-readback gate: CLEAN**
(all 16 representative points pass Checks 1-4, Check 5 clean, Check 6 all
clean). **Fault-injection triad: all as predicted** (positive control
CLEAN, FI-A/B/C all correctly caught). **Desk bound confirmed**: +/-0.5deg
half-width is the most defensible candidate bracket at theta0~=38.590deg.
Six blind Phase-5 reviews (all CONCUR-WITH-GAP(S), zero DISPUTE):
PHOTONICS found the amplitude-taper channel entirely unchecked (a
previously-refuted T28 mechanism candidate, exp-070) and that NOTES.md's
"FI-A caught transitively by Check 4" claim is mechanically false as
coded; MATERIALS found Check 5 restates r4_config()'s own formula rather
than independently re-deriving it; ELECTROMAGNETISM found Check 6 is
set-membership not positional (a same-line index swap passes undetected)
and independently re-derived the FI-A/Check-4 finding as general, not
scenario-specific; THERMODYNAMICS found a silently-reordered desk-bound
ratio triple (non-load-bearing) and an 18-vs-20 construction-count naming
mismatch; QUANTUM OPTICS independently converged on the same FI-A/Check-4
crux and found Check 6 never reads cpl_intended despite three governing
texts claiming it does; VISION found the Result section still lacks the
mandatory Idealizations banner -- now a two-cycle-old quiet convention
drift (exp-095, exp-096). Red Team's Phase-5 final audit adopted all six
reviews, zero overridden, independently re-verified from source. **New
standing rule R18 adopted**: a check's documented scope must be confirmed
against its actual code, and any check joining an already-fault-injection-
verified architecture must get its own control in the same cycle it is
added. **Checkpoint criterion 4 ruled the closest non-firing call since
R16/R17's own founding instances, for the same reason** (caught blind at
Phase 5, own founding cycle) -- **does NOT fire**. **Combined Verdict:
PARTIAL** -- the core claim survives (caller-plumbing and angle-only
transcription drift genuinely ruled out, fault-injection-verified on
Checks 1-4) but is narrower than first stated on four independently-
confirmed axes (the resolution axis rests on Check 1 alone, not
redundantly on Check 1+4; Check 6 covers angle only, not cpl/family, via
set-membership not positional comparison; Check 5 is formula-restating,
not formula-independent, covering only R4/C40; the amplitude-taper
channel is checked by nothing). Within this corrected scope, still
strengthens (does not complete) the case for genuine node migration as the
better-supported reading of exp-095's Rank 1c FAIL. Reconciled
Iteration-74 queue: Tier 0 (zero-FDTD fixes to this cycle's own gate --
fix Check 6 to positional comparison plus its own fault-injection control;
implement Check 6's missing cpl_intended half; add a fault-injection
control to Check 5 and extend it to a genuinely formula-independent
recompute at R3/R5; add a seventh check + FI-D for the amplitude-taper
channel; documentation corrections) before Tier 1 (resume real FDTD spend,
now properly unblocked -- bracket the other three established cpl=20
nulls at cpl=40; the re-centered node-bracketing re-run at 38.590deg at
the confirmed >=0.5deg half-width; pre-wire netd_row() sidecar extraction
from first commit per R16; the cpl=50/R5 interior sweep remains deferred).
Full record: `experiments/096-t28-r4-registration-readback-gate/`,
LOGBOOK.md Iteration 73); panel Iteration 72 done (exp-095, PARTIAL,
VISION SCIENCE's rotation-lead cycle: executed exp-094's own Reconciled
Iteration-72 queue items 1/3/4 as one combined, internally-gated build
(item 2, the cpl=50/R5 third resolution point, built in full and
gate-verified but explicitly gated on item 1's own verdict -- the
Director's own Phase-3 scope extension reading Red Team's "any further
R4-family spend" to cover Rank 3's own cpl=40 legs too, not only the
literal cpl=50 item named next). Five blind Phase-2 critiques (unanimous
support-with-changes, five distinct, non-overlapping catches):
PHOTONICS and QUANTUM OPTICS independently converged that the draft's
own Rank-1 control angles (39.2/39.8deg) sat too close to known
delta_scene nulls for a clean far-from-null ground-truth control;
ELECTROMAGNETISM found the new cpl=50 family had no native-sigma
comparator; MATERIALS found cpl=50 is structurally the LEAST
alias-breaking third point available from the shared r{n}_config()
recipe (only cpl a multiple of 10 keeps Gate 3's radius invariant
exact), so no cpl=50 outcome could discharge R15's own addendum alone;
THERMODYNAMICS found no cell_metrics_r5 was named anywhere, risking a
third R16 recurrence. Red Team's Phase-2 audit (PROCEED-WITH-MANDATORY-
FIXES, 9 items, zero overridden) independently found a sixth defect:
checked against the FULL six-crossing null set, the draft's own "safe"
control angle (39.2deg) was itself only 0.610deg from a genuine null,
and the naive fix (39.0/39.4deg) was not uniformly safe. Phase 3
adopted all nine fixes: corrected control angles (39.2/39.4deg); a new,
additive Rank 1c node-bracketing recovery check (38.49/38.69deg,
+/-0.1deg around the established cpl=20 null theta0~=38.590deg,
QUANTUM's own proposal) combined with Rank 1a into one go/no-go gate;
a native-sigma R5 comparator leg; a necessary-not-sufficient reframing
of any Rank-2b outcome against R15's addendum; cell_metrics_r5 named
and wired from first commit; plus the Director's own independently-
found spec-resolution gap (this codebase never persists raw field
captures across process boundaries -- corrected, raising the PASS-path
total from 72 to 86 calls). Phase 4 ran 20 of 86 possible FDTD calls,
22.47 min wall. **Rank 1a -- PASS**, delta_scene(R4) negative at both
39.2/39.4deg. **Rank 1c -- FAIL**: both 38.49/38.69deg floor-clear but
the SAME (negative) sign -- the established theta0~=38.590deg null does
not manifest as a sign change in the R4 (cpl=40) family within the
tested window. **The combined go/no-go gate correctly HALTed** -- Ranks
2/3 (66 calls) SKIPPED on a since-shown-fragile anchor. **Rank 4
(independent, unconditional) -- NEITHER**: 38.4deg at corrected sigma
reads frac_contrast at only 2.71% of FLOOR, floor_pass=False. Six blind
Phase-5 reviews (all CONCUR/CONCUR-WITH-GAP(S), zero DISPUTE, five
independently-convergent findings via five different routes):
THERMODYNAMICS and MATERIALS independently found the +/-0.1deg bracket
was narrower than this window's own already-documented null-migration
precedent (0.194/0.320/0.377deg between cpl=20 and cpl=30, already on
file); QUANTUM, self-critical of its own idea, proposed a new
angle-domain analog of Gate 5 (a registration/incidence-angle readback);
ELECTROMAGNETISM independently re-derived that Yee-grid dispersion
predicts a node shift 25x-78x too small to explain the FAIL, naming the
crux finding ("observationally degenerate": Gate 5 has never checked
geometric registration, only sigma_e magnitude); VISION found NOTES.md
was missing its Result/Learned/Next sections entirely; **PHOTONICS
supplied the single most load-bearing new finding**: this cycle's own
Rank 4 already places the corrected-sigma cpl=30 crossing at
theta~=38.4deg, a 0.190deg shift matching exp-092's own independently-
measured 0.194deg migration to two significant figures. Red Team's
Phase-5 final audit independently re-verified every finding (zero
disputes on any mechanical number among all seven parties), ruled
genuine node migration is now the better-supported reading of Rank 1c's
FAIL ("an impressionistic 2:1 to 3:1... not a computed posterior") but
explicitly NOT proven -- EM's "observationally degenerate" point
stands, and Red Team's own further finding shows "directional
coherence" is weaker evidence than it looks, since R3/R4/R5 share one
deterministic recipe, not independent discretizations. **New standing
rule R17 adopted**: a tolerance/bracket sizing a presence-or-absence
test must be justified against the largest already-established
cross-resolution shift on file, not adopted as an illustrative round
number; a narrower-than-precedented bracket's FAIL framing must give
equal weight to under-sizing as to any other named hypothesis.
**Checkpoint criterion 4 ruled the closest non-firing call, on two
matters** (the one-sided pre-run Rank-1c framing; VISION's NOTES.md
structural gap, identical to the already-twice-non-fired exp-080/
exp-090 precedent) -- both caught blind, same cycle, before this
LOGBOOK entry; **does NOT fire**. A five-item same-shift mandatory-fix
docket applied post-audit (frozen framing flagged not rewritten, with
correction pointers; new Result/Learned/Next sections written; a
commensurability nit corrected; a bracket-provenance disclosure added),
zero results.json change needed. **Combined Verdict: PARTIAL** -- the
combined go/no-go gate did exactly what it was built to do (Rank 1c
caught a genuine ambiguity a sign-only check would have missed, saving
66 calls); smooth numerical dispersion is ruled out as an explanation;
a new quantitative anchor shifts belief toward genuine node migration
without proving it; the fully-built, gate-verified cpl=50 family is
correctly left unused, to be REUSED (not rebuilt) once the registration
question resolves; R16 compliance is clean. Whether exp-094's own
headline six-point reversal at 41.75-41.90deg survives remains
untouched. Reconciled Iteration-73 queue: an angle-domain
registration-readback gate (QUANTUM, near-zero marginal FDTD cost, run
first); a zero-FDTD desk bound sizing a wider bracket against the
established migration precedent; bracketing the other three established
cpl=20 nulls at cpl=40 (EM, ~24 calls, the decisive discriminator); a
reconciled, re-centered, directionally-weighted node search at
38.590deg with a native-sigma companion leg (~8-16 calls); the cpl=50/
R5 family's own interior sweep, explicitly deferred until the
registration question resolves, to be reused not rebuilt. Full record:
`experiments/095-t28-r4-ground-truth-sign-control/`, LOGBOOK.md
Iteration 72); panel Iteration 71 done (exp-094, PARTIAL,
QUANTUM OPTICS' rotation-lead cycle: exp-093's own Reconciled
Iteration-71 queue executed as one combined build, cheapest-and-
independent-first (a genuine departure from exp-092/093's own gated
chain -- no cross-item dependency this cycle): a sigma-corrected
measurement at the window's lower flanking anchor, 41.6deg (Rank 2, 4
calls); an R3-verify of the three still-unmeasured original cpl=20
caution-zone points, 36.0/38.4/38.8deg (Rank 3, 12 calls, the single
most-repeated open item on the whole T28 board); a genuinely new cpl=40
congruent-geometry family (R4, a mechanical R4_RATIO=2.0 substitution
into the already-validated R3 recipe) re-sweeping exp-093's own six
interior near-null points (Rank 1a settling gate, 8 calls; Rank 1b
interior sweep, 24 calls); plus a zero-FDTD caution-zone extension
(Rank 3-ext). Five blind Phase-2 critiques (unanimous support-with-
changes, five distinct, non-overlapping catches): MATERIALS and
ELECTROMAGNETISM independently converged, by different reasoning paths,
on the same real gap -- no gate in this sub-thread's history has ever
read the constructed Sim object's own sigma_e array, only Python
constants; a runtime wiring bug in the new R4 family would sail through
every static gate undetected, reproducing R15's own founding defect.
PHOTONICS found the Rank-2 CONFIRM lean inverted R13/R14's own
established ratio_k/near-null relationship. VISION found a real
ambiguity about undisclaimed NETD byproducts. THERMODYNAMICS found
Rank 1b's new cells carried no zero-cost energy-channel anchor check.
Red Team's Phase-2 audit (PROCEED-WITH-MANDATORY-FIXES, 5 items, zero
overridden) elevated MATERIALS' runtime sim.sigma_e[shell_mask].max()
check to mandatory Gate 5 -- EM's own proposed static-assert remedy
independently shown algebraically tautological, not a substitute. Phase
3's Director synthesis adopted all five fixes plus independently
re-verified the one disputed figure set a third time, bit-exact.
Phase 4 ran all gates PASS, 48 calls, 50.56 min wall. **Rank 2 --
CONFIRM**, no lean stated in advance. **Rank 3 -- TWO CONSISTENT, ONE
FLIPPED**: 38.4deg flips (ratio_k 0.9075->16.9967, ~19x) despite being
the single smallest-margin point of the entire original n=7 set --
the modal-expectation-violating outcome NOTES.md's own Predictions
explicitly flagged as plausible. **Rank 1a -- PASS** (rel_dev=0.13%).
**Rank 1b -- TWO-NODE CONFIRMED, and materially stronger than the
category name conveys: ALL SIX interior points reverse sign AND
classification** relative to exp-093's own cpl=30 SINGLE-NULL reading --
a complete, full-window reversal, not a boundary-adjacent excursion.
p_abs_w stays flat (<=0.6% swing) throughout. **Rank 3-ext -- CONFIRM**,
bit-exact base table, non-inverted extension. Six blind Phase-5 reviews
(all CONCUR-WITH-GAP(S), zero DISPUTE, a program-record five genuinely
distinct catches, three convergent): PHOTONICS, MATERIALS, and QUANTUM
OPTICS' own self-review all three, independently, caught the identical
defect -- NOTES.md's own Result section claimed Gate 5 was verified "by
injecting a simulated wiring defect into a standalone test harness
during Phase 4" with no corresponding artifact anywhere in the record
(this program's own R4 recompute-don't-hand-type discipline, its first
instance applied to a verification claim rather than a numeric figure);
all three independently reconstructed the test and confirmed the
underlying claim true. VISION found a second overclaim in the same
Result section (the UNDETECTABLE classification, not just the energy-
flatness ratio, was claimed confirmed at cpl=40 without actually being
measured). THERMODYNAMICS traced this to source: the NETD-surfacing
machinery's own byproducts were computed everywhere but persisted
nowhere -- netd_row(), exp-093's own fix for this exact purpose, was
never called in this cycle's genuinely new R4-family code. MATERIALS
and PHOTONICS independently converged on a new R15 addendum (a
full-span reversal cannot default to the finer grid as more correct).
QUANTUM's own self-review flagged the sharpest gap: no control point
verifies the new R4 family reproduces an already-known-correct sign at
a robust, far-from-null angle. Red Team's Phase-5 final audit
independently re-derived every figure a fourth-plus way, adopted the
new R15 addendum, and the Director ratified new standing rule **R16**
(a disclaimer traveling unconditionally is necessary but not
sufficient -- the byproduct itself must be persisted). **Checkpoint
criterion 4 ruled the closest non-firing call in this sub-thread's
history** -- two independent overclaims plus a recurrence of a pattern
declared "genuinely closed" one cycle earlier -- but ruled NOT the
strict "known, named, ignored" bar (the code path was genuinely new,
never having called netd_row() at all). Standing forward-elevating
clause adopted: a third disclaimer-without-persistence occurrence fires
Checkpoint criterion 4 automatically. Five same-shift fixes applied,
zero load-bearing to any verdict, including a deterministic rerun
(bit-exact on every existing figure) extracting the missing NETD/
p_abs_w sidecar -- all Rank-3 census angles and all Rank-1b interior
angles classify UNDETECTABLE. **Combined Verdict: PARTIAL** -- confirmed
cleanly: Rank 2/3/1a/3-ext; most consequentially, Rank 1b's complete
sign-and-classification reversal at cpl=40, physically coherent with
R13/R14's mechanism and (per EM's re-applied dispersion-integral work)
too large for smooth Yee-grid dispersion, pointing to curved-boundary
staircasing. Genuinely new, open: the 41.6-42.0deg window's status
across cpl in {20,30,40} is now three-way unresolved, indistinguishable
per the new R15 addendum from a persistent R3/R4-recipe artifact or a
registration defect absent a third resolution point and a far-from-null
ground-truth control. Reconciled Iteration-72 queue: a ground-truth
sign-recovery control for the R4 family at an already-robust,
far-from-null point (rank 1, QUANTUM's own rank, ahead of the already-
queued cpl=50 check); a third resolution point cpl=50/45 at the same
six interior angles, gated on rank 1 (rank 2); closing the sigma-
comparability gap at both window edges (rank 3); 38.4deg at corrected
sigma (rank 4, QUANTUM's own self-falsified-Idealization-21 finding).
Full record: `experiments/094-t28-cpl40-resolution-sigma-r3-census/`,
LOGBOOK.md Iteration 71); panel Iteration 70 done (exp-093, PARTIAL,
THERMODYNAMICS' rotation-lead cycle: exp-092's own Reconciled
Iteration-70 queue executed as one combined, ordered build (item 5 -> 3
-> 1 -> 2 -> 4): a full NETD/energy-sidecar backfill of exp-092's own
Rank-1 14 cells (item 5, 28 calls, THERMODYNAMICS' own signature item);
a sigma_max PRIMARY-channel check localized to the upper near-null
(item 3, 4 calls); a denser off-grid cpl=30 sweep of 41.75-41.90deg to
resolve the double-crossing (item 1, 24 calls, sigma branch-gated on
item 3); a zero-FDTD cpl=30-only caution-zone re-fit gated on item 1
(item 2); and the twice-deferred Yee-grid dispersion phase-accumulation
integral (item 4, MANDATORY under R8's third-citation tripwire). Five
blind Phase-2 critiques (unanimous support-with-changes, two
independently-convergent load-bearing catches: QUANTUM OPTICS found
item 2's own headline "AUC reversal" claim was a sign-convention
artifact, no real reversal exists; ELECTROMAGNETISM found item 4's
chosen length scale (round-trip PAD) substituted a different,
already-refuted mechanism for the actually-named aperture-length
mandate) and Red Team's 6-item PROCEED-WITH-MANDATORY-FIXES audit (zero
overridden, both disputes independently re-derived from primary source)
landed cleanly pre-run. Phase 3's Director synthesis adopted all six
fixes plus independently re-verified both disputed figures a THIRD time
before freeze, bit-exact match both times. Phase 4 ran all gates PASS,
56 calls, 29.4 min wall (well under the 55-166 min estimate), trust
suite re-confirmed 41/41 green. **Item 5 -- CONFIRM, bit-exact**, all 14
NETD cells UNDETECTABLE. **Item 3 -- REFUTE**: delta_scene FLIPS SIGN at
42.0deg between native and corrected sigma_max, a genuine contamination
Rank 3's own broader census never covered; branches item 1 to corrected
sigma_max. **Item 1 -- SINGLE-NULL**: every interior point reads
delta_scene<=0; the "double-crossing" does not survive resolution
refinement, best read as one smooth near-total-null trough, not two
genuine nodes -- resolving exp-092's own top open question, though only
angular-resolution-verified, not yet R15-grade cross-cpl-verified.
**Item 2 -- CONFIRM, bit-exact** against the frozen n=8 cpl=30-only
table. **Item 4 -- CONFIRM**: at the corrected ell=A_HALF_APERTURE
length scale, ratios 32.1x/80.2x/95.8x land inside the corrected
[10x,200x] band -- the dispersion-alone mechanism is genuinely REFUTEd
(one clear order of magnitude, not the pre-freeze draft's mistaken two)
and R8's own tripwire is discharged for the first time at the correct
length scale. Six blind Phase-5 reviews (all CONCUR-WITH-GAP(S), zero
DISPUTE) each caught a genuinely distinct defect: MATERIALS+PHOTONICS
independently converged on NOTES.md missing its Result section (fixed
mid-Phase-5 by the Director) and a stale "always native sigma_max"
caption in run.py persisted uncorrected into results.json;
THERMODYNAMICS' own self-review (self-critical) caught its own §1
self-test was promised but never reported for item 1's own interior
points -- a third, milder, self-caught instance of the same
"confident-claim-unverified" shape Phase 2 had already caught twice in
its own draft; ELECTROMAGNETISM independently re-derived item 4's own
ratios bit-exact and found item 1's own "continuous curve" mixes
native- and corrected-sigma points with no single consistent physical
basis (real, disclosed, confirmed non-load-bearing); QUANTUM OPTICS
independently reproduced item 2's own figures bit-exact and confirmed
item 1's own outcome logic depends purely on delta_scene<=0. Red Team's
Phase-5 final audit adjudicated every finding (both mid-Phase-5
Director fixes ruled adequate and non-firing under this program's own
"caught blind, same cycle" precedent; the caption defect UPHELD, real,
non-load-bearing, one same-shift fix required and applied
post-audit). **No CHECKPOINT this cycle** (all five criteria worked
through explicitly; criterion 4 -- the disclaimer-erosion lineage's own
fourth-and-fifth-instance question -- does NOT fire, VISION's own prior
structural fix genuinely closed that gap class). No new standing rule
adopted -- R13/R14/R15 applied unchanged. **Combined Verdict: PARTIAL**
-- confirmed: the double-crossing does not survive resolution
refinement; the twice-deferred Yee-dispersion mandate is finally
discharged at the correct length scale; the energy channel stays flat
and UNDETECTABLE everywhere, including the disputed node's own
interior. Genuinely new, open: a real sigma_max-sensitivity at the
exact angular band this cycle also resolution-swept (item 3's sign
flip), meaning SINGLE-NULL is not yet cross-verified against the
native-sigma regime that originally located the double-crossing.
Reconciled Iteration-71 queue: a targeted cpl=40 spatial-resolution
check at 41.75-41.90deg (rank 1, convergent MATERIALS+PHOTONICS);
closing the sigma_max comparability gap at both window edges (rank 2,
convergent EM+QUANTUM); R3-verifying the three still-unmeasured
original caution-zone points 36.0/38.4/38.8deg (rank 3, the single
most-repeated item on the whole T28 board). Full record:
`experiments/093-t28-upper-crossing-resolution-netd-thread/`,
LOGBOOK.md Iteration 70); panel Iteration 69 done (exp-092, PARTIAL,
ELECTROMAGNETISM's rotation-lead cycle: exp-091's own reconciled
Iteration-69 Ranks 1-3 combined into one 40-call build, run in Red
Team's own mandated order -- Rank 3 (12 calls) FIRST, gating Rank 1's
(28 calls) sigma_max choice; Rank 2 (zero FDTD) rebuilding exp-090's
caution zone under DROP/RELABEL treatments. Five blind Phase-2
critiques (unanimous support-with-changes, two independently-convergent
pairs: MATERIALS + QUANTUM OPTICS both independently found Rank 1's
20-call spend unsequenced with the 6-call Rank 3 validity check;
PHOTONICS found the net's own amplitude-inflation corroboration a non
sequitur, though its stronger alternative basis independently motivated
the same net-extension fix; THERMODYNAMICS found Rank 3's own p_abs_w
byproduct unscored; VISION found a silently-dropped idealization and an
about-to-recur print-parity gap) and Red Team's 7-item
PROCEED-WITH-MANDATORY-FIXES audit (zero overridden, sequencing fix
independently confirmed to cost zero net wall-time) landed cleanly
pre-run. Phase 3's Director synthesis adopted all seven items plus
caught an eighth defect of its own: the proposal's claimed "zero-cost"
empty-leg reuse was not actually implementable (contrast_from_runs
needs the raw empty-run profile array; no T28-family experiment
persists raw captures to disk) -- missed by the proposal's author, all
five critics, and Red Team alike; fixed by re-running the empty leg
fresh (a deterministic reproduction), growing the cycle from 34 to 40
calls. Phase 4 ran all gates PASS, 40 calls, 20.58 min wall. **Rank 3 --
CONFIRM, cleanly:** the sigma_max confound does NOT contaminate the
PRIMARY delta_scene/frac_contrast channel (ratios 0.92x-1.18x, sign
held), resolving exp-091's own top open question in the clean
direction; sigma branch licensed Rank 1 to run at native sigma_max=0.5.
**Rank 1 -- NEITHER**, a genuinely split result: the lower cpl=30
crossing is cleanly LOCATED (40.0718deg, a real -0.194deg shift from the
known cpl=20 location); the upper window reveals a NEW double-crossing
structure (41.7811deg/41.8377deg, 0.057deg apart, straddling a
NODE-UNRESOLVABLE near-total interference null) -- real but drawn
entirely from floor-gate-failing points, status (genuine two-node
feature vs. under-resolved single null) explicitly undecided. **Rank 2
-- CONFIRM, bit-exact**, a seventh independent reproduction of this
sub-thread's most-verified deliverable. Six blind Phase-5 reviews (all
CONCUR/CONCUR-WITH-GAP(S), zero overlap) each caught a genuinely
distinct defect: PHOTONICS found NOTES.md's own Learned/Next sections
self-contradicted on the double-crossing's own evidentiary status; MATERIALS
found results.json silently dropped the second located upper crossing;
EM's own self-review found its Phase-1 dispersion-integral mechanism
argument was never actually computed, a second consecutive cycle this
exact check was named but not run; THERMODYNAMICS found netd_disposition
computed but never persisted/printed, the identical gap already present
unnamed in exp-091's own record; QUANTUM OPTICS independently re-derived
every headline number bit-exact, zero discrepancies; VISION confirmed
both its own prior-cycle fixes landed and caught a new duplicate-
placeholder defect in NOTES.md, same-shift-fixed. Red Team's Phase-5
final audit adjudicated all four findings and applied same-shift fixes
to each (PHOTONICS' internal inconsistency walked back and Next section
re-ordered; MATERIALS' JSON gap patched additively; THERMODYNAMICS'
NETD gap ruled first-time-naming, non-firing, backfilled, forward
tripwire set; EM's own gap ruled non-firing under R8 but elevated to a
mandatory Iteration-70 item). **No CHECKPOINT this cycle** (all five
criteria worked through explicitly; none fire). No new standing rule
adopted -- R13/R14/R15 applied unchanged. **Combined Verdict: PARTIAL**
-- confirmed: sigma_max confound ruled out on the PRIMARY channel; the
lower crossing located, not merely known-absent from the old window; the
caution-zone DROP/RELABEL table bit-exact a seventh time. Genuinely new,
open: the upper double-crossing's own status, on par with R15's own
still-provisional caution zone. Reconciled Iteration-70 queue: a denser
off-grid/cpl=40 sweep of 41.6-42.2deg to resolve the double-crossing
ambiguity (rank 1); re-fitting R15's caution zone using the located
crossings, gated on rank 1 (rank 2); a targeted sigma_max check at the
upper near-null region itself (rank 3). Full record: `experiments/092-
t28-crossing-relocation-caution-zone-rebuild/`, LOGBOOK.md Iteration 69);
panel Iteration 68 done (exp-091, PARTIAL,
MATERIALS' rotation-lead cycle: the R3 spatial-resolution (cpl 20->30)
check on the T28 C40/G40 PAIR_PAD ambient channel, three cycles overdue
and flagged by MATERIALS itself at exp-088/089/090 -- a 40-call, 4-leg
build (native-cpl repeat at tighter settling; a cpl=30 R3 leg, adding the
one missing G40_R3 config; an R3 settling spot-check corrected to run at
BOTH 40.2/41.4deg per Red Team's own upheld Phase-2 finding that 41.4deg,
not 40.2deg, is the record's actually-harder case; a new 40.4/41.6deg
bracket leg to locate the cpl=30 zero-crossings). Five blind Phase-2
critiques (unanimous support-with-changes, zero overlap: PHOTONICS found
the reused magnitude-ratio tolerance band mistransfers from a different
physical quantity class; ELECTROMAGNETISM found testing against the
unverified cpl=20 FLOOR is circular at exactly the two crossing-proximate
angles; THERMODYNAMICS found the numerator (frac_p_abs) was left
completely untested for resolution survival; QUANTUM OPTICS caught the
41.4-vs-40.2-hardest-case inconsistency; VISION found a mis-cited
idealization banner) and Red Team's 10-item PROCEED-WITH-MANDATORY-FIXES
audit (zero overridden, EM's fix elevated to mandatory under R8) landed
cleanly pre-run. Phase 4 ran all gates PASS but delivered a major,
disclosed-as-possible falsification, not a clean confirmation:
delta_scene(40.2deg) changes SIGN between cpl=20 and cpl=30; neither
bracket reproduces the known cpl=20 crossing at cpl=30 (their true
locations are unlocated, not merely shifted); 37.2deg holds CONSISTENT as
predicted; 40.2deg survives ENERGY-DOMINANT by only 0.74% of
RATIO_HIGH=10.0's own value; **41.4deg RECLASSIFIES from ENERGY-DOMINANT
to CONSISTENT** -- one of exactly two points defining exp-090's own
caution-zone foundation fails its first resolution check; frac_p_abs
(the numerator) stays resolution-robust at all three angles, isolating
the instability to the denominator. Six blind Phase-5 reviews (all
CONCUR-WITH-GAP/variant, each independently confirming the headline
numbers and each surfacing a genuinely distinct finding) and Red Team's
final audit (independently re-derived every number a further time from
source) delivered the cycle's decisive result: **relabeling 41.4deg per
its own cpl=30 finding INVERTS exp-090's own non-parametric caution-zone
construction** (min{margin:Y=0}=1.3095 < max{margin:Y=1}=1.4764),
triggering exp-090's own pre-registered falsification clause. MATERIALS'
self-review found a genuinely new confound (graded_black_shell's
sigma_max left unscaled under the R3 rescale, ~1.5x native optical depth
by this program's own tau_center convention) -- checked and judged small
on p_abs_w but, per Red Team's own extension, NOT yet checked against the
PRIMARY delta_scene/frac_contrast/ratio_k channel the headline sign flip
rests on -- elevated to this cycle's top open question alongside the
still-unlocated crossings. VISION found the mandatory NETD disclaimer
written correctly to results.json but never printed to run_output.txt --
ruled by Red Team a NEW, distinct gap shape (JSON-vs-stdout, not the
Iteration-65 lineage's prose-to-prose propagation failure), non-firing on
two independent grounds. **New standing rule R15 adopted** (a calibration
boundary built from resolution-sensitive-interference-node-proximate
points needs independent R3-verification before being trusted; R13's
floor gate is necessary but not sufficient). **No CHECKPOINT this cycle**
(all five criteria worked through explicitly; none fire -- the
caution-zone-inversion finding is scientifically major but not a "known,
named, ignored" rule violation). **Combined Verdict: PARTIAL** --
confirmed: 37.2deg holds, frac_p_abs/(b2) classification-stable, settling
clean at both resolutions, no geometry-rescale defect; materially
revised: exp-090's caution zone [1.4764,2.1709]/Firth fit m50=2.071,
characterized one cycle earlier as "sound... reproduced by at least nine
parties," must now be treated as cpl=20-specific and provisional, not
resolution-verified, until re-fit under R15. Reconciled Iteration-69
queue: locating the actual cpl=30 crossings with a wider net (rank 1,
5-of-6 convergent); rebuilding exp-090's caution zone under both
drop/relabel treatments, zero-FDTD (rank 2); the sigma_max rescale check
extended to the PRIMARY channel (rank 3); a third cpl=40 resolution
point; extending R3 to the remaining four of exp-090's seven
caution-zone points; a print-parity/Result-section-existence structural
safeguard. Full record: `experiments/091-t28-r3-resolution-denser-
recheck/`, LOGBOOK.md Iteration 68); panel Iteration 67 done (exp-090, PARTIAL,
PHOTONICS' rotation-lead cycle: a zero-FDTD logistic/threshold fit of
R13's FLOOR_FRAC=0.10 floor gate against all 7 now-resolved (theta,
margin, ratio_k) points across exp-087/088/089, executing exp-089's own
near-unanimous Iteration-67 Tier-1 item 1. Method: a non-parametric
caution zone (order-statistic gap between the largest misclassified and
smallest correctly-classified margin), an exact permutation test, Firth's
bias-reduced logistic regression (replacing a demonstrably divergent
naive MLE at this perfectly-separated n=7 sample), and an exhaustive
leave-one-out jackknife -- plus a new PRIMARY distance-to-nearest-known-
crossing comparator (Q8), computed by the Director before freeze rather
than left as an argued-not-computed regressor-choice defense. Five blind
Phase-2 critiques (unanimous support-with-changes, zero overlap: MATERIALS
found the undischarged R3 spatial resolution gap on this channel's own
inputs; ELECTROMAGNETISM found the exact permutation test's null isn't
exchangeable with the actual generative mechanism; THERMODYNAMICS found
the caution zone risks misuse as a sampling-deprioritization signal;
QUANTUM OPTICS found the LOO jackknife's own falsifier can never fire
given the sample's perfect separation; VISION SCIENCE found a missing
mandatory NETD/constraint-3-4 disclaimer, the same disclaimer-erosion
shape that fired Checkpoint 4 one cycle earlier) and Red Team's Phase-2
audit (PROCEED-WITH-MANDATORY-FIXES, 9 items, zero overridden -- including
reclassifying the permutation test and LOO jackknife from falsifiable
predictions to diagnostic sanity checks, a real methodological
correction) landed cleanly pre-run; all nine items adopted in full by the
Director's synthesis. Phase 4 ran all gates PASS, zero FDTD calls: every
frozen prediction reproduced exactly, including Q8's own distance
comparator (both regressors achieve perfect separation; margin's zone is
wider by the raw numbers). **Six blind Phase-5 reviews (five CONCUR/
CONCUR-variant, one PARTIAL) surfaced four genuinely new, non-overlapping
record-hygiene defects after eight prior independent verification
passes**: PHOTONICS (self-reviewing its own proposal) and ELECTROMAGNETISM
independently found the physical mechanism behind Q8 (the four
delta_scene crossings have ~1.8x-differing local slopes, explaining why
margin normalizes better than raw distance); MATERIALS found Q1's own
Result-section narrative ("diverges after 2000 steps, still climbing")
does not match the committed run.py's actual behavior (a hard exit at
iteration 11); ELECTROMAGNETISM separately found Q8's "roughly a third"/
"roughly 3x" gap-ratio language matches neither natural reading of its
own numbers (1.32x direct, 4.20x excess-over-edge); QUANTUM OPTICS found
Q8's own "margin more robust" claim is confounded by sample construction
(the zone-edge-setting points were selected by minimizing margin itself,
not distance) -- connecting two of Red Team's own separate Phase-2
findings that had never been combined; VISION SCIENCE found the Result
section's carried-idealizations banner narrower than the Predictions
section's own per-item citations, a third distinct catch of the
banner-carry-forward mechanism in two consecutive T28 cycles. **Red
Team's Phase-5 final audit** upheld all four findings, extending
MATERIALS' own the furthest -- traced phase3_synthesis.md's own
uncommitted beta=(65.0,-256.8) figure to a variant of the committed
function that exits via a mislabeled "converged" gradient-underflow
branch at iteration 24, the opposite of the "diverges, still climbing"
narrative it was cited to support -- ruled VISION's Phase-5 banner
finding a MILDER variant than the Iteration-65 firing precedent and, on
two independent grounds, **Checkpoint criterion 4 does NOT fire** on any
of the four findings. All seven Tier-0 fixes applied same-shift. No new
numbered rule adopted. **Combined Verdict: PARTIAL** -- a sound, usable
calibration deliverable (the caution zone [1.4764, 2.1709] and Firth's
corroborating fit, m50=2.071) shipped alongside four real, same-shift-
fixable, non-severe defects, an unusually deep (nine-plus-party)
verification stack. Reconciled Iteration-68 queue: a combined FDTD cycle
running the still-overdue R3 spatial resolution check jointly with a
repeat/denser measurement at 37.2/40.2/41.4deg (near-unanimous rank 1
across all six seats); a zero-cost unbiased margin-vs-distance rebuild on
the full 31-point window (rank 2); PHOTONICS' own long-deferred
grazing-incidence validity check (rank 3); the x-wall wavelength-
generality leg (now FIFTEEN consecutive cycles deferred); a mechanical
banner-parity lint safeguard, named for the board. Full record:
`experiments/090-t28-floor-frac-threshold-fit/`, LOGBOOK.md Iteration 67);
panel Iteration 66 done (exp-089, PARTIAL,
VISION SCIENCE's rotation-lead cycle: the combined denominator-node/
numerator-gap census -- one 12-call FDTD set at theta={37.2,40.2,41.4}deg,
each the tightest-floor-margin grid neighbor of one of the three
still-unsampled `delta_scene` zero-crossings, sized to answer both the
node census and the interior-gap census at once. **Primary result:** the
predicted CONSISTENT lean CONFIRMED at 37.2deg (thinnest resolved-margin,
1.046x, ever accepted) but DECISIVELY MISSED at 40.2deg/41.4deg -- both
read `ratio_k`>>10 (25.08, 28.81) despite formally clearing R13's floor
gate at only 1.31-1.48x margin, exactly the single most consequential
possible outcome the document itself pre-registered, realized at both
lowest-confidence angles simultaneously. The combined 8-point
classification FLIPS to ENERGY-DOMINANT (a second and third
floor-clearing ENERGY-DOMINANT angle, not one isolated node) and the
floor-gate-adequacy test CONFIRMS `FLOOR_FRAC=0.10` is not fully
protective at this margin -- a genuine new instrument-calibration
finding. Five blind Phase-2 critiques (unanimous support-with-changes,
two convergent pairs: PHOTONICS+THERMODYNAMICS both flagged the
un-executed R14(a) smoothness check and the 1.4deg interior gap's thin
margin; MATERIALS restated the FLOOR/RMS specificity caveat; EM caught a
false-superlative risk; QUANTUM found the Q4 periodicity test inherited
the exact CONFIRM/REFUTE-labeling hazard that fired Checkpoint 4 one
cycle earlier) and Red Team's Phase-2 audit (9-item docket, zero
overridden, three items elevated to blocking) landed cleanly pre-run;
the Director closed the carried-idealizations banner gap in the same
synthesis, before NOTES.md existed -- Checkpoint criterion 4 did NOT
fire on this gap (caught blind, before Phase 3). Phase 4 ran all gates
PASS, 12 calls, 150.4s, including a new R14(a) smoothness gate (PASS).
**Six blind Phase-5 reviews (five converging independently on the
identical mechanistic finding via five different methods) resolved the
surprise as a corrected diagnosis, not just a corrected
classification**: PHOTONICS, EM, THERMODYNAMICS, and QUANTUM OPTICS each
independently decomposed the `ratio_k` swing and found it ~90%
attributable to the denominator (continuing to collapse toward a real,
nearby zero-crossing) and only ~10% to the numerator's own ordinary
growth -- an R13 (denominator) story, not a new R14 (numerator) hazard.
VISION independently found the same pattern via a clean margin/outcome
separation and caught that NOTES.md's own filed Q6 sentence and Learned
item 1 both asserted language the cycle's own data contradicts
("non-artifactual," "away from any... neighborhood"). **QUANTUM OPTICS,
self-reviewing its own Phase-1 proposal, found and proved the identical
defect false by direct primitive re-derivation** (both angles sit
0.061-0.065deg from a real crossing -- the closest available grid point
to each, chosen for exactly that reason by the cycle's own design).
**Red Team's Phase-5 final audit** independently re-derived every
load-bearing number a fifth and sixth way, confirmed QUANTUM's finding
as a genuine, materially false statement in the frozen record -- but,
after reasoning explicitly against all four prior disclaimer-erosion
instances' own defining shape (an existing correct caveat failing to
propagate, not a freshly-composed false claim), **ruled this does NOT
fire Checkpoint criterion 4** as a fifth instance of that lineage; logged
instead as a new R4/R9 registry note. Separately ruled R13's
`FLOOR_FRAC=0.10` empirically demonstrated inadequate (a clean n=7
margin/outcome separation) but minting a new numbered threshold
premature at this sample size -- recommended a zero-FDTD
logistic/threshold fit as Iteration-67's top item instead. All six
Tier-0 fixes (corrected Q6 sentence, corrected Learned item 1, the
decomposition filed into the permanent record, the R4/R9 note,
MATERIALS' scoping sentence, THERMODYNAMICS' Q7-vs-Q3 decoupling
sentence) applied same-shift. **No new numbered rule adopted. No
CHECKPOINT this cycle.** Full record: `experiments/089-t28-combined-
angle-census/`, LOGBOOK.md Iteration 66); panel Iteration 65 done
(exp-088, PARTIAL,
QUANTUM OPTICS' rotation-lead cycle: the decisive theta=38.4/38.8deg
bracketing follow-up around exp-087's theta=38.6deg ENERGY-DOMINANT
spike, folded with R13's own new denominator floor gate applied both
forward (to the 2 new angles) and retroactively (to exp-087's own 3
already-collected points) -- an 8-call FDTD build plus a zero-marginal-
cost desk computation. **Primary result:** exp-087's own filed
ENERGY-DOMINANT classification reclassifies **CONSISTENT** at the 5
now-sampled angles (theta=38.6deg excluded NODE-UNRESOLVABLE by the
floor gate, `ratio_k`={2.64, 0.908, 5.71, 3.87} resolved at the other
four) -- a disclosed, forward-citable reading, explicitly NOT a
retroactive edit of exp-087's own unedited filed record. Both new
angles cleared `RATIO_HIGH=10` with margin exactly as predicted
(qualitative CONFIRM), but `ratio_k(38.4deg)=0.908` missed its own
pre-registered `[1.5,5.0]` quantitative band: the full 5-point
`frac_p_abs(theta)` sequence is genuinely non-monotonic (a real,
well-resolved dip at 38.4deg below even the 36.0deg anchor value),
disclosed honestly rather than smoothed over. Five blind Phase-2
critiques (unanimous support-with-changes, zero overlap: PHOTONICS
found `delta_scene` crosses zero FOUR times in the window, not just
this one node; MATERIALS found the floor threshold is
article/wavelength-specific and needed an explicit disclaimer; EM
found the bracket width was never justified against any physical
linewidth; THERMODYNAMICS raised an R8 concern later ruled NOT an
actual violation; VISION caught an incipient fourth disclaimer-erosion
instance before Phase 3) and Red Team's Phase-2 audit (10-item
docket, zero overridden) both landed cleanly pre-run. Phase 4 ran all
gates PASS, 8 calls, 138.4s. **Six blind Phase-5 reviews converged
from three independent angles on the same genuine surprise**:
PHOTONICS argued the dip likely inherits T28's own established
~2.84-2.95deg periodicity (C40/G40 are the identical pair
`delta_scene` is built from); MATERIALS found this channel has never
received an R3-mandated spatial (`cpl`) resolution check, only a
temporal one; EM found the data itself (a 3.07x jump in one 0.2deg
step) may instantiate exactly the sub-0.4deg feature its own adopted
bound disclaimed protection against, and that 38.4deg carries the
cycle's thinnest noise margin (2.70x); THERMODYNAMICS mechanistically
traced the dip to the sigma_ext(theta) config-differential term,
forced there by T9-flat `ratio_abs_ext`; **VISION caught the disclaimer-
erosion shape recurring a FOURTH time** -- NOTES.md's own Q4 Result
paragraph (the PRIMARY metric, the cycle's sole new finding) carried
zero inline occurrence of the NETD/constraint-3 disclaimer through
Phase 5, though the adjacent Q1/Q5/Q6 paragraphs and the frozen
Predictions section all correctly carried it; **QUANTUM OPTICS,
self-reviewing its own Phase-1 proposal, found `frac_p_abs` (`ratio_k`'s
own numerator) is architecturally the SAME small-difference-over-base
hazard class R13 already named for the denominator** -- but its own
"Secondary note" falsely claimed no fourth disclaimer instance
existed. **Red Team's Phase-5 final audit** independently re-derived
every load-bearing number from raw primitives, confirmed all six
findings, rejected QUANTUM's false claim directly (logged as its own
R4/R9 registry note), **ruled Checkpoint criterion 4 FIRES** --
explicitly NOT discretionary, since Iteration 64's own close used
unconditional language for a fourth disclaimer-erosion instance ("fires
automatically... no further deliberation"), a deliberate escalation
beyond R6-R13's usual same-cycle-discharge pattern -- procedural/
program-integrity, not scientific (no arithmetic wrong, no gate
bypassed). **New standing rule R14 adopted** (a ratio classifier's own
numerator, built as a small difference between two comparable,
independently-varying quantities, needs the same single-point-distrust
R13 applies to a zero-crossing-capable denominator, even absent a
demonstrated zero-crossing -- PHOTONICS' periodicity-inheritance and
THERMODYNAMICS' sigma_ext-differential findings ruled complementary to
QUANTUM's construction-level hazard, not competing). Ruled the
bracket-width bound retroactively weakened by data; the forward
tripwire restated as ONE combined denominator+numerator angle census.
**CHECKPOINT fired (14th time, notification not pause)** -- fixed
same-shift: the one-sentence disclaimer added to Q4's Result paragraph,
and the "carried idealizations" banner escalated from recommended to
MANDATORY at both the Predictions and Result sections of any future
T28 document (this cycle is direct proof a banner scoped to one section
does not propagate to the other). Full record: `experiments/088-t28-
node-bracket-r13-floor-gate/`, LOGBOOK.md Iteration 65); panel
Iteration 64 done (exp-087, PARTIAL,
THERMODYNAMICS' rotation-lead cycle: the joint EM/THERMO
energy-interception cross-check, named at Iteration 59 and deferred/
exempt four consecutive cycles, finally measured for real -- a genuine,
purpose-built, 13-call article-loaded Poynting-box FDTD measurement
(`lab/sections.py::widths()`, never before run on T28's `PAIR_PAD` scene)
discharges the Iteration-63 forward tripwire (a fifth deferral would have
fired Checkpoint criterion 4 automatically) and FALSIFIES its own
pre-registered ENERGY-DECOUPLED hypothesis. **Primary result:**
`ratio_k`={2.64, 53.99, 5.71} at θ={36.0,38.6,41.8}° classifies
ENERGY-DOMINANT; `θ=38.6°` sits almost exactly on `delta_scene`'s own
zero-crossing (a disclosed, quantitatively-confirmed-sufficient candidate
denominator artifact -- three seats and Red Team's final audit
independently verified this), but even discounting it, the other two
angles both read CONSISTENT (not the predicted DECOUPLED) -- a genuine,
non-artifactual falsification updating this sub-thread's own ten-plus-
cycle phase/interference-only prior. A real bug (a sign-convention
mismatch in `sections.widths()`'s `i_inc` for T28's `-x`-propagating
scene) was found and fixed same-cycle with a zero-`lab/`-diff caller-side
wrapper; Phase 5 (EM) further found this exact geometry/defect pairing
already existed, silently absorbed via ad hoc `abs()`-wrapping, since
Iteration 2 (exp-024) -- a historical-accuracy correction, not a new
defect. All five Phase-2 critiques (unanimous support-with-changes) and
all six Phase-5 reviews (unanimous PARTIAL/CONCUR) found zero-overlapping,
independently-verified issues; Red Team's Phase-5 final audit confirmed
every one, ruled Checkpoint criterion 4 does NOT fire on any of five
non-load-bearing matters (a third disclaimer-erosion instance closed
same-shift with a new forward tripwire for a fourth), and adopted **new
standing rule R13** (a ratio classifier whose denominator has real
zero-crossings must be floor-gated before a single-point decade
classification is trusted -- an algebraic instability distinct from the
R5/R10 statistical-look-elsewhere lineage). **Checkpoint criterion 2
N/A**, matching every T28 desk/instrument cycle since exp-069. Full
record: `experiments/087-t28-energy-interception-poynting-check/`,
LOGBOOK.md Iteration 64); panel Iteration 63 done (exp-086, PARTIAL,
ELECTROMAGNETISM's rotation-lead cycle, executing exp-085's own Red Team
Phase-5 final audit §7 Tier-1 items 1-3: fixed the R11 boundary-pinning
defect (`free_period_with_widening`'s silent narrowest-stage fallback) at
all three affected call sites -- both non-quiet copies PLUS the identical-
shape `_quiet` sibling (Director's own scope extension) -- re-scored
exp-085's Method C classification on the corrected machinery, extended
the circular-shift null to all 37 sub-windows, and ran a bounded
prior-citation audit. Method C re-score reproduced every frozen
prediction exactly: `frac_recovered=21/37=0.5676`, `classification_a=NOT
STABLY PERIODIC` -- exp-085's own "STRONG COHERENT CHIRP" reconfirmed
dead, now by the automated pipeline itself, not a hand audit. Three
pre-registered Spearman stride phases found the overlap-corrected
significance genuinely phase-dependent (one of three clears `p<0.05`,
two don't). The quiet-variant's audit-coverage gap (Red Team's own
Phase-2 finding: a 6.70% boundary-firing rate inside the null-calibration
appendix underwriting T28's "settled" x-normal REFUTE since Iteration
54) was closed with a controlled matched-seed comparison finding
`max_r2_over_trials`/`p_r2_ge_070` **bit-identical** between old-buggy
and corrected logic -- a materially cleaner result than predicted --
corroborated across 10 independent seeds after QUANTUM's Phase-5 review
caught the original single-seed gap. **New standing rule R12 adopted**
(a fix's "negligible effect on a tail statistic" claim needs >=5-8-seed
corroboration before being reported as settled -- R6/R6-addendum
lineage). Full five-phase cycle, six blind Phase-5 reviews (unanimous
PARTIAL, five Phase-2 critiques and three Phase-5 findings with zero
overlap between them -- ten independently-caught defects across the
cycle, none load-bearing), Red Team's Phase-5 final audit independently
re-confirmed all six Phase-5 findings from source and added a seventh of
its own (a promised Method-A re-fit never executed, proven a mathematical
no-op by construction). **CHECKPOINT criterion 4 does NOT fire** on any
of four near-misses this cycle produced, explicitly conditioned on a
4-item Tier-0 mandatory-fix docket landing before the LOGBOOK entry --
it did. **CHECKPOINT criterion 2 N/A**, matching every T28 desk cycle
since exp-069. **New forward tripwire**: the joint EM/THERMO energy-
interception cross-check, now FOUR consecutive cycles deferred/exempt
(083-086) -- a fifth consecutive deferral without either a purpose-built
scene or an explicit retirement of the deferral framing fires Checkpoint
criterion 4 automatically. Full record:
`experiments/086-t28-free-period-boundary-fix-rescore/`, LOGBOOK.md
Iteration 63); panel Iteration 62 done (exp-085, PARTIAL,
MATERIALS' rotation-lead cycle: a zero-FDTD wide-window/dense
re-evaluation of leg (a)'s exact model, asking whether the narrow
31-point window's own INCONCLUSIVE period-match reflects a too-narrow
sample or a genuinely non-stationary curve. Global instruments (Methods
A/B) collapse cleanly to noise-scale -- no single stationary period
exists over the wide domain. The local instrument (Method C) nominally
filed "STRONG COHERENT CHIRP" but Red Team's Phase-5 final audit,
adjudicating two independent Phase-5 catches (MATERIALS+PHOTONICS: a
silent boundary-pinning defect in shared, ~15-experiment-reused period-
search machinery; QUANTUM+VISION: an invalid overlap-inflated
significance figure), recomputed frac_recovered from 1.000 to 0.595 --
**failing the gate every named positive classification shares, so none
is reachable from the as-filed data.** Reported as NOT STABLY PERIODIC,
not STRONG COHERENT CHIRP. **New standing rule R11 adopted** (a
boundary-pinned/non-convergent period-search result must be surfaced,
never silently reported as resolved -- binding on any future reuse of
the affected machinery). **CHECKPOINT criterion 4 ruled NOT firing**
(a close call, correctly weighed: caught blind, same-cycle, before
LOGBOOK commit; no currently-cited T28 number affected; both historical
firings of the same defect, in exp-078/079, were inert). Checkpoint
criterion 2 N/A, matching every T28 desk cycle since exp-069. Full
record: `experiments/085-t28-leg-a-wide-window-period-pin/`,
LOGBOOK.md Iteration 62); panel Iteration 61 done (exp-084, PARTIAL,
PHOTONICS' rotation-lead cycle: the T28 sub-thread's first-ever
diffraction (not reflection/echo) treatment of a boundary — a near-field
Fresnel/Kirchhoff integral over the source aperture's own two tapered
edges. Leg (a) downgraded SUPPORT→INCONCLUSIVE on the period-match vs
`P_edge_A=2.8421°` (fails the program's own harder-companion circular-
shift null, `15/30=50.0%`) but credited with a genuinely new, triply-
stress-tested positive result: `corr(model, real FDTD C80(θ))=0.958` —
the first result in nine-plus T28 cycles showing a zero-FDTD vacuum
construction track real physics this closely. Leg (b) (article-rim vs
`P*=2.9474°`) NO VERDICT — its own pre-registered Anchor 2 failed a
convergence-checked test; ELECTROMAGNETISM's Phase-5 review then PROVED
algebraically that a bare phase-factor fix is powerless (`amb.weber`'s
scale-invariance), narrowing the real fix to a matrix-valued RS/Kirchhoff
kernel. New standing rule **R10** adopted (a specificity-over-targets
sweep is not a substitute for a null-under-noise test — second
consecutive cycle this exact divergence was outcome-determining).
**CHECKPOINT criterion 4 FIRES (13th time)** on the joint EM/THERMO
energy-interception cross-check's third consecutive silent absence —
Red Team's final audit both confirmed the firing and directly adjudicated
VISION's own governance concern (13/13 "notification not pause" firings)
as not evidence of toothlessness, while naming a real, fixable gap in the
escalating-tripwire format itself (no clause distinguishing "chose not
to" from "structurally could not") as a standing Iteration-62 board item.
Full record: `experiments/084-t28-edge-diffraction-derivation/`, LOGBOOK.md
Iteration 61); panel Iteration 60 done (exp-083, PARTIAL, VISION SCIENCE's
rotation-lead cycle, the full 31-point/0.2° `PAIR_PAD`-with-article
re-test at 600nm — the three-branch period discriminator resolved
decisively to Branch B (matches `P_edge_A`), the causal label walked back
twice over (Occam's-razor: `P_edge_A` originates on a scene with zero
article calls), a two-tone admixture claim reversed under the correct
circular-shift null then its own would-be AR(1) rescue caught failing to
reproduce. Full record: `experiments/083-t28-pad-article-full-power-
retest/`, LOGBOOK.md Iteration 60); panel Iteration 59 done (exp-082,
PARTIAL, QUANTUM OPTICS' rotation-lead cycle, discharging the six-cycle
PAD-loaded real-article tripwire — `ratio=0.6573`, VERDICT SURVIVES
mechanically, but the mechanism-continuity question demonstrated
UNRESOLVABLE (not merely under-supported) at this cycle's own 7-point
power. Full record: `experiments/082-t28-pad-real-article-check/`,
LOGBOOK.md Iteration 59); panel Iteration 58 done (exp-081, PARTIAL,
THERMODYNAMICS' rotation-lead cycle, PHOTONICS' construction finally built
exactly as specified and scored via the free-period fit against real T28
data — Combined Verdict NEITHER mechanically, REFUTE-leaning
substantively and decisively (the lone SUPPORT proven, via a pair-
specific reflectance-ablation control, to need zero wall physics at all).
Full record: `experiments/081-t28-photonics-construction-total-field/`,
LOGBOOK.md Iteration 58); panel Iteration 57 done (exp-080, PARTIAL,
ELECTROMAGNETISM's rotation-lead validity pre-check of the plane-wave/
global-steering y-wall construction Red Team's exp-079 audit recommended:
(a) Fraunhofer-margin/`theta_local`-spread check **FORECLOSE**, robust
across the full 3-λ sweep; (b) single-effective-angle reproduction of
exp-079's own true per-point curve **admittance-family-dependent**
(INCONCLUSIVE under the matched/unobtainium admittance, mean `R²=0.7345`;
**REFUTE** under the realizable `μ_r=1` admittance, mean `R²=0.4305`, two
configs negative, surviving a best-fit-scale robustness check); (c)
QUANTUM's blind Phase-2 critique directly built PHOTONICS' own
not-yet-built §4 plane-wave construction (zero new FDTD) and found the
SAME pathology at a WORSE floor — but Phase 5 (QUANTUM again, independently,
confirmed by Red Team's final audit against the primary source) found this
was scored by the WRONG methodology entirely (an `R²` shape-comparison
against a candidate curve, not the free-period fit against real T28 data
PHOTONICS actually specified) and is missing `E_direct` — which PHOTONICS'
own Phase-5 review then proved, from primitives, cancels bit-identically
across every congruent config, so every ingredient for the actually-
correct test now exists for the first time in this nine-cycle sub-thread.
Full five-phase cycle, six blind Phase-5 reviews (unanimous PARTIAL,
zero miscalculated figures across eleven independent reproductions), Red
Team's final audit **explicitly corrected an overconfident "does not clear
a bar" framing before it could reach LOGBOOK.md** — **CHECKPOINT criterion
4 does NOT fire** (ruled a closer call than exp-079's own Iteration-56
precedent, conditioned explicitly on the corrected framing being what is
inherited forward, not the pre-Phase-5 language) — **CHECKPOINT criterion 2
(mechanism-class boundary) ruled NOT YET RIPE**, more precisely specified:
the one test that would settle it (a free-period fit of the total field
against real T28 periods) has never been run, though every ingredient for
it now exists. Full record: `experiments/080-t28-y-wall-planewave-
validity-precheck/`, LOGBOOK.md Iteration 57); panel Iteration 56 done (exp-079, PARTIAL,
the full non-edge-reduced y-mirrored aperture sum computed for T28's
y-wall echo mechanism — the flat/zero-amplitude result exp-078's Phase-5
single-edge model found does NOT survive (`ss_tot` ratio `9.4×10⁻⁷`,
`≈20.2` orders above exp-078's own floor, convergence-checked), but the
recovered `theta_beam`-dependence is structurally, not merely empirically,
incapable of discriminating a real y-wall echo, at ANY period, from no
echo at all — independently confirmed against a SECOND, materially
different admittance family at Phase 5 (MATERIALS' realizable-admittance
re-run: every scored period shifts `≤0.015°`, no verdict flips) —
**CHECKPOINT criterion 4 does NOT fire** (ruled explicitly a close call,
more layers of correction than any prior T28 cycle except exp-078 itself)
— MATERIALS lead by rotation, executing `experiments/078-.../phase5_
redteam_audit.md`'s own Tier-0 item 1, the reconciled Iteration-56
ranking's single highest-value item. Full five-phase cycle: Phase 1
self-scored the result "closer to a genuine (informal) REFUTE... than to
an INCONCLUSIVE" → five blind Phase-2 critiques, unanimous
support-with-changes (ELECTROMAGNETISM's analytic derivation and QUANTUM
OPTICS' empirical ablation — independently, by orthogonal methods —
found the SAME fact: both the per-point bounce angle and the image
propagation distance are `theta_beam`-independent by construction, so
`E_echo`'s entire `theta_beam`-dependence is the spatial Fourier
transform of a `theta_beam`-independent envelope, governed by the shared
aperture window's own T21-family content regardless of the wall's true
reflectance — QUANTUM's own `r(theta_local(y_s))≡1` reflectance-ablation
control reproduces the model's periods to within grid-resolution noise;
THERMODYNAMICS caught a genuine "nine orders of magnitude" arithmetic
slip, the fifth instance of this exact R4 failure shape on this
sub-thread but the earliest caught yet; PHOTONICS found a real, disclosed,
non-load-bearing residual sideband; VISION disconfirmed a "third, sharper
outcome" framing — this is exp-078's own branch (b), refined, not a new
branch) → Red Team's Phase-2 audit (PROCEED-WITH-MANDATORY-FIXES, 9
items, zero overridden; independently re-derived every claim from
primitives, reproducing QUANTUM's ablation from scratch as a third
confirming method; ruled the proposal's own headline over-claims what the
data can support — the correct characterization is that this construction
cannot discriminate a real echo, at ANY period, from none, not "closer to
a REFUTE") → Phase 3 (Director adopted all 9 items, rewrote the headline,
fixed the arithmetic-slip citation, folded the reflectance-ablation
control into committed, reusable code — no FROZEN-PREDICTIONS git-freeze
cycle needed, since no already-computed Test-A number changed and the
ablation's own outcome was already independently reproduced three times
over during Phase 2) → Phase 4 (re-run confirmed every pre-existing
number bit-identical; the new ablation control confirmed exactly:
`PAIR_PAD`/`C80−C40`'s ablated periods reproduce the r-weighted model to
`|ΔP*|≤0.023°` — geometry alone; `PAIR_ABSORB40`'s ablated delta is
EXACTLY zero, since `G40`/`C80` share identical geometry under `PAD=40` —
a sharper, two-part confirmation, not a uniform one) → six blind Phase-5
reviews, unanimous PARTIAL (VISION and THERMODYNAMICS each caught small
record-hygiene gaps, one — a standing instruction to state an explicit
reason before a fourth PAD-sensitivity deferral — never addressed
anywhere in this cycle's own Phase 1–4 record, closed same-shift;
**MATERIALS and QUANTUM, independently, from opposite starting questions,
jointly cracked open the cycle's own central claim's true scope**:
QUANTUM correctly showed the "at ANY period" reading is proven, by the
algebra alone, only for `r(θ)` slowly-varying relative to the aperture
window — true, before Phase 5, only for the ONE matched-admittance model
tested; MATERIALS, separately, found the exp-078-era admittance-
invariance citation this cycle's own Idealization 1 inherited does NOT
generalize to this cycle's own wider envelope (Pearson `r` collapses to
`0.74–0.88`, negative at one depth) but ALSO independently re-ran the full
construction under the realizable admittance end to end and found the
practical conclusion survives, for the structural reason, not the fragile
correlation; **EM directly challenged whether Red Team's own recommended
next instrument — a plane-wave/global-steering y-wall construction — is
itself sound**: the x-wall's own two-plane-wave reduction is an EXACT
cancellation at any range, the y-wall has no such symmetry, and the
aperture sits at `0.8%–2.1%` of its own Fraunhofer distance from the wall
(deep Fresnel zone) with a `2.8×` spread in per-point bounce angle;
PHOTONICS sketched a concrete, buildable derivation route for that same
construction and ran a feasibility probe predicting its own likely
first-pass result is STILL a T21-proximate carrier) → Red Team's Phase-5
final audit: independently reproduced MATERIALS' collapsed-Pearson-r
figures to six decimal places and its full realizable-admittance Test-A
recomputation from scratch before ruling; adjudicated MATERIALS' and
QUANTUM's findings as answering the SAME question from opposite
directions — Idealization 9 scoped (not retracted): proven for `r(θ)`
slowly-varying relative to the aperture window, now confirmed against TWO
independently-tested admittance families; ruled EM's and PHOTONICS'
findings complementary (a validity precondition vs. an output prediction),
sequencing EM's cheap desk pre-check FIRST, PHOTONICS' build second;
independently re-verified two "already corrected" claims in the record it
was handed and found BOTH had actually NOT yet been applied — closed both
directly, the exact discipline that kept Checkpoint criterion 4 from
firing on a genuinely close call. **Combined Verdict: PARTIAL.** T28's own
substantive mechanism question remains open; this cycle forecloses a
SECOND consecutive construction family within the coherent-echo mechanism
class, for a precisely-scoped, now doubly-verified reason — the cleanest
negative result this sub-thread has produced since exp-076's own
lossless-vacuum proof. Full record: `experiments/079-t28-y-wall-full-
aperture-sum/`, LOGBOOK.md Iteration 56); panel Iteration 55 done (exp-078, PARTIAL,
Test-A-only official result INCONCLUSIVE (0/3 SUPPORT, 0/3 REFUTE) for
the y-direction (transverse-normal) wall-echo period pre-screen — T28's
first genuinely new, untested mechanism candidate since Iteration 52 —
**CHECKPOINT criterion 4 does NOT fire** (ruled a close call, not a clean
one) — PHOTONICS lead by rotation, executing LOGBOOK.md's own
Iteration-54 (exp-077) Tier-0 #2 queue item (PHOTONICS+EM #1): derive the
y-wall's grazing-incidence period from scratch and pre-screen it against
T28's established periods, zero new FDTD. Full five-phase cycle: Phase 1
self-scored INCONCLUSIVE (2/3 period comparisons SUPPORT, `PAIR_PAD` —
T28's actual dominant target — just missed) → five blind Phase-2
critiques, unanimous support-with-changes (MATERIALS + ELECTROMAGNETISM +
THERMODYNAMICS independently caught a load-bearing angle-convention bug —
`reflection_coefficient` fed raw `theta` instead of the geometrically
correct `90-theta` for a y-stratified wall; VISION disconfirmed a false
"near-noise-floor" framing; QUANTUM's own 2,000-trial null control on the
as-filed model scored `p=0.080`) → Red Team's Phase-2 audit
(PROCEED-WITH-MANDATORY-FIXES, 7 items, zero overridden; ran a FULL
corrected re-score, not a spot-check: **0/3 SUPPORT**, down from the
as-filed 2/3 — both nominal SUPPORTs were entirely angle-convention
artifacts) → Phase 3 (fix folded into the committed script as primary,
FROZEN PREDICTIONS committed before the corrected re-run) → Phase 4
(every frozen number CONFIRMED exactly; a fresh house-standard
20,000-trial null-calibration against the corrected model found nothing
distinguishable from noise) → six blind Phase-5 reviews, unanimous
PARTIAL (PHOTONICS + THERMODYNAMICS + VISION, three independent methods,
converged that `PAIR_PAD` is provably energy-blind/structurally
under-informative under this model; VISION + THERMODYNAMICS caught the
write-up's own `§5.2` table was never regenerated at the corrected angle;
MATERIALS re-ranked the standing realizable-admittance refit toward the
x-wall; **ELECTROMAGNETISM found even the "corrected" `90-theta` angle is
itself not the physically rigorous incidence angle** for this model's
own point-source construction — the rigorous, per-config-constant
stationary-phase bounce angle collapses the predicted curve to exactly
flat) → **Red Team's Phase-5 final audit independently confirmed EM's
finding bit-exact, then extended it**: built the doubly-corrected curve
directly, flat to float precision for all five configs (`ss_tot` ratio to
real data's own scale `5.9×10⁻²⁷`), diagnosed a NEW spurious-R²-on-a-flat-
array trap, hardened into the shared diagnostic (`SS_TOT_DEGENERATE`).
**Combined Verdict: PARTIAL** — the official INCONCLUSIVE stands, verified
bit-exact, and is sharpened (not reversed) by the Phase-5 finding: this
specific edge-image/single-near-wall reduction, evaluated at its own
internally-consistent angle, predicts no oscillatory signal at all — a
decisively stronger negative than an ordinary INCONCLUSIVE, but not a
formal REFUTE (the pre-registered band presupposes two comparably-
determined nonzero periods) and NOT the closing of the y-wall mechanism
class (the full non-edge-reduced aperture sum and far-wall pair remain
untested). **Checkpoint criterion 4 ruled a close call, not clean**:
three independent Phase-5 findings (EM's angle-within-angle defect,
VISION's stale table, THERMODYNAMICS' partially-executed docket item)
were all caught within this same cycle's own review layer, matching
Iterations 51/53's non-firing pattern, distinguished explicitly from
Iterations 49/50/52/54's firing precedents — the reason it doesn't fire
is that Red Team's own audit actually computed the alternate case rather
than filing it unverified. **Checkpoint criterion 2 ruled NOT YET RIPE.**
A same-shift 7-item mandatory-fix docket (NOTES.md written — was
missing; `§5.2`'s stale table refreshed; a stale digit corrected; a
Fisher-combined omnibus statistic wired in; the new `SS_TOT_DEGENERATE`
guard added) closed same-shift, zero `lab/` diff, pure desk analysis
throughout. Full record: `experiments/078-t28-y-wall-echo-prescreen/`,
LOGBOOK.md Iteration 55); panel Iteration 54 done (exp-077, PARTIAL,
Combined Verdict REFUTE for both `PAIR_PAD` and `PAIR_ABSORB40` on the
complete two-wall coherent-echo instrument, **CHECKPOINT criterion 4
FIRES** (12th time, notification not a pause; new standing rule **R9**
adopted) — VISION SCIENCE lead by rotation, executing PLAN.md's own
Iteration-54 queue item 1 (Tier 0 #1, EM's own pick seconded by THERMO):
refit exp-075's already passivity-gated single-wall transfer-matrix echo
model against `PAIR_PAD≡(C40,G40)` — `ABSORB` fixed at 40 for both, so
any predicted difference is pure image-source round-trip DISTANCE
(`PLANE_X` 77→117) — and `PAIR_ABSORB40≡(G40,C80)` as the geometry-fixed
control. Full five-phase cycle: Phase 1 self-scored single-wall REFUTE
for `PAIR_PAD`, INCONCLUSIVE for `PAIR_ABSORB40` → five blind Phase-2
critiques (unanimous support-with-changes: PHOTONICS + ELECTROMAGNETISM,
independently, each built the disclosed-but-unrun two-wall extension from
scratch, finding `PAIR_PAD`'s REFUTE flips from period-driven to
shape-driven and `PAIR_ABSORB40` flips INCONCLUSIVE→REFUTE; MATERIALS
confirmed the `+x`/`-x` walls share the same unrealizable admittance
class; THERMODYNAMICS found §3's "PAD is lossless" justification a
non-sequitur — the real reason is a code-level common-mode array
identity; QUANTUM flagged the missing null-calibration control, then ran
one itself confirming REFUTE) → Red Team's Phase-2 audit
(PROCEED-WITH-MANDATORY-FIXES, 5 items, zero overridden; caught a NEW
self-referential arithmetic slip inside THERMODYNAMICS' own critique) →
Phase 3 (all 5 fixes adopted; FROZEN PREDICTIONS for the corrected
two-wall-inclusive re-run, matching three independent from-scratch
implementations to 4 decimal places) → Phase 4 (re-run CONFIRMED every
frozen number exactly — **official Combined Verdict: `PAIR_PAD` REFUTE**
via Test B alone (`r²=0.0001`), **`PAIR_ABSORB40` REFUTE**, flipped from
single-wall's INCONCLUSIVE — a 20,000-trial null-calibration appendix
confirmed neither REFUTE is a look-elsewhere artifact) → six blind
Phase-5 reviews, all PARTIAL (PHOTONICS + ELECTROMAGNETISM independently
converged on a genuinely new untested candidate — a **y-direction
transverse-wall echo**, whose standoff tracks `PAD` exactly, invisible to
this cycle's own congruence check; PHOTONICS also found the two-wall
model flips to INCONCLUSIVE at 750nm, un-null-calibrated; MATERIALS
independently re-derived the standard REALIZABLE (`mu_r=1`) admittance
and found it moves `|r|`/`arg(r)` by 15–40%/15–24° — a never-tested,
materially different transfer function; THERMODYNAMICS confirmed its own
Phase-2 arithmetic slip and caught a NEW incommensurable-units error in a
T5/exp-043 comparison; QUANTUM found the committed null-calibration
appendix silently dropped 2 of 3 mandated statistics and an i.i.d.
bootstrap ignoring real residual autocorrelation; **VISION SCIENCE traced
LOGBOOK's own permanent T16 entry — `x=amp_ratio(PAIR_PAD)=0.119` cited
as "~24× `C_thr`" — back to its defining primitives and found a
DIMENSIONAL ERROR: the dimensionally-consistent reading is `≈0.12×`,
SUB-threshold, not `24×` over it**) → Red Team's Phase-5 final audit:
independently re-verified every finding from raw primitives (catching and
correcting its own first-pass estimator error before accepting QUANTUM's
autocorrelation figure); ruled the coherent-echo mechanism CLASS is NOT
closed (only the x-normal, unrealizable-admittance instantiation is
REFUTEd, twice — `NOTES.md`'s original "doubly excluded" language
corrected as overstated); Checkpoint criterion 2 explicitly does NOT fire
(not yet ripe); **Checkpoint criterion 4 FIRES** on the T16 dimensional
error's full chain (self-disclosed once, used anyway, actively but
incompletely re-verified by Red Team's own prior audit, written into
LOGBOOK's permanent record, caught only by a second independent blind
seat one cycle later); **new standing rule R9 adopted** (verifying a
cited ratio's arithmetic is not sufficient to verify the comparison's own
claim — operand commensurability must be independently confirmed). A
same-shift 7-item mandatory-fix docket closed the LOGBOOK T16 correction
plus six other record-completeness items. **Combined Verdict PARTIAL.**
T28's own mechanism question remains open, narrowed toward "not an
x-normal, unrealizable-admittance echo" specifically. Full record:
`experiments/077-t28-pad-round-trip-echo-model/`, LOGBOOK.md Iteration
54); panel Iteration 53 done (exp-076, PARTIAL,
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
- **[ACTIVE — Iteration 65 queue, Red Team's Phase-5 final-audit
  reconciliation of exp-087's six seats (`experiments/087-t28-energy-
  interception-poynting-check/phase5_redteam_audit.md`); supersedes the
  Iteration-64 queue below as the active ranking, that block retained as
  valid backlog, not deleted]** exp-087 (THERMODYNAMICS' rotation-lead
  cycle) built a genuine, purpose-built, 13-call Poynting-box measurement
  of the joint EM/THERMO energy-interception cross-check on T28's
  article-loaded `PAIR_PAD` scene, discharging the Iteration-63 forward
  tripwire and FALSIFYING its own pre-registered ENERGY-DECOUPLED
  hypothesis. **Primary result:** `ratio_k`={2.64, 53.99, 5.71} at
  θ={36.0,38.6,41.8}° classifies ENERGY-DOMINANT; `θ=38.6°` sits almost
  exactly on `delta_scene`'s own zero-crossing (a disclosed, quantitatively
  confirmed-sufficient candidate denominator artifact — PHOTONICS,
  QUANTUM, THERMODYNAMICS, and Red Team's final audit all independently
  verified this), but even discounting it, the other two angles both read
  CONSISTENT (`0.1–10`), not the predicted DECOUPLED (`<0.1`) — a genuine,
  non-artifactual falsification against ten-plus cycles of convergent
  phase/interference-only evidence. A real sign-convention bug in
  `sections.widths()`'s `i_inc` for T28's `-x`-propagating geometry was
  found and fixed same-cycle (zero `lab/` diff); EM's Phase-5 review then
  found the identical geometry/defect pairing already existed, silently
  absorbed via ad hoc `abs()`-wrapping, since Iteration 2 (exp-024) — a
  historical-accuracy correction, not a new defect, applied same-shift.
  All five Phase-2 critiques (unanimous support-with-changes, zero
  overlap) and all six Phase-5 reviews (unanimous PARTIAL/CONCUR, zero
  overlap) independently verified; Red Team's Phase-5 final audit
  confirmed every finding from source. **New standing rule R13 adopted**:
  a ratio classifier whose denominator has real, knowable zero-crossings
  must be floor-gated on that denominator's own magnitude before a
  decade-threshold classification is trusted at a single sampled point —
  an algebraic instability (present even at zero measurement noise)
  distinct from the R5/R10 statistical-look-elsewhere lineage; does not
  fire on its own founding instance. **Checkpoint criterion 4 does NOT
  fire** on any of five independently-found, non-load-bearing matters (the
  corrected historical claim; a THIRD instance of the NETD/constraint-3
  disclaimer-erosion shape, closed same-shift — a new forward tripwire set:
  a fourth instance fires Checkpoint criterion 4 automatically; a vanished
  T9-anchor comparison plus a false "reproduced bit-exact this cycle"
  citation that survived five blind Phase-2 critiques and Red Team's own
  Phase-2 audit, caught only at Phase 5, logged as reinforcing R4's
  existing discipline rather than a new rule; an inverted `back_frac`/
  `fwd_frac` direction-label defect in `lab/sections.py::widths()` itself,
  flagged forward, non-blocking) — every one caught blind, same cycle,
  before the LOGBOOK entry. **Checkpoint criterion 2 N/A**, matching every
  T28 desk/instrument cycle since exp-069. **Tier 1 (near-unanimous next,
  cheap FDTD):** (1) the decisive 8-call bracketing follow-up at
  θ=38.4°/38.8° (QUANTUM's own proposal) — cheapest, fastest, single most
  decisive resolution of the node-artifact-vs-genuine-physics question;
  (2) extend the energy-interception channel to the full/denser 31-point
  window, scoring `σ_abs(C40,θ)`/`σ_abs(G40,θ)` individually, not merely
  their PAD-difference (MATERIALS' falsifiable "passive transducer, not
  resonant source" test); (3) apply R13's new denominator floor gate to
  this cycle's own already-collected 3-angle data and report the
  corrected classification (zero new FDTD). **Tier 2:** institutionalize
  the newly-validated extinction-routes-agreement identity for
  `graded_black_shell` obliquely as a permanent stage-8 suite row; extend
  the validated measurement to `PAIR_ABSORB40`/`C80−C40` and to 450/750nm;
  extend to the near-null σ(I) article (the class that actually matters
  for constraint-3 realizability); a bounded audit of whether any other
  cited T28 ratio construction shares R13's hazard, unguarded. **Tier 3,
  standing, carried forward unchanged:** PHOTONICS' grazing-incidence
  validity check on `edge_diffraction_c_empty_corrected` (still the single
  highest-ranked standing item on the whole T28 board, near-unanimous #1
  at Iteration 63's own close); the x-wall wavelength-generality leg, now
  **TWELVE** consecutive cycles deferred (076–087), the single oldest item
  on the whole T28 board; the still-queued full-scale (60,001-call)
  null-calibration re-run (2 of 3 parts done); R12-into-standard-practice;
  PHOTONICS' domain-truncation test for leg (b)'s Anchor 2 / EM's
  matrix-valued RS/Kirchhoff kernel rebuild; QUANTUM's lossless-PEC-only-
  disk control; hardening `lab/sections.py::widths()` itself to normalize
  by `abs(i_inc)` internally, with a new stage-8 gate on a synthetic
  -x-propagating scene (now TWO independent instances, exp-024 and
  exp-087, of this exact geometry tripping the same latent issue — scope
  as its own small, gated `lab/`-change proposal, not a same-shift patch);
  the still-unresolved ritualization governance question (named Iteration
  61). **Tier 4, governance:** Checkpoint criterion 2 ruled N/A; Checkpoint
  criterion 4 ruled not firing on five matters, reasoned individually; new
  standing rule R13 adopted; the historical-accuracy correction to the
  "first-ever `src_x>obj_x`" framing and the meta-observation that a bare
  rule-name citation ("(R4)") is not itself evidence of compliance, both
  logged as reinforcing existing R4 discipline. None of the above re-opens
  or re-proposes any RULED-OUT item (R1–R13). Full record:
  `experiments/087-t28-energy-interception-poynting-check/`, LOGBOOK.md
  Iteration 64.
- **[superseded by the Iteration-65 queue above — exp-086's own docket,
  retained as a pointer to its own history, not deleted]** exp-086
  (ELECTROMAGNETISM's rotation-lead cycle) fixed the R11 boundary-pinning
  defect at all three affected call
  sites (`free_period_with_widening` ×2 + the `_quiet` sibling, the
  Director's own scope extension beyond Phase 1's original two-file plan),
  re-scored exp-085's own Method C classification on the corrected
  machinery, extended the circular-shift null to all 37 sub-windows, and
  closed the quiet-variant's audit-coverage gap with a 10-seed-
  corroborated bit-identical "negligible effect" finding. **Method C
  re-score reproduced every frozen prediction exactly**: `frac_recovered=
  21/37=0.5676`, `classification_a=NOT STABLY PERIODIC` — exp-085's own
  "STRONG COHERENT CHIRP" is now dead by the automated pipeline itself.
  **New standing rule R12 adopted** (multi-seed corroboration required
  before reporting a fix's effect on a tail statistic as "negligible").
  **Checkpoint criterion 4 does NOT fire** on any of four cycle-produced
  near-misses (a scope-description self-contradiction across three
  documents; QUANTUM's single-seed gap, closed by replication within the
  same cycle; a promised-but-unexecuted Method-A re-fit, proven a
  mathematical no-op by construction; a Learned-section scope-erosion,
  corrected before LOGBOOK) — **explicitly conditioned** on a 4-item
  Tier-0 mandatory-fix docket landing first, which it did. **Checkpoint
  criterion 2 N/A**, matching every T28 desk cycle since exp-069.
  **New forward tripwire adopted**: the joint EM/THERMO energy-
  interception cross-check, now FOUR consecutive cycles deferred/exempt
  (083–086), SEVEN since first named (Iteration 59) — a FIFTH consecutive
  deferral without either a purpose-built article-loaded scene or an
  explicit retirement of the "next scene-bearing cycle" framing fires
  Checkpoint criterion 4 automatically; **Iteration 64 must address this
  directly, one way or the other, not defer a fifth time by default.**
  **Tier 1 (near-unanimous #1, six of seven seats):** (1) a dedicated,
  cheap, zero-FDTD validity check of `edge_diffraction_c_empty_corrected`
  at grazing incidence (θc≳45°) — PHOTONICS traced the model to source
  and confirmed no Fresnel-transition/UTD shadow-boundary correction term
  exists anywhere in the chain, and the sole recovered θc=57° point sits
  amplitude-comparable to the confirmed blow-up region; this gates
  whether ANY future classification built on Method C's grazing-angle
  sub-windows is physically meaningful at all, not merely a fit-quality
  question. (2) Transcribe R12's adoption and this cycle's own 10-seed
  compliance into standard practice for future tail-statistic claims.
  (3) Complete the still-queued full-scale (60,001-call)
  `null_calibration_appendix` re-run — run in two parts per Red Team's
  own reconciliation: (a) one N=60,001 run at exp-077's own originally-
  implied seed for an apples-to-apples update of the exact cited figure,
  AND (b) folded into the R12 multi-seed protocol rather than treated as
  sufficient alone (a large single N is still one draw of the order
  statistic). **Tier 2, the board's most overdue standing items:** (4) the
  energy-interception cross-check under its new forward tripwire, above
  — this cycle's own top governance priority; (5) the x-wall wavelength-
  generality leg, now **ELEVEN** consecutive cycles deferred (076–086),
  the single oldest item on the whole T28 board. **Tier 3, standing,
  carried forward unchanged:** (6) PHOTONICS' domain-truncation test for
  leg (b)'s Anchor 2, and/or EM's matrix-valued RS/Kirchhoff kernel
  rebuild; (7) the near-null σ(I) article follow-up, still not run; (8)
  QUANTUM's lossless-PEC-only-disk control, still not run; (9) the
  ritualization governance question named at Iteration 61, still not
  resolved. **Tier 4, governance:** (10) Checkpoint criterion 2 ruled
  N/A; (11) Checkpoint criterion 4 ruled not firing on four matters,
  reasoned individually, conditioned on the Tier-0 docket (delivered);
  (12) a governance observation, not yet a rule: the fourth consecutive
  T28 cycle with multiple dense, individually-non-firing Phase-5
  near-misses — healthy but worth tracking if a fifth cycle recurs. None
  of the above re-opens or re-proposes any RULED-OUT item (R1–R12). Full
  record: `experiments/086-t28-free-period-boundary-fix-rescore/`,
  LOGBOOK.md Iteration 63.
- **[superseded by the Iteration-64 queue above — exp-086's own docket,
  retained as a pointer to its own history, not deleted]** exp-085
  (MATERIALS' rotation-lead cycle)
  re-evaluated leg (a)'s exact model over a wide/dense window to ask
  whether the narrow 31-point window's own INCONCLUSIVE period-match
  (`P_model_a=2.5338°`) reflects a too-narrow sample or genuine
  non-stationarity. **Global instruments (Methods A/B) collapse cleanly to
  noise-scale**: `R²_wide=0.0128` sits at the 45th percentile of its own
  3900-shift circular-shift null, R5 specificity control clears 0/60
  targets, and the FFT's true global maximum (`P_fft_full=140.07°`) sits
  exactly at 2.0× the domain's own Fourier resolution floor -- genuinely
  uninformative, the cycle's one clean, fully-earned finding. **The local
  instrument (Method C) nominally filed "STRONG COHERENT CHIRP"**
  (`frac_recovered=1.000, spread=9.26, ρ=0.882`) but does not survive:
  two independent Phase-5 seats (MATERIALS, PHOTONICS) found and Red
  Team's final audit confirmed and quantified a silent boundary-pinning
  defect in `free_period_with_widening` (shared machinery, reused across
  ~15 T28 experiments since exp-077) that silently returns a
  non-convergent search's own worst candidate as if resolved, corrupting
  15/37 sub-windows concentrated at grazing incidence -- corrected
  `frac_recovered` drops to `0.595`, failing the ≥0.80 gate shared by
  every named positive classification, so **none is reachable from the
  as-filed data**. Two more independent seats (QUANTUM, VISION) found the
  37 sub-windows' 67% pairwise overlap invalidates the cited
  `ρ`-significance, and that NOTES.md's own "genuinely bimodal"
  null-contamination reading fails a formal binomial test (`p=0.754`).
  Red Team's own further synthesis: even the most defensible fallback
  (genuine periodicity confined to the near-normal quarter) is itself
  majority null-contaminated on the only direct sampled evidence
  available. **Combined Verdict: PARTIAL**, unanimous across all six
  blind Phase-5 seats and the final audit -- reported as **NOT STABLY
  PERIODIC** at this instrument's current reliability level, not "STRONG
  COHERENT CHIRP" as Phase 4 filed it; this forecloses nothing about
  genuine near-field structure near the aperture's own near-normal
  region, only what this cycle's own (defective, under-null-tested)
  instrument can currently certify. **New standing rule R11 adopted**
  (full text: LOGBOOK's RULED OUT registry) -- a boundary-pinned/
  non-convergent period-search result must be surfaced, never silently
  reported as resolved; binding forward on any future reuse of the
  affected machinery. **Checkpoint criterion 2 is N/A** -- reasoned
  explicitly (instrument-quality, not a phenomenon mechanism-class
  claim), matching every T28 desk cycle since exp-069. **Checkpoint
  criterion 4 does NOT fire** -- a close call, correctly weighed against
  every firing precedent's own distinguishing test: the defect was caught
  blind, independently, by two Phase-5 seats, within the same cycle,
  before any LOGBOOK entry existed; no currently-cited T28 number
  (`P_edge_A`, `P_model_a`) is corrupted; a bounded historical scan found
  the defect fired twice before (exp-078, exp-079), both inert. **Tier 1
  (near-unanimous #1, precondition for every other fix to mean
  anything):** (1) fix `free_period_with_widening`'s all-stages-boundary
  case in both files carrying the logic (`experiments/077-.../
  pad_round_trip_model.py`, `experiments/078-.../y_wall_prescreen.py`) --
  return the WIDEST stage's own value with an explicit
  `converged=False`/`no_interior_optimum=True` flag, never the narrowest
  silently -- and re-score Method C's classification (a) on the corrected
  machinery, reusing this cycle's own already-evaluated curve data; (2)
  in the same batch: extend the circular-shift null to all 37 Method C
  sub-windows (confirmed cheap, ~30s) and correct the Spearman
  significance for the 67%-overlapping windows (effective N≈12-13, not
  37); (3) a cheap, bounded audit of whether the boundary-pinning defect
  silently affected any OTHER prior T28 citation beyond the two (inert)
  instances exp-085's own audit found (exp-078, exp-079); (4) fix the
  mislabeled `rd_wide_fft` print statement in `phase4_derivation.py` and
  correct NOTES.md's "62.8%... of their mean" citation to the true
  mean-relative figure (91.6%) -- cosmetic, classification unaffected but
  should not stand now found; (5) persist per-stage/per-null elapsed
  times as JSON fields, not print-only. **Tier 2, standing, increasingly
  overdue items:** (6) the joint EM/THERMO energy-interception
  cross-check, in full, on the next scene-bearing T28 cycle -- now THREE
  consecutive cycles deferred/exempt (083 discretionary-partial, 084/085
  structurally exempt); (7) PHOTONICS' domain-truncation test for leg
  (b)'s Anchor 2 and/or EM's matrix-valued RS/Kirchhoff kernel rebuild;
  (8) the near-null σ(I) article follow-up, still not run; (9) QUANTUM's
  lossless-PEC-only-disk control; (10) the `PAIR_ABSORB40`/`C80−C40`
  extension; (11) the x-wall wavelength-generality leg, now **TEN**
  consecutive cycles deferred (076–085), the single oldest item on the
  whole T28 board; (12) a proper R3-grade settling convergence study with
  the article present. **Tier 3, governance:** (13) Checkpoint criterion
  2 ruled N/A; (14) Checkpoint criterion 4 ruled NOT firing, close call,
  reasoned explicitly; (15) new standing rule R11 adopted; (16) the
  ritualization question named at Iteration 61, still not resolved. None
  of the above re-opens or re-proposes any RULED-OUT item (R1–R11). Full
  record: `experiments/085-t28-leg-a-wide-window-period-pin/`, LOGBOOK.md
  Iteration 62.
- **[superseded by the Iteration-63 queue above — exp-085's own docket,
  retained as a pointer to its own history, not deleted]** exp-084 (PHOTONICS' rotation-lead cycle)
  built T28's first-ever genuine near-field Fresnel/Kirchhoff diffraction
  treatment of a boundary (the source aperture's own two tapered edges),
  not another reflection/echo model. **PRIMARY: leg (a) downgraded
  SUPPORT→INCONCLUSIVE on the period-match vs `P_edge_A=2.8421°`**
  (`P_model_a=2.5338°, R²=0.3697` fails the program's own harder-companion
  circular-shift null, `15/30=50.0%` of shifts meet or exceed it — the fit
  sits at the null's own median) — VISION's own T21-decorrelation escape
  test, run to its conclusion, independently mandates the identical
  downgrade by an unrelated route. **The surviving, genuinely new positive
  finding**: `corr(model, real FDTD C80(θ))=0.9582`, control-tested against
  three unrelated curves (`|r|<0.35`) and independently stress-tested two
  further ways this cycle (an aperture-width sensitivity sweep, `r`:
  `0.958→0.45` at a 1% perturbation; a circular-shift null on the
  correlation itself, `1/30=3.3%`, near-tied with the adjacent `+0.2°`
  lag — a signature of genuine spatially-coherent structure) — the first
  result in nine-plus T28 cycles showing a zero-FDTD vacuum construction
  track real FDTD physics this closely on any axis. **Leg (b) (article-rim
  vs `P*=2.9474°`) NO VERDICT** — its own pre-registered Anchor 2
  (composition-of-propagators identity) failed a convergence-checked test
  (stable `2.894–2.895×` mismatch, 1×–8× oversampling, ruling out
  discretization); ELECTROMAGNETISM's Phase-5 review then **proved
  algebraically** (`amb.weber`'s ratio construction cancels any global
  complex constant exactly, confirmed by direct execution) that a bare
  phase-factor fix is powerless — the real fix needs a genuinely
  position-and-observation-point-dependent RS/Kirchhoff kernel; PHOTONICS'
  own review named a third, cheaper, untested cause (intermediate-window
  truncation). **New standing rule R10 adopted**: a specificity-over-
  candidate-targets sweep is not a substitute for an order-preserving
  null-under-noise test — circular-shift-on-the-real-data is now the
  mandatory default (full text: LOGBOOK's RULED OUT registry) — the
  second consecutive cycle (exp-083's two-tone reversal, exp-084's own
  leg (a)) this exact divergence has been outcome-determining.
  **THERMODYNAMICS' proposed "Anchor 3" (fringe amplitude vs the flagship
  absorber's `R≤0.2%` reflectance ceiling) is real diagnostic evidence but
  NOT yet a commensurable comparison** — an R9-class gap (a zero-
  reflectivity Kirchhoff mask's fringe vs. an unrelated global reflectance
  fraction) — minimally fixed: scope to a construction with a genuine
  partial-reflection term, both operands from the identical
  `weber`/`window_means` pipeline. **Combined Verdict: PARTIAL**, unanimous
  across all six blind Phase-5 seats and the final audit. **Checkpoint
  criterion 2 is N/A** — matching every T28 desk cycle since exp-069.
  **Checkpoint criterion 4 FIRES — the 13th time this program** — on the
  energy-interception cross-check's third consecutive silent absence;
  Red Team's final audit sharpened the record to state precisely that,
  unlike exp-082's/exp-083's own genuinely discretionary silent misses,
  exp-084 had no article-loaded FDTD scene to run the full check against
  at all (a scope mismatch), crediting a same-shift partial discharge
  (the reflectance-ceiling sanity comparison). **VISION's blind Phase-5
  review named a significant governance concern — 13/13 consecutive
  "notification, not pause" firings — which Red Team's final audit
  adjudicated directly**: not itself evidence of toothlessness (the
  substantive defect is independently corrected same-shift in every one,
  by PANEL.md's own explicit design), but this specific firing exposes a
  real, fixable gap in the escalating-tripwire format (no clause
  distinguishing "chose not to" from "structurally could not") — **named
  as a standing Tier-3 governance item for this board, below, not
  resolved.** **Tier 0, zero FDTD, desk-only:** (1) transcribe R10's
  finalized text into LOGBOOK (done); (2) rescope Anchor 3 to a genuine
  partial-reflection construction, both operands from the identical
  pipeline; (3) the Checkpoint-4 LOGBOOK precision above (done); (4) **the
  ritualization item** — should the R6–R9/R10 escalating-tripwire format
  gain a scope-applicability clause before a 14th/15th/16th firing further
  dilutes the signal?; (5) leg (b)'s narrowed causal diagnosis (a bare
  phase factor is proven powerless; PHOTONICS' domain-truncation
  hypothesis and EM's matrix-valued kernel remain open); (6) log the
  shape-correlation finding's three independent stress tests together.
  **Tier 1, cheap FDTD, near-unanimous next:** (7) **QUANTUM's own
  zero-FDTD wide-window re-evaluation of leg (a)'s model period** — the
  single sharpest, cheapest next test, pinning `P_model_a`'s own
  asymptotic value with certainty rather than a p-value, independent of
  any 31-point sampling window's own null distribution; (8) PHOTONICS'
  domain-truncation test for Anchor 2 — cheaper than a kernel rebuild, a
  precondition for leg (b) ever producing a trustworthy verdict; (9) EM's
  own matrix-valued RS/Kirchhoff kernel rebuild, scoped as its own small
  pre-registered proposal, not a patch under time pressure; (10) the
  rescoped Anchor-3-compliant leg (b) rebuild (replace the opaque mask
  with a physically-scaled partial reflection), gated behind (8)–(9) —
  also the construction that would, for the first time, let MATERIALS
  assign a published/plausible/unobtainium verdict to the article-rim
  question. **Tier 2, standing, increasingly overdue items:** (11) **the
  joint EM/THERMO energy-interception cross-check, full form** — still not
  run, Checkpoint-4's own named cause, highest institutional priority for
  the first Iteration-62+ cycle with a real article-loaded FDTD scene to
  reuse; (12) the near-null σ(I) article follow-up, still not run, now the
  single most overdue realizability-adjacent item on the whole T28 board;
  (13) QUANTUM's own lossless-PEC-only-disk control, still open; (14) the
  `PAIR_ABSORB40`/`C80−C40` extension, still open; (15) the x-wall
  wavelength-generality leg (750/450nm), now **NINE** consecutive cycles
  deferred (076–084), the single oldest item on the whole T28 board; (16)
  a proper R3-grade settling convergence study with the article present.
  **Tier 3, governance:** (17) Checkpoint criterion 2 ruled N/A this cycle;
  (18) Checkpoint criterion 4 ruled FIRING, the 13th time, with the
  sharpened scope-mismatch framing; (19) **the ritualization question
  itself**, named as a standing board item. None of the above re-opens or
  re-proposes any RULED-OUT item (R1–R10). Full record: `experiments/084-
  t28-edge-diffraction-derivation/`, LOGBOOK.md Iteration 61.
- **[superseded by the Iteration-62 queue above — exp-083's own docket,
  retained as a pointer to its own history, not deleted]** exp-083
  (VISION SCIENCE's rotation-lead cycle) ran T28's first properly-powered
  article-loaded period
  discriminator (125 FDTD calls, full 31-point/0.2° `PAIR_PAD`-with-article
  re-test at 600nm), restoring the git-provenance discipline flagged as a
  two-cycle-old tripwire at Iteration 59's close (frozen predictions
  committed and pushed at `06cb96b`, strictly before any FDTD call).
  **PRIMARY: the three-branch period discriminator resolves decisively to
  BRANCH B** — `delta_scene(θ)`'s free period, `P*=2.9474°, R²=0.8582`, is
  3.7% from `P_edge_A=2.8421°` (T28's own original `C80−C40` period), far
  from `P_continuity=4.611°` (36% off) and `P_edge_B=1.9608°` (50% off), and
  clears the MAXIMUM of a 20,000-trial null-permutation control (`p=0.0`) —
  doubly corroborated by EM's independent field-difference companion
  (`P*=2.5865°`, own `p=0.00185`). The first time in nine-plus T28 cycles
  the article-loaded channel's own dominant periodicity has been
  statistically pinned. **But the CAUSAL label does not survive scrutiny,
  twice over**: Red Team's Phase-2 audit (adopting PHOTONICS'/MATERIALS'
  own findings) ruled Branch B is a period-family MATCH, not a demonstrated
  mechanism — `P_edge_A` is T28's own founding, still-unexplained
  periodicity (nine-plus prior mechanism-search cycles have REFUTEd every
  domain-echo candidate for it), PHOTONICS' own far-field two-rim estimate
  misses by 3.3×, and this aperture's own Fresnel number (`N_F≈13`) means
  the far-field formula wasn't even the right regime; Red Team's Phase-5
  final audit sharpened this further — **`P_edge_A` was originally
  established on a scene independently confirmed to contain ZERO article/
  materials calls of any kind** (`experiments/069-.../run.py`) — an
  Occam's-razor argument favoring "inherited pre-existing artifact" over
  "genuine article-rim diffraction," without yet proving it. **A two-tone
  `PAD`-continuity admixture claim, independently raised by QUANTUM's and
  EM's own Phase-2 critiques (Freedman-Lane permutation, `p<0.001`), was
  REVERSED by Red Team's Phase-2 audit** under the correct, order-
  preserving circular-shift companion (`p=0.581`/`p=0.097`) — the
  underlying residuals are highly autocorrelated (lag-1 `r≈0.93–0.95`,
  matching a previously-documented exp-074 pattern), invalidating the naive
  null's exchangeability assumption, independently reconfirmed four times.
  **EM's own Phase-5 attempt to rescue the admixture claim with a
  wrap-free AR(1)-parametric surrogate (`p=0.766`) does NOT itself
  reproduce** — Red Team's Phase-5 final audit independently rebuilt it
  from scratch across five structural variants and got `p≈0.09–0.10`
  instead (materially weaker, not stronger); EM's qualitative critique of
  circular-shift is retained, its specific number is not — the first
  Phase-5 figure this cycle's own layered verification caught failing R4.
  **Combined Verdict: PARTIAL**, unanimous across all six blind Phase-5
  seats and both Red Team audits. **Checkpoint criterion 2 is N/A — not
  merely not-yet-ripe**: artifact-attribution/null-construction work
  internal to the lab's own instrument, unconnected to any phenomenon-
  program constraint, reasoned through explicitly despite this cycle's own
  genuine methodological depth. **Checkpoint criterion 4 does NOT fire** on
  any of three matters adjudicated (the causal-label/two-tone overclaims,
  both caught within Phase 2; EM's own unreproduced AR(1) figure, caught
  within Phase 5) — all closed same-shift. The joint EM/THERMO energy-
  interception cross-check is now a **two-cycle-old named-but-deferred
  pattern** (Iteration 59's close; this cycle's own scoping) — approaching,
  not yet at, the R8-family tripwire; a third consecutive deferral without
  an explicit reason fires it. **Tier 0, zero FDTD, desk-only:** (1) log
  the AR(1) non-reproduction finding wherever the admixture question is
  next cited; (2) log `P_edge_A`'s own empty-scene provenance as a
  standing, source-verified fact; (3) state MATERIALS' "zero realizability
  content" rule precisely — genuinely open, but the evidence now leans the
  prior toward the rule's original reading, not a symmetric question; (4)
  log the energy-interception two-cycle pattern; (5) the R5 pre-
  registration discipline note, now four cycles running. **Tier 1, cheap
  FDTD, near-unanimous next:** (6) **MATERIALS' article-radius (`R_OUT`)
  discriminator — the single highest-value item on the board (ranked #1 or
  #2 by all six Phase-5 seats), UPGRADED per Red Team's own cross-cutting
  attack on the six-way consensus** — pre-register AT LEAST TWO alternate
  radii (e.g. `R_OUT∈{50,100}` alongside the existing 78 baseline,
  geometrically confirmed feasible without domain resizing), not the
  single radius every review that names it specifies, so the outcome can
  distinguish a genuine scaling trend from a coincidental shift; pre-
  register the "period stays pinned" directional prior explicitly before
  running; (7) **PHOTONICS' own zero-FDTD Fresnel/Kirchhoff edge-
  diffraction desk derivation**, applied FIRST to the empty-scene geometry
  where `P_edge_A` actually originates, then to the article's own rim as a
  cheap second comparison — the first attempt in nine-plus prior mechanism
  cycles to model a T28 boundary as a genuine diffractor rather than a
  reflector; if it succeeds on the empty scene, item 6's own sweep can be
  scored against a quantitative prediction, not a bare direction; (8) a
  committed, independently-reproduced AR(1)-matched null-calibration test
  for the two-tone admixture question (QUANTUM's own fully-specified
  design — measure `φ̂`, generate synthetic H0 data, sweep `φ̂`, inject
  known admixture amplitudes to characterize power) — MUST reconcile with
  Red Team's own non-reproduction of EM's earlier AR(1) figure before
  either number is treated as final. **Tier 2, standing, increasingly
  overdue items:** (9) the near-null σ(I) article follow-up, still not
  run; (10) QUANTUM's own lossless-PEC-only-disk control, still open; (11)
  the `PAIR_ABSORB40`/`C80−C40` extension, still open; (12) the x-wall
  wavelength-generality leg (750/450nm), now **EIGHT** consecutive cycles
  deferred (076–083), exceeding every other item's own pre-tripwire streak
  on this board — should not be deferred again without an explicitly
  stated reason; (13) a proper R3-grade settling convergence study with the
  article present. **Tier 3, governance:** (14) Checkpoint criterion 2
  ruled N/A this cycle, reasoned through explicitly, not by pattern-match;
  (15) Checkpoint criterion 4 ruled non-firing on all three matters this
  cycle adjudicated; (16) the energy-interception item's own two-cycle
  pattern, logged explicitly as approaching — not yet at — the R8-family
  tripwire. None of the above re-opens or re-proposes any RULED-OUT item
  (R1–R9). Full record: `experiments/083-t28-pad-article-full-power-
  retest/`, LOGBOOK.md Iteration 60.
- **[superseded by the Iteration-61 queue above — exp-082's own docket,
  retained as a pointer to its own history, not deleted]** exp-082
  (QUANTUM OPTICS' rotation-lead cycle) discharged
  PLAN.md's own six-cycle tripwire on the PAD-loaded real-article check —
  the FIRST article-loaded FDTD measurement in this nine-cycle-plus T28
  sub-thread's history. Loaded the established flagship absorber
  (`materials.graded_black_shell`+`pec_disk`) into `dg065.CONFIGS["C40"]`/
  `["G40"]` (`PAIR_PAD`) at 7 angles (36°–42°, 1° step, 600nm). **Primary
  metric: `ratio=A_scene/A_empty=0.6573`, VERDICT SURVIVES, stands
  MECHANICALLY** — decisive, bit-exact, centrally inside the pre-registered
  `[0.5,2.0]` band, scoped to the flagship article class only. **The
  substantive mechanism-continuity question — whether this is the SAME
  lossless phase effect Iteration 53 characterized on the empty scene, or a
  qualitatively different article-mediated interaction — is demonstrated,
  not merely left open, to be UNRESOLVABLE at this cycle's own 7-point
  statistical power**: PHOTONICS and ELECTROMAGNETISM, independently,
  computed the Pearson correlation between `delta_scene(θ)` and
  `delta_empty(θ)` (`r≈0.031`, essentially zero); Red Team's Phase-2 audit
  went further — an exact permutation test gives `p=0.953`; the two series'
  own best-fit periods diverge 190%; a ground-truth check shows the same
  machinery recovers the WRONG period (78% off) for a signal of
  independently-known period; a 200,000-trial null-permutation control
  shows the achieved `R²≈0.86` is common under pure noise at this n. QUANTUM's
  own Phase-5 review contributed a genuinely new finding — a `~90°`
  phase-shift of a sinusoid at `PAIR_PAD`'s own true period reproduces the
  observed `r≈0.031` almost exactly — but Red Team's Phase-5 final audit
  extended it with a specificity test: **99.3% of arbitrary candidate
  periods admit an equally good phase match**, correctly read as a strong
  argument FOR the full 31-point test next, not as evidence for mechanism
  continuity. **Combined Verdict: PARTIAL** (five of six blind Phase-5
  seats and the final audit; QUANTUM's own outlier PROMISING label
  substantively described the same facts, adjudicated explicitly as a
  vocabulary mismatch, not carried to the permanent record). Two rider
  items also ran: the x-wall realizable-admittance refit (MATERIALS'
  restored item — 2 of 4 cells flip, none to SUPPORT, REFUTE-leaning
  picture stands) and the FDTD phase-convention tie-breaker extended to
  `[47.5°,54.5°]` (self-scored GENUINELY INCONCLUSIVE — the calibration
  reliability precondition fails at this angle range, a new,
  angle-range-dependent instrument-reliability finding). **Checkpoint
  criterion 2 (mechanism-class boundary) is N/A this cycle — not merely
  not-yet-ripe** — instrument-fidelity work, no mechanism-class claim made
  anywhere. **Checkpoint criterion 4 does NOT fire**, on two matters: the
  Phase-2 fix-docket adoption (confirmed landed) and a git-provenance
  pattern (predictions committed after a run already mostly complete) now
  **TWO consecutive cycles** running (exp-081, exp-082) — **a third
  consecutive recurrence at Iteration 60 fires Checkpoint criterion 4
  outright, not weighed as a close call again.** **Tier 0, zero FDTD,
  desk-only:** (1) log MATERIALS' zero-realizability-content framing rule
  (this whole confound is a scene/domain-geometry fact, never a materials
  realizability question); (2) EM's/THERMODYNAMICS' joint energy-
  interception cross-check (a tighter Poynting/interception bound on this
  cycle's own article-loaded geometry, reusing the flagship's own
  established extinction figures); (3) log the git-provenance pattern as
  the two-cycle-old tripwire above; (4) record both refinements of the
  phase-shift finding (two symmetric solutions; non-specific across 99%+ of
  candidate periods) wherever next cited. **Tier 1, cheap FDTD,
  near-unanimous next, bundle together:** (5) **the full 31-point/0.2°
  `PAIR_PAD`-with-article re-test at 600nm** — the single highest-value
  item on the board (ranked #1 by PHOTONICS, THERMODYNAMICS, QUANTUM),
  pre-register PHOTONICS' own two-branch period prediction (article-edge
  diffraction at `4.611°` vs. the T21/T28-family `~1.96°–2.84°` vs.
  "neither established family") BEFORE running, bundling in EM's own
  field-difference decomposition (`ΔE_article=E_with−E_without`, persist
  the raw `observer_profile` arrays for both legs) at zero marginal FDTD
  cost; (6) the near-null σ(I) article follow-up (`off_pass`,
  `τ_off≈0.0065`, exp-032/034) — MATERIALS' own flip condition,
  near-universal top-2 pick across all six seats; (7) QUANTUM's own
  lossless-PEC-only-disk control (`pec_disk` alone, no `graded_black_shell`,
  14 new calls) — tests whether persistence depends on the article's own
  absorption specifically or on its presence as any coherent scatterer; (8)
  extend the real-article check to `PAIR_ABSORB40`/`C80−C40` — tests
  whether SURVIVES is specific to the `PAD` axis or general to any
  boundary-tied confound. **Tier 2, standing, increasingly overdue items:**
  (9) the x-wall wavelength-generality leg (750/450nm), now **SEVEN**
  consecutive cycles deferred (076–082) — its own streak now exceeds item
  7's own pre-tripwire streak; should not be deferred again without an
  explicitly stated reason; (10) the 750nm x-wall two-wall spot-check,
  still the single oldest-unexecuted item on the whole T28 board; (11)
  broadband pulsed reflectance spectroscopy of the `ABSORB` boundary; (12)
  a proper R3-grade settling convergence study with the article present (2
  of 14 config×angle cells tested to date). **Tier 3, governance:** (13)
  Checkpoint criterion 2 ruled N/A this cycle, not merely not-yet-ripe;
  (14) Checkpoint criterion 4 ruled non-firing on both matters this cycle,
  one closed, one flagged forward as the two-cycle-old tripwire above; (15)
  QUANTUM's PROMISING verdict is a vocabulary ruling, not an override of
  any computation — the substantive finding fully retained and credited.
  None of the above re-opens or re-proposes any RULED-OUT item (R1–R9).
  Full record: `experiments/082-t28-pad-real-article-check/`, LOGBOOK.md
  Iteration 59.
- **[superseded by the Iteration-60 queue above — exp-081's own docket,
  retained as a pointer to its own history, not deleted]** exp-081
  (THERMODYNAMICS' rotation-lead cycle) finally built PHOTONICS' own
  total-field construction
  (`E_direct+r(90°−θ_beam;ABSORB)·W`) exactly as originally specified and
  scored it via the free-period fit against REAL T28 reference periods —
  the actually-decisive test this nine-cycle sub-thread has needed since
  exp-069. **Combined Verdict NEITHER, mechanically** (1 SUPPORT —
  `C80−C40`, `rel_dev=0.2910` — + 2 INCONCLUSIVE + 0 REFUTE) — **REFUTE-
  leaning substantively and DECISIVELY, not merely asserted**: Red Team's
  Phase-2 audit's own reflectance-ablation control (`r(90°−θ_beam)→1`)
  proved, pair-specifically, that `C80−C40`'s lone SUPPORT survives
  deleting 100% of the wall's reflectance almost unchanged (`0.2910→
  0.2937`) while `PAIR_ABSORB40` — the pair genuinely dependent on real
  wall reflectance — still misses badly (`rel_dev=0.5139`) even with real
  reflectance present. Independently re-verified from primitives at least
  nine times across this cycle's own record (five Phase-2 critics, Red
  Team's Phase-2 audit, six Phase-5 blind reviews, Red Team's Phase-5
  final audit). Robust to admittance family (matched vs. realizable
  `μ_r=1`, shift `≤0.0075°`, not outcome-determining — this construction's
  own `[47.5°,54.5°]` range carries an order-of-magnitude-smaller
  matched-vs-realizable phase divergence than exp-080's part(b) precedent)
  and to the `r`-vs-`conj(r)` sign convention (zero verdict flips, though
  the TRUE convention at this range remains genuinely open empirically,
  queued not resolved). This is a genuine **third** independent negative
  finding against the plane-wave/global-steering coherent-echo mechanism
  class, joining exp-078's single-edge and exp-079's full-aperture-sum
  structural forecloses. The energy budget (THERMODYNAMICS' own item 3)
  confirms this construction family could never matter to constraint 3 in
  absolute terms: the honest `theta_local`-convention bound (`~1.3×10⁻⁸`)
  is ~116,000× tighter than the naive `90°−θ_beam`-convention anchor used
  as the headline figure. **Checkpoint criterion 2 (mechanism-class
  boundary) remains NOT YET RIPE — narrowed for a THIRD consecutive
  cycle**: single construction, one wavelength, empty scene, one
  genuinely open verification gap (the real FDTD phase-convention check).
  **Checkpoint criterion 4 does NOT fire**, on two distinct governance
  findings Red Team's Phase-5 final audit adjudicated explicitly: (i)
  VISION's Phase-5 finding that PLAN.md's own twice-escalated instruction
  — a sixth deferral of the PAD-loaded real-article check "must again be
  stated explicitly in that cycle's own synthesis" — was not met in
  `phase3_synthesis.md`; the audit itself supplied the missing reason,
  closing the gap same-shift, but flagged this as **the second
  consecutive T28 cycle** the instruction was not fully met, with a
  written tripwire: a third consecutive miss "would no longer be a close
  call... I would expect it to fire criterion 4 outright." (ii)
  MATERIALS' Phase-5 finding that the x-wall realizable-admittance refit
  — named explicitly in three consecutive iterations' own rankings
  (54→55→56) — silently vanished from exp-080's own Iteration-57
  reconciled ranking with no stated disposition; a backlog-tracking
  omission, not a substantive false claim, ruled a different and
  lower-stakes failure kind than any prior R4/R6/R7/R8/R9 firing
  precedent, restored to this board (item 1, below) rather than left
  silent a fourth cycle. **Tier 0, zero FDTD, desk-only:** (1) restore or
  explicitly retire the x-wall realizable-admittance refit (MATERIALS'
  restored item — reuse `d80.reflection_coefficient_vec_realizable`
  against the already-built exp-075/exp-077 x-wall models, or state why
  their already-wide REFUTE margins make that unnecessary); (2)
  THERMODYNAMICS' hygiene bundle (a local "post-run analytic, zero FDTD"
  docstring label on `item3_energy_budget()`, the ABSORB=40-worst-case-
  across-all-depths table into `NOTES.md`, an explicit 600nm-only
  qualifier on item 3's headline sentence); (3) record, wherever this
  cycle's stress tests are next cited, that they comprise three genuinely
  independent lines of evidence (admittance family, ablation, ablation-
  constant phase), not four — the `conj(r)` check is substantially a
  corollary of the ablation check for `C80−C40` specifically (EM's own
  Phase-5 finding), not a fully separate confirmation. **Tier 1, cheap
  FDTD, next:** (4) extend the empirical FDTD phase-convention tie-breaker
  (`phase5_redteam_phase_convention_check.py`'s own idiom, exp-075's
  `[0°,20°,39°]` precedent) to 2–3 angles inside `[47.5°,54.5°]` — the
  single remaining genuinely open verification question, near-unanimous
  top pick (EM #1, QUANTUM #1, PHOTONICS #2, VISION #2); (5) broadband
  pulsed reflectance spectroscopy of the `ABSORB` boundary; (6) the 750nm
  x-wall two-wall spot-check — the single oldest-unexecuted item on the
  whole T28 board. **Tier 2, the board's two most overdue items, strongest
  cross-seat consensus of any single item this cycle:** (7) **the
  PAD-loaded real-article check — now SIX consecutive T28 cycles deferred
  (076–081)**, ranked #1 by VISION and THERMODYNAMICS, #2 by MATERIALS,
  EM, and QUANTUM — the only queued item that tests whether ANY of this
  nine-cycle sub-thread's findings, this cycle's sharpened REFUTE-leaning
  result included, bear on a scene with a real absorbing article rather
  than free-space domain-boundary geometry alone. **If Iteration 59
  defers this a seventh time, the reason must again be stated explicitly
  in that cycle's own synthesis — a third consecutive miss on this exact
  requirement fires Checkpoint criterion 4 outright, not weighed as a
  close call again.** (8) **the 750/450nm x-wall wavelength-generality
  leg — also SIX consecutive cycles deferred**, ranked #1 by PHOTONICS
  and MATERIALS from their own charter vantage (wavelength/angle
  coherence; dispersive realizability) — every quantitative finding this
  cycle produced is single-wavelength (600nm) evidence. **Tier 3,
  governance:** (9) Checkpoint criterion 2 ruled NOT YET RIPE this cycle,
  narrowed a third consecutive cycle — items 4, 7, and 8 above are what
  would actually make it ripe; (10) Checkpoint criterion 4 ruled
  non-firing this cycle on both governance findings, conditioned
  explicitly on this cycle's own fix docket being what Iteration 58's
  LOGBOOK entry inherits, with an explicit forward tripwire on item 7.
  None of the above re-opens or re-proposes any RULED-OUT item (R1–R9).
  Full record: `experiments/081-t28-photonics-construction-total-field/`,
  LOGBOOK.md Iteration 58.
- **[superseded by the Iteration-59 queue above — exp-080's own docket,
  retained as a pointer to its own history, not deleted]** exp-080 (EM's
  rotation-lead validity pre-check) found (a)
  FORECLOSE on the Fraunhofer-margin/`theta_local`-spread test, robust
  across the full 3-λ sweep; (b) admittance-family-dependent on the
  single-effective-angle reproduction test (INCONCLUSIVE matched, mean
  `R²=0.7345`; **REFUTE** realizable `μ_r=1`, mean `R²=0.4305`, two
  configs negative, surviving a robustness check); (c) QUANTUM's blind
  Phase-2 critique built PHOTONICS' own not-yet-built §4 plane-wave
  construction (zero new FDTD) and found the SAME zero-crossing pathology
  at a WORSE floor (scale-corrected mean `R²=0.602`, min `0.085`) — but
  Phase 5 (QUANTUM again, confirmed by Red Team's final audit against the
  primary source) found this was scored by the WRONG methodology (an `R²`
  shape-comparison against exp-079's own already-discredited candidate
  curve, not the free-period fit against REAL T28 periods PHOTONICS
  actually specified) and is missing `E_direct` — which PHOTONICS' own
  Phase-5 review then proved, from primitives, cancels bit-identically
  across every congruent config (a coordinate substitution `u=y_s−OBJ_Y`
  makes every ingredient PAD-invariant by the congruent series' own
  design). **Every ingredient for the actually-decisive test now exists,
  for the first time in this nine-cycle sub-thread.** Red Team's Phase-5
  final audit explicitly corrected an overconfident "does not clear a
  bar" framing (part (d) carried no scored `verdict` field and was never
  run against real data) before it could reach LOGBOOK.md as though it
  were a completed test. **Checkpoint criterion 4 does NOT fire** (a
  closer call than exp-079's own Iteration-56 precedent — three
  concentrated near-misses caught and corrected within this same Phase-5
  layer, conditioned explicitly on the corrected framing being what is
  inherited forward). **Checkpoint criterion 2 ruled NOT YET RIPE**, more
  precisely specified: the free-period fit of the total field against real
  T28 periods has never been run, though every ingredient for it now
  exists. **Tier 0 — zero FDTD, run as one batch, in order:** (1) **build
  the construction PHOTONICS actually specified, scored the way PHOTONICS
  actually specified** — total field `E_direct(θ_beam)+r(90°−θ_beam;
  ABSORB)·W(θ_beam)`, with `E_direct` now derived and proven to cancel in
  every needed pair-delta (cite PHOTONICS' own exp-080 Phase-5 formula,
  do not re-derive it), scored via `_free_period_search`/staged-widening
  against the REAL T28 reference periods (`experiments/076-.../
  results.json::headline`), under a FRESH SUPPORT/INCONCLUSIVE/REFUTE
  band **committed to git BEFORE running it** — the single highest-value
  item on the board, now fully specified for the first time; retire or
  clearly re-label `part_d_photonics_construction()`'s own note to state
  plainly it was a partial, image-only, non-authoritative draft superseded
  by this build; (2) **cheap precondition (EM):** re-run
  `gate_lossless_unimodular_range`/`gate_single_layer_identity_range`/
  `gate_passivity_range` over `[47.5°,54.5°]` before trusting
  `reflection_coefficient_vec` at this range in item 1's own build —
  currently only hand-checked in a Phase-5 review (`|r|≤0.0853`,
  passivity holds), not committed as a gate; (3) **THERMODYNAMICS:** price
  the geometric-interception × material-reflectivity energy budget — the
  still-missing third quantity for constraint 3's own bookkeeping (neither
  part (b)'s nor part (c)/(d)'s `|r|²` alone answers what fraction of
  total scene power the echo path could actually carry; even a crude upper
  bound, ≤0.15% before any interception factor at ABSORB=40, resolves
  whether this construction family could ever matter to constraint 3 in
  absolute terms); (4) **hygiene, fold into item 1's own edit
  (MATERIALS):** fix `reflection_coefficient_vec_realizable()`'s docstring
  (`mu_r=ni^2`→`mu_r=ni`); state explicitly that the realizable number, not
  the matched one, is the only one that could ever describe a real
  material; state explicitly (EM) that a valid global-angle y-wall
  construction needs an angle convention built from `theta_local(y_s)`'s
  own fixed-observer geometry, not a borrowed `θ_beam`-steering
  convention — resolving the near-field problem alone will not fix this.
  **Tier 1 — cheap FDTD, next:** (5) the real 750/450nm
  wavelength-generality x-wall leg — now deferred FIVE consecutive T28
  cycles (076–080); (6) broadband pulsed reflectance spectroscopy of the
  `ABSORB` boundary — deferred five consecutive cycles; (7) the 750nm
  x-wall two-wall spot-check — the single oldest-unexecuted item on the
  whole T28 board. **Tier 2 — now the single most overdue item on the
  whole T28 board:** (8) whether the `PAD`-sensitivity axis survives with
  a real absorbing article loaded — deferred FIVE consecutive cycles
  (076–080), each cycle's own ranking naming it explicitly and declining
  to run it; every congruent-series config to date, across nine T28
  cycles, is an EMPTY scene. **If Iteration 58 defers this a sixth time,
  the reason must again be stated explicitly in that cycle's own
  synthesis**, against this cycle's own finding (item 1 is now fully
  specified and cheap; this item remains the only one that tests
  real-world relevance at all), not by inertia. **Tier 3 — governance:**
  (9) Checkpoint criterion 2 (mechanism-class boundary) ruled NOT YET RIPE
  this cycle, more precisely specified than before — item 1 above is the
  test that would actually settle it; (10) Checkpoint criterion 4 ruled
  non-firing this cycle, conditioned explicitly on this cycle's own
  corrected framing (not the pre-Phase-5 "does not clear a bar" language)
  being what Iteration 58 and LOGBOOK.md actually inherit. None of the
  above re-opens or re-proposes any RULED-OUT item (R1–R9). Full record:
  `experiments/080-t28-y-wall-planewave-validity-precheck/`, LOGBOOK.md
  Iteration 57.
- **[superseded by the Iteration-58 queue above — exp-079's own docket,
  retained as a pointer to its own history, not deleted]** exp-079 computed the full, non-edge-reduced y-mirrored
  aperture sum: the flat/zero-amplitude result exp-078's single-edge model
  found does NOT survive (`ss_tot` ratio `9.4×10⁻⁷`, real signal,
  convergence-checked), but the recovered `theta_beam`-dependence is
  structurally, not merely empirically, incapable of discriminating a
  real y-wall echo, at ANY period, from no echo at all — both the
  per-point bounce angle and the image propagation distance are
  `theta_beam`-independent by construction, so `E_echo`'s entire
  `theta_beam`-dependence is the spatial Fourier transform of a fixed
  envelope, governed by the shared aperture window's own T21-family
  content regardless of the wall's true reflectance (independently
  confirmed three ways at Phase 2 — EM analytically, QUANTUM empirically
  via a committed reflectance-ablation control, Red Team's own from-
  scratch re-run — and re-confirmed at Phase 5 against a SECOND,
  materially different admittance family, MATERIALS' realizable-admittance
  re-run: every scored period shifts `≤0.015°`, no verdict flips). **Tier
  0 — zero FDTD, run as one batch:** (1) EM's cheap validity pre-check of
  the recommended plane-wave/global-steering y-wall construction (the
  Fraunhofer-margin calculation, already computed; a not-yet-run
  "does any single effective angle reproduce the full per-point coherent
  sum's own envelope structure to a stated tolerance" test), run BEFORE
  building it, immediately followed by PHOTONICS' own concrete build (one
  new glue function, reusing already-gated machinery unchanged,
  pre-registering PHOTONICS' own prediction — dominant period likely still
  T21-proximate, the informative result is the offset from T21 and whether
  it tracks `ABSORB`/`PAD` — and THERMODYNAMICS' own suggestion to report
  `1−|r(θ_beam)|²` as an actual reflected-power fraction) if the pre-check
  does not foreclose it — the single highest-value item on the board, the
  only construction in this seven-cycle sub-thread not structurally
  guaranteed by exp-079's own central finding to fail; (2) a more targeted
  realizable-admittance smoothness check at this cycle's own full
  `[4.77°,15.50°]` envelope (an absolute check, not merely correlation
  with the matched model); (3) the still-unexecuted x-wall realizable-
  admittance refit — the single oldest-deferred MATERIALS item on the
  whole board, three cycles running; (4) a period confidence band for
  exp-079's own T21-proximity claim (Cramér–Rao or residual bootstrap);
  (5) derive the taper's own diffraction overtone against PHOTONICS'
  2.55° residual sideband (low priority, five orders of magnitude too
  small to matter to T28's real signal regardless); (6) exp-079's own
  five-item record-hygiene docket (done, Iteration 56). **Tier 1, cheap
  FDTD:** (7) the full-width non-aliased second-wavelength `G40` leg (now
  deferred FOUR consecutive cycles: exp-076, -077, -078, -079); (8)
  broadband pulsed reflectance spectroscopy of the `ABSORB` boundary
  (deferred four consecutive cycles); (9) the 750nm x-wall two-wall
  spot-check (the single oldest-unexecuted item on the whole T28 board).
  **Tier 2 — now the single most overdue item on the whole T28 board:**
  (10) whether the `PAD`-sensitivity axis survives with a real absorbing
  article loaded — deferred FOUR consecutive cycles (exp-076 through
  exp-079), each cycle's own ranking naming it explicitly and each
  declining to run it; every congruent-series config to date, across
  eight T28 cycles, is an EMPTY scene — this is the only queued item that
  would tell the program whether this eleven-cycle sub-thread has any
  downstream relevance to constraint 3 at all. Iteration 56's own
  synthesis finally supplied the explicit scheduling reason exp-078's own
  ranking demanded (`experiments/079-.../phase3_synthesis.md` §4b: this
  cycle's own scope was Tier-0 item 1, real FDTD work was never budgeted
  there) — **but the underlying deferral itself continues; if Iteration
  57 defers this a fifth time, the reason must again be stated explicitly
  in that cycle's own synthesis.** **Tier 3 — governance:** (11)
  Checkpoint criterion 2 (mechanism-class boundary) ruled NOT YET RIPE
  this cycle — two reductions within the coherent-echo class (single-edge,
  exp-078; full-aperture-sum, exp-079) are now foreclosed by structural
  argument against two admittance families, but the plane-wave/global-
  steering construction, the x-wall realizable-admittance refit, and the
  wavelength-generality leg remain genuinely open. None of the above
  re-opens or re-proposes any RULED-OUT item (R1–R9). Full record:
  `experiments/079-t28-y-wall-full-aperture-sum/`, LOGBOOK.md Iteration
  56.
- **[superseded by the Iteration-57 queue above — exp-078's own docket,
  retained as a pointer to its own history, not deleted]** exp-078's
  y-wall echo pre-screen is INCONCLUSIVE (Test-A-only,
  0/3 SUPPORT, 0/3 REFUTE) under the geometrically corrected `90-theta`
  angle — sharpened further by Red Team's own Phase-5 finding that the
  SAME edge-image/single-near-wall reduction, evaluated at its own
  physically rigorous (per-config-constant, `theta_beam`-independent)
  stationary-phase bounce angle, predicts EXACTLY ZERO oscillatory signal
  (`ptp=0.000°`, all five configs) — a decisively stronger negative than
  an ordinary INCONCLUSIVE, but NOT the closing of the y-wall mechanism
  class (Checkpoint criterion 2 ruled not yet ripe; the full non-edge-
  reduced aperture sum and the far-wall pair remain untested). **Tier 0 —
  zero FDTD, run as one batch:** (1) **does the flat/zero-signal result
  generalize from the single-edge reduction to the FULL, non-edge-reduced
  y-mirrored aperture sum?** (merges EM's and QUANTUM's own picks,
  sharpened by Red Team's own audit into a concrete, answerable question)
  — each aperture point has its own per-point rigorous bounce angle
  (unlike the single-edge case's shared constant); `phase1_proposal.md`'s
  own §3.2 stationary-phase argument already predicts edge-domination
  should hold for the full sum too, but this is a prediction, not yet
  computed — the single most information-dense item on the whole T28
  board: if it confirms, the y-wall self-echo-off-the-near-wall
  coherent-echo sub-class is close to formally exhausted at the desk
  level, without ever writing the full propagator; if it does NOT
  generalize, that is itself the discovery of genuine `theta_beam`-
  dependence this seven-cycle sub-thread has never found evidence for,
  and would justify the full build for the first time. (2) this cycle's
  own record-hygiene docket (DONE, LOGBOOK.md Iteration 55 — listed here
  only for completeness). (3) **retarget the still-unexecuted
  realizable-admittance (`mu_r=1`) refit at the X-WALL's own two-wall
  model**, not the y-wall (MATERIALS' own re-ranking, confirmed by Red
  Team: the y-wall's period is admittance-choice-invariant, Pearson
  `r>0.9997`; the x-wall's own marginal Test-B numbers, `r²=0.0001–0.0418`
  from exp-077, remain the only place this substitution could plausibly
  move a verdict) — carried unexecuted from exp-077's own Iteration-55
  ranking, still not run two cycles later. (4) the Fisher-combined
  omnibus statistic (DONE, this shift — listed for completeness). (5)
  **gate the already-collected 750nm two-wall x-wall spot-check** with a
  properly-sized null and decide — the single oldest deferred item on the
  whole T28 board, carried unexecuted from exp-077's own ranking through
  exp-078 unchanged. (6) the `ss_tot`-scale sanity guard (DONE, this
  shift — listed for completeness). (7) **pre-register the amplitude/
  normalization convention for any future Test-B build, BEFORE it is
  built** (VISION's own forward R9 guard) — cheap, documentation-only,
  directly forecloses a fourth instance of R9's own failure shape in this
  exact sub-thread. **Tier 1 — cheap FDTD, next:** (8) the full-width,
  non-aliased second-wavelength (`G40`) leg (QUANTUM — the standing
  precondition, now deferred across THREE consecutive cycles: exp-076,
  exp-077, exp-078) — the cheapest remaining FDTD test of whether T28's
  periodicity is a real, wavelength-scaling-consistent physical effect at
  all, independent of which mechanism is being chased. (9) broadband
  pulsed reflectance spectroscopy of the `ABSORB` boundary
  (THERMODYNAMICS, carried from Iteration 53). **Tier 2 — the standing
  charter-relevant test:** (10) **test whether the `PAD`-sensitivity
  survives with a real absorbing article loaded** (VISION/THERMODYNAMICS
  — now deferred across THREE consecutive cycles: exp-076, exp-077,
  exp-078, each cycle's own ranking naming it explicitly and each one
  declining to run it). Per the Iteration-54 ranking's own standing
  instruction ("should not be deferred a third time without an explicit
  reason"), exp-078 gave no such reason — **this is now the single most
  overdue item on the whole T28 board and should not be deferred a
  fourth time without one stated explicitly in Iteration 56's own
  synthesis.** **Tier 3 — governance:** (11) Checkpoint criterion 2
  (mechanism-class boundary) ruled NOT YET RIPE this cycle — at least
  four concrete, unpriced items remain open (item 1's own generalization
  question, the far-wall/far-edge pair, the x-wall's realizable-
  admittance refit, and the wavelength-generality leg, item 8). None of
  the above re-opens or re-proposes any RULED-OUT item (R1–R9); item 1's
  own full-aperture-sum question and the x-wall realizable-admittance
  refit are new instances of the already-permitted coherent-echo
  mechanism class applied to configurations no prior cycle has tested,
  not resurrections of anything closed. Full record: `experiments/078-
  t28-y-wall-echo-prescreen/`, LOGBOOK.md Iteration 55.
- **[superseded by the Iteration-56 queue above — exp-077's own docket,
  retained as a pointer to its own history, not deleted]** exp-077
  REFUTEd the x-normal, unrealizable-admittance
  coherent-echo mechanism for both `PAIR_PAD` and `PAIR_ABSORB40` on the
  complete two-wall instrument — real, well-earned negative evidence, but
  NOT the closing of the coherent-echo mechanism class (Checkpoint
  criterion 2 explicitly ruled not yet ripe). Four concrete, unpriced
  candidates remain, three zero-FDTD. **Tier 0 — zero FDTD, run as one
  batch:** (1) correct LOGBOOK's T16 "24×" framing (DONE, LOGBOOK.md
  Iteration 54 — listed here only for completeness); (2) **a closed-form
  period pre-screen of the y-direction (transverse) wall echo**
  (PHOTONICS #1, EM #1, independently convergent) — derive the correct
  grazing-incidence period formula for a wall whose normal is transverse
  to the beam's principal axis, evaluate at `A=752` and each config's
  actual aperture-to-wall distance, compare to T28's established
  `P*≈2.84°`/`4.2–4.6°` periods; EM's own caution: `A=752` is the SAME
  reference length T21's own already-refuted edge-diffraction fringe
  model uses — may desk-close in under an hour without building the full
  y-mirrored propagator. (3) **the realizable-admittance refit**
  (MATERIALS #1) — map `lab/materials.py::graded_black_shell`'s already-
  characterized `eps_r(x)`/`sigma_e(x)` profile onto a complex `n(x)`,
  swap in the standard (`mu_r=1`) TE admittance for the matched one,
  re-score Test A/B against the same already-collected data; the only
  pending test that can move MATERIALS' realizability bound in either
  direction. (4) **gate the already-collected 750nm two-wall spot-check**
  with a null sized for its own 16-point/3° window and decide (PHOTONICS
  #2, EM #2) — if the INCONCLUSIVE flip survives calibration, the
  600nm-only REFUTE needs an explicit wavelength-generality caveat. (5)
  **a Yee-grid-numerical-dispersion-corrected re-score** (VISION #2, new)
  — recompute the round-trip phase using the engine's own closed-form 2D
  FDTD dispersion relation instead of vacuum `c`, distinguishing "the
  physics is dead" from "the model's assumed phase velocity was wrong".
  (6) **further-harden the null-calibration appendix** (QUANTUM #1) — the
  Iteration-54 mandatory-fix docket already wired up all 3 pure-noise
  statistics and added a circular-shift bootstrap variant; any remaining
  gap goes here. **Tier 1 — cheap FDTD, next:** (7) the full-width,
  non-aliased second-wavelength (`G40`) leg (QUANTUM #2, the standing
  precondition, deferred twice: exp-076, exp-077) — now the cheapest
  remaining FDTD test of whether T28's periodicity is a real,
  wavelength-scaling-consistent physical effect at all. (8) broadband
  pulsed reflectance spectroscopy of the `ABSORB` boundary
  (THERMODYNAMICS #2, carried from Iteration 53) — a genuinely orthogonal
  instrument class. **Tier 2 — the standing charter-relevant test:** (9)
  test whether the `PAD`-sensitivity survives with a real absorbing
  article loaded (THERMODYNAMICS #3, VISION #3, deferred twice:
  exp-076, exp-077) — the only item reconnecting T28's now seven-cycle-
  deep instrument-diagnostic work to a real constraint-3 scene; the
  most-deferred item on this board, should not be deferred a third time
  without an explicit reason. **Tier 3 — record hygiene (bundle, zero
  cost):** (10) exp-077's own 7-item mandatory-fix docket (`phase5_
  redteam_audit.md` §4 — all 7 items closed same-shift, Iteration 54;
  listed here for completeness only). None of the above re-opens or
  re-proposes any RULED-OUT item (R1–R9); the y-wall and realizable-
  admittance candidates are new instances of the already-permitted
  coherent-echo mechanism class applied to configurations neither
  exp-075 nor exp-077 tested. Full record: `experiments/077-t28-pad-
  round-trip-echo-model/`, LOGBOOK.md Iteration 54.
- **[superseded by the Iteration-55 queue above — exp-076's own docket,
  retained as a pointer to its own history, not deleted]** `PAD_TIED`: the
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
