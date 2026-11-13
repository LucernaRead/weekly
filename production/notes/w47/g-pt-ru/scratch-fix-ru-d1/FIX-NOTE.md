# FIX-NOTE — W47 ru fan-out D1：4 处俄语核心层文字被删（全族 10 版）

日期：2026-11-11。工作目录（goals 侧，唯一写盘位置）：
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ru-d1/`
（下称「本目录」）。红线遵守：只读 repo 生产文件，未改盘上 10 个版、未改
core-ru、未 commit、未 push；未碰其他周。交付是修好的机制，不是成品。

## 0. 开工探针（均通过）

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 通
  （返回 `9daeafb9…`，RC=0）。
- goals 侧真实写文件成功（本目录 `probe.txt`）。
- TMPDIR 全程用本目录 `tmp/`（未用 /tmp）。
- 另：`git status --porcelain -- production/2026-w47/` 无任何已跟踪文件的
  修改；`core-ru/` 与 `2026-w47-ru-zh-tw/` 只有其他并行任务留下的未跟踪
  状态，本任务未动它们。

## 1. 落点定位：丢字的不是 apply，是 TM（W46 前例）

### 1.1 4 串的真实形态：混合字面量

4 串在 core-ru 里都不是独立字面量，而是「俄语核心 + 中文译注」拼在
**同一个** Python 字符串常量里（全角空格 U+3000 分隔）：

| # | 位置 | core 字面量（全文） |
|---|---|---|
| 1 | P6 图表标题，`core-ru/content56.py:158` | `ЧЕМ ЗАЙМУТСЯ НА ЭТОЙ НЕДЕЛЕ?　УЧЕБНЫЕ ДАННЫЕ　练习数据` |
| 2 | P6 图表免责声明，`core-ru/content56.py:159` | `Это учебный опрос редакции для упражнений — не настоящая статистика. 这是编辑部练习数据，不是真实调查。` |
| 3 | P7 副标题，`core-ru/content7.py:12`（`p.band` 第 3 参） | `Фокус на язык　Три уровня, три темы　三个级别，三个主题` |
| 4 | P8 副标题，`core-ru/content8.py:12`（`p.band` 第 3 参） | `第8版　Большой тест недели + все ответы` |

核查：core `2026-w47-ru-core.text.md` 459/504/596 行分别含 1、3、4 串；
第 2 串不在 text.md 里（图表注脚，SVG-only，core 与版均如此，见 §3）。

### 1.2 丢字的链条（证据链）

1. **`tm_ru2.py` → `tm2-<lang>.json`（"lit" 桶）是落点。** TM 由 W46
   core-ru → W46 ru-\<lang\> 逐位置对齐生成。W46 当年 10 个版在翻译这
   4 个混合字面量时，已经把其中的俄语段替换成了读者语——TM 只是忠实
   继承了这个前例。10 个语种的 TM 值（`tm2-<lang>.json` "lit"）：
   - #1 `ЧЕМ ЗАЙМУТСЯ НА ЭТОЙ НЕДЕЛЕ?　УЧЕБНЫЕ ДАННЫЕ　练习数据` →
     en `ЧЕМ ЗАЙМУТСЯ НА ЭТОЙ НЕДЕЛЕ?　PRACTICE DATA`、
     zh-tw `ЧЕМ ЗАЙМУТСЯ НА ЭТОЙ НЕДЕЛЕ?　練習數據`（其余 8 语同理，
     只留句首俄语段，中间 `УЧЕБНЫЕ ДАННЫЕ` 被删）。
   - #2 整句俄语被删，只剩读者语译文，如 zh-tw
     `這是編輯部練習數據，不是真實調查。`、en 全句英译。
   - #3 `Фокус на язык　Три уровня, три темы　三个级别，三个主题` →
     zh-tw `Фокус на язык　三個級別，三個主題`（`Три уровня, три темы` 被删）。
   - #4 `第8版　Большой тест недели + все ответы` →
     zh-tw `第8版　本週大測驗 + 所有答案`（俄语副标题被删；其余语种
     页码标记已本地化，如 en `PAGE 8　The big test of the week + all the answers`）。
2. **`build_map.py`（原版）无纠正。** 它把 tm2 原样并入
   `map-<lang>.json`。已核查全部 10 个 `miss-tr-<lang>.json`：**没有任何
   一个语种对这 4 个键写过 override**——丢字值未经任何人工复核就进了 map。
3. **`apply_ru.py` 只是执行者。** `apply_content` 按字面量整串替换
   （`v in m["lit"]` → 整串换掉），没有也不应有子串保留逻辑；所以落点
   不在 apply，在 map 的内容来源（TM 前例 + build_map 无 keep-as-is 层）。

结论：违反 SOP §3「核心层永不更换，换母语只译讲解层」的是 **W46 前例
被 TM 机械继承**；修复必须卡在 `build_map.py` 这一唯一的 map 汇合点，
而不是去改 TM 生成器（tm2 是 W46 历史的如实记录）也不是改 apply。

### 1.3 为何是「整串被替换」而不是「部分被删」

`apply_ru.py:apply_content` 对 AST 字符串常量做整串查表替换。4 个混合
字面量在 map 里各只有一个键，值就是丢了俄语段的读者语版，替换后俄语
段自然整体消失。SVG 里是逐词 `<text>` 元素，所以丢字在 SVG 层面表现为
一批俄语单词消失（对照实验见 §3.3）。

## 2. 修复：改了什么（文件 + 行）

### 2.1 `build_map.py`（本目录，基于 `scratch-fanout-ru/build_map.py`）

- **第 20–100 行：新增 `KEEP_AS_IS` 表**——4 个字面量 × 10 语种
  = 40 个显式值。每个值 = **俄语段逐字保留 + 读者语译注并列**，
  与 core 的做法一致（俄语在前、译注在后）：
  - zh-tw：`ЧЕМ ЗАЙМУТСЯ НА ЭТОЙ НЕДЕЛЕ?　УЧЕБНЫЕ ДАННЫЕ　練習數據` /
    `Это учебный опрос редакции для упражнений — не настоящая статистика. 這是編輯部練習數據，不是真實調查。` /
    `Фокус на язык　Три уровня, три темы　三個級別，三個主題` /
    `第8版　Большой тест недели + все ответы`（`第8版` 本就是读者语形式，
    整串与 core 相同）。
  - 其余 9 语：译注取自 W46 TM 值的读者语部分（规则见表下注释：
    #1/#3 取 TM 值末段 U+3000 段；#2 取 TM 值整体作译注；#4 取 TM 值
    首段页码标记 + 保留的俄语副标题）。俄语段全部逐字取自 W47 core-ru，
    生成时经断言校验（形状断言全过：TM 值均为「保留段 + 译注」两段式）。
- **第 105–118 行：override 块**，在 tm2 + miss-tr 合并**之后**执行，
  因此胜过两者；键不在 map 里时记为 problem（tripwire，exit 1），
  防止 core 改字面量后静默失效；每次运行打印
  `KEEP-AS-IS overrides applied: 4 (of 4)`。
- **第 16–18 行：输入/输出分离**——输入仍读 `RU_FANOUT_SRC`
  （默认 `scratch-fanout-ru`，只读），map 写到脚本所在目录。
  其余逻辑与原版逐字相同。

### 2.2 `apply_ru.py`（本目录，基于 `scratch-fanout-ru/apply_ru.py`）

**无逻辑改动**，只加两个参数化点（修复本身在 map，不在 apply）：
- 第 27、117 行：`RU_FANOUT_MAPDIR`（默认脚本所在目录）指定 map 位置；
- 第 118–119 行：`argv[2]` 可选 `outroot`（默认仍为生产
  `production/2026-w47/`，即真实 fan-out 路径）；验证时传了 goals 侧
  scratch 路径，绝不写生产。`diff` 原版仅上述 3 处 + docstring。

### 2.3 未动的文件

- `tm_ru.py` / `tm_ru2.py`：未动。tm2 是 W46 历史的如实记录，改它等于
  篡改前例；权威纠正点是 `build_map.py` 的 override。
- `scratch-fanout-ru/` 原版文件、core-ru、盘上 10 个版：未动
  （mtime 见 §0；`map-zh-tw.json` 仍为 11-11 06:38 原版）。
- it 族参考：`scratch-fanout-it/translations.py` 是手写逐语种译表，
  其中「`翻译` 须译出、W46 前例被推翻」的修法（2026-11-11）与本修复
  同构：前例错了就由手写表在汇合点纠正，不动 TM。

## 3. 验证：修好的机制在 scratch 重跑 ru-zh-tw

### 3.1 10 语种 map 再生成（`maps/`，日志 `maps/build_map-<lang>.log`）

每语 `KEEP-AS-IS overrides applied: 4 (of 4)`。exit 0，仅 ko、zh-tw
exit 1——均为**原有** miss-tr deliberate override（tripwire，非本修复引入）：
ko 2 项（`мокрый снег`、`синоптики обещают`），zh-tw 4 项（与
`scratch-fanout-ru/zh-tw/RECORD.md` §3 所列 4 项完全一致：`講解｜` 去重、
`範文` 繁体纠正）。无 `KEEP-AS-IS key missing`。

新 map 与原版 map 的 diff：
- en / de / es / pt / ko / zh-tw：**恰好 8 行不同**（4 键 × 旧值+新值），
  其余逐字节相同。
- fr / it / nl / ja 除 4 键外另有差异——**不是本修复引入的**，而是原版
  map 在 build 之后手工改过、从未写回 tm2/miss-tr 的值（见 §4 的重推提醒）：
  fr 49 值、it 13 值、nl 3 值（均为卷引号 `’`→直引号 `'` 的手工修复，
  原版 map 各剩 1 个 `’` 未改，属逐值手工挑选）；ja 3 值（`解説 —`
  前缀剥离 + 措辞缩短，见 ja RECORD）。

