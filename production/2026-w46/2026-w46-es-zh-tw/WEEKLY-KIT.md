# WEEKLY-KIT · 2026-w46-es-zh-tw — La Lucerna, Spanish Weekly VOL.3, explanations in Traditional Chinese

Slug: `2026-w46-es-zh-tw`. Issue week: Mon 9 – Sun 15 Nov 2026. Frontmatter week: `2026-W46`.
Target language: Spanish (all article text frozen from the W46 core). Explanation layer: Traditional Chinese (Taiwan/HK usage), written natively — NOT mechanically converted from Simplified.
Build dir: `hidden_files/weekly-report-w46-es-zh-tw-build/` (copy of the W46 core build; transform tables `hidden_files/w46/t_zhtw.py` + `t_zhtw2.py`, applied by `hidden_files/w46/build_one.py`).

## 1. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38.
8 pages, 1950×2700. Final build log: zero FLOW OVERFLOW / zero HEAD TOO WIDE.
Print PDF `La-Lucerna-VOL3-ZH-TW.pdf` 17,654,406 B (TC font embedding); web PDF `La-Lucerna-VOL3-ZH-TW-web.pdf` 1,378,198 B (<7 MB), text layer 44,914 B via `pdftotext`, byte-identical to the print PDF's text.
`.text.md` exported from this edition's own SVG text layer (never from PDF).

## 2. Face + furniture (W45 ES×ZH-TW KIT §2, VOL.1→VOL.3 only)

- TC face: 4 `svglib.py` changes (`_sc_index`→`_tc_index`, suffix `SC`→`TC`, `_IDX` call, family names `Noto Serif/Sans CJK SC`→`TC`) + docstring `重阳`→`重陽` (verified present in the W46 core `svglib.py`).
- Badge occupies the y=372 slot, 19.5pt sans bold BRICK: `西班牙語正文 · 繁體中文講解 — 給繁體中文讀者的版本`.
- P1 name line: `西 班 牙 語 週 報 · VOL.3 · LA HUELGA · LA CAMPAÑA · LA ROJA`.
- Top strip: `CADA SEMANA EN ESPAÑOL · 每週一期 · 讀西班牙人正在讀的西班牙語`.
- Footer: `La Lucerna · 西班牙語週報 VOL.3 · 正文西班牙語 · 講解繁體中文`; page line `第 {n} 版 / 共 8 版` (unchanged from core).
- Band titles: VIDA · 生活 / CULTURA · 文化 / DEPORTE · 體育 / JUVENTUD · 青年 / A FONDO · 深讀 / LENGUA · 語言 (right subtitles in Traditional).
- Gloss prefix `譯注｜` (bslib4 gloss prefix pair + P1 explanation line, which also becomes `譯注｜`).
- `bridge()` → `expl()`; P8 header left `RESPUESTAS · 全部答案與簡析（第 1–8 版）` / right `每題附一句中文簡析 · 帶 ✓ 的為範本題` (already the core's strings); P8 separator `— 第 {pg} 版 —`.
- Explanation-layer quotation marks “” → 「」 (W43 ruling; W46 occurrences: P1 word note `「大罷工」`, P6 `「將要」`).
- Type names in Traditional: 單選 / 詞彙配對 / 判斷對錯 / 句型轉換 / 完形單選 / 翻譯 / 寫作 (完成句子 / 造句 unchanged in form); P8 check `== "寫作"`.
- Disclosure (Traditional): `編輯部說明：截至本期截稿，未收到真實讀者來信與第 8 版最佳作文，故本期登載編輯部示例信，承諾順延至 VOL.4。歡迎來信！`

## 3. Registry verification & key-diff adjudication

`p8.py compare` vs core P8: CLEAN, 150/150, keydiff=[137, 138] — the two translation keys re-aimed to Traditional Chinese; all other keys byte-identical. `freeze.py diff` vs core SVGs: removed CJK = Simplified-only characters, added CJK = Traditional-only characters, shared characters stay; no Simplified-only character appears in the added set (verified programmatically: 0 hits against a Simplified-only probe set). Per-page CJK totals: core 180/295/155/176/238/80/412/964 → edition 216/307/169/188/252/92/424/985.

## 4. Gates (final render)

- Builder self-check: 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; 150 exercises; `p8.py extract` 150/150.
- `tools/occlusion_audit.py`: 0 flags (`hidden_files/w46/es-zh-tw-occlusion.json`, selftest passed).
- Same-baseline furniture scan + chart GRAZE element-check (`hidden_files/w46/checks.py`): 7 rowcheck reports, all P1 contents-list 4.0px gaps — the core pattern, no overlap; chart 0 overlaps.
- Web PDF text layer: 44,914 B, identical to print text; <7 MB.
- Visual + text check: P1, P7 inspected — TC face renders throughout with no missing glyphs, Traditional forms verified in the `.text.md` export (0 Simplified-only characters; 讀/說/這/讓/議 present), top strip clear of the date line, letters box with disclosure inside, preview band clear of the footer rule. No P6/P8 size reductions were needed.

## 5. Fixups

None beyond the furniture/face transform. Core letters-box fix inherited via the build from the fixed core build.

## 6. Promises, sources, credits

As in the core: 13 Nov campaign start and 29 Nov vote lead the issue; the unverified 12 Nov decree date was NOT reintroduced; reader letters: labelled editor's example (Ana) + bilingual disclosure, promise carried to VOL.4, no reader fabricated. Sources, image credits and the full article record: see the core KIT `files/weekly-report-w46-es-core/WEEKLY-KIT.md`.

## 7. Reproduction

`python3 hidden_files/w46/build_one.py zh-tw t_zhtw` (copies the fixed core build, applies `t_zhtw.py` + `t_zhtw2.py`, runs `run.py`, renders via `tools/venv`, gates freeze/p8/occlusion). Gate outputs: `hidden_files/w46/es-zh-tw-diff.json`, `es-zh-tw-p8-compare.json`, `es-zh-tw-occlusion.json`, `es-zh-tw-build.log`; gate record in `hidden_files/w46/es-gates.log`. Independent proofread (§8.4 SOP) still outstanding — do not claim finalisation.
