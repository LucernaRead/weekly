# FIX-LOG — ru 家庭 textmd D6 修复（2026-W47，2026-11-11）

修复员：ru_textmd 叶子 fixer。范围：`ru_textmd.py`（11 份相同拷贝）+ 11 版
`*.text.md` 重导（core-ru 版有两个同名文件，均重导，见 §4）。不碰 PDF/SVG、
不碰 content 源码、不碰 ko 与其余 10 语系、不 commit、不 push。

评估依据：`../scratch-assess-textmd-d6/ASSESSMENT.md` §3.2、§5-A（推荐方案 A）；
SOP §8（只动次要导出物，不重跑复校）；AGENTS.md §Add an edition r.4
（text.md 从生产源稿导出，绝不从 PDF 回抽）。

## 0. 探针（每次写盘前重探，均通过）

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb…`，RC=0
- 笔记目录 `scratch-fix-ru-textmd-d6/` 可写；`df` 可用 77G，未遇 EDQUOT。

## 1. 诊：评估的 39 是低估——真缺口是 66 段去重内容/版

评估的 `ppara_census.py` 用**一个全局 loopmap** 记同名循环变量：同一文件内
多处 `for t in …`（facts/ideas/tab；facts/cal/pc）后写的覆盖先写的，于是
`content34.py:42/53/140` 三处都被算成 `tab` 的 4 行、`content56.py:45/129/139`
三处都被算成 `pc` 的 2 行；且 `enumerate(...)` 循环（P1 目录 topics、P2 词表
words、P7 金句 quotes）根本不在其解析范围。评估 §6 自己注明了同名循环变量
的串位风险，但 ru 的 39 只做了抽查，未逐项裁决。

本修复自写 `census_true.py`（存本目录，只读）：**逐循环归属**（Name 迭代与
`enumerate(Name)`、元组目标递归解构）+ 双片段（与 `verify_d6_v2.py` 同规则）
核查现版 text.md。

core-ru 真实普查（修前）：**p.para 共 74 处、73 个去重字符串、在册 7、缺失 66**。

| 来源 | 缺段（去重） | 说明 |
|---|---|---|
| 行内字面量 + plain 变量 | 14 | :30、:106、:107、:196 etvous、:197、:222、:173 nteam、:155 图例、:90 wt、:91、:101 lt、:102 disc_ru、:103 disc_cn、:129 下期预告 |
| brefs/last（P1 快讯/P2 节日表） | 2 + 5 | 各 3/7 项，1 项与 2 项已在正文 f.para 里出现 |
| P1 目录 topics（enumerate） | 5 | `1. …`～`5. …` |
| P2 词表 words lab/cn（enumerate） | 5 | 8 项中 3 项已在 P7 桥接/习题里出现 |
| P3 facts/ideas、P4 tab | 6 + 3 + 4 | 评估把三处压成 4 行，实为 13 行 |
| P5 facts、P6 cal/pc | 5 + 3 + 2 | 评估把三处压成 2 行，实为 10 行新段（各 1 项已在正文） |
| P7 易错诊所 errs | 12 | wrong/right/cn 各 4 行 |

66 = 39（评估数）+ 27：facts/ideas/tab +9、facts/cal/pc +8、topics +5、words +5。
在册 7 段（双片段核验 + 直接 grep）：`18 ноября — день рождения Деда Мороза.`（brefs/last
共用）、`22 ноября — День психолога.`、`тепло зимой: снег тает`、`дождь, который замерзает`、
`лёд на дороге`、`«Киберпонедельник» — 30 ноября.`、无句点的 `18 ноября — день рождения Деда Мороза`
（cal）——均以子串形式已在正文/习题里出现。修后它们在框位再出现一次（ faithfully：
PDF 里同一句子印两遍——框内一次、正文一次），`add()` 不去重，任务亦令去重/排序不变，
故不作抑制。

## 2. 工具改动（`core-ru/ru_textmd.py`，后同步 11 份）

四处，逐行见文件内 `D6 fix (2026-11-11)` 注释：

1. **`do_call()` 加 `p.para`/`p.paraq` 分支**（评估方案 A 原意）。`p.paraq` 全仓
   无定义、无调用，顺手同款覆盖。
2. **`do_p_para()` + `is_prose_para()`**：与 `f.para` 同款 `ev_str + add_para()`，
   另有一道 prose 过滤——只拦空白串与 `— СТРАНИЦА` 页脚分隔行（本期 p.para 无此
   类调用，纯属后手；附录自己的 `— СТРАНИЦА ? —` 由 `do_appendix` 发，不受影响）。
3. **`walk_stmt()` 的 `For` 加循环绑定**（`loop_items()` + `bind_target()`）：迭
   代器为常量列表/元组名的 `for ... in <name>` 与 `enumerate(<name>)` 按项走
   一遍 body、目标递归解构绑定，循环结束恢复 env；其余迭代器（range、切片、
   sorted、REG）沿用旧路单走一遍。`quotes` 列表永不绑定——它已有 `do_assign`
   的专属导出分支，绑定会使金句块在文件里出现两次。循环体内无 `ex`/`match_set`/
   `caption`/`band`/CURPAGE 赋值（全量核查过），故绑定不扰动题号与分页；
   p.text 循环项字号均 < 24 或不合 deck 条件，`do_p_text` 照旧跳过。
4. **`do_assign()` 分发赋值内的嵌套调用**：把 `isinstance(value, ast.Call)` 改为
   `ast.walk(value)` 逐个 Call 分发。`wrap/sum/len` 等 `do_call` 不认的调用照旧
   忽略，布局算术无害。

### 两处干跑抓出的错（已修，均在 FIX-LOG 留档）

- **错 1——`args[0]` 是错的。**评估 §5-A 与任务简述都说“与 f.para 同款走
  `ev_str(call.args[0], env)`”。实测：`p.para(x, y, s, …)`（svglib.py:263）
  正文在 **args[2]**，args[0] 是 x 坐标——`ev_str` 对数字报 "not a string"，
  分支悄无声息一行不发。第一版干跑输出 54,666 字节/202 块，比原文件还小，
  由此发现。已改 args[2]；`p.paraq` 无定义，暂按同样约定。
- **错 2——`muse.edit` 的 old_text 含 `elif isinstance(node, ast.If):` 而 new_text
  没写回**，导致 `If` 分支整段丢失 + For 体残留一遍重复 walk。后果：P8
  Morozko 图注（在 `if af.ci == 3` 块里）丢了一块（202 vs 203 块）。已恢复
  If 分支、删净残留。教训：改 `walk_stmt` 这类 elif 链时，new_text 必须把
  锚点行原样带回；改后通读整函数核对。

## 3. 改后验证（core-ru 干跑，未动原文件）

命令（KIT 形式，`tools/venv/bin/python`）：

```
cd production/2026-w47/core-ru
~/workspace/weekly-git/tools/venv/bin/python ru_textmd.py . \
  <out> "VOL.4 · Russian text · Simplified Chinese explanations"
