# A Lucerna — VOL.2 · PT × IT（葡萄牙语正文 + 意大利语讲解）

Lucerna 学习者周报 · W45（2026-11-02 周一 – 11-08 周日）葡语版的意大利语讲解版。
语言组合（一对一）：正文 = 巴西葡萄牙语（冻结核心版 VOL.2，逐字未动）；讲解 = 读者的母语意大利语（小字灰色注、题面意语说明、答案意语简析）。
刊头：**A Lucerna**（与核心版一致）。主题：Enem 周——Finados 连休（10 月 31 日–11 月 2 日）+ 11 月 8 日 Enem 第一天 + 巴西杯半决赛次回合周末。

- P1 徽章（砖红行）：«TESTI IN PORTOGHESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI»
- 页脚：«A Lucerna · SETTIMANALE PORTOGHESE VOL.2 · TESTI IN PORTOGHESE · SPIEGAZIONI IN ITALIANO» / «Pagina N di 8»
- 状态：**构建方全量自校完成（本 KIT §8–§11）；独立校对尚未进行，不自我认证定稿**。

## 1. 基线证明（冻结核心复现）

方法：tools/freeze.py baseline（复制核心构建目录、改指输出路径后运行，产物与核心交付 SVG 逐字节比对，跑后复验核心未动）：**8/8 逐字节相同**。

| 版 | SHA-256 前 16 位（核心交付件 = 基线复现） |
|---|---|
| P1 | 0dc8089df727dfe4 |
| P2 | 56db3aa80e1318db |
| P3 | 82f6fc3a94fbc11e |
| P4 | c5647cf6e9c080ec |
| P5 | 92e86020ce81f3c8 |
| P6 | e6097473ded2f016 |
| P7 | a72cb75a519319f4 |
| P8 | 82630480322959ad |

完工后复验：核心版 8 个交付 SVG 的 SHA-256 与上表一致，核心目录未被本版制作触碰。

## 2. 改动范围与制作基底（仅讲解层）

- **基底说明**：本版以已验证的 W45 PT×EN 分版构建目录为起点（同核心、同版式、拉丁讲解层），经 transform.py 把英文讲解层逐字替换为意大利语，再按 W43 PT×IT 实测家具校准。选择 EN 基底而非直接改中文核心，是因为 EN 版已为本核心证明过拉丁讲解层的版式；但冻结性不依赖基底信任——§6 的 freeze diff 以核心为准逐项裁定，全部非讲解层差异均为登记在案的家具/重排碎片，葡萄牙语正文零改动。
- 全部英文讲解（词注、题干说明、练习 apparatus、P8 全部 150 条答案简析、栏目标题的英文部分、E VOCÊ 框意语问句、P7 金句的译文行）译为意大利语。
- 葡语正文、标题、题面、选项、图表、图片、版式几何全部冻结（§6 裁定）；P7 词框中的葡语定义句逐字保留，仅 gloss 本地化为意大利语（阻塞门，见 §6）。
- 讲解行方法为 `gloss()` 前缀 `Nota — `（W43 PT×IT 实测）；禁用词（中间环节称谓，中英文形式）在本版报纸、KIT、构建代码中出现次数为 **0**（原始字节扫描核验）。
- 终版 8 个 SVG 可见文本中 CJK / 全角字符节点数 = **0**（程序扫描，逐页皆 0）；新增 CJK = **0**（freeze.py --strict-cjk）。
- 注册表 `type` 字段为不渲染的内部元数据，意语化为 Completa la frase / Scelta multipla / Abbinamento lessicale / Forma la frase / Vero o falso / Cloze / Traduzione / Scrivi（与全部已定稿讲解版同一做法）；报面零呈现。
- 答案简析中的括号一律半角，括号前留空格（如 «(ora di Brasilia)», «(c)»）；核心版全角冒号 `：` 在讲解层范式注中统一为半角 `:`（如 102 题，见 §6）。

## 3. 意大利语家具（逐字记录，宽度均以制作字体实测，渲染后 SVG 为准）

