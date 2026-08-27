# PHASE 2 — RED TEAM AUDIT · Panel Iteration 56 · exp-079
## Adjudicating all five blind Phase-2 critiques of the y-wall full-aperture-sum pre-screen: EM/QUANTUM's convergent structural finding is confirmed and given full weight, a genuine arithmetic slip is settled, a genuine residual sideband is confirmed, and Tier-0 item 1's own question is ruled NOT actually closed by this cycle

**Seat: RED TEAM.** Read, in order: `PANEL.md` in full (seat 7's own charter,
the target phenomenon + four constraints, the five-phase loop); `AGENTS.md`
in full; `LOGBOOK.md` in full (RULED OUT R1–R9 in full; ESTABLISHED; LIVE
THREADS in full, with close attention to the T28 sub-thread, Iterations
46–55, and exp-078 specifically); `experiments/078-.../phase5_redteam_audit.md`
in full (§2, §7 especially — this cycle's own direct ancestor); this cycle's
complete record in order — `phase1_proposal.md`, `y_wall_aperture_sum.py`,
`y_wall_aperture_sum_results.json`, `_output.txt`, then all five blind
Phase-2 critiques (`phase2_critique_{vision,photonics,em,thermodynamics,
quantum}.md`); `experiments/075-.../boundary_reflectance.py`,
`experiments/065-.../design_geometry.py`,
`experiments/048-evidentiary-chord-closure/design_geometry.py`
(`field_and_h`, the established Huygens–Fresnel amplitude-falloff
convention EM's critique cites), and `lab/fdtd2d.py::Sim.add_line_source`.
`experiments/078-.../phase2_redteam_audit.md` read as this document's own
format/tone model (not copied — a fresh audit of a different cycle). I alone
see the Phase-1 proposal AND all five blind critiques this phase, and speak
last.

---

## 0. What I independently verified this cycle, from primitives, before ruling on anything

Nothing below is taken on any critic's word, or the proposal's own word,
alone — every load-bearing number cited by any of the five critiques was
independently recomputed here, from the committed JSON or from scratch.

1. **Re-derived `theta_local(y_s)=atan(D_SP/(OBJ_Y+y_s))` and
   `dist_image(y_s)=hypot(D_SP,OBJ_Y+y_s)` from the image-source geometry
   directly** (not from the script, not from any critique) — confirmed both
   are pure functions of static per-config geometry, zero `theta_beam` term
   anywhere, matching the script's own `theta_local_deg`/`dist_image_cells`
   and EM's/QUANTUM's independently-derived tables exactly.
2. **Ran `QUANTUM`'s reflectance ablation myself, independently**, rebuilding
   `echo_field_curve` with `r(theta_local(y_s))` replaced by a bare constant
   `1.0` (own script, this session's scratchpad, not copied from QUANTUM's
   critique): `C80−C40` P*=`2.0104°`/R²=`0.9745`, solo `C40` P*=`2.0304°`/
   R²=`0.9771`, `ptp(C80−C40)=6.932×10⁻²` — matches QUANTUM's cited
   `2.0085°`/`0.9746`, `2.0310°`/`0.9771`, `6.932×10⁻²` to within
   grid-resolution noise (`<0.002°` on the period, attributable to a
   marginally different `n_grid`, not a substantive discrepancy). **QUANTUM's
   central claim is real and reproduces independently.**
3. **Ran PHOTONICS' residual-decomposition check myself, independently**,
   using the *exact* house `_fixed_period_fit`/`_free_period_search`
   convention (`run69.py`, fitting in `sin(theta)` space against a period
   converted via `T=radians(P)·cos(radians(39))` — my first attempt, fitting
   directly in `theta`-degree cos/sin space, did **not** reproduce PHOTONICS'
   number, and I traced the discrepancy to my own wrong basis before
   crediting the finding, exactly the R4/self-check discipline this program
   requires of a reviewing seat's own claims): subtracting `PAIR_PAD`'s own
   fitted `1.9925°` tone (R²=`0.9720`, matching the committed JSON exactly)
   and free-period-searching the residual over `[1°,15°]` (the committed
   `wide[1,15]` stage, `n_grid=2800`) gives **P*=`2.5506°`, R²=`0.6043`**,
   residual `ss_tot` = `2.80%` of the primary fit's own `ss_tot` — matching
   PHOTONICS' `2.5506°`/`0.6042`/`≈2.8%` to the printed digit. Also
   independently confirmed the residual forced to `PAIR_PAD`'s own real
   target (`4.6113°`) gives R²=`0.057` (PHOTONICS: `0.057`) — a clean
   REFUTE of that specific concern, exactly as cited. **PHOTONICS' finding
   is real and reproduces independently, bit-exact.**
4. **Recomputed the "nine orders of magnitude" claim two ways**, matching
   THERMODYNAMICS' own recomputation exactly: `log10(9.391589×10⁻⁷) −
   log10(5.934×10⁻²⁷) = 20.1994` (the comparison the prose actually cites —
   **twenty orders of magnitude, not nine**); `log10(6.047497×10⁻¹¹) −
   log10(10⁻²⁰) = 9.7816` (a *different* comparison — this cycle's own
   absolute `ss_tot_model` against `SS_TOT_DEGENERATE_FLOOR` — that IS
   approximately nine). `grep -rn "orders of magnitude" *.py *_results.json
   _output.txt` in this directory: zero hits — confirmed hand-typed only in
   `phase1_proposal.md` prose, nowhere in committed code/JSON/output. **This
   is a genuine, independently-reproduced R4-shaped arithmetic slip**, not
   an artifact of THERMODYNAMICS' own reading.
5. **Read `experiments/048-.../design_geometry.py::field_and_h` directly**
   to check EM's claim about a missing amplitude-falloff convention:
   confirmed `G0 = exp(1j*(k*gd["r"] - pi/4)) / sqrt(gd["r"])` is this
   bench's own established many-point Huygens–Fresnel convention for
   exactly this class of coherent aperture sum (the subject of a dedicated
   magnitude-bridge correction, Iteration 19/exp-042) — and confirmed
   `y_wall_aperture_sum.py`'s `echo_field_curve` (Sec 3.4, `y_wall_aperture_
   sum.py` lines 253–282) has no `1/√dist_image(y_s)` term anywhere. **EM's
   finding is a real, correctly-identified missing idealization**, not a
   misreading of the code.
6. **Read `lab/fdtd2d.py::Sim.add_line_source` directly** (lines 132–186)
   and confirmed the raised-cosine taper (`0.5·(1−cos(π·i/edge))`) and
   driven-phase formula (`k·sin(angle_deg)·(yy−0.5·(y_lo+y_hi))`) match
   `aperture_amplitude`/`source_driven_phase`'s own re-derivations exactly,
   corroborating PHOTONICS' own live-`Sim` cross-check (§3(b) of its
   critique) by an independent, static-code-reading route.
7. **Independently re-derived the "effective aperture width" a T21-class
   edge-diffraction model would need to exactly hit T28's own real
   `C80−C40` period**, using T21's own established `P(θ)=λ/(A·cosθ)`
   (`dg048.ripple_period_deg`, at fixed `θ=39°`,`λ=600nm`): solving
   `A_eff = 752 · P_T21/P_target = 752 · 1.9608/2.8421 = 518.8118` — see §2c
   below, a new finding, not raised by any of the five critiques.
8. **Reproduced the run itself.** `python3 y_wall_aperture_sum.py`,
   bit-identical to the committed JSON/`_output.txt` (no diff written) —
   matching all five critiques' own independent reruns.

No critique across the five overreaches; every load-bearing numeric claim
independently reproduces. All five converged on **support-with-changes**; I
concur with that overall shape, but the task requires weighing one finding —
EM's and QUANTUM's convergent structural result — with real force, not as
one bullet among several, and I do so in §2.

---

## 1. Numbered attacks / findings

### Attack 1 — the model's ENTIRE `theta_beam`-dependence is structurally carried by the aperture's own driven-phase ramp, not by the y-wall's reflectance physics; §4/§7's "closer to a genuine (informal) REFUTE" framing claims a discriminating power this construction structurally lacks [inconsistency]

**Independently confirmed at §0.1–0.2 above, from two different methods
(EM's analytic derivation, QUANTUM's empirical ablation), and now a third
(mine, §0.2, reproducing QUANTUM's ablation from scratch).** Both
`theta_local(y_s)` and `dist_image(y_s)` are, by the document's own
derivation (§3.1, independently re-verified), pure functions of *static*
per-config geometry — zero `theta_beam` dependence anywhere. The *only*
`theta_beam`-dependent ingredient in `E_echo` is `phase(y_s;theta_beam)=
k·sinθ_beam·(y_s−OBJ_Y)` — the *identical* driven-phase ramp, over the
*identical* `[y_lo,y_hi]`/`TAPER=40` window, that already produces T21's
own established fringe in the direct (non-reflected) field. This means the
model's recovered period as a function of `theta_beam` is set almost
entirely by the aperture's own geometric extent (the `A=752` Fourier
content of that ramp), not by any property of `r(theta_local(y_s);ABSORB)`
— confirmed directly: replacing `r(theta_local(y_s))` with a bare constant
`1.0` (zero wall-echo physics at all) reproduces the committed model's
period and R² to within grid-resolution noise (§0.2). **This is the single
most consequential finding of this cycle, and it is given full weight,
not waved through — see §2, its own dedicated section, below.**

### Attack 2 — "nine orders of magnitude above exp-078's own floor" is an arithmetic error (§1, §5.2, §7); the correct figure for the cited comparison is ~twenty orders [inconsistency, R4-shaped]

**Independently confirmed at §0.4, matching THERMODYNAMICS' own
recomputation exactly.** `log10(9.391589×10⁻⁷) − log10(5.934×10⁻²⁷) =
20.1994`, not nine. The hand-typed figure appears nowhere in the committed
code/JSON/output (grep-confirmed, an R4 violation on its face). Settled in
full at §3 below. **Non-load-bearing** to the qualitative conclusion the
figure decorates (`ss_tot_degenerate=False` is computed correctly in code
either way, and the *correct* figure — twenty orders, not nine — only makes
the "this is real, resolvable signal" claim MORE true, not less) but must
be corrected, and is the fourth instance of this exact hand-typed-
comparison-figure failure shape on this exact T28 sub-thread (exp-076,
exp-077, exp-078, now exp-079 — a pattern worth naming explicitly, matching
this program's own R4 discipline).

### Attack 3 — "the y-wall geometry contributes only a slowly-varying envelope, not an independent new frequency" (§5.3/§7) is asserted, not tested; a genuine, if small, residual sideband exists [inconsistency]

**Independently confirmed at §0.3, matching PHOTONICS' own recomputation
bit-exact.** Subtracting `PAIR_PAD`'s own dominant `1.9925°` tone and
free-period-searching the residual finds a genuine secondary component at
`2.5506°` (R²=`0.6043`, `ss_tot`≈2.8% of the primary fit's own) —
materially closer to T28's own `C80−C40` real period (`2.8421°`, 10.3%
away) than to T21's (`1.9608°`, 30.1% away) or to the residual forced onto
`PAIR_PAD`'s own real target (R²=`0.057`, a clean REFUTE of *that*
concern). This is real, un-dismissed structure, two orders of magnitude too
small in absolute `ss_tot` (`≈2.6×10⁻⁸`) to threaten the bottom line, but
the flat "only a slowly-varying envelope" sentence is not fully earned by
what §5 actually computed.

### Attack 4 — a missing amplitude-falloff term is an undisclosed idealization, non-load-bearing to the scored periods but load-bearing to the "nine [sic] orders of magnitude" headline statistic [inconsistency]

**Independently confirmed at §0.5.** `echo_field_curve`'s per-point
contribution has no `1/√dist_image(y_s)` factor, unlike this bench's own
established many-point Huygens–Fresnel convention
(`experiments/048-.../design_geometry.py::field_and_h`, `G0=exp(i(kr−π/4))
/√r`, Iteration 19/exp-042's own dedicated magnitude-bridge correction).
EM's own re-run with the falloff added shows the Test-A period verdicts are
essentially unaffected (`<1%` shift on every P*, confirming §5.3's own
mechanistic reading independently) but the `ss_tot` ratio moves ~753×
(`9.392×10⁻⁷→1.248×10⁻⁹`) — still nowhere near the `SS_TOT_DEGENERATE`
floor either way, but a real, undisclosed idealization on the one statistic
this document leans on hardest as decisive evidence. Absent from all 9
items in §6.

### Attack 5 — §4/§7's "a third, sharper outcome not named in either of the ranking's own two branches" framing overstates its own novelty [inconsistency]

The reconciled Iteration-56 ranking's own branch (b) reads: "if it does NOT
generalize... that IS the discovery of genuine θ-dependence... and would
justify the full build for the first time" (`phase5_redteam_audit.md` §7
item 1, quoted correctly in this cycle's own §4). This cycle's result — the
flat result does not survive (branch (a) REFUTEd) and genuine `theta_beam`
dependence is recovered — matches branch (b)'s own premise exactly. What
this cycle adds is an argument for why that dependence does NOT license
branch (b)'s own stated *consequence* ("would justify the full build") —
a refinement within branch (b)'s own framing, using the SAME "two
near-identical frequencies difference to a third at that frequency" logic
T28's founding argument already used to rule out an analogous claim for
the real data. Independently checked against the ranking's own text (§0,
this audit); VISION's reading is correct. A wording-only fix — does not
change any scored number or the recommended next step.

### Attack 6 — the one nominal Test-A SUPPORT (`C80−C40`, `rel_dev=0.2857`) carries ~zero evidentiary weight, for a reason stronger than the disclosed R5 gap names, and QUANTUM's decisive control is not yet in the committed record [inconsistency]

**Independently confirmed at §0.2 and above (verification item 9,
§ "Additional independent check" below).** Forcing `C80−C40`'s fit to
T21's own *exact* period (`1.9608°`, not the free-fit `2.0301°`) gives
R²=`0.9425` (only slightly worse than the free optimum's `0.9732`) and
`rel_dev=0.3101` against the T28 target — just outside the SUPPORT bar. The
SUPPORT/INCONCLUSIVE line for this one comparison rides on a ~2%,
sub-fitting-window difference between three curves that Attack 1's own
finding shows are, structurally, all measuring the same T21-scale aperture
quantity regardless of the wall's true reflectance. This is stronger and
more directly relevant than the disclosed-but-unrun R5 null-permutation gap
(§4 of the proposal): a null-permutation control answers "could noise
produce this," which is not in doubt at these R² (`0.97`+); the ablation
answers the question that actually matters — "does this construction's
recovered period depend on the wall physics at all" — and the answer,
independently reproduced here, is no. **QUANTUM's reflectance-ablation
control is the correct, decisive check for this specific gap and should
supersede, not merely supplement, a generic R5 null-permutation control as
the committed resolution — but it is not yet folded into
`y_wall_aperture_sum.py`/`_results.json`, only into a Phase-2 critique.**

No attack in this cycle is tagged `unfalsifiable`, `inexpressible`, or
`constraint-#N-violation`: this is pure T28 instrument/model-fidelity work
(T1 route N/A, correctly and consistently stated throughout, independently
re-confirmed — no absorber, no switch, no ambient scene, no constraint-3
claim anywhere in this file), matching every T28 cycle since exp-069.

---

## 2. The central finding, given full weight: this instrument cannot, and structurally never could, discriminate a real y-wall echo from no echo at all

This is the task's own most consequential item, and it is adjudicated here
directly, not folded into a numbered attack and left at that.

### 2a. What EM and QUANTUM each independently found, and what I independently re-derived a third way

EM's route is structural/analytic: both `r(theta_local(y_s))` and
`dist_image(y_s)` are, by the document's own §3.1 derivation, pure
functions of static per-config geometry. QUANTUM's route is empirical: an
ablation replacing `r(theta_local(y_s))` with a bare constant `1.0`
reproduces statistically indistinguishable periods and R² values. **These
are not two weak, mutually-reinforcing hints — they are the same fact,
proven twice, by orthogonal methods, and I reproduced QUANTUM's own
ablation from scratch at §0.2 as a third, independent confirmation.** The
mathematical content is a direct consequence of how `E_echo` is built:

```
E_echo(cfg,theta_beam) = INTEGRAL_{y_s} amp(y_s)*r(theta_local(y_s);ABSORB)
                          * exp(i*k*dist_image(y_s))     <- theta_beam-INDEPENDENT weight w(y_s)
                          * exp(i*k*sin(theta_beam)*(y_s-OBJ_Y))   <- the ONLY theta_beam-dependent factor
                          dy_s
```

This is, exactly, the spatial Fourier transform of the complex envelope
`w(y_s) = amp(y_s)·r(theta_local(y_s))·exp(i·k·dist_image(y_s))`, evaluated
at spatial frequency `k·sinθ_beam`. **The spectral content of `E_echo` as a
function of `theta_beam` is therefore governed by `w(y_s)`'s own spatial
structure — and `w(y_s)`'s dominant features (support width
`[y_lo,y_hi]`, `TAPER=40`-cell raised-cosine edges) are IDENTICAL to the
real, direct-field aperture's own, because `amp(y_s)` is the same taper and
the aperture is the same 1,504-cell window.** Whatever `r(theta_local(y_s))`
and `dist_image(y_s)` contribute is a *slowly-varying* modulation on top of
that shared window — exactly why swapping in `r≡1` barely moves the
recovered period at all.

### 2b. A quantitative account of *why* the recovered period is 1.6%–3.5% off T21's exact value, not exactly on it

This was not computed by any of the five critiques; I ran it as a
follow-up to Attack 1, using the same primitives (§0.7). Linearizing
`dist_image(y_s)=hypot(D_SP,OBJ_Y+y_s)` about the aperture midpoint
`y_s=OBJ_Y` gives a **local slope** `d(dist_image)/dy_s|_{y_s=OBJ_Y} ≈
0.9902` (C40) — i.e., `dist_image(y_s)` is *almost exactly linear* in `y_s`
over the aperture, with a slope corresponding to an effective incidence
angle near 82° from the beam axis. A pure linear term in `y_s` inside the
exponential is algebraically identical in form to the driven-phase ramp
itself (just a different, fixed "angle"), so **to first order it does not
change the recovered period at all** — it would only shift a phase/DC
offset. What *does* perturb the period away from T21's exact `1.9608°` is
the *curvature* (quadratic-and-higher terms) of `dist_image(y_s)`: fitting
`dist_image(y_s)` to a quadratic in `(y_s−OBJ_Y)` for C40 gives a quadratic
coefficient contributing `≈0.21` cycles of extra phase across the full
aperture window — a real, modest chirp, fully consistent in size with the
observed 1.6%–3.5% period departures from T21's exact value. **This
confirms, quantitatively and not just qualitatively, that the recovered
period is T21's own aperture-width fringe, lightly perturbed by the
image-distance function's own curvature — not an independent physical
effect tied to the wall's reflectance.**

### 2c. A forward caution this cycle's own record should carry: the "effective aperture" a fix would need is a name already on the RULED OUT list

Independently derived at §0.7, not raised by any of the five critiques.
Using T21's own established `P(θ)=λ/(A·cosθ)`, the effective aperture width
`A_eff` a T21-class edge-diffraction model would need, to exactly reproduce
T28's own real `C80−C40` period (`2.8421°`) at the same `(θ,λ)` reference,
is:

```
A_eff = A_T21 · P_T21/P_target = 752 · 1.9608/2.8421 = 518.8118 cells
```

**This is not a new number.** It is bit-identical (to the fourth
significant figure) to `A_eff≈518.81`, the exact quantity LOGBOOK's own R5
addendum (Iteration 47, exp-070) already found and ruled a **statistically
indistinguishable-from-chance dead end** (`null_p=0.497`, beaten by over
80% of pure-chance targets in a 20,000-trial permutation control) — a named
item explicitly recorded as "not to be re-proposed as a T28 mechanism
candidate without new evidence." The two derivations are independent in
method (Iteration 47 back-solved `A_eff` from a raw named-constant search
against the real data directly; this audit derives it from the T21
period-scaling relation applied to the same real target period) but land on
the identical number because they are, underneath, the same algebraic
identity (`P∝1/A` at fixed `θ,λ`). **This is a genuine, useful forward
caution, not a new finding to chase**: any future attempt to "fix" this
model class by shrinking its effective aperture toward T28's own period
would be re-approaching R5's own already-closed dead end, not new evidence
— worth stating explicitly in the record so Iteration 57 does not
rediscover `A_eff≈519` and mistake it for something new.

### 2d. What this means for how §4/§7 should be read, and what it does NOT mean

**It does not mean the proposal's Test-A numbers are wrong** — they
reproduce exactly (§0.8), the gates are genuinely re-run at a new envelope,
the convergence check is real. **It does not mean §5.3's mechanistic
reading is false** — "the recovered signal is T21's, not T28's" is true and
independently reconfirmed three ways (EM, QUANTUM, this audit). **What it
means is narrower and more important**: this specific construction was
**never capable, by its own structure, of producing any period other than
one dominated by the shared aperture's own T21-scale content** — regardless
of what the y-wall's true reflectance physics is, regardless of whether a
real y-wall echo at T28's own period exists or not. A real echo at T28's
period, had one existed, could not have been recovered by this instrument;
no echo at all produces a statistically indistinguishable result. **§4/§7's
"closer to a genuine (informal) REFUTE... than to an INCONCLUSIVE" framing,
applied to "the y-wall self-near-wall echo mechanism explains T28's real
signal," attributes to the computed DATA a discriminating power this
construction structurally does not have.** This is not a data problem — no
amount of additional FDTD or a finer angle grid would fix it — it is a
property of building `E_echo` as a coherent sum over the REAL,
`theta_beam`-driven aperture with a per-point weight that carries no
`theta_beam` dependence of its own. The correct characterization, matching
EM's own proposed fix (its own §5, "single change that would flip my
verdict"), is: **this pre-screen cannot discriminate a real-but-
T21-frequency-locked-by-construction echo from no echo at all** — a
materially different, and more useful, finding for the permanent record
than "T21, not T28," because it tells Iteration 57 *why* this whole
reduction family cannot answer the question it was built to answer, not
merely that it didn't.

---

## 3. THERMODYNAMICS' "nine orders of magnitude" — settled

**Independently re-derived at §0.4, matching THERMODYNAMICS' own figures
exactly, from raw JSON, not from either party's prose.**

- The comparison the prose actually cites (`9.392×10⁻⁷` vs exp-078's own
  `5.934×10⁻²⁷` ratio) is **20.1994 orders of magnitude**, not nine.
- A *different* comparison — this cycle's own absolute `ss_tot_model_pad`
  (`6.047497×10⁻¹¹`) against `SS_TOT_DEGENERATE_FLOOR` (`1×10⁻²⁰`,
  `y_wall_prescreen.py` line 322) — **is** approximately nine
  (`9.7816`), but this is not the comparison named in the text, and the
  prose's own citation of exp-078's `5.9×10⁻²⁷` figure as a "floor" is
  additionally imprecise: exp-078's §2c itself labels that number a
  *ratio* ("Ratio (model/real): 5.934e-27"), not a floor;
  `SS_TOT_DEGENERATE_FLOOR` is the actual, differently-valued floor in this
  program's code.
- **Ruling: non-load-bearing to the qualitative conclusion.** The scored
  `ss_tot_degenerate` boolean is computed correctly in code (`False`,
  independently re-verified both ways: `6.047×10⁻¹¹≥10⁻²⁰` directly, and
  the ratio comparison the prose intended is even more decisively
  non-degenerate at the corrected 20.2-order figure than the erroneous
  nine-order one claimed). **Mandatory, not optional**: fix the figure in
  all three places it appears (§1, §5.2, §7) to the correct twenty-order
  comparison, or explicitly retarget the citation to the ~9.78-order
  absolute-vs-floor comparison if that was the intended claim — do not
  leave the ambiguity between "which two numbers are being compared"
  unresolved. This is the fourth instance of an R4-shaped hand-typed
  comparison-figure error on this exact T28 sub-thread (exp-076, exp-077,
  exp-078, now exp-079) — worth naming as a pattern, not merely fixing in
  place, though it does not on its own rise to a fresh Checkpoint firing
  (§7 below).

---

## 4. PHOTONICS' residual sideband at 2.55° — settled

**Independently reproduced bit-exact at §0.3**, using the house
`_fixed_period_fit`/`_free_period_search` convention (the `sin(theta)`-space
fit with `T=radians(P)·cos(radians(39))`, not a naive `theta`-degree cos/sin
basis — my own first attempt used the wrong basis and did not reproduce the
finding, corrected before crediting it, per this program's own
self-verification discipline). `PAIR_PAD`'s residual, after removing its
own dominant `1.9925°` tone, carries a genuine secondary component at
`2.5506°` (R²=`0.6043`), `≈2.8%` of the primary fit's own `ss_tot`
(`≈2.6×10⁻⁸` in absolute terms) — closer to T28's own `C80−C40` real period
(10.3% away) than to T21's fringe (30.1% away) or to the residual forced
onto `PAIR_PAD`'s own real target (R²=`0.057`, cleanly ruling that
specific concern out). **Does this change anything material, in light of
Attack 1/§2's structural finding?** No — and this is worth stating
explicitly, since the task raises the question directly. A residual
sideband inside a construction whose ENTIRE `theta_beam`-dependence is
structurally locked to the shared aperture window (§2) is itself just
another feature of that same shared window's Fourier content (the raised-
cosine taper edges have their own weaker secondary lobes, a standard
diffraction-grating side-lobe structure, not a new physical channel) — it
cannot be independent evidence about the wall's own reflectance any more
than the dominant tone can. **Ruling: real, correctly caught by PHOTONICS,
must be disclosed (the flat "only a slowly-varying envelope" sentence is
not earned), but does not require a deeper investigation or change the
verdict** — it is a second-order confirmation of Attack 1's own point, not
a competing finding.

