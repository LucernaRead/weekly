# WEEKLY-KIT — ES×KO（西班牙语正文 · 韩语讲解 해요체）· W43 VOL.1

- 状态：**PASS**（独立校对一轮零缺陷、零修复，2026-10-22；校对记录见 §8）
- 期号：VOL.1 · 2026-10-19–25（Semana del 19 al 25 de octubre de 2026）
- 配对：目标语 = 西班牙语（스페인어）；读者母语 = 韩语。讲解层全韩语（해요체），西语正文逐字节冻结。
- 源核心：`files/weekly-report-es-vol1/`（build: `hidden_files/weekly-report-es-build/`）；本版 build: `hidden_files/weekly-report-es-ko-build/`（OUT 已改道 `files/weekly-report-es-ko/svg`，首跑前打印验证）。
- 练习总量：**150 = A2 52 · B1 70 · B2 28**；分版 10/18/18/18/18/18/12/38，与核心注册表逐项一致（level/page 差异 = 0）。

## §1 冻结与变换

- 开工前 `tools/freeze.py baseline`：副本在新目录复现核心 **8/8 逐字节一致**；收尾复核核心 SVG sha256 **8/8 未变**。
- 变换：`hidden_files/weekly-report-es-ko-build/scratch/transform_ko.py`（confined scratch，AST 定位拼接替换）——含汉字字符串常量 **264 个 / 484 处**全部映射为韩语，断言：清单全覆盖、出现次数逐项相等、变换后韩字（汉字）常量 = 0。讲解函数已按 KO 列定式改名 `expl()`（定义 1 + 调用 20 处）。
- `freeze.py diff` 证明：移除侧非讲解项 = 0（13 项均为折行碎片/全角标点碎片 + 8 个 P8 分隔符 «— PÁGINA n —» 的登记替换）；新增侧汉字 = 0（出货 SVG 全册汉字字符数 = 0）；西语 token 流逐页比对，差异仅韩语讲解内嵌标点/数字与页脚、分隔符家具。
- 冻结事实核验：«desde el viernes 23» = 1、「jueves 23» = 0；«40 goles» = 1、「38 goles» = 0（与核心同值）。

## §2 家具（§3 定式逐项）

- P1 徽章（插入式，FR×KO 先例；ES 核心 y=372 为冻结西语副题不可替换）：`p.text(975, 574, "스페인어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판", 22, sans, bold, BRICK, anchor="middle")`——位于暗带（底 542）与头条 kicker（基线 606）之间。
- 页脚左：`La Lucerna · 스페인어 주간지 VOL.1 · 텍스트는 스페인어 · 해설은 한국어`；页脚右：`제 {n} 면 / 총 {total} 면`（8 版全同）。
- gloss 前缀：`해설 — `（bslib4 gloss()）。
- P8 分隔：`— 제 {pg} 면 —`；P8 式样 = **短横式**（`N. key — note`，写作题 `N. ✓ note`），与核心代码/SVG 一致，未动答案生成代码。
- P1 顶带：`CADA SEMANA EN ESPAÑOL · 매주 발행 · 스페인이 읽는 스페인어`；y=330 行：`스페인어 주간지 · VOL.1 · EL RELOJ · EL CLÁSICO · LA F1`（y=372 西语副题冻结原样）。
- 目标语名表（KO 列定式）：西班牙语 = 스페인어。
- 题型标签：完成句子→문장 완성(48) · 单选→객관식(47) · 词汇配对→단어 짝짓기(12) · 判断对错→읽기 판단(8) · 造句→문장 만들기(7) · 句型转换→문장 바꾸기(10) · 完形单选→빈칸 채우기(13) · 翻译→번역(4) · 写作→쓰기(1)。
- 指令标签：填空→빈칸 채우기 · 改写→바꿔 쓰기 · 判断→참 / 거짓 · 把词和释义配对→단어와 뜻 짝짓기 · 翻译→번역 · 写作→쓰기。

