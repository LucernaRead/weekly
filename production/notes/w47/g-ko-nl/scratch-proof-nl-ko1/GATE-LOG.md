# GATE-LOG — 2026-W47 · nl → ko · proof1 机械门实跑证据

复校员独立实跑，不信 KIT，只信自己跑的结果。全部命令用 `tools/venv/bin/python`；
TMPDIR 全程指向本 scratch 下 `tmp/`；`PYTHONDONTWRITEBYTECODE=1`；
重建/探针均在 scratch 内完成，生产只读（收尾三 SHA 与开工逐字节相同）。
工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-ko1/`。
证据文件：`gates-run1.log`、`rebuild.log`、`freeze-core.log`、`freeze-ed.log`、`occlusion.log`、
`p8-extract.log`、`p8-3way.log`、`p8-compare-3way.json`、`registry-new.json`、`creambox.log`、
`boxtitle-ko.log`、`d11-probe.log`、`spill.log`、`orphan.log`、`orphan-core.log`、`crop-p8-headA-300dpi.png`、
`render/p-2.png`、`render/p-4.png`、`render/p-5.png`、`render/p-6.png`、`render/p-8.png`、`render/p300-8.png`。
（本目录内旧 build-1 轮次文件已归档至 `archive-build1-proof/`。）

## 门 1 — 身份核对：PASS

- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，rc=0；
  scratch 真实写文件 `probe.txt` 通过。
- 开工与收尾两次实测一致：印 `c4f446b9adc06c29be6a047abf30c83a445062bc26335a578a9609afb42d537d` / 17,281,343 B；
  网 `75f6730e10925f575c4a348e0428cdf6c85be2bb658ed4e9037a85d55ae1176e` / 1,919,772 B；
  文 `75fbaa3004d0da29ce096953bd584b891afc2daee6a2bffa8d7cd7fe31105dd9` / 47,585 B——与任务给定值及 WEEKLY-KIT.md 登记值逐字一致。

## 门 2 — run.py 重建：PASS

- scratch 重建（`rebuild/` 内复制 *.py + assets 运行）：rc=0，`TOTAL 150`，
  `OVERFLOW`/`TOO WIDE` 出现 0 次（`rebuild.log` 全文 grep 计数 0），`ALL DONE`。
  by page {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；by level {A2:46, B1:73, B2:31}；model words 81。

## 门 3 — SVG 重建 8/8 字节一致：PASS

- 重建 SVG 与交付 SVG 逐页 sha256 对比：p1–p8 全部 MATCH（8/8）。
  另：p3/p6/p7 与 delta 修前（build-2）SHA 前缀一致（`bbdfd827…` / `8a5ff2df…` / `4cfecc9e…`），
  仅 p4（D11）与 p8（D9）有变，与 KIT 所述一致。

## 门 4 — freeze 核心 baseline 8/8：PASS

- `tools/freeze.py baseline --build production/2026-w47/core-nl --core-svg production/2026-w47/core-nl/svg`：
  rc=0，`baseline: 8/8 SVGs byte-identical`，core integrity：8 文件重哈希未变。

## 门 5 — freeze 本版自身 8/8：PASS

- `tools/freeze.py baseline --build <本版> --core-svg <本版>/svg`（--core-svg 指向本版 svg 子目录）：
  rc=0，`baseline: 8/8 SVGs byte-identical`，integrity：8 文件重哈希未变。

## 门 6 — occlusion 几何遮挡：PASS

- `tools/occlusion_audit.py svg/`：rc=0，`svg/: 0 flags`；
  自检：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`（六类全触发）。

## 门 7 — 奶油盒纵扫 + 渲染像素双法：PASS（3 报警全假阳性）

- 纵扫（`check_creambox_delta.py`，本版 SVG 几何）：p1 0 / p2 1 / p3 0 / p4 0 / p5 1 / p6 1 / p7 0 / p8 0，共 3 flags，全部 CREAM-BOTTOM，
  0 CREAM-RIGHT，0 PAGE-EDGE：
  P2 EN JIJ 末行底 1417.8 vs 盒底 1416.8；P5 EN JIJ 966.4 vs 965.5；P6 图注 689.4 vs 盒底 691.0（行内）。
- 像素双法（`boxtitle_ko.py` 末节，盒矩形逐版重推导）：3 盒 ×（cards 1× + 印 PDF 150dpi 渲染）
  盒底下 7px 条带非纸像素全部 **0** → 假阳性（descent-allowance artifact）。
  （注：occlusion 对纯填色 `#f0eee5` 奶油盒全盲，本门不以 `boxtitle_rc: 0` 为证。）
- D11 专项双法（`d11-probe.log`）：盒底 1229.6，末行 `18:45 uur.` 基线 1209.49，基线余量 +20.11px；
  真墨余量 +20.60px（cards）/ +20.48px（印 PDF 150dpi）；7px 条带双法 0 墨。

## 门 8 — spill 横扫：PASS（0 溢出）

- `spill_sweep_reproof.py`：全部奶油盒邻接候选（ABOVE/BELOW/SIDE）均为正常邻接元素
  （下一节头、图注、讲解行，间距 24–60px），无盒内文字越过盒界；P4 D11 盒下方 60px 内无任何文字。

## 门 9 — 孤儿扫 + 核心集比对：PASS（0 新增）

- 本版：PIL-advance 1427 行 (a)=0/(b)=0；svglib-advance 1427 行 (a)=0/(b)=0；
  brute-force 以标点起首的 `<text>` 57 个，leftmost-on-baseline **0**。
