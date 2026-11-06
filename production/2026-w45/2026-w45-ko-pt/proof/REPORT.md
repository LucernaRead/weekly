# 独立校对报告 — Lucerna Weekly W45 KO×PT（韩语目标 × 葡萄牙语读者）

**结论：ZERO PROBLEMS（纸面）**

- 校对对象：`files/weekly-report-w45-ko-pt/`（svg×8、cards×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）。
- 对照：W45 KO 核心 `files/weekly-report-w45-ko-core/`（只读实测复核，未引用其他语族数值）与 W43 同配对版 `files/weekly-report-ko-pt/`（家具三方对照，W43 优先于 README #20）。
- 构建员声称值全部独立重测，不采信。工具版本：`tools/p8.py` sha256 `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b27462703d8226815046eccc0ca9`（已采纳新版，与任务给定前缀一致）。
- 未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录内容（见 §14 过程披露：一次误操作只改了 mtime，内容哈希差分全空）。
- 不宣布上架。是否入仓由主线决定。

## 0. 开工查重（stand down 判定）

- 开工时（2026-10-28 04:12 UTC）无在途 python/render 进程；交付物最新 mtime 04:11:21（KIT），经 90 秒等待后复查，静默 173 秒，无 ko-pt 树写盘 → 安全开工，不 stand down。
- 交付物声称值核实：印刷 PDF `Lucerna-VOL2.pdf` 32,555,491 B，sha256 `f315aef01943e344cb145448fafbd43554c04f2781cf33ea3ace070ea34a194e`，8 页（1462.5×2025 pts）；网页 PDF `Lucerna-VOL2-web.pdf` 3,549,551 B，sha256 `de4b0e153d0984f1e19be45025652ddcb922058c1689d9052e648a7d589c8267`，8 页（1400×1938 pts）。与 KIT §1 逐字节一致。
- SVG sha 与卡片 sha 与 KIT §1 全 8 页一致（校对前快照 `work/hashes-before.txt`，校对后复核差分空，见 §13）。

## 1. 冻结：核心基线 8/8 逐字节 + 韩语正文零删失

- 核心基线：把核心 `orig/` 拷到校对员自有 scratch（`work/core-copy/`，OUT 重定向到 scratch）重跑，8/8 与在售核心 SVG 字节一致；分版构建树拷到 `work/build-copy/` 重跑，8/8 与交付 SVG 字节一致。核心在售 SVG 哈希与构建员 KIT §3 记录逐一一致，未变。
- `freeze.py diff`（核心 SVG vs 分版 SVG）：P1 +20/−19、CJK 1462→1339；P2 +44/−39、1612→1360；P3 +34/−31、1524→1346；P4 +28/−25、1232→1074；P5 +38/−35、1433→1234；P6 +23/−19、1276→1136；P7 +40/−40、1365→1046；P8 +176/−169、2496→1238。与构建员声称逐页一致。
- 新增 CJK：全刊仅 7 个，全部在 P7：울×1、에×2、서×2、났×1、만×1；其余 7 页均为 0。逐字核实：7 音节 = 葡语诊所注释 1 的 `«에»` + `«에서»`（에×2、서×1）与注释 4 的 `«서울에서 만났어요»`（서×1、울×1、만×1、났×1）。P7 渲染原文为证：
  - 注释 1：`Vai-se com «에»; «에서» é o lugar da ação.`
  - 注释 4：`Use uma só partícula: «서울에서 만났어요».`
  - 均为葡语注释内对韩语词的引用，非未本地化残留，按 README #3 裁定合法。韩语正文其余部分零新增、零删失。
- 汉字（U+4E00–9FFF）：分版 8 页渲染文本中均为 0（构建员“Han 0”属实）。
- 桥接词：SVG 渲染文本、KIT、ABSTRACT、构建代码（build 树全部 .py/.json/.md）中 `桥接 / bridge / Bridging / ponte / Ponte` 均为 0 命中。
- P7 词框目标语定义句逐字冻结：核心 content7 的全部韩语定义正文（A2 입동/월동、B1 D-日计数、B2 예보 읽는 법、句型框、诊所韩语行）在分版 P7 渲染中逐字存活；仅 gloss 本地化（见 §3）。P7 诊所中文说明行、中文 gloss 被葡语说明行替换，属讲解层替换，非定义句改动。

