# GATE-LOG — W47 core-zh-tw fix1：D1 修後全套機械門重跑記錄

- **復校對象**：`~/workspace/weekly-git/production/2026-w47/core-zh-tw/`（修後）
- **工具**：`~/workspace/weekly-git/tools/venv/bin/python`（共享工具，永不去 /tmp）
- **日誌目錄（絕對路徑）**：
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-zh-tw-core1/`
- **時間**：2026-11-11 09:0x–09:1x UTC

## 0. 探針與交付物（見 FIX-LOG §0、§5）

- `git hash-object -w` rc=0；筆記目錄寫盤 rc=0；df 46G 可用，無 EDQUOT。
- 改後 print `Lucerna-VOL4.pdf` 19,421,129 B / SHA `daa43834…19210`；
  web `Lucerna-VOL4-web.pdf` 2,324,807 B（< 7 MB）/ SHA `596defd7…34ac1f`；
  text.md 49,816 B / SHA `1dd4afab…8bc17`；雙 PDF 各 8 頁、1462.5×2025pt。

## 1. 構建門（build.log）

- `run.py` RC=0；`render.py` RC=0；`webpdf.py` RC=0；`export_zhtw_textmd.py` RC=0。
- 無 FLOW OVERFLOW、無 HEAD TOO WIDE 警告。
- Registry：TOTAL 150（A2 44 · B1 74 · B2 32；分頁 10/18/18/18/18/18/12/38）——與修前一致。

## 2. 文字層一致（print.txt / web.txt，pdftotext）

- print 46,224 B；web 46,225 B（均 > 0，有文字層）。
- 字符多重集差：print-only **0**；web-only **1** = 1 個換行（行界空白 artifact，
  與 KIT 記錄的同類 artifact 一致：web 僅多 1 空格＋1 換行，無缺字）。
- `本週日` print/web 各 11×；`下週日` print/web 各 0。
- **結論：文字層完整一致，PASS。**
- 操作註：首次 `pdftotext` 寫 print.txt 曾報 I/O Error（打不開輸出檔），
  未改任何參數直接重跑即 RC=0（46,224 B）；屬一次性異常，重跑已排除，非門失敗。

## 3. occlusion_audit.py（occlusion-selftest.log / occlusion.log / occlusion.json）

- `--selftest` rc=0：6 類皆觸發（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），乾淨對照沉默。
- 本版審計 rc=0：**0 flags**（`flag_count: 0`）。
- **結論：PASS。**

## 4. p8.py（p8-extract.log/.json / p8-compare.log/.json）

- `extract --p8 svg/p8-test.svg --total 150` rc=0：noted set = **150/150**。
- `compare`（新核心 P8 vs zh-tw-de 版 P8，鍵值須與修前一致）rc=0：
  **CLEAN**，missing=[] extra_count=0 uncertain=[] keydiff=[]。
  150 題鍵值與修前明文逐題一致（對照 proof1 附錄逐題表：Q144 = A 等全部相同；
  寫作題 150 = ✓）。修文未動任何題鍵。
- **結論：PASS。**

## 5. checks.py（checks.log）— rc=0 PASS

- 本週金句 8 句各 2 次（文章＋P7）。
- SIMP_ONLY_HITS []（無簡體字）。
- P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]——與預期一致。

## 6. freeze.py（freeze-base.log）

- `baseline --build . --core-svg svg --out <scratch>/freeze-base` rc=0：
  **8/8 SVGs byte-identical**（重建產物與已交 SVG 逐字節相同；core integrity：
  運行前後 8 個已交 SVG 哈希不變）。
- **結論：PASS。**（core 自身比對無需 diff；與 fan-out 的 diff 待重擴後由協調員驗。）

## 7. 彎撇／彎引號全掃（U+2019/U+201C/U+201D）

- SVG 8 頁＋text.md 全掃：**0 命中**。PASS。

## 8. P8 最小字號與 §1.1 顏色（PyMuPDF／grep 抽查）

- P8 最小字號：print 與 web 雙 PDF 皆 **9.75pt**（= §1.1 下限）。
- 紙色 #fbfaf6：8 頁各 1 處；金色系 hex（#b8860b/#d4af37/#c9a227/#8b4513）與 GOLD 常數：
  **0**（grep 命中的 "Gold" 皆為正文詞 "Golden Horse" 的一部分，非顏色）。
- **結論：PASS。**

## 9. 雙 PDF 逐版目視（cards/ 8 張渲染圖，P1–P8）

- **P1**：副題「封王遊行，本週日天母出發！」✓；正文「訂在本週日（11月22日）」✓；
  本週大事「本週日 11/22 遊行、金馬獎、鋼雕閉幕、小雪」✓。無溢出／重疊／壓頁腳。
- **P2**：小雪首段「本週日（11月22日）是小雪」✓。全版乾淨。
- **P3**：標題「金馬獎本週日頒獎，誰會得獎？」✓；正文「頒獎典禮在本週日（11月22日）舉行」✓。全版乾淨。
- **P4**：標題「本週日，封王遊行天母出發！」✓；正文「訂在本週日（11月22日）」✓；
  圖注「本週日，龍隊封王遊行從天母出發。」✓。全版乾淨。
- **P5**：無改動處，全版乾淨（跨欄續排等既有版式不變）。
- **P6**：無改動處，時間軸／圖表乾淨。
- **P7**：來信「編輯好：本週日我要去看封王遊行」✓；
  下期預告「下週：金馬獎得獎名單、封王遊行直擊、鋼雕閉幕現場……下週見！」**完整保留，未動**✓；
  預告條在頁腳線上方，全版乾淨。
- **P8**：E 144「—封王遊行哪天出發？—本週日___出發。(A. 11月22日 · B. 11月15日)」✓；
  鍵 144. A — The parade is Sunday, Nov 22 ✓。全版乾淨。
- **結論：8 版逐版目視全數通過，版式無可見變化。**

## 總結：全套機械門全綠

| 門 | 結果 |
|---|---|
| 構建（run/render/webpdf/export） | RC 皆 0，無 overflow 警告，150 題分布不變 |
| occlusion_audit.py（自檢先過） | 0 flags |
| p8.py extract --total 150 | 150/150 |
| p8.py compare（新核心 vs zh-tw-de） | CLEAN，keydiff=[] |
| freeze.py baseline | 8/8 byte-identical |
| checks.py | PASS（金句 8×2、簡體 0、圖表幾何一致） |
| print/web 文字層多重集差 | print-only 0（web 僅多 1 換行 artifact） |
| U+2019/U+201C/U+201D 全掃 | 0 |
| P8 最小字號（雙 PDF） | 9.75pt（= §1.1 下限） |
| §1.1 顏色 | 紙 #fbfaf6 ×8 頁；金／紅褐 0 |
| 雙 PDF 逐版目視 | 8/8 通過，11 處皆上版，「下週」預告保留 |

## 未做事項（按任務範圍）

- 未跑 insert.py、lint --write；未做任何 git 寫操作（`git status` 僅 scoped 唯讀查看，
  core-zh-tw/ 目錄目前未入 git 追蹤，屬 W47 生產中狀態）。
- 未碰 fan-out 各版、tools/、其他目標語。WEEKLY-KIT.md 未更新（舊 PDF 字節數／SHA 仍為修前值，
  見 FIX-LOG §5，待協調員／re-proof 後統一更新）。
- 下一步（協調員另派）：核心 re-proof＋全部繁體中文版重擴。
