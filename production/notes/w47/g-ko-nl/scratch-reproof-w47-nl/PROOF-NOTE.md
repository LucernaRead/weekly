# W47 nl 家庭独立重校记录（PROOF-NOTE）

- **校对员**：独立重校（未参与建造）。只校对、不修复、不重建、不 commit、不 push、不跑 lint。
- **范围**：11 版，目标语 nl，读者母语 en / de / fr / es / it / pt / ja / ko / ru / zh-cn / zh-tw。
- **正典目录**：`~/workspace/weekly-git/production/2026-w47/2026-w47-nl-*/` 与 `core-nl/`（= nl-zh-cn 版；盘上无单独的 `2026-w47-nl-zh-cn` 目录）。`fanout-nl/` 为 staging 目录，非正典，未校。staging 与正典比对：仅 nl-es 三件套字节相同，其余 9 版 staging 均已过期。
- **校对日期**：2026-11-12。依据：SOP.md §8 + §1.1 字体表；D5-PLAN.md §1–§4。
- **结论：(b) 有问题** —— 共 21 条记录（2 条 MEDIUM、其余 low / minor / trivial），见下文「问题清单」。无事实错误；机械门全部通过。

## 工具状态

- `tools/` git HEAD（工具运行时）：`71f4e6f9df302d5322211cdd01437a9ac0f4fec7`。工作树 dirty：modified `tools/README.md`、`tools/cover.mjs`、`tools/occlusion_audit.py`、`tools/p8.py`、`tools/run_build.py`；untracked `tools/d5_creambox_audit.py`、`tools/head_check.py`。校对期间 tools/ 无变动，未重跑。
- 无 `run.py` build 日志留存于版目录 → `head_check.py` 无可扫描内容（已记、跳过）。
- `d5_creambox_audit.py` 需 pre-fix baseline 目录，无 baseline → 未跑（已记）。
- 磁盘：开工时 93G 已用 / 150G（62%）；收尾复核时未超门限（`df` 100G 门限未触发）。

## 每版文件（校对的那份文件：尺寸 + SHA 前 12）

| 版 | 印 PDF（SHA-12 / 字节） | 网 PDF（SHA-12 / 字节） | text.md（SHA-12 / 字节） |
|---|---|---|---|
| nl-de | 97420549c81e / 12104230 | 2361bedfd4d5 / 1536341 | c1342c3fe20d / 46226 |
| nl-en | d87a5242afec / 12102271 | db7a9ace064a / 1534348 | 9596c4acbb27 / 45115 |
| nl-es | 2da02d5b3081 / 12107937 | 249fda66604b / 1540062 | 44fc3d5c4287 / 47649 |
| nl-fr | 08f57ec27d86 / 12106421 | 1b429a3ff61e / 1538511 | f1d1154442c4 / 47744 |
| nl-it | 675f2bf33c42 / 12102402 | 81a3ffaf8e8e / 1534500 | f1d9e3f58b82 / 47060 |
| nl-ja | 67aeebb40b58 / 18803852 | 9a4b3dbd5dad / 1968007 | 060bfdea2434 / 47801 |
| nl-ko | fd8daad8ba7e / 13871308 | 694720afc0cc / 1791910 | 75fbaa3004d0 / 47585 |
| nl-pt | dc43c521becb / 12110806 | b9e2c0d5b7f2 / 1542946 | 7e6b0c54dcb2 / 47209 |
| nl-ru | 8fa079cbd094 / 12367658 | 69678fdcdd00 / 1779868 | f23da475ff54 / 57870 |
| nl-zh-tw | 90710eae78ae / 13888370 | 42b892b5c065 / 1976958 | 30af89dfbfe2 / 44320 |
| nl-zh-cn（core-nl） | 0c5d63b942d2 / 13830540 | 2b6f223eaff9 / 1874709 | 0b97a48dc248 / 44093 |

全部印 PDF 均为 8 页、1462.5×2025pt。全部版均有 print PDF + web PDF + text.md + ABSTRACT.txt + WEEKLY-KIT.md。

## 机械门结果（`tools/venv/bin/python`）

