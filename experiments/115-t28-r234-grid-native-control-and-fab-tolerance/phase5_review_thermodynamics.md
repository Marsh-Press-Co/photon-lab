# Phase 5 review — THERMODYNAMICS

Fresh sub-agent, this seat only, Panel Iteration 92 (exp-115), Phase 5.
Read `PANEL.md` in full including the Iteration-92 Metrics scope
amendment (`PANEL.md:153–176`); `LOGBOOK.md`'s RULED OUT registry R1–R34
and the Iteration-92 record at the end of the file; this cycle's
`phase1_proposal.md`, my own `phase2_critique_thermodynamics.md`,
`phase2_redteam_audit.md` (§3 docket, MF-10, MF-15, OV-3), `NOTES.md`,
`run115.py`, `chunk_runner115.py`, `analyze115.py`, `results.json`,
`data/readings.json`,
`data/readings_session1_interrupted_20260905T2354Z.json`,
`data/cg_session1_interrupted.log`, `data/cg_session2.log`,
`data/trust_suite_bench_20260905T235042Z.txt`; `PLAN.md:1–80`;
`experiments/061-.../NOTES.md` (THERMO disposition table);
`lab/caveat_lint_config.json`. I have read **no** other seat's Phase-5
review. No git state changed; no simulations run; every figure below was
recomputed this session in pure python from committed JSON or committed
source, never copied from any document's prose (R4).

Caveat-registry phrases carried, since this document triggers two
registry entries: the bound is **certified at margin=32 only**;
**channel and resolution are fully confounded**; the **per-bin half of
any "better than 1.6×10⁻⁴" reading is withdrawn**; exp-061's THERMO
disposition margin is the corrected **1.35×–3.79×** range, never the
superseded figure; and `tau_shell`-family citations carry
exp-052's open question — **absorptivity, not thickness** — unchanged.

---

## 1. Verdict

**PARTIAL.**

**T1 escape route: N/A**, and I independently confirm it. A per-step
wall-clock rate, a grid size and a cost exponent cannot express σ(I),
σ(x,t), angular selectivity or sub-threshold operation; no
constraint-1/2/3/4 metric is computed anywhere in this cycle. The
Iteration-92 scope amendment (`PANEL.md:153–167`) is the correct home for
that fact and the cycle sits squarely inside it.

**What CONFIRMS, from this seat's charter:**

- **MF-10's energy-ledger / thermal-sidecar N/A sentence is present,
  correct, and asserted on both sides.** Its settling arithmetic
  reproduces (§2.1), it names T27 by name, and it closes exp-104's
  named, three-cycle-old "THERMODYNAMICS thermal-sidecar-N/A sentence"
  gap. This is the completeness item my seat asked for at Phase 2 §11,
  delivered verbatim.
- **MF-15's thermal counterweight is present and verified against its
  source** (§2.2), including the larger-black-silhouette /
  constraint-3-failure-mode sentence.
- **My own Phase-2 §10(i) instrument ask is discharged in full**: every
  reading now persists per-scene wall times, ISO-UTC start/end
  timestamps, epoch midpoints, a cumulative call count and `loadavg`
  before/after, plus a machine-state block. That is the first cycle in
  this program's history whose wall-time claims are re-derivable from
  its own committed data. I used it to do everything below.

**What makes it PARTIAL and not CONFIRM:**

- **My own pre-registered falsifiable expectation is REFUTED** (§2.3) —
  stated plainly because I put it on the record before the run.
- **Both pre-registered protocol models are refuted, and the warm-up
  model that my own Phase-2 §7 opened is refuted hardest** (§2.4). The
  cycle's own instrument measured the warm-up constant at **17×** below
  what my cloud-derived estimate implied, and with the opposite sign on
  the other grid.
- **M3's `G-DURATION-INVARIANT` verdict is an artifact of its cloud
  anchor, and the anchor choice is load-bearing on two downstream
  booleans** (§2.5). This is my Phase-2 §6 R17 objection, no longer
  abstract: it is now a demonstrated flip.
- **The largest single systematic in the cycle's data — a reproducible
  +5.6%/+6.0% within-reading ramp on the r=234 grid — is not looked at
  by any metric** (§2.6).
- **Three instrument-thermodynamics defects** (§3): the cycle's wall-time
  and call-count attribution is understated at cycle scope by 12 calls
  and 2218.5 s; the budget gate is per-invocation, not per-cycle; and the
  exclusive-use instrument is architecturally blind to the contention
  source most likely responsible for the difference between the two
  sessions.

---

## 2. Findings

### 2.1 MF-10 — the energy-ledger / thermal-sidecar N/A sentence: present, arithmetic verified, T27 named

`run115.py:976–984` carries the sentence inside `DISCLAIMER_115`, which
is asserted on the predictions side at `run115.py:1185` and on the result
side at `run115.py:1252`, both inside committed re-invocable call sites
(`--predictions-only`, `--selftest`, and `analyze115.py`). It appears
verbatim in `results.json` `predictions_text` **and** `result_text`.
R23 First Addendum: satisfied, and this is the first cycle in which it is
satisfied for *this* string.

