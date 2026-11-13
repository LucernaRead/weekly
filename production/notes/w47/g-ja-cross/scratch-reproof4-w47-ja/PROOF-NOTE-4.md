# W47 ja 家庭独立重校记录（第四轮，PROOF-NOTE-4）

- **校对员**：第四轮独立重校员（全新工人，与建造者、第一/二/三轮校对员、第一/二/三轮修复工人均不同；SOP §8：修复后另派校对员从头全量重校）
- **日期**：2026-11-12
- **范围**：目标语 ja，11 版（core-ja = ja-zh-cn + 10 个 fan-out：ja-de/ja-en/ja-es/ja-fr/ja-it/ja-ko/ja-nl/ja-pt/ja-ru/ja-zh-tw）
- **结论**：**(a) 干净** —— 一整轮全量校对零问题，无 MAJOR、无 MEDIUM、无 low。按 SOP §8，本轮结论即定稿条件成立。本记录只校对、不修复。
- **硬约束遵守**：只在 `production/2026-w47/` 内读 ja 家 11 版生产文件，未改任何生产文件；未 commit、未 push、未跑 lint、未改 SOP。解释器一律 `tools/venv/bin/python`。磁盘：`/home/hatch` 150G 盘已用 95G（<100G 门限）。全部产出在本目录 `scratch-reproof4-w47-ja/`，未覆盖第一至三轮目录。渲染图（6 页）读完即删。
- **先读材料**：SOP.md 全文（重点 §8）、第一轮 `scratch-reproof-w47-ja/PROOF-NOTE.md` 全文、第一轮修复 `scratch-fix-ja/FIX-LOG.md` 全文、第二轮 `scratch-reproof2-w47-ja/PROOF-NOTE-2.md` 全文、第二轮修复 `scratch-fix2-w47-ja/FIX-LOG-2.md` 全文、第三轮 `scratch-reproof3-w47-ja/PROOF-NOTE-3.md` 全文、第三轮修复 `scratch-fix3-w47-ja/FIX-LOG-3.md` 全文，均已读完。另读 `~/workspace/weekly-git/AGENTS.md`（运行环境提示要求）。

## 1. 校对文件指纹（校对的那份文件）

11 版印/网 PDF 与 text.md 的尺寸 + SHA-256 前 12 位（2026-11-12 实测），与任务书给定的修复后期望值**逐版逐项完全一致**（33/33）：ja-es 与 ja-it 为 FIX-LOG-3 §4 的新值，其余 9 版为 PROOF-NOTE-3 §1 的 pre-fix 值（未被碰）。校对期间生产文件未变。

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） |
|---|---|---|---|
| core-ja（zh-cn） | 25,973,509 / `0ce5e4b872ae` | 4,654,731 / `0f9098ff3bf0` | 44,432 / `55c570f1bd0e` |
| ja-de | 25,813,856 / `4283e8a74ff9` | 4,387,416 / `c24dfb09d7d0` | 46,520 / `0d8d1de78a06` |
| ja-en | 25,806,211 / `c6a15edb8a6c` | 4,379,966 / `0560f0e4ea85` | 45,706 / `fb5a4700d3c9` |
| ja-es | 25,814,013 / `74066b869920` | 4,387,651 / `43a26e56278f` | 46,702 / `d8e0c3018361` |
| ja-fr | 25,812,296 / `9d4c6114fb31` | 4,386,312 / `ef073db3df37` | 46,882 / `badb0a6e7d00` |
| ja-it | 25,807,665 / `e44a8fcba1ba` | 4,381,291 / `3cb1e9559b3a` | 46,692 / `91224d88a55d` |
| ja-ko | 28,141,037 / `b78a3f6d5a39` | 4,552,025 / `bdf5074b3698` | 47,722 / `b1736ccf46f8` |
| ja-nl | 25,805,479 / `d6f14754f22c` | 4,379,026 / `97ee26ba1616` | 45,627 / `7f8f6638e635` |
| ja-pt | 25,814,751 / `3cca426dcbec` | 4,388,490 / `a573debf0755` | 46,696 / `9c9609378189` |
| ja-ru | 25,970,343 / `04b2f315e267` | 4,540,808 / `0726eda64903` | 53,004 / `f934bcf1d9f4` |
| ja-zh-tw | 25,988,418 / `4b09db1088b8` | 4,789,292 / `649ac196e81a` | 44,361 / `77fb0f36c75b` |

