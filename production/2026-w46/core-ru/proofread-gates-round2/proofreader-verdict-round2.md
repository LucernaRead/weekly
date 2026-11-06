# Round 2 Independent Proofread Verdict — Lucerna Weekly W46, RU target, VOL.3

- **Issue:** W46, dated Mon 2026-11-09 – Sun 2026-11-15, VOL.3, Russian target, ~150 exercises.
- **Proofreader:** independent subagent (did not build or fix these editions). Round 2, 2026-11-02/03.
- **Scope:** all 11 RU-target editions, one per reader-native language: de, en, es, fr, it, ja, ko, nl, pt, zh-cn, zh-tw.
- **Directory rule applied:** `files/weekly-report-w46-ru-core/` is the zh-cn edition's canonical directory (its `.text.md` is byte-identical to the zh-cn export by design; verified `cmp`: both 52,661 bytes). It is NOT a 12th edition.
- **Prior verdict:** Round 1 FAIL (0/11 shippable): D1 BLOCKING (P5 matching C keys 76/77 transposed), D2 BLOCKING (displaced wrapped instruction lines), D3 minor (ja P8 H-note kinsoku dangling bracket).
- **Fix record adjudicated:** `hidden_files/w46/ru-fix/FIX-REPORT.md` + §10 fix records appended to all 11 `WEEKLY-KIT.md` files (verified present in all 11 kits).
- **Work directory (this round):** `hidden_files/w46/ru-proofread-gates-round2/` — gate JSONs/logs in `gates/`, visual crops in `crops/`, extraction script/log in `extract_r2.py`, `extract_r2.log`, `p8-keys-extracted.json`, `kinsoku-hits.json`.
- **Proofreader-only:** no edition file was edited, re-rendered, pushed, or inserted. No defects were fixed by this round. All findings below are verifications or new reports for the fix worker.

## Verdict summary

| Edition (reader native) | D1 | D2a (P3) | D2b (P4) | D3 | New defects | Edition verdict |
|---|---|---|---|---|---|---|
| zh-cn (core dir) | CONFIRMED | n/a (clean) | n/a (clean) | n/a | none | **PASS** |
| de | CONFIRMED | CONFIRMED | CONFIRMED | n/a | none | **PASS** |
| en | CONFIRMED | CONFIRMED | CONFIRMED | n/a | none | **PASS** |
| es | CONFIRMED | CONFIRMED | CONFIRMED | n/a | none | **PASS** |
| fr | CONFIRMED | CONFIRMED | CONFIRMED | n/a | none | **PASS** |
| it | CONFIRMED | CONFIRMED | CONFIRMED | n/a | **D4 BLOCKING** (P8 tofu, keys 51 + 129) | **FAIL** |
| ja | CONFIRMED | n/a (clean) | n/a (clean) | CONFIRMED | none | **PASS** |
| ko | CONFIRMED | n/a (clean) | n/a (clean) | n/a | none (see Observation O1, non-blocking) | **PASS** |
| nl | CONFIRMED | CONFIRMED | n/a (clean) | n/a | none | **PASS** |
| pt | CONFIRMED | CONFIRMED | CONFIRMED | n/a | none | **PASS** |
| zh-tw | CONFIRMED | n/a (clean) | n/a (clean) | n/a | none | **PASS** |

**10 of 11 editions are shippable. The it edition is blocked by one new defect, D4.**

## 1. Fix verification

### D1 — P5 matching C keys 76/77 transposition: CONFIRMED fixed in all 11 editions

Three independent levels verified:

