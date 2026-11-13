# WEEKLY-KIT — 2026-W47 · German edition for Portuguese-speaking readers

- Edition: `2026-w47-de-pt` — German target text, Portuguese explanations
- Week: Mon 2026-11-16 – Sun 2026-11-22 · VOL.4 · Press time: Mon 2026-11-09
- Lead story: **Die Bundesliga kehrt zurück — Bayern gegen Köln** (40 chars, limit 56)
- Status: fan-out complete, all self-check gates green, visual proofread 8/8 pages
  zero findings (rebuild 3, 2026-11-11; core build15); independent proofread
  (proof2) zero findings except the P7 toolbox clearance it never measured —
  fixed in rebuild 4 (2026-11-11, toolbox clearance +20.0, all gates green;
  see §5). Independent proofread to be re-assigned by the coordinator.
  New standing gates (2026-11-12) found 1 boxtitle defect (P1 ZAHLEN title
  +15.5px); rebuild 5 (2026-11-12) repaired it by layout only, all gates
  green again.
- **D5 font rebuild applied 2026-11-12 (rebuild 6, all gates green — see §7)**
- Source: `core-de/` (2026-w47-de-zh-cn, build15) copied and translated in the
  explanation layer only. German target text is frozen — see §6 for the proof.
- Builder: de fan-out builder, 5th shift (2026-11-11). Scratch:
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-de/`
  (`tr_pt.py`, `transform.py`, `build_edition.py`, `pt/` gate logs).

## §1 Contents

8 pages, 1950×2700, 4 columns. **150 exercises**, continuous numbering 1–150, all in
the registry. Identical layout and exercise set to the core; only the explanation
layer (bridges, instructions, glosses, notes, toolbox, disclosure, keys notes) is Portuguese.

| Page | Section | Level | Ex. |
|---|---|---|---|
| P1 | Front: lead + Fragen der Woche + sumário + word of the week + Blitzquiz | A2 | 10 |
| P2 | Leben: Buß- und Bettag & Alltag + Rechnen | A2 | 18 |
| P3 | Kultur: Weihnachtsmärkte & stille Woche (1930 painting) | A2→B1 | 18 |
| P4 | Sport: results 3–8 Nov + fixtures table + MD10 return | B1 | 18 |
| P5 | Jugend: Adventskalender basteln + Wochenplan (1903 calendar) | B1 | 18 |
| P6 | Vertiefung: stille Woche & Haushalt 2027 + practice chart | B2 | 18 |
| P7 | Sprache: A2/B1/B2 lessons + Sätze der Woche + Fehlerklinik + Leserbriefe + VOL.5 teaser | A2/B1/B2 | 12 |
| P8 | Schlusstest + Schreiben (MUSTER 84 words) + all answers | mixed | 38 |

Levels: A2 69 / B1 67 / B2 14. Types: escolha múltipla 52 / completar 41 /
transformação 11 / verdadeiro ou falso 8 / texto com lacunas 8 / construir frases 8 /
associar palavras 12 / tradução 4 / completar o diálogo 5 / escrita 1.

Pairing furniture (VOL.4): masthead `Die Lucerna`; edition line
`SEMANAL ALEMÃO　VOL.4　VOLTA A BUNDESLIGA　SEMANA TRANQUILA`; footer
`Die Lucerna　SEMANAL ALEMÃO VOL.4　Texto alemão　Explicações em português`;
page line `Página N de 8`; gloss prefix `Nota — `.

## §2 Trend / fact sources

Frozen from the core — see `core-de/WEEKLY-KIT.md` §2 (Bundesliga MD9 3–8 Nov,
UCL/UEL MD4, Nations League, Serbia–Germany 13 Nov with the UEFA spectator-ban
exemption — ~5,000 expected, NOT zero spectators — MD10 20–22 Nov, Buß- und Bettag
18 Nov, Totensonntag 22 Nov, 1st Advent 29 Nov, Cologne Christmas markets 16 Nov–23 Dec).
No fact was changed, no trend research re-done, no answer key changed.

## §3 W46 promises / reader letters

- Same as the core (see `core-de/WEEKLY-KIT.md` §3/§9): W46 promises honoured
  (Bundesliga return, European matchdays 24–26 Nov, Buß- und Bettag, Totensonntag,
  3–8 Nov results); VOL.5 promises (first Advent 29 Nov, Europe results, MD11,
  markets in full swing, real reader letters).
- No real reader letters by press time. Per the F-MAIL rule (only letters the user
  sends directly count; none arrived, no mailbox checked, nothing invented), P7
  carries the labelled editor's example + the Portuguese disclosure:
  "Exemplo da redação: nenhuma carta real chegou antes do fecho. Envia os teus
  textos para o VOL.5!"

## §4 Images

Identical to the core (see `core-de/WEEKLY-KIT.md` §4 and `assets/CREDITS.md`):
fussball.jpg (P1), kopfball.jpg (P4), weihnachtsmarkt1930.jpg — Wilhelm Ritter 1930
(P3), christkind.jpg — Richard Ernst Kepler 1903 (P5), lesesaal.jpg — Carol M.
Highsmith, Library of Congress (P7), fussball1905.jpg (P8). All public domain, each
with target-language caption + printed credit.

## §5 Build / reproduction

- Build dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-de-pt/`
  (build code + deliverables, copied from `core-de/` by `transform.py pt`).
