# WEEKLY-KIT — 2026-W47 · German edition for French-speaking readers

- Edition: `2026-w47-de-fr` — German target text, French explanations
- Week: Mon 2026-11-16 – Sun 2026-11-22 · VOL.4 · Press time: Mon 2026-11-09
- Lead story: **Die Bundesliga kehrt zurück — Bayern gegen Köln** (40 chars, limit 56)
- Status: fan-out complete, all self-check gates green, visual proofread 8/8 pages
  zero findings (rebuild 4, 2026-11-11; core build15); fix1 rebuild 5 (2026-11-11,
  D1 toolbox-pad fix only, all gates green again); independent proofread pending
  (coordinator to assign). New standing gates (2026-11-12) found 1 boxtitle
  defect (P1 Fragen subtitle +5.5px); rebuild 6 (2026-11-12) repaired it by
  layout only, all gates green again.
- **D5 font rebuild applied 2026-11-12 (rebuild 7, all gates green — see §7)**
- Source: `core-de/` (2026-w47-de-zh-cn, build15) copied and translated in the
  explanation layer only. German target text is frozen — see §6 for the proof.
- Builder: de fan-out builder, 4th shift (2026-11-11). Scratch:
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-de/`
  (`tr_fr.py`, `transform.py`, `build_edition.py`, `fr/` gate logs).

## §1 Contents

8 pages, 1950×2700, 4 columns. **150 exercises**, continuous numbering 1–150, all in
the registry. Identical layout and exercise set to the core; only the explanation
layer (bridges, instructions, glosses, notes, toolbox, disclosure, keys notes) is French.

| Page | Section | Level | Ex. |
|---|---|---|---|
| P1 | Front: lead + Fragen der Woche + sommaire + word of the week + Blitzquiz | A2 | 10 |
| P2 | Leben: Buß- und Bettag & Alltag + Rechnen | A2 | 18 |
| P3 | Kultur: Weihnachtsmärkte & stille Woche (1930 painting) | A2→B1 | 18 |
| P4 | Sport: results 3–8 Nov + fixtures table + MD10 return | B1 | 18 |
| P5 | Jugend: Adventskalender basteln + Wochenplan (1903 calendar) | B1 | 18 |
| P6 | Vertiefung: stille Woche & Haushalt 2027 + practice chart | B2 | 18 |
| P7 | Sprache: A2/B1/B2 lessons + Sätze der Woche + Fehlerklinik + Leserbriefe + VOL.5 teaser | A2/B1/B2 | 12 |
| P8 | Schlusstest + Schreiben (MUSTER 84 words) + all answers | mixed | 38 |

Levels: A2 69 / B1 67 / B2 14. Types: choix multiple 52 / à compléter 41 /
transformation 11 / vrai ou faux 8 / texte à trous 8 / phrases à construire 8 /
associations 12 / traduction 4 / dialogue à compléter 5 / rédaction 1.

Pairing furniture (VOL.4): masthead `Die Lucerna`; edition line
`HEBDO ALLEMAND　VOL.4　RETOUR DE LA BUNDESLIGA　SEMAINE CALME`; footer
`Die Lucerna　HEBDO ALLEMAND VOL.4　Texte allemand　Explications en français`;
page line `Page N sur 8`; gloss prefix `Note — `.

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
  carries the labelled editor's example + the French disclosure:
  "Exemple de la rédaction — aucune vraie lettre n'était arrivée avant le bouclage.
  Envoyez vos textes pour le VOL.5."

## §4 Images

Identical to the core (see `core-de/WEEKLY-KIT.md` §4 and `assets/CREDITS.md`):
fussball.jpg (P1), kopfball.jpg (P4), weihnachtsmarkt1930.jpg — Wilhelm Ritter 1930
(P3), christkind.jpg — Richard Ernst Kepler 1903 (P5), lesesaal.jpg — Carol M.
Highsmith, Library of Congress (P7), fussball1905.jpg (P8). All public domain, each
with target-language caption + printed credit.

## §5 Build / reproduction

- Build dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-de-fr/`
  (build code + deliverables, copied from `core-de/` by `transform.py fr`).
- Reproduce: `tools/venv/bin/python transform.py fr` (from scratch-fanout-de) →
  `tools/venv/bin/python measure.py fr <edition-dir>` →
  `tools/venv/bin/python build_edition.py fr` (run.py → render.py → webpdf →
  verify → occlusion → p8 → freeze → pdftotext → chips → export).
  Build interpreter is `tools/venv/bin/python` (PIL 13.0.0); freeze was re-run with
  the same interpreter (system python3 has PIL 10.2.0 and measures 1.1% differently).