Settling arithmetic, re-derived rather than restated. With
`COURANT_FRAC = 0.32` the wavefront speed is
`S = 0.32/√2 = 0.2262742` cells/step; at `n = 3334` steps the front has
travelled `754.35` cells from the source plane:

| grid | `SRC_X` | front at 3334 steps | `N` | fill |
|---|---|---|---|---|
| r=156 | 160 | 914.35 | 1400 | **65.31 %** |
| r=234 | 240 | 994.35 | 2100 | **47.35 %** |

The disclaimer's "~65 percent" and "~47 percent" are both correct to the
precision they claim. The sentence names **T27** explicitly
(`run115.py:981`) as the paid-for lesson that a truncated run is not a
small perturbation of a settled one, and it declares PANEL.md's
"Absorbed energy budget + predicted re-radiation" row N/A rather than
dropping it silently. **This is the correct disposition and I endorse it
without qualification** — a `σ_abs`/`σ_ext` ledger taken at 47 % domain
fill would be a wrong number, not a free byproduct.

One scope note, not a defect: the reason given is *sufficient* for this
cycle but is **not** a general N/A. It is a statement about 1000- and
3334-step control bursts, and it does not transfer to a cycle that runs
settled scenes. §4 item 1 turns that into an opportunity rather than a
standing exemption.

### 2.2 MF-15 — the MP-5 forward conditional: present, correct, verified against source

`results.json:758–775` (`sidecar_m9.e_tier.thermal_counterweight`)
carries both rows. I re-read
`experiments/061-absorptivity-mechanism-literature-check/NOTES.md:235–240`
and they match exactly: 230× → `l_geometric` 331.2 µm, `ΔT_ss`
5.277×10⁻³ K, margin **3.79×**; 730× → 1051.2 µm, 1.4774×10⁻² K, margin
**1.35×**; NETD-lo 0.020 K; classification UNDETECTABLE at both. The
corrected 1.35×–3.79× range is used, never the superseded figure — the
`exp061-thermo-length-scale-staleness` registry entry's own requirement.

The forward conditional's optical scaling is corrected per MF-1: the
`e_tier.forward_conditional` string states the bound scales as
`exp(−τ_true)`, explicitly "not `exp(−2 τ)`". That is right, and it is
right for my seat's reason as well as PHOTONICS': the measured observable
is a relative change in a cross-section, whose leading core-dependent
term is the coherent cross term, first order in the returned amplitude.

The `larger black silhouette = constraint-3 failure mode` statement is
present in `e_tier.thermal_counterweight.reading` and it says the thing
MF-15 asked for: *the same thickening that makes the article more
backing-independent shrinks the thermal margin from 3.79× to 1.35× and
makes the article a physically larger black silhouette — constraint 3's
own failure mode. The forward conditional is not free.* This is the
omission my Phase-2 §5 existed to prevent, closed.

MF-15's third clause — "if THERMO's §7 warm-up sensitivity is reported at
all, report it at `rel_dev` 0.1227 → 0.2977" — is discharged **vacuously**:
no warm-up sensitivity is persisted (`results.json` `sensitivities` holds
only the short-reading, v2-straddle and v2-with-measured-`G` entries).
That is defensible, because §2.4 shows the cycle replaced the estimate
with a measurement. But nobody says so; see §3 D6.

### 2.3 My own pre-run expectation is REFUTED — stated first, before anything I got right

`phase2_critique_thermodynamics.md:370–377` put this seat's falsifiable
expectation on the record: *"on a single-tenant box, with the contention
term removed, per-step rate should fall with reading duration, so the
bench's `d_dur` analogue should come out **negative**, plausibly of order
−4 % to −6 % … If the bench reproduces `R_DEG > 0`, that is genuine
evidence for a real thermal/turbo effect and this analysis is wrong."*

Measured, from `results.json:6–192` (per-reading `per_step_s`):

| session | grid | short | sustained | short→sustained |
|---|---|---|---|---|
| 2 (clean) | r=156 | 0.04858939 | 0.04970505 | **+2.296 %** |
| 2 (clean) | r=234 | 0.11239203 | 0.11082376 | **−1.395 %** |
| 1 (loaded) | r=156 | 0.05090948 | 0.05237354 | **+2.876 %** |
| 1 (loaded) | r=234 | 0.11712120 | 0.12005273 | **+2.503 %** |

Three of the four are **positive**. None reaches −4 %. My expectation is
refuted, and the honest reading is the one I named as the falsifier: a
real, small, positive duration effect exists on this bench. It is
**+2.30 %** at r=156 — the same axis on which the cloud measured
`R_DEG = +7.596 %`, so the bench is **3.31× steadier**, not
sign-inverted. My §6 sign argument correctly identified that `R_DEG`
conflates duration with elapsed position; it incorrectly predicted which
term would dominate once the contention field was removed.

