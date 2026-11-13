# GATE-LOG — 2026-w47-ja-pt 第一轮返修（fix1）门禁记录

- 构建解释器：`tools/venv/bin/python`（与构建相同，Python 3.12.3）
- 终版构建：run3（修后）/ run4（freeze 重跑）；SVG 指纹 `sha-fix1-run3.txt` /
  `sha-fix1-run4.txt`；双 PDF 由 run3 的 SVG 渲染（render-fix1b.log /
  webpdf-fix1b.log）。
- 证据目录：本目录（`scratch-ja-pt-fix1/`）——全部日志、JSON、裁图、8 页重渲。

## 1. 构建（run.py / render.py / webpdf.py / export）

| 门 | 结果 |
|---|---|
| run.py run1（D1+罗马字修后） | rc 0，FLOW OVERFLOW / HEAD TOO WIDE 0 次；TOTAL 150 |
| run.py run2（freeze） | rc 0，0 溢出；SVG sha 与 run1 逐字节相同（`sha-fix1-run1/2.txt`） |
| run.py run3（标题修后） | rc 0，0 溢出；TOTAL 150 |
| run.py run4（freeze） | rc 0，0 溢出；SVG sha 与 run3 **8/8 相同**（FREEZE 通过） |
| 登记表 | A2 48 / B1 73 / B2 29；分版 10/18/18/18/18/18/12/38；类型 completamento 50 / escolha múltipla 51 / relacionar 12 / construção de frases 8 / verdadeiro ou falso 11 / cloze 13 / tradução 4 / escrita 1 |
| render.py | rc 0，8 cards PNG + 印刷 PDF |
| webpdf.py | rc 0；网版 4,485,030 字节（< 7 MB） |
| export-textmd-pt.py | 重建版（原脚本丢失，见 FIX-LOG）；修前文件逐字节复现验证通过；修后导出 46,696 字节 / 1375 行；与修前 diff 恰为 8 处改动 |

## 2. 机械门（全套，终版 SVG/PDF）

| 门 | 工具 / 命令 | 结果 |
|---|---|---|
| 遮挡审计 | `tools/occlusion_audit.py svg/` | **0 flags**；自检 OK，6 类（COVER/LINEX/FOOTER/EDGE/TEXTX/BOXTITLE）植入对照全触发、干净对照静默（`occlusion-fix1b.log`） |
| 浅色框溢出重扫 | `box-overflow-scan.py`（本目录，PIL 实测墨迹，1px 容差） | **0 处真溢出**（8 页全扫；`box-overflow-fix1b.log`）。TOL=0 时另见 3 处 0.29–0.92px `envia-nas.` 框底触线，首轮已裁定量测噪声（O4），核心版同位一致 |
| P8 extract | `tools/p8.py extract --total 150` | **150/150**（`p8-fix1b.json`） |
| P8 compare | `tools/p8.py compare` vs core-ja P8 | **CLEAN**；missing=[] extra_count=0 uncertain=[]；**keydiff 恰为 [137, 138, 139, 140]**（`p8compare-fix1b.json`） |
| 150 键逐题复核 | core/p8 JSON vs fix1 p8 JSON 全键比对 | noted set 150/150 一致；键差异仅 [137, 138, 139, 140]（E 组译键，预期） |
| 文字层双版一致 | `pdftotext` 印版 vs 网版 | **逐字节相同，46,969 B**（`print.txt` / `web.txt`）；PyMuPDF 抽取亦一致（45,737 B） |
| 双 PDF 规格 | PyMuPDF | 各 8 页，1462.5 × 2025 pt |
| P8 最小字号 | PyMuPDF p.8 spans | **9.975pt**（162 spans，答案）；次档 10.35pt（79 spans，题干）≥ 9.75pt 底线 |
| U+2019 全扫 | SVG + .text.md + content*.py | **0**（U+0027 仅见于 .py 源码字符串字面量，非印刷文本） |
| §1.1 grep | 终版 SVG | 纸色 `#fbfaf6` 每页 1×；旧 `#f7f1e2` 0×；`·` 0×；禁用色 0×；刊头 196px 1×；页脚行 `Página N de 8` 每页 1×；VOL.4 10× / VOL.5 3×（text.md） |
| 力士拼写 grep | SVG + .text.md + 源码（ live 内容） | `Fujiryūga` / `Umi-no-umi` **0 处**；`Fujiryōga` 5 处 + `Chura-no-umi` 1 处（P8 注） |
| 翻译表 grep（补记 F6） | goals 侧 `scratch-fanout-ja/map-pt.json` + `tm-pt.json` + `tm2-pt.json` | 修正后 `Fujiryūga` / `Umi-no-umi` **0 处**；`Fujiryōga` 4 处 + `Chura-no-umi` 1 处（map），`Chura-no-umi` 各 1 处（tm/tm2）；JSON 改后仍合法；词条 `祈求生意兴隆的竹耙` 值已改为 F3 缩短形 |
| 原版导出脚本验证（补记 F6） | goals 侧原版 `export-textmd-pt.py` 重导 | 与交付的 text.md **逐字节相同**（46,696 字节） |

## 3. 目视（从终版印刷 PDF 重渲，`render-print/p-1..8.png`）

| 页 | 结果 |
|---|---|
| P1 | 干净。数字框标题 `数字で見る今週　A semana em números` 已入框（2× 裁图 `p1-numbox-fixed.png`） |
| P2 | 干净。四词框释义均为单行框内；熊手框 `ancinho de bambu para bons negócios` 单行（2× 裁图 `p2-words-fixed.png`） |
| P3 | 干净（中部留白为核心既有版式，首轮 O5） |
| P4 | 干净（栏顶 `5) でお知らせします。` 跨栏续接为核心既有形式，首轮 O7） |
| P5 | 干净 |
| P6 | 干净；图表 38/24/22/16 = 100% |
| P7 | 干净。框架框标题 `今週のフレーム　Estrutura da semana` 已入框（2× 裁图 `p7-framebox-fixed.png`）；披露 5 行未压页脚 |
| P8 | 干净。答案区：注 48 `Chura-no-umi …`、49/54/63/111/116 `Fujiryōga …` 均正确；137–140 葡文答案；键流末行距页脚余量充足 |

## 4. 终版双 PDF

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-JA-PT.pdf` | 29,103,009 | `9591f16cb82a2e2534f141febc1232632ee6cf02eefa64e84e9b74cb3601b8be` |
| `Lucerna-VOL4-JA-PT-web.pdf` | 4,485,030 | `f0cdce302756b0bf118dfaa432af9dfcaf9d66b9d17056adbeb688f26258645f` |

## 5. 说明

- fix1 期间发现并修复的标题溢出（F5）不在首轮缺陷清单内，但与 D1 同类、
  同为零缺陷门槛下的真溢出，修前/修后 2× 裁图均已存本目录
 （`*BEFORE.png` / `*fixed.png`）；姊妹版同类问题不在本任务范围内，未动。
- 渲染过程一则注记：`pdftoppm` 首次写 p-7.png 时报了一次写入失败
  （盘 45G 空闲，非配额问题），重跑 7–8 页即成功；终版 8 页 PNG 均已验。
