# Lucerna 日本語版 × Italiano — VOL.2 Production Kit (W45) — BUILDER-COMPLETE (not finalized)

Week: **Monday 2 – Sunday 8 November 2026** · Issue dated **Monday 2 November 2026**.
Edition: **Japanese text + explanations in Italian** (JA × IT), built from the W45 JA core
(`files/weekly-report-w45-ja-core/`, VOL.2, Chinese explanations) by localizing ONLY the
explanation layer. Japanese articles, stems, options, letters, figures, and the P7 word-box
Japanese definition sentences are frozen byte-identical.

STATUS: builder-complete. This edition has NOT been finalized, has NOT been independently
proofread yet, has NOT been sent to Discord, has NOT been posted to the main chat, and has
NOT been inserted into the weekly repo. No cron was created and `~/workspace/weekly-git`
was not touched. The independent proofread gate (SOP §8) is still pending.

Build directory: `hidden_files/weekly-report-w45-ja-it-build/` — `transform.py` (the single
fix vehicle; all fix rounds edited this file only), `transform-round1.py` /
`transform-round2.py` / `transform-round3.py` (per-round snapshots), `run.py` + `render.py`
+ `content*.py` + `bslib4.py` + `svglib.py` + `assets/` (all produced by `transform.py` from
the pristine core build), `audit_gates.py` (ADVANCE / frame / P6-chart / kinsoku / phrase /
gloss / image / residual / P8-line audits), per-round logs and sha256 baselines
(`core-baseline-pre.txt`, `sha256-round1.txt`, `sha256-round2.txt`, `sha256-round3-prefix.txt`,
`sha256-round4.txt`), `freeze-diff-final.json`, `p8-final.json`, `occlusion-final.json`,
`audit-gates-final.json`.

## 1. Spec (per SOP + W45 JA core)

- 8 pages, 1950 × 2700, 4 columns, warm ivory `#f7f1e2`, deep olive `#3e4c2a`, brick chips.
- Masthead: blackletter **Lucerna** with **NO article** (Japanese is article-less per SOP).
- P1 masthead geometry follows the W43 JA × IT shipped SVG exactly (see §3 deviations):
  wordmark y=248, edition line y=316, badge y=356 at 19pt, strapline y=390, double rules
  y=406/413, dark band y=424 (unchanged from core).
- Badge (verbatim W43): «TESTI IN GIAPPONESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER
  I LETTORI ITALIANI». Footer: «Lucerna · SETTIMANALE GIAPPONESE VOL.2 · TESTI IN
  GIAPPONESE · SPIEGAZIONI IN ITALIANO». Page line: «Pagina N di 8». Gloss prefix:
  «Nota — ». P8 separator: «— PAGINA N —». P4 band title_left «スポーツ · 体育»
  deliberately unchanged (JA-family convention, as in the W43 JA × IT KIT).
- Topics (core-fixed, from the core KIT): Culture Day Tue Nov 3 + autumn-leaf weekend
  Nov 7–8 (Naruko Gorge peak, Kobe Nunobiki Herb Garden light-up from Sat Nov 7) +
  ゆる整え食 (Ajinomoto, Oct 21) + Reading Week in progress (to Mon Nov 9) + 立冬 Sat
  Nov 7. Japan Series P4: G1/G2 verified in full; G3–G7 schedule only, with the on-page
  deferral to VOL.3. Oct 31 Halloween is a just-passed report. P6 chart is labeled
  practice data on the chart itself.
- Images (4, payload md5-identical to the core per page, §6): P1 maple (Poliphilo, CC0),
  P3 Utagawa Hiroshige III print (public domain), P4 Yokohama Stadium (Syced, CC0),
  P5 pumpkins (Petr Kratochvil, public domain). Credits use the Commons API Artist field.
  P2/P6/P7/P8 carry no photo, as in the core.

## 2. Measured totals (one consistent method: registry output + SVG text extraction)

- **Exercises: 150 exactly** (benchmark ~150 met).
  - By level: **A2 46 · B1 75 · B2 29** (= core).
  - By page: **P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38** (= core).
  - By type (Italian type names): completamento 50 · scelta multipla 51 · abbinamento 12 ·
    costruzione di frasi 8 · vero/falso 11 · cloze 13 · traduzione 4 · scrittura 1.
- P8 writing model: 『私の11月の週末』, **167 characters**, byte-identical to the core
  (full model text compared from the rendered P8 SVGs, not just the first line).
