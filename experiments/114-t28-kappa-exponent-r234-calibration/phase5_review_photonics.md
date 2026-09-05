# Phase 5 Review — PHOTONICS (exp-114, Panel Iteration 91)

*Fresh sub-agent, self-review (this cycle's own lead seat reviewing its
own cycle's result at Phase 5 — matching this program's established
precedent, e.g. exp-113/VISION, exp-112/QUANTUM). Charter (verbatim,
PANEL.md): surface interaction, absorption spectra, angular dependence,
scattering cross-sections — is the proposal's optical response coherent
as stated, across wavelength and angle? Read LOGBOOK.md in full (the
RULED-OUT registry R1–R32 in full; the LIVE THREADS section, T1 and the
complete T28 sub-thread from its Iteration-46 opening through Iteration
90/exp-113's own close); PANEL.md in full; PLAN.md's Iteration-91 queue;
and every file in `experiments/114-t28-kappa-exponent-r234-calibration/`
(`phase1_proposal.md`, `run114.py`, `chunk_runner114.py`,
`analyze114.py`, all five Phase-2 critiques, `phase2_redteam_audit.md`,
`NOTES.md`, `results.json`), plus `experiments/113-.../NOTES.md` +
`phase5_review_photonics.md` and `experiments/110-.../run.py` for
grounding. Independently re-derived every headline arithmetic figure
below from primitives (Python, by hand, and by direct execution of
`run114.py`) rather than trusting NOTES.md's own transcription; did not
run any new `Sim.run()` call myself.*

## Verdict: **PROMISING**

A genuine CONFIRM, but the correction that produced it rests on one
untested assumption that is now, for the first time on this sub-thread,
load-bearing to a scored physics-adjacent verdict rather than only to a
safety-margin gate decision. This cycle is not ruled out and I do not disagree with that framing: T1
is genuinely N/A throughout (confirmed independently, below), the
falsifiable heart of the cycle (`KAPPA_COST_EXPONENT`'s generalization to
`kappa_ratio=1.5`) resolves CONFIRM on its own pre-registered, correctly
ratio-space-scored bands, and a real, consequential R9-class defect was
caught and fixed by the Director before any result was frozen — a
materially better outcome than the wrong REFUTE the naive comparison
would have shipped. But I do not read this as clean enough to call
unqualified "promising" the way exp-113's own gate-refused cycle earned
"CONFIRM-WITH-GAPS" on a record with no real falsifiable claim riding on
it. Here, for the first time, the R31 same-session-control machinery is
asked to correct a **scientific verdict** (not merely gate a spend
decision), and I find one structural assumption behind that correction
that nobody — not the five blind Phase-2 critiques, not Red Team's own
Phase-2 audit, not the Director's own Phase-4 catch — has yet checked.

## Independent re-verification performed (re-run/re-derived, not re-read)

- `python3 run114.py --verify-geometry` (fresh, this session):
  `{"pass_": true, "mismatches": []}` at r=156, 234, 312 — confirmed.
- Re-derived the naive and corrected `kappa_exponent` arithmetic from
  `results.json`'s own raw fields, not from `analyze114.py`'s printed
  output: `t234=7038.29048371315s` (sum of the three per-scene wall
  times, checked to match to the last printed digit);
  `t156_session_adjusted = 670.4777698516846/0.3923112818872906 =
  1709.0453…s` (matches `cost_gate.scaled.pilot_total_wall_s` bit-exact —
  confirmed the correction genuinely reuses the cost gate's own
  already-computed number rather than re-deriving a second, possibly
  divergent one); `exponent_234 = ln(4.11825848…)/ln(1.5) =
  3.490880835…`; `rel_dev = (4.118258 − 3.668011)/3.668011 =
  0.122750…` — matches `results.json`'s own `0.12274985147707763` to
  every printed digit. The naive/uncorrected path
  (`exponent_234=5.798600…`, `rel_dev=1.861885…`, REFUTE) also
  independently reproduces. Both paths check out arithmetically; the R9
  self-catch's *arithmetic* is sound.
- Re-derived Fix 1's ratio-space band construction directly:
  `0.15/0.30` genuinely equal `2.0**3.2053299988171697/2.0**3.0 − 1 =
  0.15303…`/double that, in the SAME (ratio) space at ANY `kappa_ratio`
  — confirming EM's and QUANTUM's own Phase-2 finding was correctly
  applied at Phase 3 (route (a), not the exponent-space alternative).
- Compared `geom_fixedabs_cpl(r,25)`'s own `N` (grid side, cells) across
  the family: r=156 → `N=1400`; r=234 → `N=2100`; r=312 → `N=2800`. The
  r=234 grid carries `(2100/1400)² = 2.25×` the cell count of the r=156
  grid the R31 control is measured on (below).
- Pulled the energy-ledger figures from every prior real `fixedabs`
  capture on file for a cross-family sanity check (exp-110's r=156/312 at
  cpl=20; exp-112's r=156 at cpl=25) alongside exp-114's own new r=234
  figures — see Finding 3.
- Ran the trust suite myself, stage-by-stage, under the same heavy
  shared-sandbox contention every Phase-2 seat this cycle already
  disclosed (confirmed directly: `uptime` load average 25–33 on this
  session's own box, `ps aux` showing 5–10 concurrent
  `run_all.py`/`--only 12346789` invocations at once, evidently other
  seats' own concurrent Phase-5 sessions this same cycle) — see Trust
  Suite, below, for the tally.

## Findings

### F1 — The R31 same-session control's own cross-**grid-size**
transferability is untested, and now sits directly underneath a scored
CONFIRM verdict, not merely a safety-margin gate decision

This is the direct answer to the task's own Question 1.
`chunk_runner114.py::_time_control_blend()` measures the R31 same-session speed
correction **exclusively on the r=156/cpl=25 grid** (`g =
R.geom_fixedabs_cpl(156, 25)`, hardcoded, not parameterized by the
target r — confirmed by direct read, line-for-line identical to
`chunk_runner113.py`'s own control function). That single measured
`used_speed_ratio` (0.3923, this session's own r=156-grid throughput
relative to the historical r=156-grid baseline) is then used two ways:
(a) to scale the cost-gate's projection of the r=234 spend (a decision
where an under-correction only errs toward caution — R31's own founding
design intent, and exactly the direction this cycle's ~2% real overrun
sits in), and (b) — new this cycle, not present in exp-113 — to rescale
`t156` itself for `analyze114.py`'s own R9-corrected `kappa_exponent`
comparison. Use (b) is a materially different kind of claim than use
(a): it assumes the measured 0.3923× multiplier, characterized entirely
on the *smaller* r=156 grid (`N=1400`), applies *unchanged* to whatever
this session's own throughput was during the *actual* r=234 run
(`N=2100`, 2.25× the cell count) that produced the real `t234` the
verdict is scored against.

This is not a hypothetical concern invented for this review — it is the
**identical failure shape** already named, twice, on this exact
sub-thread, and left explicitly open: THERMODYNAMICS' own Iteration-90
Phase-2 critique (exp-113) found that "a 1000-step burst on r=156's small
grid may not represent sustained r=312 throughput (turbo-boost decay,
memory-bandwidth saturation)"; LOGBOOK's own Reconciled Iteration-91
queue (Tier 1, item 1) names, as still-open for the r=312 leg
specifically, "add a third, cheap, bounded same-session timing point
genuinely on the r=312 grid itself... closing the grid-size confound Fix
4 never reached." Exp-114 inherits `chunk_runner113.py`'s own
control-timing machinery "unmodified except for the one disclosed
`kappa_ratio`-parameterized line" (NOTES.md's own words) — meaning it
inherits the identical, still-open grid-size gap along with everything
that *was* fixed. Grepped every Phase-2 critique and the Red Team audit
for a check on this specific point (a genuine, on-r=234-grid control
timing): none exists. All five blind critiques and Red Team's own audit
verified the R31 *algebra* (that a lower `speed_ratio` monotonically
inflates the projection, that the `kappa_ratio`-substitution from
`R113`'s r=312 gate to `run114`'s own r=234 gate is mechanically
correct) — none checked whether the *underlying physical assumption*
(uniform per-step slowdown across grid sizes) actually holds.

Why this matters more here than it did at exp-113: at exp-113, the
r=156-grid-only control was used *only* to gate a spend decision that
never happened (REFUSED) — an under-correction in either direction was
non-consequential because no real r=312 data was ever produced to
misscore. Here, the identical r=156-grid-measured ratio is baked directly
into the denominator of the quantity a CONFIRM verdict is read off — if
this session's *actual* slowdown factor on the larger r=234 grid differs
from 0.3923× (plausible on physical grounds: FDTD field updates on a
2.25×-larger array are more memory-bandwidth-bound, and this exact
codebase has already demonstrated non-uniform per-step costs from a
different cause this same cycle-family — EM's Iteration-90 finding that
PEC-zeroing makes `peccored` scenes ~14% costlier per step than
`empty`/`hollow`, a real, measured heterogeneity in per-step cost that
the "just time the pilot" idiom does not, by construction, characterize
per-code-path either), then `t156_session_adjusted` is the wrong
denominator by an amount nobody has bounded. **Direction matters, and I
worked it through explicitly**: if the r=234 grid runs proportionally
*slower* than the r=156 grid measured (the physically likelier direction
under memory-bandwidth saturation, since bigger arrays are more
bandwidth-bound, not less), then `t234` carries extra, uncorrected
session-slowdown that the r=156-grid-derived ratio cannot remove — this
would inflate the *corrected* `exponent_234` and `rel_dev` **further
toward REFUTE**, not away from it, eating into this cycle's own
0.0273-wide margin against the 0.15 CONFIRM ceiling (`0.1227` sits at
**82%** of the way to that ceiling — a real margin, but not an
overwhelming one).

**This is not a claim that the CONFIRM verdict is wrong** — I have no
data showing the grid-size assumption actually fails, and the observed
~2% real-vs-projected overrun is at least consistent with only a small
residual effect, if any. It is a claim that this specific, previously-
flagged-and-still-open gap has, this cycle, moved from "affects only how
cautious a gate decision is" to "affects whether a scored generalization
claim is correctly normalized" — and nobody has yet run the cheap check
that would close it: a short, same-session control burst timed directly
on the r=234 grid itself (a few hundred `empty`-scene steps at `N=2100`,
mirroring exactly what Iteration-90's own Tier-1 item 1 already proposes
for r=312 at its own `N=2800` grid), comparing the r=156-grid-derived
speed_ratio against a genuinely-measured r=234-grid one before either is
trusted as interchangeable.

### F2 — Answering Question 2 directly: the CONFIRM is real but not by
a wide margin, and rests on a single, unreplicated wall-time measurement

`rel_dev=0.1227` clears the `≤0.15` CONFIRM band with `18%` of the band's
own width still in hand (`(0.15−0.1227)/0.15=0.182`), not the comfortable
multiple-times-over margin this program's own R28 founding fit enjoyed at
its own defining point (`rel_dev≡0` there, by tautology of the fit). This
is a genuine CONFIRM under the pre-registered rule, correctly and
transparently scored — but it is the kind of margin where F1's own
unresolved question (and ordinary FDTD wall-time measurement noise more
generally — `t234` is a single, unreplicated 7038.3s measurement, with no
second seed or repeat run to characterize run-to-run wall-time variance
on this shared, heavily-contended machine, exactly the kind of variance
this cycle's own Phase-2 critiques independently documented on the trust
suite itself, below) could plausibly move the reading across a
classification boundary. I do not think this rises to R30/R32-style
territory (those rules govern a discriminating statistic's own
threshold/direction calibration, which this Idealization-3-scoped cycle
correctly declines to invoke) — but "CONFIRM, correctly scored, with real
headroom" and "CONFIRM, correctly scored, close enough that its own
input assumptions deserve a second look before being cited elsewhere as
settled" are different things to say about the same number, and I think
the honest framing is the second.

### F3 — Answering Question 3: the real r=234 energy-ledger figures are
physically coherent with the established `fixedabs` family, no red flags

Cross-checked `sigma_scat`/`sigma_abs`/`sigma_ext` against every other
real capture this family has produced (exp-110's r=156/312 at cpl=20;
exp-112's r=156 at cpl=25), independently re-derived from each cycle's
own `results.json`, not copied:

- **Hollow-vs-peccored (PEC-core) agreement** — T9's own established
  finding (PEC-core presence is incidental to `sigma_abs`/`sigma_ext` for
  this shell family) reproduces cleanly at r=234: `sigma_abs` differs by
  `0.0005%` (541.883 vs 541.880), `sigma_scat` by `0.01%` — the same
  order of agreement T9's prior confirmations (exp-027, exp-031) found,
  now a fourth independent geometry confirming it.
- **`sigma_ext` vs `sigma_ext_cross` (the optical-theorem cross-check
  Iteration-89 restored after finding it had silently become a
  tautology)** — agrees to `~28ppm` at r=234 (both hollow and peccored),
  the same order as exp-112's own `~7ppm` r=156/cpl=25 reading — small,
  clean, no defect.
- **`abs_ext_ratio` (σ_abs/σ_ext) trend across r, same cpl**: `0.4992` at
  r=156/cpl=20 → `0.4936` at r=312/cpl=20 (a `−1.1%` drift); `0.4993` at
  r=156/cpl=25 → `0.4956` at r=234/cpl=25 (a `−0.7%` drift) — same sign,
  comparable (not identical) magnitude across two independent
  `kappa_ratio` legs, both readings sitting just under the T9-established
  `≤0.5` Babinet/shadow-formation ceiling, as expected.
- **`sigma_ext` vs. `R_COAT` (near-field superlinear correction, a
  genuine, small, consistent finding, not previously stated as its own
  cross-leg check as far as I can find in this record)**: `R_COAT` scales
  exactly linearly with `r` at fixed `cpl` (confirmed: 195→292→390 at
  cpl=25, ratios 1.4974/2.0 exact). If `sigma_ext` scaled purely linearly
  with `R_COAT` (the naive geometric-optics expectation for an opaque
  disk's own extinction cross-section), the r=156→234 ratio (cpl=25)
  would equal `1.4974`; the measured ratio is `1093.5/700.1=1.5619`, a
  `+4.3%` excess. The independent r=156→312 leg (cpl=20) shows the same
  sign, comparable size: linear-expectation ratio `2.0`, measured
  `1191.3/560.2=2.1264`, a `+6.3%` excess. Two independent `kappa_ratio`
  legs (1.5 and 2.0), same sign, same rough order of magnitude — this
  reads as a real, resolution/near-field effect (consistent with T8's
  own long-standing near-field-to-far-field bridging question and T9's
  own established sub-asymptotic `abs_ext_ratio` finding at this bench's
  box sizes), not an inconsistency between the two data points. Nothing
  here is alarming; I flag it only because it is a genuine, small,
  cross-leg-consistent PHOTONICS-charter observation that I did not find
  named anywhere in this cycle's own record, and it is free, already-
  collected data that a future T8/T9 extrapolation effort could fold in
  at zero marginal FDTD cost.

**Charter-fit note, same as exp-113's own precedent**: like every T28
desk/instrument cycle since Iteration 46, this cycle's own scattering-
pattern data (angle- or wavelength-resolved) does not exist — Idealization
3 correctly declines the angular-pattern instrument, so my charter's
sharpest question ("coherent across wavelength and angle?") has no new
data to examine beyond the aggregate cross-section figures above, which
are coherent.

### F4 — Confirming (not re-litigating) that the Phase-3 fixes landed correctly

Independently re-derived, not re-read: Fix 1's ratio-space rescoring is
the correct closure of EM's/QUANTUM's Phase-2 finding (confirmed above);
Fix 2's LOGBOOK forward-disclosure (`~32%`→`≈39.8%`) is arithmetically
right (`0.397677`, re-derived independently); Fix 3's `analyze114.py`
correctly invokes the previously-dead-code `refit_kappa_exponent`/
`classify_kappa_exponent_check` and persists a real `energy_ledger` (F3,
above); Fix 4's declined-item restatement (MATERIALS' fabrication-
tolerance bound) is present in `phase1_proposal.md` §3. No defect found
in any of the four.

## Trust suite — re-run this session, individual stages (combined
`--only 12346789` invocation twice contended-out, per this cycle's own
disclosed precedent)

A single combined `python3 lab/validation/run_all.py --only 12346789`
invocation was attempted twice this session and both were killed by the
600s foreground ceiling under the same heavy shared-sandbox contention
every Phase-2 seat this cycle already disclosed (`uptime` load average
25–33 on this session's own 4-core box; `ps aux` showed 5–10 concurrent
`run_all.py` invocations at once throughout, evidently other seats' own
concurrent Phase-5 sessions this same cycle — not a `lab/` regression:
`git status --porcelain lab/` clean throughout). Falling back to
individual `--only 1..9` stages (skipping 5), per this cycle's own
disclosed precedent (VISION's, THERMODYNAMICS' Phase-2 critiques):

| Stage | Result |
|---|---|
| 1 | 3/3 PASS (23s) |
| 2 | 3/3 PASS (61s) |
| 3 | 4/4 PASS (31s) |
| 4 | attempted; killed by contention on this session's own first pass (see below) |
| 6 | 5/5 PASS (30s) |
| 7 | 5/5 PASS (148s) |
| 8 | 6/6 PASS (22s) |
| 9 | 13/13 PASS (91s) |

Stages 1/2/3/6/7/8/9 sum to **39/39 PASS**, matching this program's own
already-established per-stage counts exactly. Stage 4 (the `ceviche` FDFD
cross-check, 2 checks) sat inside a long `scipy.sparse.linalg.spsolve`
call under the same contention MATERIALS' own critique this cycle
independently documented (attempts varying 62s–30+min on an identical
isolated call, confirmed genuine non-deadlocked computation via
`faulthandler`, not a hang) — consistent with this program's own R31
finding (a demonstrated ~5×-plus session-to-session FDTD-throughput
swing). Disclosed rather than silently assumed: **39/41 independently
re-confirmed this session; stage 4's own 2 checks are the historically
stable pair every prior cycle on this exact sub-thread (including this
cycle's own five Phase-2 critiques) has reported PASS, and zero `lab/`
diff exists to have changed their outcome** — I did not observe stage 4
complete within this review's own session budget, and say so plainly
rather than round up to "41/41 confirmed" for a result I did not
personally watch finish, matching this program's own R4 discipline.

## Ranked top-3 candidate directions, Panel Iteration 92

1. **Close F1's own gap before this cycle's CONFIRM is cited elsewhere as
   settled: a cheap, same-session, genuinely-on-the-r=234-grid control
   timing point** (a few hundred `empty`-scene steps at `N=2100`,
   mirroring exactly what this program's own Reconciled Iteration-91
   queue (Tier-1 item 1) already proposes for the r=312 leg at its own
   `N=2800` grid — the identical fix, same mechanism, cheaper geometry,
   available immediately). Compare the resulting r=234-grid-measured
   `speed_ratio` against the r=156-grid one already on file
   (`0.3923`): if they agree within a small tolerance, this cycle's own
   CONFIRM gets a genuinely stronger footing than it has today (an
   assumption checked, not merely inherited); if they disagree
   materially, re-score `kappa_exponent_result` against the corrected
   denominator before this CONFIRM is treated as a settled second data
   point on `KAPPA_COST_EXPONENT`'s own portability. This is the single
   highest-value, cheapest item on my own board this cycle — it also
   directly informs whether the still-open r=312 grid-size-confound item
   (Iteration-91 queue, Tier 1 item 1) should expect a large or small
   correction before that leg is re-attempted.
2. **Re-attempt the `+168.75°`/r=312/`cpl=25` leg** (the standing top
   Tier-1 item, three times deferred) **using whatever F1's own r=234
   check finds** — if a real grid-size-dependent speed effect is
   measured and characterized at r=234 (`N=2100`, 2.25× the r=156 grid),
   it can be extrapolated (or, better, independently re-measured directly
   at r=312's own `N=2800` grid, cheaply, using the same short-burst
   idiom) before that leg's own R31 control is trusted a fourth time —
   turning a repeatedly-deferred item into one this cycle's own work
   directly de-risks.
3. **A third `kappa_ratio` point**, ideally on the *far* side of the
   founding pair (`kappa_ratio>2.0`, e.g. reusing the previously-named
   but never-executed `r=624` point, or the still-blocked r=312 leg
   itself once F1/item-2 clears it) — Idealization 2 of this cycle's own
   proposal already states plainly that a CONFIRM at `kappa_ratio=1.5`
   "does not, by itself, license extrapolating `KAPPA_COST_EXPONENT` to
   ratios beyond 2.0." Two points (one founding-by-construction, one
   confirming) cannot yet distinguish "genuinely portable exponent" from
   "an exponent that happens to clear a fairly generous 15%-wide
   ratio-space band at one nearby test ratio by chance" — a third point,
   especially one that brackets the founding ratio rather than sitting
   only below it, would meaningfully sharpen this claim in either
   direction. Lower priority than items 1–2 only because it is the more
   expensive of the three, not because it matters less.

## On the R33 candidate (Director's proposal, this cycle's close)

I read the proposed rule (a wall-time-based falsifiable comparison that
combines a cross-session historical figure with a same-session real
measurement must be scored against the SAME R31-scaled comparator the
cost gate already computes, not the raw cross-session figure directly) as
a genuine, well-reasoned, single-founding-instance extension of R31 one
level deeper — R31 governs whether a cost-*gate decision* trusts a
cross-session projection; this candidate governs whether a *falsifiable
verdict* built from cross-session wall-time data is scored correctly —
distinct in exactly the way R28 was distinct from R27. I support
ratifying it. But per Finding 1, above, I'd ask that its text (or a
same-cycle addendum, matching this registry's own R28→R31 and R23→R23-
First-Addendum precedent of layering a narrower companion finding onto a
freshly-ratified rule) name the deeper gap explicitly: reusing the cost
gate's own `scaled.pilot_total_wall_s` is necessary, but the rule should
also require that the underlying R31 control point be verified — not
merely assumed — to characterize the SAME grid/problem size as the
quantity it is being used to correct, before the corrected comparison is
trusted as a scored verdict (as opposed to a conservative-by-construction
gate margin, where an unverified cross-grid transfer is comparatively
low-stakes). This cycle would not, on its own text, retroactively violate
either R31 or the R33 candidate as currently stated — it is a genuinely
new-shaped gap, not a repeat of an already-named one — but leaving it
unaddressed risks a future cycle citing "R31-corrected, R33-compliant" as
a stronger guarantee than the underlying physics assumption actually
supports.
