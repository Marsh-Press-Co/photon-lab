# PHASE 2 — RED TEAM AUDIT · Panel Iteration 57 · exp-080
## Adjudicating EM's validity pre-check and all five blind Phase-2 critiques: does the realizable-admittance substitution really flip part (b), does building PHOTONICS' own not-yet-built construction really reproduce the same pathology, and what does that mean for Iteration 58's queue

**Seat: RED TEAM.** Read, in order: `PANEL.md` in full (this seat's own
charter, the target phenomenon + four constraints, the five-phase loop,
Checkpoints §1-5); `AGENTS.md` in full; `experiments/080-.../phase1_proposal.md`
in full, including PHASE 1 RESULTS; `validity_precheck.py`;
`validity_precheck_results.json`; all five blind Phase-2 critiques
(`phase2_critique_{photonics,materials,thermodynamics,quantum,vision}.md`);
for background, `experiments/079-.../phase5_redteam_audit.md` §3/§7 and
`phase5_review_photonics.md` §4; `y_wall_aperture_sum.py`,
`boundary_reflectance.py`, `design_geometry.py` directly (not taken from any
seat's description); `LOGBOOK.md`'s RULED-OUT registry (R1-R9) and the T28
thread tail. I alone see the complete record and all five blind critiques,
and speak last.

**No RULED-OUT item (R1-R9) is re-proposed or re-litigated by this document
or by anything it adjudicates.**

---

## 0. What I independently verified

Every number below was recomputed in a fresh scratch script
(`/tmp/.../scratchpad/redteam_verify.py`), importing the SAME already-gated
primitives `validity_precheck.py` itself imports (`dg065.CONFIGS`,
`br.n_profile_exact`/`damp_e_profile`/`nu_profile`/`CPL`,
`ywas.theta_local_deg`/`dist_image_cells`/`aperture_amplitude`/
`build_aperture_grid`/`source_driven_phase`/`reflection_coefficient_vec`/
`echo_field_curve`/`K600`/`_trapz`) — never copied from any critique's own
prose, never taken on trust.

| # | Claim | Source | My result | Reproduced? |
|---|---|---|---|---|
| 1 | `d_F=W²/λ=113,100.8` cells; `dist_image` ratios `0.76-2.15%`; `theta_local` envelope `[5.27°,15.00°]`; spread `2.60-2.75×`, all 5 configs | EM part (a) | Bit-identical, all 5 configs, computed from raw `dg065.CONFIGS` in a script that imports nothing from `validity_precheck.py` itself | **YES, exact** |
| 2 | True per-point `E_echo` curves match the committed `y_wall_aperture_sum_results.json::primary_model_curves` to float precision | EM's version-drift guard | `max\|recomputed-committed\|=0.0` for both proxies, all 5 configs, re-derived via a fresh call to `ywas.echo_field_curve` | **YES, exact** |
| 3 | `θ_eff` (primary, amp-weighted) values and `R²(Re,primary)` per config; mean `0.7345`, min `0.5214` (C70) | EM part (b), matched admittance | Bit-identical to 13+ significant figures (`0.7344904097331045` / `0.5214450714184593`), from a from-scratch script reimplementing the single-angle integral, not calling `validity_precheck.py`'s functions | **YES, exact** |
| 4 | Realizable (`μ_r=1`, `Zi=1/√(n²-sin²θ)`) admittance rerun of part (b): mean `R²(Re)=0.4305`; C40, G40 negative (`-0.62`, `-0.21`) | MATERIALS | `mean=0.4305`; `C40=-0.6230`, `G40=-0.2103`; `C60=0.9982`, `C70=0.9916`, `C80=0.9959` (these three not reported by MATERIALS but consistent with its own mean) | **YES, exact** |
| 5 | `|r(theta_eff)|²` values `1e-13` to `1e-8` are the "wrong angle"; `|r(90°-θ_beam)|²` at the real 36°-42° grid runs `2.5e-4` to `1.5e-3` for ABSORB=40, worst case `0.149%` | THERMODYNAMICS | Spot-checked at 4 ABSORB depths × 3 θ_beam points: `1.4943e-03`/`6.2003e-04`/`2.4822e-04` (ABSORB=40) down to `4.0994e-08` (ABSORB=80, θ_beam=42°) — matches THERMODYNAMICS' table to the printed digit at every cell checked | **YES, exact** |
| 6 | Best-fit scale `α*` of `|E_ablated|` against true `|E_echo|` caps `R²(abs)` at `-1.65` (C70) / `-2.30` (C80), vs. the reported `-7.82`/`-8.45` | PHOTONICS | `α*=2.6017e-6→R²=-1.6481` (C70); `α*=1.3743e-6→R²=-2.2956` (C80) | **YES, to the printed digit** |
| 7 | `git log` on `phase1_proposal.md`: exactly 2 commits, `6fb6b99`/`23203cc`, 2m21s apart | VISION | Confirmed: `6fb6b999` at 15:06:19, `23203cc3` at 15:08:40 — exactly 2m21s | **YES, exact** |
| 8 | QUANTUM's `E_photonics(θ_beam)=r(90°-θ_beam;ABSORB)·W(θ_beam)` construction (`W`=exp-079's own ablated `r≡1` integral): raw `R²(Re)` catastrophic (`-8×10⁴` to `-2×10⁷`); scale-corrected mean `R²(Re)=0.602`, min `0.085` (C70); `R²(abs)` negative at C70/C80 | QUANTUM | Raw `R²(Re)` per config: `C40=-1.093e5, C60=-5.179e6, C70=-3.334e5, C80=-1.065e6, G40=-8.153e4` — matches QUANTUM's table digit-for-digit at every config. Scale-corrected `R²(Re)`: `C40=0.8836, C60=0.6985, C70=0.0852, C80=0.5072, G40=0.8356` → mean `0.6020`, min `0.0852` (C70). Scale-corrected `R²(abs)`: `C70=-4.4949, C80=-7.7066` | **YES, exact to 4 decimals on every entry** |

