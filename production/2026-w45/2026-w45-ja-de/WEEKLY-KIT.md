# Lucerna VOL.2 — JA × DE （日语正文 + 德语讲解） · WEEKLY KIT (W45)

**Pairing:** Japanese text + GERMAN explanations — the edition for German-speaking readers.
**Week:** Monday 2 – Sunday 8 November 2026 · Issue dated Monday 2 November 2026.
**Frozen core:** `files/weekly-report-w45-ja-core/` (VOL.2, Japanese text + Chinese explanations).
Built by copying the pristine core build (`hidden_files/weekly-report-w45-ja-build/` →
`hidden_files/weekly-report-w45-ja-de-build/`) via `transform.py` and rewriting ONLY the
explanation layer into German. The core's own directories were never touched (core SVG
sha256 re-verified after the build — identical to the freeze baseline below).
Same fan-out pattern as W43 JA × DE (`files/weekly-report-ja-de/`) and W45 JA × EN.
**Not finalized by this build** — independent proofread still required before shipping.
Nothing was posted to Discord, nothing was sent to the main chat, no cron was created,
`weekly-git` was not touched.
**B1 fix (Round 3) does not finalize either:** the fix changes the rendered P8, so
per SOP §8.4 a fresh, complete proofread round is still required before shipping;
this KIT reports fix-complete only.

## Identity on the page (W43 JA × DE shipped furniture, VOL.2)

- Masthead: **Lucerna** (no article — Japanese takes none). Geometry copied whole from the
  W43 JA × DE shipped SVG: wordmark y=248, edition line y=316, badge y=356, tagline y=390,
  rules y=406/413, dark band y=424.