### 2.4 Both pre-registered protocol models are refuted; the warm-up model is refuted at 17×

`results.json:439–441` pre-registered, before any bench reading, two
models on opposite sides of the CONFIRM ceiling. Against the measured
`G_sustained = 2.245940496842567` (`results.json:383`):

| model | prediction | measured/predicted − 1 |
|---|---|---|
| drift/degradation (QUANTUM B2) | 2.5402672 | **−11.59 %** |
| warm-up amortization, scene-matched (my §7 / RT-7) | 2.8681443 | **−21.69 %** |
| warm-up amortization, blend | 2.8801736 | **−22.02 %** |
| constant-`k` (`G_ref`, the model in force) | 2.4453405 | **−8.15 %** |
| exp-114's cloud `G_E` | 2.7455057 | **−18.20 %** |
| **pure `N²` cell-count scaling** | **2.2500000** | **−0.18 %** |

The bench's answer is `N²` to **0.18 %** — `k_B = 2.9955462`
(`results.json:454`), against the pre-R28 hardcoded exponent 3.0. Every
model that posited a protocol or superlinearity premium is wrong here;
the one that posits none is right to two decimal places.

The mechanism-level refutation is sharper than the ratio. MF-7(a)'s
two-point `p(n) = p_∞ + C_g/n` bound, which Red Team adopted **instead of**
my declined OV-3 discard-first-1000-steps protocol, measured the warm-up
constant directly. I re-derived both from the readings:

```
C_g = (p_S − p_U) / (1/1000 − 1/3334)
r=156:  p_S=0.04858939, p_U=0.04939745  ->  C_156 = −1.1543 s/scene
r=234:  p_S=0.11239203, p_U=0.11093872  ->  C_234 = +2.0760 s/scene
```

bit-matching `results.json:471,473`. My Phase-2 §7 estimated
`C_234 = 35.08 s/scene` from exp-114's cloud data. The bench measures
**2.076 s/scene — 16.9× smaller** — and the other grid's constant is
**negative**. A per-scene warm-up cost cannot be negative; a contention
term that decays over a session can look like one. So exp-114's 4.467 %
within-run level shift was **not** warm-up amortization, and the "third
correction axis" I opened at Phase 2 collapses from a CONFIRM→AMBIGUOUS
span to `interval_rel_width = 1.269 %` (`results.json:479`),
`m5_protocol_caveat = False`.

**Red Team's OV-3 decline was correct and I withdraw the request.**
MF-7(a) extracted the information from readings already scheduled, at
zero extra cost, and returned a *smaller* and better-conditioned answer
than my protocol would have while preserving matched-protocol
comparability with every prior R31 reading. On the record: I was wrong
about the magnitude and Red Team was right about the method.

