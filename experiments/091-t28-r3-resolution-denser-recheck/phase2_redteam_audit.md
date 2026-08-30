# PHASE 2 — RED TEAM FINAL AUDIT · Panel Iteration 68 · exp-091
## "R3 Resolution & Denser Recheck"

Red Team reads everything: `phase1_proposal.md` plus all five blind Phase-2
critiques (PHOTONICS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS,
VISION SCIENCE). Scope note, matching every T28 desk/instrument cycle's own
Red Team audit since exp-069 (069/087/088/089/090): this is a zero-mechanism
instrument-recalibration cycle, T1 route N/A, Checkpoint criterion 2 N/A. The
charter's four attack tags are adapted accordingly, per this sub-thread's own
established convention (exp-090 `phase2_redteam_audit.md` intro, reused
verbatim): `constraint-#N-violation` would cover a misstatement of a standing
R-rule or the LOGBOOK record; `unfalsifiable` in its literal sense — a stated
claim, prediction, or falsification condition that cannot be checked against
data or cannot fire; `inconsistency` covers internal contradiction and
failure to carry an already-disclosed caveat forward; `inexpressible` does
not apply anywhere in this cycle (every quantity is concretely FDTD- or
desk-computable) and is not used below. **No `constraint-#N` tag is used in
this audit** — reasoned explicitly, not by default: this cycle makes no
phenomenon-mechanism claim (§3 states this plainly and correctly), so there
is no constraint-1–4 behavior to violate. This matches the task brief's own
expectation and every prior T28 desk-cycle Red Team audit's own scope note.

## 0. Independent verification performed (before adjudicating anything)

I did not take any of the five critiques' claims, or the proposal's own
numbers, on faith.

