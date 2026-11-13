# PROOF-NOTE — 2026-W47 ja-es 第一轮独立校对（叶子）

- 校对员：叶子（独立第一轮；与 builder、core-ja builder、各轮复校员不同人）
- 对象：`production/2026-w47/fanout-ja/2026-w47-ja-es/`（未入仓，工作树 untracked）
- 日期：2026-11-11（UTC 05:30–07:00 左右）
- 结论：**(b) 缺陷清单 — 1 个缺陷类，共 6 处 P8 答案注文**，见 D1。未达“零问题可定稿”。
  除 D1 外，其余核查全部通过（机械门全绿、150 题逐题验算通过、翻译层通过、8 版目视通过）。
- 本人只检查、不改任何源码/成品：构建目录 8 个 SVG 的 SHA 在校对开始与结束时逐一核对，
  全部未变；重跑构建是在本人 scratch 区的完整副本里做的（见 GATE-LOG）。

## 0. 身份核对（先核身份，双 PDF 均符）

| 文件 | 字节 | SHA-256（完整，自行算出） |
|---|---|---|
| 印刷 PDF `Lucerna-VOL4-JA-ES.pdf` | 29,102,097 | `0feb61136c4c9c267a9c84664287c6bb1a897ddb2fc496d79137073542eacb55` |
| 网页 PDF `Lucerna-VOL4-JA-ES-web.pdf` | 4,482,717 | `b274eac2faa2a91cdeefc303092805253b34f3cacfef095cded332cee5e95380` |

与 KIT §8 登记的字节数与完整 SHA 逐字一致；两 PDF 均为 8 页。探针双通后才动手
（`git hash-object -w` 成功；`hidden_files/w47/scratch-proof-ja-es1/.probe` 真实写入成功）。

## 1. 缺陷清单

### D1 — P8 答案注文里两名相扑力士的罗马字拼写错误（事实性错误）

- 严重度：**高**。印在答案页上的真人姓名拼错；题面（汉字）与键值（字母/数字）本身无误，
  错只在西班牙文注文的罗马字人名。6 条注文受影响，均在 P8 答案区。
- 证据（公开来源，多方一致）：
  - 美ノ海 ＝ ちゅらのうみ（Chura-no-umi）。日本相撲協会公示经由：
    sumo-guide.com「美ノ海 義久（ちゅらのうみ よしひさ）」；
    日刊スポーツ 2018-05-30「美ノ海（ちゅらのうみ）」；
    デイリー 2026-10-27「美ノ海義久（ちゅらのうみ・よしひさ）」。
    「美」在此读 ちゅら（冲绳方言“美”），绝非 umi。
  - 藤凌駕 ＝ ふじりょうが（Fujiryōga）。日本相撲協会公示经由：
    sumo-guide.com「藤凌駕 雅治（ふじりょうが まさはる）」；
    日刊スポーツ 2025-10-01「藤凌駕（ふじりょうが）」；
    ozumo.jp「藤凌駕は『ふじりょうが まさはる』と読む」。
    りょう（长 o）误作 りゅう（ū）即为另一个名字。
  - 上述来源同时佐证了正文事实无误：大の里“2場所連続優勝をねらう、初日義ノ富士・2日目藤凌駕”
    （サンスポ 2026-11-06）；藤凌駕“初土俵から11場所目で金星”“7位のスピード金星”
    （日刊スポーツ 2026-11-10）；美ノ海新小結（デイリー 2026-10-27）。错的只是罗马字本身。
- 受影响的 6 条（原文 → 应为）：

| # | 位置（P8 答案区，— PÁGINA N — 分组） | 原文 | 应为 |
|---|---|---|---|
| 1 | P8，— PÁGINA 4 —，第 48 条 | `48. B — Umi-no-umi perdió contra Hōshōryū el día 1` | `48. B — Chura-no-umi perdió contra Hōshōryū el día 1` |
| 2 | P8，— PÁGINA 4 —，第 49 条 | `49. A — Fujiryūga venció a Hōshōryū el día 3` | `49. A — Fujiryōga venció a Hōshōryū el día 3` |
| 3 | P8，— PÁGINA 4 —，第 54 条 | `54. 11 — El kinboshi de Fujiryūga: 11.º torneo desde su debut` | `… de Fujiryōga: …` |
| 4 | P8，— PÁGINA 4 —，第 63 条 | `63. ○ — Fujiryūga ganó un kinboshi el día 3` | `63. ○ — Fujiryōga ganó un kinboshi el día 3` |
| 5 | P8，— PÁGINA 7 —，第 111 条 | `111. 11 — El kinboshi de Fujiryūga: 11.º torneo desde su debut` | `… de Fujiryōga: …` |
| 6 | P8，— PÁGINA 8 —，第 116 条 | `116. A — Hōshōryū perdió contra Fujiryūga el día 3` | `116. A — Hōshōryū perdió contra Fujiryōga el día 3` |

