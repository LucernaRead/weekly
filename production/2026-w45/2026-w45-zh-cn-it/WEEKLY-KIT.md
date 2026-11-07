# WEEKLY-KIT — Lucerna 简体中文周报 VOL.2 (W45) × IT

## Identity and spec

- **Issue week:** Monday 2026-11-02 to Sunday 2026-11-08 (magazine model:
  the cycle starting Monday 2026-10-26 produces the issue dated the following
  Monday). Issue number: VOL.2, the second Simplified Chinese issue.
- **Pairing:** zh-cn × it — Simplified Chinese body text with an Italian
  explanation layer, the edition for Italian-speaking readers. Fan-out of the
  frozen W45 zh-cn core (`files/weekly-report-w45-zhcn-core/`); the target
  text, images and layout geometry are the core's, unchanged.
- **Masthead:** bare `Lucerna` in blackletter (UnifrakturMaguntia). Chinese
  is article-less per the SOP, so there is no article. Every page footer
  reads “Lucerna · SETTIMANALE CINESE SEMPLIFICATO VOL.2 · TESTI IN CINESE
  SEMPLIFICATO · SPIEGAZIONI IN ITALIANO” with “Pagina N di 8”.
- **Format:** 8 pages (a multiple of 4), 1950×2700 px, 4 columns, warm
  ivory paper `#f7f1e2`, deep olive accents. A2→B2 ramp; every exercise is
  individually level-badged. One unified numbering sequence, 1–150, with no
  gaps or duplicates; P8 answer keys are generated from the exercise
  registry.
- **Native Simplified Chinese:** written natively from the mainland-China
  ecosystem in the core. Not converted or transcoded from any Traditional
  Chinese edition. This is a zh-cn TARGET edition: the target text stays
  Simplified as in the core; nothing was converted between scripts.