---

## 5. Disposition of the five critiques' findings

| Critique | Finding | Disposition |
|---|---|---|
| **ELECTROMAGNETISM** | The model's entire `theta_beam`-dependence is structurally carried by the shared driven-phase ramp, not by wall physics — analytically derived; a missing `1/√dist_image` falloff moves the "nine [sic] orders of magnitude" statistic ~753× but not the Test-A period verdicts | **ADOPT AS MANDATORY, given the fullest weight of any finding this cycle** (Attack 1/§2 — independently re-derived from primitives by this audit, extended with a quantitative curvature account (§2b) and a forward R5-registry cross-reference (§2c) neither EM nor any other critique computed). Falloff finding **ADOPT** (Attack 4). |
| **QUANTUM OPTICS** | An empirical `r(theta_local)≡1` ablation reproduces statistically indistinguishable periods/R² — the model cannot discriminate a real echo from none; the one marginal SUPPORT is set by a ~2% sub-fitting-window artifact, not an independent frequency | **ADOPT AS MANDATORY** (Attack 1/§2, Attack 6 — independently re-run from scratch here, §0.2, reproducing to within grid-resolution noise; the T21-forced-fit sub-check on `C80−C40`, §0's item 9, independently reproduced exactly: R²=0.9425, rel_dev=0.3101). QUANTUM's own judgment that a null-permutation control is "the wrong tool" here and the ablation is the correct, more decisive one is independently endorsed (§1 Attack 6). |
| **PHOTONICS** | The "only a slowly-varying envelope" claim is untested; a genuine residual sideband at `2.55°`/R²=`0.60` exists in `PAIR_PAD`'s residual, small and off-target | **ADOPT** (Attack 3/§4 — independently reproduced bit-exact, after correcting my own first-pass wrong-basis error). Ruled non-load-bearing and mechanistically subsumed by Attack 1/§2 (a side-lobe of the same shared-aperture Fourier content, not a competing physical channel) — a real disclosure gap, not a verdict-changing one. |
| **THERMODYNAMICS** | "Nine orders of magnitude" is an arithmetic error — the cited comparison is ~twenty orders; a different, uncited comparison is the one that IS approximately nine; the THERMO N/A-disposition sentence is missing a second consecutive cycle | **ADOPT AS MANDATORY** (Attack 2/§3 — independently re-derived both figures from raw JSON, matching exactly; grep-confirmed hand-typed, zero hits in code). THERMO-sentence gap **ADOPT** (mandatory-fix docket item 7, below). |
| **VISION SCIENCE** | R9-clean (no commensurability defect); "third, sharper outcome" framing overstates novelty relative to the ranking's own branch (b); the one nominal SUPPORT should not survive into Phase 3 as informative without further work | **ADOPT** (Attack 5, R1–R9 registry §6 below). The "further work" VISION named as needed (a null-permutation control) is **superseded, not merely supplemented**, by QUANTUM's own ablation (Attack 6) — a stronger, more directly relevant test that already exists and answers VISION's own underlying concern more decisively than the control VISION requested would have. |

**Nothing is overridden.** Every load-bearing claim across all five
critiques independently reproduces, several to the printed digit, after
this audit corrected its own tooling on one recomputation (§0.3) before
crediting PHOTONICS' finding — exactly the R4/self-check discipline this
document holds every other seat to.

---

## 6. R1–R9 registry check, against this cycle

- **R1–R3**: N/A — no constraint-1 claim, no shell-thickness claim, no
  resolution-convergence question (zero-FDTD desk model; the numerical-
  integration convergence check, §5.1, is a distinct, non-R3 concept —
  correctly not conflated with a grid-resolution/staircase check anywhere
  in this cycle's own text).
- **R4**: **two confirmed instances this cycle** — the "nine orders of
  magnitude" figure (Attack 2/§3, mandatory fix) and the §5.2 "third
  outcome" framing is a *characterization* issue, not an R4 figure, and is
  handled separately (Attack 5). No other hand-typed or unreproducible
  number found anywhere in `phase1_proposal.md` — independently re-run
  (§0.8) and cross-checked digit-for-digit against the committed JSON
  throughout this audit.
- **R5**: **correctly, and more rigorously than R5's own letter requires,
  discharged by QUANTUM's ablation** (Attack 6). R5's rule targets a dense
  search over many named candidates finding a plausible match to noise —
  this proposal makes one primary model with two proxy choices (`Re`,
  `|·|`), not a search, and the recovered periods are not noise-fit
  (R²=0.97+, far above chance). A generic null-permutation control would
  have answered "could noise produce this" (no, obviously) rather than the
  question that actually mattered ("does this depend on the wall physics at
  all," also no) — QUANTUM's own judgment on this, independently endorsed
  here, is the correct resolution of the proposal's own §4 R5 disclosure,
  not a gap requiring a fresh literal R5 control. **Mandatory: fold the
  ablation into the committed record** (mandatory-fix docket, below) so
  this resolution is not left as a Phase-2-only artifact.
- **R6, R7**: N/A — no fitted carrier/phase coefficient, no un-fit
  conditioning-only closure claim anywhere in this file.
- **R8**: **the live rule this cycle, correctly discharged, not
  triggered.** Unlike R8's original firing trigger (exp-075, Iteration 52),
  no seat here adopted an unverified argument and let it stand — EM's own
  Phase-2 critique *computed* the structural claim (the falloff-corrected
  re-run, §1 Attack 4) rather than merely asserting it, QUANTUM *ran* the
  ablation rather than arguing it should be run, and this audit
  independently reproduced both from scratch (§0.1–0.2) before adopting
  either. This is R8's discipline working as intended, at Phase 2, before
  anything freezes — matching this program's own established non-firing
  shape.
- **R9**: **checked independently, clean** (matching VISION's own audit,
  independently re-derived, not merely accepted). `rel_dev` (period vs.
  period, same units, same `_free_period_search` code path throughout) and
  the `ss_tot` ratio (`sum((y−mean(y))²)` on a proxy curve in that curve's
  own native units, on both sides of every ratio) are commensurate
  throughout. No T16/`amp_ratio`-shaped unit mismatch anywhere in this
  file's scoring.

---

## 7. Checkpoint status

**No PANEL.md criterion fires on this cycle.**

Criterion 1 (constraint metric pass) and criterion 3 (engine physics beyond
validated bench classes) do not apply — zero new FDTD, zero `lab/` diff,
T1/constraint-3 correctly and consistently disengaged throughout (re-
confirmed independently, §1). Criterion 5 (two non-advancing iterations) is
not at risk — this cycle genuinely narrows the T28 board, whichever way its
own framing is corrected (§8, below).

**Criterion 4 (program-integrity drift) is the one worth reasoning through
explicitly, and it does not fire, for the same reason this exact T28
sub-thread's own non-firing precedents (Iterations 51, 53, and exp-078's
own Phase-2 audit) do not fire**: every substantive gap this document
closes — the structural over-claim (Attack 1/§2, the most severe finding
this cycle produced), the arithmetic slip (Attack 2/§3), the untested
"envelope only" claim (Attack 3/§4), the missing falloff idealization
(Attack 4), the framing overstatement (Attack 5), and the under-weighted
marginal SUPPORT (Attack 6) — was caught **at Phase 2, by blind critics
converging independently from different disciplinary angles, before Phase 3
freezes any language into `phase3_synthesis.md` or LOGBOOK.** This is the
review layer working exactly as designed, not drift. Nothing here matches
this program's own established firing shape (an unverified argument
adopted and defended past a freeze point, or a false claim actively
maintained across phases) — every claim in this cycle's own Phase-1
document, while incomplete in its own characterization (§2d), is not
*false*: `ss_tot_degenerate=False` is correct, the Test-A `rel_dev`/verdict
numbers are correct, the gates and convergence check are genuine. **Should
the mandatory-fix docket below fail to land in Phase 3 — i.e., if
`phase3_synthesis.md` or a future LOGBOOK entry repeats the "closer to a
genuine REFUTE" framing, or the uncorrected "nine orders of magnitude"
figure, after this audit exists — that would be a fresh, squarely-on-point
Criterion-4 firing**, matching this program's own repeated pattern (a
named, affordable, already-run check ignored at the freeze point).

