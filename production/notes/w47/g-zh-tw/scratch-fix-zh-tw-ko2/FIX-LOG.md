**首行：探針 `git -C ~/workspace/weekly-git hash-object -w /dev/null` rc=0（`e69de29bb2…`）+ scratch 真實寫盤通過；新三件：印 `Lucerna-VOL4-KO.pdf` 16,838,020 B / `09fd27a05b0864bbb30da93339d4f2285abf351d44ca72cef5adb7e254ea3d1c`、網 `Lucerna-VOL4-KO-web.pdf` 2,325,045 B / `e4832f3f8a789eb89e7a68c39f3986fc7428baae395223a1de27844dfd8dede4`、text.md 53,916 B / `a44ba8cbb74f28c862b8f689f27e260a2fde3c5ac328e1597147ff933029b1e1`；K2 修后实测：舊形「小雪는」在 8 個 SVG + text.md + content7.py 出現 0 次，新形「小雪은」在 content7.py:60、SVG p7-lang 節點 x=989.0 y=458.42、text.md:4699 各就其位，交付印 PDF 200 dpi 放大目视确认在版；門禁全綠（checks PASS、occlusion 0、p8 150/150 CLEAN、freeze diff 與 fix1 版逐值相同／新增 CJK 4,690、三源 keycheck 150/150、creambox 36 盒 0 負清除、印網文字層差 0、P8 最小 9.75pt；拷回生產後 freeze baseline 8/8、core 完整性 OK；K1 五處六落版點回歸全過）。**

# FIX-LOG — W47 zh-tw-ko fix2（修 proof2 新缺陷 K2，韓語助詞一字）

