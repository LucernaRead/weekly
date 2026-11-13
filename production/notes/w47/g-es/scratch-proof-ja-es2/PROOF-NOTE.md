# PROOF-NOTE — 2026-W47 ja-es 第二轮独立校对（叶子）

- 校对员：叶子（独立第二轮；与 ja-es builder、ja-es fix1 builder、ja 核心 builder、ja-es 第一轮复校员不同人）
- 对象：`production/2026-w47/fanout-ja/2026-w47-ja-es/`（未入仓，工作树 untracked）
- 日期：2026-11-11（UTC 约 09:00–10:00）
- 结论：**(a) 零问题，可定稿**（按 SOP §8.4，从头全量复校一整轮零问题）。定稿决定属协调员，本轮只报事实。
- 本人只检查、不改任何源码/成品：构建目录 8 个 SVG 的 SHA 在校对开始与结束时逐一核对，全部未变（`sha256sum -c` 全 OK）；构建重跑在本人 scratch 区的完整副本里做的（见 GATE-LOG）。

## 0. 身份核对（先核身份，双 PDF 均符，以 KIT 登记为准）

| 文件 | 字节 | SHA-256（完整，自行算出） |
|---|---|---|
| 印刷 PDF `Lucerna-VOL4-JA-ES.pdf` | 29,102,102 | `9947b70c00a378c912ad7cffd198fd19a234ca3d6a3598589f647c3eaff0fce7` |
| 网页 PDF `Lucerna-VOL4-JA-ES-web.pdf` | 4,482,721 | `49665374de81dd2a2ee7dad1b91396b22b69b2e64f5a038d55f03b5246a99550` |

与 KIT §8 fix-1 登记的字节数与完整 SHA 逐字一致；两 PDF 均为 8 页；网页版 < 7 MB。
探针双通后才动手（`git hash-object -w` 成功，`da0c4eb8…`；`scratch-proof-ja-es2/probe.txt` 真实写入成功）。

## 1. D1 回归（第一轮缺陷，6 处 P8 答案注文）—— 已改对，无内容残留

- 6 处逐处核实（py 源码 + P8 SVG 文本节点 + text.md + 印刷 P8 高清裁图四重一致）：
  - key 48：`Chura-no-umi perdió contra Hōshōryū el día 1` ✓
  - key 49：`Fujiryōga venció a Hōshōryū el día 3` ✓
  - key 54：`El kinboshi de Fujiryōga: 11.º torneo desde su debut` ✓
  - key 63：`Fujiryōga ganó un kinboshi el día 3` ✓
  - key 111：`El kinboshi de Fujiryōga: 11.º torneo desde su debut` ✓
  - key 116：`Hōshōryū perdió contra Fujiryōga el día 3` ✓
- 读音独立核实（公开来源，本轮自查，非采信复校/返修笔记）：
  - 美ノ海義久 = ちゅらのうみ：デイリー 2026-10-27「美ノ海義久（ちゅらのうみ・よしひさ）」。
  - 藤凌駕雅治 = ふじりょうが：スポーツ報知 2026-11-11「藤凌駕 雅治（ふじりょうが・まさはる）」；sumo-guide.com 同。
- 改动范围精确性（强证据）：以第一轮复校员留下的改前 P8 SVG 副本（`scratch-proof-ja-es1/rebuild/svg/p8-tesuto.svg`，hash cb2813a7…）为基准，新旧 P8 文本节点逐行 diff **仅此 6 行**；P1–P7 文本节点与改前副本**逐字相同**（另见 §2.1：P1–P7 SVG hash 与第一轮记录逐一相同，仅 P8 由 cb2813a7… 变为 25b95108…）。
- 错拼全版排查：内容文件（py + SVG 文本节点 + text.md + ABSTRACT.txt）中 `Fujiryūga` / `Umi-no-umi` 均为 **0**；正确拼写 `Fujiryōga` 5×、`Chura-no-umi` 1×。
- 其余 P8 注文人名逐条核对：Ōnosato、Hōshōryū、Yoshinofuji、Chura-no-umi、Fujiryōga、Miura Riku、Kihara Ryuichi、Miyajima、Shōsetsu、ryuuryuu、Chiikawa、Ni-no-tori / Tori-no-ichi / Ichi-no-tori / Asakusa / Arashiyama / Kioto / Monte Takao / Weathernews / Beaujolais Nouveau / Hanshin Umeda —— 全部正确，无其他人名错误。
- 关于观察项 O1（见 §3）：WEEKLY-KIT.md（§11 F4，4 行）与 EDITION-RECORD.md（Fix-1 节，1 行）仍含有旧拼写，但全部是修复记录中引用的“改前值”，属记述性引用，非读者可见内容残留，见 O1 说明。

