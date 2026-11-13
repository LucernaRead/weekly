# FIX-LOG — W47 zh-tw-it fix1（D3，機制層修復）

- **Builder**：fix1（葉子，未再派 subagent）
- **範圍**：只修 D3（意大利語系詞 è 誤用 ×5，解釋層文法錯誤）。D1（核心「下週日」11 處）由 core-zh-tw fix1 另修，本版隨核心重建——本輪**未碰 D1**；D2（網頁 abutting 9 處）由 pre-insert 網頁重建帶上——本輪**未碰 D2**。未改核心、未改本版成品 content/PDF、未重建、未跑 insert.py / lint --write、無任何 git 寫操作。
- **復校對象**：`production/2026-w47/2026-w47-zh-tw-it/`，印刷 `Lucerna-VOL4-IT.pdf`（SHA 前 16 位 `ec9d0624d91abb2a`）、網頁 `Lucerna-VOL4-IT-web.pdf`（`34c4ff2c9e3f1fe0`），與 PROOF-NOTE 核對一致，僅核對、未動。
- **先讀**：`hidden_files/w47/scratch-proof-zh-tw-it1/PROOF-NOTE.md` 全文；`hidden_files/w47/scratch-fix-zh-tw-fr1/FIX-LOG.md`（參照其機制層做法：只改 tables.py 對應語的值 + scratch 副本重跑 transform 驗證）。

## 探針（開工與每步寫盤前重探）

- 開工 2026-11-11 ~09:06 UTC：`git -C ~/workspace/weekly-git hash-object -w --stdin` rc=0；筆記目錄 `scratch-fix-zh-tw-it1/PROBE.txt` 真實寫盤 rc=0。
- 編輯 tables.py 前重探 rc=0；scratch 驗證寫盤前重探 rc=0；寫本日誌前重探 rc=0。
- 全程無 EDQUOT；`df`：/home/hatch 150G 總，72G 已用，78G 可用。

## D3 改前 → 改後（只改機制層 tables.py 的 it 值，共 5 處）

**文件**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-zh-tw/tables.py`（2430 行，ENTRIES = 238）。每處只改 `it` 值內的一個子串；英文源鍵（source literal）與 de/fr/es/pt/nl/ru/ja/ko 8 語值**一字未動**。

### (1) P1 Note — tables.py:260（text.md L165）
- **源鍵**：`The same evening, Leofoo Village's Tombstone Town closes: … The daytime parade runs daily at 14:00. …`（英 core "runs daily"）
- **版內定位**：`content12.py:41`（f.gloss），與 tables.py it 值逐字一致。
- **改前**：`La parata diurna è tutti i giorni alle 14:00.`
- **改後**：`La parata diurna si tiene tutti i giorni alle 14:00.`

### (2) P2 Note — tables.py:282（text.md L680）
- **源鍵**：`New Taipei Christmasland opened Nov 13 and runs to Dec 27 — 45 days — … The main light show runs every half hour, 5 minutes each, from 17:30 to 23:00 daily. …`（英 core "runs … daily"）
- **版內定位**：`content12.py:123`（f.gloss），與 tables.py it 值逐字一致。
- **改前**：`Lo spettacolo di luci principale è tutti i giorni dalle 17:30 alle 23:00, ogni mezz'ora, 5 minuti ogni volta.`
- **改後**：`Lo spettacolo di luci principale si tiene tutti i giorni dalle 17:30 alle 23:00, ogni mezz'ora, 5 minuti ogni volta.`

### (3) P7 B2 釋義 — tables.py:2166（text.md L4569）
- **源鍵**：`小雪 is the 20th solar term, after 立冬. … 燈秀 is a light show: the main show runs every half hour. …`
- **版內定位**：`content7.py:60`（c.para），與 tables.py it 值逐字一致。
- **改前**：`lo spettacolo principale è ogni mezz'ora.`
- **改後**：`lo spettacolo principale si ripete ogni mezz'ora.`

### (4) P7 易錯診所 — tables.py:1945（text.md L4731）
- **源鍵**：`The main light show runs every half hour: 12 shows from 17:30 to 23:00.`
- **版內定位**：`content7.py:77`（診所 gloss），與 tables.py it 值逐字一致。
- **改前**：`Lo spettacolo principale è ogni mezz'ora: 12 volte, dalle 17:30 alle 23:00.`
- **改後**：`Lo spettacolo principale si ripete ogni mezz'ora: 12 volte, dalle 17:30 alle 23:00.`

### (5) P8 答案鍵 70 — tables.py:1483（text.md L5876）
- **源鍵**：`The Christmas concert plays 4 shows in all.`
- **版內定位**：`content56.py:44`（f.ex B1 單選 B），與 tables.py it 值逐字一致。注意：鍵 70 在 P8 練習文件中（content56.py），不在 content8.py。
- **改前**：`Il concerto di Natale è in tutto 4 spettacoli.`
- **改後**：`Il concerto di Natale prevede 4 spettacoli in tutto.`

