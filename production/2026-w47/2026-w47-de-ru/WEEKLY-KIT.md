# WEEKLY-KIT — 2026-W47 · German edition for Russian-speaking readers

- Edition: `2026-w47-de-ru` — German target text, Russian explanations
- Week: Mon 2026-11-16 – Sun 2026-11-22 · VOL.4 · Press time: Mon 2026-11-09
- Lead story: **Die Bundesliga kehrt zurück — Bayern gegen Köln** (40 chars, limit 56)
- Status: fan-out complete (rebuild-B), all self-check gates green on the FIRST
  rebuild run, visual proofread 8/8 pages zero findings (rebuild-B build 1,
  2026-11-11); independent proofread pending (coordinator to assign). Fix1 rebuild
  (2026-11-11, D1 toolbox-pad + rail-raise fix only, all gates green again;
  independent proof2 pending — coordinator to assign). New standing gates
  (2026-11-12) found 1 boxtitle defect (P1 sommaire title +12.5px); rebuild
  fix2 (2026-11-12) repaired it by layout only, all gates green again.
- **D5 font rebuild applied 2026-11-12 (rebuild fix3, all gates green — see §7)**
  Rebuild 2 (2026-11-11 06:57 UTC, 5th shift) also passed all gates; this
  rebuild only carries the core build15 Q34 stem correction (see §7).
- **fix-de-ru2 rebuild (2026-11-13, gate fix — see §7):** the fix-xru
  rebuild left 6 new regressions (P1 band-headline/gloss overlap + 5
  boxtitle overflows); all 6 repaired in source and rebuilt, all gates
  green again (occlusion 0 flags, boxtitle 0 DEFECT, p8 CLEAN, freeze
  8/8 + added CJK 7, print/web text layers identical).
- Source: `core-de/` build15 (2026-11-11 08:02 UTC, proof5 (a) zero findings)
  copied and translated in the explanation layer only. German target text is
  frozen — see §6 for the proof.
- Builder: de fan-out builder B (rebuild wave, 2026-11-11). Scratch:
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-de/`
  (`tr_ru.py`, `transform.py`, `build_edition.py`, `ru/` gate logs).

## §1 Contents

8 pages, 1950×2700, 4 columns. **150 exercises**, continuous numbering 1–150, all in
the registry. Identical layout and exercise set to the core; only the explanation
layer (bridges, instructions, glosses, notes, toolbox, disclosure, keys notes) is Russian.

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

Levels: A2 69 / B1 67 / B2 14. Types: выбор ответа 52 / дополнение 41 /
преобразование 11 / верно или нет 8 / текст с пропусками 8 / составление
предложений 8 / подбор слов 12 / перевод 4 / дополнение диалога 5 / письмо 1.

Pairing furniture (VOL.4): masthead `Die Lucerna`; edition line
`НЕМЕЦКИЙ ЕЖЕНЕДЕЛЬНИК　VOL.4　БУНДЕСЛИГА ВЕРНУЛАСЬ　ТИХАЯ НЕДЕЛЯ`; footer
`Die Lucerna　НЕМЕЦКИЙ ЕЖЕНЕДЕЛЬНИК VOL.4　Немецкий текст　Пояснения на русском`;
page line `Страница N из 8`; gloss prefix `Примечание — `.

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
  carries the labelled editor's example + the Russian disclosure:
  "Пример редакции: к сдаче номера настоящих писем не пришло. Присылайте ваши
  тексты для VOL.5!"

## §4 Images

Identical to the core (see `core-de/WEEKLY-KIT.md` §4 and `assets/CREDITS.md`):
fussball.jpg (P1), kopfball.jpg (P4), weihnachtsmarkt1930.jpg — Wilhelm Ritter 1930
(P3), christkind.jpg — Richard Ernst Kepler 1903 (P5), lesesaal.jpg — Carol M.
Highsmith, Library of Congress (P7), fussball1905.jpg (P8). All public domain, each
with target-language caption + printed credit.

## §5 Build / reproduction

- Build dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-de-ru/`
  (build code + deliverables, copied from `core-de/` by `transform.py ru`).
- Reproduce: `tools/venv/bin/python transform.py ru` (from scratch-fanout-de) →
  `tools/venv/bin/python measure.py ru <edition-dir>` →
  `tools/venv/bin/python build_edition.py ru` (run.py → render.py → webpdf →
  verify → occlusion → p8 → freeze → pdftotext → chips → export).
  Build interpreter is `tools/venv/bin/python` (PIL 13.0.0); freeze was re-run with
  the same interpreter (system python3 has PIL 10.2.0 and measures 1.1% differently).
