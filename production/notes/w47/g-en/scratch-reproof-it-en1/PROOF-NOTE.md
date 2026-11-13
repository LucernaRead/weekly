# PROOF NOTE — 2026-W47 it-en (Italiano × English), independent re-proof (proof2 second round, after fix1)

**结论 (a)：零缺陷，可定稿。** proof2 的 D-1/D-2/D-3 三项均已修复，三法实测余量全部 ≥ +12.4px；全量复校未发现新缺陷。

- Proofer: independent re-proof, second round after fix1 (no subagents used). Nothing
  was taken on trust from fix1 or proof2: every number below was re-measured by me,
  with my own scripts, on the delivered files. Where proof2 is cited, it is only as
  a cross-check of scope, never as evidence.
- Date: 2026-11-11 (UTC; work done ~20:52–21:15 UTC)
- Edition dir: `production/2026-w47/2026-w47-it-en/` (clone `~/workspace/weekly-git`, main)
- My scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it-en1/`
- TMPDIR pointed at my scratch `tmp/` throughout; `PYTHONDONTWRITEBYTECODE=1` on every
  import of production sources. No production file was written, committed or pushed.

## Identity (verified by me, full SHA-256 — matches the task byte-for-byte)

- Print PDF `La-Lucerna-VOL4-EN.pdf` — 14,032,933 bytes
  sha256 `70061d6a2c613154928c27e6fe8e6962a9036ff72223a49bbdb238cf6f84047c`
- Web PDF `La-Lucerna-VOL4-EN-web.pdf` — 1,291,161 bytes
  sha256 `d037ccdf8a7f1ac94dc288625f33bf2348ffaf4582e37e9e4dfb5449771e06fc`
- Text export `2026-w47-it-en.text.md` — 55,204 bytes / 1317 lines
  sha256 `2168a652d7608744c2dbd06924909f990c95ab9b5cc48a9d1abe3ea1fad1959b`
- All three match the task exactly (fix1's new build; the old print SHA
  `3b6b2d2c…` / 14,032,945 B is gone). Identity confirmed; proofread proceeded.
- ABSTRACT.txt: one line, English, no ASCII double quotes, facts match the issue
  (Serie A MD11 Lazio 29, Torrone Cremona, Eurochocolate Perugia, Madonna della
  Salute Venice, National Tree Day, BookCity Milan, Torino Film Festival, budget
  bill; A2–B2, 150 exercises).

## Verdict

**(a) ZERO DEFECTS — ready for finalisation.** Proof2's three defects (b) are all
fixed, each with a comfortable margin on all three independent measurement methods
(see table below), and the full re-proof (SOP §8, proofread-until-zero) found no new
defect. Observations O-1 – O-11 (carried forward from proof2, re-verified present
by my own full read) are listed separately and are not counted as defects.

## Fix1 defects re-verified FIXED (my own triple measurement)

Method ① PIL true ink (`occlusion_audit.ink_box`, Noto Sans CJK SC 23 bold) on the
shipped SVG title node vs the shipped SVG cream rect; method ② dark-pixel scan on
the 96 dpi render of the DELIVERED print PDF (render px == SVG px, 1950×2700);
method ③ fitz text-layer word bboxes on the delivered print AND web PDFs
(pt → px ×4/3). Threshold: spare ≥ +5 px on all methods. Script: `verify_triple.py`,
log `verify-triple.log`. Box verdicts are taken from the delivered-PDF render
pixels (method ②), per the task rule; ① and ③ are cross-checks.

| item | new title (source) | ① PIL ink spare | ② render-pixel spare | ③ text-layer spare (print / web) | visual |
|---|---|---|---|---|---|
| D-1 P1 cifre box | `LA SETTIMANA IN CIFRE　FIGURES` (`content12.py:44`; `translations.py:93`) | +17.0 px (ink 556.5..944.0 vs box 538.5..961.0) | +20 px (darkest ink right x=941 vs 961) | +16.9 px (words x 556.5..944.1) / +16.9 px | 2× crop `pages/crop-p1-cifre.png`: title fully inside cream, clear margin |
| D-2 P2 frase box | `LA FRASE PER RICORDARE　LEARN` (`content12.py:177`; `translations.py:563`) | +13.8 px (ink 556.5..947.2 vs 961.0) | +16 px (ink right x=945 vs 961) | +12.4 px (words x 556.5..948.6) / +12.4 px | 2× crop `pages/crop-p2-frase.png`: fully inside |
| D-3 P7 errori box | `ERRORI TIPICI　TYPICAL ERRORS` (`content7.py:83`; `translations.py:969`) | +26.8 px (ink 1461.5..1835.2 vs box 1439.5..1862.0) | +29 px (ink right x=1833 vs 1862) | +25.9 px (words x 1461.5..1836.1) / +25.9 px | 2× crop `pages/crop-p7-errori.png`: final "S" well inside |

- All three spares clear the +5 px floor on every method; the tightest value
  anywhere is D-2 method ③ at +12.4 px. No borderline (0 px) case, so the
  it-de/it-fr 0-px precedent does not need to be invoked.
- My numbers reproduce fix1's claimed values exactly on all nine cells
  (+17.0/+20/+16.9, +13.8/+16/+12.4, +26.8/+29/+25.9) — an independent
  reproduction, not a copy: my script was written fresh for this round.
- Old strings are gone everywhere: `THIS WEEK IN NUMBERS` 0×, `COMMON MISTAKES` 0×,
  `REMEMBER` (as the P2 gloss) 0× in `content*.py`, `.text.md` and `svg/*.svg`;
  new titles occur exactly 1× each in `.text.md` (lines 45/205/825) and 1× each
  in their SVG.

## Italian halves untouched; only the 3 titles changed (reconstruction proof)

- Italian prefixes are byte-identical to the core and to proof2's old strings:
  core SVG titles are `LA SETTIMANA IN CIFRE　数字看本周`,
  `LA FRASE PER RICORDARE　口诀`, `ERRORI TIPICI　常见错误`; the edition keeps
  `LA SETTIMANA IN CIFRE`, `LA FRASE PER RICORDARE`, `ERRORI TIPICI` unchanged
  before the U+3000 separator. `translations.py` (fan-out source, fix1r2 copy in
  my scratch) lines 93/563/969 carry the new `"en"` values; all other languages
  byte-identical (verified by fix1's count-asserted edit; my check: the three
  Italian prefixes match the core exactly).
- `.text.md`: substituting the 3 new titles back to the 3 old ones in a scratch
  copy reproduces proof2's old file hash **exactly**
  (`f12950aa8561371585da7ada54b15eb83df595ccb0fe51cfa513650dffd6a984`) — so the
  shipped `.text.md` differs from proof2's file in **only those 3 title strings**.
- SVGs: p3/p4/p5/p6/p8 are byte-identical to fix1's pre-fix baseline copies;
  p1/p2/p7, with the single new title string substituted back to the old one,
  are byte-identical to the pre-fix baseline too. The ONLY SVG change is the
  title string in each of the three pages.
- The other 26 cream boxes: full 29-rect PIL true-ink scan (`cream_spill_orphan.py`,
  my own run, `cream-scan.log`) finds **0 CREAM-X, 0 CREAM-Y, 0 SPILL-PAGE,
  0 SPILL-FOOTER** across all 8 pages. No new overflow anywhere.

## What was verified (summary; detail in GATE-LOG.md)

- Full independent read of the 1317-line `.text.md` (all articles, boxes, captions,
  exercises 1–150 with keys and notes); 150-key three-source audit — inline stem
  keys vs RISPOSTE section vs P8 printed keys (`p8.py extract` JSON): all 150 agree
  (Q150 is the open writing task, ✓ model-text marker); stems vs RISPOSTE show 0
  real mismatches (8 apparent diffs are my parser catching the explanatory note
  inside nested parentheses, e.g. Q13 `candele (candles (plural))` — key head
  `candele` matches). Gates also verified keys 1–150 match the core (except
  re-aimed 137–139 + writing).
- Level/page distribution: TOTAL 150; A2 47 / B1 70 / B2 33; pages
  10/18/18/18/18/18/12/38 — matches KIT. Model text counted by hand/script: 99 words
  (task range 80–100).
- Arithmetic re-verified by hand: MD11 results table sums 3+1+2+3+3+2+3+1+2+4 = 24
  goals in 10 matches (Q8/Q114 key); Q85 13−11 = 2; Q86 6+7 = 13; classifica
  Lazio 29 / Inter 28 / Roma 27 / Milan 24 / Como 23 / Udinese 5 (20th) — consistent
  across P1, P4 table and keys; chart bars match their values (Torino 5° shortest,
  Napoli 13° longest).
- Golden sentences: all 8 verified verbatim in their articles (P1 «La Lazio resta
  in vetta», «ventiquattro gol in dieci partite»; P2 «il ponte votivo sul Canal
  Grande»; P3 «oltre centocinquanta figuranti in costumi rinascimentali»; P4 «la
  squadra di Gattuso è ancora imbattuta dopo 11 giornate»; P5 «sette giorni di
  libri, ragioni e follie»; P6 «il testo può ancora cambiare»,
  «approvato dal governo non vuol dire già legge») and on P7 FRASI with correct
  page references.
- §8.1 gloss check: every NOTE-box headword occurs in its article (with normal
  inflection, e.g. "imbattuta" for "imbattuto", "candele" for "candela").
- Facts: proof2's web verifications stand and were not re-litigated (Eurochocolate
  32ª, Nov 13–22, «Fate dolci», Calabria, Massari; Torrone 29ª, Nov 7–22, «Il Confine»,
  Torrone d'Oro to Davide Simonetta 11:00 Palatorrone Sun 22, corteo 16:00,
  re-enactment 17:00; Serie A / ATP / BookCity / Manovra as in proof1). This round
  re-verified the internal consistency of every number/date in the text instead.
- Dates/weekdays (Europe/Rome `date`, all match the paper): Nov 6 Fri, Nov 7 Sat,
  Nov 8 Sun (MD11 weekend), Nov 9 Mon (issue Monday), Nov 12 Thu, Nov 15 Sun,
  Nov 16 Mon, Nov 17 Tue, Nov 19 Thu, Nov 20 Fri, Nov 21 Sat, Nov 22 Sun,
  Nov 23 Mon, Nov 24 Tue, Dec 2 Wed, Dec 6 Sun, Dec 31 Thu.
- Banned terms: Ucraina/Russia/Putin/Ukraine/Gaza/Trump/Netanyahu — 0 in `.text.md`.
- U+2019: 0 in all 8 SVGs and in `.text.md` (U+2018 also 0; straight apostrophes only).
- `.text.md` CJK ideographs: 0 (only 106 × U+3000 furniture separators and
  14 × U+FF1A fullwidth colons in the 7 frozen notes — O-4).
- §1.1: paper `#fbfaf6` present on all 8 pages; no gold/brick/near-black; VOL.4 ×9,
  VOL.5 only in the 3 legitimate nodes (P2 cross-reference, P7 disclosure, P7
  next-week preview); badge colours A2/B1/B2 present; no double outer frame
  (0 full-page rects); Newsreader for Latin text; P8 min font 13.0 SVG px = 9.75 pt,
  exactly at the SOP §1.1 floor.
- KIT: §12 (fix1) carries the new three SHAs with the old SHAs retained; §7 (pre-fix
  record) untouched with the old SHAs — verified by grep.
- Web PDF: real text layer (pdftotext 109,235 bytes, byte-identical text to print),
  web P1 and P8 rendered and viewed — identical to print, no tofu; the three new
  titles present 1× each in both PDFs' text layers.

## Observations (not defects — carried forward from proof2, re-verified present)

- O-1 — P1 cifre heads translated into English (4 lines), redundant value + gloss
  (e.g. `29 — Lazio's points, top of the table after 11 matchdays (Lazio top with
  29 points)`). Factual, deliberate build1 fix. Not counted.
- O-2 — Byline "Dalla redazione de La Lucerna" uses archaic "de" for modern "di"
  (7 × "de La Lucerna", core-inherited, systematic house style). Not counted.
- O-3 — Spaced guillemets « la vetta » (P1 LA PAROLA box, P7 LA PAROLA) vs unspaced
  «…» elsewhere. Core-inherited cosmetic inconsistency.
- O-4 — Fullwidth colon ： in 7 frozen P8 notes (16–20, 60–61): 14 × U+FF1A in
  `.text.md`, 7 in the P8 key list + 7 in the exercise list. Core-inherited, legible.
- O-5 — Matching-key letter echo in P8 keys (25–28, 52–55, 141–144), e.g.
  `25. c — salute = health, c`. Core note format, translated faithfully.
- O-6 — Q120 stem truncated with "…" and options without parentheses.
  Byte-identical to the core. Core's P8 cloze abbreviation style.
- O-7 — Q32 note uses curly quotes “Fate dolci” while the article uses «Fate dolci».
  Inherited note style.
- O-8 — Masthead band, structural whitespace, P8 font size: P1 full-page render clean;
  P3/P5 mid-page structural whitespace is the core pattern (KIT §10); P8 answer
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
- O-12 (new, this round) — D-2's gloss changed sense slightly, REMEMBER → LEARN:
  "the phrase to learn (by heart)" is a faithful short gloss for a phrase the
  section teaches, and the Italian half is untouched. Not a defect; noted for the
  record because the gloss word itself changed, not just its length.

## Mechanical gates (detail in GATE-LOG.md)

run.py RC=0 / TOTAL 150 / 0 overflow · SVG rebuild 8/8 byte-identical (in a scratch
copy with OUT repointed — production was never written by the build) · print PDF
re-render byte-identical to delivered · freeze baseline (canonical tool, TRUE core
build vs core svg) 8/8 · freeze diff 0 unexplained fragments, added CJK only
13 × U+3000 · occlusion 0 flags (selftest OK) · cream-box PIL true-ink scan: 0
overflow out of 29 cream rects · spill 0 · orphan 3, all core-identical (O-10) ·
p8 extract 150/150 · p8 compare CLEAN, keydiff [137, 138, 139] (expected re-aimed
keys; Q140's key is the Italian sentence in both, so no diff — correct behaviour) ·
P8 min font 13.0 px = 9.75 pt · print/web text identical (7931 words each, exact
text equal) · web PDF 1,291,161 bytes < 7 MB · textmd validate forward-miss 0 /
reverse-miss 0 · 8/8 pages viewed from a fresh render of the delivered print PDF +
web P1/P8 viewed · gates.py re-run by me: 20 PASS, 0 FAIL ("GATES ALL PASS").

## Production integrity (my own work left nothing behind)

- No production file was modified by me: edition SVGs re-hashed after all work —
  8/8 identical to the pre-work hashes in `svg-sha-before.txt`; the three delivered
  SHAs re-verified at the end of the round; core SVGs re-hashed — 8/8 identical to
  the freeze-baseline log hashes. `git status` shows the edition dir untracked
  (`??`), no commit, no push.
- Note on method (avoids proof2's incident): proof2's `run.py` re-run rewrote the
  production SVGs because `content*.py` hardcode OUT to production. I copied the
  edition to scratch, patched OUT in the COPIES to my scratch svg dir, verified
  zero `weekly-git/production` strings remained in the copies, and only then ran
  `run.py`. Production mtimes/SHAs are unchanged.
