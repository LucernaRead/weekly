# WEEKLY-KIT — Lucerna Weekly W45 · KO × NL

**Pairing:** target Korean (KO) × reader native Dutch (NL). Korean target text frozen byte-for-byte; only the explanation layer is Dutch.
**Issue week:** 2–8 November 2026 (VOL.2). **Status: builder-complete.** Final sign-off awaits independent proofread; not yet inserted into the weekly repo (coordinator does inserts serially). Nothing was sent to Discord, to main chat, or to any cron.
**Delivery dir:** `files/weekly-report-w45-ko-nl/` — svg×8, cards×8, print PDF, web PDF, this KIT, ABSTRACT.txt.
**Build dir:** `hidden_files/weekly-report-w45-ko-nl-build/` (transform.py is the single edit source; `orig/` holds the pristine core copy).

## 1. Specs

- 1950×2700, 4 columns, 8 pages. Masthead `Lucerna` with no article (Korean takes no article).
- 150 exercises; pages 10/18/18/18/18/18/12/38; levels A2 51 / B1 72 / B2 27.
- Types: sentence completion 48, multiple choice 52, matching 16, cloze 13, sentence building 8, transformation 4, true/false 4, translation 4, writing 1.
- P8: 38 items (A8/B8/C4/D4/E4/F4/G5/H1), printed notes 150/150, dash form `N. key — note`.
- Model essay 157 characters (space-stripped), frozen verbatim, opening `나의 겨울 준비는 김장부터 시작해요.`
- Theme: Ipdong week — last foliage weekend, kimjang / winter-preparation season opening, exam countdown D-17→D-12; exam-day measures apply only on 19 November.
- Images per page 1/1/2/1/1/0/0/0 (P1 autumn, P2 ssam, P3 Bukhansan + apples, P4 baseball/Bain PD, P5 study photo).

## 2. Furniture — three-way对照 (W43 ko-nl measured wins over README #20 summary)

W43 ko-nl was measured from its actual SVGs, not copied from the README summary; the KO-family generic shape (subtitle 366, badge y=394, rules +20, dark band +9) only served as a reference and agrees with the W43 measurements.

| Item | W45 KO core | W43 ko-nl (measured) | This edition |
|---|---|---|---|
| Subtitle slot | y=366 | y=366 | y=366 |
| Badge string | — (Chinese) | `TEKSTEN IN HET KOREAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS` | identical to W43 |
| Badge y / size / colour | — | y=394, 20pt, #a4553a | identical to W43 |
| Rule lines | 412 / 421 | 412 / 421 | identical to W43 |
| Dark band rect y | 433 | 433 | identical to W43 |
| Band texts | 487 / 531 | 487 / 531 | identical to W43 |
| Footer | `… VOL.2 …` (Chinese) | `Lucerna · KOREAANS WEEKBLAD VOL.1 · TEKSTEN IN HET KOREAANS · UITLEG IN HET NEDERLANDS` | same string with VOL.2 |
| Page line | `Pagina {n} van 8` pattern (W43) | `Pagina {n} van 8` | identical to W43 |
| Gloss prefix | `Uitleg — ` | `Uitleg — ` | identical |
| Section headers | — | `생활 · Dagelijks leven`, `문화 · Cultuur`, `스포츠 · Sport`, `청년 · Jongeren`, `깊이 읽기 · Dieper lezen`, `말 공부 · Taal`, `시험과 답 · Toets en antwoorden` | identical to W43 |
| Exercise header | — | `연습 · Oefeningen blz. N` | identical |
| Exercise right line | — | `Antwoorden op blz. 8 · Niveaus kunnen gemengd staan — zoek op nummer` | identical |
| P1 quiz right line | — | `Lees de voorpagina en kies het juiste antwoord · Antwoorden op blz. 8` | identical |
| P8 separators | — (Chinese) | `— Pagina N —` | identical to W43 NL (NOT the frozen Korean separator form used by KO×PT / KO×FR) |
| P8 band subtitle | Korean frozen `제8면 · 이번 주의 큰 시험 + 모든 답` | same | identical (frozen) |
| P8 levels | — | `Alle` | identical |
| Instruction labels | — | Vul in · Koppel · Herschrijf · Bouw · Vertaal · W of O · Schrijf | identical |
| P8 header | — | `답 · Antwoorden — per pagina, zoek het nummer op` | identical |
| P8 header right line | — | `Bij elk antwoord een korte notitie in het Nederlands · ✓ = opgave met voorbeeld` | identical |

