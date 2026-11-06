# FIX-REPORT — W46 PT family, Round 1 proofreader defects (F-1–F-5)

- Issue: 2026-W46, Mon 2026-11-09 – Sun 2026-11-15. Target Portuguese (Brazilian). VOL.3, 150 exercises (A2 49 / B1 70 / B2 31), per-page 10/18/18/18/18/18/12/38, model essay 88 words.
- Verdict applied: `hidden_files/w46/pt-proofread-gates/proofreader-verdict-round1.md` (2026-11-02, ROUND 1 FAIL — 9 of 11 blocked; pt-ja and pt-zh-tw PASS as-is).
- Work dir: `hidden_files/w46/pt-fix/` — staged transforms in `stage/<lang>/`, rebuild logs in `logs/`, gate JSONs/logs in `gates/`, pre-fix snapshots (`pre-fix-artifact-hashes.txt`, `pre-fix-core-hashes.txt`, `pre-fix-transform-hashes.txt`, `pre-fix-textmd/`, `pre-fix-abstracts/`), `apply_fixes.py`, `rebuild_one.sh`, `derive_all.py` + `derive-args.json`.
- Rule honoured throughout: no rendered SVG/PDF hand-edited; every change went through source files + full re-render; `.text.md` regenerated from the source manuscript via `derive_textmd.py`, never hand-edited or extracted from PDF.
- Local only: `~/workspace/weekly-git` untouched, `index.json` untouched, nothing pushed/inserted, nothing posted to Discord, no edition content dumped into chat.
- A Round 2 independent proofread follows; this re-gating does not replace it.

## Design decision (F-1 source level)

F-1 was fixed at the **per-edition transform level, NOT in the core register**. The 10 note strings live in the core register (`bslib4.REG`, accumulated by single-process `run.py`), and ja/zh-cn/zh-tw legitimately render the same notes with fullwidth ： as CJK punctuation. Fixing the core strings to ASCII `:` and re-deriving would have changed the legitimate CJK usage. Each of the 8 Latin transforms therefore carries a §5c block of 10 exact `sub()` replacements (fullwidth → ASCII colon) applied after the REPL loop, before the §6 zero-CJK assert. The core build dir (`hidden_files/weekly-report-w46-pt-build/`) is byte-identical to before the fix (hash-verified).

## F-1 — P8 answer-note fullwidth colon (8 Latin editions: de/en/es/fr/it/ko/nl/ru)

Source: staged transform `hidden_files/w46/pt-fix/stage/<lang>/transform.py`, §5c block (per-edition source; core register untouched).

Before (identical in all 8, `svg/p8-avaliacao.svg`):

```
16. confere — conferir：ele → confere
17. abre — abrir：ele → abre
18. levamos — levar：nós → levamos
19. começa — começar：ela → começa
20. termina — terminar：ela → termina
56. mais — 2 > 0：mais
57. mais — 3 > 2：mais
58. mais — 17 < 18：mais cedo
102. confere — conferir：você → confere
103. termina — terminar：ela → termina
```

After (contrast item 101, which already used ASCII `:`: `101. confiro — conferir: eu → confiro`):

```
16. confere — conferir: ele → confere
17. abre — abrir: ele → abre
18. levamos — levar: nós → levamos
19. começa — começar: ela → começa
20. termina — terminar: ela → termina
56. mais — 2 > 0: mais
57. mais — 3 > 2: mais
58. mais — 17 < 18: mais cedo
102. confere — conferir: você → confere
103. termina — terminar: ela → termina
```

Verification: all 8 SVGs in each Latin edition contain 0 U+FF1A; the 10 notes match 10/10 with ASCII colon (HTML-unescaped text-node check). `.text.md` does not contain the P8 note strings (keys only), so F-1 cannot disturb it — confirmed: `.text.md` diffs show only F-2/F-5 lines.

## F-2 — P7 clinic trailing fullwidth full stop (7 editions: de/en/es/fr/it/nl/ru)

Mechanism: the REPL old string `假日落在周日，周一不补休` (without 。) is a prefix of the core clinic string `…不补休。`, so replacement left 。 behind. The same bare string is also the note of the P2 exercise and its P8 answer, where the translation correctly takes no trailing period; only the clinic (`content7.py`) carries 。. The fix therefore **ADDS** a second REPL entry (old string with 。, new = translation + `.`) and **keeps** the bare entry. The same add-not-replace design was applied to the timetable entry (SVG source without 。 vs `.text.md` line 36 with 。). Source: staged transforms, REPL table.

Before → after (P7 clinic gloss, ERROS COMUNS item 4):

