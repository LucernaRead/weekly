# GATE-LOG — 2026-W47 nl-ja delta (core fix3 + fix4 + fix5)

版：`2026-w47-nl-ja`，build 6。全部自跑；证据文件均在
`hidden_files/w47/scratch-delta-nl-ja/` 下（相对路径以该目录计）。
规范路径：`production/2026-w47/2026-w47-nl-ja/`。 staging 对照：
`production/2026-w47/fanout-nl/2026-w47-nl-ja/`（未动，build-5）。

## 1. 构建

| 门 | 结果 | 证据 |
|---|---|---|
| run.py | rc=0，TOTAL 150，by page 10/18/18/18/18/18/12/38，A2 46 / B1 73 / B2 31，0 FLOW OVERFLOW / HEAD TOO WIDE；P4 col3 ends 1229.6，P6 chart ends 691，P7 col3 ends 1927.5 | `rebuild/run.log` |
| render.py | rc=0，print PDF 26,049,309 B | `rebuild/render.log` |
| text.md 重导 | rc=0，47,801 B，diff 恰为 :415 一行（+5 B）；142+2+8=150；8 金句；6 gloss | `rebuild/export.log`，`pre/text-pre.md` 对照 |
| registry 重导 | rc=0，150 条 | `rebuild/dump_reg.log`，`registry-new.json` |
| webpdf.py | rc=0，2,155,389 B，text layer 47,924 B | `rebuild/webpdf.log` |

## 2. SVG 逐页 SHA 比对（修前 → 修后）

| 页 | 修前 | 修后 | 变化 |
|---|---|---|---|
| p1-voorpagina | `b1797d8c…` | `b1797d8c…` | 一致 |
| p2-leven | `35914f59…` | `35914f59…` | 一致 |
| p3-cultuur | `2ddeb68f…` | `2ddeb68f…` | 一致（D6 结构同步） |
| p4-sport | `5ed7ac08…` | `0dd0671e…` | 变（D11） |
| p5-jongeren | `314d1983…` | `314d1983…` | 一致 |
| p6-verdieping | `80417217…` | `80417217…` | 一致（D8 结构同步） |
| p7-taal | `4608bb65…` | `4608bb65…` | 一致（D7/D10 结构同步） |
| p8-toets | `1b16e2be…` | `8aa13d85…` | 变（D9） |

完整表：`pre/svg-sha-pre.txt` vs `rebuild/svg-sha-post.txt`。

## 3. 门禁套件（gates_delta.py，9 项，ALL PASS）

`gates/gates-delta.log` + `gates-ja.json`：

| 门 | 结果 |
|---|---|
| occlusion | rc=0，0 flags |
| p8_extract | noted 150/150 |
| p8_compare | rc=0，CLEAN（JSON 本体 keydiff [137, 138]；见 §4 注） |
| freeze_sha256（版内自比对） | run rc=0，8/8 |
| print_web_text | 8/8 页，posdiff 0，msdiff 0；tokens 745/706/665/661/683/647/734/1600 |
| pdftotext_nonempty | print 47,924 B = web 47,924 B；web 2,155,389 B < 7 MB |
| p8_fontsize | min 10.12pt，median 10.12pt，561 spans（≥ 10pt） |
| p8_chips | core {A2:8, B1:24, B2:3} = edition |
| s11_svg | off-palette {}，gold/old False，stroked_rects 0，VOL.5=5=core，paper fills 8 |

## 4. p8 compare（核心 vs 本版，JSON 本体为准）

- 修后：`status: CLEAN, total: 150, missing: [], extra: [], uncertain: [], keydiff: [137, 138]`
  （`gates/p8-compare.json` + `gates/p8-compare.log`）
- 修前（staging P8）：`keydiff: [137, 138, 140]`（`gates/p8-compare-pre.json`）
  ——D9 把 140 移出。137/138 为翻译题，键按设计即读者语（日文 vs 核心中文），非缺陷。
- 注：gates 套件日志里的 `keydiffs=0` 是其对 stdout 文本行的计数，与 JSON
  本体口径不同（nl-de 试点已记录同一情况），以 JSON 为准。

## 5. 三源逐题比对（registry / text.md / P8）

