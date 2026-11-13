# it-zh-tw — RECORD (build1, 2026-11-11)

## Gates — build1, `zh-tw/gates1.log`, GATES ALL PASS (first attempt)
- run.py rc 0, 150 exercises, zero FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE; flow ends P1-headline col 2/2 y=1223 (bottom 1828), P8-ex col 3/3 y=911 (bottom 1332), P8-keys col 3/3 y=2484 (bottom 2552, 68 px spare), P7 col3 1644.0
- occlusion 0 flags; p8 extract 150/150, compare CLEAN (keydiff [137,138,139]); freeze fragments 0 unexplained; freeze baseline direct sha256 8/8
- print/web text multiset identical (6,843 words each; chars equal); web < 7 MB; P8 min font 13.0 px = 9.75 pt
- §1.1 scans pass; VOL.5 = 3 legitimate nodes (same as core); textmd validate 0/0; keys match (except 137–139 + writing); notes match translations.py (table_gaps empty)
- P8 chip check: Q113–120, Q145–149, Q150 all B1, = core 1:1 — coordinates BYTE-IDENTICAL to the core, including Q150 (y=586), unlike ja/ko which flow 30 px lower
- No strict-CJK check for zh-tw (reader values are themselves CJK)

## Build history — 1 build (with a step-wise recovery after a SIGTERM)
- Pre-build measurements (probe svglib copied from core-zh-tw, `zh-tw/svglib_probe.py` — note: the probe needs `zh-tw/assets/lucerna-moth.svg` copied next to it because svglib resolves the moth asset relative to its own file): match_set instr "把詞和釋義配對" 136.5 px (budget 254.5) OK; P4 E TU 2 lines OK; P7 error notes all 1 line (Lazio 234.0, Torrone 248.1, andare 232.7, probabile 241.7); P7 disclosure 2 lines (718.1 px) OK; P7 gloss 2 lines OK; P1 cifre 2+2+3+3 = 11 lines (OVER the 8-line budget — the table's zh-tw values still carried the full Italian descriptive head); P1 bridge 2 lines (795.3 px); FRASI all 1L+1L (slots ~97 px vs 158); P8 estimate (fr→zh-tw mapping, SERIF 13 in 422.5 px) 2 two-liners (44, 134), total 4533.3 px vs 4576 capacity.
- 5 pre-build edits in translations.py (each count-asserted 1×): the 4 cifre lines rewritten whole-line into Traditional Chinese (Italian head dropped; numbers/facts unchanged) — 29 → "29 — 拉齊奧積分，11輪後居首（拉齊奧29分領跑）" (2 lines), 24 → "24 — 第11輪進球，10場比賽（11輪10場共24球）" (2 lines), 20.45 → "20.45 — 亞特蘭大對國米，週日（20:45）" (1 line), 150 → "150人以上 — 閉幕遊行演員（150名以上）" (1 line) — total 6 lines; P8 44/134 note → "主語 + 動詞" (PRE-EMPTIVE, ja/ko lesson). translations.py 149,162 → 148,989 bytes, still 239 entries.
- Build interruption (environmental, not a build defect): the `build_edition.py zh-tw` driver was SIGTERM'd by a service restart at ~284 s (exitSignal 15) — after run.py ALL DONE (150 exercises, P8-keys 2484/2552) and render.py had written the print PDF (27,779,760 bytes, 05:23) + 8 cards + 8 SVGs, during the webpdf step. The driver's tee'd stdout (`zh-tw/build1.out.log`) was empty — lost on the kill. Recovery per the nl lesson: verify what finished first (print PDF: 8 pages, 1462.5×2025 pt, pdftotext 102,884 bytes; no FLOW OVERFLOW in build1.log; P7 col3 1644.0), then run the remaining steps individually as backgrounded commands — webpdf.py alone (~298 s, WROTE 2,042,022 bytes, 44,142 text bytes) and the `.text.md` export alone via `zh-tw/export_textmd.py` (a verbatim copy of build_edition.py's export section; 52,568 bytes, 150 exercises, writing_type 寫作) — each verified (fresh mtimes + SHAs) before gates. Lesson (again): prefer backgrounded step-wise runs over one long foreground build when the runtime is busy; a killed build leaves valid SVGs + cards but may lack the web PDF / .text.md — always re-verify deliverable mtimes/SHAs after any interruption before running gates.
- Gates1: GATES ALL PASS on the first run. No rebuild needed.
- No tool fixes in this shift — the ja-shift fixes carried over (build_edition.py CJK-reader residual check, occlusion_audit.py transform stack, gates.py adjacent-pair rule). The zh-tw build exercised all three and passed first attempt.
- Re-aimed zh-tw keys (from build_edition.py tr() of the Chinese sources): 137 "聖母健康節人們走過還願橋。" / "對照原文"; 138 "週日晚上亞特蘭大對國米。" / "si gioca = 進行比賽"; 139 "週六，拉齊奧在主場對萊切。" / "in casa = 在主場"; 140 stem "每個數字都必須清楚。→ ___" / "dovere = 必須".
- P8 separators keep the Italian "— PAGINA {pg} —" by design (`P8_SEP["zh-tw"]` in build_edition.py, same as en/de/fr/es) — verified in the built content8.py:130, identical to the core.

