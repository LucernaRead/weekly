# PROOF-NOTE — 2026-W47 ru-ko (Russian target × Korean reader) — proof1

**Edition:** `production/2026-w47/2026-w47-ru-ko/` · VOL.4 · issue Mon 16–Sun 22 Nov 2026 · 8 pages
**Proofreader:** independent proof1 (subagent), 2026-11-11
**Conclusion: (b) — DEFECTS FOUND, CANNOT FINALIZE**

## §0 Identity (verified against task, all three match)

| file | bytes | SHA-256 | task |
|---|---|---|---|
| `Lucerna-VOL4-ru-ko.pdf` | 22,002,774 | `4e450e65c7c5dfb5b2574a5400ccd98be5f687c2e2341d44a95b312134055ca0` | match |
| `Lucerna-VOL4-ru-ko-web.pdf` | 3,474,892 | `797af4e6e622d16a04577ae25b4ddea8e21c7dc668a56e172d945c06350984f0` | match |
| `2026-w47-ru-ko.text.md` | 65,002 | `a1cbef3614a72175d3a46a943cf899071b12909f07ee28d81f775c424c687f99` | match |

(See GATE-LOG §0 for the one KIT discrepancy: KIT §5 says text.md is 58,811 bytes; disk says 65,002. SHA matches the task, so the KIT number is stale — not a defect.)

## Defects — 6 classes, 12 instances

### D1 — Homoglyph substitution: Hangul syllable inside a Russian word (MEDIUM, this edition's fan-out / build source)

The most serious class: a single Hangul syllable replaces Cyrillic letters inside a Russian word that learners are meant to read. Two instances, same class.

**D1a — P2, word-box gloss.** Russian word "родина" rendered as Cyrillic `роди` + Hangul `나` (U+B098).
- Location: P2 gloss box, SVG node x=899.8 y=381.94, font Noto Sans CJK SC 20.5 (the `роди` part is Noto Sans 20.5).
- Evidence: card shows `해설 — поздравить 축하하다 · роди나 / 고향 · повод 계기.`; freeze word-diff shows `родина`→`роди`+`나`; mixed-script sweep flagged it; `content12.py` gloss string is `f.gloss("поздравить 축하하다 · роди나 고향 · повод 계기.")`; also present in text.md L99.
- Fix: replace Hangul 나 with Cyrillic на in `content12.py`, re-render, re-export text.md.

**D1b — P7, B2 column bridge.** Russian phrase "синоптики обещают" rendered as Hangul `시` (U+C2DC) + Cyrillic `ноптики`.
- Location: P7 B2 bridge, SVG node x=989.0 y=660.30, Noto Sans CJK SC 20.5; full line reads `시놉틱스 обещают 예보관들이 약속한다; по данным 에 따르면;...`.
- Evidence: visually visible on the P7 card (the 시 glyph is a compact Hangul block among Cyrillic letters); `content7.py` bridge string `c.bridge("시놉틱스 обещают 예보관들이 약속한다; по данным 에 따르면; может быть 아마.")`; text.md has `시놉틱스` 1× vs correct `синоптики` 4× / `Синоптики` 8×. All other occurrences of синоптики/Синоптики on P7 (y=304 quote, y=435, y=906, Q102/Q109) are clean Cyrillic.
- Note: KIT §7 claims this bridge was "fixed" for a syllable split — the fix string it quotes (`예보관들이 약속한다; по данным 에 따르면`) does not match the actual bridge string, which prepends the Russian head; the corruption is in the Russian head, so the claimed fix never touched it.
- Fix: replace Hangul 시 with Cyrillic си in `content7.py`, re-render, re-export text.md.

### D2 — P2 D-section option b horizontal overflow (LOW, this edition's layout/fan-out)

- Location: P2 exercises band, D matching, option `b. Международный день студента`, y=2162.
- Evidence (three methods agree): PIL true-ink right edge 1871.2px (+9.2px past the right text edge 1862); rendered-card pixel scan max ink x=1869 (+7px) in rows y=2149–2161; print-PDF span ` Международный день студента` ends 1402.5pt (=1870px). Other D options end 1681–1829 (inside). No collision or clipping — 7–9px into blank margin — but a real overflow of the exercises column.
- Fix: wrap `студента` to a second line (or re-lay the option).

### D3 — Mid-word Korean syllable splits at line breaks (MEDIUM, systematic — wrap engine; this edition's build)

The wrap engine breaks Korean words between syllables instead of at word boundaries. KIT §7 says build 2 fixed three such instances (P4/P5/P7) and a simulator "confirms each new string breaks only at word boundaries" — but that validation covered only the three fixed strings. A whole-edition wrap sweep (SVG line-boundary analysis, `wrap-sweep3.txt`, cross-checked against source strings in `content*.py`) finds **six more instances** the build-2 fix never swept:

