# WEEKLY-KIT — 2026-W47 · German edition for English-speaking readers

- Edition: `2026-w47-de-en` — German target text, English explanations
- Week: Mon 2026-11-16 – Sun 2026-11-22 · VOL.4 · Press time: Mon 2026-11-09
- Lead story: **Die Bundesliga kehrt zurück — Bayern gegen Köln** (40 chars, limit 56)
- Status: fan-out complete, all self-check gates green, visual proofread 8/8 pages
  (rebuild 3, 2026-11-11; core build15); fix1 applied 2026-11-11 (D1/D2/D3,
  rebuild 4, all gates green — see §7); proof2 done 2026-11-11 (conclusion (b),
  2 defects — the D1/D2 closing quotes still wide in sans); fix2 applied
  2026-11-11 (narrow-quote render fix, rebuild 6, all gates green — see §7);
  **D5 font rebuild applied 2026-11-12 (rebuild 7, all gates green — see §7)**
  independent proofread (proof3) pending (coordinator to assign).
  NOTE: the previous proof1 (a) is void (done against the old Q34 stem); a fresh full proofread round is required.
- Source: `core-de/` (2026-w47-de-zh-cn, build15) copied and translated in the
  explanation layer only. German target text is frozen — see §6 for the proof.
- Builder: de fan-out builder, 3rd shift (2026-11-11). Scratch:
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-de/`
  (`tr_en.py`, `transform.py`, `build_edition.py`, `en/` gate logs).

## §1 Contents

8 pages, 1950×2700, 4 columns. **150 exercises**, continuous numbering 1–150, all in
the registry. Identical layout and exercise set to the core; only the explanation
layer (bridges, instructions, glosses, notes, toolbox, disclosure, keys notes) is English.

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

Levels: A2 69 / B1 67 / B2 14. Types: multiple choice 52 / fill-in 41 /
transformation 11 / true/false 8 / cloze 8 / sentence building 8 / matching 12 /
translation 4 / dialogue completion 5 / writing 1.

Pairing furniture (VOL.4): masthead `Die Lucerna`; edition line
`GERMAN WEEKLY　VOL.4　BUNDESLIGA RETURNS　A QUIET WEEK`; footer
`Die Lucerna　GERMAN WEEKLY VOL.4　German text　English explanations`;
page line `Page N of 8`; gloss prefix `Note — `.

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
  carries the labelled editor's example + the English disclosure:
  "Editor's example — no real letters had arrived by press time. Send us your
  writing for VOL.5."

## §4 Images

Identical to the core (see `core-de/WEEKLY-KIT.md` §4 and `assets/CREDITS.md`):
fussball.jpg (P1), kopfball.jpg (P4), weihnachtsmarkt1930.jpg — Wilhelm Ritter 1930
(P3), christkind.jpg — Richard Ernst Kepler 1903 (P5), lesesaal.jpg — Carol M.
Highsmith, Library of Congress (P7), fussball1905.jpg (P8). All public domain, each
with target-language caption + printed credit.

## §5 Build / reproduction

- Build dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-de-en/`
  (build code + deliverables, copied from `core-de/` by `transform.py en`).
- Reproduce: `tools/venv/bin/python transform.py en` (from scratch-fanout-de) →
  `tools/venv/bin/python measure.py en <edition-dir>` →
  `tools/venv/bin/python build_edition.py en` (run.py → render.py → webpdf →
  verify → occlusion → p8 → freeze → pdftotext → chips → export).
