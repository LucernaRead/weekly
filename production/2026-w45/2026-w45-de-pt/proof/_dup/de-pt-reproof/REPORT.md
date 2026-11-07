# 独立复校报告 — Lucerna Weekly W45 DE×PT（修复后从头全量复校，SOP §8.4）

**结论：ZERO PROBLEMS（可定稿）。** 原校对 2 项阻塞问题均已修复并经独立重测证实；以下 12 门全部通过，无编号问题。
本报告不宣称上架（上架由协调员串行执行）。

- 校对对象：`files/weekly-report-w45-de-pt/`（修复后版：印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt、svg×8、cards×8）
- 对照核心：`files/weekly-report-w45-de-core/`（VOL.2）
- 原校对报告：`hidden_files/w45/de-pt-proof/REPORT.md`（2 项阻塞：P7 NOCH EIN WORT 德语定义句本地化；P8 item 5 注文英文残留）
- 参照：`files/weekly-report-de-pt/`（W43 已发同配对版）、`tools/README.md` #7–#22、SOP
- 校对方式：全部关键断言均从渲染产物/SVG 坐标独立重测；修复员自述（fix-record.md、KIT）一律未采信，仅作比对靶子。
- 本报告证据目录：`hidden_files/w45/de-pt-reproof/scratch/`（freeze-diff-reproof.json、occlusion-reproof.json、baseline-de-core/、regcheck.json、removed-p1-p6-p8.txt）
- 未做事项：未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录、未改任何源码、未派生下级代理。登记转储仅在 scratch 拷贝（OUT 已重定向至 scratch，见门 12）中运行，事后实测在盘哈希全部未变。

## Stand-down 检查

- 开工前 `files/weekly-report-w45-de-pt/` 与 `hidden_files/weekly-report-w45-de-pt-build/` 无 de-pt 渲染进程（当时在跑的唯一渲染进程属另一分版 nl-de，未触碰）；
  100 秒后复查零新写盘（最新 mtime 仍为 21:18 的 KIT，SVG 21:17、PDF 21:15），属已完成交付的新鲜时间戳，正常开工。

## 各必查门实测值

### 门 1 修复验证 1：P7 NOCH EIN WORT —— 通过

- P7 SVG 实测三行（x=1473，20.5pt，基线 y=1432.5 / 1461.61 / 1490.72，与修复员称逐值一致）：
  - `«der Tankrabatt» (Seite 2): die`
  - `gesenkte Steuer auf Benzin und Diesel.`
  - `Desconto no combustível.`
- 德语句逐字恢复、页标恢复为 `Seite`、葡语 gloss 保留 ✓。
- 框几何（独立实测，tools venv PIL + `occlusion_audit.ink_box`）：
  - 行 2 墨右 1861.25；框 rect x=1451 宽 434 → 框右沿 1885， clearance **23.75px ≈ 23.8px** ✓；
  - gloss 墨底 1490.97；金句横线 y=1508（全宽规则线 x 65→1885）， clearance **17.03px ≈ 17.0px** ✓；
  - P7 col3 flow 终值 1504.5（我独立 scratch 重渲染实测，见门 12）< 1508，未越线 ✓（墨迹口径与 flow-cursor 口径均未越线）。

### 门 2 修复验证 2：P8 item 5 注文 + 全页英文残留 —— 通过

- P8 SVG 文本 186–187 行实测：`5. neun(9 jogos na 9ª rodada)`（键 `neun` 不变；题干 P1 `Der 9. Spieltag hat ___ Spiele.` 不变）✓。
- 与 P1 Zahlen 框同表述逐字核对：P1 文本 55 `Bundesliga (9 jogos na 9ª rodada)`，括号内表述完全一致 ✓。
- 全 8 页英文残留独立重扫（我自拟的扩展词表，不复用修复员词表：matches on matchday、matchday、care home、This week's big questions、Germany's five hot questions、goes to the end、leftover、This week、the match、matches、football week、home/away game、discount on fuel、fuel discount、tax cut、school started、autumn holiday、nursing care、this week's、Germany's、questions of the week、big/hot questions、on matchday、in the morning、at home、for all、weekend league、energy tax、goes to、the end of）：**0 命中** ✓。
- 合法保留：`Quiz-relâmpago`（葡语借词，1×）；德语专名 Real Betis、Manchester City、Crystal Palace、Champions/Europa League、NFL、Allianz Arena 等属冻结正文/专名，不计。
- 结构扫描：CJK 0、全角括号 0、全角 ｜ 0、`。` 0、`……` 0、`桥接` 0、`Le/The Lucerna` 0、`VOL.1` 0。

