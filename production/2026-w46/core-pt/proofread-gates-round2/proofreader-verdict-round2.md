# Round 2 Proofreader Verdict — Lucerna Weekly W46, PT target, VOL.3

- Issue dates: Mon 2026-11-09 – Sun 2026-11-15 (independently verified with `date -d` America/Toronto: 2026-11-09 Monday, 2026-11-15 Sunday, 2026-11-08 Sunday, 2026-11-07 Saturday, 2026-11-11 Wednesday, 2026-11-14 Saturday, 2026-11-20 Friday, 2026-11-27 Friday; 2026−1889 = 137).
- Scope: 11 editions (`2026-w46-pt-de, -en, -es, -fr, -it, -ja, -ko, -nl, -ru, -zh-cn, -zh-tw`) under `~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-pt-*/`.
- Proofreader role only: no edition file was edited, no re-render into edition dirs, no push/insert/Discord. All gate work lives in `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/pt-proofread-gates-round2/` (gate JSONs/logs, inventories, diffs, register dump, joined-line comparisons, masthead renders).
- Round 1 verdict: FAIL 9/11 (PASS pt-ja + pt-zh-tw), defects F-1–F-5. This round adjudicates every fix claim against the pre-fix snapshots in `hidden_files/w46/pt-fix/` and re-gates the final artifacts from scratch.

## Verdict

| Edition | Round 2 verdict |
|---|---|
| pt-de | PASS |
| pt-en | PASS |
| pt-es | PASS |
| pt-fr | PASS |
| pt-it | PASS |
| pt-ja | PASS |
| pt-ko | PASS |
| pt-nl | PASS |
| pt-ru | PASS |
| pt-zh-cn | PASS |
| pt-zh-tw | PASS |

**ROUND 2 PASS (all 11 shippable)** — zero blocking defects, zero residual defects. Two pre-existing, export-only phrasing observations (O-R2-1, O-R2-2) are recorded below; neither is a wrong key, neither is on a rendered page, neither was introduced by the fix, and neither blocks shipping. The pt-core stale-file finding is a caution, not a defect in any edition (see §4).

## 1. Fix verification (F-1–F-5)

Change scope first, verified by hash against the pre-fix snapshot (`current-hashes.txt`, 240 entries incl. pt-core): exactly **60 files changed** — de/en/es/fr/it/ko/nl/ru each 7 files (en additionally ABSTRACT.txt = 8); zh-cn 3 files (`.text.md`, web PDF, ABSTRACT.txt) with SVGs/cards/print PDF byte-identical to pre-fix; ja/zh-tw zero files changed; pt-core zero artifacts changed (KIT hash `b006faff…bdd8b` matches the pre-fix core hash exactly). Fix records are present in the WEEKLY-KIT.md of all 9 touched editions; ja/zh-tw KITs carry no-change verification notes.

