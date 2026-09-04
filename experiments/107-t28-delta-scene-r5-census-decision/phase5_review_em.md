# PHASE 5 — REVIEW · ELECTROMAGNETISM · Panel Iteration 84 (exp-107)

*Fresh context, blind to all other seats' Phase-5 reviews. Charter: field/
wave behavior, impedance matching, energy coupling; owns the reciprocity/
passivity/causality bookkeeping. All numbers below were independently
re-derived from primitives — the raw capture pickles this cycle's own
`chunk_runner.py`/`finalize.py` produced still sit in this session's
scratchpad (`.../scratchpad/exp107/r{156,312}_{empty,article}_done.pkl`)
— not taken from `results.json`'s printed digits or NOTES.md's prose.*

## 1. Item 1's ledger — box_dev re-derived; box-independence alone is
   NOT the full passivity/energy-bookkeeping standard this program has
   set for itself, and this cycle skipped the further check

**Re-derivation, from the actual pickled `cap_e`/`cap_a`/`sigma_e` arrays,
calling `sections.widths()` myself at both `box_a` and `box_b`:**

```
r=156: box_a sigma_ext=560.2118425678262   box_b sigma_ext=559.8150730013186
       box_dev = |Δ|/|sigma_ext(box_a)| = 0.0007082491592625747
r=312: box_a sigma_ext=1191.405731015438   box_b sigma_ext=1191.141331055922
       box_dev = 0.0002219226856419363
```

