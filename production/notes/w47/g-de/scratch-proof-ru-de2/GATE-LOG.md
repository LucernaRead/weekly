# GATE-LOG — 2026-W47 ru-de proof2（re-fanout 重建版，全部机械门自跑证据）

工具：`~/workspace/weekly-git/tools/venv/bin/python`；正典 creambox：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`。`TMPDIR` 全程指向本 scratch 的 `tmp/`。证据文件默认在 `gates/`，渲染在 `render/`，裁图在 `crops/`。驱动脚本 `run_gates.py`（本 scratch），裁决脚本 `adjudicate2.py`（由 #1 同名脚本仅改路径复用）。生产文件全程只读，未改动、未 commit、未 push（复校后 `git status`：ru-de 目录仍为原样 untracked，无 tracked 修改）。

## §0 身份核对

- 探针：`git hash-object -w`（`3a902dd3…`）+ scratch 真实写 OK 后开工。
- `sha256sum` 实跑：印 PDF `26bfbcd1…adad2`（21,231,822 B）、网 PDF `99173b8c…bed4ee`（3,385,962 B）、text.md `5ae444c8…a911`（63,516 B）——与任务先验全符。
- 核心对照实跑：core-ru 印 `d60fbd6c…cab81`（31,429,147 B）、网 `2f995f1d…4197`（4,025,834 B）、文 `348511e0…8cc`（60,953 B）——与任务一致。

## §1 Occlusion 审计（真实命令，未加 --selftest）

- 实跑 `tools/occlusion_audit.py <版>/svg --json gates/occlusion.json`：**42 TEXTX、0 LINEX**（rc=1 为“有 flag 即 1”，与 #1 同；另含自测行 planted 6 类全部触发，不计入 42）。
- 像素裁决（`adjudicate2.py` Part A v3，1× 网格卡片墨阈值 min-channel < 140）：**33 项像素测试 CLEAR + 9 项 400 dpi 目视 CLEAR**（`crops/flags-contact-sheet.png`）——9 项与 #1 的 9 项逐项同框同值（flag 7/8 P1、11/12 P2、20/21 P4、28/30 P6、37 P7），均为词与后随标点/引号分离字形（`Краснодаре,`、`истории!`、`студента.`×2、`Краснодар»`×2、`студента,`、`Планируйте:`、`студента!»`），touch_rows 1–4 行均为单行扫描伪影。**42/42 CLEAR，0 真重叠。**
- 注意：该审计对奶油框内溢出、框标题溢出、横向溢出、降部溢出是盲的——以下 §2、§6、§6b 另行实测，不以 occlusion 0 放过。

## §2 正典 creambox.py 全版扫描

- `gates/creambox.log`：+45 px 窗口 + 逐行 clearance 全版扫描；**框内负余量 0**；BELOW-WINDOW 95 行，全为 +28.0（×25）/+32.0（×41）/+34.0（×4）/+37.0（×25），与重建报告一致，全部归入下一标题类（与 gates.json 的 unclassified 空表一致）。
- 与 backup-old 的 creambox 扫描逐行 diff：**0 行**（`gates/creambox-vs-backup.diff` 为空）——重建零版式回归。
- P7-TOOLBOX 汇总（creambox.log 内）：3 框，框内最小余量 +11.9 px，降部余量最小 +5.9 px。

## §3 p8 compare（`tools/p8.py`）

- `gates/p8-ed.json` / `gates/p8-core.json` / `gates/p8-compare.json`：**CLEAN；150/150 noted；keydiff=[137,138,139,140]**。
- 与 core `ru-p8.json`（150 键）直接比对：keydiff 恰为 `['137','138','139','140']`。
- keydiff 逐条裁决（合法德语译文，核心中文键的正确德语替换）：
  - 137 “Dienstag, 17. November, Tag der Studierenden.”
  - 138 “Ein Paket muss verfolgt, abgeholt und geprüft werden.”
  - 139 “Am Dienstag spielt Russland gegen Venezuela.”
  - 140 “Allen einen schönen Tag der Studierenden!”
- Q150 印出键 `✓`；Q20 印出键 `желании`（= core 键）；Q25 印出键 `b`。

## §4 Freeze（标准口径 + edition-internal 补充）

- **标准口径**：`freeze.py baseline --build <core-ru 构建目录> --core-svg <core-ru/svg> --out gates/freeze-core`：**8/8 字节一致**（`gates/freeze-core-baseline.log`，rc=0），“core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)”。
- 补充（不得冒充前者）：`freeze.py baseline --build <版> --core-svg <版>/svg --out gates/freeze`：亦 8/8；两基线 SVGs 相同，build-copy 差异仅为版自有文件 vs 核心自有文件（预期）。
- `freeze.py diff --core-svg core-ru/svg --edition-svg <版>/svg`（`gates/freeze-diff.json`，rc=0）：removed **851（distinct 486）**；西里尔删除恰 **15 项**，全部在 P8：`Билибин、Билибина、Зимняя、Иван、Ивана、Иллюстрация、Морозко、год、достояние、иллюстрация、к、можно、ноябрю、общественное、сказка` 各 ×1 = Q46 `можно` + 14 个 Morozko 图注词（图按设计跳过），unexplained 0；新增 CJK 仅 U+3000 ×8。

## §5 Keycheck 150/150

- `gates/keycheck-150.json`：编号 1–150 连续；P8 印出键 150 项；与 text.md 答案键 **0 不符 / 149**（Q150 印 ✓，属设计；范文 97 词，实数，80–100 要求内）；分级 A2 50 / B1 76 / B2 24；分面 Ankreuzen 55 / Ausfüllen 54 / Zuordnen 20 / Sätze bilden 12 / Umformen 4 / Übersetzen 4 / Schreiben 1；P1 10、P2 18、P3 18、P4 18、P5 18、P6 18、P7 12、P8 38。
- 逐题手验：每题对照题干/正文/表格核对（逐项手核记录在 keycheck-150.json 的 `hand_note` 栏）；重点项——Q20 `желании`（前置格，#1 的 `желание` 已改正）、Q25 b 短式、Q33 键 A（11 月 26 日）、Q54 键 2:0 与 Q59 键 c（P4 赛果表）、Q56 键 20:45（P4 更正框）、Q73 `заказов`（миллиона后复数第二格，文中原句一致）、Q137–140 翻译键、Q150 范文 97 词。
- 配对块：P2 D、P3 C、P4 C、P5 C、P8 F 逐组对照 SVG 选项原文核对（字母为独立节点，逐行提取验证；P3 a、P4/P5 选项另经整页渲染目视确认）——均无误。
- P8 对话 Q145–149 键 A/B/B/A/B 与购物对话语境一致。

## §6 Boxtitle 逐个真墨实测（PIL，`adjudicate2.py` Part B v2，不只看 advance）

- 方法：各页最小包含奶油框 + 内容缘 1862 / 页缘 1950；`OA.ink_box` 真墨为准。
- **D1（本轮唯一缺陷）**：P1 标题 `ТУР В ЦИФРАХ　Der Spieltag in Zahlen`（x=727 y=1241 size=23）真墨右缘 **997.6 px**，框右缘 961.0 → **+36.6 px**（`crops/d1-p1-subtitle.png` 400 dpi 目视确认：盒缘切过 “Zahlen”）。
- 其余：**零报告**——无过内容缘、无过页缘、无过奶油盒。#1 D2 已消失（P2 y=2162 现为 `День студента`，`crops/d2-p2-matchline.png` 目视确认行尾在栏内）。

## §6b 垂直溢出另扫（spill sweep：基线落盒外整行 + 填色无描边盒溢出）

- 自写扫描（`gates/vertical-spill.log`）：每节点取最小包含奶油框（`#f0eee5`），量墨顶/墨底/基线 vs 框上下缘。
- 报告 62 个节点，**全部**为基线在框底之下 +28.0/+32.0/+34.0/+37.0 的下一节标题行（P1 `СЕЙЧАС ВЫ`/`СЛОВО НЕДЕЛИ`、P2 `ЧТО ПОЖЕЛАТЬ?`/`Запомните…`、P3 `А ЧТО УЖЕ В КИНО?`、P5 `А ЧТО С 11.11?`、P6 日历图例）——与 §2 的 95 BELOW-WINDOW 行同一类，按设计在框外，不为溢出。
- **框内墨底违规 0、墨顶违规 0、墨底超页底 0**。#1 P2 降部候选（“Studenten, einen für Väterchen Frost.” 基线 1154.0、框底 1159.0）本次未触发：真墨底 1158.0，余量 +1.0 px，通过。

