# PROOF NOTE — 2026-W47 it-en (Italiano × English), independent re-proof after re-fan-out 2 (core D-2 fix)

**结论 (a)：零缺陷，可定稿。** D-2 修正与 fix1 三项均已独立重测通过；全量复校未发现新缺陷。

- Proofer: independent re-proof after re-fan-out 2 (SOP §8.4); no subagents used.
  Nothing was taken on trust from the re-fan-out report, fix1, proof2 or re-proof (a):
  every number below was re-measured by me, with my own scripts, on the delivered
  files. Prior rounds are cited only as scope cross-checks, never as evidence.
- Date: 2026-11-11 (UTC; work done ~21:59–22:10 UTC)
- Edition dir: `production/2026-w47/2026-w47-it-en/` (clone `~/workspace/weekly-git`, main)
- My scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it2-en/`
- TMPDIR pointed at my scratch `tmp/` throughout; `PYTHONDONTWRITEBYTECODE=1` on every
  import of production sources. No production file was written, committed or pushed.
  No file was written to system /tmp. Interpreter throughout:
  `~/workspace/weekly-git/tools/venv/bin/python` (Pillow 13.0.0).
- SOP: read `~/workspace/weekly-git/SOP.md` §8 and §1.1 in full, plus
  `~/workspace/weekly-git/AGENTS.md`, `scratch-refanout-it2/FANOUT-REPORT-it2.md` (full),
  `scratch-fix-it-en1r2/FIX-LOG.md`, `scratch-reproof-it-en1/PROOF-NOTE.md`,
  `scratch-fix-core-it-d2/FIX-LOG.md`.

## Identity (verified by me, full SHA-256 — matches the task byte-for-byte)

- Print PDF `La-Lucerna-VOL4-EN.pdf` — 14,032,910 bytes
  sha256 `b0444f8a89fcd1df53941dd0e3774777f17cd238fc0f93fd519c8c680c468b17`
- Web PDF `La-Lucerna-VOL4-EN-web.pdf` — 1,291,136 bytes
  sha256 `b99776c00ae69f7b0b93264769677d9bd536bcd2993c8225c092b4614581e227`
- Text export `2026-w47-it-en.text.md` — 55,183 bytes / 1317 lines
  sha256 `ad311b5bf59ae9eafc996834abba95d1f4bd899874043c605735d57cbbd7f917`
- Pre-refanout production SHAs (task + `scratch-refanout-it2/shas-pre.txt`, verified):
  print `70061d6a2c613154928c27e6fe8e6962a9036ff72223a49bbdb238cf6f84047c`
  (14,032,933 B) / web `d037ccdf8a7f1ac94dc288625f33bf2348ffaf4582e37e9e4dfb5449771e06fc`
  (1,291,161 B) / text `2168a652d7608744c2dbd06924909f990c95ab9b5cc48a9d1abe3ea1fad1959b`
  (55,204 B). All three differ from the new triple, as expected after a rebuild.
- ABSTRACT.txt: one line, English, no ASCII double quotes, facts match the issue
  (Serie A MD11 Lazio 29, Torrone Cremona, Eurochocolate Perugia, Madonna della
  Salute Venice, National Tree Day, BookCity Milan, Torino Film Festival, budget
  bill; A2–B2, 150 exercises).

## Verdict

**(a) ZERO DEFECTS — ready for finalisation.** The D-2 correction is in place in
every live layer with the old wording at zero everywhere (see §A), the fix1
three titles hold their margins on all three measurement methods (see §B), the
P7 future-tense labels are now factually correct (see §C), and the full re-proof
(SOP §8, proofread-until-zero) found no new defect. Observations O-1 – O-13
are listed separately and are not counted as defects.

## A. D-2 regression — re-verified independently (all PASS)

D-2 (core-it `content7.py:17/:18`): L17 rule examples now only assaggiare/guardare
(`andare → andrò, ` deleted); L18 now `regolare al futuro: leggerò`.

| check | result |
|---|---|
| `text.md:775` = `…Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.` | ×1, verbatim |
| `text.md:777` = `…Il verbo è leggere, regolare al futuro: leggerò.` | ×1, verbatim |
| `text.md` diff vs pre-refanout backup (`scratch-refanout-it2/backup/2026-w47-it-en/`) | exactly lines 775 and 777, nothing else |
| `text.md` byte delta vs backup | 55,204 → 55,183 = **−21** exactly |
| Old string `Le forme sono regolari: andare` in text.md / content7.py / p7 SVG | 0 / 0 / 0 |
| Old string `irregolare al futuro: leggerò` in text.md / content7.py / p7 SVG | 0 / 0 / 0 |
| New L17 in p7 SVG (tag-stripped, whitespace-normalised) | ×1 |
| New L18 in p7 SVG | ×1 |
| Edition `content7.py:17/:18` vs core-it `content7.py:17/:18` | byte-identical |
| Print PDF P7 text layer: new L17 (arrow-normalised, `→` glues to neighbours in the layer) / new L18 / old strings | ×1 / ×1 / 0 |
| Web PDF P7 text layer: same three counts | ×1 / ×1 / 0 |
| SVG diff vs backup | only `svg/p7-lingua.svg` differs; p1–p6/p8 byte-identical |
| cards diff vs backup | only `cards/p7-lingua.png` differs; p1–p6/p8 byte-identical |
| content diff vs backup | only `content7.py`, exactly lines 17–18 |
| `andare` still occurs once on P7 — in the Q101 stem `(andare)` (original-form prompt), unrelated to the old string | confirmed, not a residual |

Note: the two PDFs changed only because P7 was rebuilt (print re-render from the
shipped SVGs is byte-identical to the delivered print PDF — see GATE-LOG §5).

## B. fix1 regression — re-verified independently (triple measurement, all PASS)

Method ① PIL true ink (`occlusion_audit.ink_box`, Noto Sans CJK SC 23 bold) on the
shipped SVG title node vs the shipped SVG cream rect; method ② dark-pixel scan on
the 96 dpi render of the DELIVERED print PDF; method ③ fitz text-layer word bboxes
on the delivered print AND web PDFs (pt → px ×4/3). Threshold: spare ≥ +5 px on
all methods. Script: `verify_triple.py`, log `verify-triple.log`. Box verdicts are
taken from the delivered-PDF render pixels (method ②); ① and ③ are cross-checks.

| item | new title (source) | ① PIL ink spare | ② render-pixel spare | ③ text-layer spare (print / web) | visual |
|---|---|---|---|---|---|
| D-1 P1 cifre box | `LA SETTIMANA IN CIFRE　FIGURES` (`content12.py:44`) | +17.0 px (ink 556.5..944.0 vs box 538.5..961.0) | +19 px (darkest ink right x=942 vs 961) | +16.9 px (words x 556.5..944.1) / +16.9 px | 2× crop `pages/crop-p1-cifre.png`: title fully inside cream, clear margin |
| D-2 P2 frase box | `LA FRASE PER RICORDARE　LEARN` (`content12.py:177`) | +13.8 px (ink 556.5..947.2 vs 961.0) | +16 px (ink right x=945 vs 961) | +12.4 px (words x 556.5..948.6) / +12.4 px | 2× crop `pages/crop-p2-frase.png`: fully inside |
| D-3 P7 errori box | `ERRORI TIPICI　TYPICAL ERRORS` (`content7.py:83`) | +26.8 px (ink 1461.5..1835.2 vs box 1439.5..1862.0) | +28 px (ink right x=1834 vs 1862) | +25.9 px (words x 1461.5..1836.1) / +25.9 px | 2× crop `pages/crop-p7-errori.png`: final "S" well inside |

- All three spares clear the +5 px floor on every method; the tightest value
  anywhere is D-2 method ③ at +12.4 px.
- Method-② values differ from fix1/re-proof (a) by 1 px on D-1 (+19 vs +20) and
  D-3 (+28 vs +29): dark-pixel band bounds, ±1 px method variance, both runs
  well above the floor. All other cells reproduce fix1's claimed values exactly.
- Old strings are gone everywhere: `THIS WEEK IN NUMBERS` 0×, `COMMON MISTAKES` 0×,
  `REMEMBER` as the P2 gloss 0× in `content*.py`, `.text.md` and `svg/*.svg`;
  new titles occur exactly 1× each in `.text.md` (lines 45/205/825) and 1× each
  in their SVG.
- The other 26 cream boxes: full 29-rect PIL true-ink scan (`cream_spill_orphan.py`,
  my own run, `cream-scan.log`) finds **0 CREAM-X, 0 CREAM-Y, 0 SPILL-PAGE,
  0 SPILL-FOOTER** across all 8 pages. The same scan run on the pre-refanout
  backup (`cream-scan-backup.log`) is identical except the P7 text-node count
  (157 vs 161 — the D-2 shortening), so there is no overflow regression.

## C. P7 teaching sentences — semantic fact-check (the D-2 lesson: read the sentence, not just the keys)

P7 A2 IL FUTURO now reads (text.md:775/:777, and in the P7 render, crop
`pages/crop-p7-a2.png`):

1. `Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.`
   — CORRECT. assaggiare and guardare are regular -are verbs in the futuro
   semplice (assaggerò/guarderò are the regular forms; -giare verbs regularly
   drop the -i-). andare is no longer cited as a regular example.
2. `Il verbo è leggere, regolare al futuro: leggerò.`
   — CORRECT. leggere is a regular -ere verb in the future (leggerò is the
   regular formation: infinitive minus -e + -ò).

Independent public sources re-checked by me this round (not copied from the
fix log): FlexiClasses lists leggere under regular verbs (io leggerò) and
andare under irregular verbs (io andrò, vowel-loss stem andr-);
LibreTexts *Indicativo futuro* gives leggere as the regular -ere example
(io leggerò) and lists andare → andr- in its irregular-stem table;
FluentU lists andare (io andrò) among the verbs that eliminate the vowel
before R. The two labels are now the right way round.
- First-sentence referents still resolve: L17's opening still names
  andremo/assaggeremo/guarderemo; L18's opening still names `leggeremo a
  BookCity`; the bridge line `Talk about plans in the future: andremo,
  assaggeremo, guarderemo, leggeremo.` is intact. Q101–104 keys unchanged
  (andremo / assaggeremo / guarderemo / B), and Q104's key note
  `leggerò is the future of leggere` makes no regularity claim.
- No other `regolar*` regularity claim exists in P7: the only two
  regularity labels in the edition are these two sentences.

## What was verified (summary; detail in GATE-LOG.md)

- Full independent read of the 1317-line `.text.md` (all articles, boxes, captions,
  exercises 1–150 with keys and notes); 150-key three-source audit — inline stem
  keys vs RISPOSTE section vs P8 printed keys (`p8.py extract` JSON): all 150 agree
  (Q150 is the open writing task, ✓ model-text marker). Gates also verified keys
  1–150 match the core (except re-aimed 137–139 + writing).
- Level/page distribution: TOTAL 150; A2 47 / B1 70 / B2 33; pages
  10/18/18/18/18/18/12/38 — matches KIT. Model text counted: 99 words
  (task range 80–100).
- Arithmetic re-verified by hand: MD11 results table sums 3+1+2+3+3+2+3+1+2+4 = 24
  goals in 10 matches (Q8/Q114 key); Q85 13−11 = 2; Q86 6+7 = 13; classifica
  Lazio 29 / Inter 28 / Roma 27 / Milan 24 / Como 23 / Udinese 5 (20th) — consistent
  across P1, P4 table and keys; chart bars match their values (Torino 5° shortest,
  Napoli 13° longest); Torrone Nov 7–22 = 16 days, three weekends; BookCity
  Nov 23–29 = 7 days; Torino Film Festival Nov 24–Dec 2 = 9 days; audizioni
  Nov 9–12 = 4 days.
- Golden sentences: all 8 verified verbatim in their articles AND on P7 FRASI
  with correct page references (P1 «La Lazio resta in vetta», «ventiquattro gol
  in dieci partite»; P2 «il ponte votivo sul Canal Grande»; P3 «oltre
  centocinquanta figuranti in costumi rinascimentali»; P4 «la squadra di Gattuso
  è ancora imbattuta dopo 11 giornate»; P5 «sette giorni di libri, ragioni e
  follie»; P6 «il testo può ancora cambiare», «approvato dal governo non vuol
  dire già legge»).
- §8.1 gloss check: every NOTE-box headword occurs in its article (29/29 checked
  by script, with normal inflection).
- Facts: proof2's web verifications stand and were not re-litigated (Eurochocolate
  32ª, Nov 13–22, «Fate dolci», Calabria, Massari; Torrone 29ª, Nov 7–22,
  «Il Confine», Torrone d'Oro to Davide Simonetta 11:00 Palatorrone Sun 22,
  corteo 16:00, re-enactment 17:00; Serie A / ATP / BookCity / Manovra as in
  proof1). This round re-verified the internal consistency of every number/date
  in the text instead.
- Dates/weekdays (Europe/Rome `date`, all match the paper): Nov 6 Fri, Nov 7 Sat,
  Nov 8 Sun (MD11 weekend), Nov 9 Mon (issue Monday), Nov 12 Thu, Nov 15 Sun,
  Nov 16 Mon, Nov 17 Tue, Nov 19 Thu, Nov 20 Fri, Nov 21 Sat, Nov 22 Sun,
  Nov 23 Mon, Nov 24 Tue, Dec 2 Wed, Dec 6 Sun, Dec 31 Thu, Oct 15 Thu (DPB),
  Oct 28 Wed (Council of Ministers), Oct 25 1441 Sunday (Sforza–Visconti wedding).
- Banned terms: Ucraina/Russia/Putin/Ukraine/Gaza/Trump/Netanyahu — 0 in `.text.md`.
- U+2019: 0 in all 8 SVGs and in `.text.md` (U+2018 also 0; straight apostrophes only).
- `.text.md` CJK ideographs: 0 (only 106 × U+3000 furniture separators and
  14 × U+FF1A fullwidth colons in the 7 frozen notes — O-4).
- §1.1: paper `#fbfaf6` present on all 8 pages; no gold/brick/near-black; VOL.4 ×9,
  VOL.5 only in the 3 legitimate nodes (P2 cross-reference, P7 disclosure, P7
  next-week preview); badge colours A2/B1/B2 present; no double outer frame
  (0 full-page rects); Newsreader for Latin text; P8 min font 13.0 SVG px = 9.75 pt,
  exactly at the SOP §1.1 floor.
- KIT: §7 carries the new three SHAs (print 14,032,910 B, web 45,129 text bytes);
  §12 (fix1) retains its SHAs; §13 (re-fan-out 2) carries the new three SHAs with
  the pre-refanout SHAs retained as "was" — all verified by grep.
- Web PDF: real text layer (pdftotext 45,129 bytes, byte-identical text to print),
  web P1 and P8 rendered and viewed — identical to print, no tofu; the three new
  titles and both D-2 sentences present in both PDFs' text layers.
- Contents page references verified against the PDF: Pag. 2–8 match the sections
  (Venezia / Torrone / Serie A / giovani / manovra / Frasi / Esercizi); in-article
  cross-references (P1 "See page 4", P2 "pagina 6", P5 "(pagina 3)/(pagina 4)",
  P7 word "pagina 1 e pagina 4") all resolve.

## Observations (not defects — O-1 – O-12 carried forward from re-proof (a), re-verified present; O-13 new this round)

- O-1 — P1 cifre heads translated into English (4 lines), redundant value + gloss
  (e.g. `29 — Lazio's points, top of the table after 11 matchdays (Lazio top with
  29 points)`). Factual, deliberate build1 fix. Not counted.
- O-2 — Byline "Dalla redazione de La Lucerna" uses archaic "de" for modern "di"
  (7 × "de La Lucerna", core-inherited, systematic house style). Not counted.
- O-3 — Spaced guillemets « la vetta » (P1 LA PAROLA box, P7 LA PAROLA) vs unspaced
  «…» elsewhere (2 × spaced in text.md). Core-inherited cosmetic inconsistency.
- O-4 — Fullwidth colon ： in 7 frozen P8 notes (16–20, 60–61): 14 × U+FF1A in
  `.text.md`, 7 in the P8 key list + 7 in the exercise list. Core-inherited, legible.
- O-5 — Matching-key letter echo in P8 keys (25–28, 52–55, 141–144), e.g.
  `25. c — salute = health, c`. Core note format, translated faithfully.
- O-6 — Q120 stem truncated with "…" and options without parentheses.
  Byte-identical to the core. Core's P8 cloze abbreviation style.
- O-7 — Q32 note uses curly quotes “Fate dolci” while the article uses «Fate dolci».
  Inherited note style (2 × “Fate dolci” in text.md).
- O-8 — Masthead band, structural whitespace, P8 font size: P1 full-page render clean;
  P2/P3/P5 mid-page structural whitespace is the core pattern (KIT §10); P8 answer
  font 13.0 SVG px = 9.75 pt exactly at the SOP §1.1 floor.
- O-9 — British-English collective plurals are correct, not errors ("Lazio are top",
  "Roma have the best attack", "Udinese are bottom").
- O-10 — Orphan scan: 3 flags, all verified by me as byte-identical nodes
  (same text, same x/y, same font) in the core SVGs: P6 "18." at x=1603.5 y=641.6;
  P8 "due" at x=538.5 y=818.975; P8 Q137 "___" blank at x=773.3 y=1187.825.
  Frozen Italian text, inherited wraps. Not defects.
- O-11 — "56 titles" is a phantom number; no count of 56 corresponds to anything
  in this edition (the string "56" occurs only twice in `.text.md`, exercise 56
  stem + key).
- O-12 — D-2's gloss changed sense slightly, REMEMBER → LEARN:
  "the phrase to learn (by heart)" is a faithful short gloss for a phrase the
  section teaches, and the Italian half is untouched. Not a defect; noted for the
  record because the gloss word itself changed, not just its length.
- O-13 (new, this round) — Tightest cream-box title in the edition is NOT one of
  the fix1 trio: P1 `IN QUESTO NUMERO　CONTENTS` ends at ink 1854.8 vs box 1862.0
  (PIL spare +7.2 px; 96 dpi render darkest pixel x=1856 → spare +6 px). It is
  inside the box, above the +5 px floor, and byte-identical to the pre-refanout
  backup (STRADDLE shared-title ink diffs: NONE) — so not a defect and not a
  regression, but it is the tightest title in the edition and worth watching if
  that box is ever re-touched.

## Mechanical gates (detail in GATE-LOG.md)

run.py RC=0 / TOTAL 150 / 0 overflow · SVG rebuild 8/8 byte-identical (in a scratch
copy with OUT repointed — production was never written by the build) · print PDF
re-render byte-identical to delivered · freeze baseline (canonical tool, TRUE core
build vs core-it's own svg) 8/8 · freeze diff 0 unexplained fragments, added CJK
only 13 × U+3000 · occlusion 0 flags (selftest OK) · cream-box PIL true-ink scan: 0
overflow out of 29 cream rects · spill 0 · orphan 3, all core-identical (O-10) ·
p8 extract 150/150 · p8 compare CLEAN, keydiff [137, 138, 139] (expected re-aimed
keys; Q140's key is the Italian sentence in both, so no diff — correct behaviour) ·
P8 min font 13.0 px = 9.75 pt · print/web text identical (7928 words each, exact
text equal; pdftotext 45,129 bytes each) · web PDF 1,291,136 bytes < 7 MB ·
textmd validate forward-miss 0 / reverse-miss 0 · 8/8 pages viewed from a fresh
render of the delivered print PDF at 200 dpi + web P1/P8 viewed · gates.py re-run
by me: 20 PASS, 0 FAIL ("GATES ALL PASS").

## Production integrity (my own work left nothing behind)

- No production file was modified by me: edition SVGs re-hashed after all work —
  8/8 identical to the pre-work hashes (only the path prefix differs between the
  two hash files); the three delivered SHAs re-verified at the end of the round;
  core SVGs re-hashed — 8/8 identical to the freeze-baseline log hashes (core p7
  `a7e6afa4…` matches the D-2 fix log's stated hash). `git status` shows the
  edition dir untracked (`??`), no commit, no push. The core-it `M` entries in
  `git status` are the D-2 fix round's, not mine.
- Method note: production `run.py`/`render.py` were NOT run in place (their
  `content*.py` OUT paths hardcode production). I copied the edition to scratch,
  patched OUT/BASE in the COPIES to my scratch dir, verified zero
  `weekly-git/production` strings remained in the copies, and only then ran
  `run.py`. Production mtimes/SHAs are unchanged.
- Tool limitation recorded: none encountered. `freeze.py diff` and `p8.py compare`
  cannot see pure-Latin text drift (both confirmed blind to the D-2 change, as the
  D-2 fix log already noted); the D-2 verification therefore rests on the
  text-layer checks, the text.md diff and the freeze baseline SVG byte comparison,
  all of which were run.