**The consequence that matters beyond this cycle:** `KAPPA_COST_EXPONENT
= 3.2053` is, on the evidence now available, a **contention artifact of
the cloud sandbox, not a property of this FDTD implementation**. Both
working sets (≈112 MB at 1400², ≈251 MB at 2100², 7 float64 planes plus a
bool) exceed the W-2145's 11 MiB L3 (`results.json` `machine_state.lscpu`)
by 10× and 23×, so this is a DRAM-bandwidth-bound streaming stencil in
both cases and byte traffic scales as `N²`. That is exactly what a clean
machine reports. Under contention the larger footprint loses
proportionally more bandwidth, which inflates `G` — and M6's
`T = 0.8180` (`results.json:443`), `|T−1| = 0.1820`, AMBIGUOUS, is that
inflation measured. This is the mechanistic prediction I filed at
Phase 2 §11 ("no cache- or TLB-hierarchy mechanism would produce a
per-step superlinearity between these two sizes, so `G ≈ 2.25` is the
mechanistically expected outcome"), and it is the one thing this seat
predicted that the bench confirmed.

### 2.5 M3's `G-DURATION-INVARIANT` is an anchor artifact — and the anchor flips two downstream booleans

`run115.py:285–297` scores `d_dur = |G_sus − G_short|/G_short` against
bars `R_DEG/2 = 0.0379821` and `R_DEG = 0.0759642`, both derived from
exp-114's **cloud** figure. Measured `d_dur = 0.02903369`
(`results.json:405`) → `G-DURATION-INVARIANT`.

The per-grid decomposition, which the cycle now persists but never
computes, says something different. From §2.3: r=156 slows **+2.296 %**
from short to sustained while r=234 **speeds up 1.395 %**. Those are
**opposite signs**. A duration effect that were grid-independent would
cancel in `G` exactly and give `d_dur ≈ 0`; the non-zero `d_dur` exists
*because* the two grids respond to duration differently. So the label
"`G` is duration-invariant" is being returned on data whose own
decomposition says the duration response is grid-dependent. It passes
only because a cloud-sized bar is 3.3× wider than the effect the bench
actually has.

Re-scored against the bench's own comparable magnitude — its measured
r=156 short→sustained shift, `R_DEG_bench = 0.022961`, which is the exact
bench analogue of how `R_DEG` was defined:

| anchor | `M3_INVARIANT_BAR` | M3 | `m3_scored` | `m6_directional_only` |
|---|---|---|---|---|
| cloud `R_DEG` (as filed) | 0.037982 | G-DURATION-INVARIANT | **True** | **False** |
| bench `R_DEG_bench` | 0.011480 | G-NOT-DURATION-INVARIANT | **False** | **True** |

Both downstream booleans flip (`results.json:489,491`). Under a
bench-native anchor, `m3_scored = False` (because `d_rep = 0.0146329`
exceeds `R_DEG_bench/2 = 0.0114805`), M3 is UNINTERPRETABLE, and
`m6_directional_only = True` — so **M6's AMBIGUOUS would be directional
only rather than a scored verdict.** M6 AMBIGUOUS is the cycle's most
consequential reading (it says the cloud `G` does not transfer); the fact
that its *scored* status rests on a cloud constant is precisely the R17
circularity I named at Phase 2 §6 — "M3/M4's bands assume the answer to
the question M6 asks" — now realized, not predicted.

I am **not** asking for a retro-edit of a pre-registered band. R17 is
satisfied as written: `R_DEG` was the largest comparable magnitude on
file *before the run*, and no bench figure existed. The correct action is
forward: a bench-native `R_DEG_bench` now exists, it should be recorded
as this cycle's own deliverable, and the sensitivity above should be
persisted as a stated, NOT-scored re-anchoring so Iteration 93 inherits a
bench anchor instead of a cloud one.

### 2.6 The largest systematic in the dataset is a within-reading ramp on r=234, and nothing looks at it

Per-scene per-step rates, `results.json:12–22, 43–53, …` and the session-1
file's `:50–60, :112–122`, divided by that reading's `control_steps`:

| session | reading | empty | hollow | peccored | max/min − 1 |
|---|---|---|---|---|---|
| 2 | S156 | 0.048684 | 0.048431 | 0.048654 | +0.52 % |
| 2 | **S234** | 0.109785 | 0.111419 | **0.115971** | **+5.63 %** (monotone) |
| 2 | U156 | 0.050208 | 0.049413 | 0.049494 | +1.61 % |
| 2 | U234 | 0.110905 | 0.110481 | 0.111085 | +0.55 % |
| 2 | U234b | 0.111008 | 0.110838 | 0.111314 | +0.43 % |
| 2 | U156b | 0.048979 | 0.048963 | 0.049327 | +0.74 % |
| 1 | S156 | 0.050386 | 0.050912 | 0.051430 | +2.07 % (monotone) |
| 1 | **S234** | 0.114497 | 0.115475 | **0.121391** | **+6.02 %** (monotone) |

The r=234 **short** reading carries a monotone +5.6 %/+6.0 % ramp across
its three scenes, **reproduced in both independent sessions**, absent
from every sustained reading (≤0.55 % at r=234) and 3–12× larger than the
same-shape effect at r=156. It is larger than M3's entire
`NOT-INVARIANT` bar (3.80 %), **4.4×** the whole protocol-mismatch
interval (1.269 %), and it sits inside the reading that sets `G_short`
(M1) and the budget gate's second re-projection.

The two-point `C_g` model cannot represent it: `C_234 = 2.076 s/scene`
accounts for 1.85 % of the short reading's rate and 0.56 % of the
sustained one — about a third of the S→U difference — but a *per-scene
constant* is structurally incapable of expressing a *trend across
scenes*. So this is unmodelled structure, not a re-parameterization of
something already measured.

Two candidate mechanisms, and I decline to pick between them on this
data:

1. **Clock/thermal ramp.** S156 + S234 are the first ≈8 minutes of
   sustained AVX load after an idle start (`machine_state.loadavg`
   `[0.044, 0.104, 0.049]` at 04:39:24Z). A Xeon W-2145 falls from
   short-duration to all-core sustained turbo on roughly that timescale.
   *Against it:* U234, later and hotter, runs 4.4 % **faster** per step
   than S234's slowest scene — a settled clock should not recover.
2. **Allocator / THP transient on the 251 MB working set.** Three
   cold-built 251 MB scenes in 5.6 minutes; `transparent_hugepage` is
   `always [madvise] never`, so the r=234 scenes need ~126 huge pages
   each and later scenes face a more fragmented free list. *Against it:*
   no direct evidence; the r=156 scenes at 112 MB show a weaker version
   of the same shape.

Whichever it is, the program-level consequence is the same and it is my
seat's business: **every cost gate in this program projects a long run
from a short burst, and the short burst carries a reproducible,
grid-dependent +6 % transient that no instrument in the cycle records.**
That biases projections in the conservative direction here, but it is
also the only remaining plausible home for exp-114's disputed 4.467 %
within-run level shift now that warm-up amortization is refuted (§2.4).

Note the recording gap that makes this hard: `machine_state.cpuinfo_head`
captures `cpu MHz: 3696.000` **once**, at 04:39:24Z, with the machine
idle — the one field whose thermal behaviour is in question, sampled in
the one state it is guaranteed not to be in during the readings.

### 2.7 Session 1 vs session 2 as a loaded-vs-clean experiment

Session 1 (`data/readings_session1_interrupted_20260905T2354Z.json`,
23:54:14Z → 00:31:28Z, 4 readings, 12 calls) and session 2
(`data/readings.json` / `results.json`, 04:39:25Z → 05:41:04Z, 6 readings,
18 calls) are the same six-reading recipe on the same machine hours
apart, one of which ended in a host hang. That pairing is the most
informative dataset this cycle produced and **nothing in the cycle
analyses it.** I do so here.

**Per-step change, session 1 relative to session 2:**

| reading | s1/s2 − 1 | residual after removing the mean |
|---|---|---|
| S156 | **+4.775 %** | −0.90 pp |
| S234 | **+4.208 %** | −1.46 pp |
| U156 | **+5.369 %** | −0.30 pp |
| U234 | **+8.328 %** | **+2.66 pp** |

mean +5.670 %, stdev 1.83 pp, spread 4.12 pp.

**Answer to the assigned question: partly, and the part that fails is
diagnostic.** Three of the four readings sit within ±1.5 pp of a common
≈+4.8 % factor — that *is* a common-mode load signature, and it shows up
where a common mode must: in the ratio. `G_short` moved only **−0.541 %**
between sessions (2.300578 vs 2.313098), i.e. a common factor cancelled
out of `G` almost exactly, which is the cleanest evidence in this cycle
that `G` is robust to session-level load. But the sustained pair's
`G_pair1` moved **+2.808 %** (2.292240 vs 2.229628), five times as much,
and the entire excess is carried by session-1 `U234` at +2.66 pp above
the common mode.

**Timeline.** Session 1's `U234` ran 00:11:27Z → 00:31:28Z; the host
stopped answering SSH at ~00:53Z (`LOGBOOK.md` Iteration-92 Phase-4
entry, `PLAN.md:47–52`). The slowdown is **progressive and tail-weighted**
— 4.78 %, 4.21 %, 5.37 %, 8.33 % in execution order — i.e. the machine
was degrading into the fault while the readings were being taken. That is
a coherent physical picture and it is the correct disposition of session
1: not a clean replicate under a constant load, but a *ramp into a
failure*, whose last reading is contaminated most.

**Was the exclusive-use protocol honored and recorded?** Recorded:
**yes, and well** — `loadavg` before/after every reading in both sessions
(`results.json:25–34` etc.), plus start/end machine-state blocks
(`machine_state`, `machine_state_end`). Honored, on the evidence
available: **yes on the Linux side, unverifiable on the host side.**
Session 2 starts at `loadavg` `[0.044, 0.104, 0.049]` — genuinely idle —
and never exceeds `[1.237, 1.083, 0.761]`, exactly one runnable process
throughout. Session 1 starts at `[0.165, 0.321, 0.147]` and likewise
never exceeds ≈1.05. **Neither session shows a second Linux process, and
session 1 was nonetheless 4–8 % slower.** That is the defect in §3 D5,
and it is a class-rule member: the instrument returned the same reading
for the clean run and the contaminated one.

### 2.8 The drift block: the two grids drift in opposite directions

`results.json:386–402`, re-derived from reading midpoints:

| grid | lag | Δ per-step | relative rate |
|---|---|---|---|
| r=156 | 2718.82 s | −6.152×10⁻⁴ s | **−1.639 %/hour** (getting faster) |
| r=234 | 1111.74 s | +2.299×10⁻⁴ s | **+0.672 %/hour** (getting slower) |

MF-6(c)'s rate normalization is the right construction given ABBA's
unequal lags, and it is correctly implemented. The reading, which no
document states: **the differential is 2.31 pp/hour**, so `G` itself is
drifting at ≈2.3 %/hour on this bench. Over the 1.03-hour block that is
the whole of `d_rep`; over a three-hour production cycle it would exceed
M7's entire `N2_HOLDS` band (±5 %).

Two honest limits. First, `d_rep = 0.0146329` and the drift pair are
**one datum, not two**: `(1 + d_234)/(1 + d_156) − 1 = 0.01463`, i.e.
M4's statistic is the exact composition of the two same-grid drifts.
M4 REPEATABLE and the drift block are not independent evidence, and
nothing says so. Second, each grid's drift is a single difference of two
readings with no replicate; the r=234 delta (+0.207 %) is small enough
that only the r=156 one (−1.238 %) is comfortably above its own scene-level
scatter. Directional, `N = 1` per grid.

### 2.9 What the cycle actually established, in my seat's terms

The instrument, characterized on a clean single-tenant machine for the
first time: per-step cost scales as `N²` to 0.18 %; the duration response
is +2.30 % (r=156) / −1.40 % (r=234) between 1000 and 3334 steps/scene;
the per-scene warm-up constant is |C| ≤ 2.1 s/scene, one grid's negative;
session drift is ≈1–2 %/hour and **not common-mode across grids**; and
there is an unexplained, reproducible +6 % within-reading ramp confined to
the r=234 short reading. The cloud's `k = 3.2053` does not transfer
(M6 `|T−1| = 0.1820`). Those are real numbers about the machine this
program now runs on, and they are worth having.

---

## 3. Defects (R-numbers)

**D1 — R19 / R21: the cycle's own wall-time and call-count attribution is
false at the scope its words claim.** `results.json` `result_text` states
*"18 real FDTD calls (Sim.run), 3700.5s (61.68 min) total wall time **this
cycle**"* (built at `run115.py:1209–1212`). Re-derived from the two
committed reading files:

```
session 2  (results.json)                : 18 calls, 3690.3 s of Sim.run, 3700.5 s elapsed
session 1  (…_interrupted_20260905T2354Z): 12 calls, 2228.7 s of Sim.run, 2234.8 s elapsed
CYCLE TOTAL                              : 30 calls, 5919.0 s
```

The prose understates the cycle by **12 `Sim.run()` calls and 2218.5 s
(37.5 %)**. Session 1 is committed data (`5bb62cc`) and its existence is
in the commit subject of `ffa81c5`, but it appears **nowhere** in
`results.json`, nowhere in `result_text`, and `NOTES.md`'s Phase 4 and
Phase 5 sections are still `(pending)` (`NOTES.md:619–625`) — so the
only prose a future citation reads is the one that is wrong. R21's own
standard is that a finding must be "stated in the prose a future citation
will actually read."

The R19 assert is *satisfied* (`chunk_runner115.py:565`, 18 == 18) and is
structurally incapable of catching this: `_SIM_RUN_CALLS`
(`chunk_runner115.py:108`) is a module global reset at every process
start, so the invariant is per-invocation by construction while the
sentence it certifies says "this cycle." R19's own text demands "an
explicit, checkable, CODE-ENFORCED assert" — it has one, at the wrong
scope.

**This is the third recurrence of the same defect on my seat's docket**
(exp-109 Phase-5 §4 "no committed artifact"; exp-110 Phase-5 §2 Fix 6;
`phase2_critique_thermodynamics.md:491–509` here). The first two were
un-sourced figures. This one is the first where the number in frozen
prose is materially wrong.

**D2 — R27 / R28 / R31 family: the budget gate is per-invocation, not
per-cycle.** `results.json:203` `gates` shows three PROCEED projections,
all seeded from session 2's own elapsed clock; session 1's 2234.8 s is
invisible to every one of them. `COST_GATE_TOTAL_S = 10800` is applied as
a per-run bound while the queue, the proposal (§6) and the LOGBOOK all
discuss it as a per-cycle budget. The cycle's true spend is 5919.0 s =
**54.8 %** of the bound, so nothing breached — but a cycle interrupted
twice would spend up to 3× the bound with every gate reading PROCEED.
This is R28's own founding lesson (trace the gate from the
resource-consuming call site backward) one scope level up: the resource
is consumed by the *cycle*, the gate is armed by the *process*.