```

干跑输出（`/tmp` 曾被回收，干跑件存本目录 `dryrun-core-ru.text.md`）：
**60,980 字节（原 54,801）、838 行（原 690）、150 题（不变）、277 块（原 203，+74）**。

逐版 diff（`diff-core-ru.txt`，相对原文件）：

- 删除 **0 行**；新增 **148 行 = 74 段 + 74 个空行分隔**；17 个纯增 hunk，
  自 P1 至 P7 按阅读顺序分布，无一 `c`/`d` hunk。
- 74 段与 §1 普查逐项核对一致：66 段真正新内容 + 7 段已在册字符串在框位
  再现 + `18 ноября — день рождения Деда Мороза.` 在 brefs/last 两框各出现一次
  （普查 73 去重 + 1 重复 = 74）。
- 格式：`### ` 行 46 = 46（无新增标题层级）；`> ` 行 16 = 16（金句未重复，
  quotes carve-out 生效）；全文唯一的 `СТРАНИЦА` 是附录自带的 `— СТРАНИЦА ? —`
  （行 668）；家具串 0；`add()` 去重/排序未动；题号/答案键未动（题数仍 150）。
- 普查复跑（`census_true.py` 对干跑件）：74 处中 69 项在册，余 4 项
  （`解冻、回暖`/`湿雪`/`冻雨`/`路面结冰`）是双片段规则本身的盲区——字符串
  去空白后仅 2–6 字符、凑不够 8 字符 head，永远通不过该规则；直接 grep 证实
  四者均以整行在干跑件中（各 6–8 次命中）。

## 4. core-ru 有两个同名文件

`2026-w47-ru-core.text.md` 与 `2026-w47-ru-zh-cn.text.md` 在修前 md5 相同
（`7b876c41…`），KIT §5 已记“字节一致（cmp 已验）”——同一版（ru × zh-cn）在
core 目录下的两个名字。重导时两文件用同一命令各写一次，保持一致；
“11 版”指 11 个版，core-ru 版占其中两个文件名。

## 5. 同步与重导

- 工具同步：11 份 md5（改后）——**`0d42818e5fcdb88764411f9ae5f70942`**，逐份验同，
  无一漏。改前 11 份同为 `1a03d0407a9e50ad79f4fc191c27207d`（评估已记）。
