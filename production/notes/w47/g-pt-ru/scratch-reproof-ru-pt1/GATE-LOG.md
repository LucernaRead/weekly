# GATE-LOG — 2026-W47 ru-pt 独立复校（re-proof，自跑）

- 版：`production/2026-w47/2026-w47-ru-pt/`；核心对照：`production/2026-w47/core-ru/`（只读对照，未动）
- 复校工作区：`~/workspace/weekly-git/hidden_files/w47/scratch-reproof-ru-pt1/`（独占；脚本、日志、渲染件全在其中）
- 工具 venv：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0，freeze 日志实测；FreeType 2.14.3）
- 判定口径：光栅 = 印 PDF 经 PyMuPDF 以 1950px 宽渲染（1x）与 3900px（2x）；PIL 真墨含前导空白 advance（U+3000 在 23pt = 23px）；下行部用 `anchor="ls"`；阈值 med−60（cutoff 189）为主，med−25/100 交叉核对。`run.py` 重建只在 scratch 副本上跑（OUT 重定向到 scratch 内绝对路径，运行前先核对目标在 scratch 内）；网 PDF 绝不重渲（SHA 不可重现），只比文字层。
- 各门日志文件均在本 scratch 内，文件名见各节。

## §0 身份核对

- 开工三 SHA 磁盘实测，与任务先验值一致：印 `4d726d922b33b6c38ab93e7ed1c47c8913817a5fa4e3bbc59988ff232bec61ed` / 21,205,591 B；网 `f21ed9285a7fcca0a3515e2daa2af2518b0e11fb83752280ea448cf80b7864df` / 3,383,546 B；文 `54d8a766e18daf5f256e91c76765c9e71fefb48c9435e83d28e103bba603d60e` / 65,155 B（修前字节不变）。
- 开工探针：`echo test | git hash-object -w --stdin` 通过 + scratch 内真实写文件通过（`probe.txt`）。

## §1 run.py（`run-rebuild.log`）

- 副本重建（`rebuild/`，删 svg/cards 后跑 run.py）：rc=0，**TOTAL 150**（A2 50 / B1 76 / B2 24；按页 10+18+18+18+18+18+12+38；按类型 Completar 54、Escolha 55、Associação 20、Construção 12、Transformação 4、Tradução 4、Escrita 1——与 fix1 自验分布一致）。
- grep：无 FLOW OVERFLOW、无 HEAD TOO WIDE、无报错。

## §2 SVG 重建（`svg-rebuild-compare.log`）

- 副本重建的 8 张 SVG 与生产 SVG **8/8 字节一致**。

## §3 freeze（`freeze-core.log`、`freeze-diff.log` / `.json`、`freeze-diff-cyrillic.txt`）

- baseline（`freeze.py baseline --build production/2026-w47/core-ru --core-svg production/2026-w47/core-ru/svg`）：rc=0，**8/8 SVG 字节一致**，核心完整性重哈希 OK（核心未被改动）。
- diff（`freeze.py diff --core-svg …/core-ru/svg --edition-svg …/2026-w47-ru-pt/svg`）：rc=0；新增 CJK 仅 U+3000，8 页各 ×1，TOTAL 8；**无新增西里尔串**（`freeze-diff-cyrillic.txt` 为空）；带拉丁的移除仅 masthead + P8 键片段。

## §4 p8 extract / compare（`p8-compare.log` / `.json`、`p8extract-core.json` / `.log`、`p8extract-ed.json` / `.log`、`keys.json`、`key-compare.log`）

- `p8.py extract --p8 …/svg/p8-test.svg --total 150`：核心 150/150，本版 150/150。
- `p8.py compare --core-p8 core-ru/svg/p8-test.svg --edition-p8 …/svg/p8-test.svg --total 150`：rc=0，**status CLEAN**，missing=[]，extra_count=0，uncertain=[]，**keydiff=[137, 138, 139, 140]**（四条 E 节 RU→PT 翻译键，手验译文正确，见 PROOF-NOTE §3）。
- P8 印出键 vs text.md Answers §：150 行连续 1–150；**149/150 一致**，唯一分歧 Q150（P8 印 `✓`，text.md 为开放题说明——与核心一致的已知例外）。

## §5 occlusion 真实审计（`occlusion.log` / `.json`）

- 工具内置阳性对照自检先行通过（6 类均触发）；`occlusion_audit.py …/svg --json occlusion.json`：**42 flags，全部 TEXTX；COVER 0 / LINEX 0 / FOOTER 0 / EDGE 0 / BOXTITLE 0**；核心同为 42；vs 核心 NEW 3。
- 独立裁决（`adjudicate_textx.py`、`adjudicate_textx_2x.py`；`textx-adjudication.log`、`.json`，1x + 2x 光栅逐条测共享墨列，不照抄前人结论）：**42/42 假阳性**。全部零共享墨列；1x 间隙 ≥0，2x 间隙 ≥0（25 例间隙 0 = 零空格标点相邻，如 `» , . : ; ! ?` 紧贴词尾，正常排版）；NEW 3 例间隙大（1x 50/50/29px；2x 100/101/57）。机理已证：PIL `getbbox('　LÍNGUA')` 返回 left=0（前导 U+3000 贡献空 bbox），而 46pt 下真墨始于 ~50px 右——审计高估左缘。8 张裁图（`crop-p*-*.png`）目检均为正常排版。

