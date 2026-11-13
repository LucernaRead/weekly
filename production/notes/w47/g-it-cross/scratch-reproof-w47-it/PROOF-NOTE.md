# W47 it 家庭独立重校记录（第二派）

- 校对员：第二派独立校对（未参与建造）。只校对，不修复、不重建、不 commit、不 push。
- 工具 HEAD（开工）：`b9ac29a6f3c640f408965572823e5a1ccebfd1e5`（`~/workspace/weekly-git`）；首派跑门控时为 `71f4e6f9`，工具其后有变，本派全部四门（p8 compare / occlusion / boxtitle / pdf edge scan）已在现 HEAD 重跑，见 `gates2/`。
- 磁盘：开工 `df` 已用 93G（<100G 门限），可开工。
- SOP 依据：`~/workspace/weekly-git/SOP.md` §8（校对闭环）+ §1.1（字体/字号/版心）；D5 定义见 `scratch-d5-plan/D5-PLAN.md` §1（讲解层拉丁字误用 Noto Sans CJK，本次重建改回 Newsreader）。
- 2026-11-16（周一）至 2026-11-22（周日）经 `date -d` 核实：16=周一，22=周日，刊期正确。

## 盘点（开工核对）

目标语 it × 读者母语 en de fr es ja ko nl pt ru zh-cn zh-tw = 11 版。盘上：

- fan-out 目录 10 个：`2026-w47-it-en/de/fr/es/ja/ko/nl/pt/ru/zh-tw`
- `2026-w47-it-zh-cn` 无独立 fan-out 目录，core 目录 `production/2026-w47/core-it/` 即 it-zh-cn 版（含 `2026-w47-it-zh-cn.text.md` + `La-Lucerna-VOL4-web.pdf` + `La-Lucerna-VOL4.pdf`）
- 无多余目录、无缺失：11/11 齐全。另有反向 `2026-w47-<母语>-it` 目录 11 个，不属本家庭范围，未校。

每版均有印 PDF（8 页，1462.5×2025 pt）+ web PDF + `.text.md` + ABSTRACT.txt。页图用首派已渲染的 `pages/`（88 张 = 11 版 × 8 页，源自印 PDF），未重渲染。

## 全家共性问题

### F-1（严重，5 版）：P1 刊头行中央标语与右侧日期重叠

- 位置：每版 P1 顶部刊头行（y≈92，SVG 坐标），中央标语末词与右端日期 `SETTIMANA DAL 16 AL 22 NOVEMBRE 2026` 相撞。
- 机制（SVG 实测）：日期元素固定在 x=1425.7（11 版相同），标语居中起排、长度随读者语而异；Newsreader（D5 重建后）下较长标语的墨迹越过 1425.7。11 版 P1 PNG 刊头行墨迹柱状扫描（阈值 <150，y 75–125）+ 局部 4 倍放大图核实：
  - **重叠（字形互压，词界消失）**：it-en（READING 的 G 压住 SETTIMANA 的 S，约 8px 交叠）、it-fr（ITALIENS 末 S 与 SETTIMANA 首 S 相叠）、it-nl（LEZEN 的 N 压住 S）、it-ru（西里尔 Ц 尾笔压住 S）、it-pt（LEEM 与 SETTIMANA 零间距相贴，词界消失，实测间距仅 ~3px）。
  - 紧但未撞：it-de（LIEST 与 SETTIMANA 间距 9px，约为正常词距下限，放大图字形清晰可辨——记为观察，非缺陷）。
  - 干净：it-es（45px）、it-ja（63px）、it-ko（147px）、it-zh-tw（122px）、it-zh-cn/core-it（121px）。
- web PDF 同样存在：抽查 it-en web PDF P1 渲染，同一位置同样重叠（同源 SVG，故 5 版 web 版同病）。
- 机械门未报：首派与本派 occlusion audit 均为 0 flags、boxtitle 0 DEFECT——刊头标语/日期对不在这两门覆盖范围内，属门控盲区（观察，非对工具的指控）。
- 严重度：严重。刊头行是每版第一眼；5/11 版词界被压坏，读者无法正常读出标语末词与日期首词。
- 修复方向（仅记录，不动手）：日期 x 不应固定，或标语须按读者语长度缩短/缩小；须整家复测 11 版。

### F-4（轻微，5 版）：P2 `LA FRASE PER RICORDARE` 盒标题译作「格言/口诀」

- 该栏是「要记住的句子」（本期固定句 `«La salute è la prima ricchezza.»` 及其讲解）；en `LEARN`、de `MERKE`、es `PARA RECORDAR`、ru `ЗАПОМНИТЕ`、ja `覚えておこう`、ko `기억해 두세요` 均表「记住」，译法正确。
- 译误 5 版：it-fr `DEVISE`（格言）、it-pt `LEMA`（格言）、it-nl `LEUS`（格言）、it-zh-tw `口訣`、core-it/zh-cn `口诀`——均不表「记住」。属同一模板译误类，应统一改回「记住」类译法。
- 严重度：轻微。栏内正文内容正确，仅栏目标签词义走偏。

### F-5（观察，非错误，8 版）：Q44/Q134 答案注缩短

- en、de、core-it/zh-cn 三版注为完整形式（`Subject + verb + place + date` / `Subjekt + Verb + Ort + Datum` / `主语 + 动词 + 地点 + 日期`）；fr、es、pt、nl、ru、ja、ko、zh-tw 八版注缩短为仅 `主语 + 动词` 类（如 `Sujet + verbe`、`主語 + 動詞`），漏了句子实际含有的地点与日期（`a Perugia il 22 novembre`）。内容本身无错，属模板不一致，记为观察。注：八版的 Q136 注均含地点，与 en 一致、完整。

### 已知非缺陷（按任务书，不记为问题）

- it-zh-tw P1 `cifre` 标题余量 +0.5px：既有非回归，只报观察（见 it-zh-tw 节）。
- CJK 三版（ja/ko/zh-tw 及 core zh-cn）日/韩/繁体基底仍用手写变体块：已裁定保留现状，不当作缺陷。
- it-ko 仅差 1 换行符的文字层差异：pdftotext 分行噪声，不当作缺陷。

---

## it-en（目标语 it，读者母语 en）

校对文件（SHA 前 12）：

| 文件 | 字节 | SHA-256 前 12 |
|---|---|---|
| 印 PDF `La-Lucerna-VOL4-EN.pdf` | 13,497,072 | `6f0bbf408826` |
| 网 PDF `La-Lucerna-VOL4-EN-web.pdf` | 1,215,817 | `da29562db637` |
| text.md `2026-w47-it-en.text.md` | 55,183 | `ad311b5bf59a` |

（以下逐版填写）

### 方法说明（第 2–11 版）

