# Round 3 Independent Proofread Verdict — Lucerna Weekly W46, RU target, it edition only, VOL.3

- **Issue:** W46, dated Mon 2026-11-09 – Sun 2026-11-15, VOL.3, Russian target, ~150 exercises.
- **Proofreader:** independent subagent (did not build or fix this edition). Round 3, 2026-11-03.
- **Scope:** ONE edition only — 2026-w46-ru-it (Russian target, Italian reader-native), folder `files/weekly-report-w46-ru-it/`. The other 10 RU editions were Round 2 PASS and hash-verified byte-identical after this fix; they were NOT re-proofread and NOT touched.
- **Prior verdict:** Round 2 FAIL on this edition only, on ONE defect D4 (missing glyph š U+0161 in P8 notes 51/129). D1/D2/D3 CONFIRMED fixed in Round 2; keys 150/150 CONFIRMED in Round 2; all gates clean; other 10 editions PASS.
- **Fix record adjudicated:** `hidden_files/w46/ru-fix-round3/FIX-REPORT.md` + §11 fix record in this edition's `WEEKLY-KIT.md` (verified present; §§1–10 byte-identical prefix to the pre-fix KIT, verified).
- **Work directory (this round):** `hidden_files/w46/ru-proofread-gates-round3/` — gate JSONs/logs in `gates/`, own raster crops in `crops/`, own extraction/font-coverage scripts (`extract_r3.py`, `font_coverage_r3.py`), own PDF page-8 rasters in the gate root. Fresh directory; no earlier gate dir reused.
- **Proofreader-only:** no edition file was edited, re-rendered, pushed, or inserted. No defect was fixed by this round. No `~/workspace/weekly-git` access, no `index.json` edit, no Discord post, no edition content dumped into chat. All raster crops were produced read-only from the shipped artifacts into the gate directory (PIL crops of the shipped card PNG; `pdftoppm` rasters of the shipped PDFs); no edition file was regenerated.

## Verdict summary

| Item | Result |
|---|---|
| D4 fix (š → ASCII in P8 notes 51/129) | **CONFIRMED** (all rendered artifacts; own crops + own font-coverage sweep) |
| D1 survival (P8 keys 76.b/77.a) | CONFIRMED |
| D2 survival (P3/P4 home instruction lines) | CONFIRMED |
| D3 | n/a — ja edition; ja files byte-identical (see §4) |
| Full key verification | **150/150 correct** (semantic re-verification + rendered-vs-registry full-string match) |
| Full re-gate (own runs) | All gates clean (see §3) |
| Change isolation | Exactly 6 files changed, all it (see §4) |
| New / residual defects | **None** |
| Edition verdict | **PASS — shippable** |

## 1. Fix verification — D4: CONFIRMED

The fix claim (source change in `hidden_files/w46/ru_maps.py`, it spec only, exactly 2 lines) was verified independently at every level; the fix worker's gate JSONs were not accepted.

### 1a. Source (verified, not trusted)

Diff of current `ru_maps.py` vs the fix worker's retained pre-fix copy (`ru-fix-round3/logs/ru_maps.py.pre-fix`): exactly 2 changed lines, both in the it spec:

- Line 1318: `('国家队周四在塔什干比赛', 'La nazionale gioca giovedì a Taškent')` → `... a Tashkent')`.
- Line 1343: `('玛莎这周是平常的一周', 'La settimana di Maša è una settimana normale')` → `... di Masha è ...')`.

Chinese source keys untouched. š (U+0161) = 0 in the whole current `ru_maps.py`.

### 1b. š = 0 in ALL rendered artifacts (own counts)

| Artifact | š (U+0161) | `Tashkent` | `Masha` | U+FFFD |
|---|---|---|---|---|
| All 8 it SVGs | 0 in every file | 1 (P8 only) | 1 (P8 only) | 0 |
| `.text.md` (55,223 bytes) | 0 | 2 (registry L229 + Answers L575) | 2 (registry L470 + Answers L661) | 0 |
| Print PDF text layer (55,066 bytes) | 0 | 1 (P8) | 1 (P8) | 0 |
| Web PDF text layer (55,066 bytes) | 0 | 1 (P8) | 1 (P8) | 0 |

