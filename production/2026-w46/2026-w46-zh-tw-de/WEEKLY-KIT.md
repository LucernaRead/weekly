# Lucerna Weekly — VOL.3 Traditional Chinese × German (W46)

## Edition identity

- **Pairing:** zh-tw × de — Traditional Chinese text, explanations in German, for German-speaking readers.
- **Issue week:** Monday 2026-11-09 to Sunday 2026-11-15. **Slug:** 2026-w46-zh-tw-de. **VOL.3.**
- **Core text frozen:** every Traditional Chinese article, exercise stem, option and box body is byte-identical to the W46 zh-tw core (see freeze diff below). Only the explanation layer (glosses, notes, box titles, band subtitles, P7 columns, P8 keys header) was rewritten natively in German.
- **Badge (P1, y=378, 21pt bold, OLIVE #3e4c2a, in-place in the core's own badge slot):** CHINESISCHER TEXT (TRADITIONELL) · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER
- **Footer:** Lucerna · CHINESISCHE WOCHENZEITUNG VOL.3 · TEXT AUF CHINESISCH (TRADITIONELL) · ERKLÄRUNGEN AUF DEUTSCH / Seite N von 8.
- **Gloss prefix:** Hinweis · (family code, as in W45). **P8 separator:** — Seite N —. **P8 key style:** dash (`N. key — note`), 12.8pt, as the core. **Band titles:** Leben / Kultur / Sport / Jugend / Vertiefung / Sprachfokus / Test & Lösungen.
- **Readers'-corner disclosure (German, on P7, beside the unchanged Traditional Chinese disclosure):** "Beispielbrief der Redaktion — kein echter Brief. VOL.2 versprach echte Leserbriefe und beste Seite-8-Texte ab dieser Ausgabe; keiner kam bis Redaktionsschluss an. Das Beispiel bleibt, die Einladung auch." No reader/letter/name/quote is invented anywhere.

## Measured totals (registry, identical to core)

**150 exercises** — A2 44 · B1 74 · B2 32; by page 10/18/18/18/18/18/12/38; by type 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1. Images: P2 1, P4 1 (same verified files/credits as the core — see the core KIT). P7 phrases: 8/8 at exactly 2 occurrences. P7 geometry: col3 ends 1732.84, teaser ends 2530.84 (footer rule 2580, clear).

## Build

- Build dir: hidden_files/weekly-report-w46-zh-tw-de-build/ (copy of the final W46 core build). Transform: hidden_files/w46-zh-tw-de-transform.py — 259 whole-string literal pairs with occurrence assertions (repointing + furniture + explanations + one geometry pair). No content module was imported standalone; run via the single one-process driver run.py, then render.py, then tools/webpdf.py.
- German-length fixes applied in source (all mirrored in the transform record, all re-verified by the audit): three column heads shortened after HEAD TOO WIDE warnings (Double-11-Wörter; Lokale Wörter; Leseverstehen); P3 box title shortened (Golden Horse); P7 error-clinic notes, sentence frame and readers'-corner disclosure condensed so col3 ends 1732.84 instead of 1893.36 (the first render pushed the VOL.4 teaser into the footer); readers'-corner box bottom padding +14 (formula +26 → +40) after a 11.3px BOXTITLE flag; memory-trick comma after 入圍 replaced by an em dash so _fw adds no full-width comma (strict-CJK).
- **Gate 10 replay:** fresh core copy + transform → 8/8 SVGs byte-identical to the shipped edition (hashes compared, stray replay dir removed).

## Gates (all recorded in hidden_files/w46/zh-tw-gates.log)

- Builder self-check: TOTAL 150, zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the final build log.
- Occlusion audit: selftest OK; edition 0 flags; NEW vs core 0 (tools/scratch/w46-zhtw-de-occlusion.json).
- Same-baseline + chart-label element scan: 0 / 0 (edition and core).
- freeze.py diff --strict-cjk: added CJK 0 on all 8 pages (exit 0).
- p8.py compare: CLEAN, 150/150 noted both, no missing/extra/keydiff.
- Residual-English scan: no leftover English except the proper name "Arts in the Park".
- Web PDF: tools/webpdf.py, 2,133,629 bytes (< 7 MB); pdftotext 46,884 bytes, byte-identical to the print PDF's extracted text. Print PDF 16,798,162 bytes, SHA-256 52a4c5ce0ef2e4091ef809e4adc164d4848c48af05b61a51608e05f110b3a928; web SHA-256 9644e03710ccb571e7ca64c0aae0633cd4f6b9b3ab420d5b195e343d4cf4f26c.
- Visual QA: P1 and P7 cards viewed; badge/footer fit, no overflow, teaser clear of footer.
- Text export: 2026-w46-zh-tw-de.text.md in this dir (from the edition's own SVG text layer, page order; never from a PDF). ABSTRACT.txt in this dir (German, single line, no ASCII double quotes).
- Delivery note: this builder does not claim finalization (independent proofread is separate), does not post to Discord, does not send cards/PDFs into the main chat, and does not insert into the repo.

## 补记 — Round 1 proofread fixes (2026-11-03, fix worker)

Fixes applied at the source (build `content*.py` / `ABSTRACT.txt`), full re-render of all 10 editions, full re-gate. No rendered SVG/PDF was hand-edited. A Round 2 independent proofread follows; re-gating does not replace it.

- **D4 (all 10, frozen core):** P6 "數字一覽 · By the numbers" box, `content56.py`: before `抽機票:23張、19天、19座城市` → after `抽機票:23張、19天、3座城市`. Only Los Angeles / Tokyo / Seoul are named anywhere in the issue (P1, P5 article, P5 timetable); "23張" and "19天" are supported and unchanged. Fixed in the core source first, then the identical one-line correction fanned out to all 9 fan-out sources. Final artifacts: "19座城市" = 0 in every SVG and text.md; "3座城市" = 1 in each.
- **D1 (this edition):** P5 practice-example glossline, `content56.py` line 30: before `Practice numbers: NT$450 + NT$1,550 = NT$2,000, exactly his budget.` → after `Übungszahlen: NT$450 + NT$1.550 = NT$2.000, genau das Budget.`. P2 practice glossline verified translated and untouched.
- **D2 (this edition):** P8 answer note 134, `content8.py`: before `Collecting points is 集點.` → after `Punkte sammeln heißt 集點.` (house wording, matching neighbours 133/135).
- **D6 (this edition):** `ABSTRACT.txt` closing reworded to practice framing (single line, no ASCII double quote, topics / A2–B2 / 150 exercises unchanged). Closing now ends: `150 Übungen mit den Themen der Woche als Material.`
- **Badge record corrected (record only, no artifact change):** this KIT previously claimed BRICK #a4553a; the rendered P1 badge fill is OLIVE #3e4c2a in all 10 editions (verified in every final P1 SVG), and the record now states the rendered truth.
- **Re-render (2026-11-03):** TOTAL 150; levels A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/12/38; zero FLOW OVERFLOW / HEAD TOO WIDE / WRAP WIDTH warnings. P7 teaser ends 2530.84.
- **Re-gate:** freeze diff rc=0, added CJK 0; p8.py compare CLEAN, 150/150 noted both, keydiff=[]. Occlusion audit: selftest OK (all 6 planted classes fired, clean controls silent), 0 flags, 0 NEW vs core. P7 phrases 8/8 at exactly 2 occurrences. Simplified-residue spot scan clean (core CJK set; Latin editions add 0 CJK).
- **Final files:** print PDF 16798216 bytes, SHA-256 7384659c67522cdf009621564c865cf75d7681cddc692f190572fa846e8ab0bf; web PDF 2133642 bytes (< 7 MB), SHA-256 e0c8ea5a73b349e87496d9a83d90cce9b3f5197943fff03e0b5c240259c6017a; pdftotext 46879 bytes on both PDFs, byte-identical print vs web; text.md 47681 bytes (exported from the edition's own SVG text layer, H1 preserved verbatim).
- **Gate evidence:** `hidden_files/w46/zh-tw-fix/gates/` (freeze/p8/occlusion JSONs + txt), render logs `hidden_files/w46/zh-tw-fix/render-*.log`, `webpdf-textmd.log`; full report `hidden_files/w46/zh-tw-fix/FIX-REPORT.md`.
