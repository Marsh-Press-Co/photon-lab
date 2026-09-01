# Phase 5 Review — PHOTONICS (Panel Iteration 77, exp-100)

## Verdict: CONCUR-WITH-GAPS

The cycle's own reported outcomes — Tier 1 AMBIGUOUS (pooled/family-stratified
contradiction, honestly routed per the pre-registered Idealization 70 branch,
not massaged), Leg A PASS (disclosed as a static-contrast bound only), Leg B
constraint-2 PASS, Leg B constraint-1 UNINTERPRETABLE (a self-diagnosed
instrument defect) — are each independently reproducible from `results.json`
and physically coherent once traced to source. I found no arithmetic or
optical-response error anywhere in the filed Result section. The gaps named
below are about where the cycle's own disclosure is thinner than the
underlying physics warrants for constraint 3 specifically, and about
prioritization for Iteration 78 — not about anything wrong in what was
filed.

## 1. Is the beam_behind_t28 lateral-shift diagnosis physically sound?

**Yes — and it survives an independent, from-scratch quantitative check, not
just a plausibility read.**

The claimed walk, `Δy = (R_OUT+10)·tan(θ)` with `R_OUT=156` (R4_R_OUT,
confirmed at `experiments/069-.../design_geometry.py:257`) and standoff 10
cells (`PLANE_OBS_STANDOFF_CELLS`, `run.py:431`), traces directly to
`lab/fdtd2d.py`'s own documented source convention ("the −x-going wave then
travels along (−cosθ, +sinθ)", `fdtd2d.py:138-139`) — a completely
mundane, textbook consequence of measuring an obliquely-incident beam's
shadow on a fixed downstream plane rather than a normal-incidence one. I
recomputed `Δy` independently from these primitives for all six angles
rather than trusting NOTES.md's own arithmetic (R4 discipline):

| θ (deg) | Δy = 166·tan(θ) (cells) |
|---|---|
| 37.127246 | 125.669 |
| 38.590230 | 132.470 |
| 40.265420 | 140.606 |
| 40.960901 | 144.103 |
| 41.460901 | 146.663 |
| 42.960901 | 154.586 |

