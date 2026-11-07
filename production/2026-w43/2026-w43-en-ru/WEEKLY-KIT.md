# WEEKLY-KIT — The Lucerna VOL.1 · EN × RU edition

English texts + Russian explanations (Тексты на английском · Объяснения на русском).
Target: English (core VOL.1, Oct 19–25 2026, W43) · Reader native language: Russian.
Masthead: **The Lucerna**. Build dir: `hidden_files/weekly-report-en-ru-build/`.
**Proofread status: PASS** (independent proofread 2026-10-22, full round zero problems — see §11).

## 1. Baseline proof (before any edit)

- The core build (`hidden_files/weekly-report-en-build/`) was copied verbatim to
  `hidden_files/weekly-report-en-ru-build/`; `tools/freeze.py baseline` reproduced the shipped
  core SVGs **8/8 byte-identical** before any edit. Core integrity re-verified at the end:
  all 8 shipped core SVG sha256 unchanged (p1 ad9904e3…, p2 684025c5…, p3 f912664a…,
  p4 6059e3fb…, p5 1f1b61ce…, p6 221066e3…, p7 74cae1c2…, p8 35c00e49…).
- Method: explanation-layer-only transform (`scratch/transform_ru.py`): exact textual edits
  (output path, core `bridge()` method renamed to `expl()` — 1 def + 11 call sites, P1 badge
  line, P8 PRINT_NOTES block), then an AST value map replacing every CJK-bearing string
  constant (334 distinct values). Post-transform scan: **0 CJK string constants** in the 6
  operative files; rendered edition contains **0 CJK characters on all 8 pages**
  (freeze.py diff: added CJK = 0). The transform restores the 6 operative files from a
  pristine snapshot on every run, so it is safely re-runnable.
- Scratch disclosure (adjudicated exception): `scratch/transform_ru.py` necessarily quotes the
  core's original `.bridge(` call string as a search pattern for the rename; it lives only in
  `scratch/`, never in operative code or the paper. The banned intermediary term (both forms)
  occurs **0 times** in the paper SVGs, the KIT and all operative code.
- svglib.py is byte-identical to the core's (its one Chinese docstring belongs to an unused
  zh-edition illustration helper, is never rendered, and is inherited from the core verbatim).
- Build: all content modules run in ONE driver process (tools/README rule 7), tools/venv.
  Final build log: zero FLOW OVERFLOW, zero HEAD TOO WIDE; every flow end within its region
  and matching the core's column-break pattern.

## 2. Totals (identical to core)

149 exercises — A2 58 · B1 72 · B2 19; per page 10 / 17 / 18 / 18 / 18 / 18 / 12 / 38.
Registry diff vs core (all 149 items, page + level + type): keys differ ONLY at {136, 139, 149}
(§3); all other keys byte-identical.

## 3. RU column furniture — the column standard (adopted from FR×RU, which set it first)

This edition follows the RU column standard established by FR×RU (its KIT §3) verbatim;
where this build had independently chosen the same forms they were confirmed identical,
and the one divergence (P8 separator case) was aligned to the standard.

- **P1 badge** (tagline slot, 19.5pt bold sans, brick, centered):
  «ТЕКСТЫ НА АНГЛИЙСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ»
- **P1 masthead serif line**: «АНГЛИЙСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.1 · СТАДИОНЫ · ГОЛОСА · ТЫКВЫ»
- **P1 top strip middle**: «WEEKLY IN ENGLISH · КАЖДУЮ НЕДЕЛЮ · АНГЛИЙСКИЙ, КОТОРЫЙ ЧИТАЕТ АМЕРИКА»
- **P1 clock band, right lines**: «ЕВРОПА — УЖЕ В ВОСКРЕСЕНЬЕ» / «АМЕРИКА — ТОЛЬКО 1 НОЯБРЯ»
  (pixel-verified clear of the English lines: gutters 212 / 86 units)
- **Footer** (every page): left «The Lucerna · АНГЛИЙСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.1 · ТЕКСТЫ НА
  АНГЛИЙСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ» · right «Страница N из 8»
