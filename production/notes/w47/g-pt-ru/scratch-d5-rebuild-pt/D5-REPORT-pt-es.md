# D5 重建报告 — pt-es（2026-11-12）

- 安装：`apply_variant.py --target pt --reader es`（mode latin；本版 svglib 原无 fix2 块，安装时一并补入）；route_assert FAILURES: 0。svglib md5 `4228b7e7…` → `8f4599b1…`。
- D5 前：普查拉丁 503 处；基线门禁 occlusion/boxtitle/spill/edge 全 0。印 `75e870cf…`（12,933,061 B）、网 `7893d33e…`（1,140,277 B）。
- 缺陷（3 项，全为 D5 引起，文字不动）：
  1. HEAD TOO WIDE ×1：P2-ex `C　COMPLETE COM OS NÚMEROS`，电池头 A–D 统一 25→22（同 core-pt）。
  2. 框标题越框 ×2（P1）：`A SEMANA EM NÚMEROS　En cifras` +35.5px（box tsize 23→20）；`EM POUCAS PALAVRAS　EN BREVE` +38.9px（p.text 23→20）。
- 门禁（gates-2，ALL-GREEN）：run TOTAL 150、0 警告；gates.py 16/16（FAILURES: none）；occlusion 0；p8 extract 150/150、compare CLEAN（keydiff=[137,138]）；freeze baseline 8/8；freeze-diff vs 自身基线新增 CJK 0；spill 0；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0（n=409，中位 1.04，粗体 1.057；P8 240→240 行，余量 47.3px）；D5 census PASS；census_quotes 0；印/网文字层各 47,060 字节、逐字节相同。
- 新 SHA：印 `9e80ddac138919ac5721a96052ee26a69b4c9179baeadb3ad0a692d4cb3f08da`（12,421,396 B）；网 `4f918ab38188d7da5339cb15a7c298721b393e013c8c485515b1c22f723e7ef6`（1,058,824 B，<7MB）。
- text.md 不变（md5 `9bdf14009d81b76ee4939b074afe427c`）。
- KIT：§6 已更新 + 文末 D5 节；日志见 `scratch-d5-rebuild-pt/2026-w47-pt-es/`。