- Reproduce: `tools/venv/bin/python transform.py pt` (from scratch-fanout-de) →
  `tools/venv/bin/python measure.py pt <edition-dir>` →
  `tools/venv/bin/python build_edition.py pt` (run.py → render.py → webpdf →
  verify → occlusion → p8 → freeze → pdftotext → chips → export).
  Build interpreter is `tools/venv/bin/python` (PIL 13.0.0); freeze was re-run with
  the same interpreter (system python3 has PIL 10.2.0 and measures 1.1% differently).
- Deliverables (fix-de-round3 rebuild, 2026-11-13; reproof fix rebuild, 2026-11-12 superseded):
  - Print PDF: `Die-Lucerna-VOL4-de-pt.pdf` — 10,354,731 bytes, 8 pages,
    sha256 `23c1505097e1d8a36fb4126c3479bebff44bd054e04b5bb40f031f7ced00c740`
  - Web PDF: `Die-Lucerna-VOL4-de-pt-web.pdf` — 1,514,736 bytes (< 7 MB),
    50,895 text bytes,
    sha256 `bda89b7b21802e0faa789c05aba2215d9ebb4379ec461257790531f7b8fb3589`
  - Text export: `2026-w47-de-pt.text.md` — 50,158 bytes, 48,292 chars,
    591 entries, 150 exercises,
    sha256 `b1b6a7e20abd04a0adfa3d979920919749d3280bd128b9775003e31a330597ca`
    (changed — wording fixed per the §7 reproof fix entry; re-exported from the fixed sources)
    (exported from production sources in reading order, never from PDF;
    **byte-identical to the pre-fix export** — the fix moved geometry only)
  - `ABSTRACT.txt` (one line, Portuguese, no ASCII double quotes):
    "Die Lucerna Semanal alemão VOL.4: volta a Bundesliga (o Bayern recebe o
    Colónia), decisiva da Nations League contra os Países Baixos, dia de
    arrependimento e oração e domingo dos mortos, abertura dos mercados de Natal
    de Colónia, resultados europeus e da Bundesliga de 3 a 8 de novembro; texto
    em alemão, explicações em português, níveis A2–B2, 150 exercícios sobre os
    temas da semana."

## §6 Gates (rebuild 4, 2026-11-11 — toolbox fix; rebuild 3 values unchanged unless noted)

- `run.py` (build.log): exit 0, **zero FLOW OVERFLOW / HEAD TOO WIDE**, TOTAL 150.
  Flow ends: P1-headline 1554 (= core), P1-fussball 2264, P1-quiz 2523,
  P2-feature 993, P2-ex 2332, P3-main 916, P3-ex 2333, P4-main 677, P4-ex 2315,
  P5-main 1026, P5-ex 2441 (= core), P6-main 777, P6-ex 2523, P7-A2 1278 / B1 1342 /
  B2 1306, P8-battery 1409, P8-keys 2457 (bottom 2560, spare 103px).