**Criterion 2 (a proven mechanism-class boundary)**, applied here
informally to the T28 coherent-echo mechanism sub-board (matching
exp-077's/exp-078's own established use of this language for a within-thread,
non-constraint boundary question, not the top-level phenomenon program):
**ruled NOT YET RIPE, but the board has shifted meaningfully this cycle,
and the *next* obvious-looking move is flagged as unlikely to escape this
cycle's own structural finding** — see §8.

---

## 8. Does Tier-0 item 1's own question get answered by this cycle? Ruled: not as posed — and that is itself the reportable finding

The reconciled Iteration-56 ranking's own item 1 asked: does the
flat/zero-signal result generalize from the single-edge reduction to the
FULL, non-edge-reduced y-mirrored aperture sum? **Literally, in the narrow
sense of "does the strict `ss_tot`-near-float-noise flatness survive": no,
correctly answered, independently reconfirmed (§0.8, Attack 1).** But the
ranking's own framing (§0 of this cycle's proposal, quoted correctly)
treated that narrow question as a proxy for a *deeper* one — whether the
y-wall self-echo-off-the-near-wall mechanism sub-class is close to
exhausted (if flat survives) or newly worth pursuing (if it does not).
**Given §2's own finding, that deeper question is not actually closed by
this cycle either way** — not because the computation is wrong, but because
**this specific construction (a coherent sum over the real, `theta_beam`-
driven aperture, weighted by a per-point angle/reflectance term that is
itself `theta_beam`-independent) is mathematically incapable, BY
CONSTRUCTION, of producing a genuinely new, T28-matching frequency, no
matter what the wall's true reflectance physics is.** A real y-wall echo
at T28's own period, had it existed, would have been just as invisible to
this instrument as no echo at all. **This means Iteration 56's own
question — "does the flat result generalize?" — has been answered for the
letter of the single-edge reduction, but the SPIRIT of the question (is
there a real y-wall coherent-echo signature this six-cycle sub-thread has
not yet found) remains genuinely open, because the instrument that would
need to answer it does not yet exist.** A different, better instrument is
needed — not a refinement of this one.