意大利语核心正文经实测 11 版字节相同：以 8 个正文段首句为探针，`diff` it-en 对其余 10 版（含 core-it）命中 0 行；长行（>150 字）差异全部落在讲解层（NOTE/HINWEIS、题干译文、答案注）。因此 it-en 全文通读（1317 行）即覆盖全家共享核心；其余各版通读其全部版别差异行（`diff` 对 core/it-en 的 '>' 侧）+ 8 页看图 + P8 答案核对 + 摘要，不重复通读相同意大利正文。

### it-en 结论

**问题 2 条（1 严重 + 1 轻微），均属全家共性，见 F-1、F-2；另 1 条轻微版别内问题（F-3，见下）。其余零问题。**

- **F-1（严重）**：P1 刊头行标语末词 READING 与日期 SETTIMANA 重叠（印 + web 两版皆然；墨迹扫描：标语墨至 x≈1493，日期墨起 x≈1486，交叠约 8px；局部 4 倍放大图已核实）。
- **F-2（轻微）**：P6「LA STRADA DELLA MANOVRA」时间线 MAR 17 NOV. 行标签与正文零间距（`NOV.Scade`，放大图核实；其余三行间距正常）。
- **F-3（轻微，全家）**：P8 答案注中 7 处全角冒号 `：` 用在拉丁文内，如 `attraversare：i veneziani → attraversano`（SVG 实测 7 处；text.md 同款 14 处，因答案在题干区与答案区各出现一次）。CJK 三版（ja/ko/zh-tw 及 core zh-cn）讲解层用 `：` 属正当 CJK 标点，不计；但 P8 答案注模板的 7 处在拉丁读者版同样存在（it-en 实测；其余拉丁读者版 SVG 计数同为 7，见各版节）。
- P1–P8 看图：除 F-1、F-2 外无溢出/重叠/压页脚/截断；盒标题无顶出（boxtitle 门 18 titles / 256 body lines，0 DEFECT）；P8 字号可读，150 条答案完整无压边。
- 事实核验：刊期 11 月 16–22 日与星期一致（16 周一、22 周日）；比分表 10 场进球合计 24（3+1+2+3+3+2+3+1+2+4）与正文「ventiquattro gol in dieci partite」一致；积分榜 Lazio 29 / Inter 28 / Roma 27 / Milan 24 / Como 23 / Udinese 5 与正文、Q47–Q51、Q121–Q124 一致；Nations League 11 月 12 日周四、15 日周日与星期一致；BookCity 11 月 23–29 日、15 届、1.360 事件/2.487 人/443 场地与 Q65–Q82 一致；Torrone 29 届 11 月 7–22 日、Eurochocolate 32 届、松露展至 12 月 6 日与 Q29–Q33 一致；1441 年 10 月 25 日 Sforza–Visconti 婚礼、Longhena 1631–1687 年圣母安康大殿、1630 年许愿、1898 年植树节起源/2013 年立法均为真实史实；模范作文逐词数 99 词，与标注一致。
- P8 答案逐题复核：1–150 连续，全部与题面/原文/图表一致（验算：Q85 13−11=2；Q86 6+7=13；Q56 più / Q57 meno / Q58 più bella / Q59 meglio；Q93–Q96 piova/nevichi/controllino/sia；Q137–Q140 翻译与原文一致；Q150 模范作文 99 词）。
- text.md：全文 1317 行通读，与印 PDF 内容一致；摘要（ABSTRACT.txt，英文）真实具体，含 VOL.4、A2–B2、150 题；`“Fate dolci”` 弯引号在 Newsreader 元素内（SVG 核实）；`VOL.4` 与台账一致；页脚 `TEXT IN ITALIAN　EXPLANATIONS IN ENGLISH` 配对标注正确；P1 刊头 `THE ITALIAN WEEKLY　VOL.4　LA SERIE A　IL TORRONE　VENEZIA` 正确。
- 机械门（本派重跑，tools HEAD `b9ac29a6`，跑前跑后一致）：p8 compare CLEAN（150/150，keydiff=[137,138,139]——系 137–139 题答案按读者语翻译，属设计差异，集合相等）；occlusion 0 flags；boxtitle 0 DEFECT；pdf edge scan 0 TOUCH / 0 NEAR；web 与印 PDF 经 pdftotext 字节相同（44,991 字节，0 行差异）。
- 字体（D5）：pdffonts 见 Newsreader 多子集 + UnifrakturMaguntia；Noto Sans CJK SC 仅用于全角空格 `　` 分隔符；讲解层拉丁文在 Newsreader 内；弯引号 U+201C/U+201D 在 Newsreader 内。D5 修复到位。

---

## it-de（目标语 it，读者母语 de）

校对文件（SHA 前 12）：印 PDF `La-Lucerna-VOL4-DE.pdf` 13,499,365 字节 `365952141076`；网 PDF `La-Lucerna-VOL4-DE-web.pdf` 1,218,125 字节 `e92b6b99d517`；text.md `2026-w47-it-de.text.md` 56,662 字节 `de0aa214818e`。

### it-de 结论

**问题 1 条轻微（全家共性 F-2）+ F-3；P1 刊头不重叠。其余零问题。**

- **F-1 不适用**：P1 刊头行标语 `LIEST` 与日期 `SETTIMANA` 间距 9px（墨迹扫描 + 4 倍放大图），字形清晰、无压叠——记为观察，非缺陷。
- **F-2（轻微）**：P6 时间线 `MAR 17 NOV.Scade` 同 it-en（核心共享内容，像素相同）。
- **F-3（轻微）**：P8 答案注全角冒号 7 处（SVG 计数），text.md 14 处，与 it-en 同模板。
- P1–P8 看图：除 F-2 外无溢出/重叠/压页脚/截断；盒标题无顶出（boxtitle 门 22 titles / 259 body lines，0 DEFECT）；德语讲解较长导致的换行（如 P5 Q77 移至第 3 栏顶、P7 语法说明换行）均干净，无压边。
- 德语讲解层（398 行差异行全读）：翻译准确——HINWEIS 各条（`la salute, die Gesundheit`、`il ponte votivo, die Votivbrücke`、`il debutto, das Debüt` 等）、题干译文（`Vervollständige die Sätze`、`Wörter zuordnen`、`Richtig oder falsch`）、答案注（`Der Komparativ von bene ist unregelmäßig: meglio`、`so che + Indikativ torna`）、Q137–Q140 翻译（`Zur Madonna della Salute überqueren die Menschen die Votivbrücke`；`Jede Zahl muss klar sein → Ogni cifra deve essere chiara`）均正确；`LA FRASE PER RICORDARE　MERKE`、`E TU?　UND DU?`、`FRASI DELLA SETTIMANA　SÄTZE DER WOCHE` 栏目标签正确；页脚 `TEXT AUF ITALIENISCH　ERKLÄRUNGEN AUF DEUTSCH` 正确。
- 摘要（ABSTRACT.txt，德文）真实具体，含 VOL.4、A2–B2、150 Übungen。
- P8 答案与 it-en 逐项一致（集合相等，p8 compare CLEAN；137–139 为德语翻译，属设计差异）。
- 机械门（本派重跑）：p8 CLEAN（150/150）；occlusion 0 flags；boxtitle 0 DEFECT；edge scan 0 TOUCH / 0 NEAR；web 与印 PDF 文字层相同（46,010 字节，0 行差异）。

