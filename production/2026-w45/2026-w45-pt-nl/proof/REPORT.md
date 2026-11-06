# W45 PT×NL 独立校对报告 — ZERO PROBLEMS（可定稿）

- 对象：`files/weekly-report-w45-pt-nl/`（svg×8、cards×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照：W45 葡萄牙语核心 `files/weekly-report-w45-pt-core/`；W43 同配对版 `files/weekly-report-pt-nl/`（家具以 W43 实测为准）
- 校对员：独立校对（只校对，不改源码；未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录；核心与 W43 仅只读对照；共享 `tools/scratch/` 未清理、未写入）
- 工具：`tools/`（`freeze.py`、`p8.py`、`occlusion_audit.py`，均用 `tools/venv/bin/python`）＋自有补充脚本（同目录 `audit.py` / `audit2.py` / `audit3.py`，输出 `audit*.txt`）
- 方法原则：构建员自述一律不采信，全部独立重测；下文所有数值均为本校对实测。

## 开工查重

- 首次检查（22:34 UTC）：交付目录最新写盘 22:33（WEEKLY-KIT.md）、构建目录最新写盘 22:31，无本版进行中的渲染进程。
- 90 秒后复查（22:36 UTC）：零新写盘 → 安全开工，非 stand down。复查时仅见一个无关进程（PT×RU 分版的 transform.py），与本版目录无关，不触发 stand down。
- 校对结束复核：交付目录 mtime 仍为构建员的 22:24–22:33，校对未改动任何交付文件；交付 18 文件哈希与构建员 `final.sha256` 逐一一致（见 §10）；核心哈希校对前后不变（见 §1）。

## 结论：ZERO PROBLEMS

10 门逐项独立重测全部通过，无阻塞项。下文“与构建员自述不符处”列出的均为非阻塞观察（口径/取整差异，或已裁定不构成缺陷的项），纸面门禁仍以交付 SVG 为准。

## 1. 冻结 — 通过

- `freeze.py baseline`（核心构建目录 `hidden_files/weekly-report-w45-pt-build` 重跑）：**8/8 字节复现**，与构建员记录的基线哈希逐一一致（p1 `0dc8089d…`、p2 `56db3aa8…`、p3 `82f6fc3a…`、p4 `c5647cf6…`、p5 `92e86020…`、p6 `e6097473…`、p7 `a72cb75a…`、p8 `82630480…`）；运行前后核心 SVG 哈希不变，校对结束时再次复核仍不变。
- `freeze.py diff --strict-cjk`（核心 vs 分版）：每页新增 CJK 均为 **0**；核心 CJK 总量 156/177/153/148/223/118/357/1123 → 分版 **0/0/0/0/0/0/0/0**（本校对文本节点扫描结果与 freeze 口径完全一致，无口径差）。
- 全文“桥接”：渲染文本 0、交付 KIT 0、构建源码 0。
- 葡语正文冻结：核心无 CJK 且长度 ≥25 的句子逐句核对，同页存活率 **100%（缺失 0 句）**。freeze-diff 的 removed 字符串中带拉丁字母的残余全部可归类，无一条是冻结葡语丢失：
  - (a) 葡语词头＋中文讲解的混合串（词头本身在荷兰语版中存活，如 `portões — portões = de poorten`）；
  - (b) 已备案家具替换（核心页脚英文式 `LUCERNA PORTUGUESE WEEKLY`、y=372 旧 strapline `O JORNAL SEMANAL PARA APRENDER — …`、各版带副标题/栏目标题的中文半句、P8 题干中文注释）；
  - (c) P8 答案行（键不变、注释中→荷，见 §3）。
- 讲解层语言：分版全部讲解为荷兰语（P8 注释 CJK 0，见 §3；英语 apparatus 0，见 §9）。

## 2. P7 词框冻结（硬性门）— 通过

- 葡语定义句逐字保留（核心 P7 与分版 P7 均在位）：
  > `« feriadão »: sábado, domingo e segunda — três dias de descanso.`
