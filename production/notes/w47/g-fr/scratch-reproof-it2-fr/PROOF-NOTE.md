# PROOF-NOTE — W47 it-fr (法语读者 × 意大利语目标) re-proof · core D-2 fix 后重扩散新版

## 结论：(a) 零缺陷，可定稿

独立全量复校（SOP §8.4）完成：150 题三源逐题复核、1317 行全文精读、8 页逐页
200 dpi 目视、20 门机械门禁独立重跑、D-2 回归逐项独立重测、三 SHA 开工/收工
两次核对、印 PDF 重渲逐字节比对、核心 freeze baseline 8/8（build-copy 核实为
core-it 自身）。
**零缺陷。** 下方“记录在案的观察”共 5 项，均非缺陷（各有实测值与判定理由），
不触发返工。

## 对象与 SHA（开工、收工两次核对一致）

- 版：`production/2026-w47/2026-w47-it-fr/`，重扩散 2 新版（core D-2 fix，
  核心复校 (a) 之后重建；协调员 2026-11-11 21:58 UTC 盘上实测值）
- 印 `La-Lucerna-VOL4-FR.pdf` — sha256
  `e80d4dd3eb4c512c7d0c84c29c10fad56b927dc85f2b76663dcd82fef68727f0` / 14,034,054 B
- 网 `La-Lucerna-VOL4-FR-web.pdf` — sha256
  `d8fe0ef50efcfe7d2641e7ca737b618d8c06a529c6e33c016557f242c8977054` / 1,290,956 B
- 文 `2026-w47-it-fr.text.md` — sha256
  `aca1356c0c90526a7a621a399bc5ea9a75f9b635aae42662022217ddc01d5cad` / 56,517 B / 1317 行
- 修前生产三 SHA（`scratch-refanout-it2/shas-pre.txt`）：印 `6e393b3d…` /
  网 `7276c70f…` / 文 `a634057b…`（完整值见该文件）；文 −21 B（56,538 → 56,517）。
- KIT §7 所载印/网/文 SHA 与字节数与盘上一致；§12 重扩散节完整保留修前 SHA
  历史行；§8 门禁值与本次独立重跑逐值一致（见 GATE-LOG.md）。

## 工作方式（只读生产）

- 磁盘探针通过（`git hash-object -w /dev/null` → e69de29bb2…，RC=0 + scratch
  真实写盘 `probe.txt`）。
- 全部重跑在 goals-side scratch
  `hidden_files/w47/scratch-reproof-it2-fr/` 内做：整版复制到 `build/` 后改
  OUT/BASE 指向 scratch 副本再跑 run.py / render.py；生产文件零写入，
  收工重验三 SHA + 8 个 SVG sha256 全部不变（p7 以外 7 个 SVG 与 proof2
  记录值逐字一致；p7 为 D-2 改动，见下）。
- `PYTHONDONTWRITEBYTECODE=1` 全程；`TMPDIR` 为自有 scratch `tmp/`；未写 /tmp。
- web PDF 未重渲染（字节不可复现），只比文字层（见 GATE-LOG.md 门 7）。
- 门禁未复用 fan-out / proof2 的日志结论：`gates.py` / `translations.py` /
  `validate_edition_textmd.py` 复制到自有 scratch、路径重定向后独立重跑 20/20；
  freeze baseline、occlusion、p8、cream 扫、重建、重渲全部独立重跑。

## A. D-2 回归（逐项独立重测，全部通过）

新串就位（各 ×1）：
- `Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.`
  在 `text.md:775`、`content7.py:17`、p7 SVG、印/网 PDF P7 文字层各 1 处。
- `Il verbo è leggere, regolare al futuro: leggerò.`
  在 `text.md:777`、`content7.py:18`、p7 SVG、印/网 PDF P7 文字层各 1 处。
- 200 dpi 裁图 `crop-p7-a2.png`：两句渲染干净，桥接句
  `Parler de projets au futur : andremo, assaggeremo, guarderemo, leggeremo.`
  与 Q101–104 完好。

旧串清零（live 文件 0 处）：
- `Le forme sono regolari: andare` 与 `irregolare al futuro: leggerò` 在
  content7.py、p7 SVG、text.md、印/网 PDF 文字层均为 0。
- P7 文字层 `andare` 仍有 2 处，均与 D-2 旧串无关：Q101 题干原形提示
  `(andare)`，以及 B2 诊所句 `Andare vuole essere, non avere.`
  （助动词规则，改前已有）。

