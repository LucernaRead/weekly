# 独立校对报告 — W45 KO × NL（目标语言韩语 × 读者母语荷兰语）

**结论：ZERO PROBLEMS — 可交付上架，阻塞项无。**
**校对员：** 独立校对（深度 2，不派生下级代理）。**对象：** `files/weekly-report-w45-ko-nl/`（svg×8、cards×8、印刷 PDF、网页版 PDF、WEEKLY-KIT.md、ABSTRACT.txt）。
**对照：** 核心 `files/weekly-report-w45-ko-core/`、W43 同配对 `files/weekly-report-ko-nl/`、build 树 `hidden_files/weekly-report-w45-ko-nl-build/`（只读；未改动）。
**证据目录：** 本目录 `work/` 下（快照、freeze/p8/occlusion JSON、各复测日志与 scratch 重跑目录）。本校对未碰 weekly-git，未改核心/W43/交付目录与 `tools/` 下任何文件，未清理共享 scratch，未发 Discord，未往主聊天发卡片/PDF，未建 cron，未宣布上架（上架由协调员串行做）。

**非阻塞勘误（与结论分离，见末节 §13）：** 仅 KIT 一处家具行表述失实（“W of O identical”）及 build 侧文档旧注，不涉及任何印张内容，不需重建/重渲染。

---

## 0. 开工查重与冻结快照

- 进程检查：开工时无任何 cwd 属于本版树的写入进程（唯一长驻进程是另一版 fr-es 的校对快照脚本，与本版无关）。交付文件 mtime 为 2026-10-28 04:31–04:53（UTC），核心 SVG mtime 为同日 04:17，均早于开工；随后执行 90 秒静默复查，交付与核心内容哈希零变化，判定为“已完成交付的新鲜 mtime + 静默”，**可以开工，不是 stand down**。
- 快照：开工前记录交付（svg/cards/双 PDF/ABSTRACT/KIT）与核心（svg/cards/双 PDF/ABSTRACT/KIT）全量 sha256（`work/snapshot-before.txt`）；校对结束后复核（`work/snapshot-after.txt`），**差分为空，内容哈希全部不变；校对期间交付与核心 mtime 未刷新**（终态仍为 svg 04:43、cards 04:43–04:44、PDF 04:44、ABSTRACT 04:52、KIT 04:53）。
- 所有重跑一律在自有 scratch（`work/ed-repro/`、`work/core-repro/`、`work/reg-core/`、`work/reg-ed/`、`work/wrap-repro/`、`work/transform-repro/`）中进行并重定向 OUT；绝未在 build 树或交付/核心目录原地跑脚本。

## 1. 冻结（Freeze）— 通过

- **核心基线自有重跑 8/8 逐字节：** `tools/freeze.py baseline` 对规范核心 build（`hidden_files/weekly-report-w45-ko-build/`，经核实与本版 build 的 `orig/` 9 个文件全部逐字节相同）重跑，8 页 SVG 与 shipped 核心逐字节相同（p1 `f1e6913d…f9b5e`、p2 `839dcdd0…6509c1`、p3 `74371179…899b34`、p4 `7f0aed9b…0902`、p5 `68e6ead9…85a3d`、p6 `e7f53e42…90a39`、p7 `ddb4e76c…6594`、p8 `17031514…646401`），且 freeze 工具自检“shipped 核心 SVG 未被该轮改变”。附注：直接以本版 `orig/` 为 `--build` 会因 `orig/` 内无 `assets/` 而在读图处失败——这是 freeze 输入要求（build 目录须含 assets），不是核心缺陷；规范 ko-build 含 assets 且内容与 `orig/` 相同，故基线有效。
- **freeze diff（`tools/freeze.py diff`，`work/freeze-diff.json`）：** 逐页新增/删除字符串 p1 +20/−19、p2 +44/−39、p3 +34/−31、p4 +28/−25、p5 +38/−35、p6 +23/−19、p7 +40/−36、p8 +189/−177；CJK（freeze 口径 `[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]`）核心→本版 p1 1462→1339、p2 1612→1360、p3 1524→1346、p4 1232→1074、p5 1433→1234、p6 1276→1136、p7 1365→1100、p8 2496→1224。**新增 CJK：p1–p7 = 0；p8 恰 {절: 1}。**
- **独立复核（自有 Counter，Hangul+汉字+假名口径）：** p1–p7 新增多重集为空，p8 新增多重集恰 {절: 1}，与 freeze 结论一致（两口径总量略差源于 freeze 另计全角形等字符，新增集一致才是门值）。**汉字 ideograph（U+4E00–U+9FFF）本版 8 页全部为 0**（核心各页为 109/189/124/92/131/75/217/1199，全部来自中文讲解层，已被荷兰语替换）。절为 Hangul 音节（U+C808），不是汉字 ideograph，故 ideograph 计 0 即使计入该引用仍成立。
- **p8 净增 절×1 的出处逐字核实：** 本刊 P7 A2 第 104 题：题号文本 `104.` 位于 (x=137, y=963.1)，题干 `’절기‘는 무슨 뜻이에요? A. 일 년의 24개 시점 ·` 位于 (x=65, y=992.6)，与核心同页同坐标逐字相同（冻结词干）。本版 P8 印刷行 `104. A — 절기 = de 24 seizoenen van het jaar`；该注与 P7 #104 本题的登记注逐字相同（REG 本版 #104 注即此串）。核心 P8 #104 注为中文 `节气＝一年24个时节`（无 절）。多重集层面：절기引入 절+기各 1，但 기因核心 P8 写作 glossline 本地化而同步减少，净增仅 절×1——属“冻结词头引用”例外，有出处、有登记对应，**合格**。
- **交付与 manifest：** `round3-full-sha256.txt` 所列 18 个渲染文件（svg×8、cards×8、双 PDF）在交付目录逐项 `sha256sum -c` 全 OK；印刷 PDF 32,552,178 B sha `dc95ad2c…e10a`、网页版 PDF 3,547,923 B sha `4fa8990c…c99`，与建造员声称值一致。ABSTRACT.txt（318 B、单行荷兰语）与 WEEKLY-KIT.md 不在该 manifest 内（manifest 只含渲染输出），二者 mtime（04:52/04:53）晚于 PDF（04:44）属正常的后渲染文档写入，非“渲染后又动渲染文件”；ABSTRACT 内容另见 §8 末，KIT 工具版本另见 §2/§5（sha 均已核实）。

