# WEEKLY-KIT — 2026-W47 · German edition for Dutch-speaking readers

- Edition: `2026-w47-de-nl` — German target text, Dutch explanations
- Week: Mon 2026-11-16 – Sun 2026-11-22 · VOL.4 · Press time: Mon 2026-11-09
- Lead story: **Die Bundesliga kehrt zurück — Bayern gegen Köln** (40 chars, limit 56)
- Status: fan-out complete (rebuild-B), all self-check gates green on the FIRST
  rebuild run, visual proofread 8/8 pages zero findings (rebuild-B build 1,
  2026-11-11); independent proofread pending (coordinator to assign). Fix1 rebuild
  (2026-11-11, D1 toolbox-pad + rail-raise fix only, all gates green again;
  independent proof2 pending — coordinator to assign). New standing gates
  (2026-11-12) found 1 boxtitle defect (P1 sommaire title +26.5px); rebuild
  fix2 (2026-11-12) repaired it by layout only, all gates green again.
- **D5 font rebuild applied 2026-11-12 (rebuild fix3, all gates green — see §7)**
  Build 1 (2026-11-11 06:46 UTC, 5th shift) also passed all gates first run;
  this rebuild only carries the core build15 Q34 stem correction (see §7).
- Source: `core-de/` build15 (2026-11-11 08:02 UTC, proof5 (a) zero findings)
  copied and translated in the explanation layer only. German target text is
  frozen — see §6 for the proof.
- Builder: de fan-out builder B (rebuild wave, 2026-11-11). Scratch:
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-de/`
  (`tr_nl.py`, `transform.py`, `build_edition.py`, `nl/` gate logs).

## §1 Contents

8 pages, 1950×2700, 4 columns. **150 exercises**, continuous numbering 1–150, all in
the registry. Identical layout and exercise set to the core; only the explanation
layer (bridges, instructions, glosses, notes, toolbox, disclosure, keys notes) is Dutch.

| Page | Section | Level | Ex. |
|---|---|---|---|
| P1 | Front: lead + Fragen der Woche + inhoud + word of the week + Blitzquiz | A2 | 10 |
| P2 | Leben: Buß- und Bettag & Alltag + Rechnen | A2 | 18 |
| P3 | Kultur: Weihnachtsmärkte & stille Woche (1930 painting) | A2→B1 | 18 |
| P4 | Sport: results 3–8 Nov + fixtures table + MD10 return | B1 | 18 |
| P5 | Jugend: Adventskalender basteln + Wochenplan (1903 calendar) | B1 | 18 |
| P6 | Vertiefung: stille Woche & Haushalt 2027 + practice chart | B2 | 18 |
| P7 | Sprache: A2/B1/B2 lessons + Sätze der Woche + Fehlerklinik + Leserbriefe + VOL.5 teaser | A2/B1/B2 | 12 |
| P8 | Schlusstest + Schreiben (MUSTER 84 words) + all answers | mixed | 38 |

Levels: A2 69 / B1 67 / B2 14. Types: meerkeuze 52 / invullen 41 /
omzetten 11 / juist of onjuist 8 / gatentekst 8 / zinnen bouwen 8 /
combineren 12 / vertaling 4 / dialoog aanvullen 5 / schrijven 1.

Pairing furniture (VOL.4): masthead `Die Lucerna`; edition line
`DUITS WEEKBLAD　VOL.4　BUNDESLIGA TERUG　RUSTIGE WEEK`; footer
`Die Lucerna　DUITS WEEKBLAD VOL.4　Duitse tekst　Nederlandse uitleg`;
page line `Pagina N van 8`; gloss prefix `Uitleg — `.

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
  carries the labelled editor's example + the Dutch disclosure:
  "Voorbeeld van de redactie: er was nog geen echte brief binnen voor de deadline.
  Stuur je teksten voor VOL.5!"

## §4 Images

Identical to the core (see `core-de/WEEKLY-KIT.md` §4 and `assets/CREDITS.md`):
fussball.jpg (P1), kopfball.jpg (P4), weihnachtsmarkt1930.jpg — Wilhelm Ritter 1930
(P3), christkind.jpg — Richard Ernst Kepler 1903 (P5), lesesaal.jpg — Carol M.
Highsmith, Library of Congress (P7), fussball1905.jpg (P8). All public domain, each
with target-language caption + printed credit.

## §5 Build / reproduction

- Build dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-de-nl/`
  (build code + deliverables, copied from `core-de/` by `transform.py nl`).
