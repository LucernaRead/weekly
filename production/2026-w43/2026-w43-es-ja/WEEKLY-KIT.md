# WEEKLY-KIT — ES×JA（西班牙语正文 · 日语讲解）W43 VOL.1

- 版次：La Lucerna · スペイン語週刊 VOL.1（W43, 2026-10-19–25），目标语 = 西班牙语，讲解 = 日语（日本語読者向け）。
- 状态：**PASS**（独立校对一轮零问题，见 §7；未入仓、未发 Discord）。
- 核心：files/weekly-report-es-vol1（西语核心 VOL.1，150 题）。build 副本：hidden_files/weekly-report-es-ja-build（源：hidden_files/weekly-report-es-build 逐字节复制后变换）。
- 产物（本目录）：svg ×8、cards ×8、印刷 PDF、网页 PDF。
  - La-Lucerna-VOL1-JA.pdf：11,775,499 B，sha256 `53aef2d8d57fe87f1c0b1c07e82fb86f536ba707fd9fef60ce9e7081f4375004`（D5 重建，2026-11-13；见末节 D5 记录）
  - La-Lucerna-VOL1-JA-web.pdf：3,449,690 B（<10 MB），sha256 `653e235f39a0768037ff5aa73b8a16e87780b0f6c78098713fcb2f0a44ed27c3`（D5 重建，2026-11-13；见末节 D5 记录）
  - SVG sha256（前 16）：p1 166077532e3a9674 · p2 22174197f2e64aa6 · p3 e36de2350ff7341e · p4 a433dbcd09247e53 · p5 3cb3e84027668f88 · p6 31bbd2e111af8fe2 · p7 2e5d1462c5c834d9 · p8 759ee6f3732ee102

## §1 变换方法（与 JA 列同法）

- AST 值映射（一遍、计数断言）：核心 build 全部 CJK 字符串常量 488 个节点 / 268 个不同值——映射 252 值（472 节点）、声明不变 12 值（12 节点，见 §6）、定点编辑消费 4 值（页脚旧形 1 + 页码 f-string 碎片 3）。变换脚本在 build 的 scratch/transform_ja.py（含核心原调用串 ".bridge(" 作为搜索模式——仅限 scratch，paper/KIT/operative code 中该术语为 0）。
- 定点编辑：OUT 改道 es-vol1→es-ja（content×5 + render.py）；PDF 名 La-Lucerna-VOL1-JA(.pdf/-web.pdf)；bslib4 `def bridge(`→`def expl(` + 调用点 `.bridge(`→`.expl(` ×20；P1 标语行→徽章行；P8 分隔 f-string 改日语形（见 §3）。
- **svglib 换日语核心版**（JA 列硬性标准）：md5 `d73e23b365676c3618d7e060b835eb4d`（自 hidden_files/weekly-report-ja-build 取件、先验 md5 后整件替换；含 JP 字面选择 + kinsoku 追い出し + SEAM_SLACK=28）。行首禁则逐行扫描 = 0（闭括号/标点/小假名/长音符起行全无）。

## §2 题量与注册表（实测）

- 总量 150 = A2 52 · B1 70 · B2 28；分页 10/18/18/18/18/18/12/38（与核心逐项同）。
- 题型（日语标签）：文の完成 48 · 選択問題 47 · 単語のペア 12 · 正誤判断 8 · 文を作る 7 · 文の書き換え 10 · 穴埋め選択 13 · 翻訳 4 · 作文 1。
- 注册表 AST 全量比对（.ex/.match_set 字面调用展开 150 条）：level 差 0、opts/right 差 0、body 差恰 2、key 差恰 3、note 差 136（核心侧全为中文注；14 条语言中立注逐字节同）。

### 键差异登记表（全部合法类别）

| # | 类别 | 核心 | 本版 |
|---|------|------|------|
| 137 | 翻译题键 | 周日我们多睡一个小时。 | 日曜日は1時間長く眠れます。 |
| 138 | 翻译题键 | 周一在九个自治区是假日。 | 月曜日は9つの自治州で祝日です。 |
| 139 | 翻译题题干改向 | 国家德比周日晚九点开踢。→ ___ | クラシコは日曜の夜9時にキックオフ。→ ___ |
| 140 | 翻译题题干改向 | 每个图表都必须标明来源。→ ___ | どのグラフにも出典を明記しなければなりません。→ ___ |
| 150 | 作文装置键 | （开放题，范文如下） | （自由記述 — 模範文は以下） |