另核对两版 KIT 内 SHA 与盘上实测一致：ja-es 印 `74066b86992080d5…`、网 `43a26e56278f7b7c…`；ja-it 印 `e44a8fcba1ba429a…`、网 `3cb1e9559b3a6e77…`（各在 KIT 内出现 2 次）；两版 KIT 各含 2 处 “Fix round 3”。

## 2. 第三轮修复核实（L3 + L4）——均已落地

### L3（ja-es，P8 答案 60「tres torneos perdidos」→「tres torneos de ausencia」）——已落地

| 检查层 | 旧措辞 `tres torneos perdidos` | 新措辞 `tres torneos de ausencia` |
|---|---|---|
| text.md | 0（全版 `torneos perdidos` 0） | 1（L1276） |
| content*.py | 0 | 1 |
| SVG（分栏拼接计数，fix3 `svg_text_count.py`） | 0 / 0 | 1 / 1 |
| 印 PDF 文字层（去空白计数） | 0 | 1 |
| 网 PDF 文字层（去空白计数） | 0 | 1 |

- text.md L1276：`60. B — Hōshōryū vuelve tras tres torneos de ausencia`。
- 未动项核对：同版 Q132（L1354）仍为全称 `Día de Acción de Gracias por el Trabajo`；text.md 全称恰 2 处（L1233 答案 20 + L1354 Q132）。
- 目检印证：ja-es P8 印出「60. B — Hōshōryū vuelve tras tres torneos de ausencia」。

### L4（ja-it，P8 答案 132「Festa del ringraziamento」→「Festa del ringraziamento per il lavoro」）——已落地

| 检查层 | 全称 `Festa del ringraziamento per il lavoro` | 裸简称（否定前瞻计数） |
|---|---|---|
| text.md | 1（L1355） | 0 |
| content*.py | 1 | 0 |
| SVG（分栏拼接计数，fix3 `svg_text_count.py`） | 1 / 1 | 0（简称作子串计 1，系全称的一部分） |
| 印 PDF 文字层（去空白计数） | 1 | 0 |
| 网 PDF 文字层（去空白计数） | 1 | 0 |

- text.md L1355：`132. A — Lunedì niente scuola: Festa del ringraziamento per il lavoro`；`ringraziamento per il lavoro` 全版 2 处（L1231 答案 20 + L1355 Q132）。
- 未动项核对：同版答案 20（L1231）仍为 `23 nov. (lun.): ringraziamento per il lavoro`。
- 目检印证：ja-it P8 印出 Q132 全称与答案 20。

## 3. 第二轮修复核实（L1 + L2）——仍在版

### L1（ja-ko，P7 金句 gloss + P8 答案 98 的 `단풍 절기` 误译）——仍在版

| 检查层 | `단풍 절정은` | `단풍 절기는` | `절기` |
|---|---|---|---|
| text.md | 2（L1022、L1299） | 0 | 1（仅 L188） |
| content*.py | 2 | 0 | 1 |
| SVG（分栏拼接计数，fix3 `svg_text_count.py`） | 2 / 2 | 0 / 0 | 1 / 1 |
| 印 PDF 文字层（去空白计数） | 2 | 0 | 1（`24절기` 1） |
| 网 PDF 文字层（去空白计数） | 2 | 0 | 1（`24절기` 1） |

- text.md L1022：`단풍 절정은 교토로 이동하고 있어요. (1면)`；L1299：`98. ○ — 단풍 절정은 북쪽에서 남쪽으로 이동해요`。
- L188 未动：`해설 — 二十四節気 24절기　働く 일하다`，`절기` 全版仅此 1 处，为正确的節氣用法。
- 目检印证：ja-ko P7 印出「단풍 절정은 교토로 이동하고 있어요. (1면)」、P8 印出「98. ○ — 단풍 절정은 북쪽에서 남쪽으로 이동해요」。

