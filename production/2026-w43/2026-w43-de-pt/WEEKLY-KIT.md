# Lucerna Weekly — DE × PT (VOL.1, W43: 19–25 October 2026)

**Edition:** German target text (frozen VOL.1 core) with ALL explanations in Portuguese (Brazilian) — the edition for Portuguese-speaking readers of German.
**Masthead:** Die Lucerna · **Pairing badge (P1):** TEXTOS EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA
**Build:** `hidden_files/weekly-report-de-pt-build/` (copy of the frozen core build `hidden_files/weekly-report-de-build/`; core never edited). Transform: `scratch/transform_pt.py` + `scratch/fix_pt.py` (exact-count replacement scripts, kept in scratch/).
**Scope of this build:** build only — no repo insert, no Discord.

## 1. Baseline proof (method step 1)

The copied core build was run UNMODIFIED with output pointed at `baseline-out/` inside the copy. All 8 produced SVGs are byte-identical (sha256) to the shipped core SVGs in `files/weekly-report-de-vol1/svg/`:

| page | core shipped sha256 | baseline reproduction |
|---|---|---|
| p1-front | be1b0f7b7f2cbee013bc6246ad7bf95fc7ddbf32c62e43ac84b37af2f2ed647d | MATCH |
| p2-leben | cac83eb5d228e2efea12f6a6967f5c89435cc1e9617348c24642d02530515b18 | MATCH |
| p3-kultur | d862d862b1232d292de89ca9b90793f10b9797bbe03fc18f4c2b914ce64db9ba | MATCH |
| p4-sport | 591eaa94747d50139db87c569c50fe6fea38396df627c64ff2b195fd18ba379a | MATCH |
| p5-jugend | b48ed8104190dda2eeeca933a15d2388fcb7066bd2a771d4f6c4ffb679af1504 | MATCH |
| p6-vertiefung | a69b6fee767dfe180ddf395180acdd3b413b56177b1be2de391a08094f21b23e | MATCH |
| p7-sprache | b4f74e0844fbf92975d93ee3cdbc5ac4baab4869840e3b03ac5e7834b73477be | MATCH |
| p8-uebungen | 8fb288ff2ee063660c2b26b825cb868ccaf9b9a7d86e95810d26dd81b0b9761d | MATCH |

Baseline: **8/8 byte-identical.** The core's shipped SVG hashes were re-verified unchanged after all work (same table, final check §11).

## 2. Totals (registry dump of the final build)

- **Exercises: 150** — A2 67 · B1 69 · B2 14 (identical to the core).
- Per page: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38 (identical to the core).
- Registry types (Portuguese names, counts): Completar frases 42 · Escolha múltipla 47 · Transformação de frases 16 · Correspondência de palavras 12 · Verdadeiro ou falso 8 · Construir frases 7 · Completar o texto 8 · Tradução 4 · Completar o diálogo 5 · Escrita 1.
- Instruction tokens: Complete · Reescreva · V ou F · Monte a frase · Associe as palavras · Traduza para o português / Traduza para o alemão.

## 3. PT furniture — as finally shipped (verbatim)

- P1 top strip centre: `WÖCHENTLICH AUF DEUTSCH · TODA SEMANA · O ALEMÃO QUE OS ALEMÃES LEEM`
- P1 subtitle (46 pt): `SEMANÁRIO EM ALEMÃO · VOL.1 · RELÓGIOS · FÉRIAS · GEADA`
- P1 pairing badge (brick, bold, 20 pt, y=372 slot): `TEXTOS EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA`
- P1 clock band, right side: `Domingo: relógio para trás` / `A noite de 25 horas · página 2`
- Footer line 1 (all pages): `Die Lucerna · SEMANÁRIO ALEMÃO VOL.1 · TEXTOS EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS`
- Footer line 2: `Página N de 8`
- Gloss prefix: `Nota — `
- P8 page separators: `— Página N —`
- P8 keys header: `ANTWORTEN · TODAS AS RESPOSTAS COM NOTAS (PÁGINAS 1–8)`
- P8 answer format: space before each note parenthesis, half-width parens only; keys typeset 13 px / 1.26 (the documented DE-family P8 adjustment, same as DE×FR / DE×ES / DE×IT).
- Section/box heads use the pattern German title + Portuguese part, e.g. `DIE TOPMELDUNG · Manchete`, `IN DIESER AUSGABE · Sumário`, `DER WERKZEUGKASTEN · Úteis`, `A · LÜCKENTEXT · Texto lacunar`, `F · WÖRTER PAAREN · Associe`.