- `measure.py`: **24/24 PASS, 0 FAIL** (measure2.log).
- `verify.py`: TOTAL 150; numbering continuous 1–150; SVGs byte-identical after
  re-run; SOP 1.1 style audit True; verbatim OK; P8 answers floor (≥ 9.75pt) True;
  all 17 forbidden terms absent.
- `tools/occlusion_audit.py`: **0 flags** (selftest OK: all 6 planted classes fired,
  clean controls silent).
- `tools/p8.py`: extract 150/150; compare vs core: `status: CLEAN missing=[]
  extra_count=0 keydiff=[137, 138, 139, 150]` — the 4 expected items only
  (137–139 forward translations, 150 open writing task; Q140 is the reverse
  item, its key IS the German target sentence, so it correctly does NOT diff).
- `tools/freeze.py` diff: exit 0; TOTAL added CJK characters 7, all U+3000
  (full-width space, the SOP §1.1 furniture separator), 1 per page on P2–P8, 0 on P1.
  **Direct freeze proof (8/8, `pt/freeze-direct.json`, script `freeze_direct.py`):**
  (a) source-level: AST string-literal multiset core vs edition — 0 unaccounted
  removed, 0 unaccounted added (520 removed / 528 added, every one accounted for
  by the translation module, the CJK inventory, or a documented transform artifact);
  (b) rendered-text level: the frozen intersection (strings identical in core and
  edition SVGs) per page — P1 147, P2 163, P3 195, P4 166, P5 173, P6 175, P7 150,
  P8 186 strings, sha256 083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 /
  2bbe05f9 / b7aa0771 / 57e118e7 — identical to de-en, de-fr, de-es and de-it, as the
  frozen content is the shared German text.
- Print/web text layer: `pdftotext` default mode — print 50,684B / web 50,684B,
  **word multiset identical**; `-raw` mode — both 49,500B, normalised text
  **exactly identical**. Web PDF has a real text layer.
- Level chips (rx="2.7" rects): per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18,
  7:12, 8:35}, **TOTAL 141**; P8 by level A2 22 / B1 13 / B2 0. The core's
  missing-14 set is fully present: cloze options Q113–120 (8 A2 chips),
  dialogue badges Q145–149 (145–147 A2, 148 B1, 149 A2), writing title chip
  (B1 on "H SCHREIBEN").
- P8 answers measured font size: keys 13.25 SVG units = **9.94 PDF pt**
  (PyMuPDF re-measured P8 minimum span 9.94pt) — above the 9.75pt floor
  (concession step 4; P8 stems stay at the core's 15.375pt).
- 150-question key check (independent, `pt/keycheck-150.json`, script
  `keycheck.py`): P8-SVG-extracted keys vs the REG built from the edition's own
  sources — **149/150 exact**; the single non-exact item is Q150, the open
  writing task, where the extractor truncates the REG key "Tarefa livre — segue
  os pontos do quadro de escrita" to "Tarefa livre" (expected; Q150 is already
  in the keydiff set). REG by page
  {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}; levels A2 69 / B1 67 / B2 14.
- U+2019 scan over the 8 SVGs: **0** (straight U+0027 throughout, as `\u0027`
  escapes in `tr_pt.py`).
- Visual proofread: all 8 pages re-rendered from the print PDF at 100 dpi and
  viewed one by one (P1–P8), plus a systematic SVG-level scan of the 7 col3
  box titles (8 instances incl. the P6 full-width box): all end ≤ 1862.0
  (max 1849.6, NOCH EIN WORT, 12.4px margin). **Zero findings** (see §7). The P8
  keys were spot-checked against the registry (dates, scores, times, grammar keys,
  MUSTER 84 words, chart 44+33+23=100).

## §6b Gates (D5 font rebuild round, rebuild 6, 2026-11-12 — full re-run on the rebuilt edition; scratch `hidden_files/w47/scratch-d5-de/de-pt/`)

