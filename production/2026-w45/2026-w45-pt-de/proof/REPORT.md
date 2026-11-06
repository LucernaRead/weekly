# 独立校对报告 — Lucerna Weekly W45 PT×DE（葡萄牙语×德语分版）

**结论：ZERO PROBLEMS（可定稿）**

校对员：独立校对（只校对，不改源码；未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心与 W43 目录——核心与 W43 均为只读对照）。
校对对象：`files/weekly-report-w45-pt-de/`（svg×8、cards×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）。
对照：W45 葡萄牙语核心 `files/weekly-report-w45-pt-core/`；W43 同配对版 `files/weekly-report-pt-de/`（家具以 W43 实测为准）。
工具：`tools/`（`freeze.py`、`p8.py`、`occlusion_audit.py`），一律用 `tools/venv/bin/python` 运行。

## 开工查重

- 首次检查时见一残留 `render.py` 进程（PID 38901），复查时该进程已不存在；交付目录最后写盘为 22:11:17 UTC，22:17:30 之后 90 秒以上复查零新写盘，判定为已完成交付的新鲜 mtime，安全开工，未 stand down。
- 校对前后交付文件哈希全量比对一致（`snapshot-start.sha256` = `snapshot-end-full.sha256`）；核心 8 张 SVG 校对前后哈希不变。

## 交付文件实测 SHA-256（全值）

| 文件 | SHA-256 | 大小 |
|---|---|---|
| svg/p1-capa.svg | 549b96f43dab7d3c4f5c52315c5bcabd8428e7f3eb7ff9af5fb810951157960c | — |
| svg/p2-vida.svg | 5e92ff59d608f1dd3718f073849d4915897acdb882ffbf0702bf2066590c5756 | — |
| svg/p3-cultura.svg | 0ba3634feac423542f36c900f0364fa3671ae98e691ae33d5c3877a02146cb72 | — |
| svg/p4-esporte.svg | 582c9300c5de4c6956980c7377471d477f1c988795c25630c570269703c3466a | — |
| svg/p5-jovens.svg | 8ee31d4239ce22eba7f21c3c8acbbd33a85b43fd4a4a5106936a723a01159a1a | — |
| svg/p6-aprofundamento.svg | e46168afaa3517c4d7f80bc2ab86a127dffafee201cc16d6c09033c1762b8753 | — |
| svg/p7-lingua.svg | 1555d4049bab1f904402effedd129bcc960b2d6dcd8901d3633e7c7a48a3d5a8 | — |
| svg/p8-avaliacao.svg | b8fa5d5df9466e161263b7bcdcdbbd06c01a55c7eaefa12ba006824d9c0f333a | — |
| A-Lucerna-VOL2-DE.pdf（印刷） | a952fcefde109f84ca0fcfc3e7c1981b47184d45432e7b04460b694822a03242 | 3,475,407 B，8 页 |
| A-Lucerna-VOL2-DE-web.pdf（网页） | beea22b7ea91b02e5c0b8304b2710c1154efeae2a808633f921df5e562a59f29 | 3,490,440 B，8 页 |

（构建员交回中的 SHA 为截断形式，本报告不引用截断值；以上为实测全值。）

## 1. 冻结

- `freeze.py baseline`（以 `hidden_files/weekly-report-w45-pt-build/` 为未改动核心构建源）：**8/8 字节复现**，与发货核心 SVG 逐字节一致（p1 0dc8089df727dfe4、p2 56db3aa80e1318db、p3 82f6fc3a94fbc11e、p4 c5647cf6e9c080ec、p5 92e86020ce81f3c8、p6 e6097473ded2f016、p7 a72cb75a519319f4、p8 82630480322959ad，前 16 位；完整值见核心发货文件），exit 0，核心完整性复核通过。
- `freeze.py diff --strict-cjk`：分版每页新增 CJK **均为 0**，分版 CJK 总量 **0**；freeze 口径核心每页 CJK 为 156/177/153/148/223/118/357/1123（与构建员 KIT 一致）。
- 全文残留独立重扫（文本节点，逐页）：中文残留 **0**、全角标点 **0**；英语功能词（the/and/with/from/your/this/that/have/has/will/would/can/should，词界匹配）逐页 **0**。构建员自称三项全部证实。
- 校对前后核心哈希不变（见开工查重）。

## 2. P7 词框冻结

- 词框葡萄牙语定义句逐字保留，与核心逐字节相同、坐标相同：
  `« feriadão »: sábado, domingo e segunda — três dias de descanso.`
