# 独立校对报告 — Lucerna Weekly W45 EN × DE（目标英语 × 读者母语德语）

**结论：ZERO PROBLEMS**

校对对象：`files/weekly-report-w45-en-de/`（SVG × 8、卡片 × 8、印刷 PDF、网页 PDF、`WEEKLY-KIT.md`、`ABSTRACT.txt`）。
对照：EN 核心 `files/weekly-report-w45-en-core/`（VOL.2，刊头 The Lucerna）；W43 同配对已上架家具 `files/weekly-report-en-de/`（只读对照）。
本校对只读、不改源码、不宣布上架、不派生下级代理；未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心与 W43 目录、未清理共享 scratch 目录。
构建员自述全部独立重测，未采信任何一项——以下每项均为本次实测结果。

## 开工条件与哈希

- 开工前查无进行中渲染进程；交付物 mtime 全部在 2026-10-28 00:13–00:21 UTC 且 90 秒复查零新写盘，安全开工（非 stand down 情形）。
- 校对前全部交付物与核心 sha256 记录于 `hashes-before.txt`；校对后复核：**全部哈希不变**（`hashes-after-clean.txt` 与校对前逐项一致）。
- 双 PDF 与任务/KIT 一致：印刷 `The-Lucerna-VOL2-DE.pdf` 17,295,556 B，sha256 `0605300932508500a7fbd13c4e506fd1b88c9ea4b86620c1e568224bdecb2d82`；
  网页 `The-Lucerna-VOL2-DE-web.pdf` 4,027,862 B，sha256 `c0edc0c215f16aef316bc65ac2e245ddc9eece7ac614d2b4e0c5b9ddfb63f4c5`；pypdf 实测均为 8 页。

## 1. 冻结

- `tools/freeze.py baseline`（EN 核心构建树）：**8/8 逐字节复现**，核心 SVG 完好性复核通过（`freeze-baseline.txt`）。
- `tools/freeze.py diff`（JSON 去重串计数，与构建员 `freeze-diff-r4.json` 逐串比对**完全一致**）：
  P1 +28/−26、P2 +27/−26、P3 +17/−17、P4 +17/−16、P5 +20/−17、P6 +19/−16、P7 +44/−32、P8 +145/−104；
  每页新增 CJK = 0，版面 CJK 总计核心 183/197/119/139/134/136/347/776 → 分版 0。
  （注：freeze.py 终端行显示的是含重复串的合计，如 P2 +34/−33；JSON 去重计数才是与 KIT 一致的口径，两者均已核对，无矛盾。）
- 被删串归属（254 条去重串，逐项分类，见 `removed-strings.txt`）：
  (a) 含 CJK 的讲解层串：P1 24、P2 26、P3 17、P4 16、P5 17、P6 16、P7 31、P8 85；
  (b) W43 家具刊头语替换核心刊头语：P1 1 条（`THE LEARNERS' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA`；核心页脚等替换串本身含 CJK，计入 (a)）；
  (c) 被保留内容的重排换行碎片：P1 1 条、P8 5 条整序碎片 + 14 条加注换行碎片（见下）；
  (d) 标点碎片：P7 1 条（`6).`）。
- **无冻结英语正文被删**，三重证据：
  (1) P1–P7 全部被删串均落入 (a)–(d)，无例外；
  (2) 核心 P1–P7 全部纯英语长行（>25 字符、无 CJK）在分版页面拼接文本中**零缺失**（P1–P6 各 0 条，P7 0 条）；
  (3) P8 的 14 条碎片确为 print-all-notes 插入注释后换行断点改变所致：碎片所涉键经登记表逐项核对全部原样存在（如碎片 `1. ballot · 2. midterm · 3. November 3 · 4. early` 对应登记键 1–4 全同；`75. d · 76. b · 77. a · 78. The map is changing colour now.` 对应键 75–78 全同）。
- 分版 SVG 8 页：CJK = 0、全角括号 = 0、`桥接` = 0；ABSTRACT 同样 0/0/0。KIT 的一点例外见文末非阻塞观察。

## 2. P8

