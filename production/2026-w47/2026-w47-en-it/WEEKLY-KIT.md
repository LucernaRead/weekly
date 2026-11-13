# WEEKLY-KIT — 2026-W47 en-it (English target, Italian reader)

## 1. Identity
- Slug: `2026-w47-en-it`
- Target language: English (en). Reader language: Italian (it).
- Issue week: Monday 16 – Sunday 22 November 2026. VOL.4.
- Core: `production/2026-w47/core-en/` (en-zh-cn), copied whole, explanation layer rewritten in Italian.
- Exercises: 150 (registry 150; per page 10/17/18/18/18/18/12/39; A2 62 / B1 66 / B2 22).
- MODEL words: 82.

## 2. Files delivered
- 8 SVG (`svg/p1-front.svg` … `svg/p8-test.svg`) + 8 card PNGs (`cards/`).
- Print PDF: `The-Lucerna-VOL4-en-it.pdf` — 28,841,732 bytes,
  SHA-256 `0062f3d9b875c63abc96e0211f980bb2d2162b7a49f5a26db156a15f4bd680f7`.
  [D5 rebuild, 12 Nov 2026 — see §3; pre-D5 values were print `2db4dad1…` 29,327,187 B,
  web `510a03ad…` 2,408,878 B.]
  [F1 fix, 12 Nov 2026 — see F1 bullet below; pre-fix values were print `7efa7263…` 28,841,334 B,
  web `681f6184…` 2,330,533 B.]
- Web PDF: `The-Lucerna-VOL4-en-it.web.pdf` — 2,330,932 bytes,
  SHA-256 `24ad7443e932c63624c050d9c9c6e3e79c4947180993449833e32d441fd2896e`
  (built only with `tools/webpdf.py`; text layer 38,339 chars, identical to the print extraction — token-multiset diff 0/0; per-page byte-identical 8/8).
- `2026-w47-en-it.text.md` — 54,115 bytes, SHA-256 `3d6c872ff631d267f202e0b9ecc56ded477a63068c4e492f8747099e5c3790a0`, exported from the build source (never from the PDF);
  stub registry 150 = real registry 150. Re-exported in the F1 fix (12 Nov 2026, see F1 bullet below; pre-fix 53,944 B `a8330625…`).
- **F1 fix (12 Nov 2026, proof-round defect F1 — Georgia runoff written as pending; work log in `hidden_files/w47/scratch-fix-en/FIX-LOG.md`, gates in `hidden_files/w47/scratch-fix-en/logs/2026-w47-en-it/`):** P2 :185 + P6 :651 rewritten as settled law + result (Georgia law calls for a Dec 1 runoff only if no one wins a majority — AP called Jon Ossoff reelected 3 Nov, ~59%, so no runoff). Q13/Q142 untouched (rule questions, answers still 1 December). Source `content12.py:171` + `content56.py:103`; text.md re-exported with `scratch-fix-en/make_textmd_fix.py` (diff exactly the 2 lines, no title lost — all 7 D5-shrunk box titles present). Full rebuild + gates ALL-GREEN: run rc=0 TOTAL 150 MODEL 82, 0 overflow; head_check PASS; occlusion 0 flags (selftest OK); p8 extract 60/150, compare CLEAN, keydiff=[137, 138, 139, 140, 150] (expected); freeze baseline 8/8; spill 0; boxtitle 0; edge 0; creambox PASS; census PASS; print/web text layers byte-identical. New deliverables: print 28,841,732 B SHA-256 `0062f3d9b875…` (was 28,841,334 B `7efa7263…`), web 2,330,932 B `24ad7443…` (was 2,330,533 B `681f6184…`), text 54,115 B `3d6c872f…` (was 53,944 B `a8330625…`); text layer 38,339 chars (was 38,207).
- `ABSTRACT.txt` — one line, Italian, no ASCII double quotes.
- `registry.json` — fresh dump (150 keys; SHA-256 `55b9fe3c6e3d6b12a33da1a21b592dd31f75f62d863b9ebcb46ebe3a02ad07d2`), only Q73 changed vs the shipped copy.

