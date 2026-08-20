# MATERIALS & METAMATERIALS — Phase 5 Review, Panel Iteration 29 (exp-052)

*Fresh-context review, cold on this cycle's execution. Charter: sub-wavelength
structure realizability, tiered published / plausible / unobtainium-with-
parameters. Independently re-derived every headline number below from
`results.json` before trusting the prose in `NOTES.md`/`phase3_synthesis.md`.*

## Reading

Reproduced from `results.json::fit`, not copied from any prose:

| r_out | `C_fixedabs` | `C_selfsim` (re-measured, PEC-cored) |
|---|---|---|
| 78 (anchor) | −0.7208684660449545 | (identical — families coincide by construction) |
| 156 | −0.80668176727563 | −0.7304552322383192 |
| 312 | −0.84031612126995 | −0.7322544463081008 |

`P1_verdict`/`P2_verdict`/`P3_verdict` all read `CONFIRMED` in code (not
hand-asserted). `R_coat = −2.879×10⁻⁷` (P-4, comfortably inside the 0.2%
gate). The core-fill check (P-5, fix 3's substituted instrument) reads
`core_fill_delta_theta0 = −1.13×10⁻⁶` (r=156) and `+1.13×10⁻⁶` (r=312) —
both five orders of magnitude inside the pre-registered ±0.02 band. All five
numbers check out; the headline is real, not a transcription artifact.

Process notes, not disputing the physics: Red Team's Phase-2 audit caught
the single most consequential defect (exp-030's own comparator was hollow-
core, never PEC-cored, at the N9-ambient level — the same defect class
exp-031 fixed for a different diagnostic and never propagated back) before
any run — the kind of catch this program's own R4/T9 history says should be
taken seriously, and it was, cleanly, at Phase 3. One item (QUANTUM's
coherent-vs-incoherent bridge-gate validity at the new 30.8%/15.4%
shell-fraction geometry) was ruled REAL and LOAD-BEARING by Red Team and
explicitly *not* closed — the Director disclosed this rather than smoothing
it over. I inherit that open item below; it bears on how much weight my own
tier call can put on the r=156/312 numbers, not just on EM/QUANTUM's
bookkeeping.

## Physical meaning

Two separate things were true before this cycle and are now three:

1. (Known, Iteration 7) The self-similar construction is the *harder*
   realizability ask — a re-engineered coating recipe at every target size,
   diverging to 0.31–0.92 m thickness at witness scale, no macroscopic
   real-material precedent.
2. (Known, this cycle's own design choice, §3 of `phase1_proposal.md`) The
   fixed-absolute-thickness construction is the more realizable one **by
   design** — literally the same `sigma_max=0.5` constant, same 48-cell
   thickness, reused unmodified across the whole family. This was always
   true by construction, not something this run needed to discover.
3. **(New, this cycle's actual finding)** The same construction that is
   easier to build is *also* optically better at scale: it does not merely
   avoid T14's wrong-direction shallowing, it reverses it — deepening
   0.086 below the r=78 anchor by r=156 and a further 0.034 by r=312,
   while the corrected self-similar comparator stays within 0.0018 of flat
   across the same span. That is not a foregone conclusion the design
   choice guaranteed; PHOTONICS' own Phase-2 critique correctly flagged it
   as a testable, not assumed, direction, and it tested true.

**Why, physically, on my own charter's terms (not re-litigating PHOTONICS'
rim-diffraction framing):** the fixed-absolute family's thickness-to-inner-
radius ratio itself collapses across this bench family — 48/30=1.6 at r=78
(thickness *exceeds* the core radius), 48/108=0.44 at r=156, 48/264=0.18 at
r=312. A coating held at fixed physical thickness on a growing substrate
becomes progressively more consistent with the "locally-planar thin film
on a curved backing" picture that any bulk-absorption coating recipe
(CNT-forest, black chrome, doped-semiconductor stack) is actually designed
and characterized against — real ultra-black coatings are validated as
thin films on gently-curved or flat substrates, not as O(1)-thickness-to-
radius annular shells. The self-similar family never leaves that regime
(thickness/inner-radius is pinned at exactly 30/48=0.625 — wait, held at
the *r=78* value 48/30=1.6 forever, since it scales in lockstep); the
fixed-absolute family exits it as r_out grows. **That the family's own
optical performance improves in exactly the direction its curvature ratio
becomes more coating-like is a second, independent (materials-native, not
diffraction-native) reading of the same result** — worth stating in these
terms because it is falsifiable on its own axis (predicts continued
deepening as thickness/radius keeps shrinking) and gives the finding a
mechanism grounded in what a coating physically is, not only in rim
diffraction.

**The catch, stated directly, per the task's own framing.** None of the
three things the review brief named as risks turn out to be a problem *for
this cycle's own construction* — if anything each cuts the other way:

- **Conductivity uniformity**: not worsened by this result. `sigma_max` is
  literally one global constant, unchanged across the entire r=78→312
  family — the fixed-absolute construction requires *zero* additional
  uniformity discipline as the object grows, unlike the self-similar
  family, which needs `sigma_max` re-tuned (∝1/κ) at every target size.
  This is the realizability case's own core claim, and this cycle measured
  it holding, not merely argued it. What the bench genuinely *cannot* see
  (a real 2D FDTD grid with one exact `sigma_max` has no spatial noise
  term at all) is real-world deposition non-uniformity — CNT-forest growth
  over larger areas is documented to show real height/density variance,
  and this idealization is unexamined here as everywhere else in this
  program's coating claims. Not new to this cycle; worth flagging because
  this cycle is the first one where the coating claim is actually being
  used as a design lead rather than an argued alternative.
- **Fabrication tolerance**: the more interesting, previously-unstated
  point. At `τ_shell=24` the design is deeply saturated (transmission
  ~e⁻²⁴) — a coating built to this target is not sensitive to *average*
  thickness error at all (an extra or missing few nm changes almost
  nothing at this depth). It *is* acutely sensitive to **local pinholes or
  thin spots**: a single sub-thickness patch is not averaged away by a
  bulk-optical-depth argument, since the silhouette-ending function is the
  *minimum* local transmission across the coated surface, not the mean.
  This bench's uniform, defect-free `sigma_max` field cannot see that
  failure mode by construction, and it is the dominant real-world risk for
  any τ≈24-class coating, independent of which geometric family is used.
- **Curvature effects the 2D idealization can't see**: real, but the
  extrapolation gap is large and should be named as a number, not a
  gesture. The bench's own thickness/inner-radius ratio only reaches 0.18
  at r=312 (9.4µm) — a hypothetical witness-scale object (say, a 0.5 m
  core) with the same 1.44µm coating would sit at thickness/radius
  ≈ 2.9×10⁻⁶, roughly **60,000× flatter** than this cycle's own most
  favorable measured point. The qualitative direction (flatter → deeper,
  by this cycle's own finding) argues the trend should not reverse between
  r=312 and witness scale — but that is an extrapolation over four to five
  more orders of magnitude of exactly the ratio this cycle's own mechanism
  depends on, unverified, and inherits the same dx-bridge gap
  (`REALIZABILITY_MEMO.md` Entry 2's own ~10⁷-cell citation) that has stood
  unaddressed since Iteration 7. Also unaddressed: this is a 2D
  (infinite-cylinder) proxy throughout — a real witness-scale coated
  volume is doubly curved, not a circular cross-section extruded to
  infinity; whether the fixed-width-rim-leak mechanism this cycle measured
  survives that geometry change is a standing 2D-vs-3D idealization this
  program has always carried, now load-bearing for a headline result
  rather than background caveat.

**The absorptivity gap is unchanged, and it is the one that actually binds
my tier call.** Fix 6 computed, for the first time, the implied e-folding
length this construction requires: `τ_shell/thickness = 24/1440nm`,
**≈60nm**. Re-verified independently here: `ALPHA_PER_NM=0.016667`,
`1/ALPHA_PER_NM=60.0nm`, matches `results.json`-adjacent
`design_geometry.py` exactly. **No citation exists anywhere in this
program tying that number to a real CNT-forest, black-chrome, or
doped-semiconductor absorption coefficient** (Red Team's own Phase-2 audit
grepped `REALIZABILITY_MEMO.md` for exactly this and confirmed the memo
carries thickness precedent only). Stated for what it's worth, informally,
not as a program citation: 60nm is not an outlandish absorption depth for
a *strongly*-absorbing thin film at visible wavelengths in the general
nonlinear/linear-optics literature this seat is aware of — amorphous
silicon and many doped narrow-gap semiconductors sit in the
10⁴–10⁵ cm⁻¹ absorption-coefficient range near their band edge (penetration
depths of order 100nm–1µm), and metallic/plasmonic films can have skin
depths of a few tens of nm — so 60nm sits at the aggressive end of
"ordinary strongly-absorbing thin film," not obviously past it. But this is
domain reasoning, not a sourced check, and it cuts the *other* way too:
CNT-forest/Vantablack-class coatings achieve their near-total absorption
substantially through geometric light-trapping across a porous,
high-aspect-ratio forest — multiple scattering into a near-absorbing bulk,
not a single-pass Beer–Lambert law through a homogeneous medium — so
comparing this bench's single scalar `sigma_max` against a bulk-material α
may not even be checking the physically-correct mechanism for the specific
class of material (CNT forest) `REALIZABILITY_MEMO.md`'s own cited
thickness precedent is drawn from. Flagging this as a *new*, unresolved
sub-question this cycle did not raise: closing the "PLAUSIBLE, not
PUBLISHED" gap needs not just an α citation, but the right *mechanism*
citation — is 1.44µm/τ=24 more like "a homogeneous absorbing film" or "a
light-trapping metamaterial forest," because the two have very different
plausibility arguments and this program has cited precedent for the
thickness of the latter while implicitly modeling the physics of the
former.

## Argued next change

Per charter, my highest-priority next move is the one that actually
converts this cycle's optical result into a materials-tier change: **the
absorptivity/mechanism check fix 6 computed but did not source.** This
cycle sharpens why it matters more now than it did at Iteration 25 when
Entry 2 first flagged it: before this run, the fixed-absolute construction
was an *argued-only* alternative; after this run it is the program's own
best-measured `graded_black_shell` design (deeper C at every tested scale
than the self-similar family this program has cited for 21 iterations) —
the realizability question has moved from "does this matter" to "this is
now the design the program is implicitly favoring, and its one remaining
unchecked claim is the absorption coefficient, not the thickness." Concrete
scope: (a) source a real α or optical-density-per-µm figure for CNT-forest/
Vantablack-class coatings specifically (not black chrome or a-Si, unless
the light-trapping-vs-homogeneous-absorption distinction above is resolved
first) — this needs either T18's WebFetch block lifted or an explicit
WebSearch-snippet-synthesis fallback in the informal style MATERIALS has
used before (Iteration 9's RSA check); (b) state explicitly which physical
mechanism (homogeneous bulk absorption vs. multiple-scattering light
trapping) this bench's single-scalar `sigma_max` law is actually meant to
represent, since the plausibility argument differs by mechanism and this
program has never stated the choice; (c) only then can §9's "PLAUSIBLE,
not PUBLISHED" tier be re-examined — it should **not** move on this
cycle's own evidence alone, since fix 6 computed a number without a
comparator to check it against.

**Tier call: unchanged. PLAUSIBLE, not PUBLISHED stands.** This cycle
strengthens the case that the fixed-absolute-thickness family is the
program's own preferred design lead (better *and* easier to build than the
self-similar alternative it has always been compared against) but supplies
zero new evidence on the one axis (absorptivity/mechanism) that would move
the tier. Recorded here as a `REALIZABILITY_MEMO.md` Amendment
recommendation, not made unilaterally in this review: Entry 2's own
"Open" item (build and measure the fixed-absolute variant) is now closed
by this experiment and should be marked so, with this cycle's C-values and
the sharpened absorptivity/mechanism question folded in as the entry's own
next open item, superseding the stale "Open" line.

## Ranked top-3 (Iteration 31+, since Iteration 30 is LOCKED to VISION's stage-10 instrument)

1. **The absorptivity/mechanism literature check, above.** Highest-value
   MATERIALS-charter item this program currently has queued: it is the
   only thing standing between "PLAUSIBLE" and either "PUBLISHED" or a
   downgrade, on the program's now-favored design. Depends on T18
   resolution or an explicit informal-synthesis fallback; zero FDTD cost
   either way.
2. **The 3λ sweep on the fixed-absolute family, r=156** (PHOTONICS' own
   fix-5 item, scoped away this cycle for cost reasons, not yet run). My
   own stake in this, distinct from PHOTONICS' wavelength-dependent
   rim-diffraction framing: "one real coating, reused at any size" is this
   memo's whole claim, but a real coating's α is not flat across 450–750nm
   either — checking whether the *measured* deepening direction survives
   at other λ is a prerequisite before this family is treated as a
   validated broadband design lead, not just a single-color curiosity.
   Cheap (one r=156 leg, ~20–35 min per this cycle's own timing) relative
   to a fresh r=312 leg.
3. **Extend the core-fill check (P-5/fix 3) to the full N9 sweep**, not
   just θ=0. The θ=0 result is a clean, five-orders-of-magnitude null —
   genuinely reassuring — but T9's own null was always a boresight
   measurement; this cycle is the first to test ratios above 0.385
   (0.692, 0.846) at all, and grazing angles (±25°/±35°) are exactly where
   a hidden PEC/hollow difference would be most likely to leak into the
   silhouette if it existed. Reuses this cycle's own already-built
   `absorber_fixedabs_hollow` machinery at trivial marginal cost (9 more
   angle-pairs, not a new instrument) — the cheapest of the three items
   here and a natural companion to item 2 if both run in the same cycle.

*Not ranked, but noted for completeness: QUANTUM's own flagged item 7 (the
coherent-vs-incoherent bridge gate at the new 30.8%/15.4% shell fraction)
remains open and is not my charter to close, but every C-value this review
rests on inherits it — any future MATERIALS citation of this cycle's
numbers as "the program's best design lead" should carry that same
caveat until QUANTUM's own item is resolved.*
