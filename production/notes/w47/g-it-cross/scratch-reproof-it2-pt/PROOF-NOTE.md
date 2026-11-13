# PROOF NOTE — 2026-W47 it-pt (Italiano × Português), independent round 3 (re-fan-out 2, core D-2 fix)

- Proofer: independent reproof (no subagents used; different person from the re-fan-out 2 builder)
- Date: 2026-11-11 (UTC; work done ~21:58–22:15 UTC)
- Edition dir: `production/2026-w47/2026-w47-it-pt/` (clone `~/workspace/weekly-git`, main)
- Task: full independent re-proof of the re-fan-out-2 build from scratch (SOP §8.4).
  Nothing was taken on trust from proof2 (a) or from the re-fan-out-2 report
  (`hidden_files/w47/scratch-refanout-it2/FANOUT-REPORT-it2.md`); every item below
  was re-measured by me. Where proof2 / the reports are cited, it is only as a
  cross-check or a method reference.
- My scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it2-pt/`
- Probe: `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`, RC=0; scratch write verified (`probe.txt`).
  `TMPDIR=<scratch>/tmp` throughout; interpreter `~/workspace/weekly-git/tools/venv/bin/python` (Pillow 13.0.0);
  `PYTHONDONTWRITEBYTECODE=1` for all production-source imports. No `/tmp` writes. No production file written.

## Identity (verified by me, full SHA-256, on disk before any work)

- Print PDF `La-Lucerna-VOL4-PT.pdf` — 14,036,607 bytes
  sha256 `9910d536048ae4975c6e1657827f299abab0d274819f881b648a56d513b65135`
- Web PDF `La-Lucerna-VOL4-PT-web.pdf` — 1,294,373 bytes
  sha256 `f2e390f31fc30d14ff08803244cc66749abafd2acdeb41763ba3800fc5f0d85e`
- Text export `2026-w47-it-pt.text.md` — 55,718 bytes / 1317 lines
  sha256 `e01360ae9c401d014a9e0a51779646845a112aac4e8afe912090269c6ffa7302`
- All three SHA-256 values and byte sizes match the task brief, the re-fan-out-2
  report §1, and WEEKLY-KIT.md §7 exactly. Identity confirmed; proofread proceeded.
- ABSTRACT.txt: one line, Portuguese, 425 bytes, no ASCII double quotes, facts match
  the issue (Serie A 11.ª jornada, Lazio 29 pontos, Torrone + Eurochocolate
  encerram no domingo, Madonna della Salute, Dia das Árvores, BookCity, Festival
  de Cinema de Turim, projeto de orçamento; A2–B2, 150 exercícios).

## Verdict

**(a) ZERO DEFECTS — this edition is ready to finalize.** No defects found in the
full re-read, the D-2 regression audit, the 150-key three-source audit, or any
mechanical gate. Observations O-1 – O-10 are listed separately and are not counted
as defects.

## Regression A — D-2 fix, independently re-verified (all sub-items PASS)

Source of truth: `scratch-refanout-it2/FANOUT-REPORT-it2.md` §1/§3 + `scratch-refanout-it2/backup/`
(pre-refan-out production files) + `scratch-fix-core-it-d2/FIX-LOG.md`.

1. **New sentences in place**
   - `text.md:775`: `Per i piani della settimana usiamo il futuro semplice: andremo a Cremona, assaggeremo il torrone, guarderemo Atalanta–Inter. Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.` — exact.
   - `text.md:777`: `E per la settimana prossima: leggeremo a BookCity, che apre lunedì 23 novembre. Il verbo è leggere, regolare al futuro: leggerò.` — exact.
   - `content7.py:17/:18`: identical strings (grep, lines 17/18).
   - p7 SVG: both sentences present in the node sequence — L18 as one node
     (`verbo è leggere, regolare al futuro: leggerò.`); L17 split across nodes 7–13
     (`Atalanta–Inter. Le forme sono regolari:` / `assaggiare ` / `→` / ` ` /
     `assaggerò, guardare ` / `→` / `guarderò.`); space-stripped concatenation
     counts each ×1. (Node-boundary gluing `regolari:assaggiare` / `→guarderò` is
     the same arrow/line-join behaviour the re-fan-out report documents for the
     PDF text layer; the rendered P7, viewed at 200 dpi, shows both sentences
     cleanly with normal spacing.)
   - Print + web PDF, P7 text layer (whitespace/arrow-normalised PyMuPDF extraction):
     new L17 ×1, new L18 ×1 on page 7 of each PDF; ×1 whole-document each.
     (First un-normalised count returned 0 for both — the layer breaks the
     sentences across lines, e.g. `regolari:\nassaggiare →assaggerò, guardare→\nguarderò.`;
     after `\s*→\s*`→`→` + whitespace collapse the counts are 1/1. Method note, not a defect.)
2. **Old strings 0 in the live edition**
   - `Le forme sono regolari: andare`: 0 in content7.py, text.md, all 8 SVGs, both
     PDF text layers (whole-document, both normalisations).
   - `irregolare al futuro: leggerò`: 0 in the same set.
   - `andare` still occurs on P7 only inside Q101's stem `(andare)` and in the P7
     ERRORI TIPICI correction `Andare vuole essere, non avere.` — unrelated to the
     old string (full old string count is 0). The only other `Le forme sono regolari:
     andare` / `irregolare al futuro: leggerò` hits in the edition directory are
     inside `WEEKLY-KIT.md:93`, which quotes them as the D-2 history — documentation,
     not live content.
3. **Diff vs pre-refan-out production backup is P7-only**
   - `text.md`: exactly −21 bytes (55,739 → 55,718); `diff` shows exactly two changed
     lines, 775 and 777, nothing else.
   - SVG: p1–p6, p8 byte-identical to backup; only `svg/p7-lingua.svg` differs.
     Node-level diff of p7 (backup 168 nodes → new 162): exactly 4 opcodes, all
     inside the two D-2 sentences (replace `andare `→`assaggiare `; replace
     `andrò, assaggiare `→`assaggerò, guardare `; delete the 5 leftover fragments of
     the old L17; replace `irregolare`→`regolare` nodes in L18).
   - cards: p1–p6, p8 byte-identical; only `cards/p7-lingua.png` differs.
   - content: only `content7.py` differs (lines 17/18); content12/34/56/8, run.py,
     render.py, bslib4.py, svglib.py byte-identical to backup.
   - Both PDFs changed (P7 rebuilt) — expected.

## Regression B — P7 teaching semantics, read sentence by sentence (D-2 lesson)

- `Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.` — CORRECT.
  assaggiare and guardare are regular -are verbs; assaggerò / guarderò are the
  regular futuro semplice formations (stem + -ò). No irregular verb is now cited
  as a regular example.
- `Il verbo è leggere, regolare al futuro: leggerò.` — CORRECT. leggere is regular
  in the futuro semplice (leggerò = infinitive minus -e + -ò). Its irregularity is
  in the passato remoto (lessi) and past participle (letto), not the future.
- The first sentence of the paragraph (`andremo a Cremona, assaggeremo il torrone,
  guarderemo Atalanta–Inter`) makes no regularity claim about andremo — correct,
  since andare → andrò is irregular (stem andr-). The bridge sentence
  `Fala de planos no futuro: andremo, assaggeremo, guarderemo, leggeremo.` is intact.
- Q101–104 keys unchanged by the fix (andremo / assaggeremo / guarderemo / B),
  confirmed by the three-source key audit below and by p8 compare vs the core
  (keydiff does not include 101–104). Q104's note (`leggerò é o futuro de leggere`)
  makes no regularity claim.

## What was verified (summary)

- Full independent read of the 1317-line `.text.md` (all articles, boxes, captions,
  exercises 1–150 with keys and notes); all 150 keys re-verified against stems/
  articles/charts by hand, plus the gates.py 150-key audit vs the core `.text.md`
  (keys match except re-aimed 137–139 and the writing item; notes match
  translations.py except 137–140 + writing), plus a third-source check: SVG-printed
  P8 keys vs `.text.md` RISPOSTE — 149/150 key-parts exact, the one difference being
  Q150, whose printed "key" is the ✓ marker by design (the printed key strings carry
  no note suffix; every key part matched, zero "key differ" entries).
- Level/page distribution: TOTAL 150; A2 47 / B1 70 / B2 33 (range items 25–28,
  52–55, 141–144 counted as 4/4/4 — my bracket-tag regex gives 44/67/30 because each
  range stem carries one tag); pages 10/18/18/18/18/18/12/38 (Q ranges 1–10, 11–28,
  29–46, 47–64, 65–82, 83–100, 101–112, 113–150) — matches KIT. Model text counted:
  99 words (range 80–100).
- Arithmetic re-computed: MD11 goals 3+1+2+3+3+2+3+1+2+4 = 24 in 10 matches;
  Q85 13−11 = 2; Q86 6+7 = 13; classifica Lazio 29 / Inter 28 / Roma 27 /
  Milan 24 / Como 23 / Udinese 5 (20th) — consistent across P1, P4 table and keys;
  Torrone Nov 7–22 = 16 days / 3 weekends; Torino FF Nov 24–Dec 2 = 9 days;
  BookCity Nov 23–29 = 7 days; P6 chart bars exactly proportional at 34 px/degree
  (5°→170, 6°→204, 7°→238, 11°→374, 13°→442, measured from SVG rect widths).
- Golden sentences: all 8 verified verbatim, exactly 2 occurrences each in
  `.text.md` (article + P7 FRASI); freeze diff shows 0 unexplained fragments.
- §8.1 gloss check: all 32 parsed NOTE-box headwords occur in their articles
  (with normal inflection, e.g. "imbattuta" for "imbattuto", "candele" for "candela",
  "figuranti" for "figurante", "protagonisti" for "protagonista", "sedi" for "sede").
  (Proof2 counted 33; my parse yields 32 — same 0 missing; the difference is only
  how `il figurante, figurante` / elided forms are counted.)
- Dates/weekdays (Europe/Rome `date`, all match the paper): Nov 6 Fri, Nov 9 Mon,
  Nov 12 Thu, Nov 15 Sun, Nov 16 Mon, Nov 17 Tue, Nov 19 Thu, Nov 20 Fri,
  Nov 21 Sat, Nov 22 Sun, Nov 23 Mon, Nov 24 Tue, Dec 2 Wed, Dec 6 Sun, Dec 31 Thu.
- Facts re-checked against public sources by me (web, 2026-11-11):
  - Sinner won the 2025 ATP Finals — beat Alcaraz 7–6(4), 7–5 in Turin, Nov 16,
    2025, retained the title (ATP Tour match report; AP) — "vincitore del 2025" is correct.
  - Torino Film Festival 2026 = **44ª edizione**, Tue Nov 24 – Wed Dec 2, 2026,
    9 days — confirmed by the official site (torinofilmfest.org) and the FIAPF
    regulation text.
  - BookCity Milano 2026 = **15ª edizione**, Nov 23–29, theme «Il senno sulla
    Luna» from Ariosto's *Orlando furioso* (IULM; World Today Journal) — confirmed.
  - Eurochocolate 32ª edizione and Festa del Torrone 29ª edizione: proof1's and
    it-en proof2's web verifications stand (not re-litigated here). Manovra facts
    (DPB Oct 15; bill C. 3174-bis; hearings Nov 9–12; amendments deadline Nov 17
    18:00) rest on the core KIT's stated independent verification, as in proof1.
  - Scenario premises, not re-verified (core-level, set in the 2026–27 season
    frame): the MD11 scores / standings themselves, Zverev as 2026 world No. 1,
    Sinner out injured in 2026, Frosinone in Serie A.
- Banned terms: Ucraina/Russia/Putin/Ukraine/Gaza/Trump/Netanyahu — 0 in `.text.md`.
- U+2019: 0 in all 8 SVGs and in `.text.md` (straight apostrophes only).
- U+FF1A: 14 in `.text.md` (7 in the P8 key list + 7 in the exercise list), 7 in the
  P8 SVG, 0 in P1–P7 SVGs — identical counts in the backup build (O-4, inherited).
- P8 personal names: only "Ariosto" (Q67 note, standard spelling), "Giulia"/"Paolo"
  (fictional section-C characters, internally consistent), "Santa Cecilia" /
  "Madonna della Salute" (feast names), "Johannes Vermeer" (image credit, standard
  spelling), "Gattuso" (Lazio coach, in the P7 quote and P4 article). No non-Latin-script
  personal name in the P8 notes.
- §1.1: paper #fbfaf6 present; no gold/brick/near-black; VOL.4 ×9, VOL.5 only in
  the 3 legitimate nodes (P2 cross-reference, P7 disclosure, P7 next-week preview);
  badge colours A2/B1/B2 present; no double outer frame (0 full-page rects);
  Newsreader for Latin text.
- KIT §7 three SHA-256 values + sizes verified against the files on disk (see Identity);
  KIT "45,787 text bytes" matches plain `pdftotext` output for both PDFs (45,787 bytes
  each; `-layout` gives 106,585 for print).
- Web PDF: real text layer (pdftotext 105,156 bytes with -layout), web P1 and P8
  rendered and viewed — identical to print, no tofu. Print/web text multiset
  identical (7,962 words each; down 3 from proof2's 7,965, exactly the D-2 deletion).
- E-section labels on `.text.md` lines 969/971/973/975 read `[A2 · Traduzir]`,
  `[B1 · Traduzir]` ×2, `[B2 · Traduzir]`; keys 137–139 are Portuguese re-aimed
  reader sentences, verified correct Portuguese translations of the Italian stems;
  key 140 is the Italian sentence "Ogni cifra deve essere chiara." in BOTH the core
  and this edition — so `p8.py compare` keydiff is [137, 138, 139] with no diff on
  140, which is the CORRECT behaviour (stem direction reverses there).
  English function-word scan of the whole `.text.md`: **0 hits**. SVG text nodes:
  **0 CJK ideographs** on all 8 pages.
- P8-keys flow ends col 3 y=2529 (bottom 2552) per the builder's log; P7 col 3 content
  ends 1667.92 (baseline; builder log 1673.0 incl. line height), P4 col 3 ends
  1135.91 (builder log 1140.45) — all inside the page.

## Defects

None.

## Box titles — STRADDLE rule adjudication (re-measured, with backup对照)

- All 38 bold ≥21 px box titles inside cream rects were raster-measured one by one
  on the 96 dpi render of the DELIVERED print PDF (x-window restricted to the
  title's own column) and cross-checked with PIL true ink (`raster_titles2.py`,
  log `raster-titles2.log`). Result: **37 fit, 1 apparent overflow — adjudicated NOT
  an overflow** (see below).
  - P1 `LA SETTIMANA IN CIFRE　DADOS`: PIL ink 556.5..924.5 vs box 538.5..961.0
    → **fits by 36.5 px** (raster 923, −38.0).
  - P2 `LA FRASE PER RICORDARE　LEMA`: PIL ink ..934.0 vs box ..961.0
    → **fits by 27.0 px** (raster 934, −27.0).
  - P7 `ERRORI TIPICI　ERROS`: PIL ink ..1721.5 vs box ..1862.0
    → **fits by 140.5 px** (raster 1719, −143.0).
  - Tightest title in the edition: P7 `LA PAROLA　PALAVRA DA SEMANA`,
    PIL ink ..1845.0 vs box ..1862.0 → fits by 17.0 px (raster 1847, −15.0).
  - Next tightest: P4 `LA CLASSIFICA　DOPO 11 GIORNATE`, fits by 29.0 px;
    P1 `IN QUESTO NUMERO　ÍNDICE`, fits by 53.8 px.
- The one raster "OVERFLOW" (P6 `MINIME DI ESEMPIO　gradi, dati inventati`,
  raster right 1110 vs box right 961) is a measurement artefact, adjudicated under
  the STRADDLE rule: the title's own PIL true ink ends at **538.2** (422.8 px spare);
  the raster band (same baseline y=1634) also catches the neighbouring twin box's
  title `PROPOSTA ≠ LEGGE`, which starts at x=1011 on the SAME baseline. The title
  node is byte-identical to the backup (`x="110.0" y="1634"`, same text, same box
  rect `x="88" width="873"`; `svg/p6-approfondimento.svg` is byte-identical to the
  backup file). **Backup对照 (run as required before judging):** the backup print
  PDF's P6 rendered at 96 dpi gives the identical ink reading in the same band
  (x-range 112..1222; left-box rightmost ink 538 in BOTH versions) — zero change,
  so no regression is possible. No glyph clipped, no ink overlapping any other
  object, no visible border (borderless cream) — **none of the three STRADDLE
  defect conditions holds**. Crop evidence: visual P6 at 200 dpi (`pages/p-6.png`,
  both boxes visible, gutter between them, chart bars inside the MINIME box).
- The cream-box PIL true-ink scan over all 29 cream rects
  (`cream_spill_orphan.py`, log `cream-spill-orphan.log`) found **0 CREAM-X and
  0 CREAM-Y flags**; spill: 0 flags (no ink outside 1950×2700, no ink below y=2580
  outside furniture).

## Observations (not defects)

### O-1 — P1 cifre heads in Portuguese, redundant value + gloss
As in proof2 (O-1): `29 — os pontos da Lazio, primeira após 11 jornadas (a Lazio lidera)`.
Content factually correct; deliberate build1 fix. Inconsistent with the P5
"IL PIANO DELLA SETTIMANA" box, which keeps Italian heads with Portuguese glosses.
Not counted: correct text, documented engineering choice.

### O-2 — Byline "Dalla redazione de La Lucerna" uses archaic "de" for modern "di"
Still present (7 × "de La Lucerna", core-inherited, systematic house style).
Not counted: attested archaic form, survived two core proof rounds, core-level fix.

### O-3 — Spaced guillemets « la vetta » (P1 LA PAROLA box, P7 LA PAROLA) vs unspaced «…» elsewhere
Still present (2 × `« la vetta » :`, French typography). Core-inherited cosmetic
inconsistency.

### O-4 — Fullwidth colon ： in 7 frozen P8 notes (16–20, 60–61)
Still present (14 × U+FF1A in `.text.md`, 7 in the P8 key list + 7 in the exercise
list; 7 in the P8 SVG). Core-inherited, legible, no layout impact (P8-keys flow ends 2529/2552).

### O-5 — Matching-key letter echo in P8 keys (25–28, 52–55, 141–144)
Still present (e.g. `25. c — salute = a saúde, c`). Core note format, translated
faithfully. Redundant but consistent.

### O-6 — Q120 stem truncated with "…" and options without parentheses
Still present, byte-identical to the core (P8 SVG: `Il Torino Film Festival apre...
A. il 20 novembre · B. il 24`). Core's P8 cloze abbreviation style.

### O-7 — CORRECTED (proof2's O-7 was a misread, not a live item)
Proof2 reported "Q32 note uses curly quotes “Fate dolci”". Re-measured in THIS
build and in the backup: U+201C/U+201D count is **0** in `text.md` and in **all 8
SVGs** (both builds). Every "Fate dolci" occurrence uses «Fate dolci» (article P3,
Q32 stem, RISPOSTE line 32). There is no curly-quote inconsistency to carry forward.
Recorded here so the next round does not re-litigate it.

### O-8 — Masthead band, structural whitespace, P8 font size
Masthead band first node at x=0.0 — flush with the left page edge (same as es).
The initial "S" and final "A" of "VENEZIA" are fully rendered on the delivered P1
(viewed at 200 dpi); no glyph clipped. P3/P5 mid-page structural whitespace is the
core pattern (documented in KIT §10). P8 answer font 13.0 SVG px
= 9.75 pt, exactly at the SOP §1.1 floor.

### O-9 — Orphan scan: 3 flags, all byte-identical to the core (inherited, not defects)
My orphan scan flagged: P6 main text last line "18." alone (LA STRADA DELLA
MANOVRA entry "…alle ore / 18.", node `<text x="1603.5" y="641.6">18.</text>`,
identical in core); P8 Q129 stem last line "due" alone (node
`<text x="538.5" y="818.975">due</text>`, identical in core); P8 Q137 stem blank
"___" alone on line 2 (node `<text x="773.3" y="1187.825">___</text>`, identical in
core — the `___` node text is byte-identical in both SVGs; 8 such nodes in each).
Frozen Italian text, same column widths, same wraps. Not defects; noted for the record.
Render evidence: `pages/p-6.png`, `pages/p-8.png`.

### O-10 — First un-normalised PDF text-layer count returned 0 for the D-2 sentences
The P7 text layer breaks the two D-2 sentences across lines and glues `→` to the
neighbouring word (`regolari:\nassaggiare →assaggerò, guardare→\nguarderò.`).
A naive exact-string search on the raw layer finds neither sentence; the
whitespace/arrow-normalised search finds each ×1. This is a property of the text
layer, not of the content — but any future text-layer check on these sentences must
use the normalisation, or it will false-alarm. Noted as a method trap, not a defect.

## Mechanical gates (detail in GATE-LOG.md)

gates.py re-run by me: **20 PASS, 0 FAIL ("GATES ALL PASS")** · core freeze baseline
8/8 (build-copy verified as core-it itself: contains `2026-w47-it-zh-cn.text.md`,
D-2 string in content7.py, p7 hash `a7e6afa4…` matching FIX-LOG) · edition freeze
baseline 8/8 · occlusion selftest OK + production 0 flags · p8 extract 150/150 ·
p8 compare CLEAN, keydiff [137, 138, 139] · freeze diff 0 unexplained fragments
(P1–P7; P8 covered by p8 compare + 150-key audit) · freeze strict-CJK: added CJK
only 8 × U+3000 (furniture separators) · print/web text multiset identical
(7,962 words each) · web PDF 1,294,373 bytes < 7 MB · textmd validate
forward-miss 0 / reverse-miss 0 · 8/8 pages viewed from a fresh 200 dpi render of
the delivered print PDF + web P1/P8 viewed · print PDF re-rendered from the shipped
SVGs byte-identical to delivered · production untouched (41 files re-hashed before
and after, identical); no commit, no push, no production file written.
