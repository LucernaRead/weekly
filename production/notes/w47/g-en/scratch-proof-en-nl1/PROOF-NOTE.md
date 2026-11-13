# PROOF-NOTE — Lucerna Weekly 2026-W47, edition en-nl (proof1, re-fanout #2 rebuild)

- **Edition:** English target, Dutch reader (`production/2026-w47/2026-w47-en-nl/`)
- **Proofreader:** independent proof1 (SOP §8.4); not the builder / not the fan-out agent.
- **Date:** 2026-11-11 (Toronto, America/Toronto)
- **Scope:** full text.md read (1,305 lines); 150/150 answer keys checked stem-by-stem against three sources
  (registry.json, text.md appendix, P8 extracted keys) plus the rendered P3/P8 SVGs where keys print;
  8 print pages + web P1/P8 visually inspected from fresh renders of the delivered PDFs;
  external facts in the rewritten Ashes article re-verified by web search; all mechanical gates re-run
  (see GATE-LOG.md).
- **Build under proof:** the en re-fanout #2 rebuild (`scratch-fanout-en2/FANOUT-REPORT.md`).
  The PROOF-NOTE/GATE-LOG from the 09:47–09:57 proof1 round belong to the superseded build
  (print `5b2a364b…`, 29,340,703 B) and were archived to `archive-oldbuild/`; nothing below is copied
  from them — every number was re-measured on the new build.
- **Core:** `core-en` finalized before this proof. Core SHAs measured before AND after this proof,
  identical (see §File identity). Core was not touched.

## Conclusion: (a) —定稿，零缺陷 (final, zero defects)

All four defects of the previous build's proof1 are verified fixed in this rebuild, and no new
defect was found in the full re-proof. The one carried-over wording that looks wrong at first
glance (P4 "lost 4–0 on their last two tours, in 2017–18 and 2021–22") is checked and NOT flagged —
see "Checked and not flagged" §4 for the reasoning with the source line.

---

## File identity (measured, before proofing)

| file | size (B) | SHA-256 |
|---|---|---|
| print `The-Lucerna-VOL4-en-nl.pdf` | 29,341,272 | `a5957d64e727662c0d4763596af517f0eae324471b93a4bd9dadb304c03bc136` |
| web `The-Lucerna-VOL4-en-nl.web.pdf` | 2,411,538 | `ee3d98baba20febe72c297ccb2591055991d4ed9b341b1429b6c7748b3371193` |
| `2026-w47-en-nl.text.md` | 53,568 | `baecaf6e92ff837857e3d6d7dd7ae28f2b1fbb15b8be78bec9428a83c13be459` |

All three match the task values exactly. Both PDFs are 8 pages (`pdfinfo`, 1462.5 × 2025 pts).
Probe: `git hash-object` OK (`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`); probe file written in
`scratch-proof-en-nl1/` before any work. No repo-side writes (all proof artifacts in the goals-side
scratch dir only; `git status` shows the two edition dirs as untracked, pre-existing state).

Core-en (measured before AND after; unchanged):
- print `The-Lucerna-VOL4-en-zh-cn.pdf` (the on-disk name inside `core-en/`) — 41,407,278 B,
  `b484e007e6e0e29a78ea3f81c412e9c27c45a7c2b317a9a6081a2f63eb416566`
- web `The-Lucerna-VOL4-en-zh-cn.web.pdf` — 2,804,271 B,
  `7277e32a96f26974efd68d5e27978e0f1570dd15222f29a060ecdf7dbd89d3f8`
- text `2026-w47-en-zh-cn.text.md` — 51,405 B,
  `e368828a3fd5bb5a90de0d506a94fc03b22453e1d3d5ff139792f2b42e0ff70b`

All three equal the fixed-core values in the fan-out report. The KIT (`WEEKLY-KIT.md` lines 14–18)
records the new edition SHAs.

## Carry-forward verification (previous proof1's 4 defects → this rebuild)

### 1. Q39→a / Q40→d — FIXED, four-way consistent (was: keys swapped, HIGH)

- **P3 SVG defs (y-order):** a. "a person who teaches and guides" (y=1078.7), b. "a person chosen
  to take part in the" (y=1149.7), c. "a person who lives with you in the" (y=1220.7),
  d. "the place where the Games are" (y=1291.7). Terms: 38 tribute, 39 mentor, 40 arena, 41 campmate.
  SVG "Uitleg" line repeats the same pairings in Dutch.
- **Registry (nl):** 38=b, **39=a** (`mentor = een mentor a`), **40=d** (`arena = de arena d`), 41=c.
  Core registry identical: 39=a, 40=d.
- **text.md appendix:** line 1083 `39. [A2] Woorden combineren — a (mentor = een mentor a)`,
  line 1085 `40. [A2] Woorden combineren — d (arena = de arena d)`.
