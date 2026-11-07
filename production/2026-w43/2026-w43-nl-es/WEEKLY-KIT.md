# WEEKLY-KIT — De Lucerna VOL.1 · NL × ES（荷兰语正文 × 西班牙语讲解）

目标语正文 = 荷兰语核心（冻结）；讲解层全部以西班牙语原生写就。刊期：2026 年 10 月 19–25 日（W43）。构建目录：`hidden_files/weekly-report-nl-es-build/`（自 `hidden_files/weekly-report-nl-build/` 复制改写）；产物目录：`files/weekly-report-nl-es/`。

## 一、身份与配对标示（如印出）

- 刊头：De Lucerna（原样冻结）。
- P1 标示带（砖红 #a4553a 粗体，置于头条横幅下、HET NIEUWS 之前，y=568）：«TEXTOS EN NEERLANDÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES»。
- 页脚（每页）：«De Lucerna · SEMANARIO NEERLANDÉS VOL.1 · TEXTO EN NEERLANDÉS · EXPLICACIONES EN ESPAÑOL» / «Página N de 8»。
- 顶栏：「ELKE WEEK IN HET NEDERLANDS · CADA SEMANA EN NEERLANDÉS」；横幅副行：「EMPIEZA EL HORARIO DE INVIERNO · PÁGINA 2」。
- 注释框前缀统一 „Nota — "。

## 二、基线证明（先证同源，再改讲解）

- 核心构建目录原样复制后在 /tmp/nl-es-baseline 以 OUT 重定向运行，8 页 SVG 与已发行核心（files/weekly-report-nl-vol1/svg/）**逐字节相同（8/8 cmp 一致）**，方才动工。
- 注册表复跑：150 题，A2 42 · B1 76 · B2 32；分页 10/18/18/18/18/18/12/38；H 节范文 87 词（与核心 build3.log 一致）。
- ES 构建终跑：150 题，A2 42 · B1 76 · B2 32（与核心逐项相同）；全程零 FLOW OVERFLOW、零 HEAD TOO WIDE。

## 三、冻结核验（终版 SVG 文本节点多重集 diff，ES vs 核心，逐页）

- ES 8 页 SVG：CJK 字符 0、全角括号 0；构建代码中讲解方法统一命名 `expl()`，被禁的中间层词汇在纸面、KIT、代码中均出现 0 次。
- 核心独有而非 CJK 的字符串仅为：(a) P7 读者来信署名碎片（陈/Chen、北京/Beijing — 读者语言条目，见五）；(b) P8 答案行碎片 — 其注释已译为西班牙语且标点已半角化，属预期差异。
- 荷兰语正文（文章、题干、选项、图表数据、图注署名、P7 金句原文）逐字节冻结；P7 金句 8 句已逐句程序化核对：均能在其标注页码（Pagina 1/2/2/3/4/5/6/6）的文章原文中逐字找到。

## 四、键差异登记（注册表级 diff：恰 3 处键变更 + 2 处题干重瞄，余皆逐字不变）

| # | 核心键（中文） | ES 键 | 说明 |
|---|---|---|---|
| 137 | 周日时钟拨回：多睡一小时！ | El domingo se atrasa el reloj: ¡una hora más de sueño! | E 节翻译题：荷→母语，答案即西班牙语译文 |
| 138 | 你的手机和电脑会自动更改时间。 | Tu teléfono y tu ordenador cambian la hora solos. | 同上 |
| 150 | （开放题，范文如下） | (Pregunta abierta — modelo a continuación) | 键本身为讲解语，全角括号改半角 |

- #139 题干 «De Dutch Design Week is in Eindhoven. →» 改为 «La Dutch Design Week es en Eindhoven. →»（母语→荷语），键（荷兰语句）不变，注改为 „Ojo a la expresión de lugar: in Eindhoven"。
- #140 题干 «Zondag sliep ik een uur langer. →» 改为 «El domingo dormí una hora más. →»，键不变，注 „Perfectum: heb geslapen"。
- P8 注册表题型名 38 处改名（完形单选→Huecos 13 · 单选→Elección 12 · 造句→Frases 4 · 翻译→Traducción 4 · 词汇配对→Relacionar 4 · 写作→Redacción 1）——仅 P8 注册表题型（P1–P7 题面题型字串与核心同构保留，不影响计数与编号）。
- 全部 150 条答案注均已译为西班牙语；括号一律半角、注括号前留空格（本支 „n. key — note" 行式与 NL×FR 同构）。

