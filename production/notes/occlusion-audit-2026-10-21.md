# Occlusion Audit — Lucerna Weekly, all shipped editions

**Date:** 2026-10-21 (audit run ~09:51–10:05 EDT)
**Scope:** 15 editions × 8 pages = 120 SVGs under `files/` — the 12 cores (vol4 FR, en/de/es/it/pt/nl/ru/ja/ko/zhcn/zhtw VOL.1) + finished fan-outs (fr-en, es-en, de-en).
**Read-only:** nothing was modified, fixed, or posted.

## Method

- Parsed every page SVG in document (paint) order (corpus is flat: 23,092 text nodes, 3,222 rects, 78 images, 24 circles, 3 paths; no transforms/opacity/tspan anywhere).
- Glyph box per text node: width measured with PIL `ImageFont.getlength` using the **exact production fonts** (Noto Sans/Serif CJK TTC, face index JP=0/KR=1/SC=2/TC=3, bold file when `font-weight=700`; UnifrakturMaguntia for blackletter) — the same measurement method as the builds' own `svglib`. Widths validated against known column widths (e.g. es P7 wrap width 434 px reproduced to <1 px). Vertical box = baseline −0.88em … +0.30em. **Tolerance:** width ±~1%; vertical box is an upper-bound ink box, so coverage % is conservative (slightly over-estimated).
- Flags: (a) ≥30% of a text node's glyph-box area covered by an opaque rect/image/circle/path painted **after** it; (b) glyphs crossing into the footer band (footer rule at y=2580 on all pages; standard footer text = size 20, baseline 2624, excluded); (c) glyph box extending beyond the page edge (1950×2700).
- Sensitivity: the 5–30% coverage band came back **completely empty** corpus-wide — flagged covers are all ≥93%, i.e. clean separation, no borderline cases.
- Every flag was then **visually verified** in the rendered card PNG (region crops at 1.4–1.8×).
- Limitation: "text outside its containing box" was assessed via the coverage/footer/edge criteria; containing boxes are not semantically marked in the flat SVGs, so a text node that sits outside its intended box but is neither covered nor in the footer band nor off-page would not be flagged.
- File-state notes: es-vol1 SVGs are the post-patch re-render of today (mtime 13:44 UTC); de-vol1 SVGs are from 06:03 UTC — the P7 patch in flight is **not yet reflected** in the files audited. de-en P6 SVG mtime 13:45 UTC.

## Confirmed defects (all visually verified in the card PNGs)

### A. Opaque-box occlusions (the target class)

| # | Edition · page | Hidden text | Covered by | Coverage |
|---|---|---|---|---|
| 1 | **de-vol1 · P6** (Vertiefung) | Article lines, col 1: „Sommerzeit wieder ein; seitdem" / „gilt sie ohne Unterbrechung."; col 2: „einig — und so blieb alles, wie es" / „ist. Die Länder konnten sich nicht" | PRO-&-CONTRA box, rect fill #f1ead6, (65,1000)–(961,1252) | 93–100% |
| 2 | **de-en · P6** (Vertiefung) | Same 4 German article lines, same coordinates | Same PRO-&-CONTRA box | 93–100% |
| 3 | **de-vol1 · P7** (Sprache) | Toolbox gloss „Es ist fraglich, ob ... = 是否……还难说" at (1473,815)–(1837,839) | LESERBRIEFE box, rect fill #f1ead6, (1451,787)–(1885,1237.5) | 100% |

- #1/#2: In the render both article columns break off mid-sentence at the box top ("…führten beide deutsche Staaten die" / "…Mitgliedstaaten wurden sich nicht") and the continuation lines exist only in the SVG text stream — each string occurs exactly **once** in the file (grep-verified: no visible re-draw). The fan-out de-en inherited the core's defect verbatim. **These two were not previously known.**
- #3 is the already-known de P7 toolbox item (patch in flight). It is **still present** in the files as they stand (SVG mtime 06:03 UTC). No *other* occlusion exists on de-vol1 P7.

### B. Footer-band intrusions (answer-key lines pushed below the footer rule, y=2580)

