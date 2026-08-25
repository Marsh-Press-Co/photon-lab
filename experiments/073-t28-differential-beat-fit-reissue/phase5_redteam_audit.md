# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 50 · exp-073
## MATERIALS' corrected re-issue of exp-072's differential/beat fit — final ruling, same-shift docket, checkpoint determination

*Fresh sub-agent, RED TEAM charter (PANEL.md seat 7: attacks every proposal,
speaks last and hardest; kills internal inconsistency, unfalsifiable claims,
mechanisms inexpressible as simulation parameters, and quiet constraint
violations; never leads, has no proposal to protect — its standard is NOT
textbook-physics compliance). Input packet: the full cycle record (Phase 1
proposal, five Phase-2 blind critiques, Phase-2 Red Team audit, Phase-3
synthesis, `NOTES.md`, `run.py`, `phase4_results.md`, `results.json`), all
six blind Phase-5 reviews, `experiments/072-.../phase5_redteam_audit.md` for
Checkpoint precedent, and LOGBOOK.md in full. Nothing below is adjudicated
from prose alone: every load-bearing numeric claim in this document was
independently re-executed against the committed code and data — direct
Python against `results.json`, a from-scratch re-derivation of the
`dR_q/dψ̄` identity (symbolic and numeric), and a live re-run of `run.py`
after the two code fixes this audit applies, diffed field-by-field against
the pre-fix committed artifact.*

---

## 0. Independent re-verification performed

| # | Check | Method | Result |
|---|---|---|---|
| A | Combined Verdict | Read `results.json` directly | `HALT_NULL_MISCALIBRATED`, `per_pair={}`, confirmed |
| B | G0-a/b/c | Recomputed from raw `experiments/069/071/072` JSON, independent script | all exact-zero residuals, PASS |
| C | G0-e(ii) residual-structure-leg pass count | `python3` filter over `results["scored"]["g0e_ii"]["residual_structure_leg"]["table"]` | **71/72 fail, 1 pass** (`σ=0.0005, ψ₀=270°, α=0.10`, rate 0.132, inside `[0.0598,0.1402]`) — NOT 72/72 as published |
| D | i.i.d.-vs-residual-structure paired-cell correlation | Matched 72 cells by `(σ,ψ₀,α)`, Pearson r | **r = 0.90669**, mean|diff| = 0.0171, both legs' means within 0.0003 of each other at every α |
| E | `build_residual_pool()`/`null_calibration_check()` construction | Read `run.py` lines 679–699, 904–986 directly | `rng.choice(residual_pool, size=n, replace=True)` — i.i.d. bootstrap over a pooled, θ-order-discarded 124-value array; **no correlation structure can survive this construction** |
| F | `ψ̄`'s definition | Read `phase1_proposal.md` §2b.1–2b.2 directly | `θ_c = 2πu/T_mean + ψ̄` — `ψ̄` **is**, by direct textual substitution, `design_matrix`'s own `psi` argument; no second symbol exists |
| G | Raw `dR_q/d(design_matrix psi)` on exp-072's real data | Independent script: load exp-072's real `(T_x,ψ,R_i,R_q)`, reconstruct `delta_ab` from raw `C40/C60/C70/C80`, rebuild `X5` at `(T_x,ψ±ε)`, central-difference | **ratio to `R_i` = −1.000000 exactly at all four pairs**; own reconstructed `R_i,R_q` matched exp-072's published values exactly (pipeline-fidelity check) |
| H | `run.py`'s post-fix behavior | Applied the two-line sign fix, re-ran `run.py` end-to-end, diffed the full JSON tree against the pre-fix committed artifact | **zero diff except `elapsed_s`** — Combined Verdict, every gate, every G0-e(i) leg figure, all identical |
| I | `carrier_q95()`'s construction | Read `run.py` lines 327–363 | calls `sign_flip_surrogates()` directly — the identical construction Attack 4/`G0-e(ii)` independently showed anti-conservative on this design |
| J | R5/named-constant-search applicability | Grepped the full document set for R5/R5-addendum dead ends | clean, confirms Red Team's Phase-2 Attack 8 and QUANTUM's Phase-5 Finding 5 |
| K | `lab/` diff | `git diff --stat -- lab/` | empty — zero engine physics touched, confirmed independently |

No claim from any of the six Phase-5 reviews was found fabricated or
unreproducible. Two real defects were found and independently confirmed —
both already caught by at least one blind seat, both re-derived here from
scratch rather than accepted on a seat's authority, and both fixed same-shift
(§1, §5).

---

## 1. Ruling on the two same-shift fixes this audit applies

### 1.1 The "72/72"/"144/144 fail" claim is false. Confirmed independently; fixed.

`phase4_results.md`'s own bottom line and `NOTES.md`'s own Result section
both stated: *"both legs fail every single cell-α combination — 72/72
(i.i.d.) and 72/72 (residual-structure)"* / *"144/144 fail."* Pulled
`results["scored"]["g0e_ii"]["residual_structure_leg"]["table"]` directly
(check C, above): **71 of 72 cells fail; one passes.** Combined: **143/144,
not 144/144.**

This is exactly the class of defect this program's own R4 discipline exists
to catch — a specific, quotable "every single X" figure that does not
reproduce from the committed artifact — inside a cycle whose own THERMO
Phase-2 critique (this same cycle) caught a third recurrence of a related
defect class on a different number (`m₀`) and whose own docket closed it.
**Independently caught, blind, by two of six Phase-5 seats (PHOTONICS,
MATERIALS)**, both correctly ruled it non-load-bearing (the gate's own
`pool_pass = all(...)` is `False` regardless of 71 or 72), both correctly
declined to call it a Checkpoint-4 matter on its own. I confirm both
findings exactly and adopt their ruling: **real, quotable, non-gating.**

**Two of six seats (QUANTUM, VISION) independently re-ran the pipeline and
still repeated the false "144/144" figure** — QUANTUM's Finding 1 states
"both legs fail all 72 of their own cell-α combinations (144/144 total)";
VISION's §2 states "both legs... fail all 144 cell-α combinations." Neither
counted the individual `pass_` flags; both trusted the aggregate `pass_`
boolean and the mean-rate table, which are consistent with either 71/72 or
72/72. This is worth naming precisely, not as a mark against either seat
(their own headline findings, both independently re-verified below, are
unaffected), but because it is this cycle's own smallest instance of the
lesson exp-072's O-1 finding stated at full scale: **agreement between
independent parties is not verification when neither checked the specific
claim at the resolution it was made at.** A boolean flag and a mean-rate
table cannot certify a "every single cell" claim; only iterating the actual
144-row array can, and only two of eight independent parties this cycle
(six reviewers, the Phase-4 write-up, `NOTES.md`) did.

