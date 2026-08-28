# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 62 · exp-085

*Fresh context. Received: `phase1_proposal.md` → all five Phase-2 blind
critiques → `phase2_redteam_audit.md` → `phase3_synthesis.md` →
`phase4_derivation.py` → `derivation_results.json` → `NOTES.md` → all six
Phase-5 blind reviews (PHOTONICS, MATERIALS, EM, THERMODYNAMICS, QUANTUM,
VISION). Read PANEL.md and LOGBOOK.md in full (RULED OUT R1–R10, ESTABLISHED,
LIVE THREADS, the complete T28 arc Iterations 46–61, both Checkpoint 52/54
entries and the Iteration-61 Checkpoint in full). Every load-bearing claim
below — the six reviews' own, and this audit's own — is independently
re-derived from primitives (source code, `derivation_results.json`, and a
fresh grep/read of every prior T28 experiment's own committed JSON), not
adjudicated by tallying seats.*

## 0. Scope note

Model-internal, zero-FDTD desk cycle re-evaluating an already-validated,
already-gated closed form (`edge_diffraction_c_empty_corrected`) over a
wider/denser domain with already-committed period-search machinery. No
absorption mechanism is proposed and no constraint-3 scene is touched
anywhere in the record — confirmed directly, matching every T28 desk cycle
since exp-069. **Checkpoint criterion 2 (mechanism-class boundary) is N/A**
— see §5 for the reasoning applied explicitly, not by pattern-match, per
this cycle's own instruction.

## 1. Independent primitive-level re-derivation performed

All commands and figures below were re-run/recomputed by this audit, not
accepted from any seat's prose. Full detail; conclusions in §2–§4.

### 1.1 Baseline reproduction

`derivation_results.json` re-read directly: `classification_a="STRONG
COHERENT CHIRP"`, `classification_b="METHOD DISAGREEMENT"`, `P_wide=
3.2556390977443606°` (`R²_wide=0.012802`, circular-shift `45.44%` of
3900 shifts meet/exceed), `P_fft=8.754371395917975°` (`P_fft_full=
140.0699423346876°`, `P2/P1=0.799`), `frac_recovered=1.0`,
`spread=9.258667605452366`, `ρ=0.8816974869606448` (`p=5.757×10⁻¹³`),
`null_sample_pass_rate=0.4` (`4/10`). All match every seat's citation and
NOTES.md exactly.

### 1.2 The `center_deg=39.0` reference-angle fix (Fix 3) — confirmed correct

Traced `phase4_derivation.py` lines 336–338 directly:
`p_local_corrected = p_star·cos(39°)/cos(θc)` is the exact algebraic
un-do/re-do of `_free_period_search`'s own fixed-`center_deg` convention.
Applied at all 37 sub-window call sites, none skipped. Methods A/B correctly
retain `center_deg=39°`, consistent with every existing `P_model_a`/
`P_edge_A` citation. **Confirmed correctly and completely implemented**,
matching EM's, QUANTUM's, and THERMODYNAMICS' own independent traces.

### 1.3 The boundary-pinning defect (PHOTONICS + MATERIALS) — CONFIRMED exactly, and quantified further

Re-derived `y_wall_prescreen.py::free_period_with_widening`'s own
`chosen`-selection loop directly from source (lines 344–361):

```python
chosen = None
for st in stages:                    # narrow[1,4] -> wide[1,15] -> widest[1,60]
    ...
    if chosen is None or (chosen["at_boundary"] and not at_boundary):
        chosen = rec
    if not at_boundary:
        break
```

Algebraic trace: if every stage is `at_boundary` (no interior optimum found
anywhere in `[1°,60°]`), `chosen` is set once, at the **first** (narrowest)
stage, and never updated again — the loop silently returns the
least-widened, least-informative reading, indistinguishable in the output
from a genuine convergence. `phase4_derivation.py`'s Method C loop builds
the full 3-stage trace (`stages_sub`, carrying `at_boundary` per stage) but
never writes it to `out["method_c"]` — the evidence needed to detect this
from the committed JSON alone does not exist; detecting it requires
re-running the search, which this audit did.

**Directly re-derived from the committed `sub_results` array** (37 rows):
exactly **6 of 37** report `p_local_reported_at_39 == 4.0000000` (the
narrow-stage upper boundary, `4.0×0.995=3.98` threshold cleared) —
`θc = 45°, 59°, 61°, 63°, 71°, 73°` — matching PHOTONICS'/MATERIALS'
claim exactly, digit for digit. Re-running the raw 3-stage search for these
(and the 4 additional points MATERIALS null-sampled at θc=59/61/63/71/73)
confirms all three stages are boundary-pinned at every one, e.g. θc=61°:
`narrow→P*=4.00 (boundary)`, `wide→P*=15.00 (boundary)`,
`widest→P*=60.00, R²=0.987 (still boundary)` — the search wants a period
beyond 60°, not the 4.00° it silently reports.

**A further, independently-derived confirmation**, going one step past both
Phase-5 reviews: filtering the 37 `p_local_corrected` values for
`>6°` (the sub-window's own physical width — a fitted period that long
never completes one full cycle inside the 31-point window used to measure
it, an unresolvable fit almost by construction) gives **exactly 15 of 37**,
concentrated at `θc≥47°` — reproducing PHOTONICS' "15/37 total in this
broader category" precisely.

### 1.4 What the defect actually does to the headline statistics — recomputed, not merely asserted

Re-scored `frac_recovered`/`spread`/`ρ` on the 37-row array under two
exclusion rules:

| Exclusion | n remaining | frac_recovered (of 37) | spread | ρ | p |
|---|---|---|---|---|---|
| none (as filed) | 37 | 1.000 | 9.259 | 0.882 | 5.8×10⁻¹³ |
| exclude the 6 exact-boundary pins | 31 | 1.000 | 9.931 | 0.838 | 4.2×10⁻⁹ |
| exclude the 15 `>6°`-width category | 22 | **0.595** | 1.097 | 0.616 | 2.3×10⁻³ |

**This is the single most consequential number in this audit.** Excluding
just the 6 literal silent-fallback cases barely moves `spread`/`ρ` (they
stay dominated by the *other* 9 boundary-adjacent, period-exceeds-window
cases in the same `θc≥47°` region). Excluding the full, defensible 15-window
"unresolvable" category — which PHOTONICS names but does not itself score
against the classification gate — **drops `frac_recovered` to 0.595,
which fails the shared `≥0.80` gate every one of STABLE, DRIFTING, and
STRONG COHERENT CHIRP requires.** Under a corrected accounting, **none of
the three positive classifications in Fix 5's own decision table is
reachable** — the honest result routes to NOT STABLY PERIODIC (or,
more precisely, "too few reliable local windows remain to call a
global classification at this window scale at all"). This independently
confirms PHOTONICS'/MATERIALS' own prediction — "a re-classification
excluding these sub-windows would likely NOT clear any of STABLE/
STRONG-CHIRP/DRIFTING's `frac_recovered≥0.80` gate" — exactly, by direct
recomputation, not by re-stating their claim.

### 1.5 The prior-cycle-impact question — did this defect silently corrupt any earlier committed number?

`free_period_with_widening`'s identical `chosen`-selection logic (bit-for-
bit the same `if chosen is None or (chosen["at_boundary"] and not
at_boundary)` pattern) exists in **two** files —
`experiments/077-.../pad_round_trip_model.py` (its origin) and
`experiments/078-.../y_wall_prescreen.py` (which the record itself says
"reproduced verbatim" from the first) — and has been reused, unmodified,
across every T28 cycle since (`grep` confirms `free_period_with_widening`/
`_free_period_search` imported or reused in experiments 069–085, at least
15 files). I grepped every committed `derivation_results.json`/
`results.json`/`*_results.json` in experiments 077–084 for stored
`{window, at_boundary}` pairs (available wherever the stage trace was
persisted) and independently re-derived `at_boundary` for the two headline
numbers this cycle itself reuses:

- **`P_edge_A=2.8421052631578947°`** (exp-078's `real_periods.c80_c40`,
  cited by every T28 cycle since, including this one) — `at_boundary:
  False`. Genuine interior optimum.
- **`P_model_a=2.533834586466165°`** and **leg (b)'s `2.1353383458646613°`**
  (exp-084's own `derivation_results.json::leg_a`/`leg_b`) — both
  `at_boundary: False`. Genuine interior optima.

**No currently-active, currently-cited T28 headline number was produced by
a boundary-pinned fallback call.** The defect DID fire, historically, twice
that this audit's own (non-exhaustive — see §6, mandatory-fix item 7) scan
of committed JSON found:

1. **exp-079** (`y_wall_aperture_sum_results.json::
   reflectance_ablation_control.pair_absorb40`): all three stages
   boundary-pinned at `p_star=1.0` (the lower boundary), `R²=0.0`. This is
   a deliberately-ablated (mechanism-nulled) control curve — `R²=0.0`
   already flags it as carrying no periodic structure by the code's own
   `ss_tot_degenerate`-adjacent logic, regardless of which boundary value
   the search happened to land on. **Harmless**: the number was never read
   as a real period by anything downstream.
2. **exp-078** (`y_wall_prescreen_results.json::
   primary_model_pair_deltas.c80_c40`): all three stages boundary-pinned
   at `p_star=4.0`, `R²=0.247`. This one WAS scored — against
   `P_edge_A=2.8421°`, `rel_dev=0.4074`. But exp-078's own code explicitly
   computed and printed `at_boundary_flags` for exactly this quantity
   ("at-search-boundary at EVERY widened stage (no interior optimum found
   anywhere up to 60°)"), and `rel_dev=0.4074` lands in the pre-registered
   INCONCLUSIVE band (`0.30<rel_dev≤1.00`) regardless of what the "true"
   (unresolved, beyond-60°) period would have been. **The qualitative
   verdict this number fed into was correct despite the artifact, and the
   artifact was self-disclosed at the time via the `at_boundary` field —
   unlike this cycle, where the equivalent field is computed and then
   discarded before it reaches `derivation_results.json` (§1.3).**

This is the decisive fact for §5's Checkpoint-4 ruling: the defect is real,
structural, and has fired before — but every prior firing was either inert
by construction or self-disclosed and non-outcome-determining, and every
currently load-bearing T28 citation is clean.

### 1.6 EM's "28× vs. 4.4×" discriminant — CONFIRMED as computed, but built on the same contaminated data PHOTONICS/MATERIALS flag

Reproduced EM's arithmetic exactly: `34.9559/1.2318=28.38×` observed local-
period growth (`θc=5°→77°`) vs. `cos(5°)/cos(77°)=4.43×` predicted by the
already-refuted `1/cosθ` grating law over the same endpoints. **But**
`θc=77°` (`P_local=34.96°`) and every other point above `θc≥47°` sit inside
§1.4's own 15-window "unresolvable" category. Recomputing EM's own
discriminant restricted to the *clean* sub-windows only (`θc=5°…57°`,
excluding the 15 flagged windows, which happens to exclude `47°–55°` from
the *interior* of this otherwise-contiguous range):

- Observed growth, clean set: `4.3962°/1.2186°=3.61×` (θc=45° vs. θc=7°).
- `1/cosθ`-predicted growth over the same θc extremes: `cos(5°)/cos(57°)=
  1.83×`.

**EM's own headline number (28× vs. 4.4×, "over 6× steeper") is
overwhelmingly a property of the same artifact-contaminated tail
PHOTONICS/MATERIALS independently flag — it is not the independent second
line of evidence for genuine near-field chirp EM's review presents it as.**
A real, much more modest residual does survive inside the clean region
(`3.61×` observed vs. `1.83×` predicted — roughly 2× steeper, not 6×) —
directionally consistent with EM's qualitative claim (something beyond a
pure obliquity projection), but the magnitude EM reports, and the specific
"DRIFTING, not full STRONG COHERENT CHIRP" downgrade EM proposes on the
strength of it, is not independently supported once the shared defect is
accounted for.

### 1.7 EM's `P_fft_full=140.07°` Fourier-resolution-floor argument — CONFIRMED independently, holds up

Recomputed the true (non-padded) frequency resolution:
`Δf=1/(u_hi−u_lo)=1.0527` cycles/unit-sinθ → `P=70.03°`. `P_fft_full=
140.0699°` is **exactly 2.0000×** that floor — bin index 2 of the padded
grid, inside the sinc-interpolation zone below the data's own true
resolution. Independently confirms EM: Method B's global result (both the
in-range `P_fft=8.75°` and the unrestricted `P_fft_full=140.07°`) is
uninformative by construction on a domain this size — neither corroborates
nor refutes a chirp hypothesis; it is simply below the instrument's own
floor. This part of EM's review is sound and adds real value independent of
the growth-discriminant issue in §1.6.

