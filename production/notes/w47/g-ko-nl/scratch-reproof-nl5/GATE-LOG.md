# GATE-LOG — core-nl fix5 独立 re-proof（2026-11-11）

复校员独立重跑记录。每项均附：命令/方法、源日志文件（`scratch-reproof-nl5/` 内）、实测值、结论。
修复者日志（`scratch-fix-nl5b/`）只作比对参考。所有时间均为本轮实测。

## 0. 前置探针与 SHA

| 项 | 命令/方法 | 源 | 实测值 | 结论 |
|---|---|---|---|---|
| /dev/null | `ls -l /dev/null` | — | 存在（crw-rw-rw-） | PASS |
| git hash-object -w | 仓库内 `git hash-object -w --stdin < /dev/null` | — | rc=0 | PASS |
| scratch 可写 | 新建 `scratch-reproof-nl5/probe.txt` | `probe.txt` | 写入成功 | PASS |
| 印 SHA | `sha256sum De-Lucerna-VOL4.pdf` | — | `b7d4a9cd…7ce47` / 25,955,578 B | 与任务书一致 ✓ |
| 网 SHA | `sha256sum De-Lucerna-VOL4-web.pdf` | — | `5a47449c…0404c` / 2,104,000 B | 与任务书一致 ✓ |
| 文 SHA | `sha256sum 2026-w47-nl-zh-cn.text.md` | — | `0b97a48d…7050c` / 44,093 B | 与任务书一致 ✓ |
| SVG 范围 | `sha256sum svg/*.svg` vs fix5b after / fix4 before | `svg-hashes-prebuild.txt` / `svg-hashes-fix5b.txt` | = fix5b after 全 8；vs fix4 仅 p4 变 | PASS |
| 源码 diff | `git diff` + 行号核对 | — | content34.py 仅 :130–134 一 hunk（89）；:37（62+64）未动 | PASS |
| FIX-LOG/KIT | 读核心内 FIX-LOG 第 5 轮与 WEEKLY-KIT §16 | 核心内文件 | §16 第 232 行三件 SHA 与实测一致 | PASS |

## 1. 构建与重现

| 门禁 | 命令/方法 | 源日志 | 实测值 | 结论 |
|---|---|---|---|---|
| run.py | `tools/venv/bin/python run.py`（原地） | `build-reproof.log` | rc=0；TOTAL 150；页 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31；0 FLOW OVERFLOW / HEAD TOO WIDE；P4 col3 ends 1229.6、P3 col3 ends 1106.6、P6 chart ends 665、P6 col3 ends 1000.0、P7 col3 ends 1898.0 | PASS |
| SVG 重建一致 | 重跑前后哈希比对 | `svg-hashes-prebuild.txt` / `svg-hashes-postbuild.txt` | 8/8 字节一致 | PASS |
| render.py | `tools/venv/bin/python render.py`（原地；印 PDF 字节可复现） | `render-reproof.log` | rc=0；8 cards；印 PDF 25,955,578 B，SHA `b7d4a9cd…7ce47` 与交付一致 | PASS |
| text.md 未被构建改动 | 重跑后 `sha256sum` | — | `0b97a48d…7050c` 不变 | PASS |
| freeze baseline | `tools/freeze.py baseline --build <真核心目录> --core-svg <真核心svg目录> --out scratch-reproof-nl5/freeze` | `freeze.log` | rc=0；**8/8 MATCH**；core integrity：发货 SVG 未变 | PASS |
| text.md 重导出 | 复制 fix4 `export47.py`+stub 至 scratch 运行（输出写回生产路径） | `export-reproof.log` | rc=0；44,093 B；SHA 与交付件一致；432 行；142+2+8=150；8 金句；6 gloss | PASS |

## 2. D11 三重实测（fix5 唯一改动）

