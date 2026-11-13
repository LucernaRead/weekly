# WEEKLY-KIT — 2026-W47 en-pt (English target, Portuguese reader)

## 1. Identity
- Slug: `2026-w47-en-pt`
- Target language: English (en). Reader language: Portuguese (pt).
- Issue week: Monday 16 – Sunday 22 November 2026. VOL.4.
- Core: `production/2026-w47/core-en/` (en-zh-cn), copied whole, explanation layer rewritten in Portuguese.
- Exercises: 150 (registry 150; per page 10/17/18/18/18/18/12/39; A2 62 / B1 66 / B2 22).
- MODEL words: 82.

## 2. Files delivered
- 8 SVG (`svg/p1-front.svg` … `svg/p8-test.svg`) + 8 card PNGs (`cards/`).
- Print PDF: `The-Lucerna-VOL4-en-pt.pdf` — 28,850,391 bytes,
  SHA-256 `eb347a545c8ec0239433ba3d7f7cf6d4c643f4aca05639f471fb2726bb6cba10`.
  [D5 rebuild, 12 Nov 2026 — see §3; pre-D5 values were print `52452731…` 29,345,708 B,
  web `b787bd7d…` 2,418,221 B.]
  [F1 fix, 12 Nov 2026 — see F1 bullet below; pre-fix values were print `4ecc163c…` 28,850,005 B,
  web `dbc0fefb…` 2,339,191 B.]
- Web PDF: `The-Lucerna-VOL4-en-pt.web.pdf` — 2,339,582 bytes,
  SHA-256 `adc0a7e864dbd52c44273229b5cf804ac0e8282446b120a728aaeb01353bcdb6`
  (built only with `tools/webpdf.py`; text layer 38,227 chars, identical to the print extraction — token-multiset diff 0/0; per-page byte-identical 8/8).
- `2026-w47-en-pt.text.md` — 54,291 bytes, SHA-256 `1b3ee4558a758ae55e2faf84daee3ad9a12bd912ff0cce5dfcef5db2e6da05c0`, exported from the build source (never from the PDF);
  stub registry 150 = real registry 150. Re-exported in the F1 fix (12 Nov 2026, see F1 bullet below; pre-fix 54,120 B `f85c55ce…`).
- **F1 fix (12 Nov 2026, proof-round defect F1 — Georgia runoff written as pending; work log in `hidden_files/w47/scratch-fix-en/FIX-LOG.md`, gates in `hidden_files/w47/scratch-fix-en/logs/2026-w47-en-pt/`):** P2 :185 + P6 :651 rewritten as settled law + result (Georgia law calls for a Dec 1 runoff only if no one wins a majority — AP called Jon Ossoff reelected 3 Nov, ~59%, so no runoff). Q13/Q142 untouched (rule questions, answers still 1 December). Source `content12.py:171` + `content56.py:103`; text.md re-exported with `scratch-fix-en/make_textmd_fix.py` (diff exactly the 2 lines, no title lost — all 7 D5-shrunk box titles present). Full rebuild + gates ALL-GREEN: run rc=0 TOTAL 150 MODEL 82, 0 overflow; head_check PASS; occlusion 0 flags (selftest OK); p8 extract 60/150, compare CLEAN, keydiff=[137, 138, 139, 140, 150] (expected); freeze baseline 8/8; spill 0; boxtitle 0; edge 0; creambox PASS; census PASS; print/web text layers byte-identical. New deliverables: print 28,850,391 B SHA-256 `eb347a545c8e…` (was 28,850,005 B `4ecc163c…`), web 2,339,582 B `adc0a7e8…` (was 2,339,191 B `dbc0fefb…`), text 54,291 B `1b3ee455…` (was 54,120 B `f85c55ce…`); text layer 38,227 chars (was 38,095).
- `ABSTRACT.txt` — one line, Portuguese, no ASCII double quotes.
- `registry.json` — fresh dump (150 keys), copied over the stale core copy from apply.py.

## 3. Gates (all green, re-run fresh 2026-11-11)
- run.py exit 0; 0 FLOW OVERFLOW / HEAD TOO WIDE; every Flow end y ≤ its bottom
  (P8-keys 2443/2560; P2-feature 1497/1540; P2-ex 2532/2560).
