# GATE-LOG — W47 nl-en 第一轮独立校对机械门（叶子自跑，2026-11-11）

- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（tools/venv）
- 命令：`~/workspace/weekly-git/tools/venv/bin/python ~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-nl/gates.py . en`（cwd 为版目录）
- 完整 stdout 存档：`gates-rerun.log`（同目录）
- 退出码：0，OVERALL: ALL PASS

## 逐门结果（本次重跑实测）

```
[PASS] occlusion: rc=0 flags=0 svg/: 0 flags
[PASS] p8_extract: rc=0 noted=150/150
[PASS] p8_compare: rc=0 verdict=CLEAN keydiffs=0
[PASS] freeze_sha256: run rc=0 match=8/8
[PASS] print_web_text: pages 8/8 posdiff=0 msdiff=0 P1:795/795:pos0:ms0 P2:830/830:pos0:ms0 P3:738/738:pos0:ms0 P4:724/724:pos0:ms0 P5:807/807:pos0:ms0 P6:748/748:pos0:ms0 P7:915/915:pos0:ms0 P8:2318/2318:pos0:ms0
[PASS] pdftotext_nonempty: print=45410B web=45415B web_size=1576939
[PASS] p8_fontsize: answer-zone min=10.12pt median=10.12pt spans=187
[PASS] p8_chips: core={'A2': 8, 'B1': 24, 'B2': 3} edition={'A2': 8, 'B1': 24, 'B2': 3}
[PASS] s11_svg: off-palette={} gold/old=False stroked_rects=0 VOL.5=5(core 5) paper_fills=8
OVERALL: ALL PASS
```

## 补充自查（机械门之外）

- 身份：print PDF 12,690,133 B / sha256 `0b4dc8c0e19b72a0d753842bdec7775064481a0b4b37bb88f66fa4aa5199f2e7`；web PDF 1,576,939 B / sha256 `477dd85dc87cda7ffa5ff71a5e5b15a5dcc33ff3db8d2ed49a8654f8a2cb8de6`——与 KIT 登记逐字一致。
- run.py 重跑：freeze 门内 clean-dir 重跑 rc=0、TOTAL 150；`en-build7.log` / `en-render7.log` 中 OVERFLOW / TOO WIDE / WARNING 计数均为 0。
- U+2019 全扫（8 SVG）：总数 **1**——`p7-taal.svg` 内 `Editor’s example` 一处（机械门不覆盖此项；见 PROOF-NOTE.md D1）。
- CJK 全扫：SVG 仅 P1 moth `<title>` 内 "三色蛾" 3 字（不可见）；印刷文字层 CJK 0；`.text.md` CJK 仅 "答案"×150；en 版 `content*.py` CJK 0；核心 243 条 CJK 字面量在 en 版源码中残留 0 条。
- 150 题分布独立重数：逐页 10/18/18/18/18/18/12/38；级别 A2 46 / B1 73 / B2 31。
- 金句 8/8 逐字见于正文，页码标注全对；范文实测 81 词。
- `.text.md` 45,080 B；VOL.4 印刷文字层 ×10；VOL.5 ×5；头条去空白 38 字符。

## 说明

机械门 9/9 全过，但机械门不覆盖 U+2019 宽字形类缺陷——本次唯一缺陷 D1 由 SVG 源码全扫 + 渲染图目视发现（见 PROOF-NOTE.md）。机械门全过 ≠ 本轮零问题。