## §3 键差异全表（注册表实测，仅此 3 项 + 2 项题干改向）

| # | 类别 | 核心键 | 本版键 |
|---|------|--------|--------|
| 137 | 翻译题键（ES→读者语） | 周日我们多睡一个小时。 | 일요일에 우리는 한 시간 더 자요. |
| 138 | 翻译题键（ES→读者语） | 周一在九个自治区是假日。 | 월요일은 아홉 개 자치주에서 공휴일이에요. |
| 150 | 装置项（写作范文） | （开放题，范文如下） | (열린 문제 — 모범 답안은 아래에 있어요) |
| 139 | 题干改向（读者语→ES，键不变） | 国家德比周日晚九点开踢。→ ___ | 엘 클라시코는 일요일 밤 9시에 열려요. → ___ |
| 140 | 题干改向（读者语→ES，键不变） | 每个图表都必须标明来源。→ ___ | 모든 도표는 출처를 밝혀야 해요. → ___ |

- 其余 145 键与核心逐字节一致（注册表 dump 对照 `scratch/reg-core.json` vs `scratch/reg-ko.json`）。
- `p8.py compare` 报 keydiff=[12, 14, 16, 17, 57, 73, 75, 83, 95, 96, 101, 105, 137, 138]：其中 137/138 为上表真实差异；其余 12 项注册表键逐字节未变，系韩语版面折行导致的抽取伪影（README #13 口径证伪）。
- 语言中立注逐条核：纯西语/公式类注（如 `ganar → ganó`、`31,7 + 26,8 + 18,7 = 77,2` 类）原样保留；含汉字注 150 条全译。

## §4 gloss 与 P7 点数

- gloss 框逐页点数（核心 译注｜ vs 本版 해설 —）：P1 0/0（P1 的 «해설 —» 出现 1 次为徽章本身）、P2 1/1、P3 1/1、P4 1/1、P5 1/1、P6 0/0、P7 0/0、P8 0/0——逐条保留，一项不少（每框内词条逐条译，未删并）。
- P7 金句：8 条西语引文逐字继承（空格剥离法计数核心/本版均 1/1）；页标签 `(Página N)` 8/8 与核心同形同数；三栏短语与出现次数 = 核心。
- 日历口径（Europe/Madrid）：换时 Sun Oct 25、El Clásico Oct 25 21:00、F1 Austin 同周——讲解层未引入国际政治，未改任何日期事实。

## §5 机械门结果（全绿）

- `freeze.py baseline/diff`：见 §1。
- `p8.py compare`：**CLEAN**（core 150 noted / edition 150 noted，missing=[]，extra=0）。
- `occlusion_audit.py`（自检先行 OK）：**NEW vs core = 0**（本版仅剩 1 个 BOXTITLE flag = 核心自带 P5 «Murcia y Canarias» 0.7px 先存 flag，非新增）。
- 同行墨迹扫描（README #10）：遮挡审计 TEXTX 类覆盖，P1 顶带三段与暗带左右行均无重叠（修复后数值：韩语暗带行起 x=1426.5 > 西语行墨迹终点 1343）。
- 图表标签元素级检查（README #12，P6）：标签 PP/PSOE/Vox/Sumar/Podemos ×2、8 个数值、`— no publicado en la fuente —` ×2、双标题、双注脚逐项 1/1 或 2/2；P6 文本元素总数 206 = 核心 206。
- 韩字折行：逐行墨迹宽由遮挡审计 EDGE/BOXTITLE 覆盖 = 0 新增；孤行标点/孤行音节扫描 = 0（修复后）。
- 残留扫描：出货 SVG 汉字 = 0；他列家具（Die/Le Lucerna、俄/日家具）= 0；禁用术语在 paper/KIT/operative code = 0（变换脚本 confined 于 build scratch 并在此披露）。
- 构建流溢出警告 = 0（P8 答案流尾行基线 2548.7 < 2552；核心尾行 2535.6）。