| # | page | location (SVG baseline) | split | word |
|---|---|---|---|---|
| D3a | P1 | lead-article gloss bridge, y=1105.6 → 1135.3 | 원 / 고 | 원고 (manuscript) |
| D3b | P2 | "А ВЫ?" box, y=1097.2 → 1125.6 | 편집 / 부에 | 편집부에 (to the editorial office) |
| D3c | P2 | "А ВЫ?" box, y=1125.6 → 1154.0 | 모로 / 즈에게 | 모로즈에게 (to Ded Moroz) |
| D3d | P3 | P3 gloss box, y=268.2 → 298.0 | 동 / 화 | 동화 (fairy tale) |
| D3e | P3 | B-section instruction, y=2534.7 → 2564.4 | 채우 / 세요 | 채우세요 (please fill in) |
| D3f | P7 | readers'-letters disclosure, y=1682.0 → 1710.4 | 편 / 집부 | 편집부 (editorial office) |

- Evidence: each was confirmed both in SVG node lines (e.g. P3 gloss lines `…сказочное 동` / `화.`) and visually on the rendered cards (P1 gloss `…на момент сдачи 원` / `고 마감 시점…`; P2 box `…써서 편집` / `부에 보내세요…데드 모로` / `즈에게 한 문장.`; P7 disclosure `…않았습니다: 편` / `집부 예시, VOL.5로 이어집니다.`).
- The sweep's completeness check: all other Korean line boundaries in the edition were tested the same way and are word boundaries (incl. P2 gloss `роди나`/`고향`, P4 gloss `поправка`/`정정`, P6 chart labels, P8 key lines — separate entries, not wraps). A second variant sweep (either-side Hangul, digit/Latin-adjacent splits) found no further mid-word splits.
- Fix: the wrap engine must prefer spaces for Korean text (same class of fix as build 2, but applied edition-wide and re-validated with a whole-edition sweep after rebuild). Each instance needs its string re-laid so the break falls at a space.

### D4 — Q30 key note: film title "Rocky" transliterated as 로키 (LOW, translation slip, this edition)

- Location: text.md Q30 key note and P8 printed key (key list, "— СТРАНИЦА 3 —"): `30. A — 〈로키 — 그게 나야〉는 스탤론 전기 영화`.
- Evidence: «Рокки — это я» is the film *Rocky*; standard Korean rendering is **록키** (e.g. 록키 발보아). 로키 is the Korean rendering of "Loki". The stem keeps the Russian title, so the error is confined to the parenthetical key note, but a Korean reader seeing 로키 reads "Loki".
- Fix: change 로키 → 록키 in the Q30 key note (content source + text.md + re-render P8 key line).

### D5 — Web PDF loses the P1 italic phrase: italic dropped + closing » detached (LOW, web-PDF builder)

Reproduces 2 of the 3 symptoms of the ru-en D3 web-PDF defect class (see task item (e)).
- Location: P1 "СЛОВО НЕДЕЛИ" word box, italic «чёрная пятница» (SVG y=1712; PDF line y=1266.76).
- Evidence:
  - Web PDF embeds **0 italic fonts** (font list: only LucernaNewsreader-Regular, LucernaNotoSerif-Regular/Bold, etc.); print embeds `Newsreader16pt-Italic` + `NotoSerif-MediumItalic`. Visual crops (`italic-print.png` vs `italic-web.png`) confirm: print renders the phrase slanted; web renders it upright.
  - PyMuPDF span dump: print span text is `чёрная пятница` (space present, italic faces); web span text is literally `чёрнаяпятница` (space character lost at span level), font LucernaNotoSerif-Regular.
  - Extracted text: print line 206 `«чёрная пятница»`; web line 206 `«чёрная пятница »` — closing » detached by a space. Span geometry: web span ends 1218.9pt, » starts 1220.6pt (1.7pt gap → pdftotext inserts a space); print span ends 1222.8pt, » starts 1220.6pt (italic overhang, no gap).
  - All other «чёрная пятница» occurrences (article lines 31/41/284, Q-lines) are byte-identical between print and web; only the italic word-box occurrence differs.
  - The space inside is recovered by pdftotext's gap heuristic, so the plain-text extraction of the phrase still reads with a space; the » detachment and the lost italic are the extraction-visible and visual defects.
- Fix: web-PDF builder must embed the italic faces (and keep the space glyph) for the P1 italic span.

## Required-check items (a)–(e) — verdicts