- Deliverables (fix-de-round3 rebuild, 2026-11-13; F1 banner fix rebuild, 2026-11-13 — rebuild 9 superseded):
  - Print PDF: `Die-Lucerna-VOL4-de-fr.pdf` — 10,352,491 bytes, 8 pages,
    sha256 `4f6ccacfb20eaa7cddae91b8041761e2183e551287c83eb31e5385cfa744d38f`
  - Web PDF: `Die-Lucerna-VOL4-de-fr-web.pdf` — 1,512,524 bytes (< 7 MB),
    51,123 text bytes,
    sha256 `22525742a6bbfdc13ab0bb8df86aabd2e3f4b9d5a3f49e682cfef930f029a0d3`
  - Text export: `2026-w47-de-fr.text.md` — 50,392 bytes, 48,514 chars,
    591 entries, 150 exercises,
    sha256 `80f1a96deb470d0cb3c798df7602bcfb36919d1292fd7b4f6c24495ccae9fbf8`
    (changed — P1 banner gloss shortened per the §7 F1 fix entry; re-exported from the fixed sources)
    (exported from production sources in reading order, never from PDF)
  - `ABSTRACT.txt` (one line, French, no ASCII double quotes):
    "Die Lucerna Hebdo allemand VOL.4 : retour de la Bundesliga (le Bayern reçoit
    Cologne), match décisif de la Ligue des nations contre les Pays-Bas, jour de
    repentir et de prière et dimanche des morts, ouverture des marchés de Noël de
    Cologne, résultats européens et de Bundesliga du 3 au 8 novembre ; texte en
    allemand, explications en français, niveaux A2–B2, 150 exercices sur les
    thèmes de la semaine."

## §6 Gates (rebuild 3, 2026-11-11 — final)

- `run.py` (build.log): exit 0, **zero FLOW OVERFLOW / HEAD TOO WIDE**, TOTAL 150.
  Flow ends: P1-headline 1554 (= core), P1-fussball 2264, P1-quiz 2523,
  P2-feature 993, P2-ex 2332, P3-main 916, P3-ex 2041, P4-main 677, P4-ex 2315,
  P5-main 1026, P5-ex 2441 (= core), P6-main 777, P6-ex 2523, P7-A2 1278 / B1 1342 /
  B2 1306, P8-battery 1409, P8-keys 2426 (bottom 2560, spare 134px).
- `measure.py`: **24/24 PASS, 0 FAIL**.
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
  **Direct freeze proof (8/8, `fr/freeze-direct.json`, script `freeze_direct.py`):**
  (a) source-level: AST string-literal multiset core vs edition — 0 unaccounted
  removed, 0 unaccounted added (520 removed / 528 added, every one accounted for
  by the translation module, the CJK inventory, or a documented transform artifact);
  (b) rendered-text level: the frozen intersection (strings identical in core and
  edition SVGs) per page — P1 147, P2 163, P3 195, P4 166, P5 173, P6 175, P7 150,
  P8 186 strings, sha256 083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 /
  2bbe05f9 / b7aa0771 / 57e118e7 — identical to de-en, as the frozen content is
  the shared German text (P3 sha changed with the Q34 stem, see Rebuild 4 note).
- Print/web text layer: `pdftotext` default mode — print 50,879B / web 50,879B,
  **word multiset identical**; `-raw` mode — both 49,698B, normalised text
  **exactly identical**. Web PDF has a real text layer.
- Level chips (rx="2.7" rects): per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18,
  7:12, 8:35}, **TOTAL 141**; P8 by level A2 22 / B1 13 / B2 0. The core's
  missing-14 set is fully present: cloze options Q113–120 (8 A2 chips),
  dialogue badges Q145–149 (145–147 A2, 148 B1, 149 A2), writing title chip
  (B1 on "H SCHREIBEN").
- P8 answers measured font size: keys 13.25 SVG units = **9.94 PDF pt**
  (PyMuPDF re-measured P8 minimum span 9.94pt) — above the 9.75pt floor
  (concession step 4; P8 stems stay at the core's 15.375pt).
- 150-question key check (independent, `fr/keycheck-150.json`, script
  `keycheck.py`): P8-SVG-extracted keys vs the REG built from the edition's own
  sources — **149/150 exact**; the single non-exact item is Q150, the open
  writing task, where the extractor truncates the REG key "Exercice libre —
  suivez les points de l'encadré d'écriture" to "Exercice libre" (expected;
  Q150 is already in the keydiff set). REG by page
  {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}; levels A2 69 / B1 67 / B2 14.
