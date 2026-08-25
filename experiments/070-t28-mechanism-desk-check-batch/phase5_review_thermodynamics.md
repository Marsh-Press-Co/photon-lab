# PHASE 5 — REVIEW · Panel Iteration 47 · Seat: THERMODYNAMICS
## On exp-070, "T28 mechanism, desk-check batch"

**Charter, verbatim:** where absorbed energy goes; what re-radiates and
whether it would be detectable; owns the per-proposal energy sidecar
(absorbed power → temperature rise → emission band → detectability),
labeled as a post-run analytic calculation, not an FDTD output. Fresh
context this phase, blind to any other seat's Phase-5 review this cycle.

## 1. The WKB/adiabatic boundary-reflectance disclosure — checked, accurate, findable

PLAN.md's Iteration-47 queue named one capacity-permitting fold-in:
"THERMODYNAMICS' own desk-only WKB/adiabatic boundary-reflectance model
for the graded-loss `ABSORB` band folds into this same batch if capacity
allows." My own Phase-2 critique (`phase2_critique_thermodynamics.md`)
flagged its total absence from the Phase-1 proposal as this cycle's one
concrete charter-relevant defect — real, not cosmetic, but minor (Phase-1
had no equivalent of exp-069's own R_contact "disclosed, not silent" line
for it).

Red Team's Phase-2 audit independently re-confirmed the omission by full-
text grep (Attack 6), ruled it "real but minor," and wrote the exact
mandatory-fix language (docket item 6): a one-line disclosure, not a
requirement to actually build the WKB model this cycle. Phase 3 accepted
this in full, no override.

**Verified in NOTES.md**: a dedicated, clearly labeled section, "Disclosed
scope choice (docket item 6)" (lines 89–96), reads:

> PLAN.md's Iteration-47 queue item 1 named a capacity-permitting fold-in:
> "THERMODYNAMICS' own desk-only WKB/adiabatic boundary-reflectance model
> for the graded-loss `ABSORB` band." **Not picked up this cycle.** No
> capacity constraint prevented it — this is a scope choice (the batch as
> designed answers a geometric/statistical question, not a boundary-physics
> one), disclosed rather than silent, per Red Team's Attack 6 ruling.

This is close to verbatim Red Team's own docket-item-6 language, sits as
its own heading (not buried inside a numbered idealization list — though
Idealization 10 also cross-references it, which is a reasonable belt-and-
suspenders repetition, not a dilution), and is honest about the actual
reason: a stated scope choice, not a capacity excuse. **Not watered down.
Finding: no defect here.**

## 2. THERMODYNAMICS standing this cycle — confirmed still low, checked against actual results, not just the proposal

My Phase-2 steel-man predicted this would be "a rare cycle where the
charter has little physics to grade" because the scene is empty — no
object, no absorbed power, no ΔT, no emission band. I re-checked this
against the actual Phase-4 output, not just the Phase-1 framing, because a
result *could* in principle have surfaced something requiring an energy-
sidecar sanity check even in a scene that started empty (e.g., if a
result had turned on absorbed-power differences between `C40`/`C80` as an
explanatory variable).

It did not. Walking all five scored predictions against `results.json`:

- **P-070-1 (CONFIRM)** — a period-matching statistic on already-recorded
  field/flux curves. No power or temperature quantity anywhere in its
  computation chain.
- **P-070-2, P-070-4 (both NEITHER)** — pure geometric/statistical
  arithmetic (beat-frequency reconstruction, named-constant search,
  permutation-null control) over FDTD *construction* constants (grid
  padding, absorbing-boundary depth in cells, taper length, clearances).
  These are domain bookkeeping numbers, not material or energy
  parameters — the batch's own mandatory disclosed caveat (docket item 5,
  MATERIALS') makes exactly this point for realizability; the same
  reasoning means there is no absorbed-power quantity here for
  THERMODYNAMICS to sanity-check either.
- **P-070-3 (REFUTE)** — a single closed-form geometric ratio
  (`TAPER=40` cells as an aperture). No energy content.
- **P-070-5 (REFUTE)** — a set-overlap check between two already-computed
  match lists. No energy content.

None of the five items computes, cites, or implicitly leans on absorbed
power, ΔT, or an emission/re-radiation band. The one item that comes
closest to a physical-mechanism claim — P-070-1's finding that the
~2.84°-family signal is config-invariant, "disfavoring an ABSORB-depth-
tied mechanism" — is a claim about diffraction *geometry* (does the
period depend on which config you're in), not about how much energy the
`ABSORB` band's differing depth (40 vs 80 cells) actually dissipates. It
would only touch my charter if a future step reads it as evidence about
absorbed-power *magnitude* between configs — it is not that, and NOTES.md
does not claim it is. **Confirmed: this remains a genuinely low-standing
cycle for THERMODYNAMICS, verified against the actual results, not merely
inferred from the proposal's framing. No result here implicitly requires
an energy-sidecar check I should flag.**

## 3. Independent numeric verification

Re-ran `desk_check_mechanism.py` directly against the committed
`results.json` (fixed seed 0, as documented in `phase4_results.md`): the
regenerated file is byte-identical to the committed one (`git status`
clean after the re-run) — the determinism claim holds, not merely
asserted.

