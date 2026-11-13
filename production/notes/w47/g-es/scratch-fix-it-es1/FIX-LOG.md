# FIX-LOG — 2026-W47 it-es fix1（proof1 D1）

**修理工**：fix1（只修 D1，不碰 PDF、不碰核心、不碰 tools/）
**日期**：2026-11-11
**工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-it-es1/`
（FIX-LOG 写 goals 侧，未写进 repo 的 `hidden_files/w47/`）
**对象目录**：`~/workspace/weekly-git/production/2026-w47/2026-w47-it-es/`

## 0. 探针（开工前）

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → rc=0（`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`）
- scratch 写入正常（`probe.txt`）
- 全程 `TMPDIR=<scratch>/tmp`，未写 /tmp

## 1. SHA 核对（开工前，三件与任务给定一致）

| 件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-ES.pdf` | 14,033,685 B | `9c7ee019b041a7484aed75d92c5d9f21f7e899fde8e8fa05813cc3c60b0b8d31` |
| 网页 PDF `La-Lucerna-VOL4-ES-web.pdf` | 1,259,244 B | `d05e956d056c76f8bf3f6ce560073d1c341a7e1ea71ce0fa17f1e19ee3d93408` |
| 文本导出 `2026-w47-it-es.text.md` | 56,259 B | `01791ae188a99e9106aab410799c3ba5f791471ca38d456f04799d4cd27f009a` |

## 2. 修法（只改 D1，4 处标签字符串）

`2026-w47-it-es.text.md` 第 969、971、973、975 行（E 节 Q137–140 题干）：

| 行 | 改前 | 改后 |
|---|---|---|
| 969（Q137） | `[A2 · 翻译]` | `[A2 · Traducir]` |
| 971（Q138） | `[B1 · 翻译]` | `[B1 · Traducir]` |
| 973（Q139） | `[B1 · 翻译]` | `[B1 · Traducir]` |
| 975（Q140） | `[B2 · 翻译]` | `[B2 · Traducir]` |

只改这 4 处标签字符串；键、注释、行尾 `[Traducir al español]` / `[Traducir al italiano]` 及所有其他文字一律不动。未重建 PDF，未改核心，未改 tools/。

## 3. 根因：导出器所致（非手改），传导链共三环

1. **源头——core-it 的 zh-cn 层**：`production/2026-w47/core-it/content8.py` 第 69–76 行，E 节 4 道题的 `f.ex()` 调用 type 与 instr 均为中文「翻译」（如 `f.ex("A2", "翻译", "圣母健康节人们走过还愿桥。", "对照原文", "Per la Madonna della Salute …", instr="翻译", …)`）。
2. **放行——fan-out 翻译表有意不映射该词**：`hidden_files/w47/scratch-fanout-it/translations.py` 头注释第 6–8 行写明：`Type '翻译' is deliberately NOT in this table (W46 precedent: kept as-is; only its instr is re-aimed per item via full-line replacement)`。于是 type 字符串「翻译」未经翻译进入本版 `content8.py` 第 69、71、73、75 行（键/注释已是西语，唯 type 仍是中文）。
3. **导出——导出器逐字照印 type**：`production/2026-w46/core-it/finish/export_it_textmd.py` 第 297 行（`build_edition.py` 第 267–268 行 import 此文件）：`s = f"{self.exn}. [{level} · {typ}] {body or ''}"`——无本地化步骤，`typ` 是什么就印什么。

结论：D1 是导出链路的系统性残留，不是某人手改错字。KIT §8 原称「有意保留（W46 前例）」已被 proof1 否定（it-en 同位置已本地化为 `Translate`，证明当前标准是本地化标签），本次已在 KIT §8 中更正。

**按任务 scope，导出器与翻译表本次均未改**：只改本版 text.md，不改 `export_it_textmd.py`、不改 `translations.py`、不改其他版。

## 4. 已知同源残留（不在本轮 scope，留给各版自己的 proof1/fix1 轮）

据 PROOF-NOTE §D1：同周 it-fr、it-de、it-pt 各残留 4 处「翻译」（同一传导链）。本轮未碰这些版，未顺手扩 scope。

## 5. 验证（修后）

- 全文 grep「翻译」：**0 命中**（无中文正文内容需豁免——文件内其余中文仅全角冒号 ：等冻结核心模式，与「翻译」无关）。
- diff 修前（`scratch-fix-it-es1/2026-w47-it-es.text.md.prefixed`）vs 修后：**仅 4 行不同**（969/971/973/975），其余逐字节相同。
- text.md：56,259 → **56,267 字节**（+8 = 4 ×（"Traducir" 8B − "翻译" 6B），吻合），1317 行不变。
- 新 text.md SHA-256：`ebd13d454e258a29fe414c04fb56ce53214308b84b2befe400a072fd3415cabf`
- 印刷 PDF SHA：`9c7ee019b041a7484aed75d92c5d9f21f7e899fde8e8fa05813cc3c60b0b8d31`（**不变**，mtime 仍为修前 02:59）
- 网页 PDF SHA：`d05e956d056c76f8bf3f6ce560073d1c341a7e1ea71ce0fa17f1e19ee3d93408`（**不变**，mtime 仍为修前 03:01）

## 6. KIT 更新

`WEEKLY-KIT.md` 三处：
- §7 交付物：text.md 新字节数/SHA + fix1 说明 + PDF 未重建声明。
- §8 Gates：更正「有意保留」说法（proof1 已否定；fix1 后 grep「翻译」为 0）。
- §9：新增 fix1 条目（修法、验证数字、根因、it-fr/it-de/it-pt 同源残留、proof2 待派）。

## 7. Commit（本地，未 push）

- commit：`8f2bba56`（main 分支）
- 内容：仅 2 个文件——`production/2026-w47/2026-w47-it-es/2026-w47-it-es.text.md` + `WEEKLY-KIT.md`（因整版目录此前未入仓，显示为 2 文件新增，共 1395 行；不含 PDF/svg/cards/jpg 等生成件）
- 未 push（推循环负责）。
- 附注：工作树中 `issues/2026-w43/…` 有一批 pre-existing 的 M 修改（他人工作），本轮未碰、未提交。

## 8. 待办（不在本轮）

- **proof2**：按 SOP §8，修后须全量重校——另派，本次不做。
- it-fr / it-de / it-pt 各 4 处同源「翻译」残留，各版自己的 proof1/fix1 轮处理。
- 根因的长期修法（导出器本地化 type 或翻译表补映射）未在本轮做；如需修，应走工具/SOP 流程，不属于单版 fix1。