**D3 — R23 / R25: execution departed from a committed pre-registered
recipe, undisclosed in the cycle's documents.** `PLAN.md:64–70` (commit
`ec6274e`, 02:20Z) pre-registered exactly two resume paths: analyze with
`repeat_skipped=True` semantics, **or** "re-run ONLY the two repeats
(`U234b`, `U156b`) as a disclosed second session." Session 2 (04:39Z)
took a third: it re-ran all six readings from scratch. **I judge that the
better choice** — it preserves ABBA's first-order drift cancellation and
single-session comparability, which option (b) would have destroyed
across a reboot, and it is what produced the loaded-vs-clean pairing of
§2.7. But the deviation and its reason appear only in the commit subject
of `ffa81c5`; `results.json`, `NOTES.md`, `LOGBOOK.md` and `PLAN.md` all
still describe Phase 4 as INTERRUPTED at four readings.

**D4 — R17, realized: the M3 anchor is load-bearing and cloud-derived.**
§2.5. Not a violation as pre-registered — no bench figure existed at
Phase 3 — but `m3_scored` and `m6_directional_only` both flip under a
bench-native anchor that now exists, and M6's AMBIGUOUS would become
directional-only. Forward fix, not retro-edit: persist `R_DEG_bench =
0.022961` as this cycle's own deliverable plus the re-anchored
sensitivity, NOT scored, so Iteration 93 inherits a bench anchor.