### 门 3 改动范围验证 —— 通过

- 修复前基线（fix-baseline-hashes.txt）vs 修复后（fix-after-hashes.txt）逐项 diff（我独立重跑 diff）：
  - **变化且仅变化**：svg/p7-sprache.svg、svg/p8-uebungen.svg、cards/p7-sprache.png、cards/p8-uebungen.png、双 PDF；
  - **逐字节不变**：svg p1–p6、cards p1–p6。无无关改动 ✓。
- 新 p7/p8 SVG 哈希与修复员称一致：
  - p7 `171e37ce40f4a697068cbfad4129037c31cb2abd4c196fc39f174d3c56f18089` ✓；
  - p8 `e79f51f4de864d8f496a78f3f4f4ac86bc81338b8b966abb1ae0a8e8904bfc37` ✓。
- 在盘现哈希与 fix-after 全 18 项逐一一致（复校开始与结束两次实测均同）。

### 门 4 Freeze 全量 —— 通过

- 我独立跑 `tools/freeze.py baseline`（核心 build 拷贝至 scratch 重渲染）：**8/8 字节复现**；
  核心 SVG 重哈希与 KIT §2 “before” 值逐字节一致（p1 `6cbd4802…`、p2 `9362256d…`、p3 `3e8a8d16…`、p4 `b787f592…`、p5 `4dcbeb97…`、p6 `01b75ad4…`、p7 `fbaf8cdd…`、p8 `299524bd…`），核心前后哈希一致、未被触碰 ✓。
- 我独立跑 `tools/freeze.py diff`：P1 +24/−23、P2 +36/−32、P3 +40/−40、P4 +25/−22、P5 +42/−39、P6 +37/−33、**P7 +60/−53**（修复前 +61/−54，恰为两项修复的净效应）、**P8 +160/−141**（修复前 +161/−141，恰为 item 5 注文一处）；**新增 CJK 全 8 页均为 0**；全文 `桥接` 0 命中 ✓。
- 删除串逐项裁定（P1–P7 added 全目视 + removed 全清单见证据 removed-p1-p6-p8.txt）：
  - P1 副标题槽位句 → 配对徽章，家具 ✓；
  - P3/P4/P6 孤 `。` → 核心自有排版类，葡语版句末为行内 `.`，无内容损失 ✓；
  - P7 `Ein Beispiel der Redaktion!` → 葡语标签 `Um exemplo da redação!`，家具 ✓；`……` → `...`，标点 ✓；
  - P7 词框行 1 仅剩括号形式差异：核心全角 `«der Tankrabatt»（Seite 2）: die` vs 本版半角 `«der Tankrabatt» (Seite 2): die`（同族 DE×EN/DE×ES/DE×IT 一致形式）✓；
  - **`gesenkte Steuer auf Benzin und Diesel.` 在 removed 与 added 两侧均不出现**（已冻结、核心与本版同一）——原问题 1 的两条定义串已不在 removed 侧 ✓；
  - P8 全角括号行片段 → 半角形式已在 added 侧对应存在，仅括号形式变化，德语 key 无丢失 ✓；
  - 其余 removed 全为中文讲解层、家具（栏头/页脚/页码行）、标点或全角括号片段，无德语正文句丢失。
- P1–P7 added 串逐条目视：均为葡语讲解、家具、双语栏头、gloss、葡译、指令 token 或 gloss 行内德语词头，无新增德语正文句。

### 门 5 P8 全量 —— 通过

