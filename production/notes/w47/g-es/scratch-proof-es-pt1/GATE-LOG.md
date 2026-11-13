# GATE-LOG — W47 es-pt proof1

Independent proofread gates, all actually run on 2026-11-11. Object SHAs (re-verified
before writing this log):

- `La-Lucerna-VOL4-es-pt.pdf` 3,500,787 B —
  `4793edeb87c2d6cd138906bbdeb0c2fc47088c91a11d99e75582b71daafde4e0`
- `La-Lucerna-VOL4-es-pt-web.pdf` 847,463 B —
  `d7429fcb83d70735f38587527d0fcc1032389d891e94b12b7dba4ad4ee4776ef`
- `2026-w47-es-pt.text.md` 44,990 B / 1,797 lines —
  `d3e4bd818b51f19bbea2c52dd1f5664bd342ea497d96f6180ae05b3f350b7a2f`

Environment: probe OK (`hash-object` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`,
scratch write OK); `/tmp` full, so `TMPDIR=<scratch>/tmp` throughout; repo tools run
with `tools/venv/bin/python`; fonts: Newsreader `tools/fonts/Newsreader-*.ttf`,
Noto Sans CJK SC `/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc` (index 2 = SC;
Bold TTC same dir).

## 1. Occlusion audit (formal, no --selftest)

- Tool: repo `tools/` occlusion audit, run against the edition SVG set.
- Result: **0 flags.**
- Selftest (run separately to validate the audit itself): all six classes fired —
  BOXTITLE / COVER / EDGE / FOOTER / LINEX / TEXTX.
- Log: `occlusion.log`.
- Caveat recorded: the audit's BOXTITLE class only checks rects with a stroke or fill
  `#2c2822`; cream boxes (`#f0eee5`, no stroke) are excluded — which is why gate 8
  (boxtitle text_w) was run explicitly, and it caught D1.

## 2. p8 extract + compare

- Extract: **150/150** items from `p8-ejercicios.svg` → `p8-extract.json`
  (also saved as `p8extract.json`).
- Compare vs core-es: **CLEAN**, missing=[] extra=0, keydiff=[137, 138] — the two
  adjudicated translation items per the W45/W46 ruling (`p8-compare.json`,
  `p8compare.json`).

## 3. Freeze baseline (8/8) — with my own first-run error recorded

- **First run reported 0/8 — that was MY command error:** `--core-svg` was wrongly
  pointed at `core-es/svg` instead of the edition's own `svg/`. Not a defect; do not
  misread it as one.
- **Correct run: 8/8 byte-identical.** Direct sha256 of
  `freeze-es-pt-proof1/build-copy/svg` vs shipped `svg/` — 8/8:
  p1 `c689a2aa05bd`, p2 `febc07f1681c`, p3 `514ad8e7fdba`, p4 `413ba104948f`,
  p5 `ed98d2fa8122`, p6 `2fd2360fa44f`, p7 `f75e8e2710d8`, p8 `aacd13cfa78f`
  (full hashes in `freeze-baseline.log`).
- Freeze diff: added CJK = **0** total (`freeze-diff.json`).

## 4. keycheck (REG vs P8-extracted)

- Setup: copied `keycheck.py` + `tr_pt.py` + `stub_bslib.py` + `stub_svg.py` from
  `hidden_files/w47/scratch-fanout-de/` into this scratch, and added a missing
  `illus_voto` no-op stub to MY copy of `stub_bslib.py` (the de-built stub lacked this
  es-only illustration fn). The stub change is in my scratch copy only; no source
  files were touched.
- Result: REG 150 entries; levels A2 50 / B1 72 / B2 28; by page P1 10 · P2 18 · P3 18 ·
  P4 18 · P5 18 · P6 18 · P7 12 · P8 38; MODELO 97 words.
- **149/150 exact match.** Only mismatch is #150 (expected open-task form: REG key
  `Questão aberta — texto modelo abaixo, nesta página`, extracted `✓` — the
  adjudicated rendered form per KIT §6.4; the script exits RC=1 only because its
  `expected_only` predicate expects a prefix match). Not a defect.
- Logs: `keycheck.log`, `keycheck-150.json`.

## 5. creambox.py full scan + PIL ink measurement

- `creambox.py` / `creambox_diag.py` copied from `scratch-proof-es-fr1/`; `ink_measure.py`
  written by me. Logs: `creambox-all.log`, `creambox-diag-p123.log`,
  `creambox-diag-p45678.log`, `ink_measure.log`.
- **Critical method point:** Portuguese explanation lines are rendered in
  **Noto Sans CJK SC**, Spanish frozen lines in **Newsreader** — ink was measured with
  the line's actual font (NotoSansCJK-Regular.ttc index 2 = SC;
  Newsreader-Regular.ttf; 4× render).
