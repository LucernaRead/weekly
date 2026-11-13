# PROOF-NOTE — 2026-W47 it-de 独立复校（core D-2 fix 后重扩散，全量复校）

**结论 (a)：干净，可定稿。0 缺陷。观察项 3 项（均在盒内/页内，字形完整，无裁切、无重叠，见 §11）。**

- 版次：2026-w47-it-de（意大利语目标语 × 德语读者，VOL.4）
- 复校员：独立复校 subagent；与重扩散员不同人；SOP §8.4 全量复校
- 复校日期：2026-11-11
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it2-de/`
- 开工探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` = `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0；scratch 真实写文件通过（`probe.txt`）；全程 `TMPDIR=<scratch>/tmp`，未写系统 /tmp；解释器全程 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0）；`PYTHONDONTWRITEBYTECODE=1`；生产目录只读，未 commit、未 push、未重渲染交付的 web PDF（web PDF 仅在 scratch 重建做文字层比对）。
- 已读：`~/workspace/weekly-git/SOP.md` §8、§1.1 全文；`scratch-refanout-it2/FANOUT-REPORT-it2.md` 全文；`scratch-fix-it-de1/FIX-LOG.md`；`scratch-reproof-it-de1/PROOF-NOTE.md`（被驳回的 (a)，只作 fix1 回归参考，不作定稿依据——该轮 PROOF-NOTE 全文 0 次提及 andare/leggere/D-2/futuro，未审查 P7 教学句事实正确性）；`scratch-fix-core-it-d2/FIX-LOG.md`。

## 1. SHA 硬规则（开工核对 + 完工复核，两次全对；完工复核时生产文件 mtime 仍为重扩散时刻 21:40–21:41，本轮未写生产一字节）

| 件 | 字节数 | SHA-256（实测） | 结果 |
|---|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-DE.pdf` | 14,037,210 | `7952f4ff3b957ecbbbdd8be5701237b2fe43824160575ee8bc217baedfa5c7b8` | ✓ 一致 |
| 网页 PDF `La-Lucerna-VOL4-DE-web.pdf` | 1,297,238 | `65e262903bd0ee8fa82fa2d575f6225ec01c815c5551451ec964ee448c9a1ac0` | ✓ 一致 |
| text.md `2026-w47-it-de.text.md` | 56,662（1317 行） | `de0aa214818e4ce2c25952323cd8cac781d72d89419130b2ffb96308dd2798c9` | ✓ 一致 |

源核心核对（D-2 定稿核心，三 SHA 与 FANOUT-REPORT-it2 §2 逐字一致）：印 `e1f89922a2b09e66d7d132eeab12b2638528e737685fa85d70f41bb8d2d1255d`（27,726,330 B）/ 网 `09f2ef6696ad67e92e57ba161c8ba2e6b35753634fa21b7ce68ea029283d71ef`（1,790,596 B）/ 文 `9eb9ee0662542e6ccf2814a2f2534fd64b62ad326de42e9cf83282092b5b6eed`（52,655 B）。备份核对（`scratch-refanout-it2/backup/2026-w47-it-de/`）：文 `36a11a8f…` / 印 `527b38ce…` / 网 `f9f4343b…`，与 `shas-pre.txt` 逐字一致。

## 2. 回归 A — D-2 修正句（逐项独立重测，不抄前人结论）

新串在 text.md:775/:777（逐字核对）：

- :775 `Per i piani della settimana usiamo il futuro semplice: andremo a Cremona, assaggeremo il torrone, guarderemo Atalanta–Inter. Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.`
- :777 `E per la settimana prossima: leggeremo a BookCity, che apre lunedì 23 novembre. Il verbo è leggere, regolare al futuro: leggerò.`

