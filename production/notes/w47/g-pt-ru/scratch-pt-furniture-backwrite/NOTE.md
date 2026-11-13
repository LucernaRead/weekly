# NOTE — W47 pt 家庭机制表回写：FURN[en] badge372 EXPLICATIONS → EXPLANATIONS

- 任务：只改 `scratch-fanout-pt/furniture.py` 第 12 行一词；其余不动。
- 执行人：回写微任务执行员；时间 2026-11-11（EST）。
- 依据：SOP.md（已读全文）、`hidden_files/w47/briefs/brief-coordinator.md`（已读）、
  `scratch-pt-en-fix1/FIX-LOG.md` §3（背景，动手前已逐项独立核实）。

## 0. 开工探针（双通后动手）

- 探针 1：`echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`。
- 探针 2：本目录真实写 `.probe` 成功（内容 `probe-ok`）。

## 1. 改前独立核实

- 机制表改前（`furniture.py:12`，含 `\u3000` 转义分隔符，与交付值逐字对应）：
  `  "badge372": "TEXT IN PORTUGUESE\u3000EXPLICATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS",`
- 交付值（`~/workspace/weekly-git/production/2026-w47/2026-w47-pt-en/content12.py:19`，已读原文确认）：
  `p.text(975, 372, "TEXT IN PORTUGUESE　EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 16, "sans", False, GREY, anchor="middle")`
- 两者确不一致（仅 EXPLICATIONS / EXPLANATIONS 一词），与 FIX-LOG §3 所述成因一致：
  builder 建版后手工改了交付值、未回写机制表。
- 改前 baseline（编辑前先跑，未动交付目录）：core-pt 新拷至本目录 `repro-before/`，
  `tools/venv/bin/python transform.py <copy> en` → rc=0，`CJK 0 OK`，`TRANSFORM COMPLETE`；
  再生 6 文件 vs 交付版目录：**5/6 一致**，唯一 diff 为 `content12.py:19`（再生 EXPLICATIONS vs 交付 EXPLANATIONS）。

## 2. 改动（仅此一行）

- 文件：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-pt/furniture.py` 第 12 行。
- 改前：
  `  "badge372": "TEXT IN PORTUGUESE\u3000EXPLICATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS",`
- 改后：
  `  "badge372": "TEXT IN PORTUGUESE\u3000EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS",`
- 仅 `EXPLICATIONS` → `EXPLANATIONS` 一词；`\u3000` 分隔符、其余逐字、行号、缩进均未动。
- 未动的 EXPLICATIONS（法语正确拼法，核实保留）：`furniture.py:65`（fr footer）、`:68`（fr badge372）、
  `:75`（fr footer_joined）。改后全文件 grep：`EXPLANATIONS IN ENGLISH` 仅 1 处（en badge372）；
  `EXPLICATIONS` 仅剩上述 3 处法语行。
- Python 导入校验通过：`furniture.FURN['en']['badge372']` 求值后与交付值逐字一致（含 U+3000）。

## 3. 改后验证（transform 复现，scratch 副本内）

- core-pt 新拷至本目录 `repro-after/`，同一命令重跑 transform → rc=0，`CJK 0 OK`，`TRANSFORM COMPLETE`。
- 再生 6 文件 vs 交付版目录 `production/2026-w47/2026-w47-pt-en/` diff：
  `bslib4.py`、`content12.py`、`content34.py`、`content56.py`、`content7.py`、`content8.py` ——
  **6/6 逐字节一致，diff 0 行**；`content12.py:19` 的 diff 已消失。
- 未重渲染、未改任何已交付成品：交付目录 `content12.py:19` 事后 grep 仍为 EXPLANATIONS 原值，
  本任务全程只读该目录；未跑 insert.py、lint --write，未做任何 git 写操作。

## 4. 清理与其他影响

- 两个 39MB 核心副本（`repro-before/`、`repro-after/`）验证完毕后已删除；本目录仅留 `.probe` 与本 NOTE。
- 其他影响：无。除第 12 行外，`furniture.py` 无任何改动；未碰 production/、core-pt、其他家庭、tools/、issues/。
- 遗留：无。本回写即 FIX-LOG §3 / §6 遗留的唯一待定项，现已闭合。