- Visual proofread: all 8 pages re-rendered from the print PDF at 100 dpi and
  viewed one by one (P1–P8), plus magnified crops of the P1 word-of-week line
  and the P4 Und-Sie box. **Zero findings** (see §7). The P8 keys were
  spot-checked against the registry (dates, scores, times, grammar keys,
  MUSTER 84 words, chart 44+33+23=100).

### Rebuild 4 (2026-11-11 — core build15 Q34 change + six box-title fixes)
- **Q34 stem change (the reason for this rebuild):** core-de build15 changed the
  P3 exercise Q34 stem from plural "Am Montag öffnen in Köln die ersten ___."
  to singular "Am Montag öffnet in Köln der erste ___." (key `Weihnachtsmarkt`
  unchanged). The edition was deleted and re-transformed from the new core.
  Verified: new stem 1x / old stem 0x in source, .text.md, P3 SVG, and both
  PDF text layers. P3 freeze sha changed accordingly (093cf378 → fc88f676);
  all other pages byte-identical to rebuild 3.
- **Box-title fixes (real defects, found by boxtitle.py precheck):** six P2/P3/P5/P7
  box titles measured over the 400.5px box budget in rebuild 3 (STILLE 453.6,
  WEIHNACHTSWÖRTER 436.7, TIPP 430.1, ADVENTSWÖRTER 413.9, WERKZEUGKASTEN 440.9,
  LESERBRIEFE 410.8) — ink ran past the cream box (visually confirmed on the
  rebuild-3 P3 render). Shortened to: La semaine / Noël / Conseil / Avent /
  Outils / Courrier. boxtitle.py now 7/7. See EDITION-RECORD.md.
- New deliverables: print 10,932,570 B sha 126e9522…; web 1,556,917 B
  sha 727c8b8a…; text.md 50,042 B sha 3ef1934a…. All gates green;
  P8 keys end 2426, flow ends otherwise identical to rebuild 3.

### Rebuild 5 (2026-11-11 — fix1, D1 only)
- **D1 (de-es proof1 family defect, reproduced on fr pre-fix):** P7
  DER WERKZEUGKASTEN cream box too short — box bottom 783.5, last entry
  `Es ist fraglich, ob ... = encore ouvert` baseline 783.9 (clearance −0.4),
  `fraglich` descender ink ~4.7 below the box. Root cause (measured per-edition):
  the `tbh` formula in `content7.py:76` counts `n*29.5+6` per entry but the real
  advance is `20.5 + n*29.11 + 6` (`Page.para` first-baseline offset, 6 entries =
  +123 missed); fr wraps Σlines=9, so clearance = pad − 90.4 and pad 90 gave −0.4.
  Core-de uses pad 110 (+18.8); the fan-out had cut it to 90 with a "validated by
  occlusion 0 flags" comment — void, since the occlusion audit cannot see text
  spilling past its own box (nothing covers it).
- **Fix (edition-local, `content7.py:76` only):** pad 90 → 110 (restores the core
  value), comment rewritten with the arithmetic. No shared helper touched. Predicted
  and verified: toolbox bottom 783.5 → **803.5**, clearance **+19.6**; LESERBRIEFE
  y 799.5 → 819.5 (16px gap preserved, +10.4 unchanged); NOCH EIN WORT ends 1518.0 →
  **1538.0** (10px before the 1548 Sätze rule, +42.9 unchanged). 300 dpi toolbox zoom
  confirms the last entry fully inside the cream box (clear cream below the `g`
  descender); print/web toolbox zooms pixel-identical. No text changed: text.md
  byte-identical (sha 3ef1934a…); freeze_direct 8/8 with all 8 page shas identical
  to rebuild 4 (083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 /
  b7aa0771 / 57e118e7).
- **Tool-note (pre-existing, not a regression):** `freeze_direct.py` / `boxtitle.py`
  run from `scratch-fanout-de/` read the stale `tr_fr.py` there (pre-rebuild-4 long
  box titles) and report source FAIL (4 unaccounted abbreviated titles) / boxtitle
  1/7. Run from `scratch-fanout-de-rebuild-A/` (current `tr_fr.py`, shortened titles)
  both pass: freeze_direct source PASS + rendered 8/8; boxtitle 7/7. The rendered
  titles themselves measure 7/7 (max 376.9 ≤ 400.5). Verified the freeze_direct FAIL
  is pre-existing by re-running it with pad reverted to 90 — same 4 unaccounted.
