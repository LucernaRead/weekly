# PROOF-NOTE — 2026-W47 it-ja（reproof，重扩散 2 后独立复校）

- 复校员：reproof（只读复校，未修版、未 commit、未 push、未派 subagent；未重渲染交付的 web PDF；生产目录 0 写入——run.py/render.py 只在 scratch build-copy 里跑，OUT/BASE 改指 scratch；freeze.py 自带防写穿守卫）
- 复校对象：`~/workspace/weekly-git/production/2026-w47/2026-w47-it-ja/`（重扩散 2 新版，core D-2 fix 后重建）
- 复校时间：2026-11-11 21:58–22:15 UTC（协调员盘上实测 21:58 UTC 后开工）
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it2-ja/`
- 先读：SOP.md §1.1/§8 全文、repo AGENTS.md、该版 WEEKLY-KIT.md 全文、`scratch-refanout-it2/FANOUT-REPORT-it2.md` 全文、`scratch-proof2-it-ja1/PROOF-NOTE.md` 全文、`scratch-fix-core-it-d2/FIX-LOG.md` 全文——已读。
- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0；scratch 内真实写文件成功。`TMPDIR=<scratch>/tmp` 全程，`PYTHONDONTWRITEBYTECODE=1` 全程，未写 /tmp（一次工具输出溢出由 runtime 写入 /tmp/jarvis-tool-output-*.json，系 runtime 自身行为，非本轮写盘）。
- 方法：从头全量重校，不抄前人结论——每项实测。机械门禁全部本人重跑（见 GATE-LOG.md）；全文 1317 行逐行读完；8 页交付印 PDF 逐页 200 dpi 目视；P7 A2 栏 200 dpi 裁图新旧对照。

## 结论

**(a) 零缺陷，可定稿。**

未发现 D 级缺陷。下述 O1–O5 均为非阻塞观察（O1–O3 为 KIT 已披露的接受项；O4 为冻结核心继承的版式特征；O5 为扫查工具口径说明）。

## 0. SHA 核对（开工前逐字核对，收工时再验一次）

| 件 | 盘上大小 | 盘上 sha256 | 任务书 / KIT §7/§12 登记 | 结论 |
|---|---|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-JA.pdf` | 28,221,020 B | `640a355a2943efe35b7c1437e1154a4012aa1ec51f18fff155fc7caa4e1c6666` | 同左 | 一致 |
| 网页 PDF `La-Lucerna-VOL4-JA-web.pdf` | 1,901,668 B | `4f1bac2c12b8762c187a60647fec578f187f9f5150a2b65cfca31b474f00ee3f` | 同左 | 一致 |
| 文本导出 `2026-w47-it-ja.text.md` | 58,165 B | `5ac2ecf5abb28bbc9f56c182572a9c7a7e4e93ae8b9c49b5468cc890e0ec16d7` | 同左 | 一致 |

印刷 PDF 8 页，版面 1462.5×2025 pt；网页 PDF 8 页同版面。收工再验三 SHA 不变。生产文件 mtime 仍为重扩散建版时间（21:48–21:56），本轮 0 写入。

## 1. 回归项 A — D-2 修正（逐项独立重测）

- 新串 ×1 各就其位（空白归一化后计数，`→` 粘词与换行断裂均已处理；未归一化会误报 0，见方法备注）：
  - `Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.` —— content7.py:17 ×1、text.md:775 ×1、p7 SVG（节点拼接）×1、印 PDF P7 文字层 ×1、网 PDF P7 文字层 ×1，全版各 ×1。
  - `Il verbo è leggere, regolare al futuro: leggerò.` —— content7.py:18 ×1、text.md:777 ×1、p7 SVG ×1、印/网 PDF P7 文字层 ×1，全版各 ×1。
