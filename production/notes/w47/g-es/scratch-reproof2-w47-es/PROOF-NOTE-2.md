# W47 es 家庭独立重校记录（第二轮，SOP §8.4）

- 校对员：独立重校（第二轮；未参与建造与修复，与第一轮校对员、修复者均不同）。
- 范围：目标语 es × 读者母语 11 版（en de fr it ja ko nl pt ru zh-cn zh-tw）。core-es 即 es-zh-cn 版（`core-es/` 目录，印 PDF 名为 `La-Lucerna-VOL4.pdf`）。
- 校对日期：2026-11-12。盘上目录枚举 11 版，无多无少。
- 结论：**(b) 有问题** —— 共 3 条 findings（G1–G3，均为低），见 §2。第一轮 F2/F3/F4 修复全部核实在版（§3）；F1 按裁定不重报。
- 磁盘：开工 94G 已用，门限 100G（150G 盘）；收尾复核见 §7。

## §1 校对文件清单（尺寸 + SHA-256 前 12 位）

与 FIX-LOG 改后 SHA 逐一核对，33 个文件全部一致（修复后无漂移）。

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） |
|---|---|---|---|
| core-es (es-zh-cn) | `La-Lucerna-VOL4.pdf` 4,317,615 / `6089c0fa5420` | `La-Lucerna-VOL4-web.pdf` 1,162,042 / `f0f6ed1de57a` | `2026-w47-es-zh-cn.text.md` 43,782 / `e537146d733d` |
| es-de | `La-Lucerna-VOL4-es-de.pdf` 2,916,396 / `3fdc2ce60e6a` | `La-Lucerna-VOL4-es-de-web.pdf` 806,895 / `fd7edd4b8415` | `2026-w47-es-de.text.md` 45,322 / `c08388962767` |
| es-en | `La-Lucerna-VOL4-es-en.pdf` 2,915,635 / `a7d5aba8bd0f` | `La-Lucerna-VOL4-es-en-web.pdf` 806,124 / `bb690dd25b6c` | `2026-w47-es-en.text.md` 44,994 / `cfdd39a9779d` |
| es-fr | `La-Lucerna-VOL4-es-fr.pdf` 2,914,957 / `fd0e9f83a989` | `La-Lucerna-VOL4-es-fr-web.pdf` 805,426 / `960de8cf8d3be` | `2026-w47-es-fr.text.md` 45,790 / `a9aed8190e83` |
| es-it | `La-Lucerna-VOL4-es-it.pdf` 2,913,352 / `0cffc84e47c0` | `La-Lucerna-VOL4-es-it-web.pdf` 803,822 / `f533bb1aa133` | `2026-w47-es-it.text.md` 45,170 / `ee56751564b3` |
| es-ja | `La-Lucerna-VOL4-es-ja.pdf` 8,530,855 / `6d89a8ddf67b` | `La-Lucerna-VOL4-es-ja-web.pdf` 1,280,428 / `c2e0230bac8c` | `2026-w47-es-ja.text.md` 46,565 / `998a9ac32500` |
| es-ko | `La-Lucerna-VOL4-es-ko.pdf` 5,229,281 / `e2ae545b1462` | `La-Lucerna-VOL4-es-ko-web.pdf` 1,097,497 / `fad91509e34f` | `2026-w47-es-ko.text.md` 47,396 / `981d43e91837` |
| es-nl | `La-Lucerna-VOL4-es-nl.pdf` 2,915,320 / `c716ce60992a` | `La-Lucerna-VOL4-es-nl-web.pdf` 805,809 / `8be3118b5080` | `2026-w47-es-nl.text.md` 45,295 / `225181a991b5` |
| es-pt | `La-Lucerna-VOL4-es-pt.pdf` 2,914,546 / `434d8d8fe9c6` | `La-Lucerna-VOL4-es-pt-web.pdf` 805,017 / `50f4402a6a19` | `2026-w47-es-pt.text.md` 45,546 / `f9531af2c638` |
| es-ru | `La-Lucerna-VOL4-es-ru.pdf` 3,213,296 / `0ca1beca6d74` | `La-Lucerna-VOL4-es-ru-web.pdf` 1,061,817 / `2febbe24084b` | `2026-w47-es-ru.text.md` 52,347 / `dadb3e8478e5` |
| es-zh-tw | `La-Lucerna-VOL4-es-zh-tw.pdf` 4,381,575 / `fd3e65ef1840` | `La-Lucerna-VOL4-es-zh-tw-web.pdf` 1,265,861 / `8871073245fd` | `2026-w47-es-zh-tw.text.md` 43,811 / `4795332ea53a` |