### 3.2 重跑（`rebuild-ru-zh-tw/2026-w47-ru-zh-tw/`）

- `RU_FANOUT_MAPDIR=maps/ apply_ru.py zh-tw rebuild-ru-zh-tw`：
  `apply OK, no unmapped literals`。重跑前已 grep 确认：复制出的源码
  无任何指向 `weekly-git/production` 的绝对路径。
- 4 串在应用后源码中的位置：
  `content56.py:158`（P6 标题）、`:159`（P6 免责声明）、
  `content7.py:12`（P7 副标题）、`content8.py:12`（P8 副标题）。
- `run.py` exit 0，TOTAL 150（A2 50 / B1 76 / B2 24，与原版 RECORD 一致），
  生成 8 个 SVG；`ru_textmd.py` 生成 text.md 60,887 字节 / 150 题 / 277 blocks。

### 3.3 4 串出现位置（验证脚本 `verify_ru_zh_tw.py`，exit 0，全 17 项 PASS）

SVG 文本以 `tools/freeze.py` 的 `load_texts` 提取后**无间隔拼接**
（SVG 是逐词 `<text>` 元素，且分隔符本身也是独立元素：`' '`、`　`、
`', '`、`'— '`；用空格拼接会把 `', '` 拼成 ` ,`、把 `'.'` 拼成 ` .`，
整串 grep 为 0 是正常的，必须用无间隔拼接或 freeze diff 查）：

