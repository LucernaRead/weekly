# W47 freeze 门加固：解释器/版本断言（防 pt-ko 双栈漂移复发）

**日期**：2026-11-11 12:00 UTC 左右
**改动对象**：`~/workspace/weekly-git/tools/freeze.py`（工作树，未 commit、未 push）
**背景**：`scratch-investigate-fonts/FONT-INVESTIGATION.md` §Q1 证实 pt-ko freeze 0/8
根因是双解释器栈——交付 SVG 由系统 python3（Pillow 10.2.0 / FreeType 2.13.2）
建成，freeze/proof 用 tools/venv（Pillow 13.0.0 / FreeType 2.14.3）复跑，韩语
词间空格量宽差 +1.11px，4 处断行变化。正典栈是 venv（SOP 规定；`tools/requirements.txt`
钉死 `pillow==13.0.0`）。

## 1. 改了 freeze.py 哪几行

完整 exact diff 见同目录 `GUARD-DIFF.txt`（`diff -u freeze.py.before-guard`
→ 安装后 `tools/freeze.py`，61 行新增、3 行改写）。原文件备份在同目录
`freeze.py.before-guard`。改动共 4 处，全部只加 freeze 门，不动构建逻辑：

| # | 位置 | 改动 |
|---|---|---|
| 1 | 模块 docstring（Exit 段后） | 增加 Runtime guard 说明段：正典栈、pt-ko 根因、断言行为 |
| 2 | `sys.path.insert(...)` 之后（约 L41 起） | 新增 guard 块：`REQUIRED_PILLOW_MAJOR = 13`；`runtime_env()`（返回 executable / Pillow / FreeType 版本，Pillow 缺失时返回 `MISSING` 而不抛错）；`runtime_env_dict()`；`check_runtime_env()`（打印 `runtime: <exe> \| Pillow <v> \| FreeType <v>`，Pillow 主版本 ≠ 13 时向 stderr 打 `ABORT: canonical stack is tools/venv Pillow 13.x …` 并返回 2） |
| 3 | `cmd_baseline` / `cmd_diff` 的 JSON 输出 | baseline JSON 增加 `"runtime": {...}`；diff report 增加 `"runtime": {...}`（ stdout 的 runtime 行由 main 统一打，两个子命令都覆盖） |
| 4 | `main()`：`parse_args` 之后、分发之前 | 先调 `check_runtime_env()`，返回非 0 即直接退出（exit 2），任何子命令都不执行。注意：baseline 的子进程用 `sys.executable` 调 `run.py`，与 freeze 自身同一解释器，断言自动覆盖重跑侧 |

**断言口径**：只断言 Pillow 主版本 == 13（任务要求“13.0.0 或至少主版本 13”）。
FreeType 只打印、不单独断言——它随 Pillow 轮子走，当前 venv 为 2.14.3、系统为
2.13.2；若日后 venv 升级 FreeType 而 Pillow 仍为 13.x，不应无故拦住。

**前置状态**：安装前 `tools/freeze.py` 工作树已有未提交改动（2026-11-10 的
mtime fallback，`git diff` 里那段），本次改动叠在它之上，未动它的一行；
`GUARD-DIFF.txt` 只含本次 guard 的差分，不含那段旧改动。

**安装方式**：原子写入——先在 scratch 完成并验证 `freeze.py.new`，再
`cp` 到 `tools/.freeze.py.tmp.<pid>`，`mv`（rename）覆盖 `tools/freeze.py`。
安装时刻正好有一个 proof agent（scratch-proof-zh-tw-es1，PID 18260）在跑
旧版 freeze.py baseline；rename 不影响已加载的旧进程（它继续用旧版跑完），
只影响 rename 之后的新调用。安装后校验：md5 与 scratch 验证过的文件一致
（`bb115a9b7d6f5e5ab4c90ff4c937afa8`），`py_compile` 通过，无临时文件残留。

## 2. 双解释器验证结果（全部在 scratch 进行，未动任何版成品）

