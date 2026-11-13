# W47 zh-cn-it 第一轮独立校对笔记（proof1）

- 校对员：独立复校员（与 zh-cn-it builder、zh-cn 核心 builder、各轮复校员不同人）
- 对象：`production/2026-w47/2026-w47-zh-cn-it/`（fan-out #3，2026-11-11）
- 日期：2026-11-11（EST 13:04 开工）
- 依据：SOP.md §8/§1.1、WEEKLY-KIT.md（zh-cn-it）、FANOUT-REPORT-zh-cn.md 第 #3 棒
  （`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-zh-cn/`）
  it/EDITION-RECORD.md、核心 `production/2026-w47/core-zh-cn/WEEKLY-KIT.md`（proof3 (a)）
- 工作目录：`~/workspace/weekly-git`（main）；笔记目录：`hidden_files/w47/scratch-proof-zh-cn-it1/`
- 红线遵守：只读 production；未改任何生产文件、未 commit/push/insert、未跑 lint --write。
  run.py 重建在 scratch 副本里做（OUT 为副本自有 svg/）；render.py 未重跑（会重写成品 PDF；
  SVG 层重跑 8/8 已证构建确定性）。开工快照与收工快照比对见末节。

## 开工探针（双通）

- `echo test | git hash-object -w --stdin` 成功（9daeafb9…）。
- `hidden_files/w47/scratch-proof-zh-cn-it1/probe.txt` 真实写盘成功。
- 注：任务所指 `hidden_files/w47/briefs/brief-coordinator.md` 在 weekly-git 内不存在
  （hidden_files/w47/ 下无 briefs/ 目录）；改按 FANOUT-REPORT-zh-cn.md + it/EDITION-RECORD.md
  + KIT 作为 #3 报告来源核对。无内容影响。

## 身份核对（自行算出，与协调员先验值逐字比对）

| 文件 | 字节 | SHA-256（完整，我方实测） | 与先验值 |
|---|---|---|---|
| 印刷 PDF `Lucerna-VOL4-IT.pdf` | 41,730,134 | `d1ae6f877573b068e757e12b69a9dcb67dd8fd5242e02d5c10b17b95fd52a001` | 一致 |
| 网页 PDF `Lucerna-VOL4-IT-web.pdf` | 2,641,804 | `75dec91ac806b884bdd4b7cdbdccc39e2c445ff7f668d24ff4365f21f233a512` | 一致 |
| 文本导出 `2026-w47-zh-cn-it.text.md` | 50,958 | `f954151fb204030d9d273e0f0032d9674509fd9bb170c7fc460c062eec46ecc4` | 一致 |

三 SHA 全符，继续校对。双 PDF 均为 8 页。

## 结论：5 条缺陷，不可定稿

按 SOP §8.4，fan-out 版定稿须经独立复校零问题。本轮发现 **5 条几何缺陷（D-01～D-05，
同属一个缺陷类：意大利语尾过长，标题/行尾越出无边框奶油盒）**，其余全部通过。
定稿决定权在协调员，本笔记只报事实。**机械门 11/11 全绿未拦下这 5 条**（原因见
「工具缺口」一节）——门绿不等于版面干净。

## 缺陷清单

### D-01（中）：P1 数字框标题越奶油盒右缘 46.5 px

- 位置：P1「数字看本周」盒标题 `数字看本周　Questa settimana in numeri`。
- 盒：cream rect x=538.5, w=422.5 → 右缘 961.0；标题 x=556.5, 23pt Bold。
- 实测（PIL 真墨，Noto Sans CJK SC Bold idx2，与 builder 自己的量法逐项对表验证：
  A-head advance 377.1、D-head 407.8、日历标题 1424.3 三处与 builder 数值分毫不差）：
  全串 advance 451.1，墨右 1007.5 → **越盒 46.5 px**；Regular 字重下仍越 29.5 px。
- 渲染证据：`crop-p1-numbers-title.png`（交付印 PDF 110 dpi 渲染）——“numeri”
  明显落在白纸上，盒的奶油底在其左结束。网 PDF 同位置同缺陷
  （`crop-web-p1-numbers-title.png`）。SVG 源码行：
  `svg/p1-touiban.svg`：`<text x="556.5" y="1147.265" … font-size="23" font-weight="700">数字看本周　Questa settimana in numeri</text>`。
- 成因：fan-out 引入——核心同盒标题只有中文，意大利尾把它推过盒缘。

### D-02（中）：P5 高频词盒标题越奶油盒右缘 33.5 px

