# 校对笔记 — 2026-W47-ja-nl（第二轮独立复校，叶子）

- 版：`2026-w47-ja-nl`（目标语日语 × 读者母语荷兰语，VOL.4，刊期 2026-11-16–22）
- 校对员：叶子（第二轮独立复校，与 builder / 核心 builder / 第一轮复校员 / 第一轮返修员不同人）
- 日期：2026-11-11（UTC 08:22–08:31）
- 结论：**(a) 零问题 — 全量复校未发现缺陷，可按零问题定稿。**
- 红线遵守：只读了 `production/2026-w47/fanout-ja/2026-w47-ja-nl/` 与 `core-ja/`（p8 compare 比对用）；
  未碰 core-ja、W43–W46、其他目标语家庭、`tools/`；未跑 insert.py、lint --write；
  未 git add/commit/push/reset/stash、未改任何源码/成品。run.py 两遍重跑为任务要求的机械门，
  重跑前后 8 SVG 哈希逐字节一致（见 GATE-LOG.md），成品无改动。
- 依据：SOP.md §8 / §1.1 全文、`WEEKLY-KIT.md`、`EDITION-RECORD.md`、
  第一轮复校笔记 `scratch-proof-ja-nl1/PROOF-NOTE.md` + `GATE-LOG.md`、
  第一轮返修记录 `scratch-fix-ja-nl1/FIX-LOG.md` + `GATE-LOG.md`。
- 方法：印刷 PDF 重新渲染 8 页逐页目视（110 dpi 全页 + 200 dpi 局部放大，见 `render/`）；
  网页 PDF 8 页逐页渲染、P1/P8 目视；`2026-w47-ja-nl.text.md` 全文通读；
  150 题逐题验算（题干—正文—答案键三方核对）；金句 8 条逐字比对；
  P8 全部注文人名逐条核对公开来源（D2/D3 复核，见下）；机械门全套自跑（见 GATE-LOG.md）；
  日期星期全部用 `date` 核验；红叶预报数字用公开来源抽查核实（见“事实核实”）。

## 身份核对（先核身份，通过）

| PDF | 字节 | SHA-256（完整） | 与任务书 / KIT 登记 |
|---|---|---|---|
| 印刷 `Lucerna-VOL4-JA-NL.pdf` | 29,099,141 | `c8b82a8491a0d4c54a01214806cede29188e8f4bf6c81c6cf8a1b3bd5ceafa56` | 逐字一致 |
| 网页 `Lucerna-VOL4-JA-NL-web.pdf` | 4,476,527 | `7a7f5fc96730e82ba8c6697a9accd10387d6aa84a731f81fe3083310df0f97b8` | 逐字一致 |
| `2026-w47-ja-nl.text.md` | 45,627 | — | 字节与任务书一致；行数为 1377（见观察项 O9：KIT 称 1378，属 KIT 计数误差，非成品问题） |

双 PDF 各 8 页。身份相符后方动手。

## 第一轮缺陷修复复核（D1/D2/D3 全部确认已修）

### D1（中）— P2「11月のことば」两条荷兰语释义溢出词框 → 已修，目视确认

- 200 dpi 放大渲染（`render/p2-words.png`）：四格释义均单行、完整在米色框内——
  熊手 `een bamboe hark voor voorspoed`、手締め `vieren met geklap`、
  解禁 `de dag dat de verkoop begint`、小雪 `wanneer er een beetje sneeuw valt`；
  下行例句「文で覚えましょう：『19日に、浅草で熊手を買います。』」清晰、无贴靠。
- SVG 几何：4 格词条框基线同为 y=1752.06（框内，底缘 1768）；旧溢出行基线 y=1776.76 出现 0×。
- 旧释义精确串 `een bamboe hark voor voorspoedige zaken` / `wanneer er een beetje sneeuw begint te vallen`
  在 content*.py、svg/、text.md 中 0×；新释义与 P8 注 16/25/28/141 一致。
- 释义缩短未改原意：`voorspoedige zaken`→`voorspoed`（兴旺）、删 `begint te`（开始下→下），均保留原意。

### D2（高）— P8 注文 `Fujiryūga` 5 处 → 已修，逐处确认

- 全版复扫：`Fujiryūga` 在 content*.py、svg/（8 个）、text.md、双 PDF 文字层中 **0×**；
  `Fujiryōga` 在 P8 SVG 中 **5×**。
- P8 答案区 200 dpi 放大（`render/p8-answers.png`）+ 印刷 PDF 文字层逐行确认：
  49 `Fujiryōga versloeg Hōshōryū op dag 3`、54 `Kinboshi van Fujiryōga: 11e toernooi sinds debuut`、
  63 `Fujiryōga won een kinboshi op dag 3`、111 同 54、116 `Hōshōryū verloor op dag 3 van Fujiryōga`。
- 47 `Yoshinofuji versloeg Ōnosato op dag 1` 未动，正确。

### D3（高）— P8 注文 `Umi-no-umi` 1 处 → 已修，确认

