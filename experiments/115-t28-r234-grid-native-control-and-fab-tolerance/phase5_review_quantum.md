# exp-115 — Phase 5 review — QUANTUM OPTICS

*Panel Iteration 92, exp-115, Phase 5 (REVIEW). Fresh context. Written
without reading any other seat's `phase5_review_*.md`. Charter (PANEL.md
lines 78–81, verbatim): "QUANTUM OPTICS — non-classical absorption,
state-dependent or coherent interactions. Expressibility contract:
mechanisms enter the bench only as effective classical parameters —
σ(I), σ(x,t), dispersive ε(ω), gain — or Red Team strikes them."*

*Method: no sub-agents, no delegation, no simulations, no git state
changed. Every number below was recomputed this session in pure python
against committed JSON and committed source, or re-derived from
primitives. Where I report a figure that refutes my own Phase-2 critique
I show the recomputation that kills it.*

---

## 1. Verdict

# PARTIAL

**T1 escape route: N/A** — correctly declared. This is an
instrument-fidelity/governance cycle on the T28 sub-thread; it records
none of PANEL.md's seven metric rows, under the Iteration-92 scope
amendment (PANEL.md:153–167) that Red Team's own §4.2 D1 required. I
confirm no σ(I)/σ(x,t)/angular/sub-threshold content is expressible in,
or claimed from, a per-step wall-clock rate. Nothing in this cycle is
constraint-3 progress and the shipped `DISCLAIMER_115` says so in both
`predictions_text` and `result_text`.

**What earns the "partial" — the measurement half is CONFIRM-grade.**
Every scored statistic in `results.json` reproduces bit-exactly from
`readings_summary` (§2.1). The six readings ran in the mandated ABBA
order under a genuinely idle machine (`machine_state.loadavg` =
`[0.0444, 0.1035, 0.0493]` at `2026-09-06T04:39:24Z` on a real Xeon
W-2145 / WSL2 / 98 GB box), 18/18 `Sim.run()` calls, identity gate 10/10,
zero `lab/` diff. MF-5's invocation fix is live and correct. MF-7(b)'s
promised caveat is carried into `result_text` — twice. R33 addendum (a),
my own, is honored. This is the cleanest wall-time measurement this
sub-thread has taken.

**What blocks a CONFIRM — the inference half over-reaches its own data
in three places, each of which I can price:**

1. **M5's CONFIRM and M6's AMBIGUOUS are scored on the same pair of
   numbers and disagree** (§2.2). The two measurements M5 claims to
   reconcile differ by **22.24%** in ratio space — wider than M5's own
   CONFIRM half-width of 15%. Each replicate places the *other* in
   AMBIGUOUS. A band that admits two mutually-inconsistent replicates is
   a containment test, not a replication test, and `m5["may_move_
   logbook_verdict"] = true` is asserted while `m6["verdict"] =
   "AMBIGUOUS"` says the transfer that would license it is unresolved.
2. **`m7["model_comparison"]["favoured"] = "constant-k"` is an over-read**
   (§2.3). Both nominated models are refuted by the datum (8.15% and
   13.42%); the un-nominated third model — pure `N²`, `k = 3.0` — fits to
   **0.18%**, 45× better than the "winner". The `favoured` string is a
   bare nearest-neighbour with no goodness-of-fit gate
   (`run115.py:435–436`), and its power certificate uses the smallest of
   four available uncertainty channels (§2.4).
3. **Two zero-cost disclosures are outstanding at the freeze line**
   (§2.6, §2.7): M8's own headline is persisted but not narrated
   (R21's *third* instance, which auto-fires Checkpoint 4 if it reaches
   LOGBOOK unnarrated), and the cycle's own first, interrupted session —
   four completed readings, an independent same-machine across-reboot
   replicate — is committed to `data/` but appears nowhere in `NOTES.md`,
   `results.json`, `run115.py`, or `analyze115.py`.

None of the three is a physics error and none touches `lab/`. All three
are correctable this shift, before the Result section is written
(`NOTES.md:619–625` are still `(pending)`), which is exactly what a
Phase-5 review is for. Corrected, this cycle is a CONFIRM.

---

## 2. Findings

### 2.1 Every scored statistic reproduces bit-exactly from primitives. CONFIRMED.

Recomputed from `results.json.readings_summary` per-step rates alone, with
no intermediate field trusted:

| quantity | recomputed | filed | file |
|---|---|---|---|
| `G_pair1 = p(U234)/p(U156)` | `2.2296275647790664` | `2.2296275647790664` | `results.json:G_pair1` |
| `G_pair2 = p(U234b)/p(U156b)` | `2.2622534289060674` | `2.2622534289060674` | `results.json:G_pair2` |
| `G_sustained` (mean of pairs) | `2.245940496842567` | `2.245940496842567` | `results.json:G_sustained` |
| `G_short` | `2.3130982736423493` | `2.3130982736423493` | `results.json:G_short` |
| `d_dur` | `0.02903368938753793` | `0.02903368938753793` | `results.json:m3.d_dur` |
| `d_rep` | `0.01463287619976741` | `0.01463287619976741` | `results.json:m4.d_rep` |
| `measured_ratio = 1.5·G` | `3.3689107452638507` | `3.3689107452638507` | `results.json:m5.measured_ratio` |
| `exponent_B = 1+ln G/ln 1.5` | `2.995546218006855` | `2.995546218006855` | `results.json:m5.exponent_B` |
| `excess = G/2.25−1` | `−0.0018042236255256805` | `−0.0018042236255256805` | `results.json:m7.excess` |
| `reference_ratio = 1.5**k` | `3.6680107109370383` | `3.6680107109370383` | `results.json:m5.reference_ratio` |

The MF-5 invocation fix is real and load-bearing: `exponent_B` is fed to
`R114.classify_kappa_exponent_check()`, and `measured_ratio` comes back
equal to `1.5·G` to `<1e-12`, as the Phase-3 assert requires. My own
Phase-2 A2 flagged the unstated conversion; it is now stated and coded.

