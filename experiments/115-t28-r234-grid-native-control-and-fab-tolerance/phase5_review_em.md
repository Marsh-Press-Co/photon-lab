# Phase 5 Review — ELECTROMAGNETISM — Panel Iteration 92 (exp-115)

*Charter: field/wave behavior, impedance matching, energy coupling; owns the
reciprocity / passivity / causality bookkeeping and formalizes what T1 permits
and forbids. Fresh context. Read in full this session: `PANEL.md` including
today's Metrics scope amendment; `LOGBOOK.md` RULED OUT registry R1–R34 and the
Iteration-92 record at the file's end; `PLAN.md` 1–80; this cycle's
`phase1_proposal.md`, my own seat's `phase2_critique_em.md`,
`phase2_redteam_audit.md` (RT-6/RT-7, §3 docket, §4), `NOTES.md` (Phase 3 +
frozen Predictions), `chunk_runner115.py`, `run115.py`, `analyze115.py`,
`results.json`, `data/readings.json`,
`data/readings_session1_interrupted_20260905T2354Z.json`,
`data/cg_session1_interrupted.log`, `data/cg_session2.log`. I did **not** read
any other seat's Phase-5 review. Every figure below was recomputed by direct
arithmetic against the committed JSON and committed source in this session;
nothing is restated from the cycle's own prose (R4). No git state was changed
and no simulation was run.*

---

## 1. Verdict

# PARTIAL

**T1 escape route: N/A — verified structurally, not accepted on assurance.**
`chunk_runner115.py::build_sim` (`:311–329`) constructs the three scenes and
`_time_control_blend` (`:330–367`) brackets `sim.run()` only; there is no
`full_capture`, no `lab/sections.py` call, no `window_stats`, no
`lab/ambient.py` call, no angular instrument anywhere in the executed path. The
cycle therefore produces **no** constraint-1/2/3/4 observable and moves none.
The article the M9 sidecar bounds (`graded_black_shell`, `tau_shell = 24`,
`eps_r ≡ 1`) is passive, linear and time-invariant, and LOGBOOK's ESTABLISHED
section already records it as failing constraint 3 by construction; a
core/backing-insensitivity bound on such an article cannot be constraint-3
progress, and both `DISCLAIMER_115` and the M9 blockquote say so **inside** the
quotable text (MF-4 discharged). This cycle conforms to PANEL.md's new
Iteration-92 scope amendment in letter and in substance.

**Why PARTIAL and not CONFIRM.** The measurement itself is sound and every
scored quantity reproduces bit-exactly from the persisted readings (§2.1–§2.4).
The ABBA protocol my own Phase-2 seat asked for was adopted in MF-6's fuller
form, executed in the coded order, and I can now show it *worked* — empirically,
not just in closed form (§2.2). Three things stop this being a clean CONFIRM:

1. **M3's verdict is anchor-dependent, and this cycle's own data supersedes the
   anchor.** `G-DURATION-INVARIANT` was scored against `R_DEG = 7.596%`, a
   *cloud* magnitude. The bench's own duration shifts, measurable for the first
   time from these readings, are `+1.663%` (r=156) and `−1.293%` (r=234) —
   4.6× smaller and **opposite in sign**. Re-anchored on the venue that ran the
   experiment, `d_dur = 0.029034` exceeds the bar and M3 flips, which flips
   `m6_directional_only` to `True` (§2.5). The pre-registration is R17-compliant
   and the scored verdict stands as filed; the *interpretation* does not survive
   the cycle's own new information.
2. **A second complete bench session is committed to `data/` and analysed
   nowhere.** `data/readings_session1_interrupted_20260905T2354Z.json` holds four
   readings whose `G_pair1 = 2.292240` differs from the scored session's
   `2.229628` by **+2.81%** — nearly 2× the `d_rep` the cycle reports as its own
   noise/drift statistic. It is quoted in LOGBOOK and PLAN and appears in
   `results.json`, `result_text` and `NOTES.md` **zero times** (§2.6, D-3).
3. **M5's verdict string says close to the opposite of M5's point estimate.**
   `k_B = exponent_B = 2.995546218006855` — the pre-R28 hardcoded exponent
   `3.0` to four decimals — is filed under the label `CONFIRM (kappa_exponent
   generalizes across kappa_ratio)` with `may_move_logbook_verdict = True`
   (§2.7). The power limit is disclosed in three places, but the *label* is
   what a future cycle quotes.

None of the three is a rule violation at freeze. All three are load-bearing for
how this cycle is written into LOGBOOK, which is what Phase 5 is for.

---

## 2. Findings — numbered, re-derived

### 2.1 ABBA was executed exactly as MF-6(a) specified, and both pairwise `G` are persisted

`chunk_runner115.py:534,538,545,546,555,556` takes readings in the order
`S156 → S234 → U156 → U234 → U234b → U156b`. That is A,B on the short pass and
**A,B,B,A** on the sustained pass, as adopted. `analyze115.py:122–128` forms
`g_pair1 = U234/U156`, `g_pair2 = U234b/U156b`, and `g_sustained = mean(...)`.
Recomputed from `results.json` `readings[*].per_step_s`:

```
per_step:  S156 0.04858939027786255   S234 0.11239203476905822
           U156 0.04970505291927912   U234 0.11082375609762692
           U234b 0.11105367999581237  U156b 0.04908984934084655
G_short   = 0.11239203476905822/0.04858939027786255 = 2.3130982736423493   filed identical
G_pair1   = 2.2296275647790664   filed identical
G_pair2   = 2.2622534289060674   filed identical
G_sustained = (G1+G2)/2 = 2.245940496842567   filed identical   (bit-exact, all 16 digits)
```