## 2. P8 — 通过（CLEAN）

- **工具与调用：** `tools/p8.py` sha256 经核实确为 `96fc2cfe…ccc0ca9`（KIT 注明的新版）；以显式双路径调用 `compare --core-p8 核心 p8 --edition-p8 本版 p8 --total 150`（未用 `--core-dir` 形式）。结果：**核心 150 noted = 本版 150 noted，status CLEAN，missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138]**（`work/p8-compare.json`；双侧 extract 各为 150/150）。
- **keydiff 逐项从印刷行 adjudicate（印刷行由 P8 渲染行重建，150 题编号连续 1–150）：**
  - **#137 — E 区真重定向：** 核心 `137. 11月7日是立冬。 — 对照第 1 版` → 本版 `137. 7 november is Ipdong. — Zie blz. 1`。源侧为韩语、答案侧为荷兰语的翻译题，键本身改向读者语，成立。
  - **#138 — E 区真重定向：** 核心 `138. 离高考还剩 12 天。 — 对照第 5 版` → 本版 `138. Nog 12 dagen tot het examen. — Zie blz. 5`。同上，成立。
  - **#139 / #140 — 词干本地化、键冻结（非 keydiff，p8 工具不列为键差）：** 本版印刷行 `139. 특별 조치는 11월 19일에만 적용돼요. — Zie blz. 6`、`140. 저는 토요일에 내장산에 단풍을 보러 가요. — Zie blz. 3`，键与核心逐字相同；其练习题干（P8 上半区）已本地化为荷兰语（`Bijzondere maatregelen gelden alleen op 19 november. → ___` / `Op zaterdag ga ik naar Naejangsan om herfstkleur te zien. → ___`），属反向 E 题（荷兰语干 → 韩语答案），transform 对子亦有此二项。REG 无词干/体字段，故词干核实取自印刷行 + transform 对子，二者一致；自有 REG 比对其他字段差异总数为 0。
  - **#150 — 装置行，非真重定向（性质须写明）：** 印刷行本版 `150. ✓ Het voorbeeld staat in deel H van deze pagina (157 tekens)`、核心 `150. ✓ 范文见本版 H 区（157 字）`——写作题印刷时不印键，只印 ✓ + 装置注，故 p8 工具将其排除在 keydiff 之外。登记表键差异 {137, 138, 150} 中的 150 项是登记元数据（核心键 `(开放题，范文如下)` → 本版键 `(open vraag — het voorbeeld staat hieronder)`，即“开放题”标记本身的本地化），**不是答案键改向**，与 137/138 的真重定向性质不同。登记表键差异恰 {137, 138, 150 装置行} 的声称经自有 REG 比对核实无误（见 §4 登记）。
  - **#109 — 无 artefact：** 本版 `109. 기준 — Andere criteria, andere data (blz. 3)`，键 `기준` 与核心逐字相同；旧工具的 [109, 137, 138] 在新工具下读为 [137, 138]，符合预期。
  - **#115 / #136（R2 定稿注）：** 本版 `115. A — Examen Koreaanse geschiedenis: zaterdag 28 november`、`136. 수험생은 도서관에서 공부해요. — Plaats van de handeling: «에서»`，与 transform.py 内 R2 对子逐字一致（各由 2 行压为 1 行）。
