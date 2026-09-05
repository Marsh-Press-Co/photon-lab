# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 89 (exp-112)
## The cpl=25 Floor Spot-Check: The Cost-Gate Flip Confirmed Bit-Exact, the DISCLAIMER's "6–8 Orders" Corrected to "~2–4.5", Check C Shown to Have No Discriminating Power (Two Seats, Two Methods), the Second R29 Instance Ruled Non-Firing (Six-of-Six), Two New Standing Rules (R30, R31)

Charter (verbatim, PANEL.md): attacks every proposal, speaks last and
hardest. Standard is NOT textbook-physics compliance — speculation is
permitted. Kills internal inconsistency, unfalsifiable claims, mechanisms
that cannot be expressed as simulation parameters, and proposals that
quietly violate a target constraint — especially #3. Never leads a cycle;
has no proposal of its own to protect.

## 0. Framing and method

Read, in full: `PANEL.md`; `LOGBOOK.md`'s RULED OUT registry (R1–R29,
lines 1–1286) and the ESTABLISHED/LIVE THREADS sections; the T28 opening
(Iteration 46/exp-069, lines 2982–3040+); the Iteration 85–88 narrative
(exp-108/109/110/111, lines 8630–9088 and 23874–24101, the latter being
this file's own recovered narrative span after LOGBOOK's disclosed
Iteration-58–87 gap); the complete exp-112 record (`phase1_proposal.md`,
all five Phase-2 blind critiques, `phase2_redteam_audit.md`, `NOTES.md`,
`run112.py`, `chunk_runner112.py`, `analyze.py`, `results.json`); and all
six Phase-5 blind reviews (`phase5_review_{photonics,materials,em,
thermodynamics,quantum,vision}.md`).

