# The Lucerna VOL.1 — EN × IT Edition Kit

**Pairing:** target language **English** (frozen VOL.1 core text) × reader native language **Italian**.
All explanations — glosses, grammar notes, instructions, exercise apparatus, and every P8 answer
note — are written in Italian. English target text, images, and layout geometry are frozen from
the core. Build directory: `hidden_files/weekly-report-en-it-build/` (copy of the core build).
The explanation-layer helper method in the code is named `expl()`; the intermediary-layer term
(in either language's form) occurs **0 times** in the paper, this kit, and the build code —
verified by grep over the final SVGs and all code files. Zero CJK characters in the final SVGs
(verified by Unicode scan of all 8 files).

## 1. Baseline proof (unmodified copy → shipped core SVGs)

Before any edit, the copied core build was run unmodified; all 8 output SVGs reproduced the
shipped core SVGs **byte-identically (sha256, 8/8)**:

| Page | sha256 |
|---|---|
| p1-front.svg | ad9904e3c910ba7e25792c74425b2b1b25dfdaab9353a4f70c1f5622cdba8467 |
| p2-life.svg | 684025c5a32287ab9c6f5628d1148a1037e1131a6c5974984c723d7b4e757720 |
| p3-culture.svg | f912664a8f65c038322788781afd6033d9c1b293185aee88b5ae5a49c10de67d |
| p4-sport.svg | 6059e3fbc1484e8f0daed69a8de61c37ed7ac5becdb015b7fffe908393a59d54 |
| p5-jeunesse.svg | 1f1b61ceae2176754ce50c16f4cd5ea4344cd89d290060ed110c4fa02efe622e |
| p6-politique.svg | 221066e3ffbd31ebc719099d7f1e2ded327f7cecc3a3f2f42a8018c6f5cea075 |
| p7-langue.svg | 74cae1c2e87a0a8f928aef0444359fd4c3d4f1d6a5638f41b517eb7ee1019d8a |
| p8-exercices.svg | 35c00e4961b91acbf739bc7faa0b148465bedab31c45bb27f6433d3242301763 |

## 2. Totals (identical to the frozen core)

- **149 exercises: A2 58 · B1 72 · B2 19**
- Per page: P1 10 · P2 17 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38
- Type counts (Italian names): Completare le frasi 39 · Scelta multipla 34 · Trasformazione 16 ·
  Abbinamento 12 · Vero o falso 8 · Completare il testo 8 · Pratica guidata 8 · Lettura del
  grafico 6 · Completare il dialogo 5 · Correzione 4 · Comprensione del testo 4 · Traduzione 4 ·
  Scrittura 1
- Registry diff vs core (n / page / level): identical for all 149 items. Build log: TOTAL 149,
  zero FLOW OVERFLOW and zero HEAD TOO WIDE warnings (six section heads shortened by wording
  only, see §4).

## 3. Key-diff registry (complete — the only registry changes)

Translation-type items re-aim at Italian, per the fan-out method. Exactly **3 keys** differ
from the core; the two re-aimed stems keep their English keys byte-identical.

| # | Core key | EN × IT key | Note |
|---|---|---|---|
| 136 | 投票不再是一天的事情，而是一个季节。 | «Votare non è più cosa di un solo giorno; è una stagione.» | stem stays English («Translate: …»); note: «no longer = non più» |
| 139 | 两家俱乐部都从未赢过世界大赛。 | «Nessuno dei due club ha mai vinto le World Series.» | stem stays English; note: «neither nega entrambi; has ever won, present perfect» |
| 149 | 开放题 — 要点见写作框，范文在第 8 版写作框内 | «(domanda aperta — il modello è nel riquadro di scrittura)» | writing apparatus; note: «si valuta in base ai punti» |

Re-aimed stems (keys unchanged, byte-identical English):

| # | Core stem | EN × IT stem | Key (unchanged) |
|---|---|---|---|
| 137 | 翻译：76 人队以 106 比 100 赢得了比赛。 | «Traduci: I 76ers hanno vinto per 106 a 100.» | The 76ers won the game 106–100. |
| 138 | 翻译：今年的提前投票在星期一开始。 | «Traduci: Quest'anno il voto anticipato è iniziato lunedì.» | This year, early voting opened on Monday. |

All other 146 keys are byte-identical to the core. All P8 answer notes are in Italian; the
printed-note set is identical to the core's (62 items), verified programmatically.

## 4. Italian furniture (verbatim, as shipped)

- Masthead: «The Lucerna» — exactly as the core ships.
- Tagline (46px serif bold, centred; measured width 1394px of 1820px available):
  «SETTIMANALE IN INGLESE · VOL.1 · STADI · VOTI · ZUCCHE»
- P1 badge (19.5px sans bold, brick slot, centred; measured 799px):
  «TESTI IN INGLESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI»
- Top strip centre (21px; measured 876.6px, clears both neighbours):
  «WEEKLY IN ENGLISH · UN NUMERO OGNI SETTIMANA · L'INGLESE CHE LEGGE L'AMERICA»
- Clock band: «L'EUROPA SPOSTA L'ORA DOMENICA» / «GLI USA L'1 NOVEMBRE (P. 7)»
- Footer left (16.5px; measured 722.6px): «The Lucerna · SETTIMANALE INGLESE VOL.1 · TESTI IN
  INGLESE · SPIEGAZIONI IN ITALIANO»
- Footer right: «Pagina N di 8»
- Gloss prefix: «Nota — » (replaces the core's gloss label everywhere)
- P8 keys block: title «ANSWERS · Risposte e note (pagine 1–8)»; page separators
  «— Pagina N —»; every note in the format ` (note)` — a space before the parenthesis,
  half-width parentheses only (core parity fix applied, as in the ES edition).
- Section heads shortened by wording only so each fits the 434px column at its drawn size
  (all other heads are the core's bilingual pattern): «A · TRUE OR FALSE ? · V o F»,
  «D · TRUE OR FALSE ? · V o F», «B · FESTIVAL WORDS · Le parole», «D · SENTENCES · Trasforma»,
  «C · COMPARATIVES · Comparativi», «D · SENTENCES · Completa» (P8).
- Box titles follow the same bilingual pattern, e.g. «THE WEEK IN NUMBERS · In cifre»,
  «DO THE MATHS · I conti», «THE TOOLBOX · Attrezzi», «THE ERROR CLINIC · Errori».

## 5. Builder's proofread (own pass, complete)

- Read all 8 pages end-to-end from the final SVGs; the full Italian layer checked for grammar,
  idiom, and consistency (terminology unified: voto anticipato, affluenza, distacco, scheda,
  adesivo, fila, portico, travestimento…).
- All 149 keys re-derived from the English text: 146 are byte-identical to the proofread core;
  the 5 translation-apparatus items (#136–139, #149) verified individually (§3).
- P7 phrases: verbatim contiguous excerpts with correct page tags — verified equal to the core
  under three independent counts (whole-issue occurrences, per-page occurrence
...[truncated 4498 chars]
---

## 6. Independent proofread — DONE · PASS (zero problems in the paper)

Independent proofreader, 2026-10-21 (EDT). One complete pass over the final rendered
artifacts; every builder claim re-verified from primary sources. No defects found in
the paper; no fixes were needed and nothing was re-rendered, so the builder's PDF
pins stand unchanged. Two documentation findings are recorded at the end.

**Baseline (independently reproduced).** A scratch copy of the unmodified core build,
run as a single-process driver (content12 → content34 → content56 → content7 →
content8, output redirected to scratch), reproduced all 8 shipped core SVGs
byte-identically (sha256 8/8), matching §1's table and the shipped files; build log
"TOTAL exercises: 149". The EN × IT build, copied and redirected the same way,
reproduces the 8 shipped EN × IT SVGs byte-identically (8/8) — the source diff below
is the edition's true diff. Core and edition SVG hashes re-verified unchanged after
all proofread work.

**Freeze.** Source diff (7 files): every changed core line is explanation layer
(contains CJK), pairing furniture, a documented registry item (§3), or one of the
infrastructure lines — 5 OUT paths, the `expl()` method rename (definition + call
sites), the P1 badge slot, the svglib docstring, the half-width note-parens print
format. Rendered-level check: per-page token multisets vs the core; every ASCII
token whose count decreased was located and adjudicated — all are the footer/strap
furniture, glosses that no longer repeat an English headword or number (P1 numbers
box, P2 time table, P3 patch gloss, P6 word gloss), the Chinese clock-band/teaser
digits, or the P8 band subtitle. No English target text changed anywhere.

**Totals.** 149 exercises: A2 58 · B1 72 · B2 19; per page 10/17/18/18/18/18/12/38;
type counts identical to the core under Italian names; numbering continuous 1–149
in the printed P8 (149 entries parsed sequentially).

**Keys.** Registry dumps compared field-by-field: page/level identical for all 149;
key diff = exactly {136, 139, 149}; stems re-aimed = {137, 138} with English keys
byte-identical. The same result holds for the PRINTED P8 keys (only parsing
artefacts at page separators apart from the three registry items). All 149 keys
re-derived against the stems and articles during a full read of all 8 pages; the
five apparatus items checked individually for faithfulness (136: «Votare non è più
cosa di un solo giorno; è una stagione.»; 139: «Nessuno dei due club ha mai vinto
le World Series.»; 149 apparatus + note; 137/138 Italian stems faithful to the
core stems, keys unchanged). The 9 registry notes identical to the core are all
language-neutral symbolic notes; zero CJK anywhere in the Italian registry.

**Printed-note set equality — PASS (decisive check).** Extracted from the shipped
P8 SVGs, the set of items printing a note is IDENTICAL in the core and in this
edition, 62 items each:
{11, 14, 15, 19, 35, 36, 40, 42, 49, 65, 74, 82, 83, 84, 85, 86, 87, 89, 101, 106,
108–149}. No drops, no extras; the Italian edition uses half-width parens only.

**P7 phrases.** All 8 phrases byte-identical to the core with the same page tags
(4, 2, 4, 4, 6, 6, 2, 2); whole-issue verbatim occurrence counts equal to the
core's for every phrase (1, 1, 1, 1, 5, 1, 1, 1 — the phrases are the issue's own
condensed form, inherited unchanged from the core).

**Calendar.** Every weekday/date claim verified against the real 2026 calendar
(`date`): Mon Oct 19, Tue Oct 20 (NBA), Wed Oct 14 & Oct 21 references, Thu Oct 22,
Fri Oct 23 (World Series G1), Sat Oct 24, Sun Oct 25 (EU clocks, F1), Fri Oct 30,
Sat Oct 31 (Halloween), Sun Nov 1 (US clocks), Tue Nov 3 (Election Day) — all
correct in the paper. Chart arithmetic re-checked: 34+27+23+16 = 100; #84 = 61%;
#86 = 18 points; P2 maths box 36/72/~75 consistent.

**Geometric occlusion audit (proofreader's own implementation).** Paint-order
parse, PIL real-font ink boxes (SC index), line boxes expanded by half stroke
width; classes COVER / LINEX / FOOTER (y > 2580, footer lines exempt) / EDGE
(frame 40..1910 and page) / TITLE (ink escaping its own box). Validated on a
synthetic positive control first: all 5 planted defect classes fired, and clean
text (underlined head, fitting boxed text, footer lines) stayed unflagged.
Real run on the edition: **1 flag total** — P1 LINEX, the word-of-week gloss line 2
vs the rule below it. Pixel adjudication on the shipped card: gloss dark ink ends
at row **1842**, the (light-gold) rule occupies rows **1843–1845**, zero dark
overlap → **non-defect**, the same adjudicated adjacency as the core (which flags
identically under this audit). Core comparison run: the core itself shows that
same P1 flag plus one P6 flag (its longer practice-data note reaching the chart's
top border) that this edition does NOT have, thanks to its shortened note.
Builder's four claimed fixes, each pixel-verified on the shipped cards:
(1) P1 gloss — as above, ink 1842 vs rule 1843 ✓;
(2) P2 sidebar — last Italian line's ink ends at row **1529**, box bottom edge at
1534.6, ≥5 clear rows ✓;
(3) P6 practice-data note — ink ends at x = **962** (pixels; 971 by font bbox),
chart edge at x = 989, clear ✓;
(4) P8 battery — last battery ink at rows **1457–1459** (pixels), above the 1485
strip limit and the writing box top at y = 1500 ✓.
No COVER, FOOTER, EDGE, or TITLE flags on any page. Inherited, non-defect: two
P8 matching-option lines ink to x = 1890/1899 — byte-identical widths in the
core, inside the frame, touching nothing (frozen English text).

**Images & credits.** Image payloads byte-identical to the core on every page
(4 images: P1, P2, P3, P6); printed credits match the placed images and the core
KIT table (Bain News Service / Library of Congress; Social Security Administration;
Halloween postcard 1912; United States Capitol — all public domain).

**Furniture.** Badge verbatim on P1; pairing footer-left and «Pagina N di 8»
present on all 8 pages (verified programmatically); gloss prefix «Nota — »
throughout; masthead «The Lucerna» as the core ships.

**PDFs (measured by the proofreader).** Web: **4,498,209 B**, sha256
`d941d47867d06cffd1bf951452f3b4168a100ff9eeaa316b9c04171dbe0b5347` (< 10 MB),
8 pages. Print: **8,615,022 B**, sha256
`e1b2f240087239a91bcdd08dcfd4ef5b69126f6c60adac55120c1d150ae9a103`, 8 pages.

**D5 rebuild (2026-11-13, see §7 below).** Print `The-Lucerna-VOL1-en-it.pdf` **7,493,650 B**,
sha256 `d54137e00e209de5bdc1cbc1eb4aa46c8025de56c8c184af3b37636363ce592e`; web
`2026-w43-en-it.web.pdf` **1,063,082 B**, sha256
`6416281b07a3362325c86e1a4fa4206a1b9578815923b0fb880e3b0504180d0a` (< 7 MB);
text.md byte-identical to the shipped version (sha256 `dbc0c91d…`). Pre-D5 values:
print 8,615,022 B, web 1,103,724 B (`32aaebd8…`, shipped in issues/).

**Terminology scan.** The intermediary-layer term: **0 occurrences** in the paper
(SVGs, cards, PDFs), in this KIT, and in the operative build sources
(content12/34/56/7/8.py, svglib.py, bslib4.py). Zero CJK in all 8 SVGs.

**Documentation findings (paper unaffected).**
(a) This KIT file itself was truncated during the builder's write: §5 ends
mid-sentence and the file carried a baked-in truncation marker; the builder's
§6+ (audit detail, PDF pins, PENDING marker) never landed. This record supplies
the verified facts; the PENDING state is hereby replaced by DONE · PASS.
(b) The terminology scan found 10 occurrences of the banned term, all confined to
the builder's one-off scratch transform scripts
(`hidden_files/weekly-report-en-it-build/scratch/fix12.py` ×4, `fix34.py` ×2,
`fix56.py` ×1, `fix7.py` ×2, `fix8.py` ×1) — specifically the search-string side
of the rename tuples, which quote the frozen core's original method calls in
order to replace them. The builder's §0 claim of a grep over "all code files" is
imprecise in that corner. The paper, this KIT, and the operative build sources
are clean; adjudicated a builder-hygiene note, not an edition defect.

Proofreader scratch (audit script, control SVG, text dumps, rebuilds, flag logs):
`hidden_files/proof-enit-independent/`.

## 7. D5 rebuild (2026-11-13, D5-only)

SOP §1.1 font fix: the explanation layer's Latin letters move from Noto Sans CJK to Newsreader (SemiBold). No commit, no push — insertion is done by the closer after an independent re-proof. Work log: `hidden_files/d5-redo/scratch-2026-w43-en/logs/2026-w43-en-it/`; per-edition report: `production/notes/2026-w43/g-en/scratch-d5-rebuild-en/D5-REPORT-2026-w43-en-it.md`.

**Install**: core landed with `apply_variant.py --patch-core en --week 2026-w43` (core-en `svglib.py` +95/−3, `_D5_READER = "latin"`); this edition installed with `--svglib patched/…/svglib.py --target en --reader it --week 2026-w43`, `_D5_READER = "latin"` (installed svglib md5 identical across de/it/nl/pt); routing unit test FAILURES: 0 (66 PASS); fix2 block kept.

**Baseline** (pre-fix production build): run TOTAL 149, 0 warnings; print PDF vs `MANIFEST-W43-D1.md` −79 B (metadata float, one of the 4); print/web text layers differ by 0 chars; self-built web vs shipped web differ by 0 non-space chars (spaces only); pre-fix census D5 Latin 550, Cyrillic 0, curly in CJK 1; baseline P8 noted 62/149 (core口径).

**Defects and fixes** (run1: 6 items, all D5 widening except the pre-existing P2 spill, which the baseline shares; sizes only, no wording changed):

- heads ×2: P4 `C　COMPARATIVES　Comparativi` 25→23 (24 still 3.7 px over); P5 `EARNINGS, IN PLAIN ENGLISH` 26→25 (column width 422.5).
- occlusion ×1 (P1): band headline vs subtitle `SPOSTA L'ORA` overlapped 55.5×20.8 px → headline 46→**44** (the family's narrowest subtitle at 27 pt, left edge x=1649.0 — 44 already clears, no need for 42).
- creambox/boxtitle ×2: P1 `THE WEEK IN NUMBERS　In cifre` +3.5 px → `tsize=22`; P1 `IN THIS ISSUE　In questo numero` (contents-box header, a bare `p.text` at 24 pt, not a `box()` title) +11.1 px → 24→**22**.
- spill ×1: P2 `Check your number !` below the DID YOU KNOW box by 12.71 px → box-height formula tail +14→+34 (box bottom +20 px; same pre-existing defect as core-en).

P8: 193→189 lines, footer slack 32.7→52.8 px.

**Gates run2 (all 17 ALL-GREEN)**: run TOTAL 149, 0 warnings; head_check 0; d5 census 0/0/0; render RC=0; webpdf RC=0 (1,063,082 B < 7 MB); occlusion 0 flags; p8 extract noted 62/149; p8 compare **CLEAN** (keydiff=[136, 139, 149], the registered reader-language keys); freeze baseline 8/8; freeze diff added CJK chars 0; spill 0; boxtitle 0 DEFECT (57 titles); edge 0/0; creambox PASS 0 defects; text layer print=web diff 0; census_quotes 0 defective; no family gates.py for en.

**New deliverables**: print `The-Lucerna-VOL1-en-it.pdf` 7,493,650 B (`d54137e0…`); web `2026-w43-en-it.web.pdf` 1,063,082 B (`6416281b…`); text.md byte-identical (`dbc0c91d…`). Still 149 exercises.