### 1.8 QUANTUM's Spearman-independence claim — CONFIRMED as valid methodology; the residual trend, on the *uncorrected* (artifact-laden) data, is still formally significant

37 sub-windows, 6°-wide, 2° step ⇒ 66.7% pairwise overlap; effective
independent count over the 72°-wide domain ≈ `72/6=12`. Recomputed
`spearmanr` on a non-overlapping stride-3 subsample (n=13, θc=5°,11°,…,77°,
i.e. **not** the clean-only set — this still includes the artifact tail):
`ρ=0.934, p=3.0×10⁻⁶`. **QUANTUM's point that `p=5.8×10⁻¹³` overstates
independence-adjusted significance is confirmed** — but a properly
independence-corrected test on the full (uncorrected) data still clears
significance by a wide margin, so this defect alone does not, on its own,
overturn the trend's existence; it only means the specific p-value cited is
not a valid measure of how surprising it is. Combined with §1.4/§1.6,
however, the *magnitude* of that surviving trend is itself substantially an
artifact of the same 15 unresolvable windows — QUANTUM's critique and
PHOTONICS'/MATERIALS' critique are compounding, not competing, findings.

### 1.9 QUANTUM's binomial test on the 4-of-10 null split — CONFIRMED exactly

`binomtest(4, 10, p=0.5)`: **p=0.7539** (two-sided), matching QUANTUM's
`p=0.754` to the printed digit. NOTES.md's "genuinely bimodal, not
uniformly contaminated" reading is **not** statistically supported by n=10
— confirmed independently, exact reproduction.

