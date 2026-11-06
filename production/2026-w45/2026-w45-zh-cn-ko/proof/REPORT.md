# INDEPENDENT PROOFREAD — W45 ZH-CN × KO (Simplified Chinese target · Korean reader)

**Verdict: PASS — ZERO PROBLEMS.**

- Edition dir: `files/weekly-report-w45-zh-cn-ko/` — svg ×8, cards ×8 (1950×2700 PNG),
  print `Lucerna-VOL2.pdf`, web `Lucerna-VOL2-web.pdf`, `WEEKLY-KIT.md`, `ABSTRACT.txt`.
- Build dir (read for code checks; never executed inside it):
  `hidden_files/weekly-report-w45-zh-cn-ko-build/` (`transform_ko.py`, `koscan.py`).
- Core: `files/weekly-report-w45-zhcn-core/` + `hidden_files/weekly-report-w45-zhcn-build/`
  (150 exercises: A2 56 / B1 69 / B2 25).
- W43 same-pairing reference: `files/weekly-report-zh-cn-ko/` +
  `hidden_files/weekly-report-zh-cn-ko-build/`.
- Proof work (this report + all logs/scripts): `hidden_files/w45/zh-cn-ko-proof/`
  (`REPORT.md` + `work/`). No subagent was spawned. No `~/workspace/weekly-git` touch,
  no `insert.py`, no Discord post, no main-chat card/PDF dump, no cron, no shared-scratch
  cleanup. No content module was ever imported inside the core build dir; every execution
  ran in fresh proof copies (freeze.py scratch, gate10 copy, webregen staging).

## 0. Pre-flight duplicate check — PASS

