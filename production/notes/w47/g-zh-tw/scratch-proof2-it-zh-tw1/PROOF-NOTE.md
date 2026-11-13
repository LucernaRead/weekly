# PROOF-NOTE — 2026-W47 it-zh-tw (proof2, independent re-proof)

**結論：(a) 零缺陷，可定稿。** 全量重校（SOP §8）完成：150 題三源逐題手驗、8 頁逐頁目視交付印 PDF、門禁全部獨立重跑。未發現任何缺陷；觀察項 16 項，全部有像素/數值證據，見 §5。

- 版：`2026-w47-it-zh-tw`（義大利語目標 × 繁體中文讀者，VOL.4；核心 it fix3 後重擴散版）
- 印 PDF `La-Lucerna-VOL4-ZH-TW.pdf`：27,779,719 B，SHA-256 `79e51c537d9bcafb7612a056358cb9597c998ec84db1e16b183099ca98e5cfe8`
- 網 PDF `La-Lucerna-VOL4-ZH-TW-web.pdf`：2,074,068 B，SHA-256 `a809a3a53ca7c0b6a462803bc7fd2cf65f5f99621a3d08b7b872ce6f49edaf79`
- text.md `2026-w47-it-zh-tw.text.md`：52,515 B，SHA-256 `681dff470eeb01dae8883e5c34773599290711c724e0ec741b59b82da8933e45`
- 三 SHA 開工前與收工時兩次核對，均與任務值逐字節一致。生產 8 SVG ×8 + 8 cards PNG 收工時重驗，與開工基線逐字節一致（`prod-svg-final.txt`、`prod-cards-final.txt`）。生產零改動、零 commit、零 push。KIT K6/K7 未碰。
- 本報告與 `GATE-LOG.md` 均在 scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-it-zh-tw1/`。

## §1 門禁匯總（全部獨立重跑，詳見 GATE-LOG.md）

| 門禁 | 結果 |
|---|---|
| 開工探針 git hash-object /dev/null | e69de29b…，rc=0 |
| 三 SHA 盤核 | 與任務值一致 |
| run.py（scratch 副本，路徑已改向） | rc=0，TOTAL 150；A2 47 / B1 70 / B2 33；頁 10/18/18/18/18/18/12/38；範文 99 詞；P8-keys 末端 y=2484 |
| 重建 SVG 8/8 vs 生產 | 逐字節一致 |
| 重渲印 PDF vs 交付 | 逐字節一致（SHA 79e51c53…，27,779,719 B） |
| 重渲 cards PNG 8/8 vs 生產 | 逐字節一致 |
| p8 extract（版 + 核心） | 各 150/150 |
| p8 compare | CLEAN；keydiff=[137, 138, 139]；missing=[]；extra=0；uncertain=[] |
| freeze baseline（核心→scratch） | 8/8 逐字節一致 |
| freeze diff（核心 vs 本版） | 541 行全部讀完分類，0 條未解釋；Italian 目標文無一字改動；proof1 D1–D5 舊文無殘留；新增 CJK 970 |
| occlusion 幾何遮擋審計 | 0 flags，rc=0；selftest 6 類全觸發 |
| 奶油盒橫/縱掃（creambox.py） | 框內最小餘量 +3.9 px；9 個負值均為視窗下 artefact（見 O5） |
| 自寫 PIL 掃（sweep.py，ink_box） | 奶油盒標題 0 溢出；MARGIN+ 0 行 |
| gutter 精掃（sweep2.py） | 僅 7 候選，均無碰撞（見 O2/O3/O4） |
| 孤兒掃 | 5 旗標，全部裁定為非缺陷（見 §4） |
| 印/網文字層比對 | print == web == rerun-web 逐字節一致（102,496 B，6,832 詞，詞多重集差 0/0） |
| pdfscan（PyMuPDF span） | P8 最小字 9.75 pt（SOP §1.1 下限）；右緣超限 ≤1.9 pt 均為 side-bearing artefact（見 O13） |
| §1.1 乾淨 | 顏色/字體/字號/VOL/ABSTRACT 全部通過（見 §3） |
| text.md 雙向驗證（validate_edition_textmd.py） | forward-miss 0 / reverse-miss 0 |
| 日期/星期（`date -d`，Europe/Rome） | 全部核對通過（見 §2） |
| 算術 | 全部重算通過（見 §2） |
| 8 金句 | 每句在 text.md 恰出現 2 次，逐字一致 |
| 150 鍵三源手驗 | 149/149 一致；#150 僅記法差異（同義） |
| 標題數 | 實測見 §4（無任何定義得出 56） |
| KIT 核對 | §1–§11 數值/聲稱與我的實測一致（見 §3） |

## §2 全文通讀與事實驗證

- text.md 1317 行（+尾換行）全讀。刊期 Mon Nov 16 – Sun Nov 22, 2026，VOL.4。
- 日期/星期（`date -d`，Europe/Rome）：Nov 6 週五、7 週六、8 週日（MD11 6–8 Nov ✓）；Nov 12 週四（聽證會至 giovedì 12 ✓；Nations League 週四 12 法國、週日 15 比利時 ✓）；Nov 16 週一、17 週二（martedì 17 ✓）、18 週三、19 週四、20 週五、21 週六、22 週日；Nov 23 週一（lunedì 23 BookCity ✓）、Nov 24 週二（martedì 24 TFF ✓）；Dec 2 週三（TFF Nov 24–Dec 2 = 9 天 ✓）、Dec 6 週日（Alba 至 Dec 6 ✓）、Dec 31 週四（Dec 31 前表決 ✓）。
- 算術：MD11 10 場 24 球；積分榜 Lazio 29 / Inter 28 / Roma 27 / Milan 24 / Como 23 / Udinese 5；Roma 最佳進攻 31 球；P6 圖表 Torino 5° 最冷、Napoli 13° 最暖，13−11=2（Q85 B ✓），6+7=13（Q86 A ✓）；BookCity 1,360 活動 / 2,487 人物 / 1,164 書 / 443 場地；manovra +0.8%、赤字 3.4%、約 260 億、法案 C. 3174-bis、Irpef 33% 5 萬→5.5 萬、約 50 億融資。範文 99 詞（程式計數）。
- 8 金句逐字出處核對：`La Lazio resta in vetta`、`ventiquattro gol in dieci partite`、`il ponte votivo sul Canal Grande`、`oltre centocinquanta figuranti in costumi rinascimentali`、`la squadra di Gattuso è ancora imbattuta dopo 11 giornate`、`sette giorni di libri, ragioni e follie`、`il testo può ancora cambiare`、`approvato dal governo non vuol dire già legge`——每句在 text.md 恰出現 2 次（正文 + P7），逐字一致。
- proof1 D1–D5 全部在源頭修復：D1 P1 頭條今為 `Sabato 21 novembre torna la Serie A con la 12ª giornata: domenica sera, a Bergamo, c'è Atalanta–Inter`；D2 P2 b/d 修短形；D3 P3 Torrazzo `il campanile medievale in mattoni più alto d'Italia`；D4 P4 b/c 修短形；D5 P8 F 修短形。逐項在 text.md、SVG、渲染中核對。
- 150 鍵三源手驗：text.md RISPOSTE vs P8 印出鍵（p8-extract）149/149 一致；#150 僅記法差異（P8 `✓` vs text.md `✓ 範文見本版 H 區（99 詞）`，同義）。行內 stem 鍵 138 個，0 錯。分組手驗：P2 25–28（salute→c、ponte→b、candela→d、piantare→a）、P4 52–55（vetta→d、imbattuto→b、girone→c、debutto→a）、P8 F 141–144（manovra→d、deficit→c、copertura→b、scaglione→a）全部正確。
- 跨版引用全部核對：P1 目錄 Pag. 2–8 與各版標題一致；P7 FRASI 頁碼（Pagina 1,1,2,3,4,5,6,6）與出處一致；P1 `詳見第 4 版`（Serie A→P4 ✓）；P2 `pagina 6`（manovra→P6 ✓）、`pagina 7, «Lettere dei lettori»`（P7 ✓）。
- 頭條 `La Lazio resta in vetta: Inter e Roma inseguono` = 39 非空格字元（≤56）。
- 禁詞掃：`Ucraina`/`Russia`/`Putin` 0 命中。text.md 簡體 `译` 0 個；`翻譯` 8 個（含 `[翻譯成繁體中文]` ×3、`[翻譯成義大利語]` ×1）。
- 8 頁交付印 PDF 逐頁目視（100 dpi 全頁 + 200 dpi 關鍵裁圖）：無溢出、重疊、頁腳侵入、豆腐。P1 cifre 盒標題貼合；P2 配對 b/d 在欄內；P3 Torrazzo 側欄正確；P4 賽果表整齊；P5 piano 盒整齊；P6 時間線 + 柱狀圖正確（Torino 最短、Napoli 最長）；P7 ERRORI/LA PAROLA/LETTERE 盒 + 8 FRASI 頁碼正確 + VOL.5 預告條；P8 150 條 RISPOSTE 齊全，E 標籤繁中，F 修短形在欄內，範文在位。

## §3 §1.1 與 KIT 核對

- 顏色：`#302c28` ×1423、`#46581f` ×332、`#6f675d` ×236、徽章 `#5c6e30`/`#37402f`、奶油 `#f0eee5`、紙 `#fbfaf6`、鵝黃 `#f6e08e`——全部 SOP §1.1 調色。非調色填色只有飛蛾 logo 內部色塊（P1，`#EDD17F`/`#D7B257`/`#7898CD`/`#4D72B4` 等為 logo 翼面）與深綠帶上淺米字 `#cac8ba`（P1 綠帶副標、P7 綠帶 `LA PROSSIMA SETTIMANA`，核心同款）。無金/磚/近黑色頁面元素。
- 字體：Newsreader ×1193、Noto Sans CJK TC ×611、Noto Serif CJK TC ×283、UnifrakturMaguntia ×1（刊頭）。無其他字體。
- 頁規：8 頁，1462.5×2025 pt，1950×2700 px，4 欄。
- VOL：`VOL.4` ×9（8 頁腳 + 刊頭），`VOL.5` ×3（P2 E TU 互引、P7 LETTERE 承諾、P7 預告條）——全部合法。
- ABSTRACT.txt：一行 323 B，繁體中文，無 ASCII 雙引號，含 La Lucerna + VOL.4，事實與本期一致。
- KIT（WEEKLY-KIT.md §1–§11）核對：§1 150 題分佈、級別、範文 99 詞、P8 9.75 pt；§2 各版內容日期；§3 頭條 39 字；§7 三 SHA/字節數/1317 行；§8 門禁 19/19（occlusion 0、p8 CLEAN、freeze 8/8 + 0 未解釋、文字層 6832 詞、VOL 計數）；§9 cifre 改寫與 P8 44/134 註釋縮短；§10 公開短板；§11 fix3 九行與翻譯修正——**全部與我的獨立實測一致，無 KIT 不準之處**。

