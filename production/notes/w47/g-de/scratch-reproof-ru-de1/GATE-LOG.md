# GATE-LOG — 2026-W47 ru-de re-proof（fix1 重建版，全部机械门自跑证据）

工具：`~/workspace/weekly-git/tools/venv/bin/python`；正典 creambox：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`。
`TMPDIR` 全程指向本 scratch 的 `tmp/`。证据文件默认在 `gates/`，渲染在 `render/`，裁图在 `crops/`。
驱动脚本 `run_gates.py`（本 scratch，由 fix1 同名脚本仅改路径复用；check_core 调用已修正为带参 `check_core.py <版>` + cwd=版目录，
fix1/FIX-LOG §6 记载的无参驱动 bug 在此不再出现），裁决脚本 `adjudicate.py`（由 fix1 同名脚本仅改路径复用），
标题量测 `measure_title.py`，垂直溢出另扫 `vertical_spill.py`（自写，方法见 §6b）。
生产文件全程只读，未改动、未 commit、未 push（复校后 `git status`：ru-de 目录仍为原样 untracked，无 tracked 修改；
`find -newermt 2026-11-11 17:06 UTC` 在版目录与 core-ru 均为 0 文件；HEAD 仍为 `c0382fa7`）。
**run.py / render.py / webpdf.py 均未在生产目录运行**——三者在 scratch 的 `build-copy/` 副本内重跑（见 §1a），生产目录零写入。

## §0 身份核对

- 探针：`git hash-object -w`（`9daeafb9…`）+ scratch 真实写 OK 后开工。
- `sha256sum` 实跑：印 PDF `872b4f1c…9ebd`（21,231,616 B）、网 PDF `c8c21903…54d`（3,385,828 B）、
  text.md `8a5f1a9b…44d`（63,506 B）——与任务先验全符。

## §1a 可复现性：scratch 副本重建（run.py / render.py / webpdf.py）

- 方法：`cp -r` 版目录 → `build-copy/`（删 `cards/`、`__pycache__`；`svg/` 移为 `svg-baseline/` 后重建）。
- `run.py`：**rc=0，TOTAL 150**，0 FLOW OVERFLOW / HEAD TOO WIDE（`render/run-copy.log`）；
  by level A2 50 / B1 76 / B2 24；by page 1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38；
  by type Ausfüllen 54 / Ankreuzen 55 / Zuordnen 20 / Sätze bilden 12 / Umformen 4 / Übersetzen 4 / Schreiben 1；
  model words 97；P8 Morozko SKIPPED（与 fix1 报告同，为既定构建条件）。
- 再生 8 张 SVG 与生产版 **逐字节一致**（`cmp` 8/8 IDENTICAL）。
- `render.py`：**rc=0**，8 张 cards + 印 PDF 21,231,616 B（`render/render-copy.log`）；
  再生印 PDF SHA-256 = `872b4f1c05d682f4f8a18749b7d63215a09bc2a151c3ca1601ef454de4019ebd`，
  **与交付印 PDF 完全相同**——印 PDF 可复现。
- `webpdf.py svg web-repro.pdf`：**rc=0**，网 PDF 3,385,846 B，57,837 text bytes（`render/webpdf-copy.log`）；
  与交付网 PDF 字节数差 18 B（预期：网 PDF 的 SHA/字节数不可复现，任务已明示永不以 SHA/字节数论证网 PDF）；
  文字层：交付网 = scratch 再生网 = 印 PDF，三者 **31,001 字符全等，逐页 8/8 全等**
  （per-page `[3131, 3380, 2715, 3418, 2950, 2862, 3590, 8955]`）。网 PDF 未重渲染生产文件。

## §1 Occlusion 审计（真实命令，未加 --selftest）

- 实跑 `tools/occlusion_audit.py <版>/svg --json gates/occlusion.json`：**42 TEXTX、0 LINEX**
  （rc=1 为“有 flag 即 1”，与 proof2 / fix1 同；另含自测行 planted 6 类全部触发，不计入 42）。
- 像素裁决（`adjudicate.py` Part A v3，1× 网格卡片墨阈值 min-channel < 140）：**33 项像素测试 CLEAR + 9 项 400 dpi 目视 CLEAR**
  （`crops/flags-contact-sheet-FIXED.png`，400 dpi clip 直接取自交付印 PDF，非 cards）——9 项与 proof2 / fix1 的 9 项逐项同框同值
  （flag 7/8 P1、11/12 P2、20/21 P4、28/30 P6、37 P7），均为词与后随标点/引号分离字形
  （`Краснодаре,`、`истории!`、`студента.`×2、`Краснодар»`×2、`студента,`、`Планируйте:`、`студента!»`），
  touch_rows 1–4 行均为单行扫描伪影。**42/42 CLEAR，0 真重叠。**
- 注意：该审计对奶油框内溢出、框标题溢出、横向溢出、降部溢出是盲的——以下 §2、§6、§6b 另行实测，不以 occlusion 0 放过。

## §2 正典 creambox.py 全版扫描

- `gates/creambox.log`：+45 px 窗口 + 逐行 clearance 全版扫描；**框内负余量 0**；
  BELOW-WINDOW 95 行，全为 +28.0（×25）/+32.0（×41）/+34.0（×4）/+37.0（×25），全部归入下一标题类
  （与 gates.json 的 unclassified 空表一致）。
- 与 backup-old 的 creambox 扫描逐行 diff：**仅 2 行**（`gates/creambox-vs-backup.diff`），即标题行本身
  （−`Der Spieltag in Zahlen` / +`Der Spieltag`，y=1240.7，clearance +343.0）——本次修复唯一新增变化。
- P7-TOOLBOX 汇总（creambox.log 内）：3 框，框内最小余量 +11.9 px，降部余量最小 +5.9 px。

## §3 p8 compare（`tools/p8.py`，直接读 `gates/p8-compare.json` 本体）

- `gates/p8-ed.json` / `gates/p8-core.json` / `gates/p8-compare.json`：**CLEAN；150/150 noted；keydiff=[137,138,139,140]**；
  `status=CLEAN`，`missing/extra/uncertain=[]`（本体已全文核对）。
- 与 core `ru-p8.json`（150 键）直接比对：keydiff 恰为 `['137','138','139','140']`。
- keydiff 逐条裁决（合法德语译文，核心中文键的正确德语替换；逐句手验见 PROOF-NOTE）：
  - 137 “Dienstag, 17. November, Tag der Studierenden.”
  - 138 “Ein Paket muss verfolgt, abgeholt und geprüft werden.”
  - 139 “Am Dienstag spielt Russland gegen Venezuela.”
  - 140 “Allen einen schönen Tag der Studierenden!”
- Q150 印出键 `✓`；Q20 印出键 `желании`（= core 键）；Q25 印出键 `b`。

## §4 Freeze（标准口径 + edition-internal 补充）

- **标准口径**：`freeze.py baseline --build <core-ru 构建目录> --core-svg <core-ru/svg> --out gates/freeze-core`：**8/8 字节一致**
  （`gates/freeze-core-baseline.log`，rc=0），“core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)”。
- 补充（不得冒充前者）：`freeze.py baseline --build <版> --core-svg <版>/svg --out gates/freeze`：亦 8/8；两基线 SVGs 相同，
  build-copy 差异仅为版自有文件 vs 核心自有文件（预期）。
- `freeze.py diff --core-svg core-ru/svg --edition-svg <版>/svg`（`gates/freeze-diff.json`，rc=0）：removed **851（distinct 486）**；
  西里尔删除恰 **15 项**，全部在 P8：`Билибин、Билибина、Зимняя、Иван、Ивана、Иллюстрация、Морозко、год、достояние、иллюстрация、к、можно、ноябрю、общественное、сказка`
  各 ×1 = Q46 `можно` + 14 个 Morozko 图注词（图按设计跳过），unexplained 0；新增 CJK 仅 U+3000 ×8。

## §5 Keycheck 150/150（逐题手验）

- `gates/keycheck-150.json` / `gates/keycheck-150.txt`：编号 1–150 连续；P8 印出键 150 项；
  与 text.md 答案键 **0 不符 / 149**（Q150 印 ✓，属设计；范文 97 词，实数，80–100 要求内）；
  分级 A2 50 / B1 76 / B2 24（配对块按节首级别归入）；分面 Ankreuzen 55 / Ausfüllen 54 / Zuordnen 20 /
  Sätze bilden 12 / Umformen 4 / Übersetzen 4 / Schreiben 1；P1 10、P2 18、P3 18、P4 18、P5 18、P6 18、P7 12、P8 38。
- 逐题手验方法：每题对照题干/正文/表格/阅读文/配对选项核对（逐项手核记录在 keycheck-150.json 的 `hand_note` 栏；
  130 道行内题干 + 20 道配对题全部逐项核对，配对块经 SVG 选项原文逐组核对）；
  重点项——Q20 `желании`（前置格）、Q25 b 短式、Q54 键 2:0 与 Q56 键 20:45（P4 赛果表 + VOL.3 更正框）、
  Q73 `заказов`（P5 原句 `14,4 миллиона заказов` 一致）、Q137–140 翻译键、Q145–149 对话键、Q129–132 Маша阅读文。

## §6 Boxtitle 逐个真墨实测（PIL，`adjudicate.py` Part B v2，不只看 advance）+ D1 双法 clear 表

- 方法：各页最小包含奶油框 + 内容缘 1862 / 页缘 1950；`OA.ink_box` 真墨为准。
- **D1（本次复核对象）**：P1 标题 `ТУР В ЦИФРАХ　Der Spieltag`（x=726.6 末段 y=1240.735 size=23）——
  法一 PIL 真墨右缘 **887.9 px**，框右缘 961.0 → **余量 +73.1 px**（`evidence/title-ink-pil.txt`）；
  法二 400 dpi 交付印 PDF 光栅（标题带 y1215–1250，clip 渲染）：真墨右缘 **887.9**（SVG 单位），余量 **+73.1**
  （`evidence/title-raster-ink.txt`）；两法相差 0.0。**D1 CLEAR。**
  400 dpi 裁图 `crops/d1-p1-subtitle-FIXED.png`（红线标框右 961.0）：词尾完整在盒内，盒右缘留明显奶油余量。
  其余：**零报告**——无过内容缘、无过页缘、无过奶油盒。D1 已从 Part B 消失。

### 框标题 clear 表（D1 双法）

| 法 | 来源 | 标题真墨右缘 | 框右缘 | 余量 | 下一栏左缘 989 距 | 结论 |
|---|---|---|---|---|---|---|
| PIL 字体真墨 `OA.ink_box` | SVG 节点 y=1240.735 | 887.9 | 961.0 | +73.1 | +101.1 | PASS（≤957） |
| 400 dpi 印 PDF 光栅 | 交付 `Lucerna-VOL4-ru-de.pdf` P1 标题带 y1215–1250 | 887.9 | 961.0 | +73.1 | +101.1 | PASS（≤957） |

- 各段真墨右缘：ТУР 600.5 / В 620.5 / ЦИФРАХ 722.9 / `　Der Spieltag` **887.9**（修前末段为 997.6，超框 +36.6 并越栏 +8.6；现已消除）。
- 碰撞：同基线仅标题本身；最近其他文字 x≥1461.5；无碰撞。

## §6b 垂直溢出另扫（spill sweep：全部奶油矩形末行墨底 + 全部框标题横向真墨）

- 自写扫描 `vertical_spill.py`（`gates/vertical-spill.log`，5,681 个节点）：每节点取最小包含奶油框（`#f0eee5`），量墨顶/墨底/基线 vs 框上下缘。
- 报告 62 个节点，**全部**为基线在框底之下 +28.0（×17）/+32.0（×26）/+34.0（×3）/+37.0（×16）的下一节标题行
  （P1 `СЕЙЧАС ВЫ`/`СЛОВО НЕДЕЛИ`、P2 `ЧТО ПОЖЕЛАТЬ?`/`Запомните…`、P3 `А ЧТО УЖЕ В КИНО?`、P5 `А ЧТО С 11.11?`、P6 日历图例）——
  与 §2 的 95 BELOW-WINDOW 行同一类，按设计在框外，不为溢出。
