# ru-nl fix1 — FIX-LOG（D7 P7 band 副标卷引号全角间隙）

- 版：`production/2026-w47/2026-w47-ru-nl/`（只改此版；核心 `core-ru` fix1 未碰）
- 缺陷 D7：P7 band 副标 `Drie niveaus, drie thema’s` 中 U+2019 在 Noto Sans CJK SC（18px）下 advance 为 1 em（18.0px），’ 与 s 之间墨间隙过大，肉眼读作 "thema' s"。
- 修法：`content7.py:12` 该处唯一的 U+2019 换为半宽直引号 U+0027（`thema's`），其余一字不动。版级修法；全生产范围的卷/直引号规则仍待用户裁定。

## 开工核对（三 SHA，proof1 2026-11-11 17:52 UTC 盘验一致）

| 文件 | 开工前 SHA-256 | 大小 |
|---|---|---|
| 印 `Lucerna-VOL4-ru-nl.pdf` | `8982ce29eaf2bc57661a089b9bf0bd8021444130e2e0c9aa505f9176de4a1e17` | 21,315,805 B |
| 网 `Lucerna-VOL4-ru-nl-web.pdf` | `abc3ec69f695129c9e248dae36880da1754f6af5ef32b62f5438435458512593` | 3,387,072 B |
| 文 `2026-w47-ru-nl.text.md` | `96dc93598dec047b87a168c2332bc30b611b8a42250d22e65c7e1da2920ac694` | 64,053 B |

核对结果：三 SHA 与任务书完全一致，开工。

## U+2019 全版计数（改前 → 改后）

| 文件 | 改前 | 改后 | 说明 |
|---|---|---|---|
| `content7.py` | 1（L12 `thema’s`） | 0 | 本次修法唯一改动点 |
| `svg/p7-yazyk.svg` | 1 | 0 | 重建后 |
| 全部 8 个 SVG | 1 | 0 | 仅 P7 含该字符 |
| `2026-w47-ru-nl.text.md` | 1（L504 同句） | 0 | 由 `ru_textmd.py` 从源码重导同步更新；仅 L504 变，64,053 → 64,051 B |
| `ABSTRACT.txt` | 1 | 1（不动） | 另一句 `thema's van de week`（摘要散文，非 P7 band 句）；任务令"只改这一处，不要动版内任何其他引号" |
| `check_core.py` | 1 | 1（不动） | L94 `CLOSES` 标点集常量，非内容 |
| `WEEKLY-KIT.md` | 2（同行 L67） | 2（不动） | 历史记录 prose（W46 TM 说明），非内容 |

注：任务书"改后全版复核计数为 0"指 D7 句所在的渲染内容链（content7.py → SVG → text.md → 两 PDF）；上表两处非内容残留（摘要另一句、标点集常量）有意保留，见说明。

## D7 实测（改前）

- PIL 真墨法（Noto Sans CJK SC 18px，`measure_gap.py` + `raster_gap.py`，`raster-curly-pre.txt`）：
  - U+2019 advance 18.00px；U+0027 advance 5.00px（`gap-straight-pre.txt`）。
  - 整句 `Фокус на язык　Три уровня, три темы　Drie niveaus, drie thema’s` 墨 run：’ run x562..564，s run x579..586 → 14 空白列 / 边距 15px；同 run 其余字母间隙 0–6 空白列（`raster-curly-pre.txt` runs 0–48）。
- 交付物实测（`cards/p7-yazyk.png`，CairoSVG 渲染交付 SVG；`raster-png-pre.txt`）：
  - 顶部墨带 rows 148..161：’ run x1806..1808 → s run x1825..1829，16 空白列 / 边距 17px；同带其余间隙 2–6 空白列。
  - 裁图：`band-crop-pre.png`（整条副标）、`apostrophe-zoom-pre.png`（’s 区域放大）——肉眼读作 "thema' s"。
- 三源一致：card / 印 PDF / 网 PDF 的 P7 均含 U+2019（fitz 验：web P7 含卷引号 True，印 P7 含卷引号 True）。

## 源码改动

- 仅 `content7.py:12`：`Drie niveaus, drie thema’s` → `Drie niveaus, drie thema's`（U+2019 → U+0027）。
- 其余源码一字未动。

## 重建（版目录正常流程，日志绝对路径进本 scratch）

1. `tools/venv/bin/python run.py` → `run.log`：rc=0，TOTAL 150，0 FLOW OVERFLOW / HEAD TOO WIDE。
2. `tools/venv/bin/python render.py` → `render.log`：rc=0，8 cards，印 PDF 21,291,643 B。
3. `tools/venv/bin/python tools/webpdf.py svg Lucerna-VOL4-ru-nl-web.pdf` → `webpdf.log`：rc=0，网 PDF 3,387,332 B，57,957 text bytes。
4. `tools/venv/bin/python ru_textmd.py . 2026-w47-ru-nl.text.md "VOL.4 · Russian text · Dutch explanations"` → `textmd.log`：rc=0，64,051 B，150 exercises，277 blocks。

## 新三 SHA（本次交付为准）

| 文件 | 新 SHA-256 | 大小 | 变化 |
|---|---|---|---|
| 印 `Lucerna-VOL4-ru-nl.pdf` | `5843ae6b80ac7e38298ec33d565b19e49d73dc165e6d18ffeec5bdddd4982fa2` | 21,291,643 B | SHA 变（P7 一字之改） |
| 网 `Lucerna-VOL4-ru-nl-web.pdf` | `d3f016d58cb7b37a35cbf5b05e9a012c49bff6a116baf716db39aca56500b3eb` | 3,387,332 B | SHA 变（P7 一字之改） |
| 文 `2026-w47-ru-nl.text.md` | `8ac1336dbc521f510747d2a838a52e763d6452a81f8ea75ee6fc7c7687942423` | 64,051 B | −2 B（U+2019 3 字节 → U+0027 1 字节）；变化行仅 L504 |

