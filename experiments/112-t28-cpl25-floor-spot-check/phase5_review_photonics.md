# Phase 5 Review — PHOTONICS (exp-112, Panel Iteration 89)

*Fresh sub-agent, blind context. Charter: surface interaction, absorption
spectra, angular dependence, scattering cross-sections — is the proposal's
optical response coherent as stated, across wavelength and angle? Have not
seen and did not seek out any other seat's Phase-5 output this cycle. All
numeric claims below are independently re-derived from `results.json`,
`experiments/110-.../results.json`, and the committed source
(`run112.py`, `chunk_runner112.py`, `analyze.py`, `lab/sections.py`) — not
taken on NOTES.md's own say-so.*

## Verdict: **CONFIRM-WITH-GAPS**

Every reported figure in NOTES.md's Result/Interpretation reproduces
exactly from primitives — nothing here is an R4-class fabrication or
hand-typed slip, and Check A's own AMBIGUOUS scored disposition (declining
"candidate real structure") is, on the numbers, the physically correct
call. But this seat's own charter question — is the optical-response
comparison this cycle stakes its verdict on actually *coherent* across the
two resolutions being compared? — surfaces two real, previously-uncaught
gaps, one of them load-bearing enough to undercut Check C's headline
number specifically: (1) Check C's near-unity correlation is not
diagnostic of anything specific to the named bin — the identical
construction clears its own bar at **every** bin in the pattern; (2) the
raw quantities Checks B and C actually compare (patterns, and the newly-
persisted energy ledger) carry an unexplained, near-exact **1.25×**
multiplicative discrepancy between `cpl=20` and `cpl=25` — precisely the
`CPL_RATIO` this cycle's own geometry recipe is built around — that
mechanically favors both checks reading "SURVIVES"-shaped regardless of
whether the −146.25° bin carries any real sub-wavelength signature at all.

## Findings (each independently re-derived from primitives)

### F1 — Every cited number reproduces exactly (R4 discipline, clean)

Re-read `experiments/110-.../results.json` directly for bin index 4
(`bin_centers_deg[4]=-146.25`, confirmed): `peccored=1.0869903329739812e-4`,
`hollow=1.1943830960599575e-4`, `delta=-1.0739276308597632e-05`,
`local_rel=9.87983%`, `floor=1.1261666277300464e-3`,
`local_snr_peccored=0.096521...`, `local_snr_hollow=0.106057...` — all
bit-exact to `phase1_proposal.md` §2.0 and NOTES.md's Setup. Re-read
`experiments/112-.../results.json`'s own `named_bin`:
`peccored=1.404528e-04`, `hollow=1.545771e-04`, `delta=-1.412430e-05`,
`local_snr_peccored=0.14442370182068412`,
`local_snr_hollow=0.15894731653238098`, `floor=0.0009725054913089504` — all
bit-exact to NOTES.md's Result block, and Check B's own "grew by 1.315×"
reproduces exactly (`1.412430e-5/1.073928e-5=1.31520`, same sign, both
negative). No R4-class defect anywhere in this document's own numeric
claims.

### F2 — Check C is not a sound test of "real structure vs. Yee-grid noise" **as constructed**: the identical construction clears its own bar everywhere in the pattern, not specially at the named bin

