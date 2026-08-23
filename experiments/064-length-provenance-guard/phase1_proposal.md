# exp-064 — Phase 1 Proposal: An Enforced `length_provenance` Guard,
# Closing T23's Witness-Scale Length-Legitimacy Question

**Panel Iteration 41. Lead: QUANTUM OPTICS, by rotation.** T1 escape route:
**N/A** — a code-architecture/instrument-trust cycle on the standing THERMO
sidecar, the exp-054/060/063 class: zero constraint-1/2/3/4 metric scored,
zero FDTD. Executes Red Team's Iteration-40 Phase-5 binding forward
commitment (`phase5_redteam_audit.md` §6/§8 item 1; `LOGBOOK.md`/`PLAN.md`
Iteration-40 "CURRENT top-of-queue" item 1): resolve T23's witness-scale
length-legitimacy question via route (a), route (b), or both, or a fourth
deferral is a program-integrity finding at Iteration 42.

---

## 0. Route chosen, stated up front

**Route (b), primary and sufficient: an enforced `length_provenance`
guard.** A bounded, disclosed diligence pass on route (a) was run first
(§6) and did not find a real, directly-measured geometric length at the
witness-scale order of magnitude this program's own MP-5 disposition
needs — consistent with this program's own prior CNT-forest geometric-
length search record. Route (b) is proposed as the decisive close: it
resolves T23 permanently and structurally (any future call, with any
future material, is protected — not just this one number), asks no
further literature luck, and matches this program's own standing
discipline of converting a recurring hand-checked caveat into permanent,
trust-suite-gated code (`caveat_lint.py`, `numeric_lint.py`, stages
16/18/23). This is honestly stated as a materials-geometry/software-
architecture fix, not a quantum-optics mechanism finding — see §7 for the
one place this seat's own discipline genuinely bears on the design.

---

## 1. Scope narrative (≤300 words)

`gas_conduction_h_eff`'s docstring states, unconditionally, that
`l_geometric` must be "a real geometric length of the conducting/
radiating SOLID body... NEVER an optical/extinction-derived length." T23
opened this question at Iteration 22 (`w_on` vs `r_out`), closed it BY
ARGUMENT at Iteration 23/31 (never by a code-level check), and the rule
has since been violated in the open: exp-063's own witness-scale
`front_surface_conduction_correction` calls (`L=τ_true/α`, MP-5's own
figure) are, on the rule's own plain text, exactly the forbidden category.
Three consecutive cycles (38, 39, 40) disclosed this in prose and deferred
it. A disclosure sentence is not a fix — nothing in the current code stops
a fourth cycle from reusing the same illegitimate length, or a future
cycle from inventing a NEW extinction-derived length and feeding it to
these functions with no disclosure at all, since nothing checks.

This proposal converts the rule from a docstring a caller must remember
into an enforced contract: every caller of `gas_conduction_h_eff`,
`lumped_cube_mass_kg`, `mixed_length_scale_regime`, and
`front_surface_conduction_correction` must declare its length's
`length_provenance`, drawn from an explicit allow-list; anything else
raises. A length whose true provenance IS extinction-derived may still be
computed, for diagnostic/bracket purposes, but only via a separate,
loudly-named `diagnostic_only=True` opt-out that is itself recorded in
the function's own return dict — never silently indistinguishable from a
licensed call. This closes T23 without waiting on a literature hit this
program's own history shows is unlikely, and it protects every future
`thermo_sidecar.py` caller from the identical mistake, not just this
one call site.

*(244 words)*

---

## 2. T1 escape route: N/A

