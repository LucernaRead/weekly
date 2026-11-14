# Lucerna Weekly VOL.1 — JA × IT （日本語正文 + 意大利语讲解）

Edition: Japanese target text (frozen VOL.1 core) with ALL explanations in Italian, for Italian-speaking readers.
Build dir: hidden_files/weekly-report-ja-it-build/ · Deliverables: files/weekly-report-ja-it/

## 1. Baseline proof
- Core build dir copied to hidden_files/weekly-report-ja-it-build/ (assets included, __pycache__ excluded), OUT repointed to scratch/baseline-svg, run UNMODIFIED.
- Result: **8/8 SVGs byte-identical** to the shipped core (sha256 vs scratch/core-shipped-hashes.txt).
- Baseline registry: 150 exercises (A2 48 · B1 75 · B2 27); per-page 10/18/18/18/18/18/12/38; model composition exactly 150 chars.
- Core re-verified untouched AFTER all work (final check): sha256sum -c → **8 OK**.

## 2. Totals (identical to core)
- Exercises: **150** — A2 48 · B1 75 · B2 27; per-page 10/18/18/18/18/18/12/38.
- Types (Italian labels): completamento 51 · scelta multipla 50 · cloze 13 · abbinamento 12 · vero o falso 11 · costruzione di frasi 8 · traduzione 4 · scrittura 1.
- Build log: no flow overflow, no head too wide. P8 answers flow ends y=2428 < 2540 (core: 2366).

## 3. Key-diff registry (complete — the ONLY registry differences vs the core)
Translation-type items re-aimed at Italian; all other 145 keys byte-identical (verified programmatically, scratch/verify.py).
- **#137** (traduzione, stem stays 行列は京都御苑を12時に出発します。): key → «La processione parte dal Kyoto Gyoen alle 12.» · note → «Vedi pagina 3»
- **#138** (traduzione, stem stays ゴミを捨てると、2,000円の罰金です。): key → «Se butti i rifiuti, la multa è di 2.000 yen.» · note → «Vedi pagina 5»
- **#139** (traduzione): stem re-aimed → «La Settimana della Lettura comincia martedì prossimo. → ___», instruction «Traduci in giapponese»; key UNCHANGED 読書週間は来週の火よう日から始まります。 · note → «Vedi pagina 7»
- **#140** (traduzione): stem re-aimed → «Vorrei andare all'evento di Halloween di Ikebukuro. → ___», instruction «Traduci in giapponese»; key UNCHANGED 私は池袋のハロウィンのイベントに行きたいです。 · note → «Vedi pagina 5 (l'evento di Ikebukuro)»
- **#150** (scrittura, apparatus only): key → «(compito aperto — testo modello qui sotto)» · note → «Testo modello nella sezione H di questa pagina (150 caratteri)» · section-H instruction line in Italian.
- ALL ~150 registry notes translated into Italian — including the notes the core itself kept in Japanese. Answer format unchanged (JA family): «{n}. {key} — {note}», separators «— Pagina {pg} —».

## 4. IT furniture (verbatim, as shipped)
- P1 badge (brick slot, y=356, sibling geometry shift): «TESTI IN GIAPPONESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI» — measured 811.7px at 19pt bold sans (inner width 1820) ✓
- Footers: left «Lucerna · SETTIMANALE GIAPPONESE VOL.1 · TESTI IN GIAPPONESE · SPIEGAZIONI IN ITALIANO» (892.9px) / right «Pagina N di 8» (116.8px) — no overlap ✓
- Gloss prefix: «Nota — »
- Masthead: «Lucerna» (no article), exactly as the core ships.
- P1 top strip: «毎週、日本語で · Ogni settimana · 日本人が読んでいる日本語を読む» (652.4px centered; no collision with the VOL.1/date items) ✓
- P8 answers header: «答え · Risposte — raggruppate per pagina: basta cercare il numero» + right «Una breve nota in italiano per ogni risposta · ✓ = la domanda con il testo modello» (804.8 + 733.0 < 1820) ✓
- Band subs measured: P2 508.0 · P3 566.6 · P4 515.7 · P5 486.0 · P6 591.9 · P7 576.5 (all ≤ band width) ✓. P4 band title_left «スポーツ · 体育» deliberately unchanged (JA-family convention, as in EN/DE/FR/ES siblings); P8 band sub unchanged (no Chinese in it).