- Deliverables (fix-de-round3 rebuild, 2026-11-13; fix-de-minor1 rebuild superseded):
  - Print PDF: `Die-Lucerna-VOL4-de-en.pdf` — 10,350,173 bytes, 8 pages,
    sha256 `aaaad1ed122ad23442e77e57615e9d823326f0111745afdc3fdeecba3ef61f91`
  - Web PDF: `Die-Lucerna-VOL4-de-en-web.pdf` — 1,510,219 bytes (< 7 MB),
    50,616 text bytes,
    sha256 `6e50a693d200fbb2beef36254b9f57266a325d9252fe6af5d315515e27b98f04`
  - Text export: `2026-w47-de-en.text.md` — 49,975 bytes, 48,344 chars,
    591 entries, 150 exercises,
    sha256 `6fb1fb37415bf055d52162bb9c213b271c08dba02f13256524cb3b87d78f2418`
    (changed — wording fixed per the §7 reproof fix entry; re-exported from the fixed sources)
    (exported from production sources in reading order, never from PDF)
  - `ABSTRACT.txt` (one line, English, no ASCII double quotes):
    "Die Lucerna German Weekly VOL.4: Bundesliga returns (Bayern vs Cologne at
    home), Nations League decider against the Netherlands, day of repentance and
    prayer and Sunday of the Dead, Cologne Christmas markets open, European and
    Bundesliga results 3–8 November; German text, English explanations, levels
    A2–B2, 150 exercises based on this week's topics."

## §6 Gates (rebuild 2, 2026-11-11 — values below; rebuild 3 and fix1 deltas in §7, current gates in `scratch-fix-de-en1/GATE-LOG.md`)

- `run.py` (build.log): exit 0, **zero FLOW OVERFLOW / HEAD TOO WIDE**, TOTAL 150.
  Flow ends: P1-headline 1554 (= core), P1-fussball 2264, P1-quiz 2523,
  P2-feature 993, P2-ex 2332, P3-main 946, P3-ex 2363, P4-main 677, P4-ex 2315,
  P5-main 1026, P5-ex 2441 (= core), P6-main 777, P6-ex 2523, P7-A2 1278 / B1 1342 /
  B2 1306, P8-battery 1409, P8-keys 2481 (bottom 2560, spare 79px).
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
  **Direct freeze proof (8/8, done by hand, not the tool's baseline 0/8):**
  (a) source-level: every core no-CJK string literal (2033) is present in the
  edition with the same count — the only 8 absent are expected transform
  artifacts (masthead subtitle, full-width parens `（）`, spaced separator
  ` · `, PDF filename, verify.py docstring/path); every added no-CJK string is
  English (TR/TYPEMAP/INSTRMAP values or formatting fragments);
  (b) rendered-text level: the frozen intersection (strings identical in core and
  edition SVGs) per page — P1 147, P2 163, P3 195, P4 166, P5 173, P6 175, P7 150,
  P8 186 strings, sha256 083e2a2a / 689045ad / 093cf378 / df1bebf7 / 86fa4421 /
  2bbe05f9 / b7aa0771 / 57e118e7.
- Print/web text layer: `pdftotext` default mode — print 50,434B / web 50,435B,
  **word multiset identical**; `-raw` mode — both 49,277B, normalised text
  **exactly identical**. Web PDF has a real text layer.
- Level chips (rx="2.7" rects): per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18,
  7:12, 8:35}, **TOTAL 141**; P8 by level A2 22 / B1 13 / B2 0. The core's
  missing-14 set is fully present: cloze options Q113–120 (8 A2 chips),
  dialogue badges Q145–149 (145–147 A2, 148 B1, 149 A2), writing title chip
  (B1 on "H SCHREIBEN").
