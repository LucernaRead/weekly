# Re-proof note — 2026-w47-ru-zh-tw (independent, 2nd round)

- **Edition:** `2026-w47-ru-zh-tw` (reader: Traditional Chinese; source: Russian)
- **Proofer:** independent re-proof (did not build this edition). Read: all 8 print-PDF pages
  (text extraction + full-page visual renders), the full `text.md` (838 lines), and the web PDF
  (text layer + P8 visual render).
- **Scope note:** this round follows the one-line Fix 1 (`ru_textmd.py:616` exporter bug):
  text.md L836 long form → `✓` form, matching print P8. Print/web PDFs were NOT rebuilt by the fix.

## Verdict: (b) — ONE finding

| # | Location | Finding | Evidence |
|---|---|---|---|
| F1 | Print P8 answers, key **58**; text.md Q58 exercise line (L≈346) and appendix line 58 | Team-name typo: **克拉斯諾輔達爾** — an extra **輔** inserted into the Krasnodar transliteration. Correct form is **克拉斯諾達爾**, used everywhere else in this same edition. | Print P8 (render + text layer): `58. a — 克拉斯諾輔達爾 a`. text.md: `58. «Краснодар» — победил ЦСКА 4:2 (key a · 克拉斯諾輔達爾 a)` and appendix `58. a — 克拉斯諾輔達爾 a`. Source string: `content34.py:235` — `["火車頭 b", "克拉斯諾輔達爾 a", "斯巴達克 c", "澤尼特 d"]`. Correct form in this edition: P4 section head `СБОРНАЯ: ТАШКЕНТ И КРАСНОДАР　國家隊：塔什干與克拉斯諾達爾`; keys 48 (`焦點戰週六：克拉斯諾達爾 4:2`), 51 (`國家隊週二 19:00 在克拉斯諾達爾比賽`), 124 (`克拉斯諾達爾 4:2 勝中央陸軍`); `content8.py:39`. Scope: zh-tw only — repo-wide grep for `輔達爾` over `production/2026-w47/` (`*.py/*.md/*.json/*.txt`) hits only this edition's `content34.py` + `text.md`; core-ru and the other fan-outs do not carry it. |

Fix for F1 (coordinator): one character deletion in `content34.py:235` (`克拉斯諾輔達爾` →
`克拉斯諾達爾`), then re-export text.md + rebuild P8/print/web. Text and print agree with each
other, so this is a content typo, not a text-vs-print mismatch.

## SHA-256 (start and end of read — unchanged)

| File | Size | SHA-256 start | SHA-256 end |
|---|---|---|---|
| `2026-w47-ru-zh-tw.text.md` | 60,856 B | `76d599d5f6d51014bc9dca019c683f9d41bb4f34c13ca81ea7771c0503b120be` | same |
| `Lucerna-VOL4-ru-zh-tw.pdf` (print) | 24,784,766 B | `2d19ad648194eeceeb03ddf9dd313326a51dd5f077ce9e9b0ae65753caeb42b4` | same |
| `Lucerna-VOL4-ru-zh-tw-web.pdf` (web) | 3,995,346 B | `91ded0180e2287d7ff9311d329453c1a557be8db9a4009908ab5e24eb7163bab` | same |

- text.md SHA matches the brief's expected value exactly (`76d599d5…`, 60,856 B) — read proceeded.
- Print SHA unchanged mid-read (no stop required). Web SHA unchanged between start and end
  reads — web verdict is NOT deferred; web P8 was rendered and checked visually.
- KIT comparison (§1): print SHA **matches KIT**; text.md SHA **matches KIT**; web SHA **differs
  from KIT** (`991b22ab…`, 3,995,314 B) — known drift, not a defect: the pre-insert web-PDF rebuild
  rewrote all 9 ru web PDFs (KIT §9 Fix-1 note). Flagged here for the coordinator's KIT-sync wave.

## Fix-1 verification (the reason for this re-proof)

- text.md L836 byte-equals the brief's new line: `150. ✓ 範文見本版 H 區（97 詞）` — verified
  by `sed -n '836p'` and by Python read.
- Print P8 contains the identical line: `150. ✓ 範文見本版 H 區（97 詞）` — verified in the
  extracted text layer and in the P8 visual render. L836 == P8 Q150 line. ✓
- The old long form `（開放題，範文如下）` is gone from the appendix; the question-line key at
  Q150 (`— key: （開放題，範文如下） (範文見本版 H 區（97 詞）)`) is unchanged, as intended
  (the fix touched only the appendix line).
- H sample essay word count re-counted: **97 words** excluding the `Пример:` label (98 tokens
  including it) — matches the stated `(97 詞)`. ✓

## Appendix keys 1–150 vs printed P8 keys

