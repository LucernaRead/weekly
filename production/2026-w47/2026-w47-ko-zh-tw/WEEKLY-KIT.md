# Lucerna Weekly — W47 Korean, Traditional Chinese reader (VOL.4) — WEEKLY KIT

- Slug: `2026-w47-ko-zh-tw` (target ko, reader Traditional Chinese)
- Issue week: 2026-11-16 (Mon) – 2026-11-22 (Sun), VOL.4
- Press time: **2026-11-10** (inherited from core-ko run 11). No score or event after Nov 10 is claimed; Nov 16–22 events are presented as scheduled. Nov 19-only measures are dated Nov 19 only.
- Format: 8 pages, 1950×2700, 4 columns, 150 exercises, continuous numbering 1–150, every exercise in the registry.
- Fan-out of the finalized ko core (`core-ko`, run 11 (fix1) + textmd fix2): Korean content frozen; only the explanation layer (glosses, box titles, instructions, "And you?" prompts, P7 letters disclosure, P8 answer notes, furniture) is in Traditional Chinese. Build interpreter locked to **/usr/bin/python3** (system PIL 10.2.0) — the venv (PIL 13.0.0) measures the same Korean serif strings ~1.1% wider and flips freeze 0/8 (core fix #15). render.py / webpdf.py still use the venv (cairosvg/fontTools, no PIL metrics).
- **This is a Korean-target edition with a Traditional Chinese reader** — it is NOT a zh-cn × zh-tw pair directory (AGENTS.md forbids the pair; this slug is `ko-zh-tw`, one of the 130 grid cells). Simplified and Traditional Chinese remain independent editions, never inter-translated: every reader string was written fresh in Traditional Chinese, not converted from the core's Simplified strings.

## Lead topic

CSAT week: D-3 (Mon Nov 16) → advance assembly D-1 (Wed Nov 18) → D-day (Thu Nov 19), then Kimchi Day (Sun Nov 22). Second lead: Samsung's Korean Series title (4–1 over kt wiz, first since 2014). Third lead: kimjang cost down 9.0% to 199,456 won (aT, Nov 9 basis, announced Nov 10).

## Contents by page

- P1 (A2): lead (CSAT week + KS + kimjang cost), numbers box (3 / 1 / 199,456 / 4–1 / 12), calendar Nov 16–22, contents, word of the week 「예비소집」, autumn photo (Hakkoda file photo, honestly captioned), quiz 7–10.
- P2 (A2): kimjang cost feature, Kimchi Day box, History exam sign-up box (81st, Sat Nov 28, advanced only, 27,000 won), 김장 나눔, 겨울 밥상, shopping list, ssam photo, D-day strip (D-3/D-1/D-데이/김치의 날), ex. 11–28.
- P3 (A2→B1): Kimchi Day + late-foliage wrap-up (forecast vs observation; no observed Naejangsan peak announced at press time — readers sent to Weather Nuri 날씨누리), bukhansan-ui + Cézanne apples photos, ex. 29–46.
- P4 (B1): full Korean Series result (G1–G5 scores, venues, 4 straight wins after 1 loss, 9th title), postseason ladder (wildcard LG 4–1 Doosan, semi-playoff KIA 3–0 LG, playoff Samsung 3–2 KIA), K League box (FC Seoul early champions 33R, 36R Nov 21–22, finals Dec 5–6), ex. 47–64.
- P5 (B1): CSAT week, advance assembly (times/places vary by school), Nov 19-only measures, 수능이 끝나면, Kimchi Day youth ideas (WiKim youth session), 시험 전날의 하루, study photo, ex. 65–82.
- P6 (B2): 「예보에서 결과로」 — forecast→result theme; comparison table (last week vs this week: KS schedule→result Samsung 4–1; foliage forecast dates→passed; kimjang cost Oct 16 price→Nov 9 survey 199,456 won), ex. 83–100.
- P7 (A2→B2): A2 김치의 날의 말, B1 날짜 세는 말 (D-3/D-1/D-데이), B2 예보와 결과 읽는 법; error clinic (김치의날 spacing; 삼성는→삼성은; 담궈요→담가요; 날예요→날이에요); frame 「在〜之後」; readers' corner (editor's example letter + single Traditional Chinese disclosure; promise carried to **VOL.5**); P7 photo strip (kimchi-making, Anattadairy CC0); 8 P7 phrases, all verbatim from this issue's own articles; VOL.5 preview (HanNeungGeom Sat Nov 28, post-CSAT stories, Kimchi Day follow-up, letters/best P8 writing). Ex. 101–112.
- P8 (全部): 38 items — A 연표 8, B 일반 8, C mini-reading 4 (test character 민준이/Minjun, 수험생 story), D 造句 4, E 翻譯 4 (stems 137/138 in Korean, keys translated to Traditional Chinese; stems 139/140 in Traditional Chinese, keys stay Korean), F 词汇配对 4, G dialogue 完形 5, H writing 1 「나의 김치의 날」 (model 169 chars, in 150–200). P8 photo (kimchi-making2, Anattadairy CC0) in col 4 below the H model. Full printed answers 1–150 with one-line Traditional Chinese notes.