- Deliverables (fix-de-round3 rebuild, 2026-11-13; fix-de-ru2 rebuild superseded — see §7):
  - Print PDF: `Die-Lucerna-VOL4-de-ru.pdf` — 10,506,857 bytes, 8 pages,
    sha256 `4e953850861bd191ebc6ae5bf7a44d2f29493c53080583c4b1d669dda8ebda05`
  - Web PDF: `Die-Lucerna-VOL4-de-ru-web.pdf` — 1,654,623 bytes (< 7 MB),
    sha256 `38bd5b1a08d12653db85056424447e7f389018234da9ebc90462059f7b66d6c6`
    (larger than the Latin editions' ~1.51 MB — Cyrillic font subsets)
  - Pre-fix-de-ru2 values (gate baseline, 2026-11-13): print 10,506,774 B
    sha `3ffe233bb14a…`; web 1,654,543 B sha `2b908bfbf757…`; text.md
    56,762 B sha `ba6a96c365b3…`.
  - Text export: `2026-w47-de-ru.text.md` — 56,774 bytes, 48,102 chars,
    591 entries, 150 exercises,
    sha256 `f768fb76cb70b3914db941a63985f3ec6578fa390e27fb42a9283998e8ca8d45`
    (changed — C-1/C-2 + P1 head restore per the §7 fix-de-minor1 entry; re-exported
    from the fixed sources, dry-run diff exactly 8 lines, 0 dropped)
    (exported from production sources in reading order, never from PDF)
  - `ABSTRACT.txt` (one line, Russian, no ASCII double quotes):
    "Die Lucerna Немецкий еженедельник VOL.4: возвращается Бундеслига
    («Бавария» принимает «Кёльн»), решающий матч Лиги наций против
    Нидерландов, день покаяния и молитвы и воскресенье поминовения усопших,
    открытие рождественских рынков Кёльна, европейские результаты и
    результаты Бундеслиги 3–8 ноября; текст на немецком, пояснения на
    русском, уровни A2–B2, 150 упражнений по темам недели."

## §6 Gates (rebuild-B build 1, 2026-11-11 — final)

- `run.py` (build.log): exit 0, **zero FLOW OVERFLOW / HEAD TOO WIDE**, TOTAL 150.
  Flow ends: P1-headline 1554 (= core), P1-fussball 2264, P1-quiz 2523,
  P2-feature 1023, P2-ex 2332, P3-main 946, P3-ex 2363, P4-main 677, P4-ex 2315,
  P5-main 1026, P5-ex 2441 (= core), P6-main 777, P6-ex 2523, P7-A2 1278 / B1 1342 /
  B2 1306, P8-battery 1409, P8-keys 2545 (bottom 2560, **spare only 15px** — passes
  but tight; the core P8-keys ends 2457, the extra 88px are the longer Russian
  instruction lines on P8).
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
  **Direct freeze proof (8/8, `ru/freeze-direct.json`, script `freeze_direct.py`):**
  (a) source-level: AST string-literal multiset core vs edition — 0 unaccounted
  removed, 0 unaccounted added (520 removed / 528 added, every one accounted for
  by the translation module, the CJK inventory, or a documented transform artifact);
  (b) rendered-text level: the frozen intersection (strings identical in core and
  edition SVGs) per page — P1 149, P2 163, P3 198, P4 166, P5 179, P6 175, P7 160,
  P8 187 strings, sha256 73347f49 / 689045ad / f356adcf / df1bebf7 / e7b235f9 /
  2bbe05f9 / 591dc064 / 7016818d. P2/P4/P6 sha8 are identical to the Latin editions
  (689045ad / df1bebf7 / 2bbe05f9); P1/P3/P5/P7/P8 differ with HIGHER frozen counts
  than the Latin 147/195/173/150/186 — the Russian SVGs carry more rendered text
  elements (P1: 207 vs 178), and the extra pure-German lines coincide with core
  lines, so the intersection grows. The German text itself is unchanged (source
  level 0 unaccounted + freeze.py exit 0 + p8 CLEAN); the sha8 difference is
  segmentation, not content.
- Print/web text layer: `pdftotext` default mode — print 57,607B / web 57,607B,
  **word multiset identical**; `-raw` mode — both 56,407B, normalised text
  **exactly identical**. Web PDF has a real text layer.
- Level chips (rx="2.7" rects): per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18,
  7:12, 8:35}, **TOTAL 141**; P8 by level A2 22 / B1 13 / B2 0. The core's
  missing-14 set is fully present: cloze options Q113–120 (8 A2 chips),
  dialogue badges Q145–149 (145–147 A2, 148 B1, 149 A2), writing title chip
  (B1 on "H SCHREIBEN").
- P8 answers measured font size: keys 13.25 SVG units = **9.94 PDF pt**
  (PyMuPDF re-measured P8 minimum span 9.94pt) — above the 9.75pt floor
  (concession step 4; P8 stems stay at the core's 15.375pt).
- 150-question key check (independent, `ru/keycheck-150.json`, script
  `keycheck.py`): P8-SVG-extracted keys vs the REG built from the edition's own
  sources — **149/150 exact**; the single non-exact item is Q150, the open
  writing task, where the extractor truncates the REG key "Свободное задание —
  следуйте пунктам из рамки письма" to "Свободное задание" (expected; Q150 is
  already in the keydiff set). REG by page
  {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}; levels A2 69 / B1 67 / B2 14.
- U+2019 scan over the 8 SVGs: **0** (straight U+0027 throughout, as `\u0027`
  escapes in `tr_ru.py`).