- (a) No live worker/process references the ko delivery or build dirs at task start
  (other editions' workers — zh-cn-ru, zh-tw, zh-tw-fr — were running, none touching ko).
- (b) Two mtime snapshots of both dirs, 08:34:47 UTC and 08:38:09 UTC:
  **ZERO changes** (`work/snap1.txt` vs `work/snap2.txt`, diff empty).
- (c) Builder session completed: last delivery-dir write 08:27 UTC (WEEKLY-KIT.md),
  before this proofread started. Proceeded on that basis. A closing snapshot
  (`work/snap3.txt`) confirms delivery + build dirs are unchanged by this proof.

## 1. Freeze baseline + diff decomposition — PASS

- `tools/freeze.py baseline` on the W45 zh-cn core build, re-run by the proofreader:
  **8/8 SVGs byte-identical**, shipped core SVGs re-hashed unchanged
  (`work/freeze-baseline.log`, `work/freeze-baseline.json`).
- `tools/freeze.py diff` (core vs edition) string counts match the proofreader's own
  multiset diff exactly: P1 +42/−44, P2 +57/−59, P3 +36/−36, P4 +37/−40, P5 +38/−40,
  P6 +37/−38, P7 +77/−83, P8 +190/−198 (`work/freeze-diff.json`, `work/analysis.txt` §1).
- Every removed string was individually inspected: all are English explanation strings,
  bilingual furniture lines, Notes｜ gloss fragments, footer/badge/page-line lines, or
  P8 answer lines (key + English note). **No pure-Chinese target string was removed**
  except wrapped-line re-breaks of the same target text (P8 model-answer paragraph and
  one P7 clinic fragment re-wrap because neighbouring Korean notes change line breaks;
  character totals below prove nothing was lost) and the page-line
  `第 {n} 版 / 共 8 版` (furniture, replaced by the Korean page line).
- **Charwise accounting** (proofreader's own count, string-multiset, per page):
  Hangul added P1 365, P2 457, P3 260, P4 292, P5 281, P6 301, P7 748, P8 1983 —
  all explanation-layer Korean. Hanzi net per page: P1 −30, P2–P7 −20 each, P8 −17,
  where the −20/−30 are exactly the removed footer/badge/page-line Chinese segments
  (14 chars losing count each page). **Net-positive Hanzi: only 候 +3, all on P8.**
  Novel-to-core Hanzi = ∅ (every Hanzi in any added string already occurs in the core).
  Freeze's P8 `cjk_added` total 1990 = 1983 Hangul + 候×3 + full-width punctuation
  （ ） ：×4 in the Korean notes — consistent, not a discrepancy.
- Strict-CJK diff exits 1 as expected for a ko edition (Hangul falls in the tool's CJK
  range); the gate applied is the charwise adjudication above, not the strict gate.
- **候 citations verified site by site (4 sites, P8 net +3, P3 net 0):**
  P3 gloss `해설 — hòu 候 — 5일 단위의 작은 계절 ·` replaces the core gloss
  `Notes｜hòu 候 — a five-day micro-season` (P3 候 total 8 = 8, net 0);
  P8 key 31 `31. A — 첫 번째 候： 물이 얼기 시작해요.`,
  P8 key 35 `35. 水始冰 — shuǐ shǐ bīng — 물이 얼기 시작해요 （첫 번째 候）.`,
  P8 key 123 `123. B — 첫 번째 候： 물이 얼기 시작해요.` (P8 候 total 2 → 5, net +3).
  Each cites the Chinese word being explained. No other added Hanzi.

## 2. Korean orphan scan — PASS (true flags 0)

- Proofreader's own implementation (`work/koscan_mine.py`, definitions verified against
  README #16 extended + task: window 10–45 incl. paren closings, line-start orphan
  punctuation, ≥3-syllable tail-mid cuts with corpus-verified splits, S2 ≤2-syllable
  final lines, S4 tight-leading continuations; corpus = edition build sources;
  SVGs contain 0 `<tspan>`, so the `<text>`-only scan covers every rendered line).
- Result, identical to a re-run of the builder's `koscan.py` on the same inputs:
  **S1 0, S2 1, S3 0, S4 0; G 2 (family gloss-continuation format), L 1 (`쓰기` label).**
- S2 sole candidate adjudicated PASS by the proofreader: P8
  `94. 179 — 199 − 20 = 179위안.` (x=989, y=1839.676) sits in the regular answer
  sequence 92 → 93 → **94** → 95 → 96 at ~29.2 spacing in the same column — a complete
  standalone key item starting with `94.`, not a wrapped continuation; its Hangul
  count is 2 only because the rest is digits/arithmetic.
- Round-1 fixes hold in the final render: no lone `것.` node on P4 (item rewritten to
  the single line `翻盘 fānpán — 경기를 뒤집는 역전승.`); no lone `광고.` node on P6
  (gloss1 now ends `… guǎnggào 广告 —` / `광고예요.`, a 4-syllable complete predicate
  wrapped at the dash boundary, not a mid-word split — no scan criterion fires).

## 3. Gate 10 — REPRODUCTION — PASS (blocking gate, verified independently)

- Fresh core copy in `work/gate10/` (core `*.py` + `assets/` + the builder's
  `transform_ko.py` copied unmodified) → transform exit 0 (`TRANSFORM OK`) →
  one-process `run.py` exit 0 → **8/8 SVGs byte-identical to the delivered SVGs**
  (sha256 compared, `work/gate10/out/` vs delivery `svg/`).
- Driver output: TOTAL 150, A2 56 / B1 69 / B2 25, by page 10/18/18/18/18/18/12/38;
  **zero `HEAD TOO WIDE` / `FLOW OVERFLOW` warnings** (grep count 0).
- Method note (does not weaken the gate): the transform's OUT repoint targets the
  delivery dir, so for this proof run the OUT lines were repointed *after* the
  transform to the proof-local `gate10/out/` — a destination-only change. Delivered
  SVGs contain no output paths (grep 0), so content is unaffected; the delivered
  dir was never written by this proof. The 123 `SKIP` lines in the transform log are
  per-file absent-string skips for shared lists, not failures.
- Registry and render warnings also match the builder's gate10 logs; the builder's
  own gate10 dir was not relied on.

## 4. Builder's self-fixes, re-verified on the final render — PASS

- (a) **P7 disclosure shortening:** letters box rect (1451, 1226.6, 434×**481.5**)
  byte-identical to core; clinic box 749.6 identical; letters-box bottom
  1226.6+481.5 = **1708.1** (the "col3 ends" figure); teaser rect y=2436.1 h=118
  (bottom 2554.1) identical to core; footer line y=2580 identical; P7 rect multiset
  differs from core ONLY in level-chip rects shifting up with shorter Korean text.
  Disclosure content preserved (see §10).
- (b) **5 residual notes, all Korean now, zero English explanation prose remaining:**
  source-level 1:1 mapping core→edition (content12/56/8 counts match) plus rendered
  confirmation — bǔdōng note (P2 gloss + P8 keys 18/28/46/138), WeChat 35 days
  (P6-exercise note + P8 keys 24/86/128), TES beat G2 Oct 26 (P8 key 125),
  new film Nov 7 (P8 key 119), Huang Yan crematory worker (P5-exercise note + P8
  keys 69/127), shùzì AI note (P5-exercise note variant + P8 keys 70/135).
  All six English originals return zero hits in every rendered SVG.
- (c) **Residual-Latin adjudication, re-run by the proofreader** (every Latin-bearing
  rendered node listed, `work/analysis.txt` §2, plus a token classifier over all
  Latin runs): remaining Latin is ONLY pinyin headwords/citations (incl. tone-marked
  forms and their line-wrap fragments), VOL.2/VOL.3 numbering, Commons Artist credit
  lines verbatim, frozen target-text codes (S16, LPL, team codes AL/IG/TES/BLG/HLE/
  G2/KC/TL/GEN/DK/TSW/MKOI/T1/LYON, BO3, AI), the cited English source phrase in the
  P7 B1 glossline («Saturday evening, Nov 7» — W43 ko precedent, see §8), frozen
  `(p. N)` tags, level badges (A2/B1/B2), option letters, `3px` chart-scale notation,
  and X/Y placeholders in the sentence-frame pattern. **No other Latin prose.**

## 5. p8.py + DASH style — PASS

- `tools/p8.py compare` (explicit `--core-p8`/`--edition-p8`, `--total 150`):
  **CLEAN — core 150 noted = edition 150 noted, missing=[], extra_count=0,
  uncertain=[], keydiff=[]** (exit 0, `work/p8.log`, `work/p8.json`).
  (Note: the `--core-dir/--edition-dir --target ko` form fails with a wrong P8
  filename guess `p8-siheom.svg` — a tool invocation quirk, not an edition issue;
  the explicit-path form is the documented one and was used.)
- DASH verified from code, not from the claim: W43 ko build `content8.py` lines
  119/121 read `f"{e_['n']}. {e_['key']} — {e_['note']}"` /
  `f"{e_['n']}. ✓ {e_['note']}"` — byte-identical in form to the W45 core and to
  this edition's `content8.py`. No style change was needed or made; answer-generation
  code lines are identical across all three (only note strings translated).

## 6. Occlusion audit + same-baseline + chart — PASS

- `tools/occlusion_audit.py`: selftest OK (all 6 classes fire exactly once, clean
  controls silent); **edition 0 flags; core 0 flags; NEW vs core 0**
  (`work/occlusion-self.log`, `work/occlusion.log`, `work/occlusion.json`).
- Proofreader's own same-baseline ink scan (`work/rowcheck_mine.py`, svglib copy
  md5-verified identical to core/edition svglib `59fddd17…`): **edition 0 collisions**.
  Core shows 1 P2 flag, confirmed as the `&amp;` measurement artifact: the flagged
  pair is the core's `Read &amp; choose` head, measured 5 chars wide for the entity
  vs 1 rendered glyph; the edition's shorter Korean heads do not trigger it, and the
  canonical true-ink audit reports core 0. Not a real overlap.