- New deliverables: print 10,932,565 B (−5 B) sha
  `0df35360ac599e8af590f990ae302dfe17f8daf23904bbc4e5aac6d641ecc413`; web 1,600,197 B
  (+43,280 B — working-tree webpdf.py now embeds the `LucernaNewsreader-Bold` subset,
  23,780 B; same effect as es/pt/ko/zh-tw; < 7 MB, text layer identical to print) sha
  `5262bfaea8f8947874171b558e704e36bc7f138e3c9419afce5809a76836b167`; text.md 50,042 B
  sha 3ef1934a… (unchanged). All gates green (occlusion 0 flags real run, p8 CLEAN
  keydiff [137,138,139,150], freeze diff +7 CJK all U+3000, freeze_direct 8/8 source
  PASS, keycheck 149/150 — Q150 extractor truncation only, boxtitle 7/7, d2scan 58
  pairs 0 web gaps >0.5pt, P8 min 9.94pt, chips 141, verify TOTAL 150, bent quotes
  U+201C 33 / U+201D 0, Q34 new stem 1x in all five places). Gate logs in
  `hidden_files/w47/scratch-fix-de-toolbox-family/gates-fr/`; build logs in
  `hidden_files/w47/scratch-fanout-de/fr/`.

### Rebuild 6 (2026-11-12 — boxtitle gate fix, P1 only)
- **Defect (new standing gate `tools/boxtitle_check.py`, 130-wide run
  2026-11-12):** P1 Fragen subtitle `Les grandes questions　Die Fragen der
  Woche` ran past its cream box by **+5.5px** (core-de fits at −22.0px).
- **Fix (edition-local, `content12.py:69` only):** subtitle font size 19 → 18
  (layout only, no text changed). Predicted and verified: ink end
  1867.5 → **1846.5**, margin **+15.5px**. No other line touched.
- New deliverables: print 10,932,566 B (+1 B) sha
  `f5e68b46039f4bdb77a8ffb8e80fd47c0e0b24ebff746e74a6da6804c127bf67`; web
  1,600,196 B (−1 B) sha
  `ae89ba2c23645fe720f812d0a2902feecdddc1f2326ef0c026d8c111b33933f7`; text.md
  50,042 B sha 3ef1934a… (unchanged). All gates green on the rebuilt edition:
  boxtitle **0 DEFECT / 0 OBSERVE / 0 marginal** (also 0 on the synced
  production files), verify TOTAL 150 + SVGs byte-identical after re-run,
  occlusion 0 flags, p8 extract 150/150 + compare CLEAN keydiff
  [137,138,139,150], freeze `diff` exit 0 (added CJK 7, all U+3000) +
  freeze-direct rendered **8/8** with all 8 frozen SHAs identical to rebuild 5
  (083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 /
  57e118e7). NOTE (pre-existing, KIT-documented in Rebuild 5): freeze-direct
  *source* level reports 4 unaccounted ADDED literals — the rebuild-4
  shortened box titles (`WEIHNACHTSWÖRTER　Noël`, `DER TIPP　Conseil`,
  `ADVENTSWÖRTER　Avent`, `DER WERKZEUGKASTEN　Outils`) live in the content
  files but not in the stale `tr_fr.py` the script reads; Rebuild 5 records
  the same 4 with the same cause. This fix changed one int + one comment, no
  string literal. Gate outputs in `scratch-gatefix-de-en/2026-w47-de-fr/`
  (FIX-LOG.md).

## §6b Gates (D5 font rebuild round, rebuild 7, 2026-11-12 — full re-run on the rebuilt edition; scratch `hidden_files/w47/scratch-d5-de/de-fr/`)

