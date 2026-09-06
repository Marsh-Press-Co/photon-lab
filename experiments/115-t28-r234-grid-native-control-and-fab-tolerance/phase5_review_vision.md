# Phase 5 — review: VISION SCIENCE

**Cycle:** Panel Iteration 92, exp-115
(`115-t28-r234-grid-native-control-and-fab-tolerance`).
**Seat:** VISION SCIENCE. Fresh context. Blind to every other seat's Phase-5
output. Read: `PANEL.md` in full (incl. the Iteration-92 Metrics scope
amendment), `LOGBOOK.md` RULED OUT R1–R34 + ESTABLISHED + LIVE THREADS
T1–T28 + the Iteration-92 record and its CHECKPOINT entry, `PLAN.md` 1–90,
this cycle's `phase1_proposal.md` / my own `phase2_critique_vision.md` /
`phase2_redteam_audit.md` / `NOTES.md` / `run115.py` / `analyze115.py` /
`results.json` / `data/`, and `lab/ambient.py`, `lab/glare_sidecar.py`,
`lab/caveat_lint.py` + config.
**No git state changed. No simulations run.** Every figure below was
recomputed this session in pure python against committed JSON and committed
source, or re-derived from primitives.

---

## 1. Verdict

# PARTIAL

**T1 escape route: N/A** — correctly and structurally, for both halves
(`results.json:result_text`; `run115.py::DISCLAIMER_115`). Nothing in this
cycle is constraint-3 progress, and the cycle says so in the one string it
asserts on both sides.

**What earned a CONFIRM and did not get one.** The measurement is sound.
Both defects I filed at Phase 2 landed as coded fixes and I verified both
live (Findings 1–2). The declared falsifiable heart returned a scored
verdict — M5 CONFIRM, `rel_dev = 0.0815428277734715` — through the
unmodified `R114` classifier via the MF-5 log inversion, with its
code-assert firing. The sidecar shipped **REPRODUCED**, corrected, and with
its scope written into the sentence R21 sends forward. The first r=234-grid
control reading in this program's history exists.

**Why PARTIAL.** The cycle's *prose* is not finished, and prose is the half
my seat scores. `NOTES.md:619-625` still reads `## Phase 4 — Results /
(pending)`. `LOGBOOK.md:25090-25127` and `PLAN.md:40-55` still report the
**interrupted first session's superseded numbers** as this cycle's readings —
including an M7 `excess` of the **opposite sign** to the filed result
(Finding 3). One of the three declared deliverables (M8, Tier-1 item 2) has
no headline anywhere in Result prose, which is R21's exact shape and R21
carries a third-occurrence auto-fire clause (Finding 4). M7's one-line
result summary is internally contradictory as written (Finding 5). M3's
verdict — the boolean that sets `m6_directional_only` — does not survive
correction by the cycle's own persisted drift rates (Finding 7, the
strongest thing I found). And a free, already-committed cross-session
replicate of the cycle's central quantity sits unanalysed on disk
(Finding 8).

None of these is a defect in the measurement. All of them are defects in
what a future citation will read. That is the difference between a CONFIRM
and a PARTIAL at this seat.

---

## 2. Findings — numbered, re-derived

Every number in this section was produced by executing code or reading
committed JSON this session. Where I could not reproduce something, I say so.

### 2.0 — Re-derivations that CONFIRM (the arithmetic spine)

Recomputed from `results.json:readings` primitives, not restated:

| Quantity | Recomputed | Filed | Match |
|---|---|---|---|
| `per_step_s`, all six readings | `total_wall_s / total_steps` | as filed | **exact, 6/6** |
| `G_short` | `0.11239203476905822 / 0.04858939027786255` | `2.3130982736423493` | exact |
| `G_pair1` (`U234/U156`) | `2.2296275647790664` | same | exact |
| `G_pair2` (`U234b/U156b`) | `2.2622534289060674` | same | exact |
| `G_sustained` (ABBA mean) | `2.245940496842567` | same | exact |
| `d_dur` | `0.02903368938753793` | same | exact |
| `d_rep` | `0.01463287619976741` | same | exact |
| `exponent_B = ln(1.5·G)/ln(1.5)` | `2.995546218006855` | same | exact |
| `measured_ratio = 1.5·G` | `3.3689107452638507` | same | exact |
| `rel_dev` vs `1.5**k = 3.6680107109370383` | `0.0815428277734715` | same | exact |
| `T = G/G_E` | `0.8180425684476521`, `\|T−1\| = 0.1819574315523479` | same | exact |
| `excess = G/2.25 − 1` | `-0.0018042236255256805` | same | exact |
| `k_B = 3 + ln(G/2.25)/ln 1.5` | `2.995546218006855` (= `exponent_B`, as it must) | same | exact |

`geom_identity.pass_ = True`; `identity_gate` 10/10 PASS
(`data/cg_session2.log`); `n_sim_run_calls = 18 = n_sim_run_calls_expected`,
`repeat_skipped = False`; `total_wall_s = 3700.5 s` against
`COST_GATE_TOTAL_S = 10800` — a 65.7% margin, better than the 43.2%
worst-anchor projection.

**The R19 call-count invariant and the R27/R28 gate both did their job and
neither was load-bearing this run** — stated so the record does not imply
they were tested.

### 2.1 — FINDING 1: MF-5 landed, and it verifies in a way nobody could have seen at Phase 2

`run115.py:326-333` defines `exponent_from_g(g) = log(1.5·g)/log(1.5)`;
`run115.py:335-347` `classify_m5()` feeds **that** to
`R114.classify_kappa_exponent_check()` unmodified and asserts
`abs(result["measured_ratio"] − 1.5·g) < 1e-12` (`run115.py:341`). I executed
`python run115.py --selftest` this session:

```
MF-5 self-test: classify_m5(G_E=2.74550565394726)
  exponent_B      = 3.490880835092507  (exp-114 filed exponent_234 = 3.490880835092507)
  measured_ratio  = 4.11825848092089  (filed 4.11825848092089)
  rel_dev         = 0.12274985147707763  (filed 0.12274985147707763)
  PASS: reproduces exp-114's filed rel_dev=0.12275 to <1e-9 (delta 0.000e+00)
  MF-5 counterfactual: rel_dev=0.44796720567305326 -> REFUTE
SELFTEST PASSED
```

**The new part, which is the point of raising this at Phase 5 rather than
just ticking the fix.** The counterfactual is verified against
`G_E = 2.7455`, where the broken route yields REFUTE and the break is
obvious. Evaluated instead at **this cycle's own measured `G`**, the broken
route yields:

