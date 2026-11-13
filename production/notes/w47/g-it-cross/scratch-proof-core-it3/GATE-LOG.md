# GATE-LOG — 2026-W47 core-it fix3 独立复校（proof3）机械门与外部事实证据

复校员：子代理（独立复校，核心层）。日期：2026-11-11。
目标：`~/workspace/weekly-git/production/2026-w47/core-it/`。
正典工具：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`（md5 `ee7a55d8b2057cf4ad42a97bb1197383`，已验）。
标准工具：`~/workspace/weekly-git/tools/venv/bin/python`。
FIX-LOG：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-core-it1/FIX-LOG.md`（已读全文；§1.3/§1.4/§11 尤其重要）。
SOP：仓库根 `SOP.md`（319 行，已读全文）。
TMPDIR 全程指向 scratch 下 `tmp/`，未用系统 /tmp。
本日志中所有门均为复校员自己实跑；不信 KIT，只信自跑结果。

## §0 身份与仓库状态
- 印 PDF `La-Lucerna-VOL4.pdf`：SHA `2ee50d92635ba496d65c09c085a9b70fbebad62a8d6f3b81c41afec4be47a412`，27,726,350 B。网 PDF `La-Lucerna-VOL4-web.pdf`：SHA `ab14a5b7bbf532e0633fee0006f5c19f44bc558b9ad475ad523d5bd0aaaecab0`，1,790,620 B。text.md `2026-w47-it-zh-cn.text.md`：SHA `d0c573b83fa679262c2da0734b08b1f504782829c11d29c9ed1e2c8cac08dbcb`，52,676 B，1317 行。**三者与任务消息一致**（复校结束时复核一次，仍一致）。
- commit `36bdec2e`（完整 `36bdec2ed2b32000e512bfa65e7fb705464d8243`），仅含 5 个源文件（`content12.py`、`content34.py`、`content8.py`、`WEEKLY-KIT.md`、`2026-w47-it-zh-cn.text.md`），与 FIX-LOG §11 一致；`git cat-file -t 36bdec2e` = commit，`merge-base --is-ancestor 36bdec2e HEAD` 通过。复校期间 HEAD 前进至 `4b688318`（core-pt fix1，并行工作），目标文件未被改动。
- 仓库工作树另有大量已修改的 W43 文件（`git status` 显示 `M issues/2026-w43/...` 多项），与本次任务无关，未碰。核心目录 `git status --porcelain -- production/2026-w47/core-it/` 仅余未追踪文件（`??`：两份 PDF、assets/、bslib4.py、cards/、content56.py、content7.py、render.py、run.py、scratch/、svg/、svglib.py、ABSTRACT.txt），无 `M` 项——复校员未改动核心目录任何文件。
- KIT（`WEEKLY-KIT.md`，112 行）已读全文。定稿要点：8 页 1950×2700、四栏；150 题（P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 38；A2 47 / B1 70 / B2 33）；范文 99 词；P8 答案字号 13 SVG px = 9.75 pt。
- 版心右缘：1862 svg px = 1396.5 pt；P4 匹配 col2 右 961 px = 720.75 pt；P8 F col3 右 1411.5 px = 1058.625 pt；P4 col1 右 510.5 px；沟槽宽 28 px。200dpi 换算：render px = svg px × 2.08333；pt = render px × 0.36；墨水判据：通道 < 200。
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 返回 `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0；scratch 真实写文件通过（`probe.txt` 为 `probe-ok`）。

## §1 机械门实跑证据

### 1.1 occlusion 审计 — 8 页 0 flags
- selftest 通过：6 类阳性 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 全触发、干净对照沉默。
- 8 页审计：**0 flags**。日志 `occlusion-proof-it3.log`、JSON `occlusion-proof-it3.json`（flags []）。
- 注意：occlusion 对奶油框内溢出、框标题溢出、横向溢出、降部溢出是盲的——这些另行实测（§1.2/§1.6/§1.8/§1.9），不是因 occlusion 0 就放过。

### 1.2 正典 creambox 全版扫描 — 29 盒，负窗 8 处均为已知假阳性
- 工具：正典 `creambox.py`（md5 已验）。日志 `creambox-proof-it3.log`。
- 负窗清除量 8 处，逐项裁定：
  1. P1 IN QUESTO NUMERO 盒 −24.0：窗下行是下一节标题 "LA PAROLA DELLA SETTIMANA"，+24.0；盒内 +16.0。
  2. P1 IN BREVE −44.0：窗下行 QUIZ LAMPO 副标题，+44.0；盒内 +38.0。
  3. P3 译注盒 −37.0：窗下行 "IL TORRAZZO E IL TORRONE" 标题，+37.0；盒内 +47.7。
  4–6. P4 成绩表 3 处 −40.0/−40.0/−26.0：窗下行是下一日组的行——已用 SVG 结构证实为斑马纹：3 条奶油带 y=1156/1280/1404，各 h=62，间隔 124px，分别罩第 1/3/5 行，第 2/4/6 行故意在纸面；另 1492 行脚注在表外。
  7–8. P6 图表/PROPOSTA 两盒 −42.0：窗下行 "ESERCIZI 第 6 版练习" 标题，+42.0；盒内 +31.2/+90.0。
- desc-clear 负值 9 处（−1.1…−2.1）均为无降部字母末行的计量 artifact，像素实测全部在盒内（§1.3）。

### 1.3 盒底像素实测（desc-clear 负值 9 处全部证伪）+ P7 toolbox
- 200dpi 像素实测（`pixel3b.py`，输出 `render-scan-proof-it3.txt`；旧版 `pixel3.log` 的 P4/P8 "OVER" 值为未限 x 窗口误拾同行他栏墨水的假阳性，已废弃）：
  - P2 LO SAPEVI +5.4px、P2 E TU +3.0px、P3 IL WEEKEND DOLCE +5.4px、**P3 E TU +2.6px**（最差 −2.1 的那处）、P4 E TU +3.3px、P5 I GIOVANI IN NUMERI +5.6px、P5 E TU +2.6px、P7 三盒 +17.0/+3.4/+3.4px。末行墨全部在盒底之上。
- P7 toolbox clearance 实测：3 盒，min inside clearance +4.5，min desc-clear −1.5；像素实测 ERRORI TIPICI 末行墨底距盒底 +17.0px、LA PAROLA +3.4px、LETTERE +3.4px，全部在盒内。
- P3 E TU 盒底末行中文裁图目视确认："更喜欢牛轧糖还是巧克力？写两句寄来。" 完整、盒底留白清晰。
- 注意：早期一次 P3 E TU 裁图与 P7 工具箱裁图曾裁错栏（裁到 col2/col3），已按实测盒坐标（E TU/工具箱皆在 col4，x=1439.5）重裁并通过；像素定量结果不受影响（boxbottom 检查按盒底坐标找 rect）。

### 1.4 freeze baseline 8/8
- **8/8 字节一致**，rc=0；"core integrity: shipped core SVGs unchanged"。
- SVG SHA 与 FIX-LOG §0 逐一吻合：P1 `d301b8864a85bb31`、P2 `a744e5d25bce0cba`、P3 `fe0a0e658a9769bc`、P4 `12ddd86c49b5de42`、P5 `08929554b5265cd1`、P6 `621054eed30717df`、P7 `3746030ae86d2745`、P8 `779aa98cae7b8e28`（P5/P6/P7 与改前字节一致）。
- 日志 `freeze-baseline-proof-it3.log`，输出目录 `freeze-baseline-proof-it3/`（在 scratch 内，未碰 shipped 文件）。
- `freeze_direct` 不存在：`tools/freeze.py` 只有 `baseline`/`diff` 两个子命令，`freeze_direct` 报错 invalid choice——按任务要求记为方法备注（PROOF-NOTE O7），不是缺陷。freeze diff 只做 CJK 会计、p8 compare 只比键值，纯拉丁改动对两门皆盲（FIX-LOG §6 已记）；本次三法实测与手验已覆盖该盲区。

### 1.5 p8 extract / compare — 150/150，CLEAN
- p8 extract：noted set = **150/150**。日志 `p8-extract-proof-it3.log`，JSON `p8-proof-it3.json`。
- p8 compare（core P8 vs 自身，显式 `--core-p8`/`--edition-p8`）：CLEAN，missing=[]、extra_count=0、uncertain=[]、**keydiff=[]**，rc=0。日志 `p8-compare-proof-it3.log`，JSON `p8-compare-proof-it3.json`。
- 三方键比对（P8 SVG 打印键 vs text.md 题干键 vs RISPOSTE 列表）：**150/150 一致**，唯一"差异"为 ex.150 开放题（登记键为占位"（开放题，范文如下）"、P8 印 "✓"，属预期行为）。见 `keycheck-150.json` 与 `p8key-vs-text-proof-it3.txt`。

### 1.6 boxtitle 逐个实测（PIL 真墨为准）
- 84 行全大写/标题行（≥22px），脚本 `measure3.py boxtitle`，输出 `boxtitle-proof-it3.txt`。
- 最大真墨 1831.9px（P1 "本周意甲第 11 轮"，y=524），其次 1828.5、1822.5px；**全部在版心（1862px）内，余 ≥30.1px**，无框标题溢出。
- 全页 PIL 真墨扫描：除页脚 "第N版／共8版" 1862.1px（+0.1px，亚像素舍入噪声；occlusion 审计页脚带已豁免该基线）和刊头误测外，**无任何文本墨超 1862**。

### 1.7 印/网文字层比对
- `pdftotext` 两版各 44,001 B，`cmp` rc=0 **字节相同**（`wc -w` 各 5,950——与 KIT 写的 6,897 词计数口径不同，字节相同才是门；已记录此口径差异）。文本文件 `print-proof-it3.txt`、`web-proof-it3.txt`。
- 网 PDF：8 页，1462.5 × 2025 pt（`pdfinfo`）。

### 1.8 P8 最小字号实测（PyMuPDF 渲染 pt，非 KIT 配置 px）
- P8 最小 **9.75 pt**（534 个 span 处于该字号），全局最小亦 9.75 pt；P1–P5/P7 最小 11.62 pt，P6 最小 12.75 pt。符合 SOP §1.1 下限（不低于 9.75 pt）。
- 刊头实测：UnifrakturMaguntia 147.0 pt，bbox x 404.77–1058.04 pt，居中在版内。我方 PIL 脚本曾因用 Newsreader 度量刊头而误报 1988px 溢出——已用 PDF span 证伪，属我方脚本字体映射缺陷，非报纸问题（PROOF-NOTE O8）。

### 1.9 三法横向实测（自写脚本 `measure3.py` 用 builder 字体度量 + `pixel3b.py` 200dpi 像素）
- P2 匹配题（栏右 1862px/1396.5pt）：PIL 真墨 a 1811.5（余 50.5）、b 1830.5（余 31.5）、c 1806.5（余 55.5）、d 1821.5（余 40.5）；PDF span b 1375.1pt（余 21.4）、d 1367.6pt（余 28.9）、a 1359.8、c 1356.4；200dpi 像素 b 1374.1pt（余 22.4）、d 1366.6pt（余 29.9）、a 1359.4、c 1355.8。续行 novembre 1580.5px / chiesa 1539.5px。全部在版心内，与 FIX-LOG 数值在 0.4px/0.4pt 内一致。
- P4 匹配题（col2 右 961px/720.75pt）：PIL 真墨 a 877.9px、b 821.5（余 139.5）、c 943.5（余 17.5）、d 958.5（余 2.5）；PDF span b 617.2pt、c 708.6pt、d 721.7pt、a 未以完整串命中 span（换行故）；200dpi 像素 a 658.4pt（余 62.3）、b 615.6pt（余 105.1）、c 707.0pt（余 13.7）、d 720.7pt（余 +0.0）。**P4-d 是全期最紧的一行**：三法分别为 PIL +2.5px 在内、PDF span +0.95pt 在外（advance 框，含末字边距）、像素墨恰触栏边 961.0px（AA 边缘像素所致，±0.24px 量化）；以真墨（PIL getbbox）为准判在栏内，不构成缺陷（PROOF-NOTE O2）。
- P8 F 题（col3 右 1411.5px/1058.625pt）：PIL 真墨 a 1377.3（FIX-LOG 值；我方 dump 漏了 a 首行窗口，像素法补得 1379.0px）、b 1360.0（余 51.5）、c 1388.0（余 23.5）、d 1394.0（余 17.5）；PDF span a 1034.9pt、b 1021.1pt、c 1043.9pt、d 1046.6pt；200dpi 像素 a 1034.3pt（余 24.3）、b 1020.6pt（余 38.0）、c 1042.2pt（余 16.4）、d 1045.1pt（余 13.5）。全部在栏内。
- 全页 PDF span 扫描（阈值 1396.5+0.5pt）：仅 4 处超边距，皆为 D7 类（§1.10）。200dpi 全页逐行像素扫描：仅 p2（1189–1191pt）、p5（451–453pt）、p8（446–448、450、461–463、465–466pt）有墨水过 1396.5pt，其余 5 页干净。

### 1.10 D7 亚 2pt 痕迹类（方法备注，非缺陷）
- PDF span 超边距 4 处——P2 副标题 "Una festa, una giornata verde" +1.62pt、P5 Corot 图注 +1.59pt、P8 范文两行 +1.84/+1.93pt（另 P1 "2026" +0.2pt、P2 图注 +0.0pt 在我方 +0.5pt 阈值之下，未列入）；200dpi 像素墨分别为 +0.7pt、+0.3pt、+1.0/+1.0pt。属渲染器与度量字体 advance 差（约 0.5–0.8%），无碰撞、无裁切。
- FIX-LOG §7 称三数值在 it-de/it-ja/it-en 已发 PDF 中完全相同——**我未独立核实该跨版断言**（见 §4）。按本轮实测：痕迹为 0.25–0.35mm、版内 65pt 以上白区，属方法备注（PROOF-NOTE O3）。

### 1.11 弯引号全版扫描
- U+201C/U+201D 在 text.md 3 对（皆在中文讲解层：P1 "la vetta"、ex.32/33 答案注 "Fate dolci" 两处）；SVG 中仅 P1 1 对（"la vetta" 中文 gloss 行，y=1816.2）、P8 1 对（"Fate dolci" 答案注，y=2394.8）；U+2019 全版 0。
- 意大利语撇号统一用 ASCII '（U+0027，SVG 各页 3–16 处），属排版惯例；弯引号均正常渲染，无豆腐块（已看 P1 gloss 裁图：引号形态清晰；P8 "Fate dolci" 裁图小，引号可辨、无缺字）。法语式 « » 在各页成对出现（P7 24 对最多）。无引号类缺陷。

### 1.12 内部标签扫描
- text.md 中 "W47"/"SOP"/"proofread"/"cover"/"Cover" 均为 0 命中；"it-zh-cn" 与 "2026-w47" 各 1 命中，皆为首行 H1 `# 2026-w47-it-zh-cn`。
- 查证：导出脚本 `export_w47_textmd.py` 第 21 行 `out_lines = [f"# {slug}", ""]`（slug 硬编码），且 W46 已发版 `issues/2026-w46/2026-w46-it-zh-cn/2026-w46-it-zh-cn.text.md` 的 H1 同为 `# 2026-w46-it-zh-cn`——属 it 系既定导出格式（de 系则用正式标题如 `# Die Lucerna · VOL.3 — 9. bis 15. November 2026`，两系不一致）。不拦停（PROOF-NOTE O5）。

