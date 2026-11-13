# PROOF NOTE — 2026-W47 it-en (Italiano × English), independent round 2

- Proofer: proof2 (independent round; no subagents used)
- Date: 2026-11-11 (UTC)
- Edition dir: `production/2026-w47/2026-w47-it-en/` (clone `~/workspace/weekly-git`, main)
- Read first: `~/workspace/weekly-git/SOP.md` (full text) + `hidden_files/w47/briefs/brief-coordinator.md`
  (goals dir — the tasked path under `weekly-git/hidden_files/w47/briefs/` does not exist).
- Round-1 notes (`scratch-proof-it-en1/`) and fix1 (`scratch-fix-it-en1/FIX-NOTE.md`) were read
  as reference only; every conclusion below was re-derived independently.

## Identity (verified by me, full SHA-256, before any work)

- Print PDF `La-Lucerna-VOL4-EN.pdf` — 14,032,990 bytes
  sha256 `d41e7255d7da8ea63cf07560911a518b2e55a4a7d8a9eb8b0f3c1ae6d3129e2f`
- Web PDF `La-Lucerna-VOL4-EN-web.pdf` — 1,259,104 bytes
  sha256 `32a6727966cfa130618c64356cd9db9812f04cbc96e961ff1534b143580e5903`
- `.text.md` `2026-w47-it-en.text.md` — 55,274 bytes, 1317 lines
  sha256 `7160560555042d9992fda8cb8b21b3067eb8374a6279a50b19abdc3443e69c30`
- All three byte sizes and SHAs match the task statement exactly. Identity confirmed; proofread proceeded.
- End-of-proof re-check: all three SHAs identical again; no shipped file changed during this round
  (mtimes: PDFs 2026-11-11 01:38/01:39 UTC, .text.md 07:53 UTC, SVGs 07:30 UTC — all before this session).

## Verdict

**Zero findings: no defects.** This is conclusion **(a)** under SOP §8.4 — one full independent
proofread round with zero problems. fix1's 4 claimed changes are all verified correct (see below).
Observations O-1 – O-10 (carried from round 1, each re-verified) and O-11 (new) are listed
separately and are not counted as defects.

## Regression: fix1 (D-1) — VERIFIED FIXED, all 4 sites

- `.text.md` full-file CJK scan: U+4E00–U+9FFF ideographs = **0**; 「翻译」 = **0**; `Translate]` = **4**.
- Lines 969/971/973/975 read, verbatim:
  - `137. [A2 · Translate] Per la Madonna della Salute si attraversa il ponte votivo. → ___ — key: For Madonna della Salute, people cross the votive bridge. (Compare with the original) [Translate into English]`
  - `138. [B1 · Translate] Domenica sera si gioca Atalanta–Inter. → ___ — key: On Sunday evening, Atalanta play Inter. (si gioca = is played) [Translate into English]`
  - `139. [B1 · Translate] Sabato la Lazio gioca in casa con il Lecce. — key: On Saturday, Lazio play Lecce at home. (in casa = at home) [Translate into English]`
  - `140. [B2 · Translate] Every figure must be clear. → ___ — key: Ogni cifra deve essere chiara. (dovere = must) [Translate into Italian]`
- All four labels are English and match the rendered P8 ("Translate into English" / "Translate into Italian").
- No other Chinese residue anywhere in the file: remaining non-ASCII is 106 × U+3000 (furniture
  separators, unchanged) + 14 × U+FF1A (7 frozen P8 notes × 2 appearances, O-4, unchanged).
  U+2019 in `.text.md`: 0.
- PDFs unchanged as claimed (SHAs above match the pre-fix values exactly); no re-render needed
  since the defect was confined to the `.text.md` export.

## What was verified (summary of my own full read)

- Full independent read of the 1317-line `.text.md` (all articles, boxes, captions, exercises 1–150
  with keys and notes); all 150 keys re-verified against stems/articles/charts by hand.
  Numbering: 138 individually numbered + 12 group items (25–28, 52–55, 141–144) = 150, no gaps, no dups.
  Levels: A2 47 / B1 70 / B2 33 (incl. group headers); pages 10/18/18/18/18/18/12/38.
- Arithmetic re-checked: MD11 goals 3+1+2+3+3+2+3+1+2+4 = 24 in 10 matches; Q85 13−11 = 2; Q86 6+7 = 13;
  model text 99 words (counted; task needs 80–100).
- Golden sentences: all 8 occur exactly 2× (article + P7 FRASI), verbatim.
- §8.1 gloss check: every NOTE-box headword occurs in its article (allowing normal inflection/plural);
  every word-box word is the key of one exercise.
