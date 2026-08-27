# PHASE 5 — REVIEW · QUANTUM OPTICS (blind) · Panel Iteration 56 · exp-079

*Fresh sub-agent, QUANTUM OPTICS charter (PANEL.md seat 5): non-classical
absorption, state-dependent or coherent interactions; expressibility
contract — mechanisms enter the bench only as effective classical
parameters (σ(I), σ(x,t), dispersive ε(ω), gain) or Red Team strikes them.
Fresh context: I have no memory of writing this same cycle's own Phase-2
critique (the reflectance-ablation control this document now leans on was,
per the record, first run by "QUANTUM OPTICS" at Phase 2) — I re-read it
here only as a historical artifact to independently re-verify, not as
unexamined authority carried over from a prior self. I do not see any other
seat's Phase-5 review this cycle.*

---

## 1. Verdict: **PARTIAL** (independently reached, concurring with the record)

This cycle answers the letter of the reconciled Iteration-56 ranking's own
Tier-0 item 1 ("does the flat result generalize?") cleanly — no — and then
does the harder, more useful thing: it shows *why* the full aperture sum,
despite being genuinely non-flat, still cannot answer the question the
ranking actually cared about (is there a real y-wall echo at T28's own
period). That second finding, not the first, is this cycle's real
contribution, and I find it sound on independent re-derivation (§2 below).
Nothing here resolves T28's own six-cycle-old mechanism question; nothing
here closes the y-wall coherent-echo-off-the-near-wall mechanism sub-class
either (Checkpoint criterion 2 correctly not fired). I have no basis to
overturn the Combined Verdict.

My own charter's operative territory this cycle is narrow but load-bearing:
the task asks me to independently scrutinize the one piece of machinery my
own prior-context self is credited with introducing (the reflectance-
ablation control) and the R5/R8 rulings built on top of it. I did that from
primitives, not from the record's own word, and found **one genuine,
previously unstated qualification to the "structurally incapable of
discriminating ANY echo" claim (§3), and one genuine, partially-open
residual precision gap underneath the "now closed" R5 ruling (§4)** —
neither changes the verdict, both belong in the permanent record.

---

## 2. Independent verification performed, from primitives

1. **Re-ran `y_wall_aperture_sum.py` end to end, myself, from this
   directory.** Output is bit-identical to the committed
   `y_wall_aperture_sum_results.json`/`_output.txt` (no diff written to
   disk) — every printed number reproduces, including the full §[7]/§[7b]
   ablation-control block. R4-clean.
2. **Re-derived `theta_local(y_lo)` for C40 from raw geometry, independent
   of any imported module**: `atan(223/(792+40))` in degrees = `15.00426°`
   — matches the committed table and exp-078 Phase-5's own cited figure to
   the printed digit.
3. **Re-derived T21's own reference fringe period from the closed-form
   formula directly**, not via `dg048.ripple_period_deg`:
   `degrees(20/(752·cos(radians(39))))` = `1.960795°` — matches
   `t21_fringe_period_A752_600nm_39deg` in the committed JSON exactly.
