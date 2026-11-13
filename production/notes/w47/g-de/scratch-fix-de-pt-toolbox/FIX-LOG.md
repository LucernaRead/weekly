# FIX-LOG — 2026-W47 de-pt toolbox fix (D1, pt-specific design)

- Edition: `2026-w47-de-pt` (German target × Portuguese readers)
- Fixer: de-pt toolbox fix agent (leaf). Date: 2026-11-11.
- Scratch: `hidden_files/w47/scratch-fix-de-pt-toolbox/` (FIX-LOG.md + creambox/descender/probe logs).
- Scope: ONLY the P7 toolbox (DER WERKZEUGKASTEN) geometry in `content7.py`. No other edition, no `tools/`, no shared helper, no commit, no push. Proof2 to be re-assigned by the coordinator after this fix.

## 0. Probes + SHA verification (pre-fix)

- Probe (task start, 2026-11-11 ~09:46 UTC): `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…` OK; real test file written in the scratch dir. `/tmp` was 2% used at probe time (not full); scratch `tmp/` used as TMPDIR anyway per the task.
- SHA verify (2026-11-11 09:46 UTC) — all three MATCH the brief:

| File | Bytes | SHA-256 |
|---|---|---|
| `Die-Lucerna-VOL4-de-pt.pdf` | 10,968,903 | `5f2bc3d4590fca0e6509fda53ddafe6a4b1cc618a5c23e78f5181e177143c2aa` ✓ |
| `Die-Lucerna-VOL4-de-pt-web.pdf` | 1,602,461 | `62371d80a399779aded2e9dbcd3ea303f46f338d7c9d9241dc929e4a1a0e7adb` ✓ |
| `2026-w47-de-pt.text.md` | 49,812 | `e2ee96ebd9dca775598431f87c511f53ed04dec2547896586d46a2c57a800928` ✓ |

## 1. Measured values (pre-fix — creambox.py + SVG probe + PIL descender)

- Tool: `creambox.py` copied from `scratch-fix-de-es1/` (byte-identical to the family copy in `scratch-fix-de-toolbox-family/`), run on the on-disk `svg/p7-sprache.svg`. Full output in `creambox-before.log`.
- Toolbox (col-3 rail, `fill="#f0eee5"` rect): **y=330, h=483.0, bottom=813.0**; last entry baseline **813.0**; **baseline clearance +0.0**.
  Last line (single line, 20.5pt Newsreader serif): `Es ist fraglich, ob ... = ainda duvidoso`.
- Descender (PIL render of the exact last line in `tools/fonts/Newsreader-Regular.ttf` at 10×, `descender.py`): the `g` in `fraglich` (the only descender in the last line) extends **5.2 units below the baseline**. **Ink ends 813.0 + 5.2 = 818.2 → ink clearance −5.2px**: the descender sits 5.2px BELOW the box bottom edge, on white newsprint outside the cream box. Overflow CONFIRMED in ink terms.
- Formula cross-check (independent of the SVG): Σlines = 10 over 6 entries; `tbh = 62 + (10×29.5 + 6×6) + 90 = 483.0` ✓; predicted last baseline from the real advance (`20.5 + n×29.11 + 6` per entry) = **812.99** ✓ matches the measured 813.0. The formula under-counts by 123 total (6 × 20.5 missed para offsets, partly offset by the 29.5-vs-29.11 line-height overestimate) — same family root cause as de-es fix1 §2.
- LESERBRIEFE: y=829.0, bottom=1381.5, last baseline 1371.1, clearance **+10.4** (unchanged by this fix).
- NOCH EIN WORT: y=1397.5, bottom=**1547.5**, last baseline 1504.6, clearance +42.9. Sätze-der-Woche hline at **y=1548** (stroke-width 2, spans 1547–1549): the box ends 0.5px above the line centre. **Zero slack downstream — any downward shift of the col-3 stack crosses the line.** (Also: first Sätze title baseline 1588.0, first phrase baseline 1637.0 — no interaction.)
- Box-top headroom: intro line 2 (`Esta página é só língua…`, 20pt sans, baseline 262, single line) ends in ink at ~266 (ç descender); box top 330 → **~64px of white above the toolbox**. Title ink top inside the box ~356 (baseline 372, 23pt bold sans). Growing the box upward is geometrically free up to ~44px before the intro ink is approached.

## 2. Confrontation with proof2 PROOF-NOTE.md L115

