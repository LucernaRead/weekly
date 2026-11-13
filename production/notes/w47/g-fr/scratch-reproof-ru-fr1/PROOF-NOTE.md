# PROOF NOTE — 2026-w47-ru-fr (independent re-proof, Round 2)

- **Edition:** 2026-w47-ru-fr (Russian text, French explanations, VOL.4)
- **Proofer:** independent (did not build this edition)
- **Date:** 2026-11-11
- **Verdict: (b) — TWO MINOR FINDINGS** (both pre-existing, neither in the changed line).
  The L836 fix itself is verified correct (see §1).

## SHAs (start = end; nothing changed mid-read)

| File | SHA-256 | Bytes |
|---|---|---|
| `2026-w47-ru-fr.text.md` | `821038d900d2e8e622e964ada030e794c35a6698df6a498e26079c93931aaf0e` | 63,498 |
| `Lucerna-VOL4-ru-fr.pdf` (print) | `8f09a2703081f12b76ace75331a79b5c4507282894b119298e68b7ce77c83562` | 21,291,969 |
| `Lucerna-VOL4-ru-fr-web.pdf` (web) | `0c708aa1f501315fffec95c7ac0cbefe8df0e5a4bac2f14049106416420008c2` | 3,385,798 |

- text.md SHA matches the required value exactly (`821038d9…`, 63,498 B) — the fix is the file on disk.
- Print SHA matches the KIT §5 line. Print did NOT change during the read.
- Web SHA differs from the KIT §5 line (`45f6401d…`, 3,385,758 B) — **KIT drift, not a defect**:
  known concurrent web-PDF rebuild rewrote all 9 ru web PDFs (see KIT Fix 1 note).
  The web PDF on disk was stable across my whole read (same SHA at start and end),
  is 8 pages, same page size as print, and its text layer is **byte-identical** to the
  print text layer (`cmp` clean, 112,049 bytes each). Coordinator to reconcile the KIT
  web SHA in the KIT-sync wave.
- Web-PDF check: NOT deferred — the file was stable and fully checked via its text
  layer (byte-identical to print) + pdfinfo (8 pages). Visual read was on the print
  PDF, the authoritative rendering.

## 1. The L836 fix — VERIFIED CORRECT

- text.md L836 is exactly: `150. ✓ Voir le texte modèle dans la section H de cette page (97 mots)`
- Printed P8 answer key (pdftotext raw, line 291) is byte-identical:
  `150. ✓ Voir le texte modèle dans la section H de cette page (97 mots)`
- The section-H model text ("Моя неделя 16–22 ноября…") counts **exactly 97 words**,
  within the stated 80–100 range; its Russian is correct.
- The old long form (`150. (Question ouverte, texte modèle ci-dessous) — …`) is gone
  from the appendix. (It still appears as the exercise statement's key on the section-H
  exercise line L663 — that is the exercise line, not the appendix; the appendix is
  what must match P8, and it does.)
- Print/web PDFs were NOT rebuilt by this fix (SHAs above; print matches KIT).

## 2. Appendix keys 1–150 vs printed P8 keys — ALL MATCH

- Appendix in text.md: keys 1–150, none missing.
- Printed P8 answer key extracted (pdftotext raw, answer-key region): 150 entries,
  none missing. Every key matches the appendix key (same answer + same note text).
  The raw diffs first flagged (Q34/35/43/61/70/72/73/79/80/81/92/95/100/105/107/108/
  133/135/136/139/140/150) were all pdftotext segmentation artifacts — missing spaces
  around `→`/`:` and `— СТРАНИЦА N —` headers bleeding into entries in raw mode —
  not real differences; keys themselves match in every case (verified entry by entry).
- All 150 exercises (stems + inline keys, incl. the 20 matching items 25–28/39–42/
  57–60/75–78/141–144) agree with the appendix and with the printed P8 keys.
- Exercises are numbered 1–150 continuously with no gaps; answer key is grouped
  correctly by page (P1: 1–10, P2: 11–28, P3: 29–46, P4: 47–64, P5: 65–82, P6: 83–100,
  P7: 101–112, P8: 113–150).

## 3. Page-by-page notes (print PDF, all 8 pages read visually at 100 dpi)

