# Lucerna Weekly VOL.1 — KO × NL edition (Korean target × Dutch explanations)

- **Pairing:** target language = Korean (frozen VOL.1 core, `weekly-report-ko-vol1/`);
  reader language = Dutch. Every explanation — glosses, grammar notes,
  instructions, exercise apparatus, all P8 answer notes — is written
  directly in Dutch. No intermediary language anywhere in the pipeline.
- **Masthead:** `Lucerna` (no article, exactly as the core ships; Korean edition).
- **Build dir:** `hidden_files/weekly-report-ko-nl-build/` (copy of the shipped
  KO core build `weekly-report-ko-build/`; only the explanation layer was
  rewritten). Scratch (inventory, transform script, registry dumps, audit
  outputs) lives in that build dir's `scratch/`.
- **Status:** builder proofread complete; independent proofread **PASS**
  (2026-10-21, see §11 — one complete independent pass, zero problems,
  no fixes, no re-render).

## 1. Baseline proof (frozen core reproduced before any edit)

The core build was copied to `weekly-report-ko-nl-build/` and run UNMODIFIED
via `tools/freeze.py baseline`: **8/8 SVGs byte-identical (sha256) to the
shipped core SVGs** in `files/weekly-report-ko-vol1/svg/` (p1 f7db1604…,
p2 f38afa34…, p3 f5a258a4…, p4 6ceb1f22…, p5 0adf32b9…, p6 e5e849ad…,
p7 d8219859…, p8 bd3b245f…). This reproduces the core's current shipped
state, including the 2026-10-21 P2 patch (D-day sentence −6px). Registry
from a pristine-core dump: TOTAL 150, A2 57 · B1 66 · B2 27, per page
10/18/18/18/18/18/12/38, writing model 162 chars. After all work, the core's
shipped SVG hashes were re-verified: **unchanged (8/8)**. A re-run of this
edition's own build also reproduces its 8 SVGs byte-identically
(deterministic build).

## 2. Totals (this edition = core, exactly)

- Exercises: **150** — A2 57 · B1 66 · B2 27; per page 10/18/18/18/18/18/12/38.
- Types: Maak de zin af 49 · Meerkeuze 51 · Koppelen 16 · Zin omvormen 4 ·
  Zinnen bouwen 8 · Waar of onwaar 4 · Cloze 13 · Vertaling 4 · Schrijven 1.
  Writing model: 162 chars. Register 해요체 throughout (frozen Korean text).
- Build log: zero FLOW OVERFLOW, zero HEAD TOO WIDE warnings.

## 3. Key-diff registry (complete — registry diff vs core)

Keys are byte-identical to the core for 147 of 150 items. The only differences
are the translation items, which legitimately re-aim at Dutch:

| # | Core key (Chinese) | This edition's key (Dutch) |
|---|---|---|
| 137 | 台风的路径还可能改变。 | De koers van de tyfoon kan nog veranderen. |
| 138 | 离考试还剩 29 天。 | Er zijn nog 29 dagen tot het examen. |
| 150 | (开放题，范文如下) | (open vraag — het voorbeeld staat hieronder) |

- #150's note: «Het voorbeeld staat in deel H van deze pagina (162 tekens)».
- Stems re-aimed (keys stay the frozen Korean originals):
  #139 stem «Controleer dit weekend het nieuwste weerbericht. → ___» (key 주말에는 최신 날씨를 확인하세요.);
  #140 stem «Ik ga vrijdag naar het Haneulpark om het zilvergras te zien. → ___» (key 저는 금요일에 하늘공원에 억새를 보러 가요.).
- All **150 notes rewritten in Dutch** (registry note-diff count = 150/150).
  Page/level metadata diff vs core: none.
- `tools/p8.py` reported informational keydiff [4, 9, 99, 109, 137, 138, 149]:
  #4/#9/#99/#109/#149 were verified line by line in the printed P8 SVG —
  the printed keys (제주도 / A / O / 기준 / B) are byte-identical to the core;
  only the notes differ (extraction artefacts of the dash-style split).

## 4. Answer-key format & printed-note set

- The core's DASH style is kept byte-for-byte in the generating code:
  `N. key — note`; #150 prints «150. ✓ Het voorbeeld staat in deel H van
  deze pagina (162 tekens)».
- P8 group separators follow the NL column pattern of the shipped NL
  editions (PT×NL, RU×NL): «— Pagina N —» for N = 1..8.
- **Printed-note set** (`tools/p8.py compare`): **CLEAN** — core 150 noted,
  edition 150 noted, missing=[], extra=0. **Sets EQUAL {1..150}.**