### L2（ja-es，P8 答案 20 的 `Día de Acción de Gracias` 简称）——仍在版

| 检查层 | 全称 `Día de Acción de Gracias por el Trabajo` | 裸简称（否定前瞻计数） |
|---|---|---|
| text.md | 2（L1233 答案 20、L1354 Q132） | 0 |
| content*.py | 2 | 0 |
| SVG（分栏拼接计数，fix3 `svg_text_count.py`） | 2 / 2 | 0（简称作子串计 2，均为全称的一部分） |
| 印 PDF 文字层（去空白计数） | 2 | 0 |
| 网 PDF 文字层（去空白计数） | 2 | 0 |

- 目检印证：ja-es P8 印出答案 20 全称（跨两行「por el / Trabajo」）与 Q132 全称。

### D1 + D2（第一轮修复）——仍在版

每版 py / text.md / svg / 印 PDF 文字层 / 网 PDF 文字层五层分别计数：

| 版 | ryuuryuu（py/text/svg/印/网） | rikuryuu（py/text/svg/印/网） | ja-ko D2 |
|---|---|---|---|
| core-ja | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-de | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-en | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-es | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-fr | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-it | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-ko | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | 츄라노우미 1 / 우미노우미 0（五层一致；text.md L1246 `48. B — 츄라노우미는 1일째에 호쇼류에게 졌어요`） |
| ja-nl | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-pt | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-ru | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |
| ja-zh-tw | 0 / 0 / 0 / 0 / 0 | 5 / 5 / 5 / 5 / 5 | — |

**结论：L3、L4 修复 2/2 落地；L1、L2 修复 3/3 仍在版；D1 修复 11/11 仍在版（每版 5 处），D2 修复 ja-ko 仍在版。**目检印证：core-ja P7 印出「rikuryuu」金句 gloss；ja-ko P8 印出 `48. B — 츄라노우미는 1일째에 호쇼류에게 졌어요`。其余版同类专名读音亦复核无误：美ノ海 en `Churanōmi`、de `Churanoumi`、fr/es/it/pt/nl `Chura-no-umi`、ru `Чура-но-уми`、zh-cn/zh-tw 汉字「美之海」；藤凌駕 ru `Фудзирёга`（属格 `Фудзирёги`、与格 `Фудзирёге` 变格正确）。

## 4. 全量通读（从头重校，非只查已修项）

