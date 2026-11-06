# 独立校对报告 — Lucerna Weekly W45 荷兰语 × 意大利语（NL × IT）

**结论：ZERO PROBLEMS（可定稿）**

- 校对对象：`files/weekly-report-w45-nl-it/`（svg × 8、cards × 8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照：W45 荷兰语核心 `files/weekly-report-w45-nl-core/`（VOL.2）与 W43 同配对版 `files/weekly-report-nl-it/`（VOL.1，家具以其实测为准）
- 校对员角色：只校对、不改源码、不宣布上架。未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录（只读对照）。
- 工具：`tools/`（`freeze.py`、`p8.py`、`occlusion_audit.py`），一律用 `tools/venv/bin/python` 运行；其余检查为本校对员独立脚本（见文末证据文件）。
- 校对全程未清理共享 scratch 目录（`tools/scratch/` 未动）。

## 开工查重（stand-down 检查）

- 首次检查（21:41 UTC）：交付目录最新 mtime 为 21:38（WEEKLY-KIT.md），此前构建写盘已结束。
- 120 秒复查（21:43 UTC）：交付目录与 `hidden_files/weekly-report-w45-nl-it-build/` 零新写盘；当时另有两个短暂进程（`hidden_files/w45/de-ko-reproof/` 相关）随后已自行结束，不属本分版、未写本分版目录。
- 结论：非进行中渲染，属已完成交付的新鲜 mtime，安全开工，未 stand down。

## 1. 冻结

- `freeze.py baseline`（核心构建目录 `hidden_files/weekly-report-w45-nl-build`，输出重定向至本校对目录）：**8/8 字节复现**，且运行前后核心哈希不变。
  - p1 `5424557b1798275b88f76dd4dadaf8b10996b36eef61ac2d1597de84d2c36280`
  - p2 `78e6fcd247a53972b339c474fc97d1cac93081bec17d111ec0238b5189fb5f5f`
  - p3 `5b9854e3c9c1e4882abdeef465e0484f1342afe456aa1c27f20348df20b07b74`
  - p4 `cc227fd9caf0dfab15de526367bd4b11a4ec6f744d871295bd4513e3b51c8431`
  - p5 `e58064c9927298ad25cf0cafad69a251c023cadd4e5333809cafd13483616865`
  - p6 `6583fe285e92969acd5149722fa372c7ad79dd9afa154d362a7efdd5310e0983`
  - p7 `65cfe2b3e45725e39eaa8a47794f543d29733bea9a458d0fde5f906c05071da9`
  - p8 `fe22a15107ab385b05326099c85f5175910e3d128dab561b5ec48ec094b795e0`
- `freeze.py diff` 核心 vs 分版（每页新增/删除字符串数；新增 CJK）：
  - p1 +32/−28，p2 +41/−33，p3 +32/−27，p4 +29/−25，p5 +41/−34，p6 +37/−32，p7 +47/−45，p8 +180/−167
  - **每页新增 CJK 均为 0**（核心 CJK/页 191 / 212 / 153 / 126 / 214 / 192 / 373 / 1033 → 分版 0）
- 校对前后核心哈希不变：开工前、基线运行后、校对结束三次哈希逐一相同（见 `core-before`/`core-after.sha`/`core-final.sha`）。
- 分版 SVG 哈希（与 KIT §9 逐一相符）：
  - p1 `b00135f11671894678785408ff457c189238f33f22211ff87429e6bb6b5eb21d`
  - p2 `10cb6dd8a247e74c9bd670f47b708008977059b6db3868ef0174534d58777be4`
  - p3 `6454819376591e6bd0630e4ebf8bee6f459a6da7ffe4eadf2dcade7f69d08668`
  - p4 `1542119759458439f110aa049672a06d6646179df7614299cbfc305bf21274ab`
  - p5 `4428f969dd8c15d5aab6b59eb3b2a7a585060f19d460a5d3bf18b00c34ed047b`
  - p6 `e79c935eac38bc30d712f6e0c392c3052a0bf980a0830ef13d8197386a890c2a`
  - p7 `adbdaf99e5ddbefe85916042923615b02326587e704b2f2d38e923ac6a72e57d`
  - p8 `444b41a423bb617e010adec14fdb8dbce1acebcaf7e59c45977b891b5a346ae2`

