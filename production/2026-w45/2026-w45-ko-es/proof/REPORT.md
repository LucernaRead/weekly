# 独立校对报告 — Lucerna Weekly W45 KO×ES（韩语目标 × 西班牙语读者）

**结论：ZERO PROBLEMS**

校对对象：`files/weekly-report-w45-ko-es/`（svg×8、cards×8、双 PDF、WEEKLY-KIT.md、ABSTRACT.txt），
对照：W45 KO 核心 `files/weekly-report-w45-ko-core/` 与 W43 同配对版 `files/weekly-report-ko-es/`（VOL.1）。
本报告只校对、不宣布上架；未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、
未改核心/W43 目录、未清理共享 scratch 目录。全部重跑均在自有 scratch 内完成并重定向 OUT，
原构建树、交付目录、核心目录均未在原地运行写回脚本。

## 0. 开工查重

- 进程 cwd 排查：开工时唯一在途构建进程 cwd 属于 `weekly-report-w45-ko-pt-build`（KO×PT 分版），
  与 ko-es 树无关，不构成 stand down；无任何 cwd 属于 ko-es 树的在途写盘。
- 静默复查：交付物最后写盘 2026-10-28 03:57:26 UTC，复查时已静默 >170 秒且哈希全程不变，安全开工。
- 校对前后哈希 diff：交付物 + 核心 SVG/cards/PDF 全量复核，**diff 为空**（见 §15）。

## 1. 冻结与核心基线

- 核心基线：`tools/freeze.py baseline`（核心构建树 `hidden_files/weekly-report-w45-ko-build`，
  OUT 重定向至本校对 scratch）**8/8 逐字节一致**，核心 SVG 在运行前后复哈希无变化。
  （注：初次误用无 w45 后缀的旧树 `weekly-report-ko-build` 得 0/8，该树实为 VOL.1 旧内容，
  属错误输入而非核心篡改；换正确树后 8/8 通过。核心 SVG SHA 与 KIT §2 逐项一致，
  核心双 PDF SHA 与核心 KIT 一致：print `4b9642d1…`、web `26075ca5…`。）
- 冻结 diff（`tools/freeze.py diff`，本校对新跑）：p1–p7 新增 CJK **0**，p8 新增 CJK **1 个：`절`**。
  - 唯一新增音节上下文（逐字核实）：核心 `104. A — 节气＝一年24个时节`（纯中文注释）→
    本版 `104. A — 절기 = las 24 divisiones del año`。`절기` 为该题冻结韩语词头本身（ko-fr #104 同类），
    其余注释成分为纯西班牙语，非未本地化残留。
  - 韩语正文零删失：全部被替换的含韩语字符串逐项分类完毕——仅四类：家具（页脚/页码/刊头行）、
    韩中配对标题与 gloss 词头（韩语部分在本版对应行中原样保留）、按 W43 同配对先例译为西班牙语的
    练习指示行（glossline，见 §9）、P8 键注（键保留、注译西语）及 E 区改向（§5）。
    无任何纯韩语文章句、题干句被删除。
- P1-headline 末端：本版重跑 `1413/1828` = 核心重跑 `1413/1828`，与构建员声称一致。

## 2. 登记展开（自有 scratch 重跑，与交付 SVG 逐字节一致 8/8）

- TOTAL **150**；页分布 **10/18/18/18/18/18/12/38**；级别 **A2 51 / B1 72 / B2 27**；
  题型：完成句子（Completar）48、单选（Opción múltiple）52、词汇配对（Emparejar）16、
  完形（Texto con huecos）13、造句（Formar una frase）8、变换（Transformación）4、
  判断（Verdadero o falso）4、翻译（Traducción）4、写作（Redacción）1——全部 = 核心。
