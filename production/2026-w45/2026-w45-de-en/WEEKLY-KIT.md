# Die Lucerna — 德语周报 VOL.2 · ENGLISH-EXPLANATIONS EDITION · WEEKLY KIT

**Edition:** German core VOL.2 × English explanations — **matrix cell DE × EN**.
Target language German, reader native language English; both dimensions named in
full. The German text is the frozen W45 DE core
(`files/weekly-report-w45-de-core/`, Die Lucerna VOL.2, already final and
shipped); only the explanation layer was rewritten, directly in English
（讲解， no bridge language). No frozen German line was edited, moved, or
deleted to fit the furniture.

**Week:** Mon 2026-11-02 → Sun 2026-11-08 (P1 header:
`WOCHE VOM 2. BIS 8. NOVEMBER 2026`). **Lead story:** Englische Woche —
Champions League, Europa League, Bundesliga matchday 9 — plus the fuel
discount (Tankrabatt) running to 31 December, the autumn holiday changeover,
and the home-care debate.

**Status: builder-complete，未定稿，待独立校对。** This KIT records the
builder's own gates only. It is NOT a finalization claim, NOT an independent
proofread verdict. Nothing was posted to Discord, nothing was sent into the
main chat, no cron was created, `~/workspace/weekly-git` was not touched, and
neither the W45 DE core nor any W43 directory was modified.

## 1. Pairing furniture — three-way record (this edition / W43 shipped DE×EN / README #20)

W43 shipped DE×EN (`files/weekly-report-de-en/`, VOL.1) wins verbatim wherever
it speaks; README #20 is the family-precedent rule, not a string source.
The DE family case in #20 applies: EN/DE/ES cores carry a native subtitle
slot at y≈372, and the badge replaces it in place.

- **Masthead (from the core, unchanged):** `Die Lucerna`, UnifrakturMaguntia
  168 pt, centred x=975, baseline y=262 — identical in the W45 core, W43
  DE×EN, and this edition.
- **P1 pairing badge (subtitle slot, y=372):**
  `TEXT IN GERMAN · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS`
  — x=975, y=372, Noto Sans CJK SC, **20 pt, weight 700, fill #3e4c2a
  (olive), centred**. Byte-identical string, slot, size, colour, and weight
  to W43 shipped DE×EN. NOTE on #20: its generic text says 19.5 pt for the
  DE-family subtitle slot, but the W43 DE×EN shipped SVG measures 20 pt;
  per the recovery brief the shipped same-pairing SVG wins, and this
  edition copies the shipped 20 pt exactly — no generalisation, no
  deletion or alteration of any frozen German line to satisfy #20.
- **Edition line (P1, y=330, 46 pt bold):**
  `GERMAN WEEKLY · VOL.2 · FOOTBALL WEEK · FUEL DISCOUNT · CARE`
  (W43: `GERMAN WEEKLY · VOL.1 · CLOCKS · HOLIDAYS · FIRST FROST` — VOL
  bumped 1→2, topics replaced, format identical).
- **Top strapline (P1, y=92, 21 pt):**
  `WÖCHENTLICH AUF DEUTSCH · ONE ISSUE A WEEK · THE GERMAN THAT GERMANS READ`
  — identical to W43 DE×EN.
- **Footer, all 8 pages (x=65, y=2624, 20 pt, start-anchored):**
  `Die Lucerna · GERMAN WEEKLY VOL.2 · German text · English explanations`
  (W43 differs only in `VOL.1`). Present 8/8.
- **Page lines, all 8 pages (x=1885, y=2624, 20 pt, end-anchored):**
  `Page 1 of 8` … `Page 8 of 8` (8/8).
- **Section heads:** German · English throughout (e.g. `LEBEN · Life`,
  `KULTUR · Culture`, `SPORT · Sport`, `JUGEND · Youth`,
  `VERTIEFUNG · Deep read`, `SPRACHE · Language`,
  `ÜBUNGEN · Page N exercises`, `ANTWORTEN · All answers with notes (pages 1–8)`).
