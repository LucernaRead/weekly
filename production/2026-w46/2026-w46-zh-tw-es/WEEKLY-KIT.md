# Lucerna Weekly — VOL.3 Traditional Chinese × Spanish (W46)

## Edition identity

- **Pairing:** zh-tw × es — Traditional Chinese text, explanations in Spanish, for Spanish-speaking readers.
- **Issue week:** Monday 2026-11-09 to Sunday 2026-11-15. **Slug:** 2026-w46-zh-tw-es. **VOL.3.**
- **Core text frozen:** every Traditional Chinese article, exercise stem, option and box body is byte-identical to the W46 zh-tw core (freeze diff below). Only the explanation layer was rewritten natively in Spanish.
- **Badge (P1, y=378, 21pt bold, OLIVE #3e4c2a, in-place in the core's own badge slot):** TEXTOS EN CHINO TRADICIONAL · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES
- **Footer:** Lucerna · SEMANARIO CHINO TRADICIONAL VOL.3 · TEXTO EN CHINO TRADICIONAL · EXPLICACIONES EN ESPAÑOL / Página N de 8.
- **Gloss prefix:** Nota — (W45 family precedent). **P8 separator:** — Página N —. **P8 key style:** PAREN (`N. key (note)`, writing `N. ✓ (note)`), per the W43/W45 zh-tw-es family's shipped build code (README #14) — the core's dash code is re-laid in this family, at core geometry. **Band titles:** Vida / Cultura / Deporte / Juventud / Lectura profunda / Enfoque lingüístico / Prueba y respuestas.
- **P8 _fw bypass (W45 precedent, replicated verbatim in content8.py):** key lines bypass svglib's `_fw` pair rule (which would full-width the parens whenever a note contains a Chinese term), restored after the keys flow — so match notes keep their Chinese terms inside half-width parens, exactly as the shipped W45 ES P8 does.
- **Readers'-corner disclosure (Spanish, on P7, beside the unchanged Traditional Chinese disclosure):** "Carta de ejemplo de la redacción, no una carta real. VOL.2 prometió cartas reales y los mejores textos de la página 8 desde este número; ninguna llegó publicable antes del cierre. El ejemplo se queda, y la invitación también." No reader/letter/name/quote is invented anywhere.

## Measured totals (registry, identical to core)

**150 exercises** — A2 44 · B1 74 · B2 32; by page 10/18/18/18/18/18/12/38; by type 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1. Images: P2 1, P4 1 (same verified files/credits as the core — see the core KIT). P7 phrases: 8/8 at exactly 2 occurrences.

## Build

- Build dir: hidden_files/weekly-report-w46-zh-tw-es-build/ (copy of the final W46 core build). Transform: hidden_files/w46-zh-tw-es-transform.py — 258 whole-string literal pairs with occurrence assertions (including the P8 paren code change, the _fw bypass block, and the letters-box padding pair). Run via the single one-process driver run.py, then render.py, then tools/webpdf.py.
- Spanish-length fixes applied in source (all mirrored in the transform record): P7-A2 head shortened ("Palabras del 11.11") after a HEAD TOO WIDE warning; readers'-corner box bottom padding +14 pre-applied (DE lesson); P7 clinic/frame/disclosure kept short from the start, so col3/teaser geometry stayed clear of the footer.
- **Gate 10 replay:** fresh core copy + transform → 8/8 SVGs byte-identical to the shipped edition.

## Gates (recorded in hidden_files/w46/zh-tw-gates.log)

- Builder self-check: TOTAL 150, zero warnings in the final build log.
- Occlusion audit: 0 flags, NEW vs core 0.
- freeze.py diff --strict-cjk: added CJK 0 on all 8 pages (first run showed 46 added full-width parens from the paren style without the bypass — fixed by replicating the W45 bypass, not by adjudication).
- p8.py compare: CLEAN, 150/150 noted both (paren style parses).
- Residual-English scan: none. P7 phrases 8/8 at 2×.
- Web PDF: 2,116,579 bytes (< 7 MB); pdftotext 47,134 bytes, byte-identical to the print PDF's extracted text. Print PDF 16,401,975 bytes, SHA-256 b6a259bc15c891b0831303486561a9bf3c0045e54305facc3f7a22216602bf5a; web SHA-256 ace7dab0eb072e0bc4c0591856643fa412600f6f69be2d0148dd29f2b89d511c.
- Visual QA: P8 card viewed — paren keys with half-width parens and Chinese terms inside, separators and footer correct.
- Text export: 2026-w46-zh-tw-es.text.md in this dir (from the edition's own SVG text layer, page order; never from a PDF). ABSTRACT.txt in this dir (Spanish, single line, no ASCII double quotes).
- Delivery note: this builder does not claim finalization (independent proofread is separate), does not post to Discord, does not send cards/PDFs into the main chat, and does not insert into the repo.

## 补记 — Round 1 proofread fixes (2026-11-03, fix worker)

Fixes applied at the source (build `content*.py` / `ABSTRACT.txt`), full re-render of all 10 editions, full re-gate. No rendered SVG/PDF was hand-edited. A Round 2 independent proofread follows; re-gating does not replace it.

- **D4 (all 10, frozen core):** P6 "數字一覽 · By the numbers" box, `content56.py`: before `抽機票:23張、19天、19座城市` → after `抽機票:23張、19天、3座城市`. Only Los Angeles / Tokyo / Seoul are named anywhere in the issue (P1, P5 article, P5 timetable); "23張" and "19天" are supported and unchanged. Fixed in the core source first, then the identical one-line correction fanned out to all 9 fan-out sources. Final artifacts: "19座城市" = 0 in every SVG and text.md; "3座城市" = 1 in each.
- **D1 (this edition):** P5 practice-example glossline, `content56.py` line 30: before `Practice numbers: NT$450 + NT$1,550 = NT$2,000, exactly his budget.` → after `Números de práctica: NT$450 + NT$1.550 = NT$2.000, exactamente el presupuesto.`. P2 practice glossline verified translated and untouched.
- **D5 (this edition):** P7 teaser box, `content7.py` geometry only (`py = fy + 66 + 4 * 138 + 18` → `+ 4`): whole teaser block shifted up 14px, no text ink touched. Teaser bottom now 2573.86 (footer rule 2580). Verified by SVG geometry and 1:1 pixel strips (last full-dark row 2572, 0 dark pixels at row 2580).
- **D6 (this edition):** `ABSTRACT.txt` closing reworded to practice framing (single line, no ASCII double quote, topics / A2–B2 / 150 exercises unchanged). Closing now ends: `150 ejercicios con los temas de esta semana como material.`
- **Badge record corrected (record only, no artifact change):** this KIT previously claimed BRICK #a4553a; the rendered P1 badge fill is OLIVE #3e4c2a in all 10 editions (verified in every final P1 SVG), and the record now states the rendered truth.
- **Re-render (2026-11-03):** TOTAL 150; levels A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/12/38; zero FLOW OVERFLOW / HEAD TOO WIDE / WRAP WIDTH warnings. P7 teaser ends 2573.86.
- **Re-gate:** freeze diff rc=0, added CJK 0; p8.py compare CLEAN, 150/150 noted both, keydiff=[]. Occlusion audit: selftest OK (all 6 planted classes fired, clean controls silent), 0 flags, 0 NEW vs core. P7 phrases 8/8 at exactly 2 occurrences. Simplified-residue spot scan clean (core CJK set; Latin editions add 0 CJK).
- **Final files:** print PDF 16402001 bytes, SHA-256 f2a9a6d3fe6d0fbe9ea45a71063b13d7d3bb7166e2c93ac485049feea4bfe808; web PDF 2116602 bytes (< 7 MB), SHA-256 d787f1670f40185dcbf563de7ddc5a4352048f740b52de2ed8faa96d8b24fd12; pdftotext 47147 bytes on both PDFs, byte-identical print vs web; text.md 47926 bytes (exported from the edition's own SVG text layer, H1 preserved verbatim).
- **Gate evidence:** `hidden_files/w46/zh-tw-fix/gates/` (freeze/p8/occlusion JSONs + txt), render logs `hidden_files/w46/zh-tw-fix/render-*.log`, `webpdf-textmd.log`; full report `hidden_files/w46/zh-tw-fix/FIX-REPORT.md`.
