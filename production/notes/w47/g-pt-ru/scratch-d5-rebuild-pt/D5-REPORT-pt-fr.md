# D5 重建报告 — pt-fr（2026-11-12）

- 安装：`apply_variant.py --target pt --reader fr`（mode latin；本版 svglib 已有 fix2 块）；route_assert FAILURES: 0。svglib md5 `152dd0fe…` → `449b31ee…`。
- D5 前：普查拉丁 504 处；基线门禁 occlusion/boxtitle/spill/edge 全 0。印 `d37d96f1…`（12,934,670 B）、网 `6dcf92f8…`（1,141,326 B）。
- 缺陷（5 项，全为 D5 引起，文字不动）：
  1. HEAD TOO WIDE ×1：P2-ex `C　COMPLETE COM OS NÚMEROS`，电池头 A–D 统一 25→22（同 core-pt）；同根 occlusion TEXTX（`26. a folga` 与加宽的电池头重叠 9.5×15.8px）随之消除。
  2. 框标题越框 ×3（P1）：`A SEMANA EM NÚMEROS　Chiffres` +26.5px（box tsize 23→20）；`NESTA EDIÇÃO　Dans ce numéro` +5.1px（p.text 24→22）；`EM POUCAS PALAVRAS　EN BREF` +37.4px（p.text 24→20）。
- 门禁（gates-2，ALL-GREEN）：run TOTAL 150、0 警告；gates.py 16/16；occlusion 0；p8 extract 150/150、compare CLEAN（keydiff=[137,138]）；freeze baseline 8/8；freeze-diff vs 自身基线新增 CJK 0；spill 0；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0（n=409，中位 1.04，粗体 1.057；P8 245→245 行，余量 47.4px）；D5 census PASS；census_quotes 0；印/网文字层各 47,430 字节、逐字节相同。
- 新 SHA：印 `90f78551a5eb6d0f8db6036a39c68e135d18679e69587c3185232580db81d2a3`（12,422,440 B）；网 `83f63d47ace71ce493d9850f244473ffb716c1dc8da3a6932f621e7b0eafb59a`（1,059,873 B，<7MB）。
- text.md 不变（md5 `98bdb7a249d9e86b3f497ef5317765a2`）。
- KIT：§6 已更新 + 文末 D5 节；日志见 `scratch-d5-rebuild-pt/2026-w47-pt-fr/`。