Rendered P8 nodes (own extraction, exact strings + positions, 13pt `Noto Serif CJK SC`):

- `<text x="527" y="1667.919">51. B — La nazionale gioca giovedì a Tashkent</text>`
- `<text x="1451" y="1622.900">129. B — La settimana di Masha è una settimana normale</text>` (byte-checked: `è` = U+00E8; the `��` seen in one tool echo was a display artifact, not the file).

`.text.md` diff vs the retained pre-fix copy: exactly 4 lines (registry L229/L470 + Answers L575/L661), no other line differs. P8 SVG node diff vs the retained pre-fix P8 SVG (339 nodes): exactly 2 nodes differ (nodes 222 and 309, the two lines above); all other 337 nodes identical.

### 1c. Own raster crops (not the fix worker's)

Saved under `crops/`; all show clean rendering — no tofu box, no blank gap:

- `r3-it-p8-key51-card.png` — card: `51. B — La nazionale gioca giovedì a Tashkent`.
- `r3-it-p8-key129-card.png` — card: `129. B — La settimana di Masha è una settimana normale`.
- `r3-it-p8-key51-webpdf.png` / `r3-it-p8-key51-printpdf.png` — 150 dpi PDF p.8 rasters: `Tashkent` clean. (Web and print p.8 rasters are byte-identical, md5 `e7f5eea1f0d1206723bfaced4d3c2484`.)
- `r3-it-p8-key129-webpdf.png` / `r3-it-p8-key129-printpdf.png` — `Masha` clean, same identity.
- `r3-it-p8-footer-card.png` — P8 footer strip: footer line clear, no intrusion.

### 1d. Own font-coverage sweep (fresh script, `font_coverage_r3.py`, fontTools, tools venv)

Every character in every SVG `<text>` node (1,466 nodes) checked against the cmap of the rendering font face actually used for that node (family + weight; SC face index 2 of the split Noto CJK TTCs; UnifrakturMaguntia TTF for the masthead):

- Distinct characters (excluding whitespace): **156**.
- **Missing glyphs: 0.** No character outside its rendering font's coverage.
- **Control: š (U+0161) is absent from all four CJK SC cmaps** (Serif Regular/Bold 44,777 chars each; Sans Regular/Bold 44,810 chars each) — the sweep would have caught D4 pre-fix. Cmap sizes match the fix worker's independent sweep exactly.
- Output: `gates/font-coverage.json`, `gates/font-coverage.log`.

### 1e. KIT §11 š occurrences — NOT a defect (as instructed, verified)

š appears 9 times in `WEEKLY-KIT.md`, all inside §11 only (lines 129–143): the defect description naming U+0161 and the quoted BEFORE strings (`Taškent`, `Maša`). The KIT is documentation, not a rendered artifact. The š=0 checks above apply to rendered artifacts only. **Not raised as a defect.** No š occurs in any other KIT section.

### 1f. D1/D2 survival (own SVG node checks)

- **D1:** rendered P8 keys `75. d — pacco d`, `76. b — reso b`, `77. a — codice promozionale a`, `78. c — picco c` (x=527, y=2374.8/2403.0/2431.2/2459.4, 13pt) — unchanged and correct. P5 block C itself unchanged and correct (see §2 block table).
- **D2a:** P3 single complete instruction node at (65, 2564.45), 20.5pt, `Noto Sans CJK SC`, fill #57523f: `Metti la forma verbale o il caso giusti.` Column 2 starts with ex. 34.
- **D2b:** P4 single complete instruction node at (65, 2553.45), 20.5pt, same style: `Completa con numeri e parole di pagina 4.` Column 2 starts with ex. 52.
- **D3:** ja edition untouched (hash-verified byte-identical, §4); no re-check needed or done.

