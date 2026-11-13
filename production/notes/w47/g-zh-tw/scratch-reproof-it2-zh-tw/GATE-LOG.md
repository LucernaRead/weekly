# GATE-LOG — 2026-W47 it-zh-tw 重擴散 2 後獨立復校

獨立重跑記錄。全部命令用 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0，FreeType 2.14.3），`TMPDIR` 全程指向 scratch 下 `tmp/`，`PYTHONDONTWRITEBYTECODE=1`。生產目錄絕對路徑：`~/workspace/weekly-git/production/2026-w47/2026-w47-it-zh-tw/`；核心：`~/workspace/weekly-git/production/2026-w47/core-it/`；修前備份：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-refanout-it2/backup/2026-w47-it-zh-tw/`。Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it2-zh-tw/`。

## G0 開工探針

| 項 | 命令/操作 | 結果 |
|---|---|---|
| git probe | `git -C ~/workspace/weekly-git hash-object -w /dev/null` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，rc=0 |
| scratch 寫入 | 在 scratch 寫測試文件 | 成功（`probe.txt`） |

## G1 三 SHA 盤核（開工 + 收工各一次，兩次一致；文件名與任務書逐字一致）

| 文件 | 大小 | SHA-256 | 與任務值 |
|---|---|---|---|
| `La-Lucerna-VOL4-ZH-TW.pdf` | 27,779,699 B | `96aa320738b09cf89c18fbb63789c38225017feb8969db98c1fedb44041d1531` | 一致 |
| `La-Lucerna-VOL4-ZH-TW-web.pdf` | 2,074,045 B | `1f5730490f765d75d9c1317c6ef65734ab8d9453541161b271591660b109a1a9` | 一致 |
| `2026-w47-it-zh-tw.text.md` | 52,494 B | `c18ad203cf49356079c4403e69b7366b1f36109963eadbcce17058da08dd8432` | 一致 |

修前生產三 SHA（`scratch-refanout-it2/shas-pre.txt` + 備份 `backup.sha256` 校驗通過）：印 `79e51c537d9bcafb7612a056358cb9597c998ec84db1e16b183099ca98e5cfe8`（27,779,719 B）、網 `a809a3a53ca7c0b6a462803bc7fd2cf65f5f99621a3d08b7b872ce6f49edaf79`（2,074,068 B）、文 `681dff470eeb01dae8883e5c34773599290711c724e0ec741b59b82da8933e45`（52,515 B）。text.md 字节差 −21，恰為 D-2 刪去的 `andare → andrò, `。

## G2 D-2 回歸（逐項獨立重測，見 PROOF-NOTE §4 A/C）

| 項 | 結果 |
|---|---|
| 新串 text.md:775/:777 | 各 ×1，逐字一致 |
| 新串 content7.py:17/:18 | 各 ×1，逐字一致 |
| 新串 p7 SVG | 各 ×1（新 3 節點，皆為兩句的子串） |
| 新串印/網 PDF P7 文字層 | 各 ×1（空白摺疊計數；樸素計數因行間 `\n` 誤為 0，見 O23） |
| 舊串 `Le forme sono regolari: andare` / `irregolare al futuro: leggerò` | content*.py、8 SVG、text.md、兩 PDF 全文文字層均 0；`andrò` 在 text.md 與 p7 SVG 均 0 |
| 與修前備份 diff | text.md 恰 :775/:777 兩行；SVG 僅 p7、cards 僅 p7；content 僅 content7.py:17/:18；其餘逐字一致 |
| P7 教學語義 | `regolar` 全版僅 2 次（皆為修正句），`irregolar` 0 次；assaggiare/guardare/leggere 規則標籤皆正確；B1/B2 段逐句核對正確 |
| 核心三 SHA 盤核 | 印 `e1f89922…` / 網 `09f2ef66…` / 文 `9eb9ee06…`，與 KIT §12 一致；核心 p7 `a7e6afa4…` 與 FIX-LOG 定稿值一致 |

## G3 幾何遮擋審計

| 項 | 命令 | 結果 |
|---|---|---|
| occlusion | `tools/occlusion_audit.py` on edition `svg/` | **0 flags**，rc=0；selftest 6 類全觸發 |
| 日誌 | `occlusion.log` | 0 flags |

## G4 P8 提取與比對

