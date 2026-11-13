# GATE-LOG — 2026-W47 it-zh-tw proof1

- 復校對象：`~/workspace/weekly-git/production/2026-w47/2026-w47-it-zh-tw/`
- 對照 core：`~/workspace/weekly-git/production/2026-w47/core-it/`（盤上 fix3，commit 36bdec2e）
- Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-it-zh-tw1/`
- TMPDIR：goals 側 scratch 下的 `tmp/`（/tmp 512M 曾滿，不用 /tmp）
- 探針：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0；goals 側寫 `probe.txt` 成功（`probe-ok`）。

## 0. SHA 核對（開工前）

```
$ cd ~/workspace/weekly-git/production/2026-w47/2026-w47-it-zh-tw
$ sha256sum La-Lucerna-VOL4-ZH-TW.pdf La-Lucerna-VOL4-ZH-TW-web.pdf 2026-w47-it-zh-tw.text.md
6171fea645bd67e0c06d77934229c727b71465aec3fc3f42a82a41ab1933e9f0  La-Lucerna-VOL4-ZH-TW.pdf
57e29e6ff725a3c093e4d1a51f9d2c0113aeff8c8481e62c27752da0e43fce16  La-Lucerna-VOL4-ZH-TW-web.pdf
53c3ca77e2a365ed7aa4ec804db8cf9cc7029eb9fbb622f5bbff771e3dc438d3  2026-w47-it-zh-tw.text.md
```
三件與任務所給一致。大小：27,779,760 B / 2,042,022 B / 52,568 B。兩 PDF 均 8 頁、1462.5×2025 pt。

## 1. occlusion audit

```
$ cd ~/workspace/weekly-git/tools
$ ./venv/bin/python occlusion_audit.py <edition>/svg > $S/occlusion.log 2>&1   # rc=0
selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
/home/hatch/workspace/weekly-git/production/2026-w47/2026-w47-it-zh-tw/svg: 0 flags
```
結果：**0 flags**，selftest 正常。註：`--selftest` 單獨跑只出 selftest 行，須不帶該旗再跑一次才出 edition 結果（兩次均已存 `occlusion.log`，以後者為準）。

## 2. p8 extract / compare

```
$ ./venv/bin/python p8.py extract --p8 <edition>/svg/p8-valutazione.svg --total 150 --json $S/p8-extract-zh-tw.json
  noted set = 150 of 150 (parse: lines)
$ ./venv/bin/python p8.py extract --p8 <core>/svg/p8-valutazione.svg --total 150 --json $S/p8-extract-core.json
  noted set = 150 of 150 (parse: lines)
$ ./venv/bin/python p8.py compare --core-p8 <core>/svg/p8-valutazione.svg --edition-p8 <edition>/svg/p8-valutazione.svg --total 150 --json $S/p8-compare.json
  status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139]
```
結果：**CLEAN**，keydiff 恰為 [137, 138, 139]；Q140 鍵為義大利語句、兩邊相同、無 diff（正確行為）。另：RISPOSTE 1–150 與 P8 印刷鍵逐項程序比對 0 差異（僅 #150 記法差異：P8 `✓` vs text.md `✓ 範文見本版 H 區（99 詞）`，同義）；正文行內鍵 138 題與 P8 一致，其餘 12 題為匹配題組頭（25–28、52–55、141–144），已人工語義核對。

## 3. freeze baseline（重跑當前 core 構建）

```
$ ./venv/bin/python freeze.py baseline --build <core> --core-svg <core>/svg --out $S/freeze-base
baseline: 8/8 SVGs byte-identical (repointed files: render.py, content12.py, content34.py, content56.py, content7.py, content8.py)
  OK  p1-prima.svg core d301b8864a85bb31 produced d301b8864a85bb31
  OK  p2-vita.svg core a744e5d25bce0cba produced a744e5d25bce0cba
  OK  p3-cultura.svg core fe0a0e658a9769bc produced fe0a0e658a9769bc
  OK  p4-sport.svg core 12ddd86c49b5de42 produced 12ddd86c49b5de42
  OK  p5-giovani.svg core 08929554b5265cd1 produced 08929554b5265cd1
  OK  p6-approfondimento.svg core 621054eed30717df produced 621054eed30717df
  OK  p7-lingua.svg core 3746030ae86d2745 produced 3746030ae86d2745
  OK  p8-valutazione.svg core 779aa98cae7b8e28 produced 779aa98cae7b8e28
