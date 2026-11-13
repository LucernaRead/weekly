# ru-ko — self-check record (2026-11-11)

## Artifacts
- Edition dir: `production/2026-w47/2026-w47-ru-ko/`
- Print PDF: `Lucerna-VOL4-ru-ko.pdf` 22,002,774 bytes, SHA-256 `4e450e65c7c5dfb5b2574a5400ccd98be5f687c2e2341d44a95b312134055ca0`
- Web PDF: `Lucerna-VOL4-ru-ko-web.pdf` 3,474,892 bytes, SHA-256 `797af4e6e622d16a04577ae25b4ddea8e21c7dc668a56e172d945c06350984f0`
- `.text.md`: 58,811 bytes, 150 exercises, 203 blocks; `ABSTRACT.txt` (416 bytes, no ASCII quotes); `WEEKLY-KIT.md` written.

## Gates (all pass)
- run.py exit 0, TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE; check_core golden BAD 0, gloss 0, 1 orphan line-start (benign, same class as core), 1 same-baseline collision (same as core).
- p8 extract 150/150; compare CLEAN; keydiff [137,138,139,140] only (E keys translated); other 146 keys byte-identical to core.
- Occlusion: 42 TEXTX, 0 LINEX; adjudication 42/42 CLEAR (shared adjudicate_ru.py).
- Freeze: baseline exit 0; direct sha256 8/8.
- Print/web text: multiset identical (26,441 chars each); web pdftotext 58,554 bytes; web < 7 MB.
- P8 min font 9.75 pt. §1.1: all checks pass (s11_check.py). Print PDF 22,002,774 bytes, 71 distinct font xrefs (ja render-size lesson applied).
- Visual: 8/8 cards read; 150-question recheck of .text.md: 0 issues (150 ex + 150 answer lines, both contiguous 1–150, 0 key mismatches; 4,026 Hangul chars, expected).
- P8 chips: A 113–120 ×8, G 145–149 ×5, H head + 150 ✓. Morozko image skipped by design (keys end col 3 y=2216.08).

## Build history
- Build 1 (print 22,006,177 bytes SHA `4c17104f…`; web 3,475,811 bytes SHA `5d6cf65f…`): gates passed (42 TEXTX, 0 LINEX, 42/42 CLEAR) but the visual check found 4 defects: (1) P4 gloss mid-word split `강등권` / `에.`; (2) P5 gloss split `입어` / `보기.`; (3) P7 B2 bridge split `약속한` / `다;` — all one class (CJK character-greedy wrapping splits Korean words); (4) P2 band `2면 연습` vs TM `N면 연습 문제` on P3–P6.
- Fixes: P4 `동점을 만들다` → `동점`; P5 `달력상의 날짜 · подошёл 잘 맞았다` → `달력 날짜 · подошёл 맞음`; P7 `기상 예보관들이 약속한다; по данным ～에 따르면` → `예보관들이 약속한다; по данным 에 따르면` (deliberate TM override); P2 band → `2면 연습 문제`. A space-preferring wrap simulator (validated against all three build-1 breaks) confirms clean word-boundary breaks. Build 2 = final, re-gated in full; all 4 fixes verified on 2× zoom crops.
- Map overrides (deliberate, build_map exit 1 is the tripwire): `мокрый снег = 湿雪` → `진눈깨비` (not TM `젖은 눈` — one Russian word, one Korean gloss per issue); P7 B2 bridge (above). Rejected after deliberation (TM accepted): `гололедица = 路面结冰` → TM `노면 결빙` (+ word-box gloss `도로 결빙` → `노면 결빙`); `答案见第8版…` → TM `답은 8면…`. NOTE: the first edit script failed with an AssertionError — the miss-tr value is the full string `목… = 진눈깨비`, not `진눈깨비` alone; the assert was wrong, the file was unchanged, and the re-edit used the full-string assert.
- No double `해설 —` prefix risk for ko (unlike ja): TM ko has only the prefix literal itself starting with `해설 — `, and W46 ru-ko has 0 `f.gloss("해설 — "` calls. Ded Moroz rendered `데드 모로즈`; `ледяной дождь` → `얼음비`, `мокрый снег` → `진눈깨비`.
- Note: SVG/cards are already 1950×2700 — 1:1 with card pixels; do NOT apply a 1.466 scale when cropping (first two build-2 crops missed their targets for this reason).

## Logs in this dir
build_map.log, build_map2.log, build_map3.log, build_map4.log, apply.log, apply2.log, apply3.log, run.log, run2.log, render.log, render2.log, webpdf.log, webpdf2.log, check_core.log, check_core2.log, occlusion.log, occlusion2.log, ru-ko-occlusion.json, ru-ko-occlusion2.json, p8-extract.log, p8-extract2.log, p8-compare.log, p8-compare2.log, ru-ko-p8.json, ru-ko-p8-2.json, ru-ko-p8-compare.json, ru-ko-p8-compare2.json, adjudication.log, adjudication2.log, freeze.log, freeze2.log, freeze/, freeze2/, textmd.log, textmd2.log, crop-p2-band.png, crop-p4-gloss.png, crop-p5-gloss.png, crop-p7-bridge.png.

## Verdict
**Zero issues. Ready for independent proofread.**
