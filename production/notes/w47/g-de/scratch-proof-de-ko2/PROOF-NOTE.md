# PROOF-NOTE — 2026-W47 de-ko · proof2（独立全量复校）

- 版：`2026-w47-de-ko`（德语目标 × 韩语读者，VOL.4，刊期 2026-11-16–22）
- 复校员：proof2（只读复校，不修版、不 commit、不 push、不派 subagent）
- 日期：2026-11-11
- proof1 结论：(a)（`scratch-proof-de-ko1/PROOF-NOTE.md`）；本次为独立复校，重点补 proof1 未做的两项：全版 creambox 扫描、P7 工具盒清除量实测、P8 H-box/Q67 宽引号测量。

## §0 校验和（开工前核对，与简报/KIT 一致）

| 件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 PDF `Die-Lucerna-VOL4-de-ko.pdf` | 15,907,006 B | `1ee2229f5e0d9803d9b32e9c048027a1bced2783bacac9ed72a83499cd866bcc` |
| 网页 PDF `Die-Lucerna-VOL4-de-ko-web.pdf` | 1,909,587 B | `9a0699420966ff7354c3e11d078a2e46ecde8ff35badab03f2be7f8722fe6776` |
| 文本导出 `2026-w47-de-ko.text.md` | 51,498 B | `fd2dbd047e23bcd0fffc5245ee8d529b9e848adc11133ff46f490b304b8a66a2` |

三件 SHA 均与简报一致；text.md 与 fix 前相同（未变）。探针通过：`git hash-object` rc=0，scratch 目录真实写文件通过。

## §1 文本通读（text.md 全 1,185 行，P1–P8 + 答案 1–150）

德语正文与韩语讲解层逐句读过，未发现语言错误、译错或数字错误。

- **算术/日期**：18.11+11=29.11（第一降临节）、15.11+7=22.11（追思主日）、16.11+6=22.11；图表 44+33=77、44+33+23=100；第 9 轮 9 场共 30 球（4+3+3+7+4+1+3+2+3）；16 个比分在 P1/P4/赛程表三处一致。星期核对（Europe/Berlin）：11-03 周二、11-04 周三、11-05 周四、11-06 周五、11-07 周六、11-08 周日、11-13 周五、11-15 周日、11-16 周一、11-17 周二、11-18 周三、11-20 周五、11-22 周日、11-24 周二、11-25 周三、11-26 周四、11-27 周五、11-29 周日——全部与正文一致。
- **150 题键逐题语义核对**：抽查/通读中核对的键均与题干一致，如 Q5 fünf、Q14 Mittwoch、Q16–20 完成时、Q25–28 d/c/a/b、Q34 Weihnachtsmarkt、Q51 B（8 und 5）、Q52–55 d/b/c/a、Q56–59 mehr/später/früher/mehr、Q76–79 weil 末位动词、Q93 wird、Q98 Kirchenjahr、Q101–103 wird/werden/wird、Q111 `Ich finde, dass das Gedenken Stille braucht`、Q113–120 A/B/A/B/A/A/B/A、Q137–139 韩译、Q140 `Am Montag schaue ich zu Hause Deutschland gegen die Niederlande.`、Q141–144 c/a/d/b、Q145–149 A/B/A/A/A、Q150 自由题。P7 Sätze der Woche 8/8 逐字出自正文，出处页码正确。
- **Q137–140 双重说明**：`(한국어로 번역하세요) [한국어로 번역하세요]` 双重结构继承自 core-de（中文核心版同结构），非 ko 版引入，不作缺陷。
- **引号用法**：`« »` 用于周词/H-box 标题/NOCH EIN WORT，`„ "` 用于引语/标题——按角色一致，不作缺陷。

### 事实逐条网查（2026-11-11，来源见 GATE-LOG）

全部通过，无事实错误：

