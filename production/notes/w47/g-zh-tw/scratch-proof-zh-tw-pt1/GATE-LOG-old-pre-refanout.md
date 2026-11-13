# GATE-LOG — 2026-W47 zh-tw-pt proof1（門禁命令與 RC）

原定路徑 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-zh-tw-pt1/GATE-LOG.md`
因 `Disk quota exceeded (os error 122)` 無法寫入；本件為 /tmp 保底副本。探針 `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin`
開工與每次寫盤前均重探，皆成功（`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`）。

| 門禁 | 命令 | RC | 結果 |
|---|---|---|---|
| 探針 | `echo test \| git -C ~/workspace/weekly-git hash-object -w --stdin` + 寫 `scratch-proof-zh-tw-pt1/probe.txt` | 0 | 通過（probe.txt 已寫入，應為唯一成功寫盤） |
| SHA 印刷 PDF | `sha256sum Lucerna-VOL4-PT.pdf` | 0 | `3673d36cb0890418…` 吻合；20,944,927 B |
| SHA 網頁 PDF | `sha256sum Lucerna-VOL4-PT-web.pdf` | 0 | `da2dd497b7fca416…` 吻合；2,396,718 B |
| pdfinfo 兩版 | `pdfinfo Lucerna-VOL4-PT.pdf` / `...-web.pdf` | 0 | 各 8 頁，1462.5×2025 pt |
| 文本層 print/web | `pdftotext`（無 -layout）兩版 + multiset 比對 | 0 | print 47,945 B / web 47,948 B；差僅 web 多 3 個換行符 |
| 逐頁 CJK 比對 | pdftotext 分頁 vs text.md 分節（Counter） | 0 | 8 頁漢字全同；拉丁詞每頁僅差 1 個 Lucerna（刊頭）；數字 8 頁全同 |
| 中文層 vs 核心 | CJK 全序列比對（core-zh-tw text.md） | 0 | 僅「下週日×11 ↔ 本週日×11」不同，其餘差異皆為解說層語言（英→葡）與頁碼家具 |
| 下週日計數 | `grep -o 下週日` text.md / print PDF / web PDF / svg/*.svg | 0 | 四處皆 11；本週日 0；11月29日 0 |
| 日期核實 | `TZ=America/Toronto date -d` 2026-11-15/16/17/19/21/22/24/29, 2026-12-27, 2027-01-03 | 0 | 11/22 週日、11/29 週日；刊期 11/16（一）–11/22（日） |
| occlusion | `tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-zh-tw-pt/svg --json /tmp/occl-pt.json` | 0 | 自測通過；終輪 0 flags |
| p8 extract | `tools/p8.py extract --p8 .../svg/p8-test.svg --total 150 --json /tmp/p8-pt-extract.json` | 0 | noted set = 150 of 150 |
| p8 compare | `tools/p8.py compare --core-p8 core-zh-tw/svg/p8-test.svg --edition-p8 .../svg/p8-test.svg --total 150 --json /tmp/p8-pt-compare.json` | 0 | CLEAN，missing=[] extra_count=0 keydiff=[]（任務預期的 keydiff [137,138,139,140] 未出現） |
| checks.py | `tools/venv/bin/python checks.py`（於版目錄） | 0 | CHECKS PASS（金句各 2 次、SIMP_ONLY_HITS []、P4 柱、P6 點位） |
| freeze | `tools/freeze.py baseline --build .../2026-w47-zh-tw-pt --core-svg .../svg --out /tmp/freeze-pt-out` | 0 | 8/8 SVG 字節一致；核心 SVG 重建前後未變 |
| 答案鍵比對 | text.md P8 答案區 150 鍵逐值比對（core vs pt） | 0 | 150/150 相同，無缺失 |
| 彎標點 | Python：U+201C/201D/2018/2019 計數於 text.md、8 SVG `<text>`、content*.py | 0 | 四處皆 0 |
| 葡語縮合/重音 | Python：`de o/em o/de a/em a/por o/com o`、無重音詞、`às + 時刻` 掃描 | 0 | 未縮合 0；重音缺失 0；às+時刻 39 處 |
| abutting 掃描 | PyMuPDF rawdict span 內相鄰字符間隙（print + web 兩版） | 0 | print 24,972 對，>0.5pt 130 對（皆為 P1 字距/標點間距，裁決非缺陷）；web 24,973 對，同分佈 |
| P8 字號 | PyMuPDF：P8 span size 最小值（兩版） | 0 | 9.75pt（SOP §1.1 下限） |
| F 範文 | 字符計數 | 0 | 142 字（120–180 帶內） |
| 級別/題數 | text.md 計數 | 0 | 150 題；A2 44／B1 74／B2 32；頁 10/18/18/18/18/18/12/38 |
| 渲染卡目檢 | 8 張 cards/*.png 縮圖逐頁目視 | — | 無溢出/重疊/頁腳碰撞 |
| 公開來源核實 | browser.search：味全龍遊行（TSNA/體育局）、BABYMONSTER 台北場 | — | 遊行 11/22 14:00 天母→大巨蛋松菸大道屬實；BABYMONSTER 11/21–22 台北小巨蛋屬實 |
| 寫盤 PROOF-NOTE.md | `muse.write` 至 scratch-proof-zh-tw-pt1/PROOF-NOTE.md | **122 EDQUOT** | **失敗：Disk quota exceeded；已停手，改寫 /tmp 保底副本** |
| 寫盤 GATE-LOG.md | 同路徑 | — | 未嘗試原路徑（配額已爆）；僅 /tmp 副本 |