### 1.13 P4 成绩表栏间实测（O1 依据）
- PIL 真墨：Cagliari–Frosinone 522.0（超 col1 右 510.5 约 +11.5）、Torino–Lecce 971.0（超 961 +10.0）、Genoa–Milan 972.0（+11.0）、Roma–Sassuolo 991.0（+30.0，越过整条沟）、Fiorentina–Juventus 1040.0（+79.0）；与 FIX-LOG 数值在 0.4px 内一致。日志 `gutter-proof-it3.txt`。
- 机制：宽表故意跨栏（同行下一栏无文字，Monza–Atalanta 同行距 Genoa 墨 21px），零碰撞、读者不可见，维持 O1 观察项（与 FIX-LOG 一致）。

### 1.14 计数与程序校验（日志 `checks1.log`、`counts-proof-it3.txt`）
- 编号连续：numbered stems 150 个，min 1 max 150，missing []；RISPOSTE 150 条齐全；题干键与文末 RISPOSTE 列表程序比对 0 不一致。
- 级别：A2 47 / B1 70 / B2 33；每页题量与 KIT 一致（P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 38；计数脚本误将 P7+P8 合并为 Lingua 50，因 P8 标题为 "Valutazione e risposte" 两词、首词匹配失败——题号区间 101–112/113–150 已人工确认，分布无误）。
- 范文实测 99 词（与 KIT 一致）；头条 39 字符（不含空格，≤56）；8 句 P7 金句在 text.md 空白归一化全文中各出现恰好 2 次；MD11 十场比分之和 = 24 球；禁词 Ucraina/Russia/Putin 0 命中。
- 视觉裁图：200dpi 渲染 `render200/p-1.png`…`p-8.png`（4063×5625，已目视），`crops/` 下 11 张裁图均已目视通过。

