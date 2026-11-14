# WEEKLY-KIT — La Lucerna VOL.1 · IT × DE (Italian text · German explanations)

Week 2026-10-19 → 2026-10-25 · 8 pages · 1950×2700 · 4 columns · ivory #f7f1e2
Build: `hidden_files/weekly-report-it-de-build/` · Output: `files/weekly-report-it-de/`
Status: built, builder-verified (see PROOFREAD RECORD), geometric audit clean.
Independent proofread + Discord delivery are separate steps (not part of this build).

## IDENTITY

- Edition: Italian weekly VOL.1 re-aimed at **German-speaking readers** — every
  Italian article, stem, option and key is the frozen core's; the entire
  explanation layer (glosses, grammar notes, instructions, section glosses,
  chart notes, P7 clinic/readers' notes, all 150 P8 answer notes) is in German.
- Masthead: **La Lucerna** (unchanged).
- Pairing badge, P1, brick red, directly under the black band:
  „ITALIENISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER"
  (22 pt sans bold, measured 1071.8 px — fits the 1820 px measure.)
- Footers on all 8 pages: „La Lucerna · ITALIENISCHE WOCHENZEITUNG VOL.1 ·
  TEXT AUF ITALIENISCH · ERKLÄRUNGEN AUF DEUTSCH" / „Seite N von 8"
  (left string measured 1038.9 px ≤ ~1100.)
- Gloss prefix: „HINWEIS · " everywhere (house style of the DE fan-outs).
- Instruction words: Ausfüllen / Zuordnen / Sätze bilden / Übersetzen /
  Entscheiden / Schreiben / Korrigieren.
- Bilingual section heads (Italian head + German second half) throughout, e.g.
  „LA NOTIZIA · DIE TITELSTORY", „ESERCIZI · ÜBUNGEN ZU SEITE n",
  „RISPOSTE · LÖSUNGEN", „— PAGINA n —" key group headers kept from the core.

## METHOD

1. Copied the core's post-patch build (`hidden_files/weekly-report-it-build/`,
   incl. §12 P8 baseline patch and §13 P1 rule patch) to
   `weekly-report-it-de-build/`. The core's directories were never edited.
2. **Baseline proof before any edit:** the unmodified copy rebuilt to SVGs
   byte-identical to the shipped patched core on all 8 pages, registry
   identical (150; A2 46 · B1 71 · B2 33; pages 10/18/18/18/18/18/12/38;
   model text 90 words).
3. Rewrote only the explanation layer, file by file (content12/34/56/7/8,
   bslib4 gloss prefix + footers). Output paths → `files/weekly-report-it-de/`;
   PDFs renamed `La-Lucerna-VOL1-DE.pdf` / `-web.pdf`.
4. The banned intermediary term appears nowhere — paper, this KIT, and code
   (the layout helper was renamed in code; grep over build sources + final
   SVGs = 0 hits).

## TOTALS (measured on the final build)

- Exercises: **150** — A2 46 · B1 71 · B2 33; per page 10/18/18/18/18/18/12/38.
- Types (registry): sentence completion 60 · multiple choice 49 · cloze MC 13 ·
  vocabulary matching 12 · sentence building 7 · translation 4 · true/false 3 ·
  transformation 1 · writing 1 — identical to the core, item for item.
- Writing model text (§H): 90 words, Italian, byte-identical.
- Visible text: 41,795 characters (sum of unescaped SVG text-node contents;
  the core measures 35,619 by the same method — German apparatus runs longer).
- Build log: zero FLOW OVERFLOW, zero HEAD TOO WIDE on the final build.

## FREEZE VERIFICATION

- Registry field diff vs the core registry: **n / page / level / type identical
  for all 150**; key diffs **exactly 3**, all documented reader-language items:
  - #137 key → „Am Sonntag schlafen wir eine Stunde länger." (IT→DE translation)
  - #138 key → „Die Ausstellung bleibt bis April geöffnet." (IT→DE translation)
  - #150 key → „(offene Aufgabe — Mustertext unten)" (registry apparatus line)
  - #139/#140: prompts re-aimed to German („Am Samstag um 18:00 Uhr spielt
    Napoli gegen Roma. → ___", „Jede Zahl muss eine Quelle haben. → ___");
    their Italian keys are byte-identical to the core.
  - #150 note → „Mustertext in Abschnitt H auf dieser Seite (90 Wörter)".