## 五、家具与版式决定（全部以生产字体实测为准）

- P1 刊名下细目行 «SEMANARIO NEERLANDÉS · VOL.1 · DE KLOK GAAT TERUG · HERFSTVAKANTIE · ADE WORDT 30»：40pt 实测 1972px > 版心 1820px → 降至 36pt（1775px），与 NL×FR 的 36pt 解同构。
- P1 标示带 20pt 粗体实测 1116px ✓；页脚行一 14.5pt 实测 674px ✓。
- P7 读者信示例人格改瞄西班牙语读者：Lucía（马德里）— „«Hallo! Ik ben Lucía en ik leer Nederlands in Madrid. In oktober slaap ik één uur langer — net als jullie!» — Lucía (voorbeeldbrief van de redactie)"，与 NL×FR 的 Camille/Paris 同构（文档化读者语言条目）。
- P8 答案流版心：字号 13.5→13.0、行距 1.16→1.12、行间隔 0.5→0.4（与 NL×FR 同构，使较长的西语注释入版）；终跑答案流结束 y=2311 < 2552。
- 其余家具（栏目头、分组头、正文次行、引文条、预告条）逐条以 text_w 实测 ≤ 版宽；band 次行「¿Por qué los neerlandeses buscan el reloj en Google?」等均在界内。

## 六、在建缺陷与修复（构建内自查发现）

1. **P1 栏目标题溢界**：«DE WEEK IN CIJFERS · LA SEMANA EN CIFRAS» 23pt 实测 513px > 栏内限 398px，渲出后压过盒右界并与邻栏 #5 题面相撞（文字叠印审计实测）。改题为 «DE WEEK IN CIJFERS · EN CIFRAS»（380px）后复跑，叠印消失。
2. **P5 盒题溢界**：«ZO PLAN JE ADE · CONSEJOS PARA EL ADE» 484px > 398px → «ZO PLAN JE ADE · CONSEJOS»（336px）。
3. **P7 词盒题溢界**：«HET WOORD · PALABRA DE LA SEMANA» 445px > 412px（盒右界即版心右界 1885）→ «HET WOORD · PALABRA SEMANAL»（389px）。
   - 上三处均由新增的「盒题 vs 盒界」专项检查（标题检查脚本）测得，改措辞不改几何。
4. **P7 第三栏栈高**：西语诊所注（19pt）每注裹 2 行（核心/FR 为 1 行）、读者信注裹 3 行，栏栈末端达 1825.5px，将压金句分隔线（y=1698）。逐条缩短注文（含义与数字不变）后栏栈末端恰回核心原值 **1678.5**，金句区版面与核心逐行同构。

## 七、几何遮挡审计（出货门，自检轮）

- 工具：audit_nl_es.py（自 NL×FR 支复制）+ audit_texttext.py + 盒题检查（/tmp/nl-es-titlecheck.py）。模型：绘制序扫描、PIL 真字体量、线框按描边半宽外扩、墨带 = 基线 −0.88em…+0.30em。
- **正例对照先行验证**：合成页植入整行遮盖文本、线条压字、页脚带文本三缺陷 → COVER（100%）/LINEX/FOOTER 三类标记全数触发，方跑真页。盒题专项检查则以其在真页上实测出下述三处真实溢界完成自证（见六）。
- 终版结果：遮挡审计 **0 标记（8/8 页）**；盒题溢界 **0**；文字叠印仅 1 处——P1 黑体刊名墨带 vs 细目行，像素裁定：刊名实墨底 264（花饰至 298），细目行墨顶 303，净空 ≥4px，与核心及各支同构的量带伪影，非缺陷。
- **已知邻接像素复核（任务指定）**：P1「本周词」西语注（2 行）与 y=1853 横线——卡上像素测：注墨底 1845、横线行 ~1850–1853、无接触（核心原发版缺陷即此线压注，已于核心修复至 1853；ES 沿用该几何且注不被压）。

