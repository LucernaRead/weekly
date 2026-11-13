# 独立校对笔记 — 2026-W47 荷兰文核心版 (core-nl, 2026-w47-nl-zh-cn)

校对员：叶子（独立校对，只读不改）。校对时间：2026-11-10 21:37–21:46 EST。
对象：`~/workspace/weekly-git/production/2026-w47/core-nl/`，De-Lucerna-VOL4.pdf / -web.pdf（各 8 页）。

## 结论：(b) 缺陷清单 — 2 项轻微缺陷 + 2 项琐碎备注，不算定稿

两项轻微缺陷均为可核实的交叉引用错误（目录 / 日程注），不在正文事实与答案之内；
全文、150 道题答案、事实、机械门、§1.1 其余项全部通过（见下）。

## 缺陷清单

### D1（轻微）— P1 日程注页码范围错误
- **位置**：P1 右栏 DEZE WEEK / 本周日程底部，"Alle data en tijden staan ook in de artikelen op pagina 2–4。/ 本周日程见第2–4版文章"。
- **问题**：日程共 5 项，其中第 5 项 "ZO 22 Robinson, 20:00 uur" 的内容只在 P5（"Elke zondag om 20:00 uur is Expeditie Robinson te zien op RTL 4"），不在第 2–4 版。注语称"全部数据与时间亦见第 2–4 版文章"，对该项不成立。
- **证据**：P1 渲染图；P5 正文；print.txt。

### D2（轻微）— P1 目录第 7 行条目名与该版实际标题不符
- **位置**：P1 IN DEZE EDITIE / 本期目录，"Pag. 7 Woorden van de week　A2→B2"。
- **问题**：P7 实际标题为 "Drie niveaus, drie gereedschappen"（栏头 TAAL　语言）。目录其余 6 行均为该版真实标题的删节（P2 "De schoen en pakjesavond"、P3 "Sinterklaas is er!"、P4 "Oranje: de beslissing"、P5 "Robinson en surprises"、P6 "Oud feest, nieuwe wensen"、P8 "Oefeningen en antwoorden"），唯 P7 一行用的不是标题、而是另起的栏目别名。
- **证据**：P1、P7 渲染图；print.txt。

### 琐碎备注（不计为缺陷，仅供 builder 酌处）
- **T1**：P1 顶栏印 "VOL. 4"（SVG 文本节点含空格，letter-spacing 1.7），而刊头副题与各页页脚均为 "VOL.4"。全刊期号一致（VOL.4），仅顶栏一处空格写法不同。
- **T2**：P1 "DE WEEK IN CIJFERS" 第二行 "20:45 — uur: de aftrap"——按该框"数字—名词：说明"的机械格式写成（16—november、8—punten、5—december 同式），但 "20:45 — uur" 在荷兰语里别扭（自然写法是 "20:45 — de aftrap"）；中文译注已澄清含义。
- **T3（仅 KIT，不在印品上）**：KIT §4 称希腊 "8 (5:4)"——希腊 4 场失球应为 3（塞尔维亚 1–2 希腊失 1、德国 0–1 希腊失 0、希腊 0–0 德国失 0、荷兰 2–2 希腊失 2）；Sportradar、myfootballfacts、Global Sports Archive、TNT Sports 与维基模板均为 5:3，仅 wettbasis 一家作 5:4。印品本身从未印出希腊失球数（只印 "7 tegen 5" 进球数对比），故不影响本期；建议改 KIT 数字。
- **T4（计数口径说明）**：范文（P8 H 区）按 whitespace 分词为 81 词（与 KIT/答案注一致），按字母数字词计为 80 词；两种口径均在 80–100 区间内，不构成问题。

## 已通过的检查（逐项）