## 2. P8（`tools/p8.py compare`，显式 P8 路径，总数 150）

- **CLEAN：核心 150 noted = 分版 150 noted，missing []，extra 0，uncertain []**。EXTRA_ONLY 不适用（无多余项）。
- keydiff `[7, 17, 70, 71, 76, 96, 137, 138, 148]`，逐项对照两版印刷 P8 行核实如下（“印刷 key token” = 印刷行第一个 ` — ` 之前的 token）：

| 题 | 核心印刷行 | 分版印刷行 | 印刷 key token | 裁决 |
|---|---|---|---|---|
| 7 | `B — 气候周共 7 天（11 月 2–8 日）` | `B — La Settimana del clima dura 7 giorni (2–8 novembre)` | B = B，逐字节相同 | p8.py 括号分支提取伪影：仅注释语言不同，key 未变 |
| 17 | `wortelen — wortelen = 生根（复数主语）` | `wortelen — wortelen = mettere radici (soggetto plurale)` | wortelen = wortelen | 同上，伪影 |
| 70 | `eiland — eiland = 岛（het）` | `eiland — eiland = isola (het)` | eiland = eiland | 同上，伪影 |
| 71 | `proef — proef = 比赛项目、考验（de）` | `proef — proef = prova, sfida (de)` | proef = proef | 同上，伪影 |
| 76 | `gaat winnen — gaat winnen = 会赢（只是猜测）` | `gaat winnen — gaat winnen = vincerà (solo un'ipotesi)` | gaat winnen = gaat winnen | 同上，伪影 |
| 96 | `advies — advies = 建议（het）` | `advies — advies = consiglio (het)` | advies = advies | 同上，伪影 |
| 148 | `B — zachte = 柔软的（土壤）` | `B — zachte = morbido (terreno)` | B = B，逐字节相同 | 同上，伪影 |
| 137 | `气候周持续七天。 — 对照第 1 版头条` | `La Settimana del clima dura sette giorni. — Confronta con il titolo di pagina 1` | key 本身变化 | **真实重定向**：题面荷兰语句 `De Klimaatweek duurt zeven dagen. → ___` 不变（题型标注 `Traduci in italiano`），key 由中文译文改为意大利语译文 |
| 138 | `橙色预警意味着：做好准备。 — 第 2 版原句 · bereid je voor 做好准备` | `Il codice arancione significa: preparati. — Frase originale di pagina 2 · bereid je voor = preparati` | key 本身变化 | **真实重定向**：题面荷兰语句 `Code oranje betekent: bereid je voor. → ___` 不变（`Traduci in italiano`），key 由中文译文改为意大利语译文 |

- 伪影机理（已证实，非推测）：7/17/70/71/76/96/148 七项的 p8.py 方法均为 `paren`——注释末尾带括号时，工具把 ` — ` 后的整段译注吞入 key 字段，导致 keydiff；印刷 token 本身与核心逐字节相同。
- 139/140 **不在 keydiff 内，证实**：
  - 139：核心与分版 key 均为 `Museumnacht duurt van 19:00 uur tot 02:00 uur.`（逐字节相同）；题面方向互换已证实——核心题面为中文 `博物馆之夜从晚上 19 点到凌晨 2 点。→ ___`（`翻译`），分版题面为意大利语 `La Notte dei musei dura dalle 19:00 alle 02:00. → ___`（`Traduci in olandese`），key 仍为同一荷兰语句。
  - 140：核心与分版 key 均为 `Ik doe mee aan de Klimaatweek.`（逐字节相同）；题面方向互换已证实——核心题面为中文 `我参加气候周。→ ___`，分版题面为意大利语 `Io partecipo alla Settimana del clima. → ___`（`Traduci in olandese`）。
  - 150：key `✓` 两版相同；印刷行仅为范文指针的语言转换（核心 `✓ 范文见本版 H 区（87 词）` → 分版 `✓ Vedi il testo modello nella sezione H (87 parole)`），范文荷兰语正文逐字相同，87 词（见 §9）。

