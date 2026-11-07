# 独立校对报告 — Lucerna Weekly W45 JA×NL（日语×荷兰语）

**结论：ZERO PROBLEMS**（无阻塞项；文末 4 条非阻塞观察不影响纸面）

- 校对对象：`files/weekly-report-w45-ja-nl/`（svg×8、cards×8、双 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照：W45 日语核心 `files/weekly-report-w45-ja-core/`（只读）、W43 同配对 `files/weekly-report-ja-nl/`（VOL.1 已交付版 SVG，只读）
- 校对员权限边界遵守：只校对、不改源码；未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录、未清理共享 scratch；构建树重跑全部在自有 scratch 内完成（见 §10），未在原地运行任何写回交付/核心目录的脚本；未派生任何下级代理。
- 证据文件均在本目录：`pre-hashes.txt`、`post-hashes.txt`、`core-hashes-before.txt`、`core-hashes-after.txt`、`freeze-diff-mine.json`、`p8-mine.json`、`occlusion-mine.json`、`analyze.json`、`reg-run.log`，scratch 见 `scratch/`（build-copy、repro1、repro2、reg、regsvg）。

## 0. 开工查重

- 在途进程逐进程查 cwd：唯一在途构建进程属 JA×KO（cwd 为 `hidden_files/weekly-report-w45-ja-ko-build`），与 ja-nl 树无关，**不构成 stand down**。
- ja-nl 交付物最后 mtime 为 WEEKLY-KIT.md 2026-10-28 02:26:19 UTC；开工复查时已静默 >120 秒，且复查后无 ja-nl 进程、无 mtime 变化，**安全开工**。
- 校对前后交付物哈希 diff 为空、核心 SVG 哈希 diff 为空（§11）。

## 1. 钉点与核心基线（全部独立重测，构建员声称值仅作比对）

- 印刷 PDF `Lucerna-VOL2-NL.pdf`：28,025,932 B，8 页，sha256 `1dd58de4cbc9a42756c59692b616c13ce440f8458c0300ec48556206e4aa4aba`——与声称值一致。
- 网页 PDF `Lucerna-VOL2-NL-web.pdf`：3,105,024 B，8 页，sha256 `464129c079e704334e450147813982dacc2a31ad9afd18b08c18042de5ff3aa0`——与声称值一致。
- 核心基线：开工前核心 SVG 哈希与构建树 `sha256-core-before.txt` 所载 8 个值逐字节一致（仅路径前缀不同），即核心 8/8 未被改动。
- 核心固定数复核（从核心实测）：VOL.2；刊头 `Lucerna` 无冠词；P8 印刷笔记口径 150 条（canonical p8 核心侧 150）；svglib canonical md5 `d73e23b365676c3618d7e060b835eb4d`（NL 构建树与核心构建树同值，未被编辑）；`SEAM_SLACK=28`；kinsoku `NO_START` 取自 svglib wrap 原文。

## 2. 冻结门禁

- canonical `tools/freeze.py diff`（独立重跑，`freeze-diff-mine.json`）：8 页 strict-CJK 新增字符数全部为 **0**。
- CJK 总量核心→本版：P1 1406→1275、P2 1312→1161、P3 1172→1051、P4 1263→1169、P5 1247→1132、P6 1186→1101、P7 1676→1306、P8 2721→1445——与 KIT §6 一致，减少量均为被移除的中文讲解层。
- 日语正文零删失（源码级佐证）：核心构建与本版构建 content12/34/56/7/8 全量 diff 中，文章段落（`f.para` 正文）无一改动；改动行仅为讲解层（注释、指令词、家具半句、gloss、"En jij?" 提示、P8 分隔符、披露行）。P7 词框见 §7。
- 桥接词扫描：`桥接`二字在以下范围均为 **0 命中**：本版 SVG×8、构建代码（transform.py、gen_nl.py、content12/34/56/7/8.py、bslib4.py、render.py、run.py、svglib.py、transform-en-reference.py）、WEEKLY-KIT.md、ABSTRACT.txt。

## 3. JA 族 P8 #37 裸串陷阱（必查项，裁定：无后缀正确）

- 陷阱源头证实：核心构建 `content34.py:82` 登记确为裸串 `工艺展到11月8日`（无星期后缀），题干为 P3 填空题，键为 `8`：
  - 核心原文：`e.ex("A2", "完成句子", "8", "工艺展到11月8日", "展覧会は11月 ___ 日（日）までです。", instr="填空", …)`。
