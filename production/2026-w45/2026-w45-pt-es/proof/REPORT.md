# 独立校对报告 — Lucerna Weekly W45 PT×ES（葡语×西班牙语）

**校对员**：独立校对（subagent，depth 2/2，只校对、不改源码、不宣布上架、无下级代理）
**交付待审**：`files/weekly-report-w45-pt-es/`（svg×8、cards×8、print PDF、web PDF、WEEKLY-KIT.md、ABSTRACT.txt）
**构建树（只读核查）**：`hidden_files/weekly-report-w45-pt-es-build/`
**对照（只读）**：W45 PT 核心 `files/weekly-report-w45-pt-core/`、W43 PT×ES `files/weekly-report-pt-es/`、W45 PT×EN / PT×DE 兄弟版
**结论：ZERO PROBLEMS** — 全部 10 部门禁逐项独立重测通过，无阻塞项。非阻塞观察见 §11。

## 0. 开工查重（stand-down 判定）

- 开工前 `files/weekly-report-w45-pt-es/` 与构建树最新 mtime 均为 22:41（UTC），无渲染进程（`ps` 无 render/transform/python 构建进程）。
- 90 秒复查：零新写盘。判定：只是已完成交付的新鲜 mtime，**安全开工，未 stand down**。
- 未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录（校对前后哈希见 §10）。

## 1. 冻结（freeze.py，共享工具独立重跑）

- `tools/freeze.py baseline`（核心构建副本，OUT 重定向至 scratch，不碰在运目录）：**8/8 逐字节复现**。
  p1 `0dc8089d…`、p2 `56db3aa8…`、p3 `82f6fc3a…`、p4 `c5647cf6…`、p5 `92e86020…`、p6 `e6097473…`、p7 `a72cb75a…`、p8 `82630480…`，与构建员基线前缀逐项一致；跑后核心 SVG 重哈希不变。
- `tools/freeze.py diff` 核心→本版：新增 CJK **8 页均为 0**（核心 CJK 计数 156/177/153/148/223/118/357/1123 → 本版 0/0/0/0/0/0/0/0）。
- 全文 `桥接`：8 页 SVG + KIT 均为 **0**。
- 葡语正文冻结：P7 词框定义句、读者园地葡语披露句、全部文章与题面与核心逐字对照一致（抽查关键串见 §2、§6）；本版构建源 bslib4/content12/34/56/7/8 的 CJK 字符数均为 0（transform.py 含 1969 个 CJK 字符是替换表本身，属预期；gates.py 8 个、svglib.py 2 个为工具/注释字符，不进入渲染，见 §11）。
- **通过。**

## 2. P7 词框（硬性门）

- 渲染后逐字核实，定义句**逐字保留**，跨两行拼接后与核心完全一致：
  `« feriadão »: sábado, domingo e segunda — três dias de descanso.`
  （P7 行：`« feriadão »: sábado, domingo e` / `segunda — três dias de descanso.`；核心 P7 同串亦存在。）
- 仅 gloss 本地化为西班牙语：`feriadão = el puente festivo.`（单行，y=1278.56）。
- 定义句无本地化，**无冻结失败。通过。**

## 3. P8（p8.py compare 独立重跑）