- Reproduce: `tools/venv/bin/python transform.py nl` (from scratch-fanout-de) →
  `tools/venv/bin/python measure.py nl <edition-dir>` →
  `tools/venv/bin/python build_edition.py nl` (run.py → render.py → webpdf →
  verify → occlusion → p8 → freeze → pdftotext → chips → export).
  Build interpreter is `tools/venv/bin/python` (PIL 13.0.0); freeze was re-run with
  the same interpreter (system python3 has PIL 10.2.0 and measures 1.1% differently).
- Deliverables (fix-de-round3 rebuild, 2026-11-13; reproof fix rebuild, 2026-11-12 superseded):
  - Print PDF: `Die-Lucerna-VOL4-de-nl.pdf` — 10,347,280 bytes, 8 pages,
    sha256 `5dd1a9bb6b67690be6c2fa9195c8a23c6acd7e483b9c51f40e0ce080f9c191e9`
  - Web PDF: `Die-Lucerna-VOL4-de-nl-web.pdf` — 1,507,329 bytes (< 7 MB),
    50,417 text bytes,
    sha256 `049a48c9145882998f873ea6a121f67c7d4acb15d9041b07784a48a21a5aa8d0`
  - Text export: `2026-w47-de-nl.text.md` — 49,770 bytes, 48,128 chars,
    591 entries, 150 exercises,
    sha256 `7cee007495073fcd5c882f937b2595cf1b8c2dcc247fb21b07bbf39815ddc5f7`
    (changed — wording fixed per the §7 reproof fix entry; re-exported from the fixed sources)
    (exported from production sources in reading order, never from PDF)
  - `ABSTRACT.txt` (one line, Dutch, no ASCII double quotes):
    "Die Lucerna Duits weekblad VOL.4: de Bundesliga is terug (Bayern ontvangt
    Köln), beslissende Nations League tegen Nederland, dag van boete en gebed en
    zondag van de doden, opening van de kerstmarkten van Keulen, Europese en
    Bundesliga-uitslagen van 3 tot 8 november; Duitse tekst, Nederlandse uitleg,
    niveaus A2–B2, 150 oefeningen bij de thema's van de week."

## §6 Gates (rebuild-B build 1, 2026-11-11 — final)

- `run.py` (build.log): exit 0, **zero FLOW OVERFLOW / HEAD TOO WIDE**, TOTAL 150.
  Flow ends: P1-headline 1554 (= core), P1-fussball 2264, P1-quiz 2523,
  P2-feature 993, P2-ex 2332, P3-main 916, P3-ex 2333, P4-main 706, P4-ex 2315,
  P5-main 1026, P5-ex 2441 (= core), P6-main 777, P6-ex 2523, P7-A2 1278 / B1 1342 /
  B2 1306, P8-battery 1409, P8-keys 2457 (bottom 2560, spare 103px).
- `measure.py`: **24/24 PASS, 0 FAIL** (measure1.log).
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
  **Direct freeze proof (8/8, `nl/freeze-direct.json`, script `freeze_direct.py`):**
  (a) source-level: AST string-literal multiset core vs edition — 0 unaccounted
  removed, 0 unaccounted added (521 removed / 529 added, identical to build 1;
  every one accounted for
  by the translation module, the CJK inventory, or a documented transform artifact);
  (b) rendered-text level: the frozen intersection (strings identical in core and
  edition SVGs) per page — P1 147, P2 163, P3 195, P4 166, P5 173, P6 175, P7 150,
  P8 186 strings, sha256 083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 /
  2bbe05f9 / b7aa0771 / 57e118e7 — identical to build 1 except P3 (the Q34 stem
  page), as the frozen content is the shared German text.
