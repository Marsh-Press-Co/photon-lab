# Phase 5 review — MATERIALS & METAMATERIALS (exp-115, Panel Iteration 92)

*Fresh context. This seat led Iteration 92; this review reads what it
proposed and what survived. Charter: sub-wavelength structure; what could
physically realize the proposed optical behavior; owns the realizability
bound (published / plausible / unobtainium-with-parameters). No git state
changes, no simulations, no sub-agents. Every figure below is produced by
invoking committed data or by arithmetic on figures read from committed
files — none is restated from a document under review without independent
recomputation (R4 second addendum, R4 third addendum).*

---

## 1. Verdict

**PARTIAL.** Tier T1: **N/A** (instrument-fidelity / governance cycle;
`DISCLAIMER_115` declares "T1 escape route: NONE / N/A" and the declaration
is honest — nothing in M9 touches a T1 escape route, a σ(I)/σ(x,t)
mechanism, or constraint 3, and the sidecar says so inside the quotable
bound itself).

The seven-cycle debt is **substantially but not fully discharged**. The
bound exists, is quotable, is caveat-gated, survives its own reproduction
arithmetic, and is a genuine advance on seven deferrals — OV-2 (decline the
eighth deferral) was the right call and is vindicated: a corrected bound
did beat another deferral. But the artifact as it now stands in
`result_text` **does not say exactly what the evidence certifies**, in
three independent, separately-fixable ways, all zero-FDTD:

1. its per-bin figures are **not** the maximum its own already-committed
   instrument records (understated 3.4× at r=156), and the stated *reason*
   for restricting to margin=32 does not reproduce against the channel the
   headline actually quotes (Finding 2);
2. it quotes only the **tail max** of the per-bin distribution, realized at
   the lowest-SNR resolved bins, and omits the median — which is stable to
   1.7× across all twelve (r, margin) cells and agrees with the withdrawn
   peak-normalized figure to within 1.6× (Finding 3);
3. the observer-return face it warns about is **entirely unresolved at ten
   of twelve (r, margin) cells** — the effect there is UNMEASURED, not
   bounded at ~5% (Finding 4).

And the realizability tier's **forward conditional is physically wrong**
under exp-061's own definition of the MP-5 thickness multiple (Finding 5) —
a MATERIALS-charter error, in this seat's own sidecar, that five review
layers passed because every one of them corrected the *exponent* and none
re-derived what MP-5's multiple actually holds fixed.

None of this reverses the cycle's headline conclusion (the aggregate
~10⁻⁴ backing-insensitivity statement stands, verified exactly), and none
of it is Checkpoint-4-grade on my reading. All of it is repairable in one
zero-FDTD re-issue, which is my Rank-1 direction.

---

## 2. Findings

### F1 — The reproduction gate ran, passed 11/11, and is genuine on 9 of its 11 checks; but it is not a HALT, and two checks cannot fail

Re-derived from `analyze115.py` and `run115.py:605-890`.

**Which asserts ran.** `analyze115.py` contains exactly four `assert`
statements: two R29 module-identity asserts (`analyze115.py:81`, `:83`) and
the two R23-First-Addendum disclaimer asserts (`:259` predictions-side,
`:277` result-side). The M9 sidecar is invoked at `analyze115.py:192` as a
plain call; **it carries no assert and no `SystemExit`**. Its `gate()`
helper (`run115.py:620-625`) appends a record and returns a boolean;
`all_ok`/`status` are computed at `run115.py:816-818` and the *only*
consequence of a failure is that `build_m9_bound_text()` returns the
"WITHHELD" string (`run115.py:898-900`). Every other sidecar sub-dict —
`c_physics`, `a_aggregate_deltas`, `b_floor`, `d_per_bin`, `d_scope`,
`perturbation`, `e_tier` — is returned and persisted **regardless of
status**. `c_physics["withheld"]` is a flag on the dict, not a withholding
of it, and it is keyed on only two of the eleven checks (`repro_cpl20 and
repro_cpl25`, `run115.py:818`).

So `DISCLAIMER_115`'s sentence "any mismatch HALTs it and it is reported
NOT-REPRODUCED rather than published" (`run115.py:961-962`, reproduced
verbatim in `results.json["result_text"]`) is **stronger than the code**.
What the code does is withhold the *headline sentence* while publishing
every number the headline is built from. That is a defensible design; it is
not what the disclaimer says. This is R18's exact shape — a check's
documented scope vs. its actual source — on the one sentence M9 offers as
its whole falsifiable content (RT-15).

**Discriminating power, check by check.** Nine of eleven can genuinely
fail: the two `tau_true` recomputations against `TAU_TRUE_FILED` (bar 1e-2,
achieved 8.13×10⁻⁷), the family bit-identity, and the six checks that read
`exp-108/110/112/114`'s committed `results.json`. **Two cannot fail under
any circumstance**: `gate("loss tangent sigma_max*cpl identical", 0.4*25,
0.5*20)` and `gate("thickness/cpl identical (lambda)", 60.0/25.0,
48.0/20.0)` (`run115.py:640-641`) compare two literal arithmetic
expressions to each other. They are float-arithmetic assertions about
constants written in the same line, not reproductions of anything
committed. They pad the gate's apparent coverage from 9 to 11 and would
report "REPRODUCED" identically whether or not any source file existed. Per
LOGBOOK's own invariant (`lab/ARTIFACTS.md`, quoted in this cycle's own
NOTES.md:227-229), *a silent gate and an absent gate produce identical
observations* — a check that cannot produce a failing reading is the same
object.