1. **全量 proofread**：print PDF 文字层全文（101,737 字节 layout 提取）逐版精读。荷兰语拼写/变位/性数/标点未见错误；中文讲解层 18 个注释词经 lemma 核查全部真实出现在正文里（`gloss-lemma.log`，18/18 OK）；6 条 gloss 行完整；目录其余 6 行、IN HET KORT 三条（ORANJE · P.4、SINTERKLAAS · P.3、EREDIVISIE · P.4）、P2 "meer over de intocht lees je op pagina 3"、P2 EN JIJ "VOL.5 (pagina 7, «Brieven van lezers»)" 交叉引用均正确；页码、级别徽章（P1 A2、P2 A2、P3 A2→B1、P4 B1、P5 B1、P6 B2、P7 A2/B1/B2、P8 分级）均正确。
2. **150 道题逐题复核**：逐题对照题面/原文/图表验算，见本笔记附表（摘要于下）。编号连续 1–150 无缺重（`.text.md` 核查 150/150；`p8.py extract --total 150` 150/150；registry TOTAL 150，分布 10/18/18/18/18/18/12/38，A2 46 / B1 73 / B2 31）。关键验算：P3 43=1天、44=4小时、45=19天、46=17年；P6 85=65（35+30）、87=100（35+30+20+15）；P8 126=B（PSV 26分）；P4 57 speelde / 58 won / 59 verloor / 60 speelden；P3 39 is aangekomen / 40 heeft ontvangen / 41 is gevaren / 42 hebben gelezen（助动词全部正确）；P5 76 gaat winnen / 77 gaan kijken / 78 gaat maken / 79 gaan schrijven；P7 104 scoorde / 105 won / 106 verloor / 107 speelde / 111 wil / 112 maakte；P8 133–136 造句、137–140 翻译、141–144 配对（b/c/d/a）、145–149 对话补全全部正确。
3. **8 版逐版看图**：print PDF 每页 72dpi 渲染（`print-p1.png` … `print-p8.png`）逐版目视：无溢出、无重叠、无压页脚；7 张照片 + P6 程序图表均在位，图注与出处完整（P1 Westertoren / Wim van Rossem–Anefo CC0；P2 sint-oud / Anefo CC0；P3 gracht / W. Punt–Anefo CC0；P4 elftal 1912 / Spaarnestad 公版；P5 strand / Elise Iovenko CC0；P7 boeken / Cristina Gottardi CC0；P8 pen / Aaron Burden CC0；与 `assets/CREDITS.md` 及 KIT §5 一致）。P8 答案区字号独立实测：PyMuPDF 取 P8 全部 span，最小 10.12pt（560 个 span），≥ 9.75pt 下限，与 KIT 所述 10.12pt 一致（10.5pt 的 8 个 span 为 "— PAGINA N —" 眉题）。
4. **事实核查（逐项，含 W46 承诺兑现）**：
   - 星期/日期全部以 `TZ=Europe/Amsterdam date -d` 核验：16 Nov 周一、22 Nov 周日、5 Dec 周六、14 Nov 周六、15 Nov 周日、11 Nov 周三、24 Nov 周二、29 Nov 周日、13 Nov 周五、21 Nov 周六，均正确；天数 16Nov→5Dec=19、22Nov→5Dec=13、14→15Nov=1、2009→2026=17，均正确。
   - 荷兰–德国周一 16 Nov 20:45 柏林奥林匹克体育场、NPO 3：全文作"今晚"预告，无任何比分、无"赛果"式表述；周五两场（13 Nov 荷兰–希腊阿姆斯特丹、塞尔维亚–德国贝尔格莱德）只写赛程、无比分；14/15 日抵达只写官方日程事实。搜索核验：德国–荷兰 16 Nov 20:45 柏林（Sportradar/UEFA赛程）与周五赛程属实；KIT §4 提到的 joyn.de 1–1 直播帖与中文网站 1–1 旧闻未在印品中出现。
   - Grave 抵达（Sat 14 Nov、Maaskade 约 12:00、节目 12:00–16:00、NPO 3 直播、市长 Marieke Moorman、要塞城市、Ozosnel）：多源核实属实（vandaagingrave.nl、kidsproof.nl、mamaliefde.nl、ozosnel.nl）。
   - 阿姆斯特丹（Sun 15 Nov、De Omval 10:15 → Scheepvaartmuseum ~11:30、Stopera 13:00 经 Rembrandtplein/Utrechtsestraat → Leidseplein、88e editie）：多源核实属实（winterfestivalamsterdam.com、desinterklaassite.nl、iamsterdam.com）。**递钥匙人选两源冲突已核实**：winterfestivalamsterdam（2026-11-09 更新）称副市长 Esmah Lahlah + 儿童市长 Ava，iamsterdam 称市长 Halsema + 儿童市长；正文只写 "Daar kreeg hij de sleutel van de stad"，确实未点名、无错误归属。
   - Pakjesavond Sat 5 Dec 预告属实；Sint-Maarten Wed 11 Nov 属实；Sinterklaasjournaal 自 11 月 9 日起每日 18:00、NPO Zapp、Merel Westrik 属实。
   - Nations League A2 积分榜（NL 8 / GR 8 / DE 5 / RS 0）与进球数（NL 7:5、DE 3:2、RS 3:8）经 Sportradar / myfootballfacts / TNT / 维基模板核实属实；荷兰 4 场（1–1 德主场、2–1 塞客场、2–2 希客场、2–1 塞主场）与德国 4 场（1–1 荷客场、0–1 希主场、2–0 塞主场、0–0 希客场）逐场算分无误；"前两名进 2027 年 3 月四分之一决赛"符合赛制。惟希腊失球数见 T3。
   - Eredivisie 第 12 轮：Heerenveen–Feyenoord 5–3、Cambuur–PSV 2–5、Twente–Ajax 2–2、积分榜 PSV 26 / Feyenoord 25 / Ajax 25、周日 8 Nov 共 31 球（轮次外单日纪录）、Mijnans 46 秒、Arokodare 2 分 22 秒，均经 eredivisie.nl / 1908.nl / fr12.nl 核实属实；第 13 轮所用 4 场（NEC–PSV 周六 16:30、Feyenoord–Excelsior 18:45、Twente–Willem II 周日 12:15、Ajax–ADO 14:30）经 KNVB 官方赛程 PDF 核实属实。
   - Expeditie Robinson（19 人、荷兰 10 + 佛兰芒 9、名人参赛、34 天、马来西亚、Nicolette Kluijver + Edson da Graça、Camille Vanuxem 记者、11 月 1 日周日首播、每周日 20:00 RTL 4）经 nl/en 维基与 RTL 系来源核实属实。
   - Heel Nederland Leest（21 届、《Het diner》Herman Koch 2009、11 月 1 日起图书馆免费领、含非会员、大字版/Makkelijk Lezen/电子书/有声书）经 CPNB 与多家来源核实属实。
   - VOL.5 预告：欧冠第 5 轮周二 24 Nov Real Madrid–PSV、Feyenoord–FC Porto（UEFA 赛程）与荷甲第 14 轮周日 29 Nov Feyenoord–Ajax 14:30（KNVB 赛程）属实。
   - 无编造、无来源事实：未发现。P6 OEFENDATA 图表按 SOP 要求以荷兰语 + 中文双语明确标注为虚构练习数据。
   - 读者园地：无真实来信，按 F-MAIL 规则刊登标注为"voorbeeldbrief van de redactie"的示例信 + 荷/中双语截稿说明 + 顺延 VOL.5 承诺，处理合规。