**A further synthesis this audit adds, combining VISION's clustering
observation with the raw null data**: of the 10 sampled sub-windows, the
4 HIGH/unreliable ones (θc=5°,21°,37°,45°) all sit in the "near-normal
quarter" (θc≤45°) — the very region PHOTONICS'/MATERIALS' own §1.4/§1.6
findings treat as the more trustworthy fallback reading. Recomputed
directly: **4 of the 6 near-normal-quarter sub-windows actually sampled for
the null (θc=5°,13°,21°,29°,37°,45°) are HIGH/unreliable** — only θc=13°
(6.7%) and θc=29° (3.3%) read clean. **The "safe" near-normal-quarter
fallback reading PHOTONICS proposes as this cycle's honest residual finding
is itself majority null-contaminated on the only direct evidence
available.** This is not a criticism of PHOTONICS' review — it is a
genuinely new synthesis only visible by combining two different seats'
independent findings, exactly the adjudication work this seat exists to do.

### 1.10 VISION's mislabeled-print finding — CONFIRMED exactly

`phase4_derivation.py` line 405 computes `rd_wide_fft = rel_dev(P_wide,
P_fft) = |a−b|/b = |3.2556−8.7544|/8.7544 = 0.62811...`, printed under the
label `"vs mean"` — but the mean-relative figure is
`|diff|/mean = 5.4988/6.0050 = 0.91569...`. Recomputed both independently:
**62.81% and 91.57%, both confirmed to the printed digit.** The actual
gating boolean (`disagreement = |P_wide−P_fft|/mean_wf > 0.10`, lines
406–407) correctly uses the mean-based formula — `classification_b`
(METHOD DISAGREEMENT) is unaffected either way. **Cosmetic, non-load-
bearing, confirmed exactly as VISION and THERMODYNAMICS both independently
found.**

