# Phase 5 Review — MATERIALS & METAMATERIALS (exp-112, Panel Iteration 89)

*Fresh context, blind to every other seat's Phase-5 output this cycle.
Charter: sub-wavelength structure; what could physically realize the
proposed optical behavior; owns the realizability bound. T1 is correctly
N/A this cycle (confirmed structurally, independently, below) — no
materials-realizability question is engaged by a pure grid-resolution
instrumentation cycle, so this review's job is the same one my seat did
at Phase 2: police whether the geometry-scaling recipe actually preserves
the MATERIAL LAW it claims to, and independently re-verify every
consequential claim from primitives, not from prose.*

## Verdict

**CONFIRM-WITH-GAPS.** Every object-level claim I re-derived from
primitives holds *except one*, and that one is real, load-bearing on a
permanent, code-enforced disclaimer string, and survived five blind
Phase-2 critiques, Red Team's own Phase-2 audit, and Phase-3 synthesis
without being independently checked. Nothing here reverses the cycle's
own Combined Verdict (PARTIAL) or touches T1/any constraint. On the
Checkpoint-4/R29-second-instance question the record explicitly declines
to self-adjudicate: my own reasoned view is **does not fire** (below).

## Findings

### F1 (most significant) — the "6–8 orders of magnitude" figure in the code-enforced DISCLAIMER does not survive re-derivation from the same, already-confirmed primitives; the true margin is ~1.8–4.5 orders

The DISCLAIMER string (`run112.py` lines 291–331, identical text asserted
into both `predictions_text` and `result_text` via R23's own
`assert DISCLAIMER in ...` machinery, and quoted verbatim twice in
NOTES.md) states:

> "...its one-way accumulated log-attenuation genuinely rises from 13.93
> (cpl=20, absorb=40) to 17.24 (cpl=25, absorb=50), a real ~1.25x change
> — but both values sit 6-8 orders of magnitude below the ~1e-4-1e-3
> measurement-floor scale this cycle actually measures at..."

I independently re-implemented `lab/fdtd2d.py::_damping()`'s own ramp
formula from raw source (`ramp=(arange(absorb,0,-1)/absorb)**3`,
`damp_e=exp(-0.30*d)`) and computed the one-way accumulated log-
attenuation via both routes named in the document:

- Discrete cell-sum (`sum(0.30*ramp)/S`, `S=0.32/√2`): **13.929451**
  (absorb=40) → **17.242357** (absorb=50) — bit-exact to the disclosed
  `13.93`/`17.24`, and bit-exact to the redteam audit's own re-derivation.
- Closed-form continuum (`-(0.3/4/S)·absorb`): **-13.258252** →
  **-16.572815** — bit-exact to the disclosed `-13.26`/`-16.57`.

