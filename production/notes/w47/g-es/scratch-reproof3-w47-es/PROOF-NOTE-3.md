# W47 es 家庭独立重校记录（第三轮，SOP §8.4）

- 校对员：独立重校（第三轮；未参与建造、第一轮与第二轮校对、第一轮与第二轮修复）。
- 范围：目标语 es × 读者母语 11 版（en de fr it ja ko nl pt ru zh-cn zh-tw）。core-es 即 es-zh-cn 版（`core-es/` 目录，印 PDF 名为 `La-Lucerna-VOL4.pdf`）。
- 校对日期：2026-11-12。盘上目录枚举 11 版，无多无少。
- 结论：**(b) 有问题** —— 共 1 条 finding（H1，低），见 §2。第二轮 G1–G3 修复全部核实在版（§3）；第一轮 F2/F3/F4 修复仍在版（§4）。
- 磁盘：开工 95G 已用，门限 100G（150G 盘）；收尾 95G 已用 / 55G 空闲，未触发。

## §1 校对文件清单（尺寸 + SHA-256 前 12 位）

与 FIX-LOG-2 改后 SHA 及 PROOF-NOTE-2 §1（其余 8 版）逐一核对，33 个文件全部一致，无漂移。

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） |
|---|---|---|---|
| core-es (es-zh-cn) | `La-Lucerna-VOL4.pdf` 4,317,615 / `6089c0fa5420` | `La-Lucerna-VOL4-web.pdf` 1,162,042 / `f0f6ed1de57a` | `2026-w47-es-zh-cn.text.md` 43,782 / `e537146d733d` |
| es-de | `La-Lucerna-VOL4-es-de.pdf` 2,916,396 / `3fdc2ce60e6a` | `La-Lucerna-VOL4-es-de-web.pdf` 806,895 / `fd7edd4b8415` | `2026-w47-es-de.text.md` 45,322 / `c08388962767` |
| es-en | `La-Lucerna-VOL4-es-en.pdf` 2,915,635 / `a7d5aba8bd0f` | `La-Lucerna-VOL4-es-en-web.pdf` 806,124 / `bb690dd25b6c` | `2026-w47-es-en.text.md` 44,994 / `cfdd39a9779d` |
| es-fr | `La-Lucerna-VOL4-es-fr.pdf` 2,914,957 / `fd0e9f83a989` | `La-Lucerna-VOL4-es-fr-web.pdf` 805,426 / `960de8cf8d3b` | `2026-w47-es-fr.text.md` 45,790 / `a9aed8190e83` |
| es-it | `La-Lucerna-VOL4-es-it.pdf` 2,913,352 / `0cffc84e47c0` | `La-Lucerna-VOL4-es-it-web.pdf` 803,822 / `f533bb1aa133` | `2026-w47-es-it.text.md` 45,170 / `ee56751564b3` |
| es-ja | `La-Lucerna-VOL4-es-ja.pdf` 8,530,586 / `cbb3efedd9a2` | `La-Lucerna-VOL4-es-ja-web.pdf` 1,280,143 / `70d46e27721f` | `2026-w47-es-ja.text.md` 46,571 / `29961f6fbc19` |
| es-ko | `La-Lucerna-VOL4-es-ko.pdf` 5,229,281 / `e2ae545b1462` | `La-Lucerna-VOL4-es-ko-web.pdf` 1,097,497 / `fad91509e34f` | `2026-w47-es-ko.text.md` 47,396 / `981d43e91837` |
| es-nl | `La-Lucerna-VOL4-es-nl.pdf` 2,915,320 / `c716ce60992a` | `La-Lucerna-VOL4-es-nl-web.pdf` 805,809 / `8be3118b5080` | `2026-w47-es-nl.text.md` 45,295 / `225181a991b5` |
| es-pt | `La-Lucerna-VOL4-es-pt.pdf` 2,914,243 / `ce89b874dfc0` | `La-Lucerna-VOL4-es-pt-web.pdf` 804,705 / `06514f66f69d` | `2026-w47-es-pt.text.md` 45,531 / `e308de125b8a` |
| es-ru | `La-Lucerna-VOL4-es-ru.pdf` 3,213,296 / `0ca1beca6d74` | `La-Lucerna-VOL4-es-ru-web.pdf` 1,061,817 / `2febbe24084b` | `2026-w47-es-ru.text.md` 52,347 / `8a57918fc0f9` |
| es-zh-tw | `La-Lucerna-VOL4-es-zh-tw.pdf` 4,381,575 / `fd3e65ef1840` | `La-Lucerna-VOL4-es-zh-tw-web.pdf` 1,265,861 / `8871073245fd` | `2026-w47-es-zh-tw.text.md` 43,811 / `4795332ea53a` |