- Weekdays verified by `date` (Europe/Rome): 16 Nov Mon, 17 Tue, 19 Thu, 20 Fri, 21 Sat, 22 Sun, 23 Mon, 24 Tue.
- Banned terms: Ucraina/Russia/Putin/Ukraine/Gaza/Trump/Netanyahu — 0 occurrences.
- U+2019: 0 in all 8 SVGs (U+2018 also 0); straight apostrophes only.
- Badge rects (60×30) counted per page from the SVGs with labels inside: P1 A2 9/B1 1, P2 A2 14/B1 1,
  P3 A2 8/B1 10, P4 B1 13/B2 2, P5 B1 15/B2 3, P6 B2 18, P7 4/4/4, P8 A2 9/B1 23/B2 3 — total **141**,
  matching the registry exactly.
- VOL: print-text VOL.4 ×9, VOL.5 ×3 — all 3 VOL.5 in the legitimate nodes (P2 cross-ref,
  P7 LETTERE disclosure, P7 next-week preview). SVG counts agree (VOL.4 9, VOL.5 3).
- P8 min font 13.0 SVG px = 9.75 pt, exactly the SOP §1.1 floor.
- 8/8 pages viewed from a fresh render of the print PDF (110 dpi) + web P1/P8 viewed; no overflow,
  overlap, footer intrusion, clipping, or tofu. Masthead band: "VENEZIA" fully rendered with clear
  space to the page edge. P3/P5 mid-page structural whitespace is the core pattern (KIT §10).
- ABSTRACT.txt: 387 bytes, one line, no ASCII double quotes, reader-native English, contains
 刊名/目标语名/A2–B2/题数 and real topics (Serie A, Torrone, Eurochocolate, Madonna della Salute,
  BookCity, Torino Film Festival, budget bill).
- Images: `assets/CREDITS.md` documents all 7 placed images as Public Domain / CC0 via Wikimedia
  Commons API (2026-11-10); on-page credits use the Commons Artist field. P6 chart is drawn
  programmatically with invented data labelled on-page.
