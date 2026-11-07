# 独立校对报告 — W45 IT × PT（意大利语 × 葡萄牙语）

**结论：ZERO PROBLEMS** — 11 项门禁全部通过，无阻塞项。
校对员：独立校对（未改源码、未宣布上架、未派生下级代理、未发 Discord、
未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心与 W43 目录；
核心/W43 仅只读对照；共享 scratch 目录未清理）。

**开工查重**：开工时进行中的 `render.py` 进程经 `/proc/<pid>/cwd` 核实属于
`weekly-report-w45-it-ja-build`，与本版无关；本版交付物在 90 秒复查内零新写盘
（最后 mtime 23:35，复查 23:38 仍为 23:35），安全开工。
交付物哈希与 KIT §11 逐项一致；校对前后交付与核心哈希经
`hashes-before.txt` vs `hashes-after.txt` diff 验证**完全不变**。

**交付物**：`files/weekly-report-w45-it-pt/`（svg×8、cards×8 1950×2700、
print `La-Lucerna-VOL2-PT.pdf` 7,137,176 B sha `ed151a39…acd4`、
web `La-Lucerna-VOL2-PT-web.pdf` 3,622,395 B sha `ff156593…49ca`，
均为 8 页；`WEEKLY-KIT.md`、`ABSTRACT.txt` 葡语单行）。
构建树：`hidden_files/weekly-report-w45-it-pt-build/`（transform.py + round1–5 日志/哈希）。

证据文件均在本目录：`baseline/`（freeze 基线）、`diff.json` + `diff-full.txt`、
`p8-compare.txt`、`p8-core.txt`、`p8-ed.txt`、`occlusion.json`、
`occlusion-core.json`、`occlusion.log`、`rightedge-ed/core.txt`、
`rowcheck-ed/core.txt`、`chartcheck-ed/core.txt`、`hashes-before/after.txt`。

---

## 1. 冻结 / 桥接 / CJK

- `tools/freeze.py baseline`（W45 IT 核心构建）：**8/8 逐字节复现**，
  且运行后核心 SVG 重哈希不变（`core integrity: shipped core SVGs unchanged`）。
  核心哈希与 KIT §1 逐项一致（p1 `81051bbb…`、p2 `d42ce9ae…`、p3 `9e45586d…`、
  p4 `62f75269…`、p5 `c907b869…`、p6 `5545f8dd…`、p7 `9fc999f4…`、p8 `3b87e54f…`）。
- `freeze.py diff` 核心 vs 本版：每页新增 CJK = 0，全期新增 CJK = 0；
  本版 8 页文本节点 CJK 字符独立扫描均为 0。
- `桥接` 全文扫描：交付目录 + 构建目录（含 KIT、ABSTRACT、全部构建代码、
  scratch 脚本）**0 次**。构建员自述“终查时 KIT 误写 1 次已清除”经复核属实：
  现 KIT 全文 0 次。
- 差分全文逐条读完（`diff-full.txt`，708 行）：移除项除下列三类外全部含中文
  （即讲解层替换）：(a) P8 破折号体 → 括号体改版行与 `— PAGINA n —` →
  `— PÁGINA n —`；(b) P6 移除片段 `bollettino · modello`——实为重排，
  该串完整存活于新增行 `probabilità · media · bollettino · modello` 内；
  (c) P7 移除行 `è probabile che / è possibile che / bisogna`——实为重排，
  分存于新增行 `Depois de è probabile che, è possibile che e` 与
  `bisogna che usa-se o conjuntivo; depois de` 内。无意大利语正文丢失。
- 意大利语正文冻结：P2/P6 manovra 段意大利语正文未动，仅中文披露句译为葡语；
  P6 图表标签、赛程表、图说、署名与核心逐字一致（差分中无此类移除项）。

## 2. P7 词框（硬性门）

