# es-zh-tw — fan-out build record (2026-11-11)

10/10 完成。繁體中文讀者版（台灣用法），獨立成版、絕不由簡中轉換。
Build 1 即終版（run 0 溢出、P8-keys 2506、P8 診斷僅 #139 一項多行且為 core 一致），
無需 build 2。

## 交付

- print `La-Lucerna-VOL4-es-zh-tw.pdf` — 17,262,202 B,
  SHA-256 `23926bd9729a041142472d066f0be2365d0edb54af3771e35e83e4d870ab8ff6`
- web `La-Lucerna-VOL4-es-zh-tw-web.pdf` — 1,686,124 B,
  SHA-256 `3e96ea85cb5bfe3cdadd1d1ef1b861c26d4954ddca4daf1798738b03dd573920`
  （render.py 內調 tools/webpdf.py；pdftotext print = web，44,169 B，
  token 多重集一致；< 7 MB）
- 8 SVG + 8 PNG（cards/）+ `.text.md` 1,786 行 + `ABSTRACT.txt`（繁中一行，
  無 ASCII 雙引號）+ `WEEKLY-KIT.md`

## 門禁（全過）

- run.py rc=0，零 FLOW OVERFLOW / HEAD TOO WIDE，TOTAL 150
  （A2 50 / B1 72 / B2 28；每頁 10/18/18/18/18/18/12/38）
- P8-keys 終 y=2506（餘 54px）；P8-ex y=842（底 1252）
- occlusion 0 flags；bridge 孤兒 0/20、box-vs-hline 0、bridge widow 0
- p8 extract 150/150；compare CLEAN，keydiff=[137, 138] 已裁定
- freeze：工具 8 OK + 直接 sha256（build-copy/svg vs 發貨 svg/）8/8
- P8 最小字號 10.125pt（Tm 解析：150 條目，最小 |a| 10.125，與 core-es
  完全相同；見 §6.10——Tm 正則須允許負號 `d 0 0 -d`，否則 0 命中）
- §1.1 逐項實測：紙色 #fbfaf6 ×8；masthead 196 units = 147pt；
  VOL.4 ×9、VOL.5 ×3（均合法下周前指）；P8 徽章 rect A2 11 / B1 21 /
  B2 3 = 35 個 + 1 個 #37402f header band rect（與 core 相同）；
  Q113–120、Q145–149、寫作標題徽章無缺失（目視確認）
- 8 版渲染圖逐版目視；150 鍵逐題復核（.text.md 1,786 行全文讀完，
  鍵 1–150 無缺；答案與題幹逐題對上）
- gloss 詞元計數（§8.1，裸詞）：P1 6/11/3/6/2、P2 5/2/2/2、
  P3 5/6/9/4/5、P4 19/7/3/2/2、P5 5/2/3/3/5，全部 ≥2
- 無 “12 de noviembre”；無簡體字殘留（見下）

## 本版唯一真缺陷：收穫漏譯 “本周计划”

- apply：487 替換；manual-over-harvest 0。收穫表 232 鍵、142 項缺失。
- leftover 清單 22 項：除 “EL PLAN DE LA SEMANA　本周计划” 外，全部經
  opencc s2t 驗證為簡繁同形（完成句子、填空、造句、球迷很多、吉他、
  榜首、德比、歌唱、舞蹈、原形、期限、第8版、投票箱在哪、第一次投票、
  VIDA　生活、CULTURA　文化、JUVENTUD　青年）——key==value，無需譯。
- 例外：收穫表把 “EL PLAN DE LA SEMANA　本周计划” 原樣返回（未譯）。
  全檔案 opencc 短語級審計（6 個 .py 全部雙引號字串）共 6 處差異：
  5 處為 opencc 誤報——公布/宣布用 布、電台用 台，皆為正確台灣繁體
  （佈只用於佈置、臺只用於臺灣/樓臺）；1 處真漏：本周计划 → 本週計劃
  （content56.py:22，P5 盒標題），建前手動修掉。
- 單引號 CJK 字串：0。修後 .text.md 再審：僅同一 5 處 布/台 差異，
  真簡體字 0 個。

## 預建修（6 處，count 斷言全中）

1. P1 gloss：收穫 2 行（418.0 units）→「辯論」：人們公開討論。
   （228.0，1 行；與 ja/ko 同款短式）
2. P6 band：讀懂競選 → 讀懂競選：辯論、政綱與民調
   （全文 sans 18 = 759.7 / 1684）
3. P8 頭 1302→1337、keys flow 1328→1363（右注 334.1 units @19.5，
   標題 493.5 @25，本無碰撞，仍按通則移位）
4. letter 全角括號 → 半角（W46 先例）
5. 本週計劃修復（見上，建前）
6. 其餘全部保留不動：P7 gloss 2 行 @20、ed note 3 行 @20（P7 col3
   精確落在 core 值 1844.51）；ERRORES 4 條全 1 行；your-turn
   P2 3 行、P3 2 行、P4 3 行、P5 3 行，全部 @20（盒底 P2 964.0、
   P3 1571.75、P4 935.5、P5 1580.55，距 1608 分隔線 27–36px 餘量）；
   橋句全部 1 行（P6 D 為 2 行且兩行有內容），無 widow。

## P8 診斷

- REG 在 /tmp 副本中跑全版後算（不動發貨 SVG）：多行項僅 #139
  （core 一致換行，保留）；#44 渲染亦 2 行（時間在前，動詞第 / 二，
  core 一致）；#137/#138 為翻譯題重定向，鍵為繁體中文句，注
  “對照原文”，keydiff 已裁定；#150 ✓ 形式
  “範文見本版 H 區（97 詞）”，與 MODELO 97 詞一致。
- 寫作類型名為 “寫作”（content8.py:134）。

## 目視備註

- P5 your-turn 第 3 行以 “？” 起首、P3 “「魂」” 跨行斷開：渲染器
  字符級 CJK 斷行，與 core 自身中文換行同類，非缺陷，保留。
- P7 A2 欄中文 “比賽在 a las 21:00 開球。”——低解析度下易誤讀為
  “開先”，源串確為 “開球”，無誤。
- P1 gloss、P5 “本週計劃”、P6 band 補全、P8 頭移位均在渲染中確認。

## 工具

- 導出器：`extract_text_es_zh-tw.py`（ko 修復版的 sed 副本；
  CJK-aware 寬度 + 跨欄切分；hangul 區間對繁體無害）。無 “282.”
  式假鍵；.text.md 鍵 1–150 齊全。
- sweep_de.py 三項全 0；Tm 解析見 KIT §6.10（負號正則）。

## 記錄

- 本檔案即子記錄；`FANOUT-REPORT-es.md` 已更新（es-zh-tw 行 +
  checklist 勾選）；KIT 為 `2026-w47-es-zh-tw/WEEKLY-KIT.md`。
- 診斷副本 /tmp/zh-tw-diag、PNG /tmp/zh-tw-png、/tmp/zh-tw-*.txt
  均為臨時區，可丟；發貨文件全在版目錄內。