- 仅 gloss 本地化为德语：核心 `feriadão = 连休长周末，共三天。` → 分版 `feriadão = langes Feiertagswochenende.`。
- P7 diff（added/removed 全量审读）：新增全部为德语讲解层/家具，移除全部为中文讲解层；**无任何葡萄牙语句子、题干、选项被改动或删除**（定义句、例句、金句葡萄牙语原文均未动）。定义句本地化阻塞项：无。

## 3. P8

- `tools/p8.py compare`：核心 **150 noted**，分版 **150 noted**，状态 **CLEAN**，missing=[]、extra_count=0、uncertain=[]，keydiff=**[2, 4, 101, 137, 138, 146]**。与构建员自称一致。
- **137/138 为真实重定向（PT→DE）**，已对照印刷行核实：
  - 137 题干冻结为葡语 `Domingo, 8 de novembro, é o primeiro dia do Enem. → ___`；键为德语 `Sonntag, 8. November ist Tag 1 des Enem.`，注 `vgl. Seite 6`。
  - 138 题干冻结为葡语 `Confira o cartão antes do domingo. → ___`；键为德语 `Prüfen Sie die Karte vor dem Sonntag.`，注 `confira = prüfen Sie`。
- **150 因 ✓ 分支无 keydiff**，已核实：两版提取键均为 `✓`；分版注已改为德语 `Mustertext in Bereich H auf dieser Seite (93 Wörter)`，§H 行 `Schreibaufgabe (offen); Mustertext (93 Wörter) unten.`；范文段落与核心逐字相同，人工逐词数得 **93 词**。
- **2/4/101/146“核心侧括号分支提取伪影”说法证实**：以印刷 key token（首个 ` — ` 之前）逐字节比对为准——
  - 2：核心印行 `2. portões — portões = 大门（考场大门）`，分版 `2. portões — portões = Eingangstore am Prüfungsort`，key token 均为 `portões`；
  - 4：核心 `4. 13h30 — 13h30 开考（巴西利亚时间）`，分版 `4. 13h30 — 13h30: Prüfungsbeginn, Brasília-Zeit`，key token 均为 `13h30`；
  - 101：核心 `101. confiro — conferir：eu → confiro（不规则）`，分版 `101. confiro — conferir: eu confiro, unregelmäßig`，key token 均为 `confiro`；
  - 146：核心 `146. A — seção = 考场分区（房间）`，分版 `146. A — seção = Prüfungsraum, Sektion`，key token 均为 `A`。
  伪影确在核心侧（p8.py paren 分支误取含全角尾括号组的长 key），分版 key 正确，无分版缺陷。
- **P8 答案注释为纯德语**：答案注行（key 区）含 ASCII `(` 的仅 1 行，即 150 行；除 150 外全部 P8 注释无括号的说法在“注释行”口径下证实（见“与构建员自述不符处”第 2 条关于全页口径的说明）。全页 CJK=0、全角标点=0。
- 139/140 键与核心逐字节相同（`O feriadão é de 31 de outubro a 2 de novembro.` / `Quando você chegar, apresente o documento com foto.`），题干改为德语，符合 DE→PT 重定向。

## 4. 几何遮挡

- `tools/occlusion_audit.py`（自检 6 类全触发，干净对照静默）：**分版 0 flags · 核心 0 flags · NEW 0**，exit 0。
- 同基线墨迹碰撞扫描：P2–P8 为 0；P1 仅目录行一处正间隙（见下）。
- P6 图表标签基线锚定墨迹法（PIL getbbox，anchor `ls`，与后续矩形求交）：`portões abertos` **0.0%**、`espera` **0.0%**、`prova` **0.0%**，均 <30%，通过；卡片上三标签+数值全部可读。
- 全部 8 页页框压线与右缘扫描（自写 PIL 墨迹扫描：页边 0..1950×0..2700、内框 40..1910×40..2660、框线 x=28/1922/40/1910、y=28/2672/40/2660）：**8 页 0 违规**。EDGE 类盲区（NL×RU 副标题压框、NL×PT 框线压字模式）已显式覆盖，无漏检。
- P1 顶栏（y=92）：分版墨迹间隙 **224.5px / 94.2px**，与构建员称 224px/94px 一致（取整），无重叠。
- P1 目录行 1.7px 间隙：实测坐标与核心**完全相同**（`Finados, o dia da memória` x=1539、y=1436、20pt；`A2→B1` x=1863 end、y=1436、18pt；墨迹右界 1797.75、左界 1799.71），为核心 KIT 已登记的保留项，正间隙、无重叠；PIL 墨迹法测得间隙约 1.96px，与构建员 1.7px 之差为度量取整/超采样口径差（见不符处第 3 条），不阻塞。