- P6 practice chart: 近場の満足 38 · 温泉 27 · 紅葉 21 · グルメ 14 = 100, labeled
  «練習用データ · Dati di esercitazione» on the chart.
- P7 phrases of the week: all 8 occur **exactly 2×** in the whitespace-stripped
  concatenation of all SVG text (article + P7 box). Page tags in order:
  p.1, p.1, p.2, p.2, p.3, p.4, p.5, p.6.
- Gloss items (rendered gloss() strings split on `·`, item by item): **39 total =
  P1 4 / P2 9 / P3 8 / P4 7 / P5 7 / P6 4** (= core's grouping; the source-grouping
  13+15+11+0 is a different counting basis and is NOT used as the render conclusion).
- P7 columns: A2 本と読書のことば / B1 紅葉のことば / B2 数字を読む; error clinic 4;
  frame box 『ゆるく整える』; readers' corner + VOL.3 teaser (§5).
- P8 sections A–H; E zone re-aimed JA↔ZH → JA↔IT (§4).

## 3. Furniture: three-way comparison (W45 core / W43 same pairing / this edition)

W43 same-pairing (files/weekly-report-ja-it, VOL.1) rules over the tools README #20
generalization wherever they differ. Measured from the W43 shipped P1 SVG:

| Item | W45 core | W43 JA × IT (shipped) | This edition |
|---|---|---|---|
| Wordmark y | 262 | 248 | 248 (W43 wins) |
| Edition line y | 330 | 316 | 316 |
| Badge | — (subtitle slot) | (975, 356), 19pt, verbatim string §1 | identical string + slot |
| Strapline y | 372 | 390 | 390 |
| Rules y | 392 / 401 | 406 / 413 | 406 / 413 |
| Dark band y | 424 | 424 | 424 |
| Top strip | 每周一期 | Ogni settimana | Ogni settimana |
| Footer | 日语周报 VOL.2 | SETTIMANALE GIAPPONESE VOL.1 | SETTIMANALE GIAPPONESE VOL.2 |
| Page line | 第 N 版 / 共 8 版 | Pagina N di 8 | Pagina N di 8 |
| Gloss prefix | 译注｜ | Nota — | Nota — |
| P8 separator | — 第N面 — | — PAGINA N — | — PAGINA N — |

Deviations from the task brief's JA-family reference figures, each adjudicated by
measurement (not assumed):

1. **Wordmark 262 → 248.** The brief's 262 is the JA-target family reference; the W43
   same-pairing shipped SVG measures 248, and the task orders W43 first. 248 used.
2. **P1 numbers box title shortened to «In numeri».** The W43 JA × IT KIT records the
   identical fix («La settimana in numeri» ink 990.8 > box border 961); round 1 of this
   build reproduced the same overflow (ink 990.8 > 961), so the W43 wording was adopted
   verbatim. Audit now 0 BOXTITLE.
3. **P4 schedule box title «Calendario».** W43 JA × IT shortened form (the longer
   «Il calendario delle Series» overflowed there); adopted directly.
4. **P7 frame box title «La frase tipo».** W43 JA × IT shortened form; adopted directly.
5. **P2 match instruction shortened to «Abbina parole e significati».** New measurement
   (not a W43 carry-over): the first rendering «Abbina le parole ai significati» ended
   at advance x=1907.2, past the 1885.5 content margin; the shortened form ends at
   1880.9. Same wording is used for the P8 F-zone match instruction.
6. **P8 answer-note shortenings (round 2, wording only, meaning preserved).** Italian
   notes run longer than the core's Chinese notes and the 4-column answer flow overflowed
   (ended y=2585, 4 clamped overlaps). 19 answer lines were tightened (e.g. «La mostra
   di artigianato è al Museo d'arte della prefettura di Ishikawa» → «Mostra di
   artigianato al Museo d'arte di Ishikawa»; «Testo modello nella sezione H di questa
   pagina (167 caratteri)» → «Testo modello nella sezione H (167 caratteri)»). After
   the change the flow ends at y=2413 with no overflow. No key, stem, or fact changed.

## 4. P8 gates (the two JA-family trap doors, both closed explicitly)

### 4a. P8 #37 bare-string trap — handled, verified on the printed line

