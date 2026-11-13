# GATE-LOG — W47 zh-tw-ja proof1 機械門（重建後版）

- 復校對象：`production/2026-w47/2026-w47-zh-tw-ja/`，Lucerna-VOL4-JA.pdf / Lucerna-VOL4-JA-web.pdf / 2026-w47-zh-tw-ja.text.md（重建後版；舊版 SHA 已過期，見 PROOF-NOTE §1）
- 探針：2026-11-11 12:22 UTC `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` OK（`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`）+ 探針文件寫入 goals 側 scratch OK；TMPDIR 為 scratch 下 `tmp/`。
- 工具：全部用 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；未用系統 python3。

## SHA 核對（開工時盤上實測，與任務書一致）

| 文件 | 字節 | SHA-256 | 結果 |
|---|---|---|---|
| Lucerna-VOL4-JA.pdf | 18,089,964 | 73f623f8884296f8d23aa54e16b46bc10a40c22df24908047478a975fdd58ef8 | 一致 |
| Lucerna-VOL4-JA-web.pdf | 2,562,627 | b5cd6ad09008846450d662aa3e1c8b0fcd1eb0ddec099d281a6f068e36042eed | 一致 |
| 2026-w47-zh-tw-ja.text.md | 53,753 | e03a56ad7254ea135f4bf6c344e6e3e798acc06a9c6452209d2b0510324e5e63 | 一致 |
| core-zh-tw 印刷 / 網頁 / text.md | 19,420,552 / 2,324,042 / 49,798 | 5ec35fe2…570d9a / 1c0799ac…240 / 09e083e1…02f02b | 與 KIT §100 一致，未變 |

## 機械門結果