- **Builder**：fix2（葉子，未再派 subagent）
- **範圍**：只改共享表 `scratch-fanout-zh-tw/tables.py:2215` 的 ko 值一字（小雪는→小雪은）+ 生產版 `content7.py:60` 同字 + 重建 ko 版一版。未改核心、未碰其他 8 版、未碰其他周次、未碰 tools/、issues/，未跑 insert.py / lint --write，無 commit、無 push。
- **復校對象**：`production/2026-w47/2026-w47-zh-tw-ko/`（繁體中文 × 韓語讀者版，VOL.4），proof2 結論 (b) 的唯一新缺陷 K2。
- **先讀**：`scratch-proof2-zh-tw-ko2/PROOF-NOTE.md`（§7 K2）+ `GATE-LOG.md` 全文；`scratch-fix-zh-tw-ko1/FIX-LOG.md`（fix1 K1 輪做法）；`~/workspace/weekly-git/SOP.md` §8、§1.1；`~/workspace/weekly-git/AGENTS.md`。
- **工作目錄（唯一）**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-zh-tw-ko2/`。`TMPDIR=<scratch>/tmp` 全程，系統 /tmp 未用。解釋器全程 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；未用系統 python3。

## 0. 探針與 SHA 硬核對（開工前，兩項皆通過才動手）

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，rc=0；`probe.txt` 真實寫盤通過。
- 修前生產三件與任務給定逐字一致：印 16,838,020 B / `c04102a9a1ceef1cf25fc7f3df6e69266e5f3d8bb2fec8d4370a3f782217d3a6`；網 2,325,041 B / `ed9e11a5c8997eb6b09cd6fd1f9bad6b64d686e2280d4730eac3d48ff65bad61`；text 53,916 B / `2af17f023ab203259aeeb294b04f31e4bbb766398a28ec5f7fd2f163622b06f7`。無出入，開工。
- 磁盤：/home/hatch 150G 總，94G 已用，56G 可用（開工時）。全程無 EDQUOT。
- 核心基線（重建前後兩次一致，未變）：印 `5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a`（19,420,552 B）、網 `1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240`（2,324,042 B）、text `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b`（49,798 B）。

## 1. 改了什麼（共 2 處同字，各以 count==1 斷言後寫入）

### 1.1 共享表（機制層）`scratch-fanout-zh-tw/tables.py:2215`

改前備份：`scratch-fix-zh-tw-ko2/tables.py.bak`，SHA-256 `56b3fba2ea76a95983f2d07028dd1f6911324e6712355ac096024d2b9d1ae530`。

| 行 | 舊（錯） | 新（對） |
|---|---|---|
| :2215 ko 值 | **小雪는** 스물네 절기 중 스무 번째, 立冬 다음이에요. | **小雪은** 스물네 절기 중 스무 번째, 立冬 다음이에요. |

`diff tables.py.bak tables.py`：**僅 :2215 一行**，該行其餘 ko 文一字未動，其他 8 版的任何值一字未動。改動順序：先在 scratch 副本（`work/tables.py`）改 + 重建 + 驗門，全部通過後才對共享表做同一字改動（見 §2）。

### 1.2 生產版 `content7.py:60`（同字，拷回生產時就地改，不從 scratch 拷貝——scratch 副本的 OUT 指向 scratch，生產 OUT 必須不動）

`diff old-build/content7.py production/.../content7.py`：**僅 :60 一行**（小雪는→小雪은），OUT 行（`~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-ko/svg`）未動。

## 2. 重建（只重建 ko 一版；先 scratch 副本，驗門通過後拷回生產）

### 2.1 scratch 副本重擴

- `work/` 內放：改後 `tables.py` 副本 + `transform.py` 副本（PROD 與 NEW_OUT 均重定向至 `work/prod`，斷言確認除 OLD_OUT 匹配串外無 `weekly-git` 殘留；絕無生產寫目標）+ 生產核心拷貝 `work/prod/core-zh-tw`。
- `transform.py ko` rc=0，248 行（與 fix1 同）。transform log（`work/transform-ko.log`）。
- 新舊 content diff：僅 `content7.py:60` 一處；其餘 content 文件僅 OUT 重定向行不同（預期內）；bslib4.py、render.py、run.py、checks.py、export_zhtw_textmd.py、svglib.py 皆 0 diff；ABSTRACT.txt 與舊版逐字相同。
- copytree 帶入的核心舊件 3 個（`Lucerna-VOL4.pdf`、`Lucerna-VOL4-web.pdf`、`2026-w47-zh-tw-en.text.md`）經 SHA 驗證與核心逐字相同後刪除。
- 舊版整目錄備份至 `scratch-fix-zh-tw-ko2/old-build/`（21 項，舊三 SHA 已驗：印 c04102a9…／網 ed9e11a5…／text 2af17f02…）。

### 2.2 scratch 內構建（`PYTHONDONTWRITEBYTECODE=1`，無新 `__pycache__`）

- run.py rc=0（0 FLOW OVERFLOW、0 HEAD TOO WIDE；P7 col3 ends 1821.42、teaser ends 2575.42，與舊版逐值相同；150 題：A2 44 / B1 74 / B2 32；見 `build-run.log`）
- render.py rc=0（見 `render.log`）；webpdf rc=0（2,325,045 B，見 `webpdf.log`）；text.md 導出 rc=0（見 `export.log`；工具打印 27,956 字符，與 fix1 相同口徑，文件為 53,916 B）
- SVG SHA：P1–P6 與舊版逐字相同（p1 `2f021d71…`、p2 `050e53b0…`、p3 `6b01d169…`、p4 `80d4d8db…`、p5 `96565ffd…`、p6 `6301c38d…`），P8 `a390fcc6…` 與舊版逐字相同，僅 P7 變（`31f7898a…` → `ea98763499232539fed49d0fd5e6bc4b33b87d97510c4ccea6d2a08aa2f824ac`）。

### 2.3 拷回生產（驗門全綠之後）

- 拷回文件（5 個，皆為事前 diff 確認的差異文件）：`svg/p7-lang.svg`、`cards/p7-lang.png`、`Lucerna-VOL4-KO.pdf`、`Lucerna-VOL4-KO-web.pdf`、`2026-w47-zh-tw-ko.text.md`；`content7.py` 就地改一字（見 §1.2）。
- **不拷**：`WEEKLY-KIT.md`（scratch 副本是核心 KIT，生產 KIT 另行編輯，見 §5）、其餘 content*.py（OUT 行不同）、run.py/render.py/checks.py 等（0 diff，留生產原物）、核心舊件（已刪）。
- 拷回後生產三件 SHA 與 scratch 候選構建逐字相同（見首行）。

## 3. 新版三件（SHA + 字節）

| 件 | 字節 | SHA-256 |
|---|---|---|
| 印 PDF `Lucerna-VOL4-KO.pdf` | 16,838,020 | `09fd27a05b0864bbb30da93339d4f2285abf351d44ca72cef5adb7e254ea3d1c` |
| 網 PDF `Lucerna-VOL4-KO-web.pdf` | 2,325,045（< 7 MB） | `e4832f3f8a789eb89e7a68c39f3986fc7428baae395223a1de27844dfd8dede4` |
| text.md `2026-w47-zh-tw-ko.text.md` | 53,916 | `a44ba8cbb74f28c862b8f689f27e260a2fde3c5ac328e1597147ff933029b1e1` |

舊三件（fix1 版，歷史）：印 16,838,020 B / `c04102a9a1ceef1cf25fc7f3df6e69266e5f3d8bb2fec8d4370a3f782217d3a6`；網 2,325,041 B / `ed9e11a5c8997eb6b09cd6fd1f9bad6b64d686e2280d4730eac3d48ff65bad61`；text.md 53,916 B / `2af17f023ab203259aeeb294b04f31e4bbb766398a28ec5f7fd2f163622b06f7`。
字節變化說明：text.md 字节不变（는/은 同为 3 字节等长替换，仅 1 处）；印 PDF 字节不变、SHA 变；网 PDF +4 B（字体子集重排所致，内容以门禁为准）。cards 除 p7-lang.png 外皆与旧版逐字节相同。

## 4. K2 / K1 逐一核對（修后实测，生產版）

### K2（本次）

| 檢查 | 結果 |
|---|---|
| 舊形「小雪는」：8 個 SVG + text.md + content7.py | **0**（各 0） |
| 新形「小雪은」：content7.py:60 | 1 處 ✓ |
| 新形「小雪은」：SVG p7-lang 節點 x=989.0 y=458.42 | 1 處 ✓ |
| 新形「小雪은」：text.md | :4699，1 處 ✓ |
| 渲染證據（交付印 PDF 200 dpi 放大） | `render/zoom-k2-p7-b2-prod.png`：「小雪은 스물네 절기 중 스무 번째」在版；同句另三詞 節氣는／燈秀는／市集은 亦在版 ✓（與 scratch 構建放大圖逐字節相同） |
| 羅馬字形 `Xiaoxue는`（元音結尾，正確） | text.md 6 處，未動 ✓ |

### K1 回歸（proof1 的 K1，fix1 已修——本輪全部驗證通過）

舊形 5 串（入圍은／鋼雕은／入圍을／市集는／入圍이에요）在生產版 8 個 SVG + text.md 出現皆 **0**；新形各就其位（入圍는／鋼雕는／入圍를／市集은 各 SVG 1 處 + text.md 1 處；入圍예요 SVG 2 處 + text.md 2 處）；`입니다`／`습니다` 全版 0。

### 全版助詞重掃（proof2 的 26 例口徑）

- CJK 引詞 + 助詞窮舉（`particle-sweep.py`，SVG `<text>` 節點 + text.md）：19 形 50 命中；新舊掃查 diff **僅「小雪는」→「小雪은」一處**（各 2 命中：SVG 1 + text.md 1）；其餘 25 例全部正確（保險箱은／入圍는／入圍를／入圍예요／夜間은／封王이／市集은／市集이／星光大道는／燈秀는／封王은／節氣는／遊行은／遊行이／鋼雕는／鋼雕예요／集點이／頒獎은；其中「封王은」跨 SVG 節點「封」＋「王은」，已按前後節點核實——proof2 所述同類跨節點情形）。
- 另掃全版「는/은」接 CJK 引詞處：同上，無新增同類錯誤。
- 純韓語詞空格消去後掃描（`pure-ko-scan.py`）：元音＋을 0、輔音＋를 0、元音＋은 0、元音＋이에요 0、輔音＋예요 0；元音＋이 2 命中皆為輔音結尾 이（풍선이／한작품이），正確；U+FFFD 0。
- 保險箱은 讀音核實：本版詞表「保險箱은 Kaohsiung의 노동 기억을 담은 금고예요」——保險箱按漢字音讀 보험상（상 收 ㅇ 輔音）→ 은 正確，與 proof2 判定一致，非新錯。

## 5. KIT 與交付

- 該版 `WEEKLY-KIT.md` 已更新：新三件字節 + SHA 寫入正文行（PDFs、Text export），舊值保留為歷史行（未刪）；新增「Fix round 2 — K2 韓語助詞修正」一節（新舊三 SHA + K2 修前／修後 + 候選記錄）；其餘舊值（§1.1 測量、Fix1 節、歷史行等）一字未動。
- **未 commit、未 push**（按任務要求）。新版留在工作樹（`??` 未提交狀態），等 proof2 #2（從頭再復校）通過後再隨 bundle 入倉。

## 6. 門禁匯總（全綠，詳見 GATE-LOG.md）

跑法：`gates.py`（自 proof2 輪複製，僅改輸出目錄與版目錄為本 scratch 候選版；gtools 同源）`ko fix2`，輸出 `gates/ko-fix2/gates.json`；freeze diff 與三源 keycheck 另跑；拷回生產後在生產版重跑 freeze baseline + checks + occlusion + p8（見 `gates/prod-verify/`）。

| 門 | 結果 |
|---|---|
| run.py（scratch 構建） | rc=0，0 溢出、0 超寬 |
| checks.py（本版自帶；生產復核同） | PASS；8 條金句各 2 次；`SIMP_ONLY_HITS []`；P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43] |
| occlusion audit（生產復核同） | selftest rc=0，flags **0** |
| p8 extract + compare（生產復核同） | extract 150/150；compare **CLEAN**（keydiff []、missing []、extra []、uncertain []） |
| freeze baseline（生產版，拷回後重跑） | **8/8** 字節一致（repointed files: content12/34/56/7/8.py）；核心完整性 OK；P1–P6/P8 SVG SHA 與舊版逐字相同，僅 P7 變 |
| freeze diff（string freeze） | 逐頁增／刪與 fix1 版相同：p1 +24/−25、p2 +35/−39、p3 +42/−47、p4 +36/−39、p5 +46/−47、p6 +31/−33、p7 +360/−120、p8 +188/−187；新增 CJK 4,690 字（與 fix1 版同，等長替換不變字數） |
| 印／網文字層 | 多重集差分 **0** 字元（print 95,029 B = web 95,029 B）；「本週日」11、「下週日」0、BABYMONSTER 0 |
| PDF 指標（PyMuPDF） | 印、網皆 8 頁、1462.5×2025 pt；最小字號 **9.75pt**（整刊與 P8 皆然）；P1 最大 147.0pt；P8 最大 34.5pt |
| keycheck（三源交叉，復用 proof2 keycheck.py，輸出改至本目錄） | **150/150 一致，mismatches []**；填空鍵 **54/54** 在正文；答案 1–150 連續；SVG/text.md CJK 版獨有 {韓}、核心獨有 {英}；U+0022 0、U+0027 1（`Kanahei's Little Animals` 專名）；寫作範文 142 字（CJK+數字 126，120–180 區間內） |
| creambox（canonical） | 36 盒；負清除 **0**；各頁 inside-only 最小：P1 18.8、P2 41.8、P3 16.1、P4 35.8、P5 6.4、P6 19.9；P7 工具盒 +40.5/+12.5/+14.0（與舊版逐值相同） |
| boxtitle（真墨） | 36 盒，超框 **0**，最小右余 18.5px |
| creambox-pil（真墨） | STRADDLE **0**，CREAM-COVER **0**；P7 最小底清除 10.5px |
| P6 時間軸銜接（真墨） | 18:30「頒獎典禮」墨右緣 990.8 → 19:00「夜間遊行」墨左緣 991.4，墨縫 **0.6px**，與核心先例一致 |
| 英文泄漏掃描 | deny_hits {}（shared_ascii_long 僅「A. 12:00 · B. 14:00 · C. 19:00」時刻串，與核心共有，非散文殘留） |
| 8 頁目視（自印 PDF 渲染，100 dpi，`render/p-1.png` … `p-8.png`；P7/P1/P8 逐版目視） | 8/8：無溢出、無重疊、無裁切、無頁腳碰撞；P5 香港11月節目表末行「迪士尼聖誕音樂會：11月21、22日」，無 BABYMONSTER 行；P7 工具盒／預告條乾淨；P8 答案區完整；其餘 6 頁 SVG 與舊版逐字節相同 |