- `occlusion_audit.py`（每版 `svg/` 目录）：**11 版全部 0 flags**。日志与 JSON 在 `mech/occl-*.json/log`。
- `p8.py compare --core-dir production/2026-w47/core-nl --edition-dir <各版> --target nl --total 150`：**10 个 fan-out 全部 CLEAN**，每版 150/150，missing=[]、extra=0、uncertain=[]；每版均有 `keydiff=[137, 138]`。core 单独抽取亦 150/150。TOTAL=150 取自 core registry（KIT：按页 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31；范文 81 词）。
  - keydiff 137/138 已人工复核：Q137/Q138 为翻译题，答案本就应用读者母语写（en "The Sinterklaas news is on every day at 18:00." / "The top two go through to the quarter-finals."；de/fr/es/it/pt/ja/ko/ru/zh-tw 各版对应译文均正确；zh-tw "聖誕老人新聞每天 18:00 播出。" / "前兩名晉級八強賽。"）。仅作信息记录，非失败。
- PSV 积分行（"Stand Eredivisie na 12 ronden: PSV 26, Feyenoord 25, Ajax 25 punten."）11 版 `svg/p4-sport.svg` 均有 —— core KIT §12 的修复已由 D5 重 fan-out 继承。
- 网 PDF 文字层：`pdftotext` 字节数印版 == 网版，11 版全部一致（core 44127、de 46657、en 45350、es 46704、fr 46769、it 46372、ja 47834、ko 47521、pt 46598、ru 54983、zh-tw 44254）—— SOP 附则四满足。
- P2 head "DRIE DINGEN VOOR 5 DECEMBER"：11 版 SVG 均为 23pt（已知的 25→23pt 修复；`content12.py:175` 注释确认 Newsreader SemiBold 在 25pt 时 advance 451.8px > 422.5px 栏宽，23pt 时 415.6px）。字体：10 版为 Newsreader，**仅 nl-ru 为 Noto Sans**（见问题 8）。
- D5 弯引号路由已在 `core-nl/svglib.py`（约 113–131 行）核实：fix2 把 U+201C/U+201D/U+2019 走 serif 分支进 Newsreader；D5 sans 分支路由：拉丁→Newsreader、西里尔→Noto Sans；`_D5_READER=="ru"` 时拉丁与西里尔均走 Noto Sans（代码注释中的 deliberate extension (1)）。
- en/ru P1 残留的 "Noto Sans CJK SC" 文本元素仅为 U+3000（表意空格，SOP 规定的 "·" 替代）与 "→" 箭头 —— 无拉丁字母，非 D5 违规。
- text.md 答案标记：每版 142 个本地化标记（de "— Antwort:"、en "— Correct:"、es/pt "— Respuesta:"、fr "— Réponse:"、it "— Risposta:"、ja "— 答え："、ko "— 정답："、ru "— Ответ："、zh-tw/core "— 答案："），非中文版 0 残留"答案"。core 与 fan-out 的 diff 每版恰为 618 行 / 241 行版面讲解行；荷兰语核心文本 11 版完全相同（diff 仅讲解层变化）。
- P8 最小字号（PyMuPDF）：**11 版全部 10.12pt**（高于 9.75pt 底线；最大 34.50pt）。span 数：core 783、de/en/es/fr/it/pt 约 385–389、ja 769、ko 838、ru 803、zh-tw 776。
- 字体抽查：ja/ko/zh-tw/core 的 P3 柱状图副标题 "Sinterklaas is er"、P1 "VANAVOND"、P2 "LEVEN" 栏头均为 Newsreader；ru 为唯一例外。
- 溢出扫描（PyMuPDF，11 版印 PDF、全部 8 页）：**11 版全部 CLEAN，0 问题** —— 无 span 超出页面矩形、无文字落入 y=1985 以下页脚区、无 P8 span < 9.75pt。
- 文字-文字碰撞扫描（PyMuPDF，全部 11 版 × 8 页，y 区间重叠 + x 重叠 > 0.3pt）：唯一真碰撞为 it P2（见问题 16）；其余命中均为误报（刊头 "De Lucerna" 花体字 bbox 与下行重叠；中/日/韩字体 bbox 高导致相邻行 y 区间重叠；数字框荷兰语行与括号注释换行）。pt P1 的碰撞为单一合并字串 "LEEMWEEK"，扫描无法以 span 对检出，以直接测量确认（见问题 14）。
- P3–P7 奶油盒标题逐盒测量（标题右端 vs 盒右缘）：无一溢出；最紧的两处见问题 19、20。

## 文本通读