## 3. P7 词框冻结

- 核心荷兰语定义句在分版 P7 词框（x=1473，y=1089–1150）内**逐字保留**：
  > «meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee.
- 与核心同区域定义句逐字相同；**无定义句本地化**。
- 其下 gloss 仅本地化为意大利语（x=1473，y=1210–1239）：
  > meedoen = partecipare: tutta l'Olanda partecipa.
- 通过。

## 4. 几何遮挡

- `tools/occlusion_audit.py`（自测 OK，6 类 planted 全部触发、clean 对照静默）：
  - 分版 **0 flags**，核心 **0 flags**，NEW vs 核心 **0**。
- 同基线墨迹碰撞扫描（独立实现：PIL 真实墨迹盒，同基线分组，8 页）：
  - p1–p8 **全部 CLEAN，0 碰撞**（含 P1 顶栏）。
- P6 图表标签覆盖（基线锚定墨迹法：getbbox 左右 + getmetrics ascent/descent 定上下，图表区 x 1451–1885、y 200–720 内全部文本 vs 其后全部 rect）：
  - **最差覆盖 0.0%**（无任何非零覆盖项），< 30% 阈值，通过。
  - 以 PIL `anchor="ls"` 直接取框复测：同样 **0.0%**。getbbox 法的虚高读数未被采用（本项两次方法均为基线锚定，结论一致）。
  - 图表值已核对：45 / 25 / 20 / 10，和为 100；荷兰语 `OEFENDATA` 说明与意大利语标题/说明 `DATI DI PROVA` 均在页上；图表标题 `DE GRAFIEK · DATI DI PROVA`、投票框标题 `VOOR OF TEGEN? · PRO O CONTRO?` 均完整落入框内（卡片目视亦确认）。

## 5. gloss 计数（渲染后 gloss 字符串本身，按 `·` 拆分）

方法：从分版 SVG 提取以 `Nota — ` 起始的 gloss 框全部折行并以空格连接成渲染字符串，再按 `·` 拆分；核心同法（核心前缀为 `译注｜`，P1 为 `讲解｜`，仅前缀不同）。

| 页 | 分版渲染 gloss（拆分后项数） | 核心（项数） | 对照 |
|---|---|---|---|
| P2 | het klimaat = clima · wortelen = mettere radici · besparen = risparmiare · de verwarming = riscaldamento · de waarschuwing = avviso, allarme · lokaal = locale.（**6**） | 6 | 6=6 |
| P3 | het museum = museo · de rondleiding = visita guidata · het tijdslot = fascia oraria · tweedehands = di seconda mano · de beurs = fiera, mercato.（**5**） | 5 | 5=5 |
| P4 | de balans = il bilancio finale · gelijkspelen = pareggiare · de speelronde = giornata · de topper = il big match · de stand = la classifica.（**5**） | 5 | 5=5 |
| P5 | het eiland = isola · de proef = prova, sfida · stemmen = votare · de aflevering = puntata · voorbij = finito, passato.（**5**） | 5 | 5=5 |
| P6 | de meteoroloog = meteorologo · waarschuwingsmoeheid = stanchezza da allarmi · vastzetten = fissare bene · het advies = consiglio · de voorstander = sostenitore.（**5**） | 5 | 5=5 |

