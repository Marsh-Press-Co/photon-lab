# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 48 · exp-071
## ELECTROMAGNETISM's C60/C70 `ABSORB`-depth causal falsification test for T28

*Fresh sub-agent, RED TEAM charter (PANEL.md seat 7). Receives the full
exp-071 record and all six blind Phase-5 reviews. Speaks last and hardest.
Standard: NOT textbook-physics compliance — internal consistency,
falsifiability, expressibility as simulation parameters, non-violation of a
target constraint, and this program's own R4/R5/Checkpoint-4 precedent,
applied explicitly. Every numeric claim below was independently re-derived
from `results.json`/code, not taken on any seat's word, including my own.*

## 0. Independent re-verification performed

- `python3 design_geometry.py` (fresh run, this session): reproduces every
  printed figure bit-for-bit against all five prior citations of it
  (congruent table, `A=752` fixed, peak-angle fractions 0.949/0.984, budget
  78 calls/6266.6 CPU-s/30.64 min/91.92 min envelope, Rayleigh-floor table).
  **R4 clean.**
- Loaded `results.json` directly and independently recomputed: `raw_confirm`,
  `raw_refute`, `unresolved_only`, `trend_resolved`, `all_pairs_resolved`,
  the linear fit (slope/intercept/R²), all 6 pairwise spreads/ratios, both
  binding preconditions, `combined_reason`'s actual branch logic. Every
  figure matches the committed JSON exactly.
