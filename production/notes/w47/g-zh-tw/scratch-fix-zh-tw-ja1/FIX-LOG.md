# FIX-LOG — W47 zh-tw-ja fix1（D-ja-2 + D1-日語，機制層修復）

- **Builder**：fix1（葉子，未再派 subagent）
- **範圍**：只修機制層 `scratch-fanout-zh-tw/tables.py` 的 **ja 值 4 處**（D-ja-2 ×1、D1-日語 ×3）。D-ja-1 **未動表**，只核實 + 寫擬改句（見 §3）。未改核心、未改本版成品 content/PDF/SVG、未重建任何版、未碰 core-zh-tw、未碰其他家庭、tools/、issues/，未跑 insert.py / lint --write、未 commit、未 push、無任何 git 寫操作（僅探針 `git hash-object -w`）。
- **復校對象**：`production/2026-w47/2026-w47-zh-tw-ja/`，PROOF-NOTE（`scratch-proof-zh-tw-ja1/PROOF-NOTE.md`）結論 (b)：D1 已知 + D-ja-1/D-ja-2 新。
- **先讀**：SOP.md §8 與 §1.1 全文、`~/workspace/weekly-git/AGENTS.md`、協調員 brief、PROOF-NOTE 全文。

## 探針（開工與每步寫盤前重探）

- 開工 2026-11-11 ~09:32 UTC：`git -C ~/workspace/weekly-git hash-object -w --stdin` rc=0；筆記目錄 `scratch-fix-zh-tw-ja1/probe.txt` 真實寫盤 rc=0。
- 編輯 tables.py 前重探 rc=0；scratch 驗證寫盤前重探 rc=0；清理副本後、寫本日誌前重探 rc=0。
- 全程無 EDQUOT；`df`：/home/hatch 150G 總，73G 已用，77G 可用。/tmp 未用，中間件全在 workspace scratch 內。

## 0. 行號勘誤（PROOF-NOTE / 任務書的舊行號已漂移，先正名）

- 本輪實測時 `tables.py` 共 2430 行，`ENTRIES = 242`（it fix1 時為 238；其後表內新增 4 條，行位整體下移約 44 行）。
- D-ja-1 條目實際位置：**源鍵 L2173、fr 值 L2175、ja 值 L2181**（PROOF-NOTE 與任務書寫的 L2137 / L2131 是舊行號，現已失效；同樣，PROOF-NOTE 寫的「詞卡句 tables.py L2126」實為 L2170）。本日誌以下一律用實測行號。
- D-ja-2（L1564）與 D1-日語（L253/L275/L330）行號與 PROOF-NOTE 一致，未漂移。

## 1. 改動：D-ja-2（P8 第 77 題答案注記，天數寫成日期）