## 3. Toolchain (measured, not copied)

- run.py and render.py both run under `tools/venv/bin/python`: Python 3.12.3, PIL 13.0.0; render additionally uses cairosvg 2.9.1. System python3 (PIL 10.2.0, no cairosvg) was NOT used for either.
- `tools/p8.py` sha256 `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b27462703d8226815046eccc0ca9` (current new version; called with explicit dual paths `--core-p8/--edition-p8 --total 150` — the `--core-dir` form mis-picks the P8 filename by native and was not used).
- `tools/occlusion_audit.py` sha256 `e1f92b42eb8996fe04c5ffb60c4ec23e1911239a5f94b76808f01ed9414addf2`.
- `tools/freeze.py` sha256 `d9adfa486a788e57e15805d383f5691094067d26f1884c127dea4d1a1e587d54`.
- Baseline proof: the unmodified core copy reproduces the core SVGs 8/8 byte-identical (`freeze.py baseline`), and core SVGs re-checked after round 3 are unchanged (see §9).

## 4. Gates — all measured on the final (round-3) render

### 4.1 Freeze (`tools/freeze.py diff`)
Per-page added/removed text counts: p1 +20/−19, p2 +44/−39, p3 +34/−31, p4 +28/−25, p5 +38/−35, p6 +23/−19, p7 +40/−36, p8 +189/−177. CJK core→edition: p1 1462→1339, p2 1612→1360, p3 1524→1346, p4 1232→1074, p5 1433→1234, p6 1276→1136, p7 1365→1100, p8 2496→1224. **New CJK: p1–p7 = 0; p8 = exactly 1 character {절: 1}** (see §5 for the adjudicated citation). Han ideographs (U+4E00–U+9FFF) in edition text nodes: 0 on all 8 pages. ASCII double quotes in text nodes: 0 on all 8 pages.

### 4.2 P8 (`tools/p8.py compare`, explicit dual paths, total 150)
Core 150 noted = edition 150 noted, status **CLEAN**, missing=[], extra_count=0, uncertain=[], keydiff=[137, 138]. Adjudication in §5.