- `tools/p8.py compare`（显式 `--core-p8/--edition-p8`；注：`--core-dir` 默认文件名与本族 `p8-avaliacao.svg` 不符，改用显式路径后正常）：**CLEAN 150=150**，missing=[]、extra=0，keydiff `[2, 4, 101, 137, 138, 146]`，与构建员一致。
- 逐项印刷行逐字节对照（印刷 key = `N. key —` 后的 token）：
  - 2：核心 `portões` = 本版 `portões`（`2. portões — portões = las puertas (las del lugar del examen)`；核心注用全角括号 `（考场大门）`）。
  - 4：核心 `13h30` = 本版 `13h30`（`4. 13h30 — 13h30: el examen empieza (hora de Brasilia)`）。
  - 101：核心 `confiro` = 本版 `confiro`（核心 `101. confiro — conferir：eu → confiro（不规则）`，全角冒号/括号；本版 `101. confiro — conferir: eu → confiro (irregular)`，半角括号）。
  - 146：核心 `A` = 本版 `A`（`146. A — sección = la zona del examen (la sala)`）。
  - → 2/4/101/146 确为**括号分支提取伪影**：机制与构建员所述一致（西语注用半角括号、核心用全角括号，`detect_note` 仅识别半角尾括号分支），印刷 key 逐字节相同，**非真实差异**。未动 `tools/p8.py`，与构建员处理一致。
  - 137：**真重定向，合法**。核心 key 为中文译句 `11 月 8 日周日是高考的第一天。`；本版 key 为西班牙语 `El domingo 8 de noviembre es el primer día del Enem.`，注 `Véase el titular de la página 6`（跨行续 `el titular de la página 6`）。翻译题（PT→读者语）答案必须落在读者语，合法。
  - 138：**真重定向，合法**。本版 key `Comprueba tu tarjeta antes del domingo.`，注 `Confira = comprueba`（续行 `comprueba`）。同理合法。
  - 139/140（读者语→PT）对照：key 保持葡语原文不变（`O feriadão é de 31 de outubro a 2 de novembro.` / `Quando você chegar, apresente o documento com foto.`），仅注本地化。150（写作）印刷行 `150. ✓ el texto modelo está en la sección H: 93 palabras`，与构建员所述一致。
- P8 注释纯西班牙语：P8 页 CJK=0，全角括号=0；答案行抽查全部为西班牙语注释（葡语仅作为被注的 key/词出现，属正常引用）。
- 印刷笔记集合相等（CLEAN，EXTRA_ONLY 无）；P8 末行基线实测 **2547.7**（item 118 行），满足 **2547.7 < 流程底 2552 < 页脚线 2580**（页脚线实测 y=2580，x 65→1885；页脚基线 2624 豁免）。
- **通过。**

## 4. 几何（occlusion_audit.py 独立重跑 + 补充扫描）

- 自检先行：`--selftest` OK（6 类 planted 全部触发，clean 对照静默）。
- `occlusion_audit.py` 本版 + `--core`：**分版 0 / 核心 0 / NEW 0**；单版重跑亦 0。
- 同基线碰撞（解码后墨迹测量，全部 8 页逐基线相邻对）：**0 旗**。
- 全 8 页框线压框 + 右缘扫描：ADVANCE 法最大右缘 1885.0–1897.3（P2 最大 1897.3），>1910 / >1922 均为 0；墨迹左右缘在页框内（最小左墨 63.0，最大右墨 1897.2，页脚基线墨迹底 2629.0 为页脚本身，豁免）。
- 框题压框：审计 0 旗（含 BOXTITLE 类）；P6 图表标签覆盖用基线锚定墨迹法（PIL getbbox，anchor ls）重测，7 个标签节点（`prova`×2、`portões abertos`、`60 min`、`espera`、`30 min`、`330 min`）与后绘矩形的重叠**全部 0**（<30% 门限），与构建员 gates 7 项清单一致。
- 修复部位复测（终版状态）：
  - R1 9 旗 → R2 1 旗 → R3 清零的叙事与终版几何自洽：词框 rect y=1098.5、高 194、底 **1292.5**，较 R2 所述底 1282.5 恰 +10（底垫 20→30 的增量）；gloss 墨迹底 1283.1，**净空 +9.4px**，无压框。词框底垫 30 亦在 `content7.py` 的 `wh` 公式尾项 `+ 30` 中核实。
  - 读者园地框（col3 栈）底 **1890.5**，较 R2 所述 1880.5 恰 +10，位置合理；金句末行译文基线 2383.2 < 预告带顶 2404（带 rect y=2404.0、高 118），金句间距 104（PT 句基线 2021.5/2125.5/2229.5/2333.5，间隔均为 104.0）。
  - 终版 **0 旗**。**通过。**

## 5. gloss（渲染后 · 拆分逐项计数）

- 源串按 `·` 拆分（README #21 口径，非 ` · `）：本版构建源 P2 6 / P3 6 / P4 5 / P5 5 / P6 4，**合计 26**；核心构建源同为 6/6/5/5/4，**1:1**。
- 渲染存活：26 项逐项核实，词头与释义全部在对应页 SVG 文本中存活（**26/26**，含 `a cabeça = la cabeza, el ánimo`、`a segunda chamada = una segunda convocatoria, una segunda entrada` 等含逗号项）。
- P7 金句：8 句各 **2×**（文章页 + P7 框），源页实测存在：
  Do feriadão…→P1、Muita gente…→P1、Finados…→P2、lembrar…→P3、cada ponto…→P4、quem dorme…→P5、primeiro…→P6、Confira…→P2。
