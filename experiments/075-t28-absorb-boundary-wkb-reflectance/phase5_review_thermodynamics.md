# PHASE 5 — REVIEW · THERMODYNAMICS · Panel Iteration 52 · exp-075

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md seat 4, verbatim): "where
absorbed energy goes. Always asks what re-radiates and whether it would be
detectable. Owns the per-proposal energy sidecar: absorbed power ->
temperature rise -> emission band -> detectability. Expressibility contract:
the sidecar is a post-run analytic calculation, not an FDTD output, and is
labeled as such." Blind to every other seat's Phase-5 review this cycle and
to Red Team's Phase-5 final audit. This is the same seat that led this
cycle's Phase 1 proposal by rotation, but a fresh sub-agent with zero memory
of writing it — reviewed exactly as skeptically as any other seat would,
per the task's own instruction not to defer to it.*

---

## 0. Verdict

**PARTIAL**, on this program's own established live-thread convention
(matching Iteration 51's own wording for a comparably decisive sub-thread
closure): both tested boundary-reflectance-echo mechanisms — the single
`-x`-wall echo (Phase 1) and the correctly-derived two-wall cavity
(Phase 3/4) — are **RULED OUT specifically and robustly**; T28 itself (the
~2.84° `C80-C40` periodicity's origin) remains **completely open**, exactly
where seven prior cycles left it. This is not a weak or hedged result: it
is a real, mapped constraint-boundary finding (PANEL.md's "honest
alternative product" — a mechanism class shown not to explain the
phenomenon, gates clean) on the FIRST cycle in this eight-cycle T28
sub-thread to engage a seat's own charter physics directly rather than
re-fit or re-price a statistical instrument. From my own seat's charter:
the finding is clean because it was never entangled with an energy/
detectability question in the first place — see §2 below for why that is
correctly argued, not merely assumed, and why it survives the extension
from one echo term to two.

---

## 1. Independent re-verification (R4 — recompute, don't restate)

I ran both committed scripts unmodified, end to end, from this review
(not copied from any prior document), and additionally built two
from-scratch checks neither script nor any Phase-2/Red-Team document
performed.

### 1a. Bit-exact reproduction of both scripts

`python3 boundary_reflectance.py`: reproduces every number in
`phase1_proposal.md`/`boundary_reflectance_results.json` exactly —
`rel_period_dev=4.2778`, `shape_r2=0.2586`, `pearson_r=-0.5085`,
`COMBINED VERDICT: REFUTE`, all three gates (`G-LOSSLESS 2.2e-16`,
`G-N1 1.4e-15`, `G-PASSIVITY worst |r|=0.006423`), and the `[5b]`
ABSORB-depth cross-check (`ptp` ratios and all six cross-config
correlations, `4/6` pairs negative — matching Phase 3's own corrected
count, not Red Team's original "3/6" slip).

`python3 two_wall_cavity.py`: reproduces every number in
`phase4_results.md`/`two_wall_cavity_results.json` exactly —
`D_left`/`D_right` tables, `rel_period_dev=4.2778` (bit-identical to the
single-wall figure), `shape_r2=0.3042`, `pearson_r=-0.5516`,
`circular_shift p_value=0.19525`, `frozen_prediction_confirmed=True`,
`COMBINED VERDICT: REFUTE`.

No discrepancy anywhere. This is, independently, the cleanest reproduction
record in this eight-cycle sub-thread — consistent with Red Team's own
Phase-2 audit finding the same thing at Phase 2.

### 1b. Exact enumeration of the circular-shift null (new this review)

`phase3_synthesis.md`'s mandatory robustness check (`circular_shift_null`,
`two_wall_cavity.py`) draws `N=20,000` *Monte Carlo* circular shifts to
estimate a p-value. But the real `delta(theta)` array has only **31
points**, so there are only **30 distinct nonzero circular shifts** —
the entire population is enumerable exactly, at negligible cost, rather
than estimated. I did this:

```
observed |r| = 0.551580  (committed: 0.5516, matches)
EXACT p-value (all 30 shifts, no MC noise) = 0.200000  (= 6/30 exactly)
committed 20,000-trial MC p-value          = 0.19525
exact null mean|r|    = 0.3006   (committed MC: 0.2989)
exact null 95th pct|r| = 0.6556  (committed MC: 0.6800)
observed |r| ranks 6th of 30 shifts by |r| (1 = most extreme)
```

**The committed MC estimate (`p=0.19525`) is confirmed correct** — it
sits within ordinary sampling noise of the true exact value (`p=0.2000`;
the binomial SE at `p≈0.2`, `N=20,000` is `≈0.0028`, and the two values
differ by `0.0048`, about `1.7` SE). `phase4_results.md`'s "NOT
significant" reading is independently reconfirmed by an exact, not
sampled, calculation. **A genuinely new point for the permanent record,
not a defect**: this test's actual resolution ceiling is `1/30≈0.033`,
not the four-decimal precision `p=0.1953` visually implies — the null
is a 30-member discrete population, not a continuous one, at this window
width. For any future cycle that builds an order-preserving circular-shift
null on this bench's `n=31`-point dense-sweep grid, **exact enumeration is
both cheaper (30 evaluations vs. 20,000) and strictly more correct than
Monte Carlo sampling** — worth adopting as the default method, not merely
a cross-check, the next time this construction is reused (it will be:
`phase3_synthesis.md`'s own Idealization/§3.4 note flags this composition
as reusable machinery for a future third echo/cavity variant).

### 1c. My own charter's number, recomputed (not restated)

`phase1_proposal.md` §3 states: "`|r|<=0.0064` throughout §2d means
`>99.996%` of incident power is absorbed, not reflected." Recomputed
directly from the committed `gate_passivity` figure
(`boundary_reflectance_results.json`, worst `|r|=0.006423411555094661`,
not the rounded `0.0064` quoted in prose):

```
reflected power fraction = |r|^2        = 4.126022e-05
absorbed power fraction  = 1 - |r|^2    = 0.99995874  =  99.995874%
Is 99.995874% > 99.996%?  FALSE
Is 99.995874% > 99.995%?  TRUE
```

**A small, non-load-bearing R4-class arithmetic imprecision, in my own
seat's own paragraph, that no other seat's charter would naturally have
checked** (none of the five Phase-2 critiques or Red Team's Phase-2 audit
touch §3 at all — sensible, since the sidecar disposition itself was never
contested by anyone). Correct statement: **`>99.995%`, not `>99.996%`**.
Trivial in isolation, but exactly the shape of figure R4 exists to catch —
"close enough by eye" is not the standard, and this is the sidecar's own
one quantitative claim, so it should be right. Recommended fix for the
permanent record: correct `>99.996%` to `>99.995%` in `phase1_proposal.md`
§3 (one-word change, no verdict implication — the qualitative point,
"essentially total absorption," is unaffected either way).

---

## 2. The sidecar question this review packet specifically asked me to
   settle: does the N/A argument hold, including for the two-wall model?

**Yes — independently re-derived, not merely re-read, and it holds
identically for both mechanisms.** My reasoning, checked against the
actual code rather than trusted from the proposal's prose:

1. **No physical absorbing object exists anywhere in this cycle's
   dataset, confirmed against the code, not assumed.** `experiments/069/
   run.py::_one_run` (the source of `block_dense.rows`, the real data
   both mechanisms are tested against) builds a scene from `Sim` +
   `add_line_source` + `.run()` only — no `graded_black_shell`, no
   `sigma_e`-based material anywhere (independently confirmed by EM's
   Phase-2 critique §0 and Red Team's audit §0.3; I re-read
   `experiments/069/run.py` myself and confirm the same). The
   `sigma_e`-based conductivity path in `lab/fdtd2d.py::Sim.run` (the
   E-update's `ca`/`cb` coefficients, lines 214-217) is genuinely unused
   here — `alpha` is identically zero.
2. **The `ABSORB` band is the engine's own domain-boundary absorbing
   construct, not a candidate optical material.** I re-read
   `lab/fdtd2d.py::Sim._damping` (lines 122-129) directly: the identical
   cubic-ramp `exp(-0.30*d(x))` multiplicative damping is applied to
   **all four** domain edges (`-x`, `+x`, `-y`, `+y`) by the same
   formula, with the same `self.absorb` parameter — this is a Yee-grid
   absorbing-boundary idiom (this bench's stand-in for a PML), used in
   literally every FDTD run this program has ever done, not a proposed
   physical coating anyone is claiming could be built. This is the
   correct basis for the proposal's own distinction (§3): the sidecar's
   real subject is `lab/materials.py::graded_black_shell` (T5's
   established thread, `lab/thermo_sidecar.py`, trust-suite stage 15,
   Iteration 20) — a candidate cloak-scene absorber that could plausibly
   sit in a real ambient scene and re-radiate detectably. The `ABSORB`
   band is neither claimed nor usable as that; it borders no observer,
   no ambient scene, and is not proposed as a real material anywhere in
   this cycle (MATERIALS' own Phase-2 finding, independently confirmed
   by Red Team, sharpens this further: the derived admittance is a
   matched-`ε=μ` numerical construct, unrealizable at optical
   wavelengths regardless).
3. **Extending from one echo term to two changes nothing about (1) or
   (2).** The two-wall model (`two_wall_cavity.py`) does not introduce a
   second absorbing object — it adds a second *coherent field*
   contribution (an image source through the domain's OTHER pre-existing
   PEC wall, `x=nx-1`) to an interference calculation. The `+x`-edge
   `ABSORB` band was already dissipating energy at the same rate, by the
   same formula, in every run this program has ever done — this cycle
   is the first to build an *analytic echo term* for it, but it does not
   change what is physically happening at that boundary, or introduce
   any new absorbed-power number. No new "where does the energy go"
   question is created by going from one wall to two: the answer ("into
   the same kind of numerical boundary construct as before, with nowhere
   physical to re-radiate into this measurement") is unchanged.

**A genuine documentation gap I found, that this review closes**: unlike
MATERIALS' realizability caveat (mandatory fix 3), which `phase4_results.md`
§5 explicitly states "applies identically to this two-wall model," **no
Phase 3 or Phase 4 document re-states or re-confirms the THERMODYNAMICS
sidecar disposition for the two-wall extension** — `phase1_proposal.md`
§3 argues N/A once, for the single-wall mechanism, and neither
`phase3_synthesis.md` nor `phase4_results.md` nor `NOTES.md` revisits it
when mandatory fix 1 extends the mechanism to a second echo term. The
disposition happens to still be correct (§2 above, independently
re-derived, not merely inherited), but the record should say so
explicitly rather than leave a silent gap that a future citation of this
cycle could misread as an oversight rather than a checked non-issue.
**Recommended fix, near-zero cost**: add one sentence to
`phase3_synthesis.md` §3 or `phase4_results.md` §5 ("What remains open")
stating the sidecar disposition is unchanged and why — matching the
precedent MATERIALS' caveat already set in the same document.

---

## 3. My own ranked top-3 candidate directions for Iteration 53

**1. G40/`PAD` decorrelation (PLAN.md's own Iteration-52 queue item 2,
~31 FDTD calls) — now more load-bearing than before this cycle ran, not
less.** This cycle closed off boundary-reflectance-echo physics as an
explanation for T28 (§0); it did *not* touch the standing `ABSORB`-or-`PAD`
confound that has run through every T28 differential result since
Iteration 48 (LOGBOOK's own standing-forward-constraint language). With
one entire mechanism *class* now ruled out and zero live positive leads
left on the board, disentangling whether the real ~2.84° signal itself is
driven by `ABSORB`, `PAD`, or genuinely neither is now the single most
information-dense open question — the "only queued item that actually
*relieves*, rather than discloses or prices, the confound" (PLAN.md's own
words, still accurate). Explicitly *not* barred by the seventh-cycle rule
(the amplitude-channel readout `√(A_i²+A_q²)/a` conditions on no fitted
carrier phase, a genuinely different instrument class from the retired
differential/two-tone fit). My own charter has no direct purchase on
*which* geometric parameter drives an optical-frequency numerical fringe —
but I can confirm this item carries zero energy/thermal content either
(same reasoning as §2: still no physical absorber anywhere in this
design), so nothing in my own sidecar territory should slow it down.

**2. Close Idealization 6 exactly, rather than leave it a bound.**
`phase3_synthesis.md` §3.3 bounds the double-bounce/resonant-cavity term
at `|r|² ≤ 4.1×10⁻⁵` (>150× smaller than the weakest already-negligible
single-bounce term) rather than computing it — a defensible bound, not a
defect, but cheap to close outright with the exact same transfer-matrix +
image-source machinery already built and vetted this cycle (add one more
coherently-summed image term per wall, weighted by `r²`, reusing
`c_empty_two_wall`'s own pattern). Low expected value (the bound is
already two-plus orders of magnitude below the observed signal's own
amplitude) but genuinely zero-FDTD, near-zero marginal cost given what
already exists, and it is the one remaining named gap in this cycle's own
idealization list that a future citation could otherwise reopen. Rank #2
rather than #1 because, unlike item 1, it cannot change T28's own
open mechanism question either way — it only tidies the boundary-
reflectance thread's own closure.

**3. Bundle this cycle's own record-hygiene items with PLAN.md's queue
item 3, plus two housekeeping items this review specifically found.**
(a) Correct `phase1_proposal.md` §3's `>99.996%` to `>99.995%` (§1c
above, cheap, non-load-bearing); (b) add the one-sentence sidecar
re-confirmation for the two-wall model that §2 above found missing; (c)
if a future cycle reuses `circular_shift_null`'s construction on this
bench's own `n=31`-point angle grids, switch it to exact enumeration
(§1b) rather than `N=20,000` Monte Carlo — strictly cheaper and exact,
not merely a style preference; (d) carry forward PLAN.md's own still-
queued items (the three-document-old "Iteration 5, exp-027" mislabel,
etc.) unchanged. None of this touches T28's own substantive question;
all of it is near-zero-cost discipline that keeps the record honest for
whichever seat next builds on this cycle's own reusable machinery.

---

## 4. Seat-specific finding: what a general-purpose read would miss

The one thing my charter is positioned to check that no other seat's is:
**whether "no energy sidecar" is actually true, not merely asserted, and
whether it stays true across a mechanism's own extension mid-cycle.**
General-purpose rigor (R4 reproduction, gate-checking, statistical
robustness) was already extremely well covered this cycle by five blind
critiques and a thorough Red Team audit — I found no defect in any of
that. What none of those seats' charters would naturally check is exactly
what I checked in §2: does adding a second coherently-summed echo term
create a second physical place for absorbed energy to go? The answer is
no, verified against the actual engine code (`_damping` applies
identically to all four edges, `sigma_e` is genuinely zero throughout),
not merely inferred from the fact that nobody flagged it. The one live
gap I found and closed is procedural, not physical: the sidecar's own
disposition was argued once, for the mechanism as it stood at Phase 1,
and never explicitly re-confirmed when Phase 3's mandatory fix 1 changed
the mechanism being tested — a documentation omission of exactly the
shape this program's own R4 lineage exists to catch, now closed by this
review rather than left for a future citation to misread.

---

## Reproduction

`python3 experiments/075-t28-absorb-boundary-wkb-reflectance/
boundary_reflectance.py` and `.../two_wall_cavity.py`, both run
unmodified from this review (§1a). The exact circular-shift enumeration
and the sidecar energy-fraction recomputation (§1b/§1c) are ad hoc scratch
scripts built for this review, driven only by the two committed
`_results.json` files — no number in this document is hand-typed from
another document without being independently recomputed first.
