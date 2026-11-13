# PROOF NOTE — 2026-W47 it-en (Italiano × English), independent round 1

- Proofer: 叶子 (round 1, independent; no subagents used)
- Date: 2026-11-11 (UTC)
- Edition dir: `production/2026-w47/2026-w47-it-en/` (clone `~/workspace/weekly-git`, main)
- Task file note: the tasked path `hidden_files/w47/scratch-fanout-it/FANOUT-REPORT-it.md`
  does not exist. The fan-out record actually consulted was
  `hidden_files/w47/scratch-fanout-it/STATUS.md` (it-en section, build4) +
  `hidden_files/w47/scratch-fanout-it/en/RECORD.md` + `en/gates5.log`.
  All builder claims in those files were re-verified independently (see GATE-LOG.md);
  nothing was taken on trust.

## Identity (verified by me, full SHA-256)

- Print PDF `La-Lucerna-VOL4-EN.pdf` — 14,032,990 bytes
  sha256 `d41e7255d7da8ea63cf07560911a518b2e55a4a7d8a9eb8b0f3c1ae6d3129e2f`
- Web PDF `La-Lucerna-VOL4-EN-web.pdf` — 1,259,104 bytes
  sha256 `32a6727966cfa130618c64356cd9db9812f04cbc96e961ff1534b143580e5903`
- Both byte sizes and SHAs match WEEKLY-KIT.md §7 exactly. Identity confirmed; proofread proceeded.
- `.text.md`: 55,286 bytes / 1317 lines (KIT says 55,286 — the on-disk file is 55,262 bytes;
  line count 1317 matches; the 24-byte difference is the KIT's figure vs the file as found —
  see observation O-10). ABSTRACT.txt: 387 bytes, one line, no ASCII double quotes.

## Verdict

**NOT zero findings: 1 defect (minor).** See D-1. Observations O-1 – O-10 are listed
separately and are not counted as defects. No定稿 decision is made here; that is the
coordinator's call.

## Defects

### D-1 (minor) — Chinese type label 「翻译」 in the English edition's body text (.text.md), Q137–140

- Location: `2026-w47-it-en.text.md`, lines for exercises 137, 138, 139, 140.
- Original (as shipped):
  - `137. [A2 · 翻译] Per la Madonna della Salute si attraversa il ponte votivo. → ___ — key: For Madonna della Salute, people cross the votive bridge. (Compare with the original) [Translate into English]`
  - `138. [B1 · 翻译] ...`, `139. [B1 · 翻译] ...`, `140. [B2 · 翻译] Every figure must be clear. → ___ — key: Ogni cifra deve essere chiara. (dovere = must) [Translate into Italian]`
- Should be: the type label in English, e.g. `[A2 · Translate]`, as the edition's own
  rendered P8 already uses ("137. Translate into English", "140. Translate into Italian").