- 本版 P8 印刷行（p8-tesuto.svg，x=65，y=2501.12，答案流内）：`37. 8 — De tentoonstelling loopt tot 8 november`——**无后缀**，与裸串登记一致。
- 对照串区分正确：#32 的带后缀登记 `工艺展到11月8日（周日）` 在本版印为 `32. B — De tentoonstelling loopt tot 8 november (zondag)`——两题登记串被正确区分，未混同。
- 星期事实：2026-11-08 为周日（`date -d 2026-11-08`，America/Toronto 与 UTC 一致）；P3 原文 `展覧会は11月 ___ 日（日）までです。` 在核心与本版 P3 均逐字存在——题干本身已向学习者给出"（日）"，答案注释无需重复星期。
- 裸串残留：中文裸串 `工艺展到11月8日` 在本版 8 页 SVG 中为 **0 页**（仅核心 P8 存在，属核心原文）；本版无任何中文裸串残留。
- 裁定：#37 无后缀处理**正确**，符合本题登记事实与 JA×DE（无后缀且正确）的先例；若强加 `(zondag)` 反而会把 #37 与 #32 的两条不同登记注释混同，属于过度翻译。**不阻塞。**

## 4. P8 注释完整性（重点核对项：两声称的调和验证）

构建员两声称表面张力："150 条答案注释全部本地化" vs "P8 相同行 108 条逐条裁定全为冻结日语"。独立调和结果：**两者同时成立，无矛盾**，理由如下：

- 相同行 108 条的构成（核心 P8 文本元素集 ∩ 本版 P8 文本元素集，`analyze.json` 全量列出）：全部为非注释元素——题号裸行（如 `113.`…`150.`）、日语题干/选项行、区标题（`A · 週のクロニクル` … `H · 書いてみましょう`）、级别徽标（`A2/B1/B2`）、数字与范文片段。逐条筛查：
  - 含 ` — ` 的完整注释行：**0 条**相同；
  - 含中文注释标记（`对照/周二/周一/周六/周日`）的行：**0 条**；
  - 含拉丁字母的相同行均为日语题干/选项/区标题/范文片段（如 `2連勝で始めたチームの優勝率は？ A. 73% · B. 24% · C. 100%`），无一条中文讲解层。
- 答案行级同一性（canonical p8 提取的全段比较）：核心与本版**完全相同的完整答案段为 0 条**——即 150 条答案注释无一条原样残留，全部已本地化。
- 词级中文残留重扫（非仅字符扫描）：本版全部 CJK 连续串（长度 ≥2）中不存在于核心全文者为 **0 条**——共享汉字中文词穿透亦无。
- 结论：108 条相同行无一条是中文讲解层穿透；"150 条全部本地化"与"108 条全为冻结日语"调和成立。**无穿透缺陷。**

## 5. P8 比较（显式双路径，逐项裁定）

- canonical `tools/p8.py compare` 独立重跑（`p8-mine.json`）：**CLEAN，150 = 150，missing []、extra []、uncertain []**，keydiff 与构建员列表逐项一致：
  `[1, 2, 5, 7, 8, 9, 29, 32, 65, 69, 78, 101, 113, 115, 117, 118, 137, 138, 140, 146, 147]`（21 项）。
- 真键头比较（段首 ` — ` 之前部分，独立于提取器的键定义）：
  - 头相等 19 项：#1(3)、#2(9)、#5(7)、#7(B)、#8(C)、#9(B)、#29(A)、#32(B)、#65(A)、#69(C)、#78(○)、#101(27)、#113(A)、#115(A)、#117(B)、#118(A)、#140（日语句）、#146(A)、#147(A)——差异只在注释段本地化，键本身逐字 = 核心。
  - 头不等仅 2 项（真重定向，合法）：#137（核心 `文化日是11月3日。` → 本版 `Cultuurdag is op 3 november.`）、#138（核心 `乱扔垃圾，要罚2,000日元。` → 本版 `Wie afval op straat gooit, krijgt een boete van 2.000 yen.`）。
