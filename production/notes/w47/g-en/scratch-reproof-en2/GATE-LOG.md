# GATE-LOG — W47 core-en fix2 独立 re-proof（2026-11-11）

Scratch: `hidden_files/w47/scratch-reproof-en2/`（全新专用）。
生产目录：`~/workspace/weekly-git/production/2026-w47/core-en/`（只读；构建与重渲均在
`scratch-reproof-en2/work/` 副本内进行）。
工具链：repo `tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3，freeze 日志源行）。
探针：`/dev/null` 存在；`git hash-object -w` 通；scratch 真实写文件成功。

## 0. SHA 核对（源行：exec 实测）

```
动手前：
08cbc1e53f2d02d6c64266d1f64ac2422eaa2f8f71e1829f877e94a5627b3213  The-Lucerna-VOL4-en-zh-cn.pdf       41407287
d7927eaad14531a9aee71331d4e27abbf951a296f6b6ee5fb1c770f8c7f7e444  The-Lucerna-VOL4-en-zh-cn.web.pdf   2804281
23855d4bd60abe4a7fb4db42050cb9343202e85789ffd434634808d299215c69  2026-w47-en-zh-cn.text.md          51402
结束时重测：三 SHA 与字节数完全相同（生产目录未动）。
修前 text.md 快照 sha256: e368828a3fd5bb5a90de0d506a94fc03b22453e1d3d5ff139792f2b42e0ff70b
  = 任务给定修前基线（scratch-fix-en2/tmp/text-prefixed.md）。
```

## 1. 改动 diff（源行：diff 实测）

```
diff text-prefixed.md 2026-w47-en-zh-cn.text.md  → 仅 1151c1151：
< 73. [A2] 完成句子 — speak (speak up = 大声说出来)
> 73. [A2] 完成句子 — up (speak up = 大声说出来)
diff <json.tool registry-prefixed.json> <json.tool registry.json> → 仅一处：
583c583 < "key": "speak"  > "key": "up"
content56.py:49 实测：f.ex("A2", "完成句子", "up", "speak up = 大声说出来",
  "Speak ___: tell a teacher.", instr="填空")
```

## 2. run.py（scratch 副本 `work/run.py`）

```
rc=0
  flow[P8-battery] ended col 3/3 y=1418 (bottom 1555)
MODEL words: 82
  flow[P8-keys] ended col 3/3 y=2548 (bottom 2560)
P8 saved, TOTAL exercises: 150
ALL DONE
grep -c "FLOW OVERFLOW|HEAD TOO WIDE" run-reproof.log → 0
日志：run-reproof.log
```

## 3. render.py（scratch 副本，tools/venv python）

```
rc=0
print PDF: work/The-Lucerna-VOL4-en-zh-cn.pdf 41407287
sha256: 08cbc1e53f2d02d6c64266d1f64ac2422eaa2f8f71e1829f877e94a5627b3213
  = 交付印 PDF SHA（字节可复现）
日志：render-reproof.log
```

## 4. freeze.py baseline（源行：freeze-reproof.log）

```
runtime: tools/venv/bin/python | Pillow 13.0.0 | FreeType 2.14.3
baseline: 8/8 SVGs byte-identical (repointed files: none)
  OK  p1-front.svg core a9a8deaf76e61cb2 produced a9a8deaf76e61cb2
  OK  p2-life.svg core 979747160de01d67 produced 979747160de01d67
  OK  p3-culture.svg core efb83ce76688554b produced efb83ce76688554b
  OK  p4-sport.svg core aa6f395e4932ef8b produced aa6f395e4932ef8b
  OK  p5-youth.svg core a6a515cd5f734d0d produced a6a515cd5f734d0d
  OK  p6-deep.svg core 7692256484f26289 produced 7692256484f26289
  OK  p7-lang.svg core da908af644651793 produced da908af644651793
  OK  p8-test.svg core 1066c475da8afe7e produced 1066c475da8afe7e
