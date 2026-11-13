# PROOF NOTE — 2026-W47 it-en (Italiano × English), independent round 2 (re-fan-out)

- Proofer: independent proof2 (no subagents used)
- Date: 2026-11-11 (UTC; work done 20:16–21:00 UTC)
- Edition dir: `production/2026-w47/2026-w47-it-en/` (clone `~/workspace/weekly-git`, main)
- Task: full re-proof of the re-fan-out build from scratch (SOP §8.4). Nothing was
  taken on trust from proof1 or from the re-fan-out report
  (`hidden_files/w47/scratch-refanout-it/FANOUT-REPORT-it.md`); every item below
  was re-measured by me. Where proof1 is cited, it is only as a cross-check.
- My scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-it-en1/`

## Identity (verified by me, full SHA-256)

- Print PDF `La-Lucerna-VOL4-EN.pdf` — 14,032,945 bytes
  sha256 `3b6b2d2c9067aa88e22914a83ef4ca6ddf37ce2e98e154c80bd9ca7fb79190fd`
- Web PDF `La-Lucerna-VOL4-EN-web.pdf` — 1,291,182 bytes
  sha256 `03bb1ff239dc46d408130d8c828417e004a9a0b488ba50e8594f5a8122dd5e2f`
- Text export `2026-w47-it-en.text.md` — 55,221 bytes / 1317 lines
  sha256 `f12950aa8561371585da7ada54b15eb83df595ccb0fe51cfa513650dffd6a984`
- All three SHA-256 values and byte sizes match the task brief and WEEKLY-KIT.md §7
  exactly. Identity confirmed; proofread proceeded.
- ABSTRACT.txt: one line, English, no ASCII double quotes, facts match the issue.

## Verdict

**(b) NOT zero findings: 3 defects, one class.** All three are English-gloss box
titles overflowing their borderless cream boxes — visible on the delivered print
PDF and the delivered web PDF alike (same SVGs). No定稿 decision is made here;
that is the coordinator's call. Observations O-1 – O-10 are listed separately
and are not counted as defects.

Why the builder's 20/20 gates missed them: `tools/occlusion_audit.py` BOXTITLE
covers bordered boxes only; these boxes are borderless cream (`#f0eee5`, no
stroke), so the tool is blind to horizontal overflow there — exactly the blind
spot the task brief warned about. The re-fan-out's PIL true-ink measurements
(`measure_built.py`) covered only the five table-fix languages (de/fr/pt/nl/ru);
`en` had no table-fix case, so its three long English gloss titles were never
measured. My scan (`cream_spill_orphan.py`, PIL true ink via
`occlusion_audit.ink_box` + pixel measurement on the 96 dpi render of the
delivered print PDF) covers all 29 cream rects on all 8 pages and flags exactly
these three.

## Defects

### D-1 (major) — P1 «LA SETTIMANA IN CIFRE» box title overflows its cream box by 155 px

- Location: P1, cifre box, title line. Sources:
  - `2026-w47-it-en/content12.py:44` — `f.box("LA SETTIMANA IN CIFRE　THIS WEEK IN NUMBERS", [`
  - `hidden_files/w47/scratch-fanout-it/translations.py:93` — `"en": "LA SETTIMANA IN CIFRE　THIS WEEK IN NUMBERS",`
  - Shipped SVG `svg/p1-prima.svg`: title node `x="556.5" y="1388.475" font-size="23" font-weight="700"`; cream rect `x="538.5" y="1351.475" width="422.5" height="442.75" fill="#f0eee5"` (box right edge x=961.0).
- Measured (PIL true ink, `occlusion_audit.ink_box`, Noto Sans CJK SC 23 bold):
  ink 556.5..1118.0 vs box 538.5..961.0 → **overhang 157.0 px** (ink).
  Pixel measurement on the 96 dpi render of the delivered print PDF
  (dark pixels in the title band, x restricted to 500..1250): ink ends x=1116
  vs box right 961 → **overhang 155 px**.
- Render evidence: `pages/crop-p1-cifre.png` (2× crop of the delivered print P1)
  and full page `pages/p-1.png`: the cream box visibly ends mid-title —
  "THIS WEEK IN NU" sits on cream, "MBERS" hangs off the box into the white
  gutter/column-3 space. The same overflow is visible on the web render
  `pages/web-p1-1.png`.