| 检查项 | 结果 |
|---|---|
| 新串 L17 `Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.` | content7.py:17 ×1、p7 SVG ×1（换行碎片合拼后）、text.md:775 ×1、印/网 PDF P7 文字层各 ×1（全文档亦各 ×1） |
| 新串 L18 `Il verbo è leggere, regolare al futuro: leggerò.` | content7.py:18 ×1、p7 SVG ×1、text.md:777 ×1、印/网 PDF P7 文字层各 ×1（全文档亦各 ×1） |
| 旧串 `Le forme sono regolari: andare` | content7.py / p7 SVG / text.md / 两 PDF 文字层（P7 与全文档）均为 0；全版 live 文件 grep 亦 0——仅 WEEKLY-KIT.md §13 历史行提及 1 次（修史记录，非 live 内容） |
| 旧串 `irregolare al futuro: leggerò` | 同上，全 0（同 KIT §13 历史行 1 次） |
| text.md 与重扩散前 diff | 恰 :775/:777 两行 replace，其余 1315 行逐字节一致；−21 字节（56,683→56,662） |
| SVG diff | p1–p6/p8 逐字节一致，仅 p7 不同；位置级文本节点 diff 仅限两句换行碎片（旧节点 `andare `/`andrò, assaggiare `/`assaggerò,`/`guardare `/`leggerò.`/`verbo è leggere, irregolare al futuro:`/`→` 等；新节点 `assaggiare `/`assaggerò, guardare `/`verbo è leggere, regolare al futuro: leggerò.`） |
| cards diff | p1–p6/p8 逐字节一致，仅 p7 不同 |
| content diff | 仅 `content7.py:17/:18` 两行；其余 content*.py、bslib4.py、svglib.py、render.py、run.py 逐字节一致 |
| 全树 diff（备份 vs 生产） | 恰 7 个文件不同：text.md、两 PDF、WEEKLY-KIT.md、cards/p7、content7.py、svg/p7——即 P7-only 预期集，无任何其他文件改动 |
| PDF 文字层注记 | `→` 在文字层粘邻词（`→assaggerò,`、`guardare→`）且句内有换行；计数前做空白归一化 + `→` 归一化（与 fanout 检查脚本同一修正，非内容问题）。`andare` 一词在 P7 另有 2 处，均为合法处：Q101 题干 `(andare)` 与 key 注 `andare mit essere als Hilfsverb.`；text.md 全文 `andare` 8 处全部合法（Q42/76/101 题干、key 注、P6 正文 `andare in stampa`） |

## 3. 回归 B — fix1（D1/D2 奶油盒标题，三法独立重测）

| 缺陷 | 标题（fix1 后） | PIL 真墨 | 96dpi 渲染像素 | 文字层 bbox（印/网同值） | 最紧值 | 结论 |
|---|---|---|---|---|---|---|
| D1 P1 cifre | `LA SETTIMANA IN CIFRE　ZAHLEN` | +25.0（墨 936.0，盒缘 961） | +28（固实墨 933） | +24.9（xMax 702.1pt → 936.1px） | **+24.9** | 通过 ≥+5 |
| D2 P2 frase | `LA FRASE PER RICORDARE　MERKE` | +9.5（墨 951.5） | +11（固实墨 950） | +8.1（xMax 714.7pt → 952.9px） | **+8.1** | 通过 ≥+5 |

- 注：D1 像素法本轮读 933（fix1 称 932，+29→+28，1px 栅格阈值差）；最紧值 +24.9 与 fix1 逐字相同，不影响结论。
- 旧串 `DIE WOCHE IN ZAHLEN`、`MERKSATZ` 在 SVG（p1/p2）+ text.md + content12.py 均为 0 次；content12.py:44 = `LA SETTIMANA IN CIFRE　ZAHLEN`，:177 = `LA FRASE PER RICORDARE　MERKE`；`translations.py` de 值 L94/L563 已核一致。
- 29 个奶油盒标题全版重扫（PIL 真墨，标题行）：0 溢出；最紧依次为 D2 +9.5、P7 ERRORI TIPICI +13.8、P3 HINWEIS +19.2、D1 +25.0。
- 全节点奶油盒扫描（每盒内全部文本节点）：29 盒 0 flags；全版最紧为 P1 副标题 `Die Woche　Cosa succede, giorno per giorno` +5.8（见 §11 O3）。

## 4. 回归 C — P7 A2 IL FUTURO 段语义逐句事实核查（D-2 教训：读教学句本身）

本轮独立检索核实（非引述 fix 员结论，见 GATE-LOG §C）：

