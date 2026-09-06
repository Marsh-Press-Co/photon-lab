# exp-115 — Phase 5 FINAL AUDIT — RED TEAM

*Panel Iteration 92. Seat 7. I speak last and with everything: the proposal,
all five Phase-2 critiques, my own Phase-2 audit (MF-1..MF-15, OV-1..OV-6,
RT-1..RT-16), the Phase-3 synthesis, both committed reading files, both run
logs, the bench trust-suite record, `results.json`, `run115.py`,
`chunk_runner115.py`, `analyze115.py`, and **all six** `phase5_review_*.md`.
Also read in full: `PANEL.md` including the Iteration-92 Metrics scope
amendment; `LOGBOOK.md` RULED OUT R1–R34 and the Iteration-92 record with its
CHECKPOINT entry; `PLAN.md` 1–80; `lab/sections.py`, `lab/caveat_lint.py` +
config; `experiments/108/110/112/114/061/100`.*

*Worked alone: no sub-agents, no delegation, no simulations, no git state
changed. Every figure below was produced this session by pure-python
re-derivation from committed JSON and committed source. Where a seat's figure
reproduces I say so and cite the recomputation; where it does not I say that
instead. Charter: I kill internal inconsistency, unfalsifiable claims,
mechanisms that cannot be expressed as simulation parameters, and proposals
that quietly violate a target constraint — especially #3. I have no proposal
of my own to protect.*

---

## 0. Method, and the one thing that makes this audit different from the six

Each seat saw its own slice. I see the union — and the union is the finding
that no single seat could reach. **Six independent R4-class defects survive
the Phase-3 freeze into this cycle's frozen text, each caught only at Phase 5.
R20's bar is three, and R20's forward clause says "fires Checkpoint criterion 4
automatically, no further deliberation." It fires (§4).** EM tallied two and
ruled it does not fire; MATERIALS tallied three and explicitly asked Red Team
to rule; PHOTONICS found none on the line ranges it checked. All three are
correct about their own slice. Nobody had the union. That is what seat 7 is
for.

Nothing in that firing touches a scored verdict. Every instance is desk-
correctable at zero FDTD cost, and I rule it **a notification, not a pause**.

**T1 escape route: N/A — verified structurally, not accepted on assurance.**
`chunk_runner115.py::build_sim`/`_time_control_blend` brackets `sim.run()`
only; the executed path contains no `full_capture`, no `lab/sections.py` call,
no `lab/ambient.py` call, no angular instrument. The cycle produces no
constraint-1/2/3/4 observable and moves none. The article the M9 sidecar
bounds is passive, linear, time-invariant and fails constraint 3 by
construction (LOGBOOK ESTABLISHED), and both `DISCLAIMER_115` and the quotable
M9 blockquote say so **inside** the quotable text. No constraint-3 slip in
this cycle's own scoring.

---

## 1. Per-metric adjudication, from primitives

### 1(a) The scored results — every one re-derived bit-exact. CONFIRMED.

Recomputed from `data/readings.json` per-scene wall times upward, trusting no
intermediate field. `per_step_s = Σ(per_scene_wall_s) / (3 × control_steps)`
reproduces all six persisted rates exactly.

```
S156  0.04858939027786255      S234  0.11239203476905822
U156  0.04970505291927912      U234  0.11082375609762692
U234b 0.11105367999581237      U156b 0.04908984934084655

G_short      = S234/S156     = 2.3130982736423493        filed identical
G_pair1      = U234/U156     = 2.2296275647790664        filed identical
G_pair2      = U234b/U156b   = 2.2622534289060674        filed identical
G_sustained  = mean of pairs = 2.245940496842567         filed identical
```

| Metric | Re-derived | Bar(s) | Verdict | Ruling |
|---|---|---|---|---|
| **M3** `d_dur = \|G_sus−G_short\|/G_short` | `0.02903368938753793` | `R_DEG/2 = 0.037982123779318644` | `G-DURATION-INVARIANT` | **arithmetic CONFIRMED; the verdict is anchor-fragile — see 1(b)** |
| **M4** `d_rep = \|G2−G1\|/G1` | `0.01463287619976741` | `0.02` | `REPEATABLE` | **CONFIRMED, within-session only** |
| **M5** `exponent_B = ln(1.5·G)/ln 1.5` | `2.995546218006855` → `measured_ratio 3.3689107452638507` vs `reference_ratio 3.6680107109370383` → `rel_dev 0.0815428277734715` | `≤0.15` | `CONFIRM` | **CONFIRMED as a containment result; see the framing ruling in §5** |
| **M5 interval** | `[2.2176904, 2.2458389]`, rel width `1.269%` | edges `2.0785394 / 2.8121415 / 1.7117383 / 3.1789426` | no edge spanned, `m5_protocol_caveat=False` | **CONFIRMED; scope must be stated (1(a)-iv)** |
| **M6** `T = G/G_E` | `0.8180425684476521`, `\|T−1\| = 0.1819574315523479` | `0.152950039837078 / 0.305900079674156` | `AMBIGUOUS` | **CONFIRMED; `directional_only` is fragile — 1(b)** |
| **M7** `excess = G/2.25 − 1` | `−0.0018042236255256805`; `k_B = 2.995546218006855` | `\|excess\| ≤ 0.05` | `N2_HOLDS` | **CONFIRMED; the "favoured" sub-field is NOT — see 1(e)** |
| **M9 sidecar** | 11/11 reproduction checks pass | — | `REPRODUCED` | **status CONFIRMED; the bound's wording is not — see 1(f)** |

Four further verifications, all mine this session:

**(i) `exponent_B ≡ k_B` identically.** `1 + lnG/ln1.5` and
`3 + ln(G/2.25)/ln1.5` are the same function of `G` because `ln 2.25 = 2 ln 1.5`.
M5's exponent, M7's `k_B` and M7's `excess` are **one number under three
labels**. Only M3 (adds `G_short`), M4 (adds the pair split) and M6 (adds
`G_E`) contribute independent information. PHOTONICS F8 and EM §2.7 both found
this independently; both are right. **The Result must say so, or this cycle
will be read as five corroborating measurements.**

**(ii) ABBA worked, and I measured it.** Mean-A midpoint `1788671659.5939`,
mean-B `1788671660.7061` — residual lag **+1.112 s** against the
`(a+b)/2 = 802.805 s` that ABAB would have left. **721.8× reduction.** The two
pairwise lags are `+804.654 s` and `−802.429 s`, symmetric to **0.277%**. EM's
A3 / my own RT-6 closed form is now empirically confirmed for the first time in
this program. MF-6(a) earned its keep.

**(iii) `d_rep` is exactly the grid-differential log-drift.** EM's identity
re-derives: `ln(G2/G1) = D_234 − D_156 = +0.0020725314347838 −
(−0.0124543173049980) = +0.0145268487397818`, and `exp(·)−1 = 0.0146328761997676`
against the filed `0.01463287619976741`. **Consequence EM states and the record
does not: common-mode drift cancels in `d_rep` exactly.** A uniform 10% session
slowdown across both grids would still read `REPEATABLE`. ABAB's null channel was
blind to monotone drift; ABBA's is blind to common-mode drift. Neither ordering,
with two sustained readings per grid, produces a channel that can see it. That is
`lab/ARTIFACTS.md`'s own invariant applied to the replacement, and it must be
written down so the next cycle does not treat `d_rep` and the MF-6(c) drift block
as two pieces of evidence. **They are two independent quantities and their exact
difference — not three.**

**(iv) The two-point interval, re-derived by hand.** `C₁₅₆ = −1.1542737280358781`
s/scene, `p₁₅₆,∞ = 0.04974366400589843`; `C₂₃₄ = +2.0759888398786654`,
`p₂₃₄,∞ = 0.11031604592917955`; `G_burst = 2.2458389149395477`,
`G_prod = 2.2276295684987977`, `G_∞ = 2.2176904`. All four filed values
reproduce. **Two disclosures the record owes** (EM D-5, QUANTUM D-Q6, both
confirmed): `C₁₅₆` is a **negative fixed per-scene overhead**, which is not an
overhead — the model is being evaluated outside its own physical interpretation
on that grid; and both production endpoints (8000/12000) lie **outside** the
`[1000, 3334]` bracket the two points define, so they are extrapolations. The
interval's 1.27% narrowness is therefore **not** evidence that the protocol
mismatch is small, and it structurally cannot contain the burst-vs-production
step exp-114 itself measured at **4.90%** (3.9× the interval's full width).
`m5_protocol_caveat = False` is a true statement about a narrower question than
MF-7(a) promised. **Ruling: the outcome stands (no plausible correction moves
it), the scope statement is mandatory.**

**(v) PHOTONICS F11, confirmed and minor.** `G_sustained` (a mean of ratios)
exceeds `interval_hi` (a ratio of means) by `4.52×10⁻⁵` relative. The interval's
own note discloses the construction difference. Non-load-bearing; one clause.

### 1(b) M3's verdict, the drift correction, and the anchor. **The sharpest finding of the cycle.**

Three independent seats attacked M3 and all three are right, on two distinct
routes with different reach. I re-derived both.

**Route 1 — VISION's drift correction (Finding 7).** From `results.json.drift`:

```
r=156 relative_rate_per_s = −4.552366720982913e−06   ( −1.6389 %/hour, later reading FASTER )
r=234 relative_rate_per_s = +1.8661564961051803e−06  ( +0.6718 %/hour, later reading SLOWER )
d(lnG)/dt = 6.418523e−06 /s = +2.311 %/hour
S-pass effective midpoint 1788669759.8136 · U-pass 1788671660.1500 · gap 1900.336 s
drift contribution to G over that gap = +1.2197 %
measured G_sus/G_short − 1                = −2.9034 %
drift-corrected duration effect           = −4.1231 %
```

`0.041231 > M3_INVARIANT_BAR = 0.037982` and `< M4_NOISY_BAR = 0.075964` →
**PARTIAL**. **VISION's arithmetic reproduces to every digit I checked.** The
drift and the duration effect push in **opposite** directions, so the raw
`d_dur` is a *lower bound* on the duration effect and the cycle scored the
flattering end. Under MF-9's inverted rule, `PARTIAL` sets
`m6_directional_only = True`.

**Route 2 — EM's and THERMO's bench-native anchor.** The two seats' figures
differ and I found why: **they use different sustained operands, and both are
defensible.**

```
r=156:  S156 → mean(U156,U156b)  = +1.6630 %   (EM, QUANTUM)
        S156 → U156 (first only) = +2.2961 %   (THERMO)
r=234:  S234 → mean(U234,U234b)  = −1.2931 %   (EM, QUANTUM)
        S234 → U234 (first only) = −1.3954 %   (THERMO)
cloud   R_DEG (exp-114, r=156, 1000→3334, single reading each) = +7.5964 %
```

**Ruling on the discrepancy: THERMO's construction is the exact analogue of
`R_DEG`'s own** — exp-114 had one short and one sustained reading, no repeat —
so `R_DEG_bench = 0.022961` is the R17-correct forward anchor, with EM's
mean form `0.016630` reported as the disclosed alternative. **The verdict is
the same either way:**

| anchor | `M3_INVARIANT_BAR` | M3 | `m3_scored` | `m6_directional_only` | `m5.may_move_logbook_verdict` |
|---|---|---|---|---|---|
| cloud `R_DEG` (as filed) | `0.037982` | `G-DURATION-INVARIANT` | **True** | **False** | **True** |
| bench first-reading `0.022961` | `0.011481` | `G-NOT-DURATION-INVARIANT` | **False** | **True** | **False** |
| bench mean `0.016630` | `0.008315` | `G-NOT-DURATION-INVARIANT` | **False** | **True** | **False** |

**Route 2 reaches one boolean further than Route 1**: because `m3_scored` gates
on `d_rep ≤ M3_INVARIANT_BAR` and `d_rep = 0.014633` exceeds *both* bench-native
half-bars, a bench anchor also sets `m3_scored = False`, which sets
`may_move_logbook_verdict = False`. **So the cycle's own claim that M5 may move
exp-114's LOGBOOK entry is anchor-fragile, on an anchor this cycle's own data
supersedes.** No seat stated that chain in full; it is the load-bearing
consequence.

**Is M3's verdict "as filed" honest under R17?** **YES — R17 is satisfied and
must not be retro-scored.** R17 requires the bar be justified *before the run*
against the largest already-established comparable magnitude on file. At Phase 3
no bench figure existed and `R_DEG` was the largest comparable. The bands were
pre-registered, committed at `f75b905` before any reading, and PHOTONICS
verified the frozen Predictions block is byte-identical to its generator.
Post-hoc re-anchoring to move a verdict is exactly the estimator-switching this
program ruled out at Iteration 1, and **I decline it explicitly (§5 decline
D-3).**

**What the record MUST say** (this is not optional; it is the forward half of
R17 and it is what every future bench cycle inherits):

> M3's `G-DURATION-INVARIANT` is scored against a **cloud** anchor
> (`R_DEG = 7.596%`) that this cycle's own readings supersede. The bench's own
> duration response is **+2.296% (r=156)** and **−1.395% (r=234)** — 3.3× smaller
> and **opposite in sign** between the two grids. On any bench-native anchor M3
> reads `G-NOT-DURATION-INVARIANT`, `m3_scored` becomes `False`,
> `m6_directional_only` becomes `True`, and `may_move_logbook_verdict` becomes
> `False`. Independently, correcting `d_dur` with this cycle's own persisted
> drift rates gives `−4.123%` against the `3.798%` bar → **PARTIAL**, which also
> sets `m6_directional_only = True`. Neither correction is scored (R17: the
> pre-registration stands). **`R_DEG_bench = 0.022961` is this cycle's own
> deliverable and is the R17 anchor for every future bench cycle; the cloud
> `R_DEG` is retired for bench work.**

**And the physics under the label, which EM and QUANTUM both found and which is
better than the label:** `(1 + r₂₃₄)/(1 + r₁₅₆) − 1 = −0.029078`, reproducing
`d_dur` to four digits. The two grids' duration effects are **opposite in sign,
so in the ratio they ADD.** Had they been equal and same-signed — the
grid-independent throughput factor that R31's r=156-only control and R33's
normalization both assume — they would have cancelled and `d_dur` would read
≈0.4%. **The verdict label is correct against its bar; the underlying behaviour
is the opposite of cancellation, and R31/R33's founding assumption is measured
false at the 2–3% level on one clean machine.** That is the cycle's best
physics-of-the-instrument result and it exists in no committed file.

### 1(c) Session 1 — it must enter the record, as a NOT-scored replicate. Three seats are right.

`data/readings_session1_interrupted_20260905T2354Z.json`: four complete
readings, same bench, same code, same protocol, 4.75 h earlier, committed at
`5bb62cc`. It appears **zero times** in `results.json`, `result_text`,
`NOTES.md`, `run115.py`, `analyze115.py` or `chunk_runner115.py`. Re-derived:

```
per-step, session 1 vs session 2:  S156 +4.775 %   S234 +4.208 %
                                   U156 +5.369 %   U234 +8.328 %
G_short    2.3005776183025777  vs 2.3130982736423493   −0.541 %
G_pair1    2.2922398627376155  vs 2.2296275647790664   +2.808 %   ( 1.92 × d_rep )
                               vs 2.245940496842567    +2.061 %   ( vs the ABBA mean )
k(session 1) = 1 + ln G/ln1.5  = 3.0458713436566054    rel_dev 0.06260911838284892  CONFIRM
excess(session 1)              = +1.8773 %             N2_HOLDS
```

EM's `k = 3.0459` reproduces exactly. VISION's `−2.73%` and EM's `+2.81%` are the
same number read in opposite directions (`s2/s1−1` vs `s1/s2−1`); both are
correct, and the record should state the direction it uses.

**Ruling — how it enters.** As
`sensitivity_session1_across_reboot_DO_NOT_SCORE`, **not** as a scored operand.
Two reasons, and the first is decisive: session 1's `U234` is the largest
deviation of the four (+8.33%) **and is the reading immediately preceding the
host hang** — the slowdown sequence in execution order is 4.78 / 4.21 / 5.37 /
8.33%, progressive and tail-weighted. That is a **ramp into a fault**, not a
clean replicate, and it contaminates exactly the reading that carries the
excess. Second, it is cross-session: folding it into `G_sustained` would break
the R33-immunity M5 currently has by construction.

**Is the omission a defect? YES — R33 addendum (a) + R21.** R33(a) requires an
alternative reading of a control quantity be disclosed as a stated, not-scored
sensitivity; an alternative *session* on the same machine for the cycle's own
primary statistic plainly meets that standard, and PLAN.md's own resume recipe
directed that the outage "goes in the record." EM's D-3, QUANTUM's D-Q5 and
VISION's Finding 8 are all confirmed.

**What it does to M4 and M6 — I computed it so the record does not have to
guess.** Scoring session 1's pair as a hypothetical third pair (explicitly NOT
adopted):

