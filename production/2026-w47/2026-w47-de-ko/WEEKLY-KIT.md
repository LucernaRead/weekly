# WEEKLY-KIT — 2026-W47 · German target, Korean reader

- Edition: `2026-w47-de-ko` — German target text, Korean explanations
- Week: Mon 2026-11-16 – Sun 2026-11-22 · VOL.4 · Press time: Mon 2026-11-09
- Lead story: **Die Bundesliga kehrt zurück — Bayern gegen Köln**
- Status: complete (rebuild-B), all gates green on the FIRST rebuild run, visual
  proofread 8/8 pages zero findings (rebuild-B build 1, 2026-11-11). Rebuild 2
  (2026-11-11 07:23 UTC) also passed all gates; this rebuild only carries the
  core build15 Q34 stem correction (see §6). Fix1 rebuild (2026-11-11, D1
  toolbox-pad fix only, all gates green again; independent proof2 pending —
  coordinator to assign). New standing gates (2026-11-12) found 1 boxtitle
  defect (P1 Fragen subtitle +6.5px); fix2 rebuild (2026-11-12) repaired it
  by layout only, all gates green again.
- **D5 font rebuild applied 2026-11-12 (all gates green — see §3b/§6)**

## §1 Contents

8 pages, 1950×2700, 4 columns. **150 exercises**, continuous numbering 1–150, all in the registry.
Chips: 141 total (P1 10, P2 15, P3 18, P4 15, P5 18, P6 18, P7 12, P8 35; P8 A2 22 / B1 13 / B2 0).

## §2 Deliverables (fix-de-round3 rebuild, 2026-11-13; F3 Haushalt fix rebuild superseded)

- Print PDF: `Die-Lucerna-VOL4-de-ko.pdf` — 12925712 B, sha256 `013b5d8e255e71728e74152790bf54a99591caa3d32ab1fc490e8e1202be7865`
- Web PDF: `Die-Lucerna-VOL4-de-ko-web.pdf` — 1789538 B, sha256 `ef851f6fa7d626a033b8dad4363272a78e0a4182c466be26b70cc16506ae33cc` (52,472 text bytes; < 7 MB)
- Text export: `2026-w47-de-ko.text.md` — 51730 B (43,602 chars, 591 entries, 150 exercises), sha256 `a8804776b2863a48b4ec09b1864ea074a3ddb7a9d61b39a3273fdcfdb83eb475` (changed — see the fix-de-minor1 and fix-de-round3 entries below)
- ABSTRACT.txt: Korean, one line, no ASCII double quotes
- 8 SVGs in `svg/`; all gates green (D5 round, see §3b)

Print PDF is 12.9 MB (was 15.9 MB): D5 moved the Latin explanation layer out of the CJK faces, so far fewer CJK glyph subsets are embedded. No gate checks print size; web PDF is the size-checked one.
- ABSTRACT.txt: 388 B, Korean, one line, no ASCII double quotes
- 8 SVGs in `svg/`; all gates green via `build_edition.py` (rebuild 2 log: `ko/rebuild2.log`)

Print PDF is 15.9 MB: genuine Korean CJK font subsets (fewer unique glyphs than Japanese, more than Cyrillic). No gate checks print size; web PDF is the size-checked one.

## §3 Gates (rebuild-B build 1)