## 3. Gates (all green, delta rebuild 2026-11-11 — Q73 sync only; see §5 item 6)
- run.py exit 0; 0 FLOW OVERFLOW / HEAD TOO WIDE; every Flow end y ≤ its bottom
  (P8-keys 2443/2560; P1-headline 1779/1828; P1-countries 2298/2300; P2-feature 1497/1540;
  P2-ex 2532/2560).
- occlusion audit: 0 flags (selftest OK).
- p8 extract: 60/150 noted (same set as core); compare CLEAN; keydiff [137, 138, 139, 140, 150]
  (reader-language translation keys + writing key — expected).
- freeze baseline tool: 8/8 byte-identical; direct sha256 re-render vs shipped core SVGs: 8/8 MATCH.
  Freeze diff: added CJK = only 9× U+3000 separators; removed = core Chinese layer.
- print/web text token-multiset diff: 0/0 (47,988 chars each; token-multiset diff 0/0; per-page byte-identical 8/8).
- `check_s11.py it`: ALL §1.1/P8 CHECKS PASS (colour set core 19 = edition 19;
  badge colours A2 #5c6e30 / B1 #46581f / B2 #37402f; P8 min font 13.5 pt ≥ 9.75;
  chip-rect counts = core per page; Q113–120 options line with [A2] tag present;
  "Levels: 145–149 [A2]" present; Q120 [A2] chip OK;
  P8 WRITING head "H　WRITING　Scrittura [B1]" present).