`n_sim_run_calls = 18 = n_sim_run_calls_expected`, R19's assert conditional on
`repeat_skipped` as MF-9 required (`chunk_runner115.py:563–569`). Three budget
gates fired at `after_S156`, `after_S234`, `after_U234`, each **before** the
next `Sim.run()` (`:535, :542, :550`), all `PROCEED`; `repeat_skipped = False`,
`sustained_stepped_down = False`. Machine-state block, per-reading ISO-UTC
timestamps, per-scene wall times and `loadavg` before/after every reading are
all present. **MF-6(a),(b),(e) and MF-12 discharged as coded.**

### 2.2 The ABBA cancellation is not just argued — I measured it. 722× lag reduction.

My Phase-2 A3 and Red Team's RT-6 both derived, in closed form, that A,B,A,B
leaves the mean-B midpoint trailing the mean-A midpoint by `(a+b)/2` for any
`a,b`, while A,B,B,A leaves lag `= 0`. From the persisted midpoints:

```
mean(A) mid = (mid[U156]+mid[U156b])/2 = 1788671659.5939
mean(B) mid = (mid[U234]+mid[U234b])/2 = 1788671660.7061
residual lag  =  +1.112 s
(a+b)/2 with a = 497.150 s, b = 1108.459 s  =  802.805 s   <- what ABAB would have given
reduction factor = 721.8x
```

That is the first empirical confirmation in this program that the reorder does
what its closed form promises. **What it bought, priced in the cycle's own
units:** using the measured relative drift rates, the ABAB bias on `G` would
have been `r_234 × 802.8 s = +0.150%` (numerator-lag form) to
`(r_234 − r_156) × 802.8 s = +0.515%` (differential form) — real, one-signed,
and invisible to `d_rep` under ABAB, but small against M5's 2.43% headroom.
The fix was correct and cheap; the systematic it guarded proved modest on this
bench. That is worth saying plainly rather than claiming a save that did not
occur.

### 2.3 `d_rep` under ABBA is exactly a **grid-differential log-drift** statistic. MF-6(d)'s "drift+noise" is right but under-specific — and there is an exact blindness it does not name.

MF-6(d) restated `d_rep` as a drift+noise statistic. Re-deriving it from the
four sustained readings shows something sharper, and it is an identity, not an
estimate:

```
ln(G2/G1) = [ln p234b - ln p234] - [ln p156b - ln p156] = D_234 - D_156
D_234 = +0.0020725314347837896      (r=234 same-grid log change over its lag)
D_156 = -0.0124543173049979920      (r=156 same-grid log change over its lag)
D_234 - D_156 = +0.014526848739781781
ln(G2/G1) computed directly from the ratios = +0.014526848739781622   (identical)
exp(...) - 1 = 0.014632876199767608     filed d_rep = 0.01463287619976741
```

So `d_rep` **is** the difference of the two grids' same-grid drifts. Two
consequences the record does not state:

- **Common-mode drift cancels in `d_rep` exactly.** Had the bench drifted 10%
  uniformly across both grids, `d_rep` would still read ≈0 and M4 would still
  return `REPEATABLE`. ABAB's null channel was blind to *monotone* drift; ABBA's
  is blind to *common-mode* drift. Neither ordering, with two sustained readings
  per grid, produces a channel sensitive to common-mode session drift. `lab/
  ARTIFACTS.md`'s invariant applies to the replacement as much as to the
  original: an alarm must be shown able to produce the reading that means "bad."
- **`d_rep` and the MF-6(c) drift-rate block carry the same information.** With
  four numbers there are three independent ratios; `drift.r156`, `drift.r234`
  and `d_rep` are two independent quantities and their exact difference. The
  drift block is not an independent corroboration of `d_rep` and should not be
  cited as one.

### 2.4 The composition rules were evaluated exactly as coded. All four booleans re-derived.

```
m3_scored          = (not repeat_skipped) and d_rep <= M3_INVARIANT_BAR
                   = True and 0.014633 <= 0.037982123779318644          -> True    filed True
m7_underpowered    = repeat_skipped or d_rep > M7_POWER_BAR
                   = False or 0.014633 > 0.03                           -> False   filed False
m6_directional_only= (m3_verdict != "G-DURATION-INVARIANT")             -> False   filed False
m5_protocol_caveat = any band edge strictly inside [2.2176904, 2.2458389]
                     edges 2.0785394 / 2.8121415 / 1.7117383 / 3.1789426-> False   filed False
m5.may_move_logbook_verdict = (not caveat) and m3_scored                -> True    filed True
```