只许 P7 变化（与修前生产版 `scratch-refanout-it2/backup/` 对照）：
- SVG p1–p6/p8 逐字节一致、cards p1–p6/p8 逐字节一致；仅 p7 SVG/card 不同。
- text.md diff 恰为 :775/:777 两行 replace，−21 字节。
- content diff 恰为 `content7.py:17/:18` 两行；其余 content*.py / bslib4.py /
  svglib.py / run.py / render.py 逐字节一致。
- p7 SVG 文本节点 diff 仅限两句 D-2 句的换行碎片（旧 7 个非空节点 / 新 3 个
  非空节点，皆为两句的子串；节点总数 168 → 162）。
- p7 card 像素 diff（阈值 >12）局限于 x 87–508、y 387–1122，即 A2 栏
  （D-2 删例致段落短一行、全栏重排）；第 2/3 栏与右侧奶油盒 0 像素差异。

## B. P7 教学段语义事实核查（D-2 教训：读教学句本身）

A2 IL FUTURO 段两句的规则性标签现在正确（独立检索核实，非抄前人结论）：
- `assaggiare → assaggerò`、`guardare → guarderò` 列为**规则形**：正确。
  -are 动词未来时规则构形为词干 -er- + -ò（assaggerò、guarderò）。
- `leggere` 列为**regolare al futuro**：正确。leggere 是规则 -ere 动词，
  leggerò 即规则构形（不定式去尾 -e + -ò）。
- `andare` 已不再列为规则例：正确。andare 未来时**不规则**，词干 andr-
  （元音脱落型，andrò 而非 *anderò）；误标为规则正是 D-2 本身。
- 公开依据（2026-11-11 检索）：
  - dante-learning.com/eng/italian-future-tense/：不规则未来时词干表列
    andare → andr-（vowel-drop 组），规则表以 leggere → leggerò 为例。
  - flexiclasses.com/italian-grammar-bank/future-simple-tense/：规则动词表
    LEGGERE → io leggerò；不规则表 Andare → io andrò。
  - lbcc.pressbooks.pub/leggiamo2/chapter/309/：规则动词未来词干 = 不定式
    去 -e；不规则词干表 andare → andr-（andrò, andremo）。
  - fluentu.com/blog/italian/italian-future-tense/：同上，andare 列入
    删元音不规则组。
- 其余 P7 教学句亦逐句读过：B1 passato prossimo（essere 配合 / avere
  不变）、B2 congiuntivo（è probabile/possibile/bisogna che + 虚拟式；
  so che / scrivono che 后用直陈式）、ERRORI TIPICI 四条（La Lazio 单数、
  è probabile che + 虚拟式、andare 用 essere、torrone 单数）全部正确。
  全核心 `regolar` 仅此两行（FIX-LOG 已核，本轮 p7 SVG/text.md 重验一致），
  无其他同类错误断言。

## 全文精读（1317 行，逐题三源）

- 意大利语目标层：与核心 freeze diff 0 unexplained（P1–P7）；8 句金句逐句
  核对均在正文原样出现 ×2（`La Lazio resta in vetta`、`ventiquattro gol in
  dieci partite`、`il ponte votivo sul Canal Grande`、`oltre centocinquanta
  figuranti…`、`la squadra di Gattuso…`、`sette giorni di libri, ragioni e
  follie`、`il testo può ancora cambiare`、`approvato dal governo non vuol
  dire già legge`）。
- 法语讲解层：拼写、性数配合、变位、标点逐行读过，无错误；150 条答案的
  key 与 note 逐题对照题干/正文/图表复核（题面源 text.md 习题区、P8 印刷键
  p8 extract 150/150、核心 text.md 键 1–150 三方一致，gates 机械核对
  mismatches=[]；Q137–139 为重定向读者句键，与预期一致）。
- Q137–140 本地化标签：L969/971/973/975 为 `Traduire en français` ×3 +
  `Traduire en italien` ×1，`「翻譯」`/中文残留 0；Q137「Pour la Madonna
  della Salute, on traverse le pont votif.」/ Q138 / Q139 / Q140 译文均正确。
- 禁用词（Ucraina/Russia/Putin）0 命中；非 U+3000 的 CJK/西里尔字符 0；
  U+3000 ×101（家具分隔符）。