- **andare 未来时不规则**：LibreTexts《Indicativo futuro》不规则词干表明确列 andare → andr-；Dante Learning、FluentU、FlexiClasses 均列 andare → andrò 为不规则（元音脱落组，*anderò* 为错形）。新版 L17 已删去 andare 规则例，✓。
- **leggere 未来时规则**：LibreTexts 以 leggere 作规则 -ere 动词例（io leggerò）；Dante Learning 规则表 parlare/leggere/dormire 并列。新版 L18 标 `regolare al futuro: leggerò`，✓。
- **assaggiare → assaggerò、guardare → guarderò 规则**：-giare 动词按规则丢 i 后加未来时词尾（FluentU：verbs ending in –ciare/–giare drop the *i*），assaggerò 为规则形；guardare 为规则 -are 动词。✓
- 首句 `andremo a Cremona, assaggeremo il torrone, guarderemo Atalanta–Inter` 只称“用 futuro semplice”，未给 andremo 贴规则标签，✓。L18 前句 `leggeremo a BookCity`（leggeremo 规则形）与桥句 `Pläne im Futur ausdrücken: andremo, assaggeremo, guarderemo, leggeremo.` 均未动，指涉不悬空，✓。
- 全版 `regolar`/`irregolare` 仅出现在这两行（content*.py + text.md grep）：无其他同类规则性断言。Q101–104 键（andremo / assaggeremo / guarderemo / B leggerò）与教学句一致；Q104 key 注 `leggerò ist das Futur von leggere` 无规则性断言，✓。
- **C 结论：P7 A2 两句的规则性标签现在正确。**

## 5. 150 题三源逐题核对（text.md 练习键 × text.md Risposte × P8 印刷键，另对 core-it）

- 题号 1–150 全齐，无缺重；练习键解析 150 条，Risposte 解析 150 条。
- 练习行键 vs Risposte 键：**0 实 mismatch**（12 处表观差异仅为本轮脚本归一化 artifact：配对题 25–28/52–55/141–144 的练习行记 `key-c`、Risposte 记 `c`，字母本身相同）。Q150 为设计差异（练习行 `(Offene Aufgabe — Modelltext unten)`，Risposte 为 `✓ Modelltext in Abschnitt H unten (99 Wörter)`）。
- P8 印刷键（`tools/p8.py extract`）vs text.md Risposte：**0 mismatch，150/150**。
- Risposte vs core-it Risposte：147 条逐字相同；仅 137/138/139 不同，均为德语重定向翻译键（预期内，与 p8 keydiff 一致）；Q150 两版同为 ✓ 注。
- 全文通读 text.md 1317 行：每题键与题面逐项读过，意大利语变位/性数/助动词均正确（attraversano/portano/piantiamo/prega/mangia；è arrivato/abbiamo assaggiato/sono andati/ha chiuso；ha vinto/ha pareggiato/sono arrivati/abbiamo guardato/ha preso；andremo/ci sarà/guarderemo/durerà；piova/nevichi/controllino/sia/leggano；è partito/abbiamo visto/hanno comprato/è finita；ERRORI TIPICI 四组纠错全部正确）。

## 6. 8 金句（P7 FRASI DELLA SETTIMANA）逐字核对

8 条全部在 core-it text.md 中逐字存在，且在本版正文（P7 FRASI 节之前）逐字存在（全文各 ×2 = 正文 1 次 + FRASI 节 1 次）；页码标注逐项核实与来源页一致：

| # | 金句 | 来源页 | 核实 |
|---|---|---|---|
| 1 | «La Lazio resta in vetta» | Pagina 1 | P1 LA NOTIZIA 标题逐字 |
| 2 | «ventiquattro gol in dieci partite» | Pagina 1 | P1 正文逐字 |
| 3 | «il ponte votivo sul Canal Grande» | Pagina 2 | P2 正文逐字 |
| 4 | «oltre centocinquanta figuranti in costumi rinascimentali» | Pagina 3 | P3 正文逐字 |
| 5 | «la squadra di Gattuso è ancora imbattuta dopo 11 giornate» | Pagina 4 | P4 正文逐字 |
| 6 | «sette giorni di libri, ragioni e follie» | Pagina 5 | P5 正文逐字 |
| 7 | «il testo può ancora cambiare» | Pagina 6 | P6 正文逐字 |
| 8 | «approvato dal governo non vuol dire già legge» | Pagina 6 | P6 正文逐字 |

另：LA PAROLA «la vetta» 注“Questa settimana vive a pagina 1 e a pagina 4”属实（P1 头条 + P4 栏目）。

## 7. 事实 / 日期 / 算术重算（独立重算 + 直播源核对）

