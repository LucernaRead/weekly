# GATE-LOG — W47 zh-tw-it fix1（D3 機制層驗證）

- **時間**：2026-11-11 ~09:06–09:11 UTC
- **探針**：開工、編輯前、驗證寫盤前、寫日誌前各重探一次，`git hash-object -w` 均 rc=0；全程無 EDQUOT；df：/home/hatch 78G 可用。
- **改動文件**：僅 `scratch-fanout-zh-tw/tables.py`（5 處 it 子串，行號 260 / 282 / 1483 / 1945 / 2166）。

## 1. tables.py 本體驗證

- `python3 -c "import tables"`：成功，`ENTRIES = 238`，`LANGS = ['de','fr','es','it','pt','nl','ru','ja','ko']`。
- 舊串全表歸零：`parata diurna è tutti` / `spettacolo di luci principale è tutti` / `spettacolo principale è ogni` / `concerto di Natale è in tutto` 計 0 行。
- 新串各 1 處：`parata diurna si tiene tutti`（:260）、`spettacolo di luci principale si tiene tutti`（:282）、`spettacolo principale si ripete ogni`（:1945、:2166 各一，共 2 處）、`concerto di Natale prevede 4`（:1483）。
- 源鍵與其餘 8 語值未動：5 次編輯均為 muse.edit 單子串替換，僅命中 it 值內目標子串；無其他行改動。

## 2. Scratch transform（9 語全跑）

- 方法（沿用 fr fix1）：筆記目錄 `work/` 內複製 core-zh-tw（33M，盤上已帶 core fix1 D1「本週日」）＋ 改後 tables.py ＋ transform.py（僅 PROD 指針改向 scratch `work/prod`），逐語重跑。
- 結果：**9/9 TRANSFORM OK**，各 244 行日誌：`transform-it.log` / `transform-es.log` / `transform-fr.log` / `transform-de.log` / `transform-pt.log` / `transform-nl.log` / `transform-ru.log` / `transform-ja.log` / `transform-ko.log`（均留存本目錄）。
- 驗證用副本（core 拷貝 33M ＋ 9 版產出約 300M）已刪，僅留日誌與 diff 檔（`diff-it.txt`、`diff-other6.txt`）。

## 3. it：五處新值流入驗證

scratch-it（`work/prod/2026-w47-zh-tw-it/`，已刪，見日誌與 diff）：
- `content12.py:41` — `La parata diurna si tiene tutti i giorni alle 14:00.` ✓
- `content12.py:123` — `Lo spettacolo di luci principale si tiene tutti i giorni dalle 17:30 alle 23:00, ogni mezz'ora, 5 minuti ogni volta.` ✓
- `content7.py:60` — `lo spettacolo principale si ripete ogni mezz'ora.` ✓
- `content7.py:77` — `Lo spettacolo principale si ripete ogni mezz'ora: 12 volte, dalle 17:30 alle 23:00.` ✓
- `content56.py:44` — `Il concerto di Natale prevede 4 spettacoli in tutto.` ✓
- 舊串在 scratch-it 全部 content 文件中 0 命中。

## 4. it diff 分類（scratch-it vs 已發版，`diff-it.txt`）

content12.py / content34.py / content56.py / content7.py / content8.py 共 **22 hunks，44 行**，全部分類，無剩餘：
- **D1 ×11**（平行修復帶入，本輪未碰）：content12.py:33、:35、:68、:111；content34.py:17、:18、:123、:125、:196；content7.py:99；content8.py:86 —— 均為「下週日」→「本週日」，因盤上 core-zh-tw 已帶 core fix1。
- **D3 ×5**（本輪）：content12.py:41、:123；content7.py:60、:77；content56.py:44。
- **P8 前存缺口 ×6**（本輪未碰，見 FIX-LOG）：content56.py:178、:191、:195；content8.py:26、:62、:70 —— scratch 殘留英文，已發版為 fan-out 時手工預補譯的意大利語；原始 transform-it.log 亦無此 6 條替換。
- bslib4.py / render.py / ABSTRACT.txt：diff 為空。

## 5. 其餘 8 語：零波及驗證

每語 scratch vs 已發版 diff（`diff-other6.txt` 含 de/pt/nl/ru/ja/ko；es/fr 在驗證過程中同法比對）：
- **es / fr**：除 D1 行外，僅 6 條 P8 缺口行（同缺口，目標語側為西/法語預補譯）；fr 另有 1 行 fr fix1 的 Astuce mémoire（tables.py 已帶 fr fix1，已發版仍為舊句——平行修復帶入）。
- **de / pt / nl / ru / ja / ko**：208 行 diff 全為 D1 行＋ 6 條 P8 缺口行（目標語側），另僅 de 有 2 行 P7 預告條 118→104px（`p.rect` / `print("P7 teaser ends"...)`，FANOUT-REPORT de 節已記錄的手工修復，fan-out 時為解 P7 欄 3 壓頁腳所改，非本輪造成）。
- **結論：8 語值與已發版逐字一致**——除上述三類前存/平行差異外無任何其他 diff；本輪 5 處 it 改動未波及其他語。

## 6. 未做

- 未改核心、未改本版成品、未重建、未跑 insert.py / lint --write、無 git 寫操作（僅探針 `git hash-object -w`）。
- D1、D2 一概未碰。P7 欄高與 occlusion 終驗留待重建輪次（見 FIX-LOG 版面影響評估）。
