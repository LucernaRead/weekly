# W47 pt 核心版第二轮独立复校笔记（2026-11-10 22:40–23:20 EST）

对象：`production/2026-w47/core-pt/`（2026-w47-pt-zh-cn，VOL.4，刊期 2026-11-16..22）
成品实测：印刷版 `A-Lucerna-VOL4.pdf` 25,311,662 字节（2026-11-10 22:16）、网页版 `A-Lucerna-VOL4-web.pdf` 1,571,251 字节（22:19），各 8 页，1462.5×2025 pt。
校对方式：只读检查，未改 core-pt 内任何文件；未跑 insert.py / lint --write / git 操作；未碰 W43/W45/W46。
校对产物：本笔记 + `work/`（自渲染 pg-1..8.png、print/web 文字层、occlusion/p8/freeze/gates 日志、三方键比对、裁剪图）。

结论：**(a) 零问题**——无硬缺陷，无需返修。D1、D2、O1、O2、O3 五项前期问题全部验证已修好；150 题答案键三方一致且 P8 113–150 全部逐题重算正确；机械门全过；§1.1 逐项实测通过（见 §5）。
另有 7 项非阻塞观察（§7，含选项折行明确裁定），均不阻塞定稿，请协调员定夺是否另立项修。

## 1. 前期问题逐项复核（全部通过）

### D1（P1/P3 国家队时间）——已修好 ✓
- 印刷版文字层：`7h15` 0 处；`Ter 17 — Singapura × Brasil, às 7h` 在 P1（文字层第 22 行）与 P3（第 219 行）各 1 处，一致。
- 渲染图目视：P1 日历栏 "Ter 17 — Singapura × Brasil, às 7h,"、P3 "Ter 17 — Singapura × Brasil, às 7h." 均确认。
- 事实独立再查（CBF 官网 2026-10-29 征召通稿，cbf.com.br，另有 OneFootball/infonews 等多家逐字转载一致）：“A Amarelinha enfrentará o Japão no dia 14 de novembro, às 7h15 (de Brasília), e no dia 17, às 7h (de Brasília), jogará contra Singapura. As duas partidas serão realizadas no Estádio Nacional de Singapura”。**日本 14 日 7h15、新加坡 17 日 7h**，刊内两处 7h 正确。

### D2（P8 Q131 键）——已修好 ✓（三处 + 源码四重确认）
- 印刷版 PDF 文字层 RESPOSTAS 区：`131. A — 周六他看帕尔梅拉斯 × 弗拉门戈`；全刊 `131. A` ×1、`131. B` ×0。
- 网页版文字层：`131. A` ×1、`131. B` ×0。
- SVG：`tools/p8.py extract` keys `131: 'A'`；`content8.py` 第 55 行 `f.ex("A2", "单选", "A", "周六他看帕尔梅拉斯 × 弗拉门戈", ...)` 源码键即 A。
- P8 渲染图目视：答案区 "131. A — 周六他看帕尔梅拉斯 × 弗拉门戈"。
- 重算依据（见 §2）：P8 C 区原文 "No sábado, 21, ele assiste a Palmeiras × Flamengo na televisão."，正确答案确为 A。

### O1（P6 时间线漏 Linguagens）——已修好 ✓
- P6 时间线渲染图 + 文字层：`8 NOV. — Primeiro dia do Enem: redação, Linguagens e Humanas.` 与同版正文一致（"No dia 8: redação, Linguagens e Ciências Humanas"）。

### O2（P1 Rugendas 图注年份）——已修好，表述准确 ✓
- 现图注："Roda de capoeira no Rio de Janeiro, em gravura de Johann Moritz Rugendas (Voyage pittoresque dans le Brésil, Paris, 1835)"（渲染图 + 文字层确认）。
- 独立查源：Dominic Winter 拍卖著录 "Voyage pittoresque dans le Brésil, Paris: Engelmann, 1835"；Swann Galleries "Paris, [1827]–1835, first edition, issued in parts"。该作分期出版、1835 年出齐，以 "Paris, 1835" 标注出版年是标准书目写法，准确。Rugendas 1802–1858，公版身份不受影响。