- **P8 注纯荷兰语：** 150 条注的注段（` — ` 之后，#150 装置行除外）汉字 ideograph 总计 **0**；英文残留程序扫描（独立词表 the/and/of/to/for/with/exam/history/answer/question/example/school）唯一命中是 Dutch 词 `week`（`Deze week…` 等 4 条，属荷兰语本词，非残留）；无双空格、无大小写粘连。注段内含 Hangul 的条目（#25–28、43–46、57–64、104、135、141–144 的韩语词头及 #136 的 «에서»）均为冻结韩语词头/语法引用 + 荷兰语讲解，属设计内的双语注格式，不是跨族残留（de-pt 前例的英文残留注情形不存在）。全部 fix 轮改动均在 transform.py 内（见 §7 末的单独复现：transform 自 orig 重建 9/9 文件与 build 逐字节相同）。

## 3. Gloss 口径裁决（重点）— 通过：本版 = 核心，AST 85

- **AST 法（必须用 AST，不得用正则）：** 自有 AST 脚本（`work/s_ast.py`）遍历 `.gloss()`/`.glossline()` 调用、取首参字符串值（f-string 拼常量段，占位符不产生 `·`）、按 `·` 分段计数。结果**核心 orig = 本版 = 85**，分文件 **content12 24、content34 26、content56 28、content7 6、content8 1**，双侧逐文件相等，无未解析调用。
- **正则法 83 属漏计，已定位两处：** 正则 `\.gloss(?:line)\(\s*([^)]*)\)` 在首个 `)` 处截断，恰漏 2 项——(1) content34:227 glossline `Zet de zinnen in de verleden tijd. (Het staat allemaal in dit nummer.)`（括号内子句含 `)`，AST 计 1 项；核心对应串为 `문장을 과거형으로 바꾸세요. (바꾼 문장은 모두 이 신문에 나온 일이에요.)`，同样 1 项）；(2) content8:107 f-string glossline `Schrijfopgave (niet één juist antwoord). Hieronder een voorbeeld van {NCHARS} tekens.`（括号 + f-string，AST 计 1 项；核心对应串为韩语同形句，同样 1 项）。83 = 85 − 2，**83 是正则 artefact，不是差异**。
- **渲染页口径 = 85，双侧逐页逐框相等：** 自有渲染提取（Sans 20.5pt #57523f 文本，按 x 分组、dy≤45 成组，组内拼接后按 `·` 分段；`work/analysis.json` §D）：p1 1 组/5 项、p2 8 组/19 项、p3 7 组/16 项、p4 6 组/10 项、p5 8 组/16 项、p6 7 组/12 项、p7 3 组/6 项、p8 1 组/1 项——**核心与本版逐页、逐组数、逐项数全部相等**，且与 AST 分文件口径交叉一致（content12 24 = p1 5 + p2 19；content34 26 = p3 16 + p4 10；content56 28 = p5 16 + p6 12；content7 6 = p7 6；content8 1 = p8 1）。
- **P8 的 1 项是什么（与 ko-pt 末位 0 的口径差异说清）：** P8 渲染组唯一 1 组 2 行，拼接为 `Schrijfopgave (niet één juist antwoord).Hieronder een voorbeeld van 157 tekens.`（行间拼接吞空格为本分析的拼接方式，渲染行本身无缺空格，见卡面目视），无 `·` 故计 1 项——**即 P8 写作 glossline 本身**。ko-pt 渲染分布末位 0 说明其口径把 content8 的 glossline 排除在渲染 gloss 之外（或其 P8 glossline 未以 20.5pt 灰字渲染）；本版口径把该行计入，且核心 P8 同样渲染此行（核心组同样 1 组/1 项，韩语原文句），故本版与核心在同一口径下相等。**绝不“纠正”他版 KIT：** ko-pt 的 66 与 ko-fr 的 84 属不同定义（84 似排除 content8 的 1 项），本版门值只担保与核心相等，两口径下均成立，不混算。

## 4. 金句 / 短语 / 范文 / 登记 / 溢出 — 通过