- `tools/p8.py compare` 独立重跑：核心 78 noted → 分版 150 noted，**status EXTRA_ONLY，missing=[]，extra_count=72，keydiff=[137, 138, 139, 140, 150]**，与构建员所报逐项一致。
- 计数口径独立确立：核心 P8 只对 78 题印注释（其余 72 题只印裸键）；分版印全部 150 题注释。72 条 extra 经 `detect_note` 逐项验证：**全部为分版有注、核心裸键**（bad=0），确为 print-all-notes 产物，非遗漏或错配；missing=[] 属实；分版 noted 集 = 1–150 全集。
- keydiff 逐项印刷行对照（分版段 vs 核心段，全文见 `p8-compare.txt` / 提取 JSON）：
  - 137 EN→DE：体 `Translate : « Patience is part of the system, not a failure of it. »` 不变；键由中文译文变为 `Geduld ist Teil des Systems, nicht ein Versagen des Systems.`，注为德语。真重定向。
  - 138 DE→EN：体 `Übersetze: Dienstag, der 3. November, ist Wahltag in den Vereinigten Staaten.`；键 `Tuesday, November 3, is Election Day in the United States.`。真重定向。
  - 139 DE→EN：体 `Übersetze: An diesem Sonntag spielt die NFL in Madrid.`；键 `On Sunday, the NFL plays in Madrid.`。真重定向。
  - 140 EN→DE：体 `Translate : « Not every place changes. »` 不变；键 `Nicht jeder Ort stellt die Uhren zurück.`。真重定向。
  - 150 写作登记键德语化：`Offene Aufgabe — Stichpunkte im Schreibkasten; Mustertext im Kasten auf Seite 8`，注 `Bewertung nach Stichpunkten`；与 W43 形式逐字一致（W43 为 149 题版，其 149 号键同串分行；见 §7）。
  - 5 项皆为语言内容真重定向，无括号分支伪影（分版统一半角 `(note)`，核心为全角 `（）`，但键文本本身的语言确实改变，非仅标点改写）。
- P8 注释纯德语：分版 P8 全部印刷段 CJK = 0；登记表注释 CJK = 0（注释为德语讲解，含英语词头属双语 gloss 设计，非中文）。
- P8 印刷笔记集合相等性裁定：**EXTRA_ONLY 可接受**——分版集合为核心集合的超集，核心 78 条全部在场且键仅上述 5 项不同。

## 3. 几何

- `tools/occlusion_audit.py`（自检 6 类 planted 全部触发）：分版 **0 旗标**、核心 **0 旗标**、NEW vs 核心 **0**（`occlusion-edition.json` / `occlusion-core.json` / `occlusion-new.json`）。
- 独立几何扫描（自写 `geometry.py`，与构建同款 Noto CJK SC 字体文件）：
  - 右缘 ADVANCE 扫描（内框右缘 1910）：8 页 **0 越线**，各页最大 advance 右端 1885.0–1903.8；
  - 框线压框扫描（外框 28..1922 × 28..2672，锚点修正后）：8 页 **0 越出**；
    （方法注：首版脚本 ink_box 忽略 middle/end 锚点，误报 end 锚文本越框；按 occlusion_audit 的锚点算法修正后重跑为 0，此为我方脚本 bug，非版面问题。）
  - 同基线解码后碰撞扫描：8 页 **0 碰撞**；
  - P6 图表覆盖（基线锚定墨迹法，PIL getmetrics，anchor ls，门限 <30%）：8 页最大覆盖 **0.0%**；核心 P6 图表确为流式文本行（`No lines : 38%` 等），其后无矩形覆盖；P1 搜索条同样 0 覆盖。