- 位置：P5「这一周的高频词」盒标题 `这一周的高频词　Parole della settimana`。
- 盒：cream rect x=538.5, y=648.0, w=422.5 → 右缘 961.0；标题 x=556.5, y=685.0, 23pt Bold。
- 实测：墨右 994.5 → **越盒 33.5 px**。
- 渲染证据：`crop-p5-freq-title.png`——“settimana”落在白纸上。
  Builder 的 #3 报告未提此盒（9 处修复点不含它）；属同类漏检。

### D-03（中）：P1 截止线越奶油盒右缘 18.5 px

- 位置：P1 右栏日历盒内末行 `Chiusura: 10 nov. — la finale non ancora giocata`。
- 盒：cream rect x=1439.5, w=422.5 → 右缘 1862.0；行 x=1461.5, y=1252.0, 19pt。
- 实测：墨右 1880.5 → **越盒 18.5 px**；同盒上一行
  `Chiusura: 10 nov. La finale è il 15 nov. alle` 墨右 1805.5，余 56.5 px，通过。
- 渲染证据：`crop-p1-chiusura.png`——“giocata”落在白纸上。

### D-04（中）：P2「本周生活小日历」标题越奶油盒右缘 12.5 px

- 位置：P2 日历盒标题 `本周生活小日历　Date della settimana`。
- 盒：cream rect x=989.0, y=200.0, w=422.5 → 右缘 1411.5；标题 x=1007.0, y=237.0, 23pt Bold。
- 实测：advance_end 1424.3（与 builder 声称的 1424.3 一致），墨右 1424.0 → **越盒 12.5 px**。
- 关键：builder 的 #3 修复是按**照片**量的（“15.2 px clear of the valley photo at x=1439.5”）——
  标题确实没碰到照片，但它先越过了自己盒子的右缘 1411.5。量错了边界。
- 渲染证据：`crop-p2-cal-title.png`——“settimana”落在奶油盒与照片之间的白纸上。

### D-05（轻）：P1 数字框第 3 项孤儿 "》" 行首

- 位置：P1 数字框第 3 项 `21 nov., sabato — esce il nuovo film 《试探》` 折行后，
  收尾 "》" 独自落在下一行行首（x=556.5, y=1366.3，单独一个 `<text>` 元素）。
- 渲染证据：`crop-p1-numbers-box.png`——"》" 单独一行。
- 全刊行首闭合标点扫描（逐元素 + 同基线左邻判定）：全刊仅此一处；核心同位置无此元素
  （核心英文行较短，不折行）——fan-out 引入。P3/P6 的 "”" 与 P7 的 "」"、
  P4 的 "），八强" 均经核对为**行中**（同基线左有邻元）且与核心逐字同位（x、y 完全相同），
  继承自核心，不计缺陷。

## #3 报告 9 处修复点逐项复核（全部存活）

| # | 修复点 | 源码行 | 实测值 | 结论 |
|---|---|---|---|---|
| 1–5 | A-head ×5 `Leggi e scegli`（P2–P6） | content12.py:1处、content34.py:2处、content56.py:2处；SVG 各 1 处 | 全串 advance 377.1 px（25pt Bold），栏余 45.5 px | 存活 ✓ |
| 6 | P8 D-head `Leggi, rispondi` | content8.py:74；SVG P8 x=989, 24pt | advance 407.8 px，栏余 14.5 px | 存活 ✓ |
| 7 | P2 日历标题 `Date della settimana` | content12.py:187；SVG P2 x=1007, y=237 | advance_end 1424.3（与 builder 一致） | 存活，但见 D-04：修的是照片边界，盒边界仍越 12.5 px |
| 8a | P8 note Q20 | content12.py:269 | `SF Express dello Hunan: +20 % di personale e capacità.`，keys flow 终 2506.4 | 存活 ✓（一行） |
| 8b | P8 note Q24 | content12.py:279 | `L'anno scorso, giorno migliore: 777 milioni di articoli.` | 存活 ✓（一行） |
| 8c | P8 note Q95 | content56.py:222 | `Una barra: totale 22 giorni; l'altra: picco di un giorno.` | 存活 ✓（一行） |
| 8d | P8 note Q109 | content7.py:51 | `「139.38亿件」: conteggio finale delle Poste, già contato.` | 存活 ✓（一行） |
| 8e | P8 note Q148 | content8.py:91 | `Dopo la Piccola Neve, vestiti pesante, non prendere freddo.` | 存活 ✓（一行） |
| 8f | P8 note Q150（f-string） | content8.py:102 | `Esercizio aperto — modello sopra, sezione F (138 caratteri).`，范文实数 138 字（自数，与 run.py `writing model chars: 138` 一致） | 存活 ✓（一行） |
| 9a | P4 gloss 不缩短 | content34.py gloss；SVG P4 Note｜起 6 行 y=595.9–744.5 | 意大利语前缀 `Note｜` 实测；6 行；盒底 792.2，下方 GEN 行 y=822.4，净空 | 通过 ✓ |
| 9b | P2 词卡例句 1 行 | SVG P2 y=1752.1，4 句各 1 个 `<text>`，19pt | advance 329.5/345.3/343.9/213.6，对 378.5 px 卡内宽余 27.0/11.2/12.6/142.9 px | 通过 ✓ |

