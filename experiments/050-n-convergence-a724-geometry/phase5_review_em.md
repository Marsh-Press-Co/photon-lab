# PHASE 5 — REVIEW (ELECTROMAGNETISM) · Panel Iteration 27 · exp-050

## 1. Code-path equivalence: is `_G_for_g` genuinely `_G_for` on `_geom_derived`'s output, or an OLD-geometry coincidence?

**Genuinely equivalent, confirmed by code inspection AND by the fact there is
only one code path — not merely a bit-exact match at `GEOM_EXP042_OLD`.**

`_G_for_g(lam_cells, gd, obliquity)` (`design_geometry.py:67-79`) computes
`G = exp(i(k·gd["r"] − π/4))/√gd["r"]`, then `G *= gd["obliquity"]` — the
identical two-line formula as exp-042's own module-global `_G_for`
(`experiments/042-.../design_geometry.py:197-212`, `G = exp(i(k·_R−π/4))/√_R;
G *= _OBLIQUITY`), with `_R`/`_OBLIQUITY` replaced by `gd["r"]`/
`gd["obliquity"]`. Verified `gd["r"]`/`gd["obliquity"]` are themselves built
by the identical construction: exp-048's `_geom_derived` (`:179-197`) computes
`dy = y_obs[:,None]-y_src[None,:]; r = sqrt(d_sp²+dy²); obliquity = d_sp/r` —
line-for-line the same as exp-042's module-global `_DY`/`_R`/`_OBLIQUITY`
(`:170-172`), just keyed off `g`'s own dict entries rather than
module-top-level constants. I traced every function this cycle calls
(`_G_for_g`, `_geom_derived`, `_src_amp`, `_window_means`,
`beam_divergence_incoherent`, `beam_divergence_coherent`) and **none
references any of exp-042's hardcoded module-global geometry constants**
(`A`, `NY`, `OBJ_Y`, `D_SP`, `R_OUT`, `GUARD_OUT`, `W_FLANK` as bare names) —
every geometric quantity is re-derived from the `g` dict argument each call.
That means there is exactly **one** implementation of the obliquity-on-E
convention in this module, invoked twice with two different `g` values — the
regression anchor validating it at `GEOM_EXP042_OLD` is not "checking a
different code path that happens to agree," it is checking the only code path
that also runs at `GEOM78`. P-NCONV27-0's own bit-exact pass (0.0 relative
error, all 108 rows, all 3 functions, independently reconfirmed by Red Team's
pre-check and reproduced by Phase 4) is therefore full evidence for GEOM78's
own numbers too, not just for OLD's. **Not a coincidence of only checking
OLD — verified structurally, not merely numerically.**

## 2. The near-zero-crossing account: does it hold up, and is there a sharper EM mechanism?

**It holds up, but NOTES.md's Reading section under-specifies it. I
recomputed the actual n-doubling trajectories directly (not just the
frozen `results.json` summary) for the two new 600nm violations, and the
picture is sharper and more falsifiable than "values ~10⁻⁴, comparable to
ABS_TOL":**

| Cell | `incoherent_corrected` C(n) | `incoherent` C(n), same cell |
|---|---|---|
| 36°/600nm | n=41: **+3.173e-4** → n=81: **−3.691e-4** → n≥161: settles at −3.7215e-4 (bit-stable to 9 s.f. from n=161 on) | n=41: +1.182e-4 → n=81: **−2.311e-4** → n=161: −2.3213e-4 |
| 40°/600nm | n=41: **+1.777e-4** → n=81: **+7.664e-4** → n≥161: settles at +7.660e-4 | n=41: +5.663e-4 → n=81: +8.728e-4 → n=161: +8.723e-4 |

Three findings from this direct computation, none visible in `results.json`'s
own stored fields (only `c41`/`c401`/`converged_value` are recorded, not the
intermediate doublings):