**Fixed this shift** (see §5 for the full list): `phase4_results.md` and
`NOTES.md` corrected to 71/72 (residual-structure) / 143/144 (combined),
with the passing cell identified and the non-load-bearing status explained
in place. `results.json` itself required no change — the raw table was
always correct; only the prose summarizing it was wrong.

### 1.2 `dR_q/dψ̄ ≡ +R_i` is the wrong sign. The correct identity is `−R_i`. Confirmed independently, three ways; fixed in `run.py`; re-run verified bit-identical except timing.

This is the highest-stakes finding in this audit, and the task's own framing
is exactly right: it is the same defect *shape* — a silent sign error in
carrier/phase bookkeeping — that fired exp-072's own Checkpoint-4, appearing
one cycle later inside the very re-issue built to close that defect class.

**What the write-up actually defines `ψ̄` to be.** `phase1_proposal.md`
§2b.1: step 1 fits "the common-mode amplitude `a_cbar` and phase `ψ̄`." §2b.2:
"With `θ_c = 2πu/T_mean + ψ̄` fixed from step 1, OLS of `delta_AB(θ)` on the
frozen 5-column basis..." `design_matrix(theta_deg, T_x, psi, xbar)` builds
`theta_c = w*u + psi` and is called with `psi = carrier["psi"]`, i.e. the
value `_amp_phase_at` returns as `psi = -math.atan2(fit["b"], fit["a"])`.
There is exactly one substitution path from the write-up's formula to the
code: `ψ̄ = psi` (`design_matrix`'s literal argument), by direct term-by-term
matching of `θ_c = 2πu/T_mean + ψ̄` against `theta_c = w*u + psi`. **No other
definition of `ψ̄` exists anywhere in this document set** — I grepped
`phase1_proposal.md`, `phase2_critique_em.md`, and `run.py` for every use of
"ψ̄"/"psi_bar" and found none that contradicts this.

**`phase3_synthesis.md`'s "Ambiguity 4" asserts the opposite**, without
deriving it: *"`design_matrix()`'s own `psi` argument is `_amp_phase_at`'s
`-atan2(b,a)`, i.e. the NEGATIVE of the symbol 'psi_bar' used in the
write-up's own formulas."* This treats the *raw* `atan2(b,a)` value as if it
were "the symbol ψ̄" — but nowhere does the write-up define ψ̄ as
`atan2(b,a)`; it defines ψ̄ as exactly the phase substituted into `θ_c`,
which is `psi = -atan2(b,a)`, not `atan2(b,a)` itself. This is not a
citation slip; it is a fabricated intermediate symbol that lets a correctly
computed number be discarded.

**Independent re-derivation, three ways, converging exactly:**

1. **Direct finite-difference on exp-072's own real data (check G, above).**
   Loaded exp-072's committed `(T_x, ψ, R_i, R_q)` for all four pairs,
   reconstructed `delta_ab` from the raw, independently-verified `C40/C60/
   C70/C80` series, rebuilt the frozen 5-column basis at `(T_x, ψ±ε)`, and
   central-differenced. My own reconstructed `R_i`/`R_q` matched exp-072's
   published values exactly at all four pairs — a pipeline-fidelity check
   that rules out a construction error on my part. **Raw
   `dR_q/d(design_matrix psi) / R_i = −1.000000` exactly, all four pairs.**
   This is the identical raw quantity `run.py`'s own G0-e(i) tripwire
   computes before its (erroneous) extra negation, and it matches the value
   `phase3_synthesis.md` itself reports having found ("ratio
   −1.0000000000 to 10 decimals... before this sign correction").
2. **A from-scratch closed-form derivation (ELECTROMAGNETISM's Phase-5
   review, independently re-checked here).** Since `cosθ_c` and `sinθ_c` are
   linear combinations of the ψ-independent vectors `cos(wu)`/`sin(wu)`, the
   column space of `X5(ψ)` is the same 5-D subspace for every ψ — changing ψ
   only re-parameterizes a basis of that fixed subspace. Demanding the fitted
   vector (which cannot depend on which basis represents the same subspace)
   be ψ-independent gives, for the `(R_i,R_q)` pair, `R_i(ψ) = B₃cosψ −
   B₄sinψ`, `R_q(ψ) = −B₃sinψ − B₄cosψ` for data-fixed constants `B₃,B₄` ⇒
   `dR_q/dψ = −B₃cosψ + B₄sinψ = −R_i(ψ)` exactly. A second, independent
   complex-exponential derivation (same review) reaches the identical result.
   I re-derived this algebra independently from the basis definition alone
   (§2b.2) before reading EM's own working and reached the same two 2×2
   systems; it is correct.
3. **The reason the *magnitude*-only check that has stood since exp-072
   never caught this.** Exp-072's own audit (item K/C19) reports "`dR_q/dψ̄
   ≡ R_i` to 5 decimals," traced (EM's review, independently confirmed by
   grepping exp-072's own record) to exp-072's THERMODYNAMICS Phase-5
   review's structural claim `R_q(ψ+δ) = R_q·cosδ + R_i·sinδ` — differentiate
   at `δ=0` and get `+R_i`. The correct relation (derivation 2, above) has
   the opposite sign on the `sinδ` term: `R_q(ψ+δ) = R_q·cosδ − R_i·sinδ`,
   giving `−R_i`. **`|dR_q/dψ|` equals `|R_i|` under either sign** — a ratio
   or magnitude check can never distinguish them. As far as this record
   shows, no seat in either cycle sign-tracked this identity by explicit
   algebra before ELECTROMAGNETISM's review this cycle: it was asserted
   once, passed a check that structurally could not have caught the sign,
   and was then *defended* — not re-derived — when exp-073's own development
   run first (correctly) computed the opposite sign and needed a reason to
   discard it.

**Consequence, precisely scoped.** Non-outcome-determining for exp-073's own
Combined Verdict: `G0-e(ii)` HALTed before `analyze_pair()` ever ran on real
data, so `per_pair` is empty and `dRq_dpsi`/`R_i_over_Rq` were never
populated with real numbers this cycle. But it is not harmless: it is stated
as fact — "Fixed," "independently re-verified" — in a frozen document
(`phase3_synthesis.md`), it is baked into "inherited, class-(c)" machinery
every future carrier/phase-fit cycle is instructed to reuse verbatim, and
`phase4_results.md`'s own identity-tripwire row reported it as a confirmed
exact algebraic fact with no caveat. **The G0-e(i) tripwire that was
supposed to catch exactly this class of error could not: it was constructed
to compare a deliberately re-negated finite difference against `+R_i`, so
its PASS was guaranteed by the construction, not evidence the underlying
claim was true** — precisely R4's and R6's own target defect shape, one
level removed from the estimator itself and inside the safety gate meant to
guard it.

**Fixed this shift, re-run and independently verified (check H, above).**
`run.py`'s `dRq_dpsi = R_i` → `dRq_dpsi = -R_i`; the G0-e(i) identity
tripwire's finite-difference formula corrected to drop the unjustified extra
negation and compare against `-R_i_est` instead of `+R_i_est`. Re-ran
`run.py` end-to-end and diffed the complete output JSON tree, key by key,
against the pre-fix committed file: **every field is bit-identical except
`elapsed_s`.** This is not a coincidence — algebraically, the old check
computed `|-raw_fd - R_i_est|` and the corrected check computes
`|raw_fd - (-R_i_est)| = |raw_fd + R_i_est|`, the identical expression; the
tripwire's own *numerical* pass/fail was always sign-agnostic (an
absolute-value comparison), so correcting the sign convention changes only
the *labeled* meaning and the never-populated `dRq_dpsi` field, not any gate
outcome. **Combined Verdict confirmed unchanged: `HALT_NULL_MISCALIBRATED`,
`G0-e(i)` PASS at the identical worst-cell error `9.4×10⁻¹¹`.** `phase3_
synthesis.md`'s Ambiguity 4 is corrected via an erratum block (original text
left standing, per house convention); `phase4_results.md`, `NOTES.md`
corrected in place (§5).

---

## 2. Adjudication of the six blind Phase-5 reviews

Every seat's own headline finding was independently re-executed, not
adjudicated from prose (§0). No finding from any of the six reviews is
overruled on its substance — a genuine outlier relative to several prior
cycles' Phase-5 audits, and a real credit to this cycle's own process. One
finding (§1.1) is corrected on a shared factual point two of six seats
independently got wrong; one omission (VISION's own T2-1 verification, §2.6)
is elevated to a binding forward constraint beyond what its own review
proposed.

### 2.1 PHOTONICS — CONFIRMED in full

The 71/72-vs-72/72 finding (§1.1) and the 1,728-cell arithmetic-slip
disclosure gap (F2) are both independently re-verified exact. The
leverage-mechanism re-derivation (a fourth, closed-form confirmation:
`cond(X5)=59.9167`, `mean diag(M5)=0.83871`, `E[Var(R_q^surr)]/Var(R_q^obs)`
= 0.79–0.80 across swept ψ₀) reproduces QUANTUM's and Red Team's own Phase-2
figures to three digits, independently re-checked here (§0, check A/B
family) and found sound. The forward-looking note that `mean diag(M5) =
(n−p)/n` is window-width-independent (an exact algebraic identity of OLS
trace) is correct and load-bearing for §7's own queue ranking below — a
wider window does not, by itself, guarantee `G0-e(ii)` clears; it must be
re-tested. Adopted in full. F2 fixed same-shift (§5).

### 2.2 MATERIALS — CONFIRMED in full

Independently re-derived the same 71/72 finding via a different route (a
standalone script importing `run.py`'s own functions rather than reading the
committed table directly) and reached the identical cell. Correctly ruled it
non-Checkpoint-4-on-its-own and explicitly deferred that specific call to
Red Team — the correct scoping of a blind seat's own charter boundary, and I
rule on it in §4 below. The realizability-caveat trace (§3, MATERIALS' own
charter duty as lead seat) and the T2-6 scope-discipline check (§4) are both
independently spot-checked here (grepped the full document set for
"T2-6"/"PAD-decorrelat[ion]"/materials-adjacent vocabulary) and confirmed
clean. The SE(ΔP)-bootstrap speculative concern (§5 of that review) is a
genuine, disclosed, checked-and-not-confirmed finding — exactly the right
epistemic posture, and I have nothing to add or subtract from it. Adopted in
full.

### 2.3 ELECTROMAGNETISM — CONFIRMED in full; this cycle's single most consequential finding

Finding 1 (the leverage-mechanism re-verification via an independent
Monte-Carlo cross-check that the closed form *predicts* the observed
inflation, not merely restates it) is a genuine fourth confirmation,
independently re-checked here. Finding 2 (§1.2 above) is the load-bearing
result of this entire audit — re-derived independently, from the document's
own text and from raw data, before I read EM's own working in full, and
found to match EM's derivation exactly on both the algebra and the
finite-difference number. EM's own explicit refusal to call the Checkpoint-4
question themselves ("I leave the formal Checkpoint-criterion-4 call to the
Director/Red Team's own synthesis... their charter, not a single blind
seat's") is the correct scoping of a blind seat's role; I rule on it in §4.
Adopted in full, with the fix (§1.2, §5) executed exactly as EM's own §2f
and ranked-#1 recommendation specify.

### 2.4 THERMODYNAMICS — CONFIRMED in full; second-most consequential finding

The `m₀`/Attack-3 re-anchor and Idealization-13 citation verifications
(items 6, 12) are independently re-checked here against the raw
`experiments/072/071` JSON and both correct. §3's own finding — the
"residual-structure" leg is a mislabeled i.i.d. bootstrap over pooled,
order-discarded values, not a test of θ-correlated structure — is
independently re-derived here directly from `run.py`'s own source (§0 check
E) and the committed data (§0 check D, reproducing THERMO's own r=0.907 to
five digits). This is a real, previously-uncaught gap in what docket item 4
actually delivers, correctly scoped by THERMO as non-outcome-determining
(the i.i.d. leg alone already fails all 72 of its own cells) but genuinely
unclosed. Adopted in full; disclosed same-shift (§5), a proper fix queued
for Iteration 51 (§7).

### 2.5 QUANTUM OPTICS — CONFIRMED on substance; Finding 1's pass-count is corrected

Finding 1 (a fourth independent from-scratch Monte-Carlo reproduction of the
2–6× anti-conservative inflation, plus a live re-execution of the official
`run.py` reproducing the committed artifact bit-for-bit) is independently
re-checked and sound — **except** its own stated "144/144 total" repeats the
uncorrected claim (§1.1); corrected here, non-load-bearing to the finding
itself. Finding 2 (the cycle respected the Phase-2 hedge, did not sneak in a
same-cycle patch) is verified against `phase3_synthesis.md`'s own text and
correct. Finding 3 (the criterion-5 flag) is adopted as the explicit prompt
for §4's own ruling below — QUANTUM's own instinct to flag rather than
assume is exactly right, and I rule on it explicitly rather than let
precedent apply by inertia. Finding 4 (T2-1/T2-4 never exercised against a
real, gate-passing pair) is independently confirmed by grep and is folded
into §7's forward queue. Finding 5 (R5 clean) independently reconfirmed.
Finding 6 (the "three independent implementations" framing conflates
derivation-kind and production-code-kind checks) is a fair, precise
correction and I adopt its wording for §0/§1 above.

### 2.6 VISION SCIENCE — CONFIRMED in full; Finding 3 elevated to a binding forward constraint

T2-1's own real-data behavior (Finding 1: `T_wrong` excluded at all four
pairs, `T_delta` admitted at three of four, the non-emptiness floor firing
correctly at C40–C60) is independently re-checked directly against `run.py`
by this audit as well (matching VISION's own direct call to `analyze_pair()`
bypassing the HALT) and confirmed bit-exact. Finding 2 (the shared-`q95`
proxy Red Team's own Phase-2 Attack 5b used was a *pattern* match, not a
reliable *magnitude* estimate — the real values run 0.076–0.294 against a
proxy of 0.272–0.472, up to 6.2× off at one pair) is independently
re-verified against `results.json`'s carrier-fit output and correct — a
genuine, previously-unstated gap in the audit's own Ambiguity-1 justification
(`phase3_synthesis.md`), non-load-bearing this cycle but a real correction to
that document's own reasoning. **Finding 3 — `carrier_q95()` is built from
the identical `sign_flip_surrogates()` construction `G0-e(ii)` independently,
three ways, showed anti-conservative on this exact design — is independently
confirmed by direct code read (§0, check I) and is not confined to a future
concern: it is a structural fact about the cycle's own committed machinery,
true today, regardless of whether any future cycle ever reaches a real
`RESOLVED` test.** §2's own reproduction of the `G0-e(ii)` HALT is confirmed.
§2's own passing repetition of "all 144 cell-α combinations" is corrected per
§1.1, non-load-bearing to Finding 3 or any other VISION claim. §4's window-
provenance nit (the residual-structure leg still touches real exp-069/071
residual *values*, even under a HALT) is correct and minor. Adopted in full;
Finding 3 is bound as a forward mandatory constraint, not left as a
"worth-a-line" note (§5, §7).

---

## 3. Red Team's own attacks — findings no seat made

**RT-1 [inconsistency] — Two of six blind Phase-5 seats independently
repeated the exact "every single X" overclaim (§1.1) they were reading the
record specifically to catch, and the reason is structural, not
carelessness: a boolean gate flag and a mean-rate table are both consistent
with 71/72 and with 72/72.** This is worth stating as a house lesson, not
merely a tally: R4's own discipline ("verify before claim, at the resolution
the claim is made at") applies to a Phase-5 *reviewer* re-checking a number
exactly as much as it applies to the cycle that first published it — the two
seats that caught this (PHOTONICS, MATERIALS) did so by iterating the actual
144-row array; the two that repeated it (QUANTUM, VISION) trusted an
aggregate that could not distinguish the two counts. I recommend this
generalization travel into R4's own standing text (§7).

**RT-2 [inconsistency] — The G0-e(i) identity tripwire's own numerical
invariance under the sign fix (§1.2) is an algebraic identity, not a
coincidence, and no document states why.** Old check:
`|dRq_dpsi_num_old − R_i_est|` where `dRq_dpsi_num_old = −raw_fd`. New check:
`|dRq_dpsi_num_new − (−R_i_est)|` where `dRq_dpsi_num_new = raw_fd`. These
are algebraically the same expression (`|−raw_fd − R_i_est|` both times), so
the tripwire's own PASS/FAIL was *always* sign-agnostic by construction —
which is exactly why a circularly-negated version of it could "pass" while
certifying the wrong sign. This is the precise mechanism by which R6's own
safety gate failed to catch the defect it exists to catch: an absolute-value
identity check can validate that *some* consistent sign convention holds,
but cannot by itself certify *which* convention is the physically correct
one — that requires an external, independently-derived reference (here,
direct substitution into the write-up's own formula, §1.2), not a
self-referential finite difference. A future `G0-e`-class tripwire for a
signed quantity should say so explicitly, or pair the magnitude check with
an independent sign derivation the way this audit's §1.2 does.

**RT-3 [process] — This is the first Phase-5 audit in the T28 differential-
fit sub-thread (071→072→073) whose own applied same-shift fix required
re-running `run.py` and diffing the full output, rather than hand-verifying
individual figures.** Recorded because it worked cleanly (§0 check H) and
because the *reason* it worked cleanly — a re-derivation that changes a
labeled sign but leaves an absolute-value gate untouched — is not
guaranteed to generalize to a future fix. Any future Red Team audit applying
a `run.py` code change to this or a sibling instrument should re-run and
diff the complete JSON tree, not spot-check the fields expected to move,
exactly as done here.

**RT-4 [statistical-defect, forward] — `carrier_q95()`'s own uncharacterized
risk (VISION's Finding 3) compounds with Finding 2's own quantified proxy
failure in a way neither finding states on its own.** Finding 2 shows the
proxy Red Team used to justify the *shared*-`q95` design choice
(Ambiguity 1) understates the real values by up to 6.2×; Finding 3 shows the
real values themselves come from a construction independently shown
anti-conservative. Both point the same direction — `carrier_q95()`'s own
95th-percentile threshold is more likely to run *too low* (over-admitting
carriers as consistent, or under-admitting the wrong-carrier comparator,
depending on which side of the gate the leverage effect bites) than too
high, on this exact design. This is not yet a quantified bound (neither
finding alone establishes the sign or size of the composite effect), but it
sharpens why §5/§7 bind this as mandatory, not optional, forward work.

---

## 4. Checkpoint determination — all five criteria, explicit

**Criterion 1 (a configuration passes all constraint metrics): DOES NOT
FIRE.** No constraint metric was scored — T1 escape route is `null`, `G0-e(ii)`
HALTed before any real pair was analyzed, and no pair could have reached a
scored constraint-3 outcome even had it not (this instrument scores T28's
own periodicity mechanism, not a constraint-1–4 configuration). Confirmed by
every seat and independently here (`results.json`'s `t1_escape_route: null`,
`per_pair: {}`).

**Criterion 2 (a proven boundary within a mechanism class): DOES NOT FIRE.**
Nothing here closes a mechanism class or a constraint subset. The `L(T)`
leakage budget (QUANTUM, carried from exp-072) and EM's Cramér–Rao pricing
are candidate closing bounds for the *differential-fit-in-this-window*
question — a real, honest "mapped constraint boundary" in PANEL.md's own
sense, if computed — but neither was computed this cycle; both remain
queued (§7).

**Criterion 3 (engine physics beyond validated bench classes): DOES NOT
FIRE.** Zero FDTD calls, zero `lab/` diff — independently confirmed (§0,
check K) directly against the repository, not merely read from the cycle's
own claim.

**Criterion 5 (two consecutive non-advancing iterations): DOES NOT FIRE —
ruled explicitly, per QUANTUM's own request that this not apply by inertia.**
This program's own governing precedent (Iteration 48's ruling on T28's third
consecutive PARTIAL) holds that criterion 5 does not fire as long as each
cycle delivers "independently verifiable, load-bearing narrowing" — and, per
the task's own framing, this program has already treated a process-only/
instrument-integrity result as satisfying that bar without qualification
(Iteration 47's desk-check batch: "no mechanism identified for T28... no
Checkpoint criterion fires"). exp-073 clears the same bar, and clears it
twice: (1) its own headline — a genuine, quantified, now five-times-
independently-confirmed (QUANTUM's Phase-2 critique, Red Team's Phase-2
audit, the official Phase-4 run, EM's Phase-5 review, this audit's own
re-derivation) methodological result about an entire instrument class
(leverage-driven anti-conservative sign-flip nulls on small `n=31,p=5`
carrier-conditioned designs), directly reusable by any future cycle fitting
a similar coefficient, on this window or a different one; (2) this audit's
own two corrections (§1) are themselves genuine, load-bearing narrowing —
the residual-structure leg's actual (non-)construction, and the corrected
`dR_q/dψ̄` identity, are both real, reusable findings that would otherwise
have silently propagated into every future reuse of this machinery. Two
consecutive genuinely-narrowing cycles is the established non-firing pattern,
not the firing one.

**But the pattern QUANTUM and ELECTROMAGNETISM both independently flagged is
real and is bound as a forward constraint, not waved off.** This is the
*fifth* consecutive non-decisive T28 cycle (Iterations 46/47/48/49/50,
exp-069→073) and the *third* consecutive cycle of the differential/beat-fit
sub-thread specifically (071→072→073) in which T28's own substantive
question — the mechanism behind the ~2.84°-family periodicity — has not
moved at all: exp-071 established the window cannot resolve absolute
periods; exp-072 built the differential fix, shipped a sign bug, and showed
the corrected instrument is non-identifiable in this window against a broad
periodic-contaminant band; exp-073 built the corrected re-issue and HALTed
on a null-calibration defect before scoring a single pair. **Binding
forward requirement (adopted from EM's ranked-#3 and QUANTUM's Finding 3,
matching this program's own Block-MINI precedent — a pre-committed decision
rule, not an open-ended deferral):** Iteration 51 must explicitly rule, in
writing, what a sixth non-advancing cycle on this exact sub-thread would
mean — either (a) commit the window-pricing calculation (§7, item 1) as a
genuinely decisive gate: if it shows 36°–42° cannot support a
carrier-conditioned discriminator at any achievable SNR under any correctly
calibrated null, that IS the honest closing bound (PANEL.md's own "mapped
constraint boundary" product) and the differential-fit sub-thread is
formally retired in this window, full stop; or (b) if the pricing licenses
further spend, state explicitly that a further HALT or a further NEITHER
with no real pair resolved is the trigger for formal retirement, not a sixth
deferral. This does not fire criterion 5 today; it forecloses criterion 5
from applying by silent inertia a sixth time.

### Criterion 4 (Red Team flags program-integrity drift): **FIRES**, on the `dR_q/dψ̄` sign defect (§1.2). The 72/72 finding (§1.1) is folded in as a supporting, non-independently-firing instance.

I weighed the strongest available non-firing argument — the same one this
program's own precedent requires be stated and rebutted, not ignored — and
it is not sufficient, for reasons that track this program's own established
tests almost exactly.

**1. This is the firing shape, not the non-firing one, by the program's own
stated test.** Iteration 45 drew the line explicitly: defects "found-and-
fixed by the cycle's own process before close" do not fire; defects that
"took blind Phase-5 seats plus the final audit to surface" do. The Director
*did* notice a contradiction during Phase-3 development — a genuine attempt
at the self-catch discipline exp-072's own Director used correctly to find
`_amp_phase_at`'s missing `w·x̄` shift — but here the self-catch's own
*resolution* was wrong: it discarded a correctly-computed number by
inventing an unsupported symbol distinction, then declared the wrong answer
"Fixed" and "independently re-verified" in a frozen document. That wrong
resolution survived Phase 3, Phase 4, and five of six Phase-5 seats; it took
one blind seat (ELECTROMAGNETISM) using three independent derivation
methods, plus this final audit's own independent fourth re-derivation, to
correct it. This is unambiguously the "took Phase 5 to surface" shape, not
the "cycle's own process caught it" shape — a near-miss self-catch that
reached the wrong conclusion is not the same event as a self-catch that
reached the right one, and this program's own Iteration-36 precedent (below)
already establishes which way a near-miss inside the fix cuts.

**2. A written verification claim in a frozen document is false.**
`phase3_synthesis.md`'s Ambiguity 4 states, as fact: *"independently
re-verified this cycle against exp-072's own real, published `(T_x, ψ, R_i)`
values (ratio −1.0000000000 to 10 decimals at all four pairs **before this
sign correction**; +1.0000000000 **after it**)."* This sentence is true
about the *arithmetic performed* and false about *which of the two results
is correct* — the "before" figure is right, the "after" figure is the one
that entered the record as fact. PANEL.md's criterion 4 names unfalsifiable
claims and program-integrity drift; a verification claim that inverts the
correct result while narrating its own correctness is squarely inside that
class, not its edge — the same structural shape as exp-072's own Checkpoint-
4-firing defect (`phase3_synthesis.md`'s "All 15 docket items... verbatim...
ZERO items un-adopted," verified false on eight counts).

**3. Aggravation, on this program's own Iteration-36 precedent, applied
across cycles rather than within one.** Iteration 36 ruled that a defect
recurring "inside the very cycle whose own fix was written to close it"
aggravates rather than mitigates. This is the identical shape one level up:
`dR_q/dψ̄`'s sign was asserted once (exp-072, THERMODYNAMICS' structural
claim), passed a check that structurally could not distinguish `+R_i` from
`−R_i` (a ratio/magnitude test), and was then defended rather than
re-derived the one time this program's own process actually produced the
correct, opposite-signed answer and needed a reason to discard it — inside
*exp-073, the cycle whose entire mandate is to close exactly this class of
inherited, never-independently-re-derived claim* (§0 of `phase1_proposal.md`:
"Every design choice below is justified by an argument that does not
reference exp-072's own observed... signs"). A cycle built specifically to
stop trusting exp-072's own unverified claims trusted this one anyway, at
the exact moment its own correctly-computed number said not to.

**4. A supporting instance, independently confirmed: the 72/72 overclaim
(§1.1).** Real, quotable, non-gating, and independently caught by two of six
blind seats before this audit — matching the "found and fixed within
Phase 5" pattern this program has previously treated as evidence *for*
process health (e.g. the R4-class defects Iteration 36 found alongside its
own firing). I do not treat this instance as independently firing (I adopt
MATERIALS' own explicit reasoning: it never touched a published gate outcome,
a coefficient, or the Combined Verdict, and it was caught blind, not only by
the final audit) — but it is real supporting texture for the broader
"quotable numeric claims in this cycle's own deliverables require the same
skepticism this cycle demands of exp-072's" finding that criterion 4 exists
to name, and I record it as such rather than omit it because it does not
independently clear the bar.

**Mitigating, and recorded in full because it is real.** `G0-e(ii)` — the
gate this cycle's own docket built specifically as a second, harder-edged
safety net beyond R6's original ground-truth-recovery mandate — worked
exactly as intended: a real, load-bearing statistical defect was caught and
HALTed before any real data was scored, independently confirmed four ways
before this audit and a fifth time here. The Combined Verdict is unaffected
by both findings in this section. No engine physics is implicated. This
cycle's own contamination-discipline extension (Attack 6, §3 of its own
Phase-2 audit) is a genuine, novel improvement over exp-072's own framework,
correctly applied throughout. The defect this section rules on was found and
corrected before it reached `LOGBOOK.md` — which is what a notification-not-
pause ruling, below, is for.

**Ruled a notification, not a pause — this program's unbroken precedent,
zero exceptions across nine prior firings (Iterations 17, 36, 37, 39×2, 40,
44, 45, 49).** No engine physics is implicated, zero `lab/` diff, the
Combined Verdict stands unchanged and is independently re-verified robust
to both corrections (§1), and the remedy (the same-shift docket, §5) is
actionable without halting any other thread. Marsh is notified via the
LOGBOOK entry and `SESSION_LOG.md` (Director's own next step).

**No new standing tripwire is required beyond what R6 already establishes**
— unlike exp-072's own firing (which produced R6 itself, a genuinely new
house rule), this finding is a *violation* of R6's own existing standard
(a claim about a phase-conditioned coefficient's sign, asserted without an
independent sign-tracked re-derivation, inside the exact machinery R6 exists
to gate), not a gap in what R6 requires. The standing lesson is procedural,
not a new gate: **a "sign correction" applied to reconcile a freshly
computed number against an inherited claim must itself be independently
re-derived by an external method (substitution into the write-up's own
formula, or a from-scratch closed-form derivation) before it is trusted —
never adopted because it makes two numbers agree.** I recommend the Director
fold this into R4's own text (RT-1, above) as an explicit extension: R4
already requires that a "precisely recomputed" figure be produced by
invoking the actual committed function; this extends it to require that a
*sign* correction specifically be justified by an independent derivation,
not by which convention reproduces a prior cycle's claim.

---

## 5. Same-shift mandatory-fix docket

**Applied and independently re-verified this shift (all six items; scope:
`run.py`, `phase3_synthesis.md`, `phase4_results.md`, `NOTES.md` only — zero
`lab/` diff, zero engine-file touch, confirmed §0 check K):**

1. **`run.py`: `dRq_dpsi = R_i` → `dRq_dpsi = -R_i`** in `analyze_pair`,
   with an inline comment carrying the full derivation and pointer to this
   audit. Non-gating field (never read by any `RESOLVED` clause or the
   Combined Verdict), never populated with real data this cycle
   (`per_pair={}`), but corrected so it is right the next time this
   machinery is reused.
2. **`run.py`: `ground_truth_recovery_check`'s identity tripwire** — dropped
   the unjustified extra negation on the raw finite difference and corrected
   the comparison target from `R_i_est` to `-R_i_est`. **Re-run end-to-end;
   full `results.json` diffed field-by-field against the pre-fix committed
   artifact: zero difference except `elapsed_s`.** Combined Verdict
   confirmed unchanged (`HALT_NULL_MISCALIBRATED`); `G0-e(i)` confirmed
   still PASS at the identical worst-cell error (`9.4×10⁻¹¹`).
3. **`phase3_synthesis.md` §3, Ambiguity 4** — erratum block added
   (original text left standing, per house convention: flag, don't
   silently rewrite), stating the correct identity and why the original
   resolution was wrong.
4. **`phase4_results.md`** — (a) the G0-e(i) table row's `dR_q/dψ̄≡R_i` label
   corrected to `≡−R_i`; (b) the "72/72 (residual-structure)"/"both legs...
   every single cell-α combination" bottom-line sentence corrected to
   "71/72... 143/144 combined"; (c) a full Phase-5 erratum section added,
   documenting both corrections with the passing cell identified and the
   non-load-bearing status explained for each; (d) a caveat block added at
   the residual-structure-leg discussion disclosing THERMODYNAMICS' finding
   (§2.4) — the leg does not test correlated residual structure, is
   empirically indistinguishable from the i.i.d. leg (r=0.907), and docket
   item 4 is not actually delivered as specified.
5. **`NOTES.md`** — Idealization 5 corrected (`dR_q/dψ̄ ≡ −R_i`, with the
   erratum noted in place); Result section corrected (71/72, 143/144, with
   the non-load-bearing status stated); the "What changed vs. exp-072" bullet
   for docket items 3–4 corrected with THERMODYNAMICS' finding disclosed
   in place.
6. **`phase3_synthesis.md` §2 item 1** — PHOTONICS' F2 (the frozen
   proposal's own "1,728 cells" arithmetic undercounting its own 12-value
   signed `ΔP` list by 2×) added as an explicit erratum note, previously
   living only in a `run.py` code comment.

**Deferred to Iteration 51, with reasons (not same-shift-safe — each
requires new code, a new design choice, or a fresh calibration run, not a
narrow, data-free correction):**

7. **Build a genuinely order-preserving residual-structure leg for
   `G0-e(ii)`** (THERMODYNAMICS' finding, §2.4) — resample whole per-config
   31-point residual vectors, or a circular-block bootstrap preserving
   θ-adjacency, instead of pooling-and-reshuffling. Bound as a **mandatory
   forward requirement**: no future null-construction fix for this or a
   sibling instrument may be considered validated against correlated
   real-FDTD-residual structure until this leg exists and is run through a
   `G0-e(ii)`-style calibration test.
8. **`carrier_q95()`'s own calibration must be checked before any future
   `RESOLVED` clause (vi) trusts it** (VISION's Finding 3, §2.6, sharpened
   by RT-4) — bound as a **binding forward constraint**: any future cycle
   that reaches a real `RESOLVED` test using this exact `carrier_q95()`
   construction (or the shared, un-re-anchored `sign_flip_surrogates()`
   machinery it calls) must run a `G0-e(ii)`-style calibration sweep on
   `carrier_q95()`'s own output before its 95th-percentile threshold is
   trusted as correctly sized — not inherited unexamined because the parent
   gate happened to pass on a *different* statistic (`R_q`'s own rejection
   rate).
9. **Generalize R6 (MATERIALS' proposal, §2.2) to require a `G0-e(ii)`-style
   null-*calibration* test as standing mandatory machinery**, not merely
   ground-truth *recovery*, for any future sign-flip/residual-permutation
   null on a small, leverage-concentrated design — `G0-e(ii)` was this
   cycle's own Red-Team-authored addition, not required by R6's own text; a
   future, unrelated cycle could otherwise ship an uncalibrated null and
   rediscover this exact failure mode from scratch. Recommended for the
   Director's own LOGBOOK.md rule set, alongside R6.
10. **R4's own text extended** (RT-1, §3) to cover Phase-5 reviewers
    re-checking a prior cycle's numeric claim: an aggregate flag or a
    mean/range table is not sufficient to certify an "every single X" claim;
    the resolution the claim is made at must be independently checked.
    Recommended for the Director's own LOGBOOK.md RULED OUT/R4 entry.

**Docket total: 6 same-shift items (applied, verified), 4 forward items
(bound, not yet built).**

---

## 6. For the Director's LOGBOOK entry

### 6.1 Final headline finding of exp-073

**Combined Verdict: `HALT_NULL_MISCALIBRATED`** — unchanged, verified robust
to both corrections in this audit. No real pair (`C40–C60`, `C60–C70`,
`C70–C80`, `C40–C80`) was ever scored.

> **The substantive methodological result, confirmed independently five
> times over (QUANTUM's Phase-2 critique, Red Team's Phase-2 audit, the
> official Phase-4 run, EM's Phase-5 review, this audit's own final
> re-derivation): a Freedman–Lane-style sign-flip null — sign-flip the
> full-model (5-column) OLS residual, add it back to the null-model
> (4-column) prediction, refit — is correctly centered (`E[R_q^surr]=0`
> exactly, an algebraic consequence of the null-model prediction lying in
> the full model's own column span) but anti-conservative by ~2–6× nominal
> across α∈[0.01,0.10], on a small (`n=31, p=5`), leverage-concentrated,
> carrier-conditioned angular-sweep design. The mechanism is exact, not
> data-dependent: the ramp-coefficient-extraction row of the pseudo-inverse
> weights concentrate on the window's highest-leverage (edge) points,
> exactly where the sign-flip surrogate's own projection residual most
> understates the true sampling variance (`mean diag(M5) = (n−p)/n =
> 26/31 = 0.8387`, `E[Var(R_q^surr)]/Var(R_q^obs) ≈ 0.79`). This is R6/
> `G0-e` working exactly as designed: a pre-registered, data-free gate
> caught a real statistical-calibration defect before any real point was
> scored, converting what could have been a second silent contamination
> event into a genuine, quantified, reusable finding about an entire
> instrument class.**

> **A second, corrective finding, of comparable house-discipline weight:
> `dR_q/dψ̄ ≡ −R_i`, not `+R_i` as this cycle's own frozen `phase3_
> synthesis.md` asserted. The write-up's own `ψ̄` is, by direct textual
> definition (`θ_c = 2πu/T_mean + ψ̄`), exactly `design_matrix`'s own `psi`
> argument — there is no second symbol for it to secretly be the negative
> of. The `+R_i` claim traces to exp-072's own THERMODYNAMICS Phase-5
> review, asserted without a sign-tracked re-derivation and "confirmed" only
> by a magnitude-only check that cannot distinguish `+R_i` from `−R_i`; it
> was never independently re-derived by explicit algebra in either cycle
> until ELECTROMAGNETISM's Phase-5 review this cycle, confirmed here three
> further independent ways (a from-scratch closed-form derivation, a
> from-scratch finite-difference check against exp-072's own real published
> data, and a live re-run of the corrected `run.py` diffed bit-for-bit
> against the pre-fix committed artifact). Non-outcome-determining this
> cycle (the field was never populated with real data; the Combined
> Verdict is verified unchanged after the fix) but a real, corrected defect
> in machinery every future carrier/phase-fit cycle is instructed to reuse
> verbatim — the same defect shape, one cycle later, that fired exp-072's
> own Checkpoint 4. CHECKPOINT criterion 4 fires (notification, not a
> pause) — full ruling and same-shift fix, `phase5_redteam_audit.md`.**

> **A third, minor, independently-confirmed erratum: `phase4_results.md`
> and `NOTES.md` both overstated a null-calibration failure count as
> "72/72 (residual-structure)"/"144/144 fail"; the committed `results.json`
> shows 71/72 (one cell passes at the loosest tested significance level),
> 143/144 combined. Non-load-bearing (the gate's own conjunctive `pass_`
> logic is unaffected either way); independently caught blind by two of six
> Phase-5 seats (PHOTONICS, MATERIALS) before this audit.**

> **A fourth, disclosed, unclosed gap: docket item 4's own "residual-
> structure robustness leg" for `G0-e(ii)` does not test θ-correlated
> residual structure — it bootstraps pooled, order-discarded residual
> values, empirically indistinguishable from the i.i.d. leg it was meant to
> be a harder companion to (paired-cell r=0.907 across 72 cells,
> THERMODYNAMICS' finding, independently re-verified). Does not change the
> Combined Verdict; means the specific hazard this docket item was written
> to close remains open for any future null-construction fix.**

**T28's own substantive question — the mechanism behind the `C80−C40`
padding delta's ~2.84°-family periodicity — is exactly where exp-072 left
it: bounded by window identifiability (leakage 15–36 per unit amplitude
across ~1.8°–5.0°), not advanced and not narrowed by this cycle. This is now
the fifth consecutive non-decisive T28 cycle and the third consecutive cycle
of the differential/beat-fit sub-thread with zero pairs ever resolved
(exp-072: zero of four resolved; exp-073: zero of four even scored).
Checkpoint criterion 5 does not fire (both this cycle and its predecessor
delivered genuine, independently-verifiable narrowing) but Iteration 51 is
bound to rule explicitly on what a sixth non-advancing cycle in this
sub-thread would mean — see §4 and §7.**

**No Checkpoint criterion fires on the physics** (criteria 1/2/3/5 all
explicitly ruled non-firing, §4); **criterion 4 fires on the process finding
above** (the `dR_q/dψ̄` sign defect, with the 72/72 overclaim folded in as a
supporting, non-independently-firing instance), independent of and not
affecting the physics verdict.

### 6.2 Ranked queue for Iteration 51 (synthesised, not vote-averaged)

All six seats converge, at or near #1, on pricing the window before any
further estimator or FDTD spend (PLAN.md's own Iteration-50 queue item 2,
already unexecuted one cycle running) — full convergence, the strongest
cross-seat agreement in this cycle's own record. They split on what comes
after: a properly-calibrated null fix, gated on the pricing result (QUANTUM,
VISION, matching MATERIALS' own D1 in substance though ranked differently);
window extension paired explicitly with a fresh calibration re-test (EM,
VISION); G40/`PAD` decorrelation, unanimous #2/#3, orthogonal to everything
else; and one genuinely new, charter-engaged physics candidate (PHOTONICS'
WKB/adiabatic boundary-reflectance model) that no prior T28 cycle has run.
Synthesis, reconciling all six:

**1. Price the window — zero FDTD, decisive either way, near-unanimous #1.**
EM's Cramér–Rao/conditioning pricing (`cond=529` at a 9-column two-tone
design, ≈6× SE inflation on `R_q`) and QUANTUM's already-established `L(T)`
leakage budget (non-identifiable against ~1.8°–5.0° periodic contaminants)
both answer, at zero cost, whether `θ∈[36°,42°]` can ever support a
carrier-conditioned discriminator at achievable SNR, for *any* correctly
calibrated null — a question logically prior to "is this specific null
calibrated," which this cycle answered "no" for one construction only.
**Extended per VISION's own §4 synergy point and PHOTONICS' own §2 caution,
both independently converging on the same requirement**: the pricing must
also explicitly report how `cond(X5)` and the leverage-concentration pattern
(`mean diag(M5)=(n−p)/n`, exact and window-width-independent by algebra;
*where* leverage concentrates is not) would change at a widened window —
answering not just "does a wider window resolve the period" but "would a
wider window plausibly let a future `G0-e(ii)`-style test pass at all." If
the answer is no — EM's own number already suggests it might be — that is a
real, citable closing bound on the differential-fit route in this window
(PANEL.md's own "mapped constraint boundary" alternative product), worth
more than a sixth non-decisive cycle, and it directly triggers §4's own
Checkpoint-5 forward requirement: formally retire the sub-thread in this
window.

**2. G40/`PAD` decorrelation — ~31 calls if MATERIALS' geometry-reuse claim
verifies, unanimous #2/#3.** The cheapest FDTD relief on the board,
orthogonal to item 1 and to the null-calibration question, and the only
queued item that actually *relieves* (not merely discloses) the
`ABSORB`-or-`PAD` confound binding every T28 deliverable since Iteration 48.
Readout on the phase-invariant amplitude channel `√(A_i²+A_q²)/a`
(baseline, exp-072: 0.161/0.041/0.020/0.166) — conditions on no fitted
carrier phase at all, so it inherits neither the window-resolution problem
nor this cycle's own leverage-driven calibration problem. MATERIALS' own
structural caveat (the 2×2 factorial is not completable — `config(80,0)`
gives `clear_span_y=−40` — so main effects are identifiable only under
additivity, the interaction not at all) must be pre-registered up front by
whichever cycle runs it.

**3. A properly-calibrated null construction, including the order-preserving
residual-structure leg (docket item 7, above) — explicitly gated on item 1's
result, not built in parallel.** QUANTUM's and VISION's own ranking logic is
adopted verbatim: building a better-calibrated null for a window that cannot
resolve the target signal at any achievable SNR solves the wrong stage of
the problem. If item 1 licenses further spend in this window (or a widened
one), this becomes the load-bearing next build — an exact small-sample
permutation test respecting the design's own leverage structure, or a
finite-sample-corrected variance estimator, gated by its own fresh
`G0-e(ii)`-style calibration test (per docket item 9's own generalized
standing rule) before it may gate any real data.

**4. PHOTONICS' WKB/adiabatic boundary-reflectance model for the graded-loss
`ABSORB` band — zero FDTD, genuinely new to this ranking, runs in parallel
with items 1–3.** Queued twice before (Iteration 46/47) and confirmed
dropped without execution both times. An analytic (not fitted) model of the
reflection phase a graded-absorption boundary of varying depth produces as a
function of angle, computed from the boundary's own admittance profile, zero
data — the one candidate on the board that engages a seat's own charter
directly rather than re-verifying statistics. Either explains the ~2.5°
family as an ordinary boundary-reflectance phase effect (closing T28's own
mechanism question outright) or rules it out (narrowing the remaining
candidate space) — either outcome is a genuine physics finding, the first
one this five-cycle sub-thread would produce.

**5. Standing rules for the Director to adopt in LOGBOOK.md, not a new FDTD
item:** docket items 9–10 (§5) — generalize R6 to require null-calibration
testing as standing machinery, and extend R4 to cover a Phase-5 reviewer's
own re-checking of a prior claim. Both zero-cost, both directly generalizing
this cycle's own two findings the way R6 itself generalized exp-072's.

**6. A pre-committed decision rule on T28's own differential-fit sub-thread
(§4's own binding requirement, EM's ranked-#3, QUANTUM's Finding 3) — must
be stated explicitly in Iteration 51's own entry, not left implicit.** Item
1's own result is the natural occasion: if it closes the window, that
closure IS the rule (formal retirement); if it does not, Iteration 51 must
state in writing what a sixth non-advancing cycle would mean, matching the
Block-MINI precedent (a formal, pre-committed non-decisive-outcome
retirement trigger) rather than defaulting to a further deferral.

*Deprioritized, with reasons*: `R_contact`'s literature search — orthogonal,
tooling-permitting, unchanged in ranking by every seat that mentioned it, now
11+ consecutive cycles blocked and outlasting every T28 sub-thread discussed
above; PHOTONICS' own MATERIALS-adjacent literature checks — not raised this
cycle, no seat proposed reopening them. *R5 check: none of the six items
above re-proposes a ruled-out idea; item 3 is a construction fix to an
existing pre-registered gate, not a new parameter search.*

---

## 7. Closing assessment

This cycle's own process is the best-documented instance yet of this
program's own stated purpose for the Phase-5 mechanism: a real, load-bearing
statistical defect (`G0-e(ii)`'s own miscalibration) was found by the exact
gate built to find it, forecast in writing before the official run, and
reported honestly as the cycle's own genuine result rather than a wasted
HALT. Every one of five blind Phase-2 critiques found a real defect with a
workable remedy; the Phase-2 Red Team audit re-implemented, not merely
adjudicated, nearly every one of them; the Phase-3 synthesis disclosed four
genuine implementation-level judgment calls in the open, in a document that
explicitly avoided repeating exp-072's own "verbatim, ZERO items un-adopted"
overclaim. That discipline is real, and this audit's own findings do not
erase it.

But the one place this cycle's own process reached for an *independent*
re-derivation and got a *contradiction* against an inherited claim, it
resolved the contradiction by discarding the correct answer — inside a
document whose own §0 states, as this cycle's entire premise, that no design
choice may rest on an exp-072 claim without independent re-derivation. The
lesson is not that this cycle's discipline was absent; it is that
discipline applied to *finding* a discrepancy is not the same discipline as
trusting what the discrepancy says once found. `G0-e(ii)` caught a defect it
was built to catch. The one defect this cycle's own machinery *did* surface
on its own — and then explained away — is the one this audit exists to
correct.

`HALT_NULL_MISCALIBRATED` stands, verified robust to both corrections.
Checkpoint criterion 4 fires, once, on the process. The docket is ten items;
six are done.
