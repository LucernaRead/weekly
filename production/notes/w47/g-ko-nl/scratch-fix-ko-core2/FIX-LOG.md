# FIX-LOG — ko textmd.py D7 修复 + core-ko text.md 重导（fix2，2026-11-11）

- 修复员：core-ko 返修 builder（叶子，未派 subagent）
- 依据：proof5 `scratch-proof-ko-core5/PROOF-NOTE.md` §4（D7 + D6）、D6 评估
  `scratch-assess-textmd-d6/ASSESSMENT.md` §3.1/§5、D6 工具修复
  `scratch-fix-ko-textmd-d6/FIX-LOG.md`、SOP.md §8、协调员 brief。
- 探针：开工 `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin`
  成功（`9daeafb…`）+ 笔记目录
  `hidden_files/w47/scratch-fix-ko-core2/` 可写；每次写盘前重探，均通过。
  未遇 EDQUOT；`/home/hatch` 余 77G。注意：`/tmp`（512M tmpfs）已 100% 写满，
  本轮一切中间文件均放 workspace scratch，未用 `/tmp`（一次 `sort > /tmp/...`
  写满失败的教训；见 GATE-LOG）。

## 0. 前置核对（D6 工具修复已落地）——通过

改前 5 份 `textmd.py` md5 全同 `d308c826875ad58f604f181e80f0f847`
（core-ko + ko-de/en/es/fr），与 D6 FIX-LOG 记录一致，含 A1 分支。
任一份不符即停手的条件未触发。

## 1. 改动（D7，两处，均在 textmd.py 内，叠在 A1 之上；A2 未采用）

文件：`~/workspace/weekly-git/production/2026-w47/core-ko/textmd.py`
（改后同步到其余 4 份，见 §2）。

### (1) `is_prose()` 的 `/` 拒收规则收窄（`textmd.py:18` 附近）

改前：
```python
if "/" in s or s.endswith((".py", ".pdf", ".svg", ".png", ".jpg", ".md")):
    return False
```
改后：
```python
# D7 (2026-11-11): reject only path-like slashes (no spaces around "/",
# e.g. "assets/x"); " / " is a word-block separator in exercise stems
# (P5/P8 D group: "저는 / 수요일에 / ... → ___") and must be kept.
if re.search(r"\S/\S", s) or s.endswith((".py", ".pdf", ".svg", ".png", ".jpg", ".md")):
    return False
```
逐行说明：
- 只拒两侧无空格的紧凑斜杠（`assets/x`、`a/b` 等路径/文件名形态）；
  练习题面的 ` / ` 分隔符（两侧空格）不再被拒。`s.endswith(...)` 与
  下一行的 `assets/`/`~`/`hidden_files` 拒收原样保留。
- 全仓核查：5 个 content.py 里 ` / ` 只出现在 8 道 D 组造句题面
  （content56:98–104 四题、content8:61–67 四题）；其余 `/` 皆为代码
  （`bw / 2`、f-string 路径 `f"{OUT}/p1-....svg"`——`strings_from` 不处理
  JoinedStr，本来就不收），无合法散文含紧凑斜杠被误伤。

### (2) `CALL_ARGS` 按方法名匹配，不论接收器名（`textmd.py:36` 附近）

新增（紧接 CALL_ARGS 表之后）：
```python
# D7 (2026-11-11): .ex / .match_set are collected by method name, whatever
# the Flow receiver is called. The (receiver, method) table above only
# whitelisted ("f", "ex") / ("f", "match_set"), so the P1 quiz (qf),
# P2-P6 (e) and P7 (a/b/c) exercises were silently dropped (99 items).
METHOD_ARGS = {"ex": [4, 5], "match_set": [2, 3]}
```
`collect()` 循环改动：
```python
method = node.func.attr
idxs = CALL_ARGS.get(key)
if idxs is None:
    idxs = METHOD_ARGS.get(method)
if idxs is not None:
    ...  # 原循环体不变；for idx in CALL_ARGS[key] 改为 for idx in idxs
    # keyword body= for .ex (any receiver)
    for kw in node.keywords:
        if kw.arg in ("body", "opts") and method == "ex":
```
逐行说明：
- 原 `(receiver, method)` 白名单只认 `("f","ex")`/`("f","match_set")`，
  `qf`（P1 闪电问答 4 题）、`e`（P2–P6 78 题 + 3 组 match_set）、
  `a`/`b`/`c`（P7 各 4 题）全漏。现按方法名收：任何接收器的 `.ex` 取
  arg[4,5]、`.match_set` 取 arg[2,3]。
- 参数位核实：全部 7 个接收器（qf/e/a/b/c/f）的 `.ex` 签名同构
  （arg[0] 级别、arg[1] 题型、arg[2] 答案、arg[3] 中文注、arg[4] 韩语题面），
  `.match_set` 同构（arg[0] 级别、arg[1] 中文题型、arg[2] 左列、arg[3] 右列）；
  全仓除这 7 个接收器外无其他 `.ex`/`.match_set` 调用。
- `("f","ex")` 仍走 CALL_ARGS 老路（`METHOD_ARGS` 只作 fallback），
  不重复收集；`p.text` y<200 跳过逻辑、`body=`/`opts=` 关键字逻辑原样保留
  （全仓 grep：无任何 `.ex` 调用用 `body=`/`opts=`）。
