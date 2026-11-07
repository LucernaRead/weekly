# Lucerna Weekly — VOL.3 Traditional Chinese × Italian (W46)

## Edition identity

- **Pairing:** zh-tw × it — Traditional Chinese text, explanations in Italian, for Italian-speaking readers.
- **Issue week:** Monday 2026-11-09 to Sunday 2026-11-15. **Slug:** 2026-w46-zh-tw-it. **VOL.3.**
- **Core text frozen:** every Traditional Chinese article, exercise stem, option and box body is byte-identical to the W46 zh-tw core (see freeze diff below). Only the explanation layer (glosses, notes, box titles, band subtitles, P7 columns, P8 keys header) was rewritten natively in Italian.
- **Badge (P1, y=378, 21pt bold, OLIVE #3e4c2a, in-place in the core's own badge slot):** TESTI IN CINESE TRADIZIONALE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI
- **Footer:** Lucerna · SETTIMANALE CINESE TRADIZIONALE VOL.3 · TESTI IN CINESE TRADIZIONALE · SPIEGAZIONI IN ITALIANO / Pagina N di 8.
- **Gloss prefix:** Nota — (family code, as in W45). **P8 separator:** — Pagina N —. **P8 key style:** paren (`N. key (note)`), per the W43/W45 zh-tw-it family's shipped code, at core geometry. **Band titles:** Vita / Cultura / Sport / Gioventù / Lettura approfondita / Focus lingua / Test e risposte.
- **CJK-paren discipline (W43/W45 IT precedent, followed exactly):** every Chinese word cited inside an Italian registry note is written in tone-marked pinyin only — the edition's registry notes contain zero Han characters, the printed P8 has no full-width parentheses and no Han characters inside parentheses. Chinese stays as Chinese in P7 prose/gloss bodies and in match lefts/rights (target text, not P8 notes). No `_fw` bypass was used: the pinyin-only notes never trigger the pair conversion. The P8-key form of the B2 ex notes (e.g. 集點/感謝祭) is the same pinyin string as the P7 form, since both are registry notes.
- **Readers'-corner disclosure (Italian, on P7, beside the unchanged Traditional Chinese disclosure):** "Lettera di esempio della redazione, non una lettera vera. VOL.2 prometteva lettere vere e i migliori testi di pagina 8 da questo numero; nessuna pubblicabile era arrivata alla chiusura. L'esempio resta, e resta anche l'invito." No reader/letter/name/quote is invented anywhere.

## Measured totals (registry, identical to core)

**150 exercises** — A2 44 · B1 74 · B2 32; by page 10/18/18/18/18/18/12/38; by type 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1. Images: P2 1, P4 1 (same verified files/credits as the core — see the core KIT). P7 phrases: 8/8 at exactly 2 occurrences (text-node join). P7 geometry: col3/teaser clear of the footer (teaser at core clearance; clinic/frame/disclosure condensed as in the DE lesson).

## Build

- Build dir: hidden_files/weekly-report-w46-zh-tw-it-build/ (copy of the final W46 core build). Transform: hidden_files/w46-zh-tw-it-transform.py — 256 whole-string literal pairs with occurrence assertions (repointing + furniture + explanations + paren code-change + one geometry pair). No content module was imported standalone; run via the single one-process driver run.py, then render.py, then tools/webpdf.py.
- Italian-length fixes applied in source (all mirrored in the transform record, all re-verified by the audit): P7-A2 head shortened ("Parole del 11.11") after a HEAD TOO WIDE warning; two P5 rail box titles shortened after 2 BOXTITLE flags ("Scheda carnevale", "Estrazione"); two B2 ex notes converted to pinyin-first forms after freeze showed 4 added full-width parens (Jídiǎn, Gǎnxièjì — registry notes, not prose); readers'-corner box bottom padding +14 pre-applied (DE lesson, formula +26 → +40).
- **Gate 10 replay:** fresh core copy + transform → 8/8 SVGs byte-identical to the shipped edition (hashes compared, stray replay dir removed).

## Gates (all recorded in hidden_files/w46/zh-tw-gates.log)

- Builder self-check: TOTAL 150, zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the final build log.
- Occlusion audit: selftest OK; edition 0 flags; NEW vs core 0 (tools/scratch/w46-zhtw-it-occlusion.json).
- Same-baseline + chart-label element scan: 0 / 0 (edition and core).
- freeze.py diff --strict-cjk: added CJK 0 on all 8 pages (exit 0).
- p8.py compare: CLEAN, 150/150 noted both, no missing/extra/keydiff.
- Residual-English scan: no leftover English except proper names (Arts in the Park, ITF, EVA Air, place names).
- Web PDF: tools/webpdf.py, 1,982,304 bytes (< 7 MB); pdftotext 46,538 bytes, byte-identical to the print PDF's extracted text. Print PDF 14,083,166 bytes, SHA-256 44982ffb5c64be703373bd4870521092a23eea04ccc32e788f703a95a128ef03; web SHA-256 98b350a543a419faaaa073aa53cb956b0ca0af0bed66faeb63161126995229fc.
- Visual QA: P1, P7 and P8 cards viewed; badge/footer fit, paren keys with half-width parens and pinyin notes, no overflow, teaser clear of footer.
- Text export: 2026-w46-zh-tw-it.text.md in this dir (from the edition's own SVG text layer, page order; never from a PDF). ABSTRACT.txt in this dir (Italian, single line, no ASCII double quotes).
- Delivery note: this builder does not claim finalization (independent proofread is separate), does not post to Discord, does not send cards/PDFs into the main chat, and does not insert into the repo.

## 补记 — Round 1 proofread fixes (2026-11-03, fix worker)

Fixes applied at the source (build `content*.py` / `ABSTRACT.txt`), full re-render of all 10 editions, full re-gate. No rendered SVG/PDF was hand-edited. A Round 2 independent proofread follows; re-gating does not replace it.

- **D4 (all 10, frozen core):** P6 "數字一覽 · By the numbers" box, `content56.py`: before `抽機票:23張、19天、19座城市` → after `抽機票:23張、19天、3座城市`. Only Los Angeles / Tokyo / Seoul are named anywhere in the issue (P1, P5 article, P5 timetable); "23張" and "19天" are supported and unchanged. Fixed in the core source first, then the identical one-line correction fanned out to all 9 fan-out sources. Final artifacts: "19座城市" = 0 in every SVG and text.md; "3座城市" = 1 in each.
- **D1 (this edition):** P5 practice-example glossline, `content56.py` line 30: before `Practice numbers: NT$450 + NT$1,550 = NT$2,000, exactly his budget.` → after `Numeri di pratica: NT$450 + NT$1.550 = NT$2.000, esattamente il budget.`. P2 practice glossline verified translated and untouched.
- **D6:** not applicable — this edition's abstract was already practice-framed (CLEAN); `ABSTRACT.txt` untouched.
- **Badge record corrected (record only, no artifact change):** this KIT previously claimed BRICK #a4553a; the rendered P1 badge fill is OLIVE #3e4c2a in all 10 editions (verified in every final P1 SVG), and the record now states the rendered truth.
- **Re-render (2026-11-03):** TOTAL 150; levels A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/12/38; zero FLOW OVERFLOW / HEAD TOO WIDE / WRAP WIDTH warnings. P7 teaser ends 2557.36.
- **Re-gate:** freeze diff rc=0, added CJK 0; p8.py compare CLEAN, 150/150 noted both, keydiff=[]. Occlusion audit: selftest OK (all 6 planted classes fired, clean controls silent), 0 flags, 0 NEW vs core. P7 phrases 8/8 at exactly 2 occurrences. Simplified-residue spot scan clean (core CJK set; Latin editions add 0 CJK).
- **Final files:** print PDF 14083148 bytes, SHA-256 e3c4edbe526aa0d78cb3ce0af18b5bfb1ce614adb09add51c278e8ced74db0b9; web PDF 1982279 bytes (< 7 MB), SHA-256 ceb15c347595475ee9ee93104480a1502b15dbc4c2e414a4acfa6839375e8941; pdftotext 46541 bytes on both PDFs, byte-identical print vs web; text.md 47324 bytes (exported from the edition's own SVG text layer, H1 preserved verbatim).
- **Gate evidence:** `hidden_files/w46/zh-tw-fix/gates/` (freeze/p8/occlusion JSONs + txt), render logs `hidden_files/w46/zh-tw-fix/render-*.log`, `webpdf-textmd.log`; full report `hidden_files/w46/zh-tw-fix/FIX-REPORT.md`.