### 2.2 The v2 straddle: the sign is correct, the persisted value is correct, and the "closure" the framing invites is NOT available. This is my seat's primary question and the answer is negative.

**The sign and the value, re-derived.** With
`f ≡ p234_prod/p234_burst = 0.9532431491914767`:

```
v2'  = 1.5 × G_sustained × f = 1.5 × 2.245940496842567 × 0.9532431491914767
     = 3.2113910881603176            (filed: 3.2113910881603176)     ✔ bit-exact
signed_dev(v2') = (3.2113910881603176 − 3.6680107109370383)/3.6680107109370383
     = −0.12448699274928553          (filed: −0.12448699274928553)   ✔ bit-exact
boundary = 3.6680107109370383/(1.5 × 0.9532431491914767)
     = 2.5652851279677367            (filed: same, all 17 digits)    ✔ bit-exact
G_sustained = 2.2459405 < 2.5652851  ⇒  signed_dev(v2') < 0
```

`results.json.sensitivities.sensitivity_v2_with_measured_G_DO_NOT_SCORE.
straddle_still_open = true` is therefore **correct against its own
pre-registered definition**, which is agreement in sign with exp-114's
*filed* `+0.12274985147707763`. It does not agree; it is negative.

**Where the "closure" reading comes from, and why it is not a closure.**
Four signed deviations are now on the table, and their pattern is the
finding:

| estimate | machine | signed dev from `reference_ratio` |
|---|---|---|
| exp-114 filed (method 1) | cloud | **+0.12274985** |
| exp-114 v2 normalization | cloud | **−0.12290452** |
| exp-115 M5 (bench, method 1) | bench | **−0.08154283** |
| exp-115 v2-with-measured-`G` | bench | **−0.12448699** |

Within the bench session the two normalizations agree in **sign** (both
negative), so exp-114's straddle *does not reproduce as a straddle on
the bench*. That is the only sense in which anything closed, and it is
**not** a resolution of exp-114's straddle. Two reasons, the second of
which is new evidence produced by this very cycle:

- v2' is a **hybrid**: it multiplies a bench-measured `G` by exp-114's
  *own session's* `p_prod/p_burst`. It contains one bench operand and one
  cloud operand. Its sign is therefore a statement about neither session
  cleanly.
- **OV-1's stated reason is now empirically reinforced, not merely
  prudential.** OV-1 declined the scored half on the ground that scoring
  it "would presume exactly the machine-independence M6 exists to test"
  (`NOTES.md` Phase-3 override 1). M6 has now run and returned
  `AMBIGUOUS` — `T = 0.8180425684476521`, `|T−1| = 0.1819574315523479`,
  **above** the `TRANSFERS` bar `0.152950039837078`. Machine-independence
  is not merely untested; it is measured and **unresolved**. The
  presumption OV-1 refused to make is exactly the presumption the data
  now refuses to grant.

**What may be concluded:** the bench's own grid-native `G` is
`2.2459405`; on the bench, the burst-vs-production normalization moves
the estimate from `−0.0815` to `−0.1245`, i.e. by 4.3 points in the same
direction, not across the reference. **What may not be concluded:** that
exp-114's straddle is resolved, that either exp-114 method is now
preferred, or that `v2'`'s sign carries evidential weight. The persisted
`NOT_SCORED` flag is the correct disposition and must stay.

**Protocol-matched, the transfer looks worse, not better.** Correcting
`G_E` for the one protocol factor exp-114 itself measured gives a
burst/burst cloud value `G_E/f = 2.880173496422133`, hence
`T = 0.7797934741197239`, `|T−1| = 0.2202` — further from transfer than
the filed `0.1820`, still short of the `0.3059` `DOES-NOT-TRANSFER` bar.
So the known protocol correction moves M6 **toward** non-transfer. Worth
persisting; it is three multiplications.

### 2.3 M5's CONFIRM and M6's AMBIGUOUS are scored on the same pair and contradict each other. The band admits two replicates that mutually refute.

`G_E = 2.74550565394726` and `G_bench = 2.245940496842567` are two
measurements of the same quantity. Their mutual relative deviation, in
the same ratio space M5's bands live in:

```
G_E/G_bench − 1 = +0.22243027266617332
G_bench/G_E − 1 = −0.18195743155234790
```

Both magnitudes exceed M5's CONFIRM half-width (`0.15`) and fall inside
its AMBIGUOUS window (`0.15 – 0.30`). **If either measurement were used
as the reference for the other, the other would score AMBIGUOUS.** Yet
each scores CONFIRM against `reference_ratio`, because `reference_ratio`
happens to sit between them (`+0.12275` and `−0.08154`).

Three consequences, stated precisely:

1. M5 is a **containment** test, not a replication test. It answers "is
   this datum within 15% of `k = 3.2053`?" It does not answer "does
   exp-114 replicate?", which is the question `phase1_proposal.md` §5-M5
   advertised ("exp-114's CONFIRM replicates independently, on a second
   machine"). RT-7 (`phase2_redteam_audit.md:280–311`) priced this in
   advance for the `k = 3.0` case; the replicate-vs-replicate case is
   sharper and is not stated anywhere in the frozen record.
2. `m5["may_move_logbook_verdict"] = true` is asserted while
   `m6["verdict"] = "AMBIGUOUS"` and `m6["m6_directional_only"] = false`.
   MF-9 wired the composition **one way only** — M3 gates M6
   (`run115.py:405`, `m6_directional_only = (m3_verdict !=
   M3_LABEL_INVARIANT)`) — and nothing gates M5 or M7 on M6. That is
   verbatim the asymmetry RT-13 (`phase2_redteam_audit.md:400–418`) named
   one level earlier, closed for M3→M6 and left open for M6→M5/M7.
3. The honest composite statement the record should carry: **the two
   measurements of `G` in existence are mutually AMBIGUOUS, and both are
   CONFIRM against a reference that lies between them.** A CONFIRM on
   this design is compatible with `k` not being a portable constant at
   all.

### 2.4 M7's "favoured" is an over-read on four independent grounds, and the record should say `NO MODEL FAVOURED`.

Filed: `excess = −0.0018042236255256805` → `N2_HOLDS`;
`rel_to_const_k = 0.0815428277734715`, `rel_to_const_eps =
0.13422460480982495`, `separation = 0.060849242573798784`,
`underpowered = false`, `favoured = "constant-k"`.

**(a) Both nominated models are refuted; the un-nominated one fits.**
`|excess| = 0.0018` means pure `N²` — algebraically identical to
`k = 3.0` exactly — fits to **0.18%**. The "favoured" model misses by
**8.15%**, i.e. **45×** worse. `results.json` states this itself, in the
field adjacent to `favoured`: `m7["note"]` reads "N2_HOLDS requires BOTH
candidate cost models to be wrong." A results file that reports "both
candidate models are wrong" and "favoured: constant-k" in neighbouring
keys is internally incoherent, and the Result prose propagates the second
("N2_HOLDS (model comparison: constant-k)") without the first.

**(b) The selection rule has no goodness-of-fit gate.**
`run115.py:435–436` is a bare nearest-neighbour:
`"constant-k" if d_k < d_eps else "constant-eps"`. It cannot return "no
model fits", so it is structurally incapable of producing the reading
that is true here. This is `lab/ARTIFACTS.md`'s own invariant applied to
a model-selection string.

**(c) The power certificate uses the smallest of four uncertainty
channels.** `analyze115.py:146` sets `m7_underpowered` from `d_rep` alone
against `M7_POWER_BAR = 0.03` (`run115.py:214`). Four channels are
measurable in this cycle's own committed data:

| channel | magnitude | in the gate? |
|---|---|---|
| immediate within-session repeat (`d_rep`) | **1.46%** | yes — and only this |
| across-reboot, same machine (session 1 vs session 2, §2.7) | **2.06%** | no — not computed |
| burst-vs-production protocol, exp-114's own r=234 measurement | **4.90%** | no (the cycle's own two-point interval, 1.27%, is 3.9× narrower) |
| machine-to-machine (M6 `\|T−1\|`, AMBIGUOUS) | **18.20%** | no |

Against a 6.08% model separation, the largest channel is **3.0×** the
separation and the cycle's own metric already reports it as unresolved.
Gating a machine-property model comparison on the one channel that
excludes machine variation is the class rule in miniature.

**(d) Neither model is well-specified for these grids.** My Phase-2 A4,
confirmed by Red Team (`phase2_redteam_audit.md:604–612`): both models are
parameterized on `kappa_ratio`, while cache/bandwidth superlinearity is a
function of **absolute `N`**. R28's founding measurement spans
`N = 1120→2240` at `cpl=20`; this cycle spans `N = 1400→2100` at
`cpl=25`. The models are not being tested on the axis they are defined
on. `predictions_text` already concedes "M7 is descriptive" — a
descriptive metric should not emit a model-selection verdict.

**Recommendation (zero cost, pre-freeze):** replace `favoured` with
`"NO MODEL FAVOURED — both nominated models are refuted by this datum
(8.15% / 13.42%); the un-nominated pure-N² model fits at 0.18%"`, and
gate it on M6 as well as `d_rep`.

### 2.5 `KAPPA_COST_EXPONENT = 3.2053` is not a contention artifact and not a constant. Five measurements now exist and they span 0.61 in exponent, with four confounds moving together. The honest statement is a table, not a number.

The Director asked whether R28's founding exponent is a contention
artifact given `k_B = 2.9955` on a clean machine. Re-derived from
primitives, every implied exponent on file:

| source | machine | `kappa_ratio` | grids (`N`) | `cpl` | protocol | implied `k` |
|---|---|---|---|---|---|---|
| R28 founding (exp-110) | cloud | 2.0 | 1120→2240 | 20 | prod/prod | **3.2053300** |
| exp-114 filed (`G_E`) | cloud | 1.5 | 1400→2100 | 25 | prod/burst | **3.4908808** |
| exp-114, protocol-matched (`G_E/f`) | cloud | 1.5 | 1400→2100 | 25 | burst/burst | **3.6089804** |
| exp-115 session 1 (interrupted, unused) | bench | 1.5 | 1400→2100 | 25 | burst/burst | **3.0458707** |
| exp-115 session 2 (filed) | bench | 1.5 | 1400→2100 | 25 | burst/burst | **2.9955462** |

(`k = 1 + ln G/ln kappa_ratio`; R28's own value re-derived independently
in my Phase-2 A4 from exp-110's raw per-scene wall times,
`ln(9.223600318696624)/ln 2 = 3.2053299988171697`, matching
`experiments/110-.../run.py:377`.)

**Answers, in order:**

1. **Is 3.2053 a contention artifact? Not determinable, and the sign
   argument is a hypothesis, not a finding.** The cloud and bench figures
   differ in machine, contention, `cpl`, absolute-`N` range, protocol and
   `kappa_ratio` **simultaneously**. Memory-bandwidth contention on a
   shared host should hurt the larger working set more and therefore bias
   `k` **up**, which is sign-consistent with cloud > bench — but R5's
   look-elsewhere discipline says one datum in a four-way-confounded
   space does not identify a cause, and the two cloud values at the *same*
   `kappa_ratio` (3.4909 / 3.6090) are **higher** than the cloud value at
   `kappa_ratio = 2.0` (3.2053), which a pure contention story does not
   explain.
2. **What IS established: `k` is not a machine-independent constant.**
   The spread `2.9955 → 3.6090` is 0.61 in exponent, 22% in `G`. The
   cycle's own M6 reads `AMBIGUOUS` on exactly this question. So the
   in-force constant, cited as `KAPPA_COST_EXPONENT` by every cost gate
   since R28, has never been shown portable across machines and is now
   measured to differ by 6.5% in exponent on the only second machine ever
   tried.