## 2. 登记展开：150 题连续，级别/页分布/题型 = 核心

- 自有 scratch 重跑登记（run.py 输出 REGISTRY STATS，分版与核心各跑一次，结果相同）：
  - 总数 150；页分布 10/18/18/18/18/18/12/38；级别 A2 51 / B1 72 / B2 27。
  - 题型：完成句子 48、单选 52、词汇配对 16、完形单选 13、造句 8、句型转换 4、判断 4、翻译 4、写作 1（与任务所给核心题型名一一对应：完形=完形单选，变换=句型转换）。
  - 零 FLOW OVERFLOW / HEAD TOO WIDE。流量终值与 KIT §7 逐一核对一致（P1-headline 1413/1828、P1-weekend 2094/2290、P1-quiz 2521/2540、P2-feature 1417/1540、P2-ex 2258/2580、P3-feature 1290/1560、P3-ex 2234/2580、P4-feature 1022/1180、P4-ex 2002/2580、P5-feature 1268/1560、P5-ex 2256/2580、P6-feature 1119/1180、P6-ex 2195/2580、P7 三栏 1062/1029/1059、P7 col3 1746.94、P7 teaser 2520.94、P8-ex 463/1252、P8-keys 2425，均 < 各自 bottom）。

## 3. gloss 口径裁定（重点，两种口径都实测）

定义（本报告内固定使用）：

- **口径 V（词汇 gloss）**：`gloss()` 全部调用 + content7 的 `glossline()` 词框 gloss（真正的词汇条目）；content12/34/56 的 `glossline()` 练习说明行不计入（它们是指令，不是词条）。
- **口径 F（全量渲染页口径）**：口径 V + content12/34/56 的 17 条练习说明 glossline（每条计 1 段）；content8 的写作题 f-string 说明行不计（无 `·`，非词条，与 ko-fr 校对处理一致）。按 p.save 映射到渲染页。

实测（核心与分版在两种口径下逐项完全相等）：

| 口径 | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | 合计 |
|---|---|---|---|---|---|---|---|---|---|
| V（词汇）SVG 分组 + AST | 5 | 16 | 13 | 7 | 12 | 8 | 6 | 0 | **67** |
| F（全量）= V + 说明行 | 5 | 19 | 16 | 10 | 16 | 12 | 6 | 0 | **84** |

- 口径 F 的渲染页分布 5/19/16/10/16/12/6/0 与 ko-de、ko-fr 校对的渲染页口径实测一致；其中 SVG 实测：gloss 盒逐页 [5,16,13,7,12,8,0,0]（核心=分版，盒内行拼接后按 `·` 切分），P7 词框 glossline 3 段×2 项 = 6（核心=分版），说明行 P2 3、P3 3、P4 3、P5 4、P6 4 = 17（核心=分版）。
- 词头渲染存活：口径 V 的 67 个韩语词头（去重后亦 67）在分版渲染中全部存活，**67/67**，0 缺失；包括跨行不断的 `하나가 되다`（P4 盒内同一 `<text>` 行内连续出现）。
- **与构建员 66 的分歧（非阻塞观察，见 §13）**：按构建员自己陈述的口径 V（content12 21、content34 19、content56 20、content7 6）复算，content12 21 ✓、content56 20 ✓、content7 6 ✓，但 content34 实为 20（P3 盒 4+3+3+3=13，P4 盒 4+2+1=7），其中单项盒 `Nota — 예상 = previsão.` 在渲染中确实存在且词头存活。构建员的 19 应为漏计该单项盒的算术 slip，口径 V 可复现总数为 **67 而非 66**。66 与 84 的差距本质是口径差（17 条说明行），不是矛盾；纸面（核心=分版、逐项相等）正确，故不以此判 NOT PASS。跨版 KIT 的 84/66 定义统一问题只记录，由主线决定是否修订 README #21；本校对不擅自“纠正” KO×DE KIT。

## 4. P8 比较：显式双路径、--total 150（p8.py 新版）

