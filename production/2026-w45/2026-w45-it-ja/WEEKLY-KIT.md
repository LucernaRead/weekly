# La Lucerna — Italian Weekly, VOL.2, week of 2–8 November 2026
## Italian × Japanese edition (IT×JA) — BUILDER KIT (not a finalization notice)

**Pairing:** text in Italian · explanations in Japanese — the edition for Japanese-speaking readers.
**Base:** W45 IT core (`files/weekly-report-w45-it-core/`, VOL.2), frozen for all Italian body text; only the explanation layer is translated into Japanese.
**Counts (measured from the core, not copied from another language family):** 150 exercises; levels A2 47 / B1 70 / B2 33; page distribution P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38; model text 81 words.
**Topics:** the first cold snap of November; 2 November Commemoration of the Dead; Panettone World Cup final in Milan, 7–8 November 2026; Festa del Torrone in Cremona; Serie A matchday 11.
**Deliverables in this directory:** `svg/` ×8, `cards/` ×8, `La-Lucerna-VOL2-JA.pdf` (print), `La-Lucerna-VOL2-JA-web.pdf` (web), this KIT, `ABSTRACT.txt`.
**Build tree:** `hidden_files/weekly-report-w45-it-ja-build/` — `transform.py` (single source of truth, including all fix rounds), per-round sha256 baselines, gate outputs, and the scripts `scan_ja.py`, `rightedge.py`, `rowcheck.py`, `chartcheck.py` (the latter three copied from the IT×EN build for identical methodology).
**Status:** builder-complete. Independent proofread is still required before finalization; this KIT does not declare the edition finalized. The edition has not been posted to Discord, sent into the main chat, or pushed to any repo by this build.

## Per-page contents

