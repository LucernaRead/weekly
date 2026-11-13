# PROOF NOTE — 2026-W47 it-pt (Italiano × Português), independent round 2 (re-fan-out)

- Proofer: independent proof2 (no subagents used)
- Date: 2026-11-11 (UTC; work done 20:36–20:53 UTC)
- Edition dir: `production/2026-w47/2026-w47-it-pt/` (clone `~/workspace/weekly-git`, main)
- Task: full re-proof of the re-fan-out build from scratch (SOP §8.4). Nothing was
  taken on trust from proof1 or from the re-fan-out report
  (`hidden_files/w47/scratch-refanout-it/FANOUT-REPORT-it.md`); every item below
  was re-measured by me. Where proof1 / the it-en proof2 are cited, it is only as
  a cross-check or a method reference.
- My scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-it-pt1/`

## Identity (verified by me, full SHA-256)

- Print PDF `La-Lucerna-VOL4-PT.pdf` — 14,036,628 bytes
  sha256 `6f74ee92c72d4ca545fb763c268231b05b6970a5e170b943cdc2882a3ce4a477`
- Web PDF `La-Lucerna-VOL4-PT-web.pdf` — 1,294,408 bytes
  sha256 `f28a563544bcac8998097fc418c94b47f92a650b351518339c9be864a1ada1c4`
- Text export `2026-w47-it-pt.text.md` — 55,739 bytes / 1317 lines
  sha256 `2ce7bfe9bb1f58d72b6249c4a2d2cd2bf5d97e028e10d2e3acfc480797627cb8`
- All three SHA-256 values and byte sizes match the task brief and WEEKLY-KIT.md §7
  exactly. Identity confirmed; proofread proceeded.
- ABSTRACT.txt: one line, Portuguese, no ASCII double quotes, facts match the issue
  (411 chars: Serie A 11.ª jornada, Lazio 29 pontos, Torrone + Eurochocolate
  encerram no domingo, Madonna della Salute, Dia das Árvores, BookCity, Festival
  de Cinema de Turim, projeto de orçamento; A2–B2, 150 exercícios).

## Verdict

**(a) ZERO DEFECTS — this edition is ready to finalize.** No defects found in the
full re-read, the 150-key three-source audit, or any mechanical gate. Observations
O-1 – O-9 are listed separately and are not counted as defects.

Why this round differs from it-en proof2: the pt gloss titles are SHORT
(`DADOS`, `LEMA`, `ERROS`, `PALAVRA DA SEMANA`) where the English ones were long
(`THIS WEEK IN NUMBERS`, `REMEMBER`, `COMMON MISTAKES`). The en defect class
(gloss-box title overflow) does not occur here — every pt box title was measured
twice (PIL true ink + raster pixels on the delivered print render) and fits inside
its cream box, the tightest with 17.0 px spare (P7 `LA PAROLA　PALAVRA DA SEMANA`).
The builder's 20/20 gates are corroborated independently by this round, including
the cream-box scan the gates do not cover.

## Defects

None.

## Re-fan-out §7 unresolved items — adjudicated by measurement

The task brief pointed at two items from the re-fan-out report §7 as prompts for
this round ("英文源 key 未改" and the bilingual small-file title STRADDLE). For the
record: the report file I read (`scratch-refanout-it/FANOUT-REPORT-it.md`) has §7
"Backup" and contains no literal item worded either way (grep for
STRADDLE / 未改 / 英文源 / 未决 / TODO / FIXME: 0 hits; `check-pt.json`:
`{"lang": "pt", "fails": []}`). I therefore treated both as measurement prompts
and adjudicated them from the edition itself:

### U-1 — "English-source key unchanged": RESOLVED, no defect

- No English key or note remains anywhere in this edition. E-section labels on
  `.text.md` lines 969/971/973/975 read `[A2 · Traduzir]`, `[B1 · Traduzir]` ×2,
  `[B2 · Traduzir]` (the 「翻譯」 residue the first fan-out carried is gone).
- Keys 137–139 are Portuguese re-aimed reader sentences
  ("Para a Madonna della Salute, as pessoas atravessam a ponte votiva.";
  "No domingo à noite, a Atalanta joga contra o Inter.";
  "No sábado, a Lazio joga em casa contra o Lecce.") — verified correct Portuguese
  translations of the Italian stems.
- Key 140 is the Italian sentence "Ogni cifra deve essere chiara." in BOTH the
  core and this edition (core-it `.text.md:1297`, same line) — so `p8.py compare`
  keydiff is [137, 138, 139] with no diff on 140, which is the CORRECT behaviour,
  not an omission (see "Mechanical gates" below). The stem direction reverses
  there (Portuguese stem → Italian key, "Traduzir para italiano").
- English function-word scan of the whole `.text.md` (" the ", " and ",
  " Sunday ", " people ", " bridge ", " evening ", " against ", …): **0 hits**.
  SVG text nodes: **0 CJK ideographs** on all 8 pages (the 3 CJK chars on P1 sit
  only inside the moth-logo `<title>Lucerna 三色蛾</title>` metadata, as in the core).

### U-2 — Bilingual small-file (box) titles, STRADDLE rule: RESOLVED, no defect

- All 38 bold ≥21 px box titles inside cream rects were raster-measured one by one
  on the 96 dpi render of the DELIVERED print PDF (x-window restricted to the
  title's own column so neighbouring columns cannot pollute the reading) and
  cross-checked with PIL true ink (`raster_titles2.py`, log `raster-titles2.log`).
  Result: **37 fit, 1 apparent overflow — adjudicated NOT an overflow** (see below).
  The three en-analogue titles, the exact class it-en proof2 found defective:
  - P1 `LA SETTIMANA IN CIFRE　DADOS`: PIL ink 556.5..924.5 vs box 538.5..961.0
    → **fits by 36.5 px** (raster 922, −39.0). Crop: `pages/crop-p1-cifre.png`.
    Contrast en: ink to 1118.0, +157 px over.
  - P2 `LA FRASE PER RICORDARE　LEMA`: PIL ink ..934.0 vs box ..961.0
    → **fits by 27.0 px** (raster 933, −28.0). Crop: `pages/crop-p2-frase.png`.
    Contrast en: ink to 1000.8, +39.8 px over.
  - P7 `ERRORI TIPICI　ERROS`: PIL ink ..1721.5 vs box ..1862.0
    → **fits by 140.5 px** (raster 1719, −143.0). Crop: `pages/crop-p7-errori.png`.
    Contrast en: ink to 1868.5, +6.5 px over.
  - Tightest title in the edition: P7 `LA PAROLA　PALAVRA DA SEMANA`,
    PIL ink ..1845.0 vs box ..1862.0 → fits by 17.0 px (raster 1846, −16.0).
  - Next tightest: P4 `LA CLASSIFICA　DOPO 11 GIORNATE`, fits by 29.0 px;
    P1 `IN QUESTO NUMERO　ÍNDICE`, fits by 53.8 px.
- The one raster "OVERFLOW" (P6 `MINIME DI ESEMPIO　gradi, dati inventati`,
  raster right 1111 vs box right 961) is a measurement artefact, adjudicated under
  the STRADDLE rule: the title's own PIL true ink ends at **538.2** (422.8 px spare);
  the raster band (same baseline y=1634) also catches the neighbouring twin box's
  title `PROPOSTA ≠ LEGGE`, which starts at x=1011 on the SAME baseline. The title
  node is byte-identical to the core (`x="110.0" y="1634"`, same text, same box
  rect `x="88" width="873"`). No glyph clipped, no ink overlapping any other object,
  no visible border (borderless cream), no regression vs the core — **none of the
  three STRADDLE defect conditions holds**. Crop evidence: `pages/crop-p6-minime.png`
  (both boxes visible, gutter between them, chart bars inside the MINIME box).
- The cream-box PIL true-ink scan over all 29 cream rects
  (`cream_spill_orphan.py`, log `cream-spill-orphan.log`) found **0 CREAM-X and
  0 CREAM-Y flags**; spill: 0 flags (no ink outside 1950×2700, no ink below y=2580
  outside furniture).

## Observations (not defects)

### O-1 — P1 cifre heads in Portuguese, redundant value + gloss
As in en (O-1): `29 — os pontos da Lazio, primeira após 11 jornadas (a Lazio lidera)`.
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
list). Core-inherited, legible, no layout impact (P8-keys flow ends 2529/2552).

### O-5 — Matching-key letter echo in P8 keys (25–28, 52–55, 141–144)
Still present (e.g. `25. c — salute = a saúde, c`). Core note format, translated
faithfully. Redundant but consistent.

### O-6 — Q120 stem truncated with "…" and options without parentheses
Still present, byte-identical to the core. Core's P8 cloze abbreviation style.

### O-7 — Q32 note uses curly quotes “Fate dolci” while the article uses «Fate dolci»
Still present. Inherited note style.

### O-8 — Masthead band, structural whitespace, P8 font size
Masthead band first node at x=0.0 — flush with the left page edge (same as es;
KIT §10 boundary case). The initial "S" and final "A" of "VENEZIA" are fully
rendered on the delivered P1; no glyph clipped. P3/P5 mid-page structural
whitespace is the core pattern (documented in KIT §10). P8 answer font 13.0 SVG px
= 9.75 pt, exactly at the SOP §1.1 floor.

### O-9 — Orphan scan: 3 flags, all byte-identical to the core (inherited, not defects)
My orphan scan flagged: P6 main text last line "18." alone (LA STRADA DELLA
MANOVRA entry "…alle ore / 18.", node `<text x="1603.5" y="641.6">18.</text>`,
identical in core); P8 Q129 stem last line "due" alone (node
`<text x="538.5" y="818.975">due</text>`, identical in core); P8 Q137 stem blank
"___" alone on line 2 (node `<text x="773.3" y="1187.825">___</text>`, identical
in core). Frozen Italian text, same column widths, same wraps. Not defects; noted
for the record. Render evidence: `pages/p-6.png`, `pages/p-8.png`.

## What was verified (summary)

- Full independent read of the 1317-line `.text.md` (all articles, boxes, captions,
  exercises 1–150 with keys and notes); all 150 keys re-verified against stems/
  articles/charts by hand, plus the gates.py 150-key audit vs the core `.text.md`
  (keys match except re-aimed 137–139 and the writing item; notes match
  translations.py except 137–140 + writing), plus a third-source check: SVG-printed
  P8 keys vs `.text.md` RISPOSTE — 149/150 exact, the one difference being Q150,
  whose printed "key" is the ✓ marker by design (see GATE-LOG §9).
- Level/page distribution: TOTAL 150; A2 47 / B1 70 / B2 33; pages
  10/18/18/18/18/18/12/38 — matches KIT. Model text counted: 99 words (range 80–100).
- Arithmetic re-computed: MD11 goals 3+1+2+3+3+2+3+1+2+4 = 24 in 10 matches;
  Q85 13−11 = 2; Q86 6+7 = 13; classifica Lazio 29 / Inter 28 / Roma 27 /
  Milan 24 / Como 23 / Udinese 5 (20th) — consistent across P1, P4 table and keys;
  Torrone Nov 7–22 = 16 days / 3 weekends; Torino FF Nov 24–Dec 2 = 9 days;
  BookCity Nov 23–29 = 7 days; P6 chart bars exactly proportional at 34 px/degree
  (5°→170, 6°→204, 7°→238, 11°→374, 13°→442).
- Golden sentences: all 8 verified verbatim, exactly 2 occurrences each in
  `.text.md` (article + P7 FRASI); freeze diff shows 0 unexplained fragments.
- §8.1 gloss check: all 33 NOTE-box headwords occur in their articles (with normal
  inflection, e.g. "imbattuta" for "imbattuto", "candele" for "candela",
  "figuranti" for "figurante", "protagonisti" for "protagonista").
- Dates/weekdays (Europe/Rome `date`, all match the paper): Nov 6 Fri, Nov 9 Mon,
  Nov 12 Thu, Nov 15 Sun, Nov 16 Mon, Nov 17 Tue, Nov 19 Thu, Nov 20 Fri,
  Nov 21 Sat, Nov 22 Sun, Nov 23 Mon, Nov 24 Tue, Dec 2 Wed, Dec 6 Sun, Dec 31 Thu.
- Facts re-checked against public sources (web, 2026-11-11):
  - Sinner won the 2025 ATP Finals — beat Alcaraz 7–6(4), 7–5 in Turin, Nov 16,
    2025, retained the title (multiple sources) — "vincitore del 2025" is correct.
  - Torino Film Festival 2026 = **44ª edizione**, Tue Nov 24 – Wed Dec 2, 2026,
    9 days — confirmed by the official regulation (torinofilmfest.org).
  - BookCity Milano 2026 = **15ª edizione**, Nov 23–29, theme «Il senno sulla
    Luna» from Ariosto's *Orlando furioso*, opening Mon Nov 23 20:00 Teatro Dal
    Verme with Colson Whitehead (2× Pulitzer), 1,360 events; Edmund de Waal among
    the international guests — confirmed (illibraio.it; milanoweekend.it;
    sudovestmilano.it). "1.360 eventi / 2.487 protagonisti / 1.164 libri /
    443 sedi" match the programme reporting.
  - Eurochocolate 32ª edizione and Festa del Torrone 29ª edizione: proof1's and
    it-en proof2's web verifications stand (re-checked by it-en proof2 on
    2026-11-11; not re-litigated here). Manovra facts (DPB Oct 15; bill
    C. 3174-bis; hearings Nov 9–12; amendments deadline Nov 17 18:00) rest on the
    core KIT's stated independent verification, as in proof1.
  - Scenario premises, not re-verified (core-level, set in the 2026–27 season
    frame): the MD11 scores / standings themselves, Zverev as 2026 world No. 1,
    Sinner out injured in 2026, Frosinone in Serie A.
- Banned terms: Ucraina/Russia/Putin/Ukraine/Gaza/Trump/Netanyahu — 0 in `.text.md`.
- U+2019: 0 in all 8 SVGs and in `.text.md` (straight apostrophes only).
- P8 personal names: only "Ariosto" (Q67 note, standard spelling), "Giulia"/"Paolo"
  (fictional section-C characters, internally consistent), "Santa Cecilia" /
  "Madonna della Salute" (feast names), "Johannes Vermeer" (image credit, standard
  spelling), "Gattuso" (Lazio coach, in the P7 quote and P4 article). No non-Latin-script
  personal name in the P8 notes.
- §1.1: paper #fbfaf6 present; no gold/brick/near-black; VOL.4 ×9, VOL.5 only in
  the 3 legitimate nodes (P2 cross-reference, P7 disclosure, P7 next-week preview);
  badge colours A2/B1/B2 present; no double outer frame (0 full-page rects);
  Newsreader for Latin text.
- KIT §7 three SHA-256 values verified against the files on disk (see Identity).
- Web PDF: real text layer (pdftotext 106,577 bytes with -layout, identical to
  print), web P1 and P8 rendered and viewed — identical to print, no tofu.

## Mechanical gates (detail in GATE-LOG.md)

run.py RC=0 / TOTAL 150 / 0 overflow · SVG rebuild 8/8 byte-identical · print PDF
re-render byte-identical to delivered · freeze baseline 8/8 (canonical tool) ·
freeze diff 0 unexplained fragments (P1–P7; P8 covered by p8 compare + 150-key
audit) · freeze strict-CJK: added CJK only 8 × U+3000 (furniture separators) ·
occlusion 0 flags (selftest OK) · cream-box PIL true-ink scan: 0 flags out of
29 cream rects · raster box-title scan: 37/38 titles fit, 1 neighbour-box artefact
adjudicated not-an-overflow (U-2) · spill: 0 flags · orphan scan: 3 flags, all
core-identical (O-9) · p8 extract 150/150 · p8 compare CLEAN, keydiff
[137, 138, 139] (expected re-aimed keys; Q140's key is the Italian sentence in
both, so no diff — correct) · P8 min font 13.0 px = 9.75 pt · print/web text
multiset identical (7965 words each, chars equal) · web PDF 1,294,408 bytes < 7 MB ·
textmd validate forward-miss 0 / reverse-miss 0 · 8/8 pages viewed from a fresh
render of the delivered print PDF + web P1/P8 viewed · gates.py copy re-run by me:
20 PASS, 0 FAIL ("GATES ALL PASS"). Production untouched: all 11 production files
re-hashed at the end, byte-identical to the pre-work hashes; no commit, no push,
no production file written.
