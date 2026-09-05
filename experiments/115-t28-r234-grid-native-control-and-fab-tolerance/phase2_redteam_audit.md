# Phase 2 Red Team Audit — exp-115 (Panel Iteration 92)

*Red Team seat, PANEL.md charter verbatim: "attacks every proposal, speaks
last and hardest. Its standard is NOT textbook-physics compliance —
speculation is permitted. It kills: internal inconsistency, unfalsifiable
claims, mechanisms that cannot be expressed as simulation parameters, and
proposals that quietly violate a target constraint — especially #3. Red Team
never leads a cycle; it has no proposal of its own to protect."*

**Inputs received:** `PANEL.md`; `LOGBOOK.md` in full (RULED OUT R1–R34 line
by line, ESTABLISHED, LIVE THREADS T1–T28, the T28 sub-thread's own
Iteration-46→57 record and Iterations 84–91); `PLAN.md` 1–110; this cycle's
`phase1_proposal.md`; all five Phase-2 blind critiques (PHOTONICS, EM,
THERMODYNAMICS, QUANTUM OPTICS, VISION SCIENCE); the exp-114 record
(`run114.py`, `chunk_runner114.py`, `analyze114.py`, `results.json`,
`phase5_redteam_audit.md` — this seat's own prior audit);
`experiments/113-.../chunk_runner113.py`+`run113.py`;
`experiments/112-.../results.json`+`chunk_runner112.py`;
`experiments/110-.../run.py`+`results.json`;
`experiments/108-.../run.py`+`results.json`;
`experiments/061-.../NOTES.md`; `lab/materials.py`; `lab/sections.py`;
`lab/fdtd2d.py`; `lab/caveat_lint.py`+`lab/caveat_lint_config.json`;
`lab/validation/VALIDATION.md`; `lab/ARTIFACTS.md`.

**Method.** No sub-agents, no delegation, no simulations, no git state
changed. Every number below was produced this session by executing pure
python against committed JSON and committed source, or by re-deriving it
from primitives — never restated from the proposal's prose or from any
critique's prose. Where a critique's figure is marked CONFIRMED I recomputed
it myself; where it is marked REFUTED I show the recomputation that kills it.
This is required, not optional, under the R4 Third Addendum's own standard
for a Phase-2 Red Team audit.

---

## 0. What I could and could not verify

**Verified from primitives (all reproduce):** the `measured_ratio ≡
kappa_ratio × G` identity (bit-exact, 15 digits); every M5/M6/M7 band edge;
`R_DEG`; `ε(2.0)`; the v2 straddle reconstruction and its `G ≥ 2.5652851`
boundary; the optical-theorem residual's bit-identity between scenes; the
`σ_ext ≡ σ_scat + σ_abs` tautology; `I_graded` and `τ_true` recomputed from
`lab/materials._graded_black` at both family members and at 450/600/750 nm;
exp-112's 48-bin arrays under three normalizations plus its own floor gate;
exp-110's floor-gated `local_rel` at both radii; exp-108's `rel32` and
`item_ii` six-margin family; exp-114's per-scene production wall times; the
caveat-lint trigger blindnesses; the constraint-3 grep.

**Could not verify:** the bench's own "41/41 in 87 s" trust-suite figure
(§6 of the proposal) — no committed artifact, no platform/numpy line, and I
am not on the T5820. `lab/validation/VALIDATION.md`'s own docket-14 rule
already says a reproducibility claim that does not name its platform is not
a gate. The Director must re-run it on the bench and commit the console
record before Phase 3 closes (docket MF-12). Also unverifiable from this
repository: exp-114's three r=234 chunk times, which survive only as
quotations inside `experiments/114-.../phase5_redteam_audit.md` §2 — the
proposal discloses this correctly (Idealization 4), and every figure I derive
from them below inherits that same non-re-derivable status and is labelled
directional.

---

## 1. Attacks on the PROPOSAL

### RT-1 [inconsistency] — M9(c) uses the wrong functional form; the sidecar's own headline physics prediction is wrong by `exp(+τ_true) ≈ 3.86×10³`

`τ_true` is a one-way **intensity** optical depth. This is not a reading of
exp-061's prose; it is forced by its own construction, which I re-derived:
`tau_true = 2·(2π/cpl)·thickness_cells·I_graded`, the leading 2 being the
`α = 2k₀·Im(n)` intensity convention, corroborated by the same block's own
`α_true = 5.7353×10⁴ cm⁻¹`, `e-fold = 1/α = 174.36 nm`, `OD = τ/ln10 = 3.587`.

The measured observable is a **relative change in a cross-section**, and every
cross-section in `lab/sections.py` is a flux integral quadratic in the
**total** field. Writing `A = A_shell + A_core`:

```
Δσ/σ = [ 2·Re(A_shell* · δA_core) + |δA_core|² ] / |A_shell|²
```

The leading term is the **coherent cross term**, first order in the returned
amplitude. Recomputed from `lab/materials._graded_black` (2×10⁶-point
trapezoid, `Im(n) = Im√(1 + i·σ·cpl/2π)`):

| quantity | value | what it is |
|---|---|---|
| `I_graded` | `0.273840` | reproduces exp-061's committed value to 6 dp |
| `τ_true` | `8.258813` | reproduces the filed `8.258819829686677` to `8×10⁻⁷` rel |
| one-way amplitude `exp(−τ/2)` | `1.6092×10⁻²` | |
| **round-trip amplitude `exp(−τ_true)`** | **`2.5896×10⁻⁴`** | the correct scale |
| **coherent cross-term bound `2·exp(−τ_true)`** | **`5.1793×10⁻⁴`** | the correct upper bound |
| `exp(−2τ_true)` (the proposal's figure) | `6.7063×10⁻⁸` | the `\|δA\|²` term only |

`exp(−2τ_true)` is the right answer to "how much core-reflected *power*
returns" and the wrong answer to "how much does the *cross-section* change."
This is a deterministic single-frequency FDTD field; the cross term does not
average away.

**Three consequences, all of which would enter the permanent record false:**

1. M9(c)'s "three orders of magnitude below anything this instrument can
   resolve" inverts. Against `2·exp(−τ_true)`, the measured aggregate deltas
   sit at `0.16×–0.30×` of the estimate, not `1250×–2280×` above it.
2. §5-M9's claim that (c) is "fully consistent with (b)'s reading that the
   measurement is floor-limited" is exactly backwards: as drafted, (b) says
   five of six deltas are *above* the floor and (c) says the physics is
   `320×–2280×` *below* them. Those cannot both be right.
3. M9(d)'s "the physical value is predicted at `O(10⁻⁷)`" and M9(e)'s
   forward scaling "the bound scales as `exp(−2·τ_true)`" both carry twice
   the true exponent — in the paragraph R21 exists to push into LOGBOOK.

**The pre-registered HALT cannot catch this.** M9's stated falsifiable element
is an arithmetic-reproduction gate to `<1e-12`, plus a `<1%` reproduction check
on `τ_true`. I ran the `τ_true` check: it **passes** (`8.258813` vs
`8.258819829686677`). A reproduction gate is structurally incapable of
catching a functional-form error — it certifies the number and publishes the
wrong physics. See RT-15.

### RT-2 [inconsistency] — M9(b)'s floor gate has provably ZERO differential content

`lab/sections.py:130–151`: `p_scat = F(ps)`, `p_abs = −F(pt)`,
`sigma_ext = (p_scat+p_abs)/i_inc`, `sigma_ext_cross = −F_cross(pi,ps)/i_inc`,
with `pt = pi + ps` and `F` sesquilinear. Then

```
p_ext = F(ps) − [F(pi) + F_cross(pi,ps) + F(ps)] = −F(pi) − F_cross(pi,ps)
p_ext_cross − p_ext = F(pi)     ← the EMPTY capture's own flux imbalance
```

— a function of `cap_empty` and the box alone, carrying **no scene
information**. Confirmed numerically against the real ledgers:

```
r=234:  σ_ext_cross − σ_ext (peccored) = 0.030391497834443726
        σ_ext_cross − σ_ext (hollow)   = 0.030391497834443726
        difference between scenes      = 0.0            (EXACTLY, float64)
r=156:  difference between scenes      = 2.27e-13       (roundoff)
```

So the quantity M9(b) adopts as its floor is **bit-identical in the two
configurations being differenced** and cancels exactly. The statements "those
deltas sit at 0.2×–12.6× the channel's own optical-theorem self-consistency
floor" and "the correct statement is therefore an upper bound, not a resolved
measurement of a nonzero effect" are both void — the first divides a
between-scene difference by a within-scene common-mode residual (a pure R9
incommensurability), the second draws a conclusion from it.

**A genuine differential floor does exist on file and says the opposite.**
exp-108's `item_ii` measures the SAME `peccored − hollow` differential at six
independent box radii. Recomputed from its committed `delta_values`:

| | mean delta | raw std over 6 margins | mean/std |
|---|---|---|---|
| r=156 | `−2.4494×10⁻⁵` | `5.486×10⁻⁶` | **4.46×** |
| r=312 | `−2.7213×10⁻⁵` | `2.327×10⁻⁶` | **11.70×** |

On the only differential floor this program has, the core-swap effect is
**resolved at 4–12×**, not floor-limited. And **no differential floor exists
at r=234 at all** (THERMODYNAMICS' `box_dev` gap, which its own exp-114
Phase-5 review already named non-load-bearing there and which M9(d) makes
load-bearing here).

### RT-3 [inconsistency + constraint-2-channel exposure] — M9(d)'s per-bin claim is refuted at the resolution this program's own R13 instrument certifies, by 99×–347×

exp-108's `rel32 = |delta32| / max|peccored32|` is normalized by the **global
peak over 48 bins**. LOGBOOK Iteration 85 already records, as PHOTONICS' own
ratified self-review finding, that this normalization is "structurally blind
to real shape differences in low-cross-section side/back-scatter sectors" —
and exp-110 was built at Iteration 87 specifically to replace it with a
floor-gated **local** normalization (`classify_item_i_local`, R13 discipline).
Recomputed from exp-110's own committed `results.json`, margin=32:

| | max floor-gated `local_rel` | bins resolved | vs M9(d)'s `1.6×10⁻⁴` |
|---|---|---|---|
| r=156 | `1.4669×10⁻²` at `+123.75°` | 34/48 | **99.4×** larger |
| r=312 | `5.290×10⁻²` at `+138.75°` | 38/48 | **346.5×** larger |

M9(d) states "the far-field optical signature — **per-bin angular pattern**
and every aggregate cross-section alike — is insensitive to the core/backing
material at **better than 1.6×10⁻⁴ relative** … 48 angular bins." That is
false for the per-bin channel on the program's own purpose-built, R13-
compliant instrument, and the sidecar re-adopts precisely the normalization
the program already corrected two iterations ago.

**Constraint-2 exposure, stated precisely.** The two largest floor-**resolved**
r=312 deviations sit at `±138.75°` (`0.0529` / `0.0523`) — inside the
observer-return hemisphere PANEL.md's metrics table row 2 scores constraint 2
on. M9(d)'s bolded sentence ("the material behind it is a free parameter over
the entire span from vacuum to a perfect conductor"; "does not need to control
the substrate or core material … at all") licenses a future cycle to vary the
backing without re-measuring a channel that moves ~5% there. I am **not**
claiming a constraint-2 failure — `back_frac ≈ 3.4×10⁻⁶` is minuscule in
absolute terms. I am ruling that the bound as written does not cover that
channel and reads as though it does. That is a quiet constraint-adjacent
overreach in a sentence built to be quoted forward, and it is squarely in this
seat's kill list.

### RT-4 [inconsistency] — M9(d)'s scope clauses contradict the proposal's own §2.0

`experiments/108-.../run.py:244–254` sets `confirm_all_margins` as one boolean
over `MARGINS = (24,32,40,48,57,65)` against `ITEM_I_CONFIRM_REL = 0.05`; only
the margin-32 array is persisted (I enumerated the keys — no other margin's
array exists). So five of six radii are certified at `5×10⁻²`, a bar **330×
looser** than the quoted figure. The proposal states this correctly at §2.0
line 104, as an R4 self-correction, and then contradicts it at line 497. R4's
second addendum ("an aggregate flag … is not sufficient to certify an 'every
single X' claim") applies directly, and here the document refutes itself two
sections apart.

Same sentence: "two grid resolutions (cpl 20 and 25)" is not a resolution
check on any channel. The per-bin channel exists only at cpl=20 (exp-108/110,
r=156/312); the aggregate channels only at cpl=25 (exp-112/114, r=156/234).
Channel and resolution are **fully confounded** — Idealization 7 discloses the
radius factorisation and not this one.

### RT-5 [inconsistency] — M5's stated invocation, executed literally, returns a false REFUTE

`run114.py:258` — `classify_kappa_exponent_check(exponent_234, kappa_ratio=…)`
takes an **exponent** and forms `measured_ratio = kappa_ratio ** exponent_234`
internally. §5-M5 says it passes `measured_ratio_B = 1.5 × G_sustained`,
"invoking the same committed classifier unmodified." Executed on exp-114's own
filed value:

```
1.5 ** 4.11825848092089 = 5.311159219494333
rel_dev = |5.311159 − 3.6680107109370383| / 3.6680107109370383
        = 0.44796720567305326   →  REFUTE
```

against the correct route, `exponent_B = ln(1.5·G)/ln(1.5) = 3.490880835…`,
`rel_dev = 0.12274985147707763` — exp-114's own filed figure. The log-inversion
step appears nowhere in the document. This is R18's literal trigger (a check's
documented use must be confirmed against its actual source before it is relied
on), and the failure mode is a *plausible-looking* wrong verdict on the
cycle's declared PRIMARY metric.

### RT-6 [inconsistency] — the execution order does not do what §2.2 says, and the fix three seats propose is not free either

**The proposal's own justification is factually wrong.** §2.2 line 163: "each
sustained reading with an adjacent **same-duration** reading on the other
grid." The readings are matched in **step count**, not duration; at
`G ≈ 2.75` the r=234 reading takes ≈2.75× the wall time of its partner. That
mismatch is the entire bias.

**Closed form, re-derived independently of EM.** For readings of duration `a`
(r=156) and `b` (r=234), taking each reading's midpoint as its sampling time:

```
A,B,A,B : mean(A) = T₀+a+b/2 ,  mean(B) = T₀+1.5a+b  →  lag = (a+b)/2   (any a,b)
A,B,B,A : mean(A) = T₀+a+b   ,  mean(B) = T₀+a+b     →  lag = 0         (any a,b)
```

Under A,B,A,B both sustained pairs inherit the **same-signed** bias, so the
mean does not cancel it and `d_rep` — the cycle's only noise instrument —
reads ≈0. That is an alarm structurally incapable of producing the reading
that means "bad," `lab/ARTIFACTS.md`'s own named invariant.

**But ABBA is not a free win, and no critique says so.** Same-grid repeat lags:

```
A,B,A,B :  A2−A1 = a+b        B2−B1 = a+b        (EQUAL)
A,B,B,A :  A2−A1 = a+2b       B2−B1 = b          (UNEQUAL, ~2.4× apart)
```

The equal-lag same-grid repeats are the *only* direct measurement of whether
session drift is **grid-dependent** — which is M3's actual question — and they
are exactly what THERMODYNAMICS' own §8 recommendation ("persist `d_156`,
`d_234` and re-anchor M3/M4 on them") depends on. ABBA destroys that
comparability. EM, THERMODYNAMICS and QUANTUM all propose ABBA; none notices
that it repurposes `d_rep` from a repeatability statistic into a drift
statistic while the three composition rules that consume `d_rep` were written
for a repeatability statistic.

Adopt ABBA (the mean of the two pairwise `G` values is then unbiased to first
order without needing to *estimate* the drift, which is the more robust
construction), **but** with per-reading timestamps, drift reported as a **rate
per unit elapsed time** so the unequal lags are handled, and `d_rep`'s changed
meaning restated wherever it gates. See MF-6.

### RT-7 [inexpressible / underpowered] — M5, the declared falsifiable heart, cannot separate its own question from its protocol mismatch

Two defensible protocol models are both on file, and they predict `G` on
**opposite sides of the CONFIRM ceiling** (`2.8121415`):

- **Drift/degradation model** (QUANTUM's B2): extrapolate `R_DEG = +7.596%`
  log-linearly from `1000→3334` to `3334→12000` ⇒ a 3334-step burst is
  ~8.08% *faster* per step than production ⇒ `G ≈ 2.5403` — comfortable
  CONFIRM.
- **Warm-up-amortization model** (THERMODYNAMICS' §7, PHOTONICS' §4.8, EM's
  A11(ii)): within exp-114's own r=234 production scene the first 3000 steps
  ran **4.467% slower** per step than the 12000-step average, so a burst is
  *slower* than production ⇒ the burst-to-burst ratio inside exp-114's own
  session is `p234_burst/p156_sustained = 2.8802` (scene-mix-corrected:
  `2.868`) — **above** the CONFIRM ceiling, i.e. AMBIGUOUS.

The span `2.540 → 2.880` is 13.4%, comparable to M5's entire CONFIRM
half-width (15%). Neither critique composes the two halves; both halves are in
the record. **M5 as designed therefore has no power to distinguish "`k`
generalizes to `kappa_ratio=1.5`" from "the burst-vs-production protocol
factor is X%."**

Independently, EM's A12(1) is correct and I re-derived it: pure `N²` scaling
gives `G = 2.25`, hence `rel_dev = |2.25/2.4453405 − 1| = 0.0799` — **inside
the CONFIRM band**. So a CONFIRM cannot distinguish `k = 3.2053` from
`k = 3.0`, the pre-R28 hardcoded exponent. The entire hypothesis space between
the two competing exponents is 8% wide; the CONFIRM band is 15% wide.

This does not kill the cycle — it means the cycle must pre-register what its
own primary metric *can* and *cannot* decide, and must persist a
protocol-mismatch interval rather than a point verdict. See MF-7.

### RT-8 [inconsistency] — three R4-class citations that do not reproduce from their own sources

1. **"`peccored` steps are ~14% costlier"** (§2.2, offered as what exp-113's
   Fix 3b established). exp-114's own committed `total_wall_s_by_scene` is the
   only profiled per-scene measurement in the record:
   `peccored/hollow = +1.287%`, `peccored/empty = +0.009%`, full spread
   **1.29%** — a 10× overstatement. Three seats converge on this
   independently. The 3-scene mix is still the right protocol choice on
   commensurability grounds; the stated reason is wrong. *Disclosure against
   my own seat:* this same "~14%" figure was used as a directional caution in
   **this seat's own exp-114 Phase-5 audit §2**; that caution is hereby
   corrected forward, and its conclusion ("its direction only widens the 28.0%
   spread") no longer stands on that ground.
2. **Idealization 4's "≲5%" chunk-boundary bound.** The three quoted chunk
   times have `max/min = 214.2101/196.8292 = 1.0883` — an **8.83%** spread.
   Worse, chunk scatter is the wrong statistic for the mismatch it claims to
   bound: the real level shift inside that same run is 4.47% between the first
   3000 and the full 12000 steps, which chunk scatter cannot see.
3. **"three independent energy-ledger channels"** (§5-M9(d) line 497).
   `lab/sections.py:150` *defines* `sigma_ext ≡ (p_scat+p_abs)/i_inc`, so
   `Δσ_ext ≡ Δσ_scat + Δσ_abs` identically. Verified: `Δσ_scat + Δσ_abs −
   Δσ_ext = 0.0` exactly at r=234, `−5.68×10⁻¹⁴` at r=156. Two channels and
   their exact algebraic sum. At r=156 the two genuine channels *partially
   cancel* (`+0.0293` against `−0.0143`), so the derived `σ_ext` delta is
   about half the largest real one — the flattering direction.

Tally: 3 in one document, plus two scope overclaims (RT-3, RT-4). R20 does
**not** fire — all five are pre-freeze and caught at Phase 2, not surviving
the Phase-3 freeze into Result/Learned and caught only at Phase 5, which is
R20's own operative condition. Named as a standing observation; this is the
sixth consecutive cycle landing at or just under R20's density bar.

### RT-9 [inconsistency] — two undisclosed, non-uniform normalization conventions inside one headline ratio

The six M9(a) deltas reproduce **only** under a symmetric-mean denominator
`|h−p|/((h+p)/2)`; the two self-consistency floors reproduce **only** under the
`peccored` scene (r=156: `/peccored = 6.649462×10⁻⁶` → quoted `6.6495e-06`;
`/hollow = 6.649320×10⁻⁶` → would round to `6.6493e-06`). Both verified. So
the headline R13-framed ratio "0.2×–12.6×" mixes a mean-normalized numerator
with a `peccored`-normalized denominator. The numbers are right; a reader
cannot reproduce them without guessing twice. One sentence of formula fixes
it. (VISION §4.10(1) — confirmed exactly.)

### RT-10 [inconsistency] — "far-field optical signature" mischaracterizes the instrument

`lab/sections.py:212–215` states in its own docstring that the angular channel
is "a square-path angular sample, not a true circular far-field pattern —
consistent with `sigma_scat`'s own near-to-mid-field box convention," and
LOGBOOK's ESTABLISHED section plus T9 record that this bench's box "sits deep
in the shadow's near zone" (the `σ_abs/σ_ext = 0.51` and `0.606–0.608`
readings both **exceed** the far-field Babinet ceiling of 0.5 for exactly that
reason). A near-field bound does not license an unqualified far-field
fabrication claim in a blockquote written to be quoted forward.

### RT-11 [inconsistency] — "resolves the v2 straddle" is a claim this cycle cannot cash

Reconstructed from primitives: `measured_ratio_v2 = 1.5 × 2.25 ×
(p234_prod/p234_burst)` — I reproduce `3.217195628521234` against the filed
`3.2171956285212335`. **No r=156 quantity appears anywhere in it.** Its two
unverified operands are (i) the assumed `G = 2.25` and (ii) the
intra-r=234-grid factor `p234_prod/p234_burst = 0.9532431491914767`. Item 1
measures (i); §2.2 runs no r=234 production leg, so (ii) is left exactly where
exp-114 left it. Substituting a measured `G`:

```
signed_dev(v2′) ≥ 0  ⟺  G ≥ 3.6680107109370383 / (1.5 × 0.9532431491914767)
                       = 2.5652851279677367
(2.5652851 − 2.0785394)/(2.8121415 − 2.0785394) = 0.6635  →  66.4%
```

**Over 66.4% of M5's own CONFIRM band, the cycle returns "CONFIRM,
replicated" while the straddle is still open** — and M6, titled "the direct
answer to the v2 straddle," computes `T = G/G_E`, which never touches v2's
construction. QUANTUM's B1 is correct in every digit.

Compounding this, EM's A2 is also correct: the straddle lives between two
normalizations of *exp-114's own cloud-session denominator*; a bench-measured
`G` bears on it only under machine-transferability, which is M6, which the
proposal itself labels an `N = 2` test (Idealization 3). As framed, the
untested assumption is used to license the claim that the straddle is
resolved.

### RT-12 [inconsistency] — the coded call-count invariant conflicts with the cycle's own graceful-degradation branch

§2.2/§8 commit to asserting **18** `Sim.run()` calls (R19 discipline); §6
permits skipping readings 5–6, which yields **12**. A coded invariant that
fires spuriously on the designed-safe path is worse than none.

### RT-13 [inconsistency] — the composition rules are asymmetric, and the one metric that can move a frozen LOGBOOK verdict has none

- **M6's caveat fires on 1 of 4 reachable M3 states.** M3 can read CANCELS,
  PARTIAL, DOES-NOT-CANCEL, or UNINTERPRETABLE (M4's own rule), plus the
  `repeat_skipped` path. PARTIAL, UNINTERPRETABLE and repeat-skipped all
  escape `g_e_protocol_caveat` — and UNINTERPRETABLE is the state in which
  least is known. This is verbatim the composition gap Red Team had to close
  in code at exp-113 Phase 5 (R32's own founding record).
- **PARTIAL is the most likely M3 outcome by construction**: DOES-NOT-CANCEL
  requires the other grid to degrade by *exactly zero*.
- **M5 has no composition rule at all**, while M3, M6 and M7 each have one —
  and M5 is the only metric that can force a re-framing of a frozen LOGBOOK
  entry. That asymmetry is R24's own shape one step earlier (a consequence
  wired into one classifier and not its sibling; cf. `classify_item_i` vs
  `classify_item_ii`, the Iteration-85 Checkpoint-4 firing).
- **M4's MARGINAL band straddles two consequential thresholds** (`0.03` ⇒ M7
  UNDERPOWERED; `0.0379821` ⇒ M3 UNINTERPRETABLE), so a reader seeing
  "M4: MARGINAL" cannot tell whether M3 was scored or voided.

### RT-14 [inconsistency] — M7's label is one-sided on a two-sided statistic, and neither candidate model can produce its "hold" outcome

`|excess| ≥ 0.1529500` also fires at `excess = −0.1529500` (`G = 1.9059`),
which is **sub**-cell-count scaling — the opposite finding — and gets the same
`N2_FAILS` string with the inherited meaning "as large as the r=312 grid's
already-established one," true only on the positive branch. Separately, and
verified: the in-force constant-`k` model predicts `excess = 0.08682` →
**AMBIGUOUS**; the constant-`ε` model predicts `excess = 0.152950039837078`,
**bit-identical to the `N2_FAILS` bar** (exceeding it by `4×10⁻⁸`). `N2_HOLDS`
requires *both* candidate models to be wrong. And VISION's identity is right:
`ε_E/ε_k ≡ G_E/G_ref ≡ measured_ratio/reference_ratio`, so M7's "12.275%" is
numerically the same datum as exp-114's filed `rel_dev` — M5 and M7's
secondary comparison are one datum wearing two hats.

### RT-15 [unfalsifiable] — M9's stated falsifiable element cannot fail on the defect that matters

§5-M9 states its expressibility contract explicitly: "this sidecar carries
**no blind prediction** … what it carries instead is a code-enforced
arithmetic reproduction gate … any mismatch HALTs the sidecar." I executed the
one substantive sub-check (`τ_true` recomputation): it **passes**. So the
sidecar's entire declared falsifiable content is a gate that passes while
publishing a physical prediction wrong by `3.86×10³` (RT-1), a floor with zero
differential content (RT-2), and a per-bin bound refuted by 347× on the
program's own instrument (RT-3). Under this seat's charter — "it kills …
unfalsifiable claims" — M9 as drafted does not clear the bar. It clears it
easily once MF-1..MF-4 land, because the corrected (c) becomes a genuine
zero-free-parameter prediction that the measured deltas either do or do not
sit within an order of, and MF-2's differential floor makes "resolved vs
floor-limited" an answerable question rather than an asserted one.

### RT-16 [inconsistency, minor] — the perturbation is not a pure core-material swap, and the alternative it opens is closable now

`materials.pec_disk` sets `sim.pec |= rr <= R_CORE`; `graded_black_shell`
writes `σ` for `rr >= R_CORE`. The sets overlap on cells at exactly
`rr = R_CORE`. I counted them: **12 cells** at both radii, i.e. `1.9×10⁻⁴` of
the r=156 shell and `1.2×10⁻⁴` of the r=234 shell. PHOTONICS' §4.11 calls this
"the innermost ring," which overstates it by ~3 orders, and leaves the
alternative open. It closes cheaply: those cells sit at the shell's inner
face, where the intensity has already been attenuated by `exp(−τ_true) =
2.6×10⁻⁴`, so their contribution to a relative `Δσ_abs` is
`~(12/98,740)×2.6×10⁻⁴ ≈ 3×10⁻⁸` — **five orders below** the smallest measured
delta, even allowing a 4× standing-wave enhancement at the PEC face. The
construction artifact is therefore **ruled out**, not merely unaddressed. M9
should say what the perturbation actually is and carry this bound.

---

## 2. Audit of each Phase-2 critique

### 2.1 PHOTONICS — support-with-changes

**Confirmed, by my own recomputation:** the identity bit-exact; every M5 band
edge; `k`, `G_ref`, `(2100/1400)²=2.25`, `1+ln 2.25/ln 1.5 = 3.0` exactly,
`R_DEG`, `ε(2.0)`, the constant-ε model figure. §4.2's coherence correction
(RT-1). §4.3's common-mode floor (RT-2) and its correct rule-compliance call
(R13 is a *mislabel* here — `σ_ext ≈ 1093` has no zero-crossing — while **R30**
is the live rule on an uncalibrated threshold cited evidentially). §4.5's
reproduction of `I_graded = 0.273840` / `τ_true = 8.258813` — I reproduce both
to the same digits. §4.6's "six box radii" overclaim. §4.7's 1.29%
refutation. §4.8's 4.47% early-window figure and its R17 sign conflict. §4.10's
three-λ table — I recomputed `I_graded` and `τ_true` at cpl = 18.75/25/31.25
and reproduce `0.214594/0.273840/0.327804` and `8.6293/8.2588/7.9091` **to
every digit quoted**, including `2·exp(−τ)` = `3.58/5.18/7.35 ×10⁻⁴` and the
2.05× red-vs-blue ratio. This is the most thoroughly re-derivable critique of
the five.

**§4.5's strengthening is right and I promote it to a mandatory fix.** The two
family members are the **same optical article by construction, not
coincidence**: `σ_max·cpl = 0.5×20 = 0.4×25 = 10` (identical loss tangent) and
`τ_true = 2·2π·(thickness/cpl)·I_graded = 2·2π·2.4·I_graded` at both (48/20 =
60/25 = 2.4 λ). Recomputed: `τ_true = 8.258813` at **both** members,
bit-identical. Idealization 9's concavity hedge is moot.

**REFUTED — §4.4's headline backscatter figures are inadmissible.** PHOTONICS'
`3.6%–11.3%` local deviations over `|θ| ≥ 135°` reproduce exactly from
exp-112's committed arrays (I get `0.0356 … 0.1128`, max at `−168.75°`, ratio
to peak-normalized `753×`, 16/48 bins above 1%, 24/48 above `1.6×10⁻⁴` — every
figure confirmed). **But exp-112's own committed, R13-mandated mirror-pooled
floor gate marks 0 of those 12 backscatter bins as resolved**, and 14 of the
16 bins exceeding 1% locally are `UNRESOLVED-BY-CONSTRUCTION`; the two that
*are* resolved read 1.37%/1.38%, and exp-112's own max resolved `local_rel` is
`0.013986` at `+123.75°`. Citing floor-failing bins with evidentiary language
("a channel that demonstrably moves by 11%") is the exact R13/R14/R30 shape
this program has fired on repeatedly. PHOTONICS' *conclusion* survives on
admissible data — exp-110's floor-gated r=312 reading gives `0.0529`/`0.0523`
at `±138.75°`, resolved, inside the observer-return hemisphere — so the
constraint-2 exposure is real, but the docket must adopt QUANTUM's numbers,
not PHOTONICS'.

**Overstated — §4.11.** See RT-16: 12 exact-radius cells, not a ring, and
quantitatively closable at `~10⁻⁸`.

**`2·exp(−τ)` vs `exp(−τ)` — adjudicated, and it is not a real conflict.**
PHOTONICS writes `2·exp(−τ_true)`; EM, THERMODYNAMICS, QUANTUM and VISION
write `exp(−τ_true)`. Both are the same *functional form*; the factor 2 is the
cross-term coefficient in `2Re(A*δA)/|A|²` and is the correct form of an
**upper bound** (`|2Re z| ≤ 2|z|`), while `exp(−τ_true)` is the correct
**characteristic scale**. PHOTONICS is the more precise of the five. Adopt
both, stated as bound and scale (MF-1). Nothing turns on the factor 2: the
proposal's error is `3.86×10³`.

### 2.2 ELECTROMAGNETISM — support-with-changes

**Confirmed:** A1's identity plus its `round()` caveat (`STEPS =
round(3200·κ·1.25)` is exact at both κ — `8000`/`12000` verified in exp-114's
own committed `geom`; written as `≡ kappa_ratio × G` it is a numerical
property of these two geometries presented as a construction identity, and
one asserted line discharges it). A3's ordering algebra — I re-derived both
orderings independently and obtain EM's lags exactly. A4's `2.427%` headroom
and every band figure. A6's four-state M6 gap. A7's derivation from
`lab/sections.py` — the algebra is right and the numerics confirm it exactly.
A9's tautology. A10's near-field mischaracterization. A11(i) 1.29%; A11(ii)
5.70% (the same datum as PHOTONICS' 4.47% and THERMO's 6.05%, with three
different denominators — no conflict). A12(2) the signature mismatch; A12(3)
the assert/skip conflict; A12(5) the channel×resolution confound; A12(6)
`R_COAT = 292` from banker's rounding of 292.5, `R_COAT/r = 1.24786` vs
`1.25`, thickness `292−232 = 195−135 = 60` exactly — all verified from the
committed `geom`. A5's R33-addendum-(a) exposure, and the genuine
`combine_control_readings` conflict (it selects the **lower** `speed_ratio`,
not "sustained," while M8 argues at length for "sustained").

**REFUTED — A9's own proposed fix contradicts A7.** EM recommends promoting
`σ_ext_cross` to "the third channel," citing `Δσ_ext_cross/σ_ext_cross =
5.204371×10⁻⁵` against `Δσ_ext = 5.204381×10⁻⁵` as an agreement "to 2 ppm"
that is "a real cross-check." It is not. A7's own derivation proves
`σ_ext_cross − σ_ext` is scene-independent, so the two **absolute** deltas are
bit-identical — I get `−0.05690973269292954` for both, and
`Δσ_ext_cross − Δσ_ext = 0.0` exactly. The "2 ppm" is nothing but the
difference between two normalization denominators. `σ_ext_cross` carries
**zero** independent information about the differential. A7 is right and A9's
remedy is void; adopt the wording fix instead (MF-13).

**Adopted with a correction — A3's ABBA remedy.** The algebra is right; the
recommendation is incomplete. See RT-6: ABBA destroys the equal-lag same-grid
drift readings that ABAB provides and that THERMODYNAMICS' own remedy
depends on.

### 2.3 THERMODYNAMICS — support-with-changes

**Confirmed:** the whole §A reproduction table (I spot-checked every
load-bearing row and every one reproduces); §1's exponent correction and its
exp-028 corroboration; §2's (b)-vs-(c) contradiction; §3's common-mode floor
(sign differs from mine by operand order only — immaterial); §4's
peak-normalization finding and the fact that `peccored32` was never persisted,
so the claim is not checkable from the record (an R16-adjacent gap); §6's
`6.046%` / `4.467%` and the decisive point that `run_control()` runs
short-then-sustained with no counterbalance, so `R_DEG` conflates duration
with elapsed position **by construction**; §9(a) 1.29% and §9(b) 8.83%;
§10's per-scene-persistence and machine-state recommendations; §11's settling
argument — verified from `COURANT_FRAC = 0.32`, `S = 0.2263` cells/step: at
3334 steps the wavefront reaches ~65% of the r=156 domain and ~47% of the
r=234 domain, so no settled ledger is computable and the metrics-table row is
genuinely N/A, which the proposal never says; §11's memory/L3 argument and the
exclusive-use requirement.

**CORRECTED — §7's headline overstates by asymmetric application.** THERMO's
table (`C = 0`, `17.54`, `35.08` s/scene ⇒ `rel_dev = 0.1227`, `0.2123`,
`0.3174`) reproduces exactly, but it applies a **grid-independent** warm-up
constant `C` to the r=156 **denominator only**. Applied consistently to both
grids — which is what "grid-independent" means, and the numerator is a
12000-step average, so `C/12000` is not zero:

```
C = 35.079 s/scene, both grids:  p156 = 0.0606886, p234 = 0.1925847
                                 G = 3.1733, measured_ratio = 4.7600
                                 rel_dev = 0.2977   →  AMBIGUOUS
```

So the axis spans **CONFIRM → AMBIGUOUS (touching, not crossing, the 0.30
REFUTE line)**, not "CONFIRM → REFUTE." THERMO's own qualifier ("a bounding
sensitivity, not a correction") is correct; the headline sentence is not. The
substantive finding — that this axis is at least as wide as the v2 straddle
and was previously unnamed — survives, corrected.

**Internal conflict, flagged:** §8 demands ABBA and §8 also demands `d_156` /
`d_234` be used as same-grid drift readings and M3/M4 re-anchored on them.
Under ABBA those two readings carry lags of `a+2b` and `b` (≈6.5u vs 2.75u) —
not comparable. See RT-6; the fix is to report drift as a rate.

**Adopt-with-verification — §5's MP-5 thermal counterweight.** I did not
re-derive exp-061's `ΔT_ss` table this session; the recommendation is sound in
mechanism (`h_eff = k_air/L` falls as `L` grows, so the optical benefit and
the IR-detectability cost are the *same* physical change) and the Director
should verify the two rows against exp-061's NOTES before quoting them.

### 2.4 QUANTUM OPTICS — support-with-changes

**Confirmed:** A1's independent route to the identity (`HISTORICAL_PER_STEP_S
≡ HIST_TOT/24000`, so `HIST_TOT` cancels *identically*, not approximately —
verified, and QUANTUM is right that this is the non-obvious part and that a
future cycle supplying a different pilot total breaks it silently); A2's
signature finding; A4's re-derivation of `KAPPA_COST_EXPONENT` from exp-110's
raw per-scene times, and its sharp observation that `k` and `ε` are treated as
functions of `kappa_ratio` while cache/bandwidth superlinearity is a function
of **absolute `N`** (exp-110 spans `N = 1120→2240` at cpl=20; this cycle spans
`1400→2100` at cpl=25) — which is why M7 can only ever be descriptive; A5;
A6; **B1's entire straddle construction, reproduced to every digit** (`v2 =
3.217195628521234`; boundary `G ≥ 2.5652851279677367`; `66.35%` of the CONFIRM
band; `G = 2.8801735` for exact agreement, above the ceiling); B5's
degrees-of-freedom point; B6/B7 on M7; B8's `M(machine)·Grid(g)·Prot(protocol)`
decomposition, which is correct and which is the cleanest statement of why M6
cannot separate a machine factor from a protocol factor with two machines and
one protocol each; **B10's floor-gated local-normalization figures**
(`0.014669070259562213` at r=156 with 34/48 resolved; `0.05290046381280309` at
r=312 with 38/48 — reproduced exactly from exp-110's own `results.json`), and
its correct observation that M9(b)'s floor gate covers only the channels that
do **not** set the headline; B11's caveat-lint mechanics (verified against
`lab/caveat_lint.py:64–68` and `check_caveat()`: trigger terms are
discovery-only and never gate the exit code).

**REFUTED — B9's concavity bound.** QUANTUM claims that at the cpl=25 /
`σ_max=0.4` / 60-cell member, "concavity of `Im(n)` in σ bounds `τ_true ∈
(6.6071, 8.2588)`," giving `exp(−τ) ∈ (2.59×10⁻⁴, 1.35×10⁻³)`, "1×–12× the
measured deltas." This is wrong. `I_graded` depends only on the loss tangent
`σ_max·cpl/2π`, and `σ_max·cpl = 10` at **both** members; `τ_true =
2·2π·(thickness/cpl)·I_graded` and `thickness/cpl = 2.4` at **both**.
Recomputed from `lab/materials._graded_black`: `τ_true = 8.258813` at both,
**bit-identical**. QUANTUM's `6.6071` comes from scaling `I_graded` by
`0.4/0.5 = 0.8` while holding `cpl = 25` — double-counting the `σ_max` change
and ignoring that `cpl` moved with it. Its upper end is inflated by 5.2×.
PHOTONICS' §4.5 has this right.

**REFUTED — B3's "8.926%" and its R17 conclusion.** QUANTUM scene-mix-corrects
its 4.905% within-run figure using the ~14% `peccored` premium that three
other seats refute *in this same cycle*, with `blend/empty = 1.04667`. From
exp-114's own committed per-scene times the real ratio is
`0.19550806899203194/0.19632804773251217 = 0.99582` — the blend is 0.42%
**cheaper** than empty, not 4.67% costlier, because `hollow` is the cheap
scene. The scene-matched figure is **4.467%** (empty-to-empty). So B3's
conclusion — "the largest already-established comparable is 8.93%, not 7.60%,
so M3's DOES-NOT-CANCEL bar is undersized against the record" — collapses: the
corrected comparable is 4.5–4.9%, **smaller** than `R_DEG = 7.60%`. What
survives of B3 is the *sign* conflict and the composite nature of `R_DEG`,
both of which THERMODYNAMICS establishes independently and without the
refuted figure.

**Internal conflict, flagged:** B2 asserts "the magnitude of the extrapolation
is uncertain; **the sign is not**," while B3 (same document) states the only
comparable r=234 datum "runs the other way," and B1 (same document) computes
`2.8802` — the value the opposite-sign model implies, *above* the CONFIRM
ceiling. B2 and B1/B3 cannot all stand as written. The honest reading is
RT-7's: two models, opposite sides of the ceiling, neither validated.

**Adopted in part — B1's M10 proposal.** The computation is right and free.
The *scoring* half is not: `measured_ratio_v2′ = 1.5·G_bench·(p_prod/p_burst)`
composes a bench-measured `G` with exp-114's own session's protocol ratio, so
pre-registering a scored `STRADDLE-CLOSED` verdict assumes the
machine-independence M6 exists to test. Adopt as a persisted, explicitly
NOT-scored sensitivity with the boundary stated (MF-8; see also the
disclosed-override list).

### 2.5 VISION SCIENCE — support-with-changes

**Confirmed:** all twelve reproductions in §4.1 (I recomputed every
load-bearing one and each is exact, including the mean-normalization
requirement on the six deltas). §4.2's margin-scope finding and its R4-second-
addendum framing. §4.3's exponent finding. §4.4's M5-composition gap and its
R17 point about the M5 REFUTE branch's label naming only one of two live
hypotheses. §4.5's four-cut-points/three-labels legibility finding. §4.6,
including the `ε_E/ε_k ≡ measured_ratio/reference_ratio` identity. **§4.7's
R18 finding, reproduced to all 17 digits: `rel_dev = 0.44796720567305326` →
REFUTE.** §4.10(1)'s dual-convention finding (verified both ways).
§4.10(3)'s 82%-vs-90.9%. §4.10(5)'s new-machinery/absolute-identity-gate
point.

**§4.8's caveat-registry findings — independently verified, both blindnesses
real.** I ran `python lab/caveat_lint.py`: **15 caveats checked, 0
required-site failures**, exit 0, with WARNs on this cycle's own documents.
And I tested the `exp061-t18-evidentiary-tier-propagation` triggers directly
against the proposal's text:

```
'PUBLISHED.{0,10}PLAUSIBLE.{0,10}UNOBTANIUM'          → False
 same pattern with 'UNOBTAINIUM' (the spelling PANEL.md itself uses) → True
'alpha.{0,15}(1\.66|1\.667|5\.7|5\.73|5\.74)'          → False
 same pattern with Unicode 'α'                          → True
```

So the one registry entry that has fired Checkpoint criterion 4 **twice in a
single iteration** is structurally unable to discover this document — over a
one-letter spelling divergence between the registry and the charter, and an
ASCII-vs-Unicode divergence. And even a matching trigger would only WARN.
`lab/ARTIFACTS.md`'s own invariant applies verbatim: *a silent gate and an
absent gate produce identical observations.*

**§4.9's constraint-3 drift — verified and adopted; see §4 of this audit.**
`grep -rln "weber(\|contrast_from_runs\|observer_profile" experiments/*/*.py`
returns nothing after exp-100. exp-101 → exp-114 is fourteen consecutive
cycles; exp-115 would be the fifteenth.

**Minor correction — §4.10(2).** "Three orders of magnitude below anything
this instrument can resolve" is indeed two orders (`6.708e−8/6.649e−6 =
0.01009`) against the tightest quoted floor — but the whole comparison is void
under RT-2, since that floor has zero differential content. Non-load-bearing.

**§4.11's assessment of M9(e)'s tier discipline is fair and I do not want it
weakened.** The tier is correctly stated as unchanged, the binding axis named,
the conditionals stated as conditionals. Its three qualifications ("at all" is
stronger than the evidence; the tier disclosure does not travel into the
quoted sentence; `exp052-alpha-60nm-absorptivity-open` bites on "thickness as
the binding constraint") are all correct and are folded into MF-4/MF-14.

### 2.6 Where the critiques conflict — adjudications, consolidated

| # | Conflict | Ruling | Ground |
|---|---|---|---|
| 1 | `2·exp(−τ)` (PHOTONICS) vs `exp(−τ)` (EM/THERMO/QUANTUM/VISION) | **Not a real conflict.** Same functional form; PHOTONICS' factor 2 is the cross-term coefficient and is the correct form of an *upper bound*; `exp(−τ)` is the correct *scale*. State both. | `Δσ/σ = 2Re(A*δA)/\|A\|² + …`, `\|2Re z\| ≤ 2\|z\|` |
| 2 | `τ_true` at the cpl=25 member: exactly equal (PHOTONICS) vs `∈(6.6071, 8.2588)` (QUANTUM) | **PHOTONICS.** Bit-identical at both members. | `σ_max·cpl = 10` and `thickness/cpl = 2.4` at both; recomputed `8.258813` |
| 3 | "~14% costlier `peccored`": refuted (PHOTONICS/EM/THERMO) vs used as a correction factor (QUANTUM B3) | **Refuted, 3–1.** | exp-114 `total_wall_s_by_scene`: 1.29% spread; `blend/empty = 0.99582` |
| 4 | Per-bin local figures: `11.3%` ungated cpl=25 (PHOTONICS) vs `1.47%`/`5.29%` floor-gated cpl=20 (QUANTUM) | **QUANTUM's are admissible; PHOTONICS' are not.** Same conclusion, different route. | exp-112's own gate marks 0/12 backscatter bins resolved |
| 5 | M3's anchor: `8.93%` and "bar undersized" (QUANTUM) vs `4.47–6.05%` (THERMO/PHOTONICS/EM) | **The latter.** `R_DEG = 7.60%` is the largest on file; the bar is not undersized. The *sign* conflict stands. | corrected scene-mix arithmetic |
| 6 | Run order: three seats say ABBA; none prices it | **Adopt ABBA with additions.** It cancels linear drift in the mean; it also destroys the equal-lag same-grid drift readings M3's own question needs. | lags `a+2b` vs `b` under ABBA; `a+b` vs `a+b` under ABAB |
| 7 | THERMO's warm-up axis "CONFIRM → REFUTE" | **CONFIRM → AMBIGUOUS (0.1227 → 0.2977).** | symmetric application of a grid-independent `C` |
| 8 | EM's A7 (`σ_ext_cross` is common-mode) vs EM's A9 (promote it as a third channel) | **A7.** `Δσ_ext_cross ≡ Δσ_ext` bit-identically. | `−0.05690973269292954` for both |

---

## 3. Mandatory-fix docket

Every item is **zero-FDTD and zero grid-steps** unless marked otherwise. None
changes the cycle's 18-call, 46,008-grid-step budget. Cost column: `desk` =
prose/JSON only; `code` = a code change with no new `Sim.run()` call;
`protocol` = a change to how the six scheduled readings are taken.

| # | Fix | Cost | Consolidates |
|---|---|---|---|
| **MF-1** | Replace M9(c)'s `exp(−2τ_true)` with the coherent cross-term form: state the scale `exp(−τ_true) = 2.5896×10⁻⁴` **and** the upper bound `2·exp(−τ_true) = 5.1793×10⁻⁴`. Strike "the physical value is predicted at `O(10⁻⁷)`" from M9(d). Correct M9(e)'s forward scaling to `exp(−τ_true)` (still exponential, half the exponent). Replace Idealization 9's concavity hedge with the exact identity (`σ_max·cpl = 10`, `thickness/cpl = 2.4` ⇒ `τ_true` bit-identical, recomputed `8.258813` from `lab/materials._graded_black`); do **not** adopt QUANTUM's `(6.6071, 8.2588)` bound. Add PHOTONICS' 3λ row (`2·exp(−τ)` = `3.58/5.18/7.35 ×10⁻⁴` at 450/600/750 nm; backing freedom weakest in the red, measured only at 600 nm). | desk + code | PHOTONICS §2/§4.2/§4.5/§4.10, EM A8, THERMO §1/§2, QUANTUM B9(partial), VISION §4.3 |
| **MF-2** | Withdraw M9(b)'s floor gate. Persist the derivation and the numbers showing `σ_ext_cross − σ_ext` is scene-independent (`0.0` exactly at r=234, `2.27×10⁻¹³` at r=156) and label it a solver self-consistency statistic, never a differential floor. Substitute exp-108's `item_ii` six-margin differential family as the only differential floor on file (`mean/std = 4.46×` at r=156, `11.70×` at r=312) and state explicitly that **no differential floor exists at r=234**. Rewrite (b)'s conclusion accordingly: on the only differential floor available the effect is resolved, not floor-limited. | desk + code | EM A7, THERMO §3, PHOTONICS §4.3, QUANTUM A6/B10 |
| **MF-3** | M9(d) must report the floor-gated **local** normalization from exp-110's own `classify_item_i_local` — `1.4669×10⁻²` (r=156, 34/48 resolved) and `5.290×10⁻²` (r=312, 38/48) — alongside the peak-normalized `1.5266×10⁻⁴`, and must state that the two largest resolved r=312 deviations sit at `±138.75°`, inside the observer-return hemisphere PANEL.md scores constraint 2 on. The per-bin half of the "better than `1.6×10⁻⁴`" claim is **withdrawn**. Do not cite exp-112's ungated bins (0/12 backscatter bins resolved). | desk + code | QUANTUM B10, PHOTONICS §4.4 (conclusion only), THERMO §4, VISION §4.2 |
| **MF-4** | Restate M9(d) at the resolution its evidence certifies: margin=32 only for the tight figure, `≤5%` (a *decision bar*) at the other five; per-bin at cpl=20 only, aggregate at cpl=25 only (channel and resolution confounded); aggregate-only at r=234. Strike "far-field" → "near-to-mid-field box-ledger, at this bench's measurement geometry"; strike "at all" → "over the vacuum-to-PEC range tested at 600 nm, normal incidence, 2D TM." Move the constraint-3-failure sentence, the realizability tier, and the T18 evidentiary tier **inside** the quotable blockquote. | desk | VISION §4.2/§4.11, PHOTONICS §4.6, EM A10/A12(5)/R21 row, QUANTUM §D |
| **MF-5** | Fix M5's invocation: `exponent_B = ln(1.5·G_sustained)/ln(1.5)`; call `classify_kappa_exponent_check(exponent_B)`; code-assert `abs(result["measured_ratio"] − 1.5·G_sustained) < 1e-12`. | code | VISION §4.7, EM A12(2), QUANTUM A2 |
| **MF-6** | **Protocol integrity of the six readings — irreversible once Phase 4 starts.** (a) Reorder the sustained pass to **ABBA** (`U156, U234, U234b, U156b`); score M2/M5 on the mean of the two pairwise `G` values. (b) Persist per-reading start/end wall-clock timestamps, per-scene wall times, and both pairwise `G`s. (c) Report same-grid drift as a **rate per unit elapsed time** (ABBA makes the two same-grid lags unequal, `a+2b` vs `b`). (d) Restate `d_rep`'s semantics — under ABBA it is a drift+noise statistic, not a repeatability statistic — and re-justify every composition rule that consumes it. (e) State and enforce an **exclusive-use protocol** on the bench for the duration of the readings (no concurrent trust-suite run, no second SSH session, no `analyze115.py`), and persist a machine-state block per reading (`lscpu`/L3, THP setting, BLAS/OMP thread count, `loadavg` before and after). | protocol + code | EM §2/A3/A12(4), THERMO §8/§10(i)/§11, QUANTUM B4, RT-6 |
| **MF-7** | M5 gets a coded composition rule and a stated power limit. (a) Persist a protocol-mismatch **interval** from the two-point `p = p_∞ + C_g/n` relation on each grid (`S` and `U` are the two points; exactly determined, so it *bounds*, it does not fit — R7); if the interval spans a band boundary, persist `m5_protocol_caveat = True` and report **BOUNDED-REPLICATION**, not a verdict that can move exp-114's LOGBOOK entry. (b) State in Result prose that pure `N²` scaling (`k = 3.0`, the pre-R28 exponent) gives `rel_dev = 0.0799`, **inside** the CONFIRM band, so a CONFIRM does not distinguish `k = 3.2053` from `k = 3.0`. (c) Pre-register, before the run, the two protocol models' opposite-side predictions (`G ≈ 2.540` vs `G ≈ 2.868–2.880`). | code + desk | EM A4, VISION §4.4, QUANTUM (d)/B2, THERMO §7, RT-7 |
| **MF-8** | Withdraw "resolves the straddle" from §1 and the M6 title. Persist `sensitivity_v2_with_measured_G_DO_NOT_SCORE = 1.5·G·0.9532431491914767` with its **signed** deviation and the stated boundary `G ≥ 2.5652851279677367`, explicitly NOT scored. Add a numbered §3 decline for the un-executable half of the Iteration-92 queue's Tier-1 item 1 ("re-score `kappa_exponent_result` against the corrected denominator"): the cross-session half dissolves under the §1 identity, and the burst-vs-production half is not measurable without an r=234 production leg. | desk + code | QUANTUM B1/M10, EM A2, RT-11 |
| **MF-9** | Reduce every composition rule to one persisted, code-asserted boolean: `m3_scored = (not repeat_skipped) and (d_rep <= R_DEG/2)`; `m5_protocol_caveat`; `m6_directional_only = (m3_verdict != "CANCELS")` — inverting the current 1-of-4-state rule; `m7_underpowered`. Split M4's MARGINAL at `0.03` and `R_DEG/2` so the label carries its consequence. Make the 18-call assert conditional on `repeat_skipped`. Make M3's labels mechanism-neutral ("`G` is / is not duration-invariant"), since the mechanism name is unvalidated and contradicted in sign on file. | code | EM A6/A12(3), VISION §4.5, THERMO §6/§10(ii), QUANTUM B7, RT-12/13/14 |
| **MF-10** | Write `DISCLAIMER_115`'s **text** in the Phase-3 document (Phase 2 cannot review a string it has not seen), with both predictions-side and result-side asserts in committed, re-invocable call sites (R23 First Addendum — a third instance of the asserted/unasserted asymmetry auto-fires Checkpoint 4). Minimum content: analytic-sidecar-not-FDTD; upper-bound-vs-resolved; **the article fails constraint 3 by construction**; the T18 evidentiary tier; and an explicit **energy-ledger / thermal-sidecar N/A** sentence carrying THERMO's settling reason (at 3334 steps the wavefront reaches ~65% of the r=156 and ~47% of the r=234 domain, so no settled ledger is computable) — which also closes exp-104's own named, three-cycle-old "THERMODYNAMICS thermal-sidecar-N/A sentence" gap. | code + desk | THERMO §11/§12, VISION §4.10(6), QUANTUM C(R21/R23) |
| **MF-11** | Correct the three non-reproducing citations: "~14% costlier" → the profiled `+1.287%` (peccored/hollow) and `+0.009%` (peccored/empty); Idealization 4's "≲5%" → the measured `8.83%` chunk spread **plus** the statement that chunk scatter does not bound the `4.47%` within-run level shift; "three independent energy-ledger channels" → "two independent channels and their exact algebraic sum" (do **not** adopt EM's A9 promotion of `σ_ext_cross`). Disclose the M9(a)/(b) normalization conventions (mean-normalized numerators, `peccored`-normalized floors). | desk | PHOTONICS §4.7, EM A11(i)/A9, THERMO §9, VISION §4.10(1), RT-8/RT-9 |
| **MF-12** | Add an **absolute identity gate on the new machinery** (PANEL.md's own Phase-4 house rule): assert that `chunk_runner115`'s parameterized `_time_control_blend` at `r=156` constructs a scene set identical to `chunk_runner114._time_control_blend()` (same geometry dict, same three scenes, same source spec), executed before any reading is trusted. Separately, re-run the trust suite **on the bench** and commit the console record with platform and numpy version (`VALIDATION.md` docket-14) — the "41/41 in 87 s" figure currently has no committed artifact. | code | VISION §4.10(5), THERMO §10(i)/Trust-suite note |
| **MF-13** | Disclose what the perturbation actually is: vacuum → PEC over `rr ≤ R_CORE`, with **12 cells at exactly `rr = R_CORE`** both PEC-zeroed and maximally lossy; carry the bound that closes PHOTONICS' alternative (`12/98,740` shell cells at `exp(−τ_true)`-attenuated intensity ⇒ `~10⁻⁸` relative, five orders below the smallest measured delta). | desk | PHOTONICS §4.11, RT-16 |
| **MF-14** | Fix the two caveat-registry blindnesses (`UNOBTANIUM`/`unobtainium` spelling alternation; ASCII `alpha` / Unicode `α`), add a `caveat_lint_config.json` entry for **this cycle's own** tolerance bound with the certified-resolution wording as its required phrase and this cycle's documents in `required_sites` (so the claim is gated, not merely warned), and add a T18 disclosure at §2.0's own `τ_true` row where the exp-061 verdict is restated. | code + desk | VISION §4.8, QUANTUM B11 |
| **MF-15** | Carry exp-061's own MP-5 thermal counterweight into M9(e)'s forward conditional (230×/730× thickness ⇒ `ΔT_ss` margins `3.79×`/`1.35×` vs NETD-lo), verified against exp-061's NOTES before quoting, and state that the same thickening makes the article a physically larger black silhouette — constraint 3's own failure mode. If THERMO's §7 warm-up sensitivity is reported at all, report it under **consistent** application: `rel_dev` spans `0.1227 → 0.2977` (CONFIRM → AMBIGUOUS), not CONFIRM → REFUTE. | desk | THERMO §5/§7/§13, RT-7 |

### Disclosed-override candidates — fixes I recommend the Director DECLINE

| # | Requested by | Recommendation | Reason |
|---|---|---|---|
| **OV-1** | QUANTUM (M10, as a **scored** `STRADDLE-CLOSED`/`STRADDLE-OPEN` verdict) | **Decline the scored half**; adopt the computation as a NOT-scored sensitivity (MF-8). | It composes a bench-measured `G` with exp-114's own session's `p_prod/p_burst`. Scoring it presumes the machine-independence M6 exists to test — assuming the answer. |
| **OV-2** | PHOTONICS ("if the seat declines the change, defer item 5 an **eighth** time") | **Decline the deferral branch.** | The changes are being adopted (MF-1..MF-4), so the bound ships corrected. A corrected bound is strictly better than an eighth deferral, and PHOTONICS' own framing ("a deferral is a debt; a false bound is a liability") supports shipping the corrected version. |
| **OV-3** | THERMODYNAMICS (§7: "discard the first ~1000 steps — `sim.run(1000)` untimed, then `sim.run(2334)` timed") | **Decline as the primary protocol**; permit as one extra, labelled reading if the Director wants it. | It changes the recipe away from `chunk_runner114::_time_control_blend`, breaking matched-protocol comparability with every prior R31 reading and with the bench-native R31 artifact this cycle also exists to produce. MF-7(a)'s two-point `C_g` bound extracts the same information from the readings already scheduled. |
| **OV-4** | EM (A9: promote `σ_ext_cross` to a third channel) | **Decline.** | Refuted by EM's own A7: `Δσ_ext_cross ≡ Δσ_ext` bit-identically; the "2 ppm agreement" is a normalization artifact. Adopt MF-11's wording instead. |
| **OV-5** | QUANTUM (B9: `τ_true ∈ (6.6071, 8.2588)`) | **Decline.** | Refuted numerically; the two family members are the same optical article by construction. Adopt PHOTONICS' exact identity (MF-1). |
| **OV-6** | QUANTUM (B3: re-anchor M3 on `8.93%`) | **Decline the magnitude; adopt the sign finding.** | The 8.93% inherits the refuted ~14% figure; corrected it is 4.47–4.91%, smaller than `R_DEG`. The sign conflict is real and is carried by MF-9's mechanism-neutral labels. |

*Not an override, stated so it is not read as one:* EM/THERMO/QUANTUM's ABBA
reorder is **adopted**, not declined — but only in MF-6's fuller form. A bare
ABBA is a partial fix that silently repurposes the cycle's only null channel.

---

## 4. Constraint-3 / program-integrity ruling

### 4.1 What does NOT fire

Checked element-by-element against each rule's own operative text:

- **R20** — tally 3 (RT-8) plus two scope overclaims, but every one is
  pre-freeze and caught at Phase 2. R20's own condition is "surviving a
  document's own Phase-3 prediction-freeze into its Result/Learned sections,
  each caught only at Phase 5 — not earlier." **Does not fire.** Named as a
  standing observation: this is the sixth consecutive cycle at or just under
  R20's density bar (exp-108 through exp-112 each tallied 1–2).
- **R24** — nothing has yet been claimed "adopted in full." **Does not fire**;
  MF-9 exists to keep it that way at Phase 3.
- **R25** — §3's declines are properly numbered queue lines with stated
  reasons, including item 3's genuinely new one. The one missing decline
  (EM's A2, the queue clause's second half) is queue-authorship fault under
  R25's own text and is added by MF-8. **Does not fire.**
- **R13** — invoked by M9(b) but not triggered (`σ_ext ≈ 1093` has no
  zero-crossing). A mislabel, not a violation. **R30 is the live rule** on
  that gate (an uncalibrated threshold cited evidentially, whose calibrating
  data already exists); MF-2 discharges it. R30's forward-firing clause
  concerns *citing* such a reading evidentially — which has not happened yet,
  because this is Phase 2. **Does not fire.**
- **R32** — no directional discriminating statistic in item 1. M3's *labels*
  assert an unvalidated mechanism direction (THERMO §6 is right); MF-9's
  mechanism-neutral wording discharges it pre-freeze. **Does not fire.**
- **R23 First Addendum** — the proposal commits to both asserts (§8). MF-10
  requires the text and the committed, re-invocable call sites in the same
  cycle. **Does not fire**, and must not be allowed to: a third instance
  auto-fires.
- **R27/R28** — §6's gate is executable, branches, and is traced upstream of
  each `Sim.run()`, with the degradation branch spending the *repeat* rather
  than the primary. Two seats independently confirm; I confirm by inspection.
  **Does not fire.** (Recommended, not mandatory: a `SUSTAINED_CONTROL_STEPS`
  step-down branch so degradation is graceful at both ends — THERMO §12.)
- **R29** — module naming and executed identity asserts committed. **Does not
  fire.**
- **R31/R33** — M5 is genuinely R33-immune by construction; I verified the
  identity independently and it holds bit-exact. Addendum (a)'s exposure is
  real (two same-session sustained readings, one pre-committed for scoring)
  and MF-6/MF-9 discharge it pre-freeze. **Does not fire.**

### 4.2 What DOES fire — Checkpoint criterion 4, at PROGRAM level, not on this proposal

**Criterion 4 FIRES**, on the narrow, verifiable ground that **PANEL.md's own
metrics section no longer describes the program it governs.**

Grounds, each independently verified this session:

1. PANEL.md lines 138–151 read "**Metrics — recorded every run**" and "Both
   ambient regimes are **recorded every run**. … VISION SCIENCE pins the
   numeric pass/fail thresholds per experiment, cited, before the run."
   exp-115 records **zero of the seven rows**.
2. `grep -rln "weber(\|contrast_from_runs\|observer_profile"
   experiments/*/*.py` returns nothing after **exp-100 (Iteration 77)**.
   exp-101 → exp-114 is **fourteen consecutive cycles** with no constraint-3
   number; exp-115 would be the fifteenth.
3. The de facto amendment exists only as a per-cycle `DISCLAIMER` string
   replicated across ~14 files (`run114.py:301–306` and siblings) — never in
   the charter a fresh seat reads first. A governing document that promises a
   reader something the program has not done for fourteen cycles is,
   structurally, the "quietly dropped" condition criterion 4 names, even
   though every individual cycle disclosed its own scope honestly.
4. Two of five blind seats raised it independently: VISION §4.9 (with the
   grep, the PANEL.md text, and the diagnosis that "**Tier order is the
   mechanism by which constraint 3 slips** — each cycle's Tier 1 is
   manufactured by the cycle before it") and QUANTUM §D (Iteration 92 is the
   **12th consecutive** cycle declaring "T1 escape route: NONE"). VISION
   explicitly declined to fire it on the proposal and named it "a
   program-level finding for the Director and Red Team." I am the Red Team.
   I rule.
5. The asymmetry is on the record: Tier-1 item 5 (MATERIALS' fabrication debt)
   received an explicit "an eighth silent cycle should not happen without an
   explicit Director decision to keep deferring, stated as such" — and is
   being paid this cycle, correctly. Tier-3 item 10 (VISION's re-score of the
   program's only-ever Tier-W/Tier-A constraint-3 citation, unrun since
   Iteration 12) has never received that treatment.

**Ruled a NOTIFICATION, not a pause** — this program's unbroken precedent, and
nothing here touches `lab/`, the trust suite, any frozen verdict, or any
engine physics. **This firing is explicitly NOT a block on exp-115.** Item 1 is
cheap, correctly ranked #1, executed in queue order, and should run.

**Discharge — two items, both zero-cost, both verifiable by the next
iteration's Red Team audit:**

- **D1.** Amend PANEL.md's Metrics section so the charter matches practice:
  state that instrument-fidelity/governance cycles on the T28 sub-thread
  record none of the seven rows and declare T1 N/A, and that the "recorded
  every run" language binds phenomenon-program cycles. Whichever way the
  Director rules, the charter and the practice must agree.
- **D2.** An explicit, on-the-record Director decision on Tier-3 item 10 —
  either "Iteration 93's lead" or a stated reason for continued deferral —
  recorded in the Iteration-92 close, matching exactly the standard applied to
  item 5.

Under **R34**, this firing self-closes the moment the next iteration's Red
Team final audit confirms D1 and D2 discharged from primitives; Marsh is
convened only if either is still undischarged after that audit.

**A companion program-integrity observation, not itself a firing.** MF-14's
caveat-registry blindnesses mean the entry that has fired criterion 4 twice
cannot see this document, and `lab/caveat_lint.py` never gates on discovery
in any case. Fifteen registry entries exist, the newest founded at exp-071;
forty-three subsequent experiments have added none, across which R23-First-
Addendum and R30–R33 were all adopted. That is the same "a silent gate and an
absent gate produce identical observations" shape, and MF-14 is the cheap fix.

---

## 5. VERDICT

# PROCEED-WITH-MANDATORY-FIXES

**Item 1 (Block CG) should run.** The `measured_ratio ≡ kappa_ratio × G`
identity is real, load-bearing, previously unnoticed by every seat including
this one, and I reproduce it bit-exact. It converts a contested cross-session
normalization dispute into a single same-session grid ratio that six cheap
readings can measure directly, it is genuinely R33-immune by construction, and
it can confirm or refute a filed CONFIRM for ~40–100 minutes of bench time. The
scope discipline is real: exactly one falsifiable FDTD question, numbered
declines per R25, an executable upstream gate that spends the *repeat* rather
than the primary. Five blind seats support it and I find nothing in §1 that
touches it.

**Item 5 (M9) must not ship as drafted** — but must not be deferred an eighth
time either. Corrected per MF-1..MF-4, it becomes what seven cycles have asked
for: one stated, falsifiable, correctly-scoped fabrication-tolerance bound with
a named realizability tier.

### The five load-bearing fixes

1. **MF-1 + MF-2 — the physics.** `exp(−2τ_true)` is the wrong functional form
   (wrong by `exp(+τ_true) ≈ 3.86×10³`), and M9(b)'s floor is bit-identically
   common-mode between the two scenes being differenced (`0.0` exactly at
   r=234). Together they are the difference between publishing "floor-limited,
   physics at `O(10⁻⁷)`" and publishing "resolved at 4–12× on the only
   differential floor on file, physics at `O(10⁻⁴)`" — in the sentence R21
   sends into LOGBOOK for future cycles to quote.
2. **MF-3 — the per-bin channel.** M9(d)'s "insensitive at better than
   `1.6×10⁻⁴`" is refuted by **99×** (r=156) and **347×** (r=312) on this
   program's own floor-gated, R13-compliant instrument, and the two largest
   resolved r=312 deviations sit at `±138.75°`, inside the constraint-2
   observer-return hemisphere.
3. **MF-5 — the M5 invocation.** As documented, executed literally, it returns
   `rel_dev = 0.44796720567305326` → **REFUTE**. A false verdict on the
   declared falsifiable heart, invited by the document's own text.
4. **MF-6 — protocol integrity of the six readings.** The only fix on this
   docket that is *not* correctable after Phase 4 starts: A,B,A,B leaves a
   same-signed `(a+b)/2` lag in every pair while `d_rep` reads ≈0, and an
   uncontrolled concurrent process on a shared team bench invalidates every
   reading of a measurement whose entire product is wall time.
5. **MF-7 — M5's power limit.** Two defensible protocol models put `G` on
   opposite sides of the CONFIRM ceiling (`2.540` vs `2.868–2.880`), and pure
   `N²` scaling (`k = 3.0`) lands *inside* the CONFIRM band at `rel_dev =
   0.0799`. Without a pre-registered protocol-mismatch interval and an
   explicit statement of what M5 cannot decide, a CONFIRM would be
   over-read as portability evidence it does not carry.

**Narrowly missed the cut and must not be read as optional:** MF-10
(`DISCLAIMER_115`'s text plus both asserts — a third instance of R23's
predictions/result asymmetry auto-fires Checkpoint 4) and MF-8 (withdraw
"resolves the straddle"; 66.4% of M5's own CONFIRM band leaves it open).

**Checkpoint criterion 4 fires** at program level (§4.2), ruled a
notification, not a pause, with a two-item zero-cost discharge and R34
self-closure. It does not block this cycle.

---

*RED TEAM, Phase 2, exp-115. Worked alone: no sub-agents, no delegation, no
simulations, no git state changed. Every figure above was recomputed this
session in pure python against committed JSON and committed source, or
re-derived from primitives; none is restated from the proposal's or any
critique's prose.*
