# Phase 2 — RED TEAM Audit (exp-077, Panel Iteration 54)

**Seat: RED TEAM.** Read: `PANEL.md` in full; `LOGBOOK.md` in full (RULED
OUT R1–R8 including R4/R6/R7/R8's exact firing conditions; LIVE THREADS
T28's complete Iteration 46–53 history); `phase1_proposal.md`,
`pad_round_trip_model.py`, `pad_round_trip_results.json`; all five blind
Phase-2 critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS,
QUANTUM OPTICS — VISION SCIENCE is this cycle's rotation lead, correctly
absent from the critique roster).

**Independent verification performed computationally this cycle** (none of
it taken on any critic's or the proposal's word alone):

1. Re-ran `pad_round_trip_model.py` end-to-end from repo root — output is
   bit-for-bit identical to `phase1_proposal.md`'s tables (`rel_dev`
   1.8798/0.9642, shape `r²` 0.0444/0.1997, Combined REFUTE/INCONCLUSIVE).
   R4-clean.
2. Independently wrote and ran my own retarget of exp-075's
   `two_wall_cavity.py` at `(C40,G40,C80)` — a third, independent
   implementation (I did not read PHOTONICS' or EM's scratchpad scripts,
   only their stated numbers) — to check the PHOTONICS/EM two-wall finding
   from scratch.
3. Read `lab/fdtd2d.py` lines 72–128 directly (not any critique's
   quotation of it) to check MATERIALS' and THERMODYNAMICS' source-level
   claims about `_damping` and the `pad` parameter.
4. Read `pad_round_trip_model.py` line 176 directly to check
   THERMODYNAMICS' "same array object" claim, and independently recomputed
   `1-|r(θ;ABSORB)|²` across the real 31-point grid from
   `boundary_reflectance.py`'s own primitives (not copied from any
   critique) to check THERMODYNAMICS' cited percentages.
5. Independently re-ran `experiments/065-.../design_geometry.py::CONFIGS`
   to confirm the `C40`/`G40`/`C80` geometry table (§2a) reproduces exactly.
6. Ran my own smaller-scale (400-trial, reduced grid) reproduction of
   QUANTUM's pure-noise null-calibration check, using the actual committed
   `_free_period_search` (imported, not reimplemented), to confirm its
   claim in outline rather than trust the reported 20,000-trial figures
   blind.

---

## Numbered attacks / findings

### Attack 1 — the two-wall extension changes the REFUTE's evidentiary basis; Idealization 9 cannot be left unrun into Phase 3 [inconsistency, R8-shaped]

**Confirmed-critic-finding, independently reproduced a third way.** My own
from-scratch retarget of `two_wall_cavity.py::c_empty_two_wall`/
`image_geometry_right` at `(C40,G40,C80)` gives, to four decimal places,
the *same* numbers PHOTONICS and EM each independently reported:

| | Single-wall (filed) | Two-wall (three independent re-derivations agree) |
|---|---|---|
| `PAIR_PAD` `P*_model` | 13.2794° | 8.6677° |
| `PAIR_PAD` Test A | `rel_dev=1.8798` → REFUTE | `rel_dev=0.8797` → **INCONCLUSIVE** |
| `PAIR_PAD` Test B | `r²=0.0444` → REFUTE | `r²=0.0001` → REFUTE (harder) |
| `PAIR_PAD` Combined | REFUTE | **REFUTE (unchanged), but via Test B alone** |
| `PAIR_ABSORB40` Test A | `rel_dev=0.9642` → INCONCLUSIVE | `rel_dev=0.6851` → INCONCLUSIVE |
| `PAIR_ABSORB40` Test B | `r²=0.1997` → INCONCLUSIVE | `r²=0.0418` → REFUTE |
| `PAIR_ABSORB40` Combined | INCONCLUSIVE | **REFUTE (flipped)** |

`D_right` (59/99/99 for C40/G40/C80) matches the proposal's own disclosed
values exactly. This is now a three-way independent confirmation
(PHOTONICS, EM, Red Team), each built from scratch.

