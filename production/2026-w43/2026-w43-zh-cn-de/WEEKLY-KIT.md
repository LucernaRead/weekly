# WEEKLY-KIT — Lucerna VOL.1 · zh-CN × DE (Simplified Chinese text · German explanations)

Week 2026-10-19 → 2026-10-25 · 8 pages · 1950×2700 · 4 columns · ivory #f7f1e2
Build: `hidden_files/weekly-report-zh-cn-de-build/` · Output: `files/weekly-report-zh-cn-de/`
Status: built, builder-verified (see PROOFREAD RECORD), geometric audit clean.
Independent proofread + Discord delivery are separate steps (not part of this build).

## IDENTITY

- Edition: the Simplified Chinese weekly VOL.1 re-aimed at **German-speaking
  readers** — every Chinese article, stem, option and key is the frozen core's
  （简体正文 + 英语讲解， files/weekly-report-zhcn-vol1/); the entire explanation
  layer (glosses, grammar notes, instructions, section glosses, chart notes,
  P7 clinic/readers' notes, all 150 P8 answer notes) is rewritten in German.
- Masthead: **Lucerna** (unchanged, no article — Chinese is article-less).
- Pairing badge, P1, brick red, directly under the masthead rules:
  „CHINESISCHER TEXT (VEREINFACHT) · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR
  DEUTSCHSPRACHIGE LESER" (19.5 pt sans bold, measured 1100.3 px — fits the
  1820 px measure on one line; the prescribed text needed no shortening).
- Footers on all 8 pages: „Lucerna · CHINESISCHE WOCHENZEITUNG VOL.1 · TEXT
  AUF CHINESISCH (VEREINFACHT) · ERKLÄRUNGEN AUF DEUTSCH" (measured 1211.4 px)
  / „Seite N von 8".
- Gloss prefix: „HINWEIS · " everywhere (house style of the DE fan-outs).
- Instruction words: Ausfüllen / Zuordnen / Schreiben.
- Bilingual section heads (Chinese head + German second half) throughout,
  e.g. „满减怎么玩 · Wie 满减 funktioniert", „练习 · Übungen",
  „答案 · Lösungen — nach Seiten, mit einer Anmerkung zu jeder Antwort",
  key group headers „— Seite N —".
- German number style in the apparatus prose: decimal comma (57,5),
  thousands point (10.100), percent with space (25,8 %). Chinese text and
  printed data keep the core's forms.

## METHOD

1. Copied the core's finalized build (`hidden_files/weekly-report-zhcn-build/`,
   post-rework, post-proofread) to `weekly-report-zh-cn-de-build/`. The core's
   directories were never edited.
2. **Baseline proof before any edit:** the unmodified copy rebuilt to SVGs
   byte-identical to the shipped core on all 8 pages, registry identical
   (150; A2 56 · B1 65 · B2 29; pages 10/18/18/18/18/18/12/38; writing model
   148 chars).
3. Rewrote only the explanation layer, file by file (content12/34/56/7/8,
   bslib4 gloss prefix + footers), via exact-match replacements with asserted
   occurrence counts. Output paths → `files/weekly-report-zh-cn-de/`; PDFs
   renamed `Lucerna-VOL1-DE.pdf` / `-web.pdf`.
4. The banned intermediary term appears nowhere — paper, this KIT, and code
   (grep over build sources + final SVGs = 0 hits).

## TOTALS (measured on the final build)

- Exercises: **150** — A2 56 · B1 65 · B2 29; per page 10/18/18/18/18/18/12/38.
- Types (registry): 完成句子 68 · 单选 50 · 词汇配对 20 · 完形单选 11 · 写作 1
  — identical to the core, item for item.
- Writing model 《我的双11购物车》: 148 characters, Chinese, byte-identical
  (verified by joining the wrapped fragments in both editions).
- Visible text: 24,701 characters no-space (concatenated SVG text nodes;
  the core measures 22,853 by the same method — German apparatus runs longer).
- Build log: zero FLOW OVERFLOW, zero HEAD TOO WIDE on the final build.

## FREEZE VERIFICATION

- Registry field diff vs the core registry: **n / page / level / type identical
  for all 150**; key diffs **exactly 1**, the documented reader-language item:
  - #150 key → „(offene Aufgabe — Mustertext unten)" (the writing item's
    registry apparatus line, was the core's Chinese apparatus line);
    its note → „Offene Aufgabe — der Mustertext steht oben in Abschnitt F
    (148 Zeichen)".
  - The core contains no zh↔EN translation exercises (types are
    完成句子/单选/词汇配对/完形单选/写作 only), so no other key could re-aim;
    all 149 other keys are byte-identical, and all 150 notes are new German.