印 PDF 均为 8 页、1462.5×2025 pt；网 PDF 均为 8 页、带文本层（pdftotext 字节 > 0），全部 < 7 MB。

## §2 Findings（3 条，均为低）

### G1 — es-ja P8 第 30 题答案简析称佛朗明哥列入「世界遺産」，实为非物质文化遗产（低）
- **位置**：es-ja P8 答案区，`content34.py:64`，印 PDF 第 8 页。
- **证据**：印 PDF 全文检索：`30. Verdadero —ユネスコが2010年にフラメンコを世界遺産に登録`（txt 第 834 行）。「世界遺産」即 UNESCO 世界遗产名录（文化/自然遗产）；佛朗明哥 2010 年列入的是人类非物质文化遗产代表作名录（正文 P3 原文：`inscribió el flamenco en su Lista del Patrimonio Cultural Inmaterial de la Humanidad`；UNESCO 2010 年 11 月 16 日内罗毕会议）。ja 版全文无「無形文化」一词（grep 0 命中），即该简析是版内唯一遗产名录表述，且表述不准。
- **对照**：其余 10 版同题简析均未越界——core「UNESCO 2010 年内罗毕宣布」、de「UNESCO: Flamenco seit 2010 Kulturerbe」、en「UNESCO listed flamenco as heritage in 2010」、fr「UNESCO : flamenco au patrimoine depuis 2010」、it「UNESCO: flamenco nel patrimonio dal 2010」、pt「UNESCO: flamenco no património desde 2010」、nl「UNESCO zette flamenco in 2010 op de erfgoedlijst」、ko「유네스코가 2010년에 플라멩코를 유산으로 등재했어요」、ru「ЮНЕСКО: фламенко в наследии с 2010 года」、zh-tw「UNESCO 2010 年將佛朗明哥列入非遺」。
- **影响**：答案字母 Verdadero 本身正确，不影响做题；仅日语简析一词失准。建议改为「ユネスコが2010年にフラメンコを無形文化遺産に登録」。

### G2 — es-pt 人称混用：标题用 você，正文通篇用 tu（低）
- **位置**：es-pt 全版。标题层 `AHORA TÚ　Agora você`（P1）、`¿Y TÚ?　E você?`（P2/P3/P4/P5）；正文与练习说明通篇 tu 形。
- **证据**（`content*.py` 原文）：`O que vais fazer na segunda-feira, 16 de novembro`、`De que gostas mais`、`Escreve duas frases em espanhol e envia-as à redação`、`Já ouviste flamenco?`、`Votarias pelo correio ou em pessoa?`、`Que jogo vais ver no sábado`。欧洲葡语中 você 配第三人称动词，tu 配第二人称；标题 você 与正文 tu 形并存，人称不一致。版内其余用词（`secções`、`bilhete de identidade`、`adeptos`、`golos`）均为欧洲葡语，tu 体是版内主导体，标题的两处 você 是孤立的例外。
- **影响**：不影响理解与答案；读者会察觉称呼跳变。建议标题改回 tu 体（`Agora tu` / `E tu?`）或正文统一改 você 体（二选一，前者改动最小）。

### G3 — es-ru text.md 两处碎片错位（DECIR 尾行与 ¿Y TÚ? 尾行互换位置；低）
- **位置**：仅 `2026-w47-es-ru.text.md`。印 PDF 与网 PDF 均正确（见对照），错位只在 text.md。
- **证据**：
  1. text.md 第 208 行（P2 导语区、日历之前）孤立出现 `nunca «en las 21:00».`；而 DECIR 段落在第 321–327 行，结尾却是 `Y para citar un partido: «a las 21:00»,` + `пришлите их в редакцию.`——后半句是 P2 ¿Y TÚ? 框俄语说明的尾句（`content12.py:213`：`…Напишите два предложения по-испански и пришлите их в редакцию.`），不属于 DECIR 段。
  2. 反之，text.md 第 254 行起的 ¿Y TÚ? 框俄语说明断在 `…Напишите два / предложения по-испански и`（约第 296–300 行），其尾句 `пришлите их в редакцию.` 在框内缺失。
  3. 其余 10 版 text.md 均正常：DECIR 标题后 6 行内即出现 `nunca «en las 21:00».`（core 278→284、de 301→307、en 305→311、fr 306→312、it 305→311、ja 297→303、ko 287→293、nl 305→311、pt 307→313、zh-tw 285→291），¿Y TÚ? 框尾句完整。
