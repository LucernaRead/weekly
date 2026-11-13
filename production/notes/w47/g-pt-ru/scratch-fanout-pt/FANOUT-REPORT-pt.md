# W47 PT fan-out — FANOUT-REPORT-pt.md

## 状态总览（2026-11-11 ~06:05 UTC，接替上一棒后第二棒）
- **pt-en：已完成，全部自查零问题。**
- **pt-de：已完成，全部自查零问题。**
- **pt-fr：已完成，全部自查零问题。**
- **pt-es：已完成，全部自查零问题。**
- **pt-it：已完成，全部自查零问题**（首轮即干净，无需修复轮）。
- **pt-nl：已完成，全部自查零问题**（两轮：P8 bridge 过长致 run1 断言失败，缩短后 run2 全绿）。
- **pt-ru：已完成，全部自查零问题**（五轮：P1 数字盒 serif 量误判 + P8 答案流超底，逐轮缩短后 run5 全绿）。
- **pt-ja：已完成，全部自查零问题**（首轮即干净，无需修复轮；occlusion 首跑自检瞬时抖动、重跑通过）。
- **pt-ko：已完成，全部自查零问题**（两轮：make_gates disc 转换机制 bug 修后 gates 重跑即绿；freeze 工具 0/8、直接复现 8/8）。
- **pt-zh-tw：已完成，全部自查零问题**（两轮：freeze diff 暴露 SEG 子串越界真缺陷 1 处，修表重建后 run2 全绿）。
- **10 版全部完成。Occlusion 口径更正（2026-11-11 ~06:05 UTC，见下）：工具自注要求用 `tools/venv/bin/python` 跑；venv（Pillow 13.0.0）下核心与 10 版全部 0 flags。早先 es/it/nl/ru/ja/ko 的“1 LINEX flag”记录是用系统 python3（Pillow 10.2.0）跑出的，同一冻结几何在两解释器下判定不同——属工具版本差异，非版面缺陷。**
- pt-en 最终：印刷 PDF 12,932,446 字节（sha256 `8d2b5815…160e4a`），网页 PDF 1,102,770 字节（sha256 `40bc2f44…a5e49c`）；run.py exit 0（150 题）；gates 16/16；occlusion 0 flags；p8 extract 150/150、compare CLEAN（keydiff 仅 [137, 138]）；freeze baseline 8/8；print/web 文字多重集 diff 0（8,502 词）；P8 答案字号实测 9.75pt（§1.1 下限）；§1.1 逐项实测通过；8 版目视全过；.text.md 全文通读 + 150 题逐题复核零问题。交付：8 SVG + 印刷 PDF + 网页 PDF + `.text.md`（535 行）+ ABSTRACT.txt（英文）+ WEEKLY-KIT.md（本版实测值）。
- pt-de 最终：印刷 PDF 12,938,940 字节（sha256 `a1b7bfc2…274c48f`），网页 PDF 1,110,425 字节（sha256 `26647474…a79b87`）；run.py exit 0（150 题）；gates 16/16；occlusion 0 flags；p8 extract 150/150、compare CLEAN（keydiff 仅 [137, 138]）；freeze baseline 8/8；print/web 文字多重集 diff 0（8,436 词）；P8 答案字号实测 9.75pt（§1.1 下限）；§1.1 逐项实测通过；8 版目视全过；.text.md 全文通读 + 150 题逐题复核零问题。交付：8 SVG + 印刷 PDF + 网页 PDF + `.text.md`（535 行）+ ABSTRACT.txt（德文，687 字节）+ WEEKLY-KIT.md（本版实测值）。
- pt-fr 最终：印刷 PDF 12,934,799 字节（sha256 `fe02b4fb…84cd7cd`），网页 PDF 1,104,302 字节（sha256 `96190bca…24717e`）；run.py exit 0（150 题）；gates 16/16；occlusion 0 flags；p8 extract 150/150、compare CLEAN（keydiff 仅 [137, 138]）；freeze baseline 8/8；print/web 文字多重集 diff 0（8,632 词）；P8 答案字号实测 9.75pt（§1.1 下限）；§1.1 逐项实测通过；8 版目视全过；.text.md 全文通读 + 150 题逐题复核零问题。交付：8 SVG + 印刷 PDF + 网页 PDF + `.text.md`（535 行）+ ABSTRACT.txt（法文，673 字节）+ WEEKLY-KIT.md（本版实测值）。
- pt-es 最终：印刷 PDF 12,933,122 字节（sha256 `faf2f098…19a321`），网页 PDF 1,103,156 字节（sha256 `8ef5e420…ec5950`）；run.py exit 0（150 题）；gates 16/16；occlusion **1 flag（仅 P1 LINEX，核心自带 0.2px 擦过——同工具对核心本身与已刊 fr 版重跑亦报同一 flag，冻结几何，见 §6 注）**；p8 extract 150/150、compare CLEAN（keydiff 仅 [137, 138]）；freeze baseline 8/8；print/web 文字多重集 diff 0（8,582 词）；P8 答案字号实测 9.75pt（§1.1 下限）；§1.1 逐项实测通过；8 版目视全过；.text.md 全文通读 + 150 题逐题复核零问题。交付：8 SVG + 印刷 PDF + 网页 PDF + `.text.md`（534 行）+ ABSTRACT.txt（西班牙文，649 字节）+ WEEKLY-KIT.md（本版实测值）。
- pt-it 最终：印刷 PDF 12,930,920 字节（sha256 `ea4e4fd8…34156aa`），网页 PDF 1,100,022 字节（sha256 `4c0d5069…31b3729`）；run.py exit 0（150 题）；gates 16/16；occlusion **1 flag（仅 P1 LINEX，核心自带 0.2px 擦过，同 es）**；p8 extract 150/150、compare CLEAN（keydiff 仅 [137, 138]）；freeze baseline 8/8；print/web 文字多重集 diff 0（8,460 词）；P8 答案字号实测 9.75pt（§1.1 下限）；§1.1 逐项实测通过；8 版目视全过；.text.md 全文通读 + 150 题逐题复核零问题。交付：8 SVG + 印刷 PDF + 网页 PDF + `.text.md`（534 行）+ ABSTRACT.txt（意大利文，314 字节）+ WEEKLY-KIT.md（本版实测值）。**首轮即干净，无修复轮。**
- pt-nl 最终：印刷 PDF 12,935,390 字节（sha256 `5a58050b…3bfe48`），网页 PDF 1,105,901 字节（sha256 `30db8b9c…a69b99`）；run.py exit 0（150 题）；gates 16/16；occlusion **1 flag（仅 P1 LINEX，核心自带 0.2px 擦过，同 es/it）**；p8 extract 150/150、compare CLEAN（keydiff 仅 [137, 138]）；freeze baseline 8/8；print/web 文字多重集 diff 0（8,561 词）；P8 答案字号实测 9.75pt（§1.1 下限）；§1.1 逐项实测通过；8 版目视全过；.text.md 全文通读 + 150 题逐题复核零问题。交付：8 SVG + 印刷 PDF + 网页 PDF + `.text.md`（534 行）+ ABSTRACT.txt（荷兰文，354 字节）+ WEEKLY-KIT.md（本版实测值）。**两轮：run1 因 P8 bridge 过长断言失败，缩短后 run2 全绿。**
- pt-ru 最终：印刷 PDF 12,916,544 字节（sha256 `d2822ae0…98db0f`），网页 PDF 1,151,627 字节（sha256 `a6a5f25f…db5ef`）；run.py exit 0（150 题）；gates 16/16；occlusion **1 flag（仅 P1 LINEX，核心自带 0.2px 擦过，同 es/it/nl）**；p8 extract 150/150、compare CLEAN（keydiff 仅 [137, 138]）；freeze baseline 8/8；print/web 文字多重集 diff 0（8,095 词）；P8 答案字号实测 9.75pt（§1.1 下限）；§1.1 逐项实测通过；8 版目视全过；.text.md 全文通读 + 150 题逐题复核零问题。交付：8 SVG + 印刷 PDF + 网页 PDF + `.text.md`（534 行）+ ABSTRACT.txt（俄文，506 字节）+ WEEKLY-KIT.md（本版实测值）。**五轮：P1 数字盒 + P8 答案流，逐轮缩短后 run5 全绿。**
- pt-ja 最终：印刷 PDF 24,992,044 字节（sha256 `04f284ed…87da7fb`），网页 PDF 1,644,666 字节（sha256 `339d2b05…c806a4`）；run.py exit 0（150 题）；gates 16/16；occlusion **1 flag（仅 P1 LINEX，核心自带 0.2px 擦过，同 es/it/nl/ru）**；p8 extract 150/150、compare CLEAN（keydiff 仅 [137, 138]）；freeze baseline 8/8；print/web 文字多重集 diff 0（6,897 词）；P8 答案字号实测 10.125pt（§1.1 下限 9.75pt 之上；日语用 13.5/1.16 非小字号）；§1.1 逐项实测通过；8 版目视全过；.text.md 全文通读 + 150 题逐题复核零问题。交付：8 SVG + 印刷 PDF + 网页 PDF + `.text.md`（534 行）+ ABSTRACT.txt（日文，327 字节）+ WEEKLY-KIT.md（本版实测值）。**首轮即干净，无修复轮。**
- pt-ko 最终：印刷 PDF 17,185,929 字节（sha256 `10c758cf…8414fed`），网页 PDF 1,394,979 字节（sha256 `b1b609fd…f6884ac`）；run.py exit 0（150 题）；gates 16/16；occlusion **1 flag（仅 P1 LINEX，核心自带 0.2px 擦过，同 es/it/nl/ru/ja）**；p8 extract 150/150、compare CLEAN（keydiff 仅 [137, 138]）；freeze **工具 0/8、直接复现 8/8**（见下）；print/web 文字多重集 diff 0（7,030 词）；P8 答案字号实测 10.125pt（§1.1 下限 9.75pt 之上；韩语用 13.5/1.16 非小字号）；§1.1 逐项实测通过；8 版目视全过；.text.md 全文通读 + 150 题逐题复核零问题。交付：8 SVG + 印刷 PDF + 网页 PDF + `.text.md`（534 行）+ ABSTRACT.txt（韩文，341 字节）+ WEEKLY-KIT.md（本版实测值）。**两轮：机制 bug 修后 gates 重跑即绿。**
- pt-zh-tw 最终：印刷 PDF 24,130,201 字节（sha256 `ddc35d9b…a5bd173`），网页 PDF 1,781,773 字节（sha256 `fff6b335…256cc12`）；run.py exit 0（150 题）；gates 16/16；occlusion **0 flags（venv Pillow 13.0.0 口径；见口径更正）**；p8 extract 150/150、compare CLEAN（keydiff 仅 [137, 138]）；freeze baseline **工具自报 8/8**；print/web 文字多重集 diff 0（7,010 词）；P8 答案字号实测 10.125pt（§1.1 下限 9.75pt 之上；繁体中文用 13.5/1.16 非小字号）；§1.1 逐项实测通过（**简体字残留 0**）；8 版目视全过；.text.md 全文通读 + 150 题逐题复核零问题。交付：8 SVG + 印刷 PDF + 网页 PDF + `.text.md`（534 行）+ ABSTRACT.txt（繁体中文，494 字节）+ WEEKLY-KIT.md（本版实测值）。**两轮：freeze diff 暴露 SEG 子串越界真缺陷 1 处（“週六 16 日:30”），修表重建后 run2 全绿。**
- 停手原因（已恢复）：`render.py` 第二次启动时，`> en-render4.log` 重定向创建即报
  `Disk quota exceeded`（01:0x UTC）。按 brief 硬规则立即停手，不重试。
  （df 仍显示 46G 空闲；quota 命令不存在；与上一棒 00:52 UTC 的三次 Errno 122 同类、
  项目级/瞬时波动。当时另有兄弟 agent 在跑 render.py，如 de-en。）