**D5 — the class rule, on the exclusive-use instrument.** MF-6(e)'s
`loadavg` block is read inside WSL2
(`machine_state.platform = Linux-6.18.33.2-microsoft-standard-WSL2`), so
it samples the Linux VM's run queue. A Windows-side process on the same
physical machine contributes to DRAM bandwidth — the resource that *is*
this measurement, per my Phase-2 §11 memory analysis — without appearing
in that number at all. Session 1 ran 4.2–8.3 % slower than session 2 with
`loadavg` ≈ 1.0 in **both**. The instrument produced identical readings
for the clean run and the run that ended in a host hang: *a watcher that
can only say "quiet" is not evidence it can hear.* Two consequences:

- The Director's session context reportedly includes a Windows-side VC++
  runtime installation at ~00:03Z — which would overlap session 1's
  `U156` (00:02:42Z → 00:11:26Z) exactly, and precede the monotone
  4.78 → 8.33 % slowdown. **That fact appears nowhere in the repository**
  (`grep` over `experiments/115-*/`, `SESSION_LOG.md`, `PLAN.md`,
  `LOGBOOK.md` returns nothing). If it is known, it is load-bearing on
  MF-6(e) and belongs in NOTES.md Idealizations, which `PLAN.md:76–79`
  already instructs for the outage cause.