- **金句 8 句（去空格全刊频次 + 页签，核心 = 本版）：** `11월 7일은 입동이에요` p1：5；`절정에 가까운 주말이라고만 말할 수 있어요` p1：2；`김장은 겨울 내내 먹는 김치를 담그는 일이에요` p1：4；`수능까지 17일 남았어요. 오늘이 D-17예요` p2：2；`낮은 길은 더 늦게 물들어요` p3：2；`KIA 타이거즈가 LG 트윈스를 3연승으로 이겼어요` p4：2；`온 나라가 수험생을 응원해요` p5：2；`날짜를 먼저 보세요` p6：2——即 **5/2/4/2/2/2/2/2**，每句均在其页签页出现。
- **P7 短语（`이번 주의 문장`，8 条）：** 韩语引句逐字出自本刊页签文章（去空格核对：1면×3、2면×1、3면×1、4면×1、5면×1、6면×1 全部在其页签页正文内），荷兰语译行各带正确页签 `(1면)`/`(2면)`/`(3면)`/`(4면)`/`(5면)`/`(6면)`（如 `7 november is Ipdong. (1면)`、`Kijk eerst naar de datum. (6면)`）。另 P7 B2 栏内有一句带 `(3면)` 的例句（`설악산 실제 관측은 10월 16일이었어요. (3면)`），属词栏例句，不计入 8 句短语，不构成重复或错误。
- **范文：** MODELO 本版与核心逐字相同，去空格计 **157 字**，起首 `나의 겨울 준비는 김장부터 시작해요.`，且 P8 H 区印有该范文全文（双侧 SVG 均含起首句）。
- **登记（自有 REG 比对，`work/reg-core/reg.json` vs `work/reg-ed/reg.json`）：** 总数 150 = 150；页分布 10/18/18/18/18/18/12/38；级别 A2 51 / B1 72 / B2 27；题型（内部键）完成句子 48、单选 52、词汇配对 16、完形单选 13、造句 8、句型转换 4、判断 4、翻译 4、写作 1；页/级别/题型差异 **无**；键差异恰 {137, 138, 150 装置行}；注变更 150/150；其他字段差异 0（词干不在 REG 内，见 §2）。
- **零 FLOW OVERFLOW：** 自有 scratch 重跑日志（`work/ed-repro.log`）中 `OVERFLOW` / `HEAD TOO WIDE` / `!!` 命中 0；各流均在其底线内结束：P1-headline 1413/1828、P1-weekend 2094/2290、P1-quiz 2521/2540、P2-ex 2258/2580、P3-ex 2234/2580、P4-ex 2002/2580、P5-ex 2256/2580、P6-ex 2195/2580、P7 三栏 1062/1029/1089（底 1560）、P8-ex 403/1252、P8-keys 2516/2540；登记统计与核心基线一致（TOTAL 150、model 157）。

## 5. 几何 — 通过（P8 三口径均过线但接近，如实标注余量）

- **Canonical `tools/occlusion_audit.py`**（sha 经核实 `e1f92b42…addf2`；自检 6 类缺陷全触发、干净对照静默）：**本版 0 旗标、核心 0 旗标、NEW（本版 − 核心）0**（`work/occlusion-ed.json`、`work/occlusion-core.json`）。
- **自有重测（`work/s_geom.py`，仅借用 OA 字体/墨迹解析，逻辑自写）：** 全页右缘 ADVANCE 扫描（限 1910）**最差 1885.0、0 旗标**；框线扫描（页脚规则线 y=2580 豁免）**0 旗标**；同基线墨迹重叠（0.6px 容差）**0 旗标**；P6 标签覆盖（基线锚定墨迹法）覆盖 >0 的标签 **0 个、最差 0.0%**（门 <30%）。
- **P8 三口径（限 2540；流光标取自有重跑日志，非建造员 round3 日志）：** 流光标 **2516.0**（余 24.00）、末基线 **2530.48**（余 9.52）、墨迹底 **2533.98**（余 6.02）——**均过线**，但墨迹底余量仅 6.02px，属“通过但接近”，已如实标注（光标 < 末基线因光标落在较空的末列、末基线落在较满的前列，符合建造员解释）。
- **P7：** 预告框底 **2519.94**（<2540，余 20.06）；来信框 rect y=1230.44、h=635.5、底 1865.94，末行墨迹底 **1854.68**（框内余 **11.26px**），末行文本 `je brief en je beste tekst van blz. 8 op!`；金句规则线 y=1895.94，距末行墨迹 **41.26px**；slack +40（公式尾常数 26→66，KO×FR 值，见 transform.py 对子）。**核心出框只报告、不重开核心：** 核心来信框底 1738.94、末行墨迹 1766.73，**出框 27.79px**，与建造员“核心公式低估约 26–29px”一致；本版未继承该出框。

## 6. 孤儿扫描 — 通过（独立方法，非只采信修正法）