- Contrast with the core: the core title `LA SETTIMANA IN CIFRE　数字看本周`
  measures ink right 960.0 vs the same 961.0 box edge — fits with 1.0 px spare.
  The overflow is en-fan-out-specific: the English gloss is far longer than the
  Chinese gloss the 422.5 px box was sized for.
- Fix direction (for the coordinator, not a decision): the English gloss must be
  shortened (or the title wrapped/split) so the ink fits inside 538.5..961.0;
  source fix in `translations.py:93` (+ the generated `content12.py:44`), then
  full re-render + full re-proof.

### D-2 (moderate) — P2 «LA FRASE PER RICORDARE» box title overflows its cream box by 39 px

- Location: P2, frase box, title line. Sources:
  - `2026-w47-it-en/content12.py:177` — `f.box("LA FRASE PER RICORDARE　REMEMBER", [`
  - `translations.py:563` — `"en": "LA FRASE PER RICORDARE　REMEMBER", …`
  - Shipped SVG `svg/p2-vita.svg`: title node `x="556.5" y="1280.75" font-size="23" font-weight="700"`; cream rect `x="538.5" y="1243.75" width="422.5" height="210.9" fill="#f0eee5"` (box right edge x=961.0).
- Measured: PIL true ink 556.5..1000.8 vs box 538.5..961.0 → **overhang 39.8 px**.
  Pixel measurement on the delivered print render (title band, x 500..1150):
  ink ends x=1000 vs box 961 → **overhang 39 px**.
- Render evidence: `pages/crop-p2-frase.png` (2× crop) and `pages/p-2.png`: the
  cream box ends inside "REMEMBER" — the tail of the word (about 2½ letters)
  sits on white outside the box.
- Contrast with the core: the core title `LA FRASE PER RICORDARE　口诀`
  measures ink right 918.0 vs 961.0 — fits with 43 px spare. Again
  en-fan-out-specific (English gloss longer than the box allows).

### D-3 (minor) — P7 «ERRORI TIPICI» box title overflows its cream box by ~6 px

- Location: P7, errori box, title line. Sources:
  - `2026-w47-it-en/content7.py:83` — `p.text(bx + 22, yy3 + 26, "ERRORI TIPICI　COMMON MISTAKES", 23, "sans", True, OLIVE)`
  - `translations.py:969` — `"en": "ERRORI TIPICI　COMMON MISTAKES", …`
  - Shipped SVG `svg/p7-lingua.svg`: title node `x="1461.5" y="242" font-size="23" font-weight="700"`; cream rect `x="1439.5" y="200" width="422.5" height="813.5" fill="#f0eee5"` (box right edge x=1862.0, the page content edge).
- Measured: PIL true ink 1461.5..1868.5 vs box 1439.5..1862.0 → **overhang 6.5 px**.
  Pixel measurement on the delivered print render (title band y 218..248,
  x 1439..1950): ink ends x=1868 vs box 1862 → **overhang 6 px**.
- Render evidence: `pages/crop-p7-errori.png` (2× crop) and `pages/p-7.png`:
  the final "S" of MISTAKES straddles the cream edge — the box boundary cuts
  through the letter.
- Contrast with the core: the core title `ERRORI TIPICI　常见错误` measures ink
  right 1735.8 vs 1862.0 — fits with 126 px spare.

## Proof1 defect re-verified FIXED

- Proof1 D-1 (Chinese type label 「翻译」 in `.text.md` Q137–140): **fixed**.
  `.text.md` lines 969/971/973/975 now read `[A2 · Translate]`, `[B1 · Translate]`,
  `[B1 · Translate]`, `[B2 · Translate]`; the rendered P8 (`pages/p-8.png`,
  `pages/crop-p8-q137.png`) shows "137. Translate into English" /
  "140. Translate into Italian". Full-file CJK scan of the shipped `.text.md`:
  **0 CJK ideographs** (only 106 × U+3000 furniture separators and 14 × U+FF1A
  fullwidth colons in the 7 frozen notes — see O-4).
- Proof1 build2/build3 geometry defects re-verified fixed: P4 E TU box is 2 lines +
  gloss, flush with the results table (no occlusion flag); P7 LETTERE disclosure
  is 3 lines ending col3 y=1673.0, clear of the FRASI hline (occlusion 0 flags).

## Observations (not defects)