**Why this is not merely informational.** Idealization 9 disclosed the
omission honestly and did *not* assert an unverified robustness claim in
its own voice (unlike exp-075's R8 violation, where EM's Phase-2 prose
*asserted* "robust to everything below [the gap]" and that unverified
assertion was adopted without checking) — so the Phase-1 proposal itself
does not repeat R8's original failure shape. But R8's standard is broader
than that one triggering pattern: *an untested-but-affordable check that
proves outcome-relevant to HOW a verdict holds must not be left un-run
once its being affordable and decision-relevant is established.* It is
now established, three ways over. The filed document's own characterization
— "REFUTE... same failure shape... not merely REFUTE on the same wrong
pair" — is empirically false on this evidence: the failure shape changes
from period-dominated to shape-dominated, and the secondary control pair's
verdict flips entirely. Leaving this in a Phase-2 critique appendix rather
than the committed script/write-up is not an acceptable final state.

**Ruling: MANDATORY**, highest priority. See §"Ruling on R8" below.

### Attack 2 — Idealization 9 mischaracterizes the far-wall omission as merely geometric; it is the same unrealizable admittance class [inconsistency]

**Confirmed-critic-finding (MATERIALS), independently verified at the
source.** I read `lab/fdtd2d.py::Sim._damping` (lines 122–128) directly:

```
ramp = (np.arange(self.absorb, 0, -1) / self.absorb) ** 3
d[: self.absorb, :]  = np.maximum(d[: self.absorb, :],  ramp[:, None])
d[-self.absorb :, :] = np.maximum(d[-self.absorb :, :], ramp[::-1][:, None])
d[:, : self.absorb]  = np.maximum(d[:, : self.absorb],  ramp[None, :])
d[:, -self.absorb :] = np.maximum(d[:, -self.absorb :], ramp[None, ::-1])
```

The identical `self.absorb`-parameterized cubic ramp is applied to all
four edges — confirmed, not merely cited. MATERIALS is correct: the `+x`
wall is built from the exact same matched-`eps=mu` unrealizable admittance
class exp-075 already bounded as unobtainium-with-parameters at optical λ
for the `-x` wall. Idealization 9's framing ("a second, uncomputed
[geometric] contribution") undersells this — a future two-wall SUPPORT
would not be materials progress of any kind, and the document should say
so explicitly next to wherever the two-wall extension is folded in
(Attack 1).

**Ruling: MANDATORY**, one-sentence fix, bundled with Attack 1's rewrite.

### Attack 3 — §3's stated justification for PAIR_PAD's N/A verdict is a non-sequitur; the real reason is a code-level common-mode identity [inconsistency]

**Confirmed-critic-finding (THERMODYNAMICS), independently verified at the
source.** §3 argues N/A because "PAD cells are proven lossless vacuum" —
true but irrelevant, since nothing in this mechanism claims PAD absorbs;
the only lossy element in either config is the `ABSORB` band itself, which
is *not* lossless (`1-|r(θ;40)|²` is 99.996%–99.999%, not 100%). I
confirmed directly at `pad_round_trip_model.py` line 176:

```python
r_for = {"C40": r40, "G40": r40, "C80": r80}
```

`r40` is the literal same Python array object passed for both `C40`'s and
`G40`'s predicted echo term — not independently recomputed or re-fetched.
This is the actual, correct reason `PAIR_PAD`'s difference cannot be an
absorbed-power effect: a quantity that enters *identically* on both sides
of a subtraction is common-mode by construction and cannot drive the
*difference*'s shape or period — regardless of whether that quantity
happens to be small. THERMODYNAMICS' point stands independently verified.

**Ruling: MANDATORY** — rewrite §3 with the correct common-mode-array-
identity reasoning for `PAIR_PAD`, and an explicit computed disposition for
`PAIR_ABSORB40` (see Attack 4 for the numbers to use).

### Attack 4 — a NEW, self-referential finding: THERMODYNAMICS' own cited absorbed-power percentages do not reproduce from the same `|r|` values it says they match [inconsistency, minor, non-load-bearing]