## Measured exercise counts (final build, run 1 — fan-out #3, new edition from core run 11)

- TOTAL **150**; by page 1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38
- By level A2 51 / B1 72 / B2 27
- By type: 填空 48, 單選 52, 配對 16, 句型轉換 4, 造句 8, 是非 4, 克漏字 13, 翻譯 4, 寫作 1
- Model chars (H writing): 169
- No FLOW OVERFLOW / HEAD TOO WIDE warnings in the final build.
- **P8 answer font size (measured with PyMuPDF on the final print PDF): min 9.975 pt** (163 spans in the P8 answers region y≥1302/2700, 158 at 9.975pt) — above the SOP §1.1 threshold of 9.75 pt.
- Level badges ("chips"): 138 total, 35 on P8.

## Trend / fact sources

All facts inherited from core-ko run 11, whose KIT documents them with attribution caveats (Korean Series 4–1; Kimchi Day Nov 22; kimjang cost 199,456 won; CSAT Nov 19, 551,864 candidates; foliage forecasts incl. Weatheri Naejangsan Nov 11; fire-precaution period Nov 1–Dec 15; K League FC Seoul champions; HanNeungGeom 81st Nov 28; Hankook Tire kimjang sharing). Nothing after Nov 10 is claimed. No new facts were introduced by this fan-out; Traditional Chinese renderings only.

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