**Concretely, for Iteration 57's own ranking**: the deferred "far-wall/
far-edge image pair" (item 8 of the exp-078 ranking, explicitly deferred
again here, §0/Idealization 3) is very likely NOT the productive next step
— it would add a second `theta_beam`-independent per-point weight term
summed against the SAME shared driven-phase ramp, inheriting Attack 1's own
structural limitation unchanged (a second static envelope layered on the
same aperture-locked carrier does not introduce a new carrier frequency).
**The productive next move, if this mechanism sub-class is to be tested at
all, is a construction that breaks the "static per-point angle" pattern —
a plane-wave/global-steering incidence-angle picture for the y-wall,
mirroring what already, successfully, makes the x-wall's own two-plane-wave
reduction (`phase1_proposal.md` [exp-078] §3.1) a `theta_beam`-dependent
test of the wall's reflectance in the first place**, rather than another
refinement within the current point-source/per-point-image family. This is
a recommendation for the reconciled ranking, not a mandatory-fix item to
this cycle's own files.

---

## 9. Overall verdict: **PROCEED-WITH-MANDATORY-FIXES**

The instrument's general strategy — generalizing exp-078's single-edge
reduction to a full, per-point-angle coherent aperture sum — is the correct
next test the reconciled ranking called for, executed with real care: the
image-source geometry is re-derived correctly and independently
reproducible (§0.1), the vectorized `r(theta)` is validated bit-exact
before use, the gates are honestly re-run at a genuinely new envelope, the
numerical-convergence check is real (`<0.002%` at 2x→4x), and both scalar
proxies are reported symmetrically. This is not a HALT-grade cycle: no
mechanism is claimed unfalsifiably, no engine change is proposed, T1/
constraint-3 stay correctly disengaged throughout, and no attack in this
cycle rises to `inexpressible` or a constraint violation. But **the
document's own self-scored interpretation (§4/§7) claims a discriminating
power about the y-wall's physical reflectance that this construction
structurally does not have** (§2, given full weight, not softened to
protect the cycle's own headline, and not manufactured where the underlying
computation is genuinely sound) — **and carries one genuine, independently
confirmed arithmetic error, one under-tested claim, and one missing
idealization disclosure alongside it.** None of these fixes touch the
committed numbers (`rel_dev`, `R²`, `ss_tot` ratios, the convergence check,
the gates) — they are entirely about what those numbers are allowed to be
read as saying.

