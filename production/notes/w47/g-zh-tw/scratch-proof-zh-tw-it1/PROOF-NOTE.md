# PROOF-NOTE — W47 zh-tw-it proof1（独立复校，2026-11-11）

- 版：`production/2026-w47/2026-w47-zh-tw-it/`，VOL.4，繁體中文正文 × 意大利語講解；重 fan-out 新建，未 commit 未 push。
- 校對：proof1 獨立全量復校（text.md 全文通讀；印 PDF 8 頁自行渲染逐頁目视，网版 P1 亦看過；150 題三源手驗；全部機械門獨立重跑）。
- **結論：(a) 零問題，可定稿。**

## 0. 前情：本 scratch 曾有上一輪 proof1 殘件（已歸檔）

本目錄在開工前已存一份上一輪 proof1 的 `PROOF-NOTE.md` / `GATE-LOG.md` / `d2-scan*.json`（2026-11-11 09:05 UTC），針對的是**舊版**成品（印 `ec9d0624…` 19,420,291 B、网 `34c4ff2c…` 2,306,683 B），結論 (b)，缺陷 D1（「下週日」×11）、D2（网 PDF abutting 缺口 9 處）、D3（意大利語 è 誤用 ×5）。為免混淆，上述舊件已移入本目錄 `prev-proof1-old-build/` 原樣保存。

**本輪逐項復驗舊輪 D1/D2/D3（針對當前新版，SHA 見 §1）：三項皆已修好**——D1：text.md「下週日」0 處、「本週日」11 處；D2：`d2scan-it.py` 重掃 1,268 對，最差网缺口 0.05 pt，>0.5 pt 者 **0**（网 PDF 建於 11:20 UTC，用已補丁 `tools/webpdf.py`，見門禁表）；D3：`è tutti/è ogni/è in tutto` 全文 0 處，5 處已改為 `si tiene` / `si ripete` / `prevede`。舊輪觀察 O1（`domenica prossima`）亦已消失（全文僅剩「La prossima settimana (VOL.5)」一處，義為「下週」，正確）；O2、O3 仍在，見 §4 觀察項。

## 1. SHA 核對（逐字核對，通過）

| 文件 | 字节 | SHA-256 | 任务给定 | 结果 |
|---|---|---|---|---|
| it 印 `Lucerna-VOL4-IT.pdf` | 19,420,437 | `5594005aae1b2ff3b69ae37edf191dc482f2c3773b29a1cdc75c72ce5b485ce9` | `5594005aae1b2ff3…` / 19,420,437 | ✓ |
| it 网 `Lucerna-VOL4-IT-web.pdf` | 2,323,037 | `a0d80c26bdc7c8eb6029af991c4d14e8af966f0e3f6d3a066f74f98bf220d0a5` | `a0d80c26bdc7c8eb…` / 2,323,037 | ✓ |
| it text.md | 51,685 | `48e04f1540a9b6bcf292f9163af32707ac2ba54bcd91b18a127f45903dc12ba7` | `48e04f1540a9b6bc…` / 51,685 | ✓ |
| core 印 `Lucerna-VOL4.pdf` | 19,420,552 | `5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a` | `5ec35fe2…` | ✓ |
| core 网 `Lucerna-VOL4-web.pdf` | 2,324,042 | `1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240` | `1c0799ac…` | ✓ |
| core text.md `2026-w47-zh-tw-en.text.md` | 49,798 | `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b` | `09e083e1…` | ✓ |

核心目录为 `production/2026-w47/core-zh-tw/`（经全目录 SHA 检索定位；任务所写 `2026-w47-zh-tw/` 不存在）。重建前后核心未变（freeze 自报 8 檔重哈希未变）。
复校期间生产文件零改动：it 目录内无一文件新于开工探针时间；工作树其余 `M` 改动（107 处，W43 相关，mtime 2026-11-10 17:44 UTC）早于本次会话，与本次复校无关。

## 2. 缺陷清单

**无。D1…Dn：0 项。**

## 3. 逐项实测（全部机械门独立重跑，见 GATE-LOG.md；此处只记实测值）