- 核心与分版 1:1。另：P1 gloss 框 4 项、P7 三个 bridge 分别为 4 / 3 / 3 项（A2：het klimaat；een boom planten；besparen；de waarschuwing。B1：meedoen；opruimen；vastzetten。B2：Ik vind dat…；Volgens mij…；Het lijkt me dat…），与构建员自述一致。

## 6. P7 金句

P7 金句与核心逐句、逐页码标签完全相同；每句在全刊归一化文本中恰出现 2 次（源文章 + P7），且在其标注页上实测存在：

| 金句（荷兰语） | 页码标签 | 全刊出现次数 | 标注页实测 |
|---|---|---|---|
| Van maandag 2 tot en met zondag 8 november is het Klimaatweek in Nederland | Pagina 1 | 2 | P1 存在 |
| De herfst is de beste tijd om te planten | Pagina 1 | 2 | P1 存在 |
| Geel betekent: let op, het weer kan gevaarlijk zijn | Pagina 2 | 2 | P2 存在 |
| Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts | Pagina 3 | 2 | P3 存在 |
| Ajax won donderdag 22 oktober met 2–0 van Atalanta | Pagina 4 | 2 | P4 存在 |
| Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur | Pagina 5 | 2 | P5 存在 |
| Een code is geen verbod, maar een advies | Pagina 6 | 2 | P6 存在 |
| Het weer is van ons allemaal, maar het raakt ons allemaal anders | Pagina 6 | 2 | P6 存在 |

- 页码标签序列与核心一致：1, 1, 2, 3, 4, 5, 6, 6。P7 短语区标题亦注明 `(PAROLE TESTUALI DA QUESTO NUMERO)`，8 句均取自本期文章（上表第 3 列的源文章一次即为证）。

## 7. 读者园地（零编造）

P7 右栏（x=1473）实测：

- 示例明确标注为编辑部示例：`— Li (voorbeeldbrief van de redactie)`，示例信正文为荷兰语原文（Li 在上海学荷兰语、气候周在阳台种树），未冒充真实来信。
- 荷兰语披露句原文保留：
  > Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3.
- 意大利语披露句同义：
  > Alla stampa: niente lettere vere, niente migliori testi di pagina 8 — quindi un esempio; promessa rimandata al VOL.3.
- 三事实同时在页：(1) 截稿时无真实来信（`nog geen echte brieven` / `niente lettere vere`）；(2) 无最佳 P8 作文（`beste pagina-8-teksten` / `migliori testi di pagina 8`）；(3) 示例 + VOL.3 承诺（`dit voorbeeld; belofte naar VOL.3` / `esempio; promessa rimandata al VOL.3`）。
- 显性意大利语邀请（构建员所称原文，逐字核实存在）：
  > Esempio della redazione, non una lettera vera. Mandaci lettera e testo di pagina 8: li pubblicheremo nel VOL.3!
  - 祈使句 `Mandaci` + 刊登承诺 `li pubblicheremo nel VOL.3` 齐备，属显性邀请；页底 `VOLGENDE WEEK` 内容预告行（提及来信与 P8 佳作）未被计作邀请。
- 页上无其他读者、来信、姓名或引言被编造。通过。

## 8. 家具（W43 实测胜泛写）

