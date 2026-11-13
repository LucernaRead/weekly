# W47 nl-en 第二轮独立校对笔记（build 8 复校）

- 版：`2026-w47-nl-en`（荷兰语目标语 × 英语读者），VOL.4，刊期 2026-11-16–2026-11-22
- 校对员：第二轮独立复校（与 builder / 核心 builder / 第一轮校对员不同人；第一轮笔记见 `round1-build7/PROOF-NOTE.md`）
- 日期：2026-11-11
- 对象：印刷 PDF `De-Lucerna-VOL4-nl-en.pdf` + 网页 PDF `De-Lucerna-VOL4-nl-en-web.pdf`（build 8 = fix1 之后）
- 工作目录：只在版目录（只读）+ 本 scratch 工作；未改动任何源文件，未 commit、未 push，未跑 insert.py / lint --write
- 渲染：全部 8 版均从印刷 PDF 用 PyMuPDF 150dpi 重新渲染后目视（`print-p1.png` … `print-p8.png`），不采信 builder 的图；关键部位另有 200dpi 裁图实测

## §0 身份核验（先核身份，通过；与任务消息逐字一致）

| 文件 | 字节（实测） | SHA-256（实测） | 与任务消息 |
|---|---|---|---|
| `De-Lucerna-VOL4-nl-en.pdf`（印刷） | 12,665,899 | `2cc431f2572abad8790d1b99d6211d3aa87a5278a4052f3f0810dd6d764b0b58` | 一致 |
| `De-Lucerna-VOL4-nl-en-web.pdf`（网页） | 1,574,228 | `0fc6232bbe2bd8d3794169d83b4c233df519845f07eef1f9f35e2fdada2f6d18` | 一致 |
| `2026-w47-nl-en.text.md` | 45,074 | `1d69f5edc43e217bfa5d9e032d3c8c6666460a37ee163d0f0db18b1bebeba45b` | 一致 |

探针：`git hash-object -w --stdin` 通过（`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`）；scratch 可写验证通过；全程 `TMPDIR` 指向本 scratch 下 `tmp/`，未用系统 /tmp。creambox.py md5 `ee7a55d8b2057cf4ad42a97bb1197383` 与任务一致。

## 缺陷清单（共 2 条）

### D1 — P1 HET WOORD 框英文注文被 y=1853 通栏细线从中切断（中）
- **页/位置**：P1 右栏 `HET WOORD VAN DE WEEK`，英文注文两行（SVG `p1-voorpagina.svg`：行 1 x=1439.5, y=1846.2；行 2 x=1439.5, y=1871.85；字体 Noto Sans CJK SC 19pt）
- **原文**：`"Group win": first place in the group, straight to / the quarter-finals.`
- **现象**：一条全页宽细线 `<line x1="88" y1="1853" x2="1862" y2="1853" stroke="#d8d2c4" stroke-width="1.2"/>`（照片区底部分隔线）横穿整个注文：行 1 在线上方、行 2 在线下方，注文被线一切为二。
- **实测证据**（三法一致）：
  - SVG 几何：行 1 基线 1846.2，行 2 基线 1871.85，线 y=1853 正好位于两行基线之间。
  - 150dpi 印刷 PDF 像素扫描（注文列 x 1439–1862）：行 1 墨迹最末行 png y=2891（svg 1850.2），线为 png y=2895 单行（svg 1852.8，661 个线色像素），行 2 墨迹始于 png y=2901（svg 1856.6）。线距行 1 降部墨迹仅 ~2 svg px、距行 2 字顶仅 ~4 svg px——未压字形墨迹，但正切在两行之间，属同一段注文被分隔线剖开。
  - 核心对照：核心版同一位置注文为中文单行（基线 y=1846.2），整段注文在线上方；英文注文因较长折成两行，第 2 行掉到线下。缺陷由 fan-out 英文折行引入，非核心继承。
  - 目视：全页渲染即肉眼可见（`crop-p1-woord.png` 放大裁图：细线横贯注文两行之间）。
