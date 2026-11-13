# WEEKLY-KIT — 2026-W47 · German edition for Italian-speaking readers

- Edition: `2026-w47-de-it` — German target text, Italian explanations
- Week: Mon 2026-11-16 – Sun 2026-11-22 · VOL.4 · Press time: Mon 2026-11-09
- Lead story: **Die Bundesliga kehrt zurück — Bayern gegen Köln** (40 chars, limit 56)
- Status: fan-out complete, all self-check gates green, visual proofread 8/8 pages
  zero findings (rebuild 3, 2026-11-11; core build15); fix1 rebuild 4 (2026-11-11,
  D1 toolbox-pad fix only, all gates green again); independent proofread pending
  (coordinator to assign).
- **D5 font rebuild applied 2026-11-12 (rebuild 5, all gates green — see §7)**
- Source: `core-de/` (2026-w47-de-zh-cn, build15) copied and translated in the
  explanation layer only. German target text is frozen — see §6 for the proof.
- Builder: de fan-out builder, 5th shift (2026-11-11). Scratch:
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-de/`
  (`tr_it.py`, `transform.py`, `build_edition.py`, `it/` gate logs).

## §1 Contents

8 pages, 1950×2700, 4 columns. **150 exercises**, continuous numbering 1–150, all in
the registry. Identical layout and exercise set to the core; only the explanation
layer (bridges, instructions, glosses, notes, toolbox, disclosure, keys notes) is Italian.

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

Levels: A2 69 / B1 67 / B2 14. Types: scelta multipla 52 / completamento 41 /
trasformazione 11 / vero o falso 8 / testo con buchi 8 / costruzione di frasi 8 /
abbinamento 12 / traduzione 4 / completamento del dialogo 5 / scrittura 1.

Pairing furniture (VOL.4): masthead `Die Lucerna`; edition line
`SETTIMANALE TEDESCO　VOL.4　RITORNA LA BUNDESLIGA　SETTIMANA CALMA`; footer
`Die Lucerna　SETTIMANALE TEDESCO VOL.4　Testo tedesco　Spiegazioni in italiano`;
page line `Pagina N di 8`; gloss prefix `Nota — `.

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
  carries the labelled editor's example + the Italian disclosure:
  "Esempio della redazione: nessuna lettera vera era arrivata prima della chiusura.
  Inviate i vostri testi per il VOL.5!"

## §4 Images

Identical to the core (see `core-de/WEEKLY-KIT.md` §4 and `assets/CREDITS.md`):
fussball.jpg (P1), kopfball.jpg (P4), weihnachtsmarkt1930.jpg — Wilhelm Ritter 1930
(P3), christkind.jpg — Richard Ernst Kepler 1903 (P5), lesesaal.jpg — Carol M.
Highsmith, Library of Congress (P7), fussball1905.jpg (P8). All public domain, each
with target-language caption + printed credit.

## §5 Build / reproduction

- Build dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-de-it/`
  (build code + deliverables, copied from `core-de/` by `transform.py it`).
- Reproduce: `tools/venv/bin/python transform.py it` (from scratch-fanout-de) →
  `tools/venv/bin/python measure.py it <edition-dir>` →
  `tools/venv/bin/python build_edition.py it` (run.py → render.py → webpdf →
  verify → occlusion → p8 → freeze → pdftotext → chips → export).
  Build interpreter is `tools/venv/bin/python` (PIL 13.0.0); freeze was re-run with
  the same interpreter (system python3 has PIL 10.2.0 and measures 1.1% differently).
