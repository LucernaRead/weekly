# PROOF-NOTE-2 — W47 it 家庭第二轮独立重校

- **校对员**：第二轮独立重校员（与建造者、修复者均不同；SOP §8/§8.4「另派」要求）
- **日期**：2026-11-12
- **范围**：W47 意大利家庭全部 11 版（core-it + 2026-w47-it-{en,de,fr,es,pt,nl,ru,ja,ko,zh-tw}），从头全量重校，非仅查已修项
- **依据**：`~/workspace/weekly-git/SOP.md` 全文（重点 §8）；第一轮 `scratch-reproof-w47-it/PROOF-NOTE.md` 全文；修复记录 `scratch-fix-it/FIX-LOG.md` 全文
- **工具**：`~/workspace/weekly-git/tools/`，HEAD `b06cb15e`（第一轮时为 `b9ac29a6`，门禁已在当前 HEAD 下全部重跑）；解释器 `tools/venv/bin/python`
- **磁盘**：开工 94G，收尾 95G（<100G 门限；增长为本轮渲染的 44 张 PNG + 门禁输出）
- **只读**：未修改任何生产文件；生产文件 SHA 与 FIX-LOG §2 逐项核对一致（33/33）；收尾抽查 5 个 SHA 仍一致；run.py 在 scratch 副本中重跑

## 总体结论：有问题——2 处 low 级发现，均不阻塞内容正确性

**发现总数 2；严重度：MAJOR 0，MEDIUM 0，low 2。** 第一轮的 6 项（F-1、F-2、F-3、F-4、F-5、core-1）及 Q136 补全、R-1 补偿均已核实到位；11 版机械门禁全部 ALL-GREEN（见下表）。

但按 SOP §8「proofread-until-zero」硬门，零发现轮次方能定稿——本轮仍有 2 处 low 级新发现（R2-1、R2-2，均在 core-it 与 it-zh-tw），故本轮**不是**零发现轮次。两处均为化妆品级（不影响事实、答案、阅读），建议修复后由下一轮确认，或由协调员裁定接受。

## 发现表

| # | 严重度 | 位置 | 证据原文 | 说明 |
|---|--------|------|----------|------|
| R2-1 | low | core-it、it-zh-tw P4 赛果标题行 | `I RISULTATI DELL'11ª GIORNATA　第 11 轮赛果（6–8 novembre）`（两版 text.md 均为 L445；zh-tw：`第 11 輪賽果（6–8 novembre）`） | 中文标题括号内月份 `novembre` 未译成中文。ja 已全本地化（`第11節の結果（11月6〜8日）`），ko 已全本地化（`11라운드 결과（11월 6~8일）`）。fr 的 `6–8 novembre` 是法语正确写法，不属此问题。 |
| R2-2 | low | core-it、it-zh-tw 配对题注释（练习行 Q25–28、Q52–55、Q141–144 + 答案行，共 24 处/版） | `25. la salute — stare bene, la prima ricchezza (key c · salute=健康 c)`；答案行 `25. c — salute=健康 c`；同型 `vetta=榜首 d`、`ponte votivo=还愿桥 b`、`manovra=预算法案 d` 等 | `=` 两侧无空格、无逗号，与 ja/ko（`salute = 健康 c`）及全部拉丁版（`salute = health, c`）不一致。两版内部自洽（24 处统一格式），可读，不影响答案。 |

## 修复核实（第一轮发现逐项复核，全部到位）