**Summary: every load-bearing numeric claim across all five blind critiques
independently reproduces from primitives, with zero discrepancy found.**
This is an unusually clean cycle by this program's own R4 standard — the
disagreements below are entirely about scope, framing, and what the record
should conclude from correctly-computed numbers, not about any miscalculated
figure. Full scratch script and JSON: `/tmp/claude-0/.../scratchpad/
redteam_verify.py`, `redteam_verify_results.json` (session-local; the
numbers are reproduced in the tables above and are re-derivable from the
already-committed repo files alone).

**One reproduction-methodology note, disclosed rather than buried**: for
item 4 (MATERIALS), "rerun (b) end-to-end" means BOTH the true per-point
curve and the single-angle model are recomputed under the realizable
admittance consistently (mirroring exp-079's own MATERIALS Phase-5 §2b
methodology, independently confirmed there by that cycle's own Red Team
audit) — not a mismatched comparison of a realizable single-angle model
against the matched-family truth. I verified this is the correct reading by
reproducing MATERIALS' exact numbers only under this consistent-family
interpretation; a mismatched-family comparison would not have hit
`0.4305`/`-0.62`/`-0.21` to four significant figures by coincidence.

---

## 1. Numbered attacks

### Attack 1 — `[inconsistency]` EM's Combined-reading recommendation is now stale relative to independently-verified evidence within this SAME Phase-2 layer

`phase1_proposal.md`'s Combined reading (post-freeze) states Idealization
2's caveat as a live, unresolved limit: PHOTONICS' `θ_beam`-dependent
construction is "a structurally different object... this test cannot rule
it out," and recommends proceeding to "PHOTONICS' own §4 build... carry
this cycle's own (b) finding forward explicitly as a documented caveat."
That was an honest statement of what EM's OWN test could show at the time
it was written. But QUANTUM's blind critique, working independently and
without seeing EM's Combined-reading language, computed exactly the check
Idealization 2 says is needed — built PHOTONICS' actual construction with
zero new FDTD and scored it against the same per-point curve — and found
(§0 item 8, independently reproduced) that it does NOT clear the bar: raw
comparison is catastrophically negative, and even the single most generous
possible correction (an optimal real-scalar rescale that is not itself part
of the physical model, since `r(90°-θ_beam)` has no free amplitude
parameter) caps at a WORSE floor (`0.085` at C70) than this cycle's own
already-INCONCLUSIVE static-`θ_eff` floor (`0.5214`). Treating Idealization
2's caveat as still "untested" going into Phase 3/LOGBOOK, when it has in
fact been tested and failed, inside this SAME Phase-2 layer, would be an
internal inconsistency in the record's own forward-looking claim versus its
own now-available evidence. This is not a defect in EM's own document as
written (the caveat was honestly disclosed as untested at freeze time) — it
is a live risk for what Phase 3 does NEXT with it. **Fix**: Phase 3
synthesis must explicitly reconcile QUANTUM's finding into the Combined
Verdict, not silently carry forward EM's pre-QUANTUM framing. See §4/§6.

