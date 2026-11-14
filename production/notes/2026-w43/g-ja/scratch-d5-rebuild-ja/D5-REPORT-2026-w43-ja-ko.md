# D5 重建报告 — 2026-w43-ja-ko（韩语读者版）

W43 ja 家 D5 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader；西里尔字母改走 Noto Sans；日文正文仍走 Noto Sans/Serif CJK JP）。施工 2026-11-13/14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-ja/logs/2026-w43-ja-ko/`（`GATES-SUMMARY.txt` 为门禁总表）。
家族报告：`hidden_files/d5-redo/FAMILY-W43-JA-BUILD.md` §2–§9。

## 一、装机

- 本家走**移植模板路线**（D5-METHOD §1.7）：组装后的 fanout svglib（427 行，JP/TC 双下标 + `face=` 参数）被安装器按设计拒绝（`apply_variant.py --check` 死于 step 2 cmap，`pattern found 0x`；证据 `logs/installer-refusal-fanout.log`）。故 svglib 取移植模板 `svglib-ja-d5.py` 原样装为本版 `svglib.py`，只改 `_D5_READER` 一行。
- 本版 `_D5_READER = "cjk"`；装后 svglib 与 W47 对应模式参照**逐字节相同**（cjk：W47 ja-ko）。fix2 块 + `_QUOTE_CLS` + kinsoku（NO_START）齐全；routing probe（在已装文件上实测 `_char_font`）0 失败。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（全家共用一次）。


- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `style-port-ja/textexp_ja.py` 新建导出（本家无已发 `.text.md`，11 份全新建，随 bundle 入仓）。

## 二、基线（修前组装版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- SVG 8/8 与 fanout 逐字节相同；textexp 与 fanout `.text.md.new` BYTE-IDENTICAL。
- 印 PDF 40,068,374 B，SHA 与 fanout D1 后印 PDF 一致；网 PDF 文字层 print=web 差 0、web vs fanout 网差 0；pdfdiff vs issues 已发网 PDF **IDENTICAL 8/8**。
- 修前普查 `d5_census.py`：D5 拉丁 214、西里尔 0、弯引号在 CJK 0（>0，符合装机前提）。
- P8：noted **150/150**（core 对照亦 150/150）。

## 三、缺陷与修法（run1 → run2）

run1 除门 15b（见下）外零缺陷，**无需二次修复**（未动任何字号与文字内容；run1 即终版）。

- 门 15b `verify_textmd.py` carryover FAIL：共享校验器的表与 drop 规则按 pt 目标语家族标定，ja 目标语格式不在其覆盖内——基线（修前 port 期已验版）同跑亦 FAIL（MD-only 2995 token vs 重建版 3209，SVG-only 4 vs 6），故为**工具-格式口径差，非重建缺陷**。权威验收为门 15c：ja 原生校验器 `verify_textexp_ja.py --edition` **ADOPT（0 UNEXPECTED）**，与 it/es 家用各自原生校验器作门 15 权威证据同款。仅余 SVG-only 6 token（`→`×2、`200`、`hersom`、`／`、`〜`各 1）均为 P6 图片 credit 行 `写真：EJ Hersom／米国防総省` 的 D5 run 拆分 token 化边缘——该行在 SVG 与 .text.md 两侧俱全，无内容缺失。


## 四、门禁（run1，17 门 + D18）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0；noto_sans_elements=0 |
| 4 render | RC=0，印 PDF 40,035,875 B |
| 5 webpdf | RC=0，网 PDF 2,728,520 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**（missing=[]，extra_count=0；keydiff=[137, 138]——KIT 已登记的读者语答案键 #137/#138） |
| 9 freeze baseline | 8/8（patched 自复现） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings TOTAL 91，run 拆分所致；本家无 es 家的 U+3000 TOTAL 1） |
| 11 spill | 0 SPILL（0 SPILL, 162 OBSERVE） |
| 12 boxtitle | 0 DEFECT（0 DEFECT, 0 OBSERVE, 0 marginal） |
| 13 edge | 0 TOUCH, 0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 196→196 行，slack 48.9→48.9px） |
| 15a 文字层 print=web | 字符多重集差 **0**（print 17437 = web 17437） |
| 15b verify_textmd carryover | FAIL（工具-格式口径差，见 §三；权威证据为 15c） |
| 15c verify_textexp_ja --edition | **ADOPT**（0 UNEXPECTED；REWRAP 30，仅 D5 重排） |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | ja 家无 gates.py |
| 18 masthead（D18） | **PASS**：标语右端→日期左端间距 **303.2px**（VOL 左缘误差 0.0、日期右缘误差 0.0） |

**OVERALL: 16/17 门 + D18 全绿；门 15b 为已解释的工具口径差（权威 15c ADOPT）。**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`；印 PDF 不入 issues）

- 印 PDF：`Lucerna-VOL1.pdf`，**40,035,875 字节**，
  SHA-256 `378f9808d6bd9918d32c25e3d1d77825f5ab0687fdfb249f34af21290bbfb722`
  （D5 前基线 40,068,374 字节，`1e5f1cfe4268…`）。
- 网 PDF：`2026-w43-ja-ko.web.pdf`，**2,728,520 字节**，
  SHA-256 `2f62a5b318c043962d2289aa251b58fc5f77a11a92a4df966154b7c211b6124b`
  （D5 前 issues 已发版 2,782,053 字节，`facd9df55802…`）。
- text.md：**新建** `2026-w43-ja-ko.text.md.new`，47,827 字节，
  SHA-256 `891cf136fa7aeab2d5478bb71dd5756289b95ba90b14d106cc85ca1ccaf08594`
  （本家无已发 `.text.md`；与 fanout `.text.md.new` 的差异仅 D5 重排，15c ADOPT）。
- 练习总量仍为 **150 题**，与 core 逐题一致（KIT 注册表未变；keydiff [137, 138]）。

## 六、KIT

- `production/2026-w43/2026-w43-ja-ko/WEEKLY-KIT.md`：文末追加 **D5 rebuild（2026-11-13）** 节（装机、基线、门禁、新交付物 SHA/字节）。
