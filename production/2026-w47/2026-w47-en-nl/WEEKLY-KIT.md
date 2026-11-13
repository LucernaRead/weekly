# WEEKLY-KIT — 2026-W47 en-nl (English target, Dutch reader)

## 1. Identity
- Slug: `2026-w47-en-nl`
- Target language: English (en). Reader language: Dutch (nl).
- Issue week: Monday 16 – Sunday 22 November 2026. VOL.4.
- Core: `production/2026-w47/core-en/` (en-zh-cn), copied whole, explanation layer rewritten in Dutch.
- Exercises: 150 (registry 150; per page 10/17/18/18/18/18/12/39; A2 62 / B1 66 / B2 22).
- MODEL words: 82.

## 2. Files delivered
- 8 SVG (`svg/p1-front.svg` … `svg/p8-test.svg`) + 8 card PNGs (`cards/`).
- Print PDF: `The-Lucerna-VOL4-en-nl.pdf` — 28,842,162 bytes,
  SHA-256 `eb6be63a66868ef1cbcfafe9a85b462ff58f8fc574b66be2267a77fd3b0e1db5`.
  [D5 rebuild, 12 Nov 2026 — see §3; pre-D5 values were print `21e13a74…` 29,341,219 B,
  web `c769e979…` 2,411,506 B.]
  [F1 fix, 12 Nov 2026 — see F1 bullet below; pre-fix values were print `ac22842f…` 28,841,767 B,
  web `ec2c820e…` 2,330,974 B.]
- Web PDF: `The-Lucerna-VOL4-en-nl.web.pdf` — 2,331,372 bytes,
  SHA-256 `32e8baa51bf9260999812e6155113630717b2a4512430aef49d8465b758dc9c5`
  (built only with `tools/webpdf.py`; text layer 38,320 chars, identical to the print extraction — token-multiset diff 0/0; per-page byte-identical 8/8).
- `2026-w47-en-nl.text.md` — 53,736 bytes, SHA-256 `cbd9a008c530e127d6a446910443047e1df60092ed9e54ba0479b7a480696fe4`, exported from the build source (never from the PDF);
  stub registry 150 = real registry 150. Re-exported in the F1 fix (12 Nov 2026, see F1 bullet below; pre-fix 53,565 B `30bfb6f9…`).