## §2 外部事实来源（必查项 a–g 的外部核实）

以下为浏览器搜索 + `date` 命令核实。早期轮次（2026-11-11 上午）的搜索结果 URL 未随摘要保留全文链接，本节按域级来源记录；本轮补查的两项（DPB、Alba）给出完整 URL（逐字复制自搜索结果）。

### (a) D1 赛程与星期
- `TZ=Europe/Rome date` 核：11-06 周五、11-07 周六、11-08 周日、11-12 周四、11-15 周日、11-16 周一、11-17 周二、11-18 周三、11-19 周四、11-20 周五、**11-21 周六、11-22 周日**、11-23 周一、11-24 周二、12-02 周三、12-06 周日、12-31 周四。
- 意甲第 12 轮 11-21 至 11-23（来源：bergamoesport.it、tuttomercatoweb.com、sportradar.com、betsson.it、antoniogenna.com、matchcalendar.football 等）：Lazio–Lecce 周六 11-21 15:00（DAZN，Stadio Olimpico）、Atalanta–Inter 周日 11-22 20:45（DAZN，Gewiss Stadium, Bergamo）、Monza–Fiorentina 周一 11-23 20:45；第 12 轮周六另有 Como–Cagliari 15:00、Parma–Roma 18:00、Napoli–Torino 20:45；周日另有 Juventus–Venezia 12:30、Bologna–Udinese 15:00、Sassuolo–Genoa 15:00、Milan–Frosinone 18:00。
- 结论：P1 "domenica sera"（周日 20:45）无误；与 P4 及 P1 CIFRE 栏全部一致。

