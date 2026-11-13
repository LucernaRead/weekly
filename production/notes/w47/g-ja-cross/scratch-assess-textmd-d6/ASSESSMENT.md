# D6 评估报告 — textmd.py 导出缺失（W47）

- 评估员：工具评估员（只调查，未改任何源文件、未重建、未 commit、未 push）
- 日期：2026-11-11（UTC 约 08:05–09:30；读数快照于此窗口内）
- 探针：开工 `git hash-object -w` 成功 + 笔记目录可写；每次写盘前重探，均通过；未遇 EDQUOT。
- 缺陷来源：`scratch-proof-ko-de1/PROOF-NOTE.md` D6（ko-de proof1，run 2）
- 调查工具（只读，均存于本目录）：`detect_d6.py` + `d6-scan.json`（全file pattern 扫描），
  `verify_d6_v2.py` + `verify2.json`（双片段 presence 核验），`ppara_census.py`
  （`p.para` 全量普查；ko/ru 各跑一次）。`verify.json` 为第一版探针（40 字符连续探针），
  对 SVG 交错提取有误报，已废弃，以 `verify2.json` 为准（仍有 1 处 es 误报，见 §4，已逐条 grep 裁决）。

## 1. 结论（先说）

**D6 缺失属实——但 PROOF-NOTE 的归属说窄了，范围也比原文大：**

1. **ko-de 缺失属实**：`2026-w47-ko-de.text.md` P7 一节确只有三个框标题
   （실수 병원 / 이번 주의 틀 / 독자의 편지），`lt`/`lcn`/`wt`/`wcn` 四段正文全无
   （`grep 안녕하세요` = 0；全文唯一的「수능 후에」在 line 571，是 `quotes` 列表的金句第 7 条，
   不是框架例句）。core-ko 自己的 text.md 同样缺（`grep 안녕하세요` = 0）。
2. **D6 不只 P7、不只 ko-de**：同形态（plain-string 变量 → `p.para`/`f.para`）在
   core-ko 共漏 **10 段**（P7 六段 + P2/P3/P5 `etvous` 三段 + P8 `MODELO` 范文一段），
   ko-de/en/fr/es 每版漏 **8 段**。
3. **同缺陷类还波及 ru 全家**：ru 的 `ru_textmd.py` 对 `p.para` 是**整类跳过**
   （`do_call` 注释明说 "Only the Page (p) is excluded"），D6 形态漏 **6 段/版**，
   且 inline 字面量、循环变量也一并漏，`p.para` 全量普查为每版 **41 个去重字符串中 39 个缺失**。
4. **其余 10 个语系（de/en/es/fr/it/ja/nl/pt/zh-cn/zh-tw）不受影响**：抽查 + 全量核验均为 0 缺失。
   它们的导出器本来就能解析变量（运行时记录）或直接读 SVG 文字层。
5. **没有统一的共用 `textmd.py`**：W47 根本没有一份共享工具——ko 用 AST 收集器（5 份相同拷贝），
   ru 用自研 AST 解释器（11 份相同拷贝），zh-tw/ja/es 用 SVG 导出，各家互不相同。
   `tools/` 目录里没有 textmd.py。W46 的旧版 `production/2026-w46/textmd.py`
   （全常量收集）反而不含此缺口——缺口是 W47 ko 收集器重写时引入的。

**受影响版数（有证据的）：16 版** —— core-ko + ko-de/ko-en/ko-es/ko-fr（5 版，ko 家族），
core-ru + ru-de/ru-en/ru-es/ru-fr/ru-it/ru-ja/ru-ko/ru-nl/ru-pt/ru-zh-tw（11 版，ru 家族）。
其余已建成版：0 缺失。未建成（尚无 text.md）：2026-w47-de-zh-tw 1 版（不在 89 个扫描目录的核验之列，
但其源文件含同形态变量，建成后若用 ko/ru 式导出器同样会漏——de 家族导出器经核验是完备的，
故预期不漏，建成后仍须按本报告方法复核一次）。
注：评估中途 ko-es（09:03 UTC）、fr-es 的 text.md 新建成并被纳入核验；fr-es 完备（etvous 在册）。

