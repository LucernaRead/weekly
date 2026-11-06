# WEEKLY-KIT — Le Lucerna · 法语周报 VOL.4 · 荷兰语（nl）讲解版

- 目标语：法语（fr）；读者母语：荷兰语（nl）；期号 VOL.4，总第 4 期。
- 刊期：2026 年 11 月 9 日（周一）至 11 月 15 日（周日）；slug 周 `2026-w46`；frontmatter 周 `2026-W46`；weekStart `2026-11-09`，weekEnd `2026-11-15`。
- 刊名：`Le Lucerna`。版式：8 版，1950×2700，4 栏，页脚配对标识每版可见，P1 配对徽章可见。
- 练习：150 道（P1 10 · P2 15 · P3 18 · P4 18 · P5 17 · P6 18 · P7 12 · P8 42），分级 A2 52 · B1 75 · B2 23（与核心版相同）。P8 答案全部由登记表生成；翻译题方向为“读者语言题干 → 法语键”（与核心版一致，含核心版）。
- 词汇表 35 条、金句 8 句（逐字出自本期正文）、范文《Mon mercredi 11 novembre》98 词，均与核心版相同；仅讲解层为荷兰语（nl）。

## 一、内容

各版内容与核心版相同（P1 参议院/停战/迪耶普头版；P2 被切成两半的一周；P3 停战纪念与迪耶普集市；P4 大师赛/都灵/蓝军；P5 巴黎摄影展与周三电影；P6 参议院社保预算深读 + 自我更正；P7 精讲/金句/诊所/读者园地/VOL.5 预告；P8 综合评估）。事实来源与图片（3 张 W45 已核实 PD 图）见核心版 KIT §三、§四，本版不再重复。

## 二、兑现 W45 承诺

与核心版 KIT §二相同：巴黎大师赛结果截稿时未出，本期如实报“结果未出”并推迟至 VOL.5（不虚构冠军；辛纳膝伤退赛已更正）；预算周投票日程自我更正（W45 预告的分任务投票未发生，3 日收入部分正式投票结果未出，只报日程）；读者园地刊登标注明确的编辑部示例 + 法语说明 + 荷兰语（nl）说明（截至付印未收到 VOL.3 投稿，VOL.5 兑现点评真实投稿的承诺；邮箱状态未核实，见 §五）；日历节点（9 日参议院、11 日停战日、14–15 日迪耶普）全部入刊，19 日博若莱新酒仅见于 VOL.5 预告。

## 三、构建与复现

讲解层源文件：`hidden_files/weekly-report-w46-fr-nl-build-expl.py`（309 个键）。构建目录：`hidden_files/weekly-report-w46-fr-nl-build/`（由冻结的核心构建目录复制 + 讲解层 `expl.py`，`content*.py` 仅 OUT 路径不同，正文与核心版字节相同；`svglib.py` 字节相同）。冻结键检查（17 个纯法语键与核心版字节相同）PASS。复现：`hidden_files/w46/build_fanout.sh nl <expl.py 路径>`（单进程驱动 + 三门禁）。注记括号格式 `note_wrap` 为 `half`（核心版为 `full`）；P8 分隔符占位符为 `{pg}`。

## 四、门禁输出（实测，2026-11-02）

- `tools/p8.py compare`：**CLEAN**，keydiff `[150]`（仅写作题键为读者语言说明）。
- `tools/occlusion_audit.py`：**0 flags**（含 LINEX、同基线家具扫描、图表 GRAZE 元素检查）。修正记录见下。
- `tools/freeze.py diff`（相对核心版）：P1–P7 移除非 CJK 字符串 0 条、新增 CJK 字符 0 个；P8 余 9 条（均为键区换行碎片），由 CLEAN 的 p8 compare 裁定。
- 大报版 PDF：8 页，9,805,029 字节，SHA-256 `d68a93027dde1b0999c31502429de8ba361b34d225d4ee64da766f65264ebb41`。
- 网页版 PDF（`tools/webpdf.py`）：8 页，1,346,342 字节（< 7 MB），SHA-256 `a39b2ceb87edefbe9580caad839d74747a3e005787bbf58704e65237b06c4448`；pdftotext 46,309 字节，与大报版文本逐词一致。
- 卡片：8 张 PNG（1950×2700），`cards/`。
- `.text.md`：`45,554` 字节，由源稿导出器从 `content*.py` 源稿导出（非 PDF 反抽），含 3 行头信息。

## 五、修正记录与待确认

