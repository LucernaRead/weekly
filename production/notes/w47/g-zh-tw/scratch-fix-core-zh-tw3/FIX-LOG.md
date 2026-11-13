# FIX-LOG — W47 core-zh-tw fix3：D3「取捨」未在本期出現（只修 D3 一條）

- **任務**：core-zh-tw fix3（葉子，不派 subagent；與 fix1、fix2、re-proof 均非同一人）
- **修復對象**：`~/workspace/weekly-git/production/2026-w47/core-zh-tw/`（僅核心，不碰其他家庭、tools/、issues/）
- **缺陷**：re-proof D3（`scratch-proof-core-zh-tw-reproof/PROOF-NOTE.md` §4）——P6 填空題 Q95 答案詞「取捨」從未在本期出現：54 個填空鍵中 53 個答案詞出自正文，獨缺此詞。題面（P6 Q95）：「四件大事同一天，要學會___。」鍵：`95. 取捨 — You cannot see everything: choose.`（鍵本身無誤，中文正確）。
- **時間**：2026-11-11 09:31–09:4x UTC（04:31–04:4x EST）
- **日誌目錄**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-core-zh-tw3/`
- **先讀**：SOP.md §8、§1.1 全文；`~/workspace/weekly-git/AGENTS.md`；`hidden_files/w47/briefs/brief-coordinator.md`；re-proof `PROOF-NOTE.md` + `GATE-LOG.md`；fix1 `scratch-fix-zh-tw-core1/FIX-LOG.md`；fix2 `scratch-fix-core-zh-tw2/FIX-LOG.md`。

## §0 探針（開工前 + 每次寫盤前重探）

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin`：rc=0（`9daeafb9…`）。
- 探針寫盤 `scratch-fix-core-zh-tw3/probe.txt` 成功；全程無 `Disk quota exceeded`。
- 開工時 `/tmp` 實測僅 2%（任務稱已滿是舊況）；全部中間輸出仍寫入本筆記目錄，未寫 /tmp。
- `git status`：倉內另有 149 條未提交改動（W43 等他線工作，開工前已存在），一概未碰；`production/2026-w47/core-zh-tw/` 為未追蹤目錄（`??`，W47 生產中狀態），本次未做任何 git 寫操作。

## §1 動手前實測核對 D3（屬實）

- **舊成品 SHA 與任務值逐字一致**（重建前實測）：印刷 19,419,829 B / `3ab3f75815444d6b6da389f026e82a17e4d747226698083c16f6b26523d3474e`；網頁 2,323,405 B / `582c4aa7b1a90a065c5d5e5e0f4b7219394a0089b67ee1791d2e700c8d46938e`；text.md 49,735 B / `7e1a45165dc663af5301d95784567b03f4e9f512766571e507663086d510791c`。
- **全核心 grep「取捨」**：源 `.py` 僅 1 處——`content56.py:184`（題目定義本身）；text.md 全文 1 處——L5898（keys 區鍵本身）；text.md 正文區（keys 區之前）**0 處**；正文 SVG（p1–p7，含 p6-deep.svg）**0 處**。
  - 註：`svg/p8-test.svg` 有 1 處——那是 P8 答案頁印出的第 95 鍵本身（P8 承載全部 150 鍵），不是正文出現；re-proof「8 個 SVG 0 處」指正文層，此處計法一致，D3 實質不變。
- **54 鍵系統性核查**（方法照 re-proof GATE-LOG §10 復現，腳本 `check_fillin_keys.py` 存本目錄）：從源 `.py` 解析全部 `e.ex/f.ex(..., "完成句子", "<key>", ...)` 調用得 54 個填空鍵，逐鍵查是否出現於 text.md keys 區（`答案　Answer keys` 行）之前。修前結果：**53/54，唯一缺失「取捨」**（`content56.py:184`，正文 0 次；其餘 53 鍵正文出現 1–119 次不等）。D3 屬實。
- **D1/D2 無回歸前置**：修前 text.md / 雙 PDF 文字層：`本週日` 11、`下週日` 0、`BABYMONSTER` 0（見 GATE-LOG）。

## §2 修法：取 re-proof 推薦項（在 P6 文章裡教這個詞），二選一取其一

- 採用推薦項 1：改 P6「怎麼辦？」段，題面與鍵不動，其餘 149 題不動。
- 未採用備選項 2（在「看活動三問」框加一句「四件大事，先選一件，就是取捨。」）：該框為定高 504px 矩形框，內容已近框底；文章段改動只加 9 字、主 flow 餘量大（見下），版面更穩。
- **唯一改動**（`production/2026-w47/core-zh-tw/content56.py:131`，P6 文章第二段）：

  改前全文：
  `f.para("怎麼辦？先選一件，再看轉播。遊行在街上，去現場最熱鬧；金馬獎在家看轉播，得獎名單一樣看得到；鋼雕在高雄、夜間遊行在新竹，去不了就留到下次。")`

  改後全文：
  `f.para("怎麼辦？先選一件，再看轉播——四件事只能取捨。遊行在街上，去現場最熱鬧；金馬獎在家看轉播，得獎名單一樣看得到；鋼雕在高雄、夜間遊行在新竹，去不了就留到下次。")`

  淨增 9 字（`——四件事只能取捨`，原句號改為破折號銜接）。英文 gloss、時間軸 caption、「看活動三問」框、「數字一覽」框、全部題面/鍵一概未動。