3. **The honest statistical statement, verbatim for the record:**
   *"`KAPPA_COST_EXPONENT` rests on N = 1 cloud session at one
   `kappa_ratio` and N = 1 bench session at a different `kappa_ratio`,
   with machine, contention, `cpl`, absolute `N` and protocol confounded
   across the two. The two disagree by 6.5% in exponent (22% in the
   cost ratio `G`). Neither refutes the other at the CONFIRM standard,
   and neither establishes portability. `k` is a per-machine,
   per-configuration fitted parameter with one measurement per
   configuration."*
4. **For the safety gate specifically: keep 3.2053.** It is the larger
   exponent and therefore the conservative one; adopting the bench's
   2.9955 would make the gate anti-conservative on a contended machine,
   which is R28's own founding failure mode running backwards. This is a
   gate-margin decision, not a scientific one, and should be labelled
   as such — the distinction R33's founding record already draws.

**Internal contradiction worth naming:** M7 declares constant-`k`
"favoured" in the same `results.json` in which the measured exponent
differs from the in-force `k` by **6.5%**. The datum that "favours" the
constant-exponent model is the same datum that refutes the constant's
value.

### 2.6 R33 addendum (a) — my own — IS honored. Credit. But the empirical warrant it cites has shrunk 4.6× and reversed sign on the other grid.

R33(a) (`LOGBOOK.md:1445`ff) requires, when a control-selection rule
justified for one purpose is reused for another: (i) independent
justification for the new purpose, stated in the record, and (ii) any
alternative reading disclosed as a stated, not-scored sensitivity.

**Both discharged.** `results.json.sensitivities.sustained_choice_
justification` states the protocol-commensurability argument (3334
steps/scene is the closer duration match to a 12000-steps/scene
production numerator than 1000 is), explicitly distinguishes it from the
Iteration-90 cost-gate conservatism argument it replaces, and — better
than I asked for — discloses the residual conflict that
`R113.combine_control_readings()` selects the *lower* `speed_ratio`,
which is a different rule that merely happened to coincide.
`sensitivity_short_reading_DO_NOT_SCORE` persists the alternative
(`measured_ratio = 4.431098887676021`, `rel_dev = 0.20803869914110543`,
AMBIGUOUS). Requirement met.

**The one thing Phase 5 adds.** The justification's cited warrant is
"`R_DEG = 0.075964` shows duration measurably matters on this axis."
That warrant is now measured on the bench, per grid, and it does not
hold as stated:

```
r=156:  p(S156)=0.04858939 → mean p(U156,U156b)=0.04939745   :  +1.663%
r=234:  p(S234)=0.11239203 → mean p(U234,U234b)=0.11093872   :  −1.293%
cloud R_DEG (exp-114, r=156, 1000→3334)                      :  +7.596%
```

The duration effect is **4.6× smaller on the bench than on the cloud**
and **opposite in sign on the r=234 grid**. The selection rule survives
on commensurability grounds alone — a closer duration match is still a
closer duration match — but the magnitude argument bolted onto it is
now refuted by the cycle's own readings and should be restated rather
than carried forward. This is exactly the sign conflict OV-6 adopted from
my B3 while (correctly) declining its magnitude; the bench has now
settled it with matched-protocol data.

**Corollary that outranks the bookkeeping: R31/R33's own founding
assumption is refuted at the 2–3% level on a single clean machine.** The
two grids' duration responses have **opposite signs** in the same
session at matched protocol; and session 1 vs session 2 (§2.7) slowed by
+5.37% on r=156 and +8.33% on r=234 — a **2.8-point grid-dependent
difference in a same-machine session factor**. "A session's throughput
factor is grid-independent" is the assumption R31's control and R33's
correction both rest on, and it is now measured false, twice, in two
independent ways, on the best-controlled data this program has.
M3's `G-DURATION-INVARIANT` verdict is *correct about `G`* — the two
grid effects partially cancel in the ratio — and MF-9's mechanism-neutral
labels are the reason that verdict cannot be misread as "degradation is
grid-independent." That fix earned its keep; the per-grid decomposition
should now be persisted alongside it, because it is the load-bearing
finding and `results.json` does not contain it.

### 2.7 The interrupted session is a free, independent, across-reboot replicate of the primary statistic — and it is unused, uncomputed, and unmentioned in `NOTES.md`.

