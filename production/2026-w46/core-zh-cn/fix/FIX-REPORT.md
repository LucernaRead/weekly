# Fix Report — 2026-w46-zh-cn-es, Round 1 verdict D1

- Edition: 2026-w46-zh-cn-es ONLY (issue dated Mon 2026-11-09 to Sun 2026-11-15, VOL.3).
  Edition folder: `files/weekly-report-w46-zh-cn-es/`.
- Authority: Round 1 verdict
  `hidden_files/w46/zh-cn-proofread-gates/proofreader-verdict-round1.md`
  (D1 blocking in zh-cn-es only; the other 9 ZH-CN editions PASSED and were
  not touched). SOP `files/weekly-report-SOP.md` read in full before work.
- Fix worker scope: fix only what the verdict lists, at the source, full
  re-render of the ES edition, re-run all gates. No push, no insert, no
  Discord post, no chat dump, no edit to `~/workspace/weekly-git` or
  `index.json`, no subagents. No rendered SVG/PDF was hand-edited.
- Status: D1 fixed and re-gated clean (see §4). A Round 2 independent
  proofread of the ES edition still follows; this report and its re-gating
  do not replace it.

## 1. Defect (verdict D1, quoted)

Stray wrap-orphan lines on P3 and P5. The section-C instruction wrapped and
orphaned the page number onto its own line:

- P3 (`svg/p3-wenhua.svg`, `<text x="527" y="2115.4249999999997">3.</text>`):
  line 1 `Responde con fechas y números de la página` / line 2 `3.`
- P5 (`svg/p5-qingnian.svg`, same coordinates): line 1
  `Responde con fechas y números de la página` / line 2 `5.`

The lone `3.`/`5.` read as a phantom exercise number, and the first
section-C exercise was displaced ~30 px down (39./75. at y=2177.1 vs
2147.4 in the core).

## 2. Fix — source files changed, before/after quotes

Only the Spanish explanation string was touched. No frozen Chinese string
changed (proved by the freeze gate in §4: per-page CJK core→edition counts
identical to Round 1, added CJK 0 on every page).

The fix abbreviates `página` to the standard Spanish abbreviation `p.`,
as the proofreader suggested. It was applied in BOTH layers that carry
the string, so a rebuild from the core reproduces the fix:

### Source 1 — render source (P3)

File: `hidden_files/weekly-report-w46-zh-cn-es-build/content34.py`,
line 96, `e.glossline(...)`.

- Before: `Responde con fechas y números de la página 3.`
- After: `Responde con fechas y números de la p. 3.`

### Source 2 — render source (P5)

File: `hidden_files/weekly-report-w46-zh-cn-es-build/content56.py`,
line 91, `e.glossline(...)`.

- Before: `Responde con fechas y números de la página 5.`
- After: `Responde con fechas y números de la p. 5.`

### Source 3 — transform map (rebuild source)

File: `hidden_files/w46/maps/es.json`, the two mapping values for the
English keys `"Answer with dates and numbers from page 3."` and
`"Answer with dates and numbers from page 5."` — same before/after as
above. The English keys are unchanged; the map still has 282 keys and
re-validates as JSON. No other map entry changed, and no other edition's
file was changed by this edit (the map is only read when a build is
re-generated from the core; the other 9 editions' shipped files were
verified byte-identical before and after — see §5).

