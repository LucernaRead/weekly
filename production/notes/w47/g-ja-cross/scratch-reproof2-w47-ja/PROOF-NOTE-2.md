# W47 ja 家庭独立重校记录（第二轮，PROOF-NOTE-2）

- **校对员**：第二轮独立重校员（全新工人，与建造者、第一轮校对员、修复工人均不同；SOP §8/§8.4：修复后另派校对员从头全量重校）
- **日期**：2026-11-12
- **范围**：目标语 ja，11 版（core-ja = ja-zh-cn + 10 个 fan-out：ja-de/ja-en/ja-es/ja-fr/ja-it/ja-ko/ja-nl/ja-pt/ja-ru/ja-zh-tw）
- **结论**：**(b) 有问题** —— 仅 2 项 low 级发现，无 MAJOR、无 MEDIUM；机械门禁 11 版全绿。按 SOP §8.4，一整轮全量校对须零问题才算定稿，这 2 项 low 是否修、修后是否再走一轮重校，由父线裁定。本记录只校对、不修复。
- **硬约束遵守**：只在 `production/2026-w47/` 内读 ja 家 11 版生产文件，未改任何生产文件；未 commit、未 push、未跑 lint。解释器一律 `tools/venv/bin/python`。磁盘：`/home/hatch` 150G 盘已用 94G（<100G 门限）。全部产出在本目录 `scratch-reproof2-w47-ja/`，未覆盖第一轮 `scratch-reproof-w47-ja/`。
- **先读材料**：SOP.md 全文（重点 §8）、第一轮 `scratch-reproof-w47-ja/PROOF-NOTE.md` 全文、修复 `scratch-fix-ja/FIX-LOG.md` 全文，均已读完。

## 1. 校对文件指纹（校对的那份文件）

11 版印/网 PDF 与 text.md 的尺寸 + SHA-256 前 12 位（2026-11-12 实测），与 FIX-LOG「最终全量验证」所记改后值**逐版逐项完全一致**，校对期间生产文件未变。

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） |
|---|---|---|---|
| core-ja（zh-cn） | 25,973,509 / `0ce5e4b872ae` | 4,654,731 / `0f9098ff3bf0` | 44,432 / `55c570f1bd0e` |
| ja-de | 25,813,856 / `4283e8a74ff9` | 4,387,416 / `c24dfb09d7d0` | 46,520 / `0d8d1de78a06` |
| ja-en | 25,806,211 / `c6a15edb8a6c` | 4,379,966 / `0560f0e4ea85` | 45,706 / `fb5a4700d3c9` |
| ja-es | 25,813,986 / `258c04418960` | 4,387,623 / `0002d6fe1481` | 46,684 / `3ddce794e256` |
| ja-fr | 25,812,296 / `9d4c6114fb31` | 4,386,312 / `ef073db3df37` | 46,882 / `badb0a6e7d00` |
| ja-it | 25,807,661 / `1bfe06107634` | 4,381,297 / `db031afe2252` | 46,678 / `9b677d40100d` |
| ja-ko | 28,140,910 / `88b2bfc1d8b0` | 4,551,878 / `753d8b4a63ba` | 47,722 / `0fbf36dd4f76` |
| ja-nl | 25,805,479 / `d6f14754f22c` | 4,379,026 / `97ee26ba1616` | 45,627 / `7f8f6638e635` |
| ja-pt | 25,814,751 / `3cca426dcbec` | 4,388,490 / `a573debf0755` | 46,696 / `9c9609378189` |
| ja-ru | 25,970,343 / `04b2f315e267` | 4,540,808 / `0726eda64903` | 53,004 / `f934bcf1d9f4` |
| ja-zh-tw | 25,988,418 / `4b09db1088b8` | 4,789,292 / `649ac196e81a` | 44,361 / `77fb0f36c75b` |

## 2. 修复核实（逐版，D1 + D2）

每版 py / svg / text.md / 印 PDF 文字层 / 网 PDF 文字层五层分别计数。

| 版 | ryuuryuu（py/svg/text/印/网） | rikuryuu（py/svg/text/印/网） | ja-ko D2 |
|---|---|---|---|
| core-ja | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-de | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-en | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-es | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-fr | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-it | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-ko | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | 우미노우미 0 / 츄라노우미 1（text.md 第 1246 行 `48. B — 츄라노우미는 1일째에 호쇼류에게 졌어요`；py/svg/印/网各 1 处） |
| ja-nl | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-pt | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-ru | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-zh-tw | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |

**结论：D1 修复 11/11 落地（每版 5 处：P7 金句 gloss 1 处 + P8 答案 66/77/80/105），D2 修复 ja-ko 落地。**目检印证：core-ja P7 印出「rikuryuu」是花样滑冰双人组合；ja-ko P8 印出 `48. B — 츄라노우미는 1일째에 호쇼류에게 졌어요`。其余版同类专名读音亦复核无误：美ノ海 en `Churanōmi`、de `Churanoumi`、fr/es/it/pt/nl `Chura-no-umi`、ru `Чура-но-уми`、zh-cn/zh-tw 汉字「美之海」；藤凌駕 ru `Фудзирёга`（属格 `Фудзирёги`、与格 `Фудзирёге` 变格正确）。

