# GATE-LOG — Lucerna Weekly 2026-W47 · ru-it · proof1（re-fanout 重建版）

复校员：独立子代理，会话 `f84a995f-048c-4872-943e-4da771dfdcde`，2026-11-11。全部机械门均为本人实跑，不信 KIT，只信自跑结果。工具：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；正典 creambox：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`。`TMPDIR` 全程指向本 scratch 的 `tmp/`。证据文件默认在 `gates/`，渲染在 `render/`，裁图在 `crops/`。驱动脚本 `run_gates.py`（本 scratch，由 ru-de proof2 同名脚本改路径复用，check_core 调用已修正为带版目录参数）、裁决脚本 `adjudicate2.py`、横扫脚本 `spill.py`、补充脚本 `extra_gates.py`（均在本 scratch）。生产文件全程只读，未改动、未重建、未提交、未推送任何源文件；网 PDF 只在 scratch 渲染比对，绝未覆盖交付件（复校后 `git status`：生产目录仍为原样 untracked，无 tracked 修改）。

## §0 身份核对

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0；scratch 真实写 OK 后开工。
- `sha256sum` 实跑：印 PDF `c69b7bdf…28359b`（21,265,865 B）、网 PDF `91028029…60afd`（3,384,095 B）、text.md `ac9636b9…10d1`（64,014 B）——与任务先验全符（`gates/gates.json`）。
- 核心对照实跑：core-ru 印 `d60fbd6c…cab81`（31,429,147 B）、网 `2f995f1d…4197`（4,025,834 B）、文 `348511e0…8cc`（60,953 B）——与任务一致。

## §1 run.py 重建（scratch 副本）

- 版目录复制到 `rebuild/`（不含 cards），`tools/venv/bin/python run.py`（`gates/run-rebuild.log`）：**rc=0，TOTAL 150**，by level A2 50 / B1 76 / B2 24，by page {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}，by type {Completare 54, Scelta multipla 55, Abbinamento 20, Frasi 12, Trasformazione 4, Traduzione 4, Composizione 1}；日志中 overflow/warn/exceed/too long/clipped 命中 **0 行**。
- 重建 SVG vs 在盘 SVG 逐字节比对（`gates/svg-ondisk.sha256`）：**8/8 OK**。
- P8 末行：`P8 morozko SKIPPED: no room (col 3 y 2303.53)`——按设计跳过，与 W46 ru-it 同。

## §2 遮挡审计（occlusion audit，真实命令，未加 --selftest）

- 实跑 `tools/occlusion_audit.py <版>/svg --json gates/occlusion.json`：自测先行——planted 6 类全部触发，干净对照静默；**42 TEXTX、0 LINEX、0 COVER / FOOTER / EDGE / BOXTITLE**（rc=1 为“有 flag 即 1”）。
- 像素裁决（`adjudicate2.py` Part A v3，1× 网格卡片墨阈值 min-channel < 140）：**33 项像素测试 CLEAR + 9 项 REAL?**（flag 7/8 P1、11/12 P2、20/21 P4、28/30 P6、37 P7），touch_rows 1–4 行，均为词与后随标点/引号分离字形（`Краснодаре,`、`истории!`、`студента.`×2、`Краснодар»`×2、`студента,`、`Планируйте:`、`студента!»`）。
- 9 项再测：`gapcheck.py` 逐像素列间隙（`gates/gapcheck.log`）+ 6×（≈432 dpi）裁图逐项目视（`crops/f07-p1.png` … `crops/f37-p7.png`，由印 PDF 直接渲染）：9/9 词与标点清晰分离，无接触。**42/42 CLEAR，0 真重叠。**
- 注意：该审计对奶油框内溢出、框标题溢出、横向溢出、降部溢出是盲的——以下 §3、§6、§7 另行实测，不以 occlusion 0 放过。

## §3 正典 creambox.py 全版扫描

- `gates/creambox.log`：+45 px 窗口 + 逐行 clearance 全版扫描；**框内负余量 0**；BELOW-WINDOW 95 行，全为 +28.0（×17）/+32.0（×26）/+34.0（×3）/+37.0（×16）+（与 §7 横扫的 62 节点同类，两工具口径差为行 vs 节点），全部归入下一标题类（unclassified 空表）。
- 与 backup-old 的 creambox 扫描逐行 diff：**0 行**（`gates/creambox-vs-backup.diff` 为空）——重建零版式回归。
- P7-TOOLBOX 汇总（creambox.log 内）：3 框，框内最小余量 +11.9 px，降部余量最小 +5.9 px。

## §4 p8 compare（`tools/p8.py`，直接读 `gates/p8-compare.json` 本体）

- `gates/p8-compare.json`：**status CLEAN**，core_count=150，edition_count=150，missing=[]，extra_count=null（JSON 内无此键；stdout 同为 extra_count=0），**keydiff=[137, 138, 139, 140]**。
- 与 core `ru-p8.json`（150 键）直接比对：keydiff 恰为 `['137','138','139','140']`。
- keydiff 逐条裁决（合法意大利语译文，核心俄语键的正确意语替换，已逐句核对原文）：
  - 137 “Martedì 17 novembre, Giorno degli studenti.”（← Во вторник, 17 ноября, — День студента.）
  - 138 “Un pacco va tracciato, ritirato e controllato.”（← Посылку нужно отследить, получить и проверить.）
  - 139 “Martedì la Russia gioca contro il Venezuela.”（← Во вторник сборная России играет с Венесуэлой.）
  - 140 “Buon Giorno degli studenti a tutti!”（← Поздравляю с Днём студента!；`a tutti` 为问候自然扩展，与德语版同式）
- Q150 印出键 `✓`；Q20 印出键 `желании`（= core 键）；Q25 印出键 `b`；Q73 印出键 `заказов`；Q46 印出键 `Вечером можно посмотреть фильм в кино.`。

## §5 keycheck 150/150（手验）

- 文件：`keycheck-150.json`（构建脚本 `build_keycheck.py`；题干与键自 text.md 机械抽取——答案节 150 键、练习节 150 题干，零缺失；verdict 为本轮 fresh 手验结果，非沿用首轮）。
- **149 ok，1 开放题（#150，按设计）**，0 错误。
- 印 P8 答案 vs text.md 答案机械比对（`run_gates.py` keycheck 节）：150 答案，mismatch（除 150 外）= **[]**；Q150 印 `✓`，范文 97 词（实数，80–100 要求内）。
- 手验依据（每题对照题干/正文/表格核对；重点项见 `keycheck-150.json` 的 `hand_checks` 栏）：P4 赛果表 8 场进球和 SVG 原文重算 1+3+1+6+2+3+4+1=**21**；Q52–60、Q64 逐行对表；Q20 前置格 `желании`；Q25 短式 `День студента`；Q73 `заказов`（14,4 млн后复数第二格）；Q86/87 对图 26/18；Q101/102/104 与 Q16/17/18 题干相同（P7 A2 天气词复习，故意螺旋重复），键相同，均已核对；Q137–140 逐句核对；Q145–149 对话键 A/B/B/A/B 与购物对话语境一致。
- 配对块（`gates/pairing3.log`，SVG 选项原文逐组核对，字母为独立节点）：P2 D 25→b, 26→d, 27→c, 28→a；P3 C 39→b, 40→d, 41→c, 42→a；P4 C 57→b, 58→a, 59→c, 60→d；P5 C 75→d, 76→b, 77→a, 78→c；P8 F 141→c, 142→d, 143→a, 144→b——**均无误**。

## §6 Boxtitle 逐个真墨实测（PIL，`adjudicate2.py` Part B v2，不只看 advance）

- 方法：各页最小包含奶油框 + 内容缘 1862 / 页缘 1950；`OA.ink_box` 真墨为准。
- **P1 统计框标题** `ТУР В ЦИФРАХ　IN CIFRE`（x=726.6 节点，y=1240.735，size=23，bold）：4 个节点真墨分别为 ТУР→600.5、В→620.5、ЦИФРАХ→722.9、`　IN CIFRE`→**845.6 px**；奶油盒 x=538.5、y=1203.735、宽 422.5（右缘 961.0）→ **余量 +115.4 px，未溢出**。核心同位置标题真墨右缘 864.6（余量 +96.4）；右邻栏 x=989，空隙 143.4 px。**ru-de D1（+36.6）未复现**；与首轮实测值 845.6 完全一致，无回归。裁图 `crops/p1-statbox.png` 目视确认标题稳在盒内。
- 其余：**零报告**——无过内容缘、无过页缘、无过奶油盒。首轮 D2（P2 Q11b）已消失。
- P2 `per Nonno Gelo.`（O1）：真墨迹底 **1158.48** vs 框底 1159.0，余量 **+0.52 px**（与首轮及首轮备份值完全相同）；裁图 `crops/p2-nonnogelo-boxbottom.png` 目视：降部贴框边、未跨出。

## §7 垂直溢出横扫（`spill.py`，逐页扫基线在盒外的行与纯填充盒的横向溢出）

- 方法：每节点取最小包含奶油框（`#f0eee5`），量墨顶/墨底/基线 vs 框上下缘；纯填充盒另查右缘/底缘 vs 页缘。
- 结果（`gates/vertical-spill.log`）：**V-BOT=0、V-TOP=0、V-PAGE-BOT=0，纯填充盒越页 0**；V-BASE-BELOW=62 个节点，间隙直方图 {28.0: 17, 32.0: 26, 34.0: 3, 37.0: 16}——**全部为基线在框底之下 +28/+32/+34/+37 的下一节标题行**（P1 `СЕЙЧАС ВЫ`/`СЛОВО НЕДЕЛИ`、P2 `ЧТО ПОЖЕЛАТЬ?`、P3 `А ЧТО УЖЕ В КИНО?`、P5 `А ЧТО С 11.11?`、P6 日历图例等），与 §3 的 95 BELOW-WINDOW 行同一类，按设计在框外，不为溢出。**框内墨底违规 0、墨顶违规 0**。