## Visual — 8/8 cards viewed (build1), zero defects
- P1: masthead band starts x=185.8 (exactly the core's start), both margins clean; cifre box rewritten lines clean (29 → 2, 24 → 2, 20.45 → 1, 150 → 1); bridge 2 lines OK; footer "第1版／共8版".
- P2: "把詞和釋義配對" instr fits; E TU box reader question fits ("你走過還願橋或種過樹嗎？寫兩句義大利語寄給編輯部。"); Canaletto image; manovra disclosure visible.
- P3: E TU box clean ("更喜歡牛軋糖還是巧克力？寫兩句寄來。"); word box wraps after 'corteo ·' (same as core).
- P4: E TU box ends flush with the table header at 1140.45 = core ("週日晚上你看哪場比賽？寫兩句義大利語寄來。" 2 lines); match_set instr fits; results table clean. (Observation: the results title reads "第 11 輪賽果（6–8 novembre）" — the month name stays Italian; table value verbatim, see below.)
- P5: clean (structural mid-page whitespace is the core pattern); word list wraps after 'sede ·' (same as core, unlike ja/ko).
- P6: clean — practice bar chart + "練習用示例最低溫" box + Q83–100.
- P7: error notes 1 line each; disclosure 2 lines ends 1644.0, clear of the FRASI hline; LA PAROLA gloss 2 lines ("vetta = 榜首。本週見第 1 版與第 4 版：拉齊奧 29 分領跑。"); B2 bridge 3 lines, fits; Dante image; FRASI 8 quotes with translations.
- P8: Q113–120 B1 badges; 141–144 "把詞和釋義配對" fits, no graze; RISPOSTE 1–150 all present; Q44/134 now 1 line each ("主語 + 動詞"); Q137/138/139 wrap to 2 lines each (fit, flow ends 2484/2552); Q135 1 line ("A che ora gioca la Lazio? — 疑問詞組在句首"); Q149/Q150 separate lines; "150. ✓ 範文見本版 H 區（99 詞）".

## Self-read — full .text.md (1317 lines), all 150 keys re-verified
- Traditional Chinese explanation layer throughout; the only Simplified Chinese residue is the deliberate 「翻译」 type label on Q137–140 (W46 precedent, 4 occurrences) + the frozen verb-paradigm fullwidth colon ： in notes 16–20/60–61 (core pattern, no added CJK).
- Spot checks: Q22 A (1630 年誓願); Q29 B; Q32 A "Fate dolci" (curly quotes — the translations.py zh-tw value verbatim, same as nl/ko); Q44/134 note "主語 + 動詞"; Q45 note "地點在前，主語在後"; Q51 B (週日晚上); Q58 "più + bella 週日晚上最好看（主觀評價）"; Q59 meglio; Q66 B (11 月 23 日); Q81 Vero; Q82 Falso; Q85 B (13−11=2); Q86 A (6+7=13); Q87 "圖表數據是練習用的、不是真實預報"; Q92 B (+0.8%); Q120 B (11 月 24 日); Q135 note "疑問詞組在句首"; Q136 note "主語 + 動詞 + 地點"; Q137–140 re-aimed.
- Model text 99 words frozen. Disclosure 2-line version in P7 LETTERE (zh-tw): "這是編輯部示例，非真實來信。截稿時未收到真實來信與最佳作文，順延 VOL.5。"

## Quota stops on this shift: NONE. Core-it untouched.
