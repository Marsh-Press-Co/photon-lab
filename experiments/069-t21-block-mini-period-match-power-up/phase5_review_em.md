# PHASE 5 — REVIEW · ELECTROMAGNETISM · Panel Iteration 46 (exp-069)

*Fresh sub-agent, ELECTROMAGNETISM charter (PANEL.md seat 3: field/wave
behavior, reciprocity/passivity/causality bookkeeping). Blind to any other
seat's Phase-5 review this cycle. My own Phase-2 self (`phase2_critique_em.md`)
flagged the "exact global period" overclaim and the `ptp/|mean|`
ill-conditioning risk — this review checks the RESULT independently against
those and against the raw data, not merely restates them.*

## Verdict: PARTIAL

Process discipline this cycle is close to exemplary — the Combined Verdict
logic, once I read `run.py::score()` line by line, correctly implements
every mandatory fix Red Team's Phase-2 audit specified, and I independently
re-executed `_fixed_period_fit`/`_free_period_search` against the raw
`results.json` rows and reproduced R²=0.2016 (fixed T) and P*=2.8421°/
R²=0.6272 (free) bit-for-bit — this is not a "trust the prose" situation,
the numbers are real and correctly computed. The LOCKED mandate's own bar
("build the properly-powered version or formally retire it, no further
relabeling") is met honestly: the pre-committed non-decisive-outcome rule
fired exactly as specified, in code, and the test is genuinely retired, not
argued around. That is real, load-bearing progress on a program-integrity
debt.

But the substantive physics question this instrument was built to answer —
is there a real coherent-fringe effect underneath T24's `ABSORB`
systematic, and if so what is it — is **not resolved, only renamed**. T28
is real (my own re-derivation below independently corroborates this, on
different grounds than the design's own P-069-1/4/5), but its mechanism is
open, and the two most likely candidate explanations (a second boundary-
reflection interference length scale vs. an unmodeled beat/harmonic of
T21's own fringe) are not yet distinguished. This is structurally the same
verdict shape as T24's own opening (Iteration 23) and T27's own opening
(Iteration 42): a rigorous instrument result that closes a citation-
discipline debt while opening a new, better-characterized question. Not
RULED OUT (nothing here bounds a mechanism class); not PROMISING outright
(the headline test's own three-way branch landed in the "non-decisive,
formally retired" bucket, and the mechanism behind its replacement thread
is unidentified, not merely underdeveloped).

---

## 1. Is there a physically sensible mechanism for T28's own ~2.84° period?

**Yes — and first-principles reasoning rules out the laziest explanation
(that it is secretly T21's own fringe, phase/amplitude-shifted) more
sharply than anything in the committed record states.**

### 1.1 The clean argument: same-frequency superposition cannot change frequency

`A_HALF_APERTURE=752` is asserted **bit-identical** for `C40` and `C80`
(`design_geometry.py`: `assert CONFIGS["C40"]["A"] == A_HALF_APERTURE ==
CONFIGS["C80"]["A"]`), and P-069-G1 independently confirms both configs'
own `C_empty(θ)` readings reproduce exp-065's committed values exactly. So
if T21's edge-diffraction fringe were the *only* oscillatory contributor to
each config's own `C_empty(θ)`, both `C_empty(C40,θ)` and `C_empty(C80,θ)`
would be sinusoids **at the identical angular frequency** ω=2π/P(θ) (same
A ⇒ same ω), differing only in amplitude and phase (a real reflection
coefficient and phase shift that plausibly does depend on `ABSORB`). A
linear combination of two sinusoids at the *same* frequency —
`a₁cos(ωθ+φ₁) − a₂cos(ωθ+φ₂)` — is **itself a sinusoid at that same
frequency**, for any a₁, a₂, φ₁, φ₂. This is not a modeling assumption; it
is the addition formula for cosines, exact.

So a delta series whose *own* best-fit period (P*=2.84°, R²=0.63, a solid
fit — see §2) is 45% away from T21's P(39°)=1.96° **cannot** be explained
as "T21's fringe, just with different amplitude/phase between the two
configs." That linear-combination argument would predict the delta
inherits T21's exact period regardless of how differently C40 and C80
scatter/reflect off their own boundary. The fact that it doesn't is
positive evidence that **at least one config carries a second, physically
distinct oscillatory contributor with its own characteristic length
scale**, tied to whatever differs between C40 and C80 — which, from the
actual committed geometry (`experiments/065-.../design_geometry.py`,
independently pulled below), is *exactly one thing*:

```
C40: absorb=40, pad=0,  nx=360, ny=1584, obj_y=792, y_lo=40,  A=752
C80: absorb=80, pad=40, nx=440, ny=1664, obj_y=832, y_lo=80,  A=752
```

Every interior feature (source, aperture edges, object window) is
translated by exactly `pad` cells; `nx`/`ny` grow by `2×pad`. The
*only* physical difference between the two scenes is that the absorbing
layer itself is 40 cells thick in `C40` and 80 cells thick in `C80` — this
is a pure `ABSORB`-depth sweep with everything else held congruent, not a
"padding" sweep in any looser sense. That reframes T28 precisely: it is
evidence of a genuine, `ABSORB`-depth-dependent interference contribution,
separate from the source-aperture-driven T21 fringe.

### 1.2 Candidate mechanism class: a second diffraction/interference length scale at the boundary

A graded lossy (`ABSORB`) layer is not a perfect sink — passivity permits,
and generically implies, a nonzero, angle- and depth-dependent residual
reflection coefficient (`|r|` shrinks with depth, but need not vanish, and
its *phase* generically varies with both angle and depth — exactly the
mechanism this program's own `graded_black_shell` σ_abs/σ_ext=0.51 finding
already established the coated absorber does NOT reach unity absorption
even at r=78 scale). If the effective phase center of that residual
reflection sits at some depth `δ` inside the layer (not at `y_lo` itself,
and not simply proportional to the full `ABSORB` value), the reflected
wave re-diffracts through the *same* two source-taper edges from an
effectively longer or offset path than the direct wave — a **second
diffraction process with its own effective aperture-offset `A_eff` ≠ A**.
Solving `P(39°)=λ/(A_eff·cosθ)` backward from the measured P*=2.84°:
`A_eff = cpl/(radians(P*)·cos39°) = 20/(0.04955×0.7771) ≈ 519 cells`. I
could not identify a clean geometric constant in the committed config
equal to 519 (not `A`, not `ABSORB`, not `pad`, not `A±ABSORB`, not
`A±pad` at either config) — the effective reflection depth/phase-center is
not a quantity this program has ever measured, so this is exactly what I
would expect from an *unmeasured* boundary reflection-phase mechanism, not
a red flag against the hypothesis. This is a **falsifiable, EM-charter
candidate**, not a hand-wave: it predicts the delta-fringe period should
shift systematically as `ABSORB` alone varies (holding `A` fixed), and
`C60`/`C70` (`ABSORB=60/70`, congruent construction, **already built** in
`experiments/065-.../design_geometry.py`, unused this cycle) let it be
tested at zero new `lab/` diff and modest FDTD cost — see §5, my ranked #1.

### 1.3 Sampling sanity check — this is not an aliasing artifact of T21's own fringe

At 0.2° step, T21's own period (1.96–1.99° across the window) is sampled
at ≈9.8 samples/period — comfortably above Nyquist (2 samples/period).
This rules out the possibility that the fixed-period fit's poor R²
(0.20) or the free-fit's different P* are artifacts of under-sampling
T21's own fringe; the design genuinely has the resolving power the mandate
asked for. Whatever is driving the mismatch is a real feature of the
`delta(θ)` series, not a sampling problem — reinforcing §1.1 rather than
competing with it.

### 1.4 Reciprocity/passivity/causality — nothing here is anomalous

This is a purely forward, linear, passive FDTD calculation (soft-source
injection into a graded-lossy-bounded box, no gain, no nonlinearity). A
depth-dependent, angle-dependent residual reflection coefficient from a
graded absorbing boundary is unremarkable and fully consistent with
passivity (`|r|≤1` throughout, and the measured `C_empty` magnitudes
— 10⁻³–10⁻² — are far below any Cauchy–Schwarz-type bound this program has
derived for this instrument, e.g. T26's own re-derived [−100%,+800%]
ceiling for N=9 coherent sums, which doesn't even apply to a single-angle
reading). Causality: `STEPS=2800` is independently confirmed settled to
~2×10⁻⁵ relative for `C80` at both tested angles (P-069-4) — the wavefront
has had ample time to traverse the domain and ring down; nothing about the
new finding depends on an unconverged transient. I find no
reciprocity/passivity/causality objection to T28 being real.

---

## 2. Independent re-derivation of the period fits — reproduces exactly

I did not take `R²=0.6272 at P*=2.84°` on faith. I loaded `run.py`'s own
`_fixed_period_fit`/`_free_period_search` functions directly, fed them the
raw `theta`/`delta` pairs from `results.json`'s own `block_dense.rows`
(not the pre-computed `scored` block), and reran both fits from scratch:

```
P-069-2 independent recompute: R^2 = 0.20164960065653104   (reported: 0.20164960065653104)
P-069-3 independent recompute: p_star_deg=2.8421052631578947, r_squared=0.6272134587910355
                                                              (reported: same, to all digits)
ptp=0.004026256293785282  mean=-0.000248529423384259  ratio=16.200320424677294  (all match)
```

Bit-exact. I also hand-verified `ptp` two ways: the max delta in the
31-row DENSE table is at θ=37.2° (+0.0019096), the min at θ=41.6°
(−0.0021166); their difference is 0.0040263, matching `ptp` to the last
printed digit. `P(39°,600nm)` recomputes to 1.9608° via
`P_deg(θ,λ)=degrees(cpl/(A·cosθ))` with `cpl=20`, `A=752` — matches
`P39_600` exactly, and the `rel_dev=0.4495` follows arithmetically
(`|2.8421−1.9608|/1.9608`). I also confirmed the free-search grid: with
`n_grid=400` over `[1.0°,4.0°]`, the reported P* lands exactly on grid
index 245 of 399 — an artifact of a 400-point linear grid (spacing
≈0.0075°), not a suspicious "found" value; the search is doing exactly
what it says. **No fabrication, no rounding games, no cherry-picking** —
this is a genuinely reproducible result from the committed raw data.

One real, if minor, gap: the R3 check (P-069-5) that is supposed to rule
out grid-discretization structure at this scale tested only `θ∈{39°,40°}`
— which happen to sit almost exactly on `delta(θ)`'s own zero-crossing
(`delta(39.0)=+0.000117`, `delta(39.2)=+0.0000332`, `delta(39.8)=
−0.0000697`, all near zero relative to the ±0.002 swing elsewhere in the
window). Near a zero-crossing, a small delta is disproportionately
sensitive to phase, and a resolution change can plausibly move a
near-zero value by a large *relative* factor (measured: 1.97×/2.50×) with
much less physical significance than the same ratio at a peak/trough
would carry. P-069-5's CONFIRM is correctly computed and the sign held
both times (a real, reassuring fact), but it is weaker evidence for
"survives resolution, real physical feature" than testing it at the
θ≈37.2°/41.6° extremes (T21-period-agnostic, largest-amplitude points)
would have been. Does not overturn P-069-5's CONFIRM; does mean "not a
resolution artifact" is better supported at the *sign* level than at the
*magnitude* level.

---

## 3. Passivity/energy sanity check on `ptp/mean=16.2` (P-069-1)

**Physically unremarkable — this is not a "16× amplification" of
anything.** My own Phase-2 critique flagged this ratio as ill-conditioned
as `mean(delta)→0`, and the data confirms exactly that reading, not a
magnitude anomaly: `ptp=0.004026` and `mean=−0.000249` are both squarely
inside the range this program has already established for T21/T24-class
quantities at this geometry (T21 fringe amplitudes 0.006–0.03 pre-
correction; T24's own `ABSORB`-boundary systematic 0.002–0.007 absolute).
The large ratio arises entirely because the *mean* of a genuinely
oscillatory (near-zero-mean) series happened to land small over this
particular 31-point window — exactly the failure mode a mean-normalized
ratio statistic has near its own singularity, and exactly what the fixed-
period fit's own coefficients corroborate independently: `a=−0.000514`,
`b=−0.000398` give a fringe amplitude `√(a²+b²)≈0.00065`, consistent order
of magnitude with `ptp/2≈0.00201` once you allow the fit only explains
20% of the variance (R²=0.2016) — the raw oscillation is somewhat larger
than the *fitted* T21-period component, again consistent with a second,
unfit contributor rather than noise. Nothing here suggests instability,
divergence, or any bound this program has derived being approached, let
alone violated. The magnitude is sane; the *ratio* framing (P-069-1's own
headline number) is simply not informative about size on its own — a
point Red Team's own docket item 10 (report raw ptp/mean) correctly
anticipated and the results now bear out.

---

## 4. Does `run.py::score()` correctly implement the Combined Verdict as specified?

**Yes, exactly, on direct code read** (`run.py` lines 341–444):

```python
coherent = p1["refute"] and p2["refute"] and p3["within_tolerance"] and p4["confirm"] and p5["confirm"]
additive = p1["confirm"] and p2["confirm"]
```

This is precisely the 5-way conjunctive gate `phase3_synthesis.md` (docket
item 3) and `NOTES.md`'s "Combined Verdict" section both specify — P-069-4
and P-069-5 are load-bearing conjuncts of `coherent`, not independent
side-rows, which is exactly Red Team's own Attack-1 fix (a prior draft let
P-069-1/2 alone license "not settling" language without checking P-069-4;
this is now structurally impossible — `coherent` cannot be `True` unless
`p4["confirm"]` is `True`). The `additive` branch correctly requires only
P-069-1 and P-069-2, matching the stated "vindicated ⟺ P-069-1 CONFIRM AND
P-069-2 CONFIRM" rule. The `else` branch is the pre-committed
`FORMAL_RETIREMENT_NON_DECISIVE` string, computed in code with the exact
reason text `NOTES.md` pre-committed before the run — I confirmed the
`combined_reason` string in `results.json` matches `NOTES.md`'s
pre-registered text verbatim, not a post-hoc rewording.

Tracing this cycle's actual numbers through the gate: `p1["refute"]=True`,
`p2["refute"]=False` (R²=0.2016 is in the 0.15–0.50 gray zone, neither
CONFIRM nor REFUTE), so `coherent` is `False` regardless of p3/p4/p5 —
correctly forces the third branch. `p1["confirm"]=False` (ratio=16.2 far
exceeds the 1.5 CONFIRM bar), so `additive` is also `False`. The result —
`FORMAL_RETIREMENT_NON_DECISIVE` — is the only branch the code's own logic
permits given these inputs. I find **no discrepancy** between what
`phase3_synthesis.md`/`NOTES.md` say the scoring should do and what
`run.py` actually does. This is a genuine, verified instance of "gate
computed in code, not argued in prose" — the exact discipline this
program's Iteration-45 CHECKPOINT found missing in the prior cycle's own
design of this same test.

---

## 5. Ranked top-3 candidate directions for Iteration 47

**(1) [ELECTROMAGNETISM's own charter — proposing to lead] Isolate whether
T28's period tracks `ABSORB` depth alone, using the already-built C60/C70
configs.** §1.2's candidate mechanism (a second, boundary-reflection-driven
diffraction/interference length scale, distinct from T21's source-aperture
fringe) makes a sharp, falsifiable prediction: the delta-fringe's best-fit
period should shift systematically as `ABSORB` varies at fixed `A`. `C60`
(`ABSORB=60`) and `C70` (`ABSORB=70`) are congruent-construction configs
**already built** in `experiments/065-.../design_geometry.py` (zero new
`lab/` diff, zero new geometry design) — a cheap dense sweep of
`C60−C40` and `C70−C40` (or `C80−C60`, `C80−C70`) at the same 0.2°/31-point
protocol this cycle validated would either show a monotonic period trend
with `ABSORB`-depth separation (confirming the boundary-reflection
hypothesis and giving T28 a real mechanism, closeable in one cycle) or
show the *same* ~2.84° period regardless of which pair is differenced
(ruling out the depth-dependence hypothesis and pointing back toward an
unmodeled beat/harmonic of T21's own fringe — see candidate 2). Either
outcome is decisive and cheap; this is the most direct, first-principles
test my own charter can propose, and it is not resource-competitive with
R_contact (desk/literature work, orthogonal).

**(2) A desk-only beat/harmonic check between T21's P(θ) and T28's P*≈2.84°,
before any further FDTD spend.** §1.1's exact argument (same-A linear
combinations cannot change frequency) is airtight for *pure* two-term
superposition, but the real signal could still be a genuine beat between
T21's fringe and a second, close-but-not-identical-frequency oscillation
(not literally the same object, but still geometrically related — e.g., a
slightly different effective `A` for the reflected-wave component versus
the direct one). NOTES.md's own "New live thread" section flags 2.84/1.96
≈1.45 as "not obviously a clean harmonic" but does not attempt a beat-
frequency reconstruction from the *existing* 31-point dataset (e.g.,
fitting a two-frequency model `c₀+Σᵢ aᵢcos(ωᵢθ)+bᵢsin(ωᵢθ)` with one ω
fixed at T21's own and the second free, and comparing its R² against the
single-frequency P-069-3 fit already computed) — a genuinely zero-cost
desk check on data already sitting in `results.json`, directly informed by
my own §1.1 argument, and a natural companion to candidate (1) rather than
a competitor for it.

**(3) The real, dedicated `R_contact` literature search** — PLAN.md's
still-standing Iteration-46 queue item #2, correctly disclosed as
untouched this cycle (Idealization 9, matching the Red-Team-mandated
disclosure), now carried forward a further consecutive cycle. Not gated to
any rotation slot, orthogonal to FDTD budget, and the only queued item
across four cycles now that can move a real materials/thermal number
(TD-5's 7.8× margin) rather than relabel or re-verify one. I rank it #3,
not #1, because — unlike Iterations 43/44/45 — this cycle's own record
gives no indication R_contact was silently dropped; it was explicitly
disclosed per the mandatory fix, and T28 is the fresher, more directly
actionable physics thread this cycle itself produced. But a further
undisclosed deferral, or continued silence on *why* WebSearch/WebFetch
tooling remains blocked, would be worth flagging at Iteration 47's own
close.

**Not recommended as a near-term priority**: re-opening the retired
`P-VIS42-10` period-match test itself in its old form. The pre-committed
non-decisive-outcome rule fired correctly and the test was built to the
mandate's own specified power — re-litigating that closure would
contradict the very discipline this cycle exists to demonstrate. T28 is
the legitimate successor question; the old instrument's own retirement
should stand.
