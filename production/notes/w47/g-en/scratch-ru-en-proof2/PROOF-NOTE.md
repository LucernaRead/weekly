# PROOF NOTE — 2026-W47 ru-en, Proof 2 (independent, from scratch)

- Edition: `2026-w47-ru-en` (Russian target × English reader), VOL.4, issue 16–22 November 2026
- Proofer: proof2 (independent of fix1); 2026-11-11
- Work dir (read-only use): `~/workspace/weekly-git/production/2026-w47/2026-w47-ru-en/`
- Core对照 (actual path): `~/workspace/weekly-git/production/2026-w47/core-ru/`
  (the brief's path `2026-w47-ru/` does not exist; `core-ru` is the core dir)
- Notes dir (intended): `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ru-en-proof2/`
- **BLOCKER — disk quota:** `/home` hit `Disk quota exceeded` (EDQUOT) from ~08:58 UTC
  (df shows 45G free on the filesystem — this is a user quota cap, not a full disk).
  Per the brief, all `/home` writes stopped immediately on EDQUOT; nothing was hammered,
  nothing was deleted to free space. This note + GATE-LOG.md are therefore written to the
  `/tmp` fallback mirror `/tmp/scratch-ru-en-proof2/` (tmpfs, 195M free, writable).
  Files already written to the intended dir BEFORE the quota hit are still there:
  `probe.txt`, `fullscan.py`, `scan.json`, `scan-out.txt`, `txt/print.txt`, `txt/web.txt`,
  `p1-teaser-print.png`, `p1-teaser-web.png`, `p1-headline-*.png`.
  No source was edited, nothing rebuilt, no commit, no push (per the brief).

## 0. Identity — SHA checks (BOTH PASS)

| PDF | Bytes | SHA-256 (first 16) | Expected | Result |
|---|---|---|---|---|
| `Lucerna-VOL4-ru-en.pdf` (print) | 21,245,374 | `7b73070c2c11313a` | `7b73070c2c11313a` | **MATCH, 8 pages** |
| `Lucerna-VOL4-ru-en-web.pdf` (web, patched-tool rebuild) | 3,367,620 | `82dfb6eaeff6eaa7` | `82dfb6eaeff6eaa7` | **MATCH, 8 pages** |

Page size 1462.5 × 2025 pts, PDF 1.7, both 8 pages (`pdfinfo`).

## Verdict: (b) — ONE defect cluster, web PDF only (D3). Print PDF: zero defects.

The print PDF passed every check below with no finding. The web PDF has a single
defect cluster on P1 (one line, three facets of the same root cause). No other defect
was found in either PDF. D1 is fixed; all 7 original D2 spots are fixed (0.00 pt).

---

## D3 — Web PDF P1, WORD OF THE WEEK box: «чёрная пятница» line renders wrong

**Location:** P1, right column, WORD OF THE WEEK box, line «чёрная пятница» (PDF y≈1266–1289,
x≈1079–1230). Print: italic, correctly spaced, closing » tight. Web: upright, words joined,
closing » detached. The line is the edition's ONLY italic text (SVG `font-style="italic"`
occurs exactly once in all 8 SVGs; 16 italic chars total in print: 14 in this span + « »).

### D3(a) — Space glyph dropped: text layer incomplete, words joined

- Print span (NotoSerif-MediumItalic, 16.12 pt): `'чёрная пятница'` — a `' '` char exists,
  bbox [1145.576, 1148.108], 2.532 pt wide.
- Web span (LucernaNotoSerif-Regular, 16.12 pt): `'чёрнаяпятница'` — NO space char at all.
  Next glyph 'п' starts at x=1148.108 in BOTH PDFs (positioning preserved, glyph lost),
  so the advance-box gap 'я'→'п' is only **1.177 pt** in web vs 2.532 pt in print.
- Whole-edition char multiset: print 35,198 chars vs web 35,197 — the ONLY difference is
  this one space (P1 spaces 496 → 495; pages 2–8 identical, all other chars identical).
