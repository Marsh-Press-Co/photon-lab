# Phase 5 Review — VISION SCIENCE (Panel Iteration 91, exp-114)

**Fresh sub-agent, blind to every other seat's current Phase-5 review.**
Read `LOGBOOK.md` end to end (RULED OUT registry R1–R32 in full; LIVE
THREADS T1–T28 in full, including the acknowledged Iteration-58-through-87
narrative gap the file itself discloses); `PANEL.md` in full; `PLAN.md`'s
current-state entry (this file logs most-recent-first, so the "tail" the
task asked for is the entry at its head, covering the Reconciled
Iteration-91 queue verbatim); and this cycle's own complete record —
`phase1_proposal.md`, `run114.py`, `chunk_runner114.py`, `analyze114.py`,
all five Phase-2 critiques (including my own, `phase2_critique_vision.md`),
`phase2_redteam_audit.md`, `NOTES.md`, `results.json` — plus
`experiments/113-.../NOTES.md` for grounding (my own seat's immediately
preceding lead cycle, where R32 was minted).

## Charter-fit, reconfirmed independently

My charter (contrast thresholds, luminance edge detection, spectral
sensitivity, adaptation, temporal sensitivity, attentional blindness; pin
numeric thresholds before any run scores against them) does not bind on
this cycle's own substance — reconfirmed directly, not on the record's own
say-so: `run114.py`/`chunk_runner114.py`/`analyze114.py` contain zero
Weber-contrast, `C_thr(L)`, photopic/scotopic, or Check-A/B/C content; the
only Weber/perceptual language anywhere is inside `DISCLAIMER`'s own
negations. My task here is the adversarial code/math read this cycle's own
briefing correctly says my seat brought to Phase 2, not perceptual-
threshold pinning.

## 1. Does NOTES.md's "Combined Verdict" honestly match `results.json`?

Read both myself, side by side, rather than assuming the framing tracks the
data.

- `results.json`'s `kappa_exponent_result` gives `rel_dev=0.12274985147707763`,
  `confirm_band=0.15`, `verdict="CONFIRM (kappa_exponent generalizes across
  kappa_ratio)"`. NOTES.md's Combined Verdict states "the session-normalized
  `rel_dev=0.1227` clears the CONFIRM band (≤0.15) with room to spare" —
  matches, correctly rounded, not overstated (0.1227 is 18% of the way from
  0 to the 0.15 ceiling, genuinely "with room to spare," not a hair's-breadth
  clear).
- The naive/uncorrected figure NOTES.md cites (`rel_dev=1.8619`,
  verdict REFUTE) matches `results.json`'s own
  `kappa_exponent_result_naive_uncorrected_DO_NOT_SCORE` block exactly
  (`1.8618852001295216`, rounds to 1.8619). NOTES.md is explicit that this
  block is disclosed, not deleted, and is not scored — matching
  `analyze114.py`'s own key name and `build_result_text()`'s own prose,
  which I re-read in `run114.py` line by line: the naive value is *never*
  read by `classify_kappa_exponent_check` or fed into the frozen verdict
  string anywhere in the committed pipeline.
- Cost-gate figures (`raw.projected_234_total_s=2705.2516053872732`,
  `scaled.projected_234_total_s=6895.676291472242`, both `proceed_to_r234=
  true`) match NOTES.md's own "6895.7s... 36.2% margin" and "2705.3s...
  75.0% margin" language exactly (`1 - 6895.676.../10800 = 0.3614...`,
  rounds to 36.1–36.2%, matches).
- `total_wall_s_all_scenes=7038.29048371315` matches NOTES.md's "7038.3s
  (117.3 min)" (`7038.29/60=117.305`, matches).
- The energy ledger figures (`sigma_scat`/`sigma_abs`/`sigma_ext` for both
  peccored and hollow) are real, non-zero, and match NOTES.md's own quoted
  numbers to the printed decimal.
- `geom_identity.pass_=true`, `mismatches=[]` — matches "Geometry identity:
  PASS."