```
1.5 ** 3.3689107452638507 = 3.9195457207972333
rel_dev = |3.9195457 − 3.6680107| / 3.6680107 = 0.06857532043463888  ->  CONFIRM
```

So on the data this cycle actually took, the un-fixed invocation would have
returned **CONFIRM** — the same verdict label as the correct route, from a
`measured_ratio` wrong by 16.3% (`3.9195` vs `3.3689`). Nothing downstream
would have flagged it: the label agrees, the band is cleared, the persisted
`rel_dev` merely reads `0.0686` instead of `0.0815`. That is `lab/ARTIFACTS.md`'s
own invariant one level up — *a silent gate and an absent gate produce
identical observations* — in its false-positive form: **a wrong computation
that agrees with the right one is indistinguishable from correctness by
verdict alone.** The fix was load-bearing not because it changed this
cycle's verdict but because without it the record would have carried an
unfalsifiable number under a true label. Credit where due: MF-5 was adopted
on the Phase-2 argument, before this data existed.

### 2.2 — FINDING 2: MF-14 landed on both halves; the residual is real and I re-measured it

Executed `python lab/caveat_lint.py` this session. **Exit code 0.**
Output tail: `16 caveat(s) checked, 0 required-site failure(s).` (was 15
entries and 0 failures at Phase 2 — the registry has moved for the first
time since exp-071/Iteration 48.)

Both blindnesses are closed and both gating halves PASS on this cycle's
files:

```
[exp061-t18-evidentiary-tier-propagation]
  PASS  experiments/115-.../NOTES.md      (matched: 'WebSearch.snippet')
  PASS  experiments/115-.../run115.py     (matched: 'WebSearch.snippet')
  PASS  experiments/115-.../analyze115.py (matched: 'WebSearch.snippet')
[exp115-t28-fabrication-tolerance-bound-certified-resolution]
  PASS  experiments/115-.../NOTES.md      (matched: 'certified at margin=32 only')
  PASS  experiments/115-.../run115.py     (matched: 'certified at margin=32 only')
  PASS  experiments/115-.../analyze115.py (matched: 'certified at margin=32 only')
```

**The residual, measured rather than asserted.** I counted WARNs per entry
across the whole run:

```
   663  exp065-steps1400-unsettled-plane-channel
   520  exp071-t28-absorb-pad-confound-and-resolution-floor
   449  exp070-t28-named-constant-null-control
   208  exp060-p10-fresnel-not-diffraction
   106  exp061-t18-evidentiary-tier-propagation
    ...
    37  exp115-t28-fabrication-tolerance-bound-certified-resolution
  TOTAL 2495 WARN, exit 0
```

`NOTES.md:213-228` already discloses the mechanism (trigger terms are
discovery-only; `run_registry` sums only `site_results` failures) and names
the fix as out of this cycle's authorization. Correct, and correctly written
down. What the disclosure does not say, and what my discipline is the one to
say: **2495 same-severity alerts with no failure state is not a warning
channel, it is a noise floor.** Signal detection has a criterion as well as a
sensitivity; a channel whose hit rate and false-alarm rate are both
saturated conveys zero bits to the observer regardless of how correct each
individual line is. Widening the T18 entry's triggers (correctly) *raised*
that floor. So MF-14 bought real gating on three files and simultaneously
made the advisory half less readable than it was.

**And the specific live gap, which is one line of config to close.** Of the
new entry's 37 WARNs, exactly two are on files where the bound will actually
be cited forward:

```
WARN  candidate site (trigger 'fabrication.tolerance' found, caveat phrase absent): LOGBOOK.md
WARN  candidate site (trigger 'fabrication.tolerance' found, caveat phrase absent): PLAN.md
```

The other 35 are prior cycles *naming the debt as undone* — benign. So the
entry gates the three files that already carry the wording and can only warn
on the two that will carry the citation. **Recommendation, this shift:** add
`LOGBOOK.md` and `PLAN.md` to `exp115-...`'s `required_sites` at the moment
the Iteration-92 Phase-5 close writes the bound into them. That is R23's own
single-source-of-truth principle applied where it bites, and it costs a
two-line edit.

### 2.3 — FINDING 3: the Result prose a human reads is a different run from the one in `results.json`

`NOTES.md:619-625`:

```
## Phase 4 — Results
(pending)
## Phase 5
(pending)
```

`LOGBOOK.md:25090-25127` and `PLAN.md:40-55` report the **session-1
(interrupted)** readings as this cycle's Phase 4. Side by side against the
filed results:

| Quantity | LOGBOOK/PLAN (session 1) | `results.json` (session 2, scored) | Δ |
|---|---|---|---|
| `S156` per-step | `0.050909` | `0.04858939027786255` | −4.56% |
| `S234` per-step | `0.117121` | `0.11239203476905822` | −4.04% |
| `U156` per-step | `0.052374` | `0.04970505291927912` | −5.10% |
| `U234` per-step | `0.120053` | `0.11082375609762692` | −7.69% |
| `G_short` | `2.3006` | `2.3130982736423493` | +0.54% |
| `G_sustained` | `2.2922` (one pair) | `2.245940496842567` (ABBA mean) | −2.02% |
| `excess = G/2.25−1` | **`+0.0188`** | **`−0.0018042236255256805`** | **sign flips** |
| `\|T−1\|` | `0.165` | `0.1819574315523479` | +10.3% |

Session 2 is a clean full re-run — `data/cg_session2.log` shows the identity
gate 10/10, all six readings, `18 Sim.run calls (expected 18)`,
`repeat_skipped=False` — so the numbers in `results.json` are the right ones
and the ABBA cancellation holds within it. The defect is purely that the
record has not caught up. **Every one of PLAN.md's and LOGBOOK's quoted
figures is superseded, one of them in sign**, and both documents still read
`INTERRUPTED` with a resume recipe for a resume that already happened and
was better than either branch the recipe offered (a full clean re-run rather
than repeat-only or degraded scoring).

This is the plainest R21/R19-family finding available: the prose a future
citation reads does not match the persisted result. It is entirely
fixable this shift, before the Iteration-92 close freezes.

### 2.4 — FINDING 4: M8 — a declared deliverable with no prose headline (R21, third-occurrence clause)

I probed `results.json:result_text` for every M8 quantity:

```
OUT  sensitivity_short_reading      OUT  4.4310988   OUT  0.20803869
OUT  sensitivity_v2_with_measured_G OUT  3.2113910   OUT  0.12448699
OUT  straddle_still_open            OUT  0.6635
```

