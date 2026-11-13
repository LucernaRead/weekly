# W47 nl-en 第一轮独立校对笔记（叶子）

- 版：`2026-w47-nl-en`（荷兰语目标语 × 英语读者），VOL.4，刊期 2026-11-16–2026-11-22
- 校对员：叶子（第一轮独立复校，与 builder / 核心 builder / 其他轮次不同人）
- 日期：2026-11-11（校对时区 Europe/Amsterdam 事实核验；`date` 核验用该时区）
- 对象：印刷 PDF `De-Lucerna-VOL4-nl-en.pdf` + 网页 PDF `De-Lucerna-VOL4-nl-en-web.pdf`
- 工作目录：`~/workspace/weekly-git`（只读本版目录与 `scratch-fanout-nl/`；未碰 core-nl、W43–W46、其他目标语、tools/；未跑 insert.py / lint --write；无任何 git 写操作）
- 渲染：全部 8 版均从印刷 PDF 用 `pdftoppm -r 100` 重新渲染后目视（`render/p-*.png`），不采信 builder 的图；网页 P1/P8 从网页 PDF 同法渲染目视（`render/w-1.png`、`render/w-8.png`）

## 身份核验（先核身份，通过）

| 文件 | 字节 | SHA-256（实测完整串） | 与 KIT 登记 |
|---|---|---|---|
| `De-Lucerna-VOL4-nl-en.pdf`（印刷） | 12,690,133 | `0b4dc8c0e19b72a0d753842bdec7775064481a0b4b37bb88f66fa4aa5199f2e7` | 逐字一致 |
| `De-Lucerna-VOL4-nl-en-web.pdf`（网页） | 1,576,939 | `477dd85dc87cda7ffa5ff71a5e5b15a5dcc33ff3db8d2ed49a8654f8a2cb8de6` | 逐字一致 |

身份相符后才开始复校。

## 缺陷清单（共 1 条）

### D1 — P7 BRIEVEN 框英文注文：弯撇号 U+2019 渲染为宽字形，呈 "Editor' s"（可见错字）
- **页/位置**：P7 右栏 `BRIEVEN VAN LEZERS` 框内英文注文第 2 行（SVG `p7-taal.svg` 文本节点 x=1461.5, y=1871.17；字体 Noto Sans CJK SC 20pt）
- **原文（SVG 源码）**：`Editor’s example, not a real letter. Send yours — we print them in VOL.5!`（撇号为 U+2019）
- **应为**：`Editor's example, not a real letter. Send yours — we print them in VOL.5!`（撇号为 U+0027，与本版其余全部撇号一致）
- **证据**：
  - 8 个 SVG 全扫：U+2019 总数 = **1**，仅此一处（其余撇号均为 U+0027，如 P1 `Oranje's`、`Sinterklaas's`、`THIS WEEK'S`，P8 `St Martin's Day`、`Sinterklaas's horse`）。
  - 印刷 PDF 文字层 U+2019 计数 = 1；`.text.md` U+2019 计数 = 1（同句，第 366 行）。
  - 目视：从印刷 PDF 重渲染的 P7 放大裁图（`render/p7-editors-crop.png`、`render/p7-brieven-crop.png`）清楚显示 `Editor’  s example`——撇号占一整字宽、与 s 之间有明显空隙，读作错字 "Editor' s"。
  - 该句是 fan-out 新写的英文注文（核心版同一位置为中文注文），缺陷由 fan-out 引入，非核心继承。
- **严重度**：中（可见错字，位于读者园地英文注文；单字符修复；按 SOP §8.4 须改源码重渲染后从头再做一轮全量校对，本版现状不能算零问题定稿）

## 已核实通过的项目（抽查方法与结果）