### Attack 2 — `[inconsistency]` a single-admittance-family headline number, when the cited family is already established program-wide as unobtainium

`validity_precheck_results.json`/`phase1_proposal.md`'s PHASE 1 RESULTS
report part (b)'s verdict as `mean R²=0.7345, INCONCLUSIVE` under the
matched (`μ_r≠1`) admittance alone — the same admittance exp-079's own
MATERIALS review (independently re-confirmed by that cycle's Red Team
audit, `phase5_redteam_audit.md` §0.7/§2) already established requires "a
broadband, angle-tracking magnetic-loss response... with no realizable
analog for an ordinary dielectric/conductive coating at optical
frequencies" — i.e., unobtainium. Reporting only the unobtainium-family
number as the headline, with the realizable-family result absent from the
committed file entirely, is not a false claim, but it is materially
incomplete in exactly the shape this program's own R8/R9-family rules exist
to catch (an inherited or single-family number cited as if it settles the
question, when a cheap alternate-family check — independently confirmed
here to move the verdict for 2 of 5 configs into REFUTE-adjacent territory
— exists and was not run before Phase 1 closed). **Fix**: append MATERIALS'
realizable-admittance table to the permanent record (§4 fix docket).

### Attack 3 — informational, not an attack: VISION's contingency-table finding

VISION correctly self-scores this as a "rigor caveat," not a violation, and
I concur on independent review of §5's contingency table: the
FORECLOSE+REFUTE branch (mean `R²<0.50`) WAS a genuinely reachable,
falsifiable outcome — the observed `0.7345` cleared it with real margin
(`0.23` above the bar), not by a hair. "Proceed anyway" being the
structurally-favored branch across 2 of 3 named outcomes is a fact about
how the two pre-registered thresholds happen to correlate at this bench's
geometry, not a hedge built into the thresholds themselves after the fact.
**No fix required**; carried forward as disclosed context only.

### Attack 4 — `[inconsistency]`, minor: the negative-`R²(abs)` narrative overstates an avoidable calibration artifact as unexplained mechanism

PHOTONICS' independently-reproduced finding (§0 item 6): the reported
`R²(abs)=-7.82/-8.45` (C70/C80) is roughly double the true shape-only floor
(`-1.65/-2.30`) because `|r(θ_eff)|` happens to undershoot the
least-squares-optimal scale by ~2× — a fixable calibration artifact, not
new physics, conflated in the proposal's prose with a "Jensen-type phase
rotation" story presented as if it were the whole explanation. The
ABSORB-depth concentration (clean at 40/60/G40, catastrophic only at 70/80)
is real and unexplained — a genuine, disclosed-as-open optical-response
question, not an inconsistency, but the write-up should not have let the
calibration-inflated number stand as the disclosed "genuine, if secondary,
finding" without noting a one-line check would have separated the two
components. **Fix**: report both numbers side by side (§4 fix docket).