- **Gloss prefix:** `Note — ` (P2–P6 gloss boxes), `Notes — ` (P1 bridge
  line). **P8 separator:** `— Page N —` for N = 1…8 (W43 DE×EN identical;
  core uses `— 第 N 版 —`).
- **Images:** 2 embedded, both public domain, both credit lines carried
  verbatim from the core / `assets/CREDITS.md`: P1 football photo
  (`Foto: Staff Sgt. Stephanie Jacobs, U.S. Air Force — public domain`);
  P4 header-duel photo
  (`Foto: DVIDS (Armed Forces Soccer Championship, Destin, Florida, 2010) — public domain`).

## 2. What was changed vs. the core — and what was not

- **Changed (explanation layer + page furniture only):** all five gloss
  boxes (English glosses, §8), the P1 bridge line, all exercise
  instructions (Fill in / Rewrite / True or false? / Build a sentence /
  Translate into English / Translate into German / Match the pairs /
  Look at the practice chart above…), section bridges and explainers,
  error-clinic notes, toolbox glosses, the readers'-letters box, the
  next-issue teaser, the writing-task instruction, and all 150 P8 answer
  notes (now in English, half-width parens — see §4). P8 note-bracket
  form follows the DE fan-out family rule (README #14): half-width
  ` (note)`, not the core's full-width `（note）`.
- **Unchanged (frozen core):** all German articles, headlines, exercise
  bodies and options, the fixture table (P4), the practice-chart data and
  its German labels (P6: 68 % / 20 % / 12 %), all facts and dates, the
  2 public-domain images and their credit lines, the model text
  (`MUSTER · Model text (84 words)` on P8), page geometry (1950×2700),
  and the exercise registry structure (§5).
- **Exercises: 150, continuously numbered 1–150.** By page:
  P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38.
  By level (registry, identical to the core KIT): **A2 66 · B1 70 · B2 14**.
  Cross-checks: the final build log's cumulative totals
  (10 / 28 / 46 / 64 / 82 / 100 / 112 / 150) match; the standalone
  level-chip sequences in the shipped SVGs match the core's page by page
  (P1 14 · P2 15 · P3 19 · P4 16 · P5 18 · P6 18 · P7 12 · P8 21 tokens —
  groups share one chip, so chip counts are below exercise counts).

## 3. Freeze gate — German text frozen, explanation layer replaced (re-run independently)

Tool: `tools/freeze.py diff --core-svg …/weekly-report-w45-de-core/svg
--edition-svg …/weekly-report-w45-de-en/svg` (tools venv). Result,
identical to the build tree's `freeze-diff2.txt`:

| Page | Added strings | Removed strings | CJK core → edition | Added CJK |
|------|---------------|-----------------|--------------------|-----------|
| P1 | 23 | 23 | 168 → 0 | 0 |
| P2 | 36 | 32 | 186 → 0 | 0 |
| P3 | 40 | 40 | 187 → 0 | 0 |
| P4 | 25 | 22 | 155 → 0 | 0 |
| P5 | 41 | 39 | 193 → 0 | 0 |
| P6 | 36 | 33 | 228 → 0 | 0 |
| P7 | 62 | 53 | 394 → 0 | 0 |
| P8 | 150 | 141 | 1429 → 0 | 0 |
| **TOTAL added CJK characters** | | | | **0** |

Adjudication: every removed string that contains German is an
explanation-layer string (a gloss headword + Chinese gloss, a Chinese
note citing a German word, or a furniture line) — e.g. P3
`das Laub — 落叶`, P5 `der Pausenhof — 课间操场`, P7
`Meiner Meinung nach ... = 在我看来`. No pure German article sentence,
exercise stem, or option was removed; the German body strings are
present unchanged in the edition. P8's +150/−141 is the answer-note
rewrite (Chinese notes → English notes, full-width → half-width
parens, separator `— 第 N 版 —` → `— Page N —`); the German prompts
and keys outside §4's four items are unchanged. A separate whole-file
CJK scan of the 8 edition SVGs finds **0 CJK characters on every page**.

Core integrity (triple evidence): `core-hashes-before.txt` vs
`core-hashes-after.txt` differ only in the path prefix — all 8 SHA-256
values identical; an independent post-build re-hash by this recovery
round reproduces the same 8 values exactly (see §7). The core was not
touched by this build.

## 4. P8 gate — CLEAN 150 = 150, keydiff adjudicated item by item (re-run independently)

Tool: `tools/p8.py compare --core-dir …/weekly-report-w45-de-core
--edition-dir …/weekly-report-w45-de-en --target de` (tools venv).
Result: `status: CLEAN  missing=[] extra_count=0 uncertain=[]
keydiff=[137, 138, 139, 150]` — core 150 noted, edition 150 noted.

- **137 — genuine re-aim, translation item (registry type: translation,
  level A2).** Prompt (P8 §E, frozen German):
  `Der Tankrabatt läuft bis Dezember.` with instruction
  `Translate into English` (core: `翻译` / `（译成中文）`). Core key:
  Chinese translation; edition key: `The fuel discount runs until
  December.` (note: `laufen = to run, to last`). Translation items
  legitimately re-aim by definition (README §4); not an extraction
  artifact — the prompt, instruction, and key are all visible on the
  P8 card.
- **138 — genuine re-aim, translation item (A2).** Prompt:
  `Ich schaue am Dienstag Fußball.` / `Translate into English`.
  Edition key: `I watch football on Tuesday.`
  (note: `schauen = to watch`).
- **139 — genuine re-aim, translation item (B1).** Prompt:
  `Die Schule hat wieder begonnen.` / `Translate into English`.
  Edition key: `School has started again.`
  (note: `wieder begonnen = started again`).
  Items 140 (`Translate into German`, key German) and all other 146
  keys are unchanged; 137–139 are the only DE→reader-language
  translation keys in this issue, and all three re-aimed correctly.
- **150 — writing-device item, not an answer change (registry type:
  writing, level B1).** Core key: open-task rubric in Chinese
  （要点见写作框，范文在第 8 版写作框内，按要点给分）; edition key:
  `Open task — follow the points in the writing box; the model text is
  in the box on this page` (note: `Marked against the points listed`).
  Verified on the P8 card: the writing box `H · SCHREIBEN · Writing`
  (80–100 words, «Meine Fußballwoche») and the `MUSTER · Model text
  (84 words)` box are both on P8 itself, so "the box on this page" is
  exact. No model text, no rubric point, and no marking rule changed;
  only the apparatus language changed. This is the expected 150-form
  for a DE fan-out, not a keydiff to fix.

No keydiff item is a bracket/dash extraction artifact (README #13–#14
checked: the DE family uses half-width parens in fan-outs, and
`p8.py`'s joined-parse output for both P8s is a clean 150-set with no
uncertain items).

## 5. Occlusion gate — 0 / 0 / 0, plus chart-graze and same-baseline scans (re-run independently)

Tool: `tools/occlusion_audit.py …/weekly-report-w45-de-en --core
…/weekly-report-w45-de-core` (tools venv, selftest first). Result:
`selftest OK: planted classes fired {BOXTITLE: 1, COVER: 1, EDGE: 1,
FOOTER: 1, LINEX: 1, TEXTX: 1}; clean controls silent` →
`edition: 0 flags; core: 0 flags; NEW vs core: 0`. Exit 0.

Two audit blind spots (README #10, #12) were additionally checked by hand
on the shipped SVGs, because the canonical audit cannot see them:

- **Same-baseline furniture band (P1 top band, y=92):** three texts share
  the baseline — `VOL. 2 · ZWEITE AUSGABE` (x=65, start),
  `WÖCHENTLICH AUF DEUTSCH · ONE ISSUE A WEEK · THE GERMAN THAT GERMANS READ`
  (x=975, middle), `WOCHE VOM 2. BIS 8. NOVEMBER 2026` (x=1885, end).
  No x-overlap; the P1 card confirms clean separation. No collision.
- **P6 practice-chart graze (sub-30% COVER blind spot):** chart bars are
  identical to the core's (x=535; y=1482 w=1156 / y=1534 w=340 /
  y=1586 w=204; 68 % / 20 % / 12 %). True-ink boxes (venv PIL, same
  method as the audit) for the small English labels at x=425, 20 pt:
  `family care` → right ink 526.8 (8.2 clear of the bar);
  `care service` → right ink 534.8 (**0.2 clear of the bar at x=535 —
  the tightest point in the issue, but no overlap, no coverage**);
  `care home` → right ink 523.2 (11.8 clear). The P6 card confirms all
  three labels fully legible with daylight before their bars, and the
  percentages (68 % / 20 % / 12 %) sit clear past their bar ends.
  Overlap count for chart text vs later-drawn rects: **0**.

History (for the proofreader, not a live defect): the build tree's
first audit (`occlusion-edition.txt`, 20:19) fired 4 flags — P3/P5
`FERIENWECHSEL · Holiday changeover` BOXTITLE overflow, P6
`DIE ZAHLEN · This week's numbers` BOXTITLE overflow, and a P6
ÜBUNGSDATEN EDGE overflow. The fix round shortened the box titles to
`FERIENWECHSEL · Holidays` (P3, P5) and `DIE ZAHLEN · Numbers` (P6);
the second audit (`occlusion-edition2.txt`, 20:20) already read 0, and
this recovery round's independent re-run confirms 0 on the final
shipped SVGs. The ÜBUNGSDATEN footnote line now renders fully inside
the page (P6 card confirmed).

## 6. Gloss count — 25 = 25, item by item, split on `·` itself (README #21)

Counting method: split each `gloss()` call string in the build sources
on the `·` character itself (never on the spaced form ` · `), and
verify every item survives in the rendered SVG text. Core build
(`hidden_files/weekly-report-w45-de-build/`) vs this edition build:
**5 gloss boxes × 5 items = 25 items in both, same German headwords in
the same order per box**, only the gloss language changed
(Chinese → English). All 25 English items were found verbatim in the
edition SVGs:

- P2: der Tankrabatt = fuel discount · die Zapfsäule = petrol pump ·
  die Energiesteuer = energy tax · die Mehrwertsteuer = VAT ·
  der Angehörige = relative.
- P3: der Ferienwechsel = holiday changeover · die Schülerin =
  schoolgirl · der Ausflug = trip · der Advent = Advent ·
  die Lesung = reading.
- P4: die Englische Woche = English week · auswärts = away ·
  empfangen = to host · der Favorit = favorite · eröffnen = to open.
- P5: der Pausenhof = schoolyard · die Klassenarbeit = class test ·
  das Referat = class talk · ausschlafen = to sleep in ·
  die Probe = rehearsal.
- P6: der Angehörige = relative · die Pflegeversicherung = care
  insurance · der Pflegedienst = care service · die Stagnation =
  stagnation · der Aufschwung = upturn.

(The P1 `Notes — die Englische Woche = English week · der Spieltag =
matchday · empfangen = to host · die Bundesliga = Bundesliga.` line
is the core's P1 bridge line, not a `gloss()` box, and is likewise
carried over with its 4 headwords intact.)

## 7. P7 golden sentences — 8/8 verbatim, each exactly 2×, page labels recorded

Header states the rule and the page keeps it:
`Quoted word for word from this issue's articles`. Each German quote
was matched verbatim (whitespace-normalised) against the source article
pages P1–P6 and against the P7 table; every quote occurs exactly twice
(source article + P7 table), 8/8:

| # | Quote (German) | Source page · level (P7 label) |
|---|----------------|--------------------------------|
| 1 | Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga. | Seite 4 · B1 |
| 2 | Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter. | Seite 2 · A2 |
| 3 | Wer 50 Liter tankt, spart rund 8,35 Euro. | Seite 2 · A2 |
| 4 | Die Schule hat nach den Herbstferien wieder begonnen. | Seite 5 · B1 |
| 5 | Die Tage sind kurz, die Abende lang. | Seite 3 · A2 |
| 6 | Zwei schwere Auswärtsspiele für die deutschen Teams. | Seite 4 · B1 |
| 7 | Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst. | Seite 6 · B2 |
| 8 | Es geht langsam aufwärts — aber von allein geht es nicht. | Seite 6 · B2 |

Page-label distribution (as printed): Seite 2 ×2, Seite 3 ×1,
Seite 4 ×2, Seite 5 ×1, Seite 6 ×2. Level distribution: A2 ×3,
B1 ×3, B2 ×2. English translations under each quote are the
explanation layer only; no German word was altered.

## 8. Readers' letters (P7) — three facts + explicit English solicitation, all present

The P7 `LESERBRIEFE · Readers' letters` box on the shipped page
contains all four required elements (verified in the SVG text and on
the P7 card). No repair was needed in this recovery round, so no
re-render was performed.

- **Fact 1 — no real letters:** `Editors' example, not a real letter:
  no real letters or best page-8 writing yet.` and, in German,
  `Bis Redaktionsschluss keine Briefe oder Texte`.
- **Fact 2 — no best P8 writing:** same English sentence
  (`…or best page-8 writing yet.`).
- **Fact 3 — example + deferral to VOL.3:** `An example from the
  editors!` + the example letter itself
  (`„Liebe Lucerna, am Dienstag schaue ich Bayern bei Atlético. Die
  Fußballwoche ist toll! Viele Grüße — die Redaktion"`) + the promise
  that the best real letters will be printed in VOL.3.
- **Explicit open solicitation for real letters, in English (the
  qualifying sentence — not a preview line, not a per-exercise
  submission prompt):**
  `Write to us! Send your real letters — the best will be printed in VOL.3.`
  (The German companion line in the same box:
  `Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten
  echten Briefe drucken wir in VOL.3.`)

NOT counted as solicitation (and not needed): the next-issue preview
bar's `Ihre Briefe: Schreiben Sie uns! Die besten echten Briefe
erscheinen in VOL.3!` and the P8 writing-task line
(`Die besten Texte drucken wir in VOL.3 (Seite 7, «Leserbriefe»)`).
The box itself already satisfies the requirement, so this edition is
not written up as missing the solicitation.

## 9. Toolchain — interpreters and PIL versions, recorded separately for run.py and render.py

Coordinator ruling applied: **the delivered SVG bytes are authoritative**.
The KIT §7 "measure with venv PIL" rule constrains only post-render
audit measurement of SVGs; it does NOT constrain the wrap/line-break
decisions inside `run.py`.

- **`render.py` (cards + PDFs) — MUST be `tools/venv/bin/python`:**
  Python 3.12.3, **Pillow 13.0.0**, cairosvg 2.9.1, pypdf (via the venv).
  This is not a choice but a necessity: the system `python3`
  (also 3.12.3, Pillow 10.2.0) has **no cairosvg installed**, so
  `render.py` cannot run under it at all. All audit measurements in
  this KIT (occlusion true-ink boxes, chart-graze boxes) were taken
  with the venv Pillow 13.0.0, as required.
- **`run.py` (SVG generation, one process, content12 → 34 → 56 → 7 → 8
  so the bslib4 exercise registry accumulates) — interpreter free per
  the ruling, but byte-reproduction required except for intended
  changes.** `run.py` is stdlib-only (`runpy` driver, no PIL/cairosvg
  dependency), so it runs under either interpreter; the predecessor
  build did not log which interpreter invoked it, and this KIT does
  not invent one. Determinism evidence: the build tree's
  `svg-hashes-before-rerun.txt` vs `svg-hashes-after-rerun.txt` are
  identical for all 8 SVGs (a full re-run reproduced the pre-final
  state byte-for-byte). See §11 for the one provenance gap this leaves.
- **Build log:** final `build-log.txt` (one-process run) ends
  `ALL DONE`, TOTAL exercises 150, with **zero FLOW OVERFLOW / HEAD TOO
  WIDE / warning strings**. Flow end positions all sit inside their
  bottoms (e.g. P1 headline ends y=1555 vs bottom 1828; P8 keys end
  y=2248 vs bottom 2560).

## 10. Shipped files — measured from disk (not copied from stale logs)

Cards: 8 PNGs, all **1950 × 2700, RGB**:

| Card | Bytes |
|------|-------|
| p1-front.png | 1,272,716 |
| p2-leben.png | 843,709 |
| p3-kultur.png | 827,764 |
| p4-sport.png | 1,164,110 |
| p5-jugend.png | 758,501 |
| p6-vertiefung.png | 796,073 |
| p7-sprache.png | 698,882 |
| p8-uebungen.png | 1,231,723 |

PDFs (both **8 pages**; print page size 1462.5 × 2025 pt, web page
size 1400 × 1938 pt):

| PDF | Bytes | SHA-256 |
|-----|-------|---------|
| Die-Lucerna-VOL2-EN.pdf (print) | 4,137,635 | 9d12db530cc871cac670fd6e5b624a531cefd29052bbecdc23eeb647ef77611d |
| Die-Lucerna-VOL2-EN-web.pdf (web) | 4,094,288 | fc7676359c54a8ac062451dc9c394e3f2dd354403ecd4b7e80bd876ab47f467c |

Edition SVG SHA-256 (disk, final state):

| SVG | SHA-256 |
|-----|---------|
| p1-front.svg | 9bdbb6811d6db5cef17b5d98f1a3c18c4fffef3e5ca7721cc0a662f22623cbd1 |
| p2-leben.svg | 3458b1d698f64a6cbec9f57d83b67119a80d949669bfea1915af2c18abe6fb09 |
| p3-kultur.svg | fa25b5da9cdb630fc8a15fd528e150720f0c7204c96308312c423316a333b1dd |
| p4-sport.svg | 5cec412dedc041a1220a4f05bd49e1f9bc873dfa79f37e9db18eb423206f5c64 |
| p5-jugend.svg | c7ae8bb67365f8f72b49d52680b0ba050d0fbd4e7c992dd2b9ee2071fd482706 |
| p6-vertiefung.svg | a1f7b01ed4459279546d809ab302ed5289752cbea498558e241ff080472b7f6a |
| p7-sprache.svg | e478847b03b354692f114f57fcad0ba5b8ff3f8d4316867af215d1fae5052cfa |
| p8-uebungen.svg | d5dd55f2f30de48937a369765b2fab672f3eb787349f276e437fec36542f4937 |

Core SVG SHA-256 (post-build re-hash, identical to before/after):

| SVG | SHA-256 |
|-----|---------|
| p1-front.svg | 6cbd48022b5f863d941aa422869639ddc2ad2cbd203169ba87b85ba0d4fade3e |
| p2-leben.svg | 9362256dca74f8772f3e45944e1e137c487d68e5a3fca772f93bf47e7b4b6d22 |
| p3-kultur.svg | 3e8a8d16136a46a3781df045944f20eb821e0dba9b872e4f1ecc10758660ae9d |
| p4-sport.svg | b787f592599cc4d1f862c16d901766e9775e5eac82330156617a04665cb0199d |
| p5-jugend.svg | 4dcbeb97c566f4dfb56e5cb7a6e97556f2f97246d97656e0b3f81c173decb77c |
| p6-vertiefung.svg | 01b75ad49a54c8037c15b885279aca9fcd530e815633eda7d1e1f79e2233090b |
| p7-sprache.svg | fbaf8cdd8a90f2994f4ecc4a769f64d717813c38e36acec74507c3aa162f278c |
| p8-uebungen.svg | 299524bd2ad25ec447c0f422166b3db344b3caeba127e061fce37dc1e3c13891 |

**Visual pass:** all 8 cards viewed in this recovery round. No
overlaps, no cut-off text, no missing boxes. Observed and accepted as
frozen-core inheritance (not edition defects): the German
low-quote style (`„…"`, e.g. P2's column-continuation
`„verschwindet "`), and the P6 chart's 0.2-clearance label (§5).
The web PDF (4,094,288 B) is under the 10 MB repo limit.