- Visual proofread: all 8 pages re-rendered from the print PDF at 100 dpi and
  viewed one by one (P1–P8), plus a systematic SVG-level scan of the 7 col3
  box titles (8 instances incl. the P6 full-width box): all end ≤ 1862.0
  (max 1853.4, LESERBRIEFE "Письма читателей", 8.6px margin). **Zero findings**
  (see §7). P5 was re-checked in detail after the build-1 fix: the 1903 calendar
  image and its caption now sit clear of the ÜBUNGEN header, Q68 is back in
  column 1, Q82 is clear of the footer; the P8 keys were spot-checked against
  the registry (dates, scores, times, grammar keys, MUSTER 84 words, chart
  44+33+23=100).

### Rebuild fix1 (2026-11-11 — D1 only)
- **D1 (de-es proof1 family defect, reproduced on ru pre-fix):** P7
  DER WERKZEUGKASTEN cream box too short — box bottom 813.0, last entry
  `Es ist fraglich, ob ... = ещё сомнительно` baseline 813.0 (clearance +0.0, baseline
  exactly on the box edge), `fraglich` descender ink ~4.7 below the box. Root cause
  (measured per-edition): the `tbh` formula in `content7.py:76` counts `n*29.5+6` per
  entry but the real advance is `20.5 + n*29.11 + 6` (`Page.para` first-baseline
  offset, 6 entries = +123 missed); ru wraps Σlines=10, so clearance = pad − 90.0
  and pad 90 gave +0.0. Core-de uses pad 110 (+18.8); the fan-out had cut it to 90
  with a "validated by occlusion 0 flags" comment — void, since the occlusion audit
  cannot see text spilling past its own box (nothing covers it).
- **Why not a flat pad 110:** ru's NOCH EIN WORT already ends at 1547.5, 0.5px before
  the 1548 Sätze rule — a flat +20 pad alone would push it to 1567.5, past the rule.
  **Fix (edition-local, `content7.py:76–77,84` only):** pad 90 → 110 (core-de value)
  **plus the whole col-3 rail raised 20** (`RTOP = CTOP − 20`, used for the toolbox
  rect y, the rail text start and `ry`). The rail's above-box slack is ~63px (P7 intro
  ends at baseline 262, toolbox top was 330), 20 used, ~43 left; the box top now sits
  20px above the A2/B1/B2 heads (330) — no overlap, nothing is drawn in col 3 between
  y 267 and 330. Verified: toolbox box y 330 → **310**, bottom **813.0 (unchanged)**,
  last baseline 813.0 → **793.0**, clearance **+20.0**; LESERBRIEFE y 829 / bottom
  1381.5 (+10.4, unchanged); NOCH EIN WORT y 1398 / ends **1547.5 (unchanged**, still
  0.5px before the 1548 rule, +42.9 unchanged). Full P7 render viewed at 100 dpi: the
  raised box top reads cleanly against the intro gap, no collision anywhere; 300 dpi
  toolbox zoom confirms the last entry fully inside the cream box (clear cream below
  the `g` descender); print/web toolbox zooms pixel-identical. No text changed:
  text.md byte-identical (sha dee6697b…); freeze_direct 8/8 with all 8 page shas
  identical to rebuild-B (73347f49 / 689045ad / f356adcf / df1bebf7 / e7b235f9 /
  2bbe05f9 / 591dc064 / 7016818d).
- New deliverables: print 10,954,759 B (−2 B) sha
  `d8f84e0500e23c19aed45e5eda095a37c8c55ca71c8e94aa43fdd0f0b5d4bf1e`; web 1,647,527 B
  (+42,190 B — working-tree webpdf.py now embeds the `LucernaNewsreader-Bold` subset,
  21,696 B; same effect as es/fr/it/pt/ko/zh-tw; < 7 MB, text layer identical to print)
  sha `462f516d1087dc7d997f9b7be66ccd842b7225fed37601ffcbf7c54ee9407c41`; text.md 56,231 B
  sha dee6697b… (unchanged). All gates green (occlusion 0 flags real run, p8 CLEAN
  keydiff [137,138,139,150], freeze diff +7 CJK all U+3000, freeze_direct 8/8 source
  PASS, keycheck 149/150 — Q150 extractor truncation only, boxtitle 7/7, d2scan 80
  pairs 0 web gaps >0.5pt, P8 min 9.94pt, chips 141, verify TOTAL 150, bent quotes
  U+201C 33 / U+201D 0, Q34 new stem 1x in all five places). Gate logs in
  `hidden_files/w47/scratch-fix-de-toolbox-family/gates-ru/`; build logs in
  `hidden_files/w47/scratch-fanout-de/ru/`.

### Rebuild fix2 (2026-11-12 — boxtitle gate fix, P1 only)
- **Defect (new standing gate `tools/boxtitle_check.py`, 130-wide run
  2026-11-12):** P1 sommaire title `IN DIESER AUSGABE　Содержание` ran past
  its cream box by **+12.5px** (core-de fits at −22.0px).
- **Fix (edition-local, `content12.py:89` only):** sommaire title font size
  24 → 22.5 (layout only, no text changed). Predicted and verified: ink end
  1874.5 → **1848.5**, margin **+13.5px**. No other line touched.