### Freeze baseline 註（scratch 版 0/8 的原因，已在生產版重跑 8/8）

gates.py 在 scratch 候選版跑的 freeze baseline 為 **0/8**——freeze.py 的重定向正則只認 `weekly-git/production/` 與 `files/` 路徑，scratch 副本的 OUT（`hidden_files/...`）不在重定向範圍內（log：`repointed files: none`），致重建寫回 scratch 原目錄而非 freeze out 目錄，屬工具對非生產路徑的局限，非版面問題。該次重建為確定性重建：事後核實 8 個 SVG SHA 與構建值逐字節未變。拷回生產後在生產版重跑 freeze baseline：**8/8 字節一致**（見上表與 `gates/prod-verify/freeze.log`）。本輪未重寫 freeze.py（工具改動不在任務範圍，留協調員決定）。

## 7. 過程事件（已如實記錄，無損害）

1. **gates.py 兩處路徑補丁失誤（均在首次運行前發現並修正，未影響構建）**：(a) 首次複製後漏了 ED 行的 f 前綴（`{LANG}` 成字面量），首跑即報錯，修正後重跑；(b) ED 路徑多寫一層 `2026-w47/`（生產佈局有週次層，scratch 佈局 `work/prod/` 下無週次層），`isdir` 判 False 定位，修正後重跑 rc=0。教訓：改路徑後先 `isdir` 驗算再跑門。
2. **freeze baseline 首次誤跑**：一次以家目錄為 cwd 誤跑（`--build .` 指向 /home/hatch），立即 kill；檢查無殘留文件（無 `~/build-copy`、`~/svg`），後以正確 cwd 重跑 8/8。教訓：freeze 的 `--build .` 必須先 `cd` 到版目錄。
3. **heredoc 引用失誤一次**：`<<'EOF'` 內 `$S` 未展開致渲染寫路徑失敗，改絕對路徑重跑通過。
4. **freeze 內重建寫回 scratch SVG**：見 §6 註——僅 scratch 目錄，確定性重建，SHA 未變；生產 SVG 絕未被重建過程直接寫（生產 OUT 只在拷回步驟由 `cp` 寫入已驗文件）。
5. 生產 `__pycache__` 與修前逐字節相同（mtime 12:49，fix1 時代）；全程 `PYTHONDONTWRITEBYTECODE=1`，未在生產目錄新建 `__pycache__`。

