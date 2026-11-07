# Lucerna 每週封面 — W43（2026年10月19日至25日）— 繁體中文讀者版

## 規格

- 依據：SOP 附則五（2026-10-28 追加）——每週封面，12 份讀者語言版之一。
- 讀者語言：繁體中文（zh-tw）。封面原創文字（標題、導言、解說）一律以繁體中文原生撰寫，絕非由簡體版轉換。
- 刊頭：Lucerna，不加冠詞（中文不取冠詞，tables.json zh-tw 條目 article 為 null）。P1 不編 VOL 號，改以 COVER 徽章標示；VOL 號只出現在 P8 一覽。
- 頁數與尺寸：8 頁，1950x2700；正刊視覺系統：暖象牙 #f7f1e2、深橄欖綠、serif。
- 取材鐵律：12 條頭條與摘錄一律取自當週 12 篇核心報 P1 主頭條，逐字一致，禁止重寫、改寫、拼湊新事實。條目原文保留原語言；解說層以繁體中文撰寫，每條 1-2 句，只重述該條標題＋摘錄，不引入核心報之外的事實。

## 12 條來源（固定順序，標題逐字照錄）

| 來源語言 | 核心報目錄 | 刊頭 | P8 VOL | 主頭條（逐字） |
|---|---|---|---|---|
| en | weekly-report-en-vol1 | The Lucerna | VOL. 1 | First Votes, First Games : America's Biggest Week of the Autumn |
| de | weekly-report-de-vol1 | Die Lucerna | VOL. 1 | Eine Stunde geschenkt: Deutschland stellt die Uhren zurück — und elf Länder haben Ferien |
| fr | weekly-report-vol4 | Le Lucerna | VOL. 2 | Présidentielle 2027 : les Français regardent déjà les sondages |
| es | weekly-report-es-vol1 | La Lucerna | VOL. 1 | Este domingo: dormimos una hora más… ¡y se juega el Clásico! |
| it | weekly-report-it-vol1 | La Lucerna | VOL. 1 | Un'ora in più di sonno: domenica torna l'ora solare |
| pt | weekly-report-pt-vol1 | A Lucerna | VOL. 1 | Domingo é dia de decisão: o Brasil volta às urnas |
| nl | weekly-report-nl-vol1 | De Lucerna | VOL. 1 | Een volle week: vakantie, design, dance — en een uur extra slaap |
| ru | weekly-report-ru-vol1 | Lucerna | VOL. 1 | Первый снег — уже на этой неделе! |
| ja | weekly-report-ja-vol1 | Lucerna | VOL. 1 | 土よう日、日本シリーズが始まる！ |
| ko | weekly-report-ko-vol1 | Lucerna | VOL. 1 | 태풍 참피가 오고 있어요 |
| zh-cn | weekly-report-zhcn-vol1 | Lucerna | VOL. 1 | 双11到了「付尾款」的这一周 |
| zh-tw | weekly-report-zhtw-vol1 | Lucerna | VOL. 1 | 強颱薔琵壓境！週五、週六風雨最大 |

- 摘錄：每條取正文開頭（至多 4 句），與核心報 P1 SVG 逐字核對一致（見「驗證」）。
- 簡體中文條目（zh-cn）的標題與摘錄在本封面中保持簡體原樣，絕不轉換；其繁體中文解說是本封面為繁體讀者新寫的文字。

## 版式

- P1：刊頭 Lucerna ＋ COVER 徽章 ＋ 週標籤「2026年10月19日至25日」＋ 封面標題「十二種語言，一週大事」＋ 導言（通用框架，無新事實）＋ 12 條頭條預告（固定順序：來源語言標籤 ＋ 刊頭 ＋ 逐字標題）。
- P2–P7：12 條全文，每頁 2 條，固定順序：P2 EN、DE；P3 FR、ES；P4 IT、PT；P5 NL、RU；P6 JA、KO；P7 zh-cn、zh-tw。每條：來源語言標籤、逐字標題、逐字摘錄，繼以「繁體中文解說」1-2 句。
- P8：本週 12 篇核心報一覽，固定順序：每篇刊頭 ＋ VOL ＋ 逐字標題。W43 各期 VOL：FR VOL.2，其餘 VOL.1。