### 1.11 THERMODYNAMICS' timing re-verification

Re-executed the identical 37-sub-window-fit + 10-null-sample loop
independently: **29.7s**, matching THERMODYNAMICS' own 29.66s re-run and
NOTES.md's "29.8s" — confirmed genuine, real, and (per THERMODYNAMICS'
own flag) not itself persisted to JSON, a minor forward-hygiene gap.

## 2. Reconciling the four partially-overlapping, partially-conflicting readings

**PHOTONICS + MATERIALS ("the chirp finding is mostly artifact, likely
doesn't survive"):** **CONFIRMED as the dominant, load-bearing reading.**
§1.4 shows a corrected `frac_recovered=0.595` fails every named
classification's shared gate — under a defensible correction, **no
positive classification (STABLE/DRIFTING/STRONG-CHIRP) is reachable at
all**, exactly as both seats predicted, now demonstrated by direct
recomputation rather than argued qualitatively.

**EM ("downgrade to DRIFTING, supported by a new discriminant"):**
**PARTIALLY CONFIRMED, but overstated, and its own new evidence is not
independent of the defect PHOTONICS/MATERIALS found.** §1.7 (the
Fourier-floor argument) is sound and stands on its own. §1.6 (the growth-
discriminant) is confirmed arithmetically but shown, by this audit's own
restriction to the clean sub-window set, to be built substantially on the
same contaminated tail — the true residual excess-over-`1/cosθ` inside the
trustworthy region is ~2×, not ~6×. EM's proposed "DRIFTING" downgrade is a
reasonable compromise position argued in good faith, but it does not, on
independent inspection, clear the bar EM itself sets for it (a discriminant
"independent" of the artifact) — and §1.9's finding (the near-normal
quarter is itself majority null-contaminated) undercuts even EM's own
robustness table (§2.4(a) of EM's review), which treats dropping only the
two literal endpoints as sufficient.

**QUANTUM + VISION ("the significance math itself is invalid regardless"):**
**CONFIRMED, independently, on both counts** (§1.8, §1.9) — but this class
of finding, on its own, does not resolve whether the underlying trend is
real (§1.8's own corrected test still clears formal significance on
uncorrected data). It is compounding evidence for skepticism, not a
standalone refutation.

**This audit's own combined verdict on classification (a):** the filed
**"STRONG COHERENT CHIRP" does not survive** — not merely "contested by its
own reliability check" (NOTES.md's own framing) but **actively overturned**
by a corrected `frac_recovered` accounting (§1.4). PHOTONICS' own proposed
fallback ("genuine modest periodicity confined to the near-normal quarter")
is the most defensible *positive* alternative on the table, but it is
itself **not currently certified** either (§1.9) — the sparse null evidence
available in that region is majority-unreliable, not majority-clean. The
honest combined reading, reconciling all four findings rather than picking
a winner: **classification (a) should be reported as NOT STABLY PERIODIC at
this instrument's current level of reliability** — with an explicit,
disclosed caveat that this is a statement about what this cycle's own
(defective, under-null-tested) instrument can currently certify, not a
claim that no local periodic structure exists in the near-normal region;
that question remains genuinely open, gated behind the mandatory-fix docket
in §6.

Classification (b) (METHOD DISAGREEMENT) is untouched by any of the above —
independently reproduced bit-exact (§1.1) and not contested by any seat.

## 3. Checkpoint criterion 4 — does the boundary-pinning defect fire it?

**Ruling: does NOT fire, on the specific facts this audit independently
re-derived — but only because it is being caught and corrected in this
very document, before LOGBOOK commits anything.** Reasoning, applying this
program's own established distinguishing test (re-derived from the
Iteration 49/50/52/54/61 firing precedents vs. the Iteration 51/53/55/58/
59/60 non-firing precedents, not merely labeled):

