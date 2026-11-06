# 独立校对报告 — Lucerna Weekly W45 DE×PT（目标德语 × 母语葡萄牙语）

**结论：不可定稿（NOT FINALIZABLE）—— 编号问题 2 项，均为阻塞问题。**
修复后须重渲染并重跑全部门禁，方可定稿。本报告不宣称上架（上架由协调员串行执行）。

- 校对对象：`files/weekly-report-w45-de-pt/`（svg×8、cards×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照核心：`files/weekly-report-w45-de-core/`（VOL.2）
- 参照：`files/weekly-report-de-pt/`（W43 已发同配对版）、`tools/README.md` #7–#22、SOP
- 校对方式：全部关键断言均从渲染产物/SVG 坐标独立重测；构建员自述（KIT）一律未采信，仅作比对靶子。
- 本报告证据目录：`hidden_files/w45/de-pt-proof/scratch/`（freeze-diff-proof.json、occlusion-proof.json、baseline-de-core/）
- 未做事项：未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录、未改任何源码、未派生下级代理。

## Stand-down 检查

- 开工前 `files/weekly-report-w45-de-pt/` 与 `hidden_files/weekly-report-w45-de-pt-build/` 无进行中写盘、无进行中渲染进程；
  95 秒后复查零新写盘（最新 mtime 仍为 20:59 的 KIT/ABSTRACT，SVG 20:56、PDF 20:49–20:50），属已完成交付的新鲜时间戳，正常开工。
- 复查时段另有一无关进程在跑（`weekly-report-w45-de-ja-build` 的 render.py），属另一分版，未触碰。

## 编号问题清单（阻塞）

### 问题 1（阻塞，门 1 冻结失败 + 补充必查门）：P7 NOCH EIN WORT 框的德语定义句被本地化，冻结违规

- 核心 P7 原文（`files/weekly-report-w45-de-core/svg/p7-sprache.svg`，词框标题 `NOCH EIN WORT · 再学一词` 之后）：
  - `«der Tankrabatt»（Seite 2）: die`
  - `gesenkte Steuer auf Benzin und Diesel.`
  - 讲解层 gloss：`油价减税。`
- 本版实测（`files/weekly-report-w45-de-pt/svg/p7-sprache.svg`，标题 `NOCH EIN WORT · Mais uma palavra` 之后）：
  - `«der Tankrabatt» (página 2): o imposto`
  - `reduzido sobre a gasolina e o diesel.`
  - `Desconto no combustível.`
- 判定：德语定义句 `die gesenkte Steuer auf Benzin und Diesel.` 被删除并译成葡语，仅剩词头 `«der Tankrabatt»` 为德语；
  页码参照亦由 `Seite 2` 改为 `página 2`。这不是讲解层改写，是冻结的德语正文被改写。
  我独立跑的 freeze diff 也印证：P7 removed-no-CJK 串中除家具/标点外，恰有
  `«der Tankrabatt»（Seite 2）: die` 与 `gesenkte Steuer auf Benzin und Diesel.` 两项无法归入讲解层/家具。
- 同族对照（均直接实测 P7 SVG）：
  - DE×EN：`«der Tankrabatt» (Seite 2): die` + `gesenkte Steuer auf Benzin und Diesel.` + gloss `Fuel discount.`——德语句逐字保留；
  - DE×ES：同上德语句逐字保留 + gloss `El descuento en la gasolina.`；
  - DE×IT：同上德语句逐字保留 + gloss `Sconto sul carburante.`。
  - DE×FR：与本版同类本地化（`la taxe réduite sur l'essence et le diesel.`），但 DE×FR 本身未定稿，按补充 brief 不能作放行先例。
- KIT §1(c) 称该本地化 “as in DE×EN”——**实测为假**，DE×EN 保留德语原文。
- 修复方向：恢复德语句逐字（半角括号形式与同族一致）：
  `«der Tankrabatt» (Seite 2): die gesenkte Steuer auf Benzin und Diesel.`，保留葡语 gloss 行
  `Desconto no combustível.`；随后重渲染并重跑全部门禁（P7 栏高需重核，当前右栏墨迹终值见门 5）。

