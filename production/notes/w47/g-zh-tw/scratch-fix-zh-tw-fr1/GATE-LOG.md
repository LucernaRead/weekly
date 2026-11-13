# GATE-LOG — W47 zh-tw-fr fix1（D2 機制層修復驗證）

## 1. 開工探針

| 檢查 | 結果 |
|---|---|
| `git hash-object -w`（2026-11-11 08:43 UTC） | rc=0 |
| 筆記目錄真實寫盤 `scratch-fix-zh-tw-fr1/work/probe.txt` | rc=0 |
| EDQUOT | 全程 0 次；`df` /home/hatch 45G 可用 |
| SOP §8 / §1.1、AGENTS.md、brief-coordinator.md、PROOF-NOTE.md | 已讀（brief 實際在 goals hidden_files/w47/briefs/，任務書的 weekly-git 路徑不存在） |

## 2. 改前核實（盤上）

- `content7.py:52` 舊句與 PROOF-NOTE D2 逐字一致；`tables.py:2131` fr 值與之逐字一致。
- `grep "le lieu où elle a lieu" tables.py`：全表僅 2131 行 1 處。
- 中文層：`core-zh-tw/content34.py:18`「下午5點先走星光大道，頒獎典禮晚上6點30分開始」。
- 同頁詞卡：`content7.py:43`「星光大道 est le tapis rouge avant la cérémonie」。
- 時間：`content7.py:46`「La cérémonie commence à 18:30 le 22 nov.」；`core-zh-tw/content56.py:148` `(17.0, "星光大道")` / `(18.5, "頒獎典禮")`。

## 3. 改動（唯一）

- `hidden_files/w47/scratch-fanout-zh-tw/tables.py:2131` fr 值：
  - 舊：`Astuce mémoire : apprenez d'abord 入圍, puis la cérémonie （頒獎）, puis le lieu où elle a lieu （星光大道）.`
  - 新：`Astuce mémoire : apprenez d'abord 入圍, puis 星光大道 (le tapis rouge à 17:00, avant la cérémonie), puis la cérémonie （頒獎） à 18:30.`
- 其餘 8 語值（de/es/it/pt/nl/ru/ja/ko）與各自已發版 `content7.py` 逐字比對一致，未動。英文源串未動。

## 4. Scratch transform 驗證

| 檢查 | 結果 |
|---|---|
| `tables.py` import（tools/venv/bin/python） | OK，ENTRIES = 238 |
| transform fr（scratch `work/`，PROD 指針改向 scratch） | `TRANSFORM OK fr`，244 行日誌（`work/transform-fr.log`）；新值在 `prod/2026-w47-zh-tw-fr/content7.py:52`，全版 1 次 |
| transform es（對照，同一改後 tables.py） | `TRANSFORM OK es`（`work/transform-es.log`）；`Truco de memoria...` 行與已發 es 版逐字一致 |
| diff：scratch fr content7.py vs 已發 fr 版 content7.py | 僅 2 行差異（`work/diff-fr-content7.txt`）：52 行 = 本輪 D2 修復；99 行 = 來信句「本週日」（scratch core 拷貝）vs「下週日」（已發版）——盤上 core-zh-tw 已帶平行 core fix1 的 D1 改動，本輪未碰 D1/核心 |

## 5. 未跑（按任務）

- 未重建本版成品（無 render/webpdf）；未跑 insert.py、lint --write；無 git 寫操作。
- 版面終驗（B1 欄多約一行、終點約 1568→~1600，仍低於金句區起點 1712）留待核心重建輪的 occlusion audit + 全量復校（SOP §8.4）覆蓋。

## 6. 清理

- 驗證用 97 MB scratch 副本（`work/prod/` core 拷貝 + fr/es transform 產出、`work/__pycache__`、冗餘 tables.py/transform.py 拷貝）已刪除；僅留 `work/transform-fr.log`、`work/transform-es.log`、`work/diff-fr-content7.txt`。