`data/readings_session1_interrupted_20260905T2354Z.json` holds four
completed readings (`S156, S234, U156, U234`, 2026-09-05T23:54Z →
2026-09-06T00:31Z), taken under the same exclusive-use protocol on the
same bench, before the Windows host hung mid-`U234b` (fully disclosed in
`LOGBOOK.md`'s Phase-4 INTERRUPTED entry and `PLAN.md` Current state).
Session 2 re-ran all six from scratch after the reboot. Re-derived:

| | session 1 | session 2 (filed) | spread |
|---|---|---|---|
| `G_short` | `2.3005782` | `2.3130983` | 0.54% |
| `G_sustained` (pair 1 / ABBA mean) | `2.2922399` | `2.2459405` | **2.06%** |
| `k_B` | `3.0458707` | `2.9955462` | 0.050 |
| `excess` | `+1.877%` | `−0.180%` | |
| `signed_dev` from `reference_ratio` | `−0.062609` | `−0.081543` | |

Per-step levels, session 1 relative to session 2 (same machine, ~4.7 h
apart, across a hard reboot): `S156 +4.77%`, `S234 +4.21%`,
`U156 +5.37%`, `U234 +8.33%`.

**Why this matters, and it cuts three ways:**

1. **It strengthens the primary result.** Session 1 independently lands
   inside M5's CONFIRM window, reads `N2_HOLDS` (`+1.88%`), and sits
   nowhere near `G_E`. The headline replicates across a reboot. The
   cycle is throwing away corroboration it already paid for.
2. **It weakens `underpowered = false`.** The across-reboot spread
   (**2.06%**) is **1.41×** the immediate-repeat `d_rep` (**1.46%**) that
   is the sole input to the power gate. The gate's own noise estimator
   understates same-machine reproducibility scatter — which is precisely
   my Phase-2 B5, now measured rather than argued, and Red Team's RT-13
   ("`d_rep` cannot support the weight three composition rules put on
   it"), also now measured.
3. **It is an R25 gap at the freeze line.** `grep` over `NOTES.md`,
   `run115.py`, `analyze115.py`, `chunk_runner115.py` returns **zero**
   hits for `interrupted`, `session1`, `reboot`, or `outage`. `NOTES.md`
   Idealizations does not carry the two-session structure, and
   `PLAN.md`'s own resume recipe explicitly directed that the outage and
   any contribution our run made to it "goes in the record."
   `NOTES.md:619–625` (Phase 4 / Phase 5) are still `(pending)`, so
   nothing is frozen and this is correctable now.

**Zero-cost close:** persist
`sensitivity_session1_across_reboot_DO_NOT_SCORE` with session 1's four
readings, the 2.06% `G` spread, the 1.41× ratio to `d_rep`, and the
grid-dependent level shift; and record the two-session structure in
`NOTES.md` Idealizations. Three lines of arithmetic over a file already
committed.

### 2.8 MF-7(b) IS carried into `result_text`, as promised. Verified byte-wise, twice over.

Two independent carriages, both confirmed by substring test against
`results.json.result_text`:

- Inside `DISCLAIMER_115` (therefore covered by both the
  predictions-side and result-side R23 asserts): *"Pure cell-count (N^2)
  scaling is algebraically identical to the pre-R28 hardcoded exponent
  3.0 and lands INSIDE the CONFIRM band at rel_dev = 0.0799, so a
  CONFIRM does NOT distinguish k = 3.2053 from k = 3.0."*
- In the closing "What this cycle does NOT establish" paragraph: *"…and
  does not distinguish k = 3.2053 from k = 3.0."*

`"BOUNDED-REPLICATION"` is also present in `result_text`. R23's First
Addendum is satisfied for `DISCLAIMER_115`: the identical string appears
in both `predictions_text` and `result_text`, and MF-10 wired both
asserts into committed, re-invocable call sites (`--predictions-only`,
`--selftest`).

**But the interval that earned `m5_protocol_caveat = false` is narrower
than the effect it guards.** `protocol_mismatch_interval` spans
`[2.2176904, 2.2458389]`, `interval_rel_width = 1.269%`, against a
nearest band edge (`2.0785394`) 6.3% away. It is built from this
session's own S and U readings (1000 and 3334 steps) extrapolated via
`p(n) = p_∞ + C_g/n`. exp-114's own measured burst-vs-production factor
on r=234 is **4.90%** — 3.9× the interval's whole width. So the interval
is a *within-burst-regime* extrapolation and structurally cannot contain
the burst-vs-production discontinuity RT-7 was actually worried about.
`m5_protocol_caveat = false` is therefore a true statement about a
narrow question, presented where a wider one was promised.

**Credit where it is due, and it is substantial:** both pre-registered
protocol models are **refuted by the measurement** — `G ≈ 2.5403`
(drift/degradation) and `G ≈ 2.8681–2.8802` (warm-up amortization) both
lie far above the measured `2.2459` and outside the measured interval.
Pre-registering two models and having the data reject both is the
cycle behaving exactly as house discipline intends, and it should be
stated as a result rather than left implicit in a `preregistered_
protocol_models` dict.

### 2.9 M8's headline is persisted but not narrated. R21's third instance, pre-freeze.

Substring tests against `results.json.result_text`: `"sensitivity"` →
**False**; `"DO_NOT_SCORE"` → **False**; `"CLOSER DURATION MATCH"` (the
`sustained_choice_justification` text) → **False**. The word `"straddle"`
appears only inside `DISCLAIMER_115`, as the *pre-registered withdrawal*
of a Phase-1 claim — not as a report of the measured M8 outcome.

M8 **is** Tier-1 item 2, the queue item this cycle folded in. Its own
headline finding — `straddle_still_open = true`, signed dev `−0.1245`,
boundary `G ≥ 2.5652851` — reaches `results.json` and stops there.
R21 (`LOGBOOK.md:881`ff) asks precisely "was the field's own finding
stated in the prose a future citation will actually read?", and carries a
standing forward-elevating clause: **a third occurrence fires Checkpoint
criterion 4 automatically**. Its two founding instances are exp-099 and
exp-100.

**This is not yet that third occurrence** — `NOTES.md`'s Result section
does not exist yet (`NOTES.md:619–625`, `(pending)`), so no frozen record
omits it. It becomes the third occurrence the moment the Result section
is written without it. Contrast M9, which is narrated correctly and
explicitly (`result_text`: *"M9 — fabrication-tolerance bound (ANALYTIC
SIDECAR, R21: stated here, not merely persisted): REPRODUCED"* followed
by the full quotable bound). M9 shows the cycle knows how to do this;
M8 was simply missed.

### 2.10 On the two Phase-2 refutations of my own claims: I accept both, re-derived from primitives, without reservation.

**OV-5 / B9's concavity interval — ACCEPTED, my claim was wrong.**
Recomputed this session from `lab/materials._graded_black` (2×10⁶-point
trapezoid, `Im n = Im√(1 + iσ·cpl/2π)`, `τ_true = 2·(2π/cpl)·
thickness_cells·I_graded`):

```
sigma_max=0.5, cpl=20, thickness=48 cells:  I_graded=0.273840  tau_true=8.258813
sigma_max=0.4, cpl=25, thickness=60 cells:  I_graded=0.273840  tau_true=8.258813
                                            (sigma_max*cpl = 10.0 at both;
                                             thickness/cpl  = 2.40 at both)
```

Bit-identical at both family members, reproducing the filed
`8.258819829686677` to `8×10⁻⁷` relative. My `τ_true ∈ (6.6071, 8.2588)`
scaled `I_graded` by `0.4/0.5` while holding `cpl = 25`, double-counting
the `σ_max` change and ignoring that `cpl` moved with it. The two members
are the same optical article by construction. PHOTONICS was right; the
Director was right to decline. **The load-bearing half of B9 survives and
shipped:** the functional form is the coherent cross term, `exp(−τ_true)
= 2.5897×10⁻⁴` (upper bound `2exp(−τ_true) = 5.1793×10⁻⁴`), not
`exp(−2τ_true) = 6.71×10⁻⁸` — a factor `3.86×10³` — and `result_text`
now states it in the corrected form, at the same order as the measured
aggregate deltas (max `1.0874×10⁻⁴`) rather than 1250–2280× below them.
That correction is the single most consequential thing my seat
contributed this cycle and it is in the permanent record.

**OV-6 / B3's 8.926% — ACCEPTED, my magnitude was wrong.** Recomputed
from `experiments/114-.../results.json.total_wall_s_by_scene` =
`{empty: 2355.9366, hollow: 2326.2051, peccored: 2356.1488}`:

```
peccored/hollow − 1 = +1.2872%      peccored/empty − 1 = +0.0090%
blend/empty         = 0.99582       (the blend is 0.42% CHEAPER, not 4.67% costlier)
burst vs blend-avg  = +4.905%       burst vs empty-avg = +4.467%
```

My 8.926% inherited the "~14% peccored premium" that three other seats
refuted in the same cycle. The corrected comparable is 4.47–4.91%,
**smaller** than `R_DEG = 7.596%`, so my conclusion that M3's bar was
undersized collapses. Accepted. The **sign** finding — adopted by OV-6 —
is the half that survived, and §2.6 above shows the bench data has now
confirmed it directly, with opposite-signed duration responses on the two
grids at matched protocol.

I record both acceptances explicitly because R4's second addendum holds a
Phase-5 reviewer to recomputing rather than restating, and because a seat
that only re-derives the findings that flatter it is not doing the job.

---

## 3. Defects

Numbered, with R-numbers. All are pre-freeze (`NOTES.md` Phase 4/5 are
`(pending)`) and all are zero-FDTD.

| # | Defect | Rule | Severity |
|---|---|---|---|
| **D-Q1** | M8's own headline (`sensitivity_v2_with_measured_G_DO_NOT_SCORE`, `straddle_still_open = true`, signed dev `−0.1245`) and `sustained_choice_justification` are persisted to `results.json` and appear nowhere in `result_text`. Tier-1 item 2's entire product is unnarrated. | **R21** — and this would be the **third** instance, whose standing forward-elevating clause auto-fires Checkpoint criterion 4. Not yet fired: no frozen Result section exists. | **Blocking at close** |
| **D-Q2** | `m7["model_comparison"]["favoured"] = "constant-k"` names a winner among two models the same file's `note` field declares both wrong (8.15% / 13.42%), while the un-nominated pure-`N²` model fits at 0.18%. `run115.py:435–436` is a nearest-neighbour with no goodness-of-fit gate — it cannot emit "no model fits". | **R32** family (a directional/selection reading cited evidentially without validation) + **R18** (the metric is documented as "descriptive" in `predictions_text` and emits a selection verdict) | High |
| **D-Q3** | `m7_underpowered` is computed from `d_rep` alone (`analyze115.py:146`) against a 6.08% model separation, while the cycle's own M6 reports the machine-transfer uncertainty as **18.20%** and `AMBIGUOUS`. The power gate excludes the dominant variance channel by construction. | **R30/R32** family; `lab/ARTIFACTS.md`'s "a silent gate and an absent gate produce identical observations" | High |
| **D-Q4** | Composition is one-directional: MF-9 wired `m6_directional_only = f(m3_verdict)` (`run115.py:405`) but nothing gates M5's `may_move_logbook_verdict = true` or M7's `favoured` on M6's `AMBIGUOUS`. M5 and M7 are both machine-property claims scored while machine transfer is unresolved. | **R24** shape (a stated consequence wired into one classifier and not its sibling) — RT-13's own finding, closed one level and left open one level up | High |
| **D-Q5** | The interrupted session's four readings (`data/readings_session1_interrupted_20260905T2354Z.json`) — an independent same-machine across-reboot replicate bearing directly on D-Q3 — are committed but unused, uncomputed, and absent from `NOTES.md`, `results.json`, `run115.py` and `analyze115.py`. The two-session structure and the bench outage are also absent from `NOTES.md` Idealizations, against `PLAN.md`'s own explicit instruction. | **R25** (a declined item must be a numbered decline with a stated reason) + **R21** family | Medium-high — and it is *corroborating* evidence being discarded |
| **D-Q6** | `protocol_mismatch_interval` (width **1.27%**) is a within-burst-regime extrapolation and cannot contain the burst-vs-production discontinuity it guards; exp-114's own measured value for that discontinuity on r=234 is **4.90%**, 3.9× the interval's full width. `m5_protocol_caveat = false` is presented as discharging MF-7(a)'s promise. | **R18** (a check's claimed scope vs what its code can see) | Medium |
| **D-Q7** | The per-grid duration decomposition — `+1.663%` on r=156 and **`−1.293%`** on r=234, opposite signs, same session, matched protocol — is not persisted anywhere, despite refuting R31/R33's founding grid-independence assumption. `results.json.drift` reports same-grid drift *rates* (MF-6c) but not the short→sustained per-grid responses. | **R21** (a finding the data contains and the record does not state) | Medium — this is the cycle's best physics-of-the-instrument result |
| **D-Q8** | `machine_state.lscpu` reports **7 cores / 14 threads**; the proposal (§6) and `PLAN.md` describe the bench as **8c/16t** (W-2145 nominal). Non-load-bearing for a single-threaded FDTD, but the record's description of the runner does not match the runner's own persisted self-report. | **R4** (a stated figure that does not reproduce from its source) | Low |

