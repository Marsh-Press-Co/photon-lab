# PHASE 5 — REVIEW · Panel Iteration 70 · exp-093 · Reviewing seat: THERMODYNAMICS (self-review, lead seat)

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md verbatim: where absorbed
energy goes; always asks what re-radiates and whether it would be
detectable; owns the per-proposal energy sidecar). This seat was Iteration
70's own Phase-1 lead — this is the mandated fresh-context self-review of
my own cycle's actual results, held to a HIGHER bar than the other six
reviewers, per this program's own established lead-seat-self-reviews-at-
Phase-5 practice.*

## 0. Independent recomputation (charter duty, done from raw fields, not trusted)

`results.json::item5.per_theta["39.2"]` reports `p_abs_w_c=3.088247571865681e-12` W,
`dt_ss_full_K_c=5.07366680346532e-05` K, `netd_classification_c=UNDETECTABLE`.
Recomputed from scratch, from source constants only (`lab/thermo_sidecar.py`,
`experiments/087-.../run.py`, `experiments/091-.../run.py`), not by trusting
`run.py`'s own arithmetic:

```
l_geometric_m = R3_R_OUT_CELLS(117) * DX_M_R3(20e-9)      = 2.34e-6 m
h_eff         = K_AIR(0.026) / l_geometric_m               = 11111.11 W/m^2K
area_m2       = l_geometric_m ** 2                         = 5.4756e-12 m^2
dp_dt         = area_m2 * (4*EMISSIVITY(0.9)*SIGMA_SB*T_AMBIENT_K(293.15)**3 + h_eff)
              = 6.086815889755324e-08 W/K
dt_ss_full_K  = p_abs_w_c / dp_dt = 5.07366680346532e-05 K   -- BIT-EXACT match
```

Then checked the deeper structural claim, across all **14** item-5 cells
(both configs, all 7 angles): `p_abs_w / dt_ss_full_K` recovers the
**identical** `dp_dt=6.086815889755324e-08` W/K at every single cell, zero
spread (`stdev=0.0`) — exactly as the formula predicts (`dp_dt` depends only
on fixed geometry/material constants, never on angle or config) and exactly
the kind of absolute-identity check this program's own R4/R6 discipline
asks for before a number is trusted. **No defect found in the core NETD
computation chain.** The `UNDETECTABLE` classification is also correctly,
if trivially, applied: `NETD_BAND_K=(0.020,0.050)` and every observed
`dt_ss_full_K` sits **350×–400× below the 0.020 K floor** — given the fixed
`dp_dt`, a cell would need `p_abs_w>1.217e-9` W to even reach `MARGINAL`;
observed values cluster at `~3.1–3.4e-12` W. Worth naming plainly: at this
bench's fixed geometry and irradiance, Item 5b's own "informational,
non-gating" prediction was never actually at meaningful risk of a surprise
— the margin is roughly three orders of magnitude, not a close call the
data could plausibly have flipped.

## 1. Self-review of my own two Phase-2-caught defects — were they avoidable?