- R4 的 P1 深色带对子重测：行 1 advance 间隙 **64.8px**（与构建员所报精确一致），墨迹间隙 65.0px；行 2 advance 间隙 81.2px、墨迹间隙 106.6px（构建员所报 106.5px 为墨迹间隙口径）；顶带两间隙分别为 488.3px 与 **201.3px**（后者与所报一致）。卡片全分辨率裁剪（`crop-p1-band.png`）目视：左右两行视觉分离明确，无相触。
- 紧张点重测（构建树 scratch 重跑日志，与构建员一致）：P1-headline 流 1823/1828（5px 余量）、P7-B1 栏 1129/1150（21px 余量）、P8-keys 流 2274/2530、P8-battery 流 1390/1485，均在界内。
- R3→R4 变化范围（run3/run4 基线哈希逐项比对）：**仅 P1 SVG、P1 卡片、双 PDF 变化**，其余 SVG × 7、卡片 × 7 哈希全同——与所报范围一致。

## 4. gloss

- 渲染后重组（`Anmerkung | ` 起行 + 同 x/同字号后续行拼接，按 `·` 拆分；核心以 `译注｜讲解｜` 起行同法重测，非照搬构建员数字）：
  核心 18 = 分版 18；分版 P2 **3** / P3 **4** / P4 **4** / P5 **3** / P6 **4**，与核心独立实测分布 1:1。
- 逐项对应（英语词头 18/18 全部为核心词头的前缀一致）：
  P2 to fall back / a costume / trick or treat；P3 to open / a monster / a catchphrase / a series；
  P4 a fixture / a title / to defend / a fan；P5 a map / too close to call / a second screen；
  P6 to register / a governor / to shape laws / patience。分版全文见 `checks-out.txt` §D。

## 5. P7

- 结构与核心一致：顶栏四栏（A2 FALLING BACK + GOING TO + EXAMPLE / B1 COMPARATIVES + PAST SIMPLE + EXAMPLE / B2 HEADLINE PRESENT + WHETHER + EXAMPLE / TOOLBOX 3 随身句 + bridge）、中部 PHRASES OF THE WEEK（金句 100–107）、下部 ERROR CLINIC（108–111）+ READERS' CORNER + NEXT WEEK 预告；各栏标题 y 坐标与核心一致（116/227/1236/1903）。
- 金句 8 句：分版 P7 SVG 中全部命中，页标签与级别与核心一致（各 2×：原文页 + P7）；
  纸面 ` ?` 间距约定下逐字一致（如 `Which film would you choose ?`，核心与分版同式；KIT 引文省略空格不影响逐字性）；
  金句页标签序列：100→p.1、101→p.2、102→p.3、103→p.4、104→p.5、105→p.6、106→p.2、107→p.4，与核心一致；
  级别序列：100 A2、101 A2、102 B1、103 B1、104 B2、105 B2、106 A2、107 B1（登记表核对）。
- 定义句：核心 P7 全部纯英语长行在分版 P7 拼接文本中**零缺失**；仅 gloss/讲解德语化，无定义句本地化。
- 诊所 108 A2、109 A2、110 B1、111 B1，与核心结构一致。

## 6. 读者园地

- 英语示例信与英语标注逐字冻结：核心园地 3 行英文（`« On Sunday, I slept one hour more — and I still woke up late ! » — M. L., a reader in Chicago (editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled)`）在分版中逐字相同；VOL.3 预告英文段亦逐字保留。
- 德语披露句逐字摘录（分版 P7，4 行）：
  `Anmerkung der Redaktion | Bis Redaktionsschluss sind keine echten Leserbriefe eingetroffen, und es gibt keinen besten VOL.1-Schreibtext zu besprechen. Das Beispiel oben bleibt daher ehrlich gekennzeichnet stehen; echte Briefe erscheinen ab VOL.3. Schicke uns deinen Brief und deinen Text — wir drucken sie in VOL.3!`
- 逐项核实：3 事实全有——(1) 截至截稿无真实来信，(2) 无可讨论的最佳 VOL.1 写作，(3) 示例保持诚实标注、真实来信自 VOL.3 起刊登；
  显性祈使邀请：`Schicke uns deinen Brief und deinen Text — wir drucken sie in VOL.3!`（内容预告行 `echte Briefe erscheinen ab VOL.3.` 不算邀请，另计）；
  无编造：事实与核心园地中文披露（未收到真实来信与 VOL.1 写作投稿、VOL.3 起刊登）及 P8 写作题（最佳文本登 VOL.3）对应；无凭空新写英语披露句。