- proof2 L115: 「P7 工具盒末行距 SÄTZE DER WOCHE 分隔线 0.5px，渲染目视盒线完整、文字收进盒内，无重叠」.
- Verdict: **the「文字收进盒内」half is CONTRADICTED by measurement; the「0.5px」half is correct but refers to a different box.**
  - The 0.5px figure is the NOCH EIN WORT box (ends 1547.5 vs the 1548 line) — verified exact above, and it is untouched by this fix.
  - 「文字收进盒内」is wrong for the toolbox: the last baseline sits exactly ON the box-bottom edge (813.0 = 813.0) and the `g` descender ink extends 5.2px past it. The box line cannot be "complete with the text inside" when the ink crosses it.
  - Why the 100 dpi visual missed it: 5.2 SVG units ≈ 2.2 px at 100 dpi render, and the descender crosses a 2-unit box rule — a ~2px spill at the page edge of a cream box is below reliable visual detection. The SVG-geometry measurement (baseline + font-metric descender) is the arbiter, and it says overflow.
  - Consequence for proof2 conclusion (a): the "zero defects" verdict did not cover the toolbox clearance (proof2 ran no creambox check), so (a) was not a final sign-off for this defect class. This fix supplies the missing measurement.

## 3. Fix design (pt-specific — pad 110 is BANNED here by geometry)

- The family fix (pad 90 → 110, +20) would push the whole col-3 stack down 20px: NOCH EIN WORT would end at 1567.5, i.e. 19.5px PAST the 1548 Sätze line. Rejected — the task brief forbids it and the measurement confirms it.
- Chosen design: **grow the toolbox upward by Δ=20, bottom fixed, nothing below moves.**
  - `tbtop = CTOP − 20 = 310`; `tbh = 62 + Σ(...) + 90 + 20 = 503.0`; rect at `tbtop`; `yy3 = tbtop + 16`; `ry = tbtop + tbh + 16 = 829` (unchanged).
  - The whole toolbox block (title + 6 entries) shifts up rigidly by 20; all internal spacing, title gap, entry gaps unchanged; box bottom stays 813.0.
  - Predicted: last baseline 813.0 → **793.0**; baseline clearance **+20.0** (same class as core +18.8 and the siblings' pad-110 +19.6/+20.0); ink end 793.0 + 5.2 = 798.2 → **ink clearance +14.8**.
  - NOCH EIN WORT: still ends **1547.5** (0.5px above the 1548 line, exactly as shipped/accepted); LESERBRIEFE: still y=829, +10.4.
  - Box top 310 vs intro ink end ~266 → **44px gap remains** (was 64px); title ink top ~336, 26px below the new box top (same as before). No collision introduced.
  - Why Δ=20 and not the minimum 12: the ≥+10 target is met with margin (+20.0 baseline / +14.8 ink), it matches the family's corrected clearance class, and the headroom (44px) costs nothing. No smaller Δ buys anything.
- Alternatives considered and rejected:
  - Pad 90 → 110 (family fix): crosses the 1548 line (NOCH EIN WORT → 1567.5). Banned.
  - Shrink entries' internal title gap (`yy3 += 52` → smaller): same clearance gain but changes the internal rhythm and leaves the `tbh` formula's 62 constant stale in a second way; the upward-growth keeps the block rigid.
  - Trim NOCH EIN WORT height (150 → ~136) to make room for a downward pad shift: moves two boxes instead of one, shrinks a healthy +42.9 internal clearance, and ends the box exactly on the line unless trimmed further. More moving parts, no benefit.
- Change: `content7.py` ONLY (toolbox anchor + `tbh` + the void comment). No shared helper touched. The stale comment ("90 validated by en/fr occlusion 0 flags") is struck: that validation was void — the occlusion audit cannot see text spilling past its own box (text drawn after its box, nothing covering it), as established in de-es fix1 §2.

## 4. Rebuild + gates (to be filled)

## 4. Rebuild (rebuild 4, 2026-11-11 ~09:49–09:53 UTC)

- Command: `tools/venv/bin/python build_edition.py pt` (from `scratch-fanout-de/`;
  runs run.py → render.py → webpdf → verify → occlusion → p8 → freeze →
  pdftotext → chips → export; does NOT re-run transform, so the fix survives).
  Interpreter `tools/venv/bin/python` (PIL 13.0.0).
- Tool versions at build time: `tools/webpdf.py` UNMODIFIED in the working tree
  (no `M` in git status — unlike the es fix1 build); `tools/freeze.py`,
  `tools/occlusion_audit.py`, `tools/p8.py` show `M` — other agents' in-flight
  changes, used as-is, untouched here. Recorded in GATE-LOG.md.
- Result: **ALL GATES PASS** (see GATE-LOG.md for per-gate output).
- New deliverables:
  - Print PDF: `Die-Lucerna-VOL4-de-pt.pdf` — 10,968,902 bytes (−1 B),
    sha256 `c0019075c98389d84c3b71076d8828b9079de2e737332ff76d0fcd998a7ac4e0`
  - Web PDF: `Die-Lucerna-VOL4-de-pt-web.pdf` — 1,602,472 bytes (+11 B, < 7 MB),
    sha256 `e48265d346544f278cf25a5a040a0a5656dd7ef639480bb7ed07ad988a64282a`
  - Text export: `2026-w47-de-pt.text.md` — 49,812 bytes,
    sha256 `e2ee96ebd9dca775598431f87c511f53ed04dec2547896586d46a2c57a800928` —
    **byte-identical to pre-fix** (zero content change, as required: only
    geometry moved, no string touched)

## 5. Post-fix verification (summary — detail in GATE-LOG.md)

- creambox.py full edition: toolbox clearance **+20.0** (y=310, bottom=813.0,
  last baseline 793.0 — exactly as predicted); ink end 793.0 + 5.2 = 798.2 →
  **ink clearance +14.8**. LESERBRIEFE +10.4, NOCH EIN WORT +42.9, NOCH EIN
  WORT still ends **1547.5** — 0.5px above the 1548 Sätze line, exactly as
  shipped. Nothing below the toolbox moved. The remaining negative creambox
  rows are the matcher's known false positives (P7 −35.0 ×3 identical pre/post;
  P1 −24.0 and P2 −44.9 are next-section heads 24/44.9px below their boxes,
  inside the +45 window — geometry-verified in GATE-LOG.md; both pages'
  sources untouched, freeze shas identical to proof2).
