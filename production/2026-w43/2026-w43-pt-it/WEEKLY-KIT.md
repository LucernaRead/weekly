# A Lucerna — VOL.1 · PT × IT（葡萄牙语正文 + 意大利语讲解）

Lucerna 学习者周报 · W43（2026-10-19 周一 – 10-25 周日）葡语版的意大利语讲解版。
语言组合（一对一）：正文 = 巴西葡萄牙语（冻结核心版 VOL.1，逐字未动）；讲解 = 读者的母语意大利语（小字灰色注、题面意语说明、答案意语简析）。
刊头：**A Lucerna**（与核心版一致）。

- P1 徽章（砖红色行）：«TESTI IN PORTOGHESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI»
- 页脚：«A Lucerna · SETTIMANALE PORTOGHESE VOL.1 · TESTI IN PORTOGHESE · SPIEGAZIONI IN ITALIANO» / «Pagina N di 8»
- 校对状态：制作方全量自校完成（记录见 §8）；**独立校对已完成（见 §11）：一整轮零问题，PASS**。

## 1. 基线证明（冻结核心复现）

方法：把核心构建目录整体复制为 `hidden_files/weekly-report-pt-it-build/`，仅把输出路径改指复制目录内的 `baseline-svg/`，其余代码一字未改运行 `run.py`，产物与核心版交付 SVG 逐个比对 SHA-256：**8/8 逐字节相同**。

| 版 | SHA-256（核心交付件 = 基线复现） |
|---|---|
| P1 | 082acac0811f1efac363cc09ac53529ea1b668708fec3a02752da1b6a8d6156f |
| P2 | c4a853ac6ba9f623d5d4aea1778a388ad6c6b0fa3a3bda991cc7036db30018bf |
| P3 | bba9906a0115cbbd7b97ef2dba060f5c509cf2a806f30bad21407fe04d81e083 |
| P4 | b99417547786bd64c6d81c6eb8dc2088d4a48e3dbe708af26af9eb3c7709b489 |
| P5 | 4a1121e8bc76fb8d36e761e522188e2fddedea5c53bb02e9df9d709dffe3d256 |
| P6 | 0d0ad43604c48a3a77c5ae7cb70236c7f47905663ee0250527e82f5a6d076072 |
| P7 | d3dc772b47960626f3ed2fcc3463d52b0f8c36b900d09bf126a3e031df81171d |
| P8 | 8a944c118fde081535ea142407596907b05914ffd9cea5b616fc0eac36a1b944 |

完工后复验：核心版 8 个交付 SVG 的 SHA-256 与上表一致，核心目录未被本版制作触碰。

## 2. 改动范围（仅讲解层）

- 全部中文讲解（词注、题干说明、练习 apparatus、P8 全部 150 条答案简析、栏目标题的中文部分、E VOCÊ 框意语问句、P7 金句的译文行）译为意大利语。
- 葡语正文、标题、题面、选项、图表、图片、版式几何全部冻结：终版与核心版逐页做可见文本多重集 diff，差异项 100% 落在讲解层 / 配对家具 / §5 登记项之内，无一处葡语正文改动（diff 全表存于制作记录）。
- 讲解行方法更名为 `expl()`（按讲解版命名惯例）；禁用词（中间环节称谓，中英文形式）在本版报纸、KIT、构建代码中出现次数为 **0**（原始字节扫描核验）。
- 终版 8 个 SVG 可见文本中 CJK / 全角字符节点数 = **0**（程序扫描）。
- 注册表 `type` 字段为不渲染的内部元数据，沿核心版标签仅存于代码（与全部已定稿讲解版同一做法）；报面零呈现。
- 答案简析中的括号一律半角，括号前留空格（如 «(TSE)», «(app)»）。

## 3. 意大利语家具（逐字记录，宽度均以制作字体实测）

