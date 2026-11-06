# W45 RU×IT 独立校对报告 — 结论：不通过（仅 KIT 两处数字与实测不符；纸面零缺陷）

- 校对对象：`files/weekly-report-w45-ru-it/`（SVG ×8、卡片 ×8、print/web PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照：W45 RU 核心已发版 `files/weekly-report-w45-ru-core/`；家具对照：W43 已发版 `files/weekly-report-ru-it/`（只读，未写入）
- 校对员动作边界：只读校对，未改源码，未派生下级代理，未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未写入 W43 目录。
- 开工查重：开工时无进行中渲染进程；90 秒复查零新写盘（仅已完成交付时间戳），按协调员裁定正常开工。校对结束时交付物哈希与开工时逐值一致（顺序不同而已），核心 8/8 哈希全程无变化。

## 结论先行

**不通过 — 但原因不在纸面。纸面（SVG/卡片/PDF）经 SOP §8 全量独立验证零缺陷；WEEKLY-KIT.md 有 2 处可测量数字与已发 SVG 不符，按任务规则“纸面零问题但 KIT 不一致同样判不通过”，不能定稿。**

**修复范围 = 只改 KIT 文字，不需重建、不需重渲染、不需改 SVG/PDF：** 修正下面问题 1、2 两行数字后，本校对可直接复核这两行即转为 ZERO PROBLEMS。纸面本身不需要任何改动。

## 问题清单（编号）

### 问题 1（主）：KIT §5 “P8 keys flow ends at y=2375” 与实测不符

- 实测（独立脚本，从已发 SVG 逐元素量取，核心与本版一致）：
  - 本版编号行最大 y = **2532.59**（第 39 题，x=65 列）；核心同样为 2532.59（第 120 题，x=989 列）。
  - 各列编号行最大值：本版 x=65 列 2532.59、x=527 列 2530.45、x=989 列 2520.28、x=1451 列 2359.41（第 150 题）；核心对应列亦全部 >2400。
  - P8 中不存在 y=2375 的编号行终点；最接近的候选（x=1451 列终点 2359.41）亦差 15.6px。
- 来源：该句与 W45 ru-fr KIT §5 逐字相同，且 builder 的 verify.py 全文无 “2375”——属跨版复制的样板句，未针对本版实测。
- 实质影响：纸面仍通过——距 2580 规则线实际余量 47px（非 KIT 暗示的约 205px），occlusion 审计 0 flags、页脚带无违规；但 KIT 低估了与规则线的接近程度，必须更正为 2532.59 后方可定稿。

### 问题 2（次）：KIT §14 “P1 media head ends 1772.5” 与实测不符

- 实测（构建自带 `svglib.text_w`，即 NotoSansCJK SC Bold 27pt，与该元素的 SVG 属性一致）：
  - “СМИ · Di che parlano” 宽 290.9，x=1473 起 → 终点 **1763.9**，比 KIT 少 8.6px。
  - 同方法复核 KIT 同句的另一半数字完全吻合：“СМИ · Di che cosa parlano i media” → 1933.2（与 KIT 一致），说明测量方法无误，仅 shipped head 的数字对不上。
- 实质影响：无——1763.9 < 栏目框界 1885，余量 121px，卡片目视亦无出框。仅需把 KIT 数字更正为 1763.9。

### 明确不列为问题（按任务/协调员裁定）

- **P7 读者园地盒底接触**：盒底 1727.58、披露语第 2 行基线 1738.28 与核心逐值相同，卡片上两行披露语均可读。按 ru-en 先例的协调员裁定（冻结核心几何、几何一致 + 可读即非阻塞），不重报。
- **徽章槽位 y=372 原位替换**：实测 W43 已发版与本版徽章元素完全一致（x=975 y=372、20pt bold、#a4553a、同字符串），不是 README #20 的 574 插入族。按“已发同配对版为准”，与 W43 一致即不列为问题。
- **P8 p8.py keydiff 中的 83、148**：独立 dash-parse 证明 83 键 B=B、148 键 A=A，p8.py 差异来自括号提取 artifact（README #13），非真改动。
- **P8 138 注解换行**：注解 “Confronta pagina 5” 在卡片上断为两行（“5” 独占次行首），属正常换行、可读、无碰撞，非截断。

## 纸面验证通过项（全部独立重跑，非采信 builder 自述）

