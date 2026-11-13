# GATE-LOG — W47 de 核心版第五轮复校（build15）机械门

校对员：第五轮独立校对（叶子）。全部在 scratch 副本/只读方式自跑；原目录未写文件。
工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-de5/work/`

## 身份（自算 SHA，与 KIT 登记逐字一致）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `Die-Lucerna-VOL4-de.pdf`（印刷） | 22,965,197 | `49beffc4223ede29674a3c70c341ec9fc04d2103eb632d1194e8ffcb31250607` |
| `Die-Lucerna-VOL4-de-web.pdf`（网页） | 2,044,855 | `9b63b413424caa99ed255c7b84dc8368df3ad39f1de956768bbe2353037c01a8` |
| `2026-w47-de-zh-cn.text.md` | 49,798 | `0952bc517e96351e505d4790237aa00d4ca36032763ec256d005d6eeec3c8b48` |

终验 SHA 与开工时一致，未改动。PDF：8 页，1462.5×2025pt。

## D-01 回归

- 新题干 `"Am Montag öffnet in Köln der erste ___."`：源码 / `.text.md` L389 / P3 SVG / print 文字层 / web 文字层各 1×；P8 键 `34. Weihnachtsmarkt（圣诞市场）` 不动；REG n=34（page 3、A2、完成句子、key `Weihnachtsmarkt`）。（`work/d01.log`、`work/d01b.log`、`work/reg-de5.json`）
- 旧题干 `"Am Montag öffnen in Köln die ersten ___."`：源码、`.text.md`、8 SVG、print/web 文字层均为 0。
- build14→build15 全文 diff：仅 `.text.md` L389 一行。旧文本 SHA `1c219c84864ababa52c7a63985614f7cd54bb780913ccae43fff6890b393ce86` 与第四轮实测 build14 值一致；diff 仅一行不同（`work/d01.log`）。
- freeze 逐页哈希与 build14 对照：仅 P3 变（`7dcdfe11…`→`1c2d4850…`），其余 7 页 byte-identical。

## 机械门（全部自跑，tools/venv 解释器）

| 门 | 命令 | 结果 |
|---|---|---|
| occlusion | `tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/core-de/svg --json work/occlusion15-de5.json` | **0 flags**；自检通过（6 类植入全触发、干净对照静默）；rc 0 |
| p8 extract | `tools/venv/bin/python tools/p8.py extract --p8 …/svg/p8-uebungen.svg --total 150` | **150/150**；rc 0 |
| p8 compare | `tools/p8.py compare --core-p8 … --edition-p8 … --total 150`（核心对自身） | `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[]`；rc 0 |
| freeze | `tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/core-de --core-svg …/svg --out work/freeze-out` | **8/8 SVGs byte-identical**；core integrity：交付 SVG 运行前后未变；rc 0（build14 日志曾为空的问题已由本轮真跑解决） |
| run.py 重跑 | scratch 副本 `work/copy-de5/` 内 `tools/venv/bin/python run.py` | rc 0；TOTAL 150；`FLOW OVERFLOW` 0 次；`HEAD TOO WIDE` 0 次；流终点 P3-main 886/1560、P5-main 966/1080、P6-ex 2523/2560、P1-quiz 2523/2560、P8-keys 2504/2560、P8-battery 1409/1555 |
| verify.py | scratch 副本内 `tools/venv/bin/python verify.py` | rc 0，全绿（TOTAL 150、分版/级别/题型、编号连续、SVG byte-identical、§1.1 style audit True、旧式 hex []、金句 2×、禁词全空、头条 40 字、图柱 748/561/391、MUSTER 84、日期加法全对、P8 下限 True） |
| 登记表复现 | `work/check_de5.py`（副本内同款顺序） | TOTAL 150；by page {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；levels A2 69 / B1 67 / B2 14；types 与 KIT 一致；编号连续；Q34 key `Weihnachtsmarkt` |
| 文字层 | `pdftotext` 默认 / `-layout` / `-raw` | 默认模式各 50,498 B，词多重集相同（7,235 token）；`-layout` 归一化词序 0 处差异；`-raw` 各 49,381 B，**逐字节相同**（cmp 通过）；web < 7MB，带真实文字层 |
| P8 最小字号 | PyMuPDF（tools/venv）逐页最小 span | P8 **10.12pt** ≥ 9.75pt；其余各版 11.62–12.75pt |
| 徽章 | SVG `rx="2.7"` 计数 + 级别序列 vs REG | **141 枚**（P1 10、P2 15、P3 18、P4 15、P5 18、P6 18、P7 12、P8 35）；逐页级别 0 不匹配（配对题共享 chip 已折叠：P2 Q25–28、P4 Q52–55、P8 Q141–144） |
| 题干字号 | `work/check_stems2.py`（AST 124 个 ex() 题干 vs SVG 字号） | 124/124 命中，低于下限 0；P1–P7 22.0 单位 = 16.5pt；P8 20.5 单位 = 15.375pt（三处误匹配已排除：P2 栏目标题行、P3 事实框行） |
| §8.1 严格计数 | `work/check_gloss_strict.py`（`.text.md` 文章段口径） | P1 4/4、P2 5/5、P3 6/6、P4 5/5、P5 6/6、P6 6/6；词表框 P3/P5 各 6/6 |
| 金句 | verify.py 口径（副本重跑）+ 出处逐字核对 | 8 条各恰 2×，`verbatim OK: True` |
| 禁词 | print 默认/-raw/web -raw 三份文本 | Geisterspiel、Karneval、Volkstrauertag、NFL、American Football、Tankrabatt、Hart aber fair、Klassiker、Allerheiligen、VOL.3、VOL.2、Le Lucerna、The Lucerna、11.11、8,35、14,04、ZEW 全 0；VOL.5 7 处均为预告/来信/写作语境 |
| VOL | raw 文本 | VOL.4 8 处（每版页脚 1 处）；VOL.3 0 处 |
| 日期星期 | `date -d` Europe/Berlin | 3 日周二、4 日周三、5 日周四、6 日周五、7 日周六、8 日周日、13 日周五、15 日周日、16 日周一、17 日周二、18 日周三、20 日周五、22 日周日、24 日周二、25 日周三、26 日周四、27 日周五、29 日周日，全部与版面一致 |
| D4 外部事实 | browser.search（2026-11-11，7 家 2026-11-10 报道） | UEFA 禁令 + €50,000 罚款；儿童 <15 岁 + 50 名精选德国球迷可入场；约 5,000 人；55,000 座 Rajko-Mitić；13 日周五 20:45；荷兰 8 / 希腊 8 / 德国 5 / 塞尔维亚 0；主教练 Jürgen Klopp——与版面措辞一致 |

## 目视

- 印刷 PDF 8 版 110dpi 重渲染（`work/pg-1.png`…`pg-8.png`）逐版目视：零溢出、零重叠、零压页脚。
- 网页 PDF P1/P8 重渲染（`work/web-p1-1.png`、`work/web-p8-8.png`）目视：与印刷一致。
- 放大裁图：`work/crop-p3-q34.png`（Q34 新题干单行干净）、`work/crop-p8-q34key.png`（P8 键 34 干净）。

## 日志文件（work/）

`d01.log`、`d01b.log`、`d01c.log`、`misc-de5.log`、`gloss1.log`、`gloss-strict-de5.log`、`occlusion15-de5.log/json`、`p8extract-de5.log/json`、`p8compare-de5.log/json`、`freeze-de5.log`、`run-de5.log`、`verify-de5.log`、`reg-de5.json`、`check_de5.log`、`stems-de5.log`、`print15.txt`、`web15.txt`、`print15r.txt`、`web15r.txt`、`pg-*.png`、`web-p*.png`、`crop-p3-q34.png`、`crop-p8-q34key.png`、`copy-de5/`（复现副本）、`freeze-out/`。