### (c) D11 Torrazzo
- it.wikipedia "Torri e campanili più alti d'Italia"：1º Mortegliano 113,20 m、2º Torrazzo 112,12 m（该表数字；Mortegliano 词条正文写 Torrazzo 112,54 m，测量口径差不影响名次）。
- "Campanile di Mortegliano" 词条："113,20 metri… il primo campanile, precedendo in altezza il più noto Torrazzo di Cremona (112,54 metri)"；Mortegliano 1955–1959 钢筋混凝土、非中世纪砖塔。
- Torrazzo 为中世纪砖塔，it-wiki 定性 "la torre medievale e la torre in laterizi più alta d'Italia"；wellme.it 亦称 "il campanile medievale in laterizio più elevato d'Europa"，112.54 m。

### (g) 外部事实抽查（全部证实）
- **MD11 全部 10 场比分与 20 队积分表**（来源：minuto91.it、williamhillnews.it、tuttomercatoweb.com、antoniogenna.com 等）：Venezia–Udinese 2-1、 Cagliari–Frosinone 1-0、Torino–Lecce 1-1、Parma–Bologna 1-2、Roma–Sassuolo 3-0、Napoli–Lazio 1-1、Genoa–Milan 1-2、Monza–Atalanta 0-1、Inter–Como 2-0、Fiorentina–Juventus 2-2；24 球；Lazio 29、Inter 28、Roma 27、Milan 24、Como 23、Frosinone 20、Juventus 18、Bologna 17、Cagliari 16、Napoli 15、Torino 14、Atalanta 14、Genoa 13、Lecce 10、Fiorentina 9、Parma 8、Sassuolo 8、Monza 7、Venezia 6、Udinese 5；Lazio 不败、Gattuso 执教、Roma 最佳进攻 31 球。
- **Torrone**：29 届 11-07 至 11-22、16 天、主题 «Il Confine»、1441 年 Sforza–Visconti 婚礼传说、闭幕日 11-22 Torrone d'Oro 授予 Davide Simonetta（11:00 Palatorrone，官网 festadeltorrone.com）、corteo 16:00（150+ figuranti）、rievocazione 17:00 Piazza del Comune、sbandieratori + 火把艺人、gran finale 18:00 «Il torrone va in brodo»。
- **Eurochocolate**：32 届 11-13 至 11-22、主题 «Fate dolci»、Calabria 首个 guest region（bergamotto、cedro、peperoncino、fichi cosentini）、Fri 11-20 18.15 «I tesori della Calabria Straordinaria»（LAB）、Sun 11-22 Iginio Massari 任 gran finale 嘉宾。
- **BookCity Milano**：15 届 11-23 至 11-29、主题 «Il senno sulla Luna»（Ariosto《Orlando Furioso》）、1,360 活动 / 2,487 嘉宾 / 1,164 书 / 443 场地、开幕周一 11-23 20:00 Teatro Dal Verme（Colson Whitehead，2 次 Pulitzer）、anteprima 周日 11-22 16:00 Edmund de Waal（Fondazione Luigi Rovati）。
- **Torino Film Festival**：44 届 11-24 至 12-02、9 天。
- **ATP Finals**：11-15 至 11-22、Inalpi Arena、8 单打（Zverev No.1、Alcaraz、Shelton、Medvedev、Cobolli 首秀、Fils、Tiafoe、Jodar）、Sinner 因膝伤缺席（2024–25 冠军）、抽签周四 11-12、McEnroe/Lendl 分组、决赛周日 11-22、双打 Bolelli/Vavassori。
- **Madonna della Salute**：11-21、1630 瘟疫誓愿、Longhena 1631–1687、船桥 ponte votivo、蜡烛、castradina 于 11-20 晚食用、"quasi quattrocento anni"（1630→2026 为 396 年）。
- **Festa dell'albero**：1898 年起源、2013 年立法为国家日；**Santa Cecilia** 11-22 为音乐主保。**Sforza–Visconti 婚礼 1441-10-25** 属史实。
- **Manovra**（来源：hot-news.it、cifonenews.it、publicpolicy.net、2duerighe.com 等）：DPB 10-15 送布鲁塞尔、CdM 10-28 批准约 26bn（报章重建口径）、法案号 C. 3174-bis、听证会 11-09 至 11-12（Giorgetti 周四 11-12 约 16:00）、修正案截止周二 11-17 18:00、12-31 前终批。
- **Manovra 数字（本轮补查，完整 URL）**：
  - https://www.doppiominimo.com/manovra-2027-numeri-dpb-cosa-cambia-investitori/ — DPB 13/10 获批、15/10 送交；manovra lorda 约 23,5 mld（0,98% PIL）；deficit/PIL 2,9%（2026）、3,4%（2027）、3,2%（2028）；crescita +1,0%（2026）、+0,8%（2027）。
  - https://sienapost.it/global/economia-lavoro-global/bozdpb-2027-deficit-debito-clausola-salvaguardiaza-automatica/ — DPB 13/10 议定，crescita 1,0%/0,8%，indebitamento netto 2,9%→3,4%→3,2%→2,3%，debito 138,1%→138,5%（2027）。
  - https://www.reteconomy.it/manovra-2027-23-5-miliardi-che-dipendono/ — DPB 15/10 抵达布鲁塞尔，法案 23,5 mld，deficit 3,4%（2027）。
  - https://ogginews.com/economia/2026-10-16-manovra-2027-dpb-bruxelles-banche/ — MEF 15–16/10 夜间送交，DPB 44 页，23,5 mld，deficit 3,4%（2027）、3,2%（2028）。
  - https://parlamentonews.com/manovra-2027-il-cdm-approva-il-testo-da-235-miliardi-oltre-la-meta-e-in-deficit-5-miliardi-dalle-banche/ — CdM 28/10，23,5 mld，contributo banche/assicurazioni ~5 mld（2027），deficit 3,4% PIL，PIL 增长 0,8%。
  - https://www.dirittobancario.it/art/mef-approvato-il-documento-programmatico-di-bilancio-2027/ — MEF 15/10 发布 DPB 2027，PIL +1,0%（2026）/+0,8%（2027）/+0,9%（2028），indebitamento netto 2,9%/3,4%/3,2%。
  - 报纸措辞对照：正文 "circa 26 miliardi… secondo le ricostruzioni dei giornali"（行 653）与 "circa 5 miliardi dal settore finanziario… secondo le prime ricostruzioni"（行 657）均属有来源的谨慎措辞，与上述口径一致，未把报章重建数写成定论。