## 2. 缺失核实（D6 原文逐项）

### 2.1 ko-de P7（PROOF-NOTE 指认位置）

| PROOF-NOTE 指认 | 核实 |
|---|---|
| P7 只有三个框标题 실수 병원 / 이번 주의 틀 / 독자의 편지 | **属实**。`2026-w47-ko-de.text.md` lines 507–582：三个标题后直接是「이번 주의 문장」金句栏，无信件/框架正文。 |
| 缺来信正文「안녕하세요. 저는 수험생이에요. …」（`content7.py:90` 的 `lt`） | **属实**。全文 `grep 안녕하세요` = 0。 |
| 缺德语注文 `Hinweis der Redaktion: …`（`:91` 的 `lcn`） | **属实**。全文 `grep Hinweis der Redaktion` = 0（该串只在源文件里）。 |
| 缺框架例句「〜 후에」— '수능 후에 김치의 날이 와요.'（`:80` 的 `wt`/`wcn`） | **属实**。全文唯一的「수능 후에」在 line 571，是 `quotes` 列表的金句第 7 条；框架例句整句（含 `나중에 하는 일을 말할 때…` / `Rahmen: …`）无。 |
| PDF 正文完整 | 与 PROOF-NOTE 一致，未复核 PDF（不在本次任务内；PROOF-NOTE 已证印版/网版 P7 目视无溢出）。 |

### 2.2 core-ko（PROOF-NOTE 称“同样缺这三段”）

**属实，且比原文多**。`core-ko/2026-w47-ko-zh-cn.text.md` P7（lines 509–584）同样只有三个框标题；
`grep 안녕하세요` = 0。另：core 的 `lko`、`lcn2` 两段附加注文同样缺（见 §3.1）。

### 2.3 行号快照说明（重要）

评估读取时 core-ko 正在 fix1 进行中：`core-ko/content7.py:80` 的 `wt` 已是
`'수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요.'`（PROOF-NOTE 引用 run 2 时为
`'수능 후에 김치의 날이 와요.'`），`quotes[6]` 也已改为 P1 原句（D4 已修）。
即：**行号（80/81/90–93）与变量名（wt/wcn/lt/lcn/lko/lcn2）未变，但句面已随 fix1 变化**；
本报告所列字符串以本次读取快照为准，fix1 落定后行号可能再移。缺陷机理（变量形态漏收集）
不受句面变化影响。
ko-de 的 `wt` 仍为旧句 `'수능 후에 김치의 날이 와요.'`（fan-out 尚未同步核心改动——属 fan-out
重扩范畴，不在本评估内，仅作记录）。

## 3. 收集逻辑分析

### 3.1 ko 收集器：`core-ko/textmd.py`（= ko-en/de/fr/es 的 5 份相同拷贝，md5 `e01fe8dd…`）

`collect()` 只收两类，其余一律丢弃：

1. **方法调用参数中的字面量**：白名单 `CALL_ARGS` 限定的 `(receiver, method)` 位置参数，
   且 `strings_from()` 只下探 `ast.Constant` / `List` / `Tuple` / `Set` / `Dict` 节点。
   `p.para(x, y, wt, …)` 里 `wt` 是 `ast.Name`，`strings_from` 返回空——**变量形态必然漏**。
   即使字符串以内联字面量写进 `p.para` 也能收，但凡经变量中转即丢。
2. **模块级 List/Tuple/Dict 常量赋值**：`Assign` 且值是 List/Tuple/Dict 才收。
   `wt = "…"`、`lt = "…"` 是 `Assign` + `Constant`，**不在此列**。

`lt`/`lcn`/`wt`/`wcn`/`lko`/`lcn2` 在 `content7.py` 里正是形态（1）：

