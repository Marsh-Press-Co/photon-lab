# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 46 (exp-069, Block MINI power-up)

*Fresh sub-agent, PHOTONICS charter (PANEL.md seat 1): is the proposal's
optical response coherent as stated, across wavelength and angle? Blind to
any other seat's Phase-5 review this cycle. I led this cycle's Phase-2
critique (`phase2_critique_photonics.md`) but review the RESULT
independently here, not by restating that critique.*

## 0. Verification performed before forming a verdict

Independently re-derived, not merely read, from `results.json` and the
committed code (`run.py`, `design_geometry.py`):

- Re-ran `_fixed_period_fit`/`_free_period_search` by hand against the
  committed `block_dense` rows: P-069-2 (`R²=0.20165`) and P-069-3
  (`P*=2.84211°`, `R²=0.62721`) both reproduce bit-for-bit.
- Confirmed `P(39°,600nm)=1.96080°` from `P_deg()`'s own formula
  (`math.degrees(cpl/(A·cosθ))`, `cpl=20`, `A=752`) — matches
  `results.json`'s `p3.P39_600` exactly, and `P*/P(39°)=1.44947` matches
  `rel_dev=0.44946` (+1) exactly.
- Confirmed `run.py::score()`'s Combined Verdict logic (lines 420–441) is a
  faithful, literal implementation of the 5-way conjunction NOTES.md/
  `phase4_results.md` describe: `coherent = p1.refute AND p2.refute AND
  p3.within_tolerance AND p4.confirm AND p5.confirm`; `additive =
  p1.confirm AND p2.confirm`; else `FORMAL_RETIREMENT_NON_DECISIVE`. With
  `p1.refute=True`, `p2.refute=False` (R²=0.202 is in the gray zone, not
  ≥0.50), `p3.within_tolerance=False`, the `else` branch fires correctly —
  the code matches the prose exactly, no discrepancy found.
- Sampling-theory sanity check: at 0.2° step, 1.96° gives 9.8 samples/
  period and 2.84° gives 14.2 samples/period — both far above Nyquist (2
  samples/period). **Under-sampling/aliasing of a true ~1.96° signal into
  an apparent ~2.84° signal is not physically possible at this sampling
  rate** — a clean, sampling-theory-only argument, independent of and
  additional to the FDTD-based R3 check (P-069-5).