- Full text-node multiset diff vs the core SVGs, per page: every differing
  node classifies as German apparatus / badge / footer. The only pure-Chinese
  deltas are (a) the footer page markers （第 N 版 / 共 8 版 → „Seite N von 8"),
  (b) wrap-point fragments of three mixed paragraphs whose Chinese segments
  are unchanged (P7 measure-word pattern line, P7 sentence-frame box, P8
  model-answer paragraph — the model text itself verified byte-identical
  after joining), (c) one date fragment of the German P4 chart note.
- P7 phrases: the 8 Chinese quotes + page tags verified — each quote occurs
  exactly 2× in the issue (source + P7), byte-verbatim Simplified excerpts;
  only their translations are new (German), tags now „(S. N)".
- Images: embedded payloads byte-identical to the core on every page
  (counts per page 1/1/2/2/1/2/0/0); credits identical in substance — the
  „Photo:" label is „Foto:" and the 1896 credit's „unknown author" label is
  rendered „Autor unbekannt"; artist names and licenses unchanged (all CC0 /
  public domain).
- Facts unchanged: 双11付尾款周 lead (Tmall tail payments Tue Oct 20 20:00);
  hairy-crab figures (Xinfadi ~3两 females ¥77.5/斤 → ¥57.5/斤, −25.8 %
  labeled computed); 重阳 2026 retrospective Sun Oct 18; 霜降 Fri Oct 23.
  Zero politics, as the core.
- Traditional-character audit: OpenCC t2s over all visible text — **zero**
  traditional forms (the Chinese is Simplified only, as in the core).
- English-apparatus remnants: **zero**. Token scan of all Latin text finds
  only German, pinyin, and proper nouns (Lucerna, Tmall, JD.com, NBA, S16,
  LPL, Weibo, Xinfadi, Sina Finance, The Beijing News, Wikimedia Commons,
  CC0, team/person names).

## LAYOUT ADJUDICATIONS (German runs long; wording fitted to core geometry)

- **Shortened bilingual heads** where the measured width required it
  (head limit = 434 px column measure):
  „C · 读图与换算 · Diagramm lesen" (413.3 px; the full „Diagramm &
  Umrechnung" measured 532.2), „C · 时间换算 · Zeit umrechnen" (383.2 px;
  „Zeitzonen umrechnen" 458.0), „A2 · 购物与量词 · Klassifikatoren"
  (397.0 px; „Zähleinheitswörter" 445.8 — the body text keeps the full term
  Zähleinheitswörter).
- **P2 calendar box title** „本周生活小日历 · Wochentermine" (374.7 px ≤ 398
  box inner width). The literal „Termine der Woche" measured 411.8 px and
  would have spilled — the core's own history had a 14 px spill at this very
  title; not repeated.
- **P1 hot-search sub-line** shortened to „Momentaufnahme der Weibo-Hot-Search"
  after measurement showed the first German wording (434.4 px from x=1473)
  spilling ~22 px past the box edge at 1885. Found by card viewing +
  measurement, fixed, re-rendered, re-swept (see below).
