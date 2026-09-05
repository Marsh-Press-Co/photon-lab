# Phase 2 Critique — PHOTONICS (exp-112, Panel Iteration 89)

*Blind critique. Charter: surface interaction, absorption spectra, angular
dependence, scattering cross-sections — is the proposal's optical response
coherent as stated, across wavelength and angle?*

## Steel-man (≤150 words)

The `cpl` refinement is done the physically correct way for this charter's
own question: `tau_shell` (the coating's optical thickness) is verified
held exactly invariant (24.0 at both `cpl`), and the total simulated
optical-period count is verified identical (`320·S` at both `cpl=20` and
`cpl=25`) — so the disk's effective absorption/attenuation behavior and the
transient/settling physics are not silently altered by the very refinement
meant to test whether an *angular* feature is real. `n_bins=48` binning is
a fixed angular partition (`np.linspace(-180,180,49)`, verified by reading
`sections.py`) independent of box cell-count, so the named bin's index and
its physical angle (−146.25°) are guaranteed identical at both resolutions
by construction, not by luck — a genuine, coherent apples-to-apples
angular comparison, which is exactly what this charter demands before any
"survives/collapses" verdict on a scattering-pattern feature is trusted.

## Sharpest attack (≤150 words)

Both falsification checks (`classify_resolution_check`, `run.py`) score
the named bin in total angular isolation — `local_snr`/`delta` at index 4
alone, never its neighbors. But a genuine deterministic sub-wavelength
field feature at a near-field box (margin=32, ~1.6λ from the disk) has a
physical correlation length set by λ/box-scale, so it must imprint
correlated structure across *several* adjacent bins, not one; uncorrelated
Yee-grid staircase noise, by construction, need not. The full 48-bin
`peccored`/`hollow`/`delta` arrays already exist at both `cpl=20`
(`exp-110/results.json`) and `cpl=25` (this cycle's own `analyze.py`
output) — a bin-neighborhood cross-correlation check costs zero additional
FDTD and is the one test that would actually distinguish "real angular
structure" from "isolated noise spike" on this charter's own terms. It is
never computed or scored anywhere in `run.py`/`analyze.py`; the proposal's
verdict rests entirely on a single point compared to its own past self at
one other resolution, blind to the angular context the mechanism claim
(§1: "sub-wavelength field structure") itself requires to be coherent.

## Verdict

**support-with-changes**

## Parameter change that would flip verdict

Add a zero-FDTD, pre-registered third check: compute the bin-index
cross-correlation (or simple neighbor-window ratio) of the
`peccored`/`hollow` delta pattern in a ±2-bin window around index
`NAMED_BIN_IDX` between `cpl=20` and `cpl=25`; require it exceed a stated
bar (e.g. correlation ≥0.5) before Check A's SURVIVES reading is reported
as "candidate real structure" rather than merely "not yet ruled out."
Without this, I'd move to oppose only if Check A reports SURVIVES and that
reading is then carried into any future document's prose as evidence of
genuine physics — as an instrument-fidelity check alone, scoped exactly as
disclosed, support-with-changes stands.
