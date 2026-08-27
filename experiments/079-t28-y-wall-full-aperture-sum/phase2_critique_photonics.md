# PHASE 2 — CRITIQUE (PHOTONICS, blind) · Panel Iteration 56 · exp-079

*Fresh sub-agent, PHOTONICS charter (PANEL.md seat 1: surface interaction,
absorption spectra, angular dependence, scattering cross-sections — owns
whether the proposal's optical response is coherent as stated, across
wavelength and angle). Blind to other seats' Phase-2 critiques. Grounded on
PANEL.md, AGENTS.md, LOGBOOK.md (RULED OUT R1–R9; ESTABLISHED; LIVE THREADS
in full, T28's Iteration 46–55 history including the T21/T27 predecessor
threads), `experiments/078-.../` in full (`phase1_proposal.md`,
`phase5_redteam_audit.md` §2/§7 esp., `phase5_review_photonics.md`), this
cycle's `phase1_proposal.md`/`y_wall_aperture_sum.py`/`_results.json`/
`_output.txt`, and the reused machinery (`boundary_reflectance.py`,
`design_geometry.py` exp-065/exp-048, `run.py` exp-069, `lab/fdtd2d.py::
Sim.add_line_source`).*

---

## 1. Steel-man

The mechanistic claim is not an ad hoc rationalization — it is the standard
edge-diffraction result applied honestly. Every config's aperture spans
`[OBJ_Y−A, OBJ_Y+A]` with `A=752` bit-identical across the whole congruent
series, and the model's *only* `theta_beam`-dependent term is the identical
driven-phase ramp `k·sinθ·(y_s−OBJ_Y)` that produces T21's own real fringe
in the direct field. A coherent sum of a smooth envelope over that same
aperture width is expected, on ordinary slit-diffraction grounds, to be
edge-dominated near T21's own period regardless of envelope detail — not a
coincidence needing R5 scrutiny in the way a dense named-constant search
would. The construction itself is honest work: the vectorized `r(θ)` is
gated against the scalar function before use, the gates are re-run at the
genuinely new `[4.77°,15.50°]` envelope rather than reused from a narrower
one, and the convergence check (1x→2x→4x, <0.002% residual) is real, not
cosmetic.

## 2. Sharpest attack