- `data/cg_session1_interrupted.log` contains **two lines** — the numpy
  `pyyaml` warning and nothing else. Session 1's per-reading ticker
  output did not survive, so the only session-1 artifact is the readings
  JSON. Same shape as exp-114's lost scratch wall-time log, one cycle
  later.

**D6 — minor, R21-adjacent: two findings sit in `results.json` with no
prose that states them.** (a) MF-15's warm-up-sensitivity clause is
discharged vacuously (§2.2) because MF-7(a)'s measurement superseded the
estimate — a genuinely good outcome that nothing records; the connection
between `interval_rel_width = 1.269 %` and the CONFIRM→AMBIGUOUS span it
replaces is drawn in no document. (b) `d_rep` and the drift block are one
datum, not two (§2.8), and both are quoted in `result_text` as if
independent.

**Not defects, recorded so they are not mistaken for defects:** MF-10 and
MF-15 are discharged correctly (§2.1, §2.2); `python lab/caveat_lint.py`
reports **16 caveats checked, 0 required-site failures** with the cycle in
the tree; the MF-12 identity gate is 10/10 with `build_sim` byte-identical
to `chunk_runner114`; the bench trust-suite record is committed with its
platform, numpy/ceviche/fdtd versions named (docket-14 satisfied); and
the per-reading persistence delivered exactly what my Phase-2 §10(i)
asked for.

---

## 4. Ranked top-3 candidate directions

