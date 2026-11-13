# GATE-LOG — 2026-W47 zh-tw-ja proof2（獨立復校，逐令記錄）

- 版：`2026-w47-zh-tw-ja`（zh-tw × ja，VOL.4）
- 工作區（唯一）：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-zh-tw-ja1/`，下稱 `$S`；`$E`＝`~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-ja`；`$C`＝`~/workspace/weekly-git/production/2026-w47/core-zh-tw`；`$T`＝`~/workspace/weekly-git/tools`。
- 全部 Python 工具均用 `$T/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；凡 import 生產源码均置 `PYTHONDONTWRITEBYTECODE=1`；TMPDIR 全程＝`$S/tmp`。
- 結論：(a) 零缺陷，可定稿（詳見 PROOF-NOTE.md）。

## R0 開工探針

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0。
- scratch 寫入測試：`echo probe > $S/tmp/probe.txt` 成功；`df`：workspace 57G 可用。

## R1 三 SHA 盤核（開工）

- `sha256sum $E/Lucerna-VOL4-JA.pdf $E/Lucerna-VOL4-JA-web.pdf $E/2026-w47-zh-tw-ja.text.md`：
  - 印 18,089,964 B `73f623f8884296f8d23aa54e16b46bc10a40c22df24908047478a975fdd58ef8` ✓
  - 網 2,562,627 B `b5cd6ad09008846450d662aa3e1c8b0fcd1eb0ddec099d281a6f068e36042eed` ✓
  - text 53,753 B `e03a56ad7254ea135f4bf6c344e6e3e798acc06a9c6452209d2b0510324e5e63` ✓
- 核心對照 SHA（三個皆與 KIT 一致）：印 `5ec35fe2…570d9a`、網 `1c0799ac…240`、text `09e083e1…2b`。

## R1b 操作失誤披露（見 PROOF-NOTE §0）

- 首次在 `$S/build` 跑 `run.py` 前未核對 `OUT`：五個 content 模組 `OUT` 硬編碼生產 svg 路徑，致 8 個生產 SVG 被重寫（mtime 20:34–20:35 UTC）。
- 損害核實：其後用當時生產 SVG 重渲印 PDF，SHA 與交付逐字節相同（R2）；scratch 重建 8/8 MATCH（R3）；終驗三 SHA 未變（R13）。

## R2 重渲印 PDF（由重寫後的生產 SVG；`$S/render/render.py`）

- RC=0；`$S/render/Lucerna-VOL4-JA.pdf` SHA `73f623f8884296f8d23aa54e16b46bc10a40c22df24908047478a975fdd58ef8`——**與交付逐字節相同**。生產 cards 未動（只在 scratch 渲染）。

## R3 run.py（scratch 重定向版）

- `$S/build` 副本：`content*.py` 的 `OUT` 以 sed 改指 `$S/build/svg`（改前 grep 確認 5 處皆為生產路徑；改後重跑）。
- RC=0；TOTAL 150；by level A2 44 / B1 74 / B2 32；by page 1:10 2:18 3:18 4:18 5:18 6:18 7:12 8:38；by type 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1；0 FLOW OVERFLOW；0 HEAD TOO WIDE；P7 col3 止 1827.28，teaser 止 2581.28；P8 writing strip 止 1280.2；MODEL 142 字。
- 重建 SVG 8/8 與生產逐字節 MATCH（`cmp -s` 全部 MATCH）：
  - p1 `7388381557ce8f61a0482ca68b9d486a3e05952e7ed72666c41cd6931b8c505f`
  - p2 `69fe2b6f2ed83b8ca047cc597efb32faa6f30a00b2dffbcbdb8cac20ae060606`
  - p3 `462465bd1806a27c5b79786b9ae3ed25c84c311e0bce375671486c602de4e20c`
  - p4 `68570d76e1b3a88099b4b10b3811f4ff6ac11f3e26652bc07700d4feccc7960e`
  - p5 `2d5faac670493e2fcab4789723d6c99393ae98b3284a16f90199666460c45d89`
  - p6 `848ae19668a07ce4086f8ec16b578b9726432b7feea732f09f91165c2729adaf`
  - p7 `bfeb049f374e2c07e13f135230e4edf06f3974ab41cc09bb2bfe31333e4802ec`
  - p8 `d5e4ea733402b631dd0b4570b0a05b671d22def9b6ef7351331cd2d4e382a35d`
- 日誌：`out/run.log`（首次誤跑）、`out/run-scratch.log`。

## R4 checks.py（scratch 副本）