- 流量终点（重跑日志，零 FLOW OVERFLOW / HEAD TOO WIDE）：
  P1-headline 1413/1828、P1-weekend 2094/2290、P1-quiz 2521/2540、P2-feature 1417/1540、
  P2-ex 2258/2580、P3-feature 1290/1560、P3-ex 2234/2580、P4-feature 1022/1180、P4-ex 2002/2580、
  P5-feature 1268/1560、P5-ex 2226/2580、P6-feature 1119/1180、P6-ex 2283/2580、
  P7 三栏 1092/1029/1059（底 1560）、P7 teaser 见 §6、P8-ex 463/1252、P8-keys 见 §5。
  全部在底线内；与构建员声称值逐项一致。

## 3. 桥接词

SVG 全文 + 构建代码（content*.py、bslib4.py、svglib.py、run.py、render.py、transform.py、
audit_extra.py）+ KIT + ABSTRACT 中，`桥接` / `bridge` / `puente` 三形检索 **0 命中**。

## 4. 几何门禁

- Canonical `tools/occlusion_audit.py`：selftest 通过（6 类 planted 全触发、干净对照静默）；
  本版 **0 flags**、核心 **0 flags**、NEW vs 核心 **0**。
- 补充扫描（audit_extra.py 副本，venv PIL）：全页右缘 ADVANCE 扫描（内框 x=1910）本版/核心
  8 页全 **0**；全页框线扫描本版/核心 8 页全 **0**；同基线墨迹碰撞（0.6px 容差）本版/核心
  8 页全 **0**。
- P6 图表标签基线锚定墨迹覆盖（getmetrics 法）：12 标签本版/核心全部 **0.0%**（门限 <30%）。

## 5. P8（新版 tools/p8.py，SHA 96fc2cfe…）

- `extract --total 150`：核心 150/150，本版 150/150。
- `compare`（显式双路径，--total 150）：**CLEAN，missing=[] extra_count=0 uncertain=[]，
  keydiff=[137, 138]**——与构建员旧版（67df05f1…）结果逐项相同，新版破折号分支未翻出
  任何旧版未见的差异；109 不在 keydiff 中，无 109 式伪影。
- 109 印刷行裁定：本版 `109. 기준 — Las fechas difieren porque los criterios difieren (pág. 3)`，
  键 `기준` 与核心逐字相同，注已本地化为西班牙语。
- E 区裁定（A 113–120、B 121–128、C 129–132、D 133–136、E 137–140、F 141–144、G 145–149、H 150）：
  - 137 题干韩语冻结（`11월 7일은 입동이에요. → ___`，与核心逐字相同）→ 键西语
    `El 7 de noviembre es Ipdong.` + 注 `Compara con la pág. 1`。
  - 138 题干韩语冻结（`수능까지 12일이 남았어요. → ___`）→ 键西语
    `Quedan 12 días para el examen.` + 注 `Compara con la pág. 5`。
  - 139 题干译西语（`Las medidas especiales solo se aplican el 19 de noviembre. →`）→
    键韩语逐字（`특별 조치는 11월 19일에만 적용돼요.`，与核心相同）+ 注 `Compara con la pág. 6`。
  - 140 题干译西语（`El sábado voy a Naejangsan a ver el follaje. → ___`）→
    键韩语逐字（`저는 토요일에 내장산에 단풍을 보러 가요.`）+ 注 `Compara con la pág. 3`
    （注在印刷行上折为两行：`…Compara con la pág.` + 续行 `3`，属自然折行，非缺失）。
  - 150 键缩短：本版 `150. ✓ El modelo está en la sección H (157 caracteres)`，
    对核心 `150. ✓ 范文见本版 H 区（157 字）`：原意（范文在 H 区、157 字）与页/区指向
    （sección H）均保留，仅省去“本版”二字（所指即本期），裁定保留原意、无指向损失。
- P8 注释语言：键区汉字（U+4E00–U+9FFF）**0**；150 条键注中 126 条不含任何韩语/汉字；
  另 24 条含冻结韩语形式引用（词头/动词原形，如 `김장 = kimchi de invierno`、
  `Pasado de 이기다: 이겼어요`），均为被讲解的对象词本身、其余成分为西班牙语；
  含汉字注释 **0 条**，跨族（中文）残留 **0**。此项按冻结词头引用类裁定通过，
  非未本地化残留（与 §1 的 #104 规则同一类）。