- Print/web text layer: `pdftotext` default mode — print 50,192B / web 50,192B,
  **word multiset identical**; `-raw` mode — both 49,003B, normalised text
  **exactly identical**. Web PDF has a real text layer.
- Level chips (rx="2.7" rects): per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18,
  7:12, 8:35}, **TOTAL 141**; P8 by level A2 22 / B1 13 / B2 0. The core's
  missing-14 set is fully present: cloze options Q113–120 (8 A2 chips),
  dialogue badges Q145–149 (145–147 A2, 148 B1, 149 A2), writing title chip
  (B1 on "H SCHREIBEN").
- P8 answers measured font size: keys 13.25 SVG units = **9.94 PDF pt**
  (PyMuPDF re-measured P8 minimum span 9.94pt) — above the 9.75pt floor
  (concession step 4; P8 stems stay at the core's 15.375pt).
- 150-question key check (independent, `nl/keycheck-150.json`, script
  `keycheck.py`): P8-SVG-extracted keys vs the REG built from the edition's own
  sources — **149/150 exact**; the single non-exact item is Q150, the open
  writing task, where the extractor truncates the REG key "Open opdracht — volg
  de punten in het schrijfblok" to "Open opdracht" (expected; Q150 is already
  in the keydiff set). REG by page
  {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}; levels A2 69 / B1 67 / B2 14.
- U+2019 scan over the 8 SVGs: **0** (straight U+0027 throughout, as `\u0027`
  escapes in `tr_nl.py`).
- Visual proofread: all 8 pages re-rendered from the print PDF at 100 dpi and
  viewed one by one (P1–P8), plus a systematic SVG-level scan of the 7 col3
  box titles (8 instances incl. the P6 full-width box): all end ≤ 1862.0
  (max 1857.0, DER WERKZEUGKASTEN "Werktuig", 5.0px margin). **Zero findings**
  (see §7). The P8 keys were spot-checked against the registry (dates, scores,
  times, grammar keys, MUSTER 84 words, chart 44+33+23=100).

### Rebuild fix1 (2026-11-11 — D1 only)
- **D1 (de-es proof1 family defect, reproduced on nl pre-fix):** P7
  DER WERKZEUGKASTEN cream box too short — box bottom 813.0, last entry
  `Es ist fraglich, ob ... = nog onzeker` baseline 813.0 (clearance +0.0, baseline
  exactly on the box edge), `fraglich` descender ink ~4.7 below the box. Root cause
  (measured per-edition): the `tbh` formula in `content7.py:76` counts `n*29.5+6` per
  entry but the real advance is `20.5 + n*29.11 + 6` (`Page.para` first-baseline
  offset, 6 entries = +123 missed); nl wraps Σlines=10, so clearance = pad − 90.0
  and pad 90 gave +0.0. Core-de uses pad 110 (+18.8); the fan-out had cut it to 90
  with a "validated by occlusion 0 flags" comment — void, since the occlusion audit
  cannot see text spilling past its own box (nothing covers it).
- **Why not a flat pad 110:** nl's NOCH EIN WORT already ends at 1547.5, 0.5px before
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
  text.md byte-identical (sha e904fb3d…); freeze_direct 8/8 with all 8 page shas
  identical to rebuild-B (083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 /
  2bbe05f9 / b7aa0771 / 57e118e7).