- p8.py compare：**CLEAN**（核心印刷注集 150 = 本版 150，missing/extra/uncertain 全空；ES 核心 P8 印全 150 注，extract 实测同集）。p8.py 行级 keydiff 14 项 = 上表 #137/#138（真键变）+ 12 项提取构成伪影（#12/#14/#16/#17/#57/#73/#75/#83/#95/#96/#101/#105：提取串为「key — 注首段」，破折号前键部逐字节同、差异全在已译注内；以注册表比对为准，README #13）。

## §3 家具（JA 列定式逐项，目标语名 スペイン語）

- P1 徽章（masthead 标语位，19.5pt 粗体 BRICK）：`スペイン語テキスト · 日本語の解説 — 日本語読者のための版`
- P1 通栏题花：`ス ペ イ ン 語 週 刊 · VOL.1 · EL RELOJ · EL CLÁSICO · LA F1`
- P1 顶栏中：`CADA SEMANA EN ESPAÑOL · 毎週一号 · スペイン人が読んでいるスペイン語を読む`
- 页脚左（每页）：`La Lucerna · スペイン語週刊 VOL.1 · 本文はスペイン語 · 解説は日本語`
- 页脚右（每页）：`N ページ（全 8 ページ）`
- gloss 前缀：`解説 — `
- P1 词条行（expl 首行带前缀形）：`解説 — la madrugada 未明 · atrasar el reloj 時計を戻す · empatados 同点 · la tormenta 嵐。`
- P8 页眉左：`RESPUESTAS · 全解答と解説（1–8ページ）`；右注：`各問に日本語の解説つき · ✓ は模範文のある問題`；分隔：`— N ページ —`
- 章节带头（西语原题 · 日语短题）：`VIDA · 暮らし` / `CULTURA · 文化`（共有汉字，与核心同形）/ `DEPORTE · スポーツ` / `JUVENTUD · 若者` / `A FONDO · 深掘り` / `LENGUA · ことば`
- 题型标签：選択問題 · 文の完成 · 空所補充 · 文の書き換え · 書きかえ · 文を作る · 正誤判断 · 正誤 · 翻訳 · 単語のペア · 穴埋め選択 · 作文；配对指令 `語と意味を結ぶ`
- 目标语名表（本列条目）：西班牙语 = スペイン語。

## §4 机械门结果（全用 tools/ 定版工具）

- freeze.py baseline：开工前 8/8 逐字节复现核心；**收尾复核 8/8 未变**（p1 41f0d53f · p2 42f8603d · p3 ba31dbb0 · p4 524ad07b · p5 bf2a0790 · p6 b99e70a0 · p7 26432db2 · p8 229b1b13，与开工哈希逐项同）。
- freeze.py diff 分账闭合：源级非 CJK 常量增删 = 声明定点集全等（OUT 路径 ×6、PDF 名 ×2、P1 西语标语→徽章、P8 分隔碎片）；行级非 CJK 增删逐项归因——删除侧仅 P1 标语行 + P8 分隔 ×8；p5/p6 词库行同词重排（词多重集同、西语未动）；p7 混合行碎片 1。**西语正文多重集与核心全等、移除侧非讲解项 = 0**；added CJK 共 3,005 字，全为日语讲解层新增（--strict-cjk 的 FAIL 为 ja 原生版预期项，以分账为准）。
- occlusion_audit.py（自检先行 OK）：本版 2 旗，与核心自身 2 旗逐字同位同几何（p1 LINEX 连休注行 vs 分隔线——核心中文注同位同掠，核心出货裁定；p5 BOXTITLE «Murcia y Canarias.» 冻结西语行 0.7px，核心同旗）。**新增旗 = 0**。
- 同行墨迹扫描（README #10）：本版 0（核心 0）。行首禁则扫描：0。
- 图表元素级检查（README #12）：P6 两图 rect ×34 与核心逐元素 identical、数值标签全等（Demócrata 31,7/26,8/18,7/6,3/3,1；CIS 34,0/22,2/17,1 + Sumar/Podemos「no publicado」——两组数据未混）。
- gloss 词条点数：content12 5 · content34 10 · content56 5（与核心逐文件全等，无丢条）。
- P7：8 条西语短语逐字节 = 核心；页标签计数 (Página 1..6) = 1/2/2/1/1/1 与核心全等；VOL.2 预告（10/29 DANA 纪念、10/31、11/1、11/2、真实来信 + 最佳作文）西语原文冻结、日语注保留承诺。
- 冻结事实：`desde el viernes 23` ×1、`jueves 23` = 0；周二全欧总进球 40（正文 + #57 注 + P8 注三处一致）。
- 残留扫描：中文讲解残留 = 0（简体字形启发命中 3 处皆合法日语：通り/全体/着られる/通さず）；荷/俄/韩等他列家具 = 0；禁用术语 paper/KIT/operative code = 0。
- 日历口径：Europe/Madrid 2026——换时 Sun Oct 25、El Clásico Oct 25 21:00、F1 Austin 同刻，正文冻结继承核心已核口径。