- **意甲 11 轮 10 场比分**：与实际赛果逐场核对（williamhillnews.it、tuttoatalanta.com、tuttomercatoweb.com、minuto91.it 等多源一致）：Venezia–Udinese 2–1、 Cagliari–Frosinone 1–0、Torino–Lecce 1–1、Parma–Bologna 1–2、Roma–Sassuolo 3–0、Napoli–Lazio 1–1、Genoa–Milan 1–2、Monza–Atalanta 0–1、Inter–Como 2–0、Fiorentina–Juventus 2–2——**10/10 与直播源一致**；总进球重算 3+1+2+3+3+2+3+1+2+4 = **24** ✓；积分 Lazio 29 / Inter 28 / Roma 27 / Milan 24 / Como 23 / Udinese 5 与报道一致（“La Lazio di Gattuso… resta prima a 29 punti e imbattuta”；Roma 最佳攻击 31 球亦与报道一致）；Q49 键 A（Roma 最佳攻击）✓。
- **星期核验**（`TZ=Europe/Rome date -d`，21 个日期全验）：6日周五、7日周六、8日周日、9日周一、12日周四、13日周五、14日周六、15日周日、16日周一、17日周二、19日周四、20日周五、21日周六、22日周日、23日周一、24日周二、12月2日周三、12月6日周日、12月31日周四、10月15日周四、10月28日周三——**与文中全部星期表述一致**。注：“12ª giornata si chiude lunedì 23”与 23 日周一一致。
- **天数**：Torrone 7–22日共 16 天 ✓；BookCity 23–29日共 7 天 ✓；Torino Film Festival 24日–12月2日共 9 天 ✓。
- **BookCity 2026 直播源核对**：第 15 届、23–29日、主题 «Il senno sulla Luna»（源自 Ariosto《Orlando furioso》）、周一 23日 20:00 Teatro Dal Verme 开幕、Colson Whitehead（两届 Pulitzer 奖得主）、1,360 活动 / 2,487 主角 / 1,164 图书 / 443 场地——与官方节目册（bookcitymilano.it / Confcommercio Milano PDF）及多家报道逐项一致。
- **其他史实**：Madonna della Salute 1630 誓愿、Longhena 设计、basilica 建于 1631–1687；全国植树节 11月21日（1898 年首届植树节、2013 年立法）；Santa Cecilia 11月22日音乐主保——均为公认史实，与文中表述一致。
- **算术**：Q83 Torino 5° 最冷 ✓；Q84 Napoli 13° 最热 ✓；Q85 13−11=2 ✓；Q86 6+7=13 ✓；Q8 24 球 ✓；范文 99 词（实数 99）✓；Q114 24 球、Q121 29 分等 P8 评估题键全部与正文一致。
- **Q137–140 翻译逐句核对**：137 意→德（si passivante → “die Menschen” 主动句，正确）、138 ✓、139 ✓、140 德→意 “Jede Zahl muss klar sein” → “Ogni cifra deve essere chiara” ✓。
- **禁词**：text.md 汉字 0 个；Ucraina/Russia/Putin 0 次；无国际政治内容。

## 8. 目视检查（交付印 PDF 200dpi 全页逐页 + 6 张标注裁图）

8 页全页图逐页目视：版式、图片、图注、表格、练习区、答案区均干净，无溢出、无重叠、无裁切、无乱码、无豆腐。

- P1：D1 cifre 盒、头条、球场照、QUIZ LAMPO 正常。
- P2：D2 frase 盒正常；中栏 `E LA SETTIMANA SCORSA?` 下留白为 core 固有栏流。
- P3：Torrazzo 照、IL WEEKEND DOLCE、E TU? 正常；中栏留白为 core 固有模式；`costruzioni.` 为栏中段换行末词（core 同节点，已接受）。
- P4：赛果表、LA CLASSIFICA、柱状图位置正常；右栏 HINWEIS 下留白为 core 固有。
- P5：Corot 画、IL PIANO DELLA SETTIMANA、I GIOVANI IN NUMERI 正常。
- P6：MINIME 柱状图条长与数值成比例（Torino 5° 最短、Napoli 13° 最长）、PROPOSTA ≠ LEGGE 正常。
- P7：D-2 两句渲染干净完整（见裁图）；Q101–104 完好；Dante 像、ERRORI TIPICI、LA PAROLA、LETTERE、FRASI 8 条页码、LA PROSSIMA SETTIMANA 栏均正常。A2 段末 `guarderò.` 独占一行是段末自然换行，非孤儿（见 §10）。
- P8：150 题 + 150 答案行全齐；Q137–139 德语翻译键、Q150 范文注、Vermeer 图均正常；P8 局部答案行换行碎片（freeze diff P8 +164/−629）由 p8 compare CLEAN 证同，非缺陷。