**(a) This is a genuine, clean, fast-converging destructive-interference
null of the angular integral itself — not numerical noise, and not a
per-angle flank/window-normalization artifact.** By n=161 every violating
cell is stable to 9 significant figures; n=41 alone gives the qualitatively
wrong sign. I checked the candidate "null in the incoherent-sum's own
flank/window construction" the Director's brief raised directly: the
per-angle flank-window means `f_θ` (the quantity `incoherent_sum` divides
each profile by) are large and consistently **negative** across the full
41-angle sample at all three violating cells (range ≈ −370 to −930, never
near zero) — the normalization denominator is nowhere near a null. **The
null is in the θ-integral of the fringe itself**: at GEOM78's ~2°-period
600nm fringe, an n=41 uniform grid (Δθ_sample=2.5° across the ±50° sampled
range, with effective weight concentrated within ≈±17° of θ₀, i.e. ~8–9
fringe periods) is a coarse Riemann sum over a rapidly sign-alternating
function whose Gaussian-weighted mean sits very close to zero — a classic
quadrature-aliasing regime, exactly the "phase, not period-magnitude"
axis PHOTONICS and I both flagged at Phase 2 (Attack 1), now shown to bite
in a third function neither of our own diagnostics targeted.

**(b) `incoherent` (the original/committed, obliquity-on-E convention) shows
the *identical qualitative artifact* at the *same two coordinates* — sign
flip, large relative swing, fast settling by n≥161 — yet stays classified
CONFIRMED/no-tier-change. This is the specific, previously undisclosed fact
that answers the Director's question directly: `incoherent_corrected`'s
single-obliquity-via-H convention is NOT uniquely prone to zero-crossings
*in kind* — `incoherent` crosses zero via the same undersampled-quadrature
mechanism at the same cells.** What differs is *degree*, at the level of the
one number the criterion actually tests: the raw n=41→81 absolute step,
`Δabs = |C(81)−C(41)|`. At 36°/600nm: `incoherent_corrected` moves 6.864e-4
(**above** `ABS_TOL=5e-4`, fails); `incoherent` moves 3.493e-4 (**below**,
passes). At 40°/600nm: `incoherent_corrected` moves 5.887e-4 (fails,
narrowly); `incoherent` moves 3.065e-4 (passes). Both cells: the two
functions' aliasing excursions are the same *kind* of event, of comparable
but not identical *size*, landing on opposite sides of a single fixed
absolute threshold. **The tier violation is real and correctly measured, but
it is a boundary-proximity coincidence of the fixed `ABS_TOL=5e-4` gate
against two structurally-similar (not structurally-different) aliasing
artifacts — not evidence that the corrected convention's physics is
qualitatively more zero-crossing-prone than the original convention's.**

**(c) `coherent` never shows this at all, for a completely different and
already-known reason, not a new one:** every `coherent` FWHM=20° cell sits at
|C| ≈ 0.90–0.98 (near-total-shadow, grating-lobe/beamforming regime, per
QUANTUM's own Iteration-23 finding and Red Team's Attack 2 this cycle) — an
entirely different physical quantity, nowhere near this small-signal
edge-diffraction fringe. The three functions therefore split into two
regimes, not three: {`incoherent`, `incoherent_corrected`} share the
zero-crossing-prone edge-diffraction-fringe regime (differing only in
excursion size, per (b)); `coherent` lives in an unrelated saturated regime
Attack 2 already explains.