- #139 归属（在 keydiff 外，正确）：键段逐字 = 核心 `読書週間は10月27日から始まります。`，题干已重定向为荷兰语提示 `De Leesweek begint op 27 oktober. → ___`，仅 cross-ref 注释本地化（`— 对照第7版` → `— Zie pagina 7`），故不入 keydiff。
- #140 归属（在 keydiff 内，但键逐字 = 核心）：真键头 `神戸の紅葉のライトアップを見に行きたいです。` 两边一致；提取器键差异源于本地化的 cross-ref（`— 对照第6版` → `— Zie pagina 6`）落在括号注释边界之前，属注释差异类，非键差异。
- #5 表面键差异（核实说明）：P8 SVG 中确有一行续行元素 `5.00 uur`（x=527，y=2222.77，系 #66 注释 `…van 18.00 tot 5.00 uur` 的换行续行），朴素的"行首数字即题号"解析会误认；但 canonical lines 法提取的 #5 段干净，键 `7` 与核心 `5. 7 — 神户灯光秀从7日（周六）开始` 一致（本版：`5. 7 — De verlichting in Kobe begint op 7 november (zaterdag)`）。#5 入 keydiff 的原因是注释本地化，非续行误认。
- 计数表述核实：**21 = 2 真重定向（#137/#138）+ 19 注释差异/伪影**；提示本地化共 2 项（#139 在外、#140 在内），无双重计数。本版 keydiff 构成（2+19）与 ja-de（2+1+18）、ja-pt（17+2+2）各不相同属实——已逐项核实本版构成，非只核总数。**无无法归类项，不阻塞。**

## 6. 几何门禁

- canonical `tools/occlusion_audit.py`（自检 6 类全部触发，`occlusion-mine.json`）：本版 **0 告警**、核心 **0 告警**、NEW（本版相对核心新增）**0**。
- 同基线墨迹碰撞 0（NEW=0 的直接含义）。
- ADVANCE 法全页右缘扫描（限 1885.5，跳过 Unifraktur 刊头字）：**0 违规**。
- 全页框线扫描（canonical 审计不抓框线压字，独立补扫）：**0 命中**。
- P6 图表标签基线锚定墨迹覆盖（PIL 真实墨迹盒 vs 后绘不透明矩形，**未用 getbbox 法**）：MAX **0.000**（门 <0.30）。
- 行首 kinsoku：**0 命中**（NO_START 16 字集取自 svglib.py wrap 原文）。
- P8 答案流末端：#150 元素基线 **2530.73**（距 2540 余 9.27px）；墨迹底口径：同串 PIL `anchor='ls'` bbox 底 = **2534.73**（余 5.27px）；本页最紧墨迹为分隔行 `— Pagina 8 —` 墨迹底 2536.10（余 3.90px）——三口径均 <2540，**通过，但余量须明示**：基线口径余 9.27px、墨迹口径余 5.27px。
- P7 预告末端：末行基线 2490.12，墨迹底 2494.12（余 45.88px）；构建员声称的 2524.12 经核实为**预告带底边**（带 rect y=2406.12，h=118，底 = 2524.12，余 15.88px），非末行基线——口径已澄清，两口径均 <2540。
- 构建日志：scratch 登记重跑日志（`reg-run.log`）零 `!!` 告警，无 FLOW OVERFLOW、无 HEAD TOO WIDE。说明：日志中 `flow[P8-keys] ended col 3/3 y=2547 (bottom 2540)` 为游标值（末基线 2530.73 + 行高 ≈ 2547），非墨迹溢出，见上墨迹实测。
- P1 顶带墨迹间距（y=92）：左 65–220（`VOL. 2 · 第2号`）、中 675–1275（顶条行）、右 1530–1885（日期行），无碰撞。

## 7. P7（定义句冻结、金句、词框 gloss、增加项构成）

- 定义句本地化 **0 处**：核心构建与本版构建 content7.py 全量 diff 显示，改动仅限注释/指令词/家具半句/披露行/金句译文；以下目标语定义句逐字冻结：
  - 词框 gloss 头：`読書週間/紹介/読み聞かせ`、`見頃/紅葉狩り/落葉`、`〜倍/〜%/〜万食` 逐字 = 核心，仅荷兰语释义本地化；
  - 诊所 4 项：日语错句与纠正句逐字 = 核心，仅第 3 元素（讲解）本地化；
  - 句式框日语句 `『ゆるく整える』 — ゆるく（無理をしないで）＋整える（体と心をよくする）。忙しい人でも、ゆっくり体を整える、という意味です。` 逐字 = 核心，仅框注本地化为 `Uitleg: lichaam en geest rustig in orde brengen.`。
  - P7 移除的 35 串中唯一日语长串是核心披露行 ld（日语披露 + 中文披露 lcn 两行并存，见 §8），属披露本地化，非词框定义句删除。