- D5 mechanism: `apply_variant.py --svglib … --target de --reader pt` (mode latin) on the edition's `svglib.py`; fix2 curly-quote routing installed with it (routing assert `ROUTING FAILURES: 0`). Pre-D5 `svglib.py` backed up as `svglib.py.pre-d5`. Pre-D5 baseline verified CLEAN before install: the production dir was copied to scratch and rebuilt with the venv interpreter — freeze baseline **8/8 SVGs byte-identical** to the delivered SVGs (`freeze-pre-baseline.log`). Pre-D5 production snapshot in `scratch-d5-de/de-pt/baseline/` (SVGs + sources, rebuild-5 state). KIT wave 2 check: pre-D5 print SHA matches the KIT (`bfdc6e8f…`), but the pre-D5 web PDF on disk was sha `e723f2cb…` (1,602,460 B), NOT the §5 rebuild-5 record `e48265d3…` — the rebuild-5 web PDF had been rebuilt without a §5 sync (same class as de-en/de-fr/de-it/de-nl; the §7 Rebuild 5 section does record the correct `e723f2cb…`). The D5 values above are measured from the actual files on disk.
- Pre-D5 D5 census: **631 Latin-in-CJK-Sans elements** (matches D5-CENSUS-130); quotes defective 0; p8 extract 150/150.
- `run.py` (run2): TOTAL **150**, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`tools/head_check.py`: PASS 0 defects).
- `mechanism/d5_census.py`: **PASS — D5 Latin 0, D5 Cyrillic 0, curly-in-CJK 0**.
- `tools/occlusion_audit.py`: **0 flags** (selftest OK; fixed tool — bare `Noto Sans` runs measured on the non-CJK face, brief §10).
- `tools/p8.py`: extract 150/150; compare vs rebuilt core-de P8: `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]` — the same 4 expected reader-language items as rebuild 4.
- `tools/freeze.py`: baseline **8/8 SVGs byte-identical** (venv Pillow 13.0.0 / FreeType 2.14.3); diff pre-D5 baseline vs rebuilt: **added CJK characters 0** (added Latin strings 371 = D5 run-splitting).
- `tools/spill_sweep.py`: 32 boxes, 85 candidates, **0 SPILL**, 85 OBSERVE.
- `tools/boxtitle_check.py`: 42 titles, 250 body lines, **0 DEFECT**, 0 OBSERVE, 0 marginal (real backup comparison: `scratch-d5-de/scratch-fanout-de/backup/2026-w47-de-pt`). Coverage note: three fixed titles sit below the tool's 22pt detection floor (P1 box 20pt, P7 Material 21pt, P7 Mais uma palavra 21pt) — they are verified instead by the creambox audit (0 defects across all 32 boxes) and by direct ink measurement (spare 6.9px / 7.5px / 7.5px).
- `tools/pdf_edge_scan.py`: 8 pages, **0 TOUCH, 0 NEAR**.
- `tools/d5_creambox_audit.py` (pre-D5 baseline vs rebuilt): **PASS 0 defects**; ratios n=538, median 1.007, bold 1.044 / regular 0.975; P8 lines 232→227, footer slack 33.6→33.6px.
- Web/print text layer: `pdftotext` default mode — both **50,566 bytes**, word multiset identical, normalised text exactly identical; `-raw` mode — both 49,495 bytes, identical.

## §7 Fan-out changes (explanation layer only — no German text, fact or key changed)

### Rebuild 3 (2026-11-11 — core build15 Q34 change only; first attempt killed, retried)
- **Q34 stem change (the reason for this rebuild):** core-de build15 changed the
  P3 exercise Q34 stem from plural "Am Montag öffnen in Köln die ersten ___."
  to singular "Am Montag öffnet in Köln der erste ___." (key `Weihnachtsmarkt`
  unchanged). The edition was deleted and re-transformed from the new core.
  Verified: new stem 1x / old stem 0x in source, .text.md, P3 SVG, and both
  PDF text layers. P3 freeze sha changed accordingly (093cf378 → fc88f676);
  all other pages byte-identical to rebuild 2.