- **独立方法（`work/s_orphan.py`，与建造员 spy 的 token-span 码分开写）：** (a) 字符序列守恒：每调用的 post 行去空格拼接必须等于原文去空格串（kinsoku 移位只移边界、不增删字符）；(b) 指针走查：每行必须平铺原文（精确匹配，或单字符 oidashi 移位），边界若落在空格分词内部则计尾音节，≥3 韩语音节才旗标；(c) 行首扫描：post[1:] 行首属 NO_START 集者列出 adjudicate。wrap 日志由自有插桩重跑产生（仅记录、不改布局），该重跑 SVG 与交付仍 **8/8 逐字节相同**。
- **结果：943 调用全覆盖，字符序列违规 0、走查未解析 0、≥3 音节尾切分 0、行首 NO_START 5 条。** 943 与建造员数一致；覆盖完整性说明：943 含布局测高调用与实际渲染调用（同一文本可被 wrap 两次，如高度计算 + 段落渲染），本分析对每次调用均检查，无跳过（已废弃的去空格比对法曾跳过 328 调用，本方法未用它）。
- **5 条行首的逐项 adjudication：** 全部为 ASCII 单引号 `'` 开头的冻结韩语引语正当行首（非孤儿标点），且其中 4 条 distinct 渲染行与核心**同页同 x 同基线同文本**：P5 (x=65, y=753.98) `'힘내세요!', '떨지 마세요!', '잘할 수…`；P7 (x=65, y=369.54) `'김장'이라고 해요.`；P7 (x=527, y=304.18) `'D-17'처럼 써요. 오늘이 11월 2일, 수능이 11월…`；P7 (x=1473, y=1117.03) `'〜부터 〜까지예요?'라고 해요.`。第 5 条是同一 `「〜부터 〜까지」` 框架文本的第二次 wrap 调用（测高 + 渲染，调用号 517/519），渲染行只有 1 条——故“5 条调用、4 条渲染行”，KIT “5 entries”措辞应理解为调用数（见 §13 勘误 (c)）。
- **渲染行首全量清单（独立于 wrap）：** 全刊以 `'` 起首的渲染行双侧各 7 条；除上述 4 条外另 3 条为段落首行（post[0]，spy 行首扫描不覆盖）：P7 #102/#104 题干（`'김장'은…`、`'절기'는…`，双侧同坐标）及 P6 `'예정'과 '확정'도 나눠야 해요. 예정은…`——P6 该行 y 本版 828.95 vs 核心 799.23（+29.72px），系 P6 荷兰语层流高变化引起的正常重排，不是孤儿、不是冻结行错位，且不在任务所指的 5 条之内，特此区分说明。
- **无歧义孤儿标点扫描（全部渲染行）：** 行首为无歧义闭标点（`, . ! ? ) ] } ”` 等，不含 `'`）者：本版仅 9 条以 `·` 起首的行（P2 gloss 续行×2、P3 gloss 续行×1、P4 gloss 续行×1、P6 gloss 续行×1、P3/P5/P6 选项续行×3，如 `· 깊어지다 = dieper worden.`），核心同样有 4 条 `·` 起首行——`·` 是本刊 gloss/选项分隔符，续行以分隔符起首属版式惯例（gloss 换行即在 `·` 处断开），不是悬空闭标点；行尾为开标点（oidashi）者双侧均为 0。

## 7. 轮次核查 — 通过（基线支撑差异范围；无半写入残留）

- **R1→R2（SVG：`round1-svg-sha256.txt` vs round2-full 的 SVG 部分；卡片/PDF：`round1-full-sha256.txt` vs round2-full 的卡片/PDF 部分）：** 差异恰 p1、p7、p8 三页 SVG + 三页卡片 + 双 PDF（PDF 为整文档重渲染，必然变化）；p2–p6 SVG 与卡片逐字节相同。**支撑声称。**
- **R2→R3（`round2-full-sha256.txt` vs `round3-full-sha256.txt`，按文件名比哈希）：** 差异恰 p8 SVG（`5d0fd9ba…` → `76a88054…`）+ p8 卡（`8174c6a6…` → `4b0031af…`）+ 双 PDF（web `296aca6c…` → `4fa8990c…`；print `c863e5bb…` → `dc95ad2c…`）；p1–p7 SVG 与卡片逐字节相同。**支撑声称。** 附注：两文件路径格式不同（round2 用绝对路径、round3 用相对路径），故原始 diff 文本会全量显示，须按文件名比哈希才是有效比对。
- **基线文件链：** `baselines-round3-pre.txt` 与 `round2-full-sha256.txt` **逐字节相同**；`baselines-round2-pre.txt` 与 `round1-full-sha256.txt` **逐字节相同**；`baselines-round1-pre.txt` 为首轮前的空目录清单（svg/cards 目录尚空），与“首轮渲染”一致；R1 SVG 基线另由 `round1-svg-sha256.txt` 供给，故 R1→R2 的 SVG 差异范围仍可验证。**过程记录无缺口。**
- **两次中间编辑断言失败未写入、不计轮次：** 无产物可查，属过程陈述；但“无半写入残留进交付物”的关键证据成立——交付哈希 = round3 manifest（18/18，见 §1）且自有 transform 重跑 = 交付 8/8（见下），半写入若进入交付必破坏二者之一。
- **fix 轮改动只在 transform.py 内的单独复现：** 自有 scratch 中从 `orig/` + transform.py 单独跑 transform（其写盘均基于自身目录，ED_DIR 变量未被使用），产出的 bslib4/content12/content34/content56/content7/content8/svglib/run/render **9/9 与 build 树文件逐字节相同**，含 R2 三项（P1 gloss 缩短、P7 短语 pitch 132→102、P8 #115/#136 注压行）与 R3 一项（P8 写作 glossline 3 行→2 行）。transform 末尾的 Han 门（除内部题型键外零汉字）亦在复现中通过。

## 8. 读者来信角与荷兰语讲解层抽查 — 通过

