# W47 zh-cn-it 第二轮独立校对笔记（re-proof，fix1 后）

- 校对员：独立复校员（与 zh-cn-it builder、fix1 修复员、proof1 校对员不同人）
- 对象：`production/2026-w47/2026-w47-zh-cn-it/`（fix1 后，2026-11-11）
- 日期：2026-11-11（EST 14:23 开工）
- 依据：SOP.md §8.4 / §1.1、WEEKLY-KIT.md（zh-cn-it，fix1 章节）、proof1 笔记
  （`scratch-proof-zh-cn-it1/PROOF-NOTE.md`，D-01～D-05）、核心
  `production/2026-w47/core-zh-cn/`（proof3 (a)）
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-zh-cn-it1/`
- 红线遵守：只读生产；未改任何生产文件、未 commit/push/insert、未重渲染交付的
  web PDF。run.py 重建与 render.py 重渲均在 scratch 副本里做（OUT/BASE 已重定向
  至 scratch；`PYTHONDONTWRITEBYTECODE=1` 全程，`TMPDIR` 指向 scratch）。
  开工/收工快照：39 个真实文件字节全同（见末节）。

## 开工探针

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` 成功（`e69de29b…`）。
- goals-side scratch 真实写盘成功（`probe.txt`）。
- 注：开工中途服务重启一次，打断了第一次重渲（cards 仅写到 p4、无 PDF 产出）；
  重跑一次即完成，RC=0，与交付印 PDF SHA 逐字节相同。生产未受影响。

## 身份核对（自行算出，与任务先验值逐字比对）

| 文件 | 字节 | SHA-256（完整，我方实测） | 与先验值 |
|---|---|---|---|
| 印刷 PDF `Lucerna-VOL4-IT.pdf` | 41,730,133 | `440490c4a389e22edc2c93f5b99fdb5bec857dafceeb1256e0f3af007598a69d` | 一致 |
| 网页 PDF `Lucerna-VOL4-IT-web.pdf` | 2,641,804 | `75dec91ac806b884bdd4b7cdbdccc39e2c445ff7f668d24ff4365f21f233a512` | 一致 |
| 文本导出 `2026-w47-zh-cn-it.text.md` | 50,916 | `afc9b2c02a319ab1d20227d3c0826942fc969aa577f61caea56b3845d664544f` | 一致 |

三 SHA 全符。双 PDF 均为 8 页。WEEKLY-KIT.md 所载三 SHA 与之一致。

## 结论：(a) 零缺陷，可定稿

按 SOP §8.4 全量独立复校：proof1 的 D-01～D-05 五项修复全部经 PIL 真墨 +
交付印 PDF 渲染像素双法重测通过（最小余量 +46.4 px，门限 +5 px）；17 门
机械门中 16 门通过，唯一 FAIL 的印/网文字层门为**已知预期项**（网 PDF 仍为
#3 版，仅 P1/P2/P5 有 5 处旧串，P3/P4/P6/P7/P8 均为 0——见 E-1，不作缺陷）；
其余全量检查（冻结、溢出、孤儿、150 题三方手验、语义抽查、日期、目视）零问题。
**无新缺陷（R-01…：0 条）。** 定稿决定权在协调员，本笔记只报事实。

## fix1 五项修复逐项独立重测（PIL 真墨 + 交付 PDF 渲染像素双法）

| 项 | 源码行 | 改后串 | PIL 真墨（墨右 / 盒右 / 余量） | 渲染像素（墨右 / 余量） | 结论 |
|---|---|---|---|---|---|
| D-01 | `content12.py:47` | `数字看本周　Questa settimana` | 893.5 / 961.0 / **+67.5** | 893.4 / **+67.6** | 通过 ✓ |
| D-02 | `content56.py:25` | `这一周的高频词　Parole chiave` | 892.5 / 961.0 / **+68.5** | 892.6 / **+68.4** | 通过 ✓ |
| D-03 | `content12.py:88` | `Chiusura: 10 nov. — la finale non giocata` | 1815.5 / 1862.0 / **+46.5** | 1815.6 / **+46.4** | 通过 ✓ |
| D-04 | `content12.py:187` | `本周生活小日历　Date utili` | 1294.0 / 1411.5 / **+117.5** | 1293.0 / **+118.5** | 通过 ✓ |
| D-05 | `content12.py:50` | `21 nov., sabato — esce il film 《试探》` | 单行，孤儿 `》`→0（见下） | 孤儿行无墨、原行有墨 | 通过 ✓ |

