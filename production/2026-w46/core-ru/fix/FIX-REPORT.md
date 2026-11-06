# FIX REPORT — Lucerna Weekly W46 RU family (VOL.3), Round 1 defects D1–D3
## Fix worker, 2026-11-02 (America/Toronto). Local only: no push, no insert, no Discord, no index.json, no ~/workspace/weekly-git. A Round 2 independent proofread follows; this report's re-gating does not replace it.

## Sources changed (at the source only; no SVG/PDF hand-edits)

### D1 — core build source
- `hidden_files/weekly-report-w46-ru-build/content56.py`, P5 block C `match_set` (ex. 75–78).
- `hidden_files/w46/ru_maps.py`, per-language P8-key note pairs in all 10 fan-out specs (the same transposition, encoded as note strings `退货 a` / `促销码 b`).

### D2 — fan-out translation map
- `hidden_files/w46/ru_maps.py` only: the two bridge strings in the affected specs (see §D2). Core build source untouched for D2; clean editions' map entries untouched.

### D3 — fan-out translation map (ja only)
- `hidden_files/w46/ru_maps.py`, ja spec: the two fragments of the P8 H-note bridge.

## D1 — P5 matching exercise C, key letters 76/77 transposed (BLOCKING, all 11)

Before (core `content56.py`):
```
["посылка", "возврат", "промокод", "пик"],
["код со скидкой", "товар возвращают в магазин", "самое большое число заказов", "товар, который прислали по почте"],
["d", "a", "b", "c"],
["包裹 d", "退货 a", "促销码 b", "高峰 c"],
```
After:
```
["посылка", "возврат", "промокод", "пик"],
["код со скидкой", "товар возвращают в магазин", "самое большое число заказов", "товар, который прислали по почте"],
["d", "b", "a", "c"],
["包裹 d", "退货 b", "促销码 a", "高峰 c"],
```
P5 block itself (words + options) unchanged. Correct matches: 75 посылка→d (товар, который прислали по почте), 76 возврат→b (товар возвращают в магазин), 77 промокод→a (код со скидкой), 78 пик→c (самое большое число заказов).

Before (rendered P8 key, core): `76. a — 退货 a`, `77. b — 促销码 b`.
After (rendered P8 key, core): `76. b — 退货 b`, `77. a — 促销码 a`.
Before (manuscript registry, core `.text.md` §C): `76. возврат — код со скидкой (key a · 退货 a)`, `77. промокод — товар возвращают в магазин (key b · 促销码 b)`.
After: `76. возврат — товар возвращают в магазин (key b · 退货 b)`, `77. промокод — код со скидкой (key a · 促销码 a)`.
Before (ru_maps.py, every fan-out spec): `('退货 a', '<word> a')`, `('促销码 b', '<word> b')`.
After: `('退货 b', '<word> b')`, `('促销码 a', '<word> a')` — full per-language list in the fix log below. (Without this second change the transform would have failed its "MAP KEY NEVER FOUND" assertion, since the source notes now read `退货 b` / `促销码 a`.)

Semantic re-verification of all five matching blocks — see §Matching blocks.

## D2 — displaced wrapped instruction lines (BLOCKING)

