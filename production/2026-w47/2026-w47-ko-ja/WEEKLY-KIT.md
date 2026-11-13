# Lucerna Weekly — W47 Korean, Japanese reader (VOL.4) — WEEKLY KIT

- Slug: `2026-w47-ko-ja` (target ko, reader Japanese)
- Issue week: 2026-11-16 (Mon) – 2026-11-22 (Sun), VOL.4
- Press time: **2026-11-10** (inherited from core-ko run 11). No score or event after Nov 10 is claimed; Nov 16–22 events are presented as scheduled. Nov 19-only measures are dated Nov 19 only.
- Format: 8 pages, 1950×2700, 4 columns, 150 exercises, continuous numbering 1–150, every exercise in the registry.
- Fan-out of the finalized ko core (`core-ko`, run 11 (fix1) + textmd fix2): Korean content frozen; only the explanation layer (glosses, box titles, instructions, "And you?" prompts, P7 letters disclosure, P8 answer notes, furniture) is in Japanese. Build interpreter locked to **/usr/bin/python3** (system PIL 10.2.0) — the venv (PIL 13.0.0) measures the same Korean serif strings ~1.1% wider and flips freeze 0/8 (core fix #15). render.py / webpdf.py still use the venv (cairosvg/fontTools, no PIL metrics).

## Lead topic

CSAT week: D-3 (Mon Nov 16) → advance assembly D-1 (Wed Nov 18) → D-day (Thu Nov 19), then Kimchi Day (Sun Nov 22). Second lead: Samsung's Korean Series title (4–1 over kt wiz, first since 2014). Third lead: kimjang cost down 9.0% to 199,456 won (aT, Nov 9 basis, announced Nov 10).

## Contents by page

- P1 (A2): lead (CSAT week + KS + kimjang cost), numbers box (3 / 1 / 199,456 / 4–1 / 12), calendar Nov 16–22, contents, word of the week 「예비소집」, autumn photo (Hakkoda file photo, honestly captioned), quiz 7–10.
- P2 (A2): kimjang cost feature, Kimchi Day box, History exam sign-up box (81st, Sat Nov 28, advanced only, 27,000 won), 김장 나눔, 겨울 밥상, shopping list, ssam photo, D-day strip (D-3/D-1/D-데이/김치의 날), ex. 11–28.
- P3 (A2→B1): Kimchi Day + late-foliage wrap-up (forecast vs observation; no observed Naejangsan peak announced at press time — readers sent to Weather Nuri 날씨누리), bukhansan-ui + Cézanne apples photos, ex. 29–46.
- P4 (B1): full Korean Series result (G1–G5 scores, venues, 4 straight wins after 1 loss, 9th title), postseason ladder (wildcard LG 4–1 Doosan, semi-playoff KIA 3–0 LG, playoff Samsung 3–2 KIA), K League box (FC Seoul early champions 33R, 36R Nov 21–22, finals Dec 5–6), ex. 47–64.
- P5 (B1): CSAT week, advance assembly (times/places vary by school), Nov 19-only measures, 수능이 끝나면, Kimchi Day youth ideas (WiKim youth session), 시험 전날의 하루, study photo, ex. 65–82.
- P6 (B2): 「예보에서 결과로」 — forecast→result theme; comparison table (last week vs this week: KS schedule→result Samsung 4–1; foliage forecast dates→passed; kimjang cost Oct 16 price→Nov 9 survey 199,456 won), ex. 83–100.
- P7 (A2→B2): A2 김치의 날의 말, B1 날짜 세는 말 (D-3/D-1/D-데이), B2 예보와 결과 읽는 법; error clinic (김치의날 spacing; 삼성는→삼성은; 담궈요→담가요; 날예요→날이에요); frame 「〜 후에」; readers' corner (editor's example letter + single Japanese disclosure; promise carried to **VOL.5**); P7 photo strip (kimchi-making, Anattadairy CC0); 8 P7 phrases, all verbatim from this issue's own articles; VOL.5 preview (HanNeungGeom Sat Nov 28, post-CSAT stories, Kimchi Day follow-up, letters/best P8 writing). Ex. 101–112.
- P8 (全部): 38 items — A 연표 8, B 일반 8, C mini-reading 4 (test character 민준이/Minjun, 수험생 story), D 造句 4, E 翻译 4 (stems 137/138 in Korean, keys translated to Japanese; stems 139/140 in Japanese, keys stay Korean), F 词汇配对 4, G dialogue 完形 5, H writing 1 「나의 김치의 날」 (model 169 chars, in 150–200). P8 photo (kimchi-making2, Anattadairy CC0) in col 4 below the H model. Full printed answers 1–150 with one-line Japanese notes.

