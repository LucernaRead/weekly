# 独立校对笔记 — 第二轮全文复校 — 2026-W47 荷兰文核心版 (core-nl, 2026-w47-nl-zh-cn)

校对员：叶子（独立校对，只读不改，与 builder 和第一轮校对员不同人）。校对时间：2026-11-10 22:19–23:05 EST。
对象：`~/workspace/weekly-git/production/2026-w47/core-nl/`，De-Lucerna-VOL4.pdf / -web.pdf（各 8 页，返修后重建：print 25,955,551 字节；web 2,067,793 字节）。

## 结论：(a) 零问题 — 定稿

第一轮的 D1/D2 + T1–T3 逐项独立验证全部修好、无修坏别处；全量复校（全文、150 道题答案逐题、8 版看图、事实、机械门、§1.1、文字层）未发现新问题。

## 返修逐项验证（D1/D2/T1–T3）

### D1 ✓ 修好 — P1 日程注页码范围
- 印品 P1 注语现为 "in de artikelen op pagina 2–5." / "本周日程见第2–5版文章"（源码 content12.py:84–85；print.txt 第 36–38 行；逐页提取 page1.txt）。
- 5 项逐项独立核实（逐页 pdftotext + 源码）：
  - MA 16 Oranje–Duitsland → P4 正文第 1 段（content34.py:110；page4.txt "Op maandag 16 november speelt Oranje in Berlijn tegen Duitsland"）。
  - ZA 21 NEC–PSV → P4（content34.py:113 "speelt PSV om 16:30 uur uit bij NEC"；HET PROGRAMMA 框亦有）。
  - ZA 21 Feyenoord–Excelsior → P4（content34.py:113 "speelt Feyenoord om 18:45 uur thuis tegen Excelsior"）。
  - ZO 22 Ajax–ADO → P4（content34.py:113，断行跨两行："Zondag speelt Ajax om 14:30 uur thuis tegen ADO Den Haag"；page4.txt 第 9–11 行）。
  - ZO 22 Robinson 20:00 → P5（content56.py:17，断行："Elke zondag om 20:00 uur is Expeditie Robinson te zien op RTL 4"；page5.txt 第 12–14 行）。
- 范围 "2–5" 正确：5 项分布在 P4–P5，全部落在 2–5 内；P2/P3 不含任何日程项（grep 0 命中）。

### D2 ✓ 修好 — P1 目录第 7 行
- 印品 P1 目录现为 "Pag. 7 Drie gereedschappen　A2→B2"（源码 content12.py:97；print.txt 第 58 行；P1 渲染图目视：文字与右侧级别标签间留白清晰、无重叠）。
- 是 P7 真实标题 "Drie niveaus, drie gereedschappen"（P7 栏头带："聚焦语言　Drie niveaus, drie gereedschappen　三个级别，三件工具"）的删词缩短，与另 6 行做法一致（P2/P3/P4/P5/P6/P8 均为该版真实标题删节）。
- 几何：`occlusion_audit.py` 0 flags（含 TEXTX 类；自检 6 类阳性对照全触发、阴性对照静默），P1 渲染图确认无重叠。第一版过长缩短被工具拦下的插曲已无残留（print 全文无 "Woorden van de week"）。

### T1 ✓ 修好 — 顶栏 "VOL.4"
- SVG 全部 8 页 `<text>` 节点内 "VOL. 4" 出现 0 次；"VOL.4" 出现 P1 3 次（顶栏、刊头副题、页脚）、其余各页 1 次（页脚）。渲染后 print/web 文字层 grep "VOL. 4" 均为 0。
- 唯一命中是 KIT §12 对本次修复的历史描述句本身，不是印品残留。

### T2 ✓ 修好 — 数字框 "20:45 — de aftrap"
- 源码 content12.py:45 与印品均为 "20:45 — de aftrap（20:45：柏林奥林匹克体育场开球）"；print 全文无 "uur: de aftrap"。
- 荷兰语自然（"20:45 — de aftrap" = 开球时间）；中文译注不变，已含"柏林奥林匹克体育场开球"，与正文第 1 段（Olympiastadion）一致。数字框仍为 2 行，P1 几何未动（occlusion 0 flags）。