- 路径 1（`--core-dir / --edition-dir --target ko`）与路径 2（`--core-p8 / --edition-p8`）结果完全相同：核心 150 noted，分版 150 noted，**status CLEAN，missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138]**。日志与 JSON 存于 `work/p8-path1.json`、`work/p8-path2.json`。
- keydiff 逐项从印刷行裁定：
  - **137（真 E 改向）**：分版印刷行 `137. O dia 7 de novembro é Ipdong. — Veja a pág. 1`（P8 y=2029）。核心对应行为中文 key `11月7日是立冬。— 对照第 1 版`，改向成立。
  - **138（真 E 改向）**：分版印刷行 `138. Faltam 12 dias para o exame. — Veja a pág. 5`（P8 y=2058）。核心对应行为中文 key，改向成立。
  - **139/140（无 keydiff，韩语 key 字节冻结）**：`139. 특별 조치는 11월 19일에만 적용돼요. — Veja a pág. 6`；`140. 저는 토요일에 내장산에 단풍을 보러 가요. — Veja a pág. 3`；与核心韩语 key 部分字节一致，仅注释本地化。
  - **150（器械行，非 keydiff）**：`150. ✓ O modelo está na seção H desta página (157 caracteres)`。
- P8 注释纯葡萄牙语核查：分版 P8 全部注释为葡语；韩语出现仅限冻结的组标题（`— 제N면 —`）、练习题干/key、词头+葡语 gloss（如 `김장=kimchi para o inverno a`、`O passado de 이기다 é 이겼어요`）；新增字符串中无汉字/假名/西里尔字母；英/法/西/德功能词残留扫描 0 命中（`das/por` 命中均为葡语本身的缩合与介词，属误报排除）。
- P8 结构：38 项（A 8、B 8、C 4、D 4、E 4、F 4、G 5、H 1），与核心一致；印刷笔记集 150/150。

## 5. 金句：8 句逐字连续、页签正确，全版频次 = 核心

| 韩语句 | 葡语译文（P7） | 页签 | 全版频次（核心=分版） |
|---|---|---|---|
| 11월 7일은 입동이에요 | O dia 7 de novembro é Ipdong. | 1면 | 5（P1 3、P7 1、P8 1） |
| 절정에 가까운 주말이라고만 말할 수 있어요 | Só se pode dizer: um fim de semana perto do auge. | 1면 | 2 |
| 김장은 겨울 내내 먹는 김치를 담그는 일이에요 | Kimjang é conservar kimchi para o inverno. | 1면 | 4 |
| 수능까지 17일 남았어요. 오늘이 D-17예요 | Faltam 17 dias para o exame. Hoje é D-17. | 2면 | 2 |
| 낮은 길은 더 늦게 물들어요 | Os caminhos baixos ficam vermelhos mais tarde. | 3면 | 2 |
| KIA 타이거즈가 LG 트윈스를 3연승으로 이겼어요 | O KIA venceu o LG Twins com três vitórias seguidas. | 4면 | 2 |
| 온 나라가 수험생을 응원해요 | O país inteiro torce pelos candidatos. | 5면 | 2 |
| 날짜를 먼저 보세요 | Olhe primeiro a data. | 6면 | 2 |

- 计数方法：每页渲染文本去空格后统计（可还原跨行断句），核心与分版逐页分布亦相同。P7 金句表 8 句均以 `「…」` 括注 + 葡语译文 +（N면）页签出现，与 KIT §8 一致。

## 6. 几何：canonical 审计 + 补充扫描 + 端点