- 定义句 4 行逐字、逐行 y/字号与核心完全一致（y=1128.5/1159.03/1189.56/1220.09，
  21.5pt）：
  `« l'assaggio » è la prova di un cibo:` / `un piccolo pezzo per decidere se` /
  `piace. Questa settimana vive a` / `pagina 3, alla finale del Panettone.`
  **定义句未本地化，通过。**
- gloss 行：核心 2 行 `assaggio = 品尝。本周见第 3 版：潘妮托尼决赛上观众可以免费品尝。`
  → 本版 1 行 `assaggio = prova, página 3.`（y=1280.62，20pt，与核心首行同位）。
  缩短掉的是中文对 P3 例句的复述；定义句上方已完整保留
  “pagina 3, alla finale del Panettone”，且该例句本身以金句形式译为葡语现于
  FRASI（`O público pode provar de graça. (Pagina 3)`）；页码指向核实准确——
  P3 正文与 P3 gloss 均含 `l'assaggio`。按任务标准（定义句完整保留 + 页码指向准确）
  **无内容丢失，通过**（见“非阻塞观察”第 2 条）。
- 金句 8 句：P7 引用句与核心逐字同位（21.5pt），葡语译文各配意大利语标签；
  归一化全文（按文本节点连接）统计裸句出现次数，核心与本版均为每句 **2×**
  （正文 1 + P7 1）。标签多重集与核心一致：{1×2, 2×2, 3, 4, 5, 6}；
  阅读顺序 (1,3,1,4,2,5,2,6) 核心与本版亦完全相同。
  （构建员所谓 “Pagina (1,1,2,2,3,4,5,6)” 即该多重集，表述为排序后集合，
  非阅读顺序——非不符，仅记述方式差异。）

## 3. P8

- `tools/p8.py compare`（显式 `--core-p8/--edition-p8`，`--total 150`）：
  **CLEAN，core 150 noted，edition 150 noted，missing=[]，extra_count=0，
  uncertain=[]，keydiff=[6,13,14,15,16,20,38,58,71,74,77,137,138,139]**。
- 14 项印刷行逐项对照（13pt 答案行重连，括号体/破折号体差异仅在分隔符与注释语）：
  - 11 项括号分支伪影，键**逐字相同**：6 `previsioni`、13 `guanti`、14 `crisantemi`、
    15 `termosifoni`、16 `fa`、20 `resta`、38 `mandorle`、58 `più bella`、
    71 `gratuiti`、74 `castagne`、77 `ci sarà`。
    例：核心 #6 `previsioni — previsioni = 预报（复数）` vs 本版
    `previsioni (previsioni = previsões, plural)`；#20 核心
    `resta — restare：la scuola → resta（lei）` vs 本版
    `resta (restare: la scuola dá resta, lei)`（箭头 → 译为葡语动词 dá，属注释侧，
    键不变）；#16 全角冒号 → 半角冒号，键不变。构建员的伪影机理（核心全角括号
    致工具 paren 分支截断）与实测印刷行一致。
  - 3 项真重定向（方向 IT→PT，合法）：137 核心 `周一第一场寒冷来了。`
    → 本版 `Na segunda-feira chega o primeiro frio.`；
    138 核心 `观众可以免费品尝。` → `O público pode provar de graça.`；
    139 核心 `周日晚上，佛罗伦萨对尤文图斯。`
    → `No domingo à noite, joga-se Fiorentina–Juventus.`。
    注释均为葡语（`Ver o texto original.` / `assaggiare gratis = provar de graça` /
    `si gioca = joga-se`）。
  - 140 **未被 flag，正确**：意大利语键逐字不变
    `Ogni previsione deve essere chiara.`，注释 `dovere = dever`；
    题干为葡语 `Cada previsão deve ser clara. → ___`（PT→IT 方向，键不变）。
  - 150 写作题无键，注释葡语 `✓ O texto modelo está na seção H desta página,
    81 palavras`（核心：`✓ 范文见本版 H 区（81 词）`）。
- P8 注释纯葡语：全期 CJK=0；注释体内嵌套括号扫描 0 项（格式括号除外，
  解析无歧义，compare CLEAN 佐证）。P8 分隔符 `— PÁGINA n —`、键首
  `RISPOSTE · RESPOSTAS — organizadas por página: busque pelo número do exercício`
  与 W43 同配对一致。