- **对照（印 PDF 正确）**：`2026-w47-es-ru-print.txt` 第 150 行 `DECIR LA HORA`、第 162 行 `nunca «en las 21:00».`（同栏正下方，bbox 已核）；第 145 行 `…que pedirlo en Correos o por internet … пришлите их в редакцию.`（¿Y TÚ? 框内，正确位置）。即读者看到的 PDF 无误，错位只影响 text.md 这一校对/文本记录。
- **备注**：错位只出现在 F4 改动过的 es-ru 版、且恰好是 DECIR 框上下相邻的两框，疑与 F4 改后重排有关；机制未深究。建议重新生成 es-ru text.md（或手工换回两行）后复核。
- **影响**：低。印 PDF、网 PDF、文本层均正确；仅 text.md 阅读顺序错乱，校对者按 text.md 读会在两处读到断句。

## §3 第一轮修复核实（F2/F3/F4 全部在版）

### F2 — P6 时间轴措辞，11 版全部
- 印 PDF 全文检索：11 版 `sin el PSOE confirmado` 各出现恰 1 次，旧串 `sin el PSOE).` 出现 0 次；text.md 同样（跨行断开，逐版 grep -A1 核对）。
- 与同页正文 `Atresmedia convoca su propio debate a cuatro para el lunes 23, sin el PSOE confirmado.`（`content56.py:124`）一致。**通过**。

### F3 — P1 刊头顶行，es-fr / es-it
- PyMuPDF 实测（印 PDF P1，日期左端固定 x=1039.4pt）：
  - fr：副标 `CADA SEMANA EN ESPAÑOL　CHAQUE SEMAINE EN ESPAGNOL` 右端 x1=974.1pt，**间隙 65.4pt**；旧合并词 `ESPAGNOLSSEMANA` 全版检索 0 命中。
  - it：副标 `CADA SEMANA EN ESPAÑOL　OGNI SETTIMANA IN SPAGNOLO` 右端 x1=970.7pt，**间隙 68.7pt**；旧合并词 `SPAGNOLISEMANA` / `SPAGNOLI$EMANA` 0 命中。
- P1 渲染图目视确认两版顶行副标与日期间隙清晰、无粘连。**通过**。
- 另查：es-de 同行间隙仅 4.4pt（副标末词 `LIEST` x1=1035.0pt），但两词分明、无合并/重叠，第一轮已记为无问题；本次复核同结论，不列为发现。

### F4 — P2 “DECIR LA HORA” 尾行，es-ru
- PyMuPDF 实测（印 PDF P2）：DECIR 标题 y0=877.7pt（改前 984.8pt，上移 107.1pt，与 FIX-LOG 预测一致）；末行 `nunca «en las 21:00».` 位于 (403.9, 1052.9)，与标题同栏（x=403.9）、段落正下方、栏内（en/de 对照为 (403.9, 1095.8)）。P2 渲染图目视确认整段同栏完整。
- **被删俄语注释的信息留存核实**（逐条对照同条西语行，`content12.py:179–185`）：
  - Lunes：删 `Международный`（国际）——西语行 `Día Internacional del Flamenco` 有；删 `Народная партия предлагает`（人民党提议）——西语行 `el PP propone` 有（PP = Partido Popular）。
  - Martes：删 `едет`（走访）——西语行 `la campaña recorre España` 有（recorre = 走遍）。
  - Miércoles：删 `PSOE против PP`——西语行 `Isabel Rodríguez (PSOE) y Juan Bravo (PP)` 有两党名，辩论对阵关系可读。
  - Jueves：删 `по почте`（邮寄）——西语行 `para pedir el voto por correo` 有。
  - Domingo：`день святой Цецилии` → `св. Цецилия`（缩写，同义）；西语行 `Santa Cecilia, patrona de la música` 有。
  - 另：`радио` 一词未被删（FIX-LOG 词表中的 `радио，`是带逗号的旧 token，新串仍含 `на радио`）。**无信息丢失，通过**。