- 旧串 0 处：`Leforme sono regolari: andare` 与 `irregolare al futuro: leggerò` 在 live 内容文件（content7.py、8 个 SVG、text.md、两 PDF 文字层全 8 页）均为 0。唯一命中是 WEEKLY-KIT.md:102 的记录行（引述旧串作档案，属文档非内容）。备份旧版 p7 SVG 中旧串各 ×1（对照方向正确）。
- `andrò` 全版 0 处（text.md、SVG、两 PDF 文字层）；`andare` 在 text.md 出现 8 次，均为合法：Q42/Q76/Q101 题干原形提示、P2 衔接句 `Al momento di andare in stampa`、Q101 键注与 P7 诊所注，与 D-2 旧串无关。
- 与重扩散前生产版（`scratch-refanout-it2/backup/2026-w47-it-ja/`）diff 只许 P7 变化，逐项实测：
  - text.md diff 恰为 :775/:777 两行 replace，58,186 → 58,165 B，恰 −21 B。
  - SVG：p1–p6/p8 逐字节一致，仅 p7 不同（新 `12f2aeb9…`，旧 `d9f8fa3d…`）。
  - cards：p1–p6/p8 逐字节一致，仅 p7 不同。
  - content diff：仅 `content7.py`，恰为 :17/:18 两行。
  - p7 SVG 文本节点 diff 限定于两句 D-2 句的换行碎片（旧 168 节点 → 新 162 节点；opcode 仅 4 处 replace/delete，全在两句内；盒标题 ERRORI TIPICI/LA PAROLA/LETTERE/FRASI/LA PROSSIMA SETTIMANA 计数新旧一致）。
  - 两 PDF 因 P7 重建而变（印 28,221,039 → 28,221,020 B；网 1,901,688 → 1,901,668 B）。
- 200 dpi 裁图对照：新 P7 A2 栏两句修正句渲染干净（`render/p7-a2-crop.png`）；备份旧版同区裁图（`render/p7-a2-crop-backup.png`）仍为旧错句；除两句外版式逐行一致，Q101–104、桥句、Dante 图均在原位。

## 2. 回归项 B — P7 教学段语义逐句事实核查（D-2 教训：读教学句本身）

- L17 新句只举 assaggiare/guardare 为规则形：正确。assaggiare → assaggerò（-giare 动词去 i 后规则加 -ò）、guardare → guarderò（规则 -are 动词 a→e）均为规则未来形；andare 已移出规则例。
- L18 新句 `leggere, regolare al futuro: leggerò`：正确。leggere 为 -ere 规则动词，未来形去尾 -e 加 -ò，leggerò 恰为规则构形；其不规则处只在远过去时 lessi 与过去分词 letto，不在未来时。
- 公开依据（本轮独立检索，非抄 FIX-LOG）：LibreTexts《Indicativo futuro》以 leggere 作规则 -ere 动词例（io leggerò），并列 andare → andr- 为不规则词干；LBCC Pressbooks《IL FUTURO》同表（andare → andr-，andrò/andremo）；FluentU、Lawless Italian、Dolce Vita 均列 andare → andrò 为不规则未来形（元音脱落型词干 andr-，规则形 *anderò* 不存在）。
- P7 其余教学句逐句核对无误：B1 `è partito/è finita`（essere + 分词性数一致）、`abbiamo visto/hanno comprato`（avere 分词不变）；B2 `piova/nevichi/leggano`（è probabile che / è possibile che / bisogna che + 连接法）与 `so che + 直说式 torna` 的对立正确；ERRORI TIPICI 4 条改错（La Lazio ha / vinca / sono andato / Il torrone è dolce）全部正确。

## 3. 门禁实测（本人重跑，非只引 KIT；详见 GATE-LOG.md）

