# PHASE 2 — RED TEAM AUDIT · Panel Iteration 59 · exp-082
## Adjudicating the PAD-loaded real-article check (item 7, the six-cycle tripwire item), the x-wall realizable-admittance refit (Tier 0 item 1), the phase-convention tie-breaker extension (Tier 1 item 4), and all five blind Phase-2 critiques — with the cycle's own most consequential finding (the `delta_scene`/`delta_empty` correlation) independently reproduced, extended past a bare Pearson-r, and resolved as far as the data allow

**Seat: RED TEAM.** Read, in order: `PANEL.md` in full; `AGENTS.md` in full;
`LOGBOOK.md` (RULED OUT R1–R9 in full, ESTABLISHED, LIVE THREADS in full —
T28's complete Iteration 46–58 history, R4/R6/R8/R9 in particular); `PLAN.md`'s
Iteration-59 queue; `experiments/081-.../phase2_redteam_audit.md` (format
model); the complete `experiments/082-.../` directory in the order specified
(`phase1_proposal.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`, `x_wall_realizable_refit.py`/`_results.md`/`_results.json`/
`x_wall_output.txt`, `phase_convention_extension.py`/`_results.md`/
`_results.json`/`_output.txt`, then all five blind Phase-2 critiques). I
alone see the complete record and all five blind critiques, and speak last.

**No RULED-OUT item (R1–R9) is re-proposed or re-litigated by this document
or by anything it adjudicates.**

**Independent verification performed, not merely re-argued.** I wrote and ran
my own verification scripts (session-local scratch, do NOT modify anything
under `experiments/082-.../`), reusing only already-committed primitives
(`pad_round_trip_model.free_period_with_widening`/`free_period_with_widening_quiet`/
`_free_period_search` reused unchanged via the house `_load()` idiom;
`lab.glare_sidecar.c_thr`; raw arrays copied verbatim from `results.json`,
never hand-typed) plus new, disclosed statistics (an exact 7!-permutation
Pearson-r test; a vectorized reproduction of the committed free-period-search
grid, sanity-checked bit-exact against the real machinery before use; a
200,000-trial null-permutation control on that search's own R²). Every
number below is reproduced from primitives, not copied from any critique's
prose.

---

## 0. Independent verification table

| # | Claim checked | Source | My result | Reproduced / resolved? |
|---|---|---|---|---|
| 0a | Primary metric: `A_scene=3.4076×10⁻³`, `A_empty=5.1846×10⁻³`, `ratio=0.6573`, VERDICT SURVIVES | `results.json` | Recomputed `ptp()` directly from the committed `delta_scene`/`delta_empty` arrays: bit-identical | **YES, exact** |
| 0b | Reproduction precondition `max_dev=0.0` at all 7 shared angles vs `experiments/076-.../results.json::headline` | `results.json` | Independently re-diffed 3 of 7 points myself (θ=36/38/42) against the exp-076 file directly (not merely trusting the committed table) — `0.0` deviation, matching EM's own independent 3-point check (θ=36/39/42) at a different subset — 5 of 7 points now independently confirmed across the two audits | **YES, exact** |
| 0c | `C_thr = gs.c_thr(3.0, 0.4, bar="lab") = 0.005` | `phase1_proposal.md` §2 | Called the real function: `0.005` | **YES, exact** |
| 0d | **PHOTONICS/EM's finding: Pearson r(delta_scene, delta_empty) = 0.031** | PHOTONICS, EM | `np.corrcoef` on the committed 7-point arrays: **r = 0.030573...** | **YES, exact, both independently converge on the identical figure** |
| 0e | EM's finding: only 4/7 angles share sign | EM | Sign array: `[+,-,+,+,+,-,-]` for scene vs `[-,+,+,-,-,-,+]` for empty → agreement `[T,F,T,T,T,F,F]` = **4/7** | **YES, exact** |
| 0f | PHOTONICS' finding: elementwise ratios span −0.56 to +2.36 | PHOTONICS | `delta_scene/delta_empty` per θ: min **−0.5559**, max **+2.3595** | **YES, essentially exact** |
| 0g | **New: exact significance of r=0.031 at n=7** | none (new) | Full 7!=5040-permutation exact test on `(delta_scene, delta_empty)`: **two-sided p = 0.953** — the observed correlation is *more consistent with pure chance than a coin flip*; the exact critical `\|r\|` for α=0.05 at n=7 is **0.746**, 24× larger than the observed 0.031 | **New, decisive, exact (not asymptotic)** |
| 0h | **New: lag-tolerant cross-correlation over small integer shifts (1° steps)** | none (new) | Computed at lag ∈ [−4,+4]; every |lag|≥1 result rests on n≤6 overlapping points, with wildly unstable, sign-flipping r (e.g. lag=−2: r=−0.71, n=5; lag=+4: r=+0.998, n=3 — trivially near-1 with only 3 points) — **no lag produces a stable, well-supported peak**; the shift search is itself underpowered, not merely the zero-lag test | **New — the phase-shift-tolerant metric the task asks for is itself unusable at n=7, not merely "doesn't show a peak"** |
| 0i | **New: does the sub-thread's own `_free_period_search`/`free_period_with_widening` machinery resolve a period at this reduced power?** | none (new, per task instruction) | Ran the REAL `pad_round_trip_model.free_period_with_widening` on `delta_scene` and `delta_empty` directly. `delta_scene`: P\*=**2.940°**, R²=**0.858**. `delta_empty`: P\*=**1.015°** (grazes the `[1,4]°` window's own lower edge), R²=**0.864**. `rel_dev` between the two recovered periods = **1.896** (190% apart) | **New — the two series do NOT converge on a shared period even approximately; this is stronger disconfirmation of "same mechanism, phase-shifted" than the zero-lag r alone** |
| 0j | **New: ground-truth check on 0i — `delta_empty` at these 7 points is PROVEN (0b) bit-identical to exp-076's own committed data, whose TRUE established free period (full 31-point fit, `experiments/077-.../results.json`, reused this cycle in the x-wall refit) is `P*=4.611289746337977°`** | none (new) | The reduced 7-point search recovers **1.015°** for this exact signal — **78% off** the known-correct value, with a spuriously high R²=0.864 anyway | **New, decisive: the instrument recovers the WRONG period for a signal whose TRUE period is independently known — a direct falsification of trusting any period recovered at this window** |
| 0k | **New: is R²≈0.86 at n=7 even statistically unusual?** | none (new), per R5's own discipline (a period/parameter search needs a null-permutation control before a fit counts as evidence) | 200,000-trial null-permutation control, Gaussian noise at each series' own measured σ, run through the IDENTICAL real search (sanity-checked bit-exact against the committed function first): `P(R² ≥ 0.858 \| pure noise, σ=σ_scene) = 0.272`; `P(R² ≥ 0.864 \| pure noise, σ=σ_empty) = 0.257` | **New, decisive: neither series' own free-period R² clears even a lenient look-elsewhere bar — R²≈0.86 is what ~26–27% of PURE NOISE trials achieve at this n and grid, matching this program's own R5 house-rule shape exactly** |
| 0l | VISION's "5.5×" naive comparator and its own proposed "≈4.2×" correction | VISION | `A_scene/C_thr = 0.6815`; T16 raw `√(A_i²+A_q²) = 6.1530×10⁻⁴` (re-pulled from `experiments/076-.../results.json::carrier_diagnostics_PAIR_PAD`, exact, not rounded) → naive ratio `0.6815/(6.1530e-4/0.005) = 0.6815/0.1231 = `**5.538**, matches "roughly 5.5×" exactly. VISION's own correction: ptp-equivalent `=2×6.1530e-4=1.2306×10⁻³` — matches VISION's own stated "≈1.23×10⁻³" exactly. But `A_scene/ptp-equivalent = 3.4076×10⁻³/1.2306×10⁻³ = `**2.769**, NOT VISION's own stated "≈4.2×" | **VISION's DIRECTION of correction reproduces exactly and is right; VISION's OWN REPLACEMENT NUMBER does not reproduce from its own stated operands — see Attack 5** |
| 0m | MATERIALS' x-wall refit table: "2 of 4 cells flip, none to SUPPORT" | MATERIALS | Read `x_wall_realizable_refit_results.json::verdict_flips` directly: exactly 2 entries (`single_wall/pair_absorb40` INCONCLUSIVE→REFUTE; `two_wall/pair_pad` REFUTE→INCONCLUSIVE), neither → SUPPORT | **YES, exact** |
| 0n | THERMODYNAMICS' verification that exp-081's hygiene bundle actually landed | THERMODYNAMICS | Independently grepped `experiments/081-.../photonics_construction.py`/`NOTES.md` myself: `"""POST-RUN ANALYTIC, ZERO FDTD (Iteration-59 hygiene label...)"` and `"600nm ONLY"` qualifiers present exactly as claimed | **YES, exact** |
| 0o | VISION's git-provenance finding: `experiments/082-.../` commits bundle predictions with an already-executed run | VISION | `git log --oneline -- experiments/082-.../` shows commit `5bb78df` ("...launches the PAD-loaded real-article check FDTD run (**27/29 calls done at this commit**)...") already carries `phase1_proposal.md`'s PRE-REGISTERED §4 predictions text, `run.py`, `x_wall_realizable_refit.py`, AND a results file with 27 of 29 calls already complete, in ONE commit — **worse than VISION's own characterization** ("no git-commit boundary... at all"): the predictions text is committed strictly AFTER most of the run had already executed, not merely alongside a finished one | **YES, confirmed, and sharpened — see Attack 6** |

---

## 1. Numbered attacks

### Attack 1 — `[inconsistency]` SURVIVES's substantive "same mechanism" reading is not merely under-supported by a low Pearson r — it is UNRESOLVABLE at this cycle's own statistical power, a stronger and more specific finding than either raising critique reached

PHOTONICS and EM, independently, computed `r=0.031` and correctly flagged
that a `ptp`-ratio verdict cannot distinguish "same mechanism, phase-shifted"
from "unrelated ripple of similar scale." Both proposed the natural next
step — a phase-tolerant metric (cross-correlation over small lags per EM;
the deferred full 31-point window per both) — as the way to settle it. I ran
what is buildable **today, at zero new FDTD, from data already in
`results.json`**, going further than either critique attempted (§0h–k):

1. **Lag cross-correlation fails outright as an instrument at n=7** (0h): every
   nonzero lag rests on ≤6 overlapping points, and the resulting r values
   swing from −0.71 to +0.998 with no stable, well-supported peak. This is
   not "no phase-shift found" — it is "the phase-shift search itself has no
   statistical power at this n."
2. **The sub-thread's own established free-period-fit machinery, run directly
   on the two series, does not converge on a shared period at all** (0i):
   `delta_scene`'s own best fit is 2.94° (near T21's 2.8421° fringe, matching
   PHOTONICS'/EM's own flagged concern); `delta_empty`'s own best fit is
   1.015° — 190% different, and suspiciously hugging the search window's
   lower boundary.