- 键区折行续行 2 处（均属自然折行）：124 键注 `…11 de` + 续行 `noviembre`；
  140 键注 `…pág.` + 续行 `3`。

### P8 流末端精确测量（重点，三口径 + 核心同口径对照）

| 口径 | 本版 | 核心 | 与 2540 底线间隙（本版） | 与页脚规则线 2580 间隙（本版） |
|---|---|---|---|---|
| 流光标末端（重跑日志 P8-keys ended） | 2382 | 2351 | 158 | 198 |
| 末基线（键区文本节点最大 y） | 2514.92 | 2514.92 | 25.08 | 65.08 |
| 墨迹底（PIL 基线锚定墨盒最大底，键 38/115 行） | 2518.42 | 2516.67 | **21.58** | **61.58** |

裁定：**没有任何一口径恰为 2540**。构建员所写 “2382/2540” 中的 2540 是 P8-keys 流的
底线限值，不是实测末端；三口径实测最大值 2518.42 距底线 21.58px、距页脚规则线 61.58px，
且 canonical 遮挡旗 0、核心同口径值相等或更低（2514.92 / 2516.67），故无含糊空间：**通过**。

## 6. P7 预告与来信框几何

- P7 预告：实测预告框 rect `(65, 2404.94, 1820, 118)`，框底 **2522.94**（<2540，余量 **17.06px**；
  距页脚规则线 57.06px）；预告正文基线 2488.94、墨迹底 2491.69，框内 31.25px。
  核心同口径框底 2512.94。构建员声称值逐字复核一致（注：2522.94 为框底，非墨迹底）。
- 来信框：实测终版末行 `¡Envíanos tu carta · tu texto destacado!`（20pt，基线 1735.73）
  墨迹底 **1739.98**（`¡` 下降部 4.25px，与构建员诊断 4.3px 一致）；框 rect
  `(1451, 1201.44, 434, 547.5)`，框底 1748.94；**末行墨迹与框底间隙 8.96px，无越框**。
  代码核实：本版 content7.py 来信框 lh 尾项 `+ 65`（注释明示“+39 total slack”），
  核心为 `+ 26`，差值 **+39** 属实。框底至 P7 短语区规则线（y=1778.94）间隙 **30.00px**，
  与核心（框底 1738.94 → 规则线 1768.94）同为 30px。
  （核心侧观察，见 §14：核心自身末行中文披露行超出其框底，本版不继承此问题。）

## 7. gloss（口径明示）

- **源分组口径**（构建员所称 24/26/28/6，合计 84，另 content8 glossline 1 项）：
  本校对从构建源码逐字面量重算，规则为“含 `·` 的 gloss()/glossline() 字面量按 `·` 切分计数，
  不含 `·` 的计 1”：content12 **24**（gloss 段 21 + 指示行 3）、content34 **26**（20 + 6）、
  content56 **28**（20 + 8）、content7 **6**（3 行 × 2 段）、content8 **1**，合计 **85**；
  本版 = 核心，逐文件一致。
- **渲染页口径**（从核心渲染建立，要求本版 = 核心）：gloss 框（`Nota — ` / `译注｜` 前缀框）
  按页逐框连接折行后按 `·` 切分 + P7 词框行（3 行 × 2 段）：
  **p1 5 / p2 16 / p3 13 / p4 7 / p5 12 / p6 8 / p7 6 / p8 0，合计 67 项**；
  本版与核心**逐页、逐框段数全等**（框数分布 p1 1、p2 5、p3 4、p4 3、p5 4、p6 3）。
  另有 17 条 p1–p6 练习指示 glossline 与 1 条 p8 写作指示 glossline 属指示字符串，不计入 67 项。