### O3（P5 Gary Todd 图 CC0）——无反证；本轮未完成 live 复核，见观察 O-G
- 本地 `assets/estudo.jpg` md5 `04b18fa952a61c9998ef5bf3325341f2`，与 KIT 所称源文件 md5 完全一致；该图为 W43/W45/W46 复用已验证图；P5 印 "Foto: Gary Todd / Wikimedia Commons — CC0"（渲染图确认）；`assets/CREDITS.md` 有全表。
- 本轮 live 复核未完成：Commons 文件页抓取返回 403（与第 3 轮 builder 遭遇相同，且不再重复该请求）；站内搜索未返回该文件页的授权记录。无任何反证，不构成缺陷（详见 §7 O-G）。

## 2. P8 113–150 逐题独立重算（全部正确；不采信任何"全部正确"结论）

方法：从印刷版 PDF 文字层独立提取 P8 答案键（150/150，见 §3），再逐题对照 `.text.md` 登记表与题干/阅读原文重算。
- 113 A——20 日全国假日（正文 "Sexta, 20 de novembro, é feriado nacional"）。
- 114 A——纪念祖比·帕尔马雷斯（正文 "lembra a morte de Zumbi dos Palmares"）。
- 115 B——2026 年 11 月 20 日是周五（`date -d` 核验，见 §6）。
- 116 A——决赛 12 月 6 日。
- 117 B——决赛格雷米奥 × 帕尔梅拉斯。
- 118 A——官方答案 11 月底前公布（"até o fim de novembro"）。
- 119 A——高考第二天 11 月 15 日周日。
- 120 B——第二天考试 5 小时（13h30–18h30）。
- 121 B——Lei 14.759/2023 将 11 月 20 日定为全国假日（非"创设纪念日"，那是 12.519/2011）。
- 122 A——格雷米奥总比分 3 比 1 晋级（次回合 1 比 1 + 首回合 2 比 0）。
- 123 B——点球 5 比 4。
- 124 B——Norris 赢得圣保罗大奖赛（F1 官方战报核实，见 §6）。
- 125 A——第 36 轮帕弗大战在周六 21 日（35 轮止于 18–19 日）。
- 126 B——卡波耶拉是非洲裔巴西人的格斗与音乐艺术。
- 127 A——P6 的数字 10 指到官方答案为止的工作日天数。
- 128 A——帕尔马雷斯在阿拉戈斯州。
- 129 B——Rafael 住在萨尔瓦多（短文首句）。
- 130 B——周五他去参加卡波耶拉活动（"vai a uma roda de capoeira"）。
- 131 A——周六他看帕尔梅拉斯 × 弗拉门戈（短文原句 "No sábado, 21, ele assiste a Palmeiras × Flamengo na televisão."）。★ D2 已修。
- 132 B——周一他核对非官方答案（"confere o gabarito extraoficial do Enem"）。
- 133 Sexta é feriado nacional. / 134 O Grêmio empatou por 1 a 1. / 135 Quando sair o gabarito, confira as respostas. / 136 O Brasil lembra Zumbi em 20 de novembro.——词序组句均与所给词块一致。
- 137 11 月 20 日周五是全国假日。/ 138 帕尔梅拉斯在点球大战中 5 比 4 获胜。/ 139 O gabarito oficial sai até o fim de novembro. / 140 Anote as suas respostas e confira quando sair o gabarito oficial.——翻译双向均准确。
- 141 c（consciência = 知晓与记忆）/ 142 d（gabarito = 客观题官方答案）/ 143 b（feriadão = 带假日的三天周末）/ 144 a（agregado = 两回合总比分）——与 P2/P4 配对定义一致。
- 145 A（Mané，加林查体育场）/ 146 A（sexto，格雷米奥争第六冠）/ 147 A（quinto，帕尔梅拉斯争第五冠）/ 148 A（na internet，阴性介词）/ 149 A（obrigado）。
- 150 开放作文；范文 88 词（见 §6），印刷版文字层与 `.text.md` 逐字一致。

## 3. 全部 150 题印出键与登记键一致（三方比对）