- Pairing badge (P1, brick #a4553a, bold):
  „JAPANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER"
- Footers (all 8 pages): „Lucerna · JAPANISCHE WOCHENZEITUNG VOL.2 · TEXT AUF JAPANISCH ·
  ERKLÄRUNGEN AUF DEUTSCH" / „Seite N von 8".
- Gloss prefix: core's 译注｜ → „Anm. — " (W43 JA × DE precedent; this overrides the
  generic `tables.json` DE gloss prefix „HINWEIS · ", which no shipped JA × DE edition uses).
- Bilingual section heads (Japanese + German half): Topmeldung, Woche in Zahlen,
  Jetzt üben, In dieser Ausgabe, Wort der Woche, Kurznachrichten, Kurzquiz,
  Sanftes Essen und ein warmer November, Wörter der Jahreszeit, Vier Wörter für
  sanftes Essen, Übungen Seite N, Kulturtag und Kanazawa, Spielplan,
  Die zwei Yokohama-Spiele im Überblick, Jugend, Halloween und Herbstfeste,
  Ein warmer November und Herbstreisen, Diagramm lesen, Übungsdaten,
  Drei Stufen, drei Themen, Fehlerklinik, Muster der Woche, Leserecke,
  Sätze der Woche, Nächste Woche, Test und Antworten, Antworten.
- Instruction words (W43 DE column, identical): Ausfüllen / Multiple Choice /
  Zuordnen / Satz bilden (type Satzbau) / Richtig/Falsch / Lückentext / Übersetzen /
  Schreiben; match instructions: „Wörter zuordnen", „Ereignisse den Orten und Daten
  zuordnen". Exercise header note (P2–P6):
  „Antworten auf Seite 8 · Stufen gemischt — nach Nummer suchen".
- P7 phrase page tags: „第N面" → „S.N" (S.1, S.1, S.2, S.2, S.3, S.4, S.5, S.6).
- P8 separators: „— Seite N —" (W43 JA × DE form). P8 answer style: the W45 core's
  dash style „N. key — note" kept byte-identical in structure (only strings localized);
  W43 JA × DE's paren-style note is a W43-family property, not a rule for this core.

## Content freeze — verification

- Baseline: `tools/freeze.py baseline` on the pristine core build rebuilt all 8 shipped
  core SVGs **byte-identically** (record: `tools/scratch/baseline-w45-ja-core/`):
  p1 4abe63d2…, p2 08439072…, p3 48a1fe94…, p4 11b592b5…, p5 3035b928…,
  p6 a8095c47…, p7 08060a28…, p8 9e733a42…; shipped core SVGs re-hashed afterwards,
  unchanged.
- `tools/freeze.py diff --strict-cjk` core vs this edition: **added CJK characters = 0
  on all 8 pages** (record: `hidden_files/weekly-report-w45-ja-de-build/diff-round2.json`;
  re-run after the B1 fix: `diff-b1.json`, still 0 on all 8 pages; P8 CJK
  2721→1448, down 6 from round 2's 1454 — exactly the 6 CJK characters of the
  removed Chinese note 工艺展到11月8日）.
  Every removed element is Chinese apparatus; every added element is German apparatus.
  Japanese body text is frozen: the shared-kanji words in frozen Japanese text (e.g.
  文化の日， 見頃， 立冬） were adjudicated word by word as legitimate Japanese usage,
  not Chinese residue. Distinctive Chinese apparatus words (练习， 答案， 本周，
  读者园地， 对照第， 参考答案， 范文， 详见第 …) occur **0×** in the edition SVGs.
  The SOP-banned intermediary term occurs **0×** in the edition dir, the KIT, the
  ABSTRACT, and the build code.
- Registry (run.py, one process): **150 exercises** — A2 46 · B1 75 · B2 29;
  pages 10/18/18/18/18/18/12/38; types Ausfüllen 50 · Multiple Choice 51 · Zuordnen 12 ·
  Satzbau 8 · Richtig/Falsch 11 · Lückentext 13 · Übersetzen 4 · Schreiben 1.
  Independently re-counted from the printed P8 key list in the rendered SVG:
  separators give 10/18/18/18/18/18/12/38, numbers continuous 1–150, no gap or repeat.
- P8 writing model 『私の11月の週末』 unchanged, **167 characters** (recounted from the
  printed P8 model text, spaces stripped; inside the 150–200 range).
- P6 practice chart: 近場の満足 38 · 温泉 27 · 紅葉 21 · グルメ 14 = 100, labeled
  練習用データ / Übungsdaten on the chart itself; bar geometry frozen from the core.
- P7 structure measured from the core (not copied from any other family): A2 column
  本と読書のことば / B1 column 紅葉のことば / B2 column 数字を読む + error clinic
  (4 items) + frame box 『ゆるく整える』 breakdown + readers' corner + VOL.3 teaser.
  P7 word-box definition sentences and phrase originals are byte-identical to the core;
  only their glosses/explanations are German.
- P7's 8 phrases verbatim (Japanese originals), each occurring exactly **2×** in the
  whitespace-stripped full text of this edition (verified programmatically).
- Images (4, `<image>` elements byte-identical to the core on every page; Japanese
  credits unchanged): P1 maple.jpg (Poliphilo, CC0) · P3 hiroshige.jpg
  (Hiroshige III, public domain) · P4 stadium.jpg (Syced, CC0) · P5 pumpkin.jpg
  (Petr Kratochvil, public domain).
- House style kept: です・ます体 throughout; weekday notation 土よう日・日よう日
  (full forms); no ruby/furigana.
- Core topics kept (no new facts): Culture Day Tue Nov 3 + peak autumn leaves over
  the Nov 7–8 weekend (Naruko Gorge peak, Kobe Nunobiki Herb Garden light-up from
  Sat Nov 7) + ゆる整え食 winter food trend (Ajinomoto, Oct 21) + Reading Week in
  progress (ends Mon Nov 9) + 立冬 Sat Nov 7; P4 reports Japan Series G1/G2 only
  (verified), G3–G7 listed as schedule with results deferred to VOL.3 (note printed
  on the page); Oct 31 Halloween covered as a just-passed report.

## P8 gate — `tools/p8.py compare` (explicit dual-path form)

- Command: `p8.py compare --core-p8 <core>/svg/p8-tesuto.svg
  --edition-p8 <edition>/svg/p8-tesuto.svg --total 150`
  (the `--core-dir` form was NOT used: it once resolved the P8 filename by native
  language and picked the wrong file).
- Result: **CLEAN, 150 noted = 150 noted, missing=[] extra=[] uncertain=[]**
  (record: `hidden_files/weekly-report-w45-ja-de-build/p8-round2.json`;
  re-run after the B1 fix: `p8-b1.json`, same CLEAN 150=150, same keydiff list).
  P8 note language: German on all 150 lines AFTER the B1 fix. Round 2's wording
  here overstated this: pre-fix, #37 was Chinese (149 German + 1 Chinese), so
  "P8 notes pure German / all 150 notes German" was not true until Round 3
  (see Repair rounds, Round 3). P8 printed-note set equal (no EXTRA_ONLY).
- keydiff (21 items) adjudicated one by one:
  - **True re-aims (2, legal — direction change JA↔ZH → JA↔DE):** #137 key
    „文化日是11月3日。" → „Der Kulturtag ist am 3. November." (body Japanese
    „文化の日は11月3日です。 → ___" frozen); #138 key „乱扔垃圾，要罚2,000日元。"
    → „Wer Müll wegwirft, zahlt 2.000 Yen Strafe." (same W43 JA × DE wording;
    body Japanese frozen).
  - **Re-aimed prompts with frozen Japanese keys (2 items of prompt
    localization in total, legal — same W43 pattern):**
    #139 body „读书周从10月27日开始。→ ___" → „Die Lesewoche beginnt am
    27. Oktober. → ___", key „読書週間は10月27日から始まります。" byte-identical
    (#139 is NOT in keydiff: no parenthesis, dash-branch keys equal);
    #140 body „我想去神户看红叶灯光秀。→ ___" → „Ich möchte in Kobe die
    Herbstlaub-Beleuchtung sehen. → ___", key
    „神戸の紅葉のライトアップを見に行きたいです。" byte-identical
    (#140 IS in keydiff, counted separately below — it must not also be
    counted as an artifact).
  - **Prompt localization landing in keydiff (1):** #140 — true key frozen
    Japanese, note localized „对照第6版（神户的灯光秀）" →
    „Siehe Seite 6 (Kobe-Beleuchtung)"; the tool's paren branch folds the
    note stem into the extracted key, so it appears in keydiff although the
    true key did not change.
  - **Extraction artifacts (18, not real key changes):** #1, #2, #5, #7, #8, #9, #29,
    #32, #65, #69, #78, #101, #113, #115, #117, #118, #146, #147 — the tool's
    paren-branch truncates each printed key at the last parenthesis group, so the
    compared "key" is really (true key + translated note stem). The true printed
    keys (3, 9, 7, B, C, A, 27, ○, × …) are byte-identical to the core in every
    case; only the note language differs, which is the fan-out's job. #5 and
    #101 additionally switch dash→paren method because the German note's
    parenthesis group sits at line end while the core's full-width group does
    not — same true keys (7, 27).
    (Round 2's KIT wrongly said "artifacts 17" while listing these 18 items,
    and double-counted #140 as both a re-aim and an artifact. The unambiguous
    count, confirmed by independent proofread, is **21 = 2 true re-aims
    (#137, #138) + 1 prompt localization in keydiff (#140) + 18 artifacts**;
    prompt localizations total 2, #139 + #140.)
  - All 150 P8 key lines carry exactly one German note each (the core's one
    Chinese note per key replaced 1:1) — true only after the Round 3 B1 fix;
    pre-fix, #37 was the sole Chinese exception.

## Readers' corner (coordinator ruling, executed as specified)

- No reader, letter, name, or quotation was invented. The core's Japanese sample
  letter is kept verbatim (「こんにちは。私は中学生です。…」— 読者の手紙の例）.
- The core's Japanese disclosure line does NOT serve as the operative disclosure
  (German readers cannot read it), and the core's Chinese disclosure line was
  removed, not kept.
- The edition prints ONE German disclosure stating all 3 facts — sample, not a
  real letter; no real letters and no best Page-8 compositions had arrived by the
  deadline; both carried to VOL.3 — plus an explicit German invitation
  (imperative + VOL.3 printing promise): „Beispielbrief, kein echter Brief. Bis
  zum Redaktionsschluss keine echten Briefe und keine besten Seite-8-Aufsätze;
  beides erscheint in VOL.3. Schickt uns eure Briefe auf Japanisch —
  ausgewählte Briefe erscheinen in VOL.3!" No new German letter content was
  written beyond this disclosure.

## Geometry (mandatory SOP audit)

- `tools/occlusion_audit.py` (selftest first: all 6 planted classes fire exactly
  once, clean controls silent): **edition 0 flags / core 0 flags / NEW 0**
  (record: `hidden_files/weekly-report-w45-ja-de-build/occlusion-round2.json`;
  re-run after the B1 fix: `occlusion-b1.json` + `occlusion-b1-ed.json` +
  `occlusion-b1-core.json`, still 0 / 0 / 0).
- Same-baseline furniture-band scan (P1 top band, PIL widths): left ends 219.8,
  center strapline 643.1–1306.9, right date starts 1885 — no collisions.
- Same-baseline collision check on the DE edition's own text (shared-registry
  caveat): none found beyond the audited classes.
- ADVANCE right-edge scan (PIL advance width, all 8 pages): **0 violations**
  (no text advances past x=1950 or before x=0); frame-zone scan (x<40): 0.
- P6 chart-label coverage, baseline-anchored ink method (PIL getmetrics,
  anchor `ls`, later-drawn rects): **no label above 5% coverage** (gate <30%).
- Kinsoku line-start scan (canonical NO_START set + small kana, all 8 pages):
  **0 hits in this edition, 0 hits in the core** — same caliber, frozen line
  breaks inherited unchanged.
- P7 teaser band ends **2500.08** (content limit 2540); P8 keys flow ends inside
  its region with no FLOW OVERFLOW warning (round-1 overflow fixed, see below).
- P2 „Sie sind dran" stack ends ≈1308, season-strip rule at 1554 (clearance ≈246).

## Gloss gate

- Gloss item counts (rendered `gloss()`/`bridge()` strings split on `·`, per file):
  content12 6 calls [4,4,5,1,1,1] · content34 11 calls [4,4,1,1,1,4,3,1,1,1,1] ·
  content56 11 calls [4,3,1,1,1,1,4,1,1,1,1] · content7 3 calls [3,3,3] —
  **identical to the core, item by item**. P7 phrase glosses: 8 phrases, tags
  S.1, S.1, S.2, S.2, S.3, S.4, S.5, S.6, matching the core's tag sequence.

## Repair rounds (all edits in `transform.py`; every round re-rendered single-process)

- **Round 1 (baseline: `sha256-round1.txt`).** Registry 150 / levels / pages /
  model 167 already correct, but gates failed: occlusion 5 NEW flags (P1 trend-box
  note overflowing box + page edge and its second line colliding; P2/P8 match
  instruction „Wörter den Bedeutungen zuordnen" past the page edge and
  overprinting); P7 teaser 2555.6 > 2540; P8-keys FLOW OVERFLOW (ended 2569 >
  2540); one English leak „(Sunday)" from a prefix-substring replacement.
- **Round 2 (this delivery, baseline: `sha256-round2.txt`).** Fixes, all in
  `transform.py` (derived from the JA × EN transform by `gen_transform.py`, which
  re-generates it; the two P1 pairs whose English wording moved mid-build are
  pinned by an asserting post-step so a future rewording fails loudly instead
  of leaking English):
  - P1 trend note → „Quellen und Daten: Artikel, keine Statistik" (ink 365 < 390);
    four-topics sentence → „Das sind die vier Themen dieser Ausgabe." (1 line).
  - Match instruction → „Wörter zuordnen" (P2 + P8); „Ereignisse den Orten und
    Daten zuordnen" kept (no flag, fits its slot).
  - „(Sunday)" → „(Sonntag)" (prefix-bug fix; the (Sunday) variant now has its
    own mapping entry, longest-first).
  - 16 wrapped P8 key notes shortened to single lines (faithful terse German;
    e.g. „Kulturtag: Kultur im ganzen Land",
    „November–Januar: wärmer als im Durchschnitt",
    „Kunsthandwerksausstellung im Ishikawa-Kunstmuseum",
    „Shibuya: Alkoholverbot 18:00–05:00 Uhr",
    „Bürgerfest Naka, Yokohama, 8. November (Sonntag)"); #140's inherited
    2-line entry left untouched (core-identical).
  - P7 clinic note 1 → „Mit 「昨日」 gilt die Vergangenheit." (2 lines → 1);
    readers'-corner disclosure tightened to 6 lines (same 3 facts + invitation).
  - Result: occlusion 0/0/0, teaser 2500.08, P8 overflow gone, all counts held.
    Only P1/P2/P7/P8 SVGs and cards changed between rounds (P3–P6 byte-identical
    to round 1, as expected from the fix scope).
- Pre-fix baselines: round 1 = `sha256-round1.txt` (svg + cards + PDFs); round 2
  (final) = `sha256-round2.txt`. No fix was ever applied to a content file
  without going through `transform.py`.
- **Round 3 — B1 fix (independent proofread blocker, this round).** Pre-fix
  baseline: `sha256-prefix-b1.txt` (18 deliverables + 11 build-tree key files;
  P8 SVG `04ea10d7…`, P8 card `8d996620…`, print PDF `0b04f75c…` 28,803,270 B,
  web PDF `4770f5c4…` 3,099,512 B). Single change, in `transform.py` NOTES only:
  added `("工艺展到11月8日", "Die Ausstellung läuft bis zum 8. November")`
  (new line 90, next to the existing traditional-form entry; the bare string is
  the P3 Ausfüllen answer note for key `8`, confirmed against the core text
  "展覧会は11月8日（日）までです" and the #122 wording — same exhibition, same
  date, no weekday in this item, so no "(Sonntag)"). No key, item number, or
  any other note was touched. Rebuilt per the reproduction commands
  (`transform.py` → single-process `run.py` → `render.py`, venv python):
  registry still 150 (A2 46 · B1 75 · B2 29; pages 10/18/18/18/18/18/12/38;
  model 167), P8 keys flow ends 2366 (< 2540), P7 teaser still 2500.08.
  Only `content34.py` changed in the build tree besides `transform.py` itself.
  Changed deliverables: P8 SVG only + P8 card only + both PDFs (rebuilt from
  the pages); the other 7 pages' SVG + cards are byte-identical to pre-fix.
  Re-run gates (untruncated logs in the build tree): freeze baseline core 8/8
  (`freeze-baseline-b1.json`); freeze diff added CJK 0 on all 8 pages
  (`diff-b1.json`); p8 compare explicit dual-path CLEAN 150=150, keydiff
  unchanged 21 = 2 true re-aims + 1 prompt localization in keydiff + 18
  artifacts (`p8-b1.json`); occlusion selftest OK, edition 0 / core 0 / NEW 0
  (`occlusion-b1.json`); P8 150 answer segments vs core, wrapped-joined:
  identical segments 0 (pre-fix: exactly 1, #37); full-edition Chinese
  apparatus scan: bare string 0× in all 8 SVGs, no other apparatus hits except
  the pre-existing P7 Japanese sentence containing 第8版 (byte-unchanged P7).
  P8 card viewed: #37 sits in its Seite-3 column, single line, normal spacing
  to #36/#38, no overflow or overlap. **Fix-complete only — fresh full
  proofread still required (SOP §8.4); this round does not finalize.**

## W43 deviations (JA × DE shipped edition → this edition)

1. VOL.1 → VOL.2 (core volume; footer, edition line, badge context follow it).
2. Exercise mix follows the W45 core, not W43: A2 46 (W43: 48) · B1 75 (same) ·
   B2 29 (W43: 27); total 150 in both; page distribution identical.
3. Writing model follows the W45 core: 『私の11月の週末』 167 characters
   (W43: 『私の秋の週末』 150 characters).
4. P8 answer typography follows the W45 core's dash style (W43's paren style is
   a W43-family property, not carried over).
5. Readers' corner follows the W45 core's honest-disclosure situation (no real
   letters by press time); W43 printed the VOL.2 promise instead.
6. `tables.json` DE gloss prefix („HINWEIS · ") NOT used: the shipped W43 JA × DE
   precedent „Anm. — " wins per the build brief.
7. Content, topics, images, and promises are the W45 core's throughout; no W43
   fact, figure, or sentence was carried over.

## Reproduction

```bash
cd hidden_files/weekly-report-w45-ja-de-build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python transform.py  # core -> edition build (asserts every source string)
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py         # content12+34+56+7+8 in ONE process (registry order = numbering)
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py      # svg -> cards PNG -> Lucerna-VOL2-DE.pdf + Lucerna-VOL2-DE-web.pdf
```

- run.py interpreter: `tools/venv/bin/python` (Python 3.12.3, Pillow 13.0.0,
  cairosvg 2.9.1). render.py interpreter: the same `tools/venv/bin/python`
  (system python3 has no cairosvg and was never used). svglib.py is the canonical
  JA build file, md5 `d73e23b365676c3618d7e060b835eb4d` (SEAM_SLACK fix included),
  copied verbatim and never edited.
- Build tree: `hidden_files/weekly-report-w45-ja-de-build/` (transform.py,
  gen_transform.py, content12/34/56/7/8.py, bslib4.py, svglib.py, run.py, render.py,
  assets/, sha256-round1.txt, sha256-round2.txt, occlusion-round1/2.json,
  diff-round1/2.json, p8-round2.json, plus B1-fix records: sha256-prefix-b1.txt,
  sha256-b1-postrender.txt, freeze-baseline-b1.json, diff-b1.json, p8-b1.json,
  occlusion-b1.json, occlusion-b1-ed.json, occlusion-b1-core.json,
  gates-b1-freeze.log, gates-b1-p8-occlusion.log).

## Deliverables (`files/weekly-report-w45-ja-de/`)

- `svg/` — 8 page SVGs (1950×2700), all 8 cards viewed in full (P1–P8, no defect
  found in the final visual pass).
- `cards/` — 8 page PNGs (1950×2700).
- `Lucerna-VOL2-DE.pdf` — print PDF, 8 pp, **28,802,945 B**,
  sha256 `a15cf7cf31c8d42b858b9ce622c10afbeabbb80c2d6bf9699cf57dbbe52e72b6`
  (round 2 was 28,803,270 B / `0b04f75c…`; changed only by the B1 P8 line).
- `Lucerna-VOL2-DE-web.pdf` — web PDF, 8 pp, **3,100,274 B** (< 10 MB),
  sha256 `1639dd388fd9631f3ac53e0e282028ce7140b72b69c26ff796b6f55824219209`
  (round 2 was 3,099,512 B / `4770f5c4…`; changed only by the B1 P8 card).
- `WEEKLY-KIT.md` (this file) + `ABSTRACT.txt` (German, single line, no ASCII
  double quotes).
- Not posted to Discord (parent handles delivery + repo insert).

## D5 rebuild (2026-11-14)

- 范围：D5 + §1.1 合并重建。旧样式生产源 → §1.1 组装（`style-port-ja` fanout，
  MANIFEST-W45.md 逐文件 SHA 校验；svglib 另经 D1 波校验：反向还原 canonical §2a
  hunk 后 SHA 与 MANIFEST 一致，11/11）+ D5 安装，一次重渲。
- 安装：移植模板 `svglib-ja-d5.py` 原样装为版内 `svglib.py`，仅改 `_D5_READER`
  一行 → `"latin"`（latin 读者：与模板 0 行差）。
  路由单元测试 `test_d5_routing.py` FAILURES: 0；fix2（弯引号 → Newsreader）
  保留；kinsoku（`NO_START`）齐全。
  core 落盘：模板原样拷为 `production/2026-w45/core-ja/svglib.py`（`_D5_READER = "latin"`，
  与 W47 core-ja svglib 逐字节相同，28,392 B）；安装器 `--patch-core` 对旧式 core
  拒单已实测（`FATAL: old-style svglib (no _char_font)`，日志 `logs/installer-refusal-core.log`）。
- 基线（组装后新样式源，scratch `baseline/`）：run.py TOTAL 150、FLOW 0、
  HEAD 0；SVG 8/8 与 fanout 逐字节相同；textexp 与 fanout `.text.md.new`
  逐字节相同（46571 B）；印 PDF 28037363 B，
  SHA 与 fanout 印 PDF 一致（`841f2174eb0fa4ac5d59bbcc38b06b8fce48904b94078fb6f24ec083506cc758`）；网 PDF 文字层与已发网 PDF
  `pdf_text_diff_ja.py` IDENTICAL 8/8；印/网文字层多重集差 0；修前普查
  d5_latin_in_cjk 409（>0 ✓）、curly_in_cjk 0。
  网 PDF 字节与 fanout 不符为预期：`tools/webpdf.py` 2026-11-11 改版（commit `40963281`，
  weight + italic face resolution），D1 波（11-09）所用为旧版；文字层一致为准。
- 二次修复：
- F1: P1 信用行（右栏奶油框内） — 字号 18.5→18.0（只改该行，不改文案） (`content12.py:87` 18.5 → 18.0); P8 boxtitle 1 DEFECT（P1 [BODY] over=+6.5px right，基线同报，pre-existing，非 D5 引入；工具 'no baseline' 为其逐行基线查找失效——该行基线/重建 SVG 逐字节相同）→P8 898 元素，boxtitle 0 DEFECT 行，页脚余量 76.0px
- 门禁（16 门 + D18 + D37；门 17 N/A，本家无 gates.py）：**ALL-GREEN**
- 1 run: PASS
- 2 head_check: PASS
- 3 D5 census: PASS (latin None / cyrillic None / curly-in-CJK None)
- 4 render: PASS
- 5 webpdf: PASS
- 6 occlusion: PASS
- 7 p8 extract: PASS (noted 150/150)
- 8 p8 compare: PASS (CLEAN, keydiff [137, 138])
- 9 freeze baseline: PASS
- 10 freeze diff: PASS
- 11 spill: PASS
- 12 boxtitle: PASS
- 13 edge: PASS
- 14 creambox: PASS (P8 898 元素，末行 y=2624.0，距页底余量 76.0px)
- 15a print=web: PASS
- 15b carryover: FAIL (D27: 共享校验器 ja 格式已知口径差，基线亦 FAIL；验收见 15a+15c)
- 15c native verify: PASS
- 16 census_quotes: PASS
- 17 gates.py: PASS
- D18 masthead: PASS (gap 289.8px)
- D37 P1 y~612: PASS (end 328.0pt vs 框缘 1439.5pt, over -1111.5pt)
- 新交付物（实测，scratch `patched/2026-w45-ja-de/`）：
  - 印 PDF `Lucerna-VOL2-DE.pdf`：**24757225 B**，
    sha256 `a7d53e54b02228e082e393949431061de0169c01fca0bb56e97189c15421bb4b`（49 个嵌入字体）。
  - 网 PDF `2026-w45-ja-de.web.pdf`：**2246321 B**（< 7 MB），sha256 `480cc820316309e2abfdfd8cba1455ab55f4a306b8b13451f3d6ddb0456337c8`。
  - `2026-w45-ja-de.text.md`（新建；W45 ja 无已发 `.text.md`）：**46570 B**，
    sha256 `638f5f0d59503a74f4c5354c46b68f6a0ad3ec87dd6219ed417c6fd3a0205862`；基线导出与 fanout `.text.md.new` 逐字节相同，
    D5 导出经 ja 原生校验器 `verify_textexp_ja.py --edition` ADOPT（0 UNEXPECTED）。
- 日志：`logs/2026-w45-ja-de/GATES-SUMMARY.txt`（总表）；D5 报告
  `production/notes/2026-w45/g-ja/scratch-d5-rebuild-ja/D5-REPORT-2026-w45-ja-de.md`。
  本节只追加，不改上文旧 pin（旧 pin 为 port 前旧样式值，已过时；新值以本节为准）。