- **P8 extracted keys:** 39='a', 40='d' (also 38='b', 41='c'). The rendered P8 ANSWERS block prints
  "39. a · 40. d" (verified visually in `render/p-8.png`, "— Pagina 3 —" column).
- Four sources agree; the defect is closed. (P3's rendered page is pixel-identical to the old build —
  see old-vs-new diff — which is correct: no key letter ever printed on P3; the fix lives in
  registry/text.md/P8 only.)

### 2. Ashes staleness — FIXED, P4 fully rewritten as 2025–26 retrospective (was: HIGH)

- P1 IN BRIEF now: "ASHES — A year ago: Australia beat England 4–1 in the 2025–26 Ashes. (p. 4)".
- P2 "WHAT IS ON THIS WEEK?" now: "page 4 looks back at the Ashes". P5 "THE JUNGLE, TOO" carries no
  Ashes claim any more. Stale-phrasing sweep on text.md (`ashes begin|first test.*perth|never hosted|
  last tour skipped|Doggett may play|Day one is already sold out|Boland takes`) returns 0 hits
  (the only "first Test" hits are the retrospective ones, e.g. line 439).
- P4 feature "Perth, One Year On: How Australia Kept the Ashes" (text.md lines 439–451) — every new
  factual claim re-verified by web search on 2026-11-11 (sources: ICC via IANS, TNT Sports, Sky Sports,
  cricket.com.au, ECB schedule via Sky/ESPN/Radio Times):
  - "On Friday, November 21, 2025, Australia played England in the first Test at Perth Stadium —
    the first Ashes Test at the ground. Australia won in two days, by eight wickets. It was the
    shortest Ashes Test, by balls bowled, since 1888." ✓ — 847 deliveries, shortest since 1888
    (1888: 788 Old Trafford, 792 Lord's); 8-wicket win, Head 123.
  - "The series ran from November 21, 2025, to January 8, 2026. Australia won the first three Tests —
    in Perth, in Brisbane and in Adelaide — and kept the Ashes after the third Test." ✓
  - "England won the fourth Test, in Melbourne, by four wickets: their first Test win in Australia
    for almost fifteen years." ✓ — Melbourne 26 Dec 2025, 852 balls, two-day finish; first England
    Test win in Australia since Jan 2011.
  - "Australia won the fifth Test, in Sydney, by five wickets. The final score was 4–1." ✓
    (Sydney, target 160, Jan 8, 2026).
  - "Pat Cummins was out with a back injury, Josh Hazlewood with a hamstring injury. Steve Smith
    led the side instead. Scott Boland played, and Brendan Doggett played his first Test." ✓
    (Doggett's debut was the Perth Test; Smith captained.)
  - "Australia lost their first Test at the ground in November 2024, by 295 runs to India" ✓
    (unchanged, verified in the previous round).
  - "The ATP Finals in Turin run from Sunday, November 15, to Sunday, November 22" ✓ (Nov 15–22, 2026).
- Q46 new stem/key A: "The 2025–26 Ashes began on... A. Friday, November 21, 2025, in Perth" —
  registry key A, note "De eerste Ashes-Test 2025–26: vrijdag 21 november 2025 in Perth";
  text.md line 1097; P8 extracted 'A'; P4 SVG stem verified. ✓
- Q52 key `hosted`, Q55 key `won` — registry, text.md (lines 1109/1115), P8 extracted all agree. ✓
- Q125 key A "Australië won de Ashes 2025–26 met 4–1" — registry, text.md line 1255, P8 extracted 'A',
  P8 SVG stem "Australia won the 2025–26 Ashes by... A. 4–1". ✓
- "Perth is winning!" → "Arsenal are winning!" confirmed in P4 SVG text and visually on the render;
  "Perth is winning" 0 hits in text.md/registry/SVG text. ✓

### 3. P7 NEXT WEEK "certified results" promise — FIXED (was: MODERATE)

- New wording (text.md line 883, visually confirmed on P7 render): "Thanksgiving in America.
  The Ashes: England's rematch waits until June 2027. More certified results of the midterm
  election. And your letters — the first real ones."
- "More certified results" is a comparative, not a promise of completeness: state certification runs
  Nov 10–Dec 18, so by VOL.5's week (Nov 23–29) strictly more states will have certified than in
  VOL.4's week. The P6 conditional stands unchanged ("When the certified results are in, VOL.5 will
  report them", line 661) and Q93 (key C, "VOL.5 brengt de bekrachtigde einduitslag") is consistent
  with that conditional. No flat promise remains.
- "England's rematch waits until June 2027" ✓ — ECB-confirmed 2027 Ashes in England, 18 Jun–2 Aug
  2027 (Trent Bridge opener Fri June 18); the paper claims only "June 2027".

### 4. Dutch guillemets « » — FIXED (was: nl-level MINOR)

- 0 hits for « / » in text.md, registry.json, all 8 SVGs, and all content*.py (verified by
  `grep -c` and by <text>-only extraction). The 4 spots now use curly double quotes:
  Q65 `Het thema dit jaar is "Doorbreek de stilte"`, Q126 `Thema van de Week tegen Pesten:
  "Doorbreek de stilte"`, Q88 `De uitslag bekendmaken`, H instruction `Mijn maandag 16 november` —
  all visible with “ ” on the P8 render.

### 5. ABSTRACT — full form (was: short-form, §9-class)

- `ABSTRACT.txt` (new build): "The Lucerna Engelstalig weekblad VOL.4: de aangekondigde uitslag
  van de Amerikaanse tussentijdse verkiezingen van dinsdag 3 november — de Democraten winnen het
  Huis en de Senaat, 254 tegen 162 zetels, certificering van de stemmen van 10 november tot
  18 december; vanaf maandag 16 november de Week tegen Pesten en de Dag van de Ongelijke Sokken,
  op vrijdag 20 november Wereldkinderdag en de nieuwe Hunger Games-film, op zaterdag 21 november
  de terugkeer van de Premier League en de ATP-finale in Turijn, en een terugblik op de Ashes in
  Perth van een jaar geleden (4–1); Engelse tekst, Nederlandse uitleg, niveaus A2–B2,
  150 oefeningen, voor Nederlandstalige lezers die Engels leren met nieuws uit de Engelstalige wereld."
- Contains Lucerna (×1), VOL.4 (×1), 150 (×1), A2–B2 (×1); 0 ASCII double quotes. ✓
- "Bevestigde/Bevestigd" (old wording) 0 hits in text.md/registry/SVG text; "Aangekondigde" now in
  the P1 strip ("Tussentijdse verkiezingen · Aangekondigde uitslag · Zie pagina 6"), P1 SVG text,
  and Q82's note ("Aangekondigd op 8 november"). The old proof's P1-kicker tension observation is
  resolved by this rewording.

### 6. Core-fix titles carried over

- "SENATE IN NUMBERS　Senaat" (SVG title sweep 337.9 px, margin +66.6) and "SATURDAY, NOV 21
  Zaterdag" (334.0 px, margin +70.5) both present in the SVGs and visually clean. The old
  "THE SENATE, IN NUMBERS　De Senaat" form is superseded by the core fix, as the fan-out report notes.

## Full 150-key verification (manual, stem-by-stem)

- Registry vs text.md appendix keys: **0 mismatches / 150** (scripted parse; appendix continuous 1–150).
- Registry vs P8 extracted keys: 149/150 exact (keycheck RC=0); the single mismatch is n=150, the
  known extractor truncation of the open-question long label ('Open vraag' vs the full registry note).
- Matching sets re-verified against stems: P2 D (24 b, 25 c, 26 a, 27 d), P3 C (38 b, **39 a, 40 d**,
  41 c), P4 C (56 b, 57 c, 58 d, 59 a), P5 C (74 d, 75 a, 76 b, 77 c), P8 F (141 b, 142 c, 143 d, 144 a).
- P6 chart arithmetic 254+162+19=435 ✓ (Q87 key C). MODEL text 82 words (80–100 required) ✓.
- Per-page counts 10/17/18/18/18/18/12/39 = 150; levels A2 62 / B1 66 / B2 22; numbering continuous 1–150.
- Golden sentences 8/8 verbatim against this issue's articles (checked line by line: P2, P1, P4, P6 ×2,
  P3, P5, P1).
- P8 cloze 112–119 re-checked: 112 Tuesday (Nov 3 is a Tuesday), 113 call, 114 continues, 115 will
  meet, 116 writes, 117 will certify, 118 wears, 119 will watch — all correct in tense/person.
- Weekdays: every "Weekday, November N" in text.md verified against `date` (America/Toronto). All
  2026 dates match. The two apparent mismatches in the automated sweep were the 2025 date
  "Friday, November 21, 2025" (checked separately: 2025-11-21 is indeed a Friday; Nov 21, 2026 is
  a Saturday and is correctly called Saturday wherever the 2026 date is meant).
- "next Sunday" freeze rule: **no applicable object** — 0 hits for "next Sunday" in core-en,
  en-nl, and `tools/tables.py` (grep). The 16× "Sunday" hits in text.md are all "Sunday, November 8"
  (the calls date) and similar explicit dates, not the frozen phrase. Nothing to apply.

## Observations (not defects)

1. **Widowed section head (cosmetic, carried over):** P5 "D PRESENT CONTINUOUS" head sits at the
   bottom of column 2 with its instruction line split across the column break ("Herschrijf in de
   tegenwoordige tijd (wat er" / "nu gebeurt).") and items 78–81 at the top of column 3. Readable,
   just untidy. Same as the previous round's observation; P4's heads are NOT widowed in this build
   (B/C/D heads each sit with their items in column 3).
2. **P5 "FRIDAY'S WORDS":** "Elk kind heeft rechten | Every child has rights = Elk kind heeft
   rechten." — the gloss repeats the Dutch. Harmless TM carryover, unchanged.
3. **House triple 254/162/19 is a live-count snapshot, not an error** — AP Nov 8 call as cited by the
   core KIT; the paper dates its figures to Nov 8 and the arithmetic checks out.
4. **Georgia runoff is phrased conditionally** ("If no candidate wins a majority…", P2/P6; Q13/Q21
   options "if needed") — true as a conditional statement of the Georgia rule (runoff Dec 1).
5. **"Rafael Jodar"** is spelled without the accent in body text and SVG (Spanish: Jódar). Diacritic
   dropped in English body text; not a factual error.

## Checked and NOT flagged (with reasoning)

1. **P4 "they lost 4–0 on their last two tours, in 2017–18 and 2021–22"** (text.md line 445;
   core-en line 445, verbatim core wording, core re-proof (a) passed with it). The sentence is
   past-perfect anchored to the eve of the 2025–26 series ("England had not won a Test series in
   Australia since 2010–11 — they lost 4–0 on their last two tours, in 2017–18 and 2021–22"):
   the two tours before the 2025–26 series were indeed both 4–0 losses, and the explicit years pin
   the phrase to those tours. The same article states, two paragraphs earlier, that Australia won
   2025–26 4–1 and England won in Melbourne — so no reader can come away thinking 2025–26 was
   4–0. The previous round's objection applied to the old article, where the series was presented
   as about to begin; the retrospective framing plus explicit years resolves it.
2. **Q93 / line 711 exercise "The certified results will be reported in... C. VOL.5"** — consistent
   with the P6 conditional ("When the certified results are in, VOL.5 will report them"); the key
   follows the paper's own conditional statement, as in the previous round.
3. **"VOL." occurrences in text.md (13×)** — the issue's own volume labels (VOL.4/VOL.5) in
   reader-facing copy, not internal structure.
4. **D5 fonts (recorded only, not judged):** SVG font-family counts — Newsreader 1023,
   Noto Sans CJK SC 663, Noto Serif CJK SC 27, DejaVu Sans 4, UnifrakturMaguntia 1.

## Visual check (fresh renders from the delivered PDFs)

- `render/p-1.png` … `p-8.png` (pdftoppm, 100 DPI, from the delivered print PDF) + `web-p1-1.png`,
  `web-p8-8.png` (from the delivered web PDF). All 8 pages + web P1/P8 viewed: no overflow, overlap,
  clipping, or cut-off text; footers "Pagina N van 8" on all pages; P3 matching block, P7 toolbox /
  readers' corner, P8 answers block all as expected; P8 answers print "39. a · 40. d" and end well
  above the footer; MODEL box ends well above the footer. Web P1/P8 are visually identical to print
  P1/P8.
- P1 SEARCHES bars, P2 SAY IT three panels (all inside), P4 Grace photo + "SATURDAY, NOV 21" box,
  P5 children photo + "ODD SOCKS, IN NUMBERS" box, P6 voting-booth photo + practice ballot,
  P7 Johnson portrait (Samuel Johnson, 1772 — correct attribution, not Mike Johnson) all clean.
- CREDITS (`assets/CREDITS.md`) verified: all 8 images PD/CC0 with sources (capitol Noclip, turkey
  Audubon, tiger Rousseau *Surprised!* 1891, grace W. G. Grace Barraud, children Bain/Lawrence 1912,
  voting Zirkel CC0, johnson Samuel Johnson 1772 Reynolds, readingroom Highsmith). football1910.jpg
  NOT used.

## Old-vs-new per-page compare (new build vs archived old build, backup SHAs verified)

Pixel diff (100 DPI renders, threshold >30): P1 0.91%, P2 0.71%, **P3 0.00% (pixel-identical)**,
P4 10.53%, P5 0.16%, P6 3.66%, P7 5.83%, P8 0.62%. Every change is confined to the regions the
rebuild touched (P4 full Ashes rewrite; P7 NEXT WEEK + drills; P6 notes/exercises; P1 strip +
IN BRIEF; P8 answer notes; P5 one box). P3 identical is expected and correct (no key letter prints
on P3). No unexpected page changed wholesale; no layout regression.
