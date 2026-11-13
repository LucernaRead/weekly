# PROOF-NOTE — 2026-W47 it-ja（proof1，独立复校）

- 复校员：proof1（只读复校，未修版、未 commit、未 push、未派 subagent）
- 复校对象：`~/workspace/weekly-git/production/2026-w47/2026-w47-it-ja/`
- 复校时间：2026-11-11
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-it-ja1/`
- 先读：SOP.md §1.1/§8/§9 全文、repo AGENTS.md、协调员 brief、该版 WEEKLY-KIT.md 全文——已读。
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` rc=0；scratch 内真实写文件成功。`TMPDIR=<scratch>/tmp` 全程，未写 /tmp。

## 0. SHA 核对（开工前，先核对三件）

| 件 | 盘上大小 | 盘上 sha256 | KIT §7 登记 | 结论 |
|---|---|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-JA.pdf` | 28,221,078 B | `f0fb8a83671a4d7bfee852436c907b6372a7631be92a7ef4725f2154d0e97220` | 同左 | 一致 |
| 网页 PDF `La-Lucerna-VOL4-JA-web.pdf` | 1,869,651 B | `b6660f12a4d57833139ba6a80a7d4fc2cd033f308ed3cf35fa36bfacdaf72cf3` | 同左 | 一致 |
| 文本导出 `2026-w47-it-ja.text.md` | 58,239 B | `87d1ec4e54d7dcaecac7028bd745aa7483978235425ae756157da6da6bd686f5` | 同左 | 一致 |

印刷 PDF 8 页，版面 1462.5×2025 pt（与 KIT 一致）。

## 1. 门禁实测（本人重跑，非只引 KIT）

| 门禁 | 命令/方法 | 结果 |
|---|---|---|
| p8 compare | `tools/p8.py compare --core-p8 production/2026-w47/core-it/svg/p8-valutazione.svg --edition-p8 production/2026-w47/2026-w47-it-ja/svg/p8-valutazione.svg --total 150` | **CLEAN**，150/150 noted，keydiff=[137,138,139]（重定向的读者句，预期内） |
| occlusion audit | `tools/occlusion_audit.py <svg dir>`，自检先过 | 自检 6 类阳性全触发；**0 flags** |
| creambox（canonical） | `hidden_files/w47/tools/creambox.py`（+45px 窗口 + 逐行表 + P7 汇总），8 个 SVG 逐个传参 | 全部盒内末行基线 clearance ≥ +4.5 px；见 §2 逐项裁定 |
| freeze diff | `tools/freeze.py diff --core production/2026-w47/core-it/svg --edition …/2026-w47-it-ja/svg` | rc=0；P1–P7 增减串数与 KIT 一致；新增 CJK 3,054 字，抽查均为日语讲解层字符（假名/汉字/、。・〜：）；碎片级“无未解释”裁定见 builder `gates2.log`（`unexplained_add=[] unexplained_rem=[]`，含 adjacent-pair 规则） |
| freeze baseline（正确用法） | `tools/freeze.py baseline --build production/2026-w47/core-it --core-svg production/2026-w47/core-it/svg --out <scratch>/freeze-baseline-core` | **8/8 byte-identical**，rc=0；core SVG 在运行中未被改动（工具自验）。见观察 O1 |
| 印刷/网页 text layer | `pdftotext -layout` 两版 + 词/字符多重集比对 | 各 6,760 词，**词多重集相等、字符多重集相等**，tofu（U+FFFD）0；网页 PDF 1,869,651 B < 7 MB |
| P8 最小字号（渲染实测） | PyMuPDF 读印刷 PDF 全部 span | **P8 最小 9.75 pt**（= SOP §1.1 让步 4 的下限，13.0 SVG px）；P1–P5/P7 最小 11.62 pt，P6 最小 12.75 pt |
| BOXTITLE 真墨迹 | occlusion audit BOXTITLE 类（真墨迹盒）0 flags + 本人对最长标题做 PDF span 实测 | 最长标题右缘余量均 ≥ 626 pt（P6 `LE MINIME DI ESEMPIO … (DATI INVENTATI PER L'ESERCIZIO)` 行 x1=835.9/1462.5 pt；P7 `FRASI DELLA SETTIMANA`、P8 `VALUTAZIONE E RISPOSTE` 均远离右缘）——无漫出 |
| abutting / keycheck | tools/ 内无名为 abutting/keycheck 的独立工具；以 occlusion TEXTX（文本-文本重叠）0 flags + 8 页目视 + scratch `gates.py` 150-key 审计（`gates2.log` 全 PASS）+ 本人 150 键逐题语义核对代替 | TEXTX 0 flags；150 键语义核对全部通过（见 §3） |
| 编号/级别 | 文本导出正则计数 | 练习题干 138 单题 + 3 组匹配题（25–28、52–55、141–144）×4 = **150 题连续无缺重**；答案区编号 1–150 连续；级别 A2 47 / B1 70 / B2 33（与 KIT 一致：匹配组每组 1 个标签计 4 题） |
| abstract（SOP §9） | 读 `ABSTRACT.txt` | 1 行（161 字）、无 ASCII 双引号、含刊名 La Lucerna、目标语名イタリア語、A2–B2、150問、真实主题（セリエA第11節、トッローネ祭、ユーロチョコレート、聖母健康祭、植樹の日、ブックシティ、トリノ映画祭、予算案）——通过 |
| 禁词扫描 | `grep -c "Ucraina\|Russia\|Putin"` 文本导出 | **0** |
| 日期/星期 | `date`（Europe/Rome）逐日核验 | 11-07 六、11-12 四、11-15 日、11-16 一、11-17 二、11-19 四、11-20 五、11-21 六、11-22 日、11-23 一、11-24 二、11-29 日、12-02 三、12-06 日——文中全部星期表述一致 |
| 模范文词数 | 人工逐词数 P8 Testo modello | **99 词**（与 KIT 一致，80–100 词区间内） |
| P7 金句 8 条 | 文本导出全文计数 | 每条恰好出现 **2 次**（正文 1 次 + P7 1 次），逐字一致，页码标注（P1/P1/P2/P3/P4/P5/P6/P6）全部正确 |

## 2. 版式几何（8 页印刷 PDF 逐页目视 + 工具）

8 页已从印刷 PDF 渲染（100 dpi）逐页看完：无溢出、无重叠、无压页脚、无豆腐块、无横向漫出、无图片与出处错位。creambox 逐盒裁定：

- 全部盒内末行基线 clearance ≥ +4.5 px。7 处 desc-clear 为负（−1.0 ~ −1.5，P2 LO SAPEVI?/E TU?、P3 IL WEEKEND DOLCE/E TU?、P4 E TU?、P5 I GIOVANI IN NUMERI/E TU?、P7 LA PAROLA/LETTERE）——逐行核查末行文字：**均不含下行字母**（日语句或 `della musica e dei musicisti.` / `continua fino al 6 dicembre.` 等无 g/j/p/q/y 的意大利语句），负值只是 0.30em 通用余量，非真实墨迹漫出；P7 三个工具盒目视确认末行在盒内留有空隙。**不是缺陷。**
- 4 处“盒下 +45px 窗口内有行”（P1 IN QUESTO NUMERO 下的 `LA PAROLA DELLA SETTIMANA`、P3 解説盒下的 `IL TORRAZZO E IL TORRONE`、P4 结果表行带、P6 MINIME/PROPOSTA 盒下的 `ESERCIZI` 栏头）——均为盒外下一区块的栏头/下一行，目视确认不重叠，是已知假阳性形态。**不是缺陷。**
- P7 工具盒实测盒底清除量：ERRORI TIPICI 末行基线 +18.1 px（desc +12.2）；LA PAROLA +4.5 px（desc −1.5，日语末行）；LETTERE +5.1 px（desc −0.9，日语末行）。三盒末行均在盒内，目视确认。
- P8 RISPOSTE 末行（150. ✓ 模範文…）在页脚线上方，flow 末端 2546/2552（KIT 称 6 px 余量，确定性流程）——目视确认无侵入页脚。
- P1 masthead 带起于 x=102.3，两侧边距干净；moth 处的 リ 目视完整（旧审计的假报已由工具修复版排除）。
- P4 E TU 盒底与表头齐平（1140.45 = core）；P4 结果表 5 行带交替底色对齐，无错行。

## 3. 内容事实（公开来源逐项核对，非只信 KIT）

全部核实通过（来源为 2026-11-09~11-11 的意/英/法媒报道与官方口径）：

- **Serie A 第 11 节**：10 场比分（Venezia–Udinese 2–1、Cagliari–Frosinone 1–0、Torino–Lecce 1–1、Parma–Bologna 1–2、Roma–Sassuolo 3–0、Napoli–Lazio 1–1、Genoa–Milan 1–2、Monza–Atalanta 0–1、Inter–Como 2–0、Fiorentina–Juventus 2–2）**逐场一致**；24 球；积分 Lazio 29、Inter 28、Roma 27、Milan 24、Como 23、Fiorentina 9、Udinese 5 垫底；Gattuso 为 Lazio 主帅；Roma 最多进球 31 球；第 12 节 11-21~23，Lazio–Lecce 周六 15:00、Atalanta–Inter 周日 20:45 Bergamo、Monza–Fiorentina 周一收官。✓
- **Nitto ATP Finals**：11-15~22 都灵 Inalpi Arena，8 人、Zverev 世界第一、Alcaraz、Cobolli 首次参赛、Sinner 为 2025 冠军因膝伤缺席。✓
- **Nations League**：意大利–法国 11-12 周四 20:45 San Siro、比利时–意大利 11-15 周日 20:45 布鲁塞尔；主帅 Mancini；文中未印赛果、推迟至 VOL.5，与事实一致。✓
- **Festa del Torrone**：第 29 届 11-07~22，主题「Il Confine」，16 天、三周末；Torrone d'Oro 11-22 11:00 Palatorrone 授予 Davide Simonetta（Cremona 出生）；corteo 16:00、150 人以上文艺复兴服装、Sforza–Visconti 婚礼重演 17:00、旗手与火舞至 18:00、终场「Il torrone va in brodo」18:00；1441 年婚礼传说。✓
- **Eurochocolate**：第 32 届 11-13~22，主题「Fate Dolci」；Calabria 首个「Regione Ospite」（bergamotto、cedro、peperoncino、fichi）；「I tesori della Calabria Straordinaria」11-20 周五 18:15；Iginio Massari 11-22 闭幕嘉宾。✓
- **Alba 白松露集市**：第 96 届 10-10~12-06。✓
- **Madonna della Salute**：11-21，1630 年瘟疫之誓（10-22），Longhena 设计、1631 年动工、1687-11-21 祝圣；奉纳桥（船桥）横跨大运河；castradina（盐渍烟熏羊肉配 verze）。✓
- **植树日**：11-21，1898 年首届 Festa dell'albero（Baccelli），2013 年第 10 号法律定为 Giornata nazionale degli alberi。✓
- **BookCity Milano**：第 15 届 11-23~29，主题「Il senno sulla Luna」（Ariosto《Orlando furioso》），1,360 活动、2,487 嘉宾、1,164 本书、443 会场；开幕 11-23 周一 20:00 Teatro Dal Verme，Colson Whitehead（两届 Pulitzer）；预览 Edmund de Waal 11-22 周日 16:00 Fondazione Rovati。✓
- **Torino Film Festival**：第 44 届 11-24 周二~12-02 周三，共 9 天（官方规章）。✓
- **Manovra 2027**：DPB 10-15 送布鲁塞尔；2027 增长 +0.8%、赤字 3.4%（DPB 规划值）；法案 10-28 内阁通过、约 260 亿欧元（多家意媒口径）；编号 C. 3174-bis；听证会 11-09~12（Giorgetti 周四 12 日）；修正案截止 11-17 周二 18:00；须 12-31 前终审；Irpef 第二档 33% 由 50,000 扩至 55,000 欧元；金融业约 50 亿财源；卫生 +34 亿。文中三处「PROPOSTA ≠ LEGGE」披露完整。✓
- **日历/算术**：Torrone 16 天、Eurochocolate 10 天、BookCity 7 天、TFF 9 天均与日期区间自洽；P6 练习图 13−11=2、6+7=13 正确；第 11 节 24 球与 10 场比分之和一致（3+1+2+3+3+2+3+1+2+4=24）。✓

**未在本轮单独复核、沿用核心 KIT 已核实记录的 3 项**（非缺陷，仅如实标注）：Torrazzo「意大利最高钟楼」的表述、Santa Cecilia 11-22（天主教历通用瞻礼日）、Filmmaker Festival 11-14 开幕~11-22 闭幕的具体日期。

## 4. 语言（意大利语正文 + 日语讲解层，逐句读完）

- 意大利语：拼写、重音、性数配合、变位、标点通读无误。抽查要点：`andare → andrò / assaggerò / guarderò / leggerò`（leggere 未来形正确）；`finire → è finita`（festa 阴性单数）；`piovere → piova`、`nevicare → nevichi`、`controllino`、`sia`、`leggano`（连接法正确）；`bene → meglio`；`ci sarà`（esserci 未来形）；`sono arrivati / ha vinto / ha pareggiato / ha preso`（分词正确）；`so che + 直说式` 与 `è probabile che + 连接法` 的对立讲解正确；`i viola`（Fiorentina 昵称）、`al Franchi`（佛罗伦萨球场）用法正确。
- 日语：讲解层全日语，无他语残留；仅有的非日语 CJK 是 W46 既定先例的「翻译」题型标签（Q137–140，4 处）与核心沿用的动词变位注全角冒号 ：（Q16–20/60–61）。译文准确自然，抽查：Q137–140 重定向译句与意语原文语义一致；Q58 注「主観的な評価」对 `più bella`（最高级）的说明恰当；Q82 Falso 的理由（开幕为 23 日、22 日仅为预览）正确；P6 披露句「締め切り時点で議会はまだ採決していません…採決結果は載せていません」准确。
- 练习键 150 题逐题与题干语义核对：**全部一致**。含 3 组匹配题（P2 25–28：c/b/d/a；P4 52–55：d/b/c/a；P8 141–144：d/c/b/a，均按渲染页上的 a–d 选项顺序逐项核对，非只比键值）；E 节重定向键 Q137–140 语义正确；Q58 `più bella`（la serata più bella = 最高级）合法；Q77 `ci sarà`、Q104 B `leggerò`、Q108 A `è finita`、Q112 B `torna` 均正确。RISPOSTE 印刷键与题干键逐项一致（抽查全部 150 条中的 113–150 与 25/52/58/137–144 等关键条）。
- 3 处文体/事实边界（核心层原文，fan-out 未改动，不作缺陷）：P6 听证会用现在时 `ascoltano`（截稿时听证会进行中，时态自洽）；P2 `quasi quattrocento anni`（1630→2026 为 396 年）；P1 `VOL. 4　QUARTA EDIZIONE` 与页脚 `VOL.4` 并存（核心格式）。

## 5. 观察（非阻塞，不构成 D 缺陷）

- **O1 — KIT §8 的 freeze baseline 表述不精确。** 该版 scratch 下 `freeze-baseline/` 内存的是**本版重建**（build-copy 为 it-ja 目录，svg 与已发 it-ja SVG 逐字节相同），即它证明的是“本版可由源码复现”，而非核心基线。正确的核心基线由本人在本轮重跑（见 §1 表）：`--core-svg` 指 core-it/svg，**8/8 byte-identical**，实质门禁通过。建议：KIT §8 改写为“本版复现 8/8 + 核心基线 8/8（本轮复校重跑）”，勿把本版复现的目录当作核心基线的证据。
- **O2 — P5 词汇表换行首出现 `·`。** 词表 `anteprima · protagonista · sede · incontro / · indipendente · lettrice` 第二行以 `·` 开头（核心在 `sede ·` 后换行）。同词、不同断行，KIT §10 已披露为接受项；视觉上仅为轻微排版毛边，无重叠、无错词。非阻塞。
- **O3 — P8-keys 仅 6 px 余量（2546/2552）、P8 答案 9.75 pt。** 均为 KIT §8/§10 已披露的确定性状态（无两行答案、无溢出），符合 SOP §1.1 让步 4 的下限。非阻塞。
- **O4 — P3/P5 中页结构性空白、P6 第 2 栏图前空白。** 核心版式 pattern，KIT §10 已披露。非阻塞。
- **O5 — tools/ 内无名为 abutting/keycheck 的独立工具。** 本轮以 occlusion TEXTX（0 flags）+ 8 页目视 + scratch gates.py 150-key 审计 + 本人 150 键逐题语义核对覆盖；建议后续把这两项检查在工具侧具名化，非本版问题。

## 6. Verdict

**(a) 零问题，可定稿。**

未发现 D 级缺陷。上述 O1–O5 均为非阻塞观察（其中 O1 是 KIT 表述问题，非本版内容问题；O2–O4 为已披露的接受项；O5 为工具具名化建议）。

三件 SHA（与 KIT §7 一致，已于开工前核对）：

- 印刷 PDF：`f0fb8a83671a4d7bfee852436c907b6372a7631be92a7ef4725f2154d0e97220`（28,221,078 B）
- 网页 PDF：`b6660f12a4d57833139ba6a80a7d4fc2cd033f308ed3cf35fa36bfacdaf72cf3`（1,869,651 B）
- 文本导出：`87d1ec4e54d7dcaecac7028bd745aa7483978235425ae756157da6da6bd686f5`（58,239 B）