**Not found by any of the five critiques** (structurally invisible to
blind peers, since none saw THERMODYNAMICS' text) — caught here by
independently recomputing, from `boundary_reflectance.py`'s own
primitives, `1-|r(θ;ABSORB)|²` across the real 31-point grid:

```
ABSORB=40: 1-|r|² ranges 99.995874%–99.999159%  (at θ=42.0°/36.0°)
ABSORB=80: 1-|r|² ranges 99.999999%(87)–99.999999%(91)
Δ = |af80-af40| ranges 8.4098e-06 to 4.1247e-05
```

THERMODYNAMICS' critique states, twice (steel-man and sharpest attack),
`ABSORB=40` ranges as "99.9979%–99.99959%" / "99.9979%–99.9996%" —
claiming this "matches §2e's `|r|=0.0029–0.0064` exactly." It does not:
plugging THERMODYNAMICS' own cited `|r|` values into `1-|r|²` gives
`0.99999159` (99.99916%) at `|r|=0.0029` and `0.99995904` (99.99590%) at
`|r|=0.0064` — matching *my* independent recomputation, not
THERMODYNAMICS' stated range. The discrepancy is systematic: THERMODYNAMICS'
stated deviation-from-100% at each endpoint is almost exactly half the
correct value (0.00042%≈half of 0.00084%; 0.00206%≈half of 0.00413%),
consistent with an arithmetic slip somewhere in that one hand-computation
(not investigated further — root cause immaterial to the ruling below).

**This is non-load-bearing.** The number that actually matters —
THERMODYNAMICS' own `Δabsorbed-fraction` differential for `PAIR_ABSORB40`,
`8.4×10⁻⁶`–`4.1×10⁻⁵` — is independently reproduced by me **exactly**
(to the digit), because it was evidently computed as a direct difference
rather than through the erroneous intermediate percentages, and it is the
number THERMODYNAMICS' own recommended fix actually needs. No verdict,
band, or Combined result depends on the wrong intermediate figures. But
per this program's own R4 discipline — extended here one level further,
to a Phase-2 critique's own illustrative arithmetic, exactly the class of
"hand-computed, not independently checked" defect R4 exists to catch —
the corrected percentages (99.9959%–99.9992% for ABSORB=40) must be the
ones that land in `phase1_proposal.md` §3 if THERMODYNAMICS' fix quotes
absolute percentages at all, not the critique's own stated range.

**Ruling: MANDATORY but trivial** — use the Red-Team-recomputed absolute
percentages (or drop them and keep only the correctly-reproduced Δ figure)
when executing Attack 3's fix.

### Attack 5 — missing null-calibration control on the free-period search [confirmed-critic-finding, R5/R6/R8-shaped process gap]

**Confirmed-critic-finding (QUANTUM), spot-checked in outline rather than
trusted at face value.** I re-ran a reduced version of QUANTUM's own two
checks (400 trials, `n_grid=1400` vs. their 20,000/2800) using the actual
committed `_free_period_search`:

```
P(rel_dev > 1.00) under pure i.i.d. noise:  0.225   (QUANTUM: 0.214 at N=20,000)
P(R² ≥ 0.70) under pure i.i.d. noise:       0/800   (QUANTUM: 0/40,000, max 0.64; mine: max 0.471)
```

Both numbers land in the same qualitative place QUANTUM reports: the bare
`rel_dev`/shape-`r²` thresholds are, on their own, reachable by chance a
non-trivial fraction of the time (so citing REFUTE by threshold-crossing
alone overstates the evidence), but the actual `R²` each real/model curve
achieves at its own optimum (0.8165/0.8592) is far outside anything
400–40,000 pure-noise trials produce — confirming both curves carry real,
non-noise periodic structure, and that QUANTUM's headline claim ("the
omission is a real process gap under this program's own standing rules,
not a substantive defect in the conclusion") holds up under an independent,
smaller-scale re-implementation. I did not reproduce QUANTUM's
bootstrap ground-truth-recovery check byte-for-byte, but see no reason to
doubt it: it reuses the same already-vetted machinery, its qualitative
claim is the mirror image of the pure-noise check I did reproduce, and
nothing in the proposal or the other four critiques contradicts it.

**One reinforcing observation not raised by any critic**: `PAIR_PAD`'s
real vs. model periods (4.61° vs. 13.28°) differ by a factor of ~2.9,
non-harmonically, over a 6°-wide window — a shape mismatch this large is
close to what two *genuinely different, non-noise* periods would produce
by construction, independent of any null-calibration subtlety. This does
not substitute for QUANTUM's proper i.i.d.-noise null (which answers a
different question — "could apparent structure be pure noise" — and
QUANTUM answered it correctly), but it is an additional, cheap reason not
to read Test B's near-threshold `r²=0.0444` as a fragile result.