Tier-1 item 2 — one of this cycle's three declared deliverables — appears in
Result prose **not at all**. That includes
`sensitivity_v2_with_measured_G_DO_NOT_SCORE`, which is the *only* M8 field
that could not be computed before the run and whose finding is
`straddle_still_open = True` at the measured `G` (measured
`3.2113910881603176`, signed dev `−0.12448699274928553`, boundary
`G ≥ 2.5652851279677367`, `G = 2.2459 < 2.5653`).

R21 (`LOGBOOK.md:881-912`) is exact about this: *"a persisted post-run
analytic sidecar field's own headline finding must be stated inline in a
cycle's own Result section, not merely persisted to `results.json`"*, and it
carries a **standing forward-elevating clause**: *"a THIRD occurrence … on
this or any T28-adjacent channel, in any form, fires Checkpoint criterion 4
automatically."* Both founding instances (exp-099, exp-100) are on the
NETD/thermal channel; this is T28-adjacent and is the same shape.

**My ruling, and I state it as a ruling rather than a flag because R21's
clause is automatic.** This is a genuine third occurrence *in substance*. It
does **not** fire, on the precedent every prior R-rule set for its own
founding and near-founding instances: it was caught blind, inside this
cycle's own Phase-5 review layer, **before** the LOGBOOK Iteration-92 close
freezes — and the DISCLAIMER already states the withdrawal, so a reader has
the boundary even without the number. The condition of non-firing is that
the Director states M8's headline in Result prose this shift. If the
Iteration-92 close lands without it, the occurrence is post-freeze and
Red Team's Iteration-93 audit should treat it as fired.

Minimum sufficient sentence, offered so the fix costs nothing:
> **M8 (Tier-1 item 2), NOT scored:** at the measured `G = 2.2459405`, the
> v2 re-normalization gives `measured_ratio = 3.2113911` (signed dev
> `−0.1244870`), below the sign boundary `G ≥ 2.5652851` — **the v2 straddle
> remains OPEN**, as MF-8 pre-registered it would over 66.4% of M5's own
> CONFIRM band. The two pre-run sensitivities are unchanged: short-reading
> `rel_dev = 0.2080387` (AMBIGUOUS); v2 `measured_ratio = 3.2171956`,
> `−0.1229045` against the filed `+0.1227499` — opposite sides of
> `reference_ratio`.

### 2.5 — FINDING 5: M7's result line asserts two incompatible things at once

`run115.py:1237-1239` renders M7 as:

```
**M7:** excess=-0.001804, k_B=2.995546, N2_HOLDS (model comparison: constant-k)
```

`run115.py:435-436` computes `favoured` as a bare nearest-neighbour with **no
rejection test**:

```python
model["favoured"] = ("UNDERPOWERED -- no model declared favoured" if m7_underpowered
                     else ("constant-k" if d_k < d_eps else "constant-eps"))
```

and `m7_underpowered` gates only on `d_rep`, which measures within-session
scatter, never distance-to-model. Recomputed this session:

| | prediction for `G` | `\|G_meas − G_model\|/G_model` |
|---|---|---|
| constant-`k` (in force) | `2.4453404739580256` | **`0.0815428277734715`** |
| constant-`ε` | `2.5941375896334256` | **`0.13422460480982495`** |
| model separation | — | `0.060849242573798784` |

The measurement sits **8.15%** from one model and **13.42%** from the other,
both larger than the **6.08%** that separates them. `run115.py:439-442`'s own
persisted note says it plainly — *"N2_HOLDS requires BOTH candidate cost
models to be wrong"* — and it is right. So the single line a human reads
announces `N2_HOLDS` (both models wrong) and `constant-k` (one model
favoured) in the same breath. `favoured` is a "least-badly-rejected" label
wearing model-selection clothes.

This is my Phase-2 §4.5/§4.6 finding recurring one level down: MF-9 made the
*verdict* labels two-sided and mechanism-neutral and left the
`model_comparison` sub-field's label untouched. **One-line fix:** gate
`favoured` on a rejection test as well as a power test — if
`min(d_k, d_eps) > separation`, emit `NEITHER -- both models rejected at
larger than their own separation`.

### 2.6 — FINDING 6: the reproduction gate is stated at `<1e-12` and coded at five different bars

`NOTES.md:591` and `run115.py:1160`, identically, in the frozen
pre-registration: *"every cited figure is recomputed in `analyze115.py` from
its source `results.json` and asserted equal to `<1e-12` relative."* The
coded bars (`run115.py:620` default, then per call site) are:

```
tau_true@cpl20 / @cpl25                       bar 1e-02   (TAU_TRUE_REPRO_REL_BAR, run115.py:529)
tau_true bit-identity                         bar 1e-12
loss tangent / thickness identities           bar 1e-15
exp-112 / exp-114 sigma_scat deltas           bar 1e-09
exp-108 item_ii r156 mean/std                 bar 1e-03   (run115.py:703)
exp-108 item_ii r312 mean/std                 bar 1e-03   (run115.py:704)
exp-110 r156 / r312 floor-gated local_rel     bar 1e-12
```

The two gated at `1e-03` are the ones carrying the sidecar's load-bearing
**"RESOLVED, not floor-limited"** conclusion (MF-2's substituted differential
floor, `4.47×`/`11.70×`). They are gated **nine orders looser** than the
pre-registration's stated figure. The bars *are* persisted per check in
`results.json:sidecar_m9.reproduction_checks[*].rel_bar`, so this is
disclosed at the JSON layer and overstated at the prose layer — R18's exact
shape (documented scope vs. code), and it survived into the frozen
predictions text.

Not load-bearing for any verdict: every check passes with margin
(worst `rel = 1.564e-04` against `1e-03`), and `1e-12` was never achievable
for figures quoted to five significant digits. The fix is honesty of
statement, not a tighter bar: replace *"asserted equal to `<1e-12`"* with
*"asserted at a per-check bar, persisted with each check
(`1e-15`…`1e-2`); the two differential-floor ratios are gated at `1e-3`
because their sources are quoted to five significant digits."*

### 2.7 — FINDING 7 (the strongest): M3's verdict does not survive the cycle's own drift correction, and M3 gates M6

M3 read `G-DURATION-INVARIANT` at `d_dur = 0.02903368938753793` against
`M3_INVARIANT_BAR = R_DEG/2 = 0.037982123779318644` (`run115.py:204`). That
verdict sets `m6_directional_only = (m3_verdict != "G-DURATION-INVARIANT")`
— so it is the boolean deciding whether M6's `AMBIGUOUS` is reported as a
scored verdict or as directional-only.

