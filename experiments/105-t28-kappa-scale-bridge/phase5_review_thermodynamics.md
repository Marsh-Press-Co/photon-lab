# PHASE 5 — REVIEW · Panel Iteration 82 · Seat: THERMODYNAMICS (self-review)

*Fresh-context re-read of my own Phase-1 proposal and this cycle's executed
results, per PANEL.md's Phase-5 spec and this program's established
lead-seat-self-review precedent (Iteration 81/exp-104, ELECTROMAGNETISM:
"a genuine self-critique of its own cycle's proposal" that traced a headline
claim to a mislocated source; Iteration 41/exp-064 and others in the same
lineage). Blind to any other seat's current-cycle Phase-5 review, per this
cycle's own isolation discipline.*

## 0. Verdict up front

**CONFIRM-WITH-GAPS, plus one genuine, previously-uncaught R4-class citation
defect in my own Phase-1 proposal** — real, disclosed here, non-load-bearing
to any scored prediction or verdict this cycle filed. The P5 sidecar's own
table (`results.json::thermal_rows`) reproduces exactly by independent hand
re-derivation; the `ΔT_ss(r) ∝ r_out` claim holds to <0.2%, correctly
re-phrased. But (a) a "computed" dominance-ratio figure in my own §6 narrative
never actually reproduces from the committed formula chain, and was then
*mis-confirmed* by Red Team's own Phase-2 audit, which claimed an independent
re-check that did not actually recover the right numbers either; and (b) this
cycle's own P3 headline finding is a legitimate, underweighted reason to
raise — not lower — my confidence bar for the `Q_ext`-invariance placeholder
my own sidecar depends on, in a way my original proposal did not anticipate
and did not instruct the future measurement to specifically guard against.

## 1. Independent hand re-derivation of the r=156 thermal row

Re-derived from the raw constants and formulas only (`DX_M=30e-9`,
`SIGMA_EXT_78=240.0073740162445`, `RATIO_ABS_EXT=0.51`,
`P_ABS_78=1.7409069740390205e-12`, `K_AIR=0.026`, `EMISSIVITY=0.9`,
`T_AMBIENT_K=293.15`), not by calling `mixed_length_scale_regime` first:

```
Q_ext          = 240.0073740162445 / (2·78)            = 1.5385088077964393
width_78 (m)   = 240.0073740162445 · 30e-9              = 7.200221220487335e-06
i_incident     = (P_ABS_78/0.51) / (width_78² · 1e4)    = 6.584362139917695e-06 W/cm²
                 (independently reproduces LOGBOOK's own T5 docket-#7 witness
                 figure, "6.58×10⁻⁶ W/cm² central" — a second confirmation
                 the chain is anchored correctly, before extending it)

r=156:
sigma_ext_156  = Q_ext · 2 · 156                         = 480.0147480324891
p_abs_156      = i_incident · (sigma_ext_156·DX_M)²·1e4·0.51
               = 6.9636278961560835e-12 W
l_geometric_m  = 156 · 30e-9                              = 4.68e-06 m
h_eff          = 0.026 / l_geometric_m                    = 5555.555555555557 W/m²K
area_m2        = l_geometric_m²                           = 2.19024e-11 m²
rad_term       = 4·0.9·5.670374419e-8·293.15³             = 5.142614061152997 W/m²K
dp_dt          = area_m2·(rad_term + h_eff)                = 1.2179263559021296e-07 W/K
dt_ss          = p_abs_156 / dp_dt                         = 5.717609987180266e-05 K
margin         = 0.020 / dt_ss                             = 349.79650666699865
```

Every one of these bit-exact matches `results.json::thermal_rows["156"]`
(`sigma_ext`, `p_abs_w`, `h_eff`, `dt_ss_K`, `margin` all reproduce to every
printed digit — confirmed programmatically, not eyeballed). A separate call
to the actual gated `lab.thermo_sidecar.mixed_length_scale_regime` on the
same hand-derived `p_abs_156`/`l_geometric_m` reproduces `dt_ss` bit-for-bit
as well. **The executed r=156 row is correct** — both the formula chain and
its application in `run.py` are doing exactly what `phase1_proposal.md` §6
and `lab/thermo_sidecar.py` specify.

