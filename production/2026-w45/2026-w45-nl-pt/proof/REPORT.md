# W45 NL×PT 独立校对报告 — NOT PASS

- **结论：NOT PASS（1 项阻塞，见 B1）**。除 B1 外，其余 9 大项 gate 全部通过；B1 修复并复测通过后方可改为 ZERO PROBLEMS。
- **校对对象**：`files/weekly-report-w45-nl-pt/`（svg×8、cards×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- **对照**：W45 荷兰语核心 `files/weekly-report-w45-nl-core/`（VOL.2，150 题，页数 10/18/18/18/18/18/12/38，A2 47/B1 72/B2 31，范文 87 词）；W43 同配对版 `files/weekly-report-nl-pt/`（家具以 W43 实测为准）
- **校对方式**：从头独立重测，不采信构建员自述。工具一律用 `tools/venv/bin/python` 跑 `tools/freeze.py`、`tools/p8.py`、`tools/occlusion_audit.py`；另自写墨迹测量脚本（PIL getmetrics ascent/descent，anchor ls 基线锚定）做补充扫描与逐项裁定。
- **校对合规**：只校对，未改任何源码/交付物；未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录（只读对照）；未清理共享 scratch 目录（本次 scratch 仅用 `/tmp/proof-nl-pt/`，工具输出与测量脚本均在该处）。
- **开工查重**：首次检查时交付目录最新写盘为 21:45:09（WEEKLY-KIT.md），无进行中渲染进程；90 秒后复查零新写盘，判定为已完成交付的安全开工，未 stand down。
- **交付物指纹（校对前后两次实测一致，未被校对改动）**：
  - 印刷 PDF `De-Lucerna-VOL2-PT.pdf`：7,944,283 B，sha256 `2c763f659807e1dc1afb6d55c4b861a9d80e6231149bd1446a0b5ca2280216cb`，8 页
  - 网页 PDF `De-Lucerna-VOL2-PT-web.pdf`：3,674,911 B，sha256 `96c3fe710724b49cf666fc5802cd95e4a66b16c734c397a203ee737dc41aecc4`，8 页
  - SVG sha256 与构建员 `final-sha256.txt` 逐项一致（p1 `74255a72…`、p2 `f6d002f1…`、p3 `e8240f62…`、p4 `10ee2009…`、p5 `2ad4c8c0…`、p6 `23d95c54…`、p7 `3c070720…`、p8 `34582529…`）；卡片 8 张均为 1950×2700。

## 阻塞项

### B1（唯一阻塞）：P2 D 节指令行压穿整页版框，末字被框线切断

- **位置**：P2 `p2-leven.svg`，D 节（25–28 题）指令行，元素属性 `x=1647, y=1973, font-size=19.5, font-family=Noto Sans CJK SC, text-anchor=start`，文本 `Associe a palavra ao significado`。
- **实测墨迹**：基线锚定墨迹盒 `(l=1647.0, t=1957.25, r=1933.2, b=1978.0)`，advance 286.3px。
  - 内框右界 1910.6px（`x=40, width=1870` 内框 + 半线宽）：**超出 22.6px**；
  - 外框右界 1923.7px（`x=28, width=1894` 外框 + 半线宽）：**超出 9.5px**；
  - 页边 1950px 未超，因此 canonical `occlusion_audit.py` 的 EDGE 类不触发。
- **卡片目视**：P2 卡片同区域 2× 放大裁图确认，`significado` 末字母 `o` 被内外两道竖框线切断（字形横跨框线），属于“无截断” gate 的明确截断。
- **为什么工具 0 旗标漏掉了它**：版框 rect 绘在文件最前（idx 1、2），LINEX 只查“后绘”线条；BOXTITLE 排除宽 ≥ 页宽 95% 的整页框；EDGE 只查页边 1950。SOP 附则一明言“工具未覆盖的新维度（如右缘 advance 溢出扫查）由校对补充”——本项正是该维度。
- **为什么是分版新增缺陷、不是核心继承**：核心同槽位指令为中文短句 `把词和释义配对`，墨迹右界仅 1783.5px；葡语长句在同一 x=1647 起点单行排布，未换行/缩短，导致溢出。构建员目视只看了 P1/P6/P7/P8 卡片，P2 不在其目视集合内，与漏网位置一致。
- **修复方向（供构建员，不由校对执行）**：缩短该指令（如改用更短的葡语指令）或折为两行，使墨迹右界 ≤1885px 栏界；仅重渲染 P2 及下游 PDF/卡片；复测须重跑全页右缘扫描 + occlusion + P2 卡片目视，其余 7 页 SVG 与 PDF 指纹除 P2 衍生物外须与本报告所列 pin 一致。

