# W45 ES × NL 独立校对报告（INDEPENDENT PROOFREAD）

- **待校版本**：`files/weekly-report-w45-es-nl/`（svg ×8、cards ×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- **核心对照**：`files/weekly-report-w45-es-core/`（已上架）；**W43 同配对对照**：`files/weekly-report-es-nl/`
- **校对员**：独立校对（只校对，未改源码、未派生下级代理、未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git）
- **开工查重**：开工前无 es-nl 进行中进程（仅无关的 ru-pt 入库在跑）；75 秒复查零新写盘后开工。校对中所有重渲染均在 `tools/scratch/` 副本内进行，实测前后核心哈希不变、分版哈希与 KIT 一致，未触动已发文件。

## 结论：不通过 —— 编号问题清单（见 §A）

**纸面（SVG / 卡面 / PDF）本身零缺陷**：全部 9 项核查中，纸面内容、几何、计数、家具均通过；
但 KIT 有 3 处数字/表述与实测不符。按任务规则“纸面零问题但 KIT 数字不一致同样判不通过”，
结论为**不通过**，问题全部在 KIT 文档层，**无需重建纸面**：修正 §A 的 3 处 KIT 行后，
仅需 KIT-only 复核即可转正（纸面无需重验）。

---

## §A 编号问题（全部为 KIT 数字/表述与实测不符，纸面无错）

### 问题 1（KIT §5）：P7 金句标签分布枚举错误 [BLOCKING-KIT]

- KIT 称：`(Pagina 1)×1、(Pagina 2)×2、(Pagina 3)×2、(Pagina 4)×1、(Pagina 5)×1、(Pagina 6)×1`。
- 独立实测（P7 FRASES 节逐项提取）：核心与分版**完全相同**，均为
  `[1, 2, 3, 4, 5, 6, 6, 1]`，即 **(Pagina 1)×2、(Pagina 2)×1、(Pagina 3)×1、(Pagina 4)×1、(Pagina 5)×1、(Pagina 6)×2**，总数 ×8 正确，分项枚举错误。
- 佐证：第 8 金句 «El domingo 8, Madrid tiene dos citas…» 的正文出处是 P1（核心与分版全文检索均仅命中 p1 + p7），
  其标签 (Pagina 1) 正确；KIT 的分布与该事实自相矛盾。
- 定性：纸面正确（与核心逐项一致），KIT 数字错。修正：按实测分布改写该句。

### 问题 2（KIT §5）：「zero (Página left」表述失实 [BLOCKING-KIT]