**文件**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-zh-tw/tables.py:1564`（只改 ja 值內一個子串；英文源鍵 L1556 與其餘 8 語值一字未動）

- **源鍵**（L1556）：`Nov 17-30 is 14 days, plus 31 in December, plus 3 in January = 48.`
- **改前**：`11月17日〜30日は14日、12月31日、1月3日を足すと48日だ。`
- **改後**：`11月17日〜30日は14日、12月は31日、1月は3日、合わせて48日だ。`
- **鍵值不動**：B（48 天）本身正確，鍵未改；同版 P5「計算の練習」注釈（tables.py L654，`11月17日〜1月3日は48日間（14＋31＋3）`）寫法一致，新句與之統一。

## 2. 改動：D1-日語 3 處（「来週の日曜日」→「今週の日曜日」）

**文件**：同表 L253 / L275 / L330（各只改 ja 值內「来週の日曜日」→「今週の日曜日」一處；英文源鍵與其餘 8 語值一字未動）

### (1) P1 Note — tables.py:253（text.md L101）
- **改前**：`味全龍の優勝パレードは来週の日曜日、11月22日（日）14:00、天母野球場から台北ドームまで行われる。天母では11月21日〜22日の2日間、ファン感謝祭がある。21日は芝生コンサートとキャンプ、22日は選手との交流だ。赤を着て龍チームを応援しよう。`
- **改後**：`味全龍の優勝パレードは今週の日曜日、11月22日（日）14:00、天母野球場から台北ドームまで行われる。天母では11月21日〜22日の2日間、ファン感謝祭がある。21日は芝生コンサートとキャンプ、22日は選手との交流だ。赤を着て龍チームを応援しよう。`

### (2) P2 Note — tables.py:275（text.md L508）
- **改前**：`来週の日曜日、11月22日は小雪、二十四節気の第20番目、冬の2番目の節気だ。冬は深まり、防寒が必要になる。小雪のあと、北東の季節風は強まり、天気は日ごとに寒くなる。頭・首・足を暖かく。夜の10〜15分の温かい足湯は眠りを助ける。`
- **改後**：`今週の日曜日、11月22日は小雪、二十四節気の第20番目、冬の2番目の節気だ。冬は深まり、防寒が必要になる。小雪のあと、北東の季節風は強まり、天気は日ごとに寒くなる。頭・首・足を暖かく。夜の10〜15分の温かい足湯は眠りを助ける。`

### (3) P4 Note — tables.py:330（text.md L2032）
- **改前**：`味全龍の優勝パレードは来週の日曜日、11月22日（日）14:00、天母野球場から台北ドームまで行われる。天母では11月21日〜22日の2日間、ファン感謝祭がある。21日は芝生コンサートとキャンプ、22日は選手との交流だ。台北市は11月中、Uスポーツのポイントを倍増する。1回5ポイントが10ポイントに、267か所で。`
- **改後**：`味全龍の優勝パレードは今週の日曜日、11月22日（日）14:00、天母野球場から台北ドームまで行われる。天母では11月21日〜22日の2日間、ファン感謝祭がある。21日は芝生コンサートとキャンプ、22日は選手との交流だ。台北市は11月中、Uスポーツのポイントを倍増する。1回5ポイントが10ポイントに、267か所で。`

### 不動項
- 全表 `来週の日曜日` 改前 3 處、改後 **0 處**；`今週の日曜日` 改後 3 處。
- L2312 `下期預告　来週 (VOL.5)`（指下一週，正確）**未動**——三處改動用行號定點 sed，只命中 253/275/330。
- D1 中文 11 處未碰（隨核心 fix1 + 重擴帶走，見 §5 分類）。

## 3. D-ja-1：只核實 + 擬改句（未動 tables.py L2181）

### ① 源句核實：復校指控屬實（兩點皆錯）

核心源句（只讀，未改）`~/workspace/weekly-git/production/2026-w47/core-zh-tw/content7.py:52` 全文：

> `b.para("Memory trick: learn 入圍 first, then the ceremony （頒獎）, then the place it happens （星光大道）.", 22)`

核實證據（皆盤上實查）：

1. **地點錯**：星光大道不是典禮地點，而是典禮前的紅毯儀式。已發版 text.md L1205（P3 正文）：「頒獎典禮在下週日（11月22日）舉行，地點在台北流行音樂中心」；同版詞卡句（tables.py L2170 的 ja 值）：「星光大道は式典の前のレッドカーペットだ」；P3 正文亦寫「頒獎典禮前，先走星光大道」。
2. **順序倒置**：星光大道 17:00 在頒獎典禮 18:30 之前。已發版 text.md L1243（P3 注釈）：「カーペットは17:00、式典は18:30」；L3648（P6 時間軸）：「レッドカーペット17:00、授賞式18:30」；Q42/Q85 鍵皆為 1.5 小時差。源句教的順序「入圍 → 頒獎 → 星光大道」把紅毯放在典禮之後。
3. 同表另一源條目（tables.py L289）自述亦證實：「The 63rd Golden Horse Awards follow on Sunday, Nov 22 at the Taipei Music Center — red carpet 17:00, ceremony 18:30」——地點與時間與源句自相矛盾。
4. 現行 ja 值（tables.py L2181，未動）：`覚え方のコツ：まず入圍、次に式典（頒獎）、そして行われる場所（星光大道）の順に覚えよう。`——逐字譯自錯源句，同錯。

### ② 擬改後的正確 ja 值全文（待落實，不入表）

> `覚え方のコツ：まず入圍、次に星光大道（式典の前のレッドカーペット）、そして式典（頒獎）の順に覚えよう。`

（按 PROOF-NOTE 修法：順序改為 入圍 → 星光大道（式典の前のレッドカーペット）→ 式典（頒獎）；刪去錯誤的「行われる場所（星光大道）」說法。）

**未動表的原因**：本任務書定——該條目的英文源鍵本身將由核心 fix4 改寫，現在改 ja 值會被 re-key 丟棄。但本輪實測發現新情況（見 §4 與 §6）：表內源鍵**已先行改寫**為新句（L2173），核心 fix4 尚未落地。ja 值的落實時機以協調員裁定為準；擬改句已一次寫對，re-key/重擴時直接取用。

### ③ 參考：fr / ko 兩版已修的同句值（只記錄，不改 fr 值）

- **fr 值**（tables.py L2175，zh-tw-fr fix1 已修）：`Astuce mémoire : apprenez d'abord 入圍, puis 星光大道 (le tapis rouge à 17:00, avant la cérémonie), puis la cérémonie （頒獎） à 18:30.`
- **fr 值與新源句匹配記錄**：匹配。順序 入圍 → 星光大道 → 式典；星光大道定性為「式典前的紅毯」（le tapis rouge, avant la cérémonie），無「地點」說法；與擬議新源句（PROOF-NOTE 建議核心改法：`learn 入圍 first, then 星光大道 (the red carpet before the ceremony), then the ceremony （頒獎）`）語義一致。fr 值另注時間 17:00 / 18:30——與表內現行新鍵 L2173（見 §4）所含 "at 17:00" / "at 18:30" 一致；若核心 fix4 最終寫法不帶時間，fr 值的時間注仍屬實（不錯，但超出源句），是否保留由協調員在 re-key 時定，**本輪不改 fr 值**。
- **ko 值**（tables.py L2182，本輪驗證期間由 zh-tw-ko fix1 同步修過，scratch-ko diff 已見）：`외우는 요령: 먼저 入圍을 외우고, 그다음 星光大道(17:00 레드카펫, 시상식 전), 그다음 시상식(頒獎) 18:30을 외워요.`——與 fr 同型（正確順序 + 時間注），亦匹配新源句。
- **其餘 7 語值在新鍵下仍錯**（見 §4）：de/es/it/pt/nl/ru/ja 仍為舊順序 +「地點」說法。