## 5. 修复部位终版几何（全部实测）

- P7 金句末行距预告框：末译文墨迹底 **2392.2**，预告框顶 **2404.0**，间隙 **11.8px**（构建员称约 10.8px，见不符处第 4 条；通过且有余量）。
- P8 各栏底线余量（最低键基线 → y=2580 规则线）：65 栏 **56.7px**、527 栏 **43.6px**、989 栏 **45.3px**、1451 栏 **47.9px**，与构建员称 56.7/43.6/45.3/47.9 逐项一致，每栏 ≥40px。
- P1 词条余量：`„Feriadão“ = langes Wochenende, drei Tage.` 墨迹底 1820.9，规则线 y=1844，余量 **23.1px**，与构建员称一致。
- Round 3 的 P7 生词框拉丁下伸笔画 1.1px 压框修复：词框底 **1290.5**，注文墨迹底 **1283.6**（框内余量 6.9px，无压框）；信框顶 **1304.5**（词框间距 14.0，确为 −8 补偿）；栏底 **1822.5 不动**；卡片目视确认无压框、无栏底移位。`content7.py` 中两处常量确已落地（`+ 28`、`ly = wy + wh + 14`）。
- Round 1 的 13 个 NEW 标记终版消除：终版 occlusion **NEW 0**；P8 148/149/150 基线分别为 **2472.82 / 2502.48 / 2532.14**，各行独立，无同基线堆叠；卡片目视 P8 键区行行分明。
- 终版构建警告：`build-run3.log` 与 `build-render3.log` 中 FLOW OVERFLOW **0**、HEAD TOO WIDE **0**（run1 的 3 条 P8-keys 溢出为 Round 1 已修复的历史记录，非终版）。

## 6. gloss 计数与金句

- 按渲染源 `gloss()` 字符串本身拆 `·` 逐项计数（页归属以调用位置核实：content12:178 在 P2-flow 之后；content34:21 为 P3、:128 为 P4；content56:28 为 P5、:130 为 P6）：
  - P2 **6=6**、P3 **6=6**、P4 **5=5**、P5 **5=5**、P6 **4=4**，合计 **26=26**，与核心逐项 1:1（P3 为 6、P6 为 4，确为葡萄牙语核心自身分布，未套用他族 5/5）。
- P7 金句 8 条各逐字出现 **2×**（源文章 + P7），与核心一致；页码标签与核心一致，且每句在其标注页上实测存在：Página 1 ×2（`Do feriadão à prova: a semana do Enem`、`Muita gente viaja, visita a família e vai ao cemitério levar flores`）、Página 2 ×2（`Finados é o dia da memória`、`Confira o cartão, durma bem, chegue cedo`）、Página 3（`lembrar é um jeito de continuar perto`）、Página 4（`cada ponto vale uma posição, cada gol vale uma história`）、Página 5（`quem dorme bem lembra melhor`）、Página 6（`primeiro as fáceis, depois as difíceis`）。
- P7 短语逐字取自本期文章：8 条金句均在源文章页实测存在（上列页分布即为实测结果）。

## 7. 读者园地（零编造）——独立裁定：通过

页上同时具备三事实：

1. **截稿时无真实来信**——葡萄牙语披露句原文保留：
   `Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3.`
   德语披露句同义：
   `Anmerkung: Echte Briefe und beste Texte kamen bis Redaktionsschluss nicht an — Beispiel bleibt, Versprechen gilt für VOL.3.`
2. **无最佳 P8 作文**——同一两句披露句明言“最好的文本”（melhores textos / beste Texte）截稿时未到，承诺顺延至 VOL.3。
3. **示例 + VOL.3 承诺**——示例同时标注 `EXEMPLO DA REDAÇÃO` 与 `Beispiel der Redaktion.`，无任何编造的读者、姓名或引言。

显性德语邀请（祈使句 + 刊登承诺，原文逐字）：
`Schreiben Sie uns! Beste Briefe erscheinen in VOL.3.`