- Deliverables (fix-de-round3 rebuild, 2026-11-13; reproof fix rebuild, 2026-11-12 superseded):
  - Print PDF: `Die-Lucerna-VOL4-de-it.pdf` — 10,348,832 bytes, 8 pages,
    sha256 `e01bc56325c4b8343f6ac9f5fd67b1ca7f709c0da5be052e1eb9150ec1da3e85`
  - Web PDF: `Die-Lucerna-VOL4-de-it-web.pdf` — 1,508,883 bytes (< 7 MB),
    50,790 text bytes,
    sha256 `87c448ebbc7923ccc4d4b873436dffa6e78b4350ac0de05d48336c3006621d99`
  - Text export: `2026-w47-de-it.text.md` — 50,058 bytes, 48,378 chars,
    591 entries, 150 exercises,
    sha256 `96babe5753bf972378eed6ed6ae8b195b2164720106d608fbe4206e55c21f2cb`
    (changed — wording fixed per the §7 reproof fix entry; re-exported from the fixed sources)
    (exported from production sources in reading order, never from PDF)
  - `ABSTRACT.txt` (one line, Italian, no ASCII double quotes):
    "Die Lucerna Settimanale tedesco VOL.4: torna la Bundesliga (il Bayern ospita
    il Colonia), decisiva di Nations League contro i Paesi Bassi, giorno di
    pentimento e preghiera e domenica dei morti, apertura dei mercatini natalizi
    di Colonia, risultati europei e di Bundesliga dal 3 all'8 novembre; testo in
    tedesco, spiegazioni in italiano, livelli A2–B2, 150 esercizi sui temi della
    settimana."

## §6 Gates (rebuild 4, 2026-11-11 — final)

- `run.py` (build.log): exit 0, **zero FLOW OVERFLOW / HEAD TOO WIDE**, TOTAL 150.
  Flow ends: P1-headline 1554 (= core), P1-fussball 2264, P1-quiz 2523,
  P2-feature 1023, P2-ex 2332, P3-main 916, P3-ex 2333, P4-main 677, P4-ex 2315,
  P5-main 1026, P5-ex 2441 (= core), P6-main 777, P6-ex 2523, P7-A2 1278 / B1 1342 /
  B2 1306, P8-battery 1409, P8-keys 2442 (bottom 2560, spare 118px).
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
  **Direct freeze proof (8/8, `it/freeze-direct.json`, script `freeze_direct.py`):**
  (a) source-level: AST string-literal multiset core vs edition — 0 unaccounted
  removed, 0 unaccounted added (520 removed / 528 added, every one accounted for
  by the translation module, the CJK inventory, or a documented transform artifact);
  (b) rendered-text level: the frozen intersection (strings identical in core and
  edition SVGs) per page — P1 147, P2 163, P3 195, P4 166, P5 173, P6 175, P7 150,
  P8 186 strings, sha256 083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 /
  2bbe05f9 / b7aa0771 / 57e118e7 — identical to de-en, de-fr and de-es, as the frozen
  content is the shared German text.
- Print/web text layer: `pdftotext` default mode — print 50,592B / web 50,592B,
  **word multiset identical**; `-raw` mode — both 49,392B, normalised text
  **exactly identical**. Web PDF has a real text layer.
- Level chips (rx="2.7" rects): per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18,
  7:12, 8:35}, **TOTAL 141**; P8 by level A2 22 / B1 13 / B2 0. The core's
  missing-14 set is fully present: cloze options Q113–120 (8 A2 chips),
  dialogue badges Q145–149 (145–147 A2, 148 B1, 149 A2), writing title chip
  (B1 on "H SCHREIBEN").
- P8 answers measured font size: keys 13.25 SVG units = **9.94 PDF pt**
  (PyMuPDF re-measured P8 minimum span 9.94pt) — above the 9.75pt floor
  (concession step 4; P8 stems stay at the core's 15.375pt).
- 150-question key check (independent, `it/keycheck-150.json`, script
  `keycheck.py`): P8-SVG-extracted keys vs the REG built from the edition's own
  sources — **149/150 exact**; the single non-exact item is Q150, the open
  writing task, where the extractor truncates the REG key "Esercizio libero —
  segui i punti del riquadro di scrittura" to "Esercizio libero" (expected; Q150
  is already in the keydiff set). REG by page
  {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}; levels A2 69 / B1 67 / B2 14.
- U+2019 scan over the 8 SVGs: **0** (straight U+0027 throughout, as `\u0027`
  escapes in `tr_it.py` — e.g. "l'Avvento", "d'Avvento", "c'è" render tight).