## 分项实测（1–10）

### 1. 冻结 — 通过（B1 不影响本项）

- `freeze.py baseline`（核心构建目录 `hidden_files/weekly-report-w45-nl-build`，tools venv）：**8/8 SVG 字节复现**，核心哈希跑前跑后一致；校对前后核心 SVG 与分版 SVG 哈希均未变。
- `freeze.py diff`（独立重跑，与构建员输出逐行一致）：
  - p1 +31/−29，p2 +39/−33，p3 +32/−27，p4 +29/−25，p5 +39/−33，p6 +37/−32，p7 +47/−45，p8 +189/−175（串数为多重集实例数）；
  - 每页新增 CJK 均为 **0**，分版 CJK 总量每页均为 0（核心 191/212/153/126/214/192/373/1033 → 分版 0）。
- **被删串逐项裁定**（全部已删串均已过目；非中文串清单如下，其余被删串均含中文，属讲解层中→葡替换）：
  - P1 `DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS`：核心 P1 y=372 槽位荷兰语 strapline（19pt、非粗体、#57523f），被同槽位葡语徽章原位替换（见第 7 项，属性与 W43 徽章逐项一致），非正文冻结句丢失；
  - P8 `— PAGINA n —` ×8：家具分隔符，替换为 W43 同形 `— PÁGINA n —`；
  - P8 `104. blijf — rood = blijf binnen` → 分版 `104. blijf — rood = ficar em casa`：键 `blijf` 与代码 `rood` 逐字保留，仅注译葡语；
  - P8 `6. planten — veel mensen → planten` → 分版 `6. planten — Sujeito no plural, por isso planten`：键 `planten` 逐字保留，仅注译葡语；
  - P6 孤 `）`、P7 `bomen。` / `thuis。` / `zij zette vast。` / `。`：中文注换行碎片；其中 `bomen` 在分版 `«een boom» ou «bomen».` 中保留，`zij zette vast` 在 `= prender: zij zette vast.` 中保留，`thuis` 的情形见非阻塞观察 O1（完整句同页另有两处逐字出现，不构成冻结句丢失）。
  - **结论：无冻结荷兰语句丢失。**构建员“删串仅为徽章原位替换、PAGINA 家具、中文注换行碎片”的说法基本属实，惟 P8 两条注译行与 P1 副标题 token 变化（见 O3）须以本裁定为准。

### 2. P7 词框冻结 — 通过

- 定义句在分版 P7（x=1473）三行逐字保留，拼接后与目标完全一致：`«meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee.`（行：`«meedoen» betekent: deelnemen,` / `erbij zijn. In de Klimaatweek doet` / `heel Nederland mee.`，与核心逐行相同）。
- 仅 gloss 本地化：核心 `meedoen = 参加、参与：气候周全荷兰都参 / 加。` → 分版单行 `meedoen = participar.`，与构建员说法一致。
- 诊所纠正句荷兰语逐字保留（两处均核对）：
  - `→ «Een» is enkelvoud: «een boom» of` / `«bomen».`（核心 y=708.28/736.16，分版同文本）；
  - `→ Na «omdat» staat het werkwoord op` / `plaats 2: «... blijf ik thuis.»`（核心 y=918.32/946.20，分版 y=891.8/919.68，仅因上行葡语注缩为一行而整体上移，文本逐字相同）。
- 定义句未被本地化，不触发阻塞条件。

### 3. P8 — 通过