---

## it-fr（目标语 it，读者母语 fr）

校对文件（SHA 前 12）：印 PDF `La-Lucerna-VOL4-FR.pdf` 13,496,942 字节 `02e2b67cdb96`；网 PDF `La-Lucerna-VOL4-FR-web.pdf` 1,215,685 字节 `1b26c4d53d58`；text.md `2026-w47-it-fr.text.md` 56,517 字节 `aca1356c0c90`。

### it-fr 结论

**问题：F-1 严重 1 条 + F-2、F-3 轻微 + 1 条轻微（DEVISE 标签译误）。其余零问题。**

- **F-1（严重）**：P1 刊头行标语 `L'ITALIEN QUE LISENT LES ITALIENS` 末尾 S 与日期 `SETTIMANA DAL 16 AL 22 NOVEMBRE 2026` 的 S 重叠（P1 全页图可见，见 F-1 墨迹扫描）。
- **F-2（轻微）**：P6 时间线 `MAR 17 NOV.Scade` 同 it-en。
- **F-3（轻微）**：P8 答案注全角冒号 7 处（与 it-en 同模板）。
- **轻微——P2「LA FRASE PER RICORDARE」栏目标签译误**：法语标签为 `DEVISE`（座右铭/格言）。该栏是「要记住的句子」，en 用 `LEARN`、de 用 `MERKE`（记住），fr `DEVISE` 未译出「记住」之义，法语读者会理解为「座右铭」。应为 `À RETENIR` 类。位置：P2 中栏 `LA FRASE PER RICORDARE　DEVISE`。
- **观察——P1 侧栏标题缩写**：`LA SETTIMANA GIORNO PER GIORNO` 栏下法语小字为 `Cette sem. Cosa succede, giorno per giorno`——`sem.` 为 `semaine` 的缩写，其余版同位置用全词；可读、无歧义，记为观察。
- **观察——刊名用词不一**：P1 通栏 `JOURNAL ITALIEN　VOL.4`，页脚却为 `HEBDOMADAIRE ITALIEN VOL.4`；en 版通栏与页脚一致（THE ITALIAN WEEKLY / ITALIAN WEEKLY）。两词本身均正确，记为观察。
- **观察——Q44/Q134 答案注不完整**：法语注为 `Sujet + verbe`，en/de 注为 `Subject + verb + place + date`；该句含地点与日期（`a Perugia il 22 novembre`），法语注略去了后两项。非错误，记为观察。
- P1–P8 看图：除 F-1、F-2 外无溢出/重叠/压页脚/截断；盒标题无顶出（boxtitle 门 20 titles / 248 body lines，0 DEFECT）；法语长讲解换行干净。
- 法语讲解层（397 行差异行全读）：翻译准确——NOTE 各条（`il ponte votivo, le pont votif`、`il figurante, figurant`、`lo sbandieratore, le lanceur de drapeaux`、`il debutto, les débuts`）、题干译文（`Complète les phrases en italien`、`Associe mots et définitions`、`Vrai ou faux`、`Forme des phrases`）、答案注（`Le comparatif de bene est irrégulier : meglio`、`so che + indicatif torna`、`La Lazio est au singulier, le verbe aussi`）、Q137–Q140 翻译（`Pour la Madonna della Salute, on traverse le pont votif`；`Ogni cifra deve essere chiara — dovere = devoir`）均正确；`E TU?　ET TOI ?`、`FRASI DELLA SETTIMANA　PHRASES DE LA SEMAINE`、`VALUTAZIONE E RISPOSTE　EXERCICES ET RÉPONSES` 栏目标签正确；页脚 `TEXTE EN ITALIEN　EXPLICATIONS EN FRANÇAIS` 正确；法语标点（`?` 前空格、`« »`、`20 h 45`）规范。
- 摘要（ABSTRACT.txt，法文）真实具体，含 VOL.4、A2–B2、150 exercices。
- P8 答案与 it-en 逐项一致（集合相等，p8 compare CLEAN；137–139 为法语翻译，属设计差异）。
- 机械门（本派重跑）：p8 CLEAN（150/150）；occlusion 0 flags；boxtitle 0 DEFECT；edge scan 0 TOUCH / 0 NEAR；web 与印 PDF 文字层相同（46,133 字节，0 行差异）。

---

## it-es（目标语 it，读者母语 es）

校对文件（SHA 前 12）：印 PDF `La-Lucerna-VOL4-ES.pdf` 13,497,643 字节 `5c703a6665d2`；网 PDF `La-Lucerna-VOL4-ES-web.pdf` 1,216,392 字节 `f602876a0f91`；text.md `2026-w47-it-es.text.md` 56,193 字节 `4fd5647e2b7a`。

### it-es 结论

**问题：F-2、F-3 轻微 2 条；P1 刊头不重叠；「LA FRASE PER RICORDARE」标签正确（`PARA RECORDAR`）。其余零问题。**

- **F-1 不适用**：P1 刊头行标语 `EL ITALIANO QUE LEE ITALIA` 与日期间距 45px，干净。
- **F-2（轻微）**：P6 时间线 `MAR 17 NOV.Scade` 同 it-en。
- **F-3（轻微）**：P8 答案注全角冒号 7 处（与 it-en 同模板）。
- **观察——Q44/Q134 答案注不完整**：西语注为 `Sujeto + verbo`，en/de 注为 `Subject + verb + place + date`；同 fr 版情况（见 it-fr 观察），非错误。
- P1–P8 看图：除 F-2 外无溢出/重叠/压页脚/截断；盒标题无顶出（boxtitle 门 20 titles / 249 body lines，0 DEFECT）；西语长讲解换行干净。
- 西语讲解层（398 行差异行全读）：翻译准确——NOTE 各条（`il ponte votivo, el puente votivo`、`la candela, la vela`、`il corteo, el desfile`、`lo sbandieratore, el abanderado`、`il debutto, el debut`）、题干译文（`Completa las frases en italiano`、`Relaciona las palabras`、`Verdadero o falso`、`Forma frases`）、答案注（`El comparativo de bene es irregular: meglio`、`so che + indicativo torna`、`La Lazio es singular, y el verbo también`）、Q137–Q140 翻译（`Para la Madonna della Salute, la gente cruza el puente votivo`；`Ogni cifra deve essere chiara — dovere = deber`）均正确；`LA FRASE PER RICORDARE　PARA RECORDAR`（正确，fr 版 `DEVISE` 之误在此版不存在）、`E TU?　¿Y TÚ?`、`FRASI DELLA SETTIMANA　FRASES DE LA SEMANA`、`VALUTAZIONE E RISPOSTE　EJERCICIOS Y RESPUESTAS` 栏目标签正确；页脚 `TEXTO EN ITALIANO　EXPLICACIONES EN ESPAÑOL` 正确；刊名通栏 `SEMANARIO ITALIANO VOL.4` 与页脚一致。
- 摘要（ABSTRACT.txt，西文）真实具体，含 VOL.4、A2–B2、150 ejercicios。
- P8 答案与 it-en 逐项一致（集合相等，p8 compare CLEAN；137–139 为西语翻译，属设计差异）。
- 机械门（本派重跑）：p8 CLEAN（150/150）；occlusion 0 flags；boxtitle 0 DEFECT；edge scan 0 TOUCH / 0 NEAR；web 与印 PDF 文字层相同（45,915 字节，0 行差异）。

