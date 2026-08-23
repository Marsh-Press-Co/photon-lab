# exp-064 — Phase 2 Critique (MATERIALS & METAMATERIALS, blind)

## Steel-man (≤150 words)

The allow-list shape is correct. `bench_construction` and
`measured_geometric` map exactly onto the two length origins this seat's
charter cares about — a length built directly into the simulated solid
vs. a length independently measured on a real physical sample — and §7's
argument for an allow-list over a deny-list is physically sound, not
borrowed: extinction cross-section generically diverges from geometric
cross-section for any sub-wavelength or resonant scatterer (the optical
theorem ties σ_ext to a coherent forward-scattering amplitude, not a ray
quantity), so T23's own history of one bad length after another (`w_on`,
then `L=τ_true/α`) will keep recurring under a deny-list. A required,
keyword-only, no-default parameter plus a raise-on-mismatch identity gate
is the right enforcement shape — unlike the docstring rule it replaces,
it cannot be silently forgotten. QP-2/QP-3's split (retag committed bench
calls cleanly; retag witness calls diagnostic-only rather than falsely
licensing them) is the honest way to close T23.

## Sharpest attack (≤150 words)

§6's headline — a "genuinely new" 24×–75× gap between a real forest's
"~14 µm" height and the 331–1051 µm witness need — is not new evidence
and appears to contradict this program's OWN already-established record
this same proposal cites for the 331–1051 µm figure: exp-061's MP-2
(CONFIRMED) sourced three independently corroborated real CNT-forest/
Vantablack thicknesses at the *hundreds-of-µm scale itself* — ResearchGate
300–500 µm, Surrey NanoSystems VBx2 datasheet 100–300 µm, S-VIS ~250 µm —
and MP-5's own table already ran exactly this comparison (verdict:
PARTIAL, "magnitude undershot," real thickness short by roughly 1×–10×
depending on which α anchor, not 24×–75×). The unsourced "up to 14
micrometers" figure — the only length in this document with no named
citation, unlike every MP-2 row — most plausibly reflects the `<20µm,
mid-IR` outlier MP-2 itself already flagged and excluded from the
record-blackness comparison class. Filing this as a fresh gap risks
seeding LOGBOOK.md with a materially wrong realizability number; it needs
reconciliation against MP-2/MP-5, not queuing as new.

## Verdict: **support-with-changes**

The `length_provenance` guard architecture (§§3–4) is sound and should
ship — it is the right, permanent fix for T23, and QP-1/QP-2/QP-3/QP-4
are well-designed falsification tests. But §6 must not close this cycle
as written. Concretely:

1. **§6 needs correction, not queuing.** Before Phase 3, cross-check the
   "~14 µm" claim against `REALIZABILITY_MEMO.md` Entry 2 Amendment 6 /
   exp-061 MP-2, which this same document already relies on for its own
   331–1051 µm figure. If reconciliation confirms MP-2's 100–500 µm
   figures are the right comparator (they are — they are sourced,
   corroborated three ways, and already scored via MP-5), §6's own
   "24×–75×, no query surfaced a directly-measured height at this scale"
   language is false as written and must be struck or rewritten to match
   the already-CONFIRMED ~1×–10× gap. Do not carry an uncorrected,
   unsourced "14 µm" figure into LOGBOOK.md's persistent memory as a
   "genuinely new" finding — this program has a standing rule (R4) against
   exactly this failure mode (a plausible-looking number that was never
   checked against the record before being cited as new).
2. **Allow-list coverage, a secondary but real gap**: `measured_geometric`
   conflates "directly measured" with "measured on the SAME candidate
   material/process class the rest of the sidecar call already assumes."
   It would happily license a `measured_geometric` length pulled from an
   unrelated geometry class (densified/drawn-sheet CNT vs. as-grown
   bulk-aggregate forest — exactly the two classes exp-063 itself kept
   separate) sitting alongside a `bench_construction` or diagnostic length
   from a different class entirely, with no cross-check. This is smaller
   than item 1 and correctly named in the proposal's own Idealization 2
   as future scope, not a blocker — but it means the guard enforces
   *declaration provenance*, not *material-identity coherence*; a future
   `numeric_lint.py`-style cross-check on provenance-tagged calls sharing
   one nominal material identity is the natural next step, not this
   cycle's job.

## Parameter change that would flip the verdict to plain support

Correct §6 before Phase 3 lands: either (a) reconcile the "~14 µm" figure
explicitly against MP-2/MP-5's own 100–500 µm sourced range and rewrite
the finding to the correct, already-established ~1×–10× (not 24×–75×)
gap, disclosing it as a restatement of an existing PARTIAL finding, not a
new one; or (b) strike §6 entirely and let the standing #3 queue item
(pin record-blackness pitch/diameter + κ together) carry the thickness
question forward undisturbed. Either fix leaves the `length_provenance`
guard itself — this cycle's actual deliverable — unchanged and fully
supported.