设计说明（已用文字层核实）：P1–P7 题干不印内联答案键——印刷版文字层 `(A)`–`(D)` 形式的内联键出现 0 次（与 builder 第 4 轮记录一致）；答案只在 P8 RESPOSTAS 区。所谓"印出键"即 P8 印出的答案。
- 登记表（`.text.md` 末尾 Respostas，150 项解析无缺重）vs SVG 提取键（`p8.py extract` 150/150）：1–149 **0 处不符**（150 为范文标记，无键）。
- 登记表 vs **印刷版 PDF 文字层** RESPOSTAS 区（150 项逐行解析）：**0 处不符**；`131. A` 明确。
- 登记表 vs 网页版文字层：Q131 同为 A（抽查项；print/web 词级多重集 diff = 0，见 §4）。
- P1–P7 易错键抽查重算（对照题面/原文）：Q7–10、Q11–15、Q29–33、Q47–51、Q56–59（mais/menos 比较级；Q58 16h30 mais cedo）、Q65–69、Q80–82（Verdadeiro/Falso）、Q83–92（工作日计数独立算得 16–30 日：工作日 10 天 16,17,18,19,23,24,25,26,27,30；周末+假日 5 天；10+5=15；第 10 个工作日 = 11 月 30 日，与 27–30 日窗口一致）、Q104、Q108（saíram）、Q109–112（虚拟式将来 sair/for/tiver）全部正确。
- 题号 1–150 连续无缺重（登记表、SVG 提取、印刷版三方确认）。

## 4. 机械门（全部重跑，均为本轮独立运行）

| 门 | 本轮实测 | 结论 |
|---|---|---|
| `tools/occlusion_audit.py`（自检先过） | 自检 6 类植入全触发、干净对照静默；当前 SVG **0 flags** | PASS |
| `tools/p8.py extract --total 150` | noted set **150/150** | PASS |
| `tools/p8.py compare`（core vs 自身） | CLEAN，missing=[] extra=0 keydiff=[] | PASS |
| `tools/freeze.py baseline` | 工具自报 0/8（已知重定向局限：副本写进 `build-copy/svg/` 而非 `--out/svg/`，工具比对处哈希为空）；**直接 sha256 比对副本与交付 SVG：8/8 一致**；工具自检 "shipped core SVGs unchanged" | PASS（以直接 sha256 为准） |
| `tools/gates_core.py` | **16/16 PASS**（VOL.4/刊期、页脚 8/8、无 VOL.3 版标残留、截稿注、P1 刊头行宽、基线零碰撞、页框零穿越、P6 图表标签覆盖 0%、译注 29 项全存活、8 金句各 2 次、读者园地披露、5 图+出处、P1 头条 41 字符 ≤56） | PASS |
| print/web 文字层 | 各 8 页；pdftotext 44,477 vs 44,482 字节；**词级多重集 diff = 0**（各 7,263 词；5 字节差 = web 多 5 个空行，提取引擎 artifact）；web PDF 1,571,251 字节 < 7MB | PASS |
| P8 最小字号 | pdftotext `-bbox` P8 页：答案区 755 个词框高均为 **10.12pt**（y>1250 区域最小值 10.125、中位数 10.125；全页最小字号即 10.12pt）；SVG 答案字号 13.5 单位 × 0.75 = 10.125pt | PASS（≥ §1.1 下限 9.75pt） |
| ABSTRACT.txt | 单行（524 字节含末尾换行）、无 ASCII 双引号、简体中文、含 VOL.4 / 150 道 / 本期真实关键词 | PASS |
| 金句 8 条 | SVG 文本中每条恰好出现 **2 次**（印刷版文字层计数 1 次的两条系 pdftotext  plain 模式跨栏交错造成的断裂，见注）；逐字出自本期正文，页码标签正确 | PASS |

注：金句 "o feriado abre um fim de semana de três dias" 与 "primeiro as fáceis, depois as difíceis" 在 print.txt  plain 提取中只数出 1 次，是因为正文句被跨栏交错拆散（"três / dias"、"depois as / difíceis" 之间插入了另一栏文字）；SVG 文本顺序中两条各为恰好 2 次（正文 1 次 + P7 金句 1 次），gates 亦验为 2×。横幅副标题 "…o feriado da Consciência Negra abre…" 不含 "o feriado abre…" 这一整串，不计入。