## 八、事实与星期核查（荷兰语正文，对 2026 真实日历逐项验）

- 2026-10-10 周六、10-17 周六、10-18 周日、10-19 周一、10-20 周二、10-21 周三、10-22 周四、10-24 周六、10-25 周日、11-01 周日（datetime 实算）。
- 与刊内claims逐项合：北区假期 10 月 10–18 日、中南区 10 月 17–25 日、北区周一（19 日）开学；冬时制夜 = 周六 10 月 24 → 周日 25 日 03:00→02:00；Trends 快照 = 周二 20 日；DDW 10 月 17–25 日共 9 天、家庭日 = 周六 24 日；Porto 周二、Sevilla 周三、Ajax 周四、顶级战周日 25 日；ADE 周三 21 日–周日 25 日；Robinson 周日 11 月 1 日 20:00 RTL 4。
- 图表算术：301+246=547；750−547=203；条长与数值成比例（与核心同冻）。

## 九、图片与署名

与核心完全相同（图片为冻结正文）：Westertoren（Wim van Rossem / Anefo, Nationaal Archief — CC0）、怀表（photo-nic.co.uk / Wikimedia Commons — CC0）、Kinderdijk 风车（Nationaal Archief / Wikimedia Commons — CC0）、秋林（Vovogov90 / Wikimedia Commons — CC0）、1912 国家队（Spaarnestad Photo / Wikimedia Commons — publiek domein）、运河船（W. Punt / Anefo, Nationaal Archief — CC0）。署名自 Commons API Artist 字段（核心阶段核定，冻结沿用）。

## 十、产物（files/weekly-report-nl-es/）

- svg/ ×8（p1-voorpagina … p8-toets）、cards/ ×8（1950×2700）。
- Lucerna-VOL1-ES.pdf（印刷版）：10,631,740 B · sha256 6c3a5c1d052817d781e43dfae9b1080339d7a68c0a50d02d0b84b23269a1ac78
- Lucerna-VOL1-ES-web.pdf（网络版，JPEG q85）：3,731,507 B（< 10 MB ✓） · sha256 5398b3bcbbf094db26975ce4d8ef6bccb6a0b4cadada0a6afca3c0eed18d8c8e
- WEEKLY-KIT.md（本文件）。

## 十一、校对状态

