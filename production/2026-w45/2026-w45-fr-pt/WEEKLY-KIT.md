# WEEKLY-KIT — Le Lucerna VOL.3 · FR × PT (W45)

**状态：builder-complete，NOT finalized。** 定稿由独立校对决定；本构建员不宣布上架、不投递 Discord、不入 GitHub 仓、不往主聊天发卡片/PDF。

## 1. 身份

- 配对：目标语 **法语（francês）** × 读者母语 **葡萄牙语（português）**，全称见每页页脚。
- 刊头：`Le Lucerna`（法语专属冠词 Le）。期号：VOL.3 · Nº 3。
- 刊期：2026 年 11 月 2 日（周一）至 11 月 8 日（周日），即 W45。
- 页数：8 页（4 的倍数）。目标语法语正文逐字冻结，讲解层全部为葡萄牙语。
- 构建树：`hidden_files/weekly-report-w45-fr-pt-build/`（transform.py 为唯一源头，见 §13）。

## 2. 计数（与核心逐项相等，核心渲染 SVG 实测）

- 习题总数：**150**，编号 1–150 连续。
- 页分布：**10 / 15 / 18 / 18 / 17 / 18 / 12 / 42**（P1–P8；注意 P2=15、P5=17、P8=42，为 FR 串；通用串对 FR 是错的）。
- 级别：A2 53 · B1 75 · B2 22。
- 题型（葡萄牙语登记标签）：Completar frases 49 · Escolha múltipla 26 · Associação 21 · Texto com lacunas 8 · Transformação 7 · Leitura de gráficos 6 · Verdadeiro ou falso 5 · Compreensão de leitura 5 · Tradução 5 · Completar diálogos 5 · Prática 8 · Correção de erros 4 · Redação 1。
- 范文：P8 MODÈLE 框范文逐字 = 核心，**86 词**（80–100 要求内），正文行与核心行逐行相同（仅刊头行改为双语 `MODÈLE · MODELO`）。
- 主题（核心实测）：决赛周末（Rolex Paris Masters，Nanterre，11 月 2–8 日；Peur sur le Parc，Plailly，末场夜场 11 月 7 日 19:00–01:00；Le Goût du Large，Port-en-Bessin，11 月 7–8 日，第 22 届）；11 月 2 日周一全法同步开学（无分区错峰）；冬令时第二周（法国 10 月 25 日切换，首周为 W44 内容）；万圣节 10 月 31 日、诸圣节 11 月 1 日、亡灵节 11 月 2 日为刚过去的报道；Pitchfork Paris 第 15 届，11 月 2–8 日；国民议会 2027 预算周按使命审议（11 月 3 日文化/媒体、4 日农业、5 日凝聚力/研究、6 日公共财政/经济；10 月 23 日社保收入部分 115–1 否决，参议院自 11 月 9 日起；日程明确标注为预定，无结果、无民调编造）。

## 3. 冻结门禁（freeze）

- 核心构建树未修改：未改动核心构建的 scratch 复现（`scratch/baseline/`，OUT 重定向）与核心交付 SVG **8/8 字节一致**（sha256，见构建树 `core-svg.sha`）；复现后核心 SVG 哈希与复现前记录一致，核心未动。
- `tools/freeze.py diff`（核心渲染 SVG vs 本版，r4）：每页新增 CJK 字符 **均为 0**，本版渲染文本节点 CJK **0**（P1 202→0、P2 244→0、P3 179→0、P4 197→0、P5 177→0、P6 198→0、P7 390→0、P8 1030→0，均为中文讲解层被葡萄牙语替换）。
- 无 CJK 的删除串逐项裁定（r4 diff 细查）：
  - P1 22 项：全部为 P1 头条段重排碎片（字号 24pt vs 核心 25pt 导致换行不同）；词集合证明：P1 全页词多重集比较，**核心独有词 = 0**（新增词全部为葡萄牙语家具/注释词）。
  - P3/P7 各 1 项 `）。`：中文注释换行残片（中文标点），非目标语。
  - P8 33 项：冷冻法语电池段/答案行重排碎片（E 题干加长、答案字号 14.5pt 导致换行不同）+ 已备案改向：`Traduisez` ×5（E1–E5 题干指令法→葡，对应新增 `Traduza` ×5；E1 法语引文保留，E2–E5 法语键保留在答案中）。
  - 除上述外，无任何法语目标串删除；法语词集合除 `Traduisez` 指令词外零损失（由 P8 双门逐键证明，见 §4）。