## §6 自校缺陷与修复（一轮全量目检 8 页卡后）

1. **P8 答案流溢出**：韩语注较长，11 条注多折一行，尾项 #150 基线落 2565.5（核心 2535.6）。按 README #15 缩短本版自有韩语注 11 条（#32 Samaín 注、#43–46 句法注、#57、#76/#78、#80、#81、#140），尾行回到 2548.7、溢出警告清零。
2. **遮挡审计 7 个 NEW flag**（P1/P2）：暗带韩语行与西语行同行碰撞（缩短为 «이번 일요일 한 시간 더 자요 · 엘 클라시코»）；CIFRAS 框题过宽压 «Austin.»（改 «LA SEMANA EN CIFRAS · 이번 주 숫자»，一并消除 TEXTX+BOXTITLE 两 flag）；CINCO CLAVES 副题与底线过宽（删 «이번 주»、底线截短）；P2 «LA FRASE» 框题过宽（韩段缩为 «암기»，与中文「口诀」二字对仗）；本周词条段韩文字形下探压 1844 金线（该段压成一行 «‘연휴’: 사흘 휴일. 이번 호는 ‘두 동강’ — 3면.»，西语释义行在其正上方）。
3. **韩语孤行碎片 3 处**：P4 讲解句尾 «요.»、P8 #44 注尾 «와요»、P8 #140 注尾 «요»——逐条缩短后孤行扫描 = 0。
4. **P7 第 3 栏越界（目检发现，审计类未覆盖）**：韩语注多折 4 行，三框底边落 1775，压过固定金句区金线（1686）。缩短 errs 两注（各回到 1 行）、palabra 注、cartas 注（各回到 2 行），三框底边与核心逐值相同（961.96 / 1312.96 / 1663.96）。
5. **小瑕**：P2 gloss 括号 «(시계를)» 被折行劈开 → 改无括号行文；P5 C 区讲解句在栏间劈词（나/타내세요）→ 缩短后整句回本栏一行。
- 每次修复后均一进程重渲染并复跑全套门（见 §5 终值）。韩文字形全页目检无缺字/方框（Noto CJK 字体口径同 EN×KO 出货先例，SVG 家族名与核心同）。

## §7 实测针脚（交付时磁盘实测）

- 印刷 PDF `La-Lucerna-VOL1-KO.pdf`：**6,282,148 B** · sha256 `38bf908926ea9b4e250bc2d978f28efd8f83e30174722e19ae9c7ae3306072ee`（D5 重建，2026-11-13；见 §9 D5 记录）
- 网页 PDF `La-Lucerna-VOL1-KO-web.pdf`：**3,417,414 B**（< 10 MB） · sha256 `aea95a87809290a1ed7e281282019a511ee8e043bb3fc31a0d2e201239edfd35`（D5 重建，2026-11-13；见 §9 D5 记录）
- SVG sha256：p1 `da993d0baa0d2409a30ee79af7b3f454b0ba2efa479be2912335a58bfe68ca10` · p2 `3654c8eb46b6f01205e83af96c7231b7ab154faeddfa1120a2ba17bfaaa73e5e` · p3 `9fe246f50b0a8433a9951dfc6430860ca22cc1fa71bb0cc9fa2237e06c416012` · p4 `2c8e9b73cba4b7c6ffd697341705d89df6ead2623a9d108c8afd0bf6d44032ae` · p5 `49ec7813abcab084f26f62cb6ad3701c2eb713dbc6823e66e0af972b6f3e9a3a` · p6 `c265b10ab5e70820217ecaacea6eccccb15fb57cb821f96c81698e03eb918bc3` · p7 `f82226dd3b89e28c2efe88c790668cbe8b14aa24a5da75134935121b6e4c56eb` · p8 `8cdb00fbd30171d43d5f0a049fc6d580b5f2b15ff0517a5fdf6d94a1cbb220d3`
- 交付物：`files/weekly-report-es-ko/`（svg ×8、cards ×8、印刷 PDF、网页 PDF、本 KIT）。未入仓、未发 Discord。

