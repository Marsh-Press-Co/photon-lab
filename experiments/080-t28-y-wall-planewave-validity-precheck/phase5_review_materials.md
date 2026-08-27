# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 57 · exp-080
## Independent re-verification of `part_b_realizable`, a from-scratch physics
## check of the realizable-admittance substitution, and the realizability-
## bound framing question, for the now-COMPLETE cycle

*Fresh sub-agent, blind to the other six seats' Phase-5 reviews this cycle.
Read `PANEL.md`, `AGENTS.md`, LOGBOOK.md's RULED-OUT registry and T28 thread
tail, `phase1_proposal.md` (incl. PHASE 1 RESULTS), `validity_precheck.py`
as it now stands post-fold-in, `validity_precheck_results.json`, all five
Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`phase4_results.md`, `_output.txt`, and my own seat's prior review
(`experiments/079-.../phase5_review_materials.md`) in full. Independent
computation performed below from primitives, in a fresh scratch script —
not asserted from the committed JSON or from either of the two prior blind
re-derivations already on record (MATERIALS' own Phase-2 critique, Red
Team's Phase-2 audit).*

---

## 1. Verdict on the whole cycle: **PARTIAL**, concurring with the record's
## own Combined Verdict, for a materials-lens reason stated independently

This cycle makes no material or mechanism proposal of its own — it is a
zero-FDTD validity/sensitivity check on an approximation scheme (replacing
a per-point bounce angle with one global `theta_eff`) layered on top of an
aperture-sum construction already known, since exp-079, to be structurally
incapable of discriminating a real y-wall echo from none. From this seat's
own charter (the realizability bound), nothing in this cycle moves that
bound in either direction: the underlying admittance physics is unchanged
from exp-075's own finding — the "matched" (`eps=mu`) family this whole
sub-thread's `r(theta)` machinery is built on requires a broadband,
angle-tracking magnetic-loss response with no realizable analog at optical
frequencies (`unobtainium-with-parameters`, restated, not re-derived, by
this review). What this cycle DOES newly and correctly establish, confirmed
independently below, is that the single-global-angle approximation's own
internal shape-fidelity is admittance-family-sensitive, and fails harder
under the one family with any claim to buildability. That is real,
non-trivial information for anyone about to build PHOTONICS' next
construction — but it is a finding about approximation quality, not a
finding that changes what a real wall could or could not do. **PARTIAL**
is the correct verdict; nothing here promotes the mechanism-class board to
RULED OUT or to a checkpoint, and nothing here understates or misrepresents
a constraint.

---

## 2. Independent re-verification of `part_b_realizable()` (mandate item 1)

I wrote a fresh script
(`/tmp/.../scratchpad/verify_part_b_realizable.py`, not shown in the repo —
session-local), importing only the lower primitives `validity_precheck.py`
itself imports (`dg065.CONFIGS`, `br.n_profile_exact`/`damp_e_profile`/
`nu_profile`/`CPL`, `ywas.aperture_amplitude`/`dist_image_cells`/
`theta_local_deg`/`source_driven_phase`/`build_aperture_grid`/`K600`). I did
**not** call `reflection_coefficient_vec_realizable`, `single_angle_curve_
realizable`, or `part_b_realizable` themselves — I re-typed the TE-wave
recursive input-impedance transfer-matrix recursion from scratch from the
standard physics (see §3), and re-implemented the trapezoidal quadrature by
hand (`numpy.trapz` is absent from this environment's numpy build, which
also forced a fully independent quadrature, not an accidental reuse of
`ywas._trapz`).

Result (mean over the 5 congruent configs, `R²(Re)` at the amplitude-
weighted `theta_eff`):

| cfg | my `theta_eff` | my `R²(Re,realizable)` | committed JSON |
|---|---|---|---|
| C40 | 8.6458° | **−0.622993** | −0.622993 |
| C60 | 8.4027° | 0.998196 | 0.998196 |
| C70 | 8.2865° | 0.991600 | 0.991600 |
| C80 | 8.1736° | 0.995934 | 0.995934 |
| G40 | 8.1736° | **−0.210328** | −0.210328 |
| **mean** | | **0.430482** | 0.430482 |
| **min** | | **−0.622993** (C40) | −0.622993 |

Exact match, to 6 significant figures (the residual ~1e-8 difference is
pure floating-point quadrature-order noise between my hand trapezoid and
`ywas._trapz`, not a discrepancy). As a pipeline sanity check I also ran the
identical fresh script against the **matched** family for C40 and got
`R²(Re)=0.824430`, matching `phase1_proposal.md`'s reported `0.8244`
exactly — confirming my independent harness reproduces both admittance
families correctly, not just the one under review by luck.

**This is the THIRD independent from-scratch reproduction of this exact
number** (MATERIALS' own blind Phase-2 critique, Red Team's Phase-2 audit
§0 item 4, and now this Phase-5 review), each written without importing the
others' code. I find no discrepancy. `part_b_realizable()`'s reported
REFUTE verdict (mean `R²=0.4305`, C40/G40 negative) is correct.

---

## 3. Is `Zi=1/sqrt(n²-sin²θ)` the right realizable substitution, and does
## `kxi` also need to change? (mandate item 2)

**No missing subtlety — the substitution as coded is physically correct,
and `kxi` is correctly left unchanged.** Derivation, done independently
here (not copied from either prior critique):

For a TE-polarized plane wave in a layer with relative permittivity `ε_r`
and permeability `μ_r` (so `n²=ε_r·μ_r`), Snell's law conserves the
tangential wavenumber (`k0·sinθ`, set by vacuum) regardless of the layer's
own `ε_r`/`μ_r` split. The normal (transverse) wavenumber is therefore

  `kx = sqrt(k² − k0²sin²θ) = k0·sqrt(n² − sin²θ)`

— a function of `n²` (the *product* `ε_r·μ_r`) alone. Two layers with the
same complex `n(x)` but a different `ε_r`/`μ_r` split (same product, e.g.
"matched" `ε_r=μ_r=n` vs. "realizable" `ε_r=n²,μ_r=1`) have **identical**
`kx` — the reflection-relevant *phase accumulation* through each layer is
unaffected. What *does* depend on the split is the TE wave impedance,
`Z_TE = μ_r/kx` (up to the same `η0`, `ω` normalization applied identically
to `Zvac=1/cosθ`), because only `μ` couples to the transverse-magnetic
boundary condition for this polarization. That is exactly the one line the
code changes (`Zi = ni/sqrt(rad)` → `Zi = 1.0/sqrt(rad)`), while `kxi` and
`rad` are shared, unedited lines in both `reflection_coefficient_vec` and
`reflection_coefficient_vec_realizable`. **Confirmed by direct source
comparison**: `validity_precheck.py` lines 288-299 keep `rad = ni**2-s2`
and `kxi = k0*sqrt(rad)` byte-identical between the matched and realizable
functions; only the `Zi=` line differs (with an explicit inline comment
flagging it as "the one line that differs"). This is the physically
required behavior, not a coincidence — a version where `kxi` were also
edited to depend on `μ_r` separately would be the actual bug, since `kx`
is a purely geometric/dispersive quantity independent of how `n²` is
apportioned. **No fix needed; the methodology is sound as implemented.**

**One documentation-accuracy issue found, non-load-bearing.** The new
docstring for `reflection_coefficient_vec_realizable()` (line 281) reads:
*"the per-layer admittance `Zi=ni/sqrt(ni²-sin²(theta))` (implicitly
`mu_r=ni²`...)"* for the matched family. That is inconsistent with the
derivation above (`Z_TE ∝ μ_r/sqrt(n²-sin²θ)` and the code's own
`Zi=ni/sqrt(rad)` together imply `μ_r=ni`, **not** `ni²`) — and, more
importantly, inconsistent with this exact sub-thread's own established and
eight-times-independently-reconfirmed name for this family: **"matched
`eps=mu`"** (`ε_r=μ_r=n`, both equal to `n`, giving `n=sqrt(ε_r·μ_r)=n` ✓),
used identically in `boundary_reflectance.py` (line 188), `y_wall_aperture_
sum.py`'s own comments, and every MATERIALS Phase-2/Phase-5 document from
exp-075 through exp-079 (`phase5_review_materials.md` line 145: *"matched
(`eps=mu`) TE admittance"*; `phase2_critique_materials.md` at exp-075/077,
same). If `μ_r=ni²` per the new docstring, then `ε_r=n²/μ_r=1` — i.e. an
*ordinary, non-magnetic* medium, the exact opposite of what "matched/
unobtainium" is supposed to mean here. This is a wording slip introduced
in this cycle's own fix-docket fold-in (the executable code is unaffected
— it never references `mu_r` numerically, so **no computed number in this
cycle is wrong**), but it is exactly the kind of small mischaracterization
this program's own R1-addendum/R4 discipline exists to catch before it
propagates: a future reader citing this docstring would get the physical
picture backwards. **Recommend a one-line docstring correction**
(`mu_r=ni`, or simply "the matched eps=mu family, eps_r=mu_r=n_i") the next
time this file is touched; not urgent enough to justify a fix-only commit
on its own.

