# PROOF NOTE — W47 ko-en, independent proof round 2 (proof2, fan-out #3 rebuild)

- Edition: `2026-w47-ko-en` (target ko, reader English), VOL.4
- Print PDF: `Lucerna-VOL4-KO-EN.pdf` 45,262,667 B, SHA-256 `1e2247c6196b4c3e9eede9b02dafa584bacbf941ba4a574352ad635d913b22c0` — verified, matches brief and the #3 builder record
- Web PDF: `Lucerna-VOL4-KO-EN-web.pdf` 4,011,476 B, SHA-256 `8fe16cdd926d50fdea0887b97daf193238287720f8d5333bb92c2f127000e182` — verified, matches brief and the #3 record
- text.md: `2026-w47-ko-en.text.md` 34,922 B, SHA-256 `9339a9931859db7b187a73042b7ec30656631fe369020d1b11fa100c1a03f846` — verified, matches brief and the #3 record (449 items)
- Core ko (read-only, never rebuilt): print `Lucerna-VOL4.pdf` 46,232,227 B, SHA-256 `53bf14edeca05f9db56e699b5d826f50c320eebcce200c4b876b394de21a2f27`; web 4,232,878 B, SHA-256 `9592945ae188dc8e50394fcab1ded155baaff63161bcf0b5f7ecbc6898c43bc7`; text.md 34,606 B, SHA-256 `da1d3a323f7c83eb95fe989e59f56ca6a706282c443f20cc5792c3f73468181a` — all match the #3 baseline exactly. Core is finalized; this proof touched core only by reading.
- Builder record: `hidden_files/w47/scratch-fanout-ko3/FANOUT-REPORT-ko3.md` + `ko3/en/EDITION-RECORD.md` (run 1). Both read; every builder conclusion re-verified independently below, none taken on trust.
- Probes: `git hash-object -w` OK; scratch dir writable; `/dev/null` present throughout (one exec aborted by a runtime restart mid-task — the 72 dpi web render it interrupted came out truncated and was re-rendered cleanly; nothing else was affected). TMPDIR kept in the goals scratch; no writes to the edition dir, no insert.py, no lint, no git writes.
- Scope: full re-proof from scratch per SOP §8 — all mechanical gates re-run independently (GATE-LOG.md), full SVG-text read (1,496 lines) + full text.md read (917 lines), visual read of all 8 print pages at 110 dpi + 300 dpi zoom of the P7 frame, 150 keys re-derived (REG on a scratch build-copy vs P8-SVG extract vs printed stems), #2-vs-#3 SVG-hash + text comparison.

## VERDICT: (a) 定稿 — zero defects

This round finds zero defects. D1 and D2 from proof1 are both closed on the page, in the source, and in the sweeps; the freeze CJK 7 are classified one by one; every hard gate passes.

### D1 CLOSED — P7 frame gloss straight quotes (proof1 D1)

- Source: `content7.py:81` now reads `wcn = "Frame: \"after ~\". Ask: \"〜 후에 뭐 해요?\""` (straight U+0022).
- Sweep: U+201C/U+201D/U+2019 = **0/0/0** across all 8 SVGs + text.md + ABSTRACT.txt.
- Page: 300 dpi zoom `work/p7-frame-zoom-proof2.png` shows `Frame: "after ~". Ask: "~ 후에 뭐 해요?"` with narrow straight quotes tight to the words — the proof1 full-width curly rendering is gone. Frame box true-ink headroom +9.9 px.

### D2 CLOSED — phrase #7 is a genuine article sentence (proof1 D2)

- Phrase #7 is now `수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요` with citation `(1면)` and the fix1-approved long note `After the CSAT ends, Kimchi Day comes on Sunday, Nov 22.`
- The sentence is verbatim the P1 lead (text.md L27; P1 SVG; P7 frame example, text.md L759; phrase list, text.md L799). `check_core` phrases: **8/8 verbatim**, including this sentence (ok p1).
- P7 frame example carries the same new sentence — P7 frame and phrase list are aligned with each other and with the core new sentence.

### Freeze CJK 7 — classified one by one (was 15 in fix1)