- 仅 gloss 本地化：核心 `feriadão = 连休长周末，共三天。` → 分版 `feriadão = het lange feestweekend, drie dagen.`。
- 无任何 DE/NL 家族词框内容：`NOCH EIN WORT`、`meedoen`、`Wort der Woche` 全 8 页 0 命中；分版 P7 词框即葡萄牙语核心的词框。

## 3. P8 — 通过

- `tools/p8.py compare`（核心 vs 分版，total=150）：**CLEAN，150 = 150，missing=[]，extra=0，uncertain=[]**；keydiff 与构建员所列完全一致：`[2, 4, 25, 26, 27, 28, 52, 53, 54, 55, 101, 137, 138, 141, 142, 143, 144, 146]`。
- `p8.py extract` 两边各为 noted set 150/150；本校对另从 SVG 文本节点重建 P8 答案行 150 行，核心与分版行号集合完全相等（缺失 0、多余 0）。
- 18 项逐项对照印刷行（印刷 key token = “ — ”之前的第一 token；token 相等性为本校对实测）：

| # | 类别 | 核心印刷行 | 分版印刷行 | token 相等 |
|---|---|---|---|---|
| 2 | 伪影 | `portões — portões = 大门（考场大门）` | `portões — portões = de poorten (van de examenlocatie)` | 是 |
| 4 | 伪影 | `13h30 — 13h30 开考（巴西利亚时间）` | `13h30 — 13h30: het examen begint (tijd van Brasília)` | 是 |
| 25 | 伪影 | `c — feriadão=连着周末的假期 c` | `c — feriadão = een feestdag vast aan het weekend (c)` | 是 |
| 26 | 伪影 | `b — cemitério=墓碑所在的地方 b` | `b — cemitério = waar de graven zijn (b)` | 是 |
| 27 | 伪影 | `d — vela=点亮纪念的物品 d` | `d — vela = wat je aansteekt ter nagedachtenis (d)` | 是 |
| 28 | 伪影 | `a — crisântemo=亡灵节带去的花 a` | `a — crisântemo = de bloem die je op Finados meeneemt (a)` | 是 |
| 52 | 伪影 | `b — finalista=进决赛的球队 b` | `b — finalista = het team dat de finale bereikt (b)` | 是 |
| 53 | 伪影 | `c — ida=对决的第一场 c` | `c — ida = de eerste wedstrijd van een tweeluik (c)` | 是 |
| 54 | 伪影 | `a — volta=对决的第二场 a` | `a — volta = de tweede wedstrijd van een tweeluik (a)` | 是 |
| 55 | 伪影 | `d — rodada=一轮比赛 d` | `d — rodada = een speelronde (d)` | 是 |
| 101 | 伪影 | `confiro — conferir：eu → confiro（不规则）` | `confiro — conferir: eu → confiro (onregelmatig)` | 是 |
| 137 | **真重定向** | `11 月 8 日周日是高考的第一天。 — 对照第 6 版标题` | `Zondag 8 november is de eerste dag van het Enem. — zie de kop van pagina 6` | 否（合法重定向） |
| 138 | **真重定向** | `周日前核对确认卡。 — Confira = 请核对` | `Controleer je kaart vóór zondag. — Confira = controleer` | 否（合法重定向） |
| 141 | 伪影 | `b — feriadão=连着周末的假期 b` | `b — feriadão = een feestdag vast aan het weekend (b)` | 是 |
| 142 | 伪影 | `d — portão=考场入口 d` | `d — portão = de ingang van de examenlocatie (d)` | 是 |
| 143 | 伪影 | `a — reta final=考前最后一周 a` | `a — reta final = de laatste week vóór het examen (a)` | 是 |
| 144 | 伪影 | `c — segunda chamada=关门后的再入场（高考没有） c` | `c — segunda chamada = opnieuw binnenkomen na sluiting (bij het Enem onmogelijk) (c)` | 是 |
| 146 | 伪影 | `A — seção = 考场分区（房间）` | `A — seção = de examenzaal (de sectie)` | 是 |