## 解說層寫法（具名決策）

- 人名、地名凡轉寫可能生造形式者，一律保留原文：PT 候選人保留 Lula（PT）與 Flávio Bolsonaro（PL）；JA 隊名保留横浜DeNAベイスターズ與福岡ソフトバンクホークス（球場名以繁體中文「橫濱球場」書寫）。
- 颱風名（見「颱風名警示」一節）：KO 條解說稱「참피 (Champi)」；zh-tw 條解說稱「薔琵」，不附拉丁名。
- ES 條「Clásico」解說為「國家德比」（通用譯名，非新事實）。

## 驗證

- 逐字核對：12/12 標題與 12/12 摘錄皆以去空白比對，在各自核心報 P1 SVG 中找到，與共享來源 headlines-w43.json 無出入；未發現 JSON 與核心報之間的差異。
- 繁體原創文字檢查：以程式掃描 build.py 全部繁體中文原創字串（標籤、標題、導言、12 條解說、頁眉頁腳），嚴格簡體專用字（如 种、说、让、学、门、头、条、发、过、语、设、边、环、应、预、号、参、轮、则、猫、宝、货、现、贩、双）命中數為 0。
- 視覺目檢：8 頁 PNG 全數目檢——無溢出、無截斷、無缺字豆腐塊、無重疊；12 種文字皆正常渲染（拉丁、西里爾、日文、韓文、簡體中文、繁體中文）。P2–P7 下半頁留白為本模板設計（每頁 2 條），與其他已通過的 W43 封面一致。
- 幾何遮擋審計：`tools/occlusion_audit.py`（自檢通過，六類陽性對照全數觸發）對 SVG 目錄回報 **0 flags，CLEAN**。
- 文字層 PDF：`tools/webpdf.py` 產出 cover-w43-zh-tw.pdf，**801,372 位元組（< 7 MB）**，8 頁，pdftotext 提取 **9,627 位元組**，12/12 標題皆可自 PDF 提取；P1 含 COVER、不含 VOL。

## 發現與修正的問題

1. **P7 禁則（kinsoku）孤標點（初版目檢發現，已修正）**：簡體摘錄出現「。」行首孤字，繁體解說出現「「」行末孤字。修正：在 build.py 的 wrap() 中加入禁則處理——句末標點（。，、；：！？」』）》）一律黏附前一 token，句首標點（「『（《〈）一律黏附後一 token。重建後全 8 頁掃描孤標點為 0，重檢 P7 無溢出，遮擋審計仍為 CLEAN。
2. **颱風名警示（2026-10-28 協調員追加檢查，已處理）**：初版 KO 條解說只寫原生韓文名「참피」，未含拉丁名；zh-tw 條解說寫「薔琵」，無拉丁名。按警示要求，KO 條補上拉丁名注釋，定稿為「참피 (Champi)」；zh-tw 條「薔琵」無拉丁名，符合警示明文許可（native characters 薔琵 with no Latin name — acceptable），維持不變。定稿全冊（含 SVG、PDF 文字層）grep 確認：Chanpi、Changpi、Fung-wong 皆為 0 命中；Champi 出現於 P6 KO 解說；薔琵出現於 P1、P7、P8。逐字標題與摘錄在本次修正中完全未動。
3. **無其他問題**：其餘 7 頁初版即通過目檢與審計；無溢出、無缺字、無重疊。

## 檔案

- 製作目錄：`hidden_files/cover-w43-zh-tw-build/`（build.py、svg/、png/、occlusion.json）
- 成品目錄：`files/cover-w43-zh-tw/`（svg/ ＋ cover-w43-zh-tw.pdf ＋ 本文件）
- 不動 git（依任務要求，本次不提交、不推送）。