- Visual proofread: all 8 pages re-rendered from the print PDF at 100 dpi and
  viewed one by one (P1–P8), plus a systematic SVG-level scan of the 7 col3
  box titles (8 instances incl. the P6 full-width box): all end ≤ 1862.0
  (max 1856.5, NOCH EIN WORT, 5.5px margin). **Zero findings** (see §7). The P8
  keys were spot-checked against the registry (dates, scores, times, grammar keys,
  MUSTER 84 words, chart 44+33+23=100).

## §6b Gates (D5 font rebuild round, rebuild 5, 2026-11-12 — full re-run on the rebuilt edition; scratch `hidden_files/w47/scratch-d5-de/de-it/`)

- D5 mechanism: `apply_variant.py --svglib … --target de --reader it` (mode latin) on the edition's `svglib.py`; fix2 curly-quote routing installed with it (routing assert `ROUTING FAILURES: 0`). Pre-D5 `svglib.py` backed up as `svglib.py.pre-d5`. Pre-D5 baseline verified CLEAN before install: the production dir was copied to scratch and rebuilt with the venv interpreter — freeze baseline **8/8 SVGs byte-identical** to the delivered SVGs (`freeze-pre-baseline.log`). Pre-D5 production snapshot in `scratch-d5-de/de-it/baseline/` (SVGs + sources, rebuild-4 state). KIT wave 2 check: pre-D5 print SHA matches the KIT (`ca802fb8…`), but the pre-D5 web PDF on disk was sha `20321311…` (1,596,994 B), NOT the KIT's rebuild-4 record `09fb2470…` — the rebuild-4 web PDF had been rebuilt without a KIT sync (same class as de-en/de-fr). The D5 values above are measured from the actual files on disk.
- Pre-D5 D5 census: **632 Latin-in-CJK-Sans elements** (matches D5-CENSUS-130); quotes defective 0; p8 extract 150/150.
- `run.py` (run2): TOTAL **150**, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`tools/head_check.py`: PASS 0 defects).
- `mechanism/d5_census.py`: **PASS — D5 Latin 0, D5 Cyrillic 0, curly-in-CJK 0**.
- `tools/occlusion_audit.py`: **0 flags** (selftest OK; fixed tool — bare `Noto Sans` runs measured on the non-CJK face, brief §10).
- `tools/p8.py`: extract 150/150; compare vs rebuilt core-de P8: `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]` — the same 4 expected reader-language items as rebuild 4.
- `tools/freeze.py`: baseline **8/8 SVGs byte-identical** (venv Pillow 13.0.0 / FreeType 2.14.3); diff pre-D5 baseline vs rebuilt: **added CJK characters 0** (added Latin strings 355 = D5 run-splitting).
- `tools/spill_sweep.py`: 32 boxes, 83 candidates, **0 SPILL**, 83 OBSERVE.
- `tools/boxtitle_check.py`: 44 titles, 248 body lines, **0 DEFECT**, 0 OBSERVE, 0 marginal (real backup comparison: `scratch-d5-de/scratch-fanout-de/backup/2026-w47-de-it`). Coverage note: two fixed titles sit below the tool's 22pt detection floor (P7 `Attrezzi` 21pt, P7 `Ancora una parola` 20pt) — they are verified instead by the creambox audit (0 defects across all 32 boxes) and by direct ink measurement (spare 13.2px / 20.3px).
- `tools/pdf_edge_scan.py`: 8 pages, **0 TOUCH, 0 NEAR**.
- `tools/d5_creambox_audit.py` (pre-D5 baseline vs rebuilt): **PASS 0 defects**; ratios n=540, median 1.012, bold 1.049 / regular 0.982; P8 lines 230→229, footer slack 33.6→33.6px.
- Web/print text layer: `pdftotext` default mode — both **50,440 bytes**, word multiset identical, normalised text exactly identical; `-raw` mode — both 49,385 bytes, identical.

## §7 Fan-out changes (explanation layer only — no German text, fact or key changed)