- `p8.py compare`（独立重跑）：核心 150 noted，分版 150 noted，**status CLEAN，missing=[]，extra_count=0，uncertain=[]**，keydiff `[7, 17, 70, 71, 76, 96, 137, 138, 148]`，与构建员输出一致。EXTRA_ONLY 不适用（集合相等）。
- keydiff 逐项对照印刷 P8 行（分版行含换行续行，已拼接核对）：
  - 伪影类（印刷 key token 与核心逐字节相同，仅注译葡语且行尾以括号结尾）：
    - 7：`B` 不变，核心 `7. B — 气候周共 7 天（11 月 2–8 日）` → 分版 `7. B — A Semana do Clima dura 7 dias (2–8 de novembro)`；
    - 17：`wortelen` 不变，`17. wortelen — wortelen = 生根（复数主语）` → `17. wortelen — wortelen = criar raízes (sujeito no plural)`；
    - 70：`eiland` 不变，`70. eiland — eiland = 岛（het）` → `70. eiland — eiland = ilha (het)`；
    - 71：`proef` 不变，`71. proef — proef = 比赛项目、考验（de）` → `71. proef — proef = prova, desafio (de)`；
    - 76：`gaat winnen` 不变，`76. gaat winnen — gaat winnen = 会赢（只是猜测）` → `76. gaat winnen — gaat winnen = vai vencer (só um palpite)`；
    - 96：`advies` 不变，`96. advies — advies = 建议（het）` → `96. advies — advies = conselho (het)`；
    - 148：`B` 不变，`148. B — zachte = 柔软的（土壤）` → `148. B — zachte = macia (solo)`。
  - 真实重定向类（翻译题按读者语重定向，符合 p8.py 规则）：
    - 137：核心键 `气候周持续七天。` → 分版键 `A Semana do Clima dura sete dias.`，译文正确（气候周持续七天）；
    - 138：核心键 `橙色预警意味着：做好准备。` → 分版键 `Código laranja significa: prepare-se.`，译文正确（橙色预警意味着：做好准备），续行 `Da página 2 · bereid je voor = prepare-se`。
  - 139/140 不在 keydiff 内已证实：`p8.py extract` 键逐字相等——139 核心/分版均为 `Museumnacht duurt van 19:00 uur tot 02:00 uur.`，140 均为 `Ik doe mee aan de Klimaatweek.`；其印刷行仅注由中文译为葡语（139 `— Atenção à…`，140 `— meedoen é um verbo separável`）。

### 4. 几何遮挡 — 工具通过，补充扫描发现 B1（见阻塞项）

- `occlusion_audit.py` 独立重跑（自检均通过，6 类 planted 阳性全触发、clean 对照静默）：分版 **0 旗标**，核心 **0 旗标**，`--core` NEW 对比 **0**。
- 自写墨迹碰撞扫描（同基线墨迹法）：COVER（后绘不透明形覆盖 ≥30%）**0 处**；TEXTX 按 canonical 阈值（宽 ≥3px 且高 ≥3px）**0 处**；FOOTER 命中仅为每页 2 条页脚本身（基线 2624，工具规则豁免，见下）。
  - 唯一亚阈值 graze 已裁定非缺陷：P8 `Associe a palavra ao significado`（墨迹 x1185–1471.25, y528.49–549.24）与 `Tekstmodel: Maandag 2 november…`（x1451–1876.75, y548.15–563.9）交叠仅 20.3×1.1px，高 1.1px < 3px 阈值，P8 卡片目视无可见碰撞（两行分属不同栏/不同基线）。
- P6 图表标签覆盖（基线锚定墨迹法重测，8 个标签逐项对后绘不透明形取最大覆盖）：`Ik blijf thuis/45`、`Ik kijk eerst naar de tekst/25`、`Ik ga toch naar buiten/20`、`Ik weet het niet/10` 均为 **0.0%**，远低于 30% 阈值；数值墨迹位置与核心逐项相同（45 y294、25 y352、20 y410、10 y468）。
- FIX3 重点复测（P1 词条注与 IN HET KORT 框）：
  - 注行单行：`«Clima»: o tempo e a natureza a longo prazo.`（x=1451, y=1846.3, fs19），advance **393.1px**（与构建员说法分毫不差），墨迹宽 393.0px；
  - 框：rect `(1451, 1874, 434×430)`，墨迹化框顶 1873.3px；注墨迹底 1851.05px，**间隙 22.25px，无覆盖、无截断**；
  - P1 卡片同区域 2× 裁图目视确认：注行完整清晰，框顶线在其下方，修复属实。

### 5. gloss 计数与金句 — 通过