- run.py exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150
- measure 24/24 PASS (ko/measure3.log)
- verify TOTAL 150, numbering continuous, SVGs byte-identical after re-run, §1.1 audit True, verbatim OK, P8 floor True, 17 forbidden terms absent
- occlusion 0 flags
- p8 extract 150/150, compare CLEAN, keydiff [137, 138, 139, 150] (expected: the three translate-to-Korean items + Q150)
- freeze (tools/freeze.py, venv interpreter): exit 0, TOTAL added CJK 3,096 — the Korean explanation layer itself (see §5)
- freeze_direct source level PASS (0 unaccounted removed/added); rendered 8/8 (frozen 149/163/201/166/179/175/160/185; sha8 73347f49 / 689045ad / 8b2e9eba / df1bebf7 / e7b235f9 / 2bbe05f9 / 591dc064 / f6dd4a15 — only P3 moved vs rebuild 2's 14aaccaf)
- print/web text layer identical (default word multiset: print 52,318 B / web 52,318 B; -raw normalised: 51,151 B both)
- P8 min font 9.94pt (≥ 9.75pt floor)
- U+2019 full scan over 8 SVGs = 0
- Box titles: 8 instances, all end ≤ 1862.0 (max 1857.3)
- keycheck 148/150: Q150 PREFIX (expected, as all editions) + Q139 space-join artifact (see §6) — both verified in the P8 SVG as correct rendering, not content defects
- Visual proofread: all 8 pages rendered at 100 dpi and viewed, zero findings

## §3b Gates (D5 font rebuild round, 2026-11-12 — full re-run on the rebuilt edition; scratch `hidden_files/w47/scratch-d5-de/de-ko/`)

- D5 mechanism: `apply_variant.py --svglib … --target de --reader ko` (mode cjk) on the edition's `svglib.py`; fix2 curly-quote routing installed with it (routing assert `ROUTING FAILURES: 0`, adapted for cjk: `_D5_READER == "cjk"`, Latin sans → news — latin/cjk share routing per CJK-DECISION §1). Install note: `CJK index SC -> KR` (the installer rewrote the CJK subfont SC→KR this time — production still carried the SC index; de-ja was already JP). Pre-D5 `svglib.py` backed up as `svglib.py.pre-d5`. Pre-D5 baseline verified CLEAN before install: the production dir was copied to scratch and rebuilt with the venv interpreter — freeze baseline **8/8 SVGs byte-identical** to the delivered SVGs (`freeze-pre-baseline.log`). Pre-D5 production snapshot in `scratch-d5-de/de-ko/baseline/` (SVGs + sources, fix2 state). KIT wave 2 check: pre-D5 print AND web SHAs both match the KIT (`5e34f31a…` / `d77adb82…`) — the second edition (after de-es) with no web-SHA drift. The D5 values above are measured from the actual files on disk.
- Pre-D5 D5 census: **463 Latin-in-CJK-Sans elements** (matches D5-CENSUS-130); quotes defective 0; p8 extract 150/150.
- `run.py` (run2): TOTAL **150**, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`tools/head_check.py`: PASS 0 defects).
- `mechanism/d5_census.py`: **PASS — D5 Latin 0, D5 Cyrillic 0, curly-in-CJK 0**.
- `tools/occlusion_audit.py`: **0 flags** (selftest OK; fixed tool — bare `Noto Sans` runs measured on the non-CJK face, brief §10).
- `tools/p8.py`: extract 150/150; compare vs rebuilt core-de P8: `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]` — the same 4 expected reader-language items as rebuild-B.
- `tools/freeze.py`: baseline **8/8 SVGs byte-identical** (venv Pillow 13.0.0 / FreeType 2.14.3); diff pre-D5 baseline vs rebuilt: **added CJK characters 0** (added Latin strings 463 = D5 run-splitting). Note: the brief's warned ko freeze ABORT under venv (Pillow 10 requirement) did NOT trigger for this edition — both freeze baseline and freeze diff ran clean under the venv; the system-python3 exception was not needed.
- `tools/spill_sweep.py`: 32 boxes, 144 candidates, **0 SPILL**, 144 OBSERVE.
- `tools/boxtitle_check.py`: 65 titles, 469 body lines, **0 DEFECT**, 0 OBSERVE, 0 marginal (real backup comparison: `scratch-d5-de/scratch-fanout-de/backup/2026-w47-de-ko`). Coverage note: two fixed titles sit below the tool's 22pt detection floor (P3 `크리스마스` 21pt, P7 `도구 상자` 21pt) — they are verified instead by the creambox audit (0 defects across all 32 boxes) and by direct ink measurement (spare 19.2px / 14.7px).
- `tools/pdf_edge_scan.py`: 8 pages, **0 TOUCH, 0 NEAR**.
- `tools/d5_creambox_audit.py` (pre-D5 baseline vs rebuilt): **PASS 0 defects**; ratios n=526, median 1.009, bold 1.049 / regular 0.987; P8 lines 232→233, footer slack 34.6→34.6px.
- Web/print text layer: `pdftotext` default mode — both **52,246 bytes**, word multiset identical, normalised text exactly identical; `-raw` mode — both 51,160 bytes, identical.