## 11. Provenance notes and self-repair checklist (read before proofreading)

Self-repair checklist — what this recovery round did and did not do:

1. [x] Confirmed no other de-en writer was running (process scan empty;
    90-second re-check: zero new writes; all edition mtimes remain
    2026-10-27 20:23).
2. [x] Read the build tree's logs (`build-log.txt`, `render-log.txt`,
    `freeze-diff2.txt`, `p8-compare2.txt`, `occlusion-edition2.txt`,
    `core-hashes-before/after.txt`) — no unresolved warnings; the only
    warnings in the tree's history are the 4 occlusion flags in the
    superseded first audit (§5).
3. [x] Independently re-ran freeze, p8 compare, and occlusion audit
    against the final disk state (not copied from old logs) — all
    match §3–§5.
4. [x] Verified gloss (§6), P7 quotes (§7), readers' garden (§8),
    furniture (§1), PDFs/cards (§10), and all 8 cards visually.
5. [x] Readers'-garden check passed on the shipped page — **no
    re-render, no SVG/card/PDF overwrite** (es-nl recovery precedent:
    only the KIT and missing items are added).
6. [ ] **For the independent proofreader:** the two provenance gaps
    below are disclosed, not papered over. Neither blocks the gates
    above, but both should be noted in the proofread record.