**D4 fix adjudication: CONFIRMED.** The defect is fixed at source, in the registry, and in every shipped artifact (SVG, card, both PDFs), with key letters 51.B/129.B unchanged and no other string disturbed.

## 2. Full key verification — 150/150, verified semantically

The full it manuscript `2026-w46-ru-it.text.md` (683 lines) was read in full and **every key 1–150 was verified semantically** against stems, article text, chart, calendar/fixture data, and grammar. In addition, the rendered P8 key list was re-extracted independently (own column-grouped, wrap-aware extraction of the 13pt nodes: 150 entries, numbers 1–150, none missing) and compared against the `.text.md` Answers section: **key-token mismatches 0, full-string diffs 0** — every rendered P8 line matches its registry line word for word, including notes. The canonical `p8.py compare` independently agrees (CLEAN 150/150; see §3). Choice-key letters extracted: 75, all matching the registry.

Notable adjudications from the semantic read (all confirmed correct): ex.12 key B (1962 — 1917 is the decree date, a distractor; the text says "отсчитывается с 1962 года"); ex.47 key B ("Номер сдан 2 ноября" — attested in the P4 article: "на момент сдачи нашего номера, 2 ноября, результаты тура ещё не были известны"); ex.63 `сыграли` (article phrasing "14-й тур сыграли 6–8 ноября"); ex.91 `ровный` (attested in the P6 ЗА/ПРОТИВ box: "За: ритм ровный"); ex.96 `работаем` (parallel to `отдыхаем`); ex.110 `может` (modal + infinitive); ex.146 B `пришла` (feminine, speaker "Я пришла"); ex.149 B `Хороших покупок!`; E-section 137–140 are Italian translations by design (accurate renderings; 140 "Buon Giorno della polizia a tutti!" is an acceptable congratulation rendering).

### Per-matching-block table (stem + printed options + key, quoted from the SVG)

| Block | Words (stems, as printed) | Printed options (as printed, incl. wraps) | Keys (verified) |
|---|---|---|---|
| 25–28 (P2, holidays; stems = date lines in the holidays box, options at x=1485) | 25. 10 ноября — День полиции; 26. 11 ноября — День экономиста; 27. 13 ноября — День войск РХБ защиты; 28. 15 ноября — Всероссийский день призывника | a. День экономиста; b. День войск РХБ защиты; c. Всероссийский день призывника; d. День полиции | **25→d, 26→a, 27→b, 28→c.** Cross-checked vs the P2 holidays box (10 Nov Police, 11 Nov Economist, 13 Nov RCB Troops, 14 Nov Sociologist, 15 Nov Conscript). |
| 39–42 (P3, film; stems at x=989, options at x=1023) | 39. биография; 40. стриминг; 41. сеанс; 42. зритель | a. человек, который смотрит фильм; b. фильм о жизни реального человека; c. показ фильма в кинотеатре; d. фильмы смотрят дома через интернет | **39→b, 40→d, 41→c, 42→a.** |
| 57–60 (P4, fixtures; stems at x=989, options at x=1023) | 57. «Локомотив»; 58. «Краснодар»; 59. «Спартак»; 60. «Зенит» | a. играет с ЦСКА в субботу в 19:30; b. играет с «Рубином» в пятницу; c. играет с «Акроном» в воскресенье в 16:15; d. играет с «Ростовом» | **57→b, 58→a, 59→c, 60→d.** Cross-checked vs the P4 14th-round calendar (Fri 6.11 Lokomotiv–Rubin 19:30; Sat 7.11 Krasnodar–CSKA 19:30; Sun 8.11 Spartak–Akron 16:15, Zenit–Rostov) and the 13th-round box (Spartak–Lokomotiv 4:0, CSKA–Orenburg 0:0). |
| 75–78 (P5, sale; stems at x=527, options at x=561) | 75. посылка; 76. возврат; 77. промокод; 78. пик | a. код со скидкой; b. товар возвращают в магазин; c. самое большое число заказов; d. товар, который прислали по почте | **75→d, 76→b, 77→a, 78→c.** (D1 fix survives; see §1f.) |
| 141–144 (P8 F, week words; stems at x=989, options at x=1023) | 141. предзимье; 142. посылка; 143. пик; 144. гололедица | a. самое большое число заказов; b. лёд на дороге; c. время между осенью и зимой; d. товар, который прислали по почте | **141→c, 142→d, 143→a, 144→b.** |

