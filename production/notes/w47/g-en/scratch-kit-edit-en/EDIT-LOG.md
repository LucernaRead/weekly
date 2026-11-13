# EDIT-LOG — W47 KIT wave-2 en 家编辑员（W2-26）

- **项号**：W2-26（en 家唯一 1 项）
- **版**：en-ru（`~/workspace/weekly-git/production/2026-w47/2026-w47-en-ru/WEEKLY-KIT.md`）
- **清单**：`hidden_files/w47/scratch-kit-wave2-inventory/KIT-WAVE2-INVENTORY.md` §W2-26
- **日期**：2026-11-13（EST）
- **磁盘**：开工 `df -h`：`/dev/mapper/rv` 98G 已用 / 52G 可用（< 100G 停手线），继续执行。

## 改了什么

只改 en-ru `WEEKLY-KIT.md` 一处文字，未动生产 PDF、`.text.md`、`content*.py` 或任何其他文件；未重建、未重校、未 commit/push/add/reset/stash、未跑 lint/insert.py。

在 boxtitle fix2 节 L52 段后新增 1 行（现为 L53），接受记录全文：

> - **HEADS-NOTE acceptance record A1/A2 (2026-11-12裁定, `hidden_files/w47/scratch-fix-xru-heads/HEADS-NOTE.md`):** the two HEAD TOO WIDE heads named above are accepted items, not to be fixed, and were not rebuilt. A1 — P7 `AN EXAMPLE LETTER`, +5.2u (200dpi pixel measurement; 200dpi 像素实测); crop clean, no collision, does not cross the column （裁图干净、无碰撞、不越栏）. A2 — P8 `Понимание текста`, +0.4u; negligible, sub-pixel （亚像素可忽略）. The HEAD TOO WIDE warning for these two may still appear in build logs / head_check — it is an accepted item, not an unfixed defect.

要点与清单一致：A1 P7 `AN EXAMPLE LETTER` +5.2u（200dpi 像素实测，裁图干净、无碰撞、不越栏）；A2 P8 `Понимание текста` +0.4u（亚像素可忽略）；出处 HEADS-NOTE.md 2026-11-12 裁定（裁定工人 e1d9dc97，协调员 #4 复核）。A2 页码 P8 取自 KIT L52 原文（HEADS-NOTE 表中记为 P?，KIT 与清单均作 P8）。

## 复核结果

- 改前 SHA-256：`fa5747a3d720ee40a14f27a816d756195a620fff526d6d67ad072e76c061dc67`；改后 SHA-256：`0b5a98921ef6a90ff99714d1c2165ed5486f405bdbb1b4d280da50c275b1eddf`（文字项，无 SHA 重测——KIT 不含该版 SHA 变动）。
- `diff` 改前备份 vs 改后文件：仅 `52a53` 新增 1 行，其余 278 行逐字节相同。
- 行数：278 → 279。
- grep 复核：`HEADS-NOTE acceptance record A1/A2` 命中 L53（boxtitle fix2 节内，紧随 L52 段、位于下一 bullet `fix1 re-gate` 之前）；`+5.2u` / `+0.4u` 均命中 L53；`AN EXAMPLE LETTER` 全文共 4 处（新增 1 处）。
- 其余内容未动：§2 SHA、fix-xru/D5/F1 各节、L52 原文均未改。

## 状态

W2-26 完成。