### Rebuild 3 (2026-11-11 — core build15 Q34 change only)
- **Q34 stem change (the reason for this rebuild):** core-de build15 changed the
  P3 exercise Q34 stem from plural "Am Montag öffnen in Köln die ersten ___."
  to singular "Am Montag öffnet in Köln der erste ___." (key `Weihnachtsmarkt`
  unchanged). The edition was deleted and re-transformed from the new core.
  Verified: new stem 1x / old stem 0x in source, .text.md, P3 SVG, and both
  PDF text layers. P3 freeze sha changed accordingly (093cf378 → fc88f676);
  all other pages byte-identical to rebuild 2.
- No box-title changes this round (boxtitle.py 7/7 as-is); the rebuild-2 P1
  ZAHLEN fix ("(Bayern-Colonia 20.30)") is preserved.
- New deliverables: print 10,965,095 B sha 0d7be581…; web 1,553,872 B
  sha dbbe5880…; text.md 49,712 B sha 1594ba08…. All gates green;
  P8 keys end 2442, flow ends otherwise identical to rebuild 2.

### Rebuild 4 (2026-11-11 — fix1, D1 only)
- **D1 (de-es proof1 family defect, reproduced on it pre-fix):** P7
  DER WERKZEUGKASTEN cream box too short — box bottom 783.5, last entry
  `Es ist fraglich, ob ... = ancora dubbio` baseline 783.9 (clearance −0.4),
  `fraglich` descender ink ~4.7 below the box. Root cause (measured per-edition):
  the `tbh` formula in `content7.py:76` counts `n*29.5+6` per entry but the real
  advance is `20.5 + n*29.11 + 6` (`Page.para` first-baseline offset, 6 entries =
  +123 missed); it wraps Σlines=9, so clearance = pad − 90.4 and pad 90 gave −0.4.
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
  byte-identical (sha 1594ba08…); freeze_direct 8/8 with all 8 page shas identical
  to rebuild 3 (083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 /
  b7aa0771 / 57e118e7).
- New deliverables: print 10,965,087 B (−8 B) sha
  `ca802fb853eb3f18c61cddd5da406c72c9c0471cabd84c76731478f4cdf6f2c0`; web 1,596,994 B
  (+43,122 B — working-tree webpdf.py now embeds the `LucernaNewsreader-Bold` subset,
  23,444 B; same effect as es/fr/pt/ko/zh-tw; < 7 MB, text layer identical to print) sha
  `09fb247059a96c37c0fa1fe0178b7dacf35cd1e5500fe6f089b929c722c82300`; text.md 49,712 B
  sha 1594ba08… (unchanged). All gates green (occlusion 0 flags real run, p8 CLEAN
  keydiff [137,138,139,150], freeze diff +7 CJK all U+3000, freeze_direct 8/8 source
  PASS, keycheck 149/150 — Q150 extractor truncation only, boxtitle 7/7, d2scan 58
  pairs 0 web gaps >0.5pt, P8 min 9.94pt, chips 141, verify TOTAL 150, bent quotes
  U+201C 33 / U+201D 0, Q34 new stem 1x in all five places). Gate logs in
  `hidden_files/w47/scratch-fix-de-toolbox-family/gates-it/` (freeze_direct/boxtitle/
  keycheck run from `scratch-fanout-de-rebuild-A/`, which holds the current `tr_it.py`);
  build logs in `hidden_files/w47/scratch-fanout-de/it/`.

