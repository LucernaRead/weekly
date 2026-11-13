# D5 重建报告 — pt-en（2026-11-12）

- 安装：`apply_variant.py --target pt --reader en`（mode latin；本版 svglib 原无 fix2 块，安装时一并补入）；route_assert FAILURES: 0。svglib md5 `4228b7e7…` → `8f4599b1…`。
- D5 前：普查拉丁 500 处；基线门禁全 0。印 `7e235e45…`（12,932,441 B）、网 `47650ec4…`（1,139,920 B）。
- 缺陷（3 项，全为 D5 引起，文字不动）：
  1. HEAD TOO WIDE ×1：P2-ex `C　COMPLETE COM OS NÚMEROS`，电池头 A–D 统一 25→22（同 core-pt）。
  2. 框标题越框 ×2（P1）：`A SEMANA EM NÚMEROS　In numbers` +24.0px（该框已有 fix round 2 的 tsize=21，D5 后再降至 19）；`EM POUCAS PALAVRAS　In brief` +16.4px（p.text 24→22）。
- 门禁（gates-2，ALL-GREEN）：run TOTAL 150、0 警告；gates.py 16/16；occlusion 0；p8 extract 150/150、compare CLEAN（keydiff=[137,138]）；freeze baseline 8/8；freeze-diff vs 自身基线新增 CJK 0；spill 0；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0（n=409，中位 1.04，粗体 1.057；P8 237→237 行，余量 44.3px）；D5 census PASS；census_quotes 0；印/网文字层各 45,958 字节、逐字节相同。
- 新 SHA：印 `91fa99c4ed0bef7120ac3c4e906c16682a3031305151132308a2dae5a2fccd86`（12,421,287 B）；网 `b100c5765c5fbd645aef430244ad1d794d15c6027028c873e106b20cda3762f5`（1,058,717 B，<7MB）。
- text.md 不变（md5 `1d0567bb24937ce9e833a2a9da6ca259`）。
- KIT：§6 已更新 + 文末 D5 节；日志见 `scratch-d5-rebuild-pt/2026-w47-pt-en/`。