- Full text-node multiset diff vs the core SVGs, per page: every differing node
  classifies as German apparatus / badge / footer. Only two non-CJK core-only
  fragments appeared, both wrap-point artefacts, both verified complete in the
  DE file: the P6 word-box noteline („Wörter aus dem Kasten: manovra · rinvio ·
  miliardo · previsione.") and the P7 B2 noteline (Italian rule string intact).
- P7 phrases: the 8 Italian quotes + (Pagina N) tags are byte-identical nodes
  to the core (each quote therefore occurs exactly twice in the issue, as in
  the core); only their translations are new (German).
- Images: embedded payloads byte-identical to the core on every page; credits
  unchanged (Italian).
- Facts unchanged: ora solare lead; Manovra honesty survives in German — the
  chart's Italian caption (frozen) plus key #85 „5 + 5 + 3,4 = 13,4 (nicht der
  Gesamtbetrag)" and #86 (difference 1,6): components 13,4 ≠ total ~23,5.
- CJK in the final SVGs: **0** on all 8 pages (registry type names remain
  internal metadata in code only, as in every sibling build; never printed).

## LAYOUT ADJUDICATIONS (German runs long; wording fitted to core geometry)

- P1 edition line: „ITALIENISCH · VOL.1 · L'ORA SOLARE · IL MALTEMPO · IL
  CINEMA" (1553.9/1820 px at 46 pt). Top strip right half:
  „ITALIENISCH, WIE ITALIEN ES LIEST" (German half added after the Italian).
- P1 CIFRE box: title „LA SETTIMANA IN CIFRE · ZAHLEN" (389.9/398 px); the four
  German parentheticals compressed so every row keeps the core's 2-line height:
  „(die Nacht: 25 Stunden)", „(Sonntagnacht)", „(21. Filmfest Rom)",
  „(8. Spieltag der Serie A)". Headline flow ends y=1809 (core: 1809 in IT×EN
  terms; bottom 1828) — no overflow.
- P1 HINWEIS noteline fitted to the core's 3 lines; „manovra" is glossed
  „Etat" here (the full „Haushaltsgesetz" gloss stands on P6); headline flow,
  CIFRE box and exercises then match the core's vertical budget exactly.
