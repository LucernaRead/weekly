# FIX-LOG-2 — 2026-W47 pt-ru: P1 masthead collision + 3 box-title overflows

Date: 2026-11-13 ~01:30–01:55 UTC. Worker: fix-pt-ru2 (scratch-fix-pt-ru2/).
Scope: ONLY `2026-w47-pt-ru`. No commit, no push, no other edition touched. P7 not touched.

## 1. Defects (4 items, all P1, one root cause)

Source: pt-family re-proof (worker a351c48a, 10/11 CLEAN) + final gate run
(worker 2a3d31a7, `scratch-gate-pt-ru-final/GATE-REPORT.md`). Root cause:
fix-xru font change (Latin Noto Sans CJK → wider Newsreader) widened the
P1 Latin titles +34–45u, pushing the Russian glosses out of their boxes.
Pre-fix state: run2 build, print `1e0ef0e66a0f…` (2026-11-13 00:25 UTC).

| # | Where | Pre-fix measurement |
|---|---|---|
| F1 | P1 top strip, y=92 | Slogan `Португальский, который читает Бразилия` vs date `SEMANA DE 16 A 22 DE NOVEMBRO DE 2026`: final `я` covered by `S`, reads "…БразилSEMANA DE 16…". Occlusion `[TEXTX] … overlaps 'Бразилия' by 19.9x12.5px`; gates.py collision 21.9. Other 10 pt editions: 90–116px whitespace (measured from their SVGs). |
| T1 | P1 numbers box | `A SEMANA EM NÚMEROS　Цифры` ink-right 1436.1 vs box-right 1411.5, over **+24.6px** (core −18.0; pre-fix-xru clearance +20.5). |
| T2 | P1 contents box | `NESTA EDIÇÃO　В этом номере` ink-right 1867.8 vs box-right 1862.0, over **+5.8px** (core −22.0; pre-fix-xru clearance +28.5). |
| T3 | P1 brief box | `EM POUCAS PALAVRAS　Коротко` ink-right 1895.3 vs box-right 1862.0, over **+33.3px** (core −22.0; pre-fix-xru clearance +8.5) — 11.3u past the 1884 page-right edge, the only out-of-page element; cream box ends mid-word, gloss hangs on white. |

## 2. Fixes (content12.py + tables_ru.py in sync; only delete words, never add)

- **F1** (`content12.py:15`): slogan → `Португальский, читаемый в Бразилии`
  ("Portuguese read in Brazil", same meaning) **and** centre-line
  letter-spacing 1.7 → 1.0 (that line only). Measured first: wording alone
  was NOT enough — a centred line moves only half the saved width
  (predicted gap ≈ 0px), so the tracking trim was required. The date
  cannot move right (its ink already ends at 1884.9, the page edge).
- **T1** (`content12.py:43`): wording kept, `f.box(..., tsize=20)` (was 23).
  Wording-only deletion of "A " left +4.3px over, so the size cut was used.
  (Side effect: box height −3px, flow below shifts up 3px; gates verify.)
- **T2** (`content12.py:89`): `В этом номере` → `В номере` (size kept 24).
- **T3** (`content12.py:139`): wording kept, size 24 → 20 (same size as
  pt-de/fr/es use for this exact title).
- `tables_ru.py` in sync: "本期目录" → `В номере` (L138),
  "读巴西人正在读的葡萄牙语" → `Португальский, читаемый в Бразилии` (L201).
  (Fanout snapshot `scratch-fanout-pt/tables_ru.py` still has the old
  strings — not a build input; noted for the next fanout.)

Post-fix margins (SVG ink vs box-right): F1 gap +28px at 200dpi (see §4);
T1 ≈ +31px (ink ≈1380.5 vs 1411.5); T2 ≈ +61px (ink ≈1801.1 vs 1862.0);
T3 ≈ +39px (ink ≈1823 vs 1862.0, inside the page edge).
Only `svg/p1-capa.svg` changed; p2–p8 SVGs byte-identical.

## 3. Rebuild (scratch-first, then sync)

Built in `scratch-fix-pt-ru2/2026-w47-pt-ru`:
`run.py` TOTAL 150 RC 0, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE →
`render.py` RC 0 → `webpdf.py` RC 0.
Synced to production: `content12.py`, `tables_ru.py`,
`svg/p1-capa.svg`, `A-Lucerna-VOL4.pdf`, `A-Lucerna-VOL4-web.pdf`,
`cards/p1-capa.png`. Production SHAs re-hashed = scratch SHAs.

## 4. P1 header re-verification (200dpi print-PDF render)

- Post-fix strip reads `…читаемый в Бразилии　SEMANA DE 16 A 22 DE NOVEMBRO DE 2026`:
  last slogan ink column 2916, date ink starts 2945 → **28px clear at 200dpi**.
  Pre-fix strip shows the merged "БразилSEMANA" cluster.
  Files: `crop-strip-{pre,post}.png`, `crop-strip-full-{pre,post}.png`.
- Three box-title crops viewed: each title ends inside its cream box with
  whitespace to spare. Files: `crop-box-{numeros,nesta,poucas}-post.png`
  (pre-fix counterparts saved alongside).