This program's own pattern, read across all 13 prior firings and 6 prior
non-firings, is not "Phase 2 vs. Phase 5" — it is whether a defect **enters
a defended, committed, permanent record uncaught by that cycle's own review
layers**, later requiring a *subsequent* cycle or Phase-5 seat to reverse a
citation already resting on it (the firing pattern — Iterations 49, 50, 52,
54, 61), versus being **caught and corrected within the same cycle's own
review process, before the Director writes the LOGBOOK entry** (the
non-firing pattern — Iterations 51, 53, 55, 58, 59, 60, each explicitly
reasoned this way in its own entry).

Applying that test here:

1. **The defect was not caught by five blind Phase-2 critiques or Red
   Team's own Phase-2 audit**, despite all of them scrutinizing the exact
   same function (`free_period_with_widening`) at primitive-source level in
   fine detail (EM's own `center_deg=39.0` catch, in the same file, one
   function up). This is a real miss, worth naming plainly.
2. **It was caught, independently, by two blind Phase-5 seats
   (PHOTONICS, MATERIALS), before any LOGBOOK entry existed.** NOTES.md's
   own "STRONG COHERENT CHIRP" is not yet a committed, cited, defended
   permanent-record claim — it is Phase-4 output awaiting exactly this
   Phase-5 layer's adjudication, which is what Phase 5 exists to do
   (PANEL.md's own design).
3. **No currently-active, currently-cited T28 number is shown corrupted**
   (§1.5) — `P_edge_A` and `P_model_a`, the two headline figures every
   future T28 citation inherits, are both confirmed genuine interior
   optima, unaffected.
4. **The two historical instances where the defect DID fire were both
   inert** (§1.5) — one self-evidently degenerate (`R²=0.0`), one
   self-disclosed at the time via an explicitly printed `at_boundary` flag
   and landing on the correct qualitative verdict regardless.
5. **This audit is the layer that completes the catch-before-commit
   pattern.** Provided the LOGBOOK entry for this iteration states the
   corrected reading (§2) — NOT STABLY PERIODIC, not STRONG COHERENT
   CHIRP, un-downgraded — rather than the as-filed classification, the
   defect does not survive into the permanent record uncaught. That is the
   operative condition this program's own precedent (Iterations 51/53/55/
   58/59/60) treats as clean.

