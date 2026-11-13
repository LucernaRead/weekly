# GATE-LOG — 2026-W47 ru-de proof1（全部机械门自跑证据）

工具：`~/workspace/weekly-git/tools/venv/bin/python`；正典 creambox：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`（md5 `ee7a55d8b2057cf4ad42a97bb1197383` 已验）。`TMPDIR` 全程指向本 scratch 的 `tmp/`。证据文件默认在 `gates/`，裁图在 `crops/`。

## §0 身份核对

- `sha256sum` 实跑：印 PDF `31fab92b…8521`（21,226,139 B）、网 PDF `1a67d6b4…96da7`（3,347,223 B）、text.md `7c68a018…58cd0`（63,452 B）——与任务一致。
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` OK；scratch 写探针 OK。

## §1 Occlusion 审计

- 自测：6 类 planted 缺陷全部触发，干净对照静默。
- 实跑（`tools/occlusion_audit.py`，8 页 SVG）：**42 TEXTX、0 LINEX、0 COVER/FOOTER/EDGE/BOXTITLE**（`gates/occlusion.json`）。
- 像素裁决：`gates/adjudicate.py` + 修正版 `gates/adjudicate2.py`（逐行像素测试，1× 网格卡片，墨阈值 min-channel < 140；v1 `text@N` 索引错，v2 修正 `els[idx]` 映射，v3 修正行规则：仅当一条墨迹连续覆盖整个声称的重叠区间才算接触）。结果：**33 项像素测试 CLEAR + 9 项 400 dpi 目视**（`crops/flags-contact-sheet.png`）——9 项均为词与后随标点/引号之间有可见空隙的分离字形。**42/42 CLEAR，0 真重叠。**
- 注意：该审计对奶油框内溢出、框标题溢出、横向溢出、降部溢出是盲的——以下 §2、§6 另行实测，不以 occlusion 0 放过。

## §2 正典 creambox.py 全版扫描 + P7 toolbox

- `gates/creambox-all.log`：+45 px 窗口 + 逐行 clearance 全版扫描；除一处候选外，无框内负余量。
- P7-TOOLBOX 汇总：3 框，框内最小余量 +11.9 px，降部余量最小 +5.9 px。
- BELOW-WINDOW 行均为 +28…+37 px 的下一标题误报（工具文档说明），除一处 P2 候选（见 §12）外。
- **P7 toolbox 真墨重测**（`gates/adjudicate.txt` Part C）：最小真墨余量 **+6.9 px**（y=992 框，`распродажа` 行）——无溢出。必查项 (c) 通过。

## §3 p8 compare（`tools/p8.py compare --core-p8 core-ru/svg/p8-test.svg --edition-p8 <版>/svg/p8-test.svg --total 150`）

- `gates/p8-compare.json`：**CLEAN；150/150 noted；missing=[]；extra=0；keydiff=[137,138,139,140]**。
- keydiff 逐条裁决（合法 E 节译文，核心中文键的正确德语替换）：
  - 137 “Dienstag, 17. November, Tag der Studierenden.”
  - 138 “Ein Paket muss verfolgt, abgeholt und geprüft werden.”
  - 139 “Am Dienstag spielt Russland gegen Venezuela.”
  - 140 “Allen einen schönen Tag der Studierenden!”
- 另：`gates/p8-core-keys.json`、`gates/p8-ed-keys.json`（P8 印出键提取）。

## §4 Freeze / freeze_direct 8/8

- `freeze.py diff --core-svg core-ru/svg --edition-svg <版>/svg`（`gates/freeze-diff.json`，exit 0）：
  - P1–P5 增减的西里尔字母：无（除下述说明层外）。
  - P6 删减的西里尔字母仅图表标签 “УЧЕБНЫЕ ДАННЫЕ” → 德语 “ÜBUNGSDATEN”（+ 德语练习数据句）——说明层，正确。
  - P7 删减 “Три темы, три уровня” → 增 “Drei Niveaus, drei Themen”——说明层，正确。
  - P8 删减的西里尔字母仅莫洛兹科图片说明词（见 §12）。
  - 新增 CJK 仅 6 个 U+3000（全角空格家具分隔符，SOP §1.1）；无汉字新增；任一版 SVG 文本节点中 0 汉字。
