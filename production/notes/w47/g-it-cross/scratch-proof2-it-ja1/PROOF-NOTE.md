# PROOF-NOTE — 2026-W47 it-ja（proof2，重扩散后独立复校）

- 复校员：proof2（只读复校，未修版、未 commit、未 push、未派 subagent；未重渲染交付的 web PDF）
- 复校对象：`~/workspace/weekly-git/production/2026-w47/2026-w47-it-ja/`（重扩散新版，核心 fix3 commit 36bdec2e）
- 复校时间：2026-11-11 20:16–21:00 UTC
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-it-ja1/`
- 先读：SOP.md §1.1/§8/§9 全文、repo AGENTS.md、该版 WEEKLY-KIT.md 全文、重扩散报告 `scratch-refanout-it/FANOUT-REPORT-it.md`——已读。
- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` rc=0；scratch 内真实写文件成功。`TMPDIR=<scratch>/tmp` 全程，`PYTHONDONTWRITEBYTECODE=1` 全程，未写 /tmp。
- 方法：从头全量重校，不假定 proof1 的旧缺陷仍在或已修——每项实测。机械门禁全部本人重跑（见 GATE-LOG.md）；全文 1317 行逐行读完；8 页印刷 PDF 逐页目视。

## 结论

**(a) 零缺陷，可定稿。**

未发现 D 级缺陷。下述 O1–O6 均为非阻塞观察（O1 是本轮复校过程的透明披露；O2–O4 为 KIT 已披露的接受项；O5 为冻结核心继承的版式特征；O6 为扫查工具口径说明）。

## 0. SHA 核对（开工前，先核对三件；收工时再验一次）