| 位置 | 字符串 | 实测 |
|---|---|---|
| P1 徽章（19pt 粗 sans，砖红） | TESTI IN PORTOGHESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI | 827px ≤ 1820 |
| P1 副刊头（36pt serif 粗） | SETTIMANALE PORTOGHESE · VOL.1 · O SEGUNDO TURNO · O DEBATE FINAL · O ENEM VEM AÍ | 1749px ≤ 1820（核心版该槽位为中文 40pt；法语讲解版同为 36pt） |
| 页脚左（20pt sans） | A Lucerna · SETTIMANALE PORTOGHESE VOL.1 · TESTI IN PORTOGHESE · SPIEGAZIONI IN ITALIANO | 952px |
| 页脚右 | Pagina N di 8 | — |
| 词注前缀 | Nota — | — |
| P1 顶栏中（21pt sans） | TODA SEMANA EM PORTUGUÊS · OGNI SETTIMANA · IL PORTOGHESE DEL BRASILE | 横跨 563–1387px，与左右两栏（止于 371 / 起于 1438）均留空隙 |
| P1 目录框头（24pt sans 粗） | NESTA EDIÇÃO · SOMMARIO | 339px ≤ 框内 390 |
| P7 错误框头（23pt sans 粗） | ERROS COMUNS · ERRORI | 303px ≤ 框内 390 |

缩短变体（如实记录，均为措辞缩短，几何未动）：
- 目录框头初版 «NESTA EDIÇÃO · IN QUESTO NUMERO» 实测 479px，溢出框内宽 390 → 改 «SOMMARIO»（与法×意版 KIT 记录的同类缩短一致）。
- 错误框头初版 «ERROS COMUNS · ERRORI FREQUENTI» 实测 440px > 390 → 改 «ERRORI»。
- P1 顶栏中初版末段 «IL PORTOGHESE CHE LEGGE IL BRASILE» 与右栏日期行仅隔 3.6px、视觉粘连 → 改 «IL PORTOGHESE DEL BRASILE»（语义不变，空隙 51px）。

## 4. 体量与题量（与核心版逐项一致）

- **总计 150 题**，统一编号 1–150 连续无缺重；分级 **A2 44 · B1 75 · B2 31**；分版 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38；题型分布与核心版完全相同（完成句子 61 · 单选 49 · 完形单选 13 · 词汇配对 12 · 造句 7 · 翻译 4 · 判断对错 3 · 写作 1）。
- 写作范文 92 词（程序计数，与核心版一致；题面 80–100 词区间内）。
- 可见文字量（同一提取脚本实测，不含空格）：本版合计 35.733 字符（P1 3.869 · P2 3.797 · P3 3.386 · P4 3.206 · P5 3.829 · P6 4.095 · P7 3.881 · P8 9.670），核心版同脚本实测 30.109 —— 增量全部来自意语讲解比中文讲解长，属预期。
- 构建日志：FLOW OVERFLOW 0 · HEAD TOO WIDE 0。

## 5. 答案键差异登记（key-diff registry，完整）

翻译类题目按讲解版惯例重新指向读者语言，共 5 项受影响，其余 145 题键与核心版逐字相同：

| 题号 | 类型 | 核心版（中文讲解） | 本版（意语讲解） |
|---|---|---|---|
| 137 | 翻译（葡→读者语） | 键 = «周日，巴西重返投票站。» | 键 = «Domenica, il Brasile torna alle urne.»（键改意语；题面葡语原句不动） |
| 138 | 翻译（葡→读者语） | 键 = «出门前，核对你的投票地点。» | 键 = «Controlla il tuo seggio prima di uscire di casa.» |
| 139 | 翻译（读者语→葡） | 题面 = «“吉他”的搜索量增长了 53%。→ ___» | 题面 = «Le ricerche di «guitarra» sono aumentate del 53%. → ___»（题面改意语；键 «As buscas por guitarra cresceram 53%.» 不动） |
| 140 | 翻译（读者语→葡） | 题面 = «你到达时，请核对一下投票站。→ ___» | 题面 = «Quando arriverai, controlla il tuo seggio. → ___»（键 «Quando você chegar, confira a seção.» 不动） |
| 150 | 写作 apparatus | 键 = «（开放题，范文如下）»；注 = «范文见本版 H 区（92 词）» | 键 = «(domanda aperta — testo modello qui sotto)»；注 = «Testo modello nella sezione H di questa pagina (92 parole)» |