- RC=1（僅 SIMP_ONLY 行失敗）；短語 8 句各 2 次 ✓；P4 柱 `[90.0, 450.0, 900.0]` ✓；P6 圓點 `[188.0, 695.21, 948.82, 1033.36, 1202.43]` ✓。
- `SIMP_ONLY_HITS ['国', '学']`：獨立核實 3 處全為日語（中國語 / 国際 / 学べる），假陽性（`out/checks.log`、`out/simp-contexts.txt`）。

## R5 p8.py

- `extract --p8 $S/build/svg/p8-test.svg --total 150`：RC=0，noted set 150/150。
- `compare --core-p8 $C/svg/p8-test.svg --edition-p8 $S/build/svg/p8-test.svg --total 150`：RC=0，**CLEAN**，missing=[] extra_count=0 uncertain=[] keydiff=[]。
- 日誌：`out/p8-extract.log`、`out/p8-compare.log`、`out/p8-extract.json`、`out/p8-compare.json`。

## R6 freeze.py

- baseline（edition 自洽：`--build $E --core-svg $E/svg --out $S/freeze`）：RC=0，**8/8 byte-identical**。
- baseline（核心版：`--build $C --core-svg $C/svg --out $S/freeze-core`）：RC=0，**8/8 byte-identical**；build-copy 經核實確為核心版（內含 `Lucerna-VOL4.pdf`、`2026-w47-zh-tw-en.text.md` 等核心文件）；跑後 core SVG 再驗 `sha256sum -c` 全 OK，未變。
- diff（`--core-svg $C/svg --edition-svg $E/svg`）：RC=0；每頁新增字符串 p1 18 / p2 31 / p3 35 / p4 31 / p5 43 / p6 24 / p7 94 / p8 178，合計 454；新增 CJK 總計 5,763。
- diff `--strict-cjk`：RC=1（STRICT-CJK FAIL）。裁決見 PROOF-NOTE §3：454 條新增字符串全部分類（408 含假名；46 無假名逐條核為家具/標籤/鍵注/圖注）；CJK-only 序列比對 `delete` 操作 0 個；工具局限，非缺陷。
- 日誌：`out/freeze-baseline.log`、`out/freeze-core-baseline.log`、`out/freeze-diff.log`、`out/freeze-diff-strict.log`、`out/freeze-diff.json`、`out/cjk-added-classify.txt`、`out/cjk-body-diff.txt`、`out/core-svg-before.txt`。

## R7 occlusion_audit.py

- `--selftest`：RC=0，`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`。
- `$E/svg`：RC=0，**0 flags**（`out/occlusion.json`：`flag_count: 0`）。

## R8 奶油盒掃描（自寫，`creambox_scan.py`，PIL 真墨）

- 本版：36 盒、630 行盒內文字，**RIGHT overruns 0，BOTTOM spills 0**。盒標題最緊：P2「耶誕城小檔　クリスマスランド案内」PIL over_right −1.25px；次緊 P1 注釈行 −18.0px、P3 注釈 −18.5px。
- 舊版備份（`scratch-refanout-zh-tw/backup/2026-w47-zh-tw-ja/svg`）：36 盒、638 行，RIGHT overruns 0，BOTTOM spills 0；最緊標題同為 −1.25px——**無回歸**。
- 日誌：`out/creambox.log`、`out/creambox.json`、`out/creambox-old.log`、`out/creambox-old.json`。

## R9 渲染像素驗證（交付印 PDF，PyMuPDF，1950px 寬）

- P2 最緊標題：最右墨點 svg-x=1858.5，盒右緣 1862.0，**餘 3.5px**（窗 x[1439.5,1950]，不伸入 gutter 之外；前 5 右緣墨點 415–419 連續）。
- P1 注釈首行：最右墨點 1393，盒右緣 1411.5，餘 18.5px。
- P6 時間軸標籤：頒獎典禮墨 [906.80, 990.80]，夜間遊行墨 [991.40, 1075.40]，**墨隙 0.6px**，無重疊。
- P8 鍵行：150 條編號鍵行 0 越欄；最緊鍵 77（`77. B — 11月17日〜30日は14日、12月は31日、1月は3日、合わせて48日`，y=2499.6，第 2 欄）：PIL 墨右緣 960.75（欄右緣 961.0，餘 0.25px）；交付渲染像素最右墨點 958.5，**餘 2.5px**，行帶內欄外（x>961）墨點 0 個。裁圖 `crops/key77-line.png`。註：首次探針誤裁第 3 欄（空窗），已按正確欄重測。
- P8 全版越欄檢查：越欄的 10 行皆為全幅通欄元素（欄頭帶、寫作範文條、鍵表頭、頁腳），非鍵行；P8 最大墨右緣 1862.05（頁腳「第8ページ／全8ページ」，0.05px 為渲染捨入）。
- 日誌：`out/pixel-probe.log`、`out/p8-colcheck.log`、`out/key77-probe.log`（誤欄）、`out/key77-probe2.log`（正欄）、`out/p6-timeline.log`。

