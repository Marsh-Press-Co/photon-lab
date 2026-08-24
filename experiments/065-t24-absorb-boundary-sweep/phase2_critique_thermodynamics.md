# PHASE 2 — CRITIQUE · THERMODYNAMICS · Panel Iteration 42

*Reviewing `experiments/065-t24-absorb-boundary-sweep/phase1_proposal.md`
blind, fresh context. Charter: where absorbed energy goes; own the
per-proposal energy sidecar (absorbed power → ΔT → emission band →
detectability), post-run analytic, labelled as such.*

## Steel-man

This is a defensible instrument-fidelity cycle, not a mechanism proposal:
zero `lab/` diff, zero new material law, and §3 explicitly disclaims any
Tier-W/Tier-A verdict for Block ARTICLE's disk. §8.3 states plainly that
`lab/thermo_sidecar.py` is not imported, closing off the specific
`length_provenance` tripwire rather than hiding behind silence. Nothing
here manufactures new absorbed power: C40→C80 hold the article's own `σ`
and `r_out` fixed and move only the far-boundary padding, so no new
thermal-load question is created by this experiment's own construction —
if a thermal disposition already exists for this article class, moving a
domain boundary 40 cells away doesn't plausibly reopen it. §0's honesty
about *not* narrowing PLAN.md's queued THERMO/MATERIALS items, rather than
implying this cycle substitutes for them, is the right instinct even where
I think its execution is thin (see attack).

## Sharpest attack

§4 P-VIS42-7 is explicitly labelled "the constraint-scored article row" —
it scores a PASS/MARGINAL/FAIL bucket and a descriptive |C|=0.00449 for a
real absorbing disk, τ_center=0.0065, which §6 idealization 8 admits
"shares τ and construction idiom with `off_pass`." That article's thermal
disposition is not new territory — it is ESTABLISHED (T5, Iteration 20/
exp-043): every OFF-state σ(I) article at this program's bench scale reads
UNDETECTABLE, >100× below sourced microbolometer NETD. The proposal never
cites this. §8.3's only `thermo_sidecar` sentence exists solely to dodge
the `length_provenance` guard tripwire, not to discharge the sidecar
obligation PANEL.md's metrics table states applies "every run." A
one-sentence citation costs zero FDTD and zero new code — its absence on a
document this disclosure-dense reads as an omission, not a genuine gap.

## Verdict: support-with-changes

Two concrete additions, both cheap, both squarely in this seat's charter:

1. **§4 P-VIS42-7 / §5**: add a citation to T5's established UNDETECTABLE
   finding (Iteration 20, exp-043, `lab/thermo_sidecar.py`) for the
   off_pass-class OFF-state article, stating explicitly that Block
   ARTICLE's disk inherits that disposition unchanged (same σ, same
   r_out — only the ambient boundary systematic is under test) and that no
   new thermal question is opened by C40 vs C80. This is the missing half
   of an otherwise well-disciplined document.
2. **§0**: the sentence "PLAN.md's three queued items... remain valid
   backlog and nothing here narrows them" is true but flattens them into
   one undifferentiated list. It should name that item (1) — the CNT-forest
   `R_contact` term — is not merely "backlog" but PLAN.md's *current
   top-ranked* item, named at/near #1 by five of six Iteration-41 seats, and
   the only carried item that can move TD-5's 7.8× margin, this program's
   thinnest safety factor on record. Choosing the T24 item over it (in
   service of Red Team's Iteration-41 recommendation to feed a
   constraint-scored FDTD run) is a defensible call — but the proposal
   should say *what* is being traded off, not just that nothing is
   "narrowed." As written, a reader skimming §0 would not learn that this
   is the second consecutive cycle the program's most urgent physics item
   has been passed over since it topped the queue.

Neither issue is fatal to the experiment's design or its P-VIS42-1..9
falsification bands, which are otherwise outside this seat's jurisdiction
and look sound on their own (instrument/boundary-systematic) terms.

## Parameter change that would flip to plain support

Add the two sentences above (T5 citation in §4/§5; explicit rank/urgency
language for the CNT `R_contact` item in §0). No band, geometry, or FDTD
budget change is needed — this is a disclosure fix, not a physics fix.