### T3 ✓ 修好 — KIT §4 希腊失球数
- KIT §4 现为 "Greece 8 (5:3)"；独立复核：myfootballfacts / TNT Sports / Sports Mole 三家积分表均为希腊 5:3，"5:3" 正确，"5:4" 是错的（KIT §12 的失球逐场加总 1+0+0+2=3 亦对）。
- 印品未动：print 全文无 "5:3"/"5:4"；只印 "7 tegen 5"（荷兰进球数对比）×3 处，与 KIT 所述一致。

## 全量复校（第二轮独立重做，非沿用第一轮结论）

1. **全量 proofread**：print PDF 文字层全文（-layout 101,737 字节）+ `.text.md` 逐版精读。荷兰语拼写/变位/性数/标点未见错误；6 条 gloss 行共 29 个注释词逐词核查，全部真实出现在正文里（`content-verify.log`）；交叉引用正确（IN HET KORT ORANJE·P.4 / SINTERKLAAS·P.3 / EREDIVISIE·P.4；P2 "Meer over de intocht lees je op pagina 3"；P2 EN JIJ "VOL.5 (pagina 7, «Brieven van lezers»)"；P1 目录其余 6 行与各版标题对应）；级别徽章（P1 A2、P2 A2、P3 A2→B1、P4 B1、P5 B1、P6 B2、P7 A2/B1/B2、P8 分级）正确。
2. **150 道题答案逐题复核（独立再验算，未轻信第一轮）**：`p8.py extract --json` 印出键与 `.text.md` 登记键逐题比对 **150/150 一致**（Q150 印出 "✓"、登记为开放题范文，属设计如此，KIT §9 已说明；初版脚本报的 11 处"不符"是我方脚本嵌套括号解析瑕疵——如 "surprise（surprise = 伪装礼物（de））"——第二版脚本已证实印出键与登记键词面完全相同）。另逐题对照题面/原文/图表独立验算：P3 43=1天、44=4小时、45=19天、46=17年；P6 85=65（35+30）、87=100（35+30+20+15）；P8 126=B（PSV 26分）；**Q131 重点复核**：P8 阅读文 "Zondag zet hij zijn schoen met een wortel en een verlanglijstje" → 选项 B，印出答案 "131. B" 正确（pt 的 Q131 教训已吸取：不是抄第一轮结论，是对着原文重算的）。编号 1–150 连续无缺重；分布 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31。
3. **8 版逐版看图**：print PDF 每页 72dpi 渲染（`print-p1.png` … `print-p8.png`）逐版目视：无溢出、无重叠、无压页脚；7 张照片 + P6 程序图表均在位，图注与出处完整（P1 Westertoren / Wim van Rossem–Anefo CC0；P2 sint-oud / Anefo CC0；P3 gracht / W. Punt–Anefo CC0；P4 elftal 1912 / Spaarnestad 公版；P5 strand / Elise Iovenko CC0；P7 boeken / Cristina Gottardi CC0；P8 pen / Aaron Burden CC0；与 `assets/CREDITS.md` 及 KIT §5 一致）。P8 答案区字号独立实测：PyMuPDF 取 P8 全部 span，最小 **10.12pt**（560 个 span），≥ 9.75pt 下限，与 KIT 所述一致（10.5pt 的 8 个 span 为 "— PAGINA N —" 眉题；10.35pt 65 个为练习区小字）。
4. **事实核查（ fresh 搜索复核，逐项）**：
   - 星期/日期全部以 `TZ=Europe/Amsterdam date -d` 核验：11 Nov 周三、13 Nov 周五、14 Nov 周六、15 Nov 周日、16 Nov 周一、21 Nov 周六、22 Nov 周日、24 Nov 周二、29 Nov 周日、5 Dec 周六，均正确；天数 16Nov→5Dec=19、22Nov→5Dec=13、14→15Nov=1、2009→2026=17，均正确；图表 35+30+20+15=100、35+30=65。
   - 德国–荷兰 Mon 16 Nov 20:45 柏林奥林匹克体育场：DFB 官网、Sportradar、多家票务/赛程源一致确认；积分榜 NL 8 (7:5) / GR 8 (5:3) / DE 5 (3:2) / RS 0 (3:8) 经 myfootballfacts、TNT、Sports Mole 三表确认；荷兰凭进球数 7 对 5 居首；前两名进 2027 年 3 月四分之一决赛符合赛制。周五 13 Nov 荷兰–希腊（Johan Cruijff ArenA）与塞尔维亚–德国（贝尔格莱德）赛程属实。
   - Sinterklaas：Grave Sat 14 Nov、Maaskade 约 12:00、节目 12:00–16:00、NPO 3 直播、市长 Marieke Moorman、要塞城市、Ozosnel；阿姆斯特丹 Sun 15 Nov、De Omval 10:15（uitamsterdam.com；holland-explorer 一处写 10:30，但多源与第一轮核实的官方口径为 10:15，印品取 10:15 有据）、Scheepvaartmuseum ~11:30、Stopera 13:00、88e editie——多源确认属实。**递钥匙人选**：正文只写 "Daar kreeg hij de sleutel van de stad"，未点名，无错误归属 ✓。
   - W46 承诺兑现：周一比赛全文只写"今晚"预告，无比分、无"赛果"式表述；周五两场只写赛程（"Vrijdag speelden Oranje en Duitsland hun vijfde wedstrijd…" 无比分）；14/15 日抵达只写官方日程事实。全文 grep "uitslag" 仅一处 P7 "Oefen met de uitslagen van deze week"（指已赛完的第 12 轮练习，非周五/周一比分）。
   - Eredivisie 第 12 轮：Heerenveen–Feyenoord 5–3、Cambuur–PSV 2–5、Twente–Ajax 2–2、PSV 26 / Feyenoord 25 / Ajax 25 经 1908.nl、fr12.nl、Sportradar 确认；周日 8 Nov 共 31 球、Mijnans 46 秒、Arokodare 2 分 22 秒均有源确认。注：个别源对 Twente 积分有 24/25 分歧（1908/fr12 为 24，fr-fans 一表为 25），印品未印 Twente 积分，不受影响；soccernews 一表误写 Ajax 22 分，与多数源（25）不符，印品取 25 正确。
   - 其余：Expeditie Robinson（19 人、34 天、马来西亚、Nicolette Kluijver + Edson da Graça、Camille Vanuxem、11 月 1 日首播、每周日 20:00 RTL 4）、Heel Nederland Leest（《Het diner》Herman Koch 2009、图书馆免费领）、VOL.5 预告（欧冠 24 Nov Real Madrid–PSV、Feyenoord–FC Porto；29 Nov Feyenoord–Ajax）——第一轮已逐项核实，本轮抽查关键项无矛盾，未发现编造、无来源事实。P6 OEFENDATA 图表按 SOP 要求荷/中双语明确标注为虚构练习数据。读者园地：无真实来信，按 F-MAIL 规则刊登标注 "voorbeeldbrief van de redactie" 的示例信 + 荷/中双语截稿说明 + 顺延 VOL.5 承诺，合规。