- `freeze.py baseline` 核心：**8/8 字节一致**，核心重哈希未变（`gates/freeze-baseline.log`）。

## §5 Keycheck 150/150

- `gates/keycheck-150.json`：编号 1–150 连续；P8 印出键 150 项；与 text.md 答案键关键部分 **0 不符 / 149**（Q150 为开放写作题，印 ✓，属设计）；分级 A2 50 / B1 76 / B2 24；分面 P1 10、P2 18、P3 18、P4 18、P5 18、P6 18、P7 12、P8 38；类型 Ankreuzen 55、Ausfüllen 54、Zuordnen 20、Sätze bilden 12、Umformen 4、Übersetzen 4、Schreiben 1。
- 逐题手验：每题对照题干/正文/表格核对；重点项——Q33 键 A（饥饿游戏 11 月 26 日上映，P3 正文）、Q54 键 2:0 与 Q59 键 c（P4 赛果表）、Q56 键 20:45（P4 更正框）、Q137–140 翻译键、Q150 范文 97 词（80–100 要求内）。
- 匹配块：P2 D 25→b, 26→d, 27→c, 28→a；P3 C 39→b, 40→d, 41→c, 42→a；P4 C 57→b, 58→a, 59→c, 60→d；P5 C 75→d, 76→b, 77→a, 78→c；P8 F 141→c, 142→d, 143→a, 144→b——均对照右栏字母序核对（`gates/keycheck-compare.txt`、`keycheck-compare2.txt`）。
- P8 对话 Q145–149 键 A/B/B/A/B 与购物对话语境一致（Q147 “Проверьте ___” → B промокод；посылку 无所指）。

## §6 Boxtitle 逐个真墨实测（PIL，不只看 advance）

- 方法：各页最小包含奶油框 + 内容缘 1862 / 页缘 1950；真墨为准。
- **D1**：P1 标题 `ТУР В ЦИФРАХ　Der Spieltag in Zahlen` 真墨右缘 997.6 px，框右缘 961.0 → **+36.6 px**（`crops/suspect-p1-subtitle.png` 目视确认）。
- **D2**：P2 `b. Международный день студента` 真墨右缘 1871.2 px，内容缘 1862 → **+9.2 px**（`crops/suspect-p2-matchline.png` 目视确认）。
- 其余：仅三处 +0.1/+0.2 px 亚像素噪声，非缺陷。
- 另：P2 降部候选（见 §12）真墨底 1158.0，余量 +1.0 px，通过；P3/P5 右栏框真墨余量均 ≥ +42.5 px；全版无降部溢出（Part C，全部框）。

## §7 印/网文字层比对

- `gates/textlayer.txt`、`gates/pdftotext-diff.txt`：pdftotext 字节数印 57,664、网 57,709；字符多重集差异：网 +41 空格、+4 换行。两版均为 8 页，网 < 7 MB。
- **KIT 的“identical multiset（30,938 字符）”不实**——实测多重集不同，网版多为空格（多为印版提取时合并的正确分词空格，如印 “ГАЗЕТАДЛЯ ИЗУЧАЮЩИХРУССКИЙ” vs 网 “… ИЗУЧАЮЩИХ РУССКИЙ”）。
- 网版引入的两处真问题见 D3（PROOF-NOTE）：闭引号脱离（`«чёрная пятница »`）、斜体丢失。
- **斜体清单**（`gates/italic-inventory.txt`、`gates/core-web-check.txt`）：印 PDF 全刊恰 3 处斜体跨度，全在 P1（`«` Newsreader Italic、`чёрная пятница` NotoSerif-MediumItalic、`»`）；**网 PDF 0 处**；核心同样 CORE-PRINT 3 / CORE-WEB 0——`tools/webpdf.py` 机制缺陷，全版继承。
- 网 P1 标题 “14- й” 传闻：PyMuPDF 跨度文本显示网版 `14-й тур:` 已连接；400 dpi 网/印标题对照（`crops/p1-web-headline.png`、`p1-print-headline.png`）像素级一致——提取产物，非缺陷。
- P8 最小字号（PyMuPDF 实测印 PDF，`gates/p8-font.txt`）：**9.75 pt**（388 跨度）；P1–P7 最小 11.62–12.75 pt；符合 SOP §1.1 下限 9.75 pt（未采信 KIT 的配置 px 数字，系实测）。