## R10 webpdf / text.md 重建

- `webpdf.py $S/build/svg $S/out/Lucerna-VOL4-JA-web.pdf`：RC=0，2,562,640 B，50,210 text bytes，SHA `65cbbb06c6d36b69e250624ef90f1584b4a808a14135ae9fd146974e81f1b9f8`。
- 第二次重建 `$S/out/web2.pdf`：RC=0，2,562,636 B，SHA `331e163e645822219f7014f0a176e5193b5aa588cf5c0cb9e9fc1cea24f51d4b`——與交付（2,562,627 B，`b5cd6ad0…`）及第一次重建皆不同，證工具字節非確定；文字層：交付網 vs 重建網 **exact text EQUAL，multiset diff 0**。
- `export_zhtw_textmd.py svg $S/out/2026-w47-zh-tw-ja.text.md "VOL.4 · 中国語（繁体字）テキスト · 日本語の解説"`（`$S/build` 內運行）：RC=0；**與交付逐字節 IDENTICAL**，53,753 B，同 SHA `e03a56ad…`（`cmp` 通過；日志「25589 bytes」為字符數）。
- 日誌：`out/webpdf.log`、`out/webpdf2.log`、`out/textexport.log`。

## R11 印/網文字層逐頁比對（PyMuPDF）

- 兩 PDF 均 8 頁，1462.5×2025pt。
- 每頁 multiset diff 0（p1–p8 全 0）；每頁詞數相等（146/227/241/205/246/215/203/879），首末詞 bbox 逐頁 0.1pt 一致。
- 全卷 pdftotext：印 50,209 B、網 50,210 B，multiset diff 1（網多 1 個 `\n`，頁界空白假影）。
- P8 最小字號：印/網均 **9.75pt**（606 spans；最大 34.5pt）。
- 日誌：`out/pdf-checks.log`、`out/print.txt`、`out/web-delivered.txt`、`out/web-rebuilt.txt`、`out/final-geometry.log`。

## R12 內容核驗（全文通讀＋逐題手驗）

- text.md 全文通讀（P1–P8）；題號 1–150 連續（`out/verify150.log`、`out/verify150b.log`：去重後 150；鍵 150 連續；填空鍵 54/54 在題面版正文出現，P8 複習詞 5 個源在 P1–P7；模型 142 字）。
- 日期/星期：`TZ=Asia/Taipei date -d` 驗 18 個日期，11/16 週一、11/17 週二、11/19 週四、11/21 週六、11/22 週日、11/13 週五、12/27 週日等全部與版面一致。
- 算術重算：1,200+800=2,000；2,000−1,200=800；45 天；48 天（14+31+3）；17 天；12 場；5 小時；1.5 小時；50/70/30；6 天——全部正確。
- 8 金句逐字定位出處，P7 頁碼引用全部正確（見 PROOF-NOTE §1）。
- 英文殘留掃描：545 個含拉丁字母 text 節點，0 英文正文/說明殘留（`out/english-scan.txt`）；6 處舊漏鍵注已全譯日語（鍵 92/98/100/117/134/138，答案值未變）。
- §1.1 掃描：紙 #fbfaf6 8 頁；fills 集合與核心完全一致；VOL.5 僅 P7 一次；頁腳 8 頁齊；「·」58 節點與核心分布一致；stroke 僅橄欖/細線/圖表色（`out/s11.log`）。
- 標題數：展示標題 23（定義見 PROOF-NOTE §8；≥30px 節點歸併計）。
- 頁界 spill：各頁內容墨底距 2596 線 46.47–94.48px，零 spill（`out/final-geometry.log`）。
- ABSTRACT.txt：日語單行 419 B，無 ASCII 雙引號。
- 8 頁目視：`render/cards/p1-front.png` … `p8-test.png`（由與交付等價的 SVG 渲染）逐頁看過，無溢出/重疊/壓頁腳。

## R13 終驗（報告寫作前）

- `find $E -newermt "2026-11-11 20:00 UTC"`：僅 8 個 svg（R1b 所述重寫，內容已證逐字節相同）；核心目錄今日零修改。
- 三 SHA 再驗，與 R1 相同，未變。
- 未 commit、未 push；KIT K6/K7 未碰。