## 本棒开工探针（均通过）
- `git hash-object -w`（weekly-git 内）OK；scratch 内真实文件写 probe2.txt OK。

## pt-en：本棒完成的部分
### 1. P7 四项修复已全部应用（先于重建）
- scratch 机制文件已改：`tables_en.py`（SEG 两条 + OVR 披露 + 见下）、
  `furniture.py`（disc_text 新版 + 新增 `p7_geo`）、`transform.py`（新增 3b 步，
  断言三处替换各恰好出现 1 次；已核对 core-pt content7.py 三处计数均为 1）。
  pt-en 版内副本已同步；content7.py / gates.py 已就地改写并逐条核对计数。
- ① SEG：`官方答案到 11 月底才出，周日晚上只有非官方版` →
  `The official key comes only at the end of November.`
- ② SEG：`意识、良知；黑人意识日：铭记抗争与文化` →
  `awareness, conscience: the memory of the struggle and the culture`
- ③ 披露（OVR + furniture disc_text + content7.py disc_en + gates.py）→
  `Editor's note: no real letters or best texts for VOL.3 had arrived — the example stands; the promise carries to VOL.5.`
- ④ p7_geo：letters_pad 22、fy_gap 30、quote_step 初值 88。
- **附加修复（本棒自查发现，非上一棒清单）：** `编辑部示例…下期见！` 的 SEG 译文末尾
  带 `!`，与源文全角 `！` 转 ASCII 后叠加成 `editors!!`（content7.py 两处，W46 英版为单个 `!`）。
  已改：SEG 译文去尾 `!` → `...Send your letters to the editors`（转写后恰为单个 `!`），
  pt-en 版内两处 `editors!!` 已改回 `editors!`。
- **quote_step 88→76（本棒实测修正，上一棒估算有误）：** 按 88 重建后 occlusion 仍剩 2 flags
  （P7 第 4 行英文译文 baseline 2418.17，墨迹底 ~2428，压进 py=2404 的下期预告框；
  实测 fy=2017.5，非上一棒估算的 1988；第 4 行需上移 ≥25px）。
  改为 76 后重建：occlusion **0 flags**，gates 仍 16/16。
  （行距 76：同条 PT/EN 两行基线差 49.67px，行间余 ~26px，目视待验。）
  furniture.py 与 transform.py 的 p7_geo 已同步为 76。

### 2. 重建与门禁（重建 4 轮日志：en-run3.log / en-run4.log / en-occlusion4.json）
- `run.py` exit 0，零 FLOW OVERFLOW / HEAD TOO WIDE；练习 150（A2 48 / B1 71 / B2 31；
  分版 10/18/18/18/18/18/12/38）。
- **occlusion_audit：0 flags**（自检 planted 类全触发，clean 对照静默）。
- **gates.py：16/16 PASS，FAILURES: none**（footer+page line 8/8、P7 8 条金句 2x+页码、
  披露四项全 True、图片 5/5、P7 金句区 max baseline 2382.17）。
- **p8.py extract：150/150；compare vs 核心 CLEAN**，keydiff 仅 [137, 138]
  （翻译题键随读者语变，属正常）。
- **freeze diff：每页新增 CJK 仅 1 个 U+3000 全角空格分隔符**（家具 `　`），
  无新增汉字；P1 的 3 个“真汉字”为品牌蛾标 SVG 内部 `<title>Lucerna 三色蛾</title>`，
  核心版同样有，不渲染。直接 sha256：8 版 SVG 均与核心不同（讲解层已改写，预期内）。

### 3. 渲染 — 已完成（run6/render7，2026-11-11 02:07 UTC）
- render.py 第 6 轮（run6，`python -u`、小日志）：exit 0，零 FLOW OVERFLOW / HEAD TOO WIDE；练习 150（A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38）。render7 完成 02:07：印刷 PDF **12,932,446 字节**，8 页，1462.5×2025 pt，sha256 `8d2b58152bc0969151f8a7ab8becb0976221efdc62cac0d3cce877de8f160e4a`。
- webpdf7 完成 02:09：**1,102,770 字节**，8 页，sha256 `40bc2f444dbc31fbf0ef49643f1f81da13c134cab5ba0ec0a3ea804574a5e49c`，文字层 46,049 字节。print/web 文字多重集 diff 0（8,502 词各）。
- P8 答案字号实测 **9.75pt**（§1.1 下限；13 SVG 单位 × 0.75；答案区 187 spans、1,539 词）。
- 印刷 PDF 比核心版（25,311,626 字节）小 ~12.4 MB：原因已核实为嵌入 CJK 字体子集大小——核心版全中文讲解层嵌入数千个不同 CJK 字形，英文版只为 U+3000 家具分隔符嵌入同一批 CJK 字体（pdffonts 两版均含 NotoSansCJKsc/NotoSerifCJKsc）；5 张图两版字节全同（capoeira 699,781 / zumbi 194,233 / estudo 256,737 / lusiadas 404,078 / garrincha 914,576）。
- 终版门禁（run6 SVG 上重跑）：gates 16/16；occlusion 0 flags；p8 extract 150/150、compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8，diff 仅新增 U+3000（P1 2 个、其余每页 1 个，共 9 个）；§1.1 复验：纸 #fbfaf6 ×8、金/砖红/近黑 0、"double" 0、徽章三色全在、VOL.4 ×9、VOL.5 ×3（均在 P7 披露/下期预告内，允许）。
- 8 版目视（终版卡片）：P1–P8 全过。P5 五步计划括号空格、P7 金句"November."单句号、P2 "? Write" 均已目视确认；P6 图表、P8 答案区与 Mané Garrincha 图均干净。P2 "D AS PALAVRAS"、P4 "B AS PALAVRAS" 栏尾孤行与 P3 中部大空白均为核心版式，非缺陷。
- .text.md（535 行）全文通读 + 150 题逐题复核：零问题。错名旧件 `2026-w47-pt-zh-cn.text.md` 已删。150 键复核：Q131 = A（核心 D2 修复已在）、Q150 空（开放作文）、137/138 为读者语翻译答案（已验正确）。
- P8 chip 复核：Q113–120 全 B1、Q145–149 全 B1、Q150 B1（练习区；答案流重复 "150." 无 chip，与核心一致，非缺陷）。写作标题徽章在（"H ESCREVA VOCÊ" + "Writing task (no single correct answer); the model text (88 words) is below."）。
- **本棒自查发现的三类缺陷（均已修源头并重渲复验，其余 9 版须同类规避）：**
  1. "?Write" 粘连——4 处 E VOCÊ 提示（P2/P3/P4/P5）：SEG 键把问题与"写两句寄来"拆开，"？"转"?"后无空格。修法（W46先例）：整句 SEG 键，如"在你的国家，有纪念反对奴役斗争的假日吗？写两句寄来。"→"In your country, is there a holiday that remembers the fight against slavery? Write two sentences and send them in."；删独立"写两句寄来"条目；built content12/34/56.py 8 行 sed 修正。
  2. "("前缺空格——4 处括号 gloss（content56 ×3、content7 ×1）：SEG 值缺前导空格而源文"（"转"("。修法：把开括号"（"包进 SEG 键、值用" ("开头，如"（出考场前先记下自己的答案）"→" (note down your answers before leaving the exam room)"。（首尝仅加前导空格导致.text.md 出现"( ("双括号，已纠正。）
  3. 双句号"November.."——SEG 值尾"."与源文尾"。"转"."叠加：值改为无尾句号"The official key comes only at the end of November"。全表系统扫描确认仅此一处双标点风险。
- 复现性证明（2026-11-11）：全新核心复制 + transform.py → 6 个构建文件（bslib4、content12/34/56/7/8）与本版字节全同（6/6）。此前唯一差异即"November.."表 bug，由此查出。
- 新增机制脚本（scratch 内）：`check_final.py`（print/web 词多重集比对 + P8 答案区字号实测；de 轮已改为按版语命名输出）、`textmd.py`（.text.md 导出；de 轮已重构为 FURN 配置——各语 header/extra 从 furniture.py FURN[lang] 取）。
- pt-en 已交付全部件（见状态总览）。

## pt-de：已完成（2026-11-11 ~03:00 UTC）
### 1. 翻译表与机制
- `tables_de.py` 新写：键与 tables_en.py 完全一致（SEG 220、OVR 54 已验相等），值为德语。`furniture.py` 增 FURN[de]（footer `PORTUGIESISCHE WOCHENZEITUNG VOL.4　TEXT AUF PORTUGIESISCH　ERKLÄRUNGEN AUF DEUTSCH`、page `Seite {n} von {total}`、gloss `HINWEIS · `、badge `PORTUGIESISCHER TEXT　DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER`、sub330 28pt、P8 band "TEST UND ANTWORTEN" / "SEITE 8　Die große Prüfung der Woche + alle Antworten"）+ textmd 配置（标题/副标题/extra 3 条）。`textmd.py` 已重构为按语 FURN 配置（en 值并入 FURN[en]）。
- 前置值检查通过：无 "?Schreiben" 粘连、"(" 前缺空格、双句号风险（3 处疑似尾 "." 为德语序数词 "am 21." 等，串尾无后续 "。"，已验安全）；4 条 E VOCÊ 整句键全在；无独立 "写两句寄来"；值内 CJK 0。
- 复现性：全新核心复制 + transform.py → 6 构建文件字节全同（6/6，开工前已验）。

