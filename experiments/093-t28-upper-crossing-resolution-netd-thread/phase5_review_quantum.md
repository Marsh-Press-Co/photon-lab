# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 70 · exp-093

*Fresh sub-agent, blind to all other seats' current-cycle Phase-5 reviews.
Charter: non-classical absorption, state-dependent/coherent interactions;
mechanisms enter the bench only as effective classical parameters
(σ(I), σ(x,t), dispersive ε(ω), gain) — by this sub-thread's own precedent
(R13/R14, exp-087/088), this seat's duty also runs to construction-level
statistical/algebraic hazard-spotting on ratio classifiers and calibration
boundaries. Every disputed number below was recomputed independently in
this session, from raw `results.json`/`run.py`/`run_output.txt` primitives
— not taken from NOTES.md's prose, and not by re-invoking the committed
functions where a from-scratch reimplementation was feasible.*

## 1. Independent recomputation of item 2 — CONFIRMED, from scratch

Reimplemented `auc()` (raw Mann-Whitney concordance) and `firth_logistic`
(Newton-Raphson with Firth's `h·(0.5−π)` bias-correction term) **from
scratch**, no import of any `experiments/090-.../run.py` code, against
`results.json::item2.base_table`'s own 8 `(margin, y)` pairs:

```
pos = {2.3005, 4.1083}  (40.0°, 40.2°)
neg = {5.4287, 9.1877, 11.2790, 15.6474, 20.6530, 23.1785}  (41.4°, 39.8°, 37.2°, 39.6°, 39.4°, 39.2°)

auc(pos, neg)   = 0.0000   # "higher margin predicts Y=1" — the wrong question
auc(-pos, -neg) = 1.0000   # "lower margin predicts Y=1" — exp-090's own convention

zone: max(pos)=4.108338359719357, min(neg)=5.428698393194279  → [4.1083, 5.4287]

Firth (scratch Newton–Raphson, own implementation): β = [3.76502935, -5.60697510],
  13 iterations, converged=True, m50 = 4.693429438742365
```

This is **bit-exact** (to the printed precision) with `results.json`'s own
`item2.base_zone` (`auc=1.0`, `zone=[4.1083..., 5.4287...]`,
`firth_beta=[3.7650293528574967, -5.606975100009267]`,
`firth_m50=4.693429438459299`) and with the headline's claim
(`auc=1.0000`, zone `[4.1083,5.4287]`). **Verified independently, a fourth
time overall** (after QUANTUM's own Phase-2 critique, Red Team's Phase-2
RT-1, and the Director's Phase-3 §0 third derivation) — the corrected
convention was actually applied in the real Phase-4 run, not merely
promised in NOTES.md. The `run.py::compute_zone()` docstring itself states
it "Uses exp-090's own `auc(-pos_m,-neg_m)` calling convention (RT-1
fix)" — confirmed true of the executed code, not just the comment.

**Also independently confirmed**: naive MLE divergence (unpenalized
logistic on this near-separable 8-point sample is expected to diverge;
Firth's penalty is what makes `m50` well-defined) — consistent with
`naive_mle_diverges=True` and the `[78.04, -115.66]` blown-up naive `β` in
`results.json`.

**Item 2 verdict: CONCUR.** No residual concern on this specific figure.

## 2. Item 1's SINGLE-NULL classification — the `ratio_k` question, resolved directly from `run.py`

**Does SINGLE-NULL depend on `ratio_k`/floor-gate classification at all?**
Read directly from `run.py:561–570`:

```python
any_confirmed  = any(r["delta_scene"] > 0 and r["floor_pass"] for r in item1_report.values())
all_nonpositive = all(r["delta_scene"] <= 0 for r in item1_report.values())
...
if any_confirmed:      item1_outcome = "TWO-NODE CONFIRMED"
elif all_nonpositive:  item1_outcome = "SINGLE-NULL"
else:                  item1_outcome = "STILL AMBIGUOUS"
```

**No. `ratio_k` and the `ENERGY-DOMINANT`/`classification_word()` labeling
play zero role in the three-way outcome.** SINGLE-NULL fires purely
because `delta_scene ≤ 0` at **all six** interior points, `floor_pass`
included — the two `NODE-UNRESOLVABLE` points (41.75°, 41.775°,
`floor_pass=False`) still contribute their (well-defined, non-tiny)
negative `delta_scene` sign to `all_nonpositive`; only their *ratio* is
untrusted, not their *sign*. This is the correct, R13-consistent design:
R13 gates a **ratio** (`ratio_k = frac_p_abs/frac_contrast`, denominator
built from `|delta_scene|`), not `delta_scene`'s own sign, and the code
does not conflate the two. **This is a clean pass** — the SINGLE-NULL
verdict cannot be an artifact of ratio-classifier hazard, because it never
consults the ratio classifier.

## 3. The "20–84×" range: not what the headline implies, once the floor gate is applied

Independently pulled the six `ratio_k` values from `results.json::item1.per_theta`:

| θ | `delta_scene` | `ratio_k` | `floor_pass` | classification |
|---|---|---|---|---|
| 41.75° | −4.33e-5 | **83.89** | **False** | NODE-UNRESOLVABLE |
| 41.775° | −6.80e-5 | **50.66** | **False** | NODE-UNRESOLVABLE |
| 41.825° | −1.03e-4 | 29.58 | True | ENERGY-DOMINANT |
| 41.85° | −1.13e-4 | 25.11 | True | ENERGY-DOMINANT |
| 41.875° | −1.17e-4 | 22.26 | True | ENERGY-DOMINANT |
| 41.9° | −1.17e-4 | 20.48 | True | ENERGY-DOMINANT |

The task brief's "four of six interior points clear R13's floor gate...
all with very large `ratio_k` (20–84×)" **conflates two disjoint groups**.
The **four that actually clear the floor gate** span only **20.48×–
29.58×**. The two points spanning **50.66×–83.89×** are precisely the two
that **fail** R13's floor gate and are excluded from classification
(`NODE-UNRESOLVABLE`) — this is R13 working exactly as designed: `ratio_k`
inflates monotonically as `frac_contrast` (built from `|delta_scene|`)
shrinks toward the near-null centered around 41.75°–41.8° (the same region
exp-092's own Rank 1 flagged `41.8°`/`42.0°` as `NODE-UNRESOLVABLE`), and
the gate correctly strips the two most inflated readings before they reach
classification. **So: is the ratio_k inflation among the passing four
itself suspicious, or a legitimate ENERGY-DOMINANT reading?**

Independently computed each passing point's margin over `FLOOR` (=
`frac_contrast/FLOOR`, `FLOOR=1.917438e-4`):

| θ | `frac_contrast/FLOOR` | note |
|---|---|---|
| 41.825° | **1.0211** (2.1% clearance) | razor-thin |
| 41.85° | 1.1208 | thin |
| 41.875° | 1.1684 | thin |
| 41.9° | 1.1624 | thin |

**41.825° clears R13's binary floor gate by only 2.1%** — squarely in the
same hazard class NOTES.md's own item-2 table explicitly names elsewhere
(`40.2°... ratio_k=10.074 (razor-thin)`, flagged inline) but does **not**
name here. R13's gate is binary (pass/fail at a fixed `FLOOR`), not a
continuous discount — a point 2% above the line is treated identically to
one 20% above it once "passed," even though the underlying hazard (a
ratio built from a shrinking, near-null-proximate denominator) is
continuous, not binary. All four passing points sit on a smooth,
monotonically-decreasing `ratio_k` trend that extrapolates smoothly into
the two failing points — there is no discontinuity in the physics at the
gate boundary, only in the label. **Verdict on this sub-question: neither
purely "legitimate, well-resolved" nor a floor-gate defect** — the four
ENERGY-DOMINANT points are correctly gate-cleared by R13's own rule as
written, but 41.825° specifically inherits enough of the same near-null
proximity that drives the two excluded points' inflation that it should
not be cited, uncaveated, as equally solid as 41.9° (whose `ratio_k` is
31% lower and whose floor margin is 14% wider). **This is inert for this
cycle's own conclusions** — SINGLE-NULL doesn't touch `ratio_k` (§2) and
these four points are explicitly "context, not zone-defining" under the
SINGLE-NULL gate — but a **future** cycle citing "four ENERGY-DOMINANT
points, `ratio_k` 20–30×" as settled should not include 41.825° without
this caveat.

## 4. A materially undercaveated hazard, independently found: item 3's own data shows the sigma-comparability gap is not hypothetical

NOTES.md's Idealization 11 and the printed `sigma_branch_disclaimer`
correctly flag, *in the abstract*, that item 1's interior points (run at
corrected `σ_max=1/3` because item 3 fired REFUTE) are "NOT directly
comparable to the native-sigma flanking anchors." Pulling item 3's own
`per_theta` data directly (not the summary table) shows this is not a
theoretical caveat — it is **directly, empirically demonstrated** at
θ=42.0°:

```
native σ_max=0.5:    delta_scene = +8.0418e-5   (positive)
corrected σ_max=1/3:  delta_scene = -5.8102e-5   (negative)
delta_scene_ratio = -0.7225, sign_match = False
```

**The sign of `delta_scene` at 42.0° literally flips depending on which
`σ_max` convention is used**, and both magnitudes are comparable
(non-degenerate, ~6-8×10⁻⁵), not a vanishing-quantity artifact. This
matters because the **original** double-crossing this entire cycle exists
to resolve (`41.7811°`, `41.8377°`, exp-092) was located under the
**native** `σ_max=0.5` convention (exp-092's own Rank 1: "ran at native
sigma_max=0.5, directly comparable to exp-091's own filed data" —
LOGBOOK Iteration 69). Item 1's six new interior points, by the
pre-registered branch rule, ran at the **corrected** `σ_max=1/3` instead,
because item 3 REFUTEd. **The denser sweep that produced SINGLE-NULL and
the original sparse sweep that produced the double-crossing it is meant
to adjudicate are, by this cycle's own data, not proven to be measuring
the same physics** — item 3 shows the two conventions can disagree even
in *sign* within the exact 41.8°–42.0° neighborhood item 1 samples.
SINGLE-NULL is a well-supported finding **about the corrected-`σ_max`
regime specifically**; it does not, on its own, establish that the
original native-`σ_max` double-crossing was a resolution/interpolation
artifact, because the corrected-`σ_max` curve was never shown to coincide
with the native-`σ_max` curve anywhere inside the disputed window (only
outside it, at the three broader Rank-3 census angles, per item 3's own
predecessor test).

This is disclosed (Idealization 11, the branch-gate rule itself, the
printed disclaimer) — not a hidden defect, and the branch rule was fixed
*before* any run, per house discipline — but the disclosure reads as a
generic comparability caveat, not as "this specific sign-flip was
independently measured and is the reason SINGLE-NULL cannot, by itself,
rule out the corrected-`σ_max` equivalent of the original crossings
existing just outside the sampled 41.75°–41.90° window (most plausibly
between 41.6° and 41.75°, unsampled this cycle)." Worth stating in exactly
those terms in any future citation of SINGLE-NULL as resolving the
double-crossing question. Separately, and non-load-bearing: the printed
context-curve note ("41.6/41.8/42.0 are always native sigma_max=0.5") is
stale for this run — `combined_curve[41.8]`/`[42.0]` are, by the code's
own conditional (`... if sigma_item1 == SIGMA_NATIVE else
item3_report[...]["sigma_corrected_delta_scene"]`), actually populated
with the **corrected**-`σ_max` values this cycle (matches the printed
numbers, -8.79e-5/-5.81e-5, not item 3's own native figures,
-1.87e-5/+8.04e-5) — a cosmetic label/data mismatch in a print statement,
not a computation error (the underlying `results.json` fields are
correct and separately labeled), but worth a one-line fix.

## 5. Item 4 — independently re-verified a fourth time

Reimplemented the Yee-grid dispersion solve and the `ℓ=A` (752/1128
cells) length-scale table entirely from scratch (fresh interpreter, no
imported code) for the three angles with a known observed shift:

```
40.0718°: ratio = 32.11x
41.7811°: ratio = 80.22x
41.8377°: ratio = 95.79x
```

Matches the Director's Phase-3 §0 figures and Red Team's RT-2 approximate
figures exactly. **CONCUR** — the corrected `ℓ=A` mandate was actually
computed (not the shorter, previously-mis-cited `2×PAD`), and the REFUTE
of dispersion-alone as a *sufficient* explanation stands at one clean
order of magnitude, correctly downgraded from the pre-freeze draft's
mistaken two-order claim.

## Verdict: **CONCUR-WITH-GAP(S)**

The instrument design, sequencing, and every headline number I could
independently re-derive (item 2's AUC/Firth/zone; item 4's dispersion
ratios; item 1's outcome logic) check out exactly as filed. The gaps are
real but narrow and none are outcome-determining for what this cycle
actually claims:

1. The task brief's own "20–84×, four points, ENERGY-DOMINANT" framing
   conflates the four floor-gate-clearing points (actually 20.48×–29.58×)
   with the two floor-gate-**failing** points (50.66×/83.89×) — worth
   correcting in any future citation (§3).
2. One of the four passing points (41.825°) clears R13's binary floor by
   only 2.1% — a disclosed-elsewhere-in-this-document hazard class
   (NOTES.md's own "razor-thin" language for 40.2°) not applied to this
   point (§3).
3. SINGLE-NULL is empirically shown, by this cycle's own item-3 data, to
   be a finding specific to the corrected-`σ_max` regime, not
   demonstrated to coincide with the native-`σ_max` regime that located
   the original double-crossing — the comparability caveat already in
   NOTES.md (Idealization 11) is correct but should be stated with the
   42.0° sign-flip evidence behind it, not as a generic disclaimer (§4).

None of these reopens Checkpoint criterion 4 — all three are namable,
affordable-to-state gaps caught here, before any further citation builds
on them, matching this sub-thread's own repeated non-firing discharge
test.

## Ranked candidate directions for Iteration 71 (QUANTUM OPTICS)

1. **Highest priority — a native-`σ_max=0.5` cross-check at a small
   subset of item 1's interior points** (2–4 calls: e.g. 41.75° and
   41.825°, the two nearest the demonstrated 42.0° sign-flip), to test
   directly whether SINGLE-NULL survives under the *same* `σ_max`
   convention that located the original 41.7811°/41.8377° crossings —
   the single cheapest test that would let SINGLE-NULL be cited as
   resolving (not merely bounding, under one sigma convention) the
   double-crossing question §4 raises.
2. **A continuous (not binary) R13 confidence report** — alongside
   `floor_pass`, print `frac_contrast/FLOOR` for every classified point,
   so a 2%-clearing point (41.825°) is visually distinguishable from a
   16%-clearing one (41.9°) without a reader having to recompute it — a
   small, zero-FDTD instrumentation change that would have made §3's
   finding visible without an independent audit.
3. **Sample 41.6°–41.75° densely** (the still-unsampled gap where, per
   §4, the corrected-`σ_max` zero-crossing implied by 41.6°'s native
   positive value and 41.75°'s corrected negative value must actually
   sit) — this both closes the one genuinely unsampled sub-interval left
   in the 41.6°–42.0° window and would directly test whether a second
   (corrected-`σ_max`) crossing exists just outside item 1's own current
   sweep, which SINGLE-NULL's own construction cannot rule out from
   inside 41.75°–41.90° alone.