- 全版复扫：`Umi-no-umi` 在 content*.py、svg/、text.md、双 PDF 文字层中 **0×**；
  `Chura-no-umi` 在 P8 SVG 中 **1×**：48 `Chura-no-umi verloor op dag 1 van Hōshōryū`（200 dpi 放大 + 文字层均确认）。

## 已核实无问题的要点（全量结论，非抽样）

- **150 题逐题验算**：编号 1–150 连续无缺重；分版 10/18/18/18/18/18/12/38；
  级别 A2 48 / B1 73 / B2 29（与 KIT 一致，run.py 注册表复核）；
  题型 zinnen aanvullen 50 / meerkeuze 51 / combineren 12 / zinnen bouwen 8 /
  waar of onwaar 11 / gatentekst 13 / vertalen 4 / Schrijven 1。
  全部 150 条答案键逐条对照题干与正文/图表验算无误（含图表算术 38−24=14、38+24=62、
  38+24+22+16=100；范文去空格计 154 字符，与注文“154 tekens”相符）。
  练习小节头一律日语，无 tr-en 式英译残留；题型标签均为荷兰文。
  p8 extract 的 150 键与第一轮复校 `proof-p8.json` 的 150 键逐键比对——**0 差异**；
  p8 compare CLEAN，keydiff 仍恰为 [137, 138, 139, 140]（E 组荷兰文翻译答案，逐条核实正确，同第一轮）。
- **日期星期**：`date` 核验 2026 年日历——11月5日周四、11月7日周六、11月8日周日、
  11月13日周五、11月19日周四、11月21日周六、11月22日周日、11月23日周一、12月1日周二——
  与全文所有星期标注一致，无一错。
- **事实核实（本轮新增公开来源抽查）**：相扑 3 日战绩与第一轮核实的报道一致，未变。
  红叶预报：ウェザーニューズ 2026-10-29「第3回紅葉見頃予想」公开报道确认——
  高尾山 11月13日ごろ、宮島 11月21日ごろ、嵐山 11月23日ごろ（与 P6 正文一致）；
  日本気象協会嵐山 11月13日から——第三方指南引 tenki.jp 2026-10-28 第3回予想确认一致（与 Q86 答案一致）。
  P6 嵐山 spot 页的 11月26日 / 落葉はじめ 12月12日 两数见观察项 O10。
- **金句 8 条**：逐字比对正文——7 条逐字出自 P1–P4 新闻正文且页码引用准确（第 6 条见观察项 O1，
  与第一轮相同）；荷兰语译文 8 条均准确。
- **讲解/界面语言**：确为荷兰文（页脚、页码行、各栏标题/注释/披露/预告/答案注文）。
  荷兰语通读无硬伤（见 O2 两处小疵，与第一轮相同）。
- **CJK/源语字面量转写**：核心日文原文冻结（与 core-ja 比对：p8 compare CLEAN；
  `ryuuryuu`、`Chiikawa` 如裁定）。
- **中文残留**：0。标记词 `吉伊卡哇`/`参考答案`/`酉之市`/`提名`/`说说你自己`/`每周一期`/
  `日语周报` 在 SVG + text.md + content*.py 全 0×；
  以“们/这/那/就/都/还/没/很/能/会/让/给/说/的/是/在/了/吗/呢/吧/啊/对/为/从/过/得”
  扫 text.md 得 25 行，逐行核实均为日语固有词（京都、会社、会場等），与第一轮相同。
- **U+2019**：8 SVG + text.md + content*.py 全 0×。撇号均为直撇号 U+0027。
- **VOL**：`VOL.4` ×10、`VOL.3` ×1（P4 前号注，正确）、`VOL.5` ×3（grep；第 4 处分属两个文本节点，
  见第一轮 O4）、`VOL.2` 0×。无错印。
- **图片来源**：5 图署名与 `assets/CREDITS.md` 一致（P1 maple — Poliphilo CC0；
  P3 beaujolais — Alainauzas 公共领域；P5/P8 Arashiyama — lumoplank CC0；
  P7 tori — Mozzucu CC0，注“2025年11月24日照片”）；P4 无图如 KIT 所述。
- **禁词**：国际政治类扫描 0 命中（ウクライナ/乌克兰/戦争/战争/ガザ/プーチン/トランプ/
  ミサイル/核兵器/台湾问题/南シナ海）。
- **P8 人名逐条核对**：Yoshinofuji ✓；Ōnosato ✓；Hōshōryū ✓；
  Miura Riku / Kihara Ryuichi ✓；Fujiryōga ✓（已修）；Chura-no-umi ✓（已修）。
- **ABSTRACT.txt**：单行、荷兰文、无 ASCII 双引号，含刊名、目标语、A2–B2 与 150 题，事实取自本期内容。
- **§1.1 版式 grep**：`·` 0×；旧纸色 `#f7f1e2` 0×；纸色 `#fbfaf6` 每版 1×；
  `Pagina N van 8` 每版 1×；P8 最小字号 9.98pt（≥9.75pt 门槛）。

## 观察项（不计缺陷，沿用第一轮 O1–O5，并新增 O9–O10）