- 标签序列**独立实测**（未采信构建员自述）：P7 译文后标签按金句顺序为 **(Página 1, Página 1, Página 2, Página 3, Página 4, Página 5, Página 6, Página 2)**，即 (1,1,2,3,4,5,6,2)，与构建员所称序列逐项一致；与核心文章页逐项核对无误。PT×IT 同类末项 2 的争议与本版无关——本版序列由本版核心独立裁定，**本版判定：正确**。
- **通过。**

## 6. 读者园地（零编造）

- 3 事实齐全，逐字摘录（P7 右栏）：
  - 葡语披露句原文（与核心逐字一致）：`Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3.`
  - 西班牙语等义句：`Nota de la redacción: las cartas reales y los mejores textos prometidos en el VOL.1 no habían llegado al cierre — queda el ejemplo y la promesa pasa al VOL.3.`
  - 编辑部示例标注：`«Vou fazer o Enem no domingo 8. Já conferi o cartão. Boa prova!» — EXEMPLO DA REDAÇÃO` + 西语标注 `Ejemplo de la redacción, no una carta real.`
  - 无署名、无虚构读者、无虚构来信/引语。
- 显性西班牙语邀请，逐字摘录：`¡Envíanos tu carta! Las mejores se publicarán en el VOL.3.`（祈使句 + VOL.3 刊登承诺，位于示例标注句内）。
- **最佳 P8 作文覆盖范围裁定：满足现行邀请门。理由如下：**
  - 邀请句字面覆盖的是**来信**（`tu carta` / `Las mejores` 指最佳来信），未字面提及 P8 作文；
  - 但披露句顺延承诺明确覆盖**最佳文本**（`los mejores textos … la promesa pasa al VOL.3`），预告行亦明确承诺 VOL.3 刊登 `os melhores textos da página 8`（葡语冻结行，全版通用）；
  - 三者合起来：来信 + 最佳 P8 文本均有 VOL.3 刊登承诺，覆盖完整；
  - 范围与 PT×EN、PT×DE 兄弟版**完全同构**：PT×EN 邀请句 `Send your letters to the editors: the best will be printed in VOL.3!` 亦只字面覆盖来信，最佳文本覆盖同样来自披露句 + 预告行；PT×DE（`Schreiben Sie uns! Beste Briefe erscheinen in VOL.3.`）亦然。若按“邀请句单句必须提及作文”的标准，EN/DE 同样不通过——族内现行门从来是三者合计，本版按同一标准**通过**。
- **通过。**

## 7. 家具（与 W43 同配对实测对照）

