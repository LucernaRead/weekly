# ru-es — self-check record (2026-11-11)

## Artifacts
- Edition dir: `production/2026-w47/2026-w47-ru-es/`
- Print PDF: `Lucerna-VOL4-ru-es.pdf` 21,272,810 bytes, SHA-256 `acef924f8742bc78726e73ca84c30ff9097ca4e8b99d1a9715bb834e92a89293`
- Web PDF: `Lucerna-VOL4-ru-es-web.pdf` 3,348,591 bytes, SHA-256 `788411a8c3aadd54e64088022d41680b90b8c15762773c594775f3c76d9bee90`
- `.text.md`: 58,041 bytes, 150 exercises, 203 blocks; `ABSTRACT.txt` (394 bytes, no ASCII quotes); `WEEKLY-KIT.md` written.

## Gates (all pass)
- run.py exit 0, TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE; check_core golden BAD 0, gloss 0, 1 orphan line-start (benign, same class as core), 1 same-baseline collision (same as core).
- p8 extract 150/150; compare CLEAN; keydiff [137,138,139,140] only (E keys translated); other 146 keys byte-identical to core.
- Occlusion: 42 TEXTX, 0 LINEX; adjudication 42/42 CLEAR (shared adjudicate_ru.py).
- Freeze: baseline exit 0; direct sha256 8/8.
- Print/web text: multiset identical (30,774 chars each); web pdftotext 57,780 bytes; web < 7 MB.
- P8 min font 9.75 pt. §1.1: all checks pass (s11_check.py).
- Visual: 8/8 cards read; 150-question recheck of .text.md: 0 issues (150 ex + 150 answer lines, both contiguous 1–150, 0 key mismatches, 0 CJK).
- P8 chips: A 113–120 ×8, G 145–149 ×5, H head + 150 ✓. Morozko image skipped by design (keys end col 3 y=2316.53).

## Build history
- Build 1 (print 21,272,814 bytes SHA `3dd80cb7…`; web 3,348,622 bytes SHA `9f06db01…`): gates passed (42 TEXTX, 0 LINEX, 42/42 CLEAR) but visual check found 1 defect: P7 error-clinic note `на + preposicional: на «чёрной пятнице».` measured 385.4 px at 19.5 px sans — just over the 378.5 px line — and wrapped to 2 lines.
- Fix: abbreviated to `на + prepos.: на «чёрной пятнице».` (330.0 px, 1 line). Build 2 = final, re-gated in full. No changes after final render.
- Note: one exec step (webpdf+check_core) was aborted mid-run by the runtime; re-ran cleanly with identical results. es/ dir had to be mkdir'd before build_map (log redirect failed otherwise).

## Logs in this dir
build_map.log, build_map2.log, apply.log, apply2.log, run.log, run2.log, render.log, render2.log, webpdf.log, webpdf2.log, check_core.log, check_core2.log, occlusion.log, occlusion2.log, ru-es-occlusion.json, ru-es-occlusion2.json, p8-extract.log, p8-extract2.log, p8-compare.log, p8-compare2.log, ru-es-p8.json, ru-es-p8-2.json, ru-es-p8-compare.json, ru-es-p8-compare2.json, adjudication.log, adjudication2.log, freeze.log, freeze2.log, freeze/, freeze2/, textmd.log, textmd2.log.

## Verdict
**Zero issues. Ready for independent proofread.**