`run115.py:300–322` implements M4's four-way MARGINAL split at `0.02 / 0.03 /
0.037982 / 0.075964` with the consequence in the label, `:285–298` M3's
mechanism-neutral labels, `:412–441` M7's two-sided labels. **MF-9 discharged
as coded, in full.** MF-5's inversion is real and load-bearing: `run115.py:326–
347` computes `exponent_B = ln(1.5·G)/ln(1.5)` and code-asserts
`|measured_ratio − 1.5·G| < 1e-12`; feeding the Phase-1 document's literal
`measured_ratio` would evaluate `1.5**(1.5·G)` and return a false REFUTE.

One convention divergence, immaterial but worth stating (D-7): `run115.py:310`
computes `d_rep = |G2 − G1| / G1`, matching the Phase-1 M4 definition. My own
Phase-2 §3 asked for `|G1 − G2| / Ḡ`, which gives `0.014526593`. The difference
is 0.7% of the statistic and crosses no bar. State the denominator; do not
change it.

### 2.5 M3's bar is a cloud number the bench now supersedes — and the "invariance" is anti-cancellation, not cancellation

This is my seat's principal finding. `d_dur = |G_sust − G_short|/G_short =
0.029034` (filed) — but decomposing it:

```
bench duration shift, 1000 -> 3334 steps/scene, per grid:
   r=156:  mean(U156,U156b)/S156 - 1 = +0.016630   (longer = SLOWER)
   r=234:  mean(U234,U234b)/S234 - 1 = -0.012931   (longer = FASTER)
   (1 + r234)/(1 + r156) - 1 = -0.029078   == the filed d_dur to 4 digits
   |r156| + |r234| = 0.029561
```

The two grids' duration effects are **opposite in sign**, so in the ratio `G`
they **add**. Had they been equal and same-signed — the "grid-independent
throughput factor" R31/R33 both implicitly assume — they would have cancelled
exactly and `d_dur` would have read ≈0.4%. The verdict label
`G-DURATION-INVARIANT` is correct against its pre-registered bar; the underlying
behaviour is the opposite of cancellation.

And the bar itself is now the wrong one for this venue:

```
scored bar:  R_DEG/2 = 0.037982  (cloud, exp-114, r=156)      -> d_dur 0.029034 => INVARIANT
bench-native r=156 anchor: 0.016630, half 0.008315            -> d_dur 0.029034 => NOT-INVARIANT
bench-native r=234 anchor: 0.012931, half 0.006465            -> d_dur 0.029034 => NOT-INVARIANT
```

Under **any** bench-native anchor M3 reads `G-NOT-DURATION-INVARIANT`, and
`m6_directional_only` (`run115.py:392–410`, MF-9's inverted rule) becomes
`True` — M6's AMBIGUOUS would be reported directional-only rather than as a
scored reading. R17 was satisfied at freeze (the cloud `R_DEG` was the largest
comparable then on file), so this is **not a rule violation and must not be
retro-scored**. It is a disclosure the Result owes and a re-anchoring input
every future bench cycle must use.

### 2.6 The cross-session comparison: load on this bench is grid-differential and sign-inconsistent — a genuine, unstated refutation of the assumption R31/R33 rest on

Session 1 (2026-09-05T23:54Z, host under residual load, interrupted at ~00:53Z)
versus session 2 (2026-09-06T04:39Z, clean start, `loadavg` 0.044/0.104/0.049):

```
per-step, session1 slower than session2 by:
   S156 +4.775%   S234 +4.208%    (short pass:  SMALLER grid hit harder)
   U156 +5.369%   U234 +8.328%    (sustained:   LARGER  grid hit harder)
G_short  s1 2.300578  vs s2 2.313098   ->  -0.541%
G_pair1  s1 2.292240  vs s2 2.229628   ->  +2.808%
```

Read as EM bookkeeping: a 4–8% **common-mode** slowdown did **not** divide out
of `G`. It carried a grid-differential residue of `−0.54%` on the short protocol
and `+2.81%` on the sustained protocol — different magnitude *and* different
sign between the two protocols. That is a direct empirical counterexample to
"a session's throughput factor is grid-independent," the assumption R31's
r=156-only control and R33's normalization both rest on. It is measured on the
same machine, the same binary, the same geometries, hours apart.

**What this says about M6's AMBIGUOUS reading of the cloud's `G_E = 2.7455`,
stated to R7's standard.** `T = 2.245940/2.745506 = 0.818043`, `|T−1| =
0.181957`, between the `0.152950` TRANSFERS bar and the `0.305900`
DOES-NOT-TRANSFER bar — AMBIGUOUS, correctly. The bench-to-cloud gap in `G` is
`2.745506/2.245940 = 1.2224`, i.e. **+22.24%**. Contention is now a
*demonstrated*, *signed*, *grid-differential* inflator of `G` on this hardware,
pointing in exactly the direction that would inflate `G_E` — so it is a live
candidate for part of the gap. It is **not** established as the cause: the
demonstrated bench magnitude is +2.81%, which is `1/7.9` of the gap, its sign is
protocol-inconsistent within this very pair, and three further confounds remain
unseparated (a different machine and memory hierarchy, exp-114's
burst-vs-production protocol mismatch, and — for `KAPPA_COST_EXPONENT` itself —
a different `kappa_ratio`). The honest sentence is *"contention is a live,
signed, partial explanation, insufficient at the measured magnitude,"* not
*"the cloud figure is a contention artifact."*

### 2.7 `k_B = 2.9955` is pure `N²`, it replicates across both bench sessions, and the record must not over-claim from it (R7)

```
excess = G_sustained/2.25 - 1 = -0.0018042236255256805      -> N2_HOLDS (|excess| <= 0.05)
k_B = 3 + ln(G/2.25)/ln(1.5) = 2.995546218006855
exponent_B (M5) = 1 + ln(G)/ln(1.5) = 2.995546218006855      IDENTICAL, and identically so:
   exponent_B - k_B = [1 + lnG/ln1.5] - [3 + (lnG - ln2.25)/ln1.5] = 0   for all G, since ln2.25 = 2 ln1.5