### 2. 六轮定稿（run1→run6）
- run1：FLOW OVERFLOW [P1-headline] + gates 13/16（3 FAIL：同基线碰撞 2——P1 band gloss 重叠 9.4px、P4 指示 vs '59.' 64.5px；页框穿越 3——P1 'EM POUCAS PALAVRAS' 标题、P2/P4 长指示、P7 金句 8 vs 页脚；披露 label False）。
- 修复：(a) label_nospace 拼写 "BeispieldderRedaktion…" → "BeispielderRedaktion—keinechterLeserbrief"（"Beispiel" 尾为 l，无双 d）；(b) "把词和释义配对" → "Paare zuordnen"（W46 先例）；(c) "快讯" → "IN KÜRZE"（W46 先例）；(d) P1 band gloss OVR → "Freitag, 20. November　Tag des Schwarzen Bewusstseins, Nationalfeiertag"；(e) quote_step 94→86；(f) P1 2023 框条目：**陷阱——OVR 整行条目（line 249）胜过同文 SEG 条目（line 251）**，两条都得缩短为 "(Gesetz von 2023: nationaler Feiertag)"。
- run2：gates 16/16，但 P1 溢出未变（同 y=1739/need 99——OVR 陷阱致缩短未生效）。run3（OVR 补修后）：run RC=0、零溢出、gates 绿；occlusion 仍 1 flag（P7 金句 8 德译行 1 y=2616.67 vs 页脚 y=2624——fy=2243 过低：德语右栏终 ly+lh=2213，英文为 1987.5）。
- P7 缩短轮（svglib wrap() 实测，CW=422.5）：E1 → "Offizielle Lösungen erst Ende November"（1 行）；E2 → "Das lange Wochenende endet am Sonntag; montags kein Ausgleich"（2 行）；E3 → "Palmeiras siegte 5:4 im Elfmeterschießen; Vasco siegte 2:1 in der regulären Zeit"（2 行）；E4 OVR → "20. November ist ein Freitag; das lange Wochenende geht bis Sonntag, den 22."（2 行）；label SEG → "Beispiel der Redaktion — kein echter Leserbrief. Schreiben Sie uns"（2 行，去尾 "!"——源文 "！" 会补）；披露（OVR + furniture disc_text 同串）→ "Anmerkung der Redaktion: Bis zum Redaktionsschluss keine echten Briefe und besten Texte für VOL.3 — das Beispiel bleibt; das Versprechen gilt für VOL.5."（4 行）；p7_geo pad 22→10、gap 30→6、step 86→76。共省 ≈7 行 + 36px ≈ 242px。
- run4：transform/run/gates 全绿、p8 150/150 CLEAN；occlusion 1 flag 新类 [LINEX]：P7 分隔线 hline 穿披露末行——**hline 画在 fy−14，fy_gap 必须 >14，否则线落在信盒内**（gap=6 时 hline y=1966，披露末行基线 1976.11 墨迹底 ~1981；盒高公式还低估 ~7px，末行基线已在盒底 1974 之下）。
- run5：fy_gap 6→16 后仍 1 flag（hline 上移 10px 至 1977，仍穿基线 1976.11 的墨迹）。run6：letters_pad 10→22（回 W46 值）——盒底下移 12px、hline 随 fy 上移，全部清除：**终版 p7_geo = pad 22、fy_gap 16、quote_step 76；末金句德基线 ≈2372 < 2404 预告框顶。** 后语教训：P7 起步用 letters_pad 22、fy_gap ≥16，右栏按英文 ly+lh 预算。

### 3. 渲染与终版门禁（run6/render1，2026-11-11 02:44 UTC）
- 印刷 PDF **12,938,940 字节**，8 页，1462.5×2025 pt，sha256 `a1b7bfc28e2a74b3ab9918dbc7f5e516ca7d7ef1b8fe56a6cc7921760274c48f`。webpdf1 02:45：**1,110,425 字节**，sha256 `26647474dbeb744211c4b67f3b6c3af9917024aaf3940d2e7a82cca917a79b87`，文字层 48,081 字节。print/web 文字多重集 diff 0（8,436 词各）。
- P8 答案字号实测 **9.75pt**（§1.1 下限；答案区 192 spans、1,456 词）。
- 终版门禁（run6 SVG 上重跑）：gates 16/16；occlusion 0 flags；p8 extract 150/150、compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8，diff 仅新增 U+3000（P1 2 个、其余每页 1 个，共 9 个）；§1.1 复验：纸 #fbfaf6 ×8、金/砖红/近黑 0、"double" 0、徽章三色全在、VOL.4 ×9、VOL.5 ×3（均在 P7 披露/下期预告内，允许）。
- 8 版目视（终版卡片）：P1–P8 全过。P1 band gloss、2023 框短版、"Paare zuordnen"、"IN KÜRZE"、P7 八金句德译 + 页码、信盒 + 披露（hline 已清）均目视确认；P6 图表、P8 答案区与 Mané Garrincha 图均干净。P3/P5 的 "Kasten." 跨栏孤词与 P4 "B AS PALAVRAS" 栏底孤悬均为核心流式版式，非缺陷；P1 "EM POUCAS PALAVRAS IN KÜRZE" 贴框边但在框内（gates 页框穿越 0）。
- .text.md（535 行）全文通读 + 150 题逐题复核：零问题。错名旧件 `2026-w47-pt-zh-cn.text.md` 已删。150 键复核：Q131 = A（核心 D2 修复已在）、Q150 = '✓'（开放作文）、137/138 为读者语翻译答案（已验正确：137 "Freitag, 20. November, ist ein nationaler Feiertag."、138 "Palmeiras gewann das Elfmeterschießen mit 5:4."）。
- P8 chip 复核：Q113–120 全 B1、Q145–149 全 B1、Q150 B1（练习区；答案流重复 "150." 无 chip，与核心一致，非缺陷）。写作标题徽章在（"H ESCREVA VOCÊ" + "Schreibaufgabe (keine eindeutige Antwort); der Mustertext (88 Wörter) steht unten."）。
- 系统扫描（终版 SVG + .text.md）：?Schreiben 0、?Write 0、"November.." 0、"( (" 0；全部 ".." 均为冻结葡语题干省略号 "..."；源 AST paren-join 0。
- 5 张图核心与 de 字节全同（cmp 验：capoeira 699,781 / zumbi 194,233 / estudo 256,737 / lusiadas 404,078 / garrincha 914,576）。
- 机制补丁：`check_final.py` 输出文件名由硬编码 "en-" 改为按版语命名（de 输出为 de-textdiff.json / de-p8size.json；此前 de 运行曾覆写 scratch 内 en-*.json——en 数值已在 KIT/报告中留存，无记录丢失）。
- pt-de 已交付全部件（见状态总览）。WEEKLY-KIT.md 为本版实测值（非核心 KIT §6 旧数），含六轮修复史与 hline 规则。

## pt-fr：已完成（2026-11-11 ~03:20 UTC）
### 1. 翻译表与机制
- `tables_fr.py` 新写：键与 tables_en.py 完全一致（SEG 220、OVR 54，已验相等），值为法语；furniture.py 增 FURN[fr]（footer `HEBDOMADAIRE PORTUGAIS VOL.4　TEXTE EN PORTUGAIS　EXPLICATIONS EN FRANÇAIS`、page `Page {n} sur {total}`、gloss `Note — `、badge `TEXTES EN PORTUGAIS　EXPLICATIONS EN FRANÇAIS — L’ÉDITION POUR LES LECTEURS FRANCOPHONES`、sub330 32pt、P8 band "TEST ET RÉPONSES" / "PAGE 8　La grande épreuve de la semaine + toutes les réponses"）。家具与指示语用 W46 pt-fr 已刊先例（"EN BREF"、"Vrai ou faux"、披露/label 的 W46 句式，VOL.2→VOL.3、VOL.4→VOL.5）。
- 前置值检查通过：无 "?Écrivez" 粘连、"(" 前缺空格、双标点风险（SEG 尾 "." 集合与 en 的 4 条完全一致）；4 条 E VOCÊ 整句键全在；无独立 "写两句寄来"；值内 CJK 0。
- 事故：一次 muse.edit 误把 fr 条目嵌进 en 条目内（old_text 命中第一处）。构建前 import 检查发现（FURN 无顶级 fr、嵌在 en 内），随即重写 furniture.py 全文为 en/de/fr 平级并 import 复验——无构建在损坏文件上跑过。教训：向 furniture.py 加语时 old_text 必须带足够上下文锚点，或直接重写全文。

### 2. 三轮定稿（run1→run3）
- run1：FLOW OVERFLOW [P1-headline] + gates 16/16——P1 2023 框条目（与 de 同类）。修复：直接缩短 OVR 整行 → "(loi de 2023 : jour férié national)"（de 教训：OVR 整行胜过 SEG，同文只须改 OVR；此轮不再走 SEG 先修的弯路）。
- run2：run RC=0、零溢出、gates 绿、p8 150/150 CLEAN；occlusion 1 flag [TEXTX]：末金句法译行 "Sans mémoire, il n'y a pas d'avenir. (Página 3)" 基线 2457.17，压进下期预告带头 "A PRÓXIMA SEMANA　La semaine prochaine (VOL.5)"（重叠 383.8×13.1px）。根因：法语右栏 E2/E3 纠错各 3 行（德语各 2 行），fy=2083.5（de 为 2002），比 de 高 81px；gates 的 "P7 金句区 clear" 检查是空洞的（过滤 y<2404 再断言 max<2404，第 4 行 PT 基线 2407.50 直接被滤掉，实测 max 2371.17 是前 3 行）——须人工 + occlusion + 目视强制。
- P7 缩短轮（svglib wrap() 实测，"sans" 19.5pt、CW−44=378.5）：E2 → "Le long week-end se termine le dimanche ; pas de congé le lundi."（3→2 行）；E3 → "Palmeiras s'est qualifié 5–4 aux tirs au but ; Vasco a gagné 2–1."（3→2 行）；共省 2 行 ≈59px；quote_step 86→80（行间余 80−69.67=10.33px；76 会使末法基线 2427 仍在带内）。终版 p7_geo = pad 22、fy_gap 16、quote_step 80；末金句法基线 ≈2380 < 2404。后语教训：右栏按英文 ly+lh 预算；纠错若 3 行一条，预留 ~60px 的 fy 并提前安排缩短 + 步长。

