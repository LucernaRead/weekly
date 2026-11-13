# GATE-LOG — W47 zh-tw-it proof1（独立复校，2026-11-11）

工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-zh-tw-it1/`
`TMPDIR` = 该目录下 `tmp/`（未用 /tmp）。全部构建/门禁一律 `~/workspace/weekly-git/tools/venv/bin/python`（正典栈），除注明外无系统 python3。
探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；hidden_files 写文件成功。两者皆通后开工。
注意：本 scratch 开工前已存上一輪 proof1 殘件（針對舊版成品，印 `ec9d0624…`），已移入 `prev-proof1-old-build/` 原樣保存，不屬本輪。

## 0. 身份核对（SHA-256 + 字节，逐字核对）

```sh
sha256sum Lucerna-VOL4-IT.pdf Lucerna-VOL4-IT-web.pdf 2026-w47-zh-tw-it.text.md
# 5594005aae1b2ff3b69ae37edf191dc482f2c3773b29a1cdc75c72ce5b485ce9  19420437B ✓
# a0d80c26bdc7c8eb6029af991c4d14e8af966f0e3f6d3a066f74f98bf220d0a5  2323037B ✓
# 48e04f1540a9b6bcf292f9163af32707ac2ba54bcd91b18a127f45903dc12ba7  51685B ✓
sha256sum core-zh-tw/Lucerna-VOL4.pdf core-zh-tw/Lucerna-VOL4-web.pdf core-zh-tw/2026-w47-zh-tw-en.text.md
# 5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a  19420552B ✓
# 1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240  2324042B ✓
# 09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b  49798B ✓
```
核心目录为 `production/2026-w47/core-zh-tw/`（经全目录 SHA 检索定位）。it 版 `git status` 为 `??`（未 commit 未 push）。
复校后核查：it 目录内无一文件新于开工探针时间；工作树其余 `M` 改动（107 处，W43 相关，mtime 2026-11-10 17:44 UTC）早于本次会话。

## 1. freeze baseline（第一步，先行）

```sh
cd production/2026-w47/2026-w47-zh-tw-it
tools/venv/bin/python tools/freeze.py baseline --build . --core-svg svg --out <scratch>/freeze-base
# runtime: venv python | Pillow 13.0.0 | FreeType 2.14.3
# baseline: 8/8 SVGs byte-identical (repointed: content56.py, content12.py, content34.py, content7.py, content8.py)
#   OK p1 4ed936c2 / p2 ec470f0c / p3 eca7b6e8 / p4 7ffa59f7 / p5 41823b2c / p6 cfcae666 / p7 61a2f200 / p8 bd19e134
# core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
```
结果：**8/8**，继续全量复校。日志：`freeze.log`。

## 2. 独立门禁总跑（gates-proof1.py — builder gates.py 的副本，M 路径改到本 scratch；两处 `python3` 调用改为 VENV python）

```sh
tools/venv/bin/python gates-proof1.py it proof1   # 输出 gates/it-proof1/gates.json + 各门日志
```
结果（`gates/it-proof1/gates.json`，逐门独立重跑，与 builder 报告 §6 逐项一致）：

| 门 | 结果 |
|---|---|
| checks.py | rc=0，**CHECKS PASS**。8 金句各 2 次；SIMP_ONLY_HITS []；P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43] |
| occlusion | selftest rc=0，audit flags **0** |
| p8 extract + compare | extract 150/150；compare **CLEAN**，keydiff []，missing []，extra []（gates.json 里 extra 显示 "?" 是驱动读错 key 名的老 bug，已直接读 `p8-compare.json` 纠正：`"extra": []`） |
| canonical creambox | 36 盒；负 clearance **0**；各页最小内 clearance：P1 18.8、P2 41.8、P3 15.8、P4 35.8、P5 6.4、P6 19.9、P7 12.5；P7 工具盒 clearance 12.5 / 14.0 |
| boxtitle | 36 盒，超框 **0**，最小标题右余 **13.8 px**（逐盒见 `gates/it-proof1/boxtitle.json`） |
| creambox-pil | **STRADDLE 2**（§3 专项裁决），CREAM-COVER **0**，P7 最小底 clearance 9.5 px |
| text layer 印/网 | print_bytes = web_bytes = 111,245；多重集差 **0**；本週日 11 / 下週日 0 / 取捨 2 / 小雪 36，印网一致 |
| PDF metrics | 印/网各 8 页，1462.5×2025.0 pt；**P8 最小字号 9.75 pt**（≥9.75，等于下限），最大 34.5 pt；P1 最大字号 147.0 pt |
| keycheck | 填空键 54 个，缺失 0；答案键 1–150 连续 ✓（150 个） |
| leak scan | deny 命中 **0**；唯一与核心共有的长 ASCII 串为选项行 `A. 12:00 · B. 14:00 · C. 19:00`（构造共享，非泄漏） |
| abutting | P6 18:30「頒獎典禮」墨右缘 990.8 与 19:00「夜間遊行」墨左缘 991.4，缝 **0.6 px**（与核心先例完全一致） |
| freeze（门内重跑） | **8/8**，rc=0 |
| files | SHA/字节与 §0 一致 |

## 3. STRADDLE 专项（builder §7 未决项 2，逐处实测 + 旧版对照）

新版扫描（`gates/it-proof1/creambox-pil.log`）：
- P1「本週一詞　Parola della settimana」ink 右缘 1862.8 vs 盒右缘 1862.0 → **+0.8 px**
- P2「耶誕城小檔　Scheda Christmasland」ink 右缘 1886.5 vs 盒右缘 1862.0 → **+24.5 px**

旧版对照：对 `scratch-refanout-zh-tw/backup/2026-w47-zh-tw-it/svg` 跑同一 `creambox-pil.py`（`old-it-check/creambox-pil-old.log`）→ STRADDLE 同样 2 处，**坐标与新版逐字相同**（P1 1862.8 / P2 1886.5），CREAM-COVER 0。
裁决三标准：(a) 字形被裁切——否，两处标题在印 PDF 渲染中字形完整；(b) 墨迹压到另一元素/可见边线——否，盒为无边框米色盒，伸出部分落在页右空白边（页宽 1950，墨迹最远 1886.5），其右无任何元素；(c) 与旧版不同——否，逐像素坐标相同，**重建引入回归 0 处**。结论：**观察项，非缺陷**。

## 4. 印/网文字层位置差分（补充：gates 只做多重集）

```sh
# venv python + PyMuPDF：逐词 (page, x0, y0, x1, y1, text) 计数器差分
# print words 4704，web words 4704；(page, text) 多重集差 0
# 带坐标差分：仅 1 词 — P1 刊头 "Lucerna"：
#   print (499.1, 62.8, 956.9, 209.8) / web (501.7, 81.3, 960.2, 233.2)
# 对照核心：core print/web 同一词、同一坐标、同一位移，故为 webpdf 管线固有属性，非 it 版缺陷。其余 4703 词坐标逐字相同。
```
另渲染网版 P1（`render/web-p1-1.png`）目视：与印版 P1 逐行一致。

## 5. 网 PDF abutting 全掃（舊輪 D2 復驗；builder gates 不含此門）

```sh
# d2scan-it.py：scratch-webpdf-patch1/d2scan-full.py 改 ED 路徑為本版（原檔未動）
tools/venv/bin/python d2scan-it.py   # 日志 d2scan-it.log
# abutting pairs scanned: 1268
# worst web gap: 0.05 pt (7, 16.12, '11', '月', 0.05)
# gaps >0.5pt: 0
```
网 PDF 建於 2026-11-11 11:20:14 UTC；`tools/webpdf.py`（09:10 UTC）已含 `:weight=100/200` 補丁。舊輪 D2（9 處缺口）已修好。

## 6. 150 题三源交叉（keycheck-150.json）

- 来源一：text.md 正文事实；来源二：text.md 答案区；来源三：svg/p8-test.svg 提取键（`p8-extract.json` 的 `keys`）。
- 结果：**150/150 PASS**，text.md 键与 SVG 键逐题值相同（0 差异）；算术题独立重算：Q23 1200+800=2000 ✓、Q24 2000−1200=800 ✓、Q41 11/6–11/22 含首尾 17 天 ✓、Q42 17:00–18:30 = 1.5h ✓、Q59 5×10=50 ✓、Q60 100−70=30 ✓、Q77 14+31+3=48 ✓、Q78 11/17–11/22 含首尾 6 天 ✓、Q84/Q99/Q128 14:00–19:00 = 5h ✓、Q85 1.5h ✓、Q100 4 件 ✓；匹配组 25–28 / 43–46 / 61–64 / 79–82 按集合核对无误。
- Q150 开放写作：范文 142 字（120–180 字范围内，实测不含空白 142 字），内容与 P1/P6 事实一致。
- 细节：Q128 选项 B 在印版渲染中折为「5小/時」两行——为栏内换行，非错误。

## 7. 其余专项扫描

- **彎引号/直引号**：SVG 文本内容直双引号 `"` 0 处；直单引号 `'` 61 处，全部为意大利语省音（l'ultima、dell'inverno、mezz'ora 等）；弯单引号 ’ 0 处、弯双引号 0 处。对照：核心 en 直 ' 28 处、fr 86 处、es 0 处，弯引号全周 0 处——直撇为全周统一写法，非 it 版缺陷。
- **简体字**：checks.py SIMP_ONLY_HITS []。另行扫查：`互` 在 SVG/text.md 各 4 处，均在「互動」（球員互動）中——「互」为繁简同形字（互動为标准繁体词），非简体。
- **E 节 type 标签繁体本地化**：A 判斷對錯、B 本週大測驗、C 完成句子、D 讀一讀，答一答、E 情景說話、F 寫一寫——全部繁体，意大利语副标齐全。
- **「next Sunday」冻结核对**：`scratch-refanout-zh-tw/tables.py:245/:267/:322` 仍为 next/Next Sunday；核心 `content12.py:37/:113`、`content34.py:127` 亦然；it 版 SVG/text.md 内「next Sunday」0 处、「本週日」11 处、「下週日」0 处。按任务要求**不列为缺陷**。
- **舊輪 D1/D3 復驗**：D1「下週日」text.md 0 處（舊輪 11 處已改「本週日」）；D3 `è tutti/è ogni/è in tutto` 全文 0 處，5 處已改 `si tiene` / `si ripete` / `prevede`（grep 驗證）。
- **目视**：印 PDF 8 页逐页渲染（`render/p-1.png` … `p-8.png`，110 dpi，自行渲染）全部看过；网版 P1 亦看过。无溢出、无重叠、无页脚碰撞；P6 时间轴 18:30/19:00 两标签目视相邻不重叠（与 0.6 px 实测一致）；P4 条形 10/50/100 比例目视正确；图片与署名位置确认。