### 4.3 Gloss — dual caliber, method stated (README #21)
- **AST call-string caliber: core = edition = 85** (content12 24, content34 26, content56 28, content7 6, content8 1).
- Rendered-page caliber: core = edition = 85 (P1 5, P2 19, P3 16, P4 10, P5 16, P6 12, P7 6, P8 1), identical per page and per box.
- Note on the 83 figure: a regex-based call-string count gives 83 for BOTH core and edition because it undercounts by exactly 2 (one parenthesised call in content34, one f-string call in content8). **85 is the correct figure; 83 is a regex artefact, not a discrepancy.**
- Do NOT "correct" sibling KITs from this: KO×PT's 66 and KO×FR's 84 use different definitions (84 appears to exclude content8's 1 item). The gate here is equality with the core, which holds under both calibers.

### 4.4 Golden sentences (8, verbatim + page tags + issue frequencies = core)
`11월 7일은 입동이에요` (p1), `절정에 가까운 주말이라고만 말할 수 있어요` (p1), `김장은 겨울 내내 먹는 김치를 담그는 일이에요` (p1), `수능까지 17일 남았어요. 오늘이 D-17예요` (p2), `낮은 길은 더 늦게 물들어요` (p3), `KIA 타이거즈가 LG 트윈스를 3연승으로 이겼어요` (p4), `온 나라가 수험생을 응원해요` (p5), `날짜를 먼저 보세요` (p6). Issue frequencies core = edition = 5/2/4/2/2/2/2/2, and each sentence was verified present on its tagged page (space-stripped match). P7 Dutch renderings are literal translations of the same sentences, each carrying the correct page tag.

### 4.5 Geometry
- Canonical `tools/occlusion_audit.py` (self-test: all 6 defect classes trigger, clean control silent): **edition 0 flags, core 0 flags, NEW (edition − core) 0 flags.**
- Full-page right-edge ADVANCE scan (limit 1910): worst 1885.0, **0 flags**.
- Frame-line scan (text ink vs rect borders/lines; footer rule y=2580 exempt): **0 flags**.
- Same-baseline ink overlap (0.6px tolerance): **0 flags**.
- P6 chart-label coverage (baseline-anchored ink method, NOT getbbox ascender method; gate <30%): labels with coverage>0: 0, worst **0.0%**.
- P8 three calibers (limit 2540): flow cursor **2516.0**, last baseline **2530.48**, ink bottom **2533.98** — all pass. (Cursor < last baseline because the cursor sits in the less-full final column while the last baseline sits in a fuller earlier column.)
- P7 preview box bottom **2519.94 < 2540**. P7 letters box: rect y=1230.44, h=635.5, bottom 1865.94; last line ink bottom **1854.68** (11.26px inside the box); golden-sentence rule line y=1895.94 (41.26px gap below the last letters line). The core letters-box formula underestimates by ~26–29px (core P7's last line overflows its box); this edition does NOT inherit the overflow — it uses the KO×FR slack (+40 on the formula's trailing constant, 26→66). Last letters line: `je brief en je beste tekst van blz. 8 op!`

### 4.6 Korean orphan scan (window 10–45, ≥3-syllable tail, all prose columns)
Method: spy build — the transformed build was copied to `spy/`, OUT redirected to `spy/svg`, and `spy/svglib.py`'s wrap() was patched to log every call's pre/post-kinsoku lines; spy SVGs reproduce delivery SVGs **8/8 byte-identical** (the spy changes nothing about layout). Analysis walks each call by a character pointer over the original text (line-internal spaces preserved; kinsoku oidashi moves recognised, not counted as splits): **943 wrap calls, 0 unparsed, 0 mid-word splits, 0 tails ≥3 syllables.** Line-start NO_START (post-kinsoku): 5 entries, all OPENING single quotes of frozen Korean quoted phrases (`'힘내세요!'`, `'김장'`, `'D-17'`, `'〜부터 〜까지예요?'` twice) — legitimate line starts, identical to core; closer-stranding orphans = 0. The rendered-line window scan (same x, dy 10–45) independently gives 4 flags, all the same frozen-Korean opening-quote lines, identical to core item-for-item; the Dutch explanation layer has no line-start orphan punctuation. (An earlier analysis pass that stripped all spaces was discarded as a method bug — it skipped 328 multi-line calls; the pointer-walk analysis above is the valid one and covers all 943 calls.)

### 4.7 Registry comparison (core vs edition, one-process dumps from scratch copies)
TOTAL 150 = 150. Page/level/type differences: **none**. Key differences: exactly {137, 138, 150-apparatus} (150 is the H apparatus line, excluded by the p8 tool, hence p8 keydiff [137,138]). Notes changed: **150/150** (fully localised). REG stores no stem/body fields, so stems 139/140 were verified directly from the P8 SVG (Dutch stems present, Korean keys frozen — see §5).

### 4.8 Dutch proofread
The full Dutch layer was read end-to-end from the rendered SVGs (notes, gloss lines, band headers, box titles, exercise instructions, P8 notes): no spelling, grammar, or date/number errors found. Number formatting follows Dutch convention in notes (551.864, 1.312, 300.000, 27.000, 415,5 mm) while Korean keys keep their own forms. Spot-checked facts against keys: #14 exam-history Saturday 28 November, #22 max fine 300.000 won, #55 typhoon became extratropical cyclone 26 October, #90 listening section 13:10–13:35, #118 Hallasan/Samgakbong 415,5 mm rain, #131 next week = exam-history preparation — all consistent.

### 4.9 Images
Payload = core under both calibers (base64-text hash / decoded-JPEG hash): P1 `535fff46b7ce`/`6f7f33ed8f40`, P2 `e66d2b455ec6`/`96a6a19b612a`, P3 `e266b6ee1a87`/`158ea3a0e81f` and `5bea45d1f81e`/`214cc390ac7c`, P4 `1a7e7d6d5ffc`/`18ad8ae06fac`, P5 `6a1bab177d54`/`35e7dc69d417`, P6/P7/P8 0 images. Credit lines take the Commons API Artist field verbatim and each credited image is placed: P1 `사진: lumoplank — CC0 (Wikimedia Commons) · 자료 사진`, P2 `사진: wizdata — CC0 …`, P3 `사진: Udonhan1992 — CC0 …` and `그림: Paul Cézanne — Public domain …`, P4 `사진: Bain News Service — Public domain …`, P5 `사진: Gary Todd — CC0 …`. The P2 ssam photo is honestly captioned as NOT a kimjang photo.

### 4.10 Web PDF vs cards (8 pages, PIL ImageStat, no numpy)
Web PDF 8 pages, print PDF 8 pages. Web page raster (1400×1938) vs card scaled, mean |diff| per channel: p1 [2.42, 1.57, 3.91], p2 [2.30, 1.51, 3.85], p3 [2.33, 1.48, 3.84], p4 [1.99, 1.28, 3.44], p5 [2.19, 1.37, 3.68], p6 [2.01, 1.29, 3.43], p7 [1.78, 1.18, 3.21], p8 [2.54, 1.60, 4.10] — all at JPEG q85 noise level; **no noise page, no blocking difference.**

### 4.11 Visual inspection
All 8 cards viewed (not only P1/P6/P7/P8): P1 badge/dark band/numbers box/gloss 3-line wrap clean, headline flow ends well above row-B; P2 band subtitle fits one line, ssam photo + honest caption; P3 subway + Cézanne photos with credits, checklist box; P4 Bain photo, bracket diagram arrows clean; P5 library photo, numbers box; P6 table labels clear with no overlap; P7 clinic box, frame box, letters box ending inside its frame, phrase pitch comfortable, preview band; P8 sections A–H, writing glossline 2 lines with no orphan line at column-4 top, answer flow ending well above the footer. **No overlaps, clipping, or stray marks on any page.**

## 5. P8 adjudications (item by item)

- **#137 — true E redirection.** Key Dutch `7 november is Ipdong.`, note `Zie blz. 1`. (E = translate; this item's source side is Korean, so the key is the Dutch target.)
- **#138 — true E redirection.** Key Dutch `Nog 12 dagen tot het examen.`, note `Zie blz. 5`.
- **#139 / #140 — stems localised, keys frozen.** Stems Dutch (`Bijzondere maatregelen gelden alleen op 19 november. → ___` / `Op zaterdag ga ik naar Naejangsan om herfstkleur te zien. → ___`); keys remain Korean verbatim (`특별 조치는 11월 19일에만 적용돼요.` / `저는 토요일에 내장산에 단풍을 보러 가요.`); notes `Zie blz. 6` / `Zie blz. 3`. (These are the reverse-direction E items: Dutch stem → Korean answer.)
- **#104 — admissible Korean headword citation.** Note `104. A — 절기 = de 24 seizoenen van het jaar`; the cited headword comes verbatim from this issue's own P7 A2 exercise #104 stem `'절기'는 무슨 뜻이에요?`. Freeze multiset net effect is 0 (the extra 절 is offset by a 기 lost when the core P8 writing glossline was localised); the only net-new CJK character is 절 ×1.
- **#109 — no artefact.** Printed line `109. 기준 — Andere criteria, andere data (blz. 3)`; key identical to core verbatim. The old tool's [109,137,138] reads [137,138] under the new tool, as expected.
- **#150 — apparatus line, not a keydiff.** `150. ✓ Het voorbeeld staat in deel H van deze pagina (157 tekens)`.

## 6. Reader letters corner (P7, KO×FR model)

- Korean letter body and Korean disclosure `lko` frozen verbatim.
- Short note: `Voorbeeldbrief van de redactie, geen echte brief.`
- Dutch disclosure + solicitation (single paragraph, on the page): `Tot de deadline kwamen er geen echte brieven en geen beste teksten van blz. 8 binnen: het voorbeeld blijft staan en de belofte schuift door naar VOL.3. Stuur ons je brief en je beste tekst van blz. 8 op!`
- This covers all three facts (no real letters, no best P8 essays, both carried to VOL.3) plus an explicit imperative solicitation covering BOTH letters and best P8 texts in the same sentence. No names, letters, or quotes were invented. Preview lines, content previews, and other pages' exercises are not counted as solicitation.

## 7. Rounds and baselines (full sha256 before every fix; build dir never reset)

- **Round 1 (first render):** TOTAL 150, levels/pages/types/model 157 chars all = core; but P1 headline FLOW OVERFLOW (col 2 y=1743 need 99, bottom 1828, flow end 1942), P7 preview 2639.94 (>2540), P8 key-flow cursor 2547 (>2540); canonical audit 4 flags (P1 LINEX×2, TEXTX×2, all headline-flow tail pushing row-B). Content gates already passed (freeze p1–p7 new CJK=0, p8 net 절×1; p8 CLEAN [137,138]). Baselines: `round1-svg-sha256.txt`, `round1-full-sha256.txt`.
- **Round 1→2 fixes (transform.py only, regenerated from `orig/`, single-process re-render):** (1) P1 gloss shortened to 3 clean lines (`입동 = Ipdong · 절정 = piek · 상륙하다 = landen · 김장 = winterkimchi · 온대저기압 = extratropische cycloon.`, breaks all at `·`); (2) P7 phrase pitch 132→102 in both places (`(i % 4) * 132` and `py = fy + 66 + 4 * 132 + 18`, KO×FR precedent; ~26px line gap); (3) P8 column-4 line saving: #115 note → `Examen Koreaanse geschiedenis: zaterdag 28 november`, #136 note → `Plaats van de handeling: «에서»` (each 2 lines → 1 by wrap simulation). Result: P1 headline end 1413/1828 (= core value), zero FLOW OVERFLOW / HEAD TOO WIDE; P7 preview 2519.94; P8 cursor 2516; SVG diffs exactly p1/p7/p8, p2–p6 byte-identical. Baselines: `round2-full-sha256.txt` (also saved as `baselines-round3-pre.txt`).
- **Round 2→3 fix (transform.py only):** P8 writing glossline 3 lines → 2 (`Schrijfopgave (niet één juist antwoord). Hieronder een voorbeeld van {NCHARS} tekens.`, faithful to core `쓰기 문제예요 (정답은 하나가 아니에요). 아래에 157자의 예가 있어요.`; the 3rd line `van 157 tekens.` had been pushed to column-4 top as an orphan). Result: P8-ex flow end 463→403, zero overflow warnings; diffs exactly p8 SVG + p8 card + both PDFs. Baselines: `round3-svg-sha256.txt`, `round3-full-sha256.txt`.
- Two intermediate round-2 edits failed their assertions and were NOT written (pitch anchor, content8 duplicate anchor); the renders in between reproduced round-1 output and are not counted as rounds. The effective round-2 output is the third, successful render.
- Core SVGs after round 3 re-check: p1 `f1e6913d…f9b5e`, p2 `839dcdd0…6509c1`, p3 `74371179…899b34`, p4 `7f0aed9b…0902`, p5 `68e6ead9…85a3d`, p6 `e7f53e42…90a39`, p7 `ddb4e76c…6594`, p8 `17031514…646401` — unchanged from baseline.

## 8. Manifest (round-3 final)

| File | Bytes | sha256 |
|---|---|---|
| svg/p1-pyoji.svg | — | `1118d884faa35a86aba96f00037293e5dcb7f2e290948c4462197f30416cbaae` |
| svg/p2-saenghwal.svg | — | `7ddac1342d2b45b102362b8bfd3827f27e5711ea738ba7c5ace2f49aae032ac1` |
| svg/p3-munhwa.svg | — | `30ec68a114b4e9474851ee65316223956f449a974eec4bff67b5798ea7eee12a` |
| svg/p4-seupocheu.svg | — | `43ff0d6b849a5ac296ea4701a4459acba54d5ea0e41cea1b82b4a1786e148b1e` |
| svg/p5-cheongnyeon.svg | — | `7f43648a7321cfe79b654d4cfbe415ca6ceba2897419c68b54172a052a8ec5e4` |
| svg/p6-gipi.svg | — | `b8c25728be720c0487aa932489a7ffda9bc3442ef68915d64ea6e2e4beb96b74` |
| svg/p7-mal.svg | — | `cbc59fecb10cc3c6f5f56f38d6d16cc51056c7272945bd95fc345050f9aab904` |
| svg/p8-siheom.svg | — | `76a880545acde83371966e61e6b43f644ee56974a553b1b0acbdb69052cb9739` |
| cards/p1-pyoji.png | 1,494,403 | `d501c7b005c2132b57997f43febd4297432e1008b2da4adae9f9940518dbf844` |
| cards/p2-saenghwal.png | 1,132,724 | `5d0ecb360b4e4da0e7ca8a25b075639107f026cdd273f4eeff8650feafc55ebd` |
| cards/p3-munhwa.png | 1,310,760 | `696327cf3e10738daaa749a69b5ad85c45f52ef01a67d074ed709d2fc6987348` |
| cards/p4-seupocheu.png | 1,026,334 | `c3999921055a0f61e7797b24754c145be6a37aba36ecdbc3e2c2a88b855b7830` |
| cards/p5-cheongnyeon.png | 1,112,532 | `912f913b2812f9738a236e9a56e1023914d07ea26bcd0bde8fbbbc20c3182971` |
| cards/p6-gipi.png | 857,568 | `7ebb9dbdadcf852d685039a2909bb5c1d5eb2d6619da5cd5608fd6b9ea0eac0e` |
| cards/p7-mal.png | 728,727 | `3d65615a4f2f1099508a9c3c55fe9fb4b5e05f1e0a96e1d4f4a55d638fb6e4a5` |
| cards/p8-siheom.png | 1,099,803 | `4b0031affc52ba6c96e062aaaf5d7d5b37c2d53eda8c3ea0b7b6186f5a12d1d0` |
| Lucerna-VOL2-NL.pdf (print) | 32,552,178 | `dc95ad2cbba52699918006eb85fc8bdf5f45bc57bd9b16ca02d7b7e1e804e10a` |
| Lucerna-VOL2-NL-web.pdf (web) | 3,547,923 | `4fa8990c62b3cc05e33dd3f290e304911b89bfd0f05f733b7cf2c62c3b62ac99` |

Full manifest file: `hidden_files/weekly-report-w45-ko-nl-build/round3-full-sha256.txt`. Files were not modified after the round-3 render, so manifest hashes are the delivery hashes.

## 9. Inherited core fact debt (inherited, not re-judged, no new claims added)

- Korean Series 2 November start carries a rain-delay caveat (issue uses `발표된` wording + deadline note); playoff G1 (26 October) result was unknown at deadline — no score printed.
- Champi record assertion deleted at core level.
- Ipdong 7 November / Sosul 22 November come from calendar blogs (KASI official site not retrieved).
- Korean-history exam details are second-hand reports.
- Commons photo gaps: no verified PD/CC0 Korean foliage / kimjang / Korean-student-study photo; the ssam photo is honestly captioned as not kimjang.

## 10. Differences from sibling KITs (method notes, not corrections)

- Gloss caliber: this KIT reports AST 85 (= rendered 85). KO×PT's 66 and KO×FR's 84 reflect different counting definitions; the programme-level definition (README #21) is pending a parent decision — this edition only guarantees equality with the core.
- P8 separators follow the W43 NL measured form `— Pagina N —`, not the frozen Korean separator form used by KO×PT / KO×FR.
- P7 letters corner follows the KO×FR model (frozen Korean letter + frozen Korean disclosure + Dutch single-paragraph disclosure/solicitation), not the KO×PT replacement-disclosure model.
- The core P7 letters-box formula underestimation (~26–29px) was worked around with slack in this edition; fixing the core formula is a separate decision.

## 11. Open items

- Independent proofread not yet performed: this edition is builder-complete, not finally approved.
- Repo insert (LucernaRead/weekly) is the coordinator's serial step; not done here.
- Discord delivery remains paused by the user's standing decision; nothing was queued or sent.
