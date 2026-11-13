# PROOF-NOTE — 2026-W47 de-es, proof1 (independent, rebuild 4)

- Edition: `2026-w47-de-es` (German target, Spanish explanations), rebuild 4
  (core-de build15, Q34 singular stem). Proofer is NOT the rebuild-A builder.
- Date: 2026-11-11. Scratch: `hidden_files/w47/scratch-proof-de-es1/`
  (GATE-LOG.md + gate outputs + d2scan-de-es.py + boxbottom.py + creambox.py).
- No source was modified, no rebuild, no commit, no push.

## Conclusion: (b) — 1 defect (D1)

## SHA verification — all three MATCH

| File | Bytes | SHA-256 (full, verified) | Expected prefix |
|---|---|---|---|
| `Die-Lucerna-VOL4-de-es.pdf` | 10,968,803 | `7bc39e1f58b9bb447caf4f69b397eb39723ab2fef1c2bc4cf99d1be4a6e580ed` | `7bc39e1f58b9bb44` ✓ |
| `Die-Lucerna-VOL4-de-es-web.pdf` | 1,558,821 | `cd453143111bfad4f7f8a6ada98190f1790d2feccdaf3fd7c762a3a683043b90` | `cd453143111bfad4` ✓ |
| `2026-w47-de-es.text.md` | 50,124 | `5f5ea69b69a578dd42865a4b6065ba1dc55e347e6802bd9b3eb3683a8b0027b3` | `5f5ea69b69a578dd` ✓ |

## Defects

### D1 — P7: DER WERKZEUGKASTEN box too short; last entry spills off its cream box

- Page: P7 (print and web — both render the same SVG).
- Current: toolbox cream box `svg/p7-sprache.svg`: rect x=1439.5 y=330 w=422.5
  h=453.5 → bottom edge y=783.5. The 6th (last) entry
  `Es ist fraglich, ob ... = aún dudoso` sits at baseline y=783.9 — 0.4 units
  BELOW the box bottom edge. Its descender ink (the `g` in `fraglich`,
  ~4.3 units at size 20.5) ends at ~y=788, i.e. ~4.7 units of ink on the
  white newsprint below the box.
- Should be: the box bottom must cover the whole last entry (baseline +
  descender, ≥ ~y=788; other col3 boxes on this page keep +10.4 / +42.9
  clearance, other pages +16…+48). Fix by extending the toolbox box and
  reflowing the two boxes below it (LESERBRIEFE starts y=799.5, NOCH EIN WORT
  ends 1518.0; 30 px slack to the 1548 rule) — or by fixing the shared
  box-height computation (see mechanism note).
- Evidence:
  - SVG measurement (`creambox.py`, all cream `#f0eee5` boxes in the edition):
    every other cream box has last-baseline clearance +10.4…+47.7; the toolbox
    is the ONLY one with negative clearance (−0.4). LESERBRIEFE +10.4,
    NOCH EIN WORT +42.9 on the same page.
  - Zoomed render (`/tmp/proof-de-es1/p7-toolbox-zoom.png`, 3× crop of the
    100 dpi print render): the cream ends at the text baseline and the `g`
    descender of `fraglich` visibly hangs below the cream onto white.
  - The builder's record claimed "toolbox (6 entries, last inside the box)" —
    numerically false (783.9 > 783.5).
- Mechanism note (for the fixer, not a separate defect): de-en P7 carries the
  byte-identical geometry (same box bottom 783.5, same last baseline 783.9,
  entry `Es ist fraglich, ob ... = Whether … is open`), while core-de's box is
  different (bottom 744.5, clearance +18.8). So this is a family-wide
  fan-out box-height defect, not an es-only value error; the shared
  transform/box helper is the likely fix site. Other de fan-out editions
  should be swept for the same −0.4 before they are proofed.

## What was verified clean

### Content — full read of `2026-w47-de-es.text.md` (1,185 lines, 48,286 chars)

- German frozen text: 951/1,186 lines byte-identical to core-de text.md; every
  differing line is explanation-layer (Chinese → Spanish) except the header
  slug line. Exercise stems: 137 numbered lines, 14 post-tag-strip diffs —
  all are P8 answer-key group lines (glosses), Q18 date rendering
  (`November = 18 de noviembre`), Q108 translated options, Q137–140
  translation-direction instructions (expected keydiff items).
- All 150 exercise keys checked by hand against their stems/options/articles
  during the full read (Q1–150), including: P2 date arithmetic
  (18+11=29, 15+7=22, 16+6=22 Nov), P4 results table vs prose (9 rows,
  all scores match; MD10 fixtures match prose), P6 poll 44+33+23=100 and
  44+33=77, P7 grammar keys (wird/werden, stiller, weil, ob, fraglich, dass
  verb-final), P8 cloze/dialogue/matching a–d mappings (verified visually on
  P2/P4/P8 renders, not just in text), MUSTER word count = 84 by token count
  (matches the "(84 palabras)" label; core label also 84).