- 双法一致：四项标题/行尾双法差值 ≤1.0 px（D-04 差 1.0 px，其余 ≤0.2 px）。
- D-05 细核：`measure_final.py` 的 `PASS=False` 是检测器 artifact（它要求第一
  个 `<text>` 元素文本以 `》` 结尾，但构建把该项拆成两个同基线元素）；直接核 SVG：
  `21 nov., sabato — esce il film `（x=556.5, y=1339.265）+ `《试探》`
  （x=819.2，同一 y=1339.265），单行无疑；全刊行首闭合标点扫描 0 孤儿；渲染像素
  确认孤儿行无墨、原行有墨。修复属实。
- 渲染证据：`crop-p1-numbers-title.png`、`crop-p1-numbers-box.png`、
  `crop-p1-chiusura.png`、`crop-p2-cal-title.png`、`crop-p5-freq-title.png`
  （交付印 PDF 110 dpi 渲染；五图均显示标题/行尾完整落在奶油盒内，余量清晰可见）。
- P7 `Parole della settimana:` 词表头是另一元素，未改（KIT 已说明）；P1 :86
  长 Chiusura 段未动，其 `non ancora giocata` 属另一句（`alla chiusura non
  ancora giocata`），与 D-03 旧串不同，见旧串核查。

## P1 截稿行重点扫查（zh-cn-ru proof1 盲区教训）

P1 右栏日历盒（右缘 1862.0）全部 8 行 PIL 真墨逐行量取，无一越盒：

| y | 行 | 墨右 | 余量 |
|---|---|---|---|
| 1020.0 | `5. 11月11日—13日— 包裹揽收高峰` | 1778.8 | +83.2 |
| 1068.4 | `Chiusura: 10 nov. La finale è il 15 nov. alle` | 1805.5 | **+56.5** |
| 1093.4 | `ore 03:00 di Pechino — alla chiusura non` | 1797.5 | +64.5 |
| 1118.3 | `ancora giocata, il campione sarà` | 1730.5 | +131.5 |
| 1143.3 | `annunciato la prossima settimana. Le` | 1774.5 | +87.5 |
| 1168.3 | `semifinali (8–9 nov.) sono risultati completi.` | 1825.5 | +36.5 |
| 1224.0 | `Tutti gli orari, ora di Pechino` | 1696.5 | +165.5 |
| 1252.0 | `Chiusura: 10 nov. — la finale non giocata`（D-03） | 1815.5 | +46.5 |

最紧为段末行 +36.5 px，D-03 行 +46.5 px，第一行 +56.5 px——截稿行无越盒。

## D4/D5 同步与旧措辞复验（SVG joined-text 计数，去空白后复核）

| 项 | 实测 |
|---|---|
| D4 `全球总决赛的BO5` | P4 ×2（正文 + Q56 题干）✓ |
| D4 Q56 键注 `per la prima volta in un BO5 dei Worlds` | ×1 ✓ |
| D4 旧措辞 `第一次在BO5里打赢T1`（无限定）/ 英文旧键注 | 0 / 0 ✓ |
| D5 `GEN在S16一场没输` | P1+P4 ×2 ✓ |
| D5 `只丢了一小局` | ×2 ✓；`对LYON 2比1` ×1 ✓；保留 `淘汰赛一局没输` ×1 ✓ |
| D5 旧措辞 `GEN今年一局没输` / `GEN今年 — 一局没输` | 0 / 0 ✓ |
| fix1 旧串 5 项 | `Questa settimana in numeri` 0、`Date della settimana` 0、`esce il nuovo film` 0、`la finale non ancora giocata` 0；`Parole della settimana` 1× 仅为 P7 词表头（合法）；`non ancora giocata` 1× 仅为 :86 段内另一句（合法） |
| fix1 新串 5 项 | `Questa settimana` 2×（P1 标题 + P2 本周日历标题，另一既有元素）、`Parole chiave` 1×、`la finale non giocata` 1×、`Date utili` 1×、`esce il film` 1× ✓ |
| text.md 导出 diff | 当前 text.md 施加 5 处反向替换后，逐字节还原为 fix1 前文件：50,958 B，SHA `f954151fb204030d9d273e0f0032d9674509fd9bb170c7fc460c062eec46ecc4`——**diff 恰好 5 行**，与 KIT 声称一致；150 题键未动（见下） |