- occlusion audit: 0 flags (selftest OK).
- p8 extract: 60/150 noted (same set as core); compare CLEAN; keydiff [137, 138, 139, 140, 150]
  (reader-language translation keys + writing key — expected).
- freeze baseline tool: 8/8 byte-identical; direct sha256 re-render vs shipped core SVGs: 8/8 MATCH.
  Freeze diff: added CJK = only 9× U+3000 separators; removed = core Chinese layer.
- print/web text token-multiset diff: 0/0 (47,926 chars each; token-multiset diff 0/0; per-page byte-identical 8/8).
- `check_s11.py pt`: ALL §1.1/P8 CHECKS PASS (colour set core 19 = edition 19;
  badge colours A2 #5c6e30 / B1 #46581f / B2 #37402f; P8 min font 13.5 pt ≥ 9.75;
  chip-rect counts = core per page; Q113–120 options line with [A2] tag present;
  "Levels: 145–149 [A2]" present; Q120 [A2] chip OK;
  P8 WRITING head "H　WRITING　Escrita [B1]" present).
- **D5 rebuild + gates (12 Nov 2026; full log `hidden_files/w47/scratch-d5-rebuild-en/logs/2026-w47-en-pt/GATES-SUMMARY.txt`)**: SOP §1.1 font fix — installed via `scratch-d5-plan/mechanism/apply_variant.py --target en --reader pt` (D5 block in this edition's `svglib.py`, `_D5_READER = "latin"`; routing unit-checked: `check_routing.py` FAILURES: 0; U+201C fix2 routing preserved — census: curly in CJK 0, all 164 curly quotes in Newsreader). Pre-fix census: 545 Latin-in-CJK-sans elements. Post-fix defects, all D5-caused: (1) P6 head `READ THE CHART　Leia o gráfico` HEAD TOO WIDE +10.1 px advance at 25 → head size 25 → 24 (`content56.py:112`); (2) P7-col3 head `AN EXAMPLE LETTER　Exemplo` HEAD TOO WIDE +10.1 px advance at 25 → head size 25 → 24 (`content7.py:104`); (3) P1 cream-box title `THE WEEK IN NUMBERS　Números` +23.5 px right → `tsize` 23 → 21 (`content12.py:43`); (4) P6 cream-box title `HOW LONG?　Duração do mandato` +4.0 px right → `tsize` 23 → 22 (`content56.py:171`). Layout only, text unchanged. Gates: run rc=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; `head_check.py` PASS 0 defects; `render.py` + `webpdf.py` rc=0; `occlusion_audit.py` 0 flags (selftest OK); `p8.py extract` 60/150 (same set), `compare` **CLEAN**, keydiff=[137, 138, 139, 140, 150] (expected); `freeze.py baseline` **8/8**; `freeze.py diff` vs core-en TOTAL added CJK 9, all U+3000; added Latin strings 363 (D5 run-splitting); `spill_sweep.py` 0 SPILL (148 OBSERVE); `boxtitle_check.py` 0 DEFECT / 0 OBSERVE / 0 marginal (34 titles, 183 body lines); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` **PASS 0 defects** (ratios n=467 median 1.003, bold 1.049); `d5_census.py` **PASS** — D5 Latin 0, Cyrillic 0, curly in CJK 0, 164 curly in Newsreader, `Noto Sans` elements 0; print/web `pdftotext` byte-identical, 38,095 chars, unchanged vs pre-fix; text.md byte-identical (`f85c55ce…`, 54,120 B). P8: 192 → 192 lines, footer slack 47.8 → 37.8 px. **OVERALL: ALL-GREEN.** Pre-D5 baselines (disk-measured): print `52452731…` (29,345,708 B), web `b787bd7d…` (2,418,221 B); new SHAs in §2 (print `4ecc163c…`, web `dbc0fefb…`).

## 4. Translation decisions (Portuguese, Brazilian)
- Follows W46 pt (TM): você-form imperatives (Complete, Reescreva, Emparelhe, Corrija); gloss format
  "term = translation", "·" separators, "Nota — " box prefix (bslib4 gloss() prepends it;
  gloss translations are bare — only the P1 bridge carries its own label, "Nota — ",
  which the bridge-size patch matches via the empty gloss_word, first f.bridge() call).
- "runoff" = "segundo turno"; "call a race" = "anunciar o resultado"
  (registry notes keep the TM "anunciar o resultado da eleição" — two different source literals,
  both correct); "to certify" = "certificar oficialmente"; "midterm" = "as eleições de meio
  mandato"; "seat" = "um assento"; theme "Break the Silence" = "Quebre o silêncio".
- Numbers box keeps the English term with a Portuguese gloss in parentheses (W46 pt precedent).
- P2 calendar lines in full-Portuguese short form (es precedent — avoids the fr P2 overflow):
  "10 nov. — os republicanos escolhem seu líder · 18–19 nov. — os democratas votam" /
  "20 nov. — Dia Mundial da Criança · 26 nov. — Thanksgiving · 27 nov. — Black Friday".
- SAY IT title = "Como dizer a data" (date, not clock time — the de D-de1 lesson).
- P1 word-of-week bridge pre-shortened to 2 lines: "Eleições de meio mandato: toda a Câmara
  e um terço do Senado." (fr/es lesson).
- TM types (used as-is): 完成句子→"Completar frases", 翻译→"Traduzir", 写作→"Redação",
  阅读理解→"Compreensão de leitura", 单选→"Múltipla escolha", 完形填空→"Completar o texto",
  词汇配对→"Emparelhamento", 句型转换→"Transformação", 对话补全→"Diálogo".
  TM instr: 填空→"Complete", 把词和释义配对→"Emparelhe", 改写→"Reescreva", 配对→"Emparelhe".
- Fresh sets: instr 纠错→"Corrija"; types 从句→"Subordinadas", 将来时→"Futuro",
  时态→"Tempos verbais", 比较填空→"Comparativos", 过去时→"Passado", 金句填空→"Frases de ouro",
  纠错→"Correção", 图表读数→"Leitura de gráficos" (overrides the poisoned TM value "sans").
- ekeys: 137 "Os democratas venceram a Câmara e o Senado.",
  138 "A apuração continua.", 139 "O novo Congresso se reunirá em janeiro de 2027.",
  140 "Quebre o silêncio.", 150 "Questão aberta — veja os pontos no quadro de redação;
  o modelo está no quadro desta página" (dash form — lit_override; the TM value used a colon,
  the es Q150 trap).
