# ru-nl — re-fanout self-check record (2026-11-11)

Rebuilt from finalized core-ru (fix1 f11854bf) with the D1 map fix.
Core verified before and after (unchanged): print `Lucerna-VOL4.pdf`
31,429,147 bytes SHA `d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81`;
web 4,025,834 bytes SHA `2f995f1deb75fce116b33a10b9da816fb415a7bac79a258d817c4f99731e4197`;
text 60,953 bytes SHA `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc`.
Old edition backed up whole-dir to
`hidden_files/w47/scratch-refanout-ru/backup-old/2026-w47-ru-nl/` (44 files).

## Artifacts (rebuilt)
- Print PDF: `Lucerna-VOL4-ru-nl.pdf` 21315805 bytes, SHA-256 `8982ce29eaf2bc57661a089b9bf0bd8021444130e2e0c9aa505f9176de4a1e17`
- Web PDF: `Lucerna-VOL4-ru-nl-web.pdf` 3387072 bytes, SHA-256 `abc3ec69f695129c9e248dae36880da1754f6af5ef32b62f5438435458512593`
- `.text.md`: 64053 bytes, 150 exercises, 277 blocks; SHA-256 `96dc93598dec047b87a168c2332bc30b611b8a42250d22e65c7e1da2920ac694`
- `ABSTRACT.txt` restored from backup (identical to map meta abstract); `WEEKLY-KIT.md` updated §5 + §7.

## D1 / D2 / D6 / kicker (all landed)
- D1 (4 KEEP strings, surgical map patch — old map + 4 values): text.md L459 `УЧЕБНЫЕ ДАННЫЕ`,
  L504 `Три уровня, три темы`, L596 `Большой тест недели + все ответы`;
  disclaimer (string 2) absent from text.md by design, present in p6 SVG;
  all 4 in SVG. Freeze diff core→rebuilt: removed distinct 487 / count-sum 854;
  Cyrillic-bearing removed 15: Билибин ×1; Билибина ×1; Зимняя ×1; Иван ×1; Ивана ×1; Иллюстрация ×1; Морозко ×1; год ×1; достояние ×1; иллюстрация ×1; к ×1; можно ×1; ноябрю ×1; общественное ×1; сказка ×1. Unexplained: 0.
  Added CJK: only U+3000 ×8 (furniture separators).
- D2: Q25 option `День студента` (content12.py:276); full phrase still ×2 in text.md, same count as core.
- D6: Q20 key `желании` (content12.py:257); text.md ×2; p8 extract key 20 = `желании` = core ru-p8.json:177.
- Kicker: content12.py:18 double spaces landed; PIL ink gaps [7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6], min 5.9 px ≥ 4.
- text.md diff old→new: exactly 6 line pairs (63984 → 64053 bytes), nothing else.

## Gates (all pass)
- apply rc=1: only the known D6 fix-comment CJK (content12.py:261 comment, not a literal); no unmapped literals.
- run.py exit 0, TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE.
- render.py exit 0; webpdf.py (patched 40963281) exit 0; print + web 8 pages.
- check_core.py exit 0: golden BAD 0, gloss 0 (orphans/collisions as in the first build — see build.log).
- p8 extract 150/150; compare CLEAN, keydiff [137, 138, 139, 140];
  direct keydiff vs core ru-p8.json exactly [137, 138, 139, 140].
- Occlusion: 42 TEXTX, 0 LINEX; adjudicated 42/42 CLEAR.
- Freeze: baseline 8/8 byte-identical.
- Print/web text: multiset identical overall and per page (31087 chars).
- P8 min font 9.75 pt (§1.1 all pass, s11_check rc 0).
- Creambox full 8-page scan: no negative inside-only clearance;
  95 BELOW-WINDOW lines (+28.0 ×25, +32.0 ×41, +34.0 ×4, +37.0 ×25), all classified pre-existing;
  scan byte-identical to the first build.
- Morozko image: SKIPPED by the build's own condition — same as the first build.

## Logs in this dir
build.log (logs/nl/), gates.log, gates.json, core-p8.json, ru-nl-p8.json,
ru-nl-p8-compare.json, ru-nl-occlusion.json, freeze/ (build-copy),
freeze-diff.json, creambox.log, creambox-vs-backup.diff (only if non-identical).

## Verdict
**Zero issues. Rebuilt, re-gated, ready for independent proofread.**