## §4 机械门（逐版结果）

> 门禁脚本：`gates_all2.sh`（复用修复轮 `gates_all.sh` 逻辑）；冻结门、occlusion、p8 抽取/比对、boxtitle、spill、edge、D5 census 逐版跑。边角“1 touch/near-lines”为汇总行本身含关键词的计数假象，JSON 实为 0 TOUCH / 0 NEAR。

| 版 | 冻结 | occlusion | p8 抽取/比对 | boxtitle | spill | edge | D5 census |
|---|---|---|---|---|---|---|---|
| core-es | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（85 observes） | 0 TOUCH / 0 NEAR | PASS |
| es-de | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 1 marginal | 0 spills（67 observes） | 0 TOUCH / 0 NEAR | PASS |
| es-en | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（70 observes） | 0 TOUCH / 0 NEAR | PASS |
| es-fr | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（71 observes） | 0 TOUCH / 0 NEAR | PASS |
| es-it | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（71 observes） | 0 TOUCH / 0 NEAR | PASS |
| es-ja | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（84 observes） | 0 TOUCH / 0 NEAR | PASS |
| es-ko | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（149 observes） | 0 TOUCH / 0 NEAR | PASS |
| es-nl | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（71 observes） | 0 TOUCH / 0 NEAR | PASS |
| es-pt | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（69 observes） | 0 TOUCH / 0 NEAR | PASS |
| es-ru | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（72 observes） | 0 TOUCH / 0 NEAR | PASS |
| es-zh-tw | 8/8 | 0 flags | 150/150 CLEAN（keydiff [137,138]） | 0 DEFECT / 0 OBSERVE / 0 marginal | 0 spills（82 observes） | 0 TOUCH / 0 NEAR | PASS |

（11 版全部跑完，`gates_all2.sh` exit 0，`GATES DONE 18:04:25`。）

## §5 已核查、非发现的项（不重报）

- **F1 首字下沉**：按 FIX-LOG 裁定不修，本轮不重报。
- **\*-ru 拉丁标题字体**（Noto Sans 而非 Newsreader）：已知跨家 D5 系统性问题，另有工人修 svglib.py；es-ru 内容照常校对，字体问题不列为发现。
- **ja “正誤正誤”**：`content34.py` 源串确为 `正誤正誤`，但印 PDF 全文检索为 0 命中、`正誤` 恰 8 次——未印出，非缺陷（与第一轮同结论）。
- **nl “aantonende wijs”**：正确荷兰语术语，指直陈式（indicative），与虚拟式 `aanvoegende wijs` 对举。版内用法一致且准确：#96 `Aunque + aantonende wijs (bekend feit)`、#111 `creo que + aantonende wijs: es`、P7 讲解 `creo que met de aantonende wijs`，与 #93–95、#109–110 的 `aanvoegende wijs`（虚拟式）形成对照。非错字。
- **ja 国民党 = PP**：已核实为正确译名，非误译。日文维基「国民党 (スペイン)」条目首句：`国民党（こくみんとう、スペイン語: Partido Popular、略称：PP）は、スペインの政党`；在スペイン日本国大使館 2022 年资料亦称 `国民党（ＰＰ）`。ko `국민당` 同为韩文标准译名（국민당 (스페인)）。仅出现于 P2 日历注释（ja `content12.py:179`、ko 同位置），各 1 次。
- **es-de P1 顶行间隙 4.4pt**：副标末词 `LIEST`（x1=1035.0pt）与日期（1039.4pt）间隙 4.4pt，两词分明、无合并/重叠；第一轮已接受，本轮复核同结论。
- **es-de boxtitle 1 marginal**：`KURZNACHRICHTEN` 超框 +0.7px，容差内；三轮一致（第一轮、修复轮、本轮），非缺陷。
- **spill “observe”行**：各版 0 spills；observe 行（如 en `taking turns; the election is on the 29th.` ABOVE −42.48px）为词框注释放置的已知观察项，非溢出。
- **“Cinco claves”导读缩写**：de/en/fr/it/nl/ru/ja 七版只译前半句（`Cinco claves, sin números inventados`），略去 `todo está explicado en esta edición`；core/pt/ko/zh-tw 全译。西语原文完整印在同一框内，信息未丢失，属导读概括写法，不列为发现。
- **ABSTRACT**：11 版全部已读，均为读者母语，事实与正文一致（11 月 13 日辩论、29 日大选、邮寄 19 日截止、弗拉门戈 16 日、圣塞西莉亚 22 日、西甲第 13 轮、欧冠）；无 ASCII 引号；zh-tw 0 简化字残留；非 CJK 版 0 CJK 字符；ja/ko/ru 各自脚本计数正常。

