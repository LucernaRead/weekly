# GATE-LOG — W47 zh-tw-ko reproof3（独立复校，针对 fix2 重建版）

- 复校员：独立复校 reproof3（与 fix2 构建者不同人）
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-zh-tw-ko2/`
- 时间：2026-11-11 21:18–21:45 UTC
- 解释器：全程 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；`TMPDIR=<scratch>/tmp`；系统 /tmp 未用。
- 工具来源：`gates.py` / `gtools/` / `keycheck.py` 自 `scratch-fix-zh-tw-ko2/` 复制，仅改两处路径（M → 本 scratch；ED → 生产版目录 `~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-ko`）；`particle-sweep.py` / `pure-ko-scan.py` 同源，未改逻辑。工具本身未改。

## 0. 探针与 SHA（开工前）

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，rc=0；scratch 真实写盘通过（`tmp/probe.txt`）。
- 生产三件与任务给定逐字一致：印 16,838,020 B / `09fd27a05b0864bbb30da93339d4f2285abf351d44ca72cef5adb7e254ea3d1c`；网 2,325,045 B / `e4832f3f8a789eb89e7a68c39f3986fc7428baae395223a1de27844dfd8dede4`；text.md 53,916 B / `a44ba8cbb74f28c862b8f689f27e260a2fde3c5ac328e1597147ff933029b1e1`。
- 核心基线（复校前后两次一致，未变）：印 `5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a`（19,420,552 B）、网 `1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240`（2,324,042 B）、text `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b`（49,798 B）。
- 磁盘：/home/hatch 150G 总，94G 已用，56G 可用（开工时）；全程无 EDQUOT。

## 1. gates.py 全部门禁（`gates.py ko reproof3`，输出 `gates/ko-reproof3/gates.json`，rc=0）

| 门 | 结果 | 证据文件 |
|---|---|---|
| checks.py | PASS，rc=0；8 条金句各 2 次；`SIMP_ONLY_HITS []`；P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43] | `gates/ko-reproof3/checks.log` |
| occlusion audit | selftest rc=0，flags **0** | `occlusion-selftest.log`、`occlusion.log`、`occlusion.json` |
| p8 extract + compare --total 150 | extract 150/150；compare **CLEAN**（keydiff []、missing []、extra []、uncertain []） | `p8-extract.json`、`p8-compare.json` |
| canonical creambox | 36 盒；负清除 **0**；各页 inside-only 最小 P1 18.8 / P2 41.8 / P3 16.1 / P4 35.8 / P5 6.4 / P6 19.9；P7 工具盒 +40.5／+12.5／+14.0 | `creambox.log` |
| boxtitle（真墨） | 36 盒，超框 **0**，最小右余 **18.5px**（P1 18.5、P2 19.5、P3 20.0、P4 23.8、P5 19.2、P6 20.2、P7 139.2）；最小左余 18.0px | `boxtitle.log`、`boxtitle.json` |
| creambox-pil（真墨） | STRADDLE **0**，CREAM-COVER **0**；各页最小底清除 P1 16.5 / P2 39.8 / P3 14.1 / P4 33.8 / P5 4.4 / P6 17.1 / P7 10.5 | `creambox-pil.log`、`creambox.json` |
| 印／网文字层 | 多重集差分 **0** 字符（print 95,029 B = web 95,029 B）；「本週日」11、「下週日」0、BABYMONSTER 0、「取捨」2 | `print.txt`、`web.txt` |
| PDF 指标（PyMuPDF） | 印、网皆 8 页、1462.5×2025 pt；最小字号 **9.75pt**（整刊与 P8 皆然）；P8 最大 34.5pt；P1 最大 147.0pt；印 16,838,020 B、网 2,325,045 B | `gates.json`（`pdf`） |
| keycheck（填空键 + 连续性） | 填空键 **54/54** 在正文，缺失 0；答案 1–150 连续 | `fillin-check.log` |
| 英文泄漏扫描 | deny_hits {}；shared_ascii_long 仅「A. 12:00 · B. 14:00 · C. 19:00」 | `gates.json`（`leak_scan`） |
| P6 时间轴衔接（真墨） | 18:30「頒獎典禮」墨右缘 990.8 → 19:00「夜間遊行」墨左缘 991.4，墨缝 **0.6px** | `gates.json`（`abutting`） |
| freeze baseline（本版） | **8/8** 字节一致（repointed files: content12/34/56/7/8.py）；核心完整性 OK | `freeze.log`、`freeze-base/` |
| 文件 SHA | 印／网／text.md 与 §0 一致；P7 SVG `ea987634…`，P8 `a390fcc6…`，P1–P6 与 proof1 旧版相同 | `gates.json`（`files`） |

## 2. freeze diff（`freeze.py diff --core-svg <core-zh-tw>/svg --edition-svg <edition>/svg`，`gates/freeze-diff.json`，rc=0）

逐页增／删（与 fix1/fix2 版逐值相同）：p1 +24/−25、p2 +35/−39、p3 +42/−47、p4 +36/−39、p5 +46/−47、p6 +31/−33、p7 +360/−120、p8 +188/−187；新增 CJK 共 **4,690** 字；新增皆为韩文音节 + 引用的中文词。逐页新增 CJK：p1 332、p2 293、p3 343、p4 313、p5 393、p6 320、p7 803、p8 1,893。

## 3. freeze baseline（核心，任务书字面口径另跑）

`freeze.py baseline --build <core-zh-tw> --core-svg <core-zh-tw>/svg --out gates/core-freeze-base` → **8/8** 字节一致（repointed files: content56/12/34/7/8.py）；核心完整性 OK。见 `gates/core-freeze.log`。
说明：gates.py 内的本版 baseline 用 `--core-svg svg`（版内已交付 SVG 参照集，canonical 用法）；本节另按任务书字面口径以 `--core-svg` 直指 core-zh-tw 的 svg 子目录跑核心基线，亦 8/8。两者互补，均绿。

## 4. keycheck 三源交叉（`keycheck.py`，输出 `keycheck-150.json`，rc=0）

- 三源一致 **150/150**，mismatches []；B 解析 150 项，范围 1..150，缺失 []。
- SVG CJK 版独有 {韓}、核心独有 {英}；text.md 同样。
- p1–p8 净 CJK 增量：仅 韓／國 为正（家具徽章），其余为引词等量替换；p7 净增 入／集／圍／間／夜／市各 1（韩语释义引用的中文词）。
- 引号：版 SVG U+0022 0、U+0027 1（`Kanahei's Little Animals` 专名）；text.md 同。
- 英文日／月名泄漏：'Sunday'–'Saturday'、'November'、'December'、'January'、'next Sunday'、'Next Sunday'、'finish line'、'end point'、'下週日'、'下周日'、'다음 주 일요일'、'BABYMONSTER'、'결승선'、'finish'、'장소' 皆 0；'이번 주 일요일' SVG 2 / text.md 2。
- P8 标头：A 判斷對錯／B 本週大測驗／C 完成句子／D 讀一讀，答一答／E 情景說話／F 寫一寫，韩语对译齐全。
- 写作范文：去空白 142 字，CJK+数字 126，120–180 区间内 ✓。