## 5. Gates (re-run on production files, 2026-11-13 ~01:48 UTC)

| Gate | Result |
|---|---|
| p8 extract/compare --total 150 | CLEAN, 150/150, keydiff=[137, 138] (adjudicated) |
| occlusion (edition + core-pt) | **0 flags** (was 1 TEXTX) |
| spill_sweep | 0 SPILL, 153 OBSERVE |
| boxtitle_check | **0 DEFECT**, 0 OBSERVE, 0 marginal (was 3 DEFECT). Note: T1/T3 titles at 20pt fall below TITLE_MIN_SIZE 22 and count as body lines (36 titles / 523 body vs 41 / 519), but the over-check covers every in-box element, so 0 flags is genuine. |
| pdf_edge_scan | 0 TOUCH, 0 NEAR; P1 min right 47.6pt (was 41.0pt) |
| D5 census | PASS (D5_lat=0, D5_cyr=0, curly 4 in Newsreader) |
| probe_xru | pt-ru `LAT@NotoSans=0 LAT@Newsreader=21000 CYR@NotoSans=4728` (CYR −8 = the two wording changes; LAT unchanged) |
| gates.py | **15/16** — only the known P7-quotes TOOL ARTIFACT (adjudicated in GATE-REPORT.md; all 8 RU translations + page tags present in the print text layer; P7 untouched per coordinator instruction). Collision check now PASS, 0 collisions. |
| freeze baseline / diff | 8/8 byte-identical; diff vs core-pt added CJK 9 / Latin 135 (same as pre-fix) |
| text layer print vs web | multiset IDENTICAL (35,274 non-space chars each; 54,913 B each) |
| text layer pre vs post | differs by exactly the two intended wording changes: only-in-pre `о×3, т×3, р×1, к×1, я×1, э×1`; only-in-post `и×1, в×1` (net −8 chars) |

## 6. text.md

**Unchanged.** None of the four strings appears in it. Re-exported with
`scratch-fanout-pt/textmd.py` (core `2026-w47-pt-zh-cn.text.md` → ru)
from the post-fix sources: diff **0 lines**, SHA unchanged.

## 7. SHAs

- **New (verified on production files):** print
  `aa12589623efdf9b2f81c12a381f9d67ad7f6e437b811d997d3bf456660fd42a`
  (12,583,100 B); web
  `15c0ddf67c2c2118f91d58c89e482b4183cd008bceb5d5ddf75db199a9421916`
  (1,202,092 B); text.md unchanged
  `87871659c0101a9d8c2f7bc415946653ea80257032332cda8b1208e6288184c8`
  (39,736 B).
- **Old (run2 build, history):** print
  `1e0ef0e66a0f180bbe012b917ad5715a54a37770e93b010ff4eed3e001b07e19`
  (12,583,257 B); web
  `9dceaf0c475ab695ec76f94bb05f665c91dc2d8c05f64eb52672de19b6d6256a`
  (1,202,246 B).

## 8. KIT

`WEEKLY-KIT.md` updated: §6 gates.py 15/16 (P7 artifact), occlusion 0
flags, print/web SHAs + sizes + text bytes; fix-xru HEAD TOO WIDE bullet
marked resolved (run2, 2026-11-13 00:25 UTC); new `fix-pt-ru2` section
appended with the full record above.

## 9. Tool debt found (not a gate failure)

The shared `run_gates.sh` (copied from `scratch-gate-pt-ru-final/`)
normalise one-liner truncates `print.txt`/`web.txt` to 0 bytes before
reading them (`open(p,'w')` is evaluated before the inner `open(p).read()`),
so its text-layer multiset check is vacuous (0 == 0) and its greps all
read 0. The 2026-11-13 01:01 gate run has the same defect (its "35,282
chars" figure came from a separate measurement). This round's text-layer
verdicts come from fresh extractions without that step (see
`prod-gates/print.txt`, `prod-gates/web.txt`, 54,913 B each). Fix the
script before the next gate run.

## 10. Files changed (not committed, not pushed)

Production `2026-w47-pt-ru/`: `content12.py`, `tables_ru.py`,
`svg/p1-capa.svg`, `A-Lucerna-VOL4.pdf`, `A-Lucerna-VOL4-web.pdf`,
`cards/p1-capa.png`, `WEEKLY-KIT.md`. Nothing else in the repo touched
(the text.md exporter also wrote its normal diff report
`scratch-fanout-pt/ru-textmd-diff.json`).

## 11. Logs

All under `hidden_files/w47/scratch-fix-pt-ru2/`: this file,
`measure.py`, `presnap.sha256`, `presnap-svg.sha256`, `pre-print.txt`,
`pre-web.txt`, `build-run.log`, `build-render.log`, `build-webpdf.log`,
`run_gates.sh`, `gate-run.log` (scratch gates), `run_gates_prod.sh`,
`prod-gates/` (production gates + fresh text layers),
`textmd-export.log`, `p1-{pre,post,prod}-1.png` (200dpi P1 renders;
prod render SHA = scratch render SHA), `crop-strip-*.png`,
`crop-box-*.png`.