- gloss 计数（按渲染后 SVG gloss 字符串本身拆 `·` 逐项计数，`Nota —` 起始块续行已拼接）：
  - P2：核心 6 = 分版 6，词头顺序一致（het klimaat / wortelen / besparen / de verwarming / de waarschuwing / lokaal）；
  - P3：5 = 5（het museum / de rondleiding / het tijdslot / tweedehands / de beurs）；
  - P4：5 = 5（de balans / gelijkspelen / de speelronde / de topper / de stand）；
  - P5：5 = 5（het eiland / de proef / stemmen / de aflevering / voorbij）；
  - P6：5 = 5（de meteoroloog / waarschuwingsmoeheid / vastzetten / het advies / de voorstander）；
  - 与核心 1:1，分版注均为葡语（如 P2 `het klimaat = clima · wortelen = criar raízes · … · lokaal = local.`）。
- P7 金句 8 句（荷兰语原文，不含 «»）：每句全页总出现次数恰为 **2**（源文章 1 + P7 «» 行 1），且在其标注页上各实测存在 1 次：
  - P1 `Van maandag 2 tot en met zondag 8 november is het Klimaatweek in Nederland`（P1 1 + P7 1）；
  - P1 `De herfst is de beste tijd om te planten`（P1 1 + P7 1）；
  - P2 `Geel betekent: let op, het weer kan gevaarlijk zijn`（P2 1 + P7 1）；
  - P3 `Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts`（P3 1 + P7 1）；
  - P4 `Ajax won donderdag 22 oktober met 2–0 van Atalanta`（P4 1 + P7 1）；
  - P5 `Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur`（P5 1 + P7 1）；
  - P6 `Een code is geen verbod, maar een advies`（P6 1 + P7 1）；
  - P6 `Het weer is van ons allemaal, maar het raakt ons allemaal anders`（P6 1 + P7 1）。
  - 页码标签序列与核心数字一致：Página 1, 1, 2, 3, 4, 5, 6, 6（核心为 Pagina 1, 1, 2, 3, 4, 5, 6, 6，词形按葡语加注音，与 W43 同形）。

### 6. 读者园地 — 通过，零编造

- P7 BRIEVEN VAN LEZERS 块逐行核对，页上同时具备三事实：
  1. 截稿时无真实来信；2. 无最佳 P8 作文；3. 示例 + VOL.3 承诺。
- 荷兰语披露句原文保留（4 行拼接）：`Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3.`（与核心逐字相同）。
- 葡萄牙语披露句同义：`Ainda não chegaram cartas reais nem os melhores textos da página 8 — por isso este exemplo; a promessa passa para o VOL.3.`
- 显性葡萄牙语邀请（祈使句 + 刊登承诺，内容预告行不算——本项为独立邀请行，已核对）：`Exemplo da redação — não é real. Envie suas cartas reais e seus melhores textos da página 8: vamos publicá-los no VOL.3!`，与构建员说法逐字一致（`Envie` 祈使 + `vamos publicá-los no VOL.3!` 承诺）。
- 示例标注为编辑部示例：`— Li (voorbeeldbrief van de redactie)` + `Exemplo da redação — não é real.`；示例信本身为核心荷兰语原文（Li 在上海学荷兰语、气候周在阳台种树），未编造新来信。

### 7. 家具（W43 实测对照）— 通过（分隔符字号差异见 O2，不阻塞）

- 徽章（P1）：分版与 W43 逐属性一致——`x=975, y=372, font-size=19.5, font-weight=700, fill=#a4553a（brick）, text-anchor=middle`，文本逐字相同：`TEXTOS EM NEERLANDÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA`。**未用 donor 的 20pt olive 形**，构建员说法属实。
- strapline 实际状态：核心同槽位（y=372）荷兰语 strapline 被徽章原位替换；W43 同配对版在同槽位使用完全相同的葡语徽章文本与属性，处理一致。
- P8 分隔符：`— PÁGINA 1 —` 至 `— PÁGINA 8 —` 齐全，粗细 700、颜色 #3e4c2a、栏位 x=65/527/989 排布与 W43 一致；字号分版 13.5pt vs W43/核心 14pt（见 O2）。
- gloss 前缀：P1–P6 均以 `Nota — ` 起始，fs20.5、#57523f，与 W43 同形（W43 Nota 亦为 20.5pt/#57523f）；P7 无 Nota 块（与 W43 一致）。
- P4 栏题：FIX4 后确为 `SPORT · Esporte`，`x=78, y=116, fs36, fw700, fill=#f3edda`，与 W43 逐属性一致。
- 页脚 8/8 标 VOL.2：每页 `De Lucerna · SEMANÁRIO NEERLANDÊS VOL.2 · TEXTOS EM NEERLANDÊS · EXPLICAÇÕES EM PORTUGUÊS`（x=65, y=2624, fs20, #57523f）+ `Página N de 8`（x=1885, y=2624）；除 VOL.2（W43 为 VOL.1，属正确卷号）外与 W43 形式一致。