- `freeze.py diff` (system python3): added CJK **7, all U+3000**. Independent per-page U+3000 totals (core vs edition SVG text) confirm the tool exactly:
  - P2–P8: net **+1 each** = 7. Each is the footer alone: core `Lucerna　韩语周报 VOL.4　LUCERNA KOREAN WEEKLY` (2× U+3000) vs edition `Lucerna　KOREAN WEEKLY VOL.4　Korean text　English explanations` (3× U+3000). Every other U+3000-carrying string is paired 1:1 between core and edition.
  - P1: net **0** (total 19 = 19). The footer +1 is offset by −1: core's lead kicker `高考周　泡菜日也来了` (1× U+3000) has no U+3000 counterpart in the edition (English-only kicker).
- No other CJK character was added on any page.

## VERIFIED CLEAN (independent re-check)

### Mechanical gates — all pass (see GATE-LOG.md for commands/logs)
- run.py on a scratch copy (system python3): rc=0, 0 FLOW OVERFLOW / 0 HEAD TOO WIDE, TOTAL 150; A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; the 8 rebuilt SVGs are **byte-identical** to the shipped SVGs.
- Freeze baseline (system python3, README form `--build core-ko`): **8/8 byte-identical**, 8 files repointed, shipped core SVGs unchanged by the run. Venv control: freeze baseline under the venv **ABORTS rc=2** exactly as the guard prescribes for the ko family (Pillow 13 vs required 10) — the expected control, not a failure; guard not bypassed, not modified.
- Occlusion audit (venv, `--core`): selftest OK (6 classes fired, clean controls silent); **0 flags**; core 0; NEW vs core 0.
- p8.py extract: **150/150 noted**. p8.py compare vs core: **CLEAN**, missing=[] extra=0, keydiff=[137, 138] (expected E-group re-aiming).
- Text layers: print vs web **byte-identical** — 50,786 bytes (plain) and 102,397 bytes (`-layout`); all 8 pages non-empty in both PDFs. Print-vs-web pixel diff at 72 dpi: mean ≤0.59/page, P6 = 0.00 — layout identical, differences are image downsampling only.
- P8 min font: **9.975pt** (167 spans, 162 at-min) in **both** PDFs, ≥9.75pt.
- keycheck (REG vs P8 SVG, my own extract): **150/150** — 149 exact + #150 `✓` (expected, core identical); per-page 10/18/18/18/18/18/12/38 all match.
- Boxtitle: **8/8 ≤386.5px** (336.5 / 373.1 / 330.1 / 329.0 / 358.4 / 236.6 / 359.9 / 312.1).
- check_core + check_gloss (adapted runner, gloss prefix `Note — `): rc=0, gloss fails 0, phrases 8/8 verbatim, orphan scan 0, dates OK.
- Curly sweep 0/0/0; hanzi residual 0; orphan-punctuation scan 0 (no lone 。/」/：/–/— line, no line-start orphan).
- §1.1 counts: VOL.4 identical page-by-page; `·` identical (13/21/20/14/20/31/17/38); VOL.5 P7 3→2 by design (Korean `lko` disclosure removed); the `Page N of 8` line is the localized page line (core uses its own form) — not a difference.
- SVG hashes match the #3 builder record (`ko3/en/sha-en-run1.txt`) for all 8 pages.

### Cream boxes — 49/49 pass (dedicated audit, true ink)
- Every `#f0eee5` rect audited with the occlusion audit's own ink formula (`baseline − ascent + getbbox bottom`, real Noto CJK fonts). All 49 inside their boxes; tightest are the three "And you?" prompt boxes (P2/P3/P5) at **+5.1 px** — roomier than finalized core-ko's own +2.5 px for the same boxes. P7 frame +9.9 px; all others ≥10.9 px. (Occlusion BOXTITLE only covers stroked rects, so fill-only cream rects needed this dedicated pass; it passes.)
- P2/P3/P5 prompt boxes visually end inside the box on the renders; core's identical geometry is tighter.

