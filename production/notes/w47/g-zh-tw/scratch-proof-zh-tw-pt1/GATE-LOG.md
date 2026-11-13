# GATE-LOG — 2026-W47 zh-tw-pt proof1（重建後版，獨立復校）

執行：2026-11-11 11:59–12:20 UTC。全部 Python 門禁一律 `~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3，Pillow 13.0.0），絕無系統 python3。TMPDIR=`scratch-proof-zh-tw-pt1/tmp`。工作目錄 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-zh-tw-pt1/`。日誌本體：`gates/pt-proof1/`。

| # | 門禁 | 命令（要點） | RC | 結果 |
|---|---|---|---|---|
| 0 | 探針 | `echo test \| git -C ~/workspace/weekly-git hash-object -w --stdin` + 寫 `.probe` | 0 | `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；寫盤成功才開工 |
| 1 | 身份 SHA | `sha256sum` + `stat` 三件（印/網/text.md） | 0 | 印 `6302ea7c…` 20,944,900 B；網 `4a257e9f…` 2,412,857 B；text `02387ce2…` 51,492 B；與任務給定及 refanout §5 一致 |
| 2 | 核心對照 SHA | `sha256sum production/2026-w47/core-zh-tw/*` | 0 | 印 `5ec35fe2…`、網 `1c0799ac…`、text `09e083e1…`，與任務給定前綴一致，重建前後未變 |
| 3 | freeze baseline（第一步） | `tools/venv/bin/python tools/freeze.py baseline --build . --core-svg svg --out gates/pt-proof1/freeze-base`（cwd=版目錄） | 0 | **8/8** SVG 字節一致；核心 SVG 重建前後未變（`gates/pt-proof1/freeze.log`；另驅動內第二次 freeze 同為 8/8） |
| 4 | 全套門禁驅動 | `tools/venv/bin/python gates-pt.py pt proof1`（`gates.py` 的本 scratch 副本：輸出改至本 scratch，兩處 system python3 改為 VENV）→ `gates/pt-proof1/gates.json` + 各門日誌 | 0 | 見下分項 4a–4l |
| 4a | checks.py | VENV `checks.py`（cwd=版目錄） | 0 | **CHECKS PASS**；P4 bars [90.0, 450.0, 900.0]、P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]；SIMP_ONLY_HITS []（`checks.log`） |
| 4b | occlusion | VENV `tools/occlusion_audit.py --selftest` + `--json occlusion.json <版>/svg` | 0 | 自測 rc 0；**flags 0**（`occlusion-selftest.log`、`occlusion.log`、`occlusion.json`） |
| 4c | p8 extract + compare | VENV `tools/p8.py extract --p8 <版>/svg/p8-test.svg --total 150 --json p8-extract.json`；`compare --core-p8 core-zh-tw/svg/p8-test.svg --edition-p8 <版>/svg/p8-test.svg --total 150 --json p8-compare.json` | 0 | extract noted 150/150；compare **CLEAN**，missing []、extra []、keydiff []（註：驅動 gates.json 內 `extra: "?"` 為 refanout §7 已載明的驅動讀 key bug，實測 `p8-compare.json` 為 `"extra": []`） |
| 4d | canonical creambox | VENV `hidden_files/w47/tools/creambox.py <版>/svg/*.svg` | 0 | 36 盒；負清除 []；各頁最小內清除 P1 18.8 / P2 15.8 / P3 15.8 / P4 35.8 / P5 6.4 / P6 19.9 / P7 12.5；P7 工具盒 +40.5 / +12.5 / +14.0（`creambox.log`、`creambox.json`） |
| 4e | boxtitle | VENV `gtools/boxtitle.py <版>/svg gates/pt-proof1` | 0 | 36 盒；超框 0；最小標題右余 **9.5px**（`boxtitle.log`、`boxtitle.json`，全 36 盒逐盒見 PROOF-NOTE §4） |
| 4f | PIL creambox | VENV `gtools/creambox-pil.py <版>/svg gates/pt-proof1` | 0 | **STRADDLE 3**、CREAM-COVER 0、P7 最小清除 8.0（`creambox-pil.log`） |
| 4g | 印/網文字層 | `pdftotext -layout` 印/網 → `print.txt` / `web.txt` + 多重集比對 | 0 | 各 102,844 B；多重集差 **0**；計數兩版一致（本週日 11、下週日 0、BABYMONSTER 0、取捨 2、end point 0、小雪 36） |
| 4h | PDF 指標（PyMuPDF） | fitz span 掃描印/網兩版 | 0 | 各 8 頁、1462.5×2025 pt；P8 最小字號 **9.75pt**（最大 34.5pt）；P1 最大字號 147.0pt（刊頭字標） |
| 4i | keycheck | VENV `gtools/check_fillin_keys.py <版>/<slug>.text.md <版>` + keys 1–150 連續性 | 0 | 填空鍵 **54**，MISS 行 []；keys 1–150 連續（150 個）（`fillin-check.log`） |
| 4j | 泄漏掃描 | deny 串（含 next Sunday/Next Sunday/英文殘句）+ 長 ASCII 串與核心比對 | 0 | deny_hits {}；共享長 ASCII 僅「A. 12:00 · B. 14:00 · C. 19:00」（Q140 選項，核心同文） |
| 4k | abutting | P6「頒獎典禮」/「夜間遊行」標籤墨縫（occlusion_audit 解析） | 0 | **0.6px**（990.8 → 991.4） |
| 4l | 文件 SHA | gates 驅動內 hashlib 復核三件 | 0 | 與 #1 完全一致；8 個 SVG SHA 見 `gates.json`（與 freeze 核心 hash 一致） |
| 5 | 舊版 STRADDLE 對照 | VENV `gtools/creambox-pil.py <舊備份>/svg gates/pt-proof1/old-check`（備份：`scratch-refanout-zh-tw/backup/2026-w47-zh-tw-pt/svg`） | 0 | 舊版同為 STRADDLE **3**，文字與坐標逐像素相同（+38.0/+12.0/+44.2）；CREAM-COVER 0 |
| 6 | STRADDLE 幾何掃查 | VENV 解析 SVG：三處超框區 x 1862–1906.2 內 rect/line/text | 0 | 除整頁底色矩形（1950×2700 #fbfaf6）外無任何元素；無裁切（最右 1906.2 < 1950）、無壓線 |
| 7 | 自渲染 8 頁 | `pdftoppm -png -r 100 <印PDF> render/p` | 0 | p-1.png … p-8.png，逐頁目視通過（見 PROOF-NOTE §5） |
| 8 | STRADDLE 高倍裁切 | fitz：P2/P3 三處 clip 3× 渲染 `render/straddle-p2.png`、`straddle-p3a.png`、`straddle-p3b.png` | 0 | 三處末字完整、落在空白紙面、無壓線（見 PROOF-NOTE §6） |
| 9 | 印/網 span 位置差分 | fitz：兩版 span (page, bbox, size, text) 多重集比對 | 0 | 各 3,167 spans；僅 1 處不同：P1「Lucerna」刊頭字標 bbox（印 499.1–956.9/62.8–209.8；網 501.7–960.2/81.3–233.2）；其餘 3,166 一致 |
| 10 | text.md 全文通讀 | `muse.read` 6,058 行分段全讀（L1–L6058） | — | 全文通讀完畢；見 PROOF-NOTE §7–§9 |
| 11 | 150 題三源核對 | p8 extract keys × text.md 答案區解析 × 正文手驗 → `keycheck-150.json`（另 `keycheck-raw.json`） | 0 | SVG vs text.md 鍵 **150/150 一致**（Q150 僅 `✓` vs `✓ Tarefa aberta` 同義文字差）；手驗 150/150 正確，0 缺陷；F 範文 142 字 |
| 12 | 模型範文計數 | text.md F 節 Resposta modelo 去空白計數 | — | **142 字**（120–180 帶內），與 P8 注一致 |
| 13 | 引號/簡體/標籤掃查 | VENV：直引號、彎引號、簡體字專表、E 節標籤、凍結 key（tables.py:245/:267/:322、core content12.py:37/:113、content34.py:127） | — | 直引號 0、彎引號 0（全文用「」）；簡體字專表 SVG/text.md 均 0；E 節六標籤繁體齊全；凍結 key 三處在（非缺陷，re-proof #3 已認證） |
| 14 | 舊 D1/D2 閉合復驗 | grep 四源：text.md / SVG / 印文字層 / 網文字層 | — | 下週日 0 / 本週日 11（四源一致）；BABYMONSTER 0（四源一致）；`próximo domingo` 0、`este domingo` 3；殘留「下週」2 次皆 P7 下期預告（正確） |
| 15 | 6 條 P8 預補譯核對 | grep/合併 tspan 提取 p8-test.svg | — | `A cerimônia é no Taipei Music Center.` 1×、`Xiaoxue é 22 de nov.` 3×（Q98/Q117/Q138）、`Quatro grandes eventos caem no mesmo domingo.` 1×、`Acumular pontos é 集點。` 1×（Q134）——齊全 |
| 16 | KIT 核對 | grep 新/舊 SHA 於 `WEEKLY-KIT.md` | — | 新三件 SHA + 字節在；舊 SHA 0 殘留；H1 葡語正確 |
| 17 | 外部事實核查 | `browser.search` 10 組查詢（金馬/味全龍/U-Sport/小雪/耶誕城/迪士尼/爵士/寶可夢/圓方/鋼雕/六福村） | — | 全部屬實，見 PROOF-NOTE §8（含來源 URL） |
| 18 | 磁碟 | `df -h /home/hatch` | — | 150G 盤，80G 已用，**70G 空閒**（54%）；寫盤全程無 quota 報錯（舊輪 EDQUOT 已消除） |

## 未做事項（依任務紅線）

未改生產文件、未重建、未 commit、未 push；僅在 `production/2026-w47/`（讀）與 `hidden_files/w47/`（寫本 scratch）內活動。舊輪 PROOF-NOTE/GATE-LOG 原樣保留為 `PROOF-NOTE-old-pre-refanout.md` / `GATE-LOG-old-pre-refanout.md`。