- **freeze baseline（第一步）**：`tools/venv/bin/python tools/freeze.py baseline` → **8/8** SVG 字节一致（p1 4ed936c2、p2 ec470f0c、p3 eca7b6e8、p4 7ffa59f7、p5 41823b2c、p6 cfcae666、p7 61a2f200、p8 bd19e134），核心完整性 OK。日志 `freeze.log`。
- **checks.py**：`CHECKS PASS`（rc=0）。8 金句各出现 2 次；SIMP_ONLY_HITS []；P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]。
- **occlusion**：selftest rc=0，audit flags **0**。
- **p8**：extract 150/150；compare vs core **CLEAN**，keydiff []、missing []、extra []（gates.json 里 extra 显示 "?" 是驱动读错 key 名的老 bug，已直接读 `p8-compare.json` 纠正）。
- **canonical creambox**：36 盒，负 clearance **0**；各页最小内 clearance P1 18.8、P2 41.8、P3 15.8、P4 35.8、P5 6.4、P6 19.9、P7 12.5；P7 工具盒 12.5 / 14.0。
- **boxtitle**：36 盒，超框 **0**，最小标题右余 **13.8 px**（逐盒 `gates/it-proof1/boxtitle.json`）。
- **PIL creambox**：STRADDLE 2（§4 O4 专项裁决，观察项）、CREAM-COVER **0**、P7 最小底 clearance 9.5 px。
- **印/网文字层**：`pdftotext -layout` 印 = 网 = 111,245 B，多重集差 **0**；本週日 11、下週日 0、取捨 2、小雪 36，印网一致。位置差分（PyMuPDF 逐词坐标计数器）：4,704 词，**仅 1 词**坐标不同——P1 刊头 "Lucerna"（印 (499.1, 62.8)–(956.9, 209.8)，网 (501.7, 81.3)–(960.2, 233.2)）；对照核心 print/web 为同一词、同一坐标、同一位移，属 webpdf 管线固有属性，非 it 版缺陷；其余 4,703 词坐标逐字相同。网版 P1 渲染目视与印版一致。
- **P8 最小字号**：印/网均为 **9.75 pt**（≥9.75，下限值），最大 34.5 pt；8 页，1462.5×2025.0 pt。
- **keycheck**：填空键 54 个，缺失 0；答案键 1–150 连续。
- **leak scan**：deny 命中 **0**；唯一与核心共有的长 ASCII 串为选项行 `A. 12:00 · B. 14:00 · C. 19:00`（构造共享，非泄漏）。
- **abutting**：P6 18:30「頒獎典禮」墨右缘 990.8 与 19:00「夜間遊行」墨左缘 991.4，缝 **0.6 px**（与核心先例完全一致，发丝缝，无重叠）。
- **网 PDF abutting 全掃（d2scan-it.py，舊輪 D2 之復驗）**：1,268 對，最差网缺口 **0.05 pt**，>0.5 pt 者 **0**。网 PDF 建於 2026-11-11 11:20 UTC，`tools/webpdf.py`（09:10 UTC）已含 `:weight=100/200` 補丁。
- **150 题三源交叉**（`keycheck-150.json`）：(1) 正文事实、(2) text.md 答案区、(3) svg/p8-test.svg 提取键——**150/150 PASS**，text.md 键与 SVG 键逐题值相同。算术独立重算：1200+800=2000、2000−1200=800、11/6–11/22 含首尾 17 天、17:00–18:30=1.5h、5×10=50、100−70=30、14+31+3=48、11/17–11/22 含首尾 6 天、14:00–19:00=5h、17:30–23:00 每半小時共 12 場、11/13–12/27 共 45 天，全部正确。匹配组 25–28 / 43–46 / 61–64 / 79–82 按集合核对无误。Q150 范文 142 字（120–180 范围内），内容与 P1/P6 事实一致。
- **彎引号全扫**：SVG 文本内容直双引号 `"` 0 处；直单引号 `'` 61 处，全部为意大利语省音（l'ultima、dell'inverno、mezz'ora 等）；弯单引号 ’ 0 处、弯双引号 0 处。对照：核心 en 直 ' 28 处、fr 86 处，弯引号全周 0 处——直撇为全周统一写法，非缺陷。
- **简体字扫查**：checks.py SIMP_ONLY_HITS []；另行扫查仅 `互` ×4，均在「互動」（球員互動）中——「互」为繁简同形字，非简体。
- **E 节 type 标签繁体本地化**：A 判斷對錯、B 本週大測驗、C 完成句子、D 讀一讀，答一答、E 情景說話、F 寫一寫，全部繁体，意大利语副标齐全。
- **「next Sunday」冻结核对**：`scratch-refanout-zh-tw/tables.py:245/:267/:322` 仍为 next/Next Sunday；核心 `content12.py:37/:113`、`content34.py:127` 亦然；it 版 SVG/text.md 内「next Sunday」0 处。按任务要求**不列为缺陷**。
- **目视**：印 PDF 8 页逐页自行渲染（`render/p-1.png`…`p-8.png`，110 dpi）全部看过；网版 P1 亦看过。无溢出、无重叠、无页脚碰撞；P6 时间轴 18:30/19:00 两标签目视相邻不重叠；P4 条形 10/50/100 比例正确；图片与署名位置确认。细节：Q128 选项 B 在印版渲染中折为「5小/時」两行——栏内换行，非错误。

