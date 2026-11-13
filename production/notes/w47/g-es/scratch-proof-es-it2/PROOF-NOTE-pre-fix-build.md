# PROOF-NOTE — W47 es-it 独立复校 (proof2，重建版)

- **版**：2026-W47 es-it（西班牙语正文 + 意大利语讲解）
- **复校员**：独立复校员（与构建者/fan-out agent 不同人），SOP §8.4 全量复校
- **对象（已核 SHA，盘上实测，复核前后各测一次、未变）**：`production/2026-w47/2026-w47-es-it/`（未 commit，未 push）
  - 印刷 `La-Lucerna-VOL4-es-it.pdf` 3,498,553 B，SHA-256 `12e7e0817b13bdd21576b820bd567b821fb69c679508189b1ef9ba973b442724`
  - 网页 `La-Lucerna-VOL4-es-it-web.pdf` 882,077 B，SHA-256 `17d4b8efd2b997ce84f260f8dd1def296c145a3ade005a4885d41a4fc35cf4d8`
  - `2026-w47-es-it.text.md` 45,176 B / 1,806 行，SHA-256 `434e8df8f0d64924b89efe561adcc9406e7b1442e801eee66c16ceeca7f06abe`
- **核心基线**：core-es fix build 10（已定稿，复核前后 SHA 未变）
  - 印 `La-Lucerna-VOL4.pdf` 17,212,955 B，SHA-256 `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`
  - 网 `La-Lucerna-VOL4-web.pdf` 1,410,471 B，SHA-256 `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`
  - `2026-w47-es-zh-cn.text.md` 1,822 行，SHA-256 `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`
- **本轮与 proof1 的关系**：proof1（旧 build，SHA `d4eaaf2f…`）的 4 项缺陷在本重建中的状态——C1 已修（实测见下）、C2 已修（实测见下）、C3 已裁定接受原样、E1 按 proof1 建议改为直撇号——但本轮必查项标准为一律弯撇号 U+2019、直撇号 U+0027 须为 0，故 E1 以新标准重判为缺陷（见 E1）。
- **复校范围**：text.md 全文 1,806 行通读；150 题逐题三源交叉（版 P8 keys / text.md 答案区 / 核心 P8 keys）+ 逐题对题干核对；8 页印版逐页渲染目视 + 网页版 P8 渲染目视；全部机械门独立重跑；撇号/引号/禁词/CJK/D5/日期/外部事实抽查（事实部分沿用 proof1 已核实的逐项结论，本重建新增内容——RTVE debate-a-ocho 时间轴行、德比信行——逐项复核，见下）。

## 结论：(b) 缺陷清单 — 共 1 项（排版规范类）

除 E1 外，本轮未发现影响理解、答案正确性或版面完整性的缺陷；全部机械门绿（见门禁表）。按 repo AGENTS.md（定稿须一轮零发现复校），本版在 E1 修复并重渲、从头再校一轮之前不能定稿。

---

### E1（本版讲解层，排版规范·轻微）— 意大利语省音撇号 28 处全部为直撇号 U+0027，弯撇号 U+2019 为 0

- **标准（本轮必查项）**：text.md 与 SVG 内意大利语省音撇号（l'、d'、un' 等）一律为 U+2019 弯撇号，直撇号 U+0027 须为 0（代码/专名原名除外，逐处说明）。直撇号残留即为缺陷。
- **独立实测**（`apostrophe.txt`，逐字符计数 + 逐处上下文）：
  - text.md：直撇号 U+0027 **×28**，弯撇号 U+2019 **×0**，U+2018 ×0，弯双引号 U+201C/U+201D ×0，直双引号 ×0。
  - SVG 8 页合计：直撇号 **×28**（P1 ×1、P2 ×1、P3 ×2、P4 ×1、P5 ×2、P6 ×0、P7 ×4、P8 ×17），弯撇号 **×0**。
  - 印/网 PDF 文字层（pdftotext）：直撇号 **×28**，弯撇号 **×0**——与 SVG 一致，交付物本身即带此缺陷。