## §8 印/网文字层比对 + D1（斜体）复核

- PyMuPDF：印/网均为 8 页；非空白字符 multiset **全等（总体 + 逐页 8/8），30,923 字符**；网 PDF 3,384,095 B < 7 MB。
- **斜体清单**：印 PDF 恰 3 处斜体跨度，全在 P1（`«` Newsreader16pt-Italic、`чёрная пятница` NotoSerif-MediumItalic、`»` Newsreader16pt-Italic）；**网 PDF 亦 3 处**（LucernaNewsreader-Italic / LucernaNotoSerif-Italic / LucernaNewsreader-Italic），bbox 与印版逐字相同——**首轮 D1 已修好**。
- 网 span 文本 `чёрная пятница`（带空格）；闭引号：印/网 `»` x0=1220.6 均紧贴斜体词尾（x1=1222.8，压入 2.2 pt，同形），无脱离。印/网 P1 斜体裁图 `crops/p1-italic-print.png` 与 `crops/p1-italic-web.png` **字节一致**（sha256 相同）。
- P8 最小字号（PyMuPDF 实测印 PDF）：**9.75 pt**（全刊最小亦 9.75 pt）；符合 SOP §1.1 下限。

## §9 freeze（标准口径 + edition-internal 补充）

- **标准口径**：`freeze.py baseline --build <core-ru 构建目录> --core-svg <core-ru/svg> --out gates/freeze-core`：**8/8 字节一致**（`gates/freeze-core-baseline.log`，rc=0），“core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)”。
- 补充（不得冒充前者）：`freeze.py baseline --build <版> --core-svg <版>/svg --out gates/freeze`（`run_gates.py` 内跑）：亦 **8/8**；两基线一致。
- `freeze.py diff --core-svg core-ru/svg --edition-svg <版>/svg`（`gates/freeze-diff.json`，rc=0）：removed **848（distinct 482）**；西里尔删除恰 **15 项**，全部在 P8：`Билибин、Билибина、Зимняя、Иван、Ивана、Иллюстрация、Морозко、год、достояние、иллюстрация、к、можно、ноябрю、общественное、сказка` 各 ×1 = Q46 `можно` + 14 个 Morozko 图注词（图按设计跳过）；新增 CJK 仅 U+3000 ×8。