| 修复项 | 核实方法 | 结果 |
|---|---|---|
| F-1 五版副标撞日期 | PyMuPDF 逐词量 P1 y=69 行：副标最右 x1 vs 日期 `SETTIMANA` 左缘 x0；en/ru 目视 P1 顶部截图 | en 114.1pt、fr 92.4、pt 97.8、nl 91.6、ru 111.4——全部 ≥91pt。新副标在位：`EVERY WEEK IN ITALIAN` / `CHAQUE SEMAINE EN ITALIEN` / `TODA SEMANA EM ITALIANO` / `ELKE WEEK IN HET ITALIAANS` / `КАЖДУЮ НЕДЕЛЮ ПО-ИТАЛЬЯНСКИ` |
| F-2 时间线 MAR 行 | P6 文本层 + SVG 坐标 | 11 版 P6 文本层均含 `NOV.` + `Scade`（ru 为换行拆分 `MAR 17 NOV.\nScade il termine`，属提取换行，非缺失）。SVG：label x=1461.5，body x=1611.5，间隙 ≈10px |
| F-3 模板全角冒号 | text.md 全版 grep + 全部 SVG grep | 11 版 text.md 0 处；11 版 SVG 全角 0 处、半角 7 处/版 |
| F-4 盒标题改回「记住」 | text.md + P2 SVG grep + boxtitle 门 | 11 版均为 remember 类：LEARN、MERKE、`À RETENIR`、RECORDAR、PARA RECORDAR、OM TE ONTHOUDEN、ЗАПОМНИТЕ、覚えておこう、기억해、請記住、请记住；旧词 DEVISE/LEMA/LEUS/口訣/口诀在 11 版 PDF 文本层中 0 次 |
| F-5 Q44/Q134 注补全 | text.md 全版 grep | 11 版 Q44、Q134 注均含主语+动词+地点+日期（如 fr `Sujet + verbe + lieu + date`） |
| Q136 注补全 | text.md 全版 grep | 11 版均完整，含 nl（`Onderwerp + werkwoord + plaats`）、ru（`Подлежащее + глагол + место`） |
| core-1 页脚与摘要 | PDF 文本层 + ABSTRACT.txt | core-it 页脚 `LUCERNA ITALIAN WEEKLY` 出现 0 次；8 页页脚均含 `正文意大利语　讲解简体中文`；摘要含 `意大利语正文与简体中文讲解，A2–B2` |
| R-1 ru P8 流溢出补偿 | 独立重跑 run.py（scratch 副本）+ 目视 ru P8 底部截图 | ru `flow[P8-keys] ended col 3/3 y=2543 (bottom 2552)`，0 FLOW OVERFLOW；P7 桥段完整术语仍在（`После è probabile che / è possibile che / bisogna che — сослагательное наклонение`）；被缩短的两处注（P6 Q94、P7 Q110）现为 `è possibile che + сослагательное nevichi`，答案行内通顺；Q93/Q96/Q109/Q111 仍保留完整 `сослагательное наклонение` |

## 全量重校（非仅已修项）

- **通读**：it-en text.md 全文 1317 行；其余 10 版全部 diff 行（de 398、fr 397、es 398、pt 400、nl 397、ru 401、ja 401、ko 401、zh-tw 401、core 401）逐行读完。讲解层翻译、术语、答案 1–150 均与题干/正文/图表一致（抽查含 Q85 13−11=2、Q86 6+7=13、Q93–96 虚拟式、Q137–140 翻译、Q150 范文 99 词——脚本数词确认）。
- **引文逐字**：P7「本周金句」8 条与 P1–P6 正文逐字核对一致（含 `«ventiquattro gol in dieci partite»`——P1 文本层因换行拆行，初查误以为缺失，已核实原文在位）。
- **事实外查**（2026-11-12 检索）：BookCity Milano 2026（23–29 Nov、第 15 届、主题 `Il senno sulla Luna`、1,360 事件/2,487 人物/443 场地）、Festa del Torrone（第 29 届、7–22 Nov、主题 `Il Confine`、1441 年 Sforza–Visconti 婚礼重演、逾 150  figuranti）、Eurochocolate（第 32 届、13–22 Nov、Perugia、主题 `Fate dolci`）、Torino Film Festival（第 44 届、24 Nov–2 Dec）——四项均与刊物一致。
- **引号普查**：11 版 text.md 均无 ASCII 直引号；弯引号成对且合乎各语惯例（en “…” 3 对、de „…“ 3 对、fr/es/pt «» 55 对、ru «» 126 对）；«» 全版成对（52/52 至 126/126）。
- **摘要**：11 份 ABSTRACT.txt 全读，均为读者母语，含 VOL.4、A2–B2、150 道练习与真实要点（Lazio 29 分、两节周日闭幕、Salute、植树节、BookCity、TFF、预算法案），无「用新闻学 X」类表述。
- **text.md 与 PDF 一致性**：5 处旧漂移行（es L45/L205、ru L45、ko L45/L205）现与 PDF 文本层一致；P1 头条 `La Lazio resta in vetta` 在 11 版 P1 文本层均在位。

## 已核查并排除的疑点（不计为发现）

- **it-ja P8-keys 流末 y=2561（bottom 2552）**：run.py 光标超出软性底线 9px，但无 FLOW OVERFLOW 警告；PDF 实测末行答案基线 y=1908.9pt、页脚基线 y=1968pt，间隔 59pt，目视 P8 底部截图第 150 题完整、无裁切、无页脚碰撞。修复工自己的日志亦为 2561，p8 提取 150/150。属流光标假象，非可见缺陷。
- **P8 栏目标题意大利语残留**：`La grande prova della settimana + tutte le risposte` 在 11 版均未译，但 `Page 8` 标记本身已本地化（Seite 8 / Página 8 / 8ページ / 第 8 版等），属模板统一样式，不计。
- **es Q55 `debutto = debut, a`**：`debut` 为西班牙语中已使用的外来词，与 en 相同但不构成错误。
- **it-ru census `noto_sans_elements=777`**：已知的跨家 D5 系统性问题（拉丁标题用 Noto Sans 而非 Newsreader），按任务要求不报；it-ru 内容照常校对，D5 核心计数 0/0/0。
- **不重报项**（FIX-LOG 已裁定）：it-de P1 间隙 5.0pt（末词 LIEST 右缘 1064.3，日期左缘 1069.3）、it-zh-tw cifre 标题余量 +0.5px、CJK 手写变体块、it-ko 印/网文本层 1 个空白字符差（multiset_diff=1，nonws_diff=0）、fr `Cette sem.`、ru `СОДЕРЖ.` 等缩写。

