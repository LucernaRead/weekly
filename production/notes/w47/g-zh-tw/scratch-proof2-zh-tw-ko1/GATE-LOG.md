# GATE-LOG — W47 zh-tw-ko proof2（停工：SHA 盤核不符，門禁未跑）

- 版：`production/2026-w47/2026-w47-zh-tw-ko/`（繁體中文 × 韓語讀者版，VOL.4）
- 工作目錄：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-zh-tw-ko1/`
- 時間：2026-11-11 20:50–21:02 UTC
- 解釋器：未啟用（門禁未跑）

## 探針

| 檢查 | 結果 |
|---|---|
| `git -C ~/workspace/weekly-git hash-object -w /dev/null` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0，通過 |
| scratch 真實寫盤 `tmp/probe.txt` | 寫入 + 讀回成功 |
| TMPDIR | 全程 `$SCRATCH/tmp`，系統 /tmp 未用 |

## SHA 盤核（門禁前置，FAIL → 停工）

| 件 | 任務值 | 盤上實測（兩次 sha256sum 一致） | 結果 |
|---|---|---|---|
| 印 PDF | 16,838,018 B / `75610665…307f0` | 16,838,020 B / `c04102a9…17d3a6` | FAIL |
| 網 PDF | 2,325,041 B / `140f83ac…67bb282` | 2,325,041 B / `ed9e11a5…65bad61` | FAIL |
| text.md | 53,922 B / `2e7038cc…986a8` | 53,916 B / `2af17f02…86a8` | FAIL |

任務值 = fix1 前舊版（proof1 baseline build-copy，11:47–11:49 UTC，與任務值逐字節一致）；盤上值 = fix1 後重建新版（本版 WEEKLY-KIT.md :35/:38/:117 自記，與盤上逐字節一致；FIX-LOG.md :234–238 亦同）。

## 門禁匯總

全部未跑（停工規則：SHA 不符即停，不繼續）：

- run.py：未跑
- checks.py：未跑
- freeze baseline / freeze diff：未跑
- occlusion 幾何遮擋：未跑
- 奶油盒掃描 / 頁界 spill / 孤兒：未跑
- p8 extract / compare：未跑
- 印/網文字層比對：未跑
- P8 最小字號 / §1.1：未跑
- 150 題手驗 / 8 頁目視 / 8 金句核對：未跑
- keydiff：未跑

## 收工生產完整性

- 未改生產任何文件，未 commit，未 push，未跑構建腳本。
- 收工重驗生產三 SHA = 開工值（印 `c04102a9…`、網 `ed9e11a5…`、text `2af17f02…`），不變。
- 本 scratch 僅含：`tmp/probe.txt`、`PROOF-NOTE.md`、本文件。

## 待辦（需協調員重發任務書）

- 以新三 SHA（見 PROOF-NOTE §4）重發 proof2 任務後，再從頭全量復校。