MF-6(c) made this cycle persist same-grid drift as a **rate per unit elapsed
time**, precisely because it matters. From `results.json:drift`:

```
r=156 : relative_rate_per_s = -4.552366720982913e-06   (later reading FASTER)
r=234 : relative_rate_per_s = +1.8661564961051803e-06  (later reading SLOWER)
```

**The two grids drift in opposite directions**, `−1.639%/h` and `+0.672%/h`
— which is *itself* the grid-dependent degradation M3 exists to detect,
sitting in the same `results.json`. Composing them:

```
d(ln G)/dt = 1.8661565e-06 − (−4.5523667e-06) = 6.418523e-06 /s  = +2.311 %/hour
S-pass effective midpoint (mean of S156, S234 mids)  = 1788669759.8
U-pass effective midpoint (mean of the four U mids)  = 1788671660.1
elapsed gap                                          = 1900.3 s (0.528 h)
expected drift contribution to G over that gap       = +1.2197 %
measured  G_sustained/G_short − 1                    = −2.9034 %
drift-corrected duration effect                      = −4.1231 %
```

`0.041231 > M3_INVARIANT_BAR = 0.037982` and `< M4_NOISY_BAR = 0.075964`
→ **PARTIAL**, not `G-DURATION-INVARIANT`. The drift and the duration effect
push in *opposite* directions, so the raw `d_dur` is a **lower bound** on the
duration effect, and the cycle scored the flattering end of it.

**What I claim and what I do not.** I do **not** claim M3's filed verdict is
wrong: the bands were honestly pre-registered, drift correction was not
pre-registered, and applying it post-hoc to move a verdict would be exactly
the estimator-switching this program ruled on at Iteration 1. What I claim
is narrower and, I think, harder to dismiss: **M3's verdict is not robust to
a correction computed entirely from this cycle's own persisted fields, the
margin is 76% of the way to its bar before correction and past it after, and
the whole M3 → `m6_directional_only` → "M6 is a scored verdict" chain
inherits that fragility.** Two further honest caveats: each drift rate is a
two-point estimate from a single same-grid lag, so it carries no uncertainty
of its own; and the correction assumes log-linearity in elapsed time across
62 minutes, which two points cannot test.

**Second, smaller, same family.** `d_dur / d_rep = 1.984` — the duration
effect is 2.0× the run-to-run scatter. A label reading `G-DURATION-INVARIANT`
tells a reader "no effect" where the measurement says "a 2.9% effect, resolved
at about 2× scatter, below a bar set at half of a 7.6% *cloud-measured*
anchor." MF-9 made the label mechanism-neutral; it did not make it
magnitude-honest. **One-line fix:** `G-DURATION-SHIFT-BELOW-BAR (−2.90%, bar
3.80%)`, and report the drift-corrected figure alongside as
`DO_NOT_SCORE`.

### 2.8 — FINDING 8: a free cross-session replicate of `G` is committed and unanalysed

`data/readings_session1_interrupted_20260905T2354Z.json` holds **four
complete readings** from an independent session on the same bench 4.75 h
earlier (`S156`, `S234`, `U156`, `U234`; `U234b` was in flight when the host
hung). It is committed. It is used nowhere: `results.json` has no field
referring to it, and `result_text` contains neither `session1` nor
`interrupted`.

Recomputed from it this session against session 2:

| | session 1 | session 2 | s1/s2 |
|---|---|---|---|
| `S156` per-step | `0.05090947675704956` | `0.04858939027786255` | `1.0477` |
| `S234` per-step | `0.11712120278676351` | `0.11239203476905822` | `1.0421` |
| `U156` per-step | `0.05237354392696442` | `0.04970505291927912` | `1.0537` |
| `U234` per-step | `0.12005272514222741` | `0.11082375609762692` | `1.0833` |
| **`G_short`** | **`2.3005776183025777`** | **`2.3130982736423493`** | **`1.00544`** |
| **`G_sustained` (one pair)** | **`2.2922398627376155`** | `2.245940496842567` (ABBA mean) | **`0.97980`** |

**The absolute per-step rates differ by 4.2–8.3% between sessions on one
machine; `G` differs by 0.54% (short) and 2.02% (sustained).** That is a
direct, same-machine, cross-session measurement of exactly the invariance M6
tests across machines — the decomposition QUANTUM's B8 said M6 with `N = 2`
machines cannot perform, sitting free on disk. Put against the machine axis:

```
within-session repeat scatter (d_rep)            1.46 %
between-session, same machine (G_short)          0.54 %
between-session, same machine (G_sustained)      2.02 %
between-MACHINE (bench vs cloud, |T−1|)         18.20 %
```

The between-machine difference is **9–34× the between-session difference on
the same machine.** That materially strengthens the reading that M6's
`AMBIGUOUS` is a real machine property rather than session noise — which is
the single most citable scientific content this run produced, and it is
currently unwritten.

**The caveat that keeps it honest, and it is not small:** session 1's `U234`
is the largest deviation of the four (+8.33%) and is the reading immediately
preceding the host hang, so a contention ramp toward the fault cannot be
excluded. This should therefore be persisted as `..._DO_NOT_SCORE` and
reported as a bound and a direction, never as a scored verdict. That is
still worth far more than leaving it on disk.

### 2.9 — FINDING 9: what M5's CONFIRM and M6's AMBIGUOUS jointly mean, which nothing states

```
bench :  measured_ratio = 3.3689107452638507,  rel_dev = −0.0815428277734715  (below reference)
cloud :  measured_ratio = 4.11825848092089,    rel_dev = +0.12274985147707763 (above reference)
reference_ratio = 3.6680107109370383
between-machine spread |G_bench − G_E|/G_E = 0.18195743155234795
M6 TRANSFERS bar = 0.152950039837078
```

**Two machines land on opposite sides of `reference_ratio` and both score
CONFIRM, while their mutual difference exceeds M6's own transfer bar by 19%.**
The CONFIRM band (`rel_dev ≤ 0.15`, i.e. 30% wide in ratio space) is wider
than the between-machine spread it is required to survive. In my own
discipline's terms this is a discrimination-threshold problem: the
classifier's just-noticeable difference is coarser than the differences in
play, so "CONFIRM" is not evidence of agreement — it is evidence that the
instrument cannot tell these two measurements apart.

