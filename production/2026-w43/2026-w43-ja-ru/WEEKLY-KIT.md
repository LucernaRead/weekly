# WEEKLY-KIT — JA×RU (Japanese body × Russian explanation layer)

- **Edition:** Lucerna Japanese Weekly VOL.1 — W43 (2026-10-19 – 2026-10-25), reader-native = Russian.
- **Status: PENDING** (builder complete; independent proofread + repo insert by the main line).
- **Source core:** `files/weekly-report-ja-vol1/` (in-repo core slug `2026-w43-ja-zh-cn`), build copied from `hidden_files/weekly-report-ja-build/` **after** the core's P7 seam patch.

## 0. Patch verification (hard precondition)
- Core `svglib.py` md5 BEFORE copying: **d73e23b365676c3618d7e060b835eb4d** (= SEAM_SLACK=28 patch) ✓ verified again in the RU build copy at close-out: same md5.
- Noto CJK faces verified to contain Cyrillic glyphs (PIL mask test); no font change needed (same as the RU-core line).

## 1. Baseline (freeze.py)
- Copied core build reproduced the shipped core SVGs **8/8 byte-identical** before any edit.
- Core SVG sha256 prefixes (unchanged at close-out): p1 db328eb8 · p2 ef09afeb · p3 07e44381 · p4 01ade8a4 · p5 403dd3db · p6 8a92c611 · p7 c7f0e380 · p8 355de22c.
- Build discipline: one-process driver (`run.py`); no module ever run standalone in the copy (README #11); `bridge()` renamed to `expl()` (def + 22 call sites).

## 2. Transform
- Literal, count-asserted replacements: **500 across 6 files**, every count derived from the pristine core files; abort-on-mismatch (log: build `scratch/transform-log.txt`).
- 6 hand fixes after the first audit (see §6). Totals: **150 = A2 48 · B1 75 · B2 27**; pages 10/18/18/18/18/18/12/38.
- freeze.py diff `--strict-cjk`: **added CJK = 0 on all 8 pages**; CJK totals fell (explanation layer Chinese → Russian); all 297 removed strings classified: explanation layer / furniture / wrap fragments only — **zero Japanese body text removed** (removed strings containing kana with length >12: 0).

## 3. Furniture (RU column standard, per FR×RU KIT §3 + EN×RU KIT §3 target-name table)
- P1 badge (19px sans bold, brick, centered, inserted y=356 after the NL-precedent masthead reflow): «ТЕКСТЫ НА ЯПОНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ»
- Footer (every page): «Lucerna · ЯПОНСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.1 · ТЕКСТЫ НА ЯПОНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ» (Japanese takes no article; masthead = Lucerna)
- Page line: «Страница N из 8»
- Gloss prefix: «Пояснение — » (10 gloss boxes: P1 ×1, P2 ×2, P3 ×2, P4 ×2, P5 ×2, P6 ×1)
- P8 separators: «— СТРАНИЦА N —»; P8 answer header: «Ответы — сгруппированы по страницам: ищите свой номер»
- P7 phrase page tags: «(Страница N)» — distribution (1)×2, (2)×2, (3)×1, (4)×1, (5)×1, (6)×1 = core
- Bilingual heads = Japanese original · Russian short form (e.g. band subs, «あなたは？ · А вы？», chart head «グラフを読もう · Читаем график», PRACTICE DATA tail «練習用データ · Учебные данные»); P4 band title «スポーツ · 体育» kept (体育 is Japanese).
- Russian number style in notes: decimal commas, thousands with a space (e.g. «штраф 2 000 иен», «62 = 34 + 28 = 62» style sums kept as printed by the core's arithmetic).
- Sommaire keeps Japanese «N面» labels; only the «全部» level word → «ВСЕ» (NL precedent).

## 4. Key discipline (registry = authority)
- Core P8 style established from core SVG + code first (README #8): JA core prints **all 150 notes**, dash style `N. key — note`, writing items `N. ✓ note`, no filtering rule → the edition keeps the core answer-generation code unchanged, forcing the full set.
- `p8.py compare`: **CLEAN 150 = 150**, missing = [], extra = 0. Extractor keydiff list [7, 12, 22, 29, 65, 78, 83, 95, 101, 113, 115, 117, 119, 120, 137, 138, 140, 146, 147] — line-parse artifacts of note translation (README #13 class), disproven by the registry diff.
- **Registry diff (authoritative): key diffs exactly {137, 138, 150}** — the two translation items + the #150 writing apparatus:
  - 137 key → «Процессия отправляется в 12 часов из Киото-Гёэн.»
  - 138 key → «За брошенный мусор — штраф 2 000 иен.»
  - 150 key → «(открытое задание — образец ниже)»; note/expl apparatus in Russian; printed char count **150 знаков** (model essay counted independently = 150 chars, Japanese frozen).
- Stem edits (translation-direction items, bodies): 139 «Неделя чтения начинается в следующий вторник. → ___», 140 «Я хочу на хэллоуинское событие в Икэбукуро. → ___»; keys of 139/140 stay the Japanese sentences (frozen).
- All 150 notes are Russian (incl. notes that were Japanese in the core); Japanese words cited inside Russian notes are quotations of the body text (registered here per the KO-column citation precedent): e.g. #16–17 keys 見頃/紅葉狩り with Russian notes; clinic/gothrough items quote Japanese example sentences verbatim from the body.
- P7 phrases: all 8 Japanese quotes byte-identical to the core; each occurs exactly **2×** in the full issue (article + deck), core = edition; translations in Russian with «(Страница N)» tags.

## 5. Mechanical gates
- `occlusion_audit.py` (selftest OK first): first run 6 NEW flags → fixed (§6) → re-run **0 flags, NEW vs core = 0**. Core itself: 0 flags.
- Same-line ink scan (build `scratch/rowcheck.py`, README #10): 7 pairs flagged, **identical 7 in the frozen core** with identical metrics — band wordmark/sub stacked baselines; pixel-adjudicated on rendered cards: wordmark ink rows 89–115, sub ink rows 126–142 (core) / 126–146 (RU), 10 clean rows between → scanner artifact, not a defect. All other same-line clusters (incl. the new P1 badge line y=356 and sommaire rows) collision-free.
- Chart elements (README #12): P6 rect tuples **byte-identical** to core (bars 34/28/22/16 = 100); head «グラフを読もう · Читаем график» and right label «練習用データ · Учебные данные» element-checked clear on the same line.
- Kinsoku: transform touches no Japanese body string; wrap fragments in the freeze-diff removed list are explanation-layer only. P7 level-column text re-wrapped by the patched lib identically (see §7).
- Images: `<image>` payloads byte-identical to core on all pages (counts 1/2/1/1/1/1/0/0).
- Residue scans: Chinese explanation residue = 0 (freeze-diff attribution); Dutch residue = 0 («Pagina»/«Uitleg»/«WEEKBLAD» = 0); banned term = 0 in paper SVGs, this KIT, and operative code (`.bridge(` count = 0 after rename). Confined exception: build `scratch/transform_ru.py` quotes the old call string as a search pattern only.
- Calendar vs real 2026 (Asia/Tokyo), all verified programmatically: Oct 17 Sat · 20 Tue · 22 Thu · 23 Fri · 24 Sat (Japan Series G1 18:30, DeNA vs SoftBank) · 25 Sun · 27 Tue (Reading Week starts; ends Mon Nov 9) · 31 Sat (Halloween).
- No international politics anywhere in the explanation layer.

## 6. Defects found in self-proofread & fixed (6 hand fixes, all width-measured with the build's own text_w)
1. P1 search-box data note overflowed its box/page (ink to x=2051) → shortened to «Приблизительные данные на 17 октября.» (384.8 ≤ 390).
2. P2 box title «『見頃』の使い方 · Как употреблять «見頃»» crossed the box border (483.6) → «『見頃』の使い方 · Употребление» (376.6).
3. P2 match instr ran off-page in col 3 → «Соотнесите место и дату» (235.3).
4. P3 match instr crossed the col2→col3 gutter (342.4) → «Соотнесите пары событий» (252.5).
5. P4 box title «… · Расписание серии» crossed the box border (443.9) → «… · Расписание» (368.9).
6. P8 match instr overlapped the #150 writing body in the next column (TEXTX 18.0×11.9) → «Соотнесите пары слов» (214.7).
- After fixes: full visual pass over all 8 rendered cards — Russian natural throughout, every gloss glosses a word on its own page; zero remaining problems.

## 7. P7 seam re-measurement (patched-core calibre)
- Rendered-card gutter scan (ink-gap between level columns, rows 322–392): A2|B1 min gap **32px** (y=358), B1|B2 min gap **32px** (y=333) — **identical values in the core and this edition**; no overprint (patched clearance preserved; NL precedent range 26–31px by band choice).

## 8. Deliverables (measured pins)
- `files/weekly-report-ja-ru/`: svg ×8, cards ×8, this KIT.
- Print PDF `Lucerna-VOL1-RU.pdf`: **37,928,127 B**, sha256 `7ef477c7e8dd063ea060d92d52c3ad2050259f03e8bfdaac3871cd0f38ecb19d`
- Web PDF `Lucerna-VOL1-RU-web.pdf`: **3,231,054 B** (< 10 MB), sha256 `3ede999afccfbc4f007b766cfd6261095f21b0e0df4182936c4f71692c37480a`
- Not inserted, not posted — insert (slug `2026-w43-ja-ru`) by the main line after independent proofread.

---

## D5 rebuild (2026-11-13)

SOP §1.1 字体修复（D5）：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader；西里尔字母改走 Noto Sans；日文正文仍走 Noto Sans/Serif CJK JP。施工不 commit、不 push；入仓由独立重校后的 closer 做。工作日志：`hidden_files/d5-redo/scratch-2026-w43-ja/logs/2026-w43-ja-ru/`；逐版报告：`production/notes/2026-w43/g-ja/scratch-d5-rebuild-ja/D5-REPORT-2026-w43-ja-ru.md`。

**装机**：移植模板路线（D5-METHOD §1.7；安装器拒单已实测，见家族报告 §3–§4）。本版 svglib 取 `svglib-ja-d5.py`，`_D5_READER = "ru"`，与模板 diff 恰好 1 行（`_D5_READER` 一行）；旧 `_D5_READER == "ru"` 分支在位（拉丁 AND 西里尔 → Noto Sans）；`test_d5_routing.py` FAILURES: 0；旧分支路由探针 0 失败（拉丁→sans_noto、西里尔→sans_noto、fix2→news、CJK→sans）；fix2 + kinsoku 齐全。

**基线**：run TOTAL 150；SVG 8/8 与 fanout 相同；印 PDF 37,533,904 B；pdfdiff vs 已发件 IDENTICAL 8/8；修前普查 D5 拉丁 214。

**D26 纠正（2026-11-14）**：Q4 原裁定（以安装器输出为准、即 fix-xru 态）已被协调员 D26（2026-11-14 ~04:30，PLAN Amendments）取代——W43/W45/W46 的 ru-reader 版一律用安装器态旧分支；fix-xru 仅属 W47，不带入三周重修。证据：(1) 安装器正典代码 `tools/mechanism-w47/apply_variant.py` D5_BLOCK（L96–108）写明 `_D5_READER == "ru"` routes Latin AND Cyrillic to Noto Sans；(2) SOP §1.1 L64 字体表“俄语读者用 Noto Sans”，L67 Newsreader 无西里尔字形；(3) W43 已入仓并独立重校通过的 en-ru、es-ru 均为旧分支。Q4 所据前提是错的：安装器并不输出 fix-xru。本版 2026-11-14 按 D26 重装（模板 + `_D5_READER="ru"`）+ 重建 + 重门禁；原 fix-xru 态作废。

**run1→run2 缺陷与修法**：D26 重建 run1 出 2 门新红，同根——P2 餅图注 credit「写真：Fumikas Sagisavas — CC0（Wikimedia Commons）」在 Noto Sans 下宽 424.8px、超 CW 422.5，贪心断行 + kinsoku 尾字下移致「Common / s）」两行（15c HOLD）；图注多 1 行致“あなたは？”框下移 20.15px，末行俄语墨盒顶 1553.8 触季节横线 y=1554（occlusion LINEX 1 旗）。修法（只动字号，未动文字）：仅该图注 credit 字号 15.5→15.0pt（实测 411.2px，复归一行；`bslib4.py` 的 `caption()` 加 `credit_size` 参数默认 15.5，`content12.py` 餅图注调用传 15.0；余 6 处 caption 调用不动）。其余 4 条长 credit（Bain/Hersom/Kratochvil 等）基线即 2 行、布局已计入，不动。run2 全量重建 + 全部门重跑。

**门禁（run2）**：17 门 + D18 中 16 门 + D18 全绿——run 150 / head_check 0 / d5 census 0（noto_sans_elements=745）/ render RC=0 / webpdf RC=0（2,697,920 B）/ occlusion 0 / p8 extract 150/150 / p8 compare CLEAN（keydiff [137, 138]）/ freeze baseline 8/8 / freeze diff 新增 CJK 0（新增拉丁 strings TOTAL 89，run 拆分）/ spill 0 / boxtitle 0 DEFECT / edge 0 TOUCH 0 NEAR / creambox PASS 0 defects（P8 237→238 行，slack 49.4px）/ print=web 文字层差 0 / census_quotes 0 defective / 刊头间距 266.0px PASS。门 15b `verify_textmd.py` carryover FAIL 为工具-格式口径差（基线同跑亦 FAIL；D27 裁定：权威证据为 ja 原生校验器 `verify_textexp_ja.py --edition` ADOPT，0 UNEXPECTED）。

**新交付物（run2 实测值）**：印 PDF `Lucerna-VOL1-RU.pdf` 37,658,315 B / SHA-256 `bfbd7b5aad026a8bb1c5ae44e79edeea9f22b9c982117336463a2bea34ecf278`；网 PDF `2026-w43-ja-ru.web.pdf` 2,697,920 B / SHA-256 `d6373f0c2316c5225794f5faae0ba833a48ac7d4c4ffad5bff6b513d5a625c53`（D5 前已发版 2,627,129 B，`29d162d735b1…`）；text.md **新建** 54,776 B / SHA-256 `d71da6d92f3e8c1689e40e2d41ec880deabcc156c5531257d75a7d14fb804f25`。（run1 fix-xru 态旧值作废：印 37,584,200 B / `fb3ad433…`、网 2,624,973 B / `f42fbcd4…`、text.md 54,775 B / `93be6414…`。）