## 4. 重要發現：Memory-trick 條目已先行 re-key（表側），但 7 語值未跟上

- 表內源鍵現為 L2173：`Memory trick: learn 入圍 first, then 星光大道 (the red carpet at 17:00, before the ceremony), then the ceremony （頒獎） at 18:30.`——即正確的新句（含 17:00 / 18:30）。
- 但 L2173 條目下 9 語值中，**只有 fr（L2175）與 ko（L2182）已改為正確寫法**；de（L2174）、es（L2176）、it（L2177）、pt（L2178）、nl（L2179）、ru（L2180）、ja（L2181）仍譯舊句（入圍 → 式典 → 地點（星光大道）），在新鍵下語義全錯。
- 後果：核心 fix4 一落地（新句進核心），重擴 transform 會通過（鍵匹配），但 7 語版會**靜默印出錯誤的 Memory-trick 行**——不再有 transform 大聲失敗兜底。重擴前必須先把 de/es/it/pt/nl/ru/ja 7 語值改為正確寫法（ja 值見 §3②；其餘 6 語各由其 fix1 按 fr/ko 同型改）。
- 另：fr fix1 的 FIX-LOG 寫明它只改 fr 值、「英文源串未動」；本次 re-key 的操作者未在任何 fix 日誌留名（grep `re-key/rekey/2173` 無命中），歸屬未明，僅記錄現象。

## 5. Scratch 驗證（未動成品，副本已清）

方法（沿用 zh-tw-it fix1）：筆記目錄 `work/` 內複製盤上 core-zh-tw（33M，已帶 core fix1 的「本週日」）＋ 改後 tables.py ＋ transform.py（僅 PROD 指針改向 scratch `work/prod`），逐語重跑；驗證後整個 `work/` 已刪（320M），僅留日誌與 diff 檔（`transform-*.log`、`diff-*.txt`）。

### 5.1 首輪失敗：2 條源鍵與盤上核心漂移（非本輪造成，如實記錄）

