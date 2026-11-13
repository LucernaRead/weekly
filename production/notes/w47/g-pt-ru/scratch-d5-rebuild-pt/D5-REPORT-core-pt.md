# D5 重建报告 — core-pt（2026-11-12）

- 接手状态：上一任已装 D5（svglib md5 `44a000db…`，`_D5_READER="cjk"`）并重建；gates-1 大半已过，遗留 HEAD TOO WIDE ×1 + 自查 2 FAIL，freeze baseline 未跑。
- 修复（2 项，文字不动）：
  1. P2-ex 电池头 `C　COMPLETE COM OS NÚMEROS` 越栏：text_w 408.8→460.0px（+12.5%），超栏 37.5px；P2-ex 四头字号统一 25→22（C 在 22 时 404.7px）。
  2. 自查 2 FAIL 为 D5 run 拆分测量假象（页脚 `第1版／共8版`、P7 金句 `总比分定格在 2 比 2。 (Página 4)`）：`gates_core.py` 新增 `squashed()` 空白折叠比对，仅用于该两项检查；基线复核 16/16，pdftotext 仍提 `第1版／共8版`。
- 门禁（gates-2，ALL-GREEN）：run TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE（head_check PASS）；occlusion 0 flags；p8 extract 150/150；freeze baseline 8/8；freeze-diff 新增 CJK 0；spill 0；boxtitle 0 DEFECT；edge 0 TOUCH, 0 NEAR；creambox PASS 0 defects（机制版 + tools 版双跑，n=383，中位 1.04，粗体 1.057；P8 229→229 行，余量 44.3px）；D5 census PASS（拉丁/西里尔/弯引号 CJK 均为 0）；census_quotes 0 defective；自查 16/16；印/网文字层各 44,343 字节、逐字节相同。
- 新 SHA：印 `edcb8d3d692089337287892646dce2845f9254edfb4b6d3ad9e0e2b41b0f3d1f`（14,137,984 B）；网 `ca9f7722ecb261e023a2600cde21639bb57c507da29e51fd14522b4e8f29ed34`（1,389,823 B，<7MB）。
- text.md 不变（md5 `a812b29406ba22eeb721ad4220971b84`）。
- KIT：§6 已更新 + §8e  dated 记录；历史 SHA 保留在 §8e。
- Logs：`scratch-d5-rebuild-pt/core-pt/`（gates-2/、freeze-2/、freeze-baseline.log、run/render/webpdf.log）。
