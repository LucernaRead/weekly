# EDIT-LOG — W47 KIT wave-2 zh-cn 家编辑员（W2-24）

- **项号**：W2-24（zh-cn 家唯一 1 项）
- **版**：zh-cn-ru — `~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-ru/WEEKLY-KIT.md`
- **清单来源**：`hidden_files/w47/scratch-kit-wave2-inventory/KIT-WAVE2-INVENTORY.md` § W2-24
- **日期**：2026-11-13（EST，约 06:05）
- **磁盘**：开工 `df -h`：`/dev/mapper/rv` 98G 已用 / 52G 可用（< 100G 停手线，继续）

## 改了什么（仅 KIT 文字，两处）

1. **L259**（`## Post-proof fix` F8 记录）：
   - 改前：`1 HEAD TOO WIDE (422.7px vs 422.5px box — the 0.2px the D5 rebuild had trimmed)`
   - 改后：`1 HEAD TOO WIDE (426.14px vs 422.5px box — 超 3.64px; fix-xru 后拉丁改走 Newsreader Bold，run-log L5159 裁定接受)`
2. **L277**（`## fix-xru` HEAD TOO WIDE 注）：
   - 改前：`(422.7px vs 422.5px box, 0.2px; gates accept exactly 1 for ru)`
   - 改后：`(426.14px vs 422.5px box, 超 3.64px; gates accept exactly 1 for ru)`

## 未动

- **L215 不动**（D5 content-fix 历史实测值 `measured 422.7px`，复核仍在）。
- 未改生产 PDF、`.text.md`、`content*.py` 或任何其他文件；未重建、未重校；未跑 lint/insert.py；未 git commit/push/add/reset/stash。
- 未碰 zh-cn 家之外任何 KIT。

## 复核结果（grep，改后）

- `grep -n "426.14"`：仅命中 **L259** 与 **L277**（各 1 处），与清单一致。
- `grep -n "422.7"`：仅命中 **L215**（D5 历史值），L259/L277 已无 422.7。
- `grep -n "422.72"`：无命中（清单旧值写法已不存在于改后两行）。
- `git status --porcelain`：工作区另有大量他家/他轮未提交改动（与本项无关，本项未动其中任何文件）；本项文件所在目录 `production/2026-w47/2026-w47-zh-cn-ru/` 为 untracked 目录，本项只改了其中 `WEEKLY-KIT.md` 两行。

## 结论

**W2-24 完成。**
