# GATE-LOG — W47 it-fr re-proof（core D-2 fix 后重扩散新版，独立重跑）

- 版：`production/2026-w47/2026-w47-it-fr/`（core D-2 fix，核心复校 (a) 后重扩散）
- 工具：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0）
- 环境：`PYTHONDONTWRITEBYTECODE=1`；`TMPDIR=<scratch>/tmp`
- scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it2-fr/`
- 探针：`git hash-object -w /dev/null` 成功（e69de29bb2…，RC=0）；scratch 真实写盘成功。

## 0. SHA 核对（开工 + 收工两次）

| 文件 | sha256 | 字节 | 开工 | 收工 |
|---|---|---|---|---|
| `La-Lucerna-VOL4-FR.pdf` | `e80d4dd3eb4c512c7d0c84c29c10fad56b927dc85f2b76663dcd82fef68727f0` | 14,034,054 | ✓ | ✓ |
| `La-Lucerna-VOL4-FR-web.pdf` | `d8fe0ef50efcfe7d2641e7ca737b618d8c06a529c6e33c016557f242c8977054` | 1,290,956 | ✓ | ✓ |
| `2026-w47-it-fr.text.md` | `aca1356c0c90526a7a621a399bc5ea9a75f9b635aae42662022217ddc01d5cad` | 56,517 | ✓ | ✓ |

KIT §7 所载印/网/文 SHA 与字节数一致；修前三 SHA（印 `6e393b3d…` /
网 `7276c70f…` / 文 `a634057b…`）见 §12 历史行与
`scratch-refanout-it2/shas-pre.txt`。

## 1. run.py（`run-rebuild.log`，scratch 副本内运行）

- RC=0；TOTAL 150；levels A2 47 / B1 70 / B2 33；
  pages 10/18/18/18/18/18/12/38；model text 99 words。
- 0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE（grep 计数 0）。
- flow 末端（均在界内，与 KIT §8 逐值一致）：P1 settimana 1250.24；
  P1-quiz 2491/2540；P2 col3 1350.6；P3 col3 1290.6；P4 col3 1140.45
  （= core 1140）；P5 col3 1249.75；P6 col3 1096.5；P7-a2 1124（D-2
  改后值，改前 1157，短一行，底 1560）；P7 col3 1673.0；
  P8-ex 870/1332；P8-keys 2514/2552。**PASS**

## 2. SVG 重建 8/8 字节一致

- scratch 副本 `run.py` 重建后与交付 SVG 逐一 sha256 比对：
  p1 874b2129… / p2 8bfcedce… / p3 617cf701… / p4 b7637046… /
  p5 9abdc25c… / p6 723d688d… / p7 40b42701… / p8 94b069ae…，8/8 OK。
  （p1–p6/p8 与 proof2 记录值逐字一致；p7 为 D-2 改动后值。）**PASS**

## 3. 重渲印 PDF 与交付逐字节相同

- scratch 副本 render.py（BASE 重定向）RC=0；
  重渲 `build/La-Lucerna-VOL4-FR.pdf` sha256
  `e80d4dd3eb4c512c7d0c84c29c10fad56b927dc85f2b76663dcd82fef68727f0`，
  14,034,054 B，`cmp` 通过；8 张 cards 与交付逐一比对全同。**PASS**

## 4. freeze 核心 baseline 8/8（`freeze-core.log`）

- `tools/freeze.py baseline --build <core-it> --core-svg <core-it>/svg
  --out <scratch>/freeze-core`：
  `baseline: 8/8 SVGs byte-identical`（p1 d301b886… / p2 a744e5d2… /
  p3 fe0a0e65… / p4 12ddd86c… / p5 08929554… / p6 621054ee… /
  p7 a7e6afa4… / p8 779aa98c…）；`core integrity: shipped core SVGs
  unchanged`。运行时 Pillow 13.0.0 / FreeType 2.14.3。**PASS**
- build-copy 核实为 core-it 自身（非 edition 目录冒充）：
  `freeze-core/build-copy/` 含 core-it 全部源文件（content*.py、run.py、
  render.py、WEEKLY-KIT.md、2026-w47-it-zh-cn.text.md 等）；
  其 `content7.py:17/:18` 为 D-2 新串（`Le forme sono regolari:
  assaggiare → assaggerò, guardare → guarderò.` /
  `Il verbo è leggere, regolare al futuro: leggerò.`）；
  产出 p7 `a7e6afa4…` 与 D-2 定稿核心 SVG 一致。
- 另：本版 freeze baseline（重扩散员 `freeze-fr/`）亦为 8/8，本轮以
  run.py 重建 8/8（门 2）+ 重渲 PDF 逐字节一致（门 3）独立复核了
  本版的可复现性。

## 5. freeze diff（gates.py 内，见 `gates-fr.log`）

- fragments explained：unexplained_add=[] unexplained_rem=[]（P1–P7）。
- 报告 present：pages 1–8。
- strict-cjk：added_cjk={'\\u3000': 8}，non_space={}。**PASS**

## 6. occlusion（gates.py 内）

- `tools/occlusion_audit.py`（selftest OK）：0 flags。**PASS**
- 注：occlusion 对无边框奶油盒横向溢出是盲的，本版另以门 7 像素扫裁决，
  不以此门为据。

## 7. 奶油盒 PIL 真墨像素扫（`cream-scan.log`，`cream_scan.py`，复用 proof2 同方法）

- 29 个无边框奶油盒（#f0eee5）逐盒像素扫：全部 PASS，无墨越界。
- 最薄：P1 LA SETTIMANA 盒（x=1439.5, y=588）margin-R=0 px
  （字墨触边，见 PROOF-NOTE O1，与 proof2 实测逐值相同）；其余 +7 至 +189 px。
- 四个表修标题像素实测：D1 +7 px；D2 0 px；D3 +9 px；D4 +110–111 px。
- P7 三盒余量 +48/+26/+30（D-2 改动栏不在奶油盒内）。
- 备份旧版对照：p1–p6/p8 cards 与 `scratch-refanout-it2/backup/` 逐字节
  一致；p7 card 像素 diff 局限于 A2 栏（x 87–508、y 387–1122），
  右侧奶油盒 0 像素差异。**PASS**

## 8. spill：0

- build 日志 0 溢出（门 1）+ 全部 flow 末端在界内（门 1）+ 奶油盒像素扫
  29/29（门 7）+ occlusion 0（门 6）。**PASS**

## 9. 孤儿扫

- P8 SVG/card 与 proof2 版逐字节一致，proof2 精扫结论（0 处栏断孤儿）
  对本版仍然成立；本轮逐页目视 + P8 键区逐行核对，仅 1 处行内独词换行：
  P8 Q139 第二行 `domicile`（p8 y=2187，判定见 PROOF-NOTE O3，非缺陷）。
  其余 7 页 flow 末端均在界内，无栏断孤儿的机械征兆。**PASS**

## 10. p8 extract 150/150（gates.py 内）

- `tools/p8.py extract` noted=150，rc=0。**PASS**

## 11. p8 compare（gates.py 内）

- `tools/p8.py compare` vs core：verdict=CLEAN，
  **keydiff 实测 [137, 138, 139]**（重定向的读者句键，与预期一致；
  Q140 键为意语句、与核心相同故无 diff，正确）。
- 另：150-key 审计 vs core `.text.md`：keys 1–150 match
  （除 137–139 与写作题外）；notes match translations.py
  （除 137–140 与写作题外；9 条冻结注释为意语变位/算术，字节一致、无 CJK）。**PASS**

## 12. P8 最小字号 ≥9.75pt

- P8 SVG 最小 font-size 13.0 px = 9.75 pt（§1.1 下限）。**PASS**

## 13. §1.1 视觉规范

- paper #fbfaf6 present；no gold/brick/near-black（hits=[]）；
  VOL.4 ×9；VOL.5 text nodes=3（仅预览/披露/交叉引用三处合法）；
  badge colours A2 #5c6e30 / B1 #46581f / B2 #37402f 齐全；
  no double outer frame（full-page rects=0）。**PASS**
- 注：`·` 总计 148 处，位于选项串/注释表内（核心同式）。

## 14. 印/网文字层一致（gates.py 内；web PDF 未重渲）

- pdftotext 词多重集：print 8009 / web 8009 词，字符多重集相等。
- plain pdftotext 字节：印/网各 46,224 B（与 KIT §7 所载一致）。
- web PDF 1,290,956 B < 7 MB；print PDF 14,034,054 B；
  两 PDF 均为 8 页，1462.5×2025 pt。**PASS**

## 15. text.md validate

- forward-miss 0 / reverse-miss 0（fr footer 正则 `Page \d+ sur 8`）。
  1317 行，150 题。**PASS**

## 16. 日期星期全验

- `TZ=Europe/Rome date -d`：Nov 6 周五、7 周六、8 周日、9 周一、
  12 周四、15 周日、16 周一、17 周二、19 周四、20 周五、21 周六、
  22 周日、23 周一、24 周二、29 周日、Dec 2 周三、Dec 6 周日、
  Dec 31 周四。文中全部星期主张逐项正确。**PASS**

## 17. D-2 回归专项（本轮独立重测，见 PROOF-NOTE §A/§B）

- 新串各就其位：text.md:775/:777、content7.py:17/:18、p7 SVG、
  印/网 PDF P7 文字层各 ×1；旧串 live 文件 0 处。
- 与修前生产版 diff 只许 P7 变化：SVG/cards 仅 p7 不同、text.md 恰
  :775/:777 两行（−21 B）、content 恰 `content7.py:17/:18` 两行、
  p7 SVG 节点 diff 仅限两句碎片、p7 card 像素 diff 局限于 A2 栏。
- P7 A2 教学句规则性标签语义正确（独立检索核实：andare 不规则
  andr-、leggere 规则 leggerò；来源 dante-learning / FlexiClasses /
  LBCC Pressbooks / FluentU）。**PASS**

## 18. 全文精读与看图

- `.text.md` 1317 行通读：意语层 freeze 0 unexplained；8 金句各 ×2；
  150 key/note 逐题三源复核；法语层无拼写/性数/变位/标点错误；
  Q137–140 标签本地化，无中文残留；禁用词 0；非 U+3000
  CJK/西里尔 0；99 词范文逐词数过 = 99。
- 事实抽查（公开来源）：Serie A 积分/赛果、Torrone、Eurochocolate、
  BookCity、Torino Film Festival、Filmmaker Festival、ATP Finals、
  Manovra（DPB、C. 3174-bis、听证、修正案截止、Irpef）全部与
  2026-11-11 检索到的公开来源一致（来源清单见 PROOF-NOTE）。
- 8 版逐版看图：200 dpi 全页 P1–P8 + P7 A2 / P1 D2 / P8 Q139
  全分辨率裁图；无溢出、重叠、压页脚、tofu、图片错位。**PASS**

## 19. gates.py 20 门（独立重跑，`gates-fr.log`）

```
PASS occlusion 0 flags
PASS p8 extract noted count (150)
PASS p8 compare vs core (CLEAN, keydiffs=[137, 138, 139])
PASS freeze diff fragments explained (0 unexplained)
PASS freeze diff report present (pages 1-8)
PASS freeze strict-cjk (only U+3000 x8)
PASS print/web text multiset identical (8009/8009, chars_equal=True)
PASS web PDF < 7MB (1290956)
PASS print PDF size sane (14034054)
PASS P8 min font >= 13px (min=13.0)
PASS paper #fbfaf6 present
PASS no gold/brick/near-black
PASS no VOL.5 in furniture (3 nodes)
PASS VOL.4 present (count=9)
PASS badge colours A2/B1/B2
PASS no double outer frame (0)
PASS textmd validate (0/0)
PASS answers count 150 (150/150)
PASS keys 1-150 match core (except 137-139, writing)
PASS notes match translations.py (except 137-140 + writing)
GATES ALL PASS — 20/20, 0 FAIL
```

## 总评

全部门禁通过。结论 (a) 零缺陷，可定稿。D-2 回归各项子检查全部通过；
最薄点已在 PROOF-NOTE O1–O5 中以像素实测与渲染证据记录在案，均不构成缺陷。