4. **Independently loaded `experiments/065-.../design_geometry.py::CONFIGS`
   myself** (not via `y_wall_aperture_sum.py`'s own import, a fresh load)
   and printed every field for all five congruent-series configs — see §5
   below, this is the primitive check the task specifically asks for on the
   `PAIR_ABSORB40` exact-zero claim.
5. Confirmed the committed `reflectance_ablation_control`/
   `t21_forced_fit_c80_c40` JSON blocks match every number `phase1_
   proposal.md` §5.3/§7 cites: `|ΔP*|=0.0150°`(PAIR_PAD)/`0.0226°`(C80−C40),
   `PAIR_ABSORB40` `ptp=0.000e+00`, forced-fit `R²=0.9425`/`rel_dev=0.3101`.

No discrepancy anywhere. Everything this cycle's own record claims about
its own numbers is true. The question worth spending my seat's own time on
is not "did the arithmetic reproduce" (it did, checked independently,
above) but "does the ablation control actually establish what four
successive parties (QUANTUM's own Phase-2 self, EM, Red Team's Phase-2
audit, and Phase 3) say it establishes" — §3.

---

## 3. Does the ablation control have a blind spot? Yes — a real, previously
unstated one, though not one that reopens this cycle's own headline

### 3.1 What the control actually proves, restated precisely

`echo_field_curve`'s integrand is
`amp(y_s)·r(theta_local(y_s);ABSORB)·exp(i·[phase(y_s;theta_beam) +
k·dist_image(y_s)])`. Since `theta_local(y_s)` and `dist_image(y_s)` carry
no `theta_beam` dependence, `E_echo(theta_beam)` is *exactly* the spatial
Fourier transform of `w(y_s)=amp(y_s)·r(theta_local(y_s))·exp(i·k·
dist_image(y_s))`, evaluated at spatial frequency `k·sinθ_beam` — an
algebraic identity, true for *any* function `r(θ)`, not a claim requiring
verification. **This part of Attack 1/§2 is unconditionally correct and I
re-derive it independently the same way EM did.**

What is *not* an algebraic identity, and what the ablation control alone
cannot distinguish from the general FT statement, is the further claim
(Idealization 9, as adopted): that this construction is "structurally
incapable of discriminating a real y-wall echo, **at ANY period**, from no
echo at all." That stronger claim is true only if `w(y_s)`'s own spatial
structure is dominated by the shared `[y_lo,y_hi]`/`TAPER=40` window
regardless of what `r(theta_local(y_s))` looks like — i.e., only if
`r(theta_local(y_s))`, as a function of `y_s`, stays *slowly varying
relative to the window* for any physically plausible wall reflectance, not
merely for the one transfer-matrix model actually tested.

### 3.2 The gap: the "any echo" claim is proven for one smooth family, not for all r(θ)

`theta_local(y_s)` maps the aperture monotonically onto a narrow
`[4.77°,15.50°]` angular range (§0b of the committed output). Whatever
angular structure `r(θ)` has *within that narrow range* becomes, via this
monotonic (but nonlinear) map, spatial structure in `w(y_s)` over `y_s`. If
`r(θ)` were smooth across `4.77°–15.50°` (which is what PHOTONICS'
Phase-2 densely-swept check, §3(c) of its own critique, found for the
*actual* `boundary_reflectance.py` matched-admittance graded-loss model —
strictly monotonic for `ABSORB∈{60,70,80}`, one broad shallow minimum for
`ABSORB=40`), then `w(y_s)` inherits no new fine spatial structure beyond
the taper, and the FT is indeed dominated by the window — exactly what this
cycle measures. But if a *different, still-physically-permitted* `r(θ)`
had sharp angular structure inside this same narrow range (a resonance, a
guided-mode coupling feature, or simply a *realizable* (`μ_r=1`) admittance
whose transfer function is not guaranteed to inherit the matched-admittance
model's smoothness at this specific, never-before-sampled-this-widely
`[4.77°,15.50°]` envelope), the resulting `w(y_s)` would carry a
spatially-localized feature at whatever `y_s` corresponds to the resonant
angle — and a localized feature superimposed on a wide window is exactly
the textbook recipe for a second, genuinely different spatial frequency
(a beat between the edge-diffraction carrier and the defect's own Fourier
content), which this construction's per-point-static-angle-with-static-r
machinery is fully capable of representing algebraically. **The ablation
test (`r≡1` vs. the one smooth `r(theta_local(y_s);ABSORB)` actually used)
cannot distinguish "no echo mechanism could ever produce a new period here"
from "the one specific smooth `r(θ)` family tested happens not to."**

This is not a hypothetical concern invented to score a point: MATERIALS'
own idealization 1 (carried into this cycle, not re-tested) already flags
that `r(theta_local(y_s))` here is the matched-`eps=mu` (unrealizable-
admittance) TE formula, and exp-078's own Phase-5 finding (F2, that the
realizable `μ_r=1` substitution is period-invariant, `Pearson r>0.9997`) was
measured **only** at the single-edge model's narrower `13.7°–15.1°`
envelope — never at this cycle's own much wider `4.77°–15.50°` full-aperture
range, where a realizable admittance's departure from the matched-admittance
idealization has more angular room to develop structure. Nobody this cycle
re-ran that Pearson-r check at the actual envelope this file uses.

### 3.3 What this does, and does not, change