1. **Rendered P8 keys** (extracted from `p8-test.svg`, 13pt nodes, wrap-aware column-grouped re-extraction): all 11 editions render `75. d`, `76. b`, `77. a`, `78. c` with the native note words, e.g. core `76. b — 退货 b` / `77. a — 促销码 a`; en `76. b — return b` / `77. a — promo code a`; de `Rücksendung b` / `Rabattcode a`; fr `retour b` / `code promo a`; es `devolución b` / `código promocional a`; it `reso b` / `codice promozionale a`; pt `devolução b` / `código promocional a`; nl `retour b` / `kortingscode a`; ja `返品 b` / `プロモコード a`; ko `반품 b` / `프로모 코드 a`; zh-tw `退貨 b` / `促銷碼 a`.
2. **P5 block C itself unchanged and correct** in all 11 editions (SVG node text, visually confirmed on all 11 P5 cards): words `75. посылка, 76. возврат, 77. промокод, 78. пик`; options `a. код со скидкой` (= promo code), `b. товар возвращают в магазин` (= return), `c. самое большое число заказов`, `d. товар, который прислали по почте` (+ continuation node `почте`). Correct mapping: 75→d, 76→b, 77→a, 78→c.
3. **Manuscript registry** fixed in all 11 `.text.md` files: line 316 `76. возврат — товар возвращают в магазин (key b · … b)`, line 317 `77. промокод — код со скидкой (key a · … a)`, Answers lines 602–603 `76. b — …`, `77. a — …`.
4. **No residue:** greps for the old patterns (`76. a`, `77. b`, `退货 a`, `促销码 b`, old map pairs `return a` / `Rücksendung a` / `Rabattcode b`, etc.) across all SVGs, all `.text.md` files, and `ru_maps.py` returned nothing. Build source `hidden_files/weekly-report-w46-ru-build/content56.py` line 83: keys `["d", "b", "a", "c"]`, notes `["包裹 d", "退货 b", "促销码 a", "高峰 c"]`; `ru_maps.py` contains 20 occurrences of the new pairs (`退货 b` / `促销码 a`).

### D2 — Displaced wrapped instruction lines: CONFIRMED fixed (all 13 affected instances)

- **D2a (P3, 7 editions: de, en, es, fr, it, nl, pt):** a single complete instruction node at home position (65, 2564.45), 20.5pt, fill #57523f, with the exact fix-report wordings — de `Setzen Sie Verbform und Kasus richtig ein.`; en `Fill in the right verb form or the right case.`; es `Completa la forma verbal o el caso correcto.`; fr `Complétez la bonne forme verbale ou le cas.`; it `Metti la forma verbale o il caso giusti.`; nl `Vul in: juiste werkwoordsvorm of naamval.`; pt `Complete a forma verbal ou o caso correto.` Column 2 starts cleanly with ex. 34 (badge `34.` at (599,1699) in de; same Russian stem geometry in all). Visually confirmed on all 7 P3 home crops + col-2 crops (e.g. de col-2 starts `B1 34. Ausfüllen / Фильм «Лила» ___ 12 ноября.`).
- **D2b (P4, 6 editions: de, en, es, fr, it, pt):** a single complete instruction at (65, 2553.45) — de `Zahlen und Wörter von Seite 4 einsetzen.`; en `Fill in with numbers and words from page 4.`; es `Completa: números y palabras (página 4).`; fr `Complétez: chiffres et mots de la page 4.`; it `Completa con numeri e parole di pagina 4.`; pt `Complete: números e palavras da página 4.` Column 2 starts with ex. 52 (badge `52.` at (599,1659) in de). Visually confirmed on all 6 P4 home crops + col-2 crop.
- **Own orphan-fragment scan** over all 88 pages (20.5pt nodes at x=527/989/1451, y 1600–1800, preceded by a home line at x=65, y>2400): **ORPHANS = 0**. The only band-hits are the legitimate pre-existing P5 D-head bridges directly under their heads at (989, 1747.5) in all 11 editions (e.g. core `把词组成正确的句子。`, en `Put the words in the right order.`).
- **Regression:** clean editions show the same home-line geometry as before the fix (single lines at y=2534.725 P3 / y=2523.725 P4: core `用动词的正确形式或正确的格填空。`, ja, zh-tw equivalents; nl P4 already single-line at 2553.45). Visually confirmed on core/ja/ko/zh-tw P3+P4 home crops. **Limitation (stated honestly):** no pre-fix SVGs were retained for byte-diffing, so "unchanged" rests on map-entry claims + geometry, not a byte comparison.

### D3 — ja P8 H-note kinsoku dangling bracket: CONFIRMED fixed

ja `p8-test.svg` H-note, x=1451: line 1 (y=371.12) `作文（決まった答えはありません）；模範文は`, line 2 (y=400.845) `下にあります（87 語）。` The bracketed count opens and closes inside line 2; meaning preserved ("Essay (no set answer); the model essay is below (87 words)"); 2 lines. Visually confirmed on the ja P8 H-note crop. Own kinsoku scan over all 88 pages (line ends with an opening bracket `（(［｛〈《「『【` or starts with closing punctuation): **0 hits in all 11 editions**.