```python
# core-ko/content7.py:80-93（flat 脚本，全部顶级赋值；双用途是变量存在的理由）
wt  = "「〜 후에」 — '수능이 끝나면 …' …"     # :80
wcn = "句式拆解：…"                            # :81
lt  = "「안녕하세요. 저는 수험생이에요. …」 — 독자 편지의 예"  # :90
lcn = "编辑部示例信，非真实来信。"               # :91
lko = "알려요: 이 편지는 편집부가 쓴 예예요. …"  # :92
lcn2= "郑重说明：截稿前未收到真实来信与8版优秀作文，仍刊示例，顺延至 VOL.5。"  # :93
# 每个变量用两次：wrap(wt, …) 算框高 + p.para(…, wt, …) 印出
```

同文件 `quotes` 列表（List 常量）被收到——所以金句第 7 条「수능 후에 김치의 날이 와요」在册，
而框架例句本体不在册；这正是 P7 出现“半句在、一句无”的原因。
另：`errs` 列表（List 常量）同样被收到，所以易错诊所四行在册——同页内“列表过、变量漏”的对照。

**ko 每版漏载清单（经 `detect_d6.py` 全量扫描 + `verify_d6_v2.py` 双片段核验 + 直接 grep 裁决）：**

| 版 | 漏（段数） | 清单 |
|---|---|---|
| core-ko | 10 | content12 `:222` etvous、content34 `:63` etvous、content56 `:45` etvous、content7 `:80` wt、`:81` wcn、`:90` lt、`:91` lcn、`:92` lko、`:93` lcn2、content8 `:99` MODELO（范文，`f.para`） |
| ko-de / ko-en / ko-es / ko-fr | 各 8 | 3× etvous（同位置）、wt、wcn、lt、lcn、MODELO（各版译文形态；core 的 lko/lcn2 在 fan-out 合并为一条译文 lcn，故 8 而非 10） |

**ko 收集器无更广缺口**：`p.para` 全量普查（`ppara_census.py`，45 个调用点）除上述 9 段
（+1 处同名循环变量解析伪影，见 §6 方法注）外全部在册；内联字面量与列表循环项均在册。
即 ko 的缺口**恰好等于** plain-string 变量形态，不多不少。

附：ko-de KIT 已记录本收集器的另一已知 quirks（`is_prose` 丢掉裸 3 字母拉丁词 "Alle"），
与 D6 无关；core-ko KIT round 10 亦有明文 workaround（"literals stay inside call arguments —
module-level lists would be collected by textmd.py"）——编写者已知晓此规则，
content7/12/34/56/8 的变量是因 `wrap()` 算高 + `p.para` 打印双用途而不得不用的例外。

### 3.2 ru 收集器：`core-ru/ru_textmd.py`（= 10 个 fan-out 的 11 份相同拷贝，md5 `1a03d040…`）

582 行的 AST 解释器（`ev`/`do_assign`/`walk_stmt` 维护 env 求值）。机理与 ko 不同、后果更广：

- `do_call()`（lines 316–387）只处理 `p.text`、`p.band`，以及**接收者非 `p`** 的
  `para/gloss/bridge/head/box/ex/match_set`；注释原文：
  > "Only the Page (p) is excluded — its para/text are layout, not reading text."
- **`p.para` 整类被跳过**（`p.paraq` 亦无分支）。其 `ev_str()` 本可解析变量（`MODELO` 经 `f.para`
  即被收到，证明 env 求值正常），但 `p.para` 分支根本不存在。
- 因此 ru 漏的不只是变量形态：**所有经 `p.para` 印出的字符串都不见**，无论内联字面量、
  plain 变量还是列表循环项。

**ru 每版漏载（D6 窄口径，6 段/版）**：content12 `:190` etvous、content34 `:168` nteam
（国家队赛程注）、content7 `:84` wt、`:93` lt、`:94` disc_ru、`:95` disc_cn。
`MODELO`（content8 `:99`，`f.para`）**在册**——ru 与 ko 在此点相反，可作对照。

