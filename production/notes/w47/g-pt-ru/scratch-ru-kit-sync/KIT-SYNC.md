# KIT 同步记录 — W47 俄文核心版（ru）

- 同步员：KIT 同步员（叶子）
- 日期：2026-11-11 01:02 EST（约 2026-11-10 20:02 EST 任务下达后执行）
- 对象：`~/workspace/weekly-git/production/2026-w47/core-ru/WEEKLY-KIT.md`（仅此一文件）
- 依据：第二轮复校记录 `/tmp/scratch-proof-ru2/PROOF-NOTE.md`（全文为准；该记录因磁盘配额故障暂存 /tmp，未移回 hidden_files/w47/scratch-proof-ru2/）；SOP.md 已读（只读）。
- 范围：只改 KIT 纯文字。不动源码、SVG、PDF、text.md；未跑构建/渲染/insert.py / lint --write / git push / add / reset / stash；未提交；未碰 W43/W45/W46 与其他目标语；未查邮箱。

## 1. 写探针（开工，两次全通才动手）

| 轮次 | git hash-object -w | 真实文件写 | 结果 |
|---|---|---|---|
| 第 1 轮 | `cac404bf126783058e990c2404bea1758c6abcb9` | `scratch-ru-kit-sync/probe1.txt`（7 字节） | 通 |
| 第 2 轮 | `ab31f066a1c52e4975437c2513277e1fea811346` | `scratch-ru-kit-sync/probe2.txt`（7 字节） | 通 |

- 记录目录 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ru-kit-sync/` 正常创建（`mkdir -p` OK），未复现复校轮的 `Disk quota exceeded`；`df` 显示 /home/hatch 仍有 46G 可用。
- 探针文件 probe1.txt / probe2.txt 保留在本目录作证据。

## 2. 实测核对（改前自测，与复校员数值逐项一致）

| 文件 | 实测字节 | SHA-256（实测） | 行数 |
|---|---|---|---|
| `Lucerna-VOL4.pdf`（印版） | 31,429,156 | `4b56429722dbbf4573eb80bf24a7d4ae8daf6a7217fd01537c26801fc4411868` | — |
| `Lucerna-VOL4-web.pdf`（网版） | 3,992,881 | `8a2649263171727ecfb2118e3f85bc1ddfc8a0c1f23730e66652ba78e358fca7` | — |
| `2026-w47-ru-zh-cn.text.md` | 54,801 | `08fc397b045a6afa9e08ec00eb1191f9f33954352a775ebca3d62660ab2b3739` | 690 |
| `2026-w47-ru-core.text.md` | 54,801 | （与 zh-cn 版字节一致，cmp 已由复校员验） | 690 |

- 改前 KIT 全文 grep `4e14b1ae` / `91106aa4` / `4b564297` / `8a264926`：0 命中（与复校员结论一致——无 SHA 可改，只有旧字节数）。
- §7.3 全部数值核对：§7.3 原文本无 PDF/text 字节数（只有 8191 字符、42 TEXTX、9.75pt、150/150、97 词等，复校员已复核一致）；印版 31,429,156 / 网版 3,992,881 / text.md 54,801 三项实测值已随新增 SHA 行一并写入 §7.3（见 §3 第 5 行）。§7.4 的 pdftotext 字节 56,102 / 56,050 未动——那是 pdftotext 提取字节（复校员用 `-raw` 模式得 54,870 / 55,129，方法不同数不同属预期），不是文件大小。
- §9 印版 31,429,156 字节改前已正确，未动；§9 无其他数值，无需改。

## 3. 改前 → 改后逐行对照

共 5 处编辑（4 处数值订正 + 1 行新增）。新增行使后续行号 +1（原 111→112、122→123、125→126）。

### (1) §5 第 61 行 — text.md 字节

- 改前：`W47 导出：54,802 字节、690 行、150 题、203 块；`
- 改后：`W47 导出：54,801 字节、690 行、150 题、203 块；`
- 其余（690 行、150 题、203 块、582 行）不动。

### (2) §7.4 第 111→112 行 — 网版字节

- 改前：`网版：tools/webpdf.py svg Lucerna-VOL4-web.pdf → 3,992,897 字节（<7 MB），8 页，pdftotext 56,102 字节；印版 56,050 字节，均 >0。`
- 改后：`网版：tools/webpdf.py svg Lucerna-VOL4-web.pdf → 3,992,881 字节（<7 MB），8 页，pdftotext 56,102 字节；印版 56,050 字节，均 >0。`

### (3) §9 第 122→123 行 — 网版字节

- 改前：`网版 PDF：production/2026-w47/core-ru/Lucerna-VOL4-web.pdf——3,992,897 字节，8 页（<7 MB，文本层 56,102 字节）`
- 改后：`网版 PDF：production/2026-w47/core-ru/Lucerna-VOL4-web.pdf——3,992,881 字节，8 页（<7 MB，文本层 56,102 字节）`

### (4) §9 第 125→126 行 — 文本导出字节

- 改前：`文本导出：2026-w47-ru-zh-cn.text.md = 2026-w47-ru-core.text.md，54,802 字节，690 行，字节一致`
- 改后：`文本导出：2026-w47-ru-zh-cn.text.md = 2026-w47-ru-core.text.md，54,801 字节，690 行，字节一致`

### (5) §7.3 新增第 105 行 — 实测文件 + SHA（在「印版 vs 网版文本同一性」行之后）

- 改前：无此行。
- 改后：`**实测文件（SHA-256，第二轮复校已验）**：印版 Lucerna-VOL4.pdf 31,429,156 字节，SHA-256 4b56429722dbbf4573eb80bf24a7d4ae8daf6a7217fd01537c26801fc4411868；网版 Lucerna-VOL4-web.pdf 3,992,881 字节，SHA-256 8a2649263171727ecfb2118e3f85bc1ddfc8a0c1f23730e66652ba78e358fca7；文本导出 2026-w47-ru-zh-cn.text.md 54,801 字节、690 行。`

## 4. 改后核对证据

- 旧值 grep：`grep -n "54,802\|3,992,897" WEEKLY-KIT.md` → **0 命中**（exit 1）。
- 新值 grep：`54,801` 在位（61、105、126 行）、`3,992,881` 在位（105、112、123 行）、`31,429,156` 在位（105、122 行）、`4b564297…` / `8a264926…` 完整 SHA 在位（105 行）。
- 旧 SHA 前缀：`grep -c "4e14b1ae\|91106aa4"` → **0**。
- 文件大小：WEEKLY-KIT.md 23,370 → 23,745 字节（+375，= 4 处数值各 −0/等长替换 + 新增 1 行）。
- mtime 核对（改前 → 改后）：仅 WEEKLY-KIT.md 变（2026-11-11 00:00:12 → 01:02:22 UTC）；Lucerna-VOL4.pdf（00:10:37）、Lucerna-VOL4-web.pdf（00:13:37）、2026-w47-ru-zh-cn.text.md（00:04:12）、2026-w47-ru-core.text.md（00:04:13）、ABSTRACT.txt、ru-p8.json 的 mtime 与字节数均未变。
- `git status --porcelain -- production/2026-w47/core-ru/`：仍仅 `?? production/2026-w47/core-ru/`（新目录未跟踪，状态不变）。注：全仓 `git status` 另见 W43 issues 的既有修改（改前已存在，非本次所动，未碰）。

## 5. 结论

KIT-only 3 项全部完成：§5 / §7.4 / §9 旧字节数已订正为实测值，§7.3 已补入印版/网版新 SHA 并与三项实测字节数同行核对一致，§9 无数值可改。无其他文件被改动，无构建/渲染/提交/推送。