| 串 | SVG（重跑版） | text.md（重跑版） |
|---|---|---|
| 1 `УЧЕБНЫЕ ДАННЫЕ` | p6-razbor.svg 拼接文本第 1452 字起 | 第 459 行 `### ЧЕМ ЗАЙМУТСЯ НА ЭТОЙ НЕДЕЛЕ? · УЧЕБНЫЕ ДАННЫЕ · 練習數據` |
| 2 免责声明整句 | p6-razbor.svg 第 1471 字起 | ——（不在 text.md；core text.md 里也没有，图表注脚 SVG-only，属设计如此） |
| 3 `Три уровня, три темы` | p7-yazyk.svg 第 28 字起 | 第 504 行 `### ЯЗЫК · 語言 — Фокус на язык · Три уровня, три темы · 三個級別，三個主題` |
| 4 `Большой тест недели + все ответы` | p8-test.svg 第 30 字起 | 第 596 行 `### ТЕСТ И ОТВЕТЫ · 練習與答案 — 第 8 版 · Большой тест недели + все ответы` |

text.md 其余两项 PASS：第 2 串在 core text.md 与重跑版 text.md 中均
**不存在**（一致）；1、3、4 串在重跑版 text.md 中存在。

### 3.4 freeze diff 全版审计（`tools/freeze.py diff`，共享工具）

- **core → 重跑版**（`freeze-diff-rebuilt.json`）：removed 共 317 串；
  含西里尔字母的**仅 1 串**：p8 `можно` ×1，即已知合法项——P8 Q46
  答案注 `— можно + 不定式` → `可以 + 不定式`（讲解层本地化，
  `content34.py:103` 的 `note` 参）。除此之外删串中**零西里尔字母**。✅
  （p3 的两个 `можно` 是练习题干原词，未动；p8 剩下的一个 `можно` 是
  Q46 答案句 `Вечером можно посмотреть фильм в кино.` 中的原词，未动。）
