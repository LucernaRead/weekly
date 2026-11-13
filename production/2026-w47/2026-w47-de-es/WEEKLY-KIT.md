# WEEKLY-KIT — 2026-W47 · German edition for Spanish-speaking readers

- Edition: `2026-w47-de-es` — German target text, Spanish explanations
- Week: Mon 2026-11-16 – Sun 2026-11-22 · VOL.4 · Press time: Mon 2026-11-09
- Lead story: **Die Bundesliga kehrt zurück — Bayern gegen Köln** (40 chars, limit 56)
- Status: fan-out complete, all self-check gates green, visual proofread 8/8 pages
  zero findings (rebuild 4, 2026-11-11; core build15); independent proof1 (2026-11-11)
  found 1 defect (D1, P7 toolbox box too short, see §6); fix1 rebuild 5 (2026-11-11)
  repaired D1 only, all gates green again; independent proof2 pending (coordinator to assign).
  New standing gates (2026-11-12) found 1 boxtitle defect (P1 Fragen subtitle
  +8.5px, see §6); rebuild 6 (2026-11-12) repaired it by layout only, all gates
  green again.
- **D5 font rebuild applied 2026-11-12 (rebuild 7, all gates green — see §7)**
- Source: `core-de/` (2026-w47-de-zh-cn, build15) copied and translated in the
  explanation layer only. German target text is frozen — see §6 for the proof.
- Builder: de fan-out builder, 5th shift (2026-11-11). Scratch:
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-de/`
  (`tr_es.py`, `transform.py`, `build_edition.py`, `es/` gate logs).

## §1 Contents

8 pages, 1950×2700, 4 columns. **150 exercises**, continuous numbering 1–150, all in
the registry. Identical layout and exercise set to the core; only the explanation
layer (bridges, instructions, glosses, notes, toolbox, disclosure, keys notes) is Spanish.

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

Levels: A2 69 / B1 67 / B2 14. Types: opción múltiple 52 / completar 41 /
transformación 11 / verdadero o falso 8 / texto con huecos 8 / construir frases 8 /
emparejar palabras 12 / traducción 4 / completar el diálogo 5 / redacción 1.

Pairing furniture (VOL.4): masthead `Die Lucerna`; edition line
`SEMANARIO ALEMÁN　VOL.4　VUELVE LA BUNDESLIGA　SEMANA TRANQUILA`; footer
`Die Lucerna　SEMANARIO ALEMÁN VOL.4　Texto alemán　Explicaciones en español`;
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
  carries the labelled editor's example + the Spanish disclosure:
  "Ejemplo de la redacción: no llegó ninguna carta real antes del cierre. ¡Envía
  tus textos para el VOL.5!"

## §4 Images

Identical to the core (see `core-de/WEEKLY-KIT.md` §4 and `assets/CREDITS.md`):
fussball.jpg (P1), kopfball.jpg (P4), weihnachtsmarkt1930.jpg — Wilhelm Ritter 1930
(P3), christkind.jpg — Richard Ernst Kepler 1903 (P5), lesesaal.jpg — Carol M.
Highsmith, Library of Congress (P7), fussball1905.jpg (P8). All public domain, each
with target-language caption + printed credit.

## §5 Build / reproduction

- Build dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-de-es/`
  (build code + deliverables, copied from `core-de/` by `transform.py es`).
- Reproduce: `tools/venv/bin/python transform.py es` (from scratch-fanout-de) →
  `tools/venv/bin/python measure.py es <edition-dir>` →
  `tools/venv/bin/python build_edition.py es` (run.py → render.py → webpdf →
  verify → occlusion → p8 → freeze → pdftotext → chips → export).
  Build interpreter is `tools/venv/bin/python` (PIL 13.0.0); freeze was re-run with
  the same interpreter (system python3 has PIL 10.2.0 and measures 1.1% differently).