No mechanism proposed. This is a model-fidelity/instrument-trust cycle on
`lab/thermo_sidecar.py`, the exp-054/060/063 class: zero constraint-1/2/3/4
metric scored. No new network access beyond the bounded route-(a)
diligence pass in §6 (WebSearch-snippet only; T18/WebFetch re-confirmed
blocked before that pass, 1/1 attempt, `arxiv.org` → `EGRESS_BLOCKED`,
matching every prior cycle's convention).

---

## 3. Parameter table — exact function signatures and guard logic

| Knob | Value / spec | Source / status |
|---|---|---|
| `LICENSED_LENGTH_PROVENANCE` (new module constant) | `frozenset({"bench_construction", "measured_geometric"})` | new — the only provenances a caller may declare for a length used, unflagged, in a conduction/mass/area role |
| `DIAGNOSTIC_ONLY_PROVENANCE` (new module constant) | `frozenset({"extinction_derived_diagnostic_only"})` | new — the ONLY way an extinction-derived length may enter these functions at all: explicitly named as such, and only when paired with `diagnostic_only=True` |
| `_validate_length_provenance(length_provenance, diagnostic_only)` (new private helper) | raises `ValueError` unless `length_provenance in LICENSED_LENGTH_PROVENANCE`, or (`length_provenance in DIAGNOSTIC_ONLY_PROVENANCE` and `diagnostic_only is True`) | new — single shared validator, called first thing inside all four functions below, so the check cannot be forgotten at one call site and remembered at another |
| `gas_conduction_h_eff(k_air, l_geometric, *, length_provenance, diagnostic_only=False)` | adds two required-by-position-but-keyword-only args to the existing 2-arg signature; body unchanged except the leading `_validate_length_provenance(...)` call | modifies `lab/thermo_sidecar.py:197` |
| `lumped_cube_mass_kg(density_kg_m3, l_geometric, *, length_provenance, diagnostic_only=False)` | same pattern | modifies `lab/thermo_sidecar.py:213` |
| `mixed_length_scale_regime(p_abs_w, l_geometric_m, k_air, density_kg_m3, c_p_j_kgk, emissivity, t_ambient_k=293.15, *, length_provenance, diagnostic_only=False)` | validates once, then forwards the SAME `length_provenance`/`diagnostic_only` to its own internal `gas_conduction_h_eff`/`lumped_cube_mass_kg` calls (never re-declared per sub-call — one length, one provenance, matching the module's own "mixing lengths is the historical bug" discipline); return dict gains `"length_provenance"` and `"diagnostic_only"` keys, populated verbatim (never a silent float — matches `absorbed_power_established_ratio`'s own existing convention) | modifies `lab/thermo_sidecar.py:229` |
| `front_surface_conduction_correction(k_air, l_geometric_m, k_solid, emissivity, t_ambient_k=293.15, *, length_provenance, diagnostic_only=False)` | same pattern; return dict gains `"length_provenance"`/`"diagnostic_only"` keys | modifies `lab/thermo_sidecar.py:313` |
| `biot_number(k_air, k_solid)` | **unchanged, no guard added** — takes no length argument at all (`Bi_gas=k_air/k_solid` is length-invariant, T22's own established identity); disclosed explicitly so no reviewer wonders why one of the five sibling functions is untouched | `lab/thermo_sidecar.py:294` |
| New trust-suite stage 24 | `lab/validation/run_all.py::stage24_length_provenance_guard` — 4 gate groups, ≥1 absolute-identity gate per PANEL.md's "new machinery" rule (see §4) | new |
| New `lab/caveat_lint_config.json` entry (proposed, applied at Phase 3) | `exp064-length-provenance-disclosure`: `trigger_terms` = `length_provenance`, `diagnostic_only`, `front_surface_conduction_correction`; `required_sites` = this cycle's `NOTES.md` + `phase4_results.md` | new — keeps the disclosure discipline that has protected every prior instrument cycle |

---

## 4. Guard logic — full pseudocode and the stage-24 gate design

```python
LICENSED_LENGTH_PROVENANCE = frozenset({
    "bench_construction",   # a length built directly into the FDTD/bench
                             # scene geometry (e.g. r_out = cells * dx_m) --
                             # a real, directly-specified physical dimension
                             # of the modeled solid body, not derived from
                             # any absorption/scattering measurement.
    "measured_geometric",   # a directly-measured physical dimension from a
                             # sourced primary/snippet reference (e.g. an
                             # SEM-reported forest height) -- NOT back-
                             # calculated from tau, alpha, sigma_ext, or any
                             # other optical/extinction quantity.
})
DIAGNOSTIC_ONLY_PROVENANCE = frozenset({
    "extinction_derived_diagnostic_only",  # an explicitly-acknowledged
                             # optical/extinction-derived length (e.g.
                             # L=tau_true/alpha, w_on=sigma_ext_cells*dx_m).
                             # Permitted ONLY with diagnostic_only=True --
                             # never silently treated as licensed.
})

def _validate_length_provenance(length_provenance: str,
                                 diagnostic_only: bool) -> None:
    if length_provenance in LICENSED_LENGTH_PROVENANCE:
        return
    if length_provenance in DIAGNOSTIC_ONLY_PROVENANCE and diagnostic_only:
        return
    raise ValueError(
        f"length_provenance={length_provenance!r} (diagnostic_only="
        f"{diagnostic_only}) is not licensed for a conduction-length role. "
        "l_geometric MUST be a real geometric length of the conducting/"
        "radiating SOLID body -- NEVER an optical/extinction-derived "
        "length used unflagged (T23, closed by argument at Iteration "
        "23/31, enforced in code at Iteration 41/exp-064). Licensed: "
        f"{sorted(LICENSED_LENGTH_PROVENANCE)}. Diagnostic-only (requires "
        f"diagnostic_only=True): {sorted(DIAGNOSTIC_ONLY_PROVENANCE)}.")
```

Each of the four functions calls `_validate_length_provenance(...)` as its
first statement, before any arithmetic — a caller cannot get a number out
of a mis-declared call.

**Stage 24 gate design (four groups, mirroring stage 23's own
absolute-identity + regression-anchor pattern):**

1. **Absolute identity — refusal, zero tolerance.** For all four guarded
   functions: calling with `length_provenance="extinction_derived_
   diagnostic_only"` and `diagnostic_only=False` (the default) raises
   `ValueError`, every time; calling with an unrecognized tag
   (`"bogus"`, `""`, `"w_on_extinction"`) and `diagnostic_only=False`
   also raises, every time — 4 functions × 3 forbidden-tag cases = 12
   checks, each a boolean identity (raised / did not raise), not a
   numeric tolerance. This is the gate that actually enforces the rule;
   without it, the allow-list is decoration.
2. **Regression identity — licensed calls are numerically inert.**
   Re-run every currently-committed `mixed_length_scale_regime`/
   `front_surface_conduction_correction` call site that uses a bench-
   construction length (`r_out`/`R_OUT_M`, exp-054/057/059×2/060's own
   `run.py` files, plus stage 23's own bench-scale cell in
   `run_all.py`) with `length_provenance="bench_construction"` appended
   and nothing else changed; every returned number matches its
   currently-committed value to float round-off (≤1e-12 relative). The
   guard must add zero physics change for any already-licensed caller.
3. **Diagnostic-path identity.** Calling `front_surface_conduction_
   correction(..., length_provenance="extinction_derived_diagnostic_
   only", diagnostic_only=True)` at the witness-scale MP-5 geometry
   reproduces exp-063's own committed correction-factor numbers
   bit-for-bit (the same regression anchors stage 23 gate 2 already
   checks), AND the returned dict's `"length_provenance"` /
   `"diagnostic_only"` keys read back exactly `"extinction_derived_
   diagnostic_only"` / `True` — confirming the flag travels with the
   number, not just gates the call.
4. **`inspect.signature` identity.** All four guarded functions expose a
   `length_provenance` parameter that is `Parameter.empty` (no default)
   and keyword-only — confirming the guard cannot be silently bypassed
   by a caller who simply omits the argument (a positional-default
   design, by contrast, WOULD let a legacy call keep compiling
   unguarded — this is why the parameter is required, not defaulted).

---

## 5. Falsifiable predictions — committed before any Phase-3 code lands

| # | Claim | Predicted outcome | Falsification condition |
|---|---|---|---|
| **QP-1** | `length_provenance` (required, keyword-only, no default) is added to all four guarded functions | `inspect.signature` shows the parameter present, keyword-only, `Parameter.empty` default, on all four | Falsified if any function ships with a default value for `length_provenance` (a silent bypass) or omits it from any of the four |
| **QP-2** | Every currently-committed BENCH-scale call site (exp-054/057/059×2/060 `run.py`; stage-23 bench-scale cell in `run_all.py` — 6 files, ~9 call sites) retrofits cleanly to `length_provenance="bench_construction"` with zero raise | 100% of bench-scale call sites classify as licensed on first attempt, no code-level workaround needed | Falsified if any bench-scale call site cannot be honestly tagged `bench_construction` without also changing its underlying length (would mean an EXISTING call, not just the witness-scale one, is already illegitimate — a larger finding) |
| **QP-3** | Stage 23's own 3 witness-scale (`L_MP5_730X_M`) calls in `run_all.py` CANNOT be honestly tagged `bench_construction` or `measured_geometric`; they require `extinction_derived_diagnostic_only` + `diagnostic_only=True`, or must be removed from the gated regression path entirely | Phase 3 retags these 3 calls as diagnostic-only (raising the existing prose disclosure to an enforced, machine-checkable flag) rather than silently relabeling them as licensed | Falsified — and treated as a NEW, worse program-integrity finding, not a routine implementation choice — if Phase 3 instead tags these calls `bench_construction`/`measured_geometric` (a false declaration in the type system, strictly worse than the status quo prose disclosure it would replace) |
| **QP-4** | The refusal gate (stage 24 group 1) is a true zero-tolerance absolute identity | 12/12 forbidden-tag checks raise `ValueError`, no exceptions | Falsified by any single non-raising case |
| **QP-5** | The guard changes zero already-committed physics | Every bench-scale regression number (exp-057's 699.27×/674.22× flagship margins; exp-054/059/060's own stage-18 anchors) reads bit-identical (≤1e-12 relative) before/after | Falsified by any change beyond float round-off |

---

## 6. Route (a) diligence — bounded, disclosed, not this cycle's job to
exhaust

Per the mandate's own permission ("you may run search queries now if
route (a) looks promising... do not spend excessively"), T18 (WebFetch)
was re-confirmed blocked first (1/1 attempt, `arxiv.org` →
`EGRESS_BLOCKED`, matching every prior cycle), then two WebSearch-snippet
queries were run before committing to route (b) as primary:

1. `vertically aligned carbon nanotube forest height SEM measured 500 micrometers Vantablack coating thickness`
2. `CNT forest black coating optical absorber physical thickness directly measured hundreds of micrometers not extinction derived`

**Result: a real, directly-measured geometric length WAS found, but at
the wrong scale to serve as route (a)'s answer.** General Vantablack/VACNT
literature reports actual grown forests with individual tubes "up to 14
micrometers tall" — a genuine `measured_geometric`-class length, sourced,
not back-calculated from any optical quantity. But this program's own
witness-scale need (exp-061's MP-5 disposition: 331.2–1051.2 µm, the
230×–730× multiple of the 1.44 µm bench construction) is **24×–75×
taller** than that reported real height. No query surfaced a directly-
measured as-grown CNT-forest/Vantablack-class height at the hundreds-of-
µm-to-mm scale the witness scenario needs — consistent with this
program's own prior CNT-forest geometric-length search record (Iteration
39's still-open pitch/diameter item; exp-063's own query 8 found geometry
context but no thickness figure from the pinned *Carbon* 2018 paper).

This is disclosed as a genuinely new, flagged (not scored, not resolved
this cycle) finding: **the order-of-magnitude gap between a real
Vantablack forest's typical grown height (~14 µm) and the thickness the
witness-scale beam-absorption scenario requires (331–1051 µm) is itself a
realizability question**, adjacent to but distinct from T23 — T23 asks
whether an extinction-derived length may be used for conduction; this new
observation asks whether a real forest of the REQUIRED thickness has ever
been grown at all. Queued for a future cycle (folds naturally into the
standing #3 item, pinning record-blackness pitch/diameter/κ together —
not annexed to this proposal's own scope). This finding reinforces, not
undermines, route (b) as this cycle's decisive close: it is exactly the
kind of result a further, unbounded search was unlikely to overturn this
cycle, matching the mandate's own caution against over-investing in route
(a).

---

## 7. Where QUANTUM OPTICS' own discipline genuinely bears — stated
honestly, not forced

This is, honestly, largely a materials-geometry/software-architecture
question, not a quantum-optics one — say so plainly, per the mandate.
One place this seat's own discipline is load-bearing to the DESIGN (not
the underlying materials fact): T23's forbidden examples (`w_on`,
`L=τ_true/α`) are both instances of a general phenomenon — an
extinction/absorption cross-section can differ from, and for a resonant
or sub-wavelength scatterer substantially EXCEED, the real geometric
cross-section of the object producing it (the optical theorem ties
`σ_ext` to the imaginary part of the forward-scattering amplitude, a
coherent/diffractive quantity, not a ray-geometric one; T9 already
documents this inflation numerically for this bench's own `w_on`). Because
that mismatch is a general wave-optics property, not a fact special to
`w_on` or to `τ/α` specifically, an **allow-list** (only two named-safe
provenances pass) is the physically correct enforcement shape here, not a
deny-list of today's two known-bad examples — a deny-list would leave the
guard blind to the NEXT extinction-derived length some future proposal
invents, in exactly the way T23 itself was left open for three cycles by
a prose rule nothing checked. This is the one place this proposal is
argued from QUANTUM OPTICS' own charter rather than borrowed from another
seat's ground.

---

## 8. Idealizations — stated honestly

1. **The guard enforces DECLARATION, not detection.** `_validate_length_
   provenance` cannot inspect where a float actually came from; it only
   checks the string a caller asserts. A caller could, in principle, tag
   an extinction-derived length `"measured_geometric"` and the guard
   would not catch the lie. This is a discipline/API-contract fix, not a
   physics oracle — matching this program's own established pattern
   (`caveat_lint.py`/`numeric_lint.py` are textual/registry checks, not
   semantic ones either). QP-3's falsification condition above exists
   precisely to catch the one place this cycle itself would be tempted
   to make that exact false declaration.
2. **Two licensed categories may prove too coarse or too narrow over
   time.** `bench_construction` and `measured_geometric` cover every
   currently-committed call site (QP-2) and the one witness-scale
   exception (QP-3), but a future geometry class not yet in this
   program's record might need a third category — adding one is a
   one-line change to `LICENSED_LENGTH_PROVENANCE`, not a re-architecture,
   but is explicitly out of THIS cycle's scope.
3. **`biot_number` is correctly left unguarded** (§3) — it takes no
   length argument. If a future cycle adds a length-dependent Biot
   variant, that new function inherits this guard; this proposal does not
   retroactively guard functions that do not yet exist.
4. **Route (a)'s diligence (§6) is bounded, not exhaustive** — two
   queries, not a full ten-query dispatch. A future, dedicated search
   (the standing #3 queue item, pitch/diameter+κ pinning) could still
   surface a real witness-scale geometric length; if it does, that
   length becomes a `measured_geometric`-tagged input with zero further
   code change required — route (b) does not foreclose route (a) later,
   it only stops standing on route (a) never having been resolved as an
   excuse to leave the call unguarded meanwhile.
5. **No FDTD, no new network access beyond §6's two queries.** T18
   (WebFetch) re-confirmed blocked before those queries ran (1/1 attempt,
   `arxiv.org` → `EGRESS_BLOCKED`); any FURTHER search a future cycle runs
   should re-confirm again, per every prior cycle's convention.

---

## 9. Is any FDTD needed this cycle?

**No.** This is a pure code-architecture/analytic cycle, T1 escape route
N/A, zero constraint-1/2/3/4 metric scored — the exp-054/060/061/062/063
class. Iterations 38, 39, and 40 each ran zero FDTD for the same reason;
this cycle's own Phase 4 (once Phase 3 lands the guard) is `lab/
validation/run_all.py --only <stage-24-and-siblings>`, not a solver run.