## 5. Dutch furniture (verbatim, as shipped)

- P1 badge (20pt sans bold, brick, centered; measured 1044.2px — fits):
  «TEKSTEN IN HET KOREAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS»
  (inserted under the strap exactly as in the shipped KO×EN / KO×PT editions:
  strap 372→366, badge at y=394, rules 392/401→412/421, band 424→433).
- P1 strap line: «매주 한국어로 · Elke week · 한국 사람이 읽는 한국어를 읽어요»;
  band right lines: «DE TYFOON TREKT NOORDWAARTS» / «Controleer dit weekend
  het nieuwste weerbericht · Voorbereiding op blz. 2».
- Section heads pair Korean + Dutch (e.g. «생활 · Dagelijks leven»,
  «문화 · Cultuur», «스포츠 · Sport», «청년 · Jongeren», «깊이 읽기 · Dieper lezen»,
  «말 공부 · Taal», «시험과 답 · Toets en antwoorden»); band subs pair likewise.
- Gloss prefix: «Uitleg — » (the library helper `glossline()` was renamed
  `expl()`; `gloss()` boxes carry the «Uitleg — » prefix). Count in paper: 9.
- Footers (every page): «Lucerna · KOREAANS WEEKBLAD VOL.1 · TEKSTEN IN HET
  KOREAANS · UITLEG IN HET NEDERLANDS» / «Pagina N van 8».
- Exercise-section expl lines are Dutch (e.g. «Lees de teksten op blz. 2 en
  kies het juiste antwoord.»); instr words: Vul in · Koppel · Herschrijf ·
  Bouw · Vertaal · W of O · Schrijf.
- Number format: Dutch (551.864 · 1.312 · 75.000 · 1.000 · 1,5 miljoen).
  Frozen Korean keys keep their own printed form (e.g. key #21 «551,864» is
  the Korean key itself; its Dutch note uses «551.864»).
- Deviations from word-for-word translation: **none in furniture.** One
  wording shortening inside content (§7).

## 6. Freeze check, language scans & Hangul adjudication

- `tools/freeze.py diff` (core vs this edition): every added/removed string
  is explanation layer, pairing furniture (incl. the Korean footer
  «제 N 면 / 총 N 면» → «Pagina N van 8»), or a §3 registry item.
  **No Korean target string changed.** Han ideographs in the edition's SVG
  text: **0** (the core carries 1,976+ Chinese explanation characters).
- Added-CJK accounting (KO rule: adjudicate per syllable, cf. KO×PT +8):
  pages 1–6 added **0**. Total added Hangul syllables = **11**, all
  citations of frozen Korean inside Dutch notes:
  - P7 (+2: 어·요) — the error-clinic note «In «할 수 있어요» schrijf je
    «수» los.» cites the phrase «할 수 있어요».
  - P8 (+9: 억·새·연·이·건·네·는·위·로, one each) — note #35 cites the
    festival theme «억새, 자연이 건네는 위로».
  No new Korean target text anywhere.
- The banned intermediary-layer term (either script form): **0 occurrences**
  in the paper, this KIT, and the operative build code. The explanation
  helper is named `expl()`. The one-off transform script in `scratch/`
  quotes the core build's original strings purely as search patterns
  (source side of the map); it is not operative code.
- P7 phrase occurrence counts vs core: **3/2/1/4/1/1/1/1 — identical**
  (phrases 1 and 4 legitimately recur via article/key text, as in the
  core); page tags (1면…6면) counts identical.

## 7. Geometric occlusion audit (mandatory gate)