---

## it-pt（目标语 it，读者母语 pt）

校对文件（SHA 前 12）：印 PDF `La-Lucerna-VOL4-PT.pdf` 13,500,354 字节 `30749b8d69ec`；网 PDF `La-Lucerna-VOL4-PT-web.pdf` 1,219,136 字节 `ddb897ef9a68`；text.md `2026-w47-it-pt.text.md` 55,718 字节 `e01360ae9c40`。

### it-pt 结论

**问题：F-1 严重 1 条 + F-2、F-3 轻微 + 1 条轻微（LEMA 标签译误，与 fr DEVISE 同类）。其余零问题。**

- **F-1（严重）**：P1 刊头行标语 `O ITALIANO QUE OS ITALIANOS LEEM` 末尾与日期 `SETTIMANA` 零间距，词界消失（P1 全页图可见 `LEEMSETTIMANA`，见 F-1 墨迹扫描 ~3px）。
- **F-2（轻微）**：P6 时间线 `MAR 17 NOV.Scade` 同 it-en。
- **F-3（轻微）**：P8 答案注全角冒号 7 处（与 it-en 同模板）。
- **轻微——P2「LA FRASE PER RICORDARE」栏目标签译误**：葡语标签为 `LEMA`（格言/座右铭）。与 fr 版 `DEVISE` 同类错误：该栏是「要记住的句子」，en `LEARN`、de `MERKE`、es `PARA RECORDAR` 均译出「记住」之义，pt `LEMA` 未译出。应为 `PARA RECORDAR` / `A LEMBRAR` 类。位置：P2 中栏 `LA FRASE PER RICORDARE　LEMA`。
- **观察——P1 侧栏标题缩写**：`Esta sem. Cosa succede, giorno per giorno`——`sem.` 为 `semana` 的缩写，与 fr 版同；可读、无歧义，记为观察。
- **观察——Q44/Q134 答案注不完整**：葡语注为 `Sujeito + verbo`，en/de 注为 `Subject + verb + place + date`；同 fr/es 版情况，非错误。
- P1–P8 看图：除 F-1、F-2 外无溢出/重叠/压页脚/截断；盒标题无顶出（boxtitle 门 22 titles / 247 body lines，0 DEFECT）；葡语长讲解换行干净。
- 葡语讲解层（400 行差异行全读）：翻译准确——NOTE 各条（`il ponte votivo, a ponte votiva`、`la candela, a vela`、`il corteo, o cortejo`、`lo sbandieratore, o porta-bandeiras`、`il debutto, a estreia`）、题干译文（`Completa as frases em italiano`、`Relaciona as palavras`、`Verdadeiro ou falso`、`Forma frases`）、答案注（`O comparativo de bene é irregular: meglio`、`so che + indicativo torna`、`A Lazio é singular, e o verbo também`）、Q137–Q140 翻译（`Para a Madonna della Salute, as pessoas atravessam a ponte votiva`；`Ogni cifra deve essere chiara — dovere = dever`）均正确；`E TU?　E TU?`、`FRASI DELLA SETTIMANA　FRASES DA SEMANA`、`VALUTAZIONE E RISPOSTE　AVALIAÇÃO E RESPOSTAS` 栏目标签正确；页脚 `TEXTOS EM ITALIANO　EXPLICAÇÕES EM PORTUGUÊS` 正确；刊名通栏 `SEMANÁRIO ITALIANO VOL.4` 与页脚一致；用欧洲葡语拼写（`défice`、`escalão fiscal`、`11.ª jornada`），自洽。
- 摘要（ABSTRACT.txt，葡文）真实具体，含 VOL.4、A2–B2、150 exercícios。
- P8 答案与 it-en 逐项一致（集合相等，p8 compare CLEAN；137–139 为葡语翻译，属设计差异）。
- 机械门（本派重跑）：p8 CLEAN（150/150）；occlusion 0 flags；boxtitle 0 DEFECT；edge scan 0 TOUCH / 0 NEAR；web 与印 PDF 文字层相同（45,682 字节，0 行差异）。

---

## it-nl（目标语 it，读者母语 nl）

校对文件（SHA 前 12）：印 PDF `La-Lucerna-VOL4-NL.pdf` 13,495,361 字节 `cbd50234b442`；网 PDF `La-Lucerna-VOL4-NL-web.pdf` 1,214,079 字节 `35a4070da964`；text.md `2026-w47-it-nl.text.md` 55,488 字节 `b13ef7a7abe0`。

### it-nl 结论

**问题：F-1 严重 1 条 + F-2、F-3 轻微 + 1 条轻微（LEUS 标签译误，与 fr DEVISE、pt LEMA 同类）。其余零问题。**