- core `2026-w47-nl-zh-cn.text.md` 全文通读（432 行，P1–P8）。10 个 fan-out 讲解层全文通读（抽取的 diff 文件 `mech/expl-<lang>.txt`，每版 241 行）。
- 核心事实人工复核：星期（Mon 16 Nov、Sat 14 Nov、Sun 15 Nov、Sat 5 Dec、Wed 11 Nov Sint-Maarten、Sun 1 Nov、Sun 22 Nov、Tue 24 Nov、Sun 29 Nov —— 与 2026 日历全部一致）；16 Nov→5 Dec = 19 天（Q22/Q45）；14→15 Nov = 1 天（Q43）；12:00–16:00 = 4 小时（Q44）；2009→2026 = 17 年（Q46）；荷兰 8 分 = 1–1、2–1、2–2、2–1（进球 7–5）；德国 5 分 = 1–1、0–1、2–0、0–0；图表 35+30+20+15=100、35+30=65（Q83–87）；荷兰语动词形（ontving、is aangekomen、heeft ontvangen、is gevaren、speelde/won/verloor/speelden、maakte、scoorde、kwartfinales）；P7 金句 8 条全部逐字出自本期、页码标注正确（P1、1、2、3、4、5、6、6）；PAS OP 纠错正确；范文实数 81 词（80–100 区间）；P8 编号连续 113–150（38 题）；Q126 答案 B=26 可由 P4 积分行验证；Q139/Q140 翻译 11 版全部正确（ja Q140 除外，见问题 1）。
- ABSTRACT.txt 11 版全部检查：读者母语、单行、无 ASCII 双引号、含刊名 + 目标语名 + A2–B2 + 150 练习 + 真实话题。 minor：core 摘要未写明 "16–22日" 周次（其余版均写明）；ko 摘要用 파크예스아본트（少数派译法，见问题 4）。
- H1 行（text.md）11 版全部核实：core "# De Lucerna · 荷兰语周报 VOL.4 · 2026-W47"；de "Niederländische Wochenzeitung"；en "Dutch Weekly"；es "Semanario neerlandés"；fr "Hebdomadaire néerlandais"；it "Settimanale olandese"；ja "オランダ語週刊"；ko "네덜란드어 주간지"；pt "Semanário neerlandês"；ru "Голландский еженедельник"；zh-tw "荷語週報"。

## 视觉通读覆盖

- core-nl P1–P8：全部看过，干净。ru P1–P8：全部看过（问题版，R1/R2 已视觉确认）。
- de P1–P8：全部看过，干净。en/es/fr：P1、P2、P8 看过，干净（P3–P7 以全文文本通读 + 碰撞扫描 + 盒标题逐盒测量覆盖；荷兰语核心文本与 core 字节相同）。
- it：P1、P2、P8 看过（P2 见问题 16、17）；pt：P1、P2、P8 看过（P1 见问题 14、15；P2 见问题 18）；ja：P1、P2、P8 看过；ko：P1、P2、P8 看过；zh-tw：P1、P2、P8 看过。
- P3–P7 未逐页看图的版（en/es/fr/it/pt/ja/ko/zh-tw）：以 PyMuPDF 文字碰撞扫描（全版全页）+ P3–P7 奶油盒标题逐盒测量 + 讲解层全文通读覆盖；扫描仅发现 it P2 一处真碰撞（已列问题 16），盒标题无溢出（最紧处见问题 19、20）。

## 事实核验（2026-11-12 联网核查，全部属实，无事实错误）

