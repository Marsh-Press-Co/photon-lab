# exp-115 — Phase 5 review — **PHOTONICS**

*Panel Iteration 92. Fresh context. Worked alone: no sub-agents, no
delegation, no simulations, no git state changed. Every figure below was
recomputed this session in pure python against committed JSON and
committed source, or re-derived from primitives; none is restated from
the proposal's, any critique's, or `result_text`'s prose. I did not read
any other seat's `phase5_review_*.md`.*

---

## 1. Verdict

# CONFIRM — with three named defects, none outcome-reversing

**Tier(s) addressed: NONE.** T1 escape route: N/A. This is an
instrument-fidelity / governance cycle under PANEL.md's Iteration-92 scope
amendment; it records none of the seven metric rows, and the article its
M9 sidecar describes fails constraint 3 by construction. Nothing here is
Tier-W or Tier-A progress and the record says so on both sides.

From my charter specifically — *is the optical response coherent as
stated, across wavelength and angle?*

- **Across wavelength: YES, and correctly.** `τ_true`'s construction,
  its bit-identity across the two family members, its λ-dependence and
  the 2.05× red-weakening all re-derive exactly and sit where the
  physics requires (F3).
- **Across angle: the physics is right but the record is INCOMPLETE.**
  The sidecar prints a `2·exp(−τ_true) = 5.1793×10⁻⁴` upper bound and,
  in the same paragraph, per-bin deviations 28× and 102× larger, with no
  reconciliation. The reconciliation is exact, uses only committed
  numbers, and *confirms* the corrected physics rather than embarrassing
  it — but it is not stated (F4).
- **One shared-instrument defect surfaced.** `lab/sections.py`'s
  documented angle convention is inverted relative to its own
  implementation. exp-115's constraint-2-adjacent `±138.75°` claim is
  **correct under the code and wrong under the docstring it cites four
  lines away** (F5).

The scored core is sound: every scored quantity reproduces bit-exact from
committed code against the committed readings, and the pre-registered
Predictions block is byte-identical to its generator (F1, F2). M5
CONFIRM, M3 G-DURATION-INVARIANT, M4 REPEATABLE, M6 AMBIGUOUS and M7
N2_HOLDS are all correctly computed against correctly pre-registered
bands. My reservations are about what the record *says*, not what it
*computed* — with the single exception of F9, where the cycle's own
committed session-1 data materially qualifies M3/M4's robustness and is
not read.

---

## 2. Findings

### F1 — Full bit-exact reproduction of the analysis from committed code

I re-imported `analyze115.py` in a scratch process, re-ran
`analyze(json.load(data/readings.json))` and
`R.build_result_text(...)` / `R.build_predictions_text()`, and diffed every
leaf against `results.json` (recursive dict/list walk, 100% coverage of
the recomputed tree).

- **`result_text` identical: True. `predictions_text` identical: True.**
  Byte-for-byte, from committed code alone — the R23 First Addendum's
  "committed, re-invocable call site" standard, satisfied.
- **16 leaf mismatches, all last-ulp**, every one inside the `τ_true`
  desk integral and its derivatives (e.g. `tau_true_recomputed_cpl25`
  `8.258813114090950` here vs `…952` filed; `wrong_by_factor`
  `3861.508209872947` vs `…954`). Max relative deviation `6.45×10⁻¹⁶`,
  attributable to numpy 2.5.0 (this machine) vs 2.4.6 (the bench,
  `results.json:machine_state.numpy_version`) summation order over a
  2,000,001-point trapezoid. **Every scored field — M1…M7, all gates,
  every verdict string, every boolean — reproduces exactly.** The
  sidecar's own gates run at `1×10⁻¹²` and `1%`, four and fourteen orders
  above this.

### F2 — Every pre-registered band honored exactly, and the pre-registration itself verified byte-for-byte

`NOTES.md`'s `## Predictions (committed before any run)` fenced block
(NOTES.md:453–618) is **byte-identical** to `R.build_predictions_text()`
— extracted by heading, `difflib` reports 0 diff lines. `run115.py`,
`chunk_runner115.py`, `analyze115.py` and `NOTES.md` were committed at
`f75b905` ("PREDICTIONS COMMITTED before any run"); the readings arrived
at `5bb62cc` / `ffa81c5`. Pre-registration is therefore not a claim, it is
a verified property of the tree.

Bands re-derived independently rather than restated:

| Metric | Band as filed | My re-derivation |
|---|---|---|
| M3 | `0.037982123779318644` / `0.07596424755863729` | `R_DEG/2`, `R_DEG` ✓ |
| M4 | `0.02 / 0.03 / R_DEG/2 / R_DEG` | matches the frozen table ✓ |
| M5 CONFIRM in `G` | `[2.0785394, 2.8121415]` | `0.85·3.6680107109370383/1.5 = 2.0785394029`; `1.15·…/1.5 = 2.8121415451` ✓ |
| M5 REFUTE in `G` | `≤1.7117383`, `≥3.1789426` | `0.7·…/1.5 = 1.7117383`; `1.3·…/1.5 = 3.1789426` ✓ |
| M6 | `0.152950039837078` / `0.305900079674156` | R28's founding miss and its double ✓ |
| M7 | `0.05` / `±0.152950039837078` | ✓ two-sided, as MF-9/RT-14 required |

