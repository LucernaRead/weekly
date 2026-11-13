# GATE-LOG — 2026-W47 it-zh-tw proof2

獨立重跑記錄。全部命令用 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0，FreeType 2.14.3），`TMPDIR` 全程指向 scratch 下 `tmp/`，`PYTHONDONTWRITEBYTECODE=1`。生產目錄絕對路徑：`~/workspace/weekly-git/production/2026-w47/2026-w47-it-zh-tw/`；核心：`~/workspace/weekly-git/production/2026-w47/core-it/`。Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-it-zh-tw1/`。

## G0 開工探針

| 項 | 命令/操作 | 結果 |
|---|---|---|
| git probe | `git -C ~/workspace/weekly-git hash-object -w /dev/null` | `e69de29b…`，rc=0 |
| scratch 寫入 | 在 scratch 寫測試文件 | 成功 |

## G1 三 SHA 盤核（開工 + 收工各一次，兩次一致）

| 文件 | 大小 | SHA-256 | 與任務值 |
|---|---|---|---|
| `La-Lucerna-VOL4-ZH-TW.pdf` | 27,779,719 B | `79e51c537d9bcafb7612a056358cb9597c998ec84db1e16b183099ca98e5cfe8` | 一致 |
| `La-Lucerna-VOL4-ZH-TW-web.pdf` | 2,074,068 B | `a809a3a53ca7c0b6a462803bc7fd2cf65f5f99621a3d08b7b872ce6f49edaf79` | 一致 |
| `2026-w47-it-zh-tw.text.md` | 52,515 B | `681dff470eeb01dae8883e5c34773599290711c724e0ec741b59b82da8933e45` | 一致 |

## G2 幾何遮擋審計

| 項 | 命令 | 結果 |
|---|---|---|
| occlusion | `tools/occlusion_audit.py` on edition `svg/` | **0 flags**，rc=0；selftest 6 類全觸發 |
| 日誌 | `occlusion.log` | 0 flags |

## G3 P8 提取與比對

| 項 | 命令 | 結果 |
|---|---|---|
| extract 版 | `tools/p8.py` extract on edition svg | 150/150 noted |
| extract 核心 | `tools/p8.py` extract on core svg | 150/150 noted |
| compare | `tools/p8.py` compare | **CLEAN**；keydiff=[137, 138, 139]；missing=[]；extra=0；uncertain=[] |
| 日誌/JSON | `p8extract.log`、`p8extract-core.log`、`p8compare.log`、`p8-extract-zh-tw.json`、`p8-extract-core.json`、`p8-compare.json` | — |

## G4 freeze 基線與差分

| 項 | 命令 | 結果 |
|---|---|---|
| baseline | `tools/freeze.py baseline --build core-it --core-svg core-it/svg --out scratch/freeze-base` | **8/8 SVGs byte-identical**，rc=0；核心 SVG 運行後重驗無變 |
| diff | `tools/freeze.py diff`（core-it/svg vs edition svg） | rc=0；p1 +42/−40、p2 +16/−16、p3 +14/−14、p4 +15/−15、p5 +22/−22、p6 +14/−14、p7 +28/−28、p8 +169/−183；新增 CJK 970 |
| 碎片分類 | `freeze-fragments.txt` 541 行全讀 | 全部歸類：(i) 簡→繁讀者層替換（絕大多數）；(ii) P1 cifre 改寫（KIT §9 已登記）；(iii) 同文重排。**0 條未解釋；Italian 目標文無一字改動；proof1 D1–D5 舊文無殘留** |
| 日誌/JSON | `freeze-baseline.log/json`、`freeze-diff.log` | — |

## G5 副本重建（freeze.py baseline 路徑；生產源碼絕不直接跑）

| 項 | 命令/操作 | 結果 |
|---|---|---|
| 副本 | 整版複製至 `scratch/rerun/`，OUT/BASE 改向 scratch，grep 確認無 `weekly-git/production` 殘留 | build-copy 與核心僅差改向的 OUT/BASE 行 |
| run.py | `rerun/run.py` | rc=0；**TOTAL 150**；A2 47 / B1 70 / B2 33；頁 {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；範文 99 詞；P8-keys 末端 y=2484（底 2552） |
| SVG 重建 | 8 重建 SVG vs 生產 | **8/8 逐字節一致** |
| render.py | `rerun/render.py`（改向後） | rc=0；印 PDF **逐字節一致**（SHA `79e51c53…`，27,779,719 B）；cards PNG **8/8 逐字節一致** |
| 日誌 | `rerun-run.log`、`rerun-render.log` | — |

## G6 網 PDF 重渲與文字層比對

| 項 | 命令/操作 | 結果 |
|---|---|---|
| webpdf 重渲 | `tools/webpdf.py` from rerun SVG | rc=0；輸出 2,074,067 B（交付 2,074,068 B，**差 1 字節**） |
| 差異分析 | PyMuPDF 逐項比對交付 vs 重渲 | 8 頁、尺寸 1462.5×2025 pt、元數據（無日期）、229 xref、逐頁文字、7 嵌入圖、全部頁內容流均逐字節一致；僅 19 條字體子集 Flate 流壓縮長度差 1–2 字節 |
| 對照實驗 | 同批 SVG 數分鐘後第二次 webpdf | 又得另一 SHA（`05ec962b…`，首異字節同在 250316）→ **webpdf.py 輸出逐次不具位元組再現性**（字體子集壓縮非確定性），1 字節差不是內容差異 |
| 文字層 | `pdftotext` print / web / rerun-web | 三版**逐字節一致**（102,496 B，6,832 詞，詞多重集差 0/0） |
| 文件 | `rerun-web.pdf`、`rerun-web2.pdf`、`print.txt`、`web.txt`、`rerun-web.txt`、`rerun-webpdf.log` | — |

## G7 奶油盒掃描

| 項 | 命令 | 結果 |
|---|---|---|
| creambox | `hidden_files/w47/tools/creambox.py` on edition SVG | rc=0；框內最小餘量 **+3.9 px**（P3/P5 E TU）；9 個負「末基線」餘量均為視窗下 artefact（P1 ADESSO TU −37.0、LA PAROLA −24.0、QUIZ 副標 −44.0；P3 TORRAZZO −37.0；P4 表行 −40/−40/−26；P6 ESERCIZI −42 ×2）；desc-clear 最小 −2.1 px（末行無降部，裁圖目視確認在盒內） |
| 日誌 | `creambox-all.log`（355 行） | — |

## G8 自寫 PIL 掃（sweep.py / sweep2.py，canonical `occlusion_audit.ink_box`）

| 項 | 結果 |
|---|---|
| (a) 奶油盒標題 | **0 溢出**。最緊 P1 `LA SETTIMANA IN CIFRE　數字看本週` 墨至 960.0 vs 盒界 961.0（**餘 +1.0 px**）；次緊 P2 `LA FRASE PER RICORDARE　口訣` +43.0、P5 譯注 +19.5、P2 譯注 +26.5、P4 `LA CLASSIFICA　DOPO 11 GIORNATE` +29.0、P7 `ERRORI TIPICI　常見錯誤` +126.2、`LA PAROLA　本週生詞` +162.2 |
| (b) MARGIN+ | **0 行**（全頁墨右緣 ≤1861.4，P1 綠帶金字 svg y=419） |
| (b) MARGIN− | 87.8（左界 88 外 0.2 px），12 節點，核心同 12 節點同值——字體 sidebearing artefact |
| (c) FOOTER-BAND | 僅頁腳本身（`第N版／共8版`，基線 2624，按設計豁免） |
| 200 dpi 像素重測（P1 cifre 標題） | 波段 svg y 1336..1362（基線 1358.75）；墨至 svg **959.0**，奶油緣 **960.5**，**餘 +1.4 px**——與 PIL +1.0 一致，通過（見 PROOF-NOTE O1）。註：首次掃描誤用波段（基線 1388.475，實為 cifre 首行）得餘 21.1 px 已作廢，不採用 |
| (d) P1 副標 | `本週日程　Cosa succede, giorno per giorno` 墨至 1839.2，餘 +22.8 px |
| fix3 針對重測 | P2 25–28 b `b. il ponte di barche per la festa in` 餘 +31.0、d `d. la piccola luce di cera accesa in` 餘 +40.2；P4 52–55 b `b. che non ha mai perso`、c `c. il gruppo di squadre in un torneo` 餘 +17.5；P8 F 141–144 a/b/c/d 餘 +34.0/+51.5/+24.0/+18.0——**全部修復** |
| gutter 精掃（sweep2.py） | P1/P2/P3/P5/P8 **0 候選**；P4 3 條（賽果表行 +10.2~+11.0，無碰撞）；P6 3 條（寬盒內部）；P7 1 條（`…演員。 (Pagina 3)` +22.8，間隙 455.8 px） |
| 日誌 | `sweep.log`、`sweep.txt`、`sweep2.log`、`sweep2.txt`、`sweep.py`、`sweep2.py` |

## G9 孤兒掃

| 旗標 | 裁定 |
|---|---|
| P5 piano `（週日` | 分組 artefact；全頁渲染顯示 gloss `(週日 20:45：亞特蘭大對國米）` 完整在一行 |
| P6 譯注 `序。` | CJK 正常換行 |
| P6 時間線 `18.` | `…alle ore / 18.`，完整可讀 |
| P8 Q129 `due` | 核心繼承義大利語換行（`C. i / due`）；freeze diff 證實 stem 未動 |
| P8 Q137 `___` | 答題空行設計 |

## G10 pdfscan（PyMuPDF span，交付印 PDF 本身）

| 頁 | spans | 最小字 | 右緣超限 | 備註 |
|---|---|---|---|---|
| p1 | 276 | 11.62 pt | +0.2 pt（`2026`） | side-bearing artefact |
| p2 | 191 | 11.62 pt | +1.6 pt（副標） | 同上 |
| p3 | 189 | 11.62 pt | 0 | — |
| p4 | 186 | 11.62 pt | 0 | — |
| p5 | 182 | 11.62 pt | +1.6 pt（圖注） | 同上 |
| p6 | 206 | 12.75 pt | 0 | — |
| p7 | 172 | 11.62 pt | 0 | — |
| p8 | 738 | **9.75 pt** | +1.8/+1.9 pt（範文行） | 同上；**9.75 pt = SOP §1.1 下限，通過** |

左緣超限：全頁 0。PIL 真墨右緣全頁 ≤1861.4（界 1862）。

## G11 §1.1 乾淨掃

| 項 | 結果 |
|---|---|
| 顏色 | 調色內全部 SOP §1.1 色；非調色填色僅飛蛾 logo 內部（P1）與深綠帶淺米字 `#cac8ba`（P1 綠帶副標、P7 綠帶預告條，核心同款）；無金/磚/近黑色頁面元素 |
| 字體 | Newsreader ×1193、Noto Sans CJK TC ×611、Noto Serif CJK TC ×283、UnifrakturMaguntia ×1 |
| 頁規 | 8 頁，1462.5×2025 pt，1950×2700 px，4 欄 |
| VOL | `VOL.4` ×9（8 頁腳 + 刊頭），`VOL.5` ×3（合法節點） |
| ABSTRACT.txt | 一行 323 B，繁體中文，無 ASCII 雙引號，含 La Lucerna + VOL.4，事實與本期一致 |
| 英文殘留 | `Translate` text.md + 8 SVG 均 0；`LUCERNA ITALIAN WEEKLY` 8 SVG 均 0；簡體 `译` 0 |
| text.md 雙向驗證 | `validate_edition_textmd.py <dir> 2026-w47-it-zh-tw` rc=0：**forward-miss 0 / reverse-miss 0**（`textmd-validate.log`） |

## G12 內容實證（全量手驗）

| 項 | 結果 |
|---|---|
| text.md 通讀 | 1317 行全讀 |
| 150 鍵三源 | RISPOSTE vs P8 印出鍵 149/149 一致；#150 僅記法差異（同義）；行內 stem 鍵 138 個 0 錯；分組 P2 25–28、P4 52–55、P8 F 141–144 全部手驗正確 |
| 日期/星期 | `date -d`（Europe/Rome）：Nov 6–8、12、16–22、23、24、Dec 2、Dec 6、Dec 31 全部核對通過 |
| 算術 | MD11 10 場 24 球；榜 Lazio 29/Inter 28/Roma 27；Roma 31 球；13−11=2、6+7=13；BookCity 1360/2487/1164/443；manovra 數值全部重算通過；範文 99 詞（程式計數）；頭條 39 非空格字元 |
| 8 金句 | 每句 text.md 恰 2 次，逐字一致 |
| keydiff | 版 vs 核心恰 [137, 138, 139]；Q140 兩版皆義大利語，無差異為正確行為 |
| 標題數 | T1 size≥40 17 個；T2 粗體≥21 270 個；T3 `## ` 8 個；T4 全大寫行 54 個（扣表/時間線標籤後 48 個欄/盒標題）；正文頭條 6 條。**無任何定義得出 56** |
| 8 頁目視 | 交付印 PDF 100 dpi 全頁（`pages/p-1.png`–`p-8.png`）逐頁目視 + 200 dpi 裁圖（`crop-p2-match.png`、`crop-p4-match.png`、`crop-p8-f.png`、`crop-p7-errori.png`、`crop-p3-etu-bottom.png`、`crop-p5-etu-bottom.png`、`crop-p1-cifre.png`（正確波段重裁））：無溢出、重疊、頁腳侵入、豆腐 |
| KIT 核對 | WEEKLY-KIT.md §1–§11 全讀；數值/聲稱與本報告實測一致，無不準之處 |

## G13 收工完整性

| 項 | 結果 |
|---|---|
| 三 SHA 重驗 | 與任務值一致（`sha256sum`，見 G1） |
| 8 生產 SVG 重驗 | 與開工基線逐字節一致（`prod-svg-final.txt` vs `baseline-prod-hashes.txt`） |
| 8 生產 cards 重驗 | 與開工基線逐字節一致（`prod-cards-final.txt`） |
| git status | 生產目錄無追蹤修改（該目錄本就未追蹤） |
| 寫入紀律 | 全部構建在 scratch 副本；OUT/BASE 改向經 grep 確認；`PYTHONDONTWRITEBYTECODE=1`；生產無 `__pycache__` 寫入；零 commit、零 push |

## 缺陷清單

**無缺陷。** 觀察項 16 項見 PROOF-NOTE §5（O1–O16），均不計缺陷。