- **28 处逐处清单**（全部为意大利语省音，无一处属于代码或专名原名；`L'UNESCO` 为意语冠词 l' + 专名 UNESCO 的省音，仍属省音）：

  | # | 位置 | 字符串 | 源码位置 |
  |---|---|---|---|
  | 1 | P1 刊头 | `TESTI IN SPAGNOLO　SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI` | `content12.py:21` |
  | 2 | P2 C 组桥接句 | `Leggi l'articolo e scegli la risposta giusta.` | `content12.py:275` |
  | 3 | P3 注 | `el duende = l'anima del flamenco.` | `content34.py:22` |
  | 4 | P3 C 组桥接句 | `Leggi l'articolo di pagina 3: vero o falso?` | `content34.py:61` |
  | 5 | P8 答案 39 注 | `L'UNESCO lo annunciò a Nairobi nel 2010` | `content34.py:87` |
  | 6 | P8 答案 42 注 | `Dopo il flamenco: l'elezione del 29 novembre` | `content34.py:93` |
  | 7 | P4 C 组桥接句 | `Leggi l'articolo di pagina 4 e scegli la risposta giusta.` | `content34.py:168` |
  | 8 | P5 注 | `la urna = l'urna.` | `content56.py:29` |
  | 9 | P5 C 组桥接句 | `Leggi l'articolo di pagina 5 e scegli la risposta giusta.` | `content56.py:66` |
  | 10 | P8 答案 73 注 | `documento de identidad = documento d'identità` | `content56.py:86` |
  | 11 | P8 答案 82 注 | `Quest'anno si può votare con MiDNI` | `content56.py:107` |
  | 12 | P8 答案 92 注 | `Sondaggio: foto con margine d'errore, un giorno preciso` | `content56.py:218` |
  | 13 | P8 答案 100 注 | `margen de error = margine d'errore` | `content56.py:237` |
  | 14 | P7 A2 桥接句 | `L'ora: es la una (singolare), son las dos (plurale)…` | `content7.py:20` |
  | 15 | P8 答案 101 注 | `Per l'una si usa il singolare Es` | `content7.py:21` |
  | 16 | P8 答案 104 注 | `L'una si dice Es la una` | `content7.py:27` |
  | 17 | P7 B2 桥接句 | `…creo que con l'indicativo.` | `content7.py:52` |
  | 18 | P7 ERRORES 栏 | `L'una è singolare: si usa es.` | `content7.py:69` |
  | 19 | P7 FRASES 栏 | `Un sondaggio è una foto con margine d'errore, scattata un giorno preciso.` | `content7.py:124` |
  | 20 | P8 题 126 注 | `MiDNI è l'app ufficiale di identificazione` | `content8.py:44` |
  | 21 | P8 答案 136 注 | `Parola interrogativa all'inizio` | `content8.py:67` |
  | 22 | P8 答案 137 注 | `Cfr. l'originale.` | `content8.py:70` |
  | 23 | P8 答案 138 注 | `Cfr. l'originale.` | `content8.py:72` |
  | 24 | P8 答案 143 注 | `margen de error = margine d'errore` | `content8.py:86` |
  | 25 | P8 答案 146 注 | `documento de identidad = carta d'identità` | `content8.py:91` |
  | 26 | P8 答案 147 注 | `Dov'è l'urna?`（含 `Dov'è` + `l'urna` **2 处**） | `content8.py:93` |
  | 27 | P8 H 组桥接句 | `Prova di scrittura (senza un'unica risposta giusta)…` | `content8.py:100` |
  - （上表 27 行共 28 处：第 26 行一行含 2 处。）
- **与 builder 记录的出入**：KIT §9 称 E1 修复后 "text.md shows 4× straight, 0× curly"——**实测为 28×，记录失实**。4 仅为 `Leggi l'articolo` 桥接句数（P2/P3/P4/P5 各 1）；其余 24 处（注文、答案注、刊头、P7 栏）未被计入。E1 的“修复”实为把 proof1 发现的唯一 1 处弯撇号改直，与全版其余 27 处直撇号统一——方向与本轮标准相反。
- **严重度**：轻微（排版规范类）。字形在正常阅读距离几乎不可辨（目视 8 页未见任何可辨的视觉破损）；不影响内容、答案正确性、版面几何与任何机械门。但按本轮必查项，直撇号残留即缺陷，故结论 (b)。
- **建议修复**：上述 27 行源码字符串内的 28 个 U+0027 一律改为 U+2019（text.md 与 SVG/PDF 随重建与重渲同步更新；KIT §9 的 "4×" 计数一并更正为实测值），重渲后按 SOP §8.4 从头再校一轮。