- **框内墨底违规 0、墨顶违规 0、墨底超页底 0**。#1 P2 降部候选（“Studenten, einen für Väterchen Frost.” 基线 1154.0、框底 1159.0）
  本次未触发：真墨底 1158.0，余量 +1.0 px，通过。
- 全部框标题横向真墨：见 §6 Part B v2 零报告。

## §7 印/网文字层比对 + D3 复核

- PyMuPDF：印/网均为 8 页；非空白字符 multiset **全等（总体 + 逐页 8/8），31,001 字符**；
  网 PDF 3,385,828 B < 7 MB；scratch 再生网 PDF 文字层亦全等（见 §1a）。网 PDF 未重渲染生产文件（只在 scratch 渲染比对）。
- **斜体清单**：印 PDF 恰 3 处斜体跨度，全在 P1（`«` Newsreader Italic、`чёрная пятница` NotoSerif-MediumItalic、`»`）；
  **网 PDF 亦 3 处**（LucernaNewsreader-Italic / LucernaNotoSerif-Italic / LucernaNewsreader-Italic）——#1 D3 已修好。
- 闭引号：`пятница»` 印/网各 7 处，脱离式 `пятница »` 0 处；`14-й` 印/网各 5 处，`14- й` 0 处。
  网版 P1 导读 `crops/d3-p1-web-standfirst.png` 目视：`«чёрная пятница»` 呈斜体、» 紧贴。