- **F-1（严重）**：P1 刊头行标语 `HET ITALIAANS DAT DE ITALIANEN LEZEN` 末尾 N 与日期 `SETTIMANA` 的 S 重叠（P1 全页图可见，见 F-1 墨迹扫描 ~8px）。
- **F-2（轻微）**：P6 时间线 `MAR 17 NOV.Scade` 同 it-en。
- **F-3（轻微）**：P8 答案注全角冒号 7 处（与 it-en 同模板）。
- **轻微——P2「LA FRASE PER RICORDARE」栏目标签译误**：荷兰语标签为 `LEUS`（格言/座右铭）。与 fr `DEVISE`、pt `LEMA` 同类错误：该栏是「要记住的句子」，en `LEARN`、de `MERKE`、es `PARA RECORDAR` 均译出「记住」之义，nl `LEUS` 未译出。应为 `OM TE ONTHOUDEN` 类。位置：P2 中栏 `LA FRASE PER RICORDARE　LEUS`。
- **观察——Q44/Q134 答案注不完整**：荷兰语注为 `Onderwerp + werkwoord`，en/de 注为 `Subject + verb + place + date`；同 fr/es/pt 版情况，非错误。
- P1–P8 看图：除 F-1、F-2 外无溢出/重叠/压页脚/截断；盒标题无顶出（boxtitle 门 22 titles / 252 body lines，0 DEFECT）；P7 `LA PAROLA　WOORD VAN DE WEEK` 长标题经 3 倍放大核实，末尾 K 完整在盒内，无溢出。
- 荷兰语讲解层（397 行差异行全读）：翻译准确——NOTE 各条（`il ponte votivo, de geloftebrug`、`la candela, de kaars`、`il corteo, de stoet`、`lo sbandieratore, de vaandeldrager`、`il debutto, het debuut`）、题干译文（`Maak de zinnen af in het Italiaans`、`Koppel de woorden`、`Waar of niet waar`、`Maak zinnen`）、答案注（`De vergrotende trap van bene is onregelmatig: meglio`、`so che + aantonende wijs torna`、`La Lazio: enkelvoud, het werkwoord ook`）、Q137–Q140 翻译（`Voor de Madonna della Salute steken mensen de geloftebrug over`；`Ogni cifra deve essere chiara — dovere = moeten`）均正确；`E TU?　EN JIJ?`、`FRASI DELLA SETTIMANA　ZINNEN VAN DE WEEK`、`VALUTAZIONE E RISPOSTE　TOETS EN ANTWOORDEN` 栏目标签正确；页脚 `TEKSTEN IN HET ITALIAANS　UITLEG IN HET NEDERLANDS` 正确；刊名通栏 `ITALIAANS WEEKBLAD VOL.4` 与页脚一致。
- 摘要（ABSTRACT.txt，荷文）真实具体，含 VOL.4、A2–B2、150 oefeningen。
- P8 答案与 it-en 逐项一致（集合相等，p8 compare CLEAN；137–139 为荷兰语翻译，属设计差异）。
- 机械门（本派重跑）：p8 CLEAN（150/150）；occlusion 0 flags；boxtitle 0 DEFECT；edge scan 0 TOUCH / 0 NEAR；web 与印 PDF 文字层相同（45,774 字节，0 行差异）。

---

## it-ru（目标语 it，读者母语 ru）

校对文件（SHA 前 12）：印 PDF `La-Lucerna-VOL4-RU.pdf` 13,752,905 字节 `ead7a5eed56f`；网 PDF `La-Lucerna-VOL4-RU-web.pdf` 1,465,974 字节 `f3272028c9a2`；text.md `2026-w47-it-ru.text.md` 67,731 字节 `47c0471515d3`。

### it-ru 结论

**问题：F-1 严重 1 条 + F-2、F-3 轻微。其余零问题。**

- **F-1（严重）**：P1 刊头行标语 `ИТАЛЬЯНСКИЙ, КОТОРЫЙ ЧИТАЮТ ИТАЛЬЯНЦЫ` 末尾西里尔字母 Ц 的尾笔与日期 `SETTIMANA` 的 S 重叠（P1 全页图可见，见 F-1 墨迹扫描）。
- **F-2（轻微）**：P6 时间线 `MAR 17 NOV.Scade` 同 it-en。
- **F-3（轻微）**：P8 答案注全角冒号 7 处（与 it-en 同模板）。
- **观察——P1 目录栏标题缩写**：`IN QUESTO NUMERO　СОДЕРЖ.`——`СОДЕРЖ.` 为 `СОДЕРЖАНИЕ`（目录）的缩写，可读、无歧义，记为观察（同 fr `Cette sem.` 类）。
- **观察——Q44/Q134 答案注不完整**：俄语注为 `Подлежащее + глагол`，en/de 注为 `Subject + verb + place + date`；同 fr/es/pt/nl 版情况，非错误。
- P1–P8 看图：除 F-1、F-2 外无溢出/重叠/压页脚/截断；盒标题无顶出（boxtitle 门 26 titles / 320 body lines，0 DEFECT）；西里尔长讲解换行干净。
- 俄语讲解层（401 行差异行全读）：翻译准确——`LA FRASE PER RICORDARE　ЗАПОМНИТЕ`（「记住」命令式，译法正确；fr/pt/nl 的「格言」译误不存在于此版）、NOTE 各条（`il ponte votivo, обетный мост`、`la candela, свеча`、`il corteo, шествие`、`lo sbandieratore, знаменосец`、`il debutto, дебют`）、题干译文（`Дополните предложения по-итальянски`、`Соедините слова`、`Верно или неверно`、`Составьте предложения`）、答案注（`Сравнительная степень bene: meglio`、`so che + изъявительное наклонение torna`、`«Лацио» — ед. число, и глагол тоже`）、Q137–Q140 翻译（`В праздник Мадонны делла Салюте люди переходят обетный мост`；`Ogni cifra deve essere chiara — dovere = должен`）均正确；`E TU?　А ТЫ?`、`FRASI DELLA SETTIMANA　ФРАЗЫ НЕДЕЛИ`、`VALUTAZIONE E RISPOSTE　ТЕСТ И ОТВЕТЫ` 栏目标签正确；页脚 `ТЕКСТЫ НА ИТАЛЬЯНСКОМ　ОБЪЯСНЕНИЯ НА РУССКОМ` 正确；刊名通栏为 `ИТАЛЬЯНСКИЙ VOL.4`（页脚全称 `ИТАЛЬЯНСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.4`，同 fr 版刊头简称/页脚全称的命名不一致，记为观察）。
- 摘要（ABSTRACT.txt，俄文）真实具体，含 VOL.4、A2–B2、150 упражнений。
- P8 答案与 it-en 逐项一致（集合相等，p8 compare CLEAN；137–139 为俄语翻译，属设计差异）。
- 机械门（本派重跑）：p8 CLEAN（150/150）；occlusion 0 flags；boxtitle 0 DEFECT；edge scan 0 TOUCH / 0 NEAR；web 与印 PDF 文字层相同（53,040 字节，0 行差异）。

---

## it-ja（目标语 it，读者母语 ja）

校对文件（SHA 前 12）：印 PDF `La-Lucerna-VOL4-JA.pdf` 21,050,074 字节 `52ed13225c1b`；网 PDF `La-Lucerna-VOL4-JA-web.pdf` 1,697,194 字节 `4f256d24c59e`；text.md `2026-w47-it-ja.text.md` 58,165 字节 `5ac2ecf5abb2`。

### it-ja 结论

**问题：F-2 轻微 + F-3 轻微（CJK 标点部分为讲解文本合法用法，模板 7 处同在）。其余零问题。**