| 門 | 命令 / 方法 | 結果 | 日誌 |
|---|---|---|---|
| freeze diff 首檢 | `tools/venv/bin/python tools/freeze.py diff --core-svg production/2026-w47/core-zh-tw/svg --edition-svg production/2026-w47/2026-w47-zh-tw-ja/svg`（+ `--json freeze.json`） | **8/8 頁**；新增 CJK 5763 字；rc 0 | freeze.json |
| freeze baseline | `tools/freeze.py baseline --build . --core-svg svg --out gates/ja-proof1/freeze-base`（gates-ja.py §11） | **8/8 SVG 字節一致**；shipped core SVG 完整性 OK | gates/ja-proof1/freeze.log |
| freeze diff --strict-cjk | 同上 + `--strict-cjk` | RC=1（預期內，fan-out 必然新增日語 CJK；新增 5763 字） | gates/ja-proof1/freeze-strict.log / freeze-strict.json |
| checks.py | edition 內 `checks.py`（gates-ja.py §1） | 短語 8×2 ✓；P4 [90.0, 450.0, 900.0]、P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43] ✓；`SIMP_ONLY_HITS ['国', '学']` 親驗為日語誤報（PROOF-NOTE §4）；總評 FAIL 僅由此行引起 | gates/ja-proof1/checks.log |
| occlusion 審計 | `tools/occlusion_audit.py --selftest` + `--json occlusion.json <edition>/svg` | 自檢 rc 0，**0 flags** | gates/ja-proof1/occlusion*.log / occlusion.json |
| p8 extract | `tools/p8.py extract --p8 svg/p8-test.svg --total 150 --json p8-extract.json` | **150/150** | gates/ja-proof1/p8-extract.log |
| p8 compare | `tools/p8.py compare --core-p8 core-zh-tw/svg/p8-test.svg --edition-p8 svg/p8-test.svg --total 150 --json p8-compare.json` | **CLEAN**（missing=[] extra_count=0 keydiff=[]） | gates/ja-proof1/p8-compare.log |
| creambox canonical | `hidden_files/w47/tools/creambox.py <edition>/svg/*.svg` | 36 盒，負清除 0；P1 18.8 / P2 41.8 / P3 16.1 / P4 35.8 / P5 6.4 / P6 19.9 / P7 12.4；P7 工具盒 +40.5 / +12.4 / +14.0 | gates/ja-proof1/creambox.log / creambox.json |
| boxtitle | `gtools/boxtitle.py <edition>/svg gates/ja-proof1` | 36 盒，超框 0；最小標題右余 **1.2px**（P2 耶誕城小檔） | gates/ja-proof1/boxtitle.log / boxtitle.json |
| creambox-pil | `gtools/creambox-pil.py <edition>/svg gates/ja-proof1` | STRADDLE **0**；CREAM-COVER **0**；P7 最小清除 10.4 | gates/ja-proof1/creambox-pil.log |
| 印/網文字層比對 | `pdftotext -layout` 兩版 + multiset 差 | 兩版各 89,711 B；多重集差 **0**；本週日 11 / 下週日 0 / BABYMONSTER 0 / 取捨 2 / 小雪 54（兩版一致） | gates/ja-proof1/print.txt / web.txt |
| fitz span 位置差分 | PyMuPDF 讀兩版全部 span（本輪另跑） | 兩版各 3,099 spans，僅 1 處不同：P1「Lucerna」字標 bbox（裝飾字標重嵌字體，文字相同） | （本文件內記錄） |
| PDF 規格 | PyMuPDF（gates-ja.py §7） | 兩版各 8 頁、1462.5×2025 pt；P8 最小 9.75pt、最大 34.5pt；網版 2,562,627 B < 7 MB | gates/ja-proof1/gates.json |
| keycheck | `gtools/check_fillin_keys.py <edition>/<slug>.text.md <edition>` + 答案區正則 | 填空鍵 54，無 MISS；keys 1–150 連續 | gates/ja-proof1/fillin-check.log |
| SVG 鍵 vs text.md 答案 | keycheck-raw.json 逐題比對（本輪另跑） | 95 字母鍵 0 不符；54 填空詞 0 不符；Q150 同義（`✓` vs `✓ 自由課題`） | keycheck-raw.json / keycheck-150.json |
| 泄漏掃描 | deny 串（next Sunday / Next Sunday / finish line 等 10 條）掃 edition SVG | deny_hits {}；唯一共享長 ASCII 串「A. 12:00 · B. 14:00 · C. 19:00」（核心同文，Q140 選項） | gates/ja-proof1/gates.json |
| P6 墨縫 | occlusion_audit 幾何量測（gates-ja.py §10） | **0.6px**（990.8 → 991.4） | gates/ja-proof1/gates.json |
| 彎/直引號全掃 | grep SVG + text.md | `"` / `'` 皆 0（SVG 僅標頭屬性引號）；“ ” ‘ ’ 皆 0 | （本文件內記錄） |
| 簡體字擴大掃查 | 專用簡體字表掃 SVG + text.md | 僅 国/学（日語句內，§4），其餘皆 0 | （本文件內記錄） |
| 漢字字形掃查 | 日語新字體/繁體字形分語境掃 SVG | 0 處混用（PROOF-NOTE §4） | （本文件內記錄） |
| VOL / 「·」計數 | grep / 文本節點分類 | VOL.4 ×10、VOL.5 ×1、VOL.3 ×2、VOL.2 ×0；「·」59 處 | （本文件內記錄） |
| 級別分佈 | SVG 題號徽章計數 + 配對組折算 | A2 44 / B1 74 / B2 32（徽章直計 41/65/32，配對組 25–28 A2、43–46/61–64/79–82 B1 各補 3） | （本文件內記錄） |
| 日期/星期 | `date -d`（Asia/Taipei） | 11-16 一、11-17 二、11-19 四、11-21 六、11-22 日、11-24 二；11-13 五；12-27 日；2027-01-03 日 | （本文件內記錄） |
| 8 版看圖 | 自渲染印刷 PDF 100 dpi 全 8 頁 + P2 最緊盒 200 dpi 裁切 | 無溢出/重疊/壓頁腳；P4 柱狀圖比例正；P6 時間軸五點齊全 | render/p1–p8.png、render/tight-p2-耶誕城小檔.png |
| 作文範文 | text.md 去空白計數 | **142 字**（120–180 帶內），與 P8 注一致 | （本文件內記錄） |
| ABSTRACT.txt | 讀取 | 單行日語，無 ASCII 雙引號，真實主題＋A2からB2＋150問 | （本文件內記錄） |
| SVG 斜體 | grep | 0 處 | （本文件內記錄） |
| P7 末端 | occlusion_audit 幾何量測（本輪另跑） | 右欄末基線 1815.28；預告條底 2581.3，頁腳線 2596，淨空 14.7px | （本文件內記錄） |
| 舊缺陷閉合 | grep 四源 | 下週日 0 / 本週日 11（SVG、text.md、印/網 PDF 各 11/0）；来週の日曜日 0 / 今週の日曜日 6；D-ja-1/D-ja-2 皆為修後措辭 | （PROOF-NOTE §3） |

## 結論

機械門除 freeze-diff --strict-cjk（fan-out 預期 RC=1，已人工分類）與 checks.py SIMP_ONLY 誤報行外全部通過。
內容結論見 PROOF-NOTE.md：**(a) 零問題，可定稿**。舊輪 3 項缺陷（D1/D-ja-1/D-ja-2）皆已在重建中消除；全量復校未發現新缺陷。