| Fix | Claim | Adjudication | Evidence |
|---|---|---|---|
| F-1 | Fullwidth colon U+FF1A in P8 notes replaced by ASCII colon in the 8 Latin editions, at per-edition transform level (10 notes each: items 16,17,18,19,20,56,57,58,102,103); CJK punctuation untouched | **CONFIRMED, both directions** | Punctuation inventory (`punct-inventory-round2.txt`): de/en/es/fr/it/ko/nl/ru totals FF1A=0, U+3002=0 across all 8 SVGs; all 10/10 P8 notes per edition carry ASCII colon, e.g. `16. confere — conferir: ele → confere`. CJK editions KEPT legitimate punctuation: ja FF1A=54 / U+3002=70 (P8 FF1A=42, 10/10 fullwidth ：); zh-cn and zh-tw FF1A=54 / U+3002=48 (P8 FF1A=42, 10/10 fullwidth ：) — exactly the FIX-REPORT figures. |
| F-2 | Trailing fullwidth full stop U+3002 in the P7 clinic sentence replaced by ASCII `.` in 7 editions (de,en,es,fr,it,nl,ru); regenerated `.text.md` diffs exactly 2 lines each | **CONFIRMED** | All 7 clinic glosses end with ASCII `.` when wrap-joined (`p7-clinic-full.txt`): de `…keinen Ausgleich.`, en `…Monday off.`, es `…recupera.`, fr `…le lundi.`, it `…recupera.`, nl `…inhaal.`, ru `…выходного нет.`; ja keeps legitimate 。 (`祝日が日曜日に重なり、月曜の振替なし。`). `.text.md` diffs vs pre-fix (`textmd-diffs.txt`) are exactly 2 lines each (line 36 timetable gloss + line 371 clinic), nothing else. |
| F-3 | ko orphan 。 node deleted; clinic sentence one node ending `.`; ko `.text.md` 。 count reduced; clinic gloss geometry clean after CW−44→CW−40 tweak | **CONFIRMED** | ko P7 has 150 nodes; node 107 is the single sentence `공휴일이 일요일에 겹쳐도 월요일에 쉬지 않아요.` and node 108 is `A PALAVRA · 이번 주 단어` (no orphan node). Ko P7 U+3002=0; ko total U+3002=1, the legitimate P1 gloss node 127 `proclamação = 선포（공화국 선포）。`. Ko `.text.md` diff is exactly 1 line (371, 。→.), U+3002 count 3→2, lines 36/44 keep 。. Occlusion audit clean (0 flags); full-frame P7 card view confirms the clinic line ends `.` with a clean gap to the A PALAVRA box, no overflow. |
| F-4 | en + zh-cn abstracts rewritten practice-framed, single-line, no ASCII double-quote, facts intact; other 9 abstracts untouched and clean | **CONFIRMED** | en ABSTRACT.txt 441 bytes, 0 trailing newline, 0 ASCII double-quotes, tail now `…150 exercises on this week's topics, for English speakers learning Portuguese.` Zh-cn ABSTRACT.txt 385 bytes, 0 trailing newline, 0 double-quotes, tail now `…以本周话题为素材的 150 道练习。` Other 9 abstracts byte-identical to pre-fix and clean (full texts in `abstract-audit-round2.txt`). |
| F-5 | zh-cn `.text.md` header line 3 in Simplified Chinese with the same facts, via export; zh-cn SVGs byte-identical to pre-fix | **CONFIRMED** | zh-cn `.text.md` diff vs pre-fix is exactly line 3, now `2026 年 11 月 9–15 日 · 正文葡萄牙语 · 讲解简体中文 · 级别 A2–B2 · 150 道练习题`. All `.text.md` files are 480 lines; headers in each reader's native language verified for all 11. zh-cn SVGs/cards/print PDF byte-identical to pre-fix (change-scope hash check). |

**Regression sweep on all changed pages** (P7/P8 ×8, ko P7, abstracts, zh-cn header): no new defect found. Re-gates below (§3) all clean; card views of every changed page clean (§3, cards).

**Round 1 adjudicated non-defects stay non-defects** (re-confirmed, not re-raised): pt-es P2 wrap orphan node `2.` (node 151 after `Completa con los números de las páginas 1 y`); pt-ko short wrap tails; ABSTRACT trailing newlines (now 0 in the two rewritten abstracts; cosmetic elsewhere); KIT subtitle-width figures (advance-width estimates).

## 2. Full key verification — 150/150 semantically correct

