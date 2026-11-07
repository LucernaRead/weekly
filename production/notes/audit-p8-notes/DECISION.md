# Adjudication of the P8 printed-note audit (main line, 2026-10-21)

Audit result: 51/51 repo editions checked. 49 CLEAN, 0 SHORT, 2 EXTRA_ONLY (en-de, en-fr print all 149 notes vs the EN core's filtered 62; the extra 87 are genuine translated registry notes).

## Decisions
- **en-de / en-fr EXTRA_ONLY — ACCEPTED, no correction.** A superset of correct notes is not a defect: nothing missing, nothing wrong. The core's length filter was a space device for Chinese notes. Re-rendering two archived editions to REMOVE correct content risks new defects for zero reader benefit. Do not re-flag in future audits; this is the settled state.
- **de-en #32 `Falsch(note)` (missing space before parenthesis) — LOGGED, not churned.** One cosmetic spacing deviation in one note of an archived edition; below the correction-flow bar (cf. factual/layout corrections: ES viernes weekday, IT footnote spill). Fix it opportunistically if de-en is ever re-rendered for another reason.
- **Gate change (permanent):** every future fan-out proofread must include the printed-note SET equality check (edition printed set vs core computed set, by exercise number). Especially load-bearing for editions built on the EN and FR cores — the only two cores with the risky length-threshold print rule (EN prints 62/149, FR prints 67/145; all FR fan-outs so far verified exact).