| 门禁 | 结果 |
|---|---|
| run.py（scratch build-copy，OUT/BASE 改指 scratch） | RC=0；150 题；0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE；级别 A2 47 / B1 70 / B2 33；页分布 10/18/18/18/18/18/12/38；模范文 99 词；P8-keys 末端 2546/2552；P7-a2 flow 末端 y=1124（修前 1157，短一行，底 1560）；P4 col3 末端 1140.45（= 核心）；P7 col3 末端 1673.0 |
| SVG 重建 | build-copy 重建 8/8 字节一致（`cmp` 逐个）；`tools/freeze.py baseline` 本版 8/8 + 核心 core-it 8/8（两轮均 RC=0；`--core-svg` 指 core-it 自身 `svg/`，build-copy 经核实确为 core-it——p7 hash `a7e6afa4…` 为 D-2 定稿值，非 edition 冒充） |
| 重渲印 PDF | build-copy 重渲印 PDF sha256 `640a355a…`，与交付逐字节相同（28,221,020 B） |
| freeze diff vs core | RC=0；P1–P7 增减碎片 0 未解释；P1 +61/−39、P2 +31/−28、P3 +30/−28、P4 +27/−26、P5 +44/−39、P6 +26/−25、P7 +41/−39、P8 +305/−376，与 proof2 逐页相同（D-2 纯拉丁改动使 core 与版同向变化，diff 计数不变）；新增 CJK 全部为日语讲解层字符（CJK 版无 strict-CJK 项） |
| occlusion audit | 自检先过（6 类阳性全触发、干净对照沉默）；新版 8 页 **0 flags**；备份旧版 8 页亦 **0 flags**（STRADDLE 对照，见 §6） |
| creambox（canonical） | 29 盒，盒内末行基线 clearance 全部 ≥ +4.5 px；P7 三工具盒 min +4.5；7 处 desc-clear 负值（−0.9 ~ −1.5）末行均不含下行字母（日语句），非真实漫出 |
| creambox_check 窄带 | 8 页全部 NO OVERFLOW |
| spill 扫查 | 候选 61 处，与 proof2 日志逐字节相同，全部为已知假阳性形态（下一区块栏头/表行/双栏图表另一半）；真溢出 **0** |
| 孤儿扫查 | 1439 行：class-a 0、class-b 0（PIL + svglib 双口径，逐页全 0）；暴力复核闭合标点起首元素行首者 0（proof2 为 1438 行，+1 行系 P7 D-2 重排净增，零孤儿结论不变） |
| 列溢出扫查 | 原始命中 43 处，与 proof2 日志逐字节相同，逐项裁定全部为假阳性（双栏通栏/通栏带/居中家具/表元伸入 28 px 栏间隙）；真溢出 **0** |
| p8 extract / compare | 150/150 noted；vs core **CLEAN**，keydiff = **[137, 138, 139]**（重定向的读者句，预期内；实测值，非硬套） |
| print/web 文字层 | pdftotext 各 47,419 B，`cmp` 逐字节相同；词多重集相等（各 6,746 词，较 proof2 的 6,749 恰少 3 词 = D-2 删去的 `andare`、`→`、`andrò,`）；tofu（U+FFFD）0；网页 PDF 1,901,668 B < 7 MB |
| P8 最小字号 | SVG 13.0 px；渲染实测 PyMuPDF **P8 最小 9.75 pt**（= SOP §1.1 让步 4 的下限）；P1–P5/P7 最小 11.62 pt，P6 最小 12.75 pt |
| §1.1 | 纸色 #fbfaf6；无金/红褐/近黑；徽章色 A2/B1/B2 齐全；VOL.4 ×9；VOL.5 仅 3 处合法节点；无双线外框（全页 rect 0）；字体 Newsreader 1136、Noto Sans CJK JP 627、Noto Serif CJK JP 295、UnifrakturMaguntia 1（较 proof2 少 6 节点 = P7 D-2 重排 9→3 节点所致）；页脚 `La Lucerna　イタリア語週刊 VOL.4　本文はイタリア語　解説は日本語` + 页码行逐页在位 |
| text.md 校验 | forward-miss 0 / reverse-miss 0；答案 150 条连续 1–150；键 1–150 与核心一致（除 137–139 重定向与写作项）；注释与 translations.py 值一致（除 137–140 与写作项） |
| fix3 九项 | 新措辞各 ×1（text.md；D1/D2b/D2d/D11/P8a 另经 SVG 节点拼接核实 ×1）、旧措辞 0（text.md + SVG）；缩短后的 7 行首行 PIL 真墨右缘余量重测：P2 b +31.0 / d +40.2、P4 b +139.2 / c +17.5、P8 a +34.0 / b +51.5 / c +24.0 px，全部在栏内，与 fix3 修后值逐字一致 |
| 标题数 | “56 titles”是幻数，仍不成立。实测：SVG `<text>` 节点 font-size ≥ 30 px 共 **51 个**（P1 22 / P2–P6 各 5 / P7 2 / P8 2），与备份旧版逐页相同；去重后独立标题行 16 条（8 版带 + P1 刊头 + P1 眉题 + 6 篇正文标题） |
| 日期/星期 | 文中全部星期表述经 `date`（Europe/Rome）核验一致（VEN 6.11、SAB 7.11、DOM 8.11、giovedì 12、domenica 15、LUN 16、MAR 17、GIO 19、VEN 20、SAB 21、DOM 22、lunedì 23、martedì 24、martedì 17、11-29 日、12-02 三、12-06 日、12-31 四）；天数自洽（Torrone 16 天、Eurochocolate 10 天、BookCity 7 天、TFF 9 天）；算术 24 球之和、13−11=2、6+7=13 正确 |
| 模范文词数 | 人工 + 程序双计 **99 词**（80–100 词区间内） |
| P7 金句 8 条 | 全文计数每条恰好 **2 次**（正文 1 次 + P7 1 次），逐字一致，页码标注 P1/P1/P2/P3/P4/P5/P6/P6 全部正确 |
| 匹配题选项顺序 | 对 SVG 渲染字母逐项核对：P2 a/b/c/d = mettere / il ponte di barche / stare bene / la piccola luce → 键 c/b/d/a ✓；P4 = la prima volta / che non ha mai perso / il gruppo / il primo posto → 键 d/b/c/a ✓；P8 = un livello di reddito / i soldi che pagano / la differenza / la legge di bilancio → 键 d/c/b/a ✓ |
| SIMP_ONLY ['国','学'] | Unicode 级计数：本版 8 个 SVG + 文本导出中 **国 0 次、学 0 次**；核心 core-it P1 的各 1 次是中文家具（本版已换为日语）。无可核实之处，非缺陷（与 proof2 结论一致，实测重做） |
| 「翻譯」残留 | 文本导出 翻訳 ×4（L969/971/973/975，Q137–140 型标签）、翻譯 ×0；SVG 中该标签本就不绘制，其唯一渲染面就是文本导出——已在该面核实 |
| 禁词扫描 | `Ucraina\|Russia\|Putin` 文本导出 **0** |
| abstract（SOP §9） | 1 行（423 字节）、无 ASCII 双引号、含刊名 La Lucerna、目标语名イタリア語、A2–B2、150問、真实主题——通过，与 KIT §7 逐字一致 |
| 刊头带真墨 | P1 刊头带墨左缘 102.3、右缘 1778.9（版宽 1950），左余量 102.3、右余量 171.1；蛾旁的 リ 目视完整 |
| 核心未动 | 本轮运行后 core-it 目录 0 个文件被改动（freeze 两轮核心完整性自验通过；core p7 hash `a7e6afa4…` 为 D-2 定稿值） |