- 排查范围：全版罗马字人名清单已逐一核对——Ōnosato（大の里）、Hōshōryū（豊昇龍）、
  Yoshinofuji（義ノ富士）、Miyajima、Shōsetsu、Tori-no-ichi、Ni-no-tori、Asakusa、Kioto、
  Miura Riku、Kihara Ryuichi、ryuuryuu、Chiikawa 均正确；题面与 P7 均用汉字，无罗马字，
  故错误只在上述 6 条 P8 注文。`Fujiryūga` 全版共 5 处、`Umi-no-umi` 全版共 1 处，
  与上表 6 条注文一一对应，无遗漏。
- 注：此错为 fan-out 层引入（核心版注文为中文、无罗马字；p8.py compare 只比对键值，
  不比对注文散文，故机械门拦不住——见观察项 O8）。

## 2. 已核对通过的项目（事实摘要）

### 2.1 机械门（全部自跑，见 GATE-LOG.md）
- occlusion：自检 6 类全触发、干净对照静默；实跑 **0 flags**。
- p8 extract：noted set **150/150**（`--total 150`）。
- p8 compare（vs core-ja P8）：status **CLEAN**，missing=[]，extra=0，uncertain=[]，
  keydiff=**[137, 138, 139, 140]**，与预期完全一致；其余 146 个键值逐字相同。
- freeze：`tools/venv/bin/python run.py` 在本人 scratch 副本里重跑，exit 0，
  FLOW OVERFLOW / HEAD TOO WIDE 计 0，8 个 SVG 与原构建 **8/8 字节相同**。
  构建解释器即 KIT §9 所指的 `tools/venv/bin/python`（Python 3.12.3，Pillow 13.0.0）。
  重跑 registry 与 KIT 一致：TOTAL 150；级别 A2 48 / B1 73 / B2 29；
  分版 10/18/18/18/18/18/12/38；题型 completa 50、opción múltiple 51、relacionar 12、
  construye una frase 8、verdadero o falso 11、cloze 13、Traduce 4、Redacción 1；
  范文 154 字（本人另从 text.md 实数 154 字，一致）。
- print/web 文字层：pdftotext 各 102,065 字节，**逐字节相同**；web PDF 4,482,717 字节 < 7 MB。
- U+2019：8 个 SVG 总数 **0**；text.md 中 U+2019 与直撇号均为 0；含撇号的行目视无宽字形断裂。
- P8 字号（PyMuPDF 测印刷 PDF 第 8 页）：最小 **9.98pt ≥ 9.75pt**；次档 10.35pt（题干，79 个 span），
  与 KIT 登记的 9.975pt / 10.35pt 一致；题干 10.35pt 不动（已 adjudication，不列缺陷）。

### 2.2 150 题逐题验算
- 题号 1–150 连续无缺重（text.md：“N.” 独行 138 条 + 配对题内联 “N. 词” 12 条 = 150）。
- 分版与级别：按文档顺序逐题配对徽章，P1 10（A2 10）、P2 18（A2 18）、P3 18（A2 7/B1 11）、
  P4 18（B1 18）、P5 18（B1 18）、P6 18（B2 18）、P7 12（A2 4/B1 4/B2 4）、P8 38（A2 9/B1 22/B2 7）；
  合计 **A2 48 / B1 73 / B2 29**，与 KIT 一致。
  （徽章 rect 本身只有 141 个：3 组 4 项配对题 25–28、43–46、141–144 每组共用 1 个徽章，
  各少 3 个；级别按组徽章归属：25–28 全 A2、43–46 全 B1、141–144 全 B2，已逐题核实。）
