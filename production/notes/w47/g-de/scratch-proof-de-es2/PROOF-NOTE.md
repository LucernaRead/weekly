# PROOF-NOTE — 2026-W47 de-es, proof2 (independent, rebuild 5)

- Edition: `2026-w47-de-es` (German target, Spanish explanations), rebuild 5
  (fix1: `content7.py:76` pad 90 → 110, D1 only). Proofer is NOT fix1.
- Date: 2026-11-11. Scratch: `hidden_files/w47/scratch-proof-de-es2/`
  (PROOF-NOTE.md + GATE-LOG.md + gate outputs + renders + creambox.py + d2scan-de-es.py).
- No source modified, no rebuild, no commit, no push, no subagent.
- Probes: `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` →
  `9daeafb9…` OK; real test file written in `hidden_files/w47/scratch-proof-de-es2/`.
  Workspace scratch used throughout; no `/tmp` writes.

## Conclusion: (a) — 0 defects. D1 fixed and verified; full round clean.

## SHA verification — all three MATCH the task values exactly

| File | Bytes | SHA-256 (full, verified) |
|---|---|---|
| `Die-Lucerna-VOL4-de-es.pdf` | 10,968,798 | `6e8bde3f30a6dcb415321051d0a9f1a19f3a5c033d0167b80215a969aa69077e` ✓ |
| `Die-Lucerna-VOL4-de-es-web.pdf` | 1,601,888 | `f43d561a2e54de16ffd194ea5f05b1ad9c6c44ef6d60809324cc73e2dfd28d7e` ✓ |
| `2026-w47-de-es.text.md` | 50,124 | `5f5ea69b69a578dd42865a4b6065ba1dc55e347e6802bd9b3eb3683a8b0027b3` ✓ |

Note: text.md SHA is identical to rebuild 4 (fix1 claimed zero content change) —
confirmed: the file proof2 read is byte-identical to the file proof1 read.

## D1 fix verification — creambox real measurement + 300 dpi visual (double check)