- P8 答案按页分隔符展开计数：{1:10(1–10), 2:18(11–28), 3:18(29–46),
  4:18(47–64), 5:18(65–82), 6:18(83–100), 7:12(101–112), 8:38(113–150)}，
  连续 1–150 无缺重，核心与本版相同。

## 4. 几何

- `tools/occlusion_audit.py`（自检 6 类全触发，干净对照静默）：本版 **0 flags**，
  核心 **0 flags**，NEW vs 核心 **0**（自测先行，`occlusion.json`）。
- 同基线碰撞（解码后真墨迹测量，独立解析 + 构建员 rowcheck.py 正确路径重跑，
  两者一致）：本版 **7 项**，核心 **7 项**，逐项完全相同——P1 目录
  `Pag. N <> 标题`（y=1396/1436/1476/1516/1556/1596/1636，墨迹间隙均为 4.0，
  正间隙非重叠，P1 目录固有布局，继承自核心，非 NEW，卡片目视干净）。
- P6 图表标签覆盖（基线锚定墨迹法，PIL `getmetrics`，anchor `ls`）：
  本版与核心最差覆盖均为 **0.0%**（门限 <30%）。
- 全 8 页框线压框 + 右缘扫描（ADVANCE 法，正确路径重跑）：
  框越线（>1910）本版 **0**、核心 **0**；边缘区 (1885,1910] 本版 4 项、
  核心 4 项，字符串与 advance 值逐项相同（P1 parola 两行 1889.3/1888.8、
  P2 匹配项 b 1902.5、P8 写作题干 1898.6），均为冻结核心串；
  唯一差异是 P8 题干 y 值（本版 663 vs 核心 633，P8 版式位移，串与边值不变，
  非缺陷）。无框体 rect 越过 1885。
- 复测终值：
  - P7 col3：末行披露句基线 1642.95（20pt），真墨迹底 1646.95；
    构建日志流终值 1648；FRASI 规则线实测在 SVG 内为
    `<line x1="65" y1="1686" x2="1885" y2="1686">`。线下净空约 **38–39px**，
    优于核心的 13px（核心 col3 1673）。构建员称“线下 38px”属实。
  - P1 副标题墨迹：终版缩短串
    `SEMANÁRIO ITALIANO · VOL.2 · PRIMO FREDDO · PANETTONE · SERIE A`
    （46pt serif bold，middle）真墨迹右缘 **1826.6**（构建员称 1826.5，
    0.1 为取整差）；带冠词的假想全串实测右缘 **1924.8**（构建员称 1925），
    越过双框线 1910/1922。去冠词修复属实且必要。
- 修复范围哈希差分验证：
  - round4 → round5（round 3）：仅 P1 与 P7 两页哈希变化，
    P2–P6、P8 字节不变——与 round 3 所述范围（P1 副标题 + P7 信件）精确一致。
  - round2 → round5：同样仅 P1/P7 变化，P8 自 round2 起未变。
  - round 2 的 7 项 NEW（构建员 `occlusion.json`：P1 日注 EDGE+BOXTITLE、
    P1 parola 次行 LINEX、P1 日框标题 BOXTITLE、P1 目录标题 BOXTITLE、
    P7 parola 标题 BOXTITLE、P7 gloss 底缘 BOXTITLE）终版全消除——
    终版审计 0/0/0 佐证；round 4 已 0/0/0，round 5 再确认。

## 5. gloss

- 核心源独立实测（`weekly-report-w45-it-build/content*.py` 的 `gloss()` 串，
  按 `·` 拆分）：P2 6、P3 5、P4 4、P5 4、P6 5，合计 **24**（非借他族数字）。
- 本版渲染后 `gloss()` 串同法计数：P2 6、P3 5、P4 4、P5 4、P6 5，合计 **24**，
  与核心 **1:1**；24 个意大利语词头全部在渲染 SVG 文本中现身；
  渲染前缀均为 `Nota — `。分布按页：0/1/1/1/1/1/0/0（P2–P6 各一框）。