- Ran the 750nm leg's own free-period search myself (the design never
  runs one — P-069-6 reports only a fixed-T fit, "context only, not
  scored"). Result: **the search hits the boundary of its own range** —
  `P*→6.0°` when searched over `[1°,6°]`, `P*→4.0°` when searched over
  `[1°,4°]` (matching the 600nm leg's own bounds). This is the classic
  symptom of a window too narrow to constrain any period near or above
  its own span: LEG750 covers only 3.0° (≈1.22 T21-predicted periods, and
  fewer still of the ~2.84°-scale period), so a free search there cannot
  locate an interior optimum. By contrast, re-running the 600nm free
  search over an extended `[1°,6°]` range independently reproduces the
  reported `P*=2.842°` (found at `P*=2.841°` in the wider search) — a
  genuine interior optimum, not a boundary artifact. **This asymmetry is
  not disclosed anywhere in `phase4_results.md`**; P-069-6 is described
  only as "under-powered by design," which is true but understates the
  specific failure mode (a degenerate free-period fit, not just a noisy
  one).
- Built and ran my own cross-wavelength consistency test the design never
  attempts: converted the 600nm free-fit period (`P*=2.8421°` at θ=39°)
  into an implied effective offset `A_eff = cpl/(rad(P*)·cosθ) ≈ 518.8`
  cells (vs. T21's own `A=752`), then predicted the λ-scaled period this
  same `A_eff` implies at 750nm (`T_new = cpl_750/A_eff`, giving
  `P_new(39.5°,750nm) ≈ 3.58°`), and fit the 750nm delta series against
  that **fixed**, wavelength-scaled period. Result: **R²=0.767** — a
  substantially better fit than either the flat null or T21's own
  stationary-phase period fit to the same 750nm data (R²=0.348, the
  number actually reported in `results.json`'s `p6`). See §2.

## 1. Overall assessment of process and headline

The design itself is honest, well-instrumented, and does what it says.
The Combined-Verdict machinery (5-way conjunction, computed in code, no
PARTIAL-and-defer escape hatch) is correctly wired — I could not find a
gap between the code and the prose, which is itself notable given this is
the exact class of defect (a conjunctive safeguard not actually binding
the headline claim) that fired Checkpoint criterion 4 one cycle ago on
this same test's own ancestor. `P-VIS42-10` is retired cleanly, on its own
pre-committed terms, with a real finding surfacing in its place rather
than a fifth deferral. This is good house discipline and I have no
complaint about the process.

The physics questions this review was asked to scrutinize, however,
surface real gaps in how the *new* finding (T28) is characterized —
gaps that understate how interesting, and how coherent, it actually is.

## 2. Is the ~2.84° (600nm) period physically sensible, and does 750nm's
own data show a consistent or inconsistent cross-λ picture?

**Physically sensible: yes, on two independent grounds.** (a) It is
comfortably above the sampling Nyquist limit (9.8×/period at 600nm — not
an artifact of the 0.2° grid), and (b) it survives the cpl 20→30
resolution refinement (P-069-5 CONFIRM, though see §4 for a caveat on
*how well* this rules out grid structure). The signal is real.

**Does it scale across wavelength the way a genuine coherent optical
effect should? The design's own instrumentation cannot answer this
question — LEG750 is 1.22 T21-periods wide, which is not enough to
resolve any period near or above its own span, as its degenerate
free-search boundary-hit demonstrates. But when the question is asked the
right way — not "does T21's OWN period fit 750nm" (a strawman; we already
know T21's period does not fit the 600nm delta signal either) but "does
the SAME physical length scale implied by the 600nm fit predict the
750nm behavior" — the answer is a clean, and quite striking, yes.** The
750nm delta series fits a fixed period derived by simple λ-scaling of the
600nm-implied effective aperture (`A_eff≈519` cells) at **R²=0.767**,
more than double the fit quality (R²=0.348) that T21's own model achieves
on the identical 750nm data — the very number `phase4_results.md` reports
as "suggestive of a shared mechanism across λ." **This is exactly the
signature a real, single-mechanism Huygens-type interference effect
should show under λ-scaling** (period ∝ λ at fixed geometric offset,
tested here via the `T=cpl/A` structural form the program has used since
T21 itself), and it is a materially stronger, more specific claim than
anything in the committed record. It is not proof — 16 points, 3
parameters, and a period derived from the same dataset being tested
against a second, independent (but power-limited) dataset — but it moves
T28 from "an unexplained residual, mechanism unclear" toward "consistent
with a genuine, wavelength-coherent diffraction effect with its own
characteristic length scale distinct from T21's `A=752`." **This
cross-check should have been run this cycle and was not** — the
`phase4_results.md` text that exists ("same qualitative shape... not
scored") is a much weaker and less informative statement than the data
already on hand supports.

## 3. Is the harmonic/beat relationship "checked and inconclusive" claim
audited fairly?

**No — "checked" overstates what was actually done.** The entirety of the
check, per `phase4_results.md`'s own text, is: "2.84/1.96 ≈ 1.45 — not
obviously a clean harmonic." That is a single ratio eyeballed against
small-integer fractions, not a beat-frequency analysis. I checked the
obvious small-integer candidates myself: 3/2=1.500 (3.5% off), √2=1.414
(2.4% off), 10/7=1.429 (1.5% off), 7/5=1.400 (3.4% off) — none matches
cleanly, so the qualitative conclusion ("not a small-integer harmonic")
survives a more careful pass. But the more physically relevant check — a
genuine two-frequency beat model, `1/P_beat = |1/P_a − 1/P_b|` solved for
a plausible second period `P_b` given `P_a=P(39°,600nm)=1.961°` and
`P_beat=2.842°` — was never attempted, and gives `P_b≈6.33°` (difference
beat) or `P_b≈1.16°` (sum beat), neither of which was checked against any
named geometric length scale in `design_geometry.py` (`TAPER=40`,
`GUARD_OUT=185`, `d_sp=223`, absorb thickness 40/80, pad 0/40 — none of
these, nor `A_eff≈519` cells identified in §2, obviously matches either
candidate). The honest state of the record is: the small-integer-harmonic
hypothesis is fairly ruled out; the beat-with-a-named-geometric-feature
hypothesis was never tested, contrary to what "checked" implies; and my
own §2 finding (a self-consistent single new length scale, not a beat of
two existing ones) is a more promising lead than either.

## 4. Does the R3 resolution check (P-069-5) actually rule out what it
claims to?

**Partially, and more weakly than the "CONFIRM... a real physical
feature, not Yee-grid discretization structure" language suggests.** Two
concerns, both optics-fidelity-relevant:

1. **The two R3 cells sit almost exactly at a near-null of the fringe,
   not at a peak.** `block_dense`'s own committed rows show
   `delta(38.8°)=3.9e-5`, `delta(39.0°)=1.17e-4`, `delta(39.2°)=3.3e-5`,
   `delta(39.4°)=-1.07e-4`, `delta(40.0°)=1.67e-4` — all roughly an order
   of magnitude below the fringe's actual peak-to-trough scale (`ptp=
   0.00403`, e.g. `delta(37.2°)=1.91e-3`, `delta(41.4°)=-1.98e-3`). Testing
   resolution-robustness at a near-zero-crossing is a much more sensitive,
   and much less physically diagnostic, test than testing it at a peak: a
   modest resolution-driven PHASE shift of the whole fringe pattern (fully
   consistent with ordinary Yee-grid dispersion, and exactly what this
   program's own T21 record already documents as a real, if smaller,
   effect — LOGBOOK T21, "the SMALLER ±θ magnitude asymmetry" attributed
   to staircasing) would produce a large *relative* change right at a
   node, while being nearly invisible at a peak. The measured ratios
   (`1.97×`, `2.50×` — the signal roughly doubled to two-and-a-half-ed
   under cpl 20→30) are exactly consistent with this reading, not just
   with "genuine physical feature, confirmed."
2. **The CONFIRM band itself is wide** (`ratio∈[0.3,3.0]`) relative to
   the observed values (1.97, 2.50) — both pass, but neither is close to
   1.0 (true resolution-converged stability), and 2.50 sits at 83% of the
   3.0 ceiling. "Survives cpl 20→30 within a factor of 3" is a real and
   useful falsification band (it does rule out sign flips and order-of-
   magnitude blowups, cleanly closing the crudest artifact
   hypothesis) but it is a considerably weaker claim than "confirmed, a
   real physical feature" implies at face value.

**Net: P-069-5 correctly rules out the crudest artifact hypothesis (sign
flip / order-of-magnitude resolution-dependence) but does not, by itself,
establish that the fringe's location and amplitude are resolution-
converged** — a peak-cell R3 check (θ≈37.2° or 41.4°, where the signal is
an order of magnitude larger and far less sensitive to a modest phase
shift) would be a materially stronger test and was not run. This is a
genuine gap, not a fatal one — the finding is not overturned, but the
"decisively ruled out" framing in `phase4_results.md` §3 overstates what
a near-null-only resolution check can show.

## 5. Wavelength-restriction red flag

Yes, one specific to this design, distinct from the general "600nm only"
scope decision (which Phase 2/3 already corrected honestly — the
"least-aliased" justification was properly struck). The remaining issue:
**LEG750 is disclosed as under-powered ("~1.22 periods... context only,
not scored") but the language used to describe its result ("same
qualitative shape... suggestive of a shared mechanism across λ") implies
more cross-wavelength support than a 1.22-period, degenerate-free-search
leg can actually provide.** §2 above shows the leg's data, read
correctly, is actually MORE informative than that hedge suggests (R²=
0.767 against the right, λ-scaled hypothesis) — but that is a finding
this review had to extract by re-analysis, not one the committed record
states. The primary claim (T28 is real) is properly scoped to 600nm only,
which is honest; the throwaway characterization of the 750nm leg is where
the imprecision lives.

## Verdict for this cycle: **PARTIAL**

The instrument-closure mandate itself is executed cleanly and honestly —
`P-VIS42-10` is retired on its own pre-committed terms, no relabeling, no
escape hatch, and the Combined-Verdict code matches its own prose exactly
(independently re-verified, §0). From my own charter, that process
integrity is real progress and not in question.

But the substantive optical-coherence question this cycle's headline
finding raises — is the `C80−C40` fringe a genuine, wavelength-coherent
diffraction effect with its own characteristic length scale, and is it
truly resolution-converged — is **not yet closed, and is currently
under-characterized relative to what the existing data already supports**
(§2's λ-scaling fit, R²=0.767, is a materially stronger cross-wavelength
signal than anything in the committed write-up; §4's near-null R3
placement is a materially weaker resolution check than the "decisively"
language implies). Not RULED OUT — the sampling-Nyquist argument and the
λ-scaling check both push toward "real, coherent effect," not artifact.
Not PROMISING outright either — that would overstate a still-single-λ-
powered, still-peak-untested finding as more settled than it is.

## Top-3 ranked candidate directions for Iteration 47 (my own charter,
not a restatement of PLAN.md's queue)

1. **Properly power T28 at 750nm (and ideally 450nm), mirroring Block
   DENSE exactly** — ≥3 periods of the NEW ~2.84°(600nm)-family period
   (not T21's), 0.2° step, settled STEPS=2800, same C40/C80 congruent
   construction. This is the single most decisive, cheapest (zero `lab/`
   diff, reuses this cycle's own harness verbatim), and most directly
   PHOTONICS-charter-relevant next step: it would turn §2's post-hoc
   R²=0.767 λ-scaling check from a suggestive re-analysis into a
   pre-registered, properly-powered falsification test — either
   confirming a genuine coherent optical mechanism with a new
   characteristic length scale (a real, named finding, T21-precedent
   shape), or refuting it cleanly.
2. **Trace the physical origin of the implied `A_eff≈519`-cell offset in
   the C40/C80 congruent construction.** The two configs share `A=752`
   (the source-taper-to-aperture offset T21 governs) by explicit
   construction, but differ in `absorb` (40 vs 80), `pad` (0 vs 40), and
   consequently `src_x`/`plane_x`/`obj_x`/`ny`. A short EM-charter-
   adjacent geometric derivation of which of these differences produces a
   diffracting or reflecting feature with a ~519-cell effective offset
   would let T28 graduate from a fitted residual to a named,
   zero-free-parameter mechanism — the same path that took T21 itself
   from an "unexplained fringe" (Iteration 18) to a "Red-Team-verified,
   zero-free-parameter model" (Iteration 19).
3. **Re-run the cpl 20→30 R3 check at one or two peak cells of the DENSE
   sweep** (e.g. θ≈37.2° or θ≈41.4°, |delta|≈0.0019–0.0021, an order of
   magnitude above the near-null θ=39°/40° cells actually tested), not to
   overturn P-069-5's CONFIRM but to tighten it — a peak-cell ratio close
   to 1.0 would make "not a grid-discretization artifact" a genuinely
   strong claim instead of a "survives within a generous 3× band at a
   phase-sensitive null point" claim, closing the gap §4 identifies at
   near-zero marginal cost (2 more FDTD calls at cpl=30).

R_contact (PLAN.md queue item #2) is outside this seat's charter and is
not re-argued here; MATERIALS owns that bound.