### 8. 语言纯度 — 通过（FIX2 已修复）

- 全 8 页脚本重扫：CJK 0、平假名/片假名 0、韩文 0、西里尔 0、阿拉伯 0、希腊 0；英文星期/月份名 0（Monday…Sunday、October、November 均为 0）。
- FIX2 两处子串顺序污染已修复：`False:` 全页 0 处，`On Thursday` 0 处，`Thursday` 0 处；P8 真/假注均为荷兰语键 + 葡语注的正确顺序，如 `62. Niet waar — Falso: o NEC perdeu por 2–4`、`63. Niet waar — Falso: Twente–Ajax é às 13h30; 11h15 é Heerenveen–Feyenoord`。
- 误报逐项排除：`O ADE`（2 处）与 `O Ajax`（2 处）均为葡语冠词 + 专名（如 `67. C — O ADE fez 30 anos este ano`、`47. B — O Ajax venceu o Atalanta por 2–0`），非污染；P1 `Pagina 2` 为荷兰语正文交叉引用（荷兰语 pagina，无注音，属目标语正文）；P6 `les` 为荷兰语正文 `de les`（课程/教训），非他族残留。
- P8 答案注释：150 条已逐条过目，注层为纯葡萄牙语（荷兰语键、荷兰语例句、语法术语与专名除外）；另 `Nota em português em cada resposta · ✓ = com modelo` 与实际一致。
- 构建员“FIX2 修复 5 处漏译与 2 处子串顺序污染”的说法在终态得到证实：终态无中文残留、无 `False:`/`On Thursday` 残留。

### 9. 其他 — 除 B1 外通过

- 图片：仅公有领域/CC0，每照片页恰 1 个 `<image>`（P1 herfstbos、P2 kinderdijk、P3 gracht、P4 elftal1912；P5–P8 无照片，与核心一致）；署名行均已排版且与 KIT 所述 Commons API Artist 字段一致——P1 `Foto: Vovogov90 — CC0`、P2 `Foto: Nationaal Archief — CC0`、P3 `Foto: W. Punt / Anefo, Nationaal Archief — CC0`、P4 `Foto: Spaarnestad Photo / Wikimedia Commons — publiek / domein`（两行，与核心同形）。
- 全文 `桥接` 0 处、`讲解` 0 处（8 页 SVG 文本层统计）。
- ABSTRACT.txt：单行（strip 后 1 行）、无 ASCII 双引号；含真实主题关键词（Semana do Clima、Noite dos Museus、Crossing Border、Eredivisie、Expeditie Robinson）与学习者搜索短语（`aprender neerlandês lendo`），含 VOL.2、A2–B2、150 练习；全文：`De Lucerna, semanário em neerlandês VOL.2: a Semana do Clima nos Países Baixos de 2 a 8 de novembro, a Noite dos Museus em Amsterdã, o festival Crossing Border, a 12.ª rodada da Eredivisie e o Expeditie Robinson, com textos em neerlandês e explicações em português para aprender neerlandês lendo, níveis A2 a B2, 150 exercícios.`
- 卡片 8 张逐页目视（构建员只看了 P1/P6/P7/P8，本校对看了全部 8 张）：P1、P3、P4、P5、P6、P7、P8 无重叠、无截断；P2 除 B1 外其余部分正常（D 节选项 c 行见 O4）；P1 FIX3 部位裁图复核通过（见第 4 项）。
- 终态一致性：P1 头条流尾与核心逐行同基线（`1437.8 … 1814.8`，末行 `open tot 02:00 uur) en in Den Haag`）；数字框 4 项词头相同（7、200、70+、9），框体因葡语注更长而下移加高（核心 y1303.475/h434 → 分版 y1333.2/h461，底 1794.2，KIT 不等式 1333.2+461+12=1806.2 < 1828 成立，无溢出）；练习行数与核心一致（题号元素计数每页与核心相等，P3 多出的 `3.` 见 O5）；KIT 计数与核心 KIT 一致（10/18/18/18/18/18/12/38，总 150，A2 47/B1 72/B2 31，范文 87 词且与核心范文逐字相同）。