1. **150 题全量验算**：逐页题数 10/18/18/18/18/18/12/38（P1 1–10，P2 11–28，P3 29–46，P4 47–64，P5 65–82，P6 83–100，P7 101–112，P8 113–150）；级别 A2 46 / B1 73 / B2 31（按 SVG 徽章 + `.text.md` 级别标记独立重数，与 KIT 一致，F 组 141–144 共用一枚 B2 徽章已计入）。P8 答案 150/150 齐全（`p8.py extract`），`compare` vs core CLEAN、0 key diff。全部答案逐题对照题面/正文/图表复核：完成时助动词 39–42（is aangekomen / heeft ontvangen / is gevaren / hebben gelezen）、图表算术 83–87（35/30/65/15/100，相加 35+30+20+15=100）、日期算术 22/43/44/45/46（19 天/1 天/4 小时/19 天/17 年）、判断题 61–64/80–82 均与正文一致。范文 81 词（80–100 档，以源码实测 81 词，与 P8 注 "81 words" 一致）。
2. **金句 8 条**：P7 `ZINNEN VAN DE WEEK` 8 句逐字比对正文——8/8 逐字出现在正文 SVG 与 `.text.md` 中；页码标注 (Pagina 1/1/2/3/4/5/6/6) 逐条核对与句子实际所在页一致；英文译文 8 条逐条核对无误。
3. **禁词/红线**：印刷全文扫描：Oekraïne/Ukraine/oorlog/Trump/Amerika/Poetin/Rusland/Gaza/Israël 均为 0；"NAVO" 命中 1 次是 `VANAVOND` 一词内的子串假阳性（"vanavond" 今晚），非北约内容。无国际政治；目标国国内政治仅体现为体育赛事（Nations League，红线允许）。内部词 SOP/cover/W47/lint/TODO/placeholder/Lorem/FIXME/XXX 全文 0。
4. **VOL 与头条**：VOL.4（印刷文字层 ×10：每页页脚 + P1 刊头区 2 处）；VOL.5 ×5，与核心一致（ gates s11 门 VOL.5=5=core）。头条 `Vanavond in Berlijn: Oranje tegen Duitsland` 去空白 38 字符 ≤ 56。ABSTRACT.txt 为英语单行 271 字节，无 ASCII 双引号，含刊名/目标语/A2–B2/150 题，事实取自本期。
5. **翻译层专项**：
   - 讲解/界面语言全为英文（刊头、栏目条、Note 框、题干说明、P8 答案注文均为英文；荷兰语仅为目标语正文/题面）。
   - CJK 机制核实：核心 `cjk-literals.json` 共 243 条中文源语字面量；在 en 版源码中逐条核查——**0 条残留**（`content*.py` 的 CJK 字符数为 0；`svglib.py` 的 2 个汉字 "包裹" 仅出现在代码注释里，非渲染文本）。印刷 PDF 文字层 CJK 字符 0；`.text.md` 的 CJK 仅 `答案`×150（300 字）；8 个 SVG 的 CJK 仅 P1 moth 标记 `<title>Lucerna 三色蛾</title>` 内 3 字（见观察项 O4）。
   - E 组：137/138 为荷兰语→英语（答案键为英文："The Sinterklaas news is on every day at 18:00." / "The top two go through to the quarter-finals."），139/140 为英语→荷兰语（答案键为荷兰语），方向正确。
   - `svglib.py` 注释外的中文残留：无。