- **为什么 occlusion 审计漏检**：审计 LINEX 类只查线是否穿过文本节点的墨迹带（基线 −0.88em ~ +0.30em）；此线距行 1 墨迹带下缘约 0.5px、距行 2 墨迹带上缘约 2px，恰好落在两带之间的缝隙里，0 flags。属审计盲区同类（与 KIT 已修的 P7 BRIEVEN 溢出同属"英文注文变长、挤占既有版式边界"类）。
- **严重度**：中（头版"本周一词"栏目，读者一眼可见的版式缺陷；不在文字内容，纯版式）。
- **归属**：本版（fan-out）
- **修复建议**：builder 选其一：(a) 收紧荷兰语释义与英文注文之间的空隙（释义末行基线 1790.1，注文行 1 基线 1846.2，中间有约 56px 空隙），使两行注文整体上移、末行基线 ≤ ~1845，完全越过 y=1853 线；或 (b) 把英文注文缩短为一行（约 417px 内，如 `"Group win": first in the group.`，释义已含"直通四分之一决赛"之意）；或 (c) 将该通栏线下移至注文之下。修后按 SOP §8.4 整期重渲染、从头再做一轮全量校对。
- **备注**：同一缺陷在 build 7 即已存在（注文文字除弯引号外与 build 8 相同），第一轮目视记"P1 干净"时漏检；本次复校新发现。

### D2 — 网页 PDF 丢失全版唯一一处斜体：P1 «de groepswinst» 在网 PDF 中变直体（轻）
- **页/位置**：P1 `HET WOORD VAN DE WEEK` 词条 `«de groepswinst»`（印刷版 Newsreader-Italic，bbox x 1079.6–1201.8pt）
- **现象**：网页 PDF 同一 span 字体为 `LucernaNewsreader-Regular`（直体），bbox x 1079.6–1210.7pt（直体略宽）；网 PDF 全部字体清单中无任何 Italic 字体（仅 `LucernaNewsreader-Regula`、`LucernaNotoSansCJKSC-Bol/Reg`、`LucernaUnifrakturMagunti`）。SOP §1.1 规定斜体用于本周词，网版与印版不一致。
- **实测证据**：PyMuPDF span 检查：印刷版 P1 italic span 1 个（`Newsreader16pt-Italic`），全版 8 页仅此 1 个；网页版 italic span 0 个。`crop-italic-print.png`（斜体）vs `crop-italic-web.png`（直体）目视对照确认。
- **未复现的同类症状**：ru-en D3 三联症之 (1) 斜体词丢空格、(2) 闭引号脱离——本版均未出现：印/网文字层 8 页逐页位置差分 0、多重集差分 0（见 GATE-LOG），P1 原始文本 `«de groepswinst»` 前后空格与引号完整一致。仅 (3) 斜体丢失一项成立。
- **严重度**：轻（单处词条、文字内容无损、仅字形斜/直差异；但网 PDF 是入仓/读者所见版）。
- **归属**：机制（`tools/webpdf.py` 字体裁切时未带入 Newsreader-Italic 面；凡带斜体的版其网 PDF 均会同症）
- **修复建议**：webpdf.py 字体裁切白名单加入 Newsreader-Italic（与 Regular 同法裁切改名），重建网 PDF 后复验该 span 字体；修好后复查同周其他含斜体版的网 PDF 是否同症。
- **备注**：build 7 同症（webpdf.py 未变），第一轮未查字体面，漏检。

## 第一轮 D1 已核实修复

第一轮缺陷 D1（P7 BRIEVEN 注文 `Editor’s` 的 U+2019 渲染为宽字形 "Editor' s"）已修复并核实：
- 全扫：U+2018/U+2019/U+201C/U+201D/U+201A/U+201E/U+2032/U+2033 在 `content*.py`、8 个 SVG、`2026-w47-nl-en.text.md`、`ABSTRACT.txt`、印/网两 PDF 文字层中均为 **0**。
- 目视：P7 全页渲染中 `Editor's example, not a real letter. Send yours — we print them in VOL.5!` 为直撇号、无宽空隙；P1 注文 `"Group win"` 亦为直引号。

## 已核实通过的项目（本轮独立重做，非引用第一轮）

