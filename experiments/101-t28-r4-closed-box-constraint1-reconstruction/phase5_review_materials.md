# Phase 5 Review — MATERIALS & METAMATERIALS — Panel Iteration 78 (exp-101)

*Fresh sub-agent, MATERIALS & METAMATERIALS charter (sub-wavelength structure;
realizability bound: published / plausible / unobtainium-with-parameters). I
critiqued this cycle's Phase-1 proposal once already (`phase2_critique_
materials.md`); this is a second, independent pass over the finished cycle,
including real results. Blind to the other six seats' Phase-5 reviews. Every
load-bearing number below was re-derived directly from `results.json`,
`lab/sections.py`, `experiments/069-.../design_geometry.py`, and
`experiments/034-.../REALIZABILITY_MEMO.md` — not taken from NOTES.md's own
prose on faith.*

## 1. Charter-fit note

Same as Phase 2: this cycle proposes zero new material or mechanism. The
article is byte-identical to exp-100's own `R4_CONFIGS` (`pec_disk` +
`graded_black_shell`, `SIGMA_R4_CORRECTED=0.25`, re-verified this session at
`experiments/069-.../design_geometry.py:300`, `==0.25` to 1e-12). This is a
pure instrument-fidelity cycle (closed four-face Poynting-box reconstruction
of `beam_behind_t28`), and it delivers on that scope: `lab/` diff is zero
(confirmed — all new logic lives in `experiments/101-.../run.py`), and my
Phase-2 mandatory fix (T9's disclaimer carried with the `[0.505,0.520]`
band/measured `[0.5129,0.5145]` range) genuinely landed. But two results this
cycle actually produced — never anticipated in Phase 1 or caught in Phase
2/Red-Team — do bear on my charter, and I flag both below (§3, §4). Neither
overturns the cycle's own Tier-0 verdict; both are disclosure gaps a future
citation could exploit exactly the way MATERIALS' own Phase-2 attack warned
against.

## 2. Verification of my own mandatory fix (item (a) of this review's brief)

**CONFIRMED, correctly and completely carried.** I independently recomputed
`sigma_abs/sigma_ext` for all 12 cells directly from `results.json`:

| θ | C40_R4 | G40_R4 |
|---|---|---|
| 37.127246 | 0.51398 | 0.51363 |
| 38.590230 | 0.51376 | 0.51397 |
| 39.200000 | 0.51397 | 0.51345 |
| 40.265420 | 0.51291 | 0.51326 |
| 41.460901 | 0.51450 | 0.51437 |
| 42.960901 | 0.51403 | 0.51420 |

min=0.51291, max=0.51450 → NOTES.md's stated `[0.5129, 0.5145]` is exact, not
rounded-favorably. NOTES.md's Result item 1 states, immediately adjacent to
this range: *"T9's disclaimer applies as pre-registered (change 6): this
exceeds the Babinet/shadow-formation ≤0.5 ceiling and is read as a near-field
box-geometry effect (z/z_R≈0.04–0.06, T8), not an asymptotic
material-absorptivity constant."* That is T9's disclaimer verbatim in
substance (I checked it against `LOGBOOK.md` line 1161 directly), stated in
the Result section itself (not buried in Idealizations), co-located with the
number as my own mandatory fix required. **No gap here.**

## 3. A new, undisclosed realizability-relevant pattern in the raw `sigma_abs` values (item (b))

NOTES.md's Result narrates `sigma_abs` rising "310→339" alongside the thermal
sidecar, but only ever discusses the **ratio** `sigma_abs/sigma_ext` against
the Babinet ceiling (≤0.5). Nobody — not the Phase-1 proposal, not any of the
five Phase-2 critiques, not Red Team — checked the raw `sigma_abs` figures
against the article's own **geometric footprint**, `2·R4_R_OUT = 312` cells
(`lab/sections.py`'s own stated convention: these are widths in cells, "the
2D analogue of cross-sections," with `Q = width/(2·outer_radius)` the correct
ranking metric — i.e. `sigma_abs/312` is exactly `Q_abs`, absorption
efficiency).

I computed `Q_abs = sigma_abs/312` for all 12 cells directly from
`results.json`:

| θ | C40_R4 Q_abs | G40_R4 Q_abs |
|---|---|---|
| 37.127246 | 0.9966 | 0.9942 |
| 38.590230 | 1.0188 | 1.0231 |
| 39.200000 | 1.0275 | 1.0286 |
| 40.265420 | 1.0439 | 1.0407 |
| 41.460901 | 1.0616 | 1.0664 |
| 42.960901 | 1.0858 | 1.0817 |

**10 of the 12 cells have `Q_abs > 1`** — the object's absorption cross
section alone (not extinction) exceeds its own geometric diameter, rising
monotonically to **8.6% over unity** at the largest tested angle
(42.960901°). `Q_abs ≤ 1` is the idealized geometric-optics ceiling for *any*
passive object's true absorption efficiency (a perfectly black disk absorbs
at most all the power geometrically incident on it, in the far field — this
is a sharper, more elementary bound than the `σ_abs/σ_ext ≤ 0.5` Babinet
ratio T9 already names, since it does not require invoking the forward-
diffraction companion lobe at all). This is the exact same class of finding
MATERIALS' own Phase-2 attack caught for the ratio — a bench-measured number
that structurally cannot describe any real absorptivity a material could
have — but it currently carries **no disclaimer anywhere in this cycle's
record**, despite T9's disclaimer having been carried faithfully for the
adjacent ratio quantity one line above it in NOTES.md's own Result section.

This does not overturn anything Tier 0 measured (the closed-box mechanics
are still correct and box-independent — `box_dev_scat_downstream` confirms
this at every angle), and it is fully consistent with, not contradictory to,
the near-field-box explanation (T8) already invoked for the ratio: a box at
`z/z_R≈0.04–0.06` is not yet in the asymptotic regime where `Q_abs≤1`
strictly holds either. But it is a **defect of omission** a future cycle or
a future MATERIALS review could trip on: citing "the absorber's own
cross-section, ~310–339 cells" without noting it exceeds the object's own
156-cell radius's diameter would read, to an unwary future reader, as
evidence of super-unity absorption efficiency in a real coating — exactly
the kind of near-field artifact my charter exists to flag before it travels
further. **Recommended fix**: extend NOTES.md's existing T9-disclaimer
sentence (already present for the ratio) to also cover `Q_abs=sigma_abs/312`
explicitly, one sentence, no re-run required.

## 4. Prediction 3's falsification and the extinction-paradox explanation — consistency check against the ARTICLE'S OWN LOCKED REALIZABILITY VERDICT (item (c))

NOTES.md's Result item 3 explains the ~4× overshoot of `sigma_scat_downstream`
past its predicted ceiling as the textbook extinction-paradox companion of a
near-perfectly-black, optically-large absorber (`Q_ext→2`, split roughly
`Q_abs≈1`/`Q_scat≈1` in the far field) — this is correct, standard
diffraction physics for an object that actually achieves near-total,
near-zero-reflectance absorption. My charter's question is narrower: **is
the object this cycle actually simulated the kind of object that physics
applies to, and does a real build of it exist?**

I traced the exact geometry independently from `design_geometry.py`:
`R4_R_OUT=156` cells, `PEC_R_R4=60` cells, `DX_M_R4=1.5e-8 m` (15nm/cell) →
shell thickness `(156−60)×15nm = 1.44 µm`, and `SIGMA_R4_CORRECTED =
SIGMA_NATIVE_FOR_R4/R4_RATIO = 0.25` — the file's own comment states this
"holds the shell's [optical depth constant]" as the grid resolves finer,
i.e. this is literally the same self-similar, τ_shell-preserving
`graded_black_shell` construction `REALIZABILITY_MEMO.md` Amendments 6–7
formalize and score. **The 1.44 µm figure is not a coincidence — it is the
identical thickness Amendment 6/7 cite by name** ("this construction's own
1.44µm shell") when they LOCK `graded_black_shell` **UNOBTANIUM-WITH-
PARAMETERS, overdetermined by the thickness axis**: real CNT-forest/
Vantablack-class coatings run 100–500 µm (70–350× thicker), NiP-black
10–45 µm (6.9–31× thicker, with its own rate gap 11–56× worse), and
carbon/graphene aerogel 1–5 mm (694–3472× thicker) — "four independently-
sourced real-material comparator classes... zero clear the joint 2×/2× bar,"
per that memo's own closing line, itself unchanged by anything in this
cycle.

**Consequence for Prediction 3's explanation**: the extinction-paradox
mechanism NOTES.md invokes is correct physics *for the idealized,
already-simulated article* — but that article's own near-total blackness
(`τ_shell≈24`, driving `Q_abs≈1–1.09` and the resulting large forward
companion lobe) is precisely the trait no currently-known real material can
deliver at this exact 1.44 µm thickness. A real, buildable coating at this
thickness (extrapolating from the closest real comparator, NiP-black, whose
own rate gap is 11–56× at comparable thickness) would be far less optically
black, would extinguish far less power, and — by the SAME extinction-paradox
logic NOTES.md correctly cites — would show a correspondingly SMALLER, not
comparably-sized, forward-diffracted companion lobe, because a leaky/
partially-transmitting/partially-reflecting real shell of this thickness
does not approach `Q_ext→2` at all. **This is not a flaw in the physics
explanation as stated — it is a scope gap**: NOTES.md's Result and Learned
sections state the extinction-paradox finding as a general lesson for "any
future constraint-1 instrument" without noting that the specific numeric
magnitude measured here (`sigma_scat_downstream∈[170.5,192.2]`, ~55–62% of
the geometric ceiling) is itself a property of an article already LOCKED
unobtainium, not a number that would carry over to a realizable absorber
substituted at the same thickness. No prior document in this cycle's record
(proposal, five critiques, Red Team audit) makes this connection — the
Phase-1 proposal's own §5 disclosed only that this is a near-field, not a
witness-intensity, measurement; it never connected the measured absorber's
identity to the standing realizability lock. **Recommended fix**: one
sentence in NOTES.md's Learned section noting that the extinction-paradox
magnitude measured here describes the LOCKED UNOBTANIUM-WITH-PARAMETERS
`graded_black_shell` construction specifically (cross-reference
`REALIZABILITY_MEMO.md` Amendments 6–7), not a property any currently-named
real coating at this thickness would reproduce.

## 5. Thermal sidecar ("all 12 cells UNDETECTABLE")

Independently re-verified directly from `results.json`
(`netd_classification_c`/`_g` for all 6 angles): all 12 read
`"UNDETECTABLE"`, exactly as NOTES.md states, with `p_abs_w`/`dt_ss_full_K`
both rising monotonically with θ in step with `sigma_abs` (e.g.
`p_abs_w_c`: 2.7866e-12 W → 3.3080e-12 W; `dt_ss_full_K_c`: 4.578e-5 K →
5.435e-5 K). No realizability implication follows from this specific
finding for my charter: `graded_black_shell`'s tier verdict is already
overdetermined by the thickness axis (§4, above) independent of thermal
detectability, and nothing about a monotonic ~19% rise in an already-
UNDETECTABLE absorbed-power reading moves that. I confirm THERMODYNAMICS'
own mandatory R21 fix (narration, not just persistence) genuinely landed —
this is not merely a `results.json` field, it is stated in NOTES.md's
Result prose as committed.

## 6. Verdict on this cycle (MATERIALS charter)

**Confirm, with two disclosure gaps to close, neither blocking.** The Tier-0
core deliverable is sound: the closed-box reconstruction is a genuine
instrument improvement (I independently re-derived box-independence,
`box_dev_scat_downstream∈[0.0057,0.0454]`, comfortably inside `XI_TOL`),
zero `lab/` diff, zero new material or mechanism, and my own Phase-2
mandatory fix (T9's ratio disclaimer) is carried correctly and completely.
Neither of the two gaps I found (§3's raw `Q_abs>1` values; §4's extinction-
paradox-magnitude-describes-a-locked-unobtanium-article gap) was caught by
the Phase-1 proposal, any of the five Phase-2 critiques, or Red Team's
audit — all of which examined the `sigma_abs/sigma_ext` RATIO's Babinet
ceiling but never checked the ABSOLUTE `sigma_abs` magnitude against the
object's own geometric footprint, and none connected Prediction 3's own
physics explanation back to `REALIZABILITY_MEMO.md`'s standing tier lock on
the exact article being measured. Both are one-sentence NOTES.md additions,
not re-runs.

## 7. Ranked next steps (this seat's own charter priority, not binding on lead rotation)

1. **Close §3/§4's disclosure gaps in NOTES.md** (one sentence each,
   zero FDTD cost) before this cycle's Result section is cited by any future
   iteration — the same standing discipline (R9/R20-shaped) that produced
   this cycle's own mandatory T9 fix in the first place.
2. **The still-unbuilt coherent, phase-resolved downstream point-intensity
   instrument** (NOTES.md's own "Next" #1) — I concur from my own charter
   angle for an additional reason NOTES.md doesn't state: only a coherent
   (phase-aware) instrument can eventually distinguish "this specific,
   currently-unrealizable near-total absorber's forward lobe" from "what a
   real, thickness-constrained coating's forward lobe would actually look
   like" — a question my charter will need answered before any future
   witness-scale realizability claim about constraint 1 can be made.
3. **Tier 1's R3-vs-R4 `delta_scene` split** remains queued, unchanged,
   out of scope this cycle — no charter-specific addition from MATERIALS
   beyond what NOTES.md/Red-Team's audit already disclosed (the pool-
   duplication caveat, correctly carried as a caveat, not settled fact).