## 6. P8 印刷注集合核验（printed-note set equality）

方法：从两版交付 P8 SVG 逐个抽取印刷出的答案条目（编号 + 键 + 注），按编号比对。
- 核心版印刷集合 = {1…150}（核心版为全印规则）；本版印刷集合 = {1…150}。**两集合按编号相等**，无缺注、无多注。
- 印刷键逐号比对：仅 137、138 两号不同（即 §5 登记的意语键）；150 号为写作条目，两版均以 «✓ + 注» 形式印刷，注文为 §5 登记的意语 apparatus。139、140 两号印刷键为葡语原键，未变（变的是题面，见 §5）。

## 7. 几何遮挡审计（出厂门槛，制作方自查）

工具：`hidden_files/weekly-report-pt-it-build/audit_pt_it.py`（按绘制顺序解析 SVG，字形度量用制作同款 PIL 字体；墨迹带 = 基线 −0.88em … +0.30em；线框按线宽一半外扩；判据：后绘不透明元素覆盖 ≥30% / 后绘细线穿墨迹带 / 字形侵入页脚带 y>2580 / 字形出页边）。
**正例对照先行验证**：合成对照页植入 COVER / LINEX / FOOTER / EDGE 四类缺陷，审计全部命中（4/4），且干净文本零误报。
审计结果：

- 本版 8 版共 **1 个标记**：P1 本周生词意语注第二行 «voto.»（基线 1842，19pt）被其下横线（y=1844）按模型墨迹带（下沿 1847.7）判为穿线。**裁图 + 像素裁定：非缺陷（测量伪报）** —— «voto.» 无降部字母，渲染墨迹实测止于第 1840 行，距横线 4px，成图目检横线在词下方留白处通过，不划字。模型 +0.30em 降部余量对该词不适用。
- 核心版同法审计：0 标记（参照）。
- **框题出界专项扫描**（审计盲区补充：单行文本右端 vs 版心右界 1885）：本版初版检出 2 处自产溢出（P1 目录框头、P7 错误框头，见 §3），均以缩短措辞修复，终版复扫仅剩 1 处 **与核心版逐字节相同** 的既有项：P2 配对题右列 «a. o dinheiro que você paga por uma» 右端 1891（核心版同为 1891，在内框线 1910 之内，属冻结正文，不动），如实登记。
- P7 专项（本核心版的已知缺陷类）：金句区纵坐标由公式 `fy = max(1712, ly + lh + 44)` 决定；意语注初版使第三栏堆高至 1809.5（核心版 1722.0），将把金句压入下期预告深色带。修复（纯措辞）：错误框注 1 改 «assistir (guardare) chiede a: ao debate.»（2 行→1 行）、注 2 改 «en e la sono spagnolo; em + a = na.»（2 行→1 行）、读者园地注改 «Lettera di esempio della redazione, non vera. Nel VOL.2 le vostre lettere vere e il miglior testo di pagina 8!»（4 行→3 行），栏底回到 1721.5，fy = 1765.5（核心版 1766）。终版 P7 成图逐条目检：8 条金句及意语译文全部完整可见，无一条被深色带遮挡；金句逐字连续、页码标注（1, 1, 2, 3, 4, 5, 6, 2）与核心版一致，程序计数每条在全期恰出现 2 次（源版 1 次 + 第 7 版 1 次）。

## 8. 制作方全量校对记录