- 伪影机制与构建员所述一致：16 项均为 p8.py 的 key 字符串含本地化 gloss 文本所致（配对集 25–28、52–55、141–144 由裸字母尾标改为荷兰语 `(letter)` 括号式；2、4、101、146 的全角括号改为半角括号），答案 token 本身逐字节未变。成簇出现正是因为三组配对集共用同一版式切换机制，非单项异常。
- 139/140：葡语 key 逐字节未变（`O feriadão é de 31 de outubro a 2 de novembro.` / `Quando você chegar, apresente o documento com foto.`），仅注释中→荷，故正确不在 keydiff 列。分版印刷行：
  - 139：`O feriadão é de 31 de outubro a 2 de novembro. — feriadão = het lange weekend`
  - 140：`Quando você chegar, apresente o documento com foto. — aanvoegende wijs toekomst chegar + gebiedende wijs apresente`
- 150：p8.py 不列入 keydiff（两边均为 ✓ apparatus 式）；分版印刷行 `150. ✓ voorbeeldtekst in deel H (93 woorden)`，注释纯荷兰语。注：本校对朴素行重建会把页脚文本并入 150 行尾而显示 token 不等，那是重建伪影，应以 p8.py 的 apparatus 判定为准。
- P8 注释纯荷兰语：分版 P8 文本节点 CJK 0；P8 答案区字号实测 13pt（168 个节点，核心为 13.5pt，与 KIT 所述 13.5→13 一致）；P8 括号式为半角括号（与全部已发 DE 家族 fan-out 的代码惯例一致，非核心中文全角式）。
- P8 键流最深基线 2544.56（第 78 行），墨迹底仍在 2580 页脚规则之上；canonical 审计 FOOTER 0（见 §4）。

## 4. 几何 — 通过

- `tools/occlusion_audit.py`（自检先行：6 类阳性全部触发，干净对照静默）：分版 **0 flags**、核心 **0 flags**、NEW vs 核心 **0**，exit 0。
- 同基线墨迹碰撞扫描（全部 8 页，真墨盒，>1px x 重叠）：**0 碰撞**。
- 页框/右缘扫描（ADVANCE 法，框外 28..1922、内框 40..1910；页脚基线 2624 豁免）：每页 max advance-right 为 P1/P3/P4/P5/P6/P7/P8 的 1885.0 与 P2 的 **1897.3**，min advance-left 全页 65.0，**0 缺陷**。真墨盒右缘最大值：P2 1897.2，其余页 ≤1885.3，均在内框 1910 之内。
- P2 冻结葡语配对行重点复测：分版与核心均为 `d. o objeto que dá luz e se acende em`（x=1485，23pt），advance 右缘同为 **1897.3**（构建员称 1897.2，0.1px 为取整/超采样口径差），距内框 1910 尚有 **12.7px**，属继承（核心同值），非新溢出。非阻塞观察：该行基线在核心为 y=2304、分版为 y=2355（同栏整体下移 51px，文本与 advance 不变，审计干净，不构成缺陷）。
- P6 图表标签覆盖（基线锚定墨迹法：PIL `getbbox(anchor="ls")`，标签墨迹 vs 其后绘制的条形；条形实测在位：90/45/495 宽）：`portões abertos`、`espera`、`prova`×2、`60 min`、`30 min`、`330 min` 全部 **0.0%**（门限 <30%）。
- 全 8 页框线压框＋右缘扫描：canonical 审计 BOXTITLE/EDGE/LINEX 0；补充真墨盒扫描无任何文本墨迹穿越内框。
- P7 修复部位复测：金句行距 96.0（两栏 2040.5→2136.5→2232.5→2328.5 逐行差均为 96.0）；末行译文基线 **2378.17**，预告框顶 2404（框 `[65, 2404, 1885, 2522]`），余量 **25.83px**（构建员称 25.8px，取整差；round 2 前仅 1.8px 的说法与本测量的修复幅度一致）。
- P8 字号 13/1.12：字号 13 实测（见 §3）；行高由键流无溢出（FLOW 0、审计 0）佐证。
- round 1 的 16 NEW 是否全消除：构建员 history-run1 的 `occlusion-run1.json` 实测为 `flag_count=16, new_flag_count=16`（P7 COVER/TEXTX 6 项＋P8 TEXTX 10 项，与 KIT 所述两成因一致）；终版审计 0/0/0，**16 项全消除**。

## 5. gloss 与 P7 金句 — 通过

