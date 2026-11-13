# ru-pt — self-check record (2026-11-11)

## Artifacts
- Edition dir: `production/2026-w47/2026-w47-ru-pt/`
- Print PDF: `Lucerna-VOL4-ru-pt.pdf` 21,199,772 bytes, SHA-256 `e6171dabf8d871619b75a45c691ffbf41cd994bf1ef597ad6907294b6f26ff88`
- Web PDF: `Lucerna-VOL4-ru-pt-web.pdf` 3,344,677 bytes, SHA-256 `cc8fea68fcf0c8292cae4f73ee0ed23c2facacae1d34e77f9fdd1b2d995323ce`
- `.text.md`: 58,994 bytes, 150 exercises, 203 blocks; `ABSTRACT.txt` (404 bytes, no ASCII quotes); `WEEKLY-KIT.md` written.

## Gates (all pass)
- run.py exit 0, TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE; check_core golden BAD 0, gloss 0, 1 orphan line-start (benign, same class as core), 1 same-baseline collision (same as core).
- p8 extract 150/150; compare CLEAN; keydiff [137,138,139,140] only (E keys translated); other 146 keys byte-identical to core.
- Occlusion: 42 TEXTX, 0 LINEX; adjudication 42/42 CLEAR (shared adjudicate_ru.py).
- Freeze: baseline exit 0; direct sha256 8/8.
- Print/web text: multiset identical (31,041 chars each); web pdftotext 58,200 bytes; web < 7 MB.
- P8 min font 9.75 pt. §1.1: all checks pass (s11_check.py).
- Visual: 8/8 cards read; 150-question recheck of .text.md: 0 issues (150 ex + 150 answer lines, both contiguous 1–150, 0 key mismatches, 0 CJK).
- P8 chips: A 113–120 ×8, G 145–149 ×5, H head + 150 ✓. Morozko image skipped by design (keys end col 3 y=2301.84).

## Build history
- Build 1 (print 21,199,757 bytes SHA `f96174ec…`; web 3,344,665 bytes SHA `baf8c33b…`): gates passed (42 TEXTX, 0 LINEX, 42/42 CLEAR) but visual check found 1 defect: P3 gloss `криминальная criminal policial` — two adjectives reading as "criminal police".
- Fix: `криминальная policial` (matching es `policíaca`). Build 2 = final, re-gated in full. No changes after final render.
- 0 curly apostrophes in TM pt (no map fix needed). Ded Moroz rendered `Avô Gelo` (fr/it-parallel).

## Logs in this dir
build_map.log, build_map2.log, apply.log, apply2.log, run.log, run2.log, render.log, render2.log, webpdf.log, webpdf2.log, check_core.log, check_core2.log, occlusion.log, occlusion2.log, ru-pt-occlusion.json, ru-pt-occlusion2.json, p8-extract.log, p8-extract2.log, p8-compare.log, p8-compare2.log, ru-pt-p8.json, ru-pt-p8-2.json, ru-pt-p8-compare.json, ru-pt-p8-compare2.json, adjudication.log, adjudication2.log, freeze.log, freeze2.log, freeze/, freeze2/, textmd.log, textmd2.log.

## Verdict
**Zero issues. Ready for independent proofread.**
