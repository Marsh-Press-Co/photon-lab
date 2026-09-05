# Phase 5 Review — MATERIALS & METAMATERIALS (exp-113, Panel Iteration 90)

*Fresh sub-agent, blind context. I have not seen and did not seek out any
other seat's Phase-5 output this cycle. Charter (verbatim, PANEL.md):
sub-wavelength structure; what could physically realize the proposed
optical behavior; owns the realizability bound (published / plausible /
unobtainium-with-parameters). Read `PANEL.md` in full; `LOGBOOK.md`'s
RULED OUT registry (R1–R31 in full, R27–R31 read closely — this seat's
own finding founded R28's companion caution and Fix 2 of this cycle),
the T28 live-thread opening (`sed -n '3094,3200p'`), and the full
Iteration-89 entry (`sed -n '24215,24415p'`). Read every file in
`experiments/113-t28-r312-cpl25-plus168-bin/` in full:
`phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `NOTES.md`, `run113.py`, `chunk_runner113.py`,
`analyze113.py`, `results.json`. Independently re-ran*
`python3 -c "import sys; sys.path.insert(0,'experiments/113-t28-r312-cpl25-plus168-bin'); import run113 as R; print(R._SPONGE_MARGIN_ORDERS_FLOOR, R._SPONGE_MARGIN_ORDERS_SIGNAL, R._SPONGE_MARGIN_ORDERS_DELTA)"`
*and cross-checked every load-bearing number in `results.json`,
`chunk_runner113.py`, and `analyze113.py` against fresh, independent
recomputation from primitives — never taken any figure below from this
document's own prose. No real FDTD was run.*

## Verdict: **CONFIRM-WITH-GAPS**

My own charter's substantive burden (realizability bound: published /
plausible / unobtainium-with-parameters) is not engaged this cycle — T1
is N/A, confirmed independently, and no new material or mechanism is
proposed. What I *can* confirm is narrower and process-oriented: this
seat's own Fix 2 (three-figure sponge-margin disclosure) landed correctly
and completely, the `DISCLAIMER` text matches its Phase-2 spec in
substance, the cost-gate refusal is real and correctly gates upstream of
any spend, and zero real r=312 scoring FDTD calls occurred — matching
the brief exactly. "CONFIRM" on everything I re-derived; "-WITH-GAPS"
because the cycle's own headline outcome is a genuine non-result (the
named-bin question deferred a third time) and because one of my own
Phase-2 critique's forward-looking asks (a `min(|peccored|,|hollow|)`
figure) is present, but the underlying realizability-relevant question
this bin exists to answer — real structure vs. grid artifact — remains
completely unresolved, now with the added complication that even the
diagnostic direction (R32/Fix 5) is unvalidated at this bin's own
geometry and cannot become validated without data this cycle could not
obtain.

## Finding 1 — Fix 2's three-figure sponge-margin disclosure: CORRECT and COMPLETE

Independently re-ran the exact command specified:

```
FLOOR:  4.01750990406764
SIGNAL: 3.4297964514362818
DELTA:  2.4664481228313373
```

These match, to full float precision, both `NOTES.md`'s own claimed
figures (`~4.02` / `~3.43` / `~2.47`) and `phase2_redteam_audit.md`'s own
independently-recomputed figures (`4.0175` / `3.4298` / `2.4664`) —
bit-exact three-way agreement (Red Team's audit / `run113.py`'s live
constants / my own fresh re-derivation). I additionally recomputed all
three from raw primitives, outside `run113.py`'s own import path, using
only `BASELINE_FLOOR`, `BASELINE_PECCORED`, `BASELINE_HOLLOW`,
`BASELINE_DELTA`, and `_SPONGE_LOG_ATTEN_CPL25` read directly out of the
module — identical to 15 significant figures. This is a completely clean
re-derivation: no rounding drift, no stale constant, no hand-typed number
anywhere in the chain (R4 discipline genuinely honored).

The underlying operands also check out independently:
- `_SPONGE_ABS_VAL = exp(-17.242357) = 3.248923608023393e-08` — reused,
  not re-derived, from exp-112's own Phase-2/Phase-5-corrected figure;
  correctly `cpl`-specific (25) and correctly NOT `r`-specific (ABSORB/
  EDGE depend on `cpl` alone — I independently confirmed
  `geom_fixedabs_cpl(312,25)["absorb"] == geom_fixedabs_cpl(156,25)["absorb"] == 50`).
- `BASELINE_FLOOR = 3.3826e-4`, `BASELINE_PECCORED = 8.740e-5`,
  `BASELINE_HOLLOW = 9.692e-5`, `BASELINE_DELTA = -9.510e-6` — these are
  exp-110's own committed r=312/`cpl=20` values, not this cycle's own
  (nonexistent) real `cpl=25` data. **This is the load-bearing fact for
  the brief's own "data-dependent vs. baseline-derived" question**: Fix
  2's entire figure set is derived from already-committed exp-110
  baseline data plus the reused exp-112 sponge constant — it never
  depended on this cycle's own r=312/`cpl=25` FDTD calls, which never
  happened. Fix 2 is exactly correct **regardless of** the cost-gate
  refusal; nothing about the REFUSED outcome puts this fix's own
  correctness at risk. Same is true of Fix 1 (box_a clearance in
  wavelengths, `3.2λ`/`6.4λ` — pure `geom_fixedabs_cpl` arithmetic,
  independently reproduced) — both are geometry/baseline-derived, not
  data-dependent, so both remain fully trustworthy even with zero r=312
  scoring calls this cycle.

By contrast, Fix 5 (Check-C direction validation via
`resolved_unresolved_crosstab` on r=312's own real data) is genuinely
data-dependent and was **not** exercised: I traced `analyze113.py` and
confirmed it early-exits at the gate-refused branch (`raise
SystemExit(0)` immediately after writing the REFUSED `results.json`,
before ever reaching `analyze_r312_cpl25()` or the crosstab call). Fix
3b/Fix 4 (the R31 control machinery) sit in between — they ARE
data-dependent and WERE genuinely exercised against real data this
cycle (six real FDTD calls, all r=156/cpl=25, producing the short/
sustained control readings in `results.json['r31_control']`), just not
against the r=312 data the cycle's own named-bin question needed.

## Finding 2 — `DISCLAIMER` text matches the Fix 2 spec, word-for-word in substance

`phase2_redteam_audit.md`'s Fix 2 spec requires three labeled figures:
- `_SPONGE_MARGIN_ORDERS_FLOOR` — "relative to the instrument's own K=1
  noise-floor scale"
- `_SPONGE_MARGIN_ORDERS_SIGNAL` — "relative to the named bin's own
  signal magnitude"
- `_SPONGE_MARGIN_ORDERS_DELTA` — "relative to `|delta|`, the quantity
  Check B actually scores"

`run113.py`'s live `DISCLAIMER` string (lines ~516–532) reads: "relative
to the instrument's own K=1 noise-floor scale (`{BASELINE_FLOOR}`),
`~{FLOOR:.2f}` orders of magnitude; relative to the named bin's own
signal magnitude (`min(|peccored|,|hollow|)={...}`), `~{SIGNAL:.2f}`
orders; relative to `|delta|={...}` (the quantity Check B actually
scores), `~{DELTA:.2f}` orders — all three non-fatal... but genuinely
different numbers, not interchangeable." This is the spec's own three
labels, in the spec's own order, verbatim in substance — not merely
"a similar disclosure," an actual match down to the specific phrase
"the quantity Check B actually scores." I confirmed the numeric
interpolations (`{FLOOR:.2f}` etc.) render as `4.02`/`3.43`/`2.47` by
re-running `python3 run113.py --predictions-only` myself — unchanged
from the cited figures. No gap here: this seat's own Phase-2 critique
was fully and correctly closed.

I also independently checked the "single figure only" failure mode my
own Phase-2 critique named as the verdict-flipping condition (shipping
`_SPONGE_MARGIN_ORDERS` as the sole disclosed figure): grepped
`run113.py` for any remaining bare, unlabeled `_SPONGE_MARGIN_ORDERS`
reference — none exists; only the three suffixed constants are defined
or used anywhere in the file. Confirmed clean.

## Finding 3 — a realizability angle worth naming for a future cycle attempting this bin's own physical fabrication question

This remains instrument-fidelity work, not phenomenon work — no
realizability verdict is due this cycle, and I do not score one. But if
a future cycle ever asks "could a real fabricated shell/core structure
exhibit the near-field feature this bin's `cpl=20` reading hints at,"
two facts from this cycle bear directly on that future question and
should not be lost:

1. **Scale is squarely in the published/plausible metamaterial-shell
   regime, at both radii, not a new tier.** Independently recomputed:
   at `cpl=25`, `R_COAT=390` cells ⇒ physical shell radius
   `390/25 = 15.6λ ≈ 9.36 µm` at 600 nm (r=312); at r=156,
   `R_COAT=195` cells ⇒ `7.8λ ≈ 4.68 µm`. Both sit at scales where
   graded-absorptive-shell/PEC-core sub-wavelength boundary control is
   published/plausible with existing e-beam- or FIB-patterned lossy
   metasurface fabrication (tens-of-nm placement tolerance against a
   micron-scale feature) — consistent with, and reproducing, my own
   Phase-2 critique's background note. No new fabrication-tier finding
   this cycle; named for continuity since a future cycle inheriting this
   bin should not have to re-derive it.
2. **Fix 1's own box_a-in-wavelengths confound (3.2λ vs 6.4λ) is a real
   materially-relevant caution for any future fabrication argument, not
   just a diagnostics-instrument footnote.** If a future cycle wants to
   argue that a physical shell would exhibit a comparable near-field
   feature at the probed angular location, the *physical probe depth*
   past the coat surface differs by exactly `kappa_ratio=2.0` between
   the two legs this program has now run (independently confirmed:
   `(box_a_hw − CX − R_COAT)/cpl` = 3.2 at r=156 vs 6.4 at r=312, present
   already at `cpl=20`, so it is a geometry fact, not a refinement
   artifact). A real material's own near-field decay length (set by its
   dielectric/absorptive profile, not by this program's grid) must be
   compared against the ACTUAL probe depth used at whichever `r` a
   future cycle cites — "the companion bin" framing this cycle's own
   Fix 1 already warns Phase 5 away from cross-leg-conflating applies
   with equal force to any future fabrication-realizability argument
   built on either leg's own reading in isolation.
3. **The realness-vs-artifact question itself is a precondition for any
   future realizability bound, and it is currently unresolved in a way
   that specifically blocks my own charter.** Check A stays AMBIGUOUS-
   by-construction at `cpl=20` for this bin (`local_snr` 0.258/0.287,
   both <1) and Check C's own diagnostic direction (R32/Fix 5) is
   explicitly `direction_validated=False`, unresolvable without the very
   r=312 data the cost gate refused. Until Check A/C jointly determine
   whether this bin's 10.88% deviation is genuine PEC-core/shell-
   boundary field structure or Yee-grid discretization noise, there is
   literally nothing for MATERIALS to bound — "realizability of a grid
   artifact" is not a coherent question. This is the concrete reason my
   own charter has nothing more to say this cycle beyond process
   verification, and it is also the concrete reason Finding 4, below,
   matters for MATERIALS specifically, not only for cost management.

## Finding 4 — the cost-gate refusal and what it changes about a cheaper materials-relevant geometry variant

I traced `geom_fixedabs_cpl`'s own domain-sizing formula
(`experiments/112-.../run112.py` lines 99–127) to check whether `box_a`
(the monitoring sub-region Fix 1 concerns) drives simulation cost at
all — it does not: `N`, `CX`, `CY`, `STEPS` (the cost drivers) scale with
`kappa_of(r) * ratio`, entirely independent of `BOX_A_MARGIN0`. So a
narrower `box_a` margin is not a lever for a cheaper leg; it only changes
what is measured, not what is computed. The real lever is `r` itself: the
cost-gate's own measured `kappa_exponent≈3.205` (independently confirmed
against `results.json['cost_gate']['raw']['kappa_exponent']=3.2053`) means
cost scales roughly as `kappa_ratio**3.2`, and `kappa_of(r)=r/78` (I
confirmed `kappa_of(156)=2.0`, `kappa_of(312)=4.0`, `kappa_ratio=2.0`
between them, matching `results.json` exactly).

**Concrete, cheaper alternative for Iteration 91, still answering a
materials-relevant question**: an intermediate radius between the two
already-tested endpoints — e.g. `r=234` (`kappa=3.0`, `kappa_ratio=1.5`
relative to the r=156/`cpl=25` pilot) — projects to roughly
`1.5**3.2 ≈ 2.98×` the pilot cost, versus `2.0**3.2 ≈ 9.24×` for the full
r=312 leg actually attempted this cycle — **about 32% of this cycle's
own projected/refused cost** for a genuinely new data point. This would
not answer the named `168.75°`/r=312 bin's own question directly, but it
would do two things this cycle's refusal leaves undone at low
incremental cost: (a) give the empirical `kappa_exponent` a third,
independent calibration point (currently fit from only two `r`
observations, r=156 and r=312, both from the SAME pilot/projection
chain — a third point at a genuinely different scale is the kind of
check R15's own two-point-insufficiency discipline already flags this
thread as needing); (b) give Fix 1's own box_a-wavelength confound and
Fix 2's own sponge-margin figures a third geometry to independently
re-verify against, at a fraction of the cost that just got refused. I
name this as a candidate, not a proposal — scope/sequencing is the
Director's call, and it competes with the Reconciled queue's own named
Tier-1 item (re-attempting r=312 itself with a corrected, now-real
control baseline).

One more cost-gate observation bearing on my own charter, stated
narrowly: the refusal is a **compute-budget** fact, not a
**realizability** fact — the physical structure being modeled (shell
radius, sponge thickness, etc.) is unchanged by whether the simulation
ran. Nothing about "16737.4s vs 10800s" bears on published/plausible/
unobtainium for this bin's own geometry; that bound would be unaffected
even if the FDTD had run and returned data. I flag this only because the
brief invites the connection — worth stating explicitly so a future
reader does not conflate "the simulation was too expensive to run" with
"the material is too hard to fabricate," two entirely independent axes
this cycle's own framing keeps properly separate throughout.

## Ranked top-3 candidate directions for Panel Iteration 91 (MATERIALS' own ranking)

1. **Re-attempt the `+168.75°`/r=312 leg with the NOW-REAL, this-cycle-
   measured control baseline**, per the Reconciled queue's own standing
   Tier-1 item — this session's own real per-step throughput
   (`0.406×` historical) is now on file; a future session's own R31
   control point will tell honestly whether THAT session can afford the
   leg, rather than re-deriving a projection from a two-cycle-old
   cross-session figure again. This is the single highest-value item
   this cycle's own refusal actually creates (a materially different,
   truthful starting point for the next attempt), not merely a repeat of
   what was already queued.
2. **A genuinely cheaper intermediate-`r` data point (e.g. `r=234`,
   ~32% of this cycle's own refused-leg cost)** — independently
   motivated above (Finding 4): a third `kappa_exponent` calibration
   point and a third geometry to re-verify Fix 1/Fix 2's own figures
   against, at a fraction of the r=312 cost, while the r=312 leg itself
   remains gated on item 1's own fresh control.
3. **Once real r=312 data eventually lands (by whichever route), execute
   Fix 5's `resolved_unresolved_crosstab` immediately** — it is already
   written, zero marginal FDTD cost, and is the only thing that can
   resolve R32's own direction-validation question at this bin's actual
   geometry. Until it runs, MATERIALS' own eventual realizability
   question for this bin (Finding 3, item 3) has no defensible answer in
   either direction, and no future cycle should cite Check C's own
   percentile reading evidentially before it does — a restatement, from
   my own charter's angle, of `run113.py`'s own already-correct
   `direction_validated=False` posture, which should not quietly lapse
   in a future cycle's haste to finally get real r=312 data scored.

Secondary, lower-priority but still real and now sixth-consecutive-cycle
undone: MATERIALS' own long-deferred fabrication-tolerance bound
(named in `phase1_proposal.md` §3 as "fifth consecutive cycle" before
this cycle also declined it) — I do not rank it above the three items
that keep this specific bin's own data pipeline honest, but it should not
silently become a seventh-cycle debt without an explicit Director
decision to keep deferring it.