- P8 最小字号（PyMuPDF 实测印 PDF）：**9.75 pt**（全刊最小亦 9.75 pt）；符合 SOP §1.1 下限。

## §8 check_core.py / s11_check.py / verify_ed.py

- `check_core.py <版>`（cwd=版目录，带参；本次驱动已修正无参 bug）：**rc=0**；golden BAD **0**、gloss fails **0**；
  orphan line-starts 1（P7 y553 `”».`，已知良性，与核心同类）；same-baseline collision 1（P1 y1712 `чёрная`，与核心同位，节点逐项核对一致）。
  日志 `gates/check_core.log`。
- `s11_check.py <版>`：**rc=0**，`FAILURES: none`；8 SVG、纸色 `#fbfaf6`、徽章色、VOL.4 家具、左缘 88.0、可视 SVG 零真实 CJK、
  网 PDF 8 页 < 7 MB 均 PASS（`gates/run.log` 的 s11 节；注：run.log 里 “s11 FAIL lines: ['FAILURES: none']” 是收集脚本的误标——
  该行本身即“零失败”）。
- **verify_ed.py**：ru-de 不存在此脚本——`scratch-fanout-ru/` 与版目录均无 `verify_ed*.py`；已有的 `verify_ed.py` 均为 en-core 系，
  核查 en 专属项（Ashes Q39/40 等），不适用于 ru 版。等效覆盖已由 check_core（rc=0）+ s11_check（rc=0）+
  keycheck-150（0 不符）+ p8 compare（CLEAN）提供；此处如实记录，不冒充运行。

