# PHASE 2 — CRITIQUE (ELECTROMAGNETISM, blind) · Panel Iteration 56 · exp-079

*Fresh sub-agent, ELECTROMAGNETISM charter: field/wave behavior, impedance
matching, energy coupling; owns reciprocity/passivity/causality bookkeeping —
formalizes what T1 permits and forbids. Blind to other seats' Phase-2
critiques this cycle. Grounded on PANEL.md, AGENTS.md, LOGBOOK.md (RULED OUT
R1–R9, T28's full Iteration 46–55 history, my own prior-cycle finding at
exp-078 Phase 5), the complete exp-078 record (`phase1_proposal.md`,
`y_wall_prescreen.py`, `phase5_redteam_audit.md` §2/§3/§7), this cycle's
`phase1_proposal.md`/`y_wall_aperture_sum.py`/`_results.json`/`_output.txt`,
`experiments/075-.../boundary_reflectance.py`,
`experiments/065-.../design_geometry.py`, and `lab/fdtd2d.py::
Sim.add_line_source`.*

---

## 1. Steel-man

The per-point generalization is the right move, done rigorously, not
guessed. `theta_local(y_s)=atan(D_SP/(OBJ_Y+y_s))` is not y_lo-specific in
its own derivation — mirroring *any* aperture point through the shared
`y=0` wall gives an image at `(SRC_X,-y_s)`, and the straight
image-to-observer line's angle to the wall normal is a pure function of
that point's own `(Δx,Δy)=(D_SP,OBJ_Y+y_s)`, independent of which point is
chosen. I re-derived this from scratch and it holds cleanly at every
`y_s∈[y_lo,y_hi]`, including the ~5° far-edge envelope no prior gate had
sampled — nothing "breaks" geometrically. Re-gating `reflection_coefficient`
fresh at the new `[4.77°,15.50°]` envelope (not reusing exp-078's narrower
one) and validating the vectorized `r()` bit-exact before trusting it at
~7,500 calls is exactly the discipline this program requires before a
number is used.

## 2. Sharpest attack

**The coherent sum can never recover a genuinely T28-shaped period,
independent of whether a real wall echo exists — a structural property of
§3.4's construction, not an empirical finding about the wall.** Both
`r(theta_local(y_s))` and `dist_image(y_s)` are, by this document's own
derivation, pure functions of *static* geometry, zero `theta_beam`
dependence anywhere. The *only* `theta_beam`-dependent ingredient in
`E_echo` is `phase(y_s;theta_beam)=k·sinθ_beam·(y_s−OBJ_Y)` — the identical
driven-phase ramp, identical `[y_lo,y_hi]`/`TAPER=40` window, that already
produces T21's own fringe in the *direct* field. A coherent sum of
`exp(i·k·sinθ_beam·(y_s−OBJ_Y))` over a fixed-edge window times *any*
slowly-varying envelope is edge-dominated at essentially T21's own period,
by the identical stationary-phase logic LOGBOOK's own T28-opening argument
already uses ("two sinusoids sharing one frequency..."). §5.3's finding —
1.6–3.5% from T21, not T28 — was close to guaranteed once `theta_local`
was fixed `theta_beam`-independent, for *any* envelope, real or wrong.
§7's "closer to informal REFUTE than INCONCLUSIVE" over-reads what a
structurally-foreclosed test licenses.

## 3. Independently computed check

Rebuilt `theta_local`/`echo_field_curve` from scratch (not imported) in
`/tmp/.../scratchpad/em_check.py`, this session — two checks:

**(a) Headline angle, recomputed from raw geometry, no exp-079 imports:**
`theta_local(y_lo)` for C40 from `atan(223/(792+40))` = **15.0043°**,
matching the proposal's own table to the printed digit.

**(b) Sensitivity to the missing 2D cylindrical-wave amplitude falloff.**
`dE(y_s)=amp(y_s)·r(...)·exp(i[...])` has no `1/√dist_image(y_s)` factor —
unlike this program's own already-established, hard-won Huygens-Fresnel
convention for exactly this kind of many-point coherent sum
(`experiments/048-evidentiary-chord-closure/design_geometry.py::
field_and_h`, `G0=exp(i(kr−π/4))/√r`, the subject of a dedicated
magnitude-bridge correction, Iteration 19/exp-042). `dist_image(y_s)` spans
~861→~2347 cells (C40, near→far edge) — a 2.7× range, `1/√r` a ~1.65×
weighting swing. I re-ran the full pipeline with the falloff (and its
`−π/4` phase) added:

| quantity | as-built (no falloff) | with `1/√dist_image` (established convention) |
|---|---|---|
| `ss_tot(model PAIR_PAD)/ss_tot(real)` | `9.392e-07` | `1.248e-09` (**−753×**) |
| `PAIR_PAD` P* | `1.9925°` | `2.0075°` |
| `PAIR_ABSORB40` P* | `2.0226°` | `2.0150°` |
| `C80−C40` P* | `2.0301°` | `2.0226°` |

**Result: the period-based Test-A verdicts are essentially unaffected**
(all shifts <1%, confirming §5.3's own mechanistic reading — the recovered
frequency is set by the shared edge/taper window, not by the envelope) —
this is a genuine reassurance for the specific numbers scored in §5.3/§7,
found by checking rather than assuming it. **But the reported "nine orders
of magnitude above exp-078's floor" `ss_tot` figure (§5.2, the document's
own headline evidence that "this is real, resolvable, non-degenerate
signal") is itself convention-dependent by ~3 orders of magnitude** — a
missing, undisclosed idealization (absent from all 8 items in §6), on a
statistic this document leans on as decisive. It does not flip
`ss_tot_degenerate` (still `False` either way, `1.25e-9 ≫ 1e-20`), so
Branch (a) ("edge-domination generalizes, flat result survives") still
correctly REFUTEs — but the specific "9 orders of magnitude" framing should
not be read as a precise, convention-free number.

## 4. Verdict: **support-with-changes**

Sound zero-FDTD method, a real methodological advance over exp-078 (every
aperture point now gets its own rigorously-derived angle, not one shared
constant), the vectorized `r()` is validated before use, gates are honestly
re-run at a genuinely new envelope, the convergence check is real and
correctly interpreted, and the two-proxy (`Re`/`|·|`) reporting is not
cherry-picked. But §7's interpretive framing outruns what §3.4's own
construction can support: because `theta_local`/`dist_image` are
`theta_beam`-independent by design, this specific test could not, in
principle, have distinguished "a real wall echo whose period happens to
differ from T21's" from "no wall echo at all" — both would look identical
under this construction. That distinction belongs in the document as a
disclosed limitation (idealization 9), not folded into a "closer to REFUTE"
verdict on the underlying mechanism class. The missing `1/√r` falloff
(idealization 10) should also be disclosed, even though I found it
non-load-bearing for the period numbers actually scored.

## 5. Single change that would flip my verdict to plain `support`

Add Idealization 9, stating explicitly that this construction's
`theta_beam`-dependence is structurally confined to the driven-phase ramp
shared with the direct field, so a T21-proximate period is close to
guaranteed by design regardless of the true wall-reflectance physics — and
soften §7's "closer to a genuine (informal) REFUTE... than to an
INCONCLUSIVE" to state plainly that this pre-screen cannot discriminate a
real-but-T21-frequency-locked echo from no echo at all. With that
correction in place (no new computation required — it is a disclosure
fix, not a numerical one), I would move to plain `support`.
