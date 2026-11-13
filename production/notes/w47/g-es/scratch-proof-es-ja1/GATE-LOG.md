# GATE-LOG — W47 es-ja, proof round 1 (independent)

Edition `production/2026-w47/2026-w47-es-ja/`, repo clone `~/workspace/weekly-git`.
Scratch: `hidden_files/w47/scratch-proof-es-ja1/` (`tmp/` + `logs/`; all runs `TMPDIR=<scratch>/tmp`).
Probe passed at start: `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`.
Read in full before gating: SOP.md §1.1 + §8, repo AGENTS.md, edition WEEKLY-KIT.md.
Tools in scratch: `creambox.py` (from `scratch-proof-de-es1`), `creambox_diag.py` (own strict variant), `boxtitle.py` (own, `core-es/svglib.py:text_w`). `keycheck.py`/`freeze_direct.py` (de-family, copied from `scratch-fanout-de`) NOT used. `sweep_de.py` used from `scratch-fanout-es/`.

## Identity (KIT §7 + disk, 2026-11-11)

| File | Bytes | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4-es-ja.pdf` | 17,294,297 | `de40fa29ee957b64…` (full match KIT) |
| `La-Lucerna-VOL4-es-ja-web.pdf` | 1,503,253 | `859b4421086697da…` (full match KIT) |
| `2026-w47-es-ja.text.md` | 46,018 | `e1486c4686b7a0d2…` (full match KIT; note filename is `2026-w47-es-ja.text.md`, not `text.md`) |

## Gates — all re-run, none taken from KIT

| # | Gate | Command / method | Result |
|---|---|---|---|
| 1 | Occlusion audit | `tools/occlusion_audit.py svg` (formal audit, no `--selftest`) | **0 flags**. Selftest OK (6 planted classes fired, clean controls silent). `logs/occlusion.log`, `occlusion.json` |
| 2 | p8 extract | `tools/p8.py extract` (or equivalent) | **150/150** keys extracted. `p8extract.json`, `logs/p8extract.log` |
| 3 | p8 compare | p8 answers vs `core-es` | **CLEAN**. `keydiff=[137, 138]` (expected re-aimed Japanese translation keys, KIT §6.12). `p8compare.json`, `logs/p8compare.log` |
| 4 | Freeze diff | `tools/freeze.py diff` | Added CJK 2,946 total (Japanese explanation layer, expected). All Latin-only added/removed strings are re-wrap artefacts or gloss swaps (`PSOE ` vs `PSOE`, `Después ___ (` → `Después ___` + `el sobre.`). P8 key stems match; notes swap zh→ja. **No Spanish content change.** `freeze-diff.json`, `logs/freeze-diff.log` |
| 5 | Freeze direct | copy edition to `scratch/rerun`, run `run.py` | rc=0, **0 FLOW OVERFLOW / HEAD TOO WIDE**, TOTAL 150, A2 50 / B1 72 / B2 28, by page 10/18/18/18/18/18/12/38, MODELO 97 words, P8-keys y=2521. Regenerated SVGs sha256 **8/8 MATCH** shipped. `logs/rerun.log` |
| 6 | Print vs web text layer | `pdftotext` both PDFs | Byte-identical, 47,054 B each; 8 pages; 1462.5×2025 pt. `print.txt`, `web.txt` |
| 7 | Bridge/orphan sweep | `sweep_de.py` | bridge orphans 0/20 bridges, box-vs-hline 0, bridge widows 0. `logs/sweep.log` |
| 8 | Cream boxes | `creambox.py` + strict `creambox_diag.py` | Crude script's negative clearances were false alarms (next-section headings inside its +45 slack). Strict diag: every cream box with text clears **+1.9 to +110.8** (tightest P3 `¿Y TÚ?` +1.9, P5 `¿Y TÚ?` +1.9; P7 col3: ERRORES +42.5, LA PALABRA +26.5, CARTAS +5.7). P1's two "empty" cream boxes are the image plate (x=88 y=1874 w=873 h=320) and a stroked frame (x=362 y=1999.2 w=255 h=142.8). **No `HERRAMIENTAS` toolbox exists in es P7** — P7 col3 clearances reported instead. `logs/creambox.log`, `logs/creambox-diag.log` |
| 9 | Box titles | `boxtitle.py` (text_w, sans bold, rendered size vs box-right − title-x) | **25/25 fit.** Tightest: P5 `EL PLAN DE LA SEMANA　今週の計画` 400.2/404.5 (+4.3); P1 `LA SEMANA EN CIFRAS　今週の数字` 388.6/404.5 (+15.9; KIT claimed 415.7/422.5 by a different method — still fits); P7 `ERRORES TÍPICOS　よくある間違い` 387.8/400.5 (+12.7). `logs/boxtitle.log` |
| 10 | P8 min font | PyMuPDF span scan | **10.125 pt** (748 spans) ≥ 9.75 floor. `logs/minfont-badges.log` |
| 11 | Paper / masthead / vols | SVG + PDF inspection | Paper `#fbfaf6` on all 8 pages. Masthead `La Lucerna` 196 units = 147 pt. **VOL.4 ×9** in SVG text (P1 ×2, others ×1); **VOL.5 ×3, all P7**. |
| 12 | Level chips | rx=2.7 rects per page | P1 10 (A2 8/B1 2), P2 15 (13/2), P3 18 (11/7), P4 15 B1, P5 18 B1, P6 18 B2, P7 12 (4/4/4), P8 35 (A2 11/B1 21/B2 3) — P8 matches KIT; total 141. P2 15 vs 18 exercises: matching set 25–28 shares one chip; P4 15 vs 18: 52–55 share one; P8 35 vs 38: the three matching sets (25–28, 52–55, 141–144) share one chip each (38 − 3 = 35). |
| 13 | Curly quotes | grep U+201C/U+201D/U+2019/U+2018 in all SVGs + text.md | **0 / 0 / 0 / 0.** Guillemets « » balanced 53/53 in text.md; per-page SVG counts equal. (P7 Newsreader italic exception: none present.) |
| 14 | Fonts | SVG font-family counts | Newsreader 1096, Noto Sans CJK SC 619, Noto Serif CJK SC 319 (CJK runs split out of serif paras + `→` arrows — renderer design, not a defect), UnifrakturMaguntia 1. Odd fills (`#EDD17F` etc.) inside the moth `<svg>` illustration, inherited from core. |
| 15 | Dates | `date -d` (Europe/Madrid) | 13 Nov Fri, 16 Mon, 17 Tue, 18 Wed, 19 Thu, 20 Fri, 21 Sat, 22 Sun, 24–28 Tue–Sat, 27 Fri, 28 Sat, 29 Sun, 10 Nov Tue, 9 Nov Mon — all consistent with the paper. |
| 16 | «12 de noviembre» | grep across svg/ + py + md + txt | Found only in WEEKLY-KIT.md (the rule statement itself). **Absent from all content.** |

## Visual pass

- Cards P1–P6, P7, P8 PNGs viewed in full. No overflow, no overlap, no clipped text observed.
- P1: urn illustration on cream plate; caption below; consejo box present (see PROOF-NOTE D1).
- P3: Sargent dancer image + caption «Bailaora española» (1880–81); image matches the *Spanish Dancer* (1880–1881, private collection) — verified via Google Arts & Culture / Dallas Museum of Fine Art.
- P5: Jebulon bronze urn photo, CC0 caption; EL PLAN DE LA SEMANA 5 items; word bank (see PROOF-NOTE D2).
- P6: RTVE free-minutes chart (PSOE 45 / PP 45 / Vox 30 / Frente Amplio 30 / Podemos 15; +3×10 = 195 total); numbers box (poll ban 5 / campaign 15 days / silence 1); debate timeline 13–29 Nov.
- P7: A2 LA HORA / B1 COMPARATIVOS / B2 EL SUBJUNTIVO grammar columns; Book of Hours initial; ERRORES TÍPICOS (4 items); LA PALABRA («el debate»); CARTAS DE LOS LECTORES (Marta sample letter + editor's note, 4-line Japanese); FRASES DE LA SEMANA (8 quotes, all verbatim from P1–P6); LA PRÓXIMA SEMANA (VOL.5).
- P8: sections A–H + RESPUESTAS (all 150 keys + Japanese notes). MODELO essay verified **97 words** by AST parse of `content8.py`.

## Key verification (150/150, stem-by-stem)

- Q1–Q10 (P1), Q11–Q28 (P2), Q29–Q46 (P3), Q47–Q64 (P4), Q65–Q82 (P5), Q83–Q100 (P6), Q101–Q112 (P7), Q113–Q150 (P8): each stem checked against its key from `p8extract.json` and against the article text. **No key error found.** Q39 = B (Nairobi), Q40 = A (duende) — no swap; the en-family Q39/Q40 swap does not occur here. Matching sets verified against definitions (25–28, 52–55, 97–100, 141–144).
- Two apparent key errors (Q79 «comprar», Q86 key B) were the proofreader's misreadings of the small P8 print; SVG text + extract confirm «comparar» and Q86 = A. Recorded in PROOF-NOTE as withdrawn candidates.

## External fact verification (online, 2026-11-11)

Verified: 29N election (RD 806/2026; 29 Nov 9:00–20:00; campaign 13–27 Nov; 38,728,356 voters); postal vote (6 Oct–19 Nov inclusive; docs from 9 Nov); La Liga J13 all 10 fixtures + J12 result/standings; UCL J5 + J4; MiDNI suspension lifted 5 Nov 2026; Flamenco Day 16 Nov 2010 Nairobi; laSexta debate Fri 13 Nov 21:30 (moved from Mon 9); SER housing debate Wed 18 Nov (Rodríguez–Bravo); other debates (hedged framing matches record as of 10 Nov); Bilbao Municipal Band Sun 22 Nov 12:00 Euskalduna; Santa Cecilia 22 Nov; poll ban LOREG art. 69.7 (5 days → 24–28 Nov); Black Friday Fri 27 Nov; Sargent *Spanish Dancer* (1880–81, private collection).
Limitation: RTVE free-minutes per-party table — verified against LOREG art. 64 baremo + 2023 results + BOE-A-2026-23258 existence; the JEC's per-party table itself was not directly retrieved. Every checkable element (scale, brackets, total 195) is consistent.

## Outcome

All mechanical gates **PASS**. Content proof found **4 defects** (PROOF-NOTE D1–D4, all core-attributed). Conclusion **(b)** — not ready for 定稿 until the core fixes land and are re-checked.