## §8 弯引号全版扫描（8 个 SVG）

- « » 各页平衡：25/25、4/4、21/21、73/73、21/21、1/1、36/36、17/17；零直引号 `"`/`'`；零 U+2019。
- P5 一对 „ “（P5 标题德语 „Schwarzer Freitag"，正确）。
- P7 一对 “ ”——故意保留的例外，已于错题诊所 “на “чёрной пятнице””（x≈1512, y≈552.6）确认。

## §9 text.md 检查

- 0 汉字/CJK 字符；E 节类型标签已本地化（`[A2 · Übersetzen]`、`[Ins Deutsche übersetzen]`）——必查项 (d) 不复现。
- 分隔符 `— СТРАНИЦА? —` 与核心 text.md 第 668 行相同——导出器格式，非缺陷。
- 答案解析 150 项、无缺失；行内键 129 项均与答案节一致。

## §10 全页目视（卡片逐页）

- P1：刊头、条带、标题带、导读、统计框（D1 可见）、目录页码锚（Стр. 2–8 齐全）、词框、照片 + CC0 说明、短讯框、测验 Q7–Q10、页脚 `Lucerna　RUSSISCHE WOCHENZEITUNG VOL.4　TEXT AUF RUSSISCH　ERKLÄRUNGEN AUF DEUTSCH` + `Seite 1 von 8`——余皆干净，无首字下沉（KIT 列为已知非缺陷）。
- P2：尤恩画 + 说明在位；节假日表、“А ВЫ?” 框、词汇四框、练习 A–D 齐全；中栏留白为核心版式（见 §12）。
- P3：三栏正文、HINWEIS 词注框、右栏两框、练习 A–D（Q29–46）齐全；无图（按设计）。
- P4：1912 年照片 + 说明、VOL.3 更正框、赛果表 8 场、国家队栏、15 轮赛程表、TOP-5 表、练习 A–D（Q47–64）齐全。
- P5：市场玉米照 + 说明、黑五日期框、练习 A–D（Q65–82）齐全；德语标题引号为 „ “，正确。
- P6：日历条（16 пн…22 вс，21–22 高亮）、练习数据图（38+26+18+18=100%，标明练习数据）、“ЗА И ПРОТИВ”框、练习 A–D（Q83–100）齐全。
- P7：三栏 A2/B1/B2、错题诊所四条（均在框内）、“СЛОВО”框、读者来信框（含“无来信”披露，在框内）、普希金肖像 + 说明、金句 8 条（页码 1,1,2,3,4,5,6,6）、下周预告齐全。
- P8：A–H 栏、Q113–150、Маша阅读文、H 范文（97 词）、答案键 150 项（按页排序）齐全；页脚 `Seite 8 von 8`。

## §11 外部事实来源

