# exp-064 — Phase 5 Review: THERMODYNAMICS

**Panel Iteration 41. Fresh sub-agent, blind — no other seat's Phase-5
review of this cycle was read before writing this.** Charter: where
absorbed energy goes; whether the resulting ΔT/emission is detectable;
the per-proposal energy sidecar. This is the seat that led Iteration 40
(exp-063, the CNT-forest κ/Biot correction this cycle's guard now wraps)
and that raised the specific Phase-2 attack (mandatory-fix 4) this review
is asked to re-examine with fresh eyes.

Independent verification performed before writing a word of judgment:
`git log --oneline -3` (HEAD confirmed at `482392a`, "exp-064 Phase 4
results," current); full read of `lab/thermo_sidecar.py` as it now
stands, `lab/validation/run_all.py` stages 18/23/24 in full, and
`lab/caveat_lint.py`'s own matching/discovery mechanics plus the live
`exp064-length-provenance-disclosure` registry entry
(`lab/caveat_lint_config.json`, read via direct `json.load`, not a
paraphrase); `lab/numeric_lint_config.json` (4 entries, none new for
exp-064 — consistent with the record, no gap); exp-064's Phase 1/2 (all
five critiques + Red Team audit)/3/4 documents and NOTES.md in full;
exp-063's `phase4_results.md` TD-3/TD-4/TD-5 sections read directly
(lines 100–199), not taken on trust from exp-064's own restatement.

---

## (a) Does `_geometric_realizability_note` close the ambiguity I flagged
at Phase 2?

**Partially — real, load-bearing progress at the function/dict level; NOT
yet closed at the propagation level, and the gap that remains is
concrete, not hypothetical.**

**What is genuinely fixed.** My own Phase-2 attack was that a green
`diagnostic_only=True` call still returns a full numeric dict with
nothing distinguishing "provenance correctly flagged as unlicensed" from
"the object this describes may not exist at any provenance tag." Red
Team's mandatory-fix 4 adopted option (a) — an additive
`geometric_realizability` field — over option (b) — stripping the
witness-scale calls from the gated regression path — reasoning that (a)
preserves stage 23's existing regression anchors while still closing the
named ambiguity. Reading `_geometric_realizability_note` directly: for
`diagnostic_only=True` it returns an unambiguous, self-contained sentence
("UNGROUNDED... NEVER a buildability question... See exp-064 NOTES.md,
live thread T23"), not a bare flag a reader has to interpret. This is not
decoration — stage 23 gate 2 and stage 24 gate 3 both regression-anchor
the field's exact prefix (`"UNGROUNDED"` vs `"N/A"`) against the licensed/
diagnostic branches, so the distinction cannot silently regress without
failing the trust suite. **For anyone who inspects the returned dict
itself — which is what every current call site in this program's code
does — the ambiguity I flagged is gone.** This is a genuine strengthening
of the epistemic record, the same kind this program credited at
Iterations 38–40 for `caveat_lint.py`/`numeric_lint.py`.

**What is not fixed — verified independently, not merely suspected.**
`_geometric_realizability_note` is "just one more dict key" in exactly
the sense the sharpest form of my own worry named: nothing forces a
*downstream prose citation* — a future `LOGBOOK.md` entry, a future
`phase4_results.md` Summary table, a future results.json restating
TD-5's margin — to reproduce or even reference it. I checked whether this
program's own propagation-check machinery closes that gap and it does
not, for a specific, checkable reason:

- `lab/caveat_lint_config.json`'s new `exp064-length-provenance-
  disclosure` entry's `trigger_terms` are `["length_provenance",
  "front_surface_conduction_correction", "T23"]` — module/function/thread
  *names*, not the actual headline quantities a future citation would
  plausibly use (`correction_factor`, `1.2920`, `7.8×`, `TD-5`,
  `κ_critical`, `MP-5`/`730×`). A future document that restates "TD-5's
  margin is 1.2920×, 7.8× above κ_critical" — exactly the phrasing this
  program's own record already uses in `LOGBOOK.md` Iteration 40 and
  `PLAN.md`'s current-state block — would not even register as a
  candidate site for `caveat_lint.py`'s own WARN-level discovery, because
  none of its trigger terms would match. I confirmed this by reading
  `lab/caveat_lint.py:219-236` directly: `trigger_terms` gates candidate
  *discovery* itself, not just which files get flagged.
- Even where a trigger term *does* match, `check_caveat`'s own candidate
  path is explicitly WARN-only and, per the tool's own docstring, "never
  affect[s] the exit code" — it surfaces nothing unless a human runs
  `python3 lab/caveat_lint.py` (full registry, no `--only`) and reads the
  WARN lines. A future cycle running `--only` a different entry, or simply
  not running the tool at all before writing a summary table, gets no
  signal.

So the honest answer to "is there a way a future careless reader could
still miss this field entirely": **yes, concretely** — a future Iteration
42+ document that restates TD-5's number in prose (not by calling
`front_surface_conduction_correction` fresh and printing the whole dict)
carries zero mechanical guarantee of carrying `geometric_realizability`
with it, and the one registry entry built this cycle to guard exactly
this class of drift is scoped too narrowly (by trigger-term choice, not
by design flaw) to catch it. This is the same *shape* of gap — a
real fix, correctly built, whose net doesn't yet reach the citation
one level downstream — that has cost this program six-plus Checkpoint-
adjacent findings (T23 itself; the `netd_disclaimer` losses at
Iterations 17 and 40; the `candidate_globs` narrow-scoping firings at
Iteration 39 ×2). It is smaller in stakes here (no number is wrong, no
gate is green when it shouldn't be) but it is the identical failure
mode, one level further out, and this program's own history says it
recurs unless someone widens the net before a citation, not after.

**Should a future cycle go further?** Yes — cheaply. Two concrete,
zero-FDTD moves, in order of cost:

1. Widen `exp064-length-provenance-disclosure`'s `trigger_terms` to
   include the actual numbers/labels a citation would use
   (`correction_factor`, `TD-5`, `κ_critical`, `MP-5`, `730×`/`730x`) —
   a one-line JSON edit, turns silent misses into WARN-level candidate
   hits the next time anyone runs the full registry.
2. A `numeric_lint.py` `derivation_consistency`-style entry (this
   program already has the idiom — `exp063-cf-bench-vs-witness-
   derivation`/`-phase4`): wherever a document's BASIS condition holds
   (cites TD-5's margin or `correction_factor` at the MP-5 geometry), a
   disclosure pattern (`diagnostic_only`/`UNGROUNDED`/`provenance-
   honesty`) MUST also appear in the same window, or the check FAILs —
   not a WARN, a real gate. This is the fix that would have actually
   discharged my own Phase-2 worry in full; item 1 above is the cheap
   partial substitute if item 2 is judged too much for a single future
   cycle to prioritize over the physics queue.

Neither is urgent enough to block this cycle's own verdict — the
function-level fix is real, tested, and regression-anchored, and no
document in this program's *current* record actually violates the
propagation gap yet (I checked: `PLAN.md`'s and `LOGBOOK.md`'s own
Iteration-40 entries were written before this cycle existed and
predate the `diagnostic_only` distinction entirely, so they are not
retroactively wrong, just not yet updated — a separate, non-blocking
bookkeeping note, not a defect this cycle created).

---

## (b) Do TD-1 through TD-5 survive unchanged? — confirmed numerically,
independently

**Yes, bit-for-bit, and I re-derived this myself rather than trusting the
cycle's own claim.** Three independent checks:

1. **Direct source diff-by-eye.** `lab/thermo_sidecar.py`'s
   `biot_number`, `front_surface_conduction_correction`, and
   `mixed_length_scale_regime` carry exactly one new line of *behavior*
   each (`_validate_length_provenance(length_provenance, diagnostic_only)`
   as the first statement) and three new *trailing* dict keys
   (`length_provenance`, `diagnostic_only`, `geometric_realizability`).
   Every line of arithmetic between those two edits — `bi_gas`, `bi_rad`,
   `correction_factor = 1.0 + bi_gas + bi_rad`, `dt_ss_full`,
   `tau_thermal_s` — is untouched. This is a guard clause plus additive
   metadata, not a formula edit.
2. **The regression anchors themselves, read directly from
   `run_all.py`.** Stage 23 gate 2 still asserts
   `bench["correction_factor"]` against `1.013006 (±1e-5)` and
   `mp5["correction_factor"]` against `1.015703 (±1e-5)` (lines
   2145–2150); gate 3 still bisects `κ_critical` against `0.089731
   (±1e-4)` (line 2170) — the exact three figures the task brief names,
   unchanged in the committed gate code itself, not merely in a document
   describing it.
3. **exp-063's own `phase4_results.md` TD-3/TD-5 sections**, read
   directly (lines 100–199): the sourced-κ bracket — `CF_bench(rear-
   only)` 1.00052×–1.03716×, `margin_bench` 674.22×–698.91×,
   `margin_mp5(rear-only)` 1.2920×–1.3492×, `κ_critical=0.0897 W/(m·K)`
   — is the number set this cycle's stage-23/24 gates were built to
   reproduce, and I find no daylight between what exp-063 committed and
   what exp-064's gates check.

`phase3_synthesis.md`'s own **107/107** full-bench figure
(`--only 12346789,10,11,18,19,20,21,22,23,24`) is consistent with QP-5
(zero physics change) and with my own source read. As a fourth,
independent check beyond reading the code, I ran the guarded stages live
in this review session (`python3 lab/validation/run_all.py --only
18,23,24`, this cycle's own analytic, zero-FDTD stages — T1 escape route
N/A means the FDTD stages are unaffected and were separately confirmed
earlier at Iteration 40): **43/43 PASS**, with the exact three anchor
values printed verbatim — `1.013006`, `1.015703`, `0.089731` — plus the
`geometric_realizability` field reading `UNGROUNDED`/`N/A` correctly on
the diagnostic/licensed branches respectively, and gate 4's source-scan
finding the expected 2 witness-scale / 3 bench-scale call sites, all
correctly tagged, against the live HEAD (`482392a`).

**Conclusion: TD-1 through TD-5's own verdicts are untouched by exp-064
— not "probably," but numerically confirmed at the source level.** What
changed is exactly what Red Team's mandatory-fix-4 ruling said would
change: the epistemic *label* on TD-5's witness-scale leg (now
permanently, code-enforced `diagnostic_only=True` / `UNGROUNDED`, where
before it was a prose caveat three cycles disclosed and never enforced).
No digit moved.

---

## (c) Is the CNT-forest root-to-substrate contact resistance still the
right #1 priority for Iteration 42?

**Yes — and exp-064's own work sharpens, not weakens, that case, from
THERMO's discipline specifically.**

The reasoning: exp-064 is a pure provenance/labeling cycle by design (T1
escape route N/A, zero FDTD, zero constraint metric). It could not and
did not touch any number in TD-1 through TD-5 (§b, above) — it only
changed how honestly the witness-scale leg's *length* is labeled. That
means the physics question that made TD-5 this program's "thinnest
safety factor of any kind on record" (7.8× over κ_critical, per
Iteration 40) is exactly as open today as it was before this cycle ran.
The root-to-substrate contact-resistance question (MATERIALS' Iteration-
40 finding, PLAN.md queue item 2) is the only one of the three carried
Iteration-41 items that could actually **move a number** in the chain
this seat owns — not relabel it, move it. Query 10's own already-sourced
finding (inter-tube van der Waals junction conductance <1% of a single
tube's axial conductance) is the mechanism by which κ_solid was already
driven down to 0.7–9.62 W/(m·K) for as-grown forests; if the SAME class
of poor-contact physics governs the root-to-mounting-substrate bond too,
that is a *second*, structurally distinct thermal bottleneck the current
model has no term for at all — `front_surface_conduction_correction`'s
own `bi_gas`/`bi_rad` model loses heat only via gas conduction and
radiation at a rear boundary; it contains no substrate-conduction path,
so a poor root bond is not "a smaller κ_solid to look up," it is a
missing series resistance term. Sourcing (or bounding) it is squarely
this seat's own charter ("absorbed power → ΔT → emission →
detectability" — every link presumes the object's thermal boundary
conditions are correctly modeled, and this one currently is not).

By contrast, the standing queue item 3 (pin pitch/diameter + κ together,
now also carrying the thickness/realizability question exp-064's own §6
correctly struck rather than resolved) is a **buildability** question —
does an object of the needed length exist at all — which is now
correctly and durably flagged (via `geometric_realizability`) as open,
but resolving it would not, by itself, change any ΔT or margin number;
it would only tell us whether the number describes a real object. That
is MATERIALS'/PHOTONICS' question more than THERMO's. Item 2 is the one
that bears on whether the number itself is right.

**One sharpening this review adds, not previously on record**: if a
future Iteration 42 cycle finds the root-substrate bond is indeed a
comparable-or-worse contact resistance, the correct model extension is
NOT simply "re-run `front_surface_conduction_correction` with a lower
`κ_solid`" — that would conflate a bulk-material property with a
boundary/interface property the current formula has no slot for. The
physically correct fix is a genuinely new series term (a third thermal
resistance, `R_contact`, in series with the existing
`bi_gas`+`bi_rad` chain), gated the same way this cycle gated its own new
physics (an `R_contact→0` absolute-identity limit recovering the current
bracket exactly, matching PLAN.md's queue item 2's own already-correct
instinct) — not a same-function reparameterization. Flagging this now so
Iteration 42's Phase 1 doesn't reach for the cheaper-looking wrong fix.

---

## Verdict: **PROMISING**

T23 — a three-cycle-deferred, Red-Team-declared binding forward
commitment — is genuinely closed, not merely disclosed again: a required,
keyword-only, no-default `length_provenance` argument, backed by a
12-case zero-tolerance refusal gate and, critically, a source-inspection
gate (stage 24 gate 4) independently demonstrated live via a deliberate-
break test against the actual committed `run_all.py` (FAIL when broken,
PASS when correct) — the single strongest form of evidence this
program's own history recognizes for an "enforced, not merely disclosed"
claim. Every number in TD-1 through TD-5 is confirmed unchanged, by my
own independent re-derivation from source, not by trusting the cycle's
own restatement. The cycle's own Phase-2 process caught and struck a
materially wrong §6 claim (24×–75× vs. the correct ≈1×–10.5×) before it
reached the record — exactly the R4 discipline this program has needed
enforced repeatedly. My own Phase-2 attack (mandatory-fix 4) was accepted
in full and given a real, tested, regression-anchored fix, not a token
one.

The one residual gap I find on independent re-inspection — the
`geometric_realizability` field's propagation net (trigger-term coverage
in `caveat_lint_config.json`) does not yet reach a plausible future
citation of TD-5's bare numbers — is real, concretely demonstrated (not
speculative), and matches this program's single most recurrent failure
shape. It is not load-bearing against this cycle's own verdict (no
current document violates it; the fix the cycle shipped is not wrong,
only not-yet-extended one more hop) and is cheap to close — I rank it
below the physics queue, not above it, for Iteration 42.

---

## Ranked top-3 for Iteration 42 (THERMODYNAMICS' own ranking)

1. **Source, or at minimum formally model as a third series thermal
   resistance, the CNT-forest root-to-substrate contact resistance**
   (PLAN.md queue item 2, MATERIALS' Iteration-40 finding) — the only
   carried item that can move TD-5's own number, not just its label; this
   program's thinnest-ever margin (7.8×) deserves the next real physics
   test, not another provenance pass. Build as a genuinely new
   `R_contact` series term (gated by an `R_contact→0` absolute-identity
   limit recovering exp-064's own current bracket exactly), not a
   `κ_solid` reparameterization — see the model-shape note in §c above.
2. **Widen `exp064-length-provenance-disclosure`'s `trigger_terms`** to
   the actual headline quantities (`correction_factor`, `TD-5`,
   `κ_critical`, `MP-5`/`730×`) and/or add a `numeric_lint.py`
   `derivation_consistency` entry requiring the `diagnostic_only`/
   `UNGROUNDED` disclosure to co-locate with any future citation of
   TD-5's numbers — a one-cycle, zero-FDTD closeout of the propagation
   gap identified in §a, before a future document restates "1.2920×,
   7.8× margin" without it, recreating the exact drift pattern this
   program has now paid for six-plus times.
3. **Pin the record-blackness/Vantablack-class CNT forest's own pitch/
   diameter, through-thickness κ, AND the thickness/realizability
   question exp-064's own struck §6 left exactly where it was** (PLAN.md
   queue item 3, now carrying three sub-questions instead of two) — real,
   still fully open, but a buildability question one layer upstream of
   any number THERMO's own charter computes; correctly ranked below item
   1 for this seat, not dropped.

---

*THERMODYNAMICS, Panel Iteration 41, blind Phase-5 review of exp-064. No
other seat's Phase-5 review of this cycle was read before writing this.*