This is structurally the same shape as the v2 straddle the cycle correctly
withdrew a claim about (MF-8), re-instantiated on a new axis, and it
compounds with MF-7(b)'s pre-registered statement that pure `N²` (`k = 3.0`,
`rel_dev = 0.0799`) also lands inside CONFIRM. The bench measured
`k_B = 2.995546218006855` — **0.149% from exactly 3.0** — so this run's
central estimate *is* the pre-R28 exponent that `KAPPA_COST_EXPONENT`
replaced, and the classifier calls that a CONFIRM of `k = 3.2053`.

The pieces are all in `result_text` (the CONFIRM, the `N2_HOLDS`, the
`k = 3.0`-inside-CONFIRM sentence, the M6 AMBIGUOUS). The *joint* reading is
not, and it is the reading a future cycle needs. **Recommended sentence for
Result prose:**
> The bench's `G = 2.2459405` and exp-114's cloud `G_E = 2.7455057` sit on
> **opposite sides** of `reference_ratio` and **both score CONFIRM**, while
> differing from each other by 18.20% — above M6's own 15.295% transfer bar.
> M5's CONFIRM band is therefore wider than the between-machine spread it
> must survive, and this cycle's own central estimate (`k_B = 2.9955`) is
> 0.15% from the pre-R28 exponent `k = 3.0`.

### 2.10 — On the assigned question: does PANEL.md's D1 amendment now say what the practice is, honestly?

**Mostly yes, and I want to say that first** — it names the count, names
exp-101 as the start, points at `lab/ambient.py`, and explicitly declines to
endorse the practice as permanent. That is the opposite of drift-by-
concealment, and it is more than the charter said before. Three defects:

1. **The amendment's own class test is self-certifying.** *"any iteration
   whose proposal names a mechanism or a T1 escape route"* — the exempt
   class is decided by a string the proposal writes **about itself**, and
   twelve consecutive proposals have written `NONE / N/A`. A cycle now
   becomes exempt from the seven metric rows by declining to name a
   mechanism, which is precisely what a drifting program does. **Fix, one
   line:** the class is assigned by the **Director in the Iteration entry**,
   not by the proposal, and PANEL.md carries a standing counter —
   *"consecutive governance-class cycles: N"* — so the drift is a number on
   the charter page a fresh seat reads, not a grep a seat has to think to
   run. Criterion 5 already treats a run of non-advancing cycles as
   reportable; this is the same instinct applied to a class that criterion 5
   does not reach.

2. **It amends the sentence but not my seat's duty, which is now vacuous on
   the majority class of cycle.** `PANEL.md:86-87` still reads, unamended,
   *"Duty: pin numeric thresholds, with sources, BEFORE any run that scores
   against them"*, and `PANEL.md:150-151` still reads *"VISION SCIENCE pins
   the numeric pass/fail thresholds per experiment, cited, before the run."*
   On a governance cycle there is nothing to pin, and the charter does not
   say so — so a fresh VISION seat reads a duty it cannot perform and either
   invents one or goes quiet. Both have happened. **Fix:** add to the
   amendment — *"on governance-class cycles VISION's threshold duty is
   discharged by the DISCLAIMER's constraint-3 N/A sentence, and by nothing
   else."*

3. **The count in the charter goes stale by one every cycle.**
   `PANEL.md:163` says *"unrun since exp-100 (14 cycles)"*; with exp-115 it
   is fifteen. I re-verified the underlying grep this session —
   `grep -rln "weber(\|contrast_from_runs\|observer_profile" experiments/*/*.py`
   returns nothing after `experiments/100-...`; `lab.ambient` is *imported*
   as late as exp-107, but no Weber entry point is called. Write it as
   *"since exp-100 (Iteration 77)"* with no count.

**And the D2 ruling is the right call and I will say so plainly** — it
applies to item 10 exactly the standard that was applied to item 5, it is on
the record in three places (`PANEL.md:164-167`, `LOGBOOK.md` CHECKPOINT
entry, `PLAN.md:33-35`), and it removes the ordering mechanism I named at
Phase 2 as the thing through which constraint 3 slips. I take the item.

---

## 3. Defects, by R-number

| # | Defect | Rule | Severity | Fix cost |
|---|---|---|---|---|
| D1 | `NOTES.md:619-625` Phase 4/5 `(pending)`; `LOGBOOK.md:25090-25127` and `PLAN.md:40-55` report session-1's superseded readings as this cycle's, one figure (`excess`) **sign-flipped** | **R21**, R19-family | **high** — this is the prose a future citation reads | desk, this shift |
| D2 | M8 (Tier-1 item 2, incl. `sensitivity_v2_with_measured_G_DO_NOT_SCORE` / `straddle_still_open=True`) has no headline in Result prose | **R21** + its third-occurrence auto-fire clause | **high**; does NOT fire *if* fixed pre-freeze (§2.4) | desk, one paragraph |
| D3 | M7 result line asserts `N2_HOLDS` (both models wrong) and `constant-k` (one model favoured) together; `favoured` has no rejection test (`run115.py:435-436`) | R24-family / legibility (my Phase-2 §4.5–4.6, recurring) | medium | 2 lines of code |
| D4 | Pre-registration states a `<1e-12` reproduction gate (`NOTES.md:591`, `run115.py:1160`); coded bars are `1e-15`…`1e-2`, with the two differential-floor ratios at `1e-3` (`run115.py:703-704`) | **R18** | low — disclosed in JSON, overstated in prose | desk |
| D5 | M3's `G-DURATION-INVARIANT` does not survive correction by the cycle's own persisted drift rates (→ PARTIAL at `4.12%` vs bar `3.80%`); the label also asserts invariance at a `−2.90%` effect that is 2.0× run-to-run scatter; M3 gates `m6_directional_only` | R17 (anchor/label) + R24 (a stated consequence wired into the classification) | **high** — it is the only finding that touches a scored chain | desk + one `DO_NOT_SCORE` field |
| D6 | The two grids' drift rates have **opposite signs** (`−1.64%/h` vs `+0.67%/h`) — the grid-dependent degradation M3 exists to detect — persisted and uninterpreted | R21 (persisted ≠ narrated) | medium | desk |
| D7 | `data/readings_session1_interrupted_*.json` (4 complete readings, a free same-machine cross-session replicate of `G`) is committed and unanalysed | R21-adjacent; a lost measurement, not a false one | medium | desk arithmetic |
| D8 | M5 CONFIRM + M6 AMBIGUOUS jointly = two machines straddling `reference_ratio`, both CONFIRM, spread (18.20%) > transfer bar (15.295%) — unstated | R21 | medium | one sentence |
| D9 | `lab/caveat_lint.py` emits 2495 WARNs at exit 0; the new exp-115 entry can only WARN on `LOGBOOK.md`/`PLAN.md`, the two files that will carry the forward citation | **R23** (disclosed as a TODO at `NOTES.md:213-228`, correctly) | medium | 2-line config now; code change later |
| D10 | `PANEL.md`'s D1 amendment: self-certifying class test; VISION's threshold duty left vacuous and unamended; a hardcoded cycle count that goes stale | governance | medium | 3 lines of charter |