- **Expeditie Robinson 2026**：19 人、34 天、马来西亚、Sun 1 Nov 2026 20:00 RTL 4 首播、主持 Nicolette Kluijver + Edson da Graça、记者 Camille Vanuxem —— en.wikipedia.org/wiki/Expeditie_Robinson_2026 及多家荷兰媒体一致。周日 22 Nov 新一集亦符合周播节奏。
- **Heel Nederland Leest 2026**：书为 Herman Koch《Het diner》（2009 年），11 月全月图书馆免费取、非会员亦可，另有大字版、Makkelijk Lezen 版、电子书、有声书 —— nl.wikipedia.org/wiki/Het_diner_(roman) 及多家地方图书馆公告一致。
- **Sinterklaas intocht**：全国进城 Sat 14 Nov 2026 Grave、Maaskade 约 12:00、市长 Marieke Moorman、节目 12:00–16:00、NPO Zapp/NPO 3 直播、Merel Westrik 主持；阿姆斯特丹 Sun 15 Nov 2026、10:15 De Omval 出发、11:30 抵 Scheepvaartmuseum、13:00 Stopera 骑马上街、经 Rembrandtplein 与 Utrechtsestraat 至 Leidseplein、第 88 届；Sinterklaasjournaal 每日 18:00、自 Mon 9 Nov 起 —— playtix / amsterdaminside / vandaagingrave.nl / NTR 公告一致。
- **Nations League A2（2026-27）**：分组荷兰/希腊/德国/塞尔维亚为真，非教学虚构。积分：荷兰 8、希腊 8、德国 5、塞尔维亚 0；四场比分与进球（荷兰 7–5）与 UEFA.com / DFB 数据中心一致；Fri 13 Nov 荷兰–希腊（主场，Johan Cruijff ArenA）+ 塞尔维亚–德国（贝尔格莱德）；Mon 16 Nov 德国–荷兰 20:45 柏林 Olympiastadion —— uefa.com、datencenter.dfb.de 一致。Q61–Q64 全部可验。
- **Eredivisie 12 轮后**：PSV 26（12 场 8-2-2，40-15）、Feyenoord 25、Ajax 25；第 12 轮 Cambuur 2–5 PSV、Heerenveen 5–3 Feyenoord、Twente 2–2 Ajax；第 13 轮 NEC–PSV Sat 21 Nov 16:30、Feyenoord–Excelsior 18:45、Ajax–ADO Sun 22 Nov 14:30、Twente–Willem II 12:15 —— sportradar / 1908.nl / Ziggo / soccernews 一致。
- **下周预告**：Tue 24 Nov 2026 欧冠 Real Madrid–PSV、Feyenoord–FC Porto；Sun 29 Nov 2026 Feyenoord–Ajax（Eredivisie 第 14 轮）—— UEFA.com、sportradar 一致。

## 问题清单（只记录，不修复）

### 1. nl-ja Q140 译文缺 "surprise" 对应词 —— low-medium
- **位置**：P8，Q140 翻译题源句；`2026-w47-nl-ja.text.md` 对应行；印 PDF P8。
- **证据**：日语源句 "小さな詩つきのプレゼントを作ります。"（做一个带小诗的礼物）无任何 "surprise（伪装礼物）" 对应词；标准答案却要求 "Ik maak een surprise met een kort gedicht."。其余 9 版 + core 均含 surprise 对应词（de "eine Surprise"、en "a surprise"、es "una sorpresa"、fr "une surprise"、it "una surprise"、ko "깜짝 선물"、pt "uma surprise"、ru "сюрприз"、zh-tw/core "偽裝禮物"）。学习者无法从日语源句推出 "surprise"。
- **严重度**：low-medium（练习题源句与答案脱节）。

### 2. nl-ja Pakjesavond 译名不统一 —— low
- **位置**：`2026-w47-nl-ja.text.md` 第 83 行 P2 栏目标题 "PAKJESAVOND IN VIER WOORDEN … パッケスアフォント"；其余 5 处为 パッケスアーフォント（Q5、Q10、Q13、Q20 注释、金句第 371 行）。
- **证据**：パッケスアフォント ×1 vs パッケスアーフォント ×5。同一版内同一专名两种写法。
- **严重度**：low。

### 3. nl-ja Q135 语法注释分隔符不统一 —— trivial
- **位置**：Q135 语法注释用 ASCII " + "（"主語 + 動詞 + 時間 + 場所"），Q133/134/136 用全角 "＋"。
- **严重度**：trivial。

### 4. nl-ko Pakjesavond 译名不统一 —— low
- **位置**：`2026-w47-nl-ko.text.md` 第 371 行金句用 파크예스아본트 ×1；Q5、Q10、Q13、Q20 注释用 팍예스아폰트 ×4；ko `ABSTRACT.txt` 亦用 파크예스아본트。
- **严重度**：low。

### 5. nl-ko Q135 分隔符 + 括号前缺空格 —— trivial
- **位置**：Q135 语法注释用 " + "，其余题用 "·"；ko 版括号注释系统性缺空格，如 "Berlijn(11월 16일"、数字框 "Berlijn(11월 16일：독일–네덜란드)"、"(20:45: 킥오프)"、"(8점：공동 선두)"、"(12월 5일：19일 남음)"。
- **严重度**：trivial（全版系统性版式习惯，非单处错误）。

