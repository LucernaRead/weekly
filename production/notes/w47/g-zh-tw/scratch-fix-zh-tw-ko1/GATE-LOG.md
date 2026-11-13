# GATE-LOG — W47 zh-tw-ko fix1（M1–M5 + D1-韓語，機制層驗證）

- **時間**：2026-11-11 ~09:31–09:37 UTC
- **探針**：開工重探 `git hash-object -w` rc=0；全程無 EDQUOT；df：/home/hatch 77G 可用。/tmp 未用。
- **改動文件**：僅 `scratch-fanout-zh-tw/tables.py`（11 處替換：D1-ko ×3、M1 源串+ko、M2 源串+ko、
  M3 ×1、M4 ko ×4、M5 ×1）。行號見 FIX-LOG。

## 1. tables.py 本體驗證

- `python3 -c "import tables"`：成功，`ENTRIES = 242`，`LANGS = ['de','fr','es','it','pt','nl','ru','ja','ko']`
  （it fix1 時 238 條；+4 為他輪補的 M4 條目）。
- 舊串全表歸零：`다음 주 일요일` 0、`finish line` 0、`결승선` 0、`밤의` 0、
  `the place it happens` 0、`열리는 장소` 0、`개방형 과제 - ` 0、`참고: 11월` 0、
  `센터입니다` 0、`22일입니다` 0、`열립니다` 0、`集點입니다` 0。
- 新串：`이번 주 일요일` 3 處（:254/:276/:331）、`end point` 1 處（:2107）、
  `끝나는 곳` 2 處（:2116 新值 + :2138 既有自釋）、`夜間(밤)` 1 處（:2116）、
  `red carpet at 17:00, before` 1 處（:2173）、`17:00 레드카펫` 1 處（:2182）、
  `개방형 과제 — ` 1 處（:2436）、`센터예요` 1 處（:1664）、`集點이에요` 1 處（:1697）、
  `참고｜ 11월` 1 處（:666）。
- 源串與其餘 8 語值未動：11 次編輯均為精確子串替換（每處替換前斷言命中數），
  M1/M2 除源串與 ko 值外，他語值一字未動；M3/M4/M5/D1 只動 ko 值內目標子串。

## 2. Scratch transform（9 語全跑）——含核心對齊依賴實證

- 方法（沿用 it fix1）：筆記目錄 `work/` 內複製 core-zh-tw（33M，盤上已帶 core fix1「本週日」與 fix2 刪 BABYMONSTER 行）
  ＋ 改後 tables.py ＋ transform.py（僅 PROD 指針改向 scratch `work/prod`）。
- **第一跑（未補 scratch 核心）即實證依賴**：ko transform 拋
  `AssertionError: 'Parades give you four useful words: 遊行 (parade), 封王 (clinching the title), 夜間 (night-time) and 終點 (end point). Learn them once, and every parade makes sense.': found 0 < 1`
  ——新源串在盤上核心中無匹配，transform 按設計 loud fail。殘留的半成品版目錄已刪。
- **補 scratch 核心副本兩處源串後**（content7.py:18 `(finish line)`→`(end point)`、
  :52 記憶法改寫；**僅 scratch 副本，真實 core-zh-tw 未碰**），9 語重跑：
  **9/9 TRANSFORM OK**，各 248 行日誌：`transform-de.log` / `transform-es.log` / `transform-fr.log` /
  `transform-it.log` / `transform-ja.log` / `transform-ko.log` / `transform-nl.log` /
  `transform-pt.log` / `transform-ru.log`（均留存本目錄）。
- 驗證用副本（core 拷貝 33M ＋ 9 版產出約 300M）已刪，僅留日誌與 diff 檔
  （`diff-ko.txt`、`diff-others.txt`）。

## 3. ko：20 個 hunks 全部分類（`diff-ko.txt`）

content12.py / content34.py / content56.py / content7.py / content8.py 共 **20 hunks**，無剩餘：

- **D1-core 中文 ×11 行**（平行修復帶入，本輪未碰）：P1 標題+正文、P1「本週大事」、
  P2 小雪正文、P3 標題+正文、P4 標題+正文、P4 圖注、P7 讀者信、P8 Q144——
  與 PROOF-NOTE 的 11 處逐一對應（text.md:53/61/257/460/1155/1197/1934/1946/2480/5017/5778）。