### 问题 2（阻塞，门 2/门 9 讲解层语言纯度）：P8 答案注文 item 5 含英文残留

- 实测（`p8-uebungen.svg` 第 186–187 行，P8 卡面“— Página 1 —”答案区肉眼亦可见）：
  - `· 5. neun(9 matches on matchday 9) · 6. Tankrabatt(desconto vai até 31 de`
- 核心对应注文：第 9 轮共 9 场。正确葡语形式应如 `9 jogos na 9ª rodada`（与 P1 Zahlen 框已用表述一致）。
- 判定：葡语版答案注文混入英文 `matches on matchday 9`（DE×EN 适配残留），违反“P8 答案注文全程葡萄牙语”，
  且与 KIT §10 “no leftover English tokens (expanded list)” 的断言直接矛盾。
  全 8 页 SVG 定向英文残留扫描（matches/matchday/care home/This week's big questions 等）仅此一处命中；
  `Quiz-relâmpago` 为葡语借词，属合法，不计。
- 修复方向：将该注文改为纯葡语；重渲染 P8 并重跑门禁（P8 哈希与双 PDF 随之变化）。

## 各必查门实测值

### 门 1 Freeze：除问题 1 外通过

- 我独立跑 `tools/freeze.py baseline`（核心 build 拷贝至 scratch 重渲染）：**8/8 字节复现**；
  核心 SVG 重哈希与 KIT §2 “before” 值逐字节一致（p1 `6cbd4802…`、p2 `9362256d…`、p3 `3e8a8d16…`、
  p4 `b787f592…`、p5 `4dcbeb97…`、p6 `01b75ad4…`、p7 `fbaf8cdd…`、p8 `299524bd…`），核心未被触碰。
- 我独立跑 `tools/freeze.py diff`：与构建员数字完全一致——P1 +24/−23、P2 +36/−32、P3 +40/−40、P4 +25/−22、
  P5 +42/−39、P6 +37/−33、P7 +61/−54、P8 +161/−141；**新增 CJK 全 8 页均为 0**；全文 `桥接` 0 命中。
- Removed-no-CJK 逐项裁定：
  - P1 副标题槽位句 `DIE WOCHENZEITUNG FÜR LERNENDE — …` → 配对徽章，家具 ✓；
  - P3/P4/P6 孤 `。` → 核心自有排版类，葡语版句末为行内 `.`，无内容损失 ✓；
  - P7 `Ein Beispiel der Redaktion!` → 葡语标签 `Um exemplo da redação!`，家具 ✓；`……` → `...`，标点 ✓；
  - P7 上述两条德语定义串 → **问题 1**，不属于讲解层/家具 ✗；
  - P8 全角括号行片段 → 半角形式已在 added 侧对应存在，仅括号形式变化，德语 key 无丢失 ✓。
- P1–P7 added 串逐条目视：均为葡语讲解、家具、双语栏头、gloss、葡译、指令 token，无新增德语正文句。

### 门 2 P8：除问题 2 外通过

- 我独立跑 `tools/p8.py compare`（显式 SVG 路径；`--target pt` 的默认 P8 文件名不适用本族，改用显式路径后复现）：
  **CLEAN，core 150 noted = edition 150 noted，missing=[]，extra=0，keydiff=[137, 138, 139, 150]**。