- 徽章：`TEXTOS EN PORTUGUÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`，与 W43 **逐字一致**；P1 y=372 槽位（strapline 槽位）、**19pt 粗体**，与 W43（y=372、19pt 粗体）一致；实测宽 1052.9px ≤ 1820。
- 页脚：8 页均为 `A Lucerna · SEMANARIO PORTUGUÉS VOL.2 · TEXTO EN PORTUGUÉS · EXPLICACIONES EN ESPAÑOL`，除 VOL.2（周次变更）外与 W43（VOL.1）逐字一致。
- 页码行：8 页均为 `Página N de 8`，与 W43 一致。
- gloss 前缀：`Nota — `（P2 首行 `Nota — o feriadão = el puente festivo · o…`），与 W43 前缀一致。
- 顶栏西语串：`TODA SEMANA EM PORTUGUÉS · CADA SEMANA · EL PORTUGUÉS QUE LEE BRASIL`，与 W43 逐字一致；黑带 `SEMANA DEL ENEM` / `2 nov: puente de Finados · 8 nov: día 1 del Enem` 一致。
- `BREVE` / `QUIZ RÁPIDO` / `CUÉNTANOS`：均不在 P7 而在 P1（`EM POUCAS PALAVRAS · BREVE`、`QUIZ RELÂMPAGO · QUIZ RÁPIDO`）与 P2–P5（`E VOCÊ? · CUÉNTANOS`），**与 W43 逐字一致**。
- 配对笔记格式：内层格式 `词 = 释义: 字母` 与 W43 一致（W43 例 `25. d (seção = el lugar exacto de tu voto: d)`；本版例 `25. c — feriadão = un festivo junto al fin de semana: c`）。外层括号→破折号是 W45 族体例变更（见下），内层格式未变。
- P1 版头行：实测 **38pt**（节点 size=38.0 粗体，y=330）；同串同字体复测：38pt = **1782.4px**，40pt = **1876.4px**，限 1820——构建员所称 1782/1876 均复现（0.4px 为舍入），38pt 档位正确；W43 为 36pt（节点 size=36.0），差异属实且有测量依据。
- P8 破折号体：本版 `N. key — nota` / `N. ✓ nota`，与 W45 PT 核心一致，且与 W45 PT×EN 兄弟版一致（例 `2. portões — portões = the gates (the exam venue gates)`）；W43 为括号体（例 `2. urnas (voltar às urnas = …)`）。裁定：**族内一致性成立**——W45 族决策 + 兄弟先例双重支撑；p8.py CLEAN 只证明集合相等，不证明体例选择，但体例选择本身已由核心与兄弟版核实，故**通过**（非仅凭 CLEAN）。
- 练习类型名：已译为西班牙语（`completar la frase` 等，见 KIT § Tipos）；类型从不印刷——8 页 SVG 的 CJK=0 且无中文元数据残留，**无印刷面影响**。类型分布（61/49/12/7/3/13/4/1）与核心 KIT 一致，编号/级别/页分布冻结继承；渲染标签独立 corroboration：配对 3 个区间头×4=12、Traduce 4、Forma la frase 7、¿Verdadero o falso? 3、Escribe 1，余下完成句子/单选/完形拆分属核心注册表继承（见 §11 说明）。
- 词框底垫 30 + 金句间距 104：均为 W45 核心几何，实测见 §4。
- 读者园地延期披露：W45 核心 FIX1 继承，葡语披露句与核心逐字一致，见 §6。
- **通过。**

## 8. 图片

- 仅 P1 一图：8 页 `<image>` 计数 P1=1、其余 7 页=0。
- 嵌入载荷 = 核心：P1 base64 串 SHA-256 `fd231e77993f09e0`（构建员口径：base64 串本身的 SHA；解码字节 SHA 为 `cc351a4d…`，两者口径下核心与本版均相等），base64 长 342316 字符，核心与本版**完全一致**。
- 署名在版：P1 图说 `Foto: Gary Todd / Wikimedia Commons — CC0`，与核心一致。
- **通过。**

## 9. ABSTRACT

- 单行（1 个换行符结尾，无 ASCII 双引号 `"`），西班牙语，357 字符：
  `A Lucerna, semanario en portugués VOL.2 para hispanohablantes: semana del Enem, puente de Finados del 31 de octubre al 2 de noviembre, primer día del Enem el domingo 8 de noviembre y semifinales de la Copa do Brasil; textos en portugués con explicaciones en español, niveles A2 a B2, 150 ejercicios, ideal para aprender portugués leyendo noticias de Brasil.`
- 含真实主题关键词（Enem 周、Finados 桥假 10/31–11/2、Enem 首日 11/8、Copa do Brasil 半决赛）+ 学习者搜索短语（`aprender portugués leyendo noticias de Brasil`）+ 刊名、目标语名、A2–B2、150 题。事实均取自本期内容。
- **通过。**

## 10. 卡片目视 + 题量/级别/范文 + 哈希不变

- 8 张卡片（1950×2700 PNG）**全部逐页目视**：P1 报头/徽章/照片+署名、P2–P6 词框与图表标签（P6 `portões abertos 60 min / espera 30 min / prova 330 min` 及 `60+30+330=420` 全部可见）、P7 词框/读者园地/金句/预告带、P8 全部答案与范文——**无重叠、无截断、无压框、无压页脚**。
- 题量与级别独立展开计数（chip+单号 + `N–M.` 区间头展开，区间头共 3 处：P2 25–28、P4 52–55、P8 141–144）：**150 题，A2 49 / B1 70 / B2 31**；分版 10/18/18/18/18/18/12/38；并集 1..150 无缺无重。P8 答案起首按分版区间计数亦为 10/18/18/18/18/18/12/38。
- 范文：P8 渲染 `Texto modelo:` 正文（不含标签）**93 词**，与核心一致，落在题面 80–100 词区间内。
- 校对前后哈希不变：交付 PDF print `83fa3515fbfefd9f2b84ec31f425808e6420a250aaffbcc5fe4ed9c0088ddc06`（3,471,166 B）、web `892eb78d9e91e7fd5865082abe05e90e01b37108d9be1f18bb3c77e1d5d64762`（3,494,583 B），与交接一致；8 张 SVG 校对前后哈希一致，且与构建树 `build-final-svg.sha` 一致；核心 8 SVG、W43 8 SVG 校对前后哈希均不变。
- 共享 scratch 目录未清理（仅在 `tools/scratch/baseline-ptes-proof/` 留下 freeze baseline 副本，属工具正常输出）。
- **通过。**