## 4. 版式几何（8 页印刷 PDF 逐页 200 dpi 目视 + 工具）

8 页已从交付印刷 PDF 逐页看完（200 dpi 全页 + P7 A2 栏裁图）：无溢出、无重叠、无压页脚、无豆腐块、无横向漫出、无图片与出处错位。逐项裁定：

- 全部奶油盒末行基线 clearance ≥ +4.5 px；7 处 desc-clear 负值逐行核查末行文字均不含下行字母，是 0.30em 通用余量的假象；P7 三个工具盒（ERRORI TIPICI +18.1、LA PAROLA +4.5、LETTERE +5.1）目视确认末行在盒内留有空隙。**不是缺陷。**
- 盒下 +45px 窗口内 12 行（P1 `LA PAROLA DELLA SETTIMANA` +24、P3 `IL TORRAZZO E IL TORRONE` +37、P4 结果表行 +26~+40、P6 `ESERCIZI` 栏头 +42）——均为盒外下一区块的栏头/表行/下一行，目视确认不重叠，是已知假阳性形态。**不是缺陷。**
- P5 词汇表断行：`anteprima · protagonista · sede · incontro`（栏 1 底部）/ `· indipendente · lettrice`（栏 2 顶部，行首 `·`）——同词、不同断行，6 个词齐全、无重叠、无缺词；另 P5 解説行第二行行首亦为 `·`。KIT §10 已披露为接受项。**不是缺陷。**
- 9 处行首 `·`（P4 Q48/Q49、P5 解説与词表、P6 Q84/Q85/Q89、P7 Q108、P8 Q127）全部是选项串/讲解串的换行续行，核心拉丁版式亦有同类续行。**不是缺陷。**
- 匹配题指示语 `単語と意味を合わせなさい` 真墨右缘超栏边 +7.5 px（P2/P4/P6/P8 各一处），伸入 28 px 栏间隙、未触及相邻栏内容，目视确认；P4 结果表第二列个别单元格 +10~+30 px 同属栏间隙内。**不是缺陷。**
- P8 RISPOSTE 末行（150. ✓ 模範文…）在页脚线上方，flow 末端 2546/2552——目视确认无侵入页脚。
- P4 E TU 盒底与表头齐平（1140.45 = core）；P4 结果表 5 行带交替底色对齐，无错行；P6 图表 5 根柱（5°/6°/7°/11°/13°）比例与标签齐全，PROPOSTA ≠ LEGGE 盒 4 行在内。
- 7 张配图及出处逐页核对：P1 老球场（PD）、P2 Canaletto（PD）、P3 Torrazzo（CC0）、P4 1920s 网球全景（PD）、P5 Corot 1868（PD）、P7 Dante（Met CC0）、P8 Vermeer（PD）——图说与出处均与 KIT §5 一致，图在位、无错位。