`p8-compare-3way.json` + `gates/p8compare-3way.log`：**149/149 MATCH**，
DIFF=[]，MISSING=[]；Q150 为开放写作例外（P8 键 `✓`，text.md 81 词
Tekstmodel，registry 开放题占位）。Q140 三源同为
`Ik maak een surprise met een kort gedicht.`（MATCH）。配对键 25–28 =
d/c/a/b，141–144 = b/c/d/a。
（脚本 `p8compare_delta.py`：nl-de 版改写——marker 由德语 `— Antwort:` /
`(Antwort …)` 改为日语 `— 答え：` / `(答え …)`；`p8compare_fix4.py` 为
核心侧脚本，本 delta 未用。）

## 6. Freeze（核心对照）

`tools/freeze.py baseline --build production/2026-w47/core-nl
--core-svg production/2026-w47/core-nl/svg --out scratch/freeze-core`：
rc=0，**8/8 SVGs byte-identical**，core shipped SVG 跑前后哈希不变。
（`gates/freeze-core.log`）

## 7. 孤儿标点横扫（双类，双 advance，brute-force 交叉）

| | 修前（staging） | 修后 |
|---|---|---|
| 行数 | 1444 | 1444 |
| (a) 独行标点 PIL / svglib | 0 / 0 | 0 / 0 |
| (b) 行首标点 PIL / svglib | 0 / 0 | 0 / 0 |
| brute-force leftmost | 0（13 片段全非行首） | 0（13 片段全非行首） |

证据：`gates/orphan-sweep-pre.log`、`gates/orphan-sweep.log`、
`orphan-sweep-delta.py`（nl-de 版复用，路径重定向）。
**0 新增。**附注：复用脚本的 targeted 小节仍用德语 needle，在本版无命中
（预期）；日语 needle 逐行实测见 `gates/targeted-lines.log`。

## 8. Creambox

修后 TOTAL 6 flags（`gates/creambox.log`）与修前 6 flags
（`gates/creambox-pre.log`）**逐项一字不差**：P2 CREAM-RIGHT + CREAM-BOTTOM、
P5 CREAM-BOTTOM、P6 PAGE-EDGE + CREAM-RIGHT + CREAM-BOTTOM——均为 build-2
已裁定的已知假阳性。P4 D11 盒 0 flags。**真溢出 0。**

## 9. Spill 横扫

`gates/spill-sweep.log`：**0 spills**。P4 HET PROGRAMMA 盒（底 1229.6）
无任何 below 命中；其余 BELOW 命中 6 处均为独立版块（下一节标题、
quiz 提示语、gloss 解説）。

## 10. D11 双量测（PIL 真墨 + 交付 PDF 渲染像素）

`verify-d11-ja.py` → `gates/d11-verify.log`：

| 量测 | 值 |
|---|---|
| 盒底（SVG 实测） | 1229.6（y=591.6，h=638.0） |
| 末行基线 `18:45 uur.` | 1209.49，基线余量 **+20.11px** |
| PIL 真墨底（4× Newsreader） | y=1208.74，余量 **+20.86px** |
| Card 1× 最低文字墨行 | 1209，余量 +20.6px |
| Card 1× 盒底下 7px 条带 | 0 非纸像素（y=1230–1236；初报 422 像素为盒底行 y=1228/1229 的奶油填色本身，盒宽 422.5px，已订正） |
| 印 PDF 150dpi 盒底下 7px 条带 | 0 非纸像素 |
| 习题线 y=1608 间隔 | 378.40px |

## 11. 目检裁图（印 PDF，200dpi）

`crop-p3-d6.png`（桥接 2 行，`。` 在行末）、`crop-p7-d7.png`（3 行，
末行 `する。`）、`crop-p4-programma.png`（`18:45 uur.` 在盒内，下有明显
留白）、`crop-p8-q140.png`（`140. Ik maak een surprise met een kort
gedicht. — surprise は決まった言い方`）——四处均目检通过。

## 12. 三 SHA（交付，build 6）

- 印 `f78ffe324aaf24d39fa71cc815b96d6c163cf2747c27a10d7633e94cb41943b0` / 26,049,309 B
- 网 `b4d4501b8665d0adee4b8484a66a8bd17031ee4953f397e7c0142b7b0ee4762b` / 2,155,389 B
- 文 `060bfdea243483edb1a30691ff26291eac1a90bc69f2ea4c38fe97eac05bb93a` / 47,801 B

旧值（build-5）：印 `40e58eb2…446e49` / 26,049,308 B；网 `3c60dddb…4ae49` /
2,155,388 B；文 `e890ba13…dcf6` / 47,796 B。staging 三 SHA 复核未变。