## Measured exercise counts (final build, run 2 — fan-out #3, new edition from core run 11)

- TOTAL **150**; by page 1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38
- By level A2 51 / B1 72 / B2 27
- By type: 穴埋め 48, 選択問題 52, 組み合わせ 16, 書き換え 4, 文を作る 8, 正誤 4, 空所補充 13, 翻訳 4, 作文 1
- Model chars (H writing): 169
- No FLOW OVERFLOW / HEAD TOO WIDE warnings in the final build (run 1 was also clean — the two run-2 fixes are a box title and a wrapped P8 note, see Fixes log).
- **P8 answer font size (measured with PyMuPDF on the final print PDF): min 9.975 pt** (163 spans in the P8 answers region y≥1302/2700, 158 at 9.975pt) — above the SOP §1.1 threshold of 9.75 pt.
- Level badges ("chips"): 138 total, 35 on P8.

## Trend / fact sources

All facts inherited from core-ko run 11, whose KIT documents them with attribution caveats (Korean Series 4–1; Kimchi Day Nov 22; kimjang cost 199,456 won; CSAT Nov 19, 551,864 candidates; foliage forecasts incl. Weatheri Naejangsan Nov 11; fire-precaution period Nov 1–Dec 15; K League FC Seoul champions; HanNeungGeom 81st Nov 28; Hankook Tire kimjang sharing). Nothing after Nov 10 is claimed. No new facts were introduced by this fan-out; Japanese renderings only.

## Images (same 8 as core, all verified public-domain/CC0)

| File | Page | Author | Licence |
|---|---|---|---|
| autumn.jpg | P1 | lumoplank | CC0 |
| ssam.jpg | P2 | wizdata | CC0 |
| bukhansan-ui.jpg | P3 | Udonhan1992 | CC0 |
| apples.jpg | P3 | Paul Cézanne | Public domain |
| baseball.jpg | P4 | Bain News Service | Public domain |
| study.jpg | P5 | Gary Todd | CC0 |
| kimchi-making.jpg | P7 | Anattadairy | CC0 |
| kimchi-making2.jpg | P8 | Anattadairy | CC0 |

Full Commons page URLs and caption honesty notes in core-ko `assets/CREDITS.md`.

## Fan-out mechanism