- Deliverables (fix-de-round3 rebuild, 2026-11-13; reproof fix rebuild, 2026-11-12 superseded):
  - Print PDF: `Die-Lucerna-VOL4-de-es.pdf` — 10,354,441 bytes, 8 pages,
    sha256 `07f87aa040311a5ed8da0fc636b339f5f60b6ab6d4c600dd85918bc51ea0d257`
  - Web PDF: `Die-Lucerna-VOL4-de-es-web.pdf` — 1,514,482 bytes (< 7 MB),
    51,215 text bytes,
    sha256 `8e27d9c5f9353327de68d70e06a45bd192662246d85080ecd0747d425203e6a8`
  - Text export: `2026-w47-de-es.text.md` — 50,467 bytes, 48,628 chars,
    591 entries, 150 exercises,
    sha256 `ec37787fa1d5d9ec56d962bf10e0b864227799c5908c3df4dd98fc2e2d599369`
    (changed — wording fixed per the §7 reproof fix entry; re-exported from the fixed sources)
    (exported from production sources in reading order, never from PDF)
  - `ABSTRACT.txt` (one line, Spanish, no ASCII double quotes):
    "Die Lucerna Semanario alemán VOL.4: vuelve la Bundesliga (el Bayern recibe al
    Colonia), decisiva de la Nations League contra los Países Bajos, día de
    arrepentimiento y oración y domingo de los difuntos, apertura de los mercados
    navideños de Colonia, resultados europeos y de la Bundesliga del 3 al 8 de
    noviembre; texto en alemán, explicaciones en español, niveles A2–B2, 150
    ejercicios sobre los temas de la semana."

## §6 Gates (rebuild 5, 2026-11-11 — final)

- `run.py` (build.log): exit 0, **zero FLOW OVERFLOW / HEAD TOO WIDE**, TOTAL 150.
  Flow ends: P1-headline 1554 (= core), P1-fussball 2264, P1-quiz 2523,
  P2-feature 1023, P2-ex 2332, P3-main 916, P3-ex 2333, P4-main 677, P4-ex 2315,
  P5-main 1026, P5-ex 2441 (= core), P6-main 777, P6-ex 2523, P7-A2 1278 / B1 1374 /
  B2 1306, P8-battery 1409, P8-keys 2457 (bottom 2560, spare 103px).
- `measure.py`: **24/24 PASS, 0 FAIL** (measure3.log).
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
  **Direct freeze proof (8/8, `es/freeze-direct.json`, script `freeze_direct.py`):**
  (a) source-level: AST string-literal multiset core vs edition — 0 unaccounted
  removed, 0 unaccounted added (520 removed / 528 added, every one accounted for
  by the translation module, the CJK inventory, or a documented transform artifact);
  (b) rendered-text level: the frozen intersection (strings identical in core and
  edition SVGs) per page — P1 147, P2 163, P3 195, P4 166, P5 173, P6 175, P7 150,
  P8 186 strings, sha256 083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 /
  2bbe05f9 / b7aa0771 / 57e118e7 — identical to de-en and de-fr, as the frozen content is
  the shared German text.
- Print/web text layer: `pdftotext` default mode — print 51,011B / web 51,011B,
  **word multiset identical**; `-raw` mode — both 49,812B, normalised text
  **exactly identical**. Web PDF has a real text layer.
- Level chips (rx="2.7" rects): per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18,
  7:12, 8:35}, **TOTAL 141**; P8 by level A2 22 / B1 13 / B2 0. The core's
  missing-14 set is fully present: cloze options Q113–120 (8 A2 chips),
  dialogue badges Q145–149 (145–147 A2, 148 B1, 149 A2), writing title chip
  (B1 on "H SCHREIBEN").
- P8 answers measured font size: keys 13.25 SVG units = **9.94 PDF pt**
  (PyMuPDF re-measured P8 minimum span 9.94pt) — above the 9.75pt floor
  (concession step 4; P8 stems stay at the core's 15.375pt).
- 150-question key check (independent, `es/keycheck-150.json`, script
  `keycheck.py`): P8-SVG-extracted keys vs the REG built from the edition's own
  sources — **149/150 exact**; the single non-exact item is Q150, the open
  writing task, where the extractor truncates the REG key "Tarea libre — sigue
  los puntos del recuadro de escritura" to "Tarea libre" (expected; Q150 is
  already in the keydiff set). REG by page
  {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}; levels A2 69 / B1 67 / B2 14.