## 5. Printed-note set verification (mandatory gate)
- Method (scratch/verify.py): registries dumped independently from core and IT builds; printed P8 answer entries extracted from both SHIPPED P8 SVGs.
- Registry key diffs: exactly #137, #138 (+ #150 apparatus) — as documented in §3.
- **Printed P8 entries: core 150, IT 150; sets EQUAL ({1..150} = {1..150}); no missing numbers.** The JA core prints all 150 notes (print-all rule) and so does this edition.
- P7 phrases: all 8 phrases occur exactly **2×** in the full text of BOTH editions (article + phrase box); IT translations sit under each quote with (p. N) tags; the VOL.2 promise in the readers'-corner note is preserved in Italian.
- Images: <image> payload lists per page **identical** to the core on all 8 pages.
- Freeze diff (per-page text nodes, core vs IT): every differing node classified — explanation layer / pairing furniture / §3 registry items. No Japanese target text changed.
- Residual-Chinese scan on the final SVGs: 0 simplified-Chinese explanation fragments. (Two character-class hits were legitimate Japanese words: 写真 in photo credits, 翻訳 in the P8 section head.)

## 6. Geometric occlusion audit (mandatory gate)
- Script scratch/audit.py: paint-order SVG parse, real-font (PIL) glyph metrics via the build's own svglib, ink band −0.88em/+0.30em, line boxes expanded by half stroke width; classes COVER / LINEX / FOOTER (y>2580) / EDGE / SPILL incl. every box title's ink vs its own box borders. **Synthetic positive control: PASS** (all 5 classes fire; clean control text unflagged). Core reference run: 5 flags (known graze classes).
- First IT run found **4 REAL defects — all box titles too wide at 23pt bold sans — fixed by WORDING only**:
  1. P1 numbers box: «数字で見る今週 · La settimana in numeri» (445.7px, ink to x=991 vs box right 961) → «数字で見る今週 · In numeri» (294.6px)
  2. P2 usage box: «『見頃』の使い方 · Come si usa «見頃»» (417.1px, ink 962 vs 961) → «『見頃』の使い方 · L'uso di «見頃»» (368.5px)
  3. P4 schedule box: «日本シリーズの日程 · Il calendario delle Series» (506.5px, ink 1052 vs 961) → «日本シリーズの日程 · Calendario» (353.8px)
  4. P7 frame box: «今週のフレーム · La frase della settimana» (453.8px, ink 1927 vs box right 1885) → «今週のフレーム · La frase tipo» (323.8px)