- `pdftotext` (plain): print 57,149 B / web 57,148 B; `diff` of the two texts shows
  EXACTLY ONE differing line — P1 line 207: `«чёрная пятница»` (print) vs `«чёрнаяпятница»` (web).
- Visual (3× render crops `p1-teaser-print.png` / `p1-teaser-web.png`, read by eye):
  print reads «чёрная пятница» (two words, clear space); web reads «чёрнаяпятница» (one word).
- Gate failed: "pdftotext 文本层必须完整" — the text layer is one space short; search/copy
  for "чёрная пятница" fails on this element in the web PDF.

### D3(b) — Closing » detached: 3.354 pt gap (> 0.5 pt threshold)

- Same span: print x1 = 1222.815, web x1 = 1219.461 → **x1 deficit 3.354 pt**.
- Next span '»': x0 = 1220.622 in BOTH PDFs (it does not move).
- Advance-box gap A→B: print −2.193 pt (italic overhang, quote tight) vs web **+1.161 pt**,
  diff **+3.354 pt > 0.5 pt** → D2-class abutting defect by the brief's own criterion.
- Visual: web crop shows 'пятница »' with the closing quote visibly floating; print shows it tight.

### D3(c) — Italic lost (style divergence print vs web)

- Print: NotoSerif-MediumItalic + Newsreader16pt-Italic (« »). Web: LucernaNotoSerif-Regular
  + LucernaNewsreader-Regular (upright). The whole line is upright in web.
- `tools/webpdf.py` contains NO italic handling at all (`grep -i italic|font-style|slant|oblique`
  → zero hits); `fc_match` varies only weight. No `Lucerna*Italic` subset is ever built
  (`pdffonts` on the web PDF: 0 italic faces; print embeds NotoSerif-MediumItalic +
  Newsreader16pt-Italic). Same defect class as D2 (tool face-resolution), different axis.

### D3 root cause (measured, not guessed)

- SVG source (`svg/p1-pervaya.svg`, y=1712): `чёрная` (Noto Serif, italic) + a standalone
  `<text x="1525.5" font-family="Newsreader" font-style="italic"> </text>` (space-only) +
  `пятница`. The space-only italic `<text>` loses its glyph in the web pipeline while its
  advance positioning survives ('п' x0 identical). The upright space-only `<text>`s elsewhere
  DO produce positioning-only gaps in BOTH PDFs (e.g. P5 band 'скидкис', P5 'маркетплейсахскидки',
  P1 'большая распродажав') — but those render as readable spaces in both PDFs (verified on
  3× crops) and are identical print-vs-web, so they are NOT defects. What makes D3 a defect
  is the print/web DIVERGENCE (print has the glyph, web does not) + the detached » + lost italic.
- Fix direction (for the coordinator, not done here): webpdf.py needs italic face resolution
  the way the weight patch added `:weight=200`/`:weight=100` — i.e. resolve `font-style="italic"`
  to the real italic faces and build italic subsets; the space-only italic run must emit its glyph.
  No in-edition fix exists (the SVGs are correct — freeze 8/8, check_core green).

### Why the executor's "1,704 pairs, 0 gaps" did not catch D3

- Their abutting scan pairs spans by a line-key matcher; this pair falls out of it because
  B.x0 (1220.622) differs from A.x1 (1222.815) by 2.19 pt (italic overhang) — the same matcher
  limitation fix1 itself documented ("my own scan implementation finds 4 of them").
  My scan matched spans by line y + order AND re-measured all 7 D2 spots by direct span lookup,
  so it is not subject to that matcher gap.
- Their "character multiset identical" claim (KIT §7, line 84) is also contradicted by
  measurement: the multisets differ by exactly one U+0020 (see D3(a)). The byte counts they
  quoted (57,149 / 57,148) are correct; the "identical multiset" inference from them is not.

---

## Verified green (independent re-measurement, not trusted from prior rounds)