- 我独立跑 `tools/p8.py compare`（显式 SVG 路径）：**CLEAN，core 150 noted = edition 150 noted，missing=[]，extra=0，keydiff=[137, 138, 139, 150]**（与修复员称一致）✓。
- Keydiff 逐项人工核实（答案区原文，非仅提取器输出）：
  - 137（A2 Tradução，题干 DE `Der Tankrabatt läuft bis Dezember.`）：key `O desconto no combustível vai até dezembro.`，注 `laufen = durar, continuar`——DE→PT 翻译题真实重定向 ✓；
  - 138（A2 Tradução，题干 `Ich schaue am Dienstag Fußball.`）：key `Vejo futebol na terça-feira.`，注 `schauen = ver` ✓；
  - 139（B1 Tradução，题干 `Die Schule hat wieder begonnen.`）：key `A escola recomeçou.`，注 `wieder begonnen = recomeçou` ✓；
  - 140 **不在** keydiff：key 德语不变 `Am Sonntag schlafe ich eine Stunde länger.`，仅题干反向重定向（PT `Durmo uma hora a mais no domingo.`，指令 `Traduza para o alemão`）✓；
  - 150（B1 Escrita）：key `Tarefa aberta — siga os pontos do quadro de escrita; o texto-modelo está no quadro desta página`，注 `Avaliação pelos pontos indicados`——写作 apparatus 葡文化 ✓；
  - item 5 注文改动未改变键（`neun` 不变），140 键德语不变 —— keydiff 仍为 [137, 138, 139, 150]，与修复前一致 ✓。
- 无括号/破折号提取伪影：keydiff 与人工逐行读数一致；P8 全页全角括号/全角 `｜`/`。`/`……` 均为 0，CJK 0。
- P8 形式：本版构建码 `content8.py` 第 156 行与 W43 本族构建码逐字一致——`kf.para(" · ".join(parts), 13, "sans", False, INK, 1.26, 9)`，即 **13pt / 1.26 半角括号** ✓。
- 观察（非问题，沿用原校对 O1）：连接符为无空格 `key(note)`，W43 为有空格 `key (note)`；无空格形式与 W45 DE×EN 构建码一致，属同族内形式变体，不影响可读与 key 判定。

### 门 6 几何遮挡全量 —— 通过

- 我独立跑 `tools/occlusion_audit.py`（自测 6 类全触发、干净对照静默）：**分版 0 flags、核心 0 flags、NEW vs core 0** ✓。
- 同基线墨迹碰撞扫描（我独立实现，调用共享工具 `occlusion_audit.ink_box`，全 8 页逐基线比对）：
  - **解码后（`&amp;` → `&`）实测：分版 0、核心 0**；
  - 未解码口径复现原校对 1 项——P1 sommaire S.3 行 y=1436：`Ferienwechsel &amp; Herbst` 墨右 1804.5 vs 标签 `A2→B1` 墨左 1799.7（重叠 4.8px），核心同页同款亦 1 项；
  - 解码后重测：标题墨右 **1755.0**，标签墨左 1799.7，**间隔 44.7px**；卡面像素 ground truth（P1 卡 y 1400–1470 带）：标题墨迹止于 x≈1757，标签墨迹起于 x≈1800，**间隔约 43px**，字形互不接触；
  - 判定：该项是 **XML 实体未解码的测量伪影，非真实碰撞**，且元素在核心与本版逐属性逐字相同，属核心继承且墨迹干净 ✓。
- 图表标签覆盖检查（P6 图表带文本 vs 其后绘制矩形逐项实测，另加全图表带扫描）：
  - 绘图顺序每行均为：德语标签 → 葡语标签 → 条形 → 百分比；条形后绘，实测后绘矩形重叠 = **0**；
  - 德语标签墨右：`pflegen Angehörige zu Hause` 390.5、`nutzen einen Pflegedienst` 354.5、`leben im Pflegeheim` 294.0（条左 535，间隔 ≥144.5px）；
  - 葡语关键词标签墨右：`em família` **522.8**（距条左 12.2px）、`serviço` **491.5**（43.5px）、`em lar` **484.0**（51.0px）；
  - 百分比起位 1707/891/755 vs 条右 1691/875/739，间隔均为 16px；条宽 1156/340/204 = 1700 的 68%/20%/12% ✓；68+20=88 与 item 85 key 一致 ✓。