- **O1 — 金句第 6 条出处（沿用）**：「『りくりゅう』は、フィギュアスケートのペアです。」
  逐字出处仅为 P7 自身 B1 栏，P5 课文相应句句式不同。第 6 条引注 (p. 7) 属实；
  该句为冻结核心文本，改动与否须核心层定夺，列观察不计缺陷。
- **O2 — 两处荷兰语小疵（沿用，意思可懂）**：P8 注 55/112
  `De 7e snelste kinboshi sinds de zes toernooien per jaar`——`sinds` 后宜接时间点/事件；
  注 86 `Weervoorspelling Japan: Arashiyama vanaf 13 nov.` 为电报体简写。均为答案注简写体，不影响理解。
- **O3 — 核心继承的版面现象（沿用，非 fan-out 缺陷）**：P1 趋势盒第 1 条末字「敗」单独换行；
  P4 栏顶「5) でお知らせします。」跨栏续接；P2/P3/P5 栏中大面积留白；
  P8 栏头徽章顶缘 y=180 与深绿栏条底缘 y=182 有 2px 交叠（视觉为相接，与 core-ja 一致）。
- **O4 — KIT 的 VOL.5 计数不准（沿用，非成品缺陷）**：KIT §1 称 VOL.5 出现 3×，
  实测 4×（P4 正文、P4 底栏横幅、P7 读者园地披露、P7 下期预告头）；其中 P4 正文一处分属两个文本节点，
  故字串 grep 只命中 3×。四处均为合法下期预告，无错印。
- **O5 — 核心注 47 的汉字笔误（沿用，nl 本身不受影响）**：core-ja P8 注 47 中文写“一之富士”，
  与正文及公开报道“義ノ富士”不符；nl 版注文用罗马字 `Yoshinofuji`，正确。请协调员知会核心线，nl 无需改动。
- **O6 — 备忘与盘上实测出入（沿用，第一轮已说明）**：盘上唯一交付 SVG 仍带两处错拼的是修前 nl 版，
  修后已清零；en/de/fr/es/pt/it 版 SVG 均为正确拼写。
- **O7 — FANOUT-REPORT-ja.md（沿用）**：第 8 棒重建、只含第 8 棒实测，前棒章节缺失。不影响本次校对。
- **O8 — 工作树既有修改（沿用，与本次无关）**：`git status` 显示 `issues/2026-w43/` 下有已修改的已跟踪文件，
  mtime 早于本次开工；本次未碰仓内其他目录。另：本版目录在 git 中为未跟踪（`??`），
  系 clone 现状，非本次造成；run.py 两遍重跑前后 8 SVG 哈希 8/8 一致，未改任何成品。
- **O9 — KIT text.md 行数计数差 1（新增，非成品缺陷）**：KIT §7/§8 与 fix1 GATE-LOG 称 text.md 1378 行，
  实测 `wc -l` 与 Python splitlines 均为 1377 行（文件以换行结尾）。字节 45,627 与任务书一致，
  fix1 的 12 行 diff（修前 1379 → 修后 1377，恰为两条释义并行各减 1 行）对得上；
  1378 系计数口径误差。请协调员顺手改 KIT，不必为此重渲染。
- **O10 — P6 嵐山 spot 页数字未能复验（新增，核心层事项，非 nl 缺陷）**：P6 正文称
  「ウェザーニューズの嵐山のページでは、見頃は11月26日ごろから、落葉はじめは12月12日ごろから」。
  本轮用公开来源确认了同段的 10月29日第3回予想三数（高尾山 13、宮島 21、嵐山 23）与日本気象協会 13 日，
  但 spot 页数字无法对当前 live 页复验——spot 预报每日更新（第三方 2026-11-09 查核显示该页嵐山为 11月23日頃，
  11月4日查核为 11月22日），拿不到 11月8日左右的页面状态，故既不能证实、也不能证伪 26日/12月12日。
  该句为冻结核心文本、12 版 ja  edition 共用，nl 无权擅改；且文章本意正是“预报因来源而异”，
  两数并列不构成自相矛盾。列观察，请协调员请核心线复核该处引用，不阻塞本版定稿。

## 证据文件（本轮校对，写在仓外 scratch）

`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ja-nl2/`
- `PROOF-NOTE.md`（本文件）、`GATE-LOG.md`
- `proof-run1.log`、`proof-run2.log`（run.py 两遍）、`svg-sha-pre.txt`、`svg-sha-run1.txt`、`svg-sha-run2.txt`
- `proof-occlusion.json`、`proof-occlusion.log`、`proof-p8.json`、`proof-p8.log`、
  `proof-p8compare.json`、`proof-p8compare.log`
- `proof-print.txt`、`proof-web.txt`（pdftotext，各 45,931 B，逐字节一致）
- `render/p-1.png`–`render/p-8.png`（印刷 PDF 重新渲染）、`render/web-p-1.png`–`render/web-p-8.png`（网页 PDF）、
  `render/p2-words.png`（D1 200 dpi 放大证据）、`render/p8-answers.png`（D2/D3 200 dpi 放大证据）、
  `render/p2hi-2.png`、`render/p8hi-8.png`
