# PROOF-NOTE — 2026-W47 it-zh-tw（重擴散 2 後獨立全量復校，SOP §8.4）

**結論：(a) 零缺陷，可定稿。** 全量重校（SOP §8）完成：150 題三源逐題手驗、8 頁逐頁目視交付印 PDF、全部機械門獨立重跑、D-2 回歸三項逐項獨立重測。未發現任何缺陷；觀察項見 §5（O1 為 proof2 跟蹤項，本輪獨立重測值不變；O17–O23 為本輪新增）。

- 版：`2026-w47-it-zh-tw`（義大利語目標 × 繁體中文讀者，VOL.4；core-it D-2 fix 後重擴散 2 版）
- 印 PDF `La-Lucerna-VOL4-ZH-TW.pdf`：27,779,699 B，SHA-256 `96aa320738b09cf89c18fbb63789c38225017feb8969db98c1fedb44041d1531`
- 網 PDF `La-Lucerna-VOL4-ZH-TW-web.pdf`：2,074,045 B，SHA-256 `1f5730490f765d75d9c1317c6ef65734ab8d9453541161b271591660b109a1a9`
- text.md `2026-w47-it-zh-tw.text.md`：52,494 B，SHA-256 `c18ad203cf49356079c4403e69b7366b1f36109963eadbcce17058da08dd8432`
- 文件名核對：盤上實際文件名與任務書所寫逐字一致（`La-Lucerna-VOL4-ZH-TW.pdf` / `-web.pdf`），無出入。
- 三 SHA 開工前與收工時兩次核對，均與任務值逐字一致。生產 8 SVG + 8 cards 收工時重驗，與開工基線逐字一致（`prod-svg-final.txt` vs `baseline-prod-hashes.txt`）。生產零改動、零 commit、零 push、零 `__pycache__` 寫入。KIT 未碰。
- 本報告與 `GATE-LOG.md` 均在 scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it2-zh-tw/`。

## §1 門禁匯總（全部獨立重跑，詳見 GATE-LOG.md）

| 門禁 | 結果 |
|---|---|
| 開工探針 git hash-object /dev/null | e69de29b…，rc=0；scratch 真實寫文件通過 |
| 三 SHA 盤核（開工 + 收工） | 與任務值一致 |
| run.py（scratch 副本，OUT/BASE 改向，grep 驗無生產殘留） | rc=0，TOTAL 150；A2 47 / B1 70 / B2 33；頁 10/18/18/18/18/18/12/38；範文 99 詞；P8-keys 末端 y=2484；P7 col3 末端 1644.0；P4 col3 末端 1140.45 |
| 重建 SVG 8/8 vs 生產 | 逐字一致 |
| 重渲印 PDF vs 交付 | 逐字一致（SHA 96aa3207…，27,779,699 B） |
| 重渲 cards PNG 8/8 vs 生產 | 逐字一致 |
| webpdf 重渲 + 文字層 | 重渲 2,074,040 B（交付 2,074,045 B，差 5 字節，見 O19）；print == web == rerun-web 文字層逐字一致（預設模式 44,052 B；`-layout` 模式 102,508 B） |
| p8 extract（版 + 核心） | 各 150/150 |
| p8 compare | CLEAN；keydiff=[137, 138, 139]；missing=[]；extra=0；uncertain=[] |
| freeze baseline（`--build` 為 core-it 自身，`--core-svg` 為 core-it/svg） | 8/8 逐字一致；build-copy 驗為 core-it 自身（改向 6 文件，0 生產路徑殘留）；核心 p7 `a7e6afa4…` 精確復現；核心 SVG 運行前後重哈希無變 |
| freeze diff（核心 vs 本版） | p1 +42/−40、p2 +16/−16、p3 +14/−14、p4 +15/−15、p5 +24/−24、p6 +14/−14、p7 +28/−28、p8 +169/−183；新增 CJK 970；全部 322+320 個文本節點逐項分類，**0 條未解釋；Italian 目標文無一字改動**（見 §4） |
| occlusion 幾何遮擋審計 | 0 flags，rc=0；selftest 6 類全觸發 |
| 奶油盒縱掃（creambox.py，8 頁） | rc=0；框內最小餘量 +3.9 px；9 個負「末基線」餘量與 proof2 同值同模式（見 O16） |
| 自寫 PIL 掃（sweep.py，ink_box） | 奶油盒標題 0 溢出；MARGIN+ 0 行 |
| gutter 精掃（sweep2.py） | 僅 7 候選，均無碰撞（見 O2/O3/O4） |
| 孤兒掃 | 5 旗標，全部裁定為非缺陷（同 proof2，見 §4） |
| pdfscan（PyMuPDF span，交付印 PDF） | P8 最小字 9.75 pt（SOP §1.1 下限）；右緣超限 ≤1.9 pt 均為 side-bearing artefact（見 O13）；左緣超限 0 |
| §1.1 乾淨 | 顏色/字體/字號/VOL/ABSTRACT 全部通過（見 §3） |
| text.md 雙向驗證（validate_edition_textmd.py） | forward-miss 0 / reverse-miss 0 |
| 日期/星期（`date -d`，Europe/Rome） | 全部核對通過（見 §2） |
| 算術 | 全部重算通過（見 §2） |
| 8 金句 | 每句在 text.md 恰出現 2 次，逐字一致 |
| 150 鍵三源手驗 | stem vs RISPOSTE vs P8 印出鍵 150/150 一致；#150 僅記法差異（同義） |
| KIT 核對 | §1–§12 數值/聲稱與我的實測一致（見 §3；兩處 1 token 級計數口徑差見 O17/O18，不計缺陷） |

## §2 全文通讀與事實驗證

- text.md 1317 行全讀。刊期 Mon Nov 16 – Sun Nov 22, 2026，VOL.4。
- 日期/星期（`date -d`，Europe/Rome）：Nov 6 週五、7 週六、8 週日（MD11 6–8 Nov ✓）；Nov 12 週四（聽證會至 giovedì 12 ✓；Nations League 週四 12 法國、週日 15 比利時 ✓）；Nov 16 週一、17 週二（martedì 17 ✓）、18 週三、19 週四、20 週五、21 週六、22 週日；Nov 23 週一（lunedì 23 BookCity ✓）、Nov 24 週二（martedì 24 TFF ✓）；Dec 2 週三（TFF Nov 24–Dec 2 含首尾共 9 天 ✓）、Dec 6 週日（Alba 至 Dec 6 ✓）、Dec 31 週四（Dec 31 前表決 ✓）。
- 算術：MD11 10 場 24 球（逐場相加 3+1+2+3+3+2+3+1+2+4=24 ✓）；積分榜 Lazio 29 / Inter 28 / Roma 27 / Milan 24 / Como 23 / Udinese 5；Roma 最佳進攻 31 球；P6 圖表 Torino 5° 最冷、Napoli 13° 最暖，13−11=2（Q85 B ✓），6+7=13（Q86 A ✓）；BookCity 1,360 活動 / 2,487 人物 / 1,164 書 / 443 場地；manovra +0.8%、赤字 3.4%、約 260 億、法案 C. 3174-bis、Irpef 33% 5 萬→5.5 萬、約 50 億融資。範文 99 詞（程式計數，run.py 亦印 model words: 99）。
- 8 金句逐字出處核對：`La Lazio resta in vetta`、`ventiquattro gol in dieci partite`、`il ponte votivo sul Canal Grande`、`oltre centocinquanta figuranti in costumi rinascimentali`、`la squadra di Gattuso è ancora imbattuta dopo 11 giornate`、`sette giorni di libri, ragioni e follie`、`il testo può ancora cambiare`、`approvato dal governo non vuol dire già legge`——每句在 text.md 恰出現 2 次（正文 + P7），逐字一致。
- 150 鍵三源手驗（`keycheck.txt`）：題幹內鍵（stem）150/150 解析、RISPOSTE 150/150、P8 印出鍵 150/150，三源 0 不符；#150 僅記法差異（P8 `✓` vs text.md `✓ 範文見本版 H 區（99 詞）`，同義）。分組手驗：P2 25–28（salute→c、ponte→b、candela→d、piantare→a，配對語義逐項核對正確）、P4 52–55（vetta→d、imbattuto→b、girone→c、debutto→a）、P8 F 141–144（manovra→d、deficit→c、copertura→b、scaglione→a）、Q101–104（andremo / assaggeremo / guarderemo / B）全部正確。
- 跨版引用全部核對：P1 目錄 Pag. 2–8 與各版標題一致；P7 FRASI 頁碼（Pagina 1,1,2,3,4,5,6,6）與出處一致；P1 `詳見第 4 版`（Serie A→P4 ✓）；P2 `pagina 6`（manovra→P6 ✓）、`pagina 7, «Lettere dei lettori»`（P7 ✓）。
- 頭條 `La Lazio resta in vetta: Inter e Roma inseguono` = 39 非空格字元（≤56）。
- 禁詞掃：`Ucraina`/`Russia`/`Putin` 0 命中。text.md 簡體 `译` 0 個；`翻譯` 8 個。
- 8 頁交付印 PDF 逐頁目視（100 dpi 全頁 `pages/p-1.png`–`p-8.png` + 200 dpi 裁圖 `crop-p7-a2.png`、`crop-p1-cifre.png`）：無溢出、重疊、頁腳侵入、豆腐。P1 cifre 盒標題貼合（見 O1）；P2 配對 b/d 在欄內；P3 Torrazzo 側欄正確；P4 賽果表整齊；P5 piano 盒整齊；P6 時間線 + 柱狀圖正確（Torino 最短、Napoli 最長）；P7 D-2 兩句在版乾淨 + ERRORI/LA PAROLA/LETTERE 盒 + 8 FRASI 頁碼正確 + VOL.5 預告條；P8 150 條 RISPOSTE 齊全，E 標籤繁中，F 修短形在欄內，範文在位。

## §3 §1.1 與 KIT 核對

- 顏色：`#302c28` ×1417、`#46581f` ×379、`#6f675d` ×236、徽章 `#5c6e30`/`#37402f`、奶油 `#f0eee5`、紙 `#fbfaf6`、鵝黃 `#f6e08e`——全部 SOP §1.1 調色。非調色填色只有飛蛾 logo 內部色塊（P1，含 proof2 未列出的 `#34483A`/`#F1E8D4`/`#4F765D`/`#84A283`，皆在 `<title>Lucerna 三色蛾</title>` 內，見 O22）與深綠帶上淺米字 `#cac8ba`（P1 綠帶副標、P7 綠帶預告條，核心同款）及白色等級徽章字 `#ffffff` ×141。無金/磚/近黑色頁面元素。
- 字體：Newsreader ×1188、Noto Sans CJK TC ×611、Noto Serif CJK TC ×282、UnifrakturMaguntia ×1（刊頭）。無其他字體。與修前備份差 Newsreader −5、Serif −1，恰為 P7 刪去的 D-2 舊句文本節點（見 O21）。
- 頁規：8 頁，1462.5×2025 pt，1950×2700 px，4 欄。
- VOL：`VOL.4` ×9（8 頁腳 + 刊頭），`VOL.5` ×3（P2 E TU 互引、P7 LETTERE 承諾、P7 預告條）——全部合法。
- ABSTRACT.txt：一行 323 B，繁體中文，無 ASCII 雙引號，含 La Lucerna + VOL.4，事實與本期一致；KIT §7 引文逐字相符。
- KIT（WEEKLY-KIT.md §1–§12）核對：§7 三 SHA/字節數/1317 行、§8 門禁 19/19（occlusion 0、p8 CLEAN、freeze 8/8 + 0 未解釋、P8 9.75 pt、VOL 計數）、§9 cifre 改寫與 P8 44/134 註釋縮短、§12 重擴散 2 新三 SHA 與修前三 SHA、核心三 SHA（`e1f89922…` / `09f2ef66…` / `9eb9ee06…`，盤上重驗逐字一致）——**全部與我的獨立實測一致**，僅 O17/O18 兩處 1 token 級計數口徑差。
- 英文殘留：`Translate` 在 text.md 與 8 個 SVG 均為 0；`LUCERNA ITALIAN WEEKLY` 核心 8 處、本版 8 個 SVG 均為 0（核心頁眉英文 kicker 在本版由繁體刊頭行取代，屬讀者層替換，見 §4）。

