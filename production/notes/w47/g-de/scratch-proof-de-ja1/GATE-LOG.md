# GATE-LOG — proof1 de-ja (independent re-run, 2026-11-11)

run started 2026-11-11 09:10:08 UTC
== probe ==
9daeafb9864cf43055ae93beb0afd6c7d144bfa4
probe RC=0
== SHA ==
f412f930242d16c87a7fb783506f6e92e5020a40e323edfdb1243dfd82db459d  Die-Lucerna-VOL4-de-ja.pdf
29f65fec5681e46f5b927171163c5d66559e61ed275d998583653574d8e8294a  Die-Lucerna-VOL4-de-ja-web.pdf
a59f784705bec4329b7dfa19321256c2469ab7680212302481876fc96f957f69  2026-w47-de-ja.text.md
== occlusion ==
selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
/home/hatch/workspace/weekly-git/production/2026-w47/2026-w47-de-ja/svg: 0 flags 
occlusion RC=0
== p8 extract ==
/home/hatch/workspace/weekly-git/production/2026-w47/2026-w47-de-ja/svg/p8-uebungen.svg: noted set = 150 of 150 (parse: joined)
  set: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
p8extract RC=0
== p8 compare ==
core    /home/hatch/workspace/weekly-git/production/2026-w47/core-de/svg/p8-uebungen.svg: 150 noted
edition /home/hatch/workspace/weekly-git/production/2026-w47/2026-w47-de-ja/svg/p8-uebungen.svg: 150 noted
status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]
p8compare RC=0
== freeze diff ==
p1: +37 strings / -47 strings; CJK core 189 -> edition 286; added CJK chars: 243 {'週': 6, '刊': 3, 'ド': 9, 'イ': 11, 'ツ': 8, 'が': 1, '読': 2, 'む': 1, '語': 8, 'ブ': 4}
p2: +32 strings / -30 strings; CJK core 221 -> edition 293; added CJK chars: 229 {'\u3000': 1, 'い': 4, 'め': 2, 'と': 3, 'り': 3, 'の': 7, 'プ': 1, 'ロ': 1, 'テ': 2, 'ス': 2}
p3: +45 strings / -41 strings; CJK core 208 -> edition 354; added CJK chars: 312 {'\u3000': 1, '文': 5, 'ク': 7, 'リ': 8, 'ス': 11, 'マ': 5, 'と': 1, 'か': 3, 'な': 2, '週': 2}
p4: +22 strings / -21 strings; CJK core 174 -> edition 224; added CJK chars: 180 {'\u3000': 1, 'ス': 3, 'ポ': 1, 'ー': 10, 'ツ': 4, '結': 2, 'と': 3, 'リ': 3, 'グ': 2, '復': 1}
p5: +39 strings / -38 strings; CJK core 210 -> edition 309; added CJK chars: 269 {'\u3000': 1, '若': 1, '者': 1, 'ア': 2, 'ド': 5, 'ベ': 3, 'ン': 4, 'ト': 10, 'カ': 2, 'レ': 4}
p6: +33 strings / -34 strings; CJK core 243 -> edition 307; added CJK chars: 237 {'\u3000': 1, '掘': 1, 'り': 3, '静': 1, 'か': 6, 'な': 4, '週': 3, '間': 2, 'と': 1, '家': 2}
p7: +62 strings / -64 strings; CJK core 434 -> edition 523; added CJK chars: 412 {'\u3000': 1, '言': 1, '語': 5, '今': 5, '週': 7, 'の': 26, '文': 1, 'と': 4, '間': 7, '違': 4}
p8: +157 strings / -140 strings; CJK core 1434 -> edition 1709; added CJK chars: 1112 {'\u3000': 1, '練': 1, '習': 1, 'と': 8, 'え': 4, '最': 7, '終': 1, 'テ': 5, 'ス': 19, 'ト': 20}
TOTAL added CJK characters: 2994
freeze RC=0
== freeze diff --strict-cjk (expected RC=1 by design: JA layer adds CJK) ==
STRICT-CJK FAIL: edition adds CJK characters the core does not have
p1: +37 strings / -47 strings; CJK core 189 -> edition 286; added CJK chars: 243 {'週': 6, '刊': 3, 'ド': 9, 'イ': 11, 'ツ': 8, 'が': 1, '読': 2, 'む': 1, '語': 8, 'ブ': 4}
p2: +32 strings / -30 strings; CJK core 221 -> edition 293; added CJK chars: 229 {'\u3000': 1, 'い': 4, 'め': 2, 'と': 3, 'り': 3, 'の': 7, 'プ': 1, 'ロ': 1, 'テ': 2, 'ス': 2}
p3: +45 strings / -41 strings; CJK core 208 -> edition 354; added CJK chars: 312 {'\u3000': 1, '文': 5, 'ク': 7, 'リ': 8, 'ス': 11, 'マ': 5, 'と': 1, 'か': 3, 'な': 2, '週': 2}
p4: +22 strings / -21 strings; CJK core 174 -> edition 224; added CJK chars: 180 {'\u3000': 1, 'ス': 3, 'ポ': 1, 'ー': 10, 'ツ': 4, '結': 2, 'と': 3, 'リ': 3, 'グ': 2, '復': 1}
p5: +39 strings / -38 strings; CJK core 210 -> edition 309; added CJK chars: 269 {'\u3000': 1, '若': 1, '者': 1, 'ア': 2, 'ド': 5, 'ベ': 3, 'ン': 4, 'ト': 10, 'カ': 2, 'レ': 4}
p6: +33 strings / -34 strings; CJK core 243 -> edition 307; added CJK chars: 237 {'\u3000': 1, '掘': 1, 'り': 3, '静': 1, 'か': 6, 'な': 4, '週': 3, '間': 2, 'と': 1, '家': 2}
p7: +62 strings / -64 strings; CJK core 434 -> edition 523; added CJK chars: 412 {'\u3000': 1, '言': 1, '語': 5, '今': 5, '週': 7, 'の': 26, '文': 1, 'と': 4, '間': 7, '違': 4}
p8: +157 strings / -140 strings; CJK core 1434 -> edition 1709; added CJK chars: 1112 {'\u3000': 1, '練': 1, '習': 1, 'と': 8, 'え': 4, '最': 7, '終': 1, 'テ': 5, 'ス': 19, 'ト': 20}
TOTAL added CJK characters: 2994
freeze-strict RC=1

