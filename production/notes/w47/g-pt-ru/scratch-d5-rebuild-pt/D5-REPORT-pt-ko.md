# D5 重建报告 — pt-ko（2026-11-12）

- 接手状态：上一任 51df9048 已装 D5（svglib md5 `222c918a…`，`_D5_READER="cjk"`，CJK index SC→KR）并重建 run + render，印 PDF 已是 D5 版；约 06:30 EST 被运行时重启打断于 webpdf 中，网 PDF 仍是 D5 前旧版，门禁未跑。
- 安装（上一任）：`apply_variant.py --target pt --reader ko`（mode=cjk；本版 svglib 原无 fix2 块，安装时一并补入）；route_assert latin FAILURES: 0（本任复核：Latin→news、西里尔→sans_noto、fix2 引号→news、CJK→sans）。
- D5 前：普查拉丁 345 处；基线门禁 occlusion/boxtitle/spill/edge 全 0。印 `cdff9fe4…`（17,184,511 B）、网 `f38917a6…`（1,431,218 B）。注：KIT §6 旧行所记印/网 SHA 与快照盘上值不符（盘上值见 KIT 文末 D5 节注释；与 pt-ja 同类情况，快照文件为准）。
- 缺陷（2 项，全为 D5 引起，文字不动）：
  1. HEAD TOO WIDE ×1：P2-ex `C　COMPLETE COM OS NÚMEROS`，电池头 A–D 统一 25→22（同 core-pt/pt-ja）。上一任 round-1 印 PDF 建于修前，已作废。
  2. 自查 FAIL ×1（gates-1）：P7 quotes 检查——D5 run 拆分测量假象，非内容丢失（与 pt-ja/core-pt 同类）：8 条韩文译文全在 SVG 内，strict 子串匹配只因 D5 把 `3일` 等拆成多 run、`joined()` 在拆分处插空格而失败；页脚 8/8 严格通过，无需改动。修法：`gates.py` 增 `squashed()`（照 pt-ja/`gates_core.py`），仅用于 P7 quotes 检查。
  3. 无框标题越框（round 1 boxtitle 0、creambox PASS）：韩文副标短，加宽的拉丁头未越界。
- 门禁（gates-2，ALL-GREEN）：run TOTAL 150、0 警告；head_check PASS 0 defects；gates.py 16/16；occlusion 0；p8 extract 150/150、compare CLEAN（keydiff=[137,138]）；freeze baseline 8/8（venv，Pillow 13——ko 族 Pillow-10 门不适用于 ko 读者版，路径 `2026-w47-pt-ko` 不匹配 `2026-w47-ko-*`，未用系统 python3 例外）；freeze-diff vs 自身基线新增 CJK 0（vs core-pt 3397 = 韩文讲解层本身）；spill 0；boxtitle 0 DEFECT（48 titles，522 body lines）；edge 0/0；creambox PASS 0（机制版 + tools 版双跑，n=389，中位 1.04，粗体 1.057；P8 230→230 行，余量 42.6px）；D5 census PASS；census_quotes 0；印/网文字层各 47,284 字节、逐字节相同（`-layout` 口径各 94,863 字符，字符多重集差 0）。
- 新 SHA：印 `f3104fecd528e9a50d21ae72136a13a4cdd1d0ac29943105ad77a7bc105f4e55`（14,231,397 B）；网 `797ad196553e64af5b9a992905dda169cd49ba776b945fe0d420aaf73f354744`（1,307,288 B，<7MB）。
- text.md 不变（md5 `2cfbfa663d5e714eef660c7f079606f1`）。
- KIT：§6 已更新 + 文末 D5 节；日志见 `scratch-d5-rebuild-pt/2026-w47-pt-ko/`（freeze-2 build-copy 已清，只留日志与 JSON）。