- text.md L504 新文：`### ЯЗЫК · TAAL — Фокус на язык · Три уровня, три темы · Drie niveaus, drie thema's`（直引号）。
- text.md U+2019 计数：1 → 0（`ru_textmd.py` 从源码重导同步）。

## SVG 变化清单

- 仅 `svg/p7-yazyk.svg` 变化：`a53762d3…ea4` → `527a45eb…ecd9`。
- 其余 7 页 SHA-256 与改前完全相同（`svg-before.sha256` vs `svg-after.sha256`，diff 仅 1 行）。
- p7 SVG 内 U+2019：1 → 0；全部 8 个 SVG 内 U+2019：1 → 0；两 PDF P7 内 U+2019：有 → 无（fitz 验）。

## D7 实测（改后）

- PIL 真墨法（同法重测，`raster-straight-post.txt`）：直引号 advance 5.00px；整句 ’+s 合并为一个墨 run x562..572（阈值 20 下抗锯齿相连）；孤立词 `thema's` 18px 渲染：’ run x55..57 → s run x59..66，1 空白列。
- 交付 card（`cards/p7-yazyk.png`，`raster-png-post.txt`）：顶部墨带 rows 148..161：’ run x1820..1821 → s run x1825..1830，**3 空白列 / 边距 4px**；同带其余间隙 2–6 空白列——落入 1–6px 邻字母区间。
- 交付印 PDF 光栅（fitz 1950×2700，`pdf-print-p7.png`）：同一墨带 ’ run x1821..1822 → s x1825..1830，**2 空白列 / 边距 3px**。
- 交付网 PDF 光栅（`pdf-web-p7.png`）：与印 PDF 逐列相同（’ 1821..1822 → s 1825..1830）。
- 改前对照：同一墨带 16 空白列 / 边距 17px（见上节）。三源一致：card / 印 PDF / 网 PDF 均已修复。
- 裁图：`band-crop-post.png`（整条副标）、`apostrophe-zoom-card-post.png` / `apostrophe-zoom-pdfprint-post.png` / `apostrophe-zoom-pdfweb-post.png`（’s 区域放大）——肉眼读作 "thema's"，不再读作 "thema' s"。

## 门禁（逐项实测见 GATE-LOG.md）

- run.py rc=0 TOTAL 150；check_core.py rc=0（golden BAD 0，gloss 0，orphan 1 项与改前同，collision 1 项与改前同）。
- p8 extract 150/150（core 与版双侧）；p8 compare CLEAN，keydiff [137, 138, 139, 140]；直接 JSON keydiff 同 [137, 138, 139, 140]。
- occlusion 真实审计 42 flags 全 TEXTX，LINEX 0；旗标集合与改前构建逐项相同；交付 PDF 实测裁决 42/42 CLEAR（注：修正 SX=1.0 后 cards 判 38 CLEAR/4 OVERLAP、PDF 光栅判 41 CLEAR/1 OVERLAP——5 个争议旗标逐个实测均为误判：4 个 Краснодар 为 1px 真实间隙、1 个 Кипренского 为背景分类误判，正确浅底重测间隙 8 空白列；详见 GATE-LOG.md g5b）。
- freeze baseline 8/8（core 重建逐页 OK）；freeze diff 与改前构建相比唯一变化即 D7 句（p7 added_strings 卷引号 → 直引号），其余全同。
- 印/网文字层逐页一致（pdftotext 110,893 字节双侧；fitz multiset 37,531 字符双侧；逐页 [True ×8]）。
- P8 最小字号 9.75pt（印/网双 PDF，fitz；s11_check 同值）≥ SOP §1.1 下限 9.75pt；s11_check rc=0，FAILURES: none。
- 150 键复核无回归（见 p8 项）。
- D1/kicker/D2/D6 均验存活（见 GATE-LOG.md 末节）。

## 交付

- 本 scratch 内：`FIX-LOG.md`（本文件）、`GATE-LOG.md`；测量脚本 `measure_gap.py`、`raster_gap.py`；裁图 `band-crop-pre/post.png`、`apostrophe-zoom-*.png`、`glyph-*-180.png`、`adj-*.png`；日志 `run.log`、`render.log`、`webpdf.log`、`textmd.log`、`gates.log`、`sha-new.txt`、`svg-before/after.sha256`；门禁 JSON `core-p8.json`、`ru-nl-p8.json`、`ru-nl-p8-compare.json`、`ru-nl-occlusion.json`、`freeze-baseline.json`、`freeze-diff.json`；裁决脚本 `adjudicate_ru_fix1.py`（SX 修正版）、`adjudicate_upstream_sx.py`（交叉对照）；交付 PDF 光栅 `pdf-print-p7.png`、`pdf-web-p7.png`、`pdf-pages/`（8 页）。
- 未 commit、未 push（协调员统一处理）。未碰核心与其他版；未动 D1/kicker/D2/D6 及版内任何其他引号（ABSTRACT.txt 另一句 `thema's` 与 check_core.py L94 标点集常量有意保留，见计数表）。

## 结论

**a = 修完自验全过。** D7 已修复（’→'，三源实测间隙落入邻字母区间），重建三 SHA 如上，门禁逐项全过，无回归。