- **D1-ko ×3 行**（本輪）：content12 P1 gloss、content12 P2 gloss、content34 P4 gloss，
  `다음 주 일요일`→`이번 주 일요일`。
- **D2 ×1 hunk**（核心 fix2 帶入，本輪未碰）：content56 香港表 BABYMONSTER 行刪除、
  表框高 480→418、by4 498→436（與 PROOF-NOTE 所述 fix2 做法逐數一致）。
- **核心另改 ×1 行**（平行帶入，非本輪）：content56 `怎麼辦？先選一件，再看轉播——四件事只能取捨。`
  ——盤上核心 content56.py:131 已帶，非 tables.py 改動。
- **本輪 M1 ×1**（content7:18）、**M2 ×1**（content7:52）、**M3 ×1**（content34:146）、
  **M4 ×6 行**（content56:178/191/195、content8:26/62/70）、**M5 ×1**（content8:116）。
- bslib4.py / render.py / ABSTRACT.txt：diff 為空。
- 舊串在 scratch-ko 全部 content 文件中 0 命中：`다음 주 일요일` 0、`결승선` 0、`밤의` 0、
  `참고:` 0、`입니다` 0（已發版 5 處）、ASCII `개방형 과제 - ` 0。
  新串：`이번 주 일요일` 3 處、`참고｜` 2 處（M3 行 + 既有另一處）、`개방형 과제 — ` 1 處。

## 4. 其餘 8 語：零波及驗證（`diff-others.txt`，100 個 hunks 全部分類）

- **de 12** = D1-core 8 hunks + D2 2 hunks + 核心另改 1 + P7 預告條手修 1（`p.rect … 104`，
  FANOUT-REPORT de 節已記錄的手工修復，非本輪）。
- **fr 12** = D1-core 8 + D2 2 + 核心另改 1 + fr fix1 Astuce mémoire 1（tables.py 已帶 fr fix1，
  已發版仍為舊句——平行修復帶入）。
- **es 11** = D1-core 8 + D2 2 + 核心另改 1。
- **it 15** = D1-core 8（其中 P1 hunk 內含 D3-1）+ D2 2 + 核心另改 1 + D3 ×4 獨立 hunks
  （D3-2 `si tiene`、D3-3/D3-4 `si ripete`、D3-5 `prevede 4`；D3-1 `si tiene` 在 P1 hunk 內）。
- **pt 11**、**nl 11** = D1-core 8 + D2 2 + 核心另改 1。
- **ru 16** = D1-core 8 + D2 2 + 核心另改 1 + ru 表值漂移 5（前存平行修復，非本輪）：
  皮卡丘 gloss `шар-Пикачу`→`надувной Пикачу`、迪士尼 B1 `Диснее`→`Диснейленде`、
  皮卡丘填空同改、M1 `Выучите их раз`→`Выучите их один раз`（終點 `финиш` 本身未動）、
  迪士尼 A2 `Диснее начинается`→`Диснейленде начинается`、Q134 `集點。`→`集點.`。
  其中 diff 顯示的 `н��чинается` 為顯示偽影：已按字節核實 tables.py 含 0 個 U+FFFD，
  :1772/:2091 的 ru 值為正確俄語 `начинается`。
- **ja 12** = D1-core 8 + D2 2 + 核心另改 1 + 迪士尼 48 天注改寫 1（前存平行修復，非本輪）。
- **結論：本輪改動未波及其他語**——8 語各自的 M1/M2 值與已發版逐字一致
  （除上述前存漂移外無任何其他 diff）；M1/M2 的 ru/fr 等值在本輪前後均未動。

## 5. 未做

- 未改核心、未改本版成品、未重建、未跑 insert.py / lint --write；無 git 寫操作（僅探針）。
- D1 中文、D2 版內一概未碰。P7 欄高與 occlusion 終驗留待重建輪次（見 FIX-LOG 版面影響評估）。
- scratch 驗證副本已刪（本地存儲規矩：推完/發完及時清中間件）；只留日誌與 diff 檔。