6. **U+2019 回归扫查**：见 D1（总数 1，不为 0）。除 D1 外，含撇号的行目视无宽字形断裂。
7. **P8 注文人名逐条人工核对（公开来源）**：P8 答案注文与题面中出现的人名/专名——Herman Koch（《Het diner》2009，Heel Nederland Leest 2026  campaign book，多家荷兰图书馆/维基证实）、Merel Westrik（Sinterklaasjournaal/intocht 主持，NTR 通稿与多家媒体证实）、Marieke Moorman（Land van Cuijk 市长、在 Grave 迎接 Sinterklaas，多家来源证实）、Ozosnel（Sinterklaas 的马，ozosnel.nl 及 intocht 报道证实）、Nicolette Kluijver / Edson da Graça（Expeditie Robinson 2026 主持）、Camille Vanuxem（弗拉芒记者，2026 年新加入）、Daan（P8 阅读短文虚构人物，非真人）、Wim van Rossem / W. Punt（Anefo 照片署名）、Aaron Burden / Cristina Gottardi（Unsplash 照片署名）。**拼写全部正确，无 ja 家庭相扑力士式错误。**P5 照片署名 "Elise Iovenko / Unsplash" 未独立核验（见观察项 O6）。
8. **事实与日期星期（公开来源核验）**：
   - 全部日期星期用 `date` 核验：1 Nov 2026 周日、13 Nov 周五、14 Nov 周六、15 Nov 周日、16 Nov 周一、21 Nov 周六、22 Nov 周日、5 Dec 周六、24 Nov 周二、29 Nov 周日——与文中全部星期表述一致。
   - Nations League A2 组：荷兰 8 分（7:5）、希腊 8 分（5:3）、德国 5 分、塞尔维亚 0 分；荷兰四场 1–1 德国（主）、2–1 塞尔维亚（客）、2–2 希腊（客）、2–1 塞尔维亚（主）；德国 0–1 负希腊（主）、2–0 胜塞尔维亚、0–0 平希腊（客）；11 月 13 日周五 荷兰–希腊（阿姆斯特丹 Johan Cruijff ArenA）+ 塞尔维亚–德国（贝尔格莱德）；11 月 16 日周一 德国–荷兰（柏林 Olympiastadion，20:45）——与 sportradar / UEFA 赛程 / 多家荷德媒体一致。**KIT §8 所列核心核验债（德国/周五比分）至此全部核实无误。**
   - Eredivisie 第 12 轮：Heerenveen–Feyenoord 5–3、Twente–Ajax 2–2、Cambuur–PSV 2–5；PSV 12 轮 26 分榜首（Feyenoord/Ajax 25，Twente 24）——与 FR12 / soccernews / 1908 / KNVB 赛程一致；第 13 轮 NEC–PSV 周六 16:30、Feyenoord–Excelsior 周六 18:45、Twente–Willem II 周日 12:15、Ajax–ADO 周日 14:30——与 KNVB 官方赛程一致。
   - Sinterklaas：全国 intocht 2026 年 11 月 14 日周六 Grave（Maaskade 约 12:00 靠岸，节目 12:00–16:00，NPO Zapp/NPO 3 直播）；阿姆斯特丹 11 月 15 日周日第 88 届（De Omval 10:15、Scheepvaartmuseum 11:30、Stopera 13:00 起步、经 Rembrandtplein/Utrechtsestraat 至 Leidseplein）——与组织方时刻表及多家媒体一致（"10:15 出发/到达" 的措辞见观察项 O3）。
   - Expeditie Robinson 2026：19 名选手（10 荷 + 9 弗拉芒）、马来西亚（兰卡威）、34 天、11 月 1 日周日 20:00 RTL 4 首播、Nicolette Kluijver + Edson da Graça 主持、Camille Vanuxem 任记者——与 nl/en 维基及多家荷兰媒体一致。
   - Heel Nederland Leest 2026：书为 Herman Koch《Het diner》（2009），11 月全月图书馆免费取（含简易读本/大字本/电子书/有声书）——与 CPNB 活动及多家图书馆来源一致。
   - 下期预告（P7 VOLGENDE WEEK）：11 月 24 日周二 Real Madrid–PSV、Feyenoord–FC Porto（欧冠第 5 轮），11 月 29 日周日 Feyenoord–Ajax 14:30（De Klassieker）——与 UEFA.com 及多家媒体一致。
9. **版面目视**：P1–P8 逐版目视——P1 副标题/数字框/P6 图表头/P2 `ZO ONTHOUD JE HET REMEMBER` 框、P7 BRIEVEN 框（底边在 ZINNEN 规则线上方，修复有效）均无溢出/重叠/压线；P8 练习 113–150 连续、答案 1–150 齐全；P8 答案区实测最小字号 10.12pt ≥ 9.75pt（中位数亦 10.12pt）；徽章逐页计数与级别分布一致（见上）；照片 7 张 + P6 图表均带出处/授权标注；§1.1 调色板门通过（无金色、无描边矩形、纸色 8 处）。
10. **网页 PDF**：P1/P8 目视与印刷版一致；文字层逐页位置差分 0、多重集差分 0（见机械门）。
11. **P1 栏断句核查**：P1 第 1 栏末 "…aan de Maas in" 在第 2 栏顶以 "Noord-Brabant: rond 12:00 uur…" 续接，非截断句（`.text.md` 第 9 行全文一致）。