## 逐版结论

| 版 | 结论 |
|---|---|
| core-it | 通过，带 R2-1、R2-2（low） |
| it-en | 通过，无发现 |
| it-de | 通过，无发现 |
| it-fr | 通过，无发现 |
| it-es | 通过，无发现 |
| it-pt | 通过，无发现 |
| it-nl | 通过，无发现 |
| it-ru | 通过，无发现（R-1 已核实；字体系统性问题不在本轮范围） |
| it-ja | 通过，无发现（2561 流末已核实无可见影响） |
| it-ko | 通过，无发现 |
| it-zh-tw | 通过，带 R2-1、R2-2（low） |

## 逐版门禁结果（tools HEAD `b06cb15e` 下独立重跑）

| 版 | run.py | occlusion | p8 extract / compare | D5 census | boxtitle | spill | edge | 印/网文本层 |
|---|---|---|---|---|---|---|---|---|
| core-it | TOTAL 150，0 溢出，0 HTW；P8-keys 2499/2552 | 0 flags | 150/150；compare 跳过（自身） | 0/0/0；弯引号 4/4 Newsreader | 24 题 320 行，0 DEFECT | 29 盒 101 候选，0 SPILL | 0 TOUCH 0 NEAR；P8 底距 55.8pt | 差 0 |
| it-en | 150，0，0；2514 | 0 | 150/150；CLEAN，keydiff=[137,138,139] | 0/0/0；4/4 | 18/256，0 | 29/69，0 | 0/0；53.6 | 差 0 |
| it-de | 150，0，0；2514 | 0 | 150/150；CLEAN，keydiff 同上 | 0/0/0；2/2 | 22/259，0 | 29/71，0 | 0/0；56.5 | 差 0 |
| it-fr | 150，0，0；2529 | 0 | 150/150；CLEAN，keydiff 同上 | 0/0/0；0 | 20/248，0 | 29/68，0 | 0/0；53.6 | 差 0 |
| it-es | 150，0，0；2543 | 0 | 150/150；CLEAN，keydiff 同上 | 0/0/0；0 | 20/249，0 | 29/70，0 | 0/0；53.6 | 差 0 |
| it-pt | 150，0，0；2543 | 0 | 150/150；CLEAN，keydiff 同上 | 0/0/0；0 | 22/247，0 | 29/68，0 | 0/0；53.6 | 差 0 |
| it-nl | 150，0，0；2543 | 0 | 150/150；CLEAN，keydiff 同上 | 0/0/0；2/2 | 22/252，0 | 29/68，0 | 0/0；53.6 | 差 0 |
| it-ru | 150，0，0；2543 | 0 | 150/150；CLEAN，keydiff 同上 | 0/0/0；0（noto_sans 777，系统性问题，见上） | 26/320，0 | 29/69，0 | 0/0；53.6 | 差 0 |
| it-ja | 150，0，0；2561（已核实无可见影响） | 0 | 150/150；CLEAN，keydiff 同上 | 0/0/0；0 | 24/341，0 | 29/107，0 | 0/0；55.8 | 差 0 |
| it-ko | 150，0，0；2546 | 0 | 150/150；CLEAN，keydiff 同上 | 0/0/0；4/4 | 36/493，0 | 29/177，0 | 0/0；55.8 | 差 1（仅空白字符，nonws 差 0，已知噪声） |
| it-zh-tw | 150，0，0；2499 | 0 | 150/150；CLEAN，keydiff 同上 | 0/0/0；4/4 | 24/325，0 | 29/102，0 | 0/0；55.8 | 差 0 |

注：keydiff=[137,138,139] 为三道翻译题的读者母语译文差异，属设计差异（第一轮已确认）；boxtitle/spill/edge/occlusion 数字为门禁工具输出；P8-keys 末值单位为渲染坐标，底线 2552。

## 产出与证据位置

工作目录 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof2-w47-it/`：
- `PROOF-NOTE-2.md`（本文件）
- `gates2.sh`（门禁脚本）、`logs/`（run-*.log、gates-*.log、measure-f1*.log）、`gates/<版>/`（occlusion/p8/census/boxtitle/spill/edge JSON 与日志）
- `diff-<版>.txt`（各版 vs it-en 的 text.md 差异行）、`runs/<版>/`（run.py scratch 副本）
- `pages/`（P1/P2/P6/P8 渲染 PNG 44 张 + P1 顶部与 P8 底部特写）