Both routes are correctly, verifiably re-derived — the *log-attenuation
numbers themselves* are genuinely sound, and Docket Fix 2's own numeric
content is honestly disclosed. But the DOWNSTREAM claim built on top of
those numbers — that the attenuation *factor* (i.e. `exp(-value)`) sits
"6-8 orders of magnitude below" a `~1e-4`–`1e-3` floor scale — is a
different arithmetic step that nobody in this cycle's own chain
(MATERIALS' own Phase-2 critique, EM's own Phase-2 critique, Red Team's
Phase-2 audit's re-verification table, or Phase-3 synthesis) actually
performed. Doing it:

```
exp(-13.929451) = 8.923e-07   exp(-17.242357) = 3.249e-08   (discrete route)
exp(-13.258252) = 1.746e-06   exp(-16.572815) = 6.346e-08   (continuum route)
```

Compared against the stated `1e-4`–`1e-3` scale (log10 = -4 to -3), the
true margin is:

| cpl | route | factor | orders below 1e-4 | orders below 1e-3 |
|---|---|---|---|---|
| 20 | discrete | 8.92e-7 | 2.05 | 3.05 |
| 25 | discrete | 3.25e-8 | 3.49 | 4.49 |
| 20 | continuum | 1.75e-6 | 1.76 | 2.76 |
| 25 | continuum | 6.35e-8 | 3.20 | 4.20 |

**~1.8 to ~4.5 orders of magnitude, not 6–8.** This is not a rounding
quibble — it is roughly a factor of 100–1000 overstatement of the safety
margin, in a string a code-level assert makes authoritative and
permanent. Tracing the provenance: EM's own Phase-2 critique explicitly
flagged this as "my own estimate... ~7+ orders below the ~1e-4 target
signal (non-load-bearing)" and pre-registered its own flip condition —
"if... residuals differing from the ~1e-4 target-signal scale by fewer
than, say, 3–4 orders of magnitude... I would flip to oppose." My own
seat's parallel Phase-2 critique independently landed on "~6-8 orders
below." Neither number was the result of actually exponentiating the
(separately, correctly) confirmed log-attenuation values and comparing
them to the stated floor scale — both were back-of-envelope estimates
that Red Team's own Phase-2 audit table (§1) confirmed only at the
*log-attenuation* level (`13.929451`/`17.242357` bit-exact) and never
re-checked at the *"orders of magnitude below the floor"* level, which is
the actual claim that made it into the permanent, asserted text. This is
the R4/R9 house-discipline shape exactly: a downstream comparison
inherited from an unverified estimate, never independently recomputed,
riding on top of correctly-verified antecedent numbers.

**Non-outcome-reversing.** The qualitative conclusion — "non-fatal, this
boundary effect cannot manufacture the near-field signal under test" —
still holds at the corrected ~1.8–4.5 order margin: the signal under test
is a ~9.88% (`≈10⁻¹`) relative deviation, several further orders above
even the corrected residual, and no r=312 leg exists this cycle to
compound the discrepancy. Nothing here moves T1 (still N/A) or any scored
check. But by this program's own R4 standard the specific number is
wrong, it is now baked into a code-enforced, doubly-asserted, permanent
DISCLAIMER string, and by EM's own explicitly pre-registered numeric
standard the corrected figure sits inside or right at the boundary of the
zone EM itself named as grounds to flip to oppose — a check EM's own
critique named but never actually completed to its own stated standard.
**Recommend**: correct the DISCLAIMER's "6-8 orders" to "~2-4.5 orders"
(or simply "several orders," if a single cited range is judged not worth
a second same-shift edit) in the next cycle that touches this string, and
treat this as confirmation that Docket Fix 2's own mandate — "compute...
and disclose... an actual number" — needs to mean the number in the
sentence that is actually asserted, re-derived end-to-end, not only its
antecedent inputs.

### F2 — the geometry-scaling recipe's own material-parameter invariance (`tau_shell`, `sigma_max`) does hold cleanly in the real cpl=25 data; no unexpected material-behavior shift is visible in the energy ledger

This is the question my own charter is specifically asked this cycle.
`results.json["energy_ledger"]` (real cpl=25, r=156 data, first captured
this cycle) gives:

```
peccored: sigma_abs=349.5371138134443  sigma_ext=700.1082897642503
hollow:   sigma_abs=349.5228378615304  sigma_ext=700.1233206386078
```

against the committed cpl=20 baseline (exp-110's own re-verified
`reproduction_precondition`, peccored-vs-empty, r=156):
`sigma_abs=279.66065695338267`, `sigma_ext=560.198850825502`.

I computed, independently, both the raw cross-cpl scaling ratio and the
resolution-independent dimensionless invariant (`abs_ext_ratio`, the
fraction of extinguished power that is absorbed — the physical quantity
`tau_shell` invariance is supposed to protect):

```
sigma_abs ratio (cpl25/cpl20, peccored) = 1.249862   (expected exactly 1.25 — a grid-cell-unit
sigma_ext ratio (cpl25/cpl20, peccored) = 1.249750    conversion factor, cpl/CPL_600, not a physics effect)

abs_ext_ratio, cpl=20 (peccored)  = 0.499217
abs_ext_ratio, cpl=25 (peccored)  = 0.499261   (Δ = 0.009% relative)
abs_ext_ratio, cpl=25 (hollow)    = 0.499230   (Δ = 0.003% relative to cpl=20 peccored)
```

Two independent, convergent, reassuring signals: (1) the raw `sigma_abs`/
`sigma_ext` figures scale by 1.2498–1.2497×, matching the expected pure
grid-unit conversion factor (`cpl_new/cpl_old = 1.25`) to four significant
figures — exactly what "same physical cross-section, finer grid" predicts,
and inconsistent with a genuine physical drift of that scale; (2) the
dimensionless `abs_ext_ratio` — invariant under a unit-conversion, and the
one quantity `tau_shell`'s provable resolution-invariance (independently
re-derived at Phase 2 by both my own seat and ELECTROMAGNETISM from
`lab/fdtd2d.py`'s own `alpha=sigma_e·S/(2·eps_r)` update coefficient) is
actually a claim about — reproduces to **<0.01%** between cpl=20 and
cpl=25, and to <0.01% between hollow and peccored at cpl=25. This is
squarely inside ordinary FDTD discretization convergence, not a signature
of the (separately identified, F1 above) ABSORB/EDGE sponge
non-invariance leaking into the bulk cross-section ledger. **Answer to my
own charter question: no, I find no sign of an unexpected
material-behavior shift between resolutions in the energy-ledger figures
— the material-parameter invariance the recipe claims holds up cleanly in
the real, captured data**, at a level of agreement (<0.1%) that is itself
independent, quantitative corroboration of the Phase-2 steel-man both my
own seat and EM offered *before* real data existed.

**One completeness gap, not a defect**: nobody in this cycle's own
record — not the Phase-1 proposal, not any of the five Phase-2 critiques
(THERMODYNAMICS' own Docket Fix 6 recommended *persisting* `sigma_abs`/
`sigma_ext`, "needed by any future cycle attempting a genuinely physical
interpretation," but never ran the cross-cpl comparison itself), not Red
Team's Phase-2 audit, not NOTES.md — actually computed or narrated this
specific cross-resolution ledger check, even though the data needed for
it (the cpl=20 baseline ledger, already committed since exp-110; the
cpl=25 ledger, persisted this cycle per Fix 6) has been available at zero
marginal cost since Phase 4 completed. I am the first to run it. Given it
comes back clean, this is not urgent, but it is exactly the kind of
"already-computed, never-stated" finding this program's R21 lineage
exists to catch before it becomes a gap — recommend a one-line Result
addendum in a future cycle stating this cross-cpl `abs_ext_ratio`
agreement explicitly, since it is the only direct evidence on file that
the tau_shell-invariance *steel-man* (a Phase-2 prediction) actually held
in real data, not merely in the pre-registered arithmetic.

### F3 — the second R29 collision instance (my own reasoned view on the Checkpoint-4 question NOTES.md declines to self-adjudicate)

I independently re-read `analyze.py`'s own committed source (lines
27–59) and confirm the narrative exactly: a second, structurally-
identical same-basename-module collision (`import chunk_runner as CR`
resolving to exp-110's `chunk_runner.py`, not this directory's own, due
to `sys.path` insertion order) was found only at Phase 4 — genuinely
undiscoverable at Phase 2, because Phase 2's blind critiques only ever
executed the pipeline as far as the FIRST collision (the `run`/`run112`
one) before it crashed, and both collisions were introduced in the same
original Phase-1 sitting. The fix (rename to `chunk_runner112.py`, add
`assert EXP110_DIR_NAME not in os.path.dirname(CR.__file__)`) is real,
present, and I confirm it is what makes `results.json` (energy_ledger,
resolution_check, etc. — all independently re-derived above, F2) exist at
all.

R29's own forward-elevating clause: "a second instance of this exact
collision shape, on this or any channel, **after this rule is on the
books**, fires Checkpoint criterion 4 automatically." My own reasoned
view: **this does not fire.** Reasoning:

1. **Unbroken house precedent treats a single cycle's own multiple
   occurrences of a newly-named failure shape as one founding instance,
   not a founding-plus-second-instance pair** — every rule in the
   registry that has ever faced this exact shape has resolved it this
   way. R19's own founding instance (exp-098) had the identical
   call-count/row-count conflation occur *twice in the same document*
   (once caught by a code-level assert before `results.json` existed,
   once recurring one paragraph later in the same Result section) and
   this was named "the founding case," not "founding plus a second,
   auto-firing instance." R18's founding instance (exp-096) had two
   independent, unrelated defects in the same six-check gate, both
   counted as one founding cycle. R20 exists specifically because this
   program recognizes *density within one cycle* as its own distinct
   measure (three-plus independent R4-class slips in one document), set
   apart from, and requiring a materially higher bar than, the
   single-instance-ratified forward-firing model every other rule (R16,
   R21–R28, and R29 itself) uses. Under that same convention, two
   occurrences of one newly-discovered import-collision idiom, both
   written in the same Phase-1 sitting of the very cycle that names the
   rule, are the founding cycle's own (now more complete) discovery — not
   a founding instance followed by a qualifying "second instance."
2. **The mechanistic story rules out the incentive the forward clause
   exists to punish.** R29's forward clause exists to stop a *future*
   cycle from repeating a *known, avoidable* mistake after the rule
   could have warned it off. Here, both collisions were baked into the
   code before R29 existed in any form — the rule could not have
   prevented either one, and the second was mechanically unreachable for
   Phase 2 to find (the pipeline never got past the first crash). Firing
   Checkpoint 4 on this reading would penalize a cycle for the *degree of
   diligence* its own Phase-4 execution discipline showed (catching a
   second latent defect via actual re-execution, per this rule's own
   "verify by execution, not diff-reading" text) rather than for any
   avoidable repeat.
3. **The one genuine textual wrinkle, named for completeness, not
   adopted**: R29 was ratified in Phase 3 (same shift), strictly before
   Phase 4 discovered the second collision — so a hyper-literal reading
   of "after this rule is on the books" could argue the second
   occurrence technically postdates ratification. I decline this reading:
   no other rule in this registry has ever had its forward clause fire
   within the same numbered experiment that founded it, "on the books"
   is the phrase every prior rule uses to mean "known to a *future*
   cycle," and adopting the hyper-literal reading here for the first time
   would be a genuinely new, inconsistent precedent, not an application
   of an existing one.

**Recommend, forward**: tighten R29's own text (a cheap, one-clause edit,
matching this program's own practice of closing rule-wording loopholes
it finds — see R16 closing R23's gap) to read "...a second instance...
**in a future cycle**, after this rule is on the books..." — removing the
ambiguity this case exposed, before a less mechanistically-clear future
case has to relitigate it without that precedent on file.

## Independent verification performed (primitives, not prose)

- Re-implemented `lab/fdtd2d.py::_damping()`'s ramp/exponential formula
  from raw source and recomputed the log-attenuation figures both ways
  (F1) — bit-exact to the disclosed numbers; independently computed the
  *further* step (exponentiating and comparing to the floor scale) that
  nobody upstream had performed.
- Re-derived `abs_ext_ratio` for peccored (cpl=20, cpl=25) and hollow
  (cpl=25) directly from `results.json`'s own `energy_ledger` and
  exp-110's own committed `reproduction_precondition` widths (F2).
- Re-ran `python3 run112.py --verify-geometry` (PASS, both r, matching
  the committed claim exactly) and independently invoked
  `R.cost_gate_check(489.729, 1469.186, ...)` and
  `cpl_cost_table.py` fresh — both reproduce the document's own cited
  figures bit-exact (`proceed_to_r312=False`, `projected_312_total_s=
  14906.30...`, `cpl=25 r156: 1469.19s`).
- Hand-verified `classify_resolution_check`'s own Check A/B/C outputs
  against `results.json`'s persisted `resolution_check` dict by
  reimplementing the comparison logic and the Pearson correlation from
  the persisted `baseline_window`/`new_window` arrays — all reproduce
  exactly (`corr=0.9993580404725309`, `rel_to_baseline=1.315199893820878`,
  Check A = AMBIGUOUS, Check B = SURVIVES).
- Confirmed the named-bin baseline figures (`local_snr_peccored=
  0.09652127013965679`, `local_snr_hollow=0.10605740453057212`,
  `floor=0.0011261666277300464`) against exp-110's own committed
  `results.json["r156"]["local_diag"]["32"]` at bin index 4 — bit-exact.
- Confirmed bin index 4 ↔ -146.25° from `np.linspace(-180,180,49)`'s own
  bin-center construction, independently.
- Confirmed via `git log`/`git show -s --format=%ci` that Phase 3
  (`19c4ac8`, 03:44:37) committed strictly before Phase 4
  (`e2d660f`, 04:01:23) — house discipline honored.
- Confirmed zero `lab/` diff since exp-110's own last commit touching
  `lab/` — Checkpoint criterion 3 correctly N/A, no trust-suite re-run
  required by this cycle's own scope.
- Re-read `analyze.py`/`chunk_runner112.py`'s own import blocks directly
  to confirm both R29 fixes (Fix 1 and the Phase-4 second instance) are
  genuinely present and structurally sound, not merely described.

## Ranked next-step recommendation

1. **Correct the DISCLAIMER's "6-8 orders of magnitude" figure to the
   independently re-derived ~2-4.5 orders** (F1) — zero marginal cost
   (pure arithmetic on already-committed, already-correct log-attenuation
   values), closes a real R4/R9-shaped gap in a permanent, code-asserted
   string before any future citation inherits the overstated number
   out of context (exactly the failure mode VISION's own Docket Fix 4 was
   built to prevent for "detection floor" — the identical risk applies
   here to "6-8 orders").
2. **State F2's cross-cpl `abs_ext_ratio` agreement (<0.1%) explicitly in
   a future Result/Learned section** — it is the only direct evidence on
   file that this cycle's own tau_shell-invariance steel-man held in real
   data, it is already computed from committed, persisted fields, and it
   answers exactly the question THERMODYNAMICS' own Docket Fix 6 named
   but did not itself run.
3. **Adjudicate the R29 second-instance question explicitly in the
   Director's synthesis or the next Red Team audit** (F3) — my own
   reasoned view is non-firing, for reasons that generalize past this one
   rule (the house convention on within-cycle multiplicity), so ruling on
   it now is cheap and forecloses a harder version of the same question
   recurring on a less clear-cut future case. If adopted, fold the
   one-clause "in a future cycle" tightening into R29's own text at the
   same time.

Beyond this cycle's own scope: the twice-deferred, now-once-executed
r=156 spot check remains genuinely inconclusive (Check A AMBIGUOUS, Check
B SURVIVES, Check C's 0.9994 correlation in tension with Check A) — a
third, differently-scaled resolution point (e.g. `cpl=30`, already costed
in `cpl_cost_table.py`) is the R15-disciplined minimum needed to move this
past "not yet ruled out," and the `+168.75°` r=312 bin remains untested
throughout. Neither is this review's call to schedule, but both remain
the honest, still-open state of the underlying physics question this
instrument exists to answer.