- **Re-derived the proposal's own §2b table from primary sources**, not from
  the proposal's citation of it. `experiments/089-t28-combined-angle-census/
  NOTES.md` and its `results.json` give, bit-exact: FLOOR-margin 37.2°
  2.1709×, 40.2° 1.4764×, 41.4° 1.3095×; crossing distances 40.2° 0.0654°,
  41.4° 0.0609° (from the true crossings at 40.265°/41.461°, linearly
  interpolated on exp-083's own 31-point window). Both match the proposal's
  §2b table to the digit.
- **Independently re-derived `delta_scene(θ)` from `experiments/083-t28-
  pad-article-full-power-retest/results.json::per_theta`** directly (not
  from any later citation): 37.2° `+2.348254×10⁻⁴`, 40.2° `−1.540815×10⁻⁴`,
  41.4° `+1.337362×10⁻⁴` — bit-exact to the proposal's §2b table, and to
  `frac_contrast_of()` (`experiments/088-.../run.py:96`, `=|delta_scene|/
  |C40_C|`) applied to the same rows: 4.162655×10⁻⁴ / 2.830881×10⁻⁴ /
  2.510967×10⁻⁴ — bit-exact.
- **Re-derived FLOOR from its own defining code** (`experiments/088-.../
  run.py::compute_floor`): `FLOOR_FRAC=0.10`, `RMS=1.91744×10⁻³` over
  exp-083's 31-point window ⇒ `FLOOR=1.91744×10⁻⁴` — matches.
- **Read `lab/fdtd2d.py::Sim._damping`/`experiments/069-.../design_
  geometry.py::r3_config` directly**, not the proposal's paraphrase of them,
  to check the geometry-rescale claims in §2a: confirmed `_damping` is a
  pure function of the `absorb` parameter alone (zero `nx`/`ny`/`pad`
  dependence — `PAD` is provably lossless vacuum, the load-bearing fact
  behind PHOTONICS' attack, §1.1); confirmed `r3_config()`'s `y_lo =
  R3_BASE_ABSORB + pad` (not `absorb + pad`), so `A = obj_y − y_lo =
  R3_BASE_OBJ_Y − R3_BASE_ABSORB` is exactly `pad`-independent by
  construction — the proposal's "pad-independent by construction" claim in
  §2a is verified true in code, not merely asserted; `G40_R3 = r3_config(60,
  60)` and `C80_R3 = r3_config(120, 60)` do produce bit-identical `nx=660,
  ny=2496` (both depend on `pad` only) — the proposal's claimed
  cell-footprint/cost-basis identity to `C80_R3` is verified true.
- **Re-derived every cost/budget number in §2d from `dg069._cost()`'s own
  formula** by hand: native repeat `3×2×(75.0+104.4)=1076.4`, R3 leg
  `3×2×(168.75+234.9)=2421.9`, R3 spot-check `2×(253.125+352.35)=1211.0`,
  total `4709.3` CPU-s, wall `1.15×4709.3/(4×0.98)=1381.6s≈23.0min`, 3×
  envelope `≈69min`. All exact. **No defect found anywhere in the geometry
  or budget arithmetic** — this proposal's own numbers are sound wherever I
  could independently check them against a committed primitive.
- **Re-derived QUANTUM's central numeric claim from primitives, not from
  QUANTUM's own citation of it** (§1.4, below — this is the task's own
  named check).
- **Computed VISION's own requested check** (§4, below) rather than
  leaving it as an unresolved "should add a sentence" ask.

## 1. Adjudication of the five blind critiques

### 1.1 PHOTONICS — the reused P-069-5 band mistransfers a magnitude-delta tolerance onto a phase/propagation-delta quantity — **UPHOLD**

Tag: `inconsistency`. PHOTONICS' physical claim rests on `G40−C40` being a
pure-`PAD` (lossless-vacuum) effect, structurally different from `C80−C40`
(a pure-`ABSORB`-depth, i.e. graded-loss-magnitude, effect) — the band this
proposal reuses in §4(a) was derived for the latter. I independently
re-verified the load-bearing fact from the engine source myself (§0, above):
`_damping`'s array depends only on `self.absorb`, never on `pad`; `G40` and
`C40` share `absorb=40` bit-identically (`experiments/065-.../design_
geometry.py::CONFIGS`), so the boundary's reflectance magnitude is
structurally guaranteed identical between them — this is not new physics,
it is exp-076's own established, Red-Team-confirmed finding
(`experiments/076-.../phase5_redteam_audit.md`, "PAD is provably lossless
vacuum... It cannot, by this argument, be [an absorbed-power] effect."). The
citation PHOTONICS makes to its own exp-069 Phase-5 precedent
(`phase5_review_photonics.md` §4: the P-069-5 ratios 1.97×/2.50× sit near a
zero-crossing, not a peak, and the `[0.3,3.0]` band is ~10× wider than this
program's historical ~7% R3-survival precedent) is verified accurate — I
independently confirmed both cited ratios from `experiments/069-.../
results.json` (§0). PHOTONICS' attack is real: a wide magnitude-ratio band
built for one physical quantity class does not automatically transfer to a
different one (a coherent round-trip-timing signal), and the two angles this
band is asked to certify at (40.2°/41.4°) are, by construction, the two
nearest this cycle's own crossing — exactly where a resolution-driven phase
shift produces the largest relative swing while telling you nothing about
whether the underlying feature moved. PHOTONICS' proposed fix (a
location-sensitive companion test, using only the R3-leg's own 3 already-
budgeted points, zero marginal cost) is real and cheap.

### 1.2 ELECTROMAGNETISM — using the unverified cpl=20 FLOOR to test whether the cpl=30 crossing has moved is circular — **UPHOLD**

Tag: `inconsistency` (an epistemic circularity in what §4(b)'s test can
actually license, not a numeric error). EM's claim requires two supporting
facts, both independently checked: (1) `FLOOR` is the RMS of `frac_contrast`
*at cpl=20* (confirmed, §0); (2) 40.2°/41.4° were selected specifically
*because* they sit near a cpl=20 `delta_scene` zero-crossing (confirmed —
this proposal's own §1 and §2b state this explicitly, and exp-089's own
NOTES.md §1 selection rule, independently re-read, states the same). Given
both, EM's point holds: testing whether `ratio_k`'s cpl=30 classification
still clears an cpl=20-calibrated `FLOOR` conflates "did the classification
survive resolution refinement" with "did the crossing move, and by how
much" — the two questions are confounded by construction at exactly the two
angles this design is honest enough to flag as the two-sided, non-formal
part of its own test (§4a's closing paragraph). EM's cited T10 precedent
(46%→128% relative spread under `cpl×1.5` on a near-field point-probe
channel, later shown ~96% attributable to an unrelated `SIGMA_ON` confound,
residual 46%→49%) is verified accurate against LOGBOOK's own T10 record
(lines 877–971, 6349–6852) — a real, on-the-record precedent that a
near-field/point-probe channel (which `frac_contrast`/`delta_scene` is,
being built on `lab/ambient.py`'s Weber-contrast field probe, not a
closed-surface flux integral) can be resolution-sensitive in ways a
flux-box channel is not. EM's proposed fix (2–4 cheap `cpl=30` bracketing
points around 40.2°/41.4°, ±0.1–0.2°) directly and cheaply converts an
argued-robust claim into a computed one — see §5 for why this specific gap
is a real R8-shape mandatory item, not a discretionary nice-to-have.

### 1.3 THERMODYNAMICS — the numerator (`frac_p_abs`) receives no cross-resolution scrutiny at all — **UPHOLD**

Tag: `inconsistency` (an asymmetric treatment: one half of `ratio_k` is
resolution-tested, the other is not, despite both being equally
load-bearing to §4(b)'s classification question). I independently confirmed
from the proposal's own §4(d) text that the only numerator-side check this
design runs is a 3-point *smoothness-across-angle-at-cpl=30* check
(R14(a)-style), never a *cpl=20-vs-cpl=30 value match* at any of the three
angles — `grep`-level confirmation, the text simply never states such a
comparison anywhere in §4. This is exactly the gap R14 (adopted Iteration
65, exp-088) exists to police: `frac_p_abs = |p_abs_w(G40,θ)−p_abs_w(C40,θ)|
/p_abs_w(C40,θ)` is architecturally the identical small-difference-over-base
construction R14 already flagged as numerator-side-fragile, independently
mechanistically explained (THERMODYNAMICS' own Iteration-65 finding,
re-confirmed at Iteration 66 five independent ways) as living in the
`σ_ext(θ)` config-differential term specifically — precisely the quantity a
finer grid could plausibly shift differently between `C40_R3`/`G40_R3`. The
critique's own point that 40.2° (the chosen settling-spot-check angle) is
not `frac_p_abs`'s own historically-worst case (38.4°, R14's founding dip)
is correct and independently checkable from the R14 registry text itself.
THERMODYNAMICS' proposed fix (a co-equal PRIMARY `frac_p_abs(θ,cpl=30)` vs.
`frac_p_abs(θ,cpl=20)` prediction, reusing (a)'s own `[0.3,3.0]`/`[0.1,10]`
bands, zero marginal FDTD cost since `p_abs_w` is already computed at both
resolutions by the already-budgeted 28 calls) is real, cheap, and — per §2
below — compounds with EM's fix rather than merely coexisting with it.

### 1.4 QUANTUM OPTICS — §4c2's settling spot-check is pointed at the wrong angle by the record's own numbers — **UPHOLD, independently re-derived from primary sources (the task's own named check)**

Tag: `inconsistency`. This is the sharpest attack of the five, and I
re-derived it myself directly from `experiments/089-t28-combined-angle-
census/NOTES.md`/`results.json` — **not** from the proposal's own citation
of these numbers, matching this program's own R4/R9 standard for
independently re-checking a claim rather than restating it.

**FLOOR margin** (`frac_contrast(θ)/FLOOR`, `FLOOR=1.91744×10⁻⁴`):
- 40.2°: `frac_contrast=2.830881×10⁻⁴` ⇒ margin `= 2.830881/1.91744 =
  1.47638×` (proposal cites 1.4764 — matches).
- 41.4°: `frac_contrast=2.510967×10⁻⁴` ⇒ margin `= 2.510967/1.91744 =
  1.30954×` (proposal cites 1.3095 — matches).
- **41.4° margin (1.3095×) < 40.2° margin (1.4764×). 41.4° is thinner.**

**Crossing distance** (from `experiments/089-.../NOTES.md` line 463's own
cited true crossings, `40.265°`/`41.461°`, independently re-confirmed
against `experiments/090-.../phase2_redteam_audit.md`'s own from-scratch
interpolation of the same 31-point window, which reports the identical
`40.265°`/`41.461°`):
- 40.2°: `|40.265−40.2| = 0.065°`.
- 41.4°: `|41.461−41.4| = 0.061°`.
- **41.4° distance (0.061°) < 40.2° distance (0.065°). 41.4° is closer.**

**Both independently-derivable metrics agree, and both come from the
proposal's own §2b table (which cites the identical bit-exact numbers) —
this is not a disputable reading.** §4c2's text states, verbatim: "θ=40.2°
(this cycle's thinnest-margin, most crossing-proximate angle)." By the
record's own two available numeric criteria, this is factually backwards:
**41.4° is the thinner-margin, more crossing-proximate angle on both
counts.** This is a genuine internal inconsistency — the proposal's own
§4c2 claim contradicts its own §2b table, presented four lines apart in the
same document. It recurs a second time, verbatim in substance, in
Idealization 10 ("chosen as the thinnest-margin, most crossing-proximate
point... if adequate at the hardest case it is unlikely to be the binding
constraint elsewhere") — so the false premise is baked into the design's
own scoping logic twice, not stated once as a typo (see RT-2, §4, below).

QUANTUM's **secondary observation** (the reused P-069-5 precedent ratios,
1.97×/2.50×, sit close to the [b]-flipping thresholds at these two angles)
I independently re-checked arithmetically: to flip 40.2°'s `ratio_k=25.08`
below `RATIO_HIGH=10` requires `frac_contrast_R3/frac_contrast_cpl20 >
25.08/10 = 2.508`; for 41.4° (`ratio_k=28.81`), `>2.881` — both match
QUANTUM's cited ">2.51"/">2.88" exactly (algebra: `ratio_k` scales as
`1/frac_contrast` at fixed `frac_p_abs`, confirmed directly from
`ratio_k = frac_p_abs/frac_contrast` in `experiments/089-.../run.py:288`).
**One refinement, not a reversal, of QUANTUM's own framing**: the P-069-5
precedent's higher observed ratio (2.50×, at θ=40°) sits *below* both this
cycle's own flip thresholds (2.51 and 2.881) — so if this cycle's own
measured ratios exactly repeated that one historical precedent, (b) would
NOT flip at either angle. "The passing ratios themselves already sit almost
exactly where they'd need to be... to flip" is accurate and well-supported;
"the exact range that make a CONFIRM-on-(a)/flip-on-(b) outcome the
*expected* case, not an edge case" overstates this by one notch — the
single available precedent falls just short of the flip line, not past it.
The live-possibility framing survives; "expected" should read "a close,
live possibility, not yet demonstrated" (folded into the mandatory docket
as a wording precision, not a substantive disagreement).

QUANTUM's proposed fix (run the §4c2 spot-check at 41.4°, or both angles)
is correct and should be adopted; see §5's mandatory docket.

### 1.5 VISION SCIENCE — the mandatory carried-idealizations banner cites the wrong idealization numbers — **UPHOLD**

Tag: `inconsistency`. I independently checked this term-by-term against
§5's own numbered idealization list (already quoted in full in
`phase1_proposal.md`, re-read directly rather than taken from VISION's
paraphrase): the banner's third clause ("`FLOOR`/`RMS[frac_contrast]`
remain `graded_black_shell`/600nm-specific and are applied here,
unrecomputed... a disclosed mixed-resolution comparison") is a near-verbatim
restatement of **Idealization 6** ("`FLOOR`/`RMS[frac_contrast]` are
applied, not recomputed, against the new `cpl=30` numbers — a disclosed
mixed-resolution comparison"). Idealization 8 is unrelated content (declining
the full 31-point/124-call R3 rebuild and the still-queued R14(b) period
fit). The banner cites "Idealizations 3/7/8"; the correct citation is
**3/6/7**. VISION is right on the letter and right that this matters: a
future citation tracing "Idealization 8" for this specific caveat lands on
the wrong text.

**Independently verified VISION's supporting claim about the escalated
banner rule's own history** (§5 below covers whether this fires Checkpoint
4): this proposal's banner is present, correctly worded, and correctly
scoped at §4 — genuinely the strongest Phase-1-stage compliance with the
Iteration-65 escalated rule this sub-thread has produced, as VISION's own
steel-man states and as I independently confirm by direct comparison
against exp-088/089/090's own Phase-1 documents (none of which opened §4
with a banner at all). The defect here is narrower than any of the four
prior disclaimer-erosion instances (LOGBOOK Iterations 53/63/64/65): those
were *omissions* (a correct caveat existing elsewhere in the same document
failing to propagate into one prose restatement); this is a **miscitation**
inside a banner that is present, correctly worded, and correctly placed —
a different, milder defect, closer to the R4/R9 "cross-reference accuracy"
family than to the disclaimer-erosion "omission" family. See §5 for why
this distinction is dispositive for the Checkpoint-4 question.

## 2. Compounding finding: EM's and THERMODYNAMICS' fixes answer the two complementary halves of the same question and should both be adopted, not traded off

EM's fix (bracket 40.2°/41.4° with 2–4 cheap `cpl=30` points to locate the
crossing directly) targets the **denominator** side of `ratio_k`
(`frac_contrast`, whose zero-crossing location is what the old `FLOOR`
implicitly assumes is unmoved). THERMODYNAMICS' fix (a co-equal PRIMARY
`frac_p_abs(θ,cpl=30)` vs. `cpl=20` comparison) targets the **numerator**
side. Read together: adopting only one leaves the other half of `ratio_k`'s
classification untested at resolution, an asymmetry neither critique alone
states as starkly. Both are cheap (EM's: 2–4 extra FDTD calls, well inside
this cycle's own 69-minute 3× safety envelope even doubled; THERMODYNAMICS':
literally zero marginal FDTD cost, since `p_abs_w` at both resolutions is
already produced by the already-budgeted 28 calls). Phase 3 should adopt
both as co-equal fixes, not select one as "sufficient." PHOTONICS' own fix
(a location-sensitive companion test using only the R3-leg's own 3 points,
zero marginal cost) is the cheapest of the three and answers a similar
denominator-side question at lower resolution than EM's bracket — Phase 3
should run PHOTONICS' free interpolation first; if it is inconclusive
(e.g., the 3-point local slope estimate is itself noisy), EM's bracket is
the fallback, not a redundant parallel spend.

## 3. VISION's own requested check, computed (not left as "should add a sentence")

VISION asked whether the `[0.3,3.0]` CONFIRM band's edges, in absolute
Weber-contrast units, sit above or below `C_THR_BASE=0.005`
(`lab/glare_sidecar.py:74`, sourced Blackwell 1946/Rose 1948/CIE 19/2/
Adrian 1989 — confirmed at `lab/glare_sidecar.py:78`). **Doing this
correctly requires care VISION's own critique does not spell out and which
this program's own R9 rule exists to police**: `frac_contrast` is *not*
itself a Weber contrast — it is `|delta_scene|/|C40_C|`
(`experiments/088-.../run.py:96`), a dimensionless ratio normalized by the
scene's own large baseline contrast (`|C40_C|≈0.53–0.56` at these three
angles). Comparing `frac_contrast` (or a multiple of it) directly against
`C_THR_BASE` would be exactly the unit-mismatch shape R9 was adopted to
catch (LOGBOOK Iteration 54, `experiments/077-.../phase5_redteam_audit.md`
§0.2). The commensurate quantity is `delta_scene` itself — recovered by
multiplying `frac_contrast`'s CONFIRM-band edge by `|C40_C(θ)|`, which is
algebraically identical to scaling the already-known `|delta_scene(θ)|`
directly by the same band factor. Using the bit-exact `delta_scene` values
re-derived in §0 from `experiments/083-.../results.json`:

| θ | `\|delta_scene\|` (measured, cpl=20) | ×3.0 (CONFIRM upper edge) | vs. `C_THR_BASE=0.005` | ×10 (REFUTE edge) | vs. `C_THR_BASE` |
|---|---|---|---|---|---|
| 37.2° | 2.348254×10⁻⁴ | 7.0448×10⁻⁴ | 14.1% (≈7.1× below) | 2.3483×10⁻³ | 47.0% (≈2.1× below) |
| 40.2° | 1.540815×10⁻⁴ | 4.6224×10⁻⁴ | 9.2% (≈10.8× below) | 1.5408×10⁻³ | 30.8% (≈3.3× below) |
| 41.4° | 1.337362×10⁻⁴ | 4.0121×10⁻⁴ | 8.0% (≈12.5× below) | 1.3374×10⁻³ | 26.7% (≈3.7× below) |

**Answer: at every one of the three angles, even the loosest CONFIRM-band
edge (a full 3× upward resolution-driven shift) stays 7–12.5× below
`C_THR_BASE`, and even the REFUTE-band edge (a 10× shift, itself a
falsifying outcome for this cycle) stays 2.1–3.7× below it.** VISION's
concern — that the wide reused tolerance could swallow the one pinned
perceptual threshold this channel's own instrument exists to police — does
not materialize numerically at these three angles, though it comes closest
(within ~2.1×) at 37.2° under the REFUTE, not CONFIRM, outcome. This does
not change any verdict (this cycle explicitly, correctly disclaims testing
constraint 3 — Idealization 3/7), but it is exactly the kind of "compute
it, don't just argue it" answer this program's own R8 discipline calls for,
and it should be added to the document as a checked fact, per VISION's own
request (§5, mandatory docket item).

## 4. Red Team's own additional attacks (not raised by any of the five blind critiques)

**RT-1. The §1 narrative claims a benefit this cycle never operationalizes into any §4 prediction — an unfalsifiable claim.** [`unfalsifiable`]

§1 states the native-`cpl` repeat leg runs "jointly... directly relieving
37.2°'s own separately-flagged 'felt-lucky' noise-floor margin" — a
reference to exp-089's own NOTES.md Learned #4 (independently re-confirmed
by exp-090's own Red Team audit, RT-1, at `1.0455×`), a *different*
quantity from `frac_contrast`'s `FLOOR` margin: the `resolved`-gate
significance test `|Δp_abs|/(NOISE_MULT·box_dev_max·p_C40)` on the
box-ledger (`p_abs_w`) channel. I grepped the full, already-quoted proposal
text for "felt-lucky," "1.046," "noise-floor margin," and "resolved-gate":
the phrase "felt-lucky" appears exactly once, in §1, and never again
anywhere in §2–§7. **No prediction in §4 scores this quantity at 37.2° under
`STEPS=4200`, at any resolution.** This is not merely undischarged — it is
never even named as a target the design is being scored against, despite
being explicitly claimed as a benefit of running the cycle at all. The data
needed to check it is not hypothetical: the native-repeat leg (rows 1–8 of
§2c) already runs both `p_abs_w(C40,37.2°)` and `p_abs_w(G40,37.2°)` at
`STEPS=4200`, i.e. exactly the inputs the `resolved`-gate margin needs.
**Fix (mandatory, zero marginal cost):** either add, as a disclosed
(not necessarily gating) §4(d)-style report, the recomputed 37.2°
`resolved`-gate margin at `STEPS=4200` alongside its cited `STEPS=2800`
figure of `1.046×`, or remove the "directly relieving" claim from §1 as an
unbacked assertion.

**RT-2. The false "40.2° is the hardest case" premise QUANTUM identified in §4c2 is restated a second time, in Idealization 10, and should be fixed in both places.** [`inconsistency`]

Idealization 10 restates: "chosen as the thinnest-margin, most
crossing-proximate point, on the reasoning that if `R3_STEPS=4200` is
adequate at the hardest case it is unlikely to be the binding constraint
elsewhere." This is the identical false premise QUANTUM's attack (§1.4,
upheld) refutes by the record's own numbers. Fixing §4c2 alone (moving or
adding the spot-check at 41.4°) without correcting Idealization 10's own
restated justification would leave the document's own scope-rationale
internally contradicting its corrected prediction. **Fix (mandatory, same
edit as QUANTUM's, applied in both locations):** once §4c2 targets 41.4°
(or both angles), Idealization 10's text should be corrected to match, not
left as a stale restatement of the superseded reasoning.

**RT-3. QUANTUM's secondary-observation wording should be precisioned, not adopted verbatim.** [`inconsistency`, minor]

Per §1.4 above: the P-069-5 precedent's higher ratio (2.50×) sits *below*
both of this cycle's own flip thresholds (2.51/2.881), so QUANTUM's "the
expected case, not an edge case" overstates the single available data
point. **Fix (mandatory, wording only, zero cost):** if QUANTUM's secondary
observation is folded into Phase 3's synthesis text, it should read as "a
close, live possibility this design's own two-sided framing already
anticipates" rather than "the expected case" — the distinction matters
because "expected" could be read, by a future citation, as implying this
cycle predicts a flip, which it explicitly and correctly does not (§4b's
own "no confident lean, stated plainly, not hedged" framing is the correct
one and should govern).

## 5. Checkpoint / standing-rule check

**Constraint 1–4 / T1**: N/A, correctly and consistently disclosed
throughout (§3, the carried-idealizations banner, Idealization 7) — no
misstatement found. No `constraint-#N` tag applies anywhere in this audit,
for the reason stated in this document's own opening scope note.