### Mandatory-fix docket (Director executes in Phase 3 synthesis)

1. **Add a new Idealization stating Attack 1/§2's structural finding
   explicitly**: `theta_local(y_s)`/`dist_image(y_s)` being pure functions
   of static per-config geometry means `E_echo`'s entire `theta_beam`-
   dependence is carried by the shared driven-phase ramp — the identical
   mechanism producing T21's own fringe in the direct field — independent
   of any property of `r(theta_local(y_s))`. State plainly, in the same
   place: this construction cannot discriminate a real y-wall echo (at any
   period) from no echo at all. [Attack 1, EM/QUANTUM, §2]
2. **Reframe §4/§7's headline.** Replace "closer to a genuine (informal)
   REFUTE... than to an INCONCLUSIVE" with a statement that this pre-screen
   — like exp-078's single-edge model before it — cannot in principle
   distinguish a real T28-matching y-wall echo from no echo, so its own
   result is not informative about whether a real y-wall echo mechanism
   explains T28's signal, in either direction. Replace "a third, sharper
   outcome not named in either of the ranking's own two branches" with
   language stating this is branch (b), refined (VISION's correction).
   [Attacks 1, 5, §2, §8]
3. **Fold QUANTUM's `r(theta_local)≡1` reflectance-ablation control into
   `y_wall_aperture_sum.py`/`_results.json`** as a committed, reusable
   check, not a Phase-2-critique-only artifact — the decisive,
   mechanism-appropriate resolution of the proposal's own disclosed R5 gap
   (§1 Attack 6, §6 R5). Explicitly state the `C80−C40` nominal SUPPORT is
   non-informative once this control is in the record (the T21-forced-fit
   sub-check, R²=0.9425/rel_dev=0.3101, §0 item 9, should ship alongside
   it).
4. **Fix "nine orders of magnitude" in §1, §5.2, and §7** to the correct
   `≈20.2` orders for the comparison actually cited, or explicitly retarget
   the citation to the `≈9.78`-order absolute-`ss_tot`-vs-floor comparison
   if that was the intended claim — state which, do not leave it ambiguous.
   [Attack 2, §3]
5. **Add the missing `1/√dist_image` amplitude-falloff idealization**,
   disclosing EM's finding (this bench's own established `field_and_h`
   convention, exp-048/exp-042) and its quantified, non-load-bearing
   `≈753×` effect on the `ss_tot` ratio (Test-A period verdicts shift
   `<1%`). [Attack 4, §1]