## §8 独立校对记录（2026-10-22，校对员独立复跑，未采信建造者自报）

- **结论：PASS（一轮零缺陷、零修复，无重渲染）。**
- freeze：baseline 核心 8/8 逐字节复现；校对员在 hidden_files/es-ko-proof-scratch 的改道副本（OUT 经打印验证、真实路径残留 = 0）中一进程复渲双 build，出货 SVG 双侧 8/8 逐字节复现（构建确定性自证）；收尾核心 SVG sha256 与开工快照 8/8 全等，核心零触碰。diff 分账：新增串含汉字 = 0、新增 CJK 3,236 字全为韩字音节；移除侧无汉字/韩字串 13 项逐项裁定为折行碎片（21:00)、Halloween（、indefinido。、tenga/sea/llueva）。、indecisos 重排碎片）+ P8 分隔符登记替换 ×8，非讲解项移除 = 0；西语 token 多重集逐页对照，差异仅页脚家具替换、注内引文标点附着与讲解层数字，无正文丢失。
- 注册表：校对员自备一进程 dump（与建造者 dump 互证：核心 dump 逐字全等；KO dump 仅 #44/#140 两注与建造者 scratch 旧 dump 不同，系建造者 §6-3 孤行修复后的终形，建造者 dump 为修复前旧快照——以出货 build 代码为准，非版面问题）。page/level 差 = 0；**键差异恰 {137, 138, 150}**（与 §3 表逐字全等）、题干改向 {139, 140} 韩语题干与原中文题干语义逐项核合、键不变；type 150 全译；注差 141 条，未变 9 条逐条裁定为纯西语变位/算式中立注（#18/20/60/61/62/63/87/102/103）；注内数字序列差 8 项全为中文数字→阿拉伯数字等值转写，无一改值。**全部 150 键由校对员自西语正文/题干/选项逐题手工重推导，零分歧**（含 #87 算式 31,7+26,8+18,7=77,2、#85 双组 Vox 均第三、范文实数 82 词在 80–100 区间）。
- p8.py：extract 出货核心独立复证印刷集 = 150；本版 150；compare **CLEAN 150=150**，missing=[]、extra=0，keydiff=[12, 14, 16, 17, 57, 73, 75, 83, 95, 96, 101, 105, 137, 138]——其中 12 项经注册表逐字节同键证伪为行级抽取伪影（README #13），与建造者登记逐项相同。P8 印刷式样短横式（149 条 `N. key — note` + #150 `✓`），与核心代码/SVG 及 ES 家族口径一致。
- 冻结事实：«desde el viernes 23» 核心/本版各 ×1、「jueves 23» = 0；总进球 40（正文题干 «¡40 en toda Europa!»、本版 #57 注 «40골»），38 无出处。
- KO 列定式：徽章实测 x=975 居中、y=574、22pt、700、#a4553a，文与 EN×KO §3 定式（目标名 스페인어）逐字合；页脚 ×8、页码 «제 N 면 / 총 8 면» ×8、顶带、y=330 行、P8 分隔 «— 제 N 면 —» ×8（旧式 = 0）全合；gloss 前缀单层、无双前缀；expl() 定义 1 + 调用 20 与登记合，operative code 中 bridge = 0。
- gloss 点数：源码 AST 逐框点数 P2/P3/P4/P5 各 5 条，与核心同数同序、词头序列全等（20 条全译，无丢条）。
- 几何兜底：occlusion_audit（自检先行）本版 1 旗 = P5 «Murcia y Canarias.» BOXTITLE（底墨 1037.5 > 框 1036.8），与核心自身同位同值同串（冻结西语行），NEW vs core = 0，继承成立；核心 P1 LINEX 在本版不出现（本版自有韩语行已收一行，第 15 条合规）。同行墨迹扫描（README #10）本版/核心均 0 碰撞。P6 图表元素级（第 12 条）：文本元素 206 = 206，两组民调数值/分组逐项全等未混（Demócrata 31,7/26,8/18,7/6,3/1；CIS 34,0/22,2/17,1 + «no publicado» ×2），以审计墨迹机械复测全页任意覆盖率 >0.1% 者 = 0。P7 金线复核：三框底边自出货 SVG 实测 961.96/1312.96/1663.96 与核心逐值全等，金线 y=1686（#b3a06a，×2）双侧同位，卡面像素扫描 1664–1685 行带无墨迹侵入；P8 尾行最大基线与核心逐值同（2535.64，墨迹底 ≈2548.7 < 2552），页脚带 y>2580 仅页脚本体。孤行扫描：短元素仅 P8 题型标签（번역 ×4、쓰기 ×1）与 P1 «폭풍우.»（完整名词收尾，与核心同位折行形态一致），孤行标点/孤行音节 = 0；gloss 续行行首 «·» 与核心同位同形（家族格式）。
- P7：8 条金句 + 页标签 8/8（分布 1:1、2:2、3:2、4:1、5:1、6:1）与核心全等。
- 日历（Europe/Madrid 实测）：10-19 周一、10-23 周五、10-25 周日（换时 + Clásico 21:00）、10-31 周六、11-01 周日、11-02 周一、11-29 周日（大选）、2027-03-28 周日——与纸面全合。内容红线：讲解层全为核心既有内容的韩语转写，无国际政治新增。
- 残留：成品 SVG 汉字 = 0、西里尔 = 0、荷/俄/日家具 = 0、bridge/가교/KIT/operative = 0。
- 最终针脚（磁盘实测，与 §7 登记逐值全合）：网页 PDF 3,812,736 B · sha256 2840d5a697804fb310e90cada85b5ad4b81fdbfd5045d523f1bb879fc83c682b；印刷 PDF 10,974,471 B · sha256 cb861bdb57153529fb2d69fbc38697073a9fbabbf2984aac0623319951c42f60；两 PDF 均 8 页。
- 备注（非缺陷）：§1 «40 goles» 计数为建造者对代码的速记，SVG 渲染面作 «¡40 en toda Europa!»，事实本身已实证；§6-1 的 2548.7 为墨迹底口径，基线口径 2535.64 与核心逐值同。