- 构建者全量自校：完成（逐页读卡 8/8、西语全串提取复读、答案 150 条逐条对题干/原文、P7 金句逐字核、日历逐项验如上）。
- 独立校对：**PASS（2026-10-21，完整一轮零问题）**。独立校对者（未参与构建）复核记录：
  1. **基线独立复跑**：将核心构建与 ES 构建各自复制到隔离目录、重定向 OUT 后整轮重跑——两套构建均逐字节复现各自已发行 SVG（8/8 + 8/8 cmp 一致），双构建日志零 FLOW OVERFLOW / 零 HEAD TOO WIDE；基线方法可信，发行文件确出自该构建代码、无事后手改。
  2. **冻结差分**：注册表级 diff（n/页/级全 150 项一致；分页 10/18/18/18/18/18/12/38；级别 A2 42 · B1 76 · B2 32 与核心全同）——键差异恰 3 处（#137、#138 译键改西语、#150 键为讲解语改西语），与登记表完全一致；题型名改名恰 38 处（#113–150：Huecos 13 · Elección 12 · Frases 4 · Traducción 4 · Relacionar 4 · Redacción 1），与 KIT §四一致。文本节点多重集逐页 diff：全部差异属讲解层/配对家具/登记项；#139/#140 题干已改瞄西语、荷兰语键逐字不变（P8 E 节实印核对）。登记表之外的荷兰语正文改动：零。
  3. **答案独立复核**：150 题逐题对题面/原文/图表重解——全对（含图表算术 301.000+246.000=547.000、750.000−547.000≈203.000、60.500÷6.600≈9、票价 19,50+19,50+32,50=71,50、范文实数 87 词）；#137/#138 西语译键经核为所印荷兰语题干（«Zondag gaat de klok terug: een uur langer slapen!» / «Je telefoon en je computer veranderen de tijd zelf.»）的忠实翻译。
  4. **西语讲解完整性**：终版 SVG 文本层 + 原始字节双扫——CJK 0、全角括号 0；150 条答案注中 141 条为西语新译、9 条为语言中立的荷兰语/数字注（与核心同文，属设计）；题干说明、词注、栏目标题逐页西语化；8 张整版图逐页目检，西语拼写/重音/性数配合无误。
  5. **编号与分级**：P8 答案行覆盖 1–150 无缺无重（#141–144 在配对节与答案区各印一次，与核心同构）；逐页级别徽章计数与核心逐页全同。
  6. **P7 金句**：8 句逐字连续摘录程序化核对——每句在整期恰出现 2 次（原文 + 金句栏），且均出现在所标页码页上（Pagina 1/2/2/3/4/5/6/6），页签全对。
  7. **星期/日期**：datetime 对 2026 真实日历逐项验——10/10 周六、10/17 周六、10/18 周日、10/19 周一、10/20 周二、10/21 周三、10/22 周四、10/24 周六、10/25 周日、11/1 周日，与刊内全部 claims（北区假期 10–18 日、周一复课；中南区 17–25 日；冬时制夜 10/24→25 日 03:00→02:00；Trends 快照周二 20 日；DDW 9 天、家庭日周六 24 日；球赛周二/三/四/周日；ADE 周三至周日；Robinson 周日 11/1 20:00）全合。
  8. **几何遮挡审计（校对者自写脚本自跑）**：脚本先经合成正例对照验证（COVER/LINEX/FOOTER/EDGE/BOXTITLE 五类缺陷全数触发，方跑真页）；模型 = 绘制序扫描 + PIL 生产字体实测 + 线框按描边半宽外扩 + 墨带 −0.88em…+0.30em。结果：COVER 0 · LINEX 0 · EDGE 0 · BOXTITLE 0（构建者缩短的 3 个盒题 P1 «DE WEEK IN CIJFERS · EN CIFRAS»、P5 «ZO PLAN JE ADE · CONSEJOS»、P7 «HET WOORD · PALABRA SEMANAL» 在渲染图上复核均在盒界内）。原始标记 30 个，全部裁定为量带伪影：16 个 FOOTER = 页脚家具本身（基线 2624，与核心同位、正文无一侵入）；1 个 TEXTX = P1 黑体刊名 vs 细目行（与核心同构，像素实墨不接触）；13 个 TEXTX = P8 答案行与其折行续行——逐对在渲染卡上做像素裁定，每对两行墨迹之间均有空白像素行分隔（最窄 #137/#139 亦有 2 行），无接触。**任务指定邻接复核**：P1 本周词西语注（2 行）vs y=1853 细线（#d8cfb4，x 65–1885）——像素实测：注第一行密墨止于 1845、'j' 下伸尖端至 1851，线占行 1852–1853 且该两行内文字黑墨像素 = 0，第二行墨起于 1861——线穿行间空隙、无接触、无划字，非缺陷（与核心修复后几何一致）。
  9. **图片与 PDF**：8 页图片载荷与核心逐字节相同（逐页哈希一致）；每图署名与所放图片对应（P1 Westertoren、P2 怀表、P3 Kinderdijk + 秋林、P4 1912 国家队、P5 运河船）。Web PDF 独立实测 3,731,507 B（< 10 MB）、sha256 5398b3bcbbf094db26975ce4d8ef6bccb6a0b4cadada0a6afca3c0eed18d8c8e，与 KIT 钉值一致；印刷版 10,631,740 B、sha256 6c3a5c1d…ac78 亦一致。
  10. **禁词扫描**：中间层术语（中文形与英文形）在报纸 SVG、本 KIT、构建代码中均为 0（«ezelsbruggetje» 为冻结荷兰语正文词汇，不计）。
  - 结论：构建者全部声明经独立复核属实；本版通过出厂门，可由主线入仓。本轮未动构建、未重渲染。