**So: NOTES.md's Reading option (a)** ("a real, physically meaningful
near-zero-crossing sensitivity *specific to* `incoherent_corrected`")
**is not quite right — it is real and physically meaningful, but not
specific to that one function in kind.** **Option (b)** ("a construction
artifact of `ABS_TOL` being comparable in scale to genuinely tiny `|C|`
values") **is the closer reading, sharpened here to a falsifiable,
quantitative account**: both conventions produce comparably-sized
undersampled-quadrature aliasing excursions at these coordinates; whether a
given (function, cell) pair registers as a tier violation depends on which
side of the fixed `ABS_TOL=5e-4` line its own excursion happens to fall —
verified directly by computing both functions' actual step sizes, not
inferred from the converged values alone.

## 3. Common structural feature across all three violations

All three violating cells (36°/600nm, 40°/600nm, 40°/750nm — the last
pre-registered) share: FWHM=20° (the one regime this program has repeatedly
found under-sampled at n=41, since exp-046/exp-049), `incoherent_corrected`
only among the three functions that show it as an actual tier change, and a
converged value two-to-three orders of magnitude below `C_THR=0.005` —
i.e., every one sits in the criterion's own exemption zone (`|C(2n)| <
C_THR` ⇒ relative check skipped, absolute-only). The mechanism connecting
them, established above by direct computation rather than by the coincidence
of shared magnitude NOTES.md observed: each is a Gaussian-angular-window
average of a fringe oscillating faster than the n=41 grid resolves,
landing close enough to that fringe's own zero that the discrete sum at
n=41 lands on the wrong side of it. The 750nm cell (pre-registered from
Attack 1's Nyquist-proximity diagnostic) and the two 600nm cells (not
pre-registered by either Attack 1 or Attack 2, since Attack 1's own
crossing-diagnostic table was computed only for the 750nm coordinates the
proposal happened to check) are the same phenomenon at different
(λ,θ) coordinates — Attack 1's diagnostic was directionally correct in
mechanism but incomplete in coverage (it was never run at 600nm), a gap
disclosed here, not previously named in this cycle's own record.

## 4. Verdict

**PROMISING.** The headline instrument-fidelity result (P-NCONV27-1: global
max n\*=81, matching A=752 exactly; P-NCONV27-5: FWHM≤10° universally safe
at n=41) is confirmed cleanly and independently re-derivable from
`_geom_derived`'s own geometry-agnostic construction, not merely from
`results.json`'s narrative. The regression anchor is genuinely, structurally
sound (§1) — this is not a case where a same-geometry check happened to
pass. P-NCONV27-2's REFUTATION is real, but it is informative rather than
damaging: it is now (per §2) a quantitatively characterized, falsifiable,
boundary-proximity phenomenon of a fixed absolute tolerance against a
genuine but shared aliasing artifact — not a sign that the corrected
Poynting-flux convention (this program's own Iteration-19 erratum, the
physically-grounded PRIMARY reading since T21) carries some new,
undiscovered physical instability. No T1 exposure, no
`REALIZABILITY_MEMO.md` tier movement, nothing here touches a constraint-3/4
claim — confirmed by the same grep discipline Red Team applied at Phase 2.

## 5. Ranked candidate next-steps for Iteration 28

1. **(Low-cost, desk-only, worth doing — not a dedicated cycle.)** Add a
   one-paragraph addendum to this thread's LOGBOOK entry documenting §2(b)'s
   ABS_TOL-boundary-proximity account, and — since the mechanism is now
   understood, not merely observed — **adopt n\*≥81 as the standing safe
   default specifically for `{incoherent, incoherent_corrected}` at FWHM=20°
   near any near-boundary contamination-risk citation**, closing this exact
   gotcha class permanently rather than re-deriving it per cell each future
   cycle. Zero FDTD, no new machinery — a documentation/policy fix riding on
   work already done this cycle.
2. **(Low-cost, desk-only, optional strengthening.)** Re-run Attack 1's own
   samples-per-period diagnostic at 600nm (it was computed only for the
   750nm coordinates in this cycle's own pre-check) — would have
   pre-registered both new violations before Phase 4, closing the
   incompleteness named in §3. Cheap, but not blocking anything: the
   phenomenon is already explained after the fact with equal rigor.
3. **NOT worth a dedicated Iteration-28 mechanism cycle.** This is
   instrument-calibration business (how a fixed absolute tolerance interacts
   with two conventions' comparably-sized quadrature-aliasing artifacts),
   not new field physics — the underlying T21 edge-diffraction fringe is
   already established and magnitude-validated (Iteration 19), and this
   cycle's own P-NCONV27-2 finding does not suggest either convention is
   wrong, unstable at high n, or in tension with reciprocity/passivity/
   causality. Rank this behind the standing higher-value queue items already
   carried from Iteration 26/27 (the genuine FDTD `ABSORB` sweep at the
   T21-vs-T24 geometry; THERMODYNAMICS' overdue `h_eff` re-derivation; the
   fixed-absolute-thickness `graded_black_shell` variant) — none of which
   this cycle's finding should displace.