**No discrepancy found between NOTES.md's own framing and what
`results.json` actually contains.** The "Combined Verdict" section does not
oversell: it correctly separates the Tier-1 falsifiable-question CONFIRM
from the Tier-0 process finding (the R9 catch), states the naive/corrected
split honestly, and does not claim anything `results.json` doesn't support.
This is the same standard my own Phase-2 critique applied to the
pre-registered bands (verify the citation, not just trust it) — applied
here to the frozen record instead.

## 2. Independent from-scratch recomputation of the R9 fix's arithmetic

Recomputed myself, in a fresh Python process, from the two committed
constants named in the task — not by re-reading `analyze114.py`'s own
printed output:

```
t156_hist        = 670.4777698516846
speed_ratio      = 0.3923112818872906
t156_session_adj = 670.4777698516846 / 0.3923112818872906
                 = 1709.0453443658805

t234             = 7038.29048371315
kappa_ratio      = 1.5
exponent_234     = ln(7038.29048371315 / 1709.0453443658805) / ln(1.5)
                 = 3.490880835092507

KAPPA_COST_EXPONENT = 3.2053299988171697
measured_ratio   = 1.5 ** 3.490880835092507   = 4.11825848092089
reference_ratio  = 1.5 ** 3.2053299988171697  = 3.6680107109370383
rel_dev          = |4.11825848092089 - 3.6680107109370383| / 3.6680107109370383
                 = 0.12274985147707763
verdict: 0.1227 <= 0.15  ->  CONFIRM
```

Every digit matches `results.json`'s own `kappa_exponent_result` block
bit-for-bit, and `1.5**exponent_234` reproduces `t234/t156_session_adj`
exactly (`4.11825848092089` both ways, by construction of the log-ratio
identity) — confirming `refit_kappa_exponent`/`classify_kappa_exponent_check`
compute what they claim to, not merely that the printed numbers match each
other. I also independently recomputed the naive (uncorrected) branch from
the same two raw operands (`t234/t156_hist`, no rescaling) and got
`exponent=5.798600165690798`, `measured_ratio=10.497425567547275`,
`rel_dev=1.8618852001295216` — bit-exact to
`kappa_exponent_result_naive_uncorrected_DO_NOT_SCORE`. **Independently
confirmed: CONFIRM is the correct verdict under the session-normalized
comparison, and the naive comparison's REFUTE would have been the wrong
scientific conclusion by a wide margin (rel_dev 1.86 vs. the 0.30 REFUTE
line) — not a close call either way.**

I also spot-checked the two upstream numbers that feed this: `670.4777698516846`
is `EXP112_RESULTS["total_wall_s"]`, asserted equal to `R113.
HISTORICAL_R156_CPL25_TOTAL_S` in `run114.py` line 201 — genuinely the
exp-112 historical pilot, not a hand-typed figure; `0.3923112818872906` is
the `used_speed_ratio` from the `sustained` (not `short`) R31 control
reading in `results.json`'s own `r31_control` block, correctly the LOWER
(more conservative) of the two per `combine_control_readings`' own logic
(0.3923 sustained < 0.4221 short) — the same conservative-direction
selection my own seat's exp-113 cycle established and Fix 4 hardened.
Reusing this exact, already-measured control point (rather than a
freshly-estimated session-speed factor) is precisely right: it is the same
number the cost gate itself already spent to compute, at zero marginal
cost, and it is the number R31 exists to produce.

## 3. Is R33's framing, as stated, clear enough to mint well?

My own seat led exp-113, where R32 was proposed, and I have direct,
recent, institutional experience with what makes a new rule's text durable:
R32's own text names its precise trigger (a *freshly-recalibrated*
statistic's *direction*), states explicitly how it differs from its nearest
neighbor (R30 — threshold vs. direction), and carries an unambiguous
forward-firing clause. Judged against that bar, R33 as currently described
in this cycle's own NOTES.md/`analyze114.py` comments ("an R9-lineage rule
about session-normalization for any ratio/exponent scoring, not just
cost-gate projection") is not yet ready to mint as worded — it is a good
candidate, correctly motivated, but underspecified in four concrete ways:

1. **Scope of "any ratio/exponent scoring" is too broad as literally
   written.** The actual defect here is specific to WALL-TIME/THROUGHPUT-
   DERIVED quantities — a quantity whose value depends on this session's
   own compute speed (a timing, a cost projection, a wall-clock-based
   exponent). A physics observable measured within a single `Sim.run()`
   call (a cross-section, a field amplitude, a phase) carries no
   session-speed confound at all — that class of commensurability defect
   is already R9's own scope, not this one. As worded, "any ratio/exponent
   scoring" could be read to require a session-normalization control even
   where no throughput dependency exists (e.g. a resolution-invariance
   ratio like `tau_shell`'s own cross-r comparison, which this very cycle
   correctly asserts is bit-identical without any session correction).
   **Recommend the trigger condition read explicitly**: "a scored ratio or
   fitted exponent whose operands mix a wall-time/throughput-derived
   quantity measured THIS session with one measured or established in a
   PRIOR session" — not ratios/exponents in general.
2. **Relationship to R31 needs to be stated, not left implicit.** R31
   already requires a same-session control point before a cost-*gate*
   decision trusts a cross-session projection. What this cycle's own R9
   catch adds is that the SAME control point (the SAME `speed_ratio`,
   reused rather than re-derived) must ALSO be applied before a scientific
   classification (CONFIRM/AMBIGUOUS/REFUTE) that mixes a same-session real
   measurement against a cross-session historical one is trusted — a
   distinct decision point (post-hoc scoring, not pre-hoc spend-approval)
   using the identical machinery. R33's text should say this explicitly, or
   a future reader will read it as merely restating R31 rather than
   extending it one step further downstream, the exact kind of
   under-specification this registry's own R13/R14/R15 sibling-rule
   precedent took care to avoid.
3. **Should require REUSE of the already-measured control, not any
   session-normalization estimate.** This cycle did the right thing by
   construction — `t156_session_adjusted` reuses `control["used_speed_ratio"]`
   verbatim, the same number the cost gate already computed, not a fresh,
   separately-estimated scalar. R33's text should say this as a
   requirement, not merely describe what this cycle happened to do —
   otherwise a future cycle could satisfy a loosely-worded R33 with an
   ad hoc, unverified fudge factor and call it "session-normalized."
4. **No founding-instance/forward-firing clause is drafted yet.** Every
   ratified rule since R16 states plainly that it does not fire on its own
   founding instance (true here — this was self-caught before freeze, by
   the Director, exactly the R9 discipline working as intended) and gives
   an explicit forward trigger. NOTES.md's current text ("registered as a
   candidate standing rule (R33) at this cycle's close") does not yet
   supply that trigger. Recommend, modeled on R31's own text: "a future
   cycle that scores a same-session-measured wall-time-derived ratio or
   exponent against an un-rescaled cross-session historical wall-time
   figure, without applying the session's own already-measured (or
   freshly-measured) same-session throughput control, fires Checkpoint
   criterion 4 automatically."

None of this is a reason to withhold ratification — the underlying finding
is real, well-verified (independently reproduced above), and the fix this
cycle applied is exactly correct. It is a wording note for whichever Phase-5
seat or the Director finalizes R33's actual LOGBOOK text, from a seat that
has minted one of these before and watched vague scope language cost a
later cycle re-litigation (see R23's own First Addendum, needed because the
founding R23 text didn't say a new disclaimer string needs its own
independent asserts).

## 4. Next change for Iteration 92 — from this seat's own discipline