## 观察项（不计缺陷）

- **O1**：KIT §7 登记的 P7 token 数 "935" 与实测不符：我重跑的 print/web 文字层为 P7 795/830/738/724/807/748/**915**/2318（builder 自己的 `en-gates7.log` 亦为 915）。双 PDF SHA 与 KIT 一致、文字层逐页差分 0，属 KIT 记录笔误，非成品问题。
- **O2**：builder 记录 `en.md` 与最终 build 7 不一致两处（`.text.md` 记 45,187 B，实测 45,080 B 与 KIT 一致；BRIEVEN 英文注文记 "No real letters yet — so, an example."，实测 SVG 为 "No letters yet — an example; VOL.5 next." 与 KIT 一致；pdftotext 亦记 build 6 的 45,517/45,522 B，实测 45,410/45,415 B）。均为记录滞后，非成品问题。
- **O3**：P3 阿姆斯特丹 intocht："de boot vertrok om 10:15 uur bij De Omval"；组织方时刻表记 10:15 为到达 De Omval 的时间，离港约 10:30（另一来源），各家对 10:15/10:30 表述不一且组织方自称 "richttijden"。属 KIT §8 已登记的核心核验债（"arrival details beyond the official schedule"）范畴，不作新缺陷。
- **O4**：P1 moth 标记 SVG 源码内含 `<title>Lucerna 三色蛾</title>`（核心继承，`cjk-literals.json` 243 条之外；印刷文字层无此串、不可见）。非读者可见内容，不计缺陷。
- **O5**：`svglib.py` 第 203 行代码注释中含 "包裹" 二字（U+3000 探针回归注释），非渲染文本。
- **O6**：P5 照片署名 "Elise Iovenko / Unsplash — CC0" 未独立核验（无反证，列此备查）。
- **O7**：P7 金句 #5 英文译文 "The Netherlands are first because they scored more goals…" 用复数 are（英式球队复数），可接受。

## 机械门结果（自跑，tools/venv 解释器）

详见 `GATE-LOG.md`（本次重跑完整日志：`gates-rerun.log`）。结论：**9 门全过**。

| 门 | 结果 |
|---|---|
| occlusion（`tools/occlusion_audit.py svg/`） | 0 flags，rc=0 |
| p8 extract（`p8.py extract --total 150`） | 150/150 |
| p8 compare vs core（`p8.py compare`） | CLEAN，0 key diffs |
| freeze（clean-dir 重跑 `run.py`，8 SVG 直接 sha256） | 8/8 MATCH，run.py rc=0，TOTAL 150；`en-build7.log` 中 OVERFLOW/TOO WIDE/WARNING 计数 0 |
| print/web 文字层（PyMuPDF 位置排序） | 8 页 posdiff 0 / msdiff 0（tokens 795/830/738/724/807/748/915/2318） |
| pdftotext 非空 | print 45,410 B / web 45,415 B；web PDF 1,576,939 B < 7 MB |
| P8 答案字号 | 最小 10.12pt，中位数 10.12pt（≥ 9.75pt） |
| P8 徽章 vs core | A2 8 / B1 24 / B2 3，两边一致 |
| §1.1 SVG 审计 | off-palette {}，无金色，描边矩形 0，VOL.5=5（core 5），纸色填充 8 |

## 结论

**(b) 缺陷清单：1 条（D1）。本轮不是零问题，不能定稿。**

D1 为单字符修复（P7 注文 `Editor’s` 的 U+2019 → U+0027），修复后须按 SOP §8.4 改构建源码、整期重渲染、从头再做一轮全量校对，直至一整轮零问题。修复本身不在本轮校对员权限内（只检查、不改成品），请协调员派 builder 处理。
