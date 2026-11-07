# -*- coding: utf-8 -*-
"""W46 ES x JA transform: explanation layer into Japanese (W43/W45 ESxJA precedent).
JP face + kinsoku transplant in svglib.py. bridge() -> expl(). Type names translated;
P8 check == "作文". Badge: y=372 slot, 19.5pt. Separators '— N ページ —'.
Declared unchanged shared-kanji items: 文化, el cementerio 墓地, cementerio = 墓地,
himno = 国歌, 原形, letter attribution （ejemplo, escrito por la redacción）, frozen Spanish letter body."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from engine import apply_pairs, residue_scan

BS = ["bslib4.py"]; C12 = ["content12.py"]; C34 = ["content34.py"]
C56 = ["content56.py"]; C7 = ["content7.py"]; C8 = ["content8.py"]
ALL = ["bslib4.py", "content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]

KINSOKU = '''    if cur.strip():
        lines.append(cur.rstrip())
    # kinsoku shori (JA build): a line must not START with closing punctuation —
    # pull the previous line's last character down (oidashi). Line count unchanged.
    NO_START = "。、，．！？：；）」』】ー…‥・ぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮ"  # FIX-W45-ESJA-1: small kana added (kinsoku: 捨て仮名 must not start a line)
    pre_w = [text_w(ln, kind, bold, size) for ln in lines]
    for i in range(1, len(lines)):
        while lines[i] and lines[i][0] in NO_START and len(lines[i - 1]) > 1:
            lines[i] = lines[i - 1][-1] + lines[i]
            lines[i - 1] = lines[i - 1][:-1].rstrip()
    # Seam repair (2026-10-21 core patch — JA P7 glyph overprint): oidashi
    # never re-measures the receiving line, and a line starting with a
    # NO_START chain (e.g. 』!。) pulls one glyph per pass, so the receiving
    # line can end far past max_w. A wrapped line may legitimately sit in
    # the gutter (SEAM_SLACK: the 4-column grid's pitch minus column width),
    # but once its ink crosses the pitch it overprints the neighbouring
    # column's first glyph. Repair ONLY such seam-crossing lines that
    # oidashi itself grew (pre_w <= max_w + SEAM_SLACK): shed trailing
    # glyphs to the head of the next line until the line fits max_w again,
    # cascading forward. A NO_START glyph is shed together with the glyph
    # before it, so the next line never starts with one.
    cascade = False
    for i in range(len(lines)):
        if text_w(lines[i], kind, bold, size) <= max_w + SEAM_SLACK:
            cascade = False
            continue
        if not cascade and pre_w[i] > max_w + SEAM_SLACK:
            continue  # unbreakable token, already seam-crossing pre-kinsoku
        cascade = True
        while text_w(lines[i], kind, bold, size) > max_w and len(lines[i]) > 1:
            if lines[i][-1] in NO_START and len(lines[i]) > 2:
                move, lines[i] = lines[i][-2:], lines[i][:-2]
            else:
                move, lines[i] = lines[i][-1], lines[i][:-1]
            if i + 1 < len(lines):
                lines[i + 1] = move + lines[i + 1]
            else:
                lines.append(move)
        lines[i] = lines[i].rstrip()
    return lines'''

PAIRS = [
    # ---- svglib.py: JP face + kinsoku + seam slack (W45 ESxJA transplant) ----
    ('if f.getname()[0].endswith("SC"):', 'if f.getname()[0].endswith("JP"):', ["svglib.py"]),
    ('"Noto Serif CJK SC"', '"Noto Serif CJK JP"', ["svglib.py"]),
    ('"Noto Sans CJK SC"', '"Noto Sans CJK JP"', ["svglib.py"]),
    ('''    if cur.strip():
        lines.append(cur.rstrip())
    return lines''', KINSOKU, ["svglib.py"]),
    ('INK = "#28251d"; OLIVE = "#3e4c2a"; GOLD = "#b3a06a"; PAPER = "#f7f1e2"',
     '''# Seam slack of the 4-column grid (pitch 462 = column width 434 + gutter 28):
# a wrapped line's ink may sit in the gutter but must never cross the pitch.
SEAM_SLACK = 28

INK = "#28251d"; OLIVE = "#3e4c2a"; GOLD = "#b3a06a"; PAPER = "#f7f1e2"''', ["svglib.py"]),
    # ---- bslib4 ----
    ('"La Lucerna · 西班牙语周报 VOL.3 · LUCERNA SPANISH WEEKLY"',
     '"La Lucerna · スペイン語週刊 VOL.3 · 本文はスペイン語 · 解説は日本語"', BS),
    ('第 {n} 版 / 共 {total} 版', '{n} ページ（全 {total} ページ）', BS),
    ('译注｜', '解説 — ', BS),
    ('    def bridge(self, s, size=20.5, gap=9, fill=GREY):',
     '    def expl(self, s, size=20.5, gap=9, fill=GREY):', BS),
    ('.bridge(', '.expl(', ALL),
    ('p.text(975, 372, "EL PERIÓDICO SEMANAL PARA APRENDER — LA VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "スペイン語テキスト · 日本語の解説 — 日本語読者のための版", 19.5, "sans", True, BRICK, anchor="middle")', C12),
    ('CADA SEMANA EN ESPAÑOL · 每周一期 · 读西班牙人正在读的西班牙语',
     'CADA SEMANA EN ESPAÑOL · 毎週一号 · スペイン人が読んでいるスペイン語を読む', C12),
    ('西 班 牙 语 周 报 · VOL.3 · LA HUELGA · LA CAMPAÑA · LA ROJA',
     'ス ペ イ ン 語 週 刊 · VOL.3 · LA HUELGA · LA CAMPAÑA · LA ROJA', C12),
    ('周五 13 日竞选开始 · 周三 11 日大罢工', '29-Nまであと20日 · 住宅が選挙戦を決める', C12),
    ('本期头条 · 详见第 2、6 版', '今号のトップ · 詳しくは2・6ページ', C12),
    ('weekly-report-w46-es-core', 'weekly-report-w46-es-ja', ALL + ["render.py"]),
    ('size=19, gap=3', 'size=18.5, gap=2', ["content56.py"]),
    ('La-Lucerna-VOL3.pdf', 'La-Lucerna-VOL3-JA.pdf', ["render.py"]),
    ('La-Lucerna-VOL3-web.pdf', 'La-Lucerna-VOL3-JA-web.pdf', ["render.py"]),
    ('af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)',
     'af.para(f"— {pg} ページ —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)', C8),
    # ---- type names (translated, W45 JA precedent) + P8 check ----
    ('"完成句子"', '"文の完成"', ALL),
    ('"单选"', '"選択問題"', ALL),
    ('"词汇配对"', '"単語のペア"', ALL),
    ('"判断对错"', '"正誤判断"', ALL),
    ('"造句"', '"文を作る"', ALL),
    ('"句型转换"', '"文の書き換え"', ALL),
    ('"完形单选"', '"穴埋め選択"', ALL),
    ('"翻译"', '"翻訳"', ALL),
    ('"写作"', '"作文"', ALL),
    ('== "写作"', '== "作文"', ["content8.py"]),
    # ---- content12 ----
    ('讲解｜la huelga general 大罢工 · la campaña electoral 竞选活动 · el voto por correo 邮寄投票 · la jornada de reflexión 投票前静默日。',
     'la huelga general＝ゼネスト · la campaña electoral＝選挙戦 · el voto por correo＝郵便投票 · la jornada de reflexión＝投票前日（静粛日）。', C12),
    ('20 — días faltan el lunes 9 para las elecciones del domingo 29（距 29 日大选 20 天）',
     '20 — días faltan el lunes 9 para las elecciones del domingo 29（29日の投票日まであと20日）', C12),
    ('24 — horas dura la huelga general del miércoles 11 de noviembre（11 月 11 日大罢工持续 24 小时）',
     '24 — horas dura la huelga general del miércoles 11 de noviembre（11月11日のゼネストは24時間）', C12),
    ('91,4 — % que pide más vivienda pública, según el CIS de octubre（CIS 住房晴雨表数据）',
     '91,4 — % que pide más vivienda pública, según el CIS de octubre（CIS住宅調査・10月）', C12),
    ('LA NOTICIA · 头条', 'LA NOTICIA · トップ記事', C12),
    ('LA SEMANA EN CIFRAS · 数字看本周', 'LA SEMANA EN CIFRAS · 今週の数字', C12),
    ('AHORA TÚ · 即学即练', 'AHORA TÚ · すぐ練習', C12),
    ('本周五大看点 · Para entender la semana', '五大見どころ · Para entender la semana', C12),
    ('五大看点，不编数字：全在本期里讲清。', '五つのポイント。数字のねつ造なし。', C12),
    ('EN ESTA EDICIÓN · 本期目录', 'EN ESTA EDICIÓN · 今号の目次', C12),
    ('“大罢工”：全体劳动者同一天停工 24 小时。', '「huelga general」：みんなが一日休む。', C12),
    ('BREVES · 快讯', 'BREVES · 短報', C12),
    ('QUIZ RELÁMPAGO · 闪电问答', 'QUIZ RELÁMPAGO · クイズ', C12),
    ('读头版，选出正确答案 · 答案见第 8 版', 'トップ記事を読んで、正しい答えを選ぼう · 答えは8ページ', C12),
    ('VIDA · 生活', 'VIDA · 暮らし', C12),
    ('NIVEL A2 · El miércoles 11, huelga general · 11 月 11 日周三大罢工',
     'NIVEL A2 · El miércoles 11, huelga general · 11月11日（水）ゼネスト', C12),
    ('EL CALENDARIO · 本周日历', 'EL CALENDARIO · 今週の予定', C12),
    ('（周一国家队集结；邮寄选票材料开始寄出）', '（月曜：代表合宿開始。郵便投票の書類が届き始める）', C12),
    ('（周二罢工前最后准备日）', '（火曜：スト前日の最終準備）', C12),
    ('（周三大罢工；圣马丁节）', '（水曜：ゼネスト。聖マルティンの祝日）', C12),
    ('（周四欧国联：捷克对西班牙）', '（木曜：ネーションズリーグ、チェコ対スペイン）', C12),
    ('（周五零点竞选正式开始）', '（金曜：午前0時に選挙戦が始まる）', C12),
    ('（周六联邦杯决赛在塞斯陶）', '（土曜：セスタオで連盟杯決勝）', C12),
    ('（周日欧国联：西班牙对英格兰）', '（日曜：ネーションズリーグ、スペイン対イングランド）', C12),
    ('la huelga 罢工 · el sindicato 工会 · el salario 工资 · el alquiler 租金 · los servicios mínimos 最低服务保障。',
     'la huelga＝ストライキ · el sindicato＝労働組合 · el salario＝給料 · el alquiler＝家賃 · los servicios mínimos＝最低限のサービス。', C12),
    ('11 月 11 日周三你做什么：罢工、上班还是待在家里？你最担心什么：工资、住房还是物价？写两句西班牙语寄给编辑部。',
     '11月11日（水）、あなたは何をしますか。ストに参加しますか、働きますか、家にいますか。一番心配なのは何ですか。給料、住まい、物価。スペイン語で2文書いて編集部へ。', C12),
    ('¿Y TÚ? · 说说你自己', '¿Y TÚ? · あなたは？', ALL),
    ('LOS DÍAS DE LA SEMANA · 这样说日期', 'LOS DÍAS DE LA SEMANA · 日付の言い方', C12),
    ('lunes 9 – domingo 15 de noviembre · 11 月 9 日周一至 15 日周日',
     'lunes 9 – domingo 15 de noviembre · 11月9日（月）から15日（日）まで', C12),
    ('EJERCICIOS · 第 2 版练习', 'EJERCICIOS · 2ページの練習', C12),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', '答えは8ページ · レベル混合の問題もあります。番号で探してください', ALL),
    ('用正确的日期形式补全句子。', '正しい日付の形で文を完成させよう。', C12),
    ('补全动词的现在时形式。', '動詞を現在形で補おう。', C12),
    ('读第 2 版文章，选出正确答案。', '2ページの記事を読んで、正しい答えを選ぼう。', C12),
    ('竞选 11 月 13 日周五开始', '選挙戦は11月13日（金）に始まる', C12),
    ('大罢工在 11 月 11 日周三', 'ゼネストは11月11日（水）', ALL),
    ('大选在 11 月 29 日周日', '総選挙は11月29日（日）', C12),
    ('邮寄投票须在 19 日前申请', '郵便投票は19日までに申請する', ALL),
    ('西班牙–英格兰周日 20:45 开球', 'スペイン対イングランド、日曜20:45キックオフ', C12),
    ('竞选持续 15 天', '選挙戦は15日間', C12),
    ('大选在 11 月 29 日', '総選挙は11月29日', ALL),
    ('大罢工持续 24 小时', 'ゼネストは24時間', C12),
    ('竞选 11 月 13 日开始', '選挙戦は11月13日に始まる', ALL),
    ('西班牙–英格兰周日 20:45', 'スペイン対イングランド、日曜20:45', C12),
    ('11 月 11 日周三', '11月11日（水）', C12),
    ('11 月 15 日周日', '11月15日（日）', C12),
    ('每月 1 号说 el uno', '1日は el uno と言う', C12),
    ('月份小写', '月は小文字で書く', C12),
    ('罢工口号是工资、住房、物价', 'ストのスローガンは給料・住まい・物価', C12),
    ('罢工后两天竞选开始', 'ストの2日後に選挙戦が始まる', C12),
    ('罢工日有最低服务保障', 'ストの日も最低限のサービスはある', C12),
    ('huelga=罢工 c', 'huelga=ストライキ c', C12),
    ('sindicato=工会 b', 'sindicato=労働組合 b', C12),
    ('salario=工资 a', 'salario=給料 a', C12),
    ('alquiler=租金 d', 'alquiler=家賃 d', C12),
    # ---- content34 ----
    ('A2 → B1 · San Martín, castañas y vino nuevo · 圣马丁节、栗子与新酒',
     'A2 → B1 · San Martín, castañas y vino nuevo · 聖マルティン、栗と新酒', C34),
    ('la capa 斗篷 · el mendigo 乞丐 · el veranillo 小阳春 · la gaita 风笛 · el magosto 栗子节。',
     'la capa＝マント · el mendigo＝物乞い · el veranillo＝小春日和 · la gaita＝バグパイプ · el magosto＝栗祭り。', C34),
    ('你吃过烤栗子吗？你的国家有“小阳春”吗？写两句寄来。',
     '焼き栗を食べたことがありますか。あなたの国にも「小春日和」のような言葉がありますか。2文書いて送ってください。', C34),
    ('EJERCICIOS · 第 3 版练习', 'EJERCICIOS · 3ページの練習', C34),
    ('读第 3 版文章，判断对错。', '3ページの記事を読んで、正しいか間違いか判断しよう。', C34),
    ('圣马丁节在 11 月 11 日周三', '聖マルティンの日は11月11日（水）', C34),
    ('马丁把斗篷分给乞丐', 'マルティンはマントを物乞いと分けた', C34),
    ('Humanitarios 节在阿斯图里亚斯，不在加利西亚', 'ウマニタリオス祭はアストゥリアス州で、ガリシア州ではない', C34),
    ('小阳春是秋中暖和的几天，不是夏天', '小春日和は秋の暖かい数日で、夏ではない', C34),
    ('圣马丁餐有 fabada、casadiellas 和 panchón', '聖マルティンの食事にはファバーダ、カサディエジャス、パンチョンがある', C34),
    ('马丁分开自己的斗篷 capa', 'マルティンは自分のマント（capa）を分けた', C34),
    ('mendigo = 乞丐', 'mendigo = 物乞い', C34),
    ('castañas asadas 烤栗子', 'castañas asadas = 焼き栗', C34),
    ('gaita = 风笛', 'gaita = バグパイプ', C34),
    ('veranillo de San Martín 小阳春', 'veranillo de San Martín = 聖マルティンの小春日和', C34),
    ('Humanitarios 节在 Moreda de Aller', 'ウマニタリオス祭はモレダ・デ・アジェールで開かれる', C34),
    ('puya del ramu 是拍卖祝福过的面包', 'puya del ramu は祝福されたパンの競売', C34),
    ('小阳春是秋中几天暖和天气', '小春日和は秋の数日間の暖かい天気', C34),
    ('圣马丁节之后大选在 11 月 29 日', '聖マルティンの日の後、総選挙は11月29日', C34),
    ('动词第二位', '動詞は2番目', C34),
    ('时间在前，动词第二', '時間が先、動詞は2番目', C34),
    ('地点在前，动词第二', '場所が先、動詞は2番目', C34),
    ('间接疑问用 si', '間接疑問文には si', C34),
    ('用方框里的词填空。', '枠の中の言葉で空所を補おう。', C34),
    ('选出正确答案。', '正しい答えを選ぼう。', C34),
    ('把词组成正确的句子。', '言葉を並べて正しい文を作ろう。', C34),
    ('DEPORTE · 体育', 'DEPORTE · スポーツ', C34),
    ('NIVEL B1 · Praga el jueves, Inglaterra el domingo · 周四布拉格，周日英格兰',
     'NIVEL B1 · Praga el jueves, Inglaterra el domingo · 木曜はプラハ、日曜はイングランド', C34),
    ('la fase de grupos 小组赛 · el seleccionador 国家队主教练 · la lista 征召名单 · la plaza 名额 · el amistoso 友谊赛。',
     'la fase de grupos＝グループリーグ · el seleccionador＝代表監督 · la lista＝招集リスト · la plaza＝枠 · el amistoso＝親善試合。', C34),
    ('周日 20:45 你看哪一场？A3 小组谁第一：西班牙还是英格兰？写两句西班牙语寄来。',
     '日曜20:45、どの試合を見ますか。A3組の1位はスペインとイングランドのどちらでしょう。スペイン語で2文書いて送ってください。', C34),
    ('LA LIGA DE NACIONES · GRUPO A3 · 欧国联 A3 组赛程',
     'LA LIGA DE NACIONES · GRUPO A3 · ネーションズリーグA3組の日程', C34),
    ('EJERCICIOS · 第 4 版练习', 'EJERCICIOS · 4ページの練習', C34),
    ('读第 4 版文章，选出正确答案。', '4ページの記事を読んで、正しい答えを選ぼう。', C34),
    ('西班牙在 A3 组', 'スペインはA3組', C34),
    ('周四对捷克，周日对英格兰', '木曜はチェコ戦、日曜はイングランド戦', C34),
    ('两场比赛都是 20:45', '2試合とも20:45開始', C34),
    ('周日比赛在 Metropolitano', '日曜の試合はメトロポリターノ', C34),
    ('U21 周五对日本', 'U21は金曜に日本と対戦', C34),
    ('más + importante（小组第一更重要）', 'más + importante（組1位のほうが大事）', C34),
    ('muchísimos aficionados 球迷很多', 'muchísimos aficionados = ものすごく多くのファン', C34),
    ('malo 的比较级是 peor', 'malo の比較級は peor', C34),
    ('bueno 的比较级是 mejor', 'bueno の比較級は mejor', C34),
    ('ir 的过去时是 fueron', 'ir の過去形は fueron', C34),
    ('用括号里词的比较级或 -ísimo 形式填空。', 'かっこ内の言葉の比較級か -ísimo 形で補おう。', C34),
    ('把句子改成过去时（pretérito indefinido）。', '文を過去形（pretérito indefinido）に直そう。', C34),
    ('fase de grupos=小组赛 b', 'fase de grupos=グループリーグ b', C34),
    ('seleccionador=主教练 c', 'seleccionador=代表監督 c', C34),
    ('lista=名单 d', 'lista=招集リスト d', C34),
    ('amistoso=友谊赛 a', 'amistoso=親善試合 a', C34),
]

from t_ja2 import PAIRS2  # noqa: E402