- Canonical `occlusion_audit.py`（自检 6 类 planted 全部触发、clean 对照静默）：分版 **0 flags**、核心 **0 flags**、NEW vs 核心 **0**。JSON 存于 `work/occlusion-ed.json`、`work/occlusion-core.json`、`work/occlusion-new.json`。
- 补充扫描（`audit_extra.py`，在分版 SVG 副本 + 校对员自有 wrap-spy 日志上重跑）：ADVANCE 全页右缘扫描（内框 x=1910）**0 flags**；全页框线扫描 **0 flags**；同基线扫描（0.6 px 容差）**0 flags**；P6 图表标签基线锚定墨迹覆盖：全部标签 **0.0%**（门限 <30%），最差 0.0%。
- 韩语孤儿扫描（校对员自有 spy 重跑，943 wrap calls，spy SVG 8/8 与交付字节一致）：行首 NO_START **0**、≥3 音节尾中词断裂 **0**、1–2 音节尾 **0**，全部为词界断裂。渲染行窗口复核（连续渲染行、间距窗口 10–45 px、同栏）：**658 对**，真 NO_START 集（svglib `NO_START = "。、，．！？：；）」』】ー…‥・)]}〉》.,!?%:;"`，其中 ・ 为 U+30FB，不含 U+00B7 的 `·`）行首 **0**。另见 §13 非阻塞观察：5 处行首 `·` 均为选项/ gloss 换行续行分隔符，非韩语散文孤儿标点。
- 端点（均 <2540）：P8 key-flow 终值 2425（run 日志 `flow[P8-keys] ended col 3/3 y=2425 (bottom 2540)`，即末 key 基线 2408.94 + 行距）；P8 各列 key 基线最高 **2530.3 / 2516.7 / 2514.9 / 2408.9**（x=65/527/989/1451 列实测，与构建员声称逐值一致，最小余量 9.65 px）；P7 预告末端 2520.94（预告正文基线 2486.94 + 34 的沿用口径；墨底 2489.69，余量更大）；P1-quiz 流量终值 2521/2540。
- P1 简讯 `(6면)` 碎片：渲染于句行 `11월 2일은 D-17, 7일은 D-12예요. (6면)`（y=2218.8），无孤立 `(6면)` 行；P1 另有一处裸 `6면`（x=1473, y=1526）为目录页码签，与核心同坐标同文，属正常家具。

## 7. 来信框几何重点（实测，非采信）

- 分版来信框 rect：(1451, 1230.44, 434×516.5)，框底 = **1746.94**。征集句行 1 `Envie sua carta e seu melhor texto da pág.` 基线 1736.33，墨底 **1741.33**；框边 1746.94；行 2 `8!` 基线 1764.73，墨顶 **1749.73**。即行 1 墨底 < 框边 < 行 2 墨顶，框边穿入行间空隙，无越框、无压字，canonical 审计 BOXTITLE 0 旗；金句分隔线 y=1776.94，距行 2 墨底（1764.98）**11.96 px**。卡片目视亦确认：行 1 在框内，`8!` 在框外、线上有空隙。
- 核心侧该几何属实（只报告，不重开核心）：核心来信框 rect (1451, 1230.44, 434×508.5)，框底 1738.94；核心末行 `承诺顺延至 VOL.3。` 基线 1764.73，墨底 1766.73，**悬出框底 27.79 px**（构建员称“约 26 px”，墨迹口径实测 27.8 px，量级一致）；该末行墨底距核心金句线（y=1768.94）仅 2.21 px，未压线。跨版注意事项：核心若日后修框高公式，框边与金句线将联动——本版的穿隙权宜届时需随核心重算，本校对不擅自改核心。

## 8. 家具三方对照（W45 核心 / W43 同配对 / 本版，W43 优先）