---

## 4. New finding: the C40/G40 REFUTE is a genuine phase/shape failure, not
## a calibration artifact (robustness check, not previously run)

Fix-docket item 4 (this cycle) already showed that part (b)'s *matched-
family* `R²(abs)` pathology at C70/C80 was ~50% an avoidable best-fit-scale
calibration artifact (raw `−7.82/−8.45` vs. shape-only-optimal
`−1.65/−2.30`). Neither `part_b_realizable()` nor any Phase-2 critique ran
the analogous check on the **realizable-family** `R²(Re)` pathology at
C40/G40 — I ran it, independently, as a robustness probe this review adds:

| cfg | raw `R²(Re,realizable)` | best-fit real scalar `α*` | scale-corrected `R²(Re)` |
|---|---|---|---|
| C40 | −0.6230 | **−0.832** | 0.162 |
| G40 | −0.2103 | **−2.432** | 0.212 |
| C60 | 0.9982 | +1.044 | 1.000 |
| C70 | 0.9916 | +1.058 | 0.995 |
| C80 | 0.9959 | +1.043 | 0.998 |

Two things distinguish this from the earlier abs-proxy calibration finding.
First, `α*` is **negative** at C40/G40 (vs. a positive-but-undershooting
scale in the earlier abs-proxy case) — the single-`theta_eff` model's real
part is anti-correlated in sign with the true per-point curve's dominant
variation at these two configs, not merely mis-scaled. Second, even the
most generous possible correction (a free real scalar, including a sign
flip, which `r(theta_eff)` does not actually have as a physical degree of
freedom) only recovers `R²≈0.16–0.21` — nowhere near the `0.75` floor or
`0.90` SUPPORT bar, and still below the `0.50` REFUTE line. **This means
the REFUTE verdict at C40/G40 is not an avoidable calibration artifact of
the kind fix-docket item 4 found elsewhere in this same file** — it is a
genuine failure of the single-angle model to track the true curve's SHAPE
under the realizable admittance, concentrated exactly where part (a)'s own
FORECLOSE evidence (the `2.75×` `theta_local` spread) already says a single
angle is least defensible. This strengthens, rather than merely
reconfirms, confidence in the REFUTE verdict.

