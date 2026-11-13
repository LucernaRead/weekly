# PROOF NOTE — 2026-w47-ru-de (independent re-proof, second re-proof round)

- Edition: **2026-w47-ru-de** (Russian source, German explanations, VOL.4)
- Proofer: independent (did not build this edition; did not run the earlier re-proof)
- Date: 2026-11-11 ~22:46–23:15 EST
- Scope read: full text.md (838 lines) + all 8 pages of the print PDF (text layer,
  100 dpi full-page renders, 200 dpi crops of suspect lines) + web PDF (text layer,
  diffed against print) + the earlier proof note in this same path (see §0).

## §0 Relation to the earlier note in this path — SUPERSEDED, preserved here

This path previously held a proof note (fix1 re-proof round) with verdict **(a) ZERO
FINDINGS**. I read it in full before writing this note. Its §12 adjudicated the
tight word spacing as non-defect ("core同位" — same nodes as core; "400 dpi confirmed
gaps exist"; HINWEIS pairs attributed to a U+3000 separator + word shape).

This re-proof **disagrees with that adjudication**, on new evidence the earlier round
did not have:

1. **Shipped control**: W43 and W46 ru-de web PDFs (same measurement method) have
   **0** such joins and real space characters — e.g. "редакции Lucerna" ×6,
   "Профессиональные праздники" ×3 in W46. The W47 spacing is a **regression**, not
   house style. "Same as core" is true but does not exonerate: W47 **core-ru itself**
   carries the defect (byline "редакцииLucerna" ×6, "Профессиональныепраздники" ×4).
2. **Mechanism**: the earlier note's U+3000 explanation is wrong for these pairs.
   In the SVG the separator is a plain U+0020 element (e.g. P2 HINWEIS line:
   `'поздравить'` x=670.2, `' '` x=788.4, `'gratulieren ·'` x=793.0). The U+3000s
   in the SVG are header/footer furniture, not word separators. The space element is
   placed after an **under-measured Cyrillic width** (the word's ink extends ~2.8
   units past the space element's x), so its effective advance collapses — and the
   delivered PDFs contain **no space character at all** at these boundaries.
3. **Standard**: "a gap exists at 400 dpi" is not the bar. On the same lines, same
   font/size, real spaces measure **2.78–4.36 pt** of blank; the joins measure
   **0.63–2.65 pt**, 38 of them under 1.5 pt at 15.4 pt type. A 0.63 pt gap is not a
   word space by any normal standard, and the fused forms are visible at reading size.

The earlier note's other results (D1 fix verified, 150 keys hand-checked, 16 gates
green) are not disputed; where this note re-verifies the same items it agrees. Only
the spacing adjudication differs, and it changes the verdict.

## VERDICT: (b) FINDINGS — one defect class, 131 occurrences

One systematic defect class in the delivered print AND web PDFs: **missing word
spaces**. At 131 word boundaries the PDF has no space character where text.md has
one, and the rendered gap is far below a normal inter-word space. All other content
checks pass (see "What passed"). The L836 fix itself is verified correct (see below).

## SHA-256 (start = end; nothing changed mid-read)

| File | SHA-256 | Size |
|---|---|---|
| `2026-w47-ru-de.text.md` | `d0f9b48c8fab4df8bb39acfdfebfbc6ad6cf0f09e75891449d13a0f1ce2dcc0f` | 63,471 B |
| `Lucerna-VOL4-ru-de.pdf` (print) | `872b4f1c05d682f4f8a18749b7d63215a09bc2a151c3ca1601ef454de4019ebd` | 21,231,616 B |
| `Lucerna-VOL4-ru-de-web.pdf` (web) | `9aad0067943c7b8cac9263983409b6b5b3e452be249acd0094d675171d6c43b7` | 3,385,861 B |

- text.md SHA matches the expected value in the brief exactly; size 63,471 B.
  No STOP condition triggered.
- Print SHA did **not** change mid-read (print was not rebuilt by the fix — confirmed).
- Web SHA did **not** change between start and end reads, so the web-PDF check is
  NOT deferred: the web verdict below is on the final file.
- KIT drift (for the coordinator's KIT-sync wave, NOT a finding on its own): the KIT
  §4 print SHA (`26bfbcd1…`, 21,231,822 B) and web SHA (`99173b8c…`, 3,385,962 B) both
  differ from the on-disk SHAs above. Print was rebuilt 16:44 UTC, KIT never updated.
  Content verified directly from the on-disk files.

## The L836 fix — VERIFIED

- text.md L836 reads exactly: `150. ✓ Mustertext in Abschnitt H dieser Seite (97 Wörter)`
- Printed P8 answers appendix reads exactly the same line (P8 text layer and visual
  render): `150. ✓ Mustertext in Abschnitt H dieser Seite (97 Wörter)`
- The Mustertext ("Пример: Моя неделя 16–22 ноября …") counts **97 words** —
  the "(97 Wörter)" claim is correct.
- The fix is confined to L836; the full read found no other anomaly attributable to it.

## FINDING F1 — Missing word spaces (print + web PDFs)

### What it is

Words are drawn as separate `<text>` elements positioned by measured width (SVG
source). At 131 boundaries the following word starts too early: the PDF text layer
contains **no space character**, and the ink-to-ink gap is far below a normal space.
Baseline measured on the same lines, same font/size: real space glyphs are
**2.78–4.36 pt** wide, and the ink-to-ink blank across a real space equals the
space glyph width (verified: adjacent-char gaps are 0.00 pt around a space char —
the space glyph's own box spans the blank). Measured gaps at the 130 measured joins
(of 131 boundaries — see Table B note):

- **37 measured occurrences < 1.5 pt** — words visually fused (Table A; the P4
  byline's second boundary is the same construction and was not separately measured)- **79 occurrences 1.5–2.5 pt** — visibly tight, well under a normal space
- **14 occurrences ≥ 2.5 pt** — thin but visible

Normal spaces elsewhere on the same pages render correctly (e.g. "Татьянин день",
2.65 pt gap, renders as a clear space in a 200 dpi crop), so this is not font-wide
tightness — it is a systematic under-measurement of the preceding (overwhelmingly
Cyrillic) word's width. It hits body text, HINWEIS gloss boxes, bylines, headers,
exercise stems and the P8 answers appendix on all 8 pages.

### Proof it is a regression, not house style

- Shipped **W43** and **W46** ru-de web PDFs: **0** Cyrillic↔Latin script-boundary
  joins (same method). This edition: **32** in print, **32** in web.
- All other W47 ru-* web PDFs show the same defect (~30–33 script joins each:
  ru-en 33, ru-fr 31, ru-es 30, ru-it 31, ru-pt 30), and W47 **core-ru** itself has
  7 script joins. The defect is W47-wide and upstream of this edition's text.md fix;
  it is not caused by the L836 change. (The fix must therefore land in the shared
  renderer / core build, not in this edition's content files.)
- Print-vs-web text is byte-identical (`diff` of pdftotext output empty), so the
  defect is in both deliverables, not in one conversion path.
- Consequence beyond appearance: copying text out of either PDF yields fused words
  ("Профессиональныепраздники", "редакцииLucerna"), which also breaks text search
  and the site's PDF-fallback text extraction.

### Worst instances (gap < 1.5 pt, Table A)

| Page | Joined as printed | Should read | Gap |
|---|---|---|---|
| P3 | криминальнаяKrimi- | криминальная Krimi- | 0.63 pt |
| P3 | кинозрителяKinobesucher | кинозрителя Kinobesucher | 0.74 pt |
| P1 | метеорологическаязима | метеорологическая зима | 0.91 pt |
| P3 | экранизацияVerfilmung | экранизация Verfilmung | 1.00 pt |
| P8 | заказываетподарок (×3) | заказывает подарок | 1.05 / 1.13 / 1.25 pt |
| P1–P6 | редакцииLucerna (byline, ×6) | редакции Lucerna | 1.10 pt |
| P2 | рожденияДеда | рождения Деда | 1.13 pt |
| P6 | редакциидля | редакции для | 1.20 pt |
| P8 | заказываюподарок | заказываю подарок | 1.20 pt |
| P8 | начинается16 | начинается 16 | 1.22 pt |
| P5 | календарнаядата | календарная дата | 1.23 pt |
| P8 | Устойчивыйснег | Устойчивый снег | 1.26 pt |
| P8 | Промокоддействует | Промокод действует | 1.29 pt |
| P2 | Профессиональныепраздники | Профессиональные праздники | 1.30 pt |
| P8 | выходят19 | выходят 19 | 1.30 pt |
| P8 | возвращаютпокупки | возвращают покупки | 1.30 pt |
| P2 | поздравитьgratulieren | поздравить gratulieren | 1.31 pt |
| P8 | КогдаДень | Когда День | 1.31 pt |
| P7 | можетбыть | может быть | 1.32 pt |
| P8 | Сначаласписок | Сначала список | 1.33 pt |
| P8 | начинается15 | начинается 15 | 1.34 pt |
| P6 | Профессиональныепраздники | Профессиональные праздники | 1.35 pt |
| P8 | поздравляетдруга (×2) | поздравляет друга | 1.36 / 1.41 pt |
| P7 | Профессиональныепраздники | Профессиональные праздники | 1.40 pt |
| P8 | поздравляетво | поздравляет во | 1.40 pt |
| P7 | распродажаAusverkauf | распродажа Ausverkauf | 1.41 pt |
| P8 | Сколькорабочих | Сколько рабочих | 1.44 pt |
| P8 | Сколькоочков | Сколько очков | 1.44 pt |
| P8 | поздравляюдруга | поздравляю друга | 1.47 pt |

Visually confirmed at 200 dpi (no visible space): P1 "зона вылетаdie
Abstiegszone" (1.88 pt), "момент сдачиbei Redaktionsschluss", "в историиzum";
P2 "родинаHeimat", "поводAnlass"; P4 "поправкаBerichtigung"; P8 section header
"ЧИТАЙТЕИ ОТВЕЧАЙТЕ". Control: "Татьянин день" (2.65 pt) renders as a clear space.

### Full census (Table B — 107 two-word types + 1 three-word type; 131 boundaries)

Method: PDF tokens split against the text.md vocabulary; every token that is the
concatenation of two text.md words, gap measured per occurrence with PyMuPDF char
bboxes. Excluded: "einer" (P8, gap 0.0 — a real German word, false positive of the
split test, not a join). The raw census counted 130 occurrences including that false
positive; the true total is 131 missing-space boundaries: 129 two-word joins plus
the P4 byline token `спортивнойредакцииLucerna` (three words, two boundaries —
`спортивной→редакции` and `редакции→Lucerna`, the latter measured at 1.10 pt).

| Joined token | × | Joined token | × | Joined token | × |
|---|---|---|---|---|---|
| редакцииLucerna | 5 | Профессиональныепраздники | 4 | Голодныеигры | 3 |
| Проверьтесрок | 3 | заказываетподарок | 3 | Устойчивыйснег | 2 |
| Сколькоочков | 2 | Международныйдень | 2 | предложенияпо | 2 |
| возвращается20 | 2 | сначаласписок | 2 | всегдазначит | 2 |
| возвращаютпокупки | 2 | поздравляетдруга | 2 | завершился14 | 1 |
| результатэтого | 1 | вылетаdie | 1 | историиzum | 1 |
| метеорологическаязима | 1 | двадцатыечисла | 1 | забудьтетёплую | 1 |
| Когдасборная | 1 | Когданачинается | 1 | рожденияДеда | 1 |
| главныйстуденческий | 1 | Татьяниндень | 1 | преподавателявысшей | 1 |
| налоговыхорганов | 1 | поздравитьgratulieren | 1 | родинаHeimat | 1 |
| главноежелание | 1 | успеховErfolg | 1 | пожелаетестуденту | 1 |
| 17ноября | 1 | выходятсразу | 1 | документальныйфильм | 1 |
| ЭлизабетХолмс | 1 | основательницестартапа | 1 | сказочноефэнтези | 1 |
| биографияFilmbiografie | 1 | криминальнаяKrimi | 1 | ВладимираМаяковского | 1 |
| сначалаодин | 1 | экранизацияVerfilmung | 1 | кинозрителяKinobesucher | 1 |
| Сколькопремьер | 1 | напечаталитолько | 1 | внимательнымчитателям | 1 |
| сравнялисчёт | 1 | поправкаBerichtigung | 1 | вылетаin | 1 |
| Результатна | 1 | Сколькоматчей | 1 | 20ноября | 1 |
| маркетплейсахскидки | 1 | начинаютсяуже | 1 | распродажагода | 1 |
| заказываютнесколько | 1 | промокодына | 1 | действуютобычно | 1 |
| календарнаядата | 1 | подошёлpasst | 1 | примеркиAnprobe | 1 |
| Распродажа11 | 1 | прошломгоду | 1 | бытовуютехнику | 1 |
| Неделя16 | 1 | приходятименно | 1 | Проверьтепосылку | 1 |
| примерьтепокупку | 1 | забудьтевернуть | 1 | честныеrichtige | 1 |
| серединаdie | 1 | редакциидля | 1 | Фокусна | 1 |
| Триуровня | 1 | Гололедицаопасна | 1 | будьтеосторожны | 1 |
| оттепельTauwetter | 1 | мокрыйснег | 1 | промокоддействует | 1 |
| распродажаAusverkauf | 1 | скидкаRabatt | 1 | промокодRabattcode | 1 |
| Когдафакт | 1 | хорошегоуровня | 1 | даннымlaut | 1 |
| можетбыть | 1 | современногорусского | 1 | литературногоязыка | 1 |
| забили21 | 1 | Настоящихписем | 1 | Результатматча | 1 |
| Большойтест | 1 | КогдаДень | 1 | Сколькорабочих | 1 |
| 13ноября | 1 | поздравляетво | 1 | результатматча | 1 |
| поздравляюдруга | 1 | хорошуюзиму | 1 | заказываюподарок | 1 |
| начинается15 | 1 | выходят19 | 1 | Сначаласписок | 1 |
| начинается16 | 1 | Промокоддействует | 1 | | |

(The remaining 79 tight 1.5–2.5 pt and 14 thin ≥2.5 pt occurrences are distributed
across the same token list; per-occurrence gaps were measured, worst 37 in Table A.
The P4 byline token `спортивнойредакцииLucerna` ×1 is the 108th type; its
`редакции→Lucerna` boundary (1.10 pt) is the 6th byline entry in Table A, and its
`спортивной→редакции` boundary is the 131st boundary — total byline joins: 6
bylines, one per page P1–P6.)

### Impact on the appendix-key check

Appendix keys 1–150 in text.md match the printed P8 keys **in content, 150/150**.
Three keys fail a *verbatim* match only because of this same spacing defect in the
printed answers (content otherwise identical):

- 35: print `рассказывает— рассказывать→ рассказывает` (spaces around —/→ missing)
- 82: print `Verneinter Imperativ:не спешите` (space after colon missing)
- 140: print `… —поздравляю + с + Instrumental` (space after — missing)

The P8 extract comparison (non-layout) confirms 147/150 verbatim, 3/150 spacing-only.

## Page-by-page notes

- **P1**: lead + stats box + "СЕЙЧАС ВЫ" Q1–6 + Blitzquiz Q7–10 all correct. F1:
  byline, gloss box (3 pairs), "метеорологическаязима", "Устойчивыйснег",
  "Когдасборная", "Когданачинается", "забудьтетёплую", "двадцатыечисла",
  "результатэтого", "Сколькоочков". Word of the week «чёрная пятница» correct.
  No overflow/overlap.
- **P2**: article, holidays list, "СЛОВА НЕДЕЛИ" (4 words), Q11–28 correct. F1:
  byline, HINWEIS (3 pairs), body joins incl. "Профессиональныепраздники",
  "Татьяниндень", "рожденияДеда", "Международныйдень", "17ноября". No overflow.
- **P3**: cinema article + Q29–46 correct; "Голодные игры" 26 Nov correct. F1:
  byline, both HINWEIS boxes (5 pairs incl. worst 0.63 pt), "ЭлизабетХолмс",
  "документальныйфильм", "Сколькопремьер". Large mid-column white space is the
  core layout (per earlier note), not a defect.
- **P4**: sport article, VOL.3 correction, 8-result table, national-team box,
  15th-tour fixtures, Q47–64 — all correct and mutually consistent. F1: header
  kicker, byline, HINWEIS (3 pairs), "внимательнымчитателям", "Результатна".
  No overflow.
- **P5**: Black Friday article, 11.11 box, dates box, Q65–82 correct; 14.4M orders,
  Ozon/WB/M.Video/Yandex/Lamoda dates all consistent. F1: byline, HINWEIS
  (4 pairs + "бытовуютехнику", "прошломгоду"), "маркетплейсахскидки",
  "начинаютсяуже", "заказываютнесколько". No overflow.
- **P6**: week essay, calendar strip 16–22 (21–22 highlighted), chart 38/26/18/18
  = 100 labelled as practice data, Q83–100 correct. F1: byline, HINWEIS
  (3 pairs), "Профессиональныепраздники", "редакциидля", "Неделя16". No overflow.
- **P7**: language focus A2/B1/B2 + error clinic + letters box + weekly phrases +
  VOL.5 teaser, Q101–112 correct; the letters-box disclosure (no real letters, editor
  example, promise carries to VOL.5) present in Russian and German. F1: heaviest
  page — gloss lines (13 pairs), "Профессиональныепраздники" (phrase 3),
  "Фокусна", "Триуровня", "можетбыть", Pushkin caption joins, "забили21 гол".
  No overflow/overlap.
- **P8**: test Q113–150 + answers appendix 1–150 all present; Q150 ✓ form correct;
  Mustertext 97 words. F1 heaviest in exercise stems + answers: "ЧИТАЙТЕИ
  ОТВЕЧАЙТЕ" header, "заказываетподарок" ×3, "поздравляетдруга" ×2,
  "начинается15/16", "Сначаласписок", "Промокоддействует", keys 35/82/140
  spacing-only. No overflow; min font 9.75 pt per earlier measurement (not re-measured).

## What passed (checked, no findings)

- **L836 fix**: exact match with P8, Mustertext = 97 words (counted).
- **Appendix keys 1–150**: content matches printed P8, 150/150 (see F1 note above).
- **Exercise stems 1–150**: read in full in text.md and in the print PDF (P1–P8);
  stems, options, levels (A2/B1/B2) and answer keys agree. Spot-verified facts:
  Q54 Krylja–Orenburg 2:0, Q56 Anstoß 20:45, Q49 83. Minute — all match the P4
  results table and the VOL.3 correction.
- **German**: no German language errors found in headlines, glosses, instructions
  or answers (other than the missing spaces in F1). Q137–140 translations verified
  against the printed P8 answers.
- **Weekly words**: P1 «чёрная пятница» box and P7 «распродажа» box both present
  and matching text.md.
- **Captions / images**: P1 park photo, P2 Yuon «Зима. Ростов», P4 1912 football
  photo, P5 market photo, P7 Pushkin portrait — all present, captioned correctly,
  no overlap.
- **Layout**: all 8 pages rendered and read visually; no overflow, overlap,
  clipping or tofu anywhere; footers "Seite N von 8" correct.
- **Web PDF**: text layer identical to print (diff empty); 8 pages; 3,385,861 B < 7 MB.

## Observations (not findings)

1. **Morozko caption (text.md L838) not printed.** text.md ends with
   `*«Морозко»: иллюстрация Ивана Билибина, 1932 год. Зимняя сказка — к ноябрю.*`
   Neither the image nor the caption appears in print or web PDF. The builder's KIT
   records the Morozko image as SKIPPED by the build's own condition, "by design,
   not a defect" (and the earlier proof note records the same for shipped W46 ru-de).
   I record the divergence and do not count it as a finding; the caption text itself
   is factually correct (Bilibin, 1932).
2. **KIT SHA drift** (print + web) — see SHA section; coordinator KIT-sync item.
3. The KIT's keydiff note `[137, 138, 139, 140]` (p8 extract vs core) is explained:
   Q137–140 are translations into German; the printed P8 values match text.md.
   No separate finding.

## Recommendation for the coordinator

F1 needs a renderer/core fix and a rebuild of the print + web PDFs. Root cause is
upstream of this edition: the per-word SVG positioning under-measures Cyrillic
widths (space element placed too early; the space character vanishes in the
delivered PDFs). Since the defect is W47-wide (core-ru + all ru-* fan-outs at
~30 script joins each), the fix should land in the shared renderer / core build and
the whole ru family should be rebuilt and re-proofed; whether other target families
(de-*, en-*, …) share the renderer change is worth one check with the same census
before the week is declared clean. This edition's text.md needs no change.
Re-proof after rebuild should re-run the same census (PDF token-split against
text.md vocabulary + PyMuPDF gap measurement) and confirm 0 joins; the shipped
W43/W46 issued PDFs (0 joins) are the control.

## Method note

Read-only. No production file modified, no render, no lint, no commit. Proof
artifacts: this file only. Working files in /tmp (PDF text dumps, 100/200 dpi
renders) are disposable.
