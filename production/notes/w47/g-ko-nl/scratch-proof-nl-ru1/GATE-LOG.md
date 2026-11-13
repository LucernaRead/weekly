# GATE-LOG — 2026-W47 nl-ru proof1（17 门逐项实测值）

- 版：`2026-w47-nl-ru`，VOL.4，8 版，150 题（A2 46 / B1 73 / B2 31；by page 10/18/18/18/18/18/12/38）
- 解释器：`tools/venv/bin/python`（Pillow 13.0.0）；TMPDIR = 本 scratch；`PYTHONDONTWRITEBYTECODE=1`
- 三 SHA（开工与收尾两次实测一致）：印 `21b7adf007a15e195756d49b22c824e828f854e11e02a10c916426997c468cc8` / 12,718,418 B；网 `1a17474368591008dcefb73661be58a17edc38c5dcc98f674fc0afe6ea6cc9bf` / 1,661,392 B；文 `f23da475ff54bcfe86bbe6794473eafc65b42dbd5f015766924ce3e83cefb984` / 57,870 B

| # | 门 | 实测值 | 结论 |
|---|---|---|---|
| 1 | SHA 身份核对 | 印/网/文三 SHA + 字节与任务给定值及 KIT build-6 逐字一致；收尾复测一致；8 个交付 SVG SHA 开工/收尾一致 | PASS |
| 2 | run.py scratch 重建 | `repro-build/` rc=0；TOTAL 150；by page 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31；OVERFLOW / TOO WIDE 0；`flow[P1-headline] y=1465`、`flow[P8-keys] y=2486 (bottom 2560)`、`P4 col3 ends 1229.6`（`run-rebuild.log`） | PASS |
| 3 | 重建 SVG 8/8 字节一致 | scratch 重建 SVG sha256 vs 交付 SVG：p1–p8 全部 OK（`repro-svg-sha.txt`） | PASS |
| 4 | 印 PDF 重渲逐字节相同 | scratch `render.py` rc=0；12,718,418 B；SHA `21b7adf0…468cc8` = 交付印 PDF（`render-rebuild.log`） | PASS |
| 5 | freeze 核心 baseline 8/8 | `freeze.py baseline --build core-nl --core-svg core-nl/svg` rc=0；8/8 字节一致；核心 shipped SVG 跑前后哈希不变（`freeze-core.log`） | PASS |
| 6 | freeze 本版自身 8/8 | gates `freeze_sha256`：clean-dir 重跑 run.py rc=0，match 8/8（`gates.log`） | PASS |
| 7 | occlusion 几何审计 | `tools/occlusion_audit.py svg/` rc=0，**0 flags**；自检六类全触发（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），干净对照静默（`occlusion.log`） | PASS |
| 8 | 奶油盒纵+横双扫 | 纵扫 3 flags（P2 底、P5 底、P6 右）均为假阳性：P2/P5 盒底下 7px 条带 0 非纸像素；P6 盒右沿外 x1862–1875 条带 0 非纸像素，真墨余量 +9.5px；横扫（盒标题隔离真墨）59 标题 0 越边（`creambox.log`、`probe-cream-d11.log`、`boxtitle2.log`） | PASS |
| 9 | 盒标题计数（自定重数） | 独立 census：盒标题 21 + head 出现 38 = **59**；26 奶油 rect 中 5 个无标题事实盒（标题在盒外上方）；31 个不同 head 源字符串逐一核对，SVG 精确匹配；最紧 +9.5px（`title-count.log`、`heads-source.txt`） | PASS |
| 10 | spill 横扫 | P4 HET PROGRAMMA 盒（底 1229.6）0 BELOW 命中；其余 BELOW 均为独立版块（下一节标题/提示语/gloss），ABOVE/SIDE 为图注/邻盒标题/刊头；真溢出 0（`spill.log`） | PASS |
| 11 | 孤儿扫查 + 核心集比对 | PIL + svglib 双 advance，1464 行：独行标点 0，行首标点 0；brute-force 闭标点 `<text>` 5 个、leftmost 0；核心集同法 0/0 → **0 新增**（`orphan.log`、`orphan-core.log`） | PASS |
| 12 | p8 extract 150/150 | noted set = 150 of 150（`gates/p8-extract.json`、`gates/p8-extract.log`） | PASS |
| 13 | p8 compare | vs 核心：**CLEAN**；missing []、extra 0、uncertain []；keydiff **[137, 138]**（翻译题键即读者语，按设计；140 已修出该表）（`p8-compare.json`） | PASS |
| 14 | 三方比对 + keycheck | registry vs text.md vs P8：**149/149 MATCH**，DIFF=[]、MISSING=[]；配对键 25–28=d/c/a/b、141–144=b/c/d/a；Q150 例外已重组核实：P8 `✓`（x=1470.1,y=2470.24）、text.md:431 Tekstmodel **81 词**（`p8-compare-3way.json`、`d9-check.log`） | PASS |
| 15 | 印/网文字层 8 页 | posdiff 0、msdiff 0，tokens 797/802/722/727/783/730/885/2151；pdftotext 印 55,000 B = 网 55,000 B；网 PDF 1,661,392 B < 7 MB（`gates.log`） | PASS |
| 16 | P8 最小字号 + chips | 答案区 min **10.12pt**（median 10.12，598 spans）≥ 9.75pt；chips core=edition {A2: 8, B1: 24, B2: 3}（`gates.log`） | PASS |
| 17 | §1.1 调色板/禁用色/VOL | off-palette {}；禁用金/红褐色无；stroked rects 0；paper fills 8；VOL.5=5=core（P2 1 + P7 4，均为下期前瞻引用）；VOL.4 各页刊头/页脚共 10 处；页脚全角空格分隔（`gates.log` s11_svg） | PASS |

