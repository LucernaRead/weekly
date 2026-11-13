# FIX-NOTE — tools/freeze.py: ko 家庭 Pillow 版本守卫豁免

日期：2026-11-11（UTC 约 13:07–13:12）｜文件：`~/workspace/weekly-git/tools/freeze.py`（仅此一文件）
状态：**未提交、未 push**（`git status --porcelain`：` M tools/freeze.py`，未进暂存区）

## 背景（已裁定，不另造决定）

- 2026-11-11 12:00，`tools/freeze.py`（未提交）加了 Pillow-13 运行时守卫：`main()` 在 `parse_args` 后调 `check_runtime_env()`，Pillow 主版本 ≠13 即 exit 2 中止。
- 该守卫与 ko 家庭的解释器锁冲突：ko 核心+各版用系统 python3（Pillow 10.2.0）构建；venv（Pillow 13.0.0）量韩文约宽 1.1%（40px：991.3 vs 1002.2），会移动全部断行；venv 下 freeze 0/8 是已记录的对照，不是门禁失败（core-ko `WEEKLY-KIT.md` fix #15，Round 10，见该文件 :82/:108/:115）。
- 已裁定不变量：**按家庭栈一致（build == freeze == core），不是全局 venv 强制**。pt-ko 是把版向 venv 核心看齐；ko 保持系统栈。守卫留着，ko 豁免，不重建。

## 改了哪几行（本次编辑，相对 12:00 已有守卫的版本）

共 +73 / −29 行，净增 44 行。只改 `check_runtime_env` 及相关注释/docstring，另加两个小 helper 与 `main()` 的一行传参：

1. **模块 docstring 的 Runtime guard 段（+6 行净）**：改写为按家庭分流规则——默认要求 Pillow 13，ko 家庭（core-ko 与 `production/` 下 `2026-w47-ko-*` 各版）要求 Pillow 10；说明 venv 下 ko freeze 0/8 是已记录对照（引 core-ko KIT fix #15），pt-ko 已向 venv 核心看齐、ko 留系统栈。
2. **守卫注释块（+9 行净）**：标题改为 "runtime guard (2026-11-11), per family"，写明按家庭栈一致的规则、ko 的 1.1% 量度差与 fix #15 引用、pt-ko 0/8 是反向错配；新增常量 `KO_REQUIRED_PILLOW_MAJOR = 10`（`REQUIRED_PILLOW_MAJOR = 13` 不动）。
3. **新增 `is_ko_family_path(path)`**：任一路径组件 == `core-ko` 或匹配 `^\d{4}-w\d+-ko-` 即属 ko 家庭。
4. **新增 `required_pillow_major(args)`**：baseline 看 `--build`/`--core-svg`，diff 看 `--core-svg`/`--edition-svg`；任一触及 ko 家庭路径即要求 10，否则 13。
5. **`check_runtime_env(required_major=REQUIRED_PILLOW_MAJOR)`**：签名加参数；ko 要求不满足时的中止信息引用 core-ko WEEKLY-KIT.md fix #15，说明"venv 量韩文宽 ~1.1%、全部断行移动、venv freeze 0/8 是既定结果"，并指明重跑用 `/usr/bin/python3`；非 ko 中止信息不变（指明 `tools/venv/bin/python`，引 pt-ko 0/8）。
6. **`main()`**：`check_runtime_env()` → `check_runtime_env(required_pillow_major(args))`。

未动：baseline/diff 的任何逻辑、`runtime` 字段、`CONTENT_ORDER`、子进程调用方式（仍用 `sys.executable`）。`python3 -m py_compile tools/freeze.py` 通过。

## 四种验证（全部跑过，日志在同目录）

TMPDIR 均为本 scratch 目录；`--out`/`--json`/日志均在此。

| # | 命令 | 结果 |
|---|---|---|
| (a) | `/usr/bin/python3 tools/freeze.py baseline --build production/2026-w47/2026-w47-ko-ja --core-svg production/2026-w47/2026-w47-ko-ja/svg --out a-ko-ja --json a-ko-ja.json` | **PASS：8/8，rc=0**。`runtime: /usr/bin/python3 \| Pillow 10.2.0 \| FreeType 2.13.2`；8 页全 OK；core SVG 完整性：发货文件未变。日志 `a-ko-ja.log`，json `a-ko-ja.json`（`runtime.pillow=10.2.0`） |
| (b) | 同上，ko-zh-tw（`--build/--core-svg production/2026-w47/2026-w47-ko-zh-tw…`，`--out b-ko-zh-tw`） | **PASS：8/8，rc=0**。同上，8 页全 OK。日志 `b-ko-zh-tw.log`，json `b-ko-zh-tw.json`（`runtime.pillow=10.2.0`） |
| (c) | `tools/venv/bin/python tools/freeze.py baseline --build …2026-w47-ko-ja --core-svg …/svg --out c-ko-ja-venv` | **PASS：ABORT，rc=2**，且带 ko 豁免信息：`ABORT: ko family builds on system python3 (Pillow 10.x) — core-ko WEEKLY-KIT.md fix #15: the venv (Pillow 13) measures Korean ~1.1% wider and re-wraps every line, so a venv freeze of a ko edition is 0/8 by construction. Got Pillow 13.0.0 at …/tools/venv/bin/python; re-run with /usr/bin/python3.` 日志 `c-ko-ja-venv.log` |
| (d) | `/usr/bin/python3 tools/freeze.py diff --core-svg production/2026-w47/core-pt/svg --edition-svg production/2026-w47/2026-w47-pt-en/svg --json d-pt-diff.json` | **PASS：ABORT，rc=2**（venv 家庭 pt 版，系统解释器被挡）：`ABORT: canonical stack is tools/venv Pillow 13.x (got Pillow 10.2.0 at /usr/bin/python3); re-run with tools/venv/bin/python. A wrong interpreter silently re-measures text (W47 pt-ko freeze 0/8).` 日志 `d-pt-diff.log` |

## 探针与环境备注

- 开工探针：`touch /dev/null` 后 `git hash-object -w` 正常（回 `da0c4eb8…`）；goals 侧 scratch 真实写文件成功（`probe.txt`）；系统 Pillow 10.2.0、venv Pillow 13.0.0 已核对；磁盘 68G 空闲。
- 探针中途 `/dev/null` 消失过一次（`git` 报 `could not open '/dev/null' rc=128`），按任务指引 `touch /dev/null` 垫回后即恢复，不是配额问题；之后每次 git 前都先垫回。
- 工作树另有大量其他 agent 的未提交改动（W43/W47 各版等），本次只动了 `tools/freeze.py` 一个文件，未碰其他文件，未 commit、未 push。

## 交付物

- 改动：`~/workspace/weekly-git/tools/freeze.py`（未提交）
- 本说明：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-freeze-guard/FIX-NOTE.md`
- 验证日志/产物：同目录 `a-ko-ja.log/.json`、`b-ko-zh-tw.log/.json`、`c-ko-ja-venv.log`、`d-pt-diff.log` 及 `a-ko-ja/`、`b-ko-zh-tw/` 重建产物
