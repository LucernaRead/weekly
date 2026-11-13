# ru-en — re-fanout self-check record (2026-11-11)

Rebuilt from finalized core-ru (fix1 f11854bf) with the D1 map fix.
Core verified before and after (unchanged): print `Lucerna-VOL4.pdf`
31,429,147 bytes SHA `d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81`;
web 4,025,834 bytes SHA `2f995f1deb75fce116b33a10b9da816fb415a7bac79a258d817c4f99731e4197`;
text 60,953 bytes SHA `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc`.
Old edition backed up whole-dir to
`hidden_files/w47/scratch-refanout-ru/backup-old/2026-w47-ru-en/` (44 files).

## Artifacts (rebuilt)
- Print PDF: `Lucerna-VOL4-ru-en.pdf` 21,251,190 bytes, SHA-256 `b244c56b7575f425e52902f19823f740d46cdafea2afcb1b86cdde24df863406`
- Web PDF: `Lucerna-VOL4-ru-en-web.pdf` 3,380,786 bytes, SHA-256 `d306b3f365c5b4a04022f2a900faee904eb3f838c2f530fe5b4ce667c62d14a9`
- `.text.md`: 62,829 bytes, 150 exercises, 277 blocks; SHA-256 `1e06ec55e8ba694224e244e37d81e6bfdfc3c3299e6aeb925308fd08e0b0e2ea`
- `ABSTRACT.txt` restored from backup (identical to map meta abstract); `WEEKLY-KIT.md` updated §5 + §7.

## D1 / D2 / D6 / kicker (all landed)
- D1 (4 KEEP strings, surgical map patch — old map + 4 values, byte-identical to
  `scratch-fix-ru-d1/maps/map-en.json`): text.md L459 `УЧЕБНЫЕ ДАННЫЕ`,
  L504 `Три уровня, три темы`, L596 `Большой тест недели + все ответы`;
  disclaimer (string 2) absent from text.md by design, present in p6 SVG;
  all 4 in SVG. Freeze diff core→rebuilt: removed distinct 484 / count-sum 850;
  Cyrillic-bearing removed 15 = Q46 `можно` ×1 (known legal) + 14 Morozko
  caption words (Билибин/Билибина/Зимняя/Иван/Ивана/Иллюстрация/Морозко/год/
  достояние/иллюстрация/к/ноябрю/общественное/сказка — core p8 y≥2450 caption
  block; image skipped by design in en, keys end y≈2288.84). Unexplained: 0.
  Added CJK: only U+3000 ×8 (furniture separators).
- D2: Q25 option `День студента` (content12.py:276); text.md L187 changed
  `17 ноября — Международный день студента` → `17 ноября — День студента`;
  full phrase still ×2 in text.md (article + Q11 stem), same count as core.
- D6: Q20 key `желании` (content12.py:257); text.md ×2 (L173 stem + L694 key
  list); p8 extract key 20 = `желании` = core ru-p8.json:177.
- Kicker: content12.py:18 double spaces landed; PIL ink gaps (INVEST-NOTE
  method 1) [7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6], min 5.9 px ≥ 4 —
  exactly the INVEST-NOTE Table 1 values; P1 row byte-identical to core.
- text.md diff old→new: exactly 6 line pairs (D6 ×2 lines, D2 ×1, D1 ×3) and
  nothing else (+60 bytes: 62,769 → 62,829). Old KIT/report numbers
  (56,604 bytes / 203 blocks) were stale — the shipped text.md was already
  62,769 bytes; regen from the old sources is byte-identical.

## Gates (all pass)
- apply rc=1: only the known D6 fix-comment CJK (`content12.py:261` comment,
  not a literal); no unmapped literals. en `content56.py:12` fix1 trailing
  comment re-added (map now carries the straight quotes directly — the old
  KIT claim that the map still had curly quotes is stale).
- run.py exit 0, TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE.
- render.py exit 0; webpdf.py (patched 40963281) exit 0; print + web 8 pages.
- check_core.py exit 0: golden BAD 0, gloss 0, orphans 1 (P7 y553 `”».`,
  known benign), same-baseline collision 1 (P1 y1712, known).
- p8 extract 150/150; compare CLEAN, keydiff [137, 138, 139, 140];
  direct keydiff vs core ru-p8.json exactly [137, 138, 139, 140].
- Occlusion: 42 TEXTX, 0 LINEX; adjudicated 42/42 CLEAR.
- Freeze: baseline 8/8 byte-identical.
- Print/web text: multiset identical overall and per page (30,363 chars).
- P8 min font 9.75 pt (§1.1 all pass, s11_check rc 0).
- Creambox full 8-page scan: no negative inside-only clearance; 95
  BELOW-WINDOW lines, all classified (next-block titles +37/+34, P2
  weather-word boxes +32, P6 day-strip legend +28 — the legend is the
  separate `content56.py:155` paragraph, by design); scan byte-identical
  to the backup-old scan (only path headers differ) — zero layout regression.
  P2 А ВЫ box desc-clear −1.0 is pre-existing (same in backup scan).

## Logs in this dir
build.log, gates.log, gates.json, core-p8.json, ru-en-p8.json,
ru-en-p8-compare.json, ru-en-occlusion.json, adjudication.log (in gates.log),
freeze/ (build-copy), freeze-diff.json, creambox.log, creambox-backup.log.

## Verdict
**Zero issues. Rebuilt, re-gated, ready for independent re-proofread**
(ru-en was finalized before, then voided by the core D2 fix).
