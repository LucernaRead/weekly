# ru-it — self-check record (2026-11-11)

## Artifacts
- Edition dir: `production/2026-w47/2026-w47-ru-it/`
- Print PDF: `Lucerna-VOL4-ru-it.pdf` 21,260,017 bytes, SHA-256 `a3e17e19cca04a961963feea38afd63e001b27b3cea5fa872ae6f74890e87575`
- Web PDF: `Lucerna-VOL4-ru-it-web.pdf` 3,345,188 bytes, SHA-256 `04fa800929cbf87e65a7e16b658f296c4939ba18ebbfdd7b149296ed4e501912`
- `.text.md`: 57,852 bytes, 150 exercises, 203 blocks; `ABSTRACT.txt` (390 bytes, no ASCII quotes); `WEEKLY-KIT.md` written.

## Gates (all pass)
- run.py exit 0, TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE; check_core golden BAD 0, gloss 0, 1 orphan line-start (benign, same class as core), 1 same-baseline collision (same as core).
- p8 extract 150/150; compare CLEAN; keydiff [137,138,139,140] only (E keys translated); other 146 keys byte-identical to core.
- Occlusion: 42 TEXTX, 0 LINEX; adjudication 42/42 CLEAR (shared adjudicate_ru.py).
- Freeze: baseline exit 0; direct sha256 8/8.
- Print/web text: multiset identical (30,862 chars each); web pdftotext 57,648 bytes; web < 7 MB.
- P8 min font 9.75 pt. §1.1: all checks pass (s11_check.py).
- Visual: 8/8 cards read; 150-question recheck of .text.md: 0 issues (150 ex + 150 answer lines, both contiguous 1–150, 0 key mismatches, 0 CJK).
- P8 chips: A 113–120 ×8, G 145–149 ×5, H head + 150 ✓. Morozko image skipped by design (keys end col 3 y=2288.34).

## Build history
- Build 1 (print 21,260,003 bytes SHA `e9379a97…`; web 3,345,203 bytes SHA `01ed8ec6…`): gates passed (42 TEXTX, 0 LINEX, 42/42 CLEAR) but visual check found 1 defect: P2 gloss `поздравить congratularsi` — reflexive, needs `con` for a person; in a holiday-greeting context the idiomatic Italian is `fare gli auguri` (matches P8 key 130 `Fare gli auguri a un amico studente martedì`).
- Fix: `поздравить fare gli auguri · родина terra natale · повод occasione.` Build 2 = final, re-gated in full. No changes after final render.
- 14 TM curly apostrophes replaced ’ → ' at map level before apply (fr lesson); 0 curly in applied sources (grep-verified). Ded Moroz rendered `Nonno Gelo` (fr-parallel: Père Gel).
- Note: first grep for the fix looked in content34.py and returned 0 — the P2 note lives in content12.py (verified with full-dir grep).

## Logs in this dir
build_map.log, build_map2.log, apply.log, apply2.log, run.log, run2.log, render.log, render2.log, webpdf.log, webpdf2.log, check_core.log, check_core2.log, occlusion.log, occlusion2.log, ru-it-occlusion.json, ru-it-occlusion2.json, p8-extract.log, p8-extract2.log, p8-compare.log, p8-compare2.log, ru-it-p8.json, ru-it-p8-2.json, ru-it-p8-compare.json, ru-it-p8-compare2.json, adjudication.log, adjudication2.log, freeze.log, freeze2.log, freeze/, freeze2/, textmd.log, textmd2.log.

## Verdict
**Zero issues. Ready for independent proofread.**