**R3**: this cycle is the intended, direct discharge of R3's own
meta-rule for the `PAIR_PAD`/`G40_R3` channel — not a violation of it. I
independently confirmed (§0) that `G40_R3` has never previously existed in
`R3_CONFIGS`, and that the underlying `r3_config()` machinery the proposal
extends to build it is already committed, tested code, not new
speculation. This is exactly what R3 requires before `40.2°`/`41.4°`'s
values keep being cited at face value in future T28 citations.

**R13/R14**: correctly applied unchanged — the proposal explicitly declines
to re-derive or relax either threshold (§4d, §6), and I find no place where
it extends R13/R14 to a resolution it hasn't earned. THERMODYNAMICS' upheld
attack (§1.3) identifies a real *gap* in resolution-testing R14's own
numerator-hazard construction, not a violation of R14's text.

**R8 (an unverified robustness argument is not sufficient when an
affordable named check exists)**: EM's attack (§1.2) is, on inspection,
squarely an R8-shape gap, not merely a "support-with-changes" nicety.
Idealization 6/§4d disclose that `FLOOR` is unverified at `cpl=30` and
explicitly, correctly decline the expensive (~124-call) full rebuild — that
part of the disclosure is sound and proportionate. But EM's own proposed
fix (2–4 bracketing calls, a small fraction of this cycle's own 69-minute
safety envelope) is exactly the kind of "specific, affordable check" R8's
own text requires be run rather than argued around. **This elevates EM's
fix from optional to mandatory** under this program's own standing rule,
matching how exp-090's own Red Team audit treated an analogous gap (RT-3,
"an R8-shape gap... a ~10-line, same-shift computation" — there, mandatory
too).