- 8 版逐版通读终版渲染文本：葡语正文与核心版 diff 冻结核验（§2）；意语讲解逐项通读（语法、拼写、重音、与正文对应关系）。
- 150 题答案逐题重推：与核心版登记表比对，键差异仅 §5 五项；算术题复算（23 题 982+514+431+312=2.239；86 题 350+350=700；87 题 900−250=650；图表条长与数值成比例，与核心版同图）。
- 日期/星期逐项按 2026 年真实日历核验（`date` 实测）：10/4 周日（第一轮）、10/11 周日、10/15 周四、10/18 周日（Band 辩论）、10/20 周二（Vasco×Boca）、10/21 周三（Prova do Fazendeiro）、10/23 周五（Globo 辩论）、10/24 周六、10/25 周日（第二轮）、10/31 周六、11/1 周日（巴西杯半决赛首回合）、11/2 周一（Finados）、11/7 周六、11/8 与 11/15 周日（Enem）——全部与报面一致。
- 红线复核：全期百分比均为谷歌搜索热度并如此标注（P1 图注 «Dati Google: non è un voto.»、P6 两图图注与正文），**无任何民调百分比**；无国际政治。
- 自查发现并修复（均改构建源码后整期重渲染）：
  1. P5 判断题 instr 漏译（«判断» 残留在 3 道题面）→ 改 «Vero o falso»，复扫全码可见字符串零中文残留。
  2. P7 第三栏意语注过长（栏底 1809.5）危及金句区 → §7 三处措辞缩短，栏底 1721.5。
  3. P1 顶栏中意语行与日期行视觉粘连（间隔 3.6px）→ 缩短末段，间隔 51px。
  4. P1 目录框头、P7 错误框头溢出框界 → §3 缩短变体。
- 终版复核（修复后全量）：构建零警告；文本 diff、印刷注集合、审计、溢出扫描、金句计数全部复过；8 张成图逐版目检无溢出、无重叠、无压页脚。

## 9. 图片与授权（与核心版相同，逐张经 Wikimedia Commons 核验，详单见构建目录 assets/CREDITS.md）

终版 SVG 内嵌图片载荷与核心版逐页 MD5 比对：**全部逐字节相同**（P1 1 张、P3 2 张、P5 1 张）。

- P1 电子投票箱（urna.jpg）— 公有领域，Tribunal Superior Eleitoral (TSE)。
- P3 violão 演奏者特写（violao.jpg）— CC0（累西腓 Marco Zero 广场）。
- P3 Django Reinhardt（django.jpg）— 公有领域，William P. Gottlieb 摄于 1946 年。
- P5 图书馆学生（estudo.jpg）— CC0，Gary Todd。

## 10. 文件与复现

- 交付：`svg/`（8）、`cards/`（8 PNG，1950×2700）、`A-Lucerna-VOL1-IT.pdf`（印刷版，**6.450.106 B**，8 页，SHA-256 `2897b9c2481b460bd8dce7d3f78a340b29be65a1560b64d060d23bd1d2bd7e92`）、`A-Lucerna-VOL1-IT-web.pdf`（网页版，**3.685.048 B** < 10 MB，8 页，SHA-256 `b440947e2ba3fad32b3e3c72b62682b2e2a8f998064dcef7ffaa1e1f9b0073aa`）。
- D5 rebuild (2026-11-13–14, see D5 rebuild section at the end of this KIT): print master `A-Lucerna-VOL1-pt-it.pdf` **5353932 B** · sha256 `df3abee80c67989a9278df44782d12a4b8d612901055bd1d5aaa934719912f74`; render-web `A-Lucerna-VOL1-pt-it-web.pdf` **3299664 B** · sha256 `02bb6131eaab67dd6d879a50b49324eba6ba5bd01d9c77ebad9dcf8434fc40d1`; web (issues-type) `2026-w43-pt-it.web.pdf` **641287 B** · sha256 `e82569ff705c059cc6cf32488d4eacf64a3ff019ac1b9339300cb59bb9a50c07` (< 7 MB); text.md byte-identical to the shipped version (sha256 `461229b03ab46da844298519467425b9dd2ebb3e2d42c24266dc21aa3f0c0fcb`). Pre-D5 KIT pins above (print 6,450,106 B (sha256 `2897b9c2…`); render-web 3,685,048 B (sha256 `b440947e…`)) are D1-era values, already expired before this rebuild (toolchain drift: Bold/Italic subset split in tools/webpdf.py commit 40963281).
- 制作源码：`hidden_files/weekly-report-pt-it-build/`（bslib4.py、svglib.py、content12/34/56/7/8.py、run.py、render.py、audit_pt_it.py、assets/、baseline-hashes.txt）。
- 复现：`cd hidden_files/weekly-report-pt-it-build && /tmp/wp-venv/bin/python run.py && /tmp/wp-venv/bin/python render.py`（venv 需含 cairosvg、pillow、pypdf；禁用 /opt/meta-chromium）。

