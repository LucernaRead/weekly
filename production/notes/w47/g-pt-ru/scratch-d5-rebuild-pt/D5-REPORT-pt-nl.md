# D5 重建报告 — pt-nl（2026-11-12）

- 安装：`apply_variant.py --target pt --reader nl`（mode latin；本版 svglib 原无 fix2 块，安装时一并补入）；route_assert FAILURES: 0。svglib md5 `4228b7e7…` → `8f4599b1…`。
- D5 前：普查拉丁 506 处；基线门禁 occlusion/boxtitle/spill/edge 全 0。印 `7404001d…`（12,935,296 B）、网 `6460410a…`（1,142,952 B）。注：KIT §6 旧行所记印/网 SHA 与快照盘上值不符（盘上值见 KIT 文末 D5 节注释；与 pt-fr fix2 节同类情况，快照文件为准）。
- 缺陷（5 项，全为 D5 引起，文字不动）：
  1. HEAD TOO WIDE ×1：P2-ex `C　COMPLETE COM OS NÚMEROS`，电池头 A–D 统一 25→22（同 core-pt）；同根 occlusion TEXTX（`26. a folga` 与加宽的电池头重叠 9.5×15.8px）随之消除。
  2. 框标题越框 ×3：P1 `A SEMANA EM NÚMEROS　In cijfers` +34.5px（box tsize 23→20）；P1 `EM POUCAS PALAVRAS　KORTOM` +44.4px（p.text 24→20）；P2 `PARA NÃO ERRAR　Ezelsbruggetje` +5.5px（box tsize 23→21）。
- 门禁（gates-2，ALL-GREEN）：run TOTAL 150、0 警告；gates.py 16/16；occlusion 0；p8 extract 150/150、compare CLEAN（keydiff=[137,138]）；freeze baseline 8/8；freeze-diff vs 自身基线新增 CJK 0；spill 0；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0（n=413，中位 1.04，粗体 1.057；P8 255→255 行，余量 43.3px）；D5 census PASS；census_quotes 0；印/网文字层各 47,100 字节、逐字节相同。
- 新 SHA：印 `7fbf77a5d9da65c1b8e7921eb911988e0a27230ccd1b125606ae4baa6917a153`（12,422,999 B）；网 `0fc3730b1fb50a6bf279e9e33b43794bd431c4bc319252602e4bb707c5d722de`（1,060,452 B，<7MB）。
- text.md 不变（md5 `40b63423459e8a956bdfba81acc85412`）。
- KIT：§6 已更新 + 文末 D5 节；日志见 `scratch-d5-rebuild-pt/2026-w47-pt-nl/`。