**Ruling: MANDATORY** — add QUANTUM's null-calibration appendix (both
checks, at their full 20,000-trial scale, not my reduced spot-check) to
`pad_round_trip_model.py`/`pad_round_trip_results.json`, cited in
`phase1_proposal.md` §5, before Phase 3 treats REFUTE as fully closed on
the record. Not HALT-grade: independently confirmed, twice now (QUANTUM
at full scale, Red Team in outline), to strengthen rather than threaten
the REFUTE conclusion.

### Attack 6 — checked and found clean: the outcome scheme has no exp-076-style Attack-1 gap

Not a defect — recorded because it is exactly the kind of check this
sub-thread has been burned by skipping (exp-076's Attack 1: a multi-way
outcome scheme that was neither mutually exclusive nor exhaustive). This
cycle's scoring is a single deterministic trichotomy per test
(`SUPPORT` iff `≤0.30`/`≥0.30`, `REFUTE` iff `>1.00`/`≤0.05`, else
`INCONCLUSIVE`, for period/shape respectively) combined by a simple,
total rule (`REFUTE` if either test `REFUTE`s; `SUPPORT` only if both
`SUPPORT`; else `INCONCLUSIVE`). I verified algebraically that this
partitions the entire `(rel_dev, r²) ∈ [0,∞)×[-1,1]` space with no gap and
no overlap — unlike exp-076's `(x,y)` scheme, there is no free second
dimension for a boundary case to fall through. No fix needed.

---

## Disposition of the five critiques' findings