```

So M5's exponent, M7's `k_B` and M7's `excess` are **one number under three
labels**, all monotone in the single measured `G`; only M3 (adds `G_short`), M4
(adds the pair split) and M6 (adds `G_E`) contribute independent information.
The frozen Predictions already carry VISION's version of this identity; the
Result should carry it too, so the cycle is not read as five corroborating
measurements.

**Cross-session replication, free and not in the record.** Scoring session 1's
own sustained pair through the same arithmetic:

```
session 2 (scored):    G = 2.245940  ->  k = 2.995546   rel_dev 0.08154  CONFIRM, N2_HOLDS
session 1 (unscored):  G = 2.292240  ->  k = 3.045871   rel_dev 0.06261  CONFIRM, excess +0.0188 => N2_HOLDS
pure N^2 reference:    G = 2.250000  ->  k = 3.000000   rel_dev 0.07988
cloud KAPPA_COST_EXPONENT:            k = 3.205330 <-> G_ref 2.445340, +8.9% above the bench
```

Two bench sessions, different host load, both land within 2% of pure cell-count
scaling and both give `k ≈ 3.0`. **That is a materially stronger statement than
the single scored session and it costs nothing.** The record must say: `k =
3.2053` is not reproduced on this bench at `kappa_ratio = 1.5`; the bench's own
two sessions give `2.9955` and `3.0459`. The record must **not** say:
`KAPPA_COST_EXPONENT` is a cloud-contention artifact, or that `k = 3.0` is
restored program-wide — `k` was fitted at `kappa_ratio = 2.0`, this cycle
establishes nothing at any other ratio (Idealization 2, correctly stated), and
the machine axis and the protocol axis are unseparated.

### 2.8 The two-point protocol interval: `c156` is negative, which is not an overhead, and both production endpoints are extrapolations. Neither is disclosed.

`run115.py:349–390`. `p(n) = p_∞ + C_g/n` with `S` and `U` as the two points.
Re-derived from the readings (`p_U` = the mean over each grid's two sustained
readings, as coded):

```
denominator 1/1000 - 1/3334 = 7.00060e-04
r=156: (0.04858939 - 0.04939745)/7.00060e-04 = c156 = -1.1542737280358781   p_inf = 0.04974366400589843
r=234: (0.11239203 - 0.11093872)/7.00060e-04 = c234 = +2.0759888398786654   p_inf = 0.11031604592917955
G(burst 3334/3334) = 2.2458389149395477
G(production 8000/12000) = 2.2276295684987977
G(n -> inf) = 0.11031604592917955/0.04974366400589843 = 2.217690396029104
interval [2.2176904, 2.2458389], rel width 1.269%, spans no band edge -> m5_protocol_caveat False
```

All four filed values reproduce exactly. Two things the record must add:

- **`C` has units of seconds and is a per-scene fixed overhead.** `c234 =
  +2.076 s/scene` is a physically sensible warm-up/allocation cost for a 2100²
  scene set. **`c156 = −1.154 s/scene` is a *negative* fixed overhead — not an
  overhead at all.** It encodes that on r=156 the per-step rate got *slower* with
  the longer run, the opposite of amortization, so the two-point form is being
  evaluated outside its own physical interpretation on that grid and the
  `n → ∞` endpoint extrapolates a warm-up transient in the wrong direction. Its
  origin is visible in the per-scene data (§2.9): a single cold-start scene.
- **Both production endpoints are extrapolations, not interpolations.** 8000 and
  12000 lie outside the `[1000, 3334]` bracket the two points define. The note
  in `results.json` discloses the mean-of-ratios caveat but not this. The
  interval's 1.27% narrowness is therefore **not** evidence that the protocol
  mismatch is small — it is a statement about how little this particular pair of
  `C` values moves `G` between the three chosen `n`.

### 2.9 The per-scene sub-timings — the instrument upgrade I asked for at Phase 2 — contain a real noise floor and a real cold-start transient, and nothing in the cycle reads them

MF-6(b) persisted per-scene wall times. Comparing the **same scene** across the
two sustained readings on a grid gives three genuine replicate pairs per grid:

```
r=156  U156b/U156 per scene:  empty 0.97553   hollow 0.99090   peccored 0.99662
                              sample std 1.091%   spread 2.109%
r=234  U234b/U234 per scene:  empty 1.00093   hollow 1.00323   peccored 1.00207
                              sample std 0.115%   spread 0.230%