| 门禁 | 命令/方法 | 源日志 | 实测值 | 结论 |
|---|---|---|---|---|
| SVG 几何 | Python 解析 `<text>`/`<rect>`（不用 grep 扫 SVG） | `inkprobe-d11-reproof5.log` | 盒 (1439.5, 591.6, 422.5, 638.0)，盒底 1229.6；末行 `18:45 uur.` 基线 1209.49；基线余量 **+20.11px**；首基线 680.60，距盒顶 **89.00** | PASS |
| 真墨 cards 1× | `inkprobe-d11-reproof5.py`（cards/p4-sport.png） | 同上 | 最低真墨行 1209.00，真墨余量 **+20.60px**；盒底以下 7px 带非纸像素 **0** | PASS |
| 真墨印 PDF 150dpi | 同脚本（render/p-4.png，scale 1.5625） | 同上 | 最低真墨行 1209.12，真墨余量 **+20.48px**；7px 带非纸像素 **0** | PASS |
| 目视裁图 | 150dpi 裁图 | `render/crop-p4-programma.png` | 5 条事实全在盒内，`18:45 uur.` 下有清晰奶油边距 | PASS |
| P3 同形盒交叉核对 | SVG 解析 | （exec 输出） | 盒底 1106.60，末基线 1090.40，余量 **+16.20px** | PASS |
| 公式复算 | `89 + 487 + 62 = 638.0`；行数 3/3/3/2/3=14 | — | 与 SVG 一致 | PASS |

## 3. D8/D9/D10 回归

| 门禁 | 命令/方法 | 源日志 | 实测值 | 结论 |
|---|---|---|---|---|
| D8 目标行 | SVG 检索 p6 | `orphan-sweep-reproof5.log` | 行 1 `…非真实调查。`（635.02）、行 2 `问题：…`（659.44）；2 行 | PASS |
| D8 宽度带 | `width_scan_reproof.py`（生产 `wrap()`） | `width-scan-reproof5.log` | 目标行带 388.5–425.0；397.5 在带内；行 1 末端 1850.0，距右缘 12px | PASS |
| D8 裁图 | 150dpi 裁图 | `render/crop-p6-d8.png` | 行 1 以 。 结尾，行 2 行首为“问” | PASS |
| D9 Q140 | `p8compare_reproof.py` 四源 | `p8-compare-reproof5.json` / `.log` | #140 MATCH；键 = `Ik maak een surprise met een kort gedicht.` | PASS |
| D9 裁图 | 150dpi 裁图（fitz 定位 Q140） | `render/crop-p8-q140.png` | `140. Ik maak een surprise met een kort gedicht. — surprise 是固定搭配` 已印出 | PASS |
| D10 目标行 | SVG 检索 p7 | `orphan-sweep-reproof5.log` | 行 1 `…最佳作文，`（1754.27）、行 2 `刊登示例信，…`（1782.67）；2 行 | PASS |
| D10 宽度带 | 同上 | `width-scan-reproof5.log` | 目标行带 380.5–430.0（窄带 338.5–360.0）；390.5 在带内；行 1 末端 1841.6，距右缘 20px | PASS |
| D10 裁图 | 150dpi 裁图 | `render/crop-p7-d10.png` | 行 1 以 ， 结尾，行 2 行首为“刊” | PASS |
| SVG 字节一致 | p6/p7/p8 vs fix4 | `svg-hashes-prebuild.txt` | 字节一致，三处按构造不可能回归 | PASS |

## 4. 孤儿标点 sweep（独立自写脚本，三种方法）

| 门禁 | 命令/方法 | 源日志 | 实测值 | 结论 |
|---|---|---|---|---|
| (a) 独占一行 。 | `orphan_sweep_reproof.py`：xml 解析，按基线分组、x 间隙 >60px 分段；PIL 实测推进量 | `orphan-sweep-reproof5.log` / `orphan-sweep-reproof5.json` | 1421 重建行；(a)=**0**（逐页 0） | PASS |
| (a) 同上 | 同脚本，svglib `text_w` 推进量第二遍 | 同上 | (a)=**0** | PASS |
| (b) 行首标点 | 同上两遍（行首 。/，/、/：/；/！/？/”/’/」/』/）/》/»） | 同上 | (b)=**0** / **0**（逐页 0） | PASS |
| 蛮力复核 | 所有以闭标点开头的 `<text>` 元， adjudicate 是否基线最左元 | 同上 | 12 片段（P1 `：`1、P8 `：`4、`）`7），最左元 **0** | PASS |

## 5. P8 与键

