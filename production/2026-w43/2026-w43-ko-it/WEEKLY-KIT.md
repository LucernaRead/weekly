# Lucerna Weekly — KO × IT edition (Korean text · Italian explanations)

- **Edition**: Korean target text (frozen VOL.1 core) with the complete explanation layer rewritten in Italian for Italian-speaking readers.
- **Pairing badge (P1)**: «TESTI IN COREANO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI»
- **Week**: VOL.1 — Mon 19 Oct to Sun 25 Oct 2026 (W43), same issue as the core.
- **Masthead**: «Lucerna» (no article, exactly as the core ships).
- **Layout**: 8 pages, 1950×2700, 4 columns, warm ivory — geometry frozen from the core; only wording changed.
- **Build**: `hidden_files/weekly-report-ko-it-build/` (copy of the core build; `render.py` repointed to this edition's dir; one-off transform scripts confined to that build's `scratch/` subdir).
- **Status**: builder proofread complete — INDEPENDENT PROOFREAD **PASS** (2026-10-21, one explanation-layer defect found and fixed; see the proofread record at the end — final PDF pins there supersede the builder's).

## Baseline proof (before any edit)

The copied core build was run UNMODIFIED with its output path pointed at the copy's own `baseline-out/` directory. All 8 regenerated SVGs are byte-identical (sha256) to the shipped core SVGs in `files/weekly-report-ko-vol1/svg/` — 8/8 match. The frozen core's shipped SVG hashes were re-verified again after all work finished: 8/8 unchanged (the core was never edited).

## Totals (identical to the core)

- **150 exercises** — A2 57 · B1 66 · B2 27.
- Per page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- By type (Italian labels): Completa la frase 49 · Scelta multipla 51 · Abbinamento 16 · Trasforma la frase 4 · Costruisci la frase 8 · Vero o falso 4 · Cloze 13 · Traduzione 4 · Scrittura 1.
- Writing model (P8 §H): 162 characters, unchanged.
- Build log: zero flow-overflow and zero head-too-wide warnings; every flow ends inside its column (P8 answer flow ends y=2442 of 2540; P7 teaser box ends y=2523).

## Key-diff registry (complete — registry-level diff vs the core)

Only these registry items differ from the core. All other 147 keys are byte-identical to the core's; page/level metadata differs on 0 items; all 150 notes were rewritten in Italian.

| # | Core key | This edition's key | Why |
|---|---|---|---|
| 137 | 台风的路径还可能改变。 | «La traiettoria del tifone può ancora cambiare.» | Translation exercise re-aimed at Italian; note → «Confronta con pag. 1» |
| 138 | 离考试还剩 29 天。 | «Mancano 29 giorni all'esame.» | Translation exercise re-aimed at Italian; note → «Confronta con pag. 2» |
| 150 | (开放题，范文如下） | «(domanda aperta — il modello è qui sotto)» | Writing apparatus in Italian; note → «Il modello è nella sezione H di questa pagina (162 caratteri)» |

Stems re-aimed (exercise body only; keys byte-identical Korean, as the reader now translates FROM Italian):

| # | Core stem | This edition's stem | Key (unchanged) |
|---|---|---|---|
| 139 | 周末看最新预报。→ ___ | «Nel fine settimana, controlla le previsioni più recenti. → ___» | 주말에는 최신 날씨를 확인하세요. (from P1) |
| 140 | 星期五我去天空公园看芒草。→ ___ | «Venerdì vado al Parco Haneul a vedere l'erba argentata. → ___» | 저는 금요일에 하늘공원에 억새를 보러 가요. (from P3) |

Answer-key format: the core family's dash style is kept — `N. key — note` (and `150. ✓ note` for the writing item); parentheses, where they occur inside notes, are half-width only.

## Printed-note set verification

The core prints all 150 P8 notes unconditionally (print-all rule). Verified in this edition's rendered P8 SVG by extracting every printed answer line: the printed set is {1..150} — EQUAL to the core's set by number. All 8 «— 제N면 —» group headings have answer keys below them in the same column (no orphaned headings).

## Italian furniture (verbatim, as printed)

- P1 subtitle: «SETTIMANALE COREANO · VOL.1 · 태풍 참피 · 가을야구 · 단풍»
- P1 top strip, middle segment: «Ogni settimana» (right segment stays Korean)
- P1 pairing badge: «TESTI IN COREANO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI» (brick slot under the tagline)
- P1 dark band, right side: «IL TIFONE AVANZA VERSO NORD» / «Controlla le previsioni più recenti · Preparazione a pag. 2»
- Gloss prefix: «Nota — »
- Footers (all pages): «Lucerna · SETTIMANALE COREANO VOL.1 · TESTI IN COREANO · SPIEGAZIONI IN ITALIANO» / «Pagina N di 8»
- Measured widths (build font metrics): badge 824px, subtitle 1177px, footer line 835px, band lines 373px / 554px — all inside their slots.
- Deviations (wording only, geometry untouched): (1) the P1 trend-source line is shortened to «KoreaTrendBoard (10월 21일) · Valori appross.» at 17px — the full Italian wording did not fit that narrow slot (same treatment as the shipped ES sibling); (2) the P2 D-day box title is «「D-데이」 사용법 · L'uso del D-day» — shortened after the geometric audit flagged the longer first wording (see Audit).

## Freeze check (text diff vs the core)

Full text-node diff of all 8 SVGs against the shipped core: every removed string is a Chinese explanation-layer string or Chinese pairing furniture; every added string is its Italian counterpart (glosses, grammar/expl lines, instructions, exercise apparatus, section titles' explanation halves, P8 notes, footer/badge furniture) or one of the 5 documented registry items above. Zero Korean target-text strings changed. Operative build code contains zero Han ideographs after the rewrite, and the core build's explanation method was renamed (`glossline` → `expl`, definition + all call sites). The intermediary-layer term (either language's form) occurs 0 times in the paper, this KIT, and the operative build code; it survives only inside the one-off transform scripts in the build's `scratch/` subdir, quoted there as search patterns from the core's original call strings.

P7 phrases of the week: verbatim Korean excerpts, byte-identical to the core, page tags identical (1면/1면/2면/2면/3면/4면/5면/6면); per-phrase occurrence counts equal the core's exactly (4/2/2/4/2/2/2/2 — phrases 1 and 4 legitimately recur via the vocab deck and key stems, in the core and here alike); only the translation lines under each phrase are Italian.

Calendar re-verified against the real 2026 calendar: CSAT Thursday 19 Nov 2026; 21 Oct → 19 Nov = 29 days (D-29 ✓); 준플레이오프 G3 Tue Oct 20, G4 Wed Oct 21, G5 (if needed) Fri Oct 23; playoff vs Samsung Sun Oct 25; Korean Series from Mon Nov 2; Eulalia festival last day Fri Oct 23; Cheongsong on-site Nov 4–8. Typhoon Champi remains an OPEN forecast in the frozen Korean text (landfall undecided), and the Italian notes preserve that status («previsione»).

## Geometric occlusion audit (mandatory gate)

Method: own script (build `scratch/audit_ko_it.py`, adapted from the KO×DE sibling's audit) — SVGs parsed in paint order, glyph boxes from the production font metrics (ink band = baseline −0.88em..+0.30em), line boxes expanded by half the stroke width. Classes: COVER (≥30% glyph coverage by a later opaque shape), LINEX (later thin line/border crossing an ink band), FOOTER (ink bottom > 2580), EDGE (ink past a page edge), TITLESPILL (a text starting inside an earlier filled box whose ink crosses that box's right/bottom edge — titles tested explicitly against their own boxes). The script was validated on a synthetic positive control first: all 5 planted defect classes caught, clean texts unflagged.

Results:
- Frozen core (reference run): 0 flags.
- This edition, first run: **1 flag — TITLESPILL on P2**: the D-day box title's ink ended at x=976 vs the box's right edge 961 (~15px over). Fixed by wording only («Come si usa il D-day» → «L'uso del D-day»); re-rendered and re-audited: **0 flags on all 8 pages**.
- Pixel adjudications on the rendered cards: P1 badge ink rows 378–393, clear of the tagline ink (ends 366) by 12 rows and of the masthead rules (412/421) by 19 rows; P1 dark-band left/right texts separated (right lines end-anchored at x=1855 with measured widths 373/554px; left line-2 pale ink ends x=864); P2 D-day sentence ink ends row 1795 vs rule rows 1803–1804 — the core's adjudicated adjacency, unchanged; P7 teaser ink ends row 2523, clear of the footer rule at 2580.

## Images (identical payloads to the core — verified byte-identical per page: 1/1/2/1/2/1/0/0)

All public domain / CC0, Commons-verified 2026-10-21 (full records in the core build's `assets/CREDITS.md`):

| Page | Image | Credit as printed |
|---|---|---|
| P1 | Super Typhoon Maysak eye, ISS-43 (2015 file photo, NOT Champi) | NASA — Public domain |
| P2 | Students studying, Sias Library 2017 (file photo) | Gary Todd — CC0 |
| P3 | Quail Feeding Amidst Susuki and Kikyo | Matsumura Keibun — Public domain |
| P3 | Still Life with Apples | Paul Cézanne — Public domain |
| P4 | Washington baseball team group photo | Bain News Service — Public domain |
| P5 | Crowd at Fort Knox concert (file photo, NOT NMIXX) | US Army — Public domain |
| P5 | Movie theater seats | Elijah Flores — CC0 |
| P6 | Hakkoda Mountains, Jogakura Valley in autumn (file photo, NOT Seoraksan) | lumoplank — CC0 |

## Deliverables

- `svg/` ×8, `cards/` ×8 PNG (1950×2700 each).
- Print PDF `Lucerna-VOL1-IT.pdf`: **32,292,387 B** (D5 rebuild, 2026-11-13), 8 pages, sha256 `7c6d7395db0728b5602a8802dea98c557c55970617d9e5cf744a8eb130c9a228` — supersedes the post-proofread-fix value 34,450,127 B / `0817b807…`.
- Web PDF `Lucerna-VOL1-IT-web.pdf`: **2,006,832 B** (< 7 MB, D5 rebuild, 2026-11-13), 8 pages, sha256 `b6d87852dc940c6eb0cacc98727d32781b31a07fae1a10a9364ee4a14053210b` — supersedes the post-proofread-fix value 3,092,430 B / `a775b191…`.

## Proofread record

- Builder's own full pass (this build): all 8 pages read end-to-end in text dumps; all 150 keys re-derived via the registry-level diff above; totals/levels equal the core; P7 verbatim/occurrence check passed; calendar re-verified; Champi open-forecast status confirmed; Italian layer read in full (582 extracted Latin-script lines) — consistent, complete, no Chinese residue (ideograph scan of the 8 SVGs: zero Han characters).
- **Independent proofread: PASS** (2026-10-21, independent proofreader; full record below). No repo insert, no Discord — delivery is the parent's call.

### Independent proofread record (2026-10-21)

**Verdict: PASS** — one complete independent pass over the final artifacts found ONE real defect (below); it was fixed in the explanation layer only and the ENTIRE pass was then re-run from the top on the final artifacts with zero remaining problems.

**Defect found & fixed.** P1 search-heat box: the Italian gloss «Queste quattro parole sono i temi della settimana.» (430 px at 18.5 px) wrapped to two lines inside the 390 px wrap width; its second line «settimana.» (baseline 1209.5) collided with the fixed source line «자료: Google 트렌드 한국 (10월 17일)» (baseline 1216) — pixel proof on the shipped card: one merged ink band, rows 1198–1220, where two lines should be (the core's one-line Chinese gloss never wraps, so the core is clean). Fix (Italian wording only, no geometry, no Korean, no keys): gloss replaced with «Quattro parole: i temi di questo numero.» (345 px, one line) in `hidden_files/weekly-report-ko-it-build/content12.py`, edition re-rendered. Post-fix pixels: four separate ink bands (gloss ends row 1188; source lines 1201–1220 and 1230–1247). Only P1's SVG changed (sha `3485150b…` → `c7d9afc4…`); pages 2–8 byte-identical to the builder's; rebuild warnings 0.

**Freeze vs the KO core: PASS.** Source-level diff of both builds (every hunk classified) + rendered-text comparison: all differences are explanation layer (glosses, notes, instruction lines, exercise type labels, clinic/frame/letter explanations, P8 notes, H instruction), pairing furniture (badge, footers, band halves, subtitle edition label, «Pagina N di 8», «Nota — » prefix), or the documented registry items below. No undocumented Korean-text change. Han ideographs in the edition's 8 SVGs: **0** (core: 1,976, its Chinese layer, fully replaced). Baseline verified: a scratch copy of the unmodified core build reproduced all 8 shipped core SVGs byte-identically, and the (fixed) IT build likewise reproduces all 8 final edition SVGs byte-identically.

**Keys (all 150 independently re-derived from the Korean text while reading all 8 pages).** Registry diff vs the core is EXACTLY {137, 138, 150}: #137 key → «La traiettoria del tifone può ancora cambiare.», #138 key → «Mancano 29 giorni all'esame.» (both faithful to the printed Korean stems «태풍의 경로는 아직 바뀔 수 있어요.» / «시험까지 29일이 남았어요.»), #150 apparatus Italian. Stems #139/#140 re-aimed in Italian («Nel fine settimana, controlla le previsioni più recenti.» / «Venerdì vado al Parco Haneul a vedere l'erba argentata.») with their Korean keys byte-identical to the core. The other 147 keys are byte-identical; all 150 notes rewritten in Italian, none empty.

**Printed-note sets.** Extracted by number from both shipped P8 SVGs: core printed set = {1..150}, edition printed set = {1..150} — **EQUAL**, both complete and in order, dash style `N. key — note` as in the core. Joined entries match the registry `key — note` verbatim for 149/150 in BOTH editions; #150 is the model-pointer line by design in both («✓ Il modello è nella sezione H di questa pagina (162 caratteri)»).

**Totals.** 150 exercises (A2 57 · B1 66 · B2 27); per page 10/18/18/18/18/18/12/38; writing model 162 chars. P7 phrases: all 8 verbatim-contiguous on their tagged pages (1면/1면/2면/2면/3면/4면/5면/6면) with per-phrase occurrence counts EQUAL to the core's: 4/2/2/4/2/2/2/2.

**Calendar (verified with `date`, Asia/Seoul).** CSAT Thu 2026-11-19 ✓; Oct 21 → Nov 19 = exactly 29 days (D-29 ✓); G5 Fri Oct 23 ✓; playoff Sun Oct 25 ✓; Korean Series Mon Nov 2 ✓; festival last day Fri Oct 23 ✓; Oct 20 Tue / Oct 21 Wed ✓. Champi remains an OPEN forecast in the text (landfall explicitly undecided; path «아직 바뀔 수 있어요»).

**Geometric occlusion audit (proofreader's own implementation).** Paint-order SVG parse, PIL real-font glyph metrics (Noto Serif/Sans CJK KR + UnifrakturMaguntia), ink band = baseline −0.88em…+0.30em, shape boxes expanded by half stroke width; validated on a synthetic positive control BEFORE the real run (control produced exactly the 4 planted flags: COVER 100%, LINEX, FOOTER, EDGE; a clean in-box text was not flagged). Final run on all 8 edition pages + the core as reference: **0 COVER, 0 LINEX, 0 FOOTER, 0 EDGE**. Remaining model flags, all adjudicated NOT defects: (a) BOXSPILL hits on exercise numbers vs the 60 px level chips beside them (numbers sit right of the chips by design) and chart/table labels — geometrically identical in the core; (b) TEXTX P1 masthead vs subtitle (band model overestimates the blackletter face): pixel-measured ink bottom 265 vs subtitle ink top 295 = 30 px clear, identical in the core; (c) a near-miss sweep (band gap < 6 px, horizontal overlap > 0) was run over every text pair and each class pixel-adjudicated — P8 answer-flow wraps are separate ink bands with clear whitespace rows; the P2–P8 dark-band masthead vs gold subtitle measures 13–16 px of real clearance (colour-separated pixel test); headline/credit wraps are frozen core geometry with positive real gaps. The pre-fix run of this same audit is what caught the P1 trend-box collision above (the builder's audit had missed it).

**Builder's claimed fixes — pixel-verified on the shipped cards.** P1 badge text ink rows 378–393, inside its band ✓. P1 trend-source line shortened («KoreaTrendBoard (10월 21일) · Valori appross.», 17 px) ✓, and after the gloss fix its two lines sit clear of the gloss and the box bottom. P2 D-day box title «「D-데이」 사용법 · L'uso del D-day»: ink x 545→921.3 inside the box (527–961) ✓. P2 D-day memorise sentence ink ends row **1795** vs the rule at 1803–1804 ✓ (the core's adjudicated adjacency, unchanged). P7 VOL.2 teaser ink ends row 2522 (builder said 2523; 1-row measurement difference, immaterial), clear of 2540/2580 ✓.

**Images & credits.** Embedded payloads byte-identical to the core per page (counts 1/1/2/1/2/1/0/0); every printed credit matches a placed image and the core KIT (NASA PD, Gary Todd CC0, Keibun PD, Cézanne PD, Bain PD, US Army PD, Elijah Flores CC0, lumoplank CC0) ✓.

**Banned-term scan.** The intermediary-layer term (Chinese and English forms): 0 occurrences in the paper SVGs, this KIT, and the operative build code (re-scanned after the fix) ✓.

**Final PDF pins (supersede the builder's).** Web `Lucerna-VOL1-IT-web.pdf`: **3,092,430 B**, sha256 `a775b1918573376279b426602ad272cc3258257d03a2da4e321fa69aba634818`, 8 pages, < 10 MB ✓. Print `Lucerna-VOL1-IT.pdf`: **34,450,127 B**, sha256 `0817b807136809f077a29a2ab7dd359ebe96c868ff9d94cb20e9e105728914c7`, 8 pages. (Builder's pins — web 3,092,612 B / `c91bdaf0…`, print 34,450,138 B / `7cd878ab…` — were verified accurate for the pre-fix artifacts and are superseded by the fix.)

**Core integrity.** The frozen core was never edited; its 8 shipped SVG sha256 are unchanged at the end of this work (p1 `f7db1604…`, p2 `f38afa34…`, p3 `f5a258a4…`, p4 `6ceb1f22…`, p5 `0adf32b9…`, p6 `e5e849ad…`, p7 `d8219859…`, p8 `bd3b245f…`, identical to the values recorded at the start of the pass).

## D5 rebuild (2026-11-13)

D5 rebuild (2026-11-13–14；builder：W43 ko 家三任；不 commit、不 push；独立重校另派他人；入仓由 closer 做）。D5 报告：`production/notes/2026-w43/g-ko/scratch-d5-rebuild-ko/D5-REPORT-2026-w43-ko-it.md`；门禁日志：`hidden_files/d5-redo/scratch-2026-w43-ko/logs/2026-w43-ko-it-run2/GATES-SUMMARY.txt`。

- 装机：移植模板 `tools/mechanism-w47/svglib-ko-d5.py`（539 行）原样装为版内 `svglib.py`，仅改写 `_D5_READER = "latin"`；core-ko 落盘同模板（`production/2026-w43/core-ko/svglib.py`，+333/−40）。路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 保留（`_QUOTE_CLS` 在位）。ko-ru 无 fix-xru（W43 重建标准，见家族报告 §0）。
- 基线：`run.py` TOTAL 150、0 警告（fr 例外：基线唯一警告为 port 已知良性 HEAD TOO WIDE，见 D5 报告 §二）；修前普查 D5 拉丁 427、西里尔 0、弯引号在 CJK 0；基线印 PDF 34,433,754 B、sha256 `0b62babae16171b10d7bc43a38364a3f656a88dd945b1ee73a6e20e74738d531`；基线网 PDF 2,105,460 B、sha256 `2a9f774619a31cad0cc2b80dffe512d0d43dd06b9b876b73e3945e92c3b3b69a`。
- 缺陷与修复（只动字号，文字内容未动）：
- run1 无真缺陷；唯一 FAIL 为门 17 缺脚本 SKIP（production 与 fanout 均无 `audit_ko_it.py`），不是 FAIL，不阻塞。
- 门禁 run2：PASS=18 FAIL=1（run1：PASS=18 FAIL=1）。run TOTAL 150；head_check PASS 0 defects；d5 census 0/0/0；render RC=0；webpdf RC=0（2006832 B <7MB）；occlusion 0；p8 extract 150/150；p8 compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8；freeze diff vs base 新增 CJK 0；spill 0；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0 defects（ratios n=379，中位 1.011，粗体 1.04，常规 0.995；P8 228→229 行，距页脚线余量 48.9px）；文字层 print=web 多重集差 0（各 29095 字符）；census_quotes 0 defective；D18 刊头间距 GAP=325.3；门 17：SKIP（无此脚本）。
- 新交付物（实测发运值）：印 PDF `Lucerna-VOL1-IT.pdf` 32,292,387 B、sha256 `7c6d7395db0728b5602a8802dea98c557c55970617d9e5cf744a8eb130c9a228`；网 PDF `Lucerna-VOL1-IT-web.pdf` 2,006,832 B、sha256 `b6d87852dc940c6eb0cacc98727d32781b31a07fae1a10a9364ee4a14053210b`（<7MB，待 closer 换入 `issues/2026-w43/2026-w43-ko-it/2026-w43-ko-it.pdf` 并更新 pin）；新建 text.md `2026-w43-ko-it.text.md` 21,701 B、sha256 `4f514c9328fccc890215035fd7e95e29d970a6f945e3c22b78c07ce9430eeab9`，与 fanout `.text.md.new` BYTE-IDENTICAL，`verify_textexp_ko.py --edition` ADOPT。
- KIT 旧值（印 34,450,127 B / 网 3,092,430 B，校对修复后终值，旧配方）已过期——基线实测印 34,433,754 B。本节交付物行已更新为上述 D5 新值。