- 渲染前缀：本版 `Nota — `（p1–p6），与 W43 同配对版前缀一致；方法名保留
  `gloss()`/`glossline()`（W43 改为 `expl()`，渲染前缀同为 `Nota — `，无渲染差异）。

## 8. 金句

8 句逐字连续且页签正确（韩语原文 + 西班牙语译文 + `(N면)` 标签均在 P7 在位，
译文与 KIT §7 逐字一致）；全版频次（去空白连接计数）**本版 = 核心 = 5/2/4/2/2/2/2/2**：
`11월 7일은 입동이에요` 5、`절정에 가까운 주말이라고만 말할 수 있어요` 2、
`김장은 겨울 내내 먹는 김치를 담그는 일이에요` 4、`수능까지 17일 남았어요. 오늘이 D-17예요` 2、
`낮은 길은 더 늦게 물들어요` 2、`KIA 타이거즈가 LG 트윈스를 3연승으로 이겼어요` 2、
`온 나라가 수험생을 응원해요` 2、`날짜를 먼저 보세요` 2。
每句在其标签页均有命中。P7 词框目标语定义句逐字冻结、仅 gloss 本地化：
P7 非来信栏节点多重集差异仅为金句译文、词框 gloss 行、题型标签（填空→Completa）与
预告标题，无任何韩语定义句变动。

## 9. 家具三方对照（W45 核心 / W43 同配对 / 本版；W43 优先于 README #20）

| 项目 | W45 核心 | W43 ko-es | 本版（实测） |
|---|---|---|---|
| 刊头 | 无冠词 | — | 无冠词 `Lucerna` ✓ |
| 徽章 P1 | 无 | `TEXTOS EN COREANO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`，y=394，20pt，x=975 | 同串、y=394、20pt、x=975 ✓ |
| 副标/规则/暗带/带线 P1 | 副标 372、规则 392/401、带 424、带线 478/522 | 副标 366、规则 412/421、带 433、带线 487/531 | = W43（副标 366、规则 412/421、带 rect y=433、带线文本 487/531）✓ |
| 页脚（8 页，基线 2624） | 韩文 | `Lucerna · SEMANARIO COREANO VOL.1 · TEXTO EN COREANO · EXPLICACIONES EN ESPAÑOL` | VOL.2 同式，8 页全 ✓ |
| 页码行（8 页） | `제 N 면 / 총 8 면` | `Página N de 8` | **8 页全部 `Página N de 8`**（R7 补映射后，逐页核实）✓ |
| P1 刊行 | 韩文 | `SEMANARIO COREANO · VOL.1 · …` | `SEMANARIO COREANO · VOL.2 · 입동 · 단풍 · 김장` ✓ |
| 顶栏 | 韩文 | `매주 한국어로 · Cada semana · 한국 사람이 읽는 한국어를 읽어요` | 同串 ✓ |
| 栏目标题 | 韩文 | 생활·Vida cotidiana、문화·Cultura、스포츠·Deportes、청년·Juventud、깊이 읽기·Lectura profunda、말 공부·Lengua、시험과 답·Test y respuestas | 逐页在位 ✓ |
| 练习头/题型/指示标签 | 韩文 | `연습 · Ejercicios pág. N`；Completar、Opción múltiple、Emparejar、Texto con huecos、Formar una frase、Transformación、Verdadero o falso、Traducción、Redacción；Completa、Forma la frase、Traduce、Escribe、Reescribe、Relaciona | 注册表题型与 SVG 指示标签逐项在位 ✓ |
| P8 头 | 韩文 | `답 · Respuestas — ordenadas por página, busca el número`；右行 `Cada respuesta con una nota breve en español · ✓ = ejercicio con modelo`；分隔符韩文（`— 제N면 —`） | 同式 ✓（分隔符仍韩文） |
| P7 标题 | 韩文 | `실수 병원 · La clínica de errores`、`이번 주의 틀 · La frase modelo`、`독자의 편지 · Cartas de los lectores`、`이번 주의 문장 · Frases de la semana (textuales, de este número)`、预告 `다음 주 · La semana que viene (VOL.3)`（正文仍韩文） | 同式 ✓ |
| 副标措辞（`이번 주의 말`） | `이번 주의 말 · 本周词语`（y=1660，x=1451，22pt） | `이번 주의 말 · La palabra de la semana`（同坐标同字号） | `이번 주의 말 · Palabra de la semana`（**同坐标同字号**，仅措辞微差，非家具尺寸偏差）✓ |
| 图片说明/署名/日期 | 韩文 | 说明仍韩文；署名仍韩文（`Lucerna 편집부 · 읽기 레벨: A2`、`VOL. 1 · 제1호`） | 说明仍韩文；署名仍韩文（VOL.2 式，`VOL. 2 · 제2호` 在位）✓ |

