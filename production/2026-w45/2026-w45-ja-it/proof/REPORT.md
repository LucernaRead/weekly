# W45 JA×IT 独立校对报告（VOL.2）

**结论：ZERO PROBLEMS** —— 全部强制门禁独立重测通过，无阻塞项。本报告只作校对结论，不宣布上架。

- 校对对象：`files/weekly-report-w45-ja-it/`（svg×8、cards×8、双 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照：`files/weekly-report-w45-ja-core/`（W45 JA 核心）、`files/weekly-report-ja-it/`（W43 同配对版，VOL.1）
- 开工查重：开工时无 cwd 属于 ja-it 树的在途进程（唯一在途进程属 ja-ru 分版，不构成 stand down）；交付物最新 mtime 02:15:56 UTC，静默 162 秒后开工。校对全程未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录；全部重跑均在自有 scratch（`hidden_files/w45/ja-it-proof/scratch-build/`、`scratch-core/`）内完成并重定向 OUT，交付目录/核心目录只读。
- 校对前后哈希 diff：交付物 21 文件、核心 18 文件 pre/post **全部一致，无变化**（`pre-hashes.txt` vs `post-hashes.txt`、`pre-core-hashes.txt` vs `post-core-hashes.txt`）。

## 1. 交付物与 PDF 针脚（独立重测 = 构建员声称值）

- 印刷 PDF `Lucerna-VOL2-IT.pdf`：28,797,345 B，sha256 `7ced69eeded294989496b9f798df0422efffb02ac12770ffd21ca4981f8ded8b`，8 页 ✓
- 网页 PDF `Lucerna-VOL2-IT-web.pdf`：3,098,042 B（<10 MB），sha256 `c5d152d6482a72fa4ea3b4edce07bcab15e100072b5b482eb99c7bd1de0a467d`，8 页 ✓
- SVG sha256 8/8 与 KIT §9 列表逐一相符；scratch 重跑再生 SVG 8/8 与交付逐字节相同（可复现）。

## 2. 冻结门禁

- 核心基线：交付核心 18 文件与构建员 `core-baseline-pre.txt` 逐字节相符 18/18；scratch 重跑核心 build 再生 SVG 与核心交付逐字节相同。核心未动。
- `tools/freeze.py diff --strict-cjk`：8 页新增 CJK 字符均为 **0**（P1–P8：0/0/0/0/0/0/0/0）。
- 桥接词：`桥接` 在 SVG×8 + KIT + ABSTRACT + 构建代码（transform.py、content*.py）全文 **0** 处。
- 日语正文零删失：逐页核查 freeze removed 串中的日语片段——凡属正文（词头、题干、选项、例信、金句、预告、图表句）均在分版逐字重现；仅有的“消失”日语片段属于讲解层（P7 日/中双语披露行、P8 注释中日语措辞的注释句），均已按规则本地化为意大利语（见 §5、§6），不构成正文删失。
- svglib：构建树与核心树 svglib.py md5 均为 `d73e23b365676c3618d7e060b835eb4d`（canonical），未被编辑；`SEAM_SLACK = 28` 在位。

## 3. P8 #37 裸串陷阱（必查项，通过）

- 核心 `content34.py:82` 登记确为裸串 `工艺展到11月8日`（无星期后缀），键 8，题干 `展覧会は11月 ___ 日（日）までです。`（P3 卡片目视确认题干含（日））。
- 本版印刷行（P8 SVG 实测）：`37. 8 — La mostra dura fino all'8 novembre (domenica)`，键 8 ✓。
- 星期事实：`date` 核实 2026-11-08 为周日（Asia/Tokyo 与 UTC 一致）；且 P3 正文自身写明 `展覧会は11月8日（日）までです。`，(domenica) 后缀有本题内事实依据，不是照搬别题。
- 裸串残留：`工艺展到11月8日` 在分版 8 页 SVG 中 **0** 处。
- 对照：#32（核心注释本带（周日））本版同样渲染 `(domenica)`，两题一致，无矛盾。

## 4. P8 注释完整性与 keydiff（独立双路径重算）

