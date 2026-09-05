# exp-115 — Phase 2 critique — QUANTUM OPTICS (blind)

*Panel Iteration 92, candidate exp-115. Written blind to every other
seat's current-cycle output. Charter: non-classical absorption,
state-dependent or coherent interactions; expressibility contract —
mechanisms enter the bench only as effective classical parameters.
Phase-4 venue: the T5820 bench, a machine no prior experiment ran on.*

---

## 1. Steel-man (≤150 words)

The load-bearing identity is real and I reproduced it bit-exact, by an
independent route: because `HISTORICAL_PER_STEP_S` is *defined* as
`HISTORICAL_R156_CPL25_TOTAL_S/(3×8000)` and the cost gate's own pilot
total *is* that same constant, `t156_session_adjusted` collapses
algebraically to `24000 × p156_sustained`, and exp-114's scored
`measured_ratio` collapses to `1.5 × G`. Every cross-session term
cancels. That is a genuinely new, correct, and consequential reading of
a frozen verdict, and no seat — including mine — saw it last cycle.
The consequence the proposal draws is right: what exp-114 scored was
never a cross-session ratio, so the cheapest possible measurement — six
control bursts, 46,008 grid-steps, zero production legs — can replicate
or refute a filed CONFIRM. The R17 anchoring discipline is real
(`R_DEG`, `ε(2.0)` both invoked, both re-derivable), the composition
rules are pre-registered as code, and the declined-items list is honest.

*(141 words.)*

---

## 2. Sharpest attack (≤150 words)

