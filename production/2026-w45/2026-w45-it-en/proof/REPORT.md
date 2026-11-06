# W45 IT×EN 独立校对报告 — 结论：NOT PASS（1 项阻塞）

- 校对对象：`files/weekly-report-w45-it-en/`（SVG×8、卡片×8、print PDF 7,173,236 B sha `6103191a…774eb3`、web PDF 3,570,974 B sha `6f038cbd…f37`、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照核心：`files/weekly-report-w45-it-core/`（只读）；W43 同配对：`files/weekly-report-it-en/`（只读）
- 校对方式：全部机械门禁由本校对独立重跑（工具 `tools/freeze.py`、`tools/p8.py`、`tools/occlusion_audit.py` 及自写扫描 `scan.py`，未使用构建员的 `rightedge.py`/`rowcheck.py`/`chartcheck.py` 输出）；8 张卡片逐页目视。
- 开工查重：首次检查时交付目录最新 mtime 为 23:16（KIT/ABSTRACT），经 90 秒复查零新写盘后开工；唯一运行中的渲染进程属于另一分版（it-de 校对），与本版无关。校对期间未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心与 W43 目录。
- 校对前后哈希：交付 SVG×8 + 核心 SVG×8 + 双 PDF 校对前后 sha256 全部一致（`hashes-pre.txt` = `hashes-post.txt`）。

## 阻塞项（1 项）

### B1 — P7 读者园地：意大利语侧无延期披露句（阻塞）

逐字实测（P7，x=1473 列）：

- 意大利语信件逐字冻结，与核心一致：
  > «Ciao! Sono Li, studio italiano a Pechino. Lunedì metto il cappotto e la sciarpa, sabato assaggio il panettone — almeno in foto!» — Li
  > (esempio della redazione)
- 英语注释（3 行，20pt，行距 28.4）：
  > Editor's sample, not a real letter: no real letters yet, no best page-8 essay yet — both promised for VOL.3. Write to us!
- 下周预告带（P7 底部，意大利语，冻结）：
  > Lunedì 9 novembre: chiude il Festival dei Popoli a Firenze. La Festa del Torrone continua a Cremona fino al 22 novembre. E poi: le vostre lettere vere e i testi migliori della pagina 8. A lunedì!

裁定：

- (a) 意大利语侧页上真实载有的只有两样：示例标签 `(esempio della redazione)`（仅说明“这是编辑部示例”，即信件非真实）与预告行中的 VOL.3 承诺（“下期登你们的真实来信与第 8 版最佳作文”）。**“尚无真实来信、尚无最佳 P8 作文、顺延至 VOL.3”这三项事实的意大利语陈述在页上不存在**——标签不陈述后两项，预告行只作未来承诺，不披露当前缺席。
- (b) 按任务书明示的现行规则：延期披露须在页上以目标语（意大利语）+ 读者母语（英语）双语呈现；预告行不计入邀请、也不等同于披露；KIT-only 披露不通过。英语注释再完整也不能替代缺失的意大利语句子。**故构成阻塞。**构建员的“冻结意大利语标签 + 预告带意大利语承诺 + 英语注释即满足”之解释不予采纳。
- (c) 构建员的 col3 几何主张属实，但不改变结论。实测：FRASI 规则线确在 y=1686（P7 line 65→1885）；col3 末行（英语注释末行）基线 y=1667.95，PIL 墨迹底 ≈1673.95，距规则线仅约 12px（构建员称 1673.0/13px，见观察 O2）；注释行距 28.4px。**加任何一行意大利语披露（哪怕 1 行）都将越过 FRASI 规则**，几何主张成立。然而“没地方加”不是“可以不加”的理由——正确修复是腾出地方，而不是省略披露。
- 修复方向（不得编造来信）：在 LETTERE 框内补一句紧凑的意大利语披露（如实陈述“尚无真实来信、尚无最佳作文，均顺延至 VOL.3”之意），空间三选一：① FRASI 带整体下移约 30px（FRASI 末行墨迹底约 2316，下期预告带标题在 2448，约有 110px 余量）；② col3 注释字号/行距微调；③ 英文注释措辞收紧并与意大利语披露合写为双语注释块。修复后按 SOP §8 须整期重渲染并从头再做一轮全量校对，不得只复查 P7。
- 先例说明：本版结构与 W43 IT×EN 完全同类（W43：意大利语标签 `(lettera di esempio, scritta dalla redazione)` + 英语注释 “A sample letter from the editors, not a real reader's. VOL.2 prints real letters and the best page 8 writing — write to us!” + 意大利语预告承诺）。本裁定执行的是任务书明示的现行规则；若父线认定 W43 先例即现行规则，则 B1 撤销、本版其余门禁全过——此判断请父线确认，但按所给规则结论为 NOT PASS。