- New deliverables: print 10,954,763 B (+4 B) sha
  `237d36ae2d04b84808b017752307d6742155f5f84762fc4e3e581a6c7b430c29`; web
  1,647,542 B (+15 B) sha
  `1a708f26903d2b4fbc2aa82b1130fb7f8843528742568cc8cbdef7ebd8b61554`; text.md
  56,231 B sha dee6697b… (unchanged). All gates green on the rebuilt edition:
  boxtitle **0 DEFECT / 0 OBSERVE / 0 marginal** (also 0 on the synced
  production files), verify TOTAL 150 + SVGs byte-identical after re-run,
  occlusion 0 flags, p8 extract 150/150 + compare CLEAN keydiff
  [137,138,139,150], freeze `diff` exit 0 (added CJK 7, all U+3000) +
  freeze-direct rendered **8/8** with all 8 frozen SHAs identical to rebuild
  fix1 (73347f49 / 689045ad / f356adcf / df1bebf7 / e7b235f9 / 2bbe05f9 /
  591dc064 / 7016818d). NOTE (pre-existing, not this fix): freeze-direct
  *source* level now reports 1 unaccounted removed literal (`'sans'` ×2 in
  `svglib.py`) — core-de's `svglib.py` was patched (fix2 U+201C routing,
  2026-11-11 22:35) after ru was copied from it; at fix1 time the source
  level PASSED. This fix changed one int + one comment, no string literal.
  Gate outputs in `scratch-gatefix-de-en/2026-w47-de-ru/` (FIX-LOG.md).

## §6b Gates (D5 font rebuild round, rebuild fix3, 2026-11-12 — full re-run on the rebuilt edition; scratch `hidden_files/w47/scratch-d5-de/de-ru/`)

- D5 mechanism: `apply_variant.py --svglib … --target de --reader ru` (mode ru) on the edition's `svglib.py`; fix2 curly-quote routing installed with it. Pre-D5 `svglib.py` backed up as `svglib.py.pre-d5`. Pre-D5 baseline verified CLEAN before install: the production dir was copied to scratch and rebuilt with the venv interpreter — freeze baseline **8/8 SVGs byte-identical** to the delivered SVGs (`freeze-pre-baseline.log`). Pre-D5 production snapshot in `scratch-d5-de/de-ru/baseline/` (SVGs + sources, rebuild-fix2 state). KIT wave 2 check: pre-D5 print SHA matches the KIT (`237d36ae…`), but the pre-D5 web PDF on disk was sha `1a708f26…` (1,647,542 B), NOT the KIT's rebuild-fix2 record `462f516d…` — the rebuild-fix2 web PDF had been rebuilt without a KIT sync (same class as de-en/de-fr/de-it/de-nl/de-pt). The D5 values above are measured from the actual files on disk.
- **Routing (mode ru — different from the Latin readers, by design)**: the copied latin routing assert failed 7 checks (`_D5_READER == latin`, Latin sans → news) because ru readers route **Latin+Cyrillic → sans_noto** (Noto Sans Medium 500 / Bold 700 exact) per `svglib-d5.py` and CJK-DECISION §2 — that is the SOP's ru-reader spec (core-ru parity), not a defect. A ru-mode assert (`routing_assert_ru.py`: `_D5_READER == "ru"`, Latin sans → sans_noto ×6, Cyrillic sans → sans_noto regular + bold, CJK sans → sans, serif Latin → news, fix2 ×6) gives **`ROUTING FAILURES: 0`**.
- Pre-D5 D5 census: **858 elements — 482 Latin + 376 Cyrillic in Noto Sans CJK** (matches D5-CENSUS-130); quotes defective 0; p8 extract 150/150.
- `run.py` (run2): TOTAL **150**, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`tools/head_check.py`: PASS 0 defects) — no head overflowed, because Noto Sans Latin is narrower than CJK Sans Latin (the Latin readers all overflowed the same heads in Newsreader SemiBold).
- `mechanism/d5_census.py`: **PASS — D5 Latin 0, D5 Cyrillic 0, curly-in-CJK 0**.
- `tools/occlusion_audit.py`: **0 flags** (selftest OK; fixed tool — bare `Noto Sans` runs measured on the non-CJK face, brief §10).
- `tools/p8.py`: extract 150/150; compare vs rebuilt core-de P8: `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]` — the same 4 expected reader-language items as rebuild-B. Note: unlike the en-ru pilot's 3 P8 key-line collisions, this edition's P8 has no collisions (occlusion 0).
- `tools/freeze.py`: baseline **8/8 SVGs byte-identical** (venv Pillow 13.0.0 / FreeType 2.14.3); diff pre-D5 baseline vs rebuilt: **added CJK characters 0** (added Latin strings 238 = D5 run-splitting).
- `tools/spill_sweep.py`: 32 boxes, 90 candidates, **0 SPILL**, 90 OBSERVE.
- `tools/boxtitle_check.py`: 48 titles, 297 body lines, **0 DEFECT**, 0 OBSERVE, 0 marginal (real backup comparison: `scratch-d5-de/scratch-fanout-de/backup/2026-w47-de-ru`) — no title fix was needed: bold Cyrillic narrows in Noto Sans, so every title fits.
- `tools/pdf_edge_scan.py`: 8 pages, **0 TOUCH, 0 NEAR**.
- `tools/d5_creambox_audit.py` (pre-D5 baseline vs rebuilt): **PASS 0 defects**; ratios n=556, median 0.999, bold 0.956 / regular 1.018 — the ru sign flip from the pilot (bold Cyrillic narrows, regular widens); P8 lines 226→237 (+11, same as the en-ru pilot), footer slack 33.6→33.6px.
- Web/print text layer: `pdftotext` default mode — both **57,469 bytes**, word multiset identical, normalised text exactly identical; `-raw` mode — both 56,407 bytes, identical.