5. **机械门槛（独立重跑）**：
   - `occlusion_audit.py svg/`：selftest OK（6 类阳性对照全触发、阴性对照静默），`svg/: 0 flags`（`occlusion.log`）。
   - freeze：未采信 `freeze.py` 自报（已知布局假象）；干净目录重跑 `run.py`（exit 0，TOTAL 150、分布与级别计数与 KIT 一致），8 个 SVG sha256 与交付 SVG **8/8 一致**（`freeze-sha256.log`、`repro.log`）。
   - `p8.py extract --p8 svg/p8-toets.svg --total 150`：`noted set = 150 of 150`（`p8-extract.log`；`--json` 键见 `p8-extract.json`）。说明：跑的是 builder 改动后（未提交）的 tools/p8.py；git diff 为 92 行增 / 16 行删；改动后工具行为正常、结果与 builder 所述一致；我未改工具、未提交。
   - P8 字号见第 3 项（10.12pt）。
   - 文字层：raw pdftotext print 44,134 字节、web 44,135 字节（差 1 字节为尾部换行，与 KIT §12 一致）；PyMuPDF 位置排序提取：两版各 6,591 token，8 页逐页 positional-diff 0、multiset-diff 0（`content-verify.log`）。注：KIT §12 称 6,511 token，与我的 6,591 之差是 token 化口径不同（我用 words API 位置排序），两种口径下 diff 均为 0，内容实质一致。