```

The r=234 grid reproduces to **0.1–0.2% per scene**. The r=156 grid's apparent
`−1.245%` "drift" — which, per §2.3, *is* essentially the whole of `d_rep` — is
**not rate-like at all**: it is concentrated in one scene, `U156/empty`, which
ran 2.45% slower than its repeat while `peccored` moved only 0.34%. `U156/empty`
is the first 3334-step run ever executed on that grid in that session; in
`U156b` the same scene is the *fastest* of the three. That is a first-touch /
working-set warm-up transient, not a session drift, and it means the MF-6(c)
r=156 "rate" of `−1.639%/hour` is an unwarranted rate-ification of a one-off
step.

**Sensitivity, stated as not-scored (R33 addendum (a) discipline).** Replacing
`U156/empty` with its own repeat value:

```
U156 per_step 0.04970505 -> 0.04929552   G_pair1 2.2296276 -> 2.2481506
G_sustained 2.2459405 -> 2.2552020 (+0.412%)   excess -0.0018 -> +0.0023
k_B 2.995546 -> 3.005696
```

Every verdict is unchanged and the headline moves *toward* exactly 3.0. **The
central result is robust to the largest identifiable defect in its own inputs**
— which is the strongest thing I can say for it, and it should be said.

### 2.10 Energy bookkeeping N/A — the settling arithmetic verified, under a convention the record does not name

`S = COURANT_FRAC/√2 = 0.32/1.41421356 = 0.22627416997969518` cells/step
(`experiments/110-.../run.py:58`). At 3334 steps the wavefront advances
`754.398` cells. Two readings of "reaches X% of the domain":

```
fraction of N traversed:        r=156  53.89%      r=234  35.92%
source-anchored, (SRC_X + S*n)/N: r=156  65.31%    r=234  47.35%   <- reproduces "~65%" / "~47%"
```

**The cited 65%/47% figures are correct**, under the source-anchored convention
(wavefront position as a fraction of the domain, having started at the source
plane). That convention is nowhere stated, and the naive reading gives 54%/36%;
name it. Either way the conclusion holds *a fortiori* — the fields are far from
settled, no `σ_abs/σ_ext` ledger is computable, and T27's paid-for lesson (a
truncated run is not a small perturbation of a settled one) applies. **The
energy-ledger / THERMO-sidecar N/A declaration is correct, correctly reasoned,
and correctly stated as physical rather than clerical.** This closes the
disclosure I asked for in my own Phase-2 A14 and exp-104's three-cycle-old gap.

The companion claim in the same sentence does **not** reproduce: production
sizing gives `8000 × 0.226274 / 1400 = 1.293` traversals (`1.407`
source-anchored) on both grids, not "~2 domain crossings" (D-1).

### 2.11 The M9 sidecar: reproduction gate passed, and the corrections I asked for at Phase 2 landed

`sidecar_m9.status = "REPRODUCED"`. `τ_true` recomputed from
`lab/materials._graded_black` at both family members —
`8.258813114090946` (cpl=20) and `8.258813114090952` (cpl=25), `rel = 8.13e-07`
against the filed `8.258819829686677` — confirming PHOTONICS' exact identity and
retiring QUANTUM's concavity interval. MF-1 landed: `exp(−τ_true) = 2.58966e-04`
as the scale, `2·exp(−τ_true) = 5.17932e-04` as the upper bound, with
`exp(−2·τ_true) = 6.70635e-08` persisted only under
`proposal_figure_exp_minus_2tau_WITHDRAWN` and its `wrong_by_factor =
3861.508`. That is my A8 adopted in full, and the corrected estimate does what
A8 predicted: the largest measured aggregate delta is `1.0874e-04`, i.e.
`0.21×` the coherent upper bound — same decade, not three decades below.
MF-2 landed: the `|σ_ext − σ_ext_cross|` quantity is withdrawn as a differential
floor with the bit-identical between-scene values persisted (`0.0` exactly at
r=234, `2.274e-13` at r=156), and exp-108's six-margin `item_ii` family
substituted. MF-11 landed: "two independent channels and their exact algebraic
sum," with my own OV-4 promotion of `σ_ext_cross` correctly **declined** — Red
Team is right that `Δσ_ext_cross ≡ Δσ_ext` and my "2 ppm agreement" was a
normalization artifact, refuted by my own A7. MF-4/MF-10 landed: the
constraint-3 failure, the realizability tier and the T18 tier all sit *inside*
the quotable blockquote.

One arithmetic inconsistency inside the sidecar's own citations (D-2), and one
observation on the gate: `run115.py:707–708` asserts the differential-floor
ratios against hand-typed targets `4.4653` and `11.6959` at `rel_bar = 1e-3`,
while the computed values are `4.464602` and `11.695432`. The gate passes
because its tolerance is 7× the disagreement — a reproduction gate whose own
expected value is hand-typed and slightly off is R4's shape inside the machinery
built to prevent R4.

---

## 3. Defects

| # | Rule | Defect | Load-bearing? |
|---|---|---|---|
| **D-1** | **R4** | `DISCLAIMER_115` (`run115.py:977`, in **both** `predictions_text` and `result_text`): "each grid gets ~2 domain crossings." Reproduces as **1.293** traversals (1.407 source-anchored) at the production step counts. Frozen at Phase 3, survived into Result, caught only at Phase 5. | No — the N/A conclusion it supports is strengthened by the corrected figure. |
| **D-2** | **R4** | The same `results.json` states the exp-108 differential-floor ratio as **"4.47x"** (`DISCLAIMER_115`, `run115.py:965`, and the sidecar's own `reading` string, `:709`) and as **"4.46x"** (`result_text` body). The computed value is `4.464602`. The reproduction gate's own hardcoded target is a third value, `4.4653` (`:707`), passing only because `rel_bar = 1e-3` is 7× the disagreement. | No — but it is a self-contradiction inside one committed artifact, and it is the **second** R4-class item in text MF-11 was written to clean. |
| **D-3** | **R33 addendum (a)** + **R21** | `data/readings_session1_interrupted_20260905T2354Z.json` — four readings from a second, same-machine bench session — is committed, quoted in LOGBOOK's Iteration-92 entry and PLAN's Current state, and appears **zero times** in `results.json`, `result_text`, `analyze115.py` or `NOTES.md`. Its `G_pair1 = 2.292240` differs from the scored `2.229628` by **+2.81%**, ~1.9× the cycle's own `d_rep`. R33 addendum (a) requires alternative same-session readings be disclosed as a stated, not-scored sensitivity; the same standard plainly applies to an alternative *session* on the same machine. | **Yes.** Two same-machine values for the cycle's own primary statistic now sit in the permanent record with no reconciliation; either can be quoted forward. It is also, per §2.7, the cycle's strongest replication evidence, unused. |
| **D-4** | **R17** (satisfied at freeze) / **R15** | M3's bar is a cloud `R_DEG = 7.596%`; the bench's own duration shifts are `+1.663%` / `−1.293%`, 4.6× smaller and opposite in sign. On any bench-native anchor M3 flips and `m6_directional_only` becomes `True`. Not a violation — a superseded anchor and an undisclosed anchor-dependence. | **Yes** for interpretation and for every future bench cycle's R17 anchoring; **no** for the frozen score. |
| **D-5** | **R7** / **R21** | `protocol_mismatch_interval`: `c156 = −1.154 s/scene` is a negative fixed overhead — the model evaluated outside its own interpretation, with the `n → ∞` endpoint extrapolating a cold-start transient backward. Both production endpoints (8000/12000) lie **outside** the `[1000, 3334]` bracket. Neither disclosed; the interval's 1.27% narrowness is cited as if it bounded the protocol mismatch. | Partly — the `m5_protocol_caveat = False` outcome is unaffected by any plausible correction, but the interval is being read as stronger evidence than it is. |
| **D-6** | **R21** | `m7.model_comparison.favoured = "constant-k"` is persisted and quoted in Result prose as "(model comparison: constant-k)", while the same metric's verdict `N2_HOLDS` means **both** candidate models are excluded (const-k predicts `excess = +0.08682`, const-ε `+0.15295`; measured `−0.00180`). The "both models wrong" statement exists only in `m7.note` inside the JSON, not beside the label. | Yes for citation risk — "favoured: constant-k" is exactly the phrase a future cycle lifts. |
| **D-7** | **R18** (minor) | `run115.py:310` codes `d_rep = |G2 − G1|/G1` (Phase-1's literal definition); my adopted Phase-2 change specified `/Ḡ`, giving `0.014526593`. 0.7% of the statistic, no bar crossed. State the convention; do not change the code. | No. |
| **D-8** | **R21** / house discipline | `NOTES.md`'s own **"Phase 4 — Results"** section still reads `(pending)` and `"Phase 5"` `(pending)`. Every result, including the M9 blockquote R21 requires stated inline, exists only inside `results.json`'s `result_text`. | Must be closed in this Phase-5 write-up — flagged as an open action, not a shipped defect. |
| **D-9** | **R25** (disclosure) | The Phase-4 re-run took a path neither branch of PLAN.md's own pre-registered resume recipe names: the recipe offered (i) analyse with `repeat_skipped=True` or (ii) re-run only `U234b`/`U156b` as a disclosed second session; what was executed was a **full six-reading re-run from scratch**. That was the *better* choice — it preserves ABBA inside one session — but a deviation from a pre-registered degradation path is a numbered disclosure, not a silent improvement. | No, but it must be written down. |

**R20 tally:** D-1 and D-2 are two independent R4-class defects surviving the
Phase-3 freeze into Result and caught only at Phase 5. R20's bar is **three**.
**R20 does not fire.** Named as a standing observation: Red Team's Phase-2 audit
already called this cycle the **sixth** consecutive one at or just under R20's
density bar (exp-108 → exp-112 each tallying 1–2); the Result section adds two
more, still under the bar. Both new instances sit inside the `DISCLAIMER_115`
string that MF-10 wrote to fix exactly this class — the correction machinery is
now the place the class recurs.

**R34:** the Iteration-92 criterion-4 firing was ruled a notification. D1
(PANEL.md scope amendment) is written and verified present. D2 (the Director's
ruling on Tier-3 item 10) is written into both PANEL.md and the LOGBOOK
CHECKPOINT entry. Under R34 the firing self-closes on Iteration 93's Red Team
audit confirming both from primitives. Nothing in this review opens a new
criterion-4 firing.

---

## 4. Ranked top-3 candidate directions

Ranked by expected value to the **program**, not to the T28 sub-thread. My
standing position, stated as this seat's own: exp-115 is a well-executed cycle
of a kind the program has now run fifteen times consecutively, and its marginal
scientific yield is falling. Iteration 93 must not be a sixteenth.

### Rank 1 — Iteration 93, item 2: **the T1 ledger, written as a passivity/causality bound with numbers.** My seat's own charter debt, unpaid for eleven cycles.

**The move.** PANEL.md seat 3 assigns me "the reciprocity / passivity /
causality bookkeeping — formalizes what T1 permits and forbids for each
proposal." Eleven consecutive cycles have filed "T1 escape route: NONE" and not
one has written the quantitative statement of what each of T1's four named
escape routes *requires*. This is the exact shape of the debt MATERIALS finally
paid this cycle as item 5, and it is exactly as cheap: **zero FDTD, zero
grid-steps.**

**The content, concretely, so Red Team can price it as a real question.** For
the intensity-gated route `σ(I)` — the route the witness statement most directly
implies — the medium must be *more* absorbing at the beam's irradiance than at
ambient irradiance, at the same volume, at the same wavelength. Write the
required contrast as a pure ratio of two irradiances that VISION's item-1
re-score will pin (beam irradiance at the volume; night-ambient irradiance at
the same volume), convert it to the required `dσ/dI` and threshold `I_th`, and
then check the sign against passivity: a **passive** saturable medium *bleaches*
with intensity (`dσ/dI < 0` — that is what saturable absorption means); the
phenomenon demands `dσ/dI > 0` across a threshold, i.e. reverse saturable
absorption, which is a real class (RSA, two-photon, free-carrier) with real
published `β` values and a real, boundable magnitude. State the required `β` or
`σ_ex/σ_gs` ratio, and whether *any* value of it can satisfy constraints 1+2+3
jointly at the pinned irradiances. Do the same, in one paragraph each, for
`σ(x,t)` (which requires an energy source and is therefore not passive — say so
with the switching energy), angular selectivity (a reciprocity argument: a
medium opaque along the beam axis and transparent along the observer axis is
permitted by reciprocity only if the two axes differ, so bound the required
angular acceptance against the beam's own divergence), and sub-threshold
operation.

**Why this is Rank 1.** If the σ(I) sign-and-magnitude argument closes, that is
a **Checkpoint criterion 2** — "a constraint subset shown jointly unsatisfiable
within a whole mechanism class, gates clean" — which PANEL.md names as the
program's honest alternative product and which the program has never once
reached. If it does not close, it produces the first *parameterized target* for
MATERIALS to price (published / plausible / unobtainium-with-parameters), which
is the fastest route back to a real proposal. Either outcome advances the
logbook. Nothing else on the board can say that.

**Ruled-out check.** R1 rules out passive refractive/TO cloaking; nothing here
proposes it. T1 itself names σ(I) as a permitted escape route. R5's addendum
concerns the `≈233/234` named-constant periodicity and is unrelated. Not a
re-proposal.

**Cost:** zero FDTD, one shift, desk arithmetic plus VISION's pinned numbers.

### Rank 2 — Iteration 93, item 3: **bench-native re-anchoring + the cross-session load datum + this review's D-1..D-7.** Folded in, zero FDTD, no new falsifiable question.

Deliverables, all arithmetic over already-committed data:
1. Persist and publish the **bench-native duration anchors** (`+1.663%` r=156,
   `−1.293%` r=234) and the **per-scene replicate noise floor** (r=234 sample
   std `0.115%`; r=156 `1.091%`, dominated by one cold-start scene). Adopt the
   rule that an R17 tolerance anchor must come from the **venue the run executes
   on** when the quantity is venue-dependent — the cloud `R_DEG` is retired for
   bench cycles.
2. Persist the **session-1 vs session-2 comparison** as a stated,
   `..._DO_NOT_SCORE` sensitivity (D-3), including session 1's own
   `k = 3.045871`, so the two-session replication of `k ≈ 3.0` is on the record
   and neither value can be quoted forward alone.
3. Persist the M3 **re-anchoring sensitivity** (D-4): on a bench-native anchor
   M3 flips and `m6_directional_only` becomes `True`. Not scored; disclosed.
4. Correct D-1, D-2, D-5, D-6; state D-7's convention; close D-8 and D-9 in the
   Phase-5 write-up.
5. Add a **common-mode drift channel** the current design cannot see (§2.3): the
   per-scene sub-timings already persisted give three replicate pairs per grid
   at zero cost. Making that the null channel is the positive control `d_rep`
   structurally cannot be.

This is bookkeeping, not a question. It rides as a labelled rider exactly as
item 5 did this cycle, and it must **not** be allowed to become the cycle's
falsifiable heart.

### Rank 3 — Iteration 94, item 1: **the r=312 / cpl=25 / +168.75° leg, with the per-bin observer-return channel — the only queued item that produces new field observables.**

Red Team's Iteration-92 queue sequenced this explicitly *after* item 1 so it
could reuse whatever cross-grid factor item 1 measured; `G` is now measured, so
the sequencing condition is discharged and the item is unblocked. It is also the
one T28 item with a genuine constraint-2 hook: this cycle's own sidecar
(`sidecar_m9.d_per_bin`) shows the core/backing perturbation moves the
floor-gated **local** per-bin angular pattern by `5.290×10⁻²` at r=312, with the
two largest resolved deviations at **±138.75°** — inside the observer-return
hemisphere PANEL.md scores constraint 2 on. A near-`10⁻⁴` aggregate bound and a
`5%` observer-hemisphere per-bin excursion are *the same article*, and only the
angular channel touches a constraint. Extending it to `+168.75°` and to r=234
(whose per-bin data has never existed — exp-114's captures were never persisted)
is the first move in this sub-thread that could feed back into a constraint
metric rather than into a cost model.

**Bench-anchored cost, computed from this cycle's own measured rates** (which is
precisely what exp-115 was for): three production scenes at r=156/cpl=25,
8000 steps/scene = `3 × 8000 × 0.0493975 = 1185.5 s` (19.8 min); at
r=234/cpl=25, 12000 steps/scene = `3 × 12000 × 0.1109387 = 3993.8 s` (66.6 min).
Both, and their sum (`5179 s`), fit inside `COST_GATE_TOTAL_S = 10800` with the
`1.10` margin applied. This is the first cost projection in the program's
history that uses a same-venue, same-grid measured rate — R31 and R33 are
satisfied by construction rather than by correction.

---

## 4b. As Director-lead of Iteration 93: how I execute D2

D2 is fixed and I do not relitigate it. **Iteration 93's Tier-1 item 1 is
VISION SCIENCE's re-score of the program's only-ever Tier-W/Tier-A constraint-3
citation through the modernized `lab/ambient.py` instrument, regardless of
lead-seat rotation.** I lead by rotation; VISION owns the thresholds. My
execution commitments:

**What VISION must pin, before any run, in code with cited sources — its own
PANEL.md charter duty, and the thing that has never been done:**

1. **The scene's ambient regime**, in cd/m², for the reported night flashlight
   sweep — scotopic or mesopic, said explicitly, with a source. One number per
   tier, not a range.
2. **The observer's adaptation state including self-glare from the flashlight.**
   PANEL.md's Tier-W definition names this in its own text ("adaptation state
   including self-glare once pinned with sources") and it has never been pinned.
   Tier W cannot be scored without it.
3. **`C_thr(L)`**, the Weber threshold as a function of adaptation luminance, at
   both the photopic and the scotopic point, cited — PANEL.md's Metrics table
   requires **both** regimes every run and this cycle must restore that.
4. **The angular subtense** of the volume and the corresponding threshold
   correction. Contrast threshold is size-dependent; a bar quoted without a
   subtense is not a bar.
5. **Which citation is being re-scored, and its original value** — so the output
   is a comparison against the program's own filed number, not a fresh
   assertion. This is the whole point of a re-score.
6. All of the above as **code constants with their source strings**, in the
   cycle's own module, committed before any run — not in prose (R24/R19
   discipline).

**What the ambient instrument needs re-verified before a single number off it is
trusted.** `lab/ambient.py` (`observer_profile:36`, `weber:53`,
`incoherent_sum:59`, `contrast_from_runs:73`) has not been invoked by any
experiment since exp-100 — fifteen cycles. PANEL.md's own Phase-4 house rule
("new machinery ⇒ a new suite stage with at least one absolute identity gate
BEFORE results are trusted") binds here: after fifteen cycles of dormancy across
an engine that has changed, this is new machinery.

1. **Absolute identity gate:** re-run `weber` / `contrast_from_runs` /
   `observer_profile` against exp-100's own committed inputs and reproduce
   exp-100's committed outputs **bit-exactly**. Any drift halts the cycle before
   a threshold is scored. This is exp-115's own MF-12 pattern, which worked
   (10/10 PASS) and should simply be copied.
2. **A positive control — the non-negotiable half.** A dormant instrument that
   returns a plausible number is not a verified instrument. Feed it (a) a
   synthetic scene whose Weber contrast is known analytically and confirm it
   returns the analytic value, and (b) a second scene deliberately **below**
   threshold and confirm it returns "below." The instrument must be shown able
   to produce the reading that means *fail* before it is allowed to produce one
   that means *pass*. `lab/ARTIFACTS.md`'s own invariant — a silent gate and an
   absent gate produce identical observations — is the reason, and it is the
   invariant this program has now paid for repeatedly.
3. **Signature/interface check:** confirm the instrument's expected inputs still
   exist in the shape it wants after exp-101→115's `lab/` changes. Silent
   signature drift is the failure mode a numeric check will not catch.
4. **Bench trust suite re-run with the platform-named console record
   committed** (`VALIDATION.md` docket-14), exactly as exp-115 did in
   `data/trust_suite_bench_20260905T235042Z.txt`; add an ambient stage if none
   exists, so future cycles inherit a gate rather than a habit.
5. **Persist both photopic and scotopic rows** even where only one is the design
   target, per PANEL.md's Metrics table.

**Cost, and how I gate it.** Steps 1–3 are **zero FDTD** — they run over
already-committed captures. If exp-100's captures are committed, the entire
re-score is zero FDTD and the cycle costs one shift. If they are not — and this
program has a documented pattern of unpersisted captures (exp-114's r=234
pickles) — the re-score needs three production scenes at r=156/cpl=25, which
this cycle's own measured bench rate prices at **1185.5 s (19.8 min)**, `1304 s`
with the `1.10` margin, against `COST_GATE_TOTAL_S = 10800`: **12.1% of the
bound.** I will project it with `chunk_runner115`-style upstream gates using the
bench-native per-step rate, not any cloud prior, and I will say so in Phase 1.

**What I will not do.** I will not let Iteration 93 become a sixteenth
consecutive instrument cycle. Item 1 is the constraint-3 re-score; item 2 is the
T1 ledger, which is phenomenon-facing and costs nothing; item 3 is bookkeeping
that rides free with no falsifiable question of its own. If the cycle can carry
only two, item 3 is what I drop — and I will number it as a decline (R25), not
absorb it silently. I will also carry forward, in Phase 1, the honest statement
this seat owes: exp-115 measured the instrument accurately and the instrument is
not the problem.

---

## 5. Summary (≤150 words)

**PARTIAL.** The measurement is sound: all six readings, both pairwise `G`, the
drift rates, the two-point interval and all four composition booleans reproduce
bit-exactly from the persisted data. ABBA worked — I measured the mean-midpoint
lag at 1.11 s against ABAB's 802.8 s, a 722× reduction. `d_rep` is exactly the
grid-differential log-drift, so common-mode drift cancels in it identically.
Three findings limit the cycle: M3's bar is a cloud figure the bench's own data
(+1.66%/−1.29%, opposite signs) supersedes — re-anchored, M3 flips and M6
becomes directional-only; a second committed bench session (`G = 2.2922`,
+2.81%) is analysed nowhere; and `k_B = 2.9955` — pure `N²`, the pre-R28
exponent — ships under the label "CONFIRM: exponent generalizes." Contention is
a demonstrated, signed, partial explanation of the 22.2% cloud gap, insufficient
at 2.81%. T1 N/A verified structurally. Energy-ledger N/A correct; 65%/47%
reproduces source-anchored.

*(149 words.)*