## 4. Key-diff registry (the ONLY registry deviations from the core)

Translation-type items legitimately re-aim at Portuguese; everything else is byte-identical to the core registry (keys and German text frozen).

| # | core (DE × ZH) | this edition (DE × PT) | kind |
|---|---|---|---|
| 137 | key = Chinese translation of „Die Nacht hat 25 Stunden."; stem = the German sentence + „translate into Chinese" | key = **„Esta noite tem 25 horas."**; stem = „Die Nacht hat 25 Stunden."; instr = „Traduza para o português" | key + stem re-aimed |
| 138 | key = Chinese translation of „Ich stelle die Uhr am Samstagabend um." | key = **„No sábado à noite, ajusto o relógio."**; stem = the German sentence; instr = „Traduza para o português" | key + stem re-aimed |
| 139 | stem = Chinese sentence „I sleep one hour longer on Sunday" + „translate into German"; key = German sentence | stem = **„No domingo, durmo uma hora a mais."**; instr = „Traduza para o alemão"; key unchanged (German) | stem re-aimed only |
| 140 | stem = Chinese sentence „In the library one can borrow books" + „translate into German"; key = German sentence | stem = **„Na biblioteca, pode-se pegar livros emprestados."**; instr = „Traduza para o alemão"; key unchanged (German) | stem re-aimed only |
| 150 | writing apparatus: Chinese key/note (open question, graded by points) | key = **„Pergunta aberta — siga os pontos do quadro de escrita; o texto-modelo está no quadro desta página"**; note = **„Avaliação pelos pontos indicados"** | apparatus translated |

