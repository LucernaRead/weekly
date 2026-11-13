# GATE-LOG — 2026-W47 zh-tw-it proof1

每道門禁的命令與 RC。工作目錄：`~/workspace/weekly-git`（除註明外）。工具 venv：`tools/venv/bin/python`。
版目錄：`production/2026-w47/2026-w47-zh-tw-it/`；核心對照：`production/2026-w47/core-zh-tw/`。

## 0. 開工探針

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，RC=0
- 寫 `hidden_files/w47/scratch-proof-zh-tw-it1/probe.txt`（`probe-ok`）→ 成功；`probe2.txt` → 成功

## 1. SHA 核對（印刷＋網頁 PDF）

- `cd production/2026-w47/2026-w47-zh-tw-it && sha256sum Lucerna-VOL4-IT.pdf Lucerna-VOL4-IT-web.pdf && stat -c '%n %s' …` → RC=0
  - 印刷：`ec9d0624d91abb2ae8875f5f51cb2064d7927d4f1a4a8e4f2454b1fb11894bce`，19,420,291 B ✓
  - 網頁：`34c4ff2c9e3f1fe0e3714c773b5ead11306e542c4a60e52b2c815684ba986988`，2,306,683 B ✓

## 2. 「下週日」計數（防漏檢清單 1）

- `grep -o '下週日' 2026-w47-zh-tw-it.text.md | wc -l` → **11**；`grep -n` 行號：53, 61, 259, 462, 1167, 1209, 1958, 1970, 2512, 4763, 5526
- 核心對照：`grep -o '下週日' core-zh-tw/2026-w47-zh-tw-en.text.md | wc -l` → 0；核心「本週日」11 處（行 53, 61, 259, 462, 1165, 1207, 1954, 1966, 2506, 4749, 5510）
- 日期驗證：`TZ='America/Toronto' date -d '2026-11-22' '+%A %F'` → Sunday 2026-11-22；`2026-11-16` → Monday；`2026-11-29` → Sunday
- 核心路徑更正：任務所給 `production/2026-w47/2026-w47-zh-tw/` 不存在，核心實在 `production/2026-w47/core-zh-tw/`（內含 `2026-w47-zh-tw-en.text.md`、PDF、KIT）。

## 3. text.md 全文 diff（core vs it）

- `diff core-zh-tw/2026-w47-zh-tw-en.text.md 2026-w47-zh-tw-it/2026-w47-zh-tw-it.text.md > /tmp/diff-core-it.txt`（RC=1，正常 diff；2,142 行）
- CJK 字符序列比對（Python，difflib）：除 D1 的 11 處 `本週日→下週日`＋預期翻譯（刊頭/頁腳/H1、P1 詞卡釋義句改意大利語——其餘八版 fanout 同式，已驗 de/fr/es/ja/ko/nl/pt/ru `拿下總冠軍` 各 5 處保留）外全等。
- 數字 token 多重集：core 1,539 個 vs it 1,540 個，僅差一個 "4"（it H1 `VOL.4`，core H1 無數字）。
- 彎標點：text.md 全文 U+201C/U+201D/U+2019/U+2018 皆 0；8 個 SVG 亦皆 0；核心 SVG 同為 0。

## 4. 幾何遮擋掃描

- `tools/venv/bin/python tools/occlusion_audit.py --selftest` → `selftest OK`，RC=0
- `tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-zh-tw-it/svg` → `0 flags`，RC=0

## 5. P8 門禁

- `tools/venv/bin/python tools/p8.py extract --p8 production/2026-w47/2026-w47-zh-tw-it/svg/p8-test.svg --total 150` → `noted set = 150 of 150`，RC=0
- `tools/venv/bin/python tools/p8.py compare --core-p8 production/2026-w47/core-zh-tw/svg/p8-test.svg --edition-p8 production/2026-w47/2026-w47-zh-tw-it/svg/p8-test.svg --total 150` → `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[]`，RC=0
- 題號檢查（text.md）：編號行 300（題幹 150＋鍵注 150），1–150 無缺。

## 6. freeze 8/8