## §7 印/网文字层比对 + D3 复核

- PyMuPDF：印/网均为 8 页；非空白字符 multiset **全等（总体 + 逐页 8/8），31,009 字符**；网 PDF 3,385,962 B < 7 MB。网 PDF 未重渲染生产文件（只在 scratch 渲染比对）。
- **斜体清单**：印 PDF 恰 3 处斜体跨度，全在 P1（`«` Newsreader Italic、`чёрная пятница` NotoSerif-MediumItalic、`»`）；**网 PDF 亦 3 处**（LucernaNewsreader-Italic / LucernaNotoSerif-Italic / LucernaNewsreader-Italic）——#1 D3 已修好。
- 闭引号：`пятница»` 印/网各 7 处，脱离式 `пятница »` 0 处；`14-й` 印/网各 5 处，`14- й` 0 处。网版 P1 导读 `crops/d3-p1-web-standfirst.png` 目视：`«чёрная пятница»` 呈斜体、» 紧贴。
- P8 最小字号（PyMuPDF 实测印 PDF）：**9.75 pt**（全刊最小亦 9.75 pt）；符合 SOP §1.1 下限。

## §8 check_core.py / s11_check.py / verify_ed.py

- `check_core.py <版>`（cwd=版目录，首次误无参调用 rc=1 已纠正为带参重跑）：**rc=0**；golden BAD **0**、gloss fails **0**；orphan line-starts 1（P7 y553 `”».`，已知良性，与核心同类）；same-baseline collision 1（P1 y1712 `чёрная`，与核心同）。日志 `gates/check_core.log`。
- `s11_check.py <版>`：**rc=0**，`FAILURES: none`；8 SVG、纸色 `#fbfaf6`、徽章色、VOL.4 家具、左缘 ≥ 87、无拉丁版 CJK 均 PASS（`gates/run.log` 的 s11 节；注：run.log 里 “s11 FAIL lines: ['FAILURES: none']” 是我方收集脚本的误标——该行本身即“零失败”）。
- **verify_ed.py**：ru-de 不存在此脚本——`scratch-fanout-ru/` 与版目录均无 `verify_ed*.py`；已有的 `verify_ed.py` 均为 en-core 系，核查 en 专属项（Ashes Q39/40 等），不适用于 ru 版。等效覆盖已由 check_core（rc=0）+ s11_check（rc=0）+ keycheck-150（0 不符）+ p8 compare（CLEAN）提供；此处如实记录，不冒充运行。