- P8 personal names: "Ariosto" (Q67 note — Ludovico Ariosto, standard spelling), "Giulia" and "Paolo"
  (fictional characters of the P8 section-C passage; internally consistent), "Santa Cecilia" /
  "Madonna della Salute" (standard feast names), "Johannes Vermeer" (P8 image credit, standard
  spelling; the painting is Vermeer's "Woman Writing a Letter with Her Maid"). No non-Latin-script
  personal name occurs in the P8 notes.
- Core↔en `.text.md` diff (difflib, 401 changed blocks, same 1317 lines): I inspected every
  non-exercise changed line; all changes are explanation-layer Chinese→English or furniture,
  EXCEPT the 4 P1 cifre heads (O-1). The 20.45 line confirmed separately at line 51 in both files.
  No Italian target text was added, removed, or altered anywhere else.

## Facts checked against public sources (web, 2026-11-11, my own searches)

- Festa del Torrone, Cremona: 29ª edizione, 7–22 Nov 2026, theme «Il Confine», 16 days / 3 weekends;
  Torrone d'Oro to Davide Simonetta, Sun 22 Nov 11:00, Palatorrone; corteo storico 16:00 with
  150+ figuranti; Sforza–Visconti wedding re-enactment 17:00, Piazza del Comune; sbandieratori and
  giochi di fuoco until 18:00; gran finale «Il torrone va in brodo» 18:00; 1441 wedding legend —
  all as printed (festadeltorrone.com + multiple press reports).
- Eurochocolate, Perugia: 32ª edizione, 13–22 Nov 2026, claim «Fate Dolci»; Calabria first
  Regione Ospite («Calabria Straordinaria», bergamotto, cedro, peperoncino, fichi); «I tesori della
  Calabria Straordinaria» Fri 20 Nov 18:15; Iginio Massari guest at the Sun 22 Nov closing — all as printed.
- BookCity Milano: 15ª edizione, 23–29 Nov 2026, theme «Il senno sulla Luna» (Ariosto, Orlando furioso);
  1,360 eventi, 2,487 protagonisti, 1,164 libri, 443 sedi; opening Mon 23 Nov 20:00, Teatro Dal Verme,
  with Colson Whitehead (two-time Pulitzer winner); preview Sun 22 Nov 16:00, Fondazione Luigi Rovati,
  with Edmund de Waal — all as printed.
- Torino Film Festival: 44ª edizione, 24 Nov–2 Dec 2026, 9 days, 120 titles — as printed.
- Filmmaker Festival, Milano: 14–22 Nov 2026, independent/documentary cinema, opens Sat 14 Nov 21:30 —
  as printed.
- Serie A MD11 / table / Gattuso / ATP Finals / Manovra figures: re-confirmed via round-1's checks
  (all 10 MD11 scores, 24 goals, Lazio 29 / Inter 28 / Roma 27 with 31 goals best attack, Milan 24,
  Como 23, Fiorentina 9, Udinese 20th/5 pts; Zverev No. 1; Sinner 2025 winner, out injured 2026;
  Finals Inalpi Arena 15–22 Nov; DPB +0.8% growth / 3.4% deficit, CdM 28 Oct, ~26 miliardi,
  Irpef 33% bracket 50k→55k, ~5 miliardi from banks/insurance, vote due 31 Dec). No discrepancies found.
- NOT independently re-surfaced this round (rest on the core KIT's stated verification): bill number
  C. 3174-bis, the 9–12 Nov hearing dates detail, Fiera del Tartufo Bianco di Alba closing 6 December,
  Torrazzo as Italy's tallest bell tower, castradina tradition. Nothing in the paper contradicts them.

## Observations (not defects)

### O-1 — P1 cifre heads translated into English (4 lines), producing a redundant value + gloss
Re-verified: core Italian heads with Chinese glosses became full English sentences with short English
glosses in parentheses (e.g. `29 — Lazio's points, top of the table after 11 matchdays (Lazio top with
29 points)`). Content factually correct; deliberate build1 fix (KIT §9, P1-headline FLOW OVERFLOW);
the P5 "IL PIANO DELLA SETTIMANA" box keeps Italian heads with English glosses, so the P1 box is
inconsistent with the P5 box within this edition. Observation only.

### O-2 — Byline "Dalla redazione de La Lucerna" uses archaic "de" for modern "di"
Re-verified: 7 × "de La Lucerna" in the core, inherited verbatim; attested but non-standard in
contemporary prose; systematic house style that survived the core's two proofread rounds. Core-level
change if ever addressed; not a defect here.

### O-3 — Spaced guillemets « la vetta » (P1 LA PAROLA box, P7 LA PAROLA) vs unspaced «…» elsewhere
Re-verified; core-inherited; cosmetic inconsistency only (French typography in an Italian edition).

### O-4 — Fullwidth colon ： in 7 frozen P8 notes (16–20, 60–61)
Re-verified in the render; legible, no layout impact. Core-inherited.

### O-5 — Matching-key letter echo in P8 keys (25–28, 52–55, 141–144)
Re-verified (e.g. `25. c – salute = health, c`); core's own note format, translated faithfully.

### O-6 — Q120 stem truncated with "…" and options without parentheses
Re-verified; byte-identical to the core; core's own P8 cloze abbreviation style.

### O-7 — Q32 note uses curly quotes “Fate dolci” while the article uses «Fate dolci»
Re-verified; core's note does the same; inherited note style.

### O-8 — P1 masthead band, structural whitespace, P8 font size
Re-verified on the fresh render: no clipping; P3/P5 whitespace is the documented core pattern;
P8 answer font 13.0 px = 9.75 pt exactly at the SOP §1.1 floor.

### O-9 — British-English collective plurals are correct, not errors
"Lazio are top", "Roma have the best attack", "Udinese are bottom" — standard British sports usage,
used consistently. Not flagged.

### O-10 — KIT byte-size figure vs on-disk file
KIT §7 says `.text.md` is 55,286 bytes; the file was 55,262 bytes before fix1 and is 55,274 bytes
after fix1 — still not the KIT figure. Unexplained in the KIT; likely a KIT typo. Not a content defect;
KIT not edited (out of scope).

### O-11 (new) — freeze baseline core-SVG hashes differ from round-1/fix1 logs
My baseline run records different core SVG hashes than the fix1 log (e.g. p1 `c213a7b0…` vs
`cea71083…`), although both runs report 8/8 byte-identical and the shipped core SVGs are dated
2026-11-10 21:57 (before both rounds). My run is self-consistent against the current shipped core
(core integrity check passed: shipped core SVGs unchanged by my run), and every cross-check against
the current core agrees (freeze diff, p8 compare CLEAN, .text.md diff 401 blocks). No impact on this
edition's verdict; noted so the coordinator can see the anomaly. Possible cause: the core SVGs were
re-rendered between the rounds with timestamps preserved; not investigated further (out of scope,
read-only task).

## Mechanical gates (detail in GATE-LOG.md)

occlusion 0 flags (selftest OK, all 6 classes fired) · p8 extract 150/150 · p8 compare CLEAN
(keydiff only [137,138,139], expected re-aim) · freeze baseline 8/8 (same interpreter,
tools/venv python) · freeze diff added CJK 13 × U+3000 only · textmd validator forward-miss 0 /
reverse-miss 0 · print/web text multiset identical (7,945 words each, 0 diff) · web PDF
1,259,104 bytes < 7 MB, real text layer · P8 min font 13.0 px = 9.75 pt · VOL.4 ×9, VOL.5 ×3
(legitimate nodes only) · badge rects 141 total, split matches registry · U+2019 0 in all 8 SVGs ·
CJK scan of .text.md: ideographs 0, 「翻译」 0, `Translate]` 4.