## §7 Fan-out changes (explanation layer only — no German text, fact or key changed)

- **Rebuild-B (2026-11-11):** core-de build15 corrected the P3 Q34 stem to the
  singular form matching key `Weihnachtsmarkt` (the D-01 stem/key mismatch from
  the de-fr first-round proof, resolved at the core). This edition was deleted
  and re-transformed from the new core with unchanged `tr_ru.py` /
  `vals_ru.json`; the rebuild passed all gates first run with no fixes, and the
  visual proofread (P1–P8 at 100 dpi, /tmp/ru-rb-proof-*.png) found zero
  findings. Only delta vs rebuild 2 is that one stem string (P3); all flow ends,
  chips, keys and frozen sha8 are otherwise identical (only P3 sha8 moved).
- **Build 1 (2026-11-11 ~06:48 UTC) failed 3 gates** — FLOW OVERFLOW [P5-ex]
  col 3 y=2563 need 104 (flow ended y=2682, 122px over) + occlusion 3 flags,
  all on p5-jugend.svg: the 1903 calendar caption's 2nd line sat on the ÜBUNGEN
  header rule (TEXTX, image + caption overlapping the header), and a Q82 line
  crossed the footer hline (LINEX). Root causes, both measured in the SVGs:
  (1) the P5 section-A instruction "Прочитайте стр. 5 и выберите правильный
  ответ." wrapped to 2 lines, pushing every A question +30px and cascading Q68
  out of column 1 (+241px on P5-ex); (2) two P5 vocab-box entries wrapped to
  2 lines at the 377.5px box width in serif 21.5pt — "der Wunschzettel — список
  желаний" 380.6px and "das Christkind — Младенец Христос" 382.3px — adding
  ~61px to the col3 stack and driving the image into the header.
- **Fixes (vals_ru.json, 3 values, tr_ru.py diff exactly 3 lines):**
  "Прочитайте стр. 5 и выберите правильный ответ." →
  "Прочитайте стр. 5 и выберите ответ." (366.7px sans / 387.3px serif at 20.5pt,
  1 line); "das Christkind — Младенец Христос" → "das Christkind — Младенец"
  (285.4px serif 21.5pt, 1 line); "der Wunschzettel — список желаний" →
  "der Wunschzettel — желания" (294.3px serif 21.5pt, 1 line). Rebuild 2:
  vocab ends 979.36 (= it), image ends 1732.93 (= it), P5-ex ends 2441 (= core).
  Untouched: the standalone key "Младенец Христос" (line 96) and the P8 key
  "Wunschzettel=список желаний" — different keys/uses.
- **Build 1 also taught:** P3-ex 2363 (+30 vs it, same 2-line-instruction class)
  and P3-main 946 (+30) pass with margin — no action. P8-keys ends 2545
  (spare 15px) — passes, no action.
- Box titles (from the 5th-baton sweep, before build 1): STILLE "Тихая неделя"
  → "Тишина" (340.4px); WEIHNACHTSWÖRTER "Рождество" → "Слова" ("Праздник"
  measured 406.9px, still OVER, rejected); ADVENTSWÖRTER "Слова Адвента" →
  "Адвент" (323.9px); TOOLBOX "Инструменты" → "Справка" (391.8px) (boxtitle.py 7/7).
- P2 Rechnen note shortened during validation to 1 line: "Внимание: рынки
  закрыты в Totensonntag — приходите в пн. или вт." (667.5px at 20pt in 795px).
- P8 battery A head is "A　LÜCKENTEXT　Пропуски" (338.9px; "Текст с пропусками"
  458.0px would exceed the 422.5px column width); F head "Подбор слов" 421.4px
  (1.1px margin, deterministic pass, keep).
- **Apostrophe rule applied from the start:** `tr_ru.py` was written with straight
  apostrophes U+0027 throughout (as `\u0027` escapes inside single-quoted
  strings); U+2019 scan over the 8 SVGs is 0.
- Cyrillic: fully covered 64/64 by Noto Serif CJK SC and Noto Sans CJK SC
  (Newsreader has no Cyrillic, as SOP §1.1 says); per-char fallback renders it.
- **Rebuild fix2 (2026-11-12 — boxtitle gate fix; LAYOUT only):** P1 sommaire
  title `IN DIESER AUSGABE　Содержание`: fs 24 → 22.5 (`content12.py:89`);
  ink 1874.5 → 1848.5 (+13.5px margin). No text changed, no other line
  touched. See §6 Rebuild fix2.

### D5 font rebuild (2026-11-12 — rebuild fix3)

