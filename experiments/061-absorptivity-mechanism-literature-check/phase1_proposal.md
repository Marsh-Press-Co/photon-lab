# exp-061 — Phase 1 Proposal: The `graded_black_shell` Absorptivity Literature
# Check + the Caveat-Propagation-Check Tool

**Panel Iteration 38. Lead: MATERIALS & METAMATERIALS, by UNCONDITIONAL LOCK**
(not rotation — the absorptivity literature check is now eight cycles
deferred, Iteration 29→37, the longest deferral chain this program has run
before a lock fired; `h_eff` fired at 5, `graded_black_shell_flagship` and
`Q_ext(x)` both fired at 3). Two co-mandatory items, both delivered below.
**T1 escape route: NONE.** Zero constraint-1/2/3/4 metric is scored this
cycle. This is a realizability-bound + tooling cycle, the same category as
exp-036/037 (literature checks) and exp-038/046 (new machinery at Phase 1).
Zero FDTD this cycle for item (A); zero FDTD, zero network for item (B).

---

## Item (A): the absorptivity literature check

### 1. Mechanism/scope narrative (≤300 words)

`graded_black_shell`'s fixed-absolute-thickness variant — this program's
own flagship-adjacent design, CLOSED on thickness at Iteration 29 (exp-052:
`C` deepens monotonically toward −1 as the object scales, the physically
*right* direction) but explicitly left OPEN on absorptivity — implies a
physical volumetric absorption coefficient this program has never checked
against a real material. Re-derived here directly from
`experiments/052-fixed-absolute-thickness-shell/design_geometry.py`
(R4 house rule: no hand-typed figure), running `python3 design_geometry.py`
this shift:

```
realizability (Fix 6): thickness=1440.0nm, tau_shell=24.0,
alpha=0.016667/nm, e-fold length=60.00nm
```