## §9 D5 重建记录（2026-11-13，W43/W45/W46 D5+§1.1 合并重修 Phase 1）

- **原因**：D5 缺陷——sans 层拉丁/西里尔字符落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者）。本版修前 census：D5 拉丁 346、西里尔 0、弯引号 CJK 4（修前已在 CJK 者 4 个，fix2 后归 Newsreader）。
- **安装**：`tools/mechanism-w47/apply_variant.py --svglib <版>/svglib.py --target es --reader ko --week 2026-w43`（先 `--check` dry-run 通过）。`_D5_READER = "cjk"`。路由单元测试 `test_d5_routing.py` FAILURES: 0。fix2（U+201C/U+201D/U+2019 → serif）保留：本版弯引号 5 个全在 Newsreader（U+2019×5）。
- **基线**：重建前先证基线干净——`run.py` TOTAL 150、0 警告；`render.py` + `webpdf.py` 产出与已发版文本层逐字一致（字符多重集差 0）；重建 SVG 8/8 与已发版逐字节相同。基线实测（已发版配方）：印 PDF `3474f60c845a5771743987d2732e3ed7a943716cc1c9f9989ec5e73a5e031d97`（9,097,069 B）、网 PDF（render）`6acefbaec02f6aa4aaec8c8607dd22e222561dc0d7522d20889f3d13bdfaddfa`（3,407,869 B）。§7 旧值（10,974,471 / 3,812,736 B）为更旧配方，已过期，以上两值为准。
- **二次修复（只动字号，文字零改动；实测 advance，patched svglib `text_w`，sans bold；栏宽 CW=422.5，盒标题内宽 404.5）**：
  1. `content12.py:126` P1 头 `EL OTOÑO EMPIEZA DE VERDAD` 25→24（439.1→421.5）。
  2. `content34.py:23` P3 头 `RECORDAR JUNTOS　함께 기억해요` 25→24（436.8→419.3）。
  3. `content7.py:16` P7 头 `A2　DECIR LA HORA Y EL PRESENTE` 24→21（471.1→412.2；同时清除 P7 TEXTX 碰撞——该头压 `B1` 20.5×16.8px）。
  4. `content7.py:48` P7 头 `B2　CREO QUE… / NO CREO QUE…` 24→23（428.8→411.0）。
  5. `content12.py:48` P1 盒 `LA SEMANA EN CIFRAS　이번 주 숫자` tsize 23→21（428.5→391.2；22pt 仍 +5.3）。
  6. `content12.py:177` P2 盒 `LA FRASE PARA RECORDAR　암기` tsize 23→22（406.5→388.8；boxtitle +1.7，低于 creambox 2.0 阈值但高于 boxtitle 1.0 阈值，按严门修）。
