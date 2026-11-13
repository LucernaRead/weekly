# W47 KO core — 第五轮独立校对机械门日志（proof-ko5，run 10，2026-11-11）

> 复校对象：run 10 成品。印刷 PDF SHA-256 `7b004b36…aeb5e`（46,232,169 字节）；
> 网页 PDF SHA-256 `e9c1ca0c…8fbfa`（4,232,790 字节）；
> text.md SHA-256 `81ebd0a3…e8c0`（26,014 字节，333 项）。
> 本目录文件：`freeze-ko5.log` / `freeze-ko5.json` / `freeze-ko5/svg/`（锁定环境 8/8 产物），
> `freeze-ko5-venv.log` / `freeze-ko5-venv.json` / `freeze-ko5-venv/svg/`（venv 对照 0/8），
> `occlusion-ko5.log` / `occlusion-ko5.json`，`occlusion-ko5-syspy.log` / `occlusion-ko5-syspy.json`，
> `p8-extract-ko5.log` / `p8-extract-ko5.json`，`p8-compare-ko5.log`，
> `check-core-ko5.log`，`check-gloss-ko5.log`，`print-ko5.txt` / `web-ko5.txt`（各 49,379 字节），
> `svg-text-ko5.txt`（8 页可见文本，1,496 行），`work/pg-{1..8}.png`（印刷版重渲染），
> `work/webpg1-1.png` / `work/webpg8-8.png`（网页版 P1/P8）。

## freeze（基线复现）

- 锁定环境 `/usr/bin/python3`（PIL 10.2.0）：`tools/freeze.py baseline --build production/2026-w47/core-ko --core-svg production/2026-w47/core-ko/svg --out scratch-proof-ko5/freeze-ko5` → **8/8 SVGs byte-identical**，rc=0。
  逐文件 OK：p1 c47bc434067fdc90、p2 faf9e3c530f200b1、p3 b447a559c6f8d61d、p4 4b18a1d9b3c2f8dc、p5 09f7fc23850a1deb、p6 d45b03557f02f47a、p7 e6908156fe45e85f、p8 e88f7d421d621f92。`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。
- venv 对照 `tools/venv/bin/python`（PIL 13.0.0）：**0/8**，rc=1。P1 漂移产物 f6547a8321b81078、P2 997ef89f2b99ca16，与 fix4 记录一致——解释器 artefact，KIT 已注明为 control，非门禁失败。
- 度量差独立实测（NotoSerifCJK-Regular.ttc index=1，40px，「삼성 라이온즈가 12년 만에 한국시리즈 우승을 차지했어요」）：系统 PIL 10.2 = 991.296875；venv PIL 13.0 = 1002.15625。

## occlusion_audit.py

- venv：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`；`production/2026-w47/core-ko/svg: 0 flags`，rc=0。
- 系统 python3（与构建同款 PIL）：同样 **0 flags**，自检同样全触发，rc=0。
- 已知盲区（工具不查 `<image>` 元素）由 P7 目视覆盖：김치照片 3 栏跨度与第 4 栏两框无遮挡。

## p8.py

- `extract --p8 svg/p8-siheom.svg --total 150`：**noted set = 150 of 150 (parse: lines)**，1–150 连续，rc=0。
- `compare --core-p8 … --edition-p8 … --total 150`：**CLEAN**，missing=[] extra_count=0 uncertain=[] keydiff=[]，rc=0。

## check_core.py / check_gloss.py（系统 python3）

- check_core：gloss fails **0**；P7 phrases **8/8 verbatim**；orphan issues **0**；
  dates：2026-11-16 Mon → D-3；2026-11-18 Wed → D-1；2026-11-19 Thu → D-day；2026-11-22 Sun → 김치의 날；
  Nov 16 Monday / Nov 18 Wednesday / Nov 19 Thursday / Nov 22 Sunday / Nov 28 Saturday。rc=0。
- check_gloss：10 项（P2 조사하다/등재되다/아삭하다；P4 하나가 되다/전하다；P5 가벼워지다/피곤하다/졸리다；P6 바뀌다/전하다），
  皆为词典形 vs 屈折形同类；本轮逐项核实 10 个屈折形全部真实出现在正文中。rc=0。

## 文字层（双版一致）

- `pdftotext` 印刷版与网页版各 **49,379 字节**，`cmp` 逐字节同。
- P8 最小字号（PyMuPDF，印刷版，答案区 y≥976.5pt）：162 spans，最小 **9.975pt**（158 个 9.975pt + 4 个 12.75pt），≥ SOP §1.1 下限 9.75pt。
- 页尺寸 1462.5 × 2025 pt；8 页文字层逐页检出 VOL.4。

## 徽章与题量（编程式核对）

- 逐题归属：P1 10（A2 10）、P2 18（A2 16 / B1 2）、P3 18（A2 12 / B1 6）、P4 18（B1 18）、P5 18（B1 18）、P6 18（B2 18）、P7 12（A2 4 / B1 4 / B2 4）、P8 38（A2 9 / B1 24 / B2 5）；合计 **150，A2 51 / B1 72 / B2 27**，与 KIT 登记一致。
- H 写作范文去空白字符计 **169 字**（150–200 区间内）。

## 孤悬标题重扫

- 全部 size-25 橄榄粗体 sans 标题（8 页共 36 个）：每标题同栏下方均有正文，**0 处**孤悬。
- P4 D 标题 (989.0, 1641) 第 3 栏顶，61–64 项 y=1731–1842 同栏；P2 D 标题 (1439.5, 1897) 第 4 栏顶，25–28 项 y=1987–2098 同栏。

## 数字空格扫描（§1.1）

- ABSTRACT.txt：`199,456韩元` / `12年后` / `150道练习题` 各 1 处；旧形式 `199,456 韩元` / `12 年后` / `150 道` / `11 月` 均为 0；数字+空格残留仅 D-3 / A2 / B2 三处代号。
- 全书可见文本：`\d [CJK 表意字]` 0 处；`\d\u3000` 仅为规定的全角空格家具分隔；`\d [한글]` 仅为 `8대 7 승리` / `3대 2 승리`（韩语词间空格，正确）。

## 目视

- 印刷版 8 页 + 网页 P1/P8：从 run 10 成品 PDF 重新渲染（`pdftoppm -r 100`，`work/`），逐页目视；
  无溢出、重叠、页脚侵入、豆腐块；P7 照片与第 4 栏框无遮挡；P4 梯形图、P6 对比表右缘均在跨度内。
