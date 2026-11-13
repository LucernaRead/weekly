# 独立校对笔记 — W47 意大利文核心版 · 第二轮全文复校 (2026-w47-it-zh-cn, VOL.4)

- 校对员：叶子（独立校对，未改任何 core-it 文件与 tools/p8.py；只读）
- 校对时间：2026-11-10 晚（返修后最终重建 21:59–22:01）
- 校对对象：`~/workspace/weekly-git/production/2026-w47/core-it/`
  - 印刷 PDF `La-Lucerna-VOL4.pdf`（8 页，27,726,384 字节）
  - 网页 PDF `La-Lucerna-VOL4-web.pdf`（8 页，1,758,563 字节）
  - KIT `WEEKLY-KIT.md`（27,982 字节），`2026-w47-it-zh-cn.text.md`（52,729 字节、1317 行），`ABSTRACT.txt`，`svg/` 8 个
- 结论：**(a) 零问题 — 定稿**。第一轮 4 项缺陷逐项验证全部修好、未修坏别处；次要观察全部落实；全量复校未发现新缺陷。
  下方另列 4 条次要观察（系统性/既有惯例，非本轮缺陷，详见末节，供父线裁定）。

## D1（硬）P4 配对 53/54 — 已修好，三重验证一致
- 源码：`content34.py` match_set keys 为 `["d", "b", "c", "a"]`，notes 为 `imbattuto=不败的 b`、`girone=小组 c`。
- 渲染图 P4（自交付 PDF 渲染，非 builder 卡片）：左列 52. la vetta / 53. imbattuto / 54. il girone / 55. il debutto；右列 a. la prima volta in un torneo importante / b. che non ha mai perso, ancora senza sconfitte / c. il gruppo di squadre che giocano tra loro / d. il primo posto in classifica, la cima。53→b、54→c 正确。
- P8 印出键：自写脚本比对（见下“P8 答案”节）53=b、54=c；渲染图 P8 RISPOSTE「53. b — imbattuto=不败的 b」「54. c — girone=小组 c」目视一致。
- 其余两组配对未受影响：P2 25–28（c/b/d/a）与 P6 141–144（d/c/b/a）逐项核对正确，P8 印出键与之相符。

## D2（硬）P4 第 11 轮赛果表星期分组 — 已修好
- 渲染图 P4 表（5 行）：VEN 6.11 仅 `Venezia – Udinese 2–1`；SAB 7.11 为 `Cagliari – Frosinone 1–0`、`Torino – Lecce 1–1`、`Parma – Bologna 1–2`、`Roma – Sassuolo 3–0`；DOM 8.11 为 `Napoli – Lazio 1–1`、`Genoa – Milan 1–2`、`Monza – Atalanta 0–1`、`Inter – Como 2–0`、`Fiorentina – Juventus 2–2`。其余 10 场比分、24 球（逐场相加 3+1+2+3+3+2+3+1+2+4=24）、积分榜（Lazio 29 / Inter 28 / Roma 27 / Milan 24 / Como 23 / Udinese 末位 5）未动。
- 事实独立核实（本次检索，多源一致）：Cagliari–Frosinone 1–0 与 Torino–Lecce 1–1 均在**周六 11 月 7 日 15:00**踢——ilovepalermocalcio.com（2026-11-07 16:12 刊）、ilquaderno.it / Adnkronos（“oggi, sabato 7 novembre”）、sportradar.com（Saturday, 7 November 2026, 9:00 AM EST = 15:00 CET）、labaroviola.com、ledicola.it；附带印证积分：Cagliari 16、Frosinone 20、Torino 14、Lecce 10，与 KIT 表一致。
- 同一单元格内两场比赛分隔符确为全角空格（渲染图 DOM 行 `Genoa – Milan 1–2　Monza – Atalanta 0–1`，无 `·`）。
- 小注：SAB 7.11 与 DOM 8.11 的日标签各在两行重复出现（5 行布局所致），准确可读，与 KIT “5 行”描述一致，属版式细节，不列缺陷。