## 2. Full key verification — 150/150, all keys verified semantically

The full core manuscript `2026-w46-ru-core.text.md` (682 lines) was read in full and **every key 1–150 was verified semantically** against stems, article text, chart, and fixture/calendar data. Rendered P8 keys in all 11 editions were re-extracted wrap-aware (13pt nodes grouped by column x∈{65,527,989,1451}, y<2580, joined per column) and compared full-text against each edition's `.text.md` Answers section (150 lines each): **0 real mismatches**. (The only apparent diffs, ja 109/139 and ko 99/139, are the checker's joiner inserting a space inside a wrapped CJK/Hangul word — rendering artifacts of the check, not defects; p8.py's CJK-aware joiner handles these.) Key-letter comparison core vs each fan-out: identical first tokens for all 150 except 137–140 (E-section translations by design; zh-tw 137 first token coincides). No U+FFFD bytes anywhere (byte-level grep over all `.text.md`, SVGs, ABSTRACT.txt, KITs: 0).

Notable adjudications from the semantic read: ex.12 key B (1962 — 1917 is the decree date, a distractor; the text says "отсчитывается с 1962 года"); ex.63 `сыграли` matches article phrasing; ex.96 `работаем` (parallel to `отдыхаем`); ex.110 `может`; ex.146 B `пришла` (feminine, speaker "Я пришла"); ex.149 B `Хороших покупок!`; E-section 137–140 are native-language translations by design (Chinese renderings accurate).

### Per-matching-block table (stem + options + key, quoted)

| Block | Words (stems) | Printed options | Keys (verified) |
|---|---|---|---|
| 25–28 (P2, holidays) | 25. День полиции; 26. День экономиста; 27. День войск РХБ защиты; 28. Всероссийский день призывника | a. День экономиста; b. День войск РХБ защиты; c. Всероссийский день призывника; d. День полиции | **25→d, 26→a, 27→b, 28→c.** Cross-checked vs P2 holidays box: 10 Nov Police Day, 11 Nov Economist Day, 13 Nov RCB Troops Day, 14 Nov Sociologist Day, 15 Nov Conscript Day. |
| 39–42 (P3, film) | 39. биографический фильм; 40. стриминг; 41. сеанс; 42. зритель | a. человек, который смотрит фильм; b. фильм о жизни реального человека; c. показ фильма в кинотеатре; d. фильмы смотрят дома через интернет | **39→b, 40→d, 41→c, 42→a.** |
| 57–60 (P4, fixtures) | 57. «Локомотив»; 58. ЦСКА; 59. «Спартак»; 60. «Зенит» | a. играет с ЦСКА в субботу в 19:30; b. играет с «Рубином» в пятницу; c. играет с «Акроном» в воскресенье…; d. играет с «Ростовом» | **57→b, 58→a, 59→c, 60→d.** Cross-checked vs P4 14th-round calendar (Fri 6.11 Lokomotiv–Rubin 19:30; Sat 7.11 Krasnodar–CSKA 19:30; Sun 8.11 Spartak–Akron 16:15, Zenit–Rostov) and 13th-round box (Spartak–Lokomotiv 4:0, CSKA–Orenburg 0:0). |
| 75–78 (P5, sale) | 75. посылка; 76. возврат; 77. промокод; 78. пик | a. код со скидкой; b. товар возвращают в магазин; c. самое большое число заказов; d. товар, который прислали по почте | **75→d, 76→b, 77→a, 78→c.** (D1 fix; see §1.) |
| 141–144 (P8 F, week words) | 141. предзимье; 142. посылка; 143. пик; 144. гололедица | a. самое большое число заказов; b. лёд на дороге; c. время между осенью и зимой; d. товар, который прислали по почте | **141→c, 142→d, 143→a, 144→b.** |

All cloze/fill keys check against grammar and article facts; all choice keys check against the article; all arithmetic/numerical keys recomputed (chart 42/24/20/14; ex.123 10 days off; ex.67 14.4M orders; ex.66 600,000 sellers). **Key-verification result: 150/150 correct in the core and in all 11 rendered P8 key lists. No wrong key letter remains.**

## 3. Full re-gate (independent re-runs on final artifacts; fix worker's gate JSONs not accepted)