## 11. 独立校对记录（SOP 出厂门槛 · 与制作方独立的第二双眼睛，2026-10-21）

方法（全部自备实现，不采信制作方脚本结论）：将核心构建与本版构建分别复制到校对 scratch 并把输出路径改指 scratch 后独立复跑；可见文本从交付 SVG 自行提取逐版比对；注册表从两次复跑的 REG 独立转储比对；几何审计为自研实现（按绘制顺序解析、PIL 同款字体实测字宽、墨迹带 = 基线 −0.88em…+0.30em、线框按线宽一半外扩），先以合成正例对照验证（COVER / LINEX / FOOTER / EDGE / BOXTITLE 五类植入缺陷全部命中、干净文本零误报）后才跑真实版面；全部标记逐一裁图/像素裁定。校对底稿存 `hidden_files/proof-ptit-independent/`。

### 核验结果（逐项）

- **基线与产物一致性**：核心构建在 scratch 独立复跑，产物与核心版交付 SVG **8/8 逐字节相同**（与 §1 表一致），§1 基线主张成立；本版构建独立复跑，产物与本版交付 SVG **8/8 逐字节相同**——交付件确由构建源码生成、无手工改图。两次复跑日志均 FLOW OVERFLOW 0 · HEAD TOO WIDE 0。
- **冻结核验（葡语正文零改动）**：源码全量 diff 逐行分类——`bslib4.py` 仅 4 处（页脚家具、讲解方法更名 `expl()`、词注前缀 «Nota — »）；`svglib.py`、`run.py` 与核心版逐字节相同；content 五文件全部改动行均属讲解层 / 配对家具 / §5 登记项。其中不含中文的改动行只有 OUT 路径（×5）与 P1 第 372 行槽位：核心版的葡语副刊头行被本版配对徽章行替换（砖红加粗，与 §3 记录一致，属配对家具）。渲染层复核：核心版全部无中文文本节点在本版逐字存在，唯一例外即上述徽章槽位，另有两处讲解行因译文折行点不同而分片不同（P6 词库行、P8 个别简析行），其葡语成分在本版完整保留（已逐条目检）。
- **注册表比对**：150 题 page/level/type 元数据零差异；**键差异恰为 {137, 138, 150}**，与 §5 登记一致（137/138 键改意语、150 为写作 apparatus）；139/140 键与核心版逐字节相同（改的是意语题面，已在 P8 交付件上核对题面与键）；简析 149 条已译为意语，第 87 题简析为纯算式串 «900 − 250 = 650»，两版相同属正常。
- **P8 印刷注集合（printed-note set equality）**：自两版交付 P8 SVG 按编号抽取印刷条目——核心版集合 = {1…150}，本版集合 = {1…150}，**两集合按编号相等**，无缺注、无多注，每条均带简析；印刷键逐号比对仅 137、138、150 不同（即 §5 登记项）。
- **题量与编号**：150 题连续无缺重；分级 A2 44 · B1 75 · B2 31；分版 10/18/18/18/18/18/12/38；写作范文与核心版逐字相同，92 词（构建口径，与题面 80–100 词及 150 题标注一致）。
- **答案逐题复核**：150 道题面与答案在交付渲染文本上逐题对照正文复核，无一处不符；算术复算（23 题 982+514+431+312=2.239；86 题 350+350=700；87 题 900−250=650）全对；改键忠实度：137 题意语键 «Domenica, il Brasile torna alle urne.»、138 题 «Controlla il tuo seggio prima di uscire di casa.» 均为对应葡语题面的忠实译文。
- **P7 金句**：8 条逐字连续、页码标注 (1, 1, 2, 3, 4, 5, 6, 2) 与核心版一致；程序计数（去空白拼接法）每条在两版全期各出现恰好 2 次（源版 1 次 + 第 7 版 1 次）。
- **日历**：`date` 实测逐项核对——10/4 周日、10/11 周日、10/15 周四、10/18 周日、10/20 周二、10/21 周三、10/23 周五、10/24 周六、10/25 周日、10/31 周六、11/1 周日、11/2 周一（Finados）、11/7 周六、11/8 与 11/15 周日（Enem）——与报面全部一致。
- **红线与百分比**：全期百分比逐项核查，均为谷歌搜索数据并如此标注（P1 图注 «Dati Google: non è un voto.»、P6 两图来源注、正文 «Interesse de busca não é intenção de voto» 明示），吉他研究三数（−74% / +53% / 75%）为搜索量数据，+40% 明示为搜索行为而非移民数据；**无任何民调百分比**；无国际政治。
- **意语完整性**：8 版逐版通读交付文本——词注、语法讲解、题干说明、题型标签（«Completa» / «Abbina» / «Forma la frase» / «Traduci» / «Scrivi» / «Vero o falso»）、P8 全部简析均为意语；全 8 个 SVG 原始字节扫描 CJK / 全角字符 = **0**。
- **几何遮挡审计（自研实现，独立于制作方工具）**：本版 8 版共 **1 个标记**——P1 本周生词注第二行 «voto.» 被 y=1844 横线按模型墨迹带判为穿线。**像素裁定：非缺陷**——成图实测该词墨迹止于第 1841 行（词尾句点底行），第 1842 行全空，横线占第 1843–1844 行，两者不相交（该词无降部字母，+0.30em 余量不适用）；与制作方 §7 的裁定方向一致（其墨迹行数读数为 1840，与本次实测差 1 行，不影响裁定）。其余 COVER / FOOTER / EDGE / BOXTITLE 四类标记均为 0（共 1582 个文本节点）。制作方自查修复逐项像素/目检复核：P7 八条金句及译文全部完整位于下期预告深色带之上（裁图目检）；P5 第 80–82 题标签 «Vero o falso» 已落实；三个框题以制作字体实测墨迹右端——数字框头 919.4 < 框界 961、目录框头 1811.6 < 1885、错误框头 1776.1 < 1885，均在框内；P1 顶栏中行与日期行间隔目检已分离。
- **核心参照跑注记（不属本版缺陷）**：以更严的「包围框」判据跑核心版时，其 P1 数字框头被标记（模型墨迹右端 968 > 框界 961；成图像素实测墨迹至 x=965，末字约 4px 越框线）——此为冻结核心版的既有微瑕，制作方工具以版心右界 1885 为判据故未报；本版同位框头已缩短（«… · CIFRE»，墨迹止于 919.4），**未继承**。核心版冻结不动，此处仅如实登记备查。
- **图片**：内嵌图片载荷逐版 MD5 与核心版逐字节相同（P1 ×1、P3 ×2、P5 ×1）；印刷图说与 CREDITS 一一对应（TSE 公版 / violão CC0 / Gottlieb 公版 / Gary Todd CC0）。
- **禁用词**：报纸 SVG、本 KIT、构建代码原始扫描，中间环节称谓（中英文形式）出现次数 = **0**。
- **PDF 针脚（校对人自测）**：网页版 **3.685.048 B**，SHA-256 `b440947e2ba3fad32b3e3c72b62682b2e2a8f998064dcef7ffaa1e1f9b0073aa`（< 10 MB）；印刷版 **6.450.106 B**，SHA-256 `2897b9c2481b460bd8dce7d3f78a340b29be65a1560b64d060d23bd1d2bd7e92`；均 8 页，与 §10 记录一致。8 张成图均为 1950×2700 并已逐版目检（无溢出、无重叠、无压页脚）。
- **口径注记**：校对人自备提取脚本计得本版可见字符（不含空格）35.730，核心版 30.100（与核心 KIT 数字恰合）；§4 记 35.733，相差 3 字符属计数口径微差（冻结已由字节级复跑证明），不作问题计。
- **核心完整性（校对后复验）**：核心版 8 个交付 SVG 的 SHA-256 与 §1 表逐一比对，**全部未变**。