印 PDF 均为 8 页、1462.5×2025 pt；网 PDF 均为 8 页、带文本层，印/网 pdftotext 逐字节一致，全部 < 7 MB。

## §2 Finding（1 条，低）

### H1 — es-ru 称呼混用：P1 栏目头用 ты，正文通篇用 вы（低）
- **位置**：es-ru 全版。P1 栏目头 `AHORA TÚ　Теперь ты`（text.md L147，印 PDF P1 在版）；¿Y TÚ? 框标题 4 处均为 `А вы?`（P2/P3/P4/P5，text.md L253/525/690/923），框内提问与全版指令通篇 вы 体。
- **证据**（text.md 全文计数）：
  - ты 体独立词仅 1 处：L147 `Теперь ты`（其余 `ты` 命中均为 `дебаты` 等词内子串，非独立词）。
  - вы 体词形 37 处：`А вы?` ×4；`Что вы будете делать…`、`Вы слушали фламенко?`、`Какой матч вы будете смотреть…`、`Вы голосовали бы…`；指令复数/敬称命令式 `Напишите`、`Прочитайте`、`Выберите`、`Соотнесите`、`Вставьте`、`Перепишите` 等。
  - 印 PDF 文字层核对一致：P1 `Теперь ты` 1 处，`А вы?` 4 处；P1/P2 渲染图目视确认两处均在版。
- **对照**：其余 9 版（en 除外，英语无 T/V 之分）称呼体前后一致——de `DU BIST DRAN` / `UND DU?`（du）、fr `À TOI DE JOUER` / `ET TOI ?`（toi）、it `TOCCA A TE`、nl `Nu jij` / `En jij?`（jij）、pt 本轮已修为 `Agora tu` / `E tu?`（tu）、ja/ko/zh-tw 无 T/V 对立。唯 es-ru 同一西语 `TÚ` 在 P1 译作 ты、在 ¿Y TÚ? 框译作 вы。
- **定性**：与第二轮 G2（es-pt você/tu 混用）同一缺陷类，规模更小（1 处 vs 5 处）。不影响理解与答案；读者会察觉称呼跳变。
- **建议**：改动最小的一致化——P1 栏目头 `Теперь ты` → `Теперь вы`（1 处；正文 вы 体为主导，全版 37 处 вы 词形 + 4 处 `А вы?` 不动）。反向统一（全版改 ты 体）改动大得多，不取。

## §3 第二轮修复核实（G1/G2/G3 全部在版）

### G1 — es-ja P8-30「世界遺産」→「無形文化遺産」
- text.md：`世界遺産` 全版 0 处；`無形文化遺産` 恰 1 处，L1772：`30. Verdadero — ユネスコが2010年にフラメンコを無形文化遺産に登録`。
- 印 PDF 文字层同：`世界遺産` 0 处、`無形文化遺産` 1 处；P8 渲染图目视确认第 30 题答案在版。**通过**。

### G2 — es-pt 标题 5 处改回 tu 体
- text.md：`você` 全版 0 处；`Agora tu` 恰 1 次、`E tu?` 恰 4 次。
- 印 PDF 文字层同：`você` 0、`Agora tu` 1、`E tu?` 4；P1 渲染图目视确认 `AHORA TÚ　Agora tu` 在版。正文 tu 形（`vais`、`gostas`、`Escreve`、`Votarias`、`comprarias`）与标题一致。**通过**。

### G3 — es-ru text.md 两处碎片归位
- text.md：L300 `пришлите их в редакцию.`（¿Y TÚ? 框尾句，在位）；L327 `nunca «en las 21:00».`（DECIR 段尾，在位）；DECIR 标题 L321 起 6 行内即见尾行，与其余 10 版一致；总行数 1888 行不变；L208 附近无孤立碎片。
- 印 PDF 文字层对照一致：L145 `…que pedirlo en Correos o por internet … пришлите их в редакцию.`（¿Y TÚ? 框内）、L162 `nunca «en las 21:00».`（DECIR 段内）；印/网 SHA 与第二轮一致（`0ca1beca6d74` / `2febbe24084b`），PDF 未动。
- P2 渲染图目视确认：DECIR LA HORA 整段同栏完整，¿Y TÚ? 框尾句完整。**通过**。

## §4 第一轮修复核实（F2/F3/F4 仍在版）

### F2 — P6 时间轴措辞，11 版全部
- text.md 与印 PDF 文字层：11 版 `sin el PSOE confirmado` 各出现恰 1 次，旧串 `sin el PSOE).` 出现 0 次。**通过**。