**Un-gated load-bearing arithmetic.** The MF-11 channel-count correction
("two independent channels and their exact algebraic sum, not three") rests
on `sum_resid_156`/`sum_resid_234` (`run115.py:667-672`), which are
computed and printed into prose but **never passed through `gate()`**. I
re-derived both from the source ledgers: residual = **−5.6843×10⁻¹⁴**
(r=156) and **0.0000×10⁰** (r=234) — the filed values reproduce exactly.
Likewise `sigma_abs` and `sigma_ext` deltas are gated at neither radius;
only `sigma_scat` is (`run115.py:657-658`), yet the headline's "at most
1.0874e-04" is a max over all six.

*Not a defect in the numbers — every one I checked reproduces. A defect in
the gate's claimed coverage.*

### F2 — "CERTIFIED AT MARGIN=32 ONLY … only the margin-32 array is persisted" does not reproduce against the channel the headline quotes, and the restriction understates the instrument's own worst case by 3.4×

This is the sharpest defect in the frozen artifact.

The scope clause (`run115.py:741-747`, verbatim in `results.json`
`sidecar_m9.d_scope.margin_scope` and in the headline) reads:

> CERTIFIED AT MARGIN=32 ONLY for the tight per-bin figure.
> `experiments/108-.../run.py:244-254` sets `confirm_all_margins` as ONE
> boolean over `MARGINS=(24,32,40,48,57,65)` against
> `ITEM_I_CONFIRM_REL = 0.05` … **only the margin-32 array is persisted.**

I verified `experiments/108-t28-reclassification-angular-pattern-batch/run.py:244-254`
line-by-line: the citation is **accurate for exp-108** — `confirm_all_margins`
is one boolean over the six peak-normalized `relm` arrays vs `0.05`, and
only `rel32` survives into `results.json["tier1"][r]["item_i"]`.

But **the headline's per-bin figures are not from exp-108.** MF-3 moved them
onto exp-110's floor-gated local normalization; `run115.py:713-714` reads
`EXP110_RESULTS[tag]["local_diag"]["32"]`. And exp-110 persists
`local_diag` at **all six margins** — re-derived directly:

```
r156 local_diag margins: ['24','32','40','48','57','65']
r312 local_diag margins: ['24','32','40','48','57','65']
```

`raw_patterns` likewise carries `peccored`/`hollow`/`delta` at all six. So
an exp-108 persistence limitation has been attached, verbatim, to an
exp-110-sourced figure to which it does not apply. **R4-class: a scope claim
that does not reproduce against the source it governs.** Root cause is
compositional, and worth naming precisely for the record: MF-3 (Red Team
docket, `phase2_redteam_audit.md:736ff`) and MF-4 are each individually
correct — MF-3 mandates the exp-110 channel, MF-4 mandates exp-108's margin
scope. Neither fix is wrong; **their composition is.** No seat owned the
join.

The consequence is substantive, not clerical. Recomputed from exp-110's own
committed `results.json`, max floor-gated `local_rel` at every margin:

| r | m=24 | **m=32 (quoted)** | m=40 | m=48 | m=57 | m=65 |
|---|---|---|---|---|---|---|
| 156 | 1.976e-03 | **1.4669e-02** | **4.9648e-02** | 1.842e-02 | 2.059e-02 | 2.274e-02 |
| 312 | 2.509e-02 | **5.2900e-02** | **7.3202e-02** | 3.357e-02 | 3.622e-02 | 3.838e-02 |

The quoted margin-32 value is **not** the maximum on either radius. At
r=156, margin 40 gives `4.9648e-02` — **3.38×** the quoted `1.4669e-02`. At
r=312, margin 40 gives `7.3202e-02` — **1.38×** the quoted `5.2900e-02`.
The headline's "moves … by up to 1.4669e-02 at r=156 and 5.2900e-02 at
r=312" therefore understates its own instrument, on data already on disk at
zero FDTD cost, in the one direction that matters for a fabrication
warning.