- 金句 8 句：去空白拼接口径下核心与本版均为 **[2,2,2,2,2,2,2,2]**（文章内 1× + P7 列表 1×）；页签分布本版 `(Pagina 1)×2、(Pagina 2)×2、(Pagina 3)×1、(Pagina 4)×1、(Pagina 5)×1、(Pagina 6)×1`，与核心元组分布（第1面×2、第2面×2、第3/4/5/6面×1）一致；日语句逐字 = 核心。
- P7 增加项 **38 条**（非 KIT 旧称 43，独立重算 freeze P7 added = 38）：构成为荷兰语 apparatus（金句荷兰语译文 8 串、诊所荷兰语讲解 4 串、来信披露荷兰语 5 行、家具荷兰语半句、页脚/页码、`Vul in`×6 等）+ 已在核心的日词头重组串（如 `ことば · Taal`、`見頃 mooiste periode · 紅葉狩り`）——新增 CJK 多重集为 0，证明无新日语文本混入。
- P7 词框 gloss：A2 3 / B1 3 / B2 3，日词头逐字 = 核心，仅荷兰语释义本地化。

## 8. gloss 与读者来信角

- gloss 渲染 · 切分（同 x 续行归组法，独立重测）：本版 P1 4 / P2 9 / P3 8 / P4 7 / P5 7 / P6 4 = **39**；核心同法（前缀 `译注｜`）亦为 P1 4 / P2 9 / P3 8 / P4 7 / P5 7 / P6 4 = **39**，逐页分布 = 核心。源文件分组口径（13+15+11+0 之类）是另一口径，不得作为渲染结论引用。
- gloss 前缀框口径：P1–P6 `Uitleg — ` 框 = **10**（P1×1、P2×2、P3×2、P4×2、P5×2、P6×1）；W43 同配对同法亦为 10 且同分布。P7 的 `Uitleg:` 框注（`Uitleg: lichaam en geest rustig in orde brengen.`）为另一形式，不计入此 10——该口径与 W43 一致（W43 P7 无 `Uitleg` 前缀行，本版 P7 有 1 行 `Uitleg:`，属 VOL.2 句式框注形式，不混入 10 框计数）。
- 读者来信角：
  - 日语例信逐字冻结：核心与本版 content7.py 的 lt 串逐字一致：`「こんにちは。私は中学生です。読書週間には、図書館で本を2冊読みたいです。文化の日には、家族と金沢へ行きたいです。」— 読者の手紙の例`，零编造。
  - 核心披露为日语 ld + 中文 lcn 两行并存；本版以单条荷兰语披露替代，属有效披露本地化（荷兰语读者无法阅读日语/中文披露）。
  - 荷兰语披露（P7 x=1473，y=1608.24–1721.84，5 行，完整位于来信角框内 rect y=1367.12 h=383，底边余 28.28px）逐字摘录：
    > `Voorbeeldbrief, geen echte brief. Er waren nog geen echte brieven of beste P8-opstellen binnen; beide verschijnen in VOL.3. Stuur je Japanse brief op — gekozen brieven komen in VOL.3!`
  - 范围裁定：含 3 事实——①示例非真信（`Voorbeeldbrief, geen echte brief`）、②无真信（`nog geen echte brieven … binnen`）、③无最佳 P8 作文（`geen … beste P8-opstellen binnen`）——+ 明确祈使征集（`Stuur je Japanse brief op`）+ VOL.3 承诺（`beide verschijnen in VOL.3` / `gekozen brieven komen in VOL.3!`）。teaser 行（`来週 · Volgend nummer (VOL.3)` + 预告段）是内容预告，不计作征集。

## 9. 家具三方对照（W45 核心 / W43 同配对 / 本版；W43 优先于 README §20 泛化）