| 件 | 盘上大小 | 盘上 sha256 | 任务书 / KIT §7 登记 | 结论 |
|---|---|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-JA.pdf` | 28,221,039 B | `279962b7b3ae203049e1646d81c737228309aff0b864fef94079f4cc81ddb319` | 同左 | 一致 |
| 网页 PDF `La-Lucerna-VOL4-JA-web.pdf` | 1,901,688 B | `4df33c6917da1b4452d8f8aa7574eb47d70161a074c0b30424cbb684ab007a7b` | 同左 | 一致 |
| 文本导出 `2026-w47-it-ja.text.md` | 58,186 B | `bf64b304305e5d6e0679a9816c6b95576709c47e30dd69aa4cc6b24bf6def634` | 同左 | 一致 |

印刷 PDF 8 页，版面 1462.5×2025 pt（与 KIT 一致）；网页 PDF 8 页同版面。

## 1. 门禁实测（本人重跑，非只引 KIT；详见 GATE-LOG.md）

| 门禁 | 结果 |
|---|---|
| run.py | RC=0；150 题；0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE；级别 A2 47 / B1 70 / B2 33；页分布 10/18/18/18/18/18/12/38；模范文 99 词；P8-keys 末端 2546/2552 |
| SVG 重建 | 本体重建 8/8 字节一致（`cmp` 逐个）；`tools/freeze.py baseline` 本版 8/8，核心 core-it 8/8（两轮均 RC=0） |
| 重渲印 PDF | 重渲后 sha256 `279962b7…`，与交付逐字节相同（28,221,039 B） |
| freeze diff vs core | RC=0；P1–P7 增减碎片 0 未解释；新增 CJK 3,054 字，全部为日语讲解层字符 |
| occlusion audit | 自检先过；**0 flags** |
| creambox（canonical） | 29 盒，盒内末行基线 clearance 全部 ≥ +4.5 px；7 处 desc-clear 负值（−0.9 ~ −1.5）逐行核查末行文字均不含下行字母（日语句或无 g/j/p/q/y 的意大利语句），非真实漫出，目视确认末行在盒内留有空隙 |
| creambox_check 窄带 | NO OVERFLOW |
| spill 扫查 | 0 真溢出（全部候选均为下一区块栏头/表行/双栏图表的另一半，逐项裁定） |
| 孤儿扫查 | 1439 行：class-a（独行 。）0、class-b（行首闭合标点）0（PIL 真墨 + svglib advance 双口径）；暴力复核 17 个闭合标点起首元素，行首者 0 |
| 列溢出扫查 | 原始命中 ~40 处，逐项裁定全部为假阳性（双栏通栏/通栏带/居中家具/表元伸入 28 px 栏间隙）；真墨 + 目视确认无一处触及相邻栏内容 |
| p8 extract / compare | 150/150 noted；vs core **CLEAN**，keydiff = **[137, 138, 139]**（重定向的读者句，预期内；实测值，非硬套） |
| print/web 文字层 | pdftotext 词多重集相等（各 6,749 词）、字符多重集相等；字符数各 37,813；tofu（U+FFFD）0；网页 PDF 1,901,688 B < 7 MB |
| P8 最小字号 | SVG 13.0 px；渲染实测 PyMuPDF **P8 最小 9.75 pt**（= SOP §1.1 让步 4 的下限）；P1–P5/P7 最小 11.62 pt，P6 最小 12.75 pt |
| §1.1 | 纸色 #fbfaf6；无金/红褐/近黑；徽章色 A2/B1/B2 齐全；VOL.4 ×9；VOL.5 仅 3 处合法节点（预告头/LETTERE 披露/P2  cross-ref）；无双线外框（全页 rect 0）；字体 Newsreader + Noto Sans/Serif CJK JP + UnifrakturMaguntia（刊头）；页脚 `La Lucerna　イタリア語週刊 VOL.4　本文はイタリア語　解説は日本語` + 页码行逐页在位 |
| text.md 校验 | forward-miss 0 / reverse-miss 0；答案 150 条连续 1–150；键 1–150 与核心一致（除 137–139 重定向与写作项）；注释与 translations.py 值一致（除 137–140 与写作项） |
| fix3 九项 | B-1~B-9 新措辞各出现恰好 1 次、旧措辞 0 次（源码 grep）；缩短后的选项首行 PIL 真墨右缘余量 +17.5 ~ +139.2 px，全部在栏内 |
| 标题数 | “56 titles”是幻数。实测：SVG `<text>` 节点 font-size ≥ 30 px 共 **52 个**（含 P1 刊头带 15 个单字/空格节点、P2–P8 小刊头家具 7 个、三行标题按行计）；去重后独立标题行 **16 条**（8 版带 + P1 刊头 + P1 眉题 + 6 篇正文标题） |
| 日期/星期 | 文中全部 16 组星期表述经 `date`（Europe/Rome）核验一致（VEN 6.11、SAB 7.11、DOM 8.11、giovedì 12、domenica 15、LUN 16、MAR 17、GIO 19、VEN 20、SAB 21、DOM 22、lunedì 23、martedì 24、martedì 17、11-29 日、12-02 三、12-06 日）；天数自洽（Torrone 16 天、Eurochocolate 10 天、BookCity 7 天、TFF 9 天）；算术 24 球之和、13−11=2、6+7=13 正确 |
| 模范文词数 | 人工 + 程序双计 **99 词**（80–100 词区间内） |
| P7 金句 8 条 | 全文计数每条恰好 **2 次**（正文 1 次 + P7 1 次），逐字一致，页码标注 P1/P1/P2/P3/P4/P5/P6/P6 全部正确 |
| 匹配题选项顺序 | 对 SVG 渲染字母逐项核对：P2 a/b/c/d = mettere / il ponte di barche / stare bene / la piccola luce → 键 c/b/d/a ✓；P4 = la prima volta / che non ha mai perso / il gruppo / il primo posto → 键 d/b/c/a ✓；P8 = un livello di reddito / i soldi che pagano / la differenza / la legge di bilancio → 键 d/c/b/a ✓ |
| SIMP_ONLY ['国','学'] | Unicode 级计数：本版 8 个 SVG + 文本导出 + 源码中 **国 0 次、学 0 次**；核心 core-it P1 的各 1 次是中文家具（本版已换为日语）。无可核实之处，非缺陷 |
| 「翻譯」残留 | 文本导出 翻訳 ×4（L969/971/973/975，Q137–140 型标签）、翻譯 ×0；SVG 中该标签本就不绘制（bslib4.ex 只画徽章/题号/指示语），其唯一渲染面就是文本导出——已在该面核实 |
| 禁词扫描 | `Ucraina\|Russia\|Putin` 文本导出 **0** |
| abstract（SOP §9） | 1 行（423 字节）、无 ASCII 双引号、含刊名 La Lucerna、目标语名イタリア語、A2–B2、150問、真实主题（セリエA第11節、トッローネ祭、ユーロチョコレート、聖母健康祭、植樹の日、ブックシティ、トリノ映画祭、予算案）——通过，与 KIT §7 逐字一致 |
| 刊头带真墨 | P1 刊头带墨左缘 102.3、右缘 1778.9（版宽 1950），左余量 102.3、右余量 171.1；蛾旁的 リ 目视完整 |
| 核心未动 | 本轮运行后 core-it 目录 0 个文件被改动（mtime 扫描）；freeze 两轮均自验核心 SVG 未变 |
| P1 刊头带 | 起于 x=102.3，两侧边距干净；moth 处的 リ 渲染图上完整（旧审计假报已由工具修复版排除） |

## 2. 版式几何（8 页印刷 PDF 逐页目视 + 工具）

8 页已从交付印刷 PDF 逐页看完（半尺寸渲染）：无溢出、无重叠、无压页脚、无豆腐块、无横向漫出、无图片与出处错位。逐项裁定：

- 全部奶油盒末行基线 clearance ≥ +4.5 px；7 处 desc-clear 负值逐行核查末行文字均不含下行字母，是 0.30em 通用余量的假象；P7 三个工具盒（ERRORI TIPICI +18.1、LA PAROLA +4.5、LETTERE +5.1）目视确认末行在盒内留有空隙。**不是缺陷。**
- 盒下 +45px 窗口内 12 行（P1 `LA PAROLA DELLA SETTIMANA` +24、P3 `IL TORRAZZO E IL TORRONE` +37、P4 结果表行 +26~+40、P6 `ESERCIZI` 栏头 +42）——均为盒外下一区块的栏头/表体/下一行，目视确认不重叠，是已知假阳性形态。**不是缺陷。**
- P5 词汇表断行：`anteprima · protagonista · sede · incontro`（栏 1 底部）/ `· indipendente · lettrice`（栏 2 顶部，行首 `·`）——同词、不同断行，6 个词齐全、无重叠、无缺词；另 P5 解説行第二行行首亦为 `·`（`· l'incontro 交流会…`），同属换行形态。KIT §10 已披露为接受项。**不是缺陷。**
- 9 处行首 `·`（P4 Q48/Q49、P5 解説与词表、P6 Q84/Q85/Q89、P7 Q108、P8 Q127）全部是选项串/讲解串的换行续行，核心拉丁版式亦有同类续行。**不是缺陷。**
- 匹配题指示语 `単語と意味を合わせなさい` 真墨右缘超栏边 +7.5 px（P2/P4/P6/P8 各一处），伸入 28 px 栏间隙、未触及相邻栏内容，目视确认；P4 结果表第二列个别单元格 +10~+30 px 同属栏间隙内。**不是缺陷。**
- P8 RISPOSTE 末行（150. ✓ 模範文…）在页脚线上方，flow 末端 2546/2552——目视确认无侵入页脚。
- P4 E TU 盒底与表头齐平（1140.45 = core）；P4 结果表 5 行带交替底色对齐，无错行；P6 图表 5 根柱（5°/6°/7°/11°/13°）比例与标签齐全，PROPOSTA ≠ LEGGE 盒 4 行在内。
- 7 张配图及出处逐页核对：P1 老球场（PD）、P2 Canaletto（PD）、P3 Torrazzo（CC0）、P4 1920s 网球全景（PD）、P5 Corot 1868（PD）、P7 Dante（Met CC0）、P8 Vermeer（PD）——图说与出处均与 KIT §5 一致，图在位、无错位。