Wrap pre-check with the build's own `wrap()` (Noto Sans, size 20.5,
column width 434 px): old string 448.3 px → 2 lines (`...página` /
`3.`); new string 401.3 px → 1 line, for both `3.` and `5.` variants.
Meaning is preserved: `p.` is the standard abbreviation of `página`
("Responde con fechas y números de la p. 3." = "Answer with dates and
numbers from page 3.").

No other string in any source file was changed. Verified after editing:
the old strings `de la página 3.` / `de la página 5.` occur 0 times in
the ES build dir and in `maps/es.json`; each new string occurs exactly
once in its content file.

## 3. Re-render (full, from source)

Commands (tools venv `tools/venv/bin/python`), in the ES build dir
`hidden_files/weekly-report-w46-zh-cn-es-build/`:

1. `run.py` → `zh-cn-fix/run.log` (exit 0): TOTAL 150, levels
   A2 56 / B1 69 / B2 25, pages 10/18/18/18/18/18/12/38, writing model
   164 characters, **zero** FLOW OVERFLOW / HEAD TOO WIDE warnings
   (grep counts 0/0 in the log).
2. `render.py` → `zh-cn-fix/render.log` (exit 0): 8 cards + print PDF
   `Lucerna-VOL3-ES.pdf`, 42,127,051 bytes.
3. `.text.md` regenerated from the source manuscript with
   `hidden_files/w46/textmd.py` (run from the build dir, never
   hand-edited, never extracted from PDF). Before regenerating, the
   unchanged sources were shown to reproduce the pre-fix export
   byte-identically, so the regeneration path is verified. Diff vs the
   pre-fix export (`zh-cn-fix/textmd-before.md`): exactly 2 lines —
   line 623 (P3 string) and line 1063 (P5 string); header
   (`# 2026-w46-zh-cn-es`, `## 第 1 版 · 头版`, …) preserved verbatim.
4. Web PDF rebuilt with `tools/webpdf.py` (svg dir → 
   `Lucerna-VOL3-ES-web.pdf`) → `zh-cn-fix/webpdf.log` (exit 0):
   8 pages, 698 distinct chars, 2,497,482 bytes, 45,801 text bytes.

Change footprint (sha256 before/after, `zh-cn-fix/post-fix-es-diff.log`):
only `svg/p3-wenhua.svg`, `svg/p5-qingnian.svg`, `cards/p3-wenhua.png`,
`cards/p5-qingnian.png`, both PDFs and `2026-w46-zh-cn-es.text.md`
changed. The other 6 SVGs, the other 6 cards and `ABSTRACT.txt` are
byte-identical to the pre-fix render. (The KIT hash changed later, when
the fix record in §6 was appended — that is the only further change.)

## 4. Re-gates (on the FINAL artifacts)

Evidence files live in `hidden_files/w46/zh-cn-fix/` alongside this
report. Gate JSONs: `occlusion-zh-cn-es.json`, `freeze-zh-cn-es.json`,
`p8-extract-es.json`, `p8-zh-cn-es.json`, `counts-phrases-chart.json`,
`orphan-scan.json`; logs: `run.log`, `render.log`, `webpdf.log`,
`occlusion-selftest.log`, `occlusion-zh-cn-es.log`,
`freeze-zh-cn-es.log`, `p8-extract-es.log`, `p8-zh-cn-es.log`,
`rowcheck-zh-cn-es.log`, `orphan-scan.log`, `pdftext-web-es.txt`,
`pdftext-print-es.txt`.

### 4.1 Standalone-`"N."` scan (proofreader's scan, re-run) — PASS

Full scan of every `<text>` node in all 8 final ES SVGs
(`zh-cn-fix/orphan-scan.log`):

- Single-digit `"N."` nodes remaining: exactly 9, ALL on P1, ALL
  legitimate exercise numbers at the exercise-number offset
  (x=137/599/1061, i.e. column x + 72): `1.` (599, 1474.925), `2.` (599,
  1560.7), `3.` (599, 1646.475), `4.` (599, 1732.25), `5.` (1061, 841.8),
  `6.` (1061, 927.575), `7.` (137, 2389), `8.` (599, 2389), `9.` (1061,
  2389).
- Orphan candidates (single-digit `"N."` at an exact column-start x =
  65/527/989/1451): **[] — zero.**
- Digit-dot nodes (`N.` / `NN.` / ranges) outside exercise-number x
  positions (137/599/1061/1523): **[] — zero**, on all 8 pages.
- Section-C instruction, P3: ONE text node, x=527 y=2085.7:
  `Responde con fechas y números de la p. 3.` — page number on line 1,
  no second line. P5: same, `… la p. 5.` Stray `3.`/`5.` at x=527: 0
  on both pages.
- First section-C exercise y: 39. ES y=2147.425 = core y=2147.425;
  75. ES y=2147.425 = core y=2147.425 (was 2177.1 before the fix —
  the ~30 px displacement is gone, exercises sit at the same y as
  the core).
- A supplementary short-fragment listing (≤3-char nodes at column-start
  x) contains only pre-existing CJK body-text fragments (e.g. `波。`,
  `着。`, `KC`, `上了。`); no digit orphan and no new fragment of any
  kind. No new orphan/overflow was introduced on any page: occlusion
  0 flags and rowcheck §1 CLEAN (below) cover all 8 pages, and the
  P3/P5 change footprint above shows no other page's SVG changed at all.

### 4.2 Occlusion audit — PASS, 0 flags

`tools/occlusion_audit.py --selftest` first: selftest OK (planted
classes fired BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 1 each; clean
controls silent). Then audit of the ES svg dir: `0 flags`, exit 0
(`occlusion-zh-cn-es.json`: `flag_count` 0).

### 4.3 Freeze check — PASS, added CJK 0 every page

`tools/freeze.py diff --core-svg <core>/svg --edition-svg <ES>/svg
--strict-cjk`, exit 0:

```
p1: +47 strings / -46 strings; CJK core 932 -> edition 882; added CJK chars: 0
p2: +61 strings / -60 strings; CJK core 968 -> edition 946; added CJK chars: 0
p3: +39 strings / -38 strings; CJK core 877 -> edition 855; added CJK chars: 0
p4: +40 strings / -39 strings; CJK core 787 -> edition 766; added CJK chars: 0
p5: +39 strings / -39 strings; CJK core 901 -> edition 879; added CJK chars: 0
p6: +42 strings / -41 strings; CJK core 1019 -> edition 997; added CJK chars: 0
p7: +85 strings / -79 strings; CJK core 741 -> edition 721; added CJK chars: 0
p8: +193 strings / -196 strings; CJK core 1084 -> edition 1063; added CJK chars: 0
TOTAL added CJK characters: 0
```

P3/P5 `+39` (Round 1: `+40`) is the expected consequence of the fix:
the two-line instruction became one string. All CJK core→edition counts
are unchanged from Round 1 — no frozen Chinese string changed.

### 4.4 P8 — PASS, CLEAN 150/150

`tools/p8.py extract --p8 <ES>/svg/p8-ceyan.svg --total 150`: noted set
= 150 of 150. `p8.py compare` core vs edition: `status: CLEAN
missing=[] extra_count=0 uncertain=[] keydiff=[]`.

### 4.5 Rowcheck — §1 CLEAN

`hidden_files/w46/rowcheck.py` §1 (same-baseline collisions): all 8
pages CLEAN. §2 crashes on the hardcoded NL P6 filename
(`p6-verdieping.svg` absent) — N/A, identical to Round 1. §3 not run
(needs a core build dir; covered by freeze + P8, as in Round 1).

### 4.6 Counts re-measured — PASS

- 150 unique exercise numbers 1–150 from chip nodes (range headers
  expanded), no gaps, no duplicates.
- Level split from the driver: A2 56 / B1 69 / B2 25.
- Per-page: P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38.
- P7 phrases: all 8 exactly 2×, each 1× in its source article page +
  1× on P7: 「双11的正日子」「先看结算页，再决定买不买」
  「提高自防自救能力」「三支队进了八强」「输了就回家」
  「老电影，新画面」「快递的高峰分三波」「着火了不坐电梯」.
- P6 chart: bars x=325, widths 220/330/550/770, h=30,
  y=1274/1324/1374/1424; first fill `#3e4c2a`, rest `#b3a06a`.

### 4.7 PDFs / text layer — PASS

- Web PDF `Lucerna-VOL3-ES-web.pdf`: **2,497,482 bytes** (≤ 7 MB),
  8 pages.
- `pdftotext` web: **45,801 bytes**; print: 45,801 bytes;
  `cmp` → **byte-identical** web vs print. 45,801 is 10 bytes fewer
  than Round 1's 45,811 — exactly the 2 × 5-byte shortening
  (`página` → `p.`). Both extractions contain `de la p. 3.` /
  `de la p. 5.` and neither contains the old wording.
- Print PDF `Lucerna-VOL3-ES.pdf`: 42,127,051 bytes, 8 pages.
- `.text.md`: 42,763 bytes, 1883 lines, header preserved verbatim.

### 4.8 Visual check — PASS

- P3 card read at full frame: section C instruction complete on one
  line with its page number (`Responde con fechas y números de la
  p. 3.`), exercise 39 directly below at the same level as the
  neighbouring columns; no orphan, overflow or overlap anywhere
  on the page.
- P5 card read at full frame: same for `… la p. 5.` / exercise 75.
- P1 and P8 cards spot-checked at full frame: clean (both byte-identical
  to the pre-fix render; P8 keys end well above the footer rule).
  The builder's original visual check covered only P1/P2; this fix
  worker's check covered the two fixed pages in full plus the P1/P8
  spot check, as tasked.

## 5. Other editions untouched — verified

Pre-fix sha256 snapshot of all 189 files of the other 9 ZH-CN editions
(core + de/fr/it/ja/ko/nl/pt/ru) was re-verified after the fix:
`sha256sum -c` exit 0, 189/189 OK, 0 failures
(`zh-cn-fix/other-editions-verify.log`). No file outside
`weekly-report-w46-zh-cn-es/`, its build dir, and `w46/maps/es.json`
was modified.

## 6. Records written

- Fix record appended to the ES `WEEKLY-KIT.md` (section
  "Post-proof fix record", Fix 1), with defect/fix quotes and the
  re-gate evidence above. The KIT diff vs the pre-fix KIT
  (`zh-cn-fix/KIT-before.md`) is only that appended record; the KIT's
  "Gates (final render)" section describes the pre-fix render and the
  fix record states that its figures supersede it. W45-promise wording,
  badge and abstract untouched (ABSTRACT.txt byte-identical).
- This report: `hidden_files/w46/zh-cn-fix/FIX-REPORT.md`, with all
  render logs and gate JSONs/logs alongside it (see §4 preamble).

## 7. Fixes NOT applied as specified

- **D2 (KIT-record inaccuracies: KO total 4300→4304, JA p2 479→477,
  JA "identical" wording) was deliberately NOT applied to any edition
  content** — the verdict and the fix task both classify D2 as
  RECORD-ONLY with no edition consequence, and the task forbids
  editing edition content for it. The ES KIT does not repeat the
  refuted KO/JA figures, so no correction was needed or made there
  either; no other edition's KIT was touched. This is the only
  verdict item not applied, and it was not applied by instruction,
  not by omission.
- Nothing else in the verdict was left unapplied: D1 is fixed as
  specified (shortened Spanish instruction, page number on line 1,
  only the Spanish string touched).

## 8. Final file inventory (ES edition, post-fix)

Sizes in bytes; sha256 in `zh-cn-fix/post-fix-es.sha256` (regenerated
after the KIT record was appended, so it reflects the final state).

| File | Bytes | sha256 (first 16 hex) |
|---|---|---|
| `2026-w46-zh-cn-es.text.md` | 42,763 | `ab2f49e9cd1677c0` |
| `ABSTRACT.txt` | 579 | `ee55a061cc554e7c` |
| `Lucerna-VOL3-ES-web.pdf` | 2,497,482 | `a736d46950b513f2` |
| `Lucerna-VOL3-ES.pdf` (print) | 42,127,051 | `4809b53d528d225b` |
| `WEEKLY-KIT.md` | 11,859 | `999f29bfb8c1d237` |
| `cards/p1-touiban.png` | (unchanged) | `83aa20e04acd933d` |
| `cards/p2-shenghuo.png` | (unchanged) | `8e8a2c20ed4f84b1` |
| `cards/p3-wenhua.png` | (changed) | `3336b00cbc9e8903` |
| `cards/p4-tiyu.png` | (unchanged) | `7225112464fdff6f` |
| `cards/p5-qingnian.png` | (changed) | `18970b7fafb6714c` |
| `cards/p6-shendu.png` | (unchanged) | `3e74c70fdbac33b9` |
| `cards/p7-ciyu.png` | (unchanged) | `8cb0d3623a755b4c` |
| `cards/p8-ceyan.png` | (unchanged) | `55cfcbcb70c61a43c` |
| `svg/p1-touiban.svg` | (unchanged) | `dbe97597c005141e` |
| `svg/p2-shenghuo.svg` | (unchanged) | `97f856564fcb1f45` |
| `svg/p3-wenhua.svg` | (changed) | `e74367f9c0f28688` |
| `svg/p4-tiyu.svg` | (unchanged) | `f0fc7962b68a9a8c` |
| `svg/p5-qingnian.svg` | (changed) | `7feb0fbc6516682f` |
| `svg/p6-shendu.svg` | (unchanged) | `fb71565f19024c7a` |
| `svg/p7-ciyu.svg` | (unchanged) | `0f379db2bf009347` |
| `svg/p8-ceyan.svg` | (unchanged) | `d22fd9191c3a02c4` |

pdftotext bytes: web 45,801, print 45,801, byte-identical. Web PDF
2,497,482 bytes ≤ 7 MB. Seed record (per verdict, not re-derived):
VOL.3, 150 exercises (A2 56 / B1 69 / B2 25).
