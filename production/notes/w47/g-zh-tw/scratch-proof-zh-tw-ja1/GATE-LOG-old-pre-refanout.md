# GATE-LOG — W47 zh-tw-ja proof1 機械門

- 復校對象：`production/2026-w47/2026-w47-zh-tw-ja/`，Lucerna-VOL4-JA.pdf / Lucerna-VOL4-JA-web.pdf / 2026-w47-zh-tw-ja.text.md
- 探針：2026-11-11 09:21 UTC `git hash-object -w` OK + 探針文件寫入 OK；寫筆記前 09:31 UTC 再探 OK。

## SHA 核對（開工時盤上實測，與任務書一致）

| 文件 | 字節 | SHA-256 | 結果 |
|---|---|---|---|
| Lucerna-VOL4-JA.pdf | 18,090,244 | 35fb9b00d5e9c33f4d1ef9fdcecaff5f83b3139e264b39182a420f2fb90b3d95 | 一致 |
| Lucerna-VOL4-JA-web.pdf | 2,548,035 | 5c3be54673d3e1d65b14df730b48a1de908ca30d6a354ea651cd1811dc9f912f | 一致 |
| 2026-w47-zh-tw-ja.text.md | 53,739 | 47162db4c1020a498e429df6336dbc3f7d83137a0ecfbb8d0ac0832f31b08918 | 一致 |

## 機械門結果

| 門 | 命令 / 方法 | 結果 | 日誌 |
|---|---|---|---|
| occlusion 審計 | `tools/venv/bin/python tools/occlusion_audit.py <edition>/svg` | 自檢通過，**0 flags** | occlusion.log |
| p8 extract | `tools/p8.py extract --p8 svg/p8-test.svg --total 150` | **150/150** | p8-extract.log |
| p8 compare | `tools/p8.py compare --core-p8 core-zh-tw/svg/p8-test.svg --edition-p8 svg/p8-test.svg --total 150` | **CLEAN**（missing=[] extra_count=0 keydiff=[]） | p8-compare.log |
| freeze baseline | `tools/freeze.py baseline --build <edition> --core-svg <edition>/svg --out freeze-out` | **8/8 SVG 字節一致**；shipped SVG 完整性 OK | freeze.log |
| freeze diff | `tools/freeze.py diff --core-svg core-zh-tw/svg --edition-svg <edition>/svg --strict-cjk` | FAIL（預期內：新增 CJK 5767 字皆為日語講解層）；人工分類見 PROOF-NOTE | freeze-diff.log / freeze-diff.json |
| 印/網文字層比對 | pdftotext print/web + 逐頁 multiset 比對 | print 50,198 B / web 50,200 B；逐頁差 0，唯 P3 web 多 1 空格（空白假影） | print.txt / web.txt |
| P8 最小字號 | PyMuPDF 讀兩份 PDF 全部 span | 印/網 P8 最小皆 **9.75pt**（§1.1 下限）；全頁最小亦 9.75pt | （本文件內記錄） |
| 彎引號全掃 | U+201C/U+201D/U+2019 掃 SVG + text.md + ABSTRACT.txt | **0 / 0 / 0** | （本文件內記錄） |
| checks.py |  edition 內 `checks.py` | 短語 8×2 ✓；圖表 P4 [90.0, 450.0, 900.0]、P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43] ✓；`SIMP_ONLY_HITS ['国', '学']` 親驗為日語誤報（見 PROOF-NOTE）；總評 CHECKS FAIL 僅由此行引起 | checks.log |
| 日期/星期 | `date -d`（Asia/Taipei） | 11-16 週一 … 11-22 週日；11-13 週五、12-27 週日 | （本文件內記錄） |
| VOL 計數 | SVG 內 grep | VOL.4 ×10、VOL.5 ×1（正確）、VOL.3 ×2（正確）、VOL.2 ×0 | （本文件內記錄） |
| 「·」計數 | SVG 文本節點分類 | 59 處：P8 選項分隔 42、P6 圖例 4、P5 人名中點 12、P8 獨立 1 | （本文件內記錄） |
| 漢字字形 | TC 字形掃日語 prose / JP 新字體掃繁體正文 | 皆 0 處混用 | （本文件內記錄） |
| 英文殘留 | freeze-diff 新增含拉丁字母串分類 | 140 條皆為日語/專名/代碼，無英文 prose | （本文件內記錄） |
| 8 版看圖 | cards/ PNG 全 8 頁目視（另 web P1/P8 渲染對照） | 無溢出/重疊/壓頁腳；web 渲染與印刷一致，無豆腐塊 | /tmp/ja1view（臨時縮圖，已棄） |
| 作文範文 | content8.py MODELO 計數 | **142 字**（120–180 帶內） | （本文件內記錄） |

## 結論

機械門除 freeze-diff --strict-cjk（fan-out 預期 FAIL，已人工分類）與 checks.py SIMP_ONLY 誤報行外全部通過。
內容結論見 PROOF-NOTE.md：(b) 缺陷清單 3 條（D1 已知繼承·中 + D-ja-1/D-ja-2 新發現·低，皆機制層）。