## §3 重建（工具 venv，日志見本目錄）

- `run.py` RC=0（build.log；TOTAL 150，A2 44 / B1 74 / B2 32，分頁 10/18/18/18/18/18/12/38，與修前一致；0 FLOW OVERFLOW / 0 HEAD TOO WIDE；`flow[P6-main] ended col 1/2 y=483 (bottom 860)`，餘量充足，無斷行溢出）。
- `render.py` RC=0（render.log）；`tools/webpdf.py svg Lucerna-VOL4-web.pdf` RC=0（webpdf.log）；`export_zhtw_textmd.py svg 2026-w47-zh-tw-en.text.md "Lucerna Weekly — Traditional Chinese, English explanations"` RC=0（export.log，寫出 33,082 字符，修前 fix2 為 33,069）。
- **僅 p6-deep.svg 變化**（`906ddb0d…` → `51dafd84a692439a0f43144a3de4e9bfd0c30cd81a76dbfc1a7cdd3a86e55058`），其餘 7 個 SVG 與修前逐字節相同（svg-hashes-before/after-run.txt diff 僅此一行；freeze 8/8 佐證，見 GATE-LOG）。
- text.md 字節變化 49,735 → 49,766（+31 B）：新句 `——四件事只能取捨。` 30 B 減原句號 3 B = +27 B，另 +4 B 為該段在 SVG 內多折一行、export 每行附加換行所致；正文 L3600 可見新句完整，鍵區 L5898 不變。

## §4 交付物（新雙 PDF + text.md，以本次重建實測 SHA 為準）

| 文件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 `Lucerna-VOL4.pdf` | 19,420,533 B | `11dae5e73bdcea590bcb54523bafd09c8d39d56b704ee0c747de6ed7a023a78f` |
| 網頁 `Lucerna-VOL4-web.pdf` | 2,324,030 B（< 7 MB） | `624685e427ee1800bbdc6955ab2c1edb2217b2ff3c96bdcbcf0baa408db0afd4` |
| `2026-w47-zh-tw-en.text.md` | 49,766 B | `80ed153b66f899e54d991e8ba8828d1995a6830012817b730941046bb62a0560` |

- 雙 PDF 各 8 頁、1462.5×2025 pt。
- 印刷 PDF 確定性驗證：`render.py` 再跑一次，印刷 SHA 仍為 `11dae5e7…23a78f`（render2.log），兩跑相同；網頁 PDF 未重跑（webpdf 每次 SHA 不同為已知特性，KIT 以本次交付文件為準）。
- 修前基線（fix2 2026-11-11 09:18）：print 19,419,829 B / `3ab3f758…3474e`；web 2,323,405 B / `582c4aa7…46938e`；text.md 49,735 B / `7e1a4516…0791c`。
- **未改 KIT**：`WEEKLY-KIT.md` 內舊 PDF 字節數／SHA 仍為 fix2 值。按任務範圍（只修 D3），KIT 由協調員／re-proof #2 後統一更新；此處如實記錄，不擅自改 KIT。

## §5 修後核實（D3 已閉合，見 GATE-LOG 全文）

- 全核心 grep「取捨」：源 `.py` 2 處（文章 L131 + 題目定義 L184）；text.md 2 處（正文 L3600 + keys 區鍵）；`svg/p6-deep.svg` 1 處（文章段）；雙 PDF 文字層各 2 處（正文 1 + P8 鍵 1）。
- **54 個填空鍵答案詞出自正文複核：54/54**（`check_fillin_keys.py` 重跑，缺失 []；「取捨」正文出現 1 次）。
- P6 卡片目視：新句完整上版，無溢出、無重疊、無壓頁腳；Q95 題面不動；時間軸、兩框、其餘題目與修前一致。
- D1 無回歸：text.md / 雙 PDF 文字層 `本週日` 各 11、`下週日` 0；D2 無回歸：`BABYMONSTER` 0。

## §6 未做事項（按任務範圍）

- 未跑 insert.py、lint --write；未做任何 git 寫操作（除探針 `hash-object` 外）；未碰 fan-out 各版、tools/、其他目標語、其他家庭；未動 §5 已裁定非缺陷項（未重提）。
- 未派復校：修後全量復校（re-proof #2）由協調員另派。