## 6. 读者园地（按协调员裁定执行）

- 保留的核心意大利语元素逐字核实：信件 4 行与核心逐字相同
  （`«Ciao! Sono Li, studio italiano a Pechino. Lunedì metto il cappotto e
  la sciarpa, sabato assaggio il panettone — almeno in foto!» — Li`），
  标签 `(esempio della redazione)` 保留；预告带意大利语承诺保留
  （`le vostre lettere vere e i testi migliori della pagina 8`）。
- 披露句终版逐字摘录（P7 信件框，3 行，20pt）：
  `Exemplo da redação: sem cartas reais` /
  `nem o melhor texto da página 8.` /
  `Escrevam, saem no VOL.3!`
  三事实齐全：(1) `Exemplo da redação` = 系示例；(2) `sem cartas reais` =
  尚无真实来信；(3) `nem o melhor texto da página 8` = 尚无最佳 P8 作文；
  显性祈使 `Escrevam` + VOL.3 刊登承诺 `saem no VOL.3!` 齐全。
  预告行未计入邀请（邀请即上述祈使句本身）。
- 最佳 P8 作文覆盖范围裁定：单数 `o melhor texto da página 8` 与
  W43 同配对披露句（`o melhor texto da página 8: escrevam!`）逐词同范围，
  亦与 W45 IT×EN（`no best page-8 essay yet`）、IT×DE
  （`bester Seite-8-Text`）同为单数最佳作文槽位；预告带的复数
  `i testi migliori` 系核心冻结原文，非披露句的承诺口径，二者并存不构成
  欠覆盖。**范围裁定：覆盖充分。**
- IT 核心 P7 确无意大利语披露句可供保留（核心信件框仅有信件 + 标签 +
  中文披露句 3 行）；终版 SVG 全文检索 round 1 意大利语披露句两变体
  （`Non è una lettera vera, è un esempio.` /
  `Esempio della redazione: non è ancora una lettera vera.`）**0 命中**，
  transform.py round 3 的删除替换经代码核实已生效（该两串仅作为 rep()
  的被替换源残留于 transform.py 文本中，不进入渲染——见“非阻塞观察”第 1 条）。
  故不以“无意大利语披露句”判 NOT PASS（与 IT×EN 同类项 B1 非阻塞裁定、
  IT×DE 同结构已上架一致）。零编造：Li/北京均为核心自带标注示例，
  未新增任何读者、信件、姓名或引言。

## 7. 徽章槽位专项裁定

三方实测值：

| 方 | P1 实测 |
|---|---|
| (a) W43 IT×PT 已上架版 | 徽章 `TEXTOS EM ITALIANO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA`，y=372，20pt bold，middle；P1 全文无 `IL GIORNALE…` strapline；W43 KIT 明言该槽原为核心的可替换趋势标题（22.5pt），即 **372 槽内容被替换**，非共存、非另置。W43 副标题 y=330 保留冠词（`L'ORA SOLARE · IL MALTEMPO · IL CINEMA`）。 |
| (b) W45 核心 P1 | y=372 为冻结意大利语 strapline `IL GIORNALE SETTIMANALE PER IMPARARE — L'ITALIA VERA, IN ITALIANO, DALL'ITALIA`（19pt sans，middle，真墨迹 x 601.0–1349.0、y 357.2–375.8）；副标题 y=330 含冠词。 |
| (c) 本版 P1 | 372 strapline **逐字保留**（同 y/x/fs/字体）；徽章串与 W43 **逐字相同**，置于 y=574，22pt bold，middle，真墨迹 x 374.1–1575.9、y 551.8–580.0。净空：上距深色带底（rect y=424 + h=118 → 542）**9.8px**；下距下一文本 `LA NOTIZIA · A MANCHETE` 真墨迹顶 589.5 **9.5px**；卡片目视徽章居中清晰，无触带、无压行。 |