- D5 mechanism: `apply_variant.py --svglib … --target de --reader fr` (mode latin) on the edition's `svglib.py`; fix2 curly-quote routing installed with it (routing assert `ROUTING FAILURES: 0`). Pre-D5 `svglib.py` backed up as `svglib.py.pre-d5`. Pre-D5 baseline verified CLEAN before install: the production dir was copied to scratch and rebuilt with the venv interpreter — freeze baseline **8/8 SVGs byte-identical** to the delivered SVGs (`freeze-pre-baseline.log`). Pre-D5 production snapshot in `scratch-d5-de/de-fr/baseline/` (SVGs + sources, rebuild-6 state). KIT wave 2 check: pre-D5 print SHA matches the KIT (`f5e68b46…`), but the pre-D5 web PDF on disk was sha `ae89ba2c…` (1,600,196 B), NOT the KIT's rebuild-6 record `5262bfae…` — the rebuild-6 web PDF had been rebuilt without a KIT sync (same class as de-en's). The D5 values above are measured from the actual files on disk.
- Pre-D5 D5 census: **637 Latin-in-CJK-Sans elements** (matches D5-CENSUS-130); quotes defective 0; p8 extract 150/150.
- `run.py` (run2): TOTAL **150**, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`tools/head_check.py`: PASS 0 defects).
- `mechanism/d5_census.py`: **PASS — D5 Latin 0, D5 Cyrillic 0, curly-in-CJK 0**.
- `tools/occlusion_audit.py`: **0 flags** (selftest OK; fixed tool — bare `Noto Sans` runs measured on the non-CJK face, brief §10).
- `tools/p8.py`: extract 150/150; compare vs rebuilt core-de P8: `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]` — the same 4 expected reader-language items as rebuild 3.
- `tools/freeze.py`: baseline **8/8 SVGs byte-identical** (venv Pillow 13.0.0 / FreeType 2.14.3); diff pre-D5 baseline vs rebuilt: **added CJK characters 0** (added Latin strings 371 = D5 run-splitting).
- `tools/spill_sweep.py`: 32 boxes, 84 candidates, **0 SPILL**, 84 OBSERVE.
- `tools/boxtitle_check.py`: 46 titles, 244 body lines, **0 DEFECT**, 0 OBSERVE, 1 marginal (P7 `Outils` +1.0px, within tolerance — the core has the same +1.0 marginal, pre-existing, not a D5 regression; real backup comparison: `scratch-d5-de/scratch-fanout-de/backup/2026-w47-de-fr`). Coverage note: the P1 box title sits at 21pt after the D5 fix, below the tool's 22pt detection floor — it is verified instead by the creambox audit (0 defects across all 32 boxes) and by direct ink measurement (right-edge spare 5.1px).
- `tools/pdf_edge_scan.py`: 8 pages, **0 TOUCH, 0 NEAR**.
- `tools/d5_creambox_audit.py` (pre-D5 baseline vs rebuilt): **PASS 0 defects**; ratios n=544, median 1.007, bold 1.045 / regular 0.976; P8 lines 233→234, footer slack 33.6→33.6px.
- Web/print text layer: `pdftotext` default mode — both **50,746 bytes**, word multiset identical, normalised text exactly identical; `-raw` mode — print 49,689 B / web 49,690 B, differing by exactly **one space** (web "früh → früher", print "früh→ früher" — poppler block grouping, same class as the core build15 note; non-space characters identical, 39,966 = 39,966, zero word characters lost).

## §7 Fan-out changes (explanation layer only — no German text, fact or key changed)

### Round 1 (build 1 → build 2, `fix_tr_fr.py`, 88 value fixes + LAYOUT pad fix)
- P1 ZAHLEN box jumped a column (box grew 334→390px) → items shortened:
  "(5 points en quatre matchs)", "(Bayern-Cologne 20 h 30)"; flow ends 1554 = core.
- P1 Fragen box bottom line overflowed the page edge → "Les cinq questions de la
  semaine." (294px).
- P4 Und-Sie prompt 3→2 lines → "Bundesliga ou équipe nationale ? Qui gagne à
  Munich ? Écrivez en allemand !"; box clears the results table.
- P5 Und-Sie prompt 4→2 lines → "Votre liste de souhaits : qu'y a-t-il ?
  Écrivez en allemand !"; col3 image ends 1523.3, hline 1744 clears.
- P5 bridges A + C 2→1 line each ("Lisez la page 5. Choisissez la bonne
  réponse." / "Reliez deux phrases avec weil."); P5-ex ends 2441 = core.
- P6 ÜBUNGSDATEN paren shortened → "(Exemple de la rédaction, pas un vrai
  sondage.)"; full line 1723px ≤ 1862px available.