### 3. 渲染与终版门禁（run3/render1，2026-11-11 03:09 UTC）
- 印刷 PDF **12,934,799 字节**，8 页，1462.5×2025 pt，sha256 `fe02b4fbb3a5869c53657e1ef8abae2e2b6a6b6b9314f4f633c88483884cd7cd`。webpdf1 03:11：**1,104,302 字节**，sha256 `96190bcacb57c5304d4356ab4c91aac75a270913abde2c6cc06624bfc024717e`，文字层 47,586 字节。print/web 文字多重集 diff 0（8,632 词各）。
- P8 答案字号实测 **9.75pt**（§1.1 下限；答案区 186 spans、1,650 词）。
- 终版门禁（run3 SVG 上重跑）：gates 16/16；occlusion 0 flags；p8 extract 150/150、compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8，diff 仅新增 U+3000（P1 2 个、其余每页 1 个，共 9 个）；§1.1 复验：纸 #fbfaf6 ×8、金/砖红/近黑 0、"double" 0、徽章三色全在、VOL.4 ×9、VOL.5 ×3（均在 P7 披露/下期预告内，允许）。
- 8 版目视（终版卡片）：P1–P8 全过。P1 2023 框短版、band gloss、"Associez les paires"、P7 八金句法译 + 页码、信盒 + 披露（hline 已清）均目视确认；P6 图表、P8 答案区与 Mané Garrincha 图均干净。P3/P5 的方框词表跨栏与 P4 "B AS PALAVRAS" 栏底孤悬均为核心流式版式，非缺陷；徽章 "L’ÉDITION" 卡片上撇号后似有空格，SVG 原文为 "L’ÉDITION"（U+2019，无空格），属字体渲染观感，已验。
- .text.md（535 行）全文通读 + 150 题逐题复核：零问题。错名旧件 `2026-w47-pt-zh-cn.text.md` 已删。150 键复核：Q131 = A（核心 D2 修复已在）、Q150 = '✓'（开放作文）、137/138 为读者语翻译答案（已验正确：137 "Le vendredi 20 novembre est un jour férié national."、138 "Palmeiras a gagné 5–4 aux tirs au but."）。
- P8 chip 复核：Q113–120 全 B1、Q145–149 全 B1、Q150 B1（练习区；答案流重复 "150." 无 chip，与核心一致，非缺陷）。写作标题徽章在（"H ESCREVA VOCÊ" + "Exercice d'écriture (pas de réponse unique) ; le texte modèle (88 mots) est ci-dessous."）。
- 系统扫描（终版 SVG + .text.md）：?Écrivez 0、?Write 0、"novembre.." 0、"( (" 0；全部 ".." 均为冻结葡语题干省略号 "..."；源 AST paren-join 0。
- 5 张图核心与 fr 字节全同（cmp 验：capoeira 699,781 / zumbi 194,233 / estudo 256,737 / lusiadas 404,078 / garrincha 914,576）。
- pt-fr 已交付全部件（见状态总览）。WEEKLY-KIT.md 为本版实测值，含三轮修复史与 P7 右栏预算规则。

## pt-es：已完成（2026-11-11 ~03:50 UTC）
### 1. 翻译表与机制
- `tables_es.py` 新写：键与 tables_en.py 完全一致（SEG 220、OVR 54，已验相等），值为西班牙语；furniture.py 增 FURN[es]（footer `SEMANARIO PORTUGUÉS VOL.4　TEXTO EN PORTUGUÉS　EXPLICACIONES EN ESPAÑOL`、page `Página {n} de {total}`、gloss `Nota — `、badge `TEXTOS EN PORTUGUÉS　EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`、sub330 30pt、P8 band "PRUEBA Y RESPUESTAS" / "PÁGINA 8　La gran prueba de la semana + todas las respuestas"）。家具与指示语用 W46 pt-es 已刊先例（"Empareja"、"Emparejar vocabulario"、披露/label 的 W46 句式，VOL.2→VOL.3、VOL.4→VOL.5）。"¿Verdadero o falso?" 用正确西语开问号（W46 用 "Verdadero o falso?" 无 ¿，本版纠正）。
- 前置值检查通过：无 "?Escribe" 粘连、"(" 前缺空格、双标点风险（SEG 尾 "." 集合与 en 的 4 条完全一致）；4 条 E VOCÊ 整句键全在；无独立 "写两句寄来"；值内 CJK 0。E2/E3 值无尾句号（渲染句号来自源 "。"，已对 built content7.py 实测确认；fr KIT 误记为值带句号，实际值无尾句号）。
- 事故：一次 muse.edit 使 furniture.py 多出一个闭合括号（33 open / 34 close）。构建前 import 检查发现，当分钟修复，全文 en/de/es/fr 平级并 import 复验。教训同 fr：加语后立即 import 验。

### 2. 两轮定稿（run1→run2）
- run1：run RC=0、零溢出、gates 16/16、p8 150/150 CLEAN；occlusion 3 flags：① P1 LINEX "em Brasília. (Página 4)"（quiz 分隔线 y=2312 擦过冻结行墨顶 0.2px）；②③ P7 COVER 两处：末金句对西译行 "Sin memoria, no hay futuro. (Página 3)" 与 "Consulta el transporte, prepara tus documentos y disfruta bien del puente" 基线 2409.67，49% 被下期预告带（顶 2404）遮住。根因：西语右栏 fy=2054（披露 4 行），gates 的 "P7 金句区 clear" 检查是空洞的（过滤 y<2404 再断言，实测 max 2360.0 是前 3 行）——须人工 + occlusion + 目视强制。
- LINEX 定性（关键）：五版（core/en/de/fr/es）P1 该处几何与元素顺序完全相同；同工具对已刊 fr SVG 与 core-pt/svg 重跑，均报同一 flag。结论：核心自带边际情形，冻结几何，渲染不可见，fan-out 内无法修（动规则或正文即动核心版式）。en/de/fr 的 "0 flags" 记录早于当前工具状态。**后续各版须以核心重跑结果为准记录，不可再以 "0 flags" 为硬门禁口径。**
- P7 修复（svglib wrap() 实测，"sans" 19.5pt、CW−44=378.5）：披露 4→3 行——"Nota de la redacción: sin cartas reales ni mejores textos del VOL.3 — queda el ejemplo y la promesa pasa al VOL.5."（保 "reales" 与 VOL.3，舍 "al cierre"；先试的 123 字符版仍 4 行，114 字符版 3 行）。fy −29px → 2025，末金句西基线 2380.67，墨底 ~2385.7，净空 ~18px；quote_step 保持 80。OVR 与 FURN disc_text 双处同步改。
- 机制教训：**transform.py 不可重入**——已转换文件上重跑即断言失败（中文 masthead 锚点已无）；中途改表须 rm -rf + cp -r 核心重建，不可在原位重跑（es 第一轮重建即因此失败，且 gates 随之报 readers corner disclosure——make_gates 已写新披露而 content7.py 仍是旧披露；整版重建后双双解决）。
- p8.py CLI 纠正：`--p8` 是 SVG 路径非页码（`--p8 8` 报 FileNotFoundError '8'）；`compare --core-dir/--edition-dir --target es` 按目标语找本地化文件名（p8-ejercicios.svg）失败——须用显式 `--core-p8/--edition-p8` 路径。

### 3. 渲染与终版门禁（run2/render1，2026-11-11 03:36 UTC）
- 印刷 PDF **12,933,122 字节**，8 页，1462.5×2025 pt，sha256 `faf2f098043d4126fb49f45b6d0f943c905b98599530e81db0afa3c5a119a321`。webpdf1 03:39：**1,103,156 字节**，sha256 `8ef5e4200eef8d5c890d74178086cb73a076cef529d3dcf9f25336258dec5950`，文字层 47,242 字节。print/web 文字多重集 diff 0（8,582 词各）。
- P8 答案字号实测 **9.75pt**（§1.1 下限；答案区 185 spans、1,607 词）。
- 终版门禁（run2 SVG 上重跑）：gates 16/16；occlusion 1 flag（仅核心自带 LINEX，见上）；p8 extract 150/150、compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8，diff 仅新增 U+3000（P1 2 个、其余每页 1 个，共 9 个）；§1.1 复验：纸 #fbfaf6 ×8、金/砖红/近黑 0、"double" 0、徽章三色全在、VOL.4 ×9、VOL.5 ×3（均在 P7 披露/下期预告内，允许）。
- 8 版目视（终版卡片）：P1–P8 全过。P1 2023 框短版 "(ley de 2023: fiesta nacional)"、P7 信盒 + 3 行披露（hline 已清）+ 八金句西译与页码、P6 图表、P8 答案区与 Mané Garrincha 图均目视确认；P3/P5 的方框词表跨栏与 P4 "B AS PALAVRAS" 栏底孤悬均为核心流式版式，非缺陷。
- .text.md（534 行）全文通读 + 150 题逐题复核：零问题（1 处已修：textmd_extra 日程行混入法式冒号前空格 "(…) : SEX"，西语改为 "(…): SEX"；其余 " :" 扫描为 0）。金句行 "….(Página N)" 无空格格式与核心导出及已刊 fr .text.md 完全同型（SVG 构建码另加空格），非缺陷。150 键复核：Q131 = A（核心 D2 修复已在）、Q150 = '✓'（开放作文）、137/138 为读者语翻译答案（已验正确：137 "El viernes 20 de noviembre es festivo nacional."、138 "El Palmeiras ganó 5–4 en los penaltis."）。
- P8 chip 复核：Q113–120 全 B1、Q145–149 全 B1、Q150 B1（练习区；答案流 "150. " 无 chip，与核心一致，非缺陷）。写作标题徽章在（"H ESCREVA VOCÊ" + "Ejercicio de escritura (sin respuesta única); el texto modelo (88 palabras) está abajo."）。
- 系统扫描（终版 SVG + .text.md）：?Escribe 0、?Write 0、".."（"…" 外）0、"( (" 0；SVG 内 3 个非 U+3000 CJK 字符均在冻结 Logo 内嵌 `<title>Lucerna 三色蛾</title>`（核心同款），非正文。
- 5 张图核心与 es 字节全同（cmp 验：capoeira 699,781 / zumbi 194,233 / estudo 256,737 / lusiadas 404,078 / garrincha 914,576）。
- pt-es 已交付全部件（见状态总览）。WEEKLY-KIT.md 为本版实测值，含两轮修复史、transform 不可重入与 p8 CLI 纠正、LINEX 定性记录。

## pt-it：已完成（2026-11-11 ~04:10 UTC，首轮即干净）
### 1. 翻译表与机制
- `tables_it.py` 新写：键与 tables_en.py 完全一致（SEG 220、OVR 54，已验相等），值为意大利语；furniture.py 增 FURN[it]（footer `SETTIMANALE PORTOGHESE VOL.4　TESTI IN PORTOGHESE　SPIEGAZIONI IN ITALIANO`、page `Pagina {n} di {total}`、gloss `Nota — `、badge `TESTI IN PORTOGHESE　SPIEGAZIONI IN ITALIANO — L’EDIZIONE PER I LETTORI ITALIANI`、sub330 30pt、P8 band "PROVA E RISPOSTE" / "PAGINA 8　La grande prova della settimana + tutte le risposte"）。家具与指示语用 W46 pt-it 已刊先例（"Abbina"、"Abbinare il lessico"、"Vero o falso?"、"IN BREVE"、披露/label 的 W46 句式，VOL.2→VOL.3、VOL.4→VOL.5）。
- 前置值检查通过：无 "?Scrivi" 粘连、"(" 前缺空格、双标点风险（SEG 尾 "." 集合与 en 的 4 条完全一致）；4 条 E VOCÊ 整句键全在；无独立 "写两句寄来"；值内 CJK 0、" :" 0。**P7 预量：披露已按 3 行预缩**（"Nota della redazione: né lettere vere né migliori testi del VOL.3 — resta l'esempio e la promessa passa al VOL.5."，svglib wrap() "sans" 19.5pt、CW−44=378.5 实测 3 行）；E1/E2/E3 各预量 2 行。p7_geo 起步即 pad 22、fy_gap 16、quote_step 80。
- 事故：加 FURN[it] 的 muse.edit 误把 es 条目尾行改成西意混合句（"Ver el texto modelo en la sezione H di questa pagina (88 palabras)"），因 old_text 锚点撞上共享键行。grep + import 检查当即发现、当分钟修复（es 尾行恢复为 "Ver el texto modelo en la sección H de esta página (88 palabras)"）；es 版自交付后未重建，成件未受影响。教训：加语锚点必须取前一条目独有的值行，改后复核前一条目的值。