## §4 裁決事項（re-fanout §7 未決項，逐項實測）

**A. keydiff — 實測 [137, 138, 139]。** 版 vs 核心鍵差異恰為 Q137–139；三鍵均為繁體中文讀者句（`聖母健康節人們走過還願橋。` / `週日晚上亞特蘭大對國米。` / `週六，拉齊奧在主場對萊切。`），核心為簡體。Q140 兩版皆為義大利語 `Ogni cifra deve essere chiara.`，無差異是**正確行為**，不是遺漏。text.md Q137–140 標籤均為繁體 `翻譯`。

**B. 「英文源 key 未改」——裁定：無殘留。** (a) 英文殘留 grep：`Translate` 在 text.md 與 8 個 SVG 均為 0；`LUCERNA ITALIAN WEEKLY` 8 個 SVG 均為 0。(b) Q137–140 鍵/標籤已正確繁體化（見 A）。(c) P1 cifre 四行已全改為繁體中文（KIT §9 改寫，freeze diff 驗證；義大利語 head 已按設計去掉，數字/事實不變）。(d) IL PIANO 盒義大利語 head + 繁體 gloss 是目標語正文 + 讀者層設計，非英文殘留。**結論：本版無任何應為繁體中文的鍵/標籤留在英文。**

**C. 雙語小文件標題 STRADDLE——裁定：無缺陷。** 全部 29 個無邊框奶油盒逐一光柵實測（sweep.py，occlusion_audit.ink_box）：**0 溢出**。最緊：P1 `LA SETTIMANA IN CIFRE　數字看本週` PIL 墨至 960.0 vs 盒界 961.0（餘 +1.0 px）；200 dpi 像素重測（正確波段，基線 svg y=1358.75）：墨至 svg 959.0，奶油緣 960.5，**餘 +1.4 px**。字形未裁、墨未重疊他物或可見邊框、與舊版（proof1 同為 +1.0 px）相比無回歸——按 STRADDLE 規則三項皆無，不構成缺陷。it-en proof2 的英文 gloss 溢出（P1 +155、P2 +39、P7 +6 px）**在本版不存在**：其次緊者 P2 `LA FRASE PER RICORDARE　口訣` +43.0、P5 譯注 +19.5、P2 譯注 +26.5、P4 `LA CLASSIFICA　DOPO 11 GIORNATE` +29.0、P7 `ERRORI TIPICI　常見錯誤` +126.2。

