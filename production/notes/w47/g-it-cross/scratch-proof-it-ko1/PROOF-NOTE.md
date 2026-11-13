# PROOF-NOTE — Lucerna Weekly 2026-W47 it-ko（proof1，独立复校）

- 复校员：proof1（只读复校；未修版、未 commit、未 push）
- 复校日期：2026-11-11
- 复校对象：`~/workspace/weekly-git/production/2026-w47/2026-w47-it-ko/`
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-it-ko1/`

## 0. SHA 核对（三件与任务书一致，复校前已验）

| 文件 | 大小 | SHA256 | 核对 |
|---|---|---|---|
| `La-Lucerna-VOL4-KO.pdf`（印刷） | 19,296,953 B | `522008ebdfed52952fc51ebdabae6ab69af7a30ae92a70610b1cd99409c5a517` | ✅ 一致 |
| `La-Lucerna-VOL4-KO-web.pdf`（网页） | 1,575,451 B | `a9bdc956ca19be6fd5acc37df5ee6e54f3fd2afdc43b456ba7f131d131652763` | ✅ 一致 |
| `2026-w47-it-ko.text.md`（文本导出） | 57,376 B，1,317 行 | `10fdd97935a99a8851c55ce12fdd1148e36d7d9431d9e3c5f0bb49f97632cc81` | ✅ 一致 |

先读：SOP.md §1.1、§8、§9 全文；`AGENTS.md`；协调员 brief；该版 KIT 全文。均已读。

## 1. 门禁全套（日志均在 scratch 目录）

| 门禁 | 结果 | 日志 |
|---|---|---|
| p8 compare（core-it 对 it-ko，`--core-p8/--edition-p8` 显式路径，150 题） | ✅ CLEAN，150/150 noted 两边一致；keydiff 仅 [137, 138, 139]（预期：重定向的读者句键） | `p8-compare.log` |
| p8 extract（本版） | ✅ noted 150/150 | `p8-extract.json` |
| freeze diff（`--core-svg` 指 core-it/svg） | ✅ rc=0；新增拉丁词全部为换行/复合碎片（见下注） | `freeze-diff.log`、`freeze-diff.json` |
| freeze baseline（从 core-it 源码重建 8 页 SVG 并比对） | ✅ **8/8 byte-identical**；shipped core SVGs 未被本次运行改动 | `freeze-baseline.log` |
| occlusion_audit（自检 6 类植入缺陷全触发、干净对照静默） | ✅ **0 flags** | `occlusion.log` |
| creambox（canonical 工具，+45px 窗口 + 逐行表 + P7 汇总） | ✅ 见 §4；最紧实测盒底清除 +4.5px，9 张放大截图逐一目视确认墨迹不超盒底 | `creambox.log`、`creambox-core-p4.log` |
| 印刷/网页 text layer 比对（`pdftotext`） | ✅ 词 multiset 完全相同（各 7,426 词）；字符 multiset 仅差 1 个 "\n"（网页版尾部换行提取伪影，非内容差） | `print.txt`、`web.txt` |
| P8 最小字号（PyMuPDF 实测渲染 pt） | ✅ 最小 **9.75pt**（RISPOSTE 键 520 个 span；其余 10.5 / 11.62…），符合 SOP §1.1 下限 9.75pt；P1–P5、P7 最小 11.62pt，P6 最小 12.75pt | — |
| BOXTITLE 真墨迹宽度（PyMuPDF 实测每盒首行墨迹右缘 vs 盒右缘） | ✅ 全部正余量；最紧 P6 해설盒首行 +15.6pt，其余 +23.4pt 以上 | — |
| 横向漫出（全页 span 右缘 vs 版心右缘 1396.5pt） | ⚠️ **仅 P2 两行超出版心**（见 D2）；其余各页最大右缘 ≤1398.4pt（P5 图注 +1.6、P8 范文 +1.9，取整/字距噪声，可忽略） | — |
| P7 工具盒盒底清除量 | ✅ ERRORI TIPICI +18.1（desc +12.2）、LA PAROLA +4.5、LETTERE +5.1；P7 汇总：3 盒，最小盒内清除 +4.5，最小 desc-clear −1.5（见 §4 注） | `creambox.log` |
| VOL.4 / VOL.5 计数（SVG grep） | ✅ VOL.4 ×9、VOL.5 ×3（合法节点），与 KIT 一致 | — |
| "·" 计数（SVG） | ✅ 151，与 KIT 一致 | — |
| 网页 PDF 图片/字体 | ✅ 7 图、P1 6 字体；与印刷版图数一致 | — |

**注 — freeze 门禁的盲区（本次复校的新发现，见 D2）：**`freeze.py` 只做 CJK 会计（`CJK_RE` 统计新增 CJK 字符；`added_strings`/`removed_strings` 仅保留含 CJK 的行）。纯拉丁语目标文本的改动对它完全不可见——本次 D2 的两处意大利语选项改动未进 freeze 的 added/removed 清单。p8 compare 只比键值，不比题干语义。两处改动是靠 content 文件逐行 diff（见 D2）才抓到的。建议：freeze 增加拉丁语行比对，或在 fan-out 后对 content*.py 做非 CJK 行 diff。

## 2. 事实核对（公开来源逐条查验，2026-11-11）

全部已确认，除 D1 外无事实错误：

- **意甲第 11 轮（11 月 6–8 日）**：10 场比分与纸面完全一致（Venezia–Udinese 2–1、Cagliari–Frosinone 1–0、Torino–Lecce 1–1、Parma–Bologna 1–2、Roma–Sassuolo 3–0、Napoli–Lazio 1–1、Genoa–Milan 1–2、Monza–Atalanta 0–1、Inter–Como 2–0、Fiorentina–Juventus 2–2）；共 24 球；积分 Lazio 29、Inter 28、Roma 27、Milan 24、Como 23、Udinese 5（垫底）；Roma 最佳攻击 31 球；"Lazio di Gattuso" 多源确认（Gattuso 2026-27 赛季执教 Lazio）。
- **ATP Finals 都灵 11 月 15–22 日**：Zverev 世界第一、Sinner 右膝伤缺（2024+2025 冠军）、Cobolli 首秀、决赛 11 月 22 日周日、8 人 2 组——均确认。
- **克雷莫纳牛轧糖节**：第 29 届，11 月 7–22 日，主题 «Il Confine»，16 天/3 个周末；Torrone d'Oro 授予 Davide Simonetta（克雷莫纳出生制作人），11 月 22 日周日 11:00 Palatorrone；巡游 16:00、150+ 扮演者；Sforza–Visconti 婚礼重演 17:00 Piazza del Comune；«Il torrone va in brodo» 18:00 收尾——均确认（含 festadeltorrone.com 官网）。1441 年 10 月 25 日婚礼传说、Torrazzo 为意大利最高钟楼——确认。
- **Eurochocolate 佩鲁贾**：第 32 届，11 月 13–22 日，主题 «Fate dolci»；Calabria 首个客座大区（bergamotto、cedro、peperoncino、fichi）；«I tesori della Calabria Straordinaria» 11 月 20 日周五 18:15 LAB-Luisa Annibale；Iginio Massari 11 月 22 日闭幕——均确认。
- **BookCity 米兰**：第 15 届，11 月 23–29 日，主题 «Il senno sulla Luna»（Ariosto《Orlando furioso》）；1,360 场、2,487 人、1,164 书、443 场地；开幕 11 月 23 日周一 20:00 Teatro Dal Verme，嘉宾 Colson Whitehead（2 届 Pulitzer）；预展 11 月 22 日周日 16:00 Fondazione Luigi Rovati，Edmund de Waal——均确认。
- **都灵电影节**：第 44 届，11 月 24 日周二–12 月 2 日周三，9 天（官网章程）；**Filmmaker 电影节米兰**：11 月 14–22 日，11 月 22 日周日闭幕——均确认。
- **Manovra 2027**：DPB 10 月 15 日送布鲁塞尔；2027 增长 +0.8% / 赤字 3.4%；CdM 10 月 28 日通过法案；法案号 C. 3174-bis；听证 11 月 9–12 日（Giorgetti 11 月 12 日周四）；修正案截止 11 月 17 日周二 18:00；2026 年 12 月 31 日前终批；银行/保险业约 50 亿；IRPEF 第二档 33% 扩至 €55,000（原 €50,000）；卫生拨款增加——均确认。**"Circa 26 miliardi" 可辩护**：政府公报称 2027 年约 €26bn（另有按 DPB 的 €23.5bn 重构）；纸面写 "circa 26 miliardi di euro, secondo le ricostruzioni dei giornali"——非缺陷。
- **Nations League**：Italy–France 11 月 12 日周四 20:45 San Siro；Belgium–Italy 11 月 15 日周日 20:45 布鲁塞尔——确认。纸面正确地未印结果（截稿后比赛）。
- **意甲第 12 轮**：Lazio–Lecce 11 月 21 日周六 15:00；Atalanta–Inter 11 月 22 日周日 20:45 贝加莫（New Balance Arena）；Monza–Fiorentina 11 月 23 日周一 20:45；第 12 轮 11 月 21 日周六–23 日周一——均确认（DAZN、atalanta.it）。
- **Madonna della Salute**：1630 年 10 月 22 日许愿（瘟疫）；教堂 Baldassarre Longhena 设计，1631 年建、1687 年 11 月祝圣；许愿浮桥（历史上船桥，现为浮桥）；castradina 传统菜——确认。**Castradina "si mangia la sera prima, il 20 novembre" 已验**（多源：传统上在前夜/守夜吃，11 月 20 日）。
- **全国植树日**：首届 Festa dell'albero 1898 年（Baccelli 部长），2013 年第 10 号法律定为国家日，11 月 21 日——确认。**Alba 白松露集市至 12 月 6 日**——确认。Santa Cecilia 11 月 22 日、音乐主保——常识，未单查。
- 星期：2026 年 11 月 16 日周一…22 日周日、17 日周二、24 日周二，均与纸面一致。

## 3. 语言与练习键核对

- **150 题键与题干语义逐一核对**：匹配题 Q25–28（P2）、Q52–55（P4）、Q141–144（P8）逐项对选项原文核过，键全部正确；其余：现在时/将来时/近过去时/虚拟式变位（16–20、40–43、60–64、76–79、93–96、101–111）、比较级（56 più、57 meno、58 più bella、59 meglio）、单选（7–10、21–24、29–33、47–51、65–69、80–82、83–92、113–132）、造句（44–46、133–136）、重定向翻译键 137–140（137 "성모 건강 축일에는 사람들이 서원의 다리를 건넌다." ✓；138 "일요일 저녁, 아탈란타가 인터와 경기한다." ✓；139 "토요일, 라치오는 홈에서 레체와 경기한다." ✓；140 "Ogni cifra deve essere chiara." ← "모든 숫자는 분명해야 합니다." ✓）、对话 145–149 ✓、写作 150 范文实数 99 词 ✓。
- **FRASI DELLA SETTIMANA（P7，8 句）**：每句均在正文找到出处（P1 «La Lazio resta in vetta»、《ventiquattro gol in dieci partite》；P2 «il ponte votivo sul Canal Grande»；P3 «oltre centocinquanta figuranti in costumi rinascimentali»；P4 «la squadra di Gattuso è ancora imbattuta dopo 11 giornate»；P5 «sette giorni di libri, ragioni e follie»；P6 «il testo può ancora cambiare》、《approvato dal governo non vuol dire già legge»），每篇正好 2 句，与 KIT 宣称一致。
- **意大利语语法讲解**：ERRORI TIPICI 全部纠正正确；将来时/近过去时/虚拟式规则正确（含 "so che + 直陈式"、"è probabile che + 虚拟式"）。
- **韩语层**：全 8 页标题、注释、说明、指令流畅一致，无其他语言残留。4 处有意的「翻译」标注（Q137–140）与 frozen 动词变位表中的全角冒号 ：（注 16–20、60–61）按 KIT §8 属有意保留。
- 练习题量：P1 10、P2 18、P3 18、P4 18、P5 18、P6 18、P7 12、P8 38 = 150；级别 A2 47 / B1 70 / B2 33。

## 4. 版式几何（逐页目视 + 工具）

- 8 页印刷 PDF 全页 100 dpi 渲染逐页目视：版式干净，无溢出、无遮挡、无错位（P1 头条、P2/P3/P4/P5/P6/P7/P8 均查）。
- **creambox（canonical，+45px）**：全部盒内清除为正；最紧：P1 CIFRE +45.7、P1 day-by-day +13.5（desc +8.5）、P1 IN QUESTO NUMERO +16.0（desc +9.7）、P2 LO SAPEVI +5.3（desc −1.1）、P2 E TU +5.0（desc −1.0）、P3 IL WEEKEND DOLCE +5.3（desc −1.2）、P3 E TU +4.5（desc −1.5）、P4 E TU +4.5（desc −1.5）、P4 LA CLASSIFICA +26.0、P5 I GIOVANI IN NUMERI +5.3（desc −1.1）、P5 E TU +4.5（desc −1.5）、P6 MINIME +31.2、PROPOSTA +90.0、LEGGERE I NUMERI +19.4、P7 ERRORI TIPICI +18.1（desc +12.2）、LA PAROLA +4.5（desc −1.5）、LETTERE +5.1（desc −0.9）；P7 汇总：3 盒，最小盒内清除 +4.5，最小 desc-clear −1.5；P8 无奶油盒。**desc-clear 负值全部是 0.30em 拉丁下行字母模型的误报**：对应末行无任何下行字母（拉丁行 "della musica e dei musicisti."、"continua fino al 6 dicembre."；韩文行 "에 보내세요."、"문장을 써서 보내세요."、"아어로 두 문장을 써서 보내세요."、"치오가 29점으로 선두."、"습니다. 약속은 VOL.5로 이어집니다."——韩文无下行字母）。
- **9 张最紧盒底放大截图逐一目视**（`crop-p2-vita-y617.png`、`crop-p2-vita-y987.png`、`crop-p3-cultura-y647.png`、`crop-p3-cultura-y1047.png`、`crop-p4-sport-y927.png`、`crop-p5-giovani-y667.png`、`crop-p5-giovani-y1037.png`、`crop-p7-lingua-y1040.png`、`crop-p7-lingua-y1370.png`）：末行墨迹全部在盒内，盒底留有奶油边。例：P7 LA PAROLA 末行 "치오가 29점으로 선두." 下方有明确奶油空隙；P7 LETTERE 末行 "습니다. 약속은 VOL.5로 이어집니다." 完整在盒内（下方绿线为 FRASI 分隔线，不重叠）；P3 IL WEEKEND DOLCE 末行 "continua fino al 6 dicembre." 在盒内。
- P4 成绩表斑马纹：奶油盒分段衬 VEN、SAB-part-2、DOM-part-2，SAB 7.11 / DOM 8.11 标题重复、行分段跨带；core-it P4 creambox 结构完全相同——属 core 设计，渲染干净、读感有意，非本版缺陷。
- P5 词表折行（"anteprima · protagonista · sede · incontro" / "· indipendente · lettrice"，第二行以 "·" 开头）：KIT §10 已披露，与 ja 版相同，视觉可接受，非新缺陷。
- P3 "IL TORRAZZO E IL TORRONE" 下方中段留白：KIT 已披露的 core  pattern，原样保留。
- P6 图表 Torino 5°/Milano 6°/Bologna 7°/Roma 11°/Napoli 13°，带 "(DATI INVENTATI PER L'ESERCIZIO)" 标注与 "NON sono previsioni reali" 说明；PROPOSTA ≠ LEGGE 盒；均干净。
- P7 LETTERE：编辑示例 + 韩语披露（"이것은 편집부의 예시이며 실제 편지가 아닙니다. 실제 편지와 최우수 작문이 도착하지 않았습니다. 약속은 VOL.5로 이어집니다."），无虚构人物。
- P8：A–H 节（113–150）、RISPOSTE 1–150 齐全；答案分组分隔符为韩语形式 "— 제 n 면 —"（SVG 内 제 1 면…제 8 면 均在；core 的 "— PAGINA n —" 在 de/en/es/fr/zh-tw 版保留、ja/ko/nl/pt/ru 版译为本族语，属合法本地化）；答案末行 y=2483.66 与 core 完全一致，末端距页脚有余量；范文 + Vermeer 图干净。
- P1 无首字下沉：KIT 已注为接受项，与 core 相同。

## 5. Abstract（SOP §9）

`ABSTRACT.txt` 单行韩语，无 ASCII 双引号；含 La Lucerna、이탈리아어（目标语）、A2–B2、연습문제 150개（题数）及真实主题（라치오 29점 선두 세리에 A 11라운드、크레모나 토로네 축제、페루자 유로초콜릿、베네치아 성모 건강 축일과 식목일、밀라노 북시티와 토리노 영화제、의회에 상정된 예산안）。**通过 §9。**（尚未入仓，无 frontmatter 可核。）

## 6. 已查清的非缺陷

- **Q32 注释弯引号**：KIT §10 称 Q32 注释用 `"Fate dolci"`（弯引号）而他版用 «Fate dolci»。实查：core-it zh-cn text.md 351/1081 行在注释中用同样弯引号；ko 选项题干用 «Fate dolci» 与 core 一致。各版一致——非缺陷。
- **P1 刊头标语** "OGNI SETTIMANA IN ITALIANO　매주　이탈리아인이 읽는 이탈리아어"：固定标语，各语言版同模式（zh-cn "读意大利人正在读的意大利语"、en "THE ITALIAN THAT ITALIANS ARE READING"、de "DAS ITALIENISCH, DAS ITALIEN LIEST"；translations.py 29–38 行）——非缺陷。
- **KIT 词数 "7,425" vs 本次实测 7,426**：计数方法差异而已；印刷/网页两版词数相等本身成立——非缺陷。
- **P8 分隔符 "— PAGINA n —" 缺失的疑点**：初查以为 ko 缺分隔符，实查 ko content8.py 中分隔符已译为 `— 제 {pg} 면 —`，SVG 内 제 1 면…제 8 면 齐全，答案末行 y 与 core 完全相同——非缺陷（首轮 grep 只搜了 PAGINA 一词，属检查方法问题）。

## 7. 缺陷清单

### D1 — P1 头条时间自相矛盾（core 级，中等严重度）

- **位置**：P1 头条第 3 段，text.md 第 35 行；core-it 同文同行。
- **原文**："Domenica 22 novembre torna la Serie A con la 12ª giornata: la sera, a Bergamo, c'è Atalanta–Inter. Sabato 21 la Lazio capolista gioca in casa con il Lecce."
- **证据**：同一句先说意甲 "22 日周日回归"，紧接着说 Lazio "21 日周六"比赛。**同版内证**：P4 文章 "La Serie A riparte sabato 21 novembre con la 12ª giornata, che si chiude lunedì 23"；P2 日程 "SAB 21 — Madonna della Salute a Venezia; torna la Serie A."。**外证**：DAZN 赛程，第 12 轮始于 11 月 21 日周六 15:00（Como–Cagliari、Lazio–Lecce）。
- **级别**：core 级——该句在 core-it 原文逐字存在，影响全部 it fan-out。
- **修法**：在 core 中把 P1 开头改为 "Sabato 21 novembre torna la Serie A con la 12ª giornata"（或 "La 12ª giornata comincia sabato 21 novembre"），重渲全部 it 版。

### D2 — 两处 frozen 意大利语选项被 fan-out 改写，并导致 P2 两行超出版心右缘（core 级 / fan-out 全域，中等严重度）

- **位置**：P2 匹配题 Q26 选项 b、Q27 选项 d；content12.py 第 264 行附近；text.md 第 289 行附近。
- **原文对照**：
  - Q26 b：core "il ponte di barche per la festa in novembre" → 全部 11 个 it 版（含 ko）"il ponte di barche per la festa del 21 novembre"
  - Q27 d：core "la piccola luce di cera accesa in chiesa" → 全部 11 个 it 版（含 ko）"la piccola luce di cera che si accende in chiesa"
- **证据**：
  1. content 文件逐行 diff（core-it 对 it-ko，5 个 content*.py 全量）：**除解释层中→韩翻译外，仅有的两处非 CJK 行改动就是这两句**；translations.py 中无对应条目（grep "accesa"、"che si accende"、"piccola luce"、"ponte di barche" 均为空）。
  2. **全域性**：de、en、es、fr、ja、nl、pt、ru、zh-tw 10 个他版 content12.py 与 ko 完全相同（均为新措辞），core-it 仍为旧措辞——改动发生在共享 fan-out 步骤，不只 ko。
  3. **几何后果**（PyMuPDF 实测印刷 PDF，版心右缘 1396.5pt = 1462.5 − 66）：Q26 b 首行 "b. il ponte di barche per la festa del 21" 右缘 **1408.2pt（超出版心 +11.7pt）**；Q27 d 首行 "d. la piccola luce di cera che si accende" 右缘 **1409.7pt（+13.2pt）**。core 对应行右缘 1375.1 / 1367.6，均在版心内。300 dpi 放大截图（`crop-p2-options-overflow.png` 对 `crop-p2-options-core.png`）目视确认：ko 版 b、d 两行明显探出右缘、超出 a、c 两行的对齐线；core 版 b、d 行收在版心内、与 a、c 对齐。
  4. **门禁为何漏检**：freeze 只做 CJK 会计，纯拉丁语改动不可见（见 §1 注）；p8 compare 只比键值。新措辞本身意大利语无误（"del 21 novembre" 比 "in novembre" 更精确；"che si accende" 与 "accesa" 均正确）——问题在**改动 frozen 目标文本且未重算版式**。
- **级别**：core 级（fan-out 全域，11 个 it 版同病；修法须在 core/fan-out 层定）。
- **严重度**：中等——两行肉眼可见地探出版心（约 4mm），在练习页，且违反 frozen 目标文本规则。
- **修法**（二选一，core 层定后重渲 11 个 it 版 + core）：
  - (a) core 采纳新措辞为 frozen 文本，同时修 P2 匹配题换行使两行收进版心（例如 b 行在 "festa" 后断开、d 行在 "che si" 后断开）；
  - (b) 11 个 it 版还原 core 措辞（"in novembre"、"accesa"），行长即恢复至版心内（如 core 所示）。

### D3 — P5「IL PIANO DELLA SETTIMANA」盒内两处孤悬 "）"（ko 版级，轻微/外观）

- **位置**：P5「IL PIANO DELLA SETTIMANA」奶油盒，第 2 项与第 3 项韩语注释末尾；SVG `p5-giovani.svg` y=779.8 与 y=891.5；印刷 PDF pt 坐标约 (584.9, 668.6)。
- **证据**：SVG 文本行逐行提取：第 2 项 "2. Sabato: Madonna della Salute a / Venezia（토요일: 베네치아 성모 건강 축일" 后独行 "）"；第 3 项 "3. Domenica: chiude il Filmmaker / Festival（일요일: 필름메이커 영화제 폐막" 后独行 "）"。300 dpi 放大截图 `crop-p5-piano-lone-paren.png` 目视确认：两行仅含一个 "）"，为明显排版瑕疵。全版孤标点扫描（8 个 SVG）仅此两处。core zh-cn 版两处注释均单行容纳（"（周六：圣母健康节）"、"（周日：电影节闭幕）"），无此现象——属 ko 版级（韩语注释较长所致）。
- **非缺陷对照**：第 5 项 "（월 / 요일: 밀라노 북시티 개막）" 在词内断开，但 core 同样在 "（周 / 一：米兰书城开幕）" 处断开——属 core 已有的逐字/逐音节换行模式，不列为缺陷。
- **级别**：ko 版级。
- **严重度**：轻微——外观瑕疵，不影响理解与做题。
- **修法**：缩短两处韩语注释使 "）" 不单独成行（例："（토요일: 베네치아 성모 건강 축일）" → "（토요일: 성모 건강 축일）"；"（일요일: 필름메이커 영화제 폐막）" → "（일요일: 필름메이커 폐막）"），仅重渲 P5。

## 8. 未核实（不作事实陈述）

- P6 "con la Banca d'Italia, l'Ufficio parlamentare di bilancio e il ministro Giorgetti"——听证日期（11 月 9–12 日）与 Giorgetti 11 月 12 日出席已确认；Banca d'Italia / UPB 出席未逐一再验，标记**未核实**，不列为缺陷。
- Santa Cecilia 11 月 22 日为音乐主保——常识，未单查，标记**未核实**。

## 9. Verdict

**(b) 有问题，不可直接定稿。**

- **D1**（core 级，中等）：P1 "Domenica 22 novembre torna la Serie A" 与同版 P2/P4 及赛程事实矛盾——须 core 改文、重渲全部 it 版。
- **D2**（core 级 / fan-out 全域，中等）：两处 frozen 意大利语选项在 fan-out 中被改写（11 个 it 版同病），致 P2 两行超出版心右缘 +11.7 / +13.2pt——须 core 层定修法（采纳新措辞并修换行，或还原 core 措辞），重渲 11 个 it 版 + core；另建议 freeze 增加拉丁语行比对，堵住本次漏检的门禁盲区。
- **D3**（ko 版级，轻微）：P5 PIANO 盒两处孤悬 "）"——缩短两处韩语注释，仅重渲 P5。

除上述三项外：事实、语言、150 题键语义、门禁（p8/freeze baseline 8/8/occlusion 0/creambox/P8 9.75pt/印刷网页 text layer 一致/abstract §9）均通过；修好后须对受影响页（P1、P2、P5）复校回放。