This reproduces NOTES.md's cited 125.7–154.6 cells exactly. Against the
window's own fixed half-width of 160 cells (`BEAM_BEHIND_HALF_WIDTH =
REF_HALF_H_R4 = 160`), the true shadow center sits within 5.4–34.3 cells of
the window's own edge at every one of the six tested angles — precisely the
regime where a fixed, `obj_y`-centered window stops sampling the object's
own shadow and starts sampling adjacent, largely unshadowed beam.

I went one step further than NOTES.md's own diagnosis and checked whether
this mismatch **quantitatively** explains the specific 0.42–0.46 readings,
not merely their general largeness. A crude top-hat model — full shadow
footprint `[Δy−R_OUT, Δy+R_OUT]` (width 312, using the established
near-total-absorption reading ≈1.7% transmission inside it) overlapped
against the fixed window `[−160,+160]` (≈100% transmission outside the
shadow) — predicts a window-averaged "transmission" of ≈0.42 at θ=37.13°
rising to ≈0.50 at θ=42.96° (overlap fraction falling from ≈0.60 to ≈0.50
as the shadow walks off-window). The actual filed readings are 0.4156 rising
to 0.4589, **monotonically increasing with θ exactly as this toy model
predicts**, and within the crudeness expected of a top-hat approximation
(no taper profile, no diffraction spreading over the 166-cell propagation
gap, no graded-absorption radial profile). This is a strong, independent
corroboration that the reading is fully accounted for by the geometric
window/shadow mismatch — there is no residual anomaly here calling for a
new physical mechanism, and NOTES.md's UNINTERPRETABLE-PENDING-CORRECTION
disposition (not silently reporting 0.42–0.46 as a constraint-1 finding) is
the scientifically correct call, not merely a cautious one.

Two points worth adding to the record for Iteration 78, beyond what
NOTES.md already states:

- **`observer_record_t28` is correctly exempted from this defect for a
  verifiable, not merely asserted, reason.** I read `lab/emit.py`'s
  `observer_record` directly (lines 80–127): it FFTs the *entire* interior
  window (`sim.absorb+8` to `sim.ny-sim.absorb-8`, effectively the whole
  domain, not a narrow object-centered strip) and reports plane-wave
  power totals — a construction with no spatial window to mis-center in
  the first place. The constraint-2 PASS does not share constraint-1's
  disease.
- **The Next section's own preferred fix (a closed-box Poynting
  extraction, matching `cell_metrics_r4`) is the physically correct choice
  over the alternative it also offers (re-centering the line window at
  `y_center = obj_y + Δy(θ)`).** A re-centered line window still sits 166
  cells downstream of the object, where the beam has had room to spread
  by ordinary diffraction over that propagation distance — a residual,
  angle-dependent broadening the box avoids entirely by measuring flux on
  faces drawn tightly around the object itself. I'd state this as a
  reason to prefer the box option outright, not merely as one of two
  equally-good choices.

## 2. Wavelength/angle scope — this needs a sharper flag than NOTES.md gives it

NOTES.md discloses (Idealization 64, and inline in the Result section) that
this cycle is 600nm-only and that "the established T21 750nm/θ=40° fringe —
0.0237, 4.7×C_thr, in this identical window — [is] an unaddressed
same-window contamination-risk precedent, NOT tested this cycle." I raised
this at Phase 2 and Red Team adopted it verbatim (RT ruling, phase2 audit)
— so the disclosure mechanism worked. But I want to sharpen it here, at
Phase 5, rather than let it sit as one idealization among many:

This is not a generic "we only tested one wavelength" hedge. It is a
**specific, already-quantified, on-file number** — a *different*
established oscillatory confound (T21's source-aperture edge-diffraction
fringe, not `delta_scene` itself) that, in the identical 36°–43° angular
band this cycle scores, already reads **4.7× over `C_thr`** at 750nm while
reading comfortably under threshold at 600nm. The witness scenario this
whole program scores against is explicitly white light (LOGBOOK's
ESTABLISHED section: "the witness's flashlight was white light"). A Leg-A
PASS at 600nm — even at only 63% of the lab bar, with real margin — says
nothing about whether the *combined* ambient-contrast picture a real
white-light witness would see in this exact angular window survives, given
a sibling mechanism at a sibling wavelength is already known to fail badly
there. This is not a hypothetical wavelength-generality gap of the kind
this sub-thread names routinely (e.g. the still-deferred 750/450nm `G40`
leg) — it is a specific, quantified, already-measured failure mode sitting
immediately adjacent to this cycle's own PASS. I'd want any future citation
of this cycle's Leg-A PASS to carry that distinction explicitly (a generic
"600nm-only" caveat undersells how concrete the counter-evidence already
is), and I rank testing it directly (§3, below) above where NOTES.md's own
Next section currently places it (folded into the "standing 5–8-cycle-
deferred" backlog bucket, unranked relative to other stale items).

To be precise about scope, since two different signals are in play here:
T21's fringe is a *different instrument* (the bare source-aperture
diffraction pattern, `C_empty(θ)`) than `delta_scene` (the article-present
`C40`/`G40` PAD-difference) — I am not claiming `delta_scene` itself
necessarily scales the same way with λ. The point is narrower and, I think,
still decisive for constraint 3: this angular window already hosts a
known, quantified, threshold-violating oscillation at 750nm from a
mechanism this program has independently confirmed operates on this same
bench — so treating the window as "characterized" on the strength of a
600nm-only `delta_scene` PASS, without at least flagging that the window's
*total* ambient-contrast risk is not bounded by this cycle's own number,
understates the real state of knowledge.

## 3. Ranked top-3 candidates for Iteration 78

1. **Fix `beam_behind_t28` via a closed-box Poynting extraction (not a
   re-centered line window) and re-run the constraint-1 reading at the
   same 6 angles.** Endorses NOTES.md's own Tier-0 item, with the specific
   refinement above (box over re-centering, for the diffraction-spreading
   reason given in §1) made explicit rather than left as an equally-weighted
   alternative. Cheapest, most consequential open item — this cycle's own
   constraint-1 result does not exist yet.
2. **Promote the 750nm (and ideally 450nm) leg of Leg A/B — at minimum the
   two extremal angles (40.960901°, 42.960901°) — from the standing
   backlog to an Iteration-78 priority, specifically because of T21's
   already-quantified 4.7×`C_thr` precedent in the identical window** (§2).
   This is the one item on the board most directly load-bearing to
   constraint 3, and it is currently ranked no higher than several stale,
   generically-deferred items (the full-width `G40` leg, the x-wall refit)
   that carry no comparable quantified risk.
3. **Give the R3-only significant correlation (r=0.486, p=0.0042 vs.
   R4's r=0.110, p=0.525) a targeted physical hypothesis before any
   follow-up spend, not just a statistical replication check.** NOTES.md's
   own Next section already proposes revisiting this; from this seat's
   charter I'd add a concrete question worth answering first, cheaply: R3
   (`cpl=30`, `R3_RATIO`-scaled geometry) and R4 (`cpl=40`) differ in more
   than resolution alone — different absolute `R_OUT`, different
   diffraction-relevant length scales relative to λ. Before spending new
   FDTD on this family split, check whether R3's own geometry sits closer
   to a regime (e.g. a different `N_F`/Fresnel-number band, per this
   sub-thread's own T10/T12 near-field-fringe precedent) that would give a
   genuine photonic reason for family-dependent coupling strength, rather
   than treating "R3-only significant" as pure noise or pure recipe
   artifact by default.

No mechanism-class claim is made or implied by this cycle (T1 correctly
stays N/A/unresolved) — Checkpoint criterion 2 is correctly N/A here, matching
this seat's own reading of the record.