5. **机械门槛**：
   - `occlusion_audit.py svg/`：selftest OK（6 类阳性对照全触发、阴性对照静默），`svg/: 0 flags`（`occlusion.log`）。
   - freeze：未用 `freeze.py`（其自报 0/8 为已知布局假象）；直接复现——将构建源码 + assets 拷贝至 scratch 干净目录重跑 `run.py`（exit 0，TOTAL 150、分布与级别计数与 KIT 完全一致），8 个 SVG sha256 与交付 SVG **8/8 一致**（`freeze-sha256.log`、`repro.log`）。
   - `p8.py extract --p8 svg/p8-toets.svg --total 150`：`noted set = 150 of 150`，无 PARSE_FAIL（`p8-extract.log`）。说明：跑的是 builder 改动后（未提交）的 tools/p8.py；其 git diff 为 92 行增 / 16 行删（builder 称 85/16，计数口径略差）；改动后工具行为正常、结果与 builder 所述一致；我未改工具、未提交。
6. **P1 主头条**："Vanavond in Berlijn: Oranje tegen Duitsland" 去空白 38 字符 ≤ 56（LIMITS.headline，other 类）✓。**8 条金句逐字核对**：全部逐字出自本期正文（1 P1、2 P4、3 P1、4 P5、5 P2、6 P6、7 P3、8 P6），页码标注全部正确。图片逐张 PD/CC0 核验见 §4(3) 与 `assets/CREDITS.md`，署名完整。
7. **§1.1 独立核实（8 项）**：
   1. 纸色：8 页渲染图四角 + 中心采样均为 (251,249,246)（#fbfaf6 = 251,250,246，绿通道 1/255 渲染舍入），SVG 背景 rect 每页一个 fill="#fbfaf6" ✓。
   2. 无金色：全 SVG fill 审计仅见 §1.1 调色板（#302c28、#37402f、#46581f、#5c6e30、#6f675d、#cac8ba、#d8d2c4、#f0eee5、#f4efe1、#f6e08e、#fbfaf6、#ffffff）+ 仅 P1 刊头蛾标内的品牌色（#34483A、#4D72B4、#D7B257 等，SOP §1.1 刊头蛾标本身规定）✓；无 #b3a06a 之类金色。
   3. 无双线外框：每页 stroke 元素仅刊头下橄榄绿线（y=420）与蛾标描边；无 stroked rect、无页框 ✓。
   4. 无近黑底：最深背景为书衣绿 #37402f 栏目条；无 #1a1a1a/#111/#000 填充 ✓。
   5. 拉丁正文 Newsreader：全 SVG font-family 统计 Newsreader 1,213 次、Noto Sans CJK SC 619、Noto Serif CJK SC 304、UnifrakturMaguntia 1（刊头）；P1 单页 Newsreader 116 次 ✓。
   6. 刊头/页脚/分隔用全角空格：页脚 "De Lucerna　荷兰语周报 VOL.4　LUCERNA DUTCH WEEKLY"、页码行 "第N版／共8版"（无空格）、刊别 "荷兰语周报　VOL.4　ORANJE　SINTERKLAAS　PAKJESAVOND"、栏头 "HET NIEUWS　头条 / LEVEN　生活 / CULTUUR　文化 / SPORT　体育 / JONGEREN　青年 / VERDIEPING　深读 / TAAL　语言 / TOETS EN ANTWOORDEN　练习与答案" 全部全角空格 ✓；残留 "·" 仅在内容内（gloss 分隔、选择题选项分隔、IN HET KORT 标签），与通过两次独立校对的 FR 核心做法一致 ✓。
   7. 版心：顶栏 y=72px=54pt；MX=88px=66pt 两侧；页脚线 y=2596px、页脚基线 y=2624px（与 FR 核心 bslib4.py 几何一致）✓。
   8. 等级徽章颜色精确匹配：`bslib4.py` LV_COLOR A2 #5c6e30 / B1 #46581f / B2 #37402f，白字，rx=2.7px≈2pt；SVG 内三色徽章填充均有出现（#5c6e30 43 次、#46581f 347 次、#37402f 37 次）✓。