**Second R4-class figure in the same clause.** "`ITEM_I_CONFIRM_REL = 0.05`
… **330× looser than the quoted figure**". Recomputed: `0.05 / 1.5266e-04 =
327.5` — correct against the **withdrawn** peak-normalized figure, and only
against that one. Against the figure the headline actually quotes,
`0.05 / 1.4669e-02 = 3.4×` at r=156, and at r=312 `0.05 / 5.2900e-02 =
0.95×` — the "decision bar" is **tighter** than the quoted deviation, not
330× looser. The argument the clause is making (a coarse boolean cannot
certify a tight figure) survives; the number attached to it does not.

**Governance consequence.** `lab/caveat_lint_config.json`'s new entry
`exp115-t28-fabrication-tolerance-bound-certified-resolution` makes
`"certified at margin=32 only"` a required phrase pattern, CI-gated on
`NOTES.md`/`run115.py`/`analyze115.py`. As of this cycle the registry
therefore **compels** every future citing document to repeat a scope
sentence whose stated reason does not reproduce and whose figure is not the
worst case. Correcting the entry is part of the same zero-FDTD re-issue.

*(I ran `lab/caveat_lint.py`: **16 caveats checked, 0 required-site
failures** — MF-14's gating half genuinely works. Note `results.json` is in
neither entry's `required_sites`, and `result_text` currently lives only
there; see F7.)*

### F3 — The bound quotes only the tail maximum; the median is stable to 1.7× across all twelve cells, and the two normalizations agree there

`classify_item_i_local` (`experiments/110-.../run.py:310-362`) defines
`local_rel = |Δ| / |peccored|` **only** where both parent patterns exceed
`K=3 ×` the mirror-pooled median floor. The max over that set is, by
construction, biased toward the bins with the smallest surviving
denominators. Recomputed across all twelve (r, margin) cells:

| r | margin | n_res | median | p90 | max | SNR at max | n > 1e-3 |
|---|---|---|---|---|---|---|---|
| 156 | 24 | 32 | 9.430e-05 | 3.167e-04 | 1.976e-03 | 2.55 | 2 |
| 156 | 32 | 34 | 1.217e-04 | 1.548e-03 | 1.467e-02 | 1.33 | 6 |
| 156 | 40 | 36 | 1.271e-04 | 8.444e-03 | 4.965e-02 | 1.52 | 8 |
| 156 | 48 | 34 | 1.431e-04 | 3.572e-03 | 1.842e-02 | 1.14 | 8 |
| 156 | 57 | 34 | 1.033e-04 | 2.700e-03 | 2.059e-02 | 1.14 | 8 |
| 156 | 65 | 33 | 1.132e-04 | 9.673e-04 | 2.274e-02 | 1.01 | 3 |
| 312 | 24 | 36 | 1.061e-04 | 3.218e-03 | 2.509e-02 | 2.49 | 6 |
| 312 | 32 | 38 | 1.263e-04 | 1.485e-02 | 5.290e-02 | 1.34 | 10 |
| 312 | 40 | 40 | 1.602e-04 | 3.136e-02 | 7.320e-02 | 1.06 | 10 |
| 312 | 48 | 36 | 1.138e-04 | 7.622e-03 | 3.357e-02 | 2.79 | 8 |
| 312 | 57 | 36 | 1.123e-04 | 8.672e-03 | 3.622e-02 | 1.86 | 8 |
| 312 | 65 | 36 | 1.204e-04 | 8.832e-03 | 3.838e-02 | 1.62 | 8 |

Three results follow, none of them in the frozen record:

**(a) The median is the stable quantity.** Median resolved `local_rel`
spans `9.430e-05 → 1.602e-04` over all twelve cells — a **1.70× total
spread** across two radii and six box radii. The withdrawn peak-normalized
figures are `1.4760e-04` (r=156) and `1.5266e-04` (r=312) — both sit inside
that band. So the two normalizations **agree on central tendency to within
1.6×**; the celebrated "99.4× / 346.5×" divergence (which I verified:
`1.4669e-02 / 1.4760e-04 = 99.38`, `5.290e-02 / 1.5266e-04 = 346.5`) is
entirely a **tail** phenomenon, max-vs-max between distributions with very
different tails. The record currently reads as though the local instrument
found an effect two orders larger than the peak-normalized one; it did not —
it found the same central effect plus a floor-adjacent tail the peak
normalization is blind to.

**(b) The tail max is realized at the least trustworthy bins.** The
`SNR at max` column is the peccored bin's own local SNR against the floor
gate: `1.01–2.79`, i.e. the maxima are always among the bins that clear the
`K=3` gate by the narrowest margin. Only 2–10 of 32–40 resolved bins exceed
`1e-3` at all.

**(c) The numerator is nearly constant; the swing is all denominator.**
Absolute `|Δσ_scat|` at the max bin, re-derived from `raw_patterns`:

| cell | bin | peccored | `\|Δ\|` (absolute) | local_rel |
|---|---|---|---|---|
| r156 m32 | +123.75° | 1.5001e-03 | **2.2005e-05** | 1.4669e-02 |
| r156 m40 | −131.25° | 4.2729e-04 | **2.1214e-05** | 4.9648e-02 |
| r312 m32 | +138.75° | 4.5259e-04 | **2.3942e-05** | 5.2900e-02 |
| r312 m40 | +146.25° | 2.4968e-04 | **1.8277e-05** | 7.3202e-02 |

`|Δ|` varies by 1.31× across a set whose `local_rel` varies by 5.0×. **The
core swap moves the backward-hemisphere per-bin σ_scat by a near-constant
≈2×10⁻⁵ absolute, independent of radius and box margin; the "1.5%–7.3%"
figures are that constant absolute change divided by whichever backward bin
happens to be smallest at the chosen box radius.** That is the physical
statement, and it is a strictly better fabrication bound than the one
filed — it tells a process engineer the invariant, not an artifact of the
measurement box.

### F4 — The observer-return face is entirely unresolved at ten of twelve cells: the constraint-2-relevant effect is UNMEASURED, not bounded at ~5%

First, the angular convention, re-derived four independent ways because I
nearly filed a false correction on it (R4 addendum: a sign/convention
correction must be re-derived by an external method before it is trusted).

`lab/sections.py`'s `angular_scattered_pattern` docstring states, twice
(`:209-210`, `:223-224`): *"0 deg = -x (toward the source, 'backward'),
+-180 deg = +x (downstream, 'forward')."* **That docstring is backwards.**
The code's own inline comments two dozen lines below say the opposite
(`:246` `# x1 face (mostly forward)` → `arctan2(dy, x1-bcx)` with
`x1-bcx > 0` → θ ≈ 0; `:247` `# x0 face (mostly backward)` → θ ≈ ±180),
and three independent physical checks confirm the code, not the docstring:

1. **Geometry.** `SRC_X0 = 64`, `CX0 = 252` (`experiments/110-.../run.py:53`)
   and `behind_x_lo = CX + R_COAT + 27` (`:110`) — the source is at low x,
   the beam-behind box downstream at high x. Propagation is **+x**.
