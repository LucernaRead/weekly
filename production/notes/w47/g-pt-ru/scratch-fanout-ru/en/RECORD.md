# ru-en — self-check record (2026-11-10/11)

## Artifacts
- Edition dir: `production/2026-w47/2026-w47-ru-en/`
- Print PDF: `Lucerna-VOL4-ru-en.pdf` 21,245,420 bytes, SHA-256 `023d9fd12bdca276751400fb13f7f399d645c267a09ba1897eb0e598d52f2e3a`
- Web PDF: `Lucerna-VOL4-ru-en-web.pdf` 3,341,934 bytes, SHA-256 `fab0fc44736ecb169a1cc3932a8e85db2504f694f02e84d45f3063435327493d`
- `.text.md`: 56,604 bytes, 150 exercises, 203 blocks; `ABSTRACT.txt` (354 bytes, no ASCII quotes); `WEEKLY-KIT.md` written.

## Gates (all pass)
- run.py exit 0, TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE; check_core golden BAD 0, gloss 0, 1 orphan line-start (benign, same class as core), 1 same-baseline collision (same as core).
- p8 extract 150/150; compare CLEAN; keydiff [137,138,139,140] only (E keys translated); other 146 keys byte-identical to core.
- Occlusion: 42 TEXTX, 0 LINEX; adjudication 42/42 CLEAR (adjudicator bug fixed: detail `\u3000` literal needed unicode-escape decode + strip).
- Freeze: baseline exit 0; direct sha256 8/8.
- Print/web text: multiset identical (30,293 chars each); web pdftotext 57,200 bytes; web < 7 MB.
- P8 min font 9.75 pt. §1.1: all checks pass (s11_check.py).
- Visual: 8/8 cards read; 150-question recheck of .text.md: 0 issues.
- P8 chips: A 113–120 ×8, G 145–149 ×5, H head + 150 ✓. Morozko image skipped by design (keys end y=2288.84).

## Build history
- Build 1: P1 LINEX (word gloss wrapped), P7 LINEX (F-MAIL stack crossed quotes divider), key 137 parse artifact — all fixed in build 2 (see KIT §7).
- Build 2 = final. No changes after final render.

## Logs in this dir
run.log, run2.log, render.log, render2.log, webpdf2.log, check_core.log, check_core2.log, p8-extract.log, p8-extract2.log, p8-compare.log, p8-compare2.log, ru-en-p8.json, ru-en-occlusion.json, occlusion.log, occlusion2.log, adjudicate_en.py, adjudication.log, textmd.log, freeze.log, freeze/ (build-copy), crop-p7-band.png, crop-p8-band.png, crop-p8-answers-head.png.

## Verdict
**Zero issues. Ready for independent proofread.**