**No `[unfalsifiable]` or `[inexpressible]` attacks found.** This cycle
makes no mechanism claim and proposes no new physics — it is pure desk
arithmetic on already-gated primitives, so the expressibility contract is
trivially satisfied throughout, and every prediction was pre-registered
with falsifiable numeric bands before computation (verified via the git
history check, item 7 above). **No `[constraint-#N-violation]` attacks
found.** Zero constraint-3 (or any constraint) engagement anywhere in this
cycle's record, independently confirmed by my own text search of
`phase1_proposal.md` and all five critiques for
witness/silhouette/ambient/scotopic/photopic language (zero hits outside
VISION's own audit of the same), matching VISION's finding exactly.

---

## 2. Disposition of the five blind critiques

| Seat | Verdict as filed | My independent check | Disposition |
|---|---|---|---|
| PHOTONICS | support-with-changes | `α*`-based R² independently reproduced exactly (§0 item 6); the ABSORB-depth-concentration observation is real and not explained anywhere else in the record | **ADOPT IN FULL.** Fold both the calibration-corrected and raw abs-proxy numbers into the permanent record (Attack 4). |
| MATERIALS | support-with-changes | Realizable-admittance rerun independently reproduced exactly, digit-for-digit, including the sign and rough magnitude of C40/G40's negative R² (§0 item 4) | **ADOPT IN FULL.** This is the single most consequential of the "smaller" findings — elevate its priority beyond a prose caveat (Attack 2); the realizable-family table belongs in the committed JSON, not just this critique file. |
| THERMODYNAMICS | support-with-changes | `\|r(90°-θ_beam)\|²` table independently reproduced exactly at every spot-checked cell (§0 item 5) | **ADOPT IN FULL.** Append the table verbatim to the permanent record; it answers a standing program question (the power-budget sidecar) that the committed JSON currently answers at the wrong angle by 5 orders of magnitude. |
| QUANTUM | support-with-changes | The full construction, raw and scale-corrected, independently reproduced to 4 decimal places on every entry (§0 item 8) — the strongest reproduction of any critique this cycle | **ADOPT IN FULL, and go further than QUANTUM's own stated "required change."** QUANTUM asks that a SUPPORT/INCONCLUSIVE/REFUTE band be pre-registered "before or immediately upon building" PHOTONICS' construction — but the construction, in its image-term form, is already built and already scored, by QUANTUM's own critique, using zero new FDTD and fully gated primitives. My own ruling (§4, §6) treats this as effectively already-done, not merely "a required change before a future build" — a step beyond what QUANTUM itself proposed, because QUANTUM (correctly, given its blind mandate) did not see that no other seat had already supplied this construction, whereas I see the whole record and can declare the build item satisfied. |
| VISION | support | Git-history claim independently reproduced exactly (§0 item 7); the contingency-table observation independently re-assessed as informational (Attack 3) | **ADOPT IN FULL.** No changes requested; VISION's own self-scoring (this is a rigor caveat, not a violation) is correct on independent review. |

**No blind critique is overridden.** Every seat's own numeric claim
reproduces and every seat's own verdict (support-with-changes ×4, support
×1) is well-calibrated to what it found. The one place I go beyond simple
adoption is procedural, not evidentiary: I read QUANTUM's own "required
change" as understating its own finding's implication once combined with
the fact (visible only from my all-seeing vantage point) that no other
seat, and nothing in `phase1_proposal.md` itself, has actually built
PHOTONICS' §4 construction yet — QUANTUM's own critique IS that build, in
substance. This is the kind of cross-seat synthesis exp-079's own Red Team
final audit found (in its own words) "no single blind Phase-5 review,
working alone, could have delivered" — the same shape recurs here one cycle
later, one phase earlier.

---

## 3. Overall ruling: **PROCEED-WITH-MANDATORY-FIXES**

Not PROCEED-AS-IS: Attack 1 and Attack 2 identify a live risk that Phase 3
synthesis and Iteration 58's queue framing, if drafted from
`phase1_proposal.md`'s own pre-QUANTUM Combined-reading language without
correction, would understate what this Phase-2 layer has already
established. Not HALT: no false claim survives (§0 — everything reproduces),
no RULED-OUT item is re-proposed, no `lab/`/engine change occurred, and the
program is not at risk — this is squarely a record-completeness and
framing correction, the same shape (and same remedy: a same-shift fix
docket, applied at the next synthesis step) as exp-079's own Phase-5 final
audit's non-firing Checkpoint-4 pattern.

### Fix docket, prioritized, for Phase 3 synthesis

1. **[HIGH]** Do not carry `phase1_proposal.md`'s "structurally different
   object... this test cannot rule it out" framing into Iteration 57's
   Combined Verdict unqualified. State explicitly: PHOTONICS' own §4 image
   term HAS now been built (by QUANTUM, zero new FDTD, fully gated
   primitives) and scored against the same per-point comparison this
   cycle's own part (b) uses; raw comparison is a catastrophic REFUTE by
   amplitude (a direct numerical consequence of part (a)'s FORECLOSE — the
   aperture never actually presents `90°-θ_beam` to the wall); the most
   generous possible shape-only rescue still lands at a worse floor
   (`0.085`) than this cycle's own already-INCONCLUSIVE result (`0.5214`).
2. **[HIGH]** Append MATERIALS' realizable-admittance rerun of part (b) to
   `validity_precheck_results.json`/`phase1_proposal.md` as a disclosed
   second verdict, not left in the critique file alone: mean `R²=0.4305`
   (below the REFUTE bar), C40/G40 negative, concentrated exactly at
   ABSORB=40 where the two admittance families are known (exp-079 MATERIALS
   §2a) to diverge most (`89.08°` `arg(r)` deviation).