1. **150 题全量手验**（`keycheck-150.json`）：text.md 逐题解析 150/150，印刷 P8 键（`p8.py extract`）149 项逐字一致 + 第 150 题为开放写作（印刷键为 ✓ + 范文指引），**0 不一致**。手验内容：题面与正文/图表逐题复核——完成时 39–42 助动词、图表算术 83–87（35/30/65/15/100）、日期算术 22/43/44/45/46（19 天/1 天/4 小时/19 天/17 年）、判断 61–64/80–82、匹配 25–28（d/c/a/b）与 141–144（b/c/d/a）、翻译 137–140 方向与译文、造句 97–100/133–136 语序；范文实测 81 词（80–100 档；按词符计 81，破折号不计仍在档内）。逐页 10/18/18/18/18/18/12/38；级别 A2 46 / B1 73 / B2 31（与 KIT 一致）。
2. **金句 8 条**：P7 `ZINNEN VAN DE WEEK` 8 句逐字比对正文——8/8 逐字见于正文，页码标注 (Pagina 1/1/2/3/4/5/6/6) 全对，英文译文逐条核对无误。
3. **P8 compare**：`p8.py compare` vs core **CLEAN**，missing=[] extra=0，keydiff=[137, 138]——逐项裁决：137/138 核心键为中文译文（核心读者为中文，正确），本版键为英文译文（英语读者，正确），139/140 两边同为荷兰语；属翻译题合法重定向，非缺陷。附注：gates.py 打印的 "keydiffs=0" 是其正则 `[Kk]ey diff` 匹配不到 p8.py 输出格式 `keydiff=[137, 138]` 所致（见 GATE-LOG 方法备注），以直接跑的 p8.py 输出 + JSON 为准。
4. **freeze**：`freeze.py baseline` 核心重跑 **8/8** byte-identical；`freeze.py diff` 逐页差分仅讲解层增减，新增 CJK 字符共 15 个且全部为 U+3000 全角空格（分隔符，每页 1–2 个），无新增中文文本。
5. **occlusion**：自检通过（6 类阳性对照全触发），**0 flags**。但 D1 证明其对"线落两行墨迹带之间"的情形是盲的（见 D1）。
6. **creambox 全版扫描**：全部奶油框末行 clearance 均为正；P7 toolbox 3 框，最小末行 clearance +13.1、最小 desc-clear +7.1；BRIEVEN 框底 1927.5，末行基线 1899.6（+27.9），在 ZINNEN 规则线（y=1937）上方 9.5px——KIT 所称修复有效。两处须裁决的窄带：(i) P2 EN JIJ 框末行 clearance +5.6、desc-clear −0.4——末行 `"Dutch and send them to the editors."` 无任何降部字母（g/j/p/q/y 皆无），真墨迹不超框底（目视框内留白清晰），为 0.30 统一余量造成的假阳性；(ii) P5 EN JIJ 框末行 clearance +6.3、desc-clear +0.3——末行 `"them in."` 同样无降部字母，目视干净。P1 IN DEZE EDITIE 框下方 +24px 的 `HET WOORD VAN DE WEEK` 标题与 P2 四词框下方 +32px 的 `Let op:` 均为框外下一标题/说明，非溢出。P6 图表框末行 `"people)"`（含降部 p）desc-clear +3.2 为正。
7. **框标题逐个实测**：occlusion BOXTITLE 类 0 flags；另用 PyMuPDF span 三法核 P1：横幅 `VANAVOND IN BERLIJN!` bbox x 88.5–489pt、副标题 `Tonight in Berlin: Netherlands vs Germany` x 953–1376pt、头条 `Vanavond in Berlijn: Oranje tegen Duitsland` x 66–929.6pt、数字框题 `DE WEEK IN CIJFERS` x 417.4–589.5pt，均在版心内；P2 `ZO ONTHOUD JE HET`、P6 `DE GRAFIEK` 亦无溢出。必查项 (a) 未复现。
8. **P3/P5 右栏末行降部**：必查项 (b) 未复现——P3/P5 右栏框末行 desc-clear 均为正（P3 +9.8，P5 +44.3/+45.6），目视无漫出。
9. **弯引号**：见上，全扫 0（第一轮 D1 已修好）。
10. **P8 最小字号实测**：PyMuPDF 取 P8 答案区（y>1040pt）：最小 **10.12pt**（162 个 span；另 10.5pt×7、12.75pt×6），中位数 10.12pt ≥ SOP §1.1 下限 9.75pt——与 KIT 登记一致（本轮实测，非引用 KIT 数字）。
11. **印/网文字层**：8 页 span 数逐页相等（218/203/189/184/196/201/188/386），多重集差分 0、位置差分（容差 2pt）0；pdftotext 印 45,404 B / 网 45,409 B，均 > 0；网 PDF 1,574,228 B < 7 MB。唯 D2 斜体面丢失（文字内容无损）。
12. **E 节 type 标签本地化**：必查项 (d) 未复现——137/138 标签 `[Translate into English]`、139/140 `[Translate into Dutch]`，均为英语，无中文「翻譯」残留。text.md CJK 仅 `答案`×150 + 全角标点 `：（）`×142 + U+3000×59，无其他中文。
13. **讲解层语言**：全部讲解/导读/题干说明/答案注文均为英文；荷兰语仅为目标语正文/题面。P8 顶栏 `Page 8　De grote toets van de week + alle antwoorden` 的荷兰语副标题未翻英文——与核心（`第8版　De grote toets…`）同为 tables.py 家具，不计缺陷（见 O8）。
14. **事实与日期星期（公开来源，本轮独立重验；与第一轮结论一致）**：
    - 全部日期星期：1 Nov 2026 周日、13 Nov 周五、14 Nov 周六、15 Nov 周日、16 Nov 周一、21 Nov 周六、22 Nov 周日、5 Dec 周六、24 Nov 周二、29 Nov 周日——与文中全部表述一致。
    - Nations League A2 组（MD4 后）：荷兰 8 分（7:5）、希腊 8 分（5:3）、德国 5 分（3:2）、塞尔维亚 0 分（3:8）；荷兰四场 1–1 德国（主）、2–1 塞尔维亚（客）、2–2 希腊（客）、2–1 塞尔维亚（主）；德国 0–1 负希腊（主）、2–0 胜塞尔维亚、0–0 平希腊（客）；MD5 11 月 13 日周五 荷兰–希腊 + 塞尔维亚–德国（贝尔格莱德）；MD6 11 月 16 日周一 德国–荷兰（柏林 Olympiastadion，20:45 CET）——与 UEFA 赛程/多家比分源一致。**KIT §8 所列核心核验债（德国/周五比分）至此全部核实无误。**
    - Eredivisie 第 12 轮：Heerenveen–Feyenoord 5–3、Twente–Ajax 2–2、Cambuur–PSV 2–5（均为 11 月 8 日）；PSV 12 轮 26 分榜首（Feyenoord/Ajax 25，Twente 24）——Q63/Q126 的"26 分"核实无误。第 13 轮 NEC–PSV 周六 16:30 CET、Feyenoord–Excelsior 周六 18:45 CET、Twente–Willem II 周日 12:15 CET、Ajax–ADO 周日 14:30 CET——与 KNVB 赛程一致（数据源常标 UTC，+1 小时即 CET，与文中一致）。
    - Sinterklaas：全国 intocht 2026 年 11 月 14 日周六 Grave（Maaskade 约 12:00 靠岸，节目 12:00–16:00，NPO Zapp/NPO 3 直播，Merel Westrik 主持，市长 Marieke Moorman 迎接）；阿姆斯特丹 11 月 15 日周日第 88 届（De Omval 10:15、Scheepvaartmuseum 约 11:30、Stopera 13:00 起步、经 Rembrandtplein/Utrechtsestraat 至 Leidseplein）——与组织方时刻表及多家媒体一致（10:15 到达/出发措辞见 O3）。
    - Expeditie Robinson 2026：19 名选手（10 荷 + 9 弗拉芒）、马来西亚、34 天、11 月 1 日周日 20:00 RTL 4 首播、Nicolette Kluijver + Edson da Graça 主持、Camille Vanuxem 任记者——与多家荷兰媒体一致。
    - Heel Nederland Leest 2026 书为 Herman Koch《Het diner》（2009 年初版）；下期预告 11 月 24 日周二 Real Madrid–PSV、Feyenoord–FC Porto（欧冠第 5 轮，20:00 UTC），11 月 29 日周日 Feyenoord–Ajax——与 UEFA.com 赛程一致。