Item 1 of Iteration 93 is fixed by D2 (VISION's constraint-3 re-score).
These are ranked for Iteration 93 items 2–3 and Iteration 94 item 1.

### #1 — Fill PANEL.md's ledger row on the D2 constraint-3 re-score. **Yes: a thermal-sidecar row can be filled, and this is the first cycle in fifteen where it can.** (Iteration 93, item 2)

Directly answering the Director's question. The reason exp-115 declared
the row N/A is *specific and does not transfer*: at 1000/3334 steps the
domain is 65 %/47 % filled, so no settled ledger exists (§2.1). VISION's
ambient re-score runs `lab/ambient.py` at photopic **and** scotopic, and a
Weber contrast is meaningless unless those runs are settled — so the very
condition that blocks the ledger here is *guaranteed satisfied* there.
The row becomes computable at **zero marginal FDTD cost**, from runs the
cycle is already paying for.

Two halves, both cheap:

- **Joule accounting (FDTD byproduct).** `σ_abs`/`σ_ext` and the absorbed
  fraction from the settled ambient scenes — the same `lab/sections.py`
  machinery exp-114 used, applied to fields that have actually settled.
- **The analytic sidecar (desk, post-run, labelled as such per my
  charter's expressibility contract).** Absorbed ambient power → `ΔT_ss`
  through exp-061's committed chain
  `ΔT_ss = I·ratio_abs_ext/(4εσT³ + h_eff)`, `h_eff = k_air/L` → Wien
  band (≈9.9 µm at every scale exp-061 tested) → NETD margin →
  detectability classification. Every input is already committed: the
  measured `ratio_abs_ext` family (0.51–0.61, worst case 1.0), the
  silicon thermal identity with its `ASSUMED — provenance terminates
  unsourced (T18)` label carried, and `L` from the scored geometry. The
  only new input is the ambient irradiance in each regime, which VISION
  must pin anyway to score constraint 3.

**Why it belongs to this seat and to constraint 3, not just to
bookkeeping.** Constraint 3 asks for an object that is not a black
silhouette at rest under ambient light. Every mechanism that terminates
the beam does so by absorbing, and absorbed ambient power has to leave.
Producing a **photopic `ΔT_ss` and a scotopic `ΔT_ss`, each with a
detectability verdict against NETD, for both Tier W and Tier A**, puts
the first number on the question my seat exists to ask about the
program's central constraint — and it does so in the one cycle in fifteen
that re-engages the phenomenon. Deliverable: one table, ~150 words of
prose, zero extra `Sim.run()` calls.

### #2 — Close the three instrument-thermodynamics gaps this cycle's own data opened (Iteration 93, item 3; ~zero FDTD)

A bundle, because the three are one failure: the cycle measures wall time
better than any predecessor and still cannot state its own spend, its own
budget, or its own contention.

- **(a) Cycle-scoped spend ledger (D1, D2).** A committed
  `data/spend.json` accumulating `(session, calls, Sim.run seconds,
  elapsed)` across invocations; `build_result_text()` states the cycle
  total and names every session including abandoned ones; the budget gate
  seeds from it so `COST_GATE_TOTAL_S` bounds the cycle, not the process.
  Fixes a false sentence in frozen prose and closes a hole through which
  an interrupted cycle can spend 2–3× its bound with every gate green.
- **(b) A contention instrument that can produce the reading that means
  "bad" (D5).** Before trusting it: a **positive control** — run a
  CPU-bound Windows-side process and confirm the recorded number moves.
  If WSL2 `loadavg` cannot move (it should not), record that fact
  explicitly and add a host-side sample, or state in the disclaimer that
  the exclusive-use evidence is VM-scoped and blind to the host. Also
  sample `cpu MHz` per reading rather than once at idle (§2.6) — again
  with a positive control, since WSL2 may report a static value, in which
  case the honest output is "not measurable here," not a constant.
- **(c) Re-anchor on the bench (D4).** Persist `R_DEG_bench = 0.022961`
  and the re-anchored M3/M6 sensitivity, NOT scored, so Iteration 93's
  bands are drawn from the machine they will run on.

### #3 — Characterize the r=234 within-reading ramp (Iteration 94, item 1; ~6 minutes of bench time)

§2.6: +5.63 % and +6.02 % in two independent sessions, r=234 only, absent
from every sustained reading, 4.4× the whole protocol-mismatch interval,
and unmodelled by anything in this cycle. It is also the only remaining
plausible home for exp-114's disputed 4.467 % within-run level shift now
that warm-up amortization is refuted at 17× (§2.4) — so it is not
housekeeping, it is the last open account on the T28 cost thread.

Protocol, all short-burst, single grid, ≈6 minutes: (i) **permute scene
order** (`peccored, hollow, empty`) — if the ramp follows the clock it
stays, if it follows the scene it moves; (ii) five back-to-back
single-scene bursts to see whether the ramp is per-reading or
per-session; (iii) sample `cpu MHz` and `/proc/vmstat` compaction
counters per scene, under the (b) positive control above. Outcome is
binary and useful either way: a clock ramp means every cost gate in this
program projects from a systematically biased sample and the bias is
bounded here for the first time; an allocator/THP transient means the
same, with a different and cheaper fix (pre-touch the arrays).

**Ranked below the cut, named so they are not silently dropped:** the
`box_dev` differential floor at r=234 (still the only radius with **no**
differential floor on file, `results.json` `b_floor.differential_floor.r234`,
my Phase-2 §3 gap, now load-bearing on the shipped bound); the third P5
thermal-margin point, still gated on the `CPL_RATIO` commensurability gap;
and the r≈624 fourth cost point, which my exp-114 Phase-5 `r^-1.16`
projection request still wants and which is now cheaper to justify because
`N²` holds at 1.5.

---

## 5. Summary (≤150 words)

**PARTIAL; T1 route N/A, confirmed.** MF-10's energy-ledger/thermal-sidecar
N/A sentence is present, asserted both sides, names T27, and its 65 %/47 %
settling arithmetic reproduces — closing exp-104's three-cycle gap. MF-15's
counterweight matches exp-061 exactly (1.35×–3.79×), silhouette clause
included. Bench thermodynamics: short→sustained is +2.30 % (r=156) and
−1.40 % (r=234) versus the cloud's +7.60 % — 3.3× steadier, opposite signs
across grids; drift −1.64 %/h and +0.67 %/h. Both pre-registered protocol
models are refuted; the warm-up constant is 17× below my own cloud-derived
estimate, so `k = 3.2053` reads as cloud contention and the bench gives
`N²` to 0.18 %. My pre-run expectation was wrong and Red Team's OV-3
decline was right. Defects: cycle spend understated by 12 calls / 2218.5 s
in frozen prose (R19/R21); per-invocation budget gate; undisclosed
deviation from the committed resume recipe; M3's anchor flips two booleans;
WSL2 `loadavg` is blind to host contention.

---

*THERMODYNAMICS, Phase 5, exp-115. Worked alone: no sub-agents, no
delegation, no simulations, no git state changed. I read no other seat's
Phase-5 review. Every figure above was recomputed this session in pure
python against committed JSON and committed source.*