| 槽位 | W45 核心 | W43 ko-pt | 本版（实测） |
|---|---|---|---|
| 刊头 | `Lucerna`，无冠词，168 pt，y=262 | 同 | `Lucerna`，无冠词，168 pt，y=262 ✓ |
| 副标题 y | 372 | 366 | 366 ✓（从 W43，非核心值） |
| 徽记 | — | y=394，20 pt，粗体 700，BRICK `#a4553a`，sans | y=394，20 pt，700，`#a4553a`，sans，字符串与 W43 逐字相同 ✓（未抄 ko-en 的 17 pt olive） |
| 规则 y | 392 / 401 | 412 / 421 | 412 / 421 ✓ |
| 暗带 rect y | 424（高 118） | 433（高 118） | 433（高 118）✓ |
| 带文 y | 478 / 522 | 487 / 531 | 487 / 531 ✓ |
| 页脚 | `Lucerna · 韩语周报 VOL.2 · LUCERNA KOREAN WEEKLY`，基线 2624 | VOL.1 式 | `Lucerna · SEMANÁRIO COREANO VOL.2 · TEXTOS EM COREANO · EXPLICAÇÕES EM PORTUGUÊS`，基线 2624，8 页全验 ✓ |
| 页码行 | `제 N 면 / 총 8 면` | `Página N de 8` | `Página N de 8`，8 页全验，基线 2624 ✓ |
| 顶带葡语段 | — | `Toda semana` | 相同 ✓ |
| gloss 前缀 | — | `Nota — ` | `Nota — ` ✓ |
| 带标题 | 생활 / 문화 / 스포츠 / 청년 / 깊이 읽기 / 말 공부 / 시험과 답 | 生活 · Vida cotidiana 等 | 생활 · Vida cotidiana、문화 · Cultura、스포츠 · Esporte、청년 · Jovens、깊이 읽기 · Leitura aprofundada、말 공부 · Língua、시험과 답 · Teste e respostas ✓ |
| 练习头/右行、P1 quiz 右行、P8 头/右行、目录 P8 级别 `Todos`、P7 带副 `언어 포커스 · 세 가지 레벨, 세 가지 주제 · Três níveis, três temas`、P7 glossline `=` 式、葡语数字格式（千分点 551.864 / 1.312 / 3.271 / 27.000， prose 小数逗号 415,5 mm）、instr 标签映射、P8 带副韩语独留 | — | W43 式 | 逐项与 W43 相同 ✓ |
| P6 判断题说明 | 韩语 맞다/틀리다措辞 | `Se for verdade, escreva O; se for falso, X.`（W43 的 key 为 O/X） | `Se a frase estiver certa, escolha 맞다; se estiver errada, 틀리다.`——与本期 key 一致（P8 97 틀리다 / 98 맞다 / 99 틀리다 / 100 맞다，选项亦为 맞다/틀리다），非照抄 W43 的 O/X ✓ |

## 9. 读者来信角

- 韩语例信逐字冻结：`「안녕하세요. 저는 대학생이에요.` … `와도 따뜻하게 지내고 싶어요.」 — 독자 편지의 예`，与核心逐行字节一致；无编造人名、信件、引文。
- 葡语延期披露（逐字摘录，含 3 事实 + VOL.3 承诺）：
  - 短注：`Exemplo da redação, não é uma carta de verdade.`
  - 披露：`Até o fechamento, não chegaram cartas de verdade nem os melhores textos da pág. 8. O exemplo fica; a promessa anterior vale para o VOL.3.`
  - 3 事实：(1) 截至截稿未收到真实来信；(2) 未收到最佳 P8 文本；(3) 示例保留、前约顺延至 VOL.3。VOL.3 承诺明确。
- 征集（明确祈使，逐字）：`Envie sua carta e seu melhor texto da pág. 8!`——祈使动词 Envie；字面同时覆盖**来信**（sua carta）与**最佳 P8 文本**（seu melhor texto da pág. 8），裁定范围充分。
- teaser 行不计作征集：teaser（`다음 주 · Na próxima semana (VOL.3)`，y=2446.94）在金句栏之后、独立于来信框；征集句在来信框内（y=1736.33/1764.73），两者分开计数。
- VOL.3 预告正文冻结：`다음 주에는 김장이 한창이에요. 수능까지 일주일이 남았어요. 한능검 시험이 가까워져요. 플레이오프와 한국시리즈 소식도 전해요. 여러분의 편지와 8면 쓰기 우수작도 실어요. 기대해 주세요!` 与核心逐字一致；其中 `여러분의 편지와 8면 쓰기 우수작도 실어요`（来信与 P8 写作优作）与来信角承诺一致，两处承诺均须在 VOL.3 兑现。

## 10. 计数 / 范文 / 图片 / 摘要

- 登记展开见 §2（150 连续，级别/页分布/题型 = 核心）。
- 范文：P8 H 区范文 `나의 겨울 준비는 김장부터 시작해요. … 겨울 준비가 끝나면 마음이 든든해져요.` 与核心逐字一致，去空格 **157 字**（印刷指令 150–200자 范围内）；P8 器械行亦标 157 caracteres。
- 图片 payload 逐页 = 核心（双哈希口径：base64 文本 sha256 前缀 + 解码 JPEG sha256 前缀）：
  - P1 1 张 `535fff46b7ce / 6f7f33ed8f`；P2 1 张 `e66d2b455ec6 / 96a6a19b61`；P3 2 张 `e266b6ee1a87 / 158ea3a0e8`、`5bea45d1f81e / 214cc390ac`；P4 1 张 `1a7e7d6d5ffc / 18ad8ae06f`；P5 1 张 `6a1bab177d54 / 35e7dc69d4`；P6/P7/P8 0 张。分布 1/1/2/1/1/0/0/0。
  - 署名在页且为 Commons API Artist 字段原文：P1 lumoplank CC0、P2 wizdata CC0、P3 Udonhan1992 CC0 + Paul Cézanne PD、P4 Bain News Service PD、P5 Gary Todd CC0；P1/P2/P3/P5  captions 含 `자료 사진`（文件照片）注；P4 署名行与核心逐字相同（`사진: Bain News Service — Public domain (Wikimedia Commons)`，分两行渲染），P4 正文 `20세기 초 미국의 야구팀` 已表明为旧照片。无新图。
