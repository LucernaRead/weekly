# Lucerna VOL.1 — JA × DE （日语正文 + 德语讲解） · WEEKLY KIT

**Pairing:** Japanese text + GERMAN explanations — the edition for German-speaking readers
（目标语正文 + 读者母语讲解；frozen core = 日语＋中文讲解版 VOL.1, week 2026-10-19 → 2026-10-25, W43).
Built by copying the finalized core build (`hidden_files/weekly-report-ja-build/` →
`hidden_files/weekly-report-ja-de-build/`) and rewriting ONLY the explanation layer into German.
The core's own directories were never touched. Same proven fan-out pattern as FR×DE / EN×DE / JA×EN.

## Identity on the page
- Masthead: **Lucerna** (no article — Japanese takes none).
- Pairing badge (P1, brick red #a4553a, bold, under the edition line):
  „JAPANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER"
- Footers (all 8 pages): „Lucerna · JAPANISCHE WOCHENZEITUNG VOL.1 · TEXT AUF JAPANISCH ·
  ERKLÄRUNGEN AUF DEUTSCH" / „Seite N von 8".
- Gloss prefix: core's 译注｜ → „Anm. — " (bslib helper renamed `bridge()` → `expl()`).
- Bilingual section heads (Japanese + German half): Topmeldung, Woche in Zahlen, Jetzt üben,
  Kurzquiz, Herbstlaub und Herbstaromen, Wörter der Jahreszeit, Jidai Matsuri und das
  Wochenende, Die Japan Series im Detail, Spielplan, Die zehn Schulen der Qualifikation,
  Comedy und Halloween, Die Para-Asienspiele im Detail, Diagramm lesen, Übungsdaten,
  Drei Stufen, drei Themen, Fehlerklinik, Muster der Woche, Leserecke, Sätze der Woche,
  Nächste Woche, Test und Antworten, Antworten.
- Instruction words (house style, identical across the DE column): Ausfüllen / Multiple Choice /
  Zuordnen / Satzbau (instr „Satz bilden") / Richtig/Falsch / Lückentext / Übersetzen / Schreiben.
- P7 phrase page tags: „第N面" → „S.N". Exercise header note (P2–P6):
  „Antworten auf Seite 8 · Stufen gemischt — nach Nummer suchen".

## Content freeze — verification
- Baseline: the unmodified copy rebuilt all 8 shipped core SVGs **byte-identically**;
  registry identical before any edit.
- Registry (both editions): **150 exercises** — A2 48 · B1 75 · B2 27; pages 10/18/18/18/18/18/12/38;
  types map 1:1 （完成句子 51→Ausfüllen, 单选 50→Multiple Choice, 词汇配对 12→Zuordnen,
  造句 8→Satzbau, 判断对错 11→Richtig/Falsch, 完形单选 13→Lückentext, 翻译 4→Übersetzen, 写作 1→Schreiben).
- Registry diff vs core: **only 3 field diffs, all documented reader-language items** —
  #137 key → German „Der Festzug startet um 12:00 Uhr am Kyoto Gyoen.",
  #138 key → German „Wer Müll wegwirft, zahlt 2.000 Yen Strafe.",
  #150 key line → German apparatus „(offene Aufgabe — Mustertext unten)".
  #139/#140 prompts re-aimed at German („Die Lesewoche beginnt nächsten Dienstag. → ___",
  „Ich möchte zum Halloween-Event in Ikebukuro gehen. → ___") with Japanese keys byte-identical.
  All other 147 keys byte-identical; all 150 P8 key lines re-verified in the rendered SVG.
- All 150 answer notes rewritten in German (Han characters appear only as the Japanese
  headwords being glossed); #92's note is pure arithmetic „34 + 28 = 62".
- Element-multiset diff per page: every removed element is Chinese apparatus; the DE edition
  introduces **zero new Han characters** (its Han set is a strict subset of the core's — all
  Japanese kanji); simplified-Chinese apparatus characters: **0**; banned intermediary term: **0**
  in pages, KIT and build code.
- Facts identical: Japan Series G1 Sat Oct 24 18:30 Yokohama, DeNA vs SoftBank; G2 Sun Oct 25 18:00;
  general sale Thu Oct 22 12:00. Matching maps re-solved: 25–28 b,c,d,a · 43–46 b,c,d,a · 141–144 b,c,d,a.
  Chart items 89–93 re-derived: 34 %, 28 %, 22−16=6, 34+28=62, Σ=100; bars byte-identical shapes.
- P7's 8 phrases verbatim (build-source strings), each occurring exactly **2×** in the
  whitespace-stripped full text of both editions; page tags S.1, S.1, S.2, S.2, S.3, S.4, S.5, S.6.
- Writing model 『私の秋の週末』 unchanged, exactly **150 characters** (build-asserted).

## Documented apparatus adaptations (German is longer than Chinese/English)
1. **Masthead shift** (same as JA×EN): wordmark 262→248, edition line 330→316, badge at 356,
   tagline 372→390, rules 392/401→406/413; black band stays at 424.
2. **P2 „Sie sind dran" line shortened** so it wraps to 3 lines (EN parity): „Und Sie? Wo sehen
   Sie dieses Wochenende das Herbstlaub? Zwei Sätze Japanisch — schicken Sie sie ein!" —
   P2 col-3 stack ends 1521.4 (32.6 px clear of the season-strip rule at 1554; the 4-line draft
   ended at 1550.4, only 3.6 px clear, and was rejected).
3. **P7 clinic notes 1 & 3 shortened** („Bücher zählt man mit 「冊」, nicht 「本」." /
   „Mit 「こと」 wird das Verb zum Nomen." — each 1 line instead of 2): P7 col-3 ends 1649.6,
   teaser band ends **2514** — exactly the core's own fixed value (the unshortened draft
   ended at 2548.64, over the 2540 content limit).
4. **P4 schedule box title shortened**: „日本シリーズの日程 · Spielplan" (337 px) — the full
   „… · Spielplan der Series" measured 455 px and crossed the box border (549+455 = 1004 > 961).
5. Gloss boxes on P2–P6 grow by the explanation length (115.95 → 145.675/175.4 px) — the flow
   engine's own computation; all flows end inside their limits, no overflow warnings.
6. **Self-caught defect, fixed before shipping:** the exercise-header note on P3–P6 was missed
   by the first transform pass (identical strings are invisible to a core↔DE diff). Caught by
   viewing the P3/P4 cards + a no-kana Han-element scan of the rendered SVGs (the only Chinese
   string in the edition); replaced on all four pages and re-verified: Chinese note 0×, German
   note 5× (P2–P6).

## Geometry (mandatory SOP audit, paint order, real-font PIL metrics)
- Coverage ≥30 % / footer band / page edge / thin-line ink-band crossings: **0 flags on all
  8 pages** (same instrument and thresholds as the programme audit; the core also scores 0).
- P8 lowest baseline **2528.8** → 51.2 px above the 2580 footer rule (≥40 px required).
- Frame-zone scan (ink past x=1910 or before x=40): none.
- Inherited adjudications, re-verified for this edition:
  - P2 rule at y=1804 rides the model sentence's baseline as an underline — the sentence
    `<text>` element (x 65, y 1800, 20.5 pt) and the rule element are **byte-identical** in
    both editions' SVGs; non-defect, kept.
  - P4 Ohtani box: the ※ line sits below the box border — bottom-region crop of the DE card is
    **pixel-identical** to the core card; kept as in the core.

## Images (7 — byte-identical `<image>` elements on every page; Japanese credits unchanged)
| Page | File | Subject | Author | License |
|---|---|---|---|---|
| P1 | stadium.jpg | Yokohama Stadium "Dream Gate" — the actual Games 1–2 venue | Syced | CC0 |
| P2 | maple.jpg | autumn maple leaves | Poliphilo | CC0 |
| P2 | mochi.jpg | handmade mochi | Fumikas Sagisavas | CC0 |
| P3 | hiroshige.jpg | Utagawa Hiroshige III, 1876 imperial-inspection procession print | Hiroshige III | Public domain |
| P4 | waseda1911.jpg | Waseda University baseball team, 1911 | Bain News Service | Public domain |
| P5 | pumpkin.jpg | jack-o'-lantern pumpkins | Petr Kratochvil | Public domain |
| P6 | paraswim.jpg | para swimming, 2016 US DoD Warrior Games (caption says so) | EJ Hersom / US DoD | Public domain |

## VOL.2 promises (carried over in German — must be honored)
Printed in the P7 teaser and readers'-corner note: Reading Week coverage (Oct 27 – Nov 9,
slogan 「静かだけど、冒険中。」), Halloween report (Oct 31, Shibuya/Ikebukuro), Japan Series
results, real readers' letters and the best Page-8 writing („VOL.2 bringt echte Briefe und
den besten Aufsatz von Seite 8!").

