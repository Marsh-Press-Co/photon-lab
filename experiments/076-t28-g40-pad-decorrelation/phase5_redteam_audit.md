# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 53 · exp-076
## Adjudicating all six blind Phase-5 reviews of the G40/`PAD` decorrelation, formalizing EM's lossless-vacuum finding, and reconciling six Iteration-54 candidate rankings into one

**Seat: RED TEAM.** Read `LOGBOOK.md` in full (RULED OUT R1–R8; ESTABLISHED;
every LIVE THREAD T1–T28, T16/T21/T24/T27/T28 read closely, including the
full Iteration 42–52 narrative bodies) and `PANEL.md` in full. Read the
complete exp-076 record: `phase1_proposal.md`, all five
`phase2_critique_*.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `run.py`, `g0e_amplitude_channel_check.py`, `phase4_results.md`,
`results.json`, and all six blind `phase5_review_*.md`. This is Phase 5's
final audit: I alone see everything — the official record and all six blind
reviews — and speak last.

## 0. What I independently verified this cycle (zero new FDTD, per scope)

- Re-derived the frozen headline directly from `results.json`:
  `x=amp_ratio(PAIR_PAD)=0.119366` (HIGH), `y=amp_ratio(PAIR_ABSORB40)=
  0.071616` (MED) → `OUTCOME=PAD_TIED`. Bin edges `THRESH_LOW=0.049762`,
  `THRESH_HIGH=0.116111` reproduce from `0.3/0.7 × amp_ratio(C40,C80)=
  0.165873` to the stated precision.
- Re-ran `carrier_fit()` (exp-072's own function, loaded verbatim) directly
  against `results.json::headline`'s and `::leg750_scored`'s committed
  arrays. 600nm: `PAIR_PAD → T_mean_deg=2.4075°, r²=0.4381`;
  `PAIR_ABSORB40 → T_mean_deg=2.4575°, r²=0.4323`. 750nm:
  `PAIR_PAD → T_mean_deg=1.7803°, r²=0.5106`; `PAIR_ABSORB40 →
  T_mean_deg=1.7613°, r²=0.5838` — **bit-for-bit reproduces PHOTONICS'
  cited figures** (1.78°/1.76°, r²≈0.51/0.58), and confirms the diagnostic
  is computed by the real pipeline (inside `carrier_fit`, called from
  `_amp_ratio_recover`) but genuinely absent from every key in
  `results.json` (`leg750_scored` carries no `T_mean_deg`/`r_squared`
  field — checked directly). Also confirms the 600nm window resolves
  2.44–2.49 cycles of its own carrier vs. the 750nm leg's 1.69–1.70 —
  PHOTONICS' "worse-conditioned than the already-marginal 600nm window"
  claim holds numerically, not just by assertion.
- Read `experiments/065-.../design_geometry.py::config()` and
  `lab/fdtd2d.py`'s `Sim.__init__`/damping-array construction directly:
  the graded-loss array `d` (lines ~120–128) is built as a cubic ramp of
  width `self.absorb` cells at each domain edge — a pure function of
  `absorb`, with **zero dependence on `nx`/`ny`/`pad`**. `PAD` cells only
  extend `nx`/`ny` and shift scene coordinates; they never enter the
  damping-mask construction. Independently confirms EM's Phase-5 claim
  from the primitive source, not merely from the `static_construction_
  identity` gate's summary line (which I also re-checked:
  `experiments/065-.../design_geometry_output.txt:85`, `max over all =
  0.000e+00 (scored window is pure vacuum: True)`).
- Grepped `run.py`/`results.json` for `g0e.main|g0_pass|"g0e"`: zero hits
  beyond a docstring comment referencing the *pattern* by name. Confirms
  QUANTUM's finding — `run.py` imports two functions
  (`exp072_run`, `_amp_ratio_recover`) from `g0e_amplitude_channel_check.py`
  but never calls `g0e.main()` or re-executes Case 1/Case 2 against real
  `G40` data; no `g0e`/`g0_pass` key exists anywhere in `results.json`.
- Read `experiments/072-.../run.py` lines 680–695 directly: the `rho_c`
  docstring Red Team's Phase-2 audit and QUANTUM's Phase-5 review both
  quote is reproduced character-for-character in source. Confirmed
  `rho_c=None`/`p072_3="NOT_EVALUABLE"` in the committed exp-072
  `results.json` — `rho_c` was genuinely never evaluated on real data
  anywhere in this program's history, exactly as both reviews state.
- Recomputed `pair_pad["amplitude"]=0.005154759`, `pair_absorb40
  ["amplitude"]=0.005513824` from `results.json::headline` — 3.1%/10.3%
  above VISION's frozen lab bar `C_thr=0.005` (T2, Iteration 1), confirming
  the "within ~10%" and "~24×" (`x/C_thr=23.87`) figures both VISION
  reviews cite.
- Confirmed `phase2_redteam_audit.md`'s disposition table and
  `phase3_synthesis.md`'s acceptance table each carry exactly the items
  traceable to a numbered Attack or a seat's *sharpest* attack; VISION's
  own "Secondary finding" (the `amp`/`C_thr` proximity + a proposed
  Idealization-8-style disclaimer) appears in neither, nor in `NOTES.md`'s
  ten idealizations — independently confirmed absent, not merely trusted
  from VISION's own Phase-5 self-report.
- Confirmed `score_headline()`'s `x`/`y` are built from `math.hypot(A_i,
  A_q)` only — no `R_q` term anywhere in the gating statistic — so the
  "not a seventh cycle on the retired instrument class" claim (§7 of
  `phase1_proposal.md`) holds by direct code inspection, independent of
  the prose asserting it.

No discrepancy found between any of the six blind reviews' load-bearing
numeric claims and the committed record. All six converged on **PARTIAL**
independently; I concur, for the reasons below.

---

## 1. Adjudication of the six reviews

| # | Seat | Finding | Verified? | Load-bearing for the record? | Disposition |
|---|---|---|---|---|---|
| F1 | PHOTONICS | 750nm leg's fitted carrier lands on an unexplained ~1.78°/1.76° periodicity (r²≈0.51/0.58), matching neither T28's own established band (2.44°–2.84°) nor T21's own 750nm-scaled prediction (~2.4°); resolves only ~1.7 cycles, worse-conditioned than the marginal 600nm window; `score_leg750()` computes but discards this diagnostic. | **CONFIRMED**, bit-exact, independently re-derived from source (§0). | **Yes.** Sharpens the 750nm leg's own evidentiary status from "narrow/advisory" to "unreliable for a specific, diagnosable reason" — belongs in the permanent record verbatim, not just as a hedge. | **ADOPT.** Mandatory-fix docket item 1 below (persist `T_mean_deg`/`r_squared` for every future carrier-fit leg). |
| F2 | MATERIALS | `PAD_TIED` makes a future physical-mechanism claim *less* plausible than an `ABSORB_TIED` result would have — `PAD` has zero witness-scene/realizable-structure analog (unlike `ABSORB`'s at-least-depth-shaped profile); the 750nm ordering flip further undercuts a physical reading (real dispersion would not flip which term dominates outright between two λ a factor of 1.25× apart). | **CONFIRMED** by direct re-read of the geometry table and the caveat-placement check (§0). The asymmetry argument (`ABSORB` is depth-shaped, `PAD` is proximity-to-domain-wall) is sound reasoning, not overreach — it does not contradict MATERIALS' own required "neither carries more physical standing" caveat, which is about *material* standing (loss tangent, dispersion), not about "which is more depth-shaped." | **Yes.** This is the correct realizability reading and should anchor T28's LOGBOOK update, not just "confound not relieved." | **ADOPT**, and elevate — see §4 below (this is the strongest single interpretive finding of the cycle). |
| F3 | EM | `PAD` is provably lossless vacuum (confirmed by `static_construction_identity`'s own "scored window is pure vacuum" result and, independently this audit, by `lab/fdtd2d.py`'s damping-array construction) — so `PAIR_PAD`'s entire signal is necessarily a propagation-phase/interference effect, never absorbed-power. Also: G40 was never settling-tested at 750nm. | **CONFIRMED**, independently re-derived from the primitive source code, not just the gate's summary line (§0) — this is the strongest verification in this audit; see §3 for why it should be stated as a formal constraint. | **Yes — the single most load-bearing new physics finding of Phase 5.** | **ADOPT AND FORMALIZE**, §3 below. |
| F4 | THERMODYNAMICS | Sidecar N/A correctly filed, independently over-determined by `static_construction_identity`'s own vacuum-window proof (not just convention-by-citation); `PAD_TIED` makes a future energy-based mechanism *less* likely to become relevant (the signal now points toward propagation/domain-geometry territory, not the still-non-physical but at-least-loss-adjacent `ABSORB` axis). | **CONFIRMED.** The "independently over-determined" claim is correct and matches F3's own vacuum finding from a different angle — both audits (THERMO's Phase 5, EM's Phase 5, and this audit) independently arrive at the same underlying fact via different routes (thermo: no dissipative volume exists to score; EM: no damping coefficient exists in that region), which is itself corroborating, not redundant. | **Yes**, minor. | **ADOPT.** Fold into T28's LOGBOOK entry as a one-line cross-reference. |
| F5 | VISION | Real, unadjudicated gap: her own Phase-2 finding (the `amp` normalizer, ~0.0052–0.0055, sits within 10% of `C_thr=0.005`) was never adopted, modified, or explicitly rejected — absent from both the Phase-2 audit's disposition table and Phase 3's acceptance table. Connects `PAD_TIED` to T16 as a third confirmed instrument-floor driver, magnitude ~24× the lab bar. | **CONFIRMED**, independently: grepped both documents myself, confirmed the finding is genuinely absent from both, not merely under-weighted (§0). | **Yes**, on both halves — the gap is real (see §2 below for the Checkpoint ruling) and the T16 cross-reference is a genuinely new, correctly-scoped connective finding this cycle's own record does not otherwise draw. | **ADOPT**, both halves. |
| F6 | QUANTUM | `G0-e`'s disposition holds on real `G40` data (fitted carrier params land comfortably inside the synthetic sweep's validated envelope and the historical baseline range) — but `NOTES.md`/Phase-1 promised an inline, executable "re-confirmed unchanged" gate at Phase 4 (matching exp-072's own `g0_pass` pattern); `run.py` never invokes it — no `g0e`/`g0_pass` key anywhere in `results.json`. | **CONFIRMED**, independently: I re-ran `carrier_fit` on the real data and independently reproduced QUANTUM's own comparison table (§0) — the disposition genuinely holds; the promised inline call genuinely does not exist in `run.py`. | **Yes**, on both halves — the physics check is correct and worth stating plainly; the process gap is real and should be corrected in future citation language. | **ADOPT**, both halves. See §2 for the Checkpoint ruling. |

No finding across the six reviews was found incorrect, overstated beyond
what the record supports, or in conflict with another seat's independently
re-derived numbers. This is an unusually clean Phase-5 crop — every seat's
headline claim survived my own from-scratch re-derivation.

---

## 2. The two self-execution gaps (F5, F6): both real, neither outcome-determining, neither fires Checkpoint criterion 4

The Director's brief asks specifically whether either gap rises to R8/
Checkpoint-4 territory (an unverified/unclosed gap that later proves
outcome-determining), or is genuinely inert.

### 2a. QUANTUM's finding (F6) — inert, verified inert, not merely asserted inert

`G0-e`'s synthetic ground-truth recovery check (`g0e_amplitude_channel_
check.py`) takes **no input from real `G40` FDTD data** — its generator is
a fixed synthetic sweep (`P_true=2.49°`, `DENSE_ANGLES` fixed, `psi0`/
`m_true` swept over a pre-registered grid). Re-running it at Phase 4 would
reproduce the identical `PASS`/`1.03×10⁻⁴`/`8.35×10⁻³` figures bit-for-bit
regardless of what the real `G40` data turned out to be. This is not an
assumption — QUANTUM's own Phase-5 review, and my own independent
re-derivation of the same comparison this audit (§0), both directly checked
the thing that actually matters: do the *real* fitted carrier parameters
(`T_mean_deg`, `psi`, `amplitude`, the headline magnitudes themselves) fall
inside the region the synthetic sweep already validated? Yes, comfortably
interior on every axis, not near an edge. **This is exactly the affordable
check R8 requires before filing a gap as non-blocking — and it was actually
run, independently, by two different Phase-5 seats (QUANTUM and, this
audit, Red Team), not merely argued.** The promise-vs-implementation gap
(NOTES.md said "re-confirmed... matching exp-072's own `g0_pass`
precondition structure"; `run.py` only imports the module's functions and
never calls `g0e.main()`) is a real documentation/implementation-fidelity
defect — the language overclaims a procedural rigor that was not literally
built — but it is provably incapable of having changed `PAD_TIED`, because
the check it describes never reads the data whose scoring it would have
gated. **Ruling: genuinely inert. Does not fire Checkpoint criterion 4.**

### 2b. VISION's finding (F5) — a real process gap, correctly caught by the design (Phase 5), not outcome-determining, does not fire criterion 4 — but closer to the line than F6

This is a different failure shape than F6's, and a different shape than R8's
own precise trigger (an *argument* substituting for an affordable check,
adopted as sufficient). Here, nothing substituted — the finding was simply
never engaged. PANEL.md's Phase-2 spec requires one steel-man and one
*sharpest* attack per seat, with room for supporting material beyond that;
VISION's own critique explicitly labeled this a "Secondary finding," not the
sharpest attack, and Red Team's Phase-2 audit engaged VISION's *sharpest*
attack (the settling differential) in full, folding it correctly into EM's
combined fix. A secondary, self-labeled-as-non-sharpest finding not
receiving its own numbered Attack is a defensible, not a mandatory,
editorial choice under this program's own protocol — I checked this against
PANEL.md's literal text, not merely against convention.

What tips this from "acceptable editorial discretion" to "worth flagging
explicitly" is the substance, independently re-verified this audit (§0):
the coincidence is real (`amp`/`C_thr` within 3–10%), the risk is a genuine
one this exact program has been bitten by before in a structurally
identical shape (exp-072's own Idealization 8, forced into that cycle's
record at VISION's own prior insistence, for the identical `C_empty`-vs-
Weber-contrast conflation risk), and — checked directly by VISION's own
Phase-5 review and independently re-confirmed by me (§0) — **the actual
committed prose in `phase4_results.md`/`NOTES.md`/`run.py` is clean: zero
matches for "contrast," "C_thr," "Weber," "photopic," "scotopic," or
"GATE_HARD" anywhere in the three files.** The gap is latent (a risk for a
*future* reader or a *future* cycle reusing this normalization convention
for a quantity that touches a real object), not live (no current sentence
in the record actually misreads `amp_ratio` as a perceptual quantity). It
was caught by exactly the layer designed to catch it — a fresh, independent
Phase-5 read — before it ever produced a misreading, which is this
program's own repeatedly-stated non-firing pattern ("Phase-5 catching a
gap is the mechanism working, not failing").

**Ruling: a real, disclosed-then-dropped gap; does not fire Checkpoint
criterion 4** (no false claim survived into the record; the risk is
prospective, not realized; it was caught, not defended). **But it should be
closed same-shift**, not carried forward a second time — see the
mandatory-fix docket, §5.

### 2c. A pattern worth naming, not firing on

Three small process/documentation gaps surfaced in Phase 5 of this single
cycle (PHOTONICS' record gap F1, VISION's dropped finding F5, QUANTUM's
promise-vs-implementation gap F6) — the cycle immediately following R8's
adoption for exactly this class of failure (Iteration 52). None is
individually outcome-determining, and all three were caught by the design
(blind Phase-5 review) rather than surviving into a defended headline claim
— the precise distinction this program has drawn, repeatedly, between a
non-firing and a firing instance of criterion 4. I do **not** read this as
criterion-4-adjacent drift requiring escalation: three cheap, independently-
diagnosed, non-outcome-determining gaps caught by six thorough blind reviews
in one cycle is closer to evidence the review layer is working at high
sensitivity than evidence of drift. But three in one cycle is enough to
warrant one procedural tightening, offered as a recommendation, not a new
numbered rule (that is the Director's call, not mine to impose
unilaterally): **Phase 3's acceptance table should include an explicit
line for every disclosed Phase-2 "secondary finding," not only the seats'
sharpest attacks — even a one-word "deferred, non-sharpest, not adopted
this cycle" disposition would have closed F5 without costing anything.**

---

## 3. Formalizing EM's finding: `PAD` is provably lossless — `PAIR_PAD`'s signal is necessarily a phase/interference effect, never an absorbed-power effect

Independently re-derived from the primitive source this audit (§0), not
merely from the gate's summary line: `lab/fdtd2d.py`'s graded-loss array is
built as `ramp = (arange(absorb,0,-1)/absorb)**3`, applied only within the
outermost `absorb` cells at each domain edge — a pure function of the
`absorb` parameter passed to `Sim.__init__`, with **no reference to `nx`,
`ny`, or any padding-derived quantity anywhere in its construction.**
`design_geometry.py::config()` confirms `PAD` cells do exactly one thing:
extend `nx`/`ny` and shift every scene coordinate by `pad` — they never
touch the `absorb` argument passed to `Sim`. Maxwell's equations in a
source-free, σ=0 region conserve Poynting flux magnitude exactly (phase and
timing may change; the *amount* of power crossing any closed surface in
that region cannot). Since `G40` and `C40` share `absorb=40` bit-identically
(confirmed by `static_construction_identity`, `max_diff=0.0`, re-verified
this audit), the graded-loss stack's reflectance *magnitude* at that
boundary is provably the same physical quantity in both configs — not
merely measured to be close, but structurally guaranteed to be identical by
construction. **The entire `PAIR_PAD` signal — the largest reading this
cycle produced, and the one driving `PAD_TIED` — can only be a coherent
propagation-phase/round-trip-timing effect. It cannot, by this argument, be
a change in absorbed power.**

This is the single most load-bearing new finding to come out of Phase 5.
It:

1. **Converts MATERIALS' realizability finding (F2) from a strong
   analogy into a proven mechanism-class statement.** `PAD_TIED` is not
   merely "less physically suggestive" than `ABSORB_TIED` would have
   been — it is now formally established that the dominant confirmed
   sensitivity axis for this signal can *only* act through phase/timing,
   never through the one channel (absorbed power) any future coating- or
   material-based mechanism proposal would need to route through. This
   sharpens, not just corroborates, MATERIALS' §2.4 verdict.
2. **Gives EM's own top-ranked Iteration-54 candidate (a `PAD`-
   reparametrized version of exp-075's passivity-gated transfer-matrix echo
   model) a first-principles justification, not just a plausible-guess
   status** — the model is now known, before it is even fit, to be testing
   the *only* physically-permitted mechanism class for this specific
   signal.
3. **Should be recorded in LOGBOOK.md as a standing physical constraint on
   this sub-thread**, exactly as EM's own §5 item 3 recommends: any future
   `PAD`-tied finding on this construction family must be read against the
   fact that `PAD` is provably lossless vacuum and can therefore only ever
   shift a signal's phase/timing, never its absorbed-power magnitude.

I find no flaw in this argument on independent re-derivation from the
primitive engine code (not the gate summary alone), and no seat's review
contradicts it. **Adopt in full, stated with the strength EM's own review
gives it** — this is not a hedge-worthy finding; it is a proof from the
engine's own construction, checkable by anyone in under five minutes, and
it should anchor how the LOGBOOK records this cycle at least as much as the
`PAD_TIED` classification itself.

---

## 4. Elevating MATERIALS' + EM's combined interpretive finding for the LOGBOOK record

Neither MATERIALS' realizability argument (F2) nor EM's passivity proof
(F3) individually captures what the two together establish. Combined: **the
signal that now most strongly explains T28's confounded `ABSORB`-series
history is (a) not tied to any parameter with a realizable-structure analog
of any kind, and (b) structurally incapable of being an absorbed-power
effect even in principle.** This is a genuine narrowing of what a future
physical mechanism for the ~2.84° periodicity would need to look like — not
merely "not yet confirmed," but "confirmed to be excluded from an entire
class of candidate physical explanations (anything acting through
absorption)." The LOGBOOK's T28 entry should state this combined reading
explicitly, not as two separate seat opinions.

---

## 5. Mandatory-fix docket (closes F1, F5, F6 same-shift; zero new FDTD)

1. **[F1, PHOTONICS]** Persist `T_mean_deg`/`r_squared` for every carrier
   fit `score_leg750()` (and any future leg-scoring function) computes —
   currently discarded in `diag_x`/`diag_y`. One-line change
   (`_amp_ratio_recover` already returns them in its `diag` dict; thread
   them into `score_leg750`'s return value and `results.json`).
2. **[F5, VISION]** Add the Idealization-8-equivalent disclaimer for
   `amp_ratio`/`delta_P_obs`/`rho_pad_absorb`/`C_empty(θ)` in this
   instrument family — the one-line fix VISION drafted at Phase 2 and that
   never received a disposition. Zero FDTD, zero substantive change.
3. **[F6, QUANTUM]** Correct the promise language: either implement an
   inline `g0e.main()`-style re-confirmation call in any future cycle that
   reuses this pattern (matching exp-072's actual `g0_pass` precedent), or —
   for this cycle specifically, since the check is retroactively confirmed
   data-independent and already passed — correct `NOTES.md`/
   `phase1_proposal.md`'s "matching exp-072's own `g0_pass` precondition
   structure" phrasing to state plainly that this cycle's `G0-e` check is a
   data-independent code-correctness test, not an inline data-conditioned
   gate, and that the distinction was verified (not merely asserted) at
   Phase 5.
4. **[F5, VISION]** Add the T16 cross-reference: log `PAD_TIED` as T16's
   third independently-confirmed instrument-floor driver (after T21's
   fringe and T27's settling-transient), with the `x=0.119`/`C_thr=0.005`
   (~24×) figures attached, in LOGBOOK.md's T16 entry, not only T28's.
5. **[§3, EM/this audit]** Add the passivity/lossless-vacuum finding to
   LOGBOOK.md's T28 entry as a standing constraint, worded per §3 above.
6. **[§4, this audit]** State the combined MATERIALS+EM interpretive
   finding explicitly in LOGBOOK.md's T28 entry, not as two separate,
   un-synthesized seat opinions.

None of these touch `PAD_TIED`, any frozen prediction, or any threshold —
all are record-completeness fixes, matching this program's own established
"catch and close same-shift" pattern for non-outcome-determining gaps.

---

## 6. Checkpoint ruling — all five criteria, explicit

1. **A configuration passes all constraint metrics.** N/A — constraint 3
   was never engaged (§3 of the proposal, correctly disclaimed throughout,
   independently re-confirmed: zero perceptual-threshold language appears
   anywhere in the committed record). **Does not fire.**
2. **A proven boundary within a mechanism class, gates clean.** N/A — this
   cycle decorrelates a measurement-instrument confound, not a T1 mechanism
   class. §3/§4's finding (PAD is lossless, hence phase-only) is a
   statement about *this FDTD instrument's own construction*, not about a
   witness-relevant mechanism class becoming jointly unsatisfiable. **Does
   not fire** — matches every seat's own independent ruling.
3. **Synthesis requires engine physics beyond the validated bench classes.**
   No engine change; `Sim` is reused as-is throughout. MATERIALS' own #3
   pick (a true-PML cross-technology check) is a *candidate* for future
   engine work, not a requirement this cycle triggered. **Does not fire.**
4. **Program-integrity drift.** Assessed in full at §2 above across all
   three candidate gaps (F1's record gap, F5's dropped finding, F6's
   promise-vs-implementation gap) plus the two disclosed Phase-4
   engineering bugs (both non-physics, both verified bit-identical across
   crashed and clean runs, both correctly disclosed rather than silently
   patched). Every one of the five was caught by the process itself
   (Phase 2's own docket for the two structural band defects Red Team's
   own Phase-2 audit found; Phase 4's own disclosure culture for the two
   engineering bugs; Phase 5's blind review layer for F1/F5/F6), none
   survived into a defended, uncaveated headline claim, and none is
   outcome-determining for `PAD_TIED` on independent re-verification.
   **Does not fire.** (See §2c for the one procedural recommendation this
   near-miss earns, offered as a suggestion, not a rule.)
5. **Two consecutive iterations with no logbook-advancing result.** This
   cycle delivers a genuine, independently-verified narrowing
   (`PAD_TIED`, plus §3's new physical constraint); Iteration 52 (exp-075)
   delivered two REFUTEd mechanisms plus R8's adoption. **Does not fire** —
   the program has advanced every recent cycle.

**No Checkpoint criterion fires.** This is a clean cycle: sound instrument,
honestly and completely reported, with real (if all non-firing) process
gaps caught and closable same-shift.

---

## 7. Reconciled Iteration-54 ranking (all six seats + this audit)

Six seats' top picks span genuinely different directions — a full-width
non-aliased leg (PHOTONICS/MATERIALS/QUANTUM/THERMO/VISION, near-unanimous
as a *precondition*); a PAD-depth causal sweep (MATERIALS); a
PAD-reparametrized passivity-gated echo model (EM, seconded by THERMO); a
loaded-article test (VISION); broadband reflectance spectroscopy (QUANTUM);
a T16 cross-reference (VISION). None is wrong; they answer different
questions at different costs. Reconciled by information-density per unit
cost, with zero-cost items that *disambiguate what to spend FDTD budget on*
placed first:

### Tier 0 — zero FDTD, run first (desk-only, decides where the budget below should go)

1. **PAD-parametrized round-trip echo model** (EM #1, seconded by
   THERMO #2) — refit exp-075's already-built, already passivity-gated
   (`G-PASSIVITY`, `|r|≤1`) transfer-matrix echo model's round-trip
   *distance* against `PAD` (using the `C40`/`G40` pair, where §3 proves
   reflectance amplitude is held constant and only phase varies) instead of
   `ABSORB` depth, the axis it was scored against — and REFUTEd — at
   exp-075. This is the cheapest, highest-information-density item on the
   board: it directly tests the mechanism §3's proof says is the *only*
   physically-permitted candidate, using code this program has already
   built and validated. **Ranked #1 overall.**
2. **Fixed-carrier re-score of the already-collected 750nm leg data**
   (PHOTONICS #2) — re-score `leg750_scored`'s committed arrays under a
   carrier FIXED at the 600nm-established ~2.5° periodicity, instead of
   `carrier_fit`'s free-period search. Directly tests whether F1's
   unexplained 1.78°/1.76° periodicity is a free-period-search artifact or
   survives a physically-motivated fixed period — decides whether the
   750nm ordering flip (§ below, item 3) is worth a full FDTD leg or is
   better explained away first.
3. **Score the already-built two-wall cavity model against the
   already-collected 750nm leg** — the still-untouched PLAN.md
   Iteration-53 queue item #2 (THERMO #3), carried over unexecuted through
   this entire cycle. Old debt; zero new FDTD; should not fall further
   behind.

### Tier 1 — cheap FDTD, next

4. **`PAD`-depth causal sweep at fixed `ABSORB=40`** (MATERIALS #1) —
   `PAD∈{20,60,80}` (reusing `design_geometry.py`'s own mechanical
   clearance-scaling), scored pairwise exactly as exp-071 did for the
   `ABSORB` axis. This is the direct causal-trend analog of exp-071's own
   `R²=0.998` finding, on the axis this cycle just showed actually
   dominates — the single most information-dense *new-FDTD* item, and the
   natural data source against item 1's model once fit.
5. **Broadband pulsed reflectance spectroscopy of `C40`/`G40`/`C80`'s
   `ABSORB` boundary** (QUANTUM #1) — ~3 FDTD calls, a genuinely
   orthogonal instrument class (single-shot time-domain FFT instead of
   another carrier-fitted angular sweep), directly tests whether 600nm's
   integer-λ aliasing condition (PHOTONICS' Phase-2 attack) is itself
   resonant, and cross-validates PHOTONICS' exp-075 WKB model against a
   real spectrum for the first time. Cheap enough to run alongside item 4
   rather than after it.

### Tier 2 — the standing precondition, and the charter-relevant test

6. **Full-width (31-point/6°), non-aliased second-wavelength leg for
   `G40`** (near-unanimous: PHOTONICS #1, MATERIALS #2, THERMO #1, QUANTUM
   #3, VISION #3) — the standing requirement before `PAD_TIED` may be cited
   as wavelength-general at all. Ranked below Tier 0/1 specifically because
   items 1–2 above should decide *which* wavelength/window configuration
   is worth the ~31-call spend (a fixed-carrier re-score might show the
   750nm flip is a fit artifact, changing what "non-aliased" should target;
   the causal sweep and reflectance spectroscopy may also sharpen where a
   second λ is most informative) — this item is mandatory, not optional,
   just not first.
7. **Test whether the PAD-sensitivity survives with a real absorbing
   article loaded** (VISION #2) — build the `G40`-decorrelation analogue
   with `graded_black_shell` or an `off_pass`/`off_bracket`-style article
   present, at the same dense window and settled `STEPS`. This is the
   actual charter-relevant question this cycle's empty-scene-only scope
   could not reach, and the one item on this list that reconnects T28's
   now five-cycle-deep instrument-diagnostic work back to a real
   constraint-3 scene. Ranked here (not #1) because it is the most
   expensive item and its interpretation benefits from items 1/4/6 already
   being in hand (a PAD-native mechanism model and a wavelength-general
   reading both sharpen what "survives loading" would mean).

### Tier 3 — record hygiene (bundle, zero cost, run alongside any of the above)

8. This audit's own mandatory-fix docket (§5, items 1–6) plus a
   2-call `G40`-at-750nm forward-settling leg (EM's own newly-disclosed
   gap, §1) and a `G0-e`-class synthetic recovery/telescoping check for
   `delta_P_obs`/`rho_c` before it is ever promoted from disclosed-only to
   a gating role (QUANTUM #2) — bundle into one closing pass, not scattered
   across future cycles.

### Longer-horizon, not in the immediate ranking

- **A structurally independent (true-PML) absorbing-boundary
  implementation** (MATERIALS #3) — the most decisive possible test of
  whether this whole family of findings is specific to the graded-damping-
  mask construction, but Checkpoint-criterion-3 (major engine build)
  territory; should not preempt the cheaper items above.

---

## 8. Bottom line

**Verdict: PARTIAL** — unanimous across all six blind Phase-5 reviews and
this final audit. `PAD_TIED` is a real, independently-reverified,
load-bearing correction to how Iterations 48–52's `{C40,C60,C70,C80}`
`ABSORB`-series causal claims should be cited (padding/domain-geometry
confound not relieved — worse than that, the dominant axis). It is
strengthened, not merely accompanied, by a new first-principles physical
constraint (§3): `PAD` is provably lossless vacuum, so its entire measured
effect must be a propagation-phase phenomenon, never an absorbed-power one
— which in turn sharpens MATERIALS' realizability reading (§4) into the
cleanest negative signal this sub-thread has produced: the axis that now
best explains T28's history has no witness-scene analog and is
structurally excluded from an entire class of physical mechanisms. Two
small, genuinely non-outcome-determining process gaps (VISION's dropped
Phase-2 finding, QUANTUM's promise-vs-implementation gap on `G0-e`'s
re-confirmation) surfaced at Phase 5 alongside one genuine record gap
(PHOTONICS' discarded 750nm carrier diagnostic) — none changes `PAD_TIED`,
none fires Checkpoint criterion 4, all close same-shift via §5's docket.
**No Checkpoint criterion fires.** T28's own substantive mechanism
question — the ~2.84° periodicity's ultimate origin — remains open, now
narrowed twice in the same cycle: toward `PAD`/domain-geometry rather than
`ABSORB` depth, and (new, this Phase 5) toward a phase/interference
mechanism specifically, never an absorbed-power one.
