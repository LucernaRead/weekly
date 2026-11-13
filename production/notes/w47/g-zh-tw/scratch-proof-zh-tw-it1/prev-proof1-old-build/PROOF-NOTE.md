# PROOF-NOTE — 2026-W47 zh-tw-it（proof1，獨立復校）

- 版：`production/2026-w47/2026-w47-zh-tw-it/`，VOL.4，繁體中文正文 × 意大利語講解
- 校對：proof1 從頭完整復校（text.md 全文 6,057 行對 core-zh-tw 全文 6,035 行逐行 diff；印刷/網頁 PDF 逐頁 pdftotext 驗證；SVG 層門禁重跑；渲染卡 P4、P7 目檢）
- 日期：2026-11-11（UTC）
- **結論：(b) 有缺陷，不可定稿** —— D1（已知）＋ D2（新）＋ D3（新）

## SHA 核對（先核對，通過）

| PDF | 大小 | SHA-256 前 16 位 | 結果 |
|---|---|---|---|
| 印刷 `Lucerna-VOL4-IT.pdf` | 19,420,291 B | `ec9d0624d91abb2a` | ✓ 與任務給定一致（全長 `ec9d0624d91abb2ae8875f5f51cb2064d7927d4f1a4a8e4f2454b1fb11894bce`） |
| 網頁 `Lucerna-VOL4-IT-web.pdf` | 2,306,683 B | `34c4ff2c9e3f1fe0` | ✓ 與任務給定一致（全長 `34c4ff2c9e3f1fe0e3714c773b5ead11306e542c4a60e52b2c815684ba986988`） |

## D1 —— 「下週日」指 11/22 是錯的（已知核心缺陷，核查計數，非新發現）

- **text.md「下週日」出現次數：11 次**（`grep -o` 計數 11；核心 `core-zh-tw-en.text.md` 為 0 次，核心對應處 11 次全為「本週日」）。
- 证据：刊期 2026-11-16（一）至 11-22（日）；`date -d` 驗證 2026-11-22 為星期日、2026-11-29 為星期日。11/22 是**本週日**，11/29 才是下週日。11 處所指事件（封王遊行、金馬獎頒獎）日期均為 11/22。
- 11 處（text.md 行號／頁／原文 → 應改）：
  1. L53，P1 頭條：`封王遊行，下週日天母出發！` → `封王遊行，本週日天母出發！`
  2. L61，P1 正文：`座總冠軍，封王遊行訂在下週日（11月22日）` → `訂在本週日（11月22日）`
  3. L259，P1 封面指南：`下週日` → `本週日`
  4. L462，P2 正文：`下週日（11月22日）` → `本週日（11月22日）`
  5. L1167，P3 頭條：`金馬獎下週日頒獎，誰會得` → `金馬獎本週日頒獎，誰會得`
  6. L1209，P3 正文：`頒獎典禮在下週日（11月22日）` → `在 本週日（11月22日）`
  7. L1958，P4 頭條：`下週日，封王遊行天母出發！` → `本週日，封王遊行天母出發！`
  8. L1970，P4 正文：`訂在下週日（11月22日）` → `訂在本週日（11月22日）`
  9. L2512，P4 圖注：`下週日，龍隊封王遊行從天母出發` → `本週日，龍隊封王遊行從天母出發`
  10. L4763，P7 讀者來信（編輯範例）：`「編輯好：下週日我要去看封王遊行，` → `「編輯好：本週日我要去看封王遊行，`
  11. L5526，P8 E 組情景題幹：`下週日` → `本週日`
- 另：意大利語 Note 中兩處 `domenica prossima, 22 nov.`（P1/P4 Note，英 core "next Sunday" 的忠實翻譯）**不是缺陷**：意大利語 "domenica prossima" 指即將到來的週日（11/22），且日期明寫，不生歧義。僅 P6 Note 寫 "Domenica 22 nov."，兩式並存但皆正確；若核心 fix1 改動英文 "next Sunday"，意大利語可同步去掉 "prossima" 以求一致（見觀察 O1）。
- 正確對照：P7 下期預告兩處「下週」（`下週：金馬獎得獎名單…下週見！`）指下週內容，用法正確，不動。
- 修復路徑：核心 fix1 修復後全繁體版重建帶上（本版不自行改源）。

## D2 —— 網頁 PDF abutting 缺口 9 處 > 0.5pt（新發現，僅網頁版）