家具准绳为 W43 PT×IT 的实测 SVG（胜过工具 README 泛写）；凡与 W43 不一致处均在 §4 说明理由。

| 位置 | 字符串 | 实测 |
|---|---|---|
| P1 徽章（19pt 粗 sans，砖红 #a4553a，y=372） | TESTI IN PORTOGHESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI | 827.0px ≤ 1820 |
| P1 副刊头（36pt serif 粗，y=330） | SETTIMANALE PORTOGHESE · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE | 1695.8px ≤ 1820 |
| P1 顶栏中（21pt sans） | TODA SEMANA EM PORTUGUÊS · OGNI SETTIMANA · IL PORTOGHESE DEL BRASILE | 824.4px |
| P1 band 右 | SETTIMANA DELL'ENEM / 2 nov., weekend di Finados · 8 nov., primo giorno dell'Enem | — |
| 页脚左（20pt sans） | A Lucerna · SETTIMANALE PORTOGHESE VOL.2 · TESTI IN PORTOGHESE · SPIEGAZIONI IN ITALIANO | 952.1px |
| 页脚右 | Pagina N di 8 | — |
| 词注前缀 | Nota — | — |
| P1 数字框头（20pt sans 粗） | A SEMANA EM NÚMEROS · IN CIFRE | 351.7px ≤ 框内 390 |
| P1 目录框头（24pt sans 粗） | NESTA EDIÇÃO · SOMMARIO | 338.6px ≤ 框内 390 |
| P7 错误框头（23pt sans 粗） | ERROS COMUNS · ERRORI | 303.1px ≤ 框内 390（与 W43 实测 303px 一致） |
| P7 金句框头（27pt sans 粗） | FRASES DA SEMANA · FRASI DELLA SETTIMANA (tratte parola per parola da questo numero) | 1211.6px ≤ 1820 |
| P6 图表框头（26pt sans 粗） | O DOMINGO 8 EM NÚMEROS · I NUMERI DI DOMENICA 8 (orari ufficiali Inep) | 962.2px ≤ 1820 |

栏目标题（PT · IT，与 W43 形式一致）：VIDA · VITA QUOTIDIANA；CULTURA · CULTURA；ESPORTE · SPORT；JOVENS · GIOVANI；APROFUNDAMENTO · APPROFONDIMENTO；LÍNGUA · LINGUA；AVALIAÇÃO E RESPOSTAS · ESERCIZI E RISPOSTE。
栏目副标题（PT 短语 · IT 短语，19pt，实测均 ≤ 1500px）：P2 «NÍVEL A2 · Finados e revisão: o feriadão do Brasil · Finados e ripasso: il lungo weekend del Brasile» (875.7px)；P3 «A2 → B1 · Finados: o dia da memória · Finados: il giorno del ricordo» (614.9px)；P4 «NÍVEL B1 · A semana do futebol · La settimana del calcio» (517.8px)；P5 «NÍVEL B1 · A reta final dos jovens · Il rettilineo finale dei giovani» (576.6px)；P6 «NÍVEL B2 · O Enem explicado · L'Enem spiegato» (437.5px)；P7 «Três níveis, três ferramentas · Tre livelli, tre strumenti» (479.6px)；P8 «Pagina 8 · A grande prova da semana + todas as respostas» (517.7px，沿 W43 形式，描述语沿用葡语原文）。
练习标签（W43 实测形式）：Completa / Abbina / Forma la frase / Traduci / Scrivi / Vero o falso。
P8 分隔符沿核心/W43 形式：«— PÁGINA {n} —»（不采用 tables.json 的泛写 PAGINA 式；W43 PT×IT 实测即 PÁGINA 式）。
P7 金句页码签沿核心形式：«Página N»（不改为意大利语 Pagina；W43 PT×IT 实测即 Página 式）。
目录行级别签 «todos» 保留（W43 PT×IT 实测亦为 todos）。

## 4. 与 W43 / 核心不一致处（逐项理由）