- `tools/p8.py compare`（显式 `--core-p8` / `--edition-p8` 路径）：核心 150 条、分版 150 条，**CLEAN，missing []、extra 0、uncertain []**，keydiff 22 项 = `[1, 2, 5, 7, 8, 9, 29, 32, 37, 65, 69, 78, 101, 113, 115, 117, 118, 137, 138, 140, 146, 147]`，与声称一致。
- 印刷行逐行对照（150 条 + 8 分隔符 = 158 行）：**逐字节相同行 0**（分隔符亦全部不同：`— 第N面 —` → `— PAGINA N —`）。无未翻译注释藏身。
- 词级中文残留重扫：核心中文注释词表（工艺、对照、范文、周日、文化日是、乱扔、垃圾、要罚、展到、练习、请填、对应、答案、意思、解释、说明、提示、注意、比如、例如、因为、所以、但是、如果、已经、正在）全版 **0** 命中；分版独有元素的 CJK 串均为日语词头/题干（市場、工芸、金箔、紅葉狩り等），无中文词残留。仅有的简体字形字符在合法日语词内（学校、会社、出会う、展覧会、全国、学ぶ、中学生等）。
- 真键（第一 ` — ` 之前）独立裁定：仅 #137、#138 为真重定向（E 区 JA↔ZH → JA↔IT：`文化日是11月3日。`→`La Festa della Cultura è il 3 novembre.`；`乱扔垃圾，要罚2,000日元。`→`Se butti i rifiuti, la multa è di 2.000 yen.`）。
- keydiff 22 的无歧义归属：**2 真重定向（#137/#138）+ 1 括号规则内注释本地化（#140：真键日语句逐字相同，注释 `对照第6版（…）`→`Vedi pagina 6`）+ 19 伪影**（#1, 2, 5, 7, 8, 9, 29, 32, 37, 65, 69, 78, 101, 113, 115, 117, 118, 146, 147：工具括号法把注释尾括号剥离后留下的 `键 — 注释去括号` 与核心相异，但真键逐字相同；#37 的伪影正源于新增的 (domenica) 括号）。
- keydiff 外：**#139**（真键日语句逐字相同，注释 `对照第7版`→`Vedi pagina 7`）、**#150**（✓ 相同，器械注释 `范文见本版 H 区（167 字）`→`Testo modello nella sezione H (167 caratteri)`）均为注释本地化，非 keydiff 漏项。
- 与 JA×DE 先例 21 之差的逐项解释：DE 版 keydiff 21 项与本版 22 项的差集**恰为 #37 一项**。机制：工具 `detect_note` 无括号时用 dash 法取键（核心 #37 与 DE 无后缀版键均为 `8`，故不入 keydiff）；本版加了 (domenica) 括号后触发 paren 法，提取键变为 `8 — La mostra…` 而入 keydiff。**是计数口径差，不是内容差异**；且本版后缀有本题事实依据（§3），DE 无后缀亦正确——两者皆不阻塞。
- P8 印刷注释口径 **150**（核心 P8 本身印 150 条，非 EN 族 78）✓；P8 A–H 区齐全，E 区已重定向为 JA↔IT。

## 5. 几何门禁（全部独立重测）

- Canonical `tools/occlusion_audit.py`：selftest 6 类全触发、干净对照静默；**分版 0 flags、核心 0 flags、NEW vs core 0**。
- 同基线墨迹：P1 顶栏（左 `VOL. 2 · 第2号`、中 strapline、右日期）墨迹盒互不重叠，分版与核心均为 0 碰撞。
- ADVANCE 全页右缘扫描（canonical svglib 字体，限 1885.5）：**0 违规**；P2 配对指令 `Abbina parole e significati` 实测 advance 终点 **1880.91**（声称 1880.9 ✓）。
- 全页框线扫描（墨迹 vs 全部 rect 边 + 规则线，canonical 审计不覆盖的维度）：**0 hits**。
- P6 图表标签基线锚定墨迹覆盖（后绘 rect 法，非 getbbox 宽度法）：**max 0.000 < 30%**（22 个标签全清）。
- 行首 kinsoku（全角 NO_START 集）：**0 hits**。
- P8 / P7 末端：最终构建日志 `flow[P8-keys] ended col 3/3 y=2413 (bottom 2540)`，scratch 独立重跑复现同一数值；P8 印刷答案行最大基线 y=2530.35（第 115 条），**两者皆 <2540**；P7 预告 `P7 teaser ends 2524.12`（末基线 2490.12 + 34 行距），scratch 重跑复现，**<2540**，距页脚线有余量。最终构建日志 `build4.log` 及 scratch 重跑日志中 **FLOW OVERFLOW / HEAD TOO WIDE 0 条**。
- 注：P4/P5 正文在 y=2555.85/2551.4 各有一行，核心同位置同 y 亦有该行（冻结日语正文），非本地化溢出。

## 6. P7 门禁

- 定义句本地化 **0 处**：P7 全部非逐字元素均为讲解层（中文译文、栏目标题、诊疗所注释、金句译文、披露、页码、页脚、instr 标签 `填空`→`Completa`）或混合词头行的换行碎片（日语词头均在分版重现）；词框日语定义句逐字冻结。
- 金句：8 句在去空白全版拼接中**每句恰 2×**（核心与分版一致）；P7 句式框日语句 8 句与核心逐字相同；页签顺序 **p.1, p.1, p.2, p.2, p.3, p.4, p.5, p.6** = 核心（第N面→p.N）。
- 词框 gloss 仅本地化（见 §7）。

## 7. gloss 渲染切分（独立重测）