## Deliverables (`files/weekly-report-ja-de/`)
- `svg/` — 8 page SVGs (1950×2700)
- `cards/` — 8 page PNGs (viewed in full: all 8)
- `Lucerna-VOL1-DE.pdf` — print PDF, 42,777,199 B (corrected after the proofread fix below)
- `Lucerna-VOL1-DE-web.pdf` — web PDF, **3,179,457 B** (< 10 MB Discord limit), SHA-256 561404273a433256 (corrected after the proofread fix below; pre-fix values were 42,777,377 B / 3,178,948 B / 654ea4ce6f3cfdfd)
- Build code: `hidden_files/weekly-report-ja-de-build/` (core build untouched)
- Not posted to Discord (parent handles delivery + repo insert).

## Independent proofread record (2026-10-21, fresh pass, not by the builder)

Method: full visible-text multiset diff vs the frozen core (all 8 pages, every removed/added
element adjudicated); registry dumped independently from both builds and diffed field by
field; Han-character set analysis; simplified-Chinese scans of the rendered SVGs AND of
every string literal in the DE build code; own paint-order geometry audit (validated on a
synthetic positive control firing all four check classes, incl. the zero-height-line-box
fix); pixel-level ink measurement for line adjudications; all 8 cards viewed.

**One defect found and fixed:**
- P7 page band read „ことば · 语言" — the Chinese band gloss from the core, left
  untranslated. It was invisible to (a) the core↔DE text diff (string identical in both
  editions) and (b) the builder's no-kana Han scan (the string contains kana ことば).
  The analogous band glosses on P5 (Jugend) and P8 (Test und Antworten) WERE translated;
  P2/P3/P6 band seconds are kana readings (Japanese layer, correctly untouched).
  Fix (ja-de build only, `content7.py`): „ことば · Sprache". Rebuilt + re-rendered;
  only the P7 SVG, P7 card and the two PDFs changed — the other 7 SVGs and 7 cards are
  byte-identical to the pre-fix state, and the registry is byte-identical before/after.
  Deliverable sizes above are the post-fix values.