- gloss 计数（README #21 方法：`gloss()` 调用串本身按 `·` 拆分，源串取自分版与核心构建目录，逐项核对渲染存活）：
  - 核心：content12 6、content34 11（P3 6＋P4 5）、content56 9（P5 5＋P6 4），合计 26；
  - 分版：content12 6、content34 11、content56 9，合计 **26 = 26**；
  - 按页：P2 6、P3 6、P4 5、P5 5、P6 4，与任务书分布一致；
  - 26 项葡语词头全部在渲染中存活（`o feriadão`、`o cemitério`、`a vela`、`o crisântemo`、`a missa`、`conferir`；`o túmulo`、`a flor`、`acender`、`rezar`、`o silêncio`、`a lembrança`；`a ida`、`a volta`、`o finalista`、`a decisão`、`a rodada`；`a reta final`、`a véspera`、`a maratona`、`separar`、`a cabeça`；`os portões`、`a segunda chamada`、`conferir`、`a correria`）。
  - 方法注：直接按渲染文本节点 `startswith('Uitleg')` 分组会因换行切分而少计（本校对初试得 25），正确方法为源串拆分＋渲染存活核对；交付本身无问题。
- gloss 前缀：全部 gloss 框均为 `Uitleg — `（5 页齐全，无其他前缀）。
- P7 金句 8 句：每句在全刊裸文本中恰好 **2×**（原文页＋P7），标签与核心一致且源页实测存在，P7 上附荷兰语译文＋`(Página N)`：
  - `Do feriadão à prova: a semana do Enem`（P1）、`Muita gente viaja, visita a família e vai ao cemitério levar flores`（P1）、`Finados é o dia da memória`（P2）、`lembrar é um jeito de continuar perto`（P3）、`cada ponto vale uma posição, cada gol vale uma história`（P4）、`quem dorme bem lembra melhor`（P5）、`primeiro as fáceis, depois as difíceis`（P6）、`Confira o cartão, durma bem, chegue cedo`（P2）。
- P7 短语逐字取自本期文章：8 句均在其标注源页的文章正文中逐字出现（上表 per-page 计数为源页 1×＋P7 1×），无外来经典句。

## 6. 读者园地 — 通过（零编造；邀请范围裁定见下）

- 3 事实齐全（均在 P7 读者园地实测在位）：
  1. 截稿时无真实来信：葡语披露句原文保留 —
     `Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3.`；
     荷兰语披露句同义 —
     `Opmerking van de redactie: de echte brieven en beste teksten uit VOL.1 waren nog niet binnen — het voorbeeld blijft, de belofte gaat naar VOL.3.`。
  2. 无最佳 P8 作文：同一披露句中的 `os melhores textos` / `beste teksten` 即指此（与 VOL.1 承诺的“最佳文本”对应），荷兰语句同义覆盖。
  3. 示例＋VOL.3 承诺：示例逐字保留并标注 —
     `«Vou fazer o Enem no domingo 8. Já conferi o cartão. Boa prova!» — EXEMPLO DA REDAÇÃO`，无署名、无编造读者、无编造引言；承诺见披露句与邀请句。
- 显性荷兰语邀请（逐字摘录，P7 读者园地独立成句，非内容预告行）：
  > `Stuur je brief op: de beste verschijnen op pagina 7 in VOL.3!`
  - 祈使句 ✓（`Stuur je brief op`）＋刊登承诺 ✓（`de beste verschijnen op pagina 7 in VOL.3`），满足现行邀请门；前置句 `Voorbeeld van de redactie — geen echte brief.` 明确区分示例与真实来信。