- 键值：p8 compare 已证 146 个与核心相同；4 个 keydiff 逐条核对题面，均是正确的西班牙文翻译
  （137 Ni-no-tori es el 19 de noviembre. / 138 El vino nuevo sale el 19 de noviembre. /
  139 Nominaciones: 5 de noviembre.（F1 认可的缩短）/ 140 Quien quiera ver las hojas debe
  comprobar las fechas del pronóstico y la situación actual.），并带 `Ver página N` 引用（2/3/5/6）。
- 验算抽查（全部与题面/正文/图表一致）：日期星期全核（11-07 六、11-16 一、11-19 四、11-22 日、
  11-23 一、12-01 二、11-05 四；11 月第 3 木曜日 = 19 日）；P6 图表 38+24+22+16=100，
  38−24=14、38+24=62；P4 星取与三日战绩一致（初日 大の里●/豊昇龍○/霧島○/琴櫻●/安青錦●；
  3 日目 豊昇龍●/大の里○/藤凌駕金星）；配对题 25–28、43–46、141–144 的键全对；
  P8 读写短文星期链（木 19/金 20/日 22/月 23）一致；对话题 145–149 的键全对。
- 金句 8 条：日语句子与核心版逐字相同，且逐句在正文原页真实出现（页码引用 1/1/2/3/4/7/1/2 全对）；
  西班牙文 gloss 齐全，页码引用均为单括号 `(pág. N)`，无 `((pág.`。
- VOL：VOL.4 为期号；VOL.3 仅 P4 前号注、VOL.5 仅 P4 次号预告与 P7 读者园地/预告，
  均为冻结正文/预告文字，已逐处核对上下文。
- 徽章颜色、纸色 `#fbfaf6` 每页 1×、旧 `#f7f1e2` 0×、禁色 0×、`·` 0×、刊头 196px、
  页脚 `Lucerna　SEMANARIO JAPONÉS VOL.4　Texto en japonés　Explicaciones en español`、
  页码行 `Página N de 8` 每页 1×，均与 §1.1 一致。
- 禁词扫描：政治/戦争/外交/選挙/首相/大統領/ウクライナ 等 0 命中；内容为相扑、酉の市、
  葡萄酒、红叶、流行语，无国际政治。
- 练习小节头：A 理解 / B ことば / C 数字と日付 / D ペアにしましょう 等全部冻结为日语；
  题型标签为西班牙文小写（completa、opción múltiple、cloze、relacionar、construye una frase、
  verdadero o falso、Traduce、Redacción），与 W46 ja-es 前例一致。
  （P1 1–6 题无题型标签——与核心版 P1 完全相同，属冻结版式，非缺陷。）
- 8 版印刷版逐版目视（从印刷 PDF 自行渲染，非 builder 的图）+ 网页 P1/P8 目视：
  无溢出、无重叠、无压页脚；P7 预告在页脚上方留白约 23px；P8 答案流三栏齐整，6 处两行注文
  （#14、#39、#86、#125、#133、#140）均在流内，无溢出。
- ABSTRACT.txt：西班牙文单行，308 字节，无 ASCII 双引号，含刊名、目标语、A2–B2、150 题与
  本期真实主题（Tori-no-ichi、Beaujolais、福冈相扑、30 提名、嵐山）。

### 2.3 翻译层专项（fan-out 特有）
- 讲解/界面语言确为西班牙文：页脚、页码行、Nota、Foto:、练习头、答案头、分隔符
  `— PÁGINA N —`、读者园地披露、错误诊所注文均为西班牙文。
- 221 键机制核实（因 builder 的 `map-es.json` 缺失——见 O1——改用全量 SVG 文本节点差分代替）：
  核心版独有节点共 298 个，逐类核查后全部归因于中文讲解层（含 `译注｜…`、中文 gloss、
  中文答案注文），无一条纯日文核心句丢失；es 独有节点全部为西班牙文或“日文词头＋西班牙文 gloss”
  的双语节点；es 独有 CJK 节点中无中文解释句（详见 GATE-LOG §5）。
- 中文残留扫描：`吉伊卡哇` 0×、`参考答案` 0×、`酉之市` 0×、`提名` 0×、`译注` 0×、`｜` 0×、
  `练习/阅读/翻译/注释/说明/词汇/语法/发音/例句/问题/选择/填空/意思/中文` 0×；
  唯一命中 `理解`（P2–P6 各 1×）均为冻结日语小节头 `A　理解`，非中文残留。
  保留的中文原文引用：无——本版无有意保留的中文原文引用（所有 CJK 均为日文核心文本）。