**Item 2 (the "AUC reversal").** Yes, avoidable, and a clean single-cause
error: I computed `auc(pos,neg)` directly and read the `0.0000` result as a
finding, without first checking that `experiments/090-.../run.py` itself
calls `auc(-pos_m,-neg_m)` — a different question ("does higher margin
predict Y=1?" vs. the source's own "does lower margin predict Y=1?"). I had
`run.py` available to read before writing the proposal (I cite it directly
elsewhere in the same document) and simply didn't re-derive the comparison
under the source's own convention before asserting a "reversal." A
one-line grep-and-match check, the same one Red Team and the Director both
ran independently afterward, would have caught this before it was ever
written.

**Item 4 (the wrong length scale).** Also avoidable, and a more serious
error in kind: my own §7 opening line claimed to finally discharge a
mandate that both cited prior reviews (`exp-091`/`exp-092`
`phase5_review_em.md`) explicitly name as the **aperture length**
(`A≈752–1128` cells) — I quoted neither figure, substituted a different
number (`2×PAD≈80–120` cells, ~9.4× shorter) from a different, unrelated
prior instrument, and cited that instrument (`pad_round_trip_echo_model`,
exp-077) as "established" support — when exp-077's own Result section is
actually a **REFUTE** of that exact coherent-echo mechanism
(`r²=0.0001`). This is not a convention mismatch like item 2; it is citing
a refutation as if it were corroborating evidence, the citation-shape
error this program's own R9 lineage exists to catch. The mandate's own two
citations were sitting in my own required reading list — this was a
reading-discipline failure, not a hard-to-find fact.

**Common shape, both errors:** in both cases the underlying arithmetic was
computed correctly (the `0.0000` AUC value and the `2×PAD` dispersion
table are both numerically right) — the defect sits one layer up, in an
unverified claim about what the correct number *means* or *answers*,
asserted with the same confident tone as the verified arithmetic beneath
it. That is exactly the failure mode this program's R4/R8/R9 lineage
exists to catch, and I produced two instances of it in one draft.

## 2. A third instance of the same shape, found in this self-review

Looking for a third defect of the identical shape — a claim stated with
confidence that was never actually verified, surviving into the frozen
record — I found one, in my own §1 hypothesis text, uncaught by Phase 2/3:

**§1's own explicit, pre-registered self-test was never actually
discharged in writing, though the data to discharge it exists.**
`phase1_proposal.md`/`NOTES.md` §1 states: *"This cycle's own §3 data will
test that expectation directly, not merely assert it: a
`netd_classification` swing coincident with the disputed node would itself
be a new, genuinely surprising finding."* But Item 5b's own NETD summary
(`run_output.txt` lines 66-81, `results.json::item5b`) reports **only** the
14 Rank-1 grid cells (39.2°–42.0° at 0.2° step) — **none of which sit
inside the actual disputed interior**, `[41.75°,41.90°]`. The cells that
*do* sit at the disputed node — item 1's own six new interior points — DO
carry full `dt_ss_full_K_c/g`/`netd_classification_c/g` fields
(`results.json::item1.per_theta`, correctly populated via
`cell_metrics_full`/`pair_metrics_full`/`netd_row`, wired for exactly this
purpose) — but those fields are **never printed, summarized, or given a
verdict anywhere**: `run_output.txt`'s Item 1 block prints only
`delta_scene`/`frac_contrast`/`ratio_k`/`class`/`floor_pass` (lines
556-559 of `run.py`); no NETD figure for these six cells appears in
`run_output.txt`, `NOTES.md`, or `results.json`'s own `item5b` block. The
proposal's own signature self-test was set up correctly, computed
correctly, and then silently dropped between computation and report.

**I independently checked it here, so it does not stand open.** Pulling
`item1.per_theta`'s own `dt_ss_full_K_c` across the full 39.2°–42.0° span
(both item 5's and item 1's own cells): the channel is smooth and
monotonically rising with θ (`5.07e-5`→`5.34e-5` K, tracking
`sigma_ext_cells`'s own gentle angle-dependence, unrelated to the
interference structure) — no swing at the disputed node. The one local
bump (41.8°/42.0° reading `~5.52–5.58e-5` vs. neighboring interior points
at `~5.3e-5`) is fully explained by the disclosed `sigma_max` mismatch
(0.5 native vs. 1/3 corrected, exactly Idealization 11's own caveat), not
a physical effect at the null. **The underlying physics claim survives —
but the written record never actually states this**, leaving the cycle's
own pre-registered falsifiability test formally undischarged on paper,
even though every field needed to discharge it was sitting in
`results.json` the whole time. This is the same *shape* as items 2 and 4
(a confident claim, unverified in the delivered record) though milder in
consequence, since the data happens to support the claim once actually
checked — nobody, including me at Phase 1/3, ever checked it before now.

**A second, purely additive process gap, also self-caught:** `NOTES.md`
has no `## Result`, `## Learned`, or `## Next` section at all (confirmed:
`grep '^##' NOTES.md` returns only Hypothesis/Setup/Idealizations/
Predictions/T1-route; compare `experiments/092-.../NOTES.md`, which has
all three after its own Phase 4). `NOTES.md`'s last edit (15:37) predates
`results.json`/`run_output.txt` (16:16) — the frozen predictions document
was never updated with the actual outcome, contrary to both this lab's own
CLAUDE.md convention ("hypothesis / setup / result / learned / next") and
this exact sub-thread's own immediately-prior precedent. This is separate
from, but compounds, the gap above: even a reader who wanted to check the
item-1 NETD self-test from `NOTES.md` alone (rather than raw JSON) would
find no Result section to check it against.

## 3. Was §1's "nothing, either way" claim actually tested, or only asserted?

**Partially tested, and the SINGLE-NULL outcome narrows what it can now
claim.** The proposal's own framing was "whichever way the double-crossing
resolves... the absorbed-energy channel is expected to stay smooth and
undetectable **regardless**" — a claim about two branches. Item 1 resolved
**SINGLE-NULL**, not TWO-NODE CONFIRMED: the "genuine two-node feature"
branch never materialized this cycle, so the "regardless" framing is now
verified for only one of the two cases it named — the trivial one, where a
smooth energy channel under a smooth interference channel is the
unsurprising default, not the branch that would have actually tested
mechanistic decoupling. The genuinely load-bearing test of decoupling — a
real two-node interference feature coincident with a real energy-channel
swing — was never run, because the interference feature it would have
needed to coincide with turned out not to exist.

**The one real, affirmative evidence for the decoupling claim this cycle
produced is Item 3b, not Item 5b.** Item 3 (the `sigma_max` check at the
near-null) fired **REFUTE** on `delta_scene` (`ratio=4.71×`/`−0.72×`,
sign flip at 42.0°) while Item 3b (`p_abs_w` ratio) fired **CONFIRM**
(`ratio=0.962`/`0.963`, both inside `[0.3,3.0]`) at the *identical* two
angles — the interference channel is sensitive to `sigma_max` exactly
where the energy channel is not. That is a genuine, already-reported,
already-scored piece of evidence for "the two channels are mechanistically
decoupled," independent of how the double-crossing itself resolves, and a
stronger test than Item 5b's own reproduction-only check. It deserves more
weight in the record than it currently gets — `NOTES.md` states the Item 3b
result but never connects it back to §1's own headline claim.

## 4. Minor, non-consequential finding

`NOTES.md`/`phase1_proposal.md` §11 cite Rank 3's own filed C-config NETD
values as "`4.6×10⁻⁵`–`5.2×10⁻⁵` K." The actual filed range
(`experiments/092-.../results.json::rank3.per_theta[*].filed_dt_ss_full_K`)
is `4.78e-5`–`5.39e-5` K — the upper bound is understated by ~4%. Does not
change any verdict (this cycle's own 14 values, `5.07e-5`–`5.59e-5` K, are
still comfortably inside the broader `1e-5`–`5e-4` K predicted band either
way) — flagged only in the spirit of this seat's own "verify, don't trust"
duty.

## 5. Verdict: **CONCUR-WITH-GAP(S)**

The substantive physics and the Phase-2/3 correction process are sound:
both Phase-2-caught defects (RT-1, RT-2) were real, were fixed with
genuine independent triple-verification (proposer → Red Team →
Director, all three landing on bit-exact figures), and the corrected
`ℓ=A` result (32×–96×, one order of magnitude, not the mistaken two) is a
*more* honest and still-clean REFUTE, not a rescued one. My own
first-principles recomputation of the NETD chain (§0) finds no defect. But
this self-review surfaces two real, avoidable gaps that should have been
closed before this cycle was called complete: (a) the cycle's own
pre-registered self-test at the actual disputed node was computed but
never reported or verdicted — a third instance of the same
confident-but-unverified-claim shape that already burned this draft twice;
(b) `NOTES.md` is missing its Result/Learned/Next sections entirely,
against both house convention and this sub-thread's own immediate
precedent. Neither is a Checkpoint-4-grade defect (both are self-caught,
before any external citation of the wrong claim, and (a)'s underlying
physics claim holds up once actually checked) — but both are exactly the
kind of gap this program's own lead-seat-self-review practice exists to
catch, and as the lead seat I should have caught (a) before Phase 4 closed
out, not at Phase 5.

## 6. Ranked candidate directions for Iteration 71 (THERMODYNAMICS perspective)

1. **Close this cycle's own dropped self-test, zero new FDTD.** Add an
   explicit "Item 1 NETD/energy-channel check" paragraph to `NOTES.md`'s
   (currently absent) Result section: state the six interior
   `dt_ss_full_K`/`netd_classification` values already sitting in
   `results.json::item1.per_theta`, verdict them against §1's own named
   self-test ("no swing coincident with the disputed node" — CONFIRM, per
   §2 above), and note the `sigma_max`-driven discontinuity at 41.8°/42.0°
   explicitly so a future reader doesn't mistake it for a physical
   effect. This is pure write-up of data that already exists.
2. **Backfill `NOTES.md`'s Result/Learned/Next sections** from
   `run_output.txt`/`results.json` before this cycle is cited forward by
   any future T28 iteration (matching the exp-080/Iteration-56 precedent
   for a same-shift missing-`NOTES.md` fix) — a pure hygiene item, but one
   this sub-thread has now needed twice.
3. **A genuine next physical question for this seat**, not just hygiene:
   Item 3b showed `p_abs_w` decoupled from `sigma_max` where `delta_scene`
   is not; this cycle's own Item 5/Item 1 backfill shows `p_abs_w` also
   smooth across the entire 39.2°–42.0° span regardless of the disputed
   interference structure. Both findings point the same direction — the
   absorbed-power channel appears robust to every perturbation this
   sub-thread has thrown at the interference channel so far. The next
   THERMODYNAMICS-owned test worth running is the inverse question this
   cycle never asked: does `p_abs_w` stay this smooth **across `cpl`**
   (20→30→40), the one axis item 2's own gate (§6/Idealization 16) already
   flags as unresolved for `delta_scene` — i.e., is the energy channel's
   own apparent resolution-independence itself R15/R3-verified, or only
   assumed by extension from the interference channel's own still-open
   cross-resolution question? Cheap (reuses `cell_metrics_full` verbatim,
   zero new `lab/` diff) and directly extends this cycle's own signature
   deliverable rather than opening a new one.