- **Occlusion audit** (`tools/occlusion_audit.py`, selftest OK on every run — planted classes BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX fired 1 each, clean controls silent): **0 flags in all 11 editions (88 pages).** JSONs/logs `gates/occlusion-ru-*.json/.log`, `gates/occlusion-selftest.log`.
- **p8.py:** core extract 150/150; `compare` vs core = **CLEAN 150/150 in all 10 fan-outs**, missing=[] extra=0 uncertain=[], keydiff=[137,138,139,140] in every edition (adjudicated: E-section translations by design). JSONs/logs `gates/p8-ru-*.json/.log`.
- **Freeze diff** (`tools/freeze.py diff` vs core SVG): Latin editions (de/en/es/fr/it/nl/pt) exit 0, added CJK = 0. ja/ko/zh-tw exit 1 under `--strict-cjk`, adjudicated as follows (verified with the tools-venv opencc + the word-analysis script, outputs in `gates/word-analysis-*.txt`):
  - Word-level Cyrillic multiset diff: **TOTAL ADD {} in all 10 fan-outs** — zero added Cyrillic words; frozen Russian intact. REM lists are only the adjudicated furniture replacements (P1 subtitle line, P6 practice-data label + disclaimer sentence, P7 heading words, P8 heading/separators incl. `СТРАНИЦА` ×8 in ja/ko/nl/zh-tw).
  - Char totals: Latin han=0 kana=0 hangul=0; ja cyr=16804 han=2944 kana=1447 hangul=0, 2 core Han nodes survive verbatim (`生活`, `文化`); ko cyr=16868 han=8 kana=0 hangul=2791, 0 core Han survive — the "han=8" is 4×`『` + 4×`』` under the script's HAN regex range, i.e. brackets only, no Han, no Kana; zh-tw cyr=16868 han=2132, 109 core Han nodes survive verbatim.
  - CJK adjudication (opencc, direction checked): ja added chars are native Japanese script only (kanji + hiragana + katakana + Japanese punctuation `、。『』（）＋：～`); the 6 chars differing under s2t (`内 声 寝 届 断 画`) are Japanese shinjitai that opencc also treats as simplified forms — by design, same as Round 1. ko added CJK = Hangul + `『』～` only. zh-tw: ZERO Simplified-form chars among added Han (s2t-differing list empty); the long t2s-differing list is Traditional-form chars, as expected. Core (zh-cn) control: its Han inventory differs under s2t as expected (Simplified forms).