**D. 孤兒 5 旗標——全部非缺陷：** P5 piano `（週日` 為分組 artefact（全頁渲染顯示 gloss `(週日 20:45：亞特蘭大對國米）` 完整在一行）；P6 譯注 `序。` 為 CJK 正常換行；P6 時間線 `18.`（`…alle ore / 18.`）完整可讀；P8 Q129 `due`（`C. i / due`）為核心繼承的義大利語換行，freeze diff 證實義大利語 stem 未動；P8 Q137 `___` 為答題空行設計。

**E. 標題數——實測，無任何定義得出 56。** 定義與計數（SVG + text.md 實測）：(T1) size≥40 展示節點 17 個（含刊頭 1、7 頁眉、1 綠帶口號、1 正文頭條、7 小刊頭）；(T2) 粗體 size≥21 共 270 個（含題號、徽章、表頭）；(T3) text.md `## ` 頁標題 8 個；(T4) text.md 全大寫行首標題行 54 個（含 5 個賽果表日期標籤與 1 個時間線標籤；扣除後為 48 個欄/盒標題）；正文頭條（混合大小寫）6 條（P1–P6；P7/P8 為欄目頁無頭條）。「56」在本版無對應定義，不採用。

**F. P8 `VUL DE KRONIEK IN` 類掃描超限——本版無此類超限。** pdfscan 全頁 span 右緣超限 ≤1.9 pt（見 O13），PIL 真墨全部在 1862 以內；無需行級裁決。