**Rules I checked and found NOT violated**, stated so the absence is on
the record: **R33(a)** — honored in full (§2.6); **R33(b)** —
discharged by direct grid-native measurement, which is the whole cycle;
**R23 + First Addendum** — `DISCLAIMER_115` identical in both texts,
both asserts in committed re-invocable call sites; **R19** — 18/18 calls,
conditional assert; **R27/R28** — the budget gate branched three times
upstream of spend (`results.json.gates`), all PROCEED; **R29** — module
naming and identity asserts executed, 10/10; **R13** — correctly
withdrawn per MF-2 rather than mislabelled; **R17** — every band anchored
on `R_DEG` or `ε(2.0)`, both re-derivable; **R9** — M5's operands are
same-session, same-machine, same-protocol by construction.

---

## 4. Ranked top-3 candidate directions

Iteration 93's Tier-1 item 1 is fixed by D2 (VISION's constraint-3
re-score). These are my seat's ranked candidates for **Iteration 93 items
2–3** and **Iteration 94 item 1**, from my charter and its expressibility
contract.

I state the frame first, because it governs the ranking. This is the
**12th consecutive cycle** declaring "T1 escape route: NONE," and my seat
has now spent 92 iterations watching a wall-clock cost-exponent
sub-thread while the constraint-3 ledger has gained nothing. D2 fixes
that for item 1. Items 2–3 should either put an effective classical
nonlinear parameter on the bench, or unblock the one check that can
close σ(I) as a class — not extend T28 again.