## 门禁逐项实测（除 B1 外全部通过）

### 1. 冻结
- `freeze.py baseline` 独立重跑：核心 8/8 逐字节复现（p1 `81051bbb…`、p2 `d42ce9ae…`、p3 `9e45586d…`、p4 `62f75269…`、p5 `c907b869…`、p6 `5545f8dd…`、p7 `9fc999f4…`、p8 `3b87e54f…`），跑后核心重哈希无变化。
- `freeze.py diff`：每页新增 CJK 均为 0（P1–P8 核心 CJK 193/179/169/145/215/149/319/1034 → 分版 0）；全文“桥接”0（SVG、KIT、ABSTRACT 全扫；print PDF 提取文本 0 次，web PDF 为图片型无文本层）。
- 冻结差分逐项核查：P1–P5 被删拉丁字符串为 0；P6 仅 1 条（`bollettino · modello`，系核心 P6 配对集换行片段，分版同页仍有 `· media · bollettino · modello` 及 gloss 全项）；P7 仅 1 条（`è probabile che / è possibile che / bisogna`，系 B2 注释换行，分版同义改写为 `After è probabile che / è possibile che / bisogna che use the subjunctive…`）；P8 被删 9 条拉丁行（#17/#18/#19/#20/#60/#61/#85/#86/#103）均为注释翻译与标点转换（：→:、→→gives、全角括号→半角），其印刷键在分版中逐字节存续。**无意大利语正文丢失。**

### 2. P7 词框硬性门 — 通过
- 定义句逐字保留，与核心逐字节同：
  > « l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere se piace. Questa settimana vive a pagina 3, alla finale del Panettone.
- 仅 gloss 本地化为英语：`assaggio = tasting. See page 3: free tasting at the Panettone final.` 无定义句本地化。
- 金句：全期 8 句在核心与分版中各恰为 2×（P7 引用节点 + 正文出处）；8 个 P7 引用节点逐字在版（见 `text-dumps.txt`）。卡片目视：ERRORI 注释各为 1 行。

### 3. P8 — 通过（两档口径已调和）
- `p8.py compare` 独立重跑：**CLEAN 150=150，missing=[]，extra_count=0，uncertain=[]，keydiff=[6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77, 137, 138, 139]**（与构建员一致）。
- 14 项印刷行逐项核实（P8 答案区首行文本，`—` 前为印刷键）：
  - 11 项括号分支伪影，印刷键逐字节同：#6 previsioni、#13 guanti、#14 crisantemi、#15 termosifoni、#16 fa、#20 resta、#38 mandorle、#58 più bella、#71 gratuiti、#74 castagne、#77 ci sarà。机制：这 11 项的核心注释和/或英语注释均含括号（核心全角（复数）/（天气）/（将有）/（主观评价）等，英语半角 (plural)/(weather)/(lei)/(there will be)/(masculine plural)），`p8.py` 的括号分支在提取印刷键时被注释内括号干扰，产出虚假 keydiff；印刷行本身未变。
  - 3 项真重定向（E 节，指令均为 Translate into English，题干为意大利语句）：#137 `On Monday the first cold arrives.`、#138 `The public can taste for free.`、#139 `Sunday evening: Fiorentina play Juventus.`——与核心中文键逐项对应，改向合法。
  - #140：印刷键逐字节同意大利语 `Ogni previsione deve essere chiara.`，题干重定向为 `Every forecast must be clear. → ___`（指令 Translate into Italian），与 W43 模式一致。
  - #150：印刷行为 `150. ✓ Model text in section H below (81 words)`；H 区桥接句为 `Writing task (no single right answer); the model text (81 words) follows.`；注释纯英语。