## §5 自校缺陷与修复（只动日语侧，README #15）

1. P3 标题 HEAD TOO WIDE：`RECORDAR JUNTOS · ともに追悼する` → `RECORDAR JUNTOS · ともに偲ぶ`。
2. P6 练习 FLOW OVERFLOW（#99/#100 压页脚）：A 组讲解两行→一行 `二つの図を見て、答えを選んでください。`，分栏级联恢复核心分布（83–86 同栏），溢出清零。
3. P1 黑带 TEXTX：deck 日语与大标题墨迹相触 → `日曜は1時間長く眠れる · クラシコもある`（去「今週は」）。
4. P1 CINCO CLAVES： expl 出页（EDGE）→ `五大見どころ：数字は作らず今号で説明。`；盒标题先缩为 `今週の五大見どころ · Para entender la semana`，实测墨迹距边仅 3.5，再缩定形 `五大見どころ · Para entender la semana`。
5. P1 CIFRAS 盒标题 BOXTITLE：`LA SEMANA EN CIFRAS · 数字で見る今週` → `LA SEMANA EN CIFRAS · 今週の数字`（实测距边 26.5）。
6. P2 FRASE 盒标题 BOXTITLE：`…· 覚えるフレーズ` → `…· フレーズ` 后实测距边仅 2.2，定形 `LA FRASE PARA RECORDAR · 一句`。
7. P7 读者信注 TEXTX：日语注 4 行（核心 2 行）压短语行 → `見本の手紙で、本物ではありません。VOL.2 に本物の手紙と最優秀作文を掲載。`（2 行，盒高随 wrap 实测自适应）。
8. P1 LINEX（连休注 vs 分隔线）：与核心同位同几何（核心中文注出货即有此旗），裁定继承、不动。

## §6 声明不变集（12 值，逐字节同核心，附理由）

- `los relojes → cambian（ellos）`、`el reloj se atrasa（él）`：西语变位式 + 代词标签，无中文。
- `van a + 原形`、`vamos a + 原形`、`va a + 原形`、`vas a + 原形`：注文为西语句型式本身（「原形」为共有汉字术语）。
- `La gente ___ (原形 buscar) el disfraz en internet.`、`El equipo femenino ___ (原形 estrenar) la camiseta el sábado.`：西语题干，「原形」共有汉字。
- `dormir: él → duerme（o→ue）`：变位式，无中文。
- 读者示例信（Mei，西语全文 + `（carta de ejemplo, escrita por la redacción）`）：冻结西语正文。
- `cementerio = 墓地`：共有汉字词义对。
- `CULTURA · 文化`：共有汉字章节头（DE×JA 出货同形）。

## §7 独立校对记录（2026-10-22，校对者独立复跑/复测，未采信建造者自报）

**结论：PASS — 完整一轮零缺陷、零修复，无重渲染。**