## §4 裁決事項（回歸項 + freeze 差分全分類）

**A. D-2 回歸——實測通過。**
- 新串在位（各 ×1）：text.md:775 `Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.`、:777 `Il verbo è leggere, regolare al futuro: leggerò.`；content7.py:17/:18 同文；p7 SVG 文本節點內（新 3 節點，皆為兩句的子串）；印/網 PDF P7 文字層各 ×1（空白摺疊計數——文字層行間斷行，需摺疊空白後計數；見 O23）；200 dpi 裁圖 `crop-p7-a2.png` 兩句渲染乾淨完整。
- 舊串 0 處：`Le forme sono regolari: andare` 與 `irregolare al futuro: leggerò` 在 content*.py、8 SVG、text.md、兩 PDF 全文文字層均為 0。`andrò` 在 text.md 與 p7 SVG 均為 0；`andare` 殘留處皆合法（Q101 題幹 `(andare)`、Q42/Q76 題幹、P7 診所 `andare 用 essere 作助動詞`、P1 正文 `andare in stampa` 等）。
- 僅 P7 變化（與修前備份逐項 diff，備份 SHA 驗證通過）：text.md diff 恰為 :775/:777 兩行（−21 字節：52,515→52,494）；SVG 僅 p7 不同、cards 僅 p7 不同；content diff 恰為 `content7.py:17/:18` 兩行；其餘 content*.py 逐字一致；p7 SVG 文本節點 diff 僅限兩句的換行碎片（舊 9 節點 / 新 3 節點）。
- 核心三 SHA 盤上重驗與 FANOUT-REPORT §2/KIT §12 逐字一致；核心 p7 SVG `a7e6afa4…` 與 FIX-LOG 定稿值一致，freeze baseline 精確復現。