## 3. 内容事实（全文逐行读完；意大利语文本与核心冻结合一，事实沿用核心已核实记录，复核其在本版中的一致性）

- **Serie A 第 11 节**：10 场比分逐场一致（Venezia–Udinese 2–1、Cagliari–Frosinone 1–0、Torino–Lecce 1–1、Parma–Bologna 1–2、Roma–Sassuolo 3–0、Napoli–Lazio 1–1、Genoa–Milan 1–2、Monza–Atalanta 0–1、Inter–Como 2–0、Fiorentina–Juventus 2–2）；24 球（3+1+2+3+3+2+3+1+2+4=24）；积分 Lazio 29、Inter 28、Roma 27、Milan 24、Como 23、Udinese 5 垫底；Gattuso 为 Lazio 主帅；Roma 最多进球 31 球；第 12 节 11-21~23，Lazio–Lecce 周六、Atalanta–Inter 周日 20:45 Bergamo、Monza–Fiorentina 周一收官。三处（P1/P4/IN QUESTO NUMERO 与练习键）口径一致。✓
- **Nitto ATP Finals**：11-15~22 都灵，8 人、Zverev 世界第一、Alcaraz、Cobolli 首次参赛、Sinner 为 2025 冠军因伤缺席；决赛周日 22 日。✓
- **Nations League**：意大利–法国 11-12 周四、比利时–意大利 11-15 周日；文中未印赛果、推迟至 VOL.5，与“截稿后开赛”一致，P1/P2/P4 三处口径一致。✓
- **Festa del Torrone**：第 29 届 11-07~22（16 天、三周末），主题「Il Confine」；Torrone d'Oro 11-22 11:00 Palatorrone 授予 Davide Simonetta（Cremona 出生）；corteo 16:00、150 人以上文艺复兴服装、Sforza–Visconti 婚礼重演 17:00、旗手与火舞至 18:00、终场「Il torrone va in brodo」18:00；1441 年婚礼传说（10 月 25 日）。✓
- **Eurochocolate**：第 32 届 11-13~22（10 天），主题「Fate Dolci」；Calabria 首个 Regione Ospite；「I tesori della Calabria Straordinaria」11-20 周五 18:15；Iginio Massari 11-22 闭幕嘉宾。✓
- **Alba 白松露集市**：第 96 届 10-10~12-06。✓
- **Madonna della Salute**：11-21，1630 年瘟疫之誓，Longhena 设计、1631–1687 年建成；奉纳桥（船桥）；castradina（盐渍烟熏羊肉配 verze，11 月 20 日晚吃）。✓
- **植树日**：11-21，1898 年首届，2013 年第 10 号法律定为国家日。✓
- **BookCity Milano**：第 15 届 11-23~29（7 天），主题「Il senno sulla Luna」（Ariosto《Orlando furioso》），1,360 活动、2,487 嘉宾、1,164 本书、443 会场；开幕 11-23 周一 20:00 Teatro Dal Verme，Colson Whitehead（两届 Pulitzer）；预览 Edmund de Waal 11-22 周日 16:00 Fondazione Rovati。✓
- **Torino Film Festival**：第 44 届 11-24 周二~12-02 周三，共 9 天。✓
- **Manovra 2027**：DPB 10-15 送布鲁塞尔；2027 增长 +0.8%、赤字 3.4%；法案 10-28 内阁通过、约 260 亿欧元；编号 C. 3174-bis；听证会 11-09~12（Giorgetti 周四 12 日）；修正案截止 11-17 周二 18:00；须 12-31 前终审；Irpef 第二档 33% 由 50,000 扩至 55,000 欧元；金融业约 50 亿财源；卫生加钱。文中三处「PROPOSTA ≠ LEGGE」披露完整（P1/P2/P6）。✓
- **日历/算术**：Torrone 16 天、Eurochocolate 10 天、BookCity 7 天、TFF 9 天均与日期区间自洽；P6 练习图 13−11=2、6+7=13 正确；第 11 节 24 球与 10 场比分之和一致。✓

