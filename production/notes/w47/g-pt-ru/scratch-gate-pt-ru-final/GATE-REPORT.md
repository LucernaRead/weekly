# GATE REPORT — 2026-W47 pt-ru FINAL (run2 build, post HEAD TOO WIDE fix)
Date: 2026-11-13 ~01:01–01:10 UTC. Runner: W47 recovery coordinator #4 gate worker.
Scope: read-only. All logs/JSONs/crops in this scratch dir.
Production dir untouched: 48-file presnap sha256 verified 0 changes after the run.

## Identity (disk, 2026-11-13 00:25 UTC build)
- Print `A-Lucerna-VOL4.pdf`: `1e0ef0e66a0f180bbe012b917ad5715a54a37770e93b010ff4eed3e001b07e19`, 12,583,257 B, 8 pp
- Web `A-Lucerna-VOL4-web.pdf`: `9dceaf0c475ab695ec76f94bb05f665c91dc2d8c05f64eb52672de19b6d6256a`, 1,202,246 B, 8 pp
- text.md `2026-w47-pt-ru.text.md`: `87871659c0101a9d8c2f7bc415946653ea80257032332cda8b1208e6288184c8`, 39,736 B — UNCHANGED (== pre-fix-xru / re-proof value)
- Note: these differ from worker C's fix-xru build (print a96fd4c4…/12,583,263; web f03415df…/1,202,236) — expected, run2 rebuilt after the P2 title change.

## Verdicts
| # | Gate | Result | Evidence |
|---|---|---|---|
| 1 | p8 compare --total 150 | **PASS** | CLEAN; core 150 / edition 150 noted; missing=[] extra=0; keydiff=[137,138] (same adjudicated non-defects as re-proof). `p8-compare.json` |
| 2 | occlusion audit | **FAIL — 1 flag** | `[TEXTX] p1-capa 'SEMANA DE 16 A 22 DE NOVEMBRO DE 2026' overlaps 'Бразилия' by 19.9x12.5px`, rc=1. Core-pt 0 flags. `occlusion.json` |
| 3a | spill_sweep | **PASS** | 31 boxes, 153 candidates, 0 SPILL, 153 OBSERVE, rc=0. `spill/` |
| 3b | boxtitle_check | **FAIL — 3 DEFECT** | P1 'Цифры' over +24.6 (core −18.0); P1 'номере' over +5.8 (core −22.0); P1 'Коротко' over +33.3 (core −22.0); 41 titles, rc=1. `boxtitle/2026-w47-pt-ru.json` |
| 3c | pdf_edge_scan | **PASS** | 8 pages, 0 TOUCH, 0 NEAR; P1 min right 41.0pt. `edge/` |
| 4 | D5 census + xru probe | **PASS** | svglib.py `_D5_READER="ru"` L100; `"ru"` branch removed w/ `[removed 2026-11-12 fix-xru]` marker L140; Latin→Newsreader by cmap. Probe: pt-ru LAT@NotoSans=0, LAT@Newsreader=21000, CYR@NotoSans=4736 (all 11 *-ru LAT@NotoSans=0). Census: D5_lat=0 D5_cyr=0, curly 4 in Newsreader, CENSUS PASS. `census.json`, `probe-post.json` |
| 5 | text-layer multiset | **PASS** | print vs web IDENTICAL (35,282 non-space chars, 54,920 B each). Current print vs fix-xru pre-text: differs by exactly {'C':1,'O':1,'M':1} = the intended "COM" removal, nothing else. P2 title "COMPLETE OS NÚMEROS" ×1 in print+web; "COMPLETE COM OS NÚMEROS" ×0. measure3.json pt-ru overhang_pixel −34.9u (in column). |
| 6 | freeze | **PASS** | baseline 8/8 SVGs byte-identical on rebuild, rc=0 (`freeze-pt-ru.log` in gate-run.log; out dir removed after, 27M). Diff vs core-pt: added CJK 9× U+3000 only (same as re-proof). |
| 7 | format | **PASS** | 8 pages both PDFs, 1462.5×2025pt; VOL.4 present (print "VOL. 4" ×1, "VOL.4" ×9); web 1,202,246 B < 7MB; text layer present. |