**B. O1 跟蹤項重測——實測通過（仍為全家最緊，按已接受先例通過，下輪仍須重測）。**
- PIL 真墨法（proof2 `sweep.py` 同方法同腳本）：奶油盒 538.5..961.0，標題墨 556.5..960.0，餘量 **+1.0 px**——與重擴散前實測值逐字相同。
- 200 dpi 像素法（印 PDF P1，亮度 <140 為墨，正確波段 svg y 1336..1362、限盒內 x 538.5..961）：墨最右 img x=1998 → svg **959.0**，奶油緣 960.5，餘量 **+1.5 px**（proof2 報 +1.4 px，墨位置同一像素 959.0/959.1，差為取整口徑；閾值 100/140/180/200 下同值）。200 dpi 裁圖目視：標題末字 `週` 完整在盒內，盒緣清晰。
- 備份舊版對照（STRADDLE 規則要求）：備份印 PDF 同法重測，墨最右同為 svg 959.0——**與舊版相同，無回歸**；字形未裁、墨未重疊他物或可見邊框。三項皆無，不構成缺陷。

**C. P7 教學段語義逐句事實核查——通過。**
- 全版 `regolar` 僅出現 2 次（text.md 與 p7 SVG 各 2 次，皆為 D-2 修正句）；`irregolar` 全版 0 次。無其他規則性斷言可供誤標。
- L17：assaggiare → assaggerò、guardare → guarderò 皆為規則未來時構形（-are 動詞去尾加 -ò，assaggiare 保留雙 g），稱「regolari」正確；andare 已不在規則例之列（andrò 為不規則詞幹 andr-，正確排除）。
- L18：leggere → leggerò 為規則未來時構形（-ere 動詞去尾 -e 加 -ò），稱「regolare」正確；leggere 的不規則處（遠過去時 lessi、過去分詞 letto）不在未來時，本句未作斷言。
- 前後指涉不懸空：L17 句首 andremo/assaggeremo/guarderemo 未動；L18 前句 `leggeremo a BookCity` 未動；橋接句 `用將來時說計劃：andremo、assaggeremo、guarderemo、leggeremo。`未動；Q101–104 鍵（andremo / assaggeremo / guarderemo / B）與三源一致。
- P7 其餘教學段逐句核對：B1 passato prossimo（essere 分詞配合性數、avere 分詞不變、è partito/è finita、abbiamo visto/hanno comprato）正確；B2 congiuntivo（è probabile/possibile/bisogna che 後虛擬式 piova/nevichi/leggano；so che/scrivono che 後陳述式）正確；ERRORI 四條糾正（La Lazio ha、vinca、sono andato、il torrone è）皆正確。

