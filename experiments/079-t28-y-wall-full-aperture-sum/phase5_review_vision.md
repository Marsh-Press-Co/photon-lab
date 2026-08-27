# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 56 (exp-079)

*Fresh sub-agent, blind to the other five Phase-5 reviewers and to Red
Team's own Phase-5 final audit (which has not yet run). Charter (PANEL.md
seat 6, verbatim): "human perceptual limits... pin numeric thresholds, with
sources, BEFORE any run that scores against them." As in every prior T28
instrument-fidelity cycle: **no perceptual threshold exists to pin here** —
T1 escape route N/A, no absorber, no ambient scene, no constraint-3 claim
anywhere in this record (independently re-confirmed, §2 below). Per this
task's own brief, this seat's load-bearing duty this cycle is the other
standing one: commensurability auditing (R9's own origin, this seat's
Iteration-54 finding) and stale-correction auditing (the exp-078 precedent),
sharpened here to the FINAL, corrected record — not the as-filed one — since
this exact sub-thread has now shown twice (exp-077's LOGBOOK entry, exp-078's
own §5.2 table) that a correction applied upstream does not automatically
propagate everywhere it needs to.*

---

## 1. Verdict: **PARTIAL**

exp-079 executed the reconciled Iteration-56 ranking's own top item: does
exp-078's flat, zero-amplitude single-edge result generalize to the full,
non-edge-reduced coherent aperture sum? The answer, independently
reproduced here, is genuinely informative in both directions at once. **No,
the flat result does not survive** — a real, converged, gate-clean,
non-degenerate oscillation reappears when every aperture point gets its own
rigorous bounce angle instead of one shared constant. **But that recovered
oscillation cannot be read as evidence for a real y-wall echo either** — a
structural finding, independently confirmed three ways in this cycle's own
Phase 2 (EM analytically, QUANTUM empirically via a reflectance-ablation
control, Red Team from scratch a third way, and reproduced a fourth time by
me below) — because both governing per-point quantities
(`theta_local(y_s)`, `dist_image(y_s)`) are, by the model's own
construction, static functions of geometry with zero dependence on the
swept beam angle. The entire recovered `theta_beam`-dependence is therefore
inherited from the same aperture window that already produces T21's own,
independently-established fringe in the direct field — confirmed directly,
not argued, by the committed reflectance-ablation control (`r≡1` reproduces
the r-weighted model's periods to `≤0.023°`). This is a real narrowing of
the T28 board (an entire construction family — single-point AND full-
aperture image-source reductions — is now shown incapable of ever
answering the question it was built to answer) but it is not progress
toward the phenomenon program's actual target, and it does not close the
y-wall mechanism class itself (Red Team's own Phase-2 audit correctly
ruled Checkpoint criterion 2 NOT YET RIPE — a genuinely different
construction, plane-wave/global-steering rather than per-point-image, is
untested). PARTIAL, not PROMISING (nothing here advances constraint 3) and
not RULED OUT (the mechanism class survives this cycle, narrowed to a
specific, now-exhausted sub-family).

**On the task's central question — is the corrected record now legible and
honest?** Yes, substantially. This is a genuine improvement over this exact
sub-thread's own recent history (§2 below): I found no analogue of exp-078's
own stale `§5.2` table, and no analogue of exp-077's LOGBOOK-level R9 defect.
Every docket item Red Team's Phase-2 audit ordered is actually present,
correctly worded, and numerically consistent with the JSON in the final
`phase1_proposal.md`. I found exactly one small, real, previously-uncaught
inconsistency (§2c) — a section left unrevised after a downstream section
resolved the exact gap it names — non-load-bearing, but worth fixing before
Iteration 57 cites this record.

---

## 2. Independent re-verification (R4) and commensurability audit

I did not restate any figure from `phase1_proposal.md`, `phase2_redteam_
audit.md`, `phase3_synthesis.md`, or `phase4_results.md`'s prose. Every
number below was recomputed by re-running `y_wall_aperture_sum.py` myself
and reading the raw committed JSON directly, not from any document's
narrative about either.

### 2a. Full reproduction — bit-identical

`python3 y_wall_aperture_sum.py`, re-run from this directory: diffs against
the committed `_output.txt` at exactly one line (`elapsed: 3.0s` vs `3.1s`,
timing noise); `y_wall_aperture_sum_results.json` unchanged on re-run (no
diff written to disk). Independently recomputed, from the raw JSON, not
from any document's prose:

- `rel_dev(PAIR_PAD vs T28)`: `|1.9924812030075187−4.611289746337977| /
  4.611289746337977 = 0.5679123818689048` — matches the committed
  `0.5679123818689048` exactly.
- `rel_dev(C80−C40 vs T28)`: `|2.030075187969925−2.8421052631578947| /
  2.8421052631578947 = 0.28571428571428564` — matches exactly, confirming
  the one nominal SUPPORT reproduces.
- `rel_dev(PAIR_PAD vs T21's exact 1.9607950099405438°)`:
  `0.016159870310938705` — matches the cited "1.6%" figure.
- **The orders-of-magnitude correction (Red Team's Attack 2/§3, adopted at
  Phase 3): independently re-derived from the raw `ss_tot_sanity` block,
  not from any party's stated figure.**
  `log10(9.391588920648808e-07) − log10(5.934e-27) = 20.199391...` — the
  comparison the document's prose actually names is **~20.2 orders**, not
  nine. The *different* comparison that IS approximately nine —
  `log10(6.047496634342288e-11) − log10(1e-20) = 9.781575...` — is a
  distinct pair of numbers, correctly disambiguated as such in the final
  document. Both figures independently reproduce to the printed digit, and
  I confirmed via `grep -rn "orders of magnitude"` across every `.py`/
  `.json`/`.txt` file in this directory that neither figure is hand-typed
  anywhere in code — both are prose-only, computed here from committed
  primitives, matching the discipline this correction itself enforces.
- **The reflectance-ablation control (docket item 3): independently
  re-verified from the raw JSON.** `reflectance_ablation_control.pair_
  absorb40.ss_tot_full = 0.0` exactly, with `ss_tot_degenerate: true` — the
  `SS_TOT_DEGENERATE` guard (exp-078's own hardening) correctly firing on a
  genuinely, bit-identically flat array, for the first time on real
  (non-synthetic) input, exactly as `phase4_results.md` §4 states.
  `abs_period_shift_vs_primary_deg.pair_pad = 0.015037593984962294` and
  `.c80_c40 = 0.022556390977443996` — both match the document's cited
  `≤0.023°` figure.
- Gates at the full `[4.77°,15.50°]` envelope: `G-LOSSLESS
  2.220446049250313e-16`, `G-N1 5.4025784115714076e-15`, `G-PASSIVITY
  0.00011512700876875968` — all reproduce exactly, all clean.
- Convergence check: relative change `2.431×10⁻⁴` (1x→2x), `1.496×10⁻⁵`
  (2x→4x) — reproduces exactly, well under the pre-registered `<1%` bar.

No R4-shaped defect found anywhere in the final `phase1_proposal.md`: every
number I checked traces to an actual computation, not a transcription.

### 2b. R9 registry check — independently re-derived, clean

Both operands of every scored comparison (`rel_dev`) are best-fit periods
in degrees-of-θ, produced by the identical imported `_free_period_search`
machinery applied to real and model curves alike — same units, same
algorithm, confirmed by direct inspection of `score_period()` and its
callers, not accepted from either the proposal's or Red Team's own R9
ruling. The two `ss_tot`-based comparisons (`~20.2` orders vs `~9.78`
orders) are, after the correction, each internally commensurate (both
operands are `sum((y−mean(y))²)` on the same proxy curve's own native
units) and, critically, are now clearly labeled as two *different*
comparisons rather than conflated into one — I checked this is true
throughout the corrected document (§1, §5.2, §7 all state both figures
with the same disambiguating language, not just the one section Red Team's
audit happened to quote). **No R9-shaped defect found anywhere in this
cycle's own scoring**, independently re-derived, not accepted on Red Team's
word.

### 2c. A small, real, previously-uncaught inconsistency: §4's R5 disclosure was never updated after §5.3/§7 resolved the exact gap it names

`phase1_proposal.md` §4 still reads, verbatim, in the final, corrected
document:

> "No null-permutation control is run here. §5.4's comparison against T21's
> own fringe period is a SINGLE, targeted, pre-named comparison... disclosed
> as a real, if narrower, gap: **Phase 2 may still reasonably require a
> formal look-elsewhere control before treating even this single
> T21-proximity finding as fully established**, particularly given the one
> nominal Test-A SUPPORT below (§5.3)."

This is the as-filed framing, carried forward unrevised. But Phase 2 *did*
run — and Red Team's own audit explicitly ruled (its §6, R5 registry,
independently re-read here) that a generic null-permutation control would
have been "the wrong tool" for this specific gap, and that QUANTUM's
reflectance-ablation control (`r(theta_local)≡1`) is the correct,
**superseding** resolution, mandated into the committed record as docket
item 3. That item was executed faithfully — §5.3 and §7 of the final
document both correctly state the ablation result and explicitly rule the
one nominal SUPPORT "non-informative... now that the ablation control is in
the record." **But §4 itself was never touched**: a reader who reads only
§4 (a natural stopping point — it is the falsifiability/pre-registration
section, the place a reader checks what was and wasn't controlled for)
comes away believing a "may still reasonably require" open question sits
unresolved, when two sections later the same document treats that exact
question as closed, by a stronger and more specific test than the one §4
still asks for. This is the identical *shape* of defect this seat's own
Iteration-55 review caught in exp-078 (a stale in-place passage sitting
under, or in this case ahead of, a correction that resolves it) — smaller
in degree (a disclosure paragraph, not a numeric table; internally
inconsistent within one document, not carried across a cycle boundary into
LOGBOOK) but the same failure mode. **Non-load-bearing**: no scored number
or verdict depends on §4's own wording, and a careful reader who reaches
§5.3/§7 gets the correct, resolved picture — but it is worth a one-sentence
same-shift fix (cross-reference §5.3's ablation control from §4, or delete
the "Phase 2 may still reasonably require" clause) before Iteration 57
cites this record as fully self-consistent.

### 2d. What I did NOT find

Unlike exp-078 (a stale five-row table reproducing wrong-angle numbers
under a "CORRECTED" label) and exp-077 (a dimensional-error comparison that
survived one full cycle into LOGBOOK's permanent record), I found **no**
comparable defect at the level this document's own headline claims rest
on. Every one of Red Team's nine mandatory-fix docket items is present,
correctly worded, and numerically verified against the JSON: the
structural Idealization 9 (theta_beam-independence), the reframed §4/§7
headline (branch (b), refined — not a third branch), the folded-in
ablation control, the corrected orders-of-magnitude figures (both, clearly
disambiguated), the falloff Idealization 10, the residual-sideband
companion note, the THERMO N/A sentence, and the `A_eff≈518.81` forward
caution against LOGBOOK's own R5-addendum dead end. This is a genuine
improvement in cycle-to-cycle correction discipline over this exact
sub-thread's own recent history, worth stating plainly rather than only
reporting what I found wrong.

---

## 3. Ranked top-3 Iteration-57 candidates

Checked against R1–R9 and T28's named dead ends first: none of the three
below revisits a ruled-out idea. In particular, none proposes shrinking
this construction's effective aperture toward T28's own period — this
cycle's own forward caution (§2c of the corrected proposal) correctly
identifies that path as re-approaching `A_eff≈518.81`, LOGBOOK's own R5
addendum dead end (Iteration 47, `null_p=0.497`).

### #1 — Test whether the empty-scene T28 signature survives with a real absorbing article loaded (deferred FOUR consecutive cycles now: exp-076, -077, -078, -079)

This is my own seat's charter-relevant candidate, named explicitly in my
own prior-cycle review and in the standing Iteration-54 ranking ("should
not be deferred a third time without an explicit reason") — and this
cycle deferred it a **fourth** time, again without a stated reason in its
own record. The case for ranking it #1 is stronger after exp-079 than it
was after exp-078, not merely repeated: this cycle just showed that an
entire *family* of mechanism instruments (the single-edge reduction AND
the full-aperture generalization) is structurally incapable of ever
resolving whether a real y-wall echo exists. Continuing to refine
mechanism models on an empty domain, when the empty-domain signal's
relevance to the actual phenomenon program has never once been tested,
risks a ninth, tenth, eleventh cycle of instrument-fidelity work on a
question that may not matter to constraint 3 at all. This is cheap
relative to a new mechanism build (reuses `graded_black_shell` and the
already-validated `C_empty`-family instrumentation, zero new machinery)
and is the one test that would tell the program, directly, whether any of
this eleven-cycle sub-thread has downstream relevance — a fundamentally
different kind of information than another period-matching exercise can
supply, however well-instrumented.

### #2 — If mechanism-hunting continues at all: the plane-wave/global-steering y-wall reconstruction, pre-registered against this cycle's own specific failure mode

Red Team's own §8/§9 recommendation (independently endorsed after tracing
through the mathematics myself, §2a above): the productive next
architecture, if this sub-class is worth testing further, is one that
breaks the "static per-point angle" pattern that has now defeated two
consecutive constructions — a global-steering incidence-angle picture
analogous to what already makes the x-wall's own two-plane-wave reduction
`theta_beam`-sensitive to the wall's actual reflectance. I add one
concrete guard, drawing on this exact sub-thread's own repeated history of
convention bugs (the x-wall admittance question, the y-wall angle
convention wrong once at exp-078's own Phase 1, then found to be
*insufficiently* corrected at exp-078's own Phase 5): **before any code is
written, the Phase-1 proposal must state, in one sentence, the specific
test that would show this new construction's `theta_beam`-dependence is
NOT solely inherited from the shared aperture window** — the exact
ablation-control idiom this cycle used, generalized into a pre-registered
requirement rather than a Phase-2 afterthought. Without that guard, a third
consecutive y-wall instrument risks the same discovery, one phase later,
that its headline result was never capable of discriminating anything.

### #3 — The full-width, non-aliased second-wavelength (`G40`) leg (also deferred FOUR consecutive cycles)

Orthogonal to the mechanism question entirely, and cheap (the cheapest
remaining FDTD test on the whole T28 board): does the ~2.84°-family
periodicity scale with wavelength the way a real physical effect must,
independent of which — if any — mechanism explains it? This has been
named in every T28 ranking since Iteration 53 and executed in none of
them. Running it does not depend on resolving #1 or #2 first, and a
negative result there (the periodicity fails to scale correctly) would be
a decisive, independent way to close a large part of the mechanism-hunting
question without needing a third y-wall model at all.

---

## 4. Seat-specific finding

Stated plainly, as instructed: no perceptual threshold applies to this
cycle's record — no contrast measurement, no luminance edge, no adaptation
state, no constraint-3 scene exists anywhere in `y_wall_aperture_sum.py`,
confirmed by my own read of the file (only `ABSORB`, `PAD`, and period/
reflectance quantities appear; no Weber-contrast, no `C_thr`, no ambient
computation). What I contributed this cycle, matching this seat's standing
duty on this exact sub-thread: an independent, from-scratch reproduction of
every load-bearing number (§2a), a from-scratch R9 commensurability check
that did not merely accept Red Team's own clean ruling (§2b), and — going
one level past what Red Team's own thorough audit checked — a pass over
whether the corrected document is internally self-consistent *everywhere*
a resolved question is discussed, not just at the section that states the
resolution. That pass found one small, real, non-load-bearing gap (§2c) and,
just as importantly, found the sub-thread's two most recent named failure
patterns (a stale table under a "CORRECTED" label; a dimensional error
surviving into LOGBOOK) genuinely absent this cycle — a finding worth
reporting with the same rigor as a defect would be.

---

## Bottom line

**PARTIAL.** exp-079 correctly and honestly establishes that the flat,
zero-signal result from exp-078's single-edge reduction does not survive
generalization to the full coherent aperture sum, but — independently
reproduced here a fourth time, after EM, QUANTUM, and Red Team's own
Phase-2 work — that recovered signal is mechanistically T21's own,
independently-established fringe, not evidence for or against a real
y-wall echo, because this entire per-point-image construction family is
structurally incapable of carrying that information regardless of the
wall's true reflectance. The corrected write-up is, on independent
verification, legible and honest: every mandatory-fix docket item is
correctly executed and numerically confirmed from the raw JSON, and this
cycle avoids both of this sub-thread's two most recent named failure
patterns. One small, real inconsistency remains (§4's R5 disclosure was
never updated after §5.3/§7 resolved the exact gap it names) —
non-load-bearing, worth a one-line fix. My top-ranked Iteration-57
candidate is, again, the now-four-times-deferred test of whether this
entire instrument-fidelity signature survives with a real absorbing
article in the domain — more urgent after this cycle than before it, since
an entire construction family has now been shown incapable of resolving
the mechanism question on an empty scene.