- 方法：沿用 `scratch-webpdf-patch1/d2scan.py`（行內相鄰 span：印刷版貼合 <0.05pt 者，量網頁版同對缺口），掃描 1,274 對，**9 處網頁缺口 > 0.5pt，最差 2.33pt**。
- 9 處全為 Newsreader 數字串與中文之間的空隙（字重失配型，與 ru-en D2 同機制）：
  - P2（24pt）×2：`11｜包裹到了，先點收再拆` gap 2.26；`11｜點` gap 2.26
  - P5（24pt）×3：`11｜月` gap 2.26；`17｜日` gap 2.33；`11｜月繼` gap 2.26
  - P6（24pt）×2：`11｜月` gap 2.26；`22｜日，一天四件大事` gap 2.33
  - P7（16.12pt）×2：`11｜月` gap 1.58；`15｜日頒獎」` gap 1.48
- 证据：本版網頁 PDF 建於 2026-11-11 02:51 UTC，用的是**補丁前** `tools/webpdf.py`（`:style=Bold`/無字重查詢）；補丁（`fc_match` 改 `:weight=200`/`:weight=100`）於同日 08:33 UTC 合入；核心 `core-zh-tw` 網頁 PDF 於 08:47 UTC 用已補丁工具重建，同法掃描 **0 缺口**。印刷版 9 處全貼合（gap < 0.05pt），印刷 PDF 不受影響，文字層字符集印刷/網頁逐頁一致。
- 修复路徑：僅用現行已補丁 `tools/webpdf.py` 重建網頁 PDF（不碰內容源、不重渲印刷版）；預期缺口歸零。需重跑 d2scan 驗證。

## D3 —— 意大利語系詞 è 誤用 ×5（新發現，解釋層文法錯誤）

英語 "is/runs + 頻率/數量" 被直譯為意大利語 "è + 頻率/數量副詞"，標準意大利語中 essere 不能帶頻率/數量補語。5 處（頁／原文 → 應改／证据）：

1. P1 Note（text.md L165）：原文 `La parata diurna è tutti i giorni alle 14:00.` → 應改 `La parata diurna si tiene tutti i giorni alle 14:00.`（英 core： "The daytime parade runs daily at 14:00."）
2. P2 Note（L680）：原文 `Lo spettacolo di luci principale è tutti i giorni dalle 17:30 alle 23:00, ogni mezz'ora, 5 minuti ogni volta.` → 應改 `… si tiene tutti i giorni dalle 17:30 alle 23:00, …`（英 core： "runs every half hour … daily"）
3. P7 B2 釋義（L4569）：原文 `lo spettacolo principale è ogni mezz'ora.` → 應改 `lo spettacolo principale si ripete ogni mezz'ora.`
4. P7 易錯診所（L4731）：原文 `Lo spettacolo principale è ogni mezz'ora: 12 volte, dalle 17:30 alle 23:00.` → 應改 `Lo spettacolo principale si ripete ogni mezz'ora: 12 volte, dalle 17:30 alle 23:00.`
5. P8 答案鍵 70（L5876）：原文 `Il concerto di Natale è in tutto 4 spettacoli.` → 應改 `Il concerto di Natale prevede 4 spettacoli in tutto.`（主語單數＋複數補語，兼數不一致；英 core： "plays 4 shows in all."）
- 内部证据：同一版內同一概念已有正確寫法——鍵 22/110/135 `si ripete ogni mezz'ora`、鍵 122/146 `dura 5 minuti ogni volta`、P2 鍵 16 `dura dal 13 nov. al 27 dic.`。其餘 "è + 時間點"（如 `è alle 14:00`、`è il 22 nov.`、`è domenica 22 nov.`）皆正確，不在內。
- 修复：改 5 處意大利語字符串（`content12.py`/`content34.py`/`content7.py`/`content8.py` 相應 Note/釋義/鍵注），重建重校。注意：改動 P7 B2 釋義與診所 gloss 會動 P7 欄高，需重跑 occlusion（P7 欄 3 底距 footer 僅 18.7px 餘量）與 freeze。

## 已驗無問題（抽樣＋全量門禁）