**ru 每版漏载（`p.para` 全量普查，`ppara_census.py`）**：core-ru 54 个调用点、**41 个去重字符串中 39 个缺失**
（ru-en 同数：54 点 / 41 去重 / 39 缺失）。除上述 6 段外还包括：
P1 副标 `14-й тур: «Зенит» и «Динамо» — по 31 очку`、本周词释义、P2 记忆句、
P3/P4/P5/P6 各栏事实列表（`facts`/`ideas`/`tab`/`cal`/`pc`）、P7 易错诊所全部 12 行
（4 行 × wrong/right/cn，直接 grep：`творительный падеж`、`Поздравляю с День студента` 皆 0）、
图表图例、下期预告句。仅 2 个去重字符串在册（`18 ноября — день рождения Деда Мороза.`、
`22 ноября — День психолога.`——因其同时在习题日历里出现，经 `f.*` 路径在册）。
金句栏（quotes）在册——经 `do_appendix` 另路处理，不走 `p.para`。

### 3.3 其他 10 个语系的导出器（均已核验完备）

| 语系 | 导出器 | 机制 | 核验结果 |
|---|---|---|---|
| de / en / fr / it / nl / pt / zh-cn | 各核自有导出路径（脚本多不在仓内：如 core-en KIT 提到的 `textmd_w47.py`、core-ja 的 `textmd-core.py` 在 clone 中无此文件；core-it 只有 `scratch/export_core_textmd.py`） | 运行时记录渲染字符串（core-en KIT 明言：stub `bslib4` 执行 content 文件并记录每个渲染串）或等价物 | `detect_d6` 检出的变量串（de 11、en 2、fr 1、it 7、nl 9、pt 11、zh-cn 8 段/核）**全部在册**（0 缺失） |
| ja | SVG 文字层导出（与 zh-tw 同类；core-ja text.md 呈逐行 `<text>` 碎片） | 读渲染后 SVG，印出的都有 | 10/10 在册；P7 来信 `こんにちは…読者の手紙` 在 lines 989–1002 |
| zh-tw | `export_zhtw_textmd.py`（core + 9 个 fan-out 拷贝） | 读 SVG `<text>` 节点 | 7/7 在册；P7 框架/来信碎片均在 |
| es | `hidden_files/w47/scratch-es/extract_text2.py`（仓外 scratch）自核心 SVG 按栏位阅读顺序导出 | 读 SVG，栏位重排 | 初版探针报 4 段缺失，**逐条 grep 裁决为误报**：`bb`/`MODELO`/etvous×2 均在册，只是提取器把他栏文字交错插进长句中间（双片段探针失效），内容本身齐全。**es 缺失 = 0** |
| pt fan-out | `textmd.py`（如 pt-es）从 core text.md 做 SEG/OVR 替换 | 继承 core text.md | core-pt 0 缺失，故 fan-out 亦 0 缺失 |

**无统一共用工具**：`tools/` 无 textmd.py；W46 旧版 `production/2026-w46/textmd.py`
是全常量收集（`strings_in_order` 走全部 `Constant`，跳过 f-string），**无此缺口**——
缺口是 W47 ko 收集器重写为“调用参数 + List/Tuple/Dict”后引入的回归。
各语系导出器互不相同，修一处不自动修他处；反之也互不干扰。

## 4. 受影响版清单（有证据的才列）

全量扫描 89 个目录（12 核 + 77 个 fan-out 目录）→ 668 段 plain-var 字符串核验
（66 个目录有 text.md；2 个目录当时无 text.md 无法核验：2026-w47-de-zh-tw、
2026-w47-fr-es——fr-es 在评估中途建成，复核为完备；de-zh-tw 至报告时仍无 text.md）。

### 受影响：16 版

