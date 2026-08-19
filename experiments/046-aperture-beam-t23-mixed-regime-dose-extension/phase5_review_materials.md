# PHASE 5 — REVIEW · Panel Iteration 23 · Seat: MATERIALS & METAMATERIALS

*Fresh-context review, blind to the other six seats' current-cycle Phase-5
output. Charter: sub-wavelength structure and realizability — published /
plausible / unobtainium-with-parameters. Read: PANEL.md, LOGBOOK.md in full
(RULED OUT, ESTABLISHED, T1–T23), `phase1_proposal.md`, all five
`phase2_critique_*.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `REALIZABILITY_MEMO.md` (Amendments 1–5), `results.json`
(summary statistics only, no bulk dump), `experiments/038-.../run.py`
(realizability_tier), `lab/thermo_sidecar.py`. This cycle proposes no
mechanism (T1 escape route: NONE) — it is instrument/model-fidelity
characterization plus realizability bookkeeping, so this review is scored
almost entirely on Blocks B and C and the memo, not Block A's optics.*

---

## Reading — the five assigned verification questions, checked directly

**1. Was `REALIZABILITY_MEMO.md` actually amended this cycle, or is this
another Iteration-21-style claimed-not-delivered instance?**
Checked the file directly (`experiments/034-floor-convergence-scale-bridge/
REALIZABILITY_MEMO.md`) and the git history. **Amendment 5 is real and
present in the live file**, landed in commit `460f018` ("exp-046 Phase 4
(part 2/2): results"), the same commit that generated `results.json` —
`git show 460f018 -- .../REALIZABILITY_MEMO.md` shows the full added text
(the "AMENDMENT 5 (Iteration 23, exp-046 Phase 4...)" block, two entries:
(a) the memory-axis dimensionless-dwell closed form, (b) the silicon
provenance downgrade). Unlike Iteration 21 (exp-044), where Phase 5 caught
the memo file sitting untouched despite the experiment's own naming
claiming delivery, this cycle's delivery checks out on the actual file, not
just on `results.json`'s or `NOTES.md`'s say-so. Amendments 1–4 are
preserved verbatim above Amendment 5, appended not overwritten, as
`phase2_redteam_audit.md` item 22 required.

**2. Is the silicon-identity relabeling to "ASSUMED — provenance terminates
unsourced" actually applied everywhere?**
Yes, checked in all three required loci:
- `results.json`: all three `block_b_mixed_length_scale_regime.regimes.*
  .material_identity.provenance` entries (`w_on_consistent`,
  `r_out_consistent`, `mixed_w_power_r_cond`) read
  `"ASSUMED -- provenance terminates unsourced (T18)"`, each carrying a full
  `provenance_trace` string that names the exact dead end (`exp-037/
  NOTES.md:828-829` reads "standard *cited* thermal constants," and a grep
  over `experiments/037-*` for DOI/Handbook/CRC/2330/148 returns only that
  sentence).
- `NOTES.md` idealization 6 states the identical relabeling and the
  identical provenance trace.
- `REALIZABILITY_MEMO.md` Amendment 5(b) states it a third time, in the
  memo itself, not just in the experiment record — which is the locus that
  actually matters for future cycles, since Amendment 2's realizability
  table is what gets read cold.

No locus still calls the identity "sourced." This is a genuine, non-
cosmetic downgrade, correctly propagated — and it traces to a real defect
Phase 2 (MATERIALS' own blind critique, M3) caught independently this same
cycle: exp-037's own line 828-829 says "standard *cited*" and cites nothing,
so every downstream document (exp-045, and exp-046's own Phase-1 draft)
that called it "sourced" was propagating a self-reference, not a citation.
This is a smaller, cleaner version of Iteration 22's fabricated-PMMA defect
— wrong label on correct numbers, not wrong numbers — and it was caught and
fixed in the same cycle it was introduced into this document's own §2.3,
which is the system working as intended.

**3. Does the extended grid (21 new points, Host E + ratio=1.0) actually
close Red Team's Attack 9 "zero unobtainium-tier points" gap?**
Checked `experiments/038-t17-rate-equation-kernel/run.py:39-46` directly:

```
def realizability_tier(host, r):
    if host == "E":
        return "UNOBTANIUM-WITH-PARAMETERS"
    if r >= 1.0:
        return "UNOBTANIUM-WITH-PARAMETERS"
    if r <= 1e-3:
        return "PUBLISHED" if host in ("A", "B") else "PLAUSIBLE"
    return "PLAUSIBLE"
