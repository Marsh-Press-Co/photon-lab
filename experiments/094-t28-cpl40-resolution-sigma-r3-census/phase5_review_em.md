# PHASE 5 — REVIEW · ELECTROMAGNETISM (blind) · exp-094 · Panel Iteration 71

*Fresh sub-agent, ELECTROMAGNETISM charter. Read in full: PANEL.md;
LOGBOOK.md (RULED OUT R1–R15 verbatim, ESTABLISHED, LIVE THREADS T1–T28 in
full including the complete T28 sub-thread history, Iterations 46–70);
PLAN.md's Current-state section; the complete exp-094 record
(`phase1_proposal.md`, all five Phase-2 critiques including my own,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md` in full,
`run.py`, `results.json`, `run_output.txt`). Independently re-derived from
primary source this session: `lab/fdtd2d.py::Sim.__init__`/`run` (the
E-update loss coefficient), `lab/materials.py::graded_black_shell`/
`_graded_black` (the smoothstep profile gate 5 actually reads), and the
raw `results.json` gate/rank1a/rank1b blocks plus exp-093's own filed
`item1` cpl=30 numbers, pulled directly, not from any prose citation. Blind
to every other seat's current Phase-5 review and to the Red Team audit.*

## 1. Independent re-derivation: does `SIGMA_R4_CORRECTED=0.25` actually
hold the invariant, in the executed run, not just on paper?

`lab/fdtd2d.py::Sim.run` states the E-update explicitly:

```
alpha = self.sigma_e * S / (2.0 * self.eps_r)      # S = courant_frac/sqrt(2), fixed
ca = (1.0 - alpha) / (1.0 + alpha)
```

Grid convention is `dx=1, c=1` (module docstring), and `S` is a pure
Courant-number ratio — numerically identical at every `cpl`. `alpha` is the
discretized form of `sigma_phys·dt/(2ε)`; since `dt = S·dx/c` and dx shrinks
as `1/cpl` while everything else is held fixed, code-`sigma_e` must satisfy
`sigma_e = sigma_phys·dx/(c·ε₀)` — an implicit factor of `dx`. Consequently
`sigma_e·r_out(cells)` is exactly `dx`-invariant (`= sigma_phys·R_out_phys/
(c·ε₀)`, the shell's true accumulated optical depth up to the fixed 2×/
grading constant), which forces `sigma_e(R) = sigma_e_native/R` for *any*
rescale ratio `R` — not a fact special to `R=1.5`. Checked numerically here,
independent of both the proposal's and my own Phase-2 algebra:

```
native: R_OUT=78,  SIGMA_NATIVE=0.5    -> 2*sigma*r_out = 78.0
R3:     R_OUT=117, SIGMA_R3=1/3        -> 2*sigma*r_out = 78.0
R4:     R_OUT=156, SIGMA_R4=0.25       -> 2*sigma*r_out = 78.0
```

Exact agreement. This confirms `SIGMA_R4_CORRECTED=0.25` is the physically
correct value **algebraically**.

**But algebra is not the same as verifying what the executed run actually
did**, and this is where my own Phase-2 critique fell short — I proposed a
static assert (`2·SIGMA_R4_CORRECTED·R4_R_OUT == 2·SIGMA_NATIVE·R_OUT`) as
the discriminating gate, and Red Team's audit correctly showed it reduces
algebraically to a tautology already implied by the existing `SIGMA_R4_
CORRECTED==0.25` constant-check — it can never fail regardless of whether
the runtime wiring is correct, because it never reads the constructed `Sim`
object. MATERIALS' fix (adopted as the cycle's new mandatory gate 5) is the
one that actually discharges the risk R15 exists to catch. I independently
traced `lab/materials.py::graded_black_shell`'s own smoothstep profile to
confirm gate 5 is a genuine discriminator, not a second disguised
tautology: `_graded_black(d)` returns `sig=0.5·s²` with `s=smoothstep(d)`,
`d=(r_out−rr)/(r_out−r_in)` — so `sim.sigma_e[shell] += sigma_max·sig/0.5 =
sigma_max·s²`, which reaches its maximum (`=sigma_max` exactly) only at
`rr=r_in`, i.e. the shell's *inner* edge, attained on this bench's
axis-aligned lattice at the grid point exactly `PEC_R_R4` cells from center.
`gate5`'s `np.isclose(sim.sigma_e[shell_mask].max(), sigma_max, atol=
1e-9)` is therefore reading a real, non-degenerate feature of the actual
array (`run.py:256-262`, wired inline in `_run_sim_r4_sigma`, before
`sim.run()`), and `results.json::gates.gate5_runtime_sigma_array` reports
`pass_=true, n_article_calls_checked=16` — with the `assert` wired as a
hard `AssertionError` on failure (would have halted the script before
`results.json` was ever written), the mere existence of the file with all
16 checks recorded is itself the empirical proof, not a self-report. I
independently confirmed `nonneg_pass=True` and `xi_pass=True` (§3, below)
the same way — asserted, run-halting checks, not printed claims — across
all 48 calls. **Conclusion: yes, `SIGMA_R4_CORRECTED=0.25` demonstrably
held the shell's accumulated optical depth invariant in the actual executed
run, not merely in the proposal's arithmetic** — confirmed by an
independent re-derivation of the physics (above) AND by an independently-
traced, genuinely discriminating runtime check that this cycle's own
Phase-2/Red Team process correctly forced into existence.

## 2. Is the full-window sign reversal physically self-consistent?

Pulled directly from `results.json`/exp-093's own filed data, not restated
from NOTES.md:

```
cpl=30 (exp-093 item1, 6 interior points):  delta_scene all NEGATIVE
   (-1.17e-4 .. -4.3e-5), classification ENERGY-DOMINANT/NODE-UNRESOLVABLE
cpl=40 (exp-094 rank1b, same 6 angles):     delta_scene all POSITIVE
   (+3.9e-4 .. +4.2e-4), classification CONSISTENT, all floor_pass=True
pg_pc_ratio (p_g/p_c, the absorbed-power channel) at cpl=40:
   1.0029 - 1.0057 (max deviation from unity: 0.57%)
```

This is not merely self-consistent — it is the textbook signature of R14's
own established mechanism operating exactly as that rule predicts, now
applied across a full window rather than one flagged point. `delta_scene`
is a coherent, near-cancelling residual (`G40−C40`, two configurations
differing only in `PAD`, both scattering nearly the same field) — a
subtractive-cancellation quantity by construction, R13/R14's own named
hazard class. `p_abs_w` is a bulk, non-oscillatory absorption/scattering
partition, independently shown flat to <0.1% under every config change on
this channel since exp-087 (T9's `σ_abs/σ_ext≈0.51` anchor). These are two
physically distinct observables built from the same field data — one a
coherent phase/interference difference, one an incoherent power sum — and
R14's own mechanistic account (the oscillatory imprint lives entirely in
the `σ_ext(θ)` config-differential/coherent term, never in the absorption/
scattering partition) predicts exactly this decoupling: the coherent
channel can swing by 100%+ of its own scale while the incoherent channel
stays flat to under 1%, because they are not different measurements of one
underlying quantity but genuinely different projections of the field.
**Nothing here violates energy conservation or any bookkeeping principle**
— a near-null coherent difference reversing sign while total absorbed power
stays constant is not "energy appearing/disappearing," it is the
interference term of two comparable, correctly-conserved field
configurations changing its own local sign, which is compatible with
constant total power by construction (the two channels are different linear
functionals of the same field, not a partition that must individually
track a shared conserved quantity).

## 3. Is a shift of this magnitude dispersion-explicable, or is it a
different mechanism? (Own exp-093 dispersion-integral work, re-applied)

My own seat computed the relevant instrument last cycle (exp-093 item 4):
the 2D isotropic Yee-grid dispersion relation, solved for the differential
phase accumulated over the aperture propagation length (`ℓ=A_HALF_APERTURE`
≈752/1128 cells, the corrected length scale after this cycle's own Phase-2
critique — mine — caught the pre-freeze draft's wrong, much shorter PAD-
round-trip length). That check found accumulated Yee-grid dispersion phase,
mapped onto an equivalent crossing-location shift via the established
period `P*=2.8421°`, underpredicts the OBSERVED `cpl=20→30` crossing shifts
(`≈0.19°–0.38°`) by **32×–95.8×** — REFUTEd, one clean order of magnitude,
even at the most generous available length scale. That result already
establishes smooth numerical dispersion is *not* a sufficient mechanism for
effects an order of magnitude smaller than what this cycle now reports.

This cycle's own finding is not a repeat of that smaller effect — it is
categorically larger. Item 4 measured a *location* shift of a
zero-crossing by a fraction of a degree; this cycle shows the *entire*
sampled interior (all six points, spanning 0.15°) reversed **sign**, with
`|delta_scene|` growing roughly 3–4× in magnitude in the process
(`~1e-4→~4e-4`), not merely relocating. If smooth numerical dispersion at
the correct (aperture) length scale already falls short by 32–96× of
explaining a sub-half-degree relocation, it falls short by at least that
much, and almost certainly more, of explaining a full-amplitude,
full-window sign reversal — the two effects are not the same order of
phenomenon. **This reversal is too large to be dispersion-explained, using
this program's own already-computed dispersion mechanism at its own
correctly-identified length scale.** This is not a new derivation on my
part so much as the direct, load-bearing consequence of last cycle's own
REFUTE, now applied to a bigger fact than the one it was built to explain —
worth stating explicitly since neither `phase1_proposal.md` nor `NOTES.md`
draws this connection directly (NOTES.md's Next §3 flags that R15 "shows
the instability was even sharper than the rule anticipated" but does not
connect this back to item 4's own quantitative dispersion-insufficiency
finding).

**Is a node moving by more than half its own window's width physically
plausible at these length scales, then, via *some* mechanism?** Yes — and
the leading candidate, already on record and not superseded by anything
here, is curved-boundary staircasing (MATERIALS' T10 account, explicitly
named in exp-093 item 4's own conclusion as "the better-supported
qualitative account"), not free-space dispersion. `graded_black_shell`'s
inner/outer radii are irrational-in-cells curved boundaries re-discretized
on a Cartesian Yee grid at two different pixel pitches (`cpl=30`:
`dx≈0.033λ`; `cpl=40`: `dx≈0.025λ`) — the staircase pattern along the
curved shell boundary is not a small, smoothly-converging perturbation the
way plane-wave dispersion is (`O(dx²)`,·which is exactly why item 4's
predicted shift was tiny); it is a geometry-dependent, discontinuous
re-tiling that can shift a near-field interference null's exact location by
an amount set by the boundary's own local curvature and the residual's own
sensitivity (R13/R14), not by a smooth error-scaling law. Combined with T8's
own standing finding that this bench sits deep in the shadow's near/Fresnel
zone (`z/z_R≈0.04–0.06`), where near-field structure is intrinsically more
sensitive to exact boundary geometry than the far-field asymptote — this is
a physically coherent story for why `delta_scene`'s null could move by more
than half the sampled window's width between two resolutions, provided the
mechanism is boundary staircasing rather than the (already independently
REFUTEd, at zero FDTD cost, one order of magnitude, by my own seat's own
prior work) free-space dispersion mechanism. **NOTES.md's own reading is
correctly scoped and I concur with it**, but the connection to item 4's own
already-quantified insufficiency deserves to be stated as an explicit,
cited cross-reference, not left implicit.

## 4. Reciprocity / passivity / causality bookkeeping — my charter's
mandatory check

- **Passivity.** `graded_black_shell` adds only a non-negative additive
  conductivity (`sigma_max·s²`, `s∈[0,1]`) at every one of the three
  `sigma_max` values exercised this cycle (0.5, 1/3, 0.25) — verified from
  `_graded_black`'s own formula (§1, above), no sign ambiguity possible.
  `alpha=sigma_e·S/(2·eps_r)>0` at every shell cell given `sigma_e≥0,
  eps_r>0`, so `ca=(1-alpha)/(1+alpha)∈(0,1)` throughout — a proper damped,
  never-amplifying leapfrog coefficient. `results.json::nonneg_pass=True`
  is a genuine, run-halting assertion on the measured `sigma_abs` (not
  merely `sigma_max`'s sign), independently confirmed here as checked at
  every one of the 48 calls (`assert nonneg_pass` appears at every one of
  Ranks 2/3/1a/1b in `run.py`, each would have raised before `results.json`
  existed). **No gain, anywhere, in this cycle's construction.**
- **Energy-conservation self-consistency.** `xi_ext` (the extinction-routes
  disagreement, `|sigma_ext_cross−sigma_ext|/|sigma_ext|`, `XI_TOL=0.12`)
  is likewise a genuine, run-halting assertion, independently confirmed
  `results.json::xi_pass=True` across all 48 calls — two independently
  computed extinction cross-sections (cross-section formula vs. direct
  box-flux route) agreeing to within 12% at every point is the bench's
  standing internal check that no spurious energy is being created or lost
  in the measurement pipeline itself, not merely in the material law.
- **Causality.** `eps_r` is real, positive, and non-dispersive within the
  shell (`graded_black_shell` perturbs only `eps_r`'s magnitude toward 1,
  never introduces a frequency-dependent or negative-real-part term); the
  added loss is a standard non-negative conductivity. This is the identical
  material class R1 (RULED OUT) already requires — dominant absorption, not
  a real-index shift — and nothing in `R4`'s construction changes the
  *material law*, only the grid density at which it is discretized. No
  Kramers–Kronig concern arises because no new dispersive term is
  introduced.
- **Reciprocity.** The engine is a standard isotropic, linear,
  time-invariant-per-run Yee update; nothing in this cycle's construction
  (a symmetric radial shell, a purely geometric `PAD` difference between
  configs) introduces a gyrotropic, biased, or time-modulated term that
  could break Lorentz reciprocity. Not independently re-tested this cycle
  (no reciprocity-specific instrument exists on this bench), but nothing
  about `R4`'s mechanical rescale creates a *new* reciprocity risk beyond
  what the already-established `graded_black_shell`/native and `R3`
  families already carry.

**T1 bookkeeping verdict: clean.** Every value of `sigma_max` used this
cycle sits strictly inside the passive, causal, reciprocal class T1's own
central tension already permits for a static, linear absorber; nothing
here is, or could be mistaken for, a T1-escape-route claim (correctly
scored N/A throughout the proposal/NOTES).

## 5. Any genuinely new defect

Nothing that changes a verdict or reopens a gate, but one small, previously
undrawn connection worth recording (§3, above): NOTES.md's Next section
does not explicitly cross-reference exp-093's own item 4 (the
dispersion-insufficiency finding) when discussing this cycle's own
full-window reversal, even though item 4's own quantitative REFUTE is the
single strongest piece of standing evidence *against* reading this as a
smooth numerical-dispersion effect and *for* the boundary-staircasing
account NOTES.md leans on only qualitatively (via MATERIALS' T10
precedent). Not a factual error — everything stated is correct — but a
missed opportunity to make an already-available, already-quantified,
zero-additional-cost argument explicit. Non-blocking; recommend folding
into whichever future cycle re-visits this window's convergence status
(NOTES.md's own Next #1).

## Verdict: **CONCUR-WITH-GAP(S)**

The `SIGMA_R4_CORRECTED` invariant is independently re-derivable from
`fdtd2d.py`'s own E-update coefficient and is confirmed, by a genuinely
discriminating runtime gate (not the tautological static assert I myself
proposed at Phase 2 — Red Team's correction there was right, and I confirm
it a second, independent way here by tracing the smoothstep profile gate 5
actually reads), to have held in the *executed* run, not merely on paper.
The full-window sign reversal is physically self-consistent with R14's own
established mechanism (coherent-channel/incoherent-channel decoupling) and
is, by my own seat's own prior quantitative work, too large to be
explained by smooth Yee-grid numerical dispersion — consistent with, and
reinforcing, NOTES.md's own qualitative lean toward a boundary-staircasing
account rather than a bug or an artifact of the measurement chain.
Reciprocity/passivity/causality bookkeeping is clean throughout, confirmed
against genuine run-halting assertions on the constructed objects, not
printed claims. The one gap: the dispersion-insufficiency cross-reference
above should be made explicit in the permanent record, and — unchanged
from NOTES.md's own honest scoping — a two-point (`cpl=30`/`cpl=40`)
comparison cannot yet distinguish a genuinely converging sequence from an
oscillating or non-convergent one; nothing in this review should be read
as resolving that open question.

## Ranked top candidate next step

1. **A `cpl=50` (or higher) check at the same six interior angles**
   (NOTES.md's own Next #1) — the single test that actually distinguishes
   convergence from oscillation from non-convergence in this window, and
   the natural next point on the same `R3`/`R4`-style congruent-geometry
   family this cycle just built (mechanically extending `RATIO=2.5`, zero
   new design freedom, matching this cycle's own precedent for how a new
   ratio is added). This is EM's own top pick specifically because it is
   the only currently-available test that could turn this cycle's own
   dispersion-insufficiency argument (§3) from "the effect is too large for
   dispersion alone" into "and here is what it actually converges to."
2. Extend the Yee-grid dispersion-integral cross-reference explicitly to
   this cycle's own reversal magnitude (zero-FDTD, a few lines of
   arithmetic reusing exp-093's own committed desk script) — cheap,
   closes the gap named in §5.
3. 38.4°'s flip (Rank 3) deserves the dedicated follow-up NOTES.md's own
   Next #2 already names — not this seat's own top pick, but I concur it
   is a real, comparably-sized open question on the same channel.
