# GATE-LOG — W47 zh-tw × de proof1（機械門獨立重跑記錄）

復校對象：`~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-de/`
核心對照：`~/workspace/weekly-git/production/2026-w47/core-zh-tw/`
工具：`~/workspace/weekly-git/tools/venv/bin/python`（共享工具，永不去 /tmp）
日誌目錄（絕對路徑）：
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-zh-tw-de1/`

## 0. 探針與交付物核驗（2026-11-11 08:29 UTC）

- `git hash-object -w`（echo test）：rc=0，`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`
- 筆記目錄真實寫盤 `probe-write.txt`：rc=0
- df：/home/hatch 150G 總／105G 已用／45G 可用；無 EDQUOT
- 交付物 SHA（復校前＝復校後，未改動）：
  - print `Lucerna-VOL4-DE.pdf` 21,717,574 B
    SHA-256 `28af6ac44b607d5a2e7518e45a422ae23859fe10bc0142ba6c81f0dc9edaa77c`
  - web `Lucerna-VOL4-DE-web.pdf` 2,436,311 B（< 7 MB）
    SHA-256 `18f1ed9d6f978b5c5e29eb080498dbc9c4b5120e2c4e899fc1e288c2894619f8`
  - text `2026-w47-zh-tw-de.text.md` 51,842 B
    SHA-256 `6a3c4ae7df0d0f95e37c758d640c0bbf449eea6e6a563fd6f55510cd4792631e`
  - 三者皆與任務所給一致；雙 PDF 各 8 頁、1462.5×2025pt
- 日期核驗：`TZ=Asia/Taipei date -d 2026-11-16` = Monday；`2026-11-22` = Sunday

## 1. 文字層一致（pdftotext，見 print.txt / web.txt）

- print 48,180 B；web 48,182 B
- 字符多重集差：print-only 0；web-only 2 字符 = 1 空格＋1 換行（行界空白 artifact，
  另有一處「香港」分行讀取順序差異，無缺字）
- 結論：文字層完整一致

## 2. occlusion_audit.py（occlusion.log / occlusion.json）

- `--selftest` rc=0：6 類皆觸發（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），
  乾淨對照沉默
- 本版審計 rc=0：**0 flags**

## 3. p8.py（p8-extract.log / p8-compare.log / p8-keys-edition.json / p8-compare.json）

- `extract --p8 svg/p8-test.svg --total 150` rc=0：noted set = **150/150**
- `compare --core-p8 core-zh-tw/svg/p8-test.svg --edition-p8 … --total 150` rc=0：
  **CLEAN**，missing=[] extra_count=0 uncertain=[] keydiff=[]
- 150 題鍵值與 core-zh-tw 逐題一致

## 4. checks.py（checks.log）— rc=0 PASS

- 金句 8 句各 2 次（文章＋P7）
- SIMP_ONLY_HITS []
- P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]
- （註：首次誤把 python 二進制當腳本傳入，rc=1 為調用錯誤而非門失敗；正確重跑 rc=0）

## 5. freeze.py

- `baseline --build <edition> --core-svg <edition>/svg --out <scratch>/freeze-base`
  （freeze-base.log）：rc=0，**8/8 SVGs byte-identical**；
  shipped SVG 重建前後哈希不變（core integrity 通過）
- `diff --core-svg core-zh-tw/svg --edition-svg <edition>/svg --strict-cjk`
  （freeze-diff.log / freeze-diff.json）：**rc=1**，TOTAL added CJK = 9，
  全部為字符「德」，逐一核實皆在家具「繁體中文正文　德語講解」
  （8 頁頁腳＋P1 徽章行），即核心「英語講解」的對應家具；
  其餘新增字符串中文部分與核心逐字相同，僅英文 gloss 換德語；
  P7 斷行碎片合併後字符集與核心一致。裁定：非目標語新增，不構成缺陷。
  （freeze-base/build-copy 為可復現中間件，已刪，只留日誌；目錄現 2.1MB）

## 6. §1.1 實測

- 紙 #fbfaf6 ×8 頁；金色系值 #c9a227/#d4af37/#8b4513 皆 0；
  「gold」字串 9 命中皆為事件名 Golden Horse 或 base64 巧合，無金色着色
- 徽章色 A2 #5c6e30 / B1 #46581f / B2 #37402f 齊全；P8 徽章 38/38（A2 8 · B1 20 · B2 10）
- VOL.4 ×10；VOL.5 ×1（僅 P7 下期預告）；VOL.3 ×2（僅 P7 延期披露）
- P8 最小字號 PyMuPDF：print 與 web 皆 **9.75pt**（= §1.1 下限）
- 頁行家具「Seite N von 8」×8（與 W46 已發 zh-tw-de 版一致）
- 寫作範文實測 142 字（120–180 字帶內），與 P8 鍵 150 注一致

## 7. 語言純度掃描

- 彎撇 U+2019／彎引號 U+201C/U+201D：SVG 8 頁＋text.md 全掃 **0**
- 英文泄漏：與核心相同的含 ≥3 拉丁詞文本節點 **0**；
  英文功能詞命中僅作品名（The Awakening of the Wendigo、A Trip to the Moon）、
  人名 Will Or、德語 also、text.md 固定英文頁標題——皆非泄漏
- SIMP_ONLY_HITS []（見 §4）

## 8. 目視

- cards/ 8 張渲染圖逐版目視：P1–P8 皆乾淨，無溢出／重疊／壓頁腳；
  P7 預告條終點 2589.8（頁腳線 2596，上方 6.2px）；P6 時間軸標籤相鄰不重疊；
  P8 D 頭合欄、150 鍵齊全、鍵末距頁腳線充足
- 6 張照片出處皆在（P2/P3/P4/P5/P7/P8）

## 9. 未執行的項（按任務）

- 未跑 insert.py、lint --write；未做任何 git 寫操作（add/commit/push/reset/stash 皆無）
- 未改任何源碼／成品；三件交付物 SHA 復校前後一致（見 §0）
- 未派 subagent（葉子）