- **Alba 白松露节（本轮补查，完整 URL）**：
  - https://www.fieradeltartufo.org/en/alba-truffle-fair-events/alba-white-truffle-world-market/ （官网）— Dates: Every Saturday and Sunday from October 10 to December 6, 2026。
  - https://www.italia.it/en/piedmont/cuneo/alba/things-to-do/event-alba-white-truffle-fair （Italia.it）— When: 2026-10-10 to 2026-12-06。
  - https://dovevado.net/sagra-tartufo/ 、https://www.piemonteweekend.it/articoli/sagre-settembre-piemonte/ 、https://www.secretpiemonte.com/alba-truffle-fair-guide/ 、https://www.ilmeteo.net/notizie/tempo-libero/fiera-del-tartufo-bianco-d-alba-2026-cosa-vedere-nel-weekend-del-17-e-18-ottobre-orari-ed-eventi.html 、https://www.spezialewineresort.it/en/alba-white-truffle-fair/ 、https://piccoloexplorer.com/international-alba-white-truffle-fair-with-kids/ 、https://www.passaportodifamiglia.com/en/italy/piedmont/international-alba-white-truffle-fair/ 、https://winetravelguides.com/festivals/alba-white-truffle-fair — 均称 10 月 10 日–12 月 6 日，第 96 届（正文未写届数，故 k 96 无冲突）。正文 "continua fino al 6 dicembre"（行 311/329）与 ex.33 键 B 正确。