| Ed. | Before (trailing 。) | After (trailing .) |
|---|---|---|
| de | `Der Feiertag fällt auf einen Sonntag, montags gibt es keinen Ausgleich。` | `Der Feiertag fällt auf einen Sonntag, montags gibt es keinen Ausgleich.` |
| en | `The holiday falls on a Sunday, with no Monday off。` | `The holiday falls on a Sunday, with no Monday off.` |
| es | `El festivo cae en domingo, el lunes no se recupera。` | `El festivo cae en domingo, el lunes no se recupera.` |
| fr | `Le jour férié tombe un dimanche, pas de récupération le lundi。` | `Le jour férié tombe un dimanche, pas de récupération le lundi.` |
| it | `La festa cade di domenica, il lunedì non si recupera。` | `La festa cade di domenica, il lunedì non si recupera.` |
| nl | `De feestdag valt op zondag, maandag geen inhaal。` | `De feestdag valt op zondag, maandag geen inhaal.` |
| ru | `Праздник выпадает на воскресенье, в понедельник выходного нет。` | `Праздник выпадает на воскресенье, в понедельник выходного нет.` |

Verification: 0 U+3002 in all 8 SVGs of each of the 7 editions; regenerated `.text.md` diff vs pre-fix is exactly lines 36 + 371 (。→ .) and nothing else; `.text.md` U+3002 count 2 → 0 in all 7.

## F-3 — pt-ko P7 orphan 。 node (ko only)

Before: `svg/p7-lingua.svg` nodes 107–108 — `공휴일이 일요일에 겹쳐도 월요일에 쉬지 않아요` followed by a standalone `。` text node on its own line, before the `A PALAVRA` header.

After: the orphan node is deleted; the sentence is a single text node ending with ASCII `.`:

```
공휴일이 일요일에 겹쳐도 월요일에 쉬지 않아요.
```

Source: staged ko transform — added dotted clinic REPL entry (same mechanism as F-2) + a §5d geometry block. After the text fix alone, the `.` wrapped onto its own line (measured overflow only 1.44 px: line 386.02 px vs 390 px max). The §5d block widens **only the clinic gloss** wrap/para from `CW - 44` to `CW - 40` (right margin 22 px → 18 px, still inside the box); simulation verified the other three glosses wrap identically at CW−40. Rebuilt ko P7: node 107 = the full sentence with `.`, node 108 = `A PALAVRA · 이번 주 단어`, 150 nodes total.

Verification: ko P7 U+3002 = 0; the kept P1 gloss `proclamação = 선포（공화국 선포）。` is untouched (P1 U+3002 = 1, legitimate); ko `.text.md` U+3002 3 → 2 (only line 371 changed; lines 36 and 44 keep 。); no other ko line disturbed; full-frame visual check of ko P7 passed (single-line clinic gloss, clear gap to the A PALAVRA box).

## F-4 — abstracts, pt-en + pt-zh-cn only (practice framing)

Other 9 abstracts untouched (verified passing, not modified).

pt-en `ABSTRACT.txt` — before:

```
A Lucerna Portuguese Weekly VOL.3: the November 15 second Enem day with natural sciences and mathematics, 90 questions, on the same Sunday as the Proclamation of the Republic holiday, 137 years on, plus the Copa do Brasil semifinal second legs deciding the finalists, the 11.11 sales season and Novembro Azul; Portuguese text with English explanations, A2 to B2, 150 exercises, for English speakers who want to learn Portuguese through real Brazilian news.
```

pt-en `ABSTRACT.txt` — after (tail replaced):

```
A Lucerna Portuguese Weekly VOL.3: the November 15 second Enem day with natural sciences and mathematics, 90 questions, on the same Sunday as the Proclamation of the Republic holiday, 137 years on, plus the Copa do Brasil semifinal second legs deciding the finalists, the 11.11 sales season and Novembro Azul; Portuguese text with English explanations, A2 to B2, 150 exercises on this week's topics, for English speakers learning Portuguese.
```

pt-zh-cn `ABSTRACT.txt` — before:

```
A Lucerna 葡萄牙语周报 VOL.3：11 月 15 日星期日 Enem 高考第二天（自然科学与数学，90 道题）与共和国宣言日假期同日，137 周年共和国宣言历史，巴西杯半决赛次回合决出决赛球队，11.11 促销季与十一月蓝色健康月；正文葡萄牙语、讲解简体中文，A2–B2 分级，150 道练习，适合学葡萄牙语的读者通过巴西新闻学葡萄牙语。
```

pt-zh-cn `ABSTRACT.txt` — after (tail replaced):

```
A Lucerna 葡萄牙语周报 VOL.3：11 月 15 日星期日 Enem 高考第二天（自然科学与数学，90 道题）与共和国宣言日假期同日，137 周年共和国宣言历史，巴西杯半决赛次回合决出决赛球队，11.11 促销季与十一月蓝色健康月；正文葡萄牙语、讲解简体中文，A2–B2 分级，以本周话题为素材的 150 道练习。
```