Core `content34.py:82` registers the P3 fill-in note as the BARE string
«工艺展到11月8日» (no weekday suffix), key 8, stem «展覧会は11月 ___ 日（日）までです。».
2026-11-08 is a Sunday (verified with `date`: Sunday 2026-11-08; the stem itself says
（日）). `transform.py` maps the bare key EXPLICITLY to the Sunday-suffixed Italian
form, identical to #32's rendering. Printed P8 line (from the shipped SVG):
«37. 8 — La mostra dura fino all'8 novembre (domenica)». No bare Chinese string reaches
the page. The sibling JA×EN/JA×DE/JA×FR builds hit the same trap; this build's mapping
is a dedicated, commented entry in `transform.py`, not a fall-through.

### 4b. P8 note-completeness comparison (not just mapped-key audit)

`tools/p8.py compare` alone cannot see untranslated notes that are byte-identical to the
core (freeze diff cannot see them either — they are not changes) and an English-word scan
cannot see Chinese. Therefore, in addition to the tool run, the builder compared the
printed P8 answer lines core-vs-edition line by line (150 items + 8 separators = 158
lines each side, reconstructed from the shipped P8 SVGs):

- Printed-note sets: **core 150 = edition 150, missing [] extra [] uncertain []**,
  status **CLEAN** (`tools/p8.py compare`, explicit `--core-p8` / `--edition-p8` paths;
  the `--target it` dir form mis-derives a filename and was not used).
- **Byte-identical P8 lines: 0.** Every core line differs in this edition — i.e. there is
  no untranslated note hiding as an unchanged line. (Separators differ by design:
  «— 第N面 —» → «— PAGINA N —»; E-zone/H-zone notes differ by re-aim/localization.)