## §6 逐版结论与总体结论

| 版 | 结论 | 发现 |
|---|---|---|
| core-es (es-zh-cn) | 干净 | 无。F2/F3 不适用；F4 不适用。 |
| es-de | 干净 | 无。P1 顶行间隙 4.4pt、boxtitle 1 marginal（+0.7px）均在容差内，见 §5。 |
| es-en | 干净 | 无。 |
| es-fr | 干净 | 无。F3 已修复并目视确认（间隙 65.4pt）。 |
| es-it | 干净 | 无。F3 已修复并目视确认（间隙 68.7pt）。 |
| es-ja | **有问题（1 低）** | G1：第 30 题答案简析「世界遺産」表述不准。 |
| es-ko | 干净 | 无。第一轮 4 处修复（48/49/84/87/91/124）已在印 P8 目视核实；国民党译名 `국민당` 为韩文标准译名。 |
| es-nl | 干净 | 无。`aantonende wijs` 为直陈式标准术语，用法准确，见 §5。 |
| es-pt | **有问题（1 低）** | G2：标题 `você` 与正文 tu 形混用。 |
| es-ru | **有问题（1 低）** | G3：仅 text.md 两处碎片错位；印/网 PDF 均正确。F4 修复在版、信息无丢失。 |
| es-zh-tw | 干净 | 无。0 简化字残留；`佛朗明哥`/`塞維亞`/`身分` 等繁体用法一致。 |

**总体结论：(b) 有问题**。共 3 条 findings，均为低（low），无 MAJOR、无 MEDIUM：
- G1（es-ja）：P8 第 30 题答案简析称佛朗明哥列入「世界遺産」，实为非物质文化遗产。
- G2（es-pt）：标题用 `você`、正文通篇 tu 形，人称混用。
- G3（es-ru）：仅 `text.md` 两处碎片错位（DECIR 尾行与 ¿Y TÚ? 尾行互换位置）；印 PDF、网 PDF 均正确。

第一轮 F2/F3/F4 修复全部核实在版（§3），无回归；机械门禁 11 版全部通过（§4，冻结 8/8、occlusion 0、p8 150/150 CLEAN、boxtitle 0 DEFECT、spill 0、edge 0 TOUCH/0 NEAR、D5 census PASS）。建议修复 G1–G3 后按 SOP §8.4 再做一轮独立重校（或由修复者自查 + 协调员核对 G3 的 text.md 重新生成）。

## §7 工作记录

- 33 个文件 SHA 与 FIX-LOG 改后值逐一核对，全一致。
- 印/网 PDF 各 11 份 `pdftotext -layout` 提取于 `txt/`；印网文本逐字节一致；网 PDF 全部 < 7 MB、有文本层。
- core `text.md` 全文通读（1803 行）；10 版 fan-out 讲解层经 `diffs/plus-*.txt` 全读；西语核心 476 条 ≥25 字符引文逐版比对，无遗漏（缺失者均为 CJK 注释正当翻译或正则代码片段假象）。
- 事实核查：RTVE 分钟合计 195；#87 45−30=15；#96 Aunque + 直陈式；#150 模板文独立重数 97 词（空白与正则两种分词一致）；8 条 FRASES DE LA SEMANA 引文逐字核对原文、页码正确；ko 第一轮 4 处修复在印 P8 核实（48. B、49. C、84. B、87. B、91. C、124. C）。
- F2/F3/F4 修复核实：见 §3（bbox 实测 + 目视）。
- 目视：90dpi 全版渲染 `png/`（88/88 页）；已看 P1/P2 全部 11 版、P6 9 版（core/de/en/fr/it/nl/pt/ru/zh-tw）、P8 4 版（ja/ko/ru/zh-tw），其余页以 text.md 全文 + PDF 文本提取 + 几何门禁覆盖。目视均干净，除 §2 的 G1–G3 外无新问题。
- 磁盘：开工 94G 已用，收尾 95G 已用 / 55G 空闲（150G 盘，门限 100G，未触发）。
