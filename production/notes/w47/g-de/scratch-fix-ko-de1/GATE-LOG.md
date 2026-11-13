# GATE LOG — W47 ko-de fix1（builder 自查，2026-11-11）
# 全部命令均在本笔记目录 scratch-fix-ko-de1 内执行；proof1 的日志只作对照，未采信其结论。
# 修后成品：印版 45,682,367 B c19fe6c1…f38；网版 4,035,061 B 375f0cf7…878；text.md 26,603 B a7641374…ca0d1

| # | 门 | 命令/方法 | 结果 | 证据文件 |
|---|---|---|---|---|
| 0 | 开工探针 | `git hash-object -w --stdin` + 笔记目录写盘 | 通过（hash 9daeafb9864cf43055ae93beb0afd6c7d144bfa4） | PROBE.txt |
| 0 | 交付件核对 | `sha256sum` + `stat` 三件 + 8 SVG 预修哈希 | 与任务书一致（印版 45,682,479 B bcf8f141…fda6；网版 4,037,656 B 10107397…b604；text.md 26,597 B a298889b…9e3e7）；SVG 与 KIT run 2 哈希逐个一致 | sha-svg-pre.txt |
| 0 | D1 预检 | 8 SVG 计数（Python） | U+201C=2、U+201D=2（全在 p7-mal.svg）、U+2019=0；核心 0/0/0 | FIX-LOG.md |
| 0 | 改前 wrap 实测 | core `svglib.wrap`（`/usr/bin/python3`）：wcn（378.5px/20pt sans）新旧各 2 行；D5 注文含 `Hinweis — ` 前缀（386.5px/20.5pt sans）新旧各 3 行 | 行数不变，版式不动 | FIX-LOG.md |
| 0 | textmd 复现预检 | 重建前跑 textmd.py 写 /tmp，`cmp` 旧 text.md | 逐字节一致，证明导出命令与参数正确 | （/tmp 文件已删） |
| 1 | 弯引号全扫（修后） | 8 SVG 计数 | **0 / 0 / 0**（U+201C/U+201D/U+2019） | sweep-fix1.log |
| 2 | 新鲜重建 | `/usr/bin/python3 run.py`（原地） | rc=0；0 FLOW OVERFLOW / 0 HEAD TOO WIDE；TOTAL 150（A2 51 / B1 72 / B2 27；各页 10/18/18/18/18/18/12/38）；P2-feature 1531；P7 teaser 2539.22；P8-keys 2457；范文 169 字 | build-fix1.log |
| 3 | SVG 变化面 | 修后 8 SVG sha256 与修前 diff | 仅 P2、P7 变化；其余 6 张逐字节一致 | sha-svg-pre.txt、sha-svg-fix1.txt |
| 4 | 印版渲染 | `tools/venv/bin/python render.py` | 8 PNG + 印版 PDF 45,682,367 B | render-fix1.log |
| 5 | 网版构建 | `tools/venv/bin/python tools/webpdf.py svg Lucerna-VOL4-KO-DE-web.pdf` | 8 页，540 distinct chars，52,015 text bytes；4,035,061 B（< 7 MB） | webpdf-fix1.log |
| 6 | text.md 重导 | `/usr/bin/python3 textmd.py` | 332 items；与旧版 diff 仅第 157 行（D5 注文） | textmd-fix1.log、text.md-pre |
| 7 | freeze baseline | `/usr/bin/python3 tools/freeze.py baseline --build <版> --core-svg <版>/svg --out /tmp/fix-ko-de1-freeze`（EDQUOT 后重试，out 在 /tmp，用后已删） | **8/8 字节一致**（repointed: none；核心 SVG 完整性未变） | freeze-baseline-fix1.log |
| 8 | freeze diff | `tools/venv/bin/python tools/freeze.py diff --core-svg core-ko/svg --edition-svg <版>/svg` | TOTAL added CJK **16**（见下裁定）；p2/p3/p5/p6/p8 与 proof1 相同（各 1×U+3000）；p1/p4/p7 之差来自核心线同期修好的 D2/D3/D4（见裁定） | freeze-diff-fix1.log |
| 9 | p8 extract | `tools/venv/bin/python tools/p8.py extract --p8 svg/p8-siheom.svg --total 150` | noted set = **150/150** | p8-extract-fix1.log |
| 10 | p8 compare | `tools/venv/bin/python tools/p8.py compare --core-p8 core-ko/svg/p8-siheom.svg --edition-p8 <版>/svg/p8-siheom.svg --total 150` | **CLEAN**，missing=[] extra=0，keydiff=[137, 138]（与 run 2 相同，德语重定向） | p8-compare-fix1.log |
| 11 | 遮挡审计 | `tools/venv/bin/python tools/occlusion_audit.py svg/` | **0 flags**；自检 6 类全触发、干净对照静默 | occlusion-fix1.log |
| 12 | 文字层一致 | `pdftotext` 印版/网版 + `cmp` | 各 **52,015 字节，逐字节一致**（+6 = Ernteaussichten − die Ernte） | print-fix1.txt、web-fix1.txt |
| 13 | P8 最小字号 | PyMuPDF（venv）读印版 P8 全部 span | **9.975pt**（≥9.75pt 阈值），与 run 2 相同 | 本 log（命令见 FIX-LOG 对应行） |
| 14 | 盒标题内宽 | `/usr/bin/python3 boxtitle-ko.py <版目录>` | **8/8 ≤386.5px**（最大 345.7px P5 Jugendzahlen） | boxtitle-fix1.log |
| 15 | PDF 文字层抽查 | PyMuPDF 读印/网版文字 | P2 `Ernteaussichten` ×1、`die Ernte` ×0；P7 `「nach ~」` 在、弯引号 0 | 本 log |
| 16 | 目视 | 新印版 pdftoppm 100dpi P2、P7 逐版读 | P2 注文盒 3 行完整、无溢出/压线；P7 框架行已为「」且与韩文行、Fehlerklinik 框体例一致、无溢出、无豆腐块；其余 6 页 SVG 未变，不重读 | p2-fix1-2.png、p7-fix1-7.png |