## §6 横向溢出三法交叉验证（修后，交付印 PDF 为准）

| 缺陷 | 光栅（MuPDF 1950px） | PIL 真墨（SVG 元素） | PDF span advance | 要求 | 判定 |
|---|---|---|---|---|---|
| D1 P1 标题 | **1845（+17）** | 1842.5（+19.5） | 1844.4（+17.6） | 离 1862 ≥ +5 | 通过 |
| D2 P1 桥接行 | **1855（+7）** | 1849.5（+12.5） | 1857.0（+5.0） | 离 1862 ≥ +5 | 通过 |
| D3 P2 | **1854（+8）** | 1850.3（+11.7） | 1856.3（+5.7） | 离 1862 ≥ +5 | 通过 |
| D3 P3 | **1854（+8）** | 1850.3（+11.7） | 1856.3（+5.7） | 离 1862 ≥ +5 | 通过 |
| D3 P4 | **1854（+8）** | 1850.3（+11.7） | 1856.3（+5.7） | 离 1862 ≥ +5 | 通过 |
| D3 P5 | **1854（+8）** | 1850.3（+11.7） | 1856.3（+5.7） | 离 1862 ≥ +5 | 通过 |
| D3 P6 | **1854（+8）** | 1850.3（+11.7） | 1856.3（+5.7） | 离 1862 ≥ +5 | 通过 |

- 三法一致通过；网 PDF 的 D1/D3 span 与印版相同（D1 1846.2；D3 尾段 1856.3 ×5 页）。
- 证据裁图：`crop-p1-palavra-fix1.png` 类比裁图在本 scratch 的 `edge-measure.log` / `d3-measure.log` 对应测量中；D1/D2/D3 行尾均距右缘留白清晰。
- D5 遗留越界（只记录，不修；`d5-raster.log`、`d5-threshold.log`、`scan-d5-boxtitle.log`、`scan-d5-advance.log`）：P8 副标题（基线 1302，SVG x=1239.7，19.5pt）光栅 **1864**（印 + 网，阈值 15/25/40/60 一致；2x 1864.5），PIL ink_box 1861.95，advance 1862.03。1864 列像素灰度 140–192（抗锯齿边缘），thr=100（cutoff 149）仍计入，仅在更严 cutoff（<140）下消失——与 fix1 的 1863 差 1px 属阈值带差异；同行同量级，未恶化。裁图 `crop-p8-subtitle.png` 目检。
- P1 `O QUE DIZEM OS MEDIA` 标题（同类 ±1px 观察项，`scan-d5-boxtitle.log`）：PIL 1863.65；光栅 1862（thr-60）/ 1863（thr-25）/ 1863.0（2x）；裁图 `crop-p1-mediabox-title.png` 目检——末尾 `A` 完整可见，未截断；边界是奶油填色边缘，无描绘的线。非缺陷。

## §7 kicker（`kicker.log`、`kicker-measure.log`、`kicker-raster.log`、`crop-p1-kicker.png`）

- `content12.py:18`，P1，16pt，9 个双空格。字隙 1x **[9, 4, 10, 7, 7, 8, 9, 9, 10]**；2x **[8.5, 4.0, 9.5, 6.5, 7.5, 7.0, 9.5, 8.5, 9.5]**；**最小 4.0px ≥ 4**，通过。裁图目检正常间距。
- 注：KIT §5 所载 `[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]`（最小 5.9）在我 1x 与 2x 两套测量下均不重现；"最小 ≥ 4px"的判定本身成立（见 PROOF-NOTE §6 (b)-1 备注）。

## §8 印/网文字层一致 + P8 字号（`textlayers/`、`text-diff.log`、`p8-font.log`）

- `pdftotext` 逐页：每页字符多重集 **完全相同（8/8 页）**；字节数相等（6230/6603/5356/6462/5730/5616/6906/15424）；去空白字符 31,105（各）。
- 网 PDF `pdftotext` 字节 > 0（58,327；单文件 3,383,546 B < 7 MB）。
- P8 最小字号：印 **9.75pt**，网 **9.75pt**（386 spans）——符合 SOP §1.1 下限 9.75pt。

## §9 check_core（`check-core.log`、`check-core-core.log`）

- 本版 `check_core.py .`：rc=0，golden BAD 0，gloss fails 0；1 孤儿行首（P7 y553 `”».`）与 1 同基线碰撞（P1 y1712 `чёрная`）。
- 核心对照跑确认：两处在核心中**完全相同存在**（核心有 5 孤儿，含 y553）——继承的良性项。

## §10 盒标题 32（`boxtitle-32b.log` / `.json`、`creambox-32.log` / `.json`、`boxtitle-32.log`）

