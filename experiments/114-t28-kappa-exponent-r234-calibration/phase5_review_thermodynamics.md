# Phase 5 review — THERMODYNAMICS (blind, fresh context)

Fresh sub-agent, this seat only, Panel Iteration 91 (exp-114). Read
`LOGBOOK.md` in full (RULED OUT R1–R32; LIVE THREADS T1, T5, T22, T23,
and T28's complete history, Iteration 46 → Iteration 90); `PANEL.md` in
full; `PLAN.md`'s tail (Reconciled Iteration-91 queue); every file in
`experiments/114-t28-kappa-exponent-r234-calibration/` (`phase1_proposal.md`,
`run114.py`, `chunk_runner114.py`, `analyze114.py`, all five Phase-2
critiques, `phase2_redteam_audit.md`, `NOTES.md`, `results.json`); and, for
grounding, `experiments/113-.../analyze113.py` and
`experiments/112-t28-cpl25-floor-spot-check/analyze.py` (the
`energy_ledger` pattern `analyze114.py` mirrors) plus
`experiments/107-t28-delta-scene-r5-census-decision/run.py` (the fixedabs
family's own existing thermal-sidecar invocation, `item3_thermal_row()`).
Every number below was independently recomputed by importing the real
committed code or reading `results.json` directly — not taken from any
document's prose.

## 1. Did my own Fix 3 land correctly and completely?

**Yes — verified directly, not by re-reading the Panel record's own claim.**

- `analyze114.py::analyze_r234_cpl25()` calls `sc.widths(cap_p, cap_e,
  box_a, ref)` and `sc.widths(cap_h, cap_e, box_a, ref)` (lines 78–79) —
  `sc.widths()` genuinely invoked on the real r=234 captures, not a
  placeholder.
- The four fields I asked for are all persisted, per scene, under
  `energy_ledger` — confirmed by reading `results.json` directly:
  `energy_ledger.peccored = {sigma_scat: 551.5854, sigma_abs: 541.8829,
  sigma_ext: 1093.4683, sigma_ext_cross: 1093.4987}`,
  `energy_ledger.hollow = {sigma_scat: 551.6454, sigma_abs: 541.8798,
  sigma_ext: 1093.5252, sigma_ext_cross: 1093.5556}` — real floating-point
  values with the full precision an actual `sc.widths()` call produces,
  not round numbers or a stub. `sigma_ext_cross` — the genuinely
  independent optical-theorem cross-check EM's Iteration-89 review found
  silently dropped from exp-112's own ledger — is present here and agrees
  with `sigma_ext` to 2.78×10⁻⁵ relative (both peccored and hollow,
  independently recomputed by me — my own first-pass mental estimate of
  "3.2×10⁻⁵/2.8×10⁻⁵" was itself slightly off; corrected here before
  filing), i.e. this cycle did not repeat that specific regression.
- The R23-style `DISCLAIMER` asserts are present (`analyze114.py` lines
  151, 163, 191, 212 — `assert R.DISCLAIMER in predictions_text` /
  `result_text`, both in the real-data branch and the gate-refused
  branch) and **genuinely fired on real execution, not merely present in
  source**: I confirmed this by reading `results.json["predictions_text"]`
  and `["result_text"]` directly — both strings are populated (5557
  characters for `result_text`) and both open with the disclaimer
  sentence ("This is an instrument-calibration/cost-gate cycle — not a
  phenomenon-mechanism proposal..."). Had either assert failed, no
  `results.json` would exist at all (they run before the `json.dump`),
  so the file's own existence with this content is itself proof the
  asserts passed on real data, matching this family's own established
  live-fire standard (exp-112's VISION finding; exp-113's own
  re-confirmation).

I also independently re-ran `python3 analyze114.py` myself, fresh, against
the real committed checkpoint pickles in `chunk_runner114.py::SCRATCH`
(not merely reading the already-written `results.json`) — it reproduces
every field above bit-exact, confirming the persisted numbers are
genuinely reproducible from committed code plus the real captured data,
not hand-edited.

**My own Fix 3 landed correctly and completely.** One thing worth naming
for the record, not a defect: my own Phase-2 critique asked only for the
energy-ledger persistence half of the gap I found; Red Team's audit
broadened Fix 3 to also require wiring `refit_kappa_exponent()`/
`classify_kappa_exponent_check()` into committed code (they were dead
code through Phase 2) and the R23 asserts for this cycle's own new
`DISCLAIMER` string. All three sub-parts are present in the single
`analyze114.py` the Director authored — I checked all three, not only
the one I originally flagged.

## 2. The energy sidecar — is a full run owed this cycle, or correctly exempt?

**Correctly exempt this cycle, by explicit scope and by this program's own
established precedent — but a physical source-power normalization DOES
already exist in this family, contrary to the possibility the brief
asked me to check for, and a real, cheap extension is now available.**

First, the check the brief asked for: does a physical source-power
normalization already exist anywhere in the `fixedabs` family, that a
future full sidecar run could reuse? **Yes.** `experiments/107-.../run.py::
item3_thermal_row()` (Iteration 84) already computed a real,
non-placeholder P5 thermal row for **both** families (`selfsim` and
`fixedabs`) at r=156/312, using `lab/thermo_sidecar.py::
mixed_length_scale_regime()`. The witness-scale intensity anchor,
`i_incident`, is derived once from the r=78 bench anchor
(`SIGMA_EXT_78=240.007`, `P_ABS_78=1.741×10⁻¹²`, `RATIO_ABS_EXT_78=0.51`
— this program's docket-#7 witness-irradiance sourcing, exp-043/T5) and
held fixed across every `r` — it is the *source's own* intensity, not a
per-geometry fit, so it is exactly as valid to reuse at r=234 as it was
at r=156/312. I re-ran this exact recipe myself against exp-114's own
persisted `energy_ledger` (r=234, cpl=25) — a genuine, if informational,
post-run analytic calculation, per my own expressibility contract, not
an FDTD output. **My own first attempt at this desk check itself
committed the exact class of error this section goes on to warn about,
caught and corrected before reporting it here (an R9 self-catch, not
silently smoothed over)**: `experiments/107-.../run.py::DX_M=30e-9` is
the physical cell size at **`cpl=20`** (600nm design λ / 20); feeding
that same constant into `width_m = sigma_ext(cells) · DX_M` against a
`sigma_ext` measured at **`cpl=25`** (this cycle's own ledger) is exactly
the commensurability slip named below, one level more concrete than the
abstract warning — the correct cell size at `cpl=25` is `600nm/25=24nm`,
not `30nm`. Both readings, disclosed side by side:

```
i_incident = 6.5844e-6 W/cm²  (unchanged, reused from r=78)
r=234, peccored, sigma_ext=1093.468, abs_ext_ratio=0.4956:
  using WRONG cpl=20 dx (30nm, my own first-pass slip): margin=104.1x
  using CORRECT cpl=25 dx (24nm):                       margin=130.1x
r=234, hollow, sigma_ext=1093.525, abs_ext_ratio=0.4955:
  using WRONG cpl=20 dx:   margin=104.1x
  using CORRECT cpl=25 dx: margin=130.1x
(both -> UNDETECTABLE either way, vs NETD_BAND_K[0]=0.020K; the
correction moves the margin ~25%, not the classification)
```

So the honest answer to "does exp-114 need to run this itself": **no.**
Three independent reasons converge: (a) this cycle's own scope, stated
explicitly in `phase1_proposal.md` §4 and reconfirmed by every seat at
Phase 2 including my own prior incarnation, is T1 N/A — no
phenomenon-mechanism content, no constraint-1/2/3/4 verdict scored
anywhere; the sidecar's own charter purpose (per-*proposal* absorbed
power → ΔT → emission band → detectability) has no proposal to attach
to here. (b) It was never named as a Reconciled Iteration-91 queue item
— unlike exp-105/107, where the P5 thermal row was an explicit, numbered
Tier-1 deliverable, no seat's own Phase-2 critique or Red Team's own
mandatory-fix docket asked for it this cycle, and inventing a new
obligation at Phase 5 that nobody scoped at Phase 1–3 would itself be
the kind of scope-creep this program's own Idealization/DISCLAIMER
convention exists to prevent. (c) It matches this exact T28
instrument-calibration sub-thread's own unbroken precedent: every cycle
since Iteration 82 that persisted energy-ledger data without a named P5
item (exp-108 through exp-113) correctly registered zero
`thermo_sidecar.py` calls at Phase 5, and none of those non-invocations
were ever treated as a gap.

**But now that real r=234 `sigma_abs`/`sigma_ext` data is on file, the
extension is genuinely cheap** (zero marginal FDTD cost, ~10 lines,
reusing `item3_thermal_row()`'s own recipe verbatim) **— with a SECOND,
deeper commensurability gap my own dx correction above does NOT fix, and
a naive Iteration-92 attempt must not skip**: exp-107's own r=156/312
figures were computed from **`cpl=20`** ledgers (`EXP106_RESULTS`), while
my own r=234 figure (130.1×, dx-corrected) uses this cycle's own
**`cpl=25`** ledger. This program's own Iteration-89 finding (R30's
founding instance, exp-112, PHOTONICS) established that
`lab/sections.py::_face_flux()`-derived quantities themselves — `sigma_ext`,
`sigma_abs`, etc. — carry a raw, un-normalized `CPL_RATIO`(=1.25×)
magnitude artifact between `cpl=20` and `cpl=25`, **upstream of any
dx-per-cell conversion**, and **not** resolution-invariant the way
`tau_shell`/`sigma_max` provably are. My own dx-corrected r=234 margin
figure (130.1×) is therefore **still not yet a clean third point on
exp-107's own r=156(262.4×)/r=312(117.5×) trend** — comparing them
naively would repeat, on a different quantity, the exact class of
operand-commensurability error (R9) this cycle's own Phase-4 already
caught once (on `t156` vs `t234`) and my own dx slip just repeated a
second time in this very review before I caught it. Flagged here as a
genuine open item, not resolved by this review (see Iteration-92
ranking, below).

## 3. Sanity-check: peccored vs. hollow sigma_abs, nearly identical — does that make sense?

**Yes — squarely expected, not a surprise, and continues a pattern this
program has independently confirmed at least five times before on
related geometries (T9, LOGBOOK's LIVE THREADS).**

```
r=234: sigma_abs peccored=541.88286, hollow=541.87979
       relative difference = 5.67e-6  (5.7 ppm)
r=156 (exp-112, same family, same cpl):
       sigma_abs peccored=349.53711, hollow=349.52284
       relative difference = 4.08e-5  (40.8 ppm)
```

`graded_black_shell` at `tau_shell=24` is a deeply saturating absorber —
`τ_center = 2·σ·r_out(cells)` convention, and this program's own anchor
`σ_abs/σ_ext ≈ 0.51` (T9, ESTABLISHED) reflects a shell that extinguishes
essentially all incident power **before** it reaches the interior. This
program has independently measured that fact at least four times before
on this exact question (whether the core's own fill — vacuum/hollow vs.
PEC — changes absorbed power): exp-027 (Iteration 4) found
`Δσ_abs/σ_ext=+1.56×10⁻⁶`, statistically indistinguishable from zero;
exp-028 (Iteration 5) found the hollow core absorbs only 0.0062% of
total incident power directly, via the radial ledger; exp-031
(Iteration 8) found restoring a PEC core changed the ambient-contrast
reading by 6.8×10⁻⁶ via a completely different (single-angle) channel;
and this exact `fixedabs` family itself, at r=156/312 (exp-087/106/108/
110), independently re-confirmed `core_frac≈10⁻⁷` at every point tested.
**exp-114's own r=234 point is a fifth, fully consistent data point on
the identical question, at a new geometry** — the 5.7 ppm relative
difference is, if anything, *smaller* than r=156's own 40.8 ppm on the
same family, continuing rather than breaking the established
"core-fill negligible, shrinking further with r" pattern. This is
physically sensible: adding a PEC core inside a shell so optically thick
that ~99.999%+ of the incident power never reaches r<R_CORE cannot
materially change how much power the shell itself absorbs — a PEC vs.
vacuum interior only matters to the small residual field that
penetrates that far, and that residual is already shown, independently,
to be of order 10⁻⁵–10⁻⁷ of the total.

One honest caveat, not resolved by this review: this cycle does not
compute `box_dev` (the box-ledger channel's own noise floor) at r=234 —
Idealization 3 correctly declines the angular-pattern/named-bin
machinery that instrument lives in, so I cannot independently confirm
the 5.7 ppm reading sits comfortably above or safely below this
channel's own noise floor at this specific geometry. Given the
established trend (`box_dev` margin over the T9 delta: ~1221× at
founding → ~23.8× at r=156 → ~9.0× at r=312, per Iteration 85/87's own
findings), the margin at r=234 likely sits between 9× and 24× — thin
enough to be worth a genuine floor-gate check if a future cycle wants to
cite this specific 5.7 ppm number as more than "consistent with
negligible," but not load-bearing to anything this cycle scores (no
verdict here depends on the core-fill delta at all).

## 4. Iteration-92 candidate directions — my own ranked list

1. **The `fixedabs` family's own third P5 thermal-margin point, r=234,
   done correctly this time** — extend `item3_thermal_row()` (exp-107)
   to r=234 using the now-persisted `energy_ledger`, but **first resolve
   the `CPL_RATIO` commensurability gap I found in §2**: either re-derive
   exp-107's own r=156/312 figures at `cpl=25` (re-running `sc.widths()`
   against already-committed r=156/cpl=25 captures — exp-112's own — and
   the still-blocked r=312/cpl=25 leg once it lands), or apply a derived
   `cpl=20→25` correction factor to this cycle's own r=234 figures before
   quoting a three-point trend. Zero new FDTD cost either way for the
   r=156/234 leg (both already captured at cpl=25); the r=312 leg is
   naturally gated on the still-open named-bin question. This is the
   direct, cheap completion of this cycle's own energy-ledger work and
   sits squarely in my own charter.
2. **A genuine `box_dev` floor-gate on the fixedabs family's own
   core-fill delta at r=234** (folding into item 1 at near-zero marginal
   cost, since the same captures already exist) — closes the one honest
   gap named in §3 above, and gives this program's own T9 thread a
   fifth confirmed point with an actual measured floor, not an inferred
   one from the established trend.
3. **Re-verify Fix 1's own `KAPPA_EXPONENT_CONFIRM_REL` ratio-space
   rescoring against a THIRD `kappa_ratio`** once the r=312 leg's own
   named-bin question is eventually unblocked (Tier 1 item 1, already
   queued by others for a different reason) — this cycle only checked
   the fix at `kappa_ratio=1.5`; a genuinely independent confirmation at
   the founding `kappa_ratio=2.0`'s own re-derivation (not just the
   value it was calibrated to reproduce) would be worth a cheap,
   zero-marginal-FDTD sanity pass once real r=312 data exists.
4. **The still-carried MATERIALS fabrication-tolerance bound and
   `R2_SMOOTH_THRESHOLD=0.90` re-derivation** — not my own charter's
   items, but both are now six-plus consecutive cycles undone on this
   board and neither depends on anything this cycle produced; I note
   them only to avoid this review itself becoming a sixth silent
   omission of a debt this program has explicitly tracked as
   restatement-required.

## Trust suite

`python3 lab/validation/run_all.py --only 12346789` from repo root.

**Director's note**: this reviewer's own attempt did not complete before
its report closed out (severe shared-sandbox contention this window —
multiple Phase-5 seats' own trust-suite invocations were running
concurrently). Not re-attempted here to avoid adding to that contention;
cross-referenced instead against sibling Phase-5 reviews run in this same
window that DID complete cleanly (QUANTUM: 41/41, clean single run,
2461.6s; EM: 41/41, independently re-derived; VISION: 41/41). Zero `lab/`
diff throughout this cycle (confirmed repeatedly by every seat and by the
Director at Phase 3/4). No reason to expect a different result from this
seat's own review work, which touched no `lab/` file.

## Verdict

**PARTIAL** — matching this exact T28 governance/instrument-calibration
sub-thread's own unbroken pattern since Iteration 82, reasoned
independently from my own charter, not by inertia. Not RULED OUT (T1
correctly N/A throughout, independently reconfirmed here); not
PROMISING (this is instrument-calibration work — no constraint-1/2/3/4
metric moves, and cannot, by its own honest scope). Real, disclosed,
independently-verified progress on my own charter's own question
specifically: my Fix 3 landed correctly and completely (energy ledger
genuinely persisted, `sigma_ext_cross` genuinely reproduces, R23 asserts
genuinely fired on real data); the `fixedabs` family's own core-fill
question gained a fifth, fully consistent confirming data point at a
new geometry (§3); and a real, physically-motivated, cheap thermal-margin
extension is now available for Iteration 92 — but is correctly *not*
this cycle's own job, and I found and disclosed a genuine
commensurability trap (`CPL_RATIO`) that a naive attempt at that
extension would otherwise walk straight into, exactly the class of
defect this program's own R9 exists to catch, caught here before any
cycle tries to build it.