Operands, re-derived from `data/readings.json` per-step rates:
`G_short = 0.11239203476905822 / 0.04858939027786255 = 2.3130982736423493`
(**bit-identical** to filed); `G_pair1 = 2.2296275647790664` ✓;
`G_pair2 = 2.2622534289060674` ✓; `G_sustained = 2.245940496842567` ✓.
`d_dur = |G_short − G_sust| / G_short = 0.02903368938753793` ✓ (the
denominator is the *short* reading, matching `R_DEG`'s own definition at
`run115.py:156` — pre-registered in code, not in the prose table; the
alternative normalization gives `0.02990`, same verdict).
`d_rep = |G_p2 − G_p1| / G_p1 = 0.014632876…` ✓.
`rel_dev = |3.3689107452638507 − 3.6680107109370383| / 3.6680107109370383
= 0.0815428…` ✓. `T = G / G_E = 0.8180425684…` ✓.
`excess = G/2.25 − 1 = −0.0018042236…` ✓.

Protocol-mismatch interval, re-derived from the two-point relation by
hand: `C₁₅₆ = (p_S − p_U)/(1/1000 − 1/3334) = −1.154273…`,
`p₁₅₆,∞ = 0.049743664…`; `C₂₃₄ = +2.075988…`, `p₂₃₄,∞ = 0.110316045…`;
`G_burst = 2.2458389`, `G_prod = 2.2276296`, `G_∞ = 2.2176904` ✓ all
three. Interval `[2.2176904, 2.2458389]`, width 1.27%, entirely inside
CONFIRM — `m5_protocol_caveat = False` is correct, and M5 **may** move
exp-114's LOGBOOK entry.

Cited line ranges checked against source — **no R4 defect found**:
`lab/sections.py:150` is exactly `"sigma_ext": (p_scat + p_abs) / i_inc`;
`lab/sections.py:212–215` is exactly the "square-path angular sample, not
a true circular far-field pattern" idealization;
`experiments/108-…/run.py:244–254` is exactly the `confirm_all_margins`
loop over `MARGINS = (24,32,40,48,57,65)` against
`ITEM_I_CONFIRM_REL = 0.05` (run.py:60, 67) — and that loop is indeed
**ungated**, confirming the "330× looser decision bar" characterization.

### F3 — The M9 sidecar's corrected physics is right at 600 nm, and coherent across wavelength

Re-derived from primitives, not read back:

`lab/materials.py:64–71` gives the quintic smoothstep `s(d)` and returns
`(s, 0.5 s²)`; `graded_black_shell` (materials.py:97) writes
`σ = σ_max · sig/0.5 = σ_max s²`. `run115.py:543–556` forms
`n = √(1 + i σ·cpl/2π)`. That normalization is correct for this engine:
in grid units `c = dx = ε₀ = 1` and `λ = cpl` cells, so `ω = 2π/cpl` and
`σ/(ωε₀) = σ·cpl/2π` — the complex permittivity, exactly.
`run115.py:559–566` forms `τ = 2·(2π/cpl)·L·∫₀¹ Im n dd`; the leading 2 is
`α = 2k₀ Im n`, the **intensity** convention. So:

> **`τ_true` is a one-way INTENSITY optical depth.** One-way *amplitude*
> attenuation is `exp(−τ/2)`; a core-reflected wave makes a round trip,
> so `|δA_core| ∝ exp(−τ_true)`, and `|δA_core|² ∝ exp(−2τ_true)`.
> Writing `A = A_shell + δA_core`, `δΣ/Σ = [2Re(A_shell* δA_core) +
> |δA_core|²]/|A_shell|²`. The leading term is first order in the
> returned amplitude, scale `exp(−τ_true)`, bounded by `2·exp(−τ_true)`
> via `|2Re z| ≤ 2|z|`. **MF-1's correction is right, and its internal
> conventions are mutually consistent.** `exp(−2τ_true)` is the
> `|δA|²`-only term; the stated `wrong_by_factor = exp(+τ_true) =
> 3861.508` correctly compares *scale to scale*, not scale to bound.

Two structural checks the record does not make, and that hold:

1. **The bound is genuinely an upper bound.** A PEC core has `|r| = 1`,
   the maximal case, so the perturbation tested is the worst one in its
   own class. Multiple internal round trips form a geometric series with
   ratio `|r|·exp(−τ_true) ≈ 2.6×10⁻⁴`; the correction to the bound is
   `O(10⁻⁴)` relative and negligible.