## 2. 已核对通过的项目（事实摘要）

### 2.1 机械门（全部自跑，见 GATE-LOG.md）
- run.py（本人 scratch 副本，`tools/venv/bin/python`，Python 3.12.3 / Pillow 13.0.0，与构建相同解释器）：exit 0，FLOW OVERFLOW / HEAD TOO WIDE 计 0；8/8 SVG 与原构建逐字节相同；registry 与 KIT 一致（TOTAL 150；A2 48 / B1 73 / B2 29；分版 10/18/18/18/18/18/12/38；题型 completa 50、opción múltiple 51、relacionar 12、construye una frase 8、verdadero o falso 11、cloze 13、Traduce 4、Redacción 1；范文 154 字，本人另从 text.md 实数 154 字，一致）。
- occlusion：自检 6 类全触发、干净对照静默；实跑 **0 flags**。
- p8 extract：noted set **150/150**（`--total 150`）。
- p8 compare（vs core-ja P8）：status **CLEAN**，missing=[]，extra=0，uncertain=[]，keydiff=**[137, 138, 139, 140]**，与预期完全一致；其余 146 个键值逐字相同。
- print/web 文字层：`pdftotext -layout` 各 102,065 字节，**逐字节相同**；plain `pdftotext` 各 47,036 字节，逐字节相同（与 EDITION-RECORD 登记的 47,036 B 一致）。
- U+2019：8 个 SVG 总数 **0**；text.md 0；content*.py 0。
- P8 字号（PyMuPDF 测印刷 PDF 第 8 页）：最小 **9.98pt ≥ 9.75pt**；次档 10.35pt（题干，79 个 span），与 KIT 登记的 9.975pt / 10.35pt 一致。
- §1.1 grep：`·` 0×；纸色 `#fbfaf6` 合计 8（每页 1×）；旧 `#f7f1e2` 0×；刊头 196px；页码行 `Página N de 8` 每页 1×；页脚 `Lucerna　SEMANARIO JAPONÉS VOL.4　Texto en japonés　Explicaciones en español` 每页 1×。

