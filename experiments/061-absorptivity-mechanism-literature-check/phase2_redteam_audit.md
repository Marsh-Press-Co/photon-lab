# Phase 2 — RED TEAM audit (exp-061 / Iteration 38)

*Fresh sub-agent, receives everything: the Phase-1 proposal and all five
blind Phase-2 critiques. Never leads. Standard: not textbook-physics
compliance — kills internal inconsistency, unfalsifiable claims,
mechanisms that cannot be expressed as simulation parameters, and
proposals that quietly violate a target constraint (especially #3).*

Verified directly (not taking any seat's word for it): ran
`caveat_lint.py` and `--selftest` (both PASS, 0 required-site failures,
exit 0 — matches all five seats' claims); ran `design_geometry.py`
(confirms `tau_shell=24.0`, `alpha=0.016667/nm`, `e-fold length=60.00nm`);
read `materials.py::graded_black_shell`/`uniform_lossy_shell` and the
exp-060 `sigma_flat`-derivation section directly; hand-derived a τ figure
none of the five seats produced (§2, below).

---

## 1. Numbered attacks (independent)

**1. [inconsistency]** `TAU_SHELL=24` is `sigma_max_fixedabs(r) *
thickness = 0.5 * 48` — a **peak-conductivity × full-thickness**
product. `graded_black_shell` (materials.py:74–100) codes σ(r) as a
quintic-smoothstep ramp from 0 at r_in to σ_max at r_out; the profile's
own raw line-integral, for the *identical* object (r_in=30, r_out=78,
σ_max=0.5), is `9.402597` (exp-060 NOTES.md, `sigma_flat*(r_out-r_in)`) —
**2.552×** smaller. Independently reproduced; a factual mismatch inside
the program's own record between two numbers describing the same object,
not a matter of opinion.

**2. [inconsistency]** Even 9.4026 is not the physically correct anchor,
and I can show *how much* it's off, for free. exp-060 already computed,
for this exact shell, `∫₀¹ Im(n(σ_graded(d))) dd = 0.273840` (NOTES.md)
via the Red-Team-corrected loss-tangent bridge `t = σ·cpl/(2π)`. Using
that already-published, already-gated number:

`τ_true = 2·(2π/cpl)·(r_out−r_in)·0.273840 = 2·0.31416·48·0.273840 ≈ 8.26`

This costs **zero new FDTD, zero new network calls** — pure arithmetic on
a number already sitting in the record. Neither PHOTONICS' fix (9.40)
nor the current text (24) is this value. Three unreconciled candidate
anchors (24 / 9.40 / 8.26) currently coexist in the program with no
single one designated the truth. Adjudicated in §2 below.

**3. [unfalsifiable-adjacent]** MP-4's dual-condition falsification (α
AND thickness both within ~2× of the target) never states, anywhere in
Section 3, which axis is expected to dominate. Computed both: MP-2
(thickness, 15–150µm predicted vs. 1.44µm built) is **unaffected by any
τ_shell correction** — a completely separate figure. MP-1 (α) is
anchor-sensitive: the gap to the predicted band swings from ~5.6–167×
(τ=24) to ~2.2–65× (τ=9.40) to a narrower-still range at τ_true≈8.26. As
written, a Phase-4 grader cannot tell from the text which condition is
the hard constraint (thickness) and which is soft (α) — a real design gap
in the falsification structure, not just a numeric slip.

**4. [constraint-#3-violation, latent]** MP-5's own table row ("YES,
PLAUSIBLE at ~15–100× the thickness") does not repeat "T1 escape route:
NONE / zero constraint-1/2/3/4 metric scored this cycle" inline — that
disclaimer lives only at the document's top. A future cycle citing MP-5's
row in isolation (exactly how `graded_black_shell` citations have
propagated before, per the registered `exp052-alpha-60nm` caveat's own
trigger-term list) could read "PLAUSIBLE" as live progress toward
constraint 3 rather than a pure thickness/absorptivity realizability
note. EM's general point, located here to the specific defect site
(MP-5's row itself, not the document generally).

**5. [inexpressible, conditional]** QUANTUM's flip condition (one added
sentence disclosing that "effective α" pools bulk/diffuse/coherent-
coupling origins) is necessary but doesn't by itself resolve what happens
to MP-4 if Phase 4 returns *only* coherence/localization-framed sources —
the proposal has no stated fallback for "the comparison turns out to not
even be the right shape." A sentence disclosing risk without
pre-registering the fallback path leaves this a live unfalsifiability
risk, not yet an actual one (Item A hasn't run).

**6. [inconsistency, minor]** Item B's self-test summary reads
"CONFIRMED, exactly as predicted... a genuine retroactive test against
real history" — accurate but stated with more generality than
Idealization 7 (two paragraphs later) discloses: exactly one phrase, one
file, two revisions. Confidence-language outrunning disclosed scope is a
small instance of the exact over-claiming pattern this tool exists to
prevent. Tighten the summary line to name the single-case scope inline.

**7. [unfalsifiable]** MP-3's table row ("NOT FOUND — predicted null
result") doesn't itself say "not found via WebSearch-snippet search" —
that scoping lives only in the separate T18 paragraph, not attached to
MP-3's own cell. Same structural defect as VISION's finding, applied to a
different row (MP-3 rather than MP-4/Section-3-generally). A "NOT FOUND"
that isn't textually scoped to its evidentiary tier reads as stronger
than it is.

---

## 2. Adjudicating PHOTONICS vs. EM

**Ruling: neither seat's proposed anchor is what Phase 3 should commit.
Use τ_true ≈ 8.26** (attack #2 above), computed from exp-060's own
already-published `Im(n)` integral at zero marginal cost — better than
PHOTONICS' cheaper fix, but short of EM's full-derivation demand.

Reasoning:
- EM is right that 9.4026 is a raw-σ line-integral, not a physical α — it
  ignores that `Im(n)` is concave in σ (the same Jensen's-inequality
  effect exp-060 already measured and gated at ~8.3% for its own
  flat-vs-graded comparison). But EM's demand for a fresh full derivation
  overstates the marginal cost: the specific number needed
  (`∫₀¹ Im(n(σ_graded(d))) dd = 0.273840`) for *this exact shell* already
  exists in exp-060's NOTES.md, already Red-Team-corrected for the
  `sim.omega` bug, already cross-validated by QUANTUM and Red Team
  independently. Converting it to τ_true is arithmetic, not a new
  derivation.
- PHOTONICS is right that 24 is wrong and self-inconsistent, but
  under-corrects: 9.40 still uses raw σ, not `Im(n)`.
- **Does it change MP-4's qualitative verdict?** No, and this is the
  decisive point for scoping how much rigor Phase 3 owes here. MP-2
  (thickness: 15–150µm predicted vs. 1.44µm built, a 10–100× gap) is
  **untouched by any τ_shell correction** — a structurally separate
  figure about real CNT-forest heights. Since MP-4 requires BOTH
  conditions within ~2× simultaneously, and the thickness axis is unmoved
  regardless of whether α is anchored at 24, 9.40, or 8.26, the
  UNOBTANIUM-WITH-PARAMETERS verdict is overdetermined by MP-2, not
  decided by which τ figure MP-1 uses. This confirms EM's own hedge
  ("plausibly enough to matter against MP-1's band, but not obviously
  enough to flip MP-4") — and this calculation shows precisely why: the
  α axis is the soft, anchor-sensitive one; the thickness axis is the
  hard, anchor-invariant one.
- **This is a realizability-bound cycle, not a load-bearing physics
  claim** (stated explicitly in the proposal, T1 escape route: NONE). The
  correct standard is "use the best number already sitting in the record
  for free, disclose its remaining idealizations, don't spend new
  FDTD/network budget refining an axis that isn't the deciding one."

**Verdict: Phase 3 uses τ_true≈8.26 as MP-1's anchor (not 24, not 9.40),
disclosed as a 1D/d-linear WKB approximation (not area-weighted — a real
but non-gating residual idealization), with MP-2 stated explicitly as the
dominant/robust falsification axis this correction does not touch.** No
new FDTD run is required before Phase 4.

---

## 3. Ruling on VISION's finding (T18-propagation self-miss)

**PROCEED-WITH-MANDATORY-FIXES material. Does NOT itself fire Checkpoint
criterion 4 this cycle** — but the margin is thin and a forward tripwire
is set below.

Reasoning: the hardened "no further deliberation required" auto-fire
(established at Iteration 37) targets a specific defect shape — **a
Phase-3/Phase-5 docket names required propagation sites, and hand-review
misses one anyway** (Iterations 35→36→37, three consecutive). VISION's
finding this cycle is a different species: the T18 evidentiary-tier
disclosure was **never registered as a propagation-tracked caveat at
all** — there is no docket item it broke. This is precisely the tool's
own self-disclosed Idealization 6 ("cannot catch a caveat that was never
registered") firing in real time, which is genuinely notable and worth
flagging hard, but it is not a broken promise — it's an un-made one,
caught during Phase 2 of the same cycle, before Phase 3 freezes anything
to git. That combination (different defect species + self-caught +
pre-freeze) keeps it below the auto-fire bar.

**Forward tripwire (binding on future cycles):** if a "never-registered
caveat" gap of this shape is found again at a *future* cycle, and it's
discovered *after* Phase 3 has already frozen predictions — i.e., after
this cycle's own T18 registry-entry fix (docket item below) — that
recurrence breaks an actual promise this cycle makes, and should
auto-fire criterion 4 under the same no-further-deliberation logic as the
propagation tripwire. This cycle gets one pass because it's registering
its own gap; a second miss of this exact shape would not.

---

## 4. Ruling on THERMODYNAMICS' demand

**Accept, in a stronger form than THERMO's own flip condition offers.**
THERMO's stated flip-to-support-only condition ("MP-4 pre-committed to
gate strictly on the FALSE branch — no live design candidate survives
Phase 4 under ANY outcome") will essentially never trigger: MP-5's own
fallback ("PLAUSIBLE at 15–100× thickness") keeps `graded_black_shell`
alive as a design candidate under nearly every realistic Phase-4 outcome
short of a clean, sourced MP-3 hit. THERMO's own escape clause is
therefore close to vacuous as written. **Rule instead: the Phase-3 THERMO
disposition box is mandatory outright**, not conditional — desk-only,
`thermo_sidecar.py` calls, bounding P_abs/ΔT/Wien-peak for the MP-1/MP-2
predicted-band worst case using exp-034/057's witness-irradiance
parameters, labeled post-run analytic per the expressibility contract.
Cheap (THERMO itself scopes it as desk-only) and closes a now
third-occurrence omission shape in THERMO's own lane.

---

## 5. Ruling on QUANTUM's demand

**Accept as stated, folded into docket item 3 below**, with one addition:
the sentence must also pre-register the fallback (attack #5 above) —
what MP-4 becomes if Phase 4's sources come back framed in
coherence/localization terms rather than a reflectance-vs-thickness curve
at all (a scope caveat on MP-4, not silent pooling, not silent
abandonment either).

---

## 6. Ruling on the missing registry entries

- **MANDATORY this iteration:**
  - QUANTUM's corrected-bias-direction entry — a real, previously-
    reversed sign with no current protection against silent
    reintroduction; cheap to add.
  - VISION's T18-propagation entry (§3) — must land before Phase 3
    freezes, per VISION's own flip condition.
- **DEFERRED/queued, not blocking Phase 3:**
  - EM's `sim.omega` historical units-bug entry — real, but the fix
    (`t=σ·cpl/(2π)`) is now the *only* loss-tangent formula anywhere in
    the program (verified by direct read); no live reintroduction vector
    exists today. Queue for whenever this code path is next touched.
  - THERMO's T25 sidecar-absence entry — real, lower urgency than the two
    above (a citation-discipline caveat, not a numeric-correctness one).
    Queue for Iteration 39.
  - PHOTONICS' numeric-value-consistency-check gap in the tool's own
    design (checks phrase presence, not that a cited *number* — like
    `tau_shell`'s value — stays consistent across sibling files, the
    exact gap that let attack #1 exist undetected). Real, demonstrated
    live, but new tool machinery, not a one-line registry entry — queue
    explicitly as an Iteration 39+ tooling proposal so it isn't lost to
    the same "un-registered gap" failure mode §3 just described.

---

## 7. Final ruling: PROCEED-WITH-MANDATORY-FIXES

Numbered mandatory-fix docket (Director applies before Phase 3 freezes
predictions to git):

1. Replace `TAU_SHELL=24` as Item A's comparator anchor with `τ_true ≈
   8.26` (Red Team's derivation, §2 — independently re-verify the
   arithmetic, don't hand-copy). Restate α, e-fold length, MP-1/MP-4/MP-5
   against it. Disclose the 1D/d-linear-WKB idealization explicitly.
   State inline that MP-2 (thickness) is unaffected by this correction
   and is the dominant, anchor-invariant falsification axis.
2. Add `caveat_lint_config.json` entry for the T18 evidentiary-tier
   disclosure; `required_sites` must include `phase1_proposal.md` (or its
   Phase-3 successor) Section 3 (specifically MP-3's and MP-4's own table
   rows, not just the general search-plan/idealizations sections) and the
   eventual Phase-4 `NOTES.md`.
3. Add the classical-parameter-scoping sentence at MP-1/Idealization 3
   (QUANTUM's fix), plus one clause pre-registering the fallback if
   Phase-4 sources are coherence/localization-framed rather than
   reflectance-vs-thickness-shaped.
4. Add the mandatory (not conditional) Phase-3 THERMO disposition box:
   desk-only `thermo_sidecar.py` bound on P_abs/ΔT/Wien-peak for the
   MP-1/MP-2 worst case, using exp-034/057's witness-irradiance
   parameters.
5. Add the QUANTUM corrected-bias-direction registry entry (§6).
6. State "T1 escape route: NONE / zero constraint metric scored" inline
   in MP-5's own table row, not only at the document top (attack #4).
7. Scope MP-3's table cell explicitly to "not found via WebSearch-snippet
   search" rather than relying on the separate T18 paragraph (attack #7).
8. Tighten Item B's self-test summary line to name its single-phrase/
   single-file scope inline, not only in Idealization 7 (attack #6).
9. Queue (non-blocking, named explicitly so not lost): EM's sim.omega
   historical registry entry, THERMO's T25 sidecar-absence entry, and
   PHOTONICS' numeric-value-consistency-check tooling gap — all
   Iteration 39+.

---

## 8. Checkpoint criterion 4 — explicit ruling

**Does NOT fire this cycle.** Two findings this cycle brush against it
(VISION's self-referential tool gap, §3; attack #1, a numeric
self-inconsistency in the proposal's headline figure) but neither matches
the hardened tripwire's specific shape — a docketed propagation promise
broken by hand-review. VISION's finding is a registration-scope gap,
self-disclosed by the tool's own Idealization 6, caught pre-Phase-3, in
the same shift the tool was built. Attack #1 is a numeric-derivation
error, not a caveat-propagation failure at all — a different defect class
the tool was never built to catch (per PHOTONICS' own tool-design
finding, §1/§6).

The self-referential irony is real and worth stating plainly: the cycle
whose whole point is closing a Checkpoint-4-adjacent gap produced, live,
inside its own deliverable, an instance of exactly the failure mode it
was built to prevent (an unpropagated caveat) plus a distinct numeric
inconsistency the new tool structurally cannot see. That is a notable
finding, on the nose, and it is precisely why the forward tripwire in §3
is set rather than treating this as a clean pass — but "notable and worth
a hard docket" is not the same bar as "fires the checkpoint," and
mechanically firing it here would blur the tripwire's own precedent (a
broken promise) with a first-time registration gap, weakening the
tripwire for the case it actually exists to catch.