**裁定**：W43 同配对在 372 时 strapline 系被替换（W43 核心该槽本就不是
冻结意大利语 strapline，VOL.1 与 VOL.2 报头结构不同），故本版 574 插入
确实偏离 W43 同配对几何；但该偏离由冻结原则强制——372 置徽章将删除
冻结意大利语正文，属更严重的冻结违规。W45 IT 族先例足以支撑该偏离：
同核心的 IT×EN、IT×DE、IT×FR 三版实测徽章均为 y=574、22pt，
且工具箱 README #20 已将“FR/IT 核心无空槽（372 为冻结 strapline）→
徽章插于 y=574、22pt”定为族规（援引 FR×JA/FR×KO/IT×JA 先例）。
配对标识在 P1 masthead 上清晰可辨（徽章 + 顶条葡语 + 全页页脚），
**徽章项通过**。
（构建员 KIT 称“头条墨迹起于 ~584”：实测下一文本真墨迹顶为 589.5，
5.5px 之差应为 em 顶与真墨迹顶的度量口径差；净空结论不变，非阻塞。）

## 8. 家具（与 W43 同配对实测对照）

逐项核实，VOL 由 VOL.1 → VOL.2 外其余与 W43 已上架版一致：
徽章串（见 §7）、页脚 `La Lucerna · SEMANÁRIO ITALIANO VOL.2 · TEXTOS EM
ITALIANO · EXPLICAÇÕES EM PORTUGUÊS`、页码行 `Página N de 8`（页脚 y=2624，
20pt）、栏目标题 `VITA · VIDA COTIDIANA` / `CULTURA · CULTURA` /
`SPORT · ESPORTES` / `GIOVANI · JOVENS` / `APPROFONDIMENTO · APROFUNDAMENTO` /
`LINGUA · LÍNGUA` / P8 `VALUTAZIONE E RISPOSTE · AVALIAÇÃO E RESPOSTAS`、
gloss 前缀 `Nota — `、P8 键首与分隔符 `— PÁGINA n —`、P8 括号排法
`N. key (note)`（W43 先例，非核心破折号体）、P7 页签保留意大利语 `Pagina`
（W43 P7 金句译文标签 8 项均为 `(Pagina N)`，本版同）。
级别 47/70/33 vs W43 的 46/71/33、范文 81 词 vs W43 的 90 词——
均为核心驱动（本版级别经源静态展开计数独立复核为 47/70/33，
核心源同为 47/70/33；范文源串与核心逐字相同，81 词），非家具偏差。
P1 数字框 / 周计划框括号前无空格：实测本版 `leggera(altitude`、
`novembre(mais de 50` 等贴靠式半角括号，与 W45 IT×EN 同式
（`leggera(a`、`novembre(5…`）完全一致，且核心中文全角括号亦为贴靠式；
属家族体例（讲解层括号贴靠），**非缺陷**（W43 用 spaced 式为 VOL.1 体例差异，
不构成本版回归）。

## 9. 图片

- 嵌入载荷逐页哈希对照（base64 解码后 sha256 前 16 位）：
  P3 核心 `b074a3c2cfe1c8ad` = 本版 `b074a3c2cfe1c8ad`；
  P5 核心 `39eaac936006604a` = 本版 `39eaac936006604a`；
  其余 6 页核心与本版均无嵌入光栅图（P1 雪花为矢量 `Disegno della redazione`，
  P6 为矢量图表）。**载荷 = 核心，全部一致。**
- 署名在版：P3 `Foto: Wikimedia Commons — dominio pubblico`、
  P5 `Foto: Wikimedia Commons — CC0`、P1 `Disegno della redazione`、
  P6 `DATI INVENTATI PER L'ESERCIZIO`（练习数据标注）均在版且与核心一致
  （差分中无署名类移除项）。

## 10. ABSTRACT

