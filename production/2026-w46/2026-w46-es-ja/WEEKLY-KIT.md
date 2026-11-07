# WEEKLY-KIT · 2026-w46-es-ja — La Lucerna, Spanish Weekly VOL.3, explanations in Japanese

Slug: `2026-w46-es-ja`. Issue week: Mon 9 – Sun 15 Nov 2026. Frontmatter week: `2026-W46`.
Target language: Spanish (all article text frozen from the W46 core). Explanation layer: Japanese, written natively.
Build dir: `hidden_files/weekly-report-w46-es-ja-build/` (copy of the W46 core build; transform tables `hidden_files/w46/t_ja.py` + `t_ja2.py`, applied by `hidden_files/w46/build_one.py`).

## 1. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38.
8 pages, 1950×2700. Final build log: zero FLOW OVERFLOW / zero HEAD TOO WIDE.
Print PDF `La-Lucerna-VOL3-JA.pdf` 17,666,248 B (JP font embedding); web PDF `La-Lucerna-VOL3-JA-web.pdf` 1,215,153 B (<7 MB), text layer 48,185 B via `pdftotext`, byte-identical to the print PDF's text.
`.text.md` exported from this edition's own SVG text layer (never from PDF).

## 2. Face + furniture (W45 ES×JA, VOL.1→VOL.3 only)

- JP face transplanted from the W45 ES×JA build into `svglib.py` (transform pairs in `t_ja.py`): `_sc_index`→JP suffix check, family names `Noto Serif/Sans CJK SC`→`JP`, kinsoku `NO_START` block (incl. small kana, oidashi + seam repair, `SEAM_SLACK = 28`) inserted after the `wrap()` tail anchor. Verified against the W46 core `svglib.py` before building.
- Badge replaces the y=372 subtitle slot, 19.5pt: `スペイン語テキスト · 日本語の解説 — 日本語読者のための版`.
- Edition line: `ス ペ イ ン 語 週 刊 · VOL.3 · LA HUELGA · LA CAMPAÑA · LA ROJA` (spaced katakana per W45).
- Top strip: `CADA SEMANA EN ESPAÑOL · 毎週一号 · スペイン人が読んでいるスペイン語を読む`.
- Band right: `29-Nまであと20日 · 住宅が選挙戦を決める` / `今号のトップ · 詳しくは2・6ページ`.
- Footer: `La Lucerna · スペイン語週刊 VOL.3 · 本文はスペイン語 · 解説は日本語` + `N ページ（全 8 ページ）`.
- Bands: VIDA · 暮らし / CULTURA · 文化 / DEPORTE · スポーツ / JUVENTUD · 若者 / A FONDO · 深掘り / LENGUA · ことば / EJERCICIOS Y RESPUESTAS · 練習と答え.
- Box titles: LA NOTICIA · トップ記事, LA SEMANA EN CIFRAS · 今週の数字, AHORA TÚ · すぐ練習, 五大見どころ · Para entender la semana, EN ESTA EDICIÓN · 今号の目次, BREVES · 短報, QUIZ RELÁMPAGO · クイズ, EJERCICIOS · Nページの練習, exercise right note `答えは8ページ · レベル混合の問題もあります。番号で探してください`, ¿Y TÚ? · あなたは？, ERRORES TÍPICOS · よくある間違い (23pt, core size kept), LA PALABRA · 今週の単語, FRASES DE LA SEMANA · 今週の文（今号の記事から一字一句そのまま）, LA PRÓXIMA SEMANA · 次号予告 (VOL.4).
- Gloss prefix `解説 — `; `bridge()` → `expl()`.
- P8 header: `RESPUESTAS · 全解答と解説（1–8ページ）` / `各問に日本語の解説つき · ✓ は模範文のある問題`; separators `— N ページ —`; P7 band `ことば特集 · Tres niveles, tres herramientas · 三つのレベル、三つの道具`.
- Plan title `EL PLAN DE LA SEMANA · 今週の計画` tsize=20; word note `「huelga general」：みんなが一日休む。`.
- Disclosure: `編集部：本物の手紙も最優秀作文も届かなかったため、見本の手紙を掲載します。約束はVOL.4へ。手紙をお待ちしています。`
- Type labels: 完成句子→文の完成, 单选→選択問題, 词汇配对→単語のペア, 判断对错→正誤判断, 造句→文を作る, 句型转换→文の書き換え, 完形单选→穴埋め選択, 翻译→翻訳, 写作→作文; instr: 填空→空所補充, 判断→正誤, 造句→文を作る, 改写→書きかえ, 翻译→翻訳, 写作→作文, 把词和释义配对→語と意味を結ぶ; P8 check `== "作文"`.
- Declared unchanged shared-kanji items (W43 §6 precedent, verified present in the diff as unchanged): `文化`, `el cementerio 墓地`, `cementerio = 墓地`, `himno = 国歌`, `原形`, P7 letter full-width attribution `（ejemplo, escrito por la redacción）` with the frozen Spanish letter body.