- **P1** — Masthead, kicker, lead (14-й тур, «Зенит»/«Динамо» 31 pt), French gloss,
  "ТУР В ЦИФРАХ", exercises 1–6 + quiz 7–10, park photo + caption, weather box,
  "В ЭТОМ НОМЕРЕ" (Стр. 2–8 all match actual pages), word of the week
  («чёрная пятница»). No overflow/overlap/clipping/tofu. Dates check out
  (12 Nov = Thursday, 17 Nov = Tuesday; тур 6–8 Nov; WB 16 Nov; 15-й тур 20 Nov).
- **P2** — Student Day / Ded Moroz / weather; holidays list 16–22 Nov; words of the
  week (оттепель / мокрый снег / ледяной дождь / гололедица) with correct French
  glosses; Yuon «Зима. Ростов» image + caption; exercises 11–28. Keys correct
  (Q20 `желании` — correct prepositional; Q22 16:20; Q25–28 matching correct).
- **P3** — Cinema 19 Nov, five premieres; exercises 29–46. Keys correct
  (Q33 26 Nov Hunger Games; Q38 `ноября` genitive; Q43–46 sentence building).
- **P4** — 14-й тур results table (8 matches) + correction note re VOL.3
  («Балтика» — «Динамо» Мх 0:1, 8 Nov, 20:45) + 15-й тур fixtures (8 matches) +
  national-team box + 1912 photo + caption; exercises 47–64. Table, article and
  keys all agree (Q52 0:1, Q53 2:2, Q54 2:0, Q55 0:1, Q56 20:45, Q57–60 matching,
  Q61–64 verb forms: сыграли / будет / играет / победило — all correct).
- **P5** — «Чёрная пятница» dates (Ozon 13 Nov–2 Dec, WB 16–30 Nov, М.Видео from
  12 Nov, Яндекс Маркет 25–27 Nov, Lamoda 27–30 Nov, Cyber Monday 30 Nov) agree
  across article, dates box and keys (Q65–69); 11.11 box (14.4M orders) and
  Q73 `заказов` agree; market photo + caption; exercises 65–82.
- **P6** — Week 16–22 Nov; calendar strip 16 пн–22 вс with 21–22 highlighted as
  weekend; chart 38/26/18/18 = 100 with correct keys (Q83 B=2, Q84 5, Q85 B,
  Q86 26, Q87 18); disclaimer "Это учебный опрос редакции… — не настоящая
  статистика / Ceci est un sondage d'exercice…" present. Month claim
  "В ноябре 20 рабочих дней и 10 выходных" VERIFIED against the 2026 production
  calendar (Nov 2026: 21 weekdays − 4 Nov Unity Day holiday = 20 working days;
  9 weekend days + 4 Nov = 10 days off; 4 Nov 2026 is a Wednesday). Exercises 83–100.
- **P7** — Three levels (A2 weather / B1 shopping / B2 attribution); 4 errors with
  correct corrections (с + instrumental, на + prepositional, 21 + гол, с + genitive);
  Pushkin/Kiprensky portrait + caption; letters box (no real letters, editorial
  example, promise moved to VOL.5 — consistent with P2 "А ВЫ?" box); 8
  "ФРАЗЫ НЕДЕЛИ" quotes all verbatim from pages 1–6 with correct French
  translations and page numbers; "СЛЕДУЮЩАЯ НЕДЕЛЯ" band. Exercises 101–112.
- **P8** — Big test 113–150 (A chronicle 8, B general 8, C Masha reading 4,
  D sentences 4, E translation 4, F matching 4, G shop dialogue 5, H writing 1 +
  97-word model text) + complete answer key 1–150 ending with the ✓ Q150 line.
  No Morozko image — per KIT this is the build's own conditional skip (keys end
  col 3 y=2301.84), same as W46 ru-fr; the page itself is complete and clean.
  Footer "Page 8 sur 8", no overflow.

## 4. Word spacing — investigated, NOT a defect

While reading the 100-dpi renders I suspected joined words
("метеорологическаязима", "От редакцииLucerna", etc.). I checked the rendered
PDF at 300 dpi by direct pixel measurement instead of trusting the downscaled view:

- P1 "метеорологическая | зима": gap 8 px = **2.56 SVG units** (present, narrow;
  normal space on that line ≈ 5.5–7.4 units). "От редакции | Lucerna" (byline):
  gap 15 px = **4.8 units** — a full normal space.