### Round 1 (build 1 → rebuild 2, one value fix)
- Build 1 failed 3 gates with ONE root cause on P1: FLOW OVERFLOW [P1-headline]
  col 2 y=1835 need 75 (flow ended 1921, bottom 1828) + occlusion LINEX ×2
  (Q6 'B1' chip and '6.' crossing the row-B hline at y=1844). Diagnosis (SVG
  measurement): the ZAHLEN box is 362px tall in it vs 334px in es — its item 2
  wrapped to 3 lines ("Freitagabend (Bayern-Colonia, ore / 20.30)") instead of 2,
  so the box no longer fit col 1's remaining space after the gloss and jumped to
  col 2, pushing JETZT ÜBEN down 362px into the image row (same class as fr
  build 1's ZAHLEN box jump).
- Fix (in `vals_it.json`, regenerated `tr_it.py` — diff exactly 1 line):
  ZAHLEN item 2 "(Bayern-Colonia, ore 20.30)" → "(Bayern-Colonia 20.30)"
  (drops ", ore"; 2 lines at the 378.5px inner width). Box back to ~334px;
  P1-headline ends 1554 = core.
- Build 2: ALL GATES PASS + visual proofread P1–P8 zero findings.
- **Apostrophe rule applied from the start:** `tr_it.py` was written with straight
  apostrophes U+0027 throughout (as `\u0027` escapes inside single-quoted
  strings); U+2019 scan over the 8 SVGs is 0. The P1 crop shows "l'Avvento"
  rendering tight (no wide full-width glyph).
- Box titles (from the 5th-baton sweep, before build 1): STILLE "La settimana
  tranquilla" → "Tranquilla"; WEIHNACHTSWÖRTER "Parole di Natale" → "Parole";
  TIPP "Il consiglio della redazione" → "Consiglio"; ADVENTSWÖRTER "Parole
  dell'Avvento" → "Avvento" (boxtitle.py 7/7).

### D5 font rebuild (2026-11-12 — rebuild 5)

- **Cause**: explanation-layer Latin rendered in Noto Sans CJK instead of Newsreader (SOP §1.1 font table). Pre-D5 census: 632 Latin-in-CJK-Sans elements.
- **Fix (mechanism)**: `apply_variant.py` installed the D5 `_char_font` sans routing on the edition's `svglib.py` (Latin → Newsreader 400/600; fix2 included). No German text, fact, or key changed; no wording changed at all.
- **Six D5-caused defects, all fixed in source and rebuilt (run2)**:
  1. P1-fussball head `EINE WOCHE, ZWEI STIMMUNGEN` — HEAD TOO WIDE at 25pt; `content12.py:124` 25→22pt (411.8px fits the 422.5px column).
  2. P1 sommaire title `IN DIESER AUSGABE　Sommario` — +8.5px; `content12.py:89` 24→22pt (375.2px fits 400.5).
  3. P7 toolbox title `DER WERKZEUGKASTEN　Attrezzi` — +24.0px; `content7.py:79` 23→21pt (387.3px fits 400.5; 22pt still overflows by 5.2px).
  4. P7 box title `NOCH EIN WORT　Ancora una parola` — +17.6px; `content7.py:105` 22→20pt (380.2px fits 400.5; 21pt leaves only 1.3px spare).
  5. P8 battery head `A　LÜCKENTEXT　Testo con buchi` — HEAD TOO WIDE at 24pt (433.3px > 422.5px column); `content8.py:78` 24→22pt (397.2px fits).
  6. P8 battery head `F　WÖRTER PAAREN　Abbinamenti` — HEAD TOO WIDE at 24pt (450.9px > 422.5px column); `content8.py:149` 24→22pt (413.4px fits).
- **Verification**: full gate re-run (§6b) — census 0, occlusion 0, p8 CLEAN, freeze 8/8, added CJK 0, spill 0, boxtitle 0 (real backup), edge 0, creambox PASS, print/web text layers identical in both modes.
- Note: the P1 box title `DIE WOCHE IN ZAHLEN　In cifre` fits as-is (short Italian tail), and the P1 masthead subtitle never collided with the headline in this edition.

### Reproof fix rebuild (2026-11-12 — rebuild 8)

- **Cause**: independent reproof of the D5 rebuild found 9 items (F7 major, rest minor) — see `hidden_files/w47/scratch-reproof-w47-de/PROOF-NOTE.md`.
- **Fix (in source, then rebuilt)**: F7 — P1 kicker shortened to `IL TEDESCO DEI TEDESCHI` (advance gap 23.6px, P1 render verified); F8 — P1 banner `TORNA LA BUNDESLIGA` 27→24pt (ink gap 38.8px, 1 empty PNG column); F1 — P5 UND SIE prompt gained the advent-calendar question; F9 — P8 `·` spaced (142 places). Knock-on: P5 image gap 26→14px (image ends 1749.93). Gates: build ALL GATES PASS; boxtitle 0 DEFECT; spill 0 SPILL; edge 0/0; census-patched PASS; head_check PASS; text.md dry-run diff 10 lines, 0 dropped.
- **Verification**: full gate re-run (logs in `hidden_files/w47/scratch-fix-de/logs/`) — see the per-edition entry in `scratch-fix-de/FIX-LOG.md`.
- New deliverables: print 10,348,810 B sha `c6643394c3c5…`; web 1,508,853 B sha `352bd66ae305…`; text.md 50,025 B sha `2bc2080597e1…`.

### fix-de-minor1 (2026-11-13 — round-2 reproof C-1/C-2)

- **Fix (in source, then rebuilt)**: C-1 — P3 lead `die ersten Weihnachtsmärkte` contradicted the Hafenmarkt (open since 13 Nov, same article §2): P3 lead → `zwei große Weihnachtsmärkte` (same length, zero layout shift); the P5 lead carried the identical false claim and was fixed with the same wording; Q34 `Am Montag öffnet in Köln der erste ___.` → `Am Montag öffnen in Köln der Markt am Dom und der Markt der Engel, zwei große ___.` (word-box word and answer key `Weihnachtsmarkt` → `Weihnachtsmärkte`); Q80 `Am 16. November öffnen in Köln die ersten Weihnachtsmärkte.` → `Am 16. November öffnen der Markt am Dom und der Markt der Engel.` (answer stays `Richtig`). Q29 left unchanged (A2-acceptable per the brief; changing it would change the answer key). C-2 — P5 1903 calendar `Die Kinder konnten die Fenster mit Bildern überkleben.` → `Die Kinder konnten die Bilder ausschneiden und auf den Kalender kleben.` (the 1903 Lang/Kepler edition was windowless cut-and-paste). The `überkleben` gloss entry is left in place (the brief's fix is the sentence only; flagged to the coordinator). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p3, p5, p8 (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-fix-de-minor1/2026-w47-de-it/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 44 titles, 249 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal; spill 0 SPILL / 85 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 0 (reader layer; the shift vs the previous round's count is P3/P5/P8 re-wrap from the longer Q34/Q80 sentences, not content — the multiset proof below is authoritative), added Latin strings 442; print/web text layers multiset-identical (40,064 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: `die ersten`→`zwei große` ×3, `erste`→`Markt am Dom und der Markt der Engel` ×2, `Fenster mit Bildern überkleben`→`Bilder ausschneiden und auf den Kalender kleben`, footer/Q34-key changes where applicable); text.md re-exported from the fixed sources, diff exactly 7 lines (L309 P3 lead, L387 box, L389 Q34, L573 P5 lead, L577 C-2, L693 Q80, L1165 P8 answers Q34 key), 591 entries / 150 exercises. New deliverables: print 10,348,855 B sha `b216b06d0bf8…`; web 1,508,908 B sha `2d1334a908ee…`; text.md 50,094 B sha `96fb4d54ca3c…`. Not committed / not pushed (coordinator inserts).


### fix-de-round3 (2026-11-13 — round-3 reproof R3-F1/R3-F2)

- **Fix (in source, then rebuilt)**: R3-F1 — the C-2 fix (fix-de-minor1) removed `überkleben` from the P5 1903 sentence but left the orphan gloss entry in the P5 gloss (`content56.py:23`); SOP §8.1 requires every glossed word to occur in the text, so the ` · überkleben …` segment was deleted from the P5 gloss (gloss shortens by one entry, layout-safe). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p5 only (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-reproof-de-round3/2026-w47-de-it/fix-round3/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 44 titles, 248 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal; spill 0 SPILL / 84 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 0, added Latin strings 441; print/web text layers multiset-identical (40,035 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: gloss `überkleben …` entry removed); text.md re-exported from the fixed sources, diff exactly L585 P5 gloss, 591 entries / 150 exercises. New deliverables: print 10,348,832 B sha `e01bc56325c4…`; web 1,508,883 B sha `87c448ebbc79…`; text.md 50,058 B sha `96babe5753bf…`. Not committed / not pushed (coordinator inserts).
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