- **Cause**: explanation-layer Latin (482) and Cyrillic (376) rendered in Noto Sans CJK instead of Noto Sans (SOP §1.1 font table, ru-reader spec). Pre-D5 census: 858 elements.
- **Fix (mechanism)**: `apply_variant.py` installed the D5 `_char_font` sans routing on the edition's `svglib.py` with `_D5_READER = "ru"` (Latin+Cyrillic → Noto Sans Medium 500 / Bold 700 exact; fix2 included). No German text, fact, or key changed; no wording changed at all.
- **One D5-caused defect, fixed in source and rebuilt (run2)**: P4 "Und Sie" gloss `Бундеслига или сборная? Кто победит в Мюнхене? Напишите по-немецки!` — regular Cyrillic widens +1.8% in Noto Sans, so the gloss wrapped to 3 lines at 20pt (baseline 2) and its last line `по-немецки!` sat 58% under the results-table band (occlusion COVER; baseline 0 flags); `content34.py:163,169` gloss 20→19.5pt (both the `eh` height formula and the `p.para` call — at 19.5pt it wraps to exactly the baseline's 2 lines, and P4 col3 now ends at 1156.02, clear of the band). No wording change. Same defect class as de-en's P4 gloss wrap (there the fix was shortening the English gloss; here a half-point size drop suffices).
- **What did NOT break (ru sign flip)**: no HEAD TOO WIDE anywhere and no boxtitle defect — bold Cyrillic narrows in Noto Sans, so all 48 titles and all 3 P8 battery heads fit as-is. P8 reflowed 226→237 lines (+11, as in the en-ru pilot) with footer slack unchanged at 33.6px, and no P8 key-line collisions appeared.
- **Verification**: full gate re-run (§6b) — census 0, occlusion 0, p8 CLEAN, freeze 8/8, added CJK 0, spill 0, boxtitle 0 (real backup), edge 0, creambox PASS, print/web text layers identical in both modes.
- Note: the P1 masthead subtitle never collided with the headline in this edition.
- **Correction (2026-11-13, fix-de-minor1)**: the D5 section's claim above — 'No German text, fact, or key changed; no wording changed at all' — was wrong for this edition. D5 also deleted `EINE` from the P1 mini-feature head (`EINE WOCHE, ZWEI STIMMUNGEN` @25pt → `WOCHE, ZWEI STIMMUNGEN` @25pt, `content12.py:124`, no comment); the other 10 editions kept `EINE` and only dropped 25→22pt. That was the 6th wording deletion across the D5 + fix-de-ru2 rounds (fix-de-ru2's '5 wording deletions' counted only its own round: D1–D4 + D6). Restored by fix-de-minor1 (see below).

### Reproof fix rebuild (2026-11-12 — rebuild 8)

- **Cause**: independent reproof of the D5 rebuild found 9 items (F7 major, rest minor) — see `hidden_files/w47/scratch-reproof-w47-de/PROOF-NOTE.md`.
- **Fix (in source, then rebuilt)**: F1 — P5 UND SIE prompt gained the advent-calendar question; F2 — P5 vocab glosses completed (`список желаний`, `Младенец Христос`); F4 — P2+P6 box title `Тишина` → `Тихая неделя` (P2 21pt, P6 24pt); F5 — P1 DIE WOCHE IN ZAHLEN box regained the three German sentences (+ reader gloss); F9 — P8 `·` spaced (142 places). Knock-ons: (a) P5 col-3 stack grew 90px (F1+F2) — three gaps 26→10px, image 313→280px, caption origin synced (image ends 1741.99, ey stays 1756); (b) the 9-line P1 numbers box (402px) broke the P1-headline flow (ended 1921 > 1828, occlusion 9 flags) — box items 20.5→18pt and P1 bridge 20.5→19pt, flow ends 1554 (= core/es). Gates: build ALL GATES PASS; boxtitle 0 DEFECT; spill 0 SPILL; edge 0/0; census-patched PASS (D5_cyr=84 from the production-schema replication is a false alarm — the authoritative patched schema drops that check; cjk_sans identical on all pages); head_check PASS; text.md dry-run diff 16 lines, 0 dropped.
- **Verification**: full gate re-run (logs in `hidden_files/w47/scratch-fix-de/logs/`) — see the per-edition entry in `scratch-fix-de/FIX-LOG.md`.
- New deliverables: print 10,624,220 B sha `dda94ec32ed3…`; web 1,770,599 B sha `b9971c845e0f…`; text.md 56,776 B sha `28db7a67610c…`.
- **fix-xru (12 Nov 2026, SOP §1.1)**: `svglib.py` `_D5_READER == "ru"` branch routed Latin text to Noto Sans CJK; branch removed (marked `[removed 2026-11-12 fix-xru]`), now always else logic — Latin → Newsreader, Cyrillic → Noto Sans. Rebuilt with `driver.sh de` (run.py rc=0, render.py rc=0, text-layer character multiset identical pre/post, 39,897 non-space chars; webpdf.py rc=0, 8 pages). Probe (SVG runs): pre-fix LAT@NotoSans=5094 LAT@Newsreader=21571 CYR@NotoSans=6954; post-fix LAT@NotoSans=0 LAT@Newsreader=26665 CYR@NotoSans=6954 (unchanged). Note: run.py now reports 4 HEAD TOO WIDE warnings (P1-fussball headline; P8 battery heads B/D/F) — pre-existing status not re-gated here, flagged to coordinator. New deliverables: print 10,506,776 B sha `ca76ee92a88b…` (was 10,624,220 B `dda94ec32ed3…`), web 1,654,528 B sha `8cd1342d91f4…` (was 1,770,599 B `b9971c845e0f…`); text.md unchanged 56,776 B `28db7a67610c…`. No retry.