core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
```
結果：**8/8 字節一致**。註：盤上 core 已是 fix3，故此門禁驗的是 fix3 core 的完整性，不是本版來源 core（本版建於 fix3 之前）。

## 4. freeze diff（core-it/svg 對本版 svg）

```
$ ./venv/bin/python freeze.py diff --core-svg <core>/svg --edition-svg <edition>/svg --json $S/freeze-diff.json
p1: +44 strings / -42 strings; CJK core 197 -> edition 226; added CJK chars: 102
p2: +19 strings / -19 strings; CJK core 191 -> edition 204; added CJK chars: 74
p3: +20 strings / -20 strings; CJK core 180 -> edition 193; added CJK chars: 55
p4: +19 strings / -17 strings; CJK core 162 -> edition 175; added CJK chars: 56
p5: +24 strings / -24 strings; CJK core 227 -> edition 240; added CJK chars: 84
p6: +14 strings / -14 strings; CJK core 167 -> edition 180; added CJK chars: 62
p7: +28 strings / -28 strings; CJK core 304 -> edition 317; added CJK chars: 110
p8: +175 strings / -187 strings; CJK core 1015 -> edition 1042; added CJK chars: 427
TOTAL added CJK characters: 970
```
結果：rc=0。586 行片段（`freeze-fragments.txt`）逐條讀過，全部可解釋：(i) 簡體→繁體讀者層互換；(ii) fix3 前舊 core 文本（D1–D5 來源）；(iii) 同文重斷行。**0 未解釋片段**，無 fan-out 擅改（zh-tw 讀者層本身為 CJK，不做 strict-CJK 判定）。

## 5. 印刷 / 網頁 text layer

```
$ pdftotext -layout La-Lucerna-VOL4-ZH-TW.pdf $S/print.txt
$ pdftotext -layout La-Lucerna-VOL4-ZH-TW-web.pdf $S/web.txt
print.txt = web.txt = 102,884 B，字節相同
print words 6843 / web words 6843，詞多重集差異 0 / 0（0 單邊詞）
```
結果：**字節相同，多重集 diff 0**。

## 6. creambox 全版掃描（canonical）

```
$ python3 ~/workspace/goals/.../hidden_files/w47/tools/creambox.py <edition>/svg/*.svg > $S/creambox-all.log 2>&1   # rc=0，355 行
```
結果：盒內清除量最小 **+3.9 px**（P3/P5 E TU）；P7 工具盒最小 +4.5，desc-clear 最小 −1.5。9 條負「末基線」清除量均為窗下誤報（下一節標題/表行）：P1 `ADESSO TU` −37.0 / `LA PAROLA DELLA SETTIMANA` −24.0 / QUIZ 副標 −44.0；P3 `IL TORRAZZO E IL TORRONE` −37.0；P4 表行 −40.0/−40.0/−26.0；P6 `ESERCIZI` 標題 −42.0 ×2。desc-clear −1.1…−2.1 px 為計量 artifact（末行無下行字母，P3/P5 E TU 200 dpi 裁圖目視確認盒內）。

## 7. PIL 真墨跡掃描（`sweep.py` / `sweep2.py`，audit 字體解析，Noto Sans CJK TC）

```
$ python3 $S/sweep.py > $S/sweep.log 2>&1     # rc=0
$ python3 $S/sweep2.py > $S/sweep2.log 2>&1   # rc=0
```
結果：
- (a) 盒題 19 個全部 fit。最緊：P1 `LA SETTIMANA IN CIFRE　數字看本週` 墨 ..960.0 vs 盒 961.0（+1.0 px）；200 dpi 像素驗證實渲染墨 ..959.3（+1.7 px）。P7 `ERRORI TIPICI` ..1735.8（+126.2）。**無盒題溢出**。
- P1 副標題 `本週日程　Cosa succede, giorno per giorno` 墨 1461.5–1839.2，餘 22.8 px，fit。
- (b) 全版唯一超出版心 1862 的墨跡：P2 b `b. il ponte di barche per la festa del 21` ..1875.0（+13.0 px）、d `d. la piccola luce di cera che si accende` ..1877.8（+15.8 px）。
- (c) P4 b ..969.0（+8.0 vs 欄 961）、c ..973.5（+12.5）；P8 F a ..1430.0（+18.5 vs 欄 1411.5）、b ..1430.5（+19.0）、c ..1419.8（+8.2）；P7 FRASI 譯行 ..533.2（+22.8 vs 欄 510.5，下一欄文字起於 989，無碰撞）。
- (d) P8 字號：[13.0, 14.0, 15.5, …, 46.0]，最小 13.0 px = **9.75 pt**。

## 8. PDF span 掃描（`pdfscan.py`，PyMuPDF，`pdfscan.log`）

```
$ ~/workspace/weekly-git/tools/venv/bin/python $S/pdfscan.py   # rc=0；8 頁，1462.5×2025 pt
```
結果：
- 右緣違規（實質）：僅 p2 b x1=1408.2（+11.7 pt）、d x1=1409.7（+13.2 pt）——與 PIL 一致，D2 第三重證實。
- 其餘右緣框外延 ≤1.9 pt 均為 side bearing（PIL 真墨跡在界內）：p1 `2026` +0.2、p2 圖注 0.0 / 副標 +1.6、p5 圖注 +1.6、p8 範文行 +1.8/+1.9。
- 無左緣/底緣違規；無可見重疊（重疊對均為刊頭帶/同行粗體/換行括注的框 artifact，8 頁目視確認）。
- 各頁最小字號：p1–p7 ≥11.62 pt；p8 9.75 pt。

## 9. 其他計量

- `pdftotext` 頁數：印刷 8 頁、網頁 8 頁。
- VOL 計數（SVG grep）：VOL.4 ×9；VOL.5 ×3（P2 E TU 交叉引用、P7 LETTERE 披露、P7 下期預告，均合法）。
- 頭條：39 非空格字符 ≤56。
- 範文：99 詞（實數）。
- 級別：A2 47 / B1 70 / B2 33（138 行內標籤 + 12 匹配題組頭各 4 題）。
- ABSTRACT.txt：1 行，含 La Lucerna + VOL.4，無 ASCII 雙引號。
- CJK：U+3000 ×101；全角冒號 ×62（凍結動詞範式注 + 答案）；唯一簡體疑似字符「译」×4（text.md Q137–140 括注標籤，KIT 已披露，見 PROOF-NOTE O6）。
- 禁用詞 Ucraina/Russia/Putin：0。
- 8 頁 100 dpi 渲染（`pages/p1.png`–`p8.png`）逐頁目視：除 D2 外無溢出/重疊/頁腳侵入/豆腐塊。
- 外部事實：5 組公開來源抽查（Serie A 第 11 輪+積分榜+第 12 輪賽程、Torrazzo 高度、Torrone/Eurochocolate、BookCity/TFF、Manovra 2027）——D1/D3 以外全部相符。
- 200 dpi 裁圖：`crop-p2-match.png`（D2）、`crop-p1-cifre.png`（O1 像素驗證）、`crop-p1-subtitle.png`（P1 副標題 fit）、`crop-p3-etu-bottom.png` / `crop-p5-etu-bottom.png`（O4）。

## 10. 門禁總表

| 門禁 | 結果 |
|---|---|
| occlusion audit | 0 flags（selftest 正常） |
| p8 extract | 150/150（本版 + core） |
| p8 compare vs core | CLEAN，keydiff [137,138,139] |
| freeze baseline | 8/8（當前 fix3 core） |
| freeze diff | rc=0，0 未解釋片段 |
| print/web text layer | 字節相同，6,843 詞，multiset diff 0 |
| P8 最小字號 | 9.75 pt |
| creambox 全版 | 盒內最小 +3.9 px，負值均為誤報 |
| BOXTITLE 真墨跡 | 全部 fit |
| ABSTRACT（SOP §9） | 通過（含 La Lucerna + VOL.4） |

**結論對應 PROOF-NOTE：(b) 有問題——D1–D5 共 5 項，全部 core 級、全部已在 core fix3 修復，待重 fan-out 後重校。**