```
3-pair G = 2.2613736188075833  →  k 3.0124356  rel_dev 0.07523  CONFIRM
                                  excess +0.5055 %             N2_HOLDS
                                  |T−1| 0.17634                AMBIGUOUS
max pairwise spread across the three pairs = 2.769 %  →  M4 would read
   MARGINAL-M3-SCORED-M7-POWERED (0.0281 sits between 0.02 and 0.03)
```

**No verdict changes and no composition boolean flips.** That is the strongest
possible reason to admit it: it is corroboration that costs nothing and risks
nothing. **M4's `REPEATABLE` is correct within one session and is not robust to
a session change** — the across-reboot spread (2.06% on the ABBA mean, 2.81% on
the matching pair) is **1.41×–1.92× the `d_rep` that is the sole input to the
power gate** — and that must be stated, because `d_rep` is the only noise
instrument three composition rules consume.

**And the positive finding buried in it, which is the most citable science this
run produced:** a 4–8% common-mode per-step slowdown moved `G` by only
**−0.54%** on the short protocol — `G` is largely robust to session-level load —
while the between-**machine** difference is **18.20%**, i.e. **9–34× the
between-session difference on the same machine.** M6's `AMBIGUOUS` is therefore
better read as a genuine machine property than as session noise. **This is a
positive result, obtained for free, currently written nowhere.**

### 1(d) Cycle spend and the budget gate. THERMO is right on both.

Re-derived from the two committed reading files:

```
session 2 (results.json)       : 18 calls, 3690.309 s of Sim.run, 3699.4 s elapsed
session 1 (…_interrupted…json) : 12 calls, 2228.700 s of Sim.run, 2234.8 s elapsed
CYCLE TOTAL                    : 30 calls, 5919.009 s        = 54.8 % of COST_GATE_TOTAL_S
```

`result_text`'s *"18 real FDTD calls (Sim.run), 3700.5s (61.68 min) total wall
time **this cycle**"* understates the cycle by **12 calls and 2218.503 s
(37.48%)**. **Ruling: R21 + R4 on the sentence; NOT an R19 violation.** The R19
assert is present, conditional, and honest about what it counts — but
`_SIM_RUN_CALLS` is a module global reset at process start, so the invariant is
**per-invocation by construction while the sentence it certifies says "this
cycle."** R19 demands a code-enforced assert and there is one, at the wrong
scope. The fix is the sentence and a cycle-scoped ledger, not a new assert.

**Ruling on the gate: NOT an R27/R28 violation this cycle** — the gate is
executable, sits causally upstream of every `Sim.run()` (three PROCEED
projections at `after_S156`, `after_S234`, `after_U234`, each before the next
call), and nothing breached at 54.8% of the bound. **But the hole THERMO names
is real and now demonstrated: the resource is consumed by the *cycle*, the gate
is armed by the *process*.** A twice-interrupted cycle could spend 2–3× the
bound with every gate reading PROCEED. That is R28's own founding lesson one
scope level up. It becomes Tier-2 item 6 of the Iteration-93 queue and the
Result must state the cycle-scope figure.

**R25 on the resume path (EM D-9, THERMO D3): confirmed.** PLAN.md pre-registered
exactly two resume branches; the executed path — a full six-reading re-run from
scratch — is a **third**. It was the better choice (it preserves ABBA's
first-order cancellation inside one session, which branch (ii) would have
destroyed across a reboot, and it produced the loaded-vs-clean pairing) but a
deviation from a pre-registered degradation path is a **numbered disclosure, not
a silent improvement.** It currently exists only in a commit subject.

### 1(e) M7's "favoured: constant-k" — an over-read. It does not ship.

`run115.py:435-436`:

```python
model["favoured"] = ("UNDERPOWERED -- no model declared favoured" if m7_underpowered
                     else ("constant-k" if d_k < d_eps else "constant-eps"))
```

A bare nearest-neighbour with **no rejection test**. Re-derived:
`d_k = 0.0815428277734715`, `d_eps = 0.13422460480982495`, `separation =
0.060849242573798784`. **The measurement sits farther from both models than the
models sit from each other.** The same `results.json`'s own adjacent
`m7["note"]` says *"N2_HOLDS requires BOTH candidate cost models to be wrong"* —
and it is right: const-`k` predicts `excess = +0.08682`, const-`ε` predicts
`+0.15295`, measured is `−0.00180`. A results file that says "both models are
wrong" and "favoured: constant-k" in neighbouring keys is internally incoherent,
and `result_text` propagates the second without the first.

**Ruling — QUANTUM's D-Q2, VISION's Finding 5 and EM's D-6 are all upheld and
consolidated. `favoured` is DECLINED as a shipped reading.** The selection rule
is structurally incapable of emitting the reading that is true here, which is
`lab/ARTIFACTS.md`'s own invariant applied to a model-selection string. Two
further grounds I confirm: `m7_underpowered` is computed from `d_rep` alone —
the **smallest** of four measurable uncertainty channels (within-session 1.46% ·
across-reboot 2.06–2.81% · burst-vs-production 4.90% · **machine-to-machine
18.20%, which this cycle's own M6 reports as unresolved**) — so the power gate
excludes the dominant variance channel by construction; and both nominated
models are parameterized on `kappa_ratio` while any cache/bandwidth
superlinearity is a function of absolute `N`, so they are not being tested on
the axis they are defined on.

**Result prose must read:**

> **M7 model comparison: NO MODEL FAVOURED.** Both nominated models are refuted
> by this datum — constant-`k` by 8.15%, constant-`ε` by 13.42%, against the
> 6.08% that separates them — while the un-nominated pure-`N²` model
> (`k = 3.0` exactly) fits at **0.18%**. `m7_underpowered` was computed from
> `d_rep` (1.46%) alone; the machine-transfer channel this cycle itself measures
> is 18.20% and reads AMBIGUOUS.

**PHOTONICS' DRAM-bandwidth interpretation (F7):** adopted as an **explicitly
NOT-SCORED reading**, and I rule it should be stated rather than declined,
because the obvious wrong reading is worse than a labelled post-hoc one. Both
grids' working sets exceed the W-2145's **11 MiB L3** by roughly an order of
magnitude (PHOTONICS counts 6 `N×N` float64 planes → ≈94 MB / ≈212 MB = 8.2× /
18.4× L3; THERMO counts 7 → ≈112 MB / ≈251 MB = 10× / 23×; the plane count is
the only difference and neither changes the conclusion), so both sit in the
DRAM-bandwidth-bound regime of an explicit Yee stencil, where per-step time is
proportional to cell count — `G → 2.25` is what that regime predicts. The
slightly-**sub**-`N²` sign is reproduced by a 0.33% fixed per-step overhead, a
0.54% perimeter term, or a 3.8% extra cost in the absorbing band; two grid
points cannot distinguish three unknowns from one equation (R5/R30 lineage), so
it is a mechanism consistent with one ratio, **not evidence.** Say it, label it
NOT-SCORED, and foreclose the inference "FDTD scales as `N²`, therefore
`k = 3.0` is the right cost exponent" — which MF-7(b) already warns M5 cannot
license.

**The honest sentence about `KAPPA_COST_EXPONENT = 3.2053`, ruled and verbatim
for the record.** EM's and QUANTUM's framings do not conflict; THERMO's does,
and **THERMO's is refuted at the magnitude.**

> `k = 3.2053` is **not reproduced on this bench at `kappa_ratio = 1.5`**: the
> bench's two sessions give `k = 2.9955` (scored) and `k = 3.0459` (session 1,
> not scored), against exp-114's cloud `k = 3.4909` at the same `kappa_ratio`
> and R28's founding `k = 3.2053` at `kappa_ratio = 2.0`. Five measurements span
> `2.9955 – 3.6090` — 0.61 in exponent, 22% in `G` — with machine, contention,
> `cpl`, absolute `N` and protocol confounded across them. **`k` is a
> per-machine, per-configuration fitted parameter with one measurement per
> configuration, and has never been shown portable.** The record may **not** say
> `KAPPA_COST_EXPONENT` is a cloud-contention artifact: contention is a
> demonstrated, signed, **partial** explanation, insufficient at the measured
> magnitude — the bench's own 4–8% per-step slowdown between sessions moved `G`
> by +2.81%, **1/7.9** of the 22.24% bench-to-cloud gap, and its sign is
> protocol-inconsistent within that same pair (`−0.54%` on the short protocol,
> `+2.81%` on the sustained). **`KAPPA_COST_EXPONENT = 3.2053` is RETAINED for
> the cost gate as the conservative (larger) choice — a gate-margin decision,
> labelled as such, not a scientific one.**

THERMO's §2.4 conclusion — *"`KAPPA_COST_EXPONENT = 3.2053` is a contention
artifact of the cloud sandbox"* — is **REFUTED** at the measured magnitude and
may not enter the record. Its *mechanism* (DRAM-bandwidth-bound stencil ⇒ `N²`
on a clean machine) is adopted as the NOT-SCORED reading above; its causal
conclusion is one datum in a four-way-confounded space, and R5's
look-elsewhere discipline forbids it. THERMO's own pre-registered expectation
(`d_dur` negative, −4% to −6%) is **REFUTED by the data** and THERMO says so
first, before anything it got right — that is the seat behaving exactly as this
panel intends, and it should be recorded as such.

### 1(f) The M9 sidecar as shipped. Corrected, not withdrawn — and five things shipped FALSE.

**What is exactly right, verified by me from primitives**, and must not be lost
in the criticism:

- `τ_true` recomputed from `lab/materials._graded_black`:
  `8.258813114090946` (cpl=20, σ_max 0.5, 48 cells) and `8.258813114090952`
  (cpl=25, σ_max 0.4, 60 cells) — **bit-identical**, reproducing the filed
  `8.258819829686677` to `8.13×10⁻⁷` relative. The family identity
  (`σ_max·cpl = 10`, `thickness/cpl = 2.40 λ`) is algebraically forced.
  **OV-5 was correctly declined and QUANTUM accepts the refutation.**
- MF-1's corrected physics: `exp(−τ_true) = 2.5896617219231565×10⁻⁴` as the
  scale, `2·exp(−τ_true) = 5.179323443846313×10⁻⁴` as the bound,
  `exp(−2τ_true) = 6.706347833994009×10⁻⁸` persisted only under
  `proposal_figure_exp_minus_2tau_WITHDRAWN` with `wrong_by_factor = 3861.508`.
  **All six measured aggregate deltas respect the bound**: bracketed from above
  by **2.38×–45.70×** (scale) and **4.76×–91.41×** (bound).
- MF-2: the `σ_ext_cross − σ_ext` "floor" withdrawn as scene-independent (`0.0`
  exactly at r=234, `2.274×10⁻¹³` at r=156 between scenes — both reproduced);
  exp-108's six-margin `item_ii` family substituted; `mean/std` recomputed
  **`4.464601791167039`** (r=156) and **`11.695432413176777`** (r=312).