### Rebuild fix-de-ru2 (2026-11-13 — gate fix, P1 band + boxtitles)

- **Cause**: after fix-xru (Latin → wider Newsreader), the gate re-run found
  6 NEW regressions (all 0 in every earlier round): 1 P1 band-headline/gloss
  overlap + 5 boxtitle overflows. Scratch:
  `hidden_files/w47/scratch-fix-de-ru2/` (gates, logs, crops).
- **Fixes (edition-local, `content12.py` + `content7.py` only; no German
  target text, fact, or key changed; 5 wording deletions, 1 font-size drop):**
  - D1 — P1 band headline `DIE BUNDESLIGA IST ZURÜCK — BAYERN GEGEN KÖLN!`
    (46pt) ran to 1479.8 and overlapped the gold gloss `БУНДЕСЛИГА
    ВОЗВРАЩАЕТСЯ` (same baseline y=524) by 60.2×21.2px. Fix: headline →
    `DIE BUNDESLIGA IST ZURÜCK — BAYERN–KÖLN!` (drop `GEGEN `, en-dash).
    Headline ink now ends 1301.0; gap to the gloss ≈119px (gate-measured
    gloss ink from 1419.6). P1 band render viewed: clean gap, no touch.
  - D2 — P1 numbers-box title `DIE WOCHE IN ZAHLEN　В цифрах` (23pt) ran
    +25.6px past its cream box. Fix: drop `DIE ` → `WOCHE IN ZAHLEN　В цифрах`;
    last run `цифрах` now ends −23.7px inside the box.
  - D3 — P1 sommaire title `IN DIESER AUSGABE　Содержание` (22.5pt) ran
    +17.5px past its box. Fix: drop `IN ` → `DIESER AUSGABE　Содержание`;
    `Содержание` now ends −15.7px inside the box.
  - D4 — P7 toolbox title `DER WERKZEUGKASTEN　Справка` (23pt) ran +33.0px
    past its box. Fix: drop `DER ` → `WERKZEUGKASTEN　Справка`; `Справка`
    now ends −24.2px inside the box.
  - D5 — P7 `LESERBRIEFE　Письма читателей` (23pt) ran +22.6px past its box.
    Fix: font size 23 → 21 (nl 25→23 precedent), wording kept;
    `читателей` now ends −14.0px inside the box. NOTE: at 21pt the line
    falls below the boxtitle tool's 22.0pt TITLE floor, so it is counted as
    a BODY line (titles 66→62, body 472→475 — the other −1 title is D6's
    deleted word `одно`); the over check applies to BODY lines identically,
    and a per-element classification diff (pre-fix SVGs rebuilt in /tmp
    from the reverted sources, byte-identical) shows zero elements with
    over > 0 anywhere post-fix — the 0 DEFECT is not vacuous for this line.
  - D6 — P7 `NOCH EIN WORT　Ещё одно слово` (22pt) ran +1.3px past its box.
    Fix: drop `одно` → `Ещё слово`; `слово` now ends −60.3px inside the box.
  - Only p1-front.svg and p7-sprache.svg changed (SHA-verified); P2–P6, P8
    byte-identical. Flow ends unchanged (P1-headline 1554 = core, P8-keys
    2545). run.py rc=0, TOTAL 150, no FLOW OVERFLOW.
- **Out of scope, untouched**: P8-battery `D　SÄTZE BAUEN　Предложения` still
  reported by head_check — **coordinator accepted** (overage +0.7u past the
  rule line, no collision; acceptance record to HEADS-NOTE.md). Re-measured
  on the rebuilt file: rendered ink ends +1.8u past the column edge
  (1413.3 vs 1411.5), 26.2u clear of the next column; occlusion 0 flags.
  Not touched.
- **Verification** (full gate re-run, logs in `scratch-fix-de-ru2/gates/`):
  occlusion **0 flags** (selftest OK); boxtitle **0 DEFECT / 0 OBSERVE /
  0 marginal** (62 titles, 475 body lines); spill **0 SPILL** (167 OBSERVE);
  edge **8 pages, 0 TOUCH, 0 NEAR**; p8 extract 150/150, compare vs core-ru
  **CLEAN, keydiff identical to pre-fix**; D5 census **PASS** (D5_lat 0,
  D5_cyr 0, curly_in_cjk 0; probe LAT@NotoSans 0, LAT@Newsreader 26648,
  CYR@NotoSans 6946); freeze baseline **8/8 SVGs byte-identical** (core
  reproducibility) + freeze diff **added CJK 7, all U+3000**; verify.py
  TOTAL 150, numbering continuous, SVGs byte-identical after re-run, style
  audit True, verbatim OK, P8 floor 9.94pt; print/web text layers
  **identical in default and -raw modes** (56,943 B / 56,893 B);
  pre/post print text-layer word diff is exactly the 7 removed + 1 added
  words of the 5 wording fixes (D5 font-size-only: no text change).
  P1 band + P7 rail renders viewed: all titles inside their boxes.