- `ちいかわ` 一律 `Chiikawa`（P7 词表、P8 答案 67/106/128），`吉伊卡哇` 全版 0×；
  `りくりゅう` 一律 romaji `ryuuryuu`（P7 gloss 含 `(pág. 7)`、P8 答案 66/77/80/105），
  核心版中文注“双人滑”“大热漫画的名字是「吉伊卡哇」”均已替换。
- P7 词表核对：`りくりゅう 双人滑　ちいかわ 吉伊卡哇`（核心）→ es 版为
  `りくりゅう pareja de patinaje artístico　ちいかわ Chiikawa`；P8 答案 80
  `ペア — ryuuryuu es la pareja Miura Riku y Kihara Ryuichi`、106
  `ちいかわ — El manga de gran éxito se llama Chiikawa`，均正确。
- F3 回归：P7 金句页码引用均为 `(pág. N)` 单括号，`((pág.` 0×。

## 3. 观察项（不计缺陷）

- O1（审计链缺口，非本版内容问题）：任务单点名的 `hidden_files/w47/scratch-fanout-ja/FANOUT-REPORT-ja.md`
  顶部审计节与关键裁定备忘**在仓内不存在**；该目录当时仅有 `.probe-stick8`、
  `build-ko-stick8-run1.log`、`ko-sha-stick8-pre.txt`，KIT §8 引用的
  `es-occlusion-run4.json`、`es-p8-run4.json`、`es-p8compare-run4.json`、
  `es-sha-run4.txt`、`es-sha-run5.txt`、`build-es-run5.log`、`map-es.json`
  全仓检索均无。因此 builder 的门记录无法复核，221 键也无法按 map 逐键核对；
  本轮全部机械门均为本人独立重跑（结果见 §2.1），翻译层改用全量文本差分核实，
  结论不依赖缺失文件。请协调员决定是否要求 builder 补交门记录与 map。
- O2（已自洽）：KIT 称 text.md 为“1349 text lines”，实测文件 1376 行、非空 1359 行；
  差额 10 行恰为文件头与 8 个 `## Page N` 标记行（1359−10=1349），内容无出入。
- O3（轻微译法不精确，键值无误）：P8 第 60 条注文 `Hōshōryū vuelve tras tres torneos perdidos`——
  原文为“3場所連続休場明け”（因伤缺席三场所后复出），`torneos perdidos` 易读作“输掉的三场所”，
  更准为 `tras perderse tres torneos` / `tras tres torneos de baja`。不影响键值 B。
- O4（轻微，键值无误）：P8 第 85 条注文 `Arashiyama: hojas desde el 12 dic. aprox.`——
  题面问的是落葉はじめ（落叶开始），注文未带“落叶/hojas que caen”限定，易与“见顷开始”混淆。
- O5（轻微，不一致）：勤労感謝の日 的西文 gloss 两处缩写不一——第 20 条 `Día de Acción de Gracias`、
  第 132 条 `Día de Acción de Gracias por el Trabajo`（后者完整）。键值无误。
- O6（ cosmetic）：P7 金句第 2 条 gloss 中 `(pág. 1)` 在行尾断行（`(pág.` / `1)` 两行），文字完整，无错。
- O7（版式，继承核心）：P2/P3/P5 中栏在 Nota 框下有较大留白，与核心版同一版式，非 fan-out 引入。
- O8（工具缺口，供后续参考）：`tools/p8.py compare` 只比对键值（字母/数字），不比对答案注文散文；
  本轮的罗马字错误（D1）因此未被机械门拦住。是否把注文散文纳入比对，由协调员/工具维护者定——
  本轮不提工具改动要求，只记录现象。

## 4. 需协调员裁定的事

- D1 修复后，按 SOP §8.4 须重渲染并**从头再做一轮全量校对**，本轮不作定稿决定。
- 修复范围建议（仅供参考，定稿决定属协调员）：P8 答案注文 6 处罗马字
  `Umi-no-umi` → `Chura-no-umi`、`Fujiryūga` → `Fujiryōga`（5 处），
  其余内容本轮已验无问题；但是否只改注文、是否同步核查同家其他语版有无同类罗马字，
  由协调员定（本轮按红线未碰其他家庭）。