2. **`τ_true`'s bit-identity across family members is algebraically
   forced, not empirical.** Both `σ_max·cpl = 10` and `L/cpl = 2.4` are
   held, so `σ·cpl/2π = 1.5915` (the integrand's only parameter) and
   `2·(2π/cpl)·L = 30.159` are *both* invariant: `(0.5, 20, 48)` and
   `(0.4, 25, 60)` are the same optical article evaluated twice. The
   `1×10⁻¹²` bit-identity gate at `run115.py:639` therefore cannot fail,
   and correctly cannot — which is the right reason to keep it (it will
   catch a future family member that breaks the identity), not evidence
   about this one.

**Wavelength (the PANEL.md "≥450/600/750 nm" metrics row, my charter's
own axis).** The 3λ row (`sidecar_m9.c_physics.wavelength_rows`) holds
`σ_max = 0.4` and `L = 60` cells while `cpl` runs 18.75 / 25 / 31.25. That
is the *physically correct* sweep: `dx = 24 nm` is fixed, so 60 cells is a
fixed 1.440 µm of real material and `σ_max` in grid units is a fixed
physical conductivity — a dispersionless conductor, the idealization
`lab/materials.py` actually implements. `cpl` here is `λ/dx`, a
**physical** ratio, not a discretization parameter — the desk integral
runs at 2×10⁶ points and carries no grid error. *The record should say
this*, because a reader arriving from the sidecar's own "CHANNEL AND
RESOLUTION ARE FULLY CONFOUNDED" clause will otherwise read the same
`cpl` symbol as the confounded one.

I reproduce `τ_true` = 8.629338 / 8.258813 / 7.909063 and
`2·exp(−τ)` = 3.5757 / 5.1793 / 7.3480 ×10⁻⁴, and the "2.05× worse in the
red" figure: `exp(8.629338 − 7.909063) = exp(0.720275) = 2.0550` ✓.

**Is that trend physically coherent?** Yes, and it lands where it must.
For a fixed-thickness, dispersionless absorber the two asymptotes are
(i) low-loss `σ/ωε ≪ 1`: `α → σ`, so `τ` is λ-**independent**, ratio
1.000; (ii) good-conductor `σ/ωε ≫ 1`: `α ∝ 1/δ ∝ ω^{1/2}`, so
`τ ∝ λ^{−1/2}`, ratio `√(750/450) = 1.2910`. Here `σ·cpl/2π` runs
1.19 → 1.99 across the band — squarely the transition regime — and the
measured `τ(450)/τ(750) = 8.629338/7.909063 = 1.0911` sits **between**
the two limits, nearer the low-loss end. The article gets optically
thinner toward the red, so backing freedom is weakest there. Correct.

One entry-reflection check the record does not make, and that passes:
`graded_black_shell`'s own docstring bar is "thickness ≥ ~1.5 design
wavelengths." At 750 nm the shell is `60/31.25 = 1.92λ` — still above the
bar, so the `|A_shell|` normalizing the bound does not collapse at the red
end and the 2.05× statement is not contaminated by a front-face-reflection
change. Worth one sentence.

### F4 — Across ANGLE: the bound and the per-bin figures are stated side by side and never reconciled — and the reconciliation *confirms* the corrected physics

`result_text`'s M9 headline says, in one paragraph:

- per-bin deviations "up to `1.4669e-02` at r=156 … and `5.2900e-02` at
  r=312", and
- "the coherent-cross-term scale `exp(-tau_true) = 2.5897e-04`, upper
  bound `2 exp(-tau_true) = 5.1793e-04`".

Taken at face value the measurement exceeds the cycle's own upper bound by
**28.3×** (`0.014669070259562213 / 5.1793×10⁻⁴`) and **102.1×**
(`0.05290046381280309 / …`). The headline is careful to scope its
"SAME ORDER" claim to the *aggregate* channels, so nothing false is
asserted — but nothing reconciles the two either, and a future citation
reading only the quotable blockquote will conclude either that the bound
is violated or that the two numbers are unrelated. Neither is true.

**The reconciliation, exact, from committed numbers only.** The bound
governs `|δA_core|` against a *fixed* reference amplitude; exp-110's
per-bin instrument normalizes each bin by its **own local**
`|A_shell(θ)|²`. Under the common global (peak) normalization the same
margin-32 arrays give (`experiments/108-…/results.json`,
`tier1.<r>.item_i.rel32`, max over 48 bins):

| r | peak-normalized max `|rel32|` | at bin | ÷ `2exp(−τ_true)` |
|---|---|---|---|
| 156 | `1.4760284822434646×10⁻⁴` | `+18.75°` | **0.2850×** |
| 312 | `1.5265673604659632×10⁻⁴` | `−18.75°` | **0.2947×** |

**Under a common normalization the `2·exp(−τ_true)` bound is honored at
every one of the 48 bins at both radii, with ≈3.4× margin.** The apparent
exceedance is *exactly* the normalization change: `28.32/99.38 = 0.2850`
and `102.14/346.53 = 0.2947`, where 99.38× and 346.53× are the sidecar's
own local-vs-peak amplification factors (which I reproduce:
`0.014669070259562213 / 1.4760284822434646×10⁻⁴ = 99.382`;
`0.05290046381280309 / 1.5265673604659632×10⁻⁴ = 346.532`). This is the
strongest positive result the sidecar actually contains — MF-1's corrected
coherent-cross-term physics survives contact with the floor-gated per-bin
instrument, at two independent radii, with margin — and it is nowhere
stated.

**Second, R9-adjacent, point on the same sentence.** "On the floor-gated
LOCAL normalization the figure is 99.4x larger at r=156 and 346.5x larger
at r=312" reads as *the same figure under a different denominator*. It is
not: `1.5266×10⁻⁴` is the peak-normalized max at `−18.75°` (the forward
lobe) while `5.290×10⁻²` is the local-normalized max at `+138.75°`. Bin
for bin at `+138.75°` (r=312) the committed margin-32 pattern gives
`peccored = 4.525881126977305×10⁻⁴`, `hollow = 4.7653023377560165×10⁻⁴`,
`|Δ| = 2.394212×10⁻⁵` — so `local_rel = 0.05290046381280309` (bit-exact ✓)
but the **peak-normalized deviation at that same bin is `3.1098×10⁻⁷`**,
and the peak/local pattern ratio there is `1.701×10⁵`, not 346.5. Two
different bins, two different denominators, one ratio presented.
Non-load-bearing, but this is the sentence MF-3 was written to *fix* a
normalization problem in.

### F5 — DEFECT: `lab/sections.py`'s documented angle convention is inverted relative to its own implementation

`lab/sections.py:209–210` and `:223–224` both state:

> "(atan2, source direction = 0 deg = 'backward toward the source',
> 180/-180 deg = 'forward, downstream')" … "angle convention: 0 deg = -x
> (toward the source, 'backward'), +-180 deg = +x (downstream,
> 'forward')."