## 8. 外部事实独立核查（2026-11-11 检索）

| 事实 | 核查结果 | 来源 |
|---|---|---|
| 味全龍第 6 冠、封王遊行 11/22 14:00 天母→大巨蛋松菸大道、感謝祭 11/21–22、U-Sport 267 間 5→10 幣、满 100 换悠遊卡储值金 | ✓ 全部属实 | 卡優新聞網 2026-11-06、聚傳媒 2026-11-07、夠棒網 2026-10-30、緯來 2026-10-30 |
| 第 63 屆金馬獎 11/22 台北流行音樂中心、17:00 星光大道、18:30 典禮、柯煒林首主持、587 部報名、入圍 10/1 公布、《狂忘警探》11 項、主題「再見江湖」、影展 11/6–11/22 | ✓ 全部属实 | applealmond、YOLO LAB、風采 2026-11-03、K-MEDIA 2026-11-02 |
| 小雪 2026-11-22（週日）、二十四節氣第 20 個、立冬之後 | ✓ 属实（15:23 交节） | 香港天文台 2026 年表、owaves、中央氣象署日曆资料 |
| 新北耶誕城 11/13–12/27 共 45 天、卡娜赫拉、主燈秀 17:30–23:00 每半小時 5 分鐘、7 處燈區、德國市集 12/4–6 | ✓ 全部属实 | 卡優新聞網、HouseFeel、WOMENT、JAMIE慢森活 |
| 香港迪士尼聖誕 11/17–2027-1/3 共 48 天、魔雪奇緣世界首個冬日市集、11/19 新日間城堡演出、亮燈+無人機、音樂會 11/21–22、12/5–6 共 4 場、雙重暢玩任選兩天 | ✓ 全部属实 | yourdisney、konggokhk、superpama、POPBEE |
| 西九爵士音樂節第 8 屆、11/13–15、17–22、24（10 天）、Diana Krall 11/13 開幕、Cory Wong×何卓彥 11/15、Stacey Kent 11/17 自由空間、Kenny G 11/24 竹翠公園收尾 | ✓ 属实 | jazznode、hongkonglei、thehkhub、U Lifestyle（注：史黛西·肯特「連開兩場」为核心原文细节，本轮检索只见到 11/17 一场之记载，未独立证实亦未证伪；属核心继承内容，非 it 版引入） |
| 六福村墓碑鎮 10 週年 9/12–11/22、夜間遊行《鹿魔覺醒》19:00（週五–週日）、5 米鹿魔、日間《異界狂想曲》每日 14:00 週二休演 | ✓ 全部属实 | 產經新聞網 2026-10-20、gofunit、痞客邦 |
| 高雄鋼雕藝術節 10/23–11/22、SUPER STAGE、SUPER SAFE 保險箱、駁二 B3/哈瑪星/鹽埕、平日 10–18 週五週末至 20:00、林洪玉秀 85 歲《萬年吉祥花》、鹽埕學裁縫縫婚紗 | ✓ 全部属实 | 高雄市政府新聞局、中央社 2026-10-29、owlting |
| 寶可夢 30 週年又一城 11/11 起、巨型皮卡丘氣球、10 米精靈球燈光裝飾、官方快閃店 | ✓ 全部属实 | konggokhk、U Lifestyle、likemagazine |

其余事实（梅里愛《月球之旅》1902、台灣消保法 7 天鑑賞期、主燈秀 17:30–23:00 共 12 場之算术）为核心继承内容，已在核心 re-proof #3 结论 (a) 中认证；本轮对 12 場算术重算无误（17:30–23:00 每半小時含首尾 = 12 場）。

## 9. 红线遵守

只读生产文件：未改任何成品、未 commit、未 push。活动范围仅 `production/2026-w47/`（读）与 `hidden_files/w47/`（写本 scratch）。交付物均在本 scratch 内。