## §4 Language

- Reader: Korean (한국어). ED_SPACING 7.0, NOTE_WRAP "full", KEYS_HALF=false.
- TYPEMAP: 完成句子→빈칸 채우기 / 单选→선택 문제 / 句型转换→바꾸어 쓰기 / 词汇配对→짝 맞추기 / 判断对错→맞다/틀리다 / 完形填空→빈칸 글 / 造句→문장 만들기 / 对话补全→대화 완성 / 翻译→번역 / 写作→쓰기
- Gloss prefix: `주 — ` · Page line: `{n} / {total}쪽` · P8SEP: `— {pg}쪽 —`
- Edition line: `독일어 주간　VOL.4　분데스리가 복귀　조용한 한 주`
- Footer: `Die Lucerna　독일어 주간 VOL.4　독일어 텍스트　한국어 설명`
- Chart labels: ['축구', '시장', '조용한 날']
- Place names: 쾰른, 마인츠, 뉘른베르크, 프라이부르크, 라이프치히, 함부르크, 글라트바흐, 브레멘, 샬케, 슈투트가르트, 작센주, 바이에른, 네덜란드
- ABSTRACT.txt (Korean): "Die Lucerna 독일어 주간 VOL.4: 분데스리가 복귀(바이에른은 홈에서 쾰른을 맞이합니다), 네덜란드와의 네이션스리그 결전, 참회와 기도의 날과 죽은 자의 주일, 쾰른 크리스마스 시장 개장, 11월 3~8일 유럽 대항전과 분데스리가 결과. 독일어 텍스트, 한국어 설명, A2~B2 수준, 이번 주 화제의 150문제."

## §5 Freeze / CJK handling (read before claiming --strict-cjk)

- `freeze.py diff --strict-cjk` does NOT pass for this edition, by design: the reader-language explanation layer itself adds CJK (3,096 chars, Hangul). The en-family precedent (en-ja: 2,092) is to record the total and audit the added characters instead.
- Residual audit: freeze_direct source level PASS with 0 unaccounted literals — every removed core literal is accounted for by a translation (source level is the strict check here; ko values are pure Hangul + Latin, no hanja, so the old strict step-12 scan passes as-is). Rendered level 8/8 PASS.
- Interpreter: `tools/venv/bin/python` (PIL 13.0.0) for build and freeze, as required (system python3 PIL 10.2.0 measures 1.1% differently).

## §6 Build history (2 rounds)