**The proposal's headline claim — that my seat's short-reading flip and
Red Team's v2 straddle "are the same question," resolved by measuring
`G` — is false, and its own numbers show it.** v2 never touches an
r=156 rate. Reconstructed from the audit's primitives, `measured_ratio_v2
= 1.5 × 2.25 × (p234_prod/p234_burst)`; the assumed `2.25` is one
operand, and `p234_prod/p234_burst = 0.95324` — an intra-r=234-grid
production-vs-burst factor — is the other. This cycle measures the
first and, by declining every production leg (§2.2), leaves the second
exactly where exp-114 left it. Substituting a measured `G`, the two
methods stop straddling `reference_ratio` only for `G ≥ 2.5652851`.
Over **66.4%** of M5's own CONFIRM band the cycle returns "CONFIRM,
replicated" while the straddle is still open — and no metric, M6
included, ever recomputes v2.

*(134 words.)*

---

## 3. Verdict

**support-with-changes.**

**The single change that would flip me to plain support:** add a
pre-registered metric — call it **M10** — that recomputes
`measured_ratio_v2' = 1.5 × G_sustained × (HIST_R234_PER_STEP_S /
p234_burst_exp114)` from committed constants (`p234_burst_exp114 =
0.2050977960427602`, `experiments/114-.../phase5_redteam_audit.md:249`),
scores its **signed** deviation against `reference_ratio` alongside
method 1's `+0.12275`, and pre-registers **STRADDLE-CLOSED iff
`G_sustained ≥ 2.5652851279677367`** / **STRADDLE-OPEN** otherwise. Zero
FDTD cost — it is three multiplications on numbers this cycle already
produces. Without it, §1 and §5-M6's "resolves the straddle" claim is an
assertion the cycle cannot cash, and the Iteration-92 queue's Tier-1
item 1 goes into LOGBOOK as discharged when its stated consequence was
not computed (R24 shape).

Five further changes I consider required, in descending order (all
derived in the Appendix): **(a)** M9(c)/(d)/(e) — the round-trip
core-return estimate must be `exp(−τ_true)` (a coherent field amplitude),
not `exp(−2τ_true)` (an incoherent intensity); the correction is a factor
**3861.5**, and it inverts (c)'s conclusion. **(b)** M9(d)'s headline
`1.6×10⁻⁴` must state its normalization, and must report the program's own
locally-normalized readings (`1.47×10⁻²` / `5.29×10⁻²`) beside it.
**(c)** Reorder readings 5–6 to **ABBA** (`U156, U234, U234b, U156b`) —
free, and it converts `d_rep` from a noise estimate into a drift
estimate. **(d)** M5 needs a composition/degradation branch; it is the
only metric in the cycle without one, and it is the only one that can
move a frozen verdict. **(e)** M7's primary band needs a power gate and
signed reporting.

---

## 4. Appendix — derivations, re-derived figures, and rule findings

Every figure below was computed this session from committed files, not
transcribed. Two-space-indented blocks are what I actually ran.

### A. Figures I re-derived successfully (the proposal's §2.0 grounding table)

**A1 — the identity `measured_ratio ≡ kappa_ratio × G`. CONFIRMED,
bit-exact, and by a route the proposal does not state.**
`analyze114.py:111` computes `t156_session_adjusted =
R.HISTORICAL_R156_CPL25_TOTAL_S / control["used_speed_ratio"]`.
`run114.py:198-201` fixes `HISTORICAL_R156_CPL25_TOTAL_S =
670.4777698516846` with `assert ... == EXP112_RESULTS["total_wall_s"]`,
and `HISTORICAL_PER_STEP_S` is that constant over `3×8000`. I verified
`670.4777698516846/24000 == 0.02793657374382019` is `True` in float, and
`used_speed_ratio = HISTORICAL_PER_STEP_S / this_session_per_step_s`.
Therefore

    t156_session_adjusted = HIST_TOT × p156/(HIST_TOT/24000) = 24000 × p156

with `HIST_TOT` cancelling *identically*, not approximately. I confirmed
`24000 × 0.07121022268191168 == 1709.0453443658805` (the filed value)
is `True`, and `1.5 × 2.74550565394726 == 4.11825848092089` is `True`.
**The cancellation is exact only because the pilot total and the
per-step constant are literally the same number** — that is the
non-obvious part of the identity, and it should be stated in NOTES.md,
because a future cycle that supplies a different pilot total breaks it
silently.

**A2 — bands.** `G_ref = 1.5**(k−1) = 2.4453404739580256`;
CONFIRM `G ∈ [2.0785394028643216, 2.812141545051729]`; REFUTE
`G ≤ 1.7117383317706178` or `G ≥ 3.1789426161454335`. All four match the
proposal's §5-M5 figures to every digit printed. Note
`classify_kappa_exponent_check(exponent_234, ...)` (`run114.py:258`)
takes an **exponent**, not a ratio — M5's "invoking it unmodified" is
only true through `exponent = 1 + ln(G)/ln(1.5)`, a conversion §5-M5
never states. Minor, but it is an R18 scope claim about a check's code.

**A3 — `R_DEG = 0.07596424755863729`.** Reproduced from
`results.json.r31_control`. Confirmed.

**A4 — R28's `0.152950039837078` is exactly `ε(2.0)−1`.** Re-derived
from exp-110's *raw per-scene* wall times rather than the quoted ratio:
`t156 = 250.6266098022461+250.08318996429443+251.51349687576294 =
752.2232966423035`; `t312 = 2334.8423988819122+2232.955216884613+
2370.4094228744507 = 6938.207038640976`; ratio `9.223600318696624`;
`ln(·)/ln 2 = 3.2053299988171697 = KAPPA_COST_EXPONENT`
(`experiments/110-.../run.py:377`). Dividing out the step ratio (2.0)
and the cell ratio (`(2240/1120)² = 4.0`) gives `1.152950039837078`.
**The proposal's claim that R28's founding miss *is* the per-step
superlinearity is correct and is a real contribution.** Note the grids:
exp-110 spans `N = 1120 → 2240` at `cpl=20`; this cycle spans
`N = 1400 → 2100` at `cpl=25` (`experiments/112-.../run112.py:110`,
`N = round(N0·k·cpl/20)`). Both `k` and `ε` are being treated as
functions of `kappa_ratio`, but cache/bandwidth superlinearity is a
function of **absolute** `N`. Neither of M7's two candidate models is
well-specified as stated; M7 can only ever be descriptive.

**A5 — sensitivities.** Short-reading: `G_short = 2.9540659251173476`,
`measured_ratio = 4.431098887676021`, `rel_dev = 0.20803869914110543`.
Matches the proposal's `0.20803870` exactly. v2: see B1.

**A6 — energy-ledger deltas (M9(a)).** From
`experiments/114-.../results.json.energy_ledger`: σ_scat
`|551.5854282367458−551.6454083870983|/551.6454083870983 =
1.0873…×10⁻⁴`; σ_abs `5.666×10⁻⁶`; σ_ext `5.2043×10⁻⁵`; floor
`|1093.4682853909158−1093.4986768887502|/1093.4682853909158 =
2.7794×10⁻⁵`. All four match the proposal's r=234 column. Confirmed.

### B. Findings

**B1 — the straddle is a two-operand object; this cycle measures one
operand (the sharpest attack, derived).**
From `experiments/114-.../phase5_redteam_audit.md:249-262`:

    p234_burst = (204.2541103363037+196.82920837402344+214.2100694179535)/3000
               = 0.2050977960427602          (empty scene, first 3000 steps, cold)
    speed_ratio_v2 = (0.02793657374382019×2.25)/p234_burst
    t156_adj_v2    = 670.4777698516846/speed_ratio_v2 = 24000×p234_burst/2.25
    measured_ratio_v2 = 36000·p234_prod / t156_adj_v2
                      = 1.5 × 2.25 × (p234_prod/p234_burst)

I reproduce `3.2171956285212335` exactly. **No r=156 quantity appears.**
The construction's two unverified operands are (i) `G = 2.25` and (ii)
`p234_prod/p234_burst = 0.19550806899203194/0.2050977960427602 =
0.9532431491914767`. Item 1 measures (i). Item (ii) is an
intra-r=234-grid production-vs-burst factor; §2.2 runs **no** r=234
production leg, so it is untouched. Substituting the measured `G`:

    signed_dev(v2′) ≥ 0  ⟺  G ≥ 3.6680107109370383/(1.5×0.9532431491914767)
                                = 2.5652851279677367

M5's CONFIRM floor is `2.0785394`; `(2.5652851−2.0785394)/(2.8121415−
2.0785394) = 0.6635` — **66.4% of the CONFIRM band returns CONFIRM with
the straddle still open.** Exact numerical agreement between the two
methods needs `G = p234_burst/p156_sust = 2.8801734964221324`, which is
**above** the CONFIRM ceiling: the cycle cannot both fully reconcile the
methods and CONFIRM. And the cycle's own most likely value is inside
the still-open region — see B2. §5-M6 is titled "the direct answer to
the v2 straddle" but computes `T = G/G_E`, a cross-machine ratio that
never touches v2's construction.

**B2 — M5 is pre-loaded toward CONFIRM by a known-sign effect the
proposal does not price.** exp-114's numerator was a 12000-steps/scene
production rate; exp-115's is a 3334-steps/scene burst. `R_DEG > 0`
establishes the sign (longer ⇒ slower per step) on the r=156 grid.
Log-linear extrapolation of `R_DEG` from `1000→3334` to `3334→12000`:

    0.07596424755863729 × ln(12000/3334)/ln(3334/1000) = 0.08079
    predicted G_115 ≈ 2.74550565394726/1.08079 = 2.5402672
    rel_dev ≈ 0.03882  (comfortable CONFIRM); straddle: 2.5403 < 2.5653 → OPEN

Because `G_E > G_ref`, *any* downward protocol correction moves the
result toward CONFIRM. §5-M5's advertised falsifier is the **upward**
edge (`G > 2.8121415`, only 2.427% above `G_E`) — the side the design
makes less likely — and the framing "sits inside the CONFIRM window at
82% of the way to its upper edge" quotes the position of `G_E`, a value
this cycle's own design predicts it will not reproduce. The downward
REFUTE bar (`1.7117`) is 30% away and unreachable by any effect on file.
The magnitude of the extrapolation is uncertain; **the sign is not**,
and nothing in §5 or §7 discloses it.

**B3 — the R_DEG anchor is a composite, and the only comparable r=234
datum has the opposite sign (R17).** `chunk_runner114.py:184-191`:
`run_control()` calls `_time_control_blend(SHORT_CONTROL_STEPS)` and
*then* `_time_control_blend(SUSTAINED_CONTROL_STEPS)`. `R_DEG` therefore
mixes a duration effect with an elapsed-session-position effect and has
never been decomposed. Meanwhile the only intra-grid duration datum on
r=234 runs the other way: the first 3000 steps cost `0.2050978` s/step
against a 36000-step average of `0.1955081` — the long run is **4.905%
cheaper**, and scene-mix-corrected (exp-113's ~14% `peccored` premium,
blend/empty = `1.04667`) **8.926%** cheaper. R17 requires anchoring on
the *largest already-established comparable* shift: that is 8.93%, not
7.60%, and it is opposite in sign. M3's DOES-NOT-CANCEL bar is
undersized against the record, and its CANCELS branch is exactly the
"narrower-than-precedented bracket returning the reassuring outcome"
shape R17 was written for. The proposal cites those same three chunk
times (Idealization 4, line 651) for chunk-boundary variability and
misses what their mean says about the duration trend it anchors on.

**B4 — the execution order biases `G` upward in every pair, and biases
M3 (free fix).** Order 1→6 places the r=234 leg **after** its r=156
partner in all three pairs. Under any monotone session drift the ratio
is biased up. Worse, the pair-internal midpoint lag is 3.33× larger for
the sustained pair than the short pair by construction (10002 vs 3000
grid-steps per reading), so even a perfectly *grid-independent*
multiplicative drift produces `G_sustained > G_short` and reads as
PARTIAL/DOES-NOT-CANCEL. **ABBA** (`U156, U234, U234b, U156b`) cancels
linear drift in the geometric mean of the two pair ratios and turns
`d_rep` into a drift measurement. Cost: reordering two lines.

**B5 — `d_rep` cannot support the weight three composition rules put on
it.** It is a single-difference, 1-degree-of-freedom statistic; for two
i.i.d. readings `E|ΔG|/G ≈ 1.128 σ`, with `P(observed < 0.4·typical) ≈
0.31`. The repeats are *immediate*, so they sample short-timescale
scatter and not the contention/thermal drift Idealization 11 names as
the dominant noise source — an estimator biased **low** for the variance
the gates are guarding. Consequences: M3's `UNINTERPRETABLE` gate fires
only at `d_rep > 0.0379821`, so a CANCELS verdict may be declared at
`d_dur = 0.0379` with `d_rep = 0.0379` — signal-to-noise 1.0. M4's own
labels disagree with that gate (a "MARGINAL" `d_rep = 0.05` still kills
M3, but the persisted verdict string does not say so). **This is the
"quietly favorable verdict" path the metrics table permits.**

**B6 — M7's primary band has no power gate, and its REFUTE bar *is* the
rival hypothesis's point prediction.** `2.25 × ε(2.0) = 2.5941375896`,
so `excess = 0.152950039837078` — bit-identical to M7's own `N2_FAILS`
threshold. A test whose failure bar sits on the alternative's central
value is a coin flip when the alternative is exactly true. The two
models differ by `6.0849%`; the proposal declares the *secondary*
comparison UNDERPOWERED unless `d_rep ≤ 0.03` (line 402) but attaches
**no** power condition to the primary band, whose AMBIGUOUS window
(`G ∈ [2.3625, 2.5941]`) is only ~1.6× the separation it just called
unresolvable. Add the same `d_rep ≤ 0.03` gate to M7's primary.

**B7 — M7's label conflates two opposite physical readings (R32
family).** `|excess| ≥ 0.1529500` also fires at `excess = −0.1529500`,
i.e. `G = 1.9058624`, which is *sub*-cell-count scaling — the opposite
finding — yet both branches persist the string `N2_FAILS` and inherit
the meaning "as large as the r=312 grid's already-established one"
(line 388), true only on the positive branch. R32's founding catch was
this seat's, at Phase 2, on exactly this shape: an unvalidated direction
attached to a magnitude statistic. Report `excess` **signed**, with
distinct labels. §8's "R30/R32 **N/A**" is therefore too quick.

**B8 — M6 measures a product, not a transfer.** Under the separable
model `p = M(machine)·Grid(g)·Prot(protocol)`, `G_bench = Grid₂₃₄/Grid₁₅₆`
(protocol cancels) but `G_E = (Grid₂₃₄/Grid₁₅₆)·(Prot_prod/Prot_burst)`.
So `T = G_bench/G_E = Prot_burst/Prot_prod` — M6's `TRANSFERS` /
`DOES-NOT-TRANSFER` labels read a *protocol* factor as a *machine*
factor, and cannot separate them with two machines and one protocol
each. The guard §5-M6 supplies (`g_e_protocol_caveat` gated on M3) is
keyed on a statistic living entirely inside the burst regime (1000 vs
3334 steps), which cannot detect the burst-vs-production factor it
guards against. *An alarm that cannot produce the reading that means
"bad" is not an alarm* — `lab/ARTIFACTS.md`'s own invariant. Gate the
caveat on B1's M10 instead.

**B9 — CHARTER-NATIVE, and the most consequential single error I found:
M9(c) uses an incoherent intensity attenuation where the observable is a
coherent field interference.** `τ_true` is an **intensity** optical
depth by construction — `experiments/061-.../NOTES.md:42` defines
`tau_true = 2·(2π/cpl)·thickness_cells·I_graded`, the leading `2` being
exactly the intensity-vs-amplitude factor, corroborated by its own
`e-fold = 1/α = 174.36 nm` and `OD = τ/ln10 = 3.587`. Hence the
round-trip **amplitude** of the core-return wave is `exp(−τ_true)`, and
`exp(−2τ_true)` is that wave's own intensity *in isolation*. But
σ_scat and the per-bin pattern are quadratic in the **total** field:

    |E_shell + δE|² − |E_shell|² = 2·Re(E_shell*·δE) + |δE|²

The measured quantity is the **cross term**, first order in `δE`, so it
scales as `exp(−τ_true) = 2.5896×10⁻⁴` — not `exp(−2τ_true) =
6.7063×10⁻⁸`. The proposal's estimate is low by a factor **3861.5**.
This inverts M9(c): the correct zero-free-parameter prediction is
`O(10⁻⁴)`, i.e. **the same order as every measured delta**
(`1.09×10⁻⁴` … `1.53×10⁻⁴`), not "three orders of magnitude below
anything this instrument can resolve." At the member the r=234 data
actually came from (cpl=25, σ_max=0.4, 60 cells), concavity of `Im(n)`
in σ bounds `τ_true ∈ (6.6071, 8.2588)` — I computed the lower end as
`2·(2π/25)·60·(0.8×0.273840)` — giving `exp(−τ_true) ∈ (2.59×10⁻⁴,
1.35×10⁻³)`, i.e. **1×–12× the measured deltas**. Consequences:
(i) M9(b)'s "upper bound set by the instrument's own floor, not a
resolved effect" loses its corroboration and is probably wrong for the
per-bin channel; (ii) M9(d)'s sentence "the physical value is predicted
at `O(10⁻⁷)`" would enter the permanent record false; (iii) M9(e)'s
forward claim "the bound scales as `exp(−2·τ_true)`" halves the true
exponential rate. **Note the pre-registered HALT cannot catch this:**
M9(c)'s gate only checks that `τ_true` *reproduces*, never that the
functional form is right — a gate that passes while publishing a wrong
physical prediction.

**B10 — M9(d)'s headline is normalization-silent and picks the most
favourable denominator (R9).** exp-108's `rel32` is **peak**-normalized:
`rel32 = |delta32|/max|peccored32|`
(`experiments/108-.../run.py:241-242`), giving `1.4760×10⁻⁴` (r=156) /
`1.5266×10⁻⁴` (r=312). The program's own purpose-built per-bin
instrument — exp-110's `classify_item_i_local`, built at Iteration 87
specifically to discharge R13's denominator question — computes
`local_rel = |Δ|/|pattern_peccored|` per bin
(`experiments/110-.../run.py:348`) and reports, on the same physical
perturbation, `max = 0.014669070259562213` (r=156, 34/48 bins clearing
the mirror-pooled floor) and `0.05290046381280309` (r=312, 38/48).
That is **99.4×** and **346.5×** weaker than the figure M9(d) quotes.
A fabrication claim as strong as "a real process ... does not need to
control the substrate or core material ... at all" cannot rest on a
silent choice between two normalizations that differ by 2.5 decades.
Relatedly, M9(b)'s floor-gate covers the **six aggregate** deltas only;
the per-bin channel — the channel that actually *sets* the `1.6×10⁻⁴`
headline — is given no floor at all, while M9(d) nonetheless calls the
figure "an upper bound set by the instrument's own floor." The floor
gate is applied to the channels that do not set the headline.

**B11 — M9(e) states the negation of a registered caveat, and the lint
cannot fail on it.** `lab/caveat_lint_config.json`, entry
`exp052-alpha-60nm-absorptivity-open`, trigger term `tau_shell`,
required phrases include *"absorptivity, not thickness"* / *"absorptivity
unchecked"*: every site citing this number must disclose that **the
absorptivity question, not just the thickness question, remains open.**
M9(d) puts `tau_shell = 24` in its headline sentence and M9(e) concludes
"leaving **thickness as the binding constraint** it already was." Two
further entries also trigger on this document — `exp063-alpha-true-efold-
staleness` (`tau_true`, `e-fold`) and `exp061-t18-evidentiary-tier-
propagation` (`PUBLISHED…PLAUSIBLE…UNOBTANIUM`, `alpha…5.74`). **None of
them will fail CI:** `lab/caveat_lint.py:64-68` states trigger terms are
"used only to discover NEW candidate sites, **never** gates the exit
code," and `check_caveat()` (`lab/caveat_lint.py:220-233`) only reports
candidates. So the cycle's own compliance here is a human duty the
proposal's §8 rule list does not mention at all.
On the substance: M9(e)'s "α_true ≈ 5.74×10⁴ cm⁻¹ is *not* an
implausible absorption rate" is quoted from exp-061's frozen **MP-4
prediction cell**, not from its **result**. MP-1's actual Phase-4
outcome (`experiments/061-.../NOTES.md`, results section) is that
real CNT-forest-class α clusters at `78 – 3.1×10³ cm⁻¹` and *"nothing in
the CNT-forest class approaches the corrected target."* The measured
absorptivity gap is therefore `5.7353×10⁴/3.1×10³ = 18.5×` to
`5.7353×10⁴/78 = 735×` — the same order as the thickness gap (70–350×),
not a resolved non-issue. Citing a pre-run prediction cell as the
outcome is R4/R19 territory.

### C. Rule-compliance summary

| Rule | Finding |
|---|---|
| **R4** | §2.0 discipline is genuinely good — every grounding figure I checked invokes rather than transcribes. One exception: M9(e)'s "not an implausible absorption rate" restates exp-061's frozen prediction cell as its result (B11). |
| **R9** | Two live instances: M5 scores a burst-vs-burst ratio against a reference (`k`) fitted from **production**-to-production wall times at `cpl=20`, `N = 1120→2240` (A4, B2); M9(d) compares a peak-normalized delta with a claim about per-bin sensitivity (B10). |
| **R13** | Applied to six aggregates, **not** to the per-bin channel that sets M9(d)'s headline (B10). exp-110 already built the floor machinery for exactly that channel. |
| **R17** | `R_DEG` is a duration/elapsed-position composite (B3); the largest established comparable intra-grid shift is 8.93% with the **opposite** sign, so M3's bars are undersized and mis-signed relative to the record. |
| **R18** | M5's "invoking `classify_kappa_exponent_check()` unmodified" requires an unstated `exponent = 1 + ln(G)/ln 1.5` conversion (A2). |
| **R21/R23** | The proposal commits to `DISCLAIMER_115` with both asserts but never says **what it contains**. M9 requires at least four distinct caveats (analytic-sidecar-not-FDTD; upper-bound-not-resolved-effect; the article **fails constraint 3 by construction**; T18 tier). R23's own Iteration-82 scope-limitation queue item — genericize to a `(sentence, required_locations)` table or ratify single-disclaimer scope — is still open and is squarely this cycle's to close. |
| **R24** | Queue Tier-1 item 1's *own stated consequence* ("re-score `kappa_exponent_result` against the corrected denominator") is not implemented as a binding element of any classification; M5 is a fresh statistic, not that re-score, and `HIST_R234_PER_STEP_S` is carried "informationally" only (§2.3). M10 (Verdict) fixes this at zero cost. |
| **R32** | §8's "N/A" is too quick: M7 attaches a one-sided physical meaning to a two-sided magnitude statistic (B7). |
| **R33(a)** | My own addendum. The proposal's re-justification of "sustained" on protocol-commensurability grounds is **better** than the conservatism appeal it replaces — I accept it — but it proves too much: by its own criterion the right comparator for a production-fitted reference is a production-duration reading, which this cycle also declines (B2). |
| **R33(b)** | PHOTONICS' cross-grid addendum is genuinely discharged for M5 by direct measurement. Credit where due. |

### D. Constraint-3 and metrics-table risk

Item 1 touches no constraint metric; T1 route NONE is correct. The risk
is **M9(d)/(e)**. Its bolded sentence — *"a real process implementing
this design does not need to control the substrate or core material"* —
is written to be quoted (§8 says so, under R21). Quoted without §4, it
reads as fabrication progress on *the lab's design*, for an article
LOGBOOK's ESTABLISHED section records as **failing constraint 3 by
construction**. That is the R16/R21/R23 disclaimer-erosion shape this
program has now caught eight-plus times, and it is exactly how constraint 3
gets quietly dropped: not by a claim that it is satisfied, but by a
cheerful fabrication bound on an article that fails it. The
constraint-3-failure sentence must be **inside** `DISCLAIMER_115`, with
both asserts, and inside the bound's own quoted paragraph — not two
sections away in §4.

Second, smaller: seven of the eight metrics are wall-clock statistics.
Nothing in this cycle records a single row of PANEL.md's own metrics
table. That is legitimate for an instrument cycle and the proposal says
so — but the record should note that Iteration 92 is the **12th
consecutive** cycle declaring "T1 escape route: NONE," and that §3's
declined Tier-3 item 10 (VISION's re-score of the program's only-ever
Tier-W/Tier-A constraint-3 citation) is the only queued item that would
change that. The proposal flags this itself, honestly, at §3 item 6. I
am recording it so the flag survives into LOGBOOK rather than staying in
a declined-items list.

---

*QUANTUM OPTICS, Phase 2, exp-115. No sub-agents, no simulations, no git
state changed. Arithmetic performed in pure python against committed
JSON and source; every figure above is reproducible from the cited
file:line.*