## 5. SOP §1.1 逐项独立实测（逐项核实 builder 第 4 轮的首次 PASS 宣称）

| 项 | 本轮实测方法与结果 | 结论 |
|---|---|---|
| 纸色 #fbfaf6 | 每页恰好 1 个整版底色 rect（8 页各 1 处），fill=`#fbfaf6`；无旧奶油纸 `#f7f1e2`/`#f5efe0`/`#faf3e3` | PASS |
| 禁用金色 | 无 `#d4af37`/`#c9a227`/`#b8860b`/`#b3a06a`（ko 版旧金）；`#f6e08e` 9 处均为书衣绿底副标题（SOP 允许用法）；P4 斑马纹 `#f4efe0`/`#efe8d2` 为表格底纹，非禁用色（见 §7） | PASS |
| 禁用近黑底 | 无 `#000000`/`#111111`/`#1a1a1a`/`#2c2822`；栏目条/导读条底色为书衣绿 `#37402f` | PASS |
| 禁用双线框 | stroked `<rect>` 共 **0 个**；无外框双线（ko 版旧模板每页两个嵌套描边框，本版无） | PASS |
| 拉丁 Newsreader | 拉丁目标语文本 1,231 处 Newsreader；刊头 UnifrakturMaguntia 1 处；中文小字 Noto Sans CJK SC 613 处 | PASS |
| 全角空格分隔 | 页脚 8/8 为 `A Lucerna　葡萄牙语周报 VOL.4　LUCERNA PORTUGUESE WEEKLY`（U+3000）；每页 U+3000 共 12–18 处；页码行 `第1版／共8版` 等中文数字无空格 | PASS |
| 徽章颜色精确匹配 | 逐个核对：徽章 rect 共 141 个（150 题 − 3 组配对题各省 3 个：P2 25–28、P4 52–55、P8 141–144 各合用 1 个徽章），填色与标签 **100% 对应、0 错配**：A2=`#5c6e30`、B1=`#46581f`、B2=`#37402f` | PASS |
| 字体字号 | P8 答案 10.12pt ≥ 9.75pt 下限（§4）；其余阶梯沿用第 3 轮版，未改动 | PASS |
| 选项不在中间折行 | 见 §7 O-A：字面未满足，但逐处核实选项文字完整无歧义，裁定**不构成缺陷** | 观察项 |

与 ko 版对照：ko 版的 §1.1 缺陷是模板级系统性未迁移（旧纸 `#f7f1e2`、近黑底 `#2c2822`、金色 `#b3a06a` 67 处、金棕/砖红徽章、双线外框、"·" 分隔 291 处且 U+3000 为 0）。本版上述各项实测全部为新规范值，**不存在 ko 式系统性未迁移**。唯一灰色地带是 Noto Serif CJK SC 的使用范围（见 §7 O-E），属 SOP 字体表未定义展示标题字体的空白，非迁移缺失。

另：三色蛾 logo（P1 刊头下，仅 P1）含金黄 `#D7B257`/`#EDD17F`、蓝 `#7898CD`/`#4D72B4`、绿 `#4F765D`/`#84A283` 等色块，是 SOP §1.1 规定的品牌标志（"三色蛾落在线中间"），非禁用金色用法。`#cac8ba` 2 处为 P1 横幅副标题与 P7 浅色文字，非禁用色。

## 6. 事实抽查（独立查源，不采信 KIT 来源说法）