- 练习指示行译西语（`Lee los textos…`、`Pon la palabra…`、`Responde con…` 等）与 W43
  同配对版已刊行先例一致（W43 p2–p6 同式西语指示行已核实），属家具层而非正文删失。

## 10. 读者来信角（逐字摘录）

- 韩语例信（与核心逐字相同，零编造）：
  `「안녕하세요. 저는 대학생이에요. 토요일에는 내장산에 단풍을 보러 가요. 일요일에는 집에서 김장을 도와요. 겨울이 와도 따뜻하게 지내고 싶어요.」 — 독자 편지의 예`
  短注：`Ejemplo editorial, no una carta real.`（标明为编辑部示例，非真实来信）。
- 韩语披露（与核心逐字相同）：
  `알려요: 이 편지는 편집부가 쓴 예예요. 마감 때까지 진짜 독자 편지와 8면 쓰기 우수작이 도착하지 않았어요. 그래서 예가 실렸고, 지난 호의 약속은 VOL.3으로 이어져요.`
- 西班牙语披露（逐字）：
  `Sin cartas reales ni mejores textos de la pág. 8, la promesa pasa al VOL.3.`
  `¡Envíanos tu carta · tu texto destacado!`
- 范围裁定：**通过**。披露含 3 事实（无真实来信 / 无 p8 优秀文本 / 承诺顺延 VOL.3）
  + VOL.3 承诺 + 明确祈使征集；祈使句字面同时覆盖两类对象——`tu carta`（来信）
  与 `tu texto destacado`（精选文本，即 p8 写作优秀作）。预告行
  （`다음 주에는 … 여러분의 편지와 8면 쓰기 우수작도 실어요.`）为 VOL.3 内容预告，
  依规则不计作征集；征集仅由来信框内祈使句承担。

## 11. 韩语孤儿扫描（窗口 10–45，≥3 音节尾标准，全部散文栏）

- 交付 SVG 直接扫描（本版与核心双侧）：行首 NO_START（含 ASCII 闭符 `)]}〉》.,!?%:;"`）
  **0**；跨行切分候选 **0**（≥3 音节尾 0、1–2 音节尾 0）；源词表 1840 词（构建源码）。
- wrap-spy 独立重跑（自有 scratch 副本，OUT 重定向）：943 条记录、去重 533 条，
  行首 NO_START **0**、切分 **0**（≥3 尾 0、1–2 尾 0）、括号末行片段**仅 1 条**，
  与构建员声称一致（去重数 533 vs 构建员 535 属去重口径微差，门禁计数全同）。
- 唯一孤立括号片段逐项核实：P5 `1,620명)`，基线 **y=1398.55**，本版与核心同坐标；
  前行 `3,271명 — 서울시 할로윈 안전 인력 (이태원`，为冻结 cifras 框行
  `3,271명 — 서울시 할로윈 안전 인력 (이태원 1,620명)` 的自然断点、完整括号数字 token
  （按 ≥3 规则计 1 音节尾），非切词，**非缺陷**。