### 门 7 Gloss 全量 —— 通过，25=25

- 按渲染后 `gloss()` 字符串本身以 `·` 拆分（源文件 grep，不执行构建模块）：核心 build 与本版 build 各 5 处调用（P2/P3/P4/P5/P6），每处 5 项，**核心 25 = 本版 25，1:1，无增删合并** ✓。
- 全部 24 个德语词头在合并渲染文本中均存活；`die Pflegeversicherung` 初查“缺失”实为换行断开（P6 gloss 框 `… · die` / `Pflegeversicherung = seguro de cuidados`），条目完整 ✓。
- P1 bridge 行（非 gloss 调用）：核心 4 项 = 本版 4 项 ✓；gloss 前缀 `Nota — `，5 处调用一致 ✓。

### 门 8 P7 金句全量 —— 通过

- 8 句德语原文在全版合并文本中**各恰 2×**（源文章页 + P7 表），核心亦各 2×；且每句均在其标注的源文章页出现：
  1. `Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.`（P4）
  2. `Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter.`（P2）
  3. `Wer 50 Liter tankt, spart rund 8,35 Euro.`（P2）
  4. `Die Schule hat nach den Herbstferien wieder begonnen.`（P5）
  5. `Die Tage sind kurz, die Abende lang.`（P3）
  6. `Zwei schwere Auswärtsspiele für die deutschen Teams.`（P4）
  7. `Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.`（P6）
  8. `Es geht langsam aufwärts — aber von allein geht es nicht.`（P6）
- P7 表内顺序配对逐项核对：每句后紧跟的页码标签与其源文章页一致；页码标签分布与核心逐项一致：**S4·B1×2、S2·A2×2、S5·B1×1、S3·A2×1、S6·B2×2**（=8）；德语引言与核心逐字一致 ✓。
- P7 短语逐字取自本期文章并带正确页码标签 ✓（上表即核对结果）。

### 门 9 读者园地全量 —— 通过，显性邀请独立再判定成立

- 页上同时具备三事实（葡语注文 2 行，P7 文本 110–111）：`Sem cartas reais nem melhores textos da página 8; a promessa passa ao VOL.3.`
  ——（1）无真实来信、（2）无最佳 P8 作文、（3）承诺顺延至 VOL.3 ✓。
- 显性公开征集句（独立判定：**构成显性邀请**，P7 文本 112–113）：`Escreva-nos! Envie a sua carta real e o seu texto da página 8 para o VOL.3.`
  ——祈使 `Escreva-nos!` + 明确对象（真实来信 + P8 作文）+ 明确去向（VOL.3），不是内容预告也不是练习提示。
  该判定仅凭读者园地本句即成立；同页 VOL.3 预告行（`Ihre Briefe: Schreiben Sie uns! …`）与其他页练习提示均未计入。
- 标签 `Um exemplo da redação!` 明确标示例身份 ✓；读者园地德语行与核心逐字一致（`Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3.`、示例信、德语征集句）；全版无编造的读者来信、姓名或引言 ✓。

### 门 10 家具三方对照 —— 通过

- P1 配对徽章与 W43 已发 `files/weekly-report-de-pt/svg/p1-front.svg` 的徽章元素**逐属性一致**：
  `x=975, y=372, 20pt, weight 700, fill #a4553a (BRICK), anchor middle`，字符串
  `TEXTOS EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA` 逐字一致 ✓。
  徽章字符串全版仅 P1 一处（其余页同名字符串命中均为页脚，属正常复用）✓。
- 注：README #20 泛写称 EN/DE/ES 族徽章为 19.5pt；W43 已发 DE×PT 实测为 20pt，本版与 W43 实测一致——按任务要求，**W43 实测胜过 README #20 泛写**，此处按 W43 裁定 ✓。
- 页脚 8/8：`Die Lucerna · SEMANÁRIO ALEMÃO VOL.2 · TEXTOS EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS` ✓；
  页码行 8/8 `Página {n} de 8` ✓；masthead 每页 1× `Die Lucerna` ✓；P1 顶条、46pt 副标题、gloss 前缀、
  P8 分隔符 `— Página {n} —`（8/8）、P8 keys 头 `ANTWORTEN · TODAS AS RESPOSTAS COM NOTAS (PÁGINAS 1–8)` 均与 W43 形式一致（VOL.2 替换 VOL.1 除外）✓。
