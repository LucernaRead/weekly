# GATE-LOG — W47 zh-cn-it fix1（修复后门禁，生产文件终验）

修复员：fix1。解释器：`tools/venv/bin/python`（Pillow 13.0.0）。
全部输出存于本目录。生产终验在同步后对生产文件重跑（见 §9）。

## 0. 身份（生产盘上实测）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| 印刷 PDF `Lucerna-VOL4-IT.pdf`（新） | 41,730,133 | `440490c4a389e22edc2c93f5b99fdb5bec857dafceeb1256e0f3af007598a69d` |
| 网页 PDF `Lucerna-VOL4-IT-web.pdf`（未变） | 2,641,804 | `75dec91ac806b884bdd4b7cdbdccc39e2c445ff7f668d24ff4365f21f233a512` |
| 文本 `2026-w47-zh-cn-it.text.md`（新） | 50,916 | `afc9b2c02a319ab1d20227d3c0826942fc969aa577f61caea56b3845d664544f` |

开工三 SHA 见 FIX-LOG（印 d1ae6f87…/41,730,134 B；网 75dec91a…；
文 f954151f…/50,958 B）。

## 1. run.py scratch 重建（OUT 改指副本后）

`run.py` RC=0，TOTAL 150（A2 56 / B1 69 / B2 25；分版 10/18/18/18/18/18/12/38；
题型 完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1）；
`FLOW OVERFLOW` / `HEAD TOO WIDE` 0 次；P8 keys end 2506.4；
P7 teaser ends 2562.26；writing model chars 138。日志 `run-rebuild2.log`
（`run-rebuild.log` 为事故那次，产物 SHA 与本次相同，见 FIX-LOG）。
SVG 变化页：p1/p2/p5；其余 5 页与生产原版字节一致。
`p.para` 截止段（:86）与 `Chiusura` 短行（:88）均未互相串位。

## 2. render.py scratch 渲染（BASE 改指副本后）

RC=0；8 张卡片重渲（仅 p1/p2/p5 与生产原版不同）；印 PDF
41,730,133 B，8 页。日志 `render.log`。网 PDF 未生成、未覆盖。

## 3. PIL 真墨（改前自测 → 改后重测，生产 SVG 终验）

| 项 | 改前（墨右 / 盒右 / 余量） | 改后（墨右 / 盒右 / 余量） | 门限 ≥+5px |
|---|---|---|---|
| D-01 | 1007.5 / 961.0 / −46.5 | 893.5 / 961.0 / **+67.5** | PASS |
| D-02 | 994.5 / 961.0 / −33.5 | 892.5 / 961.0 / **+68.5** | PASS |
| D-03 | 1880.5 / 1862.0 / −18.5 | 1815.5 / 1862.0 / **+46.5** | PASS |
| D-04 | 1424.0 / 1411.5 / −12.5 | 1294.0 / 1411.5 / **+117.5** | PASS |
| D-05 | 2 行收尾孤儿 `》`（556.5, 1366.3） | 单行，孤儿 `》` 元素 0 | PASS |

脚本 `measure_before.py` / `measure_after.py` / `measure_final.py`
（终验用生产 SVG）。D-05 的 `measure-after.json` 里 `PASS: False` 是脚本
artifact：它对单元素 `endswith('》')` 断言，而条目行是双字体 run
（拉丁 run + `《试探》` run）；直接证据为孤儿元素 0 + 接合行
`21 nov., sabato — esce il film 《试探》` 单行 + 渲染像素孤儿行无墨。

## 4. 交付印 PDF 渲染像素（110 dpi，PyMuPDF，裁决方法；生产 PDF 终验）

对照（旧生产 PDF）先跑以校验方法：D-01 −46.7、D-02 −33.6、D-03 −19.9、
D-04 −12.4（PIL −12.5）、D-05 孤儿行有墨——与 PIL 一致（±1.4 px 内）。
新生产 PDF：

| 项 | 渲染像素墨右（折 SVG 坐标） | 盒右 | 余量 | 结论 |
|---|---|---|---|---|
| D-01 | 893.4 | 961.0 | **+67.6** | PASS |
| D-02 | 892.6 | 961.0 | **+68.4** | PASS |
| D-03 | 1815.6 | 1862.0 | **+46.4** | PASS |
| D-04 | 1293.0 | 1411.5 | **+118.5** | PASS |
| D-05 | 孤儿行无墨；条目行有墨 | — | — | PASS |

注：D-04 首版带把山谷照片左缘（x=1439.5）误算为标题墨（−28.1），
已把测量带 x 上限收至 1435（照片左缘之外）重跑；对照随之复现 PIL 值。
裁图（生产 PDF）：`crops-final/` 5 张（P1 数字框标题、P1 数字框、P1 截止线、
P2 日历标题、P5 高频词标题），已目视：标题全在奶油盒内，条目单行无孤儿。
脚本 `render_check.py`，结果 `render-check-final.json`。