- 欧冠第 4 轮：拜仁 2:0 马竞（11-03，Karl 54'、Laimer 74'）；多特 2:1 贝蒂斯（11-04）；莱比锡 2:3 曼城（11-04）；斯图加特 0:2 加拉塔萨雷（11-03，伊斯坦布尔）。下轮：11-24 阿森纳–多特、莱比锡–朗斯；11-25 国米–斯图加特、里尔–拜仁。
- 欧战 11-05：勒沃库森 0:1 马赛、霍芬海姆 1:1 水晶宫、弗赖堡 1:0 特拉布宗。欧联第 5 轮 11-26 萨格勒布迪纳摩–勒沃库森已确认。
- 德甲第 9 轮（11-06–08）9 场比分全对且总进球 30 球：美因茨 1:2 拜仁、多特 2:1 埃尔弗斯贝格、莱比锡 5:2 奥格斯堡、帕德博恩 2:2 法兰克福、斯图加特 1:0 不来梅、科隆 1:2 勒沃库森、弗赖堡 2:0 柏林联、霍芬海姆 2:1 沙尔克、汉堡 3:1 门兴。拜仁榜首、科隆第 15——与“Die Bayern führen die Tabelle an — Köln ist Fünfzehnter”一致。
- 塞尔维亚–德国 11-13 贝尔格莱德：欧足联观众禁令（仅 15 岁以下儿童 + 约 50 名德国球迷，约 5,000 人预计到场），20:45，Rajko Mitić，RTL。欧国联 A2 组 4 轮后：荷兰 8 分、希腊 8 分、德国 5 分；德国–荷兰 11-16 周一柏林 20:45 ARD——与“Endspiel um das Viertelfinale”一致。
- 德甲第 10 轮：拜仁–科隆 11-20 周五 20:30；周六 5 场 15:30 + 沙尔克–斯图加特 18:30；周日奥格斯堡–美因茨 15:30、不来梅–汉堡 17:30。
- 忏悔祈祷日（Buß- und Bettag）：2026-11-18 周三；仅萨克森法定假日；1995 年废除（为护理保险筹资）、萨克森雇员多缴 +0.5 个百分点；巴伐利亚学校停课；安静日（stiller Tag），萨克森《节日法》§6：公开舞会 3:00–24:00 禁止（原文引句逐字与法律文本一致）。
- 科隆圣诞市场：大教堂市场 11-16–12-23，11-22（追思主日）关闭，官方开幕 11-17 19:00；天使市场（Neumarkt）11-16–12-23，11-22 关闭；港口圣诞市场 11-13–01-03；亚琛市场 11-20–12-23（第 53 届）。
- 1903 年降临节日历 “Im Lande des Christkinds”（Gerhard Lang，Richard Ernst Kepler 插图，24 幅图粘贴式）。注：1903 年原版为无窗式（fensterlos），正文“die Fenster mit Bildern überkleben”属简化表述，不作缺陷。
- Wilhelm Ritter（1860–1948），画作 “Weihnachtsmarkt auf der vorderen Insel Schütt”（1930）——标题与正文逐字一致。
- 电费税：家庭 2.05 Cent/kWh；Merz 主张全民降至欧盟最低，Klingbeil 谨慎/2027 预算无空间；2027 联邦预算表决计划 2026-11-27 周五（11-12 为委员会清理会，非全会表决）。
- 追思主日 11-22、第一降临节 11-29（日历计算；11-18 为追思主日前一周三，11 天间隔与“elf Tage vor dem ersten Advent”一致）。

## §2 逐页目视（印刷 PDF 100 dpi 全页 + 200 dpi 关键裁切）

- **P1**：干净。刊头、头条、导语、数字盒、FRAGEN、IN DIESER AUSGABE、WORT DER WOCHE、足球照片+图注、EINE WOCHE ZWEI STIMMUNGEN、KURZ & GUT、BLITZQUIZ 7–10 齐全，无溢出。
- **P2**：干净。Buß- und Bettag 正文、右侧四盒、RECHNEN WIR MAL、练习 11–28 齐全，无溢出。
- **P3**：干净。圣诞市场正文、Ritter 画作+图注、右侧三盒、练习 29–46 齐全。Q34 单数题干 200 dpi 裁切确认（§6）。
- **P4**：干净。体育正文、赛程表 9 行（含斑马纹）、足球照片+图注、练习 47–64 齐全。图表区无挤压。
- **P5**：干净。降临节日历正文、1903 日历图+图注、编辑部周计划表、练习 65–82 齐全。
- **P6**：干净。深化正文、DIE STILLE WOCHE 盒、DIE ZAHLEN 盒、DEBATTE 盒、民调柱状图（44/33/23 柱长比例正确）、练习 83–100 齐全。ÜBUNGSDATEN 说明行在位。
- **P7**：干净。三栏语言课、BEISPIELE 三盒、工具盒（§7）、LESERBRIEFE、NOCH EIN WORT、Library of Congress 照片+图注、Sätze der Woche 8 条、FEHLERKLINIK 4 对、下期预告盒齐全，无溢出。
- **P8**：干净。A–H 全部练习、MUSTER 模范文（84 词标签）、1905 足球照片+图注、ANTWORTEN 全部 150 题答案在页脚线上方结束，无挤压（§4 裁切确认）。

## §3 门禁（全套，日志见 gates/）