- 三项精简决定独立再裁定（不照抄原校对，逐项重测）：
  - (a) P7 工具箱 3–4 项：实测 `Es wird gespielt. = Será jogado`（无 `(passiva)`）、`Meiner Meinung nach ... = opinião`（关键词 gloss）。
    裁定可接受：被动语态在同页 A2 课（`Mit werden sprechen Sie über die Zukunft und das Passiv`）已教，且练习 104 以 `„Es wird gespielt“ ist... A. Passiv` 直接考查；
    `Meiner Meinung nach ...` 全形在同页 B2 课（`Meiner Meinung nach ... Oder: Ich finde, dass ...`）已教且用于练习 112。工具箱为速查栏，语义未损 ✓。
  - (b) P6 图表关键词标签：实测 `em família / serviço / em lar`（墨右见门 6），完整形式存活情况：
    `serviço de cuidados` 存活于 P6 文章 gloss（`der Pflegedienst = serviço de cuidados`）及 P8 答案 item 84（`serviço de cuidados 20% é o segundo`）；
    `lar de idosos` 存活于 P8 答案 item 86（`lar de idosos 12% é o menor`）及 87；
    `cuidado familiar`（行 1 完整形）全版无逐字存活；但行 1 有德语标签 `pflegen Angehörige zu Hause` + 图表标题
    `WER PFLEGT ZU HAUSE? · Quem cuida em casa?` + 百分比 68% 锚定，练习 83（`68% em família`）与 85（68+20=88）均以百分比消歧，
    `em família` 本身不产生误读。裁定可接受 ✓。
    附注（非问题，沿用原校对 O4）：KIT §11 称完整形存活于“P6 图表阅读注文”，实测存活位置为 P6 gloss + P8 答案；行 1 完整形未存活一事 KIT 未披露，但不构成缺陷。
  - (c) P7 读者注文缩短与短语 7 葡译缩短：
    读者园地德语引言与核心逐字一致，未动 ✓；缩短后的葡语注文仍完整表达三事实（见门 9），
    “编辑部示例”标记由标签 `Um exemplo da redação!` 承担 ✓；
    短语 7：德语引言逐字未动；葡译 `A economia alemã deixa devagar a estagnação, mas a recuperação não se sustenta sozinha.`
    以 `não se sustenta sozinha` 保留“不能自持”义，2 行 ✓。裁定语义无损 ✓。

### 门 11 KIT 文字订正验证 —— 通过

- §1(c)：不实“as in DE×EN”登记已修正——现为 CORRECTION 段落，明确承认旧 claim 为 FALSE（DE×EN/DE×ES/DE×IT 均逐字保留德语句），并登记修复后逐字形式与 gloss 保留 ✓。
- §10：“no leftover English”断言已修正——现为 CORRECTION 段落，明确承认修复前恰 1 处残留（P8 item 5 `9 matches on matchday 9`），已修复为纯葡语，修复后重扫 0 处 ✓（我独立重扫亦为 0，见门 2）。
- §2/§10 针脚为改后值：§2 p7/p8 SVG 哈希 = 171e37ce…/e79f51f4…（与在盘实测一致）；§10 双 PDF 尺寸与 SHA = 改后值（4,144,470 B / 313ff763…；4,167,866 B / 58e7294c…，与在盘实测一致）✓。
  附注：本 KIT 的 PDF/SVG 针脚在 §2（版 SVG 哈希）与 §10（PDF/卡片），而非 §11（§11 为精简决定）；两处针脚均已更新 ✓。
- 状态：`fix round complete, NOT finalized, awaiting independent full re-proofread`——修复轮完成、待复校，未僭越定稿 ✓。