- **(a) P1 boxtitle/subtitle horizontal overflow — DOES NOT REPRODUCE.** Three methods: PIL true-ink right-edge scan of every P1 text node (max ink-right 1862.0, exactly the designed right margin); PDF span check (widest span `ГОДА` ends 1397.7pt = 1863.6px, but pixel scan shows no P1 ink past x=1862 — span-bbox padding, not ink); 200dpi-equivalent pixel scan of all 8 cards for dark pixels past x=1862 (excluding footer band y>2596): P1, P3–P8 clean; only P2 has ink past the margin (D2). P1 cream-box titles: all first-line and max-inside ink-right clearances positive (min +18.2px).
- **(b) P3/P5 right-column cream-box descender spill — DOES NOT REPRODUCE.** PIL true-ink clearances huge: P3 boxes +68.3/+68.1, P5 box +68.4. The only inside-only negative desc-clear in the whole edition is P2 (see GATE-LOG §2) and it measures true-ink clear +3.0px.
- **(c) P7 toolbox clearance — PASS.** Canonical creambox full scan: P7 summary 3 boxes, min inside clearance +11.9, min desc-clear +5.9 (positive). Visually confirmed on the P7 card.
- **(d) text.md E-section type labels un-localized — DOES NOT REPRODUCE.** Q137–140 carry `[A2/B1/B2 · 번역]` with `[번역]` tags; no Chinese 「翻譯」 anywhere in text.md. P8 E-section prints `137. 번역` etc.
- **(e) Web-PDF italic triple-symptom — REPRODUCES (2/3).** See D5: italic lost + » detached; the space is lost at span level but recovered by pdftotext heuristics.

## Open items

- **O1 — Re-verify after rebuild.** After D1–D5 are fixed and the edition is re-rendered, re-run: (i) mixed-script sweep (D1), (ii) whole-edition wrap sweep (D3), (iii) web-PDF italic check via `italic-print.png`/`italic-web.png` method (D5), (iv) P2 D-option pixel scan (D2). The D3 fix must be validated edition-wide, not per-string — build 2's per-string validation is what let the six instances through.
- **O2 — Wrap-engine fix is upstream.** D3 is an engine defect (Korean break preference), not six independent typos. The fix belongs in the wrap engine / glossary layout, with the whole-edition sweep added to the proof gates.
- **O3 — P8 Morozko image stays out by design.** The P8 Morozko illustration + caption are absent (same as W46 ru-ko, per KIT — skipped by the build's own condition). Accepted as conditional-by-design, not a defect; text.md retains the trailing credit line. If the build condition changes, the caption must come back with it.

## Verification summary

- Full read: print PDF 8 pages (cards p1–p8) + text.md 840 lines, all read.
- 150-question hand verification (`keycheck-150.json`): 150/150 — inline keys = Answers section = P8 printed keys, 0 mismatches (Q150 is an open writing question: P8 prints the ✓ marker; consistent in substance). Counts verified: pages 10/18/18/18/18/18/12/38; levels A2 50 / B1 76 / B2 24; types 문장 완성 54 / 객관식 55 / 단어 짝짓기 20 / 문장 만들기 12 / 문장 바꾸기 4 / 번역 4 / 쓰기 1. Model text verified 97 words. Keydiff [137–140] adjudicated: edition keys are correct Korean translations of the Russian stems (core keys are Chinese); all four correct.
- Mechanical gates (all re-run independently, see GATE-LOG): occlusion 42/42 CLEAR (36 row-gap + 6 visual); creambox full scan clean except the P2 desc-clear false positive (+3.0px true ink); p8 compare CLEAN; freeze diff + baseline 8/8 byte-identical; print/web text layer present on all 8 pages (33,706 vs 33,753 chars, whitespace-only difference except D5 line 206); P8 min font 9.75pt = SOP floor (at the allowed minimum, not a defect); curly quotes: only the intentional P7 pair; boxtitle true-ink checks clean except D2.
- Facts checked against the edition itself + `date -d`: weekday claims all correct — 16 Nov Mon, 17 Tue, 18 Wed, 19 Thu, 20 Fri, 27 Nov Fri (Black Friday calendar date), 30 Nov Mon (Cyber Monday), 12 Nov Thu, 8 Nov Sun; P4 results table (8 matches, 6–8 Nov, Fri/Sat/Sun) matches Q52–60 keys exactly (Krylia–Orenburg 2:0, Spartak–Akron 2:1, Lokomotiv–Rubin 0:1, Krasnodar–CSKA 4:2, Zenit–Rostov 2:2, Baltika–Dynamo Mkh 0:1, Dynamo–Fakel 2:1); round-15 fixtures 20–22 Nov Fri–Sun consistent; chart sums 100% (38/26/18/18); 8 golden sentences verified verbatim in their cited articles with correct page refs (P1×2, P2×1, P3×1, P4×1, P5×1, P6×2).
- Source files were NOT modified, rebuilt, committed, or pushed.