## 8. 不碰項（已遵守）

- 核心 core-zh-tw 一字未動（重建前後 SHA 復核一致，三件見 §0）。
- 其餘 8 版一字未動（tables.py diff 僅 :2215 一行 ko 值）。
- O1–O6 觀察項未修（O3 小雪表記統一未做）；D5 未碰。
- 未動他語值、未改源串、未碰其他周次、未 commit、未 push。

## 9. 文件清單（本目錄，本輪新增）

- `FIX-LOG.md`（本文件）、`GATE-LOG.md`、`probe.txt`、`tables.py.bak`（共享表改前備份）、`work/transform.py`（重定向副本）、`work/tables.py`（改後副本）、`work/transform-ko.log`、`work/prod/2026-w47-zh-tw-ko/`（scratch 候選構建）、`build-run.log`、`render.log`、`webpdf.log`、`export.log`、`gates.py`、`gtools/`、`keycheck.py`、`keycheck-150.json`、`gates/ko-fix2/gates.json` 及各門日誌、`gates/freeze-diff.json`、`gates/freeze-diff.log`、`gates/keycheck.log`、`gates/prod-verify/`（生產復核：freeze.log、occlusion.json、p8-extract.json、p8-compare.json）、`particle-sweep.py`、`pure-ko-scan.py`、`sweep-old.txt`、`sweep-new.txt`、`old-build/`（舊版整目錄備份）、`render/p-1.png` … `render/p-8.png`、`render/zoom-k2-p7-b2.png`、`render/zoom-k2-p7-b2-prod.png`、`tmp/`。
- 已清：`work/prod/core-zh-tw`（核心拷貝 32M，生產核心為準，已刪）、200 dpi 中間大圖 2 張（放大裁切圖已留）。