- **最佳 P8 作文覆盖范围裁定（独立判定）：通过。** 理由与 PT×EN、PT×DE 的同类范围裁定先例完全一致：
  - 邀请句字面范围仅为来信：祈使动词的宾语是 `je brief`，`de beste` 最自然的回指就是“最佳来信”；句中未点名 P8 作文。此口径与 PT×EN（`Send your letters… the best will be printed in VOL.3`）和 PT×DE（`Beste Briefe erscheinen in VOL.3`）的裁定相同。
  - 最佳 P8 作文的征集覆盖不来自该邀请句本身，而来自同页两处显性表达：(a) 荷兰语披露句本身即为最佳文本的顺延承诺（`beste teksten … belofte gaat naar VOL.3`）——承诺刊登即征集的显性表达；(b) 同页预告框（葡语目标语正文，冻结）明言下期内容：`Mais: as suas cartas e os melhores textos da página 8.`——明确点名“第 8 页的最佳文本”将在下期刊出。
  - 三者合起来，读者在 P7 一页内即被明确告知：可寄信、可寄第 8 页作文，最佳者见 VOL.3。现行邀请门（页上须有真实来信的显性公开邀请＋三事实）满足，**不构成阻塞**。内容预告行未被计为邀请本身，仅作为覆盖范围的第二证据，与 PT×EN/PT×DE 的处理一致。
  - 补充（非阻塞）：P2 的 E VOCÊ? 荷兰语注释亦含完整投稿语（`stuur ze naar de redactie: de beste verschijnen op pagina 7`）；P3/P4 的荷兰语 E VOCÊ? 句将葡语 `mande para a redação` 简写为 `stuur ze op`（目的地隐含，句子完整、无截断），P5 的荷兰语句则在葡语无投稿语的情况下补了 `stuur ze op`，见“非阻塞观察”。

## 7. 家具（与 W43 同配对实测对照）— 通过

逐项取自 W43 `files/weekly-report-pt-nl/svg` 实测（非 README 泛值、非 PT×EN  sibling）：

- 徽章：y=372、19pt、BRICK `#a4553a`，文本与 W43 逐字同（仅 VOL 号随本期为 VOL.2）：
  `TEKSTEN IN HET PORTUGEES · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`（W43 同值；页脚复现的同串为 20pt 灰色，属页脚行，非徽章）。
- 副标题：y=330、**34pt**（W43 同为 34pt；PT×EN 的 38pt 未被套用，理由成立：W43 同配对尺寸＋荷兰语串在 34pt 下审计 0 标记，无需取英语 sibling 尺寸）：
  `PORTUGEES WEEKBLAD · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE`。
- 顶栏：`TODA SEMANA EM PORTUGUÊS · ELKE WEEK · HET PORTUGEES DAT BRAZILIË LEEST`，与 W43 逐字同。
- 版带右：`DE WEEK VAN HET ENEM` / `2 nov Finados-weekend · 8 nov dag 1 van het Enem`。
- gloss 前缀：`Uitleg — `（见 §5）。
- P8 分隔符：8 处均为 `— Pagina N —`（N=1..8），与 W43 实测 8 处同式一致；非 tables.json 的 NL 栏 provisional 空值，也非 PT×EN 保留的核心式 `— PÁGINA N —`。W43 实测为权威，沿用正确。
- 页脚：8/8 左 `A Lucerna · PORTUGEES WEEKBLAD VOL.2 · TEKSTEN IN HET PORTUGEES · UITLEG IN HET NEDERLANDS`，右 `Pagina N van 8`（N 正确）；W43 对应行为 VOL.1 同式。
- 版带标题（PT · NL）：`VIDA · LEVEN`、`CULTURA · CULTUUR`、`ESPORTE · SPORT`、`JOVENS · JONGEREN`、`APROFUNDAMENTO · VERDIEPING`、`LÍNGUA · TAAL`、`AVALIAÇÃO E RESPOSTAS · TOETS EN ANTWOORDEN`，全部在位。
- 栏目标题（PT · NL）：`A NOTÍCIA · HOOFDNIEUWS`、`AGORA VOCÊ · AAN DE SLAG`、`NESTA EDIÇÃO · IN DEZE EDITIE`、`EM POUCAS PALAVRAS · KORTOM`、`QUIZ RELÂMPAGO · BLITSQUIZ`、`PARA NÃO ERRAR · EZELSBRUG`、`E VOCÊ? · EN JIJ?`、`A SEMANA EM NÚMEROS · CIJFERS`、`OS HORÁRIOS DO DOMINGO 8 · DE TIJDEN VAN ZONDAG 8`、`A SEMANA DO FUTEBOL · DE VOETBALKALENDER`、`ERROS COMUNS · PAS OP!`、`A PALAVRA · WOORD VAN DE WEEK`、`FRASES DA SEMANA · ZINNEN VAN DE WEEK`、`A PRÓXIMA SEMANA · VOLGENDE WEEK (VOL.3)`、`EXERCÍCIOS · OEFENINGEN`、`RESPOSTAS · ANTWOORDEN`，全部在位；另有 `Antwoorden op pagina 8 · niveaus gemengd: zoek op nummer`（P2–P6）与 P8 `bij elk antwoord een korte uitleg in het Nederlands · ✓ = met voorbeeldtekst` 在位。
- 版带副标题追加式（与 PT×EN 整替式不同）：实测 P2 `NÍVEL A2 · Finados e revisão: o feriadão do Brasil · Finados en revisie: het lange weekend in Brazilië`、P3 `A2 → B1 · Finados: o dia da memória · Finados: de dag van de herinnering`、P5 `NÍVEL B1 · A reta final dos jovens · de eindsprint van de jongeren`、P6 `NÍVEL B2 · O Enem explicado · het Enem uitgelegd`、P7 `Focus op taal · Três níveis, três ferramentas · drie niveaus, drie hulpmiddelen`——葡语半句逐字保留、荷兰语短注追加。理由核实成立：W43 同配对 P2 版带副标题实测即为此追加式（`NÍVEL A2 · Como votar, passo a passo · stap voor stap stemmen`），同配对先例优先于 PT×EN 的整替式；且冻结葡语带标题不受损。
- 几何偏差（KIT §3 所列，均有实测缺陷成因）：P7 金句行距 128→96（本校对实测 96.0，见 §4）；P8 键字号 13.5→13（实测 13，见 §3）。未改动项与 KIT 一致：P1 数字框标题保持 23pt（`A SEMANA EM NÚMEROS · CIJFERS`，审计干净）、P7 词框底垫保持 20（审计干净）。