## §5 觀察項（不計缺陷）

- **O1（最緊，須跟蹤）：** P1 cifre 盒標題餘量 +1.0 px（PIL）/+1.4 px（像素，墨 959.0 / 緣 960.5）。按 it-de/it-fr 已接受先例裁定通過（墨恰觸盒界、x≥盒界+1 在任何閾值下無墨）。與核心同值（核心同標題 PIL 亦為 960.0）。**任何重擴散後必須重測。**
- **O2：** P4 gutter 候選 3 條，賽果表行 `Genoa – Milan 1–2` +11.0（下一欄間隙 21.0 px）、`Cagliari – Frosinone 1–0` +11.0（間隙 266.5 px）、`Torino – Lecce 1–1` +10.2（無相鄰物）——墨進 gutter 但無碰撞，與 proof1 同值，核心模式。
- **O3：** P7 gloss `一百五十多名身著文藝復興服裝的演員。 (Pagina 3)` +22.8 px 進 gutter，下一欄間隙 455.8 px，無碰撞（proof1 O2）。
- **O4：** P6 候選 3 條均在寬盒內部，非真 gutter：`Una cifra raccontata ≠ una cifra votata` +27.8、`«Il governo propone» ≠ «la legge dice»` +23.0（PROPOSTA ≠ LEGGE 雙欄盒 989..1862 內）；`MINIME DI ESEMPIO gradi, dati inventati` +27.8（圖表盒 88..961 內）。
- **O5：** desc-clear −2.1 px（P3/P5 E TU 末行 `更喜歡牛軋糖還是巧克力？寫兩句寄來。` 等）為量測 artefact——末行無降部字母；200 dpi 裁圖目視確認末行完整在奶油盒內、下方留白充足（`crop-p3-etu-bottom.png`、`crop-p5-etu-bottom.png`）。
- **O6：** MARGIN− 87.8（比左界 88 左 0.2 px）出現在 12 個節點，核心同 12 個節點同值——字體 sidebearing artefact，非缺陷。
- **O7：** Q32 註用直引號 `"Fate dolci"`，他處用 `«Fate dolci»`（KIT §10 已公開；舊版亦然）。
- **O8：** P4 賽果標題 `第 11 輪賽果（6–8 novembre）` 在繁體標題內保留義大利語月份（KIT §10 已公開；translations.py 原值逐字）。
- **O9：** P8 `— PAGINA {n} —` 分隔符保留義大利語（KIT §8 已公開；it 家慣例，核心同款）。
- **O10：** 選項/gloss 清單內 `·` 分隔符保留（KIT §10 已公開；核心同款。頁腳/刊頭家具分隔符仍為全角空格）。
- **O11：** P1 頭條首段無 drop cap（SOP §1.1 要求首字下沉；核心同款，KIT §10 已公開，W46-FR 已接受）。
- **O12：** O12 孤兒見 §4 D（5 旗標全部非缺陷，核心繼承或設計）。
- **O13：** pdfscan span 右緣超限 ≤1.9 pt（P1 `2026` +0.2、P2 副標 +1.6、P5 圖注 +1.6、P8 範文行 +1.8/+1.9）均為 span 包圍盒 side-bearing artefact；PIL 真墨右緣全頁 ≤1861.4（P1 綠帶金字），無 MARGIN+。
- **O14：** P8 最小字 9.75 pt = SOP §1.1 下限（讓步第 4 步，核心同款，KIT §10 已公開），非缺陷。
- **O15（工具說明，非本版缺陷）：** 重渲網 PDF 為 2,074,067 B（交付 2,074,068 B，差 1 字節），但**不是內容差異**：兩版 8 頁、尺寸、元數據（無日期）、229 xref、逐頁文字、7 嵌入圖、全部頁內容流均逐字節一致，僅 19 條字體子集 Flate 流壓縮長度差 1–2 字節；同批 SVG 數分鐘後第二次重渲又得另一 SHA（`05ec962b…`，首異字節同在 250316），證明 webpdf.py 輸出**逐次不具位元組再現性**（字體子集壓縮非確定性）。三版文字層逐字節一致（102,496 B，6,832 詞）。印 PDF 重渲則逐字節一致（SHA 79e51c53…）。
- **O16：** 奶油盒縱向 9 個負「末基線」餘量（P1 ADESSO TU −37.0、LA PAROLA −24.0、QUIZ 副標 −44.0；P3 TORRAZZO −37.0；P4 表行 −40/−40/−26；P6 ESERCIZI −42 ×2）均為視窗伸入下一欄目標題/表行所致，與 proof1 同模式，非溢出。

## §6 收工完整性

- 所有構建/渲染均在 scratch 副本進行（OUT/BASE 已改向並經 grep 確認無 `weekly-git/production` 殘留）；凡 import 生產源碼均加 `PYTHONDONTWRITEBYTECODE=1`；生產目錄無 `__pycache__` 寫入。
- 收工重驗：三 SHA 與任務值一致；8 SVG + 8 cards 與開工基線逐字節一致；`git status` 生產目錄無追蹤修改（該目錄本就未追蹤）。
- 證據文件（scratch）：`occlusion.log`、`p8*.log/json`、`freeze-baseline.log/json`、`freeze-diff.log`、`freeze-fragments.txt`（541 行已讀）、`rerun-run.log`、`rerun-render.log`、`rerun-webpdf.log`、`print.txt`/`web.txt`/`rerun-web.txt`、`creambox-all.log`、`sweep.log/txt`、`sweep2.log/txt`、`textmd-validate.log`、`pages/p-1.png`–`p-8.png`、`pages/crop-*.png`、`baseline-prod-hashes.txt`、`prod-svg-final.txt`、`prod-cards-final.txt`。