Method: the core register was parsed statically (AST, no execution) from `hidden_files/weekly-report-w46-pt-build/content12.py, content34.py, content56.py, content7.py, content8.py` + `bslib4.py` REG (`register-dump.json/.txt`): 150 items, A2 49 / B1 70 / B2 31; per-file 28/36/36/12/38 = per-page 10/18/18/18/18/18/12/38. Every key was checked semantically against the issue's own articles (Enem day 2 Sun 15 Nov, gates 12h/13h, exam 13h30–18h30, 90 questions = 45+45, day 1 Sat 8 Nov to 19h, Proclamation 15 Nov 1889 = 137 years, Deodoro first president, Lei nº 662 of 1949 as distractor, national holiday, no Monday make-up, no DST since 2019; first legs 1 Nov Grêmio 2–0 Atlético-MG and Palmeiras 1–0 Vasco; second legs Sat 7 Nov 18h Arena MRV and Sun 8 Nov 17h São Januário; final single game 6 Dec Mané Garrincha; Brasileirão round 35 only Mirassol × Atlético-MG on Sat 14; Brazil × Japan Sat 14 7h15 Singapore, 26 players; Black Friday 27 Nov, 11.11 Wed 11 Nov; Marina passage). Arithmetic recomputed: 12h→13h = 1h (#21); 13h30→18h30 = 5h (#22); 5×60 = 300 min (#23); 45+45 = 90 (#24); chart 60/30/300, 60+30+300 = 390, 12h→18h30 = 6h30 (#83–87, #127). Verb morphology verified item by item (present, pretérito perfeito, futuro do presente, futuro do subjuntivo), incl. #112 B `for` (not `é`/`seja`). Comparatives mais/menos (#56–59) correct. Word-order items #44–46, #133–136 correct incl. sentence-initial capitalisation. Items #93 (`começará`) and #94 (`chegar`, future subjunctive) are defensible: the keys are the correct forms matching the section's tense-training contrast (#95/#96 are the present-tense items; P7 §B2 teaches the quando/se/quem + future-subjunctive rule); present-tense alternatives would be grammatical in free Portuguese but are not the keyed taught forms. Not defects.

Register keys vs `p8.py extract` core keys differ only at #150 (register key `(开放题，范文如下)` = open-question note; P8 prints `✓` + model-essay pointer — expected, not a defect). Model essay (#150): 88 words exactly by whitespace count from SVG nodes 159–167, within the 80–100 prompt.

**P8 renderings in all 11 editions** (`p8-joined-lines.json`, `p8-joined-compare.txt`, `p8-answers-joined.txt`, `stems137-144-check.txt`, `match-order-check.txt`): joined answer lines extracted wrap-aware — 150/150 lines in every edition. Key parts are byte-identical to the core except exactly: #137/#138 (legitimate native-language translations — each verified correct, e.g. en `Sunday, November 15, is the second day of the Enem.` / `Check your card before Sunday.`; de, es, fr, it, ja, ko, nl, zh-tw all correct; ru full joined line `Воскресенье 15 ноября — второй день Enem.` — the shorter `p8.py extract` value for ru #137 was an extractor line-truncation artifact, NOT a defect) and #150 (native "see model text in section H" pointer, all citing 88 words, e.g. ru `✓ Образец — в разделе H этой страницы (88 слов)`). Stems #139/#140 in each edition are correct native sentences translating to the PT keys (`O feriado cai num domingo.` / `Quando você chegar, apresente o documento com foto.`); stems #137/#138 are the Portuguese sentences in every edition. **No key transposition in any edition. Zero wrong key letters. Key-verification result: 150/150 in the core and in all 11 P8 renderings.**

### Matching blocks — stem + options + key, quoted in full

**#25–28 (P2).** Options (identical order in core and every edition):
a. `a ciência dos números e das formas` · b. `o ato de anunciar uma mudança` · c. `um dia de descanso marcado por lei` · d. `a ciência da vida, da física e da química`.
Keys: 25 `proclamação` → **b** (announcing a change — correct); 26 `feriado` → **c** (a rest day fixed by law — correct); 27 `natureza` → **d** (the science of life, physics and chemistry — correct); 28 `matemática` → **a** (the science of numbers and shapes — correct). Match-note glosses in every edition repeat the correct letter and definition.

**#52–55 (P4).** Options (identical order in core and every edition):
a. `o segundo jogo de um confronto` · b. `o ponto marcado na rede` · c. `a cobrança da marca dos onze metros` · d. `o primeiro jogo de um confronto`.
Keys: 52 `gol` → **b** (the point scored in the net — correct); 53 `ida` → **d** (the first game of a tie — correct); 54 `volta` → **a** (the second game of a tie — correct); 55 `pênalti` → **c** (the kick from the eleven-metre mark — correct). Match-note glosses in every edition repeat the correct letter and definition.

**#141–144 (P8).** Options (identical order in core and every edition):
a. `a forma do Estado depois de 1889` · b. `o ato de anunciar uma mudança` · c. `uma nova entrada depois do fechamento — que não existe no Enem` · d. `a porta de entrada do local de prova`.
Keys: 141 `proclamação` → **b** (correct); 142 `portão` → **d** (correct); 143 `república` → **a** (correct); 144 `segunda chamada` → **c** (correct). Match-note glosses in every edition repeat the correct letter and definition.

## 3. Re-gates on the final artifacts (all re-run from scratch; fix worker's gate JSONs not accepted)

- **freeze.py diff** (core = `weekly-report-w46-pt-core/svg`, `freeze-pt-*.json/.log`): 7 Latin editions added CJK = 0. ko added CJK = 3140 (legitimate Hangul). zh-cn added CJK = 118, furniture-only: P1 +2/−2 strings (badge + footer), other pages +1/−1 (footer string `A Lucerna · 葡萄牙语周报 VOL.3 · 正文葡萄牙语 · 讲解简体中文`). ja added CJK = 2728, zh-tw = 911 (legitimate native script).
- **p8.py compare** (`--total 150`, `p8-pt-*.json/.log`, `p8-extract-pt-*.json`, `p8-core-extract.json`): **CLEAN 150/150 in all 11**, missing=[], extra=0, uncertain=[]; keydiff=[137,138] in all editions except pt-zh-cn ([]), adjudicated legitimate native translations (§2).
- **occlusion_audit.py** (`occlusion-pt-*.json/.log`): selftest OK on every run (all 6 planted classes fired, clean controls silent); **0 flags in all 11 editions (88 pages)**.
- **Counts re-measured** (`regates.txt`): 150 items; A2 49 / B1 70 / B2 31; per-page stems 10/18/18/18/18/18/12/38 in every edition (the single apparent extra, pt-es P2 = 19 nodes, is the R1-adjudicated O-1 wrap orphan `2.`). Paragraph freeze: 82/82 long PT sentences present (punctuation-insensitive) in every edition's P1–P6 joined text. P7 quotes: 8/8 verbatim in every edition (incl. lowercase #3 `o feriado não muda o relógio`), correct `(Página N)` labels.
- **P6 chart** (`p6-es-check.txt`): bar rects w=90/45/450 px (1.5 px/min) at identical coordinates in core and all 11 editions; P6 rect diffs vs core are only translated-gloss box heights / level-chip y-shifts (ja/ko/zh-cn/zh-tw rect-identical); caption `60 + 30 + 300 = 390` present everywhere.
- **Masthead pixel clearance** (`masthead-pixels.txt`, `masthead-pixels2.txt`, `masthead-pixels3.txt`, renders in `masthead-renders/`): masthead element identical in all 11 (x=975, y=262, size 168, UnifrakturMaguntia `A Lucerna`, font-metric ink width 710 px → x 620–1330, 555 px clearance each side to the inner frame). Subtitle lines (y=330) advance widths 1705–1756 px, centred, ≥32 px frame clearance at advance width (rendered ink per Round 1 ≥26 px). Badge/pairing lines (y=372) 485–1082 px, centred, ≥439 px clearance. Badge visibly in the P1 masthead in all 11 (subtitle + pairing line present); native footers on all 8 pages of every edition (`badge-pdf-residue.txt`: 8 distinct native page labels per edition). No frame contact; occlusion audit 0 flags.
- **PDF text layer + sizes** (`badge-pdf-residue.txt`): all 11 web PDFs ≤7 MB (882,786–1,614,344 bytes) with `pdftotext` output 43,019–53,258 bytes (>0) — text layer present. Print PDFs are larger (3.29–15.69 MB; ja/ko/zh-cn/zh-tw >7 MB) — see observation O-R2-3; they are not the web/insert artifact (insert reads the web PDF only, §4).
- **Residue / reader-facing sweep** (`badge-pdf-residue.txt`): U+FFFD=0 in all 11; `tu`-forms=0, `você`=13 in all 11 (register consistent); wrong-script residue 0 (ko U+3002=1 legitimate P1 gloss; ja/zh-cn/zh-tw CJK counts legitimate); no `w46`/`pt-`/`github`/`index.json`/`Discord`/`proofread`/`occlusion`/`lint`/`2026-w46`/`weekly-report` markers in any SVG text. `VOL.2`/`VOL.4` hits are the legitimate reader-letters note cross-references to the previous/next volume; `transform` hits are the Portuguese verb `transformar` in article text; the pt-it `SOP` hit is the substring in Italian `sopra` ("above"). No real internal-marker hits. zh-cn 0 traditional-only probes (`複習, 詞組, 分區, 毛里西奧, 繁體, 講解繁體, 週報`); zh-tw 0 simplified-only probes (`复习, 词组, 分区, 简体, 讲解简体`). ja kinsoku: 0 bad line-starts. Gloss prefixes per KIT confirmed in card views (e.g. de `Stichwörter |`, en `Key words |`, ja `キーワード |`, ko `핵심 단어 |`, zh-cn `讲解 |`).
- **W45 promises honoured** (re-confirmed from the final cards): Enem day 2 + Proclamation headline on P1; editorial example + bilingual disclosure on P7 (all 11: `EXEMPLO DA REDAÇÃO` + native disclosure, promise carried to VOL.4); second-leg deadline note + first-leg scores on P1; P4 open update slot recorded as an insert-time decision.
- **Cards** (visual, full frame): P1 × 11, P8 × 11, P7 × 8 changed editions — all viewed. No overflow, no overlap, no missing glyphs/tofu, photo credit present on every P1 (`Foto: Gary Todd / Wikimedia Commons — CC0`), footer intrusion none, ko P7 clinic/A PALAVRA gap clean. P2–P7 otherwise covered by the geometric gates plus these spot checks.

Optional freeze-baseline reproduction was deliberately skipped: the diff gate against the frozen core already establishes content equality, and re-running a baseline build was not needed for the verdict. No shipped file was touched.

## 4. pt-core finding (caution, not a defect in any edition)

`files/weekly-report-w46-pt-core/` is a frozen duplicate/reference of the pt-zh-cn edition, left untouched by the fix (all artifact hashes match the pre-fix snapshot; KIT hash matches). Its SVGs differ from the canonical zh-cn SVGs on all 8 pages by furniture strings only (freeze diff: badge + footer), consistent with the zh-cn KIT stating content identical to core except furniture. The core's `ABSTRACT.txt` still holds the pre-fix news-framed tail (`…适合学葡萄牙语的读者通过巴西新闻学葡萄牙语。`) and its `.text.md` line 3 is still the Portuguese header (`Semana de 9 a 15 de novembro de 2026 · … · 150 exercícios`).

Verified: **no shippable artifact comes from pt-core, and no insert-time process can read it by default.**

- `tools/insert.py` requires an explicit `--edition-dir` and reads the web PDF / `<slug>.text.md` / `ABSTRACT.txt` ONLY from that dir; the slug is derived from `--week/--target/--native` arguments, not from the dir name. No code path defaults to pt-core.
- `tools/tables.py`: `edition_dir('pt','zh-cn')` returns `weekly-report-pt-zh-cn` (generic rule, no W46 prefix); `core_dir('pt')` returns `weekly-report-pt-vol1` — neither is `weekly-report-w46-pt-core`.
- `tools/freeze.py diff` uses pt-core only as a read-only `--core-svg` reference.
- `hidden_files/w46/pt-fix/derive_all.py` reads pt-core `.text.md` ONLY as a derive SOURCE, with `HEADER_OLD` = the Portuguese header as anchor and per-edition `header_new` from `derive-args.json` (zh-cn `header_new` is the fixed Simplified-Chinese header) — a re-derive would reproduce the F-5 fix, not overwrite it. It never writes into pt-core. `pt-fix/gates_one.sh` uses pt-core only as a freeze reference.

Residual risk is limited to a human/coordinator explicitly passing `--edition-dir …/weekly-report-w46-pt-core` to insert.py. Recommendation: keep pt-core clearly labelled as a frozen reference (it already is, by the fix record) and never pass it as an edition dir. **Not a defect: no edition file, gate, or default process is affected.**

## 5. Observations (non-blocking, pre-existing, out of fix scope)

- **O-R2-1** — ru `.text.md` lines 461–462 stem phrasing differs from the P8 page stems: export reads `139. «Праздник выпал на воскресенье».` / `140. Придя, предъявите документ с фотографией.` while P8 stems read `«Праздник выпадает на воскресенье.»` / `«Когда придёшь, покажи документ с фото.»`. Same meaning, same PT answers (`O feriado cai num domingo.` / `Quando você chegar, apresente o documento com foto.`); export-only variance frozen from the pre-fix shipped `.text.md`, untouched by the fix, and not a wrong key. Recorded for a future export pass; does not block.
- **O-R2-2** — ja `.text.md` line 462 reads `写真付き身分証` while the P8 stem reads `写真付きの身分証` (の dropped in the export). Same meaning, same answer; pre-existing export variance, not a wrong key. Does not block.
- **O-R2-3** — Print PDFs exceed 7 MB for ja (15,687,617), zh-tw (14,818,306), zh-cn (14,775,653) and ko (7,072,429) bytes. The ≤7 MB gate applies to the web PDFs (all pass, §3) and insert reads the web PDF only (§4); the print PDFs are local artifacts, byte-identical to pre-fix for ja/zh-tw. Noted for the coordinator's push planning only; does not block.

## 6. Residual defect list

**None.** Zero blocking defects, zero residual defects. All Round 1 defects F-1–F-5 are CONFIRMED fixed (both directions for F-1), all 150 keys verified semantically correct in the core and in all 11 P8 renderings, all re-gates clean, all card views clean.

## 7. Gate artifacts saved in this directory

`current-hashes.txt`, `punct-inventory-round2.txt`, `f2-f3-f5-check.txt`, `p7-clinic-full.txt`, `textmd-diffs.txt`, `abstract-audit-round2.txt`, `freeze-pt-*.json/.log`, `p8-pt-*.json/.log`, `p8-extract-pt-*.json`, `p8-core-extract.json`, `occlusion-pt-*.json/.log`, `register-dump.json/.txt`, `core-p1..p7-nodes.txt`, `core-p8-nodes.txt`, `p8-stems-core.txt`, `p8-stems-en.txt`, `p8-joined-lines.json`, `p8-joined-compare.txt`, `p8-answers-joined.txt`, `stems137-144-check.txt`, `match-order-check.txt`, `regates.txt`, `p6-es-check.txt`, `badge-pdf-residue.txt`, `masthead-pixels.txt`, `masthead-pixels2.txt`, `masthead-pixels3.txt`, `masthead-renders/p1-*.png`.

**ROUND 2 PASS (all 11 shippable)**