Spot-checked every headline figure in `NOTES.md`/`phase4_results.md`
against `results.json` directly:

| Claim | NOTES.md / phase4_results.md | results.json | Match? |
|---|---|---|---|
| P-070-1 C40 dev | 14.29% | `rel_dev_from_delta_period: 0.142857...` | yes |
| P-070-1 C80 dev | 10.85% | `0.108466...` | yes |
| P-070-2 "plus" best_rel | 0.0148% | `0.00014806...` | yes |
| P-070-2 "minus" best_rel | 0.081% (NOTES) / 0.0807% (phase4) | `0.0008069...` | yes |
| P-070-2 null_p (plus/minus) | 0.204 / 0.806 | `0.20385` / `0.8055` | yes |
| P-070-3 rel_dev | 1197% | `11.9702...` (×100) | yes |
| P-070-4 best_rel | 0.036% (NOTES) / 0.0363% (phase4) | `0.00036268...` | yes |
| P-070-4 null_p | 0.497 | `0.4969` | yes |
| P-070-4 R²(750nm) | 0.7663 | `0.76633...` | yes |
| Search space size / distinct values | 36,680 / 7,179 | `36680` / `7179` | yes |
| P-070-5 overlap | zero, both branches | `{"plus": [], "minus": []}` | yes |

**No numeric or citation defect found.** This is a well-disciplined
write-up: every reported figure traces cleanly to the committed JSON, the
tie-counts (3-way, 2-way, 6-way) match the listed `tied` arrays exactly,
and the two places where NOTES.md rounds to one more or fewer decimal
than `phase4_results.md` (0.081% vs 0.0807%; 0.036% vs 0.0363%) are
ordinary rounding, not inconsistency.

## 4. Verdict

**Nothing load-bearing from THERMODYNAMICS this cycle.** The one
charter-relevant item this seat flagged at Phase 2 (the WKB fold-in) was
correctly and honestly disclosed exactly as Red Team's docket mandated —
findable under its own heading, not diluted into a footnote, and honest
about the reason (scope choice, not capacity). The charter's substantive
question — where absorbed energy goes — has no object in this scene to
ask it about, confirmed against the actual Phase-4 results rather than
assumed from the Phase-1 framing. All independently-checkable numbers in
NOTES.md/phase4_results.md reproduce exactly against results.json and
against a fresh re-run of the committed script. This is a legitimate
"nothing to report" cycle, consistent with this seat's own Phase-2
self-assessment and this program's own precedent for honest null findings
(exp-069's own low-content Phase-5 cycles for seats without a live
question that cycle).

## 5. Should the WKB fold-in now become a dedicated future item?

I have standing to argue this, per this task's brief, given T28's own
P-070-1 result — and I think the answer is **yes, but ranked behind two
items with a more direct claim on the next FDTD dollar**, for a reason
that is itself thermodynamic: P-070-1's finding (the signal is
config-invariant, disfavoring an `ABSORB`-depth-tied mechanism) is
*evidence against* the boundary-reflectance model being T28's driver, not
evidence for building it. If the ~2.84° period lived in the shared
geometry (`R_OUT`/`W_OBJ`, `TAPER`, etc.) rather than in the one thing
that differs between configs (`ABSORB` depth, 40 vs 80 cells), then a
model of how `ABSORB`'s own depth changes its reflectance is modeling the
less-likely branch first. It is still worth doing — EM's own C60/C70 test
(PLAN.md queue item 2) directly varies `ABSORB` and could revive the
`ABSORB`-tied hypothesis if it CONFIRMs, at which point the WKB model
becomes the natural next analytic step to explain *why* — but doing it
now, ahead of that falsification test, would be answering a question this
cycle's own result just made less likely to be the live one.

## Ranked top-3 candidate directions for Iteration 48

1. **EM's C60/C70 falsification test** (PLAN.md queue item 2, first
   branch) — reuses already-built congruent configs at zero new `lab/`
   diff, directly tests whether the ~2.84° period tracks `ABSORB` depth,
   the one variable this cycle's own P-070-1 result flags as the
   remaining live discriminator between "config-invariant geometric
   effect" and "ABSORB-tied effect." This is the most direct next FDTD
   spend and is exactly what exp-070's own "Next" section (and this
   seat's own analysis above) points to first.
2. **A dedicated THERMODYNAMICS WKB/adiabatic boundary-reflectance
   estimate for the graded-loss `ABSORB` band** — genuinely queued now
   (not before), conditioned on EM's C60/C70 test: if it CONFIRMs an
   `ABSORB`-depth dependence, the WKB model is the natural mechanism-level
   follow-up to explain the reflectance-vs-depth relationship; if it
   REFUTEs, the WKB fold-in should be dropped from the active queue
   entirely rather than carried forward a third cycle, since P-070-1 and
   a C60/C70 REFUTE together would leave no remaining reason to suspect
   `ABSORB`'s own optical property is T28's driver. Either way, this
   should not run *before* C60/C70 — it answers "why" only after C60/C70
   answers "whether."
3. **R_contact's `measured_direct` literature search** — unchanged
   ranking from Iterations 45–47's own queue (PLAN.md item 3), still the
   only item across six cycles now that can move a real materials number,
   still blocked purely on WebSearch/WebFetch tooling availability, zero
   resource competition with items 1–2.