- 第一輪 9 語**全敗**，同一斷點：`Parades give you four useful words: … 終點 (end point) …`（tables.py L2107 鍵）——盤上核心 `content7.py:18` 已是 `終點 (finish line)`，鍵 0 命中。
- 對齊該鍵後（僅 scratch 副本）第二輪 9 語全敗於另一斷點：`Memory trick: … 星光大道 (the red carpet at 17:00, before the ceremony) …`（tables.py L2173 新鍵）——盤上核心 `content7.py:52` 仍是舊句，鍵 0 命中。
- 兩處漂移皆為**表鍵 vs 核心現狀不一致**，與本輪 4 處改動無關（it fix1 09:06–09:11 曾 9/9 通過；漂移發生在其後：表內新增 4 條、Memory 條目被 re-key；核心 fix3 亦在同期跑，`scratch-fix-core-zh-tw3/` 09:35 在跑）。scratch 副本內將第二鍵亦對齊為盤上核心現有的舊句後，第三輪 **9/9 TRANSFORM OK**（各 248 行日誌，`transform-{de,fr,es,it,pt,nl,ru,ja,ko}.log`）。
- **真實 tables.py 未動這兩鍵**：L2107 仍為 `end point`、L2173 仍為新句。重擴前必須先解決（見 §6 待跟進項①②）；否則對盤上核心跑 transform 會大聲失敗、9 版全卡。

### 5.2 ja：4 處新值全部流入，舊串歸零

scratch-ja（已刪，見日誌與 `diff-ja.txt`）：
- `content12.py:37` — P1 Note，`今週の日曜日` ✓（tables.py L253）
- `content12.py:113` — P2 Note，`今週の日曜日` ✓（tables.py L275）
- `content34.py:127` — P4 Note，`今週の日曜日` ✓（tables.py L330）
- `content56.py:60` — P8 第 77 題注記，`11月17日〜30日は14日、12月は31日、1月は3日、合わせて48日だ。` ✓（tables.py L1564）
- 舊串在 scratch-ja 全部 content 文件中 **0 命中**（`来週の日曜日`、`12月31日、1月3日を足すと48日` 各 0）。
- D-ja-1 舊 ja 值按指令原樣流入 scratch-ja `content7.py:52`，與已發版一致（diff 該行無差異）。

### 5.3 ja：scratch-vs-已發版 diff 全分類（content 文件，KIT 除外）

`diff-ja.txt` 共 18 個 content hunks，**全部分類，無剩餘**：
- **D1-core ×10**（平行修復帶入，本輪未碰）：content12.py:33、:35、:68、:111；content34.py:17–18、:123、:125、:196；content7.py:99；content8.py:86——均為盤上核心已帶 core fix1 的「本週日」。
- **D1-ja ×3**（本輪）：content12.py:37、:113；content34.py:127。
- **D-ja-2 ×1**（本輪）：content56.py:60。
- **核心 fix2 平行 ×4**（本輪未碰）：content56.py:96、:104a105、:107、:131——P6 香港盒 480→418（`fix2: HK box shrank`）、刪 BABYMONSTER 一行、「四件事只能取捨」增句；皆為盤上核心現狀。
- 另有 `WEEKLY-KIT.md` 整檔差異 1 項：scratch 拷的是核心 KIT（「Traditional Chinese core」），已發版是本版 KIT——拷貝噪聲，非內容差異。另有 `Only in` 噪聲：核心目錄殘留的 `2026-w47-zh-tw-en.text.md`、`Lucerna-VOL4.pdf`、`Lucerna-VOL4-web.pdf` vs 已發版的 `2026-w47-zh-tw-ja.text.md`、`Lucerna-VOL4-JA.pdf`、`Lucerna-VOL4-JA-web.pdf`——transform 拷貝件，非內容差異。`bslib4.py` / `render.py` / `ABSTRACT.txt` diff 為空。
- **P8 前存缺口已閉合（ja）**：it fix1 時缺表的 6 條注記源串，現表已補齊——scratch-ja 在 content56.py / content8.py 對應 6 行皆為日語、無英文殘留（`The ceremony is at the Taipei Music Center.` / `Xiaoxue is Nov 22.` / `Four big events fall on the same Sunday.` / `Collecting points is 集點.` 全版 0 命中），且 `diff-ja.txt` 在該 6 行零差異（與已發版手補譯逐字一致）。

### 5.4 其餘 8 語：零波及證據

每語 scratch vs 已發版 diff（`diff-{de,fr,es,it,pt,nl,ru,ko}.txt`），content hunks 全分類如下；**其中無任何一處與本輪 4 處 ja 改動有關**（本輪 4 處改動皆為 ja 值內子串；其餘 8 語的 ja 值未動，其餘語值亦未動）：