1. 页脚与副刊头为 VOL.2（W43 为 VOL.1）：本期核心即 VOL.2，期号跟核心走。
2. P1 数字框头字号 20pt（核心 23pt）：意语标题 20pt 实测 351.7px，线性推算 23pt 约 404px > 框内 390，沿 EN 版对同一框的同类改动降为 20pt。
3. P7 金句行距 104 → 92：意语读者园地堆叠高于英文版，金句第 4 行译文撞入下期预告深色框（首轮审计真缺陷，见 §8）；行距收紧后行间仍有 42.3px 空隙。
4. P7 读者园地邀请句缩短（4 行 → 3 行）：同上修复的一部分；祈使句 + VOL.3 刊登承诺均保留（见 §7）。
5. 副刊头字号 36pt（核心中文槽位 40pt）：沿 W43 PT×IT 同槽位 36pt 实测；本期副刊头实测 1695.8px ≤ 1820。
6. 徽章颜色砖红 #a4553a（EN 版为橄榄绿）：W43 PT×IT 实测徽章即砖红，家具以 W43 为准。
7. P8 副标题沿 W43 形式用葡语描述语（«Pagina 8 · A grande prova da semana + todas as respostas»），而非英文版的英文描述语。

## 5. 体量与题量（与核心版逐项一致）

- **总计 150 题**，统一编号 1–150 连续无缺重；分级 **A2 49 · B1 70 · B2 31**；分版 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38；题型分布与核心版完全相同（完成句子 61 · 单选 49 · 完形单选 13 · 词汇配对 12 · 造句 7 · 翻译 4 · 判断对错 3 · 写作 1）。
- 写作范文 93 词（程序计数，与核心版一致；题面 80–100 词区间内）。
- 构建日志：FLOW OVERFLOW 0 · HEAD TOO WIDE 0（两轮皆然）。

## 6. 冻结核验（freeze.py diff，--strict-cjk）

- 新增 CJK = **0**；终版 CJK = 0（8 页逐页 0）；全文「桥接」= 0。
- 非 CJK 的删除串仅 14 项，逐项裁定如下（其余删除串全部含 CJK，即中文讲解层本身）：
  - P1 副刊头 strapline（葡语标语行）：被配对徽章替换，属登记家具。
  - P1 数字框条目碎片 «12h — os portões abrem no domingo 8（»、P5 计划框碎片 «5. Domingo 8: chegue antes das 12h（»、P6 桥接碎片 «chamada · local · conferir»：均为中文注长度变化导致的重排碎片，葡语成分在本版对应行中逐字存在（已逐项 grep 核实）。
  - P2 栏目副标题葡语短语：本版副标题为该短语 + 意语短语的加长串，短语本身逐字保留。
  - P8 9 项（16、17、18、19、57、58、101、102、103 及 139 碎片）：键（key token）与核心逐字节相同；差异仅为简析语言（中文→意语）与全角冒号→半角冒号的讲解层记号统一，或重排碎片。139 题键 «O feriadão é de 31 de outubro a 2 de novembro.» 未动（变的是题面，见 §9）。
- P7 词框冻结（阻塞门）：P7 无 gloss 词框定义句本地化问题——P7 三栏讲解与错误框注均为讲解层；P7 金句葡语原文逐字保留（§7）；P2–P6 的 5 个 gloss 词框中葡语词条逐字保留，仅释义译为意大利语（§7 计数）。
- 完工后复验核心 SHA（§1 表）全部未变。

## 7. Gloss、金句、读者园地（逐项实测）