- Box titles (single-line, re-measured at 23pt in this rebuild, budget 404.5 px; the old KIT
  numbers were mis-measured — the real ODD SOCKS value was 414.7, see §5 item 4): "SENATE IN
  NUMBERS　O Senado" 367.2; "HOW LONG?　Duração do mandato" 395.6 (tightest, ink margin +8.5);
  "ODD SOCKS, IN NUMBERS　N.º" 346.2; "SATURDAY, NOV 21　Sábado" 317.8; "HAYMITCH'S GAMES　Os
  Jogos" 348.1; "THE CALENDAR　Calendário" 319.1; "THE WEEK IN NUMBERS　Números" 390.9;
  "THE TOOLBOX　Ferramentas" 327.4 — all fit, audit 0 flags.
- P8 section heads use TM short labels ("Escolha", "Frases", "Diálogo") that differ from the
  registry type names ("Múltipla escolha", "Completar frases", "Diálogo") — same pattern as fr/es/it.

## 5. Fixes in this round
1. **Q150 colon → dash via lit_overrides** (es lesson, caught before the first build): the W46 pt TM
   value for the Q150 key uses a colon ("Questão aberta: …"); p8.py detect_note needs " — "
   before the trailing paren note. Overrode to dash form in fresh-pt.json.
2. **P8 key size pre-set to 13.5/1.26** (not 15.5/1.3 from the W46 meta) on the es/it lesson.
   P8-keys ends 2443/2560 — same as es/it.
3. **SCRATCH path fixed at sed time** (it lesson): the make_textmd adaptation now replaces
   `scratch-fanout-en/it` (no trailing slash) explicitly; verified SCRATCH = pt before running.
   No text.md failure this round.