### 2.2 150 题逐题验算（本轮从头重验，非采信第一轮）
- 题号 1–150 连续无缺重（text.md 行首 `N.` 集合恰为 1–150；P8 答案区 150 条逐条在列）。
- 分版与级别（按文档顺序逐题配对徽章）：P1 10（A2 10）、P2 18（A2 18）、P3 18（A2 7/B1 11）、P4 18（B1 18）、P5 18（B1 18）、P6 18（B2 18）、P7 12（A2 4/B1 4/B2 4）、P8 38（A2 9/B1 22/B2 7）；合计 **A2 48 / B1 73 / B2 29**，与 KIT 一致。徽章 rect 共 141 个：3 组 4 项配对题 25–28、43–46、141–144 每组共用 1 个徽章（25–28 全 A2、43–46 全 B1、141–144 全 B2）；P1 另有 4 个目录栏级别标注（2面 A2、4面 B1、5面 B1、6面 B2），非练习徽章，已核对与各版级别一致。
- 键值：150 个答案逐条对题面/正文/图表验算通过。抽查要点：日期星期全核（11-07 六、11-16 一、11-19 四、11-22 日、11-23 一、12-01 二、11-05 四；11 月第 3 木曜日 = 19 日）；P6 图表 38+24+22+16=100，38−24=14、38+24=62，柱长比例与数值一致，标注为练习数据；P4 星取与三日战绩一致（初日 大の里●/豊昇龍○/霧島○/琴櫻●/安青錦●；3 日目 豊昇龍●/大の里○/藤凌駕金星；大関 3 人中 2 人初日败）；配对题 25–28、43–46、141–144 的键全对；P8 读写短文星期链（木 19/金 20/日 22/月 23）一致；对话题 145–149 的键全对；E 组 137–140 逐条对题面核实为正确西班牙文翻译（137 Ni-no-tori es el 19 de noviembre. / 138 El vino nuevo sale el 19 de noviembre. / 139 Nominaciones: 5 de noviembre. / 140 Quien quiera ver las hojas debe comprobar las fechas del pronóstico y la situación actual.），并带 `Ver página N` 引用（2/3/5/6，全对）。
- 金句 8 条：日语句子与核心版逐字相同，且逐句在正文原页真实出现（页码引用 1/1/2/3/4/7/1/2 全对）；西班牙文 gloss 齐全，页码引用均为单括号 `(pág. N)`，`((pág.` 0×。
- VOL：VOL.4 为期号；VOL.3 仅 P4 前号注 1 处、VOL.5 仅 P4 次号预告 1 处 + P7 3 处（读者园地披露 2 处、预告条 1 处），均为冻结正文/预告文字，已逐处核对上下文。
- 禁词扫描：战争/外交/選挙/首相/大統領/ウクライナ/政治 0 命中；内容为相扑、酉の市、葡萄酒、红叶、流行语，无国际政治。
- 8 版印刷版逐版目视（从印刷 PDF 自行渲染，非 builder 的图）+ 网页 P1/P8 目视：无溢出、无重叠、无压页脚；P7 预告在页脚上方留白约 23px；P8 答案流三栏齐整，6 处两行注文（#14、#39、#86、#125、#133、#140）均在流内，无溢出；网页 P1/P8 与印刷版视觉一致。
- ABSTRACT.txt：西班牙文单行，308 字节，无 ASCII 双引号，含刊名、目标语、A2–B2、150 题与本期真实主题（Tori-no-ichi、Beaujolais、福冈相扑、30 提名、嵐山）。

### 2.3 翻译层专项（fan-out 特有）
- 讲解/界面语言确为西班牙文：页脚、页码行、Nota、Foto:、练习头、答案头、分隔符 `— PÁGINA N —`、读者园地披露、错误诊所注文均为西班牙文。
- 核心差分（core-ja vs 本版，SVG 文本节点全量）：核心独有节点全部含中文讲解段，唯一非 CJK 节点为 P3 图注中文行尾折行残片 `Commons）`，对应 es 版 `Foto: Alainauzas — dominio público (Wikimedia Commons)` 已完整改写，无一条纯日文核心句丢失；es 独有节点全部为西班牙文或“日文词头＋西班牙文 gloss”的双语节点，其中含 CJK 且无假名的节点逐一核查均为日文单词头/冻结小节头（熊手、金星、解禁、小雪、屋台、千秋楽、見頃、収穫、一番太鼓、京都、練習、来週、〜勝〜敗、〜番目、「昨日」等）配西班牙文 gloss，无中文解释句。
- 中文残留扫描：`吉伊卡哇` 0×、`参考答案` 0×、`酉之市` 0×、`提名` 0×、`译注` 0×、`｜` 0×、`练习/阅读/翻译/注释/说明/词汇/语法/发音/例句/问题/选择/填空/意思/中文` 0×；唯一命中 `理解`（P2–P6 各 1×）均为冻结日语小节头 `A　理解`，非中文残留。
- 练习小节头全部冻结为日语（A 理解 / B ことば / C 数字と日付 / D ペアにしましょう / 文を作りましょう / 正しい・正しくない / 読んで答えましょう / 文を完成しましょう 等）；题型标签为西班牙文小写（completa、opción múltiple、cloze、relacionar、construye una frase、verdadero o falso、Traduce、Redacción），与 W46 ja-es 前例一致。
- `ちいかわ` 一律 `Chiikawa`（P7 词表、P8 答案 67/106/128），`吉伊卡哇` 全版 0×；`りくりゅう` 一律 romaji `ryuuryuu`（P7 gloss、P8 答案 66/77/80/105）。
- text.md 与 SVG 文本节点逐行比对：1349 个 SVG 文本节点全在 text.md 中；text.md 仅 1 行不在 SVG 中，为文件头 `Week: 2026-W47 (16–22 Nov 2026)`。text.md 1377 行、非空 1359 行；KIT“1349 text lines”= 非空行减标题、Week 行与 8 个 `## Page N` 标记行（1359−10=1349），自洽。