## §10 check_core.py / s11_check.py / verify_ed.py

- `check_core.py <版>`：**rc=0**；GOLDEN: 8，golden BAD **0**、gloss fails **0**；orphan line-starts 1（P7 y553 `”».`，已知良性，与核心同类）；same-baseline collision 1（P1 y1712 `чёрная`，与核心同）。日志见 `gates/run.log` 的 check_core 节。
- `s11_check.py <版>`：**rc=0**，`FAILURES: none`；8 SVG、纸色 `#fbfaf6`、徽章色 A2/B1/B2、VOL.4 家具、左缘 88.0 ≥ 87、masthead 196px、band title 46px、无拉丁版 CJK、网 PDF 8 页 < 7 MB、有文字层、P8 最小 9.75 pt 均 PASS（`gates/run.log` 的 s11 节；注：run.log 里 “s11 FAIL lines: ['FAILURES: none']” 是收集脚本的误标——该行本身即“零失败”）。
- **verify_ed.py**：ru-it 不存在此脚本——版目录与 fanout 工作区均无 `verify_ed*.py`；已有的 `verify_ed.py` 均为 en-core 系，核查 en 专属项，不适用于 ru 版。等效覆盖已由 check_core（rc=0）+ s11_check（rc=0）+ keycheck-150（0 不符）+ p8 compare（CLEAN）提供；此处如实记录，不冒充运行。