- A2（Name 解析 env）未采用：D7 缺口全是字面量参数（arg[4] / 列表项），
  方法名匹配已全覆盖；改动最小优先。

## 2. 同步到 5 份拷贝

先改 core-ko，再 `cp` 到其余 4 份。改后逐份 md5sum（全同）：

| 拷贝 | 改后 md5 |
|---|---|
| `production/2026-w47/core-ko/textmd.py` | `bc6394a387d15d4726e194687320da20` |
| `production/2026-w47/2026-w47-ko-de/textmd.py` | `bc6394a387d15d4726e194687320da20` |
| `production/2026-w47/2026-w47-ko-en/textmd.py` | `bc6394a387d15d4726e194687320da20` |
| `production/2026-w47/2026-w47-ko-es/textmd.py` | `bc6394a387d15d4726e194687320da20` |
| `production/2026-w47/2026-w47-ko-fr/textmd.py` | `bc6394a387d15d4726e194687320da20` |

`python3 -c "ast.parse(...)"` 语法通过。未碰 ru（`ru_textmd.py`）与任何
其他语系导出器，未碰 W46，未动 content 源码。

## 3. 只重导 core-ko text.md（绝不重建 PDF/SVG；绝不重导 fan-out 4 版）

先在 scratch 试跑审 diff，通过后再落盘实盘；实盘与试跑逐字节一致（`cmp` 通过）。
命令（core-ko KIT 解释器锁定：`/usr/bin/python3`，不是 venv）：
```
/usr/bin/python3 textmd.py . 2026-w47-ko-zh-cn 2026-w47-ko-zh-cn.text.md "Lucerna Korean Weekly VOL.4 — Korean text, Chinese explanations (2026-W47)"
```
标题与现文件头一致（`# Lucerna Korean Weekly VOL.4 — Korean text, Chinese explanations (2026-W47)`）。

| | 改前 | 改后 |
|---|---|---|
| 项数 | 333 | **452** |
| 字节 | 26,048 | **34,606** |
| SHA-256 | `ba1b80f8edabc76eac398e34e80718254e1e584966a39a7c5a9a504b5fe9dda3` | `da1d3a323f7c83eb95fe989e59f56ca6a706282c443f20cc5792c3f73468181a` |
| 页 | 8（Page 1–8） | 8（Page 1–8，标题行不变） |

diff 摘要（`diff before dryrun`；详见 GATE-LOG.md）：
- 新增非空行 122，删除非空行 3，净增 **119** 项。预期 434–442 是按
  D7 99 + D6 10 的“缺失出现次数”估的上限；实际 452 的构成已逐行核清：
  - D7 99 次缺失 → 94 个去重字符串（5 处为跨版重复题面，如
    `김치의 날은 언제예요? A. 11월 22일…` 在 qf/e/a 三处出现）；
  - D6 10 段；
  - 另 15 行：子串普查判“在册”、但**独立行缺失**的真内容（见 GATE-LOG §3，
    11 行 SVG 文本节点核实 + 4 行 `___` 题干，SVG 以墨线填空呈现）；
  - 3 行移位（删+增相抵，净 0）：`김장비용`、`한국시리즈 1차전은…`、
    `올해 수험생은 몇 명이에요? …3,271명` 原经 P8 的 `f.*` 路径收在 P8 组下，
    现按题面所属版归到 P2/P4/P6 组——页归属更正，非新增。
- 94 + 10 + 15 = 119，账目闭合。新增行逐行读过：全为韩语题面/配对词/
  框架例句/来信/范文，无 print 调试串、无路径/代码串、无家具串
  （`/` 只出现在 ` / ` 题面分隔符中）。
- fan-out 4 版（ko-en/de/es/fr）**未重导**——按任务书并入 ko 重扩 #3，
  重扩员用已修工具（md5 `bc6394a3…`）重建时自然带出。

## 4. 验证

- 普查复跑（本目录 `census.py`，proof5 方法：AST 取全部 166 个 `.ex` arg[4]
  与 `.match_set` arg[2]/[3] 项 + D6 10 段，空白归一化后查存在性）：
  改前 99 缺失 + D6 10 缺失；**改后 0 缺失 / 0 缺失**（实盘复跑，
  `census-after.log`）。
- KIT 更新：`WEEKLY-KIT.md` line 127 text.md 行改为 34,606 B / 452 项 /
  SHA `da1d3a32…`（附 fix2 注）；line 83 的 `___` 计数由 23 处改为 75 处
  （实测新文件 `___` 出现 75 次，旧 23 次；SVG/PDF 渲染为墨线填空的
  既有裁定不变）。
- 未动项核实：content*.py、8 个 SVG、印刷/网版 PDF 的 mtime 均为任务前
  （08:40–08:47）；印刷 PDF SHA `53bf14ed…`、网版 `9592945a…` 与 proof5
  记录逐字一致。**未重建任何 PDF/SVG，未 commit、未 push。**

## 5. 未做的事

- 未重导任何 fan-out 版 text.md（并入 ko 重扩 #3）。
- 未碰 ru 与其他语系导出器、未碰 W46、不碰 content 源码/PDF/SVG。
- 未 commit、未 push。