- 冻结串核对（核心渲染 SVG 实测为准，全部与核心一致，无改写）：
  - P4：`41e édition en 2026 (40e anniversaire)`；全版 grep `40e` 仅此 1 处（生日语境 `anniversaire` 句保留；编号 `40.`/`140–144.`、他版 `22e`/`15e` 不属 `40e` 串，无触动）。
  - P7 #4 保留 P4 辩论框逐字 comparatif `plus excitante ou plus frustrante ?`；#8 为 P5 逐字 `Les jeunes créateurs y rencontrent leur public, en vrai.` + Q106 错误 `rencontre`、key `rencontrent`。
  - P6 同步为 `Ce calendrier peut encore bouger.`（P6 深读、P6 观点框、P7 B2 教学栏三处一致）。
  - Q120 题干 `Si j'étais libre dimanche, j'___ à Nanterre.`、选项 A. irai / B. irais / C. vais、key B、P8 注同步（si + imparfait → conditionnel + elision j'）；Q119/Q121 不动（题干与 key 均与核心一致）。

## 4. P8 双门（FR 族专属，BINDING）

- 门 ① plain `tools/p8.py`（sha256 `96fc2cfe51d3dcfa44cc87ec63052b98b27462703d8226815046eccc0ca9`，显式 `--core-p8` / `--edition-p8`，`--total 150`）：核心 noted **97**，分版 noted **97**，状态 **CLEAN**，missing=[]，extra_count=0，uncertain=[]，keydiff=[135, 150]。
  - 注意：`--core-dir/--edition-dir --target fr` 调用形式曾给出 92/92 + keydiff [135, 145]（工具路径差异）；显式路径形式与 `extract --json` 的 97 项集合逐项一致，且与 fr-de/fr-en 的同工具结论一致，故以显式路径形式为准，记此差异备查。
- 门 ② `hidden_files/w45/p8-fr-gap-fix/keycompare.py`（复用 p8.py extract --json 输出，`--total 150`）：两侧各 150 键，mismatch **仅 [135, 150]**，两项在两侧均为 noted 项且均为已备案改向（§6），**裸键 mismatch 0**。
- 通过条件满足：plain ∈ {CLEAN} 且零裸键 mismatch。plain 不单用（其对裸键盲区已知）。
- 核心 noted 基线独立核对：核心渲染 `p8.py extract --json` 得 noted 97 个，编号 [1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106, 107, 108, 109–150]；裸键补集 53 个。
- P8 注释语言纯度：全 8 页重扫，CJK 0、全角括号 0；P8 注释全部为葡萄牙语讲解（含合法的法语被释词与语法术语，如 `lire un programme = ler um programa`、`futur proche`、`passé composé`）；德语/西班牙语残留词 0（逐条目视 P8 注释清单）。

## 5. 几何门禁

- canonical `tools/occlusion_audit.py`：自检 6 类 planted 全部命中、干净对照静默；**分版 0 flags，核心 0 flags，NEW vs 核心 0**（r4 终版）。
- 补充扫描（`hidden_files/weekly-report-w45-fr-pt-build/scans.py`，venv PIL）：
  - 全页右缘扫描（ADVANCE 法，限 1885）：仅 3 项超限，全部为核心同行同字（P8 F 配对右侧行 b/d/e，最大 x1=1899.5，仍在内框线 1910 以内）——冻结法语重排继承，非分版缺陷；与核心同扫描逐项相同。
  - 全页框线扫描：**0 命中**。
  - 同基线行检查（P1 顶栏 y=92、徽记 y=574、各页页脚 y=2624）：**0 重叠**。另核 P1 深色横幅双行（478/522）：法语左段末端约 1007/1030，葡萄牙语右段起端 1273.7/1208.5，无重叠。
  - P6 图表标签基线锚定墨迹覆盖（getmetrics 法，禁用 getbbox）：**0.0%**（<30% 通过；图表为文字表，框线在文字之前绘制）。
  - 行首检查：4 项行首 `:`，全部与核心同页同坐标同文本逐字节相同（冻结法语换行所致，P3 789.65 / P4 837.12 / P5 430.65 / P7 428.1）；**葡萄牙语自有行首违规 0**。另查行中切词：法语栏 wrap 按词整体换行，无连字符切词节点（除冻结法语固有形式外）；P8 答案行换行均为词间换行。