**D. freeze 差分全分類——0 條未解釋。** 拉丁詞多重集逐頁比對（`freeze-wordcheck.txt`）：p2–p8 的拉丁詞差異**僅**為頁眉英文 kicker `LUCERNA ITALIAN WEEKLY`（核心 8 頁各 1，本版 0——讀者層取代）；p1 另有 cifre 四行改寫的義大利語 head 詞（KIT §9 已登記：`29 — i punti della Lazio…` 等改為全繁體行，數字/事實不變）與 `10`/`11` 計數差（cifre 行重排分段所致）。其餘「未匹配」皆為同文重排（`20.45 — …` 斷行、`essere/avere` 節點合併、P8 `+ ` 節點 8→4）。P8 `+ ` 之差已逐項定位：核心 Q44/Q134/Q136 註 `主語 + 動詞 + 地點 + 日期`（8 個 `+ ` 節點），本版 Q44/Q134 依 KIT §9 預先縮短為 `主語 + 動詞`、Q136 保留 `主語 + 動詞 + 地點`（4 個 `+ ` 節點），與備份版逐字相同、非本輪引入。**Italian 目標文無一字改動。**

**E. 孤兒 5 旗標——全部非缺陷（與 proof2 同裁定，本輪重驗同值）：** P5 piano `（週日` 為分組 artefact（全頁渲染顯示 gloss `(週日 20:45：亞特蘭大對國米）` 完整在一行）；P6 譯注 `序。` 為 CJK 正常換行；P6 時間線 `18.`（`…alle ore / 18.`）完整可讀；P8 Q129 `due`（`C. i / due`）為核心繼承的義大利語換行，freeze diff 證實義大利語 stem 未動；P8 Q137 `___` 為答題空行設計。