- **F-1 不适用**：P1 标语与日期间距 63px，干净。
- **F-2（轻微）**：P6 时间线 `MAR 17 NOV.Scade` 同 it-en。
- **F-3（轻微）**：P8 答案注全角冒号 38 处（SVG）/ 64 处（text.md）——其中多数为日语讲解文本内的合法全角标点，但与 it-en 相同的 7 处模板实例同在。
- **观察——Q44/Q134 答案注不完整**：日语注为 `主語 + 動詞`，en/de 注为 `Subject + verb + place + date`；同 fr/es/pt/nl/ru 版情况，非错误。注：Q136 日语注为 `主語 + 動詞 + 場所`，与 en 一致、完整。
- P1–P8 看图：除 F-2 外无溢出/重叠/压页脚/截断；盒标题无顶出（boxtitle 门 24 titles / 341 body lines，0 DEFECT）；日语长讲解换行干净；CJK 手写变体块（P1 ADESSO TU 位置等）为已裁定保留现状，不当作缺陷。
- 日语讲解层（401 行差异行全读）：翻译准确——`LA FRASE PER RICORDARE　覚えておこう`（「记住」之义，译法正确；fr/pt/nl 的「格言」译误不存在于此版）、NOTE 各条（`il ponte votivo, 奉納の橋`、`la candela, ろうそく`、`il corteo, パレード`、`lo sbandieratore, 旗手`、`il debutto, デビュー`）、题干译文（`イタリア語で文を完成させなさい`、`単語と意味を合わせなさい`、`正誤問題`、`文を作りなさい`）、答案注（`bene の比較級は不規則で meglio`、`so che + 直説法 torna`、`ラツィオは単数なので、動詞も単数です`）、Q137–Q140 翻译（`聖母健康祭では、人々は奉納の橋を渡ります`；`Ogni cifra deve essere chiara — dovere = ～しなければならない`）均正确；`E TU?　あなたは？`、`FRASI DELLA SETTIMANA　今週の名言`、`VALUTAZIONE E RISPOSTE　演習と答え` 栏目标签正确；页脚 `本文はイタリア語　解説は日本語` 正确；刊名通栏 `イタリア語週刊 VOL.4` 与页脚一致。
- 摘要（ABSTRACT.txt，日文）真实具体，含 VOL.4、A2–B2、150問。
- P8 答案与 it-en 逐项一致（集合相等，p8 compare CLEAN；137–139 为日语翻译，属设计差异）。
- 机械门（本派重跑）：p8 CLEAN（150/150）；occlusion 0 flags；boxtitle 0 DEFECT；edge scan 0 TOUCH / 0 NEAR；web 与印 PDF 文字层相同（47,324 字节，0 行差异）。

---

## it-ko（目标语 it，读者母语 ko）

校对文件（SHA 前 12）：印 PDF `La-Lucerna-VOL4-KO.pdf` 15,803,764 字节 `9815a52d5e9b`；网 PDF `La-Lucerna-VOL4-KO-web.pdf` 1,484,263 字节 `35a222e5f920`；text.md `2026-w47-it-ko.text.md` 57,326 字节 `d4d0c6c1a004`。

### it-ko 结论

**问题：F-2 轻微 + F-3 轻微（CJK 标点部分为讲解文本合法用法，模板 7 处同在）。其余零问题。**

- **F-1 不适用**：P1 标语与日期间距 147px，干净。
- **F-2（轻微）**：P6 时间线 `MAR 17 NOV.Scade` 同 it-en。
- **F-3（轻微）**：P8 答案注全角冒号 7 处（SVG）/ 14 处（text.md）——与 it-en 相同的 7 处模板实例同在。
- **观察——Q44/Q134 答案注不完整**：韩语注为 `주어 + 동사`，en/de 注为 `Subject + verb + place + date`；同 fr/es/pt/nl/ru/ja 版情况，非错误。注：Q136 韩语注为 `주어 + 동사 + 장소`，与 en 一致、完整。
- **已知非缺陷（已核实）**：网 PDF 与印 PDF 文字层仅差 1 个换行符——`이탈리아어 주간지` 一行在两份 pdftotext 输出中位置不同（印 46,790 字节 / 网 46,789 字节，差 1 字节）；为 pdftotext 分行噪声，非缺陷。
- P1–P8 看图：除 F-2 外无溢出/重叠/压页脚/截断；盒标题无顶出（boxtitle 门 36 titles / 493 body lines，0 DEFECT）；韩语长讲解换行干净；CJK 手写变体块（P1 ADESSO TU 位置等）为已裁定保留现状，不当作缺陷。
- 韩语讲解层（401 行差异行全读）：翻译准确——`LA FRASE PER RICORDARE　기억해 두세요`（「记住」之义，译法正确；fr/pt/nl 的「格言」译误不存在于此版）、NOTE 各条（`il ponte votivo, 서원의 다리`、`la candela, 초`、`il corteo, 행렬`、`lo sbandieratore, 기수`、`il debutto, 데뷔`）、题干译文（`이탈리아어로 문장을 완성하세요`、`단어와 뜻을 연결하세요`、`참 거짓 판단`、`문장 만들기`）、答案注（`bene의 비교급은 불규칙형 meglio`、`so che + 직설법 torna`、`라치오는 단수이므로 동사도 단수입니다`）、Q137–Q140 翻译（`성모 건강 축일에는 사람들이 서원의 다리를 건넌다`；`Ogni cifra deve essere chiara — dovere = ~해야 한다`）均正确；`E TU?　당신은요?`、`FRASI DELLA SETTIMANA　이번 주의 명문장`、`VALUTAZIONE E RISPOSTE　연습과 정답` 栏目标签正确；页脚 `텍스트는 이탈리아어　해설은 한국어` 正确；刊名通栏 `이탈리아어 주간지 VOL.4` 与页脚一致。
- 摘要（ABSTRACT.txt，韩文）真实具体，含 VOL.4、A2–B2、150개。
- P8 答案与 it-en 逐项一致（集合相等，p8 compare CLEAN；137–139 为韩语翻译，属设计差异）。
- 机械门（本派重跑）：p8 CLEAN（150/150）；occlusion 0 flags；boxtitle 0 DEFECT；edge scan 0 TOUCH / 0 NEAR；web 与印 PDF 文字层除上述 1 换行外相同。

---

## it-zh-tw（目标语 it，读者母语 zh-tw）

校对文件（SHA 前 12）：印 PDF `La-Lucerna-VOL4-ZH-TW.pdf` 14,906,567 字节 `78f1e78c3697`；网 PDF `La-Lucerna-VOL4-ZH-TW-web.pdf` 1,639,361 字节 `4a4a3f58fac3`；text.md `2026-w47-it-zh-tw.text.md` 52,494 字节 `c18ad203cf49`。

### it-zh-tw 结论

**问题：F-2 轻微 + F-3 轻微（CJK 标点部分为讲解文本合法用法，模板 7 处同在）+ 1 条轻微（P2 口訣标签译误）。其余零问题。**

