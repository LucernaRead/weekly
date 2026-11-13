# FIX-LOG — W47 core-zh-tw fix4：三處源句修復（P7 記憶法、P7 M1 詞表、P1 本週日末條）

- **任務**：core-zh-tw fix4（葉子，不派 subagent；與 fix1、fix2、fix3、re-proof 均不是同一人）
- **修復對象**：`~/workspace/weekly-git/production/2026-w47/core-zh-tw/`（僅核心，不碰其他家庭、tools/、issues/）
- **缺陷**：三處源句（見 §2；均為 re-proof/協調員指派的源句錯誤，非自選）
- **時間**：2026-11-11 09:43–09:54 UTC（04:43–04:54 EST）
- **日誌目錄**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-core-zh-tw4/`
- **先讀**：fix3 `scratch-fix-core-zh-tw3/FIX-LOG.md` + `GATE-LOG.md`（構建命令與門禁方法照此復現）；fix3 的 `check_fillin_keys.py` 已複製至本目錄重跑。

## §0 探針與基線（開工前實測）

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin`：rc=0（`9daeafb9…`）。
- 探針寫盤 `scratch-fix-core-zh-tw4/probe.txt` 成功；全程 `TMPDIR=<scratch>/tmp`，未寫 /tmp（開工時實測 /tmp 僅 3%，任務稱已滿是舊況；仍全程避開 /tmp）；無 `Disk quota exceeded`。
- **基線三件 SHA 與任務值逐字一致**（動手前實測）：印刷 19,420,533 B / `11dae5e73bdcea590bcb54523bafd09c8d39d56b704ee0c747de6ed7a023a78f`；網頁 2,324,030 B / `624685e427ee1800bbdc6955ab2c1edb2217b2ff3c96bdcbcf0baa408db0afd4`；text.md 49,766 B / `80ed153b66f899e54d991e8ba8828d1995a6830012817b730941046bb62a0560`（fix3 落地態）。
- 動手前已存修前 SVG 哈希（`svg-hashes-before.txt`）、修前 text.md（`text-md-before.md`）、修前三源文件副本（`content7.py` / `content12.py` / `content56.py`）於本目錄。

## §1 動手前核對（屬實，方可動手）

- **修 1 表鍵核對**：`scratch-fanout-zh-tw/tables.py:2173` 新源鍵經正則提取，與任務給定的改後句**逐字節一致**（Python `assert table_key == required` 通過），未自行改措辭：
  `Memory trick: learn 入圍 first, then 星光大道 (the red carpet at 17:00, before the ceremony), then the ceremony （頒獎） at 18:30.`
- **修 2 原文核對**：`content7.py:18` 與任務原文逐字一致（含 `終點 (finish line)`）。
- **修 3 原文核對**：`content12.py:68` 為 `"本週日 11/22 遊行、金馬獎、鋼雕閉幕、小雪"`，與任務一致；小雪已在 P2（L111 文章）與 P6（時間軸/題目）另列，改後不丟信息（修後 text.md `小雪` 37→36，僅減 P1 框內 1 次）。
- **禁動項**：`content56.py:131` 修前 SHA 已存（`content56-before.sha`），修後 `sha256sum -c` 通過——**未動**；`scratch-fanout-zh-tw/tables.py` 未動（機制重 key 由協調員另派）；其餘核心文件未動。

## §2 三處改動（僅此三行，diff 見下）

1. **`content7.py:52`**（P7 B1 記憶法源句；地點錯 + 順序倒置：星光大道是 17:00 紅毯不是地點，頒獎 18:30 在後）：
   - 改前：`b.para("Memory trick: learn 入圍 first, then the ceremony （頒獎）, then the place it happens （星光大道）.", 22)`
   - 改後：`b.para("Memory trick: learn 入圍 first, then 星光大道 (the red carpet at 17:00, before the ceremony), then the ceremony （頒獎） at 18:30.", 22)`
2. **`content7.py:18`**（P7 A2 詞表「終點」注音錯）：
   - 只改 `(finish line)` → `(end point)`，句其餘一字不動。
   - 改後：`a.para("Parades give you four useful words: 遊行 (parade), 封王 (clinching the title), 夜間 (night-time) and 終點 (end point). Learn them once, and every parade makes sense.", 22)`
3. **`content12.py:68`**（P1「本週大事」末條與 P6 規範矛盾）：
   - `"本週日 11/22 遊行、金馬獎、鋼雕閉幕、小雪"` → `"本週日 11/22 遊行、金馬獎、鋼雕閉幕、夜間遊行"`
- **diff 範圍驗證**：修前副本 vs 修後源文件，`diff` 僅上述 3 行（`content7.py` 2 行、`content12.py` 1 行）；`content56.py` diff 為空。

## §3 重建（工具 venv，日誌見本目錄）