## 3. 观察项（不计缺陷）

- O1（grep 口径说明，非内容问题）：任务单“全版 grep `Fujiryūga`/`Umi-no-umi` 须为 0”——严格按全版 grep，WEEKLY-KIT.md §11 F4（4 行）与 EDITION-RECORD.md Fix-1 节（1 行）仍含旧拼写，但全部是修复记录里引用的“改前值”（`Umi-no-umi → Chura-no-umi` 形式），不是正文/注文/成品残留；读者可见的全部交付物（py、SVG、text.md、ABSTRACT、双 PDF）均为 0。删掉这些引用会抹掉修复审计轨迹，本轮不列缺陷，请协调员裁定是否要把记录改写为不含旧拼写的表述。
- O2（第一轮 O1 更新）：第一轮称缺失的 builder 门记录现已部分补齐——`hidden_files/w47/scratch-fanout-ja/` 内已有 `FANOUT-REPORT-ja.md` 与 es 门记录（`es-occlusion-stick8.json`、`es-p8-stick8.json`、`es-p8compare-stick8.json`、`es-print.txt`、`es-web.txt`）；`map-es.json` 仍无。本轮全部机械门均为本人独立重跑，结论不依赖这些文件。
- O3（第一轮 O3，仍在，键值无误）：P8 第 60 条注文 `Hōshōryū vuelve tras tres torneos perdidos`——原文为“3場所連続休場明け”（因伤缺席三场所后复出），`torneos perdidos` 易读作“输掉的三场所”，更准为 `tras perderse tres torneos` / `tras tres torneos de baja`。不影响键值 B。
- O4（第一轮 O4，仍在，键值无误）：P8 第 85 条注文 `Arashiyama: hojas desde el 12 dic. aprox.`——题面问的是落葉はじめ（落叶开始），注文未带“落叶/hojas que caen”限定，易与“见顷开始”混淆。
- O5（第一轮 O5，仍在，不一致）：勤労感謝の日 的西文 gloss 两处缩写不一——第 20 条 `Día de Acción de Gracias`、第 132 条 `Día de Acción de Gracias por el Trabajo`（后者完整）。键值无误。
- O6（第一轮 O6，仍在，cosmetic）：P7 金句第 2 条 gloss 中 `(pág. 1)` 在行尾断行（`(pág.` / `1)` 两行），文字完整，无错。
- O7（第一轮 O7，仍在，版式，继承核心）：P2/P3/P5 中栏在 Nota 框下有较大留白，与核心版同一版式，非 fan-out 引入。
- O8（第一轮 O8，仍在，工具缺口，供后续参考）：`tools/p8.py compare` 只比对键值（字母/数字），不比对答案注文散文；D1 类罗马字错误因此未被机械门拦住，本轮的 6 处修正全靠人工核对。是否把注文散文纳入比对，由协调员/工具维护者定——本轮不提工具改动要求，只记录现象。
- O9（新增，轻微，说明）：text.md 总行数 1377 行，第一轮为 1376 行——差 1 行为重导时多出的文末空行；内容行 1349 行与 KIT 一致，无出入。text.md 字节 46,684（改前 46,682）：+2 字节恰为 `Umi-no-umi`（10 字符）→ `Chura-no-umi`（12 字符）一处之差，`Fujiryōga`/`Fujiryūga` 等长，与“仅改 6 处注文”一致。
- O10（上游提示，非本版问题，转述 fix1 已报）：同错仍见于 core-ja KIT §3（L83–88）及 de/en/fr/it/nl/pt 六个同家拉丁版，ko/ru/zh-tw 不受影响；本任务红线内只修 ja-es，其余只报告、不碰。请协调员定夺。

## 4. 需协调员裁定的事

- 本轮结论为 (a) 零问题，可定稿；定稿与入仓决定属协调员。
- O1 的记录引用写法（是否要把 KIT/EDITION-RECORD 里的旧拼写“改前值”改写掉）请协调员裁定。
- O10 上游同错（core-ja KIT 与六个同家拉丁版）是否排期同修，请协调员裁定。