All cloze/fill keys check against grammar and article facts; all choice keys check against the article; all arithmetic/numerical keys recomputed (chart 42/24/20/14; ex.123 10 days off; ex.67 14.4M orders; ex.66 600,000+ sellers; ex.23/123 November 20 work + 10 off days).

**Key-verification result: 150/150 correct in the registry and in the rendered P8 key list. No wrong key letter remains.**

## 3. Full re-gate (independent re-runs on the final artifacts; fix worker's gate JSONs not accepted)

- **Occlusion audit** (`tools/occlusion_audit.py`, selftest OK — planted classes BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX fired 1 each, clean controls silent): **0 flags on all 8 pages.** JSON/log: `gates/occlusion-ru-it.json/.log`, `gates/occlusion-selftest.log`. Masthead pixel clearance confirmed visually on the P1 full-frame card (wordmark clear of badge/rules; no overprint) and by `check_core` same-baseline collisions = 0.
- **p8.py:** extract 150/150; `compare` vs core = **CLEAN 150/150**, missing=[] extra=0 uncertain=[], keydiff=[137, 138, 139, 140] (adjudicated: E-section Italian translations by design, same adjudication as Rounds 1–2). Logs: `gates/p8-ru-it-extract.log`, `gates/p8-ru-it.log`.
- **Freeze diff** (`tools/freeze.py diff` vs core SVG): exit 0; added CJK = 0 on all 8 pages; TOTAL added CJK 0. JSON/log: `gates/freeze-ru-it.json/.log`.
- **Freeze word analysis** (own script, `gates/word-analysis-it.txt`): **TOTAL ADD {} (zero added Cyrillic words)**; char totals cyr=16860, han=0, kana=0, hangul=0 (core: cyr=17049, han=1907). Removals are the adjudicated furniture/explanation replacements only (31 distinct Cyrillic words across P1/P6/P7/P8, incl. the P8 `СТРАНИЦА` separators).
- **check_core** (it build dir, read-only run): golden BAD 0 (8/8 phrases ×2), gloss fails 0, orphan line-starts [], same-baseline collisions 0. Log: `gates/check_core-it.log`.
- **Counts re-measured** from the manuscript registry (body only, excluding Answers; ranges expanded): total **150**, per-page **10/18/18/18/18/18/12/38**, level split **A2 51 / B1 75 / B2 24**. Model text (H example, ex.150): **87 whitespace tokens** excluding the `Пример:` label (85 excluding the 2 standalone dashes) — the printed "(87 parole)" follows the token count; inside the 80–100 brief. Log: `gates/counts-phrases-chart.log`.
- **P7 golden phrases:** all 8 occur **exactly twice** (article page + P7), verbatim contiguous, in the joined SVG text. P7 `Страница N` references correct (pages 1, 1, 2, 3, 4, 5, 6, 6; phrases 7–8 both from P6).
- **P6 chart** measured from SVG rects: bars at x=685, widths **600/343/286/200** for 42%/24%/20%/14%, fill #3e4c2a; each label occurs once; labels sum 100%. Native practice-data label (`ЧЕМ ЗАЙМУТСЯ НА ЭТОЙ НЕДЕЛЕ? · DATI DI ESERCIZIO`) + disclaimer sentence (`Questo è un sondaggio di esercizio della redazione — non statistiche vere.`) present.
- **Masthead/badge/footer:** P1 masthead `Lucerna` at (975, 262), 168px, fill #28251d, UnifrakturMaguntia. Pairing badge visible in the P1 masthead area at y=372, 20pt bold, brick #a4553a: `TESTI IN RUSSO · SPIEGAZIONI IN ITALIANO — L’EDIZIONE PER I LETTORI ITALIANI`. Footer labels on all 8 pages (y=2624): `Lucerna · SETTIMANALE RUSSO VOL.3 · TESTI IN RUSSO · SPIEGAZIONI IN ITALIANO` + `Pagina N di 8`. P1 date line present: `НЕДЕЛЯ С 9 ПО 15 НОЯБРЯ 2026 ГОДА`. P8 separators: Russian `— СТРАНИЦА n —` ×8 (by design, `p8_separator: None` family pattern, adjudicated in Round 1).
- **Quotes/punctuation:** `«`/`»` balanced 127/127 in SVG text; no ASCII straight double quotes in SVG text; no U+FFFD anywhere in SVGs, `.text.md`, or PDF text layers.
- **Reader-facing sweep** over all SVG text: zero hits for W46, 2026-w46, weekly-report, SOP, proofread, occlusion, github, discord, insert.py, lint.mjs, cover. `VOL.4` occurs 7× — all legitimate forward references (P1 contents teaser, P2 letters promise, P4 disclosure, P7 letters box + teaser heading), by design.
- **Kinsoku scan** (own; node ends with an opening bracket or starts with closing punctuation, all 8 pages): **0 hits**.
- **Orphan-fragment scan** (Round 2 definition: 20.5pt nodes at x=527/989/1451, y 1600–1800, with a home line): exactly 1 band-hit — the legitimate pre-existing P5 D-head bridge `Forma frasi corrette con le parole.` at (989, 1747.5) directly under its head, adjudicated in Round 2. No other orphan.
- **Dates/weekdays independently verified** (`date -d`, Europe/Moscow): 9 Nov 2026 = Monday, 6 Nov = Friday, 7 Nov = Saturday, 8 Nov = Sunday, 10 Nov = Tuesday, 11 Nov = Wednesday, 12 Nov = Thursday, 20 Nov = Friday — matching the article, fixtures, and calendar. P6 day strip пн–вс in order (9–15) visually confirmed.
- **W45 promises honoured** (text-verified): P4 disclosure "Результаты тура на момент сдачи номера неизвестны — полные итоги в VOL.4"; P7 letters-box disclosure in Italian with promise carried to VOL.4; VOL.4 teaser heading on P7; 11.11 sale as P1/P5 lead.
- **ABSTRACT.txt:** single line (+ trailing newline), 0 ASCII double quotes, Italian, practice framing ("150 esercizi sui temi della settimana per chi studia il russo in italiano" — no news framing), naming real topics + masthead VOL.3 + A2–B2 + 150 exercises. Valid.
- **PDFs:** 8 pages each; web PDF 2,310,997 bytes (≤ 7 MB); `pdftotext` 55,066 bytes in both web and print PDFs; print-vs-web text **IDENTICAL** after whitespace normalisation (md5 `f57c76aafbb08d992f28723b30aa8f23` both); web PDF fonts embedded + subset (`Lucerna*` CJK faces + UnifrakturMaguntia, `pdffonts`). Text-layer extracts saved: `gates/web.txt`, `gates/print.txt`.
- **Native-language correctness / residue scan:** per-edition word-frequency scan shows Italian function words dominant in the explanation layer; no wrong-script residue (han=0, hangul=0, kana=0 in SVG text); no untranslated strings found; apparent cross-hits are proper names / transliterations only (Ozon, Spartak, Lilja, Uzbekistan). A perceived gap after `l’`/`dell’` in downscaled card views was byte-checked and cleared: no SVG text node contains `’` + space except the legitimate P7 grammar note quoting Italian `'da'` — not a defect, not raised.
- **Images/credits:** 4 photos covered — Toxer427 CC0 (Wikimedia Commons), Wilson Bentley public domain, 1912 squad author unknown public domain (`Фото: автор неизвестен, 1912 — общественное достояние`), Preston Keres/USDA public domain — all with visible captions + credits on P1/P2/P4/P5.
- **Cards viewed:** full-frame P1 + P8, and P2, P3, P4, P5, P6, P7 at full frame (all 8 shipped cards). No overflow, overlap, missing glyphs/tofu, or missing image credits anywhere. P3 home + col-2 start and P4 home + col-2 start visually confirmed (D2); P5 block C visually confirmed (D1); P8 keys 51/129 visually confirmed in card and both PDFs (D4).

