# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 47
## exp-070 (T28 mechanism desk-check batch)

**Seat charter:** sub-wavelength structure; what could physically realize
the proposed optical behavior; owns the realizability bound (published /
plausible / unobtainium-with-parameters). Fresh context, blind to any
other seat's Phase-5 review this cycle.

---

## Verification performed

Re-ran `python3 desk_check_mechanism.py` in
`experiments/070-t28-mechanism-desk-check-batch/` against the committed
`results.json`. **Bit-exact reproduction** — `diff` against a pre-run copy
of `results.json` is empty. All five headline numbers reproduce exactly:
P-070-1 CONFIRM (C40 dev 14.29%, C80 dev 10.85%); P-070-2 NEITHER (`null_p`
0.2039 / 0.8055); P-070-3 REFUTE (1197% off); P-070-4 NEITHER (`null_p`
0.4969, `R²(750)=0.7663`); P-070-5 REFUTE (no shared expression). The
null-permutation control uses a fixed seed (`seed=0`), so this is a real,
re-run-and-confirm identity check, not merely a code read — R4 discipline
holds cleanly.

## Finding 1 — My own Phase-2 attack's fix (docket item 2, the
null-permutation control) was implemented correctly, with no
promise/delivery gap

At Phase 2 I flagged that the `NAMED`-constant search (items b/d/e) had no
false-positive-rate control and proposed a permutation-null test
(`N≥1000`, 5th-percentile gate) as the change that would flip my verdict
to plain support. Red Team's audit independently executed the check at
`N=10,000`, found it decisive (100% of random targets in `[100,1600]`
clear the 1% band), and specified the exact gated procedure (docket item
2 / ruling 2): `N=20,000` matching T28's own founding null test, fixed
range, `p≤0.05` gate, `p` reported alongside every result.

`design_geometry.py::null_percentile()` implements this exactly: fixed
seed for reproducibility, `N=20,000`, `Uniform(100,1600)`, searched
against the identical `SEARCH_VALUES` space used for the real targets, `p`
= fraction of null trials at-or-below the real target's own best relative
deviation (the correct direction — lower `p` means the real match is rarer
than chance, which is what should gate CONFIRM). `desk_check_mechanism.py`
calls it for both P-070-2 branches and P-070-4, and gates `confirm` on
`best_rel≤0.01 AND p≤0.05` in both places — matching NOTES.md's
predictions table and the docket's ruling verbatim. Re-running the script
reproduces `null_p=0.2039/0.8055/0.4969` exactly. **No gap.** This is the
one item my own charter is positioned to check hardest (I authored the
attack), and it survived independent re-execution.

## Finding 2 — the mandatory disclosed caveat is worded correctly and
placed where a reader will see it

NOTES.md's `## Mandatory disclosed caveat` section sits immediately after
`## Setup`, before `## Idealizations`, `## Predictions`, or `## Result` —
not buried at idealization #7 or #4 the way the Phase-1 proposal's
equivalent language was. Wording matches the docket's ruling almost
verbatim, including the "graded-loss absorbing boundary — not PML" fix
(Red Team's Attack 7, correcting my own Phase-2 critique's imprecise "PML"
language against `lab/fdtd2d.py`'s actual construction, per
VALIDATION.md). `design_geometry.py`'s own module docstring (item 5)
restates it a second time at the code level. This is placed correctly.

## Finding 3 — the NEITHER-heavy result set is reported honestly; no
residual language treats a null-failed match as more informative than it is

Checked NOTES.md `## Result`, `## Learned`, `## Next`, and every relevant
paragraph of `phase4_results.md` for language that would let a reader walk
away thinking P-070-2/4's raw sub-0.1%-deviation matches (which *do* clear
the un-gated thresholds and *do* match the Phase-1 disclosed recon almost
exactly) survived as evidence. They don't: P-070-2 and P-070-4 are both
scored `neither: true` in `results.json` and reported as NEITHER
throughout prose, with explicit language ("statistically indistinguishable
from chance," "not merely 'not significant,' actively unremarkable" for
the `p=0.8055` branch). `phase4_results.md`'s own framing of P-070-4 —
"every number that made P-070-4 look like this batch's strongest finding
at Phase 1 survives entirely intact into Phase 4, and is still correctly
NEITHER" — is the correct, load-bearing sentence in this document; it
names the HARKing risk instead of laundering it. `NOTES.md`'s `## Next`
explicitly instructs that PLAN.md queue item 2 be narrowed by P-070-1's
CONFIRM only, "not by P-070-2/4's raw (pre-null) numbers," per docket item
10. I find no violation.

## Finding 4 — realizability standing view: unchanged, and this cycle is
positive evidence *for* the standing view rather than neutral