## 5. K2 / K1 / 助词扫查（独立重测）

- K2 旧形「小雪는」：8 SVG + text.md + content7.py 各 **0**；新形「小雪은」：content7.py:60 ×1、p7-lang 节点 x=989.0 y=458.42 ×1、text.md:4699 ×1；`Xiaoxue는` text.md 6 处未动。
- K1 旧形 5 串（入圍은／鋼雕은／入圍을／市集는／入圍이에요）：SVG + text.md 各 **0**；新形：入圍는／鋼雕는／入圍를／市集은 各 SVG 1 处 + text.md 1 处，入圍예요 SVG 2 处 + text.md 2 处；`입니다`／`습니다` 全版 0。
- particle-sweep（`particle-sweep.py`，SVG + text.md）：19 形 50 命中；与 fix2 `old-build/` 扫查 diff **仅「小雪는」→「小雪은」一处**（`sweep-old.txt` / `sweep-new.txt`）。
- pure-ko-scan（`pure-ko-scan.py`）：元音＋을 0、辅音＋를 0、元音＋은 0、元音＋이에요 0、辅音＋예요 0；元音＋이 2 命中（풍선이／한작품이）皆为辅音结尾 이，正确。
- U+FFFD：8 SVG + text.md 按字节计 **0**。

## 6. 盒标题 STRADDLE 备份旧版对照（fix2 `old-build/`）

- 新版：boxtitle 36 盒、超框 0、最小右余 18.5px；creambox-pil STRADDLE 0、CREAM-COVER 0。
- 旧版（`gates/old-build/`）：boxtitle 36 盒、超框 0、最小右余 18.5px；creambox-pil STRADDLE 0、CREAM-COVER 0。
- **新旧逐值相同，无回归、无差异**。判定缺陷前已跑备份对照（任务书要求；it-de D1/D2 只比核心误判的先例已避开）。

## 7. 渲染证据（交付印 PDF 渲染，`render/`）

- 200 dpi 全页：`p200-1.png` … `p200-8.png`（PyMuPDF，200dpi），8/8 逐版目视干净。
- 放大取证（200dpi 裁切）：`zoom-k2-p7-b2.png`（小雪은 在版，同句三词在版）、`zoom-k1-p7-b1.png`（入圍는／鋼雕는）、`zoom-k1-p7-memory.png`（入圍를）、`zoom-k1-p7-b2b.png`（市集은）、`zoom-k1-p8-q105.png`（入圍예요 Q105）、`zoom-k1-p8-q132.png`（入圍예요 Q132）。

## 8. 文件清单（本目录，本轮新增）

- `PROOF-NOTE.md`（本轮结论 (a)）、`GATE-LOG.md`（本文件）、`probe.txt`、`tmp/probe.txt`、`gates.py`、`gtools/`、`keycheck.py`、`keycheck-150.json`、`particle-sweep.py`、`pure-ko-scan.py`、`sweep-old.txt`、`sweep-new.txt`、`gates/ko-reproof3/`（gates.json 及各门日志／JSON／freeze-base）、`gates/freeze-diff.json`、`gates/freeze-diff.log`、`gates/core-freeze.log`、`gates/core-freeze-base/`、`gates/keycheck.log`、`gates/old-build/`（boxtitle.log、creambox-pil.log）、`render/p200-1.png` … `render/p200-8.png`、`render/zoom-k2-p7-b2.png`、`render/zoom-k1-p7-*.png`、`render/zoom-k1-p8-*.png`、`tmp/`。

## 9. 未做事项（按红线）

未改任何源文件、未重建交付物、未 commit、未 push、未派 subagent、未改 freeze.py / gates.py 等工具、未写生产目录任何东西（生产 `__pycache__/` mtime 仍为 2026-11-11 12:49:59，未变）。收工重验：生产三 SHA 与开工时同一组，未变。