- **P8 keys:** German notes are longer than the core's English; the first
  build overflowed the last key column by 5 items. Fix = wording only:
  24 answer notes tightened without content change (e.g. #83 „Netzbeiträge
  behaupteten: Preise um über 40 % gestürzt.", #127 „Ab-Hof-Preise: etwa
  Niveau der letzten drei Jahre.", #132 „Vorverkauf: erst Anzahlung, später
  Restbetrag."). Result: keys flow ends col 3/3 at y=2382; **lowest P8 body
  baseline 2530.3 → 49.7 px clear of the 2580 footer rule**. Space before
  every note parenthesis, half-width only (notes avoid parentheses around
  Chinese terms, which the typesetter would widen).
- **P7 col 3:** three German strings tightened (clinic rule 3, frame line,
  readers'-corner note) so the column ends at y=1674.7 (core: 1617.6) and
  the teaser box ends at 2520.7 (core: 2514) — clear of the footer band.
- All other changed box titles measured inside their boxes (worst case:
  „这一周的高频词 · Wörter der Woche" 396.8 / 398 px — inside, verified in
  the render).

## GEOMETRIC OCCLUSION AUDIT RECORD (SOP addendum + thin-line supplement)

- Script: `hidden_files/weekly-report-zh-cn-de-build/audit_zh_de.py` (kept
  with the build; the IT×DE audit implementation). Paint-order scan of the
  shipped SVG stream; ink band = baseline −0.88 em … +0.30 em; widths from
  the production font metrics. Checks: (a) later opaque shape covering
  ≥30 % of a text ink band, (b) text ink intruding into the footer band
  (below y=2580), (c) text ink past a page edge, (d) any later-drawn thin
  line crossing a text ink band.
- **Result: 0 flags on all 8 pages** — zero coverage, zero line-crossings,
  zero edge spills, zero footer-band intrusions. No unresolved flags.
- Supplementary sweep (every text node, all anchors): no node's ink extends
  past the content edges (x < 65 or x > 1885). Per-page lowest body
  baselines → clearances to the 2580 rule: P1 130.6 · P2 73.8 · P3 62.6 ·
  P4 95.1 · P5 40.4 · P6 102.3 · P7 93.3 · P8 49.7 px (all ≥ 40).
- Kinsoku line-start scan on the final text nodes: 0 lines begin with
  closing punctuation.
- All 8 card PNGs additionally viewed page by page: no covered, clipped or
  struck-through text; badge, footers, boxes and the P8 key columns all sit
  as designed.

## PROOFREAD RECORD (builder's own pass)

- Re-solved 50+ exercises against the printed articles/charts and the German
  notes (spot set: #1, #4, #7, #9, #11, #14, #17, #21–24 arithmetic,
  #25–28 / #43–46 / #61–64 / #79–82 / #97–100 — all five match sets
  re-solved against their printed definition lists, #31, #37, #39–42,
  #49, #50, #57 chart difference 251.928 − 249.193 = 2.735, #67, #72, #76,
  #84, #86 (20 ÷ 77,5 ≈ 25,8 %), #93, #94, #101, #109, #112, #123, #127,
  #141, #145, #147, #150 model arithmetic 260+60+40=360, −50 → 310,
  deposit 30 → balance 280) — keys and German notes consistent throughout.
- German apparatus read through in the rendered cards: glosses, clinic rules
  („地 (de) zeigt, wie eine Handlung geschieht …"), chart notes and all
  key notes are complete, natural German; pinyin stands wherever the core's
  English apparatus gives it, with German definitions for the Chinese
  headwords.
- This is the builder's pass. The SOP's independent proofread-to-zero gate
  runs as a separate step before delivery.

## REPRODUCE

```bash
cd hidden_files/weekly-report-zh-cn-de-build
/tmp/wp-venv/bin/python run.py        # -> files/weekly-report-zh-cn-de/svg/
/tmp/wp-venv/bin/python audit_zh_de.py ../../files/weekly-report-zh-cn-de/svg
/tmp/wp-venv/bin/python render.py     # -> cards/ + both PDFs
```
Never run a single content*.py alone — run.py executes them in one process so
the exercise registry accumulates in order.

## INDEPENDENT PROOFREAD RECORD (2026-10-21, second reader)

**Verdict: PASS — one complete independent pass, ZERO problems. No fixes were
needed; nothing was re-rendered.**

Verified independently (builder's claims re-derived, not trusted):

- **Reproducibility:** scratch copies of both builds (output redirected)
  rebuild SVGs byte-identical to the shipped core AND the shipped DE edition
  on all 8 pages; the registries dumped from those runs are the shipped ones.
- **Registry:** 150 items; n/page/level/type identical to the core for all
  150 (A2 56 · B1 65 · B2 29; pages 10/18/18/18/18/18/12/38; types
  68/50/20/11/1). Key diffs exactly 1 — #150's apparatus line → German. All
  150 notes are new German, none empty.
- **Freeze (strongest form):** the CJK-only character sequence of each page
  was diffed against the core. The ONLY deletions are the core's Chinese
  pairing-label furniture (P1 badge line + the per-page footer label block
  简体中文周报…第 N 版/共 8 版）. Zero insertions, zero substitutions — every
  article character, stem, option, key, gloss headword and the model text is
  sequence-identical, which also settles the three mixed paragraphs (P7
  measure-word line, P7 sentence-frame box, P8 model paragraph) at character
  level. Writing model 《我的双11购物车》 joined from the rendered fragments:
  148 characters, byte-identical in both editions.
- **Script audit:** OpenCC t2s over all DE visible text changes 0 characters;
  the DE CJK character set is a subset of the core's (only 解 missing — from
  the removed 英语讲解 label). No traditional forms, no script mixing.
- **Notes faithfulness:** all 150 DE notes read side-by-side against the
  core's English notes — every one faithful, including the tightened ones
  (#83, #127 „…der letzten drei Jahre", #132 both steps kept). All numeric
  differences are German conventions only (decimal comma, thousands point,
  ordinal dot, spelled-out numbers). Zero glued "(" and zero full-width
  parentheses in registry notes and in the rendered P8 key lines.
- **Re-solve:** all five match sets re-solved against the printed definition
  lists (#25–28 b/d/c/a · #43–46 c/d/b/a · #61–64 d/b/c/a · #79–82
  c/d/b/a · #97–100 c/d/a/b — all correct); chart arithmetic re-derived
  (251.928 − 249.193 = 2.735; (77.5 − 57.5) ÷ 77.5 = 25.8 %, labelled
  computed); the worked-example chain 260 + 60 = 320, − 50 = 270, − 30 = 240
  re-verified against the printed example; chart bars measured in the SVG
  (P4: 554.24 / 548.22 px, exactly proportional to the scores; P6: 465 px =
  77.5 × 6 px/yuan). Calendar facts checked against the real 2026 calendar
  (Oct 18 Sun · Oct 19 Mon · Oct 20 Tue · Oct 23 Fri). 35+ exercises
  re-solved in full, the rest via their verified notes.
- **Language scan:** full Latin vocabulary of the edition eyeballed — German,
  pinyin, and proper nouns only (The Beijing News, Victoria's Secret, credit
  names, „Hot-Search" as the Weibo feature name). „Notes" occurs 0×;
  „HINWEIS · " heads all 11 gloss blocks (P5's first block wraps the prefix
  onto its own line — present and correct). Exercise-header notes are German
  on every page.
- **Geometry — builder's audit caveat found and covered:** the shipped audit
  script reproduces 0 flags, and its COVER and FOOTER checks pass a
  synthetic positive control; but its LINEX check models `<line>` elements
  as zero-height boxes, and this build draws its rules as `<line>` (sw
  1.2–3) — so that check can never fire here. An independent line-crossing
  scan (lines expanded by stroke width, production font metrics, paint
  order) was therefore run over all 8 pages: exactly ONE band intersection —
  the P2 model-sentence rule (y=1804, sw 2, geometry byte-identical to the
  frozen core). Pixel measurement of the rendered cards (both editions):
  sentence ink ends at row 1802, rule rows are 1803–1804 with zero text ink
  → **non-defect** under the ink-contact standard (the RU P2 precedent); it
  reads as an underline. All other pages: zero intersections.
- **Baselines/edges:** per-page lowest body baselines re-measured —
  clearances to the 2580 rule 130.6 / 73.8 / 62.6 / 95.1 / 40.4 / 102.3 /
  93.3 / 49.7 px, exactly the builder's figures; P8 lowest baseline 2530.35
  (col 3), per-column 2514.9 / 2513.4 / 2530.4 / 2365.9. Zero text nodes past
  the content edges (65/1885) on any page; kinsoku line-start scan 0. The
  single text–text band overlap (P1 wordmark vs edition line) is a
  band-model artefact — both elements are byte-identical to the frozen core
  and the card shows clear air.
- **Badge/footers/images:** badge text exactly as prescribed, brick red
  #a4553a, bold, centred; width re-measured 1100.3 px (builder's figure
  exact), one line. German pairing footers + „Seite N von 8" with correct N
  on all 8 pages; masthead article-less. Image payloads byte-identical to
  the core on every page (1/1/2/2/1/2/0/0); credits identical in substance
  („Foto:", „Autor unbekannt, 1896").
- **Shortened heads adjudicated acceptable:** „Diagramm lesen", „Zeit
  umrechnen", „Klassifikatoren" (body keeps Zähleinheitswörter), P2
  „Wochentermine", P1 „Momentaufnahme der Weibo-Hot-Search" — in each case
  the Chinese half of the head carries the full wording and no content is
  lost (the hot-search box's next line keeps the third-party-mirror fact).
  The P6 chart note and all source lines are fully faithful in German.
- **Facts/politics:** 双11付尾款周 lead, crab ¥77.5 → ¥57.5/斤 with −25.8 %
  labelled computed, 重阳 Oct 18 retrospective, 霜降 Fri Oct 23 — all as
  finalized; zero politics. P7's 8 phrases byte-verbatim with tags
  (S. 1, 1, 2, 3, 4, 4, 5, 6) matching the core's page order.
- **Files:** both PDFs 8 pages; sizes as in DELIVERABLES (web 3,264,696 B
  < 10 MB). Visible-char counts run 44 higher than the builder's in BOTH
  editions (counting convention; the inter-edition delta is identical).
  Banned intermediary term: 0 hits in paper, KIT, and code. All 8 cards
  viewed page by page — no covered, clipped or struck text anywhere.

## DELIVERABLES (files/weekly-report-zh-cn-de/)

- `svg/` — 8 page SVGs (p1-touiban … p8-ceyan)
- `cards/` — 8 page PNGs (1950 px wide)
- `Lucerna-VOL1-DE.pdf` — print PDF, 67,697,356 bytes
- `Lucerna-VOL1-DE-web.pdf` — web PDF, 3,264,696 bytes (< 10 MB, Discord-ready)
- `WEEKLY-KIT.md` — this file
