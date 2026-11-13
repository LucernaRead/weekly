# PROOF NOTE — W47 ru-it (2026-w47-ru-it) — independent re-proof, round 2

**Proofer:** independent (did not build this edition).
**Date:** 2026-11-11 (evening, America/Toronto).
**Verdict: (b) — 6 FINDINGS** (one defect class, six instances; see §2).
Per `weekly-git/AGENTS.md`, insertion requires one full independent proofread with **zero
findings** plus a geometry-overlap audit with zero flags — this edition does **not** meet
the zero-findings bar as delivered. The fix that triggered this re-proof (text.md L836)
itself is verified correct (§1); the findings are pre-existing rendering defects in the
print PDF that this re-proof surfaced, not regressions from the fix.

## 1. The L836 fix — VERIFIED

- text.md SHA-256 at start **and** end:
  `0bb5739a9e2a1215074b8d5cba566736e88cd84d45f3bc28eb0fe5a8966f5989` (63,972 B) —
  exactly the expected value. Start = end, no change during the read.
- L836 reads exactly:
  `150. ✓ Vedi il testo modello nella sezione H di questa pagina (97 parole)`
  and matches the printed P8 Q150 line verbatim.
- Appendix keys 1–150 all present in text.md and all match the printed P8 keys.
  Programmatic comparison (text.md appendix lines 687–836 vs P8 extracted keys):
  150/150 found on both sides; the only 3 raw diffs (keys 35, 92, 139) are
  pdftotext spacing artifacts around `—` / `→` / `:` (the rendered P8 shows the
  spaces; text.md is correct). No other key differs in letter or note.
- Model text (section H) is exactly **97 words** in text.md, and is present complete
  in the print P8 H section (sentences verified in order; the 196-word figure from a
  naive regex over the raw dump is a pdftotext column-interleaving artifact, not a
  second copy — the text occurs exactly once).
- Print/web PDFs were NOT rebuilt by the fix (SHAs unchanged, §4).

## 2. FINDINGS (6) — fused word pairs in the print PDF

One defect class: in the print PDF, at six spots, the ink gap between two words is
1–5 px at 200 dpi (0.36–1.80 pt), i.e. at or below the font's own inter-letter
spacing on the same line, so the two words render as a single fused token that reads
as a typo. **The source text.md has a correct space at every one of these spots**
(verified) — the fault is in the print rendering only: `svg/` places words as
separate `<text>` elements with a space-only `<text>` element between them, and in
these six spots that space element yields an effectively zero gap. (The web PDF
carries the same text layer — its extracted text is byte-identical to the print
text — so the fused tokens are in the web text layer too.)

Method for each finding: ink-gap measured on a 200 dpi render of the delivered print
PDF at the exact SVG coordinates, compared against the same line's normal word gaps
(10–16 px) and inter-letter gaps; five of the six also visually confirmed in a
200 dpi crop.

| # | Location | As printed (defect) | Correct form | Measured gap @200dpi | Same-line word gaps |
|---|---|---|---|---|---|
| F1 | P1, "О ЧЁМ ПИШУТ" box, subtitle | `Главныетемы недели в российскихСМИ` | `Главные темы недели в российских СМИ` | Главные\|темы 7 px; **российских\|СМИ 4 px (1.44 pt)** vs 6–8 px letter gaps | 11–14 px |
| F2 | P1, "СНЕГ БУДЕТ?" column | `метеорологическаязима придёт…` | `метеорологическая зима придёт…` | **5 px (1.80 pt)** vs 5–6 px letter gaps | 10–13 px |
| F3 | P4, header band | `14-й тур: все восемь результатов+ сборная` | `…результатов + сборная` | **1 px before `+`** (12 px after it) | 10–13 px |
| F4 | P4, photo caption | `…общественное достояние(Wikimedia Commons)` | `…достояние (Wikimedia Commons)` | **1 px (0.36 pt)** vs 6 px letter gaps | 11–12 px |
| F5 | P8, appendix key 92 | `…di fila:пять дней` | `…di fila: пять дней` | **1 px (0.36 pt)** vs 2–5 px letter gaps | 5 px (small-type appendix) |
| F6 | P8, appendix key 139 | `Attenzione:играть + с + strumentale` | `Attenzione: giocare…` (i.e. `Attenzione: играть + с + strumentale`) | **3 px (1.08 pt)** vs 3 px letter gaps | 3 px (small-type appendix) |

Notes:
- F5/F6 sit in the answer key — the correctness-critical part of the paper — where a
  fused note (`fila:пять`, `Attenzione:играть`) is most likely to confuse a learner.
- F1 has two fused junctions in one line; both are counted as one finding (one line).
- F3: only the space *before* `+` is missing; the space after it (12 px) is normal.
- The P2 body instance of the same phrase as F2 (`Профессиональные праздники не дают
  выходных`, P2 body and P7 `ФРАЗЫ НЕДЕЛИ` quote) is **not** a finding: measured
  8 px (P2) / 7 px (P7) — narrow but above the letter gaps and visually spaced
  (200 dpi crop verified for P2).

## 3. What passed (no findings)