### RANK 1 — Iteration 93, item 2: **run the T18 primary-source probe with a positive control, and if it clears, execute the rigorous RSA/TPA/third-class realizability check that has been the #1 named priority since Iteration 13.**

*Charter: mine and MATERIALS' jointly; the expressibility contract makes
it mine — σ(I) enters the bench only as an effective classical parameter,
and whether any material supplies that parameter is the question this
check answers.*

**Why it outranks everything else on the board.** LOGBOOK T18
(`LOGBOOK.md:2387`ff) records that every realizability verdict since
Iteration 13 rests on WebSearch-snippet synthesis, never
primary-source-verified, after 39+ consecutive WebFetch failures — and
that **no literature-check cycle can escalate to Checkpoint criterion 2
without a working primary-source route**. Iteration 12's own Red Team
adjudication ranked "the rigorous RSA/TPA/third-mechanism-class
literature check (MATERIALS/QUANTUM, zero cost, could fire or
definitively not-fire Checkpoint-2, three-cycle-plus overdue)" as
priority **(1)**, above N33. That was **80 iterations ago**. It is the
only item on any queue that can produce a Checkpoint-criterion-2
result — "the honest alternative product" PANEL.md's own stop conditions
name — and it costs zero FDTD calls and zero grid-steps.

**The new fact that makes it actionable, and its caveat.** `WebSearch`
and `WebFetch` are both present in this session's available tool set.
That is a change from the state T18 records. It is **not** evidence they
work: the class rule binds, and a tool listed is not a tool heard from.
So the item is scoped in two stages, the first of which is ~10 minutes:

- **Stage A — positive control.** Fetch a primary source whose content is
  already known from the repo's own record (e.g. an exp-061-cited
  reference) and confirm the returned text contains a figure the record
  already quotes. A probe that can only return "blocked" is not a probe.
  Persist the raw result either way, so T18's status becomes a measured
  fact rather than an inherited one.
- **Stage B, only if A clears.** The rigorous check on the two named
  gaps: RSA's dynamic-range shortfall (`D_req ≈ 537–600×`, "1–2 orders
  short") and TPA's irradiance shortfall (flashlight `~10⁻³ W/cm²` vs
  published onset `10⁶–10⁹ W/cm²`, "9–12 orders short"), against
  primary sources rather than snippets — plus T18's own clause (b)
  survey: does **any** unchecked class have a gap ≲5–6 OOM that
  realistic field enhancement genuinely closes?

**Outcomes, both valuable.** Confirmed at primary-source tier, the two
gaps fire **Checkpoint criterion 2** — a proven boundary within the σ(I)
mechanism class, which is a real finding about the witness statement and
one of the program's two named success conditions. Refuted, σ(I) regains
standing it has not had since Iteration 12 and Rank 3 below becomes the
obvious next FDTD cycle. Blocked at Stage A, T18's block is re-confirmed
as a *measured* fact for the first time in 78 iterations and the
escalation PHOTONICS called overdue at Iteration 14 goes to Marsh with
evidence. There is no outcome in which this cycle wastes its slot.

**Falsifiable, pre-registerable:** Stage A passes iff the positive
control returns text containing the known figure; Stage B's verdict bands
are the OOM gaps already frozen in `REALIZABILITY_MEMO.md`.

### RANK 2 — Iteration 93, item 3: **close exp-115's seven zero-cost gaps as one bookkeeping item, and wire M6 into M5 and M7.**

*Charter fit: this is the statistics-and-selection-rules lane the
Director assigned my seat, and the expressibility contract depends on
it — I cannot get a σ(I) sweep priced and approved without a cost gate
whose own uncertainty accounting is honest.*

Six of the seven are pure disclosure and can be done at the Iteration-92
close rather than waiting for 93 — I recommend that, and list them here
so they are a numbered queue line (R25) if they are not:

1. **D-Q1** — narrate M8's headline in `result_text` and the `NOTES.md`
   Result section. *This one is not optional*: R21's third instance
   auto-fires Checkpoint criterion 4.
2. **D-Q2** — replace `favoured` with `"NO MODEL FAVOURED"` plus the
   0.18%-vs-8.15%-vs-13.42% comparison.
3. **D-Q3/D-Q4** — one new persisted boolean,
   `machine_transfer_caveat = (m6_verdict != "TRANSFERS")`, gating
   `m5["may_move_logbook_verdict"]` and `m7["model_comparison"]
   ["favoured"]`. Four lines of code; it closes the one-directional
   composition RT-13 named.
4. **D-Q5** — persist
   `sensitivity_session1_across_reboot_DO_NOT_SCORE` and record the
   two-session structure + bench outage in `NOTES.md` Idealizations.
5. **D-Q6** — state the interval's scope: it bounds within-burst
   extrapolation only, not the 4.90% burst-vs-production step.
6. **D-Q7** — persist the per-grid short→sustained decomposition
   (`+1.663%` / `−1.293%`) and state that R31/R33's grid-independence
   assumption is refuted at the 2–3% level on one clean machine. **This
   is a real result and it currently exists only in this review.**