## 8. 图片 — 通过

- 全期仅 1 张照片：P1 `estudo.jpg`（图书馆学习照，x=65、y=1874、896×320）；P2–P8 的 SVG 中 `<image>` 均为 0。其余为原创图表（P1 时间表、P2 时间框、P4 赛程表、P6 分钟条形图＋两周日表）。
- 嵌入 payload：解码后 JPEG 字节分版＝核心（256,737 B；sha256 `cc351a4d…a83771c`；md5 `04b18fa952a61c9998ef5bf3325341f2`），与 PT×DE 校对报告的解码测量一致。
- 署名行在 P1 照片下方在版（卡片目视在位）：`Foto: Gary Todd / Wikimedia Commons — CC0`（CC0，Gary Todd）。
- 口径注（非阻塞，见下）：构建员 KIT 所载 `fd231e77…` 为 base64 文本本身的 sha256（本校对复现一致），非解码 JPEG 的哈希；“与核心一致”的结论在两种口径下均为真。

## 9. 跨族残留 — 通过

- 中文逐页 0：CJK（含全角范围）文本节点计数分版 8 页均为 0（核心 156/177/153/148/223/118/357/1123，见 §1）。
- 全 8 页英语 apparatus 重扫 0：`Note |`、`Page N of 8`、`Answers on page`、`Levels are mixed`、`Complete the sentence`、`Multiple choice`、`Build the sentence`、`True or false`、`Cloze`、`Vocabulary matching`、`Sentence building`、`Fill in`、`Match the pairs`、`IN THIS ISSUE`、`IN NUMBERS`、`Text in Portuguese`、`Explanations in English`、`THE EDITION FOR ENGLISH-SPEAKING`、`PORTUGUESE WEEKLY`、`Editor's note`、`Send your letters` 等无一命中；`Note` 单词本身 8 页 0 次。
- 其他族标记 0：`HINWEIS`、`Seite`、`EXPLICATIONS`、`EXPLICACIONES`、`SPIEGAZIONI`、`Nota — ` 全 0。
- ABSTRACT：荷兰语单行（1 行、418 字符）、ASCII 双引号 0 个；含真实主题关键词（Enem、Finados、8 november、poorten 12h–13h、examen 13h30–19h、Copa do Brasil returns）＋学习者搜索短语（`voor wie Portugees wil leren door Braziliaans nieuws te lezen`）＋刊名（A Lucerna Portugees Weekblad VOL.2）＋目标语名（Portugees）＋讲解语（Nederlands）＋A2–B2＋150 oefeningen。摘要节标题词按 tables.json NL 栏应为 `Samenvatting`（供 insert.py 用，交付 ABSTRACT.txt 本身为单行正文）。