## 11. 与构建员自述不符处（即使非阻塞）与非阻塞观察

**与自述不符处：无阻塞性不符。** 以下为口径/方法澄清，均已复测闭合：

1. 图片哈希口径：构建员 `fd231e77993f09e0` 是 base64 串的 SHA-256，不是解码字节的 SHA（解码字节 SHA 为 `cc351a4d…`）。两种口径下核心与本版均相等，载荷同一性成立——不是实质不符，仅口径需注明。
2. 展开计数初版方法差：仅用 chip+单号配对时我方初测为 138（P2/P4/P8 各少 4），原因是配对题以 `25–28.` 等区间头渲染；纳入区间头展开后为 150，与构建员一致。此为方法口径差，非交付缺陷。
3. KIT 审计节 P6 标签列 6 项、gates-final 列 7 项（含 `prova` 两次）：两者皆真——`prova` 标签在 P6 出现两次（两行图表），我方独立重测 7 个标签节点全部 0 重叠。
4. 构建源 CJK 残留：bslib4/content* = 0（与构建员“零 CJK”一致）；gates.py 8 个、svglib.py 2 个 CJK 字符为工具/注释字符，不进入渲染；transform.py 的 1969 个为中→西替换表本身。渲染面 CJK=0 不受影响。

**非阻塞观察（均不构成问题，不阻挡上架）：**

- O1. P1 目录第 3 行（`Finados, o dia da memória` + `A2→B1`）墨迹间隙仅 +1.9px（1797.8→1799.7），视觉偏紧但无碰撞（同基线审计 0 旗），属可接受排版。
- O2. P5 第 2 栏栏首单字 `cabeça.`（句 `organizar a cabeça` 跨栏续行）——冻结核心原文的栏流，非本版引入；葡语栏流无孤字门禁，不作问题。
- O3. P8 原始答案起首行正则命中 154 行 vs 150 个唯一题号：4 个重复题号行来自练习题干与答案行的同号并存；p8.py extract 的 150 noted 为权威计数，无缺无重。
- O4. 类型分布中完成句子 61 / 单选 49 / 完形 13 的拆分未从渲染面逐项重分（渲染标签只区分到 `Completa` 族）；该拆分来自核心注册表，且本版编号/级别/页分布与核心冻结一致、渲染标签 corroboration（配对 12、翻译 4、造句 7、判断 3、写作 1）无反证，故继承成立。
- O5. P4 表格日期简写 `Dom 1º.11` 等为冻结核心原文，非本版改动。

## 证据文件（本目录）

- `REPORT.md`（本报告）
- `proof.py`（独立核查脚本，只读交付/核心/W43 目录）
- `proof-out.txt`（独立核查全量输出：CJK/家具/展开/P8 keydiff/基线/宽度/同基线/右缘/P6 标签/词框/gloss/金句/定义句/读者园地/范文/图片/家具对照）
- `p8-compare.txt`（p8.py compare 独立重跑输出）
- `occlusion-proof.json`、`occlusion-edonly.json`（occlusion_audit 独立重跑输出）
- `freeze-diff-proof.json`（freeze diff 独立重跑输出）
- `core-pre.sha`、`w43-pre.sha`、`delivery-post.sha`（校对前后哈希）
- `p8-core.txt`、`p8-ed.txt`（p8.py extract 两版输出）

**最终结论：ZERO PROBLEMS。** 本版满足全部出厂门禁，可进入下一环节（GitHub 入仓，Discord 仍暂停）。