### O-1 — P1 cifre heads translated into English (4 lines), redundant value + gloss
Still present, unchanged from proof1 (e.g. `29 — Lazio's points, top of the table
after 11 matchdays (Lazio top with 29 points)`). Content factually correct;
deliberate build1 fix. Inconsistent with the P5 "IL PIANO DELLA SETTIMANA" box,
which keeps Italian heads with English glosses. Not counted: correct text,
documented engineering choice.

### O-2 — Byline "Dalla redazione de La Lucerna" uses archaic "de" for modern "di"
Still present (7 × "de La Lucerna", core-inherited, systematic house style).
Not counted: attested archaic form, survived two core proof rounds, core-level fix.

### O-3 — Spaced guillemets « la vetta » (P1 LA PAROLA box, P7 LA PAROLA) vs unspaced «…» elsewhere
Still present (2 × `« la vetta » :`, French typography). Core-inherited cosmetic
inconsistency.

### O-4 — Fullwidth colon ： in 7 frozen P8 notes (16–20, 60–61)
Still present (14 × U+FF1A in `.text.md`, 7 in the P8 key list + 7 in the exercise
list). Core-inherited, legible, no layout impact (P8-keys flow ends 2514/2552).

### O-5 — Matching-key letter echo in P8 keys (25–28, 52–55, 141–144)
Still present (e.g. `25. c — salute = health, c`). Core note format, translated
faithfully. Redundant but consistent.

### O-6 — Q120 stem truncated with "…" and options without parentheses
Still present, byte-identical to the core. Core's P8 cloze abbreviation style.

### O-7 — Q32 note uses curly quotes “Fate dolci” while the article uses «Fate dolci»
Still present. Inherited note style.

### O-8 — Masthead band, structural whitespace, P8 font size
Masthead band starts inside the page; P1 full-page render clean. P3/P5 mid-page
structural whitespace is the core pattern (documented in KIT §10). P8 answer
font 13.0 SVG px = 9.75 pt exactly at the SOP §1.1 floor.

### O-9 — British-English collective plurals are correct, not errors
"Lazio are top", "Roma have the best attack", "Udinese are bottom" — standard
British sports usage, consistent throughout.