- Independently re-derived `dg065.CONFIGS` for all four congruent keys via a
  standalone script (not reading `design_geometry.py`'s own printed table):
  confirmed `PAD == ABSORB − 40` exactly at all four points, and
  `aperture_cells == NY − 2·ABSORB == 1504` exactly at all four points.
- Independently re-fit the four-point `P*(ABSORB)` series with a
  2-parameter saturating-exponential model (`P_inf − (P_inf−P₀)·exp(−k·(x−40))`,
  `P₀` pinned to the observed `C40` value, `P_inf`/`k` free — same 2
  residual degrees of freedom as the linear model) using `scipy.optimize.curve_fit`:
  **R² = 0.998** (`P_inf=2.539°`, `k=0.0845`) vs. the linear model's
  **R² = 0.866**. A simpler 2-parameter step/early-saturation model
  (asymptote = mean of the three ABSORB≥60 points) gets **R² = 0.977**.
  Both comfortably beat the linear fit at equal parameter count.
- `git log --oneline -- experiments/071.../run.py`: `run.py` was introduced
  in exactly one commit, `1bd57d2` ("Phase 3 synthesis — all 7 mandatory
  fixes implemented, predictions frozen BEFORE any run"). The
  `FROZEN_PREDICTIONS` string and `score_settle_c60c70()`'s docstring, which
  describe two different scoring conventions for Block SETTLE-C60C70 (see
  §2 attack 3), were both introduced in that single commit — confirmed, not
  later drift.
- Read `lab/fdtd2d.py::Sim._damping` directly: cubic ramp
  `(arange(absorb,0,-1)/absorb)**3`, `exp(-0.30·d)`, applied as a bare
  post-update multiplicative mask on the field arrays (`self.Ez *=
  self.damp_e`, etc.) — no `σE` current, no dispersive `ε''(ω)`, confirming
  MATERIALS'/THERMODYNAMICS'/EM's shared characterization exactly.

All six blind Phase-5 reviews are independently well-founded on the record.
None is overridden below; several are sharpened, and one arithmetic slip
(QUANTUM's own §6(a) cost estimate) is caught that none of the six reviews
caught in each other.

---

## 1. Adjudication of the six flagged cross-seat convergences

### 1.1 THERMO/EM/QUANTUM: `PAD = ABSORB − 40` — is "shared-geometry, NOT ABSORB-tied" well-posed?

**Independently confirmed real, and confirmed NOT outcome-determining this
cycle, but real enough to require a standing forward constraint on any
future reuse of this congruent series for causal attribution.**

Verified directly (§0): `PAD = ABSORB − 40` exactly at all four congruent
points, and every absolute position (`nx, ny, src_x, plane_x, obj_x,
obj_y`) shifts in lockstep with it — only the *relative* quantities
(`A=752`, `aperture_cells=1504`, `clear_plane=37`, `clear_src=20`) are
genuinely held fixed. This means the single ABSORB axis this cycle
manipulates is, in fact, a **compound axis**: `ABSORB` (sets the
*strength*/depth of the damping ramp) and `PAD` (sets the *round-trip
path length* to the boundary and back, via `NX`/`NY`) move together by
construction, with no config in the series holding one fixed while varying
the other.

The asymmetry the task frames matters and is real, but it cuts differently
on the two branches, and I want to be precise about which:

- **A hypothetical CONFIRM would have been mislabeled.** `P-071-2`'s
  CONFIRM branch is titled `CONFIRMED_ABSORB_TIED_NUMERICAL_BOUNDARY_EFFECT`.
  Given the exact collinearity, a genuine trend on this axis could equally
  be driven by the boundary's *depth* (ABSORB, an amplitude/reflectivity
  story, EM's §2) or by the *round-trip distance to it* (PAD, a
  path-length/phase story) — this design cannot separate the two. A CONFIRM
  branded "ABSORB-tied" would overclaim exactly the causal specificity the
  label promises.
- **A hypothetical REFUTE would NOT have been equally mislabeled.** A flat
  trend on the *compound* axis rules out sensitivity to *both* candidate
  quantities simultaneously (they move together; if the sum is flat,
  neither component is doing anything measurable at this resolution) — so
  "not ABSORB-tied" is a safe corollary of a genuine REFUTE, even though
  "shared-geometry" as the *specific, positive* alternative mechanism (edge/
  `TAPER`-diffraction interference) is not thereby *proven* — only "not
  sensitive to this compound axis" is.

So the task's own framing — "was REFUTE never well-posed as a distinct
alternative from ABSORB-tied?" — is subtly off: **REFUTE remains well-posed
(it would validly rule out both candidates together); it is CONFIRM whose
causal label the confound compromises.** This is a real design flaw, but it
attaches asymmetrically to the outcome the cycle did NOT reach.

**Does it matter given the actual verdict was NEITHER?** No, not
retroactively — NEITHER makes no causal attribution claim in either
direction, so nothing in the committed record is mislabeled by this gap.
But it is a **genuine, previously-undetected gap in this cycle's own
causal-inference logic**, independent of the outcome, and it is more
serious than a same-cycle catch: this exact congruent series (`C40/C60/C70/
C80`, `dg065.CONFIGS`) has now been reused unmodified for T28 causal work
across **three consecutive cycles** (Iteration 46/exp-069's Block DENSE,
Iteration 47/exp-070's per-config decomposition, Iteration 48/exp-071's
explicit causal test) without this confound ever being named in a proposal,
a Phase-2 critique (including my own Phase-2 audit this cycle, which missed
it — see §2, attack 6), or a Phase-3/4 document. Three independent blind
Phase-5 seats (THERMO, EM, QUANTUM) converging on it unprompted in the same
cycle is a strong signal it is real, not overread.

**Ruling:** real, confirmed, not outcome-determining this cycle, **elevated
to a mandatory forward constraint** (§4 below) rather than a Checkpoint
firing — see §5.

### 1.2 VISION/QUANTUM: was "the resolution-floor gate was decisive" accurate?

**Independently confirmed: the write-up's causal narrative is wrong, not
merely imprecise.** Directly from `results.json["trend"]`:

```
raw_confirm      = False   (spread_40_80=3.90% fails the 30% CONFIRM floor on its own)
raw_refute       = False   (R²=0.8664 fails the R²≤0.30 REFUTE ceiling on its own)
unresolved_only  = False   (the resolution-floor branch of the NEITHER-reason
                             logic in run.py::main was never even reached)
```

`raw_confirm` fails because `spread_40_80` (3.90%) is nowhere near the 30%
floor — a fact that has nothing to do with resolving power. `raw_refute`
fails because `R²` (0.8664) is nowhere near the 0.30 ceiling — again
nothing to do with resolving power. **Both pre-committed raw bands would
already miss, with or without the resolution-floor gate, from the
pre-registered thresholds alone.** `run.py`'s own `combined_reason` logic
confirms this precisely: the actual string that fired is the plain
gray-zone catch-all (`"raw trend statistic (spread/R^2) landed in the gray
zone..."`), not the resolution-floor branch — `unresolved_only=False` means
that branch's `if` was never entered.

Yet `phase4_results.md` states, verbatim: *"Resolution-floor gate
(mandatory fix 2) — decisive... The mandatory resolution-floor gate did its
job — it prevented this cycle from reporting either a false CONFIRM... or a
false REFUTE."* `NOTES.md`'s Learned §1 goes further, into a false
counterfactual: *"Without the resolution-floor gate, this cycle would
likely have reported a spurious REFUTE (max_pair_spread clears 15%)."*
This counterfactual is checkable and wrong: removing the resolution floor
entirely and re-scoring the *exact same data* against the unmodified
pre-committed REFUTE band (`max_pair_spread≤15% AND R²≤0.30`) still yields
NEITHER, because `R²=0.8664` already fails that band's own second conjunct
with no floor involved at all.

**I go one step further than VISION's and QUANTUM's own reviews here**:
this is not merely a narrative imprecision — it is a **verified internal
inconsistency** between `run.py`'s own executed logic (correct) and the
prose of `phase4_results.md`/`NOTES.md` (wrong), inside the same committed
record, and it has now propagated into the **git commit message itself**
(`d5fe629`: *"Phase 4 result — Combined Verdict NEITHER, resolution floor
is the reason"*) — a durable artifact none of the six Phase-5 reviews
checked. This is the single most citable wrong claim in the record: a
future reader who greps commit history or skims `phase4_results.md`'s bolded
line, rather than reading `combined_reason` in `results.json`, will carry
forward a false causal story about why this cycle landed NEITHER.

**What the resolution floor actually *is* good for, correctly**: it is
real, correctly computed, prospectively load-bearing (it would have
overridden a raw CONFIRM or REFUTE had the raw stat cleared either band,
and Red Team's own Phase-2 extension showing the CONFIRM band sits at only
75% of full resolving power is sound and important for any future,
differently-parameterized run) — but it was not the proximate cause of
*this run's* verdict. **Tagged [inconsistency] — mandatory same-shift fix,
§4.**

### 1.3 VISION/QUANTUM: the `resolved=True` bug on the exact C70/C80 tie

**Confirmed exactly, both the bug and its non-load-bearing status this
cycle.** `rayleigh_resolution_ratio()`'s own docstring: *"Two periods
identical returns +inf... treated as unresolved by the caller, never as a
false REFUTE."* The caller, `score_trend_and_pairs()`, computes
`resolved=bool(ratio >= dg.RESOLUTION_FLOOR_RATIO_THRESHOLD)` with no
`isfinite` guard — `float("inf") >= 1.0` is `True` in Python. Directly
confirmed in `results.json["trend"]["pairs"]`: the C70–C80 pair shows
`"resolution_ratio": Infinity, "resolved": true` — the opposite of the
function's own documented contract.

**Does it affect THIS cycle's Combined Verdict?** No. `all_pairs_resolved =
all(p["resolved"] for p in pairs)` requires **all six** pairs to be
`True`; the other five are independently `False` (ratios 0.081/0.095/0.095/
0.014/0.014), so `all_pairs_resolved=False` regardless of this bug's
mislabel on the sixth. Directly confirmed: even flipping the buggy pair to
its documented-correct `False` value changes nothing about
`all_pairs_resolved`, `trend["refute"]`, or `combined_verdict`.

**But it is a live, latent bug, not a cosmetic one.** A future reuse of
this exact pairwise-scoring machinery on a smaller or differently-shaped
config set — one where an exact discretization tie sits *alongside* pairs
that genuinely clear the floor — would let a wholly uninformative
coincidence count as "the most resolved pair of all" toward a REFUTE
verdict, silently. **Tagged [inconsistency] (code contradicts its own
documented contract) — mandatory same-shift fix, §4.**

### 1.4 MATERIALS/THERMO: the caveat-wiring gap into `combined_reason`

**Confirmed exactly in code, and confirmed non-load-bearing for what was
actually printed/committed this run, but confirmed genuinely worse for the
untested branches than either review stated.** Read `run.py::main` lines
515–546 directly:

| Branch | Caveats appended to `combined_reason` |
|---|---|
| `CONFIRMED` | `ABSORB_NOT_MATERIAL_CAVEAT` only |
| `REFUTED` | **none** |
| `NEITHER` (this run) | `THERMO_SCOPE_CAVEAT` only |

`WAVELENGTH_SCOPE_CAVEAT` is appended in **zero** of the three branches.
Both MATERIALS and THERMODYNAMICS independently found this; neither named
that the `REFUTED` branch — the one that most directly asserts an
ABSORB-related physical conclusion ("shared-geometry, NOT ABSORB-tied") —
has **zero** caveats wired into its own `combined_reason` string at all,
the worst case of the three, not merely an incomplete one.

**Was anything actually miscommunicated in the ACTUAL committed output?**
No. This cycle's `combined_verdict` is `NEITHER`; the printed tail
(`"COMBINED VERDICT: NEITHER"` + `combined_reason`) correctly carries
`THERMO_SCOPE_CAVEAT`, and a reader of the full `results.json` (the
`caveats` top-level dict) or the full stdout (`FROZEN_PREDICTIONS`, printed
unconditionally before any FDTD call) gets all three caveats regardless.
For *this run's own record*, nothing was silently dropped from the
artifact as a whole — only from the specific string welded to the verdict
line. Since NEITHER makes no ABSORB-tied claim, the missing
`ABSORB_NOT_MATERIAL_CAVEAT`/`WAVELENGTH_SCOPE_CAVEAT` next to *this run's*
verdict line is non-load-bearing. **This is a real, cheap, code-structure
fix required before the next cycle that might land CONFIRMED or REFUTED —
not a defect that misled anyone about exp-071 itself.** Tagged
[inconsistency] — mandatory fix, §4.

### 1.5 PHOTONICS/EM: does a saturating model fit better than linear, or is this an R5-family over-read?

**Independently confirmed real and well-supported — genuinely distinct
from the R5 failure shape, not an instance of it.**

My own fit (§0): a 2-parameter saturating exponential (same residual DOF as
the linear model: 4 points, 2 free parameters, 2 residual DOF) achieves
**R²=0.998** against the linear model's **R²=0.866**, and even the crude
2-parameter step/early-saturation model gets **R²=0.977**. This is not a
marginal preference — on identical parameter budget, the saturating family
fits dramatically better, and the *shape* of the fit is exactly what EM's
and PHOTONICS' independent physical arguments predict: a boundary of finite
depth cannot be perfectly reflectionless, residual back-reflection should
fall off geometrically (more lossy layers ⇒ exponentially smaller residual,
with diminishing returns) rather than grow linearly forever, and the raw
sequence (`+0.083°, +0.015°, +0.000°`) is visually and quantitatively a
saturating curve, not a line.

**Why this is NOT an R5/R5-addendum instance:** R5's failure shape requires
(a) many candidate explanations, (b) a target being searched against, and
(c) researcher degrees of freedom in what counts as a match. This is none
of those — it is a comparison between exactly **two**, both
physically-motivated, functional forms (linear vs. saturating), at **equal**
parameter count, on data whose own generating mechanism (a graded-loss
boundary) makes one of the two forms the textbook-expected shape *a
priori*, not selected post hoc from a large space. This is ordinary model
comparison, not a look-elsewhere search.

**The critical caveat neither PHOTONICS nor EM stated as sharply as it
deserves, and that must travel with this finding everywhere it is cited**:
the resolution-floor problem that sank `P-071-2` applies to the *four
underlying point estimates themselves* — `P*(40)`, `P*(60)`, `P*(70)`,
`P*(80)` are each individually Rayleigh-unresolved from their neighbors at
this window (§0, `trend_resolution_ratio=0.095`). **A better-fitting
functional form does not rescue unresolved input data — it only says which
shape the (unresolved, noisy) points happen to trace more smoothly.** Both
the linear R²=0.866 and the saturating R²=0.998 are fits to the same
underprivileged four points; a model comparison this clean on four
under-resolved points is suggestive and mechanistically well-motivated, not
dispositive. **Ruling: a real, verified, well-supported observation —
correctly proposed as a next-step hypothesis (PHOTONICS' two-tone joint
fit, EM's high-ABSORB=120 saturation test), not yet evidence for the
saturating model over the null. Not an R5-family over-read; also not yet a
confirmed physical finding.**

### 1.6 Any additional issues found in this adversarial read, not caught by the six blind reviews

1. **QUANTUM's own §6(a) proposal contains an internal arithmetic error.**
   QUANTUM's Phase-5 review proposes a new `C60'` config (`ABSORB=60,
   PAD=0`) run over "the same 31-point dense window at 600nm," then states
   *"This is a single new config, ~16 FDTD calls."* A 31-point angular
   sweep on one config costs **31** calls, not 16, at this cost basis —
   independently checked against `design_geometry.py::_cost()` and the
   Block DENSE-CAUSAL convention (31 points × 1 config = 31 calls, not a
   halved or averaged figure). A minor, non-load-bearing slip (QUANTUM's
   own review was not scored data, only a forward proposal), but it would
   propagate a wrong cost estimate into Iteration 49 planning if copied
   uncorrected — flagged for correction in the queue write-up (§6).
2. **The git commit message for the Phase 4 result (`d5fe629`) states the
   same overclaim as `phase4_results.md`'s prose** ("resolution floor is
   the reason") — see §1.2. This is worse than a prose overclaim because
   commit history is the artifact most likely to be grepped by a future
   fresh-context agent doing a quick `git log` scan rather than reading the
   full record. House convention in this program is erratum-in-place, not
   history rewriting — recommend the LOGBOOK.md Iteration 48 entry state
   the corrected causal account explicitly and not rely on the commit
   message being read as authoritative.
3. **`FROZEN_PREDICTIONS`'s Block SETTLE-C60C70 text contradicts
   `score_settle_c60c70()`'s own docstring, introduced in the same commit**
   (independently confirmed via `git log`, §0) — this is VISION's Finding B,
   independently re-verified here as accurate and, notably, **not
   caught by five blind Phase-2 critiques or my own Phase-2 audit this
   cycle either** (the docstring/prose split only exists once `run.py` is
   written at Phase 3, after Phase 2 closes — structurally impossible for
   Phase 2 to have caught it, not a Phase-2 process failure). It did not
   affect the outcome (the code, which is correct per idealization 10, is
   what ran) but is exactly the "committed prose and executed code cannot
   drift apart" failure this program's own non-negotiable discipline exists
   to prevent — and it happened at the moment of freezing, not later.
4. **The design's own null-permutation-control section (idealization 5 /
   Phase-1 §"Null-permutation-control question") is correctly reasoned as
   written** — this is not a combinatorial search, R5/R5-addendum does not
   apply, confirmed independently. No new finding here beyond what Phase 2's
   own Red Team audit (attack 3) already established.
5. **No caveat-lint registry entry exists for exp-071's own headline
   numbers** (`R²=0.8664`, `spread=3.90%`), confirmed live: `grep -c
   "071" lab/caveat_lint_config.json` returns 0. This regresses the exact
   registry-propagation practice exp-070 established one cycle ago for the
   structurally identical risk shape (a raw statistic that looks decisive
   quoted without its disqualifying context) — VISION's Finding D,
   independently confirmed here by direct `grep`, not by trusting VISION's
   own claim.

---

## 2. Numbered attacks

1. **[inconsistency]** `phase4_results.md`'s "Resolution-floor gate —
   decisive... prevented... a false CONFIRM or REFUTE" and `NOTES.md`'s
   Learned §1 counterfactual ("would likely have reported a spurious
   REFUTE") both contradict `run.py`'s own executed `combined_reason` logic
   (`raw_confirm=False`, `raw_refute=False`, `unresolved_only=False` —
   both raw bands already miss on their pre-registered thresholds alone,
   with or without the resolution floor). Propagated into the Phase-4 git
   commit message (`d5fe629`). Real, verified, mandatory same-shift
   correction (§1.2, §4).
2. **[inconsistency]** `rayleigh_resolution_ratio()`'s docstring promises
   an exact-tie pair (`+inf`) is "treated as unresolved by the caller,
   never as a false REFUTE"; the actual caller does not special-case
   infinity, and `results.json` shows the C70–C80 tie flagged
   `"resolved": true`, the documented-opposite value. Non-load-bearing this
   cycle (§1.3); live latent bug for future reuse. Mandatory same-shift
   fix, §4.
3. **[inconsistency]** `run.py`'s `FROZEN_PREDICTIONS` string (Block
   SETTLE-C60C70) describes a 1400-STEPS-relative scoring convention;
   `score_settle_c60c70()`'s own docstring and actual implementation use a
   GATE_HARD-relative convention instead, correctly per idealization 10 —
   both introduced in the same Phase-3 commit (`1bd57d2`), a
   self-contradiction present at the moment predictions were "frozen before
   any run" (§1.6 item 3). Non-outcome-affecting (the correct code ran);
   mandatory same-shift text correction, §4.
4. **[inconsistency]** `combined_reason`'s per-branch caveat wiring is
   incomplete in all three branches (CONFIRMED: 1 of 3 caveats;
   REFUTED: 0 of 3; NEITHER: 1 of 3), contradicting `NOTES.md`'s/
   `phase4_results.md`'s claim that caveats are "disclosed unconditionally,
   printed with every result regardless of outcome" — true of the artifact
   as a whole, false of the string welded to the verdict line in two of
   three branches. Non-load-bearing for this run's own NEITHER verdict
   (§1.4). Mandatory same-shift fix, §4.
5. **[constraint-#N/A — causal-inference-logic gap, program-integrity
   attack, my own extension of THERMO/EM/QUANTUM's convergent finding]**
   `PAD = ABSORB − 40` exactly across the entire congruent series this and
   the two prior T28 cycles have reused unmodified; a hypothetical CONFIRM
   on this series would have been mislabeled "ABSORB-tied" when it could
   equally be PAD/path-length-tied. Real, independently confirmed (§1.1),
   not outcome-determining this cycle (verdict is NEITHER, which survives
   the confound), but unflagged in any proposal, critique, or synthesis
   document across three consecutive cycles until this cycle's Phase 5 —
   elevated to a **mandatory forward constraint** on any future causal use
   of this series (§4, §5).
6. **[not a defect this cycle, flagged for the record]** QUANTUM's own
   Phase-5 §6(a) proposal misstates its own cost estimate (31-point dense
   sweep on one new config costs 31 calls, not "~16"). Non-load-bearing
   (a forward proposal, not scored data) but would misstate Iteration 49's
   budget if copied uncorrected. Corrected in the queue recommendation,
   §6.
7. **[not a defect — checked and cleared]** `A=752`/`aperture_cells=1504`
   congruence, the G1 identity gate, the R3-rescale construction
   (`STEPS_r3 = STEPS_native × cpl_r3/cpl_native`, ABSORB/PAD cell counts
   scaled by `R3_RATIO` to hold physical thickness fixed), and the peak-
   angle verification (0.949/0.984 of window ptp, genuinely near extrema,
   not the original zero-crossing cells) are all independently re-verified
   sound. No attack found here.

No fabricated or unverifiable number was found anywhere in the six-document
record. All six Phase-5 reviews earn their findings; none contains a
spurious claim.

---

## 3. Verdict on the Combined Verdict (NEITHER)

**Stands, independently confirmed.** G1 passed 4/4 bit-exact (re-verified,
§0). Both binding preconditions (Block SETTLE-C60C70, P-071-4) genuinely
CONFIRM under independent re-derivation (settling shifts 2–4 orders of
magnitude under `GATE_HARD`; peak-cell R3 ratios 1.234/1.047, cleanly
inside `[0.3,3.0]`). The raw trend statistic (`spread_40_80=3.90%`,
`R²=0.8664`) genuinely fails to clear either pre-registered band **on the
raw thresholds alone**, independent of the resolution-floor gate (§1.2) —
so NEITHER is doubly secured: by the pre-committed conjunctive bands
directly, and separately by the resolution floor, which (correctly) shows
neither band could be trusted here even had it cleared. None of the six
attacks above changes this outcome. The PAD/ABSORB confound (attack 5)
would have compromised a hypothetical CONFIRM's causal label but does not
touch NEITHER's validity. **This is an honest, correctly-computed NEITHER,
not a hedge, and the mandatory-fix docket from Phase 2 genuinely did its
job** (both of Red Team's own Phase-2 severe findings — settling closure,
resolution floor — were real, testable, and came back clean, exactly the
discipline working as intended) — but the record's *narrative* about why it
is NEITHER requires the same-shift corrections below before it is safe to
cite.

---

## 4. Same-shift mandatory-fix docket

All items below are cheap (text and/or a one-line code change), zero new
FDTD cost, and should be applied before this cycle's LOGBOOK.md entry is
drafted from it, per this program's own precedent (exp-069/070).

1. **Correct the resolution-floor narrative** in `phase4_results.md` and
   `NOTES.md`'s Learned §1 (erratum convention, scored values untouched):
   replace "decisive"/"prevented a spurious REFUTE" language with the
   accurate account — both raw bands already miss on their pre-registered
   thresholds alone (`raw_confirm=False` on the spread conjunct,
   `raw_refute=False` on the R² conjunct); the resolution-floor computation
   is real, correctly implemented, and prospectively load-bearing (it will
   matter on a run whose raw stat lands closer to either band), but was not
   the proximate cause of *this run's* NEITHER. Note the same overclaim
   also appears in the `d5fe629` commit message; state the correction
   explicitly in the LOGBOOK entry rather than relying on `git log`.
2. **Patch the `resolved` tie-handling bug**: change
   `resolved=bool(ratio >= dg.RESOLUTION_FLOOR_RATIO_THRESHOLD)` to
   `resolved=bool(math.isfinite(ratio) and ratio >= dg.RESOLUTION_FLOOR_RATIO_THRESHOLD)`
   in `score_trend_and_pairs()`, matching `rayleigh_resolution_ratio()`'s
   own documented contract. Re-run `run.py` (or re-derive `results.json`'s
   affected field only) to confirm `resolved: false` for the C70–C80 pair;
   `all_pairs_resolved` and the Combined Verdict are unaffected (already
   verified, §1.3).
3. **Reconcile `FROZEN_PREDICTIONS`'s Block SETTLE-C60C70 text** with
   `score_settle_c60c70()`'s actual GATE_HARD-relative construction —
   correct the prose to match the code that ran (idealization 10 already
   has the correct description; the `FROZEN_PREDICTIONS` string does not).
4. **Append all three caveat constants** (`ABSORB_NOT_MATERIAL_CAVEAT`,
   `THERMO_SCOPE_CAVEAT`, `WAVELENGTH_SCOPE_CAVEAT`) to `combined_reason`
   uniformly in all three branches (`CONFIRMED`, `REFUTED`, `NEITHER`), not
   just the current partial coverage — the `REFUTED` branch currently has
   zero.
5. **Add a `lab/caveat_lint_config.json` entry for exp-071**, mirroring
   exp-070's own precedent, protecting the headline `R²=0.8664`/
   `spread=3.90%` numbers and the `P*(ABSORB)` per-config table from future
   citation without their disqualifying resolution-floor and PAD-confound
   context. Re-run `lab/caveat_lint.py` to confirm 0 required-site failures
   with the new entry live.
6. **Add an explicit idealization/caveat naming the `PAD=ABSORB−40`
   collinearity** to `NOTES.md` and `phase4_results.md` (currently absent
   from both, surfaced only in three Phase-5 reviews) — state plainly that
   any future CONFIRM on this exact congruent series describes an
   ABSORB-*or*-PAD-tied effect, not specifically ABSORB-tied, until a
   PAD-decorrelated config exists (§6, item 1).
7. **Correct QUANTUM's Phase-5 §6(a) cost estimate** (31 calls, not "~16")
   before it is copied into any Iteration-49 proposal or budget.

---

## 5. Checkpoint determination — all five criteria, explicit

1. **A configuration passes ALL constraint metrics.** Does not fire. T1
   route N/A throughout; constraint 3 is not engaged by an
   instrument/mechanism-identification cycle, by design.
2. **A proven boundary — a constraint subset shown jointly unsatisfiable
   within a mechanism class.** Does not fire. Nothing here bounds a
   mechanism class; T28 remains an open instrument question, narrowed not
   resolved.
3. **A synthesis requires engine physics beyond the validated bench
   classes.** Does not fire. Zero `lab/` diff throughout, confirmed
   (`assert_lab_clean()` passed at run start, `git diff --stat -- lab/`
   reconfirmed clean after).
4. **Red Team flags program-integrity drift (unfalsifiable claims, a
   constraint quietly dropped — especially #3).** **Does not fire, but this
   is the closest call of the five criteria this cycle, and I want to state
   why explicitly rather than wave it through.** Attacks 1–4 (§2) are all
   real internal inconsistencies, but each was caught within this cycle's
   own Phase 5, before any LOGBOOK entry was drafted from it — the
   established non-firing precedent (Iterations 19/23/38/42/43/46/47: the
   process catching real defects before they propagate is the discipline
   working, not a defect in it). Attack 5 (the PAD/ABSORB confound) is a
   materially different *species* of finding: it is not a defect
   introduced this cycle, but a foundational design property of a
   congruent series (`dg065.CONFIGS`) that three consecutive T28 cycles
   (46/47/48) have reused for causal-adjacent purposes without ever naming
   it, until three independent blind Phase-5 seats converged on it
   unprompted this cycle. It did not survive undetected into a *published*
   causal claim (this cycle's own verdict is NEITHER, immune to the
   confound), so the specific aggravating fact that has fired criterion 4
   before — a defect surviving an entire cycle's five-phase process
   undetected, or a violated pre-committed tripwire — is genuinely absent
   here too. **Ruling: does not fire**, on the same logic as the program's
   established precedent, but flagged as a standing forward constraint
   (§4 item 6, §6) rather than a closed matter — if a future cycle runs a
   CONFIRM on this exact series without decorrelating PAD first, *that*
   would be the aggravating fact this criterion is built to catch.
5. **Two consecutive iterations with no logbook-advancing result.** Does
   not fire. This is the third consecutive PARTIAL/non-decisive T28 cycle
   (46, 47, 48), but each has delivered independently verifiable,
   load-bearing narrowing: 46 discovered and settled T28 itself; 47 killed
   one sub-hypothesis clean (`TAPER`-alone) and established the
   null-permutation-control house rule; 48 (this cycle) closes the C60/C70
   settling-closure gap for the first time, formally establishes a
   prospectively-load-bearing resolution floor, surfaces a real,
   independently-confirmed saturating-mechanism candidate (§1.5,
   R²=0.998 vs. 0.866 at equal parameter count), and surfaces the
   PAD/ABSORB confound for the first time in the program's history — each
   a genuine advance, matching Iterations 46/47's own precedent for what
   counts as "advancing." **Does not fire** — but flagged: if Iteration
   49 also lands non-decisive without a comparable concrete advance, this
   pattern deserves scrutiny on its own terms, not only via this criterion.

**No Checkpoint criterion fires.**

---

## 6. Ranked queue recommendation for Iteration 49

Reconciling all six seats' Phase-5 proposals against T28's actual open
question — does the ~2.8°-family period genuinely depend on `ABSORB`
depth, and if so via what mechanism — ranked by value-per-cost and by how
directly each closes a gap this cycle actually surfaced:

**1. MERGE EM's differential/beat-fit and QUANTUM's item (b) into one
Iteration-49 item — zero new FDTD cost, run first, same-shift if capacity
allows.** These are substantively the same proposal: fit
`delta_AB(θ)=C_B(θ)−C_A(θ)` directly for every adjacent pair (C40–C60,
C60–C70, C70–C80, plus the already-analyzed C40–C80) instead of
independently fitting absolute periods and subtracting. Both EM and
QUANTUM independently derive the same reason this is more powerful: it
converts an absolute-frequency Rayleigh-resolution problem (which QUANTUM's
own §5 shows is *unsolvable at any achievable window* for the C60–C70 pair
specifically, `Δsinθ≥5.76` vs. a max achievable `2.0`) into a
phase-accumulation/beat-detection problem, whose required resolution scales
with the *separation* being tested rather than with resolving two
near-identical absolute carriers. Reuses `results.json`'s own already-
collected 124 points, zero new calls. **This is the single highest
information-per-cost move available and directly reuses the exact
methodology that discovered T28 in the first place** (`C80−C40`,
`ptp/mean=16.2`). Fix QUANTUM's own §6(a) cost slip (attack 6) if any part
of its proposal is folded in alongside.

**2. Merge THERMODYNAMICS' matched-PAD amplitude probe and QUANTUM's item
(a) (PAD-decorrelation via period) into one new-config Iteration-49 build.**
Both independently propose the same structural fix — a config that holds
`PAD` fixed while `ABSORB` varies (or vice versa) — for the same reason:
this is the only way to close attack 5 (§1.1, §2) directly. Building the
config(s) once and scoring **both** metrics on the same run (THERMO's
resolution-floor-free `ptp(C_empty)` amplitude *and* QUANTUM's free-period
fit) doubles the value of one FDTD spend rather than running two separate
batches. THERMO's own falsifiable band (≥10% amplitude rise at fixed PAD ⇒
ABSORB-tied; ≤3% ⇒ PAD/geometry-tied) is a genuinely resolution-floor-free
discriminator and should be the primary scored metric; the period fit rides
along as a secondary, floor-caveated observation. Cost: ~62–93 calls
(THERMO's own estimate for 2 configs × 31 angles), comparable to this
cycle's own Block DENSE-CAUSAL.

**3. MATERIALS' mask-functional-form ablation** — hold `ABSORB` fixed
(e.g. `C80`) and vary the damping ramp's exponent/decay constant at fixed
cell depth. Cheap (a handful of calls, zero new geometry), and answers a
question genuinely orthogonal to items 1–2: is the periodicity tied to a
*length scale* at all (as `ABSORB`-in-cells would proxy), or to the
numerical decay *profile* of the mask, which has no length-scale
referent whatsoever? Lower priority than 1–2 because it doesn't directly
engage the PAD confound that three seats converged on, but it is the
cheapest way to rule out a purely-numerical, non-geometric origin
entirely.

**4. PHOTONICS' joint two-tone fit** (zero-cost, desk-only re-analysis of
already-collected data) and **EM's new ABSORB≈120 config** (31 calls, tests
the saturation prediction directly) should run together, informed by item
1's result — both are direct tests of the saturating-mechanism candidate
independently confirmed real in §1.5 (R²=0.998 vs. 0.866). The two-tone fit
is free and should run regardless of budget; the new high-ABSORB config is
the more direct falsification test (a continued, non-saturating shift at
ABSORB=120 would disfavor the saturating-reflection story) and should be
scheduled if items 1–2 leave capacity.

**5. VISION's general guidance — do not reuse the 36°–42° window a third
time for an absolute-period discriminator; pin the required window size (or
switch discriminator) in code before any new FDTD call.** Not a rankable
item on its own; a binding design constraint that applies to any part of
items 2–4 involving new FDTD spend, and is already substantially satisfied
by item 1's shift away from absolute-period fitting toward differential/
beat fitting.

**R_contact's `measured_direct` literature search** (PLAN.md queue item 2,
9 consecutive cycles blocked on WebSearch/WebFetch tooling) remains
unchanged in ranking relative to T28 work — still the only item that can
move a real, sourced materials number, still outside this cycle's own
locked scope; the Director's tooling-availability disclosure (`phase3_
synthesis.md`) should be acted on independently of T28's own queue
ordering above.