- 各版重导：KIT 命令形（`tools/venv/bin/python ru_textmd.py . <out> "<title>"`），
  title 均取各版原文件头；`reexport.sh`（存本目录）逐版备份旧件→重导→diff，
  12 次导出全部 RC=0、无一失败。重导前 12 文件均为 690 行 / 203 块；
  重导后均为 **838 行 / 277 块、150 题不变**，每版 diff 均为 **+148 行 / -0 行**
  （74 段 + 74 个空行分隔）。两份 core-ru 文件重导后 md5 仍相同
  （`7df02ed31b874cdae2a6403a9db280c1`），且与干跑件逐字节一致（导出确定性已验）。

| 版 | 重导前（行/字节/块） | 重导后（行/字节/块） | 新增段 | diff 审 |
|---|---|---|---|---|
| core-ru（ru-core + ru-zh-cn 两文件） | 690 / 54,801 / 203 | 838 / 60,980 / 277 | 74 | 见 §3，已审 |
| ru-de | 690 / 57,310 / 203 | 838 / 63,452 / 277 | 74 | 结构同 core，逐段属本版源文件（普查复跑 0 缺） |
| ru-en | 690 / 56,600 / 203 | 838 / 62,769 / 277 | 74 | 同上 |
| ru-es | 690 / 58,041 / 203 | 838 / 64,161 / 277 | 74 | 同上 |
| ru-fr | 690 / 57,356 / 203 | 838 / 63,489 / 277 | 74 | 同上 |
| ru-it | 690 / 57,852 / 203 | 838 / 63,962 / 277 | 74 | 同上 |
| ru-ja | 690 / 58,308 / 203 | 838 / 64,451 / 277 | 74 | 同上 |
| ru-ko | 690 / 58,811 / 203 | 838 / 65,002 / 277 | 74 | 同上 |
| ru-nl | 690 / 57,863 / 203 | 838 / 63,984 / 277 | 74 | 同上 |
| ru-pt | 690 / 58,994 / 203 | 838 / 65,098 / 277 | 74 | 同上 |
| ru-zh-tw | 690 / 54,642 / 203 | 838 / 60,815 / 277 | 74 | 同上 |

每版 diff 结构复核（`diffs/*.diff`）：74 段非空新增 + 74 空行、删除 0 行、
新增 `### ` 0 行、新增 `> ` 0 行、新增 `СТРАНИЦА` 0 行。新增段逐版属该版
自己的 content 源文件——D6 六段逐版核对，各版 `disc_cn` 均为本版母语译文
（德/英/西/法/意/日/韩/荷/葡/繁中各一），无跨版串文。

## 6. 核验脚本输出（见 GATE-LOG.md）

- `detect_d6.py` + `verify_d6_v2.py` 复跑（重导后，输出存本目录
  `d6-scan-after.json` / `verify2-after.json`）：681 段核查，ru 家庭 11 版
  **各 7/7 在册、0 缺失**。其余缺失与本任务无关：ko-de/en/es/fr 各 8
  （ko 家庭，另一 fixer 的范围，本任务禁碰）；es 家庭 `bb` 各 1（评估 §6
  已裁决的误报，grep 证实在册）；2026-w47-fr-nl 尚无 text.md。
- `census_true.py` 逐版复跑：11 版均为 74 处 / 73 去重，余下“缺失”0–4 项
  均为短词双片段规则的结构性盲区（去空白后 < 8 字符，如 `湿雪`/`wet snow`/
  `Dooi`），直接 grep 证实每项均已在新文件内（各 1–8 次命中）。
- D6 六段（etvous/wt/lt/disc_ru/disc_cn/nteam）逐版双片段核对：11 版全在册，
  且各版 `disc_cn` 为本版母语译文。

## 7. 未动清单

- 未碰任何 PDF/SVG（含 ru-en 网页 PDF 斜体修复并行线，只动 web PDF 与
  `tools/webpdf.py`，与本任务无交集）；未重建、不重跑复校。
- 未碰 ko 与其余 10 语系的导出器、W46 旧版、content 源码、index.json。
- 未 commit、未 push。production/2026-w47/ 整目录未入仓（`git status` 为 `??`），
  本次只改工作树内文件。
- 过程记录：改工具时未把原版 `ru_textmd.py`（md5 `1a03d040…`）另存备份——
  原版可按本 LOG §2 的四处改动逐项还原，评估报告亦存有其 md5；旧版 text.md
  12 份全文备份在本目录 `before/`，可一键回滚。语法检查时 `python3 -m py_compile`
  在 `core-ru/__pycache__/` 落了一个 `ru_textmd.cpython-312.pyc`，已删除；
  导出器本身以 `dont_write_bytecode` 运行，不写 pyc。
- 观察（非本任务范围，不处理）：`detect_d6.py` 重扫时 content12/34 的行号
  较评估快照移了 5–6 行（etvous :196→:190、nteam :173→:168），content7 行号
  未变；重导用的是当前源文件，核验 7/7 通过，故无影响，记录备查。