Root cause: `Flow.para`/`bridge` (bslib4.py) wraps the instruction to two lines; when only one line fits at the bottom of column 1, the second line flows to the top of column 2 (x=527, y≈1656/1696), ~900 px from its home line. Fix: shorten each affected instruction to fit one 434 px column line (widths measured with the build's own PIL/Noto metrics at 20.5 pt sans; every replacement wraps to exactly 1 line). No geometry change; clean editions untouched.

### D2a — P3 block B bridge (verdict labels it block C; the string is the bridge under head `B · ГЛАГОЛЫ И ФОРМЫ`, content34.py:72)
Source key: `用动词的正确形式或正确的格填空。`

| Ed. | Before (orphan at 527, 1696.5) | After (single line at 65, 2564.45) |
|---|---|---|
| de | `Füllen Sie die Lücken mit der richtigen Verbform oder dem richtigen Kasus aus.` / orphan `Verbform oder dem richtigen Kasus aus.` | `Setzen Sie Verbform und Kasus richtig ein.` |
| en | `Fill in the gaps with the right verb form or the right case.` / orphan `right case.` | `Fill in the right verb form or the right case.` |
| es | `Completa con la forma verbal correcta o el caso correcto.` / orphan `caso correcto.` | `Completa la forma verbal o el caso correcto.` |
| fr | `Complétez avec la bonne forme du verbe ou le bon cas.` / orphan `le bon cas.` | `Complétez la bonne forme verbale ou le cas.` |
| it | `Completa con la forma verbale giusta o il caso giusto.` / orphan `caso giusto.` | `Metti la forma verbale o il caso giusti.` |
| nl | `Vul in met de juiste werkwoordsvorm of de juiste naamval.` / orphan `juiste naamval.` | `Vul in: juiste werkwoordsvorm of naamval.` |
| pt | `Complete com a forma verbal correta ou o caso correto.` / orphan `caso correto.` | `Complete a forma verbal ou o caso correto.` |

Clean for D2a (untouched): zh-cn (core), ja, ko, zh-tw.

### D2b — P4 block B bridge (content34.py:182, under head `B · КАЛЕНДАРЬ И ДАТЫ`)
Source key: `用第 4 版的数字和词填空。`

| Ed. | Before (orphan at 527, 1656.5) | After (single line at 65, 2553.45) |
|---|---|---|
| de | `Füllen Sie die Lücken mit Zahlen und Wörtern von Seite 4 aus.` / orphan `von Seite 4 aus.` | `Zahlen und Wörter von Seite 4 einsetzen.` |
| en | `Fill in the gaps with numbers and words from page 4.` / orphan `page 4.` | `Fill in with numbers and words from page 4.` |
| es | `Completa con números y palabras de la página 4.` / orphan `página 4.` | `Completa: números y palabras (página 4).` |
| fr | `Complétez avec les chiffres et les mots de la page 4.` / orphan `page 4.` | `Complétez : chiffres et mots de la page 4.` |
| it | `Completa con i numeri e le parole di pagina 4.` / orphan `4.` | `Completa con numeri e parole di pagina 4.` |
| pt | `Complete com números e palavras da página 4.` / orphan `4.` | `Complete: números e palavras da página 4.` |

Clean for D2b (untouched): zh-cn (core), ja, ko, nl (nl instruction already fit one line: `Vul in met cijfers en woorden van pagina 4.`), zh-tw.

Orphan-fragment scan (all pages, all 11 editions): see §Orphan scan.

## D3 — ja P8 H-note kinsoku (MINOR, ja only)

Before (rendered, `p8-test.svg`): line 1 `作文（決まった答えはありません）；模範文（` (ends with dangling `（`), line 2 `87 語）は下にあります。`.
After: line 1 `作文（決まった答えはありません）；模範文は`, line 2 `下にあります（87 語）。` — the bracketed word count now opens and closes inside line 2; no line ends with an opening bracket.
Source (ja map fragments of `f.bridge(f"写作题（无唯一答案）；范文（{NWORDS} 词）见下。")`):
before: `('写作题（无唯一答案）；范文（', '作文（決まった答えはありません）；模範文（')`, `(' 词）见下。', ' 語）は下にあります。')`
after: `('写作题（无唯一答案）；范文（', '作文（決まった答えはありません）；模範文は下にあります（')`, `(' 词）见下。', ' 語）。')`
Wording preserved in meaning: "Essay (no set answer); the model essay is below (87 words)." Line count unchanged (2), so P8 layout below the note is unmoved. Kinsoku scan of the whole ja edition: see §Kinsoku scan.

## Matching blocks — semantic re-verification (all five, option-by-option)

Verified from the build sources (`hidden_files/w46/ru-fix/verify_matching.py`: left → key letter → right text + note; keys a permutation of a/b/c/d per block; note trailing letter = key; same word → same right text across blocks) and from the rendered P8 keys. p8.py CLEAN alone cannot establish this.

- 25–28 (P2, dates → holidays): 25 10 ноября→d День полиции; 26 11 ноября→a День экономиста; 27 13 ноября→b День войск РХБ защиты; 28 15 ноября→c Всероссийский день призывника. Dates cross-checked against the §3 calendar nodes (10 Nov Police Day, 11 Nov Economist Day, 13 Nov RCB Troops Day, 15 Nov Conscript Day). CORRECT, unchanged.
- 39–42 (P3, cinema words): 39 биография→b фильм о жизни реального человека; 40 стриминг→d фильмы смотрят дома через интернет; 41 сеанс→c показ фильма в кинотеатре; 42 зритель→a человек, который смотрит фильм. CORRECT, unchanged.
- 57–60 (P4, teams → fixtures): 57 «Локомотив»→b играет с «Рубином» в пятницу; 58 «Краснодар»→a играет с ЦСКА в субботу в 19:30; 59 «Спартак»→c играет с «Акроном» в воскресенье в 16:15; 60 «Зенит»→d играет с «Ростовом». Cross-checked against the printed 14th-round fixture table. CORRECT, unchanged.
- 75–78 (P5, FIXED): 75 посылка→d товар, который прислали по почте; 76 возврат→b товар возвращают в магазин; 77 промокод→a код со скидкой; 78 пик→c самое большое число заказов. Right texts identical to the P8 block for the shared words (посылка, пик).
- 141–144 (P8, week words): 141 предзимье→c время между осенью и зимой; 142 посылка→d товар, который прислали по почте; 143 пик→a самое большое число заказов; 144 гололедица→b лёд на дороге. CORRECT, unchanged.

## Render + gates

Rebuild: `hidden_files/w46/ru-fix/rebuild.sh` — core `run.py` + `render.py`, then per language `ru-transform.py` + `run.py` + `render.py`, sequential. Logs: `hidden_files/w46/ru-fix/logs/ru-core-run.log`, `ru-<lang>-transform.log`, `ru-<lang>-run.log` (builder's original logs in `hidden_files/w46/` untouched). Every edition: run exit 0, transform exit 0, render exit 0, TOTAL 150, levels A2 51 / B1 75 / B2 24, pages 10/18/18/18/18/18/12/38, model words 87, **0 FLOW OVERFLOW / HEAD TOO WIDE**.

`.text.md` regeneration: `hidden_files/w46/ru-fix/regen_textmd.sh` (`ru_textmd.py` AST walk + `ru_kit.py` titles/writing types), diffed before installing. Every diff contained ONLY the intended lines: D1 registry + Answers lines (all 11), D2 bridge lines (affected editions), ja H-note line (ja). Headers preserved verbatim. Core file copied to the zh-cn filename; `cmp` verifies byte-identity (52,661 bytes each).

Re-gates (`hidden_files/w46/ru-fix/gates.sh`, JSONs/logs under `hidden_files/w46/ru-fix/`; log `logs/ru-fix-gates.log`):

- **Web PDFs** (`tools/webpdf.py` only): 8 pages each, print-vs-web text identical after whitespace normalisation, pdftotext bytes > 0, all ≤ 7 MB (sizes in §Inventory).
- **Occlusion audit** (`tools/occlusion_audit.py`): 0 flags in all 11 editions; selftest OK ×11 (planted classes BOXTEXT/COVER/EDGE/FOOTER/LINEX/TEXTX all fired; clean controls silent). JSONs: `occlusion-fix-<lang>.json`.
- **`check_core.py`** (invoked with the edition-dir argument): all 11 — golden BAD 0, gloss fails 0, orphan line-starts `[]`, same-baseline collisions 0.
- **`p8.py compare`** vs core: CLEAN 150/150 in all 10 fan-outs, keydiff `[137, 138, 139, 140]` adjudicated (E-section translations into the reader language, by design). `p8.py extract` on the core: noted set 150 of 150.
- **Freeze** (`tools/freeze.py diff` vs core, JSONs `freeze-fix-<lang>.json`, plus `--strict-cjk` for ja/ko/zh-tw): zero added Cyrillic words in every edition — per-page word-level analysis (`freeze_word_analysis.py`, logs `logs/word-analysis-<lang>.txt`) shows TOTAL ADD `{}` for all 10 fan-outs (removals are the translated explanation strings, by design). Char totals: Latin editions han=0 kana=0 hangul=0; ja hangul=0, 2 core Han nodes survive verbatim (生活, 文化), strict-CJK exit 1 adjudicated (added chars are native Japanese script only; 6 shared shinjitai chars are flagged Simplified-only by opencc); ko han=8 (brackets 『』 only), kana=0, 0 core Han nodes survive; zh-tw 109 core Han nodes survive verbatim, zero Simplified-only chars among added Han. Core self-diff control (core vs itself): 0 added/removed strings, 0 added CJK, word ADD/REM both `{}`.
- **P6 chart** (`chart_check.py`, log `logs/chart-check.txt`): all 11 — bars at x=685 widths 600/343/286/200 for 42/24/20/14%, labels sum to 100%.
- **P7 phrases**: per-page freeze ADD `{}` on p7 in every edition — the Russian text is verbatim.
- **Counts re-measured**: 150 / per-page and level splits as above, from every run log.

## Orphan scan

`hidden_files/w46/ru-fix/orphan_scan.py` over all 8 SVGs of all 11 editions (88 pages): 20.5 pt grey nodes at column starts (x=527/989/1451) in the y 1600–1800 band whose immediately preceding document-order node is a home line at (65, y>2400). **TOTAL ORPHANS: 0.** Log: `logs/orphan-scan.txt`. The only band-hits are the legitimate, pre-existing P5 D-head bridges directly under their heads at (989, 1747.5) in all 11 editions (e.g. core `把词组成正确的句子。`, en `Put the words in the right order.`), reported separately and not orphans. The D2 home lines were verified at (65, 2564.45) P3 / (65, 2553.45) P4 as complete single lines in every affected edition.

## Kinsoku scan

`hidden_files/w46/ru-fix/kinsoku_scan.py` over all SVGs of all 11 editions (nodes ending with an opening bracket `（(［｛〈《「『【` or starting with a closing punctuation mark). **TOTAL KINSOKU HITS: 0** in ja (log `logs/kinsoku-scan-ja.txt`) and 0 in the other 10 editions (log `logs/kinsoku-scan-rest.txt`). The D3 fix is confirmed and was the only kinsoku hit in ja. The ja H-note now renders as two lines at x=1451, y=371.12 / 400.845: `作文（決まった答えはありません）；模範文は` / `下にあります（87 語）。`.

## D1 note words per edition (rendered P8 key, verified in each p8-test.svg)

| Ed. | 75 | 76 | 77 | 78 |
|---|---|---|---|---|
| core / zh-cn | d — 包裹 d | b — 退货 b | a — 促销码 a | c — 高峰 c |
| en | d — parcel d | b — return b | a — promo code a | c — peak c |
| de | d — Paket d | b — Rücksendung b | a — Rabattcode a | c — Höhepunkt c |
| fr | d — colis d | b — retour b | a — code promo a | c — pic c |
| es | d — paquete d | b — devolución b | a — código promocional a | c — pico c |
| it | d — pacco d | b — reso b | a — codice promozionale a | c — picco c |
| pt | d — encomenda d | b — devolução b | a — código promocional a | c — pico c |
| nl | d — pakket d | b — retour b | a — kortingscode a | c — hoogtepunt c |
| ja | d — 荷物 d | b — 返品 b | a — プロモコード a | c — ピーク c |
| ko | d — 소포 d | b — 반품 b | a — 프로모 코드 a | c — 정점 c |
| zh-tw | d — 包裹 d | b — 退貨 b | a — 促銷碼 a | c — 高峰 c |

Full extraction: `hidden_files/w46/ru-fix/logs/p8-keys-printed.txt` (75 letter-key lines per edition; the remaining keys are word keys / E translations / writing marks).

## Visual checks (full frame)

Cards read in full: P5 ×11 (block C words/options unchanged, no overflow, footer clear); P3 ×7 (de/en/es/fr/it/nl/pt — instruction complete at the home position, column 2 starts cleanly with ex. 34, no fragment); P4 ×6 (de/en/es/fr/it/pt — same, column 2 starts with ex. 52); P8 ja (H-note re-wrapped, keys 76. b / 77. a visible in the Answers). No defect found on any checked page.

## Per-edition file inventory (final artifacts)

| Edition | .text.md bytes | web PDF bytes | pdftotext bytes (web) | print PDF bytes | SVGs | cards |
|---|---|---|---|---|---|---|
| core (zh-cn) | 52,661 (both files, byte-identical) | 2,719,077 | 53,549 | 24,590,695 | 8 | 8 |
| en | 54,203 | 2,310,183 | 54,684 | 15,001,047 | 8 | 8 |
| de | 54,855 | 2,316,120 | 55,284 | 15,043,291 | 8 | 8 |
| fr | 54,870 | 2,312,371 | 55,349 | 14,964,702 | 8 | 8 |
| es | 55,596 | 2,314,532 | 55,332 | 15,001,970 | 8 | 8 |
| it | 55,223 | 2,311,010 | 55,066 | 15,000,311 | 8 | 8 |
| pt | 56,445 | 2,316,135 | 55,667 | 14,929,875 | 8 | 8 |
| nl | 55,432 | 2,314,264 | 55,280 | 15,041,195 | 8 | 8 |
| ja | 55,116 | 2,736,421 | 55,685 | 22,056,629 | 8 | 8 |
| ko | 55,835 | 2,490,725 | 55,864 | 16,475,626 | 8 | 8 |
| zh-tw | 52,585 | 2,760,278 | 53,507 | 17,941,804 | 8 | 8 |

Web PDF filenames: core `Lucerna-VOL3-web.pdf`; fan-outs `Lucerna-VOL3-<EN|DE|FR|ES|IT|PT|NL|JA|KO|ZH-TW>-web.pdf`. Print PDFs: `Lucerna-VOL3[-<SUFFIX>].pdf`.

## KIT records

A fix record (§10, §§1–9 untouched) was appended to all 11 `WEEKLY-KIT.md` files, with the defect/fix quotes and re-gate evidence per edition. The core KIT's record also covers the zh-cn edition (shared dir/file).

## Fixes NOT applied as specified

None. D1, D2a, D2b and D3 were all applied exactly as the verdict specified, at the source, with full re-render and re-gating. Nothing else was changed: badge fills, P8 Russian separators, "Russia play", W45-promise disclosure wording and all other matching-block keys are untouched, as instructed. No push, no insert, no Discord post, no index.json edit, no `~/workspace/weekly-git` access, no edition content dumped into chat.

## Files under hidden_files/w46/ru-fix/

`FIX-REPORT.md` (this report), `rebuild.sh`, `gates.sh`, `regen_textmd.sh`, `append_kits.py`, `orphan_scan.py`, `kinsoku_scan.py`, `freeze_word_analysis.py`, `chart_check.py`, `verify_matching.py`, `logs/` (rebuild, gates, textmd-regen, orphan/kinsoku/chart/matching/p8-key logs, word-analysis logs), `textmd-tmp/` (pre-install regeneration copies), `occlusion-fix-*.json`, `freeze-fix-*.json` (+ `-strict.json` for ja/ko/zh-tw), `freeze-fix-core-self.json`, `p8-fix-*.json`.