## §9 text.md / SVG 检查

- text.md：150 答案、无缺失；行内键 129 项与答案节一致（keycheck 脚本核对）；`___` 字面 **87 处**，全在填空题干中，核心继承的模板缺口，依任务裁定不作本版缺陷、不逐版修。
- SVG：零真实 CJK（`[\u3400-\u9fff\u3040-\u30ff]` 扫描，可见文本），U+3000 ×123（家具分隔符）；弯引号 « » 各页平衡、零直引号（与 #1 同，SVG 文本集 p3/p4/p5 与备份完全相同，p1/p2/p6/p7/p8 差异仅为本版必查节点）。
- D5 字体（只记录不判定）：见 §14。

## §10 全页目视（150 dpi 整页渲染 `render/p1–p8-print.png` + 网 P1）

- P1：刊头、条带、标题带、导读、统计框（D1 可见）、目录页码锚、词框、照片 + CC0 说明、短讯框、测验 Q7–Q10、页脚 `Seite 1 von 8`——余皆干净。
- P2：尤恩画 + 说明在位；节假日表、“А ВЫ?” 框、词汇四框、练习 A–D 齐全；Q25 选项 b 已缩短。
- P3：三栏正文、HINWEIS 词注框、右栏两框、练习 A–D（Q29–46）齐全；无图（按设计）。
- P4：1912 年照片 + 说明、VOL.3 更正框、赛果表 8 场、国家队栏、15 轮赛程表、TOP-5 表、练习 A–D（Q47–64）齐全。
- P5：市场玉米照 + 说明、黑五日期框、练习 A–D（Q65–82）齐全；德语标题引号为 „ “，正确。
- P6：日历条（16 пн…22 вс，21–22 高亮）、练习数据图（38+26+18+18=100%，标明为练习数据）、“ЗА И ПРОТИВ”框、练习 A–D（Q83–100）齐全；D1 s1 标题已落地一行内。
- P7：三栏 A2/B1/B2、错题诊所四条（均在框内）、“СЛОВО”框、读者来信框（含“无来信”披露，在框内）、普希金肖像 + 说明、金句 8 条（页码 1,1,2,3,4,5,6,6）、下周预告齐全；D1 s3 已在页眉带。
- P8：A–H 栏、Q113–150、Маша阅读文、H 范文（97 词）、答案键 150 项（按页排序）齐全；页脚 `Seite 8 von 8`；D1 s4 已在页眉带；P8 键含 Q20 `желании`。