`neighbor_correlation_check` Pearson-correlates a ±2-bin window
(`[-4.855e-6,-4.530e-6,-1.074e-5,-9.599e-6,-2.270e-5]` at `cpl=20` vs.
`[-6.399e-6,-5.847e-6,-1.412e-5,-1.186e-5,-2.817e-5]` at `cpl=25`) and
reads `corr=0.9994` against a `≥0.5` bar. I ran the identical ±2-bin
windowed correlation at **all 48** possible window centers around the full
`pattern_delta` array (using `experiments/110-.../results.json`'s
`cpl=20` delta and `experiments/112-.../results.json`'s `cpl=25` delta,
the same two committed arrays the document's own Check C reads):

```
48/48 windows clear corr>=0.5
46/48 windows clear corr>=0.9
median corr = 0.9952,  min = 0.8169 (idx 35),  max = 0.9996 (idx 19/28)
```

Every single angular sector in this 48-bin pattern — including bins deep
in the dominant forward-scattering lobe, nowhere near the near-null
sector PHOTONICS' own exp-110 Phase-5 review flagged — clears Check C's
own `≥0.5` bar, and the overwhelming majority clear even a 0.9 bar. A
check that reads "supports real structure" at essentially every candidate
location in the search space has, at this threshold, no discriminating
power over the one hypothesis it exists to test (a genuine near-field
feature specific to −146.25° vs. generic Yee-grid behavior common to the
whole pattern) — this is the same "an affordable look-elsewhere/
null-calibration control was never run before a raw number was trusted"
shape this program's R5/R17 lineage names, applied here to a correlation
bar rather than a search match or a bracket width. The `≥0.5` bar was set
by Phase-2 critique/Red Team docket reasoning alone, never checked against
what this exact statistic reads at an "obviously uninteresting" bin —
data that was zero-marginal-cost to check (both full 48-bin arrays were
already committed) at the moment the bar was chosen.

### F3 — The mechanism: an unexplained, near-exact 1.25× (=`CPL_RATIO`) multiplicative discrepancy pervades every RAW quantity compared across `cpl=20`→`cpl=25`, not only the named bin's neighborhood

I checked whether F2's result has an identifiable cause rather than being
merely "the pattern happens to be smooth." Computing `pattern_peccored(cpl25)
/ pattern_peccored(cpl20)` and the hollow equivalent, bin-by-bin, across
all 48 bins:

```
ratio_peccored: mean=1.2490, median=1.2365, std=0.0330 (n=48)
ratio_hollow:   mean=1.2534, median=~1.24,  std=0.0353 (n=48)
full-48-bin correlation, peccored(cpl20) vs peccored(cpl25): 0.99963
full-48-bin correlation, hollow(cpl20)   vs hollow(cpl25):   0.99963
```

The SAME ratio appears, independently, in the newly-persisted (Fix 6)
`energy_ledger`, which nobody in this cycle compared against exp-110's own
committed `sigma_abs`/`sigma_ext` (110's own `reproduction_precondition`
block, `sigma_abs=279.66065695338267`, `sigma_ext=560.198850825502` at
`cpl=20`; PEC-cored config, held constant since it's the same shell in
both hollow and peccored):

```
sigma_scat(cpl25,peccored) / sigma_scat(cpl20) = 1.24964
sigma_abs (cpl25,peccored) / sigma_abs (cpl20) = 1.24986
sigma_ext (cpl25,peccored) / sigma_ext (cpl20) = 1.24975
```

`CPL_RATIO = 25/20 = 1.25` exactly. Three structurally different
quantities (a per-bin angular pattern value; an integrated scattering
cross-section; an integrated extinction cross-section), computed from
entirely independent FDTD field captures, all land within **0.03%** of the
exact `cpl` ratio — far tighter than any plausible physical near-field
convergence coincidence, and I traced the mechanism to source, not
numerology: `lab/sections.py::_face_flux()`'s own docstring states it
"Returns the total outward power (grid units)" — it sums `Re(E×H*)` over
Yee-index cells with **no physical cell-width (`dx`) normalization
anywhere in the function**. `geom_fixedabs_cpl`'s own congruent-refinement
recipe holds the box's PHYSICAL perimeter fixed (verified: `box_a` spans
440 cells at `cpl=20`, 550 cells at `cpl=25` — ratio 1.25 exact — over the
identical physical arc length, since `cpl` itself grew by the same
1.25×), so the SAME physical perimeter is now swept by 25% more grid
cells; summing an un-normalized per-cell flux term over 25% more cells
covering the same physical extent inflates every raw "grid-unit power"
reading by very nearly the cell-count ratio — independent of whether the
shell's own optical depth (`tau_shell`, correctly held invariant by both
the proposal and three independent Phase-2 re-derivations) or the named
bin's own physics changed at all. This is a **units/normalization
artifact in a shared, unmodified library function** (`lab/sections.py`),
not a defect introduced by this cycle's own geometry code, but this cycle
is the first in this sub-thread's history (to my knowledge from the
supplied record) to compare **raw**, non-ratio `sections.py` output
directly across two different `cpl` values — every prior T28 resolution
check I have context for compares a *ratio*-type quantity (`frac_contrast`,
`ratio_k`, ...) computed *within* one `cpl`, where a common multiplicative
factor like this would cancel and stay invisible.

### F4 — Consequence for Checks B and C specifically: both are dominated by F3's confound, not bin-specific physics