- Core copied verbatim, then a translation map (`map-zh-tw.json`, 216 keys + 8 instr, generated by `gen-map-zh-tw.py` — generated from `gen-map-en.py` via `mk-lang.py zh-tw` with `zh-tw-replace.json` (en-value→Traditional-Chinese-value) + `zh-tw-meta.json`) applied by exact quoted-literal replacement, longest first, plus asserted structural edits (`apply-ko.py`).
- `svglib.py` copied verbatim, fonts frozen (md5 `1c94d836d46fcf6fc67e88b0f0febd34`, same as core).
- **Map-source discipline (learned on the it build, applied here):** the map values live in `gen-map-zh-tw.py`'s embedded MAP dict — editing `zh-tw-replace.json` alone does not change `map-zh-tw.json`; `mk-lang.py zh-tw` must regenerate the gen-map script first, then `gen-map-zh-tw.py`, then re-apply. (No map change was needed for zh-tw after the first apply — boxtitle 8/8, run clean, compare CLEAN on the first run.)
- Gloss prefix `譯注｜`; footer `Lucerna　韓語週報 VOL.4　正文韓語　講解繁體中文` (corrected to the W46 zh-tw precedent — the setup-phase meta had a partially English footer); page line `第 {n} 版 / 共 {total} 版` (corrected from `第{n}頁／共{total}頁` per the W46 bslib4 form).
- P7 letters: single Traditional Chinese disclosure replaces `lcn`; `lko` and `lcn2` lines + their render lines removed; `lh` formula rebuilt for 2 blocks (W46 ko-en precedent). Disclosure is 5 lines.
- P8 E-group re-aiming (W46 ko-en precedent): keys 137/138 translated to Traditional Chinese; stems 139/140 translated, keys stay Korean → `p8.py compare` keydiff `[138]` (not [137, 138] — see Adjudicated: the #137 key is script-identical between Simplified and Traditional).
- P8 page separator `— 제{pg}면 —` stays frozen. H writing note is an f-string (structural edit: `本版H區範文（{NCHARS}字）`); H key is a plain map entry (`（開放題，範文如下）`).
- KEYS_HALF / NOTE_WRAP: not present in ko core or shared tools; ko P8 keys already use dash style `n. key — note`, satisfied by construction.
- Straight apostrophe U+0027 only; U+2019 scan across all 8 SVGs = 0. Frame line uses 「」 (the map already carries the 「」 form, no post-apply fix needed; it renders across two text elements in the P7 Pattern box, complete).
- P8 answer-note person names checked one by one: the only personal name is 민준 (民俊, #129 "民俊星期三去預備召集", #135 note) — standard Revised Romanization, consistent within the edition; team/company names (Samsung 三星, kt wiz, KIA, LG, FC Seoul, Weatheri, KBO) match core's own renderings. The ja-family sumo-romaji defect class does not apply here.
- Traditional Chinese renderings follow the W46 ko-zh-tw precedent where noted: CSAT → 韓國高考 (the term TW/HK media use for the Korean exam; NOT 學測); 泡菜日; 泡菜 (kimjang); 預備召集 (예비소집); 韓史檢定 (한능검); 山林廳 (Forestry Service); Weatheri kept; Traditional Chinese dates `11月16日` / `11月22日`; numbers `54,980韓元`; score `4比1`. Type names: 填空 / 單選 / 配對 / 句型轉換 / 造句 / 是非 / 克漏字 / 翻譯 / 寫作. Instr: 填空 / 改寫 / 造句 / 翻譯 / 寫作 / 把詞和說明配對 / 把山和說明配對 / 把詞和釋義配對.
- Probe was green from the start (P8 end 2351.0, headroom 189.0, P7 teaser_end 2425.7, disclosure 5 lines); no probe-phase shortenings were needed for zh-tw.
- **textmd.py invocation (corrected during this build):** the usage is `textmd.py <build_dir> <slug> <out_path> <title_line>` — 4 positional args. With cwd = the edition dir, build_dir is `.`: `textmd.py . 2026-w47-ko-zh-tw 2026-w47-ko-zh-tw.text.md "Lucerna Korean Weekly VOL.4 — Korean text, Traditional Chinese explanations (2026-W47)"`. A 3-arg form (missing build_dir) fails with `IndexError: list index out of range`. The fan-out record's earlier rendering of the command dropped the build_dir — this KIT records the working 4-arg form.
- **Environment quirk (2026-11-11 ~12:20 UTC):** `/dev/null` is missing from this VM (`ls: cannot access '/dev/null': No such file or directory`). The git probe `echo test | git -C <repo> hash-object -w --stdin` failed once with `fatal: could not open '/dev/null'` and succeeded on retry (hash `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`). Same transient error killed a `git log`/`git diff` attempt earlier in the day. Not an edition issue; noted here so a later builder does not mistake it for a repo fault.

## Self-proofread record (full pass over rendered pages + extracted SVG text + text.md)

- **Run 1 (fan-out #3, 2026-11-11, shipped):** build clean (0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150); P2-feature ends 1531, P8-keys ends 2351, P7 teaser 2425.7. boxtitle 8/8 on the first run. All gates pass except the freeze baseline, which is BLOCKED by a tooling conflict (see Mechanical gates / Freeze note). The nl P2-feature overflow defect class and the ja P8 #81 wrapped-note defect class were both checked and did not occur (P2-feature ends 1531; p8.py compare CLEAN on the first run). Full visual read of all 8 print pages at 100dpi: zero issues (P1 `全部` in contents, quiz #10 new sentence; P2 `泡菜採購清單` box fully inside the feature area, g2 gloss 2 lines, D-day strip clean, `說說你自己` box complete; P3 `泡菜日須知` box; P7 Pattern box `句式拆解：「在〜之後」`, phrase #7 new sentence + (1면), Traditional Chinese clinic/disclosure; P8 F header `把詞和釋義配對`, E 137/138 Traditional keys, H model text correct). Full self-read of `2026-w47-ko-zh-tw.text.md` (450 items): zero issues. All 150 keys re-derived (keycheck 150/150; #150 `✓` expected, identical in core).
- **Independent proofread:** not yet done — to be assigned by the coordinator (proof1 for this edition, separate person). This KIT records the builder's self-check only.

## Fixes log

| # | Found | Fix | Round |
|---|---|---|---|
| — | No defects found in the first build. No post-apply fixes were needed. | — | run 1 |
| 1 | Independent reproof (2026-11-12): 6 exact-duplicate exercise slots (Q12/Q13/Q22/Q47/Q74/Q102), P1 lead sentence missing "다른 날의" | Q12/Q13/Q22/Q47/Q74/Q102 replaced with new questions from same-page article facts (P2 kimjang cost 13.4% below average, 6 kimjang ingredient types, chili powder -1.8%, P4 Samsung 9th title, P5 exam ticket by 8 a.m., P7 Kimchi Day fixed by law Feb 2020); P8 keys + reader notes updated; P1 sentence → "이번 주의 다른 날의 조치가 아니에요". Rebuilt + re-gated: TOTAL 150, p8 CLEAN, occlusion 0, spill/boxtitle/edge 0, textlayer PASS, text.md 456 items | fix rebuild 2026-11-12 |
| 2 | Independent reproof round 2 (2026-11-12, PROOF-NOTE-2): R2-1 text.md export drops 7 numbered items (P2 D Q26, P4 D Q61–Q63, P8 B Q121/Q126, P8 F Q142) | R2-1: `textmd.py` global `seen` dedup replaced by per-call-site retention for `.ex`/`.match_set` items (plain prose keeps global dedup); text.md re-exported, 8 items restored per edition (7 numbered + P6 table row label `김장비용`, same root cause, verified against the print P6 table); per-page inventory 150/150, match terms 16/16 standalone, whole-book 150/150; PDFs untouched (print/web SHA unchanged); p8 compare CLEAN (keydiff [138]), D5 census PASS (0/0/0, curly 0) | fix rebuild 2, 2026-11-12 |
## Adjudicated (not defects)

- **Freeze baseline BLOCKED (tooling conflict, not an edition defect):** `tools/freeze.py` gained a runtime guard at 2026-11-11 12:00 (uncommitted working-tree change) that aborts unless Pillow major == 13 (`tools/venv`). It contradicts the family's interpreter lock (core KIT fix #15 + task brief: build + freeze under `/usr/bin/python3`, PIL 10.2.0). Evidence: freeze.py baseline under the venv on this system-python3-built edition gives **0/8** (all 8 SVGs differ — dual-stack drift, PIL 13 re-measures Korean spacing ~1.11px wider per space boundary); the 8 editions built before 12:00 (en/de/es/fr/it/pt/nl/ru) froze 8/8 under `/usr/bin/python3`. The guard was NOT bypassed and the edition was NOT rebuilt under the venv (both would hide the conflict / break family consistency). The guard's own rationale cites the pt-ko 0/8, which was freeze(venv) vs build(sys) — the same mismatch. Coordinator decision needed: revert the guard, or move the family build stack to the venv. Logs: `hidden_files/w47/scratch-fanout-ko3/zh-tw/freeze-zh-tw.log` (ABORT rc=2) and `zh-tw/freeze-zh-tw-venv.log` (0/8, rc=1, build-copy deleted after the run).
- **Freeze diff added CJK 822** (p1 47, p2 66, p3 49, p4 60, p5 56, p6 42, p7 97, p8 405) — lower than ja's 2901 because core is already Simplified Chinese: most CJK is shared, and the diff is the Simplified→Traditional script change plus the new Traditional-only strings. Adjudicated by machine check (`zh-tw/verify-freeze-diff-zh-tw.py`): all 267 added strings and all 268 removed strings traced to zh-tw map values / instr / structural strings (footer, page-line f-string, gloss prefix `譯注｜`, H writing-note f-string, answer-line composites `N. KEY — NOTE`, notes + `(N면)` citations, E-stem blanks rendered as nbsp) or, for removed strings, to core map keys / core source literals. 0 unexplained on either side. The H notes on both sides are f-strings (JoinedStr in the AST, never plain literals), so both rendered forms were hardcoded in the verifier: zh-tw `本版H區範文（169字）`, core `范文见本版 H 区（169字）`.
- **p8.py compare keydiff [138] (not [137, 138])** — correct by construction: the E-group re-aiming translates keys 137/138 to Traditional Chinese, but the #137 key `11月22日是泡菜日。` is script-identical between Simplified and Traditional Chinese, so the extracted keys match; only the NOTE differs (對照第2版 vs 对照第2版) and notes are not keys. The #138 key differs (時隔12年奪冠 vs 时隔12年夺冠). Verified in the P8 SVG.
- P8 match-item notes end with the option letter repeated: the letter is in the source note literal itself, core's own convention.
- #43/#123/#124 notes "內藏山：山林廳預測紅葉高峰在11月4日" / "內藏山：Weatheri預測高峰在11月11日" / "內藏山：山林廳預測高峰在11月11日": core's own renderings of the Weatheri (private weather company) and Forestry Service (山林廳) forecasts — not typos.
- P8 #150 key renders as `✓` in both core and edition (verified: core extract #150 == `'✓'`); the "（開放題，範文如下）" text is the exercise stem, not the printed key.
- P7 VOL.5 count 3 (core) → 2 (zh-tw): core's `lko` Korean disclosure line was removed by design (single reader-language disclosure).
- text.md 450 items vs core 452: two accounted drops, no content gap — (1) `lcn2` removed by design; (2) `lko` removed by design. The Traditional Chinese P1 contents 8版 level `全部` IS in text.md — CJK passes is_prose, so zh-tw drops one fewer item than the Latin editions (449).
- Repeated page citations (1面/2面/4面/6面) appear once in text.md: textmd.py dedupes repeated citation strings — the rendered P7 phrases carry the full per-phrase citations (check_core phrases 8/8 verbatim).
- P8 answer-note stem 10.35pt is the recorded core adjudication — not a defect, not changed.
- `text.md` contains `___` (75 places) — exported from the source literals, where blanks stay as `___`; the SVG/PDF render them as 1.1pt ink underlines. Same as core.

## Occlusion audit

- `tools/occlusion_audit.py` on the edition dir: **0 flags**. Selftest first: planted classes fired {BOXTITLE: 1, COVER: 1, EDGE: 1, FOOTER: 1, LINEX: 1, TEXTX: 1}; clean controls silent. Log at `hidden_files/w47/scratch-fanout-ko3/zh-tw/occlusion-zh-tw.log` (json `occlusion-zh-tw.json`).

## Mechanical gates (final state, run 1)

- `run.py` (build run 1, `/usr/bin/python3`): exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150 (A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; P2-feature ends 1531, P8-keys ends 2351, P7 teaser 2425.7). Log `hidden_files/w47/scratch-fanout-ko3/zh-tw/build-zh-tw-run1.log`; SVG hashes `zh-tw/sha-zh-tw-run1.txt`.
- `tools/freeze.py baseline` (**BLOCKED** — see Adjudicated): the runtime guard (added 2026-11-11 12:00) aborts under `/usr/bin/python3` (rc=2, log `zh-tw/freeze-zh-tw.log`); under the venv it gives 0/8 (log `zh-tw/freeze-zh-tw-venv.log`, build-copy deleted). No 8/8 baseline exists for this edition until the coordinator resolves the interpreter conflict. The 8 editions built before 12:00 froze 8/8 under `/usr/bin/python3`.
- `tools/freeze.py diff` (core-ko svg vs edition svg, run under the venv — diff is a pure text comparison, interpreter-independent): TOTAL added CJK characters **822** (see Adjudicated). Log `zh-tw/freeze-diff-zh-tw.log` (+ json `zh-tw/freeze-diff-zh-tw.json`, verification `zh-tw/verify-freeze-diff-zh-tw.py`).
- `tools/p8.py extract` on `svg/p8-siheom.svg`: **noted set = 150 of 150** (parse: lines). Log `zh-tw/p8-extract-zh-tw.log`, json `zh-tw/p8-zh-tw.json`. `compare` vs core P8: **CLEAN** (missing=[] extra_count=0 keydiff=[138]). Log `zh-tw/p8-compare-zh-tw.log`.
- `check_core.py` / `check_gloss.py` (scratch copies with ED + gloss prefix patched to the edition): **gloss fails 0, orphan issues 0**, phrases 8/8 verbatim (incl. the new phrase #7 with (1면)); dates all correct. Log `zh-tw/check-zh-tw.log`.
- Text layers: print and web PDFs each extract to **49,645 bytes, byte-identical** (`cmp` rc 0). Extracts `zh-tw/print-zh-tw.txt`, `zh-tw/web-zh-tw.txt`; empty diff `zh-tw/textlayer-diff-zh-tw.txt`.
- P8 min font 9.975pt (PyMuPDF on the print PDF, P8 answers region y≥1302/2700: 163 spans, 158 at 9.975pt), ≥ 9.75pt. Log `zh-tw/p8font-zh-tw.log`.
- 150-key check (`keycheck-ko.py`, REG from edition sources vs keys extracted from P8 SVG): 149 exact + #150 `✓` (expected) = **150/150**. Log `zh-tw/keycheck-zh-tw.log`; full table in `zh-tw/EDITION-RECORD.md`.
- §1.1 grep audit: paper `#fbfaf6` 1×/page (P4/P6 4×, same as core — colour also used in table cells), VOL.4 correct on all pages, VOL.5 0 except P7 (2, by design), `·` counts identical to core page-by-page and only in gloss/option/credit contexts, colour set identical to core page-by-page; hanzi set-checked (1,162 CJK chars on P8, all in the edition's source literals — no stray CJK). Log `zh-tw/style11-zh-tw.log`.
- Census (`census.py`, ex/match stems + D6 segments vs text.md): ex/match 166 items, 0 missing; D6 0 missing. Log `zh-tw/census-zh-tw.log`.
- Visual read: all 8 print pages at 100dpi, zero issues. PNGs in `hidden_files/w47/scratch-fanout-ko3/zh-tw/pages/`.

## Output files + sizes (final render, run 1)

- Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ko-zh-tw/`
- Print PDF: `Lucerna-VOL4-KO-ZH-TW.pdf` — **45,219,886 bytes**, 8 pages, SHA-256 `65118aabee9f7494c50071139ea74dbff6e16f00c2c0f357902564ac06402936` (fix rebuild 2026-11-12; D5 value was 45,215,288 bytes / `17c39f4f4887…`)
- Web PDF: `Lucerna-VOL4-KO-ZH-TW-web.pdf` — **4,323,857 bytes** (< 7 MB), 8 pages, SHA-256 `189fde45fc9e7b747611f4beb0285db17ce34f77aefff372bf16e868b82110f1` (fix rebuild 2026-11-12; D5 value was 4,314,413 bytes / `fe0220266520…`); pdftotext **49,681 bytes, byte-identical to the print PDF**.
- Text export: `2026-w47-ko-zh-tw.text.md` — 35,487 bytes, 8 pages, 464 items, SHA-256 `841a26658cb7dcff9d3489e95caedd5558165a73efc9e37bbb262c75693b0203` (exported from source via the fixed `textmd.py` (md5 `00d8f52d96ecad396cbc03603d98fa9b`), never from PDF; re-exported 2026-11-12 (fix round 2, R2-1: textmd.py dedup fix, 8 items restored, 456→464 items)).
- `ABSTRACT.txt`: 268 bytes, SHA-256 `88f967a1267da0e6b6b352582fea454de11a31ce171b5a46c0d67311b34d7767`. `Lucerna韓語週報VOL.4：韓國高考倒數D-3、11月19日考試、11月22日泡菜日泡菜成本199,456韓元、三星時隔12年奪韓國大賽冠軍、韓史檢定報名與晚秋紅葉——韓文正文、繁體中文講解，A2至B2分級，150道練習題。`
- `WEEKLY-KIT.md`: this file. Build records: `hidden_files/w47/scratch-fanout-ko3/zh-tw/EDITION-RECORD.md`.

## Open verification debts (carried to the parent line)

- Independent proofread of this edition not yet done — to be assigned by the coordinator (proof1, separate person from the builder).
- ~~Freeze baseline blocked by the tools/freeze.py runtime guard (added 2026-11-11 12:00)~~ — RESOLVED 2026-11-12 by the D5 rebuild: freeze ran under the coordinator-approved one-off system-python3 exception (see D5 section below); `baseline` 7/8 with the P1 display-"1" interpreter artefact adjudicated, `diff` vs base-venv added CJK 0.
- Fact debts inherited from core-ko (see core KIT): no observed Naejangsan/Wolchulsan foliage peak announced at Nov 10 press time; HanNeungGeom details (other than date/time/fee) from secondaries; K League 35R scores not verified — not cited; WiKim Festival 2026 time/theme/session not found in an independent source (printed as scheduled).

## D5 rebuild (2026-11-12, SOP §1.1)

- Template: `mechanism/svglib-ko-d5.py` installed as edition `svglib.py` (`_D5_READER = "cjk"`, reader zh-tw; diff vs template: 1 line, `_D5_READER` only). Old svglib kept as `svglib.pre-d5` in the edition dir and in `hidden_files/w47/scratch-d5-ko/2026-w47-ko-zh-tw/pre/`.
- Build: `tools/venv/bin/python` throughout. `run.py` TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE. Base-venv control (old svglib + venv) TOTAL 150 with the known P2 FLOW OVERFLOW warning (core content, also present pre-D5).
- Gates (all in `hidden_files/w47/scratch-d5-ko/2026-w47-ko-zh-tw/`): D5 census PASS (Latin 0 / Cyrillic 0 / curly-in-CJK 0; production baseline was 210 Latin); `census_quotes.py` 0 defective glyphs; `head_check.py` PASS 0 defects; `occlusion_audit.py` 0 flags; `p8.py extract` 150/150, `compare` vs core-ko CLEAN (keydiff=[138], expected reader-language key); `spill_sweep.py` 0 SPILL (335 OBSERVE); `boxtitle_check.py` 0 DEFECT (63 titles, 1030 body lines); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` 0 absolute defects (ratios n=385 median 1.007 boldT 1.040 boldF 1.000; P8 206→205 lines, slack 78.1→78.1px); text layer print/web char-multiset diff 0 (18,114 = 18,114, pdftotext 49,577 bytes byte-identical).
- `freeze.py` (system python3 Pillow 10.2.0, coordinator-approved one-off exception): `diff` patched vs base-venv RC=0, added CJK 0 (Latin strings +450 from run splitting, expected). `baseline` 7/8 (P2–P8 OK; P1 differs): adjudicated interpreter artefact, same as core-ko — P1 text multiset identical (0 diff, verified by direct SVG text comparison, 1126 runs each); only the big display "1" (185 vs 183pt) + knock-on x shifts (31 elements, 0 text-content diffs). Production (venv, canonical) is self-consistent.
- No content files changed. No true D5 defects in this edition.