### 结论

**一整轮独立全量校对零问题，PASS。** 本版无需修改，交付件即定稿件（上述 SVG / PDF 针脚即定稿针脚）。

## D5 rebuild (2026-11-13–14, D5-only)

SOP §1.1 font fix: the explanation layer's Latin letters move from Noto Sans CJK to Newsreader (SemiBold). No commit, no push — insertion is done by the closer after an independent re-proof. Work log: `hidden_files/d5-redo/scratch-2026-w43-pt/logs/2026-w43-pt-it/`; per-edition report: `production/notes/2026-w43/g-pt/scratch-d5-rebuild-pt/D5-REPORT-2026-w43-pt-it.md`.

**Install**: core landed with `apply_variant.py --patch-core pt --week 2026-w43` (production `core-pt/svglib.py`, `_D5_READER = "latin"` — the core template); this edition installed with `apply_variant.py --svglib patched/2026-w43-pt-it/svglib.py --target pt --reader it --week 2026-w43`, `_D5_READER = "latin"` (--check dry-run clean, RC 0); routing unit test `test_d5_routing.py` FAILURES: 0; fix2 block kept (5 occurrences).

**Baseline** (pre-fix production build): run TOTAL 150, 0 warnings; print/web/issued text layers 43,886 = 43,886 = 43,886 chars, multiset diff 0; baseline web PDF 716,765 B; print PDF 5,854,607 B (`aed50f11…`); pre-fix census D5 Latin 494, Cyrillic 0, curly in CJK 0; baseline P8 noted 150/150.

