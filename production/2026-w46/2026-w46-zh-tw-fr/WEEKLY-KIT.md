# Lucerna Weekly — VOL.3 Traditional Chinese × French (W46)

## Edition identity

- **Pairing:** zh-tw × fr — Traditional Chinese text, explanations in French, for French-speaking readers.
- **Issue week:** Monday 2026-11-09 to Sunday 2026-11-15. **Slug:** 2026-w46-zh-tw-fr. **VOL.3.**
- **Core text frozen:** every Traditional Chinese article, exercise stem, option and box body is byte-identical to the W46 zh-tw core (freeze diff below). Only the explanation layer was rewritten natively in French.
- **Badge (P1, y=378, 21pt bold, OLIVE #3e4c2a, in-place in the core's own badge slot):** TEXTES EN CHINOIS TRADITIONNEL · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES
- **Footer:** Lucerna · HEBDOMADAIRE CHINOIS VOL.3 · TEXTE EN CHINOIS TRADITIONNEL · EXPLICATIONS EN FRANÇAIS / Page N sur 8.
- **Gloss prefix:** Note — (W45 family precedent). **P8 separator:** — Page N — (unchanged, per W45 precedent). **P8 key style:** dash (`N. key — note`), as the core. **Band titles:** Vie quotidienne / Culture / Sport / Jeunesse / Lecture approfondie / Focus langue / Test et réponses.
- **Readers'-corner disclosure (French, on P7, beside the unchanged Traditional Chinese disclosure):** "Lettre d'exemple de la rédaction — pas une vraie lettre. VOL.2 promettait de vraies lettres et les meilleurs textes de la page 8 dès ce numéro ; aucune n'était arrivée à la clôture. L'exemple reste, l'invitation aussi." No reader/letter/name/quote is invented anywhere.

## Measured totals (registry, identical to core)

**150 exercises** — A2 44 · B1 74 · B2 32; by page 10/18/18/18/18/18/12/38; by type 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1. Images: P2 1, P4 1 (same verified files/credits as the core — see the core KIT). P7 phrases: 8/8 at exactly 2 occurrences.

## Build

- Build dir: hidden_files/weekly-report-w46-zh-tw-fr-build/ (copy of the final W46 core build). Transform: hidden_files/w46-zh-tw-fr-transform.py — 252 whole-string literal pairs with occurrence assertions. Run via the single one-process driver run.py, then render.py, then tools/webpdf.py.
- French-length fixes applied in source (all mirrored in the transform record): four HEAD TOO WIDE heads shortened ("Compris ?", "Quiz de lecture" per the W45 FR precedent); P3 box title shortened ("Fin du festival") and P4 Over-to-you question shortened after BOXTITLE flags; three commas after CJK terms reworded (em dash / colon) after strict-CJK added 3 full-width commas; readers'-corner box bottom padding +14 pre-applied (DE lesson).
- **Gate 10 replay:** fresh core copy + transform → 8/8 SVGs byte-identical to the shipped edition.

## Gates (recorded in hidden_files/w46/zh-tw-gates.log)

- Builder self-check: TOTAL 150, zero warnings in the final build log.
- Occlusion audit: 0 flags, NEW vs core 0; same-baseline + chart-label scan 0/0.
- freeze.py diff --strict-cjk: added CJK 0 on all 8 pages.
- p8.py compare: CLEAN, 150/150 noted both.
- Residual-English scan: none. P7 phrases 8/8 at 2×.
- Web PDF: 2,073,408 bytes (< 7 MB); pdftotext 47,891 bytes, byte-identical to the print PDF's extracted text. Print PDF 15,630,960 bytes, SHA-256 570aaa3ef2ab3590a9f5df7325fbc606f35603459fc681aa31c86b841270a976; web SHA-256 c5719514bc60d82789c1412be44c61db293a492e0d38fd3242380a4b21042896.
- Visual QA: P7 card viewed clean; teaser clear of footer.
- Text export: 2026-w46-zh-tw-fr.text.md in this dir (from the edition's own SVG text layer, page order; never from a PDF). ABSTRACT.txt in this dir (French, single line, no ASCII double quotes).
- Delivery note: this builder does not claim finalization (independent proofread is separate), does not post to Discord, does not send cards/PDFs into the main chat, and does not insert into the repo.

## 补记 — Round 1 proofread fixes (2026-11-03, fix worker)

Fixes applied at the source (build `content*.py` / `ABSTRACT.txt`), full re-render of all 10 editions, full re-gate. No rendered SVG/PDF was hand-edited. A Round 2 independent proofread follows; re-gating does not replace it.

- **D4 (all 10, frozen core):** P6 "數字一覽 · By the numbers" box, `content56.py`: before `抽機票:23張、19天、19座城市` → after `抽機票:23張、19天、3座城市`. Only Los Angeles / Tokyo / Seoul are named anywhere in the issue (P1, P5 article, P5 timetable); "23張" and "19天" are supported and unchanged. Fixed in the core source first, then the identical one-line correction fanned out to all 9 fan-out sources. Final artifacts: "19座城市" = 0 in every SVG and text.md; "3座城市" = 1 in each.
- **D1 (this edition):** P5 practice-example glossline, `content56.py` line 30: before `Practice numbers: NT$450 + NT$1,550 = NT$2,000, exactly his budget.` → after `Chiffres d'entraînement : NT$450 + NT$1 550 = NT$2 000, exactement le budget.`. P2 practice glossline verified translated and untouched.
- **D2 (this edition):** P8 answer note 134, `content8.py`: before `Collecting points is 集點.` → after `Collecter des points, c'est 集點.` (house wording, matching neighbours 133/135).
- **D3 (this edition):** FR P4 note, `content34.py`: re-wrapped so no word splits mid-word. Before: `… a lieu les 21-22 nov. à Tianmu … La ville de Taipei double les points U-Sport …` → after: `… se tient les 21-22 nov. à Tianmu … Taipei double les points U-Sport …` (all facts preserved; the shared wrapper was not changed). Rendered P4 card verified: 11 lines, no split words ("Tianmu", "du", "ville" whole).
- **D5 (this edition):** P7 teaser box, `content7.py` geometry only (`py = fy + 66 + 4 * 138 + 18` → `+ 4`): whole teaser block shifted up 14px, no text ink touched. Teaser bottom now 2573.86 (footer rule 2580). Verified by SVG geometry and 1:1 pixel strips (last full-dark row 2572, 0 dark pixels at row 2580).
- **D6 (this edition):** `ABSTRACT.txt` closing reworded to practice framing (single line, no ASCII double quote, topics / A2–B2 / 150 exercises unchanged). Closing now ends: `150 exercices avec les sujets de la semaine comme matériau.`
- **Badge record corrected (record only, no artifact change):** this KIT previously claimed BRICK #a4553a; the rendered P1 badge fill is OLIVE #3e4c2a in all 10 editions (verified in every final P1 SVG), and the record now states the rendered truth.
- **Re-render (2026-11-03):** TOTAL 150; levels A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/12/38; zero FLOW OVERFLOW / HEAD TOO WIDE / WRAP WIDTH warnings. P7 teaser ends 2573.86.
- **Re-gate:** freeze diff rc=0, added CJK 0; p8.py compare CLEAN, 150/150 noted both, keydiff=[]. Occlusion audit: selftest OK (all 6 planted classes fired, clean controls silent), 0 flags, 0 NEW vs core. P7 phrases 8/8 at exactly 2 occurrences. Simplified-residue spot scan clean (core CJK set; Latin editions add 0 CJK).
- **Final files:** print PDF 15630984 bytes, SHA-256 e884c9e5e81ef25b16b2174511c4042d0373408072a77b1f236a7fbaa6b5d06d; web PDF 2073427 bytes (< 7 MB), SHA-256 93cd034644f28aaf25df7123237fc0b8c59eca269637cd445c1fe48e510098cd; pdftotext 47899 bytes on both PDFs, byte-identical print vs web; text.md 48653 bytes (exported from the edition's own SVG text layer, H1 preserved verbatim).
- **Gate evidence:** `hidden_files/w46/zh-tw-fix/gates/` (freeze/p8/occlusion JSONs + txt), render logs `hidden_files/w46/zh-tw-fix/render-*.log`, `webpdf-textmd.log`; full report `hidden_files/w46/zh-tw-fix/FIX-REPORT.md`.