- Evidence:
  - Full-file CJK scan of the shipped `.text.md`: the ONLY CJK ideographs in the whole
    file are these 4 × 「翻译」 (8 characters). No other Chinese anywhere in the file.
  - The shipped SVGs contain no 「翻译」 (P8 SVG ideograph count 0); both PDFs are clean.
    The residue is confined to the `.text.md` export, which per repo AGENTS.md is the
    site body rendered for readers and search engines — so the Chinese characters would
    appear on the English edition's web page.
  - The E-group answer keys themselves ARE correctly translated (137–139 English,
    140 Italian "Ogni cifra deve essere chiara." — correct translation of
    "Every figure must be clear."). The defect is the label only, not the keys.
  - Builder's stated justification ("deliberately kept 「翻译」 type label, W46 precedent")
    was checked: W46 it-en `issues/2026-w46/2026-w46-it-en/2026-w46-it-en.text.md`
    indeed contains the same 4 × 「翻译」. The precedent is real, but a precedent does not
    make Chinese characters correct in an English edition's body text, and the label is not
    a quotation of Chinese original text (the task's only allowed residue class).
- Severity: minor — cosmetic, confined to the `.text.md` export (4 lines); the printed and
  web PDFs are unaffected; the fix is fan-out-local (render the registry type in English
  in the export; no core change needed).
- Origin: frozen registry type `翻译` from the core (Chinese-reader core), carried into the
  export untranslated.

## Observations (not defects)

### O-1 — P1 cifre heads translated into English (4 lines), producing a redundant value + gloss
- Core (frozen): `29 — i punti della Lazio, prima in classifica dopo 11 giornate（拉齐奥 29 分领跑）`,
  `24 — i gol dell'11ª giornata, in dieci partite（…）`, `20.45 — l'ora di Atalanta–Inter, domenica 22 novembre（…）`,
  `oltre 150 — i figuranti del corteo di chiusura del Torrone（…）`.
- En (shipped): `29 — Lazio's points, top of the table after 11 matchdays (Lazio top with 29 points)`,
  `24 — the goals of matchday 11, in ten matches (24 goals in 10 matches)`,
  `20.45 — kick-off for Atalanta–Inter, Sunday 22 November (Atalanta v Inter, Sunday 20:45)`,
  `over 150 — the performers in the Torrone closing parade (over 150 performers in the parade)`.
- Each line now states the same fact twice (full English sentence + short English gloss in
  parentheses). In the core the head is Italian and the gloss is the reader language, so there
  is no duplication; in this edition both halves are English.
- Provenance: deliberate build1 fix (KIT §9: cifre items shortened to clear the P1-headline
  FLOW OVERFLOW). The full core↔en `.text.md` diff (401 changed line pairs) shows these 4
  cifre lines are the ONLY Italian prose changed anywhere in the edition (see GATE-LOG.md);
  everything else changed is pure explanation-layer Chinese→English. Content is factually
  correct; the P5 "IL PIANO DELLA SETTIMANA" box keeps its Italian heads with English glosses,
  so the P1 box is inconsistent with the P5 box within this edition. Flagged as an observation
  because the text is correct and the change was a deliberate, documented engineering choice.

### O-2 — Byline "Dalla redazione de La Lucerna" uses archaic "de" for modern "di"
- Occurrences (core source, inherited verbatim): P1 byline + P1 article
  ("Questa è la quarta edizione de La Lucerna in italiano."),
  P2, P3, P4 ("Dalla redazione sportiva de La Lucerna"), P5, P6 bylines — 7 × "de La Lucerna"
  in the core `.text.md`; core `content12.py:34,42,168`, `content34.py:16,116`, `content56.py:16,120`.
- Modern standard Italian requires "di" (articulated: "della"): "Dalla redazione di La Lucerna" /
  "dalla redazione della Lucerna". "De" is the archaic/literary form of "di" (Treccani,
  Enciclopedia Dantesca, Tullio De Mauro: "di (de; …)"; italki summary: "archaic form …
  still used in some central-Italian dialects and typically found in surnames").
  It is therefore attested but non-standard in contemporary prose.
- Not counted as a defect: it is systematic house style in the core (not a one-off slip),
  it survived the core's two proofread rounds, it does not affect comprehension or any
  exercise, and fixing it requires a core-level change (3 source files) that would ripple
  to all 11 it editions. Noted here so the coordinator can route it to a core decision if wished.

### O-3 — Spaced guillemets « la vetta » (P1 LA PAROLA box, P7 LA PAROLA) vs unspaced «…» elsewhere
- P1: `« la vetta » : il primo posto in classifica.` P7: `« la vetta » è il primo posto in
  classifica: …`. Elsewhere in the same edition: `«La salute è la prima ricchezza.»`,
  `«Fate dolci»`, `«Il Confine»`, `«La Lazio resta in vetta»` — no inner spaces.
  The spaced form is French typography; Italian normally writes «…» without inner spaces.
  Also note the space before the colon in `« la vetta » :` (French convention).
- Core-inherited (2 × `« la vetta »` in core `.text.md`). Cosmetic inconsistency only.

### O-4 — Fullwidth colon ： in 7 frozen P8 notes (16–20, 60–61)
- Notes read e.g. `16. attraversano — attraversare：i veneziani → attraversano`
  (renders with a visibly wide gap after the colon; measured in the SVG: the "：" element
  occupies a full 13.0 px cell vs ~5 px for the ASCII ":" used in all other notes;
  verified on a 2× crop of the rendered P8).
- Core-inherited, carried byte-identical (the core's Chinese notes use ： as separator;
  the 7 notes are the frozen Italian verb paradigms 16–20/60–61 + arithmetic 85–86 per KIT §8 —
  the arithmetic notes have no colon). Legible, no layout impact (P8-keys flow ends
  2514/2552, 38 px spare). The freeze strict-CJK check correctly counts 0 added CJK here
  (the character exists in the core too).

### O-5 — Matching-key letter echo in P8 keys (25–28, 52–55, 141–144)
- e.g. `25. c – salute = health, c`, `52. d – vetta = the top, d`, `141. d – manovra = budget bill, d`.
  The trailing ", c" / ", d" repeats the answer letter. This is the core's own note format
  (core: `25. c — salute=健康 c`), translated faithfully. Redundant but consistent and inherited.

### O-6 — Q120 stem truncated with "…" and options without parentheses
- P8: `120. Il Torino Film Festival apre... A. il 20 novembre · B. il 24 novembre` —
  Q113–119 have full stems with "___" and parenthesised options `(A. … · B. …)`.
  Byte-identical to the core (`Il Torino Film Festival apre... A. il 20 novembre · B. il 24 novembre`
  in core `.text.md`). Core's own P8 cloze abbreviation style, inherited.

### O-7 — Q32 note uses curly quotes “Fate dolci” while the article uses «Fate dolci»
- Note: `32. A — This year's Eurochocolate theme is “Fate dolci”`. The article (P3) writes
  `«Fate dolci»`. The core's note does the same (core note: `本届巧克力节主题是“Fate dolci”`,
  curly quotes in the Chinese note). Inherited note style, not a content error.

### O-8 — P1 masthead band, structural whitespace, P8 font size
- Masthead band starts x=7.4 (inside the page); last segment "VENEZIA" starts x=1694.8 and
  its final "A" is fully rendered with clear space to the page edge (verified on a 2× crop
  of the freshly rendered P1); occlusion audit EDGE class 0 flags. No clipping.
- P3/P5 mid-page structural whitespace is the core pattern (P3-main col 1 ends y≈1278,
  P5-main col 1 ends y≈1332), documented in KIT §10, left as-is.
- P8 answer font 13.0 SVG px = 9.75 pt exactly at the SOP §1.1 floor (concession step 4,
  same as the core). Not below the floor.

### O-9 — British-English collective plurals are correct, not errors
- "Lazio are top", "Gattuso's team are still unbeaten", "Roma have the best attack",
  "Udinese are bottom" — standard British sports usage, used consistently throughout
  (keys, notes, glosses). Not flagged.

### O-10 — KIT byte-size figure vs on-disk file
- KIT §7 says `.text.md` is 55,286 bytes; the file as found is 55,262 bytes (1317 lines,
  matching the KIT's line count). 24-byte difference, unexplained in the KIT; the file's
  content was fully read and verified regardless. Likely a KIT typo (or a re-export after
  the KIT was written). Not a content defect.

## What was verified (summary)

- Full independent read of the 1317-line `.text.md` (all articles, boxes, captions,
  exercises 1–150 with keys and notes); all 150 keys re-verified against stems/articles/
  charts by hand. Spot-verified arithmetic: MD11 goals 3+1+2+3+3+2+3+1+2+4 = 24 in 10
  matches; Q85 13−11 = 2; Q86 6+7 = 13; model text 99 words (counted; task needs 80–100).
- Level/page distribution: TOTAL 150; A2 47 / B1 70 / B2 33; pages 10/18/18/18/18/18/12/38 —
  matches KIT. Badge rects (60×30) counted per page from the SVGs: P1 A2 9/B1 1,
  P2 A2 14/B1 1, P3 A2 8/B1 10, P4 B1 13/B2 2, P5 B1 15/B2 3, P6 B2 18, P7 4/4/4,
  P8 A2 9/B1 23/B2 3 — all match the registry (group badges 25–28, 52–55, 141–144 counted once).
- Golden sentences: all 8 occur exactly 2× in the text (article + P7 FRASI), verbatim.
- §8.1 gloss check: every NOTE-box headword occurs in its article (allowing normal
  inflection/plural, e.g. "imbattuta" for lemma "imbattuto", "candele" for "candela").
  Every word-box word is the key of one exercise.
- Facts checked against public sources (web, 2026-11-11):
  - Serie A MD11 (6–8 Nov 2026): all 10 scores as printed (Napoli–Lazio 1–1, Inter–Como
    2–0, Roma–Sassuolo 3–0, Venezia–Udinese 2–1, Torino–Lecce 1–1, Cagliari–Frosinone 1–0,
    Parma–Bologna 1–2, Genoa–Milan 1–2, Monza–Atalanta 0–1,
    Fiorentina–Juventus 2–2); 24 goals; table Lazio 29, Inter 28, Roma 27 (31 goals, best
    attack), Milan 24, Como 23, Fiorentina 9, Udinese 20th/5 pts — all match the live table.
  - "la squadra di Gattuso": CORRECT. Gennaro Gattuso was appointed Lazio head coach
    23 June 2026 after Maurizio Sarri's departure (ESPN / OneFootball / SoccerNews /
    Football-Italia); he leads Lazio to the top of Serie A in 2026–27. (My initial suspicion
    was wrong; the check exonerates the text.)
  - ATP Finals: Alexander Zverev World No. 1 (since 2 Nov 2026); Sinner won the 2024 and
    2025 editions (beat Alcaraz 7–6, 7–5 in the 2025 final) and is out injured in 2026
    (right knee, season ended 6 Oct); Finals at Inalpi Arena, Turin, 15–22 Nov; Cobolli
    among the debutants — all as printed.
  - BookCity Milano: 23–29 Nov 2026, 15th edition, theme "Il senno sulla Luna" inspired by
    Ludovico Ariosto (IULM) — Q67's premise verified; Colson Whitehead two-time Pulitzer
    winner (2017, 2020) as printed.
  - Manovra 2027: DPB growth 2027 +0.8%, deficit 3.4% of GDP (with clause), bill approved
    by the Council of Ministers 28 Oct 2026 (~26 miliardi), Irpef 33% bracket extended
    50k→55k, ~5 miliardi from banks/insurance, more health funding, final approval due
    31 Dec 2026, DPB sent to Brussels 15 Oct — all as printed. (Bill number C. 3174-bis
    and the 9–12 Nov hearing dates were not re-surfaced in my searches; they rest on the
    core KIT's stated verification. Weekdays verified by `date`: 12 Nov Thu, 15 Nov Sun,
    16 Nov Mon, 17 Nov Tue, 19 Nov Thu, 20 Nov Fri, 21 Nov Sat, 22 Sun, 23 Mon, 24 Tue.)
- Banned terms: Ucraina/Russia/Putin/Ukraine/Gaza/Trump/Netanyahu — 0 occurrences in the text.
- U+2019: 0 in all 8 SVGs (straight apostrophes only, 74 total). The wide-apostrophe defect
  class is absent; apostrophe lines viewed on P1/P4 show no wide-glyph breakage.
- P8 personal names (task item 4): the only personal names in the P8 keys/notes are
  "Ariosto" (Q67 note — Ludovico Ariosto, standard spelling; verified via the BookCity
  theme source above), "Giulia" and "Paolo" (fictional characters of the P8 section-C
  reading passage; internally consistent — Giulia goes to the Madonna della Salute on
  Saturday, Paolo watches the torrone parade on Sunday — not real persons, so no public
  source applies), "Santa Cecilia" / "Madonna della Salute" (standard feast names), and
  the P8 image credit "Johannes Vermeer" (standard spelling; the painting is Vermeer's
  "Woman Writing a Letter with Her Maid"). No non-Latin-script personal name occurs in
  the P8 notes, so the ja-family romanisation failure mode has no analogue here.
- Freeze: core↔en `.text.md` diff (difflib, 401 changed line pairs): 400 blocks byte-identical;
  the ONLY Italian prose changed is the 4 P1 cifre heads (O-1). All other changes are
  explanation-layer Chinese→English. No Italian target text was added, removed, or altered
  anywhere else. Freeze diff (tool): added CJK = 13 × U+3000 only (furniture separators).

## Mechanical gates (detail in GATE-LOG.md)

occlusion 0 flags (selftest OK) · p8 extract 150/150 · p8 compare CLEAN (keydiff only
137–139, the re-aimed reader-sentence keys, expected) · freeze diff 0 unexplained fragments
(P1–P7; P8 covered by p8 compare + the 150-key audit) · freeze baseline direct sha256 8/8
(re-run with the build interpreter, tools/venv python, Pillow 13.0.0) · run.py re-run in a
scratch copy: exit 0, 0 overflow, TOTAL 150 · print/web text multiset identical (7,946 words
each, 0 diff) · web PDF 1,259,104 bytes < 7 MB, real text layer · P8 min font 13.0 px = 9.75 pt ·
VOL.4 ×9, VOL.5 only in the 3 legitimate nodes (P2 cross-ref, P7 disclosure, P7 next-week
preview) · textmd validate forward-miss 0 / reverse-miss 0 · 8/8 pages viewed from a fresh
render of the print PDF + web P1/P8 viewed; no overflow, overlap, footer intrusion, or tofu.