- Keydiff 逐项人工核实（非仅提取器输出）：
  - 137（A2 Tradução，题干 DE `Der Tankrabatt läuft bis Dezember.`）：key `O desconto no combustível vai até dezembro.`，
    注 `laufen = durar, continuar`——DE→PT 翻译题真实重定向 ✓；
  - 138（A2 Tradução，题干 `Ich schaue am Dienstag Fußball.`）：key `Vejo futebol na terça-feira.`，注 `schauen = ver` ✓；
  - 139（B1 Tradução，题干 `Die Schule hat wieder begonnen.`）：key `A escola recomeçou.`，注 `wieder begonnen = recomeçou` ✓；
  - 140 **不在** keydiff：key 德语不变 `Am Sonntag schlafe ich eine Stunde länger.`，仅题干反向重定向
    （PT `Durmo uma hora a mais no domingo.`，指令 `Traduza para o alemão`）✓；
  - 150（B1 Escrita）：key `Tarefa aberta — siga os pontos do quadro de escrita; o texto-modelo está no quadro desta página`，
    注 `Avaliação pelos pontos indicados`——写作 apparatus 葡文化 ✓。
- 无括号/破折号提取伪影：keydiff 与人工逐行读数一致；P8 全页全角括号/全角 `｜`/`。`/`……` 均为 0，CJK 0。
- P8 形式：本族构建码 `content8.py` 第 156 行与 W43 本族构建码逐字一致——
  `kf.para(" · ".join(parts), 13, "sans", False, INK, 1.26, 9)`，即 **13pt / 1.26 半角括号** ✓。
  观察（非问题，见文末 O1）：连接符为无空格 `key(note)`，W43 为有空格 `key (note)`；无空格形式与 W45 DE×EN 构建码一致。

### 门 3 几何遮挡：通过（同基线 1 项实测为测量伪影，非真实碰撞）

- 我独立跑 `tools/occlusion_audit.py`（自测 6 类全触发、干净对照静默）：**分版 0 flags、核心 0 flags、NEW vs core 0**。
- 同基线墨迹扫描（我独立实现，调用共享工具 `occlusion_audit.ink_box`，全 8 页逐基线比对）：
  工具层面复现 1 项——P1 sommaire S.3 行 y=1436：`Ferienwechsel & Herbst` 墨右 1804.5 vs 标签 `A2→B1` 墨左 1799.7（重叠 4.8px），
  核心同页同款亦 1 项。但该项是 **XML 实体未解码的测量伪影**，不是真实碰撞：
  - SVG 原文为 `Ferienwechsel &amp; Herbst`，TAG_RE 捕获后未解码，`ink_box` 把 `&amp;` 按 5 个字形计宽；
  - 解码后重测：标题墨右 **1755.0**，标签墨左 1799.7，**间隔 44.7px**；
  - 卡面像素 ground truth（P1 卡 y 1400–1470 带）：标题墨迹止于 x=1757，标签墨迹起于 x=1800，**间隔 43px**，字形互不接触。
  - 其余 6 条 sommaire 行间隔 97.5–127.0px；全版真实同基线碰撞 = **0**。该行元素在核心与本版逐属性逐字相同，属核心继承且墨迹干净。
  - 附注：未解码实体的误差方向是保守的（盒偏宽），不影响审计 0 flags 结论的可信度。
- P6 图表标签与条形/后绘矩形逐项实测（与 KIT 数值逐一吻合）：
  - 绘图顺序每行均为：德语标签 → 葡语标签 → 条形 → 百分比；条形后绘，故任何重叠都会遮盖标签——实测均无重叠。
  - 德语标签墨右：`pflegen Angehörige zu Hause` 390.5、`nutzen einen Pflegedienst` 354.5、`leben im Pflegeheim` 294.0（条左 535，间隔 ≥144.5px）；
  - 葡语关键词标签墨右：`em família` **522.8**（距条左 12.2px）、`serviço` **491.5**（43.5px）、`em lar` **484.0**（51.0px）；
  - 百分比起位 1707/891/755 vs 条右 1691/875/739，间隔均为 16px；
  - 条宽 1156/340/204 = 1700 的 68%/20%/12% ✓；68+20=88 与 item 85 key 一致 ✓。

### 门 4 Gloss：通过，25=25

- 按渲染后 `gloss()` 字符串本身以 `·` 拆分（源文件 grep，不执行构建模块）：核心与本版各 5 处调用（P2/P3/P4/P5/P6），每处 5 项，
  **核心 25 = 本版 25，1:1，无增删合并**。