## 10. 卡片目视与题量/交付完整性 — 通过

- 8 张卡片（1950×2700）全部逐页目视：无重叠、无截断、无压框、无压页脚；8 页（4 的倍数）；页脚 8/8 齐全。
  - P1：徽章、副标题、版带、数字框、照片＋署名、快讯、目录、测验——干净（目录行 `Pág. 3 Finados, o dia da memóriaA2→B1` 紧贴间距为核心保留项，见 KIT §11，可读、无重叠）。
  - P2：版带副标题在版、时间框在版、配对集在版——干净。
  - P3：gloss 框、日历框、E VOCÊ 框、练习——干净（栏末留白为核心保留的呼吸空间先例）。
  - P4：赛程表、gloss 框、配对集、比较级——干净（`B · AS PALAVRAS` 栏题位于第 1 栏末、题项顺流至第 2 栏，属流式排版，无重叠）。
  - P5：计划框、gloss 框、E VOCÊ 框、练习（含 Waar of onwaar）——干净（计划清单 1–5 为文章内容，非练习题，计数时已排除）。
  - P6：分钟条形与标签/数值无遮挡、两图表框、来源行——干净。
  - P7：三语级专栏、易错诊所、词框、读者园地（葡＋荷披露、标注示例、显性邀请）、8 金句与预告框无接触、VOL.3 预告框完整——干净。
  - P8：练习 113–150、范文（93 词）、全键 1–150 与 `— Pagina N —` 分隔符、键流止于页脚规则之上——干净。
- 题量独立展开计数（渲染后 24pt 题号节点＋19pt 级别徽章邻近匹配；配对集按范围节点展开；P5 计划清单 21pt 非题号节点已排除）：
  - 按页：P1 10（1–10）、P2 18（11–28）、P3 18（29–46）、P4 18（47–64）、P5 18（65–82）、P6 18（83–100）、P7 12（101–112）、P8 38（113–150），合计 **150**，编号连续无缺重；
  - 按级别：P1–P7 部分 A2 40／B1 47／B2 25；P8 部分 A2 9／B1 23／B2 6（其中 141–144 配对集以其范围节点 `141–144.` 的 B2 徽章计），合计 **A2 49／B1 70／B2 31**，与任务书核心数一致。
  - 题型登记：印刷题头不承载完整题型 taxonomy（与核心同构：核心亦无 `完成句子`/`单选`/`完形` 印刷题头），小类可由印刷题头精确佐证——`Bouw de zin` 7＝造句 7、`Vertaal` 4＝翻译 4、`Combineer` 3 个范围题头覆盖 12 项＝配对 12、`Waar of onwaar?` 3＝判断 3、`Schrijven` 1＝写作 1；大类（完成句子 61、单选 49、完形 13）为登记口径，其和与 stem 总数 150、键集 150、按页／按级展开数三方一致。
- 范文：P8 H 区范文 93 词，与核心逐字一致（全文比对相同，起 `Domingo, 8 de novembro, acordo cedo…` 止 `…o segundo vem no domingo 15.`）。
- PDF：印刷版 3,510,712 B、sha256 `c80072a24602c72eb73cfdf995aee937762e2dd2a2c8874f4f0ef7adab2c11b8`、8 页、1462.5×2025pt、文本可提取（36,066 字符）、含 1 图；网页版 3,500,683 B（<10 MB）、sha256 `f076efce6e08285f7480f07e7ea34e904f35ccc8c6afa54585bfa9bf1113ae02`、8 页、光栅页（8 图、0 可提取文本——与核心及 PT×EN 网页版同构，属网页版既定形态，非缺陷）。
- 校对前后交付与核心哈希不变：交付 18 文件与 `final.sha256` 逐一一致；核心 8 SVG 校对前后哈希一致。