Both files verified: single logical line, no ASCII double-quote, no trailing newline (byte shape preserved: EN 456 → 441 bytes, ZH-CN 423 → 385 bytes), reader-native, masthead + levels + 150 present, practice framing. Pre-fix copies preserved in `pt-fix/pre-fix-abstracts/`.

## F-5 — pt-zh-cn `.text.md` header line 3 (zh-cn only)

Before (Portuguese, left over from the core manuscript):

```
Semana de 9 a 15 de novembro de 2026 · Textos em português · Explicações em chinês simplificado · Níveis A2–B2 · 150 exercícios
```

After (Simplified Chinese, via the export process — header argument to `derive_textmd.py`, mirroring the zh-tw pattern, using 级别 attested in the zh-cn edition itself):

```
2026 年 11 月 9–15 日 · 正文葡萄牙语 · 讲解简体中文 · 级别 A2–B2 · 150 道练习题
```

Verification: zh-cn `.text.md` diff vs pre-fix is exactly line 3 and nothing else; zh-cn SVGs byte-identical to pre-fix (hash-verified), so no content re-render was needed for this edition beyond the export + web PDF rebuild.

## Builder-level adjustments found during the fix (not verdict defects, documented)

1. **EN §5b stale assert (pre-existing reproducibility defect).** The preserved en `transform.py` §5b asserted the long editor-example label occurs twice, but the REPL entry already emits the short label, so the count is 0 and a fresh derivation could never pass. The staged en transform relaxes that assert to `in (0, 2)`; the replacement is a no-op and the §5b geometry edits still run. No content change. Recorded in the en KIT fix record.
2. **KO §5d geometry** — see F-3 above. Layout-only, clinic gloss only. Recorded in the ko KIT fix record.
3. **pt-core divergence note.** `files/weekly-report-w46-pt-core/` is the frozen reference / derive source, left untouched per scope. Its `ABSTRACT.txt` still carries the pre-fix news-framing tail and its `.text.md` line 3 is still Portuguese (the derive `header_old` anchor). The zh-cn edition dir is canonical; its KIT fix record notes that the old "byte-identical to core" claims no longer hold for those two files, by design.

## Re-render

All 9 affected editions rebuilt from a fresh copy of the core build dir + staged transform/gates via `rebuild_one.sh` (transform → run → render → gates; fails on any FLOW OVERFLOW / HEAD TOO WIDE or non-zero exit). Order: en, de, es, fr, it, ko, nl, ru, zh-cn. Every rebuild: `gates.py` FAILURES: none; registry TOTAL 150 (A2 49 / B1 70 / B2 31); pages 10/18/18/18/18/18/12/38; model essay 88 words. Logs: `pt-fix/logs/<lang>-{transform,run,render,gates}.log`.

Hash proof vs pre-fix snapshot: exactly 40 artifact files changed in the first check (8 Latin editions × print PDF + 2 cards + 2 SVGs — only P7/P8), zh-cn SVGs byte-identical, ja/zh-tw zero changes, core dir zero changes. Final check adds only the expected changes: 9 `.text.md` files, 2 `ABSTRACT.txt` files, 9 web PDFs.

EN byte-diff proof (pre-fix-equivalent SVGs reconstructed in scratch, since deleted): P1–P6 byte-identical; P7 exactly 1 text node changed; P8 exactly the 10 F-1 nodes changed.

## Re-gate results (final artifacts)

Gate JSONs/logs: `hidden_files/w46/pt-fix/gates/` (`freeze-pt-<lang>.json`, `p8-pt-<lang>.json`, `occlusion-pt-<lang>.json` + `.log` files). Runner: `pt-fix/gates_one.sh`.

| Ed. | freeze added CJK | p8 compare | occlusion |
|---|---|---|---|
| de | 0 | CLEAN 150/150, keydiff [137,138] | 0 flags, selftest OK |
| en | 0 | CLEAN 150/150, keydiff [137,138] | 0 flags, selftest OK |
| es | 0 | CLEAN 150/150, keydiff [137,138] | 0 flags, selftest OK |
| fr | 0 | CLEAN 150/150, keydiff [137,138] | 0 flags, selftest OK |
| it | 0 | CLEAN 150/150, keydiff [137,138] | 0 flags, selftest OK |
| ko | 3140 (legitimate Hangul) | CLEAN 150/150, keydiff [137,138] | 0 flags, selftest OK |
| nl | 0 | CLEAN 150/150, keydiff [137,138] | 0 flags, selftest OK |
| ru | 0 | CLEAN 150/150, keydiff [137,138] | 0 flags, selftest OK |
| zh-cn | 118 (footer/badge furniture only, +1/−1 strings per page) | CLEAN 150/150, keydiff [] | 0 flags, selftest OK |