标注裁图（红线=盒缘/页缘 1862，`pages/crop-*.png`，均已目视）：

- `crop-d1-title.png`：标题完整在盒内，与红线有明显空隙。
- `crop-d2-title.png`：标题完整在盒内，与红线有明显空隙。
- `crop-p7-a2.png`：D-2 两句逐字完整、无裁切、无重叠。
- `crop-p7-lettere-bottom.png`：末行下行字母（`p`、`g`）完整在盒内，红线（盒底 1673）位于其下（见 §11 O2）。
- `crop-p8-furniture-wide.png`：末字 `Aufgabe` 的 `e` 字形完整，右缘恰贴红线（见 §11 O1）。
- `crop-p1-subtitle.png`：`giorno per giorno` 末端与红线有明显空隙（见 §11 O3）。

## 9. STRADDLE 裁决（备份旧版对照已跑）

- 全版 29 奶油盒标题 + 全节点扫描：0 溢出，无任何标题越过奶油盒右缘。
- 备份对照（`scratch-refanout-it2/backup/`）：8 页最右固实墨新旧逐页相同（P1 1861、P2 1862、P3 1861、P4 1861、P5 1862、P6 1861、P7 1861、P8 1864）；P2/P5 的 1862 行经 SVG 节点确认为与 core 同值同构造（P2 y=1594 `Una festa, una giornata verde`；P5 y=603 Corot 图注），恰在边距，非缺陷。
- **STRADDLE 不触发；无回归。**

## 10. 孤儿扫描

- 单字节点全版扫描（470 个）：0 孤儿。全部为 (a) 结构项（级别徽章 A2/B1/B2、题号、Einsetzen 指令、页眉 kicker、日期标题、IN BREVE 标签、图表标签），(b) 栏中换行末词/段末词，(c) 已接受项 P3-main 末行 `costruzioni.`（core 同节点同栏）。
- 新增单字节点仅 D-2 换行碎片：P7 `assaggiare` / `→` / `guarderò.`（y=402.22/434.9，A2 段内换行），非栏顶/栏底孤儿。y<400 的单字节点仅 P1 页眉 kicker（36pt）与 P2 大标题末词 `novembre`（37pt），均为标题结构。

## 11. 观察项（非缺陷，不影响定稿）

1. **O1 — P8 家具行贴边**：`Jede Antwort hat eine einzeilige Notiz auf Deutsch　✓ = Modelltext-Aufgabe`，PIL 真墨右 1862.0（恰在边距），96dpi 渲染 1864、200dpi 渲染 1864.3（抗锯齿外溢约 2px）；200dpi 加宽裁图目视：末字 `Aufgabe` 的 `e` 字形完整、无裁切，红线（1862）仅贴其右缘。无边框、无他物重叠，不触发 STRADDLE；与 core 对应行（同 y=1382，同一构造）一致。距页缘 1950 尚有 88px。
2. **O2 — P7 LETTERE 盒底极紧**：盒底 1673.0；PIL 真墨底 1672.92，余量 **+0.08px**（与上一轮 +0.1px 同值）；96dpi 渲染盒内最低固实墨行 1672，余量 +1.0px（上一轮读 1671/+2.0，1px 为栅格阈值差；LETTERE 节点与重扩散前逐字节一致，非内容变化）。200dpi 裁图目视：末行 `Aufsätze; das Versprechen gilt für VOL.5.` 下行字母完整在盒内。y=1686 的墨线是通栏橄榄绿分隔线（x 88..1862），非文字，距盒底 13px。
3. **O3 — P1 副标题最紧**：`Die Woche　Cosa succede, giorno per giorno` 墨 1856.2 vs 盒 1862 → +5.8（PIL）/+7（渲染）。在盒内。

## 12. 缺陷清单

**无。0 缺陷。**

---

*证据文件：`GATE-LOG.md`（本 scratch）、`pages/p200-1..8.png`、`pages/crop-*.png`、`out/`（各门日志）、`verify-triple-prod.log`、`scan_box_titles_prod.log`。*