- ABSTRACT：葡语单行（仅尾换行），无 ASCII 双引号；含真实主题关键词（Ipdong、folhagem de outono 末周、kimjang 开端、exame 倒计时、exame de história 报名、beisebol de outono）与学习者检索短语（`aprenda coreano lendo notícias em coreano, do nível A2 ao B2, com 150 exercícios`）。全文：`Lucerna Semanário Coreano VOL.2: a semana do Ipdong, o último fim de semana da folhagem de outono, a abertura do kimjang e a contagem regressiva para o exame, com inscrições para o exame de história e notícias do beisebol de outono — aprenda coreano lendo notícias em coreano, do nível A2 ao B2, com 150 exercícios.`

## 11. 网页版 PDF 渲染抽查（fr-en 噪声教训后的必查项）

- 方法：新网页版 PDF 用 pdftoppm 逐页渲染（72 dpi 全 8 页 + 144 dpi p1/p8），与对应卡片（1950×2700 PNG）缩放到同尺寸后逐像素比对；另做空白底色区差分与 8×8 分块均值分析，并目视 p1/p8 网页渲染图。
- 全 8 页下采样差（72 dpi，1400×1938）：meanAbs 7.65–9.60，>30 差像素占比 7.12%–10.07%，无离群页（p1 9.60/9.18%、p2 9.22/9.29%、p3 8.99/9.25%、p4 7.87/7.91%、p5 8.47/8.62%、p6 7.83/7.86%、p7 7.65/7.12%、p8 9.11/10.07%）。
- p1/p8 全分辨率差（144 dpi，2800×3876）：p1 meanAbs 7.53、>30 占比 7.92%；p8 meanAbs 7.79、>30 占比 8.98%。与下采样同一量级。
- 噪声排除：空白底色区（卡片底色 247/241/226 附近 ±15）差分仅 meanAbs 3.53（p1）/ 3.68（p8），>30 占比 1.81%/2.29%，属 JPEG q85 底噪 + 重采样；分块均值最小 1.0–1.4（空白块），最大 21.9–22.1（图文密集块），呈图文边缘驱动分布，非全页均匀噪点。p1/p8 网页渲染图目视干净、可读，与卡片内容一致。
- **结论：无噪声页，不构成阻塞项。** 残差量级由网页 PDF 的 JPEG q85 压缩与卡片 PNG→JPEG 尺寸重采样解释，8 页均匀，无单页异常。

## 12. 核心事实债处理（只核实继承，不擅自扩围）

本版在下列核心债点上的措辞与核心一致（韩语正文冻结；葡语注释为翻译，不新增主张）；核心事实债本身不判为本版阻塞项：