**Not defects — stated so the record does not read as uniformly critical.**
MF-5, MF-6(a/b/c/e), MF-9, MF-10, MF-12 and MF-14 all landed as code and all
verify: ABBA was not cosmetic — I measured the two same-grid lags at
**+804.65 s** and **−802.43 s**, symmetric to **0.276%**, so the mean of the
two pairwise `G` cancels linear drift to first order exactly as EM's A3
argued it would. The identity gate is a real absolute gate (`build_sim`
source segment byte-identical, 10/10). The bench trust suite is committed
with its platform named, and **stage 9 — the ambient instrument's own gates
— is green on the bench, 13/13**, which matters directly for Iteration 93.
`DISCLAIMER_115` (3788 chars) is verified a literal substring of **both**
`predictions_text` and `result_text` in the committed `results.json`, with
asserts at `analyze115.py:259` and `:277` plus two re-invocable call sites in
`run115.py` — **R23's First Addendum is discharged, and this is the first
cycle where I can say that from the artifact rather than from the promise.**

---

## 4. Ranked top-3 candidate directions

Item 1 of Iteration 93 is fixed by D2 (my constraint-3 re-score). These are
**items 2–3 of Iteration 93 and item 1 of Iteration 94.**

### #1 (Iteration 93, item 2) — Decompose `G`'s variance: score the free session-1 replicate, then add one third runner

**Why first.** This cycle's own idealization 3 concedes M6 measures machine
transfer with `N = 2` — *"the minimum that can detect a difference, not enough
to characterize a distribution"* — and QUANTUM's B8 adds that with one
protocol per machine, M6 cannot separate a machine factor from a session
factor. **The separating datum already exists and is already committed**
(§2.8): same machine, different session, `G` stable to 0.54–2.02% while
absolute rates move 4.2–8.3%. Scoring it converts M6 from an unresolvable
`AMBIGUOUS` into a bounded three-level decomposition (within-session 1.46% ·
between-session 0.5–2.0% · between-machine 18.2%). A third runner's six
readings (~60 min, the measured cost of this cycle) would then give the first
figure this program has ever had for how `G` varies across machines rather
than between two of them.

**Deliverable:** a persisted variance decomposition and a pre-registered test
of whether M5's CONFIRM band (±15%) is wider than the machine spread it must
survive — with the direct consequence that if it is, the band is not fit for
purpose and must be re-derived from measured machine variance rather than
from R28's founding miss.
**Cost:** zero FDTD for the committed half; ~60 min for the third runner.
**Falsifier:** a between-session `G` spread comparable to 18% would refute
the reading that M6's AMBIGUOUS is a machine property and reassign it to
session noise — which is equally publishable and equally cheap.

### #2 (Iteration 93, item 3) — `KAPPA_COST_EXPONENT`: re-derive it per runner, or retire the single-constant model

**Why.** This is the direct scientific consequence of this cycle's primary
result and nobody has queued it. The bench measures `k_B = 2.995546`; exp-114's
cloud point implies `k = 3.490881`; the in-force constant is `3.205330` —
almost exactly the midpoint of two measurements that **disagree by 0.495 in
exponent**. M5 cannot separate them (`rel_dev` 0.0815 vs 0.1227, both CONFIRM),
and MF-7(b) pre-registered that it cannot separate `3.2053` from `3.0` either.
Every cost gate in this program projects through this constant. A cost
exponent that varies by ±0.25 with the runner is not a portable constant, and
continuing to project from it while knowing that is the kind of thing this
program's own R-rules exist to stop.

**Deliverable:** either a **runner-conditioned `k`** (measured on the runner
that will execute, which is now cheap: this cycle proves a 62-minute
six-reading burst determines it) or a documented retirement of the
single-constant model in favour of a measured per-session `G`, with the
cost-gate call sites updated.
**Cost:** zero new FDTD if #1's readings are reused; desk otherwise.
**Falsifier:** a third runner landing within ±0.05 of `3.2053` would defend
the constant and close the question.

### #3 (Iteration 94, item 1) — Close the caveat-registry's gating half, and gate the forward-citation surfaces

**Why last of the three, and why not lower.** It is pure governance, so it
ranks below two live measurements — but it is the item whose absence
manufactures the failures the other two would have to survive. Right now
`lab/caveat_lint.py` emits **2495 WARNs and exits 0**; the entry that has
fired Checkpoint criterion 4 **twice in one iteration** can finally see this
cycle's documents and still cannot fail on them; and the new exp-115 entry
gates the three files that already carry its wording while merely warning on
`LOGBOOK.md` and `PLAN.md`, the two that will carry the citation. `NOTES.md:213-228`
names this honestly and says the code change was out of authorization —
so the authorization is the item.

**Deliverable:** (a) an opt-in `gate_on_candidates: true` per entry in
`lab/caveat_lint.py`, so a trigger-hit-without-phrase can fail CI where an
entry's author asks for it; (b) `LOGBOOK.md` + `PLAN.md` added to
`exp115-t28-fabrication-tolerance-bound-certified-resolution`'s
`required_sites` — that half is two lines and should not wait for 94;
(c) a WARN triage pass, because a 2495-line advisory channel is below any
reader's detection threshold and the tool's own founding invariant applies
to noise as squarely as to silence.
**Cost:** ~20 lines plus config.
**Falsifier:** none — this is instrument work, and it should be labelled as
such rather than dressed as a question.

---

## 5. Pre-registration sketch for the D2 item — Iteration 93, Tier-1 item 1

*Written so ELECTROMAGNETISM can lift it into Phase 1. Thresholds pinned
before the run, with sources, per my charter duty. Every literature figure
below is **T18 tier — WebSearch-snippet synthesis, not primary-source
verified** — and that tier must travel to every claim point, not sit in a
methodology section.*

### 5.1 The target, named precisely