7. **D-Q8** — correct the bench description to 7c/14t as the machine
   itself reports.

The one item that genuinely belongs in Iteration 93 rather than the
close: **write the honest `KAPPA_COST_EXPONENT` statement from §2.5 into
LOGBOOK's T28 entry** — the five-row table, the four confounds, and the
ruling that `k` is a per-machine fitted parameter with one measurement
per configuration, retained at 3.2053 for gate conservatism and labelled
as a gate-margin choice. Every future cost gate cites this constant; the
record should say what it is.

### RANK 3 — Iteration 94, item 1: **the first bench-native σ(I) two-intensity run — reverse-saturable absorption as an effective classical parameter, priced from exp-115's own measured cost law.**

*Charter: squarely and only mine. This is the T1 escape route my seat
exists to express, and it has not been on the bench since Iteration 12.*

**Not a re-proposal of a ruled-out idea, checked line by line.** R1's
addendum rules out a dominantly-**real** `Δε` shift, static or
intensity-triggered — an RSA σ(I) is dominantly **imaginary/absorptive**
and is not under R1. Red Team's Iteration-12 ruling is explicit:
"criterion 2 (proven boundary within a mechanism class) does **NOT**
fire — this thread shows one calibration point fails correctly-
instrumented measurement at both geometries checked, not that σ(I) as a
class is jointly unsatisfiable" (`LOGBOOK.md:2219`ff). σ(I)'s status is
"permitted, undemonstrated" — the same standing as the other three
routes. What died at Iteration 12 was exp-032's *single bench PASS* under
N17 quadrature correction, not the class. The near-null σ(I) article
follow-up is named on file, repeatedly, and **still not run**.

**Why RSA and not saturable absorption:** the sign is the whole point.
Saturable absorption gives *low* σ at high intensity — the beam punches
through, which fails constraint 1. Reverse-saturable absorption gives
`σ(I) = σ₀(1 + I/I_ref)`: the ambient field sees the low σ (constraint 3
survivable) while the swept beam sees the high σ (constraint 1
satisfiable). That asymmetry is the only reason T1's
linear-time-invariant theorem does not bind — the medium is nonlinear,
so "the extinction that terminates the beam darkens the ambient view
identically" is simply not a theorem about it.

**Expressibility, per my own contract:** `σ_eff(x, |E|²) = σ₀(x)·(1 +
|E|²/E_ref²)`, with `σ₀(x)` the committed `_graded_black` profile scaled
to a near-null `τ_off` and `E_ref²` the one free parameter, swept. Two
source amplitudes spanning `E_ref`, three scenes each, identical
`graded_black_shell` geometry at **r=156 / cpl=25 — the exact
configuration exp-115 just calibrated**.

**The direct payoff of exp-115, and the reason this belongs at Iteration
94 rather than sooner.** For the first time this program has a
same-machine, same-grid, matched-protocol per-step rate for this
configuration: `0.0497051 s/step` sustained on the bench. A production
leg of 3 scenes × 8000 steps × 2 intensities = 48,000 grid-steps prices
at **~2,386 s (~40 min)**, projected from a measurement rather than a
cross-session extrapolation — which is precisely the R31/R33 confound
this whole sub-thread has been fighting, now removed for this grid. The
budget gate can be run honestly for the first time. That is what
exp-115's instrument work was *for*, and spending it on another cost
cycle would waste it.

**What it needs that this cycle cannot supply, stated plainly:** an
intensity-dependent σ update in the FDTD engine is real new engine
physics beyond the validated bench classes — **PANEL.md Checkpoint
criterion 3**. It must be proposed as such, with a new trust-suite stage
carrying at least one absolute identity gate (the σ(I) article at
`I → 0` must reproduce the committed linear article bit-exactly) before
any result is trusted. Rank 1 running first is deliberate: if the
primary-source check fires criterion 2 against RSA, this build should not
happen at all, and Iteration 94 should take σ(x,t) — the externally
triggered route, which satisfies constraint 4 natively and has never been
expressed as bench parameters either.

**Runners-up, named so they are not silently dropped (R25):** (a) the
three-grid same-session `k` identification (r=156/234/312 at fixed
cpl=25, ~75 min at the measured rate) — it separates `kappa_ratio` from
absolute `N` and would settle §2.5 with two independent exponents on one
machine, and it discharges exp-115's declined Tier-1 item 3; I rank it
below Rank 3 only because it is instrument work and my charter's honest
answer is that this program needs a mechanism cycle more than it needs a
sixth exponent; (b) exp-115's own declined items 3, 4, 6, 8, 9, and the
`R2_SMOOTH_THRESHOLD = 0.90` re-derivation, now in its **eighth**
consecutive cycle.

---

## 5. Summary (≤150 words)

**PARTIAL.** The measurement is the cleanest this sub-thread has taken —
every statistic bit-exact from primitives, ABBA executed, identity gate
10/10, MF-5's invocation fix live. R33(a), my own addendum, is honored in
full; MF-7(b)'s caveat is in `result_text` twice. But the inference
over-reaches. `G_bench` and `G_E` differ by **22.2%**, wider than M5's own
CONFIRM half-width — each replicate places the other in AMBIGUOUS while
both CONFIRM the reference between them; M6 says so and nothing gates M5
or M7 on it. "Favoured: constant-k" names a winner among two models the
same file calls both wrong, while un-nominated pure `N²` fits at 0.18%.
`k` is not a constant: five measurements span 2.9955–3.6090 with four
confounds moving together. Seven zero-cost closes outstanding, one
(M8 unnarrated) is R21's third instance. I accept both Phase-2
refutations of my claims, re-derived.

---

*QUANTUM OPTICS, Phase 5, exp-115. Worked alone: no sub-agents, no
delegation, no simulations, no git state changed. No other seat's
`phase5_review_*.md` was read. Every figure above was recomputed this
session in pure python against committed JSON and committed source, or
re-derived from primitives; none is restated from the proposal's, any
critique's, or the audit's prose.*