## 与构建员自述不符处（全部非阻塞，不影响结论）

1. **图片哈希口径**：KIT §6/§13 所载 `fd231e77…` 是 base64 文本的 sha256，不是解码 JPEG 的哈希；解码 JPEG 的 sha256 为 `cc351a4d…a83771c`（分版＝核心）。“嵌入 blob 与核心相等”的结论在两种口径下均为真，仅 KIT 未注明口径（PT×DE 校对报告曾记录同一口径差）。
2. **P2 右缘取整**：构建员称 1897.2，本校对 ADVANCE 法得 1897.3（真墨盒 1897.2）；余量相应为 12.7px 而非 12.8px。核心同值，结论（继承、框内）不变。
3. **P7 余量取整**：构建员称 25.8px，本校对得 25.83px（2378.17→2404）。结论不变。
4. **P3–P6 真墨盒右缘**：构建员 ADVANCE 法称 1885.0，本校对真墨盒法得 1885.3（`Antwoorden op pagina 8…` 行），仍在内框 1910 内 24.7px。方法差，非缺陷。
5. **P2 配对行纵向位移**：冻结行 `d. o objeto que dá luz…` 基线核心 y=2304 → 分版 y=2355（＋51px），文本与 advance 不变、审计干净。KIT 未提及此位移，不构成缺陷。
6. **P8 键流末行表述**：KIT 称“键流止于页脚之上”；实测最深键基线 2544.56（第 78 行），墨迹底约 2549，仍在 2580 规则之上、canonical FOOTER 0。表述宽松但门禁通过。
7. **E VOCÊ? 荷兰语措辞**：P3/P4 的荷兰语 E VOCÊ? 句将葡语 `mande para a redação` 简写为 `stuur ze op`（目的地隐含）；P5 的葡语原文无投稿语，荷兰语补了 `stuur ze op`；P2 保留完整式 `stuur ze naar de redactie: de beste verschijnen op pagina 7`。各句均为完整句、无截断，P7 邀请门独立成立，故不阻塞。
8. **P8 #150 行重建伪影**：朴素行重建会把页脚并入 150 行尾（见 §3 注），应以 p8.py 的 apparatus 判定为准；150 不在 keydiff 列正确。

## 非阻塞观察（注明不阻塞）

- P1 目录行紧贴间距（`…memóriaA2→B1`）与 P3/P5 栏末留白均为核心保留项（KIT §11），目视可读、无重叠，保留。
- 网页版 PDF 为光栅页（见 §10），与核心及 PT×EN 网页版同构；印刷版文本可提取，互补完整。
- 构建员 KIT §8 所述 round 2 前末行译文基线“仅 1.8px”与终版 25.83px 的修复幅度一致；round 1 的 16 NEW 在 history-run1 存档中可复现（见 §4）。
- 本校对未宣布上架、未做任何投递动作；本报告仅为校对结论，供主线决定是否定稿／入库。

## 证据文件（同目录）

- `audit.py` / `audit.txt`：CJK、禁词、P7 词框、gloss 框初查、P7 金句、读者园地、家具（W43 对照）、图片、英语 apparatus 扫描
- `audit2.py` / `audit2.txt`：p8.py extract、P8 18 项逐行对照、gloss() 源串计数与渲染存活、冻结葡语句存活、freeze-diff 拉丁残余归类、版带副标题、图片哈希双口径、ABSTRACT、PDF、印刷题头统计
- `audit3.py` / `audit3.txt`：同基线墨迹碰撞、ADVANCE 右缘、P2 冻结行、P7 行距与预告框余量、P6 标签覆盖、真墨盒右缘
- `freeze-baseline.json`、`freeze-diff.json`、`p8.json`、`p8-core.json`、`p8-edition.json`、`occlusion.json`（canonical 工具输出）
- `core-start.sha256` / `core-end.sha256`（核心校对前后哈希）、`delivery-baseline.sha256` / `delivery-end.sha256`（交付与 final.sha256 对照）
- 另：构建员 history-run1 `occlusion-run1.json`（round 1 的 16 NEW 存档）由本校对只读复核，非本目录文件