---

## 已核实无误的要点（本轮独立实测）

### proof1 缺陷的修复验证
- **C1 已修**：P1 CINCO CLAVES 盒高 700→720，盒底现为 y=1308.0；盒内末行 `Cinque chiavi, zero numeri inventati.` 基线 1300.0、真墨底 1304.2，**真墨 clearance +3.8px（在内为正）**；P1 渲染目视确认该行已在盒内。粗扫查的 −44.0 为下一盒（EN ESTA EDICIÓN，y=1312）的标题落入 +45px 窗口，假阳性（creambox_diag 已裁定，owner-rect=y=1312）。
- **C2 已修**：text.md 内 `hasta el jueves` ×7、`antes del jueves` ×0；P1 正文、P1 题 3、P2 题 12、P8 题 116、P1 图注 5 处原 `antes` 措辞已全部统一为 `hasta`；答案键（19）不变。另 `sábado veo el derbi` ×1（P7 Marta 信）。
- **C3 已裁定接受**：P5 B 组词框 `sobre · papeleta · censo · identidad · plazo · urna`，答案 70 `correo`、72 `envío` 不在框内，`sobre`、`urna` 无题使用——与裁定一致，不重议。6 答案全部正确无歧义。
- **E1（proof1 版）**：proof1 称 P2 C 组引言 1 处弯撇号为孤例、建议改直；builder 已改直。按本轮新标准重判，见本轮 E1。

### 150 题逐题核对（三源交叉 + 对题干手验）
- **P8 extract 150/150**（`p8-extract.json`）；**keycheck REG vs 抽取 149/150**，唯一 mismatch 为 #150 开放写作题（抽取为 `✓`，已知例外）；**p8 compare vs 核心 CLEAN**，keydiff=[137,138]（已裁决项，见下）；**text.md 答案区 vs P8-extract 逐键比对 150/150**（`triple-check3.log`：答案区含 `N. <key>` 全部 150 项，与抽取值逐字相符）。
- **MCQ 有效性**：选择题 60 项（Scelta multipla 47 + Cloze 13），键全部 ∈ {A,B,C}；配对题 12 项，键全部 ∈ {a,b,c,d}；正误题 8 项，键全部 ∈ {Verdadero,Falso}。题型分布：Completare frasi 48、Scelta multipla 47、Abbinare parole 12、Vero o falso 8、Formare frasi 7、Trasformare frasi 10、Cloze 13、Traduci 4、Scrivi 1；级别 A2 50 / B1 72 / B2 28；按页 10/18/18/18/18/18/12/38。
- **逐题对题干核对**：1–150 全部与题干/原文/图表一致。含：配对 25–28（debate=c、mitin=b、cartel=d、escaño=a）、52–55（jornada=c、derbi=b、liderato=a、fase liga=d）、97–100（sondeo/muestra/indecisos/margen de error）、141–144（sondeo=c、muestra=d、margen de error=b、junta electoral=a）；图表题 83–88（RTVE 45/45/30/30/15、总和 195、禁发 5 天）；虚拟式 93/94/95/96/109/110/112；过去时 60–64（ganó/recibió/perdió/volvió/cerró）；ir a + 不定式 76–79；Q79 键为 `comparar`（非 `comprar`，SVG 原文 + 抽取双重确认）；范文 97 词（80–100 词范围内）。
- **keydiff [137, 138]（已裁决，非缺陷）**：翻译题 137/138 题干为西班牙语句、答案须为意大利语句。本版键 `137. Lunedì è la Giornata internazionale del flamenco.` / `138. Sabato guardiamo il derby di Siviglia.`，与题干 `El lunes es el Día del Flamenco.` / `El sábado vemos el derbi Sevilla–Betis.` 逐句对应正确；三源一致（版 P8 keys / text.md 答案区 / 核心 P8 keys 的中文译句对照）。139/140 题干为意大利语句、键为西班牙语句，两版一致（`El voto por correo se pide hasta el jueves 19.` / `Cada promesa tiene que llevar datos.`）。
- **P8-keys 终 y=2521**（底 2560），0 OVERFLOW；rerun 0 FLOW OVERFLOW / 0 HEAD TOO WIDE；P8 渲染目视：末键 `150. ✓ Vedi il modello, sezione H (97 parole)` 距页脚线有充分余量。
- **P7 金句 8/8**：8 句均逐字出自本期正文，意大利语 gloss 准确，页码标注（P1/P2/P3/P4/P5/P6）全部与出处页相符；P1 词条、P7 词条、读者来信示例（Marta，明确标注为编辑部所写示例）及“承诺顺延至 VOL.5”的编辑注均与核心一致，无编造来信。
- **重建新增内容复核**：P6 时间轴新增 RTVE debate-a-ocho 行（`23 NOV. — RTVE propone un debate a ocho, con los portavoces de los ocho grupos.`）与 P6 正文同句一致；P7 Marta 信 `el sábado veo el derbi`（德比为周六 21 日 18:30，正确）；其余核心 build 10 改动（C1/C2）见上。无新增事实错误。