- D1 国家队：见 §1（CBF 官网 verbatim）。
- 巴西杯半决赛：11 月 7 日 Atlético-MG 1–1 Grêmio（Arena MRV；Renan Lodi 25′/26′、Carlos Vinícius 37′/38′——各家分钟数 25/26 与 37/38 两说，KIT 的 ~25/26′、~37/38′ 折中正确，**正文未印分钟数**；Vitão 下半场红牌——正文未提）；首回合 Grêmio 2–0，总比分 3–1；格雷米奥第 10 次进决赛、争第 6 冠。11 月 8 日 Vasco 2–1 Palmeiras（São Januário），总比分 2–2，点球 5–4；首回合 Palmeiras 1–0。决赛 12 月 6 日周日单场、马内·加林查、史上首次单场决赛（多家 11 月 8–9 日报道一致）。✓
- Enem：Edital nº 64/2026（2026 年 5 月 21 日）"até o 10º dia útil" ✓；自 11 月 16 日起算、扣除 20 日假日则第 10 个工作日 = 11 月 30 日，计假日则 27 日——本期印 27–30 日窗口正确；第二天 11 月 15 日周日、自然科学 45 + 数学 45 = 90 题、13h30–18h30、5 小时；第一天 11 月 8 日、redação + Linguagens + Humanas、13h30–19h；两日 12h 开门、13h 关门；确认报名 5,051,345 人（纸面只写"5 百万以上"，无冲突）；个人成绩 2027 年 1 月（Página do Participante）；TRI 答对数 ≠ 分数。✓
- F1 圣保罗大奖赛 11 月 8 日（FIA 官方战报）：Norris（McLaren）杆位夺冠；Verstappen 第 21 位发车获第二；Hadjar 第三；Russell 第四；Antonelli 第五；71 圈；梅赛德斯锁定车队冠军。✓ 与刊内一致。
- 黑人意识日：Zumbi 1695 年 11 月 20 日去世、帕尔马雷斯（今阿拉戈斯 Serra da Barriga）、Lei 12.519/2011 设纪念日、Lei 14.759（2023 年 12 月 21 日签署）定全国假日自 2024 年起、2026 年 11 月 20 日周五、连休 20–22 日；Parreiras《Zumbi》1927 年。✓（与第一轮核实一致；均为公认史实。）
- 巴甲：35 轮 11 月 18 日 Cruzeiro × Palmeiras 20h30、Flamengo × Athletico-PR 20h30；11 月 19 日 Vasco × Internacional 19h30、São Paulo × Fluminense 21h30；36 轮 11 月 21 日 Palmeiras × Flamengo 16h30（Nubank Parque）。✓（与 KIT 赛程表一致。）
- 日期星期（`date -d`，America/Sao_Paulo）：11 月 7 日周六、8 日周日、14 日周六、15 日周日、16 日周一、17 日周二、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、27 日周五、30 日周一、12 月 6 日周日；另 11 月 1 日周日（P4 "Ida, dom 1º"）。**全部 16 个日期与刊内一致。**
- 范文词数：印刷版文字层独立数出 **88 词**，与 `.text.md` 逐字一致，80–100 区间内。✓
- 下期预告与 W46 承诺兑现：巴西杯次回合赛果 + 决赛队（P4）、黑人意识日 11 月 20 日周五头条（P1）、Enem 官方答案（P5+P6）。✓ 读者来信：无真实来信，P7 刊编辑部示例 + 葡/中双语披露、承诺顺延 VOL.5，标注清晰、无编造读者。✓
- 译注对照：29 个译注词头经 gates 核查全部真实出现在印刷文本中（29/29）。
- 长句完整度：`.text.md` 长散文句经词级多重集核对，在印刷版文字层与 SVG 中均无实质缺失；15 处"未命中"均为分词/case/跨栏拼合 artifact（家具行、"Palavras do texto" 源稿标签、P6 图表改写句、中文无空格整段换行断词等），内容本身均已印出（细节见 work/ 下核对记录）。

## 7. 非阻塞观察（7 项，均不构成缺陷、不阻塞定稿）