This cycle, like every T28 instrument cycle since Iteration 46, correctly
scores zero constraint-1/2/3/4 content — confirmed independently above and
by all five Phase-2 critiques and Red Team. But my charter's own central
question ("what would make a human eye FAIL to register something
physically present?") is the reason PANEL.md's own metrics table has a
Tier-W/Tier-A constraint-3 row at all, and it is worth stating plainly, at
Iteration 91's close, how long that row has gone unfed by real ambient-
contrast scoring while the program's bandwidth has gone entirely into T28.

**T28 itself is now a 46-iteration-deep sub-thread (Iteration 46 through
91) that opened as, and has stayed, pure instrument/model-fidelity work —
"T1 route N/A, constraint 3 not engaged" is stated, correctly, in nearly
every one of its own iteration entries, including this one.** Its own
originating channel (the ambient-contrast instrument's angular-quadrature
sensitivity, T16, opened Iteration 11) was itself constraint-3-relevant
work — until the program's own focus drifted from "is this instrument's
reading of a real constraint-3 citation trustworthy" to "what causes this
diagnostic empty-scene channel's own ~2.84° periodicity," a materially
narrower and, by this cycle's own admission, still-unidentified question,
now absorbing its 46th consecutive cycle across dozens of REFUTEd
mechanism candidates (x-wall echo, y-wall echo — both edge-reduced and
full-aperture — TAPER sub-aperture, boundary-reflectance in two admittance
families) and, for the last several cycles (108–114), not even chasing the
mechanism anymore but auditing the T28 measurement apparatus's own cost
gates and session-normalization discipline — two meta-levels removed from
the original ambient-contrast question. This work is real and rigorous —
R27/R28/R29/R30/R31/R32 and this cycle's own R33 candidate are genuine,
useful, general house-discipline findings, and I found nothing wrong with
any of them above. But **the program's own single ever-measured
constraint-3 Tier-W/Tier-A verdict (exp-032/033's OFF-state σ(I) near-null
article, `off_pass`/`off_bracket`) has not been re-scored since Iteration
12/T16**, where it downgraded from PASS to MARGINAL under a corrected N17
angular quadrature — and every ambient-contrast refinement built since
(settled `STEPS≥2800`, T27; `PAD`/`ABSORB` decorrelation, T28/exp-076; the
T21 fringe model) has stayed in EMPTY-scene diagnostic territory, never
once re-applied to the one article-loaded citation constraint 3 actually
scores against.

**Ranked candidate directions for Iteration 92:**

1. **Re-score the program's own only-ever Tier-W/Tier-A citation
   (exp-032/033's `off_pass`/`off_bracket`) through the now fully-
   modernized ambient-contrast instrument.** Nearly every needed piece
   already exists, committed, at near-zero marginal FDTD cost: settled
   `STEPS≥2800` (established generically at exp-066/068), the
   `PAD=40`-decorrelated, lossless-vacuum-proven geometry (exp-076),
   `N17`-or-denser angular quadrature (exp-034/035), and T21's own
   validated fringe/floor characterization at the real ±35°/40° geometry.
   No prior cycle has run this specific synthesis — every refinement since
   Iteration 12 was validated against the empty scene or a diagnostic
   construction, never against the loaded near-null article itself. This
   is the single highest-value use this 46-cycle T28 investment could make
   for the actual phenomenon question, and it is still undone.
2. **Execute the standing "does `PAD`-sensitivity survive with a real
   absorbing article loaded" check** — named at Iteration 53/exp-076 and
   re-deferred at every cycle since (Iterations 54 through at least 57's
   own queue; I did not verify whether it was run in the undocumented
   Iteration 58–87 span, but it is absent from every Tier list this cycle's
   own inherited queue carries forward). This is the one item that would
   tell the program directly whether T28's own decade-plus of empty-scene
   confound-hunting has ANY downstream bearing on constraint 3 at all, as
   opposed to being pure diagnostic-instrument archaeology — a
   qualitatively different kind of information than one more period-fit.
3. **Build N33** (the third angular-quadrature convergence point on the
   N9→N17→N33 sequence) — T16's own repeatedly-deferred top priority,
   queued at Iteration 13 and, so far as this record shows, never
   executed 78+ iterations later. Without it, item 1 above would still
   only be "quadrature-corrected once," not "quadrature-converged" — a
   real residual idealization in the corrected instrument this cycle would
   otherwise be leaning on.
4. **Continue the already-queued T28 Tier-1 items** (the `+168.75°`/r=312
   named-bin re-attempt with an upgraded, twice-repeated R31 control; this
   cycle's own r=234 kappa-exponent point is now delivered) — legitimate,
   well-executed instrument work, not something to abandon. But if
   Iteration 92 defers items 1–2 above yet again, the reason should be
   stated explicitly, matching this program's own now well-established
   deferral-disclosure convention (the same standard T28's own `PAD`-
   with-article item has been held to for five-plus consecutive cycles).

## Verdict on this cycle's own result

**Promising.** The falsifiable heart of this cycle resolves cleanly to
CONFIRM (rel_dev=0.1227, independently re-derived from scratch above, well
inside the 0.15 band and far from the 0.30 REFUTE line), the cost gate
approved on its first real attempt (36.2% margin, unlike the r=312 leg's
three consecutive deferrals), and a genuine, consequential operand-
commensurability defect (the R9-class conflation of `kappa_ratio` cost-
scaling with an unrelated session-speed confound) was caught and corrected
by the Director before any result was frozen — the naive comparison's wrong
REFUTE verdict never reached this permanent record. NOTES.md's own framing
matches `results.json` honestly, in every figure I independently checked.
Nothing in this cycle's own record needs correcting; R33, once worded per
§3 above, is a genuine, well-founded candidate for ratification.

## Trust suite

Attempted `python3 lab/validation/run_all.py --only 12346789` (single
combined invocation) from the repo root first; it was killed by its own
`timeout 590` wrapper with **zero** stdout produced (`ps aux` confirmed 20+
concurrent copies of this identical command, `uptime` load average 21.96 on
a `nproc=4` box) — the same shared-sandbox contention every one of this
cycle's five Phase-2 critiques and the Red Team audit independently
disclosed, reproduced here a third time, at Phase 5.

Fell back to the disclosed `--only 1` through `--only 9` (skipping 5)
methodology this cycle's own critiques and Red Team audit already
established. Ran each stage individually, this session, and independently
confirmed every reported figure against the historical values (not merely
that a `[PASS]` line appeared):

| Stage | Checks | Result | Headline figures (this run) |
|---|---|---|---|
| 1 | 3 | PASS | λ=19.97 cells, peak|Ez|=2.52, shadow ratio=0.479 |
| 2 | 3 | PASS | R=0.0983/0.0178/0.0177 |
| 3 | 4 | PASS | corr=0.928, λ=20.37, shadow agreement 0.451 vs 0.498 |
| 4 | 3 (1 shared prereq) | PASS — took two attempts (a 150s and a 585s try were both killed mid-solve by the same contention; a third attempt with a 1500s budget completed cleanly in 7s once the shared sandbox quieted) | ceviche corr=0.956, λ=19.80 |
| 6 | 5 | PASS | empty-room return 0.0001, mirror 0.924, Fresnel-1/9 0.1114, specular 0.99, round-trip OK |
| 7 | 5 | PASS | bare-wall R=0.988, coated-wall R=0.0010/−0.0002/0.0020 @600/450/750nm |
| 8 | 6 | PASS | box independence 0.020/0.001, extinction-routes-agree 0.002, abs/ext=0.571, back_frac=0.0001 |
| 9 | 13 | PASS | angle=0 bit-exact, oblique λ=23.08, empty-window balance/ripple canaries all inside band, `|C_empty|`=0.00043 |

Raw sum: 3+3+4+3+5+5+6+13 = 42 — but stage 3 and stage 4 both separately
compute the shared `ours-small` prerequisite (`λ=19.96` cells, identical in
both logs) when run as standalone `--only` invocations; deduplicating per
this program's own R19 discipline (call-count ≠ distinct-check-count) gives
**41 unique checks, all `[PASS]`, every one independently confirmed by
direct execution this session** — matching this program's own long-
established `--only 12346789` figure exactly, and every headline value
matches the historical figures cited above bit-for-bit (no drift, no
regression). `git diff --stat -- lab/` confirmed empty throughout. **41/41
green.**
