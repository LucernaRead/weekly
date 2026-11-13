# GATE-LOG — W47 core-zh-tw re-proof：fix1 + fix2 後全套機械門獨立重跑記錄

- **復校對象**：`~/workspace/weekly-git/production/2026-w47/core-zh-tw/`（fix2 交付狀態，未動）
- **工具**：`~/workspace/weekly-git/tools/venv/bin/python`（共享工具，永不去 /tmp）
- **日誌目錄（絕對路徑）**：
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-core-zh-tw-reproof/`
- **時間**：2026-11-11 09:24–09:3x UTC
- **探針**：每次寫盤前 `git hash-object -w` rc=0。註：`/tmp` 已滿（512M tmpfs 100%，他線遺留物），
  全部中間輸出寫入本目錄，未寫 /tmp。
- **未重建**：按任務紅線，未跑 run.py / render.py / webpdf.py / export（未重建、不改源）。
  freeze 門改以 SHA 比對驗證（見 §6）。

## 0. 交付物（盤上實測，與任務指定值逐字一致）

- print `Lucerna-VOL4.pdf` 19,419,829 B / SHA `3ab3f75815444d6b6da389f026e82a17e4d747226698083c16f6b26523d3474e`
- web `Lucerna-VOL4-web.pdf` 2,323,405 B（< 7 MB）/ SHA `582c4aa7b1a90a065c5d5e5e0f4b7219394a0089b67ee1791d2e700c8d46938e`
- text `2026-w47-zh-tw-en.text.md` 49,735 B / SHA `7e1a45165dc663af5301d95784567b03f4e9f512766571e507663086d510791c`
  （與 KIT L53/L129/L144 登記一致；fix2 稱 `7e1a4516…0791c`，盤上實測全值相符）
- 雙 PDF 各 8 頁、1462.5×2025 pt（PyMuPDF 實測）

## 1. 文字層一致（print.txt / web.txt，pdftotext -layout）

- print 101,415 B；web 101,415 B（均 > 0，有文字層）。逐頁字符數雙版完全相同
  （P1 2226 / P2 2685 / P3 3128 / P4 2344 / P5 3165 / P6 2342 / P7 3567 / P8 8982）。
- 字符多重集差：print-only **0**；web-only **0**（本跑 -layout 模式下零差異；
  fix2 非 -layout 模式記 web 僅多 1 換行 artifact，本跑未再現）。
- `本週日` print/web 各 11×；`下週日` 各 0；`BABYMONSTER` 各 0；`台北演唱會` 各 0；
  `香港11月節目` 各 1。
- **結論：文字層完整一致，PASS。**

## 2. occlusion_audit.py（occlusion-selftest.log / occlusion.log / occlusion.json）

- `--selftest` rc=0：6 類皆觸發（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），乾淨對照沉默。
- 本版審計 rc=0：**0 flags**（`flag_count: 0`）。
- **結論：PASS。**

## 3. checks.py（checks.log）— rc=0 PASS

- 本週金句 8 句各 2 次（文章＋P7）。
- SIMP_ONLY_HITS []（無簡體字）。
- P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]——與預期一致。

## 4. p8.py（p8-extract.log/.json / p8-compare.log/.json）

- `extract --p8 svg/p8-test.svg --total 150` rc=0：noted set = **150/150**。
- `compare`（本核心 P8 vs `../2026-w47-zh-tw-de/svg/p8-test.svg`，fan-out 德語讀者版）rc=0：
  **CLEAN**，missing=[] extra_count=0 uncertain=[] keydiff=[]。
  （對照版文件 mtime 2026-11-11 01:58；與 fix1/fix2 同一對照，結果一致。）
- **結論：PASS。**（fix2 稱對 zh-tw-de CLEAN keydiff=[]——獨立重跑核實一致。）

## 5. P5 幾何核查（SVG 實測，fix2 數值逐項復核）

- 香港表框：y=1405.6、h=418 → 底 1823.6 ✓（fix2：480→418）
- 5 行基線：1503.6 / 1565.3（爵士行折行續 1595.0）/ 1656.7 / 1718.4 / 1780.1；
  末行底距 43.5px（改前 43.8px），無多餘留白 ✓
- 爵士表框：y=1841.6（改前 1903.6，上移 62px）、h=430、底 2271.6；框間距 18px 不變；
  距頁腳線 2596 有 324.4px ✓
- 爵士表內容：標題 1885.6；4 dated 行 1939.6（+1969.3 折行）/ 2031.0（+2060.7）/ 2122.4 / 2184.1；
  末行「戶外舞台免費，室內場要買票」2245.8，皆在框內（1841.6–2271.6）✓
- `BABYMONSTER` 在 p5-youth.svg 中 0 命中 ✓
- **結論：PASS，D2 幾何全數復核一致。**

## 6. freeze（SHA 比對，未重建——任務紅線不重建）

- 盤上 8 個 SVG 的 SHA-256 全值（本次實測）：
  - p1-front `0a362c6eca296456fac7a50a88c96992c2cae069208605e5f8b0ec0d5143f880`
  - p2-life `55378c704c4030760f64b79bccb0b862bc2b2744c4b6930df30a965286cb2c56`
  - p3-culture `1ef686586ca28490cc9be22a0e7a78a4f0314b433e7776f3eb2132bed95c5656`
  - p4-sport `182d930169be0a18cd88d5b5e4d92c6e4a44550313e529db071b8122526d6b07`
  - p5-youth `183e0bc4691239d693f846dffd1ec7b397bd2654aebad10f951abc4c2952fdbf`
  - p6-deep `906ddb0d5c893ff4f50f2c3963ac08402ef75cab7d6d8aeb0965d35db82b21bc`
  - p7-lang `292a5110ad85f799c4ed4f21ba5b308489053ba11ebf3cced7ff297e0266e21b`
  - p8-test `8e65cb3f67c261fe03d4eece01c81b5022874e317d4909cd9189e18fe4ecf25d`
- 與 fix1 freeze-base 記錄逐頁比對：p1/p2/p3/p4/p6/p7/p8 前 16 位哈希與 fix1 完全相同；
  **僅 p5-youth.svg 不同**（fix1 `3b257230…` → 本次 `183e0bc4…`），且與 fix2 的 freeze 記錄值一致；
  與 fix2 `svg-hashes-before.txt` 8 行逐字相同。
- **結論：8/8 核實通過——僅 P5 與 fix1 不同，其餘 7 頁與 fix1 逐字節同。**
  （方法說明：未跑 `freeze.py baseline` 重建，改以交付 SVG 哈希對 fix1/fix2 的基線記錄比對；
  fix2 自己的 freeze baseline 已驗證重建產物與交付 SVG 逐字節相同，本次比對建立在其上。）

## 7. 彎撇／彎引號全掃（U+2018/U+2019/U+201C/U+201D，Python 按碼點計數）

- SVG 8 頁＋text.md 全掃：**0 命中**。PASS。
- 另：text.md 與雙 PDF 文字層 `本週日` 11 / `下週日` 0 / `BABYMONSTER` 0（見 §1）；
  源 .py `下週日` 0、`本週日` 4+5+1+1=11、`BABYMONSTER` 0。

## 8. P8 最小字號與 §1.1 顏色（PyMuPDF）

- P8 最小字號：print 與 web 雙 PDF 皆 **9.75pt**（= §1.1 下限）；P8 最大 34.5pt（欄目標題）。
- 雙 PDF 逐頁文字字符數一致（見 §1）。
- **結論：PASS。**

## 9. 雙 PDF 逐版目視（cards/ 8 張渲染圖，P1–P8）

- **P1**：副題「封王遊行，本週日天母出發！」✓；正文「訂在本週日（11月22日）」✓；
  本週大事「本週日 11/22 遊行、金馬獎、鋼雕閉幕、小雪」✓。無溢出／重疊／壓頁腳。
- **P2**：小雪首段「本週日（11月22日）是小雪」✓；雨天照片＋出處 ✓。全版乾淨。
- **P3**：標題「金馬獎本週日頒獎，誰會得獎？」✓；正文「頒獎典禮在本週日（11月22日）舉行」✓；
  月球照片＋出處 ✓。全版乾淨。
- **P4**：標題「本週日，封王遊行天母出發！」✓；正文「訂在本週日（11月22日）」✓；
  圖注「本週日，龍隊封王遊行從天母出發。」✓；U 幣柱狀圖比例正確 ✓。全版乾淨。
- **P5**：香港表 5 行末行「迪士尼聖誕音樂會：11月21、22日」，框底距均勻；爵士表 5 行完整，無碰撞；
  維港照片＋出處 ✓。**D2 目視通過。**
- **P6**：時間軸 5 點（14:00/17:00/18:30/19:00/20:00）標籤相鄰無重疊；Q95 題面「四件大事同一天，要學會___。」可見。
  全版乾淨（D3 內容問題見 PROOF-NOTE §4，非版式問題）。
- **P7**：來信「編輯好：本週日我要去看封王遊行」✓；下期預告「下週：金馬獎得獎名單、封王遊行直擊、鋼雕閉幕現場……下週見！」
  **完整保留，未動**✓；金句 8 句＋頁碼標註 ✓；延期披露中英俱全 ✓。全版乾淨。
- **P8**：E 144「—封王遊行哪天出發？—本週日___出發。(A. 11月22日 · B. 11月15日)」✓；
  150 鍵齊全，鍵區末行在頁腳線上方 ✓。全版乾淨。
- **結論：8 版逐版目視全數通過（版式）；內容缺陷 1 條見 PROOF-NOTE §4。**

## 10. 內容系統性核查（補充機械門）

- keys 區逐行分類：單選 79、配對 16、填空 54、寫作 1，合計 150，與 KIT 題型統計一致。
- 填空鍵答案詞正文出現核查：54 個中 53 個出現於正文（keys 區之前），唯一例外 `取捨`（Q95）——見 PROOF-NOTE §4 D3。
- 寫作範文 142 字符（全文字符計數；去標點後 126），落在 120–180 字帶內 ✓。
- `松菸大道` 碼點核實：全部 5 處為 松 + U+83F8 菸 ✓。
- W46 封王查證：`production/2026-w46/core-zh-tw/2026-w46-zh-tw-en.text.md` L966
  「封王：拿下總冠軍，叫封王」——P4「上週本報已經教過這個詞了」屬實 ✓。
- ABSTRACT.txt：單行、無 ASCII 雙引號（grep -c '"' = 0）、英文 ✓。

## 總結

| 門 | 結果 |
|---|---|
| 交付物 SHA/尺寸 | 全符（§0） |
| occlusion_audit.py（自檢先過） | 0 flags |
| p8.py extract --total 150 | 150/150 |
| p8.py compare（本核心 vs zh-tw-de） | CLEAN，keydiff=[] |
| freeze（SHA 比對，未重建） | 8/8（僅 P5 與 fix1 不同） |
| checks.py | PASS（金句 8×2、簡體 0、圖表幾何一致） |
| print/web 文字層多重集差 | 0 / 0（-layout 模式） |
| U+2018/U+2019/U+201C/U+201D 全掃 | 0 |
| P8 最小字號（雙 PDF） | 9.75pt（= §1.1 下限） |
| P5 幾何（D2） | 全數復核一致 |
| D1 回歸（本週日/下週日） | 11/11、0 |
| 雙 PDF 逐版目視 | 8/8 通過（版式） |
| 內容全量復校 | **1 條輕微缺陷 D3（Q95 取捨未在本期出現），見 PROOF-NOTE §4** |

## 未做事項（按任務範圍）

- 未改任何源文件、未重建、未 commit、未 push、未動其他家庭、未派 subagent。
- 未跑 insert.py、lint --write；未做任何 git 寫操作（除探針 `hash-object` 外）。