**The code says the opposite.** Three independent confirmations:

1. **The atan2 arguments and the function's own inline comments.**
   `sections.py:246–247`: `np.degrees(np.arctan2(yy-bcy, x1-bcx))
   # x1 face (mostly forward)` and `…(yy-bcy, x0-bcx)  # x0 face (mostly
   backward)`. With `x1 > bcx > x0`, the **high-x** face maps to ≈0° and
   the low-x face to ≈±180°. The inline comments therefore assert
   0° = forward, contradicting the docstring 37 lines above them.
2. **`widths()`'s own face assignment plus the source position.**
   `sections.py:137` computes `p_back` at the `x0` face and `:139`
   computes `p_fwd` at the `x1` face. The source sits at low x
   (`geom_fixedabs_cpl(156,25)` → `SRC_X = 160`, `CX = 630`; at r=234,
   `SRC_X = 240`, `CX = 945`), so propagation is **+x**: high x is
   downstream. Consistent with (1), inconsistent with the docstring.
3. **The committed data — decisive.** exp-110's margin-32 `peccored`
   pattern peaks at `|θ| = 26.25°` (`36.127` at r=156, `76.989` at r=312)
   and falls to `3.4×10⁻⁵` / `8.0×10⁻⁵` near `±176.25°` — a factor
   `≈10⁶`. For a strongly absorbing disk many wavelengths across, the
   dominant lobe is the shadow-forming **forward** lobe; nothing in
   physics puts a 10⁶:1 lobe on the backscatter side of a black absorber.
   So `0° = forward`, `±180° = backward / observer-return`.

**Consequence for exp-115.** `sidecar_m9.d_per_bin.withdrawal` /
`run115.py:735, 912, 928` state that the two largest resolved r=312
deviations at `±138.75°` are "INSIDE the observer-return hemisphere
PANEL.md scores constraint 2 on." Under the code this is **correct**
(138.75° is 41.25° off exact backscatter, deep in the back hemisphere).
Under the docstring the cycle cites four lines away — `lab/sections.py:
212–215`, for the far-field scope clause — it is **exactly backwards**.
The cycle's one constraint-2-adjacent claim rests on a source whose own
documentation contradicts it.

**Blast radius, bounded.** `experiments/017-trough-angular-pattern/
NOTES.md:22` — the founding cycle of this instrument — propagates the
inverted convention verbatim ("0° = toward the source (backward), ±180° =
downstream (forward)"). `experiments/087-…/phase5_redteam_audit.md:404`
correctly reads `widths()`'s `x0` face as backward, so the two-way split
is unaffected; the inversion is confined to `angular_scattered_pattern`'s
docstring and to documents that quoted it. This is **not exp-115's
defect** — it has stood since exp-017 — but exp-115 is where it becomes
load-bearing, and this cycle is where it was found.

### F6 — R21 exposure: three mandated findings persisted but absent from the result prose; `NOTES.md` has no Result section at all

At the reviewed commit (`main @ ffa81c5`), `NOTES.md:619–621` reads:

```
## Phase 4 — Results

(pending)
```

The Phase-4 results commit (`ffa81c5`) touched only `data/readings.json`,
`data/cg_session2.log` and `results.json`. So **the only result prose in
the repository is `results.json["result_text"]`** — the artifact R21's own
registry text names as insufficient ("must be stated inline in a cycle's
own Result section, **not merely persisted to `results.json`**"). The
string self-certifies: "**M9 … (ANALYTIC SIDECAR, R21: stated here, not
merely persisted)**" — but "here" *is* `results.json`. (For contrast,
exp-114's `## Result` section was written in its own Phase-4 commit
`f491b93`, before Phase 5.)

Content that is persisted and absent from the result prose (`grep` of
`result_text`, case-insensitive; `"450"`, `"750"`, `"wavelength"`,
`"1.5266"`, `"99.4"`, `"346.5"`, `"sensitiv"`, `"DO_NOT_SCORE"`, `"M8"`
all return **False**):

| Missing item | Persisted at |
|---|---|
| **(a) MF-1's mandated 3λ row** and "backing freedom weakest in the red, 2.05× worse at 750 nm than 450 nm, measured only at 600 nm" | `sidecar_m9.c_physics.wavelength_rows`, `.note` |
| **(b) MF-3's mandated peak-normalized companion `1.5266×10⁻⁴`** and the 99.4× / 346.5× amplification | `sidecar_m9.d_per_bin` |
| **(c) all three M8 sensitivities**, including the post-run `sensitivity_v2_with_measured_G_DO_NOT_SCORE` (`straddle_still_open = True`, `signed_dev = −0.124487`, boundary `G ≥ 2.5652851`, measured `G = 2.2459` **below** it) | `results.json.sensitivities` |