- **来信角逐字摘录（P7 col3，x=1473）：**
  - 韩语来信（冻结，与核心逐行相同）：`「안녕하세요. 저는 대학생이에요.` / `토요일에는 내장산에 단풍을 보러 가요.` / `일요일에는 집에서 김장을 도와요. 겨울이` / `와도 따뜻하게 지내고 싶어요.」 — 독자` / `편지의 예`。
  - 韩语披露（冻结，与核心逐行相同）：`알려요: 이 편지는 편집부가 쓴 예예요. 마감` / `때까지 진짜 독자 편지와 8면 쓰기 우수작이` / `도착하지 않았어요. 그래서 예가 실렸고,` / `지난 호의 약속은 VOL.3으로 이어져요.`。
  - 荷兰语短注：`Voorbeeldbrief van de redactie, geen echte brief.`（2 行）。
  - 荷兰语单段披露 + 征集句（5 行拼接后逐字）：`Tot de deadline kwamen er geen echte brieven en geen beste teksten van blz. 8 binnen: het voorbeeld blijft staan en de belofte schuift door naar VOL.3. Stuur ons je brief en je beste tekst van blz. 8 op!`
- **披露 3 事实 adjudication：** (1) 无真实来信 `geen echte brieven` ✓；(2) 无最佳 P8 文本 `geen beste teksten van blz. 8` ✓；(3) 两者均顺延至 VOL.3（`het voorbeeld blijft staan en de belofte schuift door naar VOL.3`）✓。**征集句字面同时覆盖来信与最佳 P8 文本：** 同句祈使句 `Stuur ons je brief en je beste tekst van blz. 8 op!` 同时含 `je brief` 与 `je beste tekst van blz. 8` ✓。预告行（P7 末 `다음 주… 여러분의 편지와 8면 쓰기 우수작도 실어요`）为下期预告，**不计作征集**，本 adjudication 不依赖它。无虚构人名、来信或引文。
- **荷兰语数字/日期格式与关键日期数字（与核心一致）：** 荷兰语注用荷兰惯例——`551.864`（#75/#91/#121；韩语键保留 `551,864` 逗号形，键与注各守其式）、`415,5 mm`（#118；韩语键/正文为 `415.5`）、`300.000 won`（#13/#22）、`1.312`（#76/#92/#122）、`27.000 won`（#23）、`3.271`（#68/#73）、`1.620`（#78）。抽查事实：#14 韩史考试周六 11 月 28 日（`Examen Koreaanse geschiedenis: zaterdag 28 november`）✓；#22 最高罚款 300.000 won ✓；#55 台风 10 月 26 日转为温带气旋（注 `Op 26 oktober werd het een extratropische cycloon`；先前拼接无空格的 `extratropischecycloon` 系本校对重建行拼接方式所致，原始渲染行为 `…extratropische` / `cycloon` 两行、登记注含空格，已核实非缺陷；#131 同理）✓；#90 听力 13:10–13:35 ✓；#118 Hallasan/Samgakbong 415,5 mm ✓；#131 下周 = 韩史考试准备 ✓。
- **拼写抽查范围与方法（如实声明）：** 通读范围 = P8 注全部 150 条（登记串，并与印刷行交叉核对）+ 渲染 gloss 全部 41 调用/85 项 + 来信荷兰语段与短注 + P7 短语荷兰语译行 8 条 + 家具/标题/指令串（与 W43 逐串比对，见 §9）；程序扫描 = 注段汉字 0、英文功能词残留 0（仅 Dutch 本词 `week` 命中）、双空格 0。**未发现拼写、语法或日期/数字错误。** 未声称通读全部荷兰语之外的文本——正文为冻结韩语，无荷兰语正文可读；本段即全部抽查范围。

## 9. 家具三方对照（核心 / W43 / 本版）— 通过（附一处 KIT 表述勘误，见 §13）