### #2 vs #3 — only the #3 fixes changed, nothing else
- SVG hashes vs #2 run 2 (`fanout-ko/en/sha-en-run2.txt`): P2/P3/P5/P6/P8 **byte-identical**; P1/P4/P7 changed.
- Text diff (#3 SVG text vs proof1's #2 extraction, whitespace artifacts of the two extractors aside): the only real content changes are the core fixes — P1 Q10 stem `어디예요` → `어느 팀이에요` (correct "which team" form), P4 Q47 same stem fix, P4 Q48 `한국시리즈 시리즈 전적` → `한국시리즈 전적` (removes the duplicated word), P7 frame new sentence + straight quotes, P7 phrase #7 new sentence + long note + (1면). No other string changed.
- Cross-proof pixel comparison is confounded (mean ~4.5 even on byte-identical P8; neither a ±1 px shift nor a 2 px blur explains it — the two render sessions rasterize differently) and is not used as evidence; SVG hashes + text diff are authoritative.

### 150 keys — verified, 150/150
- Three sources agree for every key: REG (scratch-copy run), P8-SVG printed keys (own extract), and the printed stems on P1–P7.
- All 40 keys on changed pages hand-verified stem-by-stem against the articles: P1 #1–10 (incl. new Q10 wording, key A Samsung), P4 #47–64 (incl. fixed Q48, key C 4승 1패; #57–60 past forms; #61–64 matching), P7 #101–112 (incl. #110 A 산 전체의 약 80% vs P6 #89 B for the same fact in different option order — both correct in their own lists).
- The other 110 keys sit on pages byte-identical to #2, whose full hand verification from proof1 carries; keycheck + p8 compare re-confirm them mechanically here.
- #137/#138 re-aimed translations (expected keydiff); #150 `✓` model item; H model text recounts **169 characters excluding spaces (221 incl.)**, same convention as core.
- P8 answer-note prose spot-checked against keys (incl. #25–28/#43–46/#61–64 matching notes, #57–60 past forms, #137–140 "See page" pointers — all point at the right pages). Repeated option letter at the end of matching notes and "Weatheri" are core's own conventions — adjudicated, not defects (proof1).

### Text / content — full read
- text.md (917 lines) read in full + re-export reproduced **byte-identical** (34,922 B, 449 items) from a scratch copy. Title line, 8 page sections, no placeholders, curly 0/0/0.
- ABSTRACT.txt: 305 B, SHA `1187194316bea8381ec48d359fd41698d6e18e8e4dfa090889df92724fabc812` (matches record), one line, 0 ASCII double quotes, carries masthead/target/levels/150 exercises + real topics.
- All 8 pages visually clean at 110 dpi: no overflow, overlap, footer intrusion, or clipped text; all photos present with honest captions (Hokkoda file photo P1, early-20th-century US team photo P4, Cézanne P3, library P5, kimchi hands P7/P8); P1 drop cap reads "11월 16일…"; P4 ladder "LG가 두산에 4대 1로 승리" is core-identical (game-score `대`, adjudicated in proof1).
- Dates/weekdays, percentages, and external facts were fully verified in proof1 on byte-identical pages; the changed pages introduce no new fact (P1/P4 stems are wording fixes on the same verified facts).

## Observations (not defects)
- O1: text.md phrases citations — the `(n면)` citations are absent from text.md (the export captures only the note literal, not the `note + " (" + pg + ")"` concatenation) and one stray bare `1면` line stands at L781. **Byte-identical behaviour in finalized core-ko's text.md** (same stray `1면` after phrase #2). Shared `textmd.py` exporter quirk; the print PDF carries all 8 citations. Fix belongs in the exporter, not in this edition.
- O2: text.md drops the bare word "All" (P1 contents 8면 row), the F-section 2nd term, D-section stems, and P8 answer-key lines — same as #2 and core (proof1 O1); print unaffected, export quirk.
- O3: P3 column-2 top "않았어요." is a normal column-break word continuation ("확인되지 않았어요" split at a word boundary), not an orphan.
- O4: Cross-proof pixel diff is confounded by renderer differences between sessions (see above); not used as evidence.
- D5 font — **record only, not judged** (per brief, production-level pending item): print PDF embeds NotoSansCJKkr + NotoSerifCJKkr (Regular + Bold, subset) + UnifrakturMaguntia (masthead blackletter); web PDF embeds the same families under `Lucerna`-prefixed subset names. No Newsreader face in either PDF.

## Deliverables
- `PROOF-NOTE.md` (this file), `GATE-LOG.md`, `pages-print/p-1.png` … `p-8.png` (110 dpi print renders), `work/` (all gate logs, JSONs, scans, zoom crops `p7-frame-zoom-proof2.png`, `svg-text-proof2.txt`, re-export).
- No production file was modified; no commit; no push. Regenerable bulk intermediates (freeze build-copies, 72 dpi renders, full 300 dpi page) were deleted after verification; logs and hashes retained.