### 6. nl-it + nl-pt P8 题型标签 "Cloze" 未本地化 —— low
- **位置**：`2026-w47-nl-it.text.md` 第 383–390 行（Q113–120）与第 423–427 行（Q145–149）；`2026-w47-nl-pt.text.md` 相同行号。标签为 "[B1 · Cloze]"。
- **证据**：其余版均本地化（en "cloze choice"、de "Lückentext"、es "Texto con huecos"、fr "Texte à trous"、ja "穴埋め選択"、ru "Выбор в тексте"；ko 全版用 "객관식"，描述性正确）。注：该标签仅见于 text.md（网版正文），印版 P8 的栏目标题 "A VUL DE KRONIEK IN" / "G DIALOOG BIJ DE SCHOEN" 上无此标签。
- **严重度**：low。

### 7. nl-ru P1 数字框注释截断 —— low
- **位置**：P1 "DE WEEK IN CIJFERS" 数字框第一行；`2026-w47-nl-ru.text.md` 第 13 行。
- **证据**："16 — november: Duitsland – Nederland in Berlijn (16 ноября: Германия)" —— 俄语注释只写 "Германия"，丢了 "– Нидерланды" 与柏林。其余 9 版均含两队（如 en "(16 Nov: Germany–Netherlands, Berlin)"、zh-tw "(11月16日：德國–荷蘭在柏林)"）。
- **严重度**：low。

### 8. nl-ru R1：拉丁目标语标题全版误用 Noto Sans —— MEDIUM
- **位置**：全部 8 页，sans 层所有拉丁目标语标题。
- **证据**：SVG 字体统计：ru 版 8 个 SVG 共 338 个纯拉丁 + 64 个混合文字 Noto Sans 元素；其余 10 版对应位置均为 Newsreader。受影响标题包括 P1 "VANAVOND IN BERLIJN!"、"HET NIEUWS"、"DE WEEK IN CIJFERS"、"NU JIJ"、"DEZE WEEK"、"IN DEZE EDITIE"、"HET WOORD VAN DE WEEK"、"BLIKSEMQUIZ"；P2 "DRIE DINGEN VOOR 5 DECEMBER"（23pt）、"ZO ONTHOUD JE HET"、"WIST JE DAT?"、"EN JIJ?"、"PAKJESAVOND IN VIER WOORDEN"；P2–P6 栏头 "LEVEN/CULTUUR/SPORT/JONGEREN/VERDIEPING/TAAL" 与黄色副标题；盒标题（"DE STAND IN GROEP 2"、"HET PROGRAMMA"、"DE GRAFIEK"、"VOOR OF TEGEN EEN LIJSTJE?"、"JONGEREN EN DE SURPRISE"、"ZO KIJK JE ROBINSON"、"VOETBALWOORDEN"、"DE VERLEDEN TIJD"、"BIJZINNEN MET OMDAT"、"PAS OP!"、"HET WOORD"、"BRIEVEN VAN LEZERS"、"ZINNEN VAN DE WEEK"、"VOLGENDE WEEK"）；练习组标题（"OEFENINGEN"、"BEGRIJPEN"、"WOORDEN"、"HET PERFECTUM"、"REKENEN"、"VERLEDEN TIJD"、"WAAR OF NIET WAAR?" 等）；P8 栏目标题（"TOETS EN ANTWOORDEN"、"VUL DE KRONIEK IN"、"ALGEMENE VRAGEN"、"LEES EN ANTWOORD"、"MAAK DE ZINNEN"、"VERTAAL"、"WOORDEN VAN DE WEEK"、"DIALOOG BIJ DE SCHOEN"、"SCHRIJF ZELF"、"ANTWOORDEN"、"— PAGINA n —"）。视觉确认：ru P1 大标题 "Vanavond in Berlijn: Oranje tegen Duitsland" 为无衬线体，其余 10 版同一标题为 Newsreader 衬线体。
- **根因**：D5 机制扩展 (1)：`svglib.py _char_font` 中 `_D5_READER=="ru"` 时 sans 分支把拉丁文也路由到 Noto Sans。D5-PLAN §3 明确要求单独做 ru 读者试点，正因该路径在 pt-fr 试点中从未触发。
- **范围界定**：刊头家具（"ELKE WEEK IN HET NEDERLANDS"、"WEEK VAN 16 TOT EN MET 22 NOVEMBER 2026"、"VOL.4"、A2/B1/B2 徽章、图片 credit、"Van de redactie van De Lucerna"、"Leesniveau: A2"）在 ru 版亦为 Noto Sans —— 按 SOP §1.1 第 5 行（俄语读者家具用 Noto Sans）可视为合规，故违规范围限定为目标语标题；家具列为同机制背景。
- **严重度**：MEDIUM（系统性、全版、违反 SOP §1.1 第 2 行"拉丁书写的目标语标题、正文 Newsreader"）。