## 核心 D4/D5 同步落地（逐处源码行 + 实测值）

核心 `core-zh-cn` fix2（proof3 (a)）的 D4/D5 在本版全部同步落地，旧措辞 0 残留
（SVG joined-text 计数）：

| 项 | 源码行 | SVG 实测 |
|---|---|---|
| D4 P4 正文「第一次在全球总决赛的BO5里打赢T1」 | content34.py:130 | `全球总决赛的BO5` P4 ×2（正文 + Q56 题干） |
| D4 Q56 题干 | content34.py:211 `BLG是第一次在全球总决赛的BO5里打赢___。`，键 T1 | P8 键 56：`T1 — BLG ha battuto T1 per la prima volta in un BO5 dei Worlds.`（意大利语键注，Worlds 为赛事名保留） |
| D4 旧措辞 | — | `第一次在BO5里打赢T1`（无限定）全刊 0；旧英文键注 `for the first time in a Worlds BO5` 0 |
| D5 P1 | content12.py:42 `GEN在S16一场没输，只丢了一小局：瑞士轮3胜0负，八强3比0，半决赛3比0。` | P1 ×1 |
| D5 P4 | content34.py:131 `GEN在S16一场没输，只丢了一小局——瑞士轮3胜0负（对LYON 2比1），八强3比0，半决赛3比0。` | P4 ×1；`对LYON 2比1` P4 ×1 |
| D5 保留项 | content34.py:160 `GEN今年 — 淘汰赛一局没输` | P4 ×1（淘汰赛 QF 3–0 + SF 3–0 共 6–0，为真，范围正确） |
| D5 旧措辞 | — | `GEN今年一局没输` 全刊 0 |

## 150 题逐题手验（key 与题干配对，非仅三源一致）

- 自跑 keycheck（stub 补 `glossline`/`ci` 后，见 GATE-LOG）：REG 150 条，P8 SVG 抽取键
  150 条，**149/150 精确**；唯一非精确为 Q150 开放写作题（REG 键 `(开放题，范文如下)`，
  印刷键为 `✓`，为预期内的开放题标记，与 de-fr 的 Q150 截断同类）。
- 逐题验算（`reg-dump.txt`，题干、原文、图表再验算）：149 题键与题干/正文/图表全部相符，
  含 20 道词汇配对（逐项核对左右列语义：Q25–28 a/b/c/d、Q43–46 b/d/a/c、Q61–64 d/b/c/a、
  Q79–82 c/b/d/a、Q97–100 c/d/a/b——配对定义与键一一对应；Q25–28 键恰为 a/b/c/d 顺序，
  系核心继承的出题编排，未改）、Q56（D4）、完形 Q113–120（A/B/B/A/A/B/A/B，
  与题面逐一核对）、对话 Q147–149（A/A/A）、翻译/造句/图表题（Q83–96 的 139.38/7.77/
  三波/22 天等数字与 P6 正文、图表互核一致）、P8 D 篇小林短文 Q141–149
  （深圳、11月8日半决赛、网上买书、11月11日取件、11月14日与妈妈去文化馆、顺序
  半决赛→包裹→文化馆，与短文逐句核对；星期核对：11月8日星期日、11月11日星期三、
  11月14日星期六、11月15日星期日，与核心 KIT 的 `date -d` 表一致）。