- 全部 24 个德语词头 + 葡语译文在合并渲染文本中均存活；初查 `die Pflegeversicherung` “缺失”实为换行断开
  （P6 gloss 框第 58–59 行 `… · die` / `Pflegeversicherung = seguro de cuidados`），条目完整。
- P1 bridge 行（非 gloss 调用）：核心 4 项 = 本版 4 项
  （`die Englische Woche = semana inglesa · der Spieltag = rodada · empfangen = receber em casa · die Bundesliga = Bundesliga.`）。
- Gloss 前缀 `Nota — `，5 处调用一致。

### 门 5 P7 金句：通过（右栏终值以墨迹口径另注）

- 8 句德语原文在全版合并文本中**各恰 2×**（源文章页 + P7 表），且每句均在其标注的源文章页出现：
  1. `Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.`（P4）
  2. `Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter.`（P2）
  3. `Wer 50 Liter tankt, spart rund 8,35 Euro.`（P2）
  4. `Die Schule hat nach den Herbstferien wieder begonnen.`（P5）
  5. `Die Tage sind kurz, die Abende lang.`（P3）
  6. `Zwei schwere Auswärtsspiele für die deutschen Teams.`（P4）
  7. `Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.`（P6）
  8. `Es geht langsam aufwärts — aber von allein geht es nicht.`（P6）
- 页码标签分布与核心逐项一致：**S4·B1×2、S2·A2×2、S5·B1×1、S3·A2×1、S6·B2×2**（=8）；德语引言与核心逐字一致。
- P7 短语逐字取自本期文章并带正确页码标签 ✓（上表即核对结果）。
- P7 右栏终值：金句横线为 y=1508 的全宽规则线；右栏最后文本 `Desconto no combustível.`（20.5pt，基线 1490.72），
  我用 venv PIL + Noto Serif CJK SC 实测墨迹底 **1490.97**，距规则线 **17.0px**，右栏未越线。
  构建员称 1504.5 属 flow-cursor 口径（非墨迹底），两种口径下均未越线，门禁实质通过（见文末 O3）。

### 门 6 读者园地：通过，显性邀请成立

- 页上同时具备三事实（葡语注文 2 行）：`Sem cartas reais nem melhores textos da página 8; a promessa passa ao VOL.3.`
  ——（1）无真实来信、（2）无最佳 P8 作文、（3）承诺顺延至 VOL.3 ✓。
- 显性公开征集句（独立判定：**构成显性邀请**）：`Escreva-nos! Envie a sua carta real e o seu texto da página 8 para o VOL.3.`
  ——祈使 `Escreva-nos!` + 明确对象（真实来信 + P8 作文）+ 明确去向（VOL.3），不是内容预告也不是练习提示。
  标签 `Um exemplo da redação!` 明确标示例身份 ✓。
- 同页 VOL.3 预告行（`Ihre Briefe: Schreiben Sie uns! …`）未计入——邀请仅凭 P7 读者园地本句即已成立。
- 读者园地德语行与核心逐字一致（`Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3.`、
  示例信、德语征集句）；全版无编造的读者来信、姓名或引言 ✓。

### 门 7 家具三方对照：通过（修复范围有一项证据边界，见 O5）

- P1 配对徽章与 W43 已发 `files/weekly-report-de-pt/svg/p1-front.svg` 的徽章元素**逐属性一致**：
  `x=975, y=372, 20pt, weight 700, fill #a4553a (BRICK), anchor middle`，字符串
  `TEXTOS EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA` 逐字一致 ✓。
  徽章仅 P1 一处（其余页同名字符串命中均为页脚）。