### 9. nl-ru R2：P8 答案层误用 Noto Serif CJK SC —— low
- **位置**：P8 答案区全部俄语注释与 Q139/Q140 俄语题干。
- **证据**：ru P8 共 561 个 Noto Serif CJK SC 元素，如 "Прибытие в Амстердам е по счёту"、"Я делаю сюрприз с небольшим стихотворением"、Q137 答案 "Германия Нидерланды начало в понедельник в Берлине"。按 SOP 应为 Noto Sans（讲解层，第 5 行）或 Noto Serif Cyrillic（第 3 行）。
- **根因**：P8 答案走 serif 分支；ru `svglib.py` 第 21 行 `_SERIF = NotoSerifCJK-Regular.ttc`（继承自中文 core 模板）；D5 修复只动了 sans 分支。后果：同一版内讲解层 P1–P7 为 Noto Sans、P8 为 Noto Serif CJK SC。视觉上与 Noto Serif Cyrillic 近乎相同，但属字体表偏差；是否补西里尔衬线路由须协调员定。
- **严重度**：low。

### 10. nl-zh-tw Pakjesavond 译名分裂 —— low
- **位置**：禮物之夜 ×4（Q5、Q10、Q13、Q20 注释）vs 收禮夜（数字框、Q24、Q116、金句）。
- **证据**：core zh-cn 全版一致用 收礼夜。zh-tw 版内同一概念两种译名。
- **严重度**：low。

### 11. nl-zh-tw 语法术语分裂 —— low
- **位置**：Q97/98/133/134 用台湾术语 主詞/受詞；Q135/136 用大陆术语 主語/賓語（如 Q133 "（主詞 + 動詞 + 時間）" vs Q135 "（主語 + 動詞 + 時間 + 地點）"）。
- **严重度**：low。

### 12. nl-en BRIEVEN 注释缺 "best P8 texts" —— minor
- **位置**：P7 "BRIEVEN VAN LEZERS" 框内英文注释。
- **证据**：en 版 "No letters yet — an example; VOL.5 next." / "Editor's example, not a real letter. Send yours — we print them in VOL.5!" 未提 "best P8 texts"（beste pagina-8-teksten）；core 注释与 de/es/fr/it/ja/ko/pt/ru/zh-tw 均含此句。
- **严重度**：minor（完整性缺口，非事实错误）。

### 13. core-nl text.md 第 5 行多余 "VOL.4" —— minor
- **位置**：`core-nl/2026-w47-nl-zh-cn.text.md` 第 5 行，`## Pagina 1` 之后一行的裸 "VOL.4"；10 个 fan-out 均无此行（431 行 vs 432 行）。
- **严重度**：minor（导出噪声，见于 zh-cn 网版正文）。

### 14. nl-pt P1 刊头 kicker 与日期重叠 —— MEDIUM
- **位置**：P1 顶行，印 PDF `2026-w47-nl-pt/De-Lucerna-VOL4-nl-pt.pdf`，y≈59.6pt。
- **证据**：葡萄牙语 kicker "O NEERLANDÊS QUE OS NEERLANDESES LEEM" 过长，末词 "LEEM" 撞上右侧日期 "WEEK VAN 16 TOT EN MET 22 NOVEMBER 2026"，零间隙 —— PyMuPDF 将两者合并为一个 span "LEEMWEEK"（x0=1002.9，x1=1083.9）。实测：kicker 止于 x=1083.9，日期始于 x=1039.5 → **重叠 44.4pt**。其余 10 版均有清晰间隙（core 61.0pt、de 30.5、en 65.4、es 47.6、fr 30.6、it 48.4、ko 49.0、zh-tw 61.0、ru 114.7pt；ja 最紧 4.5pt，视觉有空隙、未相接）。目视确认：首页顶行读作无意义词 "LEEMWEEK"。
- **根因提示**：pt kicker 译的是长描述句（"the Dutch that the Dutch read"），而非短版 "every week" 对应语（如 es "CADA SEMANA EN NEERLANDÉS"）；缩短为如 "TODAS AS SEMANAS EM NEERLANDÊS" 即可容纳。
- **严重度**：MEDIUM（首页可见，日期被读成错词）。