- `run.py` RC=0（build.log；TOTAL 150，A2 44 / B1 74 / B2 32，分頁 10/18/18/18/18/18/12/38，與修前一致；0 FLOW OVERFLOW / 0 HEAD TOO WIDE；`flow[P7-b1] ended col 0/0 y=1535 (bottom 1560)`——新記憶句比修前長（修前 y=1501），仍留 25px 餘量，無溢出；`flow[P1-lead] y=1659 (bottom 1935)` 不變）。
- `render.py` RC=0（render.log）；`tools/webpdf.py svg Lucerna-VOL4-web.pdf` RC=0（webpdf.log，8 頁，46,212 text bytes）；`export_zhtw_textmd.py svg 2026-w47-zh-tw-en.text.md "Lucerna Weekly — Traditional Chinese, English explanations"` RC=0（export.log，寫出 33,114 字符，修前 fix3 為 33,082）。
- **僅 p1-front.svg 與 p7-lang.svg 變化**（`svg-hashes-before.txt` vs `svg-hashes-after-run.txt` diff 僅此兩行：p1 `0a362c6e…`→`cc70b39c…`，p7 `292a5110…`→`839a8093…`；其餘 6 頁與修前逐字節相同——本次修復只動 P1、P7，無其他頁回歸）。
- `webpdf.py` 為 commit `40963281` 的定稿版，直接使用，未改動。

## §4 交付物（新雙 PDF + text.md，以本次重建實測 SHA 為準）

| 文件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 `Lucerna-VOL4.pdf` | 19,420,551 B | `97e896947fba550a0e4dd496e093a2cbafef88ed5cd0398052a3508aa77f11b0` |
| 網頁 `Lucerna-VOL4-web.pdf` | 2,324,051 B（< 7 MB） | `121cba14278ef1af117eff324b4ac9c2ec6837e0564186c3d91bd98148cd8d62` |
| `2026-w47-zh-tw-en.text.md` | 49,798 B | `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b` |

- 雙 PDF 各 8 頁、1462.5×2025 pt。
- 印刷 PDF 確定性驗證：`render.py` 再跑一次，印刷 SHA 仍為 `97e89694…77f11b0`（render2.log），兩跑相同；網頁 PDF 未重跑（webpdf 每次 SHA 不同為已知特性，KIT 以本次交付文件為準）。
- 修前基線（fix3 2026-11-11 09:35）：print 19,420,533 B / `11dae5e7…23a78f`；web 2,324,030 B / `624685e4…0afd4`；text.md 49,766 B / `80ed153b…a0560`。
- **text.md 字節變化可解釋（+32 B，僅三處源句所致）**：diff opcode 逐行求和 = +32 B，與文件增量 49,766→49,798 完全一致：
  - 修 3（L265）：`幕、小雪` → `幕、夜間遊行`，+6 B；
  - 修 2（L4225）：`(finish line). Learn` → `(end point). Learn`，−2 B；
  - 修 1（L4487–4499）：新句原文 +29 B，但 SVG 斷行重排後 export 行數少 1 行（少 1 個 `\n`），淨 +28 B；
  - 合計 +6 −2 +28 = **+32 B**。另：text.md 內 `小雪` 37→36、`夜間遊行` 24→25、`finish line` 1→0、`end point` 0→1。
- **KIT 已更新**：`WEEKLY-KIT.md` 僅 L53（雙 PDF 字節數/SHA）與 L129（text.md 字節數/SHA）改為本次交付值，標為 fix4；括號內補記 fix3 舊值備查（`WEEKLY-KIT-before.md` 存本目錄，diff 僅此兩行）。

## §5 修後核實（見 GATE-LOG 全文）

- 三處新句在雙 PDF 文字層、text.md、SVG 均完整上版（`print.txt` vs fix3 `print.txt` diff 僅 3 處：P1 L57、P7 L640、P7 L688–691）。
- **54 個填空鍵答案詞出自正文複核：54/54**（`check_fillin_keys.py` 重跑，缺失 []；D3「取捨」正文仍在，雙 PDF 文字層各 2 次）。
- 防回退：D1 `本週日` 11/11、`下週日` 0；D2 `BABYMONSTER` 0（源、text.md、雙 PDF 文字層）；Q34（《月球之旅》是哪一年拍的？鍵 `34. C — A Trip to the Moon was made in 1902.`）在 text.md keys 區仍為 L5772，與修前同行同文；`content56.py:131` D3 句「——四件事只能取捨」SHA 未變。
- 目視：P7 記憶句完整四行上版、`ceremony （頒獎）` 間有空格、無溢出（`p7-crop.png`）；P7 M1 句完整（`p7-m1-crop.png`）；P1 本週日框末條兩行完整、框體無破損（`p1-crop.png`）。
- 一處文字層提取說明（非內容缺失）：新記憶句中 `ceremony （頒獎）` 的空格在 SVG 內確實存在（節點 161 `ceremony), then the ceremony ` 尾端帶空格，節點 162 `（頒獎）` 起於 x=849.6；目視有空格），但 `pdftotext -layout` 拼接相鄰 span 時將該空格略去，印出 `ceremony（頒獎）`。印/網雙版一致、字符多重集差 0/0；屬提取拼接 artifact，視覺與 SVG 均正確。舊句同位置空格在同一節點內，故舊提取保留——差異僅由斷行位置造成。

## §6 未做事項（按任務範圍）

- 未跑 insert.py、lint --write；未做任何 git 寫操作（除任務要求的 hash-object 探針外）；未碰 fan-out 各版、tools/、其他目標語、其他家庭；未動 `content56.py:131` 與 `scratch-fanout-zh-tw/tables.py`。
- 未派復校：修後全量復校由協調員另派。
