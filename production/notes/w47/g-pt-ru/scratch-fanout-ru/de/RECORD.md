# ru-de — self-check record (2026-11-11)

## Artifacts
- Edition dir: `production/2026-w47/2026-w47-ru-de/`
- Print PDF: `Lucerna-VOL4-ru-de.pdf` 21,226,139 bytes, SHA-256 `31fab92b7b1b392f9bb3a80acf449af239e948c55584581f96428c15a1248521`
- Web PDF: `Lucerna-VOL4-ru-de-web.pdf` 3,347,223 bytes, SHA-256 `1a67d6b46352c3ae7bc039832bca0302399254f4e410dd268c43e98065296da7`
- `.text.md`: 57,310 bytes, 150 exercises, 203 blocks; `ABSTRACT.txt` (419 bytes, no ASCII quotes); `WEEKLY-KIT.md` written.

## Gates (all pass)
- run.py exit 0, TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE; check_core golden BAD 0, gloss 0, 1 orphan line-start (benign, same class as core), 1 same-baseline collision (same as core).
- p8 extract 150/150; compare CLEAN; keydiff [137,138,139,140] only (E keys translated).
- Occlusion: 42 TEXTX, 0 LINEX; adjudicated 42/42 CLEAR (shared adjudicate_ru.py).
- Freeze: baseline exit 0; direct sha256 8/8.
- Print/web text: multiset identical (30,938 chars each); web pdftotext 57,709 bytes; web < 7 MB.
- P8 min font 9.75 pt. §1.1: all checks pass (s11_check.py).
- Visual: 8/8 cards read; 150-question recheck of .text.md: 0 issues.
- P8 chips: A 113–120 ×8, G 145–149 ×5, H head + 150 ✓. Morozko image skipped by design.

## Build history
- Single build (build 1 = final). Pre-build width fixes in miss-tr-de.json (measured with svglib.text_w): P1 gloss → `Black Friday (Ausverkauf).`, P7 word gloss → `großer Ausverkauf.`, A-bridges → `Seite N lesen und die Antwort wählen.`, key 137 ` — ` → `, `.

## Logs in this dir
build_map.log, apply.log, run.log, render.log, webpdf.log, check_core.log, occlusion-selftest.log, occlusion.log, ru-de-occlusion.json, p8-extract.log, p8-compare.log, ru-de-p8.json, ru-de-p8-compare.json, adjudication.log, freeze.log, freeze/ (build-copy), textmd.log.

## Verdict
**Zero issues. Ready for independent proofread.**