- 中文正文：CJK 字符序列與核心全等，僅 D1 的 11 處＋預期翻譯（刊頭/頁腳 `Pagina N di 8`、H1、P1 詞卡釋義句改意大利語——de/fr/es/ja/ko/nl/pt/ru 八版同式，非本版獨有）。
- 數字／日期／算術：數字 token 多重集與核心全等（僅 H1 `VOL.4` 多一個 "4"）；抽驗算術全對：10×10=100、5×10=50、7×10=70＋30=100、14+31+3=48、11/6–22 含首尾 17 天、11/17–22 含首尾 6 天、17:00→18:30 為 1.5 小時、14:00→19:00 為 5 小時、17:30→23:00 每半小時共 12 場、1,200+800=2,000、2,000−1,200=800、11/13–12/27 共 45 天。
- P7 金句：8 句逐字摘自正文，逐句驗證為「正文頁 1 次＋P7 1 次」（`封王遊行從天母棒球場出發` P1、`夜間遊行晚上7點，最後一場不要錯過` P1、`小雪之後，天氣一天比一天冷` P2、`主燈秀每半小時一次，每次5分鐘` P2、`頒獎典禮晚上6點30分開始` P3、`保險箱裡，裝的是高雄的勞動記憶` P3、`穿上紅色衣服，一起上街為龍隊喝采` P4、`迪士尼聖誕，從11月17日開始` P5）。
- P8：150 題齊全（編號 1–150 無缺，題幹 150＋鍵注 150）；`p8.py extract` 150/150；`p8.py compare` vs core **CLEAN，keydiff=[]**（任務預期 E 組 [137,138,139,140] 未出現，鍵值與核心全同）；寫作範答 142 字與核心逐字一致；P8 最小字號印刷/網頁皆 9.75pt。
- 彎標點：U+201C/U+201D/U+2019 在 text.md 全文為 0，在 8 個 SVG 中亦為 0（與核心一致）；意大利語省音用直撇號 `'`（如 `l'inverno`、`d'acciaio`）。
- 意大利語層：全文 diff 逐行對英 core 校過——動詞變位、冠詞、介詞、前置詞縮合抽驗無誤；未縮合 `di il`/`a la`/`in gli` 等 27 式掃描 0 命中，縮合形 `del/al/dal/nel/della/nella/sullo` 俱全；`Vestitevi caldi` 屬副詞化形容詞用法（類 `vestiti pesante`），不列缺陷。
- 文字層：pdftotext 印刷 111,616 B／網頁 111,616 B，非空白字符多重集整體與逐頁皆一致（僅 P3 為分段噪聲）；text.md 每頁字符多重集與印刷 PDF 每頁全等（md-only=0；PDF 僅多刊頭 "Lucerna" 7 字符）。
- 幾何：`occlusion_audit.py` 自測通過＋本版 **0 flags**；`checks.py` PASS（8 金句各 2 次、簡體 0、P4 柱 90/450/900、P6 點位吻合）；`freeze.py baseline` **8/8 SVG 字節一致**；VOL.5 恰 1 次（P7 預告頭）、VOL.3 2 次（P7 披露中英各 1）、VOL.4 11 次。
- 目檢：渲染卡 P4、P7 逐欄看過，無溢出、重疊、頁腳碰撞；P4 `Parole del baseball` 折兩行在欄內（KIT 已記非缺陷）。

## 觀察（非缺陷，記下供協調員判斷）

- O1：`domenica prossima, 22 nov.`（P1/P4 Note）與 `Domenica 22 nov.`（P6 Note）並存，皆正確，僅一致性可議。
- O2：鍵 83 `il segnale più presto`／鍵 86 `l'ultimo segnale` 譯英 "marker"（時間軸標記）偏弱，可解但欠準；建議改 `il primo orario`／`l'ultimo orario`，非強制。
- O3：P4 欄頭 `La parata scudetto e i punti sport`——`punti sport` 勉強可解，標準寫法 `punti sportivi`。
- O4：P3 pdftotext 印刷/網頁字面差異僅為分段噪聲（字符集一致），與核心同類 artifact 一致。
- O5：本次校對中磁碟配額 EDQUOT 兩度發作（見 GATE-LOG 末段）：首次寫 diff 檔失敗、重探後恢復；收尾寫盤前重探失敗，60 秒後再探仍失敗，故 PROOF-NOTE.md 與 GATE-LOG.md 暫存 /tmp（見下方），未寫入 scratch 目錄；待配額恢復後請協調員或後續任務將兩檔移入 `hidden_files/w47/scratch-proof-zh-tw-it1/`。

## 寫入狀態（EDQUOT 備註）

- 本檔原定路徑：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-zh-tw-it1/PROOF-NOTE.md`
- 因磁碟配額（EDQUOT）收尾寫盤失敗，暫存：`/tmp/proof-it/PROOF-NOTE.md`（同目錄另有 `GATE-LOG.md`、`diff-core-it.txt`、`d2-scan.json`、`d2-scan-core.json`、print/web pdftotext）。
- 本次未改源、未重建、未 commit、未 push。源目錄只讀使用；freeze baseline 的重建在 /tmp 副本內完成，核對後未動原 SVG（freeze 自報 core integrity：8 檔未變）。