### (d) D12 接受记录
- 全源 grep：`content*.py`、text.md、SVG 中 "18 novembre"/"mercoledì"/"MER 18" **零命中**。
- text.md 全部 "18" 命中：行 75（"entro il 17, ore 18"）、195/233（年份 1898、1630）、263（题号 18）、275（选项年份）、307/325（"fino alle 18"）、567（年份 1868）、655/677（"alle 18" 修正案截止）、737（题）、921/939/943/1053/1197/1253/1269（题号/年份/时间）。无一为 11 月 18 日事件。
- P6 "LA STRADA DELLA MANOVRA" 四步 28 OTT / 9–12 NOV / MAR 17 NOV / 31 DIC 无 11-18 事；P5 "IL PIANO DELLA SETTIMANA" 五条为周五/周六/周日/周日/周一，无周三。6 天为编辑选择、未编造内容。**接受记录已核实。**

## §3 判为非缺陷的项（裁决记录）
1. creambox 8 处负窗 + 9 处 desc-clear 负值 —— 均为已知假阳性，逐项裁定见 §1.2/§1.3；像素实测最紧处 +2.6px 在盒内。
2. P4 成绩表 5 行伸入栏间沟槽 —— 宽表故意跨栏，同行下一栏无文字，零碰撞（§1.13；PROOF-NOTE O1）。
3. P4-d 三法分歧 —— 真墨在栏内，仅 span advance 框 +0.95pt 在外、像素墨恰触栏边；无进入他栏文字的路径（§1.9；PROOF-NOTE O2）。
4. D7 亚 1pt 痕迹 4 处 + P1 dateline "2026" +0.22pt —— 0.25–0.35mm，版内 65pt 白区，无裁切/碰撞（§1.10；PROOF-NOTE O3）。
5. P4 日标签重复（SAB/DOM ×2）—— 分组版式，每行自洽（PROOF-NOTE O4）。
6. text.md H1 slug —— it 系既定导出格式，W46 已发版同然；管线级，非 fix3 引入（§1.12；PROOF-NOTE O5）。
7. ex.58 主观比较级、ex.82 apertura/anteprima 区分 —— 合法练习设计（PROOF-NOTE O6）。
8. 页脚 "第N版／共8版" 真墨 1862.1px（+0.1px）—— 亚像素舍入噪声；occlusion 审计页脚带已豁免该基线。
9. `wc -w` 5,950 vs KIT 6,897 —— 计数口径不同（KIT 法计入 CJK 字符）；印/网文字层字节相同才是门。
10. P4 匹配 a 未以完整串命中 PDF span —— 因换行拆串；像素法已补测 658.4pt（余 62.3），在栏内。