- New deliverables: print 10,964,697 B (−2 B) sha
  `c8a5f5e2ea2affc15df0aef472ce08f74e3ae5cc826d2ef49d636c866c083521`; web 1,596,830 B
  (+42,976 B — working-tree webpdf.py now embeds the `LucernaNewsreader-Bold` subset,
  22,408 B; same effect as es/fr/it/pt/ko/zh-tw; < 7 MB, text layer identical to print)
  sha `4ed5b46e385815a4358cb01407e0a476f69cdc9885801756998410fd5e336d8a`; text.md 49,403 B
  sha e904fb3d… (unchanged). All gates green (occlusion 0 flags real run, p8 CLEAN
  keydiff [137,138,139,150], freeze diff +7 CJK all U+3000, freeze_direct 8/8 source
  PASS, keycheck 149/150 — Q150 extractor truncation only, boxtitle 7/7, d2scan 54
  pairs 0 web gaps >0.5pt, P8 min 9.94pt, chips 141, verify TOTAL 150, bent quotes
  U+201C 33 / U+201D 0, Q34 new stem 1x in all five places). Gate logs in
  `hidden_files/w47/scratch-fix-de-toolbox-family/gates-nl/`; build logs in
  `hidden_files/w47/scratch-fanout-de/nl/`.

### Rebuild fix2 (2026-11-12 — boxtitle gate fix, P1 only)
- **Defect (new standing gate `tools/boxtitle_check.py`, 130-wide run
  2026-11-12):** P1 sommaire title `IN DIESER AUSGABE　In dit nummer` ran
  past its cream box by **+26.5px** (core-de fits at −22.0px); visually
  confirmed (the whole gloss `In dit nummer` ends on white paper past the
  box edge).
- **Fix (edition-local, `content12.py:89` only):** sommaire title font size
  24 → 22 (layout only, no text changed). Predicted and verified: ink end
  1888.5 → **1852.5**, margin **+9.5px**. No other line touched.
- New deliverables: print 10,964,699 B (+2 B) sha
  `55489de172f5743e6480b939ba485a6c8be34029d37f53de0e0acaf2d59e4b72`; web
  1,596,814 B (−16 B) sha
  `56aeb8cd7bedd98fc8a96a7175a583b8183333ab1aa457e4fac3992f857c5734`; text.md
  49,403 B sha e904fb3d… (unchanged). All gates green on the rebuilt edition:
  boxtitle **0 DEFECT / 0 OBSERVE / 0 marginal** (also 0 on the synced
  production files), verify TOTAL 150 + SVGs byte-identical after re-run,
  occlusion 0 flags, p8 extract 150/150 + compare CLEAN keydiff
  [137,138,139,150], freeze `diff` exit 0 (added CJK 7, all U+3000) +
  freeze-direct rendered **8/8** with all 8 frozen SHAs identical to rebuild
  fix1 (083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 /
  b7aa0771 / 57e118e7). NOTE (pre-existing, not this fix): freeze-direct
  *source* level now reports 1 unaccounted removed literal (`'sans'` ×2 in
  `svglib.py`) — core-de's `svglib.py` was patched (fix2 U+201C routing,
  2026-11-11 22:35) after nl was copied from it; at fix1 time the source
  level PASSED. This fix changed one int + one comment, no string literal.
  Gate outputs in `scratch-gatefix-de-en/2026-w47-de-nl/` (FIX-LOG.md).

## §6b Gates (D5 font rebuild round, rebuild fix3, 2026-11-12 — full re-run on the rebuilt edition; scratch `hidden_files/w47/scratch-d5-de/de-nl/`)