3. **[MEDIUM]** Append THERMODYNAMICS' `|r(90°-θ_beam)|²` table (correct
   angle for the standing power-budget question) to the permanent record,
   explicitly labeled as distinct from the JSON's own `theta_eff`-based
   numbers (5+ orders of magnitude smaller, answering a different
   question) — a reader should not be able to mistake one for the other.
4. **[MEDIUM]** Report PHOTONICS' calibration-corrected `α*`-based
   `R²(abs)` (`-1.65`/`-2.30`) alongside the raw `θ_eff`-based number
   (`-7.82`/`-8.45`), and flag the ABSORB-depth concentration (worst at 70/80)
   as an open, unexplained optical-response question for whoever next
   examines this construction family.
5. **[LOW]** Note explicitly, as an inherited-not-verified assumption, that
   QUANTUM's (and PHOTONICS' §4) construction omits `E_direct(θ_beam)` —
   valid only insofar as `E_direct` cancels identically across congruent
   configs' pair deltas (an assumption inherited from exp-079's own
   modeling choice, never independently re-derived by anyone in this
   sub-thread's record I read). Cheap to check; not yet done.

---

## 4. Checkpoint ruling

**Criterion 1** (a configuration passes all constraint metrics): **N/A.**
Zero constraint-3 or any-constraint engagement anywhere in this cycle,
confirmed independently by direct text search, matching VISION's own
finding.