- 流末端（末基线/墨迹底为 SVG 实测，流光标为构建日志）：
  - P1 headline 栏光标 1537（限 1812）；P1 hiver 末基线 2253.6 = 核心值，墨迹底约 2260.3（quiz 规则线 2312，余 51.7px；光标 2298 为尾部间隙假象）；P1 quiz 末基线 2479.9 = 核心值（限 2540）。
  - P2 feature 642，习题 2365；ET VOUS 框底 1546.6（见 §12 偏差 9；日期规则线 1558，余 11.4px）。
  - P3 正文 813；P4 正文 1246，微习题 2154；P5 正文末基线 2486.1（核心 2456.4），墨迹底约 2493.3（限 2540，余 46.7px；正文流仅占第 0–1 栏，y>2400 节点全部在 x<989 内，未溢入第 3 栏；第 3 栏较核心多 2 行均为葡萄牙语本地化换行，遮挡审计 0 旗）。
  - P6 深读 1049，习题末基线 2505.1（核心 2504.5），墨迹底约 2511.7（页脚规则线 2580，余 68.3px；光标 2557 为尾部间隙假象，与核心同口径）；观点栏 1256（距图表顶 1330 有 74px），微习题 2050。
  - P7：A2 954，B1 1053，B2 988，工具箱 1008，短语栏 1574（限 1830），诊所 2140（限 2268）；读者框末基线 2233.3 = 核心值，墨迹底约 2239.2（框底 2258，余 18.8px）；**预告末基线 2494.0，墨迹底约 2500.0 < 2540（余 40px）**。
  - P8：battery 末基线 1446.4（核心 1455.8），墨迹底约 1452.4（写作条规则线 1486，余 33.6px；光标 1487 为尾部间隙假象）；答案流末栏光标 2298（限 2545）；**答案最大基线 2544.0（核心 2539.2），墨迹底约 2549.1，距页脚规则线 2580 有 30.9px，遮挡审计 FOOTER 0 旗**——2540 不是 canonical 审计限值（核心自身墨迹底亦为 2543.8），按口径一致 + 页脚间隙 + FOOTER 0 旗标 adjudicate（fr-de 前例同法）；光标（末栏）小于最大基线（满栏）是多栏流的正常现象，非矛盾。

## 6. P8 改向与显式注释集（W43 先例方法）

- 注释规则：葡萄牙语注释长于核心 ≤10 字规则，改用显式 `PRINT_NOTES` 集合（与 W43 同配对版同法）；全角括号一律改为半角。
- 仅翻译项改向：E1（#135）翻转为法→葡——题干 `Traduza para o português: « Lire un programme, c'est déjà comprendre la France. »`，键 `Ler um programa já é compreender a França.`，注释 `lire un programme = ler um programa`。E2–E5 题干改为葡萄牙语，法语键不变（E2 `Ele corre mais rápido que o irmão.` / E3 `Os alunos estão de férias desde 17 de outubro.` / E4 `Hoje à noite, vamos preparar as nossas mochilas.` / E5 `Ainda não se conhecem os finalistas.`）。写作项（#150）键 → `Questão aberta — os pontos estão no quadro de escrita e o modelo está no quadro MODÈLE desta página`，注释 `Avaliação por pontos`。P8 葡萄牙语写作说明追加 `Os melhores textos sairão no VOL.4 (página 7, « Le courrier des lecteurs »).`
- 改向逐项印刷核实（非照抄他版）：P8 电池区 E1–E5 题干与答案区 #135/#150 印刷行均已从本版 P8 SVG 实测确认（见 §3 Q120 同法核对）。

