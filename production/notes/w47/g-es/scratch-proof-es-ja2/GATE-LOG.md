# GATE-LOG — W47 es-ja, proof round 2 (independent, re-fanout rebuild)

Edition `production/2026-w47/2026-w47-es-ja/`, repo clone `~/workspace/weekly-git`.
Scratch: `hidden_files/w47/scratch-proof-es-ja2/` (`logs/` + `tmp/` + `png/` + `rerun/` + `freeze-es-ja2/`).
All runs `TMPDIR=<scratch>/tmp`, `PYTHONDONTWRITEBYTECODE=1`, interpreter `tools/venv/bin/python`.
Probe passed at start: `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `5bf82ddb…`;
goals-side scratch write verified (`probe-es-ja2.txt`).
Read before gating: repo `AGENTS.md`, `SOP.md` (via prior rounds; production-SOP canonical copy noted),
edition `WEEKLY-KIT.md` (§1–§8, incl. §8 rebuild record), proof1 `PROOF-NOTE.md`/`GATE-LOG.md`,
core-es3 re-proof `PROOF-NOTE.md` (core build 10, conclusion (a)), `scratch-refanout-es/classify-ja.txt`,
`scratch-fanout-es/es-ja.md` (builder build-3 record).
No production file was modified: shipped SVG sha256 verified identical before and after all gates
(`logs/svg-sha-before.txt`, `sha256sum -c` OK 8/8).

## Identity (task + disk, 2026-11-11)

| File | Bytes | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4-es-ja.pdf` | 17,294,448 | `459d570a294a14a3b170e7bf99ca4db3bc91560603dc21c43d371977e55da12f` (full match task) |
| `La-Lucerna-VOL4-es-ja-web.pdf` | 1,540,831 | `5895fce90fffd07cccf1909f8de1aa481572751e8caa9bc3a0d80be00845f71f` (full match task) |
| `2026-w47-es-ja.text.md` | 46,554 (1,820 lines) | `7479077861f46c27c4d69ae265d43bab40e14cdc2e09bec48d53772142b3e9ea` (full match task) |

Core-es build 10 re-verified on disk (unchanged): print 17,212,955 B
`2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`;
web 1,410,471 B `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`;
text.md 43,788 B / 1,822 lines `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`.

## Gates — all re-run, none taken from KIT or builder logs