| 门禁 | 结果 |
|---|---|
| occlusion_audit.py（真实跑，非 --selftest） | **0 flags**，rc=0；自测已验证（6 类 planted 均触发，干净对照静默） |
| p8.py extract | **150/150**，rc=0 |
| p8.py compare vs core-de | **CLEAN**，missing=[]，keydiff=[137, 138, 139, 150]（预期内，见 §8） |
| freeze.py diff | 全部 CJK 新增 **3,096**（韩语讲解层） |
| freeze_direct.py（source，`scratch-fanout-de/` 副本，见 §8 偏差说明） | **PASS**（unaccounted removed 0 / added 0），rendered 8/8；SHA 与 KIT 一致：73347f49 / 689045ad / 8b2e9eba / df1bebf7 / e7b235f9 / 2bbe05f9 / 591dc064 / f6dd4a15 |
| boxtitle.py（同上副本） | **7/7 fit**，rc=0；最紧 `WEIHNACHTSWÖRTER　크리스마스` 395.8/400.5 |
| keycheck.py | **148/150**，rc=1（预期内）；仅 Q139、Q150 提取器 artifact（§8） |
| P8 最小字号（PyMuPDF 渲染 pt） | **9.94pt**，印刷与网页一致（≥9.75pt 下限） |
| d2scan.py abutting | 72 对检查，**0 个网页间隙 >0.5pt** |
| text layer（pdftotext） | 逐页词多重集印≡网（8/8）；全文默认文本**字节相同**（各 52,318 B）；`-raw`**字节相同**（各 51,151 B） |

### 全版 creambox 扫描（canonical `tools/creambox.py`，8 个 SVG 全扫）

- **P7 工具盒实测确认 fix 宣称**：盒底 774.0，最后基线 754.8，**清除 +19.2，desc-clear +13.1**；LESERBRIEFE 盒内 +10.4（desc-clear +4.5）；NOCH EIN WORT 最后基线 1465.6，清除 +42.9（盒底 1508.5）。P7-TOOLBOX 汇总：6 盒，盒内最小清除 +10.4，最小 desc-clear +4.5。
- 其余负原始清除值均已裁定为已知假阳性：P1 −37.0/−24.0（窗下标题 JETZT ÜBEN +37.0、DAS WORT DER WOCHE +24.0；盒内 +45.7/+16.0）、P2 −44.9（窗下标题 'Die Daten der Woche' +44.9；盒内 +19.5）、P7 三个 −35.0 行（BEISPIELE 盒误配下方练习序号，FIX-LOG §1 已记录假阳性；盒内 +47.4）。P8 MUSTER 盒内 +47.1。
- **每盒盒内清除 ≥ +10.4，无真溢出。**未用窄带 creambox_check.py 作证据。

## §4 网页 PDF / 文本层

- 8 页网页版目视（200 dpi）：P8 与印刷版版式、文字、位置一致；P3 与印刷版一致（抽查）。
- 印/网 text layer 字节比对（§3）：默认与 `-raw` 均字节相同；逐页词多重集 8/8 相同。
- P8 答案区底部 200 dpi 裁切：最后答案行（37. Advent / 78. Sie geht… / 117. A）距页脚线约 150pt，无挤压。

## §5 引号计数

- text.md：U+201C 33 个 / U+201D 0 / U+201E 33 个 / U+2019 0；8 个 SVG 合计相同（P1 5、P5 6、P7 21、P8 1）。
- « » 各 6 个、成对（P1 1、P5 1、P7 1、P8 3）。

## §6 Q34（单数题干）

- text.md、P3 SVG、印刷与网页 text layer：新单数题干 `Am Montag öffnet in Köln der erste ___.` 各出现 1 次，旧复数题干 0 次。
- 200 dpi 裁切确认：`A2 34. Am Montag öffnet in Köln der erste ___.`——单数 `der erste`，空位正确。

## §7 P7 工具盒重测（本次重点之一）

- `content7.py:76` 确认 pad 110 及 fix1 算术注释。
- canonical creambox.py 实测：工具盒底 774.0，最后基线 754.8，清除 **+19.2**，desc-clear +13.1——与家庭修宣称（+19.2、774.0）逐数一致。
- 300 dpi 工具盒放大裁切目视：6 条全部在奶油盒内，末条 `Es ist fraglich, ob ... = 아직 미정` 下方有明显奶油留白，盒底在文字下方；LESERBRIEFE 标题在下一盒顶部，两盒间有白间隔。
- LESERBRIEFE 盒内 +10.4，NOCH EIN WORT 止于 1508.5（最后基线 1465.6 +42.9）——宣称全部属实。

## §8 既存/继承项（照实记录，不拦停定稿）

- **keycheck 148/150**：Q139 提取 `대림절 달력을만들고 있습니다.` vs 键 `대림절 달력을 만들고 있습니다.`（空格提取 artifact）；Q150 提取 `자유과제` vs 键 `자유 과제 — 쓰기 상자의 항목을 따르세요`（提取器截断）。KIT 已记录的既存项，非 ko 版缺陷。
- **p8 compare keydiff [137, 138, 139, 150]**：预期内（Q137–139 为韩译题、Q150 为自由题，核心版键不适用）。
- **工具副本偏差**：简报要求 freeze_direct/boxtitle 用 rebuild-A 的新副本，但 rebuild-A 无 ko 文件（仅 en/es/fr/it/pt + tr 文件）；按 fix1 `gates.sh` 注释，ko 当前 `tr_ko.py` 位于 `scratch-fanout-de/`，freeze_direct.py、boxtitle.py、keycheck.py 均从该目录跑。已记录此偏差，原因如上。
- 1903 年降临节日历“窗口粘贴”表述为简化（§1），不作缺陷。