## §4 未核实项与限制（必须如实记录）
1. **FIX-LOG §7 跨版断言未核实**：称 D7 三数值在 it-de/it-ja/it-en 已发 PDF 中完全相同——本仓无 `issues/2026-w47/` 目录，无法核对。另查 W46 已发版 `issues/2026-w46/2026-w46-it-zh-cn/2026-w46-it-zh-cn.pdf`：span x1>1397.0pt 多达 60+ 处（最高 1415.34pt），但 W46 为旧版式（版心更宽：页脚 "第1 版/ 共8 版" span 至 1414.3pt），绝对 pt 值不可与新版式横比；该对比不能证实也不能证伪 §7 断言，仅说明跨版式数值不可比。D7 痕迹本身在本版已实测为 0.25–0.35mm、版内白区，不影响结论。
2. **早期轮次搜索结果的完整 URL 未随摘要保留**：§2 中 (a)(c)(g) 的早期来源以域级记录（bergamoesport.it、tuttomercatoweb.com、minuto91.it 等）；本轮补查的 DPB 与 Alba 两项有完整 URL。其事实结论（比分、日期、届数、时间线）均已多源交叉证实。
3. 早期一次 P3 E TU / P7 工具箱裁图裁错栏，已重裁通过；定量结果不受影响（§1.3 注）。
4. P8 F-a 的 PIL 首行窗口 dump 漏值，像素法补得 1379.0px；与 FIX-LOG 值 1377.3px 在 1.7px 内，结论不变。