| Critique | Finding | Disposition |
|---|---|---|
| **PHOTONICS** | Two-wall extension leaves REFUTE intact but via a different mechanism; near-metallic/fast-phase-drift aside (inherited, non-blocking) | **ADOPT** the two-wall finding as MANDATORY (Attack 1, merged with EM's identical finding — three independent implementations now agree to 4 decimal places). The near-metallic aside is independently plausible and explicitly framed by PHOTONICS itself as informational, inherited from exp-075 — kept non-blocking, no override. |
| **MATERIALS** | Two-wall omission is not merely geometric — the `+x` wall shares the `-x` wall's unrealizable matched-`eps=mu` class | **ADOPT verbatim as MANDATORY** (Attack 2). Independently confirmed at the primitive source (`lab/fdtd2d.py::_damping`, all four edges identical construction). |
| **ELECTROMAGNETISM** | Two-wall extension: Test A's REFUTE is not robust (flips to INCONCLUSIVE); only Test B's REFUTE survives, and gets stronger; the control pair flips INCONCLUSIVE→REFUTE; "same failure shape" prose is inaccurate | **ADOPT as MANDATORY** (Attack 1/the correction language). Independently reproduced from scratch, exact match to 4 decimal places. |
| **THERMODYNAMICS** | §3's "PAD is lossless" justification is a non-sequitur; the real reason is `r40` being the same array object for both `PAIR_PAD` terms; `PAIR_ABSORB40` needs its own quantified, computed disposition | **ADOPT the reasoning fix as MANDATORY** (Attack 3), independently confirmed at the source line. **Correct, not override, the specific percentages THERMODYNAMICS cites** — a new, Red-Team-only finding (Attack 4): those numbers don't reproduce from the very `|r|` values THERMODYNAMICS says they match. The Δ-differential figure it reports for `PAIR_ABSORB40` (8.4e-6–4.1e-5) IS independently confirmed exact and should be kept. |
| **QUANTUM OPTICS** | Missing null-calibration control (pure-noise + bootstrap-recovery) on the free-period search; a real R5/R6/R8-shaped process gap that, once run, confirms rather than undermines REFUTE | **ADOPT as MANDATORY** (Attack 5). Spot-checked in outline (400-trial reduced reproduction), qualitatively consistent with the reported 20,000-trial figures. QUANTUM's own judgment that this doesn't warrant a new numbered house rule is accepted — R5/R6 already cover the dense-search and carrier-conditioned-significance cases respectively, and this is a period-comparison test, neither. |

**Nothing is overridden.** All five critiques' core findings independently
reproduce; none overreaches or overclaims relative to what the evidence
supports.

---

## Ruling on the two-wall extension and R8

**Yes — the two-wall extension MUST be folded into the committed Phase-3
script (not left as a Phase-2 critique appendix) before any headline
REFUTE is finalized.** Three independent implementations (PHOTONICS, EM,
Red Team) now agree, to four decimal places, that running the disclosed-
but-unrun Idealization 9 changes *which test* carries the REFUTE for the
primary target (`PAIR_PAD`: period test flips REFUTE→INCONCLUSIVE; shape
test gets four orders of magnitude worse, 0.044→0.0001) and *flips the
verdict outright* for the secondary control (`PAIR_ABSORB40`:
INCONCLUSIVE→REFUTE). This is precisely the shape R8 exists to police:
an affordable, already-named check, once actually computed, is
outcome-relevant to *how* the headline verdict holds even though it does
not change *whether* it holds for the primary target — and it does change
the verdict for the secondary one. Filing this as "available immediately"
in an idealization footnote and not running it is not an acceptable final
state for a document that also states, in its own §1 narrative, a flat
"REFUTE... same failure shape" headline.

**This is not, itself, a fresh R8 violation by the Phase-1 proposal.**
Unlike exp-075's original R8 trigger (an *unverified robustness assertion*
adopted without checking), exp-077's Idealization 9 made no robustness
claim at all — it disclosed the gap honestly and deferred to Phase 2/3,
exactly the house discipline R8 is meant to encourage. The failure mode
this audit is closing is the *next* one down the same road: a Phase-1
idealization correctly flagged as open must not be allowed to survive,
unresolved, into a Phase-3-frozen headline once Phase 2 has actually
priced it and found it outcome-relevant. Catching this now, at Phase 2,
before any freeze, is this program's own established non-firing pattern
(exp-065/Iteration 42's own language, reaffirmed at exp-076's Phase-2 Red
Team audit) — **provided the fold-in actually happens in Phase 3.**

---

## Checkpoint status