- **D5 rebuild + gates (12 Nov 2026; full log `hidden_files/w47/scratch-d5-rebuild-en/logs/2026-w47-en-it/GATES-SUMMARY.txt`)**: SOP §1.1 font fix — installed via `scratch-d5-plan/mechanism/apply_variant.py --target en --reader it` (D5 block in this edition's `svglib.py`, `_D5_READER = "latin"`; routing unit-checked: `check_routing.py` FAILURES: 0; U+201C fix2 routing preserved — census: curly in CJK 0, all 164 curly quotes in Newsreader). Pre-fix census: 542 Latin-in-CJK-sans elements. Post-fix defects, all D5-caused: (1) P6 head `READ THE CHART　Leggi il grafico` HEAD TOO WIDE +26.4 px advance at 25 → head size 25 → 23 (`content56.py:112`); (2) P7-col3 head `AN EXAMPLE LETTER　Esempio` HEAD TOO WIDE +8.0 px advance at 25 → head size 25 → 24 (`content7.py:104`); (3) P1 cream-box title `THE WEEK IN NUMBERS　In cifre` +3.5 px right → `tsize` 23 → 22 (`content12.py:43`). Layout only, text unchanged. Gates: run rc=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; `head_check.py` PASS 0 defects; `render.py` + `webpdf.py` rc=0; `occlusion_audit.py` 0 flags (selftest OK); `p8.py extract` 60/150 (same set), `compare` **CLEAN**, keydiff=[137, 138, 139, 140, 150] (expected); `freeze.py baseline` **8/8**; `freeze.py diff` vs core-en TOTAL added CJK 9, all U+3000; added Latin strings 357 (D5 run-splitting); `spill_sweep.py` 0 SPILL (146 OBSERVE); `boxtitle_check.py` 0 DEFECT / 0 OBSERVE / 0 marginal (34 titles, 181 body lines); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` **PASS 0 defects** (ratios n=467 median 1.008, bold 1.050); `d5_census.py` **PASS** — D5 Latin 0, Cyrillic 0, curly in CJK 0, 164 curly in Newsreader, `Noto Sans` elements 0; print/web `pdftotext` byte-identical, 38,207 chars, unchanged vs pre-fix; text.md byte-identical (`a8330625…`, 53,944 B). P8: 192 → 192 lines, footer slack 47.8 → 37.8 px. **OVERALL: ALL-GREEN.** Pre-D5 baselines (disk-measured): print `2db4dad1…` (29,327,187 B), web `510a03ad…` (2,408,878 B); new SHAs in §2 (print `7efa7263…`, web `681f6184…`).

## 4. Translation decisions (Italian)
- Follows W46 it (TM): tu-form imperatives (Completa, Riscrivi, Abbina, Correggi); gloss format
  "term = translation", "·" separators, "Nota — " box prefix (bslib4 gloss() prepends it;
  gloss translations are bare — only the P1 bridge carries its own label, see §5).
- "runoff" = "ballottaggio"; "call a race" = "annunciare il risultato"
  (registry notes keep the TM "proclamare il risultato" — two different source literals, both correct);
  "to certify" = "certificare ufficialmente"; "midterm" = "le elezioni di medio termine";
  "seat" = "un seggio"; theme "Break the Silence" = "Rompi il silenzio".
- Numbers box keeps the English term with an Italian gloss in parentheses (W46 it precedent).
- P2 calendar lines in full-Italian short form (es precedent — avoids the fr P2 overflow):
  "10 nov. — i repubblicani scelgono il loro leader · 18–19 nov. — i democratici votano" /
  "20 nov. — Giornata mondiale dell'infanzia · 26 nov. — Thanksgiving · 27 nov. — Black Friday".
- SAY IT title = "Come si dice la data" (date, not clock time — the de D-de1 lesson).
- SAY IT box3 sub shortened in the rebuild (see §5 item 4): "Buon Giorno del Ringraziamento!"
  (309.8 px) → "Buon Ringraziamento!" (208.2 px) — fits the default 280 px panel with 35.9 px/side.
- P1 word-of-week bridge pre-shortened to 2 lines: "Elezioni di medio termine: tutta la Camera
  e un terzo del Senato." (fr/es lesson).
- TM types (used as-is): 完成句子→"Completare le frasi", 翻译→"Traduzione", 写作→"Scrittura",
  阅读理解→"Comprensione", 单选→"Scelta multipla", 完形填空→"Completa il testo",
  词汇配对→"Abbinamento", 句型转换→"Trasformazione", 对话补全→"Dialogo".
  TM instr: 填空→"Completa", 把词和释义配对→"Abbina", 改写→"Riscrivi", 配对→"Abbina".
- Fresh sets: instr 纠错→"Correggi"; types 从句→"Subordinate", 将来时→"Futuro",
  时态→"Tempi verbali", 比较填空→"Comparativi", 过去时→"Passato", 金句填空→"Frasi d'oro",
  纠错→"Correzione", 图表读数→"Lettura del grafico" (overrides the poisoned TM value "sans").
- ekeys: 137 "I democratici hanno vinto la Camera e il Senato.",
  138 "Lo spoglio continua.", 139 "Il nuovo Congresso si riunirà a gennaio 2027.",
  140 "Rompi il silenzio.", 150 "Compito aperto — punti chiave nel riquadro di scrittura;
  testo modello nel riquadro a pagina 8" (dash form, from the TM — no override needed).
- Box titles (single-line, measured at 23pt): "ERROR CLINIC　Errori", "READERS' CORNER　Lettere",
  "AN EXAMPLE LETTER　Esempio", "THE TOOLBOX　Strumenti", "NEXT WEEK　Anteprima VOL.5",
  "THE SENATE, IN NUMBERS　Il Senato", "HOW LONG?　Durata del mandato",
  "ODD SOCKS, IN NUMBERS　Cifre", "SATURDAY, NOV 21　Sabato",
  "HAYMITCH'S GAMES　I Giochi", "THE CALENDAR　Calendario" — all short forms, no collision
  (occlusion 0 flags).
- P8 section heads use TM short labels ("Scelta", "Completa", "Dialogo") that differ from the
  registry type names ("Scelta multipla", "Completare le frasi", "Dialogo") — same pattern as fr/es.

## 5. Fixes in this round (each → rebuild + re-render + full re-gate)
1. **P1 bridge size patch missed (apply.py WARN).** The W47 core's P1 bridge literal starts with
   "讲解｜" (same as gloss); my #189 translation used "Nota — " (the gloss prefix), but apply.py's
   bridge-size patch looks for `f.bridge("<gloss_word>...")` and it gloss_word is "Spiegazione | "
   (the W46 it P1-bridge label). No match → the bridge rendered at the default 20.5pt instead of
   19.5. Fixed #189 to the W46 it convention: "Spiegazione | a midterm = le elezioni di medio
   termine · to call a race = annunciare il risultato · a seat = un seggio." — patch then applied
   size=19.5. Lesson for nl/ru/ja/ko/zh-tw: check the W46 P1-bridge label per language; the
   bridge label need NOT equal the gloss prefix (de "Erklärung | " vs "Anmerkung | " is the same
   pattern; fr/es happened to match because their gloss_word equals their bridge label).
2. **text.md exporter SCRATCH path (same sed trap as es).** `make_textmd_w47.py` line 15 still
   pointed at `scratch-fanout-en/es` (trailing `/es"` has no slash, so `s|/es/|/it/|g` missed it)
   → "key mismatch" (it loaded the ES registry). Fixed the path, re-ran: RC=0, 150/150.
3. **P8 key size pre-set to 13.5/1.26** (not 15.5/1.3 from the W46 meta) on the es lesson: Spanish
   proved 15.5 overflows the answers block (87 lines); Italian notes are the same shape.
   P8-keys ends 2443/2560 — same as es.
4. **Rebuild + fix1 (11 Nov 2026, core-en fix1 sync — this round).** Core-en was fixed and
   re-proofed (Q39→a, Q40→d, Ashes rewritten as a 2025–26 retrospective, 已宣布 wording,
   SEARCHES/DID YOU KNOW box heights, SENATE/SATURDAY titles, SAY IT middle panel widened)
   and this edition was rebuilt from the fixed core via `scratch-fanout-en2/fanout/apply.py` +
   patched `map-it.json` (14 new literals: Q39/Q40 keys + notes, Q46/Q52/Q55/Q125 notes,
   SATURDAY/SENATE titles, P1 strip, Q7/Q82/Q83/Q84 notes, P6 bridge). Proof1 defects D1–D2
   were core-level and are resolved by the rebuild (verified per edition: registry keys
   39=a/40=d, notes `mentor = un mentore a` / `arena = l'arena d`; Q46 note dated Fri 21 Nov
   2025; Q52 `hosted`, Q55 `won`, Q125 `A (4–1)`; text.md answers 39→a, 40→d, 125→A;
   `Arsenal are winning!`; no `Perth is winning!` / `second week in Perth` / `Ashes begin`).
   **New defect found by this round (edition-level, in the D2 SAY IT fix itself):** widening
   SAY IT box3 to w=340 to fit "Buon Giorno del Ringraziamento!" (309.8 px) put the panel's
   right edge at x=1370 — exactly where the SAY IT glossary column starts (`lx = 1370` in
   content12.py), so the glossary words sat flush against the cream with 0 px gutter (caught
   on the P2 card crop; the SVG title sweep also flagged it as an apparent −106.6 px
   overflow, which is what exposed the crowding). Not a title overflow — a real layout
   collision. **Fix chosen: shorten the sub, not the panel** — map value
   `感恩节快乐！` → "Buon Ringraziamento!" (208.2 px, 35.9 px/side in the default 280 panel);
   the w=340 panel edit was reverted by the re-apply (apply.py re-copies content12.py from
   core). Rebuilt + re-gated: all green, svg boxtitle sweep 18/18, P2 card re-checked. The
   sweep itself was also hardened (`sweep_svg_titles.py`: a title must start within 60 px of
   its rect's left edge, so glossary words at the rect edge can no longer be mistaken for
   titles). The it arena note was the same error class as es (`lo stadio` was wrong) and was
   fixed to `l'arena d` in the map patch.
5. **Rebuild gates (11 Nov 2026, second build of this round; logs in
   `hidden_files/w47/scratch-fanout-en2/fanout/it/build-gates.log`)**: `run.py` exit 0, zero
   OVERFLOW / TOO WIDE, all flows within bottom, TOTAL 150, MODEL 82; `occlusion_audit.py`
   0 flags, selftest OK; `p8.py extract` noted set 60/150 (same set as core); `p8.py compare`
   CLEAN, keydiff=[137, 138, 139, 140, 150] (expected); registry vs P8 extract 149/150 exact
   + n=150 short-label exception; registry keys vs core 145/150 (diff only the 5
   reader-language keys 137–140, 150); `freeze.py baseline` 8/8 SVGs byte-identical
   (edition baseline `--build` = edition dir, re-run under the corrected invocation;
   core read-only对照 `--build` = core-en likewise 8/8 + direct sha 8/8);
   `freeze.py diff` TOTAL added CJK 9, all U+3000; print/web text layers 47,988 chars each,
   token-multiset diff 0/0, per-page byte-identical 8/8; `check_s11.py` ALL PASS; source
   boxtitle sweep 12/12 fit; SVG boxtitle sweep 18/18 fit; canonical `creambox.py` scan: all
   inside-only clearances positive; P8 min PDF font 10.12 pt ≥ 9.75 pt; SVG zero real CJK.
   (First build of this round passed everything except the svg boxtitle sweep, which caught
   the SAY IT box3 crowding above; the second build is the shipped one.)
6. **Q73 delta (11 Nov 2026, core-en fix2 sync — this round, only change).** Core-en fix2
   changed Q73 key "speak" → "up" (stem "Speak ___: tell a teacher." and note
   "speak up = parlare senza paura" unchanged). This edition synced the single key in
   `content56.py:49` only — no other source line touched. Registry diff exactly 1 entry
   (n=73 speak→up); text.md diff exactly 1 line (line 1151); Q73 four-source consistent
   for "up" (registry, text.md, P8 printed key, P5 stem + "to speak up" gloss). Only
   `svg/p8-test.svg` changed (its answers block); the other 7 SVGs are byte-identical to
   the shipped ones (p5 unchanged is correct and expected — the Q73 key only prints
   on P8; en-es delta confirmed the same). Rebuilt + re-gated: `run.py` exit 0, TOTAL 150, MODEL 82, 0 OVERFLOW;
   occlusion 0 flags; p8 extract 60/150 noted (same set as core), compare CLEAN,
   keydiff=[137, 138, 139, 140, 150]; keycheck 149/150 + n=150 exception (canonical and
   independent re-run agree); freeze baseline 8/8 + direct sha 8/8; freeze diff added CJK
   9, all U+3000; print/web text layers 47,988 chars each, token-multiset diff 0/0,
   per-page byte-identical 8/8; `check_s11.py` ALL PASS; source boxtitle sweep 12/12 fit;
   SVG boxtitle sweep 18/18 fit; canonical `creambox.py` log byte-identical to proof1's
   (32 boxes, min inside-only clearance +5.0px; P2 AND YOU? desc-clear −1.0px is the same
   known false alarm); `verify_ed.py` ALL PASS (23/23); P8 min PDF font 10.12 pt ≥ 9.75 pt;
   SVG zero real CJK; all 70 fill-in/rewrite keys re-checked against their stems (Q73
   "Speak up: tell a teacher." fits); 8 print pages + web P1/P8 visually checked, clean.
   Logs in `hidden_files/w47/scratch-delta-en-it/` (DELTA-NOTE.md, gates/, render/).
   New SHAs in §2 above (print `2db4dad1…`, web `570eef4f…`, text `a8330625…`).

## 6. Self-check (2026-11-11)
- Full read of `2026-w47-en-it.text.md` (all ~1,306 lines): zero issues.
  Notes kept: Q2/Q95 note "call a race = proclamare il risultato" (TM) vs P6 gloss
  "annunciare il risultato" — two source literals, both correct; Q136 "whether = se" vs Q105
  "whether = se (per quello che non si sa)" — two source literals, both correct; Q54
  "eight (otto = eight)" tautological like the core's note pattern; Q34 "(open = uscire
  (terza persona singolare con -s))" correct in context; Q110 "more than, la struttura" terse
  as in core; "Cinque frasi | who, where, cosa è successo, la svolta, la fine: cinque frasi
  bastano." is the W46 it TM value for the FIVE SENTENCES bridge (kept).