```

UNOBTANIUM-tier is exactly: Host E (any ratio), or ratio = 1.0 (any host).
exp-045's own Block C grid (Host D, 4 ratios ∈ {1e-9,1e-5,1e-3,1e-1}) never
touched either condition — Attack 9's complaint was structurally correct,
not a nitpick. I recomputed `results.json`'s
`block_c_dose_accumulation_full_grid.points` directly (42 point-runs, 21
new host/ratio combos × 2 gaps) and confirmed: **12 of the 42 point-runs
land at UNOBTANIUM-tier** (Host D r=1.0 ×2 gaps, Host E × 5 ratios × 2
gaps), and it is exactly this UNOBTANIUM subset that produces the cycle's
only nonzero memory readings. The gap is closed, not just gestured at —
the code that decides "was this cell actually tested at the tier the claim
is about" and the code that reports the memory ratio are the same 21-point
grid, and I re-derived the point count (25-point full grid − Host D's 4
exp-045-committed points = 21) independently rather than trusting Phase 3's
own hand-count, which the record itself flags as corrected once already
(Red Team's docket text originally said "+18," Phase 3's own note walks
through why the real number is 21 and defers to the code — I confirm the
code's own printed `n_new_points` is 21, matching Phase 3's corrected
count, not Red Team's original 18).

**4. Does the reported finding (memory only at Host D/ratio=1.0 and Host E;
zero at published-tier) actually corroborate `REALIZABILITY_MEMO.md`'s
existing Amendment 3?**
Recomputed from `results.json` directly rather than trusting NOTES.md's
prose count. Extracting `periodic_over_first_ratio` from the
`mixed_w_power_r_cond_T23_PRIMARY` regime at all 42 point-runs: **exactly 7
exceed 1.05**, and every one of the 7 is at Host D r=1.0/0.5τ-gap or Host E
(any ratio)/0.5τ-gap, plus Host E r=1.0/5τ-gap. **Zero of the 12 PUBLISHED-
tier point-runs (Hosts A/B, r≤1e-3) show any memory at all** — I confirmed
`|ratio−1| = 0.0` exactly (not merely small) at all 30 negative-control
point-runs, matching NOTES.md's own claim and the closed form's own
prediction that PUBLISHED hosts sit `D/τ_k ≥ 66.7`, a factor 26 past the
`D/τ_k < ln(21f) ≈ 2.54` onset threshold. This is a real, independently
reproducible corroboration of Amendment 3's original (Iteration 15)
finding, now with a mechanism attached (the closed-form dimensionless-dwell
criterion, C2/Amendment 5(a)) rather than resting on "these happen to be
the two least-realizable hosts." I consider this the cycle's most solid
result from my own charter's angle: Amendment 3 was originally tempered by
Red Team as "substantially a near-mechanical consequence" of one fixed
pulse duration; this cycle's C2/C3 (250-point duration scan, agreeing with
the closed form at 250/250) converts that tempering into an actual proof —
the memory axis is not a host-list property at all, it is one dimensionless
number against one threshold. That is a genuine strengthening of the memo,
not a restatement.

**5. Does the fill-factor idealization disclosure correctly state the
physics?**
This is where I have a finding the write-up does not fully cover. Checked
`lab/thermo_sidecar.py` directly:

- `netd_disposition(delta_t_k, netd_band_k, fill_factor=1.0,
  emissivity_correction=1.0)` (`:187-220`) computes
  `effective_dt = delta_t_k * fill_factor * emissivity_correction` — a
  **post-hoc multiplier applied after `delta_t_k` is already computed**,
  not a change to the physics that produced `delta_t_k`.
- `mass_kg` (used inside `transient_delta_T`/`τ_thermal`, computed upstream
  in `run.py`) is `ρ_Si · L³` at full bulk density — unaffected by
  `fill_factor`, which both exp-045 and exp-046 leave at 1.0 in every call.

NOTES.md idealization 7 and `results.json`'s
`fill_factor_disclosure.note` state: a dilute host "lowers the effective
ΔT (making UNDETECTABLE more conservative) but also lowers τ_thermal —
both sides disclosed together." I verified this is **internally
consistent and correctly signed for the two effects it names**: if a
future cycle actually applied `fill_factor` to `mass_kg` (mass ∝
fill_factor for a genuinely dilute host), τ_thermal ∝ fill_factor too
(confirmed by the cited 10%-fill sensitivity row: `dwell/τ_thermal` = 1942×
= 194.18×/0.1, exactly the scaling `τ_thermal = ρC_P L²/(4εσT³L+k_air)`
predicts), which makes `dwell/τ_thermal` **larger**, not smaller — i.e.
MORE comfortably past `N_TRANSIENT_TAU=25`, not less. So on the two axes
this idealization names, dilution is conservative in both directions, as
claimed.

**But the disclosure is incomplete on an axis it does not name, and that
axis is already on the record elsewhere in this program.**
`steady_state_delta_T`'s own docstring (`lab/thermo_sidecar.py:151-153`)
states: *"Graybody radiative-equilibrium is itself a questioned
idealization for a dilute vapor/aerosol host (Red Team's exp-033 attack
11) — carried forward unresolved, not fixed by this module."* I confirmed
this citation is real: `experiments/033-g600-resolution-check/results.json`
`on_endpoint_lwir_claim` records Red Team's own exp-033 finding that
"MATERIALS restricts `off_pass`'s realizable host to dilute vapour/aerosol,
where graybody radiative-equilibrium is the wrong model" — a THIRD
consequence of host dilution, on top of the two exp-046 discloses. If a
dilute vapor/aerosol radiates less effectively as a graybody than the fixed
`emissivity=0.9` this module assumes (a physically reasonable expectation —
fewer molecules per unit path length coupling to the far-field radiation
field, compared to a continuous solid surface), then `dP/dT = area·(4ε
σT³+h_conv)` is **smaller** than modeled, and `dt_ss_full = P_abs/(dP/dT)`
is correspondingly **larger** than modeled — the opposite sign from the
two effects NOTES.md's idealization 7 discloses. This is exactly the "cut
the other way" case the review question anticipates, and it is not a
speculative worry invented for this review: it is a standing, named,
unresolved Red Team attack from Iteration 10 that this cycle's own module
docstring still flags as unfixed, and which idealization 7's own "both
sides disclosed together" framing does not connect to or mention. Given
the current margins (607× at the mixed regime, 1839×/5558× at the other
two), a modest emissivity reduction would not flip any UNDETECTABLE
verdict on its own — but the disclosure as written reads as if dilution is
uniformly conservative, and a third, undisclosed-here consequence of the
same idealization is not.

---

## Physical meaning

Nothing in this cycle changes what real material could realize the target
phenomenon. Block A is illumination-model/propagator characterization
(PHOTONICS'/ELECTROMAGNETISM's charter, not mine) and touches no
realizability bound — I independently confirmed this via the same argument
Phase 2's MATERIALS critique made: `beam_divergence_incoherent`/`_coherent`
exist only in exp-042 (Iteration 19), built after every D_req figure in the
memo, so no D_req/irradiance number in `REALIZABILITY_MEMO.md` could ever
have depended on that machinery. Blocks B and C are pure bookkeeping on an
already-UNDETECTABLE thermal signature and an already-negligible memory
effect — neither block was ever going to move a tier, and neither did.

What the cycle actually accomplishes, from this charter's angle, is
epistemic hygiene: (a) the memo's own provenance standard is now honestly
applied to a citation that was quietly circular; (b) a previously
untestable realizability claim (Amendment 3's "memory only at the least-
realizable hosts") now has a mechanism instead of a coincidence-shaped
correlation, closing a loose end Red Team itself flagged as suspicious at
Iteration 15/16; (c) the specific gap Red Team's Attack 9 named (a
positive-control grid that structurally could not contain a positive
UNOBTANIUM-tier reading) is closed with real data, not a promise. All
three of those are real, checkable improvements to the standing
realizability record, independent of whether any constraint-3/4 verdict
ever moves.

## Argued next change

**Extend the fill-factor idealization's own disclosure to the emissivity/
graybody coupling exp-033's Attack 11 already named**, rather than treating
`fill_factor` as a clean, uniformly-conservative multiplier. Concretely:
add a `emissivity_correction < 1` sensitivity row beside the existing
`fill_factor`/ρC_P row (the machinery for this already exists —
`netd_disposition`'s own second parameter, `emissivity_correction`, is
declared and unused in every call this program has made) and state
explicitly whether, at the margins this cycle reports (607×–5558× below
NETD), a physically plausible emissivity reduction for a dilute host could
close enough of that margin to matter. My own back-of-envelope: even
`emissivity_correction = 0.1` (a severe, probably-too-generous-to-the-
worry reduction) only inflates `dt_ss_full` by up to ~4× at the mixed
regime (dominated by `h_conv`, not the radiative term, since Bi≪1 already
means conduction dominates over radiation for this geometry) — comfortably
short of threatening 607×. Stated but not computed by this cycle; the
computation is one line and removes a standing "carried forward
unresolved" flag that has now sat in the module's own docstring since
Iteration 10 (exp-033) without a single cycle actually bounding it.

## Ranked top-3 directions for Iteration 24 (this seat's own ranking)

1. **Bound the graybody/emissivity coupling for a dilute host**, per the
   argued next change above — zero-cost, closes a five-iteration-standing
   Red Team flag (exp-033 Attack 11), and is the one loose thread this
   cycle's own fill-factor disclosure left unconnected despite citing the
   same module section that names it.
2. **VISION's glare/adaptation Tier-W sidecar**, per the hardened
   unconditional rule this cycle's own Phase 3 restated (Checkpoint
   criterion 4 fires automatically if Iteration 24 closes without it) — not
   this seat's charter, but the highest-severity standing item in the
   record, and I confirm the rule as re-stated in `phase3_synthesis.md`
   matches the Iteration-22 aperture-check precedent it claims to mirror.
3. **A rigorous (not WebSearch-snippet) primary-source check on the
   silicon thermal-constant identity now labeled ASSUMED**, closing the
   provenance gap this cycle correctly diagnosed but could not fix (T18's
   WebFetch block is now an 11-consecutive-shift-confirmed standing
   condition, unrelated to this specific gap but the reason it can't close
   itself). Low priority only because the values are independently
   plausible for bulk crystalline Si and no verdict rests on the third
   decimal place — but it is the last unresourced citation this program's
   own thermal chain depends on.

## Verdict

**PROMISING**, from this seat's charter specifically. Every claim this
review was tasked to verify checked out under direct inspection of the
live files (not just the write-up's own prose): the memo was actually
amended, the relabeling is applied everywhere it needs to be, the extended
grid genuinely closes the positive-control gap Red Team named and produces
a result in exactly the cell predicted, and that result is a real
strengthening (not a restatement) of Amendment 3. The one finding I add
beyond what NOTES.md/the memo already disclose — the fill-factor
idealization is directionally correct but incomplete, silent on a
same-module, already-on-the-record emissivity/graybody concern — does not
threaten any verdict at current margins and is a one-line fix, not a
defect in this cycle's arithmetic. No realizability tier moved, none was
claimed to, and nothing in Block A (outside this charter) touches the
memo's own D_req/irradiance bookkeeping, confirmed independently rather
than taken on the proposal's word.