### 15. nl-pt 刊头刊名未本地化 —— low
- **位置**：P1 刊名行。
- **证据**：pt 印版刊名行读作 "WEEKBLAD IN HET NEDERLANDS VOL.4 ORANJE SINTERKLAAS PAKJESAVOND"（荷兰语短语，与 en 版相同），而 pt H1 为 "De Lucerna · Semanário neerlandês VOL.4"、页脚为 "SEMANÁRIO NEERLANDÊS VOL.4"。es/it/fr/de 均本地化刊名（SEMANARIO NEERLANDÉS / SETTIMANALE OLANDESE / JOURNAL NÉERLANDAIS / NIEDERLÄNDISCH）；en 与 pt 共用荷兰语形式，故为版式惯例不一致，非孤例错误。
- **严重度**：low。

### 16. nl-it P2 栏目标题与右侧提问重叠 —— low-medium
- **位置**：P2，"PAKJESAVOND IN VIER WOORDEN PAKJESAVOND IN QUATTRO PAROLE" 标题行，印 PDF `2026-w47-nl-it/De-Lucerna-VOL4-nl-it.pdf`，y≈1180pt。
- **证据**：标题末词 "PAROLE" 止于 x=899.5，右侧提问 "Wat hoort bij pakjesavond?" 始于 x=897.7 → **重叠 1.8pt**。目视确认：版面读作 "PAROLEWat hoort bij pakjesavond?"，无间隙。其余版同行间隙：core 493.0、de 46.4、en 94.6、fr 80.8、ja 146.4、ko 271.9、ru 100.1；es/pt 测得 0.0 为尾随空格假象（标题以空格结尾，视觉有一词空格，见"已核查非问题"）。
- **严重度**：low-medium（D5 盒标题变宽类的同类缺陷；重叠 1.8pt，目视可辨）。

### 17. nl-it P2 "ZO ONTHOUD JE HET" 盒标题溢出盒缘 —— low
- **位置**：P2 中栏奶油盒，标题 "ZO ONTHOUD JE HET RICORDA"。
- **证据**：标题右端 x=721.3，奶油盒右缘 x=720.8 → **溢出 0.5pt**（末字母 "A" 顶出盒缘）。目视确认："RICORDA" 贴到盒右缘。对照：es "RECUERDA" 止于 711.2（余 9.6pt）、en "REMEMBER" 止于 703.5（余 17.3pt）。
- **严重度**：low（D5 预测的粗体盒标题 Newsreader 变宽类缺陷；溢出量小但可测）。

### 18. nl-pt P2 "ZO ONTHOUD JE HET" 盒标题几近贴盒缘 —— low
- **位置**：P2 中栏奶油盒，标题 "ZO ONTHOUD JE HET LEMBRA-TE"。
- **证据**：标题右端 x=718.8，盒右缘 x=720.8 → **仅余 2.0pt**；盒内左 padding 为 13.5pt（417.4−403.9），右侧几乎无 padding。目视确认："LEMBRA-TE" 贴到盒右缘。
- **严重度**：low（未溢出，但与问题 17 同类，D5 变宽所致）。

### 19. nl-es P7 "HET WOORD" 盒标题几近贴盒缘 —— low
- **位置**：P7 右栏奶油盒，标题 "HET WOORD PALABRA SEMANAL"。
- **证据**：标题右端距盒右缘（x=1396.5）**仅余 2.6pt**。P3–P7 盒标题逐盒测量的最紧两处之一（另一处见问题 20）。
- **严重度**：low。

### 20. nl-pt P6 "VOOR OF TEGEN?" 盒标题几近贴盒缘 —— low
- **位置**：P6 右栏奶油盒，标题 "VOOR OF TEGEN? A FAVOR / CONTRA"。
- **证据**：标题右端距盒右缘（x=1396.5）**仅余 2.4pt**。同页 "DE GRAFIEK DADOS DE TREINO" 余 4.1pt（见问题 21）。
- **严重度**：low。

### 21. 其余偏紧的盒标题（观察项）—— trivial
- **位置与实测**：de P2 "ZO ONTHOUD JE HET MERK DIR" 余 4.8pt；pt P6 "DE GRAFIEK DADOS DE TREINO" 余 4.1pt；de P6 "VOOR OF TEGEN? DAFÜR / DAGEGEN" 余 5.2pt；it P7 "PAS OP! CLINICA DEGLI ERRORI" 余 5.6pt；de P6 "DE GRAFIEK ÜBUNGSDATEN" 余 6.2pt；ru P6 "DE GRAFIEK УЧЕБНЫЕ ДАННЫЕ" 余 6.5pt。均未溢出、目视有间隙，列为观察项。ja P1 kicker 间隙 4.5pt（11 版中最紧，目视有小空隙、未相接），亦列为观察项。
- **严重度**：trivial。

