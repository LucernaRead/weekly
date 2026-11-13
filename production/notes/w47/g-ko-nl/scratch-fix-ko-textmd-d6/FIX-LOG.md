# FIX-LOG — ko textmd.py D6 修复（2026-11-11）

- 修复员：ko textmd 工具修复员（叶子）
- 依据：`scratch-assess-textmd-d6/ASSESSMENT.md` §3.1 与 §5-A（推荐方案 A、ko 部分）
- 探针：开工 `git hash-object -w` 成功 + 笔记目录可写；每次写盘前重探，均通过；未遇 EDQUOT。

## 1. 改动（方案 A1，唯一改动；A2 未采用）

文件：`~/workspace/weekly-git/production/2026-w47/core-ko/textmd.py` 的 `collect()`，
在既有“模块级 List/Tuple/Dict 常量”分支之后新增一条分支（7 行注释 + 3 行代码）：

```python
# A1 (D6 fix 2026-11-11): module-level plain-string assignments
# (wt/lt/lcn/etvous/MODELO...). A top-level `x = "..."` is prose
# used twice (wrap() for box height + p.para/f.para print); the
# List/Tuple/Dict branch above never sees it and strings_from()
# drops ast.Name args, so these were silently missing from text.md.
if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
    if is_prose(node.value.value):
        items.append((cur, node.value.lineno, seq, node.value.value)); seq += 1
```

改动逐行说明：
- 条件只认 `Assign` + 值是 `Constant` str：与既有 List/Tuple/Dict 分支并列、同在
  `for stmt in tree.body: for node in ast.walk(stmt)` 循环内，页码 `cur` 由同一循环的
  CURPAGE 追踪给出，新增项落在正确的 `## Page N` 下（核验见 GATE-LOG）。
- 仍过 `is_prose` 门：短串/路径/文件名照旧排除；`print()` 参数不是赋值，不会被收
  （评估报告担心的 "P7 col3 ends" 类调试串不在此列）。
- A2（Name 解析 env）未采用：改前全量 AST 扫描证明 5 版 5 个 content 文件里的
  plain-string 赋值**恰好等于**漏载清单（core-ko 10 段、各 fan-out 8 段，全部顶级、
  全部 `is_prose=True`，无嵌套、无遗漏），A1 已全覆盖，改动最小优先。

## 2. 同步到 5 份拷贝

改前 5 份 md5 相同：`e01fe8dd80ed38cfab970e2840721c39`。
先改 core-ko，再 `cp core-ko/textmd.py` 到其余 4 份。改后逐份 md5sum：

| 拷贝 | 改后 md5 |
|---|---|
| `production/2026-w47/core-ko/textmd.py` | `d308c826875ad58f604f181e80f0f847` |
| `production/2026-w47/2026-w47-ko-de/textmd.py` | `d308c826875ad58f604f181e80f0f847` |
| `production/2026-w47/2026-w47-ko-en/textmd.py` | `d308c826875ad58f604f181e80f0f847` |
| `production/2026-w47/2026-w47-ko-es/textmd.py` | `d308c826875ad58f604f181e80f0f847` |
| `production/2026-w47/2026-w47-ko-fr/textmd.py` | `d308c826875ad58f604f181e80f0f847` |

5 份一致。未碰 ru（`ru_textmd.py`）与任何其他语系导出器，未碰 W46，未动 content 源码。

## 3. 未做的事

- **未重导任何版目录下的 text.md**（core-ko proof5 正在用当前 text.md 做复校对象）。
  正式重导由协调员在 proof5 落定 + ko 重扩 #3 时另派。
- 未 commit、未 push。