**The "merely a slowly-varying envelope, no sidebands" claim (§5.3/§7) is
asserted, not tested.** `R²=0.97–0.98`, not `≈1.0`, means 2–3% of every
curve's variance is *not* single-tone T21 content, and the write-up never
inspects what that residual actually is. I did (§3 below): subtracting
`PAIR_PAD`'s own fitted `1.9925°` tone and free-period-searching the
residual over `[1°,15°]` finds a genuine secondary component at `2.55°`
(`R²=0.60`, `ss_tot` ≈2.8% of the primary fit's own `ss_tot`) — materially
closer to T28's own `C80−C40` real period (`2.8421°`, 10% away) than to
T21's (`1.9608°`, 30% away) or to noise. This is a real, un-dismissed
sideband, not the clean "no independent frequency" picture §7's prose
claims. It is far too small in absolute terms to explain T28's actual
signal (the full model's own `ss_tot` is already `9.4×10⁻⁷` of real-data
scale, so a 2.8%-of-that residual is `~2.6×10⁻⁸`), which is why it does not
threaten the bottom line — but the mechanistic narrative overstates what a
single-sinusoid fit alone actually established.

## 3. Independent verification performed (RECOMPUTE, not restatement)

**(a) Re-ran `y_wall_aperture_sum.py` end to end.** Bit-identical to the
committed JSON at every printed number (`C80−C40 rel_dev=0.2857 SUPPORT`;
`PAIR_PAD rel_dev=0.5679`/`PAIR_ABSORB40 rel_dev=0.5157` both
INCONCLUSIVE; `ss_tot` ratio `9.392×10⁻⁷`; convergence `2.431×10⁻⁴`→
`1.496×10⁻⁵`). No discrepancy.

**(b) Verified `aperture_amplitude()` against a LIVE `Sim.add_line_source`
call, not merely the code-reading the write-up's Idealization 8 discloses
as untested.** Built a real `Sim` at `C40`'s geometry, called
`add_line_source(src_x, y_lo=40, y_hi=1544, angle_deg=0, edge=40)`, and
diffed `sim.sources[0]["profile"]` against `aperture_amplitude(np.arange(40,
1544), C40)`: **max abs diff = 0.0, exact.** Idealization 8's disclosed gap
is closed favorably — a genuine strengthening the document did not itself
run.

**(c) Swept `br.reflection_coefficient` densely (400 points) over
`[4.5°,15.6°]`, wider than the write-up's own gate battery, for all four
`ABSORB` depths — checking for exactly the branch-cut/non-monotonicity risk
the task named.** `ABSORB∈{60,70,80}`: strictly monotonic, zero local
extrema. `ABSORB=40`: **one** broad, shallow minimum near `θ≈12.15°`
(`|r|`: `1.16×10⁻⁴→8.77×10⁻⁵→1.16×10⁻⁴`, a smooth single dip over ~11°, not
an oscillatory ripple) — consistent with the "slowly-varying" framing for
`|r|` specifically, and I found no `|r|>1` excursion or phase discontinuity
anywhere in the range beyond ordinary `±360°` wrapping. This part of the
claim holds up under a harder check than the write-up itself ran.

**(d) Residual-decomposition check (the gap named in §2).** Recomputed
`PAIR_PAD`'s model curve independently, fit the single dominant sinusoid at
its own reported best period (`1.9925°`), subtracted it, and free-period-
searched the residual: secondary period `2.5506°`, `R²=0.6042` — not the
featureless noise the "envelope, not an independent frequency" framing
implies, and notably *not* a match to `PAIR_PAD`'s own real target either
(`4.6113°`; residual forced to that period gives `R²=0.057`, clean REFUTE
of that specific concern). Net: the residual has *some* structure, it
leans toward T28's shorter-period member rather than its actual target, and
it is two orders of magnitude too small in absolute `ss_tot` to matter
physically — a real finding the write-up should have made itself, not one
that overturns its conclusion.

**(e) `theta_local` convention.** Independently re-derived `θ_local(y_s) =
atan(D_SP/(OBJ_Y+y_s))` from the same image-source geometry
(`Δx=D_SP`, `Δy=OBJ_Y+y_s`) and confirmed it is `theta_beam`-independent by
construction and matches exp-078 Phase-5's own table exactly at `y_s=y_lo`
(`15.0043°/14.3450°/14.0362°/13.7402°`). No angle-frame defect of the kind
that hit exp-078's as-filed and once-corrected models recurs here.

## 4. Verdict: **support-with-changes**

The construction is the correct next test the reconciled Iteration-56
ranking called for, its gates and convergence checks are genuine (I
re-ran/extended several myself), and its headline finding — the flat
single-edge result does not generalize, but the recovered oscillation is
T21-tied rather than a new T28-matching frequency — is well-supported for
the *dominant* spectral content and is argued with real (not asserted)
physics. But the specific mechanistic sentence in §5.3/§7 ("the y-wall
geometry contributes only a slowly-varying envelope, not an independent new
frequency") is not fully earned by what was computed: no residual/secondary-
harmonic check was run, and when I ran one, it surfaced genuine (if tiny
and off-target) sideband structure the prose denies exists at all. This is
a real, my-seat-relevant gap — angular/spectral coherence claimed but not
checked at the resolution the claim itself makes — not a defect that should
block the cycle's own bottom line (§5.2's negative-generalization finding
and §5.3's T21-proximity finding both independently reproduce).

## 5. Single change that would flip my verdict to plain `support`

Add, as a mandatory same-cycle check (not deferred to Iteration 57): for
each of the three scored `PAIR_*`/`C80−C40` model curves, subtract the
fitted dominant sinusoid and free-period-search the residual over the full
`[1°,15°]` window, reporting whether any residual period lands inside T28's
own established band (`2.84°–4.61°`) at an `R²` comparable to the primary
fit's own `0.97–0.98` (not my own quick spot-check's weak `0.60` on one
curve alone). If every residual comes back near-featureless or, like mine,
weakly structured but off-target and two-orders-of-magnitude sub-dominant,
the "slowly-varying envelope, no independent frequency" sentence is earned
and I would move to plain `support`. If any residual instead shows a
strong, T28-matching secondary tone, the mechanistic narrative in §7 needs
withdrawing even though the magnitude argument would likely still carry the
same bottom-line verdict.