## D3（硬）都灵电影节日期 — 已修好，6 处 + ex 120 全部核实
- 来源独立核实（本次检索）：FilmFreeway 规程（2026-03-06 更新，英意双语一致）：“The 44th Torino Film Festival will be held from Tuesday, November 24th to Wednesday, December 2nd, 2026, for a total of nine days.” / “Il 44° Torino Film Festival si svolgerà da martedì 24 novembre a mercoledì 2 dicembre 2026, per la durata di nove giorni.”；torinofilmfest.org 规程页逐字相同；Cineuropa 2026-11-06：“from 24 November to 2 December”。（附带：dolcevia.com 的 FAQ 仍写错的 “begins on 20th November”，但其自家活动页日期为 11-24 至 12-02——错日期在聚合站流传，官方口径无歧义。）
- 6 处改动在渲染图/文本中逐项确认：(1) P1 LA SETTIMANA VEN 20 改为 Eurochocolate「I tesori della Calabria Straordinaria」18.15（见下事实核查）；(2) P5 标题「il cinema torna a Torino」；(3) P5 正文「E martedì 24 novembre, a Torino, apre il Torino Film Festival, la 44ª edizione, fino al 2 dicembre: nove giorni…」（11-24 至 12-02 含首尾共 9 天 ✓）；(4) P5 IL PIANO 第 1 条改为周五巧克力节；(5) P5 I GIOVANI IN NUMERI「dal 24 novembre al 2 dicembre, 44ª edizione」；(6) 练习 81 题干「apre il 24 novembre」，键 Vero。
- ex 120 重出核实：P8 印出「Il Torino Film Festival apre... A. il 20 novembre · B. il 24 novembre」，键 B；两选项仅 B 正确（24 日开幕属实，20 日为门票优惠期首日、非开幕），键为 B ✓。
- 「8 dicembre」：text.md 0 次、svg/ 0 次、PDF 文字层 0 次 ✓。
- 「20 novembre」4 处（text.md grep）：P2 castradina 前夜（“si mangia la sera prima, il 20 novembre”）、练习 23 干扰项 B、练习 66 干扰项 A、练习 120 干扰项 A——4 处均合法。注：SVG grep 仅 3 次、PDF 文字层 grep 仅 3 次，因 P2 一处在 SVG/文字层中跨行断开（“il 20 / novembre”），内容本身存在，非缺失。

## D4（系统性）SOP §1.1 视觉规范 — 已迁移，成品实测逐项通过
- 源码：`svglib.py` 与 core-en 的 `diff` 为空（逐字节相同）；`assets/lucerna-moth.svg` 与 core-en 的相同；`bslib4.py`：PAPER `#fbfaf6`、INK `#302c28`、GREY `#6f675d`、LINE `#d8d2c4`、CLOTH `#37402f`、OLIVE `#46581f`、GOOSE `#f6e08e`、ONCLOTH `#f4efe1`、徽章 `LV_COLOR = {"A2": "#5c6e30", "B1": "#46581f", "B2": "#37402f"}`，与 §1.1 表精确一致；无双线外框代码（单页纸色 rect + 细线 hline）。
- SVG grep：旧色 `#f7f1e2/#b3a06a/#a4553a/#2c2822` 8 文件全 0；新色齐全（`#fbfaf6` 10、`#302c28` 1435、`#6f675d` 240、`#d8d2c4` 9、`#37402f` 39、`#46581f` 379、`#f6e08e` 9、`#f4efe1` 17、`#5c6e30` 44、`#f0eee5` 29）。
- 字体（pdffonts 独立验证）：印刷版含 `Newsreader16pt-Regular`（已嵌入，子集化），网页版含 `LucernaNewsreader-Regular`（已嵌入）；刊头 `UnifrakturMaguntia` 已嵌入；CJK 为 Noto Sans/Serif CJK SC（见次要观察 2）。
- 分隔符：`VOL.4 ·` / `· VOL` 在 SVG 中 0 次；页脚「La Lucerna　意大利语周报 VOL.4　LUCERNA ITALIAN WEEKLY」+「第N版／共8版」为全角空格分隔，刊头、栏目条同为全角空格。`·` 残留共 148 个，逐处分类：109 个为练习选项分隔符（`A. … · B. … · C. …`），39 个为词表内部（讲解/译注词串与 P3/P5/P6 词框，如 `torrone · cioccolato · corteo · …`）——全部在内容内部，家具位置确无 `·`，与已通过的英文版惯例一致。
- 刊头实测（P1 渲染图）：哥特体 La Lucerna 居中，刊头下单道橄榄绿线、三色蛾居中落在线上，书衣绿带 + 副标，无双线外框 ✓。
- P8 答案字号独立核实：PyMuPDF 取印刷版 P8 最小字号 **9.75 pt**（534 个 span），恰为 SOP §1.1 下限，不低于下限 ✓。