- `tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/2026-w47-zh-tw-it --core-svg production/2026-w47/2026-w47-zh-tw-it/svg --out /tmp/freeze-it` → `baseline: 8/8 SVGs byte-identical`，`core integrity: shipped core SVGs unchanged`，RC=0（重建在 /tmp 副本內完成）

## 7. checks.py（P7 金句／簡體／圖表）

- `cd production/2026-w47/2026-w47-zh-tw-it && tools/venv/bin/python checks.py` → `CHECKS PASS`，RC=0
  - 8 金句各 2 次；SIMP_ONLY_HITS []；P4 柱 [90.0, 450.0, 900.0]；P6 點 [188.0, 695.21, 948.82, 1033.36, 1202.43]
- 逐檔複驗：8 金句皆為「正文頁 1 次＋p7-lang.svg 1 次」。

## 8. abutting 掃描（網頁 PDF 缺口 >0.5pt 即缺陷）

- 方法：複製 `hidden_files/w47/scratch-webpdf-patch1/d2scan.py` 改路徑為本版（原檔未動），輸出 `/tmp/proof-it/d2-scan.json`
- `tools/venv/bin/python /tmp/proof-it/d2scan-it.py` → `abutting pairs with web gap >0.5pt: 9`（共掃 1,274 對；最差 2.33pt），RC=0
  - P2×2（2.26, 2.26）、P5×3（2.26, 2.33, 2.26）、P6×2（2.26, 2.33）、P7×2（1.58, 1.48），皆 Newsreader 數字串 vs 中文
- 對照：同法掃核心（網頁 PDF 2026-11-11 08:47 UTC 已補丁工具重建）→ `0`，RC=0
- 時序證據：`stat` 本版網頁 PDF 2026-11-11 02:51:03 UTC；`tools/webpdf.py` 08:33:18 UTC（含 `:weight=100/200` 補丁）；核心網頁 PDF 08:47:29 UTC。

## 9. 文字層完整性

- `pdftotext -layout` 印刷＋網頁（整份＋逐頁 P1–P8）→ RC=0；印刷 111,616 B／網頁 111,616 B
- 印刷 vs 網頁：非空白字符多重集整體＋逐頁皆一致（僅 P3 字面分段差異）；每頁 text.md 字符多重集 vs 印刷 PDF：md-only=0（8 頁皆然）；PDF 僅多刊頭 "Lucerna" 7 字符。
- P8 最小字號（PyMuPDF）：印刷 9.75pt／網頁 9.75pt；8 頁，1462.5×2025 pt。

## 10. 意大利語層抽驗

- 未縮合前置詞＋冠詞 27 式掃描（`di il`/`a la`/`in gli`…）：0 命中；縮合形 `del/al/dal/nel/della/nella/sullo` 俱全。
- `è tutti/ogni/in tutto` 全文 grep：5 處（P1 Note、P2 Note、P7 B2、P7 診所、鍵 70）＋SVG 複驗同數；`è alle` 3 處、`è il 22` 7 處、`è domenica` 6 處皆正確。
- 範答字數：142 字（CJK 121＋數字 5＋標點 16），與核心逐字一致。

## 11. 目檢

- 渲染卡 `cards/p4-sport.png`、`cards/p7-lang.png` 逐欄目檢：無溢出、重疊、頁腳碰撞；P4 `Parole del baseball` 折兩行在欄內。

## 12. 磁碟配額 EDQUOT（兩度發作）

- 約 08:48 UTC：`diff … > hidden_files/w47/scratch-proof-zh-tw-it1/diff-core-it.txt` → `Disk quota exceeded`，RC≠0；其後重探 `probe2.txt` 寫入成功，改以 /tmp 存放中間件繼續工作。
- 收尾約 09:1x UTC：`echo test | git hash-object` 成功（`9daeafb…`），但寫 `probe3.txt` → `Disk quota exceeded`；等待 60 秒後再探仍失敗，遂停手。PROOF-NOTE.md 與本 GATE-LOG.md 暫存 `/tmp/proof-it/`（tmpfs，未受配額影響），未寫入 `hidden_files/w47/scratch-proof-zh-tw-it1/`；待配額恢復後移入。
- 注意：`df -h` 顯示 /home/hatch 仍有 45G 空閒，屬配額（quota）而非磁碟滿，與 AGENTS.md 2026-11-10 條一致。