**F. 雙語小文件標題 STRADDLE——裁定：無缺陷。** 全部 29 個無邊框奶油盒逐一光柵實測（sweep.py，occlusion_audit.ink_box）：**0 溢出**。最緊即 O1（+1.0 px）；其次緊者 P2 `LA FRASE PER RICORDARE　口訣` +43.0、P5 譯注 +19.5、P2 譯注 +26.5、P4 `LA CLASSIFICA　DOPO 11 GIORNATE` +29.0、P7 `ERRORI TIPICI　常見錯誤` +126.2。it-en proof2 的英文 gloss 溢出在本版不存在。

## §5 觀察項（不計缺陷）

- **O1（最緊，須跟蹤）：** P1 cifre 盒標題餘量 +1.0 px（PIL）/+1.5 px（像素，墨 959.0 / 緣 960.5；proof2 +1.4 px 為同像素取整差）。按 it-de/it-fr 已接受先例裁定通過（墨恰觸盒界、x≥盒界+1 在任何閾值下無墨）。與備份舊版同值，無回歸。**任何重擴散後必須重測。**
- **O2：** P4 gutter 候選 3 條，賽果表行 `Genoa – Milan 1–2` +11.0（下一欄間隙 21.0 px）、`Cagliari – Frosinone 1–0` +11.0（間隙 266.5 px）、`Torino – Lecce 1–1` +10.2（無相鄰物）——墨進 gutter 但無碰撞，與 proof2 同值，核心模式。
- **O3：** P7 gloss `一百五十多名身著文藝復興服裝的演員。 (Pagina 3)` +22.8 px 進 gutter，下一欄間隙 455.8 px，無碰撞（proof2 O2）。
- **O4：** P6 候選 3 條均在寬盒內部，非真 gutter：`Una cifra raccontata ≠ una cifra votata` +27.8、`«Il governo propone» ≠ «la legge dice»` +23.0（PROPOSTA ≠ LEGGE 雙欄盒 989..1862 內）；`MINIME DI ESEMPIO gradi, dati inventati` +27.8（圖表盒 88..961 內）。
- **O5：** desc-clear −2.1 px（P3/P5 E TU 末行 `更喜歡牛軋糖還是巧克力？寫兩句寄來。` 等）為量測 artefact——末行無降部字母；200 dpi 全頁目視確認末行完整在奶油盒內、下方留白充足。creambox 最小框內餘量 +3.9 px，與 proof2 同值。
- **O6：** MARGIN− 87.8（比左界 88 左 0.2 px）出現在 12 個節點，核心同 12 個節點同值——字體 sidebearing artefact，非缺陷。
- **O7：** Q32 註用直引號 `"Fate dolci"`，他處用 `«Fate dolci»`（KIT §10 已公開；舊版亦然）。
- **O8：** P4 賽果標題 `第 11 輪賽果（6–8 novembre）` 在繁體標題內保留義大利語月份（KIT §10 已公開；translations.py 原值逐字）。
- **O9：** P8 `— PAGINA {n} —` 分隔符保留義大利語（KIT §8 已公開；it 家慣例，核心同款）。
- **O10：** 選項/gloss 清單內 `·` 分隔符保留（KIT §10 已公開；核心同款。頁腳/刊頭家具分隔符仍為全角空格）。
- **O11：** P1 頭條首段無 drop cap（SOP §1.1 要求首字下沉；核心同款，KIT §10 已公開，W46-FR 已接受）。
- **O12：** 孤兒見 §4 E（5 旗標全部非缺陷，核心繼承或設計）。
- **O13：** pdfscan span 右緣超限 ≤1.9 pt（P1 `2026` +0.2、P2 副標 +1.6、P5 圖注 +1.6、P8 範文行 +1.8/+1.9）均為 span 包圍盒 side-bearing artefact；PIL 真墨右緣全頁 ≤1861.4（P1 綠帶金字），無 MARGIN+。
- **O14：** P8 最小字 9.75 pt = SOP §1.1 下限（讓步第 4 步，核心同款，KIT §10 已公開），非缺陷。
- **O15（工具說明，非本版缺陷）：** 重渲網 PDF 為 2,074,040 B（交付 2,074,045 B，差 5 字節），但**不是內容差異**：三版文字層逐字一致（預設模式 44,052 B；`-layout` 模式 102,508 B），與 proof2 O15 同類（webpdf.py 輸出逐次不具位元組再現性，字體子集壓縮非確定性）。印 PDF 重渲逐字一致（SHA 96aa3207…）。
- **O16：** 奶油盒縱向 9 個負「末基線」餘量（P1 ADESSO TU −37.0、LA PAROLA −24.0、QUIZ 副標 −44.0；P3 TORRAZZO −37.0；P4 表行 −40/−40/−26；P6 ESERCIZI −42 ×2）均為視窗伸入下一欄目標題/表行所致，與 proof2 同模式，非溢出。
- **O17（本輪新增，計數口徑）：** proof2 PROOF-NOTE §1 freeze-diff 表寫 p5「+22/−22」，但其自帶 `freeze-diff.log` 寫 +24/−24；本輪獨立 diff 確認為 **+24/−24**。PROOF-NOTE 筆誤，log 為準；無內容影響。
- **O18（本輪新增，計數口徑）：** KIT §8「pdftotext word multiset identical (6829 words each)」與本輪實測 6,830 個空白分隔 token（交付印 PDF，預設模式；同法在修前文本上恰得 proof2 的 6,832）差 1 token。差由 D-2 刪句後的 `44.造句`→`44.`+`造句` 重分詞所致（P7 A2 欄短一行後的 pdftotext 行分組變化）；token 多重集差除 D-2 兩句外為 0。文字層同一性門禁不受影響。
- **O19（本輪新增，見 O15）：** webpdf 重渲差 5 字節，文字層逐字一致，非內容差異。
- **O20（本輪新增）：** P7 PyMuPDF spans 168（proof2 報 172）——D-2 刪節點所致（舊 9 節點→新 3 節點），預期內。
- **O21（本輪新增）：** 字體計數 Newsreader 1193→1188、Noto Serif CJK TC 283→282（vs 修前備份）——D-2 刪節點所致，預期內。
- **O22（本輪新增）：** 飛蛾 logo 內部色比 proof2 §3 所列多 4 個（`#34483A`/`#F1E8D4`/`#4F765D`/`#84A283`，皆在 P1 `<title>Lucerna 三色蛾</title>` 內）；`#ffffff` ×141 為白色等級徽章字。皆非調色違規，proof2 列表不全而已。
- **O23（本輪新增，方法備註）：** PDF 文字層在句中斷行（`\n`），樸素子串計數會把 D-2 新句誤計為 0；須空白摺疊後計數（新串各 ×1、舊串 0）。方法問題，非內容問題。
- **O24：** P3/P5 中欄大面積留白、P7 A2 欄 Q104 下方留白為核心繼承的版式模式，與備份版一致，非缺陷。