**沿用核心 KIT 已核实记录、未在本轮单独复核的 3 项**（非缺陷，仅如实标注）：Torrazzo「意大利最高砖砌中世纪钟楼」的表述（fix3 B-4 已按核实结果改写）、Santa Cecilia 11-22（天主教历通用瞻礼日）、Filmmaker Festival 11-14 开幕~11-22 闭幕的具体日期。

## 4. 语言（意大利语正文 + 日语讲解层，逐句读完）

- 意大利语：拼写、重音、性数配合、变位、标点通读无误。抽查要点：`andare → andrò / assaggerò / guarderò / leggerò`（leggere 未来形正确）；`finire → è finita`（festa 阴性单数）；`piovere → piova`、`nevicare → nevichi`、`controllino`、`sia`、`leggano`（连接法正确）；`bene → meglio`；`ci sarà`（esserci 未来形）；`sono arrivati / ha vinto / ha pareggiato / ha preso`（分词正确）；`so che + 直说式` 与 `è probabile che + 连接法` 的对立讲解正确；`i viola`（Fiorentina 昵称）、`al Franchi`（佛罗伦萨球场）用法正确。
- 日语：讲解层全日语，无他语残留；仅有的非日语 CJK 是「翻譯」已清零后的「翻訳」题型标签（Q137–140，4 处，文本导出面）与核心沿用的动词变位注全角冒号 ：（Q16–20/60–61）。译文准确自然，抽查：Q137–140 重定向译句与意语原文语义一致（137 圣母健康祭/奉纳之桥、138 周日夜阿塔兰塔–国米、139 周六拉齐奥主场对莱切、140 Ogni cifra deve essere chiara 的反向翻译）；Q58 注「主観的な評価」对 `più bella`（最高级）的说明恰当；Q82 Falso 的理由（开幕为 23 日、22 日仅为预览）正确；P6 披露句「締め切り時点で議会はまだ採決していません…採決結果は載せていません」准确。
- 练习键 150 题逐题与题干语义核对：**全部一致**。含 3 组匹配题（P2 25–28：c/b/d/a；P4 52–55：d/b/c/a；P8 141–144：d/c/b/a，均按渲染页上的 a–d 选项顺序逐项核对，非只比键值）；E 节重定向键 Q137–140 语义正确；Q58 `più bella`（la serata più bella = 最高级）合法；Q77 `ci sarà`、Q104 B `leggerò`、Q108 A `è finita`、Q112 B `torna` 均正确。RISPOSTE 印刷键与题干键逐项一致（全 150 条读完核对）。
- 3 处文体/事实边界（核心层原文，fan-out 未改动，不作缺陷）：P6 听证会用现在时 `ascoltano`（截稿时听证会进行中，时态自洽）；P2 `quasi quattrocento anni`（1630→2026 为 396 年）；P1 `VOL. 4　QUARTA EDIZIONE` 与页脚 `VOL.4` 并存（核心格式）。