| # | Edition · page | Text | Visual result |
|---|---|---|---|
| 4 | **it-vol1 · P8** | „75. cosplay — cosplay = 角色扮演服装" (baseline 2588, size 14) | Footer rule strikes **through** the glyphs; line sits in the footer band above the footer text |
| 5 | **pt-vol1 · P8** | „75. local — local = 地点" (baseline 2588, size 14) | Same strike-through |
| 6 | **nl-vol1 · P8** | „150. ✓ 范文见本版 H 区（87 词）" (baseline 2589, size 14) | Same strike-through |
| 7 | **ru-vol1 · P8** | „41. c — 《神怪尤多》c" and „82. В среду я позвоню бабушке. — 时间在前；позвонить + 与格" (baselines ≈2603, size 13.3) | Both lines sit **below** the rule inside the footer band, jammed directly against the footer line (glyph boxes touch: answer bottoms ≈2607 vs footer-text top ≈2606) |

All four are legible but visibly broken layout: the last answer row(s) of the key overflowed the content area into the footer strip. In it/pt/nl the later-painted footer rule is drawn **over** the text (same "exists in text stream, drawn over in render" family, by a line rather than an opaque box).

### C. Page-edge overflow

| # | Edition · page | Text | Visual result |
|---|---|---|---|
| 8 | **en-vol1 · P1** | „“hot dog recall” 周一快照搜索量 200K+（见第 2 版）。" — single node at x=1473, size 19, measured width 488 px → ends at x≈1961 | Line overflows its column and crosses the double page frame; the final „。" is clipped at the page edge (only a sliver of the glyph is inside 1950). Rest of the line is visible — minor severity, but the sentence's closing punctuation is effectively lost |

## Artifacts dismissed

**None.** After width validation, all 15 geometric flags were visually confirmed as real (9 cover flags → defects #1–3; 5 footer-band flags → #4–7; 1 page-edge flag → #8). No zh-CN-P1-masthead-style false positives occurred in the final run.

## Clean editions (zero flags, nothing to verify)

- **weekly-report-vol4 (FR)** — clean
- **weekly-report-es-vol1** — clean **in its current post-patch files** (P7 clinic fix verified geometrically; no other occlusion anywhere in the edition)
- **weekly-report-ja-vol1** — clean
- **weekly-report-ko-vol1** — clean
- **weekly-report-zhcn-vol1** — clean
- **weekly-report-zhtw-vol1** — clean
- **weekly-report-fr-en** — clean
- **weekly-report-es-en** — clean

## Per-edition summary

| Edition | Verdict |
|---|---|
| vol4 (FR core) | ✅ clean |
| en-vol1 | ⚠️ defect #8 (P1 edge overflow, minor) |
| de-vol1 | ❌ defects #1 (P6, 4 lines hidden) + #3 (P7, known, patch not yet in files) |
| es-vol1 | ✅ clean (post-patch files) |
| it-vol1 | ⚠️ defect #4 (P8 footer strike-through) |
| pt-vol1 | ⚠️ defect #5 (P8 footer strike-through) |
| nl-vol1 | ⚠️ defect #6 (P8 footer strike-through) |
| ru-vol1 | ⚠️ defect #7 (P8 footer-band collision, 2 lines) |
| ja-vol1 | ✅ clean |
| ko-vol1 | ✅ clean |
| zhcn-vol1 | ✅ clean |
| zhtw-vol1 | ✅ clean |
| fr-en | ✅ clean |
| es-en | ✅ clean |
| de-en | ❌ defect #2 (P6, 4 lines hidden — inherited from de core) |

**Out of scope note:** `weekly-report-it-en/`, `weekly-report-nl-en/`, `weekly-report-pt-en/` directories also exist under `files/` but were not in the assigned scope (only fr-en / es-en / de-en were listed as finished fan-outs). Given de-en inherited its core's P6 defect, the remaining fan-outs (including ru/ja/ko/zh fan-outs when produced) should be audited before shipping — P8 footer overflow in it/pt/nl/ru cores will otherwise propagate the same way.