## §11 本版必查（D1 / D2 / D6 / kicker，`gates/gates.json`）

- D1：s1 `УЧЕБНЫЕ ДАННЫЕ` 在 text.md L459 ✓；s3 `Три уровня, три темы` L504 ✓；s4 `Большой тест недели + все ответы` L596 ✓；s2（免责声明）不在 text.md ✓，在 P6 SVG ✓；4 串全在 SVG（p6 s1/s2、p7 s3、p8 s4）✓。
- D2：`День студента` text.md ×11；全称 `Международный день студента` text.md ×2 = core ×2 ✓。
- D6：`желании` text.md ×2；P8 印出键 20 = `желании` = core 键 ✓（P2 SVG 计 0，预期：P2 只有题干空白，键只印在 P8）。
- Kicker：11 个 token，9 处间隙 **[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]**，最小 **5.9 px ≥ 4** ✓；双空格已落地（p1 SVG 节点 `'  '` ×7、`'—  '` ×1、`',  '` ×1）。

## §12 判为非缺陷的项（附证据）

- **P2 降部候选**：框底 1159.0，末行基线 1154.0，真墨底 1158.0，**余量 +1.0 px**——无溢出（该行无降部字母）；紧但通过（§6b 未触发）。
- **P8 无莫洛兹科图/注**：与已发 W46 ru-de 同，为既定构建条件先例，非缺陷；freeze diff 的 14 个图注词删除与此一致。
- **窄字距**：HINWEIS 框内俄德词对贴紧（如 `поздравить gratulieren`）为 U+3000 分隔符 + 词形所致；#1 已用 400 dpi 裁图证实词间有空隙，SVG 节点与备份相同；全版 P1 目视无并词。
- **P7 “гололедица, будьте” 逗号**：SVG 中逗号为独立节点，与核心一致。
- **P7 普希金肖像紧裁剪**：与核心同一图像处理，非本版问题。
- **各页中栏留白**（P2/P3/P6 中栏在练习带上方的大面积空白）：核心版式继承，非缺陷。
- **P6 图表**：38+26+18+18=100%，并以德语标明为编辑部练习调查、非真实统计——正确。
- **Q100 键 “или”**：改写题用 “или” 连接两句，语法可用，键与印出一致。
- **check_core 孤儿/碰撞各 1**：P7 `”».` 与 P1 `чёрная` 均为核心同类已知项，非缺陷。
- **Q137 em-dash 提取截断**：本版提取键完整（`Dienstag, 17. November, Tag der Studierenden.`），无截断；为已知非缺陷。