## §6 收工完整性

- 所有構建/渲染均在 scratch 副本進行（OUT/BASE 已改向並經 grep 確認 0 處 `weekly-git/production` 殘留）；凡 import 生產源碼均加 `PYTHONDONTWRITEBYTECODE=1`；生產目錄無 `__pycache__` 寫入；核心目錄自探針起無任何文件寫入（find newer 為空）。
- 收工重驗：三 SHA 與任務值一致；8 SVG + 8 cards 與開工基線逐字一致；`git status` 中本版目錄為整體 untracked（`?? production/2026-w47/2026-w47-it-zh-tw/`），無任何追蹤修改屬本版（clone 內 125 個 M 為其他並行工作的文件，與本版無關）。
- 證據文件（scratch）：`occlusion.log`、`p8*.log/json`、`freeze-baseline.log/json`、`freeze-diff.log/json`、`freeze-wordcheck.txt`、`rerun-run.log`、`rerun-render.log`、`rerun-webpdf.log`、`print.txt`/`web.txt`/`rerun-web.txt`、`creambox-all.log`、`sweep.log/txt`、`sweep2.log/txt`、`textmd-validate.log`、`keycheck.txt`、`facts-check.txt`、`style-check.txt`、`pdfscan.txt`、`pages/p-1.png`–`p-8.png`、`pages/p-*-200.png`、`pages/crop-p7-a2.png`、`pages/crop-p1-cifre.png`、`pages/backup-p1-200.png`、`baseline-prod-hashes.txt`、`prod-svg-final.txt`。