## 次要观察 — 全部落实（渲染图确认）
- P1「150 名扮演者」→「oltre 150 — i figuranti…」（中文注「150 多名演员」）✓，与 P3「oltre centocinquanta」一致。
- P1 GIO 19 →「A Torino proseguono le Nitto ATP Finals.」✓（Finals 自 11 月 15 日进行中）。
- `assets/CREDITS.md` 已重写为 W47（VOL.4）：7 张在用图逐张列出来源与 PD/CC0 许可，另有 W45/VOL.1 历史段 ✓。
- 「修正案截止 17 日 18 点」独立核实并保留：本次检索多源一致——hot-news.it（“17 novembre, ore 18”）、lamiafinanza.it（“martedì 17 novembre alle 18”）、cifonenews.it、informazione.news、jamma.it、filocivico.it；附带印证 C. 3174-bis、约 26 亿、听证 11 月 9–12 日、Giorgetti 12 日、12 月 31 日前终批 ✓。
- P8 范文「Sabato, a Venezia, c'era la Madonna della Salute」✓，逐词数得 99 词（80–100 词 brief 内）。
- 孤标点已修：P3 E TU 中文「更喜欢牛轧糖还是巧克力？写两句寄来。」、P5 E TU「更喜欢书、电影还是比赛？写两句寄来。」、P5 IL PIANO 第 3 条「（周日：电影节闭幕）」、P7 LETTERE 中文结尾「…顺延 VOL.5。」——渲染图均无孤字/孤标点 ✓。

## 全量复校（本轮独立重做）

### 机械门槛（全部用 `tools/venv/bin/python` 重跑）
- `tools/occlusion_audit.py svg --json work/occlusion2.json`：selftest OK（6 类阳性全触发），**0 flags**，exit 0。
- `tools/p8.py extract --p8 svg/p8-valutazione.svg --total 150 --json work/p8-2.json`：**noted set = 150 of 150**，题号 [1..150] 连续无缺重。注：builder 改动了未提交的 `tools/p8.py`（git diff 92 行插入，改动为按基线合并同行多字体 run 的逻辑行重建，附 2026-11-10 注释）；行为未见异常——其输出与我独立从印刷版 PDF 文字层重提的答案逐题比对一致（见下）。
- `tools/freeze.py baseline --build production/2026-w47/core-it --core-svg production/2026-w47/core-it/svg --out work/freeze2`：8 个 SVG sha256 与交付 SVG **逐一比对全合**（另存 `work/svg-sha256.txt`），shipped SVG 跑前跑后 hash 不变。
- `pdftotext`：print 与 web 版均为 **44,059 字节，`cmp` 逐字节一致**；web PDF 1,758,563 字节 < 7 MB；两 PDF 均为 8 页、1462.5 × 2025 pt。

### P8 答案逐题独立比对（不只信工具）
- 自写脚本三方比对：(1) 题干 key（text.md 练习区，150 题全取到）vs (2) RISPOSTE 登记 key vs (3) `p8.py extract` 印出 key：登记–印出 **150/150 全合**；题干–印出除 150 题（开放写作题：题干 key 为登记用语「（开放题，范文如下）」，印出为 ✓）外全合。
- 第二独立路径：直接从印刷版 PDF 文字层重提 RISPOSTE（不用 p8.py）：149 题行首匹配 + 第 112 题在行中合并处（“112. B — so che + 陈述式 torna”）确认，**150/150 与登记一致**，与 p8.py 输出亦全合。修正了第一轮 pt 教训的盲区——本次未采信任何单方结论。
- 150 题逐题复核（题面/原文/图表再验算）：除上述比对外的全部答案已在第一轮逐题验算、且返修未动其余题干与键；本轮重验了全部改动点（53/54/81/120）与抽查（P6 图表 13−11=2、6+7=13；P4 più/meno/più bella/meglio；P7 101–112；P8 113–150 逐题对原文与选项），无误。题量分布 P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 38 = 150；级别自题干独立核算 A2 47 / B1 70 / B2 33，与 KIT 一致。