### 2. 首轮定稿（run1，无修复轮）
- run1：run RC=0、零溢出、gates 16/16、p8 extract 150/150、compare CLEAN（keydiff [137, 138]）、freeze baseline 8/8；occlusion 仅 1 flag（P1 LINEX 核心自带 0.2px 擦过，同 es 定性）；P7 无 flag——末金句意基线 2380.67，墨底 ~2385.7，净空 ~18px（< 2404 预告框顶）。p7_geo 终版 = pad 22、fy_gap 16、quote_step 80。**首版单轮通过：es 教训的预量法（披露 3 行 + 纠错各 2 行 + step 80）即为已验证成型，后 5 语照此起步。**

### 3. 渲染与终版门禁（run1/render1，2026-11-11 03:57 UTC）
- 印刷 PDF **12,930,920 字节**，8 页，1462.5×2025 pt，sha256 `ea4e4fd80e9aa3f9d9fa305a985f9e234abc4858b6f10e4d4b2ab416e34156aa`。webpdf1 03:59：**1,100,022 字节**，sha256 `4c0d5069ba440d21f7601bb88ba37ec14a77f30c51ab8a9202fe7bb2a31b3729`，文字层 46,871 字节。print/web 文字多重集 diff 0（8,460 词各）。
- P8 答案字号实测 **9.75pt**（§1.1 下限；答案区 186 spans、1,554 词）。
- 终版门禁（run1 SVG 上重跑）：gates 16/16；occlusion 1 flag（仅核心自带 LINEX，见上）；p8 extract 150/150、compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8，diff 仅新增 U+3000（共 9 个）；§1.1 复验：纸 #fbfaf6 ×8、金/砖红/近黑 0、"double" 0、徽章三色全在、VOL.4 ×9、VOL.5 ×3（均在 P7 披露/下期预告内，允许）。
- 8 版目视（终版卡片）：P1–P8 全过。P1 2023 框短版 "(legge del 2023: festa nazionale)"、"Quiz lampo"、"Abbina"、P7 信盒 + 3 行披露（hline 已清）+ 八金句意译与页码、P6 图表、P8 答案区与 Mané Garrincha 图均目视确认；P3/P5 的方框词表跨栏与 P4 "B AS PALAVRAS" 栏底孤悬均为核心流式版式，非缺陷；徽章 "L’EDIZIONE" 卡片上撇号后似有空格，SVG 原文为 "L’EDIZIONE"（U+2019，无空格），属字体渲染观感（同 fr），已验。
- .text.md（534 行）全文通读 + 150 题逐题复核：零问题。错名旧件 `2026-w47-pt-zh-cn.text.md` 已删。150 键复核：Q131 = A（核心 D2 修复已在）、Q150 = '✓'（开放作文）、137/138 为读者语翻译答案（已验正确：137 "Venerdì 20 novembre è festa nazionale."、138 "Il Palmeiras ha vinto 5–4 ai rigori."）。
- P8 chip 复核：Q113–120 全 B1、Q145–149 全 B1、Q150 B1（练习区；答案流 "150. " 无 chip，与核心一致，非缺陷）。写作标题徽章在（"H ESCREVA VOCÊ" + "Esercizio di scrittura (senza risposta unica); il testo modello (88 parole) è sotto."）。
- 系统扫描（终版 SVG + .text.md）：?Scrivi 0、?Write 0、".."（"…" 外）0、"( (" 0、" :" 0；SVG 内 3 个非 U+3000 CJK 字符均在冻结 Logo 内嵌 `<title>Lucerna 三色蛾</title>`（核心同款），非正文。
- 5 张图核心与 it 字节全同（cmp 验：capoeira 699,781 / zumbi 194,233 / estudo 256,737 / lusiadas 404,078 / garrincha 914,576）。
- pt-it 已交付全部件（见状态总览）。WEEKLY-KIT.md 为本版实测值，含首轮通过记录与 furniture.py 事故。

## pt-nl：已完成（2026-11-11 ~04:35 UTC，两轮）
### 1. 翻译表与机制
- `tables_nl.py` 新写：键与 tables_en.py 完全一致（SEG 220、OVR 54，已验相等），值为荷兰语；furniture.py 增 FURN[nl]（footer `PORTUGEES WEEKBLAD VOL.4　TEKSTEN IN HET PORTUGEES　UITLEG IN HET NEDERLANDS`、page `Pagina {n} van {total}`、gloss `Uitleg — `、badge `TEKSTEN IN HET PORTUGEES　UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`、sub330 32pt、P8 band "TOETS EN ANTWOORDEN" / "PAGINA 8　De grote toets van de week + alle antwoorden"）。家具与指示语用 W46 pt-nl 已刊先例（"Koppel"、"Woordenschat koppelen"、"Waar of niet waar?"、"KORTOM"、披露/label 的 W46 句式，VOL.2→VOL.3、VOL.4→VOL.5）。
- 前置值检查通过：无 "?Schrijf" 粘连、"(" 前缺空格、双标点风险（SEG 尾 "." 集合与 en 的 4 条完全一致）；4 条 E VOCÊ 整句键全在；无独立 "写两句寄来"；值内 CJK 0、" :" 0。**P7 预量：披露首稿 124 字符 → 4 行，改 119 字符版 3 行**（"Opmerking van de redactie: geen echte brieven of beste teksten uit VOL.3 — het voorbeeld blijft, de belofte naar VOL.5."）；E3 首稿 3 行，改 75 字符版 2 行（"Palmeiras door na strafschoppen 5–4; in de reguliere tijd won Vasco met 2–1"）；E1/E2/E4 各 2 行。p7_geo 起步即 pad 22、fy_gap 16、quote_step 80。**P8 bridge 未预量——run1 断言失败后才查出（见下）。**

### 2. 两轮定稿（run1→run2）
- run1：run.py RC=1——content8.py:119 断言 `P8 image has no room: f.y=1005.87 ci=3`；gates 15/16（footer+page line 败，只因 run 死后 P8 SVG 仍是核心复制件）。根因：荷兰语 model bridge（"Schrijfopdracht (zonder één juist antwoord); de modeltekst (88 woorden) staat hieronder."，88 字符）在 20.5pt、CW 422.5 下绕 **3 行**（英/意各 2 行），练习流多 ~30px；图片余位 `min(250, 1150−(f.y+12))` = 132 < 150 触发断言。**新缺陷类：P8 图片余位断言。**ex 的 note 参数只进答案登记簿、不占练习流，只有 bridge 影响练习流。
- 修复：model_bridge（FURN[nl]）→ "Schrijfopdracht; de modeltekst (88 woorden) staat hieronder."（60 字符，wrap() 20.5pt 实测 2 行）；整版重建（transform 不可重入）。run2：run RC=0、零溢出、gates 16/16，P8 流终 y=976.15（图片余位 162 ✓）；occlusion 仅 1 flag（P1 LINEX 核心自带）；p8 150/150 CLEAN；freeze 8/8；P7 末金句荷基线 2351.17（< 2404 预告框顶，净空 ~48px）。**后 4 语：model_bridge 须以 wrap() 20.5pt、CW 422.5 预量至 ≤2 行（英/意为 2 行）；P8 练习流仅 ~18px 余量。**

### 3. 渲染与终版门禁（run2/render1，2026-11-11 04:20 UTC）
- 印刷 PDF **12,935,390 字节**，8 页，1462.5×2025 pt，sha256 `5a58050b684893bba2a4e35ab3569f74f7a14e8bfb74da65db0da1104a3bfe48`。webpdf1 04:22：**1,105,901 字节**，sha256 `30db8b9ca8a3331ca2ff323c673c7422ab8cd2cffae1df6263f4156fd4a69b99`，文字层 47,250 字节。print/web 文字多重集 diff 0（8,561 词各）。
- P8 答案字号实测 **9.75pt**（§1.1 下限；答案区 190 spans、1,559 词）。
- 终版门禁（run2 SVG 上重跑）：gates 16/16；occlusion 1 flag（仅核心自带 LINEX，见上）；p8 extract 150/150、compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8，diff 仅新增 U+3000（共 9 个）；§1.1 复验：纸 #fbfaf6 ×8、金/砖红/近黑 0、"double" 0、徽章三色全在、VOL.4 ×9、VOL.5 ×3（均在 P7 披露/下期预告内，允许）。
- 8 版目视（终版卡片）：P1–P8 全过。P1 2023 框短版 "(wet van 2023: nationale feestdag)"、"Bliksemquiz"、"KORTOM"、"Koppel"、P7 信盒 + 3 行披露（hline 已清）+ 八金句荷译与页码、P6 图表、P8 答案区与 Mané Garrincha 图均目视确认；P3/P5 的方框词表跨栏与 P4 "B AS PALAVRAS" 栏底孤悬均为核心流式版式，非缺陷。
- .text.md（534 行）全文通读 + 150 题逐题复核：零问题。错名旧件 `2026-w47-pt-zh-cn.text.md` 已删。150 键复核：Q131 = A（核心 D2 修复已在）、Q150 = '✓'（开放作文）、137/138 为读者语翻译答案（已验正确：137 "Vrijdag 20 november is een nationale feestdag."、138 "Palmeiras won met 5–4 na strafschoppen."）。
- P8 chip 复核：Q113–120 全 B1、Q145–149 全 B1、Q150 B1（练习区；答案流 "150. " 无 chip，与核心一致，非缺陷）。写作标题徽章在（"H ESCREVA VOCÊ" + bridge "Schrijfopdracht; de modeltekst (88 woorden) staat hieronder."）。
- 系统扫描（终版 SVG + .text.md）：?Schrijf 0、?Write 0、".."（"…" 外）0、"( (" 0、" :" 0；SVG 内 3 个非 U+3000 CJK 字符均在冻结 Logo 内嵌 `<title>Lucerna 三色蛾</title>`（核心同款），非正文。
- 5 张图核心与 nl 字节全同（cmp 验：capoeira 699,781 / zumbi 194,233 / estudo 256,737 / lusiadas 404,078 / garrincha 914,576）。
- pt-nl 已交付全部件（见状态总览）。WEEKLY-KIT.md 为本版实测值，含 P8 bridge 断言修复史与预量规则。