### O-10 — Orphan scan: 3 flags, all byte-identical to the core (inherited, not defects)
My orphan scan flagged: P6 main text last line "18." alone (after "emendamenti,
alle ore"); P8 Q129 stem last line "due" alone ("…C. i / due"); P8 Q137 stem
blank "___" alone on line 2. Each flagged node is the identical node at the
identical x/y in the core SVGs (verified: core `p6-approfondimento.svg`
`<text x="1603.5" y="641.6">18.</text>`; core `p8-valutazione.svg`
`<text x="538.5" y="818.975">due</text>` — same in en). Frozen Italian text,
same column widths, same wraps. Not defects; noted for the record.
Render evidence: `pages/crop-p6-orphan.png`, `pages/crop-p8-q118.png`.

### O-11 — "56 titles" is a phantom number; measured title counts for this edition
No count of 56 corresponds to anything in this edition: the string "56" occurs
only twice in `.text.md` (exercise 56, stem + key). Measured: 6 article headlines
(P1–P6); 85 all-caps title/furniture lines in `.text.md` (incl. section bars,
box titles, exercise-group letters); 8 page sections + 1 answer-key section.
The builder's gates (20/20) do not count titles at all.

## What was verified (summary)

- Full independent read of the 1317-line `.text.md` (all articles, boxes, captions,
  exercises 1–150 with keys and notes); all 150 keys re-verified against stems/
  articles/charts by hand, plus the gates.py 150-key audit vs the core `.text.md`
  (keys match except re-aimed 137–139 and the writing item; notes match
  translations.py except 137–140 + writing).
- Level/page distribution: TOTAL 150; A2 47 / B1 70 / B2 33; pages
  10/18/18/18/18/18/12/38 — matches KIT. Model text counted by hand: 99 words
  (task range 80–100).
- Arithmetic spot checks: MD11 goals 3+1+2+3+3+2+3+1+2+4 = 24 in 10 matches;
  Q85 13−11 = 2; Q86 6+7 = 13; classifica Lazio 29 / Inter 28 / Roma 27 /
  Milan 24 / Como 23 / Udinese 5 (20th) — consistent across P1, P4 table and keys.
- Golden sentences: all 8 verified verbatim in their articles and on P7 FRASI
  (checked against the `.text.md` read; freeze diff shows 0 unexplained fragments).
- §8.1 gloss check: every NOTE-box headword occurs in its article (with normal
  inflection, e.g. "imbattuta" for "imbattuto", "candele" for "candela").
- Facts re-checked against public sources (web, 2026-11-11; proof1's Serie A /
  ATP / BookCity / Manovra checks stand and were not re-litigated, but the two
  edition numbers proof1 did not cover are now verified):
  - Eurochocolate 2026 = **32ª edizione**, Nov 13–22, theme "Fate Dolci", Calabria
    guest region, Iginio Massari at the Nov 22 finale — confirmed
    (eurochocolate.net; tagumbria.it; latuaetruria.it). Q30/Q123 key C correct.
  - Festa del Torrone 2026 = **29ª edizione**, Nov 7–22, 16 days / 3 weekends,
    theme "Il Confine", Torrone d'Oro to Cremona-born Davide Simonetta at 11:00
    Palatorrone Sun 22, corteo 16:00, Sforza–Visconti re-enactment 17:00 —
    confirmed (milanodimoda.it; foodtour.info; dossiercultura.it). All P3
    times/numbers match.
  - Serie A MD11 dates: Fri 6 / Sat 7 / Sun 8 Nov 2026 confirmed by `date`
    (Nov 9 Mon → Nov 6 Fri, Nov 7 Sat, Nov 8 Sun).
- Dates/weekdays (Europe/Rome `date`, all match the paper): Nov 9 Mon, Nov 12 Thu,
  Nov 15 Sun, Nov 16 Mon, Nov 17 Tue, Nov 19 Thu, Nov 20 Fri, Nov 21 Sat,
  Nov 22 Sun, Nov 23 Mon, Nov 24 Tue, Dec 2 Wed, Dec 6 Sun, Dec 31 Thu.
- Banned terms: Ucraina/Russia/Putin/Ukraine/Gaza/Trump/Netanyahu — 0 in `.text.md`.
- U+2019: 0 in all 8 SVGs and in `.text.md` (straight apostrophes only).
- P8 personal names: only "Ariosto" (Q67 note, standard spelling), "Giulia"/"Paolo"
  (fictional section-C characters, internally consistent), "Santa Cecilia" /
  "Madonna della Salute" (feast names), "Johannes Vermeer" (image credit, standard
  spelling). No non-Latin-script personal name in the P8 notes.
- §1.1: paper #fbfaf6 present; no gold/brick/near-black; VOL.4 ×9, VOL.5 only in
  the 3 legitimate nodes (P2 cross-reference, P7 disclosure, P7 next-week preview);
  badge colours A2/B1/B2 present; no double outer frame (0 full-page rects);
  Newsreader for Latin text; no double outer frame.
- KIT §1 three SHA-256 values verified against the files on disk (see Identity).
- Web PDF: real text layer (pdftotext 109,236 bytes, identical to print), web P1
  and P8 rendered and viewed — identical to print, no tofu; the D-1/D-2/D-3
  overflows are visible in the web render too (same SVGs).

## Mechanical gates (detail in GATE-LOG.md)

run.py RC=0 / TOTAL 150 / 0 overflow · SVG rebuild 8/8 byte-identical · print PDF
re-render byte-identical to delivered · freeze baseline 8/8 (canonical tool) ·
freeze diff 0 unexplained fragments (P1–P7; P8 covered by p8 compare + 150-key
audit) · freeze strict-CJK: added CJK only 13 × U+3000 (furniture separators) ·
occlusion 0 flags (selftest OK) · cream-box PIL true-ink scan: 3 flags (D-1/D-2/D-3
above) out of 29 cream rects · spill: 0 flags (no ink outside the page or in the
footer band) · orphan scan: 3 flags, all core-identical (O-10) · p8 extract
150/150 · p8 compare CLEAN, keydiff [137, 138, 139] (expected re-aimed keys;
Q140's key is the Italian sentence in both, so no diff — correct) · P8 min font
13.0 px = 9.75 pt · print/web text multiset identical (7934 words each, chars
equal) · web PDF 1,291,182 bytes < 7 MB · textmd validate forward-miss 0 /
reverse-miss 0 · 8/8 pages viewed from a fresh render of the delivered print PDF
+ web P1/P8 viewed · gates.py copy re-run by me: 20 PASS, 0 FAIL
("GATES ALL PASS" — the builder's 20 gates do not cover cream-box title overflow,
which is why this note reports (b) despite the green gates).
