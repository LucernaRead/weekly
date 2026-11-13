# D5 重建报告 — pt-zh-tw（2026-11-12）

- 接手状态：上一任 51df9048 只拍了基线快照（已核实与生产逐字节一致）即被运行时重启打断；生产未动（svglib md5 `4228b7e7…`，无 _D5_READER，印/网均为 D5 前旧版）。
- 安装：`apply_variant.py --target pt --reader zh-tw`（mode=cjk；本版 svglib 原无 fix2 块，安装时一并补入；TC 基底）；route_assert latin FAILURES: 0。svglib md5 `4228b7e7…` → `1f776e96…`。
- D5 前：普查拉丁 346 处；基线门禁 occlusion/boxtitle/spill/edge 全 0。印 `42d7d4de…`（24,130,648 B）、网 `8432b628…`（1,820,207 B）。注：KIT §6 旧行所记印/网 SHA 与快照盘上值不符（盘上值见 KIT 文末 D5 节注释；与 pt-ja/pt-ko 同类情况，快照文件为准）。
- 缺陷（3 项，全为 D5 引起，文字不动）：
  1. HEAD TOO WIDE ×1（round 1）：P2-ex `C　COMPLETE COM OS NÚMEROS`，电池头 A–D 统一 25→22（同 core-pt/pt-ja/pt-ko）。
  2. 自查 FAIL ×2（gates-1）——D5 run 拆分测量假象，非内容丢失（与 pt-ja 同类）：页脚检查（`第1版／共8版`）与 P7 quotes 检查（一条含数字的繁體譯文 `總比數定格在 2 比 2。`）只因 D5 把一串源文拆成多 run、`joined()` 在拆分处插空格而失败；其余 7 条金句严格通过，基线 gates.py 事前全过，空白折叠（squashed）比对在 D5 版上页脚 8/8、8 条金句均通过，pdftotext 仍提 `第1版／共8版`。修法：`gates.py` 增 `squashed()`（照 pt-ja/`gates_core.py`），仅用于页脚与 P7 quotes 两项检查。
  3. 无框标题越框（round 1 boxtitle 0、creambox PASS）：繁體副标短，加宽的拉丁头未越界。
- 门禁（gates-2，ALL-GREEN）：run TOTAL 150、0 警告；head_check PASS 0 defects；gates.py 16/16；occlusion 0；p8 extract 150/150、compare CLEAN（keydiff=[137,138]）；freeze baseline 8/8；freeze-diff vs 自身基线新增 CJK 0（vs core-pt 948 = 繁體讲解层本身）；spill 0；boxtitle 0 DEFECT（30 titles，352 body lines）；edge 0/0；creambox PASS 0（机制版 + tools 版双跑，n=382，中位 1.04，粗体 1.057；P8 227→227 行，余量 44.3px）；D5 census PASS；census_quotes 0；印/网文字层各 44,534 字节、逐字节相同（`-layout` 口径各 95,154 字符，字符多重集差 0）。
- 新 SHA：印 `2bbf46445f9e03ee05c6759f7fae7aa75e940d3b44aa3c6176d8fcaf5d90da4a`（13,804,538 B）；网 `2d0e80af74d7d33eaa1cc4e669b9b6471f004649a8d1440400a02db30554e85a`（1,463,493 B，<7MB）。
- text.md 不变（md5 `c168f080013c63f7c430209c42ce92a3`）。
- KIT：§6 已更新 + 文末 D5 节；日志见 `scratch-d5-rebuild-pt/2026-w47-pt-zh-tw/`（freeze-2 build-copy 已清，只留日志与 JSON）。