## 已核查、非问题

- ru "башмак" ×1（Q131 注释）vs "ботинок" ×8 —— 可接受的同义词；ru Q139 注释 "(88-й)" 与 Q140 注释 "(surprise (фикс.))" —— 简略但可懂；fr Q136 语法注释缺 "+ manner"；pt Q122 保留荷兰语河名 "Maas"；it Q134 "(S + V + C + luogo)"；de Q31 "legt um 10:15 Uhr in De Omval ab" —— 略别扭但可接受；en "de intocht arrival" 注释可接受。
- P3 图注 "Zondag voer de stoomboot…"（SVG 文本确认为 "voer"，100dpi 渲染看似 "voor"）—— 非缺陷。
- P5 注释 "de aflevering （一）集。" —— 全角括号 U+FF08/U+FF09 成对 —— 非缺陷。
- fr Q139 "L'arrivée à Amsterdam" —— 纯 "Amsterdam"，无锐音符 —— 非缺陷。
- P4 词库跨栏断行（core）—— 可读、完整，仅为排版流转痕迹。
- fr 刊名 "JOURNAL NÉERLANDAIS" vs 页脚 "HEBDOMADAIRE NÉERLANDAIS" —— 短名/全名惯例，仅作观察。
- ru P1 目录 "Pag. 2De schoen…" 疑似粘连 —— PDF span 实测：'Pag. 2' + ' De schoen en pakjesavond'（带前导空格），与 en/de 结构相同（仅 Noto Sans 使 "Pag. 2" 宽 0.3pt）；100dpi 渲染假象，非缺陷。
- ru P2 栏目标题疑似粘连 "WOORDENPAKJESAVOND" —— span 实测：'PAKJESAVOND IN VIER WOORDEN' 止于 416.4，俄语注释始于 437.4，间隙 21.0pt；先前拼接为测量脚本 join 假象，非缺陷。
- es/pt P2 栏目标题与右侧提问间隙测得 0.0 —— 标题以尾随空格结尾，视觉有一词空格，非缺陷。
- P2 栏目标题拼接文本中 "DE GRAFIEKÜBUNGSDATEN"、"VOOR OF TEGEN?DAFÜR / DAGEGEN"、"HET WOORDWORT DER WOCHE" 等无空格 —— 测量脚本 join 假象；span 间实有空格，非缺陷。
- 文字碰撞扫描中 CJK/俄语版的大量命中 —— 行距小于字体 bbox 高导致的 y 区间重叠假象；已逐类核对版面渲染，无真实碰撞。
- ja P1 kicker 间隙 4.5pt —— 目视有空隙，未相接（见问题 21 观察项）。
- P8 keydiff 137/138 —— 翻译题答案本就应用读者母语（已人工复核 11 版），非失败。

## D5 重校专项小结

- 弯引号 U+201C/U+201D/U+2019 已路由进 Newsreader（`core-nl/svglib.py` 约 113–131 行核实）；P2 head 23pt 11 版全部无溢出；P8 最小字号 10.12pt（底线 9.75pt）；P8 未变长失控（`p8.py` 150/150 CLEAN）。
- D5-PLAN 预测的"粗体盒标题在 Newsreader 下变宽"类缺陷实际出现：it 溢出 1 处（问题 17，−0.5pt）+ 标题与右侧文本重叠 1 处（问题 16，−1.8pt）+ 几近贴盒缘 3 处（问题 18、19、20，余 2.0–2.6pt）+ 偏紧 6 处（问题 21，余 4.1–6.5pt）。另有 pt P1 kicker 重叠 44.4pt（问题 14，MEDIUM）—— 同类"译文过长顶出版式"缺陷，但非盒标题。
- D5 未覆盖的系统性问题：ru R1（问题 8，MEDIUM）与 R2（问题 9）—— ru 读者路径在 D5 试点中从未触发，D5-PLAN §3 要求的 ru 试点缺口正在此处兑现。

## 工作文件

- 本记录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-w47-nl/PROOF-NOTE.md`
- 机械门日志与 JSON：同目录 `mech/`（occl-*.json/log、p8-*.json/log、p8-core.json/log、diff-core-vs-*.txt、expl-*.txt）
- 逐页渲染 PNG（`pages/`，88 张，约 95M）：校对结束即清理（磁盘纪律；`mech/` 保留）。