**It does not touch this cycle's own scored result.** `boundary_
reflectance.py`'s actual reflectance, the only one tested, is confirmed
smooth across the relevant range (PHOTONICS, independently re-confirmed by
my own reading of that critique's own dense sweep, not re-run by me — a
zero-cost check already performed this cycle, no need to duplicate it).
Given that smoothness, the FT argument is airtight for this specific model,
and the T21-not-T28 conclusion stands. **It does change how Idealization 9
and §7's headline should be read**: "this construction cannot discriminate
a real y-wall echo at any period from no echo" is true *for any
smoothly-varying r(θ) over the sampled envelope* — a weaker, more accurate
statement than the unqualified "at ANY period" the adopted language now
carries. The distinction matters going forward specifically because the
standing realizable-admittance refit (exp-078's own §7 item 3, re-ranked
to the x-wall this cycle but never formally retired for the y-wall) has
never been checked for smoothness at *this* cycle's own wider envelope —
if it turns out not to be smooth there, the "structurally incapable"
finding would need re-testing, not merely re-citing.

**Recommended same-shift addition** (Iteration 57, not a fix to this
cycle's own frozen numbers): add one sentence to Idealization 9 scoping the
claim to "for r(θ) smooth over the sampled envelope, confirmed here only for
`boundary_reflectance.py`'s matched-admittance model" — and re-run the
existing dense-sweep smoothness check (PHOTONICS' own §3(c) idiom) against
the realizable-admittance substitution at the full `4.77°–15.50°` range
specifically, not merely re-cite exp-078's narrower-envelope Pearson-r
number.

---

## 4. Is the R5 gap now genuinely closed? Mostly — one residual precision
question remains unquantified

The proposal's own §4 R5 disclosure ("no null-permutation control on the
single T21-proximity comparison") is, on the substance that actually
matters, correctly superseded by the ablation control — I independently
confirm QUANTUM's own Phase-2 judgment (a permutation control answers
"could noise reach `R²≥0.97` by chance," obviously no; the ablation answers
"does the recovered period depend on the wall physics at all," also no, and
is the *decisive* test for that specific question). Red Team's R5-registry
ruling (§6 of `phase2_redteam_audit.md`) is correct as far as it goes.

**But "does the period depend on `r(θ)`" is a different question from "is
the quoted 1.6%–3.5% closeness to T21 itself a tight, well-resolved
number, or is it slop within the window's own achievable period
resolution."** The real 31-point window spans only `36°–42°` (6°) — about
3 cycles at a ~2° period, a regime this *exact* T28 sub-thread already
established is poorly conditioned for period discrimination (Iteration 51,
exp-074's own Cramér–Rao/`desk_check_pricing.py` pricing work, on a
comparably narrow window). The committed T21-forced-fit sub-check (§[7b])
is suggestive evidence in this direction, already in the record: forcing
`C80−C40`'s fit to T21's *exact* period costs only `R²: 0.9732→0.9425` — a
modest drop, not a sharp one — meaning the data does not tightly reject
periods somewhat off T21's exact value either. Nobody this cycle converted
that single forced-fit comparison into an actual confidence interval (or
re-used exp-074's own already-built Cramér–Rao pricing machinery) on
`P*_model` itself. **Quoting `rel_dev` to three significant figures
(`0.0162`, `1.6%`) against a period whose own resolving uncertainty in this
window was never bounded is a smaller, more specific version of the
imprecision the T21-forced-fit check already gestures at but does not
close.** This does not threaten the qualitative finding — the FT argument
(§3.1) establishes the mechanism analytically, independent of curve-fitting
precision — but it is a genuine, disclosed-nowhere gap under a claim this
document's own §5.3 states with unqualified numeric precision.

**Ruling, my own seat's judgment**: non-load-bearing to this cycle's
verdict (the structural argument does not need the numeric proximity to be
tight to be true), but worth a same-shift disclosure sentence, and a cheap
same-cost item for whichever future cycle reuses `_free_period_search`'s
staged-widening machinery on a similarly narrow window: report a period
confidence band (bootstrap over the θ-grid, or `desk_check_pricing.py`'s
own Cramér–Rao route) alongside any single-point `rel_dev` quoted to more
precision than the window can support.

---

## 5. `PAIR_ABSORB40`'s exactly-zero ablated delta — independently
re-derived from primitives: yes, a genuine mathematical certainty, not a
coincidence the current check happens not to have caught otherwise

Loaded `experiments/065-.../design_geometry.py::CONFIGS` myself, fresh,
independent of `y_wall_aperture_sum.py`'s own import:

```
G40: absorb=40 pad=40 obj_y=832 y_lo=80 y_hi=1584 A=752 d_sp=223 aperture_cells=1504
C80: absorb=80 pad=40 obj_y=832 y_lo=80 y_hi=1584 A=752 d_sp=223 aperture_cells=1504
```

**`obj_y`, `y_lo`, `y_hi`, `d_sp`, and `aperture_cells` are identical
between `G40` and `C80` to the last digit — only `absorb` differs (40 vs
80).** Tracing the ablated computation (`y_wall_aperture_sum.py` §[7]):
`build_aperture_grid(cfg,1)` depends only on `(y_lo,y_hi,aperture_cells)`;
`aperture_amplitude` depends only on `(y_lo,aperture_cells)`;
`dist_image_cells` depends only on `(d_sp,obj_y)`; `source_driven_phase`
depends only on `obj_y`; and `r_ablated=np.ones_like(y_grid,dtype=complex)`
has **no dependence on `absorb` at all** — it is `absorb`'s own only
appearance in the unablated integrand (via `r(theta_local(y_s);ABSORB)`)
that the ablation specifically removes. With every other input identical
and `absorb` (the one differing parameter) removed from the computation
entirely, `G40`'s and `C80`'s ablated integrands are **the same Python
expression evaluated on the same floating-point inputs, in the same
operation order, twice** — IEEE-754 arithmetic is deterministic under
those conditions, so the two resulting complex arrays are bit-identical by
necessity, not by favorable rounding. **This is a genuine mathematical
certainty, correctly identified as such by the committed code comment,
not an artifact the current check happens not to have caught a
counterexample to.** There is no discretization/grid-alignment route by
which they *could* differ: both curves are built from `np.linspace(80,
1584, n_pts)` with textually identical arguments, not two independently
rounded quantities that could drift apart. The only way this claim could
fail is if `G40` and `C80`'s `design_geometry.py` entries were not in fact
identical on those five fields — checked directly above, they are.

---

## 6. Charter-applicability check (unchanged from exp-078's own precedent)

Re-confirmed, independent of my own prior-cycle self's Phase-2 finding:
`r(theta_local(y_s);ABSORB)` is `boundary_reflectance.py`'s fixed, static,
per-config transfer-matrix reflectance, reused unchanged (`grep`-confirmed,
no new physics call anywhere in `y_wall_aperture_sum.py`). No intensity
argument, no time dependence, no atom/molecule/real absorbing medium
anywhere in this instrument — `σ(I)`/`σ(x,t)` have no input to act on here;
the coherent interference being scored is fully classical (a Huygens-Fresnel
aperture sum) at these field strengths. Not applicable, correctly, for the
same structural reason as every T28 instrument cycle since exp-069.

---

## 7. Ranked top-3 candidate directions for Iteration 57 (my own seat's lens)

Checked against RULED OUT R1–R9 (nothing below re-proposes a dead end —
in particular, not `A_eff≈518.81`, §2c/Idealization 11's own forward
caution, correctly already flagged in this cycle's own record) and against
the reconciled ranking already on file (`phase2_redteam_audit.md` §8):

1. **Close the smoothness gap this review names (§3) before the standing
   realizable-admittance refit is finally executed.** The refit (exp-078's
   own §7 item 3, still pending for the y-wall's own two-wall extension) has
   only ever been checked for period-invariance at the single-edge model's
   narrower `13.7°–15.1°` envelope. Re-run PHOTONICS' own dense-sweep
   smoothness check (§3(c) of its critique, zero new FDTD, reused code)
   against the realizable substitution at THIS cycle's own full
   `[4.77°,15.50°]` range specifically. If it stays smooth there too, the
   "structurally incapable, for any physically-plausible r(θ)" reading of
   Idealization 9 is earned in full, not merely for the one idealized model
   tested; if it is not smooth, that is the first genuine crack in this
   six-cycle sub-thread's now-repeated "T21, not T28" finding, and would be
   the single most consequential result on the board if it appeared.
   Cheap: this file's own §[2b] vectorized-`r()` machinery already exists to
   run it.

2. **Build the genuinely different instrument this cycle's own §8/§9
   correctly identifies, but pre-register its own spectral reachability
   BEFORE running it** — a plane-wave/global-steering incidence-angle
   construction for the y-wall (the analogue of the x-wall's own
   `theta_beam`-dependent two-plane-wave reduction), the first construction
   in this sub-thread's per-point-image family that would NOT inherit
   Attack 1's structural degeneracy. My own charter's addition to this
   already-ranked item: before spending the build, apply this review's own
   §3.1 Fourier argument to the PROPOSED new construction first — confirm
   in writing that its own per-point weight genuinely carries `theta_beam`
   dependence of a kind that COULD in principle recover a T28-period signal
   at the achievable SNR (using exp-074's own Cramér–Rao pricing machinery,
   §4's own recommended reuse), rather than discovering post hoc, a seventh
   time, that a superficially different construction shares the same
   silent degeneracy.

3. **Quantify a period confidence band for this cycle's own T21-proximity
   claim** (§4) — reuse `desk_check_pricing.py`'s existing Cramér–Rao
   machinery or a residual-bootstrap on the fitted curve, applied to
   `P*_model(PAIR_PAD/C80−C40)`, and report it alongside the existing
   `rel_dev` figures. Cheap, zero new FDTD, closes a real (if
   non-load-bearing) precision gap under a number this cycle's own record
   states to three-significant-figure precision without ever bounding its
   own uncertainty — matching this sub-thread's own repeated R4/R9
   discipline of not letting a precise-looking figure stand unexamined.