## 7. gloss 分布（渲染 · 切分逐项计数，核心 = 分版）

口径（README #21）：gloss() 调用串按 `·` 本身切分（非 ` · `）；Nota 桥接串先去前缀 `Nota — ` 再切分（否则前缀自带分隔符多计 1 项）；词表按 mots 列表字面计数。三口径分开记账，勿混算。

| 页 | gloss() 项 | Nota 项（去前缀后切分） | 词表项 |
|---|---|---|---|
| P1 | 7 | 0 | 0 |
| P2 | 6 | 3 | 0 |
| P3 | 6 | 0 | 10 |
| P4 | 7 | 3 | 8 |
| P5 | 6 | 0 | 8 |
| P6 | 6 | 3 | 0 |
| P7 | 0 | 0 | 0 |
| P8 | 0 | 0 | 0 |
| 合计 | 38 | 9 | 26 |

## 8. P7（词框、金句、读者角）

- 词框目标语定义句逐字冻结，仅 gloss 行本地化（P7 三级教学栏与工具箱三句的法语句全部保留；本地化定义句即冻结失败——本版无此情况）。
- 金句 8 句均为本期正文逐字连续摘录、页签正确，联合文本计数（8 页全文拼接，空白归一）与核心逐项相等：
  1. `Le lundi 2 novembre, on reprend les cours.`（page 2）×5
  2. `On ne connaît pas encore les finalistes.`（page 1）×3
  3. `Les cimetières se sont remplis de chrysanthèmes.`（page 3）×1
  4. `Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ?`（page 4，P4 辩论框逐字 comparatif）×5
  5. `Le festival se promène dans Paris.`（page 5）×1
  6. `Ce calendrier peut encore bouger.`（page 6；P6 同步形式）×3
  7. `Ce week-end, tout se joue.`（page 1）×1
  8. `Les jeunes créateurs y rencontrent leur public, en vrai.`（page 5；Q106 改写：error `rencontre`，key `rencontrent`）×3
- 每句均已在所标源文章页实测命中（句末标点归一化核对：正文中 #2/#3/#5/#7 句后接 ` — `/` :`，P7 表格将其规范为独立句，与核心同法）。
- 教学栏 / 工具箱重复 #1/#2/#4/#6 为 KIT 设计，非缺陷（“2×” = 源文章 + P7 表格对）。
- 读者角（LE COURRIER DES LECTEURS · CARTAS DOS LEITORES）零编造三件套（均印在 P7 版面上）：
  - 标注的编辑示例：`Exemple de la rédaction (ce texte n'est pas une lettre de lecteur)`（法语示例段逐字保留）+ 葡萄牙语点评 `Xiao Mo comenta (texto-exemplo): …`；
  - 三事实披露（葡萄牙语披露句 + 法语编辑注双语）：截至付印未收到任何读者来信、未收到 VOL.2 第 8 版投稿作文（W44 未出刊）、两者均延至 VOL.4；
  - 明确的公开征集祈使句（逐字）：`Enviem-nos cartas e as melhores redações da página 8 para o VOL.4!`——字面同时覆盖来信与最佳 P8 文本；同页披露句把真实文本延期至 VOL.4，P8 写作条把最佳文本指向 VOL.4 第 7 页，预告点名 `e as vossas cartas, finalmente!`——组合满足来信与最佳 P8 作文两项，VOL.4 必须兑现。
- 预告（LA SEMAINE PROCHAINE · PRÓXIMA SEMANA · VOL.4）：法语原文保留；葡萄牙语 `Na próxima semana: o Senado e o orçamento da Segurança Social, 11 de novembro, Dia do Armistício, feira de Dieppe — e as vossas cartas, finalmente!`

## 9. FR 族已裁定事实（执行结果）

- 核心渲染 SVG 实测：41e 形式、P7 #4/#8、P6 同步、Q120 均已为正确形式（见 §3），本版未改写任何冻结法语串。
- P7 “2×”指原文 + P7 表格对（教学栏/工具箱重复 #1/#2/#4/#6 是 KIT 设计，非缺陷）。

