# D5 重建報告 — 2026-w47-es-zh-tw

日期：2026-11-12（UTC ~09:45–10:10）。構建解釋器全程 `tools/venv/bin/python`。CJK 讀者版（裁定 §1：按字符文字分流，不加 `_READER_LANG` 門）。

## 安裝
- `mechanism/apply_variant.py --svglib <版>/svglib.py --target es --reader zh-tw`（mode=cjk）。
- `svglib.py` md5 `6a46ee51…` → `04b42710…`（安裝器同時補 port 了 fix2）；路由斷言 10/10；機制 `test_d5_routing.py` FAILURES: 0。
- 修前基線（`pre.sh` 新建，因 scratch 原無 CJK 基線目錄）：印 17,263,265 B `ef5f1cde…`、網 1,725,941 B `9208bd35…`；D5 普查 347 violations（與裁定 §1.1 預期 347 一致）；boxtitle 0 DEFECT；occlusion 0。

## 預修（與 core-es 相同的 3 項共用版式）
P1 欄頭 `UNA SEMANA, TRES ESCENARIOS` 25→23pt；P3 欄頭 `LO QUE QUEDA DE NOVIEMBRE` 25→24pt；P3 手工題 `EL FLAMENCO, EN TRES DATOS` 24→23pt。

## 逐項修（D5 新缺陷，CJK 類）
- P1 框題 `LA SEMANA EN CIFRAS　數字看本週` +22.5px → 該框 `tsize=21`（餘量 14.7px）。
- P5 框題 `EL PLAN DE LA SEMANA　本週計劃` +13.7px → 該框 `tsize=21`（22pt 餘量僅 4.5px，取 21 求穩）。以上文字均未動。注：ink=advance（尾字為全角 CJK），框題可用寬 404.5px。

## 門禁（最終版全綠）
- run TOTAL 150，0 FLOW OVERFLOW，HEAD TOO WIDE 0；head_check PASS 0 defects；render rc=0。
- D5 普查 0；U+201C 普查 0。
- occlusion 0 flags；p8 extract 150/150；p8 compare vs 新 core-es CLEAN，keydiff=[137, 138]（僅讀者語譯註）。
- boxtitle 0 DEFECT；creambox（tools 版）PASS 0 defects（P8 241 行、餘量 38.9px 不變）。
- spill 0；edge 0 TOUCH/0 NEAR；freeze baseline 8/8；freeze diff vs core-es 新增 CJK 字符 955 個（繁體讀者層相對 core-es 簡體讀者層的正當差異）；同版 freeze diff（修前基線 vs 新版）新增 CJK 字符僅 1 個 U+3000。
- 印/網文字層 37,931 字符、7,268 詞，逐字一致。

## 交付
- 印刷版 `La-Lucerna-VOL4-es-zh-tw.pdf` 4,381,574 B，SHA-256 `9a60b0786b1cf2f12ff9d2df94a7b28b3d2176ecf9385deb51d4814078555902`。
- 網頁版 `La-Lucerna-VOL4-es-zh-tw-web.pdf` 1,265,855 B，SHA-256 `4851fee5b3a41a17ea7bfc6aab26188b6297b1826eaeb7ba61eb8e6125df594a`。
- `text.md` 字節不變（SHA `930fc2ba…`）。
- KIT 已更新（§1 交付行 + 尾部 D5 記錄）。日誌在本目錄；freeze build-copy 已刪。
