# FIX-LOG — W47 core-zh-tw fix1：D1「下週日」→「本週日」（只修 D1 一條）

- **任務**：core-zh-tw fix1（葉子，不派 subagent）
- **復校對象**：`production/2026-w47/core-zh-tw/`（印刷 `Lucerna-VOL4.pdf`，讀者 en）
- **復校依據**：`scratch-proof-zh-tw-de1/PROOF-NOTE.md`（proof1，D1：11 處，主要）
- **先讀**：SOP.md §8、§1.1 全文；`~/workspace/weekly-git/AGENTS.md`；
  `hidden_files/w47/briefs/brief-coordinator.md`
- **工作時間**：2026-11-11 08:41–09:2x UTC（任務時間 03:41 EST）
- **筆記目錄**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-zh-tw-core1/`
- **只改**：`production/2026-w47/core-zh-tw/`（4 個內容源文件＋重渲產物 svg/cards/雙 PDF/text.md）
  與本筆記目錄。**未碰** fan-out 各版、tools/、insert.py、lint --write、任何 git 寫操作。

## 0. 探針與日期核實（動手前）

- `git hash-object -w`（echo test）：rc=0，`da0c4eb8d9a48d171a33574b380752e183286751`
- 筆記目錄真實寫盤 `.probe`：rc=0
- df：/home/hatch 150G 總／105G 已用／**46G 可用**；無 EDQUOT（全程未遇配額問題）
- `date`（Asia/Taipei）：**2026-11-16 週一、11-22 週日、11-29 週日**——
  刊期 11/16（週一）–11/22（週日），11/22 是**本週日**；「下週日」按標準用法是 11/29。
  P7 下期預告的「下週」指 11/23–29 那一週，與「下週日 = 11/22」自相矛盾——D1 屬實。

## 1. 盤上核實（改前逐字核對，全部屬實）

- core `2026-w47-zh-tw-en.text.md`：`下週日` **11×**（行 53、61、259、462、1165、1207、1954、1966、2506、4749、5510）
- zh-tw-de `2026-w47-zh-tw-de.text.md`：`下週日` **11×**（未碰，待重擴）
- 核心源文件共 11 處，分布：content12.py 4、content34.py 5、content7.py 1、content8.py 1；
  content56.py 0 處。**11 處上下文逐一核對，全部確指 11 月 22 日，無一處指 11/29**——
  8 處直接附（11月22日）或 11/22；P1 副題、P3/P4 標題、P4 圖注、P7 來信、P8 Q144
  所指事件（封王遊行／金馬獎頒獎）皆為 11/22 的活動，Q144 選項 A 即 11月22日。
  故 11 處全改，無保留。

## 2. 11 處修法（`下週日` → `本週日`，逐字，3 字對 3 字）

| # | 源文件:行 | 頁面／位置 | 原文（節錄） | 改後 |
|---|---|---|---|---|
| 1 | content12.py:33 | P1 副題（deck） | 封王遊行，下週日天母出發！ | 封王遊行，本週日天母出發！ |
| 2 | content12.py:35 | P1 頭條正文 | 封王遊行訂在下週日（11月22日）下午2點 | 封王遊行訂在本週日（11月22日）下午2點 |
| 3 | content12.py:68 | P1 本週大事欄 | 下週日 11/22 遊行、金馬獎、鋼雕閉幕、小雪 | 本週日 11/22 遊行、金馬獎、鋼雕閉幕、小雪 |
| 4 | content12.py:111 | P2 小雪首段 | 下週日（11月22日）是小雪 | 本週日（11月22日）是小雪 |
| 5 | content34.py:17 | P3 頭條標題 | 金馬獎下週日頒獎，誰會得獎？ | 金馬獎本週日頒獎，誰會得獎？ |
| 6 | content34.py:18 | P3 金馬獎正文 | 頒獎典禮在下週日（11月22日）舉行 | 頒獎典禮在本週日（11月22日）舉行 |
| 7 | content34.py:123 | P4 頭條標題 | 下週日，封王遊行天母出發！ | 本週日，封王遊行天母出發！ |
| 8 | content34.py:125 | P4 正文 | 封王遊行訂在下週日（11月22日）下午2點 | 封王遊行訂在本週日（11月22日）下午2點 |
| 9 | content34.py:196 | P4 照片圖注 | 下週日，龍隊封王遊行從天母出發。 | 本週日，龍隊封王遊行從天母出發。 |
| 10 | content7.py:99 | P7 讀者園地來信 | 「編輯好：下週日我要去看封王遊行……」 | 「編輯好：本週日我要去看封王遊行……」 |
| 11 | content8.py:86 | P8 E 144 題對話 | —封王遊行哪天出發？—下週日___出發。(A. 11月22日 · B. 11月15日) | —封王遊行哪天出發？—本週日___出發。(A. 11月22日 · B. 11月15日) |

- 改後核查：源文件 `下週日` 殘留 **0**；`本週日` content12.py 4、content34.py 5、content7.py 1、content8.py 1，合計 11。
- **未動**：content7.py:141 P7 下期預告「下週：金馬獎得獎名單……下週見！」（指 11/23–29 週，正確）；
  content56.py 無改動；其餘全部內容未碰。

## 3. 刻意未動（記錄在案，非遺漏）

- `WEEKLY-KIT.md:88` 仍含「下週日11月22日」——那是**逐字引用 W46 KIT 的 VOL.4 預告原文**
  （歷史引文，說明 W46 承諾本期兌現），不是本期正文；改它等於篡改歷史記錄，故不動。
- 英文講解層 `Notes | ... set for next Sunday (Nov 22)`（P1/P4 等）未動：D1 只指中文「下週日」；
  英文 "next Sunday" 自週一 11/16 起指下一個到來的週日即 11/22，語義無誤（proof1 對德語
  "nächsten Sonntag" 同理裁定無問題）。如協調員另有裁定，請再派。
- fan-out 各版（含 zh-tw-de）未碰——待協調員另派全繁體版重擴。

## 4. 重渲染（run → render → webpdf → text.md，見 build.log）

- `tools/venv/bin/python run.py` RC=0；registry TOTAL 150（A2 44 · B1 74 · B2 32；
  分頁 P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38）——與修前一致。
- `render.py` RC=0；`tools/webpdf.py svg Lucerna-VOL4-web.pdf` RC=0（46,225 文字字節）；
  `export_zhtw_textmd.py svg 2026-w47-zh-tw-en.text.md "Lucerna Weekly — Traditional Chinese, English explanations"` RC=0。
- 構建 log 無 FLOW OVERFLOW、無 HEAD TOO WIDE 警告。

## 5. 改前／改後交付物（新雙 PDF 字節數／SHA）

| 交付物 | 改前（修前實測，與 KIT 一致） | 改後 |
|---|---|---|
| print `Lucerna-VOL4.pdf` | 19,420,492 B，SHA-256 `f2764750d3872fc07adc034ef3c1e80cad60d543067f6a96a710b16bd8f89fba` | **19,421,129 B**，SHA-256 `daa438344c73bf6be8e71557d2062ef82536579a0b5163d8e9b8fc543b219210` |
| web `Lucerna-VOL4-web.pdf` | 2,307,484 B（< 7 MB），SHA-256 `9191ef790de862fd1defc7e51ea661e8de71b1438e1d55068a393eb211dc54a2` | **2,324,807 B**（< 7 MB），SHA-256 `596defd7d42870cd94178846e750ba0d22df5bd093874356452dab3c2134ac1f` |
| text `2026-w47-zh-tw-en.text.md` | 49,816 B，SHA-256 `4a99110975bb0c4b684de82a8a9ed7fa11bddb59562bb75398327cb4446207a5` | **49,816 B**（字節數不變：下→本同為 3 字／9 字節），SHA-256 `1dd4afab886a7b62d0d580336db4e35b55227e6a766a325169f529647bf8bc17` |
| 頁數／版面 | 雙 PDF 各 8 頁、1462.5×2025pt | 雙 PDF 各 8 頁、1462.5×2025pt（不變） |

- 改後全文核查：SVG 合計 `本週日` 11×（P1 3、P2 1、P3 2、P4 3、P7 1、P8 1；P5/P6 0）、
  `下週日` **0**；text.md `本週日` 11×、`下週日` 0；雙 PDF pdftotext `本週日` 各 11×、`下週日` 0。
- web PDF 字節數變化（2,307,484 → 2,324,807）屬 webpdf 已知特性：字體子集隨機標籤致兩次運行
  字節不相同，只看內容一致性（見 GATE-LOG 文字層門：print-only 0 缺字）。
- **未改 KIT**：`WEEKLY-KIT.md` 內舊 PDF 字節數／SHA 仍為修前值。按任務範圍（只修 D1、
  不碰其他內容），KIT 由協調員／re-proof 後統一更新；此處如實記錄，不擅自改 KIT。

## 6. 目視確認（cards/ 8 張逐版，見 GATE-LOG 第 6 節）

P1 三處、P2 一處、P3 兩處、P4 三處、P7 來信一處、P8 Q144 一處皆已上版為「本週日」；
P7 下期預告「下週」完整保留；8 版皆無溢出、無重疊、無壓頁腳，版式無可見變化。