## §11 text.md / SVG 检查

- text.md：838 行；150 答案、无缺失；行内键 129 项与答案节一致（keycheck 脚本核对）；`___` 字面 **87 处**，全在填空题干中，核心继承的模板缺口，依任务裁定不作本版缺陷、不逐版修。
- SVG：零真实 CJK（`[\u3400-\u9fff\u3040-\u30ff]` 扫描，可见文本），U+3000 ×123（家具分隔符）；弯引号 « » 各页平衡（199/199）、零直引号；弯双引号 “ ” 仅 P7 一对（`на “чёрной пятнице”`，故意保留的例外）；直撇号 ×9 全为意大利语省音（`l'anno scorso`、`l'ultima`、`dell'anno`、`DELL'ESERCIZIO`、`l'8 novembre`、`dell'infanzia`、`all'83°`、`d'inizio`、`l'Orenburg`）。
- 可见文本禁词扫描：`2026-w47` / `ru-it` / `W47` / `cover` / `SOP` / `lint` / `proofread` / `翻譯` / `翻译` / `github` 均为 0；`VOL.4` ×9 为刊头/页脚印刷家具（SOP §1.1 要求），非内部标签。
- text.md：`«` / `»` 各 165，`“` / `”` 各 1，U+2019 为 0，**0 个 CJK 字符**，无 `翻譯`/`翻译`；E 节标签为意大利语：`Traduzione`、`[Traduci in italiano]`。
- `ABSTRACT.txt`：391 字节，意大利语，点名真实 W47 话题 + VOL.4 + A2–B2 + 150 题，无 ASCII 双引号。
- `— СТРАНИЦА ? —` 分隔符：core 与本版 text.md 各 ×1（导出器格式，继承，非缺陷）；P1 moth `<title>` 元数据内 `三色蛾` 为非可见文本（与 core 相同）。

## §12 本版必查（D1 / D2 / D6 / kicker，`gates/gates.json`）

- D1：s1 `УЧЕБНЫЕ ДАННЫЕ` 在 text.md L459 ✓；s3 `Три уровня, три темы` L504 ✓；s4 `Большой тест недели + все ответы` L596 ✓；s2（免责声明）不在 text.md ✓，在 P6 SVG ✓；4 串全在 SVG（p6 s1/s2、p7 s3、p8 s4）✓。
- D2：`День студента` text.md ×11；全称 `Международный день студента` text.md ×2 = core ×2 ✓；P2 SVG 选项 b 行 5 节点 → 3 节点（缩短后）。
- D6：`желании` text.md ×2；P8 印出键 20 = `желании` = core 键 ✓（P2 SVG 计 0，预期：P2 只有题干空白，键只印在 P8）。
- Kicker：11 个 token，9 处间隙 **[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]**，最小 **5.9 px ≥ 4** ✓；双空格已落地。