- **对照实验 core → 已发版（破损版）**（`freeze-diff-shipped-control.json`）：
  removed 含西里尔字母 22 词（除 Q46 的 `можно` 外），包括
  `УЧЕБНЫЕ`、`ДАННЫЕ`、`Это`、`учебный`、`опрос`、`редакции`、`для`、
  `упражнений`、`не`、`настоящая`、`статистика`、`Три`、`уровня`、`темы`、
  `Большой`、`тест`、`недели`、`все`、`ответы` 等——审计**能抓到**这个
  bug；另有 `желании` 1 词，来自 D2/D6 core 修复（见下），不属本 bug。
- **text.md 审计**（已发版 vs 重跑版行级 diff）：恰好 12 行不同
  （6 对），全部可解释——3 对是 KEEP 标题行，另 3 对是 core 在
  11-11 当天晚于已发版（09:41）才落地的 D2/D6 修复（core
  `content12.py` 注释为证，core 11:50–11:55 重渲染）：Q20 答案
  `желание`→`желании`（前置格纠正）、Q25 配对选项
  `Международный день студента`→`День студента`（超宽修复）。
  其余 832 行逐字相同。顺带：RECORD 所写已发版 text.md
  「54,642 字节 / 203 blocks」与盘上实物（60,815 字节）不符；
  用已发版源码原样重跑 `ru_textmd.py` 得到 60,815 字节 / 277 blocks，
  与盘上文件**逐字节相同**——277 才是自洽数，RECORD 数字已过期。
- **基线移动说明**：验证期间（12:04）有其他并行任务重渲染了 core
  p1–p6 SVG，freeze diff 的 removed 总数因此由 308 变为 317；
  移动前后审计结论不变（删串西里尔字母始终仅 Q46 `можно` 1 项），
  移动后连续两次 diff 结果完全相同（已稳定）。

## 4. 给协调员的重推提醒（未做的事）

1. **重推全族 10 版时，二选一**：(a) 用本目录修好的 `build_map.py`
   再生成 10 个 map，再**逐值补回** fr（49）、it（13）、nl（3）的
   `’`→`'` 手工修复与 ja（3）的措辞修复——精确值表可用
   `diff scratch-fanout-ru/map-<lang>.json maps/map-<lang>.json`
   恢复；或 (b) 不动现有 map，只把 `KEEP_AS_IS` 的 4 个值手术式写入
   现有 `map-<lang>.json`。两种路线的终态 map 应当相同。
2. **恢复的俄语比丢字版长**（P6 标题多 `УЧЕБНЫЕ ДАННЫЕ`、P8 副标题
   多整段俄语），版式宽度须重过门：occlusion 审计、p8 提取、check_core、
   §1.1 一个不能少（本次验证只做了 SVG/text.md，未跑 render/PDF/门禁）。
3. 本目录 `rebuild-ru-zh-tw/` 只是验证用重跑版（8.6M，无 PDF），
   **不是成品**，不要直接把它当版发；正式版仍由协调员按 fan-out
   流程重推。
4. 若未来 core 再改这 4 个字面量原文，`KEEP_AS_IS` 的键会命中
   tripwire（exit 1 + `KEEP-AS-IS key missing from map`），届时同步
   更新表即可；TM 本身无需动。

## 5. 本目录文件清单

| 文件 | 说明 |
|---|---|
| `FIX-NOTE.md` | 本文件 |
| `build_map.py` | 修好的 map 生成机制（§2.1） |
| `apply_ru.py` | 同上，仅加 outroot/MAPDIR 参数（§2.2） |
| `verify_ru_zh_tw.py` | 验证脚本（§3，exit 0） |
| `maps/map-<lang>.json` | 修好机制再生成的 10 语种 map |
| `maps/build_map-<lang>.log` | 各语种 build_map 输出 |
| `rebuild-ru-zh-tw/2026-w47-ru-zh-tw/` | 重跑的 ru-zh-tw 版（svg/ + text.md + `run.log`/`textmd.log`） |
| `freeze-diff-rebuilt.json` | core → 重跑版 freeze diff 全量 |
| `freeze-diff-shipped-control.json` | core → 已发版 freeze diff 全量（对照） |
| `tmp/` | TMPDIR；含 `shipped-textmd-rerun.md`（已发版源码重跑 text.md，与盘上文件逐字节相同） |
| `probe.txt` | 开工探针 |
