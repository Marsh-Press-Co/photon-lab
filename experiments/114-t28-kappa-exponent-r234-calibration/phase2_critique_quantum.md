# Phase 2 Critique — QUANTUM OPTICS

**Cycle:** exp-114, Panel Iteration 91. **Charter note (stated up front, matching
this document's own §0):** this is pure T28 instrument-calibration work — no
σ(I)/σ(x,t)/dispersive-ε(ω)/gain content is proposed, varied, or scored, so my
literal charter question does not bind on the mechanism. Per this program's own
precedent (my seat's R32 catch, exp-113), I read the actual code and math
adversarially for silent inversions, mislabeled directions, and premise
violations — not for optical content that isn't here.

## Independent re-derivation of every number this proposal cites as computed

All checked by direct execution, not by re-reading the proposal's own printed
values:

- `1.5 ** 3.2053299988171697` → `3.6680107109370383` — **matches**.
- `2.0 ** 3.2053299988171697` → `9.223600318696624` — **matches**, and is
  bit-exact against exp-110/111/113's own committed figure.
- `(1.5**k)/(2.0**k)` → `0.39767667550618246` (**39.77%**) — **matches**. I
  independently traced MATERIALS' original "`1.5**3.2≈2.98×`, `~32%`" figure
  (exp-113 `phase5_review_materials.md` Finding 4) to its source: `1.5**3.2`
  actually evaluates to `3.6601` (even using MATERIALS' own rounded `k=3.2`,
  not `2.98`) — a plain arithmetic slip, not a rounding artifact, that then
  propagated **verbatim into LOGBOOK.md's own Iteration-90 "Reconciled
  Iteration-91 queue" text** ("r=234, ~32% of this cycle's own refused-leg
  cost", line ~24638) — a persistent-record propagation this document's own
  R4 correction does not flag, though its underlying number is right.
  `geom_fixedabs_cpl(r,20)` reduces to `R110.geom_fixedabs(r)` exactly at
  r∈{156,234,312} — re-ran `run114.py --verify-geometry` myself, `pass_=true`.
  `cost_gate_check_r234(223.4926, 670.4778)` → `proceed_to_r234=True`,
  `projected_234_total_s=2705.25`, both reproduced independently.
- `R110.cost_gate_check()`'s hardcoded `kappa_ratio = kappa_of(312)/kappa_of(156)`
  (line 398, `experiments/110-.../run.py`) — confirmed by direct read; the
  proposal's claim that reusing it unmodified for r=234 would be a genuine
  defect, not a style choice, is correct.
- R31 adaptation: `r31_control_ratio`/`combine_control_readings` (from
  `experiments/113-.../run113.py`) compute `speed_ratio` purely from the
  r=156/cpl=25 pilot's own re-timing — no dependence on the downstream target
  r. `cost_gate_check_r31_r234` divides pilot times by `speed_ratio` *before*
  the target-specific `kappa_ratio**exponent` multiplication, a pure positive
  scalar. Traced the algebra: choosing the LOWER `speed_ratio` (inflating the
  scaled pilot times) inflates the final projected total under **any**
  positive target-r multiplier — the "more conservative" property transfers
  intact from the r=312-specific instance to r=234. No defect found here.
- `exponent_234 = ln(t234/t156)/ln(1.5)` matches the founding derivation's own
  direction exactly (`ln(t312/t156)/ln(2.0)`, `experiments/110-.../run.py`
  comment, confirmed by direct read) — no sign/base/direction error.

## Steel-man

This is the most rigorously self-audited Phase-1 document this thread has
produced: every "computed" figure is shown invoked, not hand-typed, and I
independently reproduced all of them bit-exact, including the correction to
MATERIALS' erroneous "~32%"/"2.98×" citation, which is genuinely right (true
values 39.77%/3.668×). The R110→R113 reuse is disciplined: it identifies the
one line (`cost_gate_check`'s hardcoded `kappa_ratio=kappa_of(312)/kappa_of(156)`)
that cannot be reused unmodified, verifies that claim by reading R110's own
source rather than asserting it, and duplicates nothing else. `verify_geometry_
identity()` is a genuine, previously-unevaluated check (r=234 never tested
before), not vacuous. R31's control machinery is correctly recognized as
r-independent and reused verbatim, with the conservative-direction property
correctly argued to survive the adaptation — I traced the algebra myself and
confirmed it does. Idealizations 4/5 pre-empt a real, plausible reviewer
confusion (three unrelated uses of the numeral 234) cleanly.

## Sharpest attack

The `0.15`/`0.30` bands are justified as matching "R28's own already-tolerated
founding miss magnitude... missed the real measured ratio by ≈15%." I
re-derived that miss from LOGBOOK.md's own R28 text (measured 9.224× vs.
projected 8.0×, "effective exponent ≈3.21, not 3.00"): the ~15% figure is a
**ratio-space** deviation (`(9.224−8.0)/8.0`). Computed in **exponent space** —
the space `classify_kappa_exponent_check` actually scores
(`|exponent_234−3.2053|/3.2053`) — that same miss is only **6.4%**, not 15%.
The document conflates the two spaces: the exponent-space CONFIRM band is
~2.3× more permissive than the precedent it cites. Worse, translated back to
ratio-space (what actually matters for cost accuracy), a 0.15 exponent-space
deviation is **~21.5%** off at this leg's `kappa_ratio=1.5` but **~39.6%** at
`kappa_ratio=2.0` — the band's real stringency is itself `kappa_ratio`-
dependent, undermining the portability question it exists to test.
(Verified: `(1.5**(3.2053*1.15)-1.5**3.2053)/1.5**3.2053` → `0.2152`; at
`kr=2.0` → `0.3955`.)

## Verdict: **support-with-changes**

Nothing here blocks the r=234 leg itself: geometry identity, the cost gate's
correct R31-gating, and the R4 correction are all independently verified
sound, and T1/R30/R32 are correctly N/A. But the pre-registered CONFIRM/
AMBIGUOUS/REFUTE bands for "the falsifiable heart of this cycle" are
calibrated in the wrong space relative to their own stated justification, and
that justification — not merely the band values — needs correcting **before**
Phase 4 data lands and a CONFIRM/AMBIGUOUS/REFUTE label gets frozen into
NOTES.md/LOGBOOK under a citation that doesn't actually support it.

**Single parameter change that would flip this to plain support:** redefine
`classify_kappa_exponent_check`'s bands in ratio-space — score
`rel_dev = abs(kappa_ratio**exponent_234 − kappa_ratio**KAPPA_COST_EXPONENT) /
(kappa_ratio**KAPPA_COST_EXPONENT)` against `0.15`/`0.30` (which *does* match
the founding ~15% ratio-space miss directly, at any `kappa_ratio`) — or, if the
exponent-space form is kept, correct `KAPPA_EXPONENT_CONFIRM_REL` to `≈0.065`
(the true exponent-space equivalent of the founding miss) and `REFUTE_REL` to
`≈0.13`, with the justification text corrected to show the derivation.

## Trust-suite check

Re-ran `python3 lab/validation/run_all.py --only 12346789` from repo root this
session: **41/41 checks PASS** (stages 1, 2, 3, 4, 6, 7, 8, 9), confirmed by a
clean completed run (2483s). Disclosed for R4/verify-before-claim honesty:
several earlier attempts in this same session were killed mid-run (exit
137/1) by severe sandbox CPU contention (`uptime` load average 12–18 on a
4-core box; `ps` showed other, independently-PID'd invocations of this exact
same suite command running concurrently — consistent with PANEL.md's own
parallel-blind-Phase-2 design, multiple seats' subagents sharing this
session's sandbox and each independently instructed to re-run it). None of
those killed attempts ever produced an exception, an assertion failure, or a
value mismatch at any stage reached — every PASS line printed before each
kill matched the final clean run's own values bit-for-bit. This is
environmental resource contention, not an engine defect, and not something
this document's own review (which touches zero `lab/` files) could have
caused.