**关于“最佳作文征集是否显性表达”的显性判定：通过，理由如下。** 邀请句字面只提“最佳来信”（Beste Briefe），但第 8 页最佳作文的征集在**同一页他处有显性表达**，不依赖对邀请句的扩大解释：
- 德语披露句本身即为最佳文本的顺延承诺（`beste Texte … Versprechen gilt für VOL.3`）——承诺刊登即征集的显性表达；
- 同页预告框（葡萄牙语，目标语正文）明言下期内容：`Mais: as suas cartas e os melhores textos da página 8.`——明确点名“第 8 页的最佳文本”将在下期刊出；
- 通用祈使句 `Schreiben Sie uns!` 覆盖一切寄件（含作文投稿）。
三者合起来，读者在 P7 一页内即被明确告知：可寄信、可寄第 8 页作文，最佳者见 VOL.3。现行邀请门（页上须有真实来信的显性公开邀请 + 三事实）满足，**不构成阻塞**。
非阻塞观察：若将德语邀请句补为 `Beste Briefe und Texte erscheinen in VOL.3.`，则德语单句本身亦完备；现版已通过，不必为此返工。

## 8. 家具（与 W43 同配对版 SVG 逐属性对照）

- P8 分隔符：分版 8 处均为 `— PÁGINA n —`，与 W43 实测（8 处同式）一致，**非** tables.json 的 SEITE 形式；构建员称沿用 W43 实测证实。P8 副标题 `SEITE 8 · A grande prova da semana + todas as respostas` 与 W43 同式逐字一致。
- P2 band 副标题：保留葡语半句并追加德语半句——
  `NÍVEL A2 · Finados e revisão: o feriadão do Brasil · Finados und Wiederholung: das lange Wochenende in Brasilien`，
  与 W43 模式（葡语半句 + 德语半句、右对齐 x=1872）一致；墨迹 850.9–1871.9，宽度 1021.0px，**在版心内**（右界 <1910 内框）。
- P1 徽章：与 W43 逐字、字号（19pt bold）、坐标（y=372）相同，墨迹宽 **962.2px**（W43 同值；构建员称 962.3 为取整差），居中。
- P7 词框/信框两处常量微调：`+28 / +14` 已落地（见 §5），几何无劣化（词框内余量 6.9px、栏底不动、终版 occlusion 0）。
- 137 键：长度修剪后的德语短式 `Sonntag, 8. November ist Tag 1 des Enem.`——日期（8. November）、事件（Tag 1 des Enem）齐全的完整句，无歧义；注 `vgl. Seite 6`；题干葡语冻结（见 §3）。
- P8-A 115 注与 P2 时间框共用译文：P8 115 注 `13:30 Uhr: Beginn` 与 P2 时间框 `13:30 Uhr: Beginn` **逐字一致**。
- 134 注：仅 P8 内缩写为 `S + V + O + Ort`（content8 专属后处理）；P3 正文（content34 #45 练习注）保持全式 `Subjekt + Verb + Objekt + Ort`，且 P8 #45/#46/#136 注亦保持全式。核实通过。
- 副标题 34pt 线宽：实测墨迹宽 **1743.0px ≤ 1820**（构建员称 1742.9 为取整差）；W43 副标题同为 34pt（其文本墨迹宽 1793.2px），字号对照一致。
- 页脚：8/8 标 VOL.2，左 `A Lucerna · PORTUGIESISCHE WOCHENZEITUNG VOL.2 · TEXT AUF PORTUGIESISCH · ERKLÄRUNGEN AUF DEUTSCH`，右 `Seite N von 8`。

## 9. 图片/署名

- 全期仅 1 张照片：P1 图书馆复习图（`<image>` 唯一，x=65、y=1874、896×320），卡片上确实排版在位；署名行在位：`Foto: Gary Todd / Wikimedia Commons — CC0`。
- 嵌入 payload 与核心一致：解码后 JPEG 字节 md5 **04b18fa952a61c9998ef5bf3325341f2**（分版 = 核心 = 两边 `assets/estudo.jpg`，256,737 字节）。构建员 KIT 所载 `7e6fa99b…` 为 base64 文本本身的 md5（实测复现一致），口径不同而非数值不符（见不符处第 1 条）。
- 其余为自制图表（P1 时间表、P2 时间框、P4 赛程表、P6 分钟条形图 + 两周日表），无新增照片。

## 10. 复现性（独立 scratch 重渲染）