- 两档口径调和：注册表字段级 diff（`reg-core.json` vs `reg-en.json`，构建员留档，本校对只作比对引用）为：page/level/type diff **0 项**；note diff 150 项（全部为翻译）；**key diff 仅 #137/#138/#139/#150**。与 p8 compare 的 14 项之差恰为上述 11 项：注册表比较的是答案字段原值（11 项原值未变），而 p8 compare 比较的是工具从印刷行解析出的键（11 项被括号注释干扰）。两档在“印刷键是否变”这一点上经直接印刷行核实一致：11 项未变、3 项真变。不得只采一档——本报告两档均列出并以印刷行为准。
- P8 注释纯英语：分版全页 CJK=0（见 §1），答案区 150 条注释无中文残留。
- 观察 O1（非阻塞，见下）：构建员称“P8 key flow 终 y=2484”与实测不符。

### 4. 几何 — 通过（自写独立扫描，未用构建员脚本）
- `occlusion_audit.py` 独立重跑（自检 6 类全触发）：分版 **0 旗**、核心 **0 旗**、NEW vs 核心 **0 旗**。
- 同基线碰撞（自写扫描，按基线分组、advance 宽、相邻间距 <5px 计旗）：分版 7 旗 = 核心 7 旗，**逐项文本与间距完全相同**（sommario 标签/标题对，设计间隙 4.0px，无重叠，属继承）——构建员称属实。
- P6 图表标签覆盖（自写扫描，PIL getmetrics 基线锚定墨迹带 × 后绘矩形）：最差覆盖 **0.0%**（门限 <30%），卡片目视 Torino 3°/Milano 4°/Bologna 5°/Roma 9°/Napoli 12° 全部完整。
- 全 8 页框线压框 + 右缘扫描（自写扫描，anchor start/middle/end 全处理）：
  - 右缘 >1910（内框线）违规：**0 条**；出页边/压外框：**0 条**。
  - 边距区 (1885, 1910] 条目恰为 4 条，且逐条文本与右缘值与核心对应条目一致：P1 parola 行 ×2（1889.3/1888.8）、P2 配对右行（1902.5）、P8 H 题干行（1898.6）——均为冻结意大利语行，属继承（构建员称属实）。
  - 全页内容底：距页脚线（2580）最近的是 P5 词框行（基线 2565.9，墨迹底约 2571，约 9px 余量），审计 FOOTER 0 旗，卡片无压脚。
- P7 col3：末行基线 1667.95，墨迹底 ≈1673.95，FRASI 规则线 y=1686（P7 line 实测），余量约 12px（见 O2）。
- P8 key flow：各列末行基线 col1 2536.40（#37）、col2 2532.76（#75）、col3 2504.44（#112，另分隔行 2533.76）、col4 2468.84（#150）；全局墨迹底约 2540，距页脚线 2580 约 40px，FOOTER 0 旗（见 O1）。
- Round 4 变更范围实测：`baseline-round3-pre.txt` vs `baseline-round4.txt` 仅 P1/P2/P4/P8 的 SVG 与卡片 + 双 PDF 变化，P3/P5/P6/P7 SVG 哈希未变；已交付文件与 round4 基线逐项一致。构建员“round 4 恰为 P1/P2/P4/P8 变化”之称属实。构建员自承的 round 3 扫描 bug（相对路径 glob 为空、anchor 正则 bug）已规避：本校对全部几何结论来自自写扫描与 canonical 工具，与其脚本无关。

### 5. gloss — 通过（渲染后按 · 拆分，从核心独立实测）
| 页 | 核心（译注｜） | 分版（NOTE ·） | 词头 1:1 |
|---|---|---|---|
| P2 | 6：il cappotto/la sciarpa/i guanti/a strati/il termosifone/il crisantemo | 6，同序 | ✓ |
| P3 | 5：il panettone/il torrone/l'assaggio/la bancarella/il cantiere | 5，同序 | ✓ |
| P4 | 4：la giornata/la presentazione/gli spalti/la sera | 4，同序 | ✓ |
| P5 | 4：il cosplay/gratuito/il documentario/lo schermo | 4，同序 | ✓ |
| P6 | 5：la probabilità/la media/il modello/il bollettino/aggiornare | 5，同序 | ✓ |
| 合计 | **24** | **24** | ✓ |

### 6. 读者园地 — 见阻塞项 B1（重点裁定如上）