- **F-1 不适用**：P1 标语与日期间距 122px，干净。
- **F-2（轻微）**：P6 时间线 `MAR 17 NOV.Scade` 同 it-en。
- **F-3（轻微）**：P8 答案注全角冒号 37 处（SVG）/ 62 处（text.md）——其中多数为繁体中文讲解文本内的合法全角标点，但与 it-en 相同的 7 处模板实例同在。
- **轻微——P2 `LA FRASE PER RICORDARE` 盒标题译为 `口訣`**（口诀/格言、座右铭类）。该栏是「要记住的句子」，en 用 `LEARN`、de `MERKE`、es `PARA RECORDAR`、ru `ЗАПОМНИТЕ`、ja `覚えておこう`、ko `기억해 두세요` 均表「记住」；`口訣` 不表「记住」，与 fr `DEVISE`、pt `LEMA`、nl `LEUS` 同属一类译误。本家庭第 4 例。
- **观察——Q44/Q134 答案注不完整**：繁体注为 `主語 + 動詞`，en/de 注为 `Subject + verb + place + date`；同 fr/es/pt/nl/ru/ja/ko 版情况，非错误。注：Q136 繁体注为 `主語 + 動詞 + 地點`，与 en 一致、完整。
- **已知非回归（只报观察）**：P1 `LA SETTIMANA IN CIFRE` 标题余量 +0.5px，P1 看图标题完整无顶出。
- P1–P8 看图：除 F-2 外无溢出/重叠/压页脚/截断；盒标题无顶出（boxtitle 门 26 titles / 323 body lines，0 DEFECT）；繁体长讲解换行干净；CJK 手写变体块（P1 ADESSO TU 位置等）为已裁定保留现状，不当作缺陷。
- 繁体中文讲解层（401 行差异行全读）：翻译准确——NOTE 各条（`il ponte votivo, 還願橋`、`la candela, 蠟燭`、`il corteo, 遊行隊伍`、`lo sbandieratore, 旗手`、`il debutto, 首次亮相`）、题干译文（`用義大利語補全句子`、`把詞和釋義配對`、`判斷對錯`、`造句`）、答案注（`bene 的比較級是不規則的 meglio`、`so che + 陳述式 torna`、`拉齊奧是單數，動詞用單數`）、Q137–Q140 翻译（`聖母健康節人們走過還願橋`；`Ogni cifra deve essere chiara — dovere = 必須`）均正确；`E TU?　說說你自己`、`FRASI DELLA SETTIMANA　本週金句`、`VALUTAZIONE E RISPOSTE　練習與答案` 栏目标签正确；页脚 `正文義大利語　講解繁體中文` 正确；刊名通栏 `義大利語週報 VOL.4` 与页脚一致。**繁简独立核实**：本版用臺灣用語（義大利語、拉齊奧、義甲、那不勒斯、科莫、貝加莫、烏迪內斯），与简体版各自独立、未互译，符合规则。
- 摘要（ABSTRACT.txt，繁体中文）真实具体，含 VOL.4、A2–B2、150 道练习。
- P8 答案与 it-en 逐项一致（集合相等，p8 compare CLEAN；137–139 为繁体中文翻译，属设计差异）。
- 机械门（本派重跑）：p8 CLEAN（150/150）；occlusion 0 flags；boxtitle 0 DEFECT；edge scan 0 TOUCH / 0 NEAR；web 与印 PDF 文字层相同（43,976 字节，0 行差异）。

---

## core-it（目标语 it，读者母语 zh-cn）

校对文件（SHA 前 12）：印 PDF `La-Lucerna-VOL4.pdf` 14,833,164 字节 `f867980ae60d`；网 PDF `La-Lucerna-VOL4-web.pdf` 1,540,034 字节 `aceaf1055042`；text.md `2026-w47-it-zh-cn.text.md` 52,655 字节 `9eb9ee066254`。注：本版 PDF 文件名不带 ZH-CN 后缀（与 fan-out 版命名不同），已按实际文件名核对。

### core-it 结论

**问题：F-2 轻微 + F-3 轻微（CJK 标点部分为讲解文本合法用法，模板 7 处同在）+ 1 条轻微（P2 口诀标签译误）+ 1 条轻微（页脚与摘要缺配对标注）。其余零问题。**

- **F-1 不适用**：P1 标语与日期间距 121px，干净。
- **F-2（轻微）**：P6 时间线 `MAR 17 NOV.Scade` 同 it-en。
- **F-3（轻微）**：P8 答案注全角冒号 37 处（SVG）/ 62 处（text.md）——其中多数为简体中文讲解文本内的合法全角标点，但与 it-en 相同的 7 处模板实例同在。
- **轻微——P2 `LA FRASE PER RICORDARE` 盒标题译为 `口诀`**（口诀/格言、座右铭类）。该栏是「要记住的句子」，en 用 `LEARN`、de `MERKE`、es `PARA RECORDAR`、ru `ЗАПОМНИТЕ`、ja `覚えておこう`、ko `기억해 두세요` 均表「记住」；`口诀` 不表「记住」，与 fr `DEVISE`、pt `LEMA`、nl `LEUS`、zh-tw `口訣` 同属一类译误。本家庭第 5 例。
- **轻微——页脚与摘要缺配对标注**：8 版页脚均为 `La Lucerna 意大利语周报 VOL.4　LUCERNA ITALIAN WEEKLY`（文字层核实，8 处），未像其余 10 版那样标注配对（例 zh-tw 页脚 `正文義大利語　講解繁體中文`）；摘要亦只写「意大利语 A2–B2」，未像其余 10 版那样写明讲解语言（例 en `Italian text with explanations in English`、zh-tw `義大利語正文與繁體中文講解`）。本版标题与讲解内容本身仍明确为简体中文读者版，故为轻微不一致，非内容错误。
- **Q44/Q134 答案注完整**：简体注为 `主语 + 动词 + 地点 + 日期`，与 en/de 一致；fr/es/pt/nl/ru/ja/ko/zh-tw 8 版的缩短注问题不存在于本版。Q136 简体注为 `主语 + 动词 + 地点`，与 en 一致。
- P1–P8 看图：除 F-2 外无溢出/重叠/压页脚/截断；盒标题无顶出（boxtitle 门 26 titles / 318 body lines，0 DEFECT）；简体长讲解换行干净；CJK 手写变体块（P1 ADESSO TU 位置等）为已裁定保留现状，不当作缺陷。
- 简体中文讲解层（401 行差异行全读）：翻译准确——NOTE 各条（`il ponte votivo, 还愿桥`、`la candela, 蜡烛`、`il corteo, 游行队伍`、`lo sbandieratore, 旗手`、`il debutto, 首次亮相`）、题干译文（`用意大利语补全句子`、`把词和释义配对`、`判断对错`、`造句`）、答案注（`bene 的比较级是不规则的 meglio`、`so che + 陈述式 torna`、`拉齐奥是单数，动词用单数`）、Q137–Q140 翻译（`圣母健康节人们走过还愿桥`；`Ogni cifra deve essere chiara — dovere = 必须`）均正确；`E TU?　说说你自己`、`FRASI DELLA SETTIMANA　本周金句`、`VALUTAZIONE E RISPOSTE　练习与答案` 栏目标签正确；刊名通栏 `意大利语周报 VOL.4`。**繁简独立核实**：本版 text.md 内繁体字（週/讀/義大利）出现 0 次，全为简体用语（意大利语、拉齐奥、意甲、那不勒斯、科莫、贝加莫、乌迪内斯），与繁体版各自独立、未互译，符合规则。
- **核心版特有写法（非缺陷）**：P1 `LA SETTIMANA IN CIFRE` 数字框用意大利语句 + 中文括号释义（例 `29 — i punti della Lazio, prima in classifica dopo 11 giornate（拉齐奥 29 分领跑）`），与 fan-out 版的纯中文行不同——为核心版模板写法，内容一致。
- 摘要（ABSTRACT.txt，简体中文）真实具体，含 VOL.4、A2–B2、150 道练习；唯缺配对语言说明（见上条轻微）。
- P8 答案与 it-en 逐项一致（集合相等，p8 compare CLEAN；137–139 为简体中文翻译，属设计差异）。
- 机械门（本派重跑）：p8 CLEAN（150/150）；occlusion 0 flags；boxtitle 0 DEFECT；edge scan 0 TOUCH / 0 NEAR；web 与印 PDF 文字层相同（43,859 字节，0 行差异）。