- 分版：{1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；级别 A2 56 / B1 69 / B2 25；
  题型 完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1；编号连续 1–150。
  均与 KIT 一致。

## 全量目视（自 print PDF 重新渲染 110 dpi，不采信 builder 的图）

- P1–P8 逐版目视：除 D-01～D-05 外，零溢出、零重叠、零压页脚、图片与出处均在位。
  网页 PDF P1 目视与印刷版一致（含 D-01 同缺陷）。
- P4 gloss 盒 6 行、GEN 行净空；P5 C 头 `Ore e numeri` 在位；P7 teaser 带止于 2562.26，
  离页脚线 2596 有余；P8 D 头、keys 1–150 + 页脚清楚，无压线。
- 事实抽查（均与正文/表格互核一致）：P2 算术 320−80=240、196 城/4 小时；
  P4 赛程 QF 11月4–7日、SF 11月8–9日、决赛 11月15日 03:00、BLG 三胜 LCK；
  P6 图表 139.38/7.77、22 天 vs 一天、三波 10月20日/10月31日/11月11日；
  P5 片单（《试探》11月21日、《珠穆朗玛》11月6日、《我们仅有一次的人生》11月7日、
  《白衣逆行者》撤档）；P3 小雪 11月22日星期日、第 20 个节气、冬天第 2 个；
  11月15日星期日、11月21日星期六、11月22日星期日均与 `date -d` 一致。

## 金句 8 条逐字比对正文（SOP §4）

SVG joined-text 计数：8 句在全刊各出现 **2 次**（正文 1 次 + P7 1 次），逐字一致：
「决赛对阵GEN」(P1)、「包裹都到了吗」(P2)、「小雪气寒而将雪矣」(P3)、
「两支中国队进了四强」(P4)、「先看简介，再决定」(P5)、「无高峰，全高峰」(P6)、
「先打开看一看，再确认收货」(P6)、「悦读深圳」(P3)。来源标注页码与正文出处一致；
8 条意大利译文均准确。

## 几何专项（de/fr 同族缺陷类）

- P1 数字框标题：**越盒，见 D-01**（PIL 真墨 + 交付 PDF 渲染像素双重验证）。
- P2「本周生活小日历」标题：**越盒，见 D-04**（量错边界：builder 只量了照片）。
- P1 数字框内引用收尾引号孤儿行首：数字框仅有 D-05 的孤儿 "》"；全刊行首闭合标点
  扫描仅 D-05 一处；P1 无 "”/」" 行首项。
- P1 截止线：两行中第一行余 56.5 px 通过，第二行**越盒，见 D-03**。
- 全刊奶油盒内文本大扫查（522 个文本元，PIL 真墨逐个量右缘）：溢出 4 处即 D-01～D-04；
  仅 1 处贴边：P4「看比赛的中文　Parole delle partite」余 6.5 px，通过（贴边但未越）。

## 工具缺口（须回写工具，见 GATE-LOG）

**`tools/occlusion_audit.py` 的 BOXTITLE 类对无边框奶油盒全盲。** 源码
`tools/occlusion_audit.py:471-474`：BOXTITLE 只看带 `stroke` 或 fill `#2c2822` 的 rect；
SOP §1.1 规定侧栏小框不加边框、用浅底 `#f0eee5` 区分——本版全部奶油盒都是无边框
`#f0eee5`，于是 4 处标题/行尾越盒（D-01～D-04）全部漏过，审计仍报 0 flags。
Builder 的 gates-zhcn.py 11 门全绿同样未拦下。建议：BOXTITLE 候选 rect 增加
fill `#f0eee5` 的无边框盒（或凡是含文本的浅底 rect），并补一则阳性对照
（P1 数字框标题即现成用例）。

## 翻译层专项（fan-out 特有）

- 讲解/界面语言确为意大利语：栏目副题、桥接、说明、Note（前缀 `Note｜`，非英文量）、
  工具箱、读者园地披露、练习数据注、答案简析、ABSTRACT 均为意大利语；
  意大利语拼写/性数/变位抽查无误（如 `l'ultima partita`、`non è automatico`、
  `è il 20º termine solare`、`Il picco dei pacchi è dall'11 al 13 nov.`）。
- 泄漏扫描（SVG `<text>` 全部拉丁词频）：无真实英文残留。英文形词均为有意保留：
  `Level A2/B1/B2`（KIT 已裁定，沿 W46 成品）；`Sunday, Nov 22`（P7 B1 教学对照句，
  举英文日期顺序为例）；`Worlds`（S16 赛事名，Q56 键注）；`Double 11`（活动名）；
  `Barclays Center / Brooklyn`、`SF Express / Hunan`、`Sina`（专名）；
  `Foto: … — CC0 (Wikimedia Commons)`（图注按 W45 先例留英文）；`Sport`
  （意大利语同形）；`test / trend / online / shopping / suspense / quiz`
  （意大利语通用外来词）；`Note｜` 前缀为意大利语量，非英文。
- 读者园地：P7 为编者示例 + 意大利语披露 `Nota della redazione: VOL.3 aveva
  promesso lettere vere in VOL.4; nessuna è arrivata entro il 10 nov. Rimandato,
  non cancellato.`，与 KIT / F-MAIL 规则一致。
- 范文：标签 `(138 caratteri)`；范文自数 **138 字**，与 run.py 一致。
- ABSTRACT.txt：319 B，意大利语单行，0 个 ASCII 双引号，内容与本期事实一致。
- 刊头/页脚：`TESTO CINESE　SPIEGAZIONI IN ITALIANO` 拉丁-only 徽章（P1 x=88, y=434, 14pt）；
  页脚 `Lucerna　简体中文周报 VOL.4　LUCERNA — SETTIMANALE IN CINESE SEMPLIFICATO`、
  页码行 `Pagina N di 8`（N=1–8）逐页核实；P7 的 VOL.3/VOL.5 为内容引用
  （下期预告 VOL.5、读者园地提 VOL.3），与核心逐字同位，非误印。
- U+2019：全刊 0；U+201C 2 处（P3/P6 中文引号 “…” 的开引号，正确）。

## VOL.4、徽章、字号

- VOL.4：刊头 `简体中文版　VOL.4　S16决赛　包裹到了　小雪`、页脚 VOL.4、页码行逐页核实。
- P8 最小字号：PyMuPDF 独立实测印刷 PDF 与网页 PDF 均为 **9.98pt ≥ 9.75pt**
  （SOP §1.1 底线；P8 其余字号至 34.5pt；P1 最小 10.50pt）。与 builder 的 9.98pt 一致。
  注：底线是 9.75pt 不是 10pt，9.98pt 通过（核心设计值）。
- P8 chips：A2 11 / B1 24 / B2 3 = 核心。

## 机械门全套自跑（构建解释器 tools/venv/bin/python）

详见 GATE-LOG.md。结果一览：freeze diff --strict-cjk TOTAL added CJK **0**（exit 0）；
freeze baseline（核心，现行口径 `--build` 核心目录 + `--core-svg` 核心 svg 子目录）
8/8 字节一致、核心完整性确认；run.py scratch 重建 8/8 SVG 字节一致、TOTAL 150、0 溢出；
p8 extract 150/150、compare CLEAN keydiff=[]；occlusion 0 flags（自检 OK——但见「工具缺口」，
此 0 旗不覆盖 D-01～D-04）；印/网文字层逐字相同（pdftotext 44,907 B 双份，
词多重集 4,823 词一致；gates 逐页 posdiff/msdiff 0）；gates-zhcn.py 11/11 全过（自跑复现）。

## 观察项（单独列，不计缺陷）

- **O-1**：P1 Chiusura 段意大利语 `Le semifinali (8–9 nov.) sono risultati completi.`
  措辞略生硬（应为 `sono concluse` 一类），但可解、无事实错；核心英文底本同构，属翻译层
  风格项，不计缺陷。
- **O-2**：P4「看比赛的中文　Parole delle partite」盒标题余 6.5 px，贴边但未越，通过。
- **O-3**：Q25–28 词汇配对键恰为 a/b/c/d 顺序（左右列同序），题过易；系核心继承的
  出题编排，键本身全部正确，不计缺陷。
- **O-4**：P8 答案 9.98pt 高于 9.75pt 底线但低于 11.25pt 目标（KIT §8 已记为让步 4），
  属核心设计值，不计缺陷。
- **O-5**：`Level A2/B1/B2` 英文级名保留（KIT 已裁定，沿 W46 成品）；`Sunday, Nov 22`
  为 P7 教学对照句中的英文例证。均非泄漏。

## 未做事项（明示）

- 未重跑 `render.py` / 全量 webpdf（会重写成品 PDF；SVG 层重跑 + gates 的 print/web
  文字层比对已覆盖该门；网 PDF P1 渲染目视与印版一致）。
- 未复核核心版 zh-cn 自身的全部校对记录；核心事实（除 D4/D5 同步项外）以 core proof3 (a)
  为准；D-01～D-05 的核心同源性已逐项核对（D-05 核心无；其余 4 处核心同盒标题为
  纯中文、未越盒，属 fan-out 引入）。

## 生产零写入核对

- 开工快照 `snapshot-start.txt`（41 文件）vs 收工快照：39 个真实文件（全部 .py 来源、
  SVG、PDF、text.md、KIT、ABSTRACT）**字节全同**；另有 2 个 `__pycache__/*.pyc`
  （gitignored 缓存）：我方 keycheck/regdump 导入生产 .py 时写了 5 个新 .pyc，
  清理时误删了开工已有的 bslib4/svglib 2 个 .pyc，已用同一解释器
  `py_compile` 重编恢复——新编字节与原文件 SHA 不同（原字节已无法恢复，见 GATE-LOG），
  但 .pyc 仅为 Python 导入缓存、未入 git、不属交付物，Python 下次导入即重建；
  39 个真实文件零写入已验。