- 范文逐词数过 = 99 词（80–100 词要求内）。
- 算术重算：10 场赛果进球 3+1+2+3+3+2+3+1+2+4 = 24（与“24 球”一致）；
  13−11=2、6+7=13；Torrone 11月7–22日 = 16 天、三周末；
  BookCity 11月23–29日 = 7 天；Torino Film Festival 11月24日–12月2日 = 9 天。
- 日期星期（`TZ=Europe/Rome date -d` 全验）：11月6日周五、7日周六、8日周日、
  9日周一、12日周四、15日周日、16日周一、17日周二、19日周四、20日周五、
  21日周六、22日周日、23日周一、24日周二、29日周日、12月2日周三、
  12月6日周日、12月31日周四。文中全部星期主张（LUN 16 / MAR 17 / GIO 19 /
  VEN 20 / SAB 21 / DOM 22 / martedì 17 / giovedì 12 / lunedì 23 /
  martedì 24 / VEN 6.11 / SAB 7.11 / DOM 8.11）逐项正确；MER 18 无条目
  （D12 已接受，不编造）。
- 事实交叉（正文、表格、习题三方一致，并对公开来源抽查）：
  - Serie A 11 轮后：Lazio 29 / Inter 28 / Roma 27 / Milan 24 / Como 23 /
    Udinese 5；Roma 31 球最佳攻击；10 场赛果与积分一致。公开来源核实：
    williamhillnews.it（2026-11-09）、tuttoudinese.it、tuttomercatoweb.com、
    sportradar 全表一致；Gattuso 执教 Lazio、Napoli–Lazio 1–1、Inter–Como
    2–0、Roma–Sassuolo 3–0、Milan 2–1 Genova 均一致。
  - Torrone：29 届、11月7–22日、主题「Il Confine」、16 天、三周末、
    Torrone d'Oro 授予 Davide Simonetta（11月22日 11 时 Palatorrone）、
    16 时 corteo（150+ figuranti）、17 时 Sforza–Visconti 婚礼重演、
    sbandieratori 与火戏至 18 时、压轴「Il torrone va in brodo」。
    核实：festadeltorrone.com 官方日程 + foodtour.info / petitchef.it /
    lamescolanza.com 一致；1441 婚礼为传说（文中已写“leggenda”）。
  - Eurochocolate：32 届、11月13–22日、主题「Fate dolci」、Calabria 首个
    Regione Ospite（bergamotto、cedro、peperoncino、fichi）、「I tesori
    della Calabria Straordinaria」11月20日 18.15、Iginio Massari 压轴
    11月22日。核实：latuaetruria.it / radiosubasio.it / tagumbria.it 一致。
  - BookCity：15 届、11月23–29日、主题「Il senno sulla Luna」（Ariosto《Orlando
    furioso》）、1.360 eventi、2.487 protagonisti、1.164 libri、443 sedi、
    11月23日 20 时 Teatro Dal Verme 开幕、Colson Whitehead（两届 Pulitzer）。
    核实：milanoweekend.it / milano-business.com / visumnews.it /
    sudovestmilano.it 一致。11月22日 16 时 Fondazione Luigi Rovati 預覽
    Edmund de Waal 属日程细节，未单独检索，不影响题面（无题考此点）。
  - Torino Film Festival：44 届、11月24日–12月2日、9 天。
    核实：museocinema.it / boxofficebiz.it / quotidianocontribuenti.com 一致。
  - Filmmaker Festival：11月14日开幕、11月22日闭幕。核实：
    filmbyfilm.it / mentelocale.it 一致。
  - ATP Finals：11月15–22日都灵、8 人、两组、Zverev 世界第一、Alcaraz
    热门、Cobolli 意大利独苗首秀、Sinner（2025 冠军）因膝伤缺席。
    核实：thegiornale.it / monzalive.com / sportnews.snai.it / tntsports.co.uk
    一致。
  - Manovra：DPB 送布鲁塞尔 10月15日；2027 增长 +0,8%、赤字 3,4% PIL；
    10月28日内阁批准约 26 miliardi；C. 3174-bis；听证 11月9–12日
    （12日 Giorgetti 收官）；修正案截止 11月17日周二 18 时；Irpef 33%
    档由 50k 扩至 55k；12月31日前两院表决。核实：
    lamescolanza.com（DPB 10月13日政府批准、+0,8%/3,4%）、euroborsa.it
    （26 miliardi、3,4%）、takethedate.it（10月28日批准、听证 9–12日、
    17日 18 时、Irpef 50k→55k）、srlonline.com / rivalutazione-oro.it /
    fattiecontesto.it（A.C. 3174 于 10月30日提交、11月4日分拆后为
    A.C. 3174-bis，全部一致）。「约 5 miliardi 来自金融业」一句文中已标
    “secondo le prime ricostruzioni”（报道口径，非断言），本次未单独核实
    该估计值，见观察 O5。
  - 其他：Madonna della Salute 1630 誓愿、Longhena 设计、圣殿 1631–1687；
    Giornata nazionale degli alberi（1898 植树节起源、2013 年立法）；
    Santa Cecilia 11月22日；Torrazzo 为意大利最高砖砌中世纪钟楼——均为
    稳定史实，与正文一致，未见矛盾。