core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
rc=0；--build 指 core-en 构建目录，--core-svg 指其 svg/ 子目录。
```

## 5. occlusion_audit.py（真实命令，无 --selftest；源行：occlusion-reproof.log / .json）

```
selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
…/core-en/svg: 0 flags
core: 0 flags; NEW vs core: 0
json: {"flag_count": 0, "core_flag_count": 0, "new_flag_count": 0, "flags": [], "new_flags": []}
rc=0
```

## 6. p8.py extract + compare（源行：p8-extract-reproof.log / p8-compare-reproof.json）

```
extract rc=0：noted set = 60 of 150 (parse: joined)
  set: [3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82, 83, 84, 85, 86, 87, 89, 108, 109, 110,
        111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128,
        129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145,
        146, 147, 148, 149, 150]
  与 fix1/fix2 基线集合逐项相同（脚本比对 a==b True）；73 不在 noted 集内（P5 注记超长，属既定过滤）。
compare rc=0：core 60 noted / edition 60 noted
  status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[]
  p8-compare-reproof.json 本体："status": "CLEAN", "missing": [], "extra": [], "uncertain": [], "keydiff": []
extract keys['73']='up'；keys['70'..'72']=['silence','socks','rights']；
  keys['79']='Children are speaking up this week.'；keys['150']='开放题'
```

## 7. keycheck（我的脚本 keycheck_reproof.py；源行：keycheck-reproof.log）

```
exact: 149/150  exceptions: [150]  mismatches: 0
KEYCHECK: PASS
（#150：registry 全文键 vs P8 印出 "开放题"，已知全文例外）
```

## 8. 150 题手验（我的脚本 dump_keyverify_reproof.py；源行：keyverify-reproof.txt）

```
records=150 ex/match/cloze/dlg/writing kinds: {'ex': 116, 'match': 20, 'cloze/dlg': 13, 'writing': 1}
registry 逐条断言 key/note 相等通过；150 行由我逐行读完：150/150 PASS。
分布：by page {1: 10, 2: 17, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 39}；
  by level {'A2': 62, 'B1': 66, 'B2': 22}
```

## 9. 印/网文字层逐页一致（交付件；源行：textlayers/print + textlayers/web，pdftotext 同参）

```
P1 IDENTICAL (4868 B)   P2 IDENTICAL (5983 B)   P3 IDENTICAL (5352 B)   P4 IDENTICAL (5807 B)
P5 IDENTICAL (4709 B)   P6 IDENTICAL (5615 B)   P7 IDENTICAL (6073 B)   P8 IDENTICAL (9728 B)
Q73：P5 文字层 "Speak ___: tell a teacher."（行 205）+ "to speak up" 译注；
     P8 文字层 "73. up"（行 352，印/网同行一致）。
