# Phase 5 Review — VISION SCIENCE

**Panel Iteration 54, exp-077 (T28 `PAD` round-trip-distance echo model
refit). Fresh sub-agent, blind to all other Phase-5 reviews this cycle —
including any Red Team final audit — even though my own seat led this
cycle's Phase 1 by rotation.** Charter: human perceptual limits — contrast
thresholds, luminance edge detection, spectral sensitivity, adaptation,
temporal sensitivity; central question: what would make a human eye FAIL
to register something physically present; duty: pin numeric thresholds,
with sources, BEFORE any run that scores against them.

Read in full before writing this review: `PANEL.md`; `LOGBOOK.md` (RULED
OUT R1–R8; LIVE THREADS T16 in full, T28's complete Iteration 46–53
history); `phase1_proposal.md` (my own cycle's original proposal, as
corrected post-Phase-2/3/4), `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `phase4_results.md`, `NOTES.md`,
`pad_round_trip_model.py`, `pad_round_trip_results.json` — and, because
this cycle's own mandate traces every number to exp-076, its full record
(`phase1_proposal.md`, `NOTES.md`, `results.json`,
`phase5_review_vision.md`, `phase5_redteam_audit.md`) and `experiments/072-
.../run.py` (the `amp_ratio` machinery's original source).

---

## 1. Verdict: **PARTIAL**

Consistent with every T28 Phase-5 verdict since Iteration 46. The coherent
single/two-wall echo mechanism class — the one mechanism exp-076's own
lossless-vacuum proof left physically permitted for `PAIR_PAD` — is
REFUTEd, robustly, on the complete instrument (I independently re-verify
this in §2 below; it is not my seat's physics to dispute and it holds up).
T28's own substantive mechanism question is not answered by this cycle;
nothing here forecloses future mechanism candidates. My own charter has no
scene to score (T1 N/A is correct throughout, §3) — but my duty ("pin
numeric thresholds ... before any run scores against them") is directly
engaged by a real, load-bearing error in how this exact sub-thread has
been characterizing its own signal size against my seat's own pinned bar,
found this cycle (§2) and owed a correction to the permanent record.

---

## 2. Independent check — including a correction to this sub-thread's own headline magnitude claim

### 2a. The mechanism REFUTE itself, re-verified (light touch — not my charter's physics, but R4 requires it)

Ran `pad_round_trip_results.json` values directly against the tables in
`phase1_proposal.md`/`phase4_results.md` — bit-exact:

```
PAIR_PAD:      single-wall rel_dev=1.87976  r²=0.04440  → REFUTE (period+shape)
               two-wall    rel_dev=0.87968  r²=0.00009  → REFUTE (shape alone)
PAIR_ABSORB40: single-wall rel_dev=0.96415  r²=0.19966  → INCONCLUSIVE
               two-wall    rel_dev=0.68509  r²=0.04176  → REFUTE (flipped)
Gates: G-LOSSLESS 2.220e-16, G-N1 1.404e-15, G-PASSIVITY worst|r|=0.006423 — all PASS
Null calibration: P(R²≥0.70)=0.0/20000 pure-noise trials (max 0.5609) vs real R²=0.8165
```

Every number reproduces exactly from the committed JSON, independent of
the prose. Four independent implementations (PHOTONICS, EM, Red Team,
this Phase-4 run) already agree to 4 decimal places — I have nothing to
add or subtract from that physics finding. **Combined REFUTE for both
pairs, on the complete two-wall instrument, stands.**

### 2b. The task's own framing, checked: is `x=amp_ratio(PAIR_PAD)=0.119` really "~24× C_thr"?

The brief for this review states the premise as established fact, quoting
`LOGBOOK.md`'s own T16 entry (Iteration 53): *"a domain-padding choice
ALONE ... can move this channel's signal by `x=amp_ratio(PAIR_PAD)=0.119`
at a fixed `ABSORB` depth, ~24× VISION's own pinned lab detection bar
(`C_thr=0.005`)."* I checked this by recomputing `amp_ratio` from its own
primitives rather than accepting the ratio as already comparable to
`C_thr`, and it does not survive the check.

`amp_ratio = √(A_i²+A_q²) / amp` (`experiments/072-.../run.py:172,286`),
where `amp` is **not a fixed reference scale** — it is itself a *fitted
carrier amplitude*, the size of the shared common-mode fringe oscillation
present in both configs being differenced. Independently recomputed from
`experiments/076-.../results.json::headline`:

```
PAIR_PAD:      A_i=6.0811e-4  A_q=-9.3774e-5  amp(carrier)=5.15476e-3
               raw = sqrt(A_i^2+A_q^2) = 6.1530e-4
               amp_ratio = raw/amp = 0.119366  (reproduces exactly)