4. **Rebuild + fix1 (11 Nov 2026, core-en fix1 sync — this round).** Core-en was fixed and
   re-proofed (Q39→a, Q40→d, Ashes rewritten as a 2025–26 retrospective, 已宣布 wording,
   SEARCHES/DID YOU KNOW box heights, SENATE/SATURDAY titles, SAY IT middle panel widened)
   and this edition was rebuilt from the fixed core via `scratch-fanout-en2/fanout/apply.py` +
   patched `map-pt.json` (14 new literals: Q39/Q40 keys + notes, Q46/Q52/Q55/Q125 notes,
   SATURDAY/SENATE titles, P1 strip, Q7/Q82/Q83/Q84 notes, P6 bridge). Proof1 defects D1–D2
   were core-level and are resolved by the rebuild (verified per edition: registry keys
   39=a/40=d, notes `mentor = um mentor a` / `arena = a arena d`; Q46 note dated Fri 21 Nov
   2025; Q52 `hosted`, Q55 `won`, Q125 `A (4–1)`; text.md answers 39→a, 40→d, 125→A;
   `Arsenal are winning!`; no `Perth is winning!` / `second week in Perth` / `Ashes begin`).
   The old ABSTRACT was short-form (§9-class, like ja D4) and was rewritten to the full form
   (announced results; certification 10 Nov–18 Dec; 16 Nov Anti-Bullying/Odd Socks; 20 Nov
   Children's Day + Hunger Games; 21 Nov Premier League back + Turin ATP final + Ashes 4–1
   look-back; reader language; A2–B2; 150).
   **New defect found by this round's own boxtitle sweep (pre-existing, missed by pt proof1):**
   P5 box title `ODD SOCKS, IN NUMBERS　Números` measured 414.7 px against the 404.5 px budget
   (−10.2 px; identical in the pre-rebuild SVG — the old KIT's claimed 397.2 was mis-measured).
   Same defect class as ko D3 and the ja P5 title found this round. Fixed to
   `ODD SOCKS, IN NUMBERS　N.º` (346.2 px, +58.2; "N.º" is the standard Portuguese abbreviation
   for "número(s)") in `map-pt.json`, full rebuild + re-gate; only `svg/p5-youth.svg` changed vs
   the first build of this round. All 18 SVG box titles now fit (tightest HOW LONG? +8.9 advance,
   +8.5 true ink).
5. **Rebuild gates (11 Nov 2026, second build of this round; logs in
   `hidden_files/w47/scratch-fanout-en2/fanout/pt/build-gates.log`)**: `run.py` exit 0, zero
   OVERFLOW / TOO WIDE, all flows within bottom, TOTAL 150, MODEL 82; `occlusion_audit.py`
   0 flags, selftest OK; `p8.py extract` noted set 60/150 (same set as core); `p8.py compare`
   CLEAN, keydiff=[137, 138, 139, 140, 150] (expected); registry vs P8 extract 149/150 exact
   + n=150 short-label exception; registry keys vs core 145/150 (diff only the 5
   reader-language keys 137–140, 150); `freeze.py baseline` 8/8 SVGs byte-identical;
   `freeze.py diff` TOTAL added CJK 9, all U+3000; print/web text layers 47,926 chars each,
   token-multiset diff 0/0, per-page byte-identical 8/8; `check_s11.py` ALL PASS; source
   boxtitle sweep 12/12 fit; SVG boxtitle sweep 18/18 fit; canonical `creambox.py` scan: all
   inside-only clearances positive; P8 min PDF font 10.12 pt ≥ 9.75 pt; SVG zero real CJK.
   (First build of this round passed everything except the two boxtitle sweeps, which caught
   the ODD SOCKS title above; the second build is the shipped one.)
6. **Delta Q73 speak→up (11 Nov 2026, core-en fix2 sync — this change only).** Core-en fix2
   changed the Q73 key `"speak"` → `"up"` (stem `Speak ___: tell a teacher.`, note
   `speak up = …` untouched); all 10 en-* reader editions carried the old key. This edition
   synced the one key only: `content56.py:49` key `"speak"` → `"up"` (note + stem verbatim);
   no other source line, map, translation file, ABSTRACT or KIT file touched. Rebuilt via
   `run.py` / `dump_reg.py` / `make_textmd_w47.py` / `render.py` / `tools/webpdf.py`.
   Diffs: registry exactly 1 line (Q73 speak→up); text.md exactly 1 line (l.1151);
   SVG only `p8-test.svg` changed (p5 stem page byte-identical — the stem string never
   changed); print PDF same byte size, new SHA (see §2); web PDF 2,418,222 B.
   Q73 four-source agreement: registry `up`, text.md `up`, P8 printed key `73. up`,
   P5 stem `Speak ___` + note `speak up = falar sem medo`.
   Full re-gate (logs in `hidden_files/w47/scratch-delta-en-pt/`): run.py rc=0, TOTAL 150,
   0 overflow; occlusion 0 flags (edition + core + NEW vs core 0); p8 extract 60/150 both,
   compare CLEAN, keydiff [137, 138, 139, 140, 150]; freeze: 版 baseline 8/8
   (`--build` 指版目录，`--core-svg` 指版 svg 目录；见 `freeze-edition.log`）+ core 只读
   对照 8/8（直接 sha256，见 `core-readonly-check.txt`）；另 `--build core-en` 补充 8/8；
   freeze diff p8 +106/−100 (was +105/−99 — the one changed key string), other pages
   identical counts to proof1, added CJK 9×U+3000; print/web token diff 0/0 (47,923 chars);
   per-page layout bytes identical 8/8 (p8 23,483 B vs 23,489 B pre-delta, only the answer
   reflow); keycheck 150/150, 0 mismatches; P8 min font 10.12 pt both PDFs (others 11.62);
   boxtitle source + SVG sweeps PASS (tightest HOW LONG? +8.9 advance / +8.5 true ink);
   `check_s11.py pt` ALL PASS; creambox + creambox2 logs byte-identical to proof1
   (24 heuristic next-section flags + the P1 406-px header-top strip, both dispositioned in
   proof1; only known tight margin P2 AND YOU true-ink +0.9 px unchanged); furniture strings
   verbatim; pdffonts 41/41 objects (record only); pixel diff vs proof1 renders: p1–p7 0 px,
   p8 4,509 px (0.15%) confined to the answer block (x 404–719, y 1699–1757); 8 pages + web
   P1/P8 visually checked, clean. Fill-in/transform audit: all 65 fill-in items re-checked
   (34 Completar frases + 16 Transformação + 8 cloze + 7 P7 drills) — every key fits its
   blank; Q73 `Speak [up]` correct. Pre-existing repeats (Q6=Q12 January, Q2=Q95 call,
   Q5=Q96 changed) unchanged from proof1 (a), not defects of this delta.

## 6. Self-check (2026-11-11)
- Full read of `2026-w47-en-pt.text.md` (all ~1,306 lines): zero issues.
  Notes kept: "SPORT · Desporto" is the shipped W46 pt head (content34.py:96) — kept as-is, not a
  defect; Q13 note "Segunda volta a 1 de dezembro" (TM, European form) coexists with the fresh
  "segundo turno" (Q21) — two source literals, both correct Portuguese, kept like the fr/es
  Q136/Q105 pattern; Q2/Q95 note "call a race = anunciar o resultado da eleição" (TM) vs P6 gloss
  "anunciar o resultado" — two source literals, both correct; Q34 "(open = estrear (terceira
  pessoa do singular com s))" correct; Q54 "eight (oito = eight)" tautological like the core's
  note pattern; Q97 "take time = levar tempo" is the TM value; Q110 "more than, a estrutura"
  terse as in core; Q136 "whether = se" vs Q105 "whether = se (para o que não se sabe)" — two
  source literals, both correct; "Cinco frases de crítica: quem, onde, o que aconteceu,
  a reviravolta e o final; cinco bastam." is the W46 pt TM value for the FIVE SENTENCES bridge
  (kept); "Inglês de jogo: o placar, quem marcou, quem está na frente; frases curtas, como ao
  vivo." and "Um mapa: cinquenta estados, cinquenta regras; …" are W46 pt TM values (kept).
