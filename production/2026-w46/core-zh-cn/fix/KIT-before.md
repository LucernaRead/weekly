# WEEKLY-KIT — Lucerna 简体中文周报 VOL.3 (W46), zh-cn × es

## Identity and spec

- **Issue week:** Monday 2026-11-09 to Sunday 2026-11-15. VOL.3.
- **Pairing:** zh-cn × es — Simplified Chinese body text with a Spanish
  explanation layer, the edition for Spanish-speaking readers. P1 badge
  (Latin-only, W45 precedent): “TEXTOS EN CHINO SIMPLIFICADO ·
  EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES
  HISPANOHABLANTES”.
- **Masthead:** bare `Lucerna` (no article). Every page footer reads
  “Lucerna · SEMANARIO CHINO SIMPLIFICADO VOL.3 · TEXTO EN CHINO
  SIMPLIFICADO · EXPLICACIONES EN ESPAÑOL”; page line “Página {n} de 8”.
  Gloss prefix “Nota — ”. P8 separator “— Página {n} —”. P7 phrase tags
  “Página N” (W45 ES precedent). Model answer “Respuesta modelo: ”.
- **Format:** 8 pages, 1950×2700 px, 4 columns, same geometry as the core.
  150 exercises, unified numbering 1–150, P8 keys generated from the
  registry. Core text frozen (see below); only the explanation layer was
  rewritten, natively in Spanish.
- **Status:** builder self-check complete (see gates below). Builder
  handoff, NOT a finalisation claim — independent proofreading is still
  owed by the parent line. No Discord, no chat dumps, no repo push.

## Contents

Identical to the core edition (`files/weekly-report-w46-zh-cn-core/
WEEKLY-KIT.md` — contents table, trend sources, W45-promise handling,
image authorisations). This KIT records only what differs: the Spanish
explanation layer, the transform, and the gates.

## Frozen-core proof

- Built by copying the finished W46 core build dir and applying exact-
  string replacements (282 keys, `hidden_files/w46/maps/es.json`,
  `hidden_files/w46/transform.py` — every key asserted found; coverage
  checked with `hidden_files/w46/coverage.py`: all English display strings
  covered or explicitly frozen).
- `tools/freeze.py diff --strict-cjk` core vs this edition: **TOTAL added
  CJK characters: 0** (exit 0). All Simplified Chinese core text is
  byte-identical in substance; CJK counts fall only where English strings
  were replaced.
- Phrases of the week: all 8 exactly 2× (article + P7) in the final SVGs
  (joined-text counting).
- Photo credits kept in English (W45 precedent). Pinyin kept; English
  glosses translated.

## Adjudications (for the independent proofreader)

- **Badge is Latin-only:** the core badge's Chinese half (“简体中文正文 ·
  英语讲解”) is replaced wholesale by the Latin badge, per the W45 ES
  precedent — otherwise naming the reader language in Chinese would add
  CJK characters the core does not have and fail strict-CJK. No Chinese
  reader-facing label for the explanation language is printed.
- **Exercise head shortened:** “B · 词语填空 · Huecos de vocabulario” →
  “B · 词语填空 · Huecos” (HEAD TOO WIDE on P2–P6 in build 1; the wide
  head also overlapped the first exercise line below it — 4 TEXTX flags —
  all cleared by the one shortening).
- **Box titles shortened:** “数字看本周 · Cifras de la semana”,
  “本周生活小日历 · Fechas clave”, “看比赛的中文 · Palabras clave”,
  “这一周的高频词 · Palabras clave” (BOXTITLE flags in build 1; the P4
  and P5 boxes share the Spanish title “Palabras clave” — their Chinese
  titles differ).
- **Comma-after-CJK:** two Spanish notes were reworded to use “—” instead
  of a comma directly after a CJK character (e.g. “Los paquetes llevan
  个 — no 只 ni 条.”), because the typesetter converts such commas to
  full-width “，” and that would add a CJK character under strict-CJK.
- **P7 B1 example:** the Spanish explanation keeps the English example
  sentence (“So English «Monday, Nov 9» becomes …”), as in W45.

## Gates (final render)

- Driver: TOTAL 150, levels A2 56 / B1 69 / B2 25, pages
  10/18/18/18/18/18/12/38, writing model 164 characters, **zero** FLOW
  OVERFLOW / HEAD TOO WIDE warnings (terse notes from the start: the P8
  keys simulation ends at y = 2279, bottom 2540, 153 wrapped lines).
- Occlusion audit (`tools/occlusion_audit.py`, selftest first): **0 flags**.
- Same-baseline ink-collision scan (`hidden_files/w46/rowcheck.py` §1):
  all 8 pages CLEAN (§2 hardcodes the NL P6 filename and does not run for
  this family; P6 chart rects verified directly: 220/330/550/770 px from
  x=325).
- `tools/p8.py extract --total 150`: noted set = 150 of 150.
- `tools/p8.py compare` core vs edition P8: status CLEAN (missing = [],
  extra = 0, keydiff = []).
- `tools/freeze.py diff --strict-cjk`: added CJK = 0 (see above).
- Web PDF (`tools/webpdf.py`): `Lucerna-VOL3-ES-web.pdf`, 2,497,496
  bytes (< 7 MB); `pdftotext` output byte-identical to the print PDF
  (`Lucerna-VOL3-ES.pdf`, 42,127,062 bytes), 45,811 text bytes. Print PDF
  kept in the edition dir.
- Visual check: P8 card read in full after the final render (keys end
  cleanly above the footer rule); P1/P2 cards spot-checked for the fixed
  box-title areas.
- Files: 8 SVGs in `svg/`, 8 cards PNG, print + web PDFs, `ABSTRACT.txt`
  (Spanish), `2026-w46-zh-cn-es.text.md` (exported from the source
  manuscript with `hidden_files/w46/textmd.py`, never from PDF), this KIT.

## Reproduction

```bash
cd hidden_files/weekly-report-w46-zh-cn-es-build
../../tools/venv/bin/python run.py
../../tools/venv/bin/python render.py
cd ../../tools
./venv/bin/python occlusion_audit.py --selftest
./venv/bin/python occlusion_audit.py ../files/weekly-report-w46-zh-cn-es
./venv/bin/python p8.py extract --p8 ../files/weekly-report-w46-zh-cn-es/svg/p8-ceyan.svg --total 150
./venv/bin/python p8.py compare --core-p8 ../files/weekly-report-w46-zh-cn-core/svg/p8-ceyan.svg --edition-p8 ../files/weekly-report-w46-zh-cn-es/svg/p8-ceyan.svg --total 150
./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w46-zh-cn-core/svg --edition-svg ../files/weekly-report-w46-zh-cn-es/svg --strict-cjk
./venv/bin/python webpdf.py ../files/weekly-report-w46-zh-cn-es/svg ../files/weekly-report-w46-zh-cn-es/Lucerna-VOL3-ES-web.pdf
python3 ../w46/textmd.py 2026-w46-zh-cn-es ../files/weekly-report-w46-zh-cn-es/2026-w46-zh-cn-es.text.md
```

To rebuild from the core: copy the core build dir, repoint OUT paths to
`files/weekly-report-w46-zh-cn-es/svg`, apply `hidden_files/w46/maps/
es.json` with `hidden_files/w46/transform.py`, then run as above.

## Post-proof fix record

None yet. Independent proofreading is still owed.