(a) and (b) are not optional narration: MF-1 says "**Add** PHOTONICS' 3λ
row"; MF-3 says the local figures must be reported "**alongside** the
peak-normalized `1.5266×10⁻⁴`". Both are satisfied at R16's persistence
level and fail R21's narration level — the exact distinction R21 exists to
draw.

R21's founding instances are exp-099 and exp-100, and its forward clause
makes a **third** occurrence on this channel auto-fire Checkpoint
criterion 4. **I do not think it should fire here, and I recommend it does
not**: the reviewed commit is mid-Phase-5, the Result section is
explicitly "(pending)" rather than written-and-deficient, and every item
above is zero-cost to state. But the exposure is real and must be closed
when the Director writes that section — including deleting or relocating
the "R21: stated here" self-certification, which is the one part that is
wrong wherever it lands inside `results.json`.

### F7 — `k_B = 2.9955` ("pure N² scaling") has a concrete numerical interpretation the record should state, or explicitly decline

The record's own line — "`G` is a MACHINE PROPERTY, not a physics
constant" — is right, but it offers no mechanism for *why* `N²` should
hold, and `N2_HOLDS` is filed with the note that it "requires BOTH
candidate cost models to be wrong." From my seat the mechanism is
checkable and mundane:

**(i) Why `N²` at all.** `geom_fixedabs_cpl` gives `N = 1400` (r=156) and
`N = 2100` (r=234) — ratio exactly 1.5, cells exactly `2.25×`.
`lab/fdtd2d.py:87–123` allocates at least six `N×N`-scale float64 arrays
(`eps_r`, `sigma_e`, `Ez`, `Hx`, `Hy`, the damping array at `:123`) plus a
bool mask. One float64 field array alone is **15.7 MB** at r=156 and
**35.3 MB** at r=234, against **11 MiB of L3** (`results.json:
machine_state.lscpu`, "L3 cache: 11 MiB (1 instance)"); the full working
set is ≈94 MB and ≈212 MB, i.e. **8.2× and 18.4× L3**. Both grids
therefore sit firmly in the DRAM-bandwidth-bound regime of an explicit Yee
stencil, where per-step time is proportional to cell count. `G → 2.25` is
what that regime *predicts*; it is not a coincidence, and it is not a
statement about FDTD's algorithmic complexity.

**(ii) Why slightly *below* `N²`.** `excess = −0.180%`. Any sub-quadratic
term does this, and the required magnitudes are all trivially small
(solved exactly against the measured `G = 2.245940496842567`):

| Model | Required parameter | As a share of the r=156 per-step cost |
|---|---|---|
| `p = a·N² + c` (fixed per-step overhead) | `c/a = 6386.0` | **0.326%** (≈0.16 ms of a 49.7 ms step) |
| `p = a·N² + b·N` (perimeter-scaling work) | `b/a = 7.619` | **0.544%** |
| absorbing layer costs `δ` extra per cell (`absorb = 50`, `edge = 50`, width fixed in cells ⇒ layer cell count `∝ N`) | `δ = 3.81%` | — |

Any one of the three reproduces the measurement. A cache-hierarchy
*transition* between the grids would push `G` **above** 2.25; the measured
sign is the opposite, consistent with both grids already being DRAM-bound
and the larger one amortizing fixed and perimeter work over more cells.