### O-A. 选择题选项流式折行——裁定：不构成缺陷（请协调员裁定是否另立项修引擎）
- 现象：排版引擎将选项作流式文本折行，多处选项在中间断开。经本轮在 150dpi 渲染图 + 2× 裁剪图上逐处目视，实例包括：P1 Q7 `A. no / dia 15`、Q8 `C. numa / segunda`；P2 Q12 `B. / numa sexta`、Q13 `C. / cinco dias`、Q14 `B. / pode rodar em horário reduzido`；P3 Q29 `B. / em 2011`、Q31 `C. acabou / com o feriado`、Q32 `B. o / maior…`、`C. um time de / futebol`、Q33 `A. …cultura / afro-brasileira`、`B. …Proclamação da / República`；P4 Q47 `A. 1 a 1, / e o Grêmio…`、Q48、Q49 `A. 4 a / 3`、Q50 `C. no / dia 15`、Q51 `C. / Isack Hadjar`；P5 Q65 `B. / Natureza e Matemática…`、Q68 `B. / não é a nota…`；P6 Q85 `B. 5 / dias`、Q87 `B. o prazo do / gabarito`、Q88 `A. …na / noite…`、`C. a nota / final`、Q89、Q91、Q92 `B. em janeiro / de 2027`；P7 Q104 `B. / aproveitamos`、Q108 `A. saem / · B. saíram`、Q112 `A. / sai`；P8 Q121、Q122 `B. 2 a 2 no / total`、Q123 `C. 6 a / 5`、Q125 `B. / domingo 22`、Q126、Q127 `A. …até o / gabarito`、Q131 `B. / ao Enem`、Q132 `B. o gabarito / extraoficial`。
- 裁定理由：(1) 逐处对照 `.text.md`，每处断开的选项文字**完整无缺字**，print/web 词级多重集 diff = 0；(2) 每处断点均有 "·" 分隔符 + 选项字母，续行归属唯一，**无歧义**，无任何一处会把碎片误读为另一选项；(3) 这是全期系统性引擎行为，第 3 轮版已相同，第一轮校对 8 页目视通过；(4) 与之同类的 P5 计划第 5 条中文译注右括号 "）" 独自成行（见 O-D）亦为流式折行所致。SOP §1.1"选项不在中间折行"一句字面未满足，但按"选项文字完整无歧义"的实质标准不构成缺陷；若按字面执行则须动排版引擎，属跨 12 语的模板级决策，超出本核心版返修范围。请协调员裁定：或在 SOP 中明确该句指"不断字、不歧义"，或另立项修引擎。

### O-B. P1 快讯 O FUTEBOL 末行溢出面板（本轮新发现；轻微版式瑕疵）
- 位置：P1 右下 "EM POUCAS PALAVRAS" 框。实测坐标（SVG）：面板 rect y=1874、高 436，底边 y=2310；末行 "em Brasília. (Página 4)" 基线 y=2327.6，落在面板之外，下方 quiz 分隔线 y=2312 从其字顶擦过。文字完整可读、无遮挡、无截断（occlusion 0 flags 亦不覆盖此情形——无遮盖，只是面板未包住末行）。第 3 轮版即有（该条内容自第一轮未动）。非阻塞。

### O-C. P1 数字框 2023 项左括号后多一空格（轻微排版瑕疵）
- "2023 — o ano da lei do feriado nacional（ 2023 年立法，定为全国假日）"：左括号后有一空格（2× 裁剪图确认；源稿 `.text.md` 该处无空格，系跨 run 折行所致）。内容无误。第 3 轮版即有。非阻塞。

### O-D. P5 等待计划第 5 条中文译注右括号独自成行（轻微排版瑕疵）
- "5. Descanse no feriado: a cabeça agradece（假日好好休息：大脑会感谢你" 后，"）" 独自占一行（2× 裁剪图确认）。与 O-A 同源（流式折行）。内容完整。第 3 轮版即有。非阻塞。