Provenance gap A — **stale `render-log.txt`.** The build tree's
`render-log.txt` (20:20) predates the final 20:23 render: it lists
print PDF 4,137,638 B / web PDF 4,094,531 B and card sizes for p1
(1,273,137), p4 (1,164,238), p8 (1,230,645) that differ from the
disk-measured values in §10 (p2/p3/p5/p6/p7 match). The §10 values are
the authoritative ones — measured from the final files by this round
(pypdf page counts + SHA-256 + PIL dimensions). Do not "correct" the
disk files to match the old log.

Provenance gap B — **final SVGs vs the 20:22 rerun hashes.** The
build tree's `svg-hashes-after-rerun.txt` (20:22) matches the current
disk for p2, p3, p5, p6, p7, but **differs for p1, p4, p8**
(20:22: p1 `524ca3df…`, p4 `6a28a691…`, p8 `e09b3034…` vs disk §10).
The final one-process run (`build-log.txt`, 20:23:22) rewrote the
content modules (content12/34/56/8 mtimes 20:23:20) and produced the
disk state; the intermediate SVGs were not retained, so the exact
p1/p4/p8 text deltas between 20:22 and 20:23 cannot be diffed from the
build tree. What IS established about the final state: all gates in
§3–§8 were re-run against it and pass; the registry page/level totals
in the final build log match the core; the P8 keys on the final card
match the registry dump for all keydiff items (§4). The proofreader's
fresh pass over the final files is the control for this gap — it does
not need the intermediate files.

## 12. ABSTRACT.txt (delivered, verified — no correction needed)

Single line, English, no ASCII double quotes, naming the real topics,
a learner search phrase, the masthead, the target language, levels
A2–B2, and the exercise count. Verified against the delivered pages
(football week, Champions/Europa/Bundesliga matchday 9, fuel discount
to 31 December, holiday changeover, home-care debate — all present):

> Die Lucerna German Weekly VOL.2: a football week of Champions League, Europa League and Bundesliga matchday 9, the fuel discount running to 31 December, the autumn holiday changeover and the home-care debate; German text with explanations in English, A2 to B2, 150 exercises, for learners who want to learn German by reading real German news.

Build sources: `hidden_files/weekly-report-w45-de-en-build/`
(run.py one-process driver, content12/34/56/7/8, bslib4.py, svglib.py,
transform.py, assets/CREDITS.md + fussball.jpg + kopfball.jpg).
Edition dir: `files/weekly-report-w45-de-en/` (svg/ ×8, cards/ ×8,
Die-Lucerna-VOL2-EN.pdf, Die-Lucerna-VOL2-EN-web.pdf, ABSTRACT.txt,
this WEEKLY-KIT.md).