### 冻结与 CJK
- **freeze baseline（源码重建）8/8**：重建 SVG 与 shipped SVG 逐字节一致；shipped SVG 未被改动（`freeze-baseline.log`）。
- **freeze diff（字符串冻结）**：新增 CJK 码点共 **6 个，全部为 U+3000**（全角空格，SOP §1.1 规定的分隔符；P1–P6 各 1，P7/P8 各 0）；新增串含非 U+3000 的 CJK **0**；西语词丢失检查 `removed-es-words-missing-from-added: NONE`（被删串全部为中文讲解层或西语断行碎片，其词均在新增串中出现）。
- **SVG 内 CJK 全量分类**：`<text>` 内 CJK 字符共 124 个，**全部为 U+3000**（P1 21 / P2 17 / P3 14 / P4 16 / P5 15 / P6 15 / P7 12 / P8 14）；`<text>` 外唯一 CJK 为 P1 moth `<title>三色蛾</title>`（非渲染，与核心一致，KIT §6.12 已记录）。
- **练习小节头冻结为源语言**：P8 A–H 小节头全部为西语（A COMPLETA LA CRÓNICA、B PREGUNTAS GENERALES、C LEE Y RESPONDE、D CONSTRUYE FRASES、E TRADUCE、F LAS PALABRAS DEL 29N、G DIÁLOGO EN EL COLEGIO、H ESCRIBE TÚ）；`ESERCIZI` ×6 均为家具双语标签（`EJERCICIOS　ESERCIZI　PAGINA n`、`EJERCICIOS Y RESPUESTAS　ESERCIZI E RISPOSTE），非小节头。
- **"next Sunday" 核查**：es-it 全版（.py/.svg/.md）含 "next Sunday" **0 处**，无英文讲解层泄漏。另：任务书所引行号（content12.py:37/:113、content34.py:127）按盘上实测属 **core-zh-tw**（该核心的英文 gloss：味全龙封王游行与小雪），不在 core-es 内；core-es 内 "Sunday" 0 处。无论如何，本版无此问题，不列为缺陷。
- **双语小文件标题越奶油盒右缘**：boxtitle 真墨实测 25 盒全部正余量（最紧 P7 `ERRORES TÍPICOS　ERRORI TIPICI` +14.4px；其余 ≥+20.1px），0 溢出；occlusion BOXTITLE 类 0 flags。无此问题。

### 几何与版面（真墨实测）
- **creambox 全版扫查（canonical `hidden_files/w47/tools/creambox.py`）**：粗扫查 6 处负余量，creambox_diag 真墨复核逐项裁定——**全部为假阳性**（下一栏目标题/图注落入 +45px 窗口），自有末行墨 clearance 全部 ≥0（`creambox-diag.log`）。最紧两处均为 **+0.1px**：P2 `¿SABÍAS QUE…?` 盒（末行 `ley.`，墨底 543.4 vs 盒底 543.5）与 P5 `VOTAR POR PRIMERA VEZ` 盒（末行 `compara precios antes de pagar.`，墨底 1251.4 vs 盒底 1251.5）——**与 core-es 同盒同坐标同数值逐字一致，属继承的核心几何**，墨未出盒，非缺陷；目视 P2/P5 确认两行均在盒内。其余：P3/P5 `¿Y TÚ?` +1.7、P4 `¿Y TÚ?` +1.3、P7 CARTAS 栏 +1.5、P7 其余 +38.0/+22.0。
- **boxtitle 宽度**：见上，0 溢出。
- **chips（`rx="2.7"` level 芯片）**：共 **141**（P1 10、P2 15、P3 18、P4 15、P5 18、P6 18、P7 12、P8 35），PIL 真宽复测**全部 fits，0 溢出**；级别分布与 KIT 一致（P8 A2 11 / B1 21 / B2 3）。
- **sweep**：box-vs-hline 0、bridge orphans 0/20、bridge widows 0。
- **P8 最小字号**：10.125pt（n=375），0 处 < 9.75pt 下限。
- **8 页逐页渲染目视**（`view/p1–p8.png`，印版 96dpi）：无溢出、无重叠、无压页脚、无缺字、无豆腐块；Sargent 舞者图、青铜投票箱图、Book of Hours 图、鹅毛笔图均正常渲染；P4 六场赛程表、P6 RTVE 柱状图（45/45/30/30/15）与 5/15/1 迷你柱均正确。网页版 P8 渲染与印版一致。
- **印/网一致**：pdftotext 均为 108,723 字节且逐字节一致；像素比对（96dpi）印 vs 网 mean|d| 0.000–0.290；印 vs SVG 直接渲染 mean|d| 3.98–8.91，大差异像素遍布全页文字边缘（光栅化器抗锯齿差异，P8 文字最密故最高），无局部内容差异。

### 文字层与引号/禁词/日期
- **弯引号**：«/» 全版各 56 处（text.md 56/56；SVG 逐页 2/10/2/0/1/3/31/7 = 56），全部成对；U+201C/U+201D/直双引号 ×0。
- **禁词**：text.md 中 CJK 0 字符（除 U+3000 外见上）；`SOP`/`proofread`/`cover`/`12 de noviembre` 0；VOL.4 印刷层 9 次 + 刊头 `VOL. 4` 1 次（合计 10）；VOL.5 ×3 均为合法的下期预告（P7）。
- **日期星期**（Europe/Madrid）：11 月 9 日周一、10 日周二、13 日周五、16 日周一、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、24 日周二、25 日周三、26 日周四、27 日周五、28 日周六、29 日周日，全部吻合；16 日→29 日为 13 天，与头条“trece días”一致。
- **ABSTRACT.txt**：意大利语单行 471 B，无 ASCII 双引号，含刊名、目标语名、A2–B2、150 esercizi 与本期真实主题词（laSexta 辩论 13 日、大选 29 日、邮寄投票 19 日截止、弗拉门戈日 16 日、圣塞西莉亚 22 日、13 轮、欧冠），事实无误。
- **KIT §9 新 SHA** 与盘上实测完全一致（印/网/text.md）；§8 旧 build 数字（3,498,408 B 等）为重建前记录，已由 §9 取代。唯 §9 的 E1 计数 "4×" 失实（见 E1）。

### D5 字体（只记录，不判 (b)）
- 拉丁讲解层落在 Noto Sans CJK SC：全版 `<text>` 元素字体分布 Newsreader 973、Noto Sans CJK SC 632、Noto Serif CJK SC 43、UnifrakturMaguntia 1。
- **实测段数**：Noto Sans CJK SC 中纯拉丁字母元素 **491 段**（P1 62 / P2 62 / P3 63 / P4 61 / P5 62 / P6 51 / P7 60 / P8 70）；core-es 同口径为 259 段，净增 +232 段（即原中文讲解层转为意大利语后仍落 CJK 字体者）。另：含 U+3000 的 sans 元素 120 段，仅标点/数字的 sans 元素 21 段（632 = 491 + 120 + 21）。按任务书，此为全周级已知待定项，**只记录、不以此判 (b)**。

### 外部事实（proof1 已逐项核实，本轮复核重建新增点）
- proof1 已核实：大选日历（Real Decreto 806/2026，29 日周日 9:00–20:00，竞选 13–27 日，28 日静默日）、邮寄投票（申请截至 19 日周四含当天、文件自 9 日起寄出）、辩论（laSexta 13 日 21:30 已确定；SER 住房辩论 18 日；Atresmedia 23 日；RTVE 八方辩论 23 日提议；PP 26 日提议无 pactada 日期；cara a cara 16 日未确认，均与本版“提议≠确定”的措辞一致）、西甲第 13 轮六场时间、欧冠第 5 轮、弗拉门戈（2010 年 11 月 16 日 UNESCO 列入）、圣塞西莉亚 22 日、MiDNI 11 月 5 日解除停用、毕尔巴鄂市立乐队 22 日 12:00 Euskalduna、Black Friday 27 日、民调禁发 24–28 日、RTVE 195 分钟算术自洽。本轮通读 text.md 全文未发现与上述事实矛盾的新表述；重建新增的 RTVE 时间轴行与正文同句一致。
- 未独立锁定的两项（沿用 proof1，不列为缺陷）：RTVE 195 分钟逐项第二来源；Sargent 图年份 1880–81 到年精度。

## 机械门结果（详见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| SHA 核对（任务书 + KIT §9 + 盘上实测，复核前后各一次） | 3 件全符；复核后 core-es 3 件亦未变 |
| 页数 | 印/网各 8 页，1462.5 × 2025 pt |
| run（源码重建，副本内 run.py） | rc=0，TOTAL 150，0 FLOW OVERFLOW / 0 HEAD TOO WIDE；重建 SVG 与 shipped 8/8 逐字节一致 |
| occlusion 审计 | 0 flags（自检六类全触发） |
| p8 extract | 150/150 |
| p8 compare（vs core） | CLEAN，missing=[] extra=0，keydiff=[137, 138]（已裁决） |
| source freeze（freeze.py baseline） | 8/8 SVG 逐字节一致，shipped SVG 未被改动 |
| string freeze（freeze.py diff） | 新增 CJK 仅 6 个 U+3000；西语零丢失 |
| text layer 印/网 | 108,723 B，逐字节一致 |
| p8 font（minfont） | 10.125 pt ≥ 9.75 pt 下限 |
| scans（creambox 全扫 + refined + 真墨 diag） | 自有墨 clearance 全部 ≥0，6 处粗负值皆假阳性 |
| chips（rx=2.7） | 141 个，全部 fits，0 溢出 |
| keycheck（REG vs 抽取） | 149/150，唯一 #150 开放题 `✓` 例外 |
| mcq（60 选择题 + 12 配对 + 8 正误） | 键全部在合法选项集内 |
| widths（boxtitle） | 25 盒全部正余量，最紧 +14.4px |
| band spans（sweep bridge） | orphans 0/20，widows 0，box-vs-hline 0 |
| P8-keys | 终 y=2521（底 2560），0 OVERFLOW |
| 撇号实测 | 直 ×28 / 弯 ×0（text.md、SVG、印/网文字层三处一致）— **E1 缺陷** |

## 复校员说明

- 本版除 E1（28 处直撇号）外全部通过。是否定稿由协调员裁定：E1 修复（28 处 U+0027→U+2019）+ 重渲后，按 SOP §8.4 与 repo AGENTS.md，须从头再做一轮全量校对且零发现方可定稿。
- 本复校未改任何生产文件、未重建生产文件、未 commit、未 push、未动 tools/。复核前后生产文件全量哈希逐字节一致（`before-hashes.txt` vs `after-hashes.txt`，es-it 与 core-es 各 35 文件）。全部工作文件在 `hidden_files/w47/scratch-proof-es-it2/`。
- 方法说明：`render.py` 未在原地重跑（它会重写 shipped PDF；等效验证改用 freeze baseline 副本重建 + SVG 直接渲染与印版 PDF 的像素比对）；`freeze_direct.py` 为 de 族工具（硬编码 core-de），es 族不适用，source/string freeze 由 `tools/freeze.py` baseline + diff 覆盖；`creambox.py` 用 canonical `hidden_files/w47/tools/creambox.py`，未复制。
- 环境说明：`/dev/null` 在复核期间多次缺失/变为空白普通文件（`mknod` 在本容器无权限，`Operation not permitted`；按任务书以 `touch /dev/null` 垫回后探针通过，`git hash-object` 全程正常）。每次写盘前均重探针，未遇配额问题。