- All 8 cards visually checked after the final render — clean. P1: bridge 2 lines clear of
  IN BRIEF, numbers box English+gloss, "TRY IT NOW · Prova subito", footer "Pagina 1 di 8".
  P2: calendar short form, "THE SENATE, IN NUMBERS · Il Senato", SAY IT "Come si dice la data",
  gloss single "Nota — to certify = …". P3: "COMING SOON · Prossimamente",
  "HAYMITCH'S GAMES · I Giochi", gloss single "Nota — a tribute = …", Rousseau tiger.
  P4: "SATURDAY, NOV 21 · Sabato" (core fix1 title), gloss single "Nota — a Test: …", W. G. Grace photo; P4 lead is the Ashes 2025–26 retrospective "Perth, One Year On: How Australia Kept the Ashes".
  P5: "ODD SOCKS, IN NUMBERS · Cifre", gloss single "Nota — bullying = …",
  "SPEAK UP · Alza la voce", Lawrence children photo. P6: "HOW LONG? · Durata del mandato",
  gloss single "Nota — to call a race = …", "A PRACTICE BALLOT · Scheda", voting booth photo.
  P7: all gloss boxes single "Nota —", "THE TOOLBOX · Strumenti", "READERS' CORNER · Lettere",
  "AN EXAMPLE LETTER · Esempio", "ERROR CLINIC · Errori", "NEXT WEEK · Anteprima VOL.5",
  Johnson portrait. P8: cloze + [A2] option tags, "B MULTIPLE CHOICE · Scelta",
  "C READING · Comprensione", "D SENTENCES · Completa", "E TRANSLATION · Traduzione" with
  "Traduci:", "F WORDS · Abbina", "G DIALOGUE · Dialogo" + "Levels: 145–149 [A2]",
  "H WRITING · Scrittura [B1]" + Italian instruction, MODEL + Reading Room photo,
  ANSWERS block all 150 keys ending well above the footer with "150. Compito aperto — punti
  chiave nel riquadro di scrittura; testo modello nel riquadro a pagina 8
  (Valutazione per punti chiave)"; footer "Pagina 8 di 8".