### 门 12 PDF/卡片全量 —— 通过

- 双 PDF（tools venv pypdf + sha256 独立实测，与 KIT 逐值一致）：
  - 印刷 `Die-Lucerna-VOL2-PT.pdf`：8 页、1462.5×2025 pt、**4,144,470 B**、sha256 `313ff7635f3cde5bcef10c08119bdec1d89c7c531d6280bd433f6c7eecd748d2` ✓；
  - 网页 `Die-Lucerna-VOL2-PT-web.pdf`：8 页、1400×1938 pt、**4,167,866 B**（<10 MB）、sha256 `58e7294ca04d4f722cf5664038ac73f31f352de241ab1ba04d8f98cbeac04f42` ✓。
- 8 张卡面（1950×2700）全部目视：无重叠、无截断；P1 卡确认徽章、sommaire S.3 间隙与 Zahlen 框；P6 卡确认图表标签与条形无遮盖；
  P7 卡确认词框三行、读者园地与工具箱完整、金句横线间距清晰；P8 卡确认答案区可读并肉眼确认 item 5 已为纯葡语注文 ✓。
- 150 题分页与等级分布（我独立 scratch 重渲染登记转储，不在在盘目录执行构建代码）：
  - TOTAL 150，连续编号 1–150；分页 **10/18/18/18/18/18/12/38**；等级 **A2 66 / B1 70 / B2 14**；
  - 类型：Escolha múltipla 52、Completar frases 41、Transformação de frases 11、Correspondência de palavras 12、Verdadeiro ou falso 8、
    Completar o texto 8、Construir frases 8、Completar o diálogo 5、Tradução 4、Escrita 1（=150，与核心类型计数 1:1）；
  - 与核心一致性另经渲染产物交叉验证：P8 答案分区逐页计数 10/18/18/18/18/18/12/38（P2 分区多出的 “31” 实为 item 13 注文内日期 `31 de dezembro` 的误匹配，非练习）；
    P1–P7 逐页等级 token 分布与核心逐页完全相同；item 5 登记 = {key: neun, note: 9 jogos na 9ª rodada}；item 140 登记 key 德语不变；
  - P7 col3 flow 终值 1504.5、P8 keys flow 终值 2352（均在底线内）；
  - scratch 重渲染 SVG 与在盘版 SVG **8/8 字节一致**（构建确定性证据）；事后在盘哈希全部未变 ✓。
- ABSTRACT.txt：单行（377 字节，末尾换行符除外）、**无 ASCII 双引号**、葡萄牙语；含 masthead `Die Lucerna`、目标语名称、A2–B2、150 练习；
  真实主题关键词：semana inglesa、Champions League、Europa League、9ª rodada da Bundesliga、Tankrabatt até 31 de dezembro、Ferienwechsel、cuidados em casa；
  学习者搜索短语：`aprender alemão lendo notícias de verdade`。
  事实锚点均核实：`até 31 de dezembro` 见 P8 答案注文（item 6/9/13）；`semana inglesa` 见本版 gloss（`die Englische Woche = semana inglesa`）✓。

## 非阻塞观察（已裁定不列为问题）

- O1：P8 注文连接符为无空格 `key(note)`，W43 为有空格 `key (note)`；无空格形式与 W45 DE×EN 构建码一致，属同族内形式变体（见门 5）。
- O2：同基线“1 项命中”是 `&amp;` 未解码的测量伪影（见门 6），真实间隔约 43–45px；卡面已证实干净。
- O3：P7 “1504.5”为 flow-cursor 口径，墨迹底为 1490.97；两种口径下右栏均未越过 y=1508 金句横线。
- O4：KIT §11 称完整形存活于“P6 图表阅读注文”，实测存活位置为 P6 gloss + P8 答案 84/86；行 1 完整形 `cuidado familiar` 全版无逐字存活（已裁定可接受，见门 10b）。
- O5：README #20 泛写 19.5pt vs W43 实测 20pt——按任务要求以 W43 实测裁定，本版与 W43 一致（见门 10）。

## 问题清单

无。12 门全部通过，原 2 项阻塞问题均已修复并独立证实。