- **Status:** builder self-check complete (see “Builder's proof log” below).
  This is a builder handoff, NOT a finalisation claim — independent
  proofreading is still owed by the parent line. No Discord delivery, no
  main-chat card/PDF delivery, no cron, no repo push, no insert.py run was
  done by this builder.

## Contents, page by page

| Page | Section | Level | Exercises | Content |
|---|---|---|---|---|
| 1 | 头版 Top story (A2) | A2 | 10 (1–10) | Lead: Double 11 still running × Start of Winter on Saturday. This-week calendar box (Mon 11-02 Double 11 spot-sale period; Wed–Sat 06:00 S16 quarter-finals; Sat 11-07 Start of Winter + new film; Sun 11-08 Journalists' Day + S16 semi-final). Contents, word of the week 「立冬」, parcel-locker photo, briefs, quick quiz. Italian explanation layer throughout. |
| 2 | 生活 Life (A2) | A2 15 / B1 3 | 18 (11–28) | Double 11 shopping life (spot sales, direct cuts, AI help, WeChat shop) + Start-of-Winter life (layering, regional winter food, some schools' mid-term exams). Practice example labelled as practice numbers (sweater 240 + scarf 80 = 320, direct cut 50 → payable 270). Shopping word cards 现货 / 直降 / 立减 / 补冬. This-week dates box. Autumn-valley photo. |
| 3 | 文化 Culture (A2→B1) | A2 15 / B1 3 | 18 (29–46) | Start of Winter feature (19th solar term, 17:52 moment, three micro-seasons, regional food differences, uneven cooling, Journalists' Day paragraph). Frost + dumpling photos. Festival-dates box. |
| 4 | 体育 Sport (B1) | B1 | 18 (47–64) | S16 feature (AL out, IG/TES/BLG chasing the quarter-finals, Swiss format, fourth-round preview, 2026-10-27 cutoff stated on the page, final Beijing 2026-11-15 03:00). S16 schedule box (no score chart — final Swiss scores were not yet knowable). LAN-party file photo. Sports-dates box. Match-words box. |
| 5 | 青年 Youth (B1) | A2 1 / B1 17 | 18 (65–82) | AI film 《三星堆：未来往事》 (release, licence, 100 minutes, Maoyan 4-day figure, debate) + Start-of-Winter new film 《我们仅有一次的人生》 (cast, public synopsis, original title, festival prize, 114 minutes). Popcorn photo. Film-dates box. |
| 6 | 深读 Deep read (B2) | B2 | 18 (83–100) | Double 11 deep read (why the rules got simpler: more spot sales, more direct cuts, AI help, new platform; but “lowest price” claims must be checked against the checkout page, delivery cost, and returns rules). Practice-data bar chart only (see below). Key-points box. “Three questions for reading news” box. |
| 7 | 词语精讲 Language focus (A2/B1/B2 columns + error clinic + sentence frame + readers' corner + phrases + VOL.3 teaser) | A2 4 / B1 4 / B2 4 | 12 (101–112) | A2 shopping/winter words; B1 time-and-date order (big → small, e.g. 11月7日星期六17点52分); B2 reading news (说法 / 数据 / 广告); error clinic (的/地/得, measure-word order, date order); frame 先…再…; readers' corner (labelled editor's example + Italian on-page disclosure + explicit open invitation, see below); 8 phrases; VOL.3 teaser. |
| 8 | 测验与答案 Test & keys | A2 11 / B1 24 / B2 3 | 38 (113–150) | A true/false (8) + B big quiz (10) + C complete-the-sentence (10) + D read-and-answer passage about Xiao Hong in Beijing (6) + E in-conversation (3) + F writing (1). Then all 150 answer keys with brief Italian notes, generated from the registry, grouped by page with “— Pagina N —” headers for pages 1–8. Writing topic 《我的立冬周末》, 120–180 characters; model answer programmatically counted at 172 characters. |

## Measured totals

- **Exercises: 150 total** — A2 56 · B1 69 · B2 25. By page: 10 / 18 / 18 /
  18 / 18 / 18 / 12 / 38.
- **By type:** 完成句子 (fill in) 68 · 单选 (choose) 50 · 词汇配对
  (matching) 20 · 完形单选 (cloze choose) 11 · 写作 (writing) 1. Type
  strings were kept frozen (they are registry metadata, not rendered text);
  the visible instruction labels are Italian (`Completa`,
  `Abbina le parole`, `Scrittura`).
- **Visible text** (concatenated `<text>` nodes of the final SVGs):
  25,591 characters without spaces / 29,293 characters with spaces
  (core: 22,990 / 26,717 — the increase is the Italian explanation layer).
- **Benchmark comparison:** 150 exercises against the 《英语周报》 counted
  benchmark of 154, at the SOP's ~150 target. Identical to the core.
- **P6 practice chart** (cols 0–2): rows A 毛衣+围巾 270 yuan, B 耳机
  179 yuan, C 书+本子 160 yuan; bars drawn from zero at exactly 3.0 px per
  yuan, i.e. widths 810 / 537 / 480 px, starting at x = 325, verified in
  the edition P6 SVG rects. Basket maths printed in the article: A 240 + 80
  = 320 − 50 = 270; B 199 − 20 = 179; C 120 + 40 = 160 with no cut. The
  chart note reads “Le barre partono da 0 (3 px = 1 yuan). Solo dati di
  esercizio — non sono prezzi reali. I calcoli sono nell'articolo qui
  sopra.” P4 has no score chart, for the reason given in the core KIT.
- **Files:** 8 SVGs in `svg/`, 8 full-page PNG cards at 1950×2700 in
  `cards/`, print PDF `Lucerna-VOL2.pdf` (46,262,363 bytes, 8 pages,
  SHA-256 `612959385fedcfd660f0892efe6964007b2aa8a14a5dffafa137b743f05a4efa`),
  web PDF `Lucerna-VOL2-web.pdf` (3,262,810 bytes, 8 pages, JPEG pages
  q85 @1400 px — under the 10 MB Discord ceiling, though this builder does
  not deliver via Discord),
  SHA-256 `742c01caaa149105addc903dd08739b3c143a6314c973471a0c934c4bed4b621`.
  (Superseded pre-fix pins, 2026-10-28 fix: print 46,262,380 B /
  `799d95f4…77cc`, web 3,262,614 B / `93e8056d…527d66` — see "Fix record"
  at the end of this KIT.)
- **Phrases of the week (P7):** 8 phrases, each verbatim from this issue's
  own articles and each occurring exactly twice in the final SVGs (article
  + P7, rendered full-width punctuation): 「不用等11月11日」 p. 1;
  「下单就能发货」 p. 2; 「先看结算页，再付款」 p. 2; 「水开始结冰」 p. 3;
  「三场都输了」 p. 4; 「小局一场没赢」 p. 4; 「故事够不够好」 p. 5;
  「别以后，就现在」 p. 5. Tags read “Pagina 1, 2, 2, 3, 4, 4, 5, 5”,
  matching the core's pages.
- **Gloss counts** (split on `·` itself per tools README #21): 10 gloss()
  calls, 33 items total — core 33 = edition 33, equal item by item
  (P1 4, P2 4+4, P3 3+3, P4 3, P5 3+3, P6 3+3). Rendered “Nota — ” prefix
  counts match the call distribution (P1 1, P2 2, P3 2, P4 1, P5 2, P6 2).
- **Images:** 6 photos, byte-identical embedded payloads to the core on
  every page (md5 lists equal, in order): P1 1, P2 1, P3 2, P4 1, P5 1,
  P6 0, P7 0, P8 0. Credits kept from the Commons API Artist field;
  only the label was translated (`Photo:` → `Foto:`).

## Trend and fact sources

Inherited unchanged from the core (see the core KIT for the full source
chain). Summary: Double 11 buildup (JD.com spot sales from 20:00
2026-10-12; Taobao/Tmall presale from 20:00 2026-10-15, tail-payment + spot
sales from 20:00 2026-10-20, spot period to 2026-11-13; WeChat shop first
Double 11, 2026-10-12 to 2026-11-15, 35 days; 18th Double 11; simpler rules
with spot sales, direct cuts and AI help); Start of Winter Saturday
2026-11-07, 17:52交节, 19th solar term, three micro-seasons, regionally
varied customs, uneven cooling; S16 with the 2026-10-27 cutoff honestly
dated on the page (LPL 0–4 round 1; 2026-10-26 IG beat HLE, TES beat G2,
BLG beat KC, all 2–1; GEN/DK 3–0 through; AL/TSW 0–3 out; fourth-round draw
2026-10-29–31; quarter-finals 2026-11-04–07, semi-finals 2026-11-08–09, final
Beijing 2026-11-15 03:00); films 《三星堆：未来往事》 (2026-10-23, 100
minutes, Maoyan 4-day ~1.192 million yuan) and 《我们仅有一次的人生》
(2026-11-07, 114 minutes, original title 《余烬》, Tiantan Best
Cinematography); Journalists' Day Sunday 2026-11-08; some schools' mid-term
exams in early November (not a national unified date). No anniversary
material, no international politics, no Chinese domestic politics. No
fact, date or weekday was changed in this fan-out; all dates/weekdays are
the core's, verified there with `date -d` (Asia/Shanghai).

## W43 promises: how each was handled

Inherited from the core, unchanged: 立冬 Saturday 2026-11-07 honoured as a
lead; S16 reported only as far as verifiable at the 2026-10-27 build cutoff
(completed Swiss/knockout report is a VOL.3 teaser item); 双11 itself
(Wednesday 2026-11-11, outside the issue week) written only as buildup /
in-progress sale, with parcel arrivals as a VOL.3 teaser item.

## Readers' corner: disclosure + open invitation (Italian, on the page)

No genuine reader letters are on record, so no reader, letter, name, or
quotation was invented. The P7 corner prints the core's Chinese editor's
example letter unchanged, followed by an Italian disclosure that (a) labels
it an editor's example and states it is not a real letter, states the VOL.1
promise (real reader letters + the best VOL.1 writing in this issue) and
that nothing has arrived, and (b) contains an EXPLICIT open invitation for
real letters:

> “Una lettera di esempio della redazione — non è una lettera vera. Il
> VOL.1 aveva promesso per questo numero le lettere vere dei lettori e il
> miglior tema del VOL.1: non è arrivato nulla, quindi l'invito resta
> aperto. Rimandato, non cancellato — mandateci le vostre lettere in
> cinese, le pubblicheremo!”

Precedent note: the W43 zh-cn-it corner likewise carried an Italian-only
disclosure (its `lcn` was Italian-only in the shipped build code), so the
core's Chinese disclosure sentences were replaced, not kept alongside —
the disclosure is fully in the reader's language. The corner head reads
“读者园地 · L'angolo dei lettori”.

## VOL.3 promises printed in this issue (P7 teaser, frozen Chinese)

“双11当天11月11日星期三，包裹到了吗？S16淘汰赛打完了，谁进了决赛？
总决赛北京时间11月15日凌晨3点。还有你们的来信和第8版最佳作文。下周
见！” — 2026-11-11 is a Wednesday and the final's Beijing time is
2026-11-15 03:00, both verified in the core KIT.

## Image authorisations

6 photos, all CC0 / public domain, credit taken directly from the Commons
API Artist field (core KIT + core build `assets/CREDITS.md`). Placement
and image-element counts in the final SVGs: P1 1, P2 1, P3 2, P4 1, P5 1,
P6 0, P7 0, P8 0 — 6 photos total. Embedded payloads were MD5-verified
against the core's (identical, in order). File photos are captioned 资料图
and never presented as this week's event.

## Furniture three-way (tables.json template vs W43 shipped artifact vs this edition)

All strings below were verified against the shipped W43 zh-cn-it SVGs
and/or its shipped build code (`hidden_files/weekly-report-zh-cn-it-build/`),
never from memory.

| Item | tables.json (×IT template, VOL.1) | W43 shipped zh-cn-it | This edition (VOL.2) |
|---|---|---|---|
| P1 badge | `TESTI IN CINESE SEMPLIFICATO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI` | identical (P1 SVG, y=434, 19.5pt) | identical, same slot/size |
| Footer | `Lucerna · SETTIMANALE CINESE SEMPLIFICATO VOL.1 · TESTI IN CINESE SEMPLIFICATO · SPIEGAZIONI IN ITALIANO` | identical (bslib4.py:70) | `Lucerna · SETTIMANALE CINESE SEMPLIFICATO VOL.2 · TESTI IN CINESE SEMPLIFICATO · SPIEGAZIONI IN ITALIANO` (VOL follows the target core, VOL.2) |
| Page line | `Pagina {n} di 8` | `Pagina {n} di {total}` (bslib4.py:71) | `Pagina {n} di 8` |
| Gloss prefix | `Nota — ` | `Nota — ` (bslib4.py:197) | `Nota — ` |
| P8 separator | `— PAGINA {n} —` (generic ×IT template) | `— Pagina {n} —` (content8.py:117 + shipped P8 SVG) | `— Pagina {n} —` (shipped same-pairing artifact wins over the generic template) |
| P1 strap | — | `SETTIMANALE CINESE SEMPLIFICATO · VOL.1 · 双11 · 大闸蟹 · 霜降` | `SETTIMANALE CINESE SEMPLIFICATO · VOL.2 · 双11 · 立冬 · S16` (weekly name + VOL + this issue's topics) |
| P1 top strip | — | `每周读中文 · Leggi il cinese vero, ogni settimana` | identical |
| P1 strapline | — | `给学中文的人的周报 — Leggi la Cina vera, in cinese` | identical |
| P8 header | — | `答案 · Soluzioni — per pagina, con una nota per ogni risposta` / `Tutte le note in italiano · ✓ = il compito di scrittura` | identical |
| Band titles | — | `生活 · Vita`, `文化 · Cultura`, `体育 · Sport`, `青年 · Giovani`, `深读 · Lettura approfondita`, `词语 · Focus sulla lingua`, `测验与答案 · Test e soluzioni` | identical |
| Bylines | — | `Redazione Lucerna · Livello di lettura A2` (+ levels) | identical pattern |

**Badge slot/size case (tools README #20):** the zh-cn core family carries
its own native badge slot — the core's own pairing badge sits at y=434,
19.5pt, olive, centred, and the W43 zh-cn-it edition replaces it IN PLACE
at the same y/size. This edition does the same (badge string replaced in
the same `p.text(975, 434, …, 19.5, …)` call; no geometry moved). This is
NOT the FR/IT inserted-at-y=574 case (those cores have a frozen body
strapline at y=372 and no free slot) and NOT a masthead-shift case:
the zh-cn P1 masthead geometry is untouched (wordmark 262, strap 330,
strapline 372, badge 434, all at core positions).

**P8 answer-note style (paren vs dash):** the W45 core itself prints DASH
style (`N. key — note`, verified in the core P8 SVG). The zh-cn×IT
family's shipped fan-out style is PAREN: the W43 zh-cn-it shipped build
code renders `f"{n}. {key} ({note})"` and `f"{n}. ✓ ({note})"`
(content8.py:119,121) with `— Pagina {pg} —` separators, and its shipped
P8 SVG prints half-width parens throughout. This edition keeps the
family's paren style (content8.py render lines converted to the paren
form; writing entry key `(domanda aperta — modello qui sotto)`, note
“Domanda aperta — il modello è nella sezione F di questa pagina, 172
caratteri”, mirroring the W43 IT writing entry). Pinyin discipline
(also from the W43 IT KIT): Chinese words cited inside Italian P8 notes
appear in pinyin only (e.g. `zhíjiàng`, `lìdōng`, `ruìshì lún`,
`táotài sài`, `zǒngjuésài`), because svglib's `norm()` converts a
parenthesised pair to full-width parens when the enclosed text contains
any CJK — see “Self-fixed defects” below. Han characters inside
parentheses on P8 = 0 (full-width parens remain only inside the frozen
Chinese exercise stems, byte-identical to the core).

## Adjudications and shortfalls (for the independent proofreader)

- **P8 top rule proximity:** inherited from the core — the P8 test flow
  ends at y = 1262 against a bottom of 1252, with the keys rule at y = 1264.
  The canonical occlusion audit reports no flag there (the last ink sits
  above the rule). Visually checked on the final P8 card: clean.
- **P8 keys flow ends at y = 2545** against a bottom of 2540 (5 px past
  the nominal bottom after the last block was placed; no FLOW OVERFLOW
  warning fired). The occlusion audit reports no FOOTER flag and the final
  P8 card shows the last key line above the footer rule. Same adjudication
  as the core's top-rule case: check the card, not just the number.
- **Italian words that coincide with English words** are Italian, not
  leftovers: `shopping` (loanword), `quiz`/`Quiz lampo`, `film`, `data`
  (= date), `test` in `Test e soluzioni`, `Sport`, and the proper names
  `Sina Sports`, `JD.com`, `Taobao`, `Tmall`, `WeChat`, `Maoyan`, `S16`.
  A stoplist scan of the rendered SVGs was run; every hit outside the
  fixed band titles (below) falls in this class.
- **Box-title shortenings** (see “Self-fixed defects”): five box/section
  titles carry shorter Italian wording than the first draft, forced by
  measured widths — meaning is preserved and the full wording survives in
  adjacent glosslines/notes where applicable.
- **Traditional-character audit:** no Traditional conversion was performed
  anywhere (this is a Simplified-target edition); freeze diff strict-CJK
  added = 0 on all pages, which subsumes the script-purity check.

## Builder's proof log (self-check, final render)

- **Pre-flight duplicate check (2026-10-28 ~06:58 UTC):** my build dir
  (`hidden_files/weekly-report-w45-zh-cn-it-build/`) and edition dir did
  not exist; the zh-cn core build was last written 2026-10-27 17:54 UTC
  (>30 min idle); the only live process was an unrelated fr-ru insert.py
  touching neither of my dirs. No stand-down needed. No subagent was
  spawned; `~/workspace/weekly-git`, insert.py, Discord, main-chat
  delivery and cron were never touched.
- **Baseline (STEP 1):** `tools/freeze.py baseline` on the core build:
  **8/8 SVGs byte-identical** to the shipped core (p1 e057bbfcdfcd6fca,
  p2 c87aa67eb6785a58, p3 d50f09e1a72b6fd3, p4 dd3b1b0fdc80627a,
  p5 c71ef3153d70701c, p6 b06a85d276db8a53, p7 f2319cb8997f8d36,
  p8 eaf368f8dca48dff — full hashes in the freeze output), core SVGs
  re-hashed unchanged afterwards. Build copy was repointed (all OUT/BASE
  paths core→edition, verified by grep: zero `zhcn-core` references left)
  before any edit; content modules were executed only through the
  single one-process driver `run.py`, never imported inside the core
  build dir.
- **Driver (single process, content12 → content34 → content56 → content7
  → content8):** TOTAL 150, levels A2 56 / B1 69 / B2 25, pages
  10/18/18/18/18/18/12/38, writing model 172 characters, **zero**
  `FLOW OVERFLOW` / `HEAD TOO WIDE` warnings on the final render.
- **Freeze diff (final SVGs, `--strict-cjk`):** per-page added CJK = 0 on
  all 8 pages (P1 851→815, P2 1053→1031, P3 812→790, P4 810→789,
  P5 944→922, P6 1005→983, P7 760→652, P8 1102→985; removals are pairing
  furniture and Chinese citations inside core English notes converted to
  pinyin). TOTAL added CJK characters: 0. Target text is zero-diff vs the
  core up to explanation-layer churn (string-count deltas are the
  explanation layer only).
- **P8 gate (`tools/p8.py compare` vs core):** core 150 noted, edition
  150 noted, **status CLEAN, missing=[] extra_count=0 uncertain=[],
  keydiff=[]**. The #150 writing key change (core `(开放题，范文如下)` →
  edition `(domanda aperta — modello qui sotto)`) does not surface as a
  keydiff because the writing entry prints as `150. ✓ (note)` in both
  editions; the note itself is the translated W43-IT-pattern note.
- **Geometric occlusion audit (`tools/occlusion_audit.py`, selftest
  first):** selftest OK (all 6 planted classes fire, clean controls
  silent); final SVGs **0 flags**, core 0 flags, **NEW vs core: 0**.
- **Same-baseline ink-collision scan** (furniture-band class the canonical
  audit does not cover; `scratch/rowcheck.py`, PIL + real TTC faces):
  **0 flags** on the final SVGs, re-run after the last fix round.
- **P6 chart-label element check** (same script: earlier-drawn text ink vs
  later-drawn bar rects): **0 grazes**; bars verified 810 / 537 / 480 px
  in the SVG rects.
- **Exercise chips contiguous 1–150** across pages (P1 1–10, P2 11–28,
  P3 29–46, P4 47–64, P5 65–82, P6 83–100, P7 101–112, P8 113–150);
  registry by-type matches the core exactly.
- **Phrases of the week:** all 8 exactly 2× (article + P7), matching the
  core's counts.
- **Visual check of the final cards:** all 8 cards read in full (P1–P8),
  plus band crops for the five re-titled bands (P2/P3/P5/P6/P7) — all
  clean: no overflow, no overlap, no footer intrusion, P7 teaser band
  ends at y = 2553.12 (footer rule 2580), P7 col3 ends at y = 1707.12.
- **Italian completeness:** every explanation element is Italian on all 8
  pages; the only English retained is the frozen source name “Sina
  Sports” inside the translated P4 standings note (as in the core's
  citation), the credit lines (Commons Artist field, verbatim), and
  Italian loanwords / proper names listed under “Adjudications”.

## Self-fixed defects (each followed by a full one-process re-render, never patched in output)

1. **P6 HEAD TOO WIDE (first render):** `C · 练习篮子算一算 · Calcoli con
   i cesti` exceeded the build's width check → shortened to `C ·
   练习篮子算一算 · Calcoli` (the glossline “Calcola con i cesti di
   prova.” carries the full meaning). Zero HEAD/FLOW warnings after.
2. **Pinyin discipline / strict-CJK FAIL (first freeze diff):** the first
   render printed 38 P8 notes with full-width parens — svglib `norm()`
   converts a parenthesised pair to full-width when the enclosed note
   contains any CJK, and 38 Italian notes still cited Han characters.
   Fixed per the W43 zh-cn-it KIT discipline: all 34 affected note
   strings converted to pinyin-only citations (e.g. 直降 → zhíjiàng,
   立冬 → lìdōng, 瑞士轮 → ruìshì lún, 淘汰赛 → táotài sài, 总决赛 →
   zǒngjuésài, 最低价 → zuìdījià, 毛衣/件/个/条 → máoyī/jiàn/gè/tiáo,
   凌晨 → língchén, 早上 → zǎoshang, 周六 → zhōuliù), with match-note Han
   dropped where pinyin was already present. Re-render: strict-CJK added
   = 0 on all pages, P8 half-width parens throughout (full-width parens
   on P8 back to the core's 11, all inside frozen stems).
3. **BOXTITLE flags round 1 (4 NEW):** P1 numbers box, P2 calendar box, P4
   match-words box, P5 words box — Italian subtitles overflowed their
   boxes by 55.5 / 89 / 1.8 / 32.2 px → shortened to `Numeri della
   settimana` (via `I numeri della settimana`), `Date della settimana`,
   `Parole per la gara`, `Parole settimanali`. Re-render: P4/P5 fixed.
4. **BOXTITLE flags round 2 (2 NEW):** P1 numbers box still over by 8.2 px
   and P2 calendar box by 11.8 px → shortened to `Numeri della
   settimana` (final) and `Date settimanali`. Re-render: audit 0 flags.
5. **Missed band titles (visual check catch):** the first mapping pass
   translated band subtitles but not the five band title_lefts, leaving
   English `Life`, `Culture`, `Youth`, `Deep read`, `Language focus` on
   P2/P3/P5/P6/P7 (found by a residual-English stoplist scan of the
   rendered SVGs + eyeballing; `Sport` on P4 is identical in Italian and
   needed no change). Fixed to `Vita`, `Cultura`, `Giovani`, `Lettura
   approfondita`, `Focus sulla lingua` per the W43 zh-cn-it build code.
   Re-render: occlusion 0, strict-CJK 0, P8 CLEAN, bands visually verified.
6. **P7 readers'-corner disclosure length:** the first Italian draft
   (mixed Chinese + Italian) measured 5 wrapped lines vs the core's 4,
   which would have pushed the teaser band past the 2580 footer rule.
   Fixed per the W43 zh-cn-it precedent (Italian-only `lcn`): full
   Italian disclosure with explicit invitation (see above). Final: P7
   col3 ends 1707.12, teaser ends 2553.12, footer clear.

## Reproduction

Build code lives in
`hidden_files/weekly-report-w45-zh-cn-it-build/` (bslib4.py, svglib.py,
run.py, render.py, content12.py, content34.py, content56.py, content7.py,
content8.py, assets/, scratch/ with transform.py, pinyin_fix.py,
rowcheck.py, extract.py, diff/occlusion JSONs). Content modules run only
through the single one-process driver; never run a module standalone and
never import one inside a core build directory (their module-level code
executes on import and their OUT paths point at a shipped edition
directory).

```bash
cd hidden_files/weekly-report-w45-zh-cn-it-build
../../tools/venv/bin/python run.py        # single-process driver
../../tools/venv/bin/python render.py     # svg -> cards PNG -> print + web PDF
cd ../../tools
./venv/bin/python occlusion_audit.py --selftest
./venv/bin/python occlusion_audit.py ../files/weekly-report-w45-zh-cn-it --core ../files/weekly-report-w45-zhcn-core
./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w45-zhcn-core/svg --edition-svg ../files/weekly-report-w45-zh-cn-it/svg --strict-cjk
./venv/bin/python p8.py compare --core-dir ../files/weekly-report-w45-zhcn-core --edition-dir ../files/weekly-report-w45-zh-cn-it --target zh-cn
```

(Use `tools/venv/bin/python` — never the ephemeral `/tmp/wp-venv`.)

## Toolchain versions (actually used)

- Interpreter: `tools/venv/bin/python` — Python 3.12.3
- Pillow: PIL 13.0.0
- CairoSVG: 2.9.1
- pypdf: 6.21.2
- Fonts: NotoSerifCJK / NotoSansCJK split TTCs (SC face index 2),
  UnifrakturMaguntia for the masthead — same as the core build.

## Fix record (2026-10-28, after independent proof verdict NOT PASS)

Fix only — NOT a finalization; a full independent reproof follows (SOP §8.4).
Full log: `hidden_files/weekly-report-w45-zh-cn-it-build/fixlog/FIXLOG.md`
(pre/post SHA-256 tables, Gate 10 logs, mechanical-gate JSONs).

- **B1 — P8 key 135 note, English → Italian.** Old:
  `135. 数字 (shùzì — the AI film's characters are digital images.)` New:
  `135. 数字 (shùzì — i personaggi del film AI sono immagini digitali.)`
  Mirror evidence: ex 70 (P5) reads
  `shùzì — i personaggi del film sono immagini digitali.`
  (`content56.py:81`, delivered P5); the B1 form adds `AI` after `film` for
  the AI variant and keeps the paren style. The mapping lives in
  `scratch/transform.py` phase 1 (not a post-hoc edit), so Gate 10 covers it.
  Fit: zero FLOW OVERFLOW / HEAD TOO WIDE warnings; P8 text-node diff
  pre→post = exactly one changed node (key 135, same y 2059.70, neighbours
  unchanged, zero reflow); last key line still clear of the footer rule.
- **B2 — Gate 10 fix layer folded into `scratch/transform.py`.** The
  transform-solo repro diff was enumerated first and matched the proof's
  itemization exactly (no extra edits): phase 2a = 11 literals (4 box-title
  shortenings: Numeri della settimana / Date settimanali / Parole per la
  gara / Parole settimanali; 5 band re-titles: Vita / Cultura / Giovani /
  Lettura approfondita / Focus sulla lingua; P6 head `Calcoli`; P7 full
  Italian disclosure with the invitation verbatim) + phase 2b = the 34
  pinyin-discipline literals from `scratch/pinyin_fix.py` (retained for
  history, no longer needed for reproduction). Two phases because phase-2
  olds are phase-1 outputs. All splices are exact unique literals
  (tools README #17/#18). The it-build content files were re-synced from
  the fixed-transform output.
- **Change set (verified exactly):** P1–P7 SVGs and cards BYTE-IDENTICAL to
  pre-fix; only P8 SVG + P8 card + both PDFs differ, solely via key 135.
  New PDF pins: print 46,262,363 B,
  SHA-256 `612959385fedcfd660f0892efe6964007b2aa8a14a5dffafa137b743f05a4efa`;
  web 3,262,810 B,
  SHA-256 `742c01caaa149105addc903dd08739b3c143a6314c973471a0c934c4bed4b621`.
  ABSTRACT.txt and all furniture strings unchanged.
- **Gate 10 re-run:** fresh core copy + fixed `scratch/transform.py` alone,
  one-process driver → 8/8 byte-identical to the new delivered SVGs.
  Exit codes: transform count 0, transform apply 0, run.py 0; zero HEAD TOO
  WIDE / FLOW OVERFLOW warnings; registry TOTAL 150 (A2 56 / B1 69 / B2 25).
- **Mechanical gates re-run:** occlusion selftest OK, edition 0 flags, core 0,
  NEW vs core 0; `p8.py compare` CLEAN 150=150 keydiff []; gloss 10 calls /
  33 items = core; P8 header claim "Tutte le note in italiano" now true
  (distinctive-English-word scan over all 8 new SVGs: NONE on every page).