### 7. 家具（与 W43 IT×EN 实测对照）— 通过（除 B1 的规则适用外）
- 徽章：P1 (975, 574) 22pt BRICK，`Text in Italian · Explanations in English — the edition for English-speaking readers`，与 W43 同位同式（VOL 随期变）。
- 页脚：`La Lucerna · ITALIAN WEEKLY VOL.2 · TEXT IN ITALIAN · EXPLANATIONS IN ENGLISH`；页码行 `Page N of 8`；gloss 前缀 `NOTE · `；P8 分隔符保持意大利语 `— PAGINA n —`。
- P1 副标题：分版 44pt（`THE ITALIAN WEEKLY · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A`），W43 同配对为 46pt（`THE ITALIAN WEEKLY · VOL.1 · L'ORA SOLARE · IL MALTEMPO · IL CINEMA`）。44pt 实测 advance 边缘 73.1..1876.9，内框（40..1910）与内容右缘（1885）内，全文保留；46pt 同串实测右缘 1917.9，确会越内框线——降字号有据、可读性无损（见 O3 左缘数值差异）。
- FRASE 框标题：分版与 W43 均为 19pt（`LA FRASE PER RICORDARE · Remember`，分版 P2 y=1200.75，W43 P2 y=800.08，位置随版面不同），W43 先例属实；23pt 原串 450.7px、19pt 后 372.2px（构建员值与框内实测一致）。
- `Match the pairs`：分版 P2 D、P4 B、P8 F 三处，与 W43 三处逐字同；“Match words to definitions”已不存在。
- P8 E 重定向遵循 W43 裁定之类别（意→英翻译改向 + #140 意大利语键保留），但有一处表述不精确（见 O4）。
- P8 key-note 修剪与 P1 settimana/parola 缩短：逐项核实见观察 O5（措辞收紧，无键/题干/意大利语正文丢失；注释层有 3 处可指出的弱化，均非阻塞）。

### 8. 图片 — 通过
- 每页 `<image>` 载荷 sha（href 前 16 位）与几何（x/y/w/h）分版 = 核心，全 8 页逐项相等；P3 与 P5 各 1 图（其余页为线描/图表，无照片载荷）。
- 署名在版且与核心同：P3 `Foto: Wikimedia Commons — dominio pubblico`；P5 `Foto: Wikimedia Commons — CC0`。卡片目视两图完整、署名清晰。

### 9. ABSTRACT — 通过
- 英语单行（375 字节，无换行符；无尾换行不影响单行性），ASCII 双引号 0 个。
- 含刊名 La Lucerna、目标语 Italian、读者语 English、真实主题关键词（first cold snap、All Souls Day on 2 November、Panettone World Cup final in Milan on 7-8 November、Torrone festival in Cremona、Serie A matchday 11）、题数 150 exercises、分级 A2 to B2、学习者搜索短语 `Learn Italian by reading real Italian…`。

### 10. 卡片目视与题量 — 通过
- 8 张卡片逐页目视：无溢出、无重叠、无压框、无压页脚、无截断；P1 徽章/副标题/规则、P2 配对右行、P3 照片+署名、P4 赛程表、P5 照片+署名、P6 图表+说明、P7 栏列+FRASI、P8 答案区+页脚间距均干净。
- 题量独立展开计数（渲染 SVG：独立 `N.` 节点 + `N–M.` 区间展开 + 每题前 42px 处 fs19 级别徽章配对）：**150 题，连续 1–150**，页分布 **10/18/18/18/18/18/12/38**，级别 **A2 47 / B1 70 / B2 33**，分版 = 核心（区间题：P2 25–28、P4 52–55、P8 141–144；无未配级别题）。
- 范文：81 词，与核心逐字一致（`Testo modello:` 后正文比对 identical）。
- 双 PDF 均为 8 页；print PDF 文本层“桥接”0 次。

## 非阻塞观察（与构建员自述不符处均列出）