**Disclaimer-erosion lineage (VISION, §1.5) — explicit ruling, not
pattern-match.** This program's escalated rule (LOGBOOK Iteration 65,
CHECKPOINT block) states unconditionally that "a fourth instance fires
[Checkpoint criterion 4] automatically" — with no discharge clause
attached, a deliberate departure from R6–R13's usual "caught blind, same
cycle" non-firing pattern, because three successive just-in-time catches
demonstrated the omission shape is not reliably prevented by per-cycle
vigilance alone. **I find this proposal's defect is not an instance of that
specific lineage at all, on two independent grounds, either of which is
sufficient on its own:**

1. **Shape**: every one of the four prior instances (Iterations 53, 63, 64,
   65) was an *omission* — a caveat that already existed correctly
   elsewhere in the same document failing to propagate into one prose
   restatement of the finding it governs. This proposal's defect is a
   *miscitation* — the banner is present, in the correct section, correctly
   worded, and its substantive content (NETD-not-human-eye,
   constraint-1–4-not-tested, FLOOR/RMS mixed-resolution) is exactly what
   the escalated rule requires. Only the footnote *numbering* pointing back
   to §5 is wrong. This is closer to the R4/R9 cross-reference-accuracy
   family than to the disclaimer-erosion omission family — a genuinely
   different, milder defect, not a fifth member of the specific lineage the
   unconditional language targets. (This mirrors exp-090's own Red Team
   ruling on a *different* near-miss one cycle earlier — Iteration 67's
   audit ruled a banner-adjacent defect "milder... only a supplementary,
   self-invented per-item convention" failed, not the mandatory disclaimer
   itself — the same discipline of distinguishing defect *kind*, not just
   defect *presence*, applies here.)