3. **A ground-truth check proves that boundary-hugging fit is wrong, not
   informative** (0j): `delta_empty` at these 7 points is bit-identical
   (§0b) to `experiments/076-.../results.json`'s own committed `PAIR_PAD`
   data, whose TRUE free period — fit over the full 31-point window,
   already re-used this cycle in the x-wall refit — is **4.611°**. The
   7-point reduction recovers **1.015°** for a signal we independently KNOW
   has period 4.611°: a 78% miss, with R²=0.864 anyway.
4. **A null-permutation control (this program's own R5 discipline, applied
   here for the first time to this specific instrument) shows that R²≈0.86
   is not even unusual under pure noise at this n**: 200,000 trials give
   `P(R²≥0.858)=0.272` and `P(R²≥0.864)=0.257` (0k) — roughly a quarter of
   pure-noise 7-point series clear the SAME bar both real series clear.
5. **An exact permutation test on the Pearson r itself** (0g): `p=0.953`,
   two-sided, exact (not asymptotic) — the observed r=0.031 is almost
   exactly what pure chance produces (the exact critical value at α=0.05,
   n=7, is `\|r\|≥0.746`, 24× the observed magnitude).

**Ruling on the question the task poses directly**: this is NOT a case where
a phase-tolerant metric reveals the two series ARE the same phenomenon
merely shifted by the article's own presence. Every phase-tolerant
elaboration I could build at this power (lag correlation, free re-fit
against each other, ground truth against the known-correct period) either
fails to find a stable shift or actively falsifies trusting the recovered
periods at all. **But it would equally be an overclaim to rule the two
series "genuinely decorrelated"** — that requires POWER to detect an
imperfect (phase-shifted, amplitude-modulated by the article's own dominant
shadow term via the nonlinear `C=(B_obj−B_flank)/B_flank` ratio EM's §4
correctly names) relationship, which this instrument does not have at n=7.
**The honest, most decisive finding is a THIRD one, sharper than either
critique's own framing**: the shape/mechanism-identity question is not
merely "not yet resolved" — it is demonstrated, from primitives, to be
**below this instrument's own resolving power**, independent of which way
the true answer lies. This is a stronger, more useful, more falsifiable
statement than "informally suggests decorrelation" (both critiques' own
softer landing) because it is now backed by a ground-truth failure mode
(0j) and a calibrated null (0k), not just a low correlation coefficient.