- text.md appendix: 150 keys, contiguous 1–150. ✓
- Programmatic comparison (whitespace-squashed) of every appendix line against the P8 text
  layer: **148/150 full-line matches**; the other 2 (79, 100) are pdftotext column-interleave
  artifacts only — the P8 render shows both lines intact
  (`79. Сначала список, потом цены, потом промокод. — 先清單，後價格，再折扣碼`;
  `100. Люди проверяют посылки или возвращают покупки. — или = 或者`). **150/150 match in
  substance.** ✓
- Keys 137–140 in Traditional comma form, matching KIT §6: 137 `11月17日星期二，大學生節。`,
  138 `包裹要追蹤、領取並檢查。`, 139 `星期二俄羅斯隊對陣委內瑞拉隊。`,
  140 `祝大家大學生節快樂！` ✓

## Page-by-page notes (print PDF, visual + text)

- **P1:** Head `14-й тур: «Зенит» и «Динамо» — по 31 очку`, kicker double-spaced after core fix1
  (renders with clear word gaps); lead, `ТУР В ЦИФРАХ`, word-of-week `чёрная пятница =
  黑色星期五（年末大促）。`, `БЛИЦ-ВИКТОРИНА` Q7–10, photo + caption, footer `第1版／共8版`.
  No overflow/overlap. ✓
- **P2:** Holidays list, weather words, Q11–28, Yuon painting + caption. Gloss boxes each carry a
  single `譯注｜` prefix. `Четыре слова о ноябрьской погоде` band. No defects. ✓
- **P3:** Cinema premieres, glosses single `譯注｜`, Q29–46, matching keys 39–42 (b/d/c/a). ✓
- **P4:** Results tables (14th round + 15th round fixtures), national-team box, 1912 photo +
  caption, Q47–64, gloss `сравняли счёт 扳平比分 · поправка 更正 · в зоне вылета 處於降級區。`
  wraps cleanly (L2 ends `級區。`, no dangling 。). ✓
- **P5:** Black Friday, market photo + caption, dates box, Q65–82, pairing keys 75–78 = d/b/a/c
  (core fix verified). ✓
- **P6:** Week calendar strip (16–22, 21–22 highlighted), practice-data chart 38/26/18/18 with
  the `不是真實調查` disclaimer, Q83–100. ✓
- **P7:** Three-level language focus, error clinic (4 items), word box
  `распродажа = 大促銷，要計劃，別急。`, Pushkin portrait + caption, reader-letters box —
  `поздравлю друга-студента` renders correctly (earlier `��` was a transcript-display artifact;
  text layer has 0 U+FFFD, SVG source clean), phrases of the week with page refs, VOL.5 preview.
  ✓
- **P8:** Test Q113–150, answers 1–150 (see appendix check), H writing task + 97-word sample
  essay, `Морозко` Bilibin image + caption present, footer `第8版／共8版`. Only defect on this
  page is F1 (key 58). ✓ otherwise.

## Web PDF

- Text layer **byte-identical** to print (`pdftotext -layout`, 104,493 bytes each; per-page char
  counts identical; `diff` clean). Same as print on the Fix-1 note: web P8 render is visually
  identical to print P8 (same layout, same F1 typo, same Q150 ✓ line, Morozko image present).
- Web PDF was read from the final on-disk file (SHA `91ded018…`, stable across this read).

## Other checks

- Simplified-character sweep (common simplified-only forms) over text.md and the print text
  layer: **NONE**. `塔什干`'s `干` is the established transliteration exception (KIT §5). ✓
- Text layer: 0 U+FFFD in print and web; no tofu observed in any rendered page. ✓
- Exercise-answer spot cross-checks (keys against stems/articles/charts): Q20 `желании`
  (core D6 fix present), Q48/Q124 Krasnodar 4:2, Q58's *answer letter* `a` is correct
  (Krasnodar did beat CSKA 4:2) — only the Chinese team-name note is mistyped (F1).
- P8 min font / occlusion / freeze gates were not re-run (read-only brief; KIT gates stand).

## Checked and NOT flagged (established non-defects)

- Narrow CJK word spaces that look joined at page scale (`От редакцииLucerna`,
  `российскимСМИ`, `Профессиональныепраздники`, `синоптикиобещают`, `можетбыть`,
  `результатов+ сборная`): core KIT §7.2 item 9 adjudicated this class a non-defect
  (pixel-measured 4–5px gaps, narrow Noto Sans CJK SC space, same as shipped W46); carried
  over by this edition's KIT §5/§7. Space elements exist in the SVGs.
- Chinese character-level line breaks (`截|至`, `濕|雪`): normal typography (KIT §5).
- P1 y1712 same-baseline collision `чёрная`: same as core (KIT §5).
- `— СТРАНИЦА ? —` in text.md appendix header: known exporter artifact, core ruling (KIT §5).
- P7 orphan line-starts (end/mid-line punctuation): false positives, same class as core (KIT §5).

## Files written (only one)

- `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-ru-zh-tw1/PROOF-NOTE.md` (this file). No production file modified; no PDFs copied; no re-render of the edition; no commit/push/lint. Temp renders in `/tmp/ruzhtw/` deleted after use.