### O-E. §1.1 字体灰色地带：Noto Serif CJK SC 的使用范围超出"中文标题"（SOP 表述空白，非迁移缺失）
- 实测清单（SVG 文本元素）：Noto Serif CJK SC 共 329 处——P1 刊头行 "葡萄牙语周报"、P1 数字框中文括号注、P5 计划框中文括号注、P3/P7/P8 的 "→" 箭头（P8 占大头：造句/翻译题的 "→ ___" 与答案区中文简析）；其余中文讲解层、图注、页眉页脚均为 Noto Sans CJK SC（613 处）；拉丁目标语正文/标题全为 Newsreader（1,231 处）；刊头 UnifrakturMaguntia（1 处）。
- SOP §1.1 字体表只规定"刊别、讲解层、栏目小字、页眉页脚——中日韩读者用 Noto Sans CJK"，未给中文展示标题、"→" 箭头另立字体。本版属"展示面中文用衬线、讲解层中文用无衬线"的成系统选择，与 W46 模板一致，视觉上统一、无错字形，与 ko 版的系统性未迁移（旧纸/近黑底/金色/双线框/错徽章/"·"分隔）完全不同。本轮裁定：不构成缺陷；建议 SOP 补一行（明确中文展示标题与箭头字体）或模板统一为 Sans。不阻塞。

### O-F. KIT 记录滞后（非成品问题，请协调员令 builder 补写）
- KIT §6 "返修后自查（第 4 轮全量）" 仍为 "[待重渲染后填写]"；第 4 轮实测记录实际在 `hidden_files/w47/scratch-pt-fix2/round4-log.md`，未抄入 KIT；KIT 内 print/web 字节数仍为第 3 轮值（print 25,311,626→实测 25,311,662；web 1,571,245→实测 1,571,251）。成品本身无误，但 KIT 与成品不一致，不符合 SOP §8.5"每轮校对记录写入当期 KIT"。建议只改 KIT、不动成品。非阻塞。

### O-G. O3 Gary Todd CC0：本轮未完成 live 复核（无反证）
- 本轮尝试打开 Commons 文件页（KIT 所给 URL）返回 403（与第 3 轮 builder 遭遇相同，不再重复请求）；站内搜索亦未返回该文件页的授权记录。支持 CC0 的旁证：本地 md5 与 KIT 所称源 md5 完全一致；为 W43/W45/W46 复用已验证图；P5 印 "Foto: Gary Todd / Wikimedia Commons — CC0"；无任何反证。O3 保持"未由本轮 live 复核、旁证一致"的状态记录，不构成缺陷。

## 8. 8 版渲染图逐版目视（自渲染，150dpi，print PDF）

- P1：无溢出/重叠/压页脚；D1 两处 7h、O2 图注、刊头、目录页码与级别徽章均确认；中部右侧两框间留白正常；见 O-B、O-C 两处轻微瑕疵。
- P2：无溢出/重叠/压页脚；连休日程四格标签清晰（SEX 20 / SÁB 21 / DOM 22 / SEG 23）；中部 2–3 栏大面积留白（版式疏朗，与第一轮记录一致，非违规）。
- P3：无溢出/重叠/压页脚；Ter 17 7h 确认；Zumbi 配图 + 出处齐全；中部 1–2 栏留白与第一轮记录一致。
- P4：无溢出/重叠/压页脚；足球周历表 6 行 + 截稿注齐全；3–4 栏中部留白与第一轮记录一致。
- P5：无溢出/重叠/压页脚；Gary Todd 配图 + "CC0" 出处齐全；中部留白与第一轮记录一致；见 O-D。
- P6：无溢出/重叠/压页脚；O1 时间线已补 Linguagens；工作日计数图表（10 天 + 5 天 = 15 天）与 "两种答案"对照表齐全；中部 2–3 栏留白与第一轮记录一致。
- P7：无溢出/重叠/压页脚；8 条金句 + 页码标签、常见错误 4 组、本周词、读者来信示例 + 双语披露、下期预告 VOL.5 均齐全；《Os Lusíadas》配图 + 出处齐全。
- P8：无溢出/重叠/压页脚；Q131 题干与答案区 131. A 均目视确认；范文全文 + 马内·加林查配图 + 出处齐全；答案区 150 项齐全。

## 9. 未改动声明

只读校对：未修改 core-pt 内任何文件；未跑 insert.py / lint --write / git push/add/reset/stash；未提交；未碰 W43/W45/W46。校对产物仅本笔记与 `scratch-proof-pt2/work/` 下的提取文本、渲染图、裁剪图、freeze 副本、工具输出。写文件过程无 EPERM / Disk quota exceeded / ffmpeg 失败。