- `creambox.py` (proofer's copy, re-run on rebuild-5 `svg/p7-sprache.svg`):
  - DER WERKZEUGKASTEN: rect y=330, bottom **803.5**, last baseline 783.9,
    clearance **+19.6** (was −0.4) ✓ — matches fix1's claim exactly.
  - LESERBRIEFE: rect y=**820**, bottom 1372.0, last baseline 1361.6,
    clearance +10.4 (unchanged) ✓. Gap toolbox-bottom → LESERBRIEFE top =
    16.5 px (fix1's predicted 819.5 vs measured 820 — see O2, not a defect).
  - NOCH EIN WORT: rect y=1388, bottom **1538.0**, last baseline 1495.1,
    clearance +42.9 (unchanged) ✓ — exactly 10 px before the Sätze rule at
    y=1548.
  - Last entry `Es ist fraglich, ob ... = aún dudoso` fully inside the box:
    baseline 783.9 + descender ≈ 4.7 → ink ends ≈ 788.6, box bottom 803.5,
    ≈ 15 px of clean cream below the ink.
- 300 dpi zoom (`p7-toolbox-print-300.png`, clip of the print PDF) viewed:
  the `g` descender of `fraglich` has clear cream beneath it, the cream box
  continues below the text, then a white gap, then the LESERBRIEFE box.
  Web zoom is byte-identical to print (sha256 `8a72ebeb…`, same file) —
  the fix is in the shared SVG, both PDFs carry it.
- Full-edition creambox sweep (`svg/*.svg`, 32 rows): no negative clearance
  except the matcher's known false positives — P7 BEISPIELE boxes −35.0
  (matched against exercise numbers below them, same as proof1/fix1) and
  P1 `DAS WORT DER WOCHE` −24.0 (following section head inside the +45
  window, same as fix1). Occlusion audit 0 flags + P1 visual confirm
  neither is a defect.
- `content7.py:76` confirmed to carry pad **110** with the fix1 comment
  (read-only check).

## What was verified clean

### Content — full read of `2026-w47-de-es.text.md` (1,185 lines), from scratch

- All 150 exercise keys re-verified by hand against stems/options/articles
  during the full read (Q1–150), including the matching groups decoded
  letter-by-letter (Q25–28: d/c/a/b; Q52–55: d/b/c/a; Q141–144: c/a/d/b —
  all correct), the P7 grammar keys (wird/werden, stiller, weil, ob,
  fraglich, dass verb-final), and the P8 cloze/dialogue keys (113–120,
  145–149, person/number agreement all correct).
- Dates/weekdays re-checked with `date` (Europe/Berlin): 3.11 Tue, 4.11 Wed,
  5.11 Thu, 6.11 Fri, 7.11 Sat, 8.11 Sun, 13.11 Fri, 16.11 Mon, 17.11 Tue,
  18.11 Wed, 19.11 Thu, 20.11 Fri, 22.11 Sun, 24.11 Tue, 25.11 Wed, 26.11 Thu,
  27.11 Fri, 29.11 Sun — every weekday named in the text matches.
- Date arithmetic: 18+11=29, 15+7=22, 16+6=22 Nov ✓; Buß- und Bettag 11 days
  before 1st Advent (18→29 Nov) ✓; Totensonntag 4 days after Buß- und Bettag ✓.
- P4 results table vs prose: 9 MD9 rows, goal sum 4+3+3+7+4+1+3+2+3 = **30**
  ✓ (matches "30 Tore in neun Spielen"); all nine scores match the prose;
  Bayern–Mainz 1:2 / Dortmund–Elversberg 2:1 / Leipzig–Augsburg 5:2 /
  Hamburg–Gladbach 3:1 all consistent both places.
- P6 poll: 44+33+23=100 ✓, 44+33=77 ✓; labelled ÜBUNGSDATEN (practice data,
  not a real survey) ✓.
- P7 Sätze der Woche **8/8 verbatim from body text** (script-checked, not
  eyeballed): P1·A2 ×2, P2·A2, P3·A2, P5·B1, P4·B1, P6·B2 ×2 — page and
  level attributions all correct.
- P8: 150 exercises + full answer key present; key tokens cover 1–150 with
  none missing; MUSTER token count = **84** (matches "(84 palabras)").
- ABSTRACT.txt: 426 B, one line, Spanish, 0 ASCII double quotes.
- No other content, number, date, score, or key error found on any page.

### Q34专项 (no regression — five places)

- New singular stem `Am Montag öffnet in Köln der erste ___.`: 1× in
  `content34.py`, 1× in `.text.md`, 1× in `svg/p3-kultur.svg`, 1× in print
  PDF text layer, 1× in web PDF text layer.
- Old plural stem `Am Montag öffnen in Köln die ersten ___.`: 0× in all
  five places.
- P3 visual: Q34 renders as the new singular stem (print render viewed).
- Key `Weihnachtsmarkt` unchanged; P3 freeze sha `fc88f676` (same as rebuild 4).

### Geometry / gates (all re-run independently by the proofer; see GATE-LOG.md)

- `tools/occlusion_audit.py` (proper run, NO --selftest): selftest OK
  (all 6 planted classes fired, clean controls silent), **0 flags**, RC=0.
- `tools/p8.py extract`: **150/150 noted**. `compare` vs core-de: **CLEAN**,
  missing=[] extra_count=0, keydiff=[137, 138, 139, 150] (expected).
- `tools/freeze.py diff`: RC=0; TOTAL added CJK 7, all U+3000, 1 per page
  P2–P8, 0 on P1.
- `freeze_direct.py es`: source PASS; rendered **8/8** — frozen
  147/163/195/166/173/175/150/186, sha `083e2a2a / 689045ad / fc88f676 /
  df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7` — **identical to
  rebuild 4 on all 8 pages** (P3 Q34 + P7 frozen text unchanged; only P7
  box geometry moved).
- `keycheck.py es`: **149/150 exact**; only Q150 extractor truncation
  (`Tarea libre` vs full key) — expected.
- `boxtitle.py es`: **7/7 fit** (356.5 / 387.6 / 227.0 / 341.4 / 358.8 /
  248.2 / 380.7; budget 400.5).
- Chips (`rx="2.7"` rects): 10/15/18/15/18/18/12/35 = **141** total.
- P8 minimum span size (PyMuPDF): **9.94 pt** ≥ 9.75 pt floor.
- §1.1 grep: zero old-palette hexes (no gold, no red-brown, no near-black);
  all hexes in use are the §1.1 palette except the P1 three-colour moth
  logo mark (brand artwork, see O3).

### Bent punctuation专项

- U+201C: 33× in text.md / 33× in SVGs — ALL German `„…"` closing quotes,
  each paired with U+201E (33×/33×). U+201D: 0. U+2019: 0.
- Spanish values: 0 curly quotes.

### Web PDF

- 8 pages; per-page word multiset vs print identical on all 8 pages.
  Default mode: print 51,011 B / web 51,011 B, 8,088 words, multiset
  identical. `-raw` normalised text: exactly identical, 49,812 B each.
- Abutting scan (`d2scan-de-es.py`): 58 print-abutting span pairs,
  **0 with web gap > 0.5 pt**.
- Pixel diff print-vs-web @100 dpi: mean |Δ| P1 0.368, P2 0.000, P3 0.121,
  P4 0.213, P5 0.260, P6 0.000, P7 0.096, P8 0.069 grey levels — font-weight/
  antialiasing level only, and closer than rebuild 4 (0.19–2.10).
  No web-only defect. P7 toolbox zoom byte-identical print/web.

### Visual proofread (print PDF @100 dpi, all 8 pages viewed)

- P1–P8: zero findings. P7: D1 confirmed fixed (see above); the rest of
  the page (lessons, Sätze der Woche, Fehlerklinik, teaser) clean.
- P2/P5/P6 column-flow white gaps are layout whitespace, same as proof1 —
  not defects.

## Defects

None.

## Observations (NOT defects)

- O1 (already ruled, carried from proof1): P4 prose mentions
  `VfB Stuttgart verlor in Istanbul bei Galatasaray mit 0:2`, but the
  results table lists no Stuttgart–Galatasaray row. Coordinator already
  ruled this not a defect; not re-raised.
- O2 (measurement note, not a defect): fix1's `content7.py:76` comment and
  FIX-LOG §3 predict LESERBRIEFE y=819.5, but the shipped SVG rect measures
  y=820 (16.5 px gap from the toolbox bottom instead of 16.0). Clearance
  +10.4 and NOCH EIN WORT end 1538.0 are exactly as predicted; the 0.5 px
  is a layout-vs-SVG rounding difference with no visual consequence.
- O3 (checked, clean): the only non-§1.1-palette hexes in the SVGs live
  inside the P1 three-colour moth logo mark under the masthead
  (`#34483A`, `#7898CD`, `#4D72B4`, `#EDD17F`, `#D7B257`, `#84A283`,
  `#4F765D`) — brand artwork, not page furniture; verify.py's §1.1 style
  audit passed the same palette in rebuild 4.
- O4 (tool state, for the coordinator): this web PDF was built with the
  in-flight D2-patch webpdf.py (same state as fix1; the coordinator's
  pre-insert final-tool rebuild still stands). The rebuild-5 web PDF is
  measurably closer to print than rebuild 4's, so no action follows from
  this round.
