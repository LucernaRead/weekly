# D5 重建報告 — 2026-w43-en-zh-tw（繁體中文讀者版）

W43 en 家 D5-only 重建（SOP §1.1 字體修復：講解層拉丁字母由 Noto Sans CJK 改走
Newsreader）。施工 2026-11-13；**不 commit、不 push**（入倉由獨立重校後的 closer 做）。
工作日誌：`hidden_files/d5-redo/scratch-2026-w43-en/logs/2026-w43-en-zh-tw/`
（`GATES-SUMMARY-run2.txt` 為門禁總表，`GATES-SUMMARY-run1.txt` 為修前總表，
`logs/2026-w43-en-zh-tw-run1/` 為 run1 日誌快照）。

## 一、裝機

- Core 落盤（全家共用一次）：`apply_variant.py --patch-core en --week 2026-w43`
  → `production/2026-w43/core-en/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安裝：`apply_variant.py --svglib patched/2026-w43-en-zh-tw/svglib.py --target en
  --reader zh-tw --week 2026-w43`（先 `--check` dry-run，10 項改動 + mode cjk 正確）。
  裝後 `_D5_READER = "cjk"`。安裝器注記 TC 面（繁體字形）。
- 路由單元測試 `test_d5_routing.py`：**FAILURES: 0**（66 PASS）；fix2 塊保留。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由
  `scratch-prep-p3b/en_textmd_w43.py` 導出（P3b T5 已驗與 issues 已發版字節一致）。

## 二、基線（修前生產版，全部乾淨才裝機）

- `run.py` RC=0，**TOTAL 149**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 與 `MANIFEST-W43-D1.md` 差 −5 B（元數據浮動，同批 4 版之一）。
- 文字層：印 PDF vs 自建網 PDF 字符多重集差 **0**；自建網 PDF vs issues 已發 web PDF
  **非空字符差 0**，僅空格數差（webpdf 文字層空格推斷浮動，D5-METHOD §3.7 同款情形，
  零詞字符丟失）。
- 修前普查 `d5_census.py`：D5 拉丁 **399**、西里爾 0、彎引號在 CJK **1**（>0，符合裝機前提）。
- 基線 P8 口徑：noted **62/149**（與 core 同口徑；de/fr 兩版為 149/149）。

## 三、缺陷與修法（run1 → run2）

run1 共 9 項缺陷，逐項與簡體版（core-en，zh-cn）相同，修法同值。全部為 D5 字體加寬引起
（拉丁粗體在 Newsreader SemiBold 下比 Noto Sans CJK 寬約 5.7%），另有 1 項既有缺陷
（P2 spill，基線同值）。修法只動字號，**未動任何文字內容**。

| # | 門 | 位置 / 內容 | 實測 | 修法 |
|---|---|---|---|---|
| 1 | head_check | P3 `B　FESTIVAL WORDS　節日詞填空` | 25pt 寬 425.2px，超欄 2.7（欄寬 422.5） | `content34.py:118` 25→**24**（408.2 ✓） |
| 2 | head_check | P5 `EARNINGS, IN PLAIN ENGLISH` | 26pt 寬 425.1px，超 2.6 | `content56.py:23` 26→**25**（408.8 ✓） |
| 3 | head_check | P5 `C　THIS WEEK, LIVE　現在進行時` | 25pt 寬 424.8px，超 2.3 | `content56.py:54` 25→**24**（407.8 ✓） |
| 4 | occlusion | P1 暗帶標題與副標 `本週日歐洲撥鐘` 重疊 | 38.5×20.8px（副標 27pt 左緣 x=1665.5；44pt 標題右緣 1613.6 空隙 51.9px） | `content12.py:25` 暗帶標題 46→**44**（與 core-en 同值） |
| 5 | occlusion | P1 `One team…` 與 `　數字看本週` 重疊 | 8.5×12.8px | 隨 #6 框標題縮小解決（與 core-en 同款） |
| 6 | creambox / boxtitle | P1 `THE WEEK IN NUMBERS　數字看本週` | +36.5px | `content12.py:43` 加 `tsize=21`（與 core-en 同題同值） |
| 7 | creambox / boxtitle | P3 `SAY IT ON THE NIGHT　當晚這樣說` | +3.6px | `content34.py:25` 加 `tsize=22`（390.2 ✓） |
| 8 | creambox / boxtitle | P5 `WORDS OF THE SCREEN　螢幕詞表` | +8.9px | `content56.py:76` 加 `tsize=22`（395.9 ✓；繁體 `螢幕` 對簡體 `屏幕`） |
| 9 | spill | P2 `Check your number !` 跌出 DID YOU KNOW 框底 | +12.71px | `content12.py:193` 框高公式尾數 +14→**+34**（框底 +20px；與 core-en 同款既有缺陷，基線同值） |

P8 變化：179→**179** 行，距頁腳線餘量 33.7→**33.7 px**（正，無溢出）。

## 四、門禁（run2，全套 17 門 ALL-GREEN）

| 門 | 結果 |
|---|---|
| 1 run | RC=0，TOTAL 149，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里爾 0、彎引號在 CJK 0 |
| 4 render | RC=0，印 PDF 9,153,657 B |
| 5 webpdf | RC=0，網 PDF 1,576,737 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 類全觸發） |
| 7 p8 extract | noted 62/149（與 core 同口徑） |
| 8 p8 compare | **CLEAN**（missing=[]，extra_count=0；keydiff=[136, 139, 149]——與 KIT 記載的讀者語答案鍵一致） |
| 9 freeze baseline | 8/8（core SVG 未被重建改動） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings，run 拆分所致；對照是 base 修前生產版，不是 core） |
| 11 spill | 0 SPILL（181 OBSERVE） |
| 12 boxtitle | 0 DEFECT（55 titles，390 body lines；本次以基線 svg 為真對照，backup 已補） |
| 13 edge | 0 TOUCH，0 NEAR（8 頁） |
| 14 creambox | PASS，0 defects（P8 179→179，slack 33.7→33.7） |
| 15 文字層 print=web | 字符多重集差 **0** |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | en 家無 gates.py（`audit_en_fr.py`/`audit_en_es.py` 是舊版幾何審計前身，不算 gate） |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 內，closer 拷入 issues 時網 PDF 改名 `<slug>.pdf`）

- 印 PDF：`The-Lucerna-VOL1-en-zh-tw.pdf`，**9,153,657 字節**，
  SHA-256 `c367edeb43683e6956b61649a8776c1fa3d9575d9e7ce1a3c9e5a54d851c41f1`
  （D5 前 KIT §8 記值 22,033,928 字節；繁體版印 PDF 含 CJK 字體嵌入，體量大於拉丁版，
  屬正常）。
- 網 PDF：`2026-w43-en-zh-tw.web.pdf`，**1,576,737 字節**，
  SHA-256 `d13e636bfd9588a3385c68fbde7b66ae7f44f7b0d4b0dba26d634a125eee7d22`
  （D5 前 issues 已發版 1,954,849 字節，`6b67bc90…`）。
- text.md：導出與 issues 已發版 **BYTE-IDENTICAL**
  （SHA-256 `83e0804ee7a434322393b400a7bfa44a24430123d0229465a5133a9c778faffd`）。
- 練習總量仍為 **149 題**。

## 六、KIT

- `production/2026-w43/2026-w43-en-zh-tw/WEEKLY-KIT.md`：§8 實測針腳追加 D5 交付物行
  （新 SHA + 字節數，註明 D5 前值）；文末追加 **§9. D5 重建記錄（2026-11-13）**
  （裝機、基線、缺陷與修法、門禁 ALL-GREEN、新交付物）。