## §9 text.md / SVG 检查

- text.md：150 答案、无缺失；行内键 129 项与答案节一致（keycheck 脚本核对）；`___` 字面 **87 处**，全在填空题干中，
  核心继承的模板缺口，依任务裁定不作本版缺陷、不逐版修。
- SVG：零真实 CJK（`[\u3400-\u9fff\u3040-\u30ff]` 扫描，可见文本），U+3000 ×123（家具分隔符）；
  弯引号 « » 各页平衡、零直引号。
- text.md vs backup-old：**14 行（7 对）** = 修前 6 对 + 本次 L25 1 对（`Der Spieltag in Zahlen` → `Der Spieltag`），别无其他。
- SVG 文本集 vs backup-old：p1 41 节点（kicker 双空格重排 40 + y=1240.7 标题 1 键：本次修复唯一新增变化）、
  p2 7（全在 y=2162，Q25 选项 b 短式化，既有）、p3/p4/p5 **0**、p6 24（D1 s1 + 免责声明，既有）、
  p7 18（D1 s3，既有）、p8 23（Q20 键 + D1 s4，既有）。无手 patch 丢失。
- D5 字体（只记录不判定）：见 §14。

## §10 全页目视（150 dpi 整页渲染 `render/p1–p8-print150.png`，取自交付印 PDF）