2. **The shadow lobe.** Re-derived from exp-110's `raw_patterns['32']
   ['peccored']` at r=156: the `|θ| < 45°` sector (x1 face) carries
   **+275.74** of the **+280.54** total σ_scat — **98.3%**. That is the
   forward shadow lobe. The `|θ| > 135°` sector (x0 face) carries
   **+9.551×10⁻⁴**, i.e. **3.4×10⁻⁶ of total** — consistent to the order
   with LOGBOOK ESTABLISHED's "backward spray ≤ 10⁻⁴ of extinction"
   (exp-002). Under the docstring's convention the absorber would be
   emitting 98% of its scattered power straight back at the observer.
3. **exp-112's own count.** The sidecar's "0 of 12 backscatter bins
   resolved" reproduces **exactly** — and the set it reproduces on is the
   twelve bins with `|θ| > 135°`, confirming that those, not the forward
   ones, are what this program calls backscatter.

So: **the sidecar's "±138.75° … INSIDE the observer-return hemisphere" claim
is CORRECT** (x0 face, source side), and `lab/sections.py:209-210,223-224`
carries a **live R18-class documented-scope-vs-code defect in shared `lab/`
machinery** reused across ~15 T28 cycles. It is inert today only because
every consumer has read the code rather than the docstring. It is precisely
the trap R22 exists to prevent, and it should be corrected in `lab/`.

**Now the substantive finding.** Restricting to the source-facing x0 face
(`|θ| > 135°`, the twelve bins that actually face the observer), across all
twelve cells:

| r | m=24 | m=32 | m=40 | m=48 | m=57 | m=65 |
|---|---|---|---|---|---|---|
| 156 | 0/12 | **0/12** | 0/12 | 0/12 | 0/12 | 0/12 |
| 312 | 0/12 | **2/12** | 4/12 | 0/12 | 0/12 | 0/12 |

**Ten of twelve (r, margin) cells resolve ZERO of the twelve
observer-facing bins.** The only two that resolve any are exactly the two
the headline quotes (r=312, margins 32 and 40), at 2/12 and 4/12. At r=156
the headline's own max bin (±123.75°) is not on the observer-facing face at
all — it is a side-scatter bin on the y-faces.

The headline's fabrication-consequence sentence — *"it does NOT license
varying the backing without re-measuring the per-bin angular channel in the
observer-return hemisphere, **which moves by ~5 percent there**"* — is
therefore built on a 2-of-12-bin sample at one box radius out of six. The
warning is **right**, but for close to the opposite reason it gives: the
correct statement is not "the observer-return channel moves by ~5%" but
**"at ten of twelve box radii the observer-facing face lies entirely below
this instrument's floor gate — the core-swap effect there is UNMEASURED,
not bounded."** That is the R13/R30 discipline this program already
codified (a max over a resolved subset says nothing about the unresolved
set), applied to a case where the unresolved set *is* the constraint-2 set.

**And the units are wrong for the constraint.** PANEL.md's Metrics table
scores constraint 2 as *"Backscatter to observer vs **camera floor**"* —
an absolute comparison, via `emit.observer_record` (stage 6). The sidecar
reports a **relative** per-bin movement of a face carrying 3.4×10⁻⁶ of
total σ_scat, and never compares the absolute ≈2×10⁻⁵ change to any floor.
A 5% change in a channel carrying a millionth of the cross-section may or
may not be a constraint-2 exposure; nothing in the record answers that.
This is the single largest open question my seat's bound leaves behind, and
it is my Rank-2 direction.

### F5 — The MP-5 forward conditional does NOT hold with the corrected exp(−τ) scaling: MP-5 holds τ_true FIXED by construction, so the bound is invariant, not strengthened

`results.json` `sidecar_m9.e_tier.forward_conditional` (`run115.py:876-881`):

> IF a future cycle re-specs this article at exp-061's own MP-5-plausible
> thickness (230-730x of 1.44 um), the core/backing freedom **survives and
> strengthens** — the bound scales as exp(-tau_true) … and **tau_true grows
> with thickness**.

Read against exp-061's own resolution of MP-5
(`experiments/061-absorptivity-mechanism-literature-check/NOTES.md:440-449`),
verbatim:

> **MP-5 (achievable at some thickness): PARTIAL.** … Magnitude undershot:
> visible-band figures need **~230–730×** the 1.44µm thickness … **to reach
> τ_true**

MP-5's multiple **is defined as the thickness at which a real, lower-α
CNT-forest-class coating reaches the SAME τ_true ≈ 8.2588.** τ_true is the
target that is held fixed; the thickness is what varies to hit it. The
sidecar's premise is the opposite one — thickness growing at fixed α —
which is only available if α stays at `5.74×10⁴ cm⁻¹`, the very value
exp-061's MP-1 found nothing in the class approaches (`NOTES.md:375-380`,
best in-class visible-band figure `2.28×10³ cm⁻¹`, short by **>25×**).

Therefore, under MP-5's own scenario:

`2·exp(−τ_true) = 5.1793×10⁻⁴` — **unchanged**, at 230× and at 730× alike.

The bound **survives**; it does not **strengthen**. Nothing about the
core/backing freedom improves under the re-spec. (Under the counterfactual
the sidecar actually describes — 230× thickness at the unobtainable α —
τ would be `8.2588 × 230 ≈ 1.90×10³` and the bound `~10⁻⁸²⁵`, a figure with
no physical referent.)

This defect **originated in Phase 1** (`phase1_proposal.md:524-529`, with
`exp(−2·τ_true)`) and **survived every review layer**. MF-1's own text
(`phase2_redteam_audit.md`, docket) reads *"Correct M9(e)'s forward scaling
to `exp(−τ_true)` (still exponential, half the exponent)"* — the mandate
patched the exponent and preserved the conflation. EM (`phase2_critique_em.md:378-379`)
caught only the factor-of-two. THERMODYNAMICS (`phase2_critique_thermodynamics.md:608-622`)
found the missing thermal cost and explicitly *accepted* the optical
premise: *"Thickening 230–730× improves the optical backing-independence
and simultaneously drives the IR detectability margin to 1.35×–3.79×."*
Nobody re-derived what the multiple holds fixed.

**The consequence is not cosmetic — it inverts MF-15's counterweight from a
trade-off into a strict loss.** MF-15's `thermal_counterweight.reading`
(`run115.py:810-814`) frames it as a balance: more backing-independence
bought at the cost of thermal margin. Corrected, under MP-5 the article
gets:

- **zero** additional backing freedom (bound invariant at 5.1793×10⁻⁴),
- thermal margin against NETD-lo collapsing **3.79× → 1.35×** (verified
  against `experiments/061-.../NOTES.md:235-240`: 230× → 331.2 µm →
  ΔT_ss 5.277×10⁻³ K, margin 3.79×; 730× → 1051.2 µm → 1.4774×10⁻² K,
  margin 1.35×; NETD-lo 0.020 K; and `230×1.44 = 331.2`, `730×1.44 =
  1051.2` both reproduce),
- a physically **larger black silhouette** — constraint 3's own failure
  mode.

That is strictly worse on every axis. As the seat that owns the
realizability bound, I record it that way: **the MP-5 re-spec buys nothing
optically and costs on two independent axes.** It should not be carried
forward as an attractive direction.

### F6 — Three R4-class arithmetic/citation defects, all non-outcome-reversing

**(a) The "even allowing a 4× standing-wave enhancement" clause is false as
written.** `run115.py:786-800`, persisted verbatim in `sidecar_m9.perturbation.closure`:

> their contribution to a relative delta is ~3.15e-08 — **180× below** the
> SMALLEST of the six measured aggregate deltas (5.666e-06) and **3455×
> below** the largest (1.087e-04), **even allowing a 4× standing-wave
> enhancement** at the PEC face.

Re-derived: `overlap_bound = (12/98740) × exp(−τ_true) = 3.1472×10⁻⁸`
(reproduces `closure_bound` exactly); `5.666e-06 / 3.1472e-08 = 180.0` and
`1.087e-04 / 3.1472e-08 = 3454.9` — **both computed WITHOUT the 4×**. With
the 4× allowed (`closure_bound_with_4x_standing_wave = 1.2589×10⁻⁷`, itself
persisted correctly): **45.0×** and **863.7×**. The sentence asserts the
ratios hold under the enhancement; they do not. Qualitative conclusion
(RULED OUT) unchanged at 45×. This is inherited from RT-16's own wording
(`phase2_redteam_audit.md:449-465`) — the cycle correctly caught and
disclosed RT-16's "five orders" error (NOTES.md:200-210, honest R4 forward
correction, `log10(180.04) = 2.26`, `log10(3454.9) = 3.54` both verified)
but carried the "even allowing" clause forward onto the corrected numbers.

**(b) The closure bound is computed at the flattering radius.**
`overlap_bound` uses `overlap234/shell234 = 1.2153×10⁻⁴` (`run115.py:771`),
the smaller of the two overlap fractions; at r=156 the fraction is
`1.9281×10⁻⁴`, giving `4.9932×10⁻⁸` and a smallest-delta ratio of **113.5×**
(28.4× with the 4×). The bound is then compared against deltas drawn from
**both** radii. Still ruled out; the record should say which radius the
bound is computed at.

**(c) `4.47×` vs `4.46×` inside one document.** `DISCLAIMER_115`
(`run115.py:965`) and `sidecar_m9.b_floor.differential_floor.reading`
(`run115.py:706-709`) both hand-type **4.47×**; the adjacent computed field
`mean_over_std = 4.464601791167039` prints as **4.46×** in the headline
(`%.2f`). 4.47 is exp-108's *filed* figure (`4.4653`, the gate's
`expected`); 4.4646 is this cycle's recomputation. Both defensible, but the
same document states both without reconciling them. R4: a hand-typed figure
sitting beside the committed function's own different output.

**(d) An R9-shape unit slip, one line.** `a_aggregate_deltas.channel_count_correction`
says *"At r=156 the two genuine channels PARTIALLY CANCEL, so the derived
sigma_ext delta is about half the largest real one."* In **absolute** units
that is right (`1.503e-02 / 2.931e-02 = 0.513`); in the **relative**
normalization every other number in that dict uses, it is a **quarter**
(`2.147e-05 / 8.359e-05 = 0.257`). One sentence, two normalizations.

*Everything else I checked reproduces exactly*: the six aggregate deltas
and both channel-sum residuals (F1); `wrong_by_factor = exp(8.2588) =
3861.5`; the λ rows and "2.05× worse at 750 nm than 450 nm"
(`exp(8.629338 − 7.909063) = 2.055`); `70–350×`
(`100/1.44 = 69.4`, `500/1.44 = 347.2`); `1.440 µm = 2.40 λ` and
`60/25 = 48/20 = 2.40`; `99.4× / 346.5×`; `34/48` and `38/48`; exp-112's
`0 of 12`. **R20 tally on this document: 3 R4-class instances (a), (c), (d)
surviving into the frozen artifact** — at the threshold, not over it, and
all three are non-load-bearing. I do **not** read R20 as firing: R20's
founding standard requires three defects *each caught only at Phase 5*
whose density is the finding; here (a) is an inherited docket phrase the
cycle partially self-corrected in the same document, and (c)/(d) are
internal normalization slips, not citations that fail against an external
source. I flag the tally so Red Team can rule independently.

### F7 — Two disclosure/persistence gaps, both closable before the cycle closes

**(a) NOTES.md's Result section is still `(pending)`** (`NOTES.md:619-621`).
`results.json["result_text"]` labels the M9 headline *"R21: stated here,
not merely persisted"* — but "here" is currently `results.json`, not the
Result prose R21's text names. R21's own wording forbids leaving a
sidecar's headline finding "merely persisted to `results.json` or left in
Setup/the frozen Predictions table." The headline **must** land verbatim in
`NOTES.md § Phase 4 — Results` before close, or the R21 discharge is only
half made. (`NOTES.md` *is* in both caveat entries' `required_sites`, so
once it lands, the gate covers it. `results.json` is in **neither** — worth
adding.)

**(b) MF-15's own substance is persisted but never narrated.** The thermal
counterweight (`3.79× → 1.35×`) and the forward conditional live only in
`sidecar_m9.e_tier` and in NOTES.md's **Phase-3 disposition table**
(`NOTES.md:119`) — never in `result_text`, whose only sidecar content is
the `headline` string, which contains neither. That is R21's named shape
("left in Setup / the frozen Predictions table") one level down, on a
sub-field rather than the sidecar's own headline. I flag it as a **candidate**
third occurrence for Red Team to rule on rather than declaring R21's
forward-elevating clause fired: the sidecar's *own* headline is narrated,
which is R21's literal target. And I note without irony that the omission
was **protective** this cycle — F5's wrong claim never reached the prose a
future cycle would quote.

### F8 — The λ-dependence claim rests on an undisclosed non-dispersive-σ idealization

`c_physics.wavelength_rows` and its note state *"Backing freedom is weakest
in the red (2.05x worse at 750 nm than 450 nm)"*. That row set is generated
(`run115.py:649-652`) by holding `sigma_max = 0.4` fixed in grid units and
scaling `cpl` with λ (18.75 / 25 / 31.25). Since `n = sqrt(1 + i·σ·cpl/2π)`
and `cpl ∝ λ`, holding σ fixed in these units is exactly the statement that
the coating's **physical conductivity is frequency-independent** — a DC-like
Drude-free conductor. Real ultra-black coatings in the class exp-061
benchmarks against are not that; their blackness is dominated by structural
light-trapping, which exp-061's own MP-1 record explicitly says (*"Real
blackness is plausibly dominated by structural … not a
reflectance-vs-thickness curve reducible to a scalar α at all"*).
Idealization 9 (`NOTES.md:433-440`) discloses that the figure is *measured*
only at 600 nm — good — but not that the 450/750 nm rows assume a
non-dispersive σ, and the direction of the wavelength trend is not robust
to that assumption. One sentence, zero cost, and it belongs in the
Idealizations list where a MATERIALS reader will look for it.

### F9 — What is genuinely, unambiguously PAID

Stated plainly, because the debt was real and most of it is now discharged:

- The bound **exists**, in one quotable sentence, produced by committed
  code (`build_m9_bound_text`, `run115.py:893-943`), and it appears in
  `results.json["result_text"]` **verbatim** — I verified by exact string
  containment: `sidecar_m9["headline"] in result_text` → **True**.
- Its aggregate half is **exactly right and fully verified**: the six
  deltas, the symmetric-mean normalization, the two-channels-plus-exact-sum
  correction, both residuals, the differential-floor resolution at 4.46×/
  11.70×, the withdrawal of the scene-independent `σ_ext_cross − σ_ext`
  "floor" (bit-identical between the two differenced scenes: `0.0` exactly
  at r=234, `2.27×10⁻¹³` at r=156 — I reproduced both).
- The corrected physics (MF-1) is right and is a real prediction: measured
  deltas sit **2.38×–45.70×** below `exp(−τ_true)` and **4.76×–91.41×**
  below `2·exp(−τ_true)`, i.e. the bound is respected by every channel.
  (One precision note: the headline's blanket *"the SAME ORDER as the
  measured aggregate deltas"* holds for four of six channels within a
  decade and fails for two — r=156 σ_ext at 12.06× and r=234 σ_abs at
  45.70× below the scale. "Bracketed from above by 2.4×–46×" is the exact
  statement.)
- MF-4's hard scope clauses (near-to-mid-field box ledger not far-field;
  channel/resolution confound; r=234 aggregate-only), the constraint-3
  failure, the realizability tier and the T18 evidentiary tier are all
  **inside** the quotable sentence, which is what makes it safe to quote.
- The tier itself — **UNOBTANIUM-WITH-PARAMETERS, thickness-driven,
  70–350× gap, inherited from exp-061 at WebSearch-snippet tier (T18)** —
  is stated **honestly** and verified against exp-061's MP-2/MP-4 CONFIRMED
  record. `moved_by_this_finding = False` is correct: nothing in a
  core/backing tolerance bound bears on a thickness gap.

**The one-sentence bound a future cycle may quote** (my seat's, corrected
for F2–F5; offered for the re-issue, and I recommend the registry's
required phrase be updated to match it):

> For the `graded_black_shell` article at `τ_shell = 24`, `ε_r ≡ 1`,
> λ = 600 nm, plane-wave normal incidence, 2D TM, measured on this bench's
> near-to-mid-field box ledger at its own measurement geometry: replacing
> the entire core/backing from vacuum to a perfect electric conductor moves
> the aggregate cross-section channels by at most **1.09×10⁻⁴** relative
> (σ_scat and σ_abs, opposite in sign, plus their exact algebraic sum
> σ_ext — two channels, not three), and moves the **typical** resolved
> angular bin by **≈1.2×10⁻⁴** (median floor-gated local normalization;
> 9.4×10⁻⁵–1.6×10⁻⁴ across **all six** box radii at r=156 and r=312, within
> 1.6× of the peak-normalized figure), with a tail of 2–10 low-SNR bins in
> the backward hemisphere moving by up to **7.3×10⁻²** — a near-constant
> **|Δσ_scat| ≈ 2×10⁻⁵ absolute** divided by whichever backward bin is
> smallest at the chosen box radius, not a growing physical effect; **the
> source-facing face is entirely below the floor gate at ten of twelve
> (r, margin) cells, so the observer-return channel is UNMEASURED there,
> not bounded**, and has never been scored in the absolute units against
> the camera floor that PANEL.md measures constraint 2 with. Per-bin
> evidence exists at cpl=20 only and aggregate evidence at cpl=25 only, so
> **channel and resolution are fully confounded**; r=234 contributes
> aggregate channels only. Fabrication consequence, at that scope: a
> process implementing this design need not control the core/backing
> material to better than the **~10⁻⁴ aggregate level**, and this does not
> license varying the backing without measuring the backward-hemisphere
> channel against an absolute floor. The optical function is carried
> entirely by a **1.440 µm (2.40 λ)** graded-σ coating whose physical
> thickness is invariant across r = 156/234/312 and cpl = 20/25. **This
> article FAILS CONSTRAINT 3 BY CONSTRUCTION** and this bound is not
> constraint-3 progress. **REALIZABILITY TIER: UNOBTANIUM-WITH-PARAMETERS**,
> inherited unchanged from exp-061, driven by the 70–350× thickness gap
> (1.44 µm asked of a class that runs 100–500 µm), every literature figure
> behind it WebSearch-snippet synthesis, not primary-source-verified (T18) —
> and **INVARIANT, not improved, under exp-061's own MP-5 re-spec**, which
> by its own definition preserves `τ_true` rather than growing it, so
> thickening buys no backing freedom while costing thermal margin
> (3.79× → 1.35× vs NETD-lo) and a physically larger black silhouette.

---

## 3. Defects (R-numbers)

| # | Defect | Rule | Load-bearing? |
|---|---|---|---|
| D1 | `DISCLAIMER_115`/`result_text` claim the M9 gate "HALTs"; the code halts nothing — it withholds the headline string and publishes every underlying field. `c_physics["withheld"]` is keyed on 2 of 11 checks. | **R18** (documented scope vs. actual code) | No — all 11 passed |
| D2 | Two of eleven "reproduction checks" (`0.4*25` vs `0.5*20`; `60/25` vs `48/20`) compare literals written on the same line and cannot fail. | **R30-family** (an instrument with no demonstrated failing branch) | No |
| D3 | `sigma_abs`/`sigma_ext` deltas and both channel-sum residuals — the arithmetic MF-11's correction rests on — are computed and quoted in prose but never gated. | **R19-adjacent** (a cited invariant not code-enforced) | No — all reproduce |
| D4 | "only the margin-32 array is persisted" is true of exp-108 and **false of exp-110**, the channel the headline actually quotes (all six margins persisted). | **R4** | **Yes** — see D5 |
| D5 | The quoted per-bin figures are not the maxima on their own committed instrument: margin 40 gives **3.38×** more at r=156 and **1.38×** more at r=312. | **R4 / R15-adjacent** (a boundary trusted at one sampled condition) | **Yes** — headline understates |
| D6 | "330× looser than the quoted figure" reproduces only against the **withdrawn** peak-normalized figure; against the quoted local figure it is 3.4× (r=156) and **0.95×** — tighter — at r=312. | **R4** | No (argument survives) |
| D7 | The bound quotes only the tail max; median (1.70× stable across all 12 cells) and the SNR of the realizing bin (1.01–2.79) are absent, so the 99×/346× normalization gap is presented as a physical finding rather than a tail effect. | **R14** (single-point distrust on a subtractive-cancellation ratio) | **Yes** — misleads on magnitude |
| D8 | "moves by ~5 percent there [the observer-return hemisphere]" rests on 2 of 12 bins at one of six box radii; the source-facing face is **entirely unresolved at 10 of 12 cells**, and the change is never expressed in the absolute units PANEL.md scores constraint 2 in. | **R13/R30** (unresolved set excluded from the claim) + **R9** (units) | **Yes** — the honest reading is UNMEASURED |
| D9 | MP-5 forward conditional: "τ_true grows with thickness … survives and **strengthens**". MP-5 holds τ_true **fixed** by construction; the bound is invariant. Inverts MF-15's counterweight from a trade into a strict loss. | **R4** (a claim that does not reproduce from its cited source) + **R9** (what the multiple holds fixed) | **Yes** for the realizability record; not for the scored bound |
| D10 | "180×/3455× below … **even allowing** a 4× standing-wave enhancement" — the ratios are computed without the 4×; with it, 45.0×/863.7×. | **R4** | No (conclusion holds at 45×) |
| D11 | Closure bound computed at r=234's overlap fraction (the flattering one) and compared against deltas from both radii; at r=156 it is 4.99×10⁻⁸ (113.5×, 28.4× with the 4×). | **R4-adjacent** | No |
| D12 | `4.47×` hand-typed in `DISCLAIMER_115` and `b_floor…reading` beside the committed function's own `4.4646` (`4.46×` in the headline). | **R4** | No |
| D13 | "the derived σ_ext delta is about half the largest real one" — true in absolute units, a quarter in the relative units the surrounding dict uses. | **R9** | No |
| D14 | **`lab/sections.py:209-210, 223-224`** state the angular convention **exactly backwards** (0° claimed = toward source; the code, the geometry, the 98.3% forward shadow lobe and exp-112's own 0/12 backscatter count all say 0° = downstream), contradicting the same function's inline comments at `:246-247`. Shared machinery, ~15 T28 cycles. | **R18** (live, in `lab/`) | Not yet — every consumer read the code |
| D15 | `NOTES.md § Phase 4 — Results` is still `(pending)`; the R21 discharge currently rests on `results.json`, which is in neither caveat entry's `required_sites`. | **R21** | Closable before cycle close |
| D16 | MF-15's counterweight and forward conditional are persisted + in the Phase-3 disposition table, never in Result prose. Candidate third occurrence of R21's forward-elevating shape — flagged for Red Team, not declared fired. | **R21** (sub-field) | No (protective this cycle) |
| D17 | The 450/750 nm rows assume a **frequency-independent σ**; the "weakest in the red" conclusion is stated as physics without that idealization disclosed. | Idealization-disclosure (R4-adjacent) | No |

**Checkpoint criterion 4:** I do **not** find it fires on this cycle from my
charter. D4/D5/D7/D8/D9 are first instances of their specific shapes, all
caught blind within this cycle's own review layers before LOGBOOK, all
zero-cost to repair, and none reverses a scored verdict — matching the
founding-instance precedent every rule R16–R33 sets. **R20 tally: 3** (D10,
D12, D13), at the density bar but not over it on my reading (see F6). D14
is a `lab/` defect this cycle inherited, not created.

---

## 4. Ranked top-3 candidate directions

*Iteration 93 item 1 is fixed by the Director's D2 ruling (VISION's
constraint-3 re-score through the modernized `lab/ambient.py`); these are
offered for **Iteration 93 items 2–3** and **Iteration 94 item 1**. All
three are MATERIALS-charter items.*

### Rank 1 — Iteration 93, item 2: the zero-FDTD re-issue of the fabrication-tolerance bound at full scope

**Cost: zero FDTD, zero grid-steps, zero new data.** Everything needed is
already committed.

1. Recompute the per-bin channel at **all six** margins from exp-110's own
   `local_diag` (D4/D5), and report **median + p90 + max + SNR-at-max +
   absolute |Δ|** rather than max alone (D7). Strike "only the margin-32
   array is persisted"; correct "330× looser" (D6).
2. Report the observer-facing face as **UNMEASURED at 10/12 cells** rather
   than "moves by ~5%" (D8).
3. Correct the MP-5 forward conditional to **invariant, not strengthened**,
   and restate MF-15's counterweight as a strict loss on two axes (D9).
4. Fix D10–D13 and disclose D17.
5. Update `lab/caveat_lint_config.json`'s
   `exp115-…-certified-resolution` required phrase so the registry stops
   compelling the superseded scope sentence; add `results.json` to
   `required_sites`.
6. Land the corrected headline verbatim in `NOTES.md § Phase 4 — Results`
   (D15).
7. Correct `lab/sections.py:209-210, 223-224` (D14) — the only `lab/` touch,
   docstring-only, requiring a trust-suite re-run per CLAUDE.md.

**Why first:** it is the cheapest item in the queue and the only one that
repairs a **machine-enforced** caveat currently locking a partly-wrong
scope claim into every future citing document. It also discharges, in the
same motion, the debt this seat only half-paid — and R25's own lesson is
that a fix disclosed in prose and not given its own numbered queue line is
the fix that gets dropped. This is that numbered line.

### Rank 2 — Iteration 93, item 3: score the observer-return channel in absolute units against the camera floor (`emit.observer_record`, stage 6)

Run the hollow/peccored pair at r=156, cpl=20 with a stage-6
`observer_record` capture and express the core-swap effect as an **absolute
backward flux change vs. the empty-room camera floor** — the quantity
PANEL.md's Metrics table actually scores constraint 2 with, and the one my
bound conspicuously does not supply (D8). Two `Sim.run()` calls at the
cheapest geometry; well inside any cost gate.

**Why second, and why it pairs with item 1:** it is the *only* way to learn
whether "does not license varying the backing" is a real fabrication
constraint or a rounding artifact — the observer-facing face carries
**3.4×10⁻⁶ of total σ_scat**, so a 5% relative movement there may be
comfortably below any camera floor. It also re-warms a constraint-2
instrument that, like `lab/ambient.py`, has gone cold on the T28
sub-thread; running it in the same iteration as VISION's constraint-3
re-score is the natural pairing, and it directly serves the Checkpoint-4
discharge the Director has already ruled (D1/D2). Pre-register the floor
comparison and its units **before** the run (R9: confirm commensurability
before the comparison is scored — this is exactly the trap that produced
R9's founding instance).

### Rank 3 — Iteration 94, item 1: de-confound channel from resolution — the per-bin angular channel at cpl=25 (or the aggregate channels at cpl=20), one radius

MF-4's channel/resolution confound is the largest surviving scope
limitation on the bound and is stated, correctly, inside the quotable
sentence: per-bin evidence exists at cpl=20 only, aggregate at cpl=25 only,
so *"two grid resolutions" is not a resolution check on any channel*. One
r=156 pair at the complementary `cpl` converts that from a confound into a
real R3 resolution check on a single channel.

**Why third, not first:** it costs real FDTD, and it should follow items 1–2
so that the re-issued bound defines exactly **which** figure the new
resolution point must reproduce — the median, per F3, not the tail max,
which F3 shows is a floor-gate artifact that would not be expected to
reproduce across resolutions and would generate a spurious R15-shaped
"reversal." Running this before the re-issue would very likely manufacture
a false resolution-instability finding. R15's own founding instance is the
cautionary precedent.

*Explicitly **not** recommended, and I ask that it be recorded as such:* the
MP-5 thickness re-spec as a forward direction. Per F5/D9 it buys **no**
backing freedom (τ_true invariant by MP-5's own construction), costs
thermal margin 3.79× → 1.35×, and enlarges a silhouette that already fails
constraint 3 by construction. The record should stop describing it as an
attractive conditional.

---

## 5. Summary (≤150 words)

**PARTIAL; T1 N/A.** MATERIALS' seven-cycle debt is written, quotable, and
in `result_text` verbatim — a real advance, and OV-2 (decline an eighth
deferral) was right. The aggregate half is exactly correct and fully
reproduced. But the bound overstates its own scope discipline and
understates its own effect. Its per-bin figures are not the maxima its
committed instrument records (3.4× low at r=156); the stated reason for the
margin-32 restriction is exp-108's, not exp-110's, and is false for the
channel quoted; only the tail max is reported, while the median is stable to
1.7× across all twelve cells and agrees with the withdrawn peak-normalized
figure; and the observer-facing face is entirely unresolved at ten of twelve
cells, so its "~5%" movement is UNMEASURED, not bounded. The realizability
tier is honest, but its MP-5 forward conditional is wrong: MP-5 holds
`τ_true` fixed, so thickening buys nothing and costs thermal margin. One
zero-FDTD re-issue fixes all of it.