## §9 P8 H-box / Q67 宽引号测量（de-en D1/D2 方法，200 dpi 墨列测量）

方法来源：`scratch-proof-de-zh-tw2/quote_pixel.py`（单连续 x 窗口，任意像素 <128 为墨，引号墨 = 起点落在引号进位框内 ±1px 的墨列；闭引号前空隙 >0.2em 为缺陷）。字符位置取自印刷 PDF PyMuPDF rawdict。

| 点 | 字体/字号 | 前空隙 | 结论 |
|---|---|---|---|
| H-box 德语闭引号 »（«Meine Novemberwoche»） | Newsreader 16.12pt | **1.80pt = 0.11em** | PASS |
| Q67 键闭引号 »（«Im Lande des Christkinds»） | NotoSansCJKsc 9.94pt | **0.0pt = 0.00em**（300 dpi 干净带复测确认） | PASS |
| H-box 韩语闭引号 』（『11월의 나의 한 주』） | NotoSansCJKsc 15pt | **1.44pt = 0.10em** | PASS |
| P8 对话闭引号 “（对照） | Newsreader 14.62pt | 1.44pt = 0.10em | PASS |
| P7 NOCH EIN WORT »（对照） | Newsreader 15.38pt | 1.44pt = 0.09em | PASS |

- Q67 细节：200 dpi 下 's' 与 » 的墨列连续无间（脚本初次“quote ink=[]”系归因 artifact，非宽空隙）；300 dpi 干净带（y 1831.53–1845.92）复测：前一墨列止于 505.80pt，引号区首墨列始于 505.80pt，空隙 **0.0pt**。300 dpi 裁切目视：`ds» (`——» 紧贴 s，无可见空隙。
- H-box 裁切目视：» 紧贴 `Novemberwoche` 的 e，无宽空隙。
- **de-en D1/D2 类缺陷在 de-ko 未复现**：五点全部 ≤0.11em，远低于 0.2em 阈值。
- zh-tw proof2 同类加测亦未复现（H 0.11em、Q67 0.11em），与 de-ko 结论一致。

## §10 ABSTRACT（SOP §9）

- `ABSTRACT.txt`：388 B，**单行**，韩语，无 ASCII 双引号，内容与本期一致（분데스리가 복귀/바이에른 홈 대 쾰른、네덜란드와의 네이션스리그 결전、참회와 기도의 날과 죽은 자의 주일、쾰른 크리스마스 시장 개장、11월 3~8일 유럽 대항전과 분데스리가 결과、독일어 텍스트/한국어 설명、A2~B2、150문제），含刊名 Die Lucerna、目标语名（독일어 주간）、A2–B2 与题数 150，文内 VOL.4 与台账（W47=VOL.4）一致。
- SOP §9“出现两次”（md frontmatter `abstract` + 正文摘要节）为**入仓时生成**：`tools/insert.py`（165–180 行）读取 ABSTRACT.txt，校验单行/无 ASCII 双引号/VOL.n 与台账一致（本版三项均通过），再写入 frontmatter `abstract` 字段与正文摘要节（标题取 `tables.json` languages.ko.abstract_heading =「요약」）。因此 proof2 阶段可核的唯一件即 ABSTRACT.txt 本身——已验证合格；frontmatter 与摘要节尚不存在，非缺失。
- 横向对照：de-en、de-zh-tw、de-es 三版 ABSTRACT.txt 与 de-ko 同模板（亦无“learn German by reading”式搜索短语）；三版 text.md 中 “abstract” 出现均为 0 次——属全家一致的既定形态，非 de-ko 缺陷。
- 摘要句在生产树中的来源位置：ABSTRACT.txt 即 SOP 指定的交付件（“构建者在版本目录交付 ABSTRACT.txt”），insert.py 机制已说明其来源；生产树全文 grep 已由该机制说明取代，不再追查。

## Verdict

**(a) 零问题，可定稿。**

本次独立全量复校未发现缺陷：P7 工具盒清除量实测与家庭修宣称逐数一致（+19.2、盒底 774.0）；P8 H-box/Q67 宽引号五点测量全部 ≤0.11em，de-en D1/D2 类缺陷未复现；全版 creambox 扫描每盒盒内清除 ≥+10.4；全部事实逐条网查通过；150 题键语义核对通过；印/网文本层字节相同。D1…：无。