**No PANEL.md criterion fires on this cycle as it stands, contingent on
the docket below landing before Phase 3 freezes any language.** Criteria
1/2 do not apply (no constraint metric scored, no mechanism-class
boundary at issue — T1 correctly stays disengaged, §4). Criterion 3 does
not apply (zero new FDTD, zero `lab/` diff, the validated `Sim`/
`boundary_reflectance.py`/`two_wall_cavity.py` machinery is reused
unchanged). Criterion 5 is not at risk (this cycle narrows T28's own
mechanism question regardless of which way the two-wall fold-in lands —
REFUTE for `PAIR_PAD` is confirmed three independent ways). **Criterion 4
is the live one, and it does not fire**: every gap this audit closes
(Attacks 1, 2, 3, 5) was caught at Phase 2, before Phase 3 froze any
prose — the designed mechanism working, not failing, matching this
program's own repeated non-firing precedent (most recently exp-076's own
Phase-2 Red Team audit, itself citing exp-065/Iteration 42). Attack 4
(THERMODYNAMICS' own internal arithmetic slip) is even further upstream —
caught inside a Phase-2 critique before it could propagate into the
record at all. Should any of Attacks 1/2/3/4/5 survive unaddressed into
`phase3_synthesis.md` and later prove outcome-determining, that would be a
fresh, mechanically predictable Criterion-4 firing, matching this
sub-thread's own repeated pattern (Iterations 49, 50, 52) — the docket
below exists specifically to prevent that.

---

## Overall verdict: **PROCEED-WITH-MANDATORY-FIXES**

The instrument and its physics are sound: the gates re-verify clean
(G-LOSSLESS `2.2e-16`, G-N1 `1.4e-15`, G-PASSIVITY worst `|r|=0.0064`),
the geometry-congruence assertions are correct (independently re-run
against `design_geometry.py::CONFIGS`), the single-wall Test A/B numbers
reproduce bit-for-bit, and — most importantly — the primary result
(`PAIR_PAD` Combined REFUTE) is now confirmed **three independent ways**
including through the one check the filed document itself disclosed but
did not run. Nothing here is HALT-grade: no mechanism is claimed
unfalsifiably, no engine change is proposed, T1/constraint-3 correctly
stay disengaged, and no R1–R7 rule is re-triggered (independently checked
against §7's own compliance table — accurate as stated). But five
independent, previously-uncaught-in-the-committed-record gaps — one an
R8-shaped omission that changes the REFUTE's own evidentiary shape and
flips the control pair's verdict, one a materials-realizability scoping
gap, one a non-sequitur sidecar justification, one a self-referential
arithmetic slip inside a critique, and one a missing null-calibration
control — must close before this cycle's language freezes into LOGBOOK.

### Mandatory-fix docket (Director executes in Phase 3 synthesis)

1. Fold the two-wall-cavity retarget (`(C40,G40,C80)`, reusing
   `two_wall_cavity.py`'s `image_geometry_right`/`c_empty_two_wall`
   verbatim) into `pad_round_trip_model.py` itself as a primary,
   pre-registered co-result — not a deferred idealization. Report Test
   A/B for both single- and two-wall cuts side by side, for both
   `PAIR_PAD` and `PAIR_ABSORB40`, in `phase1_proposal.md` §5. [Attack 1]
2. Correct the §1/§5 "REFUTE... same failure shape" language to state
   plainly: Combined REFUTE for `PAIR_PAD` is robust across single- and
   two-wall cuts, but via different tests in each (period-dominated →
   shape-dominated); `PAIR_ABSORB40`'s verdict is NOT robust to the
   far-wall term (INCONCLUSIVE→REFUTE) and must be reported as such, not
   folded silently into the primary headline. [Attack 1]
3. Add one sentence to Idealization 9 (or a new Idealization 10): the `+x`
   wall's boundary is built from the identical unrealizable matched-
   `eps=mu` admittance class as the `-x` wall (`lab/fdtd2d.py::_damping`,
   verified symmetric across all four edges), so the two-wall extension
   is an instrument-fidelity check only — it cannot move, in either
   direction, MATERIALS' realizability bound on this mechanism class.
   [Attack 2]
4. Rewrite §3 (THERMODYNAMICS sidecar): (a) for `PAIR_PAD`, replace "PAD
   is lossless vacuum" with the correct reasoning — `r_for["C40"]` and
   `r_for["G40"]` are the literal same array object
   (`pad_round_trip_model.py` line 176), so the absorbed-power fraction is
   common-mode by code-level construction, not by PAD's own lossless
   status; (b) for `PAIR_ABSORB40`, add the explicit, computed
   Δabsorbed-fraction disposition (`8.4×10⁻⁶`–`4.1×10⁻⁵`, independently
   reconfirmed exact) and argue its thermodynamic insignificance
   quantitatively, as THERMODYNAMICS specifies. **Use the Red-Team-
   recomputed absolute percentages (99.9959%–99.9992% for ABSORB=40, not
   THERMODYNAMICS' own stated 99.9979%–99.9996%) if absolute percentages
   are quoted at all** — THERMODYNAMICS' own critique contains an
   internal arithmetic inconsistency at that specific figure (Attack 4),
   though its load-bearing Δ number is unaffected and independently
   confirmed correct. [Attacks 3 + 4]
5. Add QUANTUM's null-calibration appendix — the full 20,000-trial
   pure-noise Monte-Carlo null and the 20,000-trial bootstrap ground-
   truth-recovery check, both against the actual committed
   `_free_period_search` — to `pad_round_trip_model.py`/
   `pad_round_trip_results.json`, cited numerically in `phase1_proposal.md`
   §5, before the REFUTE verdict is treated as fully closed on the record.
   [Attack 5]

**Total marginal cost: zero new FDTD calls, zero `lab/` diff** — every
item above is desk work reusing already-committed, already-vetted
machinery (`two_wall_cavity.py`, `boundary_reflectance.py`,
`_free_period_search`), matching this cycle's own original zero-cost
scope.