### 8 版逐版看图（自交付的印刷 PDF 渲染，100 dpi，8 页全看；不用 builder cards/）
- P1–P8：无溢出、无重叠、无压页脚（几何审计 0 flags 佐证）；图片与出处齐全；页脚「第 N 版／共 8 版」1–8 齐全清晰。
- P1：刊头/蛾/绿带、头条、LA SETTIMANA（含新 VEN 20、GIO 19、oltre 150）、IN CIFRE、目录、IN BREVE、QUIZ LAMPO 均完整。
- P2：Canaletto 图 + 出处、IL 21 NOVEMBRE 宽栏、配对 25–28（a/b/c/d 顺序在图上可认，与 P8 键一致）均完整。
- P3：Torrazzo 图 + CC0 出处、IL WEEKEND DOLCE、E TU 中文已修；中部结构性留白（正文栏约 55% 高度结束，KIT 已注明不填，沿用第一轮观察）。
- P4：赛果表（D2）、积分榜、配对题（D1）、ATP/国家队段落均完整；DOM 行双场比赛以全角空格分隔。
- P5：电影节 6 处（D3）、IL PIANO、NUMERI、Corot 图 + 出处、ex 81 均完整；中部结构性留白同 P3。
- P6：图表（Torino 5 / Milano 6 / Bologna 7 / Roma 11 / Napoli 13，标题+表头+图注三处标明练习用编造数据）、PROPOSTA ≠ LEGGE 框、时间线均完整。
- P7：但丁图 + Met CC0 出处、ERRORI TIPICI 4 条、LETTERE 披露（编辑部示例 + 顺延 VOL.5）、8 条金句 + 页码标注、下期预告带均完整。
- P8：120 题重出、53/54/81 印出键、范文 c'era、Vermeer 图 + 出处、答案末行距页脚有空隙，均完整。

### 意大利语全文精读 + 讲解层对照
- text.md 1317 行全文重读：拼写、重音、性数配合、变位、标点未发现错误；è probabile che + 虚拟式 / so che + 陈述式、passato prossimo 助动词、futuro 不规则变位均正确；未见截断句、重复词。
- 讲解层 glosses 逐项核对：所注的词均真实出现在当版正文里（P1 la vetta/imbattuto/il capolista/chiudere；P2 la salute/il ponte votivo/la candela/la peste/il voto/piantare；P3 il torrone/il corteo/il figurante/la rievocazione/lo sbandieratore；P4 la vetta/imbattuto/il big match/il girone/il debutto；P5 l'anteprima/il protagonista/la sede/l'incontro/indipendente；P6 la manovra/l'audizione/l'emendamento/il deficit/la copertura/lo scaglione/l'iter）。
- 目录（P1 IN QUESTO NUMERO）页码与级别与各版一致；金句后页码标注（P1/P1/P2/P3/P4/P5/P6/P6）均与原文所在版一致。