- U+2019 scan over the 8 SVGs: **0** (straight U+0027 throughout, as `\u0027`
  escapes in `tr_es.py`).
- Visual proofread: all 8 pages re-rendered from the print PDF at 100 dpi and
  viewed one by one (P1–P8), plus a systematic SVG-level scan of the 7 col3
  box titles (8 instances incl. the P6 full-width box): all end ≤ 1862.0
  (max 1849.1). **Zero findings** (see §7). The P8 keys were spot-checked
  against the registry (dates, scores, times, grammar keys, MUSTER 84 words,
  chart 44+33+23=100).

### Rebuild 4 (2026-11-11 — core build15 Q34 change only)
- **Q34 stem change (the reason for this rebuild):** core-de build15 changed the
  P3 exercise Q34 stem from plural "Am Montag öffnen in Köln die ersten ___."
  to singular "Am Montag öffnet in Köln der erste ___." (key `Weihnachtsmarkt`
  unchanged). The edition was deleted and re-transformed from the new core.
  Verified: new stem 1x / old stem 0x in source, .text.md, P3 SVG, and both
  PDF text layers. P3 freeze sha changed accordingly (093cf378 → fc88f676);
  all other pages byte-identical to rebuild 3.
- No box-title changes this round: the five titles shortened in rebuild 3
  (Tranquila / Consejo / Adviento / Útiles / Cartas) re-verified 7/7.
- New deliverables: print 10,968,803 B sha 7bc39e1f…; web 1,558,821 B
  sha cd453143…; text.md 50,124 B sha 5f5ea69b…. All gates green;
  P8 keys end 2457, flow ends otherwise identical to rebuild 3.

### Rebuild 5 (2026-11-11 — fix1, D1 only)
- **D1 (proof1):** P7 DER WERKZEUGKASTEN cream box too short — box bottom 783.5,
  last entry `Es ist fraglich, ob ... = aún dudoso` baseline 783.9 (clearance −0.4),
  `fraglich` descender ink ~4.7 below the box. Root cause (measured): the `tbh`
  formula in `content7.py:76` counts `n*29.5+6` per entry but the real advance is
  `20.5 + n*29.11 + 6` (`Page.para` first-baseline offset, 6 entries = +123 missed);
  clearance = pad − 90.4 for es (9 lines). Core-de uses pad 110 (+18.8); the fan-out
  had cut it to 90 with a "validated by occlusion 0 flags" comment — void, since the
  occlusion audit cannot see text spilling past its own box (nothing covers it).
- **Fix (edition-local, `content7.py:76` only):** pad 90 → 110 (restores the core value),
  comment rewritten with the arithmetic. No shared helper touched. Predicted and
  verified: toolbox bottom 783.5 → **803.5**, clearance **+19.6**; LESERBRIEFE
  y 799.5 → 819.5 (16px gap preserved, +10.4 unchanged); NOCH EIN WORT ends 1518.0 →
  **1538.0** (10px before the 1548 Sätze rule, +42.9 unchanged). No text changed:
  text.md byte-identical (sha 5f5ea69b…); freeze_direct 8/8 with all 8 page shas
  identical to rebuild 4.