## 奶油盒像素裁决（交付渲染像素为准，STRADDLE 规则）

- 对重建卡片（与交付 SVG 字节一致、印 PDF 重渲逐字节一致，同一渲染）
  做逐盒像素扫（复用 proof2 `cream_scan.py`，同一方法）：29 个无边框奶油盒
  （#f0eee5），盒内最右墨点与盒边的余量全部 ≥0，最薄者见 O1；其余盒余量
  +7 至 +189 px；P7 三盒余量 +48/+26/+30（D-2 改动栏不在奶油盒内）。
- 四个表修标题的像素实测与 proof2 逐值一致：D1 cifre +7 px；D2 subtitle
  0 px（见 O1）；D3 frase +9 px；D4 errori +110–111 px。
- 备份旧版对照（STRADDLE 判定前必做）：p1–p6/p8 cards 与
  `scratch-refanout-it2/backup/` 逐字节一致，故其盒标题像素与已定稿
  proof2 版完全相同，无回归可能；p7 card 像素 diff 局限于 A2 栏
  （x 87–508、y 387–1122），右侧三奶油盒 0 像素差异。
- 判定：无一盒标题构成缺陷——无字形被裁、无墨水与另一元素或可见边框
  重叠、无与备份旧版的差异。

## 孤儿扫

- P8 SVG 与 proof2 版逐字节一致（94b069ae…）、P8 card 逐字节一致；
  proof2 精扫结论（0 处栏断孤儿）对本版仍然成立，本轮未重做全量孤儿扫，
  改为逐页目视 + P8 键区逐行核对：仅 1 处行内独词换行（P8 Q139 第二行
  `domicile`，见观察 O3），与 proof2 实测相同。
- 其余 7 页 flow 末端均在界内（见 GATE-LOG.md），无栏断孤儿的机械征兆。

## 8 版逐版看图（200 dpi 交付印 PDF 渲染）

- P1–P8 全页逐版看完（`render/view/p1–p8.png`）+ P7 A2 栏、P1 D2 字幕、
  P8 Q139 三张全分辨率裁图。版式干净一致：无溢出、无重叠、无压页脚、
  无缺字（tofu）、无图片错位。
- P3/P5 中部结构留白为核心既有版式（KIT §10 已接受），非缺陷（见 O4）。
- P6 练习用柱状图柱长与数值（Torino 5° / Milano 6° / Bologna 7° /
  Roma 11° / Napoli 13°）目视相符。
- P8 答案区末行 y=2514（底 2552），未侵页脚。

## 记录在案的观察（非缺陷，不返工）

### O1 — P1 D2 副标题像素余量 0 px：字墨恰触盒边，未越界
- 位置：`p1-prima.svg`，LA SETTIMANA 盒（x=1439.5, y=588, w=422.5, h=700，
  右边 x=1862）；节点 `Cette sem.　Cosa succede, giorno per giorno`。
- 实测（本次重跑 cream scan）：ink-right-in=1861，余量 0 px；与 proof2
  实测逐值相同；200 dpi 裁图 `crop-p1-d2.png` 显示 `giorno` 末字母完整、
  无裁切。
- 按 STRADDLE 判定为非缺陷：① 墨未越界，盒无边框、边几不可见，视觉上
  无缺陷；② 渲染确定性（印 PDF 重渲逐字节一致），余量稳定，非抖动；
  ③ 与备份旧版逐字节一致（p1 card 与 proof2 定稿版相同），无回归；
  ④ 同族已接受先例：it-de D1 副标题像素实测同样为 0 px，已随 de 版定稿；
  ⑤ 该法语形式已是最短式（全称 `Cette semaine` 更长），无更短替代。