- **core-ja text.md 全文 1357 行通读**：P1–P8 文章、练习、P8 答案逐题核对。P7 本周金句 8 条逐字核对与正文一致、页码引用正确（19日二の酉 P1、ボジョレー解禁 P1、熊手 P2、新酒 P3、両横綱 2勝1敗 P4、りくりゅう P7、紅葉京都 P1、酉の市 P2）。
- **10 个 fan-out 讲解层全文通读**：每版取与 core 的 diff 全量（fan-out-only 行：de 380、en 379、es 380、fr 381、it 382、ko 360、nl 381、pt 379、ru 386、zh-tw 288 行），逐行读完——家具、译注、题干说明、P7 金句 gloss、读者园地、P8 全部答案简析、137–140 翻译题译文。
- **答案键跨版比对（程序化）**：150 题答案键（字母/×○/数字/填空词）与 core 逐题比对，137–140 除外——10 版**全部一致**；137–140 为预期的读者语翻译题键（zh-tw 仅 139/140 不同，137/138 与核心逐字节同）。
- **题号连续性（程序化，`qnum_model.py`）**：11 版 Q 1–150 与 A 1–150 均齐全、无缺无重（Q 25–28、141–144 以区间行计入，已展开核对；答案 92 各版均在版，`92. 62 — 38+24=62`，因与核心逐字节同而不入 fan-out diff）。
- **日期/星期（日历核验，`date -d`）**：11-03 周二、11-05 周四、11-07 周六、11-08 周日、11-13 周五、11-16 周一、11-19 周四（11 月第 3 个周四，ボジョレー解禁日正确）、11-21 周六、11-22 周日、11-23 周一、12-01 周二——与正文所称星期全部一致；刊期 11-16 周一～11-22 周日正确。
- **算术复核**：P6 图表 38+24+22+16=100；Q91 差 14、Q92 和 62、Q93 合计 100；Q54/Q111 11 场所、Q55/Q112 第 7 快；范文 154 字（11 版逐版去空白精确计数，均为 154 字；Q150 指引句 11 版均写 154 字）。
- **事实抽查**：P6 正文自身同时给出嵐山見頃两说（Weathernews 第 3 回予想 10 月 29 日：23 日；同社嵐山 spot 页 11 月 8 日更新：26 日ごろ、落葉はじめ 12 月 12 日）并注明是预报版本差，练习只用 23 日/12 月 12 日，无内在矛盾（第一轮 O1，本轮复核后不重报）。
- **ABSTRACT.txt**：11 版均有、读者母语、单行、无 ASCII 双引号，含刊名、目标语名、A2–B2、150 题与真实主题。
- **P8 最小字号（PyMuPDF 实测印 PDF 第 8 页）**：11 版均为 **9.98pt** ≥ SOP §1.1 底线 9.75pt；印 PDF 均为 8 页。
- **text.md 与 PDF 一致性（全量，非抽查）**：印/网 PDF 逐页文字多重集 **IDENTICAL**（11 版 × 8 页）；text.md 全部有效行（去空白归一化）均在印 PDF 文字层中逐字找到，**缺失 0 行**（11 版：core 1329 行、de 1349、en 1348、es 1349、fr 1350、it 1351、ko 1329、nl 1350、pt 1348、ru 1355、zh-tw 1325）。
- **目检**：渲染 ja-es P8、ja-it P8、ja-ko P7/P8、core-ja P7/P8（72dpi 全页）逐页看过：无溢出/重叠/压页脚/豆腐块/截断句；P7 底部照片条、P8 寺院图、P1 头版版式均在位；渲染图读完即删。

## 5. 发现表

无发现。

## 6. 逐版门禁结果

门禁脚本：`run_gates.sh`（+ 续跑 `run_gates_resume.sh`：首跑后台任务在 ja-en boxtitle 步被服务重启中断，续跑补完 ja-en 剩余门禁及 ja-es～ja-zh-tw 全部门禁，退出码 0；生产文件未动），逐版跑 `p8.py compare --total 150`、occlusion、D5 census、引号普查、boxtitle/spill/edge 三门；完整日志 `gates.log`，逐版 JSON 在 `gates/`。**11 版全部通过**（77 个门禁 RC 全部为 0，无非零 RC）。

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
| ja-ru | CLEAN，keydiff [137–140] | 0 flags | PASS（noto_sans_elements=712，ru 读者预期） | 0 | 0 DEFECT，**1 marginal**（pre-existing，见 §7） | 0 SPILL | 0 TOUCH，0 NEAR |
| ja-zh-tw | CLEAN，keydiff [139,140] | 0 flags | PASS | 0 | 0 DEFECT，0 marginal | 0 SPILL | 0 TOUCH，0 NEAR |

说明：keydiff [137–140]（zh-tw 仅 [139,140]，137/138 与核心逐字节同）为预期的读者语翻译题键；D5 普查 11 版均为拉丁在 CJK 0、西里尔在 CJK 0、弯引号在 CJK 0、curly_total=0。未重跑项：freeze baseline 与 creambox 差分审计（第三轮记录：修复轮已跑 8/8 与 PASS 0 defects，生产文件指纹与修复轮终值完全一致，结论仍成立；本轮任务门禁清单未含此项）。

## 7. 未重报项（按任务要求）