2. **Discharge test**: even setting (1) aside, this defect was caught
   blind, by a Phase-2 critique, before any Phase-3 synthesis exists —
   this program's own universal, standing discharge test for every prior
   rule's first catch (R3 through R14, and every prior disclaimer-erosion
   instance's own *first* catch), applied identically here.

**Ruling: Checkpoint criterion 4 does NOT fire, on either of two
independent grounds.** VISION's banner-citation finding is real and must be
fixed (mandatory docket item below) — this is not a judgment that it
doesn't matter, only that it is not the specific fifth-instance-fires-
automatically case the escalated rule targets.

**No other matter in this audit approaches Checkpoint criterion 4.** RT-1
(the unbacked "felt-lucky" narrative claim, §4) was caught here, at Phase
2, before Phase 3 — the standard discharge test, cleanly met; it is also a
first-time-shape finding (no prior LOGBOOK entry names this specific
pattern — an untested narrative benefit-claim — as a recognized, escalated
lineage), so no "known, named, ignored" standard from R6–R14 applies to it
either. QUANTUM's mislabeled-hardest-case finding (§1.4) is likewise caught
at Phase 2, pre-freeze.

**Checkpoint criterion 5** (two consecutive non-advancing cycles): N/A —
exp-090 was itself a logbook-advancing PARTIAL (a usable calibration
deliverable, per its own Combined Verdict), and this cycle, once the
docket below is applied, directly discharges the single oldest
undischarged item on the whole T28 board (R3 on this channel, three
cycles running, exp-088/089/090) — logbook-advancing by construction.

