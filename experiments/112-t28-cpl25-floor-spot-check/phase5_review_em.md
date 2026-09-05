# exp-112 — Phase 5 Review — ELECTROMAGNETISM (blind)

Charter: field/wave behavior, impedance matching, energy coupling;
reciprocity/passivity/causality bookkeeping — what T1 permits and forbids.
Read blind, fresh context, independent of any other seat's Phase-5 output
this cycle. All findings below are independently re-derived from primitives
(raw `results.json` arrays, `lab/sections.py`/`lab/fdtd2d.py` source,
committed critique/audit text) — none are restated from any document's own
printed flags or summary language without recomputation.

## Verdict: PARTIAL — concur with the cycle's own Combined Verdict

T1 route N/A confirmed structurally (this cycle touches only a congruent
grid-resolution refinement, a checkpoint/resume driver, and two
already-existing classification functions — no σ(I)/σ(x,t)/angular-
selectivity/sub-threshold content anywhere). Not RULED OUT (Check B and
Check C both lean toward "not yet ruled out," genuinely, not manufactured).
Not PROMISING (Check A — the cycle's own primary, pre-registered
instrument — independently re-verified below to read exactly AMBIGUOUS,
never reaching SURVIVES). Zero Checkpoint criteria fire under my own
reasoned reading of the one open adjudication question this cycle
explicitly left to Phase 5 (§3, below) — though I flag that reading as a
judgment call, not a mechanical certainty, and recommend it be made
explicit in LOGBOOK rather than left implicit.

## Findings

### F1 — Docket Fix 2's disclosure text carries only MATERIALS' numbers, never EM's own; the attached "agree bit-exact" / "~1.25×" language overstates cross-route agreement (minor, non-blocking, disclosed here for the first time)

**Re-derivation performed:** I independently recomputed both attenuation-
exponent routes from `lab/fdtd2d.py`'s own `_damping()` formula, not
trusting either document's printed figures:

```
discrete cell-sum (MATERIALS' route): sum(0.30*(arange(absorb,0,-1)/absorb)**3)/S
  absorb=40 (cpl=20): 13.929451   absorb=50 (cpl=25): 17.242357   ratio = 1.2378
continuum closed-form (my own route, phase2_critique_em.md):  -(0.3/4/S)*absorb
  absorb=40 (cpl=20): -13.258252  absorb=50 (cpl=25): -16.572815  ratio = 1.2500 (exact)
```
(`S = 0.32/√2` both routes.) Both reproduce Red Team's Phase-2 audit table
bit-exact (§1) and my own Phase-2 critique bit-exact.

**What I checked, per your instruction:** whether Docket Fix 2's disclosure
text — `phase1_proposal.md` §5's corrected Idealizations paragraph,
`run112.py`'s own `DISCLAIMER` string, and (since NOTES.md's Predictions/
Result blocks are verbatim quotes of `build_predictions_text()`/
`build_result_text()`) NOTES.md itself — matches my own (EM's) numbers
exactly. **It does not.** All three surfaces state only "13.93 (cpl=20,
absorb=40) to 17.24 (cpl=25, absorb=50)" — MATERIALS' discrete-cell-sum
figures. My own closed-form continuum figures (`-13.26`/`-16.57`) appear
nowhere in any of the three single-source-of-truth disclosure surfaces —
only in `phase2_critique_em.md` and the internal cross-check table inside
`phase2_redteam_audit.md` §1.

**This is not a rule violation.** The mandatory-fix docket's own Fix-2 text
(`phase2_redteam_audit.md` §3, row 2) explicitly offered an either/or:
"either the closed-form continuum route... or the discrete cell-sum
route... state which convention." The Director made a valid, disclosed
choice within that latitude — this does not fire R23 (the single-source-
of-truth string is used consistently, byte-identical, in both predictions
and result text) or R4 (the 13.93/17.24 figures themselves are correct and
independently reproducible).