| 项目 | W45 KO 核心 | W43 ko-nl（实测） | 本版（实测） | 结论 |
|---|---|---|---|---|
| 刊头 | `Lucerna` (x=975, y=262, 168pt)，无冠词 | 同 | 同 | = W43 |
| 副标槽 | y=372 | y=366 | y=366 | = W43 |
| 徽章串 | —（无；中文刊头层） | `TEKSTEN IN HET KOREAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS` | 与 W43 逐字相同 | = W43 |
| 徽章 y/字号/颜色/字重/锚点 | — | y=394、20pt、#a4553a、700、x=975 middle | 同（y=394、20pt、#a4553a、700、x=975 middle） | = W43 |
| 规则线 | 392 / 401 | 412 / 421 | 412 / 421 | = W43 |
| 暗带 rect y | 424（h=118） | 433（h=118） | 433（h=118） | = W43 |
| 暗带文本基线 | 478 / 522 | 487 / 531 | 487 / 531 | = W43 |
| 页脚串 | `Lucerna · 韩语周报 VOL.2 · LUCERNA KOREAN WEEKLY` + `제 N 면 / 총 8 면` | `Lucerna · KOREAANS WEEKBLAD VOL.1 · TEKSTEN IN HET KOREAANS · UITLEG IN HET NEDERLANDS` + `Pagina N van 8` | 同 W43 串、VOL.2（`Lucerna · KOREAANS WEEKBLAD VOL.2 · …` + `Pagina N van 8`） | = W43（VOL 递进） |
| 栏目标题 | — | `생활 · Dagelijks leven`（p2）、`문화 · Cultuur`（p3）、`스포츠 · Sport`（p4）、`청년 · Jongeren`（p5）、`깊이 읽기 · Dieper lezen`（p6）、`말 공부 · Taal`（p7）、`시험과 답 · Toets en antwoorden`（p8） | 7/7 同页同串 | = W43 |
| 练习头 / 右线 | — | `연습 · Oefeningen blz. N` / `Antwoorden op blz. 8 · Niveaus kunnen gemengd staan — zoek op nummer` | 同串（5 页） | = W43 |
| P1 quiz 右线 | — | `Lees de voorpagina en kies het juiste antwoord · Antwoorden op blz. 8` | 同串 | = W43 |
| P8 分隔符 | `— 제N면 —`（韩语形） | `— Pagina N —` | `— Pagina N —`（8 个齐全） | = W43 NL 形（非 ko-pt/ko-fr 的韩语形） |
| P8 栏副标 | 韩语冻结 `제8면 · 이번 주의 큰 시험 + 모든 답` | 同（冻结） | 同（冻结） | = 核心 |
| P8 头 / 右线 | — | `답 · Antwoorden — per pagina, zoek het nummer op` / `Bij elk antwoord een korte notitie in het Nederlands · ✓ = opgave met voorbeeld` | 同串 | = W43 |
| gloss 前缀 | `译注｜`（中文） | `Uitleg — ` | `Uitleg — ` | 前缀串 = W43（gloss 条数随当期内容而异，非家具项） |
| 指令标签（实测集） | 中文指令（填空等） | Vul in / Koppel / Herschrijf / Bouw / Vertaal / W of O / Schrijf | **Vul in 42、Koppel 4、Herschrijf 4、Bouw 8、Vertaal 4、Schrijf 1；“W of O”0 次** | 见下段（非阻塞勘误） |

- **P7 词栏定义句冻结、仅 gloss 本地化：** P7 A2/B1/B2 三栏定义段（A2 入冬/金장/月동准备段、B1 D-17 段、B2 预报段）及诊所韩语纠错句、框架韩语文本、短语韩语引句、练习韩语题干，在核心→本版 Hangul 行多重集差异中**无一纯韩语内容行变化**；差异行全部是讲解层行（glossline 中文→荷兰语、诊所荷兰语注、框架荷兰语注、短语荷兰语译行、栏目标题、页脚），且其中韩语子串逐字相同。P7 三栏 glossline 各 1 条（2 项），即 §3 的 P7 3 组/6 项。
- **“W of O”说明（非阻塞）：** 本版全文无 `W of O` 文本；核查表明核心亦无——W45 核心的 4 道判断题（#97–100，P6 D 栏 `D · 맞다 틀리다` + 荷兰语 glossline `Klopt de zin, kies 맞다; klopt hij niet, kies 틀리다.`）在核心与本版源码中均**无 instr 参数**，故不渲染指令 chip；W43 的 4 个 `W of O` 属 W43 当期判断题自带的 instr，与 W45 无对应项。KIT §2 “Instruction labels … W of O … identical”一句因此失实，但**印张本身忠实于核心**（无中生有加 chip 反而会违背核心），故列为 §13 的 KIT 文字勘误，不阻塞上架。

## 10. 图片 — 通过

- **Payload = 核心（两种口径，`work/analysis.json` §H）：** p1 `535fff46b7ce`/`6f7f33ed8f40`、p2 `e66d2b455ec6`/`96a6a19b612a`、p3 `e266b6ee1a87`/`158ea3a0e81f` 与 `5bea45d1f81e`/`214cc390ac7c`、p4 `1a7e7d6d5ffc`/`18ad8ae06fac`、p5 `6a1bab177d54`/`35e7dc69d417`、p6/p7/p8 0 图——前为 base64 文本 sha256 前 12 位、后为解码 JPEG sha256 前 12 位，双侧逐项相等；页分布 **1/1/2/1/1/0/0/0**。
- **Credit 行 Artist 原文且确已放置：** p1 `사진: lumoplank — CC0 (Wikimedia Commons) · 자료 사진`（图框 y 1874–2194，credit 基线 2245.7，正下方）；p2 `사진: wizdata — CC0 …`（图 200–430，credit 507.3）；p3 `사진: Udonhan1992 — CC0 …`（图 200–385，credit 436.6）与 `그림: Paul Cézanne — Public domain (Wikimedia Commons)`（图 854.8–1054.8，credit 1132.1 起、换行续 `Commons)`）；p4 `사진: Bain News Service — Public domain (Wikimedia Commons)`（图 200–440，credit 491.6 起、续 `Commons)`）；p5 `사진: Gary Todd — CC0 …`（图 200–430，credit 507.3）。**各 credit 串与核心同页同坐标逐字相同**，即本版未新造 credit，冻结自核心。限度声明：build `assets/CREDITS.md` 为 VOL.1 时期文档（未列 ssam/bukhansan 等 W45 用图），不能用作 W45 的 Commons Artist 佐证；Artist 原文的 Commons 侧核实属核心层继承事项，本版仅担保 credit 行与核心冻结一致且已放置。
- **ssam 照诚实标注在位：** P2 照片正下方韩语说明（x=1451, y=454.0/479.65，credit 行之上）逐字为 `쌈 채소와 쌈장. 겨울 식탁의 한국 음식이에요. 김장 사진이 아니에요.`（“ssam 菜与 ssam 酱，冬季餐桌的韩国食物，**不是金장照片**”），诚实标注明确在位。