## 10. 家具三方对照（W43 同配对版 优先于 README #20 泛化）

- 徽记：(975, 574)，22pt BRICK 粗体，居中，与 W43 字符串逐字相同：`TEXTOS EM FRANCÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA`（实测宽 1200.3px）。README #20 的 (975, 574) 22pt 描述的是法语作目标时的情形，与本版一致，无冲突。
- P1 顶栏（y=92 三段）：左 `VOL. 3 · Nº 3`（W43：VOL. 2 · Nº 2）；中 `HEBDOMADAIRE EN FRANÇAIS · TODA SEMANA · O FRANCÊS QUE OS FRANCESES LEEM`（与 W43 相同）；右 `SEMAINE DU 2 AU 8 NOVEMBRE 2026`（W43：19–25 OCTOBRE 2026）。
- 刊名 262（178pt）、副标题 330（46pt）`SEMANÁRIO EM FRANCÊS · VOL.3 · FIM DE SEMANA DECISIVO`（W43：VOL.2 · OUTONO E FESTAS；实测宽 1412.0px，适配）、标语 372 法语原文与 W43 相同、暗带 478/522（法语头条为本周内容，葡萄牙语右侧为本周短语）、规则线与暗带几何与 W43 相同。
- 页脚（每页，y=2624）：`Le Lucerna · SEMANÁRIO FRANCÊS VOL.3 · TEXTOS EM FRANCÊS · EXPLICAÇÕES EM PORTUGUÊS` + `Página N de 8`（W43 模板，VOL 号更新）。
- 短双语栏头（与 W43 同）：PALAVRAS、O DEBATE、TREINO、NÍVEL BÁSICO / INTERMEDIÁRIO / DESAFIO、PARA LEVAR（工具箱，W43 偏差：FERRAMENTAS 超宽）、CLÍNICA、LER O CALENDÁRIO、DATAS、SUMÁRIO、EM RESUMO、QUIZ RELÂMPAGO、VOCABULÁRIO（P6 LES MOTS 流栏头与 P8 F 栏头，W43 同法）；gloss 前缀 `Nota — `；P8 分隔 `— Página {n} —`；cloze 标签 `Opções:`。
- 暗带右侧双行（右对齐于 1855）：`SEGUNDA, VOLTA ÀS AULAS · EM TODA A FRANÇA`（起端 1273.7）/ `COMEÇO DO MASTERS · ABERTURA DO FESTIVAL · VER PÁGINA 2`（起端 1208.5），与法语左段无重叠。

## 11. 图片（仅明确公有领域，credit 取 Commons API Artist 字段原文）

| 页 | 图 | 放置（x, y, w×h） | credit（与核心逐字相同） | payload 哈希口径 |
|---|---|---|---|---|
| P1 | atget-paris.jpg | 65, 1874, 896×320 | Eugène Atget (1857-1927), photographie, domaine public | base64 文本 sha256 `ff20bc2bd2654cdc075f7e09bcb5a96622650c7cb5921fe07384703067fa8e5d`；解码 JPEG sha256 `f3705af28f175ce48d8abad95944accb7aacc45d6a8a50c47b24af5c5144595f`，334674 字节 |
| P2 | hiroshige-maple.jpg | 1451, 200, 434×480 | Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA | base64 文本 sha256 `6918cb8bbe4b4bec2d6dd9bafb1636901ed2a46f9df8e49566749e404d1664ae`；解码 JPEG sha256 `5b772facb5db886c18fa96c05b9c8fb1a459eaaff931a4a8c121896edf970ee2`，646242 字节 |
| P3 | chrysanthemum-blanco.jpg | 1451, 200, 434×540 | Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public | base64 文本 sha256 `bfaadf5b6b912416f770c1bf579c3467e47c662efd130b5656292bb86171eca9`；解码 JPEG sha256 `be071fdae81a71b48d76383bd33147371968f44e37eef4312102d52dea6d0c94`，142340 字节 |

