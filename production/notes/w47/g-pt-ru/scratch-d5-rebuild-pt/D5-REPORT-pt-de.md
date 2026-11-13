# D5 重建报告 — pt-de（2026-11-12）

- 安装：`apply_variant.py --target pt --reader de`（mode latin；本版 svglib 原无 fix2 块，安装时一并补入）；route_assert FAILURES: 0。svglib md5 `4228b7e7…` → `8f4599b1…`。
- D5 前：普查拉丁 514 处；基线门禁 occlusion/boxtitle/spill/edge 全 0。印 `b8a738de…`（12,938,912 B）、网 `013679d3…`（1,147,627 B）。
- 缺陷（5 项，全为 D5 引起，文字不动）：
  1. HEAD TOO WIDE ×2：P1 `AGORA VOCÊ　Jetzt sind Sie dran` 25→23；P2-ex 电池头 A–D 统一 25→22（同 core-pt）。
  2. 框标题越框 ×3：P1 `A SEMANA EM NÚMEROS　In Zahlen` +43.5px（box tsize 23→20）；P1 `EM POUCAS PALAVRAS　IN KÜRZE` +52.4px 且越页框（p.text 24→20）；P2 `PARA NÃO ERRAR　Die Merkregel` +1.5px（box tsize 23→22）。
- 门禁（gates-2，ALL-GREEN）：run TOTAL 150、0 警告；gates.py 16/16（德语页脚/金句检查无需改动）；occlusion 0；p8 extract 150/150、compare CLEAN（keydiff=[137,138]）；freeze baseline 8/8；freeze-diff vs 自身基线新增 CJK 0；spill 0；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0（n=418，中位 1.04，粗体 1.057；P8 253→253 行，余量 45.3px）；D5 census PASS；census_quotes 0；印/网文字层各 47,966 字节、逐字节相同。
- 新 SHA：印 `a8c54d0c9b428a6c313a27105c7d4abca294cbadf280a173c8734c14eaaba89b`（12,426,508 B）；网 `d76c126f27884924bb14302de1abd4e98fdfa4d7aa3f260d46550dcc458ad68a`（1,063,964 B，<7MB）。
- text.md 不变（md5 `9dfae3c4c21b5401dd209affff5e3596`）。
- KIT：§6 已更新 + 文末 D5 节；日志见 `scratch-d5-rebuild-pt/2026-w47-pt-de/`。