- **徽章（P1，y=568）**：`TESTI IN OLANDESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI`，20pt 粗体、BRICK #a4553a、居中（x=975，text-anchor=middle），与 W43 同配对版字符串、y、字号、粗细、颜色、锚点全部相同；PIL Sans Bold 20pt 实测宽度 **840.89px（分版）= 840.89px（W43）**，构建员所称 840.9px 属四舍五入一致。
- **荷兰语 strapline（y=372）原样保留**：`DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS`，与核心逐字相同。
- **副标题（y=330，36pt 粗体 serif）**：`SETTIMANALE OLANDESE · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12`，实测 **1619.95px ≤ 1820**；W43 同位置副标题（36pt）实测 1764.78px，与构建员所称 1764.8px 一致。
- **gloss 前缀**：P1–P6 全部 gloss 框前缀均为 `Nota — `，与 W43 同配对版前缀相同。
- **顶栏（P1，y=92）**：左 `VOL. 2`、中 `ELKE WEEK IN HET NEDERLANDS · OGNI SETTIMANA IN OLANDESE`（21pt，W43 IT 字符串）、右荷兰语周日期 `WEEK VAN 2 TOT EN MET 8 NOVEMBER 2026`，与核心日期一致。
- **页脚 8/8 标 VOL.2**：每页 y=2624 页脚均为 `De Lucerna · SETTIMANALE OLANDESE VOL.2 · TESTI IN OLANDESE · SPIEGAZIONI IN ITALIANO`，实测宽度 908.0px（W43 页脚亦为 908.0px，VOL.1/VOL.2 同宽）；页码行 `Pagina N di 8`（N=1–8）逐页正确。
- **刊头**：`De Lucerna` 与核心一致；P1 右侧 band 为 `SETTIMANA DEL CLIMA` / `Tutta la nazione partecipa · vedi pagina 2`。
- 另核实（构建员 §8 定稿措辞）：P1 议程副标题 `Agenda van de week · GLI EVENTI`、议程脚注两行 `Tutte le date e gli orari sono` / `negli articoli alle pagine 2–4.`、P6 标题与投票标题（见 §4）均已在最终 SVG 中，终版遮挡 0 旗标与之相符。

## 9. 其他

- **页数/题量/级别**：8 页；从已发布 SVG 题面标记独立清点（P8 答案区除外，范围标记展开，级别取题号前紧邻的 A2/B1/B2 标签）：**150 题**，每页 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38，**A2 47 / B1 72 / B2 31**，与核心同一方法清点结果完全相同。范文荷兰语正文逐字与核心相同，**87 词**（不含 `Tekstmodel:` 标签），在 80–100 要求内。
- **图片**：仅公有领域/CC0 图片；`<image>` 元素 P1–P4 各 1 个、P5–P8 各 0 个，与核心逐元素完全相同（未引入新图）。4 张署名图片均已排版，credit 行：
  - P1 `Foto: Vovogov90 — CC0`
  - P2 `Foto: Nationaal Archief — CC0`
  - P3 `Foto: W. Punt / Anefo, Nationaal Archief — CC0`
  - P4 `Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein`（SVG 中折为两行，第二行 `domein`）
  - 4 行与核心逐字相同；见“与构建员自述不符处”第 1 条（仅 KIT 转述省略，不影响排版行本身）。
- **禁词/禁字符（全部 8 页文本层）**：`桥接` 0、CJK 0、ASCII 双引号 0、双空格 0、带空格的 guillemet（`« ` / ` »`）0。
- **ABSTRACT.txt**：意大利语单行，无 ASCII 双引号：
  > De Lucerna, settimanale olandese VOL.2 per lettori italiani: la Settimana del clima 2–8 novembre, la Notte dei musei di Amsterdam il 7 novembre, il festival Crossing Border e la 12ª giornata di Eredivisie con Twente–Ajax; testi in olandese con spiegazioni in italiano, livelli A2–B2, 150 esercizi per imparare l'olandese leggendo le notizie olandesi.
- **PDF**：印刷 PDF `De-Lucerna-VOL2-IT.pdf` **7,915,647 B**，sha256 `fee7c18ccf19e3884ec5e3cc94add80542392ce4ffc235a55d84327b668a3c74`，8 页；网页 PDF `De-Lucerna-VOL2-IT-web.pdf` **3,658,192 B**，sha256 `5f1e481ac83ae22bf911cbc7c808a6623c5ee5826187905e3746960cfeec8a19`，8 页（均与任务给定值及 KIT §9 相符，pypdf 核实页数）。
- **卡片逐页目视检查（8 张，1950×2700 PNG）**：P1（刊头/徽章/议程/词框/照片/quiz）、P2（代码框/gloss/练习）、P3（照片/gloss/练习）、P4（1912 球队照/gloss/练习）、P5（gloss/练习）、P6（图表/投票框/gloss/练习）、P7（词框/读者园地/金句/下周预告）、P8（练习 113–150/答案键 1–150/范文）——**全部无重叠、无截断、无缺陷**。P7 第 3 栏栈在金句横线之上收束，P8 答案键块在页脚之上收束，与遮挡 0 旗标一致。