- **F1 fix (12 Nov 2026, proof-round defect F1 — Georgia runoff written as pending; work log in `hidden_files/w47/scratch-fix-en/FIX-LOG.md`, gates in `hidden_files/w47/scratch-fix-en/logs/2026-w47-en-nl/`):** P2 :185 + P6 :651 rewritten as settled law + result (Georgia law calls for a Dec 1 runoff only if no one wins a majority — AP called Jon Ossoff reelected 3 Nov, ~59%, so no runoff). Q13/Q142 untouched (rule questions, answers still 1 December). Source `content12.py:171` + `content56.py:103`; text.md re-exported with `scratch-fix-en/make_textmd_fix.py` (diff exactly the 2 lines, no title lost — all 7 D5-shrunk box titles present). First fix attempt (worker 118ea848) was cut by a runtime restart mid-webpdf (print PDF + text.md already rebuilt, web PDF still the pre-fix file); takeover worker re-ran the full `fix_build.sh` to completion. Gates ALL-GREEN: run rc=0 TOTAL 150 MODEL 82, 0 overflow; head_check PASS; occlusion 0 flags (selftest OK); p8 extract 60/150, compare CLEAN, keydiff=[137, 138, 139, 140, 150] (expected); freeze baseline 8/8; spill 0; boxtitle 0; edge 0; creambox PASS; census PASS; print/web text layers byte-identical. New deliverables: print 28,842,162 B SHA-256 `eb6be63a6686…` (was 28,841,767 B `ac22842f…`; re-run reproduced the interrupted run's print SHA exactly), web 2,331,372 B `32e8baa5…` (was 2,330,974 B `ec2c820e…`), text 53,736 B `cbd9a008…` (was 53,565 B `30bfb6f9…`); text layer 38,320 chars (was 38,188).
- `ABSTRACT.txt` — one line, Dutch, no ASCII double quotes.
- `registry.json` — fresh dump (150 keys), copied over the stale core copy from apply.py.

## 3. Gates (all green, re-run fresh 2026-11-11 after the P2 fix)
- run.py exit 0; 0 FLOW OVERFLOW / HEAD TOO WIDE; every Flow end y ≤ its bottom
  (P8-keys 2375/2560; P2-feature 1438/1540; P2-ex 2532/2560).
- occlusion audit: 0 flags (selftest OK).
- p8 extract: 60/150 noted (same set as core); compare CLEAN; keydiff [137, 138, 139, 140, 150]
  (reader-language translation keys + writing key — expected).
- freeze baseline tool: 8/8 byte-identical; direct sha256 re-render vs shipped core SVGs: 8/8 MATCH.
  Freeze diff: added CJK = only 9× U+3000 separators; removed = core Chinese layer.
- print/web text token-multiset diff: 0/0 (48,044 chars each; token-multiset diff 0/0;
  per-page byte-identical 8/8).
- `check_s11.py nl`: ALL §1.1/P8 CHECKS PASS (colour set core 19 = edition 19;
  badge colours A2 #5c6e30 / B1 #46581f / B2 #37402f; P8 min font 13.5 pt ≥ 9.75;
  chip-rect counts = core per page; Q113–120 options line with [A2] tag present;
  "Levels: 145–149 [A2]" present; Q120 [A2] chip OK;
  P8 WRITING head "H　WRITING　Schrijven [B1]" present).
- **Boxtitle gate fix (12 Nov 2026, all on the rebuilt edition; logs in `hidden_files/w47/scratch-gatefix-de-en/2026-w47-en-nl/`)**: new standing gate `tools/boxtitle_check.py` (130-wide run) found the P1 SEARCHES footnote `Relatieve populariteit, geen exacte zoekcijfers.` running past its cream box by **+7.5px** (core-en fits at −22.0px). Fix (edition-local, `content12.py:85` only): footnote font size 19 → 18 (layout only, no text changed); ink end 1869.5 → **1848.5**, margin **+13.5px**. New deliverables: print 29,341,266 B (−1 B) sha `626e4c1bbf2c77cb579ac9f6e7511ce7036d6af1bebdb5b7700a729615dc7fee`; web 2,411,532 B (−14 B) sha `dd4cee4884e6f3d3af68788b469ac33d4b452c75d4bad91fd68e01dc8e70cf38`; text.md 53,565 B sha 30bfb6f9… (unchanged). Gates: `run.py` exit 0, zero OVERFLOW / TOO WIDE, TOTAL 150, MODEL 82; boxtitle **0 DEFECT / 0 OBSERVE / 0 marginal** (also 0 on the synced production files); `occlusion_audit.py` 0 flags, selftest OK; `p8.py extract` noted set 60/150 (same set as core), `compare` CLEAN keydiff=[137, 138, 139, 140, 150] (expected); `freeze.py diff` vs core-en exit 0, TOTAL added CJK 9, all U+3000; frozen-intersection check (core vs pre-fix vs rebuilt SVGs) **PASS 8/8 identical**; determinism re-run (`run.py` again in the build copy) SVGs byte-identical; print/web text layers identical content. NOTE: this edition has no `verify.py` (de-family script); TOTAL/MODEL come from `run.py`, determinism from the re-run.
- **D5 rebuild + gates (12 Nov 2026; full log `hidden_files/w47/scratch-d5-rebuild-en/logs/2026-w47-en-nl/GATES-SUMMARY.txt`)**: SOP §1.1 font fix — installed via `scratch-d5-plan/mechanism/apply_variant.py --target en --reader nl` (D5 block in this edition's `svglib.py`, `_D5_READER = "latin"`; this edition's svglib already carried fix2, so the installer reported "fix2 already present"; routing unit-checked: `check_routing.py` FAILURES: 0; U+201C fix2 routing preserved — census: curly in CJK 0, all 168 curly quotes in Newsreader). Pre-fix census: 545 Latin-in-CJK-sans elements. Post-fix defects, all D5-caused: (1) P7-col3 head `AN EXAMPLE LETTER　Voorbeeld` HEAD TOO WIDE +27.1 px advance at 25 → head size 25 → 23 (`content7.py:104`); (2) P8-battery head `B　MULTIPLE CHOICE　Meerkeuze` HEAD TOO WIDE +18.6 px advance at 24 → head size 24 → 22 (`content8.py:44`); (3) P5 cream-box title `ODD SOCKS, IN NUMBERS　Cijfers` +12.3 px right → `tsize` 23 → 21 (`content56.py:22`). Layout only, text unchanged. Gates: run rc=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; `head_check.py` PASS 0 defects; `render.py` + `webpdf.py` rc=0; `occlusion_audit.py` 0 flags (selftest OK); `p8.py extract` 60/150 (same set), `compare` **CLEAN**, keydiff=[137, 138, 139, 140, 150] (expected); `freeze.py baseline` **8/8**; `freeze.py diff` vs core-en TOTAL added CJK 9, all U+3000; added Latin strings 361 (D5 run-splitting); `spill_sweep.py` 0 SPILL (149 OBSERVE); `boxtitle_check.py` 0 DEFECT / 0 OBSERVE / 0 marginal (32 titles, 183 body lines); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` **PASS 0 defects** (ratios n=468 median 1.009, bold 1.049); `d5_census.py` **PASS** — D5 Latin 0, Cyrillic 0, curly in CJK 0, 168 curly in Newsreader, `Noto Sans` elements 0; print/web `pdftotext` byte-identical, 38,188 chars, unchanged vs pre-fix; text.md byte-identical (`30bfb6f9…`, 53,565 B). P8: 199 → 178 lines, footer slack 35.9 → 35.9 px. **OVERALL: ALL-GREEN.** Pre-D5 baselines (disk-measured): print `21e13a74…` (29,341,219 B), web `c769e979…` (2,411,506 B); new SHAs in §2 (print `ac22842f…`, web `ec2c820e…`).

## 4. Translation decisions (Dutch)
- Follows W46 nl (TM): imperatives (Vul in, Herschrijf, Combineer, Corrigeer); gloss format
  "term = translation", "·" separators, "Uitleg — " box prefix (bslib4 gloss() prepends it;
  gloss translations are bare — only the P1 bridge carries its own label, "Uitleg — ",
  which the bridge-size patch matches via gloss_word).
- "runoff" = "de tweede ronde"; "call a race" = "de uitslag bekendmaken"
  (TM: "to call a race = de uitslag bekendmaken · to certify = bekrachtigen · a runoff =
  de tweede ronde"); "to certify" = "bekrachtigen"; "midterm" = "de tussentijdse verkiezingen";
  "seat" = "een zetel"; theme "Break the Silence" = "Doorbreek de stilte".
- Numbers box keeps the English term with a Dutch gloss in parentheses (W46 nl precedent).
- P2 calendar lines in full-Dutch short form (es precedent — avoids the fr P2 overflow):
  "10 nov. — de Republikeinen kiezen hun leider · 18–19 nov. — de Democraten stemmen" /
  "20 nov. — Wereldkinderdag · 26 nov. — Thanksgiving · 27 nov. — Black Friday".
- SAY IT title = "Zo zeg je de datum" (date, not clock time — the de D-de1 lesson).
- P1 word-of-week bridge pre-shortened to 2 lines: "Tussentijdse verkiezingen: het hele Huis
  en een derde van de Senaat." (fr/es lesson).
- TM types (used as-is): 完成句子→"Zinnen aanvullen", 翻译→"Vertalen", 写作→"Schrijven",
  阅读理解→"Begrijpend lezen", 单选→"Meerkeuze", 完形填空→"Gatentekst",
  词汇配对→"Woorden combineren", 句型转换→"Zinnen omvormen", 对话补全→"Dialoog aanvullen".
  TM instr: 填空→"Vul in", 把词和释义配对→"Combineer", 改写→"Herschrijf", 配对→"Combineer".
- Fresh sets: instr 纠错→"Corrigeer"; types 从句→"Bijzinnen", 将来时→"Toekomst",
  时态→"Werkwoordstijden", 比较填空→"Vergelijkingen", 过去时→"Verleden tijd",
  金句填空→"Gouden zinnen", 纠错→"Correctie", 图表读数→"Grafieken lezen"
  (overrides the poisoned TM value "P8 saved, TOTAL exercises:").
- ekeys: 137 "De Democraten wonnen het Huis en de Senaat.",
  138 "De telling gaat door.", 139 "Het nieuwe Congres vergadert in januari 2027.",
  140 "Doorbreek de stilte.", 150 "Open vraag — punten in het schrijfblok; voorbeeldtekst
  in het kader op pagina 8" (dash form, from the TM — no override needed).
- Box titles (single-line): "ERROR CLINIC　Fouten", "READERS' CORNER　Brieven",
  "AN EXAMPLE LETTER　Voorbeeld", "THE TOOLBOX　Gereedschap", "NEXT WEEK　Vooruitblik VOL.5",
  "HOW LONG?　Duur van de termijn", "ODD SOCKS, IN NUMBERS　Cijfers",
  "SATURDAY, NOV 21　Zaterdag" (core fix1 title), "HAYMITCH'S GAMES　De Spelen",
  "THE CALENDAR　Kalender" — all short forms. The SENATE title is now
  "SENATE IN NUMBERS　Senaat" (core fix1 dropped "THE"; the old "THE SENATE, IN NUMBERS　De
  Senaat" fix in §5 is superseded).
- P8 section heads use TM short labels ("Meerkeuze", "Leestekst", "Zinnen vormen",
  "Dialoog aanvullen") that differ from the registry type names ("Meerkeuze" = same;
  "Begrijpend lezen", "Zinnen aanvullen", "Dialoog aanvullen") — same pattern as fr/es/it/pt.

## 5. Fix in this round (→ rebuild + re-render + full re-gate)
- **P2 SENATE box title ran into the next column — a defect the occlusion audit MISSED.**
  "THE SENATE, IN NUMBERS　De Senaat" (text_w 413.0pt vs 386.5 inner box width) overflowed its
  box to the right; pixel-measured on the final card, the last ink of "Senaat" ended 6pt before
  the first ink of the column-3 line "Second story of the week" — no ink overlap, but less than
  a word space, reading as one run ("De SenaatSecond story"). The audit's LINEX/EDGE checks do
  not cover title-to-neighbouring-column text. Fix: shortened to "THE SENATE, IN NUMBERS　Senaat"
  (drop "De ") — re-measured gap 39pt. Still used as-is in es? Note: es's SENATE title
  (411.4pt) has the same ~6pt tightness on its card; it was judged "tight but no collision" and
  left alone — the nl fix follows the fr-round proactive rule ("shorten when clearly sticking
  out of the box"). Lesson for ru/ja/ko/zh-tw: **do not trust text_w alone for box titles**
  (it under-measures U+3000-containing titles by ~15pt — true ink width 428.5 vs text_w 413.0);
  pixel-check any title that faces live text in the next column, and shorten pre-emptively.
- P8 key size 13.5/1.26 is already the W46 nl value (no es-style change needed).
- **Rebuild + fix1 (11 Nov 2026, core-en fix1 sync — this round).** Core-en was fixed and
  re-proofed (Q39→a, Q40→d, Ashes rewritten as a 2025–26 retrospective, 已宣布 wording,
  SEARCHES/DID YOU KNOW box heights, SENATE/SATURDAY titles, SAY IT middle panel widened)
  and this edition was rebuilt from the fixed core via `scratch-fanout-en2/fanout/apply.py` +
  patched `map-nl.json` (14 new literals: Q39/Q40 keys + notes, Q46/Q52/Q55/Q125 notes,
  SATURDAY/SENATE titles, P1 strip, Q7/Q82/Q83/Q84 notes, P6 bridge). Proof1 defects D1–D3
  were core-level and are resolved by the rebuild (verified per edition: registry keys
  39=a/40=d, notes `mentor = een mentor a` / `arena = de arena d`; Q46 note dated Fri 21 Nov
  2025; Q52 `hosted`, Q55 `won`, Q125 `A (4–1)`; text.md answers 39→a, 40→d, 125→A;
  `Arsenal are winning!`; no `Perth is winning!` / `second week in Perth` / `Ashes begin`).
  **D4 (edition-level) fixed in the map**: the 4 French guillemets « » in Dutch text →
  Dutch "…" quotes — H instruction (text.md line 993), Q65, Q88, Q126 notes. Verified 0 « in
  the rebuilt content*.py, registry.json, text.md and all 8 SVGs; the 4 spots now read e.g.
  Q65 `Het thema dit jaar is "Doorbreek de stilte"`, Q126 `Thema van de Week tegen Pesten:
  "Doorbreek de stilte"`. The old ABSTRACT was short-form (§9-class, like ja D4) and was
  rewritten to the full form (announced results; certification 10 Nov–18 Dec; 16 Nov
  Anti-Bullying/Odd Socks; 20 Nov Children's Day + Hunger Games; 21 Nov Premier League back +
  Turin ATP final + Ashes 4–1 look-back; reader language; A2–B2; 150).
- **Rebuild gates (11 Nov 2026; logs in `hidden_files/w47/scratch-fanout-en2/fanout/nl/build-gates.log`)**:
  `run.py` exit 0, zero OVERFLOW / TOO WIDE, all flows within bottom, TOTAL 150, MODEL 82;
  `occlusion_audit.py` 0 flags, selftest OK; `p8.py extract` noted set 60/150 (same set as
  core); `p8.py compare` CLEAN, keydiff=[137, 138, 139, 140, 150] (expected); registry vs P8
  extract 149/150 exact + n=150 short-label exception; registry keys vs core 145/150 (diff
  only the 5 reader-language keys 137–140, 150); `freeze.py baseline` 8/8 SVGs byte-identical;
  `freeze.py diff` TOTAL added CJK 9, all U+3000; print/web text layers 48,044 chars each,
  token-multiset diff 0/0, per-page byte-identical 8/8; `check_s11.py` ALL PASS; source
  boxtitle sweep 12/12 fit; SVG boxtitle sweep 18/18 fit; canonical `creambox.py` scan: all
  inside-only clearances positive; P8 min PDF font 10.12 pt ≥ 9.75 pt; SVG zero real CJK.
- **Delta Q73 speak→up (11 Nov 2026, core-en fix2 sync — this change, only change).**
  Core-en fix2 changed Q73 key `"speak"` → `"up"` (stem "Speak ___: tell a teacher.",
  note `speak up = …` unchanged). This edition synced the same one-key change in
  `content56.py:49` only — no other source line touched. Rebuilt with the edition's own
  run.py / render.py / webpdf.py; registry diff exactly 1 entry (n=73 speak→up),
  text.md diff exactly 1 line (line 1151); Q73 four-source consistent as `up`
  (registry, text.md, P8 printed key, P5 stem + "to speak up" note). SVG change confined
  to p8-test.svg only (p1–p7 byte-identical; P8 answer reflow "73. up" only, 0.14% pixels);
  all gates re-run fresh and green (see §9 delta log). Previous build SHAs (proof1):
  print `a5957d64…` 29,341,272 B; web `ee3d98ba…` 2,411,538 B;
  text `baecaf6e…` 53,568 B.
- **U+201C fix2 port (12 Nov 2026, core-de fix2 port — this change, only change).**
  Core-de's fix2 (proof2 D1/D2) routes U+201C through the serif branch
  (Newsreader) because in Noto Sans CJK SC/TC its advance is 1000/1000em
  (full width); the fan-out copies never got the patch. Ported into this
  edition's `svglib.py` only — `_char_font` + the `_QUOTE_CLS`/`_PATH` rows,
  extended to all three codepoints (`U+201C`, `U+201D`, `U+2019`, all three
  1000/1000em in SC/TC); no other source line touched. SVG census before:
  4 defective glyphs, all P8 (D1 instruction 20pt “…” + D2 key note 13.5pt
  “…” in `Noto Sans CJK SC`); after: 0 defective, all quotes Newsreader.
  SVG change confined to p8-test.svg only (p1–p7 byte-identical). Rebuilt
  with the edition's own run.py / render.py / webpdf.py; all gates re-run
  fresh and green (see §9 fix2-port log). Previous build SHAs (boxtitle
  fix): print `626e4c1b…` 29,341,266 B; web `dd4cee48…` 2,411,532 B;
  text `30bfb6f9…` 53,565 B (unchanged).

## 6. Self-check (2026-11-11)
- Full read of `2026-w47-en-nl.text.md` (all ~1,306 lines): zero issues.
  Notes kept: "Herschrijf in de tegenwoordige tijd (wat er nu gebeurt)." is the W46 nl TM value
  for the present-continuous bridge (kept); "Vijf zinnen | who, where, wat er gebeurde,
  de wending, het einde — vijf zinnen zijn genoeg." is the W46 nl TM value for the FIVE SENTENCES
  bridge (kept); "Voetbalengels | Stand, wie scoorde, wie leidt — korte zinnen zijn live Engels."
  and "Eén kaart | Vijftig staten, vijftig regels — …" are W46 nl TM values (kept); Q34
  "(open = in première gaan (3e persoon enkelvoud + s))" correct; Q54 "eight (acht = eight)"
  tautological like the core's note pattern; Q97 "take time = tijd kosten" correct Dutch; Q98
  "differ → differs in de 3e persoon enkelvoud" is the TM value; Q110 "more than, de structuur"
  terse as in core; Q136 "whether = of" vs Q105 "whether = of (voor wat je niet weet)" — two
  source literals, both correct; "READ THE CHART · Grafiek" is the TM head (short, the bridge
  carries the instruction).
- All 8 cards visually checked after the final render — clean. P1: bridge 2 lines clear of
  IN BRIEF, numbers box English+gloss, "TRY IT NOW · Oefen nu", footer "Pagina 1 van 8".
  P2 (fixed): "THE SENATE, IN NUMBERS · Senaat" now fits its box with a clear gap to
  "Second story", calendar short form, SAY IT "Zo zeg je de datum",
  gloss single "Uitleg — to certify = …". P3: "COMING SOON · Binnenkort",
  "HAYMITCH'S GAMES · De Spelen", gloss single "Uitleg — a tribute = …", Rousseau tiger.
  P4: "SATURDAY, NOV 21 · Zaterdag" (core fix1 title), gloss single "Uitleg — a Test: …", W. G. Grace photo; P4 lead is the Ashes 2025–26 retrospective "Perth, One Year On: How Australia Kept the Ashes".
  P5: "ODD SOCKS, IN NUMBERS · Cijfers", gloss single "Uitleg — bullying = …",
  "SPEAK UP · Spreek je uit", Lawrence children photo. P6: "HOW LONG? · Duur van de termijn",
  gloss single "Uitleg — to call a race = …", "A PRACTICE BALLOT · Stembiljet", voting booth
  photo. P7: all gloss boxes single "Uitleg —", "THE TOOLBOX · Gereedschap",
  "READERS' CORNER · Brieven", "AN EXAMPLE LETTER · Voorbeeld", "ERROR CLINIC · Fouten",
  "NEXT WEEK · Vooruitblik VOL.5", Johnson portrait. P8: cloze + [A2] option tags,
  "B MULTIPLE CHOICE · Meerkeuze", "C READING · Leestekst", "D SENTENCES · Zinnen vormen",
  "E TRANSLATION · Vertalen" with "Vertaal:", "F WORDS · Woorden combineren",
  "G DIALOGUE · Dialoog aanvullen" + "Levels: 145–149 [A2]", "H WRITING · Schrijven [B1]" +
  Dutch instruction, MODEL + Reading Room photo, ANSWERS block all 150 keys ending well above
  the footer with "150. Open vraag — punten in het schrijfblok; voorbeeldtekst in het kader op
  pagina 8 (Beoordeel op punten)"; footer "Pagina 8 van 8".

## 7. Furniture
- foot_left "The Lucerna　ENGELS WEEKBLAD VOL.4　TEKSTEN IN HET ENGELS　UITLEG IN HET NEDERLANDS";
  foot_right "Pagina {n} van {total}"; gloss_prefix "Uitleg — "; p8_sep "— Pagina {pg} —";
  translate prefix "Vertaal: "; badge "TEKSTEN IN HET ENGELS　UITLEG IN HET NEDERLANDS — DE
  EDITIE VOOR NEDERLANDSTALIGE LEZERS"; topstrip "WEEKLY IN ENGLISH　Elke week　Waar de
  Engelstalige wereld over praat"; edition line "ENGELS WEEKBLAD　VOL.4　VERKIEZINGEN　JUNGLE
  FILMS"; edition spacing 11.5; p1_bridge_size 19.5; p8_mode "notes".

## 8. Provenance
- TM: W46 `2026-w46-en-nl` positional alignment (260 pairs). Poisoned values caught:
  '图表读数' → 'P8 saved, TOTAL exercises:' (rejected by build_map's POISON regex; overridden by
  fresh type "Grafieken lezen"); '改错' → 'sans' (not a needed key — harmless).
  'THE ERROR CLINIC　易错诊所' → 'THE ERROR CLINIC　Fouten' is a legitimate translation, not poison.
- Map: `scratch-fanout-en2/fanout/map-nl.json` (lit 247, instr 5, type 17, ekey 4 — one fewer lit than
  the Romance editions because one miss is covered by the nl TM directly).
  Misses: 205 total, 182 with real CJK = 171 lit + 7 types + 4 ekeys.
  build_map normalizes U+2019 → ASCII apostrophe in all map values (fr lesson).
- F-MAIL: no real letters arrived; P7 prints the labelled editor's example + the VOL.3
  disclosure promising real letters from VOL.5. No invented letters, no email checked.

## 9. Build record
- `scratch-fanout-en2/fanout/nl/` — build-gates.log, make_textmd_w47.py, occlusion.log/json,
  p8-extract/compare.json, freeze.log/diff.json, webpdf.log, textmd.log, registry.json, dump_reg.log,
  freeze-final/.
- Delta Q73 (11 Nov 2026): `hidden_files/w47/scratch-delta-en-nl/` — DELTA-NOTE.md,
  delta-build/delta-gates stdout logs, gates/ (occlusion, p8-extract/compare, freeze,
  printweb, keycheck, check_s11, boxtitle, creambox), render/ (8 fresh 100-DPI renders +
  old-vs-new pixel diff), fillin-rewrite-check.txt (50/50 key-fit review).
- Boxtitle gate fix (12 Nov 2026): `hidden_files/w47/scratch-gatefix-de-en/2026-w47-en-nl/` — FIX-LOG.md (full per-edition record), run-build.log, webpdf.log, boxtitle.log, p8-extract/compare.json, occlusion.log, freeze.log/diff.json, frozen-check.log, determinism.log.
- Fix2 port (12 Nov 2026): `hidden_files/w47/scratch-gatefix-u201c-en/2026-w47-en-nl/` — FIX-LOG.md (full per-edition record), run-build.log, webpdf.log, freeze-baseline.log, freeze-diff.json/log, p8-extract/compare.json/log, occlusion.log, spill.log, boxtitle.log (+ boxtitle-prod), textmd.log, determinism.log, census BEFORE/AFTER.

## 10. Tool note (NOT fixed — p8.py is off-limits to the builder)
- `tools/p8.py` FOOTER_RE does not match the mixed-case footer "The Lucerna …" + "Pagina 8 van 8":
  the merged footer line leaks into the last answer segment (key 150) for every edition.
  Masked when key 150 is dash-style (nl, pt, it, fr, de), bites when paren-style without a dash
  (es, before its fix). A case-insensitive match on the masthead, or dropping the merged footer
  line by its y=2624 baseline, would close it.
- Occlusion audit gap (found this round): the audit does not flag a box title running into live
  text in the neighbouring column (see §5). A title-vs-neighbour text proximity check would close it.