## 2. Does the "ΔT_ss ∝ r_out" claim actually hold up?

My own Phase-1 proposal (§6) predicted `ΔT_ss(r) ∝ r_out` — linear growth —
from the algebraic argument that `p_abs_w ∝ r_out²` (via `σ_ext ∝ r_out`
under `Q_ext`-invariance, area convention `iso_xsec_sq` squares it) while
`dp/dT ≈ area·h_eff = l_geometric²·(k_air/l_geometric) = k_air·l_geometric`
is linear in `r_out`, since gas-conduction overwhelms the radiative term.

The executed table gives margins 699.27× / 349.80× / 175.06× — halving at
each κ-doubling. **Yes, this is the same claim as the original prediction,
correctly re-phrased as its reciprocal**: `margin = NETD_lo/dt_ss`, so
`margin ∝ 1/ΔT_ss`; if `ΔT_ss ∝ r_out` then `margin ∝ 1/r_out`, i.e. margin
halves exactly when `r_out` (and κ) doubles. Checked directly against the
filed numbers:

```
dt_ss(156)/dt_ss(78)  = 1.99908   margin(156)/margin(78)  = 0.50023
dt_ss(312)/dt_ss(156) = 1.99815   margin(312)/margin(156) = 0.50046
```

Both ratios sit within 0.2% of the naive-linear ideal (exactly 2.0/0.5), and
the SMALL, systematic sub-linear deviation is itself explained by the
proposal's own disclosed mechanism: the radiative term is not literally
zero, only small, and its relative weight against gas-conduction shrinks as
`r_out` grows (`h_eff/rad_term` = 2160.6× at r=78 → 1080.3× at r=156 →
540.1× at r=312 — see §3 below for why these particular numbers themselves
needed re-deriving), so `dp/dT` grows fractionally faster than pure-linear
as κ increases, pulling `ΔT_ss` fractionally below pure-linear by a growing
(but still tiny) margin at each step. **The original linear-scaling argument
holds, essentially exactly, and the direction of its own small residual is
exactly where the proposal's own physics says it should be.** No defect here
— this is the part of my own proposal I am most confident survives fresh
scrutiny unchanged.

## 3. A genuine defect: the "1949×/487×" dominance-ratio figure does not reproduce

While re-deriving §2's numbers I re-checked every "computed:" figure in my
own Phase-1 proposal's §6 narrative against the same constants the Appendix
script actually uses — and one does not reproduce.

`phase1_proposal.md` §6 states: *"gas-conduction loss overwhelmingly
dominates radiative loss at every r tested (computed:
`h_eff/[4·ε·σ_SB·T³] ≈ 1949× at r=78`, shrinking to `≈487× at r=312`...)."*

Using the SAME constants the Appendix script declares and that every other
number in §6's own table verifiably uses (`K_AIR=0.026`, `EMISSIVITY=0.9`,
`T_AMBIENT_K=293.15`, `SIGMA_SB=5.670374419e-8`):

```
r=78:  h_eff/rad_term = 11111.111.../5.142614...  = 2160.6×   (not 1949×)
r=312: h_eff/rad_term = 2777.778.../5.142614...   =  540.1×   (not 487×)
```

The proposal's own claimed figures are consistently ~10.85% too small at
both endpoints (`1949/2160.6 = 0.9020`, `487/540.1 = 0.9017` — the same
ratio to three significant figures, which points to a single systematic
input error, most likely a different `k_air` value substituted in this one
hand-evaluated sentence and nowhere else, though the exact source of the
substitution is not recoverable from the document as written). This sentence
is a hand-typed "computed" figure that was never actually run through the
committed Appendix script (the script prints every OTHER §6 number but does
not print this ratio anywhere) — an R4-class defect (RULED OUT registry) by
this program's own standing definition.