## 3. Registry verification & key-diff adjudication

`p8.py compare` vs core P8: CLEAN, 150/150, keydiff=[137, 138] — the two translation keys re-aimed to Japanese; all other keys byte-identical. `freeze.py diff` vs core SVGs: added CJK is entirely Japanese (hiragana/katakana/kanji; `cjk_added_total` inspected — no Simplified-only characters); removed CJK is the core's Simplified explanation layer. Removed non-CJK strings are re-wrap fragments only; the JP face measures Latin glyphs marginally differently, moving line breaks (W45 JA precedent).

## 4. Gates (final render)

- Builder self-check: 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; 150 exercises; `p8.py extract` 150/150.
- `tools/occlusion_audit.py`: 0 flags (`hidden_files/w46/es-ja-occlusion.json`, selftest passed).
- Same-baseline furniture scan + chart GRAZE element-check (`hidden_files/w46/checks.py`): 7 rowcheck reports, all P1 contents-list 4.0px gaps — the core pattern, no overlap; chart 0 overlaps.
- Web PDF text layer: 48,185 B, identical to print text; <7 MB.
- Visual: P1, P7 inspected — JP face renders throughout, top strip clear of the date line, kinsoku/seam behaviour correct on P7 (no line-initial forbidden punctuation; quote tags intact), letters box with disclosure inside, preview band clear of the footer rule.

## 5. Fixups (Japanese apparatus only; core geometry and Spanish text untouched)

1. First build: P6 exercise flow overflow (3 FLOW OVERFLOW lines, 18 occlusion flags — all P6 spill onto the footer). Fixed: P6 exercises 19pt/gap3 → 18.5pt/gap2 (EN/FR/IT/NL/RU precedent). No P6/P8 size reductions were pre-applied for JA (Japanese text is compact); the P8 answers needed no reduction. Rebuilt: 0 flags.
2. Core letters-box fix inherited via rebuild from the fixed core build.

## 6. Promises, sources, credits

As in the core: 13 Nov campaign start and 29 Nov vote lead the issue; the unverified 12 Nov decree date was NOT reintroduced; reader letters: labelled editor's example (Ana) + bilingual disclosure, promise carried to VOL.4, no reader fabricated. Sources, image credits and the full article record: see the core KIT `files/weekly-report-w46-es-core/WEEKLY-KIT.md`.

## 7. Reproduction

`python3 hidden_files/w46/build_one.py ja t_ja` (copies the fixed core build, applies `t_ja.py` + `t_ja2.py`, runs `run.py`, renders via `tools/venv`, gates freeze/p8/occlusion). Gate outputs: `hidden_files/w46/es-ja-diff.json`, `es-ja-p8-compare.json`, `es-ja-occlusion.json`, `es-ja-build.log`; gate record in `hidden_files/w46/es-gates.log`. Independent proofread (§8.4 SOP) still outstanding — do not claim finalisation.
