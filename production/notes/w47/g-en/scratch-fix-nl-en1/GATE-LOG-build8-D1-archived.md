# GATE-LOG — W47 nl-en fix1 机械门（builder 自跑，2026-11-11，build 8）

- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（tools/venv）
- 命令：`~/workspace/weekly-git/tools/venv/bin/python ~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-nl/gates.py . en`（cwd 为版目录）
- 完整 stdout 存档：`en-gates8.log`（同目录）
- 退出码：0，OVERALL: ALL PASS

## 逐门结果（本次重跑实测）

```
[PASS] occlusion: rc=0 flags=0 svg/: 0 flags
[PASS] p8_extract: rc=0 noted=150/150
[PASS] p8_compare: rc=0 verdict=CLEAN keydiffs=0
[PASS] freeze_sha256: run rc=0 match=8/8
[PASS] print_web_text: pages 8/8 posdiff=0 msdiff=0 P1:795/795:pos0:ms0 P2:830/830:pos0:ms0 P3:738/738:pos0:ms0 P4:724/724:pos0:ms0 P5:807/807:pos0:ms0 P6:748/748:pos0:ms0 P7:915/915:pos0:ms0 P8:2318/2318:pos0:ms0
[PASS] pdftotext_nonempty: print=45404B web=45409B web_size=1574228
[PASS] p8_fontsize: answer-zone min=10.12pt median=10.12pt spans=187
[PASS] p8_chips: core={'A2': 8, 'B1': 24, 'B2': 3} edition={'A2': 8, 'B1': 24, 'B2': 3}
[PASS] s11_svg: off-palette={} gold/old=False stroked_rects=0 VOL.5=5(core 5) paper_fills=8
OVERALL: ALL PASS
```

## 补充自查（机械门之外）

- 身份（build 8）：print PDF 12,665,899 B / sha256 `2cc431f2572abad8790d1b99d6211d3aa87a5278a4052f3f0810dd6d764b0b58`；web PDF 1,574,228 B / sha256 `0fc6232bbe2bd8d3794169d83b4c233df519845f07eef1f9f35e2fdada2f6d18`；web < 7 MB。
- run.py 重跑：freeze 门内 clean-dir 重跑 rc=0、TOTAL 150；`en-build8.log` / `en-render8.log` 中 OVERFLOW / TOO WIDE / WARNING 计数均为 0。
- VOL 核对：印刷文字层 VOL.4 ×10；VOL.5 ×5（= core，见 s11_svg 门）。
- `.text.md` validator：`export_fanout.py` 导出校验——45,074 B；142 单题行 + 2 match headers + 8 match items = 150；8 golden；6 gloss（`en-export8.log`）。
- U+2019 全扫：源码（`content*.py`）0、`svg/` 0、`.text.md` 0、印刷 PDF 文字层 0、网页 PDF 文字层 0。
- 弯引号全扫（U+2018/U+2019/U+201C/U+201D/U+201A/U+201E/U+2032/U+2033）：源码 + SVG + `.text.md` + 双 PDF 文字层全部为 **0**。
- P8 答案字号：最小 10.12pt，中位数 10.12pt（≥ 9.75pt 底线）。
- 徽章：P8 A2 8 / B1 24 / B2 3，与 core 一致。
- 目视：P1 gloss `"Group win":` 与 P7 BRIEVEN `Editor's example ...` 两处裁图已验直引号、无宽空隙（见 FIX-LOG.md §7）。

## 结论

机械门 **9/9 全过**。本轮 builder 不做复校，待协调员另派第二轮全量复校。