| 語 | D1-core | 本語 fix1 平行 | 前存/平行其他 | 計 |
|---|---|---|---|---|
| de | 10 | 0 | 6（content56 fix2 ×4；P7 teaser 118 vs 104 ×2，FANOUT-REPORT 已記的手工修復） | 16 |
| fr | 10 | 1（content7.py:52 fr fix1 的 Astuce mémoire） | 4（content56 fix2 ×4） | 15 |
| es | 10 | 0 | 4（content56 fix2 ×4） | 14 |
| it | 10 | 5（D3 it fix1：content12:41、:123；content56:44；content7:60、:77） | 4（content56 fix2 ×4） | 19 |
| pt | 10 | 0 | 4（content56 fix2 ×4） | 14 |
| nl | 10 | 0 | 4（content56 fix2 ×4） | 14 |
| ru | 10 | 9（ru fix1：D1-俄語 3 處 content12:37、:113、content34:127；詞彙 3 處 content56:28、:34、:55；content7:18「Выучите их один раз」；content8:22、:62） | 4（content56 fix2 ×4） | 23 |
| ko | 10 | 13（ko fix1：D1-韓語 3 處 content12:37、:113、content34:127；Memory-trick content7:52；Parades content7:18；P8 敬語 6 處 content56:177、:190、:194、content8:26、:62、:70；content34:149 標點；content8:116 破折號） | 4（content56 fix2 ×4） | 27 |

- **結論**：8 語與已發版的全部差異，皆為 D1-core 平行、核心 fix2 平行、各語自身 fix1 平行或前存手工修復——**本輪 4 處 ja 改動對其餘 8 語零波及**。

## 6. 待協調員跟進項（本輪未做，需他人裁定/動手）

1. **重擴前必先解 2 條源鍵漂移**（否則 transform 對盤上核心 9 語全敗，見 §5.1）：
   - (a) tables.py L2107 鍵 `終點 (end point)` vs 核心 `content7.py:18` 的 `終點 (finish line)`——機制側改鍵為 `finish line` 即可。各語值多已是終點線語義（de Ziellinie、fr ligne d'arrivée、it traguardo、pt linha de chegada、nl finish、ru финиш、ja ゴール、es meta），僅 ko 現值「끝나는 곳」（終點處，偏 end point 語義；已發版為「결승선」）是否需隨鍵改回，由 ko 線在 re-key 時核。
   - (b) Memory-trick：表鍵 L2173 已是新句，核心 `content7.py:52` 仍是舊句——等核心 fix4 落地新句（或 re-key 輪次另行裁定）。核心 fix4 寫法若與 L2173 現行新鍵有出入（例如不帶 17:00/18:30），鍵須再對齊一次。
2. **Memory-trick 7 語值跟進**（見 §4）：de/es/it/pt/nl/ru/ja 在新鍵下仍錯；ja 擬改句見 §3②，其餘 6 語各由其 fix1 按 fr/ko 同型改。重擴前未改完會靜默印錯。
3. **fr 值無需重改**（見 §3③）：fr L2175 已匹配新源句；僅當核心 fix4 最終寫法不帶時間時，再議是否去掉 fr 值的 17:00/18:30 時間注。
4. **D1 中文 11 處**：核心 fix1 已進盤上核心，重擴即帶走（本輪 scratch diff 已見 10 處平行帶入；第 11 處為 text.md L5398 的 P8 Q144 題面，在 content8.py:86 的同一 hunk 內，"本週日___出發" 已帶入——計數：10 個 hunk 含 11 處中文改動）。
5. **P8 前存缺口（他語）**：ja 的 6 條已閉合；ko 的 6 條在 scratch-ko 與已發版間仍有敬語差（이에요 vs 입니다，ko fix1 同期改值所致），屬 ko 線內部事，不屬本輪。

## 未做

- 未動 tables.py L2181（D-ja-1 ja 值，按任務書只記錄擬改句）與 L2175 fr 值。
- 未改核心（core-zh-tw 只讀；content7.py:52 全文見 §3①）、未改本版成品、未重建、未跑 insert.py / lint --write；無任何 git 寫操作（僅探針 `git hash-object -w`）。
- 未碰 D1 中文、D2 網頁、其他家庭、tools/、issues/。
- scratch-only 的 2 處鍵對齊（§5.1）只存在於已刪的 `work/tables.py` 副本內，真實 tables.py 未動。
- 驗證用副本 `work/`（320M）已按本地存儲規矩清理；僅留 `transform-*.log`（9 份）與 `diff-*.txt`（9 份）+ 本日誌。