- P1：刊头、条带、标题带、导读、统计框（D1 已修好，词尾在盒内）、目录页码锚、词框、照片 + CC0 说明、短讯框、测验 Q7–Q10、页脚 `Seite 1 von 8`——干净。
- P2：尤恩画 + 说明在位；节假日表、“А ВЫ?” 框、词汇四框、练习 A–D 齐全；Q25 选项 b 已缩短。
- P3：三栏正文、HINWEIS 词注框、右栏两框、练习 A–D（Q29–46）齐全；无图（按设计）。
- P4：1912 年照片 + 说明、VOL.3 更正框、赛果表 8 场、国家队栏、15 轮赛程表、TOP-5 表、练习 A–D（Q47–64）齐全。
- P5：市场玉米照 + 说明、黑五日期框、练习 A–D（Q65–82）齐全；德语标题引号为 „ “，正确。
- P6：日历条（16 пн…22 вс，21–22 高亮）、练习数据图（38+26+18+18=100%，标明为练习数据）、“ЗА И ПРОТИВ”框、
  练习 A–D（Q83–100）齐全；D1 s1 标题已落地一行内，免责声明在位。
- P7：三栏 A2/B1/B2、错题诊所四条（均在框内）、“СЛОВО”框、读者来信框（含“无来信”披露，在框内）、普希金肖像 + 说明、
  金句 8 条（页码 1,1,2,3,4,5,6,6）、下周预告齐全；D1 s3 已在页眉带。
- P8：A–H 栏、Q113–150、Маша阅读文、H 范文（97 词）、答案键 150 项（按页排序）齐全；页脚 `Seite 8 von 8`；
  D1 s4 已在页眉带；P8 键含 Q20 `желании`。

## §11 本版必查（D1 / D2 / D6 / kicker，`gates/gates.json`）

- D1：s1 `УЧЕБНЫЕ ДАННЫЕ` 在 text.md L459 ✓；s3 `Три уровня, три темы` L504 ✓；s4 `Большой тест недели + все ответы` L596 ✓；
  s2（免责声明）不在 text.md ✓，在 P6 SVG ✓；4 串全在 SVG（p6 s1/s2、p7 s3、p8 s4）✓。
- D2：`День студента` text.md ×11；全称 `Международный день студента` text.md ×2 = core ×2 ✓。
- D6：`желании` text.md ×2；P8 印出键 20 = `желании` = core 键 ✓（P2 SVG 计 0，预期：P2 只有题干空白，键只印在 P8）。
- Kicker：11 个 token，9 处间隙 **[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]**，最小 **5.9 px ≥ 4** ✓；
  双空格已落地（p1 SVG 节点 `'  '` ×7、`'—  '` ×1、`',  '` ×1）；kicker 真墨左 586.3、右 1363.1，均在版心内。
- D1 修法 4 处同步核实：`content12.py:48`、`text.md:25`、`map-de.json:96`、`miss-tr-de.json:33` 均为短式；
  版内 `Spieltag in Zahlen` 残留 0 处；core-ru `content12.py` SHA `1f4c42a9…8cd9` 修前修后一致。

## §12 判为非缺陷的项（附证据）

- **P2 降部候选**：框底 1159.0，末行基线 1154.0，真墨底 1158.0，**余量 +1.0 px**——无溢出（该行无降部字母）；紧但通过（§6b 未触发）。
- **P8 无莫洛兹科图/注**：与已发 W46 ru-de 同，为既定构建条件先例，非缺陷；freeze diff 的 14 个图注词删除与此一致。
- **窄字距**：HINWEIS 框内俄德词对贴紧（如 `поздравить gratulieren`）为 U+3000 分隔符 + 词形所致；P7 col 3 `может быть`、
  P5 `начинаются уже` / `заказывают несколько` 的“并词”观感，经节点核查均为独立节点且 PIL 真墨间隙真实存在
  （如 P7 y=466.4 `может` 真墨右 1072.3 → `быть` x=1077.1，间隙 4.8 px），且与 core 逐节点同位；150 dpi 渲染观感，非缺陷。
- **P4 页眉 `результатов+ сборная` 观感**：源文 `content34.py:113` 本有空格；SVG 中 `результатов` / ` ` / `+ ` 为独立节点，非缺空格。
- **P7 “гололедица, будьте” 逗号**：SVG 中逗号为独立节点，与核心一致。
- **P7 普希金肖像紧裁剪**：与核心同一图像处理，非本版问题。
- **各页中栏留白**（P2/P3/P6 中栏在练习带上方的大面积空白）：核心版式继承，非缺陷。
- **P6 图表**：38+26+18+18=100%，并以德语标明为编辑部练习调查、非真实统计——正确。
- **Q100 键 “или”**：改写题用 “или” 连接两句，语法可用，键与印出一致。
- **check_core 孤儿/碰撞各 1**：P7 `”».` 与 P1 `чёрная` 均为核心同类已知项，非缺陷；
  P1/P2/P3 的 `От редакцииLucerna` 毗邻为核心同位节点（x/y/字体/字号逐项一致），非 fanout 缺陷。