- 方法：按渲染块拼接（同 x、同字号、行距续行合并）后按 `·` 切分，逐项计数。
- **核心 = 分版 = 39，总分布 P1 4 / P2 9 / P3 8 / P4 7 / P5 7 / P6 4**，与声称一致；各页词头逐字相同，仅 gloss 本地化（例 P1：祝日 giorno festivo · 見頃 momento migliore per ammirare · 暦 calendario · お届けします per portarvi.）。
- 源文件分组 13+15+11+0 未被用作渲染结论（仅作口径区分记录）。

## 8. 读者来信角（P7，逐字摘录裁定）

- 日语例信逐字冻结（4 行，含结尾 `— 読者の手紙の例`），零编造；仅 y 坐标因上方意大利语栏位变长而下移。
- 意大利语披露（P7 披露段，原文摘录）：
  > “Esempio della redazione, non una lettera vera. Entro la scadenza non sono arrivate vere lettere né i migliori testi di pagina 8; entrambi appariranno nel VOL.3. Scrivici in giapponese!”
- 裁定：含 3 事实 ✓（示例非真信；无真信到达；无最佳 P8 作文到达）+ 明确祈使征集 ✓（`Scrivici in giapponese!`）+ VOL.3 承诺 ✓（`appariranno nel VOL.3`）。核心的日/中双语披露行被**替换而非叠加**（符合 JA×EN 协调裁定模式）；VOL.3 预告行（`来週 · Prossimo numero (VOL.3)` + 日语预告正文逐字 = 核心）为内容预告，**不计作征集**。未为凑双语编造额外目标语披露句；本族披露结构以 JA 核心为准，裁定通过。

## 9. 家具三方对照（W45 核心 / W43 同配对 / 本版；W43 优先于 README #20 泛化）

| 项目 | W45 核心 | W43 JA×IT（实测） | 本版（实测） | 裁定 |
|---|---|---|---|---|
| 刊头 wordmark y | 262 | 248 | 248 | W43 优先 ✓ |
| 刊头刊名 | Lucerna（无冠词） | Lucerna（无冠词） | Lucerna（无冠词） | ✓（日语无冠词，SOP） |
| 版次行 y | 330 | 316 | 316 | W43 ✓ |
| badge 串 | —（副标题槽） | (975, 356) 19pt `TESTI IN GIAPPONESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI` | 串逐字相同，槽 (975, 356) 19pt middle 锚点相同 | ✓（颜色见观察项 O1） |
| strapline y | 372 | 390 | 390 | W43 ✓ |
| 双规则 y | 392 / 401 | 406 / 413 | 406 / 413 | W43 ✓ |
| 深色带 y | 424 | 424 | 424（65, 424, 1820×118, #2c2822 三方同） | ✓ |
| 顶栏 | 每周一期 | Ogni settimana | Ogni settimana | ✓ |
| 页脚 | 日语周报 VOL.2 | SETTIMANALE GIAPPONESE VOL.1 | SETTIMANALE GIAPPONESE VOL.2（VOL 号正确递进） | ✓ |
| 页码行 | 第 N 版 / 共 8 版 | Pagina N di 8 | Pagina N di 8 | ✓ |
| gloss 前缀 | 译注｜ | Nota — | Nota — | ✓ |
| P8 分隔符 | — 第N面 — | W43 VOL.1 P8 无 PAGINA 形分隔符（版式不同） | — PAGINA N —（核心分隔符的意大利语本地化） | ✓ 无冲突 |
| P1 数字框标题 | 数字で見る今週 · 数字看本周 | 数字で見る今週 · In numeri（同坐标 y=1013.47） | 数字で見る今週 · In numeri（同坐标） | 缩短仅删意大利语 `La settimana` 修饰，数字行（3/7/9/1.5）与核心逐字相同，**无内容损失** ✓ |
| P4 日程框标题 | 日本シリーズの日程 · 大赛日程 | 日本シリーズの日程 · Calendario | 日本シリーズの日程 · Calendario | W43 缩短形 ✓ |
| P7 句式框标题 | 今週のフレーム · 本周句式 | 今週のフレーム · La frase tipo（1473, 1115.12） | 今週のフレーム · La frase tipo（同坐标） | W43 ✓ |
| P2 配对指令 | 把词和释义配对 | （W43 P2 为不同题目，不适用照搬） | `Abbina parole e significati`（advance 1880.91 < 1885.5）；P8 F 区同句 | 新实测缩短，仅删冠词/介词，语义不变 ✓ |
| P4 栏目标题左 | スポーツ · 体育 | スポーツ · 体育 | スポーツ · 体育（未改） | ✓ JA 族惯例 |

## 10. 计数 / 范文 / 图片 / 摘要

