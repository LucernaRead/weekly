# ru-ja — self-check record (2026-11-11)

## Artifacts
- Edition dir: `production/2026-w47/2026-w47-ru-ja/`
- Print PDF: `Lucerna-VOL4-ru-ja.pdf` 27,404,856 bytes, SHA-256 `929a5c4786f256cb194cdab9cd7aafd0db1b8331e73ed8b0d1c1dcaf44b2a06e`
- Web PDF: `Lucerna-VOL4-ru-ja-web.pdf` 3,683,942 bytes, SHA-256 `fbfb35d3d34e7e196c43254db3995e78d84224f5da79fdeeb48fff7a0436d233`
- `.text.md`: 58,308 bytes, 150 exercises, 203 blocks; `ABSTRACT.txt` (392 bytes, no ASCII quotes); `WEEKLY-KIT.md` written.

## Gates (all pass)
- run.py exit 0, TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE; check_core golden BAD 0, gloss 0, 4 orphan line-starts (all inline-punctuation false positives on P7 + benign `”».`), same-baseline collision same as core.
- p8 extract 150/150; compare CLEAN; keydiff [137,138,139,140] only (E keys translated); other 146 keys byte-identical to core.
- Occlusion: 42 TEXTX, 0 LINEX; adjudication 42/42 CLEAR (shared adjudicate_ru.py).
- Freeze: baseline exit 0; direct sha256 8/8.
- Print/web text: multiset identical (26,540 chars each); web pdftotext 58,411 bytes; web < 7 MB.
- P8 min font 9.75 pt. §1.1: all checks pass (s11_check.py).
- Visual: 8/8 cards read; 150-question recheck of .text.md: 0 issues (150 ex + 150 answer lines, both contiguous 1–150, 0 key mismatches; 4,042 CJK chars = Japanese explanations, expected).
- P8 chips: A 113–120 ×8, G 145–149 ×5, H head + 150 ✓. Morozko image skipped by design (keys end col 3 y=2187.89).

## Build history
- Build 1 (print 27,405,307 bytes SHA `ae667e08…`; web 3,684,512 bytes SHA `007ea87f…`): gates passed (42 TEXTX, 0 LINEX, 42/42 CLEAR) but visual check found 4 defects: P6 double `解説 — 解説 —` prefix (W46 TM bug); P7 B2 bridge `解説 —` prefix inconsistent with A2/B1 bridges on the same page; P2 dangling 。 (gloss `成功を · 願い。`); P4 dangling 。 (D bridge `空所を埋める。`). Note: the first run+render attempt was killed by a service restart mid-run (7/8 SVGs, run.log 0 bytes); clean re-run produced build 1.
- Build 2 (print 72,574,946 bytes SHA `7404e9d6…` — DISCARDED): the 4 content fixes were in, but that run's pypdf merge duplicated the embedded CJK font subsets (6,485 font references vs normal 71). Per-page cairosvg output was normal (~27.4 MB total, matching core per-page scale); an isolated re-merge of the same SVGs gave 27,405,262 bytes / 71 fonts. Re-ran render.py → clean build. The 72 MB file was never gated or delivered.
- Build 3 = final (print 27,404,856 bytes SHA `929a5c47…`; web 3,683,942 bytes SHA `fbfb35d3…`): the B2-bridge shortening re-wrap left a dangling `；` + lone `ん。` (build-2 check found it); shortened again to `予報士が約束する；по данным により；может быть たぶん。` (L1 395.0 px, L2 401.7 px vs 422.5 px limit) — 2 clean lines, verified by 2× zoom crop. All 4 fixes verified visually. No changes after final render.
- 0 TM curly apostrophes. Ded Moroz rendered `ジェド・マロース` (standard katakana; no W46 precedent).

## Logs in this dir
build_map.log, build_map2.log, apply.log, apply2.log, apply3.log, apply4.log, run.log, run2.log, run3.log, render.log, render2.log, render2b.log, render3.log, webpdf.log, webpdf2.log, webpdf3.log, check_core.log, check_core2.log, check_core3.log, occlusion.log, occlusion3.log, ru-ja-occlusion.json, ru-ja-occlusion3.json, p8-extract.log, p8-extract3.log, p8-compare.log, p8-compare3.log, ru-ja-p8.json, ru-ja-p8-3.json, ru-ja-p8-compare.json, ru-ja-p8-compare3.json, adjudication.log, adjudication3.log, freeze.log, freeze3.log, freeze/, freeze3/, textmd.log, textmd3.log.

## Verdict
**Zero issues. Ready for independent proofread.**