- New deliverables: print 10,506,789 B sha `e8474308adec4…`; web 1,654,559 B
  sha `0bc09dbd4428…`; text.md 56,738 B sha `a6ebb0818b2b…` (5 lines
  changed, 0 dropped; dry-run re-export reproduced the pre-fix text.md
  byte-identically before the edit).

### fix-de-minor1 (2026-11-13 — round-2 reproof C-1/C-2 + P1 head restore)

- **Fix (in source, then rebuilt)**: C-1 — P3 lead `die ersten Weihnachtsmärkte` contradicted the Hafenmarkt (open since 13 Nov, same article §2): P3 lead → `zwei große Weihnachtsmärkte` (same length, zero layout shift); the P5 lead carried the identical false claim and was fixed with the same wording; Q34 `Am Montag öffnet in Köln der erste ___.` → `Am Montag öffnen in Köln der Markt am Dom und der Markt der Engel, zwei große ___.` (word-box word and answer key `Weihnachtsmarkt` → `Weihnachtsmärkte`); Q80 `Am 16. November öffnen in Köln die ersten Weihnachtsmärkte.` → `Am 16. November öffnen der Markt am Dom und der Markt der Engel.` (answer stays `Richtig`). Q29 left unchanged (A2-acceptable per the brief; changing it would change the answer key). C-2 — P5 1903 calendar `Die Kinder konnten die Fenster mit Bildern überkleben.` → `Die Kinder konnten die Bilder ausschneiden und auf den Kalender kleben.` (the 1903 Lang/Kepler edition was windowless cut-and-paste). The `überkleben` gloss entry is left in place (the brief's fix is the sentence only; flagged to the coordinator). **de-ru fix (edition-local, `content12.py:124`)**: P1 mini-feature head `WOCHE, ZWEI STIMMUNGEN` @25pt → `EINE WOCHE, ZWEI STIMMUNGEN` @22pt (the other 10 editions carry `EINE …` @22pt per the D5 fix; this edition's D5 round deleted `EINE` and kept 25pt, unrecorded — see the D5 correction note added in §7 below; the 6th wording deletion across the D5 + fix-de-ru2 rounds). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE except the accepted de-ru SÄTZE item — see below); changed SVGs: p1, p3, p5, p8 (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-fix-de-minor1/2026-w47-de-ru/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 62 titles, 475 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal; spill 0 SPILL / 165 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check 1 defect = the accepted P8-battery `D　SÄTZE BAUEN` (+0.7u, coordinator-accepted, untouched); D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 0 (reader layer; the shift vs the previous round's count is P3/P5/P8 re-wrap from the longer Q34/Q80 sentences, not content — the multiset proof below is authoritative), added Latin strings 243; print/web text layers multiset-identical (39,929 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: `die ersten`→`zwei große` ×3, `erste`→`Markt am Dom und der Markt der Engel` ×2, `Fenster mit Bildern überkleben`→`Bilder ausschneiden und auf den Kalender kleben`, footer/Q34-key changes where applicable); text.md re-exported from the fixed sources, diff exactly 8 lines (the 7 base lines + L145 P1 head `EINE WOCHE, ZWEI STIMMUNGEN`), 591 entries / 150 exercises. New deliverables: print 10,506,882 B sha `216d673c75df…`; web 1,654,660 B sha `5abf79780edb…`; text.md 56,812 B sha `832319d2424b…`. Not committed / not pushed (coordinator inserts).


### fix-de-round3 (2026-11-13 — round-3 reproof R3-F1/R3-F2)

- **Fix (in source, then rebuilt)**: R3-F1 — the C-2 fix (fix-de-minor1) removed `überkleben` from the P5 1903 sentence but left the orphan gloss entry in the P5 gloss (`content56.py:23`); SOP §8.1 requires every glossed word to occur in the text, so the ` · überkleben …` segment was deleted from the P5 gloss (gloss shortens by one entry, layout-safe). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE except the accepted de-ru SÄTZE item — see below); changed SVGs: p5 only (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-reproof-de-round3/2026-w47-de-ru/fix-round3/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 62 titles, 472 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal; spill 0 SPILL / 165 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check 2 findings on the post-fix log — both the same accepted P8-battery `D　SÄTZE BAUEN` (+0.7u, coordinator-accepted, untouched), one per build pass (run_build.py appends to run-build.log; the log holds the rebuild pass + the gates re-run pass); the P8 SVG is byte-identical to pre-fix; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 0, added Latin strings 242; print/web text layers multiset-identical (39,907 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: gloss `überkleben …` entry removed); text.md re-exported from the fixed sources, diff exactly L585 P5 gloss, 591 entries / 150 exercises. New deliverables: print 10,506,857 B sha `4e953850861b…`; web 1,654,623 B sha `38bd5b1a08d1…`; text.md 56,774 B sha `f768fb76cb70…`. Not committed / not pushed (coordinator inserts).
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
- P8-keys ends 2545 (spare only 15px) — the tightest of the de family so far;
  any future Russian-length growth on P8 must be watched.