- 扫描器另标出的短末行（如 P3 打包清单 `물`/`간식`/`카메라`、gloss 框末行、选项行）
  均为完整清单项/选项/gloss 项，非散文切词；本版与核心结构相同，无新增类。

## 12. 计数 / 范文 / 图片 / 摘要

- 登记展开 150 题连续（1–150 无缺号），级别/页分布/题型 = 核心（§2）。
- 范文：P8 H 区范文去空格 **157 字**，本版与核心去空格串**逐字相等**，
  起句 `나의 겨울 준비는 김장부터 시작해요.`。
- 图片 payload 逐页 = 核心（双口径）：base64 体 SHA-256 前 12 位与 KIT §8 逐项一致
  （P1 `535fff46b7ce…`、P2 `e66d2b455ec6…`、P3 `e266b6ee1a87…` + `5bea45d1f81e…`、
  P4 `1a7e7d6d5ffc…`、P5 `6a1bab177d54…`）；解码 JPEG SHA-256 前 12 位亦逐项一致；
  页分布 **1/1/2/1/1/0/0/0**。Credit 在页且取 Artist 字段原文：
  P1 lumoplank CC0、P2 wizdata CC0、P3 Udonhan1992 CC0 + Paul Cézanne Public domain
  （`그림: Paul Cézanne — Public domain (Wikimedia Commons)`，折行续 `Commons)`）、
  P4 Bain News Service Public domain、P5 Gary Todd CC0。
- ABSTRACT：西班牙语单行（293 字节，末尾换行），无 ASCII 双引号，无汉字；
  含真实主题关键词（Ipdong 周、红叶尾声、kimjang 季开端、高考倒计时、韩史考试报名、
  秋季棒球、150 题 A2–B2）与学习者检索短语 **`aprender coreano leyendo`**。

## 13. 核心事实债继承核查（只核实继承，不扩围；核心侧问题不判为本版阻塞项）

- 11 月 2 日开赛雨延变动措辞：`발표된` 措辞在位（P4 `발표된 일정은 11월 2일부터`、
  `한국시리즈: 11월 2일 발표 (변경 가능)`、`KBO 발표를 확인해야`，本版 = 核心逐字，
  仅练习行 y 坐标因版式平移）+ 截稿注在位（P4 `이 신문은 10월 26일에 마감했어요`）。
- 季后赛 G1 结果截稿时未知：本版未印比分；P4 明示 `결과 없는 경기 — 아직 열리지 않은 경기는 점수가 없어요. 그래서 이 신문은 결과만 전해요.`，
  练习问原因（选项为雨/雪/停电），无比分主张。
- Champi 纪录断言：`챔피` 全刊 **0 命中**（本版与核心同），已删断言未复活。
- Ipdong/Soseol 历法来源：本版未新增任何核心没有的日历主张（`11월 22일` 本版与核心均为 0 命中；
  `절기` 框架与核心一致）。
- 韩史考试细节：`한능검` 21 命中，本版与核心韩语文本逐字相同（仅家具西语行不同）。
- Commons 图短缺诚实标注：P2 ssam 照说明 `쌈 채소와 쌈장. 겨울 식탁의 한국 음식이에요. 김장 사진이 아니에요.`
  （明确非泡菜照）+ wizdata CC0 credit，本版 = 核心逐字。
- 本版新增主张扫描：freeze 新增串中含数字者逐项核对，全部为核心数字的西语翻译
  （日期、551.864、1.312、3.271、415,5、300.000、27.000、D-17/D-12 等）或家具行；
  **无核心没有的新事实主张**。国际政治 0 项；韩国国内政治（高考措施、考试管理）符合既定规则。

## 14. 网页版 PDF 渲染抽查与全 8 卡目视

- 新网页版 PDF（3,579,175 B，SHA `8eea982b…`，8 页）逐页 pdftoppm 渲染并与对应卡片比对：
  全 8 页下采样差 + p1/p8 全分辨率差。8 页差异全部落在同一窄带
  （原分辨率均值 5.36–6.87、>40 像素占比 4.4–5.6%；半分辨率均值 3.69–4.69），
  属 JPEG q85 + 缩放伪影，**无离群噪声页**；p1/p8 全分辨率目视干净，与卡片一致。