| 項 | 命令 | 結果 |
|---|---|---|
| extract 版 | `tools/p8.py extract --p8 <edition>/svg/p8-valutazione.svg --total 150` | 150/150 noted |
| extract 核心 | `tools/p8.py extract --p8 <core>/svg/p8-valutazione.svg --total 150` | 150/150 noted |
| compare | `tools/p8.py compare --core-dir core-it --edition-dir <edition> --target it --total 150` | **CLEAN**；keydiff=[137, 138, 139]；missing=[]；extra=0；uncertain=[] |
| 日誌/JSON | `p8extract.log`、`p8extract-core.log`、`p8compare.log`、`p8-extract-zh-tw.json`、`p8-extract-core.json`、`p8-compare.json` | — |

## G5 freeze 基線與差分

| 項 | 命令 | 結果 |
|---|---|---|
| baseline | `tools/freeze.py baseline --build <core-it 絕對路徑> --core-svg <core-it>/svg --out scratch/freeze-base` | **8/8 SVGs byte-identical**，rc=0；build-copy 驗為 core-it 自身（改向 6 文件，0 生產路徑殘留）；核心 SVG 運行後重驗無變；核心 p7 `a7e6afa4…` 精確復現 |
| diff | `tools/freeze.py diff --core-svg <core-it>/svg --edition-svg <edition>/svg` | rc=0；p1 +42/−40、p2 +16/−16、p3 +14/−14、p4 +15/−15、p5 +24/−24、p6 +14/−14、p7 +28/−28、p8 +169/−183；新增 CJK 970 |
| 碎片分類 | `freeze-diff.json` 322 added + 320 removed 全部分類（`freeze-wordcheck.txt` 拉丁詞多重集 + `plus-check.txt`/`plus-ctx.txt`） | 全部歸類：(i) 簡→繁讀者層替換；(ii) P1 cifre 改寫（KIT §9 已登記）；(iii) P8 44/134 註釋縮短（KIT §9 已登記）；(iv) 頁眉英文 kicker 取代；(v) 同文重排。**0 條未解釋；Italian 目標文無一字改動** |
| 日誌/JSON | `freeze-baseline.log/json`、`freeze-diff.log/json`、`freeze-diff2.log` | — |
| 註 | 首次 baseline 因 `--build` 傳相對路徑報 FileNotFoundError（rc=1，工具未寫任何文件），改傳 core-it 絕對路徑後通過；此為調用錯誤，非門禁失敗 | — |

## G6 副本重建（生產源碼絕不直接跑；OUT/BASE 改向 scratch，grep 確認 0 處 `weekly-git/production` 殘留）