- P7 visual (100 dpi full page + 300 dpi toolbox zoom, print; web rail
  pixel-identical, 0 pixels >60 gray of 1,312,085): last entry fully inside the
  cream box with clear cream below the `fraglich` descender; 16px gap to
  LESERBRIEFE; box top clear of the intro lines (44px gap); no collision.
- Full gates: occlusion (real run, no --selftest) **0 flags**; p8 extract
  150/150 + compare **CLEAN** keydiff [137,138,139,150]; freeze diff RC=0
  (added CJK 7, all U+3000); freeze_direct **8/8**, source PASS, P3 sha now
  fc88f676 (the driver-dir freeze-direct.json was stale rebuild-2, P3
  093cf378 — the driver does not run freeze_direct; fresh re-run in this
  scratch dir); keycheck **149/150** (Q150 truncation only); boxtitle **7/7**;
  measure **24/24**; chips 141; P8 min size **9.94pt**; print/web text-layer
  compare identical (default 50,684 B each; -raw normalised 49,500 B each);
  d2scan 60 pairs, 0 web gaps >0.5pt; German bent quotes „ 33 = “ 33 paired,
  U+201D 0 / U+2019 0; Q34 new stem 1× / old 0× in all five places; D1
  `pess.` 13 / `pers.` 0 in all five text layers (content8.py, text.md,
  P8 SVG, print P8, web P8).
- proof2 conclusion (a) is now complete for this defect class: the toolbox
  clearance — the one measurement proof2 never ran — is measured, fixed, and
  re-verified at +20.0 baseline / +14.8 ink. The proof2 L115 「文字收进盒内」
  claim is corrected by §2 above; the 0.5px NOCH EIN WORT figure stands.

## 6. Files changed

- `production/2026-w47/2026-w47-de-pt/content7.py` (toolbox anchor: `tbt = CTOP-20`,
  `tbh` +20, `yy3 = tbt+16`, `ry = tbt+tbh+16` — 1 block + comment; no string,
  no shared helper touched).
- Rebuilt deliverables in the same edition dir (SVG p7, both PDFs, text.md
  re-exported — content-identical; see GATE-LOG for new SHAs).
- `production/2026-w47/2026-w47-de-pt/WEEKLY-KIT.md` (§5 rebuild-4 subsection +
  Status line + stale-SHA correction note; numbers only, no content change).
- Notes only: `hidden_files/w47/scratch-fix-de-pt-toolbox/{FIX-LOG.md,
  GATE-LOG.md, creambox-*.log, probe_p7.log, descender.log, gates-fix1.log,
  freeze-direct.json/.log, keycheck.log, keycheck-150.json, boxtitle.log,
  measure.log, print.txt, web.txt, print-raw.txt, web-raw.txt, d2scan.py,
  d2scan.json/.log, p8extract.json (driver copy for keycheck), p7-print-100dpi.png,
  p7-toolbox-zoom.png, run-gates.sh, creambox.py (family copy), probe_p7.py,
  descender.py, tmp/}`.
- NOT touched: any other edition, `core-de/`, `tools/`, `issues/`, `covers/`,
  git index (no commit/push — the push loop owns that).