- **All 22 cream boxes inside.** Tightest ink clearances (ink right/bottom vs box edge):

  | Location | Line | Clearance |
  |---|---|---|
  | P5 VOTAR box | `compara precios antes de pagar.` | **+0.05** |
  | P2 (frozen) | `ley.` | **+0.07** |
  | P7 CARTAS box | last line | +1.45 |
  | P2 ¿Y TÚ? box | `envia-as à redação.` | +1.54 |
  | P5 ¿Y TÚ? box | `frases e envia-as.` | +1.62 |
  | P3 ¿Y TÚ? box | `envia-as.` | +1.72 |
  | P4 ¿Y TÚ? box | (last line) | +1.75 |

  P7 toolbox clearance measured: ERRORES box ink +38.01 (baseline +42.5);
  LA PALABRA +21.22; CARTAS +1.45.
- Six negative baseline clearances in creambox output are all false positives
  (below-box headings/notes, same coordinates as core — verified via diag).
- **es-fr1's D1 does NOT reproduce in es-pt:** Portuguese `frases` has no `p`;
  French `phrases` does. (Side note: es-fr1 measured its D1 with the wrong font —
  Newsreader for a Noto Sans CJK SC line; with the correct font its overflow is
  ~+2.35 px not +2.85 px, so its D1 still stands.)

## 6. Print/web text layer

- `pdftotext` on both PDFs: both **45,996 B, byte-identical** (`cmp` clean) —
  `print.txt`, `web.txt`. Both PDFs 8 pages.

## 7. P8 minimum font (PyMuPDF spans, print = web)

- P8 min **10.125 pt** — KIT's 10.125 pt claim verified correct this time (the task
  warned KIT numbers had mismatched before; this one matches).
- Other pages min 11.62–12.75 pt. ≥ 9.75 pt floor ✓.

## 8. boxtitle text_w (all 27 box titles, PIL advance width, real font/weight)

- Log: `boxtitle.log`, script `boxtitle.py`.
- **One overflow — D1:** P1 `LA SEMANA EN CIFRAS　Em números`, advance right 971.9,
  **+10.9** past box edge 961; PNG ink rightmost x=968 at y=1322 (**+7 px**); cream
  edge confirmed x=961 (cream 540..960 at y=1330); crops `crop-p1-title-row.png`,
  `crop-p1-title-right.png`.
- All other 26 titles positive; minimum +9.0 (P7 LA PALABRA).
- Same defect class in es-fr (advance right 977.8, +16.8) — missed by its proof;
  es-de/en/it fit.

## 9. Curly quotes / guillemets / ASCII quotes

- U+201C / U+201D / U+2019 = **0** in all SVG text and in text.md (the "P7 Newsreader
  italic pair" exception is moot — none exist).
- Guillemets « » balanced **56/56**.
- 0 ASCII apostrophes / straight double quotes in text.md.

## 10. §1.1 fonts / colors

- Paper `#fbfaf6` ×8 (one rect per page); masthead UnifrakturMaguntia 196 units ×1;
  VOL.4 ×9, VOL.5 ×3 (all legitimate forward refs); P8 chip rects 35
  (A2 `#5c6e30` 11 / B1 `#46581f` 21 / B2 `#37402f` 3); no gold/brick-red
  (moth yellows `#D7B257`/`#EDD17F` only, as in core); CJK in SVG `<text>` = 0 on all
  pages; U+3000 total 118; moth `<title>Lucerna 三色蛾</title>` present (non-rendered,
  as in core).
- Fill census vs core-es: **no new colors introduced by the fan-out.**
- Mechanism observation: explanation layers render in Noto Sans CJK SC, not SOP §1.1
  Newsreader; body text `#302c28`, not SOP's `#3a3631` (0 occurrences of `#3a3631`
  in both core and edition) — uniform across production, mechanism-level only.

## 11. Dates (`date -d`, Europe/Madrid)

2026-11-13 Fri, 11-16 Mon, 11-19 Thu, 11-20 Fri, 11-22 Sun, 11-24 Tue, 11-25 Wed,
11-26 Thu, 11-27 Fri, 11-28 Sat, 11-29 Sun — all match the paper's weekday claims.

## 12. 150 answer keys — semantic verification

- Layout extractor `extract_items.py` → `items-150.txt`: 138 items extracted
  (SVG column-major COLX ≈ [88, 538.5, 989, 1439.5] + y-order — authoritative;
  text.md interleaves columns row-wise and misassigns stems if read naively).
- The 12 matching items 25–28 / 52–55 / 141–144 verified separately from REG.
- **All 150 keys correct.** Matching: 25=c, 26=b, 27=d, 28=a; 52=c, 53=b, 54=a, 55=d;
  141=c, 142=d, 143=b, 144=a.
- Golden sentences 8/8, each exactly 2× (original + P7 quote); page refs
  P1/P4/P2/P5/P3/P6/P3/P6 all correct. Model text 97 words ✓.