- P8 answers measured font size: keys 13.25 SVG units = **9.94 PDF pt**
  (PyMuPDF re-measured P8 minimum span 9.94pt) — above the 9.75pt floor
  (concession step 4; P8 stems stay at the core's 15.375pt).
- 150-question key check (independent, `en/keycheck-150.json`): P8-SVG-extracted
  keys vs the REG built from the edition's own sources — **149/150 exact**;
  the single non-exact item is Q150, the open writing task, where the extractor
  truncates the REG key "Open task — follow the points in the writing box" to
  "Open task" (expected; Q150 is already in the keydiff set). REG by page
  {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}; levels A2 69 / B1 67 / B2 14.
- Visual proofread: all 8 pages re-rendered from the print PDF at 100 dpi and
  viewed one by one (P1–P8), plus magnified crops of every corrected spot.
  **Zero findings after the apostrophe fix** (see §7). The P8 keys were
  spot-checked against the registry (dates, scores, times, grammar keys,
  MUSTER 84 words, chart 44+33+23=100).

## §6b Gates (D5 font rebuild round, rebuild 7, 2026-11-12 — full re-run on the rebuilt edition; scratch `hidden_files/w47/scratch-d5-de/de-en/`)

- D5 mechanism: `apply_variant.py --svglib … --target de --reader en` (mode latin) on the edition's `svglib.py` — the edition already carried the fix2 curly-quote routing from rebuild 6, and the installer preserved it (routing assert `ROUTING FAILURES: 0`). Pre-D5 `svglib.py` backed up as `svglib.py.pre-d5`; pre-D5 production snapshot in `scratch-d5-de/de-en/baseline/` (SVGs + sources, rebuild-6 state).
- Pre-D5 D5 census: **637 Latin-in-CJK-Sans elements** (matches D5-CENSUS-130); quotes defective 0 (35 curly, all in Newsreader); p8 extract 150/150.
- `run.py` (run3): TOTAL **150**, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`tools/head_check.py`: PASS 0 defects).
- `mechanism/d5_census.py`: **PASS — D5 Latin 0, D5 Cyrillic 0, curly-in-CJK 0**; curly total 35, all in Newsreader.
- `tools/occlusion_audit.py`: **0 flags** (selftest OK).
- `tools/p8.py`: extract 150/150; compare vs rebuilt core-de P8: `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]` — the same 4 expected reader-language items as rebuild 2.
- `tools/freeze.py`: baseline **8/8 SVGs byte-identical** (venv Pillow 13.0.0 / FreeType 2.14.3); diff pre-D5 baseline vs rebuilt: **added CJK characters 0** (added Latin strings 375 = D5 run-splitting).
- `tools/spill_sweep.py`: 32 boxes, 84 candidates, **0 SPILL**, 84 OBSERVE.
- `tools/boxtitle_check.py`: 46 titles, 244 body lines, **0 DEFECT**, 0 OBSERVE, 0 marginal. Coverage note: the tool only detects titles at ≥22pt (`TITLE_MIN_SIZE`); the P7 `DER WERKZEUGKASTEN　Toolbox` title sits at 21pt after the D5 fix, so it is not counted here — it is verified instead by the creambox audit (0 defects across all 32 boxes) and by direct ink measurement (right-edge spare 14.2px).
- `tools/pdf_edge_scan.py`: 8 pages, **0 TOUCH, 0 NEAR**.
- `tools/d5_creambox_audit.py` (pre-D5 baseline vs rebuilt): **PASS 0 defects**; ratios n=546, median 1.013, bold 1.042 / regular 0.982; P8 lines 231→229, footer slack 33.6→33.6px.
- Web/print text layer: `pdftotext` default mode — both **50,295 bytes** (8,135 words), word multiset identical, normalised text exactly identical; `-raw` mode — both 49,265 bytes, identical. (Rebuild 6 was 50,433 bytes; the −138 bytes are whitespace/line-break grouping from reflowed runs, zero word characters lost.)
- Pre-D5 web-PDF note (KIT wave 2 check): the web PDF on disk before this rebuild was sha `06030c9a…` (1,597,899 B), NOT the KIT's rebuild-6 record `2c190c75…` (1,597,904 B) — the rebuild-6 web PDF had been rebuilt without a KIT sync (5-byte webpdf nondeterminism, same class as the fix2 note). The print PDF on disk did match the KIT (`c8904dea…`). The D5 values above are measured from the actual files on disk.

## §7 Fan-out changes (explanation layer only — no German text, fact or key changed)

### Mechanism fixes (in `transform.py` / `build_edition.py` / `export_text_lang.py`)
- verify.py pointed at core-de (tilde-form path never matched the replace) →
  tilde-form replace first + asserts. Export failed (DE core has no `expl.py`) →
  synthetic `expl` module injected from `W47_GLOSS_PREFIX` / `W47_NOTE_WRAP`.