This cycle is T1-N/A instrumentation (pure grid-resolution spot-check on a
named angular bin's own noise floor) — no constraint is scored, no
mechanism class is bounded. The task charter names three findings for
independent re-derivation from primitives (not restatement): (a)
THERMODYNAMICS' cost-gate-flip finding, (b) MATERIALS' "6–8 orders" vs
"~1.8–4.5 orders" arithmetic, (c) PHOTONICS'/QUANTUM's convergent
Check-C-not-diagnostic finding. All three independently re-verified below,
by direct code execution and from-scratch recomputation, before anything
else in this audit is trusted. **All three hold up exactly as the finding
seats reported — no correction to any of the three was needed.**

## 1. Re-verified from primitives — THERMODYNAMICS' cost-gate-flip finding

Located the real per-scene wall-time logs, still present in this session's
own scratch directory (`.../scratchpad/exp112/r156_cpl25_{empty,hollow,
peccored}_walltime.json`), and summed them directly — not taken from any
document's own prose:

```
empty:    221.5263090133667 s
hollow:   224.09255647659302 s
peccored: 224.85890436172485 s
total:    670.4777698516846 s   (matches results.json["total_wall_s"] bit-exact)
```

Imported `R.cost_gate_check` directly from `experiments/110-.../run.py`
(the real, unmodified, already-ratified R27/R28 function — not a
reimplementation) and invoked it twice, myself:

```python
R.cost_gate_check(221.5263090133667, 670.4777698516846)   # real pilot
-> {"pilot_pass": true, "kappa_ratio": 2.0, "kappa_exponent": 3.2053299988171697,
    "safety_margin": 1.1, "projected_312_total_s": 6802.6408688513,
    "total_pass": true, "proceed_to_r312": true}

R.cost_gate_check(221.5263090133667, 1469.186126254499)   # phase1_proposal.md's own
                                                            # pre-registered pilot
-> {"pilot_pass": true, "kappa_ratio": 2.0, "kappa_exponent": 3.2053299988171697,
    "safety_margin": 1.1, "projected_312_total_s": 14906.304184580222,
    "total_pass": false, "proceed_to_r312": false}
```

**Confirmed bit-exact, both directions.** Using the pre-registered,
cross-session-projected pilot (`cpl_cost_table.py`'s own `1469.19s`
extrapolation, the number `phase1_proposal.md` §2.0/§3 actually used to
scope this cycle to r=156-alone), the gate REFUSES. Using the real,
now-measured pilot from this cycle's own genuine FDTD spend, the SAME,
unmodified gate function APPROVES, with 37% margin (`6802.6s` vs.
`10800s`). **THERMODYNAMICS' finding is not merely plausible, it is a
bit-exact reproduction of what the real, committed `cost_gate_check()`
function outputs on the real data — the r=312 deferral is a scope decision
based on a projection that itself did not survive contact with real
data, not a scope decision the current numbers still support.**

Root cause independently re-traced. Per-scene wall time actually
*decreased* between `cpl=20` (exp-110, prior session: 250.6/250.1/251.5s)
and `cpl=25` (this cycle, this session: 221.5/224.1/224.9s) despite 1.953×
more raw cell-steps (`N` scales `ratio²=1.5625`, `STEPS` scales `ratio`, so
total cell-steps scale `ratio³=1.953`, confirmed: `320·S` optical periods
held fixed at both `cpl`, verified independently). The only accounting
that fits: this session's own compute throughput is roughly `1469.19/670.48
= 2.191×` that of exp-110's own prior session. A `cross_session_ratio` of
this size, silently absorbed into a pilot combining one session's baseline
with another session's fresh measurement, is a real, previously
undisclosed, and — checked directly against the full RULED OUT registry —
genuinely novel axis distinct from R28's own founding ~15% *exponent*-fit
miss (a systematic error in the geometric law itself, present even
within one session) and from R28's own causal-position concern (whether
the gate's branch sits upstream or downstream of the spend it purports to
control). Neither R27 nor R28, as ratified, requires a same-session
control point on the gate's own INPUT data. New standing rule ratified,
§7 below (**R31**).

## 2. Re-verified from primitives — the "6–8 orders of magnitude" DISCLAIMER claim

Re-implemented `lab/fdtd2d.py::_damping()`'s own ramp/exponential formula
from raw source (`ramp=(np.arange(absorb,0,-1)/absorb)**3`,
`damp_e=exp(-0.30*ramp)`, `S=0.32/√2`), independently, without reading
either MATERIALS' or EM's own arithmetic first:

```
discrete cell-sum:  sum(0.30*ramp)/S   absorb=40 -> 13.929451   absorb=50 -> 17.242357
continuum closed-form: -(0.3/4/S)*absorb            absorb=40 -> -13.258252  absorb=50 -> -16.572815
```

Bit-exact to both `phase1_proposal.md`'s own disclosed figures and Red
Team's own Phase-2 audit table — the log-attenuation numbers THEMSELVES
are genuinely correct, confirmed independently a third time. The DOWNSTREAM
step — exponentiating and comparing the result to the DISCLAIMER's own
stated `~1e-4`–`1e-3` measurement-floor scale — is what nobody in this
cycle's own chain (MATERIALS' Phase-2 critique, EM's Phase-2 critique, Red
Team's Phase-2 audit, Phase-3 synthesis) actually performed before
freezing "6-8 orders of magnitude below" into a permanent, doubly-asserted
(R23) DISCLAIMER string. Performed it directly, independently:

```
exp(-13.929451) = 8.923e-7    exp(-17.242357) = 3.249e-8    (discrete route)
exp(-13.258252) = 1.746e-6    exp(-16.572815) = 6.346e-8    (continuum route)
```

| cpl | route | factor | orders below 1e-4 | orders below 1e-3 |
|---|---|---|---|---|
| 20 | discrete  | 8.92e-7 | 2.05 | 3.05 |
| 25 | discrete  | 3.25e-8 | 3.49 | 4.49 |
| 20 | continuum | 1.75e-6 | 1.76 | 2.76 |
| 25 | continuum | 6.35e-8 | 3.20 | 4.20 |

**Bit-exact to MATERIALS' own table.** The true margin is **~1.8–4.5
orders of magnitude, not 6–8** — a ~100–1000× overstatement of the safety
margin, in a string a code-level assert makes authoritative and permanent,
quoted verbatim twice in `NOTES.md` and twice in `results.json`.
**Non-outcome-reversing**: the corrected margin (still several orders
above the ~10⁻¹-scale `9.88%`/`14.3%` relative-deviation signal actually
under test, and no r=312 leg exists this cycle to compound it) leaves the
qualitative "non-fatal" conclusion untouched. But the specific asserted
figure is wrong, and it is exactly the shape this program's R4/R9 lineage
exists to catch: a downstream comparison inherited from an unverified
back-of-envelope estimate (EM's own Phase-2 critique separately guessed
"~7+ orders"; MATERIALS' own Phase-2 critique separately guessed "~6-8
orders" — two independent guesses, never reconciled by actually computing
the number), riding on top of correctly-verified antecedent inputs, into a
permanent record. Same-shift fix applied, §6 below.

Checked EM's own adjacent finding (the "~1.25×... two independent routes...
agree bit-exact" language) against R4/R23's own text directly, per EM's own
Phase-5 review: **EM is correct that this is NOT itself R4/R23-class** —
the disclosed `13.93`/`17.24` figures are genuinely, independently
reproducible (confirmed a third time here); what is imprecise is only
which route's own ratio (`1.2500` exact, continuum; `1.2378`, discrete —
the one actually shown) gets attributed the "~1.25×" headline label, a
documentation-precision nicety, not a wrong number. Concur with EM: not a
rule violation, does not contribute to any Checkpoint tally.

## 3. Re-verified from primitives — Check C has no demonstrated discriminating power (PHOTONICS and QUANTUM, independently, by different methods)

Ran the identical `±2`-bin Pearson correlation `neighbor_correlation_check`
applies to the named bin (index 4) at **all 48** possible window
positions, using only the two committed arrays the document's own Check C
itself reads (`experiments/110-.../results.json["r156"]["raw_patterns"]
["32"]["delta"]` at `cpl=20`; `experiments/112-.../results.json
["pattern_delta"]` at `cpl=25`) — independently, from a from-scratch
script, before reading either PHOTONICS' or QUANTUM's own numbers:

```
48/48 windows clear corr>=0.5      46/48 windows clear corr>=0.9
median corr = 0.9952   min = 0.8169 (idx 35)   max = 0.9996 (idx 19)
named bin (idx 4): corr = 0.9993580404725309
```

**Bit-exact to PHOTONICS' own table.** Split by exp-110's own committed
RESOLVED/UNRESOLVED mask (`local_diag_margin32.resolved`, 34 resolved / 14
unresolved at `cpl=20`):

```
RESOLVED (n=34):   range [0.8169, 0.9996], mean 0.9793
UNRESOLVED (n=14):  range [0.9689, 0.9995], mean 0.9921
```

**Confirms QUANTUM's own finding closely** (QUANTUM reports mean `0.9916`
for the unresolved population; this independent recomputation gives
`0.9921` — a rounding-level difference, not a disagreement) — and the
qualitative point is unambiguous and independently reproduced: **the
UNRESOLVED population's own mean correlation is HIGHER than the RESOLVED
population's**, the opposite of what the check's own motivating premise
("a genuine deterministic sub-wavelength field feature... must imprint
correlated structure across several adjacent bins... uncorrelated Yee-grid
noise need not") predicts, and the single LOWEST correlation anywhere in
the pattern (`0.8169`, bin 35) sits in the RESOLVED — supposedly
"obviously real" — population, not the unresolved one. The named bin's own
`0.9994` reading is unremarkable against either population; it sits near
the middle of the unresolved population's own distribution, not in any
tail.

Independently confirmed the mechanism both seats name: `delta(θ)` is
dominated by the disk's own smooth diffraction envelope at BOTH
resolutions (full-48-bin correlation of `pattern_peccored(cpl20)` vs.
`pattern_peccored(cpl25)`, and the hollow equivalent: `0.99963` both),
so any `±2`-bin window correlates highly under a congruent mesh refinement
essentially everywhere, independent of whether that window's own absolute
magnitude clears the mirror-pooled-floor SNR test or not. **Check C, as
built, measures whether the local SHAPE of an already-smooth curve
persists under refinement — a property nearly guaranteed everywhere in
this pattern — not whether the fine-scale component Check A exists to
adjudicate (real near-field feature vs. staircase artifact) is present.**
A `corr≥0.5` bar that 48 of 48 sampled bins clear carries zero
discriminating power at the resolution this cycle needed it to operate at.

**This independently falsifies `NOTES.md`'s own Interpretation-section
language** ("a striking number for an independent grid refinement to
reproduce by chance... not obviously expected... by chance") — checked, a
purely-uninteresting bin elsewhere in the identical pattern (e.g. bin 0,
`local_snr≈0.04`, deep in the unresolved population) reproduces `0.9959`,
higher than the named bin's own `0.9994` is unusual relative to.
**Non-outcome-reversing** (the document's own scored disposition — no
"candidate real structure" claim, Check A never reached SURVIVES — is
unaffected, and is if anything more defensible once corrected, since the
one reading that looked like it might tip the balance is shown to carry no
information at all). Same-shift fix applied, §6 below. New standing rule
ratified, §7 (**R30**).

Also independently traced PHOTONICS' own further finding (the mechanism
behind why Check B and Check C both read favorably): a near-exact
`1.25×`(`=CPL_RATIO`) multiplicative discrepancy pervades every RAW
(non-ratio) quantity compared across `cpl=20`→`cpl=25` — the per-bin
pattern (`ratio_peccored` mean `1.2490`, `ratio_hollow` mean `1.2534`,
n=48) AND the newly-persisted `energy_ledger` (`sigma_scat`/`sigma_abs`/
`sigma_ext` ratios all `1.2497`–`1.2499`). Traced to `lab/sections.py::
_face_flux()`'s own docstring ("Returns the total outward power (grid
units)") — confirmed by direct source read: it sums `Re(E×H*)` over
Yee-index cells with no physical `dx` normalization anywhere in the
function, so summing over 25% more grid cells covering the identical
physical box perimeter (the congruent-refinement recipe holds the box's
PHYSICAL extent fixed) inflates every raw "grid-unit power" reading by
very nearly the cell-count ratio, independent of any real near-field
physics. **This is a genuine units/normalization artifact in a shared,
unmodified library function, not a defect this cycle's own geometry code
introduced** — and, checked against the historical record, this appears to
be the FIRST time this T28 sub-thread has ever compared RAW (non-ratio)
`sections.py` output across two different `cpl` values (every prior
resolution check compares a within-`cpl` ratio-type quantity, where a
common multiplicative factor cancels and stays invisible). Checked directly
against R9's own ratified text ("verifying that a cited ratio or
comparison reproduces arithmetically is not sufficient to verify the
comparison's own claim; the operands' commensurability... must be
independently confirmed"): **this is a fresh instance of R9's existing
principle, not a new failure category** — the operands here (raw
`sections.py` output at two different `cpl`) are not actually
commensurable without a `dx`/`cpl` normalization step nobody applied. R9
does not fire (the incommensurable comparison has not yet been filed into
a permanent LOGBOOK entry as "confirmed" — Check B/C's own readings were
reported honestly, hedged, not asserted as confirmed physics) but this is
squarely an R9-relevant finding, flagged for Iteration 90, §8 below.

## 4. The second R29 instance — definitive ruling: does NOT fire Checkpoint criterion 4

`NOTES.md`'s own Phase-4 section discloses, and explicitly declines to
self-adjudicate, a second manifestation of the identical import-collision
shape (`analyze.py`'s bare `import chunk_runner as CR` silently resolving,
via `sys.path` insertion order, to exp-110's own `chunk_runner.py` rather
than this directory's `chunk_runner112.py`) — found only at Phase 4, after
R29 had already been ratified at Phase 3 in the same shift. All six blind
Phase-5 reviews independently reasoned to the identical conclusion
(non-firing); this audit independently re-verifies the facts and the
reasoning from primitives before ruling.

**Facts, independently re-confirmed:**

- `git log`/`git show -s --format=%ci`: the Phase-1 commit (`b25ff99`)
  already contains BOTH collision-prone import patterns — `chunk_runner.py`
  AND `analyze.py` both doing `import run as R110` + `import run as R`
  (the first collision, caught at Phase 2), AND `analyze.py` separately
  doing `import chunk_runner as CR` against a directory that also holds
  exp-110's own `chunk_runner.py` (the second, caught at Phase 4) — both
  written in the SAME sitting, by the SAME author (QUANTUM OPTICS' own
  Phase-1 draft), from the IDENTICAL root cause (a bare same-basename
  import shadowed by this cycle's own `sys.path.insert(0, ...)` staging,
  copied from exp-110→exp-111's own established two-cycle convention
  without independently checking it against every file the new package
  introduces).
- Direct re-execution confirms the second collision was **structurally
  unreachable** at Phase 2: `chunk_runner.py`/`analyze.py` both crash with
  `AttributeError` on their own FIRST `R.`-attribute access (before
  `time.time()`, before any `Sim` construction) — no amount of re-running
  either crashing file surfaces a bare-import line that sits further down
  the same file, un-executed because the interpreter never reaches it.
  This is a **detection-ordering artifact**, not a defect that survived a
  review layer capable of catching it.
- The rule (R29) was proposed by Red Team's own Phase-2 audit and ratified
  by the Director at Phase 3, `19c4ac8` (03:44:37 UTC) — strictly BEFORE
  Phase 4 (`e2d660f`, 04:01:23 UTC) discovered the second collision.
  R29's own founding-instance text names "exp-112 (this cycle)" as the
  whole founding instance — not one file-level event within it.
- Both instances were caught, disclosed, and fixed in the SAME governance
  cycle, before any check's outcome was scored, before Phase 5, before any
  external citation ever treated Fix 1 alone as having closed the hazard.

**Ruling, checked element-by-element against R29's own ratified text and
this registry's own unbroken precedent for founding-instance treatment:**

1. **Root cause is singular, not repeated.** Both collisions trace to one
   authoring decision, made once, in one sitting, before R29 existed even
   as an idea (it was proposed IN RESPONSE to the first collision). R29's
   forward clause exists to deter a cycle that reuses a *known, avoidable*
   hazard after the rule could have warned it off — it structurally cannot
   apply to code written before the hazard was named.
2. **Every rule in this registry, without exception, treats a founding
   cycle's own multiple manifestations of a newly-named shape as one
   founding instance, not a founding-plus-second-instance pair** — R18
   (two independent, unrelated defects in one six-check gate, one founding
   cycle); R19 (the identical call-count/row-count conflation recurring
   TWICE in the same document, one founding case); R20 (exists precisely
   because within-cycle density is its own distinct, materially-harder-bar
   measure, set apart from every other rule's single-instance model); R21
   (explicitly declines to fire on EITHER of its own two founding
   instances); R23 First Addendum (its own two-builder asymmetry, one
   consolidating instance). Applying that same, unbroken convention here:
   exp-112 is one founding instance of the R29 shape, entitled to the same
   immunity every prior rule extends its own founding cycle.
3. **A hyper-literal Phase-3-precedes-Phase-4 timing reading is
   considered, and rejected** — "after this rule is on the books" is the
   phrase every prior rule uses to mean "known to a FUTURE cycle's own
   authors before they wrote new code," not "chronologically later within
   the same shift that names the hazard." Adopting the hyper-literal
   reading here would be a new, inconsistent precedent, not an application
   of an existing one — and would produce a perverse incentive (a cycle
   that discovers and ratifies a new rule becomes MORE exposed to
   instantly tripping it than one that never named the hazard, for
   exposing more of its own scope in the same sweep).

**Ruling: the second R29 instance does NOT fire Checkpoint criterion 4.**
It is the same founding instance's own second, previously-unreachable
manifestation of one root cause, discovered and fixed within the cycle
that also proposes, ratifies, and fixes the founding instance — not a
future cycle's reuse of a known, avoidable hazard.

**Textual addendum ratified, closing the ambiguity for future
adjudication** (all six Phase-5 seats independently recommended some form
of this; adopting THERMODYNAMICS'/VISION's own most precisely-scoped
phrasing): R29's own forward-firing clause is tightened, in place, in the
RULED OUT registry:

> **R29 addendum (ratified this audit, Iteration 89's own consolidating
> instance):** "a second instance... after this rule is on the books"
> means a **future cycle's** own reuse of the collision-prone idiom, or a
> later, separately-reviewed change, after that cycle's own authors had
> the opportunity to consult this registry — not a second, previously-
> unreachable manifestation of the identical root cause, discovered and
> fixed within the SAME cycle that proposes, ratifies, and fixes the
> founding instance, before any result is scored. Does not fire on its own
> founding instance (exp-112), matching every prior rule's own precedent.

## 5. Other findings independently re-verified, no correction needed

- **EM's F2 (the energy-ledger tautology; `sigma_ext_cross` silently
  dropped).** Re-read `lab/sections.py` directly: `"sigma_ext": (p_scat +
  p_abs) / i_inc` — confirmed, `sigma_ext` is *defined* as the sum, so
  `sigma_scat+sigma_abs==sigma_ext` is guaranteed by construction and
  proves nothing about correctness. `widths()` also computes
  `sigma_ext_cross = p_ext_cross/i_inc` (`p_ext_cross=-_cross_flux(pi,ps,
  box)`, a structurally independent interference/optical-theorem route) —
  confirmed present in `analyze.py`'s own in-memory `w_p`/`w_h` dicts but
  absent from the persisted `energy_ledger`. Independently confirmed
  exp-110's own committed `results.json` DOES persist this exact field
  (`grep` against `experiments/110-.../results.json`: present at
  `reproduction_precondition/widths/sigma_ext_cross`, both r) — exp-112
  broke that established continuity. THERMODYNAMICS' own self-review
  independently re-derived the real cross-check (`sigma_scat+sigma_abs`
  vs. `sigma_ext_cross`, agreeing to `6.65×10⁻⁶` relative at both configs)
  from the raw captures — reproduced here exactly:
  `sigma_ext_cross`(peccored)=`700.1129451080386`,
  (hollow)=`700.1279759823958`. Checked against R16's own ratified text
  (scoped specifically to NETD/thermal-sidecar `_full` fields) — does not
  literally fire (different field family, no disclaimer here claims
  `sigma_ext_cross` coverage the way R16's shape requires) — but the
  underlying principle (an already-established cross-check field, once
  persisted for a family in one cycle, silently dropped in a later cycle
  reusing the same underlying function) is the same spirit. Non-blocking
  (T1 N/A, Docket Fix 6 was explicitly "not load-bearing"). **Same-shift
  fix applied**, §6 below — restores `sigma_ext_cross` to the persisted
  ledger, zero marginal FDTD cost (already computed, discarded).
- **VISION's Fix 4/Fix 5 re-verification.** Independently re-ran
  `analyze.py` fresh against the raw `.pkl` captures still present in this
  session's own scratch directory; the regenerated `results.json`
  (pre-this-audit's-own additive fix) reproduced the previously-committed
  file byte-for-byte. Confirms VISION's own finding to a second,
  independent standard.
- **F1/F2's own "does this fire R4/R20?" classification.** Checked
  directly: the "6-8 orders" claim (§2) is R4/R9-shaped (a downstream
  arithmetic step nobody performed, riding on correctly-verified
  antecedents into a permanent asserted string) but is a DERIVATION gap,
  not literally "a citation failing to reproduce from its own cited
  source" in R4/R20's narrowest sense. The Check-C Interpretation overclaim
  (§3) is closer to R8/R9's shape (an unverified claim, checkable at zero
  marginal cost, never checked before being frozen) than to R4's literal
  "figure/citation/label/coincidence" text, though it does resemble R20's
  own founding "false coincidence" example closely enough to be a
  defensible R20-adjacent read either way. Tallied conservatively below,
  §7.

## 6. Same-shift fixes applied (this audit, verified by direct re-execution — zero re-run of any FDTD, zero verdict-arithmetic change)

1. **`analyze.py`**: restored `sigma_ext_cross` to `energy_ledger` (both
   configs) — zero marginal FDTD cost, already computed by `sc.widths()`.
   Re-ran `analyze.py` fresh against the raw captures still present in
   this session's own scratch directory; diffed the regenerated
   `results.json` against the pre-fix committed file field-by-field:
   **exactly two additions, nothing else changed**
   (`energy_ledger.peccored.sigma_ext_cross=700.1129451080386`,
   `energy_ledger.hollow.sigma_ext_cross=700.1279759823958`, matching
   THERMODYNAMICS' own independently-derived figures bit-exact).
2. **`run112.py`**: a corrective code comment added directly above the
   live `DISCLAIMER` constant, naming the "6-8 orders" error and the
   correct `~2-4.5 orders` figure, and instructing any future cycle that
   extends this string (the `DISCLAIMER`→`DISCLAIMER_88`-style idiom) not
   to propagate the uncorrected figure forward. The `DISCLAIMER` string
   ITSELF is left unmodified — it is already byte-frozen into this
   cycle's own committed `results.json`; verified directly that
   `run112.py`'s own `DISCLAIMER` still matches `results.json`'s
   persisted text fields exactly after this edit (a comment-only change).
3. **`NOTES.md`**: three blockquoted, attributed corrections — (a) at
   Phase 3's Fix-2 disposition, the "6-8 orders" arithmetic error and the
   corrected ~1.8–4.5-orders table; (b) at the Interpretation section, the
   Check-C "striking/not expected by chance" overclaim, with the all-48-
   bin calibration data and the RESOLVED/UNRESOLVED population split; (c)
   at the Combined Verdict, this audit's own ruling (PARTIAL confirmed,
   R29 second-instance non-firing, R30/R31 ratified, zero Checkpoint
   criteria fire).
4. Trust suite re-confirmed green after all patches: **43/43, 110s**
   (current suite size — the `stage26` count established at Iteration 87
   plus growth since; zero `lab/` diff throughout, confirmed by `git
   status --short lab/`). `git status --short` confirms the diff is
   scoped to exactly `analyze.py`, `results.json`, `run112.py`, `NOTES.md`
   — no other file touched.

## 7. New standing rules ratified

**R30 — an adopted, uncalibrated discriminating-instrument threshold must
be checked against its own already-computable null/background population
before its reading is cited with evidentiary language in Result/
Interpretation prose — not merely before it gates a pre-registered
classification (not a ruled-out idea; a standing house-discipline rule,
proposed independently and convergently by PHOTONICS and QUANTUM at Phase
5, by two different methods, ratified by Red Team's Phase-5 final audit,
Iteration 89).** Distinguished from the existing uncalibrated-threshold
lineage: R5/its exp-070 addendum concerns a dense NAMED-CONSTANT SEARCH
needing a null-permutation control; R10 concerns a FREE-PERIOD/FREE-PHASE
FIT needing a circular-shift-on-real-data null; R17 concerns a
TOLERANCE/BRACKET sized to test whether a feature has MOVED, needing
justification against an *already-on-file* comparable magnitude BEFORE
the run. None of these literally covers this shape: a freshly-built
discriminating STATISTIC (a spatial correlation, not a search, fit, or
bracket) whose calibrating data (the OTHER 47 bins of the identical
pattern) did not exist until AFTER the run that motivated the check, and
which — once it did exist — was never checked before the statistic's own
reading was described with strong evidentiary language ("striking," "not
expected by chance") in frozen prose. Founding instance: exp-112's own
`neighbor_correlation_check` (`corr≥0.5`, an illustrative "e.g." offered
in PHOTONICS' own Phase-2 critique, adopted verbatim into Red Team's own
Phase-2 mandatory-fix docket) — independently shown, by two Phase-5 seats
via different routes (an exhaustive 48-window scan; a RESOLVED/UNRESOLVED
population split), to clear its own bar at 48 of 48 sampled bins (median
`0.9952`), with the UNRESOLVED population's own mean correlation HIGHER
than the RESOLVED population's — the opposite of the check's own
motivating premise. **Rule: once the calibrating data for an
adopted-verbatim, uncalibrated discriminating threshold becomes available
(even if it did not exist when the threshold was chosen), it must be
checked — e.g. against the instrument's own reading at other, independently
labeled cases in the same dataset — before that threshold's reading is
used with evidentiary/interpretive language ("striking," "in tension
with," "would not be expected by chance") in any Result or Interpretation
section.** A future cycle that cites such a reading evidentially without
this check, when the check later shows the threshold has no demonstrated
discriminating power, fires Checkpoint criterion 4 automatically — a
single-instance-ratified, forward-firing model, matching R16/R21–R29's own
precedent. **Does not fire on its own founding instance** (exp-112),
matching every prior rule's own precedent — caught blind, same cycle
(independently, by two seats), before LOGBOOK, corrected same-shift (§6).
Full record: this document, §3.

**R31 — a wall-time-based cost-gate projection that combines pilot data
measured in two different execution sessions must include a same-session
control point (re-timing one already-completed, cheap scene at the start
of the new session and scaling by the ratio to its own historical figure)
before its output is trusted for a scope-limiting decision (not a
ruled-out idea; a standing house-discipline rule, proposed by
THERMODYNAMICS' own Phase-5 self-review, independently re-verified and
ratified by Red Team's Phase-5 final audit, Iteration 89).** Distinguished
from R27 (a numeric gate must be enforced by executable code, not merely
referenced in prose) and R28 (a gate satisfying R27 must sit causally
upstream of the spend it purports to control): both concern the gate's own
POSITION and ENFORCEMENT; this concerns the gate's own INPUT DATA. Founding
instance: exp-112's own r=156/`cpl=25` scope decision — `cpl_cost_table.py`'s
own `ratio**3` extrapolation, combining exp-110's real `cpl=20` baseline
(a PRIOR session) with this cycle's OWN `cpl=25` pilot (projected, not yet
measured), predicted `1469.19s` total; the REAL measured total, once this
cycle's own genuine FDTD spend completed, was `670.48s` — `45.6%` of the
projection, a `>2×` miss. Independently re-invoking the real, unmodified
`R.cost_gate_check()` with the real pilot flips its own r=312-expansion
decision from REFUSED (`14906.3s` projected vs. `10800s` bound) to APPROVED
(`6802.6s` vs. `10800s`) — confirmed bit-exact, §1 above. Root cause,
independently traced: this session's own compute throughput is
`~2.19×` exp-110's own prior session's — a genuine, previously undisclosed
cross-session machine-speed confound, larger than R28's own founding ~15%
exponent-fit miss, and checked directly against the full RULED OUT
registry text (no prior entry names "cross-session," "machine speed," or
"hardware" anywhere). **Rule: before trusting any wall-time-based cost
projection or gate decision that combines pilot/baseline data measured in
two different sessions, re-time one already-completed, cheap scene (e.g. a
fresh `cpl=20`/r=156/empty run) at the start of the new session, and scale
the cross-session baseline by the ratio of that control time to its own
historical figure, before combining it with the new session's own pilot in
any gate decision.** A future cycle that ships a cross-session cost
projection or gate decision without this control, when the projection
later proves off by a factor comparable to or larger than this cycle's own
`2.19×` finding, fires Checkpoint criterion 4 automatically — a
single-instance-ratified, forward-firing model, matching R16/R21–R30's own
precedent. **Does not fire on its own founding instance** (exp-112),
matching every prior rule's own precedent — the gate's own conservative
miss (over-, not under-, estimating the cost) meant no unsafe spend
actually occurred; the deferral it produced was merely more cautious than
the real numbers required, caught and disclosed by THERMODYNAMICS' own
self-review before LOGBOOK. Full record: this document, §1.

No third new rule is warranted. PHOTONICS' `_face_flux()` normalization
finding (§3) is a fresh instance of R9's EXISTING principle, not a new
category (§3, above) — flagged for Iteration 90, not separately ratified.

## 8. Checking every other candidate against R1–R29's own operative text

- **R4/R9 (documentation defects surviving freeze)**: the "6-8 orders"
  claim (§2) and the Check-C Interpretation overclaim (§3) are each
  independently R4/R8/R9-adjacent, caught only at Phase 5. Neither is a
  clean, unambiguous R4/R20 "citation/figure/label/coincidence fails to
  reproduce from its own source" instance in the narrowest sense (§5) —
  conservatively tallied, **R20's own tally for this document is 1–2, one
  to two short of "three or more" — does NOT fire.** This continues (does
  not newly cross) the established pattern this exact T28 governance
  sub-thread has shown for FIVE consecutive cycles now (exp-108 tally 2,
  exp-109 tally 2, exp-110 tally 2, exp-111 tally 2, exp-112 tally 1–2 by
  this audit's own conservative count) — named explicitly, as a standing
  observation, not a rule violation: **a future Red Team audit may wish to
  consider whether R20's own hard "three or more" bar, now approached-but-
  not-crossed for five consecutive cycles running, still correctly
  separates genuine density from this sub-thread's own baseline rate of
  one-to-two independently-caught documentation slips per cycle** — this
  audit does not ratify a change to R20's own bar, reasoning (matching
  Iteration 88's own identical restraint) that R20 is a deliberately hard
  density threshold and a "trending toward 3" test would be exactly the
  kind of inference-stretching this seat's charter exists to resist.
- **R6/R7/R8**: not applicable (no fitted estimator, no un-fit design
  conditioning claim scored this cycle). R8's own forward clause
  specifically requires the untested argument later prove
  OUTCOME-DETERMINING — the Check-C overclaim (§3) does not (both
  PHOTONICS and QUANTUM confirm non-outcome-reversing) — so R8 does not
  fire even under the more generous reading.
- **R9**: discussed above (§3) — a fresh, non-firing instance/extension
  (the incommensurable raw cross-`cpl` comparison has not reached a
  permanent LOGBOOK entry as "confirmed").
- **R10–R12, R15**: not applicable (no free-period/free-phase fit, no
  tail-statistic "negligible" claim, no cross-resolution caution-zone
  reclassification scored this cycle). This cycle's own DISCLAIMER
  correctly, explicitly invokes R15's own two-point caution rather than
  overclaiming continuum convergence.
- **R13/R14**: not directly invoked — no ratio classifier built on a
  zero-crossing-capable denominator or subtractive-cancellation numerator
  was scored against a threshold this cycle (Check A's own `local_snr`
  denominator, `floor`, is confirmed strictly positive and orders of
  magnitude from any degenerate case at both `cpl`, matching R13's own
  established non-firing precedent for data that has never triggered it).
- **R16/R21**: the `sigma_ext_cross` omission (§5) does not literally fire
  either — R16's own forward clause is scoped to NETD/thermal-sidecar
  `_full` fields specifically, and no disclaimer here claims
  `sigma_ext_cross` coverage the way R16's shape requires (nothing was
  misrepresented; the field was simply, silently, never asked for by
  Docket Fix 6's own text). Same-shift fix applied (§6) rather than a rule
  firing.
- **R17/R18/R19**: not applicable in their literal forms this cycle (no
  node-bracketing tolerance, no multi-check scope-overclaim gate, no
  call-count/row-count conflation). R30 (§7) supersedes R17 as the correct
  home for the CORR_BAR finding, for the reasons stated there.
- **R22–R28**: not applicable (no frozen vector self-consistency identity,
  no multi-section disclaimer requiring R23's own assert-pairing — R23
  itself IS honored cleanly this cycle, both `assert DISCLAIMER in ...`
  calls present and independently re-confirmed firing on real execution by
  THERMODYNAMICS, VISION, and this audit; no Phase-2 mandatory-fix
  consequence left unwired, R24; no audit-identified fix dropped from a
  numbered queue item, R25; no dangling forward cross-reference, R26 — the
  Idealizations section's own "See phase1_proposal.md §5" pointer resolves
  to real content, confirmed by direct read; the R27/R28 cost gate is
  correctly invoked, forward-looking, non-blocking, and its own known
  ~15%/`kappa_ratio`-exponent bias is separate from and does not mask
  §1's own cross-session finding).
- **R29**: ruled definitively, §4 above — does not fire, textual addendum
  ratified.

**Checkpoint criteria, checked element-by-element against PANEL.md's own
five-item list:**

1. **A configuration passes ALL constraint metrics** — N/A. No constraint
   metric is scored; T1 is structurally N/A, confirmed independently by
   every reviewing layer including this one.
2. **A proven boundary (constraint subset jointly unsatisfiable)** — N/A,
   same reason.
3. **A synthesis requires engine physics beyond validated bench classes**
   — does NOT fire. Zero `lab/` diff (confirmed by `git status --short
   lab/`, empty, both before and after this audit's own same-shift
   fixes); trust suite re-confirmed green, 43/43, both before and after.
4. **Red Team flags program-integrity drift** — the question this audit
   exists to answer. Checked against every finding individually (§§1–5,
   8, above): the second R29 instance does not fire (§4, six-of-six
   unanimous); R20's own density tally is 1–2, short of 3 (§8); R8/R9 do
   not fire (outcome-determining/permanent-record preconditions unmet);
   R16 does not literally cover the `sigma_ext_cross` gap. **No Checkpoint
   criterion fires this cycle.** The two genuinely new findings (Check-C's
   own null-calibration gap; the cross-session cost-gate confound) are
   ratified as new standing rules (R30, R31, §7) rather than firing
   anything retroactively — both correctly non-firing on their own
   founding instances, matching this registry's unbroken convention.
5. **Two consecutive iterations with no logbook-advancing result** — does
   NOT apply. This cycle lands a real, independently-verified new
   physical data point (the `cpl=25`/r=156 spot-check itself, genuinely
   executed, three real FDTD calls) plus a governance-consequential
   finding (the cost-gate flip) that directly changes the affordability
   calculus for Iteration 90's own headline next step — real forward
   motion on both the physics and the governance ledger, not stagnation.

## 9. Overall verdict and Combined Verdict label

**Overall verdict: CONFIRM-WITH-GAPS, matching the six-of-six blind
Phase-5 seats' own near-unanimous landing** (five of six explicitly used
this label or its PARTIAL equivalent; all six independently re-derived
every object-level numeric claim from primitives and found the underlying
instrumentation genuinely sound where checkable). Every consequential
finding this audit was tasked with independently re-verifying (the
cost-gate flip; the "6-8 vs ~2-4.5 orders" arithmetic; the Check-C
null-calibration gap) reproduces bit-exact from primitives, exactly as the
finding seats reported — no correction to any of the three substantive
findings was needed, only to the frozen prose built on top of one of them
(§2) and to one Interpretation claim built on another (§3), both now
same-shift-corrected (§6).

**Combined Verdict (LOGBOOK-level vocabulary): PARTIAL.** Not RULED OUT —
T1 is correctly, structurally N/A throughout (confirmed independently by
every layer), and the named bin is not shown to be pure noise (Check B
genuinely SURVIVES; Check C's own high correlation, though non-diagnostic
per §3, is not evidence AGAINST real structure either — it is simply
uninformative). Not PROMISING — Check A, this cycle's own primary,
pre-registered instrument, stays genuinely AMBIGUOUS (both `local_snr`
readings sit 6–7× below even the permissive K=1 bar), and a real,
independently-confirmed documentation-arithmetic error (§2) plus a
real, independently-confirmed interpretive overclaim (§3) both survived
Phase-3/4 freeze into permanent text, caught only at Phase 5 — denser than
a clean landing carries, though neither is outcome-reversing and both are
now corrected. This continues, unbroken, this exact T28 governance
sub-thread's own established pattern: every cycle since Iteration 82 has
landed PARTIAL. Real, disclosed, independently-reproduced progress stands
alongside the gaps: this is the first genuinely new FDTD data this
long-deferred spot-check has ever produced; the geometry-scaling recipe's
material-parameter invariance (`tau_shell`) is independently confirmed to
hold in real data to <0.01% (MATERIALS' F2); the module-collision defects
(both instances) are genuinely, verifiably fixed, re-confirmed by
independent re-execution; R23 compliance is genuinely clean, re-confirmed
by three independent parties; and the cost-gate re-invocation (§1) hands
Iteration 90 a concretely unblocked, affordable next step that did not
exist before this cycle ran.

## 10. Reconciled Iteration-90 queue

**Tier 0** — (0a) rule on the Iteration-85 Checkpoint-4/R24 firing at the
next convened checkpoint (unchanged, still Marsh's own call, still
pending — five cycles now); (0b) ratify or reject the R23 First Addendum
(Iteration 88, still pending); (0c, new this audit) ratify or reject R30
and R31 (proposed and provisionally ratified by this audit, per this
program's own established Phase-5-final-audit-proposes-and-adopts
practice — ratification is final unless a future Director/Marsh session
reverses it).

**Tier 1** — (1) **re-invoke `R.cost_gate_check()` with the real,
now-measured `cpl=25`/r=156 pilot (already done, §1 — `proceed_to_r312=
True`, 37% margin) and execute the `+168.75°` bin at r=312/`cpl=25` with
the SAME three-check instrument used here, before treating the r=312
deferral as still gate-bound** — the single highest-value item on this
queue: genuine new FDTD (predicted, from `cpl_cost_table.py`'s own
r=312/`cpl=25` column, `13551.19s`≈3.76h for the r=312 leg alone, or
`15020.37s`≈4.17h for both r together — still needs its own fresh,
same-session pilot re-measurement per R31, not assumed to transfer
unchanged from this cycle's own r=156 figures); (2) apply R31's own
same-session-control discipline to that new pilot BEFORE trusting its own
projection; (3) recalibrate or replace Check C's own `corr≥0.5` bar with
the R30-mandated null-calibrated version (percentile/z-score against this
cycle's own 48-window background distribution, already computed, zero
marginal cost, directly reusable) before it is applied to the r=312 leg;
(4) diagnose and either normalize (a `dx`/`cpl` correction to
`lab/sections.py::_face_flux()`) or explicitly bound the `CPL_RATIO`
raw-magnitude confound (§3/PHOTONICS' F3) before any future RAW
(non-ratio) cross-`cpl` `sections.py` comparison is trusted — zero new
FDTD, a desk check against already-committed data.

**Tier 2** — a third, differently-scaled resolution point (`cpl=30`,
already costed in `cpl_cost_table.py`) for the named bin, per R15's own
two-point-insufficiency discipline — but only AFTER Tier-1 items 3–4 are
resolved, so a third raw data point does not simply repeat the same
uncalibrated-Check-C/un-normalized-`_face_flux` confounds a third time;
state MATERIALS' own F2 cross-cpl `abs_ext_ratio` agreement (<0.1%)
explicitly in a future Result section (already computed, zero marginal
cost); the long-outstanding `R2_SMOOTH_THRESHOLD=0.90` re-derivation (now
a SIXTH consecutive cycle naming it undone); MATERIALS' own
fabrication-tolerance quantitative bound (now a FIFTH consecutive cycle
naming it undone); the sixth `gate_reposition_control.py` checkpoint-resume
case (Iteration-88's own carried item, still outstanding).

**Tier 3 — unchanged standing items**: the oblique-angle extension; the
750/450nm leg; the `G40` full-width leg; the x-wall admittance refit;
`PAD`-with-article survival; `box_dev`'s own thinning margin (~9.0× at
r=312, still unresolved).

## 11. Ranked top-3 candidate next-step list for Iteration 90's own queue

1. **Re-run the r=312/`cpl=25` cost gate with a fresh, same-session pilot
   (R31 discipline) and, if it clears, execute the `+168.75°` companion
   bin with the SAME three-check (A/B/C, R30-calibrated) instrument.**
   This is the single most consequential, concretely unblocked physics
   step this sub-thread has queued in several cycles — the cost-gate flip
   this audit independently confirmed (§1) removes the specific,
   code-derived reason (`proceed_to_r312=False`) that has justified
   deferring this exact leg twice already, and it is the only way to learn
   whether the −146.25° bin's own genuinely inconclusive (Check A
   AMBIGUOUS) reading generalizes to its r=312 mirror bin or is
   scale-specific.
2. **Normalize or explicitly bound `lab/sections.py::_face_flux()`'s own
   `CPL_RATIO`-scale raw-magnitude artifact (§3) before trusting Checks
   B/C's own evidentiary basis further, and recalibrate Check C per R30.**
   Zero new FDTD, a desk check against already-committed data, and the
   single item most likely to change whether Check B's "SURVIVES" reading
   means anything once its own confound is accounted for.
3. **A third, differently-scaled resolution point (`cpl=30`, already
   costed) for the named bin at r=156**, once items 1–2 above are
   resolved — the R15-disciplined minimum needed to move this bin's own
   status past "not yet ruled out, not yet confirmed" into a genuine
   convergence-or-artifact call, and the natural companion leg to item 1's
   own r=312 extension.

## 12. Summary table

| Finding | Independently re-verified? | Classification | Fires anything? |
|---|---|---|---|
| Cost-gate flip: real pilot (670.48s) APPROVES r=312 where the projected pilot (1469.19s) REFUSED it (THERMODYNAMICS) | **CONFIRMED bit-exact**, both directions, real `R.cost_gate_check()` invoked directly | New failure axis: cross-session pilot-data confound | New **R31** ratified; does not fire on founding instance |
| DISCLAIMER's "6-8 orders of magnitude" vs. true ~1.8-4.5 orders (MATERIALS) | **CONFIRMED**, bit-exact to MATERIALS' own table, independently re-derived a third time | R4/R9-adjacent documentation defect | R20 tally +1 (of 1-2 total, conservative count) |
| Check C (`corr=0.9994`) has no discriminating power — 48/48 bins clear the bar, UNRESOLVED mean > RESOLVED mean (PHOTONICS, QUANTUM — independent methods) | **CONFIRMED**, bit-exact/near-exact to both seats' own figures, independently re-derived from scratch | New failure axis: uncalibrated discriminator threshold | New **R30** ratified; does not fire on founding instance; R20 tally +0-1 (Interpretation overclaim, conservatively counted) |
| `sigma_ext_cross` silently dropped from `energy_ledger`, breaking exp-110's own established persistence convention (EM) | **CONFIRMED** — present in `widths()`'s own return dict, absent from the persisted ledger, present in exp-110's own committed `results.json` | Non-blocking; R16-adjacent, does not literally fire (different field family) | Same-shift fix applied (§6); no rule fires |
| Second R29 collision instance (`chunk_runner.py`/`chunk_runner.py`, Phase 4) | Facts independently re-confirmed via `git log`/direct execution | Same founding instance's own second manifestation, not a future-cycle reuse | Does NOT fire, ruled definitively (six-of-six unanimous); R29 textual addendum ratified |
| `_face_flux()`'s un-normalized `CPL_RATIO` raw-magnitude artifact (PHOTONICS) | **CONFIRMED**, traced to source, bit-exact ratios (~1.2497-1.2534) across three independent quantities | Fresh instance of R9's existing principle | Does not fire (not yet filed as a "confirmed" comparison in a permanent record); flagged for Iteration 90 |

**Checkpoint criterion 4: does NOT fire.** **Combined Verdict: PARTIAL,
confirmed.** **Two new standing rules ratified (R30, R31), one textual
addendum to R29 ratified, three same-shift fixes applied (§6).**