### 10. 过程合规 — 通过

- 校对全程未清理共享 scratch 目录；未向 weekly-git、Discord、主聊天、cron 做任何写入或投递；核心与 W43 目录仅只读。

## 与构建员自述不符处

1. **实质性不符（即 B1）**：构建员 canonical 工具“0 旗标”属实但不完整——补充右缘扫描发现 P2 框线溢出；构建员目视集合（P1/P6/P7/P8）恰好不含 P2，与漏网一致。
2. **其余自述均经独立重测证实**：freeze 8/8 与 CJK 0、P8 CLEAN 与 keydiff 集合、FIX3 393.1px、FIX2 修复、徽章 19.5pt/700/brick、P4 `SPORT · Esporte`、gloss 计数、页脚 VOL.2、图片署名——以上全部与实测一致，无其他实质性出入。

## 非阻塞观察（注明：不阻塞）

- **O1 — P7 诊所葡语注尾省略 `thuis`（不阻塞）**：分版 `Na oração principal, o verbo fica em 2.º lugar: blijf ik.` 对比核心中文注 `omdat 从句后，主句动词在第二位：blijf ik thuis。`，葡语例证缺 `thuis`。实测完整形 `lugar: blijf ik thuis.` 仅 167.4px，远小于 412px 栏宽，故非版式所迫；但该句语义完整（动词第二位已由 `blijf ik` 示出），且完整句 `blijf ik thuis` 同页另有两处逐字出现（错句 `«Omdat het regent, ik blijf thuis.»` 与荷兰语纠正句 `«... blijf ik thuis.»`），不构成冻结句丢失。建议下次修复轮顺手补回，不阻塞本期。
- **O2 — P8 分隔符字号 13.5pt vs W43/核心 14pt（不阻塞）**：文本、粗细、颜色、栏位均与 W43 一致，仅字号小 0.5pt 且 y 流因重排而异；无重叠、无溢出，形式正确。
- **O3 — P1 副标题 donor 缩短，缺 MUSEUMNACHT token（不阻塞，KIT 已披露）**：分版 y=330 副标题为 `WEEKBLAD IN HET NEDERLANDS · VOL.2 · KLIMAATWEEK · SPEELRONDE 12`，核心同行含 MUSEUMNACHT token；KIT 称完整荷兰语题行实测 1958.8px 超 1820px 内宽故缩短。副标题为家具行，MUSEUMNACHT 仍见于头条、目录与 P3 全版，不构成内容丢失。
- **O4 — P2 选项 c 行超栏界但未出框（非缺陷）**：`c. voor je eigen omgeving, niet overal` 墨迹右界 1901.5px，超 1885px 栏界 16.5px，但未超内框 1910.6px，且几何与核心逐字/逐坐标相同（同 x=1485、同文本），属核心继承版式，卡片上完整可见。
- **O5 — P3 题号 naive 计数 19 vs 18 的解释（非缺陷）**：多出的 `3.` 是 D 节葡语指令换行残行（`Calcule: responda com os números da página` / `3.`），核心中文指令为单行；不是一道题，P3 实际题数仍为 29–46 题共 18 题。

## 复测要求（B1 修复后）

1. 仅改 P2 D 节指令的措辞/换行，使其墨迹右界 ≤1885px；重渲染 P2 卡片与两份 PDF。
2. 复测：全页右缘扫描（内框 1910.6/外框 1923.7 双阈值）0 溢出 + `occlusion_audit.py` 0 旗标 + P2 卡片目视（指令行完整、不压框线）。
3. 其余 7 页 SVG 与 PDF 指纹除 P2 衍生物外须与本报告所列 pin 一致；任一 gate 回退即仍为 NOT PASS。