- Chart-label element check: P6 bars from x=325 measure **810 / 537 / 480 px**
  (3.0 px/yuan from zero) in BOTH core and edition, labels `A: 毛衣+围巾` /
  `B: 耳机` / `C: 书+本子` at identical positions; `content56.py` diff core→edition
  contains no bar-geometry lines (only explanation strings + OUT repoint).
  P4 element check 0 (builder's `chartcheck.py` pattern; P4 carries no chart bars).

## 7. Gloss counts — PASS

- Split on `·` (README #21): **10 calls / 33 items** in both core and edition
  (content12 3/12, content34 3/9, content56 4/12), and the 33 headwords match
  **item by item in order** (xiànhuò 现货 … tuìhuànhuò 退换货). Rendered gloss-head
  nodes: 10 in both.

## 8. P7 golden sentences — PASS (with a KIT-citation correction, see Non-blocking)

- All 8 sentences verbatim from this issue's own articles, each appearing on exactly
  2 pages (article page + P7) under page-concatenated search, identically in core
  and edition: 不用等11月11日 (P1), 下单就能发货 (P2), 先看结算页，再付款 (P2),
  水开始结冰 (P3), 三场都输了 (P4), 小局一场没赢 (P4), 故事够不够好 (P5),
  别以后，就现在 (P5).
- Edition page tags, read off the rendered P7 golden box: **p. 1/2/2/3/4/4/5/5** —
  correct against the article pages above. Tag form `(p. N)` (half-width parens)
  matches the W43 ko precedent (W43 P7 carries the same form; its own tag set
  1–6 reflects W43's different articles).
- The KIT §6 cites the tags as "p. 1/1/2/3/4/4/5/6" — that citation is wrong
  (sentence 2 is P2, not P1; sentence 8 is P5, not P6). The EDITION tags are right;
  only the KIT sentence needs correcting (non-blocking, §15).

## 9. Images — PASS

- **6 payloads byte-identical to core** (md5 of base64 payloads), same page placement:
  P1 1 / P2 1 / P3 2 / P4 1 / P5 1 / P6 0 / P7 0 / P8 0.
- Credit lines verbatim and identical to core: `Photo: Map hobby — CC0`,
  `Photo: Paul Gilmore — CC0`, `Photo: Gerda Arendt — CC0`, `Photo: Syced — CC0`
  (×2 pages), `Photo: Based5290 — Public domain`, all `(Wikimedia Commons)`.
  W43 ko shipped SVGs also carry English credit lines, so the English form is
  precedent-consistent, not a defect. Commons API was NOT re-queried live for this
  proof (see Limitations); the check is byte-identity to the shipped core plus
  W43 precedent.

## 10. Readers' corner — PASS

- Code-level: the frozen Chinese disclosure string's first 106 chars are
  byte-identical between core and edition `content7.py`
  (`编辑部示例信,不是真实来信。编辑部说明:VOL.1曾预告本期(VOL.2)刊登真实读者来信和VOL.1第8版最佳作文;至今没有收到真实来信,也没有可刊登的投稿,所以本期仍刊登编辑部示例,并继续征集。延期不是取消。`);
  rendered Chinese lines match (first wrapped line identical; the wrap continues
  into the Korean tail on the shared line, as the typesetter does).
- Korean disclosure states: no genuine letters have arrived, no publishable
  submission exists (`VOL.1에서 약속한 실제 독자 편지와 VOL.1 8면 우수 작문은
  아직 도착하지 않아`), the corner still prints an editor's example
  (`이번 호에도 편집부 예시를 싣습니다`), deferral ≠ cancellation
  (`연기가 취소는 아닙니다`), and ends with the verbatim open invitation
  (`여러분의 편지와 작문을 보내 주세요!`).

## 11. Furniture three-way (core EN · W43 ko · this edition) — PASS

- P1 badge MEASURED on all three P1 SVGs: **(975, 434), 19.5pt, weight 700,
  anchor middle, BRICK #a4553a** in both W43 ko and this edition (core EN is
  OLIVE #3e4c2a at the same slot); text verbatim W43 ko:
  `중국어 간체 텍스트 · 한국어 해설 — 한국어 독자를 위한 판` — in-place
  replacement, NOT the 372 slot and NOT the 574 insert slot. The y=372 node is the
  frozen bilingual strapline in all three
  (`给学中文的人的周报 — 진짜 중국을 중국어로 읽어요`, 19.0pt, in W43 ko and here).
- Footer on all 8 pages: `Lucerna · 중국어 간체 주간지 VOL.2 · 텍스트는 중국어 간체 ·
  해설은 한국어` + `제 {n} 면 / 총 8 면` (VOL.2 from this core; W43 ko reads VOL.1).
- P8 separators `— 제 {pg} 면 —` on all 8 pages; gloss prefix `해설 —`;
  P8 answers head verbatim W43 ko: `答案 · 모든 정답과 해설 (1–8면)` /
  `해설은 모두 한국어 · ✓ = 쓰기 과제`. Section-head bilingual form, instr labels
  (빈칸 채우기 / 단어와 뜻 짝짓기 / 쓰기), byline (Lucerna 편집부 · 읽기 수준 {L}),
  answers pointer (정답은 8면 · 答案见第 8 版) all follow the W43 ko pattern.
- No furniture discrepancy requiring adjudication was found (tables.json was not
  edited by this proof; shipped W43 would win over tables.json per the task rule).

## 12. Web regen — PASS

- Proof-local re-render from the delivered SVGs (staging copies of the builder's
  `render.py`, BASE repointed to proof staging): **cards 8/8 byte-identical**,
  **print PDF byte-identical** (42,233,918 B, sha256 unchanged) — in both regen runs.
- Web PDF, filename-exact second run (`work/webregen2/`): same size 3,074,264 B and
  **date-stripped byte-identical** to the delivered web PDF; all 8 embedded page
  JPEGs byte-identical (same sha + sizes per page). The raw bytes differ ONLY in
  the CreationDate/ModDate timestamp fields — stated explicitly as the task allows.
  (A first regen run with a different staging filename also differed in the /Title
  metadata field, which is the staging filename, not content; the filename-exact run
  removes even that difference.)
- Cards are 1950×2700 PNGs (PIL-verified for all 8).

## 13. Eyeball all 8 cards — PASS

- All 8 delivered cards read in full: layout clean; no overflow, no overlap, no
  missing glyphs/tofu, no footer intrusion on any page. P7 teaser clears the footer
  line; P6 chart labels sit clear of bars; P4 match-words item is a single clean
  line; P6 gloss1 ends cleanly inside its box; P8 answer columns end above the
  footer. Box-height shrinkages vs core on P1/P2/P4/P5/P6 (shorter Korean text)
  reflow cleanly with no clipped text (consistent with occlusion 0 + rowcheck 0).
- Korean prose on P1–P7 was read in full (`work/korean-prose.txt`): natural,
  dates/numbers consistent with the Chinese text and with P8 keys
  (Nov 13 / Nov 7 Sat / Oct 12 20:00 / Nov 10 20:00 / Nov 2–8 / Nov 1 / Nov 4–7 /
  Nov 8 / 06:00 Beijing / Oct 26–27 / 3–0 / 0–3 / 35 days / baskets 270/179/160 /
  119.2万 / 100 min AI film / 114 min new film). No Korean error found
  (see Limitations for the non-native-speaker caveat).

## 14. ABSTRACT.txt — PASS

- Korean single line (one trailing newline), **174 chars** (stripped), **no ASCII
  double quotes**. Names the real topics: 쌍11 현물 판매와 직접 인하, 11월 7일
  토요일 입동, 리그 오브 레전드 S16 8강전과 준결승, AI 영화와 입동 신작 영화;
  learner search phrase `중국어 신문으로 중국어 배우기`; paper name Lucerna;
  target language 중국어 간체; A2–B2 (`A2부터 B2까지`); exercise count 150문제.
  Facts match the edition itself (no template swap).

## PDF pins re-verified (final state)

- Print `Lucerna-VOL2.pdf`: **42,233,918 B**, sha256
  `c8f8de1ec602a433f2a2f2f8aa89e888da1228aaaa57febda9f77c64a7e79c7d` ✓
- Web `Lucerna-VOL2-web.pdf`: **3,074,264 B**, sha256
  `dd03c90138f02fad070220915f6e8af9d21128043fd101c69f2b99b08468510b` ✓
- SVG sha256 (8): p1 `385896c68ec495fd226797f218425edfa17ab8529553d2b7483206a1a81fae81`,
  p2 `7e8ba530d59c6fc22ad82103a0dcfb382958d5b7ef9d0dde76e2de533068542c`,
  p3 `e1365b72c6af2809662c626ce5603b13a64ffb78b13eafd60a068c04860661fd`,
  p4 `a78dff9c7c60109ee3e5243b75f5d60b211903b92f5817d038978009bd49864f`,
  p5 `79e2e341e3f3d253688680eb5ec4ac53917d93711f0446d27f653dde3dce0240`,
  p6 `ad3d07c12e3edc8f28153e46df34f7301bf0a6246d1e9f7a3858630083955853`,
  p7 `d6f551b42b9ae4316241d84351e6ba5b803b40f5d33037f5c8cf87376354a9a3`,
  p8 `c2d0cfc7226b42a52d87068923f5a1ce238a83e60dfaabfbba9a667ff7d8b2b5` —
  all match the KIT §12 pins. Delivered SVGs/PDFs were re-hashed at the end of this
  proof and are unchanged by it.

## 15. Non-blocking observations (NOT part of the verdict)

1. KIT §6 cites the golden-sentence page tags as "p. 1/1/2/3/4/4/5/6"; the correct
   sequence, verified against the articles, is p. 1/2/2/3/4/4/5/5 (see §8).
   The edition is correct; only the KIT line should be fixed by the coordinator.
   (Also KIT §7.3's "P3 matching note bǔdōng" label is loose: the translated bǔdōng
   note lives in the P2 gloss + P8 keys; the substance — 1:1 translation, zero
   English remaining — is verified.)
2. `tools/p8.py compare --core-dir/--edition-dir --target ko` guesses a wrong P8
   filename (`p8-siheom.svg`); the explicit `--core-p8/--edition-p8` form works and
   was used. Tool quirk, not an edition issue; worth a tools/README note.
3. P7 B2 column's `6면이 그 예예요` is elliptical but grammatical and clear in
   context; left as is.

## Limitations (stated honestly)

- Korean was checked by full reading of every rendered Korean node (P1–P7 prose +
  P8 notes) plus mechanical scans, not by a native speaker; no Korean error was
  found, but native-speaker nuance review was not performed.
- Commons Artist credit lines were verified byte-identical to the shipped core and
  consistent with W43 ko precedent; the Commons API was not re-queried live.
- Chinese target text was verified unchanged (freeze diff + charwise accounting),
  not re-proofread as new copy — it is the shipped core's text, which passed its
  own proofread; this proof covers the fan-out layer.
- Display mangling in some tool outputs (e.g. `��` for 첫/모/시) was confirmed by
  `repr()` checks to be a rendering artifact only; all underlying strings are clean
  (FFFD count 0 in transform source and delivered SVGs).

## Report path

`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-ko-proof/REPORT.md`
— with `work/` containing: `snap1.txt`, `snap2.txt`, `snap3.txt`, `analysis.txt`,
`korean-prose.txt`, `freeze-baseline.log/.json`, `freeze-diff.log/.json`,
`freeze-diff-strict.log/.json`, `p8.log/.json`, `occlusion-self.log`,
`occlusion.log/.json`, `rowcheck-ed.log`, `rowcheck-core.log`,
`koscan-mine.log`, `koscan-builder-rerun.log`, `koscan_mine.py`,
`rowcheck_mine.py`, `svglib.py` (copy, md5 = core), `analyze.py`,
`gate10/` (fresh reproduction: `gate10-transform.log`, `gate10-render.log`,
`out/*.svg`), `webregen/` + `webregen2/` (card/PDF regen + logs).
