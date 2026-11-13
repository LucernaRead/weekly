# EDIT-LOG — W47 KIT wave-2 zh-tw 家编辑

- **编辑员**：W47 KIT wave-2 zh-tw 家编辑员（恢复协调员 #6 派单，步骤 3）
- **日期**：2026-11-13 EST ~06:04–06:15
- **清单**：`hidden_files/w47/scratch-kit-wave2-inventory/KIT-WAVE2-INVENTORY.md`（W2-23、W2-25）
- **磁盘**：开工 `df -h` 已用 98G / 可用 52G（< 100G 停手线，继续）
- **范围**：只改以下两处 KIT 文字；未改生产 PDF、.text.md、content*.py 或任何其他文件；未重建、未重校；未 commit/push/add/reset/stash；未跑 lint/insert.py；未碰他家 KIT。
- **附注**：`~/workspace/weekly-git` 的 `git status` 显示两 KIT 文件为 untracked（`??`，从未入仓），故 `git diff` 无输出——改动以磁盘文件 grep 为准（见下复核）。仓内其余已改文件（covers 等）为开工前已有的他人改动，与本次无关，未动。

## W2-23 — core-zh-tw KIT Measured totals 补 text SHA ✅ 完成

- **文件**：`~/workspace/weekly-git/production/2026-w47/core-zh-tw/WEEKLY-KIT.md`
- **重测 SHA**（改前，磁盘实测）：
  - `2026-w47-zh-tw-en.text.md`：49,804 B，SHA-256 `9b8b5295ddd822afc020a8c439a55e35cb5259b5d18afa25f4e4d4cacd376905`
  - **与清单一致**（清单所列 49,804 B / 同 SHA），按清单值写入。
- **改了什么**：Measured totals L53（PDFs 行）之后新加一行（现 L54）：
  `- **Text export:** \`2026-w47-zh-tw-en.text.md\` 49,804 bytes, SHA-256 9b8b5295ddd822afc020a8c439a55e35cb5259b5d18afa25f4e4d4cacd376905.`
- **复核**：
  - grep `9b8b5295…` 全文命中 2 处：新行 L54（Measured totals）+ 原 L129（现 L130，Proofread record 的 Text export 行，内容逐字未动，仅行号 +1）。
  - L53 PDFs 行未动。

## W2-25 — zh-tw-ru KIT L35 笔误 ✅ 完成

- **文件**：`~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-ru/WEEKLY-KIT.md`
- **磁盘核对**（文字项，不写入新 SHA；供核对的现值）：
  - 印 `Lucerna-VOL4-RU.pdf`：11,291,943 B，SHA-256 `8c3aca16ea41ed1cd8f5eb6174861c30ce4db1536cbf14427a8bd08aa901e2f5`——与 KIT L35 行首一致。
  - 网 `Lucerna-VOL4-RU-web.pdf`：1,997,666 B，SHA-256 `04606730a740e008fe427e69859c1e90a911f2872ec6079b8df75a135421afa1`——与 KIT L35 行首一致。
- **改了什么**（只改 L35 Note 句两处）：
  1. `the print PDF is smaller than the other editions' (~20 MB)` → `(~11.2 MB)`。
  2. `Web PDF 2,070,745 bytes (Cyrillic UTF-8 is 2 bytes per letter` → `Web PDF 1,997,666 bytes (Cyrillic UTF-8 is 2 bytes per letter`。
- **复核**：
  - L35 行首印/网 SHA 与字节数未动；行内 D5 括号历史值未动（仍为 print 11,366,251 B / web 2,070,745 B，grep 确认）。
  - `Web PDF 2,070,745` 全文 0 命中（Note 句已改，D5 括号内写法为 `web 2,070,745 B`，不在此列）。
  - `~20 MB` 全文仅剩 L100 一处（`Print PDF 12.9 MB vs ~20 MB for the other editions`），属 L35 之外的行，按清单未动。
  - L129 fix-xru 节 New SHAs 行（印/网现值）未动。

## 汇总

| 项号 | 状态 | 重测 SHA 与清单是否一致 |
|---|---|---|
| W2-23 | ✅ 完成 | 一致（49,804 B / `9b8b5295…`） |
| W2-25 | ✅ 完成 | 文字项；磁盘印/网现值与 KIT L35 行首一致，无 SHA 写入 |
