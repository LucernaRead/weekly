# de-core duplicate re-sync (coordinator, 2026-11-03 ~06:21 UTC, after DE Round 4 PASS)

Decision (held since Round 3): re-sync the de-core duplicate by copying fixed canonical
artifacts + hash-verify, after a DE PASS verdict. Executed after the Round 4 PASS verdict.

Scope: EXACTLY 4 artifact files copied from the canonical edition dir
`files/weekly-report-w46-de-zh-cn/` into `files/weekly-report-w46-de-core/`
(core filenames kept for the PDFs):
- svg/p8-uebungen.svg (same filename)
- cards/p8-uebungen.png (same filename)
- Die-Lucerna-VOL3-ZH-CN-web.pdf -> Die-Lucerna-VOL3-web.pdf (content copy, core name kept)
- Die-Lucerna-VOL3-ZH-CN.pdf -> Die-Lucerna-VOL3.pdf (content copy, core name kept)

NOT touched: WEEKLY-KIT.md (the core KIT is a different document from the edition KIT —
core §§1–9, no Round 3 fix record, no wrong statements to correct), .text.md and
ABSTRACT.txt (already byte-identical), all other SVGs/cards.

Verification (before/after hash snapshots in this dir):
- Exactly 4 files changed (before-hashes.txt vs after-hashes.txt diff).
- Core P8 SVG sha256 now 0056300847d759bf98d55c65b2d0e61e157727bff6f447e914c119f0d48b0d17,
  equal to the canonical fixed SVG.
- sNFL: 0 in core P8 SVG, 0 in core web-PDF text layer (was 1); `das NFL-Spiel` x3 in
  core web-PDF text layer.
- Remaining canonical-vs-core diffs are only the PDF filenames (expected) and WEEKLY-KIT.md
  (deliberately untouched, different document).

The duplicate no longer carries the D-R2-1 defect. The standing caution remains: inserts
use canonical edition dirs only; never pass a *-core dir as --edition-dir.