**This is a close call, correctly weighed, not a reflexive non-firing.**
The distinguishing fact from every firing precedent is squarely
"first-time, blind-caught, same-cycle, before LOGBOOK" — matching the
non-firing shape exactly, not merely resembling it. It is *not* excused by
"the record disclosed a related gap" (NOTES.md's own Fix-2/Fix-5 collision
disclosure, which is a *different*, narrower defect than the boundary-
pinning one — the two should not be conflated, and this audit does not
credit one for excusing the other).

**Forward consequence, not a firing, but binding going forward**: because
this defect lives in shared machinery reused across at least 15 T28
experiments since exp-077, and has now fired at least twice historically
and once (with real headline consequence) this cycle, it is **named,
explicitly, from this point forward**. A future cycle that reuses
`free_period_with_widening`/`_free_period_search` without applying the
mandatory-fix docket's item 1 (§6) fix, and ships a classification that
turns out to depend on a silently-boundary-pinned "chosen" value, would
**no longer be a first-time discovery** — it would fire Checkpoint
criterion 4 on the same standard as R6/R7/R8/R9/R10's own "known, named,
ignored" escalation shape.

## 4. Checkpoint criterion 2 — does the defect's institutional reach change anything?

**Ruling: remains N/A, unchanged.** Criterion 2 governs proven mechanism-
class boundaries for the phenomenon program's own constraints (PANEL.md
§"Checkpoints," item 2) — a *phenomenon* question, not an *instrument*
question. This cycle, like every T28 desk cycle since exp-069, makes no
mechanism-class claim bearing on any of the four phenomenon constraints;
nothing here touches constraint 1/2/3/4 or T1's escape-route taxonomy. The
boundary-pinning defect's institutional reach (shared machinery, ~15
experiments) is real and consequential — for the T28 sub-thread's own
internal record-keeping and for Checkpoint criterion 4's forward posture
(§3) — but it is a program-integrity/instrument-quality finding, not a
mechanism-class-boundary finding, and criterion 2's own text does not
stretch to cover it. Widening criterion 2 to absorb instrument-quality
findings would blur it into criterion 4's own territory and is not
warranted by anything in this cycle's record.

## 5. LOGBOOK-ready verdict

**Combined Verdict: PARTIAL.** Unanimous across all six blind Phase-5 seats
and this final audit — but this audit's own corrected reading of
classification (a) is materially more specific, and in the local-structure
question more skeptical, than NOTES.md's own filed headline:

- **Global scale (Methods A, B): CONFIRMED, robustly, independently
  reconfirmed at least five separate ways (this audit, EM's own
  from-stored-data reconstruction, THERMODYNAMICS, PHOTONICS,
  MATERIALS) — no single stationary period exists over the wide/dense
  domain.** `R²_wide=0.013` sits at the null's own 45th percentile;
  `P_fft`'s in-range peak is not sharp (`P2/P1=0.80`); the FFT's true
  global maximum (`P_fft_full=140.07°`) sits exactly at 2× the domain's
  own Fourier resolution floor — a genuinely uninformative reading, not
  contested evidence either way. This is the cycle's one clean, fully
  earned finding.
- **Local scale (Method C): the filed "STRONG COHERENT CHIRP" does NOT
  survive.** A previously-undisclosed defect in shared, multiply-reused
  search machinery (`free_period_with_widening`, in service since exp-077,
  ~15 T28 experiments) silently returns a non-convergent search's own
  worst (narrowest-stage) candidate as if resolved, affecting 15 of 37
  (41%) of Method C's sub-windows, concentrated at grazing incidence.
  Correcting for this drops `frac_recovered` to `0.595`, failing the
  `≥0.80` gate shared by every named positive classification — under a
  defensible accounting, **no STABLE/DRIFTING/STRONG-CHIRP classification
  is reachable.** The Spearman significance figure (`p=5.8×10⁻¹³`) is
  independently confirmed invalid as computed (37 heavily-overlapping,
  non-independent sub-windows; effective count ≈12) and NOTES.md's own
  "genuinely bimodal" null-contamination reading is independently
  confirmed unsupported (binomial `p=0.754` against uniform 50%
  contamination). **Even the most defensible positive fallback — genuine,
  modest periodicity confined to the near-normal quarter — is not
  currently certified**: the sparse null evidence actually available
  there (4 of 6 sampled sub-windows) is itself majority null-contaminated,
  a finding only visible by combining two different seats' own results,
  which neither seat states on its own.
- **Net**: this cycle's own stated goal (pin `P_model_a`'s asymptotic
  value with certainty) is not met, and — more specifically than any
  individual seat's own verdict — **no defensible period-existence claim
  of any kind currently survives at any resolved scale of this
  instrument**, global or local. This does not rule out genuine near-field
  structure (nothing here forecloses it; the honest state is "not yet
  measurable with a corrected, fully null-tested instrument," not
  "absent") and does not promote it either.
- **Checkpoint criterion 2: N/A**, matching every T28 desk-cycle
  precedent since exp-069 — reasoned explicitly (§4), not by pattern-match.
- **Checkpoint criterion 4: does NOT fire** — a close call, correctly
  weighed against every firing precedent's own distinguishing test, and
  resolved by this audit's own act of catching and correcting the defect
  before LOGBOOK commits the as-filed headline (§3). Named forward,
  binding on any future reuse of the affected machinery.

## 6. Mandatory-fix docket for close-out

1. **Fix `free_period_with_widening`'s all-stages-boundary case**, in both
   files that carry the identical logic (`experiments/077-.../
   pad_round_trip_model.py` and `experiments/078-.../y_wall_prescreen.py`,
   the latter reused by every T28 cycle since including this one). When
   every stage is boundary-pinned, return the **widest** stage's own value
   with an explicit `converged=False`/`no_interior_optimum=True` flag —
   never the narrowest stage's silently. Surface this flag through every
   caller (including `phase4_derivation.py`'s Method C loop, which
   currently computes and discards it).
2. **Re-score Method C's classification (a)** on the corrected machinery
   (reusing this cycle's own already-evaluated curve data — no new
   evaluations needed) and report the result under the label this audit's
   §5 verdict specifies, not "STRONG COHERENT CHIRP," in `NOTES.md` and any
   LOGBOOK entry.
3. **Extend the circular-shift null to all 37 Method C sub-windows** (not
   just 10) — unanimous across all six Phase-5 seats, confirmed cheap
   (~30s total, independently re-timed by this audit and THERMODYNAMICS at
   29.7s/29.66s).