| 家族 | 版 | 缺失段数 | 缺失内容（类别） |
|---|---|---|---|
| ko | core-ko（`2026-w47-ko-zh-cn.text.md`） | 10 | P7 框架例句 wt + 注文 wcn、来信 lt + 注文 lcn/lko/lcn2（6）；P2/P3/P5 etvous（3）；P8 MODELO 范文（1） |
| ko | 2026-w47-ko-de | 8 | 同上（lko/lcn2 合并为一条德语 lcn）；P7 四段即 D6 原文 |
| ko | 2026-w47-ko-en | 8 | 同上 |
| ko | 2026-w47-ko-es（09:03 UTC 新建成，纳入核验） | 8 | 同上 |
| ko | 2026-w47-ko-fr | 8 | 同上 |
| ru | core-ru（`2026-w47-ru-core.text.md`；另有 `2026-w47-ru-zh-cn.text.md` 亦同源，核验用前者） | 6（D6 口径）；`p.para` 全量 39 去重段缺失 | P7 wt/lt/disc_ru/disc_cn（4）；P2 etvous；P4 nteam；另 `p.para` 全类漏（见 §3.2） |
| ru | 2026-w47-ru-de/ru-en/ru-es/ru-fr/ru-it/ru-ja/ru-ko/ru-nl/ru-pt/ru-zh-tw | 各 6（D6 口径）；`p.para` 全量同 core-ru | 同上（各版译文形态） |

### 未受影响（已核验 0 缺失）：其余全部已建成版

de 家族 10 版（core-de + 9 fan-out，11 段/版全在册）、en 家族 10 版、es 家族 11 版
（初版 4 段“缺失”为 SVG 交错提取误报，已逐条 grep 裁决在册）、fr 家族 3 版
（core-fr + fr-de/fr-en/fr-es）、it 家族 10 版、ja 核 1 版、nl 核 1 版、pt 家族 11 版、
zh-cn 家族 1 版（core-zh-cn + zh-cn-de）、zh-tw 家族 10 版（core-zh-tw + 9 fan-out）。
另 core-en/core-fr/core-it/core-nl/core-zh-cn 的核 text.md 亦 0 缺失。

### 不推测的部分

- 2026-w47-de-zh-tw：尚无 text.md，未核验。de 家族导出器经核验完备，预期不漏，但建成后须按本报告
  方法（`detect_d6.py` + 双片段核验）复核一次再定论。
- ko 其余 7 个 fan-out（it/pt/nl/ja/ru/zh-cn/zh-tw）与 ja 全部 10 个 fan-out、nl 全部 fan-out：
  目录尚不存在，无法核验；建成时若沿用各自家族导出器，预期与已核验同家族版一致。
- W43–W46 的旧周 text.md 不在本次任务范围，未扫。

## 5. 三种修复形态的利弊与推荐

### 推荐：A. 修工具（两个收集器）+ 重导 16 版 text.md —— **唯一推荐**

**ko `textmd.py`（5 份相同拷贝）**：二选一，取其一即可——
  - (A1) 在 `collect()` 加一条：`Assign` 且值为 `Constant` str → `is_prose` 过即收
    （wt/lt/etvous/MODELO 全是顶级 plain-string 赋值，一条分支全覆盖；循环变量已由 List 分支覆盖，
    无需动）；
  - (A2) 对 `CALL_ARGS` 的参数做 Name 解析：先扫一遍建立 `name → 常量串` env，
    `strings_from` 遇 `Name` 查 env（与 ru 解释器同款思路，更通用，能覆盖将来出现的拼接形态）。
  建议 A1 为主（改动最小），A2 视 fixer 判断。改后须 diff 审一遍：新收的字符串应恰为漏的段
  （core-ko 333 → 约 343 项；ko-de 332 → 约 340 项），多出 print 调试串之类即回滚重审
  （`is_prose` 会放过 "P7 col3 ends" 这类串——但它们是 `print()` 参数不是赋值，A1 不会收；
  仍须以 diff 为准）。

**ru `ru_textmd.py`（11 份相同拷贝）**：在 `do_call()` 给 `p.para`（及 `p.paraq`，现无使用，
  顺手覆盖）加分支，与 `f.para` 同款走 `ev_str(call.args[0], env)` + `add_para()`。
  但须注意原注释的顾虑（"`p.para` 是 layout"）——普查证明该断言对本期内容不成立，
  可仍加一道 `is_prose` 式过滤（ru 已有 `titleize`/`space_cjk_digits` 等，fixer 自定），
  并 diff 审一遍新增行（应为 39 段去重内容/版；页脚类家具串如 `— СТРАНИЦА` 若被带入须排除）。
  另须确认 `add()` 去重/排序在新增 `p.para` 行后仍与已发格式一致（ru text.md 含 `###` 标题层级与
  `>` 引用行，`p.para` 行应为普通段落）。