15. **版面目视**：P1–P8 逐版目视——除 D1 外无溢出/重叠/压线/压页脚；P8 练习 113–150 连续、答案 1–150 齐全；照片 7 张 + P6 图表均带出处；§1.1 调色板门通过（gates.py s11：off-palette {}、无金色、描边矩形 0、VOL.5=5=core、纸色填充 8）。P7 VOLGENDE WEEK (VOL.5) 两行完整；P8 顶栏、页脚 `Page N of 8` 齐全。
16. **禁词/红线**：沿用第一轮扫描结论（Oekraïne/Ukraine/战争类词 0；"NAVO" 仅 `VANAVOND` 内子串假阳性）；无国际政治；目标国国内政治仅体现为体育赛事（红线允许）。
17. **VOL 与头条**：VOL.4（印刷文字层 ×10：每页页脚 + P1 刊头区 2 处）；VOL.5 ×5，与核心一致；头条去空白 38 字符 ≤ 56。ABSTRACT.txt 为英语单行，含刊名/目标语/A2–B2/150 题，事实取自本期。

## 观察项（不计缺陷）

- **O1**：P2 D 组匹配题 c 项 `c. eten voor het paard van Sinterklaas` 超出右栏家具边约 8.6pt——印 PDF span x1=1406.3pt（同栏 a/d 行分别为 1325.4/1357.6pt），200dpi 像素实测最右墨迹 1405.1pt；**核心版同一行同一位置亦然**（span x1=1406.3pt、像素 1405.1pt，逐值相同），为核心继承的版式，与 fan-out 无关；右方为空白边距（距页边仍有 56pt），无碰撞、无压线。目视见 `crop-p2-match.png`。
- **O2**：KIT §7 登记的 P7 token 数 "935" 与实测不符（实测 915；第一轮 O1 延续，KIT 记录笔误，非成品问题）。
- **O3**：P3 阿姆斯特丹 intocht："de boot vertrok om 10:15 uur bij De Omval"；组织方时刻表记 10:15 为到达 De Omval 的时间，离港约 10:30（另一来源），各家表述不一且组织方自称 "richttijden"。属 KIT §8 已登记的核心核验债范畴（第一轮 O3 延续），不作新缺陷。
- **O4**：P1 moth 标记 SVG 源码内含 `<title>Lucerna 三色蛾</title>`（核心继承；印刷文字层无此串、读者不可见）。第一轮 O4 延续。
- **O5**：`svglib.py` 代码注释中含 "包裹" 二字，非渲染文本。第一轮 O5 延续。
- **O6**：P5 照片署名 "Elise Iovenko / Unsplash — CC0" 未独立核验（本轮检索 "Elise Iovenko Unsplash" 无确认结果亦无反证；与核心逐字相同，核心 KIT §5 记图片授权已验）。第一轮 O6 延续，列此备查。
- **O7**：P7 金句 #5 英文译文 "The Netherlands are first because they scored more goals…" 用复数 are（英式球队复数），可接受。第一轮 O7 延续。
- **O8**：P8 顶栏副标题 `De grote toets van de week + alle antwoorden` 为荷兰语、无英文注文；核心同一位置为 `第8版　De grote toets…`（读者语页码 + 荷兰语副标题），同为 tables.py 家具，非 fan-out 缺失。
- **O9**：`2026-w47-nl-en.text.md` 首行标题含 `2026-W47` 周次码；核心 text.md 首行同模板（`荷兰语周报 VOL.4 · 2026-W47`），为全版通用导出格式，非本版新增。
- **O10**：方法备注——`tools/freeze.py` 只有 `baseline`/`diff` 两个子命令，无 `freeze_direct` 子命令；本轮以 baseline 8/8 + diff 完成冻结门，不作缺陷。
- **O11**：gates.py 的 `p8_compare` 门打印 "keydiffs=0" 是其正则 `[Kk]ey diff`（要求空格）匹配不到 p8.py 输出 `keydiff=[137, 138]` 所致；直接跑的 p8.py 输出 + `p8-compare.json` 为准（CLEAN，keydiff=[137,138]，已裁决为合法重定向）。建议修 gates.py 的正则（`keydiff` 不带空格亦计）。
- **O12**：KIT §8 核心核验债（德国/周五比分；官方时刻表之外的到场细节）——本轮已全部独立核实无误（见上 §14），可销账；唯 O3 的 10:15 措辞仍留组织方"richttijden"口径。

## 结论

**(b) 缺陷清单：2 条（D1 中、D2 轻）。本轮不是零问题，不能定稿。**

D1、D2 均须改源码/工具后重渲染，从头再做一轮全量校对，直至一整轮零问题。修复不在本轮校对员权限内（只检查、不改成品），请协调员派 builder 处理：D1 缩短或上移 P1 注文（或下移通栏线）；D2 修 webpdf.py 字体裁切带入 Newsreader-Italic。