4. **Correct the Spearman significance calculation for window overlap**
   before any `ρ`/p-value is cited as evidence in a permanent record again
   — either restrict to a non-overlapping subsample (≈12–13 windows, this
   audit's own §1.8 reconstruction available as a starting point) or apply
   an explicit block/effective-N correction.
5. **Fix the mislabeled `rd_wide_fft` print statement** (`phase4_derivation.py`
   line ~418) and correct NOTES.md's "62.8%... of their mean" citation to
   the true mean-relative figure (91.6%) — cosmetic, non-blocking, but
   should not stand now that it is found (§1.10).
6. **Persist per-stage/per-null elapsed times as JSON fields**, not
   `print()`-only, per THERMODYNAMICS' own forward-hygiene finding — closes
   a real, if minor, R4-verifiability gap before a more expensive timing
   claim is cited somewhere it cannot be cheaply re-run.
7. **A bounded, not-yet-exhaustive prior-cycle audit** (this audit's own
   §1.5 scan covered every committed JSON in experiments 077–084 that
   persists `{window, at_boundary}` pairs, and found exactly two historical
   firings, both inert) — a fully rigorous version would dynamically
   re-run every historical `free_period_with_widening` call across the
   full T28 board and check every stage, not merely grep stored JSON for
   already-persisted flags (some historical calls may not have persisted
   the per-stage trace at all). Not required to close this cycle out — the
   two confirmed instances are both inert, and no currently-cited number is
   at risk — but worth doing once, cheaply, as institutional hygiene,
   folded into item 1's own fix batch.

## 7. Reconciled ranked top-3+ candidate directions for Iteration 63

Drawing on all six seats' own top-3 lists (PHOTONICS #1/#2, MATERIALS #1/#2,
EM #1, QUANTUM #1, VISION #1, THERMODYNAMICS #1 all independently converge
on the same underlying repair-and-rerun cluster) plus this audit's own
judgment about what the boundary-pinning discovery changes:

1. **Fix `free_period_with_widening`'s boundary-fallback defect and
   re-run/re-classify Method C** (docket items 1–2, §6) — near-unanimous
   #1 (PHOTONICS, MATERIALS explicitly; a precondition for QUANTUM's,
   VISION's, and EM's own proposed fixes to mean anything, since all three
   operate on `p_local_corrected` values the defect currently contaminates).
   Cheapest, most consequential, zero new FDTD, directly answers this
   cycle's own central open question with a corrected instrument rather
   than an argued adjustment.
2. **In the same batch: extend the circular-shift null to all 37
   sub-windows and correct the Spearman significance for window overlap**
   (docket items 3–4, §6) — QUANTUM's, VISION's, THERMODYNAMICS', EM's
   shared #1/#2. Running items 1 and 2 together, rather than sequentially,
   avoids adjudicating a partially-corrected instrument twice.
3. **A cheap, bounded audit of whether this defect silently affected any
   OTHER prior T28 citation beyond the two found here** (docket item 7,
   §6) — this audit's own addition, not named by any individual Phase-5
   seat, motivated directly by the shared-machinery discovery and matching
   this program's own R4/R9 precedent of checking a newly-found defect
   class against history before moving on.
4. **The joint EM/THERMO energy-interception cross-check, in full, on the
   next scene-bearing T28 cycle** — now the standing item across three
   consecutive cycles (083 discretionary-partial, 084/085 structurally
   exempt), THERMODYNAMICS' and MATERIALS' own #3. Iteration 63 should
   either select a cycle with a real article-loaded scene so this finally
   runs, or state the exemption explicitly a third time, matching this
   sub-thread's own established discipline.
5. **PHOTONICS' domain-truncation test for leg (b)'s Anchor 2, and/or EM's
   matrix-valued RS/Kirchhoff kernel rebuild** — standing Tier-1 items from
   Iteration 61/62's own board, untouched by this cycle, EM's own #3.
6. **Standing Tier-2/3 items, carried forward unchanged**: the x-wall
   wavelength-generality leg (now ten consecutive cycles deferred,
   076–085 — should not be deferred an eleventh time without an explicit
   reason), the near-null σ(I) article follow-up, QUANTUM's lossless-PEC-
   only-disk control, and the ritualization governance question named at
   Iteration 61 (still not resolved, not urgent).