**Recommendation — state it as explicitly NOT-SCORED, or explicitly
decline.** This is a post-hoc mechanism consistent with one ratio, not a
measured result; R5's and R30's lineage forbids presenting a post-hoc fit
as evidence, and two grid points cannot distinguish `a·N²+b·N+c` from pure
`N²` (three unknowns, one equation). Either form is acceptable; what is
not acceptable is a headline `N2_HOLDS` with no stated reading, since the
obvious wrong reading ("FDTD scales as `N²`, therefore `k = 3.0` is the
right cost exponent") is exactly the inference MF-7(b) already warns M5
cannot license.

### F8 — `exponent_B ≡ k_B` identically: M5 and M7 are one number read against two bands

`run115.py` computes `exponent_B = ln(1.5·G)/ln 1.5 = 1 + ln G / ln 1.5`
and `k_B = 3 + ln(G/2.25)/ln 1.5 = 3 + ln G/ln 1.5 − 2 = 1 + ln G/ln 1.5`.
**Algebraically the same quantity**, and bit-identical as filed:
`m5.exponent_234 = m5.exponent_B = m7.k_B = 2.995546218006855`. The
Predictions block flags a "one datum wearing two hats" identity, but only
for M7's *secondary* model comparison; the PRIMARY equivalence is not
stated, and `result_text` prints `exponent_B=2.9955462` and
`k_B=2.995546` on separate lines as though they were two results.
**M5 CONFIRM and M7 N2_HOLDS are not two independent confirmations** —
they are one measurement scored against two bands whose centres happen to
sit 8.0% apart. One sentence fixes it.

### F9 — The interrupted session 1 is a free between-session replicate, and it materially qualifies M3/M4. It is not read.

`data/readings_session1_interrupted_20260905T2354Z.json` holds four
readings on the **same machine, same protocol, same code**, ≈4.75 h
earlier. Recomputed per-step rates and the session-2 change:

| Reading | session 1 | session 2 | s2/s1 − 1 |
|---|---|---|---|
| `S156` | `0.05090948` | `0.04858939` | **−4.56%** |
| `S234` | `0.11712120` | `0.11239203` | **−4.04%** |
| `U156` | `0.05237354` | `0.04970505` | **−5.10%** |
| `U234` | `0.12005273` | `0.11082376` | **−7.69%** |

`G_short`: `2.300578 → 2.313098` (**+0.54%**).
`G_pair1`: `2.292240 → 2.229628` (**−2.73%**).

Three consequences, all derivable from committed data and none stated:

**(a) The scored operand's between-session spread exceeds its
within-session repeatability.** `|ΔG_pair1|/G = 2.73%` is **1.87×**
`d_rep` (1.46%), **72%** of `d_dur` (2.90%), and **3.0×** M3's own margin
below its bar (`0.037982 − 0.029034 = 0.008948`). M4's REPEATABLE and M3's
G-DURATION-INVARIANT are correct *within one session* — which is what they
were pre-registered to test — but they are **not robust to a session
change**, and the cycle's own disk says so. Given that this cycle's whole
lineage (R31, R33) exists because cross-session wall-time comparisons kept
being wrong, that is worth one line in the record. Note the direction of
the R33 argument is unaffected: M5 remains R33-immune by construction
because *both* operands come from one session. What the session-1 data
adds is a measured size for the session term the construction cancels —
and it is not small.

**(b) Contention biases `G` upward — and the magnitude *strengthens*
M6's reading.** The slower session gave the *higher* `G` (2.2922 vs
2.2296), so contention does **not** cancel in the ratio. That is the right
sign to worry about the cloud's `G_E = 2.7455` being partly a contention
artifact (THERMODYNAMICS' Phase-2 finding that exp-114's `R_DEG` anchor is
cloud contention, not duration, points the same way). But the size does
not support it: reaching `G_E` from the bench's `2.2459` needs **+22.24%**,
which is **8.1×** the `+2.73%` that a 4–8% per-step slowdown actually
produced here. On the one lever we have measured, contention cannot
account for the cloud/bench gap — so `T = 0.818`, AMBIGUOUS, is better
read as a genuine machine difference than an artifact. That is a
*positive* finding this cycle can bank at zero cost, and it is the single
most useful thing the wrecked session 1 left behind.

**(c) `loadavg` cannot see the contamination MF-6e wrote it to catch.**
Session 1's per-reading `loadavg_before` is `0.17 / 1.04 / 1.04 / 0.93`;
session 2's is `0.044 / 1.005 / 1.039 / 1.237`. **Statistically
indistinguishable** — yet session 1 ran 4–8% slower on every reading.
Whatever slowed it (Windows-side load invisible to WSL's loadavg, thermal
state, or the fault that killed the host 20 min later), MF-6e's
machine-state block reports "clean" and "4–8% slow" in the same words.
This is this program's own class-rule shape — an instrument that cannot
physically produce the reading that means "bad." The exclusive-use
protocol's real evidence in session 2 is the readings' own mutual
consistency (`d_rep = 1.46%`, contiguous 1–2 s gaps between readings,
loadavg pinned at ≈1.0 = exactly one runnable process for 61.7 min),
**not** loadavg itself. The record should say which of those two it is
relying on.

### F10 — The two same-grid drift rates have opposite signs: no drift systematic is resolved

`results.json.drift`: r=156 `relative_rate_per_hour = −0.016389` (getting
*faster*); r=234 `+0.006718` (getting *slower*). Opposite signs, 6×
different magnitudes, both far inside the ±4–8% session-to-session
variation of F9. MF-6c's rate instrument is correctly built and correctly
composes — I verify that the two rates reproduce `d_rep` exactly:
`+0.2075% − (−1.2377%) = +1.445%` against `d_rep = 1.463%` (the residual
is the second-order term in the ratio). But a drift with opposite signs on
two grids measured in the same 62 minutes is noise, not drift. Report it
as "no drift systematic resolved at this precision," not as a measured
drift rate — otherwise a future cycle will anchor a bracket on
`−0.0164 h⁻¹` the way this one anchored on `R_DEG` (R17).

### F11 — Minor: the scored `G_sustained` lies just outside the interval built to bound it

