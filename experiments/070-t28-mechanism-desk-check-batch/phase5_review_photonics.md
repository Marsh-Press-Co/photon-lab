# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 47 · exp-070

**Charter:** surface interaction, absorption spectra, angular dependence,
scattering cross-sections. Owns: is the proposal's optical response
coherent as stated, across wavelength and angle?

Fresh context, blind to any other seat's Phase-5 review this cycle.
Independent verification performed: re-ran `python3 desk_check_mechanism.py`
in `experiments/070-t28-mechanism-desk-check-batch/` — **output is
bit-exact against the committed `results.json`** (`git status`/`git diff`
both empty after the re-run). No numeric, hand-typing, or R4 defect found
in any headline figure.

## 1. Did Phase 3/4 close my own Phase-2 critique?

**Yes, cleanly, with no open item.** My Phase-2 sharpest attack was the
named-constant search's look-elsewhere risk (items b/d/e): a dense
280-single + 36,400-pair space nearly guarantees a sub-1% match regardless
of ground truth, and the headline `3·R_OUT=234` candidate is not even the
closest match in its own space. My proposed fix — a pre-registered
permutation-null control mirroring T28's own 20,000-trial founding test —
was **adopted, and independently executed rather than left as a proposed
future step**: Red Team's Phase-2 audit ran it for real (`N=10,000`
scratch, then the committed `N=20,000` run), found the search space has
essentially zero discriminating power (100% of random targets in
`[100,1600]` cells clear the 1% band), and required `p≤0.05` before any
P-070-2/4/5 CONFIRM. The final run reports `null_p=0.204/0.806` (item b)
and `0.497` (item d) — none clears the bar, all three correctly scored
NEITHER despite raw matches as tight as 0.015%. This is the single
clearest close of a Phase-2 critique I can verify in this program's
record: not merely "accepted," independently *proven* and then *executed
through to a gated result*.

One correction to my own prior text, caught by Red Team (Attack 3, not
overturning my verdict): my critique's illustrating numbers conflated two
different targets' tie-groups (`519`'s six-way tie vs. `233`'s two-way
tie) when citing "headline not closest match." Phase 3/4 fixed this in
place (`phase4_results.md`'s "Search-space provenance" section) and
attributed the correction to Red Team's audit rather than silently
absorbing it. Correctly handled.

## 2. Is P-070-1's CONFIRM (config-invariant hypothesis) correctly derived and honestly reported?

**Correctly derived, honestly reported, but the prose narrates it about
one notch more decisively than the underlying numbers support.**

The redefined gate (docket fix 1 — score the recovered period's deviation
from `P*_delta`, not bare R², after Red Team proved the original bare-R²
gate would CONFIRM via a spurious, unrelated third period) is sound and
correctly reuses this program's own established precedent: the identical
20%-CONFIRM/50%-REFUTE band already used at exp-069's own P-069-3 (testing
whether the delta's free-fit period matched T21's fixed period — that
comparison landed at 44.9% and scored the "genuine gray zone" NOTES.md
history now cites). Reusing that exact convention for a new comparison is
methodologically consistent, not gerrymandered.

The reported numbers are accurate (verified bit-exact): `C40` recovers
`P*=2.4361°` (14.29% from `P*_delta=2.8421°`), `C80` recovers `P*=2.5338°`
(10.85%), both inside the 20% band, `R²=0.4327/0.4337`, neither
disqualifying. **What NOTES.md's Learned #1 slightly overstates**: it
reads "the recovered periods... both independently land close to the
padding-delta's own free-fit period" as if this were a tight match. Two
things complicate that framing, both real and both absent from the
write-up:

- **`C40` and `C80`'s own recovered periods differ from each other by
  ~3.7%** (`(2.5338−2.4361)/2.8421`), despite the claimed shared physical
  length scale (`R_OUT`/`W_OBJ`/aperture geometry — Idealization 4) being
  **bit-identical** between the two configs by the congruent-construction
  discipline. A single coherent diffraction feature tied to an identical
  geometric edge would be expected to reproduce closer to the same period
  in both configs than this — T21's own established fringe, sourced from
  an analogous identical-geometry argument, fits at R² up to 0.83. This
  residual 3.7% scatter is plausibly ordinary 31-point fit noise, but
  NOTES.md doesn't say so; it should.
- **The fixed-period fit against T21's OWN period (`T_SINTHETA_600`,
  1.9608°) is computed and stored (`r_squared_fixed = 0.2988` for `C40`,
  `0.2645` for `C80`) but never surfaced in NOTES.md or `phase4_results.md`
  prose.** These are not negligible — they sit close to the `R²≥0.30`
  threshold this exact program used elsewhere (P-069-2's own CONFIRM bar)
  and only moderately below the free-fit's `0.43`. The data does not
  *cleanly* discriminate "closer to 2.84°" from "still meaningfully
  explained by 1.96°" — it leans toward 2.84°-family, correctly, but the
  lean is softer than the prose conveys. This is a `results.json` field
  that exists, is correct, and is simply not cited — a citation gap, not a
  numeric one.

Neither point overturns the CONFIRM (which is scored on the pre-committed,
Red-Team-audited period-deviation gate, not on R² comparison, and passes
that gate honestly). Both are one-line additions NOTES.md should carry so
a future reader citing "config-invariant" does not read it as tighter than
it is.

## 3. Anything optically incoherent about the padding-delta / per-config treatment?

**No structural incoherence.** Comparing raw `C40(θ)`/`C80(θ)` curves
individually against a period derived from their *difference* is a sound,
standard move: two configs sharing an identical aperture/edge geometry by
construction should imprint the same interference structure on each raw
curve, not only on the difference — that is exactly what item (a) tests,
and a signal found "only in the difference" would indeed point toward the
one thing that differs (`ABSORB`). The beat-frequency algebra (item b) is
correctly self-flagged (Idealization 6) as assuming linear two-tone
superposition, with an honest hedge for a non-additive alternative. The
mandatory disclosed caveat (docket item 5) correctly scopes itself to
items (b)/(d)/(e) — appropriately, since those are the ones searching the
NAMED bookkeeping-constant space; item (a) makes no such claim and needs
no such caveat. No conflation found between what a "config-invariant"
result can and cannot license (Idealization 7 states this correctly: "a
specific, falsifiable geometric candidate survives a zero-cost check,"
not a proven mechanism).

## 4. Numeric / citation / caveat-propagation defects

**One load-bearing gap, found by checking the registry, not the prose.**
`lab/caveat_lint_config.json` has **no entry for exp-070**. This cycle's
own headline near-misses — `A_alt=233.19` matching `3·R_OUT=234` at
0.081%, `A_eff=518.81` matching a six-way tie at `519` at 0.036% — are
exactly the shape of number this program has repeatedly required a
registry guard for: tight-looking, easy to cite favorably, correct only
when paired with context that lives in a different sentence (`null_p
=0.806`/`0.497` — worse than or indistinguishable from a random target in
the same search space). `phase4_results.md`/NOTES.md both currently pair
every such number with its `null_p` correctly — the gap is **forward**,
not present: nothing stops a future citation (most immediately, whatever
document reports EM's C60/C70 test, the very next queued item) from
quoting "`A_eff≈518.81`, 0.036% match" without the null-context that makes
it NEITHER, not CONFIRM. This is the identical failure shape LOGBOOK
records Checkpoint-4 firing on multiple times (R_contact's endpoint
conflation, Block ARTICLE's caveat propagation) — caught here before any
violation exists, which is the cheap, correct time to catch it.

**Proposed fix (load-bearing, cheap):** add a
`lab/caveat_lint_config.json` entry (e.g.
`exp070-t28-named-constant-null-control`) with `trigger_terms` covering
`A_eff`, `A_alt`, `518.8`, `233.19`, `3\*R_OUT`, the six-way `519` tie
members, and `required_sites`/`candidate_globs` mirroring the existing
`exp067-r-contact-analogy-proxy-disclosure` pattern (this cycle's closest
precedent for "a tight number that is only correctly interpreted with an
attached caveat"), covering `LOGBOOK.md`, `PLAN.md`, and
`experiments/*/phase*.md` generically so EM's/PHOTONICS' own Iteration-48
follow-up is caught automatically rather than by hand review.

**No other numeric defect found.** Every table value in `phase4_results.md`
and `NOTES.md` reproduces bit-exact from the independently re-run script;
the search-space size (36,680/7,179), the `P_taper=36.86°` REFUTE, and all
five verdicts (CONFIRM/NEITHER/REFUTE/NEITHER/REFUTE) check out against
`results.json` directly.

## 5. Supplementary due-diligence (diagnostic only, not committed to git, R4-compliant disclosure)

Because item (a) received a different fix (docket item 1: score on
recovered period) than items (b)/(d)/(e)'s null-permutation control
(docket item 2), despite using the identical `_free_period_search` grid
machinery with its own look-elsewhere exposure, I ran a scratch
permutation-shuffle check (shuffle `C40`/`C80`'s own 31 values across
their fixed θ positions, re-run `_free_period_search`, N=3000) to see
whether this asymmetry in the docket's rigor matters. **It does not
overturn anything, but it is a real gap the batch should have closed
itself:** the observed `R²=0.4327`/`0.4337` are genuinely significant
against a shuffle-null (`p≈0.012`, `p≈0.006` — only ~1% and ~0.6% of
shuffled trials reach that R² or higher), and the shuffle-null's own
spurious high-R² fits cluster near the grid's low edge (`~1.0–1.5°`), not
near `2.4–2.5°` — so the recovered periods are not simply a generic
search-grid artifact. This independently corroborates P-070-1's CONFIRM.
**Recommended minimal fix, non-blocking:** a one-paragraph addendum (or a
same-shift follow-up script, mirroring items b/d/e's own null-control
pattern) formally running this check through committed code and citing it
in NOTES.md, so the asymmetry between item (a)'s and items (b)/(d)/(e)'s
statistical rigor is closed by evidence already in hand rather than left
as an unstated gap a later reviewer could reasonably re-raise.

## Ranked top-3 candidate directions for the program

1. **EM's C60/C70 congruent-construction falsification test** (PLAN.md
   queue item 2, first branch). Already-built configs, zero new `lab/`
   diff. This is the correct next step, and more valuable now than before
   this cycle: P-070-1's CONFIRM leans toward a geometry-invariant
   mechanism but rests on only two configs whose own recovered periods
   differ from each other by ~4% — adding `ABSORB=60/70` gives two more
   points to determine whether the ~2.4–2.5° period genuinely holds flat
   across four `ABSORB` values (strengthening item (a)'s finding with real
   statistical power) or drifts with `ABSORB` (overturning it). Directly
   narrows T28 with new data, at minimal cost, rather than further desk
   arithmetic on an already-exhausted named-constant space.

2. **Add the missing `lab/caveat_lint_config.json` entry for exp-070's
   null-permutation context** (§4, above). Zero-FDTD, minutes of work,
   closes the exact caveat-propagation gap class this program has fired
   Checkpoint-4 on repeatedly — and the highest-leverage moment to add it
   is now, before item 1's own write-up becomes the first opportunity to
   miscite `A_eff≈518.81`/`A_alt≈233.19` without their `null_p` context.

3. **R_contact's `measured_direct` literature search** (PLAN.md queue item
   3, unchanged ranking). Orthogonal to T28, competes for no FDTD budget
   or rotation slot, and remains the only item across many cycles that can
   move a real, sourced materials number for TD-5's still-UNANSWERED
   tier — blocked purely on WebSearch/WebFetch tooling, not on any
   physics or process gap.
