# Lucerna Weekly — VOL.3 Traditional Chinese × Dutch (W46)

## Edition identity

- **Pairing:** zh-tw × nl — Traditional Chinese text, explanations in Dutch, for Dutch-speaking readers.
- **Issue week:** Monday 2026-11-09 to Sunday 2026-11-15. **Slug:** 2026-w46-zh-tw-nl. **VOL.3.**
- **Core text frozen:** every Traditional Chinese article, exercise stem, option and box body is byte-identical to the W46 zh-tw core (see freeze diff below). Only the explanation layer (glosses, notes, box titles, band subtitles, P7 columns, P8 keys header) is in Dutch. This edition's explanation layer and build are the pre-existing NL builder's work, resumed by this recovery run; the only change made here is the pair-255 fix below plus the missing deliverables (text.md, web PDF, ABSTRACT.txt, this KIT).
- **Badge (P1, y=378, 21pt bold, OLIVE #3e4c2a, in-place in the core's own badge slot):** TEKSTEN IN HET CHINEES (TRADITIONEEL) · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS
- **Footer:** Lucerna · CHINEES WEEKBLAD VOL.3 · TEKSTEN IN HET CHINEES (TRADITIONEEL) · UITLEG IN HET NEDERLANDS / Pagina {n} van {total}.
- **Gloss prefix:** Uitleg — . **P8 separator:** — Pagina {pg} —. **P8 key style:** dash (`N. key — note`), as the core. **Band titles:** Leven / Cultuur / Sport / Jeugd / Verdieping / Taalfocus / Test & antwoorden.
- **Readers'-corner disclosure (Dutch, on P7, beside the unchanged Traditional Chinese disclosure):** Voorbeeldbrief van de redactie — geen echte brief. VOL.2 beloofde echte lezersbrieven en de beste pagina-8-teksten vanaf dit nummer; er was er geen publiceerbaar binnen voor de deadline. Het voorbeeld blijft, en de uitnodiging ook. No reader/letter/name/quote is invented anywhere.

## Measured totals (registry, identical to core)

**150 exercises** — A2 44 · B1 74 · B2 32; by page 10/18/18/18/18/18/12/38; by type 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1. Images: P2 1, P4 1 (same verified files/credits as the core — see the core KIT). P7 phrases: 8/8 at exactly 2 occurrences (article + P7, source-level count). P7 geometry: col3/teaser ends 2586.36 — see the adjudication note under Gates; this is the pre-existing NL builder's geometry, NOT introduced by this recovery run.

## Build

- Build dir: hidden_files/weekly-report-w46-zh-tw-nl-build/ (copy of the final W46 core build). Transform: hidden_files/w46-zh-tw-nl-transform.py — 255 whole-string literal pairs with occurrence assertions (repointing + furniture + explanations + one geometry pair: readers'-corner box bottom padding +14, formula +26 → +40). No content module was imported standalone; run via the single one-process driver run.py, then render.py, then tools/webpdf.py.
- The family-wide missed string (core content56.py Practice-numbers glossline, untranslated in all 6 finished editions — flagged to the coordinator, finished editions NOT touched) IS translated here as pair 255 (appended to the NL transform with a `# fix 1` comment): Oefengetallen: NT$ 450 + NT$ 1.550 = NT$ 2.000, precies het budget. Print PDF after the fix: 14,476,818 bytes (9 bytes smaller than the pre-fix render).
- **Gate 10 replay:** fresh core copy + transform → 8/8 SVGs byte-identical to the shipped edition (hashes compared before/after, print PDF size identical 14,476,818; replay dir removed; logs hidden_files/replay-nl-*.log).

## Gates (final renders)

- Builder self-check: TOTAL 150, zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the final build log (hidden_files/w46-zh-tw-nl-build-final.log).
- Occlusion audit: selftest OK; edition 0 flags; NEW vs core 0 (tools/scratch/w46-zhtw-nl-occlusion-final.json).
- Same-baseline + chart-label element scan: 0 / 0 (edition and core).
- freeze.py diff --strict-cjk: TOTAL added CJK characters 0 (tools/scratch/w46-zhtw-nl-freeze-final.json).
- p8.py compare: CLEAN, 150/150 noted both, no missing/extra/keydiff.
- Residual-language scan: no leftover English display strings except proper names/codes (Lucerna, VOL, NT$, ITF, SUPER STAGE/SAFE, momo, U-Sport, Shopee, TSNA, Arts in the Park, photo credits) and the `p. N` phrase-source refs kept as-is. `Practice numbers` English string: 0 occurrences.
- **P7 teaser adjudication (visual, 2026-11-03):** the measured teaser-box bottom (2586.36) sits 6px past the 2580 footer-rule line in SVG coordinates. The P7 card was viewed at full frame: the teaser box does NOT touch any footer ink, the footer rule and footer text are fully clear with visible ivory space between box and rule, and the pixel-based occlusion audit reports 0 flags. Adjudication: NO reader-visible defect; the geometry is the pre-existing NL builder's and is retained unchanged — re-deriving the NL P7 layout is out of scope for this recovery run.
- Web PDF: tools/webpdf.py, 1,990,340 bytes (< 7 MB); pdftotext 45,996 bytes, byte-identical to the print PDF's extracted text. Print PDF 14,476,818 bytes, SHA-256 b2b306dccba8a67c64e0019af2ed33609a75bf8e9b59300c1601201bb7fbbc16; web SHA-256 0c9db98a0ed3a09b63018143ab7869886c7cfe9cb669bd3a4ed1dc5f55e3c527.
- Visual QA: P1 and P7 cards viewed; badge/footer fit, no overflow (see teaser adjudication above).
- Text export: 2026-w46-zh-tw-nl.text.md in this dir (46,801 bytes; exporter hidden_files/w46/export_zhtw_textmd.py, validated byte-identical against the DE text.md convention; from the edition's own SVG text layer, page order; never from a PDF). ABSTRACT.txt in this dir (Dutch, single line, no ASCII double quotes).

## Proofread (proofread-until-zero)

- **Round 1 (2026-11-03, full):** all 255 pairs re-read against the English source (target-language spelling/grammar, explanation↔article correspondence, answers re-derived against the registry, numbering, dates/weekdays, facts vs core KIT sources, P7 quotes verbatim + translations matching the quoted Chinese, disclosure wording, red lines). This re-check covers the inherited NL explanation layer as rendered, plus the pair-255 fix. Result: ZERO issues. No fix, no re-render needed; this round stands as the zero-issue round.
- Delivery note: this builder does not claim finalization (independent proofread is separate), does not post to Discord, does not send cards/PDFs into the main chat, and does not insert into the repo.

## 补记 — Round 1 proofread fixes (2026-11-03, fix worker)

Fixes applied at the source (build `content*.py` / `ABSTRACT.txt`), full re-render of all 10 editions, full re-gate. No rendered SVG/PDF was hand-edited. A Round 2 independent proofread follows; re-gating does not replace it.

- **D4 (all 10, frozen core):** P6 "數字一覽 · By the numbers" box, `content56.py`: before `抽機票:23張、19天、19座城市` → after `抽機票:23張、19天、3座城市`. Only Los Angeles / Tokyo / Seoul are named anywhere in the issue (P1, P5 article, P5 timetable); "23張" and "19天" are supported and unchanged. Fixed in the core source first, then the identical one-line correction fanned out to all 9 fan-out sources. Final artifacts: "19座城市" = 0 in every SVG and text.md; "3座城市" = 1 in each.
- **D5 (this edition):** P7 teaser box, `content7.py` geometry only (`py = fy + 66 + 4 * 138 + 18` → `+ 4`): whole teaser block shifted up 14px, no text ink touched. Teaser bottom now 2572.36 (footer rule 2580). Verified by SVG geometry and 1:1 pixel strips (last full-dark row 2572, 0 dark pixels at row 2580).
- **D6 (this edition):** `ABSTRACT.txt` closing reworded to practice framing (single line, no ASCII double quote, topics / A2–B2 / 150 exercises unchanged). Closing now ends: `150 oefeningen met de thema's van deze week als materiaal.`
- **Badge:** OLIVE #3e4c2a confirmed as rendered in this edition's P1 SVG; no badge colour changed.
- **Re-render (2026-11-03):** TOTAL 150; levels A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/12/38; zero FLOW OVERFLOW / HEAD TOO WIDE / WRAP WIDTH warnings. P7 teaser ends 2572.36.
- **Re-gate:** freeze diff rc=0, added CJK 0; p8.py compare CLEAN, 150/150 noted both, keydiff=[]. Occlusion audit: selftest OK (all 6 planted classes fired, clean controls silent), 0 flags, 0 NEW vs core. P7 phrases 8/8 at exactly 2 occurrences. Simplified-residue spot scan clean (core CJK set; Latin editions add 0 CJK).
- **Final files:** print PDF 14476823 bytes, SHA-256 295271cb313dade0acc1a6b88318e0d52e886ba3f5b33e316673b59a376601ec; web PDF 1990345 bytes (< 7 MB), SHA-256 b2b5de57e11a3053d2c3d448c20b992f2b9bd37de46ffcf8e54e8fb3b0b8e066; pdftotext 45996 bytes on both PDFs, byte-identical print vs web; text.md 46800 bytes (exported from the edition's own SVG text layer, H1 preserved verbatim).
- **Gate evidence:** `hidden_files/w46/zh-tw-fix/gates/` (freeze/p8/occlusion JSONs + txt), render logs `hidden_files/w46/zh-tw-fix/render-*.log`, `webpdf-textmd.log`; full report `hidden_files/w46/zh-tw-fix/FIX-REPORT.md`.
