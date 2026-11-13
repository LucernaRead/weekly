# PROOF-NOTE — 2026-W47 nl → fr（proof1，独立复校）

- 版：`production/2026-w47/fanout-nl/2026-w47-nl-fr/`（nl 家庭，`fanout-nl/` 子目录）
- 印 PDF：`De-Lucerna-VOL4-nl-fr.pdf`（12,704,394 字节）
- 网 PDF：`De-Lucerna-VOL4-nl-fr-web.pdf`（1,577,894 字节）
- text.md：`2026-w47-nl-fr.text.md`（47,536 字节）
- 复校员 scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-fr1/`
- 日期：2026-11-11（America/Toronto）

## 结论：(b) 有缺陷，不能定稿

共 **4 项缺陷**：D1（中）、D3（中偏轻，机制）、D4（轻）、D2（极轻、边界）。
全文通读（印 PDF 8 页卡片 + text.md 全文）、150 题逐题手验（见 `keycheck-150.json`，150/150 通过）、
全部机械门实跑。缺陷以外未再发现问题。

## 缺陷清单

### D1 — P7 框标题溢出奶油盒（中）
- 位置：P7 右栏 `HET WOORD` 奶油盒标题 `HET WOORD　LE MOT DE LA SEMAINE`（SVG `p7-taal.svg`，框 y=1030–1340.5，框右界 x=1862.0）。
- 实测（三法一致）：
- PIL 真墨迹（Noto Sans CJK SC Bold 23pt，框题实际字体）：墨右 x=1883.6，超框右 **21.6 px**；
- 印 PDF 词位：末词 `SEMAINE` x1=1413.5 pt，框右=1396.5 pt，超 **17.0 pt（= 22.7 SVG px）**；
- 200 dpi 像素扫描（印 PDF 216 dpi 渲染）：最右墨点 x=1883.1，超框右 **21.1 px**。
- 存证裁图：`p7-hetwoord-title.png`——“SEMAINE”末几字落在白色页底上，奶油底色已断。
- 页右边界未超（页宽 1950，余量约 67 px），只超奶油盒。
- 归属：本版（法语 gloss `LE MOT DE LA SEMAINE` 加长所致；同类前例：it-de/it-fr/pt-fr/es-pt/pt-ru/it-ru 框标题溢出）。
- 修复建议：缩短法语段，如 `HET WOORD　LE MOT`，或降字号；改后用正典 creambox + PIL 墨右重测（目标余量 ≥ 5 px）。
- 附注：正典 occlusion 审计报 0 flags，未检出此项——BOXTITLE 类对此标题漏检（见 GATE-LOG §7，需回写工具）。

### D2 — P6 框标题贴边/微超奶油盒（极轻、边界）
- 位置：P6 右栏 `VOOR OF TEGEN?　POUR OU CONTRE?`（框右界 x=1862.0）。
- 实测：PIL 真墨迹墨右 1862.8，超 **0.8 px**；216 dpi 像素扫描墨右 1862.7，超 **0.7 px**；印 PDF 词位末字 `?` x1=1397.9 pt，超框右 1.4 pt（= 1.9 SVG px，advance 口径）。
- 三法一致、仅约 1 px，肉眼不可见，但墨迹确实越过盒界。
- 归属：本版（同 D1 类）。修复建议：与 D1 同批处理，略缩法语段（如 `POUR OU CONTRE` 去尾空格/缩一词），重测至墨右 ≤ 框右。

### D3 — 网 PDF 丢失斜体（中偏轻）
- 位置：P1 `HET WOORD VAN DE WEEK` 词条 `«de groepswinst»`（本版唯一斜体 span，SVG `p1-voorpagina.svg` 内 `font-style="italic"`）。
- 实测：
- 印 PDF：该 span 字体 `Newsreader16pt-Italic` 16.12 pt；
- 网 PDF：同 span 字体 `LucernaNewsreader-Regular`（直体），且整份网 PDF **不含任何斜体字体**（仅 `LucernaNewsreader-Regular/Bold` 等），斜体丢失；
- 文字层本身完好：印/网逐词多重集 8 页全等（P1 826/826 … P8 2437/2437），无丢空格、无闭引号脱离——ru-en D3 三联症只复现第三腿（斜体丢失）。
- 归因：随版的网 PDF 建于当前 `tools/webpdf.py` 的 D3 斜体修复（2026-11-11）之前。现版工具已含修复（`fc_match` `:slant=italic` → Newsreader-Italic.ttf）。
- 修复验证（已在 scratch 实跑，非改动原文件）：用当前 `tools/webpdf.py` 重建网 PDF 得 `rebuilt-web.pdf`（1,614,231 字节），含 `LucernaNewsreader-Italic`，该 span 恢复斜体，8 页词数与印 PDF 全等。修复 = 用当前工具重建网 PDF 并重验 SHA。
- 附注：KIT 称“print/web text posdiff 0 msdiff 0”是词级比较，测不到样式丢失，不能作为斜体门的证据。

### D4 — 法语层撇号混用：直撇 U+0027 与弯撇 U+2019 并存（轻，装饰性）
- 实测：全版 SVG 扫描——法语层 U+0027 约 40+ 处，U+2019 仅 8 处：
- P7 ZINNEN 译文 4 处：`parce qu'il`、`l'Allemagne`、`c'est`、`qu'ils`；
- P8 4 处：眉题 `l'exercice d'écriture`（2 处）、#125 `L'Allemagne`、#126 `l'Eredivisie`。
- 同词两种写法：P1 `l'Allemagne`（U+0027）vs P7/P8 `l'Allemagne`（U+2019）；P5 `c'est là que`（U+0027）vs P7 `c'est`（U+2019）。
- 渲染后果：U+2019 在 Newsreader 下带可见空隙，P7 卡片上呈 `qu' il`、`l' Allemagne` 状（与 KIT 所述 quirk 一致）；其余法语撇号（U+0027）无此空隙。
- 归属：本版法语层。修复建议：8 处 U+2019 一律改 U+0027（与法语层多数一致，且避开空隙 quirk）；改后重建 SVG/PDF。
- 附注：KIT 称此 quirk“与核心相同”不准确——实测核心 8 页 SVG 含 U+2019 共 0 处（见 GATE-LOG §7）。

## 未决事项

- O1：D1/D2 修复时由构建者定缩短方案（本复校只给方向：缩法语段或降字号，目标墨右余量 ≥ 5 px）；修复后须重跑 creambox + PIL 墨右 + 像素扫描三法。
- O2：D3 修复（重建网 PDF）后须重录网 PDF SHA/字节数并更新 KIT；定稿前以新 SHA 为准。
- O3：occlusion 审计 BOXTITLE 类漏检 D1——建议工具侧跟进（为何该标题未被标记），不阻塞本版（已有三法实测证据）。
- O4：#63/#126 的“PSV 榜首 26 分”事实只见于本版 P8 #126 题干本身，未见于 P4 正文；答案键与冻结核心一致（p8 compare 无差异），属核心层构造，本版不作缺陷；如需外核，由核心复校定。

## 核实摘要（已核实无问题）

- 三 SHA 与任务一致（见 GATE-LOG §0）；creambox.py md5 `ee7a55d8b2057cf4ad42a97bb1197383` 一致。
- 机械门：occlusion 0 flags（自检通过）；creambox 全版扫描已逐项裁决（最紧 P6 图表末行真墨余量 +3.7 px）；p8 compare CLEAN（150/150 noted，keydiff 仅 137/138，均为合法法语重定向，答案皆正确）；freeze baseline 8/8；freeze diff 仅 U+3000 分隔符，无新增中文；印/网词层 8 页全等；P8 答案区最小字号实测 10.12 pt（与 KIT 一致）。
- 必查项：(a) P1 框标题全过（最紧 numbers 标题余量 +5.0 px；页边全清）；(b) P3/P5 右栏末行降部全清（最紧 +3.7 px）；(c) P7 toolbox 最小 desc-clear +7.1 px；(d) E 节标签全法语 `Traduction`，无「翻譯」残留，text.md 唯一中文是标准 `答案：` 标记（142×，与核心同数）；(e) 网 PDF 斜体三联症只复现第三腿 → D3；(f) ABSTRACT.txt 含 `Lucerna VOL.4`。
- 150 题：逐题手验 150/150（答案与正文事实、P8 印键、冻结核心三方一致；分级 A2 46 / B1 73 / B2 31；页分布 10/18/18/18/18/18/12/38；范文 81 词与核心同数同口径）。
- P1 HET WOORD 法语两行夹行规则 y=1853：真墨上行余量 +2.2 px、下行余量 +3.3 px（像素扫描），紧但不触线。
- 法语引号 « » 全版成对（P1 2/2、P2 2/2、P7 30/30、P8 2/2）；P7 8 句 ZINNEN 引文经核与正文逐字一致，法语译文准确。
- 8 页卡片已逐页目视：除 D1/D2/D4 外无溢出、遮挡、截断、错字；页脚 `Page N sur 8`、刊头 VOL.4、双语栏标全齐。