## 11. 网页版 PDF 与卡面目视 — 通过

- **网页版 PDF 逐页对卡片渲染比对（自有实现，pypdf 抽图 + PIL，`work/web.log`）：** 网页版 8 页、印刷版 8 页；网页版尺寸 3,547,923 B、印刷版 32,552,178 B；网页页光栅均为 1400×1938；逐页 mean |diff|（R/G/B）：p1 [2.42, 1.57, 3.91]、p2 [2.30, 1.51, 3.85]、p3 [2.33, 1.48, 3.84]、p4 [1.99, 1.28, 3.44]、p5 [2.19, 1.37, 3.68]、p6 [2.01, 1.29, 3.43]、p7 [1.78, 1.18, 3.21]、p8 [2.54, 1.60, 4.10]——**均在 JPEG q85 噪声量级，无离群页**（最高为 p8 蓝通道 4.10，与各页 3.21–4.10 的带宽一致，非阻塞差异；已吸取 fr-en 噪声教训，逐页比对而非只看均值）。
- **目视全部 8 张卡（逐张）：** p1 徽章/暗带/数字框/gloss 3 行换行干净，头条流止于行 B 上方甚远，秋景照 + lumoplank credit 在位；p2 栏副标一行，ssam 照 + 诚实标注 + wizdata credit，D-17/D-12 数字框；p3 地铁照 + Cézanne 苹果静物照 + 双 credit，清单框；p4 Bain 老棒球队照 + 晋级箭头图干净；p5 图书馆照 + Gary Todd credit、数字框；p6 对照表标签清晰无重叠；p7 诊所框、框架框、来信框止于框内，短语行距舒适，预告带完整；p8 A–H 区齐全，写作 glossline 2 行、第 4 列顶无孤儿行、答案流止于页脚上方甚远。**8 页均无重叠、裁切、杂点。**

## 12. 核心事实债与新增主张

- **核心事实债只继承、不判本版阻塞（与 KIT §9 一致，不重开）：** 韩国系列赛 11 月 2 日开赛含雨延 caveat（刊内用 `발표된` 措辞 + 截止注）；季后赛 G1（10 月 26 日）结果截稿时未知、刊内未印比分；Champi 纪录断言已于核心层删除；立冬 11 月 7 日 / 小雪 11 月 22 日源自历法博客（未取 KASI 官网）；韩史考试细节为二手报道；Commons 图缺口（无已验证 PD/CC0 韩国红叶/金장/韩国学生备考照，ssam 照已诚实标注非金장）。
- **本版新增主张 0：** 荷兰语层全部为核心内容的翻译/本地化（注、gloss、标题、指令、来信荷兰语段）；数字/日期经 §8 抽查与核心对应；唯一新 CJK 为 §1 的冻结词头引用（有出处）；未引入新的事实断言、比分、日期或图片主张。

## 13. 非阻塞勘误（不影响 ZERO PROBLEMS 结论，无需重建/重渲染）

1. **KIT §2 家具表“Instruction labels … W of O … identical”失实：** 实测本版与核心均无 `W of O`（原因见 §9）。建议协调员在插库时将该行改为“W of O：W43 有，本版与核心均无（判断题无 instr；P6 D 栏标题 + 荷兰语 glossline 承担题型说明）”——**纯 KIT 文字勘误，不动任何渲染文件**。
2. **transform.py 两处旧注与实际对子不符（build 侧文档，非印张）：** 头注称 P2–P6/P8 指令 glossline “become Portuguese”（实际全部为荷兰语对子）；另注称 P8 分隔符“NOT touched（韩语 `— 제N면 —` 形）”（实际对子明确替换为 `— Pagina N —`）。实际输出正确，注文待顺手修正。
3. **KIT §4.6 “5 entries”措辞：** 5 为 wrap 调用数（框架文本测高 + 渲染各 1 次），渲染行首引语行为 4 条（见 §6）；建议措辞改为“5 次调用、4 条渲染行”，内容结论不变。
4. **build `assets/CREDITS.md` 为 VOL.1 时期文档：** 不可用作 W45 credit 的 Commons 佐证（见 §10 限度声明）；W45 credit 以核心冻结行为准。

## 结论重申

**ZERO PROBLEMS — W45 KO × NL 可交付上架，阻塞项无。** 12 门全部独立重测通过；唯一发现均为上述 §13 的文档措辞勘误，不触及印张内容与渲染文件。