- FIX-LOG 裁定不修项：ja-ru boxtitle 1 marginal——本轮门禁复核，第一轮与修复轮均已证实 pre-existing（对改前 pre-src 重跑同样为 1 marginal），非修复引入，不作新发现。
- ja-ru 版拉丁标题字体问题（拉丁文用了 Noto Sans 而非 Newsreader）：已知的跨家 D5 系统性问题，另有跨家工人统一修 svglib.py；ja-ru 版内容照常校对，字体问题不作新发现。
- 第一轮 O1（嵐山 23 日/26 日双日期）：P6 正文已同时交代两说并注明预报版本差，练习无内在矛盾，不重报。O2（读者来信 gloss 多一句邀稿）、O3（`_D5_READER="latin"` 标签）、O4（EDITION-RECORD 历史 SHA 滞后）复核仍属观察项、非缺陷，不重报为发现。
- 第二轮 L1/L2、第三轮 L3/L4 已修且核实落地（见 §2、§3），不重报。

## 8. 总体结论

**(a) 干净——一整轮全量校对零问题。**

- 第三轮 L3（ja-es 答案 60「tres torneos de ausencia」）与 L4（ja-it 答案 132「Festa del ringraziamento per il lavoro」）修复 2/2 落地，五层全验（py/text.md/svg/印/网 PDF 文字层），Q132（ja-es）与答案 20（ja-it）均未动；两版 KIT 内 SHA 与盘上实测一致。
- 第二轮 L1（ja-ko `단풍 절정은`，P7 金句 + P8 答案 98）与 L2（ja-es 答案 20 全称）修复 3/3 仍在版，五层全验，`二十四節気 24절기`（L188）与 Q132（L1354）均未动。
- 第一轮 D1（11 版 ryuuryuu）与 D2（ja-ko 우미노우미）修复 11/11 仍在版，五层全验（ryuuryuu 0、rikuryuu 每版 5；ja-ko 츄라노우미 1、우미노우미 0）。
- 其余 9 版未被碰：指纹 33/33 与 FIX-LOG-3/PROOF-NOTE-3 核对一致。
- 从头全量重校：core-ja text.md 1357 行全文 + 10 版讲解层 diff 全量（共约 3700 行）+ 答案键跨版逐题比对 + 题号/日期/算术/事实复核 + 印/网/text.md 全量一致性 + 6 页目检，均完成。
- 机械门禁 11 版全绿：p8 compare 全部 CLEAN、occlusion 全部 0 flags、D5 census 全部 PASS、引号普查 defective 0、boxtitle 0 DEFECT、spill 0 SPILL、edge 0 TOUCH；P8 最小字号 11 版均为 9.98pt。
- 按 SOP §8，定稿须一整轮全量校对零问题；本轮零问题，ja 家庭 W47 满足定稿条件。本记录只校对、不修复。磁盘收尾 95G（<100G 门限）。

## 附：工作产物与探针说明

- 本日志：`scratch-reproof4-w47-ja/PROOF-NOTE-4.md`
- 修复核实与交叉核对：`scratch-reproof4-w47-ja/fix_verify4.py`（输出 `fix-verify.txt`）、`cross_checks.py`（输出 `cross-checks.txt`）、`qnum_model.py`（输出 `qnum-model.txt`）、`make_diffs.py`（输出 `diffs/`）
- 门禁：`scratch-reproof4-w47-ja/run_gates.sh`、`run_gates_resume.sh`（服务重启中断后补跑）、完整日志 `gates.log`、逐版 JSON 在 `gates/`
- 探针说明（供下一轮）：`cross_checks.py` §3 的「core model text chars 29」是该脚本的提取 bug——其正则 `例： (.+?)\n` 只取范文首行；范文实际跨多行，`qnum_model.py` 的多行提取给出 11 版均为 154 字（与第一轮精确计数一致）。另：朴素拼接 SVG 文本会把 D5 拆词后的短语计成 0，短语计数须用 fix3 的分栏拼接计数器 `svg_text_count.py`（本轮 L1/L2/L3/L4 的 SVG 层均以此复核）。