- **First attempt killed (RC 120, 08:31–08:32):** run.py finished but the
  driver died during render.py (cards p1–p3 only, no PDF) under heavy parallel
  load on the machine. Retried 08:37–08:41 with `python -u`: ALL GATES PASS.
  No box-title changes this round (boxtitle.py 7/7); the rebuild-2 P8
  battery-A head fix ("Preenchimento") is preserved.
- **Web PDF +40 KB vs rebuild 2 (tool change, not content):** the pt web PDF
  was built after an uncommitted `tools/webpdf.py` change (`:style=Bold` →
  `:weight=200` fc-match) landed mid-session, so it embeds a Newsreader-Bold
  subset on all 8 pages; the en/fr/es/it web PDFs (built 08:15–08:29, pre-patch)
  embed none. Text layer identical to print; valid deliverable. See
  EDITION-RECORD.md. Sibling web PDFs can be rebuilt once the patch settles.
- New deliverables: print 10,968,908 B sha 33e2dc7d…; web 1,599,432 B
  sha a251196e…; text.md 49,812 B sha 42579207…. All gates green;
  P8 keys end 2457, flow ends otherwise identical to rebuild 2.

### Rebuild 4 (2026-11-11 — P7 toolbox fix, D1-class; proof2 follow-up)

- **Defect (measured, not visual):** the P7 DER WERKZEUGKASTEN box leaked ink.
  creambox.py on the on-disk SVG: box y=330, bottom=813.0, last entry baseline
  **813.0** (clearance **+0.0**); the `g` in `fraglich` descends 5.2 units
  (PIL-measured in Newsreader 20.5pt), so ink ended 818.2 — **5.2px below the
  box bottom**. Root cause (family-wide, see de-es fix1): the `tbh` formula
  under-counts by 123 (6 × 20.5 missed para offsets); the fan-out pad 90
  (down from the core's 110) was "validated by occlusion 0 flags" — a void
  validation, since the audit cannot see text spilling past its own box.
  proof2's "zero findings" never ran creambox, and its PROOF-NOTE L115
  「文字收进盒内」 (100 dpi visual) is contradicted by the SVG geometry:
  a ~2px spill at 100 dpi is below visual detection. The L115 "0.5px" figure
  itself is correct but refers to NOCH EIN WORT (ends 1547.5 vs the 1548 line).
- **Fix (pt-specific; the family pad-110 fix is impossible here):** NOCH EIN
  WORT already ends 1547.5, 0.5px above the Sätze rule at 1548, so any
  downward shift crosses it. Instead the toolbox **grows upward by 20**:
  `tbt = CTOP − 20 = 310`, `tbh` +20 (bottom stays 813.0), the whole block
  (title + 6 entries) shifts up rigidly, `ry` stays 829 — LESERBRIEFE and
  NOCH EIN WORT do not move. Intro ink ends ~266, so 44px of gap remains
  above the new top. Result: baseline clearance **+20.0**, ink clearance
  **+14.8**. One block in `content7.py` only; no string, no helper touched.
- **Verified pre-fix values (disk + proof2, 2026-11-11):** print 10,968,903 B
  sha `5f2bc3d4590fca0e6509fda53ddafe6a4b1cc618a5c23e78f5181e177143c2aa`;
  web 1,602,461 B sha `62371d80a399779aded2e9dbcd3ea303f46f338d7c9d9241dc929e4
  a1a0e7adb`; text.md 49,812 B sha `e2ee96ebd9dca775598431f87c511f53ed04dec25
  47896586d46a2c57a800928`. (Correction: the rebuild-3 SHAs previously listed
  in §5 predate the D1-fix rebuild that proof2 verified; the values above are
  the verified ones. New rebuild-4 deliverables are in §5.)
- **Rebuild 4 gates:** driver ALL GATES PASS (occlusion 0, p8 CLEAN keydiff
  [137,138,139,150], freeze diff RC 0 / 7 CJK, text layer identical, chips
  141, P8 9.94pt); freeze_direct **8/8** source PASS (P3 fc88f676, P7
  b7aa0771 unchanged); keycheck 149/150 (Q150 only); boxtitle 7/7; measure
  24/24; d2scan 0 gaps >0.5pt; quotes „ 33 = “ 33 paired; Q34 new stem 1× /
  old 0× everywhere; D1 `pess.` 13 / `pers.` 0 in all five layers; text.md
  byte-identical to pre-fix. Scratch:
  `hidden_files/w47/scratch-fix-de-pt-toolbox/` (FIX-LOG.md, GATE-LOG.md).

### Rebuild 5 (2026-11-12 — boxtitle gate fix, P1 only)

- **Defect (new standing gate `tools/boxtitle_check.py`, 130-wide run
  2026-11-12):** P1 ZAHLEN box title `DIE WOCHE IN ZAHLEN　Em números` ran
  past its cream box by **+15.5px** (core-de fits at −11.5px).
- **Fix (edition-local, `content12.py:43` only):** the `f.box` title size
  `tsize` 23 → 21.5 (layout only, no text changed). Predicted and verified:
  ink end 976.5 → **948.5**, margin **+12.5px**. The box is 1.5px shorter
  (334.2 → 332.7); the P1-headline flow end stays 1554 (= core), verified
  identical with the fix reverted in a scratch copy — the 1.5px slack is
  absorbed at the column break. No other line touched.
- **Rebuild 5 gates:** boxtitle **0 DEFECT / 0 OBSERVE / 0 marginal** (also 0
  on the synced production files), verify TOTAL 150 + SVGs byte-identical
  after re-run, occlusion 0 flags, p8 extract 150/150 + compare CLEAN keydiff
  [137,138,139,150], freeze `diff` exit 0 (added CJK 7, all U+3000) +
  freeze-direct rendered **8/8** with all 8 frozen SHAs identical to rebuild 4
  (083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 /
  57e118e7). NOTE (pre-existing, not this fix): freeze-direct *source* level
  now reports 1 unaccounted removed literal (`'sans'` ×2 in `svglib.py`) —
  core-de's `svglib.py` was patched (fix2 U+201C routing, 2026-11-11 22:35)
  after pt was copied from it; at rebuild-4 time the source level PASSED.
  This fix changed no string literal (one kwarg + one comment). New
  deliverables: print 10,968,901 B (−1 B) sha
  `bfdc6e8fda242f11dfaee0658b016dc6cf7c622c71b7287d1dfa018809fab9e9`; web
  1,602,460 B (−12 B) sha
  `e723f2cbc267d6d0fbe35be45d243ae5c3dcfe3130d8a38a012d6f018ad1a010`; text.md
  49,812 B sha e2ee96eb… (unchanged). Scratch:
  `hidden_files/w47/scratch-gatefix-de-en/2026-w47-de-pt/` (FIX-LOG.md).

### D5 font rebuild (2026-11-12 — rebuild 6)

- **Cause**: explanation-layer Latin rendered in Noto Sans CJK instead of Newsreader (SOP §1.1 font table). Pre-D5 census: 631 Latin-in-CJK-Sans elements.
- **Fix (mechanism)**: `apply_variant.py` installed the D5 `_char_font` sans routing on the edition's `svglib.py` (Latin → Newsreader 400/600; fix2 included). No German text, fact, or key changed; no wording changed at all.
- **Eight D5-caused defects, all fixed in source and rebuilt (run2)**:
  1. P1-fussball head `EINE WOCHE, ZWEI STIMMUNGEN` — HEAD TOO WIDE at 25pt; `content12.py:124` 25→22pt (411.8px fits the 422.5px column).
  2. P1 cream-box title `DIE WOCHE IN ZAHLEN　Em números` — +23.2px past the box; `content12.py:43` `f.box(…, tsize=20)` (397.6px fits 404.5; 21pt still overflows by 13.0px). Note: the rebuild-5 fix (23→21.5) held under CJK Sans but not under Newsreader SemiBold — the D5 widening re-broke it.
  3. P3 vocab-box title `WEIHNACHTSWÖRTER　Palavras` — +24.9px; `content34.py:58` 24→22pt (389.9px fits 400.5).
  4. P7 toolbox title `DER WERKZEUGKASTEN　Material` — +30.0px; `content7.py:88` 23→21pt (393.0px fits 400.5; 22pt still overflows by 11.2px).
  5. P7 reader-letters title `LESERBRIEFE　Cartas dos leitores` — +3.2px; `content7.py:105` 23→22pt (385.9px fits 400.5).
  6. P7 box title `NOCH EIN WORT　Mais uma palavra` — +11.6px; `content7.py:114` 22→21pt (393.0px fits 400.5).
  7. P8 battery head `A　LÜCKENTEXT　Preenchimento` — HEAD TOO WIDE at 24pt (430.1px > 422.5px column); `content8.py:78` 24→22pt (394.3px fits).
  8. P8 battery head `F　WÖRTER PAAREN　Associações` — HEAD TOO WIDE at 24pt (435.3px > 422.5px column); `content8.py:149` 24→22pt (399.0px fits).
- **Verification**: full gate re-run (§6b) — census 0, occlusion 0, p8 CLEAN, freeze 8/8, added CJK 0, spill 0, boxtitle 0 (real backup), edge 0, creambox PASS, print/web text layers identical in both modes.
- Note: the P1 masthead subtitle never collided with the headline in this edition.

### Round 1 (build 1 → rebuild 2, one value fix)
- Build 1 failed exactly ONE gate: 'no HEAD TOO WIDE' — the P8-battery head A
  "A　LÜCKENTEXT　Texto com lacunas" measures 434.6px at 24pt bold sans vs the
  422.5px column-width limit (CW). Everything else passed (occlusion 0 flags,
  chips 141, p8 CLEAN, freeze exit 0, P8 min font 9.94pt). No column-jump or
  overflow cascade: P8-battery still ends 1409, P8-keys 2457.
- Fix (in `vals_pt.json`, regenerated `tr_pt.py` — diff exactly 1 line):
  "A　LÜCKENTEXT　Texto com lacunas" → "A　LÜCKENTEXT　Preenchimento"
  ("Preenchimento" = 400.4px, PASS with 22px margin; the standard Portuguese
  term for a cloze exercise; "Lacunas" 315.9 and "Texto lacunar" 377.7 were the
  other measured candidates).
- Build 2: ALL GATES PASS + visual proofread P1–P8 zero findings.
- **Apostrophe rule applied from the start:** `tr_pt.py` was written with straight
  apostrophes U+0027 throughout (as `\u0027` escapes inside single-quoted
  strings); U+2019 scan over the 8 SVGs is 0.
- Box titles (from the 5th-baton sweep, before build 1): STILLE "A semana
  tranquila" → "Tranquila"; ADVENTSWÖRTER "Palavras do Advento" → "Advento";
  TOOLBOX "Ferramentas" → "Material" ("Utensílios" measured 405.7, still OVER,
  rejected) (boxtitle.py 7/7).

### Reproof fix rebuild (2026-11-12 — rebuild 8)

- **Cause**: independent reproof of the D5 rebuild found 9 items (F7 major, rest minor) — see `hidden_files/w47/scratch-reproof-w47-de/PROOF-NOTE.md`.
- **Fix (in source, then rebuilt)**: F7 — P1 kicker shortened to `O ALEMÃO DOS ALEMÃES` (advance gap 31.9px, P1 render verified); F1 — P5 UND SIE prompt gained the advent-calendar question; F9 — P8 `·` spaced (142 places). Knock-on: P5 image gap 26→14px (image ends 1749.93). Gates: build ALL GATES PASS; boxtitle 0 DEFECT; spill 0 SPILL; edge 0/0; census-patched PASS; head_check PASS; text.md dry-run diff 10 lines, 0 dropped.
- **Verification**: full gate re-run (logs in `hidden_files/w47/scratch-fix-de/logs/`) — see the per-edition entry in `scratch-fix-de/FIX-LOG.md`.
- New deliverables: print 10,354,705 B sha `55e95caf7bcb…`; web 1,514,735 B sha `c62f38ea0c65…`; text.md 50,121 B sha `2e2ce4689359…`.

### fix-de-minor1 (2026-11-13 — round-2 reproof C-1/C-2)

- **Fix (in source, then rebuilt)**: C-1 — P3 lead `die ersten Weihnachtsmärkte` contradicted the Hafenmarkt (open since 13 Nov, same article §2): P3 lead → `zwei große Weihnachtsmärkte` (same length, zero layout shift); the P5 lead carried the identical false claim and was fixed with the same wording; Q34 `Am Montag öffnet in Köln der erste ___.` → `Am Montag öffnen in Köln der Markt am Dom und der Markt der Engel, zwei große ___.` (word-box word and answer key `Weihnachtsmarkt` → `Weihnachtsmärkte`); Q80 `Am 16. November öffnen in Köln die ersten Weihnachtsmärkte.` → `Am 16. November öffnen der Markt am Dom und der Markt der Engel.` (answer stays `Richtig`). Q29 left unchanged (A2-acceptable per the brief; changing it would change the answer key). C-2 — P5 1903 calendar `Die Kinder konnten die Fenster mit Bildern überkleben.` → `Die Kinder konnten die Bilder ausschneiden und auf den Kalender kleben.` (the 1903 Lang/Kepler edition was windowless cut-and-paste). The `überkleben` gloss entry is left in place (the brief's fix is the sentence only; flagged to the coordinator). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p3, p5, p8 (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-fix-de-minor1/2026-w47-de-pt/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 42 titles, 251 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal; spill 0 SPILL / 87 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 0 (reader layer; the shift vs the previous round's count is P3/P5/P8 re-wrap from the longer Q34/Q80 sentences, not content — the multiset proof below is authoritative), added Latin strings 439; print/web text layers multiset-identical (39,901 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: `die ersten`→`zwei große` ×3, `erste`→`Markt am Dom und der Markt der Engel` ×2, `Fenster mit Bildern überkleben`→`Bilder ausschneiden und auf den Kalender kleben`, footer/Q34-key changes where applicable); text.md re-exported from the fixed sources, diff exactly 7 lines (L309 P3 lead, L387 box, L389 Q34, L573 P5 lead, L577 C-2, L693 Q80, L1165 P8 answers Q34 key), 591 entries / 150 exercises. New deliverables: print 10,354,753 B sha `43afa6245ae1…`; web 1,514,771 B sha `ce68d33381bd…`; text.md 50,190 B sha `fc3ed0a7e464…`. Not committed / not pushed (coordinator inserts).


### fix-de-round3 (2026-11-13 — round-3 reproof R3-F1/R3-F2)

- **Fix (in source, then rebuilt)**: R3-F1 — the C-2 fix (fix-de-minor1) removed `überkleben` from the P5 1903 sentence but left the orphan gloss entry in the P5 gloss (`content56.py:23`); SOP §8.1 requires every glossed word to occur in the text, so the ` · überkleben …` segment was deleted from the P5 gloss (gloss shortens by one entry, layout-safe). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p5 only (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-reproof-de-round3/2026-w47-de-pt/fix-round3/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 42 titles, 250 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal; spill 0 SPILL / 86 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 0, added Latin strings 438; print/web text layers multiset-identical (39,876 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: gloss `überkleben …` entry removed); text.md re-exported from the fixed sources, diff exactly L585 P5 gloss, 591 entries / 150 exercises. New deliverables: print 10,354,731 B sha `23c1505097e1…`; web 1,514,736 B sha `bda89b7b2180…`; text.md 50,158 B sha `b1b6a7e20abd…`. Not committed / not pushed (coordinator inserts).
## §8 Honest shortfalls (inherited from the core)

- No real reader letters by press time — editor's example + disclosure (see §3).
- Events of 13/15/16 Nov are previews only at press time — no results claimed.
- Practice chart (P6, 44/33/23) is labelled ÜBUNGSDATEN — practice data, not a
  real survey.
- P8 answers at 9.94pt — above the 9.75pt floor but below the 11.25pt target
  (concession step 4; no expansion needed).
- P8 exercise stems at 15.375pt (concession step 3); P8 cloze passage and dialogue
  passage at 14.625pt, option rows at 13.875pt (core O1, left by coordinator
  decision, pending the joint ruling with ko/ja/zh-tw).
- No drop cap on the P1 lead first paragraph (shared with the accepted W46-FR
  edition; flagged in the core KIT §8).