## 5. 内容事实（全文逐行读完；意大利语文本与核心冻结合一，事实沿用核心已核实记录，复核其在本版中的一致性）

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

## 6. 语言（意大利语正文 + 日语讲解层，逐句读完）

- 意大利语：拼写、重音、性数配合、变位、标点通读无误。要点：`andare → andremo / assaggeremo / guarderemo / leggerò`（未来形正确）；`finire → è finita`（festa 阴性单数）；`piovere → piova`、`nevicare → nevichi`、`controllino`、`sia`、`leggano`（连接法正确）；`bene → meglio`；`ci sarà`（esserci 未来形）；`sono arrivati / ha vinto / ha pareggiato / ha preso`（分词正确）；`so che + 直说式` 与 `è probabile che + 连接法` 的对立讲解正确；`i viola`（Fiorentina 昵称）、`al Franchi`（佛罗伦萨球场）用法正确。
- 日语：讲解层全日语，无他语残留；仅有的非日语 CJK 是「翻訳」题型标签（Q137–140，4 处，文本导出面）与核心沿用的动词变位注全角冒号 ：（Q16–20/60–61）。译文准确自然，抽查：Q137–140 重定向译句与意语原文语义一致（137 圣母健康祭/奉纳之桥、138 周日夜阿塔兰塔–国米、139 周六拉齐奥主场对莱切、140 Ogni cifra deve essere chiara 的反向翻译）；Q58 注「主観的な評価」对 `più bella`（最高级）的说明恰当；Q82 Falso 的理由（开幕为 23 日、22 日仅为预览）正确；P6 披露句「締め切り時点で議会はまだ採決していません…採決結果は載せていません」准确。
- 练习键 150 题逐题与题干语义核对：**全部一致**。含 3 组匹配题（P2 25–28：c/b/d/a；P4 52–55：d/b/c/a；P8 141–144：d/c/b/a，均按渲染页上的 a–d 选项顺序逐项核对，非只比键值）；E 节重定向键 Q137–140 语义正确；Q58 `più bella`（la serata più bella = 最高级）合法；Q77 `ci sarà`、Q104 B `leggerò`、Q108 A `è finita`、Q112 B `torna` 均正确。RISPOSTE 印刷键与题干键逐项一致（全 150 条读完核对）。
- 3 处文体/事实边界（核心层原文，fan-out 未改动，不作缺陷）：P6 听证会用现在时 `ascoltano`（截稿时听证会进行中，时态自洽）；P2 `quasi quattrocento anni`（1630→2026 为 396 年）；P1 `VOL. 4　QUARTA EDIZIONE` 与页脚 `VOL.4` 并存（核心格式）。

## 7. 盒标题横向溢出专项（STRADDLE 规则）

- 判定：**无缺陷，无观察项。** 证据三重：
  1. `tools/occlusion_audit.py` 的 BOXTITLE 类（盒标题墨迹 vs 自身框界）自检可触发（阳性对照 BOXTITLE=1），新版 8 页 **0 flags**、备份旧版 8 页 **0 flags**。
  2. 新旧对照：p7 SVG 节点 diff 限定于两句 D-2 句；全部盒标题（ERRORI TIPICI、LA PAROLA、LETTERE DEI LETTORI、FRASI DELLA SETTIMANA、LA PROSSIMA SETTIMANA 及各版栏目条）新旧计数一致、文本一致；其余 7 页 SVG 与备份逐字节一致，盒标题无从不同。
  3. 200 dpi 全页目视：全部盒标题完整在框内，无字形被裁、无墨水与另一元素或可见边框重叠。