- 最佳 P8 作文覆盖范围裁定：**已覆盖**——披露句 (2) 说明无最佳 VOL.1 写作可讨论，且邀请明确包含 `deinen Text` 并承诺 VOL.3 刊登，与 P8 写作题 `The best texts will appear in VOL.3` 闭环。
- 4 行框内无溢出实测：园地框 rect x=989 y=1878 w=896 h=300（框底 2178），披露末行基线 2160，**余量恰 18px**，与 KIT 所报一致。

## 7. 家具

- W43 偏差清单逐项核实：
  - 缩短的德语框标题（advance 量宽 + 在框验证，全部在框且与所报宽度精确一致）：
    P1 `THE WEEK IN NUMBERS · Zahlen` 375.9px（≤412）、P1 搜索副标题 `Diese Woche gesucht · Google Trends USA` 382.0px（≤412）、
    P3 `AT HOME THIS WEEK · Zu Hause` 368.1px、P4 `SUNDAY, NOVEMBER 8 · Spiele` 353.0px、
    P5 `TOO CLOSE TO CALL · Zu knapp` 365.1px、P5 `FIVE SENTENCES · Fünf Sätze` 341.3px、
    P6 `A PRACTICE BALLOT · Stimmzettel` 395.6px、P6 `READ THE CHART · Diagramm` 375.7px（≤434，替代 `Diagramm lesen`）；
    另 P1 带首行 `SONNTAG UMGESTELLT`（R4 缩短）见 §3。
  - 徽章逐字一致：`ENGLISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER`（W43 同串）；
    页脚形式一致（仅 VOL.1→VOL.2 的卷号变化）：`The Lucerna · ENGLISH WEEKLY VOL.2 · Englischer Text · Deutsche Erklärungen`；
    页行 `Seite N von 8` 8 页全同；gloss 前缀 `Anmerkung | ` 全同；P8 分隔符 `— Seite N —`（N=1–8）与 W43 全同；
    P8 渲染参数与 W43 一致（印全部注释、半角括号、D 标题 `D · SENTENCES · Sätze formen`、写作键 W43 形式，见 §2）；
    P1 strapline 与 W43 逐字一致：`WEEKLY IN ENGLISH · Jede Woche neu · Englisch, wie Amerika es liest`。
- P6 选票框 ☐ 缺字框：核心卡片与分版卡片同区域裁剪对照（`crop-p6-ballot-co.png` / `crop-p6-ballot-ed.png`）——**同一位置、同一缺字形、同一冻结英文串**，确为核心固有渲染，非分版缺陷。

## 8. 其余交付核查

- 图片载荷：每页图片数与核心相等（P1/P2/P3/P4/P6 各 1、P5/P7/P8 各 0），解码后载荷哈希逐页相等；署名在版且与核心逐字相等
  （P1 Kenneth C. Zirkel — CC0, via Wikimedia Commons；P2 Public domain, via Wikimedia Commons；
  P3 Édouard Manet — CC0, via Wikimedia Commons；P4 Frank R. Snyder — public domain, via Wikimedia Commons；
  P6 Public domain, via Wikimedia Commons）。
- ABSTRACT：德语单行（1 行 + 换行符）、无 ASCII 双引号、含真实主题关键词（Midterm-Wahlen、Wahltag 3. November、Zeitumstellung 1. November、Halloween、The Cat in the Hat、Godzilla Minus Zero、NFL in Madrid 8. November、US-Wahlsystem）与学习者搜索短语（`Englisch lernen mit Nachrichten aus den USA, Wahlen und Vokabeln`）。
- 题量与级别（登记表 scratch 重跑展开计数，非照搬 KIT）：**150 题**；页分布 **10/17/18/18/18/18/12/39**；
  级别 **A2 60 / B1 69 / B2 21**；类型：单选 41、完成句子 33、词汇配对 20、句型转换 16、完形填空 8、跟练 8、图表读数 6、对话补全 5、改错 4、阅读理解 4、翻译 4、写作 1；
  登记表比对：页码与级别 150 题全同，键仅 137/138/139/140/150 不同；类型 token 12 类与核心中文类型 1:1 映射（本地化层，预期内）。