| 门禁 | 命令/方法 | 源日志 | 实测值 | 结论 |
|---|---|---|---|---|
| p8 extract | `tools/p8.py extract --p8 svg/p8-toets.svg --total 150 --json p8-extract.json` | `p8-reproof5.log` / `p8-extract.json` | noted set **150/150**（1–150 全） | PASS |
| 三源对照 | 自写 `p8compare_reproof.py`（REG 原地重跑导出；text.md 解析；P8 键取自本轮 p8-extract.json） | `p8compare-reproof5.log` / `p8-compare-reproof5.json` | **MATCH 149/149，DIFF 0，MISSING 0**；#150 开放写作例外；Q140 四源一致；25–28=d/c/a/b，141–144=b/c/d/a | PASS |
| REG 一致性 | 本轮现导 `reg-dump.json` vs re-proof nl4 的 `reg-dump.json`（json.tool 规范化 diff） | `reg-dump.json` | 逐项一致，diff 为空 — fix5 未动任何键 | PASS |
| 键手验 | 通读 `keytable-150.txt` 150 条 + 外部事实复核（`date -d` Europe/Amsterdam；算术复算） | `keytable-150.txt` | 150/150 填空合理；Q140 外无同类键错；星期/算术全部复核通过 | PASS |
| Q150 范文 | text.md:432 直接计数 | `q150-line432.txt` | 81 词（去独立 `–` 为 80），在 80–100 内；P8 10/10 片段齐全 | PASS |
| P8 最小字号 | PyMuPDF 逐 span（印 PDF 第 8 页） | `gates-reproof5.log` / `gates-reproof5.json` | min **10.12pt**（561 段）≥ 9.75pt | PASS |
| keycheck | registry vs P8 extract | （p8compare 覆盖） | 149/150（仅 [150] 除外，为开放写作例外） | PASS |

## 6. 几何门禁

| 门禁 | 命令/方法 | 源日志 | 实测值 | 结论 |
|---|---|---|---|---|
| occlusion（真实审计） | `tools/occlusion_audit.py <svg目录>`（非 --selftest；工具先行自测） | `occlusion.log` | selftest OK；**0 flags**（含 BOXTITLE 0） | PASS |
| creambox canonical | `hidden_files/w47/tools/creambox.py <8 个 SVG 文件>` | `creambox-canonical-reproof5.log` | rc=0；P4 盒 inside-only 末基线 1209.5，余量 +20.1，desc-clear +13.7；负余量仅 3 处已 adjudicate 的下方独立区块 | PASS |
| creambox 旧脚本 | `check_creambox_reproof.py` | `creambox2-reproof5.log` | 3 flags：P2/P5/P6 各 1 处 CREAM-BOTTOM（≤1.6px）；P4 0；其余 0 | 3 处均为已知假阳性（见下） |
| creambox 真墨探针 | `inkprobe2_reproof.py`：框底 7px 带逐像素 + 最低真墨行 | `inkprobe2-reproof5.log` | 三处带内非纸像素 **0**；真墨余量 P2 +3.4 / P5 +3.5 / P6 +3.6px | **3 处真溢出 0** |
| **溢出全扫** | `spill_sweep_reproof.py`：每奶油盒外 0–60px 邻近文本扫描（补 creambox 盲区） | `spill-sweep-reproof5.log` | **0 溢出**；P4 盒无 BELOW 命中；最近 BELOW 命中 +24.00px（P1 区块标题），其余 ≥+32px，均已 adjudicate 为独立区块 | PASS |
| D3 回归 | PIL 真墨（P2 左右列） | `gates-reproof5.log` | 右 a +98.2 / b +46.0 / c +72.2 / d +55.8；左 25 +272.8 / 26 +280.2 / 27 +200.0 / 28 +259.2（边 1862） | PASS（均 ≥+46.0） |
| 金句在框/在版 | P7 `ZINNEN VAN DE WEEK` 8 句坐标 + 最低真墨行 vs 页脚带 | `inkprobe2-reproof5.log` | 最低真墨 y=2378.0，页脚带顶 2439，余量 61.0px | PASS |
| §1.1 适配检查 | 自写 `check_s11_core_nl.py`（check_s11.py/verify_ed.py 无 core-nl 版，见 PROOF-NOTE §7 备注 3） | `check_s11_core_nl.log` | 17 PASS：纸底 8/8、等级芯片全在 LV 色集、VOL.4 每页 ≥1、P4 无新增填充色 | PASS |

## 7. 印/网文字层与 PDF