### O2 — P1 D1 cifre 标题像素余量 +7 px（PIL +4.5 为悲观估计）
- 位置：`p1-prima.svg`，`LA SETTIMANA IN CIFRE　CHIFFRES`，盒右 x=961；
  本次实测 ink-right-in=953，余量 +7 px，在盒内，无处理。

### O3 — P8 Q139 键第二行独词 `domicile`
- 位置：p8 y=2172 行 `139. Samedi, la Lazio joue à domicile contre Lecce.
  — in casa = à`，y=2187 行仅 `domicile`（200 dpi 裁图 `crop-p8-q139.png`
  为证）；与 proof2 实测逐字相同。
- 判定为非缺陷的理由：① 非栏断孤儿——两行相邻、同属一条答案，读者
  可自然连读，无歧义、无丢失；② 2 行的 139 键已在 KIT §9 明确量测并接受
  （`139 = 2 lines`，P8 总量 4533 px < 4576 px 容量）；③ 同族接受模式：
  it-en / it-de 的 Q137 同样占 2 行；④ 全版 150 键中仅此 1 处独词换行，
  Q137 第二行是完整短语。

### O4 — 其余文体小注（均非缺陷，沿用 proof2 结论并重验）
- 动词变位注释（16–20、60–61）用全角冒号 `：`，系核心冻结原样沿用
  （KIT §8 已记），非 fan-out 残留。
- `(bougies (pluriel))` 双括号（13/14/37 题），全版统一写法。
- P2 E TU 法语行是意大利题干的简写提示，未译出“最佳作品登 VOL.5”
  从句；该承诺的法语版在 P7 LETTERE 披露中完整给出，故读者不失信息。
- Q137 note `(Compare avec l'original)` 为指向性提示而非释义，与
  138/139 的释义式 note 不同，但作为翻译题的提示足用。
- Q58 note `le plus beau dimanche soir (un jugement)` 将阴性 `serata`
  按意译为阳性 `dimanche soir`，为释义式意译（KIT §9 原定），非语法主张。
- P3/P5 中部结构留白为核心既有版式（KIT §10 已接受）。
- P8 答案 9.75 pt 为 SOP §1.1 下限（低于 11.25 pt 目标，让步第 4 步；
  与核心一致，无需扩版）。

### O5 — 「约 5 miliardi 来自金融业」为报道口径估计值
- 位置：P6 正文「circa 5 miliardi dal settore finanziario, banche e
  assicurazioni, secondo le prime ricostruzioni」。
- 文中已明确标注为“首批报道重建”的约数，非断言性事实；本次检索未
  单独核实该估计值（其余 manovra 数字全部核实，见上）。不构成缺陷，
  亦不建议为此返工。

## 只读合规

- 生产文件零修改：三 SHA 收工重验与开工一致；8 个 SVG sha256 重验一致
  （p7 除外：p7 为 D-2 改动，40b42701…，与重扩散宣称一致）；
  `git status` 仅见 D-2 fix 轮遗留的改动（core-it text.md/KIT 的 M、
  it-fr 未追踪目录），本次无新增改动。
- 未 commit、未 push、未重渲染交付的 web PDF；未改动 `core-it/`。
- 工具局限：无。本轮未改工具；`cream_scan.py` 复用 proof2 拷本（同一方法、
  同一脚本）；`gates.py` / `translations.py` /
  `validate_edition_textmd.py` 复用 fan-out 拷本（仅 SCRATCH 路径重定向）。

## 证据位置

- `hidden_files/w47/scratch-reproof-it2-fr/`：
  `PROOF-NOTE.md`（本件）、`GATE-LOG.md`、`probe.txt`、`run-rebuild.log`、
  `render/render.log`、`build/La-Lucerna-VOL4-FR.pdf`（重渲，与交付逐字节
  一致）、`freeze-core.log`、`freeze-core/`、`gates-fr.log`、`gates/`、
  `cream-scan.log`、`cream_scan.py`、`render/contact-sheet.png`、
  `render/pages/p1–p8.png`（200 dpi）、`render/view/p1–p8.png`、
  `render/crop-p7-a2.png`、`render/crop-p1-d2.png`、`render/crop-p8-q139.png`、
  `shipped-svg.sha256`、`rebuilt-svg.sha256`。