`tools/occlusion_audit.py` (selftest passed first): edition **0 flags**,
core 0 flags, **NEW vs core = 0**. Supplementary width measurements with
the build's own `text_w` (advance) for the fixed-position strings the
audit does not box-check: P1 badge 1044.2/1820, band right lines
408.5 and 728.6 (no contact with the Korean band text — also covered by
the audit's TEXTX class), footer left 933.5 (clear of the right footer),
P1 search-box source line 389.4/412 available, D-day box title 376.9/398,
contents title 255.5/390, numbers-box title 309.2/398, all exercise-header
right lines and band subs within bounds. Builder's full proofread: all 8
cards read in final render — no overflow, no struck-through text, no
footer-band ink.

## 8. Calendar & content red lines

All weekday claims verified against the real 2026 calendar (Asia/Seoul):
Mon Oct 19 (issue week start), Tue Oct 20 (3차전), Wed Oct 21 (4차전),
Fri Oct 23 (5차전 if needed; silver-grass festival's last day),
Sun Oct 25 (play-off start), Mon Nov 2 (Korean Series), Thu Nov 19 (수능,
D-29 from Oct 21). Typhoon Champi stays in the core's open-forecast
framing (forecasts differ; landfall undecided) — no Dutch note re-states
it as fact. The foliage two-peaks dispute is frozen core content,
carried unchanged.

## 9. Deliverables & PDF pins

- `svg/` ×8, `cards/` ×8 (1950×2700).
- Print PDF `Lucerna-VOL1-NL.pdf`: **32,295,727 B**, sha256 `dde99f41773fb287353b8e37535946d81ca05d415f9255fb5b0f18e6357557e4` (D5 rebuild, 2026-11-13).
- Web PDF `Lucerna-VOL1-NL-web.pdf`: **2,009,801 B** (< 7 MB), sha256 `4f1031653e3cec2890f634081e2728f8e3b6fd76f65c57d1ba2499280cbb9d3d` (D5 rebuild, 2026-11-13).

## 10. Defects found & fixed during the build

- None in the final artifacts. The build ran clean on the first pass
  after the transform (zero flow warnings); the only corrective action
  was preventive: the P1 KoreaTrendBoard source line was shortened to
  «Ca. aantallen» during wording (advance 389.4px vs 412px available),
  mirroring the shipped KO×PT wording-shortening at the same slot.

## 11. Independent proofread record (2026-10-21) — PASS

One complete independent pass over the final artifacts; **zero problems
found — no fixes, no re-render.** Scratch: `hidden_files/proof-ko-nl/scratch/`.

- **Tools (all re-run independently):** `freeze.py baseline` on a fresh
  copy of the core build — **8/8 byte-identical**, core integrity
  confirmed; core SVG sha256 set re-verified unchanged again after ALL
  runs (8/8 OK). `freeze.py diff` — pages 1–6 added CJK = 0; P7 +2,
  P8 +9 (see Hangul adjudication below). `p8.py compare` — **CLEAN**,
  150 noted = 150 noted, sets EQUAL {1..150}, keydiff [4, 9, 99, 109,
  137, 138, 149]. `occlusion_audit.py` (selftest passed) — edition
  **0 flags**, core 0 flags, **NEW vs core = 0**.
- **Registry diff (fresh one-process dumps of both builds):** 150 = 150;
  page/level metadata diffs NONE; **key diffs exactly {137, 138, 150}**
  with the exact Dutch strings of §3; notes changed 150/150; type counts
  map 1:1; writing model counted 162 chars in both dumps. All 150 keys
  additionally re-derived by hand from the Korean articles/stems in a
  full read of all 8 pages — every key correct; #139/#140 Dutch stems
  confirmed in the build and the printed P8, Korean keys byte-identical.
- **Printed-key artefacts adjudicated in the P8 SVG:** #4 제주도,
  #9 A, #99 O, #109 기준, #149 B — printed keys byte-identical to the
  core, only notes translated (dash-split extraction artefacts, as §3).
  #150 prints «150. ✓ Het voorbeeld staat in deel H van deze pagina
  (162 tekens)» exactly as §4.
- **Hangul adjudication:** +11 total, all citations — P7 clinic note
  «In «할 수 있어요» schrijf je «수» los.» (+어·요) and P8 note #35
  «Het thema is «억새, 자연이 건네는 위로»» (+9) located verbatim in the
  final SVGs. No new Korean target text; Han ideographs in the edition
  = 0 on all 8 pages.
- **Geometry (true ink, pixel checks):** P1 source line ink 1475→1864
  (margin 1885; core 1475→1862) — the «Ca. aantallen» shortening holds.
  P1 badge band: strap ink ends row 366, badge ink rows 379–393, band
  rule rows 411–412 — no contact. P2 patch point preserved exactly:
  D-day sentence element at identical coordinates (x=65, baseline 1794)
  and card ink ends row 1795 with per-row dark counts identical to the
  patched core card; rows 1796+ clear.
- **Furniture:** badge on P1, footers + «Pagina N van 8» on all 8 pages,
  «Uitleg — » ×9 (= core's 9 gloss slots), P8 separators «— Pagina N —»
  ×8 — all verbatim. Dutch number forms (551.864 · 1.312 · 75.000 ·
  1,5 miljoen · 1.000) appear only inside Dutch notes; printed keys keep
  the core forms (551,864 · 1,312 · 1,000 · 75,000). Images byte-identical
  per page (base64 payload hashes equal); credit lines identical to the
  core on every page.
- **P7 phrases:** all 8 quotes verbatim with «(N면)» tags; per-phrase
  occurrence counts equal between core and edition under an independent
  full-text count (and equal to §6 under the builder's count).
- **Calendar (re-checked with `date`, Asia/Seoul):** Oct 19 Mon,
  Oct 20 Tue, Oct 21 Wed, Oct 23 Fri, Oct 25 Sun, Nov 2 Mon, Nov 19 Thu;
  Nov 19 − Oct 21 = 29 days (D-29 exact). Champi remains an open
  forecast in every Dutch note; the foliage two-peaks framing is intact.
- **Banned intermediary term:** 0 in the final SVGs, this KIT, and the
  operative build code (incl. scratch). Core untouched throughout.
- **Final pins (measured on disk, match §9):** web **3,087,276 B** /
  `ec89fb2d2dca2eb428114102ad4eda77f3e99ae704ecc2e38ff7a4fcc0e46f3c`;
  print **34,452,871 B** /
  `0128ca958e25e8335cb759440b6ed7c433ec7c407b15dd4980430d7055379b0f`
  (print size is the KO family's image-source weight — recorded only).

## 12. D5 rebuild (2026-11-13)

D5 rebuild (2026-11-13–14；builder：W43 ko 家三任；不 commit、不 push；独立重校另派他人；入仓由 closer 做）。D5 报告：`production/notes/2026-w43/g-ko/scratch-d5-rebuild-ko/D5-REPORT-2026-w43-ko-nl.md`；门禁日志：`hidden_files/d5-redo/scratch-2026-w43-ko/logs/2026-w43-ko-nl-run2/GATES-SUMMARY.txt`。

- 装机：移植模板 `tools/mechanism-w47/svglib-ko-d5.py`（539 行）原样装为版内 `svglib.py`，仅改写 `_D5_READER = "latin"`；core-ko 落盘同模板（`production/2026-w43/core-ko/svglib.py`，+333/−40）。路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 保留（`_QUOTE_CLS` 在位）。ko-ru 无 fix-xru（W43 重建标准，见家族报告 §0）。
- 基线：`run.py` TOTAL 150、0 警告（fr 例外：基线唯一警告为 port 已知良性 HEAD TOO WIDE，见 D5 报告 §二）；修前普查 D5 拉丁 435、西里尔 0、弯引号在 CJK 0；基线印 PDF 34,436,224 B、sha256 `52dacd178c63cd0f7a2001011445680d6ecfed8c8261567df79160e2519ffd6d`；基线网 PDF 2,108,716 B、sha256 `8ce23455e33ec7f57f86d81d076ff4bffb4b134b7c6a050373cf48fe78412865`。
- 缺陷与修复（只动字号，文字内容未动）：
- run1 无真缺陷；唯一 FAIL 为门 17 缺脚本 SKIP（production 与 fanout 均无 `audit_ko_nl.py`），不是 FAIL，不阻塞。
- 门禁 run2：PASS=18 FAIL=1（run1：PASS=18 FAIL=1）。run TOTAL 150；head_check PASS 0 defects；d5 census 0/0/0；render RC=0；webpdf RC=0（2009801 B <7MB）；occlusion 0；p8 extract 150/150；p8 compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8；freeze diff vs base 新增 CJK 0；spill 0；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0 defects（ratios n=376，中位 1.01，粗体 1.04，常规 0.994；P8 237→242 行，距页脚线余量 47.2px）；文字层 print=web 多重集差 0（各 28667 字符）；census_quotes 0 defective；D18 刊头间距 GAP=350.4；门 17：SKIP（无此脚本）。
- 新交付物（实测发运值）：印 PDF `Lucerna-VOL1-NL.pdf` 32,295,727 B、sha256 `dde99f41773fb287353b8e37535946d81ca05d415f9255fb5b0f18e6357557e4`；网 PDF `Lucerna-VOL1-NL-web.pdf` 2,009,801 B、sha256 `4f1031653e3cec2890f634081e2728f8e3b6fd76f65c57d1ba2499280cbb9d3d`（<7MB，待 closer 换入 `issues/2026-w43/2026-w43-ko-nl/2026-w43-ko-nl.pdf` 并更新 pin）；新建 text.md `2026-w43-ko-nl.text.md` 21,656 B、sha256 `1e6e08ff083f7f692996317b984b3ae5439f26286d380f07f762df6f283f3055`，与 fanout `.text.md.new` BYTE-IDENTICAL，`verify_textexp_ko.py --edition` ADOPT。
- KIT 旧值（印 34,452,871 B / 网 3,087,276 B，旧配方）已过期——基线实测印 34,436,224 B。本节交付物行已更新为上述 D5 新值。