Both **exact bit-for-bit matches** to `results.json`'s printed `box_dev`
values, computed here independently from the raw field snapshots, not
copied from the file. The formula used (`abs(wa.sigma_ext-wb.sigma_ext)/
abs(wa.sigma_ext)`) is also confirmed, by direct code read of `run.py`'s
`item1_and_4_one_r()` and `finalize.py`'s `finalize_r()` (identical line
in both), to be the SAME convention every one of the ~27 other on-repo
`box_dev` definitions uses — no metric drift of the kind LOGBOOK's own
exp-091 Phase-2 audit once caught (T11's silent `/mean` redefinition).
Both values sit 2–3 orders of magnitude inside the established `≤0.12`
band. **This part of the claim is fully confirmed, not merely trusted.**

**But box-independence answers only one question — "does the answer
depend on where I drew the box?" — and this program's own instrument
(`sections.radial_absorbed_power`) carries a SECOND, physically distinct
check built for exactly this ledger: whether the box-integrated absorbed
power agrees with the independently-computed spatial (Joule-dissipation)
integral.** `sections.py`'s own module docstring names this explicitly as
an *empirical closure* check — "the sum-over-bins-equals-box-ledger-p_abs
comparison this function's own suite gate (stage 10) checks... not an
exact identity to machine epsilon" — and exp-106's own `ledger_check()`
computed it every time it invoked this exact instrument (`closure =
abs(total - p_abs_box)/abs(p_abs_box)`), on this same fixed-abs family, at
this same r=156 (and r=312, though that leg didn't commit at exp-106).
`run.py`'s `item1_and_4_one_r()` and `finalize.py`'s `finalize_r()` both
call `radial_absorbed_power()` for `core_frac` alone and never compute
`closure` — the field simply does not exist anywhere in `results.json`.

**Is the omission load-bearing? I computed it myself, from the same raw
pickles, so this is not speculation:**

```
r=156: radial_total (Joule-density sum, r<=R_COAT) = 690.9033091549353
       p_abs_box (sigma_abs * i_inc, box ledger)    = 690.7676771573351
       closure = |Δ|/|p_abs_box| = 0.000196  (0.0196%)
r=312: radial_total = 1453.7188587733742
       p_abs_box     = 1452.9004484288666
       closure = 0.000563  (0.0563%)
```

Both closures are excellent — an order of magnitude *tighter* than
box_dev itself at both r, comfortably inside any threshold this program
has ever used for this channel. **The omission is a real discipline gap
(a check exp-106's own sibling instrument treated as standard practice
was silently dropped when the same instrument was reused one cycle
later) but is demonstrably NOT outcome-determining this cycle** — had it
been run, it would have passed cleanly, corroborating rather than
undermining Item 1's PASS. I flag this as the R16-family shape (a
established-elsewhere check quietly not carried forward into a new
call site of the same instrument) rather than a live physics concern.

**A genuinely new, independent check neither exp-106 nor exp-107 ran, but
that this program's own `sections.widths()` already computes for free**:
the two-route extinction identity (`sigma_ext` via face-flux vs.
`sigma_ext_cross` via the incident×scattered optical-theorem integral —
`sections.py`'s own header: "the two routes must agree"). I computed
both at `box_a`:

```
r=156: sigma_ext=560.2118425678262   sigma_ext_cross=560.2085680585642   rel dev = 5.85e-6
r=312: sigma_ext=1191.405731015438   sigma_ext_cross=1191.4201473798992  rel dev = 1.21e-5
```

Excellent agreement, independent of `box_dev`/`closure`. This is a third,
free reciprocity-adjacent cross-check this cycle's own item 1 already had
available and didn't surface — worth naming in the record even though it
changes no verdict.

## 2. Item 4's interpretation — physically plausible, but the specific
   candidate confound EM should flag (numerical dispersion) has not
   been discriminated from the favored (real-shadow) reading

The finding — 18.3% (r=156) / 26.8% (r=312) of the article-scene window's
cells sit below the solver's own 10%-of-RMS noise floor, monotonically
worse at the larger r — is **plausible as genuine physics, not
manifestly an error**, for a concrete, checkable reason: this window sits
directly behind a near-total-absorber (established anchor: `abs_ext_
ratio≈0.49–0.52` at every r/family on this bench, and the program's own
"beam-behind 1.5–1.8%" precedent for a comparably efficient shell). A
fixed-size window (`behind` box is a constant 100×40-cell strip in the lab
frame, unscaled by r) sampling the shadow of a coating whose *silhouette*
grows with `R_COAT` will geometrically contain a shrinking bright-core
fraction and a growing deep-shadow fraction as r increases — exactly the
monotonic 18%→27% trend observed, with no need to invoke solver error.
PHOTONICS' own already-flagged `~200,000×` article-scene collapse at
r=312 (exp-106 Phase 5) is independent corroboration of the same physical
mechanism from a different angle.

That said, **my own charter obliges a specific check for the alternative
this cycle did not run: numerical (Yee-grid) phase dispersion accumulated
over the run.** At fixed `cpl=20` the *per-wavelength* dispersion error is
constant across r, but the *total optical path* (in wavelengths) traveled
before the field reaches the downstream window scales with `R_COAT`, and
`STEPS` scales linearly with r as well (6400→12800) — so a genuine
dispersion-driven phase/amplitude drift, if present, would also be
expected to *worsen* with r, giving the identical monotonic direction as
the shadow-geometry explanation. The two hypotheses are not
distinguished by this cycle's own data; they make the same qualitative
prediction. **This program's own standing meta-rule (R3 in the RULED OUT
registry: "any surprising feature gets a resolution check before it gets
a mechanism debate — and 'artifact' claims need the check too") has not
yet been applied to this finding.** The correctly-targeted, cheap
discriminator is a `cpl`-refinement (e.g. `cpl=30`) rerun of the r=312
hollow-article window only: if `frac_unresolved` holds near 26.8% (or
worsens further, since finer grids resolve MORE structure, not less) the
shadow-geometry reading is confirmed; if it collapses toward 0% under
refinement, dispersion/under-resolution is implicated instead. Absent
that check, I read the shadow-geometry explanation as the *better*
supported of the two on prior-precedent grounds (it fits three
independent, already-established facts: the near-total-absorption anchor,
PHOTONICS' collapse figure, and the fixed-window/growing-silhouette
geometry) — but "better supported" is not the same as "discriminated,"
and NOTES.md's own Result section does not make this distinction.

## 3. The chunked checkpoint/resume methodology (`chunk_runner.py`) —
   plausibly exact by construction, genuinely unverified this cycle,
   and no gate in this cycle's record could have caught a discontinuity

**Scope correction first, independently confirmed from the pickles
themselves**: only the **r=312** leg actually used pickled mid-run
checkpointing (`r312_{empty,article}_done.pkl` — 6 chunks of 2200/1800
steps each, `12800` total, exact). **r=156 did NOT** — its own saved
pickle (`r156_empty.pkl`, keys `cap_e`/`ez_e`, no `sim`/`steps_done`)
confirms it ran as a single uninterrupted `sim.run(6400)` call, matching
`run_output.txt`'s own "single foreground call" label. `chunk_runner.py`'s
own module docstring claims r=156 "completes in 1 chunk" then
immediately contradicts itself ("`STEPS=6400 < CHUNK_STEPS` is not true
here") — a real but harmless documentation inconsistency (the code path
taken for r=156 bypassed this module entirely; nothing about it affected
that leg's numbers). **The discontinuity question below applies only to
r=312's four numbers** (`sigma_abs`, `sigma_ext`, `core_frac`, floor-gate
fraction).

**Steel-man**: reading `lab/fdtd2d.py::Sim.run()` line by line, the
per-step recursion is a pure function of instance state that is entirely
ordinary-picklable: `Ez`/`Hx`/`Hy`/`Bx`/`By` (numpy float64 arrays,
bit-exact through pickle), `sigma_e`/`eps_r`/`damp_e`/`damp_hx`/`damp_hy`
(static per run — this bench's own documented "no time-varying
materials" gap, LOGBOOK ESTABLISHED §2 — hence unchanged across a
checkpoint boundary by construction), `sources` (dicts of plain arrays/
scalars), and `step_count` (a plain Python int, the SOLE quantity the
source phase `sin(omega*n)` and ramp envelope `n<ramp` depend on). There
is no wall-clock-, RNG-, or process-local state anywhere in the update
loop. `alpha`/`ca`/`cb` are recomputed fresh inside every call to `run()`
from `sigma_e`/`eps_r` alone — recomputing them once per chunk rather than
once for the whole run cannot introduce drift, since floating-point
arithmetic is deterministic given identical inputs. On this reading,
resuming from a full pickle and calling `.run(remaining)` again should be
bit-identical to one uninterrupted `.run(total)` call. `materials.py`'s
own `objects.append()` calls store plain param dicts, not closures or
bound methods, so the whole `Sim` object pickles cleanly with nothing
silently dropped or reconstructed on load.

**Sharpest attack**: this is a code-reading argument, not an executed
verification, and this cycle shipped **zero** empirical check of it —
neither a bit-exact diff against a genuinely continuous run of comparable
size, nor a new trust-suite stage, despite PANEL.md's own Phase-4
discipline stating explicitly: *"new machinery ⇒ new suite stage with at
least one absolute identity gate BEFORE results are trusted."*
`chunk_runner.py`/pickling-mid-`Sim.run()` is unambiguously new machinery
— `grep -rn "pickle\|checkpoint\|resume"` across `lab/` and
`lab/validation/` returns **nothing**; this idiom has never been
suite-gated. The "independently re-run... to confirm bit-exact
reproduction" language in `run.py`'s own module docstring and NOTES.md's
Result section is a **self-consistency check of the chunked pipeline
against itself** (re-running `chunk_runner.py`+`finalize.py` a second
time and diffing), not a comparison against an uninterrupted run — it
would reproduce a bug in the chunking mechanism just as faithfully as it
reproduces correct behavior. **A genuinely free verification opportunity
existed and was not taken**: r=156 already ran single-shot this cycle
(~623s combined); routing it once more through `chunk_runner.py`'s own
checkpoint/resume path (3 chunks at `CHUNK_STEPS=2200`) and diffing
`sigma_abs`/`sigma_ext`/`core_frac` bit-for-bit against the already-banked
single-shot numbers would have cost perhaps 10–15 extra minutes against
this cycle's own ~110-minute spend and would have been a real, cheap,
in-cycle A/B test of the exact mechanism r=312's own numbers depend on.
It was not run.

**Would any check in this cycle's own record have caught a discontinuity
had one existed?** No, checked directly: **Gate P0** compares only
pre-`Sim.run()` geometry-dict fields (`N, CX, CY, SRC_X, STEPS, R_CORE,
R_COAT, sigma_max, tau_shell, behind, box_a, box_b, ref`) against
exp-106's committed values — it is a static-parameter check that executes
*before* any `Sim.run()` call and has no visibility into runtime field
state at all. **`box_dev`** and the **face-flux/cross-term identity** I
re-derived in §1 are both computed from the SAME single field snapshot at
each r — a systematic corruption shared identically by both boxes (or
both extinction routes) — e.g. a `step_count` off-by-`N` error shifting
the source's phase reference uniformly — would not show up as a
box-to-box or route-to-route disagreement, since both quantities are
computed from the identical (possibly-already-wrong) `Ez`/`Hx`/`Hy`
arrays. A step-accounting sanity check does exist implicitly (chunk
step-counts for r=312 sum to exactly `2200×5+1800=12800=STEPS(312)`,
confirmed by direct read of `run_output.txt`), which rules out a *gross*
under/over-run, but not a subtle phase-reference corruption of the kind a
`step_count` pickling defect could in principle cause. **This is an
unverified assumption, correctly reasoned about but not tested, sitting
under the one leg of this cycle's own two numeric FDTD results (r=312)
that also carries this cycle's most consequential new finding (Item 4's
26.8% floor-contamination figure, §2).**

## Verdict: **CONFIRM-WITH-GAPS**

The census retirement (Tier 0) is sound and outside my charter's
substance — I have no reciprocity/passivity objection to it. Item 3's
thermal-margin arithmetic and Item 1's headline PASS both reproduce
exactly from primitives, and I independently corroborate them with two
checks this cycle didn't run itself (`closure`, the two-route extinction
identity) — both pass cleanly, so nothing here overturns a scored
verdict. But two real, disclosed-or-discoverable gaps sit under the
record as filed: (1) the ledger's own `closure` field, standard practice
one cycle ago on this identical instrument, was silently dropped this
cycle (non-load-bearing, as I've now shown, but undisclosed as a gap in
NOTES.md itself); (2) the chunked checkpoint/resume execution path —
genuinely new machinery, plausibly exact by code-level reasoning, but
carrying zero empirical verification and zero suite-stage gate, under
exactly the r=312 leg this cycle's own most novel finding depends on.
Neither gap changes today's verdict; both are exactly the shape of gap
this program's own R6/R8/R16 lineage says should not go unclosed twice.

## The single most important thing for Iteration 85, from this seat

**Before r=312's checkpoint/resume path is reused again for any future
cycle, run the cheap, still-available A/B test this cycle skipped**: take
r=156's own already-completed single-shot article/empty pair, replay it
through `chunk_runner.py`'s pickled checkpoint/resume path (3 chunks),
and diff `sigma_abs`/`sigma_ext`/`core_frac`/`floor_gate` bit-for-bit
against the already-banked single-shot numbers. If they match to machine
precision (my own code-level analysis in §3 predicts they will), promote
`chunk_runner.py` to a named, suite-gated trust-suite stage (one absolute
identity gate: chunked-vs-continuous agreement on a cheap reference case)
so every future long-`STEPS` cycle inherits verified, not merely
argued-for, checkpoint/resume fidelity — closing this gap once, the way
this program has closed every other "plausible but unverified" gap in
its own RULED OUT registry, rather than re-arguing it from code each time
the idiom is reused.