## §5 文件清单（scratch）
- `PROOF-NOTE.md`、`GATE-LOG.md`（本文件）、`keycheck-150.json`
- `occlusion-proof-it3.log/.json`、`creambox-proof-it3.log`、`freeze-baseline-proof-it3.log`、`freeze-baseline-proof-it3/`、`p8-extract-proof-it3.log`、`p8-proof-it3.json`、`p8-compare-proof-it3.log/.json`、`print-proof-it3.txt`、`web-proof-it3.txt`、`checks1.log`、`counts-proof-it3.txt`、`boxtitle-proof-it3.txt`、`gutter-proof-it3.txt`、`h-scan-proof-it3.txt`、`h-scan-all-proof-it3.txt`、`h-scan-matchlines-proof-it3.txt`、`h-pdf-scan-proof-it3.txt`、`render-scan-proof-it3.txt`、`boxbottom-proof-it3.txt`、`p8key-vs-text-proof-it3.txt`、`measure3.py`、`pixel3.py`、`pixel3b.py`、`render200/`（8 页 200dpi PNG）、`render200.log`、`crops/`（11 张裁图）、`tmp/`（TMPDIR）、`probe.txt`
- 注意：`pixel3.log` 为旧版像素脚本输出，内含已废弃的假阳性 OVER 值——以 `render-scan-proof-it3.txt` 为准，不得引用旧值。