## Freeze-diff 新增 CJK 16 个逐字裁定（对当前盘上新核心）
- U+3000 ×7（p2/p3/p4/p5/p6/p7/p8 各 1）：页脚空格，与 run 2 / proof1 相同，已接受。
- P1 예 ×1、디 ×1：D2 冻结文本——本版仍为旧核心句「우승한 팀은 어디예요?」（ex 10），
  新核心已改为「어느 팀이에요?」。非本轮引入，待重扩消除。
- P4 시 ×1、리 ×1、즈 ×1、예 ×1、디 ×1：D3 冻结文本「한국시리즈 시리즈 전적」（ex 48，
  시/리/즈）+ D2 冻结文本「어디예요」（ex 47，예/디）。新核心两句均已改。非本轮引入，待重扩消除。
- P7 후 ×2：D4 冻结文本——本版框架例句 wt 仍引旧金句「수능 후에 김치의 날이 와요」，
  新核心 wt 与 #7 均已改为「수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요」（无 후）。
  本轮 D1 只换了 wcn 的引号字符，未增韩字。非本轮引入，待重扩消除。
- 本轮引入的新增 CJK：0（「」U+300C/U+300D 在版内 CJK 总数 +4，但核心同款亦有，multiset 差分为 0，未计入新增）。
- 结论：16 个中 7 个为已知接受项、9 个为核心已修、待重扩的冻结滞后项；无本轮新引入的韩文。

## EDQUOT 事件
- 写 freeze-baseline-fix1.log 时首次报 Errno 122（`df` 显示盘余 45G，属配额非盘满）。
  按任务指令立即停手，仅删本人笔记目录内可复现中间件（`freeze/` 68M，freeze.py 可重跑复现）
  与 0 字节残日志，重试一次（--out 改放 /tmp，用后即删）后写盘恢复，基线 8/8。
  未动他人文件；重试前 freeze/ 内只有未完成的 build-copy 与空 svg/，无可用结论。