## 7. Furniture
- foot_left "The Lucerna　SETTIMANALE INGLESE VOL.4　TESTI IN INGLESE　SPIEGAZIONI IN ITALIANO";
  foot_right "Pagina {n} di {total}"; gloss_prefix "Nota — "; p8_sep "— Pagina {pg} —";
  translate prefix "Traduci: "; badge "TESTI IN INGLESE　SPIEGAZIONI IN ITALIANO — L'EDIZIONE
  PER I LETTORI ITALIANI"; topstrip "WEEKLY IN ENGLISH　Ogni settimana　Di che cosa parla il
  mondo anglofono"; edition line "SETTIMANALE IN INGLESE　VOL.4　ELEZIONI　GIUNGLA　FILM";
  edition spacing 4.6; p1_bridge_size 19.5; p8_mode "notes".

## 8. Provenance
- TM: W46 `2026-w46-en-it` positional alignment (260 pairs). Poisoned values caught:
  'note' → 'P8 saved, TOTAL exercises:' (harmless, rejected by build_map's POISON regex);
  '图表读数' → 'sans' (overridden by fresh type "Lettura del grafico").
  'THE ERROR CLINIC　易错诊所' → 'Errori' is a legitimate translation, not poison.
- Map: `scratch-fanout-en2/fanout/map-it.json` (lit 248, instr 5, type 17, ekey 4).
  Misses: 205 total, 182 with real CJK = 171 lit + 7 types + 4 ekeys.
  build_map normalizes U+2019 → ASCII apostrophe in all map values (fr lesson).
- F-MAIL: no real letters arrived; P7 prints the labelled editor's example + the VOL.3
  disclosure promising real letters from VOL.5. No invented letters, no email checked.

## 9. Build record
- `scratch-fanout-en2/fanout/it/` — build-gates.log, make_textmd_w47.py, occlusion.log/json,
  p8-extract/compare.json, freeze.log/diff.json, webpdf.log, textmd.log, registry.json, dump_reg.log,
  freeze-final/, 00-it-complete.md.

## 10. Tool note (NOT fixed — p8.py is off-limits to the builder)
- `tools/p8.py` FOOTER_RE does not match the mixed-case footer "The Lucerna …" + "Pagina 8 di 8":
  the merged footer line leaks into the last answer segment (key 150) for every edition.
  Masked when key 150 is dash-style (it, fr, de), bites when paren-style without a dash (es,
  before its fix). A case-insensitive match on the masthead, or dropping the merged footer line
  by its y=2624 baseline, would close it.