- P6 disclaimer "настоящая | статистика": PDF word boxes give a 1.49 pt gap
  = 1.99 units (present). P7 "(Страница | 1)": 1.755 pt = 2.34 units (present).
  **Direct pixel measurement on the 300-dpi renders (received after the first
  draft of this note) is better still: P6 "настоящая → статистика" = 14 px =
  4.48 units; P7 "Страница → 1)" = 18 px = 5.76 units — both full normal spaces
  (control P6 "учебный → опрос" = 5.12 units). The PIL-based estimates that
  flagged these two boundaries (-0.95u / -0.42u) were pessimistic; the rendered
  ink gaps are normal.** (One approximate probe, "P7 right-col (Страница zone",
  returned 0 px because its xB was a guess, not a verified run start — not evidence.)
- SVG geometry (PIL metrics): of 1,948 true word→word boundaries, only 16 measure
  < 1 unit, all in small grey caption/disclaimer text; direct pixel measurement of
  the tightest flagged cases shows normal gaps (4.48u and 5.76u, §4 above) — the
  PIL estimates were pessimistic. The single narrowest pixel-measured gap in the
  edition is P1 "метеорологическая | зима" at 2.56 units: tight but legible.
- Cause (for the record, not a finding): Cairo renders ≈1.5% wider than the PIL
  metrics the layout used, so the tightest spaces compress to ≈2 units. All words
  remain separated and legible; pdftotext merges some pairs only because its
  word-split threshold is coarse. No touching/overlapping words were found.

## 5. FINDINGS (2, both minor, both pre-existing — not from the L836 fix)

### F-1 (minor) — Q126 answer note: "Selon les météo" should be "Selon la météo"
- **Where:** print P8 answer key, web PDF, text.md L616 (exercise key) and L812
  (appendix): `126. B — Selon les météo : pluie et neige mouillée`
- **Evidence:** "météo" is feminine singular → "Selon la météo". The phrase is
  identical in print, web and text.md, so it is a source-text error, not a
  rendering issue. Answer-key note only; the exercise, the key letter (B) and
  the Russian stem are all correct. Likely lives in core-ru (P8 test item), so a
  fix would be core-level and affect the other ru fan-outs — coordinator's call.

### F-2 (minor) — Dangling Morozko caption in text.md
- **Where:** text.md line 838 (last line):
  `*«Морозко»: иллюстрация Ивана Билибина, 1932 год. Зимняя сказка — к ноябрю.*`
- **Evidence:** "Морозко" occurs 0 times in the print PDF, 0 times in the web PDF
  and 0 times in all 8 SVGs. The image skip itself is by design per the KIT
  (keys end col 3; image doesn't fit), but the caption line in text.md describes
  an illustration that is not in the edition. text.md is the site body, so site
  readers see a caption for a picture that isn't there. The other five image
  captions in text.md (P1 park, P2 Yuon, P4 1912 team, P5 market, P7 Pushkin)
  all have their images on the page — Morozko is the only dangling one.
  Fix: drop the line from text.md (or the exporter should skip the caption when
  the image is skipped).

## 6. What was checked in full

- Read all 8 print-PDF pages visually + full text.md (838 lines) + web PDF
  (byte-identical text layer, 8 pages, same dimensions).
- French: every gloss, instruction, exercise label and answer note read; Russian:
  every article, caption, exercise stem and key read. One French error found (F-1).
- Facts spot-verified: Nov 2026 calendar (20 working / 10 off, incl. 4 Nov Unity
  Day, Wednesday — production calendar 2026, corroborated by multiple sources);
  14-й тур results vs table vs keys; Black Friday dates across article/box/keys;
  chart sums to 100; model text word count = 97; P7 phrases verbatim vs source pages.
- No overflow, overlap, clipping or tofu on any page; footers/masthead correct on
  all pages ("Page N sur 8"); P8 answer key complete to Q150.
- The two background items in the brief: print SHA never changed (no rebuild);
  web SHA was stable across the whole read, so no deferred web verdict was needed.

## Files / scratch

- Proof note (this file): `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-ru-fr1/PROOF-NOTE.md`
- Scratch renders (ephemeral, /tmp): `/tmp/rufr/p-*.png` (100 dpi, P1–P8),
  `/tmp/rufr/hi1-1.png`, `hi-6.png`, `hi-7.png` (300 dpi),
  `/tmp/rufr/zoom_meteo.png`, `zoom_byline.png`, `print.txt`, `web.txt`,
  `p8raw.txt`, `bbox.html`.
- No production file was modified; no commit/push/lint run; nothing copied out of
  the production directory except the /tmp text extractions above.