（三图两种口径全值在核心与本版 SVG 内嵌 payload 中逐字节相同——三组哈希核心 = 本版；三张图均已核实确已放置，解码字节数与资产文件一致；全值另存构建树 `image-hashes-full.txt`。）

## 12. W43 偏差清单（预期偏差，仅此清单）

1. VOL.3 vs VOL.2、刊期 11 月 2–8 日 vs 10 月 19–25 日、副标题主题 FIM DE SEMANA DECISIVO vs OUTONO E FESTAS、暗带右侧本周短语（均为刊期内容更新）。
2. P8 答案字号 14.5pt vs W43/核心 15.5pt（葡萄牙语注释更长，答案流适配；fr-de 同法）。
3. P8 battery 习题间距 6 vs 11，F 配对间距 6 vs 14，电池段字号 21→20（cloze/阅读/对话三段；E 题干葡语化致电池段 +116px 的适配；fr-de 同法）。
4. P1 头条段字号 24pt/行高 1.45 vs 核心 25pt/1.52（葡萄牙语 gloss 增长适配；法语文本字节不变，仅呈现；fr-de 同法）。
5. P1 gloss 缩短为短释义（7 项全保留，行数 7→5，与核心行数持平）。
6. P2 ET VOUS 葡萄牙语段缩短为 2 行定稿 `Segunda de manhã: onde estavam? Que livro leram? Duas frases para a redação!`（框底回归核心值附近，见偏差 9）。
7. P7 读者角为编辑示例 + 延期披露（继承 VOL.3 核心的诚实处理；W43 为真实来信——差异来自核心内容，非分版自选）+ 新增征集祈使句（SOP 门禁要求，见 §8）。
8. 翻译改向方法同 W43 先例，项号不同（本版 #135/#150；W43 为 #132/#145）。
9. P2 ET VOUS 框底 1546.6 vs 核心 1538.6（+8px：葡萄牙语末行 `ç` 下伸笔画需离框底线，见 r4 修复；日期规则线 1558 仍余 11.4px）。
10. P6 读日程栏头 24pt（vs 其余 25pt 栏头）+ 后缀缩短为 `CALENDÁRIO`（25pt 宽 525.8 > 434 栏宽；24pt 宽 430.5 适配）。
11. P8 电池栏头后缀缩短：A `LACUNAS`、B `ESCOLHA`、C `COMPREENSÃO`（24pt 全式均 > 434 栏宽；D/E/F/G 全式适配，保留全式）。
12. P1/P3/P5 栏题缩短：`LES DATES · FIM DE SEMANA`（DECISIVO 溢出栏框）、`DATES À RETENIR · DATAS`、`PARIS CREATOR WEEK · CRIADORES`、`DANS CE NUMÉRO · SUMÁRIO`（W43 同形）；P1 日程注 `Resultados no sábado à noite e no domingo.`、P6 日程注 `Este calendário é um programa previsto; os resultados ainda não saíram.`（p.text 不换行，葡语全式溢出页边/栏框，缩短后适配）。
13. P7 栏头短式、P8 分隔、半角括号、PRINT_NOTES 方法与 W43 相同，无偏差。
14. 其余家具、规则线、暗带、页脚模板与 W43 逐项相同。

## 13. 工具链与可复现性