## pt-ru：已完成（2026-11-11 ~05:00 UTC，五轮）
### 1. 翻译表与机制
- `tables_ru.py` 新写：SEG 键与 tables_en.py 完全一致（220，已验相等），OVR 55 条（en 的 54 条 + Q140 整句 OVR 1 条，见下），值为俄语；furniture.py 增 FURN[ru]（footer `ПОРТУГАЛЬСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.4　ТЕКСТЫ НА ПОРТУГАЛЬСКОМ　ОБЪЯСНЕНИЯ НА РУССКОМ`、page `Страница {n} из {total}`、gloss `Пояснение — `、badge `ТЕКСТЫ НА ПОРТУГАЛЬСКОМ　ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ`、sub330 28pt、P8 band "ТЕСТ И ОТВЕТЫ" / "СТРАНИЦА 8　Большой тест недели + все ответы"）。家具与指示语用 W46 pt-ru 已刊先例（"Соедините"、"Соедините слова"、"Верно или неверно?"、"Коротко"、披露/label 的 W46 句式，VOL.2→VOL.3、VOL.4→VOL.5；E VOCÊ 用 W46 非正式体 "Напиши два предложения и пришли нам."）。
- 前置值检查通过：无 "?Напиши" 粘连、"(" 前缺空格、双标点风险（SEG 尾 "." 集合与 en 的 4 条完全一致）；4 条 E VOCÊ 整句键全在；无独立 "写两句寄来"；值内 CJK 0、" :" 0。**P7 预量：披露用 W46 短式 3 行**（"Примечание: настоящих писем и лучших текстов из VOL.3 не пришло. Пример остаётся, обещание — в VOL.5."）；E2/E3 各缩至 2 行（E2 "Длинные выходные — до воскресенья; в понедельник нет выходного"、E3 "Палмейрас прошёл по пенальти 5–4; в основное время выиграл Васко 2–1"）；E1/E4 各 2 行。**bridge 预量（nl 教训）：**"Письменное задание; образец текста (88 слов) — ниже." 2 行（20.5pt 实测；3 行版当场否决）。p7_geo 起步即 pad 22、fy_gap 16、quote_step 80。
- **量法教训（本版两次踩中）：** 数字盒项须以 **serif、宽 386.5（CW−2×pad）** 量，sans/422.5 会误判（2023 项 sans 2 行、serif 3 行）；P7 披露/纠错仍按 sans、19.5pt、CW−44=378.5 量（与既往一致）。

### 2. 五轮定稿（run1→run5）
- run1：run RC=0；P1-headline 溢出 1（col 2 y=1739 need 99）+ P8-keys 溢出 3（col 3 y=2559/2588）；gates 15/16（同基线碰撞 9 处，均由两处溢出引起）。两处新类：
  - **P8 答案流超底**：俄语答案注长，答案流（1328–2560）超 ~28px，末项 148/149/150 落在 2573/2587，互撞。修法：逐轮缩短答案注——"配合复数："→"множественное число: "（Q36+Q72）、model_note→"Смотри образец текста в разделе H (88 слов)"（Q150）、Q140 注新增 OVR 整句→"повелительное наклонение + quando-придаточное"（3→2 行）、"官方答案 11 月底前公布"→"Официальные ответы — до конца ноября"（Q10+Q118）、"次回合..."→"Гремио сыграл 1–1 с Атлетико-МГ, дальше 3–1 по сумме"（Q47）、"诺里斯..."→"Норрис выиграл Гран-при Сан-Паулу, Ферстаппен второй"（Q51）、"2023 年法律..."→"Закон 2023 года: 20 ноября — национальный праздник"（Q31+Q124）。**注意：重排混沌——run3 四处缩短仅净移 1 行（2588→2571），每轮须实测流终 y，缩到 < 2560 并留余量（终版 2556）。**
  - **P1 数字盒 serif 行数**：2023 项 "(закон 2023: национальный праздник)" sans 2 行、serif 3 行（盒内 serif 20pt、宽 386.5），比英版多 1 行（27px），Q6 顶进 "A SEMANA EM DOIS TEMPOS" 小专题（occlusion TEXTX 2 处）。修法：括号→"(закон 2023: праздник)"（serif 2 行）；"3" 项亦缩为 "(выходные 3 дня: 20–22 ноября)"（serif 3 行，与英版同）。run5：run RC=0、零溢出、gates 16/16、P8 流终 2556、P8 练习流终 976.15、P7 末俄基线 2351.17（< 2404，净空 ~48px）。

### 3. 渲染与终版门禁（run5/render1，2026-11-11 04:49 UTC）
- 印刷 PDF **12,916,544 字节**，8 页，1462.5×2025 pt，sha256 `d2822ae0ea1c50d12610a8f529efeec6361f608ee344ee6af36868f8bf98db0f`。webpdf1 04:51：**1,151,627 字节**，sha256 `a6a5f25f93265a8914462a17975934d91bef85201bd768ee5221387a716db5ef`，文字层 54,994 字节。print/web 文字多重集 diff 0（8,095 词各）。
- P8 答案字号实测 **9.75pt**（§1.1 下限；答案区 625 spans——西里尔词切出更多 span、1,352 词）。
- 终版门禁（run5 SVG 上重跑）：gates 16/16；occlusion 1 flag（仅核心自带 LINEX，见上）；p8 extract 150/150、compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8，diff 仅新增 U+3000（共 9 个）；§1.1 复验：纸 #fbfaf6 ×8、金/砖红/近黑 0、"double" 0、徽章三色全在、VOL.4 ×9、VOL.5 ×3（均在 P7 披露/下期预告内，允许）。
- 8 版目视（终版卡片）：P1–P8 全过。P1 2023 框短版 "(закон 2023: праздник)"、Q6 已让出空间（行 B 标题无压）、"Экспресс-викторина"、"Коротко"、"Соедините"、P7 信盒 + 3 行披露（hline 已清）+ 八金句俄译与页码、P6 图表、P8 答案区与 Mané Garrincha 图均目视确认；P3/P5 的方框词表跨栏与 P4 "B AS PALAVRAS" 栏底孤悬均为核心流式版式，非缺陷。
- .text.md（534 行）全文通读 + 150 题逐题复核：零问题。错名旧件 `2026-w47-pt-zh-cn.text.md` 已删。150 键复核：Q131 = A（核心 D2 修复已在）、Q150 = '✓'（开放作文）、137/138 为读者语翻译答案（已验正确：137 "Пятница, 20 ноября, — национальный праздник."、138 "Палмейрас выиграл 5–4 по пенальти."；注：p8.py 抽值报 Q137 键为截断的 "Пятница, 20 ноября,"——因抽取器在首个 " — " 处切分，而俄语答案本身含破折号；SVG 答案区原行完整，已直读核实，非缺陷）。
- P8 chip 复核：Q113–120 全 B1、Q145–149 全 B1、Q150 B1（练习区；答案流 "150. " 无 chip，与核心一致，非缺陷）。写作标题徽章在（"H ESCREVA VOCÊ" + bridge "Письменное задание; образец текста (88 слов) — ниже."）。
- 系统扫描（终版 SVG + .text.md）：?Напиши 0、?Write 0、".."（"…" 外）0、"( (" 0、" :" 0；SVG 内 3 个非 U+3000 CJK 字符均在冻结 Logo 内嵌 `<title>Lucerna 三色蛾</title>`（核心同款），非正文。
- 5 张图核心与 ru 字节全同（cmp 验：capoeira 699,781 / zumbi 194,233 / estudo 256,737 / lusiadas 404,078 / garrincha 914,576）。
- pt-ru 已交付全部件（见状态总览）。WEEKLY-KIT.md 为本版实测值，含五轮修复史、serif 量法与答案流重排教训。

## pt-ja：已完成（2026-11-11 ~05:15 UTC，首轮即干净）
### 1. 翻译表与机制
- `tables_ja.py` 新写：SEG 键与 tables_en.py 完全一致（220，已验相等），OVR 55 条（en 的 54 条 + label 整句 OVR 1 条，见下），值为日语（汉字用日式写法）；furniture.py 增 FURN[ja]（footer `ポルトガル語週刊 VOL.4　本文はポルトガル語　解説は日本語`、page `{n}ページ（全{total}ページ）`、gloss `解説 — `、badge `ポルトガル語テキスト　日本語の解説 — 日本語読者のための版`、sub330 34pt、P8 band "評価と解答" / "8ページ　今週の大テスト + すべての解答"、p8_keys_small **False**——日语用 W46 pt-ja 的 13.5/1.16 非小字号）。家具与指示语用 W46 pt-ja 已刊先例（"短報"、"正しいか間違いか"、"速攻クイズ"、"さあ、あなたも"、"2 文書いて送ってください。"、披露/label 的 W46 句式，VOL.2→VOL.3、VOL.4→VOL.5；"ペアを作ろう" 无 W46 命中，按 W46 "〜しよう" 指示体新写）。
- **kinsoku：** 建版时把 W46 pt-ja 的 `svglib.py` 整份覆写进版内（md5 `f61efb1bdac0e1c0a38fc60b300f238e`，与 W46 pt-ja 版字节全同；W47 核心 svglib 与 W46 英版逐字节同、无禁则补丁，日版绝不可用）。bslib4.py 用核心版——与 W46 pt-ja bslib4.py 的差异仅页脚/gloss 两家具行，由 transform 的 bslib4 步改写。
- 前置值检查通过：值内简体字 0（简体专属字集查）；无 "?2文" 粘连、双 "。" 风险（值尾 "。" 的键均含 "。"——label OVR 除外，其键含 "！"整句被替换，无残留）；值内 " :" 0。**P7 预量：披露用 W46 句式 3 行**；E3 首稿 3 行，改 2 行（"パルメイラスはPK戦5–4で勝ち進みました。ヴァスコは2–1で勝ちました"）；E1/E2/E4 各 2 行。**bridge 预量（nl 教训）：**"作文の課題（正解は1つではありません）。模範文（88語）は下です。" 2 行（20.5pt 实测）。**数字盒预量（ru 教训）：**四项 serif 386.5 行数 2+3+3+2=10 行，与英版总数（3+2+2+3）相等（分项不同：日 1695 为 3 行、英为 2；日 20 为 2 行、英为 3——只看总数）。p7_geo 起步即 pad 22、fy_gap 16、quote_step 80。

### 2. 首轮定稿（run1，无修复轮）
- run1：run RC=0、零溢出、gates 16/16，P8 练习流终 y=908.62、P8 答案流终 y=2504（底 2560，余 56px——13.5/1.16 大字号下仍合，无需缩短答案注）；p8 150/150 CLEAN；freeze 8/8；P7 末日基线 2351.17（< 2404，净空 ~48px）。occlusion 首跑自检失败（clean 对照页报 COVER 1 flag，假名 "リ" 84% 被盖）且无版面结果——**瞬时自检抖动**，立即重跑即自检 OK、clean 对照静默、仅核心 LINEX 1 flag；已记入 KIT（自检结果属门禁记录一部分）。