## 与构建员自述不符处（均不阻塞）

1. **KIT §4 的 P4 credit 转述省略**：KIT 写 `Foto: Spaarnestad Photo — publiek domein`，但实际排版行（分版与核心、W43 逐字相同）为 `Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein`。排版行本身无误，属 KIT 转述不完整，不阻塞定稿（建议后续 KIT 修订时补全，不由本校对改动交付物）。
2. **gloss 计数方法差异，结果一致**：构建员 rowcheck 比的是构建代码中的 `gloss()` 调用串；本校对按任务要求改按**渲染后字符串本身**拆 `·` 计数，结果仍为 P2 6=6、P3–P6 各 5=5。方法更强，结论不变。
3. 其余构建员关键自述均经独立重测证实：徽章 840.9px（实测 840.89）、副标题 1619.95px、页脚 908.0px、P8 CLEAN 与 keydiff 清单、遮挡 0/0/0、图表覆盖 0.0%、金句 2× 与页码标签、P7 词框冻结句、读者园地邀请句、PDF 字节数与哈希——**无其他不符**。

## 非阻塞观察（注明不阻塞）

1. P2 右栏匹配项 `c. voor je eigen omgeving, niet overal` 墨迹右缘为 1880.0px，距 1885 栏界仅 5px，视觉完整、无截断，遮挡与同基线扫描均清白。属紧贴但合格，不阻塞。
2. P4 顶栏仅 `SPORT` 一词（无意大利语并列词），与 W43/KIT 的栏目头形式一致，属核心版式，非缺陷。
3. 范围说明：本题型分布（Completa 65 等）未从已发布 SVG 逐项重数——不在本次任务的门内，题量/级别/页分布已独立重数并与核心一致；Commons Artist 字段未重新联网查询——4 条 credit 与冻结核心/W43 逐字相同，未引入新 credit，故无新风险；构建日志中的“零警告”未从交付物反推——几何结果已由遮挡、同基线、图表覆盖与 8 页目视四重覆盖。
4. 本校对未清理共享 scratch，未动用任何构建/发布通道；校对后核心哈希仍与开工前一致。

## 证据文件（本校对目录）

- [REPORT.md](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof/REPORT.md)（本文件）
- [check_all.py](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof/check_all.py) + [check_all.json](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof/check_all.json) + [check_all.log](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof/check_all.log)（家具/gloss/金句/读者园地/图表/同基线/禁词/卡片尺寸）
- [freeze-baseline.log](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof/freeze-baseline.log) + [freeze-diff.log](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof/freeze-diff.log) + [freeze-diff.json](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof/freeze-diff.json)（基线 8/8、新增 CJK 0）
- [p8-compare.log](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof/p8-compare.log) + [p8-compare.json](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof/p8-compare.json)（CLEAN 150=150、keydiff）
- [occlusion.log](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof/occlusion.log) + [occlusion-ed.log](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof/occlusion-ed.log) + [occlusion-core.log](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof/occlusion-core.log)（分版 0 / 核心 0 / NEW 0）
- [exercise_inventory.py](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof/exercise_inventory.py) + [exercise_inventory.log](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof/exercise_inventory.log)（150 题、页分布、级别分布）
- [edition.sha](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof/edition.sha) + [core-final.sha](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof/core-final.sha)（分版哈希、校对结束时核心哈希）