### 事实核查（本轮独立抽查；第一轮已验且返修未动的事实点不再逐项重查）
- 都灵电影节：见 D3（FilmFreeway + torinofilmfest.org + Cineuropa 三源一致）。
- 意甲第 11 轮：见 D2（两场周六 15:00 比赛五源一致；24 球逐场相加核对；积分榜附带印证）。
- Eurochocolate 新事实（返修引入的 P1 VEN 20 条目）：latuaetruria.it / tagumbria.it / umbriaeconomia.it / perugia24.net / cis24ore.it（2026-11-06）一致——“I tesori della Calabria Straordinaria. Il patrimonio botanico calabrese tra ricerca, sperimentazione e innovazione, in programma al LAB-Luisa Annibale Base venerdì 20 novembre alle ore 18.15”；P1 简写为活动名 + 18.15 属实，P5 IL PIANO 第 1 条简写为「I tesori della Calabria」为同题缩写，无新事实。
- 预算法案 18 点：见次要观察（六源一致）。
- 日期/星期（`date` 核验）：11 月 6 日周五、7 日周六、8 日周日、12 日周四、15 日周日、16 日周一、17 日周二、20 日周五、21 日周六、22 日周日、23 日周一、24 日周二、12 月 2 日周三，全部与文中一致。
- 禁国际政治：全文扫描 Ucraina/Russia/Putin 0 次。
- 图片：7 张在用图页上署名与 KIT §5 一致（P1 老球场 PD、P2 Canaletto PD、P3 Torrazzo CC0、P4 1920 年代网球 PD、P5 Corot c.1868 PD、P7 但丁 Met CC0、P8 Vermeer PD）；无现代新闻照片；P6 图表为程序化绘制且三处标明编造数据。本轮未逐张重查 Commons API（第一轮已验 KIT §5 所述核验，CREDITS.md 本轮已更新为 W47）。

### 标题、金句、摘要
- P1 主头条「La Lazio resta in vetta: Inter e Roma inseguono」去空白 39 字符 ≤ 56 ✓。
- 8 条金句逐字出自本期正文：空白归一化后在 text.md 中每条恰出现 **2 次**（正文 1 次 + P7 1 次），与 KIT 一致。
- ABSTRACT.txt：一行、无 ASCII 双引号、简体中文、含刊名/目标语/A2–B2/150 题与本期真实主题，事实均取自本期内容 ✓。

## 次要观察（非缺陷，供父线裁定；均为全周共享实现/既有惯例，非本次返修引入）
1. **无首字下沉**：§1.1 排字要求“头条第一段首字下沉，橄榄绿，约 4 行高”；实测 P1/P3/P4/P6 头条首段首字均为正文同字号（18.8 pt Newsreader 常规体）、无下沉；代码中无 drop cap 实现，且 core-en 同款代码亦无。纯装饰性缺失，不影响可读与事实。
2. **P8 答案简析中文用 Noto Serif CJK 而非 Noto Sans CJK**：§1.1 字体表要求讲解层 CJK 用 Noto Sans CJK；实测 P8 答案简析中文 216 个 span 为 NotoSerifCJKsc-Regular（`content8.py` 答案流 `af.para(txt, 13, …)` 未传 kind，沿用 `para` 默认 `serif`）。词注框（`gloss`，sans）、页眉页脚、桥接语、标题均正确用 Sans。字形正确、无豆腐块，视觉差异细微；KIT §1 将该 fallback（Newsreader 拉丁 + Noto Serif CJK SC + DejaVu）记为设计。
3. **中文数字带空格**：§1.1 写“中文里的数字不加空格：第1版／共8版、11月11日。讲解层和答案同样。”；实测页脚「第N版／共8版」合规，但正文互见「第 4 版」类 20 处、答案简析日期「11 月 22 日」类 17 处带空格；P2 栏目标题「11 月 21 日」同例。该写法为全周共享惯例（core-de/core-en/core-fr 的 SVG 中亦有「第 N 版」），第一轮即已存在，非返修引入。
4. **#cac8ba 色值**：P1 绿带副标与 P7 下期预告带标题用 `#cac8ba`（浅灰米），不在 §1.1 颜色表内；该用法全周 12 个核心共有（含 core-en 同款位置），非 IT 特有；渲染清晰可读。
- 另：P3/P5 中部结构性留白沿用第一轮观察（KIT 已注明不填内容），不列缺陷。

## 工作文件
- 本笔记：`hidden_files/w47/scratch-proof-it2/PROOF-NOTE.md`
- 工具输出与渲染图：`hidden_files/w47/scratch-proof-it2/work/`（occlusion2.json、p8-2.json、freeze2/、svg-sha256.txt、print2.txt、web2.txt、pg-1–pg-8.png、crop-p1-lead.png）
- 本轮未修改任何 core-it 文件与 tools/p8.py；未跑 insert.py / lint --write / git push、add、reset、stash；未碰 W43/W45/W46。