- KIT 称分版中「zero «(Página» left」。
- 独立实测：分版 P1 仍有 **2 处**带重音的 `(Página…)`，与核心 P1 **逐字节相同**的冻结西语正文：
  `(Página 4)`（ contents 相关行）与 `(Páginas 4 y 5)`（quiz 相关行）。
- 定性：纸面正确（冻结正文，未改动；金句标签已全部转为无重音 Pagina，P7 节 8/8 转换无误），
  KIT 表述越界。修正：改为「金句标签零残留；P1 两处冻结正文页码引用保留原样」。

### 问题 3（KIT §10）：图片载荷 SHA-256 针脚错误 [BLOCKING-KIT]

- KIT 称图片载荷：P3 `54adf4face…`、P5 `91bd483d…`。
- 独立实测（SVG 内嵌 base64 解码后哈希 = 构建 assets 文件哈希，核心与分版一致）：
  P3 烤栗子 `39eaac936006604ab544173c6e8b6f59cab966d847c4249bcad984c19d9f4655`（= `castanas.jpg`），
  P5 南瓜市场 `70542c15d5106c4a1a93fda258924c156660a59affa38c969c38db33deeaa57d`（= `kuerbis.jpg`）。
  KIT 所列两哈希在核心 KIT 与核心构建树中均无出处。
- 定性：纸面正确（图片载荷与核心逐字节相同，见 §B 第 5 项），KIT 针脚数字错。修正：按实测改写两哈希。
  （另：KIT §10 的 P1 插画「4 路径、joined sha 前缀 989cf5ae」已复核属实——换行拼接全元素哈希
  `989cf5ae2bae557f…`，核心与分版一致；该项无问题。）

---

## §B 逐项核查结果（任务 §1–§9，全部独立重测，不采信构建员自述）

### 1. 冻结基线（freeze）
- `freeze.py baseline` 核心构建：**8/8 SVG 字节一致**，核心哈希前后不变（p1 `a1b30102…` … p8 `d1c46fa4…`，与 KIT §1 全 8 前缀一致）。
- `freeze.py diff --strict-cjk` 核心 vs 分版：p1 +27/−25、p2 +54/−45、p3 +34/−30、p4 +32/−27、p5 +51/−40、p6 +28/−27、p7 +45/−42、p8 +201/−177，与 KIT §7 全页一致；**新增 CJK = 0**（P7 残留 2 字符仅为全角括号对，见第 8 项）。
- 西语词元多重集逐页核查（独立 token diff）：丢失词元**全部**归属备案类，无未备案丢失：
  P1 副标题家具（aprender/desde/el/españa/español/la/para/periódico/real/semanal/vida）；
  每页页脚家具（lucerna/spanish/weekly 各 −1/页）；
  P7 标签 página −8（11→3，余 3 为正文引用）、P8 分隔符 página −8；
  P8 #1 注释翻译（ahora/escriben/están/las/listas/los/presentadas/programas/se/ya）与 #102 注释（el −1）。
  无任何西语正文词元丢失。

### 2. P8 印刷笔记（p8.py compare + 独立 dash 解析）
- `p8.py compare`：**CLEAN，核心 150 = 分版 150，missing=[]，extra_count=0**；工具 keydiff =
  [17, 18, 19, 20, 60, 61, 62, 63, 64, 72, 83, 85, 95, 96, 98, 107, 117, 137, 138, 148]，与 KIT §6 一致。
- 独立 dash 解析（键 = 首个 ` — ` 之前，逐项复核）：18 项工具 keydiff 的键**逐字节相等**
  （#17 preguntan、#18 anochece、#19 descansamos、#20 dura、#60/#61/#62/#63/#64 整句、#72 acoge、
  #83 A、#85 C、#95 para que、#96 Aunque、#98 muestra、#107 mejor、#117 A、#148 A），确为提取器 artifact
  （荷兰语括号注释被吸入键字段，如 #72 分版 `acoge — acoger → acoge (het organiseert)`、#148 `A — firmar = tekenen (het contract)`）。
- **真改动仅 2 项**，均合法（翻译题重瞄准，W43 同配对先例）：
  #137 核心 «周一在九个自治区是假日。» → «Maandag is een feestdag in negen autonome regio's.»；
  #138 核心 «周日我们看 NFL 和马竞–巴萨。» → «Op zondag kijken we naar de NFL en Atlético–Barça.»；
  注释均为 «对照原文» → «zie het origineel»。反向题 #139/#140 键逐字节不变。
- #150 为写作题标记翻译（核心 «✓ 范文见本版 H 区（84 词）» → «✓ voorbeeldtekst in deel H (84 woorden)»），非键改动。
- 括号形式以家族构建代码为准：分版构建代码用半角 `(…)`、核心用全角 `（…）`；`bridge` 在分版构建代码中出现 0 次，
  `svglib.py` 与核心字节一致，`bslib4.py` 差异恰为页脚 2 行 + `bridge`→`expl` + gloss 前缀 3 处，与 KIT §2 一致。

### 3. 几何遮挡审计
- `occlusion_audit.py --selftest`：6 类 planted 全部恰好触发 1 次，干净对照静默。
- 分版实测：**0 flags**；`--core` 对照：核心 0 flags、**NEW flags = 0**。
- 同基线墨迹补充扫描（自写 OA 真墨盒实现）：核心与分版均为 **7 处亚 6px 间隙，集合完全相同**，
  全部为 P1 目录行 «Pág. N» 与标题的 **+4.0px 正向间隔**（非重叠），属冻结继承几何。
- P6 图表逐元素检查：图表区（y<1950）矩形 **16=16 字节一致**；CIS 条 408.0/266.4/205.2/73.2/37.2、
  主议题条 417.75/156.75/152.25、图表框一致；y<1950 文本 100=100，仅 2 处家具栏标题中→荷不同。

### 4. P6 Inmigración 约 5px 压字（仅报告存在性，不判问题）
- **存在，且与核心同一**：标签元素逐字节相同（x=1011, y=1717, 21pt serif bold）；
  真墨盒 x 1011–1144.25、y 1699–1722.5，与主议题条（x=1139 起、y=1699 高 22 的 20,9% 条）在 x 向重叠约 5.25px；
  核心墨盒与条形完全相同。属冻结核心几何，**非阻塞已知缺陷**，不因此判不通过；分版未触动图表。

### 5. 计数与复现性
- 注册表（scratch 副本单进程运行，分版与核心各跑一次）：**150 题、A2 50 / B1 72 / B2 28、
  分页 10/18/18/18/18/18/12/38**，类型计数与核心一一对应（荷兰语名：Zinnen aanvullen 48、Meerkeuze 47、
  Cloze-meerkeuze 13、Woorden combineren 12、Zinnen omvormen 10、Lezen: waar/onwaar 8、Zinnen maken 7、Vertalen 4、Schrijven 1），与 KIT §3 一致。
- Gloss（按 `·` 拆分构建代码 gloss 串，README #21 方法）：核心 19 = 分版 19，分盒 **5/5/5/4**，
  西语词头逐项相等（festivo/el puente/la comunidad/anochecer/el horario de invierno；sobrio/el homenaje/el disfraz/el boniato/el cementerio；
  la jornada/recortar la distancia/recibir/visitar/el Metropolitano；el emparrillado/el himno/el touchdown/la calabaza）。
- 图片载荷与核心逐字节相同（见问题 3 实测值）；P1 插画 4 路径一致。
- P7 金句 8 句：去引号裸句在核心与分版全文中**各恰 2 次**（正文 1 次 + P7 1 次），出处页 p1/p2/p3/p4/p5/p6/p6/p1 与标签一致。
- 范文：84 词（空白拆分），核心构建代码 MODELO 句在两版 SVG 中均逐字命中，与核心一致。
- 可复现性：`freeze.py baseline` 对分版构建复跑，**8/8 SVG 字节一致**，哈希与 KIT §11 全 8 一致。
- 字号调整属实：P6 练习体 19pt→18.5pt（分版 18.5pt ×35）、P8 答案行 13.5pt→13.2pt（分版 13.2pt ×174），图表/正文未动。

### 6. 读者园地（无编造）
- P7 «CARTAS DE LOS LECTORES»：Ana 西语信文 7 行（含全角括号署名）与核心**逐字节一致**；
  西语编注 «Nota de la redacción: al cierre no había cartas reales ni los mejores textos de la página 8; publicamos este ejemplo y la promesa pasa al VOL.3.» 逐字节一致。
- 荷兰语披露三事实齐全：「geen echte brieven」（无真实来信）、「beste pagina-8-teksten」（无最佳 P8 作文）、
  「voorbeeldbrief + Belofte: VOL.3」（示例信 + 承诺顺延 VOL.3）。
- 无编造人名/信件/引言；VOL.3 预告（西语冻结）仍邀请来信 + 最佳 P8 文本。

### 7. 家具三方对照（本版 / W43 已发同配对 / 工具箱 README #20）
- 徽章：**与 W43 元素几何完全相同**（x=975, y=372, 19.5pt, bold, #a4553a，文本
  «TEKSTEN IN HET SPAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS» 逐字相同），
  属 ES 家族副标题槽位情形（README #20），无需协调员裁决；本版与 README #20 描述无出入。
- 其余家具与 W43 一致（仅 VOL.1→VOL.2、本周主题、周日期属合法更新）：P1 副标题槽（46pt, y=330）、
  顶部条中段 «CADA SEMANA EN ESPAÑOL · ELKE WEEK · HET SPAANS DAT DE SPANJAARDEN LEZEN» 逐字节相同、
  页脚模板、gloss 前缀 «Uitleg — »（×5）、P8 分隔符 «— Pagina N —»（N=1..8）、P8 答案头、
  练习头 «EJERCICIOS · Oefeningen van pagina N»、答案指针 «Antwoorden op pagina 8 · Niveaus door elkaar — zoek op nummer»、
  栏目标题双语对（P6/P7 等）——以上逐项比对均一致。
- 与 W43 不一致的非主题项（见 §C 观察项，非阻塞）：P1 两处荷兰语缩短，语义完整、版式干净。

### 8. ABSTRACT、PDF、徽章/页脚、禁词
- ABSTRACT.txt：荷兰语单行（1 行，尾换行 1 个）、无 ASCII 双引号、含真实主题关键词
  （29 november 选举倒计时、huisvesting、2 november 九区长周末、8 november NFL Bernabéu 15:30 + Atlético–Barça 21:00）
  与学习者搜索短语 «Spaans leren met Spaans nieuws»；与 KIT §12 引用逐字一致。
- PDF 针脚与 KIT §11 一致：印刷 `La-Lucerna-VOL2-NL.pdf` **7,163,203 字节、8 页**、
  sha256 `7e0398c1412ac99e0934331f8672488347e9fc1fe7373a13e788c8b725c3fbec`；
  网页 `La-Lucerna-VOL2-NL-web.pdf` **3,739,003 字节（< 10 MB）、8 页**、
  sha256 `4130e4bef0c5d8150200307ed5fac2705929d95948edc1676408fcbc7bc7b549`；SVG 哈希全 8 在 KIT 中命中。
- 配对徽章 P1 齐全；每页页脚齐全（«La Lucerna · SPAANS WEEKBLAD VOL.2 · TEKSTEN IN HET SPAANS · UITLEG IN HET NEDERLANDS» + «Pagina N van 8»）。
- 全版零汉字（Han 字符 0 处/页）；P7 全角括号仅 1 对，确属冻结信件署名 «（ejemplo, escrito por la redacción）」，与核心一致。
- 「桥接」0 次、`bridge`（SVG）0 次；「12 de noviembre」0 次、「12 november」0 次（核心 Fix 1 未被重新引入）。
- 卡面：8 张 PNG 均为 1950×2700。

### 9. 卡面目视（8/8 全张）
- P1：徽章/副标题/头条/五要点/目录/quiz/插画/页脚干净，无溢出。
- P2：文章/日历/gloss/练习干净；无重叠。
- P3：烤栗子照片 + 信用行（Wikimedia Commons — CC0）干净；练习干净。
- P4：欧洲赛程表/练习干净。
- P5：南瓜市场照片 + 信用行（USDA 公共领域）干净；练习干净。
- P6：两图表标签与条形清晰（Inmigración 压字在卡面尺度下不可辨，几何已在第 4 项确认与核心同一）；18.5pt 练习无溢出。
- P7：三语法栏/纠错栏/词卡/读者园地/金句/VOL.3 预告干净；披露 3 行完整。
- P8：38 道终测 + 150 条答案 + 84 词范文干净，无截断；#137/#138 翻译题答案为荷兰语句，与重瞄准一致。

---

## §C 观察项（已判定为非问题，不计入 §A，仅备查）

- **O1（W43 家具措辞缩短 1）**：P1 底部 quiz 指针，W43 «Lees de voorpagina en kies het juiste antwoord · Antwoorden op pagina 8»
  → 本版 «Lees de voorpagina en kies · Antwoorden op pagina 8」（同槽位 1885, 2348, 20pt, anchor=end）。
  实测 W43 长串墨盒（x 1192.9–1884.9）亦无碰撞对象，缩短非版式所迫，但语义完整（quiz 语境下 kies 即选答案）、渲染干净，判非问题。
- **O2（W43 家具措辞缩短 2）**：P1 五要点栏头，W43 «Vijf sleutelpunten · Para entender la semana»
  → 本版 «Vijf sleutels · Para entender la semana」（同槽位 1473, 686, 19pt；W43 长串墨盒止于 1874.5，在框内 1885 之前，亦可容纳）。
  近义词缩短，语义完整、渲染干净，判非问题。建议协调员将两处记为本版接受变体，或在下一版恢复 W43 原文（恢复需重渲染 + 重校对，不建议为此返工）。
- **O3（P6 压字）**：见 §B 第 4 项，冻结核心几何，已裁定非阻塞，仅报告存在性。
- **O4（同基线 +4.0px 间隙）**：见 §B 第 3 项，核心与分版集合相同，正向间隔非重叠，非问题。
- **O5（KIT §2 fix5 坐标）**：复核属实——P7 CARTAS 框底恰为 1820.08，VOL.3 预告标题 y=2484.08，均与 KIT 一致。

---

## §D 需采取的行动

1. 修正 WEEKLY-KIT.md 三处（§A 问题 1–3），不改动任何 SVG/卡面/PDF。
2. 修正后仅做 KIT-only 复核（重算三处数字与 KIT 行比对），通过即可定稿入库；纸面无需重验。
3. 本报告不构成定稿放行；在 KIT 修正复核通过前，该版不得入库。

## 证明日志（独立重测，非构建员日志）

`hidden_files/w45/es-nl-proof/indep/`：`freeze-diff.log/.json`、`freeze-baseline.log`、`core-hashes-before/after.txt`、
`p8-compare.log/.json`、`occlusion-selftest/edition/withcore.log/.json`、`edition-rerun.log`、`edition-hashes.txt`、
`registry-core/edition.log`、`indep-check.py/.log`、`indep-check2.py/.log`、`indep-check3.py/.log`。
（构建员原日志保留于同目录未加前缀的文件中，本次结论未采信其中任何一项未经重测的断言。）
