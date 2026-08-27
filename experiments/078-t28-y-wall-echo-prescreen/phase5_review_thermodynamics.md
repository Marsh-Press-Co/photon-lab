# THERMODYNAMICS — Phase 5 Review · Panel Iteration 55 · exp-078 (T28 y-wall echo pre-screen)

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md, verbatim): "where
absorbed energy goes. Always asks what re-radiates and whether it would be
detectable. Owns the per-proposal energy sidecar: absorbed power ->
temperature rise -> emission band -> detectability. Expressibility
contract: the sidecar is a post-run analytic calculation, not an FDTD
output, and is labeled as such." Blind to all other Phase-5 reviews this
cycle, including my own Phase-2 critique's text (read only as a historical
artifact under review). Grounded on PANEL.md, AGENTS.md, LOGBOOK.md in full
(R1–R9, T28's complete Iteration 46–54 history) and exp-075/076 before
reading the exp-078 record. T1 escape route: N/A throughout (instrument/
model-fidelity thread, no absorber, no scene, no constraint-3 engagement
anywhere in this file) — the literal per-proposal energy sidecar (absorbed
power → ΔT → emission band → detectability) has no witness-scene object to
attach to here, exactly as every T28 cycle since exp-071 has stated. What
follows is this seat's actual charter question at the level this cycle
does engage: does absorbed-power/reflectance bookkeeping explain any of
this cycle's own numbers.*

---

## 0. Verdict

**PARTIAL**, from this seat's own lens.

exp-078's Test-A-only INCONCLUSIVE (0/3 SUPPORT, 0/3 REFUTE, corrected)
holds up under my own independent re-derivation of the numbers that matter
to my charter (§1). The y-wall mechanism class is not ruled out by this
pre-screen and I find no energy-based reason to rule it out myself. But it
is also not promising by any measure this seat can bring to bear:
`PAIR_PAD` — T28's own dominant target, and the one comparison my charter
should have the most to say about — turns out to be **provably invisible
to absorbed-power bookkeeping entirely** (§3), so my seat's own marquee
contribution to this sub-thread (the "near-total absorption leaves little
energy budget" caution) does no discriminating work on the number the
program actually cares about. What keeps this from a clean close is a
genuine, independently-verified record gap (§2): the mandatory-fix docket
item requiring `phase1_proposal.md` §5.2 to be re-reported with the
corrected numbers was not actually executed, and the specific figure my
own prior critique's caution now hangs on (`≥99.9999%` at `C80`) traces to
data that (a) does not match the corrected primary model the rest of the
document runs on, and (b) is no longer even reproducible from the
committed script/JSON at all.

---

## 1. Independent re-verification of the corrected primary model —
holds up exactly

I did not take Phase 3/4's word that the angle fix "essentially doesn't
move `PAIR_PAD`." I pulled `primary_model_pair_deltas` and
`primary_model_scores` directly from `y_wall_prescreen_results.json` and
cross-checked every scored number against `phase4_results.md`'s own table:

```
c80_c40:        P*=4.0000°  rel_dev=0.4074  (at search boundary, every stage) → INCONCLUSIVE
pair_absorb40:   P*=2.8045°  rel_dev=0.3284                                    → INCONCLUSIVE
pair_pad:        P*=3.2180°  rel_dev=0.3021                                    → INCONCLUSIVE
```

All three reproduce Phase 4's table bit-for-bit, and the `as_filed_
incorrect_audit_trail` block independently confirms the as-filed numbers
(`0.1296`/`0.2330`/`0.3136` — 2 of 3 SUPPORT) the corrected numbers
superseded. I separately re-confirmed the code-level fact my own Phase-2
critique's cancellation argument rests on: `C40` and `G40` share
`absorb=40` in `dg065.CONFIGS` (`geometry` block of the JSON), so
`edge_image_curve`'s own `absorb_for_r=c["absorb"]` call feeds the
IDENTICAL reflection coefficient into both configs' curves at every swept
θ — meaning `arg(r(θ;40))`, and `|r(θ;40)|`, are bit-identical objects in
both terms of the `PAIR_PAD` difference regardless of which angle
convention (`theta_deg` vs `90-theta_deg`) is used, since the convention
only changes what angle is fed into a shared function, not whether it's
shared. This is the reason `PAIR_PAD` moves by only 0.0115 (`0.3136→
0.3021`) while `C80−C40`/`PAIR_ABSORB40` — which mix `ABSORB=40` against
`ABSORB=80` — move by far more (`0.1296→0.4074`, `0.2330→0.3284`). My own
prior critique's central claim holds up exactly under this cycle's actual
run, unlike last cycle's arithmetic slip.

---

## 2. NEW finding — the mandatory-fix docket's own item 2 was not fully
executed: `phase1_proposal.md` §5.2 still reports the as-filed, angle-
uncorrected per-config numbers, silently, under a section already
relabeled "CORRECTED," and the specific figure my own caution now rests
on does not survive independent recomputation

Red Team's own Phase-2 audit (`phase2_redteam_audit.md`, mandatory-fix
item 2, verbatim): **"Re-report §5.2/§5.3 with the corrected numbers as
primary."** `phase4_results.md` §3 claims this closed: *"applied directly
to `phase1_proposal.md` — original text retained, struck through/labeled
superseded, corrected replacement text added inline."*

I checked this against the actual committed file and the actual committed
JSON, not against either claim. `phase1_proposal.md`'s §5.2 table (lines
255–261) reads:

```
C40 | 76.897° | [0.0029, 0.0064] | 3.2180° | 0.1557 | no
C60 | 131.795° | [0.0001, 0.0007] | 4.0000° | 0.2418 | yes (widens to 60°, R²=0.9895)
C70 | 133.798° | [0.0001, 0.0001] | 4.0000° | 0.2777 | yes (widens to 60°, R²=0.8740)
C80 | 358.446° | [0.00003, 0.00012] | 3.1880° | 0.1439 | no
G40 | 76.897° (=C40, exact) | [0.0029, 0.0064] | 3.2105° | 0.1544 | no
```

`y_wall_prescreen_results.json::primary_model_edge_curves` +
`primary_model_period_search.chosen` — the actual output of the
now-corrected, committed script, Phase 4's own official re-run — reads:

```
C40: ptp=75.2088°  |r|∈[0.015755, 0.038656]  P*=3.218045°  R²=0.153653  at_boundary=False
C60: ptp=119.6987°  |r|∈[0.002521, 0.007152]  P*=3.127820°  R²=0.119659  at_boundary=False
C70: ptp=356.1519°  |r|∈[0.000968, 0.003627]  P*=3.195489°  R²=0.142370  at_boundary=False
C80: ptp=355.6947°  |r|∈[0.000202, 0.001889]  P*=2.909774°  R²=0.109967  at_boundary=False
G40: ptp=75.2088° (=C40, exact)  |r|∈[0.015755, 0.038656]  P*=3.105263°  R²=0.120376  at_boundary=False
```

**Every column disagrees except C40's `P*` (coincidence — see caveat
below), and the qualitative claim carried in the row text — `C60`/`C70`
"run to the search boundary... widens to 60°" — is FALSE under the
corrected model**: `primary_model_period_search.chosen` shows
`at_boundary: False` for all five configs; only the pair-DELTA
`c80_c40` (a different computation, §5.3) still hits the boundary. The
`|r|` ranges are the load-bearing part for my own charter: **the
corrected model's `C80` reflects roughly 6.7×–15.7× more strongly at its
two endpoints than the still-printed as-filed range** (`0.0002025/
0.00003=6.75×` low end, `0.0018892/0.00012=15.74×` high end), and the
residual
(non-absorbed) power fraction at the corrected model's own worst point is
**248× larger** than the as-filed figure this table still shows:

```
AS-FILED C80 |r|max=0.00012:  1-|r|² = 99.99999856%  (residual 1.440e-08)
CORRECTED C80 |r|max=0.0018892366...:  1-|r|² = 99.99964308%  (residual 3.569e-06)
ratio: 3.569e-06 / 1.440e-08 = 247.9×
```

This directly undercuts the specific digit-string my own contributed
physical caution now carries in §7's corrected replacement text (and
which Red Team's own audit, `phase2_redteam_audit.md` line 522, also
repeats verbatim without independently recomputing it): **"near-total
absorption (`≥99.9999%` at `C80`)."** That claim is true at the corrected
model's best point (`|r|min=0.0002025 → 99.999996%`) but **false at its
own worst point** (`|r|max=0.0018892 → 99.999643%`, short of the sixth
nine by 3.57×) — and the worst point is the one the caution's own logic
needs (a robustness claim about "little energy budget left" should hold
at the *least*-absorbing point in the sweep, not just the most-absorbing
one). The honest corrected statement is **"≥99.9996% at `C80`, all
θ∈[36°,42°]"** — still an extremely strong near-total-absorption
statement for my own qualitative point (§3), just not the specific figure
now sitting in the record.

**A second, sharper problem, independent of the digit itself**: I checked
whether the as-filed per-config numbers this table still shows are even
reproducible from the currently committed pipeline at all. `y_wall_
prescreen_results.json::as_filed_incorrect_audit_trail` — the file's own
explicitly-labeled audit-trail block, added specifically to satisfy this
docket item — contains **only `pair_deltas` and `scores`** (the three
`PAIR_*`/`C80-C40` comparisons); it holds no individual per-config `ptp`/
`|r|`/`P*`/`R²`/boundary data for `C40`–`G40` at all. **The five rows in
§5.2's table are therefore not recoverable, correct OR as-filed, from
anything currently committed to this directory** — they are the one place
in this cycle's entire record that fails this program's own R4 standard
("any falsifier or self-consistency figure... MUST be produced by
invoking the actual committed function... never hand-typed") outright,
inside a document whose own header claims a "CORRECTED" pass over exactly
this section.

**Caveat on `C40`'s apparent match**: the table's `C40` row (`P*=3.2180°,
R²=0.1557`) is close to but not identical to the JSON's corrected `C40`
(`P*=3.218045°, R²=0.153653`) — the period matches to 4 significant
figures (plausibly the as-filed and corrected `C40` periods are close by
chance, since the angle shift's effect on `|r(θ;40)|`'s *phase* content,
as opposed to magnitude, is evidently smaller than its effect on
magnitude), but the R² does not (`0.1557` vs `0.1537` rounded) — I do not
have the as-filed per-config JSON to settle which of "table is stale" or
"table was independently recomputed and happens to be very close" is
true for this one row, precisely because that JSON does not exist (the
point above). Given the other four rows disagree substantially and the
qualitative boundary-widening claim is flatly false under the corrected
model, "stale, unedited since Phase 1" is the far more likely
explanation, but I flag the one row where I cannot rule out
"independently recomputed and coincidentally close" with full confidence.

**Disposition**: non-load-bearing to exp-078's own Combined result (§5.3,
the section actually gated and scored, WAS correctly updated and I
reproduce it exactly in §1) but a real, R4-family correction is owed —
distinct from, and sharper than, my own exp-077 finding last cycle (a
comparison computed in incommensurable units); this one is a docket item
marked closed that demonstrably was not, on a section a Red Team audit
explicitly named by number. Recommend: either recompute and backfill
`as_filed_incorrect_audit_trail` with the individual per-config as-filed
curves for a true audit trail, or delete §5.2's stale table entirely and
replace it with the corrected `primary_model_edge_curves`/`period_search`
values shown above (my own preference — the as-filed per-config numbers
serve no purpose §5.3's own as-filed/corrected pair already doesn't
serve, and keeping unreproducible numbers in the permanent record is
exactly the failure mode R4 exists to prevent).

---

## 3. The task's own question, answered directly: is the near-total-
absorption caution load-bearing for `PAIR_PAD`, or does it explain
nothing new?

**It explains nothing about `PAIR_PAD`, and this is structural, not a
close call.** `PAIR_PAD` is `(C40, G40)` — both `ABSORB=40`. Neither
configuration ever enters the near-total-absorption regime my caution is
about: `C40`/`G40`'s own `|r|` range is `[0.0158, 0.0387]` under the
corrected model (`[0.0029,0.0064]` even under the stale as-filed one) —
absorbed fraction `99.85%–99.98%`, comfortably below "near-total" in any
sense that would starve a coherent phase term of energy. The
near-total-absorption regime (`≥99.9996%`, corrected) belongs
exclusively to `C60`/`C70`/`C80` — configs that `PAIR_PAD` never touches.
**My own seat's headline contribution to this sub-thread since exp-075
(now carried through exp-076/077/078 as "the" THERMODYNAMICS caution) is,
by construction, about a variable `PAIR_PAD` does not vary.**

Where the caution DOES touch real comparisons — `C80−C40` and `PAIR_
ABSORB40`, both of which include `C80` — it still does no discriminating
work, for the same reason it did none for the x-wall model (exp-075/077,
already REFUTEd): in both mechanism classes, wherever `C80`'s near-total
absorption is even relevant, the verdict is already settled by gross
period/shape mismatch or a clean null-calibration result before an
energy argument is needed. Here specifically: `C80−C40`'s corrected model
has **no resolvable interior-optimum period at all** in this window (runs
to the 60° boundary at every stage) — a fact about the *phase function's*
own shape, established without reference to `|r|`'s magnitude; and the
fresh 20,000-trial null-calibration (`phase4_null_calibration_corrected.
py`) already shows none of the three corrected comparisons are
distinguishable from pure noise (`p=0.13`–`0.83`) without any energy
argument entering the calculation. The x-wall precedent is the same
shape: `PAIR_PAD`'s two-wall Test B REFUTEd at `r²=0.0001` (exp-077) —
overwhelming on its own terms, no absorption argument required or cited.
**Six-plus T28 cycles in, this caution has never once been the thing that
moved a verdict.** It remains true and worth stating (§2's corrected
`≥99.9996%` figure), but it is decorative physical color, not evidence,
everywhere it has been applied in this sub-thread to date — a fair,
if unflattering, self-assessment for this seat to log.

**What, then, explains `PAIR_PAD`'s persistent landing near `rel_dev≈
0.30`–`0.31` across both this cycle's angle conventions, from an energy
lens specifically?** Nothing does, and that is itself the answer worth
recording: because `r(θ;40)` is a single shared object between `C40` and
`G40` by direct code-level construction (§1), `PAIR_PAD`'s entire
predicted signal under this model is **provably independent of the
boundary's absorbed-power behavior** — it can only be a pure geometric-
propagation-phase effect (the `76.999`-vs-`154.500`-cell fixed-offset
difference), the identical structural conclusion ELECTROMAGNETISM reached
for the x-wall model at exp-076 (`PAD` is lossless vacuum). This cycle's
own y-wall self-echo construction reproduces that same conclusion by an
independent code path (a different `Sim._damping` edge, a different
propagator), which is a genuine, if modest, cross-validation of exp-076's
finding rather than new information: **whatever eventually explains
`PAIR_PAD`'s real ~4.6° period, it is not going to be found by refining
this seat's own instrument.** The persistence of `rel_dev≈0.30` across
angle conventions is fully explained by the trivial fact that the angle
correction only touches the shared, cancelling `arg(r(θ;40))` term's
*input angle*, not whether it cancels — it was never going to move this
number much, and my seat has nothing further to add on why the *residual*
~0.30 gap (geometric-phase-model vs. real data) exists. That is squarely
PHOTONICS'/ELECTROMAGNETISM's question (is the edge-dominance idealization
or the single-near-wall-only idealization, §6.1/§6.3, hiding the missing
~30% of period), not mine.

---

## 4. Ranked candidate directions for Iteration 56 — energy-accounting lens

Checked against R1–R9 and the named dead ends (`A_alt≈3·R_OUT`, the
`519`-cluster, `P`-normalized phase offset) — none of the three below
touch any of them.

**1. `|r|`-weight the self-echo model** (already an open question in
`phase1_proposal.md` §8 item 2 and Idealization 2; reframed here as an
energy-conservation argument specifically, not just a modeling nicety).
The current `cos(Δφ_self)` proxy treats every config's contribution as
unit amplitude regardless of how strongly that wall actually reflects —
physically indefensible for a Huygens-Fresnel-style coherent field sum,
where a wall whose own `|r|` sits at `0.0002`–`0.0019` (`C80`, corrected)
cannot contribute a comparably-weighted term to a real interference
pattern as one whose `|r|` sits at `0.016`–`0.039` (`C40`/`G40`,
corrected) — roughly one to two orders of magnitude apart in field
amplitude, not power. Concretely: rebuild `C80−C40`/`PAIR_ABSORB40`'s model
curves as `|r(θ;ABSORB)|·cos(Δφ_self(θ))` differences rather than bare
`cos(Δφ_self(θ))` differences (desk-only, reuses everything already
built) and re-score against the same reference periods. Note explicitly,
so this is not oversold: this would NOT move `PAIR_PAD` (both terms share
the identical `|r(θ;40)|`, so the weighting factors out of the
difference symmetrically) — it is a targeted fix for the two comparisons
where near-total-absorption configs may be over-weighted, not for T28's
actual dominant target.

**2. Test whether the `PAD`-tied signal survives with a real absorbing
article loaded** (named at Iteration 53 item 7, Iteration 54 item 9 —
**now deferred a third consecutive cycle**, the LOGBOOK's own Iteration-54
ranking explicitly flagged a third deferral as needing "an explicit
reason," which this cycle did not give). Repeating my own exp-077 ranking
verbatim because nothing has changed: every congruent-series config to
date, `{C40,C60,C70,C80,G40}`, is an *empty scene* — every "absorption"
this whole six-plus-cycle sub-thread has discussed, including this one, is
domain-truncation-boundary bookkeeping, never a physical article warming
up. This is the only queued item that would give this seat's own sidecar
an actual thermodynamic referent for the first time in T28's history.

**3. Broadband pulsed reflectance spectroscopy of the `ABSORB` boundary**
(named at Iteration 53 item 5, Iteration 54 item 8 — also unexecuted).
Every T28 cycle to date, including this one, prices absorbed power as a
single analytic transfer-matrix number (`1-|r(θ;ABSORB)|²`) at one
wavelength. A handful of pulsed broadband FDTD calls measuring the
boundary's own time-domain Poynting-flux absorption would be the first
time this sub-thread checks the analytic proxy against an actual measured
energy flux — directly relevant given how much this cycle's own numbers
moved (§2) under a mere angle-convention correction to the SAME analytic
proxy.

None of these three re-open R1–R9 or any named dead end; all extend
already-vetted, already-committed machinery (`boundary_reflectance.py`,
`y_wall_prescreen.py`, `lab/fdtd2d.py::Sim.run()`, `lab/thermo_sidecar.py`
for item 2's eventual sidecar once a real object exists to feed it).