- **第 14 轮 8 场赛果**（2026-11-11 检索）：火车头–鲁宾 0:1（11 月 6 日）；法克尔–迪纳摩 1:2、阿赫马特–罗季娜 1:0、克拉斯诺达尔–中央陆军 4:2（11 月 7 日）；苏维埃之翼–奥伦堡 2:0、斯巴达克–阿克伦 2:1、泽尼特–罗斯托夫 2:2、波罗的卡–马哈奇卡拉迪纳摩 0:1（11 月 8 日）；共 21 球；罗季娜确在 2026/27 俄超。来源：Forbes.ru、sports.ru、rusfootball.info、Sport-Express、Championat、sportradar。15 轮赛程亦吻合（中央陆军–阿赫马特 11 月 21 日；罗季娜–火车头 11 月 22 日）；积分 31/31/29/26 与赛果一致。
- **国家队友谊赛**：Sport-Express 2026-11-09/10——乌兹别克斯坦–俄罗斯 11 月 12 日周四 18:00 塔什干帕赫塔科尔；俄罗斯–委内瑞拉 11 月 17 日周二 19:00 克拉斯诺达尔 Ozon Арена；第一频道 + Okko 直播；委内瑞拉一战纪念奥运冠军尼基塔·西蒙扬诞辰百年；为 2026 年最后一战。P4 正文每处细节均吻合。
- **Ozon 与黑五**：vc.ru 2026-10-31（引 Retail.ru/Ozon 业绩）——Ozon 2025 年 11 月 11 日单日超 1440 万单；Ozon 11.11 为 10 月 22 日–11 月 12 日；黑五 Ozon 11 月 13 日–12 月 2 日、Wildberries 11 月 16–30 日。P5 正文与日期框均吻合。
- **日历**（`date`，Europe/Moscow）：2026 年 11 月 16 日周一、17 日周二、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、12 日周四、6 日周五、7 日周六、8 日周日、27 日周五、30 日周一、29 日周日——刊内全部星期说法正确。11 月 4 日为民族团结日公众假日，故 11 月 20 个工作日 + 10 个非工作日正确（P6）。

## §12 判为非缺陷的项（附证据）

- **P2 降部候选**（必查项 (b)）：框 y=795、底 1159.0，末行基线 1154.0（“Studenten, einen für Väterchen Frost.”），creambox 降部余量 −1.0 → 真墨底 1158.0，**余量 +1.0 px**——无溢出（该行无降部字母）；紧但通过。P3/P5 右栏框真墨余量均 ≥ +42.5 px。
- **P8 无莫洛兹科图/注**：核心 P8 在 y≈2212–2560 有图 + 说明，本版 0 图、0 相关字符串；但已发 **W46 ru-de** 网 PDF（`issues/2026-w46/2026-w46-ru-de/2026-w46-ru-de.pdf`）P8 同样无此图/文、0 图——既定构建条件先例，非缺陷。范文在两版 P8 第 4 栏 y≈390 均在。
- **窄字距**（`gates/narrow-spaces.txt`、`gates/word-gaps.txt`）：全版同行相邻字串 PIL 墨盒间距 < 2 px 者均属三类——数字+月份（如 “17 ноября” 0.0 px）、U+3000 分隔符、标点紧排（» : , 等）。400 dpi 像素裁图证实词间确有空隙：`crops/p2-date16.png`（“22 ноября” 空隙清晰）、`crops/p2-prof.png`（“Профессиональные праздники” 空隙正常）、`crops/p2-gloss.png`（“родина Heimat · повод Anlass” 空隙清晰）。P1 刊头字距与核心逐值相同（继承）。先前 42 项 TEXTX 已像素裁决通过。P1 全幅目视无并词。
- **P7 “гололедица, будьте” 逗号**：SVG 中逗号为独立节点 `', '`（x=215.1），与核心节点逐一相同；缩略图看不清而已。
- **P7 普希金肖像紧裁剪**：与核心同一图像处理，非本版问题。
- **各页中栏留白**（P2/P3/P6 中栏在练习带上方的大面积空白）：核心版式继承，非缺陷。
- **P6 图表**：38+26+18+18=100%，并以德语标明为编辑部练习调查、非真实统计——正确。
- **Q100 键 “или”**：改写题用 “или” 连接两句，语法可用，键与印出一致。
- **P6 “20 个工作日”**：见 §11 日历核实，正确。