```

## 10. 网 PDF scratch 重渲对比（源行：webpdf-reproof.log）

```
rc=0；WROTE scratch-reproof-en2/web-reproof.pdf: 2804279 bytes, 48135 text bytes
交付网 PDF：2804281 B（2 B 差，网 PDF 字节不可复现为已知特性；交付件未覆盖，SHA 终验不变）
重渲网 PDF 8 页文字层与交付印 PDF 逐页字节一致（textlayers/web-reproof/ vs textlayers/print/）。
```

## 11. P8 最小字号（源行：exec 实测，shipped p8-test.svg 的 font-size 属性）

```
spans: 255  min: 15.5  max: 46.0  below 9.75pt: 0  below 10pt: 0
```

## 12. creambox / box-title 真墨扫描（我的脚本 sweep_ink_reproof.py，PIL 真墨；源行：sweep-ink-reproof.log）

```
rc=0；OVERFLOW 计数：0
8 页全扫（p1-front … p8-test，50 条 box/title/bottom 记录行）
WORST title edge clearance: +5.5 px（p1-front, 'THE WEEK IN NUMBERS　数字看本周'）
WORST box bottom clearance: +2.9 px（p2-life, box y=1211.4，AND YOU?——修前已存在）
次紧 box 底：+11.0 px（P1 SEARCHES）；标题边次紧：+107.0 px
PNG 渲染证据：pngs/*.png（1950 px，由交付 SVG 渲染）
```

## 13. SAY IT 在框内（我的脚本 sweep_sayit_reproof.py，P2 PNG；源行：sweep-sayit-reproof.log）

```
cx=299 label 'The counting continues.': ink_w=239 panel=280 over/side(ink)=-20.5 ok
cx=299 sub '计票还在继续。': ink_w=128 panel=280 over/side(ink)=-76.0 ok
cx=750 label 'The new Congress meets in January.': ink_w=358 panel=380 over/side(ink)=-11.0 ok
cx=750 sub '新国会在一月开会。': ink_w=168 panel=380 over/side(ink)=-106.0 ok
cx=1200 label 'Happy Thanksgiving!': ink_w=213 panel=280 over/side(ink)=-33.5 ok
cx=1200 sub '感恩节快乐！': ink_w=107 panel=280 over/side(ink)=-86.5 ok
vocab list over_RIGHT: -121.0 / -107.0 / -65.0 / -25.0（to certify / a runoff / sworn in / a turkey）
note para lines over_RIGHT: -6.0 / -68.0 / -134.0 / -1.0（line 3 墨至 1861 vs RIGHT 1862，与基线同）
```

## 14. 8 页逐页目视（交付印 PDF，pdftoppm 100 dpi；源行：pages/p-1.png … p-8.png）

```
P1 干净：masthead、头条、SEARCHES、TRY IT NOW、IN THIS ISSUE、LIGHTNING QUIZ 无溢出。
P2 干净：SAY IT 三面板在框内；AND YOU? 末行在框内；Q11–27 排版正常。
P3 干净：COMING SOON、Q28–45、配对 38–41、Rousseau 图注正常。
P4 干净：Ashes 回顾文与 Q46–63 一致（"final score was 4–1" 与 Q125 呼应）；W. G. Grace 图正常。
P5 干净：Q73 "Speak ___: tell a teacher." 目视确认；Q70–72、74–77、Q79 完好；SPEAK UP 框正常。
P6 干净：选票 ☐ 正常；READ THE CHART 数字 254/162/19、20/13/2、flips 7、governors 5 与正文一致。
P7 干净：WORDS/GRAMMAR/GOLDEN SENTENCES/ERROR CLINIC、Q100–111、READERS' CORNER 正常。
P8 干净：CLOZE/MCQ/READING/SENTENCES/TRANSLATION/WORDS/DIALOGUE、WRITING 范文、
     ANSWERS 区目视见 "73. up"（第 5 版答案行）；无溢出。
```

## 15. D5 字体（只记录，不判；源行：fonts-d5-reproof.txt，pdffonts 交付印 PDF）

```
5 个 family：Newsreader（Regular/Bold/Italic）、NotoSansCJKsc、NotoSerifCJKsc、
UnifrakturMaguntia、DejaVuSans（仅 P6，object 175，4 个 ☐ 选票框）；
全部 embedded + subset；与 fix1 记录一致。
网 PDF 为 Lucerna* 子集化同款字体（LucernaNewsreader / LucernaNotoSansCJKSC /
LucernaNotoSerifCJKSC / LucernaUnifrakturMaguntia / LucernaDejaVuSans）。
```

## 16. 产物清单（scratch-reproof-en2/）

```
PROOF-NOTE.md / GATE-LOG.md（本文件）
run-reproof.log / render-reproof.log / freeze-reproof.log / freeze-reproof/
occlusion-reproof.log / occlusion-reproof.json
p8-extract-reproof.log / p8-extract-reproof.json / p8-compare-reproof.log / p8-compare-reproof.json
keycheck_reproof.py / keycheck-reproof.log
dump_keyverify_reproof.py / keyverify-reproof.txt / keyverify-reproof.json
textlayers/print/ + textlayers/web/ + textlayers/web-reproof/（逐页 pdftotext）
sweep_ink_reproof.py / sweep-ink-reproof.log / pngs/*.png
sweep_sayit_reproof.py / sweep-sayit-reproof.log
web-reproof.pdf / webpdf-reproof.log
pages/p-1.png … p-8.png（目视渲染）
work/（core-en 隔离副本：run/render 重建产物，交付三件 SHA 终验未动）
fonts-d5-reproof.txt
```