- 其余页出现的 OLIVE `#3e4c2a` 属核心继承调色（栏目标题、题号芯片等），W43 同版同款分布一致，非徽章修复残留 ✓。
- 页脚 8/8：`Die Lucerna · SEMANÁRIO ALEMÃO VOL.2 · TEXTOS EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS` ✓；
  页码行 8/8 `Página {n} de 8` ✓；masthead 每页 1× `Die Lucerna` ✓；P1 顶条、46pt 副标题、gloss 前缀、
  P8 分隔符 `— Página {n} —`、P8  keys 头 `ANTWORTEN · TODAS AS RESPOSTAS COM NOTAS (PÁGINAS 1–8)` 均与 W43 形式一致（VOL.2 替换 VOL.1 除外）。
- 本版 8 个 SVG 现哈希与 KIT §2 钉住的哈希逐一一致（p1 `daf5c2ca…`、p2 `05e8bcd7…`、p3 `a706d043…`、
  p4 `bca26499…`、p5 `dd96384f…`、p6 `99e03a38…`、p7 `b2b03874…`、p8 `cb9461ff…`）；
  构建目录 `svg-hashes-before-dump.txt` 与 `svg-hashes.txt` 相同。W43 实测胜过 README #20 泛写之处已按 W43 实测裁定。
- 修复范围证据边界（O5）：构建员称“仅 P1 徽章元素变化”，但现存记录中没有修复前渲染的哈希，无法以修复前后 diff 直接证明；
  可验证的事实是：徽章现确为 BRICK 且与 W43 元素一致、徽章元素仅存于 P1、P2–P8 不含徽章元素故填色修改无法直接改动它们、
  哈希在 dump 步骤前后稳定。修复范围的其余部分依赖构建员的重渲染确定性，未独立复现。

### 门 8 精简决定复核：三项均裁定可接受，不列为缺陷

- (a) P7 工具箱 3–4 项：实测 `Es wird gespielt. = Será jogado`（无 `(passiva)`）、`Meiner Meinung nach ... = opinião`（关键词 gloss）。
  裁定可接受：被动语态在同页 A2 课（`Mit werden sprechen Sie über die Zukunft und das Passiv`）已教；
  `Meiner Meinung nach ...` 全形在同页 B2 课（`Meiner Meinung nach ... Oder: Ich finde, dass ...`）已教且用于练习 112。
  工具箱为速查栏，语义未损。
- (b) P6 图表关键词标签：实测 `em família / serviço / em lar`（墨右见门 3），完整形式存活情况：
  - `serviço de cuidados` 存活于 P6 文章 gloss（`der Pflegedienst = serviço de cuidados`）及 P8 答案 item 84（`serviço de cuidados 20% é o segundo`）；
  - `lar de idosos` 存活于 P8 答案 item 86（`lar de idosos 12% é o menor`）；
  - `cuidado familiar`（行 1 完整形）全版无逐字存活；但行 1 有德语标签 `pflegen Angehörige zu Hause` + 图表标题
    `WER PFLEGT ZU HAUSE? · Quem cuida em casa?` + 百分比 68% 锚定，练习 83（`68% em família`）与 85（68+20=88）均以百分比消歧，
    `em família` 本身不产生误读。裁定可接受。
  - KIT 表述修正：完整形存活位置是 P8 答案（83–86 题答案），不是 P6 页内的图表阅读注文；行 1 完整形未存活一事 KIT 未披露，但不构成缺陷。
- (c) P7 读者注文缩短与短语 7 葡译缩短：
  - 读者园地德语引言（101–109 行）与核心逐字一致，未动 ✓；缩短后的葡语注文仍完整表达三事实（见门 6），
    “编辑部示例”标记由标签 `Um exemplo da redação!` 承担 ✓；
  - 短语 7：德语引言逐字未动；葡译 `A economia alemã deixa devagar a estagnação, mas a recuperação não se sustenta sozinha.`
    以 `não se sustenta sozinha` 保留“不能自持”义，2 行 ✓。裁定语义无损。

### 门 9 PDF/卡片/分页/等级/ABSTRACT：通过（除问题 2 涉及的 P8 内容外，载体本身无误）