- **Content, all 8 pages:** read in full from the print PDF text extraction and verified
  against the 100 dpi full-page renders. Russian articles read correctly; Italian
  explanations read correctly; no factual/date/number contradiction found.
  Spot-verified: 31 pts Zenit/Dinamo, Krasnodar–CSKA 4:2 Sat 7 Nov, Lokomotiv–Rubin
  0:1, Baltika–Dinamo Makhachkala 0:1 at 20:45, 8 matches / 21 goals, 15th round
  20–22 Nov, national team 12 Nov Tashkent / 17 Nov 19:00 Krasnodar vs Venezuela,
  Student Day 17 Nov (decision Prague 1946; Russia's main day 25 Jan),
  Ded Moroz birthday 18 Nov in Veliky Ustyug, Black Friday calendar date Fri 27 Nov
  2026 (27 Nov 2026 is a Friday), Ozon 13 Nov–2 Dec, Wildberries 16–30 Nov,
  Cyber Monday 30 Nov, Black Friday in Russia since 2013, 11.11 Ozon 14.4M orders
  11 Nov 2025, chart 38/26/18/18 %, week 16–22 Nov = 5 working days + 2 free.
- **Exercises / keys:** keys 1–150 spot-checked against the articles (Q1–Q10, Q13,
  Q15, Q20 `желании`, Q25–28 matching, Q52–60 scores, Q65–69, Q83–100 incl. all
  four transformations, Q113–150 incl. Masha reading, translations 137–140 in
  Italian, dialogue 145–149); all correct. Weekly word `чёрная пятница` and the
  P2/P7 word glosses are correct. Captions are correct (Toxer427 CC0; Yuon
  `Зима. Ростов`; 1912 Olympic football photo, author unknown, public domain;
  Pushkin portrait by Kiprensky 1827; Bilibin `Морозко` 1932, mentioned in the
  text.md footnote).
- **Layout:** all 8 pages viewed as renders (100 dpi full page; 200 dpi for P2 and
  for every finding). No overflow, overlap, clipping or tofu observed. No U+FFFD in
  text.md or print text. No control characters in text.md.
- **text.md read:** lines 1–170, 320–460, 596–838 read directly; lines 170–320 and
  460–596 verified via the full print-text read (same strings) plus the programmatic
  appendix/key comparison (§1).
- **Web PDF:** extracted text is byte-identical to the print text (112,893 bytes each);
  web SHA unchanged during the read (see §4), so the web verdict stands (not deferred).

## 4. SHAs (start = end; nothing changed during the read)

| file | SHA-256 (start and end) | bytes | vs KIT §5 |
|---|---|---|---|
| `2026-w47-ru-it.text.md` | `0bb5739a9e2a1215074b8d5cba566736e88cd84d45f3bc28eb0fe5a8966f5989` | 63,972 | — (expected value per brief; matches) |
| `Lucerna-VOL4-ru-it.pdf` (print) | `c69b7bdf3165ed24f05be8004559e0102c0c8e38f15e395bc32360094628359b` | 21,265,865 | **matches KIT** |
| `Lucerna-VOL4-ru-it-web.pdf` (web) | `b994d11ff9c219c7900b53b2eca377a345e49a45f97e9ea691fc51712bd1ac14` | 3,384,121 | **differs from KIT** (`91028029…`, 3,384,095 B) — known drift: the concurrent pre-insert web-PDF rebuild rewrote all 9 ru web PDFs (recorded in the KIT Fix-1 note). Web text verified identical to print, so this is a KIT-sync item for the coordinator, not a content defect. Print SHA did not change mid-read. |

## 5. Observation (NOT counted as findings) — systematic narrow word spacing

The renderer puts a space-only `<text>` element between separately positioned words,
and that space is narrow everywhere: ~21 further junctions measured 7–13 px at
200 dpi (2.5–4.7 pt) — readable, but tight. Examples (all verified present as a
space, not fused): byline `От редакции Lucerna` (10 px, every page), P2
`Константин Юон` 9 px / `рождения Деда` 7 px / `ноябрьской погоде` 12 px,
Nota boxes (`поздравить fare` 8 px, `биография biopic` 13 px,
`криминальная poliziesco` 10 px, `экранизация adattamento` 10 px,
`календарная дата` 8 px, `примерки provare` 12 px,
`технику elettrodomestici` 8 px), P7 glosses (`оттепель disgelo` 10 px,
`промокод codice` 8 px, `распродажа grande` 10 px, `синоптики обещают` 11 px),
P5 header `скидки с` 8 px, P6 `редакции для` 9 px, P1 `Главные темы` 7 px,
`лицензия CC0` 7 px, P5 caption `достояние (Wikimedia` 8 px.
These are disclosed so the coordinator can judge whether the renderer wants a
spacing pass; they are not findings because a reader can still see the space.
The six findings in §2 are the spots where the gap falls to or below the letter
spacing and the words actually fuse. The same mechanism almost certainly affects
the other ru editions (shared renderer) — a sweep is suggested but out of scope
for this verdict.

## 6. Method & files

- Read-only. No production file modified; no lint/commit/push; no re-render.
- Print PDF: `pdftotext -layout` full text (all 8 pages) + 100 dpi full-page
  renders (all 8) + 200 dpi renders (P2 full; P1/P3–P8) + 200 dpi crops of every
  finding. Web PDF: full text extraction (identical to print). text.md: direct
  reads (§3) + programmatic appendix/P8 key comparison + SHA check.
- Poppler merges a word pair into one text-layer "word" when the gap is below its
  threshold; that alone was **not** treated as a defect — each candidate was
  measured in ink (200 dpi) and, for the six findings, visually confirmed.
  Counter-example kept in mind throughout: P2 `Профессиональные праздники`
  is merged by poppler yet renders with a clear visible space (8 px, crop-verified).
- This note is the only file written:
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-ru-it1/PROOF-NOTE.md`
  Working renders/extractions live only in `/tmp/ru-it-proof/` (ephemeral, ~22 MB).