- **freeze**：`freeze.py baseline` 核心 8/8 逐字节复现（哈希与 §4 登记逐项全合）；校对开局/收尾核心 8 SVG sha256 两度全等，核心零触碰。重定向副本（OUT 改道经 grep + 打印双验、无真实版面路径残留）实际执行导出的 ES×JA 注册表复渲出货 SVG **8/8 逐字节同**（构建确定性自证）。
- **freeze diff 分账**：非 CJK 增删逐项归因闭合——P1 标语→徽章（定点编辑）、P1 折行碎片 1（讲解行换行位移）、P5/P6 词库行同词重排、P7 混合行碎片 1、P8 分隔 ×8；西语正文多重集与核心全等、移除侧非讲解项 = 0；added CJK 恰 **3,005** 字全为日语讲解层。
- **注册表双路复核**（执行导出 + 校对者自写 AST 字面提取，两路互证）：150 = 150，page/level 差 0（总量 150 = A2 52 · B1 70 · B2 28，逐页 10/18/18/18/18/18/12/38）；题型 zh→ja 映射 1:1、逐类计数与 §2 全合；**键差异恰 {137, 138, 150}** 与 §2 登记表逐字合；**题干差异恰 {139, 140}**、opts/rights 差 0；注差 136 条逐条读核忠实；未变 14 条 {#18, #20, #35, #60–63, #76–79, #87, #102, #103} 逐条裁定成立（西语变位式/算式类语言中立 + 「墓地」「原形」汉日共享表记，§6 声明集内）。
- **手工重推导**：自西语正文与题面逐条重推全部 **150 键，零分歧**（含配对 #25–28/#52–55/#141–144 字母映射、图表 #83–88〔31,7+26,8+18,7=77,2 复算、双组 Vox 均第三〕、完形 #113–120、对话 #145–149、翻译 #137–140 双向核）；P8 H 区范文逐词实数 **82 词**，与两版标注吻合且在题面 80–100 区间内。
- **p8.py**：独立 extract 核心印刷集 = 150 条（全集）；compare **CLEAN 150=150**（missing=[]、extra=0）；行级 keydiff 14 项逐项做 README 第 13 条证伪核——#137/#138 为真键变，余 12 项 {#12, #14, #16, #17, #57, #73, #75, #83, #95, #96, #101, #105} 注册表键逐字节同、差异全在已译注内，属提取构成伪影；印刷式样短横式 `N. key — note`（写作项 `N. ✓ note`）与核心及 ES 家族出货代码一致。
- **冻结事实**：`desde el viernes 23` ×1、`jueves 23` = 0；总进球 40 三处（正文题干、注册表 #57 注、P8 印刷注）一致。
- **遮挡审计**：`occlusion_audit.py`（自检先行通过）本版 2 旗 = 核心同位 2 旗。P5 BOXTITLE 为冻结西语行 «Murcia y Canarias.»，墨迹盒与核心逐值全等（底 1037.5 vs 边 1036.8），继承成立。P1 LINEX 工具报 NEW 系串文本不同所致的匹配伪影，像素裁定：核心与本版卡面该注墨迹同止于第 1842 行、1843–1850 行在文本窗与对照窗暗像素同为 0，实际渲染墨迹与线零相交（核心自身同几何出货），**非缺陷**。
- **同行扫描**（README 第 10 条，自写真墨迹盒实现）：本版 0 碰撞、核心 0。
- **图表兜底**（第 12 条）：P6 rect 全表 34 = 34 与核心逐元素全等（条形几何全同）；标签 Demócrata 31,7/26,8/18,7/6,3/3,1 与 CIS 34,0/22,2/17,1 + «no publicado» ×2 逐项全等、两组未混；卡面目检标签覆盖 0%。
- **JA 列定式验收**：§3 家具逐项在版且逐字合——徽章 ×1、顶带 ×1、通栏题花 ×1、页脚 ×8 全同登记串、页码 «N ページ（全 8 ページ）» 1–8 逐页对应、P8 页首 «RESPUESTAS · 全解答と解説（1–8ページ）» + 右注、分隔 «— N ページ —» ×8、章节头（西语原题 · 日语短题）×6、gloss 前缀单层（«解説 — 解説» = 0）；目标语名 スペイン語 与 §3.1 名表一致。
- **svglib 与禁则/断词**：build svglib.py md5 实测 = `d73e23b365676c3618d7e060b835eb4d`，与日语核心 build 逐字节同；自写行首禁则扫描（XML 解析重构行，含 tspan 断行）全册 **0**；拉丁断词扫描（限含假名讲解行）3 候选逐项裁定均为词间折行（«el / pronóstico»、«el / largometraje»、«es / importante»，断点两侧皆完整词），**词中劈开 = 0**。
- **gloss 点数**（代码层 AST 逐调用核）：gloss() 词条 content12 = 5 · content34 = 10（5+5)· content56 = 5，与核心逐条同数同序、西语词头序列全等；P1 expl 词条行 4 条同核；expl() 调用数逐文件 5/9/6/3/1 与核心 bridge() 全等，改名属实。
- **P7**：8 条西语短语逐节点逐字节 = 核心（双节点短语拼接核毕）；页标签计数 (Página 1..6) = 1/2/2/1/1/1 与核心全等；VOL.2 预告西语冻结、日语注中读者信 + 最佳作文承诺保留（§5.7 两行形在版目检）。
- **建造者自校修复复核**：§5 八项落点逐项在版（P3 偲ぶ 形、P6 A 组一行指令 + #99/#100 分栏分布、P1 黑带 deck、CINCO CLAVES expl 与盒标题两度缩短定形、CIFRAS 盒标题、P2 FRASE 盒标题 · 一句、P7 读者信注两行形）；图片载荷逐页与核心全等（1/0/1/0/1/0/0/0），署名随核心冻结。
- **日历**（`date` Europe/Madrid 实测）：10-19 一、10-20 二（#57 注火曜合）、10-23 五、10-24 六（球衣首秀 «sábado 24» 合）、10-25 日（换时 + Clásico 21:00)、10-29 四（DANA 纪念 «jueves 29» 合）、10-31 六（Halloween)、11-01 日（诸圣节）、11-02 一（连休周一）与纸面全合。
- **残留/红线**：中文讲解残留 = 0（「仅汉字无假名」节点逐条裁定为正明日语：空所補充/正誤/翻訳/作文等列定式标签、天気予報/世論調査/選挙管理委員会等固有词）；西里尔 = 0、韩字 = 0、他列家具 = 0；禁用术语纸面 = 0（scratch 转换脚本内核心原串引用为例外，§1 已披露）；讲解层无国际政治新增（西班牙国内选举为核心冻结题面，讲解仅语言说明）。
- **最终针脚（磁盘实测，与 §0 登记逐字全合）**：网页版 `La-Lucerna-VOL1-JA-web.pdf` **3,842,414 B** · sha256 `bf894077083fa710ba1c3b53d477564e5800d9a8d6a63823ca9b22029390c77c`（< 10 MB)，8 页；印刷版 `La-Lucerna-VOL1-JA.pdf` **20,004,913 B** · sha256 `31ba9af8318fbfa79ba4c86745ab49dc35972d8c4f0f096f429c023a67fe0842`，8 页；cards ×8、SVG ×8。