| 项 | W43 同配对实测 | 本版实测 | 裁定 |
|---|---|---|---|
| 刊名 | y=248，`Lucerna` | y=248，168pt，`Lucerna`（无冠词） | ✓（README §20 泛化 262 不采纳，正确） |
| 副标题 | y=316 | y=316，40pt，`日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間` | ✓ |
| badge | y=356，19pt，bold，串逐字同 | y=356，19pt，weight 700，串逐字同 | ✓（颜色见观察 1） |
| 标语 | y=390 | y=390，19pt，`日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で` | ✓ |
| 规则线 / 暗带 | 406/413；暗带 rect y=424 h=118 | 406/413；暗带 rect y=424 h=118 | ✓ |
| 顶条中段 | `毎週、日本語で · Elke week · …` | 同串，y=92 | ✓ |
| 页脚 | `Lucerna · JAPANS WEEKBLAD VOL.1 · …` | `Lucerna · JAPANS WEEKBLAD VOL.2 · TEKSTEN IN HET JAPANS · UITLEG IN HET NEDERLANDS`，8 页 | ✓（VOL.1→VOL.2 正常升级） |
| 页码行 | `Pagina N van 8` | 8 页齐全 | ✓ |
| P8 分隔符 | `— Pagina N —` | 8 条齐全 | ✓ |
| P8 带右侧 | `Pagina 8 · 週の大きなテスト + 全ての答え` | 同串 | ✓（W43 NL 措辞，非 JA×EN 的冻结日语 `第 8 面`） |
| E 区指令 | 方向性 2× Nederlands + 2× Japans | `Vertaal naar het Nederlands`×2（#137/#138）、`Vertaal naar het Japans`×2（#139/#140） | ✓（W43 NL 方向性） |
| P2/P8 匹配指令 | P2 `Combineer`、P8 `Combineer` | P2 `Combineer`（25–28 题）、P8 `Combineer`（141–144 题） | ✓（W43 先例；见可读性裁定） |
| P3 匹配指令 | 完整形 | 完整形 `Koppel activiteiten aan plaatsen en tijden`（43–46 题）保留 | ✓ |
| P4 带题 | — | `スポーツ · 体育` 原样保留 | ✓ |
| 答案区标题/注脚 | — | `答え · Antwoorden — gegroepeerd per pagina: zoek je nummer op` / `Bij elk antwoord een korte notitie in het Nederlands · ✓ = de vraag met de voorbeeldtekst` | ✓ |

- `Combineer` 缩短可读性与内容损失裁定：P2 freeze diff 显示仅指令串 `把词和释义配对` → `Combineer` 一处替换，配对题干/选项无一改动；P8 同理。版式语境（P2 `25–28.` 题组 + a–d 释义项、P8 `141–144.` 题组 + a–d 释义项）使单字祈使无歧义；P3 的另一类配对（活动↔地点时间）保留完整形，类型区分未丢失。W43 同配对 P2/P8 亦为 `Combineer`，先例一致。**可读，无内容损失。**

## 10. 计数 / 范文 / 图片 / 摘要 / 复现性

- 登记展开（scratch 重跑，OUT 重定向至自有目录，单进程 run.py）：TOTAL **150**，连续 1–150；级别 **A2 46 / B1 75 / B2 29**；页分布 **10 / 18 / 18 / 18 / 18 / 18 / 12 / 38**（P1–P8）；类型分布：zinnen aanvullen 50、meerkeuze 51、combineren 12、zinnen bouwen 8、waar of onwaar 11、gatentekst 13、vertalen 4、schrijven 1——全部 = 核心。
- 范文：MODELO 经 AST 求值，核心与本版均为 **167 字**（按字数，去空格同值），文本逐字一致；P8 H 区渲染范文（`例： ` + MODELO 换行拼接）两边均与 MODELO 完全相等；标题《私の11月の週末》逐字 = 核心。
- 图片 payload（逐页 = 核心；口径说明：构建员声称值对应**解码后 JPEG 字节的 sha256 前 12 位**，base64 文本口径另列，两口径下核心 = 本版均成立）：
  - P1 红叶：解码 `140f46d9e41b`（base64 文本 `92f3f41c7cec`，474,411 B）
  - P3 歌川广重三代：解码 `e293b32d5911`（base64 文本 `76f4abb34efc`，612,700 B）
  - P4 球场：解码 `19990669abb5`（base64 文本 `ab8d113ff083`，591,942 B）
  - P5 南瓜：解码 `6242ca640af3`（base64 文本 `f954d75303c8`，70,608 B）
  - P2/P6/P7/P8 无内嵌图（= 核心）。
  - credit 行逐页 = 核心且在页：P1 `写真：Poliphilo — CC0（Wikimedia Commons）`、P3 `版画：歌川広重（三代）— パブリックドメイン（Wikimedia Commons）`、P4 `写真：Syced — CC0（Wikimedia Commons）`、P5 `写真：Petr Kratochvil — パブリックドメイン（Wikimedia Commons）`。