## 150 题三方手验（REG vs text.md vs P8）+ 语义抽查

- 分版 {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；级别 A2 56 / B1 69 /
  B2 25；题型 完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1；
  编号连续 1–150。均与 KIT 一致。
- keycheck：REG 150 条 vs P8 SVG 抽取键 150 条，**149/150 精确**；唯一非精确
  为 Q150 开放写作题（REG 键 `(开放题，范文如下)`，印刷键为 `✓`，为预期内的
  开放题标记——核心 P8 同位置亦印 `✓`，见下）。
- Q150 重组核实（任务专项）：p8.py 抽取并未截断——`p8extract.json` keys['150']
  = `✓`；交付 P8 SVG 实印：`150. ✓ Esercizio aperto — modello sopra, sezione F
  (138 caratteri).`（y=2490.964，与核心 `150. ✓ Open task - the model answer is
  printed in section F above (138 characters)` 同构同标）；范文自数 138 字，与
  run.py `writing model chars: 138` 一致。p8 compare CLEAN，keydiff=[]。
- 三方逐题：130 道非配对题题干在 text.md 与当页 SVG 中全部命中、键与 P8 抽取
  键全部一致；20 道配对题题干因左右两栏分开排版不连写（检测器 artifact，非缺陷），
  改按印出版面逐组核对，见下；配对词与释义在 text.md 中 20/20 成对存在。
- 配对题逐组核对（左词 → 右栏释义，键全部正确）：
  Q25–28 a/b/c/d（到货→a 东西到了；退换货→b；价保→c；派送→d）；
  Q43–46 b/d/a/c（小雪→b 二十四节气里的一个；三候→d 古人看天气的三个变化；
  保暖→a；着凉→c）；
  Q61–64 d/b/c/a（四强→d 最后四支队；止步→b；闹钟→c；五局三胜→a）；
  Q79–82 c/b/d/a（试探→c 试着问一问；悬疑→b；失踪→d；别墅→a）；
  Q97–100 c/d/a/b（说法→c 别人说的话；数据→d 量出来的数字；预报→a 还没发生的事；
  预计→b 大概的数字）。
- 单题语义抽查 11 题（≥8）：Q1（P4 正文“11月9日，BLG3比1打赢T1”→T1 ✓）、
  Q10（小雪 11月22日→B ✓）、Q38（P3“亲手摸古籍”→古籍 ✓）、Q56（D4 ✓）、
  Q83（P6“没有一天爆掉”→A ✓）、Q95（两根柱子：一为 22 天总数、一为单日最高→
  一天 ✓）、Q113（小雪 11月22日→对 ✓）、Q121（决赛 11月15日凌晨 3 点→B ✓）、
  Q130（决赛 BLG 对 GEN→A ✓）、Q141（P8 短文“小林住在深圳”→A ✓）、Q147
  （短文“他用取件码打开快递柜”→取件码 A ✓）。
- P8 短文日期：11月8日星期日、11月11日星期三、11月14日星期六，均与 `date -d` 一致。

## 金句 8 条逐字比对（SOP §4）

8 句在全刊各出现 **2 次**（正文 1 次 + P7 1 次），逐字一致：`决赛对阵GEN`（P1）、
`包裹都到了吗`（P2）、`小雪气寒而将雪矣`（P3）、`两支中国队进了四强`（P4）、
`先看简介，再决定`（P5）、`无高峰，全高峰`（P6）、`先打开看一看，再确认收货`
（P6）、`悦读深圳`（P3）。P7 金句带页码标注与正文出处一致（P1/P2/P3/P4/P5/P6）。

## 日期全验（`date -d`，America/Toronto）

2026-11-16 星期一（刊期首日）、2026-11-22 星期日（刊期末日/小雪）、2026-11-15
星期日（S16 决赛）、2026-11-21 星期六（《试探》上映）、2026-11-08 星期日（半决赛）、
2026-11-11 星期三（双 11）、2026-11-14 星期六（文化馆之夜）、2026-11-07 星期六
（美术馆日）、2026-11-06 星期五（《白衣逆行者》原定/《珠穆朗玛》）、2026-11-04
星期三（八强首日）、2026-11-09 星期一（半决赛次日）、2026-10-31 星期六、2026-10-20
星期二、2026-11-01 星期日（读书月首日）、2026-11-13 星期五、2026-11-10 星期二
（截稿）、2026-11-12 星期四（包裹高峰）——全部与版面所写星期一致。

## 几何专项

- 奶油盒横扫（521 个盒内文本元，PIL 真墨逐个量右缘）：溢出 **0**；仅 1 处贴边：
  P4「看比赛的中文　Parole delle partite」余 6.5 px（proof1 已记，通过，见 O-2）。
- 纵向：P5 行 `文化馆之夜在…月…日。`（y=2534.2）PIL 框底算得 2560.2，属
  PIL em 框 artifact——交付 PDF 渲染像素实测：该行实墨止于 svg y=2536.3，
  2560–2590 带 0 暗像素。无越底。
- P7 teaser 带：flow 终 2562.26（builder 值），渲染像素实墨止于 svg y=2560.7，
  离页脚线 2596 有 35 px 以上净空；核心同带止于低得多（意语文本更长所致），
  无裁字、无重叠、与 #3 版同位无回归。记观察 O-1，不计缺陷。
- spill 扫（全部 `<text>` PIL 真墨框 vs 1950×2700 版面）：出界 **0**。
  （UnifrakturMaguntia 盘上无字体文件，以更宽的 Noto Serif CJK Bold 代算，
  为保守上界；刊头居中，离边甚远。）
- 孤儿扫：本版 0，核心 0，**0 新增**。Q36/Q37/Q130 式填空行（P3/P8）与核心
  (x, y) 逐项同位，属核心继承，见 O-6。
- P4 赛程“半决赛3比1打赢T1。”居栏顶为断栏续句，与核心同句同位（核心 P4
  同文），非缺陷。

## 全量目视（自重渲卡片，印 PDF 字节与交付相同，不采信 builder 的图）

P1–P8 逐版目视：除已修复的 D-01～D-05 外，零溢出、零重叠、零压页脚、图片与
出处均在位。P1（拉丁-only 徽章、数字框、截稿行、目录、快讯照片）、P2（日历标题
离照片甚远、4 张词卡在盒内）、P3（小雪三候、节日小日历、读书月盒）、P4（Notes
盒 6 行、GEN 行净空、赛程表、C 头「读赛程」）、P5（C 头「时间与数字」、电影小日历）、
P6（22 天/单日双柱图 139.38/7.77、图表注）、P7（金句带 + 页码、teaser 带离页脚、
读者园地 + 意大利语披露）、P8（D 头「读一读，答一答」、keys 1–150 + 页脚）。

## 翻译层专项（fan-out 特有）

- 讲解/界面语言确为意大利语；拼写/性数抽查无误。泄漏扫描：无真实英文残留；
  英文形词均为有意保留（`Level A2/B1/B2`、`Sunday, Nov 22` 教学对照句、
  `Worlds` 赛事名、`Double 11` 活动名、`Barclays Center / Brooklyn`、
  `SF Express / Hunan`、`Sina` 专名、图注 `Foto: … — CC0 (Wikimedia Commons)`、
  `Sport` 意大利语同形、`test / trend / online / shopping / suspense / quiz`
  通用外来词）。
- 读者园地：P7 编者示例 + 意大利语披露，与 KIT / F-MAIL 规则一致。
- 刊头/页脚：`TESTO CINESE　SPIEGAZIONI IN ITALIANO` 拉丁-only 徽章（无中文半）；
  页脚 `Lucerna　简体中文周报 VOL.4　LUCERNA — SETTIMANALE IN CINESE SEMPLIFICATO`、
  页码行 `Pagina N di 8`（N=1–8）逐页核实；P7 的 VOL.3/VOL.5 为内容引用
  （下期预告 VOL.5、读者园地提 VOL.3），与核心逐字同位，非误印。
- U+2019：全刊 0；ABSTRACT.txt 319 B，意大利语单行，内容与本期事实一致。
- VOL.4：刊头/页脚逐页核实；§1.1 SVG 审计 clean（paper #fbfaf6 ×8、无离谱色、
  无描边页框、VOL.5 出现 1 次 = 核心同数）。

## 预期项（已知待全家统一重建状态，不作缺陷）

- **E-1**：网 PDF 仍为 #3 版（fix1 未重建，按任务要求全家统一重建），其文字层
  仍带 5 处旧串——`gates-zhcn.py` 印/网文字层门预期 FAIL。实测 token 差分：
  P1 web-only `ancora / in / numeri / nuovo`（旧 D-01/D-03/D-05 词）+ 断行
  token 化 artifact；P2 web-only `della / settimana`（旧 D-04），print-only
  `utili`；P5 web-only `della / settimana`（旧 D-02），print-only `chiave`；
  **P3/P4/P6/P7/P8 posdiff/msdiff 均为 0**。除 5 处旧串外两 PDF 文字层逐字相同。

## 观察项（单独列，不计缺陷）

- **O-1**：P7 teaser 带 flow 终 2562.26 / 实墨止于 2560.7，超 CONTENT_BOTTOM
  2560 约 0.7–2.3 px，但离页脚线 2596 有 35 px 以上净空，无裁字、无重叠，
  与 #3 版同位（proof1 已通过）。见「几何专项」。
- **O-2**：P4「看比赛的中文　Parole delle partite」盒标题余 6.5 px，贴边但未越，
  与 proof1 同值，未变。
- **O-3**：Q25–28 词汇配对键恰为 a/b/c/d 顺序（左右列同序），题过易；系核心继承
  的出题编排，键本身全部正确。
- **O-4**：P8 答案 9.98pt 高于 9.75pt 底线但低于 11.25pt 目标，属核心设计值
  （KIT §8 已记为让步 4）。
- **O-5**（承 proof1）：P1 Chiusura 段意语 `Le semifinali (8–9 nov.) sono
  risultati completi.` 措辞略生硬（应为 `sono concluse` 一类），但可解、无事实错；
  核心英文底本同构，属翻译层风格项。
- **O-6**：Q36/Q37/Q130 式填空行与核心 (x, y) 逐项同位，核心继承，观察类。
- **O-7**：`Level A2/B1/B2` 英文级名保留（KIT 已裁定）；`Sunday, Nov 22` 为 P7
  教学对照句中的英文例证；`next Sunday` 为冻结核心，永不作缺陷。

## 缺陷清单

**无。R-01…：0 条。**

## 未做事项（明示）

- 未重建/重渲染交付的 web PDF（任务明令：全家统一重建；只比文字层，已比）。
- 未复核核心版 zh-cn 自身的全部校对记录；核心事实（除 D4/D5 同步项外）以
  core proof3 (a) 为准。

## 生产零写入核对

- 开工快照 `snapshot-start.sha`（39 个真实文件：全部 .py 来源、SVG、PDF、
  text.md、KIT、ABSTRACT）vs 收工快照 `snapshot-end.sha`：**字节全同，diff 空**。
- `__pycache__/` 仅余开工已有的 `bslib4`/`svglib` 2 个 .pyc（我方全程
  `PYTHONDONTWRITEBYTECODE=1`，未新增）；.pyc 为导入缓存、未入 git、不属交付物。