6. **Add the PHOTONICS residual-sideband finding** (§5.3 companion note):
   a genuine secondary component at `2.55°` (R²=`0.60`, `≈2.8%` of primary
   `ss_tot`) exists in `PAIR_PAD`'s residual — real, disclosed, and
   mechanistically subsumed by Attack 1/§2 (a side-lobe of the same shared
   aperture, not independent evidence), not requiring further chase.
   [Attack 3, §4]
7. **Add the missing THERMO N/A-disposition sentence** — a second
   consecutive T28 cycle with this identical one-line omission after being
   named once already (exp-078's own THERMODYNAMICS critique); close it
   this time.
8. **Add, as a forward caution in the record (this audit's own new
   finding, §2c)**: the effective aperture width `A_eff≈518.81` a
   T21-class edge model would need to exactly hit T28's real `C80−C40`
   period is bit-identical to LOGBOOK's own R5-addendum-ruled-out dead end
   (Iteration 47, exp-070) — any future attempt to shrink this model
   class's effective aperture toward T28's own period would be
   re-approaching that already-closed dead end, not new evidence.
9. **Recommendation for Iteration-57's own ranking (not a fix to this
   cycle's committed files)**: the deferred far-wall/far-edge pair (item 8
   of exp-078's own ranking) is very likely NOT the productive next step —
   it inherits Attack 1's own structural limitation unchanged. If the
   y-wall coherent-echo mechanism sub-class is worth testing further, a
   plane-wave/global-steering incidence-angle construction (the y-wall's
   own analogue of what already makes the x-wall model `theta_beam`-
   sensitive to the wall's reflectance) is the genuinely different
   instrument this six-cycle sub-thread has not yet built — not a
   refinement within the current per-point-image family. [§8]

None of these nine items touch `y_wall_aperture_sum.py`'s own frozen
Test-A numbers, `lab/`, or the reused, already-gated
`boundary_reflectance.py`/`design_geometry.py` machinery — all are
record-completeness and interpretive-framing fixes, matching this
program's own established "catch and close same-shift" pattern.
