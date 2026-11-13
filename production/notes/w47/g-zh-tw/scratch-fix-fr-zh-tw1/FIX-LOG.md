# FIX-LOG — 2026-w47-fr-zh-tw fix1（D3，2026-11-11）

- 修復員：fix1；版：`2026-w47-fr-zh-tw`（法語目標 × 繁體中文讀者，VOL.4，re-fanout #2 重建版）
- 依據：proof1 結論 (b)，缺陷 D3（P4 `chiffres_note` 孤兒句號）
- 工作區：`~/workspace/weekly-git/production/2026-w47/2026-w47-fr-zh-tw/`
- 記錄目錄：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-fr-zh-tw1/`
- 未 commit、未 push；待另一位獨立校對員 re-proof，本人不定稿。

## 0. 開工核對（修前三 SHA，與簡報逐字一致）

| 件 | SHA-256 | 字節 |
|---|---|---|
| 印 `La-Lucerna-VOL4-fr-zh-tw.pdf` | `ccdfc35fb49f41f6ee966f296a0016ccdff6b1d4a865cb79238997c3b42af95b` | 30,551,086 |
| 網 `La-Lucerna-VOL4-fr-zh-tw-web.pdf` | `ac9f148038dcdb103230d78a319a1d206d3f394a3746dabd819d683852603324` | 2,552,871 |
| 文 `2026-w47-fr-zh-tw.text.md` | `6e348b8c9309d1822a3d6cf4482dee9781ea07157002f0239990b5c61ed73ba9` | 45,998 |

- 寫探針 `echo test | git hash-object -w --stdin`：通過（`9daeafb9…`），`/dev/null` 存在，無需修復。
- TMPDIR = 本記錄目錄（/tmp 僅 512M）；解釋器 `~/workspace/weekly-git/tools/venv/bin/python`。
- `~/workspace/weekly-git/AGENTS.md` 已讀。
- 修前 SVG 哈希見 `svg.pre-fix.sha`；`ABSTRACT.txt` 修前 SHA `7f328a0221c4ee30eef19f4724740cde99842feac3e1af0e40daf17f20302ac5`。

## 1. 缺陷 D3 與改動（僅 1 行源碼）

- 缺陷：P4「LES CHIFFRES DU SPORT」框 `chiffres_note` 繁體釋義
  `大師賽決賽結果與杜林名單見本版正文。` 實測 387.0 px，欄寬 378.5 px（`content34.py:168`
  `p.para(..., 21.5, "serif", ..., CW - 44)`，欄寬 = 422.5 − 44），超寬 8.5 px 折行，
  句號獨行於 `svg/p4-sport.svg` y=550.53（該基線僅此一元素，修前 SVG 實測確認：
  y=520 行 `大師賽決賽結果與杜林名單見本版正文`、y=550.53 行 `。`）。
  核心 fix4 已將法語注改為「大师赛结果与都灵名单见本版正文。」（P4 單行 y=520），讀者語釋義未同步。
- 改動：`expl.py:122` 僅此一處，刪「決賽」二字——

```diff
122c122
< "chiffres_note": "大師賽決賽結果與杜林名單見本版正文。",
---
> "chiffres_note": "大師賽結果與杜林名單見本版正文。",
```

- `diff expl.py.pre-fix expl.py` = 僅 122 行；其餘「決賽」出現處（`date_22:119`「杜林決賽＋法甲回歸」、
  g2、mots_tennis、teaser_note 等，共 15 行）全部未動；`content34.py` 等其他文件未動；
  `ABSTRACT.txt` 未動（修後 SHA 與修前相同）；`WEEKLY-KIT.md` 未動（mtime 仍為 2026-11-11 15:53）。

## 2. D3 實測（修後，`d3-verify-fix1.py`，`d3-verify-fix1.log`）

- `text_w`（21.5px serif）：舊句 387.0 px（超 +8.5），新句 **344.0 px**（欄寬 378.5，餘量 +34.5），與簡報預期 344.0 px 一致，單行。
- P4 SVG：新注為**單一** `<text x="1461.5" y="520.0" font-size="21.5">大師賽結果與杜林名單見本版正文。</text>`
  （句號附於句末）；基線 y=550.53（±1.0）上元素 **0 個**；框區內孤兒 `。` 元素 **0 個**。
- PIL 真墨（`cards/p4-sport.png`，1950×2700，與 SVG 同座標）：
  舊孤兒帶（x 1440–1862，y 530–575）墨量 **0 px**；
  新注行帶（x 1440–1862，y 495–528）墨量 **2370 px**，x 1462..1798、y 501..522，
  右緣 1798 在欄右緣 1862 之內。
- **D3 VERDICT: PASS**（rc=0）。

## 3. 重建（整版，`build-fix1.log` / `render-fix1.log` / `webpdf-fix1.log` / `export-fix1.log`）

- `run.py`：rc=0，零 `FLOW OVERFLOW` / `HEAD TOO WIDE` / `NOSPACE`；
  **TOTAL 150**（按版 10/15/18/18/17/18/12/42；按級 A2 53 / B1 75 / B2 22）。
- `render.py`：rc=0，cards 8/8，印刷 PDF 30,551,088 B。
- `tools/webpdf.py svg La-Lucerna-VOL4-fr-zh-tw-web.pdf`：rc=0，網頁 PDF 2,552,857 B（< 7 MB），46,235 text bytes。
- `export_lang.py zh-tw`（cwd=版目錄）：rc=0，`.text.md` 39,011 字符、542 條目、150 題。
- SVG 哈希變化：**僅 P4**（`5af79c73` → `b4d0e944`），其餘 7 頁與修前字節相同。

## 4. 修後三 SHA（新交付件，本次重建產生）

| 件 | SHA-256 | 字節 |
|---|---|---|
| 印 `La-Lucerna-VOL4-fr-zh-tw.pdf` | `baf81d032effddc59da8f9f8a97028aebab51b58c10f5432870dccce908b8e18` | 30,551,088 |
| 網 `La-Lucerna-VOL4-fr-zh-tw-web.pdf` | `2766f3ed492f84349159ad3fb33f87c48291256495ca997e4b7518187d48d212` | 2,552,857 |
| 文 `2026-w47-fr-zh-tw.text.md` | `e5c8c1cd50f04b7a67bf03403f6d0361d6bfd03ad975946895f0477dc8acf3a2` | 45,992 |

- 網 PDF 鐵律：SHA 與字節大小均不可復現，只比文字層——本次網 PDF 由本次重建產生，
  上表為新 SHA，不與舊 SHA 比對；文字層見 §5（逐頁一致）。
- `.text.md` 同步：`diff text.md.pre-fix → 新 text.md` **僅 515 行一處**：
  `大師賽決賽結果與杜林名單見本版正文。` → `大師賽結果與杜林名單見本版正文。`
  （字節 45,998 → 45,992，−6 B = 刪 2 個 CJK 字 × 3 B UTF-8，吻合）。
  text.md 由 `export_lang.py` 自源碼導出（非 PDF 提取），再與交付件逐字節比對如上。

## 5. 全套門禁（`gates-fix1.py`，即 re-fanout #2 `gates.py` 同款，SCR 僅改指本記錄目錄）

**GATES 15/15 PASS**（`gates-fix1.log`，`zh-tw/gates-fix1.json`）：

| 門 | 結果 |
|---|---|
| run | exit 0，零溢出；TOTAL 150（按版 10/15/18/18/17/18/12/42；按級 A2 53 / B1 75 / B2 22） |
| occlusion（真實審計，非 --selftest） | **0 flags**，自檢 OK；`zh-tw/occlusion-fix1.json`：`flag_count: 0`，`flags: []` |
| p8_extract | keys 150/150，印出注記 121/150 |
| p8_compare（直接讀 `zh-tw/p8compare-fix1.json` 本體） | **CLEAN**，total 150，core_count 121 = edition_count 121，missing []，extra []，uncertain []，**keydiff [150]** |
| source_freeze | content/bslib/svglib/run 與 core 字節相同；render.py 僅 BASE+PDF 名不同 |
| string_freeze | 核心全部非 CJK 字符串同頁存活；核心講解層中文 0 殘留；未計入 CJK 0；1 條因翻譯豁免 |
| freeze_direct（版內兩次構建） | 8/8 SHA 相同：`bc9050c8, b46154cf, 22af3699, b4d0e944, a1981b77, 81a3f8ff, 087855db, 7b8c6116`（僅 P4 變） |
| text_layer | 印/網 `pdftotext -layout` 逐字節一致（101,440 B）；網 2,552,857 B < 7 MB；印 30,551,088 B |
| p8_font | P8 最小字號 **11.625pt** ≥ 9.75pt（亦 ≥ 本任務 10pt 下限） |
| scans | U+2019=0，U+00B7=0，金色 0，舊紙色 0，紙色 #fbfaf6 ×8 |
| chips | 134 枚 [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck（對 `core-fr/final-fr-p8.json`） | 150 鍵比對，**僅 Q150 不同**（寫作題鍵，預期；Q150 抽出鍵 `開放題` 為截斷 artifact，與修前一致） |
| mcq（`zh-tw/mcq-fix1.log`） | 45 題體，1,441 渲染行，**DEFECTS: 0**，UNLOCATED: 0 |
| widths | 31 條單行字符串全部在預算內 |
| band_spans（印 PDF 實測 spans） | FR title ends 1236.9，band_r1 starts 1405.0，FR sub ends 837.2，band_r2 starts 1571.4 |

- 逐頁文字層（`textlayer/`，`pdftotext -layout -f N -l N` 逐頁比對，`cmp`）：
  P1–P8 **全部 IDENTICAL**（12,492 / 10,406 / 10,620 / 12,790 / 11,703 / 12,383 / 11,780 / 19,266 B）。
  P4 印/網均含新注 1 次、舊句 0 次。
- 標準 freeze 核心比對（`tools/freeze.py baseline --build ../production/2026-w47/core-fr
  --core-svg ../production/2026-w47/core-fr/svg --out <本目錄>/freeze-core`，`freeze-core.log`）：
  **8/8 SVG 字節相同**（p1 `6aad8b4b…`、p2 `5709e000…`、p3 `7828cfe3…`、p4 `7e46e630…`、
  p5 `fff2a8d3…`、p6 `7af7cf3c…`、p7 `75237d67…`、p8 `5bee4d44…`）；
  核心完整性：運行前後重哈希， shipped core SVG 未變。core-fr 唯讀，未寫入。
- 孤兒標點全掃（`check_extra-fix1.py`，即 re-fanout #2 `check_extra.py` 同款，`check_extra-fix1.log`）：
  **EXTRA PASS**——orphan total=2，new=**0**，inherited=2（均為核心既有 `—`：P4 y=623.13、P6 y=653.69），
  **remnant=0**（P4 `。` 殘留已隨本次修復消失），shared_baseline=0；
  孤行填空線 Q130（P8）+ P3 Q36/Q37 三處，與核心同位一致；
  Q148：stem_ok=true，key_in_content8=true，extracted=`devant le`。
- check_s11（`scratch-proof-fr-zh-tw2/check_s11.py zh-tw`，`check_s11-fix1.log`）：
  **ALL §1.1/P8 CHECKS PASS**——色集 core 19 = edition 19，extra none、missing none；
  徽章色 A2/B1/B2 均在；P8 SVG 最小字號 15.5；Q113–120 選項行在；Q120 chip OK #37402f（B2，與核心一致）；
  ÉCRITURE 頭在；Q113–116 完形空、117–119 單選號、145–149 完形空均在。

## 6. 範圍與未動項

- 生產目錄除本次修復（expl.py:122）與重建產物（svg/p4-sport.svg、cards/*.png、兩 PDF、.text.md、
  `__pycache__` 再生）外零寫入；core-fr 唯讀（freeze 證明未變）；其他版未碰；
  未 run insert.py / lint / git add / commit / push。
- 備註：檢查期間發現 `production/2026-w47/core-nl/` 有其他並行 agent 的寫入（與本任務無關，本人未碰）。
- 修後由另一位獨立校對員 re-proof；本人不定稿。

## 7. 記錄文件（本目錄）

- `FIX-LOG.md`（本文件）、`expl.py.pre-fix`、`text.md.pre-fix`、`svg.pre-fix.sha`、`abstract.pre-fix.sha`
- `build-fix1.log`、`render-fix1.log`、`webpdf-fix1.log`、`export-fix1.log`
- `gates-fix1.log`、`gates-fix1.py`、`check_mcq.py`、`zh-tw/`（build-fix1.log、build-fix1-rerun.log、
  gates-fix1.json、occlusion-fix1.json、p8-fix1.json、p8compare-fix1.json、mcq-fix1.log）
- `d3-verify-fix1.py`、`d3-verify-fix1.log`
- `check_extra-fix1.py`、`check_extra-fix1.log`、`zh-tw/extra-fix1.json`
- `check_s11-fix1.log`、`freeze-core.log`、`freeze-core/`（核心 baseline 拷貝）
- `textlayer/`（逐頁印/網文字層 P1–P8）