## 附加核验（折入上述各门，不另立门）

- **Delta D6–D11 复核**（`width-scan.log`、`probe-cream-d11.log`、`probe-pdf-d11.log`、`d9-check.log`）：D6 区间 304.3–427.8 / 中点 366.05；D7 419.8–451.9 / 435.85（行 1 实测 419.78px ≤ CW 422.5）；D8 353.1–385.5 / 369.3；D10 373.2–395.4 / 384.3；四处断行逐字不变，p3/p6/p7 SVG 字节一致。D9 三源一致（REG 键 = text.md:415 = P8 y=2173.64，`Ik maak een surprise met een kort gedicht.`；题干 `Я делаю сюрприз с небольшим стихотворением.`）。D11 双法：卡片 PIL 真墨余量 +20.60px、印 PDF 150dpi 真墨余量 +19.6px（1px 量化差）、基线余量 +20.11px、盒底下 7px 条带双法 0 墨；模拟偏移 617.89 与 SVG 实测一致。
- **语义抽查 ≥8 题**（`spotcheck.log`）：配对题 Q25–28、Q141–144 逐组核对（选项表逐字验）；单题 Q1、Q7、Q11、Q36、Q37、Q83、Q113、Q130、Q137、Q138、Q145、Q149 均正确；另验 Q22/Q43–Q45/Q46–Q51/Q57/Q124–Q128/Q133–Q136/Q139；图表求和 35+30=65、35+30+20+15=100；内部积分/赛程三处一致。
- **日期全验**：`date -d`：16 Nov 周一 … 22 Nov 周日；14 Nov 周六、15 Nov 周日、1 Nov 周日、24 Nov 周二、29 Nov 周日、5 Dec 周六；刊头 `WEEK VAN 16 TOT EN MET 22 NOVEMBER 2026` ✓。
- **目检 8 页**：交付卡片 P1–P8 逐页看过，无溢出/重叠/压页脚/裁切；P7 金句 8 句逐字核对原文与页码；裁图证据：`crop-p4-programma.png`、`crop-p8-q140.png`、`crop-p6-title.png`、`crop-p2-enjij.png`、`crop-p5-enjij.png`、`crop-p2-gedicht.png`。
- **ABSTRACT / text.md 计数**：ABSTRACT 俄语单行、0 ASCII 双引号；text.md 单题 142 行 + 配对头 2 + 配对项 8 = 150；`>` 词表 6 行 + 金句 8 行 = 14，与 KIT 一致。
- **未动生产确认**：收尾三 SHA 与 8 SVG SHA 与开工一致；生产目录无文件在本轮开工后被修改。

## 总结论

**17/17 PASS。结论 (a) 零缺陷，可定稿。缺陷清单：无。**
观察类：O1 填空行（核心继承）、O2 P2/P5 盒底 2px 容差伪报、O3 P6 标题最紧 +9.5px、O4 标题计数口径 59 vs 简报 56——均不构成缺陷，详见 PROOF-NOTE.md。