- 单源头：`hidden_files/weekly-report-w45-fr-pt-build/transform.py`（357 项：主 340 + 修复轮 17 = r2 10 + r3 5 + r4 2）；每轮修复先存全量 pre-fix SHA256 基线（`pre-fix-hashes-r1-full.txt` / `pre-fix-hashes-r2-full.txt` / `pre-fix-hashes-r3-full.txt`），修复只进 transform.py；r4 交付前以核心源码新拷贝 + transform.py 在 scratch（`scratch/repro/`）重放，6 个源码文件与构建树逐字节一致（`cmp` 全 IDENTICAL）——transform.py 单独复现已交付纸面。
- 渲染：`run.py` 单进程 driver（content12 → content34 → content56 → content7 → content8，共享 bslib4 登记）；`render.py` 卡片 PNG @1950（cairosvg）、印刷 PDF（svg2pdf + pypdf）、网络 PDF（整卡 JPEG quality 72，核心配方；临时 JPEG 留构建树内，事后删除）。
- 解释器与 PIL：run.py 与 render.py 均用 `tools/venv/bin/python`，Python 3.12.3，Pillow 13.0.0；审计测量同 venv PIL。系统 python3（同为 3.12.3，Pillow 10.2.0）无 cairosvg，故 render.py 必须用 venv；run.py 亦用 venv（基线 8/8 字节复现即以此解释器测得）。
- 确定性证明：r4 渲染日志零 FLOW OVERFLOW、零 HEAD TOO WIDE；核心构建树与 W43 目录未改动；未碰 weekly-git、未建 cron、未发 Discord、未往主聊天发卡片/PDF。
- 校对轮次：r1（初版，P1 溢出/P2 重叠/P8 溢出/4 栏头超宽）→ r2（修复，残 5 处溢出）→ r3（修复，残 2 处 BOXTITLE）→ r4（终版，几何 0 旗）；每轮变更页：r1→r2 为 P1/P2/P6/P8，r2→r3 为 P1/P3/P5/P6，r3→r4 为 P1/P2；P4/P7 自 r1 起未变。

## 14. 交付文件

- `svg/` ×8，`cards/` ×8（1950×2700），`lucerna-fr-pt-print.pdf`（印刷）9,749,607 字节，sha256 `7d87195cf9b2bfccf7dafc9321edc742d39ec0a7d6f7e55429dd0e9b1abbf152`；`lucerna-fr-pt-web.pdf`（网络）5,103,001 字节，sha256 `3321a487ae5e55b28fe80dd411e7d629b9771c213c3382648f90acac4bd5f329`（完整值见 §15）。
- `WEEKLY-KIT.md`（本文件），`ABSTRACT.txt`（葡萄牙语单行，无 ASCII 双引号）。

## 15. 终版哈希（round-4 交付）

```
lucerna-fr-pt-print.pdf      7d87195cf9b2bfccf7dafc9321edc742d39ec0a7d6f7e55429dd0e9b1abbf152
lucerna-fr-pt-web.pdf        3321a487ae5e55b28fe80dd411e7d629b9771c213c3382648f90acac4bd5f329
svg/p1-une.svg               87d7ec8f25b7d636817cc67e591f23fbac4122d45cbf3ea0aeb13a859487654d
svg/p2-vie.svg               1ab15c6d2ba4b265aeff62efb63f40f94e72b1ab0839f363625d71b45a45bf06
svg/p3-culture.svg           3a9f001074cdbcbf1e2b2a97dac059351abfb33422afff22c0488a386fc34d0c
svg/p4-sport.svg             e05b7dd4327bd6954e1aead30bcacbfdf14f730fe87e4355dc8f2dc5c5679bf9
svg/p5-jeunesse.svg          545a53ab061028411c4aa18d76c031a8165d75aebd6d0d08103c72ce2be8da20
svg/p6-politique.svg         20cc6921571713952a54337aad016b607545bc08aa2f9caad1b01fce4ee93f26
svg/p7-langue.svg            d086a953a4278c8e190494fb0dac8e2cf0771836364688f789d86c89f39e760a
svg/p8-exercices.svg         386feaf9be78d4fc654b4e7b53928d5e8df445e6f2d135df5c07d10c9654628d
cards/p1-une.png             ab62402650ce8c57b4c78f74f444de62871d4d373bcca820ebc399cd0fe6308f
cards/p2-vie.png             5f421db11f91ea51db1957df94ad75ae9479c02b2800ce329c04b319e02729c9
cards/p3-culture.png         237d3f446ae1b028ffc2fca4360c73999269eae5a784b130c3bce3f008468abf
cards/p4-sport.png           b8b67f8edb07b70dbd90f24ff6e06859382bc5cc33c7d3a08a9824fa9419da75
cards/p5-jeunesse.png        34d272eccbf80cec88883f9c29be5d76576763af06416eadaad8177983699174
cards/p6-politique.png       bb4546033aab525941ebac1cead7a16ac6eaf570fcf3b778c0f6ec8f5ae6986f
cards/p7-langue.png          947c9e56a9493985946182ce3a07647d3568c1b94281ebe44bd0c40e7c03f6a
cards/p8-exercices.png       67922cdedf692b5f466aebb504754b260a68a8830c85f6017c825a2f28e5778e
```