### F3 — P1 刊头顶行，es-fr / es-it
- PyMuPDF 实测（印 PDF P1，日期左端固定 x=1039.4pt）：
  - fr：副标 `CADA SEMANA EN ESPAÑOL　CHAQUE SEMAINE EN ESPAGNOL` 右端 x1=974.1pt，**间隙 65.4pt**；旧合并词 `ESPAGNOLSSEMANA` 0 命中。
  - it：副标 `CADA SEMANA EN ESPAÑOL　OGNI SETTIMANA IN SPAGNOLO` 右端 x1=970.7pt，**间隙 68.7pt**；旧合并词 `SPAGNOLISEMANA` 0 命中。
- P1 渲染图目视确认两版顶行副标与日期间隙清晰、无粘连。**通过**。
- 另查：es-de 同行间隙 4.4pt（副标末词 `LIEST` x1=1035.0pt，日期 1039.4pt），两词分明、无合并/重叠；两轮已接受，本轮复核同结论，不列为发现。

### F4 — P2 “DECIR LA HORA” 尾行，es-ru
- PyMuPDF 实测（印 PDF P2）：DECIR 标题 y0=877.7pt；末行 `nunca «en las 21:00».` 位于 (403.9, 1052.9)，与标题同栏、段落正下方、栏内——与第二轮实测值完全一致。P2 渲染图目视确认整段同栏完整。**通过**。

## §5 机械门（逐版结果）

> 门禁脚本：`gates_all3.sh`（复用第二轮 `gates_all2.sh` 逻辑）；冻结门、occlusion、p8 抽取/比对、boxtitle、spill、edge、D5 census 逐版跑。边角“1 touch/near-lines”为汇总行本身含关键词的计数假象，edge JSON 实为 0 TOUCH / 0 NEAR（8 页逐页核对）。`gates-all.log` 末行 `GATES DONE 18:51:12`，82 条 rc=0，0 条非零。

| 版 | 冻结 | occlusion | p8 抽取/比对 | boxtitle | spill | edge | D5 census |
|---|---|---|---|---|---|---|---|
| core-es | 8/8 | 0 flags | 150/150（无 compare，系 core） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（85 observes） | 0 TOUCH / 0 NEAR | PASS（弯引号 10/10 在 Newsreader 内） |
| es-de | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 1 marginal | 0 spills（67 observes） | 0 TOUCH / 0 NEAR | PASS（弯引号 3/3） |
| es-en | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（70 observes） | 0 TOUCH / 0 NEAR | PASS（弯引号 6/6） |
| es-fr | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（71 observes） | 0 TOUCH / 0 NEAR | PASS（弯引号 0） |
| es-it | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（71 observes） | 0 TOUCH / 0 NEAR | PASS（弯引号 0） |
| es-ja | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（84 observes） | 0 TOUCH / 0 NEAR | PASS（弯引号 0） |
| es-ko | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（149 observes） | 0 TOUCH / 0 NEAR | PASS（弯引号 4/4） |
| es-nl | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（71 observes） | 0 TOUCH / 0 NEAR | PASS（弯引号 4/4） |
| es-pt | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（69 observes） | 0 TOUCH / 0 NEAR | PASS（弯引号 0） |
| es-ru | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（72 observes） | 0 TOUCH / 0 NEAR | PASS（弯引号 0） |
| es-zh-tw | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（82 observes） | 0 TOUCH / 0 NEAR | PASS（弯引号 0） |

text.md 引号普查：11 版 U+201C/U+201D 各 0 次。D5 census 弯引号总数与 Newsreader 内数逐版相等（core 10、de 3、en 6、ko 4、nl 4，其余 0），无弯引号落在非 Newsreader 字体。

## §6 已核查、非发现的项（不重报）

- **F1 首字下沉**：按 FIX-LOG 裁定不修，本轮不重报。
- **es-ru 拉丁标题字体**（Noto Sans 而非 Newsreader）：已知跨家 D5 系统性问题，另有工人修 svglib.py；es-ru 内容照常校对，字体问题不列为发现。
- **ja “正誤正誤”**：印 PDF 全文检索 0 命中、`正誤` 恰 8 次——未印出，非缺陷（与前两轮同结论）。
- **nl “aantonende wijs”**：正确荷兰语术语（直陈式），与 `aanvoegende wijs`（虚拟式）对举，用法准确，非错字。
- **ja/ko 国民党 = PP**：日文「国民党（スペイン）」与韩文 `국민당` 均为标准译名，各 1 次，非误译。
- **es-de P1 顶行间隙 4.4pt、boxtitle 1 marginal（+0.7px）**：均在容差内，三轮一致，不重报。
- **spill “observe”行**：各版 0 spills；observe 行为词框注释放置的已知观察项，非溢出。
- **“Cinco claves”导读缩写**：de/en/fr/it/nl/ru/ja 七版只译前半句，core/pt/ko/zh-tw 全译；西语原文完整印在同一框内，信息未丢失，属导读概括写法，不列为发现。
- **pt #149 答案简析 “A que horas fecha?”**：欧洲葡语口语常见问法，可接受，不列为发现。
- **ABSTRACT**：11 版全部已读，均为读者母语，事实与正文一致（11 月 13 日辩论、29 日大选、邮寄 19 日截止、弗拉门戈 16 日、圣塞西莉亚 22 日、西甲第 13 轮、欧冠）；无 ASCII 引号；zh-tw 0 简化字残留（常用简化字表扫描）；非 CJK 版 0 CJK 字符；ja/ko/ru 各自脚本计数正常。