## 3. 全量通读（从头重校，非只查已修项）

- **core-ja text.md 全文 1356 行通读**：P1–P8 文章、练习、P8 答案逐题核对。P7 本周金句 8 条逐字核对与正文一致、页码引用正确（19日二の酉 P1、ボジョレー解禁 P1、熊手 P2、新酒 P3、両横綱 2勝1敗 P4、りくりゅう P7、紅葉京都 P1、酉の市 P2）。
- **10 个 fan-out 讲解层全文通读**：每版取与 core 的 diff 全量（fan-out-only 行：de 379、en 378、es 379、fr 380、it 381、ko 359、nl 380、pt 378、ru 385、zh-tw 287 行），逐行读完——家具、译注、题干说明、P7 金句 gloss、读者园地、P8 全部答案简析、137–140 翻译题译文。
- **答案键跨版比对（程序化）**：150 题答案键（字母/×○/数字/填空词）与 core 逐题比对，137–140 除外——10 版**全部一致**；唯一表面差异为 Q150 的范文指引句本身就是读者语翻译（例 en “Model text in section H…(154 characters)”），属预期。
- **题号连续性（程序化）**：11 版 Q 1–150 与 A 1–150 均齐全、无缺无重。
- **日期/星期（日历核验）**：11-03 周二、11-05 周四、11-07 周六、11-08 周日、11-13 周五、11-16 周一、11-19 周四、11-21 周六、11-22 周日、11-23 周一、12-01 周二——与正文所称星期全部一致；刊期 11-16 周一～11-22 周日正确；ボジョレー解禁 11 月第 3 木曜日 = 11 月 19 日正确。
- **算术复核**：P6 图表 38+24+22+16=100；Q91 差 14、Q92 和 62、Q93 合计 100；Q54/Q111 11 场所、Q55/Q112 第 7 快；范文 154 字（第一轮已精确计数，本轮复核 Q150 指引句 11 版均写 154 字）。
- **事实抽查**：P6 正文自身同时给出嵐山見頃两说（Weathernews 第 3 回予想 10 月 29 日：23 日；同社嵐山 spot 页 11 月 8 日更新：26 日ごろ、落葉はじめ 12 月 12 日）并注明是预报版本差，练习只用 23 日/12 月 12 日，无内在矛盾（第一轮 O1，本轮复核后不重报）。
- **ABSTRACT.txt**：11 版均有、读者母语、单行、无 ASCII 双引号，含刊名、目标语名、A2–B2、150 题与真实主题。
- **P8 最小字号（PyMuPDF 实测印 PDF 第 8 页）**：11 版均为 **9.98pt** ≥ SOP §1.1 底线 9.75pt。
- **text.md 与 PDF 一致性（全量，非抽查）**：印/网 PDF 逐页文字多重集 **IDENTICAL**（11 版 × 8 页）；text.md 全部有效行（去空白归一化）均在印 PDF 文字层中逐字找到，**缺失 0 行**。
- **目检**：渲染 core-ja P7/P8、ja-ko P8、ja-ru P7、ja-en P1（72dpi 全页）逐页看过：无溢出/重叠/压页脚/豆腐块/截断句；P7 底部照片条、P8 寺院图、P1 头版版式均在位。

## 4. 发现表

| # | 严重度 | 版 / 位置 | 内容与证据 |
|---|---|---|---|
| L1 | low | ja-ko，P7 本周金句 gloss（第 7 句） | 金句「紅葉の見頃は、京都へ移っています。」的韩语 gloss 写成「단풍 절기는 교토로 이동하고 있어요。」——절기（節氣）指二十四节气，用来译 見頃（最佳观赏期）用词不当；应为 절정/시기。同版内 見頃 其余各处均译对：P8 答案 144「見頃 = 가장 보기 좋은 시기」、答案 86「아라시야마 절정은 11월 13일부터」、答案 69/73「절정」。仅此 1 处不一致，不影响答案判定与事实。 |
| L2 | low | ja-es，P8 答案 20 | 勤労感謝の日 的西语简析只写「Día de Acción de Gracias」——该词是美国感恩节的通用西语名，易与日本「劳动感谢日」混淆；同版 Q132 答案已用全称「Día de Acción de Gracias por el Trabajo」（正确）。仅此 1 处简称，不影响答案判定与事实。 |

无 MAJOR、无 MEDIUM。其余 9 版讲解层、全部核心层、全部答案键均无发现。

## 5. 逐版门禁结果

门禁脚本：`run_gates.sh`，逐版跑 `p8.py compare --total 150`、occlusion、D5 census、引号普查、boxtitle/spill/edge 三门；完整日志 `gates.log`，逐版 JSON 在 `gates/`。**11 版全部通过**（`run_gates.sh` 退出码 0）。