- **Gloss 计数**（按渲染后 gloss() 字符串本身拆 `·` 逐项计数）：P2 6 · P3 6 · P4 5 · P5 5 · P6 4，合计 **26 = 核心 26**，逐文件一致；26 个词条全部在渲染 SVG 中实测存在。
- **P7 金句**：8 条逐字连续、页码标注 (1, 1, 2, 3, 4, 5, 6, 2) 与核心版一致；程序计数（去 «»、空白归一）每条在全期恰出现 **2 次**（源版 1 次 + 第 7 版 1 次），且每条在其标注页上实测存在；核心版同法计数亦为 2 次。
- **读者园地（零编造）**：无任何虚构读者/来信/人名/引言。页上同时有三事实：(1) 截稿时无真实来信（葡语披露句原文保留 + 意语披露句同义）；(2) 无最佳 P8 作文（同上两句均含「melhores textos / migliori testi」）；(3) 示例 + VOL.3 承诺（示例标注 + 顺延句）。显性意大利语邀请为独立行：«Esempio della redazione — non è una lettera vera. Mandate le vostre lettere: le migliori saranno pubblicate nel VOL.3!»（祈使句 Mandate + 刊登承诺 saranno pubblicate nel VOL.3；内容预告行、他页练习提示均不计入）。示例标注为编辑部示例（«— EXEMPLO DA REDAÇÃO» + 意语 «Esempio della redazione — non è una lettera vera»）。

## 8. 几何遮挡审计（出厂门槛，制作方自查）

工具：tools/occlusion_audit.py（先过自检：6 类植入缺陷全部命中、干净对照零误报）+ 自研同基线/框线扫描（gates-scan.py，制作同款 PIL 字体实测墨迹）。

- **首轮**：审计 3 个标记，全部为同一真缺陷——P7 金句第 4 行意语译文基线 2441.67 落入下期预告深色框（框顶 2404）：COVER 2 + TEXTX 1。修复（transform.py FIX2，见 §4.3–4.4）：邀请句 4 行→3 行 + 金句行距 104→92；P7 栏底 1949.0 → 1920.0。
- **终轮**：审计 **0 标记**；核心版同法审计 0 标记；NEW vs 核心 **0**。
- 同基线墨迹碰撞扫描（同基线文本节点墨迹重叠）：**0 标记**。
- 页框/右缘扫描（全部 8 页墨迹右界 vs 内框线 1910 / 外框线 1922 / 页边 1950，右对齐行以 advance 法判定）：**0 越界**。
- 框线压字扫描：1 个标记，经裁图裁定为**测量伪报**——P3 日历框末行 «Palmeiras, a volta.» 的 PIL 全升部墨迹框（顶 553.2）触及框底线 555.5，但成图像素实测字形墨迹顶在框线之下、框线从两行之间干净通过、无一字被划；且该行坐标与核心版、EN 版逐字节相同，属冻结核心版式原样，不动（改动将破坏冻结）。
- P6 图表标签覆盖（基线锚定墨迹法：PIL getmetrics ascent 24 / descent 6，anchor ls）：3 条标签墨迹 vs 后绘条形覆盖率均为 **0.00%**（<30% 过）；3 条数值文本与条形重叠 0。

## 9. 答案键差异登记（key-diff registry，完整）

tools/p8.py compare：**CLEAN，150 = 150**，无缺失无多余；keydiff 18 项逐项对照印刷 P8 行核实如下：

- **真实重定向（2 项，翻译类按讲解版惯例重新指向读者语言）**：
  | 题号 | 类型 | 核心版 | 本版 |
  |---|---|---|---|
  | 137 | 翻译（葡→读者语） | 键 = «11 月 8 日周日是高考的第一天。» | 键 = «Domenica 8 novembre, è il primo giorno dell'Enem.»（键改意语；题面葡语原句不动；注 «Vedi il titolo di pagina 6»） |
  | 138 | 翻译（葡→读者语） | 键 = «周日前核对确认卡。» | 键 = «Controlla la tessera prima di domenica.»（注 «Conferir = controllare, verificare»） |
  | 139 | 翻译（读者语→葡） | 题面中文句 → 键 «O feriadão é de 31 de outubro a 2 de novembro.» | 题面 = «Il lungo weekend va dal 31 ottobre al 2 novembre.» → 键不变（注 «feriadão = il lungo weekend di festa»） |
  | 140 | 翻译（读者语→葡） | 题面中文句 → 键 «Quando você chegar, apresente o documento com foto.» | 题面 = «Quando arrivi, mostra il documento con foto.» → 键不变（注 «congiuntivo futuro chegar + imperativo apresente»） |
  | 150 | 写作 apparatus | 键 = «✓ + 中文注» | 键 = «✓»；注 = «Vedi il testo modello nella sezione H di questa pagina (93 parole)»（p8.py 两版键同为 ✓，故不在 keydiff 内） |