### D1 — FIXED, both PDFs
- P5 band subtitle: `"Black Friday": sales from 16 November`, straight quotes, in print.txt:390
  AND web.txt:390 (identical line). 3× crops of the band in both PDFs read identically;
  closing straight quote tight on `:`. PIL advance (fix1's numbers re-confirmed by the crop):
  straight `"` 6.40 pt vs curly 13.50 pt.
- Curly-quote sweep (visible `<text>` in all 8 SVGs, ElementTree): U+201C ×1, U+201D ×1 — both
  on P7 y=552.64, the intended Newsreader pair `“чёрной пятнице”` (kept by design).
  U+2019 ×0, U+2018 ×0 on all 8 SVGs. Same counts in both PDFs' text layers (1 × “ and 1 × ” each).
- Source grep (`content*.py`): U+201C/U+201D only in `content56.py:12` (the Russian «Чёрная пятница»
  guillemets — correct Russian quotes, not the English string) and `content7.py:70` (the P7 pair).
  No U+2019 anywhere.

### D2 — all 7 original spots FIXED (direct span lookup, print vs web x1)
| Spot | Print x1 | Web x1 | Gap now (was) |
|---|---|---|---|
| P1 headline `14-` 39.75 pt | 133.02 | 133.02 | 0.00 (was 4.33) |
| P4 heading `14-` 24 pt | 106.46 | 106.46 | 0.00 (was 2.62) |
| P1 contents `1. 14-` 15 pt | 1138.69 | 1138.69 | 0.00 (was 2.20) |
| P4 band-sub ` все восемь результатов` 13.5 pt (`+` x0 1008.61 both) | 1008.74 | 1008.74 | 0.00 (was 1.94) |
| P1 contents `3. «` 15 pt | 1122.22 | 1122.22 | 0.00 (was 1.17) |
| P5 title `«` 24 pt (next span x0 80.11 both) | 80.11 | 80.11 | 0.00 (was 0.91) |
| P7 `«` 16.12 pt ×2 (x0=1096.12, y0=206.40 & 344.04) | 1105.61 | 1105.61 | 0.00 (was 0.58) |

### Full independent web-vs-print scan (`fullscan.py`, PyMuPDF rawdict, all 8 pages)
- Span-text equality (char stream incl. spaces): exactly **1** diff in the whole edition — D3(a).
- Abutting span pairs (advance-box gap, web−print): exactly **1** diff > 0.5 pt — D3(b) (+3.354).
- Intra-span char-pair gaps: exactly **1** diff > 0.5 pt — D3(a) pair 'я|п' (2.532 → 1.177).
- Per-page char multiset: only P1 differs (one space); P2–P8 identical.
- Font census: print italic chars 16 (NotoSerif-MediumItalic 14 + Newsreader-Italic 2, all on the
  D3 line); web italic chars 0. Web now embeds `LucernaNewsreader-Bold` (the weight patch works).

### Content proofread — print PDF, all 8 pages read fully vs core-ru
- Read `print.txt` P1–P8 end to end (858 lines, layout extraction). No content defect found.
- `freeze.py diff` core-ru vs edition SVG: **−0 strings removed on every page** (P1–P8);
  added strings are the English explanations + 121 × U+3000 furniture separators only.
  I.e. every core Russian string is present verbatim; nothing was altered or dropped.
- `.text.md` mechanical comparison vs `core-ru/2026-w47-ru-core.text.md`: 130 numbered exercises
  in both, numbers identical; **0 STEM diffs**; key diffs only the 4 expected E translation keys
  137–140 (Chinese → English) + Q150 parser artifact (verified by hand: both files say the open
  writing task's model text is in section H; edition "(Open task; model text below)").
- Dates/weekdays verified: 16 Mon / 17 Tue / 18 Wed / 19 Thu / 20 Fri / 21 Sat / 22 Sun Nov 2026;
  6–8 Nov Fri–Sun (round 14); 12 Nov Thu (Uzbekistan, 18:00, Pakhtakor); 17 Nov Tue 19:00
  (Venezuela, Krasnodar, Ozon Arena); 15th round 20–22 Nov Fri–Sun; Black Friday 27 Nov 2026 is
  a Friday; Cyber Monday 30 Nov is a Monday; Mother's Day 29 Nov is a Sunday; November 2026
  = 20 working days + 10 days off (9 weekend days + 4 Nov holiday) = 30.
- Numbers verified: 31 pts Zenit/Dynamo, 29 Spartak, 26 Krasnodar/CSKA, 15th Lokomotiv;
  21 goals; 4:2 Krasnodar–CSKA (7 Nov); 2:2 Zenit–Rostov (83rd-minute equaliser);
  2:1 Dynamo–Fakel (90+1 winner); 0:1 Lokomotiv–Rubin; correction box (VOL.3 printed 7 matches;
  8th: Baltika — Dynamo Makhachkala 0:1, 8 Nov 20:45) — all internally consistent and matching core.
  Practice chart 38+26+18+18 = 100, explicitly labelled as editor-made practice data, not real stats.
- P7 golden sentences: check_core GOLDEN 8, BAD 0 — each of the 8 quotes appears verbatim ×2
  (source page + P7). I re-verified each against the body text I read; English translations and
  page attributions (P1/P1/P2/P3/P4/P5/P6/P6) all correct. Error clinic 4 items all correct
  (с + instrumental; на + prepositional; 21 + гол; с 19 + genitive ноября).
- P8: `p8.py extract` 150/150 noted; `p8.py compare` vs core-ru **CLEAN**, missing=[], extra=0,
  keydiff=[137, 138, 139, 140] (the four E translation keys, as expected). Answer key 1–150 all
  present in the printed P8; every key I spot-checked matches the body (incl. 21→1946, 22→16:20,
  56→20:45, 63→играет, 73→заказов, 109→Синоптики обещают, 127→B Dynamo Mkh 1:0, 145–149 dialogue).
  Model text (Q150) = 97 words excluding the "Пример:" label (98 tokens incl. label).
- Photos/credits (all public domain, as labelled): 1912 Russia football team (author unknown);
  Yuon «Зима. Ростов»; Preston Keres / USDA; Kiprensky Pushkin portrait 1827; Toxer427 CC0.
  No image issue checked beyond the credits (occlusion audit covers geometry).
- VOL: visible SVG text VOL.4 ×9 (masthead + 8 footers), VOL.3 ×1 (P4 correction sentence,
  expected), VOL.5 ×6 (teasers/disclosure, expected); `tables.py vol 2026-W47` → vol 4.
- P8 min font: 9.75 pt (387 spans; next 9.98) — meets ≥ 9.75 pt.

### Mechanical gates (all re-run by me on the shipped files; see GATE-LOG.md)
- `check_core.py`: GOLDEN 8, BAD 0, gloss fails 0, P8 SVG text 10,571 chars; 1 orphan line-start
  (P7 y553 `”».`, known benign) + 1 same-baseline collision (P1 y1712 'чёрная'+' ', the D3 line).
- `p8.py extract` 150/150; `compare` CLEAN, keydiff [137,138,139,140]. RC=0.
- `freeze.py baseline`: **8/8 SVGs byte-identical**, RC=0; core integrity OK (shipped core SVGs unchanged).
- `occlusion_audit.py`: `--selftest` OK; real run RC=0: **42 TEXTX, 0 LINEX, 0 COVER, 0 FOOTER,
  0 EDGE, 0 BOXTITLE**; flag set byte-identical to fix1's `occlusion.json` (the 42/42
  pixel-adjudicated-CLEAR set from round 1 — no new flag).
- Text layer: print 57,149 B / web 57,148 B (the 1-byte difference IS D3(a)); 30,293
  non-whitespace chars each (identical — the missing char is a space).

## What this proof did NOT do (per the brief)
- No source edits, no rebuilds, no commit, no push. No changes to core-ru, other editions, `tools/`.
- The KIT was NOT edited (read-only check: §5/§7 do record the patched web PDF, SHA + bytes correct;
  but §7's "character multiset identical" and "1,704 pairs → 0 gaps" claims are contradicted
  by the measurements above and should be corrected by the coordinator).
- Freeze baseline was run with `--out` under `/tmp` (not the intended scratch dir) because of EDQUOT.