| 门禁 | 命令/方法 | 源日志 | 实测值 | 结论 |
|---|---|---|---|---|
| 印/网 token 多重集 | PyMuPDF 逐页（`gates_reproof.py`，0.1pt 取整） | `gates-reproof5.log` / `gates-reproof5.json` | 8 页 multiset diff **0**；tokens 774/715/673/671/705/663/742/1917 | PASS |
| 印/网位置 | 同上 | 同上 | 仅 P1 两 token（`De`/`Lucerna`，x 394.0 vs 393.8，0.2pt），其余页 0；交付网与 scratch 重渲结果相同 | PASS（内容一致；0.2pt 为子集化微差，见备注） |
| pdftotext | `pdftotext` 印/网/重渲三方 | `print-text-reproof5.txt` / `web-text-reproof5.txt` / `web2-text-reproof5.txt` | 44,197 B = 44,197 B = 44,197 B，**逐字节一致** | PASS |
| 网 PDF scratch 重渲 | 复制 svg 至 `webpdf/svg`，`tools/webpdf.py` 仅写 scratch（未覆盖交付件） | `webpdf.log` | rc=0；重渲 2,104,001 B（交付 2,104,000 B，+1 B）；唯一差异区 = 1 个字体子集流（obj 20，Length 2174 vs 2173，Length1 同 3320）；文字层一致 | 注：字节不可复现，文字层一致 |
| 引号 | 印 PDF 全文 + text.md 计数 | `gates-reproof5.log` | ASCII `"` 0、反引号 0；`« »` 35/35；`“ ”` 1/1；md 同值 | PASS |
| 金句逐字 | 8 句金句在 text.md 正文检索 | `gates-reproof5.log` | **8/8** | PASS |
| D5 字体（只记录） | 自写 census（`<text>` 含 `[A-Za-z]` 且无 CJK 区字符） | `gates-reproof5.log` | 字体段 Noto Sans CJK SC 619 / Newsreader 1215 / Noto Serif CJK SC 305 / UnifrakturMaguntia 1；纯拉丁落 CJK **245** 段（分版 38/23/30/29/29/26/18/52） | 记录，不判 |

## 8. 目视（印 PDF 150dpi 自渲染，`render/p-1..p-8.png` + 裁图）

| 页 | 结果 |
|---|---|
| P1 | 干净。NU JIJ 1–6、BLIKSEMQUIZ 7–10 齐全；DE WEEK IN CIJFERS 数字与题干一致。 |
| P2 | 干净。`c. eten voor Sinterklaas' paard` 在界内；“D WOORDEN”标题在第 3 栏底、内容在第 4 栏（修前既有分栏，观察，不列缺陷）。 |
| P3 | 干净。D6/D7 修复处无复发；SINTERKLAAS IN CIJFERS 盒内容全在盒内（余量 +16.20px）。 |
| P4 | **D11 已修**：HET PROGRAMMA 盒 5 条事实全在盒内，末行 `18:45 uur.` 下有清晰奶油边距；其余干净；练习区 47–64 齐全。 |
| P5 | 干净。EN JIJ 盒末行在盒内；Q73 填空区无异常；65–82 齐全。 |
| P6 | 干净。D8 图注两行在盒内；VOOR OF TEGEN 盒内容齐全；图表 35/30/20/15 与 Q83–87 一致。 |
| P7 | 干净。D10 读者来信两行在盒内；金句 8 句 + 页码注齐全；VOLGENDE WEEK 带内有余量（proof2 N3 旧貌，P7 SVG 与 fix4 字节一致）。 |
| P8 | 干净。Q140 键含 kort；Q150 范文 81 词；答案区 150 题无缺行；141–144 配对齐全。 |
| 裁图 | `crop-p4-programma.png`（D11 行在盒内）✓；`crop-p6-d8.png`（D8 。回行末）✓；`crop-p7-d10.png`（D10 ，回行末）✓；`crop-p8-q140.png`（Q140 含 kort）✓ |

## 9. 汇总

- **通过**：D11（三重实测）；D8、D9、D10（回归正确）；孤儿 sweep (a)/(b) 0/0；150 题机械+手验；freeze 8/8；occlusion 0；spill sweep 0 溢出；creambox canonical rc=0 + 3 处假阳性真溢出 0；p8 150/150；P8 ≥10.12pt；印/网文字层一致；D3 回归；引号/金句/Q150；text.md 重导出字节一致；构建/渲染字节可复现；§1.1 适配检查 17 PASS。
- **不通过**：无。
- **结论 (a)**。fix5 可进入 nl delta 重建。
- **生产目录未改动**：最终 `git status --porcelain -- production/2026-w47/core-nl/` 与接手时一致（content34.py/content7.py/text.md/FIX-LOG/WEEKLY-KIT 的 M 状态为接手时已有；SVG/PDF/cards 为 untracked 渲染缓存）；三件 SHA 与接手时一致。
