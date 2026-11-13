# REBUILD-LOG — W47 it-ru spacing fix: patch + probe (BLOCKED)

Date: 2026-11-11 ~23:13–23:30 UTC. Worker: it-ru spacing (patch + probe + production rebuild if green).
Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-it-ru/`
(Soort filenames differ from the task text: text file is `2026-w47-it-ru.text.md`,
print PDF `La-Lucerna-VOL4-RU.pdf`, web PDF `La-Lucerna-VOL4-RU-web.pdf`.)

## VERDICT: PROBE BLOCKED — production NOT rebuilt (only svglib.py patched)

The Medium patch fixes its defect class completely (naive census 147 → 6 boundaries;
all 5 known P7 joins gone, gates 20/20, freeze 8/8). But the full naive census does
NOT reach 0 real joins: **4 real joins remain on P8** (visually confirmed fused words),
all pre-existing (identical gaps in the BEFORE production PDF) and caused by a
DIFFERENT mechanism the Medium patch cannot touch — a Newsreader PIL-vs-Pango
per-word overrun that eats the trailing-space advance at Latin→Cyrillic run
boundaries. Per the task's explicit bar ("0 joins + gates green, else report blocked
and touch nothing in production beyond the svglib.py patch"), production print/web
PDFs were NOT rebuilt and the KIT was NOT updated. See §5 for the evidence and
the proposed second fix.

## 1. BEFORE state (recorded 23:13 UTC, before any edit)

| File | Bytes | MD5 | SHA-256 |
|---|---|---|---|
| `2026-w47-it-ru.text.md` | 67,731 | a4549563f7a5808a8aa201e5eda8749d | 47c0471515d3b249855e33a290d0c4259ecce431995db45ac0ce926cf5a52b1d |
| `La-Lucerna-VOL4-RU.pdf` (print) | 14,180,915 | 150ba76308a7049daff2ba4d220668f5 | 966a9d10c033ed0297cef6d018b23a548dec2b016bc0eb3ecf61440ac2247666 |
| `La-Lucerna-VOL4-RU-web.pdf` (web) | 1,441,243 | afc0c3a259289d5607f8ef531220b9ad | a34df9b05c6c199800509bfaf335fe896635f623d985030f28ecfa41b2e569bc |
| `svglib.py` | 20,722 | c70b49c04e6b1210d93d07d339698a6c | — (0 "Medium" mentions) |

## 2. Patch (4-line Medium fix, identical to ru-de)

`svglib.py` copied from `2026-w47-ru-de/svglib.py` (the two files differed ONLY in
the patch lines, verified by `diff` before copying): the 4 `_NOTO_M/_NOTO_MI/
_SANS_NOTO_M/_SANS_NOTO_MI` constants + why-comment, `_PATH` entries
`("serif",False,"noto"/"noto_i")` and `("sans",False,"sans_noto"/"sans_noto_i")`
repointed at them, plus the one comment line `NotoSerif-Italic` →
`NotoSerif-MediumItalic` (part of the ru-de patch as shipped).

- AFTER: md5 `781059e6784b789c1179446e15b8f6ad`, byte-identical to ru-de (`diff` RC=0),
  7 "Medium" mentions, 21,625 bytes, mtime 2026-11-11 23:16:55 UTC.
- text.md SHA unchanged at every later check (final: same as BEFORE above).

## 3. Probe build (scratch only)

- `tools/venv/bin/python tools/run_build.py --build production/2026-w47/2026-w47-it-ru
  --out tools/scratch/run-build/it-ru-spacing --steps run,render` → RC=0;
  run.py TOTAL 150 (A2 47 / B1 70 / B2 33), render.py RC=0, print PDF 14,180,260 B;
  wrapper integrity: "production unchanged (41 files re-hashed)".
- `tools/webpdf.py <scratch>/build-copy/svg <scratch>/build-copy/La-Lucerna-VOL4-RU-web.pdf`
  → 1,440,577 B, 53,009 text bytes, RC=0.
- Probe PDF SHAs: print `2c043ad9bd6608db7b5c9676f988a75743bf69cd8982a9ee23c49567102f558f`,
  web `7cc8075dd2b06843675a33396abdfa9d3d83066ae4ebe7f41e17220a976e1276`.
- Production SHAs re-verified immediately after the probe: identical to BEFORE.
- Second independent rebuild (`--out tools/scratch/run-build/it-ru-spacing-2`,
  TOTAL 150 again) → **8/8 SVG SHA match** vs first probe build (freeze/reproducibility).
  The `-2` dir was deleted after recording (log copies kept here as `run-build-1.log`,
  `run-build-2.log`); the first probe build is kept at
  `tools/scratch/run-build/it-ru-spacing/build-copy/`.

## 4. Census (PyMuPDF char gaps, token-split — `census.py`, copied verbatim from the ru-de probe)

Naive full census, text.md vocabulary, print AND web (identical counts in both):

| | BEFORE (production) | PROBE (scratch) |
|---|---|---|
| distinct join tokens | 78 | 6 |
| total join boundaries | 147 | 6 |

The 5 known P7 joins (coordinator's checklist): **all gone as tokens** —
`Триуровня`, `Говоритео планах в будущемвремени`, `употребляетсяс`,
`ИТАЛЬЯНСКИЙЕЖЕНЕДЕЛЬНИК` absent from the probe census; the long token
`КомандаГаттузоостаётсянепобеждённойпосле` split into separate words
(`Команда`, `Гаттузоостаётся`, `непобеждённой`, `после`, …).

Remaining 6 probe hits, adjudicated by direct ink-gap measurement
(`gap_probe.py`, PyMuPDF rawdict char bboxes) + visual raster check
(`p7-gattuzo.png`, `p7-tekst.png`, `p8-*.png` in this dir):

| Token | Page | Probe gap | BEFORE gap | Verdict |
|---|---|---|---|---|
| `Гаттузоостаётся` | 7 | 2.05 pt | 0.48 pt | FALSE POSITIVE — visually a clear, normal space (narrow only because о–о round/round bearings; P7 normal separated-gap range starts at 2.0 pt; same-line neighbours 3.16–3.35 pt) |
| `Текстещё` | 7 | 1.97 pt | 0.86 pt | FALSE POSITIVE — visually a clear space; neighbours 2.69–3.29 pt |
| `Festivalзакрывается` | 8 | **0.03 pt** | 0.03 pt | **REAL JOIN — visually fused, no space. UNCHANGED by the fix.** |
| `DPBотправлен` | 8 | **1.25 pt** | 1.25 pt | **REAL JOIN — visually fused. UNCHANGED by the fix.** |
| `24гола` | 8 | **1.39 pt** | 1.39 pt | **REAL JOIN — visually fused. UNCHANGED by the fix.** |
| `BookCityоткрывается` | 8 | **1.06 pt** | 1.06 pt | **REAL JOIN — visually fused. UNCHANGED by the fix.** |

Calibration (probe print PDF, PyMuPDF `get_text("words")` inter-word gaps):
P7 (14.62 pt sans): 552 gaps, min 2.0 / p5 3.02 / median 3.75 pt.
P8 (9.75 pt): 1,741 gaps, min 1.46 / p5 2.10 / median 2.38 pt; same-type
Latin→Cyrillic boundaries that PyMuPDF separates measure 1.80 pt
(`BookCity|проходит`, `BookCity|начинается`) and 2.13 pt (`24|гола`, line 8)
— the four residuals (0.03–1.39 pt) sit well below that.

## 5. Root cause of the 4 remaining P8 joins (measured, distinct from the Medium defect)

All four sit at a Newsreader-run → Noto-Serif-run boundary where the space is the
TRAILING character of the Newsreader `<text>` element
(e.g. `69. A — Filmmaker Festival ` → `закрывается`; SVG x 538.5 → 702.7,
byte-identical in BEFORE and probe SVGs). The next run's x comes from PIL
`getlength` of the Newsreader run INCLUDING the trailing space — but CairoSVG
renders that run WIDER than PIL measures it, so the rendered ink overruns into
the space. Isolated CairoSVG-vs-PIL ground truth (`render_truth.py`, same strings,
font-size 13, Newsreader):

| Run string | PIL len (trimmed) | CairoSVG ink width | Overrun | Trailing-space advance | Resulting gap |
|---|---|---|---|---|---|
| `8. B — 24 ` | 53.73 | 54.0 | +0.27 | 3.17 | 2.13 pt (separate words) |
| `114. A — 24 ` | 69.36 | 71.0 | +1.64 | 3.17 | 1.39 pt (JOIN) |
| `91. A — DPB ` | 73.31 | 74.0 | +0.69 | 3.17 | 1.25 pt (JOIN) |
| `119. A — BookCity ` | 110.83 | 113.0 | +2.17 | 2.88 | 1.06 pt (JOIN) |
| `69. A — Filmmaker Festival ` | 161.03 | 167.0 | **+5.97** | 3.17 | 0.03 pt (JOIN) |
| `65. B — BookCity ` | 103.00 | 104.0 | +1.00 | 2.88 | 1.80 pt (separate) |

(SVG units; PDF pt = ×0.75. The overrun grows with specific character content —
a PIL-vs-Pango shaping/kerning difference on Newsreader runs, not a face mismatch.
The Medium patch cannot affect these boundaries: they depend only on Newsreader
measurement, which the patch does not touch. The same mechanism also leaves the
two P7 residuals narrow: `Гаттузо` overrun +1.35 and `Текст` +2.50 SVG units at
19.5 pt in NotoSans-Medium — but there the 4.3-unit CJK-SC space advance still
leaves a visually normal gap.)

**Proposed second fix (for the coordinator, not attempted here):** the trailing
space inside a mixed run is fragile for the same reason the LEADING space was
(D1 fix, 2026-11-09, in `svglib.py` `Page.text`): emit the trailing space as its
own `<text>` element measured in the space's own font, or measure Newsreader runs
with the renderer's shaping (Pango-equivalent widths). Then re-probe it-ru and
sweep the other editions' P8 answer keys for the same Latin→Cyrillic pattern
(same boundary shape exists wherever a Newsreader run ending in a Latin word is
followed by Cyrillic).

## 6. Gates on the probe build — 20/20 PASS

`gates-probe.py` (copy of `scratch-fix-it-ru1/gates.py`, repointed at the probe
build-copy; own outputs under this dir, `ru/`): **GATES ALL PASS** —
occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff [137,138,139];
freeze diff 0 unexplained (P1–7); strict-CJK added = 8×U+3000 only; print/web
text multiset identical (7,696 words each, chars equal); web 1,440,577 B < 7 MB;
print 14,180,260 B sane; P8 min font 13.0 px = 9.75 pt; §1.1 scans pass
(paper #fbfaf6, no gold/near-black, VOL.4×9, VOL.5×3 legitimate, badges OK,
no double frame); textmd validate 0/0; answers 150/150; keys 1–150 match core
(except 137–139 + writing); notes match translations.py.

Note: an earlier gates run in this session accidentally ran with the UNPATCHED
paths (a `sed` quoting failure stopped the repoint chain) against the stale D-1
rebuild dir `scratch-fix-it-ru1/rebuild/` and its freeze-diff FAILED there
(P7 `verbo è leggere, irregolare al futuro:` unexplained vs core `regolare`) —
that dir's P7 SVG (mtime 21:09:46) now contains `irregolare` where core-it and
this probe contain `regolare`; it changed after its own gates passed at ~21:07.
That failure is about the stale shared dir, NOT this probe (probe freeze diff is
clean). Side effect of the misfire: it overwrote `scratch-fanout-it/ru/
{p8-extract,p8-compare,freeze-diff}.json` (regenerable intermediates, same
edition — per FIX-LOG §59 precedent); this probe's own JSONs live in this
dir's `ru/` instead.

## 7. Production final state (23:30 UTC)

- `svglib.py`: md5 `781059e6784b789c1179446e15b8f6ad` (patched — the only production change).
- `2026-w47-it-ru.text.md`: md5 `a4549563…`, sha256 `47c04715…`, 67,731 B — UNCHANGED.
- Print PDF: md5 `150ba763…`, sha256 `966a9d10…`, 14,180,915 B — UNCHANGED (mtime 21:47:50).
- Web PDF: md5 `afc0c3a2…`, sha256 `a34df9b0…`, 1,441,243 B — UNCHANGED (mtime 23:01:22).
- KIT NOT updated; no commit/push/lint; no other edition touched.
- The production print PDF still carries the 5 P7 joins (0.48–1.89 pt) and the
  4 P8 joins — the probe build fixes P7 only. Awaiting coordinator decision:
  (a) waive the 0-joins bar for the pre-existing P8 class and rebuild production
  now (strictly better: P7 fixed, P8 unchanged, gates green), or (b) hold the
  rebuild until the §5 Newsreader fix lands and re-probe to a true 0.

## Files in this scratch dir

- `REBUILD-LOG.md` (this file), `census.py` (ru-de probe's script, verbatim),
  `gap_probe.py` (ink-gap measurement), `calib.py` (page gap distributions),
  `render_truth.py` (PIL-vs-CairoSVG ground truth), `gates-probe.py`,
  `translations.py` (copy for the gates), `ru/` (gates JSONs),
  `run-build-1.log`, `run-build-2.log`, `p7-gattuzo.png`, `p7-tekst.png`,
  `p8-festival.png`, `p8-dpb.png`, `p8-24gola.png`, `p8-bookcity.png`
  (visual crops from the probe print PDF), symlink `2026-w47-it-ru` →
  `tools/scratch/run-build/it-ru-spacing/build-copy/` (kept probe build).