- All 8 cards visually checked after the final render — clean. P1: bridge 2 lines clear of
  IN BRIEF, numbers box English+gloss, "TRY IT NOW · Pratique agora", footer "Página 1 de 8".
  P2: calendar short form, "THE SENATE, IN NUMBERS · O Senado", SAY IT "Como dizer a data",
  gloss single "Nota — to certify = …". P3: "COMING SOON · Em breve",
  "HAYMITCH'S GAMES · Os Jogos", gloss single "Nota — a tribute = …", Rousseau tiger.
  P4: "SATURDAY, NOV 21 · Sábado" (core fix1 title), gloss single "Nota — a Test: …", W. G. Grace photo; P4 lead is the Ashes 2025–26 retrospective "Perth, One Year On: How Australia Kept the Ashes".
  P5: "ODD SOCKS, IN NUMBERS · N.º" (see §5 item 4), gloss single "Nota — bullying = …",
  "SPEAK UP · Fale alto", Lawrence children photo. P6: "HOW LONG? · Duração do mandato",
  gloss single "Nota — to call a race = …", "A PRACTICE BALLOT · Cédula", voting booth photo.
  P7: all gloss boxes single "Nota —", "THE TOOLBOX · Ferramentas", "READERS' CORNER · Cartas",
  "AN EXAMPLE LETTER · Exemplo", "ERROR CLINIC · Erros", "NEXT WEEK · Prévia do VOL.5",
  Johnson portrait. P8: cloze + [A2] option tags, "B MULTIPLE CHOICE · Escolha",
  "C READING · Compreensão", "D SENTENCES · Frases", "E TRANSLATION · Tradução" with
  "Traduz:", "F WORDS · Emparelhamento", "G DIALOGUE · Diálogo" + "Levels: 145–149 [A2]",
  "H WRITING · Escrita [B1]" + Portuguese instruction, MODEL + Reading Room photo,
  ANSWERS block all 150 keys ending well above the footer with "150. Questão aberta — veja os
  pontos no quadro de redação; o modelo está no quadro desta página (Pontua-se por pontos)";
  footer "Página 8 de 8".