**The program's only-ever Tier-W/Tier-A constraint-3 citation is exp-047 /
Iteration 24, prediction P-G24-2** (`LOGBOOK.md:16788+`;
`lab/glare_sidecar.py`): the `graded_black_shell` absorber's measured Weber
contrast `C_MEASURED = −0.7209` (from Iteration 7 / exp-030 — **not**
exp-020's superseded `−0.686`), composed through the glare/adaptation
sidecar, **PASSes the LAB (cued) bar at all 36 grid points, worst case
`|C_eff|/C_thr = 5.865×10⁻³`, a ~170× margin** — carried under
`TIER_W_HEADLINE_LABEL`: *"clears the bench-scale glare-diluted SURROGATE of
Tier-W, pending the T8/T13/T14 near-field-to-witness-scale bridge — NOT a
witness-scale constraint-3 verdict."* The Tier-A companion is the same
article's photopic FAIL, which I re-derived this session as
`|C|/C_thr(3 cd/m²) = 144×` (lab, cued) and `36×` (field, uncued) — the
latter reproducing LOGBOOK's "×34" on the superseded `−0.686`.

### 5.2 The one thing EM must know before writing Phase 1: where the leverage is *not*

**A re-measurement of `C` cannot move the Tier-W verdict.** PHOTONICS proved
in closed form at Iteration 24 that at the worst-case point `c_thr` is pinned
at its photopic floor independent of `C`, so scaling `|C|` to its physical
ceiling of 1.0 moves the worst ratio only to `0.00814` — still 61×/246× below
MARGINAL/FAIL. I have not found an error in that argument and I am not
proposing one. **Therefore the re-score's leverage is entirely on the
threshold and glare-model side, which is this seat's, not the bench's.**

The fact that makes that leverage real, re-derived this session:

```
un-veiled night margin at the moonless-sky anchor L_B = 1.7e-4 cd/m2:
   C_thr(L_B, p=0.4) = 0.24984   ->  |C|/C_thr = 2.886x   (supra-threshold: FAIL)
   C_thr(L_B, p=0.5) = 0.66424   ->  |C|/C_thr = 1.085x   (MARGINAL)
```

`1.085` reproduces P-G24-1's own filed MARGINAL ratio exactly. **So darkness
alone does not hide this article; the entire Tier-W PASS is carried by the
glare veil.** And EM's own Iteration-24 Phase-5 finding is that all 36
headline points run at `L_v/L_B = 2.46×10⁴ – 2.2×10⁹`, far outside the
road-lighting literature's calibration range (small integers to low
hundreds), with `P-G24-4` evaluated at `θ = 0.5°`, **below** Stiles–Holladay's
own `1.0°` validity floor — the direction where `L_v` diverges and the
point-source assumption is weakest. That is the axis on which the program's
only Tier-W claim can actually move.

### 5.3 Thresholds I will pin, with sources

| # | Threshold | Value(s), re-derived this session | Source (all T18 tier) |
|---|---|---|---|
| **T-1** | Static contrast threshold, frozen T2 (exp-020, corrected exp-024): `C_thr(L) = 0.005·max[1,(L/3)^−p]`, clipped at 1; field bar = 4× lab bar; `p ∈ [0.4, 0.5]` | `C_thr(3) = 5.00×10⁻³` lab / `2.00×10⁻²` field; `C_thr(1.7×10⁻⁴) = 0.2498` (p=0.4) / `0.6642` (p=0.5) lab | Blackwell 1946; Rose 1948; CIE 19/2 (1981); Adrian 1989 (`lab/glare_sidecar.py:C_THR_SOURCES`) |
| **T-2** | Tier-W bar selection: **LAB (cued)** is Tier-W's default, because PANEL.md names the observer as the flashlight holder — the maximally cued case | field bar computed only as disclosed context, never as headline | glare_sidecar mandatory fix 4, Iteration 24 |
| **T-3** | Adaptation-luminance ladder | photopic anchor `L = 3 cd/m²`; night anchor `L_B = 1.7×10⁻⁴ cd/m²` (moonless overcast); committed ambient class band `10⁻⁵ – 10⁻³ cd/m²` | LOGBOOK Iteration 1, docket #7 committed table |
| **T-4** | Disability-glare veiling luminance: Stiles–Holladay `L_v = 10E/θ²`, validity `1° ≤ θ ≤ 30°` | **PRE-REGISTERED SCOPE LIMIT:** any point with `θ < 1°`, `θ > 30°`, or `L_v/L_B` outside ~`10²–10³` is scored **OUT-OF-CALIBRATION** and may not carry a headline | Holladay 1926; Stiles 1929; CIE 146:2002 |
| **T-5** | Adaptation persistence, Crawford equivalent background `L_eq(t)`, half-times ≥ 10 s at these exposures | used only to state that threshold elevation outlives the `θ⁻²` veil on sweep timescales | Crawford 1946; Hecht, Haig & Chase 1937; Pugh & Lamb 2000 |
| **T-6** | The `MARGINAL` band `[0.5, 2.0]` on `C_eff/C_thr` | **UNSOURCED** — my own Iteration-24 Phase-5 finding, never closed. **I will source it or retire it before the run**, and if it cannot be sourced the re-score reports **PASS/FAIL only**. My charter says "with sources"; an unsourced band is not one | — |
| **T-7** | **Decidability floor — a threshold too, and the one this program keeps forgetting is one.** A bucket may be reported only where the measured quantity exceeds the instrument's own uncertainty budget | T16 stacked angular-sampling × domain-construction swing = **7.80×10⁻⁴** on one physical article — **1.88× the largest PASS margin this program has ever measured** (`4.14×10⁻⁴`) and 15.6% of the lab bar; T28 `PAD` contribution raw `√(A_i²+A_q²) = 6.15×10⁻⁴ ≈ 0.123 C_thr`; T21 edge-diffraction fringe **magnitude never bounded at the ±35° geometry `C_MEASURED` actually uses** | LOGBOOK T16/T21/T28; PHOTONICS Iteration-24 Phase 5 |

### 5.4 Scenes

- **S-A — the positive control, MANDATORY and FIRST.** Reproduce the frozen
  citation: the exp-030 configuration (`graded_black_shell`, r=78-native
  ±35° fallback, N9, V-weighted 3λ, floor-corrected) re-run on the bench,
  required to return `C = −0.7209`. *Rationale, and it is the whole reason
  this scene leads:* the Weber entry points have not been invoked for **15
  cycles** and have **never** been invoked on this runner. Stage 9 is green
  on the bench (13/13, `data/trust_suite_bench_20260905T235042Z.txt`) — but
  every one of those gates is an identity, symmetry or Beer–Lambert anchor.
  **A green identity suite certifies self-consistency, not the correctness
  of a reading.** This program's own class rule is that an instrument is
  verified by reproducing a value known to exist, not by running without
  error. If S-A fails, everything downstream is withheld and **the failure
  is the cycle's result** — a 15-cycle-stale instrument is a finding.