## §13 回归对照（新 vs backup-old，§0 之外）

- text.md diff：恰 **12 行（6 对）**，即 L173（D6 键）、L187（D2 选项）、L459/L504/L596（D1 标题）、L694（D6 键表），别无其他——**无事实行被改动**，首轮外部核实继续覆盖。
- SVG 文本集 diff（未逐字节跑，creambox 逐行 diff 为 0 行 + 关键节点逐项核对）：p1 kicker 双空格重排、p2 Q25 b 缩短、p6 D1 s1 + 免责声明俄语段、p7 D1 s3、p8 Q20 键 + D1 s4——与 de2 同批重建的节点清单一致，无手 patch 丢失。
- creambox vs backup：0 行 diff（§3）。occlusion flags 与首轮逐项同框同值（§2）。
- 结论：无手 patch 丢失；首轮 D1/D2 已修复，ru-de D1 在本版从未存在。

## §14 D5 字体（只记录，不判定）

- 印 PDF 字体引用 73 个：含 Newsreader16pt-Italic、NotoSerif-MediumItalic（`gates/extra.json` 的 `fonts_print` 全表）。
- 网 PDF 字体引用 73 个：同系 Lucerna 前缀字体，含 LucernaNewsreader-Italic、LucernaNotoSerif-Italic（`fonts_web` 全表）。
- 字体族未变；两者斜体均在（§8）。

## §15 全页目视（150 dpi 整页渲染 `render/p1–p8-print.png` + 网 P1）

- P1：刊头、kicker、标题带、导读、统计框（标题稳在盒内）、目录页码锚、词框（斜体）、照片 + CC0 说明、短讯框、测验 Q7–Q10、页脚 `Pagina 1 di 8`——余皆干净。
- P2：尤恩画 + 说明在位；节假日表、“А ВЫ?” 框、词汇四框、练习 A–D 齐全；Q25 选项 b 已缩短；中栏留白为核心版式。
- P3：三栏正文、NOTA 词注框、右栏两框、练习 A–D（Q29–46）齐全；无图（按设计）。
- P4：1912 年照片 + 说明、VOL.3 更正框、赛果表 8 场、国家队栏、15 轮赛程表、TOP-5 表、练习 A–D（Q47–64）齐全。
- P5：市场玉米照 + 说明、黑五日期框、练习 A–D（Q65–82）齐全；标题引号为 « »，正确。
- P6：日历条（16 пн…22 вс，21–22 高亮）、练习数据图（38+26+18+18=100%，标明为练习数据）、“ЗА И ПРОТИВ”框、练习 A–D（Q83–100）齐全；D1 s1 标题已落地一行内。
- P7：三栏 A2/B1/B2、错题诊所四条（均在框内）、“СЛОВО”框、读者来信框（含“无来信”披露，在框内）、普希金肖像 + 说明、金句 8 条（页码 1,1,2,3,4,5,6,6）、下周预告齐全；D1 s3 已在页眉带。
- P8：A–H 栏、Q113–150、Маша阅读文、H 范文（97 词）、答案键 150 项（按页排序）齐全；页脚 `Pagina 8 di 8`；D1 s4 已在页眉带；P8 键含 Q20 `желании`。

## §16 判为非缺陷的项（附证据）

- **42 TEXTX 全部裁决 CLEAR**（§2：字体度量假象，有逐像素间隙 + 6× 裁图目视）。
- creambox 全部负余量均为下一标题假阳性，框内余量健康（§3、§7）。
- P2 `per Nonno Gelo.` 降部：真墨迹余量 +0.52 px，未跨框（§6；O1，值与首轮及备份完全相同）。
- P3 中部大面积空白（第 2–4 栏，y≈1100–1600）：文章短，留白，核心版式（O2）。
- `— СТРАНИЦА ? —`：core 亦有，导出器格式（§11）。
- moth `三色蛾`：仅 P1 `<title>` 元数据，非可见文本（§11）。
- P8 最小字号 9.75 pt：正在 SOP §1.1 下限，可接受（§8）。
- P7 弯引号一对：故意保留的例外（§11）。
- ABSTRACT.txt 391 字节：意大利语，内容正确（§11）。
- P8 «Морозко» 图缺席：build 条件跳过，与 W46 ru-it 相同，按设计（§1）。
- 字面 `___` 空白（87 处）：模板级，核心继承（§11）。
- 西里尔-拉丁 gloss 交界处 4–6 px 窄词距：U+3000 分隔符 + 词形所致，渲染目视有空隙，与 core 相同（O3）。
- Q100 键 `или`：改写题用 `или` 连接两句，语法可用，键与印出一致（§5）。
- Q140 意译添 `a tutti`：问候自然扩展，与德语版同式（§4）。
- check_core 孤儿/碰撞各 1：P7 `”».` 与 P1 `чёрная` 均为核心同类已知项（§10）。