## 4. 观察项（非缺陷，供协调员判断）

- **O1（STRADDLE，双语小檔标题伸出米色盒右缘，沿用 builder §7 未决项 2）**：P1「本週一詞　Parola della settimana」+0.8 px、P2「耶誕城小檔　Scheda Christmasland」+24.5 px。逐处实测 + 旧版对照（备份 `scratch-refanout-zh-tw/backup/2026-w47-zh-tw-it/svg` 同一扫描）：旧版同样 2 处、**坐标逐字相同**，重建引入回归 0 处；两处字形在渲染中完整可读、无裁切；伸出部分落在页右空白边（页宽 1950，墨迹最远 1886.5），其右无任何元素、无可见边线。三项缺陷标准皆不满足，故为观察项。缩短标题属设计决定，待协调员定夺。
- **O2（沿用舊輪觀察，鍵 83/86 譯法偏弱）**：鍵 83「il segnale più presto」、鍵 86「l'ultimo segnale」譯英 "marker"（時間軸標記）可解但欠準；建議改「il primo orario」／「l'ultimo orario」，非強制。
- **O3（沿用舊輪觀察，P4 欄頭）**：「La parata scudetto e i punti sport」——「punti sport」勉強可解，標準寫法「punti sportivi」。
- **O4（未核實細節，核心繼承）**：P5「史黛西·肯特在自由空間連開兩場」——本輪檢索只見到 11/17 一場之記載（U Lifestyle 售票時間表），未獨立證實亦未證偽；屬核心繼承內容，非 it 版引入，不列缺陷。

## 5. 外部事实独立核查（2026-11-11 检索，全部属实）

- 味全龍第 6 冠、封王遊行 11/22 14:00 天母→大巨蛋松菸大道、感謝祭 11/21–22、U-Sport 267 間 5→10 幣、满 100 换悠遊卡储值金（卡優新聞網 2026-11-06、聚傳媒 2026-11-07、夠棒網 2026-10-30）。
- 第 63 屆金馬獎 11/22 台北流行音樂中心、17:00 星光大道、18:30 典禮、柯煒林首主持、587 部報名、入圍 10/1 公布、《狂忘警探》11 項、主題「再見江湖」、影展 11/6–11/22（applealmond、YOLO LAB、風采、K-MEDIA）。
- 小雪 2026-11-22（週日 15:23 交节）、二十四節氣第 20 個、立冬之後（香港天文台 2026 年表）。
- 新北耶誕城 11/13–12/27 共 45 天、卡娜赫拉、主燈秀 17:30–23:00 每半小時 5 分鐘、7 處燈區、德國市集 12/4–6（卡優新聞網、HouseFeel、WOMENT）。
- 香港迪士尼聖誕 11/17–2027-1/3 共 48 天、魔雪奇緣世界首個冬日市集、11/19 新日間城堡演出、亮燈+無人機、音樂會 11/21–22、12/5–6 共 4 場、雙重暢玩任選兩天（yourdisney、konggokhk、superpama、POPBEE）。
- 西九爵士音樂節第 8 屆、11/13–15、17–22、24（10 天）、Diana Krall 11/13 開幕、Cory Wong×何卓彥 11/15、Stacey Kent 11/17 自由空間、Kenny G 11/24 竹翠公園收尾（jazznode、hongkonglei、thehkhub、U Lifestyle）。
- 六福村墓碑鎮 10 週年 9/12–11/22、夜間遊行《鹿魔覺醒》19:00（週五–週日）、5 米鹿魔、日間《異界狂想曲》每日 14:00 週二休演（產經新聞網 2026-10-20、gofunit）。
- 高雄鋼雕藝術節 10/23–11/22、SUPER STAGE、SUPER SAFE 保險箱、駁二 B3/哈瑪星/鹽埕、平日 10–18 週五週末至 20:00、林洪玉秀 85 歲《萬年吉祥花》、鹽埕學裁縫縫婚紗（高雄市政府新聞局、中央社 2026-10-29）。
- 寶可夢 30 週年又一城 11/11 起、巨型皮卡丘氣球、10 米精靈球燈光裝飾、官方快閃店（konggokhk、U Lifestyle、likemagazine）。

## 6. 红线遵守

只读生产文件：未改任何成品、未 commit、未 push。活动范围仅 `production/2026-w47/`（读）与 `hidden_files/w47/`（写本 scratch）。