- P7 Sätze der Woche 8/8 verbatim from body text, with correct page + level
  attributions (P1·A2 ×2, P2·A2, P3·A2, P5·B1, P4·B1, P6·B2 ×2).
- P8: 150 exercises + full answer key present (8 groups, pp. 1–8).
- ABSTRACT.txt: 426 B, one line, Spanish, 0 ASCII double quotes.
- No other content, number, date, score, or key error found on any page.

### Q34专项 (the reason for rebuild 4)

- New singular stem `Am Montag öffnet in Köln der erste ___.`: 1× in
  `content34.py`, 1× in `.text.md`, 1× in `svg/p3-kultur.svg`, 1× in print
  PDF text layer, 1× in web PDF text layer. Old plural stem
  `Am Montag öffnen in Köln die ersten ___.`: 0× in all five places.
- P3 visual: Q34 renders as the new singular stem (print + web renders).
- Key `Weihnachtsmarkt` unchanged; P3 freeze sha `fc88f676` (the expected
  Q34 fingerprint).

### Geometry / gates (all re-run independently by the proofer; see GATE-LOG.md)

- `tools/occlusion_audit.py` (proper run, selftest OK): **0 flags**, RC=0.
  (First invocation mistakenly passed `--selftest`, which runs ONLY the
  selftest and returns 0; caught on log review and re-run without it.)
- `tools/p8.py extract`: 150/150 noted. `compare` vs core: **CLEAN**,
  missing=[] extra_count=0, keydiff=[137, 138, 139, 150] (expected).
- `tools/freeze.py diff`: RC=0; TOTAL added CJK 7, all U+3000, 1 per page
  P2–P8, 0 on P1.
- `freeze_direct.py`: source PASS (0 unaccounted removed/added);
  rendered 8/8 — frozen counts 147/163/195/166/173/175/150/186,
  sha `083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 /
  b7aa0771 / 57e118e7` (identical to builder).
- `keycheck.py` (P8-extracted keys vs REG): **149/150 exact**; only Q150
  (open writing task) differs by the known extractor truncation
  (`Tarea libre` vs full key) — expected.
- `boxtitle.py`: **7/7 fit** — Tranquila 356.5, Palabras 387.6, Consejo 227.0,
  Adviento 341.4, Útiles 358.8, Cartas 248.2, Una palabra más 380.7
  (budget 400.5). Note: this checks title WIDTH only, not box bottom —
  it does not cover D1.
- Chips (`rx="2.7"` rects): 10/15/18/15/18/12/35 = **141** total.
- P8 minimum span size (PyMuPDF): **9.94 pt** ≥ 9.75 pt floor.

### Bent punctuation专项

- U+201C: 33× in text.md / SVGs — ALL are German `„…"` closing quotes,
  each paired with U+201E (33×). Every occurrence sits in German text
  (Fragen der Woche, `Im Lande des Christkinds`, BEISPIELE, Leserbrief,
  golden sentences). U+201D: 0. U+2019: 0.
- Spanish values: 0 curly quotes. The 2× U+201C/U+201E in `tr_es.py:201`
  sit inside the German exercise stem `„Stiller als sonst" heißt...`
  (a German string being translated, not a Spanish value).

### Web PDF

- 8 pages; per-page word multiset vs print: identical on all 8 pages.
  Default mode: print 51,012 B / web 51,013 B, word multiset identical
  (8,088 words). `-raw` normalised text: exactly identical, 49,812 B each.
- Abutting scan (`d2scan-de-es.py`, proofer's method from the zh-tw-it
  proof): 58 print-abutting span pairs, **0 with web gap > 0.5 pt**.
  Extended delta check over all 81 adjacent span pairs: web gap − print gap
  never > 0.5 pt; max |Δ| = 0.0 pt.
- Web visual: all 8 pages viewed at 100 dpi; identical to print except D1
  (shared SVG). No web-only defect.
- Tool-layer note (separate from content defects, per brief): this web PDF
  was built with pre-D2-patch webpdf.py; per coordinator decision it will be
  rebuilt with the final tool at pre-insert. Pixel diff print-vs-web is
  font-weight-level only (mean |Δ| 0.19–2.10 grey levels, concentrated in
  bold/masthead areas; P1 2.10, P7 1.47); no visible weight defect at 100 dpi.
  Abutting is already 0, so the rebuild is a face-correctness formality.

### Visual proofread (print PDF @100 dpi, all 8 pages viewed)

- P1–P6, P8: zero findings. P7: D1 only (toolbox box bottom).
- Q34 new stem confirmed visually on P3 (print + web).

## Observations (NOT defects)

- O1 (already ruled): P4 prose mentions `VfB Stuttgart verlor in Istanbul
  bei Galatasaray mit 0:2`, but the results table lists no Stuttgart–
  Galatasaray row (table rows: Atlético–Bayern, Dortmund–Betis,
  Leipzig–Man. City, the three Europa/Conference rows, then Bundesliga only).
  The coordinator has already ruled this not a defect (rebuild-A report);
  recorded here only so it is not re-raised as new.