- P1 weather gloss (single line, „Unwetter: starker Regen, Wind, Stürme —
  Adam.", 424.4/434 px) sits at the core's baseline 1846.3; the §13-patched
  full-width rule at y=1864 clears its ink bottom (≈1852) by ~12 px — audit
  line-crossing check = 0 (see AUDIT).
- P2 FRASE box title set at tsize 19 („LA FRASE PER RICORDARE · MERKSATZ",
  367.8/398 px; at the standard 23 pt it overflows the box measure).
- Shortened bilingual heads where the measured width required it:
  „LA SETTIMANA DEL CALCIO · FUSSBALLWOCHE" (· DIE dropped),
  „LE CIFRE DEL DPB · DIE ZAHLEN DES DPB (…)", „LE PREVISIONI 2027 · DIE
  PROGNOSEN 2027", „FRASI DELLA SETTIMANA · SÄTZE DER WOCHE (…)", band subs
  „Herbstliche Spezialitätenfeste", „Lucca Comics und junges Kino",
  „Drei Stufen, drei Werkzeuge". E TU one-liners fitted to the core's line
  counts so the box-height formulas are unchanged.
- P6 exercise notelines fitted to core line counts: §A „Wählen Sie nach den
  Grafiken oben." (1 line), §D „Wörter aus dem Kasten: manovra · rinvio ·
  miliardo · previsione." (2 lines). P6-ex flow ends y=2569 ≤ 2580.
- P7 col-3 boxes: parola note fitted to 2 lines („anteprima = Premiere
  (Seite 5: viele Premieren)."), lettere note to 3 lines (invitation retained:
  „… schreiben Sie uns!") — col 3 ends y=1674.0, exactly the core's value.
- **P8 keys:** German notes are longer than the core's; the first build
  overflowed the last key column. Fix = wording only (size 13.5 pt and
  lh 1.16 kept at the core's patched values): 23 answer notes tightened
  without content change (e.g. #83 „Beitrag von Banken/Versicherungen: rund 5
  Milliarden", #90 „Streitpunkt: Banken- und Versicherungsbeitrag", #95
  „Tatsache nach scrivono che → Indikativ", #46 „resta aperta = geöffnet").
  Result: keys flow ends col 3/3 y=2413, zero overflow; **lowest key baseline
  per column 2535.64 / 2533.06 / 2535.64 / 2396.92 → clearance to the 2580
  footer rule 44.4 / 46.9 / 44.4 / 183.1 px (≥40 px required)**. Only four key
  lines still wrap to 2 lines: #46, #137, #138, #139 (the §E translation
  items and one long sentence key — all in columns with ample clearance).

## GEOMETRIC OCCLUSION AUDIT RECORD (SOP addendum + thin-line supplement)

- Script: `hidden_files/weekly-report-it-de-build/audit_it_de.py` (kept with
  the build). Paint-order scan of the shipped SVG stream; ink band =
  baseline −0.88 em … +0.30 em; widths from the production font metrics.
  Checks: (a) later opaque shape covering ≥30 % of a text ink band,
  (b) text ink intruding into the footer band (below y=2580), (c) text ink
  past a page edge, (d) any later-drawn thin line crossing a text ink band.
- Detector validated on a synthetic positive control (a covered text node and
  a footer-band intruder both fired correctly) before trusting the clean run.
- **Result: 0 flags on all 8 pages** — zero coverage, zero line-crossings,
  zero edge spills, zero footer-band intrusions. No unresolved flags.
- All 8 card PNGs additionally viewed page by page: no covered, clipped or
  struck-through text; badge, footers, boxes and the P8 key columns all sit
  as designed.

## PROOFREAD RECORD (builder's own pass)

- Re-solved 30+ exercises against the articles and the German notes
  (spot set: #1, #4, #7, #11, #20, #23, #29, #32, #40, #44, #47, #51, #58,
  #65, #69, #77, #82, #83, #85, #86, #90, #95, #101, #109, #112, #121, #127,
  #133, #136, #137, #139, #141, #144, #150) — keys and notes consistent.
- German apparatus read through in the rendered cards: glosses, clinic notes
  („Nur 1:00 mit è, sonst sono." / „andare steht mit essere." /
  „a + il wird al; vgl. del, nel." / „gente ist Singular (feminin)."),
  chart notes and key notes are complete, natural German; space before every
  P8 note parenthesis per house style.
- This is the builder's pass. The SOP's independent proofread-to-zero gate
  runs as a separate step before delivery.

## REPRODUCE

```bash
cd hidden_files/weekly-report-it-de-build
/tmp/wp-venv/bin/python run.py        # -> files/weekly-report-it-de/svg/
/tmp/wp-venv/bin/python audit_it_de.py ../../files/weekly-report-it-de/svg
/tmp/wp-venv/bin/python render.py     # -> cards/ + both PDFs
```
Never run a single content*.py alone — run.py executes them in one process so
the exercise registry accumulates in order.

## DELIVERABLES (files/weekly-report-it-de/)

- `svg/` — 8 page SVGs (p1-prima … p8-valutazione)
- `cards/` — 8 page PNGs (1950 px wide)
- `The-Lucerna-VOL1-it-de.pdf` — print PDF (D5 rebuild), 7992185 bytes, sha256 `41e1b19bab758e8b9d975e162a42c1b80da0412521e97c18b9653db33444d92a`
- `2026-w43-it-de.web.pdf` — web PDF (D5 rebuild, tools/webpdf.py shipped file), 1139228 bytes, sha256 `00be9ed120daf735072b5ca5384a7d9987d97a241830f471fa3c00eca6764795` (< 7 MB; old 3,644,645 B value was the render.py-era web PDF)
- `WEEKLY-KIT.md` — this file

---

## INDEPENDENT PROOFREAD RECORD (2026-10-21, separate proofreader)

Full independent pass against the frozen core — **zero problems; no fixes
required; no re-render.** The builder's claims held at every point checked.

- **Core-integrity diff** (all text nodes, both editions, per page): every
  differing node classifies as German apparatus / badge / footer. The only
  non-CJK core-only fragments are wrap/punctuation artefacts, each re-verified
  complete at node level: P5 item 3 stem (Italian identical; the core's
  trailing „(" opens its Chinese gloss, DE carries a German gloss instead),
  P6 §D word-box line 2 „miliardo · previsione." (all four words present,
  DE adds the full stop its own sentence needs), P7 B2 noteline (the Italian
  rule string „è possibile che / bisogna che / è importante che" intact
  across the DE wrap). P8 key lines differ from the core only in note
  punctuation (full-width ：/（） → half-width, house style); keys identical.
- **Registry diff** (reg-core.json vs reg-de.json): 150 items; n/page/level/
  type identical for all 150; levels A2 46 · B1 71 · B2 33; pages
  10/18/18/18/18/18/12/38; **key diffs exactly 3** — #137, #138 (German
  translation keys), #150 (apparatus line) — plus #139/#140 prompts in
  German with Italian keys byte-identical, all as documented.
- **Re-solve: all 150 exercises** re-solved from the rendered stems/options
  and articles of this edition (not spot-checked): every key correct,
  including all three matching maps against their printed definition lists
  (P2 §D a–d, P4 gloss set, P8 §F a–d) and the chart items (#85: 5 + 5 + 3,4
  = 13,4 with the German note „nicht der Gesamtbetrag"; #86: 5 − 3,4 = 1,6).
- **Notes read-through (all 150, DE vs core side by side):** the German
  apparatus is complete and natural throughout; the 23 tightened P8 notes
  retain their content. Two micro-compressions adjudicated acceptable and
  kept: #44/#134 pattern note reads „Subjekt + essere + Partizip" (the date
  stands in the key sentence itself), #137's note „wörtlich: eine Stunde
  mehr" replaces the core's „compare with the original" with the literal
  gloss — both notes remain correct. Space before every note parenthesis;
  glued „(" count = 0 in the whole edition; full-width punctuation = 0.
- **Manovra honesty:** the frozen Italian chart caption („non è il totale
  della manovra (circa 23,5 miliardi)") plus key #85's German arithmetic
  note both present and correct. Writing model: exactly **90 words**,
  byte-identical Italian.
- **CJK scan: 0** on all 8 pages. Banned intermediary term: 0 hits in
  paper, KIT and build code.
- **Geometry (proofreader's own audit, independently implemented; detector
  validated on a synthetic positive control firing all four check classes
  incl. a line-cross):** builder's audit re-run = 0 flags; own audit = 0
  coverage, 0 footer-band, 0 page-edge, 0 line-crossing flags on all
  8 pages. P8 lowest key baselines per column re-measured: 2535.64 /
  2533.06 / 2535.64 / 2396.92 → clearances 44.4 / 46.9 / 44.4 / 183.1 px,
  exactly the builder's figures. P1 rule y=1864 vs weather-gloss ink bottom
  1852.0 (12 px clear; crop-viewed, no strike). One text–text band flag
  (masthead wordmark vs edition line) crop-adjudicated as a metric artefact
  — clear air in the render, „La Lucerna" has no descenders — and identical
  in the frozen core; not a defect.
- **Badge/footers:** badge node on P1 (bold, brick red, centred; proofreader
  width measure ≈1063 px, fits the 1820 px measure; builder's 1071.8 px is
  the same fit by their metrics) and visually confirmed in the card; the
  pairing footer + „Seite N von 8" present on all 8 pages.
- **P7:** all 8 quotes byte-identical to the core, each paired with the same
  (Pagina N) tag; images byte-identical per page (base64 payload hashes
  equal), credit lines identical (Italian). Visible character counts
  recompute to the KIT's 35,619 (core) / 41,795 (DE). Both PDFs: 8 pages,
  byte sizes as in DELIVERABLES.

Verdict: **FINAL — passes the SOP gate (one complete independent pass, zero
problems).**

---

## D5 REBUILD (2026-11-13)

D5 + §1.1 合并重建记录（2026-11-13；一任 builder 至 run2 循环，二任 builder 接手核实 + gate 2 补跑；不 commit、不 push；独立重校另派他人）。

- 装机：`apply_variant.py --patch-core it --week 2026-w43 --i-understand-this-writes-production`（core-it 落盘 `_D5_READER = "latin"`）；本版 `apply_variant.py --svglib <版>/svglib.py --target it --reader de --week 2026-w43`，`_D5_READER = "latin"`；路由单元测试 `test_d5_routing.py` FAILURES: 0；fix2（U+201C/U+201D/U+2019 → serif）保留。
- 基线：run TOTAL 150、0 警告；SVG 8/8 与 fanout 逐字节相同；印 PDF 与 fanout SHA 一致（8506029 B）；修前普查 D5 拉丁 487 / 西里尔 0 / 弯引号 CJK 0。
- 二次修复（只动字号，文字零改动；盒修法行号指 tsize 行，D19）：`content34.py:22` P3 头 25→22; `content12.py:51` P1 盒 `LA SETTIMANA IN CIFRE　ZAHLEN` tsize 23→21（400.0，余 4.5px）; `content12.py:185` P2 盒 `LA FRASE PER RICORDARE　MERKSATZ` tsize 19→18（388.0，余 16.5px）; `content7.py:84` P7 `LA PAROLA　WORT DER WOCHE` p.text 23→22（384.8，余 15.7px）。
- P8：行数 205→205，距页脚线余量 57.4 px；p8 compare CLEAN（keydiff [137, 138]）。
- 新交付物：印 PDF `The-Lucerna-VOL1-it-de.pdf` `41e1b19bab758e8b9d975e162a42c1b80da0412521e97c18b9653db33444d92a`（7992185 B；修前 `7c9b56c87a753189777902370e1f7e4be1708329e2a9479a35f492898298cce0`，8506029 B）；网 PDF（tools/webpdf.py）`00be9ed120daf735072b5ca5384a7d9987d97a241830f471fa3c00eca6764795`（1139228 B；已发版 `418b1f185fc49e0d0ad90ff7f69aedfcd5843b998e569d6635243bcd848b6b7f`，1255301 B）；text.md 与 fanout `.text.md.new` BYTE-IDENTICAL（56023 B，SHA `6004269de5fad3e8eb2f654e7318f873d119ff9e72475dba62d472445bccb526`），W43 it issues/ 内无已发 `.text.md`，closer 落仓时新建补入。
- 门禁 run2 ALL-GREEN（18 门：run TOTAL 150 / head_check 0 / d5 census 0/0/0 / render RC=0 / webpdf RC=0 / occlusion 0 / p8 extract 150/150 / p8 compare CLEAN / freeze baseline 8/8 / freeze diff 新增 CJK TOTAL 0 / spill 0 / boxtitle 0 DEFECT（26 titles、237 body lines）/ edge 0/0 / creambox PASS 0 defects（n=400）/ 文字层 print=web 多重集差 0 / census_quotes 0 defective / 家族 gates.py N/A / 刊头间距 380.5 px PASS）。日志：`hidden_files/d5-redo/scratch-2026-w43-it/logs/2026-w43-it-de/GATES-SUMMARY.txt`；D5 报告：`production/notes/2026-w43/g-it/scratch-d5-rebuild-it/D5-REPORT-2026-w43-it-de.md`。gate 2 复核重跑：原 run2 已 PASS，二任照令重跑，结果一致。
- 本 KIT 交付物行已更新为以上 D5 新值；旧针脚为旧配方值，已过期，以上实测发运值为准。