- Keydiff accounting (unambiguous, no double counting). Tool keydiff (22 entries):
  [1, 2, 5, 7, 8, 9, 29, 32, 37, 65, 69, 78, 101, 113, 115, 117, 118, 137, 138, 140, 146, 147].
  **22 = 2 true key re-aims + 1 note-localization surfacing inside keydiff + 19
  extraction artifacts.**
  - True re-aims (E-zone JA→IT direction, keys change language by design): **#137**
    («文化日是11月3日。」 → «La Festa della Cultura è il 3 novembre.»),
    **#138** («乱扔垃圾，要罚2,000日元。」 → «Se butti i rifiuti, la multa è di 2.000 yen.»).
  - Note-localization inside keydiff: **#140**. Its printed key (the Japanese sentence
    «神戸の紅葉のライトアップを見に行きたいです。») is byte-identical; the tool's
    paren rule exposes the localized note («Vedi pagina 6 (le luminarie di Kobe)»)
    inside the extracted key field. It is NOT a key change.
  - Artifacts (19): #1, 2, 5, 7, 8, 9, 29, 32, 37, 65, 69, 78, 101, 113, 115, 117, 118,
    146, 147. In each, the tool's trailing-paren rule strips the weekday/qualifier paren
    from the note and leaves «key — note-minus-paren» as the extracted key; the note
    text differs because it is translated, while the true printed key (letter, digit,
    ○, or word before the first « — ») is byte-identical to the core in every case
    (verified item by item against the printed lines; #37's true key is 8 in both).
  - Outside keydiff (NOT additional keydiff entries): **#139** — key byte-identical
    Japanese, note localized («对照第7版» → «Vedi pagina 7»); **#150** — key «✓»
    identical, apparatus note localized («Testo modello nella sezione H (167
    caratteri)»). Counting #139/#140 as «2 + 19» on top of the 22 would double-count
    #140; the correct statement is the 2+1+19 = 22 above, with #139/#150 noted
    separately as non-keydiff localizations.
- P8 printed-note count per the tool: **150** (the core prints all 150 notes, and so
  does this edition; P8 note count is 150, NOT the EN family's 78).

## 5. Readers' corner (P7) — frozen letter, honest disclosure, no fabrication

- Japanese example letter (lt) frozen verbatim, including its closing
  «— 読者の手紙の例». No person, letter, or quotation was invented.
- Operative disclosure is ONE Italian paragraph (following the JA×EN coordinator-ruling
  pattern: the core's Japanese disclosure line cannot serve Italian readers, and the
  Chinese line is the core's reader-native layer; both are replaced, not stacked):
  «Esempio della redazione, non una lettera vera. Entro la scadenza non sono arrivate
  vere lettere né i migliori testi di pagina 8; entrambi appariranno nel VOL.3. Scrivici
  in giapponese!» — containing all 3 facts (sample, not a real letter; no real letters
  arrived; no best Page 8 compositions arrived) + an explicit imperative invitation
  («Scrivici in giapponese!») + the VOL.3 promise. The VOL.3 teaser row below it is a
  contents preview and is NOT counted as the invitation.
- No target-language disclosure sentence was fabricated to fill a bilingual slot: this
  edition's disclosure IS the localized reader-native disclosure (the core's lcn role),
  not an invented extra. The teaser body (Japanese VOL.3 promises) is frozen.
- P7 target-language definition sentences in the three word columns are frozen verbatim:
  the freeze diff's P7 removed/added lists contain only explanation-layer strings
  (glosses, headers, clinic notes, phrase translations, disclosure, page line, footer,
  instr label «填空» → «Completa»); no Japanese column body sentence changed. The only
  Japanese fragments in the removed list are wrap fragments of mixed gloss/header lines
  whose Japanese headwords reappear verbatim in the added lines.

## 6. Geometric + text gates (all measured on the FINAL round-4 render, venv PIL)

- Canonical `tools/occlusion_audit.py` (selftest green, all 6 classes fire, clean
  controls silent): **edition 0 flags, core 0 flags, NEW vs core 0**.
- Same-baseline ink collisions on furniture bands: 0 (P1 top band: VOL.2 left, center
  strapline, right date — no overlap; the P1 TEXTX graze from round 1, Italian trend
  sentence wrapping onto the source line, was fixed by wording, §3).
- ADVANCE right-edge scan (all text elements, limit x=1885.5): **0 violations**
  (round 3 found 1, the P2 match instruction, fixed §3 item 5).
- Full-page frame scan (every text ink box vs every rect border and every rule line,
  the dimension the canonical audit does not cover): **0 hits**.
- P6 chart-label coverage, baseline-anchored ink method (PIL getbbox, anchor ls, bars
  as later-drawn rects; NOT the getbbox-width method): **max 0.000** (gate <30%).
  Chart labels sit fully clear of the bars.
- Kinsoku line-start scan (full-width NO_START set): **0 hits**.
- P8 answer-flow end: **y=2413 < 2540**; P7 teaser end: **y=2524.12 < 2540** (56 px clear
  of the 2580 footer line). **No FLOW OVERFLOW / HEAD TOO WIDE** in the final build log
  (build4.log; earlier rounds' overflows are recorded in §7).
- Freeze: `tools/freeze.py diff --strict-cjk`: **added CJK = 0 on all 8 pages**.
  Core baseline: `tools/freeze.py baseline` on the pristine core build: **8/8 SVGs
  byte-identical**, core untouched (re-hash after the run clean).
- Core integrity at delivery: all 18 pre-recorded core hashes (8 SVG + 8 cards + 2 PDFs)
  re-verified unchanged.
- Residual-Chinese scans on the final SVGs: character scan + word-level scan (core note
  keys as substrings; Chinese-only words list) — **0 explanation-layer hits**. The only
  simplified-form characters present are inside legitimate Japanese words (学校, 会社,
  出会う, 展覧会, 全国, 学ぶ, 中学生). A code-level survivor scan (core CJK quoted
  strings still present in the edition build) returns only frozen Japanese strings and
  documented note-prefix-of-stem substrings (e.g. a note that is the stem minus 。,
  and the frozen chart sentence containing «練習用データです»); the transform's own
  post-audit asserts no note key survives as an exact quoted string in the edition code.
- The banned intermediary-layer term: **0 occurrences** in the SVGs, the build code,
  this KIT, and ABSTRACT.txt (grep-verified; the transform's search-pattern strings are
  the core's own Chinese explanation strings being replaced, not the term).
- svglib: canonical file, md5 `d73e23b365676c3618d7e060b835eb4d`, never edited,
  SEAM_SLACK=28 in place.
- All 8 cards viewed individually (P1–P8): no overflow, overlap, clipped label, or
  misplaced box. Feature-column whitespace on P2/P4/P5/P6 matches the core's pattern
  (disclosed, as in the core KIT).

## 7. Fix rounds (each round's edits went into transform.py first, then a single-process re-render; pre-fix sha256 baselines recorded each round)

- Round 1 (baseline): first full build. Counts exact; defects: P7 teaser band ended
  2582.12 (past 2540) because the Italian disclosure ran longer than the core's two
  lines; P8 answer flow overflowed (ended 2585, last items clamped/overlapping);
  P1 numbers title overflowed its box (ink 990.8 > 961); P1 trend sentence wrapped onto
  the source line (TEXTX graze).
- Round 2: disclosure shortened; numbers title → «In numeri»; trend sentence → one
  line; 19 P8 answer notes tightened (wording only). Result: P8 flow ended 2413, no
  overflow; P7 teaser still 2553.12 (disclosure still one line too long).
- Round 3: disclosure shortened once more (invitation + VOL.3 promise kept). Result:
  P7 col3 ends 1750.12, teaser ends 2524.12. P8 unchanged.
- Round 4: P2 match instruction shortened (§3 item 5). Result: ADVANCE scan 0
  violations. Only P2/P8 SVGs + cards + PDFs changed vs round 3 (sha256 diff verified);
  all other pages byte-identical. Final gates (§6) run on round 4.

## 8. Reproduction

```bash
cd hidden_files/weekly-report-w45-ja-it-build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python transform.py  # pristine core -> edition build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py         # content12+34+56+7+8 in ONE process (registry order = numbering)
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py      # svg -> cards PNG -> Lucerna-VOL2-IT.pdf + Lucerna-VOL2-IT-web.pdf
```

Interpreter record (both measured, not assumed):
- `run.py`: `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0 (self-chosen; the venv
  interpreter was used so the run byte-reproduces the core baseline; system python3 is
  also 3.12.3 but carries PIL 10.2.0 and was NOT used for run/render).
- `render.py`: `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0, cairosvg (mandatory:
  system python3 has no cairosvg). All audit measurements were taken on the rendered
  SVGs with venv PIL.
- Never use /opt/meta-chromium (hangs in this VM). Never run a build module standalone
  and never import one inside the core build directory (module-level OUT paths execute
  on import); all re-runs go through the single-process driver after transform.

## 9. Deliverables & PDF pins (final render, round 4)

- `svg/` × 8, `cards/` × 8 (1950×2700 PNG) in `files/weekly-report-w45-ja-it/`
- Print PDF: `Lucerna-VOL2-IT.pdf` — **28,797,345 B**, sha256
  `7ced69eeded294989496b9f798df0422efffb02ac12770ffd21ca4981f8ded8b`, 8 pages
- Web PDF: `Lucerna-VOL2-IT-web.pdf` — **3,098,042 B** (< 10 MB), sha256
  `c5d152d6482a72fa4ea3b4edce07bcab15e100072b5b482eb99c7bd1de0a467d`, 8 pages
- `WEEKLY-KIT.md` (this file), `ABSTRACT.txt` (Italian, single line, no ASCII double
  quotes, real topic keywords + the learner search phrase «imparare il giapponese
  leggendo»)
- Final SVG sha256 (round 4):
  - p1-hyoushi `f5625e06069723e2c533c41a6724a28e523132aac417644355fa12f9c83771a6`
  - p2-kurashi `4a35c88d92f92624fc7d405c1387449dfbe5e7c3b0e3a66af246d226845ba333`
  - p3-bunka `cccd4b978608ede9f3899b193d32f9ac8bd84d99362235fb7447f05469419ae3`
  - p4-supotsu `55f3e4dbd36784fb4e95524d6f6eec8684bcc93f3ae3085127683924f42c69b0`
  - p5-wakamono `04ae3b02e6b1128081229b244a1d8d065812c8765985f90a9cc5b0371bffc526`
  - p6-fukayomi `dbf862405390c7d30cc1e788bdaba566b7dd7a31548545b602109aa8cd936b1a`
  - p7-kotoba `ac281caf8841ebe3e0e056accb650f97ea0b5c8637be1e1997888804d248214b`
  - p8-tesuto `45700cd0f4d64a2b266e69be4221ca864d5fde3d59336868e4257b173972f1bc`

## 10. Residual, disclosed

- Feature-column whitespace on P2/P4/P5/P6 (same pattern as the core).
- P2 and P6 carry no photo (same as the core); P7/P8 carry no photo.
- The P7 B1 gloss line wraps mid-word («紅葉 | 狩り») — per-character CJK wrapping, same
  mechanism as the core; columns do not collide (occlusion 0, seam slack in place).
- Verification debt is inherited from the core KIT unchanged: Japan Series G3–G7 results
  and Halloween Oct 31 outcomes are NOT claimed anywhere in this issue; P4 states the
  gap and promises the roundup in VOL.3.