- **P8**：行数 199→199，距页脚线余量 57.4px 不变；p8 compare CLEAN（keydiff [137, 138]）。
- **新交付物（D5 重建，2026-11-13）**：印 PDF `La-Lucerna-VOL1-es-ko.pdf` sha256 `38bf908926ea9b4e250bc2d978f28efd8f83e30174722e19ae9c7ae3306072ee`（6,282,148 B）；网 PDF（render）`La-Lucerna-VOL1-es-ko-web.pdf` sha256 `aea95a87809290a1ed7e281282019a511ee8e043bb3fc31a0d2e201239edfd35`（3,417,414 B）；issues 网 PDF（`tools/webpdf.py`）`2026-w43-es-ko.web.pdf` sha256 `389bd523584acba28c558a854f8f999528ca5c9ecf20d9b5704c5667dc7d305a`（1,316,458 B）——待 closer 换入 `issues/2026-w43/2026-w43-es-ko/2026-w43-es-ko.pdf` 并更新 pin（已发版 `a31454d21995f28523496cf3ca23a38eff17b894170c191e5fdb4221afd0ef63`，1,402,447 B）。印 PDF 由 9.1MB 缩至 6.3MB 系字体子集变化（拉丁文移出 CJK 字体、按读者选 KR 变体），文字内容不变（文字层 print=web 多重集差 0）。
- **text.md**：D5 不改文字内容；重建后重出因字体宽度变化断行重排（28 REWRAP），交付件为已发版 `.text.md` 原样沿用（BYTE-IDENTICAL）；验收 `verify_textexp_es.py --edition` 判 ADOPT（0 UNEXPECTED；习题号 313/313 序列一致；8 页 token 全同）。
- **D5 门禁（17 门，run 2，全绿 ALL-GREEN）**：run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（1,316,458 B <7MB）；occlusion 0（含自检）；p8 extract 150/150；p8 compare CLEAN；freeze baseline 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 1 个（U+3000，run 拆分）；spill 0；boxtitle 0；edge 0/0；creambox PASS 0 缺陷（ratios n=385，中位 1.040）；文字层 print=web 多重集差 0；census_quotes 0 defective；家族 gates.py N/A。日志：`hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-ko/`（`GATES-SUMMARY.txt` 为总表；run1 日志归档于 `run1/` 子目录）。D5 报告：`production/notes/2026-w43/g-es/scratch-d5-rebuild-es/D5-REPORT-2026-w43-es-ko.md`。