`G_sustained = 2.245940496842567` (a **mean of ratios**) exceeds
`interval_hi = 2.2458389149395477` (a **ratio of means**) by
`4.52×10⁻⁵` relative. The interval's own note discloses the construction
difference ("a mean of ratios is not a ratio of means, but this is a
bound"). Non-load-bearing — both sit deep inside CONFIRM, and
`m5_protocol_caveat` is unaffected — but an interval whose stated job is
to bound the scored operand should contain it, or say in one clause why
it need not.

### F12 — Minor, R4-adjacent precision: "same order as the measured aggregate deltas"

The headline says the bound is "the SAME ORDER as the measured aggregate
deltas, not orders below them." Against the six aggregate deltas the bound
`5.1793×10⁻⁴` sits at `0.21×` the largest (`1.0874×10⁻⁴`, r=234
`σ_scat`) — same order ✓ — but `91.4×` above the smallest
(`5.666×10⁻⁶`, r=234 `σ_abs`), i.e. nearly two orders. The claim being
rebutted (the withdrawn `exp(−2τ) = 6.71×10⁻⁸`) is 2–3 orders *below* all
six, so the intent holds and the correction stands; the collective
phrasing simply overstates for the small channel. Per-channel phrasing
costs nothing.

### F13 — Constraint 3 and program-integrity: no slip

- `DISCLAIMER_115` is **byte-identical** (3788 characters) between
  `predictions_text` and `result_text`; both builder functions carry
  internal asserts (`run115.py:1185`, `:1252`) and both texts reproduce
  from committed code (F1). R23 First Addendum satisfied.
- "T1 escape route: NONE / N/A" appears on both sides; the article's
  constraint-3 failure by construction is stated **inside** the quotable
  blockquote (MF-4 honored), as are the margin-32 scope, the
  channel/resolution confound, the near-to-mid-field instrument scope, the
  realizability tier and the T18 evidentiary tier.
- Under PANEL.md's Iteration-92 scope amendment this cycle correctly
  records none of the seven metric rows and carries the per-cycle
  disclaimer R23 requires. No constraint-3 slip in this cycle's own
  scoring. The only constraint-adjacent substantive claim is the
  `±138.75°` observer-return statement of F5 — right, on a wrong
  docstring.
- R19 call-count invariant: expected 18, got 18, `repeat_skipped = False`
  ✓; six readings × three scenes, contiguous timestamps
  04:39:25Z → 05:41:04Z, `total_wall_s = 3700.5` against 3699 s of
  elapsed clock.

---

## 3. Defects (R-numbers)

| # | R-number | Statement | Load-bearing? |
|---|---|---|---|
| **D1** | **R18-class** (documented scope vs. actual source), with an R4-class citation hazard | `lab/sections.py:209–210, 223–224` document an angle convention inverted relative to the function's own implementation (`:246–247`), relative to `widths()`'s face assignment (`:137, :139`) with the source at low `x`, and relative to the committed pattern data (10⁶:1 lobe at `\|θ\| ≈ 26°`). exp-115's `±138.75°` observer-return claim is correct under the code and inverted under the docstring it cites at `:212–215`. Also propagated into `experiments/017-…/NOTES.md:22`. | **Yes**, for any future angular / constraint-2 claim. Not exp-115's defect — its claim is right — but exp-115 is where it became load-bearing and where it was found. |
| **D2** | **R21 exposure** (3 items) | `NOTES.md:619–621` Result section is "(pending)"; the only result prose is `results.json["result_text"]`, which R21 names as insufficient while self-certifying "R21: stated here, not merely persisted". MF-1's 3λ row, MF-3's peak-normalized companion figure + amplification, and all three M8 sensitivities are persisted and un-narrated. | Not yet — closable at zero cost when the Result section is written. **Recommend closing, not firing** Checkpoint 4; the reviewed commit is mid-Phase-5. |
| **D3** | **R9-adjacent** (operand commensurability) | The `2·exp(−τ_true)` bound and the local-normalized per-bin maxima are printed in one paragraph on incommensurable denominators, with no reconciliation; and the "99.4× / 346.5× larger" comparison is between two different bins as well as two different normalizations (bin-for-bin at `+138.75°` the ratio is `1.70×10⁵`). The commensurable form — peak-normalized max = `0.285×` / `0.295×` of the bound, i.e. **bound honored at all 48 bins at both radii** — is not stated. | Not to any verdict; materially to how the sidecar reads. |

**Not defects, checked and clear:** the three cited line ranges all
reproduce (F2); no R4 citation defect found; every pre-registered band
honored exactly; `predictions_text` byte-identical to `NOTES.md`'s frozen
block; R23 / R23-Addendum satisfied; R19 satisfied; R33 correctly declared
inapplicable to M5 by construction; R30 / R32 correctly declared N/A.

---

## 4. Ranked top-3 candidate directions

Iteration 93's Tier-1 **item 1 is fixed** by the Director's D2 ruling
(VISION's constraint-3 re-score through `lab/ambient.py`, regardless of
lead; ELECTROMAGNETISM leads 93). I rank **items 2 and 3 of Iteration 93**
and **item 1 of Iteration 94**.

### Rank 1 — Iteration 93, Tier-1 item 2: **Correct `lab/sections.py`'s angle convention, arm a positive control for it, and re-audit every angular claim in the record**

*Zero FDTD, zero grid-steps, one shift.*

1. Fix the docstring at `lab/sections.py:209–210` and `:223–224` to
   `0° = +x = forward / downstream`, `±180° = −x = backward, toward the
   source and the observer`, with the one-line justification (the `x1`
   face is the high-`x` face; the source is at low `x`).
2. **Arm a positive control in the trust suite** — the program's own "a
   watcher is verified by hearing, not by running" rule applied to an
   instrument: assert that the argmax bin of a `graded_black_shell`
   pattern lies within ±30° of 0°. This is a check that *can* produce the
   reading meaning "bad," it would have caught this inversion, and it
   catches any future face / sign transposition. It costs one existing
   capture and no new `Sim.run()`.
3. `grep` and re-audit every "forward" / "backward" / "observer-return" /
   "backscatter" angular-sector claim in `experiments/` against the
   corrected convention; annotate `experiments/017-…/NOTES.md:22` with a
   dated correction rather than editing history.

**Why first.** It is the cheapest item on this list; it is a correctness
fix to a **shared** instrument the whole angular record depends on; the
error has stood since the instrument's founding cycle and has already
propagated once; and it sits directly under PANEL.md's constraint-2
metrics row — which makes it a prerequisite for trusting *any* angular
scoring that Iteration 93's constraint-3 re-score will be filed next to.
Under R18's own standard ("a check's documented scope must be
independently confirmed against its own source code before it is relied
upon"), an instrument whose documentation inverts its implementation is
not yet fit to carry a constraint verdict.

### Rank 2 — Iteration 93, Tier-1 item 3: **Publish the per-bin ↔ bound reconciliation and the 3λ row; close the R21 exposure**

*Zero FDTD, desk only.*

Into the Result section `NOTES.md:619` still owes, state:

- the **commensurable** comparison of F4 — peak-normalized per-bin max
  `1.4760×10⁻⁴` / `1.5266×10⁻⁴` = `0.285×` / `0.295×` of
  `2·exp(−τ_true)`, so **the corrected coherent-cross-term bound is
  honored at all 48 bins at both radii**, and the 28× / 102× local-frame
  figures are exactly the normalization change (`99.38×` / `346.53×`), not
  a violation;
- MF-1's **3λ row** with the 2.05× red-weakening, plus F3's two
  clarifications: that `cpl` in that row is the *physical* `λ/dx` and
  carries no discretization confound, and that the shell stays above
  `graded_black_shell`'s own `1.5λ` entry-reflection bar even at 750 nm
  (`1.92λ`);
- MF-3's peak-normalized companion figure alongside the local ones inside
  the quotable blockquote;
- the three M8 sensitivities, including `straddle_still_open = True` with
  the measured `G = 2.2459` sitting below the `2.5652851` boundary;
- F8's `exponent_B ≡ k_B` identity, so no future citation counts M5 and M7
  as two confirmations;
- F9(b)'s contention arithmetic, which **strengthens** M6;
- F10's "no drift systematic resolved," and delete the "R21: stated here"
  self-certification from `result_text`.

**Why second.** It converts the strongest positive result this cycle
actually produced — MF-1's corrected physics surviving contact with the
floor-gated per-bin instrument at two radii with 3.4× margin — from an
unstated inference into a quotable finding, discharges D2 before it can
become R21's third occurrence, and costs nothing but a shift's writing. It
is second only because Rank 1 changes what "observer-return hemisphere"
*means*, and this item's text quotes that phrase.

### Rank 3 — Iteration 94, Tier-1 item 1: **A third grid point on the same-session control curve, plus one deliberate contention-calibration reading**

*The only item here that spends real bench time; ~35–45 min at r=78 / 117.*

`N2_HOLDS` currently rests on **one ratio between two grids**, and two
points cannot separate `p = a·N² + b·N + c` from pure `N²` — three
unknowns, one equation. This is R15's own addendum shape one domain over
("two such points cannot, on their own, distinguish genuine convergence
from a persistent recipe-level artifact"), and F7 shows a 0.33% fixed
overhead, or a 3.8% extra cost in the absorbing band, reproduces the
measurement equally well.

- Add a **third grid**: `geom_fixedabs_cpl(117, 25)` gives `N = 1050`
  (`k = 1.5`) and `geom_fixedabs_cpl(78, 25)` gives `N = 700` (`k = 1`) —
  both *cheaper* than r=156, so the item is net-cheap. With three points
  the three-parameter model is exactly determined and the `b` / `c` terms
  become measured rather than inferred. Run it ABBA against r=156 in one
  session, matched protocol, so it composes with this cycle's readings.
- Fold in a **deliberate, disclosed contention lever**: repeat one reading
  with a known concurrent load and measure `dG/d(slowdown)`. Session 1
  supplies one accidental point (F9: a 4–8% per-step slowdown moved `G` by
  +2.73%); one deliberate point turns that into a calibration, which is
  the number M6's cross-machine reading most needs and the only way to put
  an error bar on `G_E`.
- Persist a machine-state signal that **can** show contamination —
  per-scene time scatter within a reading, or a short re-timed control
  scene — since F9(c) shows `loadavg` demonstrably cannot.

**Why third.** It is the only item that costs FDTD time, both items above
are zero-cost, and Rank 2's write-up is what tells a future cycle *what
question* the third point is answering.

---

## 5. Summary (≤150 words)

**CONFIRM, T1 N/A.** Every scored quantity reproduces bit-exact from
committed code against the committed readings, and `NOTES.md`'s
Predictions block is byte-identical to its generator — pre-registration is
verified, not asserted. MF-1's corrected physics is right: `τ_true` is a
one-way intensity depth, so the cross term scales as `exp(−τ)` and is
bounded by `2exp(−τ)`; the 2.05× red-weakening is real and sits correctly
between the low-loss and skin-depth limits. Across angle the record is
incomplete: peak-normalized, the bound is honored at all 48 bins at both
radii (`0.285×` / `0.295×`), while the printed local figures read
28× / 102× above it, unreconciled. Three defects: `lab/sections.py`'s
documented angle convention is inverted versus its own code (exp-115's
`±138.75°` claim is right, its cited source is not); an R21 exposure
(three mandated findings persisted, un-narrated; `NOTES.md` Result
"(pending)"); and an R9-adjacent incommensurable comparison. `k_B = 2.9955`
is a DRAM-bandwidth-bound stencil, not a physics exponent.

---

*PHOTONICS, Phase 5, exp-115.*