## 5. 观察（非阻塞，不构成 D 缺陷）

- **O1 — 本轮复校的重建改写了生产文件（字节一致）。** `content*.py` 的 `OUT` 与 `render.py` 的 `BASE` 硬编码为生产绝对路径，故本人在副本里跑 run.py/render.py 时实际重写了生产目录的 `svg/*.svg` ×8、`cards/*.png` ×8 与印 PDF（mtime 变为 20:18–20:22）。全部为字节一致的重写：三件 SHA 收工时再验仍与任务书/KIT 完全一致；web PDF 与 text.md 未被触碰（mtime 仍为 12:30）；core-it 0 文件被改动。正确做法是走 `tools/freeze.py baseline`（它会重定向输出路径，本轮两轮 baseline 均已如此跑通）。请后续复校员勿直接在副本跑 run.py/render.py。内容无损，仅作过程披露。
- **O2 — P5 词汇表换行首出现 `·`。** 词表 `anteprima · protagonista · sede · incontro / · indipendente · lettrice` 第二行以 `·` 开头（核心在 `sede ·` 后换行）。同词、不同断行，KIT §10 已披露为接受项；视觉上仅为轻微排版毛边，无重叠、无错词。非阻塞。
- **O3 — P8-keys 仅 6 px 余量（2546/2552）、P8 答案 9.75 pt。** 均为 KIT §8/§10 已披露的确定性状态（无两行答案、无溢出），符合 SOP §1.1 让步 4 的下限。非阻塞。
- **O4 — P3/P5 中页结构性空白、P6 第 2 栏图前空白。** 核心版式 pattern，KIT §10 已披露。非阻塞。
- **O5 — 标题字号低于 SOP §1.1 阶梯。** 实测：P1 头条 44 px = 33 pt、P2–P6 正文标题 37 px = 27.75 pt、栏目条 46 px = 34.5 pt，均低于阶梯所称头条标题 40–45 pt。此为冻结核心继承的版式（核心 re-proof (a) 已按此版式通过），不在 fan-out 可改范围；本版与核心逐字节一致即为通过。非阻塞，仅记录。
- **O6 — colspill_scan.py 直搬口径过严。** 该脚本不知双栏通栏、通栏带与 `text-anchor=middle` 家具，在本版产出约 40 处原始命中，逐项裁定全部为假阳性。几何权威仍是 `tools/occlusion_audit.py`（0 flags）+ 逐页目视。建议后续把通栏/居中元素排除规则写进工具，非本版问题。

## 6. Verdict

**(a) 零问题，可定稿。**

未发现 D 级缺陷。上述 O1–O6 均为非阻塞观察（其中 O1 是复校过程披露，非本版内容问题；O2–O4 为已披露的接受项；O5 为冻结核心继承；O6 为工具口径说明）。

三件 SHA（与任务书、KIT §1/§7 一致，开工前与收工时两次核对）：

- 印刷 PDF：`279962b7b3ae203049e1646d81c737228309aff0b864fef94079f4cc81ddb319`（28,221,039 B）
- 网页 PDF：`4df33c6917da1b4452d8f8aa7574eb47d70161a074c0b30424cbb684ab007a7b`（1,901,688 B）
- 文本导出：`bf64b304305e5d6e0679a9816c6b95576709c47e30dd69aa4cc6b24bf6def634`（58,186 B）

门禁汇总：gates.py 19/19 PASS；freeze baseline 本版 8/8 + 核心 8/8；重渲印 PDF 逐字节相同；occlusion 0 flags；creambox 0 溢出；spill 0；孤儿扫 0；p8 CLEAN keydiff [137, 138, 139]；P8 最小 9.75 pt。
