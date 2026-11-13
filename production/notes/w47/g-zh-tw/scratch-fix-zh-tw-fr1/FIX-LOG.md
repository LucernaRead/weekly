# FIX-LOG — W47 zh-tw-fr fix1（D2，機制層修復）

- **Builder**：fix1（葉子，未再派 subagent）
- **範圍**：只修 D2（低，法語層）。D1（「下週日」11 處）由 core-zh-tw fix1 另修，本版隨核心重建——本輪**未碰 D1、未改核心中文、未重建本版成品**。
- **復校對象**：`production/2026-w47/2026-w47-zh-tw-fr/`，印刷 `Lucerna-VOL4-FR.pdf` 20,191,919 B SHA `beeebce2531fcadd…`，網頁 `Lucerna-VOL4-FR-web.pdf` 2,350,191 B SHA `61537f8dde6b5c04…`（與任務書一致，僅核對、未動）。
- **先讀**：`~/workspace/weekly-git/SOP.md` §8、§1.1 全文，`~/workspace/weekly-git/AGENTS.md`，`hidden_files/w47/briefs/brief-coordinator.md`（實際路徑在 goals hidden_files 下，任務書所寫 weekly-git 路徑不存在，已按實查路徑讀），`scratch-proof-zh-tw-fr1/PROOF-NOTE.md` 全文。

## 探針（開工）

- 2026-11-11 08:43 UTC：`git hash-object -w` rc=0；筆記目錄 `scratch-fix-zh-tw-fr1/work/probe.txt` 真實寫盤 rc=0。
- 全程無 EDQUOT；`df`：/home/hatch 45G 可用。無需刪檔重試。

## D2 改前 → 改後（只改機制層一處）

**文件**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-zh-tw/tables.py:2131`（`Memory trick` 條目的 `fr` 值），全表僅此一行改動。

- **改前**（舊法語全文）：
  `Astuce mémoire : apprenez d'abord 入圍, puis la cérémonie （頒獎）, puis le lieu où elle a lieu （星光大道）.`
- **改後**（新法語全文）：
  `Astuce mémoire : apprenez d'abord 入圍, puis 星光大道 (le tapis rouge à 17:00, avant la cérémonie), puis la cérémonie （頒獎） à 18:30.`

**改寫要點**：順序改為 入圍 → 星光大道 → 頒獎典禮；星光大道定性為「紅毯儀式」（le tapis rouge, avant la cérémonie），刪去錯誤的「le lieu où elle a lieu」（地點）說法；寫明紅毯 17:00、典禮 18:30。英文源串（`Memory trick: ...`）未動；de/es/it/pt/nl/ru/ja/ko 8 語值未動（見 GATE-LOG）。

## 核對依據（中文層 / 同頁詞卡 / 時間，全部盤上實查）

1. **中文層**：核心 `production/2026-w47/core-zh-tw/content34.py:18`：「下午5點先走星光大道，頒獎典禮晚上6點30分開始」——紅毯在先、典禮在後。
2. **同頁詞卡**：本版 `content7.py:43`：「星光大道 est le tapis rouge avant la cérémonie」——詞卡寫法正確，新句沿用同一表述（le tapis rouge avant la cérémonie）。
3. **時間**：本版 P7 `content7.py:46` 單選題：「La cérémonie commence à 18:30 le 22 nov.」；核心 P6 時間軸 `content56.py:148/154`：`(17.0, "星光大道")`、`(18.5, "頒獎典禮")`，即 17:00 / 18:30。另 PROOF-NOTE 獨立網搜核實：星光大道 17:00、典禮 18:30 屬實。
4. **位置核實**：舊句確在 `content7.py:52`（全版唯一一處 `Astuce mémoire`）；`tables.py` 內 `le lieu où elle a lieu` 全表僅 2131 行一處。

## Scratch 驗證（未動成品）

- 在筆記目錄 `work/` 內複製 core-zh-tw + 改後 tables.py + transform.py（transform.py 僅把 PROD 指針改向 scratch `work/prod`，其餘原樣），重跑 transform：
  - **fr**：`TRANSFORM OK fr`（244 行日誌），新值流入 `prod/2026-w47-zh-tw-fr/content7.py:52`，全版僅出現 1 次。
  - **對照 es**：`TRANSFORM OK es`，其 `Truco de memoria...` 行與已發 es 版逐字一致，未受影響。
- `diff`（scratch fr content7.py vs 已發 fr 版 content7.py）：僅 2 行差異——52 行（本輪 D2 修復）與 99 行（來信句「本週日」vs 已發版「下週日」：盤上 core-zh-tw 已帶 core fix1 的 D1 改動，本輪未碰，是平行修復帶入的差異，見 GATE-LOG）。
- `tables.py` 可正常 import（ENTRIES = 238）；de/es/it/pt/nl/ru/ja/ko 8 語值與各自已發版 content7.py 逐字一致。
- 驗證用的 97 MB scratch 副本（core 拷貝 + 兩版 transform 產出）已清，僅留日誌與 diff 檔（`work/transform-fr.log`、`work/transform-es.log`、`work/diff-fr-content7.txt`）。

## 版面影響評估（供隨後重建輪次複核）

- 新句比舊句長約 16 字符（112 → 128），在 B1 欄（`Flow(p, [(COLX[1], CW)], 200, 1560)`，size 22）至多多折一行（約 30 px）。
- 已發版 B1 flow 終點 y=1568（框底 1560，已超 8 px 但 build 0 溢出警告）；下方金句區起點 fy = max(1712, col3_end+24)， headroom 約 110 px 以上，無碰撞物。本輪未重建、不跑渲染，版面終驗由核心重建輪的 occlusion audit + 全量復校（SOP §8.4）覆蓋。

## 未做

- 未碰 D1、未改核心中文、未改 `content7.py` 成品、未重建本版 PDF/SVG/PNG。
- 未跑 insert.py、lint --write；無任何 git 寫操作（僅開工探針 `git hash-object -w` 一次）。
- 只改 `tables.py:2131` 與本筆記目錄；未碰其他文件。
