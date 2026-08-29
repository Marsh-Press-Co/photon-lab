# PHASE 5 — REVIEW · Seat: THERMODYNAMICS · Panel Iteration 67 · exp-090

Fresh sub-agent, blind to any other seat's current-cycle Phase-5 review.
Read in full: PANEL.md; LOGBOOK.md's RULED OUT (R1–R14) and ESTABLISHED
sections, the LIVE THREADS section including T28's complete history
through Iteration 66/exp-089 (both CHECKPOINT entries, Iteration 65/exp-088
and Iteration 61/exp-084, and the full R13/R14 founding text); the
complete exp-090 record (`phase1_proposal.md`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`,
`run_output.txt`, `results.json`); exp-087/088/089's own `NOTES.md` and
`results.json` for context. I have zero memory of critiquing this cycle at
Phase 2 — that was a different, now-finished fresh agent (whose critique I
read here as part of the finished record, the same as any other seat's).

## Verdict: **CONCUR with PARTIAL.**

Every load-bearing number in NOTES.md's Result section that I independently
recomputed — from raw primitives, not by re-running `run.py` and trusting
its own arithmetic — reproduces exactly. The three-layer method is
correctly specified, correctly scoped to what n=7 can support, and the
Phase-2/Red-Team layer caught and fixed the two defects (P2/P5's
evidentiary overclaim; the missing dual-section banner) that mattered most.
My own seat's Phase-2 concern (a caution zone risking silent
deprioritization of exactly the angles R14 says are most diagnostic) was
adopted correctly, in strong, unambiguous language, at Idealization 10. I
find one small, genuinely non-load-bearing numerical-hygiene point (the
"1.0455" vs. "1.045659" figure, below) and one substantive open point this
cycle correctly declines to resolve but that the record should keep in
clear view for Iteration 68's board.

## Independent verification performed (from raw primitives, not `run.py`'s own output)

I did not accept any of the five critiques', Red Team's, or the Director's
"I independently recomputed this" claims on faith — I recomputed
independently again, in a fresh script, pulling only from the three source
experiments' committed `results.json` files.

**1. Table 1 (margins, zone) — reproduced bit-exact.** From
`experiments/083-.../results.json::per_theta`, computing
`frac_contrast(θ)=|delta_scene(θ)|/|C40_C(θ)|` at all 31 grid points myself:
`RMS=1.9174375118374476×10⁻³`, `FLOOR=1.91744×10⁻⁴` — matches. At the 7
resolved angles, my own margins: `36.0°→3.8793, 37.2°→2.1709, 38.4°→7.4946,
38.8°→8.0187, 40.2°→1.4764, 41.4°→1.3095, 41.8°→6.5889` — bit-exact to
Table 1. Zone `[max{margin:Y=1}, min{margin:Y=0}] = [1.4764, 2.1709]`
follows immediately and matches Q3.

**2. Q7's disclosure-gate recomputation — independently reproduced,
confirms the claimed match.** This is the specific instruction I was asked
to verify with special care. Pulling `experiments/089-.../results.json`
directly:

```
p_abs_w(C40, 37.2°) = 2.8127043563514567e-12
p_abs_w(G40, 37.2°) = 2.808672836407139e-12
box_dev(C40, 37.2°) = {ext: 1.22045e-4, abs: 4.37168e-4}
box_dev(G40, 37.2°) = {ext: 1.27557e-4, abs: 4.56913e-4}
```

`box_dev_max = max(...) = 4.5691305539087015×10⁻⁴` (the `abs` leg of
`G40`). `noise_floor = NOISE_MULT(3.0) × box_dev_max × p_abs_w(C40) =
3.855484×10⁻¹⁵`. `Δp_abs = |p_abs_w(G40)−p_abs_w(C40)| =
4.031519944×10⁻¹⁵`. **`resolved_margin = Δp_abs / noise_floor =
1.0456585785601518`** — matching `run.py`'s own printed
`1.045659x` to every digit shown, and rounding correctly to exp-089's own
cited `1.046×` (Learned #4). **Confirmed: the claim reproduces from the
persisted `thermo`/`box_dev` primitives exactly as `run.py`/NOTES.md
state.**

One genuinely minor numerical-hygiene note, not raised by any Phase-2
critique or Red Team's own audit as a live issue but worth naming plainly:
`phase3_synthesis.md`'s own text states the Director's pre-freeze
scratch computation "lands at `1.0455×`," and Red Team's Phase-2 audit
independently states the same `1.0455×` figure. Neither of these is what
the frozen `run.py` script (or my own from-scratch, full-double-precision
recomputation above) actually produces — that computation gives
`1.045659` (which rounds to `1.0457` at 4 significant figures, not
`1.0455`). I traced the source of the discrepancy: if the same formula is
evaluated using the *rounded, printed* intermediate values Red Team's own
audit cites in its text (`box_dev_max=4.569×10⁻⁴`, `p_C40=2.8127×10⁻¹²`,
`Δp_abs=4.031×10⁻¹⁵` — each already rounded to 4 significant figures
before division), the result lands at `1.0456` (with the hand-rounding in
that intermediate step landing one figure short at `1.0455` depending on
exactly how the final division was carried out by hand). So
`phase3_synthesis.md`'s own explanation — "not a discrepancy, a
rounding-display difference" — is directionally correct in substance (both
figures round to exp-089's own cited `1.046×` at 3 significant figures,
and nothing in the record treats `1.0455` as authoritative over
`run.py`'s own `1.045659`), but the specific mechanism it names (rounding
the *final* answer under round-half-up) is not quite what actually
happened (the difference traces to rounding *intermediate* quantities
before dividing, in the two independent by-hand checks, not to a rounding
convention applied to one shared precise value). **Non-load-bearing, does
not change any classification, verdict, or the zone/`m₅₀` figures
actually used anywhere** — but a future citation should quote `run.py`'s
own persisted `1.045659×` (or exp-089's own `1.046×`), not the
`phase3_synthesis.md` scratch figure, if the two are ever placed side by
side again.

**3. Q8 (distance-to-crossing comparator) — reproduced bit-exact.**
Independently locating `delta_scene(θ)`'s zero-crossings in exp-083's own
31-point window by linear interpolation: `37.1272°, 38.5902°, 40.2654°,
41.4609°` — matches. Nearest-crossing distances at the 7 angles match
Table/Q8 exactly (e.g. `37.2°→0.0728°`, `40.2°→0.0654°`, `41.4°→0.0609°`).
Distance-zone `[0.0654, 0.0728]`, gap ratio `0.0728/0.0654 = 1.11211` —
matches `1.1121`. Margin's own gap ratio `2.1709/1.4764 = 1.47045` —
matches `1.4704`. **Q8's central claim (margin is empirically ~3× more
robust than distance-to-crossing, not merely theoretically equivalent) is
independently confirmed, not merely restated.**

**4. Q4 (Firth's fit) — independently re-implemented from the formula
alone (not from `run.py`'s code) and reproduced bit-exact.** My own
from-scratch Newton–Raphson on the modified score converges in 20
iterations to `β=(1.78058954, −5.63151961)`, `m₅₀=2.071012796646712` —
matches `run.py`'s `2.071013` to every printed digit, and lands strictly
inside the zone `[1.4764, 2.1709]`, in the upper half, exactly as
predicted.

**5. Full-script reproduction check.** I additionally ran `run.py` itself
in place; the freshly-generated `results.json` produces zero `git diff`
against the committed file — the committed artifacts are not stale or
hand-edited relative to the committed script.

Five independent checks, all load-bearing, all confirmed. Nothing in
NOTES.md's Result section fails to reproduce.

## The Idealization-10 disclosure: adopted, and worded strongly enough

The task specifically asks me to check whether my own seat's Phase-2
finding at this cycle — that the caution zone could be misread as license
to deprioritize sampling in the CAUTION region, when R14's own
`σ_ext(θ)`-differential finding argues the opposite — was actually adopted,
and whether it survived into the record with adequate force now that I can
read it in context rather than as an isolated critique.

**It was adopted, verbatim in substance, as Idealization 10**:

> "The caution zone governs trust in `ratio_k`'s classification label
> ONLY and must not be read as a signal to deprioritize or exclude
> CAUTION-region angles from any future denser `σ_abs(θ)` sampling design
> — if anything, R14's own established `σ_ext(θ)`-differential
> concentration in exactly this region argues those angles should be
> OVERSAMPLED, not skipped."

This is correctly placed (Idealizations section, item 10, one of the
eleven that ship with the frozen predictions), correctly attributes the
mechanism to R14 by name rather than asserting it fresh, and uses the
strong, unambiguous verbs the risk actually calls for ("must not be read
as," "OVERSAMPLED, not skipped") rather than a softened "should be
considered" framing that would have left the misreading available. Reading
it now, in the context of the full finished record — including Q7's own
demonstration that 37.2° (the zone's own upper-edge point) is
*simultaneously* the thinnest-ever resolved-margin point on record — I
judge the disclosure is not merely adequate but load-bearing: it is the
one sentence in this document that keeps a plausible, well-intentioned
future misuse (treating CAUTION as "avoid" rather than "look harder") from
propagating into Iteration 68's own already-named Tier-1/3 `σ_abs(θ)`
build. I would not ask for anything stronger. The one thing I would flag
forward, not as a defect but as a genuine risk this document cannot itself
close: Idealization 10 is prose, in a NOTES.md file, and this program's
own record (T16's "24×" error, the R4/R9 disclaimer-erosion lineage
firing four times running before this cycle) shows that a correctly-worded
prose caveat sitting in one document does not reliably survive being
inherited, cited, or restated by a later cycle's own drafting stage. If
the Iteration-66 board's own still-open "mechanical lint safeguard for the
dual-section-banner gap" (named in this cycle's own Next section) is ever
built, I would ask that it be scoped broadly enough to also catch a future
`σ_abs(θ)` proposal that imports this zone's numeric bounds without
importing Idealization 10 alongside them.

## From the energy-ledger lens: no new finding this cycle produces, and that is correct

This is a zero-FDTD desk-statistics cycle; it computes no new `p_abs_w`,
`dt_ss_full_K`, or `ratio_abs_ext` value, and Idealization 7 says so
explicitly. I looked specifically for any place the record might have
smuggled an energy-ledger claim in under statistical cover — it does not.
Q7 reaches into the `thermo`/`box_dev` primitives, but only to recompute a
*measurement-noise-floor* quantity (the `resolved`-gate margin), not an
absorbed-power or detectability number; the document is careful to label
this "a SEPARATE quantity from Q3's `frac_contrast`-based margin," and
that separation holds up under my own re-derivation. Idealizations 2 and 8
correctly decline to re-adjudicate the mechanistic question (already
answered, differently, by exp-089's own five-way-converged
numerator/denominator decomposition, in which my own seat's
`σ_ext(θ)`-flatness argument was one of three complementary explanatory
layers Red Team ruled mutually consistent). This cycle does not need, and
correctly does not attempt, its own energy sidecar. That is the right
scope discipline for a T28 desk-instrument-calibration cycle, matching
every T28 cycle since exp-069.

The one place I would keep a THERMODYNAMICS eye on going forward, named
here for continuity rather than as a finding against this cycle: Q7's own
disclosure that 37.2°'s `ratio_k=3.4433` reading rests on a `p_abs_w`
difference resolved at only 1.046× its own noise floor means that, quite
apart from the *classification-label* fragility the zone's own LOO table
already flags (dropping 37.2° widens the zone's upper edge to 3.8793), the
*underlying absorbed-power measurement* at that angle is itself close to
this program's own noise-floor discipline. A future `σ_abs(θ)` build that
resamples 37.2° should not assume the existing `p_abs_w(C40/G40, 37.2°)`
pair is a settled anchor to difference against — it is the single
thinnest-margin absorbed-power measurement on the entire T28 board, and a
repeat run there (already named in this cycle's own Next item 5) would
usefully re-resolve it at the same time it re-resolves `ratio_k`.

## Ranked top-3 candidate directions for Iteration 68

1. **A repeat/denser FDTD measurement at or near 37.2°, run jointly with
   the still-overdue R3 spatial (`cpl`) resolution check on this channel.**
   This is this cycle's own named Next item 5 and MATERIALS' Phase-2
   attack (Idealization 9), and from my own seat's lens the two are the
   same underlying instrument-trust question asked twice: 37.2° is
   simultaneously (a) the point whose thin `resolved`-gate margin (1.046×)
   this cycle's own Q7 flags as the operationally live risk, (b) the point
   setting the caution zone's upper edge and Firth's shallow-end anchor,
   and (c) one of exactly two points (with 40.2°/41.4°) whose
   `frac_contrast` has never been resolution-checked, undischarged three
   cycles running (exp-088, exp-089, exp-090). A single `cpl`-20→30 rerun
   at 37.2° (and ideally 40.2°/41.4°, which set the zone's *lower* edge)
   would close both gaps at once, at the one location this program's own
   record already says matters most.

2. **The Tier-1 individual-`σ_abs(C40,θ)`/`σ_abs(G40,θ)` build across a
   denser angle set, explicitly designed from the start to oversample the
   CAUTION-zone/near-crossing neighborhoods rather than sample them
   incidentally.** This is already the near-unanimous #1 item on the whole
   T28 board (named at Iterations 65/66/67 running), and this cycle's own
   Idealization 10 is the correct standing instruction for how to design
   it once it is finally scheduled: the angles this fit flags as
   least-trustworthy for classification are, by R14's own established
   mechanism, the angles where the physical quantity that build exists to
   resolve is most active. I rank this second, not first, only because
   item 1 is cheaper and would improve the very inputs this build would
   consume.

3. **PHOTONICS' still-overdue grazing-incidence validity check
   (`edge_diffraction_c_empty_corrected`).** Unrelated to this cycle's own
   deliverable, but it remains the single most-repeated, near-unanimous #1
   item on the entire T28 board across multiple iterations running and
   should not keep losing ground to desk-cycle work indefinitely, however
   productive that work has been. I rank it third rather than first
   because, unlike items 1–2, nothing in this cycle's own record makes it
   newly urgent — it is simply overdue.
