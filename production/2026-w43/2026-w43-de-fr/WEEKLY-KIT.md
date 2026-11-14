# Die Lucerna — VOL.1 — DE × FR (allemand + explications en français)

**Pairing:** German text · French explanations, for French-speaking readers.
**Week:** Mon 2026-10-19 → Sun 2026-10-25 (W43). **Masthead:** Die Lucerna.
**P1 badge (brick red):** TEXTE EN ALLEMAND · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES (replaces the core tagline line, same position as the DE×EN sibling).
**Footers (all 8 pages):** „Die Lucerna · HEBDOMADAIRE ALLEMAND VOL.1 · TEXTE EN ALLEMAND · EXPLICATIONS EN FRANÇAIS" / „Page N sur 8".
**P1 edition line:** „JOURNAL ALLEMAND · VOL.1 · HORLOGES · VACANCES · GELÉE" (measured fit at 46pt; the literal „HEBDOMADAIRE…" variant measured 1932.7px > 1820 and was not used).

## Production method
Fan-out from the frozen, patched DE core, same pattern as DE×EN: the core build (`hidden_files/weekly-report-de-build/`, post P6/P7 patch) was copied to `hidden_files/weekly-report-de-fr-build/` and ONLY the explanation layer was rewritten into full French — every gloss, grammar note, instruction, section-header gloss, chart note, P7 clinic note, readers'-corner note and all P8 answer notes. Baseline first: the unmodified copy reproduced all 8 shipped core SVGs **byte-identical**, registry identical (150). The core's patched geometry (P6 pro/contra box, P7 toolbox) is retained unchanged. The layout helper method inherited from the core was renamed in this copy so the banned intermediary term appears nowhere — paper, KIT, code (verified: 0 hits in build sources, SVGs, this KIT).

## Totals
- **150 exercises** — A2 67 · B1 69 · B2 14; per page 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38. Identical to the core (registry compared programmatically: page and level of every item identical).
- Rendered text volume: 48,108 chars (core: 40,036) — the French apparatus is complete, not a condensed gloss layer.
- CJK in final SVGs: **0**.