## 5. 奶油盒横扫 + 行首闭合标点扫描（生产 SVG 终验）

- 全刊 521 个奶油盒内文本元（原 522，D-05 孤儿元素消失减 1）：
  **溢出 0**；贴边 1 处：P4 `看比赛的中文　Parole delle partite` 余 +6.5 px
  （proof1 O-2 已通过项，未变）。
- 行首闭合标点扫描：**孤儿 0**（全刊）。
- P7 `Parole della settimana:` 词汇表头（x=88, y=271.5）是另一元素，未动；
  旧串残留仅两处应留项：text.md line 123（:86 段落 `non ancora giocata`）
  与 line 1315（P7 表头）。

## 6. freeze / p8 / occlusion（scratch 重建版）

- `freeze.py diff --strict-cjk` core vs 重建版：RC=0，
  **TOTAL added CJK characters: 0**（逐页与 proof1 相同）。日志 `freeze-diff.log`。
- `p8.py extract`：noted set **150 of 150**。`p8.py compare` core vs 重建版：
  **CLEAN，missing=[] extra_count=0 uncertain=[] keydiff=[]**。
- `occlusion_audit.py`：selftest OK（6 类 planted 全触发）；
  本版 **0 flags**，核心 0 flags，NEW vs core 0。⚠️ 此 0 旗**不是**
  D-01～D-04 的修好证据：BOXTITLE 只看带 stroke 或 fill `#2c2822` 的 rect，
  本版奶油盒为无边框 `#f0eee5`（proof1 工具缺口）；修好证据只认 §3/§4 双法。

## 7. gates-zhcn.py（门禁专用副本 gates-edition，10/11 PASS）

RC=1，OVERALL: FAILURES PRESENT——唯一 FAIL 为 `print_web_text`，系**预期内**：
网 PDF 按要求未重建，仍带 5 处旧串，故 P1/P2/P5 有位置/词差异，
P3/P4/P6/P7/P8 posdiff/msdiff 均为 0。
`P1:379/383:pos212:ms8 P2:376/377:pos356:ms1 P3:280/280:pos0:ms0
P4:353/353:pos0:ms0 P5:278/279:pos205:ms1 P6:355/355:pos0:ms0
P7:527/527:pos0:ms0 P8:1837/1837:pos0:ms0`；print pdftotext 44,862 B
vs web 44,907 B（−45 B，与缩短的措辞一致）。全家重建网 PDF 后此门应恢复全绿。
其余 10 门全 PASS：occlusion 0 旗；img_overlap 0；p8_extract 150/150；
p8_compare CLEAN keydiffs 0；freeze_sha256 8/8；pdftotext_nonempty；
p8_fontsize **9.98pt**（≥9.75；median 9.98，spans 369）；
p8_chips = 核心（A2 11 / B1 24 / B2 3）；u2019 0；s11_svg clean
（paper #fbfaf6 ×8，无金色/近黑，stroked_rects 0，VOL.5=1=核心）。
日志 `gates-it.log`，JSON `gates-it.json`。

## 8. text.md 导出 + D4/D5 + 150 题

- `export_ed.py`（CORE 改指 scratch 副本）RC=0，recorded 1050 串，registry 150；
  新 text.md 50,916 B；与生产旧 text.md diff **恰好 5 行**（5 项修复），别无他异。
- D4/D5 重建版 SVG 无缝接合计数：`全球总决赛的BO5` P4 ×2；Q56 键
  `per la prima volta in un BO5 dei Worlds` ×1；`GEN在S16一场没输` P1+P4 ×2；
  `只丢了一小局` ×2；`对LYON 2比1` ×1；保留 `淘汰赛一局没输` ×1；
  旧措辞 `第一次在BO5里打赢T1` / `for the first time in a Worlds BO5` /
  `GEN今年一局没输` 全刊 0。
- 150 题键：p8 compare CLEAN（§6）+ run.py TOTAL 150 同 breakdown 覆盖；
  键与题干未动（本次只改 5 处意大利语尾/条目，无键、无题干、无图表）。

## 9. 生产零外溢核对 + 生产文件终验

- 开工快照 `snapshot-start.txt` → 收工快照 `snapshot-end.txt`：
  恰好 **11 个文件**变化（content12.py、content56.py、svg p1/p2/p5、
  cards p1/p2/p5、印 PDF、text.md、WEEKLY-KIT.md），余 28 个文件字节全同；
  `__pycache__/` 2 个 .pyc 未变（全程 `PYTHONDONTWRITEBYTECODE=1`）。
- 同步后对生产文件重跑：PIL §3 全 PASS、渲染像素 §4 全 PASS、
  奶油横扫 0 溢出、孤儿扫描 0（`measure-final.log`、
  `render-check-final.json`、`crops-final/`）。
- KIT 已同步更新（新 SHA + fix1 章节，旧 SHA 保留；见 FIX-LOG）。
- 未 commit、未 push。网 PDF 待全家统一重建后，`print_web_text` 门需重跑确认。