- **Q137 em-dash 提取截断**：本版提取键完整（`Dienstag, 17. November, Tag der Studierenden.`），无截断；为已知非缺陷。

## §13 回归对照（新 vs backup-old，§0 之外）

- text.md diff：恰 **14 行（7 对）**，即 L25（本次）+ L173/L187/L459/L504/L596/L694（修前 6 对），别无其他。
- SVG 文本集（x,y,文本 三元组）diff：见 §9；p3/p4/p5 完全相同。
- creambox vs backup：仅 2 行 diff（§2）。occlusion flags 与 proof2 逐项同框同值（§1）。
- 结论：无手 patch 丢失；#1 D2/D3 已修复，D1 本次已修复（§6）。

## §14 D5 字体（只记录，不判定）

- 印 PDF 字体引用 **72 个 / 69 distinct**：NotoSansCJKsc Bold/Regular、NotoSans Bold/Medium、UnifrakturMaguntia、
  NotoSerif Bold/Medium、Newsreader16pt Regular/**Italic**、NotoSerif-**MediumItalic**、NotoSerifCJKsc-Regular（×4，
  多为按页子集化重复引用）；完整清单 `evidence/d5-fonts.txt`。计数法与 fix1 的 72 引用同，与 proof2 的 65 口径不同，不作比较判定。
- 网 PDF 同系 Lucerna 前缀字体，**72 引用 / 69 distinct**，含 LucernaNewsreader-**Italic**、LucernaNotoSerif-**Italic**、
  LucernaNewsreader-Bold。
- 字体族未变；两者斜体均在（§7 斜体 3=3）。

## §15 门禁总表（16/16）

| # | 门 | 结果 |
|---|---|---|
| 1 | SHA 身份（3 件） | 全符（§0） |
| 2 | run.py scratch 副本重跑 | rc=0，TOTAL 150；再生 SVG 8/8 逐字节一致 |
| 3 | render.py scratch 再生印 PDF | rc=0；SHA 与交付印 PDF 完全相同 |
| 4 | webpdf.py scratch 重渲染 + 文字层 | rc=0；交付网/再生网/印 PDF 文字层全等 31,001 字符 |
| 5 | p8 extract | 150/150 |
| 6 | p8 compare / vs core JSON | CLEAN，keydiff [137,138,139,140] |
| 7 | keycheck 150（逐题手核） | 0 不符（Q150 除外，✓） |
| 8 | check_core.py | rc=0，golden BAD 0，gloss 0 |
| 9 | s11_check.py | rc=0，FAILURES: none；P8 最小 9.75 pt |
| 10 | occlusion audit（无 selftest）+ 裁决 | 42 TEXTX / 0 LINEX，42/42 CLEAR |
| 11 | freeze 标准口径（core-ru） | 8/8；edition-internal 补充 8/8 |
| 12 | freeze diff 西里尔删除 | 恰 15 项，unexplained 0 |
| 13 | creambox | 框内负余量 0；BELOW-WINDOW 95 全分类；vs 备份仅 2 行（标题本行） |
| 14 | 垂直溢出另扫 + Boxtitle 真墨 | 框内违规 0（62 节点全为下一标题类）；Part B 零报告 |
| 15 | D1 标题双法量测 | PIL 887.9 / 光栅 887.9，余量 +73.1，目视确认；无碰撞 |
| 16 | 回归对照（D2/D3/D6/kicker/___/文本集） | 全部存活；text.md 7 对、SVG 仅预期节点 |
| — | verify_ed.py | ru-de 无此脚本（见 §8），等效覆盖已跑 |
| — | SVG 零真实 CJK | 0；U+3000 ×123 |
| — | `___` | 87 处，模板问题，非缺陷 |

**总结论：(a) 无缺陷 0 项，可以定稿。** D1 已修好，16/16 门禁绿灯。