**What I do flag:** the surrounding characterization overstates the
relationship between the two routes. `phase1_proposal.md`'s own corrected
text calls this "a real, computed ~1.25× change (two independent
derivation routes... agree bit-exact)," attributed jointly to "MATERIALS'/
ELECTROMAGNETISM's own independently convergent finding." But the two
routes' own raw ratios do **not** agree with each other: the continuum
route (mine) is exactly 1.2500×; the discrete-cell-sum route (MATERIALS',
the one actually shown) is 1.2378×, a ~1% difference — MATERIALS' own
Phase-2 critique correctly and consistently calls its own number "a genuine
**1.24×** increase" (three occurrences, `phase2_critique_materials.md`
lines 31/58-59), never 1.25×. The disclosed text's "~1.25×" borrows my own
route's exact ratio and applies it as the headline descriptor for the
MATERIALS numbers that are the ones actually shown — while my own numbers,
which are the ones that genuinely are exactly 1.25×, never appear. "Two
independent routes... agree bit-exact" is true only in the weaker sense
that each route is independently, bit-exact reproducible by a second party
(confirmed above) — not that the two routes' own numbers agree with each
other. Non-outcome-reversing (both routes, correctly stated, still land
"orders of magnitude below the measurement floor," the only claim doing any
work) — recommended fix below.

### F2 — The reproduction/self-consistency precondition genuinely passes on real data; the energy_ledger's own `sigma_ext ≈ sigma_abs+sigma_scat` check is a tautology, not an optical-theorem check, and this cycle's own genuine optical-theorem cross-check is uncomputable from its persisted data

**Reproduction/self-consistency precondition — independently re-derived
from raw arrays, not the printed flag.** I summed `results.json`'s own
persisted 48-bin `pattern_peccored`/`pattern_hollow` arrays directly and
compared against `energy_ledger`'s own `sigma_scat` figures:

```
sum(pattern_peccored) = 350.57117595080604   energy_ledger.peccored.sigma_scat = 350.57117595080604   rel_dev = 0.0
sum(pattern_hollow)   = 350.60048277707733   energy_ledger.hollow.sigma_scat   = 350.60048277707733   rel_dev = 0.0
```

Both hold to **exactly** 0.0 relative deviation (not merely `<1e-9`) —
`repro_ok=True`/`rel_dev_peccored=0.0`/`rel_dev_hollow=0.0` genuinely
reproduce from primitives, confirmed independently. But `lab/sections.py::
angular_scattered_pattern`'s own docstring states this identity plainly:
"Because binning is a re-partition of the exact same per-cell terms
`widths()` already sums in full, `sum(pattern) == sigma_scat` is not an
independent physical check — it's an implementation self-consistency
identity." This cycle's own Predictions/Result text names it correctly
("reproduction/self-consistency precondition") and never overclaims it as
more — that discipline is sound.

**The energy_ledger's `sigma_ext` vs. `sigma_abs+sigma_scat` bookkeeping —
also re-derived, also holds exactly, and is also a tautology, not the
optical-theorem check your instruction asked me to test.** I read
`lab/sections.py::widths()`'s own source directly: it returns
`"sigma_ext": (p_scat + p_abs) / i_inc` — `sigma_ext` is *defined* as
`sigma_abs+sigma_scat` in this route, so the identity
`sigma_ext == sigma_abs+sigma_scat` (confirmed exactly, both peccored and
hollow, at `rel_dev=0.0`) is guaranteed by construction, independent of
whether the underlying FDTD run is physically correct at all. The genuinely
independent check `widths()` itself already computes — `sigma_ext_cross`,
an interference-based (forward-scattering, optical-theorem) extinction
measurement, `p_ext_cross = -_cross_flux(pi, ps, box)`, a structurally
different route from the box-flux sum — exists in `analyze.py`'s own
in-memory `w_p`/`w_h` dicts (confirmed by direct source read, line 87-88)
but was **never persisted** into this cycle's own `energy_ledger` (Docket
Fix 6 asked only for `sigma_abs`/`sigma_ext`, not `sigma_ext_cross`).
This program has an established precedent for the genuinely informative
comparison: exp-110's own `results.json` **does** persist
`sigma_ext_cross` (`560.19558`/`1191.34027` at r=156/312, agreeing with its
own `sigma_ext` figures to ~3×10⁻⁵ relative — a real, non-tautological,
passing physical cross-check). exp-112 broke that continuity this cycle,
un-flagged by any of the five Phase-2 critiques, Red Team's own Phase-2
audit, or NOTES.md itself. **Net answer to your question, stated plainly:
the specific relationship you asked me to check (`sigma_ext ~ sigma_abs +
sigma_scat`, optical-theorem bookkeeping) is not testable as genuine
physics from this cycle's own persisted `energy_ledger` — only its
definitional restatement is, and that restatement necessarily reads
"PASS" regardless of correctness.** Non-blocking this cycle (T1 N/A, no
physical verdict rests on the energy ledger at all — Docket Fix 6 was
explicitly "not load-bearing"), but a real, first-identified verification
gap under my own charter, not previously named. **Recommend:** any future
cycle that persists an `energy_ledger`-style field should persist
`sigma_ext_cross` alongside `sigma_abs`/`sigma_ext` by default (zero
marginal cost — already computed, silently discarded), restoring exp-110's
own convention.