6. **P1 主头条**："Vanavond in Berlijn: Oranje tegen Duitsland" 去空白 38 字符 ≤ 56 ✓。**8 条金句逐字核对**：全部逐字出自本期正文，页码标注全部正确（P1×2、P2、P3、P4、P5、P6×2，见 `content-verify.log`）。图片逐张 PD/CC0 核验见第 3 项。
7. **§1.1 独立核实**：
   1. 纸色：SVG 背景 rect 每页一个 fill="#fbfaf6"（8 次）✓。
   2. 无金色：全 SVG fill 审计仅见 §1.1 调色板（#302c28、#37402f、#46581f、#5c6e30、#6f675d、#cac8ba、#d8d2c4、#f0eee5、#f4efe1、#f6e08e、#fbfaf6、#ffffff）+ 仅 P1 刊头蛾标内的品牌色（#34483A、#4D72B4、#D7B257 等，SOP §1.1 刊头蛾标本身规定）；无 #b3a06a ✓。
   3. 无双线外框：stroked rect 0 个；无页框 ✓。
   4. 无近黑底：最深背景为书衣绿 #37402f 栏目条；无 #1a1a1a/#111/#000 填充 ✓。
   5. 拉丁正文 Newsreader：全 SVG font-family 统计 Newsreader 1,213 次、Noto Sans CJK SC 619、Noto Serif CJK SC 304、UnifrakturMaguntia 1（刊头）✓。
   6. 刊头/页脚/分隔用全角空格：页脚 "De Lucerna　荷兰语周报 VOL.4　LUCERNA DUTCH WEEKLY"、页码行 "第N版／共8版"、刊别 "荷兰语周报　VOL.4　ORANJE　SINTERKLAAS　PAKJESAVOND" 全部全角空格 ✓；残留 "·" 仅在内容内（gloss 分隔、选择题选项分隔、IN HET KORT 标签），与通过两次独立校对的 FR 核心做法一致 ✓。
   7. 版心：与第一轮核实一致（顶栏 y=72px=54pt；MX=88px=66pt；页脚线 y=2596px、基线 y=2624px；与 FR 核心几何一致）✓。
   8. 等级徽章颜色精确匹配：LV_COLOR A2 #5c6e30（43 次）/ B1 #46581f（347 次）/ B2 #37402f（37 次），白字，rx=2.7px≈2pt ✓。
8. **ABSTRACT.txt**：324 字节、单行（末尾一个换行）、无 ASCII 双引号、简体中文读者母语，含刊名、目标语、A2–B2、150 道练习与本期真实主题（柏林决战德国、赫拉弗与阿姆斯特丹第 88 届入城式、12 月 5 日收礼夜、荷甲第 13 轮）✓。
9. **.text.md 导出**：44,026 字节，题号 1–150 连续无缺重，金句 8 条，无答案块、无家具（无页脚/刊头条）；导出头 `# De Lucerna · 荷兰语周报 VOL.4 · 2026-W47` ✓。

## 未改动声明
全程只读：未修改 core-nl 内任何文件与 tools/p8.py；未跑 insert.py、lint --write、git push/add/reset/stash；未提交任何东西；未碰 W43/W45/W46。校对产物仅在 `hidden_files/w47/scratch-proof-nl2/`（print.txt、web.txt、print-raw.txt、web-raw.txt、page1–8.txt、print-p1..p8.png、occlusion.log、p8-extract.log、p8-extract.json、p8-extract2.log、answers-verify.log、answers-verify2.log、freeze-sha256.log、repro-hashes.txt、core-hashes.txt、repro.log、repro/、content-verify.log、style11.log、本笔记）。写文件过程无 EPERM/EDQUOT 失败。