- **p8.py 括号分支提取伪影（16 项，非真实键差异）**：2、4、25、26、27、28、52、53、54、55、101、141、142、143、144、146。机理：dash 体答案的简析尾带括号（如 «(c)», «(sezione)»）时，工具取括号前整段为“键”，于是意语简析与中文简析必然不同；逐项对照印刷行证实每项的真实键 token（第一个 « — » 之前）与核心逐字节相同（如 2 题 «portões»、25 题 «c»、146 题 «A»）。
- P8 答案注释全部为意大利语（葡语词仅作语法范式引用，如 «conferir: ele → confere»）；P8 印刷注释集合 150/150。

## 10. 图片与授权（与核心版相同）

终版 SVG 内嵌图片载荷与核心版逐字节相同（SHA-256 前 16 位 fd231e77993f09e0）：

- P1 图书馆复习学生（estudo.jpg）— CC0，Gary Todd / Wikimedia Commons；版面 credit 行 «Foto: Gary Todd / Wikimedia Commons — CC0» 已排版在 P1 图说下方（目检确认）。
- 其余版面以核心版自制图表与信息图撑版（P1 时间表、P2 四格时间表、P4 足球周历表、P6 分钟条形图与两周日对照表），无新增图片、无其他署名图片。

## 11. 文件与复现

- 交付：`svg/`（8）、`cards/`（8 PNG，1950×2700）、`A-Lucerna-VOL2-IT.pdf`（印刷版，**3,469,993 B**，8 页，SHA-256 `ddedb5135e74f7f3b8ffe11979b53997825fe718f35fb134e0e3a37e84110b0f`）、`A-Lucerna-VOL2-IT-web.pdf`（网页版，**3,483,035 B** < 10 MB，8 页，SHA-256 `6cab53914433d2e6f733aa23b4c14bfc6eb362e0eafd5acce077b14ec40d1a1a`）、`WEEKLY-KIT.md`、`ABSTRACT.txt`（意大利语单行、无 ASCII 双引号）。
- 制作源码：`hidden_files/weekly-report-w45-pt-it-build/`（bslib4.py、svglib.py、content12/34/56/7/8.py、run.py、render.py、transform.py、gates-scan.py、BUILD-LOG.md、各轮 sha256 基线、freeze-diff.json、occlusion-*.json、gates-scan.json）。
- 复现：先取 W45 PT×EN 构建目录复制为本构建目录并改指 OUT/BASE 至 weekly-report-w45-pt-it，再运行 transform.py（一次），然后单进程 `run.py` + `render.py`。**解释器：tools/venv/bin/python（Python 3.12.3，PIL 13.0.0，含 cairosvg；系统 python3 无 cairosvg，不可用）**。transform.py 内含全部修复轮（FIX 顺序遮蔽修复 + FIX2 P7 修复），不得只改 content 文件。
- 8 张卡片逐页目视检查：P1–P8 全部看过，无重叠、无截断、无压框（P3 日历框末行沿框线外为核心原样，见 §8）；页数 8（4 的倍数）、页脚 8/8 标核心 VOL 号（VOL.2）、配对徽章/页眉页脚齐全。
- 跨族残留重扫：中文残留 0（逐页证实）、西里尔/韩文/假名 0、英文独立词 0（仅有的 COMPLETE 两处为核心冻结葡语栏目标题 «COMPLETE COM OS NÚMEROS» / «COMPLETE A CRÔNICA»，与核心逐字节相同）、英文 gloss 前缀 «Note |» 0、«Page N of» 0。
- 未做：未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录（只读对照）；入仓与发布由主线安排（届时需 insert.py + lint 门槛）；本版不自我认证定稿，仍需一次全新完整独立校对。