- **Build 1** (2026-11-11 ~07:17–07:21 UTC): FAILED 2 gates — occlusion only, exactly 1 real flag: [TEXTX] p1-front.svg, Q6 'Der erste Advent ist am ___.' overlapped 'DIE WOCHE IN ZAHLEN　숫자로 보는 한 주' by 12.8x5.6px (the other 4 flag classes in the log are the selftest's planted classes, not real flags). Root cause: ZAHLEN head 464.6px at 24pt bold sans (box inner width 378.5px). Fix: → 'DIE WOCHE IN ZAHLEN　숫자' (334.1px, same bare-noun pattern as ja's '数字' 337.9px). Word-of-week '대림절 달력(24개의 작은 문). 5쪽 참조.' was already 1 line (316.5px) — untouched. p8 compare was already CLEAN in build 1 (ko's Q150 dash survives the wrap — Hangul metrics differ from Japanese).
- **Build 2** (2026-11-11 ~07:22–07:23 UTC): ALL GATES PASS. One-value fix (vals_ko.json nested v['values'] addressing; gen_tr diff exactly 1 line; boxtitle 7/7; transform-ko3.log RC 0; measure3 24/24).
- **Rebuild-B build 1** (2026-11-11 ~08:52 UTC): ALL GATES PASS first run. Core-de build15 corrected the P3 Q34 stem to the singular form matching key `Weihnachtsmarkt` (D-01, resolved at the core). Edition deleted and re-transformed from the new core with unchanged `tr_ko.py` / `vals_ko.json`; no fixes needed, visual proofread 8/8 zero findings (renders /tmp/ko-rb-proof-*.png). Flow ends identical to rebuild 2 (spare 165px); only delta is that one stem string (P3 sha8 14aaccaf → 8b2e9eba; print 15,906,995 → 15,907,001 B, text 51,499 → 51,498 B). Web PDF grew 1,867,491 → 1,906,546 B because this run's webpdf embedded an extra `LucernaNewsreader-Bold` subset (21,596 B): webpdf.py runs `fc-cache -f` on every invocation and the `Newsreader:weight=200` resolution flips between Regular and SemiBold across cache regenerations — a tool nondeterminism, not a content defect (text layer byte-identical to print, still < 7 MB).
- keycheck 148/150, both mismatches verified as extractor join artifacts, not content defects:
  - Q139: extracted '대림절 달력을만들고 있습니다.' vs REG '대림절 달력을 만들고 있습니다.' — the P8 SVG shows '대림절 달력을' ending line 1 (y=2250.14) and '만들고 있습니다.' starting line 2 (y=2265.775); join2() glues Hangul across the line break without a space (same class as ja's Q150 dash issue). Rendering is correct.
  - Q150: extracted '자유과제' vs REG '자유 과제 — 쓰기 상자의 항목을 따르세요' — same space-join artifact ('자유' ends line 1 at y=2359.585, '과제 — …' starts line 2 at y=2375.22) plus the expected PREFIX truncation. Q150's note '（나열된 항목으로 채점）' IS retained and renders (unlike ja, where the note had to be removed).
- Transform history: transform 1 failed with a SyntaxError — the writing-task prompt value contained ASCII double quotes around the title, terminating the double-quoted Python string. Fix: `『11월의 나의 한 주』` (Korean title brackets). A scan of all 8 vals files confirmed it was the only content value with an ASCII `"`. Transform 2 OK, transform 3 (ZAHLEN fix) OK.
- **Fix1 rebuild (2026-11-11 — D1 only):** P7 DER WERKZEUGKASTEN cream box too short
  (family defect from de-es proof1, reproduced on ko pre-fix): box bottom 754.0, last
  entry `Es ist fraglich, ob ... = 아직 미정` baseline 754.8 (clearance −0.8), `fraglich`
  descender ink ~4.7 below the box. Root cause (measured per-edition): the `tbh`
  formula in `content7.py:76` counts `n*29.5+6` per entry but the real advance is
  `20.5 + n*29.11 + 6` (`Page.para` first-baseline offset, 6 entries = +123 missed); ko
  wraps Σlines=8, so clearance = pad − 90.8 and pad 90 gave −0.8. Fix (edition-local,
  `content7.py:76` only): pad 90 → 110 (core-de value), comment rewritten with the
  arithmetic. Verified: toolbox bottom 754.0 → **774.0**, clearance **+19.2**;
  LESERBRIEFE y 770 → 790 (+10.4 unchanged); NOCH EIN WORT ends 1488.5 → **1508.5**
  (+42.9 unchanged, far before the 1548 Sätze rule). 300 dpi toolbox zoom confirms the
  last entry fully inside the cream box; print/web toolbox zooms pixel-identical. No
  text changed: text.md byte-identical (sha fd2dbd04…); freeze_direct 8/8 rendered with
  source PASS (0 unaccounted) and all 8 page shas identical to rebuild-B (73347f49 /
  689045ad / 8b2e9eba / df1bebf7 / e7b235f9 / 2bbe05f9 / 591dc064 / f6dd4a15). New
  deliverables: print 15,907,006 B (+5 B) sha
  `1ee2229f5e0d9803d9b32e9c048027a1bced2783bacac9ed72a83499cd866bcc`; web 1,909,587 B
  (+3,041 B — the Bold subset was already embedded in the rebuild-B web PDF; < 7 MB,
  text layer identical to print) sha
  `9a0699420966ff7354c3e11d078a2e46ecde8ff35badab03f2be7f8722fe6776`; text.md 51,498 B
  sha fd2dbd04… (unchanged). All gates green (occlusion 0 flags real run, p8 CLEAN
  keydiff [137,138,139,150], freeze diff +3,096 CJK — the Korean explanation layer
  itself, keycheck 148/150 — Q139 + Q150 extractor join artifacts, both pre-existing
  and documented in §6, unchanged from rebuild-B, boxtitle 7/7, d2scan 72 pairs 0 web
  gaps >0.5pt, P8 min 9.94pt, chips 141, verify TOTAL 150, bent quotes U+201C 33 /
  U+201D 0, Q34 new stem 1x in all five places). Gate logs in
  `hidden_files/w47/scratch-fix-de-toolbox-family/gates-ko/`; build logs in
  `hidden_files/w47/scratch-fanout-de/ko/`.
- **Fix2 rebuild (2026-11-12 — boxtitle gate fix, P1 only):** new standing
  gate `tools/boxtitle_check.py` (130-wide run) found the P1 Fragen subtitle
  `이번 주의 다섯 가지 질문　Die Fragen der Woche` running past its cream box
  by **+6.5px** (core-de fits at −22.0px). Fix (edition-local,
  `content12.py:69` only): subtitle font size 19 → 18 (layout only, no text
  changed); ink end 1868.5 → **1846.5**, margin **+15.5px**. New deliverables:
  print 15,907,007 B (+1 B) sha
  `5e34f31a4922a35902ffd3decebb9ba92d81387c4e1042244799630de1707114`; web
  1,909,583 B (−4 B) sha
  `d77adb822d976cceab204f45fe8e8e66dc98ada4783de4f21820646518a1c704`; text.md
  51,498 B sha fd2dbd04… (unchanged). All gates green on the rebuilt edition:
  boxtitle **0 DEFECT / 0 OBSERVE / 0 marginal** (also 0 on the synced
  production files), verify TOTAL 150 + SVGs byte-identical after re-run,
  occlusion 0 flags, p8 extract 150/150 + compare CLEAN keydiff
  [137,138,139,150], freeze `diff` exit 0 (added CJK 3,096 — the Korean
  explanation layer itself) + freeze-direct rendered **8/8** with all 8 frozen
  SHAs identical to fix1 (73347f49 / 689045ad / 8b2e9eba / df1bebf7 / e7b235f9 /
  2bbe05f9 / 591dc064 / f6dd4a15). NOTE (pre-existing, not this fix):
  freeze-direct *source* level now reports 1 unaccounted removed literal
  (`'sans'` ×2 in `svglib.py`) — core-de's `svglib.py` was patched (fix2 U+201C
  routing, 2026-11-11 22:35) after ko was copied from it, so the edition's
  `svglib.py` is the older copy; at fix1 time the source level PASSED (0
  unaccounted). This fix changed one int + one comment, no string literal.
  Gate outputs in `scratch-gatefix-de-en/2026-w47-de-ko/` (FIX-LOG.md).
- Flow ends (rebuild 2): P1-headline 1503, P1-fussball 2264, P1-quiz 2523, P2-feature 993, P2-ex 2332, P3-main 886, P3-ex 2333, P4-main 647, P4-ex 2315, P5-main 996, P5-ex 2441 (= core), P6-main 747, P6-ex 2523, P7-A2 1278 / B1 1310 / B2 1306, P8-battery 1409, P8-keys 2395 (bottom 2560, spare 165px).
- **D5 font rebuild (2026-11-12)** — **Cause**: explanation-layer Latin rendered in Noto Sans CJK SC instead of Newsreader (SOP §1.1 font table; CJK-DECISION §1: script-based routing, Latin → Newsreader, no `_READER_LANG` gate). Pre-D5 census: 463 Latin-in-CJK-Sans elements. **Fix (mechanism)**: `apply_variant.py` installed the D5 `_char_font` sans routing on the edition's `svglib.py` with `_D5_READER = "cjk"` (fix2 included; installer also rewrote the CJK subfont SC→KR). No German text, fact, or key changed; no wording changed at all. **Four D5-caused defects, all fixed in source and rebuilt**: (1) P1-fussball head `EINE WOCHE, ZWEI STIMMUNGEN` — HEAD TOO WIDE at 25pt; `content12.py:124` 25→22pt (411.8px fits the 422.5px column). (2) P1 sommaire title `IN DIESER AUSGABE　이번 호 내용` — +9.0px; `content12.py:89` 24→22pt (375.5px fits 400.5). (3) P3 vocab-box title `WEIHNACHTSWÖRTER　크리스마스` — +34.9px, the widest CJK title overrun in the de family; `content34.py:58` 24→21pt (381.3px fits 400.5; 22pt leaves only 1.0px spare). (4) P7 toolbox title `DER WERKZEUGKASTEN　도구 상자` — +21.7px; `content7.py:79` 23→21pt (385.8px fits 400.5; 22pt still overflows by 3.7px). **Verification**: full gate re-run (§3b) — census 0, occlusion 0, p8 CLEAN, freeze 8/8, added CJK 0, spill 0, boxtitle 0 (real backup), edge 0, creambox PASS, print/web text layers identical in both modes. The ko freeze ABORT warned in the brief did not trigger (venv Pillow 13 ran both freeze steps clean). The P1 masthead subtitle never collided with the headline in this edition; no P8 battery head overflowed.
- **Reproof fix rebuild (2026-11-12)** — **Cause**: independent reproof of the D5 rebuild found 9 items (F7 major, rest minor) — see `hidden_files/w47/scratch-reproof-w47-de/PROOF-NOTE.md`. **Fix (in source, then rebuilt)**: F1 — P5 UND SIE prompt gained the advent-calendar question; F5 — P1 DIE WOCHE IN ZAHLEN box regained the three German sentences (+ reader gloss). Gates: build ALL GATES PASS; boxtitle 0 DEFECT; spill 0 SPILL; edge 0/0; census-patched PASS (P5 cjk_sans +2 = the longer F1 prompt's run split, verified); head_check PASS; text.md dry-run diff 4 lines, 0 dropped. **Verification**: full gate re-run (logs in `hidden_files/w47/scratch-fix-de/logs/`); per-edition entry in `scratch-fix-de/FIX-LOG.md`. New deliverables: print 12,926,530 B sha `be2444232568…`; web 1,791,578 B sha `49223ed15613…`; text.md 51,701 B sha `0d17881f6154…`.

- **F3 Haushalt fix rebuild (2026-11-13)** — **Cause**: de-family independent reproof (worker 4c143a3c, F3 medium) — P6 `der Haushalt` mistranslated as household budget (`가계`): the article is about the federal budget Bundeshaushalt 2027 ("11 月 27 日表决"); the other 8 editions all say budget, and this edition's own Q92 answer already says `2027년 예산`. **Fix (in source, `content56.py` only, 3 visible places)**: band head `조용한 한 주와 가계` → `조용한 한 주와 예산`; gloss `der Haushalt = 가계` → `der Haushalt = 예산`; debate sentence `가계: 전기세가 얼마나 내릴지는 아직 미정입니다` → `예산: 전기세가 얼마나 내릴지는 아직 미정입니다` (same string in the height-calc line and the render line — both changed). Plain `예산` chosen over `예산（국가 예산）`: same 2-syllable length as `가계` (zero layout shift — P6 col3 ends 1233.71, identical to the D5 build) and consistent with Q92's `2027년 예산`. No other content touched. **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); only `p6-vertiefung.svg` changed (other 7 SVGs byte-identical; p6 text diff exactly the 3 changes, 381 texts both sides, 0 `가계` left); web PDF rebuilt from the new SVGs. Full gates re-run (logs in `hidden_files/w47/scratch-fix-de-ja-ko1/de-ko/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137,138,139,150]; occlusion 0 flags; boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal; spill 0 SPILL / 142 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 3,108 (reader layer; unchanged vs pre-fix by the multiset proof below); print/web text layers multiset-identical (35,362 non-space chars each); pre/post print multiset differs ONLY by 가×3/계×3 → 예×3/산×3; text.md re-exported from source, diff exactly 3 lines (L703/L721/L753), 591 entries / 150 exercises, byte size unchanged (51,701 B). New deliverables: print 12,926,498 B sha `0f264beeb0aa…`; web 1,791,562 B sha `44c4af5caa25…`; text.md 51,701 B sha `cbe640b3e8dd…`. Not committed / not pushed (coordinator inserts).

- **fix-de-minor1 rebuild (2026-11-13)** — **Cause**: de-family round-2 independent reproof (worker 7877e6e8, §8.4 round 2) — C-1/C-2 (core German text, all 11 editions) + the de-ko UND SIE term fix. **Fix (in source, then rebuilt)**: C-1 — P3 lead `die ersten Weihnachtsmärkte` contradicted the Hafenmarkt (open since 13 Nov, same article §2): P3 lead → `zwei große Weihnachtsmärkte` (same length, zero layout shift); the P5 lead carried the identical false claim and was fixed with the same wording; Q34 `Am Montag öffnet in Köln der erste ___.` → `Am Montag öffnen in Köln der Markt am Dom und der Markt der Engel, zwei große ___.` (word-box word and answer key `Weihnachtsmarkt` → `Weihnachtsmärkte`); Q80 `Am 16. November öffnen in Köln die ersten Weihnachtsmärkte.` → `Am 16. November öffnen der Markt am Dom und der Markt der Engel.` (answer stays `Richtig`). Q29 left unchanged (A2-acceptable per the brief; changing it would change the answer key). C-2 — P5 1903 calendar `Die Kinder konnten die Fenster mit Bildern überkleben.` → `Die Kinder konnten die Bilder ausschneiden und auf den Kalender kleben.` (the 1903 Lang/Kepler edition was windowless cut-and-paste). The `überkleben` gloss entry is left in place (the brief's fix is the sentence only; flagged to the coordinator). **de-ko fix (edition-local, `content56.py:53,59`)**: P5 UND SIE prompt `어드벤트 캘린더를 만드나요?` → `대림절 달력을 만드나요?` (both the height-calc line and the render line — the rest of the edition already uses `대림절 달력` everywhere: gloss, word list, Q67–75, answers). Shorter string, no layout risk. **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p3, p5, p8 (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-fix-de-minor1/2026-w47-de-ko/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 65 titles, 479 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal; spill 0 SPILL / 142 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 3,099 (reader layer; the shift vs the previous round's count is P3/P5/P8 re-wrap from the longer Q34/Q80 sentences, not content — the multiset proof below is authoritative), added Latin strings 152; print/web text layers multiset-identical (35,411 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: `die ersten`→`zwei große` ×3, `erste`→`Markt am Dom und der Markt der Engel` ×2, `Fenster mit Bildern überkleben`→`Bilder ausschneiden und auf den Kalender kleben`, footer/Q34-key changes where applicable); text.md re-exported from the fixed sources, diff exactly 8 lines (the 7 base lines + L613 P5 UND SIE `어드벤트 캘린더` → `대림절 달력`), 591 entries / 150 exercises. New deliverables: print 12,926,102 B sha `800fc2f6e136…`; web 1,790,180 B sha `d8fda6135bb0…`; text.md 51,764 B sha `1256bd272c32…`. Not committed / not pushed (coordinator inserts).

- **fix-de-round3 rebuild (2026-11-13)** — **Cause**: de-family round-3 independent reproof (§8.4 round 3) — R3-F1/R3-F2 (see below). **Fix (in source, then rebuilt)**: R3-F1 — the C-2 fix (fix-de-minor1) removed `überkleben` from the P5 1903 sentence but left the orphan gloss entry in the P5 gloss (`content56.py:23`); SOP §8.1 requires every glossed word to occur in the text, so the ` · überkleben …` segment was deleted from the P5 gloss (gloss shortens by one entry, layout-safe). R3-F2 (de-ko only) — P5 UND SIE? prompt `대림절 달력를` used the vowel-final particle `를` after consonant-final `달력`; `content56.py:53,59` → `대림절 달력을` (answer 139 was already correct `을` and is untouched). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p5 only (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-reproof-de-round3/2026-w47-de-ko/fix-round3/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 65 titles, 475 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal; spill 0 SPILL / 142 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 3094, added Latin strings 151; print/web text layers multiset-identical (35,394 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: gloss `überkleben …` entry removed; de-ko `달력를`→`달력을` ×1); text.md re-exported from the fixed sources, diff exactly L585 P5 gloss, L613 P5 prompt, 591 entries / 150 exercises. New deliverables: print 12,925,712 B sha `013b5d8e255e…`; web 1,789,538 B sha `ef851f6fa7d6…`; text.md 51,730 B sha `a8804776b286…`. Not committed / not pushed (coordinator inserts).
