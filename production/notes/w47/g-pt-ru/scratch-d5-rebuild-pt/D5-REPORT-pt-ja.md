# D5 重建报告 — pt-ja（2026-11-12）

- 安装：`apply_variant.py --target pt --reader ja`（mode=cjk；本版 svglib 原无 fix2 块，安装时一并补入；CJK index SC→JP，kinsoku 已有）；route_assert FAILURES: 0。svglib md5 `f61efb1b…` → `fb698ac3…`。
- D5 前：普查拉丁 347 处；基线门禁 occlusion/boxtitle/spill/edge 全 0。印 `568eb36b…`（24,991,052 B）、网 `b18b3df2…`（1,680,799 B）。注：KIT §6 旧行所记印/网 SHA 与快照盘上值不符（盘上值见 KIT 文末 D5 节注释；与 pt-fr fix2 节同类情况，快照文件为准）。
- 缺陷（3 项，全为 D5 引起，文字不动）：
1. HEAD TOO WIDE ×1：P2-ex `C　COMPLETE COM OS NÚMEROS`，电池头 A–D 统一 25→22（同 core-pt）。
2. 自查 FAIL ×2——D5 run 拆分测量假象，非内容丢失（与 core-pt 同类）：页脚检查（`1ページ（全8ページ）`）与 P7 金句检查（两条含数字的日文译文 `3日間` / `2–2`）只因 D5 把一串源文拆成多 run、joined() 在拆分处插空格而失败；基线 gates.py 事前全过，空白折叠（squashed）比对在 D5 版上页脚 8/8、两金句均通过，pdftotext 仍提 `1ページ（全8ページ）`。修法：`gates.py` 照 `gates_core.py` 增 `squashed()`，仅用于页脚与 P7 金句两项检查。
3. 无框标题越框（round 1 boxtitle 0、creambox PASS）：日文副标短，加宽的拉丁头未越界。
- 门禁（gates-2，ALL-GREEN）：run TOTAL 150、0 警告；gates.py 16/16；occlusion 0；p8 extract 150/150、compare CLEAN（keydiff=[137,138]）；freeze baseline 8/8；freeze-diff vs 自身基线新增 CJK 0；spill 0；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0（n=396，中位 1.04，粗体 1.057；P8 222→222 行，余量 41.0px）；D5 census PASS；census_quotes 0；印/网文字层各 47,917 字节、逐字节相同。
- 新 SHA：印 `9208d231d66cf6e612f367cc1702c8003b5c1bcfd447da414dcedac5d8037768`（15,449,291 B）；网 `a9b4a30929c18cbd949062d1cf79425eb0d1943363251a7f7fbb578da280862b`（1,433,879 B，<7MB）。
- text.md 不变（md5 `83035b2da702df00c6fc63510b38d64d`）。
- KIT：§6 已更新 + 文末 D5 节；日志见 `scratch-d5-rebuild-pt/2026-w47-pt-ja/`。