- ABSTRACT：荷兰语单行，354 字，无 ASCII 双引号；含真实主题关键词（Cultuurdag op 3 november、herfstbladerenweekend van 7–8 november、verlichting in Kobe、Leesweek tot 9 november、Japan Series in Yokohama、rustig herfsteten）+ 学习者检索短语（`150 oefeningen op niveau A2 tot B2 voor wie Japans leert door te lezen`）。全文：
  > `Lucerna Japans Weekblad VOL.2 voor Nederlandstalige lezers: Japanse teksten met Nederlandse uitleg over Cultuurdag op 3 november, het herfstbladerenweekend van 7–8 november met de verlichting in Kobe, de Leesweek tot 9 november, de Japan Series in Yokohama en rustig herfsteten, met 150 oefeningen op niveau A2 tot B2 voor wie Japans leert door te lezen.`
- NL 族 transform 同步规则核查（修复改动必须落进 transform.py）：**通过，无 caveat**。scratch 重跑证明：
  - `transform.py`（自有 scratch 副本，仅 EDITION 路径重定向以保安全）从原始核心构建重跑，产出的 bslib4.py、content12/34/56/7/8.py、render.py、run.py 及 assets 4 文件与交付构建树**逐字节一致**；
  - `gen_nl.py` 重跑产出的 transform.py 与交付 transform.py**逐字节一致**——生成链完整可复现，修复改动确已全部进入 transform.py（无 nl-en 式"内容正确但不可复现"的过程 caveat）。
  - 登记重跑产出的 8 张 SVG 与交付 SVG **逐字节一致**（`pre-hashes.txt` 对照）。
- P8 印刷笔记口径 150 条（非 EN 族的 78），核心 P8 本身亦印 150 条，已在 §5 复核。

## 11. 全 8 卡目视与交付前后哈希

- 8 张卡片逐张目视（p1–p8）：无溢出、无重叠、无裁切标签、无错位框。重点复查：P1 刊头/badge/标语几何干净；P2 `Combineer` 配对组完整可读；P3 #37 题干与广重版画 + credit 干净；P4 球场图 + credit 干净；P5 南瓜图 + credit 干净；P6 图表标签 38/27/21/14% 齐全无裁切，练习数据声明在页；P7 读者来信角披露 5 行完整在框内、预告带完整；P8 F 区 `Combineer`、E 区方向性、#37/#32 对照、#150 行完整。
- 校对前后：交付目录哈希 diff 为空（`pre-hashes.txt` vs `post-hashes.txt`）；核心 SVG 哈希 diff 为空。校对过程未写交付/核心目录。

## 12. 非阻塞观察（不改纸面，不阻塞）

1. **KIT §1 badge 颜色词与纸面不符（KIT 文字错误，纸面按任务列举标准正确）**：KIT 写 badge"砖色 #a4553a"，但本版 badge 实测 fill 为橄榄绿 `#3e4c2a`（content12.py  badge 行用 OLIVE）。W43 同配对 badge 确为砖色 #a4553a；但 W45 JA 族内 JA×EN、JA×FR 的 badge 亦为橄榄绿 #3e4c2a（EN 脚手架继承，仅 JA×DE 为砖色），且任务列举的 badge 核查项（y=356、19pt、bold、串逐字）全部通过。裁定：属 KIT 措辞错误，纸面颜色与 W45 JA 族已过审先例一致，**不因此改纸面、不阻塞**；若母线要求严格回归 W43 砖色，需另行发话重建（不在本次校对权限内擅自改动）。
2. **P8 末端余量口径澄清**：构建员声称"P8 #150 于 2530.73"为基线口径；墨迹口径余量更紧（#150 墨迹底余 5.27px，分隔行墨迹底余 3.90px），均 <2540 通过，但余量小，未来改版若加长 P8 末行须重测。
3. **构建员补充审计的图片正则漏检**：其 `audit_suppl.py` 图片正则只认 `xlink:href`，故图片节输出为空列表；本次独立解析（`href` + `xlink:href`）已证实 payload 逐页 = 核心——属审计脚本口径问题，非纸面问题。
4. **W43 参照路径说明**：weekly-git 的 `issues/2026-w43/2026-w43-ja-nl/` 仅含 md 与 PDF，无 SVG；本次 W43 SVG 三方对照实际取自 KIT 所引的 `files/weekly-report-ja-nl/`（VOL.1 已交付版），几何与措辞实测均出自该目录。

## 阻塞项清单

无。

**不宣布上架。** 本报告仅为独立校对结论，交付动作由母线另行决定。