## §7 逐版结论与总体结论

| 版 | 结论 | 发现 |
|---|---|---|
| core-es (es-zh-cn) | 干净 | 无。 |
| es-de | 干净 | 无。P1 顶行间隙 4.4pt、boxtitle 1 marginal（+0.7px）均在容差内，见 §6。 |
| es-en | 干净 | 无。 |
| es-fr | 干净 | 无。F3 已修复并目视确认（间隙 65.4pt）。 |
| es-it | 干净 | 无。F3 已修复并目视确认（间隙 68.7pt）。 |
| es-ja | 干净 | 无。G1 已修复并目视确认（P8-30「無形文化遺産」）。 |
| es-ko | 干净 | 无。`국민당` 为韩文标准译名。 |
| es-nl | 干净 | 无。`aantonende wijs` 为直陈式标准术语。 |
| es-pt | 干净 | 无。G2 已修复并目视确认（`Agora tu` / `E tu?` ×4）。 |
| es-ru | **有问题（1 低）** | H1：P1 栏目头 `Теперь ты`（ты）与全版 вы 体混用。G3 已修复、F4 仍在版。 |
| es-zh-tw | 干净 | 无。0 简化字残留。 |

**总体结论：(b) 有问题**。共 1 条 finding，低（low），无 MAJOR、无 MEDIUM：
- H1（es-ru）：P1 `AHORA TÚ　Теперь ты` 用 ты 体，与 4 处 `А вы?` 框标题及全版 37 处 вы 词形混用；建议 1 处改 `Теперь вы`。

第二轮 G1/G2/G3 与第一轮 F2/F3/F4 修复全部核实在版，无回归；机械门禁 11 版全部通过（§5，冻结 8/8、occlusion 0、p8 150/150 CLEAN、boxtitle 0 DEFECT、spill 0、edge 0 TOUCH/0 NEAR、D5 census PASS）。建议修复 H1 后按 SOP §8.4 再做一轮独立重校（仅 es-ru 一版改动，改后重渲该版并复核）。

## §8 工作记录

- 33 个文件 SHA 与 FIX-LOG-2 改后值 + PROOF-NOTE-2 §1 逐一核对，全一致。
- 印/网 PDF 各 11 份 `pdftotext -layout` 提取于 `txt/`；印网文本逐字节一致；网 PDF 全部 < 7 MB、有文本层；印 PDF 全部 8 页、1462.5×2025 pt。
- core `text.md` 全文通读（1803 行）；10 版 fan-out 讲解层经 `diffs/plus-*.txt` 全读（5,950 行）；答案 1–150 逐题复核（算术：RTVE 分钟合计 195、45−30=15、禁发民调 5 天、竞选 15 天、13 天倒数；配对题 25–28/52–55/141–144、过去时 60–64、虚拟式 93–95/109–111 逐项核对无误）；日期/星期用 `date -d` 核验 13 个日期全部吻合（11 月 13 日周五、16 日周一、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、24 日周二、25 日周三、27 日周五、28 日周六、29 日周日）；8 条 FRASES DE LA SEMANA 引文逐字核对原文、页码正确；LaLiga 第 13 轮六场对阵/开球时间/积分榜（巴萨 33、皇马 30、马竞 28、巴萨客场 1–2 胜马竞）经公开来源核实。
- G1/G2/G3 修复核实：见 §3（text.md grep + 印 PDF 文字层 + 渲染图目视）。
- F2/F3/F4 修复核实：见 §4（text.md 与印 PDF 文字层 grep + PyMuPDF bbox 实测 + 渲染图目视）。
- 目视：100dpi 渲染 6 页——ru P1/P2、ja P8、pt P1、fr P1、it P1；其余页以 text.md 全文 + PDF 文本提取 + 几何门禁覆盖。目视均干净，除 §2 的 H1 外无新问题。
- 磁盘：开工 95G 已用，收尾 95G 已用 / 55G 空闲（150G 盘，门限 100G，未触发）。