- 在自有校对目录 `hidden_files/w45/pt-de-proof/repro/`（未碰共享 scratch）中：全新核心复制 + `transform.py` 单独重跑，exit **0**，256 条 OK、无 MISS、无失败，残留 CJK 源码行 0；随后 `run.py` 重渲染 exit **0**，零警告，注册表与核心一致（150 题；A2 49 / B1 70 / B2 31；分版 10/18/18/18/18/18/12/38；题型 完成句子 61 / 单选 49 / 配对 12 / 造句 7 / 判断 3 / 完形 13 / 翻译 4 / 写作 1）。
- **8/8 SVG 与交付版字节一致**（p1 549b96f43dab7d3c、p2 5e92ff59d608f1dd、p3 0ba3634feac42354、p4 582c9300c5de4c69、p5 8ee31d4239ce22eb、p6 e46168afaa3517c4、p7 1555d4049bab1f90、p8 b8fa5d5df9466e16，前 16 位；完整值见 §“交付文件实测 SHA-256”）。构建员复现说法证实。
- 复现过程未写交付目录：复现前后交付哈希全量一致（见开工查重）。

## 11. 其他

- ABSTRACT.txt：德语**单行**（1 行，373 字节），无 ASCII 双引号，含真实主题关键词（Enem-Prüfungswoche、Finados-Feiertag 2. November、Enem-Tag 8. November、Copa do Brasil）+ 学习者搜索短语（`Portugiesisch lernen mit brasilianischen Nachrichten, Enem-Wortschatz und Pretérito Perfeito`）。
- 8 张卡片**逐页目视检查完毕**（p1–p8 全部看过）：无重叠、无截断、无压框、无页脚压线。P1 照片与署名在位；P7 词框/信框/金句区/预告框间距清晰；P8 四栏键流齐整、148/149/150 各行独立。
- 两 PDF 各 8 页，尺寸与任务书一致（印刷 3,475,407 B、网页 3,490,440 B）。

## 与构建员自述不符处（全部非阻塞，不影响结论）

1. **照片 md5 口径**：KIT 所载 `7e6fa99b846ad620c84eb989452c52d4` 是 base64 文本的 md5，不是解码后 JPEG 字节的 md5（后者为 `04b18fa952a61c9998ef5bf3325341f2`）。两种口径下分版与核心均一致，照片同一性成立。
2. **P8 括号表述的口径**：KIT“P8 lines containing `(` 恰为 1 行”仅在“答案注释行”口径下成立；全页口径下，冻结的葡语题干（如 `(A. o primeiro dia · …)`）与 §H 德语行 `Schreibaufgabe (offen); Mustertext (93 Wörter) unten.` 也含括号。题干为冻结葡语、§H 行为德语装置行，均非 P8 注释，不影响 p8.py（仅解析键行），不阻塞。
3. **P1 目录间隙数值**：PIL 墨迹法测得约 1.96px，构建员称 1.7px；坐标与核心逐值相同、正间隙、无重叠，差值为度量口径差。
4. **P7 金句末行间隙数值**：PIL 墨迹法测得墨迹底 2392.2 → 间隙 11.8px，构建员称约 10.8px（墨迹底约 2393）；通过且有余量，差值为度量口径差。
5. **若干取整差**：徽章宽 962.2（称 962.3）、副标题宽 1743.0（称 1742.9）、顶栏间隙 224.5/94.2（称 224/94），均为四舍五入/超采样口径差。
6. **核心 CJK 总量口径**：本校对文本节点扫描得核心每页 140/164/139/137/195/109/299/1048，与 freeze 口径 156/177/153/148/223/118/357/1123 不同；分版在两种口径下均为 0，冻结结论不受影响。

## 非阻塞观察（注明不阻塞）

- P3 右上 `A SEMANA, DIA A DIA` 框内末行 `Dom 8 — Enem, dia 1; Vasco × Palmeiras, a volta.` 视觉上贴近框底，但墨迹在框内、occlusion BOXTITLE 干净，不阻塞。
- P2 `E VOCÊ?` 框称最佳文本见 P7《读者来信》栏，与 P7 的征集表达相互印证（跨页佐证；P7 本页证据已足够，见 §7）。
- 德语邀请句若补“und Texte”则单句更完备（见 §7），现版已通过，不必返工。

## 校对过程合规声明

- 未清理共享 scratch 目录（所有中间文件均在自有 `hidden_files/w45/pt-de-proof/` 内：diff.json、p8.json、occlusion.json、geom.txt、audit1–3、freeze-baseline/、repro/ 及快照文件）。
- 未宣布上架以外的任何投递动作；本报告仅为校对结论，供主线决定是否定稿/入库。