keydiff [137,138] is adjudicated legitimate (translation items re-aimed at the reader's native language). Counts re-measured from the rebuild logs: 150 total, A2 49 / B1 70 / B2 31, per-page 10/18/18/18/18/18/12/38, 0 FLOW OVERFLOW / HEAD TOO WIDE in all 9 runs.

Visual check at full frame: P8 ×8 (de/en/es/fr/it/ko/nl/ru), P7 ×8 (7 F-2 editions + ko), abstracts ×2 (read in full, text-verified — abstracts have no rendered page). No overflow, overlap, tofu, footer intrusion, or orphan punctuation found; ko clinic line renders on one line with its period, clear of the A PALAVRA box.

## Final per-edition file inventory

Web PDFs built with `tools/webpdf.py <svg-dir> <out.pdf>` only; all ≤ 7 MB; `pdftotext` bytes > 0 on every web PDF.

| Ed. | `.text.md` bytes (480 lines) | Web PDF (bytes) | Web PDF `pdftotext` bytes | Print PDF (bytes) |
|---|---|---|---|---|
| de | 33,222 | 900,010 (`A-Lucerna-VOL3-DE-web.pdf`) | 45,311 | 3,532,428 |
| en | 33,031 | 891,340 (`A-Lucerna-VOL3-web.pdf`) | 44,314 | 3,489,843 |
| es | 33,214 | 887,246 (`Lucerna-VOL3-ES-web.pdf`) | 45,216 | 3,489,333 |
| fr | 33,286 | 886,398 (`A-Lucerna-VOL3-FR-web.pdf`) | 45,429 | 3,489,110 |
| it | 33,133 | 882,786 (`A-Lucerna-VOL3-IT-web.pdf`) | 44,940 | 3,465,332 |
| ja (untouched) | 33,284 | 1,497,357 (`A-Lucerna-VOL3-JA-web.pdf`) | 45,872 | 15,687,617 |
| ko | 33,281 | 1,172,271 (`Lucerna-VOL3-KO-web.pdf`) | 45,663 | 7,072,429 |
| nl | 33,126 | 895,921 (`A-Lucerna-VOL3-web.pdf`) | 44,993 | 3,527,841 |
| ru | 34,946 | 923,066 (`A-Lucerna-VOL3-web.pdf`) | 53,258 | 3,291,447 |
| zh-cn | 32,515 | 1,367,191 (`A-Lucerna-VOL3-web.pdf`) | 43,025 | 14,775,653 |
| zh-tw (untouched) | 32,515 | 1,614,344 (`A-Lucerna-VOL3-web.pdf`) | 43,019 | 14,818,306 |

## CJK punctuation confirmation (ja / zh-cn / zh-tw kept legitimate usage)

- ja: untouched (hash-verified). SVG totals FF1A = 54, U+3002 = 70 (P8 FF1A = 42); P8 10 notes 10/10 fullwidth ：; `.text.md` FF1A = 8, U+3002 = 49.
- zh-tw: untouched (hash-verified). SVG totals FF1A = 54, U+3002 = 48 (P8 FF1A = 42); P8 10 notes 10/10 fullwidth ：; `.text.md` FF1A = 9, U+3002 = 32.
- zh-cn: SVGs byte-identical to pre-fix (hash-verified). SVG totals FF1A = 54, U+3002 = 48 (P8 FF1A = 42); P8 10 notes 10/10 fullwidth ：; `.text.md` FF1A = 9, U+3002 = 32 (only line 3 changed, F-5). Abstract changed only as specified (F-4).
- All 8 Latin editions: 0 U+FF1A and 0 U+3002 in all SVGs; `.text.md` U+3002 = 0 (ko = 2, legitimate lines 36/44).

## KIT records

Fix records appended to the WEEKLY-KIT.md of all 9 touched editions (defect/fix quotes + re-gate evidence + final file numbers; en assert relaxation and ko §5d geometry noted in their KITs). No-change verification notes appended to the ja and zh-tw KITs (hash-verified unchanged, legitimate ：/。 inventories, not re-rendered, not re-gated). The pt-core KIT was not touched.

## Fixes NOT applied as specified

None. All five defects (F-1–F-5) were applied exactly as the verdict specified. The two builder-level adjustments (en §5b assert relaxation, ko §5d clinic-gloss widening) were necessary consequences of the specified fixes, are layout/assert-only, and are documented above and in the respective KITs. No-action observations O-1–O-4 were left alone, and register (você throughout) is unchanged.