- **O1 — P8 key flow 终值口径不符（非阻塞）。**构建员称“终 y=2484（bottom 2552）”。实测：2484 ≈ col4 末行基线 2468.84 + 15.2（仅 col4）；全局最晚基线为 col1 #37 的 2536.40，墨迹底约 2540（≈其称的 bottom 2552 的另一种算法）。实质结论不变：距页脚线约 40px，FOOTER 0 旗，无溢出。但“2484”作为全局终值不准确，KIT 表述应修正为按列终值。
- **O2 — P7 col3 终值小数差异（非阻塞）。**构建员称 1673.0/余量 13px；本校对 PIL 墨迹底 1673.95/余量约 12px。差异来自墨迹度量取整，不影响“加一行即越线”的结论（行距 28.4px ≫ 12px）。
- **O3 — 46pt 副标题左缘数值差异（非阻塞）。**构建员称 46pt 边缘 57.1..1917.9；本校对同串同字体实测 32.1..1917.9。右缘一致（均越 1910 内框线），左缘差异疑与其 round 3 时期 anchor 解析 bug 有关；44pt 降字号的必要性与充分性不受影响（实测 73.1..1876.9）。
- **O4 — “与 W43 裁定同题号”表述不精确（非阻塞）。**W43 分版 P8 #139 键为意大利语（`Sabato alle 18:00 si gioca Napoli–Roma.`），#140 键亦为意大利语；W43 的英改向为 #137/#138。W45 #139 改向为英语在其自身语境下合法（核心 #139 为翻译题、核心键为中文句，与 #137/#138 同类），但不宜表述为“与 W43 同题号裁定”——W43 #139 恰为保留意大利语的一例。
- **O5 — 措辞收紧中的 3 处注释层弱化（非阻塞；键、题干、意大利语正文均无丢失）。**
  - P8 #44/#134 注释：核心 `主语 + essere + 地点 + 日期` → 分版 `Subject + essere + place`，**“+ date”未出现在注释中**（日期要素仍在键句 `La finale è a Milano il 7 novembre.` 中可见，故学习者仍能看到，但注释陈述的句式严格变窄）。
  - P8 #41 注释：核心 `assaggiare 用 avere：abbiamo assaggiato` → 分版 `assaggiare takes avere`，例句 `abbiamo assaggiato` 未在注释中重复（但它本身就是印刷键，信息未失）。
  - P8 #58 注释：核心 `più + bella 周日晚最美（主观评价）` → 分版 `più + bella: Sunday evening is the finest`，“主观评价”限定词未译出（`finest` 本身已含主观最高级意味，弱化轻微）。
  - P1 settimana 副标题：核心 `本周日程 · Cosa succede, giorno per giorno` → 分版 `This week · Cosa succede, giorno per giorno`，“日程/diary”一词未译出（框内逐日内容未变）。
  - P1 parola gloss：分版 `‘Il primo freddo’: cold after a mild autumn.`，较意大利语体 `il primo freddo serio dopo un autunno mite` 少了 `serio/serious` 一词（`first` 由引用的意大利语短语本身承载；意大利语体逐字未动）。
  - 其余修剪（#3、#56、#138 注释，#139 键）经逐项比对与核心同义，无弱化。
- **O6 — P1/P5 括号式英语小注无空格（家族体例，非缺陷）。**如 P1 cifre 行 `leggera(altitude of the first light snow)`、P5 piano 行 `a Milano(Tuesday: …)`，括号紧贴前词；核心中文小注同为紧贴体例（全角括号），故为家族体例而非新增缺陷。
- **O7 — ABSTRACT 无尾换行（非阻塞）。**文件 375 字节、0 个换行符，仍为单行；insert 流程若要求尾换行请 builder 补一个，不影响本校对结论。

## 证据文件（同目录）

- `REPORT.md`（本报告）、`scan.py`（自写独立扫描）、`independent-scan.json`（右缘/同基线/图表/框线/gloss/图片/家具原始输出）
- `freeze-diff.json`、`p8-compare.txt`、`p8-nodes.txt`、`text-dumps.txt`（P7 全量节点）
- `occlusion-ed.json`、`occlusion-core.json`、`occlusion-new.json`（canonical 审计输出，均为 0 旗）
- `hashes-pre.txt`、`hashes-post.txt`（校对前后一致）
- 构建树内构建员留档（仅作比对引用，未采信其扫描输出）：`baseline-round*.txt`、`occlusion4.json`、`occlusion-new4.json`、`reg-core/reg-core.json`、`reg-en/reg-en.json`

## 最终结论

**NOT PASS。**除阻塞项 B1（P7 读者园地意大利语侧无延期披露句）外，冻结、P7 词框、P8、CJK、几何、gloss、家具、图片、ABSTRACT、题量、范文、卡片目视共 10 项门禁全部独立复测通过。修复 B1 后须整期重渲染并从头再做一轮全量校对，方可复议定稿。
