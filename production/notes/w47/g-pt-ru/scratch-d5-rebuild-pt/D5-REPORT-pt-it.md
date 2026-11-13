# D5 重建报告 — pt-it（2026-11-12）

- 安装：`apply_variant.py --target pt --reader it`（mode latin；本版 svglib 已有 fix2 块）；route_assert FAILURES: 0。svglib md5 `152dd0fe…` → `449b31ee…`。
- D5 前：普查拉丁 502 处；基线门禁 occlusion/boxtitle/spill/edge 全 0。印 `f9f892d1…`（12,930,844 B）、网 `62c98772…`（1,137,090 B）。
- 缺陷（6 项，全为 D5 引起，文字不动）：
  1. HEAD TOO WIDE ×1：P2-ex `C　COMPLETE COM OS NÚMEROS`，电池头 A–D 统一 25→22（同 core-pt）；同根 occlusion TEXTX（`26. a folga` 与加宽的电池头重叠 9.5×15.8px）随之消除。
  2. 框标题越框 ×3：P1 `A SEMANA EM NÚMEROS　In cifre` +17.5px（box tsize 23→20）；P1 `EM POUCAS PALAVRAS　IN BREVE` +49.4px（p.text 24→20）；P7 `ERROS COMUNS　Errori frequenti` +6.7px（p.text 23→21）。
  3. 自查 FAIL ×1（与第 2 项同根）：page-frame ink crossings = 1——`IN BREVE` 标题墨水越过 P1 页框右缘 1.4px；同一次 24→20 缩字修复。
- 门禁（gates-2，ALL-GREEN）：run TOTAL 150、0 警告；gates.py 16/16；occlusion 0；p8 extract 150/150、compare CLEAN（keydiff=[137,138]）；freeze baseline 8/8；freeze-diff vs 自身基线新增 CJK 0；spill 0；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0（n=409，中位 1.04，粗体 1.057；P8 227→227 行，余量 47.3px）；D5 census PASS；census_quotes 0；印/网文字层各 46,710 字节、逐字节相同。
- 新 SHA：印 `56f388e7ce3a1a7c1faf5d9f0e214758b41f9dca32f95d4efa0d59abf042f7aa`（12,418,794 B）；网 `ab8305b734dc085e482bcad725a259b42bc983da3efe33405d4be627dc4b55ae`（1,056,196 B，<7MB）。
- text.md 不变（md5 `39b09bea2a4f4aa4ee1013eabde15c3a`）。
- KIT：§6 已更新 + 文末 D5 节；日志见 `scratch-d5-rebuild-pt/2026-w47-pt-it/`。