| 测试 | 解释器 | 结果 |
|---|---|---|
| `diff --core-svg pt-ko/svg --edition-svg pt-ko/svg` | venv `tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3） | **exit 0**；首行 `runtime: …/tools/venv/bin/python \| Pillow 13.0.0 \| FreeType 2.14.3`；8 页全 +0/-0，added CJK 0；`--json` 里含 `runtime` 字段 |
| 同上 | 系统 `/usr/bin/python3`（Pillow 10.2.0 / FreeType 2.13.2） | **exit 2**；打印 runtime 行后 stderr `ABORT: canonical stack is tools/venv Pillow 13.x (got Pillow 10.2.0 …)`；diff 未执行（无 `--json` 产物） |
| `baseline`（故意用空 core-svg 目录，只测门是否先打印） | venv | runtime 行先打印，随后原有的 `ABORT: core svg dir has 0 SVGs`（exit 2）——断言通过、流程继续 |
| 同上 | 系统 python3 | runtime 行 + guard ABORT（exit 2），`--out` 目录根本没创建——断言在 `cmd_baseline` 做任何事之前拦截 |
| 安装后复测（repo 内 `tools/freeze.py` 本体） | venv / 系统 | 与 scratch 验证完全一致（venv exit 0、系统 exit 2） |

注：第一次 diff 测试误把 edition 根目录当 `--core-svg`（SVG 实际在
`svg/` 子目录），pages 为空、只有 TOTAL 行；与 guard 无关，改用
`pt-ko/svg` 重测后 8 页正常。验证用的 pt-ko SVG 只读，未写回。

## 3. run.py 构建入口：共享还是一版一份？构建侧断言应落在哪一处

**结论：没有共享入口。`run.py` 是一版一份的拷贝，共 121 份。**

- `production/2026-w47/` 下 `find -name run.py` 共 **121 份**（12 个 `core-*` + 109 个
  edition 目录，含 `fanout-nl/` 下的复份）。
- 内容几乎全同，只有 3 个主变体（md5 统计）：78 份标准模板（仅 docstring 的语言名
  不同）；22 份 REGISTRY-STATS 变体（末尾多打 `bslib4.REG` 统计，en/de 两族）；
  11 份 es 族 docstring 变体；另有 10 份 `fanout-nl/` 下的一次性复份各不相同。
  模板本体都是：`os.chdir(本目录)` + `runpy.run_path` 依次跑
  `content12/34/56/7/8.py`。
- 各版目录完全自包含：`content*.py` 一律 `sys.path.insert(0, 本目录)` 后
  `from bslib4 import *`，`bslib4.py` 再 `from svglib import *`；没有任何版
  import 共享模块或 `tools/`。真正量字宽的是各版自己的 `svglib.py`
 （`text_w` → PIL `ImageFont.getlength`），全周共 23 个不同 hash（按目标语族分化）。
- KIT 记录的构建命令是 `tools/venv/bin/python -u run.py`（如 pt-ko KIT L75、
  en-fr KIT L65），但没有任何代码强制它——pt-ko 实际跑的正是系统 python3，
  这就是漂移能悄悄发生的口子。

**构建侧断言落点建议（只报告，不批量改）：**

1. **首选——新共享包装脚本，不动 121 份 run.py**：新增 `tools/run_build.py`，
   先断言（复用与 freeze.py 同款的 Pillow 主版本 13 检查），再 `exec` 目标
   版目录的 `run.py`。只需改 KIT/SOP 的构建命令写法（`tools/venv/bin/python
   tools/run_build.py <版目录>`），一处落地、全周覆盖；但这改的是构建命令
   约定，须另行定夺（SOP 相关，本任务未动）。
2. **次选——`svglib.py` 的量字点**：断言放在 `svglib.text_w`/`_pil` 首次建
   `ImageFont` 时最贴近漂移根因，且每个构建必然经过它。但 `svglib.py` 有 23 个
   变体，须机械扫一遍逐份插入并验 hash；且各版 `svglib.py` 是版资产的一部分，
   批量改属于生产侧改动，须单独立项。
3. **不建议——逐份改 121 个 `run.py`**：量大、易漂移（新版 scaffold 时又会回到
   旧模板），且 run.py 本身不量字宽，断言放它只是“入口检查”，不如包装脚本。
4. **现状已兜底**：freeze baseline 用 `sys.executable` 重跑构建，且现在 freeze
   自身先过 guard——任何用错解释器建出的版，在 proof 环节一定以 0/8 暴露，
   不会再悄悄入库。这是“出货门已锁”，上面 1/2 解决的是“别让 builder 白跑一次”。

**同类暴露、未在本任务动**：`tools/` 里另外三个用 PIL 的工具同样没有版本
打印/断言——`occlusion_audit.py`、`webpdf.py`、`splice_last_keyframe.py`。
若它们也在系统 python3 下被跑过，同样会悄悄量错字（occlusion 审计与 webpdf
的 PDF 侧）。建议后续同款处理，但不在本次 freeze 门任务范围内。

## 4. 未做的事（按任务边界）

- 未改 `SOP.md`；未改任何版的成品与构建代码；未 commit、未 push。
- 未批量改各版 `run.py`（只做了落点调查与建议，见 §3）。
- 本次只改了 `tools/freeze.py` 一个文件（工作树状态仍为 `M tools/freeze.py`，
  其中含安装前就有的 2026-11-10 mtime fallback 未提交改动）。
