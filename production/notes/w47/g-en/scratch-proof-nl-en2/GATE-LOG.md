# GATE-LOG — W47 nl-en proof2 (build 8, 全量复校机械门自跑)

- 版：`2026-w47-nl-en`，VOL.4，刊期 2026-11-16–2026-11-22
- 校对员：第二轮独立复校
- 日期：2026-11-11
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（全部机械门）
- 对象 SHA（实测，与任务登记逐字一致）：
  - print `De-Lucerna-VOL4-nl-en.pdf` 12,665,899 B `2cc431f2572abad8790d1b99d6211d3aa87a5278a4052f3f0810dd6d764b0b58`
  - web `De-Lucerna-VOL4-nl-en-web.pdf` 1,574,228 B `0fc6232bbe2bd8d3794169d83b4c233df519845f07eef1f9f35e2fdada2f6d18`
  - text `2026-w47-nl-en.text.md` 45,074 B `1d69f5edc43e217bfa5d9e032d3c8c6666460a37ee163d0f0db18b1bebeba45b`

## 1. 弯引号回归扫查（fix1 回归）

- 范围：`content*.py`、`svg/*.svg`、`2026-w47-nl-en.text.md`、`ABSTRACT.txt`、`svglib.py`、`bslib4.py`、`render.py`、`run.py` + 双 PDF 文字层（pdftotext）
- U+2018 / U+2019 / U+201C / U+201D / U+201A / U+201E / U+2032 / U+2033：**全部为 0**
- `.text.md` 第 366 行：`Editor's example, not a real letter. Send yours — we print them in VOL.5!`
- `.text.md` 第 45 行：`"Group win": first place in the group, straight to the quarter-finals.`
- 放大裁图核实：`render/p7-editors-crop2.png`（`Editor's` 紧贴、无宽空隙）、`render/p1-groupwin-crop3.png`（`"Group win":` 紧贴、冒号前无宽空隙）

## 2. occlusion_audit（0 flags）

```
$ tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/fanout-nl/2026-w47-nl-en/svg/
selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
production/2026-w47/fanout-nl/2026-w47-nl-en/svg/: 0 flags
rc=0
```

## 3. p8 extract / compare（150/150，CLEAN）

```
$ tools/venv/bin/python tools/p8.py extract --p8 production/2026-w47/fanout-nl/2026-w47-nl-en/svg/p8-toets.svg --total 150
production/2026-w47/fanout-nl/2026-w47-nl-en/svg/p8-toets.svg: noted set = 150 of 150 (parse: lines)
extract rc=0

$ tools/venv/bin/python tools/p8.py compare --core-p8 production/2026-w47/core-nl/svg/p8-toets.svg --edition-p8 production/2026-w47/fanout-nl/2026-w47-nl-en/svg/p8-toets.svg --total 150
core    production/2026-w47/core-nl/svg/p8-toets.svg: 150 noted
edition production/2026-w47/fanout-nl/2026-w47-nl-en/svg/p8-toets.svg: 150 noted
status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]
compare rc=0
```

keydiff [137, 138] 裁定：核心答案键为中文，en 版为英文——翻译题按读者语重定向（137/138 荷→英；139/140 英→荷），合法。详见 PROOF-NOTE.md。

## 4. freeze baseline（8/8）

```
$ tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/fanout-nl/2026-w47-nl-en --core-svg production/2026-w47/fanout-nl/2026-w47-nl-en/svg --out <scratch>/freeze
baseline: 8/8 SVGs byte-identical (repointed files: none)
  OK  p1-voorpagina.svg core e9b37a631cf976cc produced e9b37a631cf976cc
  OK  p2-leven.svg core 27be7be587a52d0d produced 27be7be587a52d0d
  OK  p3-cultuur.svg core 66f52611c661084a produced 66f52611c661084a
  OK  p4-sport.svg core 385e60d0448bb582 produced 385e60d0448bb582
  OK  p5-jongeren.svg core 5d45aacc25715492 produced 5d45aacc25715492
  OK  p6-verdieping.svg core 8b94a87911a1b02d produced 8b94a87911a1b02d
  OK  p7-taal.svg core cdefd6d6a8ec900c produced cdefd6d6a8ec900c
  OK  p8-toets.svg core cf3a415aebdf94da produced cf3a415aebdf94da
core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
freeze rc=0
```

## 5. print/web 文字层（PyMuPDF 位置排序）

```
P1: print tokens 218 web 218 posdiff 3 msdiff 0
P2: print tokens 203 web 203 posdiff 0 msdiff 0
P3: print tokens 189 web 189 posdiff 0 msdiff 0
P4: print tokens 184 web 184 posdiff 0 msdiff 0
P5: print tokens 196 web 196 posdiff 0 msdiff 0
P6: print tokens 201 web 201 posdiff 0 msdiff 0
P7: print tokens 188 web 188 posdiff 0 msdiff 0
P8: print tokens 386 web 386 posdiff 0 msdiff 0
```

P1 的 3 处 posdiff 均为 ≤0.2pt 舍入（`De Lucerna` 394.0 vs 393.8；`SINTERKLAAS` 884.1 vs 884.2；`PAKJESAVOND` 1109.4 vs 1109.5），内容逐字相同。pdftotext 逐页词数 print=web：768/820/722/705/793/740/896/2112。

## 6. pdftotext 非空 + web 体积

- print 45,404 B / web 45,409 B（均 > 0）
- web PDF 1,574,228 B = 1.50 MB < 7 MB

## 7. P8 答案字号（PyMuPDF）

- 最小 10.125pt，中位数 10.35pt（≥ 9.75pt）

## 8. VOL 核对

- `tools/tables.py vol 2026-W47` → vol 4
- 印刷文字层 VOL.4 ×10、VOL.5 ×5

## 9. 徽章计数（.text.md 标记独立重数）

- A2 46 / B1 73 / B2 31（单题标记 A2 43/B1 73/B2 28 + D 组 25–28 共用一枚 A2 + F 组 141–144 共用一枚 B2）；合计 150，与 KIT 一致

## 10. §1.1 SVG 审计

- 家具无金色；描边矩形 0；调色板外色值仅限 P1 三色蛾品牌标记（嵌套 SVG）与绿底栏副标题淡色 #cac8ba
- 纸色填充等与 proof1 门一致；无新增问题

## 结论

全部机械门通过。fix1 回归为 0；freeze 8/8；p8 150/150 CLEAN；occlusion 0 flags；print/web 文字层多重集一致；P8 最小字号 10.125pt ≥ 9.75pt。