- D5 mechanism: `apply_variant.py --svglib … --target de --reader nl` (mode latin) on the edition's `svglib.py`; fix2 curly-quote routing installed with it (routing assert `ROUTING FAILURES: 0`). Pre-D5 `svglib.py` backed up as `svglib.py.pre-d5`. Pre-D5 baseline verified CLEAN before install: the production dir was copied to scratch and rebuilt with the venv interpreter — freeze baseline **8/8 SVGs byte-identical** to the delivered SVGs (`freeze-pre-baseline.log`). Pre-D5 production snapshot in `scratch-d5-de/de-nl/baseline/` (SVGs + sources, rebuild-fix2 state). KIT wave 2 check: pre-D5 print SHA matches the KIT (`55489de1…`), but the pre-D5 web PDF on disk was sha `56aeb8cd…` (1,596,814 B), NOT the KIT's rebuild-fix2 record `4ed5b46e…` — the rebuild-fix2 web PDF had been rebuilt without a KIT sync (same class as de-en/de-fr/de-it). The D5 values above are measured from the actual files on disk.
- Pre-D5 D5 census: **636 Latin-in-CJK-Sans elements** (matches D5-CENSUS-130); quotes defective 0; p8 extract 150/150.
- `run.py` (run2): TOTAL **150**, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`tools/head_check.py`: PASS 0 defects).
- `mechanism/d5_census.py`: **PASS — D5 Latin 0, D5 Cyrillic 0, curly-in-CJK 0**.
- `tools/occlusion_audit.py`: **0 flags** (selftest OK; fixed tool — bare `Noto Sans` runs measured on the non-CJK face, brief §10).
- `tools/p8.py`: extract 150/150; compare vs rebuilt core-de P8: `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]` — the same 4 expected reader-language items as rebuild-B.
- `tools/freeze.py`: baseline **8/8 SVGs byte-identical** (venv Pillow 13.0.0 / FreeType 2.14.3); diff pre-D5 baseline vs rebuilt: **added CJK characters 0** (added Latin strings 371 = D5 run-splitting).
- `tools/spill_sweep.py`: 32 boxes, 84 candidates, **0 SPILL**, 84 OBSERVE.
- `tools/boxtitle_check.py`: 44 titles, 244 body lines, **0 DEFECT**, 0 OBSERVE, 0 marginal (real backup comparison: `scratch-d5-de/scratch-fanout-de/backup/2026-w47-de-nl`). Coverage note: the two fixed 20pt titles (P1 sommaire, P7 Werktuig) sit below the tool's 22pt detection floor — they are verified instead by the creambox audit (0 defects across all 32 boxes) and by direct ink measurement (spare 18.5px / 18.8px).
- `tools/pdf_edge_scan.py`: 8 pages, **0 TOUCH, 0 NEAR**.
- `tools/d5_creambox_audit.py` (pre-D5 baseline vs rebuilt): **PASS 0 defects**; ratios n=546, median 1.011, bold 1.040 / regular 0.980; P8 lines 230→228, footer slack 33.6→33.6px.
- Web/print text layer: `pdftotext` default mode — both **50,067 bytes**, word multiset identical, normalised text exactly identical; `-raw` mode — both 48,995 bytes, identical.

## §7 Fan-out changes (explanation layer only — no German text, fact or key changed)

- **Rebuild-B (2026-11-11):** core-de build15 corrected the P3 Q34 stem to the
  singular form matching key `Weihnachtsmarkt` (the D-01 stem/key mismatch from
  the de-fr first-round proof, resolved at the core). This edition was deleted
  and re-transformed from the new core with unchanged `tr_nl.py` /
  `vals_nl.json`; the rebuild passed all gates first run with no fixes, and the
  visual proofread (P1–P8 at 100 dpi, /tmp/nl-rb-proof-*.png) found zero
  findings. Only delta vs build 1 is that one stem string (P3); all flow ends,
  chips, keys and frozen sha8 are otherwise identical (only P3 sha8 moved).
- **Build 1** passed all gates and the visual proofread with zero findings, so
  no rebuild was needed then.
- **Apostrophe rule applied from the start:** `tr_nl.py` was written with straight
  apostrophes U+0027 throughout (as `\u0027` escapes inside single-quoted
  strings); U+2019 scan over the 8 SVGs is 0.
- Box titles (from the 5th-baton sweep, before build 1): STILLE "De stille week"
  → "Stille week"; WEIHNACHTSWÖRTER "Kerstwoorden" → "Kerst"; ADVENTSWÖRTER
  "Adventswoorden" → "Advent"; TOOLBOX "Gereedschap" → "Werktuig" (395.5px, 5px
  margin, deterministic) (boxtitle.py 7/7).
- Dutch-specific value fixes made during validation (before build 1, in
  `vals_nl.json`): gloss prefix "Opgelet — " corrected to "Uitleg — " (Opgelet is
  for warnings; the P2 note correctly keeps "Opgelet:"); a typo'd key
  "beginnen → begint" corrected to "beginnen → beginnt" (German verb forms stay
  identical).