- 双 PDF（我用 tools venv pypdf + sha256 独立实测，与 KIT 逐值一致）：
  - 印刷 `Die-Lucerna-VOL2-PT.pdf`：8 页、1462.5×2025 pt、4,144,504 B、sha256 `0bc3a3ba9163852befa0287094a99f46163ba629b448a0dfa62319b6f88fa594` ✓；
  - 网页 `Die-Lucerna-VOL2-PT-web.pdf`：8 页、1400×1938 pt、4,167,863 B（<10 MB）、sha256 `88ab3fedb4ba0adcbc903f1fb365c91382ac977f81d4ed3027a6ab190d5fb23a` ✓。
- 8 张卡面（1950×2700）全部目视：无重叠、无截断；P7 卡确认右栏与金句横线间距清晰、读者园地与工具箱完整；
  P8 卡确认答案区可读（并同时肉眼确认问题 2 的英文注文）；P6 卡确认图表标签与条形无遮盖。
- 150 题与核心一致：P8 独立提取 1–150 全集无缺号（核心与本版同）；P1–P7 逐页题号/等级 token 分布与核心逐页完全相同
  （P3 一个 token 差异实为 `página 3.` 的误匹配，非练习差异）；P8 compare CLEAN 150=150。
  绝对登记值（分页 10/18/18/18/18/18/12/38，A2 66/B1 70/B2 14）以核心已定稿登记 + 本版逐页结构同一性为依据；
  本次未执行构建模块的登记转储（避免在核心/分版目录外执行构建代码，freeze.py 的受控重渲染除外），见 O6。
- ABSTRACT.txt：内容单行（末尾换行符除外）、无 ASCII 双引号、葡萄牙语；含 masthead `Die Lucerna`、目标语名称、
  A2–B2、150 练习；真实主题关键词：Champions League、Europa League、9ª rodada da Bundesliga、Tankrabatt、Ferienwechsel、
  cuidados em casa；学习者搜索短语：`aprender alemão lendo notícias de verdade`。
  事实锚点均核实：`até 31 de dezembro` 见 P8 答案注文（item 6/9/13）；`semana inglesa` 见本版 gloss（`die Englische Woche = semana inglesa`）。

## 非阻塞观察（已裁定不列为问题，修复时可顺手澄清）

- O1：P8 注文连接符为无空格 `key(note)`，W43 为有空格 `key (note)`；无空格形式与 W45 DE×EN 构建码一致，属同族内形式变体，
  不影响可读与 key 判定；KIT §3 “with a space” 表述不准确。
- O2：同基线“1 项命中”是 `&amp;` 未解码的测量伪影（见门 3），真实间隔约 43–45px；卡面已证实干净。
- O3：P7 “1504.5”为 flow-cursor 口径，墨迹底为 1490.97；两种口径下右栏均未越过 y=1508 金句横线。
- O4：KIT §11.2 称完整形存活于“P6 图表阅读注文”，实测存活位置为 P8 答案 84/86；行 1 完整形 `cuidado familiar` 全版无逐字存活（已裁定可接受）。
- O5：徽章修复范围“仅 P1 变化”无修复前哈希可供前后 diff 佐证（见门 7）；可验证部分均已通过。
- O6：分页/等级绝对值未以 fresh registry run 独立复现，依据为核心同一性 + P8 150 全集；修复重渲染后建议由构建方重出登记转储并由下一轮校对核对。

## 修复后重校清单（供协调员）

1. 恢复 P7 NOCH EIN WORT 德语定义句逐字（问题 1 修复方向），保留葡语 gloss 行。
2. 将 P8 item 5 注文改为纯葡语（问题 2 修复方向）。
3. 重渲染后重跑：freeze diff（新增 CJK 0、P7 removed 串须不再含德语定义句）、p8 compare（CLEAN 且 keydiff 不变）、
   occlusion audit（0/0/0）、P7 右栏墨迹终值、双 PDF 尺寸与 SHA 重钉、8 卡重目视。
4. 修复不得改动其他已通过项；上架仍由协调员串行执行，本报告不作上架宣称。