## 核對依據（逐字核實 + 內部一致性）

1. **逐字核實**：動手前逐處核對 text.md 行號與原文（L165 / L680 / L4569 / L4731 / L5876 均與 PROOF-NOTE 一致）及版內 content 文件行號（content12.py:41、:123；content7.py:60、:77；content56.py:44），五處 tables.py it 值與版內字符串逐字對應。
2. **內部證據**：同版同一概念已有正確寫法 `si ripete ogni mezz'ora`，見 `content7.py:63`（B2）、`content8.py:64`（B1）、`content12.py:148`（A2）三處「主燈秀」完成句子（即 PROOF-NOTE 所稱鍵 22/110/135）；(3)(4) 新句沿用同一措辭，(1)(2) 用 `si tiene`（與法語 "a lieu" / 葡語 "acontece" 的存在義對應，時刻/頻率作狀語而非補語），(5) 用 `prevede`（主語單數＋數量補語兼數不一致問題一併消除）。
3. **不動項**：其餘 "è + 時間點"（如 `è alle 14:00`、`è il 22 nov.`）皆正確，不在內；P1/P4 Note 的 `domenica prossima, 22 nov.`（PROOF-NOTE 已裁定正確）不動。
4. **鍵未動**：五處英文源鍵均未改（fr fix1 前例同樣鍵不動）；`grep` 驗證舊串全表歸零、新串各出現 1 次（"spettacolo principale si ripete ogni" 兩處：(3)(4) 各一）。

## Scratch 驗證（未動成品，見 GATE-LOG）

- 在筆記目錄 `work/` 內複製 core-zh-tw + 改後 tables.py + transform.py（transform.py 僅把 PROD 指針改向 scratch `work/prod`，其餘原樣），9 語全部重跑 transform：**9/9 TRANSFORM OK**（各 244 行日誌，ENTRIES = 238，tables.py 可正常 import）。
- 五處新值全部流入 scratch-it 對應 content 文件（content12.py:41、:123；content7.py:60、:77；content56.py:44），舊串在 scratch-it 全版歸零。
- scratch-it vs 已發版 diff：22 個 hunks，全部可分類——**11 D1**（盤上 core-zh-tw 已帶 core fix1 的「本週日」，平行修復帶入，本輪未碰）＋ **5 D3**（本輪）＋ **6 P8 缺口**（見下），無其他差異。
- 其餘 8 語 scratch vs 已發版：除 D1 與已知缺口外**零差異**（見 GATE-LOG），即本輪改動未波及其他語。

## 已知前存缺口（非本輪造成，僅記錄）

- **6 條 P8 答案注記 tables.py 缺源串**：scratch 9 語的 content56.py:178/191/195 與 content8.py:26/62/70 均殘留英文（`The ceremony is at the Taipei Music Center.` / `Xiaoxue is Nov 22.` / `Four big events fall on the same Sunday.` / `Collecting points is 集點.`）。FANOUT-REPORT（第 7 棒）與 it.md:11 已記錄：fan-out 時「首輪構建前已在 content56.py/content8.py 預補譯」，9 版同一缺口；原始 transform-it.log（02:42）亦無此 6 條替換。故 scratch diff 中這 6 行屬**前存已知缺口**，不是本輪回歸；tables.py 仍缺這 5–6 條源串（de.md 稱缺 5 條），留待後續補表輪次處理，本輪不擴範圍。

## 版面影響評估（供隨後重建輪次複核）

- (1) `è`→`si tiene`：+4 字符；(2) 同 +4 字符；(3) `è`→`si ripete`：+8 字符；(4) 同 +8 字符；(5) `è in tutto 4 spettacoli`→`prevede 4 spettacoli in tutto`：+2 字符。均在 P1/P2 Note gloss（欄寬足）與 P7 B2/診所、P8 鍵注內。
- PROOF-NOTE 提醒：P7 欄 3 底距 footer 僅 18.7px 餘量——(3)(4) 各長 8 字符，B2 釋義與診所 gloss 所在欄需在重建輪重跑 occlusion + freeze 終驗；本輪未重建，不作版面結論。

## 未做

- 未碰 D1（未改核心中文、下週日 11 處原樣留待核心 fix1）、未碰 D2（未動 webpdf.py、未重建網頁 PDF）。
- 未改本版成品 content/PDF/SVG、未重建、未跑 insert.py、未跑 lint --write；無任何 git 寫操作（僅探針 `git hash-object -w`）。
- 只改 `tables.py` 5 處 it 子串與本筆記目錄；未碰其他文件。