- **Family sweep (fix1, read-only creambox on all 9 siblings' P7):** all 9 have the
  defect in ink terms — en/fr/it −0.4 (same geometry as es), pt/nl/ru +0.0 (baseline
  exactly on the box edge, descender still spills), ja/ko/zh-tw −0.8. Pad 110 would
  give +19.2…+20.0 everywhere, BUT pt/nl/ru end NOCH EIN WORT at 1547.5 today — a flat
  +20 would cross the 1548 rule there, so those three need their own fix design.
  Coordinator to decide the family rollout; de-en fix1 runs in parallel (same geometry
  as es, pad 110 works cleanly there). Detail in `scratch-fix-de-es1/FIX-LOG.md` §6.
- New deliverables: print 10,968,798 B (−5 B) sha `6e8bde3f30a6dcb415321051d0a9f1a19f3a5c033d0167b80215a969aa69077e`;
  web 1,601,888 B (+43,067 B — working-tree webpdf.py now embeds the
  `LucernaNewsreader-Bold` subset, 24,224 B; same effect as pt/ko/zh-tw; < 7 MB,
  text layer identical to print) sha `f43d561a2e54de16ffd194ea5f05b1ad9c6c44ef6d60809324cc73e2dfd28d7e`;
  text.md 50,124 B sha 5f5ea69b… (unchanged). All gates green (occlusion 0 flags
  real run, p8 CLEAN keydiff [137,138,139,150], freeze 8/8, keycheck 149/150, boxtitle
  7/7, chips 141, P8 min 9.94pt, d2scan 0 web gaps >0.5pt); P7 visual (100 dpi + 300 dpi
  toolbox zoom, print; web zoom pixel-identical) confirms the last entry fully inside
  the cream box. Q34 new stem 1× / old 0× in all five places (no regression).
  Gate outputs in `scratch-fix-de-es1/GATE-LOG.md`.

### Rebuild 6 (2026-11-12 — boxtitle gate fix, P1 only)
- **Defect (new standing gate `tools/boxtitle_check.py`, 130-wide run
  2026-11-12):** P1 Fragen subtitle `Las grandes preguntas　Die Fragen der
  Woche` ran past its cream box by **+8.5px** (core-de fits at −22.0px);
  visually confirmed (line end on white paper past the box edge).
- **Fix (edition-local, `content12.py:69` only):** subtitle font size 19 → 18
  (layout only, no text changed). Predicted and verified: ink end
  1870.5 → **1849.5**, margin **+12.5px**. No other line touched.
- New deliverables: print 10,968,799 B (+1 B) sha
  `a255aa6b268d54ac861759a2c459ca4f673aeb9a72f37f7af1153ebfc5e06deb`; web
  1,601,884 B (−4 B) sha
  `682fd0d0ef1eaeea704cbc56e2159b4ca23d58cf42cbcb59bcff12ac0ad0558d`;
  text.md 50,124 B sha 5f5ea69b… (unchanged). All gates green on the rebuilt
  edition: boxtitle **0 DEFECT / 0 OBSERVE / 0 marginal** (also 0 on the synced
  production files), verify TOTAL 150 + SVGs byte-identical after re-run,
  occlusion 0 flags, p8 extract 150/150 + compare CLEAN keydiff
  [137,138,139,150], freeze `diff` exit 0 (added CJK 7, all U+3000) +
  freeze-direct rendered **8/8** with all 8 frozen SHAs identical to rebuild 5.
  P1 visual crop confirms the subtitle ends inside the cream box.
  NOTE (pre-existing, not this fix): freeze-direct *source* level reports 1
  unaccounted removed literal (`'sans'` ×2 in `svglib.py`) — core-de's
  `svglib.py` was patched (fix2 U+201C routing, 2026-11-11 22:35) after de-es
  was copied from it (08:20); the edition's `svglib.py` is the older copy.
  No string literal was changed by this fix (fs int + comment only).
  Gate outputs in `scratch-gatefix-de-en/de-es/` (FIX-LOG.md).
  Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-gatefix-de-en/`.

## §6b Gates (D5 font rebuild round, rebuild 7, 2026-11-12 — full re-run on the rebuilt edition; scratch `hidden_files/w47/scratch-d5-de/de-es/`)

- D5 mechanism: `apply_variant.py --svglib … --target de --reader es` (mode latin) on the edition's `svglib.py`; fix2 curly-quote routing installed with it (routing assert `ROUTING FAILURES: 0`). Pre-D5 `svglib.py` backed up as `svglib.py.pre-d5`; pre-D5 production snapshot in `scratch-d5-de/de-es/baseline/` (SVGs + sources, rebuild-6 state). KIT wave 2 check: pre-D5 on-disk SHAs match the KIT's rebuild-6 record (print `a255aa6b…`, web `682fd0d0…`).
- Pre-D5 D5 census: **636 Latin-in-CJK-Sans elements** (matches D5-CENSUS-130); quotes defective 0; p8 extract 150/150.
- `run.py` (run2): TOTAL **150**, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`tools/head_check.py`: PASS 0 defects).
- `mechanism/d5_census.py`: **PASS — D5 Latin 0, D5 Cyrillic 0, curly-in-CJK 0**.
- `tools/occlusion_audit.py`: **0 flags** (selftest OK; fixed tool — bare `Noto Sans` runs measured on the non-CJK face, brief §10).
- `tools/p8.py`: extract 150/150; compare vs rebuilt core-de P8: `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]` — the same 4 expected reader-language items as rebuild 5.
- `tools/freeze.py`: baseline **8/8 SVGs byte-identical** (venv Pillow 13.0.0 / FreeType 2.14.3); diff pre-D5 baseline vs rebuilt: **added CJK characters 0** (added Latin strings 357 = D5 run-splitting).
- `tools/spill_sweep.py`: 32 boxes, 83 candidates, **0 SPILL**, 83 OBSERVE.
- `tools/boxtitle_check.py`: 48 titles, 243 body lines, **0 DEFECT**, 0 OBSERVE, 0 marginal (real backup comparison: `scratch-d5-de/scratch-fanout-de/backup/2026-w47-de-es`).
- `tools/pdf_edge_scan.py`: 8 pages, **0 TOUCH, 0 NEAR**.
- `tools/d5_creambox_audit.py` (pre-D5 baseline vs rebuilt): **PASS 0 defects**; ratios n=545, median 1.007, bold 1.040 / regular 0.977; P8 lines 230→230, footer slack 33.6→32.6px.
- Web/print text layer: `pdftotext` default mode — both **50,873 bytes**, word multiset identical, normalised text exactly identical; `-raw` mode — both 49,805 bytes, identical. (Rebuild 6 was 51,011 bytes; the −138 bytes are whitespace/line-break grouping from reflowed runs, zero word characters lost.)

## §7 Fan-out changes (explanation layer only — no German text, fact or key changed)

### Round 1 (build 1 → build 2, value fixes + LAYOUT)
- Build 1 failed 3 gates: P8-battery F head too wide ("F　WÖRTER PAAREN　Palabras
  emparejadas", 525.6px > CW 422.5) + occlusion 4 flags (P3 WEIHNACHTSWÖRTER title
  ink to 1987.75; P7 DER WERKZEUGKASTEN title to 1994.75; P8 same F head to 1965.0;
  P3 LINEX — tip 3rd line baseline 1623.66 crossed the exercise rule at y=1608).
- Fixes: P3 title → "WEIHNACHTSWÖRTER　Palabras"; toolbox →
  "DER WERKZEUGKASTEN　Herramientas"; F head → "F　WÖRTER PAAREN　Parejas";
  LAYOUT `("content34.py", "ey = 1620", "ey = 1680")` — the es col3 stack is
  ~30px taller than fr (tip ends 1623.66 vs fr 1593.13); same class as en, which
  moved the exercise section down. The ey move was applied proactively to all 8
  languages of this baton (all have 3-line undsie prompts like es).
- Build 2: ALL GATES PASS, but the visual proofread found a NEW defect class
  the occlusion audit cannot see (it only flags the 1950 page edge): col3
  box-title overflow — titles longer than the 400.5px box budget spill off
  their cream box background onto newsprint (box right edge 1862.0; titles start
  x=1461.5). es had 5.

### Round 2 (build 2 → rebuild 3, box-title fixes; new script `boxtitle.py`, 400.5px budget)
- STILLE "La semana tranquila" → "Tranquila" (356.5px; was OVER box edge by 84.0).
- TIPP "Consejo de la redacción" → "Consejo" (227.0; was OVER by 10.1).
- ADVENTSWÖRTER "Palabras de Adviento" → "Adviento" (341.4; was OVER by 83.4).
- WERKZEUGKASTEN "Herramientas" → "Útiles" (358.8; was OVER by 47.5).
- LESERBRIEFE "Cartas de los lectores" → "Cartas" (248.2; was OVER by 15.0).
- The same class was swept across all 8 languages before their builds
  (21 titles in 5 languages shortened; boxtitle.py 7/7 for es/it/pt/nl/ru/ja/ko/zh-tw).
  en/fr were proofread clean under their own values (en fits, fr ends at the box
  edge) — no action on en/fr.
- **Apostrophe rule applied from the start:** `tr_es.py` was written with straight
  apostrophes U+0027 throughout (as `\u0027` escapes inside single-quoted
  strings); U+2019 scan over the 8 SVGs is 0.

### Round 3 (rebuild 5 → rebuild 6, boxtitle gate fix; LAYOUT only)
- P1 Fragen subtitle `Las grandes preguntas　Die Fragen der Woche`: fs 19 → 18
  (`content12.py:69`); ink 1870.5 → 1849.5 (+12.5px margin). No text changed,
  no other line touched. See §6 Rebuild 6.

### D5 font rebuild (2026-11-12 — rebuild 7)

- **Cause**: explanation-layer Latin rendered in Noto Sans CJK instead of Newsreader (SOP §1.1 font table). Pre-D5 census: 636 Latin-in-CJK-Sans elements.
- **Fix (mechanism)**: `apply_variant.py` installed the D5 `_char_font` sans routing on the edition's `svglib.py` (Latin → Newsreader 400/600; fix2 included). No German text, fact, or key changed; no wording changed at all.
- **Five D5-caused defects, all fixed in source and rebuilt (run2)**:
  1. P1-fussball head `EINE WOCHE, ZWEI STIMMUNGEN` — HEAD TOO WIDE at 25pt; `content12.py:124` 25→22pt (411.8px fits the 422.5px column).
  2. P1 masthead collision — the 46pt headline `DIE BUNDESLIGA IST ZURÜCK — BAYERN GEGEN KÖLN!` widened in Newsreader SemiBold and overlapped the right-anchored subtitle `VUELVE LA BUNDESLIGA` by 14.5×20.8px (occlusion TEXTX; baseline 0 flags); `content12.py:27` subtitle 27→24pt (subtitle ink now starts at 1506.0, 26.2px clear of the headline ink at 1479.8). Headline untouched. Same defect class as the en-fr pilot's P1 collision.
  3. P1 cream-box title `DIE WOCHE IN ZAHLEN　En cifras` — +10.8px past the box; `content12.py:43` `f.box(…, tsize=22)` (397.4px fits 404.5).
  4. P3 vocab-box title `WEIHNACHTSWÖRTER　Palabras` — +25.9px; `content34.py:58` 24→22pt (390.6px fits 400.5).
  5. P8 battery head `A　LÜCKENTEXT　Texto con huecos` — HEAD TOO WIDE at 24pt (450.9px > 422.5px column); `content8.py:78` 24→22pt (413.3px fits).
- **Verification**: full gate re-run (§6b) — census 0, occlusion 0, p8 CLEAN, freeze 8/8, added CJK 0, spill 0, boxtitle 0 (real backup), edge 0, creambox PASS, print/web text layers identical.
- Note: the other box titles (sommaire, P2 `Tranquila`, P5 `Adviento`, P7 `Útiles`) fit as-is — Round 2 had already shortened their Spanish tails, so D5 widening stays inside the box.

### Reproof fix rebuild (2026-11-12 — rebuild 8)

- **Cause**: independent reproof of the D5 rebuild found 9 items (F7 major, rest minor) — see `hidden_files/w47/scratch-reproof-w47-de/PROOF-NOTE.md`.
- **Fix (in source, then rebuilt)**: F7 — P1 kicker reader segment shortened to `EL ALEMÁN QUE LEEN` (advance gap 49.6px, P1 render verified); F1 — P5 UND SIE prompt gained the advent-calendar question; F9 — P8 `·` spaced (142 places). Knock-on: F1 pushed the P5 col-3 image into the exercises hline, fixed by shrinking the image gap 26→14px (image ends 1749.93, ey stays 1756). Gates: build ALL GATES PASS; boxtitle 0 DEFECT; spill 0 SPILL; edge 0/0; census-patched PASS; head_check PASS; text.md dry-run diff 10 lines, 0 dropped.
- **Verification**: full gate re-run (logs in `hidden_files/w47/scratch-fix-de/logs/`) — see the per-edition entry in `scratch-fix-de/FIX-LOG.md`.
- New deliverables: print 10,354,400 B sha `2286ca8be3f3…`; web 1,514,438 B sha `dd6b52264ee1…`; text.md 50,430 B sha `a10745854e27…`.

### fix-de-minor1 (2026-11-13 — round-2 reproof C-1/C-2)

- **Fix (in source, then rebuilt)**: C-1 — P3 lead `die ersten Weihnachtsmärkte` contradicted the Hafenmarkt (open since 13 Nov, same article §2): P3 lead → `zwei große Weihnachtsmärkte` (same length, zero layout shift); the P5 lead carried the identical false claim and was fixed with the same wording; Q34 `Am Montag öffnet in Köln der erste ___.` → `Am Montag öffnen in Köln der Markt am Dom und der Markt der Engel, zwei große ___.` (word-box word and answer key `Weihnachtsmarkt` → `Weihnachtsmärkte`); Q80 `Am 16. November öffnen in Köln die ersten Weihnachtsmärkte.` → `Am 16. November öffnen der Markt am Dom und der Markt der Engel.` (answer stays `Richtig`). Q29 left unchanged (A2-acceptable per the brief; changing it would change the answer key). C-2 — P5 1903 calendar `Die Kinder konnten die Fenster mit Bildern überkleben.` → `Die Kinder konnten die Bilder ausschneiden und auf den Kalender kleben.` (the 1903 Lang/Kepler edition was windowless cut-and-paste). The `überkleben` gloss entry is left in place (the brief's fix is the sentence only; flagged to the coordinator). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p3, p5, p8 (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-fix-de-minor1/2026-w47-de-es/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 48 titles, 244 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal; spill 0 SPILL / 85 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 0 (reader layer; the shift vs the previous round's count is P3/P5/P8 re-wrap from the longer Q34/Q80 sentences, not content — the multiset proof below is authoritative), added Latin strings 443; print/web text layers multiset-identical (40,211 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: `die ersten`→`zwei große` ×3, `erste`→`Markt am Dom und der Markt der Engel` ×2, `Fenster mit Bildern überkleben`→`Bilder ausschneiden und auf den Kalender kleben`, footer/Q34-key changes where applicable); text.md re-exported from the fixed sources, diff exactly 7 lines (L309 P3 lead, L387 box, L389 Q34, L573 P5 lead, L577 C-2, L693 Q80, L1165 P8 answers Q34 key), 591 entries / 150 exercises. New deliverables: print 10,354,460 B sha `5dadd05cda9c…`; web 1,514,495 B sha `ef1574d33427…`; text.md 50,499 B sha `37907e01020e…`. Not committed / not pushed (coordinator inserts).


### fix-de-round3 (2026-11-13 — round-3 reproof R3-F1/R3-F2)

- **Fix (in source, then rebuilt)**: R3-F1 — the C-2 fix (fix-de-minor1) removed `überkleben` from the P5 1903 sentence but left the orphan gloss entry in the P5 gloss (`content56.py:23`); SOP §8.1 requires every glossed word to occur in the text, so the ` · überkleben …` segment was deleted from the P5 gloss (gloss shortens by one entry, layout-safe). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p5 only (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-reproof-de-round3/2026-w47-de-es/fix-round3/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 48 titles, 243 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal; spill 0 SPILL / 84 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 0, added Latin strings 442; print/web text layers multiset-identical (40,186 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: gloss `überkleben …` entry removed); text.md re-exported from the fixed sources, diff exactly L585 P5 gloss, 591 entries / 150 exercises. New deliverables: print 10,354,441 B sha `07f87aa04031…`; web 1,514,482 B sha `8e27d9c5f935…`; text.md 50,467 B sha `ec37787fa1d5…`. Not committed / not pushed (coordinator inserts).
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