Notes on all other 145 items: translated into Portuguese 1:1 (notes that were already pure German/formula in the core — e.g. „trennbar: um-ge-stellt", „gewinnen → gewann", „46 + 18 = 64" — are unchanged, as in the other DE fan-outs).

## 5. Printed-note set verification (mandatory gate)

The core prints ALL 150 P8 notes (print-all rule). Verified **in the rendered P8 SVG** of this edition (not just the registry): the key block contains exactly 150 numbered entries (1–150, none missing), and **every entry carries its note** in the form `key (note)` — space + half-width parens; full-width parens in the key block: **0**. Printed set = core set = {1…150}. **EQUAL.**

## 6. Freeze check

Full text diff of the 8 final SVGs against the core's shipped SVGs (multiset of text elements per page; record: `scratch/freeze-diff.txt`). Every differing fragment is one of: (a) Portuguese explanation layer (glosses, instruction lines, exercise instructions, P8 notes), (b) pairing furniture (§3), (c) the documented registry items (§4). **No German target text outside §4 differs.** Zero CJK characters in the final SVGs; zero CJK/full-width characters in the operative build code.

## 7. Wording-only fit fixes (geometry never touched)

Portuguese runs longer than the core's Chinese layer; five spots needed shorter Portuguese wording so the frozen layout fits exactly as the core's does (final flow ends match the core's: P1 headline flow ends y=1585 = core; P2 col 3 ends 1519.75 = core; P5 exercises 2138 = core; P6 exercises 2402 = core; P7 col 3 ends 1485.5 = core):

1. P1 gloss line shortened (fits 4 rendered lines; the Bundesland gloss was dropped from this one line — all clock terms kept; the word is glossed again in the P2 article gloss family wording and in the numbers box context).
2. P1 numbers-box parentheticals shortened: `(25 horas)`, `(11 em férias juntos)`, `(mais de 8 000 no país)`.
3. P2 „Und Sie?" Portuguese paragraph shortened to 2 lines (question content preserved: Funkuhr at home? adjust the clocks yourself? write two German sentences).
4. P6 health-box Portuguese paragraph compressed (all STIKO groups kept: 60+, pregnant from the 2nd third, chronically ill, health professionals; protection 10–14 days).
5. One-line instruction lines on P4/P5/P6 (`Leia o artigo… e responda.` etc.) so exercise columns cascade exactly as in the core.
6. Three box/section titles shortened after the geometric audit found their ink crossing their own box borders: `DIE WOCHE IN ZAHLEN · Números`, `IN DIESER AUSGABE · Sumário`, `DER WERKZEUGKASTEN · Úteis`; P8 heads `A · LÜCKENTEXT · Texto lacunar` and `F · WÖRTER PAAREN · Associe` (the build's head-width check).

## 8. Geometric occlusion audit (mandatory gate)

Script: `scratch/audit.py` — paint-order SVG parse, text ink boxes from PIL real-font metrics (the build's own Noto CJK fonts + UnifrakturMaguntia), line boxes expanded by half the stroke width. Classes: COVER (≥30% ink under a later opaque shape), LINE-INK, TT (text–text), BAND (footer rule y=2580), EDGE, TITLE (ink past its own box border), BOXBOT, BOXLINE. **Validated first on a synthetic positive control: all planted defects flagged (COVER 100%, LINE-INK, BAND, EDGE, TITLE, TT).**

Results on the final SVGs: **0 flags in every hard class** (COVER, LINE-INK, TT, BAND, EDGE, BOXLINE all zero on all 8 pages). Remaining TITLE/BOXBOT heuristic hits were adjudicated one by one:

- Identical-geometry core inheritances (same coordinates in the core's SVGs; not introduced here): P2 facts-box last line descenders touching the box bottom border (pixel-crop compared core vs this edition: pixel-identical; text paints over the border; legibility unaffected); P3 facts-box and P5 facts-box bottom grazes; P6 Pro-&-Contra line graze.
- Free full-width lines with no container and no collision (right-anchored subtitles, section titles, footer lines; ink ends inside the page measure, max x=1885 < 1890): the audit's nearest-rect heuristic matches them to unrelated boxes; the core shows the same pattern.
- P6 health box: last Portuguese line ink bottom y=1399.1 vs box bottom 1400 — INSIDE the box; pixel crop confirms clean clearance above the border in the render and 8 px clearance to the chart rule below (y=1408).
- Three real defects found by the audit and fixed by wording (see §7.6): P1 numbers-box title, P1 sommaire title, P7 toolbox title — re-audit after fixes: gone.

Final: **0 unresolved NEW flags vs the core.**

## 9. Builder's full proofread (own pass, complete)

- Read every page end-to-end in the rendered cards. German text byte-identical to the frozen core (freeze check §6); Portuguese layer read in full via the freeze diff.
- **All 150 keys re-derived** from the German text and compared against the printed P8 block: identical to the core's registry values except §4 items. Chart arithmetic re-added (46+22+18+14=100; 46+18=64). „halb zehn = 9:30", „halb drei = 2:30" traps intact.
- **P7 phrases of the week:** all 8 German quotations are verbatim contiguous excerpts of this issue's articles with correct page tags; each occurs **exactly 2×** in the full issue (article + P7), counted programmatically in both this edition and the core — counts equal (2/2 for all 8).
- **Calendar:** every weekday/date claim in the Portuguese layer verified against the real 2026 calendar — Zeitumstellung Sun 25 Oct 03:00→02:00; Tag der Bibliotheken Sat 24 Oct; Klassiker Sat 31 Oct; Allerheiligen Sun 1 Nov; P4 Friday match Fri 23 Oct 20:30; P3 note „o 31 de outubro é sábado" correct. (German-layer claims are the core's, already proofread there.)
- Totals/levels/per-page counts re-dumped from the final registry (§2) — equal to the core.
- Masthead „Die Lucerna" on all 8 pages; pairing visibly badged on P1 and in every footer.
- Zero politics beyond the core's frozen domestic-debate content (P6 EU clock debate, as in all DE fan-outs).

## 10. Images (inherited from the core; all public domain, verified per image in the core KIT)

| file | subject | credit (as printed) |
|---|---|---|
| frost.jpg | Hoar frost on branches | Courtney Celley, U.S. Fish and Wildlife Service — public domain (US federal work) |
| atomuhr.jpg | NIST-F1 atomic clock | NIST — public domain (US federal work) |
| luther.jpg | Martin Luther, 1528 | Lucas Cranach the Elder, Veste Coburg — public domain (life+70) |
| kuerbis.jpg | Pumpkins at USDA Farmers Market, 2016 | U.S. Department of Agriculture — public domain (US federal work) |

Full credit lines are printed under each image in the paper, unchanged from the core.

## 11. Deliverables

In `files/weekly-report-de-pt/`: `svg/` ×8, `cards/` ×8 PNG (1950×2700), print PDF, web PDF, this KIT.

| file | bytes | sha256 |
|---|---|---|
| The-Lucerna-VOL1-de-pt.pdf (print) | 9,360,031 | de1a15071e7ec7de6957effc596bd2526bb1031c6fbd789fcf6e3f26c5d24c79 |
| 2026-w43-de-pt.web.pdf | 1,471,934 | 9ded968023edde7aaff1cc153bb61f34471f9a18e667b31f646375884aaf6f1 |

Web PDF < 10 MB ✓ (1400 px-wide JPEG pages, q85 — the finalized core recipe). Final SVGs (sha256): p1 710fb692…, p2 cb807038…, p3 faf45392…, p4 91d5772f…, p5 1fa99440…, p6 5498d084…, p7 3a7dd7b7…, p8 9eaacb1d… (full values in the build log).

Core integrity: the frozen core's shipped SVG sha256 values (§1 table) re-verified at the end of the build — **unchanged**.

Hygiene: the explanation method was renamed (`expl()`) throughout the operative build code; the pre-rename name and the intermediary-layer term occur **zero times** in the paper, this KIT, and the operative build code. The frozen core's original call strings appear only as search patterns inside the one-off transform scripts under `scratch/`, per the standing hygiene adjudication.

## 12. Status

Builder's own proofread complete (this KIT). **Independent proofread: PASS** (2026-10-22, proofreader agent; one defect found and fixed, then the full pass re-run clean — see §13). No repo insert, no Discord (per scope).

## 13. Independent proofread record (2026-10-22)

**Verdict: PASS after one explanation-layer fix.**

**Defect found & fixed (P1 gloss):** the P1 gloss line dropped the core's fifth entry («das Bundesland 联邦州») — the core glosses five terms, this edition carried four, and the word is glossed nowhere else in the edition (P2 glosses the different word «Bundesanstalt»; the P1 numbers box only paraphrases the phrase). §7.1's justification ("glossed again on P2 / in the numbers box") does not hold. Shipped siblings DE×ES/FR/IT/RU all keep the entry. Fix (wording only, build `content12.py` line 42, single-process `run.py` + `render.py` re-render): the line now ends «… · Winterzeit = horário de inverno · Bundesland = estado federado.» — it fits the existing 4th rendered line (previously just «inverno.»); every baseline on P1 is unchanged, P2–P8 SVGs are byte-identical to the pre-fix state, and the core is untouched (hashes re-verified).

**Minor KIT prose slip (edition itself correct):** §9 lists the first-frost / oven-clock facts against #22/#23 in swapped order — as printed, #22 is the oven-clock item (key C) and #23 the first-frost item (key A, night Mon→Tue 19→20 Oct ✓).

**Full pass (run twice — before and after the fix; post-fix values):**
- freeze.py baseline: core build reproduces the shipped core 8/8 byte-identical; core hashes unchanged after all work.
- freeze.py diff: added CJK = 0 on all 8 pages; edition CJK total = 0; removed-side non-German strings classified (pairing badge slot on P1 — same structure as shipped DE×NL — plus re-wrap fragments of translated notes).
- Registry (independently dumped, one process, both builds): 150 = 150; levels A2 67 · B1 69 · B2 14; per-page counts identical; page/level zero diffs; type labels 1:1 zh→PT with identical counts; key diffs exactly {137, 138, 150} (137 «Esta noite tem 25 horas.» / 138 «No sábado à noite, ajusto o relógio.» — faithful; 150 apparatus translated); stems {139, 140} translated, keys unchanged German; notes byte-unchanged = exactly 15 items {16, 17, 19, 37, 46, 57, 60, 61, 62, 63, 85, 88, 99, 104, 129}, all pure German/formula.
- p8.py compare: **CLEAN** — core 150 noted = edition 150 noted, missing [], extra 0, keydiff [137, 138, 150].
- P8 style & size (README #14/#3): answer notes half-width ` (note)` per the DE fan-out build code (edition P8 full-width parens = 0; core 169); answer block 13.0/1.26 — the DE×FR/ES/IT subgroup value (DE×NL/RU use 13.0/1.16); last body baseline 2559.68 vs core 2559.73, ink bottom ≈ 2564, clear of the 2580 footer rule.
- Occlusion audit (canonical, selftest first): edition **0 flags**; core 1 flag (its own frozen P1 Fragen-subtitle BOXTITLE); new vs core = 0. The edition's own PT Fragen subtitle passes on its own ink (README #15).
- Same-line ink scan (all 8 pages, both versions): 0 collisions. Chart element check (README #12): P6 bar rects identical to core (46/22/18/14 = 100), chart-label ink coverage by later shapes 0% in both; the only rect diffs are two explanation-box bottoms extended for PT text (audit BOXBOT clean).
- Manual key re-derivation from the German text: chart #83–88 (B/C/B/B/A/B from 46/22/18/14), matching #25–28 / #52–55 / #141–144 letter maps, time traps #11/#101/#104/#129 (halb drei = 2:30, Viertel vor, halb vier = 3:30, halb zehn = 9:30 → A), build items #44–46, #22/#23, dialogue #145–149, #137–140, #150 — all derive correctly.
- P7: all 8 German quotes occur exactly 2× in both versions; page tags «Seite N · LEVEL» multiset identical to core (DE-family shipped pattern, cf. DE×ES/FR/IT/NL/RU).
- Calendar vs real 2026 (Europe/Berlin, programmatic): Sat 24 Oct, Sun 25 Oct (03:00→02:00), Tue 20 Oct (Dortmund), Fri 23 Oct, Sat 31 Oct, Sun 1 Nov, Sun 28 Mar 2027 — all as printed. Model essay counted: exactly 87 words (label «87 palavras» accurate).
- Furniture verbatim: badge ×1, footer ×8/8 with «Página N de 8», gloss prefix «Nota — » (6 gloss lines, parity with DE×NL), P8 separators «— Página N —» (shipped PT-column form, cf. EN×PT/JA×PT/zh×PT).
- Residues: CJK/full-width = 0; Dutch/Russian/other-column furniture = 0; banned intermediary term = 0 in paper/KIT/operative code (scratch transform scripts + basecheck core copies only, the disclosed exception); `expl()` rename verified (def + 22 call sites).
- Images: embedded JPEG payloads md5-identical to core on P1/P2/P3/P5; credit lines byte-identical (Courtney Celley / USFWS, NIST, USDA). P2 facts-box region pixel-identical to core (the core's box-bottom graze is inherited unchanged, German text frozen).
- Brazilian PT: no EP-only spellings/constructions found («você» throughout; the single «está a» hit is estar + article, not the EP progressive).
- **Final pins (D5 重建，2026-11-13):** print `The-Lucerna-VOL1-de-pt.pdf` 9,360,031 B, sha256 `de1a15071e7ec7de6957effc596bd2526bb1031c6fbd789fcf6e3f26c5d24c79`; web `2026-w43-de-pt.web.pdf` 1,471,934 B, sha256 `9ded968023edde7aaff1cc153bb61f34471f9a18e667b31f646375884aaf6f1`; both 8 pages. (Pre-D5 builder pins were also verified as measured: 10,484,289 B / 62b53122… and 4,268,240 B / 030ba97c…; only P1 changed.)
## D5 重建记录（2026-11-13，W43/W45/W46 D5+§1.1 合并重修 Phase 1）

- **原因**：D5 缺陷——sans 层拉丁/西里尔字符落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者）。本版修前 census：D5 拉丁 660、西里尔 0、弯引号 CJK 0。
- **安装**：`tools/mechanism-w47/apply_variant.py --svglib <版>/svglib.py --target de --reader pt --week 2026-w43`（先 `--check` dry-run 通过）。`_D5_READER = "latin"`。路由单元测试 `test_d5_routing.py` FAILURES: 0。fix2（U+201C/U+201D/U+2019 → serif）保留：本版弯引号 33 个全在 Newsreader。
- **基线**：重建前先证基线干净——`run.py` TOTAL 150、0 警告；重建 SVG 8/8 与 port fanout 逐字节相同；印 PDF 与 fanout BYTE-IDENTICAL。基线实测（§1.1 组装版）：印 PDF `50732a94fc4233e0f1c12eb00d0e8087a21e371ac3df17149a8048f97eae72d1`（9950637 B）、网 PDF `1c636e17111d437f21748e926a6195ef5fcc5e3ece6c47b88d5b30a0bf09dcd7`（1559224 B）。本 KIT 上方旧值（更旧配方）已过期，以上两值为准。
- **二次修复（只动字号与断行，文字零改动；实测 advance，patched svglib `text_w`，sans bold；栏宽 CW=422.5，盒标题内宽 404.5，P7 两 p.text 标题内宽 400.5）**：
  1. `content12.py:25` P1 band 标题 36→31pt（与最紧 band-right 左界 ru 1542.0 间隙 76.7px）。
  2. `content12.py:124` herbst 头 25→22pt（框宽 422.5；25pt 430.2 超 7.7px，22pt 378.6）。
  3. `content12.py:47` numbers 盒 `f.box` 加 tsize=21（最差 +25.8；21pt 最大 392.8 < 404.5）。
  4. `content12.py:89` contents `IN DIESER AUSGABE` 24→22pt（最差 +9.0）。
  5. `content12.py:175` merksatz 盒 `f.box` 加 tsize=21（最差 +25.5；21pt 最大 392.5 < 404.5）。
  6. `content34.py:35` / `content56.py:34` P3/P5 facts 盒 +14→+34（末行溢出约 12.7px；en 家先例）。
  7. `content56.py:56` P5 Saturday-plan 头 24→22pt（nl +55.3；22pt 829.3 < 849.4）。
  8. `content56.py:155` P6 timeline 头 24→22pt（pt +10.3；22pt 376.1 < 400.5）。
  9. `content7.py:72` Toolbox 23→21pt（最差 +23.0；21pt 最大 386.4 < 400.5；22pt en 404.7 仍超）。
  10. `content7.py:92` NOCH EIN WORT 22→21pt（最差 +11.6；21pt 393.0 < 400.5）。
  11. `content8.py:74` P8 D 组头 24→22pt（it 428.3、nl 431.5 均超 422.5；22pt 最大 395.6）。

- P2 例外（run2b）：P2 facts 盒改回 +14（高度不变），facts 正文 21.5→21pt（wrap 8→7 行，盒底 356，余 22.1px）；P3/P5 保持 +34。
- **P8**：行数 226→232，距页脚线余量 33.3px；p8 compare CLEAN（keydiff [137, 138, 150]）。
- **新交付物（D5 重建，2026-11-13）**：印 PDF `de1a15071e7ec7de6957effc596bd2526bb1031c6fbd789fcf6e3f26c5d24c79`（9360031 B）；网 PDF `9ded968023edde7aaff1cc153bb61f34471f9a18e667b31f646375884aaf6f1c`（1471934 B）。印 PDF 缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差 1 字节），以最终实测值为准。
- **text.md**：D5 不改文字内容；交付件为 port `.text.md.new` 原样沿用（BYTE-IDENTICAL，50552 B，sha256 `dc78fcc39c140c98ad299c3f49f67ade33ceb74cc86bca879728d12c476452f0`，570 条目 / 150 习题）；重建后重出 token-identical（rewrap RC=0）。本家 `issues/` 无已发 `.text.md`，基线以 port fanout 为准。
- **D5 门禁（17 门，run2b，全绿 ALL-GREEN）**：run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（1471934 B <7MB）；occlusion 0（含自检）；p8 extract 150/150；p8 compare CLEAN；freeze baseline 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 0；spill 0；boxtitle 0；edge 0/0；creambox PASS 0 缺陷（ratios n=568，中位 1.003）；文字层 print=web 多重集差 0；census_quotes 0 defective；家族 gates.py N/A；D18 刊头间距 62.0px。日志：`hidden_files/d5-redo/scratch-2026-w43-de/logs/2026-w43-de-pt/`（`GATES-SUMMARY.txt` 为总表）。D5 报告：`production/notes/2026-w43/g-de/scratch-d5-rebuild-de/D5-REPORT-2026-w43-de-pt.md`。
