# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 59 · exp-082

**Seat:** VISION SCIENCE (human perceptual limits — contrast thresholds,
luminance edge detection, spectral sensitivity, adaptation, temporal
sensitivity, attentional blindness; duty: pin numeric thresholds, with
sources, BEFORE any run that scores against them). Blind to other seats'
current-cycle critiques.

## Steel-man (≤150 words)

The secondary metric gets the R9 lesson's *letter* right, on purpose, not
by luck: `A_scene = ptp(ΔC_scene)` is built entirely from `contrast_from_
runs`'s raw `C`, never the fitted-local-carrier-normalized `amp_ratio`
that caused the original T16/R9 dimensional error. Both operands —
`A_scene` and `C_thr` — are the same dimensionless Weber-contrast unit;
the proposal names the R9 convention explicitly and follows it. The
metric is also correctly scoped as "disclosed, not gating" — it never
drives the pre-registered SURVIVES/CANCELS verdict, which rests entirely
on `ratio = A_scene/A_empty`, an internally consistent comparison (same
7-point ptp convention, numerator and denominator alike). The
reproduction precondition (bit-exact vs exp-076's committed headline,
`max_dev=0.0`) is exactly the R4 discipline this sub-thread has followed
throughout, applied correctly before a single new number was trusted.

## Sharpest attack (≤150 words)

`C_thr(L)` is T2's pinned threshold for a single, static Weber contrast at
fixed adaptation — the JND for one steady scene (Blackwell/Rose
calibration). `A_scene` is peak-to-peak of a *difference between two
numerical domain-treatments* of the same physical scene, swept across 7
angles — no human ever views that quantity directly. Units match (R9's
letter), but the *kind* of quantity doesn't — this program already named
this gap for this exact bar (LOGBOOK: "`C_thr(L)` is a static-target
threshold applied to a physically transient event," T3, unresolved). Worse,
`A_scene`'s estimator is unstable: 7 points at 1° step against a ~2.84°
period is ~2.8 samples/cycle, near-Nyquist. The "5.5× larger than T16"
comparator mixes this raw aliased ptp against T16's `√(Ai²+Aq²)`, a
*fitted-sinusoid peak amplitude* — ptp-equivalent `≈1.23×10⁻³`, not
`6.153×10⁻⁴` — so the true ratio is closer to `4.2×`. Non-equivalent
estimators, compared as if commensurate.

## Verdict: **support-with-changes**

The primary, gating result (`ratio=0.6573`, SURVIVES) is sound: both
numerator and denominator share one convention, computed identically, and
I don't dispute it. The secondary metric needs correction before Phase 3
lets it inform any future citation: (1) relabel `A_scene/C_thr` explicitly
as an *instrument-uncertainty-budget* number, in T16's own established
idiom (compare a swing to a real citation's *margin* against `C_thr`, not
to `C_thr`'s raw value as though the artifact itself were a viewable
contrast) — never phrase it as "68% of the way to visible"; (2) disclose
that this number was measured on the flagship absorber (`C≈−0.55`, far
from threshold), not a near-threshold σ(I) article — the only case where
this artifact could plausibly flip a real PASS/MARGINAL call; (3) fix or
drop the "5.5×" cross-cycle comparator — it currently divides two
different amplitude estimators of nominally the same signal.

## Record-hygiene audit (task-specific, beyond the standard Phase-2 fields)

- **NOTES.md**: complete for its declared scope — explicitly labeled
  "Phase 1 only... at time of writing," matching exp-081's/exp-076's own
  precedent of deferring T1/R6/new-machinery dispositions to
  `phase1_proposal.md` rather than restating them inline. Hypothesis /
  Setup / Result / Learned / Next are all present and populated.
- **Verdict fields**: appropriately populated for this stage — a
  self-scored Phase-1 verdict (SURVIVES) is stated; no Combined Verdict is
  claimed prematurely (correctly deferred to Phase 3, per the document's
  own explicit disclaimer in NOTES.md's opening paragraph).
- **T1-escape-route N/A**: stated once, correctly, in `phase1_proposal.md`
  §3 ("N/A... instrument-fidelity/generalization work, not a constraint-3
  mechanism candidate"). Checked `run.py`, `results.json`, and NOTES.md for
  any place a scored contrast is used as evidence for/against a T1 escape
  route — found none. Applied consistently.
- **New finding**: `git log` shows commit `5bb78df` bundles
  `phase1_proposal.md` (the predictions text), `run.py`, **and**
  `results.json`/`run_output.txt` at 27/29 FDTD calls already complete —
  into one commit. There is no git-commit boundary separating "predictions
  frozen" from "run executed" at all (worse than exp-081's own gap one
  cycle ago, where at least file mtimes suggested some separation). Per
  the exp-081 precedent (my own seat, Iteration 58), PANEL.md's
  git-before-run mandate literally binds Phase 3, not Phase 1, so this is
  **not a rules violation** — but it is the same auditability regression
  recurring a second consecutive cycle, now under a different lead seat,
  after being named explicitly last time. Worth a same-shift fix (commit
  the x-wall/phase-convention riders' own predictions similarly going
  forward) and worth flagging that a third recurrence should not be read
  as a close call.

## Parameter change that would flip my verdict

To **oppose**: if Phase 3 lets the "`A_scene/C_thr=0.68×`" / "5.5× larger"
framing stand as a literal near-threshold perceptual-detectability claim
about the padding artifact itself — without the static-vs-swept caveat or
an estimator fix — that repeats T16/R9's exact failure shape in this
program's permanent record, one cycle after Checkpoint criterion 4 fired
on the first instance. To move cleanly to **support**: relabel item (1)
above and drop or correct the "5.5×" comparator; the primary SURVIVES
result needs nothing further from my seat.