- P8 keys overflow (first build: keys ended 3336, bottom 2560) → wy kept at the
  core value 1650 (the +77 move was unnecessary and cost 308px); keys typography
  13.25 units / lh 1.18 / gap 4 / headers 16 / half-width parens / bare `·`
  (9.94pt, above the floor); P8 note shortenings (64 TR entries, ~757 chars in REG).
- `wrap()` glued Latin words across line boundaries ("DieBundesliga", "onMonday",
  the Q133 keydiff) → space-integrity sweep appended to `wrap()` in the edition's
  `svglib.py` (from `svglib_wrap_sweep.txt`, verified offline on all 16 keys paras).
- P8 battery header too wide → `B　WISSENSFRAGEN　Quiz` (W46 de-en precedent).
- p8 keydiff expectation corrected for W47: [137, 138, 139, 150] (Q140 is the
  reverse item, not a translation item).

### Layout / tuning (in `tr_en.py`, all measured, no content compromise)
- P1 ZAHLEN box jumped a column → items 2–3 shortened by one line each
  ("(Bayern v Cologne 20.30)", "(30 goals, matchday 9)"); flow ends 1554 = core.
- P5-ex overflow → four "Read the page N article…" instructions shortened to
  the 1-line form "Read page N, choose the right answer."; flow ends 2441 = core.
- P4 Und-Sie box overflowed into the results table → prompt shortened to
  "Bundesliga or national team? Who wins in Munich? Write two German sentences!"
  (2 lines, W46 form); box ends 1156.02, edge-touch like the core.
- P3 col3 overshoot (+120.6px) → ey 1620→1680 (hline 1668, col3 ends 1643.19,
  25px clear); P3 prompt NOT shortened (no faithful 2-line form exists).
- P5 col3 image crossed the caption hline → prompt shortened to "Making a
  calendar? What's on your wish list? Write two German sentences!" (2 lines);
  image ends 1732.93, hline 1744 clears by 11px; the P5 ey move was tried and
  reverted (it cost capacity).