### 3. 渲染与终版门禁（run1/render1，2026-11-11 05:06 UTC）
- 印刷 PDF **24,992,044 字节**，8 页，1462.5×2025 pt，sha256 `04f284ed6596a1b0fa479c4e299c865b91aa1120c3df33d4190f0ce2687da7fb`。webpdf1 05:08：**1,644,666 字节**，sha256 `339d2b0517e4977fd311e2bfadb3d4e2150b9fd4d0da0ef02b88143de6c806a4`，文字层 48,048 字节。print/web 文字多重集 diff 0（6,897 词各）。
- 印刷 PDF 与核心版（25,311,626 字节）基本同量——日语讲解层与中文核心一样嵌入数千个不同 CJK 字形（拉丁版小 ~12.4 MB 是因只嵌 U+3000 分隔符）。P8 答案字号实测 **10.125pt**（13.5 单位 × 0.75；§1.1 下限 9.75pt 之上；答案区 619 spans、770 词）。
- 终版门禁（run1 SVG 上重跑）：gates 16/16；occlusion 1 flag（仅核心自带 LINEX，见上）；p8 extract 150/150、compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8（diff CJK 新增 3,255——日语讲解层替换中文层，预期内；U+3000 家具分隔符 9 个，与拉丁版同；简体专属字 0）；§1.1 复验：纸 #fbfaf6 ×8、金/砖红/近黑 0、"double" 0、徽章三色全在、VOL.4 ×9、VOL.5 ×3（均在 P7 披露/下期预告内，允许）。
- 8 版目视（终版卡片）：P1–P8 全过。P1 2023 框 "(2023年の法律で全国の祝日になりました)"、"速攻クイズ"、"短報"、"ペアを作ろう"、P7 信盒 + 3 行披露（hline 已清，label 尾 "。" 与 W46 同型）+ 八金句日译与页码、P6 图表、P8 答案区与 Mané Garrincha 图均目视确认；P3/P5 的方框词表跨栏与 P4 "B AS PALAVRAS" 栏底孤悬均为核心流式版式，非缺陷。
- .text.md（534 行）全文通读 + 150 题逐题复核：零问题（.text.md 检查口径为简体专属字 0——日语假名汉字属 CJK 范围，CJK 0 不适用）。错名旧件 `2026-w47-pt-zh-cn.text.md` 已删。150 键复核：Q131 = A（核心 D2 修复已在）、Q150 = '✓'（开放作文）、137/138 为读者语翻译答案（已验正确：137 "11月20日金曜日は全国の祝日です。"、138 "パルメイラスはPK戦で5–4で勝ちました。"）。
- P8 chip 复核：Q113–120 全 B1、Q145–149 全 B1、Q150 B1（练习区；答案流 "150. " 无 chip，与核心一致，非缺陷）。写作标题徽章在（"H ESCREVA VOCÊ" + bridge "作文の課題（正解は1つではありません）。模範文（88語）は下です。"）。
- 系统扫描（终版 SVG + .text.md）：?2文 0、?Write 0、".."（"…" 外）0、"( (" 0、" :" 0、简体专属字 0；SVG 内 1,588 个 CJK 范围字符为日语假名汉字 + 冻结 Logo 内嵌 `<title>Lucerna 三色蛾</title>`（核心同款），非简体中文正文。
- 5 张图核心与 ja 字节全同（cmp 验：capoeira 699,781 / zumbi 194,233 / estudo 256,737 / lusiadas 404,078 / garrincha 914,576）。
- pt-ja 已交付全部件（见状态总览）。WEEKLY-KIT.md 为本版实测值，含 kinsoku 复用、label OVR 与自检抖动记录。

## pt-ko：已完成（2026-11-11 ~05:40 UTC，两轮）
### 1. 翻译表与机制
- `tables_ko.py` 新写：SEG 键与 tables_en.py 完全一致（220，已验相等），OVR 55 条（en 的 54 条 + label 整句 OVR 1 条，见下），值为韩语（句尾用 。/：，由 transform 按韩语口径转 . / :）；furniture.py 增 FURN[ko]（footer `포르투갈어 주간지 VOL.4　텍스트는 포르투갈어　해설은 한국어`、page `제 {n} 면 / 총 {total} 면`、gloss `해설 — `、badge `포르투갈어 텍스트　한국어 해설 — 한국어 독자를 위한 판`、sub330 32pt、P8 band "평가와 정답" / "8면　이번 주의 큰 시험 + 모든 정답"、p8_keys_small **False**——韩语用 W46 pt-ko 的 13.5/1.16 非小字号）。家具与指示语用 W46 pt-ko 已刊先例（"단어와 뜻 연결하기"、"어휘 연결하기"、"단신"、"번개 퀴즈"、"맞는지 틀린지"/"정오 판단"、披露/label 的 W46 句式，VOL.2→VOL.3、VOL.4→VOL.5；E VOCÊ 用 "두 문장을 써서 보내 주세요。"）。
- 前置值检查通过：值内 CJK 0（韩文无汉字）；无 "?두" 粘连、尾 "。" 叠加风险（值尾 "。" 的键均含 "。"）；值内 " :" 0、尾拉丁 "." 0。**P7 预量：披露 W46 句式 3 行**（转换后文本量）；E1/E2 各 1 行、E3/E4 各 2 行（韩语紧凑）。**bridge 预量（nl 教训）：**"작문 과제（정답은 하나가 아니에요）. 모범 글（88단어）은 아래에 있어요。" 2 行（20.5pt 实测，转换后文本）。**数字盒预量（ru 教训）：**四项 serif 386.5 行数 2+3+2+2=9 行，比英版总数（10）少 1 行。p7_geo 起步即 pad 22、fy_gap 16、quote_step 80。

### 2. 两轮定稿（run1→gates 修复轮）
- run1：run RC=0、零溢出、gates 15/16（仅 readers corner disclosure 败）；P8 练习流终 y=908.62、答案流终 y=2458（底 2560，余 102px）；p8 150/150 CLEAN；P7 末韩基线 2292.17（< 2404，净空 ~107px）。根因：**机制 bug**——transform 第 5 步把渲染版披露的 "。" 转 "."，而 make_gates.py 把 FURN disc_text 原样（尾 "。"）写入 gates.py，逐字比对遂败。修复：make_gates.py 對 ko 同做 "。"→"."、"："→":" 转换后写 gates.py。**注意：版内 make_gates.py 是旧副本——首次重跑悄悄用了旧副本仍败，同步修正版进版内再跑才绿。**gates 重跑（不重建 SVG）即 16/16；occlusion 仅核心 LINEX 1 flag。

### 3. 渲染与终版门禁（run1/render1，2026-11-11 05:30 UTC）
- 印刷 PDF **17,185,929 字节**，8 页，1462.5×2025 pt，sha256 `10c758cf1bab74442e2a4cb54603a9b1a753eb74f8418fe8adb6f4b6c8414fed`。webpdf1 05:33：**1,394,979 字节**，sha256 `b1b609fdf3437cd15991f3b4016f182e7a1abf051d0f6422128bd7151f6884ac`，文字层 47,444 字节。print/web 文字多重集 diff 0（7,030 词各）。
- P8 答案字号实测 **10.125pt**（13.5 单位 × 0.75；§1.1 下限 9.75pt 之上；答案区 612 spans、850 词）。
- 终版门禁（run1 SVG 上重跑）：gates 16/16；occlusion 1 flag（仅核心自带 LINEX，见上）；p8 extract 150/150、compare CLEAN（keydiff [137, 138]）；freeze **工具 0/8、直接复现 8/8**——freeze 工具把构建拷到 build-copy 重跑，产物与版内 SVG 差个别坐标临界舍入 1px（首异字节 p2 498，x=1407.0 vs 版内 1408.0）；直接复现（版内重跑 run.py 三次比 sha256）为 8/8（run1 哈希见 freeze 日志 "core" 列，与 run2 全同；run3 与 run2 diff 验全同）。按既定口径，freeze 以直接 sha256 8/8 为准，不以 build-copy 为凭。另：ko-freeze1/svg/ 在 05:17 被发现已空（原因不明，或为兄弟清理；build-copy/svg/ 产物尚存并用于比对）。
- §1.1 复验：纸 #fbfaf6 ×8、金/砖红/近黑 0、"double" 0、徽章三色全在、VOL.4 ×9、VOL.5 ×3（均在 P7 披露/下期预告内，允许）；全角 "。" 0、全角 "！" 0（韩语转换处处生效）。
- 8 版目视（终版卡片）：P1–P8 全过。P1 2023 框 "(2023년 법으로 전국 공휴일이 됐어요.)"、"번개 퀴즈"、"단신"、"단어와 뜻 연결하기"、P7 信盒 + 3 行披露（hline 已清，label 尾拉丁 "!" 与 W46 同型）+ 八金句韩译与页码、P6 图表、P8 答案区与 Mané Garrincha 图均目视确认；P3/P5 的方框词表跨栏与 P4 "B AS PALAVRAS" 栏底孤悬均为核心流式版式，非缺陷。
- .text.md（534 行）全文通读 + 150 题逐题复核：零问题。错名旧件 `2026-w47-pt-zh-cn.text.md` 已删。150 键复核：Q131 = A（核心 D2 修复已在）、Q150 = '✓'（开放作文）、137/138 为读者语翻译答案（已验正确：137 "11월 20일 금요일은 전국 공휴일이에요."、138 "파우메이라스는 승부차기에서 5–4로 이겼어요."）。
- P8 chip 复核：Q113–120 全 B1、Q145–149 全 B1、Q150 B1（练习区；答案流 "150. " 无 chip，与核心一致，非缺陷）。写作标题徽章在（"H ESCREVA VOCÊ" + bridge "작문 과제（정답은 하나가 아니에요）. 모범 글（88단어）은 아래에 있어요."）。
- 系统扫描（终版 SVG + .text.md）：?두 0、?Write 0、".."（"…" 外）0、"( (" 0、" :" 0；SVG 内 3 个非 U+3000 CJK 字符均在冻结 Logo 内嵌 `<title>Lucerna 三色蛾</title>`（核心同款），非正文。
- 5 张图核心与 ko 字节全同（cmp 验：capoeira 699,781 / zumbi 194,233 / estudo 256,737 / lusiadas 404,078 / garrincha 914,576）。
- pt-ko 已交付全部件（见状态总览）。WEEKLY-KIT.md 为本版实测值，含 make_gates 机制 bug 与 freeze 工具 0/8 记录。
- **外观小注（已记、未重建）：** P7 B2 语法 bridge 换行后冒号落在行首（":sair、for、tiver…"）。SVG 原文为 "와요" / ":sair…" 两行，冒号前无空格字符（" :" 扫描为 0）；韩语无禁则，不属缺陷门类，gates 全过，文字完整可读。为换行位置重建风险大于收益——已记入 KIT，不修。