## Adjudication of the FAILs (all real, all in the delivered PDF)
- **Boxtitle ×3 — REAL, pixel+visual confirmed.** Re-proof's own inkprobe.py re-run on current SVGs: 'A SEMANA EM NÚMEROS' ink-right 1436.1 vs box 1411.5 (clear −24.6, was +20.5 pre-fix); 'NESTA EDIÇÃO' 1867.8 vs 1862.0 (−5.8, was +28.5); 'EM POUCAS PALAVRAS' 1895.3 vs 1862.0 (−33.3, was +8.5). Crops `crop-p1-box-numeros/nesta/poucas.png`: cream box ends mid-gloss, "Цифры"/"Коротко" hang outside the box on white. 'Коротко' ink reaches 1895.3u — 11.3u past the 1884 page-right boundary (inkprobe §A: sole element beyond 1884 on any page); edge-scan P1 min-right 41.0pt (=54.7u → ink at 1895.3u) corroborates.
- **Occlusion TEXTX ×1 — REAL, pixel confirmed.** P1 top strip, baseline y=92: "Бразилия" (x=1353.0, Noto Sans 17pt, ls 1.7) vs date line "SEMANA DE 16 A 22 DE NOVEMBRO DE 2026" (x=1413.1, Newsreader). Connected-component analysis of the 200dpi print-PDF render: glyph pitch ~11.5u/char puts "л/и/я" at ~1412.6/1424.2/1435.8u, colliding with "S/E/M" at 1413.1/1426/1438u — merged components at 1412.5–1422.1 / 1425.9–1435.5 / 1437.9–1455.2u. Crop `crop-p1-strip.png` shows the garbled "яSE" cluster.
- **Root cause (both):** fix-xru font change — Latin Noto Sans CJK → wider Newsreader. P1 title Latin parts widened +34–45u, pushing the Cyrillic glosses past their boxes; the P1 strip x-positions were computed under old metrics. The fix-xru rebuild driver ran NO occlusion/boxtitle/gates, so this was never gated. Re-proof (pre-fix build 86447421) was clean on all of these (gates 16/16, occlusion 0, inkprobe clearances positive).
- **gates.py 14/16 (supporting, not in the 7 items):** FAIL "same-baseline ink collisions" = the same real P1 masthead overlap (counts once). FAIL "P7 quotes 2x + page tag + RU" = **TOOL ARTIFACT, not a content defect**: all 8 RU translations + page tags verified present in the print text layer; the check's exact-string match breaks because fix-xru run-splitting puts ". (Página N)" in a separate Newsreader run element (joined text has "Палмаресе . (Página 3)" with a space before the period). Only 'o agregado…' passes because its ". (Página 4)" rides inside one Latin run.

## Observations (not gate FAILs)
- **KIT stale:** WEEKLY-KIT.md §5 (L50) + fix-xru § (L178/180) still record worker C's SHAs/sizes (a96fd4c4…/12,583,263; f03415df…/1,202,236; 54,970 text bytes) and the HEAD TOO WIDE defect as "needs ruling, NOT fixed". Production now holds run2 values (see Identity). insert.py measures pins from disk, not the KIT, so this likely does not block insert mechanically — but KIT wave 2 must update §5 + add a run2 note.
- P2 HEAD TOO WIDE fix itself verified good: run2 log has no HEAD TOO WIDE flag; title in column (−34.9u); text layer changed by exactly "COM".

## OVERALL: NOT GATE-CLEAN — FAIL
Do NOT insert pt-ru as-is. Needs a fix round for the 4 real P1 defects (3 box-title overflows + 1 masthead collision), then rebuild + full re-gate. No source files were modified by this worker.