- **P1 Prima (10):** top story "Arriva il primo freddo", pairing badge, settimana day-by-day, cifre box, parola box, IN BREVE, QUIZ LAMPO 7–10, frost drawing (redazione).
- **P2 Vita (18):** first cold / dressing / 2 November, NOTE box, LO SAPEVI, E TU, FRASE box, exercises 11–28.
- **P3 Cultura (18):** Panettone final Milan, Torrone Cremona, Alba white truffle (photo + PD credit), NOTE box, IL WEEKEND DOLCE, E TU, exercises 29–46.
- **P4 Sport (18):** Serie A matchday 11 + European cups, fixture table, NOTE box, E TU, exercises 47–64.
- **P5 Giovani (18):** after Lucca Comics, Forum Cultura Milan, Festival dei Popoli Florence, piano box, NOTE box, E TU, chestnut photo + CC0 credit, exercises 65–82.
- **P6 Approfondimento (18):** how to read a forecast (probability, not certainty), practice chart (invented data, labelled DATI INVENTATI PER L'ESERCIZIO), NOTE box, Manovra disclosure in Japanese, exercises 83–100.
- **P7 Lingua (12):** three level columns (A2 weather verbs, B1 passato prossimo, B2 congiuntivo), ERRORI TIPICI, LA PAROLA «l'assaggio», LETTERE DEI LETTORI, FRASI DELLA SETTIMANA (8 golden sentences), LA PROSSIMA SETTIMANA (VOL.3).
- **P8 Valutazione (38):** test sections A–H (113–150) + full answer key grouped by page, Japanese separators "— N ページ —", model text in section H (81 words).

## Furniture (measured from the shipped W43 IT×JA SVGs, which govern over README #20 generalizations)

- Pairing badge, P1, replacing the (975,372) tagline call, sans 20 bold, BRICK #a4553a, centred: "イタリア語テキスト · 日本語の解説 — 日本語読者のための版".
- P1 top strip: "OGNI SETTIMANA IN ITALIANO · 毎週一号 · イタリア人が読んでいるイタリア語を読む"; P1 subtitle (spaced form, 46pt): "イ タ リ ア 語 週 刊 · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A"; P1 dark-band right: "初寒の週 · 詳しくは2ページ".
- Footer: "La Lucerna · イタリア語週刊 VOL.2 · 本文はイタリア語 · 解説は日本語"; page line "N ページ（全 8 ページ）"; gloss prefix "解説 — " (single, 6 occurrences: P1 expl + P2–P6 boxes, double prefix 0); P7 grammar prefix "文法ポイント — " (×3).
- Section headers keep Italian first + Japanese tail ("LA NOTIZIA · トップニュース", "VITA · 生活", "CULTURA · 文化", "SPORT · スポーツ", "GIOVANI · 青年", "LINGUA · 言語", "APPROFONDIMENTO · 深掘り", "VALUTAZIONE E RISPOSTE · 演習と答え", "ESERCIZI · Nページの練習", "E TU? · あなたは？", "ERRORI TIPICI · よくある間違い", "LA PAROLA · 今週の言葉", "FRASI DELLA SETTIMANA · 今週の名文（今号の記事からそのまま引用）", "LA PROSSIMA SETTIMANA · 次号予告 (VOL.3)").
- P7 golden-sentence page tags keep the frozen Italian form "(Pagina N)".
- P8 titles: "RISPOSTE · 全解答と解説（1–8ページ）"; right note "各問に日本語の短い解説つき · ✓ は模範文のある問題"; separators "— N ページ —".
- Instruction words: 空所補充 / 文を作る / 正誤 / 語と意味を結ぶ / 翻訳 / 作文; P8 E-section directions: 137–139 "日本語に翻訳", 140 "イタリア語に翻訳".
- Registry type names (never printed) stay in Chinese, exactly as in the W43 IT×JA / W45 IT×EN precedents, keeping the registry byte-comparable with the core; the P8 writing type check therefore also stays.

## Method

- `transform.py` applies literal `rep()` replacements only; each `rep()` fails loudly if its old string is absent, so a typo can never silently skip a translation. Italian target text is never a replacement target. Every fix-round edit went into `transform.py`; content files were restored pristine from the core build before each re-render.
- Repointing: all five content files plus `render.py` change `weekly-report-w45-it-core` to `weekly-report-w45-it-ja`; PDF names become `La-Lucerna-VOL2-JA.pdf` / `La-Lucerna-VOL2-JA-web.pdf`.
- Re-renders run through the single driver process: `run.py` then `render.py` under `tools/venv/bin/python` (system python3 has no cairosvg).
- Interpreters / libraries (recorded separately as required): run.py — `tools/venv/bin/python`, Python 3.12.3, Pillow 13.0.0; render.py — `tools/venv/bin/python`, Python 3.12.3, Pillow 13.0.0.
- svglib: the canonical JA version, md5 `d73e23b365676c3618d7e060b835eb4d` (verified before the build, after the build, and after every restore; kinsoku + SEAM_SLACK=28). The canonical file was never edited; the one tool-level consequence (the audit's relative-path misparse, see Fix round 1) was fixed in the audit tool itself, not in svglib.
- `bridge()` renamed to `expl()` following the W43 IT×JA precedent (definition + all 22 calls, last step of the transform so the string reps still match).
- Registry dumps were not needed: counts were verified from the rendered SVGs themselves (chips + printed numbers + P8 key groups), independent of the registry.

## Measured gates (final round, round 2)

- **Core freeze:** `tools/freeze.py baseline` reproduced 8/8 core SVGs byte-identical before any editing (with the core svglib in the copy; the JA svglib swap is a separate documented step and its metric delta is expected). Core SVGs re-hashed after the build: 8/8 OK, unchanged (`core-svg-baseline.txt`).
- **Freeze diff:** per-page added/removed strings close as explanation-layer churn only. Italian-word multiset check (CJK stripped, Latin tokens compared): core-only words are exactly the replaced 372 strapline, the footer "LUCERNA ITALIAN WEEKLY", and the P8 "PAGINA" separators; edition-only Latin tokens are the katakana-"セリエA" letter artifacts, the P1 parola-gloss "il primo freddo", and the second "VOL.3" mention in the Japanese letter note. All other removed/added pure-Latin fragments are wrap-point re-splits of identical Italian words (JP Latin metrics slightly narrower — the W43 IT×JA §7(b) class).
- **Explanation-layer purity:** every CJK run in the edition SVGs is a substring of a Japanese string in `transform.py` (word-level residual scan, 0 unmatched); a denylist scan for Chinese-only words and simplified-only characters returns 0 on all 8 pages (the scanned list is recorded in the build dir, not in this KIT). Shared-kanji words (生活, 文化, 青年, 初雪, 死者の日, 優秀作文, 模範文) are standard Japanese usage. The banned explanation-layer term appears in no deliverable (SVG, KIT, ABSTRACT all scanned, 0).
- **P8:** `tools/p8.py compare` (explicit paths) reads CLEAN 150=150, missing=[], extra_count=0, uncertain=[]. Keydiff list [6, 13, 14, 15, 38, 58, 71, 74, 77, 137, 138, 139] adjudicated item by item below. P8 notes are pure Japanese; the printed-note set is equal (no EXTRA_ONLY items at all).
- **Occlusion:** `tools/occlusion_audit.py` edition 0 flags (self-test OK), core 0 flags, NEW vs core 0 (outputs `occlusion-r2.json`, `occlusion-new-r2.json`, `occlusion-core-r2.json`).
- **Chart labels (P6):** baseline-anchored ink method (PIL getmetrics, anchor `ls`), worst chart-label coverage 0.0%, gate <30% — pass (`chartcheck.py`).
- **Right edge (all 8 pages):** ADVANCE method, 0 violations past the frame line (1910). Four margin-zone entries (1885, 1910]: three byte-identical frozen Italian lines also present in the core (P1 parola lines, P2 match line); the fourth is the same frozen P8 model-text line, displaced from y=633 to y=663 because the JA P8 exercise flow ends lower — inherited content, not new (`rightedge-ja.txt` vs `rightedge-core.txt`).
- **Same-baseline collisions (all 8 pages):** 7 entries, byte-identical to the core's 7 — the P1 sommario label/title pairs with a designed 4.0 px gap, no overlap — inherited, not new (`rowcheck-ja.txt`).
- **Gloss:** rendered `gloss()` strings split on `·` and counted item by item: core [6, 5, 4, 4, 5] total 24, JA identical [6, 5, 4, 4, 5] total 24; P1 expl 4 items both sides.
- **P7 golden sentences:** all 8 occur exactly 2× in both core and JA when node texts are joined with spaces; all 8 quote nodes present verbatim on P7 with frozen "(Pagina N)" tags.
- **P7 word box (blocking gate):** Italian definition sentence kept verbatim — "« l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere se piace. Questa settimana vive a pagina 3, alla finale del Panettone." — only the gloss localized: "assaggio = 試食。第3ページ：パネットーネ決勝で観客は無料で試食できます。" Errori notes are terse one-liners at 19.5pt, holding the core's column-3 geometry exactly (P7 column 3 ends y=1673.0, exactly the core value, 13 px clear of the FRASI rule at y=1686).
- **Column-3 ends (final):** P2 1025.0, P3 1281.25, P4 875.0, P5 1285.75, P6 1096.5, P7 1673.0 — all within their limits.
- **Independent recount (from rendered SVGs, chips + printed numbers, not the registry):** 150 items, continuous 1–150, levels A2 47 / B1 70 / B2 33; per-page 10/18/18/18/18/18/12/38; P8 key groups per page identical (10/18/18/18/18/18/12/38), 150 keys continuous. Registry comparison agrees: meta diffs (page/level/type) NONE; key diffs only #137, #138, #139, #150 (see below); note diffs all 150 (translated).
- **Model text:** 81 words, text byte-identical to the core.
- **Japanese line-start scan:** kinsoku closers + small kana + ASCII closers, all 8 pages, 0 orphans in the final round (`scan_ja.py`).
- **Visual inspection:** all 8 cards viewed page by page (P1 badge/subtitle/cifre box/frost, P2 FRASE box, P3 photo + credit, P4 fixture table, P5 photo + credit, P6 chart + caption, P7 column stack + FRASI + letter box, P8 key block ending with footer clearance). No defects observed in the final round.
- **Overflow:** zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the final render (`build-log-r2.txt`).

## P8 keydiff adjudication (12 items)

- **9 dash-branch extraction artifacts, not real key changes** (the canonical tool was NOT modified; adjudication only): for #6 previsioni, #13 guanti, #14 crisantemi, #15 termosifoni, #38 mandorle, #58 più bella, #71 gratuiti, #74 castagne, #77 ci sarà, the printed key (text before " — ") is byte-identical on both sides; only the note differs (Chinese → Japanese). Same family as the tools README #13 dash-truncation lesson.
- **3 genuine keydiffs, all legal E-section re-aims** (same item numbers as the W43 IT×JA ruling): #137 "月曜日に最初の寒さがやってきます。" / #138 "観客は無料で試食できます。" / #139 "日曜の夜、フィオレンティーナ対ユヴェントス。" — each with instruction "日本語に翻訳".
- **Not in keydiff, confirmed separately:** #140's printed key is identical Italian ("Ogni previsione deve essere chiara.") with the body re-aimed to "すべての予報は明確でなければならない。→ ___" (instruction "イタリア語に翻訳"); #150's key is "✓ 模範文は本ページ H 欄（81 語）" with no answer key, as in the core.

## Readers' corner — no fabrication

The Italian letter stays frozen verbatim including "(esempio della redazione)". The Japanese note states all three disclosure facts plus an imperative invitation: "編集部の例文です。本物の手紙も8ページの優秀作文も未着で、約束はVOL.3へ。手紙を送ってください。VOL.3に掲載します！" (1: no real letters yet; 2: no best page-8 essay yet; 3: the sample stands in and both are promised for VOL.3; invitation: 手紙を送ってください + VOL.3に掲載します). Per the coordinator clarification, NO new Italian disclosure sentence was written (the core has none, W43 has none, IT×DE has none, and P7 col3 has no spare room); the frozen Italian elements (letter, label, VOL.3 preview promise in the next-week band) stand with this Japanese disclosure. No reader, letter, name, or quote was invented.

## Fix-round record

- **Round 1 (initial):** 150 exercises, correct levels/pages, P7 column 3 ends 1673.0, zero overflow warnings. Defects found by the gates: (a) occlusion 33 flags on P1 — 31 frost-path artifacts + 2 cifre-title flags (see tool fix below); (b) orphan scan 2 small-kana line starts (P3/P5 E TU notes).
- **Fix round 1 (tool fix, in `tools/occlusion_audit.py` — NOT in the canonical svglib, NOT in the edition):** the audit's `shape_box` path branch treated every number in a path `d` as an alternating (x, y) pair, so the JA svglib frost path ("M451 2022 l20 -14 ...") misread its relative deltas as absolute coords and produced a page-spanning bogus box (-20, -14, 571, 2022) covering 31 texts. Fix: a proper path walker (`_path_points`) tracking the current point and resolving relative commands (M/L/H/V/C/S/Q/T/A, implicit lineto, comma/sign separators); curve control points included (conservative). Regression evidence: JA frost box now equals the core's absolute-L box exactly (451, 2008, 571, 2036); selftest still OK (all 6 planted classes fire, clean controls silent); core audit still 0; W43 IT×JA still 0; the doctored BOXTITLE case still fires with the exact historical geometry (1888.0 > 1885.0). After the fix the edition read 2 flags, both the real cifre-title defect.
- **Fix round 2 (wording only, in `transform.py`; pre-fix baselines in `baseline-round2-pre.txt`):** (a) P1 cifre box title → "LA SETTIMANA IN CIFRE · 数字で今週" (the W43 IT×JA precedent form; ink now inside the 412 px slot, audit 0); (b) P3 E TU note → "伝統的なパネットーネとチョコレート味、どちらが好き？2文書いて送りましょう。" (2 wrap-verified lines, no bad line starts; was 3 lines with a stranded "ょう。"); (c) P5 E TU note → "ルッカの後、どこへ：文化フォーラム、映画、食の祭り？2文書いて送りましょう。" (2 wrap-verified lines; was 3 lines with a stranded "ォーラム…"). Round 2 change scope verified by sha256: only P1/P3/P5 SVG+cards and both PDFs changed; P2/P4/P6/P7/P8 byte-identical. Round 2: zero overflow/wide warnings; P3 col3 1281.25, P5 col3 1285.75 (each −29, one fewer E TU line, self-consistent via the box-height formula); P7 col3 still 1673.0.
- **Transform incident (round 0, before round 1):** the first transform run aborted midway on an over-escaped apostrophe (`l\\\'Europa` in the search string); the partial output was discarded, content files were restored pristine from the core build, the escaping was fixed (single backslash, as in the IT×EN precedent), and the transform was re-run to a clean TRANSFORM COMPLETE. The aborted run changed no shipped file.

## W43 deviation list (furniture matches W43 IT×JA except where noted)

1. VOL.1 → VOL.2 in the footer (required by the issue).
2. P1 subtitle topics, band-right text, and all article-driven furniture strings follow the W45 core content (same patterns, new week).
3. P1 parola gloss, E TU notes, and all exercise notes are new-week Japanese translations (same patterns, new content); the P3/P5 E TU notes were shortened in fix round 2 for kinsoku (see above).
4. Readers'-corner Japanese note states the three disclosure facts explicitly + imperative invitation (see above); W43's note was a shorter sample-letter sentence, and the W45 core's disclosure facts are the VOL.3-carryover facts (see core KIT §6).
5. P8 E-section re-aims #137–#140 and #150 note follow the W43 IT×JA ruling exactly (same item numbers).
6. FRASE box title ("LA FRASE PER RICORDARE · 覚え方") uses tsize=19 — the W45 IT×EN precedent for an over-wide box title (W43 IT×JA's title was shorter).
7. P1 cifre title shortening and P3/P5 E TU shortenings (fix round 2) are JA-build-only wording fits; no layout parameter was changed in any round.
8. The occlusion-audit path-parser fix (fix round 1) is a shared-tool improvement, not an edition deviation; it is recorded here and in the tool file.
9. Everything else — badge geometry, footer pattern, page line, gloss prefix, P8 separators, RISPOSTE titles, band-sub patterns, instruction words, image assets and credit lines, registry type names — matches W43 IT×JA.

## Reproduce

```
cd hidden_files/weekly-report-w45-it-ja-build
cp ../weekly-report-w45-it-build/content{12,34,56,7,8}.py ../weekly-report-w45-it-build/bslib4.py ../weekly-report-w45-it-build/render.py .
cp ../weekly-report-ja-build/svglib.py .   # canonical JA, md5 d73e23b365676c3618d7e060b835eb4d; never edit
rm -rf __pycache__
tools/venv/bin/python transform.py
tools/venv/bin/python run.py
tools/venv/bin/python render.py
```

## Final files (round 2)

- Print PDF `La-Lucerna-VOL2-JA.pdf`: 20,236,595 bytes, sha256 4f66a914729d70233eea3f68379250454e5ee3ea984cb7e60414e0470ecf670a
- Web PDF `La-Lucerna-VOL2-JA-web.pdf`: 3,509,235 bytes, sha256 d3b629deed6b33c9eb5df9b5cff8282ab37feaa9159da17c44f27174402da423