| 版 | p8 compare（150/150） | occlusion | D5 census | 引号普查 | boxtitle | spill | edge |
|---|---|---|---|---|---|---|---|
| core-ja | CLEAN，keydiff [] | 0 flags（自检 OK） | PASS（违规 0，curly_total 0） | defective 0 | 0 DEFECT，0 marginal | 0 SPILL | 0 TOUCH，0 NEAR |
| ja-de | CLEAN，keydiff [137–140] | 0 flags | PASS | 0 | 0 DEFECT，0 marginal | 0 SPILL | 0 TOUCH，0 NEAR |
| ja-en | CLEAN，keydiff [137–140] | 0 flags | PASS | 0 | 0 DEFECT，0 marginal | 0 SPILL | 0 TOUCH，0 NEAR |
| ja-es | CLEAN，keydiff [137–140] | 0 flags | PASS | 0 | 0 DEFECT，0 marginal | 0 SPILL | 0 TOUCH，0 NEAR |
| ja-fr | CLEAN，keydiff [137–140] | 0 flags | PASS | 0 | 0 DEFECT，0 marginal | 0 SPILL | 0 TOUCH，0 NEAR |
| ja-it | CLEAN，keydiff [137–140] | 0 flags | PASS | 0 | 0 DEFECT，0 marginal | 0 SPILL | 0 TOUCH，0 NEAR |
| ja-ko | CLEAN，keydiff [137–140] | 0 flags | PASS | 0 | 0 DEFECT，0 marginal | 0 SPILL | 0 TOUCH，0 NEAR |
| ja-nl | CLEAN，keydiff [137–140] | 0 flags | PASS | 0 | 0 DEFECT，0 marginal | 0 SPILL | 0 TOUCH，0 NEAR |
| ja-pt | CLEAN，keydiff [137–140] | 0 flags | PASS | 0 | 0 DEFECT，0 marginal | 0 SPILL | 0 TOUCH，0 NEAR |
| ja-ru | CLEAN，keydiff [137–140] | 0 flags | PASS（noto_sans_elements=712，ru 读者预期） | 0 | 0 DEFECT，**1 marginal**（pre-existing，见 §6） | 0 SPILL | 0 TOUCH，0 NEAR |
| ja-zh-tw | CLEAN，keydiff [139,140] | 0 flags | PASS | 0 | 0 DEFECT，0 marginal | 0 SPILL | 0 TOUCH，0 NEAR |

说明：keydiff [137–140]（zh-tw 仅 [139,140]，137/138 与核心逐字节同）为预期的读者语翻译题键；D5 普查 11 版均为拉丁在 CJK 0、西里尔在 CJK 0、弯引号在 CJK 0、curly_total=0。未重跑项：freeze baseline（修复轮已跑 8/8，生产文件指纹与修复轮终值完全一致，结论仍成立；本轮任务门禁清单未含此项）与 creambox 差分审计（需改前 base，本轮 scratch 未保留；修复轮已跑 PASS 0 defects，文件未变）。

## 6. 未重报项（按任务要求）

- FIX-LOG 末节裁定项：ja-ru boxtitle 1 marginal——本轮门禁复核（见 §5），第一轮与修复轮均已证实 pre-existing（对改前 pre-src 重跑同样为 1 marginal），非修复引入，不作新发现。
- ja-ru 版拉丁标题字体问题（拉丁文用了 Noto Sans 而非 Newsreader）：已知的跨家 D5 系统性问题，另有跨家工人统一修 svglib.py；ja-ru 版内容照常校对，字体问题不作新发现。
- 第一轮 O1（嵐山 23 日/26 日双日期）：P6 正文已同时交代两说并注明预报版本差，练习无内在矛盾，不重报。O2（读者来信 gloss 多一句邀稿）、O3（`_D5_READER="latin"` 标签）、O4（EDITION-RECORD 历史 SHA 滞后）复核仍属观察项、非缺陷，不重报为发现。

## 7. 总体结论

**(b) 有问题——仅 2 项 low 级发现（L1 ja-ko「단풍 절기」用词、L2 ja-es「Día de Acción de Gracias」简称），无 MAJOR、无 MEDIUM。**

- 第一轮 D1（11 版 ryuuryuu）与 D2（ja-ko 우미노우미）修复 11/11 落地，五层全验（py/svg/text.md/印/网 PDF 文字层：ryuuryuu 0、rikuryuu 每版 5；ja-ko 츄라노우미 1、우미노우미 0），目检印证已印出。
- 从头全量重校：core-ja text.md 1356 行全文 + 10 版讲解层 diff 全量（共约 3700 行）+ 答案键跨版逐题比对 + 题号/日期/算术/事实复核 + 印/网/text.md 全量一致性 + 5 页目检，均完成。
- 机械门禁 11 版全绿：p8 compare 全部 CLEAN、occlusion 全部 0 flags、D5 census 全部 PASS、引号普查 defective 0、boxtitle 0 DEFECT、spill 0 SPILL、edge 0 TOUCH；P8 最小字号 11 版均为 9.98pt。
- 按 SOP §8.4，定稿须一整轮全量校对零问题；本轮有 2 项 low，是否修复及修复后是否再走一轮重校，由父线裁定。本记录只校对、不修复。磁盘收尾 95G（<100G 门限）。