## §13 回归对照（新 vs backup-old，§0 之外）

- text.md diff：恰 **12 行（6 对）**，即 L173/L187/L459/L504/L596/L694，别无其他。
- SVG 文本集（x,y,文本 三元组）diff：p3/p4/p5 完全相同；p1 仅 kicker 双空格重排（20 节点，x 平移）；p2 仅 Q25 b 行 5 节点 → 3 节点；p6 仅 D1 s1 + 免责声明俄语段（2 → 24 节点）；p7 仅 D1 s3（5 → 13 节点）；p8 仅 Q20 键 + D1 s4（7 → 17 节点）。
- creambox vs backup：0 行 diff（§2）。occlusion flags 与 #1 逐项同框同值（§1）。
- 结论：无手 patch 丢失；#1 D2/D3 已修复，D1 未修复（PROOF-NOTE 缺陷清单）。

## §14 D5 字体（只记录，不判定）

- 印 PDF 字体引用 65 个：NotoSansCJKsc Bold/Regular、NotoSans Bold/Medium、UnifrakturMaguntia、NotoSerif Bold/Medium、Newsreader16pt Regular/**Italic**、NotoSerif-**MediumItalic**、NotoSerifCJKsc-Regular（多为按页子集化重复引用）。
- 网 PDF 同系 Lucerna 前缀字体，含 LucernaNewsreader-**Italic**、LucernaNotoSerif-**Italic**、LucernaNewsreader-Bold。
- 字体族未变；两者斜体均在（§7）。

## §15 门禁总表

| 门 | 结果 |
|---|---|
| SHA 身份（3 件 + core 3 件） | 全符 |
| p8 extract / compare / vs core JSON | 150/150，CLEAN，keydiff [137,138,139,140] |
| keycheck 150（手核） | 0 不符（Q150 除外，✓） |
| check_core.py | rc=0，golden BAD 0，gloss 0 |
| s11_check.py | rc=0，FAILURES: none；P8 最小 9.75 pt |
| verify_ed.py | ru-de 无此脚本（见 §8），等效覆盖已跑 |
| occlusion audit（无 selftest） | 42 TEXTX / 0 LINEX，42/42 CLEAR |
| freeze 标准口径（core-ru） | 8/8；edition-internal 补充 8/8 |
| freeze diff 西里尔删除 | 恰 15 项，unexplained 0 |
| 印/网文字层 | multiset 全等（总体 + 逐页），31,009 字符 |
| 斜体（D3 复核） | 印 3 = 网 3；» 无脱离 |
| creambox | 框内负余量 0；BELOW-WINDOW 95 全分类；vs 备份 0 diff |
| 垂直溢出另扫 | 框内违规 0（62 节点全为下一标题类） |
| Boxtitle PIL 真墨 | **1 项溢出：P1 D1 +36.6 px** |
| SVG 零真实 CJK | 0；U+3000 ×123 |
| D1 / D2 / D6 / kicker | 全部落地（§11） |
| `___` | 87 处，模板问题，非缺陷 |
| 全页目视 P1–P8 | 除 D1 外干净 |
| 回归对照（#1 备份） | 仅 6 行对 + 本版必查节点；无丢失 |

**总结论：(b) 有缺陷 1 项（中，P1 D1），不能定稿。**其余门全部通过。