- 核心 core-nl 同脚本同法：1421 行 (a)=0/(b)=0；brute-force 起首标点 13 个，leftmost **0**。
  两版 class-a/b 均为 0，brute leftmost 均为 0 → **0 新增**。
- 靶向行（韩语针头自查）：D6 2 行、D7 2 行、D8 3 行（基线 635.02/659.44/683.86）、D10 2 行全部如 KIT 所述，
  无行首/独行标点。（delta 脚本内置德语针头在本版为空集，属预期，已改用韩语针头重查。）

## 门 10 — p8 extract 150/150：PASS

- `tools/p8.py extract --p8 svg/p8-toets.svg --total 150`：rc=0，`noted set = 150 of 150`（1–150 全集）。

## 门 11 — p8 compare vs core：PASS（CLEAN）

- `tools/p8.py compare --core-p8 core-nl/svg/p8-toets.svg --edition-p8 <本版>/svg/p8-toets.svg --total 150`：
  `status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`；
  keydiff [137, 138] 为翻译题键即读者语（韩语），属设计。

## 门 12 — keycheck / 150 题三方逐字比对：PASS（149/149 + Q150 例外）

- 三源：registry-new.json（scratch 重建 dump，150 条）vs text.md（韩语标记 `— 정답：` 142 处 + `(정답 x` 8 处）
  vs P8 extract JSON：**MATCH 149/149，DIFF=[]，MISSING=[]**（`p8-compare-3way.json`）。
- Q140 三源逐字一致：`Ik maak een surprise met een kort gedicht.`（registry + text.md:415 + P8 节点 y=2143.98）。
- Q150 例外重组核实：P8 键 `✓`；text.md Tekstmodel 81 词；REG 为开放写作占位符；
  第 9 处 `(정답` 为 Q150 说明行 "쓰기 과제(정답이 하나가 아니에요)"，非配对题。
- text.md 审计：Han 字符 0；`答案` 残留 0；431 行；Tekstmodel 81 词；ABSTRACT 韩语一行。

## 门 13 — 印/网文字层 8 页：PASS（posdiff/msdiff 0）

- PyMuPDF 位置排序逐页比对：P1 733/733，P2 713/713，P3 668/668，P4 667/667，P5 695/695，P6 657/657，
  P7 754/754，P8 1640/1640；posdiff=0，msdiff=0；页数 8/8。
- pdftotext：印 47,618 B / 网 47,618 B；网 PDF 1,919,772 B（< 7 MB）。

## 门 14 — P8 最小字号 ≥9.75pt：PASS

- 印 PDF P8 答案区（y ≥ 1328×scale）：min **10.12pt**，median 10.12pt，spans 613。

## 门 15 — §1.1 调色板 / 禁用色 / VOL.4：PASS

- off-palette={}；禁用 GOLD/旧色 False；带 stroke 的 rect 0；VOL.5=5（= core 5，系正文 "VOL.5로" 引用）；
  纸色 `#fbfaf6` fills=8；VOL.4 每页 1 处，共 8 处。

## 门 16 — 盒标题真墨扫 + P8 A 标题裁决：PASS（1 OVER 为扫描件 artifact，记观察）

- 本版自写 `boxtitle_ko.py`（头标题取自本版源码 `.head()`，盒坐标逐版重推导，未复用他版坐标）：
  59 标题（38 HEAD 出现 + 21 BOX），1 OVER：P8 `A　VUL DE KRONIEK IN`，cards 1× 真墨右 537，栏缘 510.5，−26.5px。
- 裁决证据（见 PROOF-NOTE D-01）：PIL bold advance 234.79px → 字形实测右缘 320.0（栏内余量 +190.5px）；
  印 PDF 150dpi 字形行最右墨 320.6；−26.5 墨点为版头带下沿 + 第 2 栏 B1 色块（x=538.5）左缘抗锯齿被 28px 外伸扫描窗吃入；
  core-nl 同位测量逐值相同（冻结设计，非回归）；300dpi 裁图目视字形完整、零重叠。
  **结论：观察，非缺陷**；其余 58 标题 ok；最紧余量 +0.5px（head 下划线止于栏缘）。
- 跨版注：nl-en 同项亦 −26.5 而其扫描报 0 越边，应为计数口径差异；建议协调员决定是否立项 sweep 全家统一扫描口径。

## 门 17 — 语义抽查 + 日期全验 + D6–D11 复核：PASS

- 语义抽查 0 错配（配对题 Q25–28、Q141–144 逐组核对；单题抽查 Q1/Q2/Q7/Q15/Q20/Q22/Q23/Q32/Q37/Q113/Q126/Q137/Q138/Q139/Q140/Q145/Q149/Q87，
  键–干逐项核对，事实均有正文依据；详见 PROOF-NOTE）。
- 日期：`date -d`（America/Toronto）2026-11-16 星期一、2026-11-22 星期日；
  P1 刊头 `WEEK VAN 16 TOT EN MET 22 NOVEMBER 2026`；P7 下周预告 24 日星期二、29 日星期日与日历一致。
- D6/D7/D8/D10 结构同步值在本版区间内且断行不变（w=414.35 / w=423.65 / capcn_w=380.7 / dt_zh_w=376.3，
  源码行见 PROOF-NOTE），p3/p6/p7 SVG 字节一致；D9/D11 真修双法/三方法复核通过。
- 目视 8 页（交付 cards）：0 缺陷。孤儿填空行（Q130/Q36/Q37 式）属观察类、核心继承，不修不报；
  "next Sunday" 为冻结核心，永不作缺陷。
