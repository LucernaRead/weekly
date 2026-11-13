# PROOF-NOTE — W47 zh-tw-ko proof2（停工：SHA 盤核不符，未開工復校）

**首行結論：停工——盤上三 SHA 與任務值全部不符，按任務書硬規則停止，不繼續復校。任務書三 SHA 是 fix1 前舊版（proof1 已判 (b) 的版），盤上文件是 fix1 後重擴散新版。**

- 版：`production/2026-w47/2026-w47-zh-tw-ko/`（繁體中文 × 韓語讀者版，VOL.4）
- 復校員：獨立復校 proof2；工作目錄 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-zh-tw-ko1/`
- 時間：2026-11-11 20:50–21:02 UTC（任務發出 15:48 EST = 20:48 UTC 後即刻開工探針）
- 探針：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0；scratch 內真實寫盤 `tmp/probe.txt` 成功。TMPDIR 全程指向本 scratch 下 `tmp/`，系統 /tmp 未用。

## 1. SHA 盤核（兩次獨立 sha256sum，結果一致）

| 件 | 任務值（字節 / SHA-256） | 盤上實測（字節 / SHA-256） | 結果 |
|---|---|---|---|
| 印 PDF `Lucerna-VOL4-KO.pdf` | 16,838,018 / `75610665146d9903c5144148f799386d2ed928f11264e2a8697cb24429c307f0` | 16,838,020 / `c04102a9a1ceef1cf25fc7f3df6e69266e5f3d8bb2fec8d4370a3f782217d3a6` | **不符**（+2 B） |
| 網 PDF `Lucerna-VOL4-KO-web.pdf` | 2,325,041 / `140f83acdba99fba9b67ec26f8e1418d85a2e5aa9f791d3f16238265c67bb282` | 2,325,041 / `ed9e11a5c8997eb6b09cd6fd1f9bad6b64d686e2280d4730eac3d48ff65bad61` | **不符**（同字節，不同 SHA） |
| text.md `2026-w47-zh-tw-ko.text.md` | 53,922 / `2e7038cc4c1266146824db80b1a20f87f83593b69f3e8bd755596b435e6986a8` | 53,916 / `2af17f023ab203259aeeb294b04f31e4bbb766398a28ec5f7fd2f163622b06f7` | **不符**（−6 B） |

盤上文件 mtime：印 2026-11-11 12:52:42 UTC，網 12:56:33 UTC，text.md 12:56:35 UTC。版目錄 git 狀態 `??`（未提交、未入倉）。

## 2. 不符原因（已證實，非猜測）

任務書三 SHA 是 **fix1 前舊版**，proof1 的 baseline build-copy（`scratch-proof-zh-tw-ko1/baseline/build-copy/`，mtime 11:47–11:49 UTC）逐字節對上任務值三項：

- 印 16,838,018 B / `75610665…`、網 2,325,041 B / `140f83ac…`、text.md 53,922 B / `2e7038cc…`——與任務值完全一致。

盤上文件是 **fix1 後重擴散新版**（K1 韓語助詞／繫詞修正後 `transform.py ko` 從未動核心重建），證據：

- 本版自帶 `WEEKLY-KIT.md` :35、:38、:117 明文記載新三件即盤上值（印 16,838,020 B / `c04102a9…`、網 2,325,041 B / `ed9e11a5…`、text.md 53,916 B / `2af17f02…`），並在 :36、:39 把任務值列為「History（fix1 前，proof1 (b) 版，K1 未修）」舊值。
- `scratch-fix-zh-tw-ko1/FIX-LOG.md` :234–238 同樣記載新舊兩套三件，與盤上 / 任務值逐一對應；並說明 −6 B 來自 K1-5「入圍이에요」→「入圍예요」×2 處各 −3 B，其餘 K1 為同長度替換（與印 +2 B、網同字節異 SHA 的變化方向一致）。
- 時間線一致：proof1 12:25–13:05 UTC 判 (b)（新缺陷 K1）→ fix1 改表重建 → 新版 12:52–12:56 UTC 落盤，晚於 proof1 舊版備份 11:47–11:49 UTC。

即：任務書誤把 proof1 舊版三 SHA 當作待復校新版的三 SHA。待復校的對象（fix1 新版）本身未被證明有問題，但按任務書「按 SHA 認文件」「有任何出入即停」的硬規則，本員無權自行改認另一套 SHA 繼續。

## 3. 本員未做的事（按停工規則）

- 未通讀、未手驗 150 題、未目視 8 頁、未跑任何門禁（run.py / freeze / occlusion / keycheck 等一概未跑）。
- 未跑任何構建腳本，未讀 content*.py:6 OUT、未碰生產任何文件；未 commit、未 push、未重渲染。
- 未寫入生產目錄任何東西；僅在自有 scratch 寫入探針文件與本 NOTE + GATE-LOG。收工重驗：生產三 SHA 與開工時同一組（c04102a9… / ed9e11a5… / 2af17f02…），未變。

## 4. 需協調員裁決（本員不自行決定）

- 如需復校 fix1 新版，請重發任務書，三 SHA 改為盤上實測值：印 `c04102a9a1ceef1cf25fc7f3df6e69266e5f3d8bb2fec8d4370a3f782217d3a6`（16,838,020 B）、網 `ed9e11a5c8997eb6b09cd6fd1f9bad6b64d686e2280d4730eac3d48ff65bad61`（2,325,041 B）、text.md `2af17f023ab203259aeeb294b04f31e4bbb766398a28ec5f7fd2f163622b06f7`（53,916 B）。
- 屆時本員（或重派的 proof2 員）再從頭全量復校；本次停工不等於對新版的任何結論（(a)/(b) 均未作出）。