### F3 — The second R29 collision instance (found at Phase 4): my own reasoned view, as requested

NOTES.md's own Phase-4 section explicitly declines to self-adjudicate
whether the second collision (`analyze.py`'s bare `import chunk_runner as
CR` resolving, via `sys.path` insertion order, to exp-110's own
`chunk_runner.py` rather than this directory's) fires R29's forward clause
("a second instance of this exact collision shape... fires Checkpoint
criterion 4 automatically") or is the founding instance's own second,
previously-undiscovered manifestation. My reasoned view: **it does not
fire Checkpoint criterion 4 this cycle** — I read it as the latter.

Reasoning from R29's own text and PANEL.md's Checkpoint criteria:

1. **Same root cause, same authoring act.** R29's own founding-instance
   text states plainly that "this cycle's own original Phase-1 draft
   introduced BOTH collisions in the same sitting" — the second collision
   is not a fresh mistake made by someone who had R29 available to consult
   and reused the danger anyway (the scenario the forward clause exists to
   deter); it is a second symptom of the identical pre-rule authoring
   defect (careless multi-directory `sys.path.insert(0, ...)` staging
   combined with this T28 sub-thread's own recurring `run.py`/
   `chunk_runner.py` basenames), merely undiscovered until Phase 4 because
   Phase 2's blind critique crashed on the first collision before ever
   reaching code that would exercise the second.
2. **Same general hazard class, not a different one.** R29's own opening
   sentence names the class broadly — same-basename modules reachable from
   more than one directory on `sys.path`, resolved silently rather than by
   an executed identity check. The mechanical detail differs (the founding
   instance is two competing `as`-aliases collapsing to one cached object;
   the second is a single bare import resolving to the wrong directory
   purely by insertion order) but both are the identical underlying Python
   import-hygiene footgun this rule's remedy (distinct basenames, or an
   `importlib`-scoped load, either way verified by an executed identity
   check) is built to close — and Fix 1's own remedy, applied only to the
   first collision, left the second one's identical hazard (`chunk_runner`
   still same-named across two directories, still no executed check)
   sitting untouched precisely because nobody yet knew it existed.
3. **Matches this registry's own dominant precedent for within-cycle
   discovery density**, most directly R20 (exp-099: FIVE independent
   R4-class defects discovered across one document's own lifecycle, ruled
   non-firing collectively as the founding instance's own discovery sweep)
   rather than R24's own precedent (where the *second* instance fired,
   because that one occurred on a genuinely *different, later cycle*, on a
   *different code channel*, after the rule had already been available in
   LOGBOOK for that new cycle's own authors to consult and did not).
   exp-112's second collision is discovered inside the SAME cycle that
   proposes, ratifies, and fixes the founding instance — closer to R20's
   shape than to R24's.
4. **Timing counter-argument, acknowledged, not persuasive on balance.** A
   strict textual reading could note Phase 3 ratified R29 into LOGBOOK.md
   before Phase 4 discovered the second collision, so the forward clause's
   "after this rule is on the books" precondition is literally met. I do
   not find this persuasive: the rule's own purpose (deterring reuse of a
   *named* danger) cannot apply to code written before the danger was
   named at all, and treating a same-cycle Phase-3→Phase-4 sequencing gap
   as sufficient to trigger an automatic, "no further deliberation" fire
   would produce a perverse incentive — a cycle that discovers and
   ratifies a new rule becomes MORE exposed to instantly tripping it than
   one that never named the hazard, for exposing more of its own scope in
   the same sweep.

**Recommendation attached to this finding:** whichever way Red Team's own
Phase-5 final audit rules, LOGBOOK's R29 entry should be updated to state
the disposition explicitly (it currently reads as if only one collision
ever existed) and to add a clarifying sentence for future cycles: multiple
manifestations of a single pre-rule authoring defect, discovered across
different Phases of the SAME cycle that also proposes and ratifies the
rule, count as one founding instance for firing purposes — closing this
precise ambiguity before a future cycle can exploit (or be unfairly
penalized by) the timing question this cycle leaves open.

## Independently re-verified, no defect found (background, supports the verdict above)

- Check B (`SURVIVES`): recomputed `delta_new/delta_old = 1.3152` directly
  from `results.json`'s own `named_bin`/`baseline` fields — sign preserved,
  inside `[0.1,10]`, matches NOTES.md's claimed "grew by 1.315×" exactly.
- Check C (neighbor correlation): recomputed the Pearson correlation of the
  ±2-bin window directly from `pattern_delta` (this cycle) against the
  literal window read out of exp-110's own committed `raw_patterns.32`
  array (bit-exact match to the `baseline_window` cited) — `corr=0.99936`,
  reproduces exactly, genuinely traces to real committed exp-110 data, not
  fabricated.
- `local_snr_peccored`/`local_snr_hollow` (`0.1444`/`0.1589`) and the
  mirror-pooled floor (`9.725e-4`) independently recomputed from raw
  `pattern_peccored`/`pattern_hollow` via `mirror_pooled_floor`/K=3/median —
  bit-exact match; Check A's own AMBIGUOUS classification (neither reaches
  the `1.0` bar) correctly applied.
- `tau_shell` invariance (`24.0` both `cpl`) and total simulated optical
  periods (`320·S` both `cpl`) spot-checked by hand from the geometry
  table — hold exactly, as claimed.
- The second-instance R29 fix itself (`chunk_runner112.py`/`analyze.py`)
  reads correctly in the currently-committed source: distinct basenames,
  executed identity assertions present, matching NOTES.md's own account.

## Ranked next-step recommendation

1. **Close F3 explicitly in LOGBOOK** — a Director/Red-Team ruling on the
   R29 second-instance question, plus the forward-looking clarifying
   sentence recommended above, before Iteration 90 opens. Cheapest, most
   process-load-bearing item on this list (zero FDTD, prevents this exact
   ambiguity recurring).
2. **Persist `sigma_ext_cross` by default** in any future `energy_ledger`-
   style field (F2) — zero marginal FDTD cost (already computed in
   `analyze.py`'s own `w_p`/`w_h`), restores this program's own established
   two-route optical-theorem cross-check convention, and is the specific,
   affordable fix that would let a future cycle actually answer the
   physical-bookkeeping question this cycle's own energy_ledger only
   answers tautologically.
3. **Correct the "~1.25×" mislabeling** (F1) to "~1.24×" (matching the
   actually-disclosed MATERIALS route's own true ratio, and MATERIALS' own
   critique language), or display both routes' numbers side by side with
   their own distinct ratios — closing the asymmetric-attribution gap
   where a finding is credited to two seats jointly but only one seat's
   numbers ever reach the traveling record. Purely a documentation-
   precision fix; non-outcome-reversing either way.

Separately, on the substantive physics question this cycle exists to
answer: Check A's own genuine AMBIGUOUS reading (not SURVIVES, not
COLLAPSES) combined with Check C's striking `0.9994` neighbor correlation
means the named bin remains genuinely undecided, not merely under-powered
— a third, differently-scaled resolution point (`cpl=30`, already costed in
`cpl_cost_table.py`) is the R15-consistent minimum next physics step,
which I endorse as directionally correct, though it is not primarily an
EM-charter call.
