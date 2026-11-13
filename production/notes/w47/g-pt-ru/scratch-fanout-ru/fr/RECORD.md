# ru-fr — self-check record (2026-11-11)

## Artifacts
- Edition dir: `production/2026-w47/2026-w47-ru-fr/`
- Print PDF: `Lucerna-VOL4-ru-fr.pdf` 21,260,891 bytes, SHA-256 `b9476fc2d49584d134e61d59f587bd24e76f4da0caf66de03884ba86523f3629`
- Web PDF: `Lucerna-VOL4-ru-fr-web.pdf` 3,346,639 bytes, SHA-256 `78a56be6b7094ce1e9dd2435f174e4e8bb563e6c7363b2a2f82815dfd17128fe`
- `.text.md`: 57,356 bytes, 150 exercises, 203 blocks; `ABSTRACT.txt` (434 bytes, no ASCII quotes); `WEEKLY-KIT.md` written.

## Gates (all pass)
- run.py exit 0, TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE; check_core golden BAD 0, gloss 0, 1 orphan line-start (benign, same class as core), 1 same-baseline collision (same as core).
- p8 extract 150/150; compare CLEAN; keydiff [137,138,139,140] only (E keys translated); other 146 keys byte-identical to core.
- Occlusion: 42 TEXTX, 0 LINEX; adjudication 42/42 CLEAR (shared adjudicate_ru.py).
- Freeze: baseline exit 0; direct sha256 8/8.
- Print/web text: multiset identical (30,708 chars each); web pdftotext 57,844 bytes; web < 7 MB.
- P8 min font 9.75 pt. §1.1: all checks pass (s11_check.py).
- Visual: 8/8 cards read; 150-question recheck of .text.md: 0 issues (150 ex + 150 answer lines, both contiguous 1–150, 0 key mismatches, 0 CJK).
- P8 chips: A 113–120 ×8, G 145–149 ×5, H head + 150 ✓. Morozko image skipped by design (keys end col 3 y=2301.84).

## Build history
- Build 1 (print 21,335,558 bytes SHA `f1a5947b…`; web 3,347,012 bytes SHA `3354dfef…`): gates passed (43 TEXTX, 0 LINEX, 43/43 CLEAR) but visual check found 2 real defects:
  1. P1 numbers-box head `La journée en chiffres` ended x≈989, touching the B1 Q6 chip (0 px gap) — pixel-measured.
  2. Curly apostrophe U+2019 renders full-width (20.5 px at 20.5 px font) in the CJK SC sans font, giving `C' est`, `l' année` — 9–10 px gaps. Inherited from W46 TM (31 curly values), fixed anyway.
- Fixes: head → `EN CHIFFRES` (W46 pattern); ’ → ' in 52 map values (map-fr.json post-process; meta.abstract kept curly). Build 2 = final, re-gated in full. No changes after final render.
- Also fixed during build 1 authoring: a typo'd miss-tr key (`。` before `»`) caught by build_map as UNUSED — fixed the key, no duplicate added.

## Logs in this dir
build_map.log, apply.log, run.log, run2.log, render.log, render2.log, webpdf.log, webpdf2.log, check_core.log, check_core2.log, occlusion-selftest.log, occlusion.log, occlusion2.log, ru-fr-occlusion.json, ru-fr-occlusion2.json, p8-extract.log, p8-extract2.log, p8-compare.log, p8-compare2.log, ru-fr-p8.json, ru-fr-p8-2.json, ru-fr-p8-compare.json, ru-fr-p8-compare2.json, adjudication.log, adjudication2.log, freeze.log, freeze2.log, freeze/, freeze2/, textmd.log, textmd2.log, adjudicate_en.py (build-1 copy; build 2 used shared adjudicate_ru.py).

## Verdict
**Zero issues. Ready for independent proofread.**