| 項 | 命令/操作 | 結果 |
|---|---|---|
| 副本 | 整版複製至 `scratch/rerun/`，OUT/BASE 改向 scratch | build-copy 與生產僅差改向的 OUT/BASE 行 |
| run.py | `rerun/run.py` | rc=0；**TOTAL 150**；A2 47 / B1 70 / B2 33；頁 {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；範文 99 詞；P8-keys 末端 y=2484（底 2552）；P7 col3 末端 1644.0；P4 col3 末端 1140.45 |
| SVG 重建 | 8 重建 SVG vs 生產 | **8/8 逐字一致** |
| render.py | `rerun/render.py`（改向後） | rc=0；印 PDF **逐字一致**（SHA `96aa3207…`，27,779,699 B）；cards PNG **8/8 逐字一致** |
| 日誌 | `rerun-run.log`、`rerun-render.log` | — |

## G7 網 PDF 重渲與文字層比對

| 項 | 命令 | 結果 |
|---|---|---|
| webpdf 重渲 | `tools/webpdf.py rerun/svg rerun-web.pdf` | rc=0；輸出 2,074,040 B（交付 2,074,045 B，**差 5 字節**） |
| 差異分析 | `pdftotext` 三版比對 | 預設模式三版**逐字一致**（44,052 B）；`-layout` 模式三版**逐字一致**（102,508 B）；空白分隔 token 6,830（見 O18） |
| 文字層 | print == web == rerun-web | 逐字一致；5 字節差為字體子集壓縮非確定性（同 proof2 O15），非內容差異 |
| 文件 | `rerun-web.pdf`、`print.txt`、`web.txt`、`rerun-web.txt`、`rerun-webpdf.log` | —（`-layout` 三版曾誤寫至 `~` 根，已刪） |

## G8 奶油盒掃描

| 項 | 命令 | 結果 |
|---|---|---|
| creambox | `hidden_files/w47/tools/creambox.py <edition>/svg/*.svg` | rc=0；框內最小餘量 **+3.9 px**（P3/P5 E TU）；9 個負「末基線」餘量與 proof2 同值同模式（P1 ADESSO TU −37.0、LA PAROLA −24.0、QUIZ 副標 −44.0；P3 TORRAZZO −37.0；P4 表行 −40/−40/−26；P6 ESERCIZI −42 ×2）；desc-clear 最小 −2.1 px（末行無降部，目視確認在盒內） |
| 日誌 | `creambox-all.log` | — |

## G9 自寫 PIL 掃（sweep.py / sweep2.py，canonical `occlusion_audit.ink_box`；proof2 腳本拷貝，僅 OUT 路徑改向本 scratch）

| 項 | 結果 |
|---|---|
| (a) 奶油盒標題 | **0 溢出**。最緊 P1 `LA SETTIMANA IN CIFRE　數字看本週` 墨至 960.0 vs 盒界 961.0（**餘 +1.0 px**）；次緊 P2 `LA FRASE PER RICORDARE　口訣` +43.0、P5 譯注 +19.5、P2 譯注 +26.5、P4 `LA CLASSIFICA　DOPO 11 GIORNATE` +29.0、P7 `ERRORI TIPICI　常見錯誤` +126.2 |
| O1 像素重測（200 dpi，正確波段 svg y 1336..1362，限盒內 x） | 墨至 svg **959.0**，奶油緣 **960.5**，**餘 +1.5 px**（閾值 100/140/180/200 同值）；備份舊版同法重測同為 959.0，無回歸 |
| (b) MARGIN+ | **0 行**（全頁墨右緣 ≤1861.4，P1 綠帶金字 svg y=419） |
| (b) MARGIN− | 87.8（左界 88 外 0.2 px），12 節點，核心同 12 節點同值——字體 sidebearing artefact |
| (c) FOOTER-BAND | 僅頁腳本身（`第N版／共8版`，基線 2624，按設計豁免） |
| (d) fix3 針對重測 | P2 25–28 b `b. il ponte di barche per la festa in`、d `d. la piccola luce di cera accesa in`；P4 52–55 b `b. che non ha mai perso`、c `c. il gruppo di squadre in un torneo`；P8 F 141–144 a/b/c/d——全部在欄內，值與 proof2 一致 |
| (g) P1 副標 | `本週日程　Cosa succede, giorno per giorno` 墨至 1839.2，餘 +22.8 px |
| gutter 精掃（sweep2.py） | P1/P2/P3/P5/P8 **0 候選**；P4 3 條（賽果表行 +10.2~+11.0，無碰撞）；P6 3 條（寬盒內部）；P7 1 條（`…演員。 (Pagina 3)` +22.8，間隙 455.8 px） |
| (e) P8 字號 | 最小 13.0 svg px = **9.75 pt**（SOP §1.1 下限） |
| 日誌 | `sweep.log`、`sweep.txt`、`sweep2.log`、`sweep2.txt`、`sweep.py`、`sweep2.py` |

## G10 孤兒掃

| 旗標 | 裁定 |
|---|---|
| P5 piano `（週日` | 分組 artefact；全頁渲染顯示 gloss `(週日 20:45：亞特蘭大對國米）` 完整在一行 |
| P6 譯注 `序。` | CJK 正常換行 |
| P6 時間線 `18.` | `…alle ore / 18.`，完整可讀 |
| P8 Q129 `due` | 核心繼承義大利語換行（`C. i / due`）；freeze diff 證實 stem 未動 |
| P8 Q137 `___` | 答題空行設計 |

## G11 pdfscan（PyMuPDF span，交付印 PDF 本身）

| 頁 | spans | 最小字 | 右緣超限 | 備註 |
|---|---|---|---|---|
| p1 | 276 | 11.62 pt | +0.2 pt（`2026`） | side-bearing artefact |
| p2 | 191 | 11.62 pt | +1.6 pt（副標） | 同上 |
| p3 | 189 | 11.62 pt | 0 | — |
| p4 | 186 | 11.62 pt | 0 | — |
| p5 | 182 | 11.62 pt | +1.6 pt（圖注） | 同上 |
| p6 | 206 | 12.75 pt | 0 | — |
| p7 | 168 | 11.62 pt | 0 | —（proof2 172，差 4 為 D-2 刪節點，見 O20） |
| p8 | 738 | **9.75 pt** | +1.8/+1.9 pt（範文行） | 同上；**9.75 pt = SOP §1.1 下限，通過** |

左緣超限：全頁 0。PIL 真墨右緣全頁 ≤1861.4（界 1862）。

## G12 §1.1 乾淨掃

| 項 | 結果 |
|---|---|
| 顏色 | 調色內全部 SOP §1.1 色（`#302c28` ×1417、`#46581f` ×379、`#6f675d` ×236、徽章 `#5c6e30`/`#37402f`、奶油 `#f0eee5`、紙 `#fbfaf6`、鵝黃 `#f6e08e`）；非調色填色僅飛蛾 logo 內部（P1，含 proof2 未列的 `#34483A`/`#F1E8D4`/`#4F765D`/`#84A283`，見 O22）與深綠帶淺米字 `#cac8ba` ×2（核心同款）及白色徽章字 `#ffffff` ×141；無金/磚/近黑色頁面元素 |
| 字體 | Newsreader ×1188、Noto Sans CJK TC ×611、Noto Serif CJK TC ×282、UnifrakturMaguntia ×1（vs 備份 −5/−1，D-2 刪節點所致，見 O21） |
| 頁規 | 8 頁，1462.5×2025 pt，1950×2700 px，4 欄 |
| VOL | `VOL.4` ×9（8 頁腳 + 刊頭），`VOL.5` ×3（合法節點） |
| ABSTRACT.txt | 一行 323 B，繁體中文，無 ASCII 雙引號，含 La Lucerna + VOL.4，事實與本期一致；與 KIT §7 引文逐字相符 |
| 英文殘留 | `Translate` text.md + 8 SVG 均 0；`LUCERNA ITALIAN WEEKLY` 核心 8 處、本版 0 處；簡體 `译` 0 |
| text.md 雙向驗證 | `validate_edition_textmd.py <dir> 2026-w47-it-zh-tw` rc=0：**forward-miss 0 / reverse-miss 0**（`textmd-validate.log`） |

## G13 內容實證（全量手驗）

| 項 | 結果 |
|---|---|
| text.md 通讀 | 1317 行全讀 |
| 150 鍵三源 | stem 150/150、RISPOSTE 150/150、P8 印出鍵 150/150，三源 0 不符；#150 僅記法差異（同義）；分組 P2 25–28、P4 52–55、P8 F 141–144、Q101–104 全部手驗正確（`keycheck.txt`） |
| 日期/星期 | `date -d`（Europe/Rome）：Nov 6–8、12、16–22、23、24、Dec 2、Dec 6、Dec 31 全部核對通過 |
| 算術 | MD11 10 場 24 球（逐場相加）；榜 Lazio 29/Inter 28/Roma 27；Roma 31 球；13−11=2、6+7=13；BookCity 1360/2487/1164/443；TFF Nov 24–Dec 2 共 9 天；manovra 數值全部在位；範文 99 詞（程式計數 + run.py 印證）；頭條 39 非空格字元 |
| 8 金句 | 每句 text.md 恰 2 次，逐字一致（`facts-check.txt`） |
| keydiff | 版 vs 核心恰 [137, 138, 139]；Q140 兩版皆義大利語，無差異為正確行為 |
| 8 頁目視 | 交付印 PDF 100 dpi 全頁（`pages/p-1.png`–`p-8.png`）逐頁目視 + 200 dpi 裁圖（`pages/crop-p7-a2.png` D-2 兩句、`pages/crop-p1-cifre.png` cifre 盒）：無溢出、重疊、頁腳侵入、豆腐 |
| KIT 核對 | WEEKLY-KIT.md §1–§12 全讀；數值/聲稱與本報告實測一致，僅 O17/O18 兩處 1 token 級計數口徑差 |
| 門禁總計 | **19/19 PASS**（CJK 版無 strict-CJK 項） |

## G14 收工完整性

| 項 | 結果 |
|---|---|
| 三 SHA 重驗 | 與任務值一致（`sha256sum`，見 G1） |
| 8 生產 SVG + 8 cards 重驗 | 與開工基線逐字一致（`prod-svg-final.txt` vs `baseline-prod-hashes.txt`） |
| git status | 本版目錄整體 untracked（`?? production/2026-w47/2026-w47-it-zh-tw/`）；clone 內 125 個 M 為其他並行工作文件，與本版無關 |
| 寫入紀律 | 全部構建在 scratch 副本；OUT/BASE 改向經 grep 確認；`PYTHONDONTWRITEBYTECODE=1`；生產無 `__pycache__` 寫入；核心目錄自探針起無文件寫入；零 commit、零 push |

## 缺陷清單

**無缺陷。** 觀察項見 PROOF-NOTE §5（O1–O16 為 proof2 跟蹤項，本輪重驗同值；O17–O24 為本輪新增），均不計缺陷。