---

## 总结（11 版全校完）

**结论：有问题——结论类型 (b)。11 版均已全量通读（每版 P1–P8 看图 + 讲解层差异行 100% 通读 + P8 答案逐项复核 + 摘要 + web/印文字层比对），无一版零问题。**

### 问题总表

| 编号 | 严重度 | 范围 | 位置 / 内容 |
|---|---|---|---|
| F-1 | 严重 | 5 版：en、fr、pt、nl、ru | P1 刊头行：中央标语末词压住右侧日期 `SETTIMANA…` 首词，词界消失（en ~8px、fr/nl/ru 字形互压、pt 零间距） |
| F-2 | 轻微 | 11 版全家 | P6 `LA STRADA DELLA MANOVRA` 时间线 `MAR 17 NOV.` 行：`NOV.Scade` 零间距贴住正文 |
| F-3 | 轻微 | 11 版全家（模板 7 处） | P8 答案注：全角冒号 `：` 用在拉丁文内，如 `attraversare：i veneziani → attraversano`（拉丁读者版 SVG 各 7 处；CJK 版另有讲解文本内合法全角标点） |
| F-4 | 轻微 | 5 版：fr、pt、nl、zh-tw、zh-cn | P2 `LA FRASE PER RICORDARE` 盒标题译作「格言/口诀」（`DEVISE` / `LEMA` / `LEUS` / `口訣` / `口诀`），不表「记住」 |
| core-1 | 轻微 | 仅 core-it/zh-cn | 8 版页脚均为 `LUCERNA ITALIAN WEEKLY`，无配对标注；摘要亦缺讲解语言说明（其余 10 版页脚与摘要均有配对标注） |

### 逐版问题计数

- it-en：F-1 严重 + F-2、F-3 轻微（3 条）
- it-de：F-2、F-3 轻微（2 条；P1 刊头紧但未撞，观察）
- it-fr：F-1 严重 + F-2、F-3、F-4 轻微（4 条）
- it-es：F-2、F-3 轻微（2 条）
- it-pt：F-1 严重 + F-2、F-3、F-4 轻微（4 条）
- it-nl：F-1 严重 + F-2、F-3、F-4 轻微（4 条）
- it-ru：F-1 严重 + F-2、F-3 轻微（3 条）
- it-ja：F-2、F-3 轻微（2 条）
- it-ko：F-2、F-3 轻微（2 条）
- it-zh-tw：F-2、F-3、F-4 轻微（3 条）
- core-it/zh-cn：F-2、F-3、F-4、core-1 轻微（4 条）

### 已核实无问题的方面（全家）

- 意大利语核心正文 11 版字节一致；事实/日期/星期（意甲第 11 轮 24 球、积分榜、BookCity 15 届、Torrone 29 届、Eurochocolate 32 届、1630 誓愿、1631–1687 教堂、1898/2013 植树节等）全部一致、真实；P8 答案 150/150 与题面/原文/图表一致（p8 compare 10/10 CLEAN）。
- D5 重建到位：讲解层拉丁文在 Newsreader 内，弯引号 U+201C/U+201D/U+2019 在 Newsreader 内；盒标题无一顶出（boxtitle 11 版 0 DEFECT）；P8 无变长溢出；occlusion 0 flags；edge scan 0 TOUCH / 0 NEAR。
- 讲解层翻译：11 版差异行（每版约 400 行）全部通读，NOTE、题干、答案注、Q137–Q140 翻译均正确（除 F-4 标签译误外）；繁简各自独立，未互译（core text.md 繁体字 0 次）。
- 摘要 11 版均为读者母语、真实具体、含 VOL.4、A2–B2、150 道练习（唯 core 摘要缺配对语言说明，见 core-1）。
- web 与印 PDF 文字层：10 版完全相同；it-ko 仅差 1 换行（已知 pdftotext 噪声，非缺陷）。

### 观察（非问题）

- F-5：Q44/Q134 答案注在 8 版缩短为仅「主语 + 动词」，漏地点与日期；en、de、core-it 三版为完整注。
- it-de P1 刊头间距 9px，紧但字形清晰。
- it-zh-tw P1 `cifre` 标题余量 +0.5px（已知非回归）。
- CJK 版手写变体块（已裁定保留）、it-ko 1 换行文字层差异（已知噪声）。

### 门控盲区（记录）

- F-1（刊头重叠）与 F-2（时间线标签贴文）均不在 occlusion / boxtitle / edge 三门覆盖范围内——四门全绿时仍存在可见缺陷。F-4（标签译误）与 core-1（页脚缺配对）亦为人工通读发现，机械门不覆盖。

### 校对条件（收尾核实）

- tools/ git HEAD：`b9ac29a6f3c640f408965572823e5a1ccebfd1e5`，开工与收尾一致，未变；四门均由本派在该 HEAD 下重跑。
- 磁盘：收尾 `df` 已用 93G（阈值 100G），与开工一致，未超限。
- 未做任何修复、重建、commit、push、lint；只读/写 production/2026-w47/ 与 hidden_files/w47/。