- 印刷 PDF：32,555,388 B，SHA `d8ccaea5…`，8 页，与构建员声称值逐字一致。
- 全 8 卡目视：无重叠、无裁切、无缺图，页脚/页码行逐页正确，P6 表格 12 标签全清晰，
  P7 来信框内祈使句距框底有可见余量，P8 键区完整至 150。**零视觉缺陷**。
- 汉字检查：本版全部 8 页文本节点汉字 **0**、ASCII 双引号 **0**（核心汉字 2136，均为已替换的中文讲解层）。

## 15. 非阻塞观察（纸面正确，KIT 文字问题，不阻塞）

1. KIT §5 冻结串数（p1 +20/−19、p2 +43/−38、p3 +33/−30、p4 +27/−24、p5 +36/−34、
   p6 +23/−18、p7 +35/−35、p8 +171/−168）为 **R7 页码行补映射前的旧计数**（计数口径为含重复的串数和）；
   本校对新跑终版为 p1 +21/−20、p2 +44/−39、p3 +34/−31、p4 +28/−25、p5 +37/−35、
   p6 +24/−19、p7 +36/−36、p8 +172/−169，差值恰为每页一对页码行（韩文→`Página N de 8`）。
   终版纸面正确，KIT 数未同步属文字滞后。
2. KIT §6 称新版 p8.py“未采纳”——该陈述仅对构建时成立；当前 `tools/p8.py` 已是新版
   （SHA `96fc2cfe…` 与 KIT 所载新版文件一致），本校对即用新版跑出与旧版相同结论。
3. KIT §5 “P8-keys 2382/2540”中的 2540 是底线限值而非实测值（实测见 §5 三口径表）。
4. 核心侧几何观察（非本版问题，不阻塞本版）：核心 P7 来信框末行中文披露行
   （`承诺顺延至 VOL.3。`，基线 1764.73、墨迹底 1766.73）位于其框底（1738.94）之外、
   规则线（1768.94）之前——核心自身框高低估约 28px；本版以 +39 slack 与 3 行西语披露
   彻底避开此问题（间隙 8.96px），不继承。

## 16. 证据文件

- 本报告：`hidden_files/w45/ko-es-proof/REPORT.md`
- 冻结 diff：`hidden_files/w45/ko-es-proof/freeze-diff.json`
- 核心基线重跑：`hidden_files/w45/ko-es-proof/freeze-baseline/`（8/8 OK）
- P8 新版：`hidden_files/w45/ko-es-proof/p8-core.json`、`p8-ed.json`、`p8-compare.json`
- 遮挡审计：`hidden_files/w45/ko-es-proof/occlusion.json`；补充扫描：`hidden_files/w45/ko-es-proof/audit-extra.log`
- 自有 scratch 重跑：`hidden_files/w45/ko-es-proof/scratch/rerun.log`（本版，SVG 8/8 逐字节 = 交付）、
  `hidden_files/w45/ko-es-proof/scratch/core-rerun.log`（核心，SVG 8/8 逐字节 = 核心）、
  `hidden_files/w45/ko-es-proof/scratch/spy/`（wrap-spy 重跑）、
  `hidden_files/w45/ko-es-proof/scratch/proof_main.log`、`proof_pass2.log`、`proof_pass3.log`、
  `proof_orphan.log`、`scratch/webpdf/`（网页版渲染页）
- 校对起止哈希快照：`/tmp/koes-proof-pre.sha256`（校对前后 diff 为空）

## 17. 合规声明

本次校对未向 Discord 投递、未向主聊天发送卡片或 PDF、未创建 cron、未接触 weekly-git、
未修改核心目录、W43 目录与共享 scratch 目录；原构建树未在原地运行任何写回脚本。
结论仅为校对结论，不宣布上架。