As a mechanistic cross-check (also independent, not in any prior document
I read for this cycle), I evaluated `arg(r)` for both admittance families
at each config's own `theta_eff` (≈8.2–8.6°): the matched-vs-realizable
phase deviation is **−72.6°** at ABSORB=40 (C40/G40) vs. only **~1.1–1.5°**
at ABSORB=60/70/80 — the same order-of-magnitude concentration exp-079's
own MATERIALS review found at a different, wider angular sweep (`89.08°`
envelope-max at ABSORB=40 vs. `1.19–18.35°` elsewhere). Two independently-
computed angular ranges, same qualitative story: the two admittance
families' phase behavior diverges sharply and specifically at the
shallowest (`ABSORB=40`) loss depth, and that is exactly where the
single-angle reconstruction fails hardest under the realizable family.
Consistent, not coincidental.

---

## 5. Does `phase3_synthesis.md`'s "admittance-family-dependent" framing
## correctly characterize the realizability implication? (mandate item 3)

**Technically accurate as far as it goes; incomplete in one respect worth
naming, not a wrong claim.** The synthesis correctly labels the matched
family "unobtainium" and the `mu_r=1` family "realizable," correctly
reports both numbers, and correctly states neither the SUPPORT-vs-REFUTE
split nor the underlying construction's realizability is settled by this
test (§3(c) explicitly keeps Checkpoint criterion 2 NOT YET RIPE). It does
**not**, however, restate the specific disclaimer this seat's own prior
review (exp-079, §1) attached to this identical substitution:

> *"It does not touch the realizability bound this seat owns, in either
> direction... this cycle neither confirms nor refutes anything about
> whether a buildable (`mu_r=1`) instantiation would behave differently."*

That disclaimer matters here for a precise reason: `part_b_realizable()`
holds `n(x)` **fixed** at the profile derived from the matched-loss FDTD
absorber's own `damp_e_profile` (the same `nu_profile`/`n_profile_exact`
call, unchanged) and swaps only the admittance-formula's `μ_r`/`ε_r` split.
That is a legitimate, cheap sensitivity probe on the SAME machinery — it is
not a model of an independently-designed, actually-buildable ordinary-
dielectric coating engineered to hit some target reflectance; such a
coating would in general need its own `n(x)`, not this cycle's inherited
one. So "REFUTE under the realizable family" should be read narrowly, as
this review reads it: *if* a buildable, `μ_r=1` structure happened to share
this exact complex-index profile, the single-global-angle simplification
of the (already-foreclosed-on-other-grounds) per-point model would fit its
own shape worse — a statement about approximation fidelity, layered two
removes from a statement about what any specific buildable wall could
achieve. Read that way, phase3's framing is not wrong, and I do not think
it overstates the case (it never claims a buildable wall has been "ruled
out"). But read loosely by a future reader skimming only "REFUTE
(realizable)," it invites exactly the overreading this seat's exp-079
review pre-empted explicitly and this cycle's synthesis does not restate.
**Recommendation, not a correction of anything already claimed**: the next
document in this sub-thread that cites exp-080's `(b)` result should carry
the exp-079 §1 disclaimer forward verbatim (or an equivalent), the same way
this cycle correctly carried forward exp-079's own admittance-correlation
collapse (§2a) as reasoning material. One further point in the other
direction, also worth stating plainly for the realizability bound this
seat owns: of the two numbers on offer, **the realizable one is the only
one that could ever describe a real material** — the matched number
describes a family already established (exp-075) as requiring an
angle-tracking magnetic-loss response with no known optical-frequency
analog. A future synthesis leaning on the matched-family `0.7345`
INCONCLUSIVE as the "better" or "primary" number, because it is the
one originally pre-registered, would be citing the physically irrelevant
family for any claim about what a buildable wall's approximation quality
looks like. This cycle does not make that mistake (both numbers are
reported, REFUTE is not buried), but it also does not say this explicitly
— worth stating outright next time this framing recurs.

---

## 6. Anything else new

Nothing else load-bearing. `part_c_power_budget_at_true_angle()` and
`part_d_photonics_construction()` do not touch the realizability bound
(they reuse the matched-family `reflection_coefficient_vec` unchanged, a
choice already flagged and scoped correctly elsewhere in the record). I
did not find any other admittance-family conflation, mismatched-family
comparison, or hand-typed number in `validity_precheck.py` as it now
stands — the fix-docket fold-in is clean.

---

## 7. Summary

**Verdict: PARTIAL**, concurring with the cycle's own Combined Verdict.
Independent re-verification (§2, a third from-scratch reproduction)
confirms `part_b_realizable()`'s numbers exactly: mean `R²=0.4305`, REFUTE,
C40/G40 negative. The realizable-admittance substitution's methodology is
physically sound (§3) — `kxi` is correctly left unchanged because it
depends only on `n²`, not on the `ε_r`/`μ_r` split, and no subtlety was
missed there — though the new docstring's characterization of the matched
family's own `μ_r` value is a (non-load-bearing) documentation error
inconsistent with this sub-thread's own eight-cycle-established "eps=mu"
naming. A new robustness check (§4), not previously run, shows the C40/G40
REFUTE survives a best-fit-scale correction (unlike the earlier abs-proxy
pathology elsewhere in this same file) — it is a genuine phase/shape
failure, strengthening rather than merely reconfirming the verdict.
Phase 3's "admittance-family-dependent" framing (§5) is accurate but
should, next time it is cited, carry forward this seat's own exp-079
disclaimer that this substitution bears on approximation fidelity, not on
whether any buildable wall could achieve the underlying response — and
should say plainly that the realizable number, not the matched one, is the
one that will ever describe a real material.