## 4. Change isolation (independent sha256 re-hash)

Compared all 232 files under `files/weekly-report-w46-ru-*` against the fix worker's pre-fix manifest (captured before any edit = the Round 2 state). Result: **exactly 6 files changed, all in the it edition**:

1. `files/weekly-report-w46-ru-it/2026-w46-ru-it.text.md`
2. `files/weekly-report-w46-ru-it/Lucerna-VOL3-IT-web.pdf`
3. `files/weekly-report-w46-ru-it/Lucerna-VOL3-IT.pdf`
4. `files/weekly-report-w46-ru-it/WEEKLY-KIT.md` (§11 appended; §§1–10 byte-identical prefix, verified)
5. `files/weekly-report-w46-ru-it/cards/p8-test.png`
6. `files/weekly-report-w46-ru-it/svg/p8-test.svg`

The other 226 files — the other 7 it SVGs/cards, `ABSTRACT.txt`, all files of the other 10 editions, and the frozen RU core directory (including the core/zh-cn `.text.md` pair) — are **byte-identical** to pre-fix. Current hashes also match the fix worker's post-fix manifest with **0 differences**. No files added or removed. Manifests: `gates/current-hashes.txt`, `gates/change-isolation.txt`. (The one earlier hash attempt in this round failed only on a wrong working directory and was re-run correctly; no file was written outside the gate directory.)