- **S-B — the σ(I) OFF-state citation at its third convergence point.**
  exp-032/033's `off_pass` article (`τ_off ≈ 0.0065`), r=78-native, at
  **N33** — the point queued as Iteration 13's top priority and never run.
  The sequence on file: N9 → PASS (`C = −0.004586`); N17 → **MARGINAL**
  (`C = −0.005239`). N33 decides whether the program's first-ever
  constraint-3 PASS survives angular-quadrature convergence. As of
  Iteration 12, *no* σ(I) OFF-state configuration survives N17 on a
  correctly-constructed domain.
- **S-C — empty-scene floor**, same domains, same angle sets, giving the
  per-geometry `δ_C` that T-7 gates on. Not optional: without it neither
  S-A nor S-B is decidable.
- **S-D — Tier-W recomposition, zero FDTD.** Re-run `lab/glare_sidecar` on
  whatever `C` S-A returns, with T-4's out-of-calibration flag enforced
  **per point**, and report the un-veiled night margin (§5.2) separately
  from the veiled one.

### 5.5 Pass/fail, pre-registered

- **P1 (S-A — the gate).** `r = |C_bench − (−0.7209)| / 0.7209`.
  **INSTRUMENT-REPRODUCES** iff `r ≤ 0.0186`; **DRIFTED** if
  `0.0186 < r < 0.0509` (everything downstream reported directional-only);
  **NOT-REPRODUCING → HALT** if `r ≥ 0.0509`.
  *Anchors (R17), both from this channel's own record, neither round:*
  `0.0186` is exp-033's measured cross-resolution shift of a headline figure
  on this channel (`raw g600 0.6927 → 0.7056`); `0.0509` is the largest
  same-article headline move on file (exp-020's `−0.686` → exp-030's
  `−0.7209`, the floor correction).
- **P2 (S-B — N33).** Apply T-7 **first**: report a bucket only if
  `|C_N33 − C_N17| > 7.80×10⁻⁴`; otherwise **N33-UNDECIDABLE**, and state
  that the convergence sequence cannot be closed on this instrument at this
  budget. If decidable: **PASS** iff `|C_N33| < 5.00×10⁻³`, else **FAIL** —
  two buckets only, because T-6's MARGINAL band is unsourced and I will not
  score against an unsourced threshold.
  *Falsifier:* `|C_N33| ≥ 5.00×10⁻³` refutes "the program's first-ever σ(I)
  OFF-state constraint-3 PASS survives angular-quadrature convergence," and
  the N9→N17→N33 trend either converges or does not.
- **P3 (S-D — Tier W).** Report (a) the un-veiled night margin at both `p`
  — **PASS iff `< 1`**, and my pre-run statement of record is that it will
  read `2.886×` (p=0.4) and `1.085×` (p=0.5), i.e. **FAIL/MARGINAL**;
  (b) the veiled margin, only at points inside T-4's validity envelope;
  (c) `n_out_of_calibration / 36` for exp-047's own headline grid.
  *Pre-registered prediction:* **36/36 out of calibration**, on EM's
  measured `L_v/L_B` range. If that lands, exp-047's "170× margin" is
  **withdrawn as un-scoreable** and Tier W returns to open — which is a
  real, checkpoint-relevant result about the program's only Tier-W claim,
  obtained at zero FDTD cost.

### 5.6 Two things EM must not get wrong when writing Phase 1

1. **Iteration 93 is a phenomenon-program cycle, not a governance cycle.**
   S-B's article is a **σ(I) OFF-state endpoint** — the escape route under
   test is **σ(I) intensity gating**. PANEL.md's own D1 amendment exempts
   only *"instrument-fidelity / governance cycles"* and binds *"any
   iteration whose proposal names a mechanism or a T1 escape route."*
   Iteration 93 therefore **records the seven metric rows, or states per row
   why not**, and declares its escape route as `σ(I)`, not `N/A`. Writing
   `T1 escape route: NONE` on this cycle would be the thirteenth
   consecutive `NONE` and would be wrong on the amendment's own text.
2. **`lab/ambient.py` returns a contrast, never a luminance.** All
   normalization is per-component against each run's own empty flank mean
   (`incoherent_sum`), so the empty sum's flank mean is 1 by construction.
   The photopic/scotopic distinction the Metrics table demands therefore
   enters **only** through `C_thr(L)`, which is external to the module and
   is mine to pin. Any Phase-1 text implying the instrument itself
   distinguishes ambient regimes is wrong. Related, and still open: `C_thr`
   is a **static-target** threshold applied to a physically **transient**
   event — T3's temporal instrument (metric-table stage 10) remains
   unbuilt, so a Tier-W verdict on a *swept* beam is bounded by that gap no
   matter how the arithmetic lands.

---

## 6. Summary (≤150 words)

**PARTIAL.** The measurement is clean: 18/18 calls, identity gate 10/10,
ABBA lags symmetric to 0.28%, M5 CONFIRM at `rel_dev = 0.08154`. Both
Phase-2 defects I filed landed and verify — and the MF-5 counterfactual, at
*this* cycle's `G`, returns a **false CONFIRM** (`rel_dev = 0.0686`), so the
bug would have been invisible by verdict alone. Caveat-lint: 16 entries,
0 required-site failures, exit 0 — but **2495 WARNs**, and the new entry can
only warn on `LOGBOOK.md`/`PLAN.md`, the forward-citation surfaces.
`DISCLAIMER_115` verified in both texts.

Why not CONFIRM: `NOTES.md` Phase 4/5 read `(pending)`; LOGBOOK/PLAN quote
the interrupted session, one figure sign-flipped. M8 has no prose headline
(R21). M3's verdict flips to PARTIAL under the cycle's own drift rates —
and M3 gates M6. Two machines straddle the reference and both CONFIRM,
18.2% apart, above M6's 15.3% bar. A free cross-session replicate sits
unanalysed.

---

*VISION SCIENCE, Panel Iteration 92, Phase 5. Worked alone: no sub-agents,
no delegation, no simulations, no git state changed. Every figure recomputed
this session against committed JSON and committed source, or re-derived from
primitives.*