- P7 Sätze overlap (+203.5px) → toolbox entries 3/5/6 shortened by one line each
  (UEFA detail dropped — it is in the P1 article; "..." marks dropped; "Whether …
  is open"); disclosure shortened to 3 lines ("Editor's example — no real letters
  had arrived by press time. Send us your writing for VOL.5."); toolbox pad
  110→90 (the pad is load-bearing — the formula underestimates ink advance by
  ~85px; a first attempt at 40 produced 3 occlusion flags and was corrected).
  P7 col3 ends 1518.0, 30px clear of the 1548 Sätze rule.
- Q150 key: dropped the redundant clause ("the model text is in the box on this
  page" — the box is on the same page); Q150 is already in the keydiff set.

### Rebuild 3 (2026-11-11 — core build15 Q34 change + one box-title fix)
- **Q34 stem change (the reason for this rebuild):** core-de build15 changed the
  P3 exercise Q34 stem from plural "Am Montag öffnen in Köln die ersten ___."
  to singular "Am Montag öffnet in Köln der erste ___." (key `Weihnachtsmarkt`
  unchanged). The edition was deleted and re-transformed from the new core.
  Verified: new stem 1x / old stem 0x in source, .text.md, P3 SVG, and both
  PDF text layers. P3 freeze sha changed accordingly (093cf378 → fc88f676);
  all other pages byte-identical to rebuild 2.
- **Box-title fix (real defect, found by boxtitle.py precheck):** P3
  "WEIHNACHTSWÖRTER　Christmas words" measured 483.5px vs the 400.5px box
  budget — the ink ran 83px past the cream box (visually confirmed on the
  rebuild-2 render). Shortened to "WEIHNACHTSWÖRTER　Words" (359.9px; bare-noun
  pattern as it/pt/es). boxtitle.py now 7/7. See EDITION-RECORD.md.
- New deliverables: print 10,966,409 B sha 47aae035…; web 1,555,605 B
  sha 37ba00d4…; text.md 49,665 B sha 2eb03632…. All gates green (see §6);
  P8 keys end 2481, flow ends otherwise identical to rebuild 2.

### Fix 1 (2026-11-11 — proof2 D1/D2 + appended D3; rebuild 4)

- **D1** (content8.py:201): P8 H writing instruction `“My week in November”` →
  `„My week in November“` (German quotes, as P5).
- **D2** (content56.py:99 — the P5 Q67 key note, printed into the P8 keys via REG;
  not content8.py, which holds no "Christkind" string): P8 key 67 note
  `“Im Lande des Christkinds”` → `„Im Lande des Christkinds“`, now identical to
  the P5 title/option. Key `B` unchanged.
- Both values fixed in the mechanism layer too (`scratch-fanout-de/tr_en.py:279`
  and `:141`); full-edition U+201D is 0 (SVG + text.md + both PDF text layers),
  U+201C = U+201E = 35 (all German „ " pairs, retained), U+2019 = 0.
- **D3** (content7.py only): P7 toolbox cream box was 0.4px short of the last
  baseline (box bottom 783.5 vs baseline 783.9, `fraglich` descender ~4.7px on bare
  paper). Root cause: the `tbh` formula missed the +20.5 first-baseline offset of
  every `p.para` call. Fixed by deriving `tbh` from the simulated ink end
  (last baseline + 16px): tbh 469.9, box bottom 799.9, clearance +16.0;
  LESERBRIEFE y 799.5 → 815.9, NOCH EIN WORT ends 1534.4 (13.6px clear of the
  1548 Sätze rule). No shared helper exists for `tbh` (inline per edition;
  core +110, all 10 de-* +90) — family-wide fix needs core + 10 editions;
  read-only scan: es/fr/it share the identical −0.4, ja/ko/zh-tw −0.8,
  nl/pt/ru baseline exactly on the bottom edge (+0.0, descenders spill).
  Refined creambox check (0–8px spill band, all 8 pages): NO OVERFLOW.
- Gates (fix1, see `scratch-fix-de-en1/GATE-LOG.md`): build_edition ALL GATES PASS
  (occlusion 0 flags; p8 150/150 CLEAN keydiff [137,138,139,150]; freeze diff exit 0,
  added CJK 7 × U+3000; print/web text identical 50,433B / raw 49,277B; chips 141;
  P8 min 9.94pt; measure 24/24; keycheck 149/150 with only the expected Q150
  truncation; freeze_direct rendered 8/8 with shas identical to rebuild 3;
  boxtitle 7/7 from the shipped SVG). Q34 new stem 1× in all 5 places, old 0×;
  content12.py:58 untouched.
- Build note: first rebuild failed only on webpdf (`ENOSPC`, /tmp 512M tmpfs 100%
  full with other agents' proof renders); rebuilt with `TMPDIR=<scratch>/tmp`,
  no /tmp files deleted. Web PDF is 42,277 B larger than rebuild 3 because the
  current worktree webpdf.py embeds Newsreader-Bold/Italic subsets (known tool
  version split, content-neutral).
- Known pre-existing inconsistency (not introduced by fix1, flagged for the
  coordinator): freeze_direct source level FAIL — the added literal
  `WEIHNACHTSWÖRTER　Words` is unaccounted because shared `tr_en.py` still says
  `Christmas words` (rebuild-A's fix never synced there); a future re-transform
  from shared tr_en.py would regress the box-title fix. Rendered freeze 8/8 PASS.
  (proof2 re-ran it after the shared tr_en.py sync at 09:37 UTC and got
  source level PASS, unaccounted 0/0 — see its PROOF-NOTE.)

### Fix 2 (2026-11-11 — proof2 D1/D2 still wide, rebuild 5 then rebuild 6)

- **Root cause (fix1's "same as P5 title" claim was wrong):** the characters
  were fixed (U+201D = 0) but the glyphs were not cured — U+201C is full-width
  (advance 40/40em) in Noto Sans CJK SC, its ink hugging the right edge of the
  cell: D1 gap 9.72pt = 0.49em, D2 gap 7.20pt = 0.72em. The other 33 „ " pairs
  render narrow in Newsreader (0.09–0.15em). Cure: a narrow glyph for the
  closing quote in these 2 sans strings.
- **Fix (edition `svglib.py` only; no string, key, or other pair touched):**
  `_char_font` routes U+201C in sans runs through the serif branch, so it
  renders in Newsreader; the `_PATH` rows for `("sans", bold, <class>)` are
  added by deriving the class name (`_char_font("“", "serif", False)`)
  instead of spelling the literal `'news'` — a spelled `'news'` fails
  freeze_direct's source level (no tr literal contains it; rebuild 5 did
  exactly that and failed). Characters stay U+201C everywhere, so
  U+201C = U+201E = 35, U+201D = 0, U+2019 = 0, and text.md is byte-identical
  (SHA unchanged). SVG census: exactly 2 U+201C in the edition were
  sans-rendered (both P8); now all 35 are Newsreader.
- **Rejected alternative:** ASCII `"` — PIL ink test: D1 0.77pt but D2
  −0.31pt (ink touches) and the straight shape mismatches the German „ pair.
- **Measured (400dpi pixel method, same single-window ink-column analysis
  as proof2; 200dpi full-band cross-check D1 2.16pt = 0.11em):**
  D1 gap **0.18pt = 0.01em**, D2 gap **0.72pt = 0.07em** (control P8 dialogue
  1.26pt = 0.09em by the same method); both ≤ 0.2em; 200dpi crops viewed.
  Key B (Q67) unchanged; keycheck 149/150 (only expected Q150 truncation);
  p8 CLEAN keydiff [137, 138, 139, 150]; freeze_direct source PASS (0/0),
  rendered 8/8 with shas identical to fix1; creambox refined NO OVERFLOW,
  P7 toolbox +16.0; boxtitle 7/7; Q34 new stem 1× / old 0×.
- Gates (fix2, see `scratch-fix-de-en2/GATE-LOG.md`): build_edition
  ALL GATES PASS (rebuild 6); measure 24/24; occlusion 0; print/web text
  identical 50,433B / raw 49,277B; chips 141; P8 min 9.94pt.
- **Regression risk (for the coordinator):** the fix lives in the edition's
  `svglib.py`, which transform re-copies from core-de — a future re-transform
  would drop it. The durable fix is the same routing in core-de/svglib.py
  (or a transform injection step); not done here (out of scope: no core-de /
  other-edition / tools/ changes).
- Build note: web PDF differs by 2 B between the two content-identical
  rebuilds (5→6, print PDF byte-identical) — webpdf nondeterminism,
  content-neutral (text layers identical, gates green).

### Apostrophe fix (rebuild 2, 2026-11-11 — found in visual proofread)
- **Defect:** 9 English strings used the curly apostrophe U+2019 ("Let's
  calculate", "This week's dates", "Editor's tip", "the league's return",
  "The editors' week", "the editors' practice example", "Readers' letters",
  "Editor's example", "Learners' four most common mistakes"). In Noto Sans CJK SC
  U+2019 renders as a wide full-width glyph — "Let' s calculate",
  "Editor' s tip" — visible on P2, P3, P4, P5, P6, P7. The straight apostrophe
  U+0027 renders tight ("Germany's five hot questions this week." on P1 was already
  correct and was the control).
- **Fix:** all 9 values in `tr_en.py` now use the straight apostrophe, written as
  the `\u0027` escape inside single-quoted strings (a raw `'` would terminate the
  literal — the first attempt broke `tr_en.py` with a SyntaxError and was fixed
  the same way). Rule added to the `tr_en.py` docstring. Rebuild 2 re-ran all
  gates (ALL GATES PASS) and the 5 magnified crops confirm the apostrophes now
  render tight; total U+2019 across the 8 SVGs is 0.
- **Lesson for the remaining 9 languages:** use straight apostrophes (U+0027,
  as `\u0027` in single-quoted strings) in every reader-language string from the
  start; add a U+2019 scan to the per-edition self-check.

### D5 font rebuild (2026-11-12 — rebuild 7)

- **Cause**: explanation-layer Latin rendered in Noto Sans CJK instead of Newsreader (SOP §1.1 font table). Pre-D5 census: 637 Latin-in-CJK-Sans elements. The fix2 curly-quote routing (rebuild 6) is preserved — the D5 installer re-verified it, routing assert 0 failures.
- **Fix (mechanism)**: `apply_variant.py` installed the D5 `_char_font` sans routing on the edition's `svglib.py` (Latin → Newsreader 400/600). No German text, fact, or key changed.
- **Eight D5-caused defects, all fixed in source and rebuilt (run3)** — the same defect class throughout: German bold-cap heads widen in Newsreader SemiBold and push the English tail (or the next line) out of its box:
  1. P1-fussball head `EINE WOCHE, ZWEI STIMMUNGEN` — HEAD TOO WIDE at 25pt; `content12.py:124` 25→22pt (411.8px fits the 422.5px column).
  2. P1 cream-box title `DIE WOCHE IN ZAHLEN　Numbers` — +13.8px past the box; `content12.py:43` `f.box(…, tsize=22)` (399.9px fits 404.5).
  3. P1 sommaire title `IN DIESER AUSGABE　In this issue` — +27.5px; `content12.py:89` 24→22pt (392.4px fits 400.5).
  4. P2 box title `DIE STILLE WOCHE　A quiet week` — +26.1px; `content12.py:221` 24→22pt (390.9px fits 400.5). (The P6 wide-box instance of the same string is unaffected — its box spans 3 columns.)
  5. P3 vocab-box title `WEIHNACHTSWÖRTER　Words` — +1.9px; `content34.py:58` 24→22pt (368.7px fits 400.5).
  6. P5 vocab-box title `ADVENTSWÖRTER　Advent words` — +30.4px; `content56.py:46` 24→22pt (395.2px fits 400.5).
  7. P7 toolbox title `DER WERKZEUGKASTEN　Toolbox` — +23.0px; `content7.py:93` 23→21pt (386.4px fits 400.5; 22pt still overflows by 4.2px, so 21pt is required here — and the title therefore falls below boxtitle_check's 22pt detection floor; see §6b coverage note).
  8. P4 "Und Sie" box, English gloss — the gloss wrapped to 3 lines in Newsreader (was 2 in CJK Sans) and its last line `sentences!` was 51% covered by the results-table band below (occlusion COVER); `content34.py:163,169` shortened the gloss to "Bundesliga or national team? Who wins in Munich? Write two sentences!" (drops "German" — the German prompt directly above still says "auf Deutsch"), which wraps to 2 lines again. The box-height formula recomputes from the new wrap, so no formula change was needed. This is the edition's only wording change in the D5 rebuild; the text export was re-generated and differs by exactly that one line (455).
- **Verification**: full gate re-run (§6b) — census 0, occlusion 0, p8 CLEAN, freeze 8/8, added CJK 0, spill 0, boxtitle 0, edge 0, creambox PASS, print/web text layers identical.
- Size rule learned (applies to the remaining de fan-outs): prefer 22pt fixes so titles stay inside boxtitle_check's detection; use 21pt only when 22pt still overflows.

### Reproof fix rebuild (2026-11-12 — rebuild 8)

- **Cause**: independent reproof of the D5 rebuild found 9 items (F7 major, rest minor) — see `hidden_files/w47/scratch-reproof-w47-de/PROOF-NOTE.md`.
- **Fix (in source, then rebuilt)**: F9 only — P8 `·` separators spaced (`"·".join` → `" · ".join`, 142 places; text.md `)·` count 0, P8 zoom verified). Gates: build ALL GATES PASS; boxtitle 0 DEFECT; spill 0 SPILL; edge 0/0; census-patched PASS; head_check PASS; text.md dry-run diff 9 lines (1 D5-era gloss + 8 P8), 0 dropped.
- **Verification**: full gate re-run (logs in `hidden_files/w47/scratch-fix-de/logs/`) — see the per-edition entry in `scratch-fix-de/FIX-LOG.md`.
- New deliverables: print 10,350,164 B sha `e861ff1d468d…`; web 1,510,214 B sha `8638905f9014…`; text.md 49,942 B sha `7f6f56e355f3…`.

### fix-de-minor1 (2026-11-13 — round-2 reproof C-1/C-2)

- **Fix (in source, then rebuilt)**: C-1 — P3 lead `die ersten Weihnachtsmärkte` contradicted the Hafenmarkt (open since 13 Nov, same article §2): P3 lead → `zwei große Weihnachtsmärkte` (same length, zero layout shift); the P5 lead carried the identical false claim and was fixed with the same wording; Q34 `Am Montag öffnet in Köln der erste ___.` → `Am Montag öffnen in Köln der Markt am Dom und der Markt der Engel, zwei große ___.` (word-box word and answer key `Weihnachtsmarkt` → `Weihnachtsmärkte`); Q80 `Am 16. November öffnen in Köln die ersten Weihnachtsmärkte.` → `Am 16. November öffnen der Markt am Dom und der Markt der Engel.` (answer stays `Richtig`). Q29 left unchanged (A2-acceptable per the brief; changing it would change the answer key). C-2 — P5 1903 calendar `Die Kinder konnten die Fenster mit Bildern überkleben.` → `Die Kinder konnten die Bilder ausschneiden und auf den Kalender kleben.` (the 1903 Lang/Kepler edition was windowless cut-and-paste). The `überkleben` gloss entry is left in place (the brief's fix is the sentence only; flagged to the coordinator). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p3, p5, p8 (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-fix-de-minor1/2026-w47-de-en/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 46 titles, 244 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal; spill 0 SPILL / 84 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 0 (reader layer; the shift vs the previous round's count is P3/P5/P8 re-wrap from the longer Q34/Q80 sentences, not content — the multiset proof below is authoritative), added Latin strings 445; print/web text layers multiset-identical (39,815 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: `die ersten`→`zwei große` ×3, `erste`→`Markt am Dom und der Markt der Engel` ×2, `Fenster mit Bildern überkleben`→`Bilder ausschneiden und auf den Kalender kleben`, footer/Q34-key changes where applicable); text.md re-exported from the fixed sources, diff exactly 7 lines (L309 P3 lead, L387 box, L389 Q34, L573 P5 lead, L577 C-2, L693 Q80, L1165 P8 answers Q34 key), 591 entries / 150 exercises. New deliverables: print 10,350,192 B sha `b66086e55ad4…`; web 1,510,233 B sha `0f09a21df893…`; text.md 50,011 B sha `ff7e31deda95…`. Not committed / not pushed (coordinator inserts).


### fix-de-round3 (2026-11-13 — round-3 reproof R3-F1/R3-F2)

- **Fix (in source, then rebuilt)**: R3-F1 — the C-2 fix (fix-de-minor1) removed `überkleben` from the P5 1903 sentence but left the orphan gloss entry in the P5 gloss (`content56.py:23`); SOP §8.1 requires every glossed word to occur in the text, so the ` · überkleben …` segment was deleted from the P5 gloss (gloss shortens by one entry, layout-safe). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p5 only (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-reproof-de-round3/2026-w47-de-en/fix-round3/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 46 titles, 244 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal; spill 0 SPILL / 84 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 0, added Latin strings 445; print/web text layers multiset-identical (39,788 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: gloss `überkleben …` entry removed); text.md re-exported from the fixed sources, diff exactly L585 P5 gloss, 591 entries / 150 exercises. New deliverables: print 10,350,173 B sha `aaaad1ed122a…`; web 1,510,219 B sha `6e50a693d200…`; text.md 49,975 B sha `6fb1fb37415b…`. Not committed / not pushed (coordinator inserts).
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