## 7. Furniture
- foot_left "The Lucerna　SEMANÁRIO INGLÊS VOL.4　TEXTOS EM INGLÊS　EXPLICAÇÕES EM PORTUGUÊS";
  foot_right "Página {n} de 8"; gloss_prefix "Nota — "; p8_sep "— Página {pg} —";
  translate prefix "Traduz: "; badge "TEXTOS EM INGLÊS　EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO
  PARA OS LEITORES DE LÍNGUA PORTUGUESA"; topstrip "WEEKLY IN ENGLISH　Todas as semanas　Do que
  se fala no mundo anglófono"; edition line "SEMANÁRIO EM INGLÊS　VOL.4　ELEIÇÕES　SELVA　CINEMA";
  edition spacing 6.9; p1_bridge_size 19.5; p8_mode "notes".

## 8. Provenance
- TM: W46 `2026-w46-en-pt` positional alignment (260 pairs). Poisoned values caught:
  'note' → 'P8 saved, TOTAL exercises:' (harmless, rejected by build_map's POISON regex);
  '图表读数' → 'sans' (overridden by fresh type "Leitura de gráficos").
  'THE ERROR CLINIC　易错诊所' → 'THE ERROR CLINIC　Clínica' is a legitimate W46 head, not poison.
- Map: `scratch-fanout-en2/fanout/map-pt.json` (lit 248, instr 5, type 17, ekey 4).
  Misses: 205 total, 182 with real CJK = 171 lit + 7 types + 4 ekeys.
  build_map normalizes U+2019 → ASCII apostrophe in all map values (fr lesson).
- F-MAIL: no real letters arrived; P7 prints the labelled editor's example + the VOL.3
  disclosure promising real letters from VOL.5. No invented letters, no email checked.

## 9. Build record
- `scratch-fanout-en2/fanout/pt/` — build-gates.log, make_textmd_w47.py, occlusion.log/json,
  p8-extract/compare.json, freeze.log/diff.json, webpdf.log, textmd.log, registry.json, dump_reg.log,
  freeze-final/.

## 10. Tool note (NOT fixed — p8.py is off-limits to the builder)
- `tools/p8.py` FOOTER_RE does not match the mixed-case footer "The Lucerna …" + "Página 8 de 8":
  the merged footer line leaks into the last answer segment (key 150) for every edition.
  Masked when key 150 is dash-style (pt, it, fr, de), bites when paren-style without a dash (es,
  before its fix). A case-insensitive match on the masthead, or dropping the merged footer line
  by its y=2624 baseline, would close it.
