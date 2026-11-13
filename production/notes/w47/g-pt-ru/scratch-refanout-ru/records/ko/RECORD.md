# ru-ko — re-fanout self-check record (2026-11-11)

Rebuilt from finalized core-ru (fix1 f11854bf) with the D1 map fix.
Core verified before and after (unchanged): print `Lucerna-VOL4.pdf`
31,429,147 bytes SHA `d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81`;
web 4,025,834 bytes SHA `2f995f1deb75fce116b33a10b9da816fb415a7bac79a258d817c4f99731e4197`;
text 60,953 bytes SHA `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc`.
Old edition backed up whole-dir to
`hidden_files/w47/scratch-refanout-ru/backup-old/2026-w47-ru-ko/` (44 files).

## Artifacts (rebuilt)
- Print PDF: `Lucerna-VOL4-ru-ko.pdf` 22007810 bytes, SHA-256 `78e4442af8af9ec286c407ff66e08bac2029dd79d3ded43d1bfde3d555a6a400`
- Web PDF: `Lucerna-VOL4-ru-ko-web.pdf` 3513230 bytes, SHA-256 `3bf39ecf4fa4563458c68319ca42171642f9ad0be24650064faa9b7d9bd03195`
- `.text.md`: 65069 bytes, 150 exercises, 277 blocks; SHA-256 `d1feb40e417ba058d773a58ada62ad7fd7805b6a943599d8d017510b402d5a3d`
- `ABSTRACT.txt` restored from backup (identical to map meta abstract); `WEEKLY-KIT.md` updated §5 + §7.

## D1 / D2 / D6 / kicker (all landed)
- D1 (4 KEEP strings, surgical map patch — old map + 4 values): text.md L459 `УЧЕБНЫЕ ДАННЫЕ`,
  L504 `Три уровня, три темы`, L596 `Большой тест недели + все ответы`;
  disclaimer (string 2) absent from text.md by design, present in p6 SVG;
  all 4 in SVG. Freeze diff core→rebuilt: removed distinct 361 / count-sum 529;
  Cyrillic-bearing removed 15: Билибин ×1; Билибина ×1; Зимняя ×1; Иван ×1; Ивана ×1; Иллюстрация ×1; Морозко ×1; год ×1; достояние ×1; иллюстрация ×1; к ×1; можно ×1; ноябрю ×1; общественное ×1; сказка ×1. Unexplained: 0.
  Added CJK: only U+3000 ×8 (furniture separators).

- D1a/D1b (ko-only, proof1-flagged, same KEEP mechanism): two translator typos
  in the ko map's `lit` bucket, corrected in `maps/map-ko.json` (pre-fix copy
  `map-ko.json.bak-pre-d1ab`): P2 gloss `родина` was rendered `роди나`
  (Hangul 나 for Cyrillic на; proof1 D1a, text.md L99) and P7 bridge
  `синоптики` was rendered as Hangul 시 + Cyrillic `ноптики` (proof1 D1b,
  text.md L538). Both were present in the first build (identical freeze
  removals); the re-fanout restores the core's words. After the fix the freeze
  diff's Cyrillic-bearing removed list is the standard {Q46 `можно` + 14
  Morozko-caption words}, same as the other 9 editions.
- D2: Q25 option `День студента` (content12.py:276); full phrase still ×2 in text.md, same count as core.
- D6: Q20 key `желании` (content12.py:257); text.md ×2; p8 extract key 20 = `желании` = core ru-p8.json:177.
- Kicker: content12.py:18 double spaces landed; PIL ink gaps [7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6], min 5.9 px ≥ 4.
- text.md diff old→new: exactly 8 line pairs (65002 → 65069 bytes), nothing else.

## Gates (all pass)
- apply rc=0, apply OK.
- run.py exit 0, TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE.
- render.py exit 0; webpdf.py (patched 40963281) exit 0; print + web 8 pages.
- check_core.py exit 0: golden BAD 0, gloss 0 (orphans/collisions as in the first build — see build.log).
- p8 extract 150/150; compare CLEAN, keydiff [137, 138, 139, 140];
  direct keydiff vs core ru-p8.json exactly [137, 138, 139, 140].
- Occlusion: 42 TEXTX, 0 LINEX; adjudicated 42/42 CLEAR.
- Freeze: baseline 8/8 byte-identical.
- Print/web text: multiset identical overall and per page (26535 chars).
- P8 min font 9.75 pt (§1.1 all pass, s11_check rc 0).
- Creambox full 8-page scan: no negative inside-only clearance;
  96 BELOW-WINDOW lines (+28.0 ×25, +32.0 ×41, +34.0 ×4, +37.0 ×25, +44.0 ×1), all classified pre-existing;
  scan differs from the first build in 3 lines.
- Morozko image: SKIPPED by the build's own condition — same as the first build.

## Logs in this dir
build.log (logs/ko/), gates.log, gates.json, core-p8.json, ru-ko-p8.json,
ru-ko-p8-compare.json, ru-ko-occlusion.json, freeze/ (build-copy),
freeze-diff.json, creambox.log, creambox-vs-backup.diff (only if non-identical).

## Verdict
**Zero issues. Rebuilt, re-gated, ready for independent proofread.**