`ABSTRACT.txt`：单行（296 字符 + 末尾换行）、无 ASCII 双引号；
含刊名 `La Lucerna VOL.2`、周次 `2 a 8 de novembro de 2026`、
真实主题关键词（`primeiro frio`、`Forum Cultura`、`Taça do Mundo do Panettone`、
`Festa del Torrone`、`jornada 11 da Serie A`）、学习者搜索短语
（`aprender italiano` / `ler italiano verdadeiro`）、目标语 `italiano`、
分级 `A2 a B2`、题数 `150 exercícios com respostas`。事实均取自本期内容。**通过。**

## 11. 卡片目视 / 题量 / 范文 / 哈希

- 8 张卡片全部逐页目视：P1 徽章/副标题/日框/parola、P2 gloss 与 E TU、
  P3 松露照片与署名、P4 赛程表、P5 栗子照片与周计划框、P6 图表与
  DATI INVENTATI 标注、P7 col3 与 FRASI 规则线、P8 答案区底与页脚——
  均无溢出、重叠、压页脚、触框；P7 信件框 3 行披露句清晰可读。
- 题量独立展开计数（源静态计数，不执行构建模块）：
  本版 `f.ex` + `match_set` 左项展开 = **150（A2 47 / B1 70 / B2 33）**，
  核心源同法 = 150（47/70/33）；页分布经 P8 分隔符展开 = 10/18/18/18/18/18/12/38
  （见 §3）。与任务给定的 IT 核心数一致。
- 范文：源 `MODELO` 串核心与本版逐字相同，`split()` 计 **81 词**；
  渲染后 P8 H 区全文连接亦可完整复原该串。核心逐字一致。**通过。**
- 校对前后交付与核心哈希不变（`hashes-before.txt` = `hashes-after.txt`，
  diff 空）。未清理共享 scratch 目录。

---

## 与构建员自述不符处（均非阻塞）

1. KIT §8 称下一文本墨迹起于“~584”：实测 `LA NOTIZIA` 真墨迹顶 589.5，
   徽章底 580.0，净空 9.5px（非 ~4px）；结论（留空合格）不变。
2. KIT §7.6 称副标题墨迹止于 1826.5：实测 1826.6（0.1 取整差）；全串 1925
   实测 1924.8。结论不变。
3. 首轮补充脚本曾因相对路径错误（`../../files` 自 scratch 目录指向不存在路径，
   glob 为空）返回空洞 0 值；已发现并以正确路径重跑，终值来自正确路径运行
   与独立解析的双重一致。内容无问题，方法教训已记于此。
4. transform.py 注释残留：round 1 注释“gloss 缩为一行以便容纳下文意大利语披露句”
   及 round 1 rep() 的被替换源串（含已删除的意大利语披露句）在 round 3 后
   已成死文本；最终渲染已证实不含该句。属文档陈旧，非内容缺陷，
   建议主线归档时顺手清理注释（不阻塞上架）。

## 非阻塞观察

1. P7 gloss 由核心 2 行缩为 1 行（见 §2）：掉的是中文例句复述，
   定义句与例句译文另有承载，页码指向准确；按任务标准不计内容丢失。
2. P1 副标题去冠词（`IL PRIMO FREDDO · IL PANETTONE · LA SERIE A` →
   `PRIMO FREDDO · PANETTONE · SERIE A`）为框线修复所必需；
   主题词完整保留，W43 保留冠词系因其串长未越框，不可比。
3. P8 写作题干 y 值本版 663 vs 核心 633（P8 版式位移），串与右缘值不变，
   不影响任何门限。
4. P7 三栏正文在约 y=1121–1214 处结束、下方留白，系核心版式（栏高未变），
   非缺内容；P7 练习编号 101–112 与 P8 分隔符页分布一致。
5. KIT §3“注释不含括号”应理解为注释体内无嵌套括号（实测 0 项），
   格式括号本身即为 P8 括号体；解析无歧义（compare CLEAN）。

---

**最终结论：ZERO PROBLEMS。** 本版可按主线流程交付（入 LucernaRead/weekly 仓；
Discord 仍暂停，不发 Discord；不向主聊天发卡片/PDF）。