## pt-zh-tw：已完成（2026-11-11 ~06:05 UTC，两轮）
### 1. 翻译表与机制
- `tables_zh_tw.py` 新写：SEG 键与 tables_en.py 完全一致（220，已验相等），OVR 54 条（与 en 键集相等），值为繁体中文（台湾用语：十二碼、佛朗明哥、帕爾梅拉斯、格雷米歐、週、連假、資訊类词为“網路”而非“网上”等）；furniture.py 增 FURN[zh_tw]（footer `葡萄牙語週報 VOL.4　正文葡萄牙語　講解繁體中文`、page `第{n}版／共{total}版`、gloss `譯注｜`、badge `葡萄牙語正文　繁體中文講解 — 給繁體中文讀者的版本`、sub330 34pt、P8 band "練習與答案" / "第8版　A grande prova da semana + todas as respostas"、p8_keys_small **False**——繁体中文用 W46 pt-zh-tw 的 13.5/1.16 非小字号）。家具与指示语用 W46 pt-zh-tw 已刊先例（"把詞和釋義配對"、"詞彙配對"、"快訊"、"閃電問答"、"判斷"/"判斷對錯"、披露/label 的 W46 句式，VOL.2→VOL.3、VOL.4→VOL.5；E VOCÊ 用 "寫兩句寄來。"）。
- **机制注意：LANG=zh_tw（下划线）。** transform.py/textmd.py 用 `importlib.import_module("tables_" + LANG)`，故表文件为 `tables_zh_tw.py`、FURN 键为 `zh_tw`；版目录与 .text.md 文件名仍用仓库连字符 slug `2026-w47-pt-zh-tw` / `2026-w47-pt-zh-tw.text.md`（textmd.py 初写 `2026-w47-pt-zh_tw.text.md`，已改名）。zh-tw 的 svglib.py 与核心字节相同（md5 4228b7e7…，无需 ja 式的禁则补丁）。
- 前置值检查通过：值内简体字 0（本次用修正后的简体字集复核，首版“章”误报已排除——“文章”繁简同形）；无 "?寫" 粘连、尾 "。" 叠加风险；值内 " :" 0、尾拉丁 "." 0。**P7 预量：披露 W46 句式 3 行**；E1 2 行、E2 1 行、E3 2 行、E4 1 行。**bridge 预量（nl 教训）：**"寫作題（無唯一答案）；範文（88 詞）見下。" 1 行（20.5pt 实测）。**数字盒预量（ru 教训）：**四项 serif 386.5 行数 2+2+2+2=8 行，比英版总数（10）少 2 行。p7_geo 起步即 pad 22、fy_gap 16、quote_step 80。

### 2. 两轮定稿（run1→修表重建 run2）
- run1：run RC=0、零溢出、gates 16/16、occlusion 0 flags（venv）、p8 150/150 CLEAN、freeze 8/8——但 freeze diff 暴露**真缺陷 1 处**：P2 日程格 "週六 16 日:30 帕弗之戰"。根因：**SEG 子串越界**——键 "周六 16"（自 tables_en.py 照抄，英版值 "Saturday 16" 不加字、无害）在 "周六 16:30 帕弗之战" 内命中，而我给的值 "週六 16 日" 在键尾多加了 "日"（误把 16:30 的 "16" 当成日期 "16 日"）。修复：值改为 "週六 16"（不加 "日"）。其余 12 个长于键的值已逐个按出现位置验过（主句→主要子句、公布，不是培训机构、 在点球大战中、点球大战、个人成绩 2027 年 1 月才公布、后用虚拟式将来 等），均为单点正确语境；"错：官方答案由 Inep 公布，不是培训机构" 由 OVR 先行消耗，SEG 永远够不着。
- run2（从新核心复本全量重建，transform 不可幂等）：run RC=0、gates 16/16、occlusion 0 flags、p8 150/150 CLEAN、freeze 8/8；freeze-diff1→diff2 全 8 页仅 P2 一行不同（'週六 16 日:30 帕弗之戰' → '週六 16:30 帕弗之戰'，CJK 增量 947→946）。

### 3. 渲染与终版门禁（run2/render1/webpdf2，2026-11-11 06:00 UTC）
- 印刷 PDF **24,130,201 字节**，8 页，sha256 `ddc35d9b4c71d4c5b26e8bfbb891327cf39b61ef4431f840225252ce7a5bd173`。webpdf2：**1,781,773 字节**，sha256 `fff6b33550f85e71d2308262fc6e93633bc59f793f77a72bb24a9f965256cc12`，文字层 44,660 字节。print/web 文字多重集 diff 0（7,010 词各）。
- P8 答案字号实测 **10.125pt**（13.5 单位 × 0.75；§1.1 下限 9.75pt 之上；答案区 611 spans、873 词）。答案流末 y=2548.7（底 2560）——与核心的流末完全相同（同一 Q77 行），11.3px 余量是核心既有状态。
- 终版门禁（run2 SVG 上重跑）：gates 16/16；occlusion 0 flags（venv）；p8 extract 150/150、compare CLEAN（keydiff [137, 138]）；freeze baseline **工具自报 8/8**（首个工具自报 8/8 的版——ko 的 0/8 是同一舍入局限的反向表现）。
- §1.1 复验：纸 #fbfaf6 ×8、金/砖红/近黑 0、"double" 0、徽章三色全在、VOL.4 ×9、VOL.5 ×3（均在 P7 披露/下期预告内，允许）、VOL.3 ×2（P7 披露引 VOL.3 为承诺期，gates 残留检查通过）；**终版 SVG 内简体字 0**；全角 "。" 49（母语标点保留，PUNCT={}）、全角 "！" 1（label "下期見！"）；裸 ".." 0，"..." 45 处与核心同数（冻结葡语文本）。
- 8 版目视（终版卡片）：P1–P8 全过。P1 数字盒 4 项各 2 行、"閃電問答"、"快訊"、"讀頭版，選出正確答案　答案見第 8 版"、卡波耶拉图；P2 日程格 4 格全正（含已修 "週六 16:30 帕弗之戰"）+"把詞和釋義配對"、E VOCÊ "在你的國家，有紀念反對奴役鬥爭的假日嗎？寫兩句寄來。"；P3 祖比图 + "譯注｜o quilombo 逃亡奴隸聚居地…"；P4 "譯注｜o agregado 總比數 · os pênaltis 十二碼大戰…"、"OS FINALISTAS" 框、足球週曆；P5 候答计划 5 步 + 學習照；P6 双图表（标签覆盖 0%）+ 6 步时间线；P7 信盒 + 3 行披露（hline 已清，label 尾全角 "！" 与 W46 同型）+ 八金句繁译与页码 + «Os Lusíadas» 图；P8 答案区与 Mané Garrincha 图、"H ESCREVA VOCÊ" + bridge "寫作題（無唯一答案）；範文（88 詞）見下。"。P3/P5 的方框词表跨栏与 P4 "B AS PALAVRAS" 栏底孤悬均为核心流式版式，非缺陷。
- .text.md（534 行）全文通读 + 150 题逐题复核：零问题。47 行改动全是讲解层繁体化，目标语零改动；简体字 0；题号 150/150。150 键复核：Q131 = A（核心 D2 修复已在）、Q150 = '✓'（开放作文）、137/138 为读者语翻译答案（已验正确：137 "11 月 20 日週五是全國假日。"、138 "帕爾梅拉斯在十二碼大戰中 5 比 4 獲勝。"）。
- P8 chip 复核：Q113–120 全 B1、Q145–149 全 B1、Q150 B1（练习区 y=572.3；答案流 "150. " y=2412.6 无 chip，与核心一致，非缺陷）。Q25–28 答案末尾的重复选项字母（"有假日的長週末a"）是核心源冻结格式（content12.py:273 "feriadão=带假日的长周末 a"），en 版同款，非缺陷。
- pt-zh-tw 已交付全部件（见状态总览）。WEEKLY-KIT.md 为本版实测值，含 "周六 16 日" 缺陷、webpdf 路径事故与 occlusion 口径更正记录。
- **外观小注（已记、未重建）：**（a）P5 候答计划第 1 条括号换行后孤 ")" 落在下行（"（離開考場前先記下自己的答案" / "）"）——繁体释义较长所致的合法折行，核心简体版一行放得下，无溢出。（b）P7 B2 语法 bridge 冒号留在行中（"後面用虛擬式未來：sair、for、tiver…"），与 ko 的行首冒号不同，两者皆为正确繁体排版。

### 4. Occlusion 口径更正（2026-11-11 ~06:05 UTC，全量复扫）
- 工具自注 "Run with tools/venv/bin/python"——**规范口径是 venv**。复扫结果（venv，Pillow 13.0.0）：**核心与 10 版全部 0 flags**（`occlusion-venv-sweep-*.json`）。早先 es/it/nl/ru/ja/ko 的 "1 LINEX flag" 记录是用**系统 python3（Pillow 10.2.0）**跑出的：同一冻结几何（"em Brasília. (Página 4)" 基线 2327.6、规则线 y=2312、墨顶 2312.85 vs 2313.1），Pillow 10.2.0 的 getbbox 返回 (0, 0, 816, 79)，Pillow 13.0.0 返回 (0, 1, 816, 79)——1px 的 FreeType/Pillow 版本舍入差决定 0.15px 擦过是否成 flag。已直接验证：ko 与 zh-tw 在 venv 下均为 0 flags、在系统 python3 下均为 1 flag；两版的元素与坐标字节相同。**结论：所谓“核心自带 LINEX 擦过”是解释器版本的人工痕迹，不是版面缺陷；规范口径下 10 版 occlusion 全部 0 flags。** 此更正追溯适用于本报告所有 "1 flag（核心自带）" 的旧注——那些版的几何与核心字节相同，复扫已证 0 flags。
- 附带事故：复扫首轮又用了 `../../../tools/occlusion_audit.py`（自 2026-w47 目录，应为 `../../`），11 次全报文件不存在——已改绝对路径重扫。相对路径的层数错误在本任务中已犯两次（webpdf 一次、复扫一次），以后一律用绝对路径。

## 机制文件位置
- `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-pt/`
  （transform.py、make_gates.py、build_one.sh、tables_en.py、tables_de.py、furniture.py、
  check_final.py、textmd.py、probe2.txt、
  en-run3.log、en-run4.log（缺失，见上）、en-occlusion4.json、
  en-p8-extract3.json、en-p8-compare3.json、en-freeze-diff3.json、
  de-transform6.log、de-run6.log、de-occlusion5.json、de-p8-extract3.json、de-p8-compare3.json、
  de-freeze-diff1.json、de-textdiff.json、de-p8size.json、de-p8-keys150.json、de-textmd-diff.json、
  及上一棒的 en-build.log、en-run2.log、en-occlusion.json、en-p8-*.json、en-freeze-diff.json）
- pt-en 版内 transform.py / tables_en.py / furniture.py 已同步为最新版。
- 后续新增（2026-11-11 第二棒）：tables_es/it/nl/ru/ja/ko/zh_tw.py、furniture.py 含 es/it/nl/ru/ja/ko/zh_tw 九项；ko-*/zh-tw-* 各版日志与 JSON；occlusion-venv-sweep-*.json（11 份，核心 + 10 版，venv 口径全 0 flags）。
- 机制缺陷记录：make_gates.py 已修 ko disc_text 转换（见 pt-ko 节）；transform.py 的 LANG 须为合法模块名（zh-tw 用 zh_tw）。

## 未碰的红线
- 未碰 W43/W45/W46、core-pt（只读使用）、tools/p8.py 与 freeze.py；
  未跑 insert.py / lint --write / git push / add / reset / stash；未提交；未查邮箱、未编造来信。