- Per-page Note-word counts match KIT exactly (P1 reflexión 2; P2 mitin/cartel/escaño 2;
  P3 cante 5/toque 6/baile 9/compás 4/duende 6; P4 parón 2/liderato 3; P5 papeleta 2/
  censo 3/plazo 3). P8 answer notes (Portuguese) read fully.

## 13. External facts (web, 2026-11-11)

All verified ✓ except the two core-level candidates noted in PROOF-NOTE.md:

- Election calendar: RD 806/2026 (BOE 2026-10-06); vote Sun 2026-11-29 9:00–20:00;
  campaign Fri Nov 13 00:00–Fri Nov 27 24:00; reflection Sat Nov 28; no polls
  Tue Nov 24–Sat Nov 28 (LOREG art. 69.7).
- UNESCO flamenco: declared 2026-11-16, 2010, Nairobi.
- LaLiga MD13: all six fixtures/times + standings (Barça 33, Madrid 30, Atlético 28,
  Betis 26); Atlético–Barça 1–2 Sun 2026-11-08 at Metropolitano (Fermín brace).
- UCL MD4: Barça 3–0 Aston Villa Nov 3; Atlético 0–2 Bayern Nov 3; AEK 2–3 Real
  Madrid Nov 4. MD5: Real Madrid–PSV Tue Nov 24 21:00; Sabah–Barça Wed Nov 25 18:45;
  Atlético–Viking Wed Nov 25 21:00; Villarreal and Betis also play MD5.
- MiDNI: JEC Acuerdo 342/2026, session 2026-11-05, lifts MiDNI suspension
  (MiDGT stays suspended).
- Debates: laSexta Nov 13 21:30, Ana Pastor, Cuerpo/Bravo/Bustinduy/Figaredo;
  SER Nov 18 vivienda, Bravo vs Isabel Rodríguez; Atresmedia debate-a-cuatro moved to
  Mon Nov 23 (Feijóo, Abascal, Colau confirmed; PSOE invited, unconfirmed);
  RTVE debate-a-cuatro Nov 26; PP cara a cara Sánchez–Feijóo Mon Nov 16 (Mediaset).
  Frente Amplio confirmed as a real 2026 Spanish formation.
- Bilbao Municipal Band: Sun Nov 22, 12:00, Palacio Euskalduna.
- Sargent `«Bailaora española»` (1880–81): Google Arts & Culture — *Spanish Dancer*
  (1880–1881, private collection).
- Postal vote: documentation from Mon Nov 9; application deadline Thu Nov 19
  (inclusive); deposit by Wed Nov 25; scrutiny Fri Dec 4 (Correos official note
  2026-11-10; LOREG art. 72).
- **C1 (core):** Nov 13 laSexta debate theme — core says economy only; quadratin.com
  2026-11-10 and diarioenpositivo.com 2026-11-06 say economy + housing. Core KIT
  §6.10 adjudicated economy-only (diariodesantiago.es 2026-11-06). Insufficient to
  overturn.
- **C2 (core):** RTVE free-minutes split (45/45/30/30/15 + 3×10 = 195) presented as
  JEC-settled — diariodia.es 2026-11-01 (upd. 2026-11-09): FA vs Podemos dispute over
  Sumar's inheritance pending before the JEC; RTVE propaganda-slot proposal not yet
  presented. Core KIT §5.3 cites queproponen.es; that page could not be retrieved in
  search for independent confirmation. Recommend coordinator re-check before the
  Nov 16–22 publication window.

## 14. Visual check — 8 rendered PNGs

`cards/p1-portada.png` … `p8-ejercicios.png` (1950×2700 each) read in full.
P1: only D1 visible. P2–P8: clean — no overlap, no footer intrusion, no
image-caption mismatch. Details in PROOF-NOTE.md.

## Files in this scratch

`PROOF-NOTE.md`, `GATE-LOG.md` (this file), `tmp/` (TMPDIR), `creambox.py`,
`creambox_diag.py`, `keycheck.py`, `tr_pt.py`, `stub_bslib.py` (patched with
`illus_voto` no-op stub, scratch copy only), `stub_svg.py`, `occlusion.log`,
`p8-extract.json`, `p8-compare.json`, `p8extract.json`, `p8compare.json`,
`freeze-baseline.log`, `freeze-diff.json`, `freeze-es-pt-proof1/`, `keycheck.log`,
`keycheck-150.json`, `creambox-all.log`, `creambox-diag-p123.log`,
`creambox-diag-p45678.log`, `ink_measure.py`, `ink_measure.log`, `boxtitle.py`,
`boxtitle.log`, `print.txt`, `web.txt`, `items-150.txt`, `extract_items.py`,
`crop-p1-title-right.png`, `crop-p1-title-row.png`.

**No source files were modified, rebuilt, committed, or pushed by this proof.**
