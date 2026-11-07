# Lucerna Weekly — VOL.3 Traditional Chinese × Portuguese (W46)

## Edition identity

- **Pairing:** zh-tw × pt — Traditional Chinese text, explanations in Portuguese, for Portuguese-speaking readers.
- **Issue week:** Monday 2026-11-09 to Sunday 2026-11-15. **Slug:** 2026-w46-zh-tw-pt. **VOL.3.**
- **Core text frozen:** every Traditional Chinese article, exercise stem, option and box body is byte-identical to the W46 zh-tw core (see freeze diff below). Only the explanation layer (glosses, notes, box titles, band subtitles, P7 columns, P8 keys header) was rewritten natively in Portuguese (Brazilian conventions per the W43/W45 PT precedent: thousands separator `.`, currency `NT$` with a space, ordinals `1.º`/`34.ª`, Duplo 11, Taipé).
- **Badge (P1, y=378, 21pt bold, OLIVE #3e4c2a, in-place in the core's own badge slot):** TEXTOS EM CHINÊS TRADICIONAL · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA
- **Footer:** Lucerna · SEMANÁRIO CHINÊS TRADICIONAL VOL.3 · TEXTOS EM CHINÊS TRADICIONAL · EXPLICAÇÕES EM PORTUGUÊS / Página N de 8.
- **Gloss prefix:** Nota — (family code, as in W45). **P8 separator:** — Página N —. **P8 key style:** paren (`N. key (note)`), per the W43/W45 zh-tw-pt family's shipped build code, at core geometry, with the `_fw` bypass RETAINED verbatim (key lines matching `^\d+\. ` bypass svglib `_fw` pair conversion, restored after the keys flow). **Band titles:** Vida / Cultura / Esporte / Juventude / Leitura a fundo / Foco linguístico / Teste e respostas.
- **Pinyin discipline (W43/W45 PT precedent, followed exactly):** every Chinese word cited inside a Portuguese registry note is written in tone-marked pinyin only — the edition's registry notes contain zero Han characters. Chinese stays as Chinese in P7 prose/gloss bodies and in match lefts/rights (target text, not P8 notes).
- **Readers'-corner disclosure (Portuguese, on P7, beside the unchanged Traditional Chinese disclosure):** "Carta de exemplo da redação, não uma carta real. VOL.2 prometia cartas reais e os melhores textos da página 8 a partir desta edição; nenhuma publicável havia chegado até o fechamento. O exemplo fica, e o convite também." No reader/letter/name/quote is invented anywhere.

## Measured totals (registry, identical to core)

**150 exercises** — A2 44 · B1 74 · B2 32; by page 10/18/18/18/18/18/12/38; by type 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1. Images: P2 1, P4 1 (same verified files/credits as the core — see the core KIT). P7 phrases: 8/8 at exactly 2 occurrences (text-node join). P7 geometry: col3/teaser clear of the footer (clinic/frame/disclosure condensed as in the DE lesson).

## Build

- Build dir: hidden_files/weekly-report-w46-zh-tw-pt-build/ (copy of the final W46 core build). Transform: hidden_files/w46-zh-tw-pt-transform.py — 258 whole-string literal pairs with occurrence assertions (repointing + furniture + explanations + paren code-change + `_fw` bypass insertion + one geometry pair). No content module was imported standalone; run via the single one-process driver run.py, then render.py, then tools/webpdf.py.
- Build incident (recorded honestly): the first transform run silently did nothing — the transform file was missing its `main()` block (exit 0, empty log). The untransformed core copy then rendered into the CORE edition dir. The core SVGs/PDFs were re-verified byte-identical against the recorded baseline hashes (8/8 SVG hashes, both PDF SHAs unchanged) — no harm done. The transform was fixed, the build dir re-copied fresh, and the build re-run properly into the PT dir.
- Portuguese-length fixes applied in source (all mirrored in the transform record, all re-verified by the audit): two P7 heads shortened after HEAD TOO WIDE warnings ("Palavras do 11.11", "Falares locais"); P4 Over-to-you question shortened after a 4.4px BOXTITLE flag; P5 ticket-draw box title shortened ("Sorteio") after a 33.8px BOXTITLE flag; readers'-corner box bottom padding +14 pre-applied (DE lesson, formula +26 → +40).
- **Gate 10 replay:** fresh core copy + transform (OUT pairs skipped, paths pre-repointed by sed) → 8/8 SVGs byte-identical to the shipped edition (hashes compared, stray replay dir removed).

## Gates (all recorded in hidden_files/w46/zh-tw-gates.log)

- Builder self-check: TOTAL 150, zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the final build log.
- Occlusion audit: selftest OK; edition 0 flags; NEW vs core 0 (tools/scratch/w46-zhtw-pt-occlusion.json).
- Same-baseline + chart-label element scan: 0 / 0 (edition and core).
- freeze.py diff --strict-cjk: added CJK 0 on all 8 pages (exit 0).
- p8.py compare: CLEAN, 150/150 noted both, no missing/extra/keydiff.
- Residual-English scan: no leftover English except proper names (Arts in the Park, ITF, EVA Air, place names).
- Web PDF: tools/webpdf.py, 2,075,620 bytes (< 7 MB); pdftotext 46,512 bytes, byte-identical to the print PDF's extracted text. Print PDF 15,632,970 bytes, SHA-256 937c4d50b0d62cad98a39ff0c463ed7e8b4380062997c901c29a280ab33ddf69; web SHA-256 ba9b0380c6ea27a95d19fab54e52c6beb06a4092fd0472a66ef57747204cf9f4.
- Visual QA: P1 and P8 cards viewed; badge/footer fit, paren keys with half-width parens and pinyin notes, no overflow.
- Text export: 2026-w46-zh-tw-pt.text.md in this dir (from the edition's own SVG text layer, page order; never from a PDF). ABSTRACT.txt in this dir (Portuguese, single line, no ASCII double quotes).
- Delivery note: this builder does not claim finalization (independent proofread is separate), does not post to Discord, does not send cards/PDFs into the main chat, and does not insert into the repo.

## 补记 — Round 1 proofread fixes (2026-11-03, fix worker)

Fixes applied at the source (build `content*.py` / `ABSTRACT.txt`), full re-render of all 10 editions, full re-gate. No rendered SVG/PDF was hand-edited. A Round 2 independent proofread follows; re-gating does not replace it.

- **D4 (all 10, frozen core):** P6 "數字一覽 · By the numbers" box, `content56.py`: before `抽機票:23張、19天、19座城市` → after `抽機票:23張、19天、3座城市`. Only Los Angeles / Tokyo / Seoul are named anywhere in the issue (P1, P5 article, P5 timetable); "23張" and "19天" are supported and unchanged. Fixed in the core source first, then the identical one-line correction fanned out to all 9 fan-out sources. Final artifacts: "19座城市" = 0 in every SVG and text.md; "3座城市" = 1 in each.
- **D1 (this edition):** P5 practice-example glossline, `content56.py` line 30: before `Practice numbers: NT$450 + NT$1,550 = NT$2,000, exactly his budget.` → after `Números de práctica: NT$ 450 + NT$ 1.550 = NT$ 2.000, exatamente o orçamento.`. P2 practice glossline verified translated and untouched.
- **D6:** not applicable — this edition's abstract was already practice-framed (CLEAN); `ABSTRACT.txt` untouched.
- **Badge record corrected (record only, no artifact change):** this KIT previously claimed BRICK #a4553a; the rendered P1 badge fill is OLIVE #3e4c2a in all 10 editions (verified in every final P1 SVG), and the record now states the rendered truth.
- **Re-render (2026-11-03):** TOTAL 150; levels A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/12/38; zero FLOW OVERFLOW / HEAD TOO WIDE / WRAP WIDTH warnings. P7 teaser ends 2557.36.
- **Re-gate:** freeze diff rc=0, added CJK 0; p8.py compare CLEAN, 150/150 noted both, keydiff=[]. Occlusion audit: selftest OK (all 6 planted classes fired, clean controls silent), 0 flags, 0 NEW vs core. P7 phrases 8/8 at exactly 2 occurrences. Simplified-residue spot scan clean (core CJK set; Latin editions add 0 CJK).
- **Final files:** print PDF 15632996 bytes, SHA-256 ad62003b7e54ed1bf9c65d6dec939beaa87f2e45d7e551a000e9a45430faeb8a; web PDF 2075639 bytes (< 7 MB), SHA-256 776c892766c7a80601d8df0c921921054842694ec9e63812e121c4de9001bf82; pdftotext 46523 bytes on both PDFs, byte-identical print vs web; text.md 47298 bytes (exported from the edition's own SVG text layer, H1 preserved verbatim).
- **Gate evidence:** `hidden_files/w46/zh-tw-fix/gates/` (freeze/p8/occlusion JSONs + txt), render logs `hidden_files/w46/zh-tw-fix/render-*.log`, `webpdf-textmd.log`; full report `hidden_files/w46/zh-tw-fix/FIX-REPORT.md`.
