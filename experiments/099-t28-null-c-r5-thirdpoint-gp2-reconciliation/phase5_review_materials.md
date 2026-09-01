# Panel Iteration 76 (exp-099) — Phase 5 Review: MATERIALS & METAMATERIALS

*Fresh-context seat. Blind to all other seats' Phase-5 reviews, per PANEL.md
independence mechanics. Speaking only from this discipline's charter:
sub-wavelength structure / what could physically realize the proposed
optical behavior; owns the realizability bound (published / plausible /
unobtainium-with-parameters). No RULED-OUT idea (R1–R19, LOGBOOK.md read in
full) is re-proposed below.*

## 1. Independent spot-verification

Six load-bearing numbers recomputed from primitives (not trusted from
NOTES.md's prose), plus a direct source-code check of the claim this
seat's charter is specifically asked to adjudicate.

1. **Item 2 crossing angle (`find_sign_change`, linear interpolation,
   `θc50`).** From `results.json::item_2.step3.report`: at
   θ=39.688519316666°, `delta_scene=−5.951707119924432×10⁻⁴`; at
   θ=39.854519316666°, `delta_scene=+5.230823206044954×10⁻⁴`. Linear
   interpolation: `frac = |d1|/(d2−d1) = 5.951707119924432e-4 /
   1.1182530325969386e-3 = 0.532233`; `θc = 39.688519316666 +
   0.532233×0.166000 = 39.776870°`. Filed value:
   `crossing_cpl50 = 39.77686992722644`. **Matches to 5 decimal places** —
   confirmed.
2. **Richardson ratio, 30/40/50 triple.** `shift_20_30` (relabeled;
   = exp-098's real 30→40 shift) `= −0.15031902190763446`; `shift_30_40`
   (relabeled; = this cycle's fresh 40→50 shift) `= θc50 − θc40 =
   39.77686992722644 − 39.921519316666235 = −0.14464938943979...`.
   `observed_ratio = 0.14464938943979.../0.15031902190763446 = 0.962283`.
   Filed: `observed_ratio=0.962282667915931`, `naive_order2_ratio=0.64`
   (`(40/50)²`). **Both confirmed exactly.**
3. **Item 1 interval-slope-decay ratios (the "reversal" claim).** From the
   7 filed/new `delta_scene` values: `diffs = [8.518394764230886e-4,
   1.1343724614854555e-3, 3.214553325128211e-4]`;
   `r_ratios = [|diffs[1]|/|diffs[0]|, |diffs[2]|/|diffs[1]|] =
   [1.331674, 0.283377]`. Filed: `[1.3316739748300177,
   0.28337723580831364]`. **Matches exactly** — independently confirms the
   genuine bounce (r₄=1.332>1, growing, not decaying) that drives the
   INCONCLUSIVE-AT-THIS-WIDTH verdict.
4. **Item 3 `ptp` ratio at θc=87°.** `ptp(87°)=0.07461436316975525`,
   `ptp_ref(θc=5°)=0.00025576654006225`; `ratio = 291.728`. Filed:
   `291.7283986857513`. **Matches.**
5. **R5-family construction parameters vs. R4** (`design_geometry.py`,
   read directly this session, not from any cited excerpt).
   `R4_RATIO=2.0`, `R5_RATIO=2.5` — both mechanical substitutions into the
   identical `r3_config()`-derived recipe. `R4_R_OUT=round(78×2.0)=156`,
   `R5_R_OUT=round(78×2.5)=195`; `DX_M_R4=600e-9/40=1.5e-8`,
   `DX_M_R5=600e-9/50=1.2e-8`; `L_GEOMETRIC_M_R4 = 156×1.5e-8 = 2.34e-6`,
   `L_GEOMETRIC_M_R5 = 195×1.2e-8 = 2.34e-6` — **bit-identical, both
   `assert`ed in the module itself to `<1e-12` against the native
   `R_OUT×30nm` anchor.** `SIGMA_R4_CORRECTED = 0.5/2.0 = 0.25`,
   `SIGMA_R5_CORRECTED = 0.5/2.5 = 0.2` — matches `run.py`'s own asserted
   values exactly, and `run_output.txt` confirms `sigma_max=0.25`
   (R4 calls) / `sigma_max=0.2` (R5 calls) applied correctly at every
   `article=True` call — no repeat of exp-091's own native-default
   `sigma_max` bug. **Confirmed: the R5 family is a mechanically faithful,
   line-for-line rescale of the R4 recipe, geometrically bit-identical in
   physical (SI) terms.**
6. **The "cpl-is-orthogonal-to-realizability" claim itself** — see §3
   below; this is the load-bearing check this review's charter exists to
   perform, done directly against `design_geometry.py` source, not taken
   on MATERIALS' own Phase-2 critique's word.

All six checks reproduce exactly or within interpolation precision. No
arithmetic defect found anywhere in this cycle's load-bearing figures.

## 2. Steel-man

This is genuinely disciplined instrument-trust work, and MATERIALS'
charter interest — what R5's construction actually represents physically
— is served well by it. Three things are done right, materially, not
cosmetically: **first**, R5's four-cycle-old, never-spent machinery is
finally exercised, and it is exercised *behind* a real gate, not merely
unblocked — the three-way Phase-2 convergence (QUANTUM's fault-injection
gap, this seat's own R15-addendum far-from-null sign check, EM's unpriced
HALT outcome) forced a genuine ground-truth discipline onto R5's first
real spend that no prior T28 resolution family (R3, R4) had applied
*before* its own first interior-near-null reading was trusted — R3 and R4
both earned that discipline only after the fact (R15's own founding
instance, Iteration 71). R5 is the first family in this sub-thread's
history to clear a far-from-null ground-truth sign check (θ=36°,
confirmed negative, matching R3/R4) *before* any near-null reading is
reported. **Second**, the construction itself is verified, this session,
to be what it claims to be: bit-identical physical geometry (`2.34×10⁻⁶`
m) across R3/R4/R5 despite three different grid densities — a real,
`assert`-enforced invariant, not an assumption. **Third**, the cycle
correctly refuses to over-read its own genuine third-point result: the
Richardson figure (`observed_ratio=0.962` vs. naive `0.64`) is reported
with the same "descriptive only, no continuum reference" discipline
(Idealization 49) applied the first time this figure was computed
(exp-098), not upgraded to a convergence-order claim just because it
reproduced a second time in the same qualitative direction. That is the
correct level of caution for a two-point pattern on a family this
sub-thread's own R15 lineage already treats as potentially
recipe-systematic, not independently-converging.

## 3. Sharpest finding — the "cpl-orthogonal-to-realizability" claim is
real but narrower than NOTES.md's own §T1 disposition states it, and the
gap matters specifically to this seat's charter

NOTES.md's §T1 disposition states: *"`cpl` is confirmed purely a
grid-density/numerical-resolution parameter... with physical geometry
(`L_GEOMETRIC_M`) held invariant to 1e-12 across R3/R4/R5 — it carries
**zero realizability content of its own**; the realizability bound
MATERIALS' charter owns remains entirely un-addressed by any cpl-indexed
work in this seven-cycle run, and **is orthogonal to it**."*

**What was actually checked, this cycle, is narrower than that language.**
The verification performed (MATERIALS' own Phase-2 critique, independently
re-confirmed by me directly against `design_geometry.py` in §1.5 above) is
that the *geometric radius in meters* is held invariant across R3/R4/R5.
That is a real, `assert`-enforced fact, and it is a genuinely new check —
this is the first cycle this invariance has been confirmed for R5
specifically, since R5 never existed as a real-FDTD family before this
cycle. But "the geometric radius doesn't change with grid density" is a
narrower claim than "`cpl` carries zero realizability content." Two
distinct questions are being run together:

- **(a) Does the `cpl` KNOB itself encode any physical/material
  information?** Yes — confirmed, and correctly so: `cpl` selects grid
  spacing only, and the accompanying `σ` correction
  (`SIGMA_R{4,5}_CORRECTED = SIGMA_NATIVE / RATIO`) is explicitly designed,
  per the module's own comment, to hold the shell's accumulated optical
  depth `2·σ·r_out(cells)` invariant under the rescale — this is the
  correct discipline (T22/SIGMA_ON's own erratum lineage exists precisely
  because this WASN'T always done correctly in this program's past).
- **(b) Is the delta_scene(θ) sign-structure FEATURE these seven cycles
  have been tracking across cpl=20/30/40/50 evidence of, or bearing on,
  any realizable physical mechanism at all?** This is the question the
  disposition's "orthogonal to it" language actually needs to answer for
  MATERIALS' charter to be honestly discharged, and this cycle does not
  test it — nor could it, since items 1–3 are pure resolution/instrument
  work on an already-established artifact class. The sub-thread's OWN
  prior record already answers this, more specifically than "orthogonal":
  exp-076 proved `PAD` is lossless vacuum (the round-trip-timing/phase
  mechanism this whole `C40`/`G40`/Null-B/Null-C signal traces to cannot
  be a change in absorbed power, by construction); Iteration 59 adopted
  "zero realizability content" as a **standing framing rule** for exactly
  this class of finding — a domain/boundary-geometry artifact, not a
  material response. NOTES.md's restatement this cycle is consistent with
  that standing rule, not a new claim — but presenting it inside a
  freshly-derived "cpl is confirmed purely numerical" sentence, without
  citing that it is *also*, separately, a re-affirmation of an already-
  adopted framing rule about the FEATURE (not the resolution knob), risks
  exactly the kind of claim-compounding this program's own R4/R9 lineage
  exists to catch: a reader citing this cycle's §T1 disposition forward
  could reasonably (and wrongly) read "cpl has zero realizability content"
  as "MATERIALS has newly re-confirmed this whole channel has zero
  realizability content," when what was actually newly confirmed is a
  narrower geometric fact, and what licenses the broader reading is an
  *inherited* finding from three cycles earlier that this cycle's own text
  does not cite.
- **A second, smaller, related precision gap**: the `σ` correction that
  underwrites even claim (a) is documented in `design_geometry.py`'s own
  comment as holding optical depth invariant only **"leading-order in
  alpha"** — an approximation, not an exact identity, unlike the geometric
  radius's own bit-exact `1e-12` assertion. This residual has already been
  checked once and found non-contaminating at the PRIMARY channel (exp-092's
  Rank 3, at native `sigma_max`) — so this is not a new open risk — but the
  §T1 disposition's "held invariant to 1e-12" phrasing borrows the
  geometric assertion's own precision language for a claim (the physical σ
  profile is resolution-invariant) that does not carry the same precision
  guarantee. A minor scoping imprecision, not a substantive error.

**Is the claim verified this cycle, or just asserted?** Both, in different
proportions than the text implies: claim (a) (the resolution knob's own
physical inertness) is genuinely, newly verified this cycle, extended to
R5 for the first time — real work, correctly credited. Claim (b) (the
tracked FEATURE's own realizability irrelevance) is *asserted* this cycle
by re-stating an inherited standing rule, not independently re-tested —
which is defensible (Iteration 59's rule does not need re-deriving every
cycle) but is not what "confirmed... this session" language, applied
uniformly across the sentence, suggests to a reader who has not also read
Iteration 59's own entry.

**This is not a defect that changes any verdict this cycle** — no
prediction, no gate, no classification in items 1–3 depends on this
sentence's own precision. It is, however, squarely this seat's own
charter question, genuinely under-discharged in the way the disposition
is phrased, and — given this program's own R4/R9 lineage's standard that
claim-compounding across cycle boundaries is exactly the failure mode
worth naming even when non-load-bearing — worth a same-shift wording
correction: separate "the `cpl` resolution knob is physically inert
(newly confirmed for R5 this cycle)" from "the tracked `delta_scene`
feature itself carries zero realizability content (an inherited framing
rule from Iteration 59, not re-tested here)."

## 4. Secondary findings

1. **A field-naming collision risk in `results.json`, non-load-bearing but
   worth flagging for any future citation.** `richardson_style_diagnostic`
   is called with `shift_20_30=SHIFT_B_30_40` (i.e., the argument literally
   named `shift_20_30` is populated with exp-098's real **30→40** shift,
   `−0.150319°`) to produce the 30/40/50-relabeled figure. NOTES.md's own
   prose is careful about this (`"relabeled positionally... exactly as its
   own docstring permits"`), but the persisted field in `results.json`
   (`item_2.step3.richardson_30_40_50.shift_20_30 = −0.15031902190763446`)
   carries no in-JSON annotation that this is a relabeled 30→40 figure, not
   Null B's real (and numerically quite different, `−0.193581°`) 20→30
   shift. A future cycle reading this JSON cold — without NOTES.md's own
   surrounding prose — could genuinely confuse the two. This is exactly
   the class of risk R9 exists to guard against (operand commensurability
   surviving into a bare JSON citation), one step upstream of an actual
   miscitation rather than a citation itself. Cheap fix for a future
   cycle: persist an explicit `note` field inside the JSON object itself
   (not only in NOTES.md prose) stating which physical shift each
   positional key actually holds.
2. **A dead/over-permissive assert, harmless this run.** `run.py`'s final
   call-count assert allows `total_calls==16` on the HALT-path branch, but
   Step 1 (4 calls) and Step 2 (8 calls) both run unconditionally per this
   cycle's own Red-Team-mandated fix — so the HALT-path item-2 subtotal is
   always exactly 12, and the true HALT-path grand total is always 24
   (12+12), never 16. The code's own inline comment concedes this
   ("Step2 always runs -- N/A"). Not a defect that could let bad data
   through (the assert is over-permissive, not under-permissive), but
   worth tightening next time this script is touched.
3. **Item 1's "genuine bounce" reading is well-supported and consistent
   with the established period, independently re-confirmed** (§1.3
   above). The reversal (`r₄=1.332`) occurring at `θ₀+0.5°` to `θ₀+0.83°`
   — roughly a sixth of the established `~2.9474°` period past `θ₀` — is
   a physically sensible location for a trough-to-rising-flank transition
   if `delta_scene`'s own established oscillation governs this window, and
   Fix 5's period-based VANISHING-AMPLITUDE gate correctly prevented this
   cycle from mis-scoring this as a genuine asymptote. Good instrument
   design, properly executed.
4. **The Phase-2 three-way convergence on item 2's validation gap (Attacks
   1–3) is real and correctly adjudicated** — I independently re-traced
   the same three files Red Team cites (`run_checks_1234_and_7`'s
   hardcoded `family="R4"` calls; R15's addendum text; `cell_metrics_r5`'s
   inline asserts) and confirm none of the three critiques restates
   another; this was a genuine three-independent-routes finding, correctly
   escalated to mandatory rather than treated as a flip-to-support
   courtesy (QUANTUM's own Attack 1).

## 5. Verdict

**CONCUR-WITH-GAP(S).**

The FDTD physics, the process discipline (frozen predictions before code,
honest disclosure of the mid-run `KeyError` and its confinement to a
downstream lookup, zero silent overclaiming in Result), and every checked
arithmetic figure are sound — no finding here is outcome-determining
against any of this cycle's three items. The gap is squarely this seat's
own charter: the §T1 disposition's "zero realizability content... is
orthogonal to it" language compounds a newly-verified narrow fact
(geometric invariance) with an inherited, un-re-tested broader claim (the
tracked feature's own realizability irrelevance) without distinguishing
the two — a real, if non-blocking, precision gap in exactly the kind of
claim this program's own R4/R9 lineage treats as worth naming even when
harmless this cycle.

## 6. Ranked top-3 candidate directions for Iteration 77

NOTES.md's own draft Next section ranks: (1) widen Null C's bracket to a
full period; (2) the T1/constraint-scoring trigger; (3) generalize the
Richardson pattern to Null A; (4) recompute item 3 directly with exp-086's
method; (5) standing deferred items. **I agree items 3–5 belong lower, but
I would re-order 1 and 2, and add a genuinely new MATERIALS-charter item
this cycle's own gap motivates.**

1. **(Promoted from NOTES.md's own #2) Run the actual constraint-1/2/3/4
   scoring pass, treating `delta_scene(θ)`'s now-more-fully-characterized
   sign structure as an angular-selectivity parameter, scored against the
   existing instruments (`emit.observer_record`, `lab/ambient.py`, the
   beam-behind box).** This is the ONLY route by which any of this
   seven-cycle-plus T28 resolution program could ever become relevant to
   this seat's own realizability-bound charter — until it runs, MATERIALS
   has, and can have, nothing concrete to bound. Seven consecutive T1:N/A
   cycles is not yet a Checkpoint-4 pattern (no rule requires a T1 entry
   every cycle, and THERMODYNAMICS' own disposition this cycle is reasoned,
   not silent) — but the un-discharged charter debt named explicitly in
   NOTES.md's own §3 is this program's clearest present symptom that the
   sub-thread's center of gravity has drifted from "does this bear on the
   phenomenon" toward "does this bracket converge," and I rank closing
   that gap above a further bracket refinement on an already-well-
   characterized-as-domain-artifact channel.
2. **New item, this seat's own: a short, zero-FDTD MATERIALS disposition
   memo that formally closes (not merely restates) the realizability
   status of the whole `PAD`/`ABSORB`-boundary/coherent-echo artifact
   class**, drawing together exp-076's lossless-vacuum proof, Iteration
   59's "zero realizability content" framing rule, and this cycle's own
   geometric-invariance confirmation, into one citable finding that
   distinguishes (per §3 above) "the resolution knob is inert" from "the
   feature is a domain artifact, not a material response" explicitly.
   This converts a repeatedly-restated informal disposition into a single
   closed record, matching this program's own established discipline for
   closing a many-times-deferred flag with a reasoned finding rather than
   a further deferral — and directly discharges the gap named in §3/§5
   above.
3. **(Demoted from NOTES.md's own #1) Null C's wider-bracket question —
   is the observed bounce a true local trough or the near edge of a wider
   oscillation** — remains legitimate, falsifiable science and I do not
   dispute it belongs on the board; I rank it third, not first, because
   spending a further cycle narrowing an oscillation this sub-thread's own
   record already treats as a domain-boundary artifact (not disputed by
   this cycle's own findings), without first taking item 1 above, risks
   exactly the pattern of continuing to characterize an artifact in ever
   finer detail while the conversion-to-constraint-relevance step keeps
   getting deferred — the same shape THERMODYNAMICS' own §T1 trigger
   language in NOTES.md warns against for a hypothetical Iteration 77 that
   files T1:N/A an eighth time without addressing it.

Standing items I do not re-rank but endorse carrying forward unchanged:
the Richardson-pattern generalization to Null A (real, but lower stakes
than items 1–2 above); the item-3 direct-method recompute; and the
board's own oldest deferred items (the second-wavelength `G40` leg, the
x-wall realizable-admittance refit, and — still the single most overdue
item on the whole T28 board — whether `PAD`-sensitivity survives with a
real absorbing article loaded, now approaching six consecutive cycles
deferred).