Pearson correlation is invariant under any per-vector positive affine
rescale — F3 alone (a near-uniform ~1.25× multiplier applied to both the
`cpl=20` and `cpl=25` delta windows) is close to sufficient, on its own,
to produce `corr≈1` regardless of any genuine local feature (confirmed:
replacing the real `cpl=25` window with `baseline_window * mean_ratio`
reproduces `corr=1.0` exactly). Check B ("same sign, within one order of
magnitude") is a comparably weak bar; that it reads SURVIVES here is
better explained by where the named bin sits relative to the pattern's own
zero-crossings than by anything specific to it: `pattern_delta(cpl=20)`
crosses zero near bin-pairs (0,1), 9, (14-19), (27-32), 37, and 46 — the
named bin's own ±2-bin window (indices 2-6) sits entirely inside one
single-signed region, comfortably clear of any crossing — while
`ratio_delta = delta(cpl25)/delta(cpl20)` computed across ALL 48 bins
shows wild instability elsewhere in the pattern (`std=1.53`, ranging from
`-6.82` to `1.75`, including outright sign flips) at bins nearer those
crossings. This is exactly this program's own R13/R14 lesson (a
subtractive-cancellation quantity is fragile near a zero, stable away from
one) — the named bin's neighborhood happening to sit in a numerically
well-behaved stretch of the curve is a property of *where on the curve it
sits*, not evidence about *what physically produces the ~9.9%/9.9%
deviation there*.

### F5 — Even Check A's own modest "improvement" is largely a composite of two generic effects, not bin-specific evidence

`local_snr` improved from `0.0965/0.1061` (cpl=20) to `0.1444/0.1589`
(cpl=25) — a ~1.50× rise — while the mirror-pooled floor itself *fell*
(`1.1262e-3 → 0.9725e-3`, ~0.86×), the opposite direction from F3's
pattern-wide 1.25× rise. `1.25/0.86 ≈ 1.45-1.50`, matching the observed
`local_snr` rise closely. This means the floor (a mirror-asymmetry
statistic, itself independently subject to the same R13/R14 subtractive-
cancellation fragility Check A's own sibling instrument already discloses
— it did not track F3's pattern-wide multiplier at all, in fact moving
opposite it) and the raw pattern's F3 confound largely explain Check A's
own modest rise without invoking any bin-specific physics. Both named
bins still sit ~6-7× below the K=1 bar regardless — the AMBIGUOUS
disposition is not threatened by this, but the *reason* for even the
partial improvement is generic, not a signal that the −146.25° feature is
becoming "more real" under refinement.

### F6 — NOTES.md's Interpretation reaches the right SCORED disposition but overstates Check C's evidentiary weight in its own prose

NOTES.md correctly declines "candidate real structure" (Check A never
reached SURVIVES, and the DISCLAIMER's own pre-registered gating is
honored exactly as written — no complaint here). But its own framing of
Check C's `corr=0.9994` as "a striking number for an independent grid
refinement to reproduce by chance" and "in real tension with Check A's
own AMBIGUOUS reading" does not survive F2/F3: it is not striking (median
window correlation across the WHOLE pattern is 0.995; every window
clears the bar), and there is no real tension to resolve, because Check C
was never capable of reading otherwise under this pattern's own
resolution-refinement behavior. This is not a scored-verdict error (the
document does not upgrade anything on this basis, matching its own
pre-registration), but it is a **prose overclaim about an instrument's
own diagnostic power**, of a piece with this program's own R5/R17
"uncalibrated-threshold" family, and it should be corrected in the
permanent record before a future citation lifts "0.9994, striking"
without this context (the exact R4/R9 "citation-shortening" failure mode
this program has paid for before).

### F7 — R29's second instance (Phase 4, `chunk_runner.py`): does not fire Checkpoint criterion 4 — same founding instance, not a fresh recurrence

Read R29's own ratified text (LOGBOOK RULED OUT registry) directly: the
forward-firing clause requires "a second instance of this exact collision
shape... **after this rule is on the books**." Checked element-by-element
against this cycle's own record (`NOTES.md` Phase 4; `analyze.py`'s own
comment block, lines ~34-50):