| # | Gate | Command / method | Result |
|---|---|---|---|
| 1 | Identity + core SHA | `sha256sum` + `stat` on 3 files; same for core-es 3 files | **3/3 match task; core 3/3 match core-es3** |
| 2 | run.py | copy edition to `rerun/`, `run.py` there | **rc=0, 0 OVERFLOW / 0 TOO WIDE, TOTAL 150, A2 50 / B1 72 / B2 28, MODELO 97 words, P8-keys y=2521.** Regenerated SVGs sha256 **8/8 MATCH** shipped. `logs/rerun.log` |
| 3 | Occlusion audit | `tools/occlusion_audit.py svg --json occlusion.json` | **0 flags**. Selftest OK (6 planted classes fired, clean controls silent). `logs/occlusion.log`, `occlusion.json` |
| 4 | p8 extract | `tools/p8.py extract --p8 svg/p8-ejercicios.svg --total 150 --json p8extract.json` | **150/150** keys extracted. `p8extract.json`, `logs/p8extract.log` |
| 5 | p8 compare | `tools/p8.py compare --core-p8 core-es/svg/p8-ejercicios.svg --edition-p8 svg/p8-ejercicios.svg --total 150 --json p8compare.json` | **CLEAN**. `keydiff=[137, 138]` (re-aimed Japanese translation keys, adjudicated §5). `p8compare.json`, `logs/p8compare.log` |
| 6 | Freeze baseline | `tools/freeze.py baseline --build <ed> --core-svg <ed>/svg --out freeze-es-ja2` | **rc=0, baseline: 8/8 SVGs byte-identical**; core integrity: shipped SVGs unchanged. `logs/freeze.log` |
| 7 | Freeze diff | `tools/freeze.py diff --core-svg core-es/svg --edition-svg <ed>/svg --json freeze-diff.json` | **rc=0.** Added CJK **2,946** (p1 205 / p2 326 / p3 221 / p4 218 / p5 283 / p6 115 / p7 403 / p8 1,175). Latin-only added/removed strings classified: p2 `PSOE` vs `PSOE ` (trailing space); p5 Q72 stem re-split (`Después ___ (` → `Después ___` + `el sobre.` + `enviar`); p6 leading `·` re-wrap; p7 letter parens full-width → half-width (MERGE fix); p8 51/51 re-segmentations of the same key strings (gloss `=` moved to Japanese note runs). **No new Spanish content.** `freeze-diff.json`, `logs/freeze-diff.log` |
| 8 | Freeze diff --strict-cjk | same as 7 + `--strict-cjk` | **rc=1, EXPECTED for ja** (reader language differs from core zh-cn; the strict rule requires zero added CJK). Added CJK fully accounted (see gate 15); diff itself rc=0. `freeze-diff-strict.json`, `logs/freeze-diff-strict.log` |
| 9 | Print vs web text layer | `pdftotext -layout` both PDFs, `cmp` | **Byte-identical, 109,951 B each**; 8 pages; 1462.5×2025 pt. `print.txt`, `web.txt` |
| 10 | keycheck (REG vs print) | `keycheck_core.py <rerun-copy> p8extract.json` | **149/150 exact**; only #150 mismatch (REG `（自由な問題。模範文は下）` vs extracted `✓`, open-question convention, same as core). `keycheck-150.json`, `logs/keycheck.log` |
| 11 | Cream boxes | `creambox.py svg/*.svg` (crude) + `creambox_diag.py "svg/*.svg"` (strict, inside-only) | Crude negatives are the known below-box headings (+45 slack). Strict: every text-bearing cream box clears **+1.9 to +110.8** (tightest P3/P5 `¿Y TÚ?` +1.9, last lines all-CJK `送ろう。`; P7 col3: ERRORES +42.5, LA PALABRA +26.5, CARTAS +5.7; P1 C1 +8.0). P1's two "empty" boxes are the image plate (x=88 y=1874 w=873 h=320) and a stroked frame (x=362 y=1999 w=255 h=142.8). **No `HERRAMIENTAS` toolbox exists in es P7** — P7 col3 clearances reported instead. `logs/creambox.log`, `logs/creambox-diag.log` |
| 12 | Box titles | `boxtitle.py "svg/*.svg"` (proof1 method) + `boxtitle_core.py svg` (refanout method) | **25/25 fit, 0 overflow, both methods agree.** Tightest: P5 `EL PLAN DE LA SEMANA　今週の計画` 400.2/404.5 (+4.3); P1 `LA SEMANA EN CIFRAS　今週の数字` 388.6/404.5 (+15.9); P7 `ERRORES TÍPICOS　よくある間違い` 387.8/400.5 (+12.7). `logs/boxtitle.log`, `logs/boxtitle-core.log` |
| 13 | P8 min font | `minfont.py La-Lucerna-VOL4-es-ja.pdf` | **10.125 pt** (735 spans) ≥ 9.75 floor; 0 below 9.75. `logs/minfont.log` |
| 14 | Bridge/orphan sweep | `sweep_de.py <ed>` | **box-vs-hline 0; bridges found 20, bridge orphans 0; bridge widows 0.** `logs/sweep.log` |
| 15 | Freeze CJK accounting + SIMP_ONLY | `freeze-diff.json` `cjk_added_total` classified; all 289 unique rendered ideographs via opencc `s2t`/`t2s`; 16 s2t-changed chars vs joyo lists (Wikipedia + writejapanese.com) | Added 2,946 = hiragana 986 + katakana 644 + punct/symbol 215 + shared ideographs 1,084 + joyo-16 17; **UNACCOUNTED 0**. s2t-changed 16/16 joyo (`争会体党写参叙号国届数断来点画静`), all in grammatical Japanese; `学` 0 occurrences in the edition; residue chars `读话说语认学对发达过` all 0; t2s-changed 77 all correct Japanese words. `simp-candidates.json`, `trad-candidates.json` |
| 16 | 7 bridge fixes (re-verify) | grep new/old forms in `content*.py`; locate each bridge string as a single `<text>` line in its SVG | **7/7 new forms present at classify lines; 7/7 old forms 0 occurrences; 7/7 render as single complete `<text>` lines** (P2×1, P4×3, P5×2, P6×1). See PROOF-NOTE §2(a). |
| 17 | Exporter #82 | grep `282.` in text.md / print.txt / web.txt; `p8extract.json` key 82 | **`282.` 0 everywhere; key 82 = `Verdadero`; all keys 1–150 present, no number >150.** |
| 18 | D1–D4 re-check | grep + SVG text + visual | D1 consejo complete ✓; D3 `antes del jueves` 0 in text.md + all 8 SVGs ✓; D4 `el sábado veo el derbi` ✓; D2 bank unchanged per C3 adjudication ✓. |
| 19 | §1.1 / paper / vols / chips / quotes | SVG + PDF inspection, per-page counts | Paper `#fbfaf6` ×8. Masthead 196 units = 147 pt. **VOL.4 ×9; VOL.5 ×3, all P7.** Chips rx=2.7: P1 10 / P2 15 / P3 18 / P4 15 / P5 18 / P6 18 / P7 12 / P8 35 (A2 11 / B1 21 / B2 3); total 141. P2 15 vs 18 exercises: matching set 25–28 shares one chip; P4 15 vs 18: 52–55 share one; P8 35 vs 38: three matching sets share one each (38 − 3 = 35). Curly quotes 0 / rsquo 0 / straight quotes in text nodes 0. `12 de noviembre` 0 in text.md + all SVGs (only KIT rule statement). ABSTRACT.txt Japanese, one line, 447 B, no ASCII double quotes. Fonts (D5, record only): Newsreader 1109, Noto Sans CJK SC 619, Noto Serif CJK SC 319, UnifrakturMaguntia 1. |
| 20 | Gloss tokens (core §8.1) | per-page SVG substring counts | P1 reflexión 2; P2 mitin 2 / cartel 2 / escaño 2; P3 cante 5 / toque 6 / baile 9 / compás 4 / duende 5; P4 parón 2 / liderato 3; P5 papeleta 2 / censo 3 / plazo 3 — **all ≥2**. (KIT's P5 3/2/4 counted with P6 spillover; see PROOF-NOTE O2.) |
| 21 | Orphan direct scan | `<text>`-node regexes: lone `。` / line-initial `。` / lone `」` / lone `：` / lone `–/—` / lone `)` | **lone `。` 0; line-initial `。` 0; lone `」` 0.** 6 single-node punctuation hits, each adjudicated mid-line by same-baseline neighbours (p2 `）`, p5 `）`, p8 `：`, p8 `）`, p8 `— ` ×2) — see PROOF-NOTE §5. |
| 22 | FRASES verbatim | source-level exact match of 8 quotes vs P1–P6 article strings | **8/8 verbatim.** (The 4 `«…»` MISSes in the same scan are the ERRORES TÍPICOS examples, not quotes.) |
| 23 | Dates | `date -d` (Europe/Madrid) | 13 Nov Fri, 16 Mon, 17 Tue, 18 Wed, 19 Thu, 20 Fri, 21 Sat, 22 Sun, 24–28 Tue–Sat, 27 Fri, 28 Sat, 29 Sun, 10 Nov Tue, 9 Nov Mon — all consistent with the paper. |

## Visual pass (150 dpi renders of the print PDF, `png/p-1.png`–`p-8.png`)

- P1–P8 all viewed in full. No overflow, no overlap, no clipped text, no lone-punctuation line.
- P1: consejo sentence complete («…cómo leer un debate sin perderse.»); urn illustration + caption; CINCO CLAVES / EN ESTA EDICIÓN / LA PALABRA / BREVES all clear.
- P2: calendar, gloss, ¿SABÍAS QUE…?, ¿Y TÚ?, DECIR LA HORA, weekday table, exercises A–D; C bridge one line.
- P3: Sargent dancer + caption «Bailaora española» (1880–81); EL FLAMENCO EN TRES DATOS; ¿Y TÚ? above divider; exercises A–D.
- P4: J13 six-match table; LA CHAMPIONS VUELVE; ¿Y TÚ?; exercises A–D; A/C/D bridges one line each.
- P5: bronze urn photo + caption; EL PLAN (5 items); gloss; VOTAR box; ¿Y TÚ? above divider; bank `sobre · papeleta · censo · identidad · plazo · urna`; exercises A–D; A/C bridges one line; Q72 parenthetical one line.
- P6: EL CAMINO AL 29N timeline in order 13/16/18/19/23/23/24–28/26/27/28/29 with the **RTVE eight-party row present**; RTVE chart (45/45/30/30/15, footnote 195 + 3×10) and numbers box (5/15/1) with no clipped labels; LEER UN DEBATE box; exercises A–D; D bridge one line.
- P7: three grammar columns; Book of Hours image; ERRORES 4×1 line; LA PALABRA; CARTAS (Marta letter «el sábado veo el derbi», half-width parens, 4-line Japanese editor's note inside the box); FRASES 8 quotes with glosses + page refs; VOL.5 banner well above footer.
- P8: sections A–H + RESPUESTAS (all 150 keys + Japanese notes); MODELO essay (97 words, verified by count); swan/quill image; keys end y=2521, 39 px above footer; #150 `✓` form.

## Key verification (150/150, stem-by-stem)

- Q1–Q10 (P1), Q11–Q28 (P2), Q29–Q46 (P3), Q47–Q64 (P4), Q65–Q82 (P5), Q83–Q100 (P6), Q101–Q112 (P7), Q113–Q150 (P8): each stem checked against its key from `p8extract.json` and against the article text (`stems-150.txt` — 138 `f.ex()` calls + 3 `match_set`s = 150 items). **No key error found.** Q39 = B (Nairobi), Q40 = A (duende) — no swap; matching sets verified against definitions (25–28, 52–55, 141–144) with letter order confirmed in `bslib4.match_set` (a=rights[0] … d=rights[3]).
- MODELO essay counted: **97 words** exactly, as claimed (independent count + run.py + P8 note agree).
- P8 chip count 35 vs 38 exercises: Q25–28 share one chip, Q52–55 share one, Q141–144 share one (38 − 3 = 35). ✓
- #150 open-question exception: REG descriptive key vs printed `✓` — same convention as core, not a defect.

## Full read

`2026-w47-es-ja.text.md` lines 1–1820 read end-to-end (all 8 pages: articles, exercises, P8 answers);
P1–P8 print renders viewed. No new factual/language defect found.
External facts were NOT re-verified live this round: they were independently verified online by proof1
(2026-11-11) and re-verified by core-es3 re-proof (conclusion (a)), and the rebuild changed none of them
(`classify-ja.txt`: no factual changes outside the adjudicated core items).

## Outcome

All mechanical gates **PASS**. Content proof found **0 defects**.
Conclusion **(a)** — ready for 定稿.
Observations O1–O4 (PROOF-NOTE §9) are non-blocking notes, not defects.