8. **文字层**：web 44,141 字节 vs print 44,140 字节（差 1 字节为尾部换行）；PyMuPDF 位置排序提取：两版各 6,852 token，multiset 差 0、排序后差 0，每页（764/717/673/659/700/659/738/1,685）逐页差 0（`webprint-verify.log`）。实质一致 ✓。
9. **ABSTRACT.txt**：单行、324 字节、无 ASCII 双引号、简体中文读者母语，含刊名、目标语、A2–B2、150 道练习与本期真实主题（柏林决战德国、赫拉弗与阿姆斯特丹第 88 届入城式、12 月 5 日收礼夜、荷甲第 13 轮）✓。
10. **.text.md 导出**：44,025 字节，题号 1–150 连续无缺重，金句 8 条，无答案块、无家具（无页脚/刊头条）；导出头 `# De Lucerna · 荷兰语周报 VOL.4 · 2026-W47` ✓。

## 未改动声明
全程只读：未修改 core-nl 内任何文件与 tools/p8.py；未跑 insert.py、lint --write、git push/add/reset/stash；未提交任何东西；未碰 W43/W45/W46。校对产物仅在 `hidden_files/w47/scratch-proof-nl/`（print.txt、web.txt、print-p1..p8.png、occlusion.log、p8-extract.log、p8-fontsize.log、freeze-sha256.log、repro.log、repro/、webprint-verify.log、textmd-verify.log、gloss-lemma.log、本笔记）。

## 150 道题答案复核摘要
逐题对照结果：150/150 正确。分版：P1 1–10、P2 11–28、P3 29–46、P4 47–64、P5 65–82、P6 83–100、P7 101–112、P8 113–150，答案键与题面/原文/图表全部相符（验算细节见正文逐题记录；完整答案文本在 print.txt 的 ANTWOORDEN 区）。