- 按 STRADDLE 规则：无一盒标题满足任一缺陷条件（被裁 / 重叠 / 与备份不同），故不列缺陷；亦无须列观察项。

## 8. 观察（非阻塞，不构成 D 缺陷）

- **O1 — P5 词汇表换行首出现 `·`。** 词表 `anteprima · protagonista · sede · incontro / · indipendente · lettrice` 第二行以 `·` 开头（核心在 `sede ·` 后换行）。同词、不同断行，KIT §10 已披露为接受项；视觉上仅为轻微排版毛边，无重叠、无错词。非阻塞。
- **O2 — P8-keys 仅 6 px 余量（2546/2552）、P8 答案 9.75 pt。** 均为 KIT §8/§10 已披露的确定性状态（无两行答案、无溢出），符合 SOP §1.1 让步 4 的下限。非阻塞。
- **O3 — P3/P5 中页结构性空白、P6 第 2 栏图前空白。** 核心版式 pattern，KIT §10 已披露。非阻塞。
- **O4 — 标题字号低于 SOP §1.1 阶梯。** 实测：P1 头条 44 px = 33 pt、P2–P6 正文标题 37 px = 27.75 pt、栏目条 46 px = 34.5 pt，均低于阶梯所称头条标题 40–45 pt。此为冻结核心继承的版式（核心 re-proof (a) 已按此版式通过），不在 fan-out 可改范围；本版与核心逐字节一致即为通过。非阻塞，仅记录。
- **O5 — colspill_scan.py 直搬口径过严。** 该脚本不知双栏通栏、通栏带与 `text-anchor=middle` 家具，在本版产出 43 处原始命中，逐项裁定全部为假阳性（与 proof2 日志逐字节相同）。几何权威仍是 `tools/occlusion_audit.py`（0 flags）+ 逐页目视。建议后续把通栏/居中元素排除规则写进工具，非本版问题。

## 9. 方法备注（不修工具，只记录）

- PDF 文字层与 SVG 文本节点的整句计数必须先做空白归一化（全部空白折叠为单空格 + `→` 前后空白归一）：D-2 两句在 PDF 文字层与 SVG 里均跨行/跨节点断开，未归一化会误报 0。归一化后新串各 ×1、旧串 0。
- 本轮复校未重蹈 proof2 O1：run.py/render.py 未在生产副本里跑，全部构建验证走 scratch build-copy（OUT/BASE 改指后 grep 确认 0 处生产路径残留）+ `tools/freeze.py baseline`（自带重定向与防写穿守卫）。生产文件 mtime 未变，三 SHA 收工再验一致。
- 200 dpi 渲染扫描的 P2/P5/P8 亚 1 pt 痕迹与 fix3 §7/§8 的改前值完全相同，属管线系统性特征（PIL 度量与渲染器 advance 差约 0.5–0.8%），本次不修（目视 P2 “Una festa, una giornata verde”完整在界内）。

## 10. Verdict

**(a) 零问题，可定稿。**

未发现 D 级缺陷。上述 O1–O5 均为非阻塞观察（其中 O1–O3 为已披露的接受项；O4 为冻结核心继承；O5 为工具口径说明）。

三件 SHA（与任务书、KIT §7/§12 一致，开工前与收工时两次核对）：

- 印刷 PDF：`640a355a2943efe35b7c1437e1154a4012aa1ec51f18fff155fc7caa4e1c6666`（28,221,020 B）
- 网页 PDF：`4f1bac2c12b8762c187a60647fec578f187f9f5150a2b65cfca31b474f00ee3f`（1,901,668 B）
- 文本导出：`5ac2ecf5abb28bbc9f56c182572a9c7a7e4e93ae8b9c49b5468cc890e0ec16d7`（58,165 B）

门禁汇总：gates.py 19/19 PASS；freeze baseline 本版 8/8 + 核心 8/8；重渲印 PDF 逐字节相同；occlusion 0 flags（新旧两版）；creambox 0 溢出；spill 0；孤儿扫 0；列溢出 0（真溢出）；p8 CLEAN keydiff [137, 138, 139]；P8 最小 9.75 pt；D-2 回归 A/B 全过；P7-only diff 核实。