**No LOGBOOK misstatement found** in this proposal: every cited historical
figure (FLOOR, the three FLOOR margins, the three crossing distances, the
P-069-5 ratios) reproduces bit-exact against its own primary source (§0).

## 6. Overall verdict: **PROCEED-WITH-MANDATORY-FIXES**

The core deliverable — extending R3's resolution check, for the first
time, to the `C40`/`G40` `PAIR_PAD` channel that every T28 caution-zone and
classification number since exp-087 depends on — is well-targeted, cheap,
correctly scoped as pure instrument recalibration, and its own geometry
and cost arithmetic are sound wherever independently checkable (§0). This
proposal is a direct, faithful execution of Iteration-67's own
near-unanimous Reconciled-Queue Rank-1 item, not a scope deviation. Nothing
in this audit overturns the design's core; the docket below closes real
gaps — one genuine internal inconsistency about which angle is actually
hardest (§1.4, self-contradicting the proposal's own §2b table), an
asymmetric resolution-test coverage between `ratio_k`'s numerator and
denominator (§1.3), a mistransferred tolerance band's physical basis
(§1.1), a circularity in what the classification test can license (§1.2,
elevated to mandatory under R8, §5), a wrong internal citation (§1.5), and
an unoperationalized narrative claim this audit found independently (§4
RT-1) — all fixable same-shift in prose/scope or with a small (2–4 call)
addition well inside this cycle's own 69-minute safety envelope.

### Mandatory-fix docket (apply before Phase 3 freezes; ten items)

1. **Move (or add) the §4c2 R3-settling spot-check to θ=41.4°** (or run
   both 40.2° and 41.4°) — the proposal's own §2b table shows 41.4° is
   both the thinner-margin (1.3095× vs. 1.4764×) and the more
   crossing-proximate (0.061° vs. 0.065°) of the two angles by every metric
   the design itself cites (QUANTUM, upheld, §1.4).
2. **Correct Idealization 10** to match fix 1 — it currently restates the
   same superseded "40.2° is the hardest case" reasoning a second time
   (RT-2, §4).
3. **Add PHOTONICS' location-sensitive companion test**: report whether
   `delta_scene`'s locally-interpolated zero-crossing angle (from the
   R3-leg's own three points) shifts by more than half the 0.2° grid step
   relative to the native-`cpl` crossing location, alongside §4(a)'s
   magnitude-ratio test (PHOTONICS, upheld, §1.1).
4. **Add EM's cheap bracketing points**: 2–4 extra `cpl=30` `PAIR_PAD`
   calls at ±0.1–0.2° around 40.2°/41.4°, to directly locate the `cpl=30`
   crossings rather than inferring crossing-stability indirectly through
   the unverified `cpl=20` `FLOOR` — mandatory under R8 (an affordable
   named check exists and was not run; §5), not merely discretionary
   (EM, upheld, §1.2).
5. **Add THERMODYNAMICS' co-equal PRIMARY prediction**: `frac_p_abs(θ,
   cpl=30)` vs. `frac_p_abs(θ,cpl=20)` at all three angles, reusing (a)'s
   own `[0.3,3.0]`/`[0.1,10]` CONFIRM/REFUTE bands — zero marginal FDTD
   cost (THERMODYNAMICS, upheld, §1.3). Per §2, adopt jointly with fix 4,
   not as an alternative to it — together they resolution-test both
   halves of `ratio_k`.
6. **Fix the banner citation**: "Idealizations 3/7/8" → "Idealizations
   3/6/7" (VISION, upheld, §1.5).
7. **Add the computed absolute-Weber-contrast comparison** (§3, this
   audit): state that the `[0.3,3.0]`/`[0.1,10]` band's edges, in absolute
   `delta_scene` units, sit 7–12.5× (CONFIRM edge) / 2.1–3.7× (REFUTE
   edge) below `C_THR_BASE=0.005` at all three angles — a checked fact,
   not an assumed one, discharging VISION's own request (§1.5) with a
   number rather than leaving it open.
8. **Either operationalize or drop the §1 "felt-lucky noise-floor margin"
   relief claim**: no §4 prediction currently scores the 37.2°
   `resolved`-gate margin at `STEPS=4200`, despite the native-repeat leg
   already producing the `p_abs_w` values that quantity needs (RT-1, §4).
9. **Precision QUANTUM's secondary-observation wording** if folded into
   Phase 3: "a close, live possibility," not "the expected case" — the
   single available precedent ratio (2.50×) sits just below, not past,
   this cycle's own flip thresholds (RT-3, §4).
10. **State explicitly, in whichever section documents fix 4's bracketing
    result, whether it changes the read on fix 1's own re-targeted spot-
    check** — i.e., if the bracketing points show the `cpl=30` crossing has
    shifted materially closer to 41.4° than to 40.2° (or vice versa), that
    directly informs which angle's settling result is actually the binding
    one, and should be cross-referenced rather than reported as two
    independent findings.

No item above requires re-scoping this cycle's own budget beyond a small,
already-affordable addition (fix 4); none touches the design's own core
R3-discharge purpose or its geometry/cost arithmetic, both independently
verified sound in §0.