## §17 门禁总表

| 门 | 结果 |
|---|---|
| SHA 身份（3 件 + core 3 件） | 全符 |
| run.py（scratch 副本） | rc=0，TOTAL 150，0 溢出；重建 SVG 8/8 字节一致 |
| p8 extract / compare / vs core JSON | 150/150，CLEAN，keydiff [137,138,139,140]（直接读 p8-compare.json 本体） |
| keycheck 150（手核） | 0 不符（Q150 除外，✓）；范文 97 词 |
| check_core.py | rc=0，golden BAD 0，gloss 0 |
| s11_check.py | rc=0，FAILURES: none；P8 最小 9.75 pt |
| verify_ed.py | ru-it 无此脚本（见 §10），等效覆盖已跑 |
| occlusion audit（无 selftest） | 42 TEXTX / 0 LINEX，42/42 CLEAR |
| freeze 标准口径（core-ru） | 8/8；edition-internal 补充 8/8 |
| freeze diff 西里尔删除 | 恰 15 项（Q46 + 14 图注词） |
| 印/网文字层 | multiset 全等（总体 + 逐页），30,923 字符 |
| 斜体（D1 复核） | 印 3 = 网 3，同 bbox；» 无脱离；印网裁图字节一致 |
| creambox | 框内负余量 0；BELOW-WINDOW 95 全分类；vs 备份 0 diff |
| 垂直溢出横扫 | V-BOT/V-TOP/V-PAGE-BOT 均为 0（62 节点全为下一标题类） |
| Boxtitle PIL 真墨 | **零报告**；P1 标题余量 +115.4 px（ru-de D1 未复现） |
| SVG 零真实 CJK | 0；U+3000 ×123 |
| D1 / D2 / D6 / kicker | 全部落地（§12） |
| `___` | 87 处，模板问题，非缺陷 |
| 全页目视 P1–P8 | 干净 |
| 回归对照（首轮备份） | 仅 6 行对 + 本版必查节点；无丢失 |

**总结论：(a) 零缺陷，可定稿。**其余门全部通过。

## §18 交付文件（scratch）

- `PROOF-NOTE.md`（结论 (a)，零缺陷）
- `GATE-LOG.md`（本文件）
- `keycheck-150.json`（150 题逐题手验；构建脚本 `build_keycheck.py`）
- 驱动/裁决脚本：`run_gates.py`、`adjudicate2.py`、`spill.py`、`extra_gates.py`、`gapcheck.py`
- 证据：`gates/gates.json`、`gates/run.log`、`gates/run-rebuild.log`、`gates/svg-ondisk.sha256`、`gates/occlusion.json`、`gates/adjudicate2.txt`、`gates/gapcheck.log`、`gates/creambox.log`、`gates/creambox-vs-backup.diff`、`gates/p8-compare.json`、`gates/p8-ed.json`、`gates/p8-core.json`、`gates/freeze-core-baseline.log`、`gates/freeze-diff.json`、`gates/vertical-spill.log`、`gates/extra.json`、`gates/pairing.log`、`gates/pairing3.log`、`gates/misc.log`、`gates/nonnogelo.log`、`render/p1–p8-print.png`、`render/p1-web.png`、`crops/`（9 项 TEXTX 裁图、p1-statbox、p1-italic-print/web、p2-q25b、p2-nonnogelo-boxbottom）