- **Rebuild fix2 (2026-11-12 — boxtitle gate fix; LAYOUT only):** P1 sommaire
  title `IN DIESER AUSGABE　In dit nummer`: fs 24 → 22 (`content12.py:89`);
  ink 1888.5 → 1852.5 (+9.5px margin). No text changed, no other line
  touched. See §6 Rebuild fix2.

### D5 font rebuild (2026-11-12 — rebuild fix3)

- **Cause**: explanation-layer Latin rendered in Noto Sans CJK instead of Newsreader (SOP §1.1 font table). Pre-D5 census: 636 Latin-in-CJK-Sans elements.
- **Fix (mechanism)**: `apply_variant.py` installed the D5 `_char_font` sans routing on the edition's `svglib.py` (Latin → Newsreader 400/600; fix2 included). No German text, fact, or key changed; no wording changed at all.
- **Six D5-caused defects, all fixed in source and rebuilt (run2)**:
  1. P1-fussball head `EINE WOCHE, ZWEI STIMMUNGEN` — HEAD TOO WIDE at 25pt; `content12.py:124` 25→22pt (411.8px fits the 422.5px column).
  2. P1 cream-box title `DIE WOCHE IN ZAHLEN　In cijfers` — +9.8px past the box; `content12.py:43` `f.box(…, tsize=22)` (396.6px fits 404.5).
  3. P1 sommaire title `IN DIESER AUSGABE　In dit nummer` — +19.5px; `content12.py:89` 22→20pt (382.0px fits 400.5; 21pt still +0.6px over). Note: the rebuild-fix2 fix (24→22) held under CJK Sans but not under Newsreader SemiBold — the D5 widening re-broke it, so the fix2 "22 fits (+9.5px margin)" comment is now stale and was replaced.
  4. P2 box title `DIE STILLE WOCHE　Stille week` — +3.1px; `content12.py:221` 24→22pt (369.4px fits 400.5).
  5. P7 toolbox title `DER WERKZEUGKASTEN　Werktuig` — +39.0px, the widest box-title overrun in the de family; `content7.py:80` 23→20pt (381.7px fits 400.5; 21pt still +0.3px over).
  6. P8 battery head `F　WÖRTER PAAREN　Combineren` — HEAD TOO WIDE at 24pt (440.9px > 422.5px column); `content8.py:149` 24→22pt (404.2px fits).
- **Verification**: full gate re-run (§6b) — census 0, occlusion 0, p8 CLEAN, freeze 8/8, added CJK 0, spill 0, boxtitle 0 (real backup), edge 0, creambox PASS, print/web text layers identical in both modes.
- Note: the P1 masthead subtitle never collided with the headline in this edition.

### Reproof fix rebuild (2026-11-12 — rebuild 8)

- **Cause**: independent reproof of the D5 rebuild found 9 items (F7 major, rest minor) — see `hidden_files/w47/scratch-reproof-w47-de/PROOF-NOTE.md`.
- **Fix (in source, then rebuilt)**: F7 — P1 kicker shortened to `HET DUITS VAN DUITSERS` (advance gap 31.0px, P1 render verified); F1 — P5 UND SIE prompt gained the advent-calendar question; F9 — P8 `·` spaced (142 places). Knock-on: P5 image gap 26→14px (image ends 1749.93). Gates: build ALL GATES PASS; boxtitle 0 DEFECT; spill 0 SPILL; edge 0/0; census-patched PASS; head_check PASS; text.md dry-run diff 10 lines, 0 dropped.
- **Verification**: full gate re-run (logs in `hidden_files/w47/scratch-fix-de/logs/`) — see the per-edition entry in `scratch-fix-de/FIX-LOG.md`.
- New deliverables: print 10,347,239 B sha `6a452b7accfb…`; web 1,507,275 B sha `3c0e337e55b4…`; text.md 49,713 B sha `551f278a1026…`.

