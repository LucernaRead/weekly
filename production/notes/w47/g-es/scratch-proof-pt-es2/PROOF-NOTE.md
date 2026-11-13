# PROOF-NOTE — 2026-W47 pt-es（葡萄牙语目标 · 西班牙语读者版）· proof1 独立复校（重建版）

- 版目录：`production/2026-w47/2026-w47-pt-es/`（重建版，core-pt fix1 + fix2 后重建）
- 复校员：独立复校（proof1），2026-11-11
- Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-es2/`
- 身份：印 `f1b4fc207a3575391868aeb9c8f7d0f34659c434ecf3a13c85c8cba19362a0d4` / 12,933,062 B；网 `d00e8f5420750496b7cb7551eab51e7207a123b1c3f0a55896aead83dac4ae7c` / 1,140,276 B；文 `96d6f11a5616ab97291115bb9da0577bce8049031f14988576f6cced77b29e27` / 37,467 B——三者 SHA 与任务书逐字一致。

## 结论：(b) 有 1 项缺陷，不能定稿

仅 **1 项缺陷**：P1 奶油框标题 `EN BREVE` 在交付的印/网 PDF 中墨迹超出框右缘 **3px**。其余全部机械门通过；首轮 7 项缺陷中的 6 项已修复并存活（§2），150 题逐题手验全部通过（§4）。

**源文件未改动、未重建、未 commit、未 push。**生产目录 47 文件、core-pt 41 文件开工收工 SHA 复核零改动。

## §1 缺陷清单

### D-NEW1 — 轻微 · P1 · 本版（盒标题真墨溢出）

- **位置**：P1 右栏 EM POUCAS PALAVRAS 奶油框标题 `EM POUCAS PALAVRAS　EN BREVE`。
- **源码行**：`content12.py:139`：`p.text(bx + 22, 1914, "EM POUCAS PALAVRAS　EN BREVE", 24, "sans", True, OLIVE)`；框 rect（SVG）：`x=1439.5 y=1874 w=422.5 h=474` → 框右缘 **1862.0**（框高 474 为 fix1 由 436 加高而来，修的是 D1 的底边问题，标题未动）。
- **实测证据（三法一致）**：
  1. advance（`boxtitle_core.py`）：标题宽 404.1，右缘 1865.6，clear **−3.6**；
  2. PIL 真墨（`boxtitle_trueink.py`，版内 svglib `_pil` + getbbox anchor='ls'，24pt 粗体本字号）：真墨右缘 1865.5，clear **−3.5**；
  3. **交付 PDF 渲染**（`pdf_render_titles.py`，交付印 PDF 经 pdftoppm 96dpi 渲染，1:1 SVG 单位）：标题行最右深色像素 x=1865，clear **−3**；逐列计数：x=1863 有 9px、1864 有 6px、1865 有 2px 深色像素（亮度<190）；网 PDF 同页渲染亦为 1865，clear −3。
- **渲染证据**：`p1-enbreve-title-pdf.png`（交付印 PDF 渲染 4× 裁切）：末字母 `E` 的三道横臂落在奶油盒外的白纸上；`render/print-p-1.png` 整页同见（需放大）。
- **为什么首轮没抓住**：首轮 O2 称该标题“墨迹恰止于 1862（0px）”——其测量对象是 CairoSVG 重渲的卡片 PNG。本次重测证实：同一 SVG，CairoSVG 卡片读 1862（0px），而**交付 PDF 的渲染读 1865（−3px）**。两者用的同一字体文件（fontconfig 与 svglib 均解析到 `NotoSansCJK-Bold.ttc` SC face），差异来自渲染路径的 hinting/字距取整：卡片路径把整行收窄约 3px，PDF 文本布局按未取整 advance 排字（PDF 内该标题第二 span：origin svg-x=1752.4，advance 右 1867.7）。交付物是 PDF，故以 PDF 渲染为准。PIL 度量（−3.5）与 PDF 渲染（−3）互相印证，卡片 0px 是假阴性。
- **判定依据**：任务书缺陷标准——墨越过可见边即缺陷。末字母 `E` 的横臂 3px 位于框外白纸上，且越过版心右缘 1862；同类先例：pt-de D4（+0.5）与 pt-en D-B1/D-B2（+21.5/+14.5）均记为缺陷。3px 属轻微，但门限是 0。
- **修复建议**：缩短该标题 gloss（如 `EN BREVE` → `Breve`，与 D4/D5/D6 的缩短 gloss 同法）或将该标题字号 24pt → 23pt（宽度约缩 4%，右缘 ≈1848，余量 +14）；改后重跑 gates + boxtitle + **PDF 渲染**复核（只测卡片会重蹈 0px 假阴性）。

## §2 首轮缺陷修复存活复验（7 项 → 6 项已修复，1 项新发现）

| # | 首轮缺陷 | 本次复验 | 结果 |
|---|---|---|---|
| D1（核心） | P1 EM-BREVE 框末行整行在框外 +33px，分隔线穿字 | 框高 436→474，底边 2310→2348；末行基线 2327.6、真墨底 2332.6、余量 **+15.4**（creambox-diag）；卡片逐行：墨止于 2332，框下 2333–2348 无墨；PDF 渲染：墨止于 2331，分隔线现于 2349–2350（框外 422px 通栏线，与文本分离） | **已修复，存活** |
| D2（核心） | P3 日程框末行 `16h30.` 在框外 +16px | 框底 525→551；末行基线 540.6、真墨底 540.9、余量 **+10.1**；卡片/PDF 渲染：墨止于 539/540，框下无深色行 | **已修复，存活** |
| D3（核心） | P6 时间线框末行降部越边 6px | 框底 840→854；末行基线 840.8、真墨底 846.0、余量 **+8.0**；卡片逐行：降部墨 841–845 在框内，846 后无墨；PDF 渲染：墨止于 844 | **已修复，存活** |
| D4（本版） | P2 `PARA NÃO ERRAR　La regla para recordar` +67px | 源 `tables_es.py:58`「口诀」→`La regla`、`content12.py:183` 均已落地；旧长 gloss 全版 0 处；PIL 真墨 863.5、clear **+97.5**；PDF 渲染 863、clear **+98**；卡片 865、clear +96 | **已修复，存活** |
| D5（本版） | P7 `ERROS COMUNS　Errores frecuentes` +13px | 源 `tables_es.py:107`「常见错误」→`Errores`、`content7.py:82` 已落地；PIL 真墨 1750.5、clear **+111.5**；PDF 渲染 1750、clear **+112** | **已修复，存活** |
| D6（本版） | P7 `A PALAVRA　La palabra de la semana` +17px | 源 `tables_es.py:136`「本周生词」→`La palabra`、`content7.py:93` 已落地；PIL 真墨 1724.5、clear **+137.5**；PDF 渲染 1724、clear **+138** | **已修复，存活** |
| D7（核心） | P8 范文第 2–3 行超出版心 +2/+14px | 范文已重排（第 2–3 行现为 `despertador…leio sobre` / `Zumbi e Palmares…`）；PDF 渲染 10 行最右墨 1829、最小余量 **+33**；卡片最右墨 1840、最小余量 +22 | **已修复，存活** |
| D-NEW1 | —（首轮 O2 误判为 0px，见 §1） | 交付 PDF 渲染 −3px | **新增缺陷，见 §1** |

## §3 补充检查（pt-it 线索，独立量测、独立判定）

### S1 — P2「PARA NÃO ERRAR」框标题：通过，不复现 pt-it 缺陷

- pt-it 版同框意语 gloss「La regola da ricordare」PIL 真墨右 1020.5、框右 961.0、漫出 −59.5。本版同框标题「PARA NÃO ERRAR　La regla」独立三法量测：PIL 真墨（23pt 粗体本字号）右 863.5、clear **+97.5**；advance 右 863.7；交付 PDF 渲染最右深色像素 863、clear **+98**。裁图 `p2-para-title-pdf.png` 目视：标题止于框内近 100px 处。
- 结论：**通过**。不复现的原因是 gloss 长度：西语 `La regla` 9 字符，意语 `La regola da ricordare` 21 字符。源：`tables_es.py:58`、`content12.py:183`；SVG 标题元素 x=556.5 y=642.02 fs=23 bold；框 x[538.5, 961.0]。

### S2 — P1 顶栏标语「El portugués que lee Brasil」：语法成立，不记缺陷（附观察项 O-S1）

- 核实：`tables_es.py:201`「读巴西人正在读的葡萄牙语」→「El portugués que lee Brasil」；渲染于 P1 顶栏中段（SVG y=92，fs=17，letter-spacing 1.7，x=622.6–1327.4，居中于 x=975）。
- **独立判定：原句成立，不构成主客颠倒。**语法依据（书面）：
  1. 西班牙语关系从句中，`que` 可作直接宾语，主语后置于动词之后——标准句式，如 `el libro que lee Juan`（胡安读的那本书）、`el quechua que habla Perú`（秘鲁说的克丘亚语）。「El portugués que lee Brasil」按此式解析即「巴西读的葡萄牙语」，主语为后置的 `Brasil`，宾语为先行的 `el portugués`。
  2. 反向解析（`que` 作主语＝`el portugués`，`Brasil` 作宾语）被语义选择封堵：`leer` 要求有生主语（能阅读者）；语言本身不能阅读，而 `Brasil` 可转喻指巴西人（新闻语体常见，如 `Brasil vota`、`Brasil celebra`）。`leer Brasil`（把巴西当阅读对象）则无义。
  3. 动词 `lee` 单数与两者均一致，无形态线索——消歧全凭语义，而语义唯一指向意定读法；与已接受的英文定稿 `The Portuguese Brazil is reading` 结构等价（宾语前置 + 主语）。
- **但如实记录**：该句表面确有歧义——按频率最高的增量解析，`que` 先被当作主语，首读会闪现倒置义（「葡语读巴西」），须经语义再分析纠正；对西语学习者读者（本刊受众）而言，第一眼的歧义更明显；协调员与 pt-it 复校员被同一句式绊住，即是佐证。这是清晰度瑕疵，不是语法错误，故不记为缺陷、不阻塞定稿，列为观察项 O-S1，建议协调员裁定是否采用下述已量测的替代表述。
- **改后行宽量测**：替代表述「El portugués que leen los brasileños」（复数动词与 `los brasileños` 一致，主语显明，歧义消除，且与中文原文「巴西人」完全对应）——整行 17pt + letter-spacing 1.7，居中于 x=975 时跨度 **[577.6, 1372.4]**（按 n 计 letter-spacing 则 [576.8, 1373.2]）；在版心 [88, 1862] 内，左段止于 327.2（余量 +250）、右段起于 1459.5（余量 +87），**放得下，无碰撞**。现行句跨度 [622.6, 1327.4]（实测 PDF span 至 1328.6）。

## §4 机械门（全部独立重跑，见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| 身份（字节+SHA-256） | 三 SHA 与任务书逐字一致 |
| run.py 重跑（build-copy 内） | **rc=0，TOTAL 150**；A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38；FLOW OVERFLOW 0；重建 SVG **8/8 字节一致** |
| gates.py（版内自检，只读） | **16/16 PASS，FAILURES: none** |
| freeze baseline（核心重建 vs 发货核心 SVG） | **8/8 byte-identical**（--build 指 core-pt 的 build 目录，--core-svg 指 core-pt 的 svg 目录） |
| freeze baseline（版重建 vs 发货版 SVG） | **8/8 byte-identical**（补充自比对） |
| freeze diff（核心对照） | 新增 CJK 共 9 个，全部为 U+3000（P1 2、其余每页 1）；新增汉字 0 |
| occlusion 真实审计 | **0 flags**；内置自检 6 类全触发、干净对照静默 |
| p8 extract | **150/150** |
| p8 compare vs 核心 | **CLEAN**，missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138]（预期，翻译题答案） |
| keycheck | **149/150**；唯一不符 #150（开放作文，提取为 `✓`，预期） |
| text.md Respostas vs REG 键 | **149/150 一致**（Q150 为同义表述差，预期） |
| 印/网文字层 | `pdftotext -layout` **逐字节相同 109,231 B**；逐页 8/8 相同；`check_final` 词多重集 diff 0（各 8,576 词），页数 8/8 |
| P8 最小字号 | **9.75pt**，低于 9.75pt 0 处；答案区 185 spans、1,607 词 |
| creambox 真墨 | 31 个 OWN 末行全部正余量（最小 −0.3px 两处经卡片裁决为字体度量 artifact，框下 0 深色像素）；D1/D2/D3 真墨底余 +15.4/+10.1/+8.0 |
| boxtitle | **1 处溢出**（见 §1）；其余 29 盒最小正余量 +10.5（advance）/+12（PDF 渲染） |
| sweep | box-vs-hline 0；bridges 20，orphans 0，widows 0 |
| 重渲对比（仅 scratch 副本） | 印 PDF 重渲 **SHA 与交付逐字相同**（`f1b4fc20…`）；网 PDF 重渲 SHA 浮动（`c792a22b…`，1,140,275 B，预期浮动），**文字层与交付网 PDF 逐字节相同** |
| check_s11 | 仓库与 pt 家族内无此名检查（见 GATE-LOG §2）；gates.py 16 项 + check_final.py 已覆盖并全 PASS |

## §5 150 题逐题手验（题干与键逐项适配）

- 方法：通读 text.md 534 行全部练习题干与答案，逐题核对键是否适配题干；另以 keycheck-150.json（REG vs P8 提取键）与 Respostas 三方比对为机械背书。P8 compare CLEAN 只核对题号集合，不核对键与题干配对，故手验独立进行。
- **150/150 通过**。逐项要点：
  - Q1–10：题干与键一致（Q7–10 quiz：B/B/C/B）。
  - Q11–28：Q11–15 全 B（日 20/周五/三天/减班/27 日，题干各有出处）；Q16–20 现在时变位 cai/dura/descansamos/abrem/aproveita；Q21–24 数字 3/1695/2023/27；Q25–28 配对 a/b/c/d（feriadão/folga/programação/aproveitar 定义正确）。
  - Q29–46：Q29 C（1695-11-20）、Q31 B（14.759 使成国定假日，12.519 仅设纪念日）、Q33 A；Q34–39 填空 quilombo/resistência/escravizados/líder/memória/combate；Q40–43 过去时 morreu/nasceu/defendeu/formaram；Q44–46 组句与键逐字一致。
  - Q47–64：Q47 A（1–1，总 3–1）、Q48 B（2–1，点球晋级）、Q49 B（5–4）、Q50 B（单场，12 月 6 日）、Q51 A（Norris）；Q52–55 配对 b/a/d/c（定义正确）；Q56–59 比较级 mais/mais/mais/menos（16h30 早于 17h 为 mais cedo；两日少于一周为 menos）；Q60–64 过去时 empatou/venceu/abriu/garantiu/foram。
  - Q65–82：Q65–69 B/B/A/B/B；Q70–75 gabarito/oficial/extraoficiais/**espera**/nota/pesa——**Q73 重点核验**：「Depois da prova, começa a ___.」键 `espera` 与正文「Depois da prova, começa…a espera pelo gabarito」贴合，题干动词 `começa` 与 `espera` 搭配自然，无三源同错；Q76–79 将来时 sairá/publicarão/decidirá/chegará；Q80–82 V/F/V。
  - Q83–100：图表算术独立验算——11 月 16–30 日共 15 天，工作日 10 天（16–19、23–27、30），周末 + 假日 5 天（21、22、28、29、20），10+5=15；Q83 B（15）、Q84 A（10）、Q85 B（5）、Q86 B（15）、Q87 B；Q88 A、Q89 B（两周日 8/15）、Q90 B、Q91 B、Q92 B；Q93–96 serão/contam/fixa/pesa；Q97–100 词库 prazo/dia útil/coerência/chute（「Um chute certo vale menos do que um acerto consistente」）。
  - Q101–112：em/numa/é/B（aproveitamos）/empatou/venceu/abriu/B（saíram）/sair/for/tiver/B（sair）——Q108 `saíram` 含重音正确，Q112 未来虚拟式正确。
  - Q113–132：A/A/B/A/B/A/A/B（Q116 6 日、Q117 Palmeiras、Q119 15 日、Q120 五小时 13h30–18h30）；Q121 B、Q122 A（3–1）、Q123 B、Q124 B、**Q125 A（36 轮：正文称 35 轮止于周四 19 日，故周六 21 日场次属 36 轮，题干正确）**、Q126 B、Q127 A、Q128 A；Q129–132 B/B/A/B（Rafael：Salvador/周五 capoeira/周六 Palmeiras×Flamengo/周一查 extraoficial）。
  - Q133–136 组句逐字正确；**Q137/138 译文手验正确**（El viernes 20 de noviembre es festivo nacional. / El Palmeiras ganó 5–4 en los penaltis.——keydiff 预期项）；**Q139/140 反向翻译手验正确**（La clave oficial…→ O gabarito oficial sai até o fim de novembro. / Apunta tus respuestas…→ Anote as suas respostas e confira quando sair o gabarito oficial.）。
  - Q141–144 配对 c/d/b/a（定义正确）；Q145–149 全 A（Mané/sexto/quinto/**na internet**/obrigado——Q148 `na internet` 正确，`no internet` 为错）。
  - Q150：开放作文；范文手数 **88 词**（× 计为一词，与构建器 `model words: 88` 一致），内容覆盖周五/周六/周日三日与 20 日纪念意义。
- 事实抽查：星期全部 `date -d` 核实（11-07 周六、11-08 周日、11-15 周日、11-16 周一、11-17 周二、11-18 周三、11-19 周四、11-20 周五、11-21 周六、11-22 周日、11-27 周五、12-06 周日）；Lei 12.519/2011 设日、Lei 14.759/2023 为国定假日、Enem 两日 8/15 日时段 13h30–19h/13h30–18h30、90 题 5 小时、10 个工作日计至 11 月 30 日、Grêmio 争第六冠（已有 5 冠）/Palmeiras 争第五冠（已有 4 冠）、Os Lusíadas 1572 年首版、Parreiras 1927 年 Zumbi 画像——均与版面一致（核心事实承首轮 KIT §2 公开来源核实，本次未发现抵牾）。

## §6 判为非缺陷的项（证据见 GATE-LOG）

- **O1**：P4/P5/P7 词框 −0.3px 真墨底余为字体度量 artifact：卡片上框底以下 30px 窗口内 0 深色像素；P5 E VOCÊ 框 +0.4px、P2 +0.3px，墨迹均在框内。P5 数字框 `2027.` 余量 +4.9px。
- **O2**：creambox 4 处负余量均为盒外后继标题行（P1 `AGORA VOCÊ`、P2 `Atenção:`、P3 `UM DIA, DOIS SENTIDOS`、P6 `EXERCÍCIOS`），非溢出；D1 框下 2349–2350 行的 422px 横线为 quiz 分隔线，位于盒外、与末行墨迹分离 17px。
- **O3**：P1 `EN BREVE` 之外其余 29 盒标题最小正余量：advance +10.5（`A SEMANA EM NÚMEROS　En cifras`）、PDF 渲染 +12；P2 `Palmeiras × Flamengo, às` +22。
- **O4**：D5 字体问题只记录（GATE-LOG §2）：P7 A2 gloss ASCII 单引号 `'caer en un día'`，与 en/de 版 gloss 约定一致，拉丁解释层字体事待用户裁定。
- **O5**：`｜`（U+FF5C）×6 为 gloss 分隔符（`Nota｜…`、`Palabras clave｜…`），非汉字，与 en 版同数；text.md CJK 表意字 0；p1 的 3 个表意字在 moth logo 内部不可见 `<title>Lucerna 三色蛾</title>` 中。
- **O6**：Q38 `Sem ___ , não há futuro.` 的空格+逗号为与核心版逐字相同的空白占位符固有格式；P8 答案行 `56. mais — 3 > 1:mais` 等 4 处冒号为键值分隔符，同核心格式。
- **O7**：P2/P3/P4 练习区栏底小标题（如 P2 栏 3 底 `D AS PALAVRAS`、P3 栏 1 底 `B AS PALAVRAS DO TEXTO`）与内容分置两栏，属本刊多栏流式版式常态，无遮挡无溢出（sweep bridges 20、orphans 0、widows 0）。
- **O8**：P1 顶栏标语歧义见 §3 S2（O-S1），不记缺陷。
- **O9**：首轮 `freeze_direct` 在仓库 `tools/freeze.py` 中无此子命令（仅有 `baseline`/`diff`）；本次 freeze 证据为 baseline 直接重跑 8/8（核心与版内两种读法）+ diff。如协调员另有所指的 freeze_direct 步骤，请指明路径。

## 核实摘要

- **印 PDF 8 页 + text.md 全文已通读**（8 张整版目检 + text.md 534 行逐行读过）；星期 12 个日期全部与版面一致。
- **150 题逐题手验：150/150 通过**（§5；P8 提取键与 text.md Respostas 摘要 149/150 一致，Q150 为开放题表述差，预期；范文 88 词已手数）。
- **机械门实跑**：gates.py 16/16 PASS；occlusion 0 flags；creambox 31 框；p8 extract 150/150；p8 compare CLEAN，keydiff=[137, 138]；freeze baseline 核心 8/8 + 版内 8/8；freeze diff 新增 CJK 仅 U+3000（9 个）；印/网 PDF 文字层逐字相同（109,231 字节）；P8 最小字号实测 **9.75pt**（= SOP §1.1 下限）；弯引号 U+201C/U+201D 各 2（仅 P8 E139/E140）、U+2019 0；text.md CJK 表意字 0。
- **首轮修复复验**：D1/D2/D3/D7 核心修复与 D4/D5/D6 本版修复**全部存活**（§2）。
- **补充检查**：S1 P2 标题通过（PIL +97.5 / PDF +98）；S2 标语语法成立、不记缺陷，替代表述已量测放得下（§3）。