- 内容盒 32（9 绿带 + 23 奶油，基线分组 v2）：全部间隙为正；最紧 **8.3px**（P6 `ЗА И ПРОТИВ / PRÓS E CONTRAS` 右侧）。
- 规范 creambox-32（全部 `#f0eee5` 矩形 + 所含文字）：最紧 **−1.65px PIL**（P1 `O QUE DIZEM OS MEDIA` 标题，见 §6 观察项）；次紧 O3 P2 盒底 **+0.52px PIL / 1px 光栅**（最低墨行 1158，盒底 1159.0）——在内，与 pt1（1158.98/+0.02）、pt2（1159.00/+0.00）在方法噪声内一致；裁图 `crop-p2-boxbottom.png` 目检干净。

## §11 D7 网 PDF 斜体（`d7` 相关证据见 §1 引用与裁图）

- 网 P1 内嵌 `LucernaNotoSerif-Italic` + `LucernaNewsreader-Italic`；`«чёрная пятница»` span 为 `LucernaNotoSerif-Italic` 16.12pt（印版 `NotoSerif-MediumItalic` 16.12pt，同字号）。
- 文字层：`чёрная пятница»` 贴合 ×4（印/网各），脱离 `чёрная пятница »` ×0。
- 印/网裁图 `crop-p1-italic-print.png` / `crop-p1-italic-web.png` **字节相同**，斜体 + 闭引号贴合均目检落地。

## §12 内容手验（`p4-table.log`、`match-groups.log`、`match-groups2.log`）

- text.md L1–838 全读，Q1–150 逐题手验：**全部正确**（PROOF-NOTE §3）。
- P4 赛果表（P4 SVG 按基线重组）：8 场比分，进球 1+3+1+6+2+3+4+1 = **21**（Q54 2:0、Q59 2:1、Q53 2:2、Q55 1:0、Q64 2:1 均与表一致）；6.11 五、7.11 六、8.11 日；15 轮 8 场 20–22.11 齐全。
- 五组配对 SVG 选项表核对 20/20（P2 D、P3 C、P4 C、P5 C、P8 F）；G 对话 P8 SVG 全文读，Q145–149 键 A/B/B/A/B 均合语境。
- Q150 范文我自数 **97 词**（brief 80–100）。
- 日期星期（`date -d`，America/Toronto）：2026-11-06 五、07 六、08 日、12 四、13 五、14 六、16 一、17 二、18 三、19 四、20 五、22 日、27 五、29 日、30 一——与刊内全部日期表述一致。
- map D1 四锚点：P6 图题 + `УЧЕБНЫЕ ДАННЫЕ`（`content56.py:158`，text.md:459）；P6 免责声明（`content56.py:159`，印/网 P6 文字层 L117；早先 grep 漏查系 pdftotext 分段 `редакциидля`）；P7 副标题（`content7.py:12`，text.md:504）；P8 副标题（`content8.py:12`，text.md:596）——印 + 网均落地。

## §13 KIT 身份号核对（缺陷 (b)-1 的证据）

- 直接 grep `WEEKLY-KIT.md`（L53–54、L56、L77、L79、L83）：
  - §5 L53 印 PDF：`59f01012f5c6…` / 21,205,597 B —— 盘上 `4d726d92…` / 21,205,591 B。
  - §5 L54 网 PDF：`485a27b6be19…` / 3,383,529 B —— 盘上 `f21ed928…` / 3,383,546 B。
  - §5 L56：pdftotext 58,200 字节；31,041 字符（各）——实测 58,327 字节；31,105 字符（各；re-fanout 值为 31,107，2 字为抽取方法差）。
  - §5 L77 重复 31,041；§1.1 L79 网 PDF 3,344,677 B（proof1 的网 PDF 大小）——实测 3,383,546 B。
  - §5 L83 引用 `hidden_files/w47/scratch-refanout-ru/records/pt/RECORD.md`——本 clone 内 `find` 无此目录，引用悬空。
- 成因：KIT 记的是 fix1 修前 re-fanout 构建；fix1 重建了 PDF（其 GATE-LOG §9 给出新 SHA，与本复校盘上实测一致），但 GATE-LOG §8 明文列出 `WEEKLY-KIT.md` 未动。Docs-only：无内容/门禁/读者可见影响；修复 = 只改 KIT 里的 5 个数字 + 1 条引用。

## §14 生产零写入核对（`opening-snapshot.sha256`、`closing-snapshot.sha256`）

- 开工 44 个生产文件快照与收工重哈希对比：**44/44 哈希完全相同**。未改任何生产文件，未 commit，未 push。
- `git status`：`production/2026-w47/2026-w47-ru-pt/` 为未追踪目录（整版未入仓状态如前，未动）。

## §15 结论

- **(b)**：唯一缺陷 (b)-1（KIT §5/§7 身份号过期，docs-only；修复只需改 KIT 数字，无需重建/重校内容）。
- 其余：R2-D1/D2/D3 全部通过；map D1、kicker、Q20、Q25、D7 斜体全部落地；run 150、SVG 重建 8/8、freeze 8/8、p8 CLEAN [137,138,139,140]、occlusion 42 TEXTX 全假阳性、印/网文字层逐页一致、P8 最小字号 9.75pt、150 题逐题手验全对；D5 仍为记录项（1864，未恶化）。