- **Gloss prefix**: «Пояснение — » (gloss-box strings carry no prefix; bslib4 adds it.
  P7 grammar points begin «Грамматика — »; phrase drills' expl strings begin «Пояснение — »)
- **P8 answer separators**: «— СТРАНИЦА N —» (all caps, per the FR×RU standard)
- **P8 typography**: core paren style kept — `key (note)`, space before the parenthesis,
  half-width parens; answer-generation code structure unchanged except the print-set
  mechanism (§5).
- **Bilingual section heads**: English original · Russian name, the Russian part shortened
  where the column width requires it (e.g. «D · VERB FORMS · Глаголы»,
  «B · SCREEN WORDS · Экран», «C · THIS WEEK, LIVE · Настоящее»,
  «THE WEEK'S FIXTURES · Матчи», «READING THE CHART · График», «ELECTION WORDS · Выборы»).
- **Russian target-name table for the RU column** (adjective for ЕЖЕНЕДЕЛЬНИК / «НА + prep.»):
  en АНГЛИЙСКИЙ / НА АНГЛИЙСКОМ · de НЕМЕЦКИЙ / НА НЕМЕЦКОМ · fr ФРАНЦУЗСКИЙ / НА ФРАНЦУЗСКОМ ·
  es ИСПАНСКИЙ / НА ИСПАНСКОМ · it ИТАЛЬЯНСКИЙ / НА ИТАЛЬЯНСКОМ · pt ПОРТУГАЛЬСКИЙ /
  НА ПОРТУГАЛЬСКОМ · nl НИДЕРЛАНДСКИЙ / НА НИДЕРЛАНДСКОМ · ru РУССКИЙ / НА РУССКОМ ·
  ja ЯПОНСКИЙ / НА ЯПОНСКОМ · ko КОРЕЙСКИЙ / НА КОРЕЙСКОМ ·
  zh-cn КИТАЙСКИЙ (УПРОЩЁННЫЙ) / НА КИТАЙСКОМ (УПРОЩЁННЫЙ) ·
  zh-tw КИТАЙСКИЙ (ТРАДИЦИОННЫЙ) / НА КИТАЙСКОМ (ТРАДИЦИОННЫЙ).
- Russian typographic conventions: decimal commas (3,6% · 0,45 кг · 13,5 млрд · 22,54),
  thousands with a space (7 889). English body text is frozen core text, untouched.

## 4. Key-diff registry (complete — exactly 3, all translation/writing items)

| n | core key | EN×RU key | why |
|---|----------|-----------|-----|
| 136 | 投票不再是一天的事情，而是一个季节。 | Голосование — это уже не один день, а целый сезон. | translation INTO the reader's language; identical sentence to the P6 KEY SENTENCE box line (verbatim constraint kept) |
| 139 | 两家俱乐部都从未赢过世界大赛。 | Ни один клуб ещё никогда не выигрывал Мировую серию. | translation INTO the reader's language |
| 149 | 开放题 — 要点见写作框，范文在第 8 版写作框内 | открытый вопрос — критерии в рамке письма; образец — в рамке письма на этой странице | writing item; apparatus in the reader's language |

- Stems 137/138 re-aimed, keys byte-identical: in the core these two items present the
  sentence to translate IN THE READER'S LANGUAGE as the item body («Перевод: «76ers» выиграли
  106–100.» / «Перевод: досрочное голосование началось в понедельник.»); their keys are the
  English translations and are unchanged. (137's body was shortened from «…выиграли матч со
  счётом 106–100.» during layout fitting — see §6; the key and note are untouched.)
- All 146 other keys byte-identical to the core (registry diff + p8.py printed-key diff agree).

## 5. Printed-note set verification (the EN-family hard gate)

- The core's print rule is a length threshold calibrated for Chinese notes; Russian notes are
  longer and would be silently dropped. This edition therefore applies the core's printed set
  EXPLICITLY by exercise number (`PRINT_NOTES` in content8.py, parity comment in code):
  {11, 14, 15, 19, 35, 36, 40, 42, 49, 65, 74, 82–87, 89, 101, 106, 108–149} = **62 notes**.
- `tools/p8.py compare` (final artifacts): **CLEAN — core 62 noted, edition 62 noted,
  missing=[], extra=0, keydiff=[136, 139, 149]** (exactly the §4 registry).
- Notes byte-identical to the core — exactly 9, all language-neutral (grammar arrows and
  arithmetic carry no reader-language content): #18 «we → are going to», #77 «fans → are
  watching», #78 «prepare → is preparing», #84 «34 + 27 = 61», #95 «218 − 214 = 4 < 10»,
  #100 «open → opened», #103 «neither → has», #119 «be going to → is going»,
  #120 «9:15 = a quarter past nine». All other 140 notes are full Russian renderings.
- Tool fix recorded for the programme: `tools/p8.py` `detect_note` misread Russian notes —
  its dash/paren disambiguation truncated any paren-style key whose note contains « — »
  (e.g. «(Present Simple — о привычках)») at the note's first dash, producing phantom
  keydiffs. Fixed 2026-10-22 (dash branch now requires a paren-free dash-key candidate).
  Regression evidence: en-nl, en-es, de-nl, es-nl, fr-nl compare outputs byte-identical
  before/after; FR×RU's phantom keydiffs cleared 15 → [71, 72, 73, 132, 145], now exactly
  matching FR×NL's legitimate list.

## 6. Defects found by the builder and fixed (explanation layer only; geometry frozen)

Layout fitting (Russian runs longer than Chinese; diagnosed by per-block flow traces against
the core build's own log, then fixed by wording compression only):
1. P1 headline flow overflow (+366 over core) → compressed the expl line and the two
   IN NUMBERS parentheticals; flow end back to the core's exact 1585.
2. P2 exercises: section-A expl wrapping to 2 lines shifted the column-break cascade so the
   D match block (395 units) no longer fit → A/C expls shortened to 1 line each; P2-ex end
   back to the core's exact 2565.
3. P2 AND YOU box: Russian line wrapped 5 lines vs the core's 2 (+87) and crossed the
   TELLING THE TIME band → text shortened to the core's 2 lines («Есть ли у вас хот-дог в
   холодильнике? Какой доход приходит в семью?»); col3 end back to the core's exact 1534.6.
   (The full prompt remains in the frozen English text directly above.)
4. P3 col3 (+209) → festival-table glosses and the debate line compressed; end 2534 ≤ 2540.
5. P5 col3 (+421) → screen-words table, SAY IT ONLINE and debate lines compressed; end 2534.
6. P6 article flow: the gloss box wrapped to 5 lines (core: 2) and overflowed the article
   region → gloss compressed to 3 lines (midterm / the House — Палата / turnout; incumbent
   and margin remain glossed in the ELECTION WORDS box and P8 matching); end = core's 1408.
7. P8 battery (+174): item 137's Russian presentation body measured 2 lines vs the core's 1,
   shifting the E–G cascade into the writing strip → body shortened to 1 line
   («Перевод: «76ers» выиграли 106–100.»), 138's body tightened for margin; battery end 1448
   ≤ 1485 (core: 1418).
8. Over-wide heads (HEAD TOO WIDE ×6) → Russian head parts shortened per §3.
9. P4 box title «THE WEEK'S FIXTURES · Расписание недели» ink crossed its box border by
   101 units (BOXTITLE) → «…· Расписание» still +9.5 → «…· Матчи» (fits, 36+ units clear).
10. Match instruction «Соедините слово и значение» (276 units) was clipped — on P4 by the
    right-rail box (tail glyphs covered) and on P2 past the page frame — a sub-threshold
    cover the audit does not flag (only ~4% of the string's ink) → «Соедините пары слов»
    (207 units; P4 ends 59 units clear of the rail box, P2 inside the frame).
11. P6 PRACTICE DATA disclaimer: the Russian tail «…Данные учебные, выдуманные.» ended at
    ink x=1004 and the READING head's gold rule struck through the ascenders of «выдуманные»
    (the EN×NL P6 defect class; the core's Chinese tail clears the rule) → tail shortened to
    «Данные учебные.»; ink now ends x=879, 109 units clear; the audit flag disappeared.
    (The English sentence is frozen core text and already carries the full disclaimer.)

## 7. Geometric occlusion audit (mandatory gate)

`tools/occlusion_audit.py` (selftest passes first). Final run: **2 flags, both pixel-adjudicated
non-defects, both identical to the core's own state**:
- P1 LINEX (word-of-week gloss vs rule below): the core flags the identical line box
  [64.4, 1843.4, 1885.6, 1844.6]. Pixel check on the rendered cards: gloss ink ends at row
  1842 in BOTH editions, rule occupies 1843–1844 → zero contact (the programme's standing
  adjudication for this pair).
- P1 TEXTX («The Lucerna» wordmark vs the Russian masthead line): the audit's font-metric ink
  boxes overlap 6px, but rendered pixels show wordmark ink bottom = row 287 and masthead-line
  ink top = row 288 — a 1px clear gap, exactly the core's own rendered clearance.
- P1 top-band same-row scan (the FR×RU lesson — same-baseline collisions the audit's TEXTX
  cannot see): rendered ink groups on the top strip — left cluster ends x=304, centre
  strapline spans 532–1419, right cluster starts 1519; identical left/right clusters in the
  core; minimum inter-group gap 100 units → 0 collisions in both editions.
- Residual-language scan: all SVG text scanned against a stoplist of Dutch/German/French/
  Spanish/Italian/Portuguese function words — 4 hits, all false positives («Los» Angeles ×3,
  English «over» ×1). No residual third-language furniture.

## 8. Images & calendar

- Images are the core's, unchanged (public-domain, credited in place from the Commons API
  Artist field in the core build; credit lines verified present in the render on P1/P2/P3/P6).
- Calendar re-verified against 2026: NBA opening Tue Oct 20 · World Series G1 Fri Oct 23 ·
  F1 Austin Sun Oct 25 · Halloween Sat Oct 31 · US clocks Sun Nov 1 · Election Day Tue Nov 3 —
  the Russian explanation texts agree with the core's (verified) claims throughout.

## 9. Deliverables (files/weekly-report-en-ru/)

- `svg/` ×8, `cards/` ×8 (1950×2700 PNG)
- Print PDF `Lucerna-VOL1-RU.pdf` — 8,574,128 bytes · sha256 403e98435f08f87047f4927e8c39c2581349d8dc19d7532d11bdc0cc75f76b24
- Web PDF `Lucerna-VOL1-RU-web.pdf` — 4,546,960 bytes (< 10 MB) · sha256 18d35eb4e71dfc45080bdbc4cd9dfdc6d371cec7ab387990bedf50a0252d1cfc
- This KIT. No repo insert, no Discord (both are the parent line's steps, per current rules).

## 10. Proofread status

**PASS** — independent proofread complete 2026-10-22 (see §11); ready for repo insert.

## 11. Independent proofread record (2026-10-22, fresh pass, all values independently re-measured)

**Verdict: PASS — one complete round, zero defects, zero fixes.** All builder claims re-derived,
none taken on trust.

- **Freeze**: `freeze.py baseline` 8/8 byte-identical; core SVG sha256 set re-verified unchanged
  after every run (start/end snapshots identical). `freeze.py diff`: edition CJK = 0 on all 8
  pages, added CJK = 0; raw CJK in shipped SVGs = 0.
- **Printed-note gate**: `p8.py extract` on the shipped core P8 independently reproduces the
  62-set {11, 14, 15, 19, 35, 36, 40, 42, 49, 65, 74, 82–87, 89, 101, 106, 108–149};
  `p8.py compare` CLEAN — 62 = 62, missing=[], extra=0, keydiff=[136, 139, 149].
- **p8.py fix regression spot-check** (§5 tool fix): `en-nl` compare reproduces CLEAN 62=62,
  keydiff [136, 139, 149]; `fr-nl` compare reproduces CLEAN 67=67, keydiff [71, 72, 73, 132, 145]
  — exactly the adjudicated FR×NL list. No regression.
- **Registry diff** (independent one-process dumps of both builds): 149 = 149; page and level
  metadata diffs = 0 (A2 58 · B1 72 · B2 19; per page 10/17/18/18/18/18/12/38); key diffs exactly
  {136, 139, 149} with the §4 strings; the 13 type labels map 1:1 Chinese→Russian with identical
  counts; notes differ on 140, unchanged exactly the 9 language-neutral ones
  {#18, 77, 78, 84, 95, 100, 103, 119, 120} (verbatim contents match §5); no CJK in any RU key/note.
  Stems 137/138: core bodies are reader-language presentation sentences («翻译：…»), RU bodies
  «Перевод: «76ers» выиграли 106–100.» / «Перевод: досрочное голосование началось в понедельник.»,
  English keys byte-identical. #136: the RU key is byte-identical to the RU P6 KEY SENTENCE box
  line; the core's own key adds 的事情 over its box line, so the RU key follows the box form — a
  correct, consistent translation (recorded, not a defect).
- **Manual key re-derivation**: 20+ items across P2–P8 re-derived from the shipped body text,
  incl. the full P6 chart set against the chart's own values (34/27/23/16 = 100): #82 C, #83 27,
  #84 61%, #85 False (27+16=43<50), #86 18 points, #87 100% — all agree; #49 C (Sunday, body seen
  on P4), #65 A («lakers roster» in the P5 article), #95 smaller (218−214), #120 B (9:15).
- **Occlusion audit** (selftest first, independent re-run): edition 2 flags, both P1, both
  pixel-adjudicated non-defects — LINEX: hard ink ends row 1842 in both editions, the rule is the
  220-grey band at rows 1843–1844, zero contact (the standing EN-core adjudication; the core flags
  the identical line box). TEXTX: font-metric boxes overlap 6px, but rendered pixels show the
  wordmark ink ending row 289 and the Russian serif line starting row 295 (5 clear rows; the
  core's own gap is 1 row) — no contact. The audit also confirms the builder's P6 fix: the core
  itself flags P6 PRACTICE DATA LINEX, the RU edition does not.
- **Same-row scan** (README rule 10): P1 top strip ink clusters on the card — left ends x=304,
  centre 530–1420, right starts 1516; left/right clusters identical to the core; min gap 96 —
  0 collisions in both editions.
- **Chart/label element checks** (README rule 12), pixel-verified: P4 fixtures title ink
  550–903 vs box right border 961 (58 clear); match instruction «Соедините пары слов» ink ends
  ≈1390 on P4 (column rule ends 1423, next column ≈1451) and ≈1852 on P2 (frame 1885) — no
  clipping; P6 PRACTICE DATA tail ink ends x=880 at the rule row, gold rule spans 989–1422 —
  109+ clear. Clock-band gutters re-measured with the audit's ink boxes: 211.8 / 85.7 (builder:
  212 / 86). Body ink bottoms per page equal the core's on 7/8 pages (P7 +30, still ≤2452.5,
  no FOOTER flag).
- **Furniture**: footer string + «Страница N из 8» correct on all 8 pages; badge and serif line
  verbatim; P8 separators «— СТРАНИЦА 1–8 —» all caps; P8 answers in core paren style
  (space + half-width parens); «Пояснение — » / «Грамматика — » prefixes in place.
- **P7**: pure-English string multiset identical to the core (28 quoted-phrase lines each);
  (page N) tag multiset identical; the one mixed line differs only by its translated note.
- **Residual language**: targeted furniture-term scan (NL/DE/FR/ES/IT/PT) = 0 hits on all 8
  pages; a broad function-word scan's only hits are frozen English body words / proper nouns
  (Los Angeles, El Clásico, ET). Banned intermediary term: 0 in paper SVGs and operative code
  （桥接 0 everywhere incl. KIT); the word `bridge` survives only as the core's original method
  name in this KIT's rename record + §1 disclosure and in scratch — the shipped-precedent form.
  `expl()` = 1 def + 11 call sites, counted.
- **Images/credits**: image payloads byte-identical to the core per page (P1/P2/P3/P6);
  credit lines identical and present (Bain News Service/LoC, SSA, Halloween postcard 1912,
  US Capitol — all public domain).
- **Calendar**: Oct 20 Tue, Oct 23 Fri, Oct 25 Sun, Oct 31 Sat, Nov 1 Sun, Nov 3 Tue — all
  verified against the real 2026 calendar and consistent throughout the Russian layer.
  Content: US domestic midterms = the core's frozen topic; no international politics added.
- **Final pins (measured from disk)**: print `Lucerna-VOL1-RU.pdf` 8,574,128 B ·
  sha256 403e98435f08f87047f4927e8c39c2581349d8dc19d7532d11bdc0cc75f76b24;
  web `Lucerna-VOL1-RU-web.pdf` 4,546,960 B (< 10 MB) ·
  sha256 18d35eb4e71dfc45080bdbc4cd9dfdc6d371cec7ab387990bedf50a0252d1cfc.
  All 8 cards read visually; no defect found anywhere.