PAIR_ABSORB40: A_i=1.5144e-4  A_q=-3.6468e-4  amp(carrier)=5.51382e-3
               raw = sqrt(A_i^2+A_q^2) = 3.9488e-4
               amp_ratio = raw/amp = 0.071616  (reproduces exactly)
```

`amp_ratio` is a **ratio of two amplitudes, both already in `C_empty`
units** — it answers "how big is the `PAD`-tied difference relative to the
local fringe it rides on," a fraction with no dimensions. `C_thr=0.005` is
a threshold on a *raw* `C_empty`/Weber-contrast magnitude (I confirmed
`C_empty(θ)` really is computed by `lab/ambient.py::contrast_from_runs`,
the identical formula every constraint-3 `C` citation in this program
uses — `experiments/069-.../run.py:150-154` — so a raw-magnitude
comparison to `C_thr` is at least dimensionally well-formed). Dividing a
*dimensionless ratio-of-amplitudes* by an *absolute contrast threshold* —
`0.119366 / 0.005 = 23.87`, the "~24×" figure — compares two different
kinds of quantities. The dimensionally-consistent comparison is the raw
oscillation amplitude itself, `sqrt(A_i²+A_q²)`, against `C_thr`:

```
PAIR_PAD:      6.1530e-4 / 0.005 = 0.123×   (≈8× BELOW C_thr, not 24× above)
PAIR_ABSORB40: 3.9488e-4 / 0.005 = 0.079×   (≈13× BELOW C_thr, not 14× above)
```

This is not a new instrument, a new run, or a reinterpretation of
`PAD_TIED` — every input number is already committed, and my own
recomputation matches `results.json` to 5+ significant figures throughout.
It is a correction to which of two already-computed numbers belongs on
the right side of a division by `C_thr`.

**This is not a fresh mistake — it is a mistake this exact sub-thread
already named and then made anyway.** `experiments/076-.../NOTES.md`
Idealization 11 states, in the program's own permanent record: *"no basis
for reading any `amp_ratio` figure (e.g. `x=0.119`) as a multiple of a
perceptual threshold."* The prior VISION seat's own Phase-5 review
(`experiments/076-.../phase5_review_vision.md` §2) drafted exactly this
warning at Phase 2 — *"a reader ... could plausibly misread '0.119' as
'24× the lab detection bar' ... when it is a relative-to-a-vacuum-field-
ratio magnitude with no perceptual referent at all"* — flagged it as
disclosed-but-dropped (never adopted into `NOTES.md` or either disposition
table), and then, in the very same document's §4, wrote the headline line
this cycle inherited verbatim: *"a domain-padding choice ... can move this
channel's own signal by an amount ~24× VISION's own lab bar."* Red Team's
own Phase-5 final audit for that cycle (`phase5_redteam_audit.md` line 61)
"confirmed" this — but only confirmed the *arithmetic* (`0.119366/0.005 =
23.87`, correct as division), not whether `amp_ratio` was the right
numerator to divide by `C_thr` in the first place — and then mandated
(docket item 4) that the figure be written into `LOGBOOK.md`'s permanent
T16 entry, which is exactly what happened and exactly what this cycle's
own task brief quotes as settled fact. **A unit error survived one seat's
own explicit warning against it, one Red Team arithmetic re-check that
verified the wrong thing, and landed in `LOGBOOK.md`'s standing record —
where it was then handed to a second, independent VISION seat (me) as
established ground truth.** This is precisely the "verified but wrong"
shape R4/R8 exist to catch, one level removed: here the number that was
"independently re-verified" was correct arithmetic on an invalid
comparison, not a false claim about a valid one — a variant this
program's rule language has not previously named. I am not overriding the
Combined Verdict of exp-076 (unaffected — `PAD_TIED`'s classification,
the 750nm ordering flip, MATERIALS' realizability finding all stand
unchanged) or exp-077's REFUTE (§2a, likewise unaffected, and not
perceptual in nature). I am flagging that the specific figure used to rank
`PAD_TIED`'s *urgency* on the T16 floor-uncertainty ledger is, on a
unit-consistent recomputation, backwards in magnitude: this contributor is
one of the *smaller* ones by the standard T16 already applies elsewhere
(compare `experiments/056/058`'s own `|C_joint|` citations, e.g. "11.1–
11.6× `C_thr`," which correctly divide a **raw** `C`-quantity by `C_thr`,
not a ratio already normalized by something else) — not the largest, as
currently written.

---

## 3. Is there a legitimate vision-science question this thread has been avoiding — does a signal of *this size* bear on perceptibility, independent of mechanism?

Two-layered, and the correction in §2b changes the shape of both layers.

**Layer 1 (already correct, not newly found by me): no, not yet, and not
because of the mechanism gap — because there is no scene.** Every config
this six-cycle sub-thread has ever scored (`C40`/`C60`/`C70`/`C80`/`G40`)
is an *empty* scene — no absorber, no PEC, no article of any kind
(confirmed directly: `_one_run`/`_c_empty` in `experiments/069-.../run.py`
compute the vacuum reading only, reused verbatim by every cycle through
exp-077). `C_thr` is a threshold on an object-vs-background Weber
contrast; an empty scene has no object, so there is no silhouette to score
`C_thr` against, mechanism or no mechanism. T1's "N/A" disposition, stated
identically in every T28 Phase-1 proposal since exp-069 including this
one, is correct for this reason — not because the mechanism is unknown,
but because the *scene* does not exist. This was already the prior VISION
seat's own finding (exp-076 §4, Layer 1) and I independently reconfirm it:
identifying the mechanism would not, by itself, unlock a constraint-3
score here. What would is Iteration 53's own still-unexecuted Tier-2 item
7 — load a real absorbing article (`graded_black_shell`, or an
`off_pass`-style near-null σ(I) article) at this same window and see
whether the `PAD`-sensitivity survives the object-minus-flank subtraction
real constraint-3 scoring performs, or cancels as a shared background
term. **That is the correctly-scoped version of "does this bear on
perceptibility" — and it is not "avoided" so much as already identified
and twice deferred (Iterations 53, 54) in favor of mechanism-hunting.**

**Layer 2 (the correction from §2b): even the informal "how big is this
compared to `C_thr`" sanity check this program already runs for its other
floor-noise contributors (T21's fringe, T27's settling-transient) has been
run on the wrong number for `PAD_TIED`.** On the unit-consistent
recomputation, the raw `PAD`-tied oscillation is ~0.12× `C_thr` for
`PAIR_PAD` and ~0.08× for `PAIR_ABSORB40` — sub-threshold by roughly an
order of magnitude, not 14–24× over it. So the honest answer to "does a
signal of *this size* bear on perceptibility, independent of mechanism" is
that the premise needs restating before the question can be asked at all:
on the raw `C_empty` scale (the one dimensionally comparable to `C_thr`,
even setting Layer 1's scene objection aside entirely), this is not
currently a "real, large signal" in perceptual-adjacent terms — it is a
small one, smaller than several contributors this program has treated as
more marginal. That does not make `PAD_TIED` uninteresting (the shape/
period fit is real, non-noise structure, confirmed by the 20,000-trial
null above) — it means the *urgency* framing attached to it via the "24×"
figure overstates, by roughly two orders of magnitude, how much perceptual
weight this specific finding should carry relative to T16's other
catalogued floor contributors, until Layer 1's scene test is actually run.

**So: is this correctly out of scope until a mechanism is identified, or
is there a real vision-science question being avoided?** Neither framing
is quite right. It is correctly out of scope *right now*, but the reason
is scene-absence (Layer 1), not mechanism-absence — a mechanism ID would
not unlock scoring by itself. And the specific "large signal" framing that
makes this feel urgent to resolve mechanistically is itself miscalibrated
(Layer 2) — on a corrected, unit-matched reading, this is one of the
*smaller* items on T16's own ledger, which if anything argues for lower
urgency on the mechanism-hunting front and higher priority on finally
running the Layer-1 loaded-article test cheaply, now that four
consecutive cycles (074→077) have spent real analytical effort on
mechanism candidates for a signal whose actual perceptual-adjacent scale
was never correctly stated.

---

## 4. A genuinely different candidate class for Iteration 55: is `PAD`-construction sensitivity itself an instrument-floor artifact, not a physical mechanism at all?

Worth naming explicitly, distinct from anything exp-075/077 tested.

**4a. T16 already effectively classifies it this way — in tension with
exp-075/077's own framing.** `LOGBOOK.md`'s T16 entry (Iteration 53) calls
`PAD_TIED` "a third, independently-confirmed driver of this channel's own
floor uncertainty," joining angular-quadrature sensitivity and domain-
construction sensitivity — both pure numerical/instrument properties with
zero physical content, never treated as candidates needing an EM
mechanism. Yet exp-075 and this cycle have both proceeded as if `PAD_TIED`
needs a *physical* echo mechanism to be REFUTEd or confirmed — an
unexamined tension between how T16 files this finding and how T28 tests
it. Both cannot be the operative frame at once: either `PAD_TIED` is
candidate-physical (worth REFUTE-testing coherent-echo mechanisms against,
as done here) or it is candidate-instrumental (worth testing against the
FDTD engine's own numerical properties instead, never against `r(theta)`
at all). This cycle's REFUTE narrows the first path without addressing
the second.

**4b. A concrete, testable instrumental candidate, not yet tried on
`PAD_TIED` specifically: Yee-grid numerical dispersion, accumulated over
the `PAD`-dependent domain size, applied to the *wrong* phase velocity in
exp-075/077's own model.** `lab/fdtd2d.py` is a standard 2D TMz Yee-grid
leapfrog scheme (`cells_per_lambda=20`, `courant_frac=0.99` — confirmed by
direct read, `lab/fdtd2d.py:72-95`) — such schemes have a well-known,
closed-form numerical dispersion relation whose phase velocity differs
from `c` by an angle- and resolution-dependent amount, generally larger
off-axis (this program's own exp-069 Phase-5 PHOTONICS review already
invokes "ordinary Yee-grid dispersion" as the accepted explanation for a
*different* T21 asymmetry — this is established, not speculative,
machinery in this program). `boundary_reflectance.py`'s transfer-matrix
model computes each wall's round-trip phase using the **vacuum** phase
velocity (`c`), never the engine's own discretized one. Since `PAD`
changes the number of grid cells the wave traverses before reaching the
domain wall (and thus the *accumulated* numerical-dispersion phase error,
even though `PAD` itself adds no material), a coherent-echo mechanism
using the *correct* (Yee-grid, not vacuum) phase velocity has never been
scored against `PAIR_PAD`/`PAIR_ABSORB40` — a distinct hypothesis from
both "REFUTE, no echo mechanism" (this cycle's finding) and "pure
artifact, no physics at all" (4a): the echo mechanism class might not be
as cleanly dead as it looks if the model's own dispersion relation, not
the underlying physics, is what mismatched the period. Zero new FDTD:
`cells_per_lambda`, `courant_frac`, and angle are already known constants;
the standard 2D FDTD dispersion relation is closed-form.

**4c. A second, more purely "no physics required" candidate, closer to
T16's own family**: has `_free_period_search`'s own angular grid, or the
`C_empty(θ)` computation's own angular-quadrature order, ever been checked
for a `PAD`/`nx`-dependent sensitivity independent of any real field
content — the direct T28 analogue of T16's already-measured N9→N17
angular-quadrature sensitivity? This cycle's null-calibration appendix
(§2a) rules out *pure noise*, but a *systematic*, `nx`-dependent numerical
artifact in the measurement pipeline itself (not random noise, and not a
real coherent echo either) is a third possibility neither this cycle's
noise-null nor its echo-mechanism tests were built to distinguish from a
genuine field effect.

---

## Ranked top-3 candidate directions for Iteration 55

1. **Correct the "~24×" framing before it propagates further.** One
   sentence in `LOGBOOK.md`'s T16 entry and any cross-referencing PLAN.md
   text: replace the `amp_ratio/C_thr` figure with the unit-consistent
   `sqrt(A_i²+A_q²)/C_thr` figure (≈0.12×/0.08×, sub-threshold) wherever
   `PAD_TIED`'s magnitude is cited for urgency-ranking purposes, and note
   why (§2b, this document). Zero cost, prevents a category error from
   being cited a further round as this program's own record already shows
   it has been (Phase 2 → Phase 5 → Red Team audit → LOGBOOK → this
   cycle's own brief).
2. **The Yee-grid-dispersion-corrected echo re-score (§4b).** Zero new
   FDTD — recompute `boundary_reflectance.py`'s round-trip phase using the
   engine's own closed-form numerical dispersion relation at
   `cells_per_lambda=20`, `courant_frac=0.99`, per angle, instead of
   vacuum `c`, and re-run this cycle's own Test A/B. Directly answers
   whether the coherent-echo mechanism class was killed by physics or by
   a dispersion-relation mismatch in the model — the one distinction this
   cycle's REFUTE does not yet make.
3. **Execute Iteration 53's own still-queued Tier-2 item 7**: load a real
   absorbing article at `G40`'s geometry and test whether the `PAD`-
   sensitivity survives the object-minus-flank subtraction real
   constraint-3 scoring performs, or cancels as shared background — the
   only test that actually engages my charter's domain (§3, Layer 1) and
   has now been deferred through two full cycles (076, 077) in favor of
   mechanism-hunting on a signal whose own perceptual-adjacent scale (§2b)
   turns out to have been overstated by roughly two orders of magnitude.