## Freeze verification (German text byte-identical)
- Transform-pair audit: all 306 replacement pairs were enumerated; only **3** have old strings without CJK — (1) the layout-method rename, (2) the P1 tagline line → badge line (task-prescribed), (3) the P8 note join „（note）" → „ (note)" (space before, half-width parens, per house style). Every other replaced string belonged to the Chinese explanation layer.
- Registry diff vs core: keys byte-identical except the documented items below. Notes differ throughout (French), except language-neutral notes that are identical by design (e.g. „trennbar: um-ge-stellt", „haben → gehabt", „46 + 18 = 64").
- Token bag check per page: all German-token deficits adjudicated to furniture/apparatus (footers, tagline→badge, gloss lines, note-layer numerals, tokenizer punctuation artifacts); two flagged spots were closed out by direct grep (P7: all German *weil* example sentences present; P1: Fragen box German body line intact, its bilingual title line restructured — see shortenings).
- P7 phrases of the week: all 8 German quotes verified **byte-verbatim, exactly 2× each** (source article + P7), page tags correct (Seite 1 · A2; Seite 2 · A2 ×2; Seite 3 · B1; Seite 4 · B1; Seite 5 · B1; Seite 6 · B2 ×2).
- Images: `<image>` elements byte-identical to the core on every page; credit lines identical (German).
- Facts identical: „Eine Stunde geschenkt", Zeitumstellung Sun Oct 25, 03:00→02:00, 25-hour night, 410:192, 84 %, 4.6 M responses, STIKO facts — all carried over unchanged.
- Re-solve spot check: **41 items** re-solved against the French notes across all pages (incl. all translation items); zero contradictions.

## Key diffs vs core (documented reader-language items only)
- **#137** (DE→FR): key is now French — „La nuit compte 25 heures." (note: „Stunden = heures"); body no longer carries the translate-into-Chinese marker; instr „Traduire en français".
- **#138** (DE→FR): key „Je règle l'horloge le samedi soir." (note: „umstellen = régler (une horloge)"); instr „Traduire en français".
- **#139/#140** (FR→DE): prompts are now French („Le dimanche, je dors une heure de plus." / „On peut emprunter des livres à la bibliothèque."); the German keys are byte-identical to the core; instr „Traduire en allemand".
- **#150** (writing): registry key is a French apparatus line („Tâche ouverte — suivez les points du cadre d'écriture ; le texte modèle est dans le cadre de cette page"); the German writing task and the 87-word model text are unchanged.

## Documented fit shortenings (French apparatus only; German never touched)
House-style bilingual heads were measured and shortened where the full form overflowed; the compressions below were forced by fixed core geometry and are recorded here:
- P1 hero gloss condensed (drops the repeated „die/der" articles; all five glosses kept).
- P1 Zahlen box parentheticals: „(25 heures)", „(11 Länder en vacances)", „(plus de 8 000)" (the German lines carry the full facts).
- P1 headline-strip gloss → „L'heure recule dimanche" (the longer „On recule les horloges dimanche" grazed the German headline's ink).
- P1 Fragen box: the core's bilingual title line was restructured to the box's German title (FRAGEN DER WOCHE) + „Les questions des guides allemands"; closing line „Les guides y répondent dans tout le pays." kept.
- P2 UND SIE translation drops „à la maison" (the German above carries „zu Hause") so it fits 3 lines above the section rule.
- P6 health summary compressed to „Grippe : la STIKO recommande le vaccin aux plus de 60 ans, femmes enceintes dès le 2e trimestre, malades chroniques et soignants ; protection en 10 à 14 jours." — **all** facts of the core summary kept (60+, pregnancy from 2nd trimester, chronically ill, care staff, protection in 10–14 days).
- P6 exercise prompts shortened („D'après le graphique : choisissez."; „Lisez l'article page 6 et répondez."); two P6 notes compressed („pas d'accord entre les États membres"; „deux fois par an") — no fact lost.
- P5 Samstag-Plan box title → „DER SAMSTAG-PLAN DER REDAKTION · Le programme du samedi" (found by the independent proofreader, see below: the full form's ink measured 1039.9px against the box's right edge at 961 — „de la rédaction" is already carried by the German half „DER REDAKTION"; shortened title ink ends at 858.4).
- P7 toolbox title „DER WERKZEUGKASTEN · Outils" and readers' title „LESERBRIEFE · Vos lettres" (full forms measured too wide); toolbox entries: „Von O bis O" gloss tail „(l'astuce des pneus)" dropped (the mnemonic is explained in full on P2), „Ich finde, dass …" gloss tail „(verbe à la fin)" dropped (the dass verb-final rule is stated in the B2 lesson note), „Meiner Meinung nach" entry printed without ellipses; readers' note „vos lettres" for „de vraies lettres de lecteurs" (VOL.2 promise — letters + best page-8 texts — intact); word-box French tail → „Le classique allemand."
- P7 phrase translations: #3 in nominal style („Citrouille sculptée déposée du 26 au 29 octobre : billet enfant gratuit pour le 31." — all facts kept); #8 drops „gouvernements" („les États membres ne se sont pas mis d'accord" — same fact).
- P8 section heads measured and shortened: „C · LESEVERSTEHEN · Lecture", „F · WÖRTER PAAREN · Les paires".
- P8 answer keys set at 13pt (core: 14.5pt) following the DE×EN sibling — French notes are longer; keys flow ends y=2377 of 2560.

## Geometric audit (SOP addendum + thin-line supplement)
Builder ran the paint-order audit with real-font metrics and **stroke-expanded line boxes** (`audit_de_fr.py` in the build dir) plus a supplementary text–text overlap scan (`audit_texttext.py`). Defects found and fixed during production (all in the French layer / its fit, core geometry untouched):
1. P1: Zahlen box jumped a column (French parentheticals) → shortened; box back in column 1, exercises end y=1585/1828.
2. P1: headline-strip French gloss grazed the German headline → gloss shortened (see above).
3. P2: UND SIE French 4th line struck by the y=1554 section rule → translation shortened to 3 lines.
4. P6: health summary's 5th line struck by the y=1408 chart rule → summary compressed; box now ends y=1400.
5. P7: right rail grew +87px over the core (French toolbox/readers lines) pushing the word box across the phrases rule and its text into phrase 4 → toolbox/readers/word-box shortenings; rail now ends y=1484.0 (core: 1485.5).
6. P7: phrase 3's tag overprinted phrase 7's quote and phrase 8's tag was struck by the clinic rule (y=1968) → both French translations shortened one line; tags now clear.
**Final state: standard audit 0 flags on all 8 pages; text–text scan reports only the P1 masthead pair (wordmark vs edition line), a model artifact of the 248pt ink band — visually adjudicated non-defect („Die Lucerna" has no descenders; real gap ≈36px; identical geometry to the shipped core). All 8 final cards were viewed.**
Durable lesson recorded for future fan-outs: in-build line counts for Latin text can exceed svglib `wrap()` predictions (text renders in Noto Sans CJK) — geometry was therefore always verified on the rendered SVGs/cards, never on wrap predictions alone.

## Files
- `svg/` — 8 final SVGs (1950×2700).
- `cards/` — 8 page PNGs, 1950×2700.
- `The-Lucerna-VOL1-de-fr.pdf` — print PDF, 9,355,922 B, sha256 `16a4aa601567f59fb136261c20712f35949d7338d85b8a3fc14b4aa6e602e84c` (D5 重建，2026-11-13；旧配方值 10,481,150 B 已过期，见末节 D5 记录）。
- `2026-w43-de-fr.web.pdf` — web PDF, 1,467,837 B (< 7 MB), sha256 `b19a47c70f8c7facc86814a2f401c0820f74b72b8562c8054ee876d03e89e4b5` (D5 重建，2026-11-13；旧配方值 4,282,934 B 已过期，见末节 D5 记录）。
- Build: `hidden_files/weekly-report-de-fr-build/` (content12/34/56/7/8.py, bslib4.py, svglib.py, run.py, render.py, audit_de_fr.py, audit_texttext.py).

## Independent proofread (2026-10-21, fresh proofreader — PASS after 1 fix)
Full pass per SOP §8 + geometric-audit addendum, all in the rendered artifacts:
- Registry rebuilt from both builds and compared: 150 items, n/page/level/type identical; **key diffs vs core exactly {#137, #138, #150}**; #139/#140 keys byte-identical. All 150 exercises independently re-solved against the articles/chart — **zero contradictions**; all 150 printed P8 keys match the registry verbatim. Model text word count verified: 87 mots (task range 80–100).
- German freeze: code diff core↔FR touches only CJK/full-width-punctuation lines plus the prescribed furniture (tagline→badge, footers, note prefix, method rename, P8 key size 14.5→13); SVG text-multiset diff leaves exactly 18 changed non-CJK core strings, all adjudicated (tagline, CJK punctuation, P8 paren-join flow). Rebuilt SVGs from both builds byte-identical to the shipped ones (pre-fix).
- Apparatus fully French: CJK = 0 in all SVGs; no German/English explanation leftovers (179 distinct grey apparatus strings scanned; the only English is the USFWS proper noun inside the German photo credit, core-identical). The 15 notes identical to the core are all language-neutral (German forms, arithmetic).
- Badge exact (brick #a4553a), footers exact on all 8 pages, P7 phrases verified programmatically: 8/8 verbatim in their tagged pages, exactly 2 occurrences each, tags correct.
- **Geometric audit (proofreader's own implementation, PIL metrics, stroke-expanded line boxes, synthetic positive/negative controls PASS): 0 flags on all 8 pages** (coverage ≥30%, line strikes, footer band, page edge). Text–text scan: only the two known model artifacts (P1 wordmark/edition line; band wordmark/sub-line on P2–P8), both pixel-adjudicated non-defects (real ink gaps 30px and 12px). The builder's 6 in-build fixes were re-checked in the renders (P1 Zahlen box + headline gloss, P2 UND SIE 3 lines clear of the y=1554 rule, P6 health summary clear of the y=1408 rule, P7 rail + phrase tags) — all confirmed.
- **Defect found & fixed: P5 Samstag-Plan box title overflowed its box** (ink right 1039.9 vs box right edge 961; a text-vs-own-box fit case the coverage/line audits cannot see). French title segment shortened (see shortenings list), rebuild + re-render via the canonical recipe (cards reproduced byte-identical pre-fix as a chain control), then the **complete pass was re-run from the top: zero problems**. Only p5-jugend.svg changed; P5 joined text differs from pre-fix solely in the title.
- Core integrity: `node lint.mjs --require-pdf` in weekly-git GREEN; core web PDF in `files/weekly-report-de-vol1/` = 3,393,401 B, sha256 `db3d4451…` — identical to the repo pin; core SVGs byte-identical to a fresh core-build run (the builder's in-place re-render changed nothing).
- One wording correction in this KIT itself: an English noun in the P6 shortening entry was reworded so the banned intermediary term now appears nowhere in paper, KIT, or code (grep-verified 0 hits).

## Status
**FINAL — independent proofread gate PASSED (zero problems after the fix + full re-pass).** Ready for repo insert + Discord delivery by the parent.
## D5 重建记录（2026-11-13，W43/W45/W46 D5+§1.1 合并重修 Phase 1）

- **原因**：D5 缺陷——sans 层拉丁/西里尔字符落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者）。本版修前 census：D5 拉丁 671、西里尔 0、弯引号 CJK 0。
- **安装**：`tools/mechanism-w47/apply_variant.py --svglib <版>/svglib.py --target de --reader fr --week 2026-w43`（先 `--check` dry-run 通过）。`_D5_READER = "latin"`。路由单元测试 `test_d5_routing.py` FAILURES: 0。fix2（U+201C/U+201D/U+2019 → serif）保留：本版弯引号 33 个全在 Newsreader。
- **基线**：重建前先证基线干净——`run.py` TOTAL 150、0 警告；重建 SVG 8/8 与 port fanout 逐字节相同；印 PDF 与 fanout BYTE-IDENTICAL。基线实测（§1.1 组装版）：印 PDF `d8bb34c5a03aff349664cf3096c5673fc94d56134acabc6f03aac39c2549e321`（9947678 B）、网 PDF `0b0cf0b0248633f7325c17915ddcb44e3a90672c294ea469a3573822fa8d041f`（1555746 B）。本 KIT 上方旧值（更旧配方）已过期，以上两值为准。
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
- **P8**：行数 228→234，距页脚线余量 33.3px；p8 compare CLEAN（keydiff [137, 138, 150]）。
- **新交付物（D5 重建，2026-11-13）**：印 PDF `16a4aa601567f59fb136261c20712f35949d7338d85b8a3fc14b4aa6e602e84c`（9355922 B）；网 PDF `b19a47c70f8c7facc86814a2f401c0820f74b72b8562c8054ee876d03e89e4b5`（1467837 B）。印 PDF 缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差 1 字节），以最终实测值为准。
- **text.md**：D5 不改文字内容；交付件为 port `.text.md.new` 原样沿用（BYTE-IDENTICAL，51360 B，sha256 `57150d35da79970693cfda0d48a076e11c9b09dcb7f316b5cbd0da9396a31361`，570 条目 / 150 习题）；重建后重出 token-identical（rewrap RC=0）。本家 `issues/` 无已发 `.text.md`，基线以 port fanout 为准。
- **D5 门禁（17 门，run2b，全绿 ALL-GREEN）**：run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（1467837 B <7MB）；occlusion 0（含自检）；p8 extract 150/150；p8 compare CLEAN；freeze baseline 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 0；spill 0；boxtitle 0；edge 0/0；creambox PASS 0 缺陷（ratios n=576，中位 1.004）；文字层 print=web 多重集差 0；census_quotes 0 defective；家族 gates.py N/A；D18 刊头间距 67.3px。日志：`hidden_files/d5-redo/scratch-2026-w43-de/logs/2026-w43-de-fr/`（`GATES-SUMMARY.txt` 为总表）。D5 报告：`production/notes/2026-w43/g-de/scratch-d5-rebuild-de/D5-REPORT-2026-w43-de-fr.md`。