### fix-de-minor1 (2026-11-13 — round-2 reproof C-1/C-2 + de-nl gloss fix)

- **Fix (in source, then rebuilt)**: C-1 — P3 lead `die ersten Weihnachtsmärkte` contradicted the Hafenmarkt (open since 13 Nov, same article §2): P3 lead → `zwei große Weihnachtsmärkte` (same length, zero layout shift); the P5 lead carried the identical false claim and was fixed with the same wording; Q34 `Am Montag öffnet in Köln der erste ___.` → `Am Montag öffnen in Köln der Markt am Dom und der Markt der Engel, zwei große ___.` (word-box word and answer key `Weihnachtsmarkt` → `Weihnachtsmärkte`); Q80 `Am 16. November öffnen in Köln die ersten Weihnachtsmärkte.` → `Am 16. November öffnen der Markt am Dom und der Markt der Engel.` (answer stays `Richtig`). Q29 left unchanged (A2-acceptable per the brief; changing it would change the answer key). C-2 — P5 1903 calendar `Die Kinder konnten die Fenster mit Bildern überkleben.` → `Die Kinder konnten die Bilder ausschneiden und auf den Kalender kleben.` (the 1903 Lang/Kepler edition was windowless cut-and-paste). The `überkleben` gloss entry is left in place (the brief's fix is the sentence only; flagged to the coordinator). **de-nl fix (edition-local, `content12.py:175`, P2 gloss)**: `die Pflegeversicherung = zorgverzekering` → `die Pflegeversicherung = verzekering voor langdurige zorg` (`zorgverzekering` is health insurance, not German long-term care insurance). Longer gloss reflows inside the P2 flow with no spill (boxtitle 0 DEFECT, spill 0 SPILL). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p2, p3, p5, p8 (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-fix-de-minor1/2026-w47-de-nl/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 44 titles, 245 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal; spill 0 SPILL / 85 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 0 (reader layer; the shift vs the previous round's count is P3/P5/P8 re-wrap from the longer Q34/Q80 sentences, not content — the multiset proof below is authoritative), added Latin strings 441; print/web text layers multiset-identical (39,736 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: `die ersten`→`zwei große` ×3, `erste`→`Markt am Dom und der Markt der Engel` ×2, `Fenster mit Bildern überkleben`→`Bilder ausschneiden und auf den Kalender kleben`, footer/Q34-key changes where applicable); text.md re-exported from the fixed sources, diff exactly 8 lines (the 7 base lines + L199 P2 gloss `die Pflegeversicherung = verzekering voor langdurige zorg`), 591 entries / 150 exercises. New deliverables: print 10,347,296 B sha `1d4c645161a6…`; web 1,507,342 B sha `0290b9fed3d1…`; text.md 49,799 B sha `7bdeb33cfc1c…`. Not committed / not pushed (coordinator inserts).


### fix-de-round3 (2026-11-13 — round-3 reproof R3-F1/R3-F2)

- **Fix (in source, then rebuilt)**: R3-F1 — the C-2 fix (fix-de-minor1) removed `überkleben` from the P5 1903 sentence but left the orphan gloss entry in the P5 gloss (`content56.py:23`); SOP §8.1 requires every glossed word to occur in the text, so the ` · überkleben …` segment was deleted from the P5 gloss (gloss shortens by one entry, layout-safe). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p5 only (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-reproof-de-round3/2026-w47-de-nl/fix-round3/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 44 titles, 245 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal; spill 0 SPILL / 85 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 0, added Latin strings 441; print/web text layers multiset-identical (39,713 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: gloss `überkleben …` entry removed); text.md re-exported from the fixed sources, diff exactly L585 P5 gloss, 591 entries / 150 exercises. New deliverables: print 10,347,280 B sha `5dd1a9bb6b67…`; web 1,507,329 B sha `049a48c91458…`; text.md 49,770 B sha `7cee00749507…`. Not committed / not pushed (coordinator inserts).
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