- 登记展开（scratch 独立重跑 `run.py`，OUT 已重定向）：**150 题连续**，级别 **A2 46 / B1 75 / B2 29**，页分布 **10 / 18 / 18 / 18 / 18 / 18 / 12 / 38**，类型 completamento 50 / scelta multipla 51 / abbinamento 12 / costruzione di frasi 8 / vero-falso 11 / cloze 13 / traduzione 4 / scrittura 1；核心 scratch 重跑同为 150 / 46 / 75 / 29 / 同页分布。**= 核心** ✓
- 范文《私の11月の週末》：源字符串与核心**逐字相同，167 字**（源计数法去空格后 167；P8 渲染 `例：` + 范文拼接 170 字 = 3 + 167，两版一致）；P8 #150 注释 (167 caratteri) 与之相符。
- 图片：4 张 payload（长度 + md5 前缀）逐页 = 核心——P1 红叶、P3 歌川广重三代、P4 球场、P5 南瓜；P2/P6/P7/P8 无图 = 核心；credit 均在页内且与核心逐字相同（P1 Poliphilo CC0、P3 歌川広重（三代）PD、P4 Syced CC0、P5 Petr Kratochvil PD，均为 Commons API Artist 字段口径）。
- ABSTRACT：意大利语单行（1 行 + 末尾换行）、**ASCII 双引号 0**、真实主题关键词（Festa della Cultura、Naruko Gorge、Kobe luminarie、Settimana della Lettura、立冬、Japan Series、150 esercizi、VOL.2）+ 学习者检索短语 `imparare il giapponese leggendo` ✓。

## 11. 全 8 卡目视

P1–P8 逐张目视：无溢出、无重叠、无裁切标签、无错位框。P1 刊头/badge/数字框/红叶图；P2 配对指令；P3 题干 37 与广重版画；P4 Calendario 框与球场图；P5 南瓜图；P6 图表标签全清于条外；P7 诊疗所 4 条、La frase tipo 框、读者来信角披露与征集句、8 金句页签、VOL.3 预告带；P8 A–H 区、E 区意译、答案流收尾于页脚线上方。P2/P4/P5/P6 特色栏空白与核心同 pattern（已披露）；P7 B1 gloss 行中词换行（`紅葉 | 狩り`）为 CJK 逐字换行机制，栏位无碰撞（occlusion 0）。**目视 0 问题**。

## 12. 非阻塞观察（纸面正确，仅记录，不改纸面）

- **O1 徽章颜色**：badge 串、槽、字号、锚点与 W43 逐字相同，但 fill 颜色不同——W43 为砖红 `#a4553a`，本版为深橄榄 `#3e4c2a`。按 JA×FR 校对先例，颜色族内各版不同本身不阻塞；KIT 未声称颜色一致（仅称“相同串 + 槽”，属实），故不构成 KIT 错误，仅此记录。
- **O2 KIT §6 措辞**：KIT 称 “P8 answer-flow end y=2413”，该 2413 实为构建日志 `flow[P8-keys]` 的游标终点；印刷答案行最大基线为 y=2530.35（第 115 条）。两者皆 <2540，纸面正确；此处仅作口径澄清，不阻塞、不改纸面。
- **O3**：KIT 其余数值经核查均与独立实测相符（PDF 针脚、SVG sha、gloss 39、ADVANCE 1880.9、P7 预告 2524.12、P6 覆盖 0.0、freeze 0、P8 CLEAN/keydiff 22），未发现其他 KIT 文字错误。

## 证据文件

- `hidden_files/w45/ja-it-proof/REPORT.md`（本报告）
- `hidden_files/w45/ja-it-proof/pre-hashes.txt`、`post-hashes.txt`（交付物校对前后哈希，diff 为空）
- `hidden_files/w45/ja-it-proof/pre-core-hashes.txt`、`post-core-hashes.txt`（核心校对前后哈希，diff 为空）
- `hidden_files/w45/ja-it-proof/freeze.json`（strict-CJK diff：新增 0）
- `hidden_files/w45/ja-it-proof/p8.json`、`p8-printed.json`（P8 双路径对照与 158 行印刷行对照）
- `hidden_files/w45/ja-it-proof/occlusion.json`、`occlusion-core.json`（canonical 审计：分版 0 / 核心 0 / NEW 0）
- `hidden_files/w45/ja-it-proof/geom2.py`、`extract.py`（ADVANCE/框线/P6/kinsoku 独立扫描脚本）
- `hidden_files/w45/ja-it-proof/scratch-build/`、`scratch-core/`（OUT 重定向后的独立重跑树；再生 SVG 与交付逐字节相同）
- `hidden_files/w45/ja-it-proof/scratch-run.log`（分版重跑日志：P7 teaser 2524.12、P8-keys 2413、无 OVERFLOW）

**再次声明：本报告结论为 ZERO PROBLEMS；是否上架由主线裁定，本校对员不宣布上架。**
