# GATE-LOG — 2026-W47 nl-it delta, build 6 (2026-11-11)

All gates run against the scratch rebuild
(`rebuild/2026-w47-nl-it/`) unless noted; evidence files in `gates/`.
Staging = build 5 (`production/2026-w47/fanout-nl/2026-w47-nl-it/`).

## Build

| gate | result | evidence |
|---|---|---|
| `run.py` rc | 0, TOTAL 150, by page 10/18/18/18/18/18/12/38, A2 46 / B1 73 / B2 31; zero FLOW OVERFLOW / HEAD TOO WIDE | `rebuild/run.log` |
| `render.py` rc | 0; print PDF 12,667,201 B | `rebuild/render.log` |
| `webpdf.py` rc | 0; web PDF 1,610,237 B < 7 MB, 46,510 text bytes | `rebuild/webpdf.log` |
| SVG change scope | only `p4-sport.svg` (D11) + `p8-toets.svg` (D9) vs build 5; other 6 byte-identical | `svg-hashes-before.txt`, `svg-hashes-after.txt` |

## Geometry

| gate | result | evidence |
|---|---|---|
| `tools/occlusion_audit.py svg/` | selftest OK (all 6 planted classes fired, clean controls silent); **0 flags** | `gates/occlusion.log`, `gates/occlusion.json` |
| Creambox / spill sweep (fix5 method) | **0 spills**. 28 BELOW/ABOVE hits, all independent blocks at +24/+60px (section heads, captions, photo credits, notes, gloss boxes) — adjudicated, none is box content. The P4 D11 box has no below hit at all. 7px strip below every cream-box bottom: **0 non-paper pixels** on card PNGs | `gates/spill.log` (`spill_creambox.py`) |
| D11 double measurement | SVG: box bottom 1229.6, last baseline 1209.49, margin **+20.11px**. PIL 4× mask true ink bottom 1209.74, margin **+19.86px**. Delivered print-PDF 150dpi render: lowest ink row 1209.60, margin **+20.00px**; 7px strip below box bottom **0** non-paper pixels | `gates/spill.log`, `gates/pdf-probe-d11.log` (`pdf_probe_d11.py`) |

Method notes:

- `occlusion_audit.py --selftest` runs ONLY the synthetic selftest (it
  returns before auditing); the first two runs in this task audited
  nothing. The recorded run is WITHOUT `--selftest`: selftest OK + 0 flags.
- The spill sweep's original SIDE class was dropped: as first written it
  flagged every text in a neighbouring column (527 hits, all noise). The
  kept BELOW/ABOVE classes only count texts in the box's own column.
- The first 7px-strip probe showed two 422px hits (P2 bottom 1445.8,
  P4 bottom 1111.8) — exactly one row of the box's own cream fill:
  the strip started at `int(bottom)`, one row inside fractional-bottom
  boxes, and cream `#f0eee5` trips the paper threshold (blue 17 > 12),
  the fix3 artifact. Re-probed from `ceil(bottom)`: 0 everywhere.

## P8 / keys

| gate | result | evidence |
|---|---|---|
| `tools/p8.py extract --total 150` | noted set **150/150** | `gates/p8-extract.json` |
| `tools/p8.py compare` core vs edition | **CLEAN**, missing [] extra [] uncertain [], keydiff **[137, 138]** — the two translation items whose keys are reader-language by design (Italian vs Chinese in core). Pre-build keydiff was [137, 138, 140]; D9 removed 140 | `gates/p8-compare.json`, `gates/p8-compare.log` |
| Three-way registry / text.md / P8 | **149/149 MATCH**, DIFF 0, MISSING 0; only #150 differs (open-writing exception: registry `(compito aperto, testo modello sotto)`, text.md 81-word Tekstmodel, P8 key `✓`). Match keys 25–28 = d/c/a/b, 141–144 = b/c/d/a (same as core). Q140 three-way: `Ik maak een surprise met een kort gedicht.` in all three | `gates/threeway.log`, `gates/p8-compare-threeway.json`, `gates/registry.json` (`threeway.py`) |
| P8 answer-zone min font | **10.12pt** (print and web) | `gates/textlayer.log` |

## Text layer

| gate | result | evidence |
|---|---|---|
| Print vs web, per page (PyMuPDF, 0.3pt) | content-multiset diff **0**, positional diff **0**, all 8 pages; tokens 220/202/187/185/194/200/186/384 = 1,758 | `gates/textlayer.log` (`textlayer.py`) |
| `pdftotext` bytes | print 46,510 = web (new) 46,510; staging both 46,500 (+10 = D9 words) | `gates/textlayer.log` |
| New vs staging content diff | exactly the two changed P8 spans (stem `+breve`, key `+kort`), nothing else, on print AND web | `gates/textlayer.log` |

Note: the first textlayer run compared (x, y, text) tuples, so P1's
known 0.2pt `De`/`Lucerna` font-subset micro-shift showed as
multiset-diff 2 / positional-diff 1. The corrected script compares
content multisets separately from positions (0.3pt tolerance): both 0.
The pdftotext +10 (vs +11 of added word bytes) is one space dropped at
a wrap boundary — same class as core fix3's note; the token diff above
is authoritative and exact.

## Freeze

| gate | result | evidence |
|---|---|---|
| `tools/freeze.py baseline` core-nl (control) | **8/8 MATCH**; shipped core SVGs verified unchanged by the run | `gates/freeze-core.log` |
| `tools/freeze.py baseline` edition self-freeze (clean-dir re-run) | **8/8 MATCH** | `gates/freeze-self.log` |

## Orphan punctuation

| gate | result | evidence |
|---|---|---|
| Full-edition sweep, all 8 pages (fix4 method: baseline groups, >60px x-gap segments) | 1,451 line segments; class (a) lone closer **0**; class (b) line-initial closer **0**; brute-force closer-leading elements **0**, leftmost **0** | `gates/orphan.log` (`orphan_sweep.py`) |

## Visual (crops from rebuild cards, viewed by eye)

| crop | verdict |
|---|---|
| `crop-p4-programma.png` | `18:45 uur.` inside the cream box, clear margin below ✓ |
| `crop-p8-q140.png` | `140. Ik maak een surprise met een kort gedicht. — surprise è un'espressione fissa` ✓ |
| `crop-p8-q140-stem.png` | `Faccio una surprise con una breve poesia. → ___` ✓ |
| `crop-p3-d6.png` | bridge 2 lines, ends `hebben/zijn.` ✓ |
| `crop-p7-d7.png` | gloss bridge 3 lines, ends `scoren segnare.` ✓ |
| `crop-p6-d8.png` | caption 4 lines, ends `(100 giovani)` ✓ |
| `crop-p7-d10.png` | letters 2 lines, ends `VOL.5.` ✓ |

## Verdict

All acceptance gates pass: run.py rc=0 TOTAL 150; occlusion 0; p8 CLEAN
(keydiff [137,138]); freeze core 8/8 + edition 8/8; print/web text diff 0;
orphan 0 new; spill 0; P8 min font 10.12pt; 150 keys 149/149 MATCH.
SVG changes only p4 (D11) + p8 (D9); other pages byte-identical to staging.
