# GATE-LOG — W47 zh-tw-fr proof1 機械門獨立重跑記錄

復校對象：`production/2026-w47/2026-w47-zh-tw-fr/`（print SHA beeebce2531fcadd…／web SHA 61537f8dde6b5c04…／text SHA 415890f41a152310…，見 PROOF-NOTE.md）。
工具：`~/workspace/weekly-git/tools/venv/bin/python`；輸出在 `work/`（freeze baseline 副本已刪，只留日誌）。
探針：2026-11-11 08:31 UTC，git hash-object -w rc=0，筆記目錄寫盤 rc=0；08:32 一次瞬時 EDQUOT（mkdir work 失敗），停手後重試一次成功，其後正常。

## 1. 成品指紋（開工實測）
- print `Lucerna-VOL4-FR.pdf` 20,191,919 B，SHA-256 beeebce2531fcadd076f3999d8965ee425df76efe47c1e8f1584365fe74930b3，8 頁，1462.5×2025 pt ✓
- web `Lucerna-VOL4-FR-web.pdf` 2,350,191 B，SHA-256 61537f8dde6b5c04b63adebdd5835275d41108588c426688a0bf1cc4c1ce04df，8 頁 ✓
- text.md 52,507 B，SHA-256 415890f41a1523105ccd68fbfaba0d01d922dfeed78774d285efd3f51906301e ✓

## 2. 文字層一致（pdftotext）
- print 48,864 B；web 48,866 B；字符多重集差 = 2（web 多 1 換行＋1 空格），print-only 為空 → 無字符缺失 ✓
- 兩版皆 8 頁；P8 最小字號 print/web 皆 9.75pt（PyMuPDF 實測，§1.1 下限）✓
- VOL 計數（兩版一致）：VOL.4 ×9、VOL.5 ×1（P7 預告頭）、VOL.3 ×2（P7 披露）、VOL.2 ×0 ✓

## 3. occlusion_audit.py（tools/occlusion_audit.py svg/）
- rc=0；selftest OK（6 類 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 全觸發，清潔對照靜默）；**0 flags** ✓
- 日誌：`work/occlusion.log`、`work/occlusion.json`

## 4. p8.py
- extract `--p8 svg/p8-test.svg --total 150`：noted set = 150/150（1–150 連續）✓
- compare vs `core-zh-tw/svg/p8-test.svg`：**CLEAN**，missing=[] extra_count=0 keydiff=[] ✓
- 日誌：`work/p8-extract.log`、`work/p8-extract.json`、`work/p8-compare.log`、`work/p8-compare.json`

## 5. freeze.py
- baseline `--build <本版> --core-svg <本版>/svg`：rc=0，**8/8 SVG 字節一致**（副本重跑；shipped core SVG 前後哈希不變）✓
  日誌：`work/freeze-base.log`
- diff `--core-svg core-zh-tw/svg --edition-svg <本版>/svg --strict-cjk`：**rc=1**，TOTAL added CJK = 9（「法」：P1 ×2，其餘每頁 ×1）。
  逐字定位：新增「法」全在家具「法語講解」（P1 徽章行 1＋頁腳每頁 1）；正文 CJK 無新增。
  對照：同法跑 zh-tw-de 亦 rc=1（「德」×9）。裁定：工具對 fan-out 家具的結構性誤報，**非缺陷**（詳見 PROOF-NOTE.md）。
  日誌：`work/freeze-diff.log`、`work/freeze-diff.json`、`work/freeze-diff-de.log`

## 6. checks.py（本版 checks.py）
- rc=0，**CHECKS PASS**：8 句金句短語各出現恰好 2 次；SIMP_ONLY_HITS []；P4 長條 [90.0, 450.0, 900.0]；P6 圓點 cx [188.0, 695.21, 948.82, 1033.36, 1202.43] ✓

## 7. 彎標點全掃（U+2019 / U+201C / U+201D）
- 8 個 SVG＋text.md＋ABSTRACT.txt：**全部 0** ✓

## 8. 英文殘留掃描（獨立）
- 版內拉丁字母串 463 條；新於核心的 442 條逐條過英文詞表，僅 3 條命中且皆為正當專名：Will Or（人名）、The Awakening of the Wendigo（秀名）、"présentée par Will"（同人名）。**英文 prose 殘留 0** ✓
- 日誌：`work/leak-scan.log`

## 9. text.md
- H1：`# VOL.4 · Textes en chinois traditionnel · Explications en français` ✓
- 8 頁節（Page 1–8）齊全；題號 1–150 齊全（150 以「150.」行出現在 5704 行，答案區 6092 行）✓；無 ASCII 雙引號 ✓

## 10. ABSTRACT.txt
- 單行、無 ASCII 雙引號、410 字符、含 A2/B2/150、法語寫本期真實主題 ✓

## 11. 雙 PDF 目視
- 印刷 cards P1–P8 逐版目視：無溢出/重疊/壓頁腳 ✓
- 網頁版 pdftoppm 72dpi 渲染 P1–P8 逐版目視：與印刷版一致，無豆腐塊 ✓（渲染 PNG 已刪，可復現：`pdftoppm -png -r 72 Lucerna-VOL4-FR-web.pdf webp`）

## 12. 150 題逐題驗算
- 題號連續 1–150；分佈 P1 10／P2 18／P3 18／P4 18／P5 18／P6 18／P7 12／P8 38；A2 44／B1 74／B2 32 ✓
- 全部鍵值對題面＋原文＋圖表重算：**0 不符**；F 範文實測 142 字（120–180 帶內）✓

## 13. 日期/星期（date 實測）
- 11-16 週一、11-17 週二、11-19 週四、11-21 週六、11-22 週日；11-13 週五、12-27 週日 ✓

## 14. 事實網搜抽查（2026-11-11）
- 全部屬實：金馬獎 63（11-22 週日、北流、17:00/18:30、柯煒林、587 部、《狂忘警探》11 項）、味全龍第 6 冠＋遊行＋感謝祭＋U-Sport 267 間 5→10 幣、六福村墓碑鎮 10 週年（9-12..11-22、5 米鹿魔、19:00／14:00 週二休）、鋼雕藝術節（10-23..11-22、SUPER STAGE/SUPER SAFE、林洪玉秀 85 歲《萬年吉祥花》）、耶誕城（11-13..12-27＝45 天、卡娜赫拉、17:30–23:00 每半小時、德國市集 12-04..06）、迪士尼聖誕（11-17..1-3＝48 天、首個冬日市集、日間演出 11-19 起、音樂會 4 場）、爵士音樂節（第 8 屆、11-13..15/17..22/24、Krall 11-13／Wong×何卓彥 11-15／Kent 11-17 兩場／Kenny G 11-24）、BABYMONSTER 11-21..22 小巨蛋、圓方 SOCIAL WORKOUT 11-13..15 ✓

## 缺陷匯總（見 PROOF-NOTE.md）
- D1（中）：「下週日」指 11 月 22 日，全版 11 處；11 月 22 日為本刊期內週日，應為「本週日」；另 P1/P4 法語 Notes 兩處 "dimanche prochain, 22 nov." 同錯。
- D2（低）：P7 B1 Astuce mémoire 法語稱星光大道為 "le lieu" 且順序倒置。
- 其餘門禁全綠；本輪結論：(b) 缺陷清單 2 條。