**This is worse than an isolated authoring slip, and that is the sharper
finding**: `phase2_redteam_audit.md` (§4, attack 4) explicitly states *"I
independently re-derived the underlying physics
(`lab/thermo_sidecar.py::mixed_length_scale_regime`, §0.2)... **1949× at
r=78, 487× at r=312**, per the proposal's own Appendix output, **independently
re-checked** against the function's own `dp_dt = area_m2·(4εσT³ + h_eff)`
formula."* Red Team's own Phase-2 audit — the layer this program's R4
addendum (Iteration 50) specifically requires to *"independently re-derive
that BOTH operands... before the comparison itself counts as verified"* —
cited the correct formula but did not actually recover the correct numeric
ratio, and reported having verified a figure that does not reproduce.

**Severity, stated plainly**: non-load-bearing to every scored prediction
and verdict this cycle filed. The qualitative claim the sentence exists to
support ("gas-conduction dominates radiative loss by orders of magnitude
across this family") is still true at the corrected numbers (540×–2160×,
still 2–3 orders of magnitude) — nothing in P5's CONFIRMED verdict, the
`dp/dT ≈ k_air·r_out·dx` linear-in-`r_out` argument, or any margin/
classification value depends on the exact ratio. It never propagated into
`NOTES.md`'s own Setup/Result sections, which use only the vaguer, still-true
"~3 orders of magnitude" phrasing — so this does not, on the most natural
reading, meet R20's specific "three-or-more defects surviving into a
document's own Result/Learned sections" trigger (it lived in `phase1_
proposal.md` and `phase2_redteam_audit.md`, both pre-freeze documents, in
descriptive, explicitly-non-binding text). It is, however, a real instance of
this program's oldest, most-repeated failure shape (R4), including a genuine
instance of the R4-addendum failure mode specifically (a reviewer's own
"independently re-checked" language attached to a figure that does not
actually check out) — caught only now, at Phase 5, by the seat that
originated it. **For the permanent record: the correct dominance ratios are
≈2160.6× at r=78 and ≈540.1× at r=312, not 1949×/487×.** Any future citation
of this cycle's own §6 narrative should use the corrected figures.

## 4. Does P3's collapse bear on the sidecar's own `Q_ext`-invariance assumption?

This is the substantive physics question the task poses, and my answer is:
**yes, materially — my own Phase-1 proposal underweighted this, and I now
think the P5 sidecar's illustrative bands deserve less trust than "CONFIRMED"
suggests, even though the SCORED claims (classification stays UNDETECTABLE;
margin trend non-increasing) are safe regardless (§3's own re-derivation
shows the classification-flip risk is a near-null this side of a
multi-order-of-magnitude surprise — Red Team's own finding, independently
re-confirmed here).**

**The naive worry, and why it is not quite right as stated.** `kappa_window`
collapsed ~20.7× then ~185× — accelerating, catastrophically outside both
pre-registered power laws (shape_ratio=19.79 vs. 2.00±0.3/4.00±0.5). If
`σ_ext(r)` behaved anything like that, the `Q_ext`-invariance placeholder
would be worthless and the whole P5 table would need discarding, not
merely re-measuring. But `kappa_window` and `σ_ext` are not measuring the
same kind of quantity, and the difference is not incidental — it is exactly
the kind of measurement-construction distinction this program's own R13/R15
lineage exists to force reviewers to check before assuming one channel's
pathology transfers to another:

- `kappa_window` is a **point/narrow-window near-field intensity sample**,
  at a FIXED-CELL offset behind the object (this cycle's own explicit,
  T8-precedented design choice, §2a: "the window/`DENSE_X` offset from the
  object's own surface stays FIXED in cells across r=78/156/312, NOT scaled
  by κ"). NOTES.md's own Next item 1 already names the direct consequence:
  a fixed absolute offset becomes an ever-SHRINKING fraction of the object's
  own growing radius, pushing the sample deeper into the near-field shadow
  as r grows — a genuine, geometry-forced reason for exactly this shape of
  divergence, independent of any exotic diffraction physics.
- `sections.widths()` (the function any real `σ_ext(r)` measurement would
  call, `lab/sections.py:114`) is a **closed four-face Poynting-box,
  global-energy-conservation quantity** — an integrated statement of the
  optical theorem, gate-proven two independent ways to agree (the direct
  flux-integral route and the incident×scattered cross-term route,
  trust-suite stage 8). Structurally, an integrated conservation quantity
  is far more robust to near-field point-sampling pathology than a
  point-window intensity reading deep in a diffraction pattern.
  Critically, **when this program has actually built a self-similar `r`
  family for a box-ledger measurement, the box itself was scaled
  proportionally with κ, not held at a fixed cell offset** — T8's own
  `beam_geometry(r)` (`experiments/030-scale-bridge/design_geometry.py:
  253-264`) builds `box_a = tuple(round(v·κ) for v in BEAM_BOX_A0)`, the
  self-similar convention, for exactly this instrument family. So the
  specific geometric mechanism NOTES.md's own Next item 1 names as the
  leading explanation for `kappa_window`'s collapse (a fixed-offset window
  sampling an ever-deeper fraction of the near zone) does not, by
  construction, apply to a `σ_ext(r)` measured the way this bench's own
  established convention already measures it.

**A previously-uncited, directly relevant data point I found while checking
this: this program already has one self-similar `r`-family `σ_ext`
measurement in its history, on a self-similarly-SCALED box, and it stayed
close to invariant.** `experiments/030-scale-bridge/results.json::t11`
(exp-030's own T11 beam-scene companion, the SAME `beam_geometry(r)`
formula chain this cycle's own §2a explicitly re-derives from) measured
`sigma_ext_a`/`sigma_ext_b` at r=78 and r=156 for a DIFFERENT article (a
uniform-`σ` disk with `σ_on(r)=TAU_ON/(2r)`, holding optical depth τ=3.9
fixed — not `graded_black_shell`, and not the mandatory `sigma_max=0.5/κ`
shell rescale this cycle's own article uses):

```
r=78:  sigma_ext ≈ 236.01 (avg a/b)   →  Q_ext = 236.01/156 = 1.5129
r=156: sigma_ext ≈ 474.73 (avg a/b)   →  Q_ext = 474.73/312 = 1.5216
```

`Q_ext` drifted by only **+0.58%** under an actual κ=2 measurement on a
self-similarly-scaled box — nowhere near the order-of-magnitude territory
`kappa_window` showed. This is a DIFFERENT article (uniform disk, not the
graded shell), so it is corroborating evidence, not proof, for this cycle's
own `graded_black_shell` `Q_ext`-invariance assumption — but it is real,
already-paid-for, already-committed data that neither my own Phase-1
proposal nor this cycle's five Phase-2 critiques nor Red Team's own audit
cited, and it points the same direction my construction-based argument
above does: a scaled-box extinction measurement on this exact bench family
has, the one time it has actually been checked, stayed close to invariant
under exactly this κ-doubling, even while a fixed-offset near-field window
on the same bench family is now shown capable of catastrophic collapse.

**So: should I be MORE skeptical of `Q_ext`-invariance because of P3? Yes —
but for a more precise reason than "a nearby channel misbehaved."** The
right update is not "distrust the placeholder because kappa_window failed
its power-law test" (that specific failure mode is plausibly an artifact of
`kappa_window`'s own fixed-offset construction, and does not mechanically
transfer to a properly-scaled box). The right update is: **this cycle
demonstrated, on this exact bench family, that a naive "should be roughly
scale-invariant" intuition about a coherent near-field quantity can be
wrong by more than an order of magnitude — which is a general argument for
verifying rather than assuming ANY unmeasured invariance claim on this
instrument family, `Q_ext` included, even where the construction-level
argument (self-similar box vs. fixed-offset window) gives good reason to
expect better behavior.** My own Phase-1 proposal's §6 disclaimer ("the
table above is ILLUSTRATIVE... not yet measured... Phase 4 must replace it
with a REAL `sections.widths()` measurement... before P5's own verdict is
scored") was the right call procedurally, but it was written and defended
(mandatory fix 6, MATERIALS' Phase-2 critique) on REALIZABILITY grounds
(is `σ_ext=240` at r=78 an honest measurement of a buildable object, T9's
own diffraction-inflation caveat) — not on SCALE-INVARIANCE grounds. Those
are two independent reasons the placeholder needs replacing, and my own
proposal only fully argued one of them. This cycle's own P3 finding is the
missing second argument, and I did not anticipate it at Phase 1 because the
coherent point/region-intensity channel's own extreme near-field behavior
had not yet been measured when I wrote it.

**What the future `sections.widths()` measurement (Next item 3) should
specifically watch for, that my own original proposal did not name:**

1. **Confirm, explicitly and in code (not by habit), that the measurement
   box scales proportionally with `r_out`/κ** — reuse `beam_geometry(r)`'s
   own `box_a = round(v·κ)` convention (or an equivalent self-similar
   construction), not a fixed-cell offset. This bench family already has
   both conventions live in its own code (T8's own scaled box for `σ_ext`;
   this cycle's own fixed-offset window for `kappa_window`) — a future
   implementer copying whichever nearby code is closest at hand risks
   silently inheriting `kappa_window`'s own fixed-offset artifact into the
   `σ_ext` measurement, which would erase the exact structural distinction
   this section's own argument for cautious optimism depends on.
2. **Report the measured `Q_ext(156)`/`Q_ext(312)` ratio against BOTH
   anchors**: this cycle's own `σ_ext(78)=240.007` (the actual article), and
   exp-030's own T11 `Q_ext≈1.51–1.52` (a different article, same box
   convention, same bench family) — as an analogous-construction sanity
   check, not a substitute measurement.
3. **Floor-gate the measurement itself** (R13/R15 discipline) rather than
   assuming a box-ledger channel is automatically safe from the kind of
   dynamic-range collapse `kappa_window` just demonstrated is possible on
   this exact bench family — see §5 below, which finds this discipline was
   not even applied to `kappa_window` itself this cycle, despite being
   available and already applied to a sibling channel.

## 5. A second, previously-unflagged gap: `kappa_window` itself was never floor-gated

While tracing §4's argument I checked whether this cycle's own P4 machinery
(`floor_gate`, `FLOOR_FRAC=0.10`, `run.py:238`) — built specifically to
apply R13's house rule (a ratio/decade classification must be floor-gated
against its own measurement-noise floor before it is trusted) — was ever
applied to `kappa_window` itself, the metric P2 (monotonicity) and P3 (the
shape-discriminator, this cycle's own headline, most-surprising finding)
both actually score. It was not: `floor_gate()` is called only on the
`DENSE_X` wide/point channel pools (`run.py:586-587,675`, feeding P4's
ripple search) — never on `win_e312["mean"]`/`win_a312["mean"]` or the
`kappa_window_312` ratio those channels form.

This is a genuine gap in my own Phase-1 proposal's own instrument design,
not merely an open question NOTES.md's own Next item 1 already names
("kappa_window(312)=4.8e-6 is getting close to floating-point/
discretization noise territory... a floor/dynamic-range artifact"). NOTES.md
correctly FLAGS the possibility; what neither my own Phase-1 proposal nor
Phase 3's synthesis did was apply the exact, already-available, already-used
(one paragraph away, on a sibling channel, in the same `run.py`) R13
discipline to the actual headline metric. A resolution/floor check for P3's
own accelerating-collapse finding (NOTES.md's own Next item 1, ranked #1)
should not be a fresh instrument design — it should start by computing
`floor_gate([win_e312 pool], "r=312 BEHIND window")` (and the r=156
equivalent, for a clean two-point trend) against the SAME empty-scene
absolute-intensity floor convention this cycle's own P4 machinery already
established, before any mechanism debate about whether the ~185× collapse
is real near-field physics or numerical floor.

## 6. A caution for future citers: the linear-in-r_out trend, extrapolated, is not always comforting

Not a defect — a sharpening of my own Phase-1 proposal's own disclaimer,
worth stating explicitly for the record. `margin(r) ∝ 1/r_out` (§2) means
this program's now-familiar "always comfortably UNDETECTABLE, orders of
magnitude" thermal conclusion is a property of the BENCH-SCALE `r_out`
range this family has ever tested (µm scale), not a scale-free fact. Taken
at face value and extrapolated (which neither this cycle nor any prior one
claims to license — T8/T13's own unresolved near-field→witness bridge, and
the `Q_ext`-invariance/gas-conduction-regime assumptions themselves, both
break down long before witness scale), the SAME linear formula predicts the
margin would fall below 1× — DETECTABLE — at an `r_out` roughly five to six
orders of magnitude beyond r=312 (312 cells·30nm≈9.4µm; the docket-#7
witness geometry's own `WITNESS_R_M=(0.5,1.0,1.5)` m, `experiments/030-.../
design_geometry.py:230`, sits ~10⁵–10⁶× larger). This is not a new physics
finding — it is exactly why "no witness-scale extrapolation is attempted or
claimed this cycle" (my own Idealizations §5) is a load-bearing disclaimer,
not a formality, and I think it is worth this document naming the actual
number rather than leaving the caution purely qualitative, so a future
cycle tempted to cite "this program has never found a thermal margin in
danger" knows precisely why that would stop being true, and at roughly what
scale, if the assumptions this margin depends on were ever (incorrectly)
carried past the regime where they hold.

## 7. Top-3 ranked candidate directions (THERMODYNAMICS' own discipline)

1. **The real, measured `sections.widths()` `σ_ext(r)` trend (already
   NOTES.md's own Next item 3), now re-ranked to the top of my own queue
   for the reason in §4, not merely the realizability reason my own Phase-1
   proposal originally gave** — build it with an explicitly self-similar
   box (not a fixed offset), cross-check against exp-030's own T11
   `Q_ext≈1.51→1.52` two-point precedent, and floor-gate the result before
   trusting it. Zero marginal FDTD cost, reusing this cycle's own captured
   fields.
2. **Apply R13's floor-gate discipline to `kappa_window` itself** (§5) —
   compute the r=156/r=312 `BEHIND`-window floor margins with the SAME
   machinery this cycle's own P4 channel already uses, before any
   mechanism debate about P3's own accelerating collapse. Cheapest,
   most directly actionable item on this list; a genuine gap in my own
   original instrument design, not a new build.
3. **Correct the record on the "1949×/487×" dominance-ratio figure**
   (§3) and, going forward, extend R4-addendum discipline explicitly to
   THERMODYNAMICS' own sidecar narrative sentences specifically —
   this program's R4 registry already spans nine cycles and multiple
   disciplines; this is this seat's own first confirmed instance of
   authoring one, caught only by the same seat's own later self-review,
   exactly the failure shape R4's own addenda exist to close going
   forward. Low cost, non-load-bearing, but the honest thing to log.

*(NOTES.md's own Next items 2, 4, 5, 6 — the r=312 settling leg, the
oblique-angle extension, the `delta_scene` R3-vs-R4 split, and the other
Reconciled Iteration-82 Tier-1 items — remain open and correctly queued;
not re-ranked here since they sit outside this seat's own charter-specific
findings this cycle.)*