- 范文：分版 P8 MODEL 段 **85 空白词**，与核心范文逐字相同（85 词，含 `« Ohio is too close to call ! »` 等标点分词口径一致）。
- 构建可复现性（强于 KIT 自述）：分版构建树 scratch 重跑 8/8 SVG 与交付逐字节相同；核心构建树 scratch 重跑亦 8/8 相同。
  流末值与 KIT 一致：P1-headline 1823/1828、P2-ex 2390/2562、P8-battery 1390/1485、P8-keys 2274/2530。
- 目视：8 张卡片全部逐页看过（p1-front、p2-life、p3-culture、p4-sport、p5-jeunesse、p6-politique、p7-langue、p8-exercices），另加 R4 后 P1 深色带全分辨率裁剪复查；未见溢出、遮挡、错位、缺字（除上述核心固有选票框缺字形外）。
  注：P4 栏间断句（栏末 `On Saturday, November 7, the` 接下栏 `warm-up is already on`）为正常跨栏续句，核心同式，非截断。

## 非阻塞观察（不影响 ZERO PROBLEMS）

1. **KIT 的 CJK 字面计数为 1 而非 0**：`WEEKLY-KIT.md` §10 在举例被删标点碎片时原文引用了 `。`（`(`6).`, `。`)`）。这是对碎片类别的元讨论引用，非中文正文；KIT 无中文讲解、无 `桥接`。构建员“KIT CJK=0”的自述在 freeze 正则（含 `。` 所在区段）下严格不成立，特此订正；不构成纸面缺陷，建议后续 KIT 改写该例时避免直接引用该字符。
2. **R4 带行 2 间隙口径**：构建员所报 106.5px 为墨迹间隙（实测 106.6px），advance 间隙实测 81.2px；行 1 的 64.8px 则为 advance 间隙（实测精确一致）。两行间隙均舒适，无问题。
3. **R1/R2 基线缺失（流程记录缺口，非纸面缺陷）**：构建树现存 run3/run4 基线与最终轮输出，R1/R2 原始日志与基线已不在树中（与 KIT §9 所述一致）。本结论建立在终版全量重测之上（冻结 8/8、登记表全量、几何全量、逐页目视），未因此免测；建议后续轮次保留全部轮次基线。
4. **紧张余量**：P1-headline 流 5px、P7-B1 栏 21px，虽在界内但偏紧；终版几何与目视均干净，列为观察，不阻塞。
5. **P6 ☐ 缺字框与 P7 诊所 ☒ 标记**：前者为核心固有渲染（§7 已对照），后者在核心与分版同式出现，均不作分版缺陷。

## 证据文件（本目录）

- `REPORT.md`（本报告）、`hashes-before.txt`、`hashes-after.txt`、`hashes-before-clean.txt`、`hashes-after-clean.txt`
- `freeze-diff-proof.json`、`freeze-diff-proof.txt`、`freeze-baseline.txt`、`freeze-baseline.json`
- `p8-compare.txt`、`p8-compare.json`、`p8-extract-core.json`、`p8-extract-edition.json`、`p8-extract-w43.json`、`p8-extract-summary.txt`
- `occlusion-selftest.txt`、`occlusion-edition.txt`、`occlusion-edition.json`、`occlusion-core.txt`、`occlusion-core.json`、`occlusion-new.txt`、`occlusion-new.json`
- `checks.py`、`checks-out.txt`、`checks2.py`、`checks2-out.txt`、`geometry.py`、`geometry-out.txt`
- `registry.py`、`registry-edition.json`、`registry-core.json`、`registry-edition-log.txt`、`registry-core-log.txt`、`registry-edition-hashes.json`、`registry-core-hashes.json`
- `removed-strings.txt`、`crop-p1-band.png`、`crop-p6-ballot-ed.png`、`crop-p6-ballot-co.png`
- scratch：`freeze-baseline/`、`scratch/edition/`、`scratch/core/`（仅校对复现用，未写入交付树）