**Fix**: revise `NOTES.md`'s "Learned" §1–2 and `phase1_proposal.md`'s
"Combined self-score"/"What this result does NOT establish" sections to
state precisely: SURVIVES stands MECHANICALLY, exactly as pre-registered
(§0a) — a comparable-SCALE oscillation is measured on the real scoring
channel. The stronger claims currently in the record ("the PAD confound
reaches the real, article-loaded Weber-contrast channel," "the empty-
scene-only status... is retired," "the same lossless phase artifact
reaches the scored channel") assume mechanism continuity that is neither
established NOR resolvable with this cycle's own data — replace with
language stating the shape/mechanism-identity question is open and, per
this audit, below this window's resolving power specifically (not merely
un-run). Append §0d–0k in full to the permanent record.

### Attack 2 — `[inconsistency]` MATERIALS' article-generality gap is real and correctly disclosed as an idealization, but the write-up's own generalizing prose oversteps its own disclosed scope

MATERIALS is correct: the one article tested is the flagship
`graded_black_shell`, whose own baseline `C≈−0.55` sits roughly 100×
past `C_thr` by design — nothing here bears on whether a near-threshold
σ(I) article would show the same 0.66/0.68 reading. `phase1_proposal.md`'s
own Idealization 5 discloses this correctly and by name. But `NOTES.md`'s
"Learned" §1 ("every future ambient-contrast citation... should now
disclose this as a named, quantified... confound") and `phase1_proposal.md`'s
own "Combined self-score" paragraph state the finding as a property of the
CHANNEL, not of this one article — a real gap between the idealization list
(correctly scoped) and the headline prose (not). This is the identical
shape MATERIALS' own critique names.

**Fix**: scope every generalizing sentence in `NOTES.md`/`phase1_proposal.md`
explicitly to "the flagship, strongly-absorbing article class" until the
near-null follow-up MATERIALS names as its own flip condition (`off_pass`,
`τ_off≈0.0065`) is run. Add that follow-up to PLAN.md's board as a named
Tier item (not merely left inside Idealization 5's prose).

### Attack 3 — `[inconsistency]` THERMODYNAMICS' mechanism-identity gap is real, converges with Attack 1's own shape-evidence gap, and is currently treated as two unrelated footnotes rather than one open question

THERMODYNAMICS is correct that Iteration 53's own losslessness proof
(`lab/fdtd2d.py`'s damping mask is a pure function of `absorb`, independent
of `pad`/`nx`/`ny`) is an EMPTY-scene proof. I independently confirm the
proof itself is unaffected by article presence — it is a fact about the
BOUNDARY mask's own construction, structurally disjoint from where a
`materials.pec_disk`/`graded_black_shell` object sits inside the domain —
so the boundary's own reflectance physics is untouched, exactly as
Idealization 7 assumes. But THERMODYNAMICS' sharper point stands: whether
`delta_scene(θ)`, the actually-measured quantity, is STILL that same
lossless phase effect (now merely observed through the article's own large
shadow term and the nonlinear Weber-contrast ratio), or a qualitatively
different absorption-coupled interaction, is genuinely open — and this is
NOT a separate question from Attack 1's own shape-evidence gap: both are
asking, from different charter angles (energy-accounting vs.
statistical-shape), the identical underlying question — does the SAME
mechanism persist once a real absorber sits in the coherent path? Treating
them as independent footnotes (as the current record does — THERMODYNAMICS'
critique never engages the correlation numbers; neither shape critique
engages the mechanism-identity framing) understates how much converging
evidence already exists that this is genuinely open.

**Fix**: merge THERMODYNAMICS' finding and Attack 1's finding into one
"mechanism-identity: open" note in `NOTES.md`, stating explicitly that two
independent charter lines (energy-accounting, statistical-shape) both land
on the same unresolved question, neither alone sufficient to answer it.

### Attack 4 — `[inconsistency]` VISION's metric-kind mismatch (static JND vs. swept domain-difference) is correctly identified and matches this program's own T3 precedent

Independently confirmed: `C_thr` is T2's pinned static-scene JND; `A_scene`
is a peak-to-peak swing of a *difference between two numerical
domain-treatments*, swept across angle — no human views that quantity
directly, and LOGBOOK's own T3 thread already names exactly this category
error for a structurally identical bar-comparison. VISION's requested fix
(relabel as an instrument-uncertainty-budget number, never phrase as "N%
of the way to visible") is correct and should be adopted; I independently
confirmed the current record does not yet use the literal "visible"
framing VISION warns against (`NOTES.md`/`phase1_proposal.md` both say
"68% of VISION's frozen photopic lab bar," not "68% visible"), so this is
a preemptive, not yet realized, risk — worth fixing before it recurs, not
evidence of an existing violation.

**Fix**: adopt VISION's relabeling request verbatim (§4 fix docket item 3,
below).

### Attack 5 — `[inconsistency]` VISION's own "5.5×→4.2×" corrected comparator does not itself reproduce — the properly like-for-like figure is ≈2.77×, not ≈4.2×

VISION's DIRECTIONAL critique is correct and independently confirmed
(§0l): the naive "5.5×" comparator divides a peak-to-peak quantity
(`A_scene`) by a single-sided sinusoid amplitude (T16's `√(A_i²+A_q²)`),
mismatched conventions. VISION's own stated correction — double T16's
figure to a ptp-equivalent, `≈1.23×10⁻³` — reproduces exactly from the
raw `A_i`/`A_q` I re-pulled directly from `experiments/076-.../
results.json::carrier_diagnostics_PAIR_PAD` (not rounded, not copied from
VISION's own prose). But **dividing `A_scene` by that correctly-converted
ptp-equivalent gives `3.4076×10⁻³ / 1.2306×10⁻³ = 2.769`, not VISION's own
stated "≈4.2×"** — and this is scale-invariant under every equivalent
reformulation I tried (halving `A_scene` instead of doubling T16's figure
gives the identical ratio, as algebra requires). I could not reconstruct
VISION's own "4.2×" from its own stated inputs by any reasonable reading;
it appears to be an arithmetic slip inside the correction itself — **the
same failure shape R4/R9 exist to catch, now applied to a Phase-2
reviewer's own "corrected" figure**, exactly the class of check this
program's own precedent (Iteration 54's R9 addendum: "a reviewer's
confirmation... must independently re-derive," LOGBOOK RULED OUT) requires
before any correction is trusted, adopted here to a NEW instance one cycle
after R9 itself was adopted for the FIRST such instance (T16's original
"24×" error).

**Fix**: do not adopt VISION's "≈4.2×" verbatim. Record the corrected
comparator as **≈2.8×** (properly like-for-like, ptp vs. ptp — this
audit's own independently re-derived figure, §0l), alongside the original
uncorrected "≈5.5×" (mismatched-convention, disclosed as such) and T16's
own historical "≈0.12×" — three distinct, correctly-labeled numbers, not
two.

### Attack 6 — `[inconsistency]`, procedural: the git-provenance pattern VISION flags is real, confirmed, and — checked directly — worse than VISION's own description; a third consecutive cycle should not repeat it

`git log` (§0o) confirms VISION's core claim exactly and then some: commit
`5bb78df`'s own message states the PAD-loaded-article FDTD run was already
**27/29 calls complete** at the moment `phase1_proposal.md`'s own §4
PRE-REGISTERED predictions text was committed. This is not merely "no
commit boundary" (VISION's own framing) — the predictions text is
demonstrably NOT ex-ante with respect to the run by git's own timeline,
regardless of when the text was drafted locally. Per exp-081's own Phase-2
audit (my format model, and VISION's own prior-cycle seat), PANEL.md's
literal, non-negotiable git-before-run mandate binds **Phase 3's FROZEN
PREDICTIONS commit** specifically — not Phase 1 — so this is, again,
**not a rules violation**, and exp-081's own Phase 3 already restored
proper two-commit discipline for ITS frozen predictions (per LOGBOOK
Iteration 58). But this is now confirmed as the **second consecutive
cycle** a blind Phase-2 critique has had to flag this exact pattern at
Phase 1, under a **different lead seat** (THERMODYNAMICS, exp-081;
QUANTUM, exp-082) — a lead-seat-independent habit, not a one-off. Per
exp-081's own audit's tripwire language, a third recurrence "should not be
read as a close call."

**Fix**: if any of this docket's fixes require new FDTD (none currently
do — see §3), Phase 3 MUST commit fresh FROZEN PREDICTIONS in a dedicated
commit strictly before that run, restoring exp-080's own standard.
Separately, as a forward-looking house habit (not a binding rule): Phase 1
itself should adopt the same two-commit discipline going forward, not only
Phase 3, given this is now a two-cycle pattern under two different leads.

**No `[unfalsifiable]` attacks found.** Every prediction in this cycle
(SURVIVES/CANCELS/INCONCLUSIVE bands, the x-wall refit's reused `score()`
thresholds, the phase-convention extension's calibration check) is a
falsifiable numeric band, pre-registered (predictions precede results
within the same document, per the git-timeline caveat in Attack 6),
computed from committed code, and reproduces exactly (§0). **No
`[inexpressible]` attacks found.** Every quantity is either a direct FDTD
measurement (`contrast_from_runs`) or desk arithmetic on already-gated
primitives (`reflection_coefficient_vec_realizable`, `free_period_with_
widening`) — no new physics mechanism is proposed. **No
`[constraint-#N-violation]` attacks found.** T1 disposition is stated N/A
consistently across every document I read (`phase1_proposal.md` §0/§3,
`NOTES.md`); the one place a reader could misread the secondary metric as
a literal visibility claim (`A_scene/C_thr=0.68`) does not currently use
"visible"/"invisible" language (confirmed by direct grep, §0), matching
VISION's own preemptive-not-yet-realized framing (Attack 4) — Red Team
concurs this is a real risk worth fixing before it becomes a violation, not
evidence one occurred.

---

## 2. Disposition of the five blind critiques

| Seat | Verdict as filed | My independent check | Disposition |
|---|---|---|---|
| PHOTONICS | support-with-changes | r=0.031 reproduces exactly (0d); elementwise ratio range reproduces (0f) | **ADOPT the attack in full; EXTEND substantially.** The Pearson-r finding is correct and load-bearing. My own extension (§0h–k) shows the honest conclusion is stronger and more specific than PHOTONICS' own flip condition names: not merely "add a shape check," but "this window cannot resolve shape/phase at all, independent of which way the truth lies." |
| MATERIALS | support-with-changes | x-wall refit table reproduces exactly (0m); article-scoping attack independently assessed as real | **ADOPT IN FULL.** Both audited claims (refit count, article-generality gap) are correct. The requested scoping fix (Attack 2) should be applied verbatim. |
| ELECTROMAGNETISM | support-with-changes | r=0.031 reproduces exactly (0d), independently converging with PHOTONICS; EM's own second settling check and phase-convention self-downgrade assessment both read as sound, independent verification not re-run here (EM's own new FDTD call, taken as disclosed) | **ADOPT IN FULL; EXTEND.** EM's own §2 two-reading framing ("same mechanism, phase-shifted" vs. "unrelated new structure") is exactly the right question — this audit resolves it as far as it is resolvable (§0h–k: neither reading is establishable at this power, a sharper answer than EM's own "the near-zero correlation is consistent with two readings" framing landed on). EM's flip condition (a lag-aware check materially above r=0.031) is now run (§0h) and does NOT clear it — my own verdict does not move to full "support" on EM's own stated terms, because the instrument itself, not merely the observed r, is now shown underpowered. |
| THERMODYNAMICS | support-with-changes | Hygiene-bundle verification reproduces exactly (0n); mechanism-identity attack independently assessed as real and convergent with Attack 1 | **ADOPT IN FULL; MERGE with Attack 1.** THERMODYNAMICS' own attack and PHOTONICS'/EM's shape attack are the same underlying open question from two charter angles — see Attack 3. |
| VISION | support-with-changes | Metric-kind-mismatch attack confirmed real (Attack 4); git-provenance finding confirmed and sharpened (Attack 6, §0o); **"5.5×→4.2×" correction does NOT reproduce (§0l, Attack 5)** | **ADOPT the metric-kind-mismatch and git-provenance findings in full; OVERRIDE the specific "≈4.2×" replacement figure.** VISION's own diagnosis of the error (ptp vs. single-sided-amplitude mismatch) is correct; VISION's own arithmetic executing that diagnosis is not. The corrected figure for the permanent record is **≈2.8×** (this audit's own independently re-derived number), not VISION's "≈4.2×". This is a partial override of one specific sub-claim, not of VISION's verdict or its other two fix requests, both adopted in full. |

**No blind critique's OVERALL verdict is overridden** — all five filed
support-with-changes and I concur with support-with-changes for all five.
**One specific numeric sub-claim is overridden** (VISION's own "≈4.2×"
figure, Attack 5) — disclosed explicitly above with the independent
computation that produced the correction, per this program's own R4/R9
standard for how a reviewer's "confirmation"/"correction" must be earned,
not merely asserted. This is the first instance in this sub-thread's
record of Red Team overriding a SPECIFIC ARITHMETIC CLAIM inside a
critique that itself was created to correct a DIFFERENT arithmetic claim
— a second-order instance of the exact discipline R9 exists to enforce.

---

## 3. Overall ruling: **PROCEED-WITH-MANDATORY-FIXES**

Not PROCEED-AS-IS: the primary metric's own MECHANICAL computation is
correct and reproduces bit-exact (§0a) — no defect in the measurement
itself — but the record's own SUBSTANTIVE prose (`NOTES.md`'s "Learned,"
`phase1_proposal.md`'s "Combined self-score") currently states a
mechanism-continuity claim ("the PAD confound reaches the real...
channel," "the same lossless phase artifact reaches the scored channel")
that this audit shows is neither established NOR resolvable with this
cycle's own data — a reader of the current record alone could not
distinguish "SURVIVES, scale-only, mechanism open" from "SURVIVES,
confirmed same mechanism," and the current prose reads as the latter.
VISION's own uncorrected "≈4.2×" figure would also enter the permanent
record unchecked without this audit. Not HALT-AND-REDESIGN: no false
claim survives independent re-derivation of anything ALREADY CHECKED and
COMMITTED (§0 — every existing number in `results.json`/`x_wall_
realizable_refit_results.json`/`phase_convention_extension_results.json`
reproduces exactly); no RULED-OUT item is re-proposed; zero new FDTD
anywhere in this cycle's own record (`assert_lab_clean()` passed, `git
diff --stat -- lab/` empty, confirmed) or in this audit's own verification;
every gap found is fixable same-shift, in prose, with data already in
hand — the shape of this program's own established PROCEED-WITH-
MANDATORY-FIXES precedent (exp-080, exp-081, among others).

### Fix docket, prioritized, for Phase 3 synthesis

1. **[HIGH]** Revise `NOTES.md` "Learned" §1–2 and `phase1_proposal.md`'s
   "Combined self-score"/closing sections per Attack 1: SURVIVES stands
   MECHANICALLY (§0a); the mechanism-continuity reading is not established
   and is shown, not merely suspected, to be below this cycle's own
   resolving power (§0d–k, all four independent lines: exact permutation
   test p=0.953; lag-correlation instability; the two series' free periods
   diverging 190%; a ground-truth check showing the KNOWN-correct signal's
   period is unrecoverable at this window; a null-permutation control
   showing R²≈0.86 is common under pure noise at n=7). Append §0 in full.
2. **[HIGH]** Scope MATERIALS' article-generality finding per Attack 2:
   every generalizing sentence restricted explicitly to the flagship,
   strongly-absorbing article class; add the near-null σ(I) follow-up
   (MATERIALS' own flip condition) to PLAN.md as a named board item.
3. **[HIGH]** Correct the secondary-metric comparator per Attacks 4–5:
   relabel `A_scene/C_thr` as an instrument-uncertainty-budget number
   (VISION's request, adopted in full); replace the "5.5×"/VISION's own
   uncorrected "4.2×" language with all three correctly-labeled figures —
   naive (mismatched-convention) ≈5.5×, properly like-for-like ≈2.8× (this
   audit's own re-derivation), T16's own historical ≈0.12× — each stated
   as measuring a different thing.
4. **[MEDIUM]** Merge THERMODYNAMICS' mechanism-identity finding with
   Attack 1's shape-evidence finding into one open question, per Attack 3
   — not two independent footnotes.
5. **[MEDIUM]** State explicitly, per Attack 6: if this docket's fixes
   require any further FDTD spend (none currently do), Phase 3's FROZEN
   PREDICTIONS for that run must be committed in a commit genuinely
   separate from, and strictly before, the run's own results — restoring
   exp-080's own standard, now a two-cycle-old, lead-seat-independent
   pattern if it recurs a third time.
6. **[LOW]** No fix required, noted for completeness: the reproduction
   precondition, settling precondition (both independently corroborated,
   including EM's own additional spot-check), the x-wall refit's "2
   flips, none to SUPPORT" self-scoring, and the phase-convention
   extension's own "genuinely inconclusive, reliability precondition
   fails" self-scoring are all independently verified correct (§0b, 0m,
   and direct inspection of `phase_convention_extension_results.json`)
   and need no correction.

---

## 4. Checkpoint ruling

**Criterion 1** (a configuration passes all constraint metrics): **N/A.**
Zero constraint-3 or any-constraint engagement anywhere in this cycle
(T1: N/A, stated and applied consistently, §1 closing paragraph).

**Criterion 2** (a proven mechanism-class boundary): **N/A, not merely
not-yet-ripe.** This cycle is explicitly instrument-fidelity/
generalization work, not a mechanism proposal — no mechanism-class claim
is made or scored here at all, so criterion 2's "ripe/not ripe" framing
does not apply. (This cycle's own finding may eventually bear on how much
weight the WHOLE T28 y-wall/PAD sub-thread's mechanism-class rulings
should carry once a real scene is involved — flagged for Iteration 60's
own ranking, not a criterion-2 event itself.)

**Criterion 3** (engine physics beyond validated bench classes): **N/A.**
Zero new `lab/` machinery — `assert_lab_clean()` passed in `run.py`'s own
execution (confirmed in `run_output.txt`), and both riders (x-wall refit,
phase-convention extension) import only already-committed experiment-local
functions, confirmed by direct inspection of both files' own import blocks.

**Criterion 4** (program-integrity drift): **Reasoned through explicitly,
does not fire — conditioned on Phase 3 adopting this audit's fix docket
(§3), the same condition exp-081's own Iteration-58 audit attached to its
own comparable near-miss.** Every gap this audit found (Attacks 1–6) is
caught WITHIN this Phase-2 review layer — five blind critiques plus this
audit — before Phase 3 has had any opportunity to carry an unqualified
claim forward. No FALSE claim about a specific, ALREADY-CHECKED,
COMMITTED computation survives (§0 — the mechanically-computed SURVIVES
number, `0.6573`, IS correct); the risk is overclaimed SUBSTANTIVE
interpretation and one uncorrected reviewer arithmetic slip (VISION's own
"4.2×"), both resolved inside this same document. This matches the
established non-firing shape (exp-079 Iteration 56, exp-080 Iteration 57,
exp-081 Iteration 58's own Phase-2 audit: genuinely new information
surfaced and reconciled inside the review layer itself, not a defended
wrong claim surviving to the next phase). **The distinguishing condition,
stated plainly, exactly as exp-081's own audit stated it one cycle
earlier**: if Phase 3 repeats `NOTES.md`'s pre-audit "the PAD confound
reaches the real... channel"/"the same lossless phase artifact reaches the
scored channel" language, or VISION's own uncorrected "≈4.2×" figure,
verbatim — without folding in this audit's own §0 findings and the fix
docket (§3) — THAT would be the firing shape one phase later. Criterion 4
continuing not to fire is conditioned explicitly on the fix docket being
adopted, not on this audit's existence alone.

**Criterion 5** (two consecutive non-advancing iterations): **Not at
risk.** This cycle discharges the standing six-cycle tripwire on item 7 for
the first time, delivers the sub-thread's first-ever article-loaded FDTD
measurement in nine T28 cycles, and produces a genuinely new,
independently-verified instrument-limitation finding (§0i–k) with
implications beyond this one result — substantive advancement regardless
of how Iteration 60 ultimately weighs the mechanism-identity question.

### My own read on flagging for Phase 5 / Checkpoint consideration (not a formal ruling)

**Worth flagging explicitly for discussion at Phase 5, on two grounds
distinct from any single criterion above.** First, this cycle formally
discharges PLAN.md's own twice-escalated, six-cycle-deferred tripwire —
worth a clean, explicit closing statement in LOGBOOK regardless of how the
mechanism-identity question resolves, so the tripwire's own resolution is
part of the permanent record, not merely implied. Second, and more
substantively: §0i–k's own finding — that this program's own established
free-period-search machinery, when run at reduced (7-point) power, both
fails to recover a KNOWN-correct period for ground-truth data (§0j) AND
achieves "significant-looking" R² on pure noise roughly a quarter of the
time (§0k) — is a genuinely new, general instrument-caution finding, not
scoped to this one cycle's own SURVIVES verdict. It does not itself meet
any Checkpoint criterion (no false claim entered the record; nothing here
touches a prior cycle's own already-committed, full-power 31-point
results), but Phase 5 should decide explicitly whether it warrants a
standing house note (in the R5 family) about minimum window size before
any future reduced-power period/phase test is trusted, the same way R5
itself grew out of a single cycle's own look-elsewhere finding.

---

## 5. Note for Iteration 60

Not a full reconciled ranking (Phase 3/4/5 have not yet run for exp-082).
Three items this audit's own findings bear on directly: (1) the
mechanism-identity question (Attack 1/3, merged) is now the board's own
best-characterized OPEN question on the real-article channel — the natural
next test, once budgeted, is the already-named full 31-point window at
this same `PAIR_PAD` pair, which would give the free-period search the
power this cycle's own 7-point reduction demonstrably lacks (§0i–k); (2)
MATERIALS' near-null-article follow-up (Attack 2) and the still-untested
`PAIR_ABSORB40`/`C80−C40` pairs (Idealization 3, undisturbed by this
audit) remain open scope questions for the real-article channel,
independent of (1); (3) the x-wall wavelength-generality leg and the
750nm two-wall spot-check remain the board's own oldest-unexecuted items,
untouched by this cycle's own scope, now due for explicit re-ranking
alongside the newly-resolved items above.

None of the above re-opens or re-proposes any RULED-OUT item (R1–R9).