**Second complete pass after the fix: ZERO problems.** Verified in that pass:
- Core integrity: every diff delta is German apparatus, the badge/footer pair, or a
  documented item. Registry: 150 = 150, page/level identical for all 150; **key diffs
  exactly #137/#138/#150**; #139/#140 German prompts with Japanese keys byte-identical.
  All 150 German notes read against the core's notes — faithful, no information loss.
- Re-solved from the printed matter: matching maps 25–28, 43–46, 141–144 all **b,c,d,a**
  (verified against the printed option lists); chart items #91 22−16=6, #92 34+28=62,
  #93 Σ=100; translations #137–#140; writing model counted independently at exactly
  **150 characters**.
- Language: DE Han set (400 chars) is a strict subset of the core's — zero new Han,
  zero simplified-Chinese apparatus anywhere (only remaining simplified-scan hits are
  Japanese 万 in 万回/万円）. Gloss prefix „Anm. —" throughout. Exercise-header note in
  German on ALL of P2–P6 (the builder's self-caught fix is complete). P8 note
  parentheses all preceded by spaces, half-width only.
- Geometry (own audit): 0 COVER / FOOTER / EDGE flags on all 8 pages; the single LINEX
  flag is the inherited P2 y=1804 rule — sentence and rule elements byte-identical to
  the core, and pixel measurement on the rendered card shows the sentence's ink ends at
  row 1801 with zero ink on the rule rows (1803–1805): an underline, **non-defect**,
  as adjudicated in the core. P8 lowest baseline re-measured at **2528.8** (51.2 px
  above the 2580 rule) — the builder's figure is exact. P4 Ohtani box region is
  pixel-identical to the core card (inherited ※ placement, kept).
- Masthead: wordmark y=248, edition line y=316, badge (brick #a4553a) y=356, tagline
  y=390, rules y=406/413, band y=424 — all as documented. Badge visible on P1; pairing
  footers on all 8 pages; masthead "Lucerna" with no article.
- P7's 8 phrases byte-verbatim, each exactly 2× issue-wide, tags S.1, S.1, S.2, S.2,
  S.3, S.4, S.5, S.6. All 7 `<image>` elements byte-identical to the core, Japanese
  credits unchanged. Documented adaptations (masthead shift, P2 3-line reader box,
  P7 clinic notes 1 & 3 shortened, P4 „… · Spielplan" title) all verified — no
  information lost (the Japanese halves carry the full wording).
- Adjudicated non-defects: P1 sidebar „Näherungswerte vom 17. Oktober." compresses the
  core's trend-data disclaimer (approximate values + date preserved); P7 B1-column
  text that looked merged in a downscaled preview is clean at full resolution.

Note for the record: during this proofread a scratch copy of the core build was
mistakenly run with its original output path, regenerating the core SVGs in place.
The build is deterministic: all 8 regenerated SVGs have byte-identical sizes to the
shipped originals and re-render to PNGs byte-identical with the shipped core cards —
the frozen core is provably unchanged.

**Verdict: PASS — the JA × DE edition is final.**

---

## Patch note — 2026-10-21 · Core-level correction: P7 vocabulary-deck column-seam overprints (geometry only)

**Defect (found by the JA×PT independent proofread, §13; record: hidden_files/ja-p7-overprint-correction.md).** Two frozen Japanese lines on P7 wrapped past their column and overprinted the neighbouring column's first glyph, producing merged illegible glyphs: (a) B1 column (x=527, baseline y=336.86) line ending …スタジアムで大き vs B2 column (x=989) という意味です…; (b) A2 column (x=65, baseline y=369.54) line ending …季節で vs B1 column (x=527) な声… Inherited from the JA core by every shipped JA fan-out; earlier "visually clean" adjudications of these flags were wrong and are superseded.

**Diagnosis.** The wrap width metric is correct (PIL, Noto Serif CJK JP; every greedy pre-kinsoku line fits the 434-unit column). The defect is in the kinsoku oidashi loop in `svglib.py` `wrap()`: pulled glyphs are never re-measured, and a line starting with a NO_START chain pulls one glyph per pass — B1's line cascaded 3 pulls (』→！→な) to 23 glyphs = 491.92 units (+57.92 over the limit; ≈30 units of ink past the 462-unit column pitch), A2's line cascaded 2 pulls to 471.28 (+37.28; ≈9 units past the pitch). A programme-wide census of the core found 16 overfull lines; only these 2 exceed the 28-unit gutter (all others ≤17.50 over, ink inside the gutter, shipped and audit-clean).

**Fix (identical in all 7 JA build dirs; patched `svglib.py` md5 d73e23b365676c3618d7e060b835eb4d in each).** New module constant `SEAM_SLACK = 28` (grid pitch 462 − column width 434). `wrap()` now records pre-kinsoku line widths and, after the oidashi loop, repairs ONLY lines oidashi itself grew past `max_w + SEAM_SLACK`: trailing glyphs are shed to the head of the next line until the line fits `max_w` again (cascading forward; a NO_START glyph is shed together with the preceding glyph so no line starts with one). No content string changed; no other wrap result in the issue changes (verified below).

**Verification (this edition).** Pages 1–6 and 8 SVGs byte-identical to the previously shipped files. P7 SVG differs in exactly 4 text elements — the two seam line pairs, at unchanged coordinates (A2 lines at y=369.54/402.22: …本を読む季節で→…本を読む季 / す。→節です。; B1 lines at y=336.86/369.54: …スタジアムで大き→…スタジアム / な声が聞こえます。→で大きな声が聞こえます。); concatenated text identical on all 8 pages; exercise registry unchanged (150). Geometric occlusion audit (ink-extent, synthetic positive control passed): flags 22 → 20, the delta being exactly the two P7 TEXTX seam flags removed, zero new flags. Pixel check on the rendered P7 card: seam (a) B1 ink now ends at column 962, B2 ink starts 994 (31 clear columns); seam (b) A2 ink ends 502, B1 ink starts 528 (25 clear columns) — glyphs no longer touch at either seam.

**Pins.** Web PDF: 3,179,457 B / sha256 561404273a43325612b228b9f7fb44b43d45b0a1e574c6970f80beaa2d51fe03 → **3,180,008 B / sha256 b5fbd34c49e192d008b9dd788723981e02f4708ab0047dedf519d9f1272ca5e5**. Print PDF: 42,777,199 B → 42,777,194 B. Repo re-pin by the main line.

---

## D5 rebuild (2026-11-13)

SOP §1.1 字体修复（D5）：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader；西里尔字母改走 Noto Sans；日文正文仍走 Noto Sans/Serif CJK JP。施工不 commit、不 push；入仓由独立重校后的 closer 做。工作日志：`hidden_files/d5-redo/scratch-2026-w43-ja/logs/2026-w43-ja-de/`；逐版报告：`production/notes/2026-w43/g-ja/scratch-d5-rebuild-ja/D5-REPORT-2026-w43-ja-de.md`。

**装机**：移植模板路线（D5-METHOD §1.7；安装器拒单已实测，见家族报告 §3–§4）。本版 svglib 取 `svglib-ja-d5.py`，`_D5_READER = "latin"`，与 W47 对应模式参照逐字节相同；`test_d5_routing.py` FAILURES: 0；fix2 + kinsoku 齐全。

**基线**：run TOTAL 150；SVG 8/8 与 fanout 相同；印 PDF 41,605,522 B；pdfdiff vs 已发件 IDENTICAL 8/8；修前普查 D5 拉丁 423。

**门禁**：17 门 + D18 中 16 门 + D18 全绿——run 150 / head_check 0 / d5 census 0 / render RC=0 / webpdf RC=0（2,529,212 B）/ occlusion 0 / p8 extract 150/150 / p8 compare CLEAN（keydiff [137, 138]）/ freeze baseline 8/8 / freeze diff 新增 CJK 0 / spill 0 / boxtitle 0 DEFECT / edge 0 TOUCH 0 NEAR / creambox PASS 0 defects（P8 223→223 行，slack 47.9px）/ print=web 文字层差 0 / census_quotes 0 defective / 刊头间距 266.0px PASS。门 15b `verify_textmd.py` carryover FAIL 为工具-格式口径差（基线同跑亦 FAIL；权威证据为 ja 原生校验器 `verify_textexp_ja.py --edition` ADOPT，0 UNEXPECTED）。

**新交付物（实测值）**：印 PDF `Lucerna-VOL1-DE.pdf` 37,487,491 B / SHA-256 `e7201370801912d366df85b590f8cdef092f2f66ecc05b3e65602273ef51549f`；网 PDF `2026-w43-ja-de.web.pdf` 2,529,212 B / SHA-256 `d5a61674c0ec82cb16e25dbd0d26995cb444ad5988d727a55355da74dd8cca41`（D5 前已发版 2,749,738 B，`0e4872608b3a…`）；text.md **新建** 46,646 B / SHA-256 `603faa59ebffba6528ddcb49ded0745d573a92c392ea9060c2ae606b867e2e59`。