- Core copied verbatim, then a translation map (`map-ja.json`, 216 keys + 8 instr, generated by `gen-map-ja.py` — generated from `gen-map-en.py` via `mk-lang.py ja` with `ja-replace.json` (en-value→Japanese-value) + `ja-meta.json`) applied by exact quoted-literal replacement, longest first, plus asserted structural edits (`apply-ko.py`).
- `svglib.py` copied verbatim, fonts frozen (md5 `1c94d836d46fcf6fc67e88b0f0febd34`, same as core).
- **Map-source discipline (learned on the it build, applied here):** the map values live in `gen-map-ja.py`'s embedded MAP dict — editing `ja-replace.json` alone does not change `map-ja.json`; `mk-lang.py ja` must regenerate the gen-map script first, then `gen-map-ja.py`, then re-apply. (Both run-2 fixes went through exactly this chain.)
- Gloss prefix `解説 — `; footer `Lucerna　韓国語週刊 VOL.4　本文は韓国語　解説は日本語` (corrected to the W46 Japanese precedent — the setup-phase meta had an English footer); page line `{n} ページ（全 {total} ページ）`.
- P7 letters: single Japanese disclosure replaces `lcn`; `lko` and `lcn2` lines + their render lines removed; `lh` formula rebuilt for 2 blocks (W46 ko-en precedent). Disclosure is 114 chars.
- P8 E-group re-aiming (W46 ko-en precedent): keys 137/138 translated to Japanese; stems 139/140 translated, keys stay Korean → `p8.py compare` keydiff `[137, 138]`, status CLEAN.
- P8 page separator `— 제{pg}면 —` stays frozen. H writing note is an f-string (structural edit: `このページのHセクションの模範解答（{NCHARS}字）`); H key is a plain map entry (`（自由課題 — 模範解答は下）`).
- KEYS_HALF / NOTE_WRAP: not present in ko core or shared tools; ko P8 keys already use dash style `n. key — note`, satisfied by construction.
- Straight apostrophe U+0027 only; U+2019 scan across all 8 SVGs = 0. Frame line uses 「」 (the map already carries the 「」 form, no post-apply fix needed).
- P8 answer-note person names checked one by one: the only personal name is 민준 (ミンジュン, #129 "ミンジュンは水曜日に予備招集に行きます", #135 note) — standard Revised Romanization, consistent within the edition; team/company names (Samsung, kt wiz, KIA, LG, FC Seoul, Weatheri, KBO) match core's own renderings. The ja-family sumo-romaji defect class does not apply here.
- Japanese renderings follow the W46 ko-ja precedent where noted: CSAT → 修学能力試験; キムチの日; キムジャン kept; 予備招集 (예비소집); 韓国史検定 (한능검); 山林庁 (Forestry Service); ウェザーアイ (Weatheri) kept; Japanese dates `11月16日` / `11月22日`; numbers `54,980ウォン`; score `4-1`. Type names: 穴埋め / 選択問題 / 組み合わせ / 書き換え / 文を作る / 正誤 / 空所補充 / 翻訳 / 作文. Instr: 空欄を埋める / 書き換える / 文を作る / 翻訳する / 書く / 単語と注を結ぶ / 山と注を結ぶ / 単語と意味を結ぶ.
- Probe was green from the start (P8 end 2351.0, headroom 189.0, P7 teaser_end 2454.7); no probe-phase shortenings were needed for ja.
- **Display artefact, not a defect (checked 2026-11-11):** the ja replace.json appeared to contain `��` in the 연승 gloss when dumped to the terminal; byte-level check (unicode_escape) shows the gloss is clean — `연승 = 連勝 · 정상 = 頂点 · 통산 = 通算 · 확정하다 = 確定する`, U+00B7 separators intact, U+FFFD count 0 in the map and in the edition sources.

## Self-proofread record (full pass over rendered pages + extracted SVG text + text.md)

- **Run 1 (fan-out #3, 2026-11-11):** build clean (0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150); P2-feature ends 1531, P8-keys ends 2351, P7 teaser 2454.7. boxtitle 7/8 (P3 title OVER — see Fixes log #1). p8.py compare FAILED SHORT missing=[81] (the #81 note wrapped — see Fixes log #2). Discarded.
- **Run 2 (fan-out #3, 2026-11-11, shipped):** build clean (0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150); P2-feature ends 1531, P8-keys ends 2351, P7 teaser 2454.7. boxtitle 8/8. All gates pass except the freeze baseline, which is BLOCKED by a tooling conflict (see Mechanical gates / Freeze note). Full visual read of all 8 print pages at 100dpi: zero issues (P1 `すべて` in contents, quiz #10 new sentence; P2 `買い物リスト` box fully inside the feature area, g2 gloss 2 lines, D-day strip clean; P3 shortened `知っておく` title on one line; P7 Pattern box `枠組み：「〜のあと」`, phrase #7 new sentence + (1면), Japanese clinic/disclosure; P8 F header `単語と意味を結ぶ`, E 137/138 Japanese keys, #81 a single line, H model text correct). Full self-read of `2026-w47-ko-ja.text.md` (450 items): zero issues. All 150 keys re-derived (keycheck 150/150; #150 `✓` expected, identical in core).
- **Independent proofread:** not yet done — to be assigned by the coordinator (proof1 for this edition, separate person). This KIT records the builder's self-check only.

## Fixes log

| # | Found | Fix | Round |
|---|---|---|---|
| 1 | P3 box title OVER after apply round 1: `김치의 날에 알아 둘 것　知っておくこと` 393.4px vs 386.5px limit (boxtitle 7/8) | Shortened in the map source (`ja-replace.json`: `知っておくこと` → `知っておく`), then `mk-lang.py ja` + `gen-map-ja.py` + re-apply; boxtitle 8/8, title renders on one line in the P3 box | run 1 → run 2 |
| 2 | P8 #81 answer note wrapped to a second line: the note `リスニングの時間は飛行機が飛ばない` (15 chars) measured 463.5px for the full answer line at 13.3px, past the ~420–464px wrap threshold (widest fitting answer line 420.1px), so the P8 key printed as `81. 비행기는 듣기 시간에 뜨지 않아요. —` with the note on the next line, and p8.py compare failed SHORT missing=[81] (the extractor reads one text element per answer) | Shortened in the map source (`ja-replace.json`: `リスニングの時間は飛行機が飛ばない` → `聴解中は飛行機が飛ばない`, 12 chars, 397.6px — comfortably below the widest fitting line; 聴解 is the standard Japanese term for the listening test, meaning preserved), then `mk-lang.py ja` + `gen-map-ja.py` + re-apply; #81 is now a single line `81. 비행기는 듣기 시간에 뜨지 않아요. — 聴解中は飛行機が飛ばない`, p8.py compare CLEAN. Only the P8 SVG changed between run 1 and run 2; text.md byte-identical (the note is not in the text.md export set) | run 1 → run 2 |
| 3 | Frame line: no defect — the map already carries the 「」 form (`枠組み：「〜のあと」。たずね方：「〜 후에 뭐 해요?」`) | None needed; post-build sweep U+201C = 0, U+201D = 0, U+2019 = 0 across all 8 SVGs + text.md; the 「」 form is visible in the P7 render and in text.md | run 2 |
| 4 | Independent reproof (2026-11-12): 6 exact-duplicate exercise slots (Q12/Q13/Q22/Q47/Q74/Q102), P1 lead sentence missing "다른 날의" | Q12/Q13/Q22/Q47/Q74/Q102 replaced with new questions from same-page article facts (P2 kimjang cost 13.4% below average, 6 kimjang ingredient types, chili powder -1.8%, P4 Samsung 9th title, P5 exam ticket by 8 a.m., P7 Kimchi Day fixed by law Feb 2020); P8 keys + reader notes updated; P1 sentence → "이번 주의 다른 날의 조치가 아니에요". Rebuilt + re-gated: TOTAL 150, p8 CLEAN, occlusion 0, spill/boxtitle/edge 0, textlayer PASS, text.md 456 items | fix rebuild 2026-11-12 |
| 5 | Independent reproof round 2 (2026-11-12, PROOF-NOTE-2): R2-1 text.md export drops 7 numbered items (P2 D Q26, P4 D Q61–Q63, P8 B Q121/Q126, P8 F Q142) | R2-1: `textmd.py` global `seen` dedup replaced by per-call-site retention for `.ex`/`.match_set` items (plain prose keeps global dedup); text.md re-exported, 8 items restored per edition (7 numbered + P6 table row label `김장비용`, same root cause, verified against the print P6 table); per-page inventory 150/150, match terms 16/16 standalone, whole-book 150/150; PDFs untouched (print/web SHA unchanged); p8 compare CLEAN (keydiff [137, 138]), D5 census PASS (0/0/0, curly 0) | fix rebuild 2, 2026-11-12 |

## Adjudicated (not defects)

- **Freeze baseline BLOCKED (tooling conflict, not an edition defect):** `tools/freeze.py` gained a runtime guard at 2026-11-11 12:00 (uncommitted working-tree change) that aborts unless Pillow major == 13 (`tools/venv`). It contradicts the family's interpreter lock (core KIT fix #15 + task brief: build + freeze under `/usr/bin/python3`, PIL 10.2.0). Evidence: freeze.py baseline under the venv on this system-python3-built edition gives **0/8** (all 8 SVGs differ — dual-stack drift, PIL 13 re-measures Korean spacing ~1.11px wider per space boundary); the 8 editions built before 12:00 (en/de/es/fr/it/pt/nl/ru) froze 8/8 under `/usr/bin/python3`. The guard was NOT bypassed and the edition was NOT rebuilt under the venv (both would hide the conflict / break family consistency). The guard's own rationale cites the pt-ko 0/8, which was freeze(venv) vs build(sys) — the same mismatch. Coordinator decision needed: revert the guard, or move the family build stack to the venv. Logs: `hidden_files/w47/scratch-fanout-ko3/ja/freeze-ja.log` (ABORT rc=2) and `ja/freeze-ja-venv.log` (0/8, build-copy deleted after the run).
- **Freeze diff added CJK 2901** (p1 122, p2 257, p3 204, p4 154, p5 211, p6 121, p7 345, p8 1487) — expected: Japanese explanations are CJK vs core. Adjudicated by machine check (`ja/verify-freeze-diff4.py`): all 307 added strings and all 303 removed strings traced to ja map values / instr / structural strings (footer, page-line f-string, gloss prefix `解説 —`, H writing-note f-string, answer-line composites `N. KEY — NOTE`, notes + `(N면)` citations, E-stem blanks rendered as nbsp). 0 unexplained on either side. The last removed string needed the core H f-string (`范文见本版 H 区（{NCHARS}字）`, a JoinedStr in the AST, not a plain literal).
- P8 match-item notes end with the option letter repeated: the letter is in the source note literal itself, core's own convention.
- #43/#123/#124 notes "内蔵山：山林庁の予想では紅葉のピークは11月4日" / "内蔵山：ウェザーアイの予想では11月11日" / "内蔵山：山林庁の予想ではピークは11月11日": core's own renderings of the Weatheri (private weather company) and Forestry Service (산림청) forecasts — not typos.
- P8 #150 key renders as `✓` in both core and edition (verified: core extract #150 == `'✓'`); the "（自由課題 — 模範解答は下）" text is the exercise stem, not the printed key.
- P7 VOL.5 count 3 (core) → 2 (ja): core's `lko` Korean disclosure line was removed by design (single reader-language disclosure).
- text.md 450 items vs core 452: two accounted drops, no content gap — (1) `lcn2` removed by design; (2) `lko` removed by design. The Japanese P1 contents 8면 level `すべて` IS in text.md — CJK passes is_prose, so ja drops one fewer item than the Latin editions (449). Run-2 text.md byte-identical to run 1 (the #81 note is not in the export set — P8 answer notes are not collected by textmd.py, same for en).
- Repeated page citations (1면/2면/4면/6면) appear once in text.md: textmd.py dedupes repeated citation strings — the rendered P7 phrases carry the full per-phrase citations (check_core phrases 8/8 verbatim).
- P8 answer-note stem 10.35pt is the recorded core adjudication — not a defect, not changed.
- `text.md` contains `___` (75 places) — exported from the source literals, where blanks stay as `___`; the SVG/PDF render them as 1.1pt ink underlines. Same as core.

## Occlusion audit

- `tools/occlusion_audit.py` on the edition dir: **0 flags**. Selftest first: planted classes fired {BOXTITLE: 1, COVER: 1, EDGE: 1, FOOTER: 1, LINEX: 1, TEXTX: 1}; clean controls silent. Log at `hidden_files/w47/scratch-fanout-ko3/ja/occlusion-ja.log` (json `occlusion-ja.json`).

## Mechanical gates (final state, run 2)

- `run.py` (build run 2, `/usr/bin/python3`): exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150 (A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; P2-feature ends 1531, P8-keys ends 2351, P7 teaser 2454.7). Log `hidden_files/w47/scratch-fanout-ko3/ja/build-ja-run2.log`; SVG hashes `ja/sha-ja-run2.txt`. (Run 1 log `ja/build-ja-run1.log` kept as evidence of the #81 fix.)
- `tools/freeze.py baseline` (**BLOCKED** — see Adjudicated): the runtime guard (added 2026-11-11 12:00) aborts under `/usr/bin/python3` (rc=2, log `ja/freeze-ja.log`); under the venv it gives 0/8 (log `ja/freeze-ja-venv.log`, build-copy deleted). No 8/8 baseline exists for this edition until the coordinator resolves the interpreter conflict. The 8 editions built before 12:00 froze 8/8 under `/usr/bin/python3`.
- `tools/freeze.py diff` (core-ko svg vs edition svg, run under the venv — diff is a pure text comparison, interpreter-independent): TOTAL added CJK characters **2901** (see Adjudicated). Log `ja/freeze-diff-ja.log` (+ json `ja/freeze-diff-ja.json`, verification `ja/verify-freeze-diff4.py`).
- `tools/p8.py extract` on `svg/p8-siheom.svg`: **noted set = 150 of 150** (parse: lines). Log `ja/p8-extract-ja.log`, json `ja/p8-ja.json`. `compare` vs core P8: **CLEAN** (missing=[] extra_count=0 keydiff=[137, 138]). Log `ja/p8-compare-ja.log`. (Run 1 compare failed SHORT missing=[81] — see Fixes log #2.)
- `check_core.py` / `check_gloss.py` (scratch copies with ED + gloss prefix patched to the edition): **gloss fails 0, orphan issues 0**, phrases 8/8 verbatim (incl. the new phrase #7 with (1면)); dates all correct. Log `ja/check-ja.log`.
- Text layers: print and web PDFs each extract to **53,212 bytes, byte-identical** (`cmp` rc 0). Extracts `ja/print-ja.txt`, `ja/web-ja.txt`; empty diff `ja/textlayer-diff-ja.txt`.
- P8 min font 9.975pt (PyMuPDF on the print PDF, P8 answers region y≥1302/2700: 163 spans, 158 at 9.975pt), ≥ 9.75pt. Log `ja/p8font-ja.log`.
- 150-key check (`keycheck-ko.py`, REG from edition sources vs keys extracted from P8 SVG): 149 exact + #150 `✓` (expected) = **150/150**. Log `ja/keycheck-ja.log`; full table in `ja/EDITION-RECORD.md`.
- §1.1 grep audit: paper `#fbfaf6` 1×/page (P4/P6 4×, same as core — colour also used in table cells), VOL.4 correct on all pages, VOL.5 0 except P7 (2, by design), `·` counts identical to core page-by-page and only in gloss/option/credit contexts, colour set identical to core page-by-page; hanzi set-checked (825 CJK chars on P8, all in the edition's source literals — no stray CJK). Log `ja/style11-ja.log`.
- Census (`census.py`, ex/match stems + D6 segments vs text.md): ex/match 166 items, 0 missing; D6 0 missing. Log `ja/census-ja.log`.
- Visual read: all 8 print pages at 100dpi, zero issues. PNGs in `hidden_files/w47/scratch-fanout-ko3/ja/pages/`.

## Output files + sizes (final render, run 2)

- Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ko-ja/`
- Print PDF: `Lucerna-VOL4-KO-JA.pdf` — **50,279,548 bytes**, 8 pages, SHA-256 `f8c7508f9be83c8fd83ffca7041864df83609ea394972132c93f5e79e64c8a6d` (fix rebuild 2026-11-12; D5 value was 50,274,489 bytes / `387b3922ce85…`)
- Web PDF: `Lucerna-VOL4-KO-JA-web.pdf` — **4,373,107 bytes** (< 7 MB), 8 pages, SHA-256 `f9bb1d3a392996ba8344083be0aac90ed30873ddb2ab8f296516de656c65b7f8` (fix rebuild 2026-11-12; D5 value was 4,361,673 bytes / `eddc96d9fe6d…`); pdftotext **53,268 bytes, byte-identical to the print PDF**.
- Text export: `2026-w47-ko-ja.text.md` — 36,275 bytes, 8 pages, 464 items, SHA-256 `be048d7d4164ed8466642665f18bdf765174ccfff62342642a489327f6d71a9e` (exported from source via the fixed `textmd.py` (md5 `00d8f52d96ecad396cbc03603d98fa9b`), never from PDF). Byte-identical to the run-1 export (the #81 note is not in the export set; re-exported 2026-11-12 (fix round 2, R2-1: textmd.py dedup fix, 8 items restored, 456→464 items)).
- `ABSTRACT.txt`: 342 bytes, SHA-256 `4a9445de3848203250f4d4992a79fb08992dada8cd0f747e2b745746f453157a`. `Lucerna Korean Weekly VOL.4：修学能力試験までD-3、試験は11月19日、キムチの日は11月22日でキムジャンの費用は199,456ウォン、サムスンの12年ぶりの韓国シリーズ優勝、韓国史検定の申込みと晩秋の紅葉 — 韓国語の本文に日本語の解説付き、レベルA2〜B2、150問。`
- `WEEKLY-KIT.md`: this file. Build records: `hidden_files/w47/scratch-fanout-ko3/ja/EDITION-RECORD.md`.

## Open verification debts (carried to the parent line)

- Independent proofread of this edition not yet done — to be assigned by the coordinator (proof1, separate person from the builder).
- ~~Freeze baseline blocked by the tools/freeze.py runtime guard (added 2026-11-11 12:00)~~ — RESOLVED 2026-11-12 by the D5 rebuild: freeze ran under the coordinator-approved one-off system-python3 exception (see D5 section below); `baseline` 7/8 with the P1 display-"1" interpreter artefact adjudicated, `diff` vs base-venv added CJK 0.
- Fact debts inherited from core-ko (see core KIT): no observed Naejangsan/Wolchulsan foliage peak announced at Nov 10 press time; HanNeungGeom details (other than date/time/fee) from secondaries; K League 35R scores not verified — not cited; WiKim Festival 2026 time/theme/session not found in an independent source (printed as scheduled).

## D5 rebuild (2026-11-12, SOP §1.1)

- Template: `mechanism/svglib-ko-d5.py` installed as edition `svglib.py` (`_D5_READER = "cjk"`, reader ja; diff vs template: 1 line, `_D5_READER` only). Old svglib kept as `svglib.pre-d5` in the edition dir and in `hidden_files/w47/scratch-d5-ko/2026-w47-ko-ja/pre/`.
- Build: `tools/venv/bin/python` throughout. `run.py` TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE. Base-venv control (old svglib + venv) TOTAL 150 with the known P2 FLOW OVERFLOW warning (core content, also present pre-D5).
- Gates (all in `hidden_files/w47/scratch-d5-ko/2026-w47-ko-ja/`): D5 census PASS (Latin 0 / Cyrillic 0 / curly-in-CJK 0; production baseline was 210 Latin); `census_quotes.py` 0 defective glyphs; `head_check.py` PASS 0 defects; `occlusion_audit.py` 0 flags; `p8.py extract` 150/150, `compare` vs core-ko CLEAN (keydiff=[137, 138], expected reader-language keys); `spill_sweep.py` 0 SPILL (348 OBSERVE, 49 boxes); `boxtitle_check.py` 0 DEFECT (63 titles, 1089 body lines); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` 0 absolute defects (ratios n=390 median 1.006 boldT 1.040 boldF 1.000; P8 206→205 lines, slack 78.1→78.1px); text layer print/web char-multiset diff 0 (19,284 = 19,284, pdftotext 53,150 bytes byte-identical).
- `freeze.py` (system python3 Pillow 10.2.0, coordinator-approved one-off exception): `diff` patched vs base-venv RC=0, added CJK 0 (Latin strings +447 from run splitting, expected). `baseline` 7/8 (P2–P8 OK; P1 differs): adjudicated interpreter artefact, same as core-ko — P1 text multiset identical (0 diff, verified by direct SVG text comparison, 1128 runs each); only the big display "1" (185 vs 183pt) + knock-on x shifts (31 elements, 0 text-content diffs). Production (venv, canonical) is self-consistent.
- No content files changed. No true D5 defects in this edition.