- **Counts re-measured** from the manuscript (body only, excluding the Answers section): total **150**, per-page **10/18/18/18/18/18/12/38**, level split **A2 51 / B1 75 / B2 24** (from `[LEVEL]` tags, group ranges expanded). Model text (H example, ex.150): **87 whitespace tokens** (85 excluding standalone dashes; printed "(87 words)" follows the token count; inside the 80–100 brief).
- **P7 golden phrases:** all 8 occur **exactly twice** in every edition (article page + P7), verbatim contiguous. P7 `Страница N` references correct in all editions (pages 1–6; phrases 7–8 both from P6).
- **P6 chart** measured from SVG rects in all 11: bars at x=685, widths **600/343/286/200** for 42%/24%/20%/14% (proportional, 14.29px/pt; labels sum 100%), fill #3e4c2a. Native practice-data label + disclaimer sentence present in all 11 (e.g. de `ÜBUNGSDATEN` / `Dies ist eine Übungsumfrage der Redaktion — keine echte Statistik.`; ja `練習用データ`; zh-tw `練習數據`).
- **Masthead/badge/footer:** masthead `Lucerna` geometrically identical in all 11 (x=975, 168px, fill #28251d, UnifrakturMaguntia). Pairing badge visible in the P1 masthead area in every edition: at y=372, brick #a4553a, in de/en/es/fr/it/ja/nl/pt (en olive #3e4c2a — by design per build spec, NOT a defect); ko/zh-tw keep the Russian subtitle at y=372 and the badge below at y=574, brick (visually confirmed on ko/zh-tw P1 badge crops; badge clear of the headline block). Core/zh-cn keeps its Russian subtitle line as its own badge. Footer labels on all 8 pages of all 11 editions (footer band y=2624, native-language string + native page line, VOL.3 everywhere). Quotes `«`/`»` balanced 127/127 in every edition; no ASCII straight quotes in SVG text; no U+FFFD.
- **Reader-facing sweep** over all SVG text: zero hits for W46, 2026-w46, weekly-report, SOP, proofread, occlusion, github, discord, insert.py, lint.mjs, cover. Only `VOL.4 ` hits (1 per edition) = the legitimate next-issue teaser `(VOL.4)` on P7.
- **Images/credits:** 6 credit strings per edition covering 4 photos — Toxer427 CC0 (Wikimedia Commons), Wilson Bentley public domain, 1912 squad author unknown public domain (`Фото: автор неизвестен, 1912 — общественное достояние`), Preston Keres/USDA public domain. P8 separators: Russian `— СТРАНИЦА n —` in de/en/es/fr/it/pt (by design, `p8_separator: None`), native in ja (`— n ページ —`), ko (`— 제 n 면 —`), nl (`— Pagina n —`), zh-tw (`— 第 n 版 —`).
- **W45 promises honoured** (text-verified in all 11): P4 disclosure "Результаты тура на момент сдачи номера неизвестны — полные итоги в VOL.4" (+ P4 subtitle "итоги неизвестны"); P7 letters-box disclosure in the reader's native language with promise carried to VOL.4; VOL.4 teaser heading on P7; 11.11 sale as P1/P5 lead.
- **Dates/weekdays independently verified** (`date -d`, Europe/Moscow): 9 Nov 2026 = Monday, 6 Nov = Friday, 20 Nov = Friday — matching the article (Mon 9, Tue 10, Wed 11, Thu 12 Nov; fixtures Fri 6 / Sat 7 / Sun 8 Nov; round 15 Fri 20 Nov). P1 date line `НЕДЕЛЯ С 9 ПО 15 НОЯБРЯ 2026 ГОДА` present in all 11 P1s. P6 day strip пн–вс in order (x=195…1755, y=1424) in all editions.
- **ABSTRACT.txt (all 11):** single line each, 0 ASCII double quotes, reader-native language, practice framing (never "learn Russian from the news" or equivalents), naming real topics + masthead VOL.3 + A2–B2 + 150 exercises. Script check: zh-tw abstract has zero Simplified-form chars (s2t-differing list empty); core abstract has zero Traditional-form chars (t2s-differing list empty); ja abstract's 3 s2t-differing chars (`学`, `点`) are standard Japanese forms. All valid.
- **PDFs (all 11):** 8 pages each; web PDFs 2,310,183–2,760,278 bytes (all ≤ 7 MB); `pdftotext` bytes > 0 in every web and print PDF; print-vs-web text **IDENTICAL** after whitespace normalisation in all 11 (md5 compare, `gates/pdf-text-compare.txt`; inventory in `gates/pdf-inventory.txt`). Core `.text.md` vs zh-cn `.text.md`: byte-identical (52,661 bytes each, `cmp` clean).
- **Native-language correctness / residue scan:** per-edition stopword scan shows own-language function words dominant; apparent cross-hits are shared cognate forms only (de `des`, es/it `con`/`una`, pt `das`/`para`). CJK script counts: ja han+kana, zero hangul; ko hangul only; zh-tw han only; core han only. No wrong-script residue, no untranslated strings found.
- **Cards viewed:** full-frame P1 + P8 for all 11 editions (22 cards), P3 home+col-2 crops ×7 (D2a), P4 home+col-2 crops ×6 (D2b), P5 block-C crops ×11, ja P8 H-note crop, ko P3 wrap crop, ko/zh-tw P1 badge crops. No overflow, overlap, or missing credits anywhere — except D4 below.

## 4. New defect found in Round 2

### D4 — BLOCKING (it edition only): missing glyph U+0161 š in P8 answer-key notes 51 and 129

**Evidence (quoted, file + line/element):**

- Source strings in `hidden_files/w46/ru_maps.py` (it spec), lines 1318 and 1343:
  - L1318: `('国家队周四在塔什干比赛', 'La nazionale gioca giovedì a Taškent')`
  - L1343: `('玛莎这周是平常的一周', 'La settimana di Maša è una settimana normale')`
- Rendered SVG nodes in `files/weekly-report-w46-ru-it/svg/p8-test.svg` (font `Noto Serif CJK SC`, 13pt):
  - `<text x="527" y="1667.919" …>51. B — La nazionale gioca giovedì a Taškent</text>`
  - `<text x="1451" y="1622.900" …>129. B — La settimana di Maša è una settimana normale</text>`
- The character š (U+0161, LATIN SMALL LETTER S WITH CARON) has no glyph in the rendering font. Character inventory scan over all 88 pages: š occurs **exactly twice in the whole issue, both here**; every other non-ASCII character in the issue (Latin-1 accents, œ U+0153, arrows, ✓, CJK punctuation) was verified rendering correctly — fr key 32 `cœur` renders fine (control crop saved). The nl edition uses ASCII `Tasjkent`/`Masha` in the same notes and is unaffected.
- **Shipped artifacts affected (all three, visually confirmed with crops saved under `crops/`):**
  - Card PNG `cards/p8-test.png`: tofu box — `Ta☒kent` (key 51), `Ma☒a` (key 129). Crops: `d4-it-p8-key51-card-tofu.png`, `d4-it-p8-key129-card-tofu.png`.
  - Web PDF `Lucerna-VOL3-IT-web.pdf` p.8: blank gap — `Ta  kent` (pdftoppm raster). Crop: `d4-it-p8-key51-webpdf-gap.png`.
  - Print PDF `Lucerna-VOL3-IT.pdf` p.8: tofu box — `Ta☒kent` (pdftoppm raster). Crop: `d4-it-p8-key51-printpdf-tofu.png`.
- The same š strings are also in the it `.text.md` registry (lines 229, 470, 575, 661) — text-only, no rendering defect there, but the registry must stay consistent with whatever replacement the fix uses.
- **This is NOT a fix regression:** the š strings predate the Round 1 fix (the fix worker did not touch them) and were missed in Round 1. It is a new Round 2 finding.
- **Required fix (for the fix worker, not done here):** replace š with an ASCII transliteration in the two it note strings (`Taškent` → `Tashkent`, `Maša` → `Masha`, matching the nl edition's ASCII forms), regenerate the it `.text.md`, P8 SVG, card PNG, and both PDFs, then re-gate the it edition (p8 compare, occlusion, PDF text-layer check, and a visual re-check of the two key lines). No other edition needs any change.
- **Severity:** BLOCKING for the it edition. A visible missing glyph in the shipped answer key fails the card gate ("no missing glyphs/tofu") and the proofread-until-zero standard. The other 10 editions are unaffected.

## 5. Observation (non-blocking, recorded, NOT a defect)

- **O1 — ko P3 instruction wrap:** the ko P3 home instruction wraps with the lone syllable `요.` on line 2 (`동사의 올바른 형태나 올바른 격으로 빈칸을 채우세` / `요.`, y=2534.725/2564.45, x=65). Pre-existing, untouched by the fix, at home position directly under its header, reading in order; the orphan-fragment scan is 0 and the ko P3 card is otherwise clean. A legal Korean line break, comparable to the accepted option-d wrap (`почте` alone on line 2) in P5 block C. Recorded for the record; not gating, not a re-raised Round 1 defect.

## 6. Adjudicated non-defects (not re-raised, per Round 1)

Badge fills (en olive), P8 Russian separators in de/en/es/fr/it/pt, "Russia play" wording, and W45-promise disclosure wording were adjudicated non-defects in Round 1 and are not raised again. The nl deck string `pagina’s` (U+2019) is correct in the SVG; its odd look in one downscaled view was a rendering artifact of the viewer, not the artifact.

## 7. Regression statement

The D1/D2/D3 fixes introduced no new defect in any edition (orphan scan 0, kinsoku scan 0, occlusion 0, freeze ADD {}, p8 CLEAN, counts/chart/P7 all re-verified, all 22 full-frame cards viewed). D4 is pre-existing, not fix-caused. Limitation: clean-edition "unchanged" claims rest on geometry + map claims, not byte-diffing (no pre-fix SVGs retained).

## Final verdict

**ROUND 2 FAIL (blocking defect D4: it edition P8 answer-key notes 51 and 129 render š U+0161 as a missing glyph — tofu box in the card and print PDF, blank gap in the web PDF). All other 10 editions PASS and are shippable; the it edition becomes shippable after the D4 fix + a re-gate of the rebuilt it P8 artifacts.**
