# D5 重建报告 — pt-ru（2026-11-12）

- 安装：`apply_variant.py --target pt --reader ru`（mode ru；本版 svglib 原无 fix2 块，安装时一并补入）；route_assert FAILURES: 0。svglib md5 `c52139e5…` → `9142f7c2…`。
- D5 前：普查拉丁 357 处 + 西里尔 255 处；基线门禁 occlusion/boxtitle/spill/edge 全 0。印 `a3b022bc…`（12,916,087 B）、网 `0cdf7167…`（1,188,302 B）。
- 缺陷（1 项，D5 引起，文字不动）：occlusion COVER ×2（P7）：第 4 行金句俄文译文（`Без памяти нет будущего。`、`Проверь транспорт…`，基线 y=2409.67）一半被后绘的 `A PRÓXIMA SEMANA` 预告框（顶 y=2404）盖住，墨水被盖 52%。修法：`content7.py` 金句行距 80→74 + 句→译文间距 20→16（第 4 行译文基线→2387.67，墨水底≈2393.5，离框顶约 10.5px）。
- 无 HEAD TOO WIDE、无框标题越框：ru 模式用 Noto Sans（粗体西里尔中位 0.956，反变窄），P2-ex 电池头与 P1 框标题未越界。
- 门禁（gates-2，ALL-GREEN）：run TOTAL 150、0 警告；gates.py 16/16；occlusion 0；p8 extract 150/150、compare CLEAN（keydiff=[137,138]）；freeze baseline 8/8；freeze-diff vs 自身基线新增 CJK 0；spill 0；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0（n=416，中位 1.006，粗体 0.956；P8 253→253 行，余量 46.3px）；D5 census PASS（Noto Sans 元素 783，ru 路由真实触发）；census_quotes 0；印/网文字层各 54,970 字节、逐字节相同（`-layout` 口径差仅 3 空格）。
- 新 SHA：印 `6208be63e9175fd46c6fbf3b91bd4d118552752da267cfe6309ff8f11f58916b`（12,694,224 B）；网 `c3b7eae275d7fda1d62cd731e2591cef5e872b755c1fe4340a9514640089ec60`（1,311,813 B，<7MB）。
- text.md 不变（md5 `0db690a29850aef6c3e18e7134398d48`）。
- KIT：§6 已更新 + 文末 D5 节；日志见 `scratch-d5-rebuild-pt/2026-w47-pt-ru/`。