1. **基线**：builder 留存的未改动 build-copy（无意大利标记）重生成的 8 SVG 与核心已发版逐字节相同（p1 8bfcb7e2…、p2 5b35f1d7…、p3 8be9ba7f…、p4 9d699050…、p5 f49d0ed8…、p6 8559d61d…、p7 961119d6…、p8 2738ae04…，与任务简报前缀一致）；已编辑构建重跑亦 8/8 逐字节复现交付版 SVG。事后核心重哈希无变化。注：对已编辑构建目录直接跑 `freeze.py baseline` 得 0/8 属预期（它复现的是本版而非核心）；真正的基线证据是上述未改动 build-copy 的 8/8。
2. **freeze diff**：各页 added CJK = 0，本版 CJK 总数 0；西里尔词元多重集 P2–P8 与核心完全相等（443/338/306/316/354/397/641）；P1 差异恰为徽章替换行的 10 个词元，计数与 KIT §4 逐项一致（ЕЖЕНЕДЕЛЬНАЯ/ДЛЯ/ИЗУЧАЮЩИХ/РУССКИЙ/ЯЗЫК/НАСТОЯЩАЯ/РОССИЯ 1→0；ГАЗЕТА 2→1、ПО 3→2、РУССКИ 2→1），无未备案俄语词元丢失。
3. **P8**：`tools/p8.py compare` CLEAN（150=150，missing=[]，extra=0）；独立 dash-parse 真键差仅 [137, 138]（W43 同配对先例的 RU→IT 翻译重瞄准：137 “Mercoledì 4 novembre è festa.”、138 “Il codice promozionale è un codice sconto.”，俄语题干保留）+ 150 范文装置语（意大利语，范文俄语原文未动，独立实测 84 词）；139/140 反向键逐字节与核心相同。
4. **遮挡**：`occlusion_audit.py --selftest` 通过（6 类全触发、干净对照静默）；本版 0 flags、核心对照 0 flags、NEW vs 核心 0；同基线墨迹扫描（builder verify.py §10 独立重跑）P1 家具带 0 flags。P6 图表：4 条 bar（x=685 起，终点 1285/1179/1073/967）与数值 34%（1299）/28%（1193）/22%（1087）/16%（981）全部可见、间距恰 14、无后绘 rect 遮挡；标签终点 ≤307.6（最长恰 307.6）；图表注解行 1241.9px（构建字体实测，与 KIT 一致）。
5. **gloss/图片/金句/计数/构建日志**：gloss 按 · 拆分，9 次调用共 26 项，逐 call 与核心相等（3/3/3、3/3/3、3/2/3）；图片载荷与核心逐字节相同（P1/P4/P5 各 1 张，其余页均空）；P7 金句 8 句：全刊 2 次（来源页 1 次 + P7 引用 1 次），核心与本版一致（P7 单页内各 1 次为引用本身，另 1 次在来源文章页）；150 题、A2 51 / B1 75 / B2 24、分页 10/18/18/18/18/18/12/38；构建日志零 FLOW OVERFLOW / 零 HEAD TOO WIDE；全角括号 0。
6. **家具三方比对（本版 vs W43 已发版 vs 核心）**：徽章字符串/槽位/字号/颜色、顶栏（975,92,21pt，全文逐字同，构建字体实测跨度恰 547.5–1402.5，与 KIT 一致）、脚注（除 VOL.1→VOL.2 外逐字同）、Pagina N di 8（8/8）、gloss 前缀 “Nota — ”、短版栏目名（In cifre/Sommario/La parola/Quiz lampo/In breve/Pro e contro/Analisi/Giovani/E tu? 均在两版出现）、P8 分隔符 “— СТРАНИЦА N —”、目录 “все” 标签、y=330 俄语 strap（核心自带俄语行，保留正确）均与 W43 已发版一致。
7. **P7 几何与读者园地**：盒底 1727.58、披露第 2 行基线 1738.28 与核心逐值相同；示例信件行（1343–1465）与俄语披露行（1527–1649）逐字与核心相同，仅译文披露 2 行（1709.88/1738.28）由中文换为意大利语；无编造读者/信件/引言。
8. **ABSTRACT 与文件**：意大利语单行、无 ASCII 双引号、含真实主题关键词（4 novembre festa、3 novembre、saldi 11.11、14ª giornata 6–8 novembre）+ 学习者搜索短语（per italiani che imparano il russo con le notizie russe）+ A2–B2/150 题；两 PDF 均为 8 页，print 13,551,274 字节 sha256 20bd14c0…2079a7，web 3,173,183 字节（<10 MB）sha256 b3935443…a5ab88，与 KIT §12 逐值一致；KIT §12 的 8 个 SVG sha256 与交付版逐值一致；8 卡均为 1950×2700，8/8 目视抽查无溢出/遮挡/页脚碰撞。

## 审计输出路径

- `hidden_files/w45/ru-it-proof/PROOF-REPORT.md`（本文件）
- `hidden_files/w45/ru-it-proof/freeze-baseline.log`、`freeze-diff.log`、`freeze-diff.json`、`p8.log`、`p8.json`、`occlusion-selftest.log`、`occlusion.log`、`occlusion.json`、`occlusion-core.json`
- `hidden_files/w45/ru-it-proof/audit.py` + `audit.log`、`audit2.py` + `audit2.log`、`audit3.py` + `audit3.log`、`audit4.py` + `audit4.log`、`audit5.log`、`verify-rerun.log`
- `hidden_files/w45/ru-it-proof/hashes-delivered.txt`、`hashes-final.txt`、`core-hashes-after.txt`、`builder-baseline-hashes.txt`、`KIT-copy.md`

## 需协调员/父级采取的动作

1. 将 KIT §5 “P8 keys flow ends at y=2375” 更正为 2532.59（并注明距 2580 规则线余量 47px，仍通过）；将 KIT §14 “media head ends 1772.5” 更正为 1763.9。两处均为 KIT 文字修改，不触及 SVG/PDF。
2. 更正后请本校对（或任一复核）仅复核这两行数字，即可转为定稿；无需重建、无需重跑全量审计（纸面哈希不变即无需重验）。