**实施要点**：
- 两处改动互不相干，可并行；改完须把修复同步到**全部同 md5 拷贝**（ko 5 份、ru 11 份），
  否则 fan-out 重导仍用旧代码。长远应收敛为一份共用工具（`tools/` 下），但那是重构，
  不属 D6 修复，不要在本轮扩大范围。
- 重导范围：**只重导 16 版 text.md**（ko：`/usr/bin/python3 textmd.py . <slug> <slug>.text.md "<title>"`，
  注意 core-ko KIT 的解释器锁定——textmd 须用 `/usr/bin/python3`，不是 venv；
  ru：`ru_textmd.py <build-dir> <out.md> "<title>"`）。**不重建 PDF/SVG**（印刷版文字层完整，
  无需动）；**不重跑 proofread**（改动只影响次要导出物；但重导后须用本报告的核验脚本复跑，
  预期 0 缺失，并 diff 审新增行）。
- **不碰其余 10 个语系**：它们的导出器已完备，改工具只会引入回归风险。
- **时序**：core-ko 正在 fix1（content7.py 有改动），ko 重导须在 fix1 落定 + fan-out 重扩之后做，
  否则重导结果会被下一轮重扩覆盖；ru 无此依赖。issues/2026-w47 目前为空（0  entries 尚未入仓），
  重导只改 `production/<slug>/*.text.md`，**不触 index.json、无需 `lint --write`**。
- W46 旧版 `production/2026-w46/textmd.py` 不要动（已发版，其收集器无此缺口）。

### B. 在 content7.py 等改写法（内联字面量 / 改列表）—— **不推荐**

- **对 ru 无效**：ru 漏的是整个 `p.para` 调用类，内联字面量同样漏（普查：8 处内联字面量全漏）。
  改写法修不好 ru，须先修 ru 工具。
- **对 ko 代价失衡**：变量是双用途（`wrap()` 算框高 + `p.para` 打印），内联等于把百字长串写两遍，
  迟早两处 diverge；改列表形态同样要动 12 核的 content7/12/34/56/8，而其中 10 核的导出器本来就没问题。
- **牵连印刷版**：一动 content 源码即须重渲 PDF/SVG + freeze + 几何审计 + 全量复校
  （与 D2/D3/D4 同一量级），为修一个 26KB 导出物付出整版重建成本，不成比例。
- 唯一合理的内容侧配合：今后新写 content 时优先把只印一次的长串以内联字面量或模块级列表写
  （KIT 已有此约定），但这是规范收敛，不是 D6 修复。

### C. 手工补 text.md（逐行粘贴缺失段）—— **不推荐作为修复；仅可作临时止血**

- text.md 是生成物（文件头自述 "exported from the source manuscript"；AGENTS.md 规则 4：
  从 production source 导出，不从 PDF 回抽）。手补行下次重导即被覆盖，等于没修；
  且手补绕过导出器的排序/去重/分页（`## Page N` 归属须人工保证放对页、不得与既有行重复），
  16 版 × 6–10 行的人工操作本身就是新的出错面。
- 若网站急需读者来信文本上线、可臨時手补 ko-de 一版并明确标注“手工临时行，待工具重导覆盖”，
  但须在工具修复重导后复核覆盖，不得长期留存。
- 另：text.md 的 SHA 一旦入仓会被 lint rule 9 写入 index `text` 字段；目前 issues/2026-w47 为空，
  手补暂无 index 牵连，但入仓后任何 text.md 变更都要 `lint --write` 同步——手补不省这一步。

## 6. 风险与注意事项

1. **与 core-ko fix1 的冲突面**：本评估全程只读，未写 core 源。但 fix1 正在改 `content7.py`
   （quotes、wt 句面已变），D6 工具修复 + 重导必须排在 fix1 落定后，否则重导结果作废。
   反之工具修复本身不碰 content，与 D2/D3/D4 的源码改动无冲突。