- Builder fix after visual pass: P2 match instruction «Abbina luoghi e date del picco» measured ink end x=1918.5 (inside the page frame 1922 but past the 1885 content margin; EN sibling ends 1872.5) → shortened to «Abbina luoghi e picchi» (ink end 1846.6). Wording only.
- Final audit: **4 flags, ALL pixel-adjudicated NON-DEFECTS** (scratch/pixelcheck.py on rendered cards): P2 LINEX — model-sentence ink ends row 1800, gold rule rows 1803–1804 (identical to core); P3 あなたは box — last IT line ink ends row 1227, border 1232–1233; P4 Ohtani ※ note — ink ends 960, border 962 (same numbers as the core's shipped geometry); P5 あなたは box — ink ends 1180, border 1186.
- **Final: 0 unresolved flags.**

## 7. Calendar verification (real 2026 calendar, `date`)
Oct 17 Sat · Oct 19 Mon · Oct 20 Tue · Oct 22 Thu · Oct 23 Fri · Oct 24 Sat · Oct 25 Sun · Oct 27 Tue · Oct 31 Sat · Nov 1 Sun · Nov 9 Mon · Jan 2–3 2027 Sat–Sun — every weekday claim in the paper matches.

## 8. Image credits (from the core KIT; all public domain / CC0, verified there)
- P1 stadium.jpg — Syced, CC0 (Wikimedia Commons)
- P2 maple.jpg — Poliphilo, CC0 · mochi.jpg — Fumikas Sagisavas, CC0
- P3 hiroshige.jpg — Utagawa Hiroshige III, public domain
- P4 waseda1911.jpg — Bain News Service, public domain
- P5 pumpkin.jpg — Petr Kratochvil, public domain
- P6 paraswim.jpg — EJ Hersom / US DoD, public domain (caption states it is NOT this event)

## 9. Method notes
- The transform was applied by a one-off script (scratch/transform_it.py, exact-count-asserted replacements, run once). Per the standing adjudicated exception, that scratch script quotes the core's original Chinese explanation strings and its original method call as search patterns during the rename to `expl()`; it is confined to scratch/ and is not operative code.
- The banned intermediary-layer term (Chinese or English form) occurs **0 times** in the paper SVGs, this KIT, and all operative build code (grep-verified).
- The core's Japanese `expl()` instruction texts (the section apparatus instructions in Japanese) stay unchanged — they are Japanese apparatus, as in all JA-family siblings; only the method was renamed.

## 10. Deliverables & PDF pins (final render, post-fix)
- svg/ ×8, cards/ ×8 (1950×2700 PNG) in files/weekly-report-ja-it/
- Print PDF: Lucerna-VOL1-IT.pdf — **41,998,365 B**, sha256 `e3706bd77063072ad5a9f88570f10f70b4d8c32557a3027ce70bdd57dca60385`
- Web PDF: Lucerna-VOL1-IT-web.pdf — **3,185,159 B** (< 10 MB ✓), sha256 `ff7f9af067feb6a0da9d63bb747c95bb606e8d889e09be7ab9a70ac31a5794dd`

## 11. Proofread status
- Builder's own full proofread: DONE (all 8 cards read end-to-end; all 150 keys re-derived against the Japanese stems/articles; Italian completeness confirmed on every page; the 4 fixed box titles verified inside their boxes on the cards).
- **Independent proofread: PASS — ZERO PROBLEMS (one complete independent pass, 2026-10-21).** No fixes were required; the shipped artifacts are byte-identical to the builder's final state (all 8 edition SVGs re-hashed unchanged at the end of the pass, and the frozen core's 8 shipped SVGs likewise 8/8 unchanged). Full record:
  - **Independence of verification**: the proofreader re-copied the unmodified core build to scratch (output repointed), reproduced all 8 shipped core SVGs byte-identically (8/8), dumped both registries from the actual build dirs, extracted all text elements from both editions' shipped SVGs, and ran the shipped IT build copy — it reproduces all 8 shipped IT SVGs byte-identically (8/8), so the shipped artifacts are exactly the build's output; its log confirms the P8 key flow ends at y=2428 < 2540.
  - **Freeze verdict: PASS.** Element-level diff of all 8 pages: every difference classifies as (a) explanation layer (Chinese gloss/note/instruction/clinic/あなたは prompt/P8 note → Italian), (b) pairing furniture (badge, footers «Pagina N di 8», «— Pagina N —» separators, exercise headers, instr labels, P1 strap line), or (c) a documented registry item (#137/#138 keys, #139/#140 stems, #150 apparatus, #139/#140 «Vedi pagina» notes). No undocumented Japanese-text change; kana-bearing diff lines are mixed furniture/gloss lines whose Japanese parts mirror exactly. Residual-Chinese scan of the edition: the only flagged characters are 都 (inside 京都, a Japanese proper noun) and 着 (Japanese verbs 着く/着た) — zero Chinese explanation text remains.
  - **Registry diff (proofreader's own dumps)**: page/level/type metadata zero mismatches; totals 150 (A2 48 · B1 75 · B2 27), per page 10/18/18/18/18/18/12/38; Italian type names map 1:1 onto the core's type counts. Key diffs = exactly {137, 138, 150}: #137 «La processione parte dal Kyoto Gyoen alle 12.» ✓ faithful to its stem; #138 «Se butti i rifiuti, la multa è di 2.000 yen.» ✓ faithful; #150 «(compito aperto — testo modello qui sotto)» ✓. **#139/#140 keys byte-identical to the core** ✓ (stems re-aimed «Traduci in giapponese», notes «Vedi pagina 7» / «Vedi pagina 5 (l'evento di Ikebukuro)» ✓). All other 147 keys byte-identical; all 150 notes rewritten in Italian (notes containing CJK contain only Japanese headwords being glossed). (Precision note on §3: the "5 registry items" = 3 key diffs + the 2 stem-only changes; 147 keys are byte-identical.) All 150 keys/notes spot-re-derived against the articles in a full read of all 8 pages; arithmetic re-added (671+671=1,342 margin 33; 91+49+3=143 = 71+69+3; .650; chart 34+28+22+16=100; #91=6; #92=62; #124 1分46秒=106秒).
  - **Printed-note sets: core P8 = {1..150}, edition P8 = {1..150} — EQUAL** (extracted by the proofreader from both shipped P8 SVGs; both carry the same 154 entry-start elements incl. #141–144 in exercise and answer areas). JA-family format «{n}. {key} — {note}» with «— Pagina N —» separators confirmed printed.
  - **P7 phrases**: each of the 8 phrases occurs exactly 2× in the whitespace-stripped full text of BOTH editions (counted programmatically); page tags (p. 1/1/2/2/3/4/5/6) correct. Writing model 『私の秋の週末』 identical to the core and 150 characters (registry count in both builds). Readers'-corner example labelled as the editor's in Japanese and Italian; VOL.2 promises carried in Italian; Japan Series printed strictly as preview.
  - **Calendar**: every printed weekday claim verified against the real calendar (Asia/Tokyo): Oct 17 Sat, 18 Sun, 19 Mon, 20 Tue, 22 Thu, 23 Fri, 24 Sat, 25 Sun, 27 Tue, 31 Sat, Nov 1 Sun, Nov 9 Mon, Jan 2–3 2027 Sat–Sun — all match, incl. Japan Series G1 Sat Oct 24 18:30 (DeNA vs SoftBank, Yokohama Stadium) and G2 Sun Oct 25 18:00.
  - **Geometric occlusion audit (proofreader's OWN implementation)**: paint-order parse, PIL real-font glyph metrics (validated: badge advance measures 811.80 px vs the builder's 811.7), line boxes expanded by half stroke width, box-border STRADDLE tests, text-vs-text tests; validated on a synthetic positive control in which all 6 planted classes (COVER/LINEX/FOOTER/EDGE/STRADDLE/TEXTX) fired and clean text stayed silent BEFORE the real run. Real run on the edition: **2 flags, both TEXTX on P7, both adjudicated NON-DEFECTS by pixel measurement on the shipped card** — adjacent-column line pairs (cols 1/2 at baseline 369.54; cols 2/3 at baseline 336.86): actual rendered ink gaps ≈5–6 px (col-2 line ink ends col 986, col-3 ink begins col 992), no shared ink; the flags are an em-box metric overestimate vs the renderer's true advances. All other pages: 0 flags.
  - **Builder's 5 fixes pixel-verified on the shipped cards**: P1 numbers title ink ends col 837 (box border 961) ✓; P2 usage title ink ends col 913 (border 1423; builder's 913.5) ✓; P4 schedule title ink ends col 898 (border 1423; builder's 898.8) ✓; P7 frame title ink ends col 1796 (border 1885; builder's 1796.8) ✓; P2 instruction «Abbina luoghi e picchi» ink ends col 1843 (margin 1885) ✓.
  - **Builder's 4 graze adjudications pixel-verified**: P2 model-gloss ink bottom row 1801 vs gold rule rows 1803–1805 ✓; P3 あなたは box last line ink bottom row 1227 vs border rows 1232.5–1233.9 ✓; P4 trend-box ※ note ink bottom row 959 vs border rows 961.9–963.3 ✓; P5 あなたは box ink bottom row 1180 vs border rows 1185.9–1187.3 ✓. All clearances ≥2 rows, zero shared ink rows — all confirmed non-defects.
  - **Images**: embedded <image> payloads MD5-identical to the core per page (1/2/1/1/1/1/0/0 = 7); printed credits unchanged from the core and matching §2's table; the P6 caption's not-this-event statement intact.
  - **Banned intermediary-term scan: 0 occurrences** (both script forms and the English form) in the edition SVGs, this KIT, and the operative build code (the scratch transform script's quoted search-pattern strings are the known, adjudicated residue and are not part of the operative build).
  - **PDF pins (measured by the proofreader)**: web `Lucerna-VOL1-IT-web.pdf` = **3,185,159 B**, sha256 `ff7f9af067feb6a0da9d63bb747c95bb606e8d889e09be7ab9a70ac31a5794dd`, 8 pages, < 10 MB ✓; print `Lucerna-VOL1-IT.pdf` = **41,998,365 B**, sha256 `e3706bd77063072ad5a9f88570f10f70b4d8c32557a3027ce70bdd57dca60385`, 8 pages. These are the builder's pins, confirmed — no superseding render was needed.

---

## Patch note — 2026-10-21 · Core-level correction: P7 vocabulary-deck column-seam overprints (geometry only)

**Defect (found by the JA×PT independent proofread, §13; record: hidden_files/ja-p7-overprint-correction.md).** Two frozen Japanese lines on P7 wrapped past their column and overprinted the neighbouring column's first glyph, producing merged illegible glyphs: (a) B1 column (x=527, baseline y=336.86) line ending …スタジアムで大き vs B2 column (x=989) という意味です…; (b) A2 column (x=65, baseline y=369.54) line ending …季節で vs B1 column (x=527) な声… Inherited from the JA core by every shipped JA fan-out; earlier "visually clean" adjudications of these flags were wrong and are superseded.

**Diagnosis.** The wrap width metric is correct (PIL, Noto Serif CJK JP; every greedy pre-kinsoku line fits the 434-unit column). The defect is in the kinsoku oidashi loop in `svglib.py` `wrap()`: pulled glyphs are never re-measured, and a line starting with a NO_START chain pulls one glyph per pass — B1's line cascaded 3 pulls (』→！→な) to 23 glyphs = 491.92 units (+57.92 over the limit; ≈30 units of ink past the 462-unit column pitch), A2's line cascaded 2 pulls to 471.28 (+37.28; ≈9 units past the pitch). A programme-wide census of the core found 16 overfull lines; only these 2 exceed the 28-unit gutter (all others ≤17.50 over, ink inside the gutter, shipped and audit-clean).

**Fix (identical in all 7 JA build dirs; patched `svglib.py` md5 d73e23b365676c3618d7e060b835eb4d in each).** New module constant `SEAM_SLACK = 28` (grid pitch 462 − column width 434). `wrap()` now records pre-kinsoku line widths and, after the oidashi loop, repairs ONLY lines oidashi itself grew past `max_w + SEAM_SLACK`: trailing glyphs are shed to the head of the next line until the line fits `max_w` again (cascading forward; a NO_START glyph is shed together with the preceding glyph so no line starts with one). No content string changed; no other wrap result in the issue changes (verified below).

**Verification (this edition).** Pages 1–6 and 8 SVGs byte-identical to the previously shipped files. P7 SVG differs in exactly 4 text elements — the two seam line pairs, at unchanged coordinates (A2 lines at y=369.54/402.22: …本を読む季節で→…本を読む季 / す。→節です。; B1 lines at y=336.86/369.54: …スタジアムで大き→…スタジアム / な声が聞こえます。→で大きな声が聞こえます。); concatenated text identical on all 8 pages; exercise registry unchanged (150). Geometric occlusion audit (ink-extent, synthetic positive control passed): flags 24 → 22, the delta being exactly the two P7 TEXTX seam flags removed, zero new flags. Pixel check on the rendered P7 card: seam (a) B1 ink now ends at column 962, B2 ink starts 994 (31 clear columns); seam (b) A2 ink ends 502, B1 ink starts 528 (25 clear columns) — glyphs no longer touch at either seam.

**Pins.** Web PDF: 3,185,159 B / sha256 ff7f9af067feb6a0da9d63bb747c95bb606e8d889e09be7ab9a70ac31a5794dd → **3,185,658 B / sha256 8baaf81656655e9d43f4e7a58080127377107698efe4e24f193f255e3bb28c52**. Print PDF: 41,998,365 B → 41,998,359 B. Repo re-pin by the main line.

---

## D5 rebuild (2026-11-13)

SOP §1.1 字体修复（D5）：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader；西里尔字母改走 Noto Sans；日文正文仍走 Noto Sans/Serif CJK JP。施工不 commit、不 push；入仓由独立重校后的 closer 做。工作日志：`hidden_files/d5-redo/scratch-2026-w43-ja/logs/2026-w43-ja-it/`；逐版报告：`production/notes/2026-w43/g-ja/scratch-d5-rebuild-ja/D5-REPORT-2026-w43-ja-it.md`。

**装机**：移植模板路线（D5-METHOD §1.7；安装器拒单已实测，见家族报告 §3–§4）。本版 svglib 取 `svglib-ja-d5.py`，`_D5_READER = "latin"`，与 W47 对应模式参照逐字节相同；`test_d5_routing.py` FAILURES: 0；fix2 + kinsoku 齐全。

**基线**：run TOTAL 150；SVG 8/8 与 fanout 相同；印 PDF 41,601,142 B；pdfdiff vs 已发件 IDENTICAL 8/8；修前普查 D5 拉丁 418。

**门禁**：17 门 + D18 中 16 门 + D18 全绿——run 150 / head_check 0 / d5 census 0 / render RC=0 / webpdf RC=0（2,522,997 B）/ occlusion 0 / p8 extract 150/150 / p8 compare CLEAN（keydiff [137, 138]）/ freeze baseline 8/8 / freeze diff 新增 CJK 0 / spill 0 / boxtitle 0 DEFECT / edge 0 TOUCH 0 NEAR / creambox PASS 0 defects（P8 226→226 行，slack 48.9px）/ print=web 文字层差 0 / census_quotes 0 defective / 刊头间距 268.7px PASS。门 15b `verify_textmd.py` carryover FAIL 为工具-格式口径差（基线同跑亦 FAIL；权威证据为 ja 原生校验器 `verify_textexp_ja.py --edition` ADOPT，0 UNEXPECTED）。

**新交付物（实测值）**：印 PDF `Lucerna-VOL1-IT.pdf` 37,481,168 B / SHA-256 `3727ac366a34b193098256b93f3882546c67c84bb73c6bb1c81025f8dc46ef44`；网 PDF `2026-w43-ja-it.web.pdf` 2,522,997 B / SHA-256 `5d36040077eb632a8c7875965e4dd0ddd84140ef07a5e4f3fb9e7e5001014f83`（D5 前已发版 2,722,325 B，`6a3ede086e73…`）；text.md **新建** 47,100 B / SHA-256 `d9f815320131a10fb53feeb0bd3b3039a340ad5d9fac615c04b104b4a3f826ed`。