**Criterion 2** (a proven mechanism-class boundary): **NOT YET RIPE — a
closer call than exp-079's own non-firing ruling, reasoned through, not
asserted.** Exp-079's own Red Team final audit (§7 item 11) left the
plane-wave/global-steering construction as the ONE remaining member of the
coherent-echo mechanism class "not structurally guaranteed by Attack 1's
own mechanism to fail." QUANTUM's independently-reproduced finding (§0 item
8) is real evidence against it — but it is evidence of a specific,
narrower kind than Checkpoint 2 requires. QUANTUM's comparison target is
exp-079's own per-point aperture-sum curve, which is itself only a
CANDIDATE model, already shown (via that cycle's own reflectance-ablation
control) to be structurally incapable of discriminating a real echo from no
echo at all. A construction failing to reproduce an already-discredited
model's shape is not the same as a construction failing to reproduce the
REAL T28 reference periods via the pair-delta/free-period-fit pipeline
every prior y-wall model in this sub-thread has actually been scored
against — and that pipeline has never been run on PHOTONICS' construction.
**Ruling: does not fire.** The raw amplitude-regime catastrophe (§0 item 8,
100-400× mismatch, a hard numerical consequence of part (a)'s FORECLOSE) is
strong, cheap, decisive-feeling evidence, but the actually-decisive,
constraint-relevant test (pair-delta periods vs. real T28 data) remains
unrun. This is exactly the gap Iteration 58's queue should close (§6), not
a boundary this cycle alone can declare proven.

**Criterion 3** (engine physics beyond validated bench classes): **N/A.**
Zero new FDTD anywhere in this cycle's record — confirmed directly: every
file this cycle produced (`validity_precheck.py` and all five critiques)
imports only already-gated primitives from `dg065`/`br`/`ywas`; my own
independent scratch script does the same.

**Criterion 4** (program-integrity drift): **Reasoned through explicitly,
does not fire, but on a narrower margin than Criterion 2's own reasoning
above.** No false claim was found anywhere (§0 — the cleanest reproduction
record this exact sub-thread has produced: every one of eight independently
re-derived claims across five critiques matched exactly, none merely
"approximately"). The risk this criterion exists to catch — a constraint
quietly dropped, or an unfalsifiable claim allowed to stand — is not
present: Attack 1's concern is about what happens NEXT (Phase 3 synthesis),
not about anything already defended past a freeze point. Matching the
established non-firing shape from exp-079's own Phase-5 final audit
(`phase5_redteam_audit.md` §5): this is genuinely new information,
surfaced by an independent seat, WITHIN this cycle's own Phase-2 review
layer, caught and reconciled by this very audit before Phase 3 finalizes
anything — not a false claim surviving unexamined. **The distinguishing
condition, stated plainly**: if Phase 3 synthesis adopts this audit's fix
docket (§3) and does not simply repeat EM's pre-QUANTUM Combined-reading
language verbatim in the Combined Verdict, criterion 4 continues not to
fire. If it does repeat that language unreconciled, THAT would be the
firing shape one phase later — the same distinction exp-079's own audit
drew for its own near-miss findings (§5 there: "had this audit not
independently re-checked... THAT would have been the firing shape").

**Criterion 5** (two consecutive non-advancing iterations): **Not at risk.**
Exp-079 foreclosed the full-aperture per-point construction family; this
cycle (exp-080) now supplies strong, independently-reproduced evidence
against the ONE remaining construction in that same mechanism class,
closing what exp-079's own ranking called "the single highest-value item on
the board" — a substantive, cumulative narrowing two cycles running, even
though the underlying T28 mechanism question remains open.

---

## 5. Recommendation for Iteration 57's Combined Verdict and Iteration 58's queue

**Combined Verdict: PARTIAL**, consistent with every T28 cycle since
exp-076. State explicitly, not left implicit: (a) FORECLOSE, confirmed a
third independent way (EM's script, exp-079's own Red Team audit, and now
this audit's from-scratch re-derivation, §0 item 1); (b) INCONCLUSIVE under
the matched (unobtainium) admittance, but admittance-family-DEPENDENT —
REFUTE-adjacent (`mean R²=0.4305`, two configs negative) under the
realizable family, worst exactly at the ABSORB depth (40) where the two
families are independently known to diverge most; (c) PHOTONICS' own §4
image-term construction, though not literally built by EM or PHOTONICS
this cycle, HAS effectively been built and scored — zero new FDTD, by
QUANTUM's blind critique, using only already-gated primitives — and found
to reproduce a pathology at least as severe as, and by the shape-only floor
measure WORSE than, this cycle's own already-INCONCLUSIVE result.

**Iteration 58's queue item for "PHOTONICS' §4 build" should change from
"build it" to "gate and extend what QUANTUM already built."** My own
independent, digit-exact reproduction of QUANTUM's construction (§0 item 8)
confirms the premise the task itself poses: this is not a proposal to trust
QUANTUM's word, it is a re-derivation from the same primitives that
reaches the identical numbers. Concretely, Iteration 58 should:

1. **Formally adopt QUANTUM's `E_photonics(θ_beam)=r(90°-θ_beam;ABSORB)·
   W(θ_beam)` as the record's own canonical zero-FDTD implementation of
   PHOTONICS' §4 image term**, with fix-docket item 5 (§3) — the
   `E_direct` cancellation assumption — checked explicitly before treating
   it as final, not smuggled through unstated a second time on this
   sub-thread (after the `theta_beam`/`90-theta_beam` convention bugs
   exp-079's own record already names twice).
2. **Run the actually-decisive test this construction has never been given**:
   score its PAIR_PAD/PAIR_ABSORB40/C80-C40 deltas against the REAL T28
   reference periods via the SAME `_free_period_search`/staged-widening
   pipeline every prior y-wall model in this sub-thread has used — not
   another per-point-shape R² comparison. QUANTUM's own construction
   already computes everything this needs; the free-period fit is the one
   remaining step, and it is the metric that actually bears on Checkpoint
   criterion 2 (§4 above), which this audit's own per-point-shape evidence
   alone cannot settle.
3. **Pair it with the real 750/450nm wavelength-generality leg** (deferred
   4+ consecutive T28 cycles per exp-079's own Tier-1 ranking) — not
   redundant with the shape-only finding above, since `λ` enters both
   `d_F=W²/λ` and the reflection-coefficient phase directly, so a construction
   whose primary failure mode is an amplitude-regime mismatch at 600nm may
   or may not behave the same way at a different wavelength.
4. **Weigh promoting the PAD-loaded real-article check** (exp-079's own
   Tier-2 item #10, deferred FOUR consecutive cycles, "the single most
   overdue item on the whole T28 board") more seriously than exp-079's own
   ranking did. With the LAST untested member of the coherent-echo
   mechanism class now carrying strong negative evidence at the desk level
   (this cycle), the marginal value of continuing to hunt for a
   period-matching desk mechanism, versus testing whether ANY of this
   eight-cycle sub-thread has downstream relevance to constraint 3 at all,
   has shifted further toward the latter. If Iteration 58 defers this a
   FIFTH time, the reason should be stated with this cycle's own finding
   explicitly weighed against it, not by inertia.

None of the above re-opens or re-proposes any RULED-OUT item (R1-R9); the
plane-wave/global-steering construction is narrowed, not foreclosed outright
— Checkpoint criterion 2 remains formally NOT YET RIPE (§4) pending item 2
above, the one test that would actually settle it.
