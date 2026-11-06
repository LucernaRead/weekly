# Lucerna 日本語版 VOL.1 · Edición en español （日本語テキスト＋スペイン語解説） — WEEKLY-KIT

> Target: Japanese (frozen JA core VOL.1) · Reader native language: **Spanish**
> Pairing badge (P1): «TEXTOS EN JAPONÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES»
> Week: Mon 19 – Sun 25 Oct 2026 (W43) · VOL.1 · 8 pages · **150 exercises**

**Independent proofread: PASS** — one complete independent pass, zero problems in the paper (see §9; one documentation defect in this KIT's §2 hash table was found and corrected by the proofreader).

---

## 1. What this edition is

The fan-out of the finalized Japanese core (files/weekly-report-ja-vol1/) for Spanish-speaking readers. The Japanese target text is the frozen core, byte-identical; only the explanation layer was rewritten natively in Spanish: every definition, grammar note, instruction, furniture label, and **all 150 P8 answer notes** are in Spanish. There is no intermediary language anywhere in the paper, this KIT, or the build code (the core's explanation-render method was renamed `expl()` in this build).

## 2. Baseline proof (fan-out step 1)

- Build dir: hidden_files/weekly-report-ja-es-build/ — a copy of the core build dir (hidden_files/weekly-report-ja-build/).
- Before any edit, the unmodified copy was rebuilt and its 8 SVGs compared to the shipped core (files/weekly-report-ja-vol1/svg/): **8/8 byte-identical (sha256)**.

| page | sha256 (baseline = core) |
|---|---|
| p1-hyoushi | db328eb836828953029fbc12d1230120a9237203332957a463e6782085f63943 |
| p2-kurashi | ef09afebfbd9f86e1ac8dae4e79e3fcb1b60f06a3192fd3747776840e0e9717f |
| p3-bunka | 07e44381687ec3400d05d27f64d4082351d570bb8b6a29178f46e0e7e6c0211d |
| p4-supotsu | 01ade8a450694c8f237145da4e5f56b30016c5859df0718b58e5246c8647eaaf |
| p5-wakamono | 403dd3db6bf408077ae4dbb56c630cfeee5aa1a169cd00bbe84e96e8f300af0a |
| p6-fukayomi | 8a92c611cd503f6997de9a7c6013a36321efda96cee421f9d4ed5cef53f51afb |
| p7-kotoba | 40984ce36c5cc042b3af36f409865b5a367316c1c58c8e5851e3436197f8186a |
| p8-tesuto | 355de22c1d74c51bbeecdf956799f7f3129cd4bdfac0eea65c6f8b3dc45a2acb |

Core registry re-derived from the core build in the same run: **150 exercises — A2 48 · B1 75 · B2 27**; per page 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38. Writing model character count: 150 characters (registry count), identical to the printed claim on P8.

## 3. Totals (this edition = core)

- **150 exercises** — A2 48 · B1 75 · B2 27; per page 10/18/18/18/18/18/12/38 (registry-compared item by item against the core: number, page, and level identical for all 150).
- Type counts (Spanish labels): Completar 51 · Opción múltiple 50 · Texto con huecos 13 · Emparejar 12 · Verdadero o falso 11 · Formar una frase 8 · Traducción 4 · Redacción 1. (The core's 語彙マッチ type renders on P7 without a printed type label, as in the core.)
- Instruction strings: Completa / Forma una frase / Verdadero/falso / Traduce / Redacción; matching: «Une cada lugar con su fecha» (P2), «Une cada evento con su lugar» (P3), «Une palabra y definición» (P8 — see §7).

## 4. What changed vs the core (explanation layer only)

Freeze diff (multiset of SVG text nodes, this edition vs core; image payloads byte-identical on all 8 pages):

| page | nodes removed | nodes added |
|---|---|---|
| P1 | 19 | 21 |
| P2 | 29 | 31 |
| P3 | 22 | 24 |
| P4 | 21 | 23 |
| P5 | 26 | 27 |
| P6 | 22 | 23 |
| P7 | 36 | 41 |
| P8 | 177 | 182 |

Every changed node was reviewed line by line: all are explanation-layer items (Nota boxes — gloss prefix «Nota — » —, bilingual section/box titles, pairing badge, footers «Lucerna · SEMANARIO JAPONÉS VOL.1 · TEXTO EN JAPONÉS · EXPLICACIONES EN ESPAÑOL» / «Página N de 8», band subtitles, quiz/phrase/answer apparatus) plus the documented reader-language items in §5. The one structural note: the core's Japanese-language instruction lines printed above exercise sections on P2–P6 belong to the target layer and are unchanged; the core's three Chinese glosses inside P7 and one Chinese line on P8 were explanation layer and are now Spanish. Caption credit lines are byte-identical to the core (JA-column precedent).

Masthead geometry follows the shipped JA-column fan-outs: wordmark raised (y 262→248), edition line 330→316, badge at y=356 (19 pt bold, brick #a4553a, centered — measured 1015.8 px wide, fits), Japanese subline 372→390, double rules at 406/413, black band unchanged at y=424. The Japanese edition line «日本語版 · VOL.1 · …» and the date line «2026年10月19日（月）〜25日（日）» are core text and unchanged.

## 5. Key-diff registry (the only key changes vs the core)

All 150 answer **notes** are Spanish (apparatus). The **keys** themselves are identical to the core except:

| # | type | core key | this edition's key | why |
|---|---|---|---|---|
| 137 | Traducción | 京都御苑を12時に出発します。(full Japanese sentence) | «La procesión sale del jardín imperial de Kioto a las 12.» (note: Ver página 3) | The exercise asks the reader to translate the Japanese sentence **into their own language**; the model answer is therefore Spanish here. |
| 138 | Traducción | 2,000円の罰金です。(full Japanese sentence) | «Tirar basura cuesta una multa de 2.000 yenes.» (note: Ver página 5) | Same re-aiming as #137. |
| 150 | Redacción | apparatus: Chinese open-question marker | apparatus: «(pregunta abierta — modelo a continuación)»; note: «El modelo está en la sección H de esta página (150 caracteres)» | Open writing exercise; only the apparatus line is language-dependent. Model text (150 characters) unchanged. |

Exercises **#139 / #140** (sentence cloze) keep Japanese keys byte-identical to the core （読書週間は来週の火よう日から始まります。/ 私は池袋のハロウィンのイベントに行きたいです。); only their **prompt sentences** are printed in Spanish on P8 («La Semana de la Lectura empieza el martes que viene. → ＿» / «Quiero ir al evento de Halloween de Ikebukuro. → ＿»), because the task is to complete the Japanese sentence from a meaning given in the reader's language.

Answer-key format: this core's house format `n. key — note` (em dash) is kept, matching all shipped JA fan-outs; inside notes and keys, parentheses are half-width with a space before the note parenthesis where one occurs (e.g. #150).

## 6. Content checks

- **P7 phrases of the week**: each of the 8 quoted sentences occurs exactly twice in the issue text (once in its article, once in the P7 section) — verified programmatically; Spanish translations carry page tags (Página 1–6) matching the source pages.
- **Weekdays/dates** re-verified against the real 2026 calendar (Python datetime): Oct 17 Sat, 18 Sun (games opened), 19 Mon, 20 Tue, 22 Thu (Jidai Matsuri; ticket general sale 12:00), 23 Fri (Irohazaka), 24 Sat (**Japan Series G1, 18:30, Yokohama Stadium, DeNA vs SoftBank**), 25 Sun (G2 18:00; Yabusame 15:00), 27 Tue (Reading Week starts), 31 Sat (Halloween). Every claim in the Japanese text and the Spanish notes matches.
- **Numbers**: scores 671+671=1,342 (33-point gap) ✓; records 91勝49敗 (.650) / 71勝69敗3分け ✓ internally consistent; ekiden 10時間31分30秒； 1分46秒 = 106 s ✓; chart 34+28+22+16 = 100 %, bar lengths proportional (×30 px) ✓; 168 % ≈ 2.7× ✓; model essay = 150 characters (registry count) = the printed claim ✓.
- **P8 section H reference** («el modelo va a continuación») and the P7 readers'-corner VOL.2 promise mirror the core's own promises; nothing new promised.

## 7. Geometric occlusion audit (builder-run)

Script: paint-order scan of the final SVGs with real-font (PIL) glyph metrics; ink band baseline −0.88 em … +0.30 em; line boxes expanded by half the stroke width; checks: ≥30 % glyph coverage by later opaque shapes, lines crossing text ink, non-footer ink in the footer band (y > 2580), page-edge spill, text-vs-text overlap, box titles vs their box borders. **Synthetic positive control passed** (all defect classes fire on a planted test page) before the real run.

Final run: **4 flags, all pixel-adjudicated NON-DEFECTS** on the rendered cards:

1. TEXTX P1 — wordmark «Lucerna» vs the edition line: blackletter ink-band overestimate; the rendered card shows clear air between the wordmark descenders and the edition line (same geometry family as the core).
2. LINEX P2 — model sentence vs the gold rule at y=1804: measured ink on the card ends at row 1800 (1 stray px at 1801), rule occupies 1803–1805 → ≥2 px clear. Identical geometry to the core.
3. TEXTX P7 (×2) — adjacent-column Japanese lines: overlap-box ink counts on this edition's card (40 px / 122 px) are **identical to the core card's** — frozen-core geometry (a kinsoku-widened line ends ~6 px before the next column's ink begins; no contact). Unchanged from the shipped core.
4. **One real defect found and fixed during the build**: the P8 matching instruction «Une cada palabra con su definición» (316.7 px from x=1185) ran into the next column — its final glyphs touched the Japanese exercise text (visible in the rendered card). Shortened to «Une palabra y definición» (220.2 px, ends x=1405 < column edge 1423), page re-rendered; the flag is gone and the fixed area was re-inspected visually.

Also verified visually on all 8 cards: the P1 word-of-week gloss «見頃（みごろ）＝ época ideal para verla.» wraps to exactly one line (19 pt, 312.9 px ≤ 434) and clears the section rule below it — the two-line strike-through defect of the French build of this core does not occur here. Three bilingual box titles from the French build's fix list were pre-measured and shortened to fit: «数字で見る今週 · Semana en cifras» (377.4 ≤ 398), «『見頃』の使い方 · Uso de «見頃»» (359.8 ≤ 398), «今週のフレーム · Frase semanal» (346.3 ≤ 390); the audit's box-title check reports zero overflows on all pages. Build log: zero FLOW OVERFLOW, zero HEAD TOO WIDE; P8 keys end at y=2413 (< 2540 strip), P7 teaser ends 2514 (< 2540).

## 8. Deliverables & pins

Directory: files/weekly-report-ja-es/

- svg/ ×8, cards/ ×8 (1950×2700 PNG)
- **Lucerna-VOL1-ES-web.pdf — 3,181,949 bytes · sha256 066adb33324cd35b9fd43e2aa1f7251ebbba97b7ba9c53dd76e00aa6de4af63d** (< 10 MB, JPEG q≈85 pages)
- Lucerna-VOL1-ES.pdf (print) — 42,002,524 bytes · sha256 1d454dc57c75d4c0b109e38bd66a48e7464fc7befe1021cb491fb72b954fb2bc
- WEEKLY-KIT.md (this file)

Build code: hidden_files/weekly-report-ja-es-build/ (run.py + render.py; content files content12/34/56/7/8.py; svglib.py with the explanation method named expl()).

## 9. Proofread record

- Builder's own full pass: COMPLETE — registry re-derived and compared item-by-item with the core; freeze diff reviewed node by node; all Spanish read in the rendered cards (8/8 pages visually inspected); weekday/number checks in §6; geometric audit in §7.
- **Independent proofread: PASS (2026-10-21).** One complete independent pass by a fresh proofreader who did not build this edition; zero problems in the paper. Discord delivery is paused (user instruction 2026-10-21): this edition goes to the GitHub weekly repo only. Evidence per gate check:
  1. **Freeze diff vs core** (proofreader's own text-node multiset diff of the final SVGs, per page removed/added = 19/21, 29/31, 22/24, 21/23, 26/27, 22/23, 36/41, 177/182 — identical counts to §4): every removed node is a Chinese explanation-layer string or pairing furniture; every added node is its Spanish equivalent or a §5 registry item. No Japanese target-text change outside the registry. The core's Japanese instruction lines on P2–P6 are unchanged (absent from the diff). Han-character set of the edition ⊆ the core's — no foreign CJK entered the paper.
  2. **Spanish apparatus completeness**: all glosses (prefix «Nota — »), instructions, box titles, clinic notes, phrase translations, furniture and all 150 P8 notes are Spanish. Residual-Chinese scan: none in the text layer (every Chinese node of the core is gone) and no CJK anywhere outside `<text>` elements in the raw SVG bytes.
  3. **All 150 keys re-derived**: AST extraction of the exercise registry from both build dirs (141 calls; match_sets expand to 12) — keys identical to the core for every item except exactly #137/#138/#150 (§5). #137 «La procesión sale del jardín imperial de Kioto a las 12.» and #138 «Tirar basura cuesta una multa de 2.000 yenes.» verified faithful to the printed Japanese stems (行列は京都御苑を12時に出発します / ゴミを捨てると、2,000円の罰金です). #139/#140 keys byte-identical Japanese; only their stems are Spanish. All 150 printed P8 lines read against the core's; the Spanish notes assert the same facts as the core's Chinese notes; arithmetic re-checked (671+671=1,342, 33-point gap, 34+28=62, 22−16=6, 1分46秒=106 s, chart sums to 100 %).
  4. **Totals/levels**: the proofreader re-ran a pristine copy of the core build (OUT redirected to scratch): registry prints TOTAL 150 — A2 48 · B1 75 · B2 27; per page 10/18/18/18/18/18/12/38; type counts identical to §3's Spanish labels. Printed P8 numbering 1–150 continuous, each exactly once.
  5. **P7 phrases**: each of the 8 quotes occurs exactly 2× in the normalized full-issue text (also 2× in the core); page tags Página 1, 1, 2, 2, 3, 4, 5, 6 match the core's source pages.
  6. **Calendar** (system date, Asia/Tokyo): Oct 17 Sat, 18 Sun, 19 Mon, 20 Tue, 22 Thu (Jidai Matsuri), 23 Fri (Irohazaka), 24 Sat (**Japan Series G1, 18:30, DeNA vs SoftBank** ✓), 25 Sun (G2), 27 Tue (Reading Week), 31 Sat (Halloween) — all claims match.
  7. **Pairing furniture**: P1 badge exactly as §header (visually confirmed on the card, one line, fits); footers «Lucerna · SEMANARIO JAPONÉS VOL.1 · TEXTO EN JAPONÉS · EXPLICACIONES EN ESPAÑOL» / «Página N de 8» on all 8 pages; masthead «Lucerna» with no article (visually confirmed).
  8. **Geometric occlusion audit** (proofreader's own script: paint order, PIL real-font glyph metrics with JP face, ink band −0.88 em…+0.30 em, line boxes expanded by half stroke width; synthetic positive control fired all six classes — COVER/LINEX/FOOTER/EDGE/BOXTITLE/TEXTX — before the real run): final SVGs = **4 flags, all pixel-adjudicated NON-DEFECTS** — (a) TEXTX P1 wordmark vs edition line: rendered card shows 30 rows of clear air between wordmark ink (ends row 251) and edition-line ink (starts row 282); (b) LINEX P2 model sentence vs gold rule: sentence ink ends row 1801, rule occupies 1803–1805, identical measurement on the core card (frozen geometry); (c) TEXTX P7 ×2 adjacent-column: ink-pixel counts inside the two intersection boxes are identical between this edition's card and the core card (154 = 154; 256 = 256) — frozen-core geometry, no contact. No COVER, EDGE, BOXTITLE or FOOTER flags; lowest P8 key ink bottom = 2534 (< 2580 rule). The in-build P8 fix was visually confirmed on the card: «Une palabra y definición» (x 1185…1411) ends before the column edge (1423) with clear space before the next column's text. P1 word-of-week gloss «見頃（みごろ）＝ época ideal para verla.» is one line, ink bottom 1836 vs the rule at y=1844 (geometry + crop inspection).
  9. **Images & PDFs**: base64 image payloads byte-identical to the core on all 8 pages; credit lines are unchanged text nodes travelling with the identical images. Web PDF measured by the proofreader: **3,181,949 bytes, sha256 066adb33324cd35b9fd43e2aa1f7251ebbba97b7ba9c53dd76e00aa6de4af63d** (< 10 MB ✓); print PDF 42,002,524 bytes, sha256 1d454dc57c75d4c0b109e38bd66a48e7464fc7befe1021cb491fb72b954fb2bc; both PDFs have 8 pages.
  10. **Banned-term scan**: 0 hits (Chinese and English forms) in the paper SVGs, this KIT, and the build code (`expl()` rename confirmed in the ES build's bslib4.py).
  11. **Baseline claim — substance verified, table corrected**: the proofreader's pristine reproduction of the core build reproduced all 8 shipped core SVGs byte-identically (8/8), confirming the §2 claim. However, the eight sha256 values originally printed in the §2 table matched neither the shipped core files nor the reproduction (nor a core-content + ES-bslib4 control build); the table has been corrected by the proofreader to the true core hashes (db328eb8…, ef09afeb…, 07e44381…, 01ade8a4…, 403dd3db…, 8a92c611…, 40984ce3…, 355de22c…), each measured identically from the core files on disk and from the independent reproduction. Documentation-only defect; no paper artifact was touched, so no re-render was required and the zero-problem pass above stands on the unchanged artifacts.

---

## Patch note — 2026-10-21 · Core-level correction: P7 vocabulary-deck column-seam overprints (geometry only)

**Defect (found by the JA×PT independent proofread, §13; record: hidden_files/ja-p7-overprint-correction.md).** Two frozen Japanese lines on P7 wrapped past their column and overprinted the neighbouring column's first glyph, producing merged illegible glyphs: (a) B1 column (x=527, baseline y=336.86) line ending …スタジアムで大き vs B2 column (x=989) という意味です…; (b) A2 column (x=65, baseline y=369.54) line ending …季節で vs B1 column (x=527) な声… Inherited from the JA core by every shipped JA fan-out; earlier "visually clean" adjudications of these flags were wrong and are superseded.

**Diagnosis.** The wrap width metric is correct (PIL, Noto Serif CJK JP; every greedy pre-kinsoku line fits the 434-unit column). The defect is in the kinsoku oidashi loop in `svglib.py` `wrap()`: pulled glyphs are never re-measured, and a line starting with a NO_START chain pulls one glyph per pass — B1's line cascaded 3 pulls (』→！→な) to 23 glyphs = 491.92 units (+57.92 over the limit; ≈30 units of ink past the 462-unit column pitch), A2's line cascaded 2 pulls to 471.28 (+37.28; ≈9 units past the pitch). A programme-wide census of the core found 16 overfull lines; only these 2 exceed the 28-unit gutter (all others ≤17.50 over, ink inside the gutter, shipped and audit-clean).

**Fix (identical in all 7 JA build dirs; patched `svglib.py` md5 d73e23b365676c3618d7e060b835eb4d in each).** New module constant `SEAM_SLACK = 28` (grid pitch 462 − column width 434). `wrap()` now records pre-kinsoku line widths and, after the oidashi loop, repairs ONLY lines oidashi itself grew past `max_w + SEAM_SLACK`: trailing glyphs are shed to the head of the next line until the line fits `max_w` again (cascading forward; a NO_START glyph is shed together with the preceding glyph so no line starts with one). No content string changed; no other wrap result in the issue changes (verified below).

**Verification (this edition).** Pages 1–6 and 8 SVGs byte-identical to the previously shipped files. P7 SVG differs in exactly 4 text elements — the two seam line pairs, at unchanged coordinates (A2 lines at y=369.54/402.22: …本を読む季節で→…本を読む季 / す。→節です。; B1 lines at y=336.86/369.54: …スタジアムで大き→…スタジアム / な声が聞こえます。→で大きな声が聞こえます。); concatenated text identical on all 8 pages; exercise registry unchanged (150). Geometric occlusion audit (ink-extent, synthetic positive control passed): flags 23 → 21, the delta being exactly the two P7 TEXTX seam flags removed, zero new flags. Pixel check on the rendered P7 card: seam (a) B1 ink now ends at column 962, B2 ink starts 994 (31 clear columns); seam (b) A2 ink ends 502, B1 ink starts 528 (25 clear columns) — glyphs no longer touch at either seam.

**Pins.** Web PDF: 3,181,949 B / sha256 066adb33324cd35b9fd43e2aa1f7251ebbba97b7ba9c53dd76e00aa6de4af63d → **3,182,466 B / sha256 2b33ab3d63db3c0d84903e8bed1a5d940a95b5d0c3b77ac755496c31cdf7dd09**. Print PDF: 42,002,524 B → 42,002,518 B. Repo re-pin by the main line.