## 5. New / residual defects

**None.** No new defect and no residual defect was found in this round. In particular:

- D4 is fixed (see §1) — no tofu, no blank gap, no š residue in any rendered artifact.
- The 9 š occurrences in `WEEKLY-KIT.md` §11 are quoted before-forms in documentation — explicitly NOT a defect (see §1e).
- Adjudicated non-defects from Rounds 1–2 were NOT re-raised (ko P3 lone `요.` observation, badge fills, P8 Russian separators, "Russia play" wording, W45-promise disclosure wording).
- The P5 D-head bridge band-hit and the P7 `'da'` quotation are adjudicated/cleared above, not defects.

## 6. Gate outputs summary

| Gate | Tool / method | Result |
|---|---|---|
| Occlusion audit | `tools/occlusion_audit.py` (selftest OK) | 0 flags, 8 pages |
| P8 set/key gate | `tools/p8.py extract + compare` | CLEAN 150/150, keydiff [137–140] adjudicated |
| P8 rendered-vs-registry | own column-grouped extraction | 150 entries; key-token diffs 0; full-string diffs 0 |
| Freeze diff | `tools/freeze.py diff` | exit 0; added CJK 0 |
| Freeze words | own word multiset diff | TOTAL ADD {} |
| check_core | build-dir `check_core.py` (read-only) | golden BAD 0; gloss 0; orphans []; collisions 0 |
| Counts/levels/chart/P7 | own measurements | 150; 10/18/18/18/18/18/12/38; A2 51/B1 75/B2 24; bars 600/343/286/200; phrases ×2 |
| Font coverage | own fontTools sweep (control: š absent) | 156 distinct chars; 0 missing |
| PDF text layer | pdftotext/pdfinfo/pdffonts | 55,066 bytes both; web==print; 8 pp; web 2,310,997 B; fonts embedded |
| Kinsoku / orphan scans | own scans | kinsoku 0; orphan 1 legitimate bridge only |
| Change isolation | sha256 vs pre/post manifests | exactly 6 files, all it; 0 vs post-fix |
| Visual | all 8 cards full-frame + own crops | clean; D4 lines clean in card + both PDFs |

## Final verdict

**ROUND 3 PASS (edition shippable).**
