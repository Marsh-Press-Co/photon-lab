# PHASE 5 — REVIEW · Panel Iteration 48 · exp-071
## THERMODYNAMICS (seat 4, blind, fresh context)

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md seat 4): where absorbed
energy goes; always asks what re-radiates and whether it would be
detectable; owns the per-proposal energy sidecar (absorbed power →
temperature rise → emission band → detectability), a post-run analytic
calculation, labeled as such. No memory of this cycle's own Phase-2
critique (a different fresh instance of this seat wrote it) — read
everything fresh: `PANEL.md`, LOGBOOK.md's T28 thread + Iterations 46/47
in full, and the complete exp-071 record (`phase1_proposal.md`, all five
`phase2_critique_*.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `phase4_results.md`, `results.json`, `design_geometry.py`,
`run.py`). Independently re-derived every number below from `results.json`
and `run.py`, not taken on any document's word.

## 1. Does the sidecar apply here at all? (checked hard, again)

No. Independently re-confirmed my own seat's Phase-2 finding (Iteration 48
Phase 2, a different fresh instance): `ABSORB` is
`lab/fdtd2d.py::Sim._damping`'s own domain-truncation boundary depth (cubic
ramp, `exp(-0.30·d)`, applied to all four box edges), not a witness-scene
material. No absorbing article (Block ARTICLE, the `T5_THERMAL_CAVEAT`
carrier) is re-run this cycle — idealizations 4/8 confirm `C_empty`-only
readings — and all four congruent configs are near-total absorbers at
their boundary *by construction*, regardless of `ABSORB` depth, since that
is what "congruent" means in this series (`A`/clearances/`D_SP` held
fixed). There is no absorbed-power trend for a sidecar to characterize and
no physical material for anything to re-radiate from. Confirmed independent
of the proposal's own say-so and independent of my seat's own earlier
Phase-2 write-up.

## 2. Was the fix from my own Phase-2 critique actually applied?

**Yes, and correctly reasoned — but the code wiring is more fragile than
the documentation claims.**

`phase3_synthesis.md` (finding 4) records the fix as ACCEPTED: `THERMO_SCOPE_CAVEAT`
added, "printed unconditionally alongside every Combined Verdict." I traced
this in `run.py` rather than trusting the synthesis doc:

- The caveat text (lines 74–81) is correct and matches my seat's own
  Phase-2 language closely — genuinely re-derived reasoning, not a rubber
  stamp: no article run, near-total absorption by construction, no
  re-radiation channel.
- It **is** printed unconditionally, once, as part of `FROZEN_PREDICTIONS`
  (lines 154–157), at the top of every run's stdout, before any FDTD call —
  this satisfies the pre-registration/disclosure requirement.
- It is **always** present in `results.json["caveats"]["thermo_scope"]`
  regardless of outcome (line 576) — confirmed directly in the committed
  `results.json`.
- **But inside `main()`'s three-branch Combined-Verdict logic (lines
  515–546), the caveat is stitched into `combined_reason` — the string
  actually printed next to `"COMBINED VERDICT: {combined}"` at the end of
  the run (lines 610–611) — only in the `NEITHER` branch (line 546).** The
  `CONFIRMED` branch (line 517–521) appends `ABSORB_NOT_MATERIAL_CAVEAT`
  only; the `REFUTED` branch (lines 522–528) appends **no caveat text at
  all**. `NOTES.md` states the caveats are "disclosed unconditionally,
  printed with every result regardless of outcome" — true of the
  pre-run `FROZEN_PREDICTIONS` block and the JSON sidecar field, **not**
  true of the tail-of-run Combined Verdict announcement itself for two of
  its three possible branches.

This cycle's actual `combined_verdict` is `NEITHER` (confirmed directly
from `results.json`), so the caveat *did* appear attached to this run's own
printed verdict — the check my mandate asked me to perform passes **for
this specific outcome**, by construction of which branch fired, not because
the code guarantees it in general. Had P-071-2 landed CONFIRMED or REFUTED
instead (a live possibility going into Phase 4 — nothing in the design
determines the branch in advance), a reader grepping only the tail
`"COMBINED VERDICT"` line — the natural thing to cite in a future LOGBOOK
entry — would get the `ABSORB_NOT_MATERIAL_CAVEAT` or nothing, never the
THERMO caveat, at the exact place a future citation is most likely to be
lifted from. **Recommend for the next touch of this file (cheap, desk-only,
zero FDTD cost): append all three caveats uniformly to `combined_reason`
in every branch, not conditionally** — this is the same class of gap this
program's own R4/verify-before-claim discipline exists to catch, caught
here before any LOGBOOK entry is drafted from it.

## 3. Block SETTLE-C60C70 — does anything belong in my lane?

The instruction I was given asks specifically whether the settling result
carries a thermodynamic/energy-relaxation observation EM's own lane
wouldn't surface. Two things, checked directly against `results.json`, not
`phase4_results.md`'s summary:

**(a) The settling-shift magnitude itself has a physically sensible, if
weak and unscored, sign.** The four `SETTLE-C60C70` cells
(`results.json["settle_c60c70"]["scored"]["cells"]`):

| config | θ | \|ΔC(4200−2800)\| |
|---|---|---|
| C60 | 37.2° | 2.489×10⁻⁷ |
| C70 | 37.2° | 1.513×10⁻⁷ |
| C60 | 41.4° | 4.333×10⁻⁸ |
| C70 | 41.4° | 4.032×10⁻⁸ |

At **both** peak angles, the residual (unsettled) transient shrinks going
from `ABSORB=60` to `ABSORB=70`. That is the physically expected direction
for a graded-loss boundary: a deeper absorbing ramp should present lower
residual reflectance to a wave reaching it, so whatever hasn't fully
decayed by STEPS=2800 should be smaller for a deeper boundary — an
energy-relaxation-rate argument, not an EM impedance-matching one per se.
This is only a two-point, same-sign-at-both-angles observation (weak; the
design never scores it as a trend, only a pass/fail against `GATE_HARD`,
correctly, since that's all it was built for) — I flag it as supportive
context for the physical plausibility of "deeper ABSORB → lower residual
reflectivity," not as new evidence on its own.

**(b) A much stronger, load-bearing observation the record never states —
this is my sharpest finding this cycle.** The dense-sweep `C_empty(θ)`
peak-to-peak amplitude, computed directly from already-collected data
(`results.json["dense_causal"]["rows"]` for C60/C70; exp-069's own
committed `block_dense` for C40/C80 — **zero new FDTD calls, all four
values already sitting in git**):

| config | ABSORB | ptp(C_empty) over 36–42° |
|---|---|---|
| C40 | 40 | 0.016486 |
| C60 | 60 | 0.019429 |
| C70 | 70 | 0.019955 |
| C80 | 80 | 0.020083 |

This rises **monotonically** with `ABSORB` depth, linear-fit `R²=0.886`,
+21.8% from C40 to C80, with the gain front-loaded (+17.9% from C40→C60,
only +3.4% combined for C60→C70→C80 — a saturating shape, the kind a
residual-reflectance-vs-thickness relationship plausibly produces). This is
an *amplitude* trend, not a *period* trend — and critically, **it is not
subject to the Rayleigh/Fourier resolution floor that sank P-071-2**
(that floor bounds how finely two close *periods* can be told apart inside
a fixed angular window; a peak-to-peak amplitude is a single scalar per
config, with no frequency-resolution requirement at all). Where the
period-based headline test was floor-limited at 9.5% of the resolving
power it needed, this amplitude comparison is a clean, resolution-floor-free
readout of the same underlying `C_empty(θ)` data, and it shows a *larger*,
more monotonic, better-fit trend (21.8%, R²=0.886) than the period trend
did (3.9%, floor-limited).

**The one honest confound, and why this is a proposal for next steps, not
a finding to add to this cycle's verdict:** in exp-065's own congruent
series, `PAD` also climbs with `ABSORB` (0/20/30/40 for
40/60/70/80) — only `A` is held fixed by the congruence assertion,
not `PAD`/`NX`/`NY`. So this amplitude trend could be `ABSORB`-tied
(more absorbed → more back-reflected energy re-entering the fringe pattern,
counter-intuitively, or some other boundary-depth effect on the standing-wave
envelope) or `PAD`-tied (a bigger box changes near-field path lengths to
the observation cell), or both, entangled by construction. Nothing in this
cycle's design (nor any prior cycle's) isolates the two, and this is a
genuinely new axis — not previously scored anywhere in the T28 thread — not
a repackaging of P-071-2.

## 4. Proposed next step for T28 (concrete, falsifiable, cheap)

**A matched-PAD amplitude probe**, decoupled from the angular-resolution
floor that limited this cycle's own headline test:

- Reuse `design_geometry.py`'s existing congruent construction machinery.
  Build two new configs holding `PAD` **fixed** while `ABSORB` varies (e.g.
  `PAD=40` fixed, `ABSORB∈{40,80}` — a config pair that does not exist in
  the current `C40..C80` series, where `PAD` and `ABSORB` climb together)
  and run the identical 31-point/0.2°-step dense sweep already validated by
  this cycle's own `Block DENSE-CAUSAL` machinery.
- **Prediction, falsifiable, stated before any run:** if `ptp(C_empty)`
  still rises substantially (≥10%, this cycle's own weaker C60→C70 step
  size, as a floor) between the two `ABSORB` values at fixed `PAD`, that is
  evidence the amplitude trend found in §3(b) is genuinely `ABSORB`-tied
  (boundary-depth/reflectivity), not a `PAD`/box-size artifact — a real,
  new, resolution-floor-free discriminator for T28, complementary to (not
  competing with) EM's own wider-angular-window or beat-frequency proposal
  already queued in `NOTES.md`. If the trend collapses (≤3%, near this
  cycle's own C70→C80 step) at fixed `PAD`, that is evidence the amplitude
  effect is `PAD`/geometry-tied instead, narrowing where T28's own
  mechanism search should look next.
- Cost: 2 new configs × 31 angles × 1 λ = 62 new calls at native
  resolution (comparable to this cycle's own `Block DENSE-CAUSAL`), zero
  new `lab/` diff, reusing every piece of already-validated machinery.
- **Explicitly not my lane to adjudicate further**: whatever this probe
  finds bears on EM's reflectivity/geometry question and PHOTONICS' λ-scope
  question, not on re-radiation/detectability — my seat's role here ends at
  flagging the resolution-floor-free discriminator and its confound; the
  interpretation belongs to EM/PHOTONICS/Red Team once run.

Secondary, much cheaper: fix the `combined_reason` caveat-wiring asymmetry
found in §2 (append all three caveats uniformly across all three Combined
Verdict branches) — zero FDTD cost, text/code only, before this cycle's
NEITHER-branch text is relied on as a template for a future CONFIRMED or
REFUTED cycle.

## 5. Rating

**PARTIAL.** Consistent with the cycle's own Combined Verdict (`NEITHER`)
and with Iterations 46/47's own pattern: T28's causal question is narrowed,
not answered, and my own lane's duty (the energy sidecar) correctly found
nothing to attach this cycle — confirmed independently, not by deferring to
the proposal or to my own earlier Phase-2 self. Not RULED-OUT (T1 route N/A
throughout, no mechanism class bounded, nothing here forecloses anything).
Not PROMISING (constraint-3 ledger gained zero ground, by design). The one
substantive contribution from this seat is new: an unremarked,
resolution-floor-free amplitude trend in already-collected data that offers
a genuinely different next-step discriminator than the angular free-period
approach the record has now run twice (exp-069, exp-071) into the same
Rayleigh-floor wall.

## Summary for the Director

- THERMO sidecar: correctly inapplicable, correctly reasoned, confirmed
  independently for the second fresh-context pass in a row.
- THERMO_SCOPE_CAVEAT: present and correctly worded in the final artifacts;
  it did appear attached to this cycle's own printed Combined Verdict
  because the verdict happened to land NEITHER — but the wiring in
  `run.py` only attaches it in that one branch, not CONFIRMED or REFUTED.
  Flagged as a cheap fix, not a defect that affected this cycle's actual
  result.
- New finding: `C_empty(θ)` peak-to-peak amplitude rises monotonically with
  `ABSORB` depth (R²=0.886, +21.8% C40→C80) in data already on disk, a
  trend not subject to the Rayleigh resolution floor that limited this
  cycle's own headline period test — but confounded with `PAD`, which
  climbs alongside `ABSORB` in the existing congruent series. Proposed a
  concrete, falsifiable, ~62-call matched-PAD follow-up to decouple them.