## §8 D5 重建记录（2026-11-13，W43/W45/W46 D5+§1.1 合并重修 Phase 1）

- **原因**：D5 缺陷——sans 层拉丁/西里尔字符落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者）。本版修前 census：D5 拉丁 340、西里尔 0、弯引号 CJK 0。
- **安装**：`tools/mechanism-w47/apply_variant.py --svglib <版>/svglib.py --target es --reader ja --week 2026-w43`（先 `--check` dry-run 通过）。`_D5_READER = "cjk"`。路由单元测试 `test_d5_routing.py` FAILURES: 0。fix2（U+201C/U+201D/U+2019 → serif）保留：本版弯引号 0 个。
- **基线**：重建前先证基线干净——`run.py` TOTAL 150、0 警告；`render.py` + `webpdf.py` 产出与已发版文本层逐字一致（字符多重集差 0）；重建 SVG 8/8 与已发版逐字节相同。基线实测（已发版配方）：印 PDF `bf2e639b97f79677fd7bcdb037c329176bad6bdffc8cd6fe0e1e95485db08615`（18,045,216 B）、网 PDF（render）`955c7f6c9e3cc130747df8c1ad57f260b78bec711cec431209c4c44a62ea9640`（3,438,455 B）。§0 旧值（20,004,913 / 3,842,414 B）为更旧配方，已过期，以上两值为准。
- **二次修复（只动字号，文字零改动；实测 advance，patched svglib `text_w`，sans bold；栏宽 CW=422.5，盒标题内宽 404.5，P7 p.text 标题内宽 400.5）**：
  1. `content12.py:125` P1 头 `EL OTOÑO EMPIEZA DE VERDAD` 25→24（439.1→421.5）。
  2. `content7.py:16` P7 头 `A2　DECIR LA HORA Y EL PRESENTE` 24→21（471.1→412.2；同时清除 P7 TEXTX 碰撞——该头压 `B1` 20.5×16.8px）。
  3. `content7.py:48` P7 头 `B2　CREO QUE… / NO CREO QUE…` 24→23（428.8→411.0）。
  4. `content12.py:47` P1 盒 `LA SEMANA EN CIFRAS　今週の数字` tsize 23→21（427.0→389.8；22pt 仍 +3.9）。
  5. `content12.py:176` P2 盒 `LA FRASE PARA RECORDAR　一句` tsize 23→22（410.2→392.4）。
  6. `content7.py:79` P7 `ERRORES TÍPICOS　よくある間違い` p.text 23→22（409.2→391.3）。
  - P3 头 `RECORDAR JUNTOS　ともに偲ぶ` 25pt 实测 418.0 入栏，无需修。