- P7 toolbox entry 6 2→1 line ("Es ist fraglich, ob ... = encore ouvert");
  NOCH EIN WORT 3→2 lines ("« der Adventskalender » (page 5) : un calendrier
  de 24 petites portes."); LAYOUT toolbox pad 110→90 (same fix as en).
- P8 battery head too wide → "C　LESEVERSTEHEN　Lecture".
- P8 keys notes: ~820 chars cut across the longest notes (tier 1 + tier 2,
  incl. "(3e pers. du sing.)" → "(3e pers. sg.)"); keys flow 114→100 lines,
  P8-keys ends 2426 (spare 134px, better than en's 105 lines / 2481).

### Round 2 (build 2 → rebuild 3, `fix_tr_fr2.py`, 1 fix)
- **P1 word-of-week para (occlusion LINEX ×1, the only build-2 flag):** the
  French para wrapped 2 lines ("... Voir" / "page 5."), its 2nd line ink crossed
  the row-B hline at y=1844 (en fits 1 line). Shortened to "Calendrier de
  l'Avent (24 portes). Voir page 5." — measured with the edition's own svglib
  (19pt sans, width 423): 394.6px → 1 line (old value 459.6px → 2 lines).
  Magnified crop confirms the single line clears the hline.
- **Print PDF 69.6 MB anomaly (build 2, the other build-2 failure):** render.py
  wrote a 69,605,037-byte print PDF embedding 335 font subsets (~200/page) vs
  35 in a clean render; the duplicated subsets shifted pdftotext's word
  segmentation, so the print/web default word multiset differed on 3 topband
  tokens ("LISENT" whole in print, "LISE NT" in web). Isolated re-renders of
  the same SVGs (per-page CairoSVG + pypdf merge, and the full render sequence
  in a fresh process) all produce ~10.9 MB / 35 fonts, and a dedicated
  topband test (`topband_test.py`, print pipeline vs webpdf subset-font pipeline
  on P1) shows the CURRENT topband text extracts identically on both sides —
  so the topband wording was left unchanged and the anomaly is attributed to
  the transient render run under heavy parallel-family CPU contention. Rebuild 3
  re-rendered cleanly: print PDF 10,932,758 bytes, multiset identical.
- **Apostrophe rule applied from the start:** `tr_fr.py` was written with straight
  apostrophes U+0027 throughout (as `\u0027` escapes inside single-quoted
  strings); U+2019 scan over the 8 SVGs is 0. The P1 crop shows "l'Avent"
  rendering tight (no wide full-width glyph).
- **Reconstructed checks (the 3rd baton did both by hand):** `keycheck.py`
  (150-key check) and `freeze_direct.py` (source-AST + rendered-intersection
  freeze proof) are now saved reusable scripts in scratch-fanout-de, both
  validated against the completed de-en edition — freeze-direct reproduces
  de-en's reference counts/sha exactly (147/163/195/166/173/175/150/186).

### Round 3 (rebuild 5 → rebuild 6, boxtitle gate fix; LAYOUT only)
- P1 Fragen subtitle `Les grandes questions　Die Fragen der Woche`: fs 19 → 18
  (`content12.py:69`); ink 1867.5 → 1846.5 (+15.5px margin). No text changed,
  no other line touched. See §6 Rebuild 6.

### D5 font rebuild (2026-11-12 — rebuild 7)

- **Cause**: explanation-layer Latin rendered in Noto Sans CJK instead of Newsreader (SOP §1.1 font table). Pre-D5 census: 637 Latin-in-CJK-Sans elements.
- **Fix (mechanism)**: `apply_variant.py` installed the D5 `_char_font` sans routing on the edition's `svglib.py` (Latin → Newsreader 400/600; fix2 included). No German text, fact, or key changed; no wording changed at all. The D-01 stem (core build15) was already fixed in this edition before the D5 rebuild ("Am Montag öffnet in Köln der erste ___.").
- **Six D5-caused defects, all fixed in source and rebuilt (run2)**:
  1. P1-fussball head `EINE WOCHE, ZWEI STIMMUNGEN` — HEAD TOO WIDE at 25pt; `content12.py:124` 25→22pt (411.8px fits the 422.5px column).
  2. P1 masthead collision — the 46pt headline widened in Newsreader SemiBold and overlapped the right-anchored subtitle `RETOUR DE LA BUNDESLIGA` by 66.8×20.8px (occlusion TEXTX; baseline 0 flags) — the widest of the de family's P1 collisions; `content12.py:27` subtitle 27→22pt (subtitle ink now starts at 1490.5, 10.7px clear of the headline ink at 1479.8). Headline untouched. Same defect class as the en-fr pilot's P1 collision.
  3. P1 cream-box title `DIE WOCHE IN ZAHLEN　En chiffres` — +32.8px past the box; `content12.py:43` `f.box(…, tsize=21)` (399.4px fits 404.5; 22pt still overflows by 14.0px, so 21pt is required — see §6b coverage note).
  4. P1 sommaire title `IN DIESER AUSGABE　Sommaire` — +7.5px; `content12.py:89` 24→22pt (373.5px fits 400.5).
  5. P2 box title `DIE STILLE WOCHE　La semaine` — +7.1px; `content12.py:221` 24→22pt (373.2px fits 400.5).
  6. P8 battery head `F　WÖRTER PAAREN　Associations` — HEAD TOO WIDE at 24pt (444.5px > 422.5px column); `content8.py:149` 24→22pt (407.5px fits).
- **Verification**: full gate re-run (§6b) — census 0, occlusion 0, p8 CLEAN, freeze 8/8, added CJK 0, spill 0, boxtitle 0 (real backup), edge 0, creambox PASS, print/web text layers identical except one raw-mode space (poppler grouping, see §6b).

### Reproof fix rebuild (2026-11-12 — rebuild 8)

- **Cause**: independent reproof of the D5 rebuild found 9 items (F7 major, rest minor) — see `hidden_files/w47/scratch-reproof-w47-de/PROOF-NOTE.md`.
- **Fix (in source, then rebuilt)**: F7 — P1 kicker shortened to `L'ALLEMAND D'ALLEMAGNE` (advance gap 18.4px, P1 render verified); F3 — P2+P6 box title `La semaine` → `La semaine calme` (P2 19pt, P6 24pt); F1 — P5 UND SIE prompt gained the advent-calendar question; F9 — P8 `·` spaced (141 places). Knock-on: P5 image gap 26→14px (image ends 1749.93). Gates: build passes except the pre-existing 1-space raw quirk (`früh→` print vs `früh →` web, poppler grouping, D5-documented; webpdf rebuilt once, persists; non-space chars identical, default text layers 51,088 B identical); boxtitle 0 DEFECT; spill 0 SPILL; edge 0/0; census-patched PASS; head_check PASS; text.md dry-run diff 12 lines, 0 dropped.
- **Verification**: full gate re-run (logs in `hidden_files/w47/scratch-fix-de/logs/`) — see the per-edition entry in `scratch-fix-de/FIX-LOG.md`.
- New deliverables: print 10,352,516 B sha `c0db47831b17…`; web 1,512,555 B sha `a1b12f828e4a…`; text.md 50,367 B sha `9c66b0945bba…`.

### P1 banner F1 fix (2026-11-13 — rebuild 9; de-family independent reproof, worker 4c143a3c)

- **Cause**: de-family independent reproof F1 (light): P1 football-band gloss `RETOUR DE LA BUNDESLIGA` touched the 46pt headline `DIE BUNDESLIGA IST ZURÜCK — BAYERN GEGEN KÖLN!` — text-layer bbox overlap 4.3pt (gloss starts x=1117.9pt, headline ends x=1122.1pt); 150dpi render showed `!` against `R` with no gap. **Corrects the D5 §7 item 2 record**: the D5 fix claimed the 22pt gloss started "10.7px clear of the headline ink (1479.8)" — that measurement missed the `!` ink; the headline ink actually ends at 1496.2px (1122.1pt), so the gloss overlapped, not cleared. Same defect class as de-ru F2 (57.5pt), much lighter.
- **Fix (in source, then rebuilt)**: `content12.py:27` gloss shortened to `RETOUR BUNDESLIGA` (22pt unchanged; dropping `DE LA ` moves the gloss start right by ~57pt). Masthead line (`HEBDO ALLEMAND VOL.4 RETOUR DE LA BUNDESLIGA SEMAINE CALME`, `content12.py:18`) keeps the full phrase; exercise gloss `Retour de la Bundesliga` untouched. No German text, fact, or key changed.
- **Verification**: full gate re-run, all green (logs in `hidden_files/w47/scratch-fix-de-fr2/` — `logs/run.log`, `logs/render.log`, `logs/webpdf.log`, `logs/gates-post.log`, `logs/export.log`): run.py RC 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150; `tools/p8.py` CLEAN vs core-de, keydiff=[137, 138, 139, 150] (same 4 expected items as baseline); `tools/occlusion_audit.py` 0 flags; `tools/boxtitle_check.py` 0 DEFECT, 0 OBSERVE, 1 marginal (same as baseline); `tools/spill_sweep.py` 0 SPILL; `tools/pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `tools/head_check.py` PASS 0 defects (fresh run.log); D5 census PASS (LAT@NotoSans 0, totals identical to baseline); `tools/freeze.py` baseline 8/8 SVGs byte-identical; `verify.py` TOTAL 150, numbering continuous, SVGs byte-identical after re-run, verbatim OK, answers floor OK. Only `svg/p1-front.svg` changed.
- **Text layer**: print/web default mode identical (word multiset + normalised text, 51,085 B each); raw mode same pre-existing 1-space quirk (`früh→` print vs `früh →` web, poppler grouping). Pre/post print text layer differs ONLY by the intended change: non-space chars 40,002 → 39,998 (letters D/E/L/A of `DE LA` removed; the merged token `KÖLN!RETOUR` now extracts as two words `KÖLN!` + `RETOUR`). text.md re-exported from fixed sources (`scratch-fanout-de/export_text_lang.py`, gloss prefix `Note — `, wrap `half`): diff exactly 1 line (L23 `RETOUR DE LA BUNDESLIGA` → `RETOUR BUNDESLIGA`), 591 entries / 150 exercises.
- **P1 banner re-check (150dpi render of the rebuilt print PDF)**: text-layer bbox gap 52.7pt (`KÖLN!` ends 1122.1pt, `RETOUR` starts 1174.9pt); ink gap 117px = 56.2pt between the `!` and the `R` (junction crop `p1-post-junction.png` shows a clear gap).
- New deliverables: print 10,352,509 B sha `0908768c5d2d…`; web 1,512,540 B sha `0adf12460531…`; text.md 50,361 B sha `9d3f973edf72…`.

### fix-de-minor1 (2026-11-13 — round-2 reproof C-1/C-2)

- **Fix (in source, then rebuilt)**: C-1 — P3 lead `die ersten Weihnachtsmärkte` contradicted the Hafenmarkt (open since 13 Nov, same article §2): P3 lead → `zwei große Weihnachtsmärkte` (same length, zero layout shift); the P5 lead carried the identical false claim and was fixed with the same wording; Q34 `Am Montag öffnet in Köln der erste ___.` → `Am Montag öffnen in Köln der Markt am Dom und der Markt der Engel, zwei große ___.` (word-box word and answer key `Weihnachtsmarkt` → `Weihnachtsmärkte`); Q80 `Am 16. November öffnen in Köln die ersten Weihnachtsmärkte.` → `Am 16. November öffnen der Markt am Dom und der Markt der Engel.` (answer stays `Richtig`). Q29 left unchanged (A2-acceptable per the brief; changing it would change the answer key). C-2 — P5 1903 calendar `Die Kinder konnten die Fenster mit Bildern überkleben.` → `Die Kinder konnten die Bilder ausschneiden und auf den Kalender kleben.` (the 1903 Lang/Kepler edition was windowless cut-and-paste). The `überkleben` gloss entry is left in place (the brief's fix is the sentence only; flagged to the coordinator). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p3, p5, p8 (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-fix-de-minor1/2026-w47-de-fr/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 44 titles, 247 body lines, 0 DEFECT, 0 OBSERVE, 1 marginal (P7 `Outils` +1.0px, core same +1.0, pre-existing); spill 0 SPILL / 86 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 0 (reader layer; the shift vs the previous round's count is P3/P5/P8 re-wrap from the longer Q34/Q80 sentences, not content — the multiset proof below is authoritative), added Latin strings 448; print/web text layers multiset-identical (40,049 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: `die ersten`→`zwei große` ×3, `erste`→`Markt am Dom und der Markt der Engel` ×2, `Fenster mit Bildern überkleben`→`Bilder ausschneiden und auf den Kalender kleben`, footer/Q34-key changes where applicable); text.md re-exported from the fixed sources, diff exactly 7 lines (L309 P3 lead, L387 box, L389 Q34, L573 P5 lead, L577 C-2, L693 Q80, L1165 P8 answers Q34 key), 591 entries / 150 exercises. New deliverables: print 10,352,519 B sha `778e605a27dd…`; web 1,512,552 B sha `7a64191d329a…`; text.md 50,430 B sha `13aa1cbded55…`. Not committed / not pushed (coordinator inserts).


### fix-de-round3 (2026-11-13 — round-3 reproof R3-F1/R3-F2)

- **Fix (in source, then rebuilt)**: R3-F1 — the C-2 fix (fix-de-minor1) removed `überkleben` from the P5 1903 sentence but left the orphan gloss entry in the P5 gloss (`content56.py:23`); SOP §8.1 requires every glossed word to occur in the text, so the ` · überkleben …` segment was deleted from the P5 gloss (gloss shortens by one entry, layout-safe). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p5 only (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-reproof-de-round3/2026-w47-de-fr/fix-round3/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 44 titles, 246 body lines, 0 DEFECT, 0 OBSERVE, 1 marginal; spill 0 SPILL / 85 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 0, added Latin strings 447; print/web text layers multiset-identical (40,019 non-space chars each) (byte comparison differs by one extraction space in the P4 answers line, `spät → später` vs `spät →später`; multiset-equal, SVGs byte-identical — extraction artifact, not a content difference; same artifact as pre-fix); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: gloss `überkleben …` entry removed); text.md re-exported from the fixed sources, diff exactly L585 P5 gloss, 591 entries / 150 exercises. New deliverables: print 10,352,491 B sha `4f6ccacfb20e…`; web 1,512,524 B sha `22525742a6bb…`; text.md 50,392 B sha `80f1a96deb47…`. Not committed / not pushed (coordinator inserts).
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