- 修正记录：两轮缩短：agenda_note、head_cine 仅法语、head_outils 仅法语（HEAD TOO WIDE 警告一并消除）。
- 待协调员确认：(1) 邮箱核实——读者园地示例/说明以前提“未收到 VOL.3 投稿”为真；入仓前须核实邮箱，如有真实来信须替换示例与说明。(2) 参议院正式投票日（预告“18 日 est prévu”）为单源日程口径，已按“计划”表述；VOL.5 须以实际投票结果为准。

## 补记：独立校对 Round 1 缺陷修复（2026-11-03，本地修复工）

独立校对 Round 1 结论见 `hidden_files/w46/fr-proofread-gates/proofreader-verdict-round1.md`（本版 FAIL，缺陷 D1、D2）。以下修复均改构建源码后整版重渲染，未手改 SVG/PDF。构建脚本与门禁输出见 `hidden_files/w46/fr-fix/`（`apply_fixes.py`、`shorten_d2.py`、`render*.log`、`gates-final/`）。

### D1（全部 11 版 + 核心）——P3 第 37 题否定算子与事实冲突

源码：`hidden_files/weekly-report-w46-fr-build/content34.py` 及各母语版构建目录的 `content34.py`（除 OUT 路径外字节相同，12 份同步改动）+ 各版 `expl.py`。
改前题干：`(plus) La foire est à Paris. → ___`；P8 键：`La foire n'est plus à Paris.`——`ne...plus` 预设集市曾在巴黎，与本期通篇“集市在迪耶普”冲突。
改后题干：`(pas) La foire est à Paris. → ___`；P8 键：`La foire n'est pas à Paris.`（事实正确的否定为 `ne...pas`）。连带一致性改动：各版 `expl.py` 的 `bridge_neg` 删去 `/ ne...plus`（现仅列 `ne...jamais / ne...pas`），`n_neg3` 注记改为与各版 `n_neg2` 相同的 `ne...pas` 释义（原 `ne...plus` 释义已无对应题）。改后全版 SVG 文本中已无 `n'est plus` / `(plus)` / `ne...plus`。

### D2（本版）——第 135 题题干与印刷法语键语义不符

源码：本版构建目录 `expl.py` 的 `stem_e1`（法语键不变：`Lire un programme, c'est déjà comprendre la France.`）。改前题干：`Een programma legt Frankrijk uit.`（意为“一份节目介绍法国”，与键不符）。改后题干：`Een programma lezen is Frankrijk kennen.`。
过程注记：首版较长译法（含 déjà 对应词）使 P8 电池流末端由 y=1502 增至 y=1552，对话末句 `Merci !` 被范文框覆盖 71%（`occlusion_audit.py` COVER 旗标，卡面目视证实）——与本版构建首轮已知的 P8 溢出同类。遂改为单行短译（与已通过的 EN/DE/ES 版省略 déjà 的译法一致），电池流末端回到 y=1502，遮挡清零。`n_e1` 注记（`lire un programme` = 读节目表）未动，与新题干一致。

### 重渲染与重验门禁（最终产物）

- 整版重渲染：8 SVG + 8 PNG 卡片 + 大报版 PDF（8 页，9805028 字节，SHA-256 前 12 位 `a5ba002a7f64`）+ 网页版 PDF（`tools/webpdf.py`，8 页，1346343 字节，SHA-256 前 12 位 `d815908cff14`，< 7 MB，带文字层）。`.text.md` 由源稿导出器从 `content*.py` 重生成（45547 字节，含新题干/新键，旧字符串已无），ABSTRACT.txt 未动（仍与本期主题相符）。
- `tools/freeze.py diff` vs 核心：裁定通过——P1–P7 移除的非 CJK 字符串仅标点碎片（`。`/`）。`）；P8 移除碎片均为答案键重排断行，由 p8 比对裁定；新增 CJK 字符 0 个。
- `tools/p8.py compare`：CLEAN，核心与本版印出注记集均为 121/150，missing=[]、extra=0、uncertain=[]，keydiff=[150]（仅 #150 写作题母语注记，属预期）。
- `tools/occlusion_audit.py`：0 旗标（每次运行自检 OK）；PDF 校验：8 页，文字层齐全，网页版与大报版 pdftotext 字节相等（46302 字节）。
- 改动页人工复核：P3 否定三题（题干/桥接语/ P8 键 37）逐项验过；第 135 题题干 + P8 对话区逐行验过，`Merci !` 完整可见；未引入新缺陷。F-MAIL 旗标（读者来信邮箱核实）非文本缺陷，仍待协调员在入仓前核实，本次未动相关措辞。
