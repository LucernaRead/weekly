# GATE LOG — W47 ko-de proof1（独立重跑，2026-11-11）
# 全部命令均由复校员在本人笔记目录 scratch-proof-ko-de1 内独立执行；
# builder 的日志只作参考，未采信其结论。

| # | 门 | 命令/方法 | 结果 | 证据文件 |
|---|---|---|---|---|
| 0 | 开工探针 | `git hash-object -w --stdin` + 笔记目录写盘 | 通过（hash 9daeafb9864cf43055ae93beb0afd6c7d144bfa4） | PROBE.txt |
| 0 | 交付件核对 | `sha256sum` + `stat` 三件 | 与任务书一致：印版 45,682,479 B bcf8f141…fda6；网版 4,037,656 B 10107397…b604；text.md 26,597 B a298889b…9e3e7 | — |
| 1 | U+2019 全扫 | 8 SVG 计数 | 0 | 本 log（D1 行） |
| 2 | U+201C/U+201D 全扫 | 8 SVG 计数 | **不通过：U+201C=2、U+201D=2，皆在 p7-mal.svg**；核心 0 | 见 PROOF-NOTE D1 |
| 3 | 盒标题内宽 | `/usr/bin/python3 boxtitle-ko.py <版目录>` | 8/8 ≤386.5px（最大 345.7px P5 Jugendzahlen） | boxtitle.log |
| 4 | 遮挡审计 | `tools/venv/bin/python tools/occlusion_audit.py svg/` | 0 flags；自检 6 类全触发、干净对照静默 | occlusion.log |
| 5 | freeze baseline | `/usr/bin/python3 tools/freeze.py baseline --build <版目录> --core-svg <版目录>/svg --out <笔记>/freeze` | 8/8 字节一致；核心 SVG 完整性未变 | freeze-baseline.log（freeze/ 目录已按 EDQUOT 指令清理，可重跑复现） |
| 6 | freeze diff | `tools/venv/bin/python tools/freeze.py diff --core-svg core-ko/svg --edition-svg <版>/svg` | 新增 CJK 7，全为 U+3000（页脚空格），每页 1 个、P1 0 个 | freeze-diff.log、freeze-diff.json |
| 7 | p8 extract | `tools/venv/bin/python tools/p8.py extract --p8 svg/p8-siheom.svg --total 150` | noted set = 150/150 | p8-extract.log、p8-de.json |
| 8 | p8 compare | `tools/venv/bin/python tools/p8.py compare --core-p8 core-ko/svg/p8-siheom.svg --edition-p8 <版>/svg/p8-siheom.svg --total 150` | CLEAN，missing=[] extra=0，keydiff=[137, 138]（德语重定向，W46 先例） | p8-compare.log、p8compare-de.json |
| 9 | 150 键独立核对 | 本人脚本 proof-keycheck.py（AST 提 REG + 本人 p8-de.json 比对） | 149 exact + #150 ✓（预期内，与核心相同）= 150/150，BAD 0 | proof-keycheck.py、proof-keycheck.log |
| 10 | 文字层一致 | `pdftotext` 印版/网版 + `cmp` | 各 52,009 字节，逐字节一致 | print.txt、web.txt |
| 11 | P8 最小字号 | PyMuPDF 读印版 P8 全部 span | 9.975pt（≥9.75pt 阈值），361 spans | 本 log |
| 12 | 新鲜重建 | 复制源码到笔记目录，`/usr/bin/python3 run.py` | rc=0；0 FLOW OVERFLOW / 0 HEAD TOO WIDE；TOTAL 150（A2 51 / B1 72 / B2 27；各页 10/18/18/18/18/18/12/38）；8 SVG 与交付件逐字节一致；P2-feature 结束 1531（下限 1540）；P7 teaser 结束 2539.22（页脚 2580，余 40.8px）；P8-keys 结束 2457；范文 169 字 | rebuild.log（rebuild/ 目录已按 EDQUOT 指令清理，可重跑复现） |
| 13 | 目视 | 印版 pdftoppm 100dpi P1–P8 逐版读；网版 P1/P2/P7/P8 读 | 印版 8/8 无溢出/重叠/压页脚；网版与印版一致、无豆腐块、无缺图；P2 购物单盒与日历条无遮挡；P7 无溢出 | pages/p-1.png … p-8.png；webpages/w-1/2/7/8.png |
| 14 | 全文重读 | text.md 全文 + 8 SVG 文本 + 源码 literals | 韩/德全文重读；全部星期日历核验；百分比复算；150 注文人工全读 | PROOF-NOTE.md |
| 15 | ABSTRACT | 读 ABSTRACT.txt | 德语单行 350 B，无 ASCII 双引号，含刊名/目标语/A2–B2/150 题 | — |

## EDQUOT 事件
- 写 proof-keycheck.py 时首次报 Errno 122（`df` 显示盘余 45G，属配额非盘满）。
  按任务指令立即停手，仅删本人笔记目录内可复现中间件（`freeze/` 约 68M、`rebuild/` 约 11M），
  重试一次后写盘恢复。未动他人文件；两目录均可由 freeze.py / run.py 重跑复现。