i.e. **α = 1/60nm = 1.6667×10⁷ m⁻¹ = 1.6667×10⁵ cm⁻¹**, equivalently
**optical density ≈ τ_shell/ln(10) = 24/ln(10) ≈ 10.42 OD** packed into a
**1.44 µm** physical shell. Why now, not earlier: exp-060 (Iteration 37)
measured that the graded profile's C²-smooth entry does separable,
substantial work beyond bulk loss alone (Q_ext ~31% lower, back-scatter
5547× lower than a matched-optical-depth sharp-edged control) — the
flagship's own physical mechanism is now *measurement-backed*, which makes
whether any real material can supply that same bulk optical depth *within
that same thickness* MORE consequential to this program's realizability
verdict, not less (exp-060 Phase-5, MATERIALS' own finding).

**Question:** is α≈1.667×10⁵ cm⁻¹ (60nm e-folding) over a graded, always-on,
passive coating PUBLISHED, PLAUSIBLE, or UNOBTANIUM for a real ultra-black
coating class?

**Explicit non-scope:** the RSA/TPA/photochromic/FCA/ENZ/combined-media
*switching* mechanisms (T1's σ(I) escape route) — exhaustively checked
already (`REALIZABILITY_MEMO.md`'s main table, exp-036/037). This is a
different question: the raw absorptivity of a passive, always-on absorber,
not a switchable one.

### 2. The search plan (to run at Phase 4, NOT this step)

**Source classes accepted**, ranked by evidentiary weight:
1. Peer-reviewed optics/nano journals reporting measured CNT-forest
   reflectance/absorptivity vs. forest height or effective optical
   constants (n, k) of vertically-aligned CNT arrays (e.g. *Applied Physics
   Letters*, *Optics Express*, *Nano Letters*, *ACS Photonics*, *Proc. SPIE*).
2. NASA/GSFC technical reports and papers on carbon-nanotube black coatings
   for stray-light/baffle applications (the Hagopian et al. line of work is
   this program's own general-domain-knowledge starting point, to be
   verified not assumed).
3. NIST or other national-metrology-institute black-coating characterization
   reports (reflectance/BRDF measurements with stated coating thickness).
4. Manufacturer technical data sheets for Vantablack-class products (Surrey
   NanoSystems' Vantablack/VBx/S-VIS lines, Acktar Metal Velvet, or
   equivalent) that state coating thickness alongside reflectance.
5. A secondary, explicitly-flagged-as-less-comparable class: broadband
   graded-index nanostructured absorbers that are NOT primarily
   conductive-loss-dominated (black silicon nanocone arrays, moth-eye AR
   structures) — accepted only as a bound-widening cross-check, since their
   ε(r) profile (index grading dominant, not `eps_max=1.0` conductive-loss
   dominant) is a structurally different class from what `graded_black_shell`
   codes, and any figure from this class will be labeled accordingly, not
   pooled with the CNT-forest figures.

**Query list (exact terms, committed before any search runs):**
1. `Vantablack absorption coefficient cm-1`
2. `carbon nanotube forest reflectance vs thickness optical density`
3. `CNT forest ultra-black coating micron reflectance 0.035%`
4. `Surrey NanoSystems Vantablack technical data sheet thickness`
5. `NASA carbon nanotube black coating Hagopian absorptivity thickness`
6. `vertically aligned carbon nanotube array effective refractive index imaginary part visible`
7. `super black carbon nanotube array reflectance forest height micron`
8. `carbon nanotube forest absorption coefficient alpha cm-1 visible wavelength`
9. `carbon nanotube forest packing density volume fraction optical properties`
10. `NIST black coating characterization reflectance report`
11. `single wall carbon nanotube film extinction coefficient k optical constants`
12. `black silicon nanostructure reflectance absorption coefficient broadband`
13. `ultra-black coating optical density per micron thickness`
14. `ACktar metal velvet black coating specular reflectance thickness`
15. `ultra black coating ~1 micron thin film absorption coefficient visible`

**Evidentiary-tier disclosure (T18, standing since Iteration 13, 39+
consecutive blocked WebFetch attempts — not independently re-tested this
shift, carried forward per `REALIZABILITY_MEMO.md`'s own convention):**
Phase 4 will almost certainly be **WebSearch-snippet synthesis, not
primary-source PDF/DOI-verified reading** — the identical evidentiary tier
as exp-036/exp-037, disclosed there and here at the same standard. Per
Red Team's explicit Iteration-26 ruling (already rejected one informal,
unsourced desk tier-call for this exact question), the Phase-4 verdict
**must** cite specific WebSearch results/snippets, not be rendered as an
unsourced desk estimate — a genuine sourced search, matching every other
WITH-PARAMETERS row in `REALIZABILITY_MEMO.md`'s table.

### 3. Falsifiable predictions — committed BEFORE any search runs

General nonlinear/linear-optics and nanomaterials domain knowledge only
(no search executed to produce these numbers); reasoning stated so Phase 4
can be scored against it honestly.

**Reasoning.** Real CNT forests are *dilute* structures — vertically
aligned tubes at a small areal/volume packing fraction (order 1–10%
reported across the growth literature), not a solid carbon film. Their
measured near-total blackness (reported reflectances as low as ~0.02–0.05%
for Vantablack-class coatings) is generally understood to arise from a
**combination** of (a) a graded effective index at the entry (genuinely
comparable to this program's own adiabatic-entry design intent) **and**
(b) multiple scattering / light-trapping among sparse, high-aspect-ratio,
often-tangled tube tips over a physically **large** stack — published
forest heights achieving record blackness are consistently in the
**tens of microns**, not fractions of a micron. That combination — dilute
fill fraction + structural light-trapping, not a homogeneous bulk
Beer-Lambert medium — is mechanistically different from `graded_black_shell`'s
own coded abstraction (`eps_max=1.0`, a smooth conductivity ramp, an
effectively homogeneous lossy medium), and predicts a MUCH LOWER effective
volumetric absorption rate than 1.667×10⁵ cm⁻¹ once the total measured
optical density is divided by the material's own real thickness, not by
1.44 µm.

| # | Quantity | Predicted band | Reasoning |
|---|---|---|---|
| MP-1 | Literature CNT-forest effective **α**, as OD-per-length inferred from published (reflectance, thickness) pairs | **1×10³ – 3×10⁴ cm⁻¹** (e-fold depth ≈ 0.3–10 µm) | 1–2.5 orders of magnitude BELOW α≈1.667×10⁵ cm⁻¹ |
| MP-2 | Published CNT-forest coating thickness needed to reach OD comparable to this program's own ≈10.4 OD (τ_shell=24) | **15–150 µm** | vs. this program's 1.44 µm — a ~10–100× thickness gap |
| MP-3 | Any single primary source reporting α ≥ 1×10⁵ cm⁻¹ (i.e. within ~2× of the target) at ANY visible wavelength for a genuinely broadband, non-resonant, non-metallic-interface coating | **NOT FOUND** (predicted null result) | no mechanism in the reasoning above supports it; a hit here would be the single most falsifying possible outcome for MP-4 |
| MP-4 | **Predicted tier verdict** for α≈1.667×10⁵ cm⁻¹ / 60nm e-folding, at 1.44 µm physical thickness | **UNOBTANIUM-WITH-PARAMETERS** (not PUBLISHED; not PLAUSIBLE at THIS specific thickness) | the rate itself may turn out to be uncontroversial for carbon-black-class materials in bulk, but reaching it within a 1.44 µm, dilute, adiabatically-graded, near-ε=1 coating specifically is the predicted gap |
| MP-5 | **Conditional plausibility restatement** — if MP-1/MP-2 confirm, is τ_shell=24 achievable AT ALL for this construction class, just not at 1.44 µm? | **YES, PLAUSIBLE at ~15–100× the thickness** | reframes the verdict from "impossible" to "the specific thickness-vs-optical-depth combination is the unobtainium part," consistent with Entry 2's own closed thickness-only finding at Iteration 29 (a *different* fixed thickness, 1.44µm, was already shown optically superior in scaling behavior — this item is about whether that specific absolute thickness can carry that much absorption, not about whether the shape/PEC-coring approach works) |

**Falsification, pre-registered:** MP-4 is falsified toward PLAUSIBLE or
PUBLISHED if Phase 4 turns up a primary-or-best-available source reporting
CNT-forest (or comparable broadband graded near-ε=1 absorber) effective α
within roughly 2× of 1.667×10⁵ cm⁻¹ **at a stated thickness within roughly
2× of 1.44 µm** — both conditions together, since a high α at a much larger
thickness does not license this program's own specific construction. MP-1/
MP-2 are the primary falsifiable quantities; MP-4 is a synthesis of them,
not independently scored.

---

## Item (B): the caveat-propagation-check tool

### Design rationale

**Spec, as authorized (LOGBOOK.md, Iteration 37 close):** *"a lint-style,
grep-every-caveat-across-every-touched-file tool."* First proposed by
VISION SCIENCE at Iteration 15, never built across seven cycles of hand
patches (Iterations 17, 24, 32, 33, 34, 35, twice at 36, again at 37) that
each closed one instance and missed another — most recently, Iteration 37's
own `run_all.py::stage22_uniform_lossy_shell` docstring, the single most
permanent, git-tracked site describing exp-060's control, which still
carried the pre-run "diffraction" framing after the run's own P-10 result
had refuted it.

**What it scans:** by design, a hand-curated **registry**
(`lab/caveat_lint_config.json`, checked in) of caveat entries, each naming:
a short key phrase (as an ANY-OF list of acceptable regex paraphrases, not
one exact string — a caveat is rarely restated verbatim), a list of
`required_sites` (the N named sites a Phase-3/Phase-5 docket promised
propagation to), and `trigger_terms` (function/module names or numbers
that indicate a file is citing the *same claim* without necessarily
carrying the caveat) used only to hunt for undocketed candidate sites. The
default candidate-scan universe is `LOGBOOK.md`, `PLAN.md`, `SESSION_LOG.md`,
`PANEL.md`, every `experiments/*/NOTES.md` and `experiments/*/*.py`, every
`lab/*.py`, and `lab/validation/run_all.py`/`VALIDATION.md` — text/prose
sites a caveat plausibly propagates into. `results.json` files and the
hard-limit files (`lab/ARTIFACTS.md`, `lab/artifacts.py`, `AGENTS.md`,
`lab/viz.py`) are excluded from both required-site and candidate scanning.

**What counts as "a caveat":** operationally, exactly what the mandate
specifies — a short phrase or clause a Phase-3/Phase-5 mandatory-fix docket
names as needing to appear at N specific sites. The docket entry is the
source of truth; the registry entry is this tool's transcription of it,
and the tool's job is (1) verify all N sites actually contain a recognizable
paraphrase, and (2) separately, non-gating, flag new files that reference
the same underlying claim/number/module but don't carry the phrase, for a
human to triage.

**How a Director uses it (both a config-driven mode and an ad-hoc mode, as
the mandate asked):**
- `python3 lab/caveat_lint.py` — runs every registered caveat against the
  live working tree, prints a PASS/FAIL per required site and WARN per
  candidate site, exits 1 if any required site fails.
- `python3 lab/caveat_lint.py --only <id>` — one registry entry.
- `python3 lab/caveat_lint.py --adhoc --phrase "..." --sites a.md,b.py
  [--trigger term]` — a one-off check for a same-shift Phase-5 fix, before
  a Director decides whether it's worth adding to the checked-in registry.
- `python3 lab/caveat_lint.py --selftest` — the historical validation
  below.

**Module/CLI path:** `lab/caveat_lint.py` (script + library functions),
registry at `lab/caveat_lint_config.json`. Pure Python stdlib
(`argparse`, `json`, `re`, `os`, `fnmatch`, `subprocess` for `--selftest`
only) — **no numpy, no network, no FDTD.**

**Why this is NOT a `run_all.py` trust-suite stage** (stated explicitly,
for Red Team to check): `run_all.py`'s stages 1–22 each certify an
engine-physics or closed-form identity against hard expected numbers —
"does this substring appear in this file" is a categorically different
kind of assertion (documentation-completeness, not measurement), and
folding it in would blur `VALIDATION.md`'s own "stage N green = a physics
claim is verified" semantics. It also needs a hand-curated registry that
only a Director should decide to extend (same as deciding a new stage is
warranted) — auto-firing it inside every `run_all.py` invocation would
either silently skip undocketed new caveats (false confidence) or force
every engine-trust run to also validate an unrelated documentation
registry. The tool is real, working, and load-bearing on its own terms;
it is a lint pass, run on its own schedule (after every Phase-3/Phase-5
mandatory-fix docket lands), not a physics gate.

### Self-test / validation, run this shift (not deferred to Phase 4 — this
is code, not a literature search, so it can and should be validated now)

**Prediction, committed before running:** checking `lab/validation/run_all.py`
for the corrected framing ("Fresnel-type reflectance at the sharp
conductivity discontinuity") against two REAL git revisions — the pre-fix
commit `d5b4844` (Iteration 37 Phase 3, machinery committed before the run)
and the post-fix commit `4f29982` (Iteration 37 Phase 5, same-shift fix) —
will FAIL at `d5b4844` and PASS at `4f29982`, demonstrating the tool would
have caught the actual Checkpoint-4 gap had it existed at the time.

**Result, this shift:**
```
$ python3 lab/caveat_lint.py --selftest
  PRE-FIX  (d5b4844, Phase 3, before the run): caveat phrase ABSENT -- expected ABSENT -> PASS
  POST-FIX (4f29982, Phase 5, same-shift fix): caveat phrase FOUND -- expected FOUND -> PASS
Self-test PASSED: the tool correctly discriminates the pre-fix (gap present)
from the post-fix (gap closed) revision.
```
**CONFIRMED**, exactly as predicted. This is a genuine retroactive test
against real history, not a constructed toy case — `d5b4844` and `4f29982`
are the actual commits from Iteration 37's own record.

**Registry seeded this shift** (three entries, `lab/caveat_lint_config.json`):
1. `exp060-p10-fresnel-not-diffraction` — the case above, run live against
   the current tree: **PASS**, both required sites (`run_all.py`,
   `experiments/060.../NOTES.md`).
2. `exp060-sigma-flat-convention-caveat` — Iteration-37 mandatory fix 5's
   own propagation promise (the sigma_flat matching-convention caveat):
   **PASS**, both required sites (`experiments/060.../NOTES.md`,
   `lab/materials.py`).
3. `exp052-alpha-60nm-absorptivity-open` — THIS cycle's own standing
   caveat (no primary CNT-forest citation exists to check α≈1/60nm
   against): **PASS** at its two current required sites
   (`REALIZABILITY_MEMO.md`, `experiments/052.../design_geometry.py`).
   Registered now so that if item (A)'s Phase-4 search resolves this
   question, whichever new NOTES.md/REALIZABILITY_MEMO.md language records
   the resolution can be checked for propagation the same way, and so a
   future Director extending this registry has a live worked example for
   "how do I add a new caveat."

Full live output (all three entries, current tree): **0 required-site
failures**, several WARN-level candidate sites surfaced for human triage
(e.g. `LOGBOOK.md` and sibling experiment files that mention `tau_shell` or
`sigma_flat` without the phrase — expected and correct: not every mention
of a number needs the full caveat restated, this is exactly the
"lead, not gate" behavior by design).

---

## Idealizations — stated honestly

1. **Item (A) predictions are general-domain-knowledge estimates, not
   search results.** No WebSearch query has been run this step (house
   discipline). MP-1/MP-2's specific numeric bands are informed guesses
   about what the literature likely shows, explicitly built to be
   falsifiable at Phase 4, not themselves sourced yet.
2. **T18's WebFetch block is assumed still standing**, carried forward from
   `REALIZABILITY_MEMO.md`'s own most recent confirmation (39+ consecutive
   attempts since Iteration 13) — not independently re-tested this Phase-1
   step (Phase 4 will re-confirm before falling back to WebSearch-snippet
   synthesis, per prior cycles' own pre-flight convention).
3. **The Beer-Lambert framing itself may not be the right lens for real
   CNT forests** — the predictions above explicitly flag that real
   blackness is plausibly dominated by structural light-trapping /
   multiple scattering, not homogeneous bulk absorption, which is *why* a
   naive α comparison is predicted to look unfavorable. If Phase 4's own
   sources characterize CNT-forest blackness in genuinely different terms
   (e.g. no stated reflectance-vs-thickness curve exists at all), MP-1/MP-2
   may be unscoreable as stated and will need a restated comparison
   (disclosed here as a real risk to this cycle's own falsifiability, not
   discovered later).
4. **The secondary comparator class (black silicon, moth-eye structures)**
   is index-grading-dominant, not conductive-loss-dominant — genuinely a
   different `eps(r)` shape than `graded_black_shell` codes. Any figure
   from that class is disclosed as a bound-widening cross-check only, not
   pooled into the primary CNT-forest verdict.
5. **The caveat-lint tool's phrase matching is deliberately loose**
   (whitespace-normalized substring/regex, case-insensitive, ANY-OF a list
   of acceptable paraphrases) — a false negative (a real propagation the
   tool fails to recognize because the wording drifted too far) is possible
   for a caveat whose registry entry was written with too narrow a
   `phrase_patterns` list. This is a lint tool, not a semantic verifier; a
   human still reads the PASS/FAIL/WARN report.
6. **The tool's registry is hand-curated, not automatically populated from
   Phase-3/Phase-5 dockets** — a Director must still read a mandatory-fix
   docket and decide to add an entry. This is a deliberate design choice
   (stated above), not an oversight, but it means the tool cannot catch a
   caveat that was never registered — it converts "did we remember to
   check every site by hand" into "did we remember to register the
   caveat," a smaller and more tractable failure surface, not a zero one.
7. **`--selftest`'s historical replay checks exactly one phrase against
   exactly one file at two revisions** — a single, real, well-documented
   case, not a statistical sample of all six prior near-misses (Iterations
   17/24/32/33/34/35/36). Chosen because it is the most recent, most
   precisely documented (exact commit hashes named in NOTES.md/LOGBOOK.md),
   and directly named in this cycle's own mandate as the concrete target.
8. Item (B) required no FDTD, no `Sim`/`lab.fdtd2d` engine code, and no
   trust-suite stage — confirmed by inspecting `lab/validation/run_all.py`'s
   own structure and docstring this shift (its five documented stage
   classes: regression / impedance / fdtd-lib / ceviche / cloak-smoke, all
   engine-physics checks) before concluding a new stage would be a category
   error, not merely unnecessary.