**Defects and fixes** (run1: 5 items, sizes only, no wording changed):

- P2-ex head `C　COMPLETE COM OS NÚMEROS`: content12.py:256 `e.head` 25→22
- P3-main head `DOIS INSTRUMENTOS, UM PAÍS`: content34.py:21 `f.head` 25→24
- P1 `CIFRE` box: content12.py:47 `f.box` close, `tsize` 23→22
- P1 `IN BREVE`: content12.py:132 `p.text` 24→21
- P2 `DA RICORDARE` box: content12.py:179 `f.box` close, `tsize` 23→21

P8: 220→220 lines, footer slack 41.7→41.7 px.

**Gates run2** (16 gates; no family gates.py for pt) — **ALL-GREEN (16/16 gates)**: run TOTAL 150, 0 warnings; head_check 0 defects; d5 census 0/0/0 (curly_total=0); render RC=0; webpdf RC=0 (641,287 B < 7 MB); occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff=[137, 138] (the registered reader-language keys); freeze baseline 8/8; freeze diff added CJK chars 0 (added Latin strings 250, run splits); spill 0; boxtitle 0 DEFECT (26 titles); edge 0 TOUCH 0 NEAR; creambox PASS 0 defects; text layer print=web 103,199 chars, multiset diff 0; textmd carryover PASS 0/0 (svg 5246 = md 5246 tokens); masthead gap (D18) 36.2 px PASS; census_quotes 0 defective.

**New deliverables**: print master `A-Lucerna-VOL1-pt-it.pdf` 5,353,932 B (`df3abee8…`); render-web `A-Lucerna-VOL1-pt-it-web.pdf` 3,299,664 B (`02bb6131…`); web (issues-type) `2026-w43-pt-it.web.pdf` 641,287 B (`e82569ff…`); text.md byte-identical to the shipped version (`461229b0…`). Still 150 exercises.

**Exporter note**: pt has no `.text.md` exporter (verified: the `ru_textmd.py` trial differed by 757 lines). The issued `issues/2026-w43/2026-w43-pt-it/2026-w43-pt-it.text.md` is carried over BYTE-IDENTICAL; content identity is verified by `verify_textmd.py` carryover jointly with gate 15 (print=web text layer diff 0).