- **P8**：行数 222→222，距页脚线余量 41.7px 不变；p8 compare CLEAN（keydiff [137, 138]）。
- **新交付物（D5 重建，2026-11-13）**：印 PDF `La-Lucerna-VOL1-es-ja.pdf` sha256 `53aef2d8d57fe87f1c0b1c07e82fb86f536ba707fd9fef60ce9e7081f4375004`（11,775,499 B）；网 PDF（render）`La-Lucerna-VOL1-es-ja-web.pdf` sha256 `653e235f39a0768037ff5aa73b8a16e87780b0f6c78098713fcb2f0a44ed27c3`（3,449,690 B）；issues 网 PDF（`tools/webpdf.py`）`2026-w43-es-ja.web.pdf` sha256 `5d8fd9b1ad2b38152bbcf99494c22de52cff2eff157bc80d364e333daf40ba93`（1,547,194 B）——待 closer 换入 `issues/2026-w43/2026-w43-es-ja/2026-w43-es-ja.pdf` 并更新 pin（已发版 `6aff84ace50444208b129f56fb1c99c7d77e3b0fb1ac917f19c4d33abb3b32ed`，1,716,266 B）。印 PDF 由 18.0MB 缩至 11.8MB：`pdffonts` 核查——基线嵌 `NotoSansCJKsc`/`NotoSerifCJKsc`，D5 后嵌 `NotoSansCJKjp`/`NotoSerifCJKjp`（按读者选 CJK 变体）+ Newsreader，全部 embedded/subset/unicode，无丢字体；文字内容不变（文字层 print=web 多重集差 0）。
- **text.md**：D5 不改文字内容；重建后重出因字体宽度变化断行重排（20 REWRAP），交付件为已发版 `.text.md` 原样沿用（BYTE-IDENTICAL）；验收 `verify_textexp_es.py --edition` 判 ADOPT（0 UNEXPECTED；习题号 313/313 序列一致；8 页 token 全同）。
- **D5 门禁（17 门，run 2，全绿 ALL-GREEN）**：run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（1,547,194 B <7MB）；occlusion 0（含自检）；p8 extract 150/150；p8 compare CLEAN；freeze baseline 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 1 个（U+3000，run 拆分）；spill 0；boxtitle 0；edge 0/0；creambox PASS 0 缺陷（ratios n=395，中位 1.040）；文字层 print=web 多重集差 0；census_quotes 0 defective；家族 gates.py N/A。日志：`hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-ja/`（`GATES-SUMMARY.txt` 为总表；run1 日志归档于 `run1/` 子目录）。D5 报告：`production/notes/2026-w43/g-es/scratch-d5-rebuild-es/D5-REPORT-2026-w43-es-ja.md`。