2. **ru 修复的回归面**：`p.para` 一旦放行，新增的 39 段/版须逐行 diff 审——其中有家具类字符串
   （页脚、图表图例注）的风险；且 ru 导出器会重排 P1–P8 的行顺序？不会（解释器按源码顺序执行，
   `p.para` 行落在原语句位置），但须以 diff 证实而非假定。
3. **拷贝同步风险**：ko 5 份、ru 11 份相同文件散在各版目录；只改 core 拷贝、漏同步 fan-out 拷贝，
   是最可能的复发方式。修复提交时应 `md5sum` 逐份验同。
4. **验证方法自述（供复核者）**：
   - `detect_d6.py`：AST 扫全部 `content*.py`，只认“plain-string 赋值 → 传入打印调用（Name / f-string / 拼接）”；
     不覆盖 `f"{…}"` 内嵌长串（全仓 167 处皆为 P8 键行模板 `f"{n}. {key}…"`, 无散文）、不覆盖元组解包赋值
     （全仓 grep 0 处）。结论只针对 D6 形态。
   - `verify_d6_v2.py`：双片段（头 15 字符 + 中段 15 字符，去空白）同时命中才算在册；短串（去空白 <16 字符）
     只核头片段。法一（40 字符连续探针）的 es 误报即因此法纠正；`bb` 一案经直接 grep（`tres cosas` 两处在册）
     最终裁决为在册。
   - `ppara_census.py`：`p.para` 全量解析，循环变量按列表字面量回填；同名循环变量（多处 `for t in …`）
     存在跨循环串位可能，ko 的 1 处伪影（content12 `:220` 的 `예보에서 결과로`，经 grep line 109 在册）
     已剔除；ru 的 39 去重段均经直接 grep 抽查（易错诊所/事实列表/图例 6/7 项为 0，仅 1 项因习题复现而在册）。
   - “在册”按去空白后子串判定；SVG 碎片化导出（ja/zh-tw/es）的行间断裂已由去空白处理，
     栏位交错（es）只影响探针、不影响结论（已 grep 裁决）。
5. **严重度**：低（与 PROOF-NOTE 一致）。PDF/印刷版、网站 PDF 文字层均完整；缺的是网站文本版
   （text.md）的读者来信/框架例句/互动提问/范文段落——读者在网站文本版读不到 P7 读者园地与 P8 范文，
   SEO 文本亦缺这几段。16 版均同。

## 附：证据索引

- PROOF-NOTE：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ko-de1/PROOF-NOTE.md`（D6，lines 65–71；归属 §136–137）
- ko 收集器：`~/workspace/weekly-git/production/2026-w47/core-ko/textmd.py`（与 ko-en/de/fr/es 相同，md5 `e01fe8dd80ed38cfab970e2840721c39`）
- ru 收集器：`~/workspace/weekly-git/production/2026-w47/core-ru/ru_textmd.py`（与 10 个 ru fan-out 相同，md5 `1a03d0407a9e50ad79f4fc191c27207d`；`do_call` lines 316–387，`p.para` 无分支）
- W46 旧收集器（无缺口对照）：`~/workspace/weekly-git/production/2026-w46/textmd.py`
- 缺失原文：`core-ko/content7.py:80–93`、`content12.py:222`、`content34.py:63`、`content56.py:45`、`content8.py:99`；ko-de 同文件同行号（译文形态）
- 核验：`./d6-scan.json`、`./verify2.json`、`./detect_d6.py`、`./verify_d6_v2.py`、`./ppara_census.py`
- ko-de text.md P7（缺失现场）：`2026-w47-ko-de.text.md` lines 507–582；core-ko 同文件 lines 509–584
- KIT 旁证：`core-ko/WEEKLY-KIT.md`（round 10：解释器锁定 + “literals stay inside call arguments” 约定；text.md 333 项）、`2026-w47-ko-de/WEEKLY-KIT.md:90`（332 项 vs 333 项的 "Alle" quirks；`:155` 重导命令）、`core-es/WEEKLY-KIT.md:98`（es 导出器为仓外 `extract_text2.py`）