## 16. ABSTRACT 原文

> Le Lucerna VOL.3, semana de 2 a 8 de novembro de 2026: semanário em francês para leitores de língua portuguesa — fim de semana decisivo com o Rolex Paris Masters em Nanterre, Peur sur le Parc em Plailly e Le Goût du Large em Port-en-Bessin, volta às aulas a 2 de novembro, Halloween e Toussaint, Pitchfork Paris e o orçamento 2027 na Assembleia Nacional, com 150 exercícios do A2 ao B2, vocabulário, gramática e texto-modelo. Aprender francês com notícias reais: fim de semana decisivo, horário de inverno e festas francesas.

## 17. 终验证（r4 交付后，KIT-only 追加，不触及渲染）

- 目视：建造者已逐页目视全部 8 张卡（P1–P8 全幅）。结论：无重叠、无切字、无框外溢出、无页脚碰撞；P2 末栏 `D · LES MOTS` 栏头居栏底为核心同构（核心同页同栏亦有此栏头，y=2468；本版 y=2497，系葡语说明行加长所致，非缺陷）；P8 答案区末行与页脚规则线间隙清晰。
- 网页版 PDF 逐页渲染比对（fr-en 噪声教训）：`pdfinfo` 确认 8 页；`pdfimages -list` 确认每页内嵌 JPEG 均为 1950×2700、150ppi，与卡片 1:1，无缩放；`pdftoppm -r 150` 渲染 8 页与卡片逐像素比对（PIL ImageChops，零位移最优，±1px 位移均使均值恶化，排除错位）：各页平均绝对差 5.0–8.6（P8 最高 8.6，系答案区小字号密集所致），>30 差值像素占比 6.6–12.1%；P1 大差值像素 87.2% 位于深色文字 2px 邻域内，属 JPEG quality 72 编码振铃，非结构噪声；100% 放大裁剪目视（卡片 vs 网页渲染）文字、版式逐字相同，无斑点、无块状失真、无内容缺失。结论：**无噪声页，网页版门通过**（质量参数本身不阻塞，流 = 卡片编码才是门；本版流即卡片）。
- 交付后校验：KIT 与 ABSTRACT.txt 写入后，SVG/卡片/PDF 哈希与 §15 终版哈希逐项一致（未重新渲染）。

## 18. 未决观察（非阻塞，交独立校对裁定）

1. P8 答案最大基线 2544.0 / 墨迹底约 2549.1，名义限 2540 仅差 4.0/9.1px；但与核心同口径值对照（核心 2539.2/2543.8），距页脚规则线 2580 有 30.9px，遮挡审计 FOOTER 0 旗——多栏流满栏结构使然，非分版缺陷。
2. P8 F 配对右侧 3 行右缘超限（最大 1899.5）与 P3/P4/P5/P7 行首 `:` 4 项，全部为核心同行同字继承；葡萄牙语自有项 0。
3. P1 hiver 末基线 2253.6、P6 习题末基线 2505.1 为核心继承的紧贴值（光标值 2298/2557 为尾部间隙假象，墨迹底才是实测末端）；P6 观点栏末 1256 为本版自有值（核心重跑光标 1225；几何合格，距图表顶 1330 有 74px），遮挡审计 0 旗。
4. P5 正文流止于第 1 栏（末基线 2486.1，墨迹底约 2493.3 < 2540）；第 3 栏较核心多 2 行（y=1478 `o público ao vivo.`、y=1929 `música ouvem para aprender francês?`）均为葡萄牙语本地化换行，非正文溢出，遮挡审计 0 旗。
5. P8 `--target fr` 调用形式与显式路径形式的注记计数差异（92 vs 97，见 §4）——工具路径备查，不影响显式路径 + extract + keycompare 三方一致的门结论。
6. 本版未做项：独立校对、GitHub 入库、Discord 投递（投递暂停令仍有效，须主线另行决定）。
