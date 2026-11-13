# PROOF-NOTE — 2026-W47 ko-ja (proof1, independent)

- **Edition:** `2026-w47-ko-ja` (target ko, reader Japanese), builder fan-out #3 run 2.
- **Proofer:** independent (proof1). Work dir: `hidden_files/w47/scratch-proof-ko-ja/` (goals side only; nothing written to the repo except the git probe object — see below).
- **Date:** 2026-11-11. All gates re-run fresh by this proofer; builder logs were used only as claims to check, never as evidence.

## Verdict: (a) 定稿零缺陷

No defect found. No fix is routed. The two run-2 carry-forward fixes are verified landed, the freeze-diff adjudication is independently re-computed at 0 unexplained, and every gate passes (including the freeze baseline, which the builder's report listed as BLOCKED — the block is resolved, see §3).

## 1. SHA verification (three files + core, before and after)

| File | Bytes | SHA-256 | Result |
|---|---|---|---|
| `Lucerna-VOL4-KO-JA.pdf` (print) | 51,357,740 | `7bc95f9748e2d07ec16bd3d19e678e3525f1959dc653a9a4a18059ee2cae2d4c` | matches brief ✓ |
| `Lucerna-VOL4-KO-JA-web.pdf` (web) | 4,388,239 | `9f0567aa3357528ae0e89e682beef7481d02e679965416c5c82bac5316a8a9c0` | matches brief ✓ (< 7 MB) |
| `2026-w47-ko-ja.text.md` | 35,425 | `635ec8afac75dc7859cb362dcf9f3470dfb083a67858790a15006cfa3afd9e97` | matches brief ✓ (450 items) |
| `ABSTRACT.txt` | 342 | `4a9445de3848203250f4d4992a79fb08992dada8cd0f747e2b745746f453157a` | matches builder record ✓ |

Core-ko, measured before proof and again after proof (identical both times, = fan-out baseline):
print `53bf14edeca05f9db56e699b5d826f50c320eebcce200c4b876b394de21a2f27` (46,232,227 B),
web `9592945ae188dc8e50394fcab1ded155baaff63161bcf0b5f7ecbc6898c43bc7` (4,232,878 B),
text.md `da1d3a323f7c83eb95fe989e59f56ca6a706282c443f20cc5792c3f73468181a` (34,606 B).
**Core unchanged by this proof.**

Note: the opening git probe (`echo test | git hash-object -w --stdin`) wrote one probe object into the repo object store (`9daeafb9…`); no file, branch, commit or push was made.

## 2. Carry-forward re-tests (fan-out #3 run-2 fixes)

### P3 box title — FIXED, verified
- Source: `content34.py:32` — `김치의 날에 알아 둘 것　知っておく` (shortened from `知っておくこと`).
- Re-measured with the edition's own `svglib.text_w` (system python3, PIL 10.2.0): **347.4 px** ≤ 386.5 px budget (was 393.4 px OVER in run 1). **Minimum boxtitle margin in the edition is this title: 39.1 px.**
- Rendered P3 (print PDF, 100 dpi) shows the title on one line inside its cream box. boxtitle gate: **8/8**.

### P8 #81 wrapped note — FIXED, verified
- Source: `content56.py:101` — note shortened to `聴解中は飛行機が飛ばない` (12 chars; old `リスニングの時間は飛行機が飛ばない` is absent from all 8 SVGs).
- The P8 SVG carries the full answer as **one** `<text>` element:
  `81. 비행기는 듣기 시간에 뜨지 않아요. — 聴解中は飛行機が飛ばない`.
- Re-measured (serif 13.3 px, the P8 answer face): **397.4 px** (builder: 397.6 px; 0.2 px method rounding). Old line re-measures 463.4 px, past the wrap threshold. Widest fitting answer line in the edition is 420.1 px, so the margin is ~22.7 px.
- `p8.py compare` vs core: **CLEAN**, missing=[] extra=0, keydiff=[137, 138] (translation items only, see §4).
- P5 SVG does **not** contain the note (notes print only on P8) — the #81 fix touched P8 only.

### Freeze diff +2901 CJK — adjudication independently re-computed
- `freeze.py diff` re-run under system python3: per-page added CJK **122 / 257 / 204 / 154 / 211 / 121 / 345 / 1487 = 2901 total**; added/removed strings +17/−17, +35/−34, +28/−27, +22/−22, +32/−31, +16/−15, +38/−38, +167/−167 — all identical to the builder's diff.
- Independent adjudicator written fresh for this proof (`verify-freeze-diff-proof.py`, different implementation from the builder's `verify-freeze-diff4.py`; corpus = edition content literals + `map-ja.json` (216 keys + 8 instr) + generated structural strings + answer-line composites):
  **added unexplained 0 / 307, removed unexplained 0 / 303.**
- One string initially flagged by my verifier (`150. ✓ 范文见本版 H 区（169字）`) was my verifier's own template-rendering bug (JoinedStr `{NCHARS}` not rendered); fixed, traced to core `content8.py:111` f-string `范文见本版 H 区（{NCHARS}字）`, NCHARS=169. Re-run: 0/0.
- **The +2901裁决 stands: 0 未解释.**

## 3. Freeze baseline — BLOCKED status RESOLVED (new evidence since the builder's report)

- `tools/freeze.py` in the working tree now carries the per-family runtime guard **with the ko exemption** (uncommitted modification, `M tools/freeze.py`; `git log` shows only `8df40906` for the file). ko-family paths REQUIRE Pillow 10; all other paths REQUIRE Pillow 13.
- Baseline re-run under **/usr/bin/python3 (Pillow 10.2.0 / FreeType 2.13.2)**: **8/8 SVGs byte-identical** (`freeze-base.log`), core SVGs re-hashed unchanged. My separate `run.py` re-run in a scratch copy also regenerated all 8 SVGs byte-identical to the shipped ones.
- Control re-run under **tools/venv (Pillow 13.0.0)**: **ABORT rc=2**, as designed for the ko family ("a venv freeze of a ko edition is 0/8 by construction"). This is the expected control, not a failure.
- Consequence: ko-ja now holds a full 8/8 baseline; the builder's §5 block no longer applies. The coordinator decision the builder asked for is effectively answered by the guard change already in the tree (revert-vs-venv question is moot for ko: the guard itself now encodes the system-python3 stack).

## 4. Gate summary (all independently re-run; details in GATE-LOG.md)

| Gate | Result |
|---|---|
| run.py (scratch copy, system python3) | rc=0, **0 FLOW OVERFLOW / HEAD TOO WIDE**, TOTAL 150 (A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38); P2-feature ends 1531, P8-keys ends 2351, P7 teaser 2454.7; regenerated 8 SVGs byte-identical to shipped |
| freeze baseline (system python3) | **8/8** (see §3) |
| freeze baseline (venv, control) | ABORT rc=2, as designed |
| freeze diff | +2901 CJK, 307 added / 303 removed strings, **0 unexplained** |
| occlusion audit (system AND venv) | **0 flags** both stacks; selftest all 6 classes fired |
| p8.py extract | 150/150 noted |
| p8.py compare vs core | **CLEAN**, keydiff [137, 138] |
| keycheck (own SVG parse, independent of p8.py) | **150/150** (149 exact + #150 `✓`); my SVG keys agree 100% with p8.py's extraction |
| check_core / check_gloss (system python3) | rc=0; gloss fails 0; P7 phrases **8/8 verbatim**; orphan issues 0; dates verified (Nov 16 Mon / 18 Wed / 19 Thu / 22 Sun / 28 Sat; D-3/D-1/D-day arithmetic) |
| print/web text layers | **byte-identical** by two independent extractors (PyMuPDF and `pdftotext -layout`); 8 pages each |
| P8 min font (PyMuPDF, print PDF) | **9.975 pt** ≥ 9.75 pt; 158 spans at min; P8 stem 10.35 pt (recorded core adjudication) |
| boxtitle widths | **8/8** within 386.5 px; min margin 39.1 px (P3) |
| P8 #81 line | single line, 397.4 px (see §2) |
| creambox true-ink (own transform-aware checker, PIL getbbox) | **0 overflows** over 49 cream rects / 223 paired lines; worst clearance **+3.1 px** (P2 あなたは？ last line, inside) |
| isolated-punctuation sweep (8 SVGs + text.md, ja + core) | **0** lines starting with closing punct / ending with opening punct |
| U+2019 / curly sweep (8 SVGs + text.md) | **0** (U+2019 = 0, U+201C = 0, U+201D = 0) |
| §1.1 grep audit (canonical `style11-ko.py` re-run) | log **byte-identical** to builder's: paper/VOL.4/`·`/colours identical to core page-by-page; hanzi 62/133/100/76/116/66/154/825 (core 82/187/138/104/137/81/212/1122); CJK-reader stray check 276 chars, **0 stray**; P7 VOL.5 3→2 by design (removed `lko`/`lcn2` lines); U+2019 0 |
| text.md re-export (`textmd.py`, system python3) | reproduces shipped file **byte-for-byte (SHA identical)**; 450 items |
| census ex/match + D6 | 166 items, **0 missing**; D6 **0 missing** |
| text.md self-read (full read) | zero issues |
| 150 items, three-source hand verification | **150/150 OK** (see §5) |
| 8 pages rendered from print PDF at 100 dpi, visual read | **8/8, zero issues** |
| "next Sunday" freeze rule | **0 hits** in core-ko, ko-ja and `tools/tables.py` — no applicable object; rule not applied, not forced |
| D5 font (record only, not judged) | **0** Latin explanation-layer segments in Noto Sans CJK SC — the family renders in Noto Serif/Sans CJK **KR** throughout (873 / 611 spans); Latin-only spans: 278 Sans KR, 13 Serif KR, 1 UnifrakturMaguntia (masthead) |

## 5. 150-item three-source hand verification (150/150 OK)

Method: REG derived independently from AST of **core-ko** content files (S1) and **ko-ja** content files (S2: key, Japanese note, and the exercise sentence from the same `ex()` call / the full left/right option lists for `match_set`); **rendered P8 SVG** keys from my own column-aware parse (S3). Every row was read: key against its sentence/options, note against key and sentence, and SVG key against REG.

- core-vs-ja keys: only **3 diffs**, all legitimate translation items — #137 `11月22日是泡菜日。` → `11月22日はキムチの日。`, #138 `三星时隔12年夺冠。` → `サムスン12年ぶりの優勝。`, #150 open-task stem reworded. (Matches `p8.py compare` keydiff [137, 138].)
- ja-vs-SVG keys: **0 diffs**; SVG lines match REG for all 150, including #150 (`150. ✓ このページのHセクションの模範解答（169字）`).
- Spot-checked with sources: MC option letters verified against the printed options in every case (e.g. #89/#110 기상청 ~80% vs #33 산림청 50% — the two bodies are correctly distinguished); all four `match_set` groups verified against their option lists (#25–28, #43–46, #61–64, #141–144); all four 書き換え past-tense rewrites (#57–60); all four 文を作る word-order builds (#79–82, #133–136); all four 翻訳 items (#137–140) with their page citations verified in the P8 SVG (P2 / P4 / P5 / P8 section C — the 민준이 letter text is in P8 section C, `C　읽고 답하기`); #97/#99 正誤 keys verified against the statements (special measures only Nov 19; forecast ≠ observation); H model essay byte-identical to core (`MODELO`, NCHARS=169, `content8.py:99–109` in both).
- Japanese notes: read for every item; all accurately explain their keys. The #43/#123/#124 notes (Weatheri vs Forestry Service forecasts for 内蔵山) are core's own renderings, not typos.
- text.md drops vs core (452 → 450) are the two by-design removals (`lcn2`, `lko`); `すべて` is present in text.md line 119 (CJK passes `is_prose`).

## 6. Visual read (print PDF, 100 dpi, all 8 pages)

- P1: masthead, headline, drop cap, numbers box, practice, calendar, contents, word, short news, quiz, photo — clean.
- P2: articles, gloss boxes, shopping list, D-date cards, you-box, exercises A–D — clean; P2-feature ends 1531, inside the frame.
- P3: **fixed box title on one line inside its box**; photos, 단풍 달력, you-box, exercises A–D — clean.
- P4: playoff bracket (플레이오프 box correctly highlighted), photo, calendar box, exercises — clean. Bottom whitespace is core-inherited layout (exercises end early), not a defect.
- P5: articles, numbers box, photo, you-box, exercises A–D — clean; the あなたは？ Japanese para's last line sits inside its box (the +3.1 px creambox minimum, §4).
- P6: comparison table renders correctly (header row + cream rows, all cell text inside); D-day boxes; exercises A–D — clean.
- P7: Frame box uses the new core sentence (`수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요`) with 「」 quotes; 실수 병원, 今週のパターン, reader letter (VOL.5 handover note), 8 phrases with page citations (check_core 8/8 verbatim), photo, next-week band — clean.
- P8: exercises A–H incl. the H model essay (169字) and photo; the answers block prints all 150 lines as single lines across 4 columns, page separators `— 제N면 —`; **#81 is one line**; #150 prints as `✓` — clean.

## 7. Observations (not defects — no routing)

1. **Builder-record misstatement (record only, files unaffected):** EDITION-RECORD says "Only the P8 SVG changed between run 1 and run 2". The P3 SVG necessarily changed too: run 1 printed the title `…知っておくこと`, run 2 prints `…知っておく` (different strings → different SVG bytes). P5 did not change (the #81 note is not printed on P5 — verified by grep). The shipped files are correct; only that one sentence in the record is wrong. No run-1 SVG hashes were preserved, so a byte-level run-1→run-2 diff is impossible; the run-1→run-2 comparison rests on the run-1 logs (boxtitle 7/8, p8 compare SHORT [81]) plus the string-level proof above.
2. **Tightest true-ink margin:** +3.1 px, P2 あなたは？ box last line (`文書いて送ってください。`). Inside, passes; recorded so the next change to that box knows the headroom.
3. **Text-layer byte counts differ by extractor** (PyMuPDF 49,499 B; `pdftotext -layout` 95,759 B; builder's 53,212 B) — an extraction-mode artefact only; print == web under every method (identical SHA in each method). No action.
4. **My own first creambox pass was wrong and is corrected, not hidden:** v1 of `creambox-proof.py` treated PIL `getbbox` y as baseline-relative and flagged 18 lines; the canonical `occlusion_audit.py` code shows `getbbox` y is ascender-relative (`ink top = y − ascent + t`). After fixing, the same 223 lines measure 0 overflows with worst clearance +3.1 px. The v1 log was overwritten by the corrected run; the bug and the fix are recorded here.
5. Core-inherited content noted but not defected (core proof's scope): P1 `이번 주의 조치가 아니에요` phrasing; P3 closed-press-time wording on the unobserved Naejangsan peak (core fact debt); P6 table row label `10월 16일 가격`; P2 `평년보다도 13.4% 낮아요`. All byte-identical to core-ko; nothing in this edition changes them.

## 8. Deliverables

- This file: `PROOF-NOTE.md`
- `GATE-LOG.md` (same directory): every gate with command, log file and measured value.
- Evidence in the same directory: `freeze-diff-proof.json`, `verify-freeze-diff-proof.py/.log`, `freeze-base.log`, `freeze-base-venv.log`, `run-proof.log`, `checks-proof.log`, `occlusion-proof-*.log/.json`, `p8-*-proof.*`, `keycheck-proof.*`, `boxtitle-proof.log`, `creambox-proof.py/.log`, `creambox-adjudicate.log`, `sweeps-proof.py/.log`, `style11-proof.log`, `textlayer-proof.log`, `text-print-proof.txt`, `text-web-proof.txt`, `textmd-proof.md/.log`, `census-proof.log`, `items150-proof.json/.tsv/.log`, `p8-81.txt`, `pages/p1.png` … `pages/p8.png`, `work/ed/` (scratch rebuild copy).
- No commit, no push, no insert.py, no lint --write. freeze.py was read, never edited.