My charter's standing view of T28 (LOGBOOK/PLAN.md) is that it is a
numerical/model-fidelity question, not yet a realizability question — no
`NAMED` constant here is a material parameter (`ε(ω)`, `σ`, layer
thickness); all 14 are FDTD domain-construction bookkeeping (padding,
graded-loss boundary depth, taper length, clearances), confirmed again
this cycle at the code level (`design_geometry.py::NAMED`, traced to
`design_geometry.py::config()`'s own construction fields, exp-065). This
cycle does not merely restate that view — it strengthens it with an
executed result: the null-permutation control shows the search space is
dense enough that *any* plausible length scale in `[100,1600]` cells finds
an equally-tight match by chance (median null deviation 0.037%, tighter
than either real target's own best match), which is itself the signature
predicted by a boundary-construction-tied artifact, not a load-bearing
physical resonance. Nothing here bears on `REALIZABILITY_MEMO.md`
(correctly, no entry was touched or should be — I checked; the memo lives
at `experiments/034-.../REALIZABILITY_MEMO.md` and has no T28-adjacent
content, appropriately). **No change of standing view, in either
direction; the burden-of-proof bar for a future T28 mechanism claim to
reach my charter's ledger is, if anything, now stated more precisely.**

## Finding 5 (new, load-bearing) — the caveat_lint registry has no entry
protecting exp-070's own new numbers going forward

`lab/caveat_lint_config.json`'s only T28-adjacent entry
(`exp065-steps1400-unsettled-plane-channel`) is scoped to the STEPS=1400
settling question and Block MINI/ARTICLE retirement language — it has no
`trigger_terms` for exp-070's own headline quantities (`A_eff`, `A_alt`,
`519`, `233`, `P-070-2`, `P-070-4`) and no `required_sites` inside
`experiments/070-.../`. Running `python3 lab/caveat_lint.py` confirms
0 required-site failures and no WARN for exp-070's own files — but only
because the existing entry's `phrase_patterns` happen to match on a
carried-forward `0.8271` citation, not because anything actually checks
that a future document citing `A_eff≈519` or `A_alt≈233` also carries the
"does not bear on realizability / statistically indistinguishable from
chance" caveat. Given this program's own repeated history of exactly this
propagation gap (R4; the stale-registry catch at exp-069's own Phase 5),
this is a real, if minor, forward risk, not yet a live defect.

**Proposed fix (load-bearing for the next cycle that touches T28):** add a
`caveat_lint_config.json` entry keyed to trigger terms `A_eff`, `A_alt`,
`519`, `233`, `P-070-2`, `P-070-4`, requiring the null-controlled-NEITHER
disclosure (or the mandatory bookkeeping-not-material-parameter caveat) in
any site that cites them, `required_sites` seeded with
`experiments/070-.../NOTES.md` and `phase4_results.md`. Cheap, desk-only,
zero FDTD.

## No other defects found

`design_geometry.py`'s search-space construction (36,680 expressions,
7,179 distinct values), the tie-reporting logic (`closest_matches`), and
item (e)'s convergence check were all re-inspected against the docket's
fix 3/4 requirements — all implemented as specified, no arbitrary
single-"best"-pick ambiguity remains, and re-execution reproduces every
listed tie exactly.

---

## Ranked top-3 candidate next directions for the program

1. **EM's C60/C70 falsification test** (PLAN.md queue item 2's primary
   branch, already-built congruent configs, zero new `lab/` diff): P-070-1
   positively disfavors the `ABSORB`-tied hypothesis it was designed to
   test, and items (b)/(d)/(e) contribute no surviving candidate length
   scale to narrow a re-run toward — so this is now a clean, cheap,
   *directly falsifying* test of the one mechanism hypothesis this cycle
   left alive-but-doubted, rather than a blind redesign. Highest priority:
   it is the correctly-narrowed next FDTD-cost step this whole desk-check
   batch existed to earn.

2. **`R_contact`'s `measured_direct` literature search** (PLAN.md queue
   item 3, unchanged ranking, still blocked purely on WebSearch/WebFetch
   tooling): still the only item across six cycles now that can move a
   real material parameter on my own charter's ledger
   (`REALIZABILITY_MEMO.md` Entry 3, TD-5's 7.8× margin, unanswered).
   Orthogonal to T28 entirely — flagged here because it remains this
   seat's single most consequential open item, and every cycle it goes
   unpicked is a cycle the realizability bound stays wider than it needs
   to be.

3. **Add the `caveat_lint_config.json` entry for T28's own new NEITHER
   numbers** (Finding 5, above): cheap, desk-only, zero FDTD, closes a
   real (if currently dormant) propagation-risk gap before any future
   document has occasion to cite `A_eff≈519` or `A_alt≈233` without the
   null-controlled-NEITHER caveat attached — the exact failure shape this
   program has been burned by more than once.
