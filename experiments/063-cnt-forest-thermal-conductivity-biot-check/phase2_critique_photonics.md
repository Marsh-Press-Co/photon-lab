# Phase 2 — PHOTONICS blind critique (exp-063 / Panel Iteration 40)

*Fresh sub-agent, blind to the other six seats' current-cycle critiques.
Speaking only from surface interaction / absorption spectra / angular
dependence / scattering cross-sections — PANEL.md's PHOTONICS charter.*

## Steel-man (≤150 words)

The cycle correctly identifies and closes a genuine, long-flagged gap:
κ_solid has been silicon-proxied, `ASSUMED — provenance terminates
unsourced`, since Iteration 25, entering zero committed code
(`mixed_length_scale_regime` takes no κ_solid argument at all). Sourcing a
real CNT-forest through-thickness value and deriving a closed-form Biot
correction is legitimate model-fidelity work in the established T22/T23
register. The derivation is dimensionally sound, its κ_solid→∞ limit is an
honest absolute-identity gate recovering `dt_ss_full` exactly, and it
correctly separates a length-invariant term (Bi_gas, matching the
Iteration-22 Attack-6 identity) from a genuinely new length-dependent one
(Bi_rad). Applying the same worst-case correction to both the flagship's
comfortable 699× margin and exp-061's own fragile 1.35× margin, and naming
a real, checkable κ_critical≈0.0897 W/(m·K) falsification boundary before
any search runs, is honest, falsifiable, house-discipline-compliant work.

## Sharpest attack (≤150 words)

§4's geometry — power entering uniformly at the illuminated FRONT surface,
conducting the full L=l_geometric_m before any loss channel opens — reuses
l_geometric_m for a role its own source code forbids. `mixed_length_scale_
regime`'s docstring exists precisely because T22/T23 caught this program
mixing an absorption length with a geometric length once already: "mixing
lengths across the h_eff/mass/area chain is the exact historical bug this
pair of functions exists to prevent." This cycle reintroduces that
conflation on a new axis — l_geometric_m as both the radiating envelope
(licensed) and the absorption-to-loss-surface conduction path (never
licensed). It also contradicts established optics: T9's thrice-confirmed
radial ledger shows the flagship's absorption peaks near r_in and is
~zero at r_out — nothing is deposited where §4 puts it. The bench-scale
numbers survive only because Bi_gas is length-invariant and dominates;
neither §4 nor the Idealizations discloses that this cancellation, not
correct geometry, is what saves TD-3/TD-4.

## Verdict

**Support-with-changes.** The Biot arithmetic itself is sound and the
κ_solid gap it closes is real. But §4's stated absorption geometry is
optically incoherent with this program's own standing measurement of
where power actually deposits in the flagship (T9/exp-028), and the
proposal's Idealization list discloses only the loss-side worst-case
(heat lost only at a far boundary) while staying silent on the equally
load-bearing generation-side assumption (heat entering only at a near
boundary) — an incomplete disclosure for a document that is otherwise
careful to name every worst-case choice explicitly. This does not
overturn TD-4's flagship UNDETECTABLE finding (Bi_gas dominates there
regardless of L) and, if anything, a corrected generation length would
likely *shrink* Bi_rad rather than grow it — so the direction of risk to
TD-5's fragile 1.35× figure is probably safe, not endangered. But an
escalation-worthy, first-ever-DETECTABLE falsification boundary
(κ_critical≈0.0897 W/(m·K)) should not ship resting on an unexamined
geometric assumption this program has already built named machinery to
guard against.

## Checked against the ruled-out registry

No re-proposal of R1–R5 or of any refuted T1–T26 mechanism/model claim.
This cycle scores no constraint-1/2/3/4 metric (T1 escape route: N/A) and
proposes no optical mechanism at all — it is a THERMO-sidecar
model-fidelity continuation in the T22/T23/Iteration-25 register. My
attack is not a re-litigation of T9, T22, or T23 (all of which stand as
recorded); it is that §4's own new derivation, evaluated against those
already-established findings, has not reconciled with them.

## Parameter change that would flip the verdict

Add one sentence to §7 (Idealizations) disclosing that L=l_geometric_m is
reused here in a role — the absorption-to-loss-surface conduction
distance — distinct from, and never licensed by, T23's own h_eff/mass/
area convention; and note that T9's radial ledger contradicts the
front-surface-generation picture for the flagship specifically (though
not, via exp-061's own Beer-Lambert e-fold ≈174nm, for the witness-scale
MP-5 geometry, where front-loading is separately defensible on different
grounds). With that named as a second, independent worst-case
exaggeration — not silently riding on Bi_gas's own length-invariance to
escape scrutiny at bench scale — I would move to unconditional support.