- Both collisions (`run.py`/`run.py`, caught Phase 2; `chunk_runner.py`/
  `chunk_runner.py`, caught Phase 4) were authored in the **same Phase-1
  drafting sitting**, before R29 existed even as an idea — R29 was
  proposed by Red Team's Phase-2 audit *in response to* discovering the
  first collision. The second collision cannot be "a future cycle reusing
  an idiom after the rule is on the books," because it predates the
  rule's own conception by exactly as much as the first one does — they
  are two symptoms of one authoring-time mistake (the `import X as A;
  import X as B` idiom applied twice in one sitting), not two temporally
  separated failures to learn a lesson.
- Phase 2's blind critiques never reached the second collision because
  execution crashed on the first one first (`chunk_runner.py`'s own
  `AttributeError` on its first `R.` attribute access, before ever
  reaching `analyze.py`'s own `import chunk_runner as CR` line) — this is
  a **detection-ordering artifact**, not evidence the second collision
  survived a review layer that could have caught it.
- Every rule in this registry (R5 through R28, unbroken, checked against
  the actual ratified texts for R16/R21/R23/R24/R26 above) grants "does
  not fire on its own founding instance" at **cycle granularity** — one
  experimental cycle (`exp-NNN`) is one instance, regardless of how many
  discrete manifestations of the identical defect shape that one cycle's
  own document/code contains (R23's own founding cycle, exp-104, already
  set this precedent: at least three separate disclaimer-completeness
  gaps inside ONE document counted as one founding instance, not three).
  Applying that same convention here, exp-112 is one founding instance of
  the R29 shape, entitled to the same immunity every prior rule extends
  to its own founding cycle.
- The defect was caught, disclosed, and fixed in the SAME governance
  cycle, before Phase 5, before any external citation ever treated
  Fix 1 as "closed" on the strength of the first fix alone — matching the
  program's own repeated "caught blind, same cycle, before LOGBOOK" non-
  firing rationale (R16, R18, R19, R20's own precedent).

**My own view: this is the same founding instance's own second,
previously-undiscovered manifestation — Checkpoint criterion 4 does NOT
fire.** Recommend the LOGBOOK's own R29 entry be updated (a small, purely
narrative correction, zero re-run) to name BOTH collisions in its founding-
instance text, so a future reader does not encounter an R29 citation that
describes only half of what actually happened this cycle.

## Ranked next-step recommendations for Iteration 90

1. **Diagnose and either normalize or explicitly bound F3's ~1.25×
   raw-magnitude discrepancy in `lab/sections.py` before any future
   cross-`cpl` comparison of RAW (non-ratio) `sigma_*`/pattern quantities
   is trusted.** Zero new FDTD — this is a desk check against already-
   committed data (confirm whether dividing `_face_flux`'s own per-cell
   sum by a physical `dx`-per-cell factor, or equivalently by `cpl`,
   restores near-invariance of `sigma_abs`/`sigma_ext` across `cpl=20`→
   `25`). This is the single highest-value item on this queue: until it
   is resolved, EVERY raw-value cross-`cpl` comparison this sub-thread
   might attempt in the future (not only this cycle's) inherits the same
   silent confound, and it directly undercuts Checks B/C's own
   evidentiary basis in this cycle specifically.
2. **Recalibrate or replace Check C's fixed `corr≥0.5` bar with a
   null/look-elsewhere-informed threshold**, using exactly the all-48-
   window control computed in F2 above (already run, zero marginal cost,
   reusable directly) — e.g., score a window's correlation as a
   percentile/z-score against this cycle's own 48-window empirical
   distribution (median 0.9952) rather than an absolute value, so a
   future SURVIVES-plus-Check-C reading means "unusually well-correlated
   for THIS pattern," not "correlated at all."
3. **Once (1) is resolved, re-run Checks B/C's own arithmetic against the
   already-captured `cpl=25` data with properly normalized quantities** —
   zero new FDTD, a pure reanalysis — to see whether Check B's SURVIVES
   and Check C's high correlation persist once the shared multiplicative
   confound is removed; this is the honest way to learn whether ANY
   residual bin-specific signal remains at −146.25°, which the current
   readings cannot distinguish from F3's artifact.
4. **A genuinely third, differently-scaled resolution point (`cpl=30`,
   already costed in `cpl_cost_table.py`)** remains the right move for
   R15-disciplined continuum-convergence purposes, but only *after*
   items 1-3 — a third raw-value data point added on top of an
   uncalibrated, confound-carrying comparison would not distinguish
   genuine convergence from the same F3 artifact simply repeating at a
   third `cpl`.
5. Update LOGBOOK's own R29 entry per F7, above (narrative-only, zero
   re-run).
