# GATE-LOG — 2026-W47 de-ko · proof2

工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-de-ko2/`
（子目录 `render/`、`gates/`、`text/`、`tmp/`；全程 `TMPDIR=<scratch>/tmp`）

## 探针与 SHA

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → rc=0（`9daeafb9…`）；scratch 目录 probe 文件写入通过。
- `sha256sum` 三件（开工前）：
  - 印刷 PDF 15,907,006 B `1ee2229f5e0d9803d9b32e9c048027a1bced2783bacac9ed72a83499cd866bcc` ✓
  - 网页 PDF 1,909,587 B `9a0699420966ff7354c3e11d078a2e46ecde8ff35badab03f2be7f8722fe6776` ✓
  - text.md 51,498 B `fd2dbd047e23bcd0fffc5245ee8d529b9e848adc11133ff46f490b304b8a66a2` ✓（与 fix 前相同）

## 渲染

- `pdftoppm -png -r 200` 印刷 PDF → `render/print-p-{1..8}.png`（8/8）；网页 PDF → `render/web-p-{1..8}.png`（8/8）；`pdftoppm -r 100` 印刷 PDF → `render/print100-p-{1..8}.png`（8/8）。后台会话完成。
- 裁切（PyMuPDF，`tools/venv/bin/python`）：`crop-p7-toolbox-300dpi.png`（300 dpi，工具盒区）、`crop-p8-hbox-200dpi.png`、`crop-p8-key67-200dpi.png`、`crop-p8-key67-300dpi.png`、`crop-p8-key67-300dpi-band.png`（300 dpi，y 1831.53–1845.92 干净带）、`crop-p8-keysbottom-200dpi.png`、`crop-p3-q34-200dpi.png`（初版取位偏下，已废弃）、`crop-p3-q34b-200dpi.png`（正确取位）。

## 门禁（日志均在 gates/）

| 命令 | rc | 关键输出 |
|---|---|---|
| `tools/occlusion_audit.py`（真实跑） | 0 | 0 flags；`occlusion.json`/`occlusion.log` |
| `tools/p8.py extract` | 0 | 150/150；`p8extract.*` |
| `tools/p8.py compare` vs `core-de` | 0 | CLEAN，missing=[]，keydiff=[137,138,139,150]；`p8compare.*` |
| `tools/freeze.py diff` | 0 | CJK 新增 3,096；`freeze.*` |
| `freeze_direct.py`（自 `scratch-fanout-de/`） | 0 | source PASS（removed 0 / added 0），rendered 8/8；SHA 与 KIT 一致；`freeze-direct.*` |
| `boxtitle.py`（自 `scratch-fanout-de/`） | 0 | 7/7 fit；最紧 `WEIHNACHTSWÖRTER　크리스마스` 395.8/400.5；`boxtitle.log` |
| `keycheck.py`（自 `scratch-fanout-de/`） | 1 | 148/150；仅 Q139、Q150（提取器 artifact，KIT 已记录）；`keycheck-150.json`/`keycheck.log` |
| P8 最小字号（PyMuPDF，印+网） | — | 9.94pt（≥9.75pt）；`p8min-textlayer.log` |
| `d2scan.py` abutting | — | 72 对，0 个网页间隙 >0.5pt |
| `creambox.py` 全版（8 SVG，canonical） | — | P7 工具盒底 774.0 / 最后基线 754.8 / +19.2 / desc-clear +13.1；LESERBRIEFE 盒内 +10.4；NOCH EIN WORT 最后基线 1465.6 / +42.9（底 1508.5）；P7-TOOLBOX 汇总：6 盒，最小盒内 +10.4，最小 desc-clear +4.5；P8 MUSTER 盒内 +47.1；其余负值均为已知假阳性（见 PROOF-NOTE §3）；`creambox-full.log` |
| `pdftotext` 印/网比对 | — | 逐页词多重集 8/8 相同；全文默认文本字节相同（各 52,318 B）；`-raw` 字节相同（各 51,151 B） |
| 引号计数（text.md + 8 SVG） | — | U+201C 33 / U+201D 0 / U+201E 33 / U+2019 0；« » 各 6 成对 |
| Q34（text.md、P3 SVG、印/网 text layer） | — | 新单数 `Am Montag öffnet in Köln der erste ___.` 各 1 次，旧复数 0 次 |
| MUSTER 词数 | — | 84 tokens（83 词 + 独立破折号），与“84단어”标签一致 |

## 引号像素测量（de-en D1/D2 方法）

脚本：`gates/quote_pixel.py`（自 `scratch-proof-de-zh-tw2/quote_pixel.py` 复制）；点位：`gates/spots-p8.json`、`gates/spots-p7.json`（字符框取自印刷 PDF PyMuPDF rawdict）；日志 `gates/quote-pixel-p8.log`、`gates/quote-pixel-p7.log`。

| 点 | 结果 |
|---|---|
| H » DE Newsreader 16.12pt | 1.80pt = 0.11em PASS |
| Q67 » NotoSansCJKsc 9.94pt | 200 dpi 归因 artifact（'s'+» 墨列连续）；300 dpi 干净带复测空隙 **0.0pt = 0.00em** PASS |
| H-box KR 』 NotoSansCJKsc 15pt | 1.44pt = 0.10em PASS |
| P8 对话 “ 对照 | 1.44pt = 0.10em PASS |
| P7 NOCH EIN WORT » 对照 | 1.44pt = 0.09em PASS |

阈值 0.2em；五点全部通过，de-en D1/D2 类缺陷未复现。
（注：第一次跑 `quote_pixel.py` 时 `$G` 未定义写日志失败，已用 `$S` 路径重跑，日志完整。）

## 事实网查（browser.search，2026-11-11）

- 拜仁 2:0 马竞（11-03，Karl 54'、Laimer 74'）——fcbayern.com / bundesliga.com
- 欧冠第 4 轮：多特 2:1 贝蒂斯、莱比锡 2:3 曼城（11-04）、加拉塔萨雷 2:0 斯图加特（11-03）——UEFA.com；下轮：11-24 阿森纳–多特、莱比锡–朗斯；11-25 国米–斯图加特、里尔–拜仁
- 欧战 11-05：勒沃库森 0:1 马赛、霍芬海姆 1:1 水晶宫、弗赖堡 1:0 特拉布宗；欧联第 5 轮 11-26 萨格勒布迪纳摩–勒沃库森
- 德甲第 9 轮 9 场比分全对，总进球 30——fussballdaten.de（拜仁第 1、科隆第 15）
- 塞尔维亚–德国 11-13：欧足联观众禁令、儿童+50 名德国球迷、20:45、Rajko Mitić、RTL；欧国联 A2 组：荷兰 8、希腊 8、德国 5；德国–荷兰 11-16 柏林 20:45 ARD——kicker.de
- 德甲第 10 轮赛程（11-20 20:30 拜仁–科隆；周六 5 场 15:30 + 沙尔克–斯图加特 18:30；周日奥格斯堡–美因茨 15:30、不来梅–汉堡 17:30）
- Buß- und Bettag：11-18 周三、仅萨克森法定假日、1995 年废除/萨克森 +0.5pp、巴伐利亚停课、安静日——feiertagskalender-deutschland.de；舞会禁令 3:00–24:00——SächsSFG §6（revosax.sachsen.de 法律原文逐字一致）
- 科隆市场：大教堂市场 11-16–12-23、11-22 关闭、官方开幕 11-17 19:00；天使市场 11-16–12-23、11-22 关闭；港口市场 11-13–01-03；亚琛市场 11-20–12-23（第 53 届）
- 1903 年降临节日历 “Im Lande des Christkinds”（Gerhard Lang、Richard Ernst Kepler，24 图粘贴式）
- Wilhelm Ritter（1860–1948）、“Weihnachtsmarkt auf der vorderen Insel Schütt”（1930）——de.wikipedia
- 电费税 2.05 Cent/kWh；Merz 降税主张、Klingbeil 谨慎；2027 预算表决计划 11-27 周五——bundestag.de（11-12 为委员会清理会）
- 追思主日 11-22、第一降临节 11-29（日历计算）

## ABSTRACT（SOP §9）

- `ABSTRACT.txt`：388 B、1 行、韩语、0 个 ASCII 双引号；内容与 KIT §23 引文逐字一致。
- 本版无 `.md` 源文件（content*.py 构建）；edition 源内未见 `abstract =` 变量。
- **已解决**：`tools/insert.py` 165–180 行——读取 ABSTRACT.txt，校验单行/无 ASCII 双引号/VOL.n 与台账一致（本版：单行 ✓、无双引号 ✓、VOL.4 与 W47 台账一致 ✓），入仓时生成 frontmatter `abstract` 字段与正文摘要节（标题 `tables.json` languages.ko.abstract_heading =「요약」）。SOP §9“出现两次”为入仓时生成，proof2 阶段可核的唯一件即 ABSTRACT.txt 本身（已验证合格）；兄弟版 de-en/de-zh-tw 的 text.md 中 “abstract” 出现亦为 0 次，全家一致。
- 生产树全文 grep（会话 proc_7b1d38120f72）已由上述 insert.py 机制说明取代——ABSTRACT.txt 即 SOP 指定的交付件，不再追查其句子的其他来源。