- 韩国大赛 11 月 2 日开赛日或因雨顺延：P4 韩语正文冻结句 `플레이오프가 하루 밀렸기 때문에 11월 2일 시작이 그대로인지는 KBO 발표를 확인해야 해요.`（因顺延一日，11 月 2 日开赛是否如期须以 KBO 公布为准）——纸面自带对冲措辞，非断言；P8 #56/#63/#126 注释（`O kt espera na Série Coreana` 等）为翻译，无新增赛果主张。
- 10 月 26 日季后赛 G1 结果未知：P4/P8 仅述 10 月 25 日 G1 因雨延期、改期 10 月 26 日（P8 #54/#126 `O jogo 1 foi adiado pela chuva`），未写 G1 结果；P5 `이 신문이 마감된 10월 26일 현재, 당일의 모습은 아직 알 수 없어요.`（截至 10 月 26 日截稿，当日情形尚不可知）冻结一致。
- Champi 纪录说法已删：全刊 `참피` 仅出现在台风→温带气旋转变语境（10 月 26 日，P4/P8 #55/#60/#64/#144），无纪录主张。
- 立冬/小雪出自日历博客：`소설`（小雪）一词在核心与分版渲染中均为 0 出现；立冬（입동）相关日期/节气表述为冻结韩语正文，葡语注释未追加来源主张。
- 韩史考试细节出自二手：한능검 相关韩语正文冻结；葡语注释为翻译（报名窗口、费用等数字与核心一致；P8 数字核对：核心与分版数字集合经千分符/小数点归一化后完全一致，唯一分版多出的 `300000` 为核心 `30만` 的葡语数字展开，同一数量，非新主张）。
- Commons 图短缺：图片集与署名与核心逐页相同（§10），文件照片注继承核心；无新图、无新署名主张。
- 本版新增核心没有的主张：**无**（新增字符串 355 条全部为葡语讲解层：说明、gloss、带标题、练习头、P8 注释；数字核对见上）。

## 13. 全 8 卡目视 + 非阻塞观察 + 校对前后哈希

- 全 8 卡逐页目视：p1–p8 无重叠、无截断文字、无错位框。P7 来信框见 §7；P3 gloss 盒见下观察 2；P6 表格标签清晰；P8 答案栏读至页脚线干净。
- **非阻塞观察 1（KIT 文字错误，纸面正确）**：KIT §3/§7 的 gloss 66 应为 67（§3 详述：content34 漏计单项 `예상` 盒）。纸面核心=分版逐项相等，故仅作 KIT 文字观察，不阻塞；是否修订 KIT 由主线决定，本校对未改 KIT。
- **非阻塞观察 2（排版微瑕，纸面可读）**：P3 gloss 盒 `Nota — 현장 = no local · 유명하다 = famoso · 맛보다 = provar.` 换行后第二行行首为分隔符 `·`（`· 맛보다 = provar.`，y=1271.175）。`·`（U+00B7）不在 svglib NO_START 集中，非韩语散文孤儿标点；canonical 审计 0 旗；其余 4 处行首 `·` 均为选项换行续行（P3 y=2013.95、P3 y=2364.95、P5 y=2013.95、P6 y=2158.225），属本刊选项分隔排版惯例。均不阻塞。
- **非阻塞观察 3（跨版注意事项，只记录）**：核心来信框高公式少算约 28 px（墨迹口径，§7）；若核心日后修公式，框边与金句线联动，本版穿隙权宜需随核心重算。KO×DE KIT 的 84 定义统一问题亦只记录（§3）。
- 校对前后哈希：交付 SVG×8 + 卡片×8 + 核心 SVG×8 的内容 sha256 差分**为空**（`work/hashes-before.txt` vs 终检）；印刷/网页 PDF sha 与 §0 一致。见 §14 过程披露的 mtime 说明。

## 14. 过程披露（校对员操作失误，如实记录）

- 校对员首次 scratch 重跑时 OUT 重定向路径写错（漏掉 `work/` 一层），导致 edition 与 core 两次 run.py 实际写回了交付目录与核心目录。事后立即用校对前快照复核：**全部 SVG/卡片内容哈希未变**（重跑结果与交付字节一致，仅 mtime 被刷新为 2026-10-28 04:17–04:18 UTC）；随后修正重定向路径，在自有 scratch（`work/build-copy/`、`work/core-copy/`）内重跑，8/8 字节一致，并再次确认哈希差分空。此后一切重跑（spy、审计）均只在自有 scratch/副本上进行，未再写交付/核心目录。
- 本报告的证据文件均在 `hidden_files/w45/ko-pt-proof/work/`（`hashes-before.txt`、`freeze-diff.json`、`p8-path1.json`、`p8-path2.json`、`occlusion-ed.json`、`occlusion-core.json`、`occlusion-new.json`、`audit-extra.log`、`spy-run/spy-wrap.log`、`run-edition2.log`、`run-core2.log`、`webpdf/`）；报告本身不改动任何交付物。

## 15. 阻塞项清单

无。本报告结论为 ZERO PROBLEMS（纸面）；§13 的 3 项均为非阻塞观察，不构成阻塞项。