== freeze_direct (real tool) ==
source files core: {'bslib4.py': 101, 'content12.py': 359, 'content34.py': 351, 'content56.py': 370, 'content7.py': 201, 'content8.py': 264, 'render.py': 13, 'run.py': 9, 'svglib.py': 721, 'verify.py': 167}
source files edition: {'bslib4.py': 100, 'content12.py': 359, 'content34.py': 351, 'content56.py': 370, 'content7.py': 201, 'content8.py': 264, 'render.py': 13, 'run.py': 9, 'svglib.py': 730, 'verify.py': 167}
source literals: core=2556 edition=2564 removed=516 added=524
unaccounted removed: 1; unaccounted added: 3
  REMOVED x1: 'Noto Serif CJK SC'
  ADDED x1: 'JP'
  ADDED x1: 'Noto Sans CJK JP'
  ADDED x1: 'Noto Serif CJK JP'
  p1: frozen=144 (core 191 / edition 181) sha8=b01ba1b1 PASS
  p2: frozen=164 (core 194 / edition 196) sha8=2db0dd83 PASS
  p3: frozen=200 (core 241 / edition 245) sha8=2dd3b3f2 PASS
  p4: frozen=166 (core 187 / edition 188) sha8=df1bebf7 PASS
  p5: frozen=179 (core 217 / edition 218) sha8=e7b235f9 PASS
  p6: frozen=173 (core 207 / edition 206) sha8=89156519 PASS
  p7: frozen=163 (core 227 / edition 225) sha8=b854370f PASS
  p8: frozen=183 (core 323 / edition 340) sha8=1c855c30 PASS
source level: FAIL; rendered: 8/8
wrote /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-de-ja1/freeze-direct.json
freeze_direct RC=1

== boxtitle ==
[PASS] 'DIE STILLE WOCHE\u3000静かな一週間' sz=24 w=387.6 budget=400.5
[PASS] 'WEIHNACHTSWÖRTER\u3000聖誕' sz=24 w=333.4 budget=400.5
[PASS] 'DER TIPP\u3000編集部のヒント' sz=24 w=300.7 budget=400.5
[PASS] 'ADVENTSWÖRTER\u3000待降節の言葉' sz=24 w=379.4 budget=400.5
[PASS] 'DER WERKZEUGKASTEN\u3000道具箱' sz=23 w=361.9 budget=400.5
[PASS] 'LESERBRIEFE\u3000読者の手紙' sz=23 w=290.3 budget=400.5
[PASS] 'NOCH EIN WORT\u3000もう一言' sz=22 w=286.5 budget=400.5
box titles: 7/7 fit
boxtitle RC=0

== keycheck ==
P1 saved, exercises so far: 10
P2 col3 box1 ends 435.59000000000003
P2 col3 box2 ends 697.1800000000001
P2 col3 box3 ends 893.71
P2 col3 box4 ends 1155.3
P2 saved, exercises so far: 28
P3 image at 1020 ends 1443
P3 col3 facts ends 435.59000000000003
P3 col3 vocab ends 887.77
P3 col3 undsie ends 1084.3
P3 col3 ends 1218.83
P3 saved, exercises so far: 46
P4 col3 ends 966.53
P4 saved, exercises so far: 64
P5 col3 facts ends 435.59000000000003
P5 col3 vocab ends 887.77
P5 col3 undsie ends 1084.3
P5 col3 image ends 1523.3
P5 saved, exercises so far: 82
P6 col3 numbers ends 602.66
P6 col3 ends 798.48
P6 saved, exercises so far: 100
P7 image ends 1266 (A2 flow ended 1000 )
P7 col3 ends 1195.0
P7 saved, exercises so far: 112
P8 image height 140
P8 battery ends col3 1000 | image ends 1252
P8 saved, TOTAL exercises: 150
REG entries: 150; p8extract keys: 150
exact match: 149/150
  MISMATCH n=150 page=8 type=作文: key='自由課題 — 枠のポイントに従おう' extracted='自由課題'
wrote /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-de-ja1/keycheck-150.json
keycheck RC=0