- MF-11: two independent channels and their exact algebraic sum; residuals
  `−5.684×10⁻¹⁴` (r=156) and `0.0` exactly (r=234), both reproduced.
- MF-4's hard scope clauses, the constraint-3 failure, the realizability tier
  and the T18 evidentiary tier are all **inside** the quotable blockquote, and
  `sidecar_m9["headline"] in result_text` is **True**. That is what makes the
  sentence safe to quote *once corrected*.

**PHOTONICS' reconciliation — CONFIRMED, and it is the strongest positive result
the sidecar contains.** Under a **common (peak) normalization** the same
margin-32 arrays give max `|rel32|` = `1.4760284822434646×10⁻⁴` (r=156) and
`1.5265673604659632×10⁻⁴` (r=312) — **`0.2850×` and `0.2948×` of
`2·exp(−τ_true)`.** The corrected coherent-cross-term bound is therefore
**honored at every one of the 48 bins at both radii, with ≈3.4× margin.** The
apparent 28.3×/102.1× "exceedance" of the printed local figures is **exactly the
normalization change**: `28.32/99.38 = 0.2850`, `102.14/346.53 = 0.2947`. This
must be stated; a future citation reading only the blockquote will otherwise
conclude the bound is violated.

**MATERIALS' five findings — adjudicated one by one.**

1. **Margin-40 maxima not reported — CONFIRMED, and load-bearing.** exp-110
   persists `local_diag` at **all six** margins; I enumerated them:

   | r | m=24 | **m=32 (quoted)** | m=40 | m=48 | m=57 | m=65 |
   |---|---|---|---|---|---|---|
   | 156 | 1.9765e-03 | **1.4669e-02** | **4.9648e-02** | 1.8424e-02 | 2.0595e-02 | 2.2742e-02 |
   | 312 | 2.5085e-02 | **5.2900e-02** | **7.3202e-02** | 3.3574e-02 | 3.6223e-02 | 3.8378e-02 |

   Margin 40 gives **3.384×** the quoted figure at r=156 and **1.383×** at
   r=312. The headline understates its own instrument in the one direction that
   matters for a fabrication warning, on data already on disk at zero cost.
   **And the scope clause that licenses the restriction is FALSE**: *"only the
   margin-32 array is persisted"* is true of **exp-108** and false of
   **exp-110**, the channel the headline actually quotes. MF-3 and MF-4 are each
   individually correct; **their composition is not, and no seat owned the join
   — including me at Phase 2. I own that.**

2. **Tail-max vs median — CONFIRMED.** Median resolved `local_rel` across all
   twelve `(r, margin)` cells spans `9.4304×10⁻⁵ → 1.6020×10⁻⁴`, a **1.699×**
   total spread, and the withdrawn peak-normalized figures (`1.4760×10⁻⁴`,
   `1.5266×10⁻⁴`) sit **inside** that band. So the two normalizations **agree on
   central tendency to within 1.6×**, and the celebrated 99.4×/346.5× divergence
   is entirely a **tail** phenomenon between distributions with different tails.
   MATERIALS' further point reproduces and is the better physical statement:
   `|Δσ_scat|` at the four quoted max bins varies by only 1.31× while
   `local_rel` varies by 5.0× — **the core swap moves the backward-hemisphere
   per-bin `σ_scat` by a near-constant ≈2×10⁻⁵ absolute, and the "1.5%–7.3%"
   figures are that constant divided by whichever backward bin happens to be
   smallest at the chosen box radius.**

3. **The observer face is UNMEASURED at 10/12 cells — CONFIRMED, and this is the
   most consequential wording defect in the bound.** Restricting to `|θ| > 135°`
   (the twelve source-facing bins):

   | r | m=24 | m=32 | m=40 | m=48 | m=57 | m=65 |
   |---|---|---|---|---|---|---|
   | 156 | 0/12 | **0/12** | 0/12 | 0/12 | 0/12 | 0/12 |
   | 312 | 0/12 | **2/12** | **4/12** | 0/12 | 0/12 | 0/12 |

   At r=156 the headline's own max bin (`+123.75°`) is **not on the
   observer-facing face at all** — it is a side-face bin. The sentence *"does
   NOT license varying the backing without re-measuring the per-bin angular
   channel in the observer-return hemisphere, **which moves by ~5 percent
   there**"* rests on a **2-of-12-bin sample at one of six box radii.** The
   warning is right; the reason it gives is close to the opposite of the true
   one. **And the units are wrong for the constraint**: PANEL.md scores
   constraint 2 as *backscatter to observer vs camera floor* — an **absolute**
   comparison via `emit.observer_record` — while the sidecar reports a
   **relative** movement of a face carrying `3.4×10⁻⁶` of total `σ_scat` and
   never compares the absolute `≈2×10⁻⁵` change to any floor. **Ruling: the
   honest statement is UNMEASURED, not bounded at ~5%, and the absolute-units
   question is a real open item (Iteration-93 Tier-3).**

4. **The MP-5 forward conditional is physically wrong — CONFIRMED against
   exp-061's own text.** exp-061 `NOTES.md` MP-5: *"visible-band figures need
   **~230–730×** the 1.44 µm thickness … **to reach τ_true**."* **MP-5's multiple
   is defined as the thickness at which a real, lower-α CNT-forest-class coating
   reaches the SAME `τ_true ≈ 8.2588` — `τ_true` is held FIXED and the thickness
   varies to hit it.** The sidecar's premise (thickness growing at fixed
   `α = 5.74×10⁴ cm⁻¹`) is the opposite, and MP-1 records that **nothing in the
   class approaches that α** (best in-class visible-band figure `2.28×10³ cm⁻¹`,
   short by >25×). Therefore under MP-5's own scenario
   `2·exp(−τ_true) = 5.1793×10⁻⁴` is **unchanged at 230× and at 730× alike**:
   the bound **survives; it does not strengthen.** MATERIALS is right, and the
   consequence inverts MF-15's counterweight from a trade-off into a **strict
   loss**: zero additional backing freedom, thermal margin collapsing
   3.79× → 1.35× against NETD-lo (both rows verified against exp-061
   `NOTES.md:235-240`; `230×1.44 = 331.2`, `730×1.44 = 1051.2` both reproduce),
   and a physically **larger black silhouette** — constraint 3's own failure
   mode. **This defect originated in Phase 1 and survived every review layer,
   including my own Phase-2 docket, whose MF-1 patched the exponent and
   preserved the conflation. I own that too.** The one mitigating fact, verified:
   the `forward_conditional` string appears **nowhere** in `result_text` and
   nowhere in the quotable headline — so the false claim did not reach Result
   prose. It is persisted in `sidecar_m9.e_tier` and must be corrected there.

5. **`lab/sections.py`'s angle convention is INVERTED — CONFIRMED
   independently, and I rule it a live R18-class defect in shared `lab/`
   machinery.** The docstring at `:209-210` and `:223-224` states *"0 deg = −x
   (toward the source, 'backward'), ±180 deg = +x (downstream, 'forward')."* The
   code at `:246-247` computes `arctan2(yy−bcy, x1−bcx)  # x1 face (mostly
   forward)` with `x1 > bcx`, so the **high-x face maps to ≈0°**. Four
   independent confirmations, all of which I reproduced: the inline comments;
   `widths()`'s own face assignment (`p_back` at `x0`, `p_fwd` at `x1`) with the
   source at low `x` (`SRC_X = 160`, `CX = 630`), so propagation is **+x**; the
   committed pattern data (the `|θ| < 45°` sector carries **98.3%** of total
   `σ_scat` at r=156 — nothing puts a 10⁶:1 lobe on the backscatter side of a
   black absorber); and exp-112's own "0 of 12 backscatter bins resolved" count,
   which reproduces exactly on the `|θ| > 135°` set. **So `0° = +x = forward /
   downstream`, `±180° = −x = backward, toward the source and the observer`.
   exp-115's `±138.75°` observer-return claim is CORRECT under the code and
   inverted under the docstring it cites four lines away** (`:212-215`, for the
   far-field scope clause). This is **not exp-115's defect** — it has stood since
   exp-017, whose `NOTES.md:22` propagates it verbatim — but exp-115 is where it
   became load-bearing and where it was found. It sits directly under PANEL.md's
   constraint-2 metrics row. **Fix it in `lab/`, and arm a positive control**
   (assert the argmax bin of a `graded_black_shell` pattern lies within ±30° of
   0°): a check that *can* produce the reading meaning "bad" would have caught
   this inversion, and this program's own class rule says an instrument is
   verified by hearing, not by running.

**THERMO's confirmation of MF-15's rows: CONFIRMED** — both rows match exp-061
exactly, the corrected 1.35×–3.79× range is used, never the superseded figure,
and the larger-black-silhouette / constraint-3-failure-mode sentence is present.
MF-15's third clause (report the warm-up sensitivity at `0.1227 → 0.2977` if
reported at all) is discharged **vacuously** — no warm-up sensitivity is
persisted, because MF-7(a)'s measurement superseded the estimate. That is a good
outcome and **nothing records it.**

**Did anything ship FALSE? YES — five things, and one near-miss.** In the frozen
`DISCLAIMER_115` / `result_text` / the quotable headline / persisted sidecar
strings:

| # | Statement | Ruling |
|---|---|---|
| **α** | *"only the margin-32 array is persisted"* (scope clause, in the headline's own justification) | **FALSE** of exp-110, the channel quoted. All six margins persisted. |
| **β** | *"`ITEM_I_CONFIRM_REL = 0.05` … 330× looser than the quoted figure"* | **FALSE** against the quoted figure: `0.05/1.4669e-02 = 3.4×` (r=156) and `0.05/5.2900e-02 = **0.95×** — tighter*. Reproduces only against the **withdrawn** peak-normalized figure (`0.05/1.5266e-04 = 327.5`). Argument survives; number does not. |
| **γ** | *"the core/backing freedom survives and **strengthens** … `τ_true` grows with thickness"* (`e_tier.forward_conditional`) | **FALSE** against its cited source (MP-5 holds `τ_true` fixed). **Did not reach `result_text` or the headline.** |
| **δ** | *"180× below the smallest … 3455× below the largest … **even allowing** a 4× standing-wave enhancement"* | **FALSE as written**: `5.666e-06/3.1472e-08 = 180.04` and `1.087e-04/3.1472e-08 = 3454.9` are both computed **without** the 4×. With it: **45.0×** and **863.7×**. Conclusion (RULED OUT) survives at 45×. |
| **ε** | *"`geom_fixedabs_cpl` sizes STEPS so each grid gets ~2 domain crossings"* (`DISCLAIMER_115`, in **both** texts) | **FALSE**: at `geom_fixedabs_cpl`'s own `STEPS` (8000 at r=156, 12000 at r=234) the front travels **1.293** domain widths (**1.407** source-anchored) on **both** grids. The N/A conclusion it supports is *strengthened* by the correction. |
| ζ | *"4.47×"* in `DISCLAIMER_115` and `b_floor…reading`, beside the committed function's own `4.4646` printed as *"4.46×"* in the same document | **Self-contradiction inside one artifact.** My own Phase-2 MF-2 docket said `4.46×`; the `4.47` was introduced at Phase 3. The gate's hardcoded `expected = 4.4653` passes only because `rel_bar = 1e-3` is 6.4× the disagreement — a reproduction gate whose own expected value is hand-typed and slightly off, inside the machinery built to prevent R4. |

Near-miss, not false: *"the SAME ORDER as the measured aggregate deltas"* holds
for four of six channels within a decade and fails for two (`12.06×` for r=156
`σ_ext`, `45.70×` for r=234 `σ_abs`). The exact statement is **"bracketed from
above by 2.38×–45.70× (scale) / 4.76×–91.41× (bound)."**

**MATERIALS' F1 is upheld: the gate is not a HALT.** `DISCLAIMER_115` says *"any
mismatch HALTs it and it is reported NOT-REPRODUCED rather than published."*
What the code does is withhold the **headline string** (`build_m9_bound_text`
returns the WITHHELD text) while returning and persisting every sub-dict the
headline is built from; `c_physics["withheld"]` keys on 2 of 11 checks. **R18:
documented scope stronger than the source.** Also upheld: two of the eleven
checks (`0.4*25` vs `0.5*20`; `60/25` vs `48/20`) compare literal arithmetic
expressions written on the same line and **cannot fail** — they pad apparent
coverage from 9 to 11. (PHOTONICS' defence of the `τ_true` **bit-identity** gate
is about a *different* check and is correct: that one cannot fail *for this
family* by construction but will catch a future member that breaks the identity.
No conflict.) And `σ_abs`/`σ_ext` deltas and both channel-sum residuals — the
arithmetic MF-11's correction rests on — are never passed through `gate()`; only
`σ_scat` is, while the headline's "at most `1.0874e-04`" is a max over all six.

**Ruling on the bound: CORRECT IT, DO NOT WITHDRAW IT.** The aggregate half is
exactly right and fully reproduced; the corrected MF-1 physics is right and is
**honored at all 48 bins peak-normalized with 3.4× margin**; MATERIALS'
seven-cycle debt is discharged in substance and OV-2 (decline the eighth
deferral) is vindicated. **But the quotable sentence as shipped may NOT be cited
forward until re-issued**, and `lab/caveat_lint_config.json`'s new entry
currently **compels** every future citing document to repeat a scope sentence
whose stated reason is false (α) and whose figure is not the worst case. That is
the machine-enforced half of the defect and it is why the re-issue is Tier-1.

**What the bound MAY say**, adopting MATERIALS' §F9 draft amended with
PHOTONICS' commensurable reconciliation — this is the sentence I authorize:

> For the `graded_black_shell` article at `τ_shell = 24`, `ε_r ≡ 1`, λ = 600 nm,
> plane-wave normal incidence, 2D TM, measured on this bench's
> **near-to-mid-field box ledger** at its own measurement geometry (not a
> far-field pattern): replacing the entire core/backing from vacuum to a perfect
> electric conductor moves the **aggregate** cross-section channels by at most
> **1.0874×10⁻⁴** relative (`σ_scat` and `σ_abs`, plus their exact algebraic sum
> `σ_ext` — two independent channels, not three), **resolved, not floor-limited**,
> at **4.46×** (r=156) and **11.70×** (r=312) on exp-108's six-margin `item_ii`
> differential family, the only differential floor this program has — **no
> differential floor exists at r=234 at all**. On a **common (peak)
> normalization** the per-bin angular deviation is at most **1.4760×10⁻⁴**
> (r=156) and **1.5266×10⁻⁴** (r=312), i.e. **0.285× and 0.295× of the coherent
> cross-term upper bound `2·exp(−τ_true) = 5.1793×10⁻⁴`** — the bound is honored
> at **all 48 bins at both radii**. On exp-110's **floor-gated local**
> normalization the **typical** resolved bin moves by **≈1.2×10⁻⁴** (median
> `9.43×10⁻⁵ – 1.60×10⁻⁴` across **all six** box radii at both radii — within
> 1.6× of the peak-normalized figure), with a tail of 2–10 low-SNR bins
> (SNR 1.01–2.79 against the `K=3` gate) reaching **1.4669×10⁻²** at r=156 /
> margin 32, **4.9648×10⁻²** at r=156 / margin 40 and **7.3202×10⁻²** at r=312 /
> margin 40 — a near-constant `|Δσ_scat| ≈ 2×10⁻⁵` **absolute** divided by
> whichever backward bin is smallest at the chosen box radius, **not a growing
> physical effect.** The per-bin half of any "better than `1.6×10⁻⁴`" reading is
> **WITHDRAWN**. **The source-facing face (`|θ| > 135°`, `0° = +x = downstream`
> per `lab/sections.py`'s CODE, whose docstring states the convention backwards)
> is entirely below the floor gate at TEN of twelve (r, margin) cells, so the
> observer-return channel is UNMEASURED there, not bounded** — and it has never
> been scored in the **absolute** units against the camera floor that PANEL.md
> measures constraint 2 with. Per-bin evidence exists at cpl=20 only and
> aggregate evidence at cpl=25 only, so **channel and resolution are fully
> confounded**; r=234 contributes aggregate channels only. **Fabrication
> consequence, at that scope:** a process implementing this design need not
> control the core/backing material to better than the **~10⁻⁴ aggregate
> level**, and this does **not** license varying the backing without measuring
> the backward-hemisphere channel **against an absolute floor**. The optical
> function is carried entirely by a **1.440 µm (2.40 λ)** graded-σ coating whose
> physical thickness is invariant across r = 156/234/312 and cpl = 20/25.
> **THIS ARTICLE FAILS CONSTRAINT 3 BY CONSTRUCTION** (a perfect absorber is a
> black shape in daylight — LOGBOOK ESTABLISHED) and this bound is **not**
> constraint-3 progress. **REALIZABILITY TIER: UNOBTANIUM-WITH-PARAMETERS**,
> inherited unchanged from exp-061, driven by the **70–350×** thickness gap
> (1.44 µm asked of a class that runs 100–500 µm), every literature figure behind
> it **WebSearch-snippet synthesis, NOT primary-source-verified (T18)** — and
> **INVARIANT, not improved, under exp-061's own MP-5 re-spec**, which by its own
> definition preserves `τ_true` rather than growing it, so thickening buys **no**
> backing freedom while costing thermal margin (3.79× → 1.35× vs NETD-lo 0.020 K)
> and a physically larger black silhouette.

---

## 2. Audit of the six Phase-5 reviews

**All six did the work.** Every seat re-derived rather than restated, every seat
declared its method, and three seats (THERMO, QUANTUM, MATERIALS) reported
findings that refute their own prior positions before reporting anything that
flatters them. That is the panel working.

### 2.1 PHOTONICS — **CONFIRM.** The most valuable single contribution; the verdict is the one thing I overturn.

- **CONFIRMED**: the bit-exact re-import and leaf-diff of the whole analysis
  (16 last-ulp mismatches, all inside the `τ_true` desk integral, max relative
  `6.45×10⁻¹⁶`, attributable to numpy 2.5.0 vs the bench's 2.4.6); the
  byte-identity of `NOTES.md`'s frozen Predictions block against
  `build_predictions_text()` (pre-registration is a **verified property of the
  tree**, not a claim); all six band re-derivations; the three cited line ranges;
  **F4's reconciliation, which is the strongest positive result in the sidecar**
  (§1(f)); F5's angle-convention inversion with three independent physical
  checks; F8's `exponent_B ≡ k_B` identity; F7's DRAM-bandwidth mechanism with
  its own correct self-limiting caveat.
- **CONFIRMED, and I go further than PHOTONICS did**: F9(b)'s contention
  arithmetic — the slower session gave the **higher** `G`, so contention does not
  cancel in the ratio, but reaching `G_E` needs +22.24%, **8.1×** the +2.73% a
  4–8% slowdown actually produced. PHOTONICS calls this "a positive finding this
  cycle can bank at zero cost." It is, and it is also the direct refutation of
  THERMO's contention-artifact conclusion (§1(e)).
- **CONFIRMED**: F9(c) — the `loadavg` blindness, §1(h) below.
- **CONFIRMED**: F10 — the two drift rates have opposite signs and 6× different
  magnitudes; **report "no drift systematic resolved at this precision," not a
  measured drift rate**, or a future cycle will anchor a bracket on `−0.0164 h⁻¹`
  the way this one anchored on `R_DEG`. That is R17's own lesson applied
  pre-emptively and I ratify it.
- **VERDICT OVERTURNED: CONFIRM → the cycle is PARTIAL.** PHOTONICS' own review
  lists an R21 exposure on three mandated items, a live R18 defect in shared
  `lab/` machinery, and an unreconciled incommensurable comparison in the
  quotable bound — and then files CONFIRM. Its own §1 concedes *"my reservations
  are about what the record says, not what it computed."* **In this program the
  record IS the product**: `lab/ARTIFACTS.md`'s founding invariant, R21's whole
  existence, and R20's density rule all say the written artifact is what a future
  cycle inherits. A cycle whose computation is clean and whose frozen text is
  false in five places (§1(f)) is not a CONFIRM.
- **One thing PHOTONICS missed and no other seat caught**: it checked three cited
  line ranges and reported "no R4 defect found," which is true of those three
  and led it to under-tally R20 at zero. The union across seats is six (§4).

### 2.2 MATERIALS — **PARTIAL.** The deepest findings in the set; five of five confirmed.

- **CONFIRMED, all five headline findings**, each re-derived by me independently
  (§1(f)): F2's margin-40 maxima and the false "only the margin-32 array is
  persisted"; F2's "330× looser" refutation; F3's median stability (1.699× across
  twelve cells) and the near-constant absolute `|Δ|`; F4's 10-of-12 unresolved
  observer face and the units mismatch against PANEL.md's constraint-2 row; F5's
  MP-5 inversion; F1's not-a-HALT and the two checks that cannot fail; F6(a)'s
  "even allowing 4×", F6(b)'s flattering-radius closure bound (r=156 gives
  `4.9932×10⁻⁸` → 113.5×/28.4×), F6(c)'s 4.47/4.46, F6(d)'s absolute-vs-relative
  slip; F8's undisclosed non-dispersive-σ idealization behind the 3λ rows.
- **CONFIRMED with credit**: MATERIALS is the seat that led this cycle and it
  audited its own bound harder than anyone else would have. F5 in particular is a
  MATERIALS-charter error found in MATERIALS' own sidecar, disclosed first.
- **The R20 tally: MATERIALS counted 3 on its own document and explicitly
  deferred the ruling to me.** Correct procedure, and the answer is that the
  union across all six seats is six (§4). MATERIALS' reasoning for not firing on
  its own three ((a) inherited-and-partly-self-corrected, (c)/(d) internal
  normalization slips) is defensible **for those three**; it does not survive the
  union, which includes α, β, ε — three citation-class defects that fail against
  external sources.
- **Its corrected one-sentence bound is adopted**, amended with PHOTONICS' F4
  reconciliation (§1(f)).

### 2.3 ELECTROMAGNETISM — **PARTIAL.** The most complete instrument analysis; two claims sharpened, none refuted.

- **CONFIRMED**: §2.2's 721.8× ABBA measurement (I reproduce 1.112 s vs
  802.805 s); §2.3's `d_rep ≡ D_234 − D_156` identity and the common-mode
  blindness; §2.4's four booleans; §2.5's opposite-sign duration decomposition
  and the bench-anchor flip; §2.6's grid-differential session factor; §2.7's
  `exponent_B ≡ k_B`; §2.8's negative `C₁₅₆` and both-endpoints-extrapolated
  finding; §2.9's per-scene noise floor (r=234 sample std **0.115%**, r=156
  **1.091%** dominated by one cold-start scene) and the not-scored sensitivity
  (replacing `U156/empty` with its repeat moves `G_sustained` +0.412% to
  `2.2552020`, `k_B` to `3.005696` — **toward exactly 3.0**, every verdict
  unchanged: *the central result is robust to the largest identifiable defect in
  its own inputs*, and that is the strongest thing anyone said for it);
  §2.10's 65%/47% source-anchored settling reproduction and **D-1's "~2 domain
  crossings" refutation**, which I independently reproduce at
  `geom_fixedabs_cpl`'s own STEPS (1.293 / 1.407 on **both** grids).
- **SHARPENED**: EM's bench anchor (+1.663%/−1.293%) uses the **mean** of each
  grid's sustained readings; THERMO's (+2.296%/−1.395%) uses the **first**. Both
  reproduce. **`R_DEG`'s own construction is single-reading, so THERMO's is the
  exact analogue and is the forward R17 anchor** (§1(b)); EM's is the disclosed
  alternative. Neither seat was wrong; neither stated why they differed.
- **SHARPENED**: EM's D-4 stops at `m6_directional_only`. The chain runs one
  boolean further — `m3_scored → False → may_move_logbook_verdict → False`
  (§1(b)).
- **CONFIRMED**: D-2's third value for the differential-floor ratio (`4.4653`
  hand-typed as the gate's own `expected`, against the computed `4.464601791167039`,
  passing only because `rel_bar` is 6.4× the disagreement).
- **REFUTED, in part**: EM's R20 tally of two and its ruling that R20 does not
  fire. Correct on EM's own slice; overturned on the union (§4). EM's standing
  observation — *"both new instances sit inside the `DISCLAIMER_115` string that
  MF-10 wrote to fix exactly this class — the correction machinery is now the
  place the class recurs"* — is exactly right and belongs in the LOGBOOK entry.
- **EM's §4b execution plan for D2 is assessed in §5(j) item 1**, where I found a
  material defect in its cost fork.

### 2.4 THERMODYNAMICS — **PARTIAL.** One conclusion refuted; everything else confirmed, including a defect nobody else could have found.

- **CONFIRMED**: §2.1's settling arithmetic (65.31% / 47.35% source-anchored);
  §2.2's MF-15 verification against exp-061; §2.3's honest self-refutation;
  §2.4's measured warm-up constants (`C₂₃₄ = +2.076 s/scene` against THERMO's own
  cloud-derived estimate of 35.08 — **16.9× smaller** — and `C₁₅₆` negative),
  and its withdrawal of the OV-3 request (*"I was wrong about the magnitude and
  Red Team was right about the method"* — recorded, with credit);
  §2.5's anchor flip; §2.6's **+5.63% / +6.02% monotone within-reading ramp on
  the r=234 SHORT reading, reproduced in both independent sessions and absent
  from every sustained reading** (I reproduce: s2 S234 +5.635%, s1 S234 +6.021%,
  every sustained reading ≤0.55% at r=234) — **this is the largest unmodelled
  systematic in the dataset, it sits inside the reading that sets `G_short` and
  the gate's second re-projection, and no instrument in the cycle records it**;
  §2.7's ramp-into-failure disposition of session 1; §2.8's one-datum-not-two
  point; **D1's cycle-spend arithmetic** (30 calls / 5919.009 s, understated by
  12 calls / 2218.503 s / 37.48% — §1(d)); D2's per-invocation gate; D3's R25
  resume-path deviation; **D5's `loadavg` class-rule finding** (§1(h)).
- **REFUTED**: §2.4's conclusion that *"`KAPPA_COST_EXPONENT = 3.2053` is a
  contention artifact of the cloud sandbox, not a property of this FDTD
  implementation."* The mechanism is adopted NOT-SCORED; the causal conclusion is
  refuted at the measured magnitude by PHOTONICS' F9(b), EM's §2.6 and my own
  §1(e) — the one contention lever we have measured accounts for 1/7.9 of the gap
  and its sign is protocol-inconsistent within that same pair. Four confounds
  move together. R5's look-elsewhere discipline binds.
- **NOTED**: THERMO's D5 references *"the Director's session context reportedly
  includes a Windows-side VC++ runtime installation at ~00:03Z"* and correctly
  observes it appears nowhere in the repository. It overlaps session 1's `U156`
  (00:02:42Z → 00:11:26Z) exactly and precedes the monotone 4.78 → 8.33%
  slowdown. **It is load-bearing on MF-6(e) and it must go in NOTES.md
  Idealizations** — PLAN.md's own resume recipe already instructs it.

### 2.5 QUANTUM OPTICS — **PARTIAL.** The sharpest statistical reading; one defect refuted.

- **CONFIRMED**: §2.1's bit-exact table; §2.2's v2 reconstruction to 17 digits
  and its correct ruling that nothing "closed"; the protocol-matched
  `G_E/f = 2.880173`, `|T−1| = 0.2202` — **the known protocol correction moves M6
  TOWARD non-transfer**, three multiplications, worth persisting; §2.3's
  mutual-AMBIGUITY finding (`G_E/G_bench − 1 = +0.22243`, `G_bench/G_E − 1 =
  −0.18196`, both inside the AMBIGUOUS window while each scores CONFIRM against a
  reference lying between them — **M5 is a containment test, not a replication
  test**); §2.4's four grounds against `favoured` (§1(e)); §2.5's five-row
  exponent table and its honest statistical statement; §2.6's R33(a) credit and
  the refutation of the magnitude warrant behind `sustained_choice_justification`;
  §2.7's session-1 analysis; §2.8's twice-carried MF-7(b) verification and the
  interval-scope finding; §2.9's R21 ruling; §2.10's two self-refutations,
  accepted without reservation.
- **CONFIRMED and elevated**: D-Q4 — *composition is one-directional.* MF-9 wired
  `m6_directional_only = f(m3_verdict)` and nothing gates `may_move_logbook_verdict`
  or `favoured` on M6's AMBIGUOUS. That is my own RT-13 closed one level and left
  open one level up. **The single persisted boolean
  `machine_transfer_caveat = (m6_verdict != "TRANSFERS")` is four lines of code
  and it belongs in the Iteration-93 bundle.**
- **REFUTED**: D-Q8 (the bench described as 8c/16t while `lscpu` reports 7c/14t).
  `NOTES.md` Setup already states it correctly and completely: *"Dell T5820, Xeon
  W-2145 (8c/16t), 128 GB — **WSL2 Ubuntu 24.04 sees 14 threads / 94 GiB**."* The
  record reproduces from its source. **Not a defect; struck from the tally.**
- **NOTED, correctly**: QUANTUM's Rank-3 σ(I) proposal names its own gate —
  Checkpoint criterion 3 (engine physics beyond the validated bench classes),
  requiring a new trust-suite stage with an absolute identity gate (`I → 0`
  reproduces the committed linear article bit-exactly). Naming your own gate
  before proposing is the behaviour this panel wants.

### 2.6 VISION SCIENCE — **PARTIAL.** The strongest single finding, and the best-prepared hand-off in the set.

- **CONFIRMED**: §2.0's thirteen-row re-derivation table (every row);
  **§2.1's MF-5 counterfactual, which is the finding I most want in the LOGBOOK
  entry** — evaluated at *this* cycle's own `G`, the un-fixed invocation returns
  `1.5**3.3689107 = 3.9195457`, `rel_dev = 0.0685753` → **CONFIRM**, the same
  verdict label from a `measured_ratio` wrong by 16.3%. *A wrong computation that
  agrees with the right one is indistinguishable from correctness by verdict
  alone.* MF-5 was load-bearing not because it changed this cycle's verdict but
  because without it the record would carry an unfalsifiable number under a true
  label. That is `lab/ARTIFACTS.md`'s invariant in its **false-positive** form and
  it is a new member of the class rule;
  §2.2's caveat-lint verification (I re-ran it: **16 caveats checked, 0
  required-site failures, exit 0**, and **2529 WARNs** at this tree — VISION's
  2495 was measured before the six Phase-5 reviews landed; both are correct at
  their own tree) and the live gap that `LOGBOOK.md` and `PLAN.md` — the two
  files that will carry the forward citation — are **not** in the new entry's
  `required_sites` (I confirm; `results.json` is in **neither** entry's);
  §2.3's LOGBOOK/PLAN supersession table including the **sign-flipped `excess`**;
  §2.4's M8 finding and its minimum-sufficient sentence; §2.5's M7 incoherence;
  §2.6's five-different-bars finding (stated `<1e-12`, coded `1e-15 … 1e-2`,
  with the two **load-bearing** differential-floor ratios at `1e-3`);
  **§2.7's drift correction, which reproduces to every digit (§1(b))** — and
  which VISION correctly refuses to score, naming the Iteration-1 estimator-
  switching rule itself;
  §2.8's free replicate; §2.9's joint reading of M5+M6.
- **CONFIRMED**: §2.10's three defects in D1. The **self-certifying class test**
  is the important one: *"any iteration whose proposal names a mechanism or a T1
  escape route"* lets a cycle become exempt from the seven metric rows **by
  declining to name a mechanism**, which is precisely what a drifting program
  does. VISION's fix (the class is assigned by the **Director in the Iteration
  entry**, plus a standing "consecutive governance-class cycles: N" counter on
  the charter page) is adopted into the Iteration-93 Tier-0 queue. Its other two
  — VISION's threshold duty left vacuous on governance cycles, and a hardcoded
  count that goes stale — are adopted with it.
- **VISION's §5 pre-registration sketch is assessed in §5(j) item 1.** It is the
  best-prepared hand-off any seat has produced in this program, and I ratify it
  with three amendments.

### 2.7 Conflicts adjudicated, consolidated

| Conflict | Ruling |
|---|---|
| PHOTONICS **CONFIRM** vs five **PARTIAL** | **PARTIAL.** §2.1. |
| MATERIALS ("headline understates by 3.38×") vs PHOTONICS ("headline appears to exceed the bound by 28×/102×") | **Both correct; not a conflict.** Two different normalizations. The bound may only be stated in the **peak-normalized** frame where it is commensurable; the local-normalized figures are a separate, floor-gate-dependent statement requiring median + p90 + max + SNR + absolute `\|Δ\|` across **all six** margins. §1(f). |
| EM `+1.663%/−1.293%` vs THERMO `+2.296%/−1.395%` | **Mean-of-sustained vs first-sustained. Both reproduce. THERMO's is `R_DEG`'s exact construction and is the forward R17 anchor; EM's is the disclosed alternative. M3 flips either way.** §1(b). |
| VISION's drift route (M3 → PARTIAL) vs EM/THERMO's anchor route (M3 → NOT-INVARIANT) | **Both hold, on different routes with different reach.** Route 1 flips `m6_directional_only`; Route 2 additionally flips `m3_scored` and `may_move_logbook_verdict`. §1(b). |
| THERMO "`k = 3.2053` is a cloud-contention artifact" vs PHOTONICS/EM/QUANTUM | **THERMO REFUTED at the magnitude; mechanism adopted NOT-SCORED.** §1(e). |
| MATERIALS "two gate checks cannot fail" vs PHOTONICS "the bit-identity gate correctly cannot fail" | **Different checks. Both right.** §1(f). |
| EM R20 = 2 (no fire) · MATERIALS R20 = 3 (deferred to me) · PHOTONICS R20 = 0 | **Each correct on its own slice; the union is six. R20 FIRES.** §4. |
| QUANTUM D-Q8 (7c/14t) | **REFUTED.** `NOTES.md` Setup states both figures correctly. §2.5. |
| VISION 2495 WARN vs my 2529 | **Both correct at their own tree.** Not a conflict. |
| EM D-7 (`d_rep` denominator `/G1` vs `/Ḡ`) | **A convention note, not a defect.** State the denominator; do not change the code. |

---

## 3. R21 / R23 discharge list — what the Director's Result section and LOGBOOK close MUST contain

**R23 and its First Addendum are DISCHARGED.** Verified by me and independently
by four seats: `DISCLAIMER_115` (3788 chars) is a literal substring of **both**
`predictions_text` and `result_text` in committed `results.json`; both builder
functions carry internal asserts (`run115.py:1185`, `:1252`); `analyze115.py:259`
and `:277` assert both sides; and there are **two committed, re-invocable call
sites** (`run115.py --predictions-only`, `run115.py --selftest`), the second of
which was executed at Phase 3 with synthetic operands before any bench data
existed. PHOTONICS reproduced both texts byte-for-byte from committed code alone.
**This is the first cycle where R23's First Addendum can be certified from the
artifact rather than from the promise.** Nothing further is required.

**R21 is NOT discharged, and it fires automatically if the close lands without
the list below.** R21's forward clause makes a third occurrence of "a persisted
byproduct field's own headline finding never stated in Result/Learned prose," on
this or any T28-adjacent channel, an automatic Checkpoint-4. Four seats
independently found the exposure; all four ruled it should not fire *because
`NOTES.md`'s Result section does not yet exist* (`NOTES.md:619-625` = `(pending)`),
so no frozen record omits anything. **I concur — and I convert their conditional
into a hard, checkable list. If the Iteration-92 close is written without any
numbered item below, R21's third occurrence is post-freeze and Iteration 93's
Red Team audit must treat it as fired.**

### 3.1 MANDATORY in `NOTES.md § Phase 4 — Results` (and mirrored in the LOGBOOK close)

1. **The corrected M9 bound, verbatim**, in the form authorized in §1(f). The
   `results.json` self-certification string *"R21: stated here, not merely
   persisted"* must be **deleted or relocated** — "here" is `results.json`,
   which is the artifact R21 names as insufficient.
2. **M8 (Tier-1 item 2), NOT scored** — the queue item this cycle folded in, with
   no prose headline anywhere:
   > At the measured `G = 2.2459405`, the v2 re-normalization gives
   > `measured_ratio = 3.2113911` (signed dev `−0.1244870`), **below** the sign
   > boundary `G ≥ 2.5652851` — **the v2 straddle remains OPEN**, as MF-8
   > pre-registered it would over 66.35% of M5's own CONFIRM band. The two
   > pre-run sensitivities are unchanged: short-reading `measured_ratio =
   > 4.4310989`, `rel_dev = 0.20803870` (AMBIGUOUS); v2 `measured_ratio =
   > 3.2171956`, signed dev `−0.1229045` against the filed `+0.1227499` —
   > **opposite sides** of `reference_ratio`, a 28.0% spread between central
   > estimates. None is scored; none may move a LOGBOOK verdict.
3. **MF-1's 3λ row**: `2·exp(−τ)` = `3.5757 / 5.1793 / 7.3480 ×10⁻⁴` at
   450 / 600 / 750 nm; `τ_true` = `8.629338 / 8.258813 / 7.909063`; **backing
   freedom is weakest in the red (2.055× worse at 750 nm than 450 nm) and has
   been MEASURED only at 600 nm** — with PHOTONICS' two clarifications (`cpl` in
   that row is the **physical** `λ/dx` and carries no discretization confound;
   the shell stays above `graded_black_shell`'s own 1.5λ entry-reflection bar
   even at 750 nm, at 1.92λ) and MATERIALS' F8 disclosure (**the 450/750 nm rows
   assume a frequency-independent σ**).
4. **MF-3's peak-normalized companion, inside the quotable bound**:
   `1.4760×10⁻⁴` (r=156) and `1.5266×10⁻⁴` (r=312), and PHOTONICS' reconciliation
   — **`0.285×` / `0.295×` of `2·exp(−τ_true)`, so the corrected coherent
   cross-term bound is honored at ALL 48 bins at BOTH radii**, and the printed
   28.3× / 102.1× local-frame figures are **exactly** the normalization change
   (`99.382×` / `346.532×`), not a violation.
5. **M7's model comparison, restated**: `NO MODEL FAVOURED` per §1(e), with the
   0.18% / 8.15% / 13.42% / 6.08% figures and the NOT-SCORED DRAM-bandwidth
   reading.
6. **`exponent_B ≡ k_B` identically** — M5 and M7 are one number scored against
   two bands, not two confirmations.
7. **The cycle-scope spend**: *30 `Sim.run()` calls and 5919.0 s across two
   sessions (session 1: 12 calls / 2228.7 s; session 2: 18 calls / 3690.3 s of
   `Sim.run`, 3700.5 s elapsed) = 54.8% of `COST_GATE_TOTAL_S`*, replacing
   *"18 real FDTD calls … this cycle."* With the statement that **the R19 assert
   and the R27/R28 gate are both per-invocation by construction** and that a
   twice-interrupted cycle could spend 2–3× the bound with every gate reading
   PROCEED.
8. **The M3 anchor disclosure**, verbatim as drafted in §1(b), including
   `R_DEG_bench = 0.022961` (and the mean-form alternative `0.016630`), the
   VISION drift-corrected `−4.123%` → PARTIAL, and the full boolean chain
   `m3_scored → False`, `m6_directional_only → True`,
   `may_move_logbook_verdict → False` under a bench anchor. **Explicitly NOT
   scored; R17 satisfied at freeze.**
9. **The session-1 across-reboot replicate**, as
   `sensitivity_session1_across_reboot_DO_NOT_SCORE`: four readings, `G_short
   2.3005776`, `G_pair1 2.2922399`, `k = 3.0458713`, `rel_dev 0.0626091`,
   `excess +1.8773%`; per-step levels `+4.775 / +4.208 / +5.369 / +8.328%`;
   `G` spread **+2.808%** against the matching pair (**1.92× `d_rep`**) and
   **+2.061%** against the ABBA mean; the ramp-into-failure caveat
   (progressive, tail-weighted, `U234` immediately preceding the host hang);
   and **the statement that admitting it changes no verdict and flips no
   composition boolean** (3-pair `G = 2.2613736`, `k = 3.0124356`,
   `rel_dev = 0.07523` CONFIRM, `excess +0.5055%` N2_HOLDS, `|T−1| = 0.17634`
   AMBIGUOUS).
10. **The two-session structure and the bench outage in `NOTES.md`
    Idealizations**, per PLAN.md's own instruction — including the Windows-side
    VC++ runtime installation at ~00:03Z if the Director can source it, which
    overlaps session 1's `U156` exactly, and the fact that
    `data/cg_session1_interrupted.log` contains **two lines** (the ticker output
    did not survive — the same shape as exp-114's lost scratch log, one cycle
    later).
11. **The exclusive-use instrument's real evidence**, per §1(h) below.
12. **The R25 numbered disclosure of the resume-path deviation** (§1(d)): the
    executed path is a **third** branch, not one of PLAN.md's two; it was the
    better choice; it is disclosed, not silently improved.
13. **The joint reading of M5 + M6** (VISION §2.9, QUANTUM §2.3): the bench's
    `G = 2.2459405` and the cloud's `G_E = 2.7455057` sit on **opposite sides**
    of `reference_ratio` and **both score CONFIRM**, while differing from each
    other by **18.20%** — above M6's own **15.295%** transfer bar. **M5's CONFIRM
    band is wider than the between-machine spread it must survive**, and this
    cycle's central estimate `k_B = 2.9955462` is **0.149%** from the pre-R28
    exponent `k = 3.0`. Plus QUANTUM's protocol-matched `G_E/f = 2.880173`,
    `|T−1| = 0.2202` — the known protocol correction moves M6 **toward**
    non-transfer.
14. **The honest `KAPPA_COST_EXPONENT` statement**, verbatim as ruled in §1(e),
    including the five-row table, the four simultaneous confounds, the explicit
    refusal of the contention-artifact conclusion, and the retention of `3.2053`
    for the gate **as a labelled gate-margin choice**.
15. **The six shipped-FALSE corrections** (α–ζ, §1(f)) as forward corrections,
    each with the reproduced value: the margin-32 persistence claim; the 330×;
    the MP-5 conditional; the "even allowing 4×" (45.0× / 863.7×, and the r=156
    closure bound `4.9932×10⁻⁸` → 113.5× / 28.4×); the "~2 domain crossings"
    (**1.293 / 1.407 on both grids**); the 4.47/4.46/4.4653 triple. Plus the
    exact bracketing statement replacing "the SAME ORDER": **2.38×–45.70× below
    the scale, 4.76×–91.41× below the bound**.
16. **The R18 corrections**: the M9 gate **withholds the headline string, it does
    not HALT** (`c_physics["withheld"]` keys on 2 of 11 checks; every other
    sub-dict is persisted regardless of status); the reproduction gate is stated
    at `<1e-12` and coded at `1e-15 … 1e-2`, with the two **load-bearing**
    differential-floor ratios at `1e-3`; two of the eleven checks compare
    literals written on the same line and cannot fail; `σ_abs`, `σ_ext` and both
    channel-sum residuals are never gated.
17. **The `lab/sections.py` angle-convention finding** and its blast radius:
    exp-115's `±138.75°` claim is **correct under the code** and inverted under
    the docstring it cites four lines away; the defect has stood since exp-017
    (`NOTES.md:22` propagates it verbatim); it sits under PANEL.md's constraint-2
    row; it is Iteration-93 Tier-1 item 2.
18. **The instrument's own positive results**, so the entry is not read as a
    catalogue of defects: ABBA measured at a **721.8×** lag reduction (1.112 s vs
    802.805 s, pairwise lags symmetric to 0.277%); `d_rep ≡ D_234 − D_156`
    exactly, and **common-mode drift cancels in it identically** — with the
    statement that `d_rep` and the drift block are **two quantities and their
    difference, not three pieces of evidence**; the per-scene replicate floor
    (r=234 sample std **0.115%**; r=156 **1.091%**, dominated by one cold-start
    scene); EM's not-scored robustness check (replacing `U156/empty` with its
    repeat moves `G_sustained` +0.412% and `k_B` to `3.005696`, **toward exactly
    3.0**, with every verdict unchanged); PHOTONICS' F10 ruling that the two
    opposite-signed drift rates mean **no drift systematic is resolved at this
    precision** and must not become a future R17 anchor; VISION's MF-5
    counterfactual (**the un-fixed route returns a false CONFIRM at this cycle's
    own `G`**); THERMO's **+5.63% / +6.02% r=234 short-reading ramp**, reproduced
    in both sessions and unmodelled by anything in the cycle; and the fact that
    **both pre-registered protocol models were refuted by the measurement**
    (`2.5403` and `2.8681–2.8802` against `2.2459`), with the warm-up constant
    measured **16.9× below** its cloud-derived estimate — pre-registering two
    models and having the data reject both is house discipline working.
19. **The per-grid duration decomposition persisted**: `+2.296%` (r=156) /
    `−1.395%` (r=234) at matched protocol, opposite signs — **R31/R33's founding
    grid-independence assumption is measured false at the 2–3% level on one clean
    machine**, twice and in two independent ways (within-session duration
    response, and the session-1-vs-2 grid-differential slowdown of 2.96 pp).
    This is the cycle's best physics-of-the-instrument result and it exists in no
    committed file.
20. **The MF-15 vacuous discharge stated as such**: no warm-up sensitivity is
    persisted because MF-7(a)'s **measurement** superseded the estimate — a good
    outcome that nothing currently records.

### 3.2 MANDATORY corrections to LOGBOOK's Phase-4 paragraph (and PLAN.md's Current state)

The Iteration-92 record's Phase-4 paragraph and `PLAN.md:24-79` both quote the
**INTERRUPTED session-1 numbers as this cycle's readings**, and one of them is
**sign-flipped**. Every figure below is superseded:

| Quantity | LOGBOOK/PLAN as written (session 1) | Correct (session 2, scored) |
|---|---|---|
| `S156` per-step | `0.050909` | **`0.04858939027786255`** |
| `S234` per-step | `0.117121` | **`0.11239203476905822`** |
| `U156` per-step | `0.052374` | **`0.04970505291927912`** |
| `U234` per-step | `0.120053` | **`0.11082375609762692`** |
| `G_short` | `2.3006` | **`2.3130982736423493`** |
| `G_sustained` | `2.2922` (one pair) | **`2.245940496842567`** (ABBA mean of two) |
| `excess` | **`+0.0188`** | **`−0.0018042236255256805`** — **SIGN FLIPS** |
| `\|T−1\|` | `0.165` | **`0.1819574315523479`** |
| bench short→sustained shift | `+2.9%` | **`+2.296%` (r=156)**, and **`−1.395%` (r=234)**, opposite signs |

Required rewrites, verbatim in substance:

- **The Phase-4 paragraph must state that Block CG was run TWICE.** Session 1
  (2026-09-05T23:54:14Z → 2026-09-06T00:31:28Z, four readings, 12 calls,
  2228.7 s) was interrupted by the host outage and is **retained as committed
  data and scored NOWHERE**. Session 2 (2026-09-06T04:39:25Z → 05:41:04Z, six
  readings, 18 calls, 3690.3 s of `Sim.run`) is the complete ABBA block and is
  **the sole scored source**. Every session-1 figure previously quoted is
  superseded, `excess` in sign.
- **The resume path must be disclosed as a third branch** (R25), with its reason
  and the statement that it was the better choice.
- **The paragraph's own characterization "bench short→sustained shift +2.9%, vs
  the cloud's `R_DEG = +7.6%` — a steadier instrument"** must be replaced by the
  per-grid, opposite-signed decomposition and the anchor ruling of §1(b). As
  written it reports the ratio's magnitude as if it were a single-grid duration
  response, which is exactly the conflation MF-9's mechanism-neutral labels exist
  to prevent.
- **`PLAN.md`'s "Current state" must be rewritten to Phase 5 complete**, with the
  session-2 figures, and its resume recipe struck as executed.
- **`lab/caveat_lint_config.json`**: add `LOGBOOK.md`, `PLAN.md` **and**
  `results.json` to `exp115-t28-fabrication-tolerance-bound-certified-resolution`'s
  `required_sites` **at the moment the bound is written into them**, and update
  the entry's required phrase to the corrected scope wording of §1(f) — the
  entry currently **compels** every citing document to repeat a scope sentence
  whose stated reason is false. Two lines plus a phrase; it must ride with the
  Result section, not wait for Iteration 93.

---

## 4. Checkpoint ruling, R20 tally, R34 status

### 4.1 Criterion by criterion

| # | Criterion | Ruling | Reason |
|---|---|---|---|
| **1** | A configuration passes ALL constraint metrics | **DOES NOT FIRE** | Zero constraint metrics recorded. This is a governance-class cycle under PANEL.md's Iteration-92 scope amendment; `DISCLAIMER_115` declares `T1 escape route: NONE / N/A` on both sides, and I verified structurally that the executed path contains no constraint instrument. Neither Tier W nor Tier A is addressed. |
| **2** | A proven boundary: a constraint subset jointly unsatisfiable within a whole mechanism class, gates clean | **DOES NOT FIRE** | Nothing in this cycle bears on any mechanism class. The one queued item that could reach criterion 2 — QUANTUM's primary-source RSA/TPA check — is not executed here and is gated on a T18 probe that has never returned. |
| **3** | A synthesis requires engine physics beyond the validated bench classes | **DOES NOT FIRE** | Zero `lab/` diff; the identity gate proves `build_sim` byte-identical to `chunk_runner114`'s. **Flagged forward, not fired:** QUANTUM's Rank-3 σ(I) two-intensity proposal *will* fire criterion 3 when proposed, and names its own gate correctly. |
| **4** | Red Team flags program-integrity drift | **FIRES — on R20's automatic clause. Notification, not a pause.** | §4.2. |
| **5** | Two consecutive iterations with no logbook-advancing result | **DOES NOT FIRE** | exp-114 advanced (the first `kappa_ratio ≠ 2.0` calibration point, CONFIRM-WITH-NAMED-GAPS). exp-115 advances: the **first per-step control ever measured on any grid but r=156** in this program's history; `G` measured same-session, same-machine, matched-protocol, R33-immune by construction; both pre-registered protocol models refuted by data; MATERIALS' seven-cycle fabrication debt written; `N²` to 0.18%; a bench-native R31 anchor every future cycle inherits. **Named as a standing observation for the Director, not a firing:** this is the fifteenth consecutive governance-class cycle and the sixth consecutive cycle at or above R20's density bar. Criterion 5 does not reach a class of cycle that keeps advancing the *instrument* logbook while the constraint-3 ledger gains nothing; **D2 is the correct answer to that and it is already ruled.** |

### 4.2 Criterion 4 FIRES — R20, six independent R4-class defects

R20's operative text: *"three or more independent R4-class defects … surviving a
document's own Phase-3 prediction-freeze into its Result/Learned sections, each
caught only at Phase 5 — not earlier — in a single document, constitutes a
Checkpoint-4-grade recurrence pattern **on its own, independent of whether any
individual instance is load-bearing to a scored verdict** … fires Checkpoint
criterion 4 automatically, **no further deliberation**."* R20 is not on its
founding instance; its non-firing precedent does not apply.

**The tally, each verified by me from primitives this session, each introduced at
or before Phase 3 and each caught only at Phase 5:**

| # | Defect | Where (frozen) | Caught by |
|---|---|---|---|
| 1 | *"~2 domain crossings"* → **1.293 / 1.407** on both grids at `geom_fixedabs_cpl`'s own STEPS | `DISCLAIMER_115`, in **both** `predictions_text` and `result_text` | EM D-1 |
| 2 | *"4.47×"* hand-typed beside the committed function's own `4.4646` (printed `4.46×` in the same document), with the gate's own `expected = 4.4653` a third value | `DISCLAIMER_115` + `b_floor…reading` + `result_text` | EM D-2, MATERIALS D12 |
| 3 | *"only the margin-32 array is persisted"* — true of exp-108, **false of exp-110**, the channel the headline quotes (all six margins persisted) | `d_scope.margin_scope`, in the quotable headline's justification | MATERIALS D4 |
| 4 | *"330× looser than the quoted figure"* — reproduces only against the **withdrawn** peak-normalized figure; against the quoted one it is 3.4× and **0.95× (tighter)** | same clause, and the headline | MATERIALS D6 |
| 5 | *"even allowing a 4× standing-wave enhancement"* — the 180×/3455× ratios are computed **without** the 4× (45.0×/863.7× with it) | `perturbation.closure` | MATERIALS D10 |
| 6 | MP-5 forward conditional *"survives and **strengthens** … `τ_true` grows with thickness"* — MP-5 holds `τ_true` **fixed** by its own definition | `e_tier.forward_conditional` | MATERIALS D9 |

Struck from the tally so the count is honest: QUANTUM's D-Q8 (**refuted**,
§2.5); THERMO's D1 (a wrong **scope of words**, ruled R21/R4-adjacent in §1(d),
not a citation defect — counting it would double-count); MATERIALS' D13 (an
absolute-vs-relative slip, R9); VISION's D4 (R18, not R4). **Six clean instances
against a bar of three.** Instances 1–4 sit in `result_text`, which is currently
the **only** Result prose in the repository.

**No individual instance is load-bearing to a scored verdict, and every one is
desk-correctable at zero FDTD cost. I therefore rule this firing a
NOTIFICATION, NOT A PAUSE.** Under **R34** it self-closes the moment Iteration
93's Red Team final audit confirms, from primitives, that §3's discharge list
has landed. **Marsh is not convened** — R34's conditions for convening
(a firing ruled a pause, or one still undischarged after the next iteration's
audit) are not met.

**The observation that gives the firing its teeth, and that I want on the
record in EM's own words:** *"both new instances sit inside the `DISCLAIMER_115`
string that MF-10 wrote to fix exactly this class — the correction machinery is
now the place the class recurs."* My own Phase-2 audit already recorded this as
the sixth consecutive cycle at or just under R20's density bar. It is now over
it, and the density is concentrated in the single-source-of-truth string this
program built to stop disclaimer erosion. **A single-source-of-truth string that
is never independently re-derived is a single source of *un-audited* truth.**
The Iteration-93 discharge must therefore include a re-derivation pass over
`DISCLAIMER_115`'s own arithmetic claims, not only a correction of the six.

**R21's third-occurrence clause: DOES NOT FIRE, conditionally.** §3. Four seats
found the exposure; `NOTES.md`'s Result section is `(pending)`, so no frozen
record omits anything; the founding-instance precedent (caught blind, inside the
cycle's own review layers, before LOGBOOK) applies. **It fires automatically if
the Iteration-92 close is written without §3.1's twenty items.**

**Rules checked and NOT fired**, so the absence is on the record: **R23 + First
Addendum** (discharged, §3); **R24** (all fifteen mandatory fixes are wired into
code; the two disclosed partials — MF-14's §2.0 T18 placement rerouted to Phase-3
sites because Phase-1 documents are frozen, and MF-13's "five orders" carried
forward as a disclosed correction — are disclosed, not claimed-and-unwired);
**R25** (the declines are numbered, `DECLINE_8` exists; the two new disclosures
required in §3.1 items 9 and 12 are what keep it from firing); **R17** (satisfied
at freeze; the forward anchor ruling is a disclosure, not a violation);
**R19** (the assert exists, is conditional, and is honest about its scope — the
prose that quotes it is what is wrong); **R27/R28** (executable, upstream, no
breach at 54.8% of the bound); **R29** (module identity asserts executed);
**R30/R32** (correctly declared N/A); **R31/R33** (M5 is R33-immune by
construction; addendum (a) honored in full and better than asked; addendum (b)
discharged by direct grid-native measurement, which is the whole cycle);
**R13** (correctly withdrawn per MF-2 rather than mislabelled).

### 4.3 R34 status of the program-level Iteration-92 Checkpoint-4

The Iteration-92 CHECKPOINT entry fired criterion 4 at **program level** on the
ground that PANEL.md's Metrics section no longer described the program it
governs, ruled it a notification, and pre-registered its own closure condition:
*"Under R34 this firing self-closes when **Iteration 93's** Red Team final audit
confirms D1 and D2 discharged from primitives."*

**I am Iteration 92's Red Team — the same iteration that fired it. It does NOT
self-close here, and I decline to close my own firing.** R34's text requires *"a
**later** iteration's Red Team final audit."* What I can and do confirm from
primitives:

- **D1 — VERIFIED PRESENT.** `PANEL.md:153-167` carries the "Scope amendment
  (Director, Iteration 92, 2026-09-05)". It names the class test, names exp-101
  as the start, points at `lab/ambient.py`, declines to endorse the practice as
  permanent, and carries D2's ruling. **Three defects in it are confirmed
  (VISION §2.10) and become Tier-0 items**: the class test is **self-certifying**
  (a proposal exempts itself by declining to name a mechanism — precisely what a
  drifting program does); VISION's charter threshold duty (`PANEL.md:86-87`,
  `:150-151`) is left unamended and is now **vacuous on the majority class of
  cycle**; and the hardcoded *"unrun since exp-100 (14 cycles)"* count went stale
  the day it was written (exp-115 makes fifteen). I independently re-ran the
  underlying grep: `weber(|contrast_from_runs|observer_profile` returns nothing
  in `experiments/*/*.py` after exp-100. **Write it as "since exp-100 (Iteration
  77)" with no count.**
- **D2 — VERIFIED AS A RULING, on the record in three places** (`PANEL.md:164-167`,
  the LOGBOOK CHECKPOINT entry, `PLAN.md:33-35`). **Verified as EXECUTED: not
  yet, and cannot be until Iteration 93 runs.** That is the half only Iteration
  93's audit can confirm.

**Ruling: the Iteration-92 program-level criterion-4 firing remains OPEN and
carries to Iteration 93's Red Team final audit, exactly as its own entry
pre-registered. Marsh is not convened.** The new R20 firing of §4.2 rides the
same closure mechanism.

---

## 5. COMBINED VERDICT, and the Reconciled Iteration-93 queue

### 5.1 Verdict

# PARTIAL

**T1 escape route: N/A — unanimous across all seven seats, and verified
structurally by three of them independently.**

Seats: PHOTONICS CONFIRM; MATERIALS, EM, THERMODYNAMICS, QUANTUM, VISION
PARTIAL. **I overturn PHOTONICS' CONFIRM (§2.1) and file PARTIAL.**

**Why not CONFIRM.** The measurement half is CONFIRM-grade and I say so
without qualification: every scored statistic reproduces bit-exact from
primitives at six independent seats and again at mine; the pre-registration is a
**verified property of the git tree**, not a claim; the MF-12 identity gate is a
real absolute gate (10/10, `build_sim` byte-identical); the bench trust suite is
41/41 with its platform named and committed; ABBA worked and I measured a 721.8×
lag reduction; the budget gate branched three times upstream of spend; R23's
First Addendum is discharged from the artifact for the first time in this
program. **The record half fails.** `NOTES.md`'s Result section does not exist;
LOGBOOK and PLAN quote a superseded session, one figure in sign; six independent
R4-class defects sit in the frozen text (R20 fires); three mandated Phase-2 fixes
and an entire declared deliverable (M8) are persisted and un-narrated; the
quotable bound's scope clause is false against the instrument it governs and its
one constraint-adjacent sentence reports as bounded a channel that is
**unmeasured at ten of twelve cells**; and M3's verdict — which gates
`m6_directional_only` and, through `m3_scored`, `may_move_logbook_verdict` — does
not survive correction by the cycle's own persisted data on **two independent
routes**. In this program the record is the product. That is PARTIAL.

**Why not RULED-OUT.** Nothing here is ruled out. Every defect is
desk-correctable at zero FDTD cost, no scored verdict reverses, and the cycle
delivered four things the program did not have: the **first per-step control ever
measured on any grid but r=156**; a matched-protocol, same-session, single-machine
`G` that is R33-immune by construction; the **first bench-native R17/R31 anchor**;
and MATERIALS' seven-cycle fabrication debt written as a quotable, caveat-gated,
arithmetic-reproduced bound. OV-2 — decline the eighth deferral — is vindicated.

### 5.2 Verdict-framing ruling: what this cycle may and may not move in exp-114's LOGBOOK entry

**MAY:** add a **forward disclosure** to the Iteration-91 entry (this program's
established practice — never retroactively edit a frozen entry) recording that
exp-114's `G_E = 2.7455057` / `k = 3.4909` is **not reproduced on a second
machine at the same `kappa_ratio`**: the bench gives `G = 2.2459405` /
`k_B = 2.9955462` (scored) and `2.2922399` / `3.0458713` (session 1, not scored);
the two machines sit on **opposite sides** of `reference_ratio` and **both score
CONFIRM** while differing by **18.20%**, above M6's own **15.295%** transfer bar;
M6 reads **AMBIGUOUS**; and the protocol-matched cloud value `G_E/f = 2.880173`
moves M6 **further** from transfer (`|T−1| = 0.2202`).

**MAY NOT:**

- **May not upgrade** exp-114's `CONFIRM-WITH-NAMED-GAPS` to anything stronger.
  M5's CONFIRM is a **containment** result — `rel_dev ≤ 0.15` on a band 30% wide
  in ratio space, wider than the between-machine spread it must survive — and
  MF-7(b) pre-registered that a CONFIRM cannot distinguish `k = 3.2053` from
  `k = 3.0`. This cycle's own central estimate is **0.149% from 3.0**.
- **May not remove** any of exp-114's named gaps. None was closed here.
- **May not claim** that `KAPPA_COST_EXPONENT` is a cloud-contention artifact
  (§1(e)), nor that `k = 3.0` is restored program-wide: `k` was fitted at
  `kappa_ratio = 2.0`, this cycle establishes nothing at any other ratio, and the
  machine and protocol axes are unseparated.
- **May not rest on `may_move_logbook_verdict = True` without the anchor
  disclosure** of §1(b): that boolean is `False` under any bench-native anchor.
- **May not cite the M9 bound as shipped.** Corrected form only (§1(f)), and the
  caveat-registry entry must be updated in the same motion.
- **`KAPPA_COST_EXPONENT = 3.2053` stays in force for the cost gate**, labelled a
  gate-margin choice.

### 5.3 The Reconciled Iteration-93 queue

Merging all six ranked lists into one structure, bundling genuinely-the-same fix
rather than treating sub-proposals as competing (exp-113/114 precedent).

#### Tier 0 — governance

**0.1** Record the **R20 criterion-4 firing** (§4.2) as a CHECKPOINT entry —
notification, not a pause, six instances listed, closure condition = Iteration
93's Red Team audit confirming §3's discharge list. Marsh not convened.

**0.2** Carry the **Iteration-92 program-level criterion-4 firing OPEN** to
Iteration 93's audit (§4.3). D1 verified present, D2 verified as a ruling; D2's
execution is Iteration 93's to demonstrate.

**0.3** **Repair D1's three defects** (VISION §2.10, adopted): the
governance-vs-phenomenon class is assigned by the **Director in the Iteration
entry**, never self-certified by the proposal; PANEL.md carries a standing
**"consecutive governance-class cycles: N"** counter on the page a fresh seat
reads first; VISION's threshold duty on a governance cycle is stated as
**discharged by the DISCLAIMER's constraint-3 N/A sentence and by nothing else**;
the hardcoded cycle count becomes *"since exp-100 (Iteration 77)"*.

**0.4** **Ratify the forward R17 anchor rule**: where a tolerance/bracket
quantity is venue-dependent, its anchor must come from the **venue the run
executes on**. The cloud `R_DEG` is retired for bench cycles; `R_DEG_bench =
0.022961` (first-reading construction, `R_DEG`'s own analogue) is the anchor of
record, with `0.016630` (mean construction) as the disclosed alternative.

**0.5** **`COST_GATE_TOTAL_S` wall-clock-vs-compute policy fork** — unchanged,
still Marsh's own call, carried from Iteration 89. Not a discovered defect.

**0.6** **Ratify or reject**: a cost/safety gate must bound the **cycle**, not
the process (§1(d)). If ratified it becomes a rule; the code half is Tier-2
item 6.

#### Tier 1 — Iteration 93's three items

**1. [FIXED by D2] VISION SCIENCE's constraint-3 re-score of the program's only
Tier-W/Tier-A citation, through the modernized `lab/ambient.py`. EM leads by
rotation; VISION pins the thresholds.**

*Assessment of VISION's §5 sketch: the best-prepared hand-off any seat has
produced in this program, and I ratify it.* It names the exact target (exp-047 /
Iteration 24, P-G24-2, `C_MEASURED = −0.7209` from exp-030, **not** exp-020's
superseded `−0.686`); it pins T-1..T-7 with sources; it puts the leverage where
it actually is (PHOTONICS' Iteration-24 closed form means a re-measurement of `C`
**cannot** move the Tier-W verdict — the leverage is entirely on the threshold
and glare-model side, which is VISION's own); it makes **S-A the positive control,
mandatory and first**, with HALT semantics; and its P1 anchors are R17-compliant
and drawn from the channel's own record (`0.0186` = exp-033's measured
cross-resolution shift; `0.0509` = the largest same-article headline move on
file). **Two elements I single out as the best things in it:** T-6, where VISION
declares its own MARGINAL band **UNSOURCED** and commits to sourcing it or
reporting PASS/FAIL only — a seat retiring its own instrument rather than scoring
against an unsourced threshold; and **T-7, the decidability floor**, which is a
threshold on the *instrument* rather than the article and is exactly the
discipline this program keeps having to re-learn.

*Assessment of EM's §4b execution plan: structurally correct, with one material
defect I found from primitives.* The five pin-items, the MF-12-pattern absolute
identity gate, the **positive control as the non-negotiable half**, the
signature/interface check and the platform-named trust-suite record are all
right, and EM's insistence that a fifteen-cycle-dormant instrument is **new
machinery** under PANEL.md's own Phase-4 house rule is correct.
**The defect: EM's cost fork — *"if exp-100's captures are committed, the entire
re-score is zero FDTD"* — is unavailable. `experiments/100-t28-delta-scene-
constraint-scoring-pass/` has NO `artifacts/` directory; the captures are not
committed.** Iteration 93 must budget **real FDTD** and must project it from a
**bench-native per-step rate at the geometry actually run** — and note that
VISION's S-A is the exp-030 `r=78`-native ±35° configuration, for which **no
bench rate exists**; the bench has measured only r=156 and r=234 at cpl=25
(`3 × 8000 × 0.0493975 = 1185.5 s` and `3 × 12000 × 0.1109387 = 3993.8 s`). Take
a short r=78 control burst first, or project explicitly conservatively and say
so.

**Three amendments I attach to item 1:**
(a) **Iteration 93 is a phenomenon-program cycle, not a governance cycle** —
VISION §5.6(1) is right and it is the direct answer to D1's self-certification
hole. It declares its escape route as **σ(I)**, and it **records the seven metric
rows or states per row why not**. A thirteenth consecutive `NONE` would be wrong
on the amendment's own text.
(b) **S-A HALTs the cycle on NOT-REPRODUCING**, and *the failure is the result* —
a fifteen-cycle-stale instrument is a finding, not a wasted slot.
(c) **P3's pre-registered "36/36 out of calibration" outcome must be flagged in
advance as potentially checkpoint-relevant**: if it lands, exp-047's "170×
margin" is **withdrawn as un-scoreable** and Tier W returns to open. That is a
real result about the program's only Tier-W claim, at zero FDTD cost, and it must
not be framed as a failure of the cycle.

**2. `lab/sections.py`'s angle-convention correction, a positive control for it,
and a re-audit of every angular claim in the record.** *(PHOTONICS Rank 1;
MATERIALS D14; independently confirmed by me. Zero FDTD except a trust-suite
re-run.)*

Fix the docstring at `:209-210` and `:223-224` to `0° = +x = forward /
downstream`, `±180° = −x = backward, toward the source and the observer`, with
the one-line justification. **Arm a positive control in the trust suite**: assert
the argmax bin of a `graded_black_shell` pattern lies within ±30° of 0°. Then
grep and re-audit every "forward"/"backward"/"observer-return"/"backscatter"
angular-sector claim in `experiments/` against the corrected convention, and
annotate `experiments/017-.../NOTES.md:22` with a dated correction rather than
editing history.

**Why item 2 and not the bound re-issue:** it is a live R18-class defect in
**shared `lab/` machinery** that has stood since the instrument's founding cycle,
it sits directly under PANEL.md's **constraint-2** metrics row, and **both** item
1's angular scoring and item 3's re-issued bound quote the phrase
"observer-return hemisphere." This must land first or both inherit an unverified
convention. The positive control is the part that matters: it is a check that
*can* produce the reading meaning "bad," which is this program's own class rule,
and it would have caught the inversion.

**3. The zero-FDTD re-issue of the fabrication-tolerance bound at full scope,
bundled with the complete R20/R21 discharge.** *(MATERIALS Rank 1 + PHOTONICS
Rank 2 + QUANTUM Rank 2 + EM Rank 2 + THERMO Rank 2 + VISION's config half —
six seats converged on one document pass; bundled, not split.)*

(i) Recompute the per-bin channel at **all six** margins and report **median +
p90 + max + SNR-at-max + absolute `|Δ|`**, not max alone; strike "only the
margin-32 array is persisted"; correct "330× looser". (ii) Report the
observer-facing face as **UNMEASURED at 10/12 cells**. (iii) Correct the MP-5
forward conditional to **invariant, not strengthened**, and restate MF-15's
counterweight as a **strict loss on two axes**. (iv) Publish PHOTONICS' per-bin↔
bound reconciliation and MF-1's 3λ row. (v) Fix the six shipped-FALSE items
(§1(f) α–ζ) and the R18 gate-scope statements. (vi) Land the corrected headline
**verbatim in `NOTES.md § Phase 4 — Results`**, and delete the "R21: stated here"
self-certification. (vii) Update
`exp115-t28-fabrication-tolerance-bound-certified-resolution`'s required phrase
and add `LOGBOOK.md`, `PLAN.md`, `results.json` to its `required_sites`.
(viii) Replace `favoured` with a rejection-gated label, and add the single
boolean `machine_transfer_caveat = (m6_verdict != "TRANSFERS")` gating
`may_move_logbook_verdict` and the model comparison (QUANTUM D-Q4 / my RT-13, one
level up). (ix) Persist the bench-native anchors, the per-grid duration
decomposition, and `sensitivity_session1_across_reboot_DO_NOT_SCORE`.

**Why item 3 is Tier 1 and not a rider:** it is the only item that repairs a
**machine-enforced** caveat currently compelling a partly-false scope sentence
into every future citing document, and it is the vehicle that discharges the R20
firing. R25's own founding lesson is that a fix disclosed in prose and not given
its own numbered queue line is the fix that gets dropped. This is that line.

*Item 3 rides as a labelled rider with no falsifiable question of its own. If
Iteration 93 can carry only two items, item 3 is what drops — and it drops as a
numbered decline (R25), not silently.*

#### Tier 2 — cheap riders

**4. QUANTUM's T18 primary-source probe — STAGE A ONLY** (~10 min, zero FDTD):
fetch a primary source whose content is already known from the repo's own record
and confirm the returned text contains a figure the record already quotes. **A
probe that can only return "blocked" is not a probe.** Persist the raw result
either way, so T18's status becomes a **measured** fact rather than an inherited
one for the first time in 78 iterations. QUANTUM's new fact is correct: WebSearch
and WebFetch appear in the current session's tool roster, which is a change from
the state T18 records — **and a tool listed is not a tool heard from.**

**5. Persist EM's/THERMO's/QUANTUM's not-scored sensitivities** not already
covered by item 3(ix): QUANTUM's protocol-matched `G_E/f = 2.880173`,
`|T−1| = 0.2202`; EM's `U156/empty` cold-start substitution (+0.412%,
`k_B → 3.005696`, every verdict unchanged); PHOTONICS' F10 "no drift systematic
resolved at this precision."

**6. THERMO's cycle-scoped spend ledger** — a committed
`data/spend.json` accumulating `(session, calls, Sim.run seconds, elapsed)`
across invocations; `build_result_text()` states the cycle total and names every
session including abandoned ones; the budget gate seeds from it.

**7. A contention instrument that can produce the reading meaning "bad"** — the
positive control for §1(h): run a CPU-bound **Windows-side** process and confirm
the recorded number moves. If WSL2 `loadavg` cannot move (it should not), record
that as a measured fact and add a host-side sample, or state in the disclaimer
that the exclusive-use evidence is **VM-scoped and blind to the host**. Sample
`cpu MHz` per reading rather than once at idle — again with a positive control,
since WSL2 may report a static value, in which case the honest output is "not
measurable here," not a constant.

**8. Add a common-mode drift channel** the current design cannot see (EM §2.3):
the per-scene sub-timings already persisted give three replicate pairs per grid
at zero cost. Making that the null channel is the positive control `d_rep`
structurally cannot be.

#### Tier 3 — bigger builds

**9. [Iteration 94 Tier-1 candidate] EM's T1 passivity/causality ledger** — the
quantitative statement of what each of T1's four named escape routes *requires*,
in parameters: for σ(I), the required contrast as a ratio of two irradiances
(beam vs night-ambient at the same volume, both pinned by item 1), converted to
required `dσ/dI` and `I_th`, with the **sign check against passivity** (a passive
saturable medium *bleaches*; the phenomenon demands reverse-saturable absorption)
and a bound on the required `β` or `σ_ex/σ_gs`; then σ(x,t) with its switching
energy, angular selectivity as a reciprocity argument against the beam's own
divergence, and sub-threshold operation. Zero FDTD. **If the σ(I) sign-and-
magnitude argument closes, that is Checkpoint criterion 2 — the program's own
named honest alternative product, never once reached.** Gated on item 1 because
it literally needs VISION's pinned irradiances. **This is my recommendation for
Iteration 94's Tier-1 item 1.**

**10. Merged: VISION's G-variance decomposition + a third grid point +
a deliberate contention lever** (VISION Rank 1, PHOTONICS Rank 3, QUANTUM's
runner-up (a)). One design, because they are one experiment: `r = 78 / 117 / 156
/ 234` at fixed cpl=25 in one ABBA session separates absolute `N` from
`kappa_ratio` and makes `p = aN² + bN + c` exactly determined; a third runner's
six readings (~60 min at the measured rate) gives the first figure this program
has for how `G` varies **across** machines rather than **between** two; and one
deliberate concurrent-load reading converts session 1's accidental point into a
calibration of `dG/d(slowdown)` — the number M6's cross-machine reading most
needs. **Deliverable:** a persisted three-level variance decomposition
(within-session 1.46% · between-session 2.06–2.81% · between-machine 18.20%) and
a pre-registered test of whether **M5's ±15% CONFIRM band is wider than the
machine spread it must survive** — with the consequence that if it is, the band
must be re-derived from measured machine variance rather than from R28's founding
miss.

**11. MATERIALS' observer-return channel in ABSOLUTE units against the camera
floor** (`emit.observer_record`, stage 6) — two `Sim.run()` calls at the cheapest
geometry. The only way to learn whether "does not license varying the backing" is
a real fabrication constraint or a rounding artifact: the observer-facing face
carries **3.4×10⁻⁶** of total `σ_scat`, so a 5% relative movement there may sit
comfortably below any camera floor. **Gated on item 2** (the angle convention),
and pre-register the floor comparison and its units **before** the run (R9).

**12. EM's r=312 / cpl=25 / +168.75° leg** — now **unblocked**: the Iteration-92
queue sequenced it after a measured cross-grid factor, and `G` is measured.
Priced from bench-native rates for the first time in this program's history:
`1185.5 s` (r=156) + `3993.8 s` (r=234) = `5179.3 s`, inside
`COST_GATE_TOTAL_S = 10800` with the 1.10 margin. R31 and R33 satisfied by
construction rather than by correction.

**13. THERMO's r=234 within-reading ramp** (~6 min): permute scene order, five
back-to-back single-scene bursts, per-scene `cpu MHz` and `/proc/vmstat`
compaction counters under item 7's positive control. Binary and useful either
way, and it is **the only remaining plausible home for exp-114's disputed 4.467%
within-run level shift** now that warm-up amortization is refuted at 16.9×.

**14. MATERIALS' channel/resolution de-confound** — the per-bin channel at cpl=25
or the aggregate channels at cpl=20, one radius. **Must follow item 3**, so the
re-issued bound defines which figure the new resolution point must reproduce (the
**median**, not the tail max — running it first would very likely manufacture a
false resolution-instability finding, R15's own founding shape).

**15. QUANTUM's Stage B** (rigorous primary-source RSA/TPA/third-class
realizability check), gated on item 4 returning clear.

**16. QUANTUM's first bench-native σ(I) two-intensity run** — gated on items 9
and 15, and it **fires Checkpoint criterion 3** (engine physics beyond the
validated bench classes): it must be proposed as such, with a new trust-suite
stage carrying an absolute identity gate (`I → 0` reproduces the committed linear
article bit-exactly).

**17. `R2_SMOOTH_THRESHOLD = 0.90` re-derivation** — now in its **eighth**
consecutive cycle. Named so it is not silently dropped.

**18. The `box_dev` differential floor at r=234** — still the only radius with
**no** differential floor on file, and now load-bearing on the shipped bound.

#### Numbered declines (R25)

**D-1. The MP-5 thickness re-spec as a forward direction — DECLINED**, and
recorded so no future cycle re-proposes it. Verified from exp-061's own text:
MP-5 holds `τ_true` **fixed**, so thickening buys **zero** backing freedom
(`2·exp(−τ_true) = 5.1793×10⁻⁴` at 230× and 730× alike) while costing thermal
margin **3.79× → 1.35×** against NETD-lo and enlarging a silhouette that already
fails constraint 3 by construction. **Strictly worse on every axis.**

**D-2. Retiring `KAPPA_COST_EXPONENT = 3.2053` in favour of the bench's
2.9955 — DECLINED for the gate.** 3.2053 is the larger, conservative exponent;
adopting 2.9955 makes the gate anti-conservative on a contended machine, which is
R28's own founding failure mode running backwards. A gate-margin decision,
labelled as such, not a scientific one.

**D-3. Re-scoring M3 against a bench-native anchor as a SCORED verdict —
DECLINED.** R17 was satisfied at freeze; post-hoc estimator switching to move a
verdict is what Iteration 1 ruled out. It is disclosed forward as a NOT-scored
sensitivity (§3.1 item 8) and as the forward anchor rule (Tier-0 0.4).

**D-4. Folding session 1's sustained pair into `G_sustained` as a scored operand
— DECLINED.** Cross-session, and its `U234` is the reading immediately preceding
the host hang (+8.33%, the largest of the four): a ramp into a fault, not a clean
replicate. It enters as `..._DO_NOT_SCORE` only. Verified: admitting it changes
no verdict and flips no boolean either way.

**D-5. Scoring `sensitivity_v2_with_measured_G` — DECLINED again.** OV-1 stands
and is now **empirically** reinforced rather than merely prudential: M6 returned
AMBIGUOUS, so the machine-independence the construction presumes is measured and
unresolved.

**D-6. THERMO's discard-first-1000-steps protocol — remains DECLINED** (OV-3).
THERMO withdrew the request itself at Phase 5 after MF-7(a)'s measurement
returned a smaller and better-conditioned answer at zero extra cost.

**D-7. Promoting `σ_ext_cross` to a third energy-ledger channel — remains
DECLINED** (OV-4), refuted by EM's own A7 and accepted by EM at Phase 5.

**D-8. QUANTUM's `τ_true ∈ (6.6071, 8.2588)` concavity interval — remains
DECLINED** (OV-5), refuted numerically and accepted by QUANTUM at Phase 5.

**D-9. A sixteenth consecutive T28 instrument cycle as Iteration 93's falsifiable
heart — DECLINED.** Items 2 and 3 ride as labelled riders with no falsifiable
question of their own; item 1 is the cycle's heart. EM's own standard, ratified.

**D-10. QUANTUM's Stage B as a *scheduled* Iteration-93 item — DECLINED as
un-schedulable** before Stage A returns. Stage A is Tier-2 item 4; Stage B is
Tier-3 item 15, gated on it.

**D-11. EM's "zero-FDTD if exp-100's captures are committed" branch for item 1 —
DECLINED as unavailable.** Verified from primitives:
`experiments/100-.../` has **no** `artifacts/` directory. Iteration 93 budgets
real FDTD and projects it from a bench-native rate at the geometry actually run.

**D-12. Presenting PHOTONICS' DRAM-bandwidth mechanism, or THERMO's
contention-artifact conclusion, as evidence — DECLINED.** The mechanism ships
**NOT-SCORED** (post-hoc, one ratio, three unknowns and one equation — R5/R30);
the causal conclusion is refuted at the measured magnitude (§1(e)).

---

## 5.4 One thing I want on the record beyond the rules

This cycle built the best-instrumented wall-time measurement this program has
ever taken, and then wrote it up in a document that is false in six places.
Both halves are the finding. The machinery that produced the six defects is the
**correction machinery itself** — a single-source-of-truth disclaimer string, a
mandatory-fix docket, a reproduction gate — each of which was built to stop
exactly this class and each of which has now become the place the class lives.
`lab/ARTIFACTS.md`'s invariant has been quoted in this program's documents more
than any other sentence: *a silent gate and an absent gate produce identical
observations.* VISION found its **false-positive** twin this cycle — *a wrong
computation that agrees with the right one is indistinguishable from correctness
by verdict alone* — and I will add the one that follows from R20 firing inside
`DISCLAIMER_115`: **a single source of truth that is never independently
re-derived is a single source of un-audited truth.** Iteration 93's discharge
must re-derive that string's own arithmetic, not merely patch the six lines this
audit names.

---

*RED TEAM, Phase 5 final audit, exp-115, Panel Iteration 92. Worked alone: no
sub-agents, no delegation, no simulations, no git state changed. Every figure
above was recomputed this session in pure python against committed JSON and
committed source, or re-derived from primitives.*
